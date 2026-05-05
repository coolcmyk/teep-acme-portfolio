# Sensitivity on Material Models

Investigation of how different damage and strength models affect impact simulation outcomes (Sections 4.1.5, Tables 3-4).

### Damage Model Sensitivity (Table 3)

**Weibull Distribution Variations**:
- **Altering k (constant m=8.5)**:
  - Lower k (weaker material, σ̄_max ~20 MPa): larger damage zone, smaller/slower core
  - Higher k (stronger material, σ̄_max ~60 MPa): no closed damage shell, larger fragments, faster, no core
  - Damage evolution PATTERN unchanged
- **Altering both k and m (constant φ)**:
  - m=17.2 with corresponding k: SHOULD give similar damage theoretically
  - Actually differs: elevated m → more flaws per particle → less frequent activation (Eq. 17) → insufficient damage → chaotic stress reflections
  - Nominal case strength (40 MPa) higher than experimental value (19.43 MPa)
  - Discrepancy may relate to Weibull algorithm design

**Brittle Fracture vs Damage Accumulation**:
- Same strength threshold → brittle fracture always MORE severe
  - Instantaneous failure and stress release
  - Many small irregular fragments
- Damage accumulation: delayed stress response → viscous-like filtering → less severe damage
  - Naturally reproduces spallation

### Strength Model Sensitivity (Table 4)

**Linear Hardening (varying σ_Y)**:
- σ_Y = 3500 MPa (nominal): rarely yields (σ_Y >> damage strength)
- σ_Y = 30 MPa (below damage strength): spallation shifts, double-layered damage shell
- σ_Y = 60 MPa (above damage strength): similar to nominal, spallation present

**Modified Lundborg (varying Y₀)**:
- Y₀ = 10 MPa: pronounced plasticity, disordered damage
- Y₀ = 60 MPa: sealed shell-like damage, core-shaped fragment — matches experiments
- Y₀ = 600 MPa: similar to high-strength behavior

**Key Difference Between Models**:
- Linear hardening: only corrects shear → decouples wave velocities
- Modified Lundborg: corrects both shear and pressure → converges damage zones

Link to: [[Nominal Benchmark Case]], [[Strength Models]], [[Damage Models]], [[Weibull Parameters]], [[Modified Lundborg Model]]
