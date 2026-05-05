# Lundborg Strength Model

(Lundborg, 1968)

## Motivation

The [[Drucker Prager Model]] predicts unbounded shear strength with increasing pressure. Lundborg introduced an asymptotic upper limit to better represent geological materials at high confining pressures.

## Intact Material Yield Stress

**σ_Y^i = Y₀ + (μ_i p) / (1 + μ_i p / (Y_m − Y₀))**  (Eq. 47)

where:
- **μ_i**: internal friction coefficient for intact material (equivalent to q_φ in Drucker-Prager)
- **Y₀**: cohesion — shear strength at zero pressure
- **Y_m**: ultimate shear strength limit — the asymptotic upper bound

At low pressure (p → 0), the strength approaches the Drucker-Prager line: σ_Y^i ≈ Y₀ + μ_i p. At high pressure (p → ∞), the strength saturates at Y_m.

## Tensile Strength

**p_t ≈ −Y₀ / μ_i**  (approximation valid when Y_m >> Y₀)

## Damaged Material (Collins et al., 2004)

Completely fragmented rock follows Coulomb dry-friction behavior:

**σ_Y^d = μ_d p**  (Eq. 48)

Constrained such that σ_Y^d ≤ σ_Y^i (damaged strength never exceeds intact strength).

## Damage Interpolation

**σ_Y = (1−D)σ_Y^i + D·σ_Y^d**  (Eq. 49)

where D is the [[Damage Variable D]] (0 = intact, 1 = fully fragmented).

## Thermal Softening (Jutzi, 2015)

A linear melting coefficient is introduced: **1 − u_I / u_{I-melt}**, where u_I is the specific internal energy and u_{I-melt} is the energy at the melting point. This reduces strength as the material approaches melting.

## Remaining Issue

The original Lundborg formulation still produces **non-smooth yield surface transitions** — resolved by the [[Modified Lundborg Model]].
