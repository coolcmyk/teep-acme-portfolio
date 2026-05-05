# Modified Lundborg Model

The central material model innovation in this paper (Section 3.1).

## Key Innovation

A **single, smooth (C¹ continuous) yield surface** — no corners, no discontinuities, no multi-surface junctions. This enables the analytical derivation of the plastic corrector.

## Yield Condition (Eq. 4)

```
f(σ) = τ − [(1−D)(μ_i p / (1 + μ_i p/(Y_m−Y₀)) + Y₀)
            + D·μ_d p / (1 + μ_d p/Y_m)]
            · (1 − Q/Q_melt)
```

### Parameters

| Symbol | Meaning |
|--------|---------|
| D | [[Damage Variable D]] (0 = intact, 1 = fully damaged) |
| μ_i, μ_d | Internal friction coefficients for intact and damaged material |
| Y₀ | Cohesion (zero-pressure shear strength) |
| Y_m | Ultimate shear strength limit (asymptotic bound) |
| Q = Q₀ + ΔQ | Total heat energy (Q₀ from initial temperature, ΔQ from plastic work — Eq. 40) |
| Q_melt | Heat energy at material melting point → drives thermal softening |

### Asymptotic Behavior

- For damaged material (D → 1): shear strength → μ_d p / (1 + μ_d p/Y_m) — a smooth asymptotic curve with Y_m as the upper limit
- For intact material (D → 0): reproduces the [[Lundborg Strength Model]]
- Thermal softening factor (1 − Q/Q_melt) reduces strength linearly as melting is approached

## Plastic Corrector (Eqs. 5a–5d)

Derived analytically from plastic flow theory — corrects **both shear and pressure simultaneously**:

```
Δλ = f(σ*) / (G + K·q_ψ·H)          (plastic multiplier)
p   = p* + K·q_ψ·Δλ                  (pressure correction)
τ   = τ* − G·Δλ                       (shear correction)
```

where **H** captures the local slope of the yield surface:

```
H = [(1−D)μ_i/(1+μ_i p/(Y_m−Y₀))² + D·μ_d/(1+μ_d p/Y_m)²] · (1 − Q/Q_melt)
```

### Plastic Strain Increment (Eqs. 6a–6c)

The plastic strain includes both deviatoric and spherical (volumetric) parts — a direct consequence of the coupled correction:

```
Δε^p = Δλ·r    where r = ∂ψ/∂σ  (plastic flow direction)
```

## Advantages over Traditional Radial Return

| Aspect | Radial Return | Modified Lundborg |
|--------|---------------|-------------------|
| Shear correction | ✓ | ✓ |
| Pressure correction | ✗ | ✓ |
| Follows yield surface normal | ✗ | ✓ (strictly) |
| Volumetric-deviatoric coupling | Decoupled | Coupled |
| Convergence in damage zones | Poor | Good |
| Shear+tensile stress waves | Decoupled | Reproduced together |

The difference is illustrated in **Fig. 2(b)**: the plastic flow correction path vs. the stress-scaling path in p–τ space.
