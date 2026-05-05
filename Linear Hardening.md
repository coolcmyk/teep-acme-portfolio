# Linear Hardening

## Definition

An extension of the [[von Mises Yield Criterion]] (J2 flow theory) where the yield stress evolves linearly with accumulated plastic strain:

**σ_Y^{n+1}(ε̄^p) = σ_Y^n + E^p · Δε̄^p**

- **E^p**: constant plastic modulus (hardening slope)
- **Δε̄^p**: incremental equivalent plastic strain

## Physical Interpretation

The yield surface remains a cylinder (pressure-independent), but its **diameter increases linearly with plastic strain**. This models strain hardening observed in ductile metals.

## Plasticity Correction

```
Δε^p = (3/2) · f(σ*) / (3G + E^p) · s*/σ̄*
```

where *G* is the shear modulus and *f(σ\*)* is the trial yield function value.

The correction modifies **only shear stress** (like J2 radial return) — pressure is not corrected. This is the key distinction from the [[Modified Lundborg Model]] plastic corrector, which couples shear and pressure corrections.

## Numerical Implementation

In this work, E^p is set to a small but non-zero value (e.g., **5.31 MPa**) for numerical stability — a purely elastic-perfectly plastic model (E^p = 0) can lead to convergence issues in the return mapping algorithm.

## Application

Used as the **baseline strength model** in the lab-scale impact experiments with yield strength σ_Y = 3500 MPa, representing the behavior of the aluminum projectile and target materials.
