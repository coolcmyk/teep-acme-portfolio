# Gravitational Reaccumulation

The second phase of a catastrophic asteroid collision, where fragments generated during the impact regroup under their mutual gravity.

### Process
1. Impact fractures the parent body (shock physics phase)
2. Ejecta and fragments expand in a velocity field
3. Gravitational attraction between fragments causes reaccumulation
4. Results in rubble-pile bodies or asteroid families

### Computational Approach
- Fragmentation phase output (from SPH, MPM, etc.) → initial conditions
- N-body or DEM codes handle gravitational dynamics
- Long timescales (hours to days) compared to fragmentation (seconds)

### Key Publications
- Michel et al. (2001): First complete numerical reproduction of asteroid family formation via collision + reaccumulation
- Michel et al. (2002, 2003, 2004): Various material models and parent body structures
- Jiao et al. (2023): SPH-DEM coupling for rubble-pile impacts

### MPM's Role
The explicit fragment tracking capability of MPM makes it ideal for coupling with gravitational reaccumulation codes. Fragment shapes (not just masses and velocities) can be passed to the N-body phase, enabling studies of how irregular fragment shapes affect reaccumulation dynamics.

Link to: [[Catastrophic Disruption]], [[Rubble Pile Asteroids]], [[Asteroid Families]], [[Fragment Search Algorithm]]
