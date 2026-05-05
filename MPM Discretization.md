# MPM Discretization

The MPM discretization rests on two fundamental equations that define how the continuous fields are represented by the discrete material points and how grid and particle variables communicate.

## Density Field Discretization

$$\rho(\mathbf{x}) = \sum_{p=1}^{n_p} m_p \, \delta(\mathbf{x} - \mathbf{x}_p) \quad \text{(Eq. 1)}$$

Where:

- $\rho(\mathbf{x})$ is the continuous density field
- $n_p$ is the total number of material points in the domain
- $m_p$ is the mass of material point $p$
- $\mathbf{x}_p$ is the position of material point $p$
- $\delta(\mathbf{x} - \mathbf{x}_p)$ is the Dirac delta function

**Critical distinction**: The Dirac delta function here is a **discretization tool**, NOT a density smoothing kernel. This differs fundamentally from SPH, where a smoothing kernel with finite support is used for density estimation. In MPM, each material point represents a point mass; the density field is reconstructed from the point distribution during the mapping to grid nodes.

## Interpolation Relation

$$\mathbf{u}_p = \sum_{I=1}^{n_g} N_I(\mathbf{x}_p) \, \mathbf{u}_I \quad \text{(Eq. 2)}$$

Where:

- $\mathbf{u}_p$ is a field variable (e.g., velocity) at material point $p$
- $\mathbf{u}_I$ is the corresponding field variable at grid node $I$
- $N_I(\mathbf{x}_p)$ is the shape function of node $I$ evaluated at $\mathbf{x}_p$
- $n_g$ is the number of grid nodes with non-zero shape functions at $\mathbf{x}_p$

This has the **exact same form as standard finite element interpolation**, creating a natural bridge between grid nodal variables and material point variables.

## Key Properties

### Mass Conservation
Mass is **permanently assigned** to material points and never changes. This means conservation of mass is automatically satisfied — unlike ALE methods that must explicitly enforce it through remapping.

### No Advective Remapping
State variables (stress, strain, internal energy, damage parameters, plasticity history) reside permanently on the material points. The background grid temporarily holds only mapped mass and momentum for solving the momentum equation. After each step, only positions, velocities, and updated states are transferred back to the particles — the grid is then discarded.

### Grid Nodal Variables
Background grid nodes temporarily hold:
- Mapped mass $M_I = \sum_p m_p N_I(\mathbf{x}_p)$
- Mapped momentum $\mathbf{P}_I = \sum_p m_p \mathbf{v}_p N_I(\mathbf{x}_p)$
- Internal and external forces

These are used only for solving the momentum equation within a single time step.

## Difference from ALE

| Feature | MPM | ALE |
|---------|-----|-----|
| History tracking | On material points (permanent) | On mesh nodes (requires remapping) |
| Advective remapping | None needed | Required each step |
| Mesh distortion | Grid discarded each step | Mesh moved but can still distort |
| State variable diffusion | Zero (no advection) | Possible from repeated remapping |

## Related Concepts

[[Material Point Method]] | [[Shape Functions]] | [[Conservation Laws]]
