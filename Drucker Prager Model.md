# Drucker Prager Model

(Drucker & Prager, 1952)

## Overview

A **pressure-dependent** strength model designed for geological materials (rock, soil, regolith). Unlike [[von Mises Yield Criterion]], the yield strength increases with confining pressure.

## Yield Surface

### Shear Yield Surface

**f^s(σ) = τ − q_φ p − Y₀**  (Eq. 44)

- **τ** = √(J₂): effective shear stress
- **q_φ**: internal friction coefficient, related to the friction angle φ (e.g., q_φ = tan φ)
- **p**: hydrostatic pressure (positive in compression)
- **Y₀**: cohesive shear strength — the shear strength at zero confining pressure

### Tension Cut-Off

**f^t(σ) = p_t − p**  (Eq. 45)

A second yield surface that caps the tensile pressure at *p_t* (tensile strength). This prevents the Drucker-Prager cone from extending indefinitely into the tensile regime.

### Combined Surface

The two surfaces together form a **truncated cone** in principal stress space:
- The Drucker-Prager cone controls shear failure at moderate-to-high pressure
- The tension cut-off limits tensile failure at low/negative pressure

## Plastic Potential

Non-associated flow (see [[Associated vs Non Associated Flow]]):

**ψ = τ − q_ψ p**  (Eq. 46)

where *q_ψ* is the **dilatancy coefficient** controlling volumetric strain during plastic shear.

## Limitations

1. **Unbounded strength**: shear strength increases linearly with pressure without limit — physically unrealistic at very high pressures where material strength should saturate
2. **Multi-surface corners**: the intersection of the Drucker-Prager cone and the tension cut-off creates a **non-smooth corner** in the yield surface, complicating the determination of the plastic flow direction at the junction (no unique normal vector)
3. These limitations are addressed by the [[Lundborg Strength Model]] and ultimately the [[Modified Lundborg Model]]
