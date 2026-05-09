# TEEP ACME Portfolio

**Concept maps + CB-Geo MPM rain-simulation proof-of-concept.**

Paper basis: *"Using the Material Point Method to Investigate Hypervelocity Asteroid Impacts"* (arXiv:2604.13136v1).

## Repo structure

| Path | Content |
|------|---------|
| `.obsidian/` | Obsidian vault config |
| `*.md` | 66 concept-map notes (MPM theory, material models, EOS, damage, asteroid science) |
| `Home.md` | Map of Content linking all notes |
| `rain/` | 3D rain-on-ground CB-Geo MPM simulation |
| `ref/` | Source paper (PDF) |

## Rain simulation quick start

### 1. Prerequisites

Ubuntu 24.04 packages:
```bash
sudo apt install -y cmake g++ libboost-all-dev libeigen3-dev libhdf5-dev libopenmpi-dev libomp-dev libvtk9-dev
```

### 2. Build CB-Geo MPM

```bash
git clone https://github.com/cb-geo/mpm.git /tmp/mpm
cd /tmp/mpm && mkdir build && cd build
cmake .. -DCMAKE_BUILD_TYPE=Release -DENABLE_KAHIP=OFF -DENABLE_MPI=OFF
make -j$(nproc)
```

The binary will be at `/tmp/mpm/build/mpm`.

### 3. Clone this repo & generate inputs

```bash
git clone https://github.com/coolcmyk/teep-acme-portfolio.git
cd teep-acme-portfolio/rain
python3 generate_inputs.py
```

### 4. Run the simulation

```bash
/tmp/mpm/build/mpm -f $(pwd)/ -i rain-ground-3d.json -p $(nproc)
```

Simulation: 20000 steps × 0.1 ms = 2 seconds physical time, ~5-15 minutes on 8 cores.
Output goes to `rain/results/rain-ground-3d/` (200 VTP frames + PVD wrappers).

### 5. Visualize in ParaView

```bash
paraview rain/results/rain-ground-3d/velocities.pvd
```

Or open any `.pvd` file (`velocities`, `stresses`, `strains`, `geometry`, `mesh`). Press **Play** to animate.

### Simulation details

- **Domain**: 2×2×3 m, 10×10×15 cells (0.2 m per cell)
- **Ground**: 1600 LinearElastic3D particles (E=5 GPa, ρ=3000 kg/m³), slab z=0..0.4 m
- **Rain**: 196 Newtonian3D drops (ρ=1000 kg/m³, ν=0.05 Pa·s), falling from z=1.5..2.8 m
- **Gravity**: 9.81 m/s² downward
- **Contacts**: Multi-material friction contact (μ=0.4) at ground surface; container-side walls

## Obsidian vault

Open the repo root as an Obsidian vault. All 66 notes interconnect via `[[WikiLinks]]` — start from `Home.md`.

## License

MIT
