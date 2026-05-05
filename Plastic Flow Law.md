# Plastic Flow Law

The fundamental theory governing how materials undergo permanent (plastic) deformation when stress exceeds the yield limit (Appendix B.1).

### Core Principle
When elastic trial stress σ* gives f(σ*, q^n) > 0, the material is in a state of plastic loading and must be corrected back to the yield surface f = 0.

### Plastic Strain Rate (Eq. 38)
ε̇^p = λ̇·r

- λ̇: plastic multiplier (loading parameter, scalar) — determines magnitude
- r = ∂ψ/∂σ: plastic flow direction — determines the direction
- ψ: plastic potential function

### Return Mapping Algorithm (Eq. 39)
The system of equations solved for plasticity correction:

1. Δε^p = λ̇·r·Δt — plastic strain increment
2. σ^{n+1} = σ* − C^{σJ}:Δε^p — elastic correction (stress return)
3. q^{n+1} = q^n + λ̇·h·Δt — internal variable evolution
4. f(σ, q) = 0 — yield condition must be satisfied

Where:
- C^{σJ}: fourth-order elasticity tensor
- h: evolution equations for internal variables q

### Solution Methods
- Iterative Newton-Raphson scheme (exact)
- Linearization or semi-implicit algorithm (efficient)
- This paper: analytical derivation for Modified Lundborg (Eqs. 5a-5d)

### Plastic Heat Generation (Eq. 40)
ΔQ = σ : Δε^p
- Plastic work converts to heat → thermal softening
- Contributes to melting coefficient Q/Q_melt in the Modified Lundborg model

### Applications
- Tracks cumulative plastic strain for fatigue damage modeling
- Determines post-yield material response
- Essential for capturing realistic wave propagation and damage patterns

Link to: [[Plastic Corrector]], [[Yield Surface]], [[Associated vs Non Associated Flow]], [[Modified Lundborg Model]]
