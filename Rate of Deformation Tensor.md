# Rate of Deformation Tensor

The kinematic quantity that links material movement (velocity field) to strain rate.

### Definition (Eq. 21)
D = ½(L + L^T)

Where:
- L = ∂v/∂x: velocity gradient tensor
- L^T: transpose of velocity gradient

### Properties
- D is the **symmetric part** of the velocity gradient
- Equals the rate of true strain (ε̇) with respect to the current configuration
- Describes BOTH large deformation and rigid body motion
- Related to the spin tensor: Ω = ½(L − L^T) (skew-symmetric part)

### Decomposition
L = D + Ω
- D: rate of deformation (stretching)
- Ω: spin (rigid body rotation)

### In MPM
The strain increment for each material point is computed from grid nodal velocities (Step 7 of MUSL):
Δε_p^{n+1/2} = Δt^{n+1/2} · ½ Σ [∇N_I(x_p)⊗v_I^{n+1/2} + v_I^{n+1/2}⊗∇N_I(x_p)]

Similarly, the vorticity (spin) increment:
ΔΩ_p^{n+1/2} = Δt^{n+1/2} · ½ Σ [∇N_I(x_p)⊗v_I^{n+1/2} − v_I^{n+1/2}⊗∇N_I(x_p)]

### Role
- Strain increment → stress update via constitutive model
- Spin increment → rotational correction via Jaumann rate
- Trace of Δε → density update: ρ^{n+1} = ρ^n/(1 + tr(Δε))
- Used in calculating specific internal energy: E^{n+1} = E^n + Δε:σ/ρ

Link to: [[Updated Lagrangian Formulation]], [[Jaumann Stress Rate]], [[MPM Algorithm Steps]]
