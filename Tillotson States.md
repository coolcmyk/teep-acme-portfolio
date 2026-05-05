# Tillotson States

The four distinct material regions in the Tillotson EOS, mapped in the μ–E space (Fig. 3).

### Region A1 — Compressed State
- Condition: ρ ≥ ρ₀ (μ ≥ 0)
- Equation: P₁(ρ,E) = [a + b/(E/(E₀η²)+1)] ρE + Aμ + Bμ² (Eq. 8)
- Material is denser than initial state

### Region A2 — Cold Expanded State
- Condition: ρ_iv ≤ ρ < ρ₀ & E ≤ E_iv (μ_iv ≤ μ < 0)
- Same equation form as compressed state (Eq. 8)
- Expanded but below vaporization threshold

### Region B — Hot Expanded State
- Condition: ρ < ρ₀ & E ≥ E_cv (μ < 0)
- Equation: P₂(ρ,E) = aρE + [bρE/(E/(E₀η²)+1)] + Aμ·e^{−βν}·e^{−αν²} (Eq. 9)
- Fully vaporized, gas-like behavior
- Exponential terms (α, β) capture low-density physics

### Region C — Mixing Region
- Condition: ρ_iv ≤ ρ < ρ₀ & E_iv < E < E_cv
- Linear energy-weighted interpolation between P₁ and P₂:
  P₃ = (P₂·(E−E_iv) + P₁·(E_cv−E))/(E_cv−E_iv) (Eq. 10)
- Smoothly transitions between solid and vapor phases

### Region D — Low Energy Vapor Expansion
- Condition: ρ < ρ_iv & E < E_cv
- Equation: P₄ = [a + b/(E/(E₀η²)+1)] ρE + Aμ (Eq. 11)
- Low-density, partially vaporized state

### Key Thresholds
- **E_iv**: specific energy at incipient vaporization — material begins to vaporize
- **E_cv**: specific energy at complete vaporization — fully gaseous
- **ρ_iv**: density at incipient vaporization — defines expansion boundary

Link to: [[Tillotson EOS]], [[Equation of State]]
