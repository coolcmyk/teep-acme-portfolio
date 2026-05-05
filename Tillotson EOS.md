# Tillotson EOS

The main equation of state used in the paper (Tillotson, 1962; Brundage, 2013).

Combines the Hugoniot curve with the Thomas-Fermi model to represent solid/liquid and gaseous phases of materials. Provides full coverage of the density-energy space in a concise form.

### Key Variables
- η = ρ/ρ₀ (compression ratio)
- μ = η − 1 (volumetric strain)
- ν = 1/η − 1 (specific volume change)
- ρ₀: initial reference density

### Tillotson Parameters
- E₀: energy scale parameter
- E_iv: incipient vaporization energy
- E_cv: complete vaporization energy
- ρ_iv: incipient vaporization density
- A = ρ₀C²: where C is low-pressure sound speed
- B: compression coefficient
- a = 0.5 (always); a+b = Grüneisen coefficient at zero pressure
- α, β: expansion parameters for hot state

### Four Main Regions
See [[Tillotson States]] for detailed descriptions.

### Basalt Parameters (from Buruchenko et al., 2017)
| Parameter | Value |
|-----------|-------|
| ρ₀ | 2700 kg/m³ |
| E₀ | 4.72 MJ/kg |
| E_iv | 18.2 MJ/kg |
| E_cv | 2000 MJ/kg (very large, effectively never reached) |
| ρ_iv | 26.7 kg/m³ |
| A | 26.7 GPa |
| B | 26.7 GPa |
| a | 0.5 |
| b | 1.5 |
| α | 5 |
| β | 5 |

Link to: [[Equation of State]], [[Tillotson States]], [[Sound Speed in Solids]]
