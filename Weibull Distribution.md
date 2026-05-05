# Weibull Distribution

(Weibull, 1939; Jaeger & Cook, 1979)

A statistical theory of material strength based on the concept that failure initiates from the "weakest link" among a population of defects.

### Fundamental Equation (Eq. 15)
n(ε)/V_s = k·ε^m

- n(ε): cumulative number of flaws activated at strain ≤ ε
- V_s: volume of the solid phase (V for non-porous material)
- k: scale parameter (flaw density)
- m: shape parameter (Weibull modulus)

### Key Derived Quantities

**Average activation strain** (Eq. 16):
ε̄_act = (n_tot/(m·V))^{1/m} · (m+1)/m

**Dimensionless strength**:
φ = ln(kV)/m  — larger φ means weaker material (Benz & Asphaug, 1994)

### Numerical Implementation
- Total flaws n_tot = n_p·ln(n_p) (classical) or physically determined (this paper)
- Flaws sequentially assigned randomly to computational particles
- Each particle records:
  - ε_min,p: smallest activation strain
  - ε_max,p: largest activation strain
  - n_f,p: total flaws in the particle
- Local Weibull modulus: m_p = ln(n_f,p) / ln(ε_max,p/ε_min,p)

### Wide Strain Spread Requirement
For hypervelocity impacts, ε_max/ε_min,V ≥ 10 is needed to capture the range of fracture strains.

Link to: [[Weibull Parameters]], [[Grady Kipp Fracture Model]], [[Resolution Independent Flaw Init]]
