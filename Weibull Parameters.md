# Weibull Parameters

Two critical parameters characterize the Weibull flaw distribution and control material strength.

### Parameter Definitions

**k (m⁻³)** — Scale parameter
- Determines the overall flaw density in the material
- Values used in simulations:
  - Nominal lab case (basalt): k = 3.0×10³⁹ m⁻³ → σ̄_max ≈ 40 MPa
  - Asteroid low-strength case: k = 5.0×10²² m⁻³ → σ̄_max ≈ 0.4 MPa
  - Asteroid high-strength case: k = 1.0×10²⁵ m⁻³ → σ̄_max ≈ 40 MPa
- Higher k → more flaws → lower activation strain → weaker material

**m** — Shape parameter (Weibull modulus)
- Controls the width/spread of the flaw distribution
- Higher m → narrower distribution → more uniform activation strains
- Values used:
  - Nominal case: m = 8.5
  - Experimental basalt (Nakamura et al., 2007): m = 17.2

### Practical Constraints
- Requirement: n_tot > 10^m for proper algorithm function
- When m is elevated (e.g., 17.2):
  - More incipient flaws per material point
  - Flaw activation less frequent under same stress-strain (Eq. 17)
  - Can lead to insufficient damage development
  - This discrepancy may relate to algorithmic design and calls for further improvement

### Strength Translation
Activation strain converted to stress via Young's modulus:
- σ_min = ε_min · E_Y
- σ_max = ε_max · E_Y

The Weibull parameters critically determine whether an asteroid:
- Completely disintegrates (low strength, ~0.4 MPa)
- Survives with large coherent fragments (high strength, ~40 MPa)

Link to: [[Weibull Distribution]], [[Grady Kipp Fracture Model]], [[Sensitivity on Material Models]]
