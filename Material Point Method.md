# Material Point Method

The Material Point Method (MPM) is an extension of the FLIP (Fluid-Implicit-Particle) particle-in-cell method that combines Lagrangian material points with an Eulerian background grid. It was developed to handle problems involving large deformations, such as hypervelocity impact on asteroids.

## Lagrangian Material Points

Material points are the core data-carrying entities in MPM. Each point permanently holds all physical properties:

- Mass
- Density
- Position
- Velocity
- Stress tensor
- Strain tensor
- Internal energy
- State variables (e.g., damage, plasticity history)

Because these history variables reside permanently on the material points, **no advective remapping** is ever needed — a key distinction from Arbitrary Lagrangian-Eulerian (ALE) methods.

## Eulerian Background Grid

The background grid is a regular, fixed grid that is **regenerated each timestep** and serves as a temporary computational scratchpad. It only exists for the duration of one time step:

1. Mass and momentum are mapped from material points to grid nodes
2. Momentum equations are solved on the grid nodes
3. Positions, velocities, and states are interpolated back to material points
4. The deformed grid is discarded and a fresh regular grid is created

## Two-Phase Process

### Lagrangian Phase
Material points move with the deforming grid. Their positions, velocities, and internal states (stress, strain, energy) are updated based on the grid solution.

### Eulerian Phase
The deformed grid is fully discarded. A new, regular, undeformed grid is reset for the next time step. This avoids the mesh distortion and entanglement problems that plague purely Lagrangian finite element methods in large-deformation regimes.

## Core Advantages

- **Merges Lagrangian and Eulerian descriptions**: material points track history without diffusion, while the grid handles large deformations without tangling
- **Minimizes numerical dissipation**: no advective remeshing or remapping
- **Speeds up neighbor searching**: the regular grid provides O(1) neighbor lookups, unlike SPH which requires expensive pairwise searches
- **Automatic mass conservation**: mass is permanently assigned to material points and never changes
- **History variables strictly conserved** on material points without advective smearing

## Standard Discretization

In 3D, the standard configuration uses **8 material points per active grid cell** (2×2×2 arrangement). This provides a good balance between resolution and computational cost.

## Codebase

This work uses **MPM3D-F90**, an open-source Fortran 90 implementation, enhanced for planetary science applications with:

1. **Adaptive time-stepping** — dynamically adjusts Δt based on the CFL condition, critical for hypervelocity scenarios where velocities and sound speeds vary dramatically
2. **Advanced constitutive models** — for brittle geological materials (rock, regolith) including pressure-dependent plasticity, damage, and failure
3. **Code optimization** — parallelized and tuned for large-scale simulations

## References

Yan et al. (2026). *The Material Point Method (MPM) for simulating hypervelocity impact on asteroids.*

## Related Concepts

[[MPM Discretization]] | [[MPM Algorithm Steps]] | [[GIMP Method]] | [[Comparison with SPH]]
