# Conservation Laws

The fundamental physical principles that form the closed set of governing equations for dynamic problems.

### Three Conservation Laws

**Conservation of Mass**:
- In MPM: automatically satisfied because material point masses never change
- Mass is permanently assigned to particles: m_p = constant
- No mass transfer between particles or to the grid

**Conservation of Momentum**:
- The central equation connecting motion and stress
- Weak form: ∫ρü·δu dV + ∫ρσ^s:δ(∇u)dV − ∫ρb·δu dV − ∫t·δu dΓ = 0  (Eq. 24)
- Discretized at each grid node: Ṗ_I = F_I^int + F_I^ext  (Eq. 27)
- Internal force: from stress gradients (Eq. 29)
- External force: from body forces and surface tractions (Eq. 30)

**Conservation of Energy**:
- Specific internal energy E updated incrementally
- Form: ρĖ = ε̇:σ (neglecting heat transfer)
- Evaluated using variables stored at material points
- Plastic work ΔQ = σ:Δε^p contributes to heating (Eq. 40)

### Closed-Form System
The governing equations comprise:
1. Conservation equations (mass, momentum, energy)
2. Constitutive equation (stress-strain relation) — see [[Strength Models]], [[Equation of State]]
3. Kinematic relation (strain-displacement) — see [[Rate of Deformation Tensor]]
4. Boundary conditions
5. Initial conditions

Link to: [[Updated Lagrangian Formulation]], [[MPM Discretization]], [[MPM Algorithm Steps]]
