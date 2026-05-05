# Stress Tensor Decomposition

**σ = s − pI**  (Eq. 3)

## Components

- **σ**: Cauchy stress tensor — the total state of stress at a material point
- **s**: deviatoric (shear) stress component — governed by [[Strength Models]]
- **p**: isotropic hydrostatic pressure — governed by [[Equation of State]]
- **I**: identity tensor (second-order)

## Physical Interpretation

This decomposition separates the stress response into two independent physical mechanisms:

1. **Volumetric response** (pressure *p*): resistance to pure compression/dilation, determined by the material's equation of state. At high strain rates — such as hypervelocity impact — the EOS captures the shock-compression behavior where pressure depends on density and internal energy.

2. **Deviatoric response** (shear stress **s**): resistance to shape change without volume change. This is where the material's strength model operates — determining whether the material deforms elastically or plastically under shear.

## Role in Yield and Plastic Flow

- Deviatoric stress **s** determines yield initiation and plastic flow direction
- The von Mises effective stress `σ̄ = √(3J₂)` and `J₂ = ½ s:s` are computed from **s** alone
- Pressure *p* shifts the yield surface in stress space for pressure-dependent models (see [[Drucker Prager Model]], [[Modified Lundborg Model]])

## Influence of Damage

When damage is active (see [[Damage Variable D]]), both components are affected:

**σ = (1−D)s_E − p\*I**

where:
- `p* = (1−D)p` for tension
- `p* = p` for compression (no pressure reduction under compression)
- `s_E` is the elastic deviatoric stress

This asymmetric treatment ensures that damaged material retains compressive load-bearing capacity while losing tensile strength — consistent with the behavior of fractured geological materials.
