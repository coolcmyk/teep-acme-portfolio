# Johnson-Cook Flow Stress Model

An empirical constitutive model for metals that captures strain hardening, strain-rate sensitivity, and thermal softening.

### General Form
σ_Y = σ_Y(ε̄^p, ε̄̇^p, T)

The yield stress depends on:
- ε̄^p: accumulated effective plastic strain (strain hardening)
- ε̄̇^p: plastic strain rate (rate sensitivity)
- T: temperature (thermal softening)

### Extension of J2 Flow Theory
When using Johnson-Cook with the von Mises framework:
- The plastic modulus E^p in Eq. 43 becomes E^p = dσ_Y/dε̄^p
- This generalizes the constant plastic modulus of linear hardening

### In This Paper
Mentioned as an extension possibility for the J2 flow theory framework. Not the primary model used — the modified Lundborg model is the focus for geological materials. The Johnson-Cook model would be appropriate for modeling metallic asteroid components (e.g., iron-nickel bodies).

Link to: [[von Mises Yield Criterion]], [[Strength Models]], [[Linear Hardening]]
