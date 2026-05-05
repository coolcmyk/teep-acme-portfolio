# Updated Lagrangian Formulation

The reference frame used in MPM to formulate the governing equations. In the updated Lagrangian approach, the equations are written with respect to the current (deformed) configuration at each time step.

### Characteristics
- Variables expressed in terms of the current configuration
- The mesh (background grid in MPM) moves with the material
- Convection term associated with Eulerian formulations does NOT appear
- Suitable for history-dependent materials where state variables track deformation history

### Kinematic Condition (Eq. 21)
D = ½(L + L^T)
- D: rate of deformation tensor
- L = ∂v/∂x: velocity gradient
- D equals the rate of true strain (ε̇) with respect to the current configuration
- Describes BOTH large deformation and rigid body motion

### Weak Form (Eq. 24)
∫_Ω ρü·δu dV + ∫_Ω ρσ^s:δ(∇u)dV − ∫_Ω ρb·δu dV − ∫_Γ_t t̄·δu dΓ = 0
- δu: virtual displacement (test function)
- Ω: material domain
- Γ_t: traction boundary
- σ^s = σ/ρ: stress per unit mass
- t̄ = t/ρ: traction per unit mass
- b: body force per unit mass

### Material Objectivity
Constitutive equations must be frame-invariant. The Cauchy stress rate is not objective, so the [[Jaumann Stress Rate]] (co-rotational rate) is used instead.

### MPM Context
- Material points are the Lagrangian entities
- Background grid is reset each step (Eulerian aspect)
- The combination avoids mesh distortion while preserving Lagrangian material tracking

Link to: [[Conservation Laws]], [[Jaumann Stress Rate]], [[Rate of Deformation Tensor]], [[Weak Form Formulation]]
