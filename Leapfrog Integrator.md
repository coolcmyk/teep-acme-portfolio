# Leapfrog Integrator

The leapfrog integrator is a **variable step size, second-order precision, explicit central difference** integration scheme used in the MPM framework for time advancement.

## Time Discretization

The leapfrog scheme staggers variables in time:

- **Velocities** are stored at half-steps: $t^{n-1/2}$, $t^{n+1/2}$
- **Positions** are stored at integer steps: $t^n$, $t^{n+1}$
- **Forces, stresses, and state variables** are evaluated at integer steps: $t^n$

This staggering is the origin of the name "leapfrog" — velocity "leaps over" position in time, and vice versa.

## Integration Formulas

Grid momentum update (half-step advance):

$$\mathbf{P}_I^{n+1/2} = \mathbf{P}_I^{n-1/2} + \mathbf{F}_I^n \, \Delta t^n$$

Particle position update (full-step advance):

$$\mathbf{x}_p^{n+1} = \mathbf{x}_p^n + \mathbf{v}_p^{n+1/2} \, \Delta t^n$$

## Stability Requirement

The explicit nature of the scheme imposes a strict stability condition:

$$\Delta t \leq \Delta t_{cr}, \quad \text{where} \quad \Delta t_{cr} = \frac{d_c}{\max(c_p + |\mathbf{v}_p|)}$$

This CFL-type condition enforces that:
- **Particle movement** is constrained to $\leq 1$ grid cell per time step
- **Stress wave propagation** is constrained to $\leq 1$ grid cell per time step

Both constraints must be satisfied simultaneously, with the more restrictive one determining $\Delta t$.

## Variable Step Size

In hypervelocity impact scenarios:
- Early times: velocities are extremely high (km/s), requiring very small $\Delta t$
- Later times: velocities decrease as energy dissipates, allowing larger $\Delta t$

**Adaptive time-stepping** is implemented in this MPM framework: $\Delta t^n$ is recomputed each step based on the current maximum $c_p + |\mathbf{v}_p|$ across all material points. This dramatically improves computational efficiency compared to a fixed small time step.

## Second-Order Accuracy

The leapfrog scheme achieves $\mathcal{O}(\Delta t^2)$ accuracy, meaning the global error decreases quadratically as the time step is reduced. Combined with the explicit formulation, this provides an excellent balance of accuracy and computational cost for wave propagation problems.

## Advantages for MPM

- **Highly efficient**: no linear system solves required per time step
- **Simple implementation**: straightforward update formulas
- **Good energy conservation**: when paired with MUSL scheme
- **Naturally suited to wave dynamics**: the central difference stencil preserves wave propagation characteristics well

## Related Concepts

[[MPM Algorithm Steps]] | [[Critical Time Step]] | [[Sound Speed in Solids]]
