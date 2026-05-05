# Weak Form Formulation

The integral form of the momentum equation that serves as the basis for MPM discretization. Also called the principle of virtual work.

### Strong Form
The differential momentum equation with boundary conditions (traction boundary condition on Γ_t).

### Weak Form (Eq. 24)
∫_Ω ρü·δu dV + ∫_Ω ρσ^s:δ(∇u)dV − ∫_Ω ρb·δu dV − ∫_Γ_t t̄·δu dΓ = 0

### Terms
1. **Inertial term**: ∫_Ω ρü·δu dV — acceleration work
2. **Internal force term**: ∫_Ω ρσ^s:δ(∇u)dV — stress work (deformation resistance)
3. **Body force term**: ∫_Ω ρb·δu dV — external body forces (e.g., gravity)
4. **Traction term**: ∫_Γ_t t̄·δu dΓ — surface tractions on boundary

### Discretization
By substituting the MPM density representation (Eq. 25) and interpolation (Eq. 26):
- The integrals become sums over material points
- The nodal momentum equation becomes: Ṗ_I = F_I^int + F_I^ext (Eq. 27)

### Nodal Force Expressions
- **Internal force** (Eq. 29): F_I^int = −Σ (m_p/ρ_p)·∇N_I(x_p)·σ_p
- **External force** (Eq. 30): F_I^ext = Σ m_p N_I(x_p) b_p + ∫ N_I(x_p) t̄ dΓ

### Key Insight
The Dirac delta representation (Eq. 25) is a **numerical quadrature tool** for evaluating the weak form integrals — NOT a physical smoothing model for density (unlike SPH). This is a fundamental difference between MPM and SPH.

Link to: [[Conservation Laws]], [[Updated Lagrangian Formulation]], [[MPM Discretization]], [[Comparison with SPH]]
