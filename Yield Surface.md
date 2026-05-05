# Yield Surface

The boundary in stress space that separates elastic (reversible) from plastic (permanent) deformation. Defined by the yield function: f(σ, q) ≤ 0.

### Fundamental Concept
- f < 0: elastic domain (stress is inside the surface)
- f = 0: yield surface (plastic flow occurs)
- f > 0: inadmissible (stress must be corrected back to surface)

### Shape Variations by Model

**von Mises** (J2 flow theory):
- Cylinder in principal stress space
- Radius = σ_Y (constant yield strength)
- Pressure-independent: surface does not change with hydrostatic pressure

**Drucker-Prager**:
- Truncated cone in principal stress space
- Pressure-dependent: strength increases with confining pressure
- Multi-surface: shear envelope + tension cut-off
- Non-smooth corners at surface junctions

**Lundborg**:
- Asymptotic curved surface with upper limit Y_m
- Smooth but may have transitions between intact and damaged regimes
- Includes damage interpolation

**Modified Lundborg** (this paper):
- Single, C¹ continuous smooth surface
- No corners or discontinuities
- Enables analytical plastic flow direction determination
- Pressure-dependent with Y_m asymptotic limit
- Includes thermal softening via Q/Q_melt

### Visualization
Yield surfaces are typically visualized in:
- Principal stress space (σ₁, σ₂, σ₃) — see Fig. 2(a)
- p–τ plane (pressure vs shear stress) — see Fig. 2(b)

Link to: [[Strength Models]], [[Plastic Flow Law]], [[Plastic Corrector]], [[von Mises Yield Criterion]], [[Drucker Prager Model]], [[Modified Lundborg Model]]
