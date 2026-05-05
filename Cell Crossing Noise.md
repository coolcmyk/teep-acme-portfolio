# Cell Crossing Noise

Cell-crossing noise is a well-known numerical artifact in the Material Point Method that arises from the discontinuous nature of shape function gradients at grid cell boundaries.

## Mechanism

When a material point traverses from one grid cell to an adjacent cell:
1. The set of grid nodes with non-zero shape functions at the particle's location changes
2. The gradient of the shape functions $\nabla N_I$ changes **discontinuously** at the cell boundary
3. Since internal forces are computed as $\mathbf{F}_I^{\text{int}} = -\sum_p V_p \boldsymbol{\sigma}_p \nabla N_I(\mathbf{x}_p)$, a discontinuous change in $\nabla N_I$ produces a spurious force oscillation
4. This manifests as **localized stress oscillations** that propagate through the domain

## Dependence on Resolution

Cell-crossing noise **worsens at higher resolutions** because:
- Finer grids have more cell boundaries
- Particles cross boundaries more frequently for the same physical displacement
- The noise accumulates over more time steps

## Evidence from Discretization Convergence Study

In the convergence study presented by Yan et al. (2026):
- When the number of material points was increased to **523,984** (highest resolution), accumulated cell-crossing noise caused a **slight expansion of the failure region** inside the core-shaped fragment
- However, this did **NOT** represent numerical divergence
- Key statistical variables — failure ratio, fragment morphology, fragment size distribution — all **converged to a plateau** despite the noise
- This demonstrates that while cell-crossing noise introduces local artifacts, it does not corrupt the global solution metrics of engineering interest

## Mitigation Strategies

### GIMP Method
The primary mitigation is the [[GIMP Method]] (Bardenhagen & Kober, 2004), which smooths shape function derivatives across cell boundaries by convolving the standard shape functions with a particle characteristic function.

### SGMP Method
The Staggered Grid Material Point method offers an alternative stabilization approach.

### Practical Approach
In many cases, particularly at moderate resolutions, cell-crossing noise is acceptable as long as it does not corrupt the quantities of interest (e.g., fragment size distribution, impact energy partitioning).

## Related Concepts

[[GIMP Method]] | [[Material Point Method]] | [[Shape Functions]]
