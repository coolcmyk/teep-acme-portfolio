# Catastrophic Disruption

An impact event where the target body is completely shattered, with the largest surviving fragment comprising less than 50% of the original mass.

### Threshold
- Q*_D: specific impact energy (energy per unit mass) required for catastrophic disruption
- Depends on target size, composition, porosity, and internal structure
- Below threshold: cratering or shattering but body remains largely intact
- Above threshold: complete disruption → subsequent reaccumulation

### Phase 1: Fragmentation (Shock Physics)
- Timescale: seconds to minutes
- Modeled by hydrocodes (SPH, MPM, grid-based)
- Output: fragment size distribution, velocity field
- This is the phase addressed by the MPM framework

### Phase 2: Gravitational Reaccumulation
- Timescale: hours to days
- Modeled by N-body or DEM codes
- Input: fragmentation phase output
- Results in rubble-pile asteroids or asteroid families

### In This Paper
- High damage strength (~40 MPa) → NOT catastrophic → large coherent fragments survive
- Low damage strength (~0.4 MPa) → catastrophic → complete failure
- The survival of Eros-like fragments depends critically on Weibull parameters

Link to: [[Hypervelocity Impact]], [[Gravitational Reaccumulation]], [[Rubble Pile Asteroids]], [[Asteroid Families]]
