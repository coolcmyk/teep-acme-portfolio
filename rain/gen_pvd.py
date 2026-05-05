#!/usr/bin/env python3
"""Generate PVD for any set of VTP files in a directory."""
import os, re, sys
from collections import defaultdict

d = sys.argv[1] if len(sys.argv) > 1 else "/home/kyo/ws/teep/ACME/rain/results/rain-ground-3d"
dt = 1e-4  # time step

vtp_by_dataset = defaultdict(dict)
for f in sorted(os.listdir(d)):
    m = re.match(r'([a-z]+)(\d{4,5})\.vtp', f)
    if m:
        name, step = m.group(1), int(m.group(2))
        vtp_by_dataset[name][step] = f

for dataset, files in vtp_by_dataset.items():
    steps = sorted(files.keys())
    pvd = os.path.join(d, f"{dataset}.pvd")
    with open(pvd, "w") as fh:
        fh.write('<?xml version="1.0"?>\n')
        fh.write('<VTKFile type="Collection" version="0.1" byte_order="LittleEndian">\n')
        fh.write('  <Collection>\n')
        for s in steps:
            fh.write(f'    <DataSet timestep="{s*dt:.6f}" group="" part="0" file="{files[s]}"/>\n')
        fh.write('  </Collection>\n')
        fh.write('</VTKFile>\n')
    t0, t1 = steps[0]*dt, steps[-1]*dt
    print(f"  {dataset}.pvd  ({len(steps)} frames, {t0:.2f}s → {t1:.2f}s)")
