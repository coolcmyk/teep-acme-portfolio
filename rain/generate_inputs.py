#!/usr/bin/env python3
"""Generate 3D rain + solid ground collision simulation for CB-Geo MPM.

Layout:
  - Domain: 2x2x3 m; cell size 0.2 m
  - Ground: LinearElastic slab z=0..0.4; nodes fixed inside ground
  - Rain:   Newtonian drops falling from z=1.0..2.8
  - Friction on ground surface nodes; multi-material contact enabled
"""
import json, os, random

BASE = os.path.dirname(os.path.abspath(__file__))

# === tunables ===
LX, LY, LZ = 2.0, 2.0, 3.0
CELL = 0.2
GRAVITY = [0.0, 0.0, -9.81]
DT = 1e-4
NSTEPS = 20000
OUTPUT_EVERY = 100
PPC = 2
GROUND_TOP = 0.4        # top Z of ground slab
RAIN_Z_MIN, RAIN_Z_MAX = 1.5, 2.8
RAIN_SPACING = 3        # 1=PPC-dense, 2=every-other, 3=every-third

NX, NY, NZ = int(LX/CELL), int(LY/CELL), int(LZ/CELL)
NNX, NNY, NNZ = NX+1, NY+1, NZ+1

# ---- mesh ----
nodes = []
nmap = {}
nid = 0
for iz in range(NNZ):
    for iy in range(NNY):
        for ix in range(NNX):
            nodes.append((ix*CELL, iy*CELL, iz*CELL))
            nmap[(ix, iy, iz)] = nid
            nid += 1

cells = []
for iz in range(NZ):
    for iy in range(NY):
        for ix in range(NX):
            cells.append([
                nmap[(ix,iy,iz)], nmap[(ix+1,iy,iz)], nmap[(ix+1,iy+1,iz)], nmap[(ix,iy+1,iz)],
                nmap[(ix,iy,iz+1)], nmap[(ix+1,iy,iz+1)], nmap[(ix+1,iy+1,iz+1)], nmap[(ix,iy+1,iz+1)],
            ])

with open(f"{BASE}/mesh-3d.txt","w") as f:
    f.write("! elementShape hexahedron\n! elementNumPoints 8\n")
    f.write(f"{len(nodes)}\t{len(cells)}\n")
    for x,y,z in nodes: f.write(f"{x:.6f}\t{y:.6f}\t{z:.6f}\n")
    for c in cells: f.write("\t".join(str(n) for n in c)+"\n")
print(f"Mesh  {len(nodes)} nodes  {len(cells)} cells")

# ---- ground particles (fill z=0..GROUND_TOP) ----
s = CELL/PPC
o = s/2
ground = []
giz_max = int(GROUND_TOP / s)
for iz in range(giz_max):
    for iy in range(NY*PPC):
        for ix in range(NX*PPC):
            ground.append((ix*s+o, iy*s+o, iz*s+o))

# ---- rain particles (z=RAIN_Z_MIN..RAIN_Z_MAX) ----
random.seed(42)
rain = []
riz_s, riz_e = int(RAIN_Z_MIN/s), int(RAIN_Z_MAX/s)
for iz in range(riz_s, riz_e):
    for iy in range(NY*PPC):
        for ix in range(NX*PPC):
            if ix % RAIN_SPACING != 0 or iy % RAIN_SPACING != 0 or iz % RAIN_SPACING != 0:
                continue
            x = ix*s+o + random.uniform(-s*0.15, s*0.15)
            y = iy*s+o + random.uniform(-s*0.15, s*0.15)
            z = iz*s+o + random.uniform(-s*0.15, s*0.15)
            if z <= RAIN_Z_MAX:
                rain.append((x, y, z))

print(f"Ground {len(ground)} particles  Rain {len(rain)} particles")

with open(f"{BASE}/particles-ground.txt","w") as f:
    f.write(f"{len(ground)}\n")
    for x,y,z in ground: f.write(f"{x:.6f}\t{y:.6f}\t{z:.6f}\n")
