# MPM Algorithm Steps

The MPM algorithm in this work uses the **MUSL (Modified Update-Stress-Last)** scheme, an 8-step procedure executed per time step. MUSL was chosen for its superior energy conservation and numerical stability in extreme impact scenarios.

## The 8-Step MUSL Scheme

### Step 1: Map Mass and Momentum to Grid
Compute grid nodal mass $M_I$ and momentum $\mathbf{P}_I^{n-1/2}$ from material points using shape functions:

$$M_I^n = \sum_p m_p \, N_I(\mathbf{x}_p^n)$$

$$\mathbf{P}_I^{n-1/2} = \sum_p m_p \, \mathbf{v}_p^{n-1/2} \, N_I(\mathbf{x}_p^n)$$

### Step 2: Apply Boundary Conditions
Apply boundary conditions to grid nodal momentum. For fixed boundaries, grid node momentum is set to zero. For free surfaces, no modification is needed. This is enforced on the grid nodes, not on particles directly.

### Step 3: Compute Forces
Calculate forces acting on each grid node:

- **Internal forces $\mathbf{F}_I^{\text{int}}$**: derived from the material point stress tensors, mapped to grid nodes via the gradient of shape functions:

  $$\mathbf{F}_I^{\text{int},n} = -\sum_p V_p^n \, \boldsymbol{\sigma}_p^n \, \nabla N_I(\mathbf{x}_p^n)$$

- **External forces $\mathbf{F}_I^{\text{ext}}$**: from body forces (e.g., gravity) and surface tractions:

  $$\mathbf{F}_I^{\text{ext},n} = \sum_p m_p \, \mathbf{b} \, N_I(\mathbf{x}_p^n)$$

Total force: $\mathbf{F}_I^n = \mathbf{F}_I^{\text{int},n} + \mathbf{F}_I^{\text{ext},n}$

### Step 4: Integrate Momentum on Grid
Apply the leapfrog explicit update to advance grid nodal momentum:

$$\mathbf{P}_I^{n+1/2} = \mathbf{P}_I^{n-1/2} + \mathbf{F}_I^n \, \Delta t^n$$

This is a second-order accurate central difference in time.

### Step 5: Update Particle Positions and Velocities
Interpolate grid nodal momentum and forces back to update material points:

$$\mathbf{v}_p^{n+1/2} = \mathbf{v}_p^{n-1/2} + \Delta t^n \sum_I \frac{\mathbf{F}_I^n \, N_I(\mathbf{x}_p^n)}{M_I^n}$$

$$\mathbf{x}_p^{n+1} = \mathbf{x}_p^n + \Delta t^n \sum_I \frac{\mathbf{P}_I^{n+1/2} \, N_I(\mathbf{x}_p^n)}{M_I^n}$$

### Step 6: Re-Map Momentum to Grid (MUSL Distinctive Step)
Map the updated particle momentum **back** to the grid nodes:

$$\mathbf{P}_I^{n+1/2} = \sum_p m_p \, \mathbf{v}_p^{n+1/2} \, N_I(\mathbf{x}_p^n)$$

This re-mapping step is what distinguishes **MUSL** from the simpler USL scheme and provides improved stability.

### Step 7: Compute Strain and Update Stress
1. Compute grid nodal velocity from re-mapped momentum: $\mathbf{v}_I^{n+1/2} = \mathbf{P}_I^{n+1/2} / M_I^n$
2. Compute velocity gradient at each particle: $\nabla \mathbf{v}_p = \sum_I \mathbf{v}_I^{n+1/2} \nabla N_I(\mathbf{x}_p^n)$
3. Compute strain increment $\Delta\boldsymbol{\varepsilon}$ and vorticity increment $\Delta\boldsymbol{\Omega}$ for each particle
4. Update stress $\boldsymbol{\sigma}$ using the **Jaumann rate** (objective stress rate that accounts for rigid-body rotation)
5. Update density $\rho$ from the volumetric strain
6. Update internal energy $E$ and pressure $p$ iteratively via the equation of state

### Step 8: Reset Grid
Discard the deformed grid entirely. Generate a new regular, undeformed background grid for the next time step. Return to Step 1.

## Comparison of MPM Schemes

| Scheme   | Description                | Energy Conservation | Stability    |
| -------- | -------------------------- | ------------------- | ------------ |
| **USF**  | Update-Stress-First        | Lowest              | Least stable |
| **USL**  | Update-Stress-Last         | Moderate            | Moderate     |
| **MUSL** | Modified USL (with re-map) | Best                | Most stable  |

MUSL is used in this work because hypervelocity impact on asteroids involves extreme deformations, high strain rates, and fragmentation — conditions that demand the most robust scheme available.

## Related Concepts

[[Material Point Method]] | [[Leapfrog Integrator]] | [[MPM Discretization]] | [[Conservation Laws]]
