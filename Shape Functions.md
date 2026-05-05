# Shape Functions

Shape functions $N_I(\mathbf{x})$ are the interpolation (basis) functions used in MPM to bridge between the Eulerian background grid nodes and the Lagrangian material points. They have the **same form as standard finite element interpolation functions**.

## Role in MPM

Shape functions serve as the mapping kernel between grid and particle variables in both directions:

### Particle-to-Grid (Mapping)
Mass and momentum are mapped from particles to grid nodes:

$$M_I = \sum_p m_p \, N_I(\mathbf{x}_p)$$

$$\mathbf{P}_I = \sum_p m_p \, \mathbf{v}_p \, N_I(\mathbf{x}_p)$$

### Grid-to-Particle (Interpolation)
Grid solutions are interpolated back to particles:

$$\mathbf{v}_p = \sum_I \frac{\mathbf{P}_I}{M_I} \, N_I(\mathbf{x}_p)$$

$$\mathbf{a}_p = \sum_I \frac{\mathbf{F}_I}{M_I} \, N_I(\mathbf{x}_p)$$

## Properties

### Local Support
Shape functions are **non-zero only for grid nodes that surround the material point location**. For a standard 3D trilinear hexahedral element, exactly 8 grid nodes have non-zero shape function values at any interior point.

### Partition of Unity
$$\sum_I N_I(\mathbf{x}) = 1 \quad \text{for all } \mathbf{x}$$

This property ensures that rigid-body motion is represented exactly — if all nodes move by the same amount, all particles move by the same amount.

### Consistency
Linear shape functions guarantee that constant strain fields are reproduced exactly:

$$\sum_I \mathbf{x}_I \, N_I(\mathbf{x}) = \mathbf{x}$$

## Standard vs. GIMP Shape Functions

### Standard (Piecewise-Linear)
Standard FEM trilinear shape functions for hexahedral elements. Simple, efficient, but have **discontinuous gradients** at cell boundaries, leading to [[Cell Crossing Noise]].

### GIMP (Generalized Interpolation)
The [[GIMP Method]] replaces standard shape functions with smeared versions that have **continuous gradients** at cell boundaries. The GIMP shape function is defined as:

$$S_{Ip} = \frac{1}{V_p} \int_{\Omega_p} \chi_p(\mathbf{x}) \, N_I(\mathbf{x}) \, d\mathbf{x}$$

This convolution with the particle characteristic function $\chi_p$ smooths the gradient discontinuity, at the cost of slightly increased computational overhead.

## Practical Considerations

### $n_g$ — Number of Supporting Nodes
$n_g$ is the count of grid nodes with non-zero shape function values at a given particle position $\mathbf{x}_p$. For standard trilinear 3D elements, $n_g = 8$ when the particle is in the interior of a cell.

### Gradient Computation
The gradient of shape functions $\nabla N_I$ is needed for computing internal forces:

$$\mathbf{F}_I^{\text{int}} = -\sum_p V_p \, \boldsymbol{\sigma}_p \, \nabla N_I(\mathbf{x}_p)$$

It is the discontinuity in $\nabla N_I$ at cell boundaries that causes cell-crossing noise.

## Related Concepts

[[MPM Discretization]] | [[GIMP Method]] | [[Material Point Method]]
