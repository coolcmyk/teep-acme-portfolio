# Critical Time Step

The critical time step $\Delta t_{cr}$ is the maximum allowable time step for stable explicit time integration in MPM, governed by the CFL (Courant-Friedrichs-Lewy) condition.

## Definition

$$\Delta t_{cr} = \frac{d_c}{\max_p(c_p + |\mathbf{v}_p|)}$$

Where:

| Symbol | Meaning |
|--------|---------|
| $\Delta t_{cr}$ | Critical (maximum stable) time step |
| $d_c$ | Edge length of the regular background grid cell |
| $c_p$ | Sound speed of material point $p$ |
| $\mathbf{v}_p$ | Velocity of material point $p$ |
| $\max_p$ | Maximum value taken over all material points in the domain |

## Physical Meaning

The CFL condition enforces that **information cannot travel more than one grid cell per time step**. This applies to two distinct physical mechanisms:

### 1. Advective Transport
$|\mathbf{v}_p|$ constrains material point movement: a particle should not traverse more than one cell in a single time step. If a particle moved further, it would "skip" grid nodes and lose the spatial resolution provided by the grid.

### 2. Wave Propagation
$c_p$ constrains stress wave propagation: a pressure or shear wave should not cross more than one cell in a single time step. The sound speed $c_p$ is the longitudinal wave speed for 3D solids, obtained from the equation of state (EOS):

$$c_p = \sqrt{\frac{K}{\rho}}$$

where $K$ is the bulk modulus from the EOS (e.g., Tillotson EOS, ANEOS).

## Which Constraint Dominates?

In different regimes, different terms dominate:
- **Hypervelocity impact** (early times): $|\mathbf{v}_p| \gg c_p$, so the advective speed dominates
- **Post-impact relaxation** (late times): $c_p \gg |\mathbf{v}_p|$, so the sound speed dominates
- **Shock propagation**: both terms are comparable, and the sum determines the limit

## Adaptive Time-Stepping

The MPM framework implements **adaptive time-stepping**:
- $\Delta t^n$ is recomputed at each time step
- The maximum of $c_p + |\mathbf{v}_p|$ is tracked across all material points
- A safety factor (typically 0.3–0.9) is applied: $\Delta t^n = \alpha \, \Delta t_{cr}$

This is particularly critical for hypervelocity impact on asteroids, where impact velocities reach **km/s** initially but decay rapidly as energy is dissipated through fragmentation and wave propagation.

## Relationship to Discretization

The critical time step links spatial and temporal resolution:
- Finer grid → smaller $d_c$ → smaller $\Delta t_{cr}$ → more time steps
- Higher sound speed (stiffer material) → smaller $\Delta t_{cr}$ → more time steps
- Higher velocity → smaller $\Delta t_{cr}$ → more time steps

## Related Concepts

[[Leapfrog Integrator]] | [[Sound Speed in Solids]] | [[MPM Algorithm Steps]]
