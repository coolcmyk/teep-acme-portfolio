# Damage Models

The comprehensive set of material failure formulations implemented in the MPM framework. Damage models describe how materials weaken and fracture under tensile loading.

### Primary Model: Grady-Kipp
See [[Grady Kipp Fracture Model]] for details.
- Weibull-distributed incipient flaws
- Strain-activated crack nucleation
- Constant-velocity crack growth
- Produces realistic spallation patterns

### Brittle Fracture
See [[Brittle Fracture Criterion]] for details.
- Maximum principal stress threshold
- Instantaneous failure (D → 1)
- Suitable for materials that shatter under tension

### Fatigue Damage
- Damage accumulates based on plastic strain:
  D = Σ Δε^p/ε₀
- ε₀: critical plastic strain threshold
- Models progressive weakening under cyclic/repeated loading

### Damage Effects
- Reduces stress: σ = (1−D)·s_E − p*·I
- Reduces strength: interpolates between intact and failed yield surfaces
- Affects pressure: p* = (1−D)p for tension, p* = p for compression

### Post-Processing
- Failure threshold: D > 0.9 (accounts for time-truncated damage development)
- Failed points form boundaries between fragments
- Unfailed points form fragment interiors

Link to: [[Grady Kipp Fracture Model]], [[Brittle Fracture Criterion]], [[Weibull Distribution]], [[Damage Variable D]], [[Stress Tensor Decomposition]]
