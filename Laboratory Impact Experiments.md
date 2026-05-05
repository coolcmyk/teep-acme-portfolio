# Laboratory Impact Experiments

The experimental benchmark used to validate the MPM framework. Performed by Nakamura & Fujiwara (1991) in Japan.

### Experiment Setup (Fig. 4)
- **Target**: spherical basalt, 6 cm diameter, density 2.7 g/cm³, mass ~303 g
- **Projectile**: nylon sphere, 7 mm diameter, mass 0.213 g, density 1.18 g/cm³
- **Impact velocity**: ~3.2 km/s
- **Impact angle**: α = 30° (measured from surface normal)
  - Offset by half the target radius perpendicular to velocity direction
- Off-axis impact (not head-on)

### Why This Benchmark?
- Fully measured kinetic aspects of fragments:
  - Cumulative mass distribution
  - Mass-velocity distribution
- Ideal for validating shock-physics codes
- Used to validate the original Bern SPH code (Benz & Asphaug, 1994)
- Established material parameters available

### Experimental Observations
- Core-shaped major remnant formed
- Power-law mass distribution for fragments > few mm
- Fragment velocity decreases with increasing fragment mass
- Largest fragment velocity: ~1.35 m/s
- Largest fragment mass: ~31% of target

### Simulations
- SPH: Benz & Asphaug (1994, 1995) — close agreement with experiments
- MPM: This paper — benchmarked against both experiments and SPH

Link to: [[Nominal Benchmark Case]], [[Cumulative Mass Distribution]], [[Mass Velocity Distribution]]
