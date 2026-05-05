# Nominal Benchmark Case

The standard simulation setup used to validate the MPM code against laboratory impact experiments and SPH results.

### Setup (from [[Laboratory Impact Experiments]])
- Basalt target: 6 cm diameter, 2700 kg/m³, 303 g
- Nylon projectile: 7 mm diameter, 1180 kg/m³, 0.213 g
- Impact: 3.2 km/s at 30° angle

### Material Parameters (Table 1)

**Target (Basalt)**:
- Young's modulus: E_Y = 53100 MPa
- Poisson's ratio: ν = 0.15
- Strength: linear hardening, σ_Y = 3500 MPa, E^p = 5.31 MPa
- EOS: Tillotson (A=26.7 GPa, B=26.7 GPa, E₀=4.72 MJ/kg, E_iv=18.2 MJ/kg, E_cv=2000 MJ/kg, ρ_iv=26.7 kg/m³, a=0.5, b=1.5, α=5, β=5)
- Fracture: Grady-Kipp, m=8.5, k=3.0×10³⁹ m⁻³

**Projectile (Nylon)**:
- Young's modulus: E_Y = 219 MPa
- Poisson's ratio: ν = 0.45
- Strength: linear hardening, σ_Y = 10 MPa, E^p = 2.19 MPa
- EOS: Tillotson (E₀=7 MJ/kg, E_iv=2.4 MJ/kg, E_cv=10.1 MJ/kg, ρ_iv=33.8 kg/m³, A=2 GPa, B=2 GPa, a=0.6, b=2.0, α=10, β=5)
- No damage model (less important, lacks material parameters)

### Simulation Parameters
- Nominal precision: 0.8 mm inter-particle spacing
- Target discretized into 230,144 material points
- 8 points per active grid cell (2×2×2)
- Simulation duration: 100 µs
- Failure threshold: D > 0.9
- Energy conservation: fluctuations < 0.6%

### Key Results
- Core fragment mass: 24.6% of target (experiment: 31%, SPH: 30%)
- Core fragment velocity: 2.056 m/s (experiment: 1.35 m/s, SPH: 1.352 m/s)
- 826 fragments identified
- Good agreement with experimental cumulative mass distribution and power-law relation
- Velocity within 3σ experimental confidence interval

Link to: [[Laboratory Impact Experiments]], [[Discretization Convergence Study]], [[Material Point Method]], [[Sensitivity on Impact Conditions]]