with open(f"{BASE}/particles-rain.txt","w") as f:
    f.write(f"{len(rain)}\n")
    for x,y,z in rain: f.write(f"{x:.6f}\t{y:.6f}\t{z:.6f}\n")

# ---- velocity constraints: fix ground nodes + container walls ----
gnz = int(GROUND_TOP / CELL)
vc = []
for (ix,iy,iz), nd in nmap.items():
    if iz <= gnz:
        # ground layer: fix all 3 DOFs
        vc += [(nd,0,0.0),(nd,1,0.0),(nd,2,0.0)]
    else:
        # container walls: fix normal direction
        if ix == 0 or ix == NNX-1:
            vc.append((nd,0,0.0))
        if iy == 0 or iy == NNY-1:
            vc.append((nd,1,0.0))
with open(f"{BASE}/velocity-constraints.txt","w") as f:
    for nd, d, v in vc: f.write(f"{nd}\t{d}\t{v:.6f}\n")
print(f"Velocity constraints {len(vc)} (fixed ground nodes)")

# ---- friction: ground surface nodes (z at ground top) ----
fc = []
for (ix,iy,iz), nd in nmap.items():
    if iz == gnz:
        fc += [(nd,0,0.4),(nd,1,0.4)]
with open(f"{BASE}/friction-constraints.txt","w") as f:
    for nd, d, mu in fc: f.write(f"{nd}\t{d}\t{mu:.6f}\n")
print(f"Friction constraints {len(fc)}")

# ---- entity sets ----
with open(f"{BASE}/entity_sets.json","w") as f:
    json.dump({"particle_sets":[
        {"id":0,"set":list(range(len(ground)))},
        {"id":1,"set":list(range(len(rain)))},
    ]}, f, indent=2)

# ---- JSON config ----
cfg = {
    "title":"3D Rain Colliding with Solid Ground — CB-Geo MPM",
    "mesh":{
        "mesh":"mesh-3d.txt","entity_sets":"entity_sets.json",
        "io_type":"Ascii3D","check_duplicates":True,"isoparametric":False,
        "node_type":"N3D","cell_type":"ED3H8",
        "boundary_conditions":{
            "velocity_constraints":[{"file":"velocity-constraints.txt"}],
            "friction_constraints":[{"file":"friction-constraints.txt"}],
        },
    },
    "particles":[
        {"group_id":0,"generator":{"type":"file","material_id":0,"pset_id":0,
            "io_type":"Ascii3D","particle_type":"P3D","check_duplicates":True,
            "location":"particles-ground.txt"}},
        {"group_id":1,"generator":{"type":"file","material_id":1,"pset_id":1,
            "io_type":"Ascii3D","particle_type":"P3D","check_duplicates":True,
            "location":"particles-rain.txt"}},
    ],
    "materials":[
        {"id":0,"type":"LinearElastic3D","density":3000.0,
         "youngs_modulus":5.0e9,"poisson_ratio":0.2},
        {"id":1,"type":"Newtonian3D","density":1000.0,
         "bulk_modulus":2.2e6,"dynamic_viscosity":0.05},
    ],
    "material_sets":[
        {"material_id":0,"phase_id":0,"pset_id":0},
        {"material_id":1,"phase_id":0,"pset_id":1},
    ],
    "external_loading_conditions":{"gravity":GRAVITY},
    "analysis":{
        "type":"MPMExplicit3D","stress_update":"usf","locate_particles":True,
        "dt":DT,"uuid":"rain-ground-3d","nsteps":NSTEPS,"locate_particles":False,
        "boundary_friction":0.4,
        "damping":{"type":"Cundall","damping_ratio":0.05},
    },
    "post_processing":{
        "path":"results/",
        "vtk":["stresses","strains","velocities"],
        "output_steps":OUTPUT_EVERY,
    },
}
with open(f"{BASE}/rain-ground-3d.json","w") as f:
    json.dump(cfg, f, indent=2)

print(f"\nRun: /home/kyo/ws/teep/mpm/build/mpm -f {BASE}/ -i rain-ground-3d.json -p 8")
