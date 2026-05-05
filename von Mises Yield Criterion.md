# von Mises Yield Criterion

(J2 flow theory, Mises 1913)

## Yield Condition

**f(σ) = σ̄ − σ_Y ≤ 0**  (Eq. 41)

where:
- **σ̄** = √(3J₂): von Mises effective stress
- **J₂** = ½ s:s: second invariant of the deviatoric stress tensor **s**
- **σ_Y**: yield strength (temperature- and rate-dependent; constant for elastic-perfectly plastic)

## Geometric Interpretation

The yield surface is a **cylinder** in 3D principal stress space, centered on the hydrostatic axis. This cylinder is:
- **Pressure-independent**: hydrostatic pressure has no effect on yielding
- **Open-ended**: no cap on the tensile or compressive sides
- Suitable for metals and non-porous ductile materials

## Plasticity Correction: Radial Return

When the elastic trial stress **σ\*** exceeds the yield surface (`f(σ*) > 0`):

1. Plastic strain increment: **Δε^p** = f(σ\*) / (2G σ̄\*) · **s\***
2. Post-correction deviatoric stress: **s** = (σ_Y / σ̄\*) · **s\***
3. Pressure is left uncorrected — only shear stress is modified

This is the simplest plasticity corrector (see [[Plastic Corrector]] for comparison with the flow-law-based approach).

## Extensions

### Linear Isotropic Hardening
- σ_Y^{n+1}(ε̄^p) = σ_Y^n + E^p · Δε̄^p
- Constant plastic modulus *E^p* (see [[Linear Hardening]])
- For Johnson-Cook: E^p = dσ_Y / dε̄^p evaluates the instantaneous hardening slope

### Limitation
When combined with the simplified radial return, the von Mises model **decouples volumetric and deviatoric plastic strain increments** — an assumption invalid for geological materials that exhibit pressure-dependent yielding and shear-induced dilatation.
