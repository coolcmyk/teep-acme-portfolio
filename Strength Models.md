# Strength Models

Constitutive models that define the yield limit and post-yield behavior of elastoplastic materials. They govern the deviatoric (shear) component of the stress tensor.

### Classification

**Pressure-Independent**:
- [[von Mises Yield Criterion]] — J2 flow theory, cylindrical yield surface
- Suitable for metals, non-porous ductile materials
- Yield strength is constant (or depends only on plastic strain)
- Includes linear hardening and Johnson-Cook extensions

**Pressure-Dependent**:
- [[Drucker Prager Model]] — cone-shaped yield surface, unbounded
- [[Lundborg Strength Model]] — asymptotic with upper limit Y_m
- [[Modified Lundborg Model]] — C¹ continuous smooth surface (this paper's innovation)
- Suitable for rocks, soils, geological materials
- Shear strength increases with confining pressure (friction)

### Key Parameters Across Models
| Parameter | Symbol | Meaning |
|-----------|--------|---------|
| Cohesion | Y₀ | Shear strength at zero pressure |
| Internal friction | μ_i, q_φ | Rate of strength increase with pressure |
| Ultimate limit | Y_m | Maximum possible shear strength |
| Dilatancy | q_ψ | Volumetric strain during shear |
| Damage friction | μ_d | Friction coefficient for fully damaged material |

### Role in Impact Simulations
- The choice of strength model affects:
  - Wave propagation (shear vs compression wave coupling)
  - Damage pattern development
  - Core fragment formation
  - Fragment size and velocity distributions

In the lab impact experiments (Section 4.1), linear hardening with σ_Y = 3500 MPa was the nominal case. The modified Lundborg model was tested with Y₀ values of 10, 60, and 600 MPa.

Link to: [[Stress Tensor Decomposition]], [[Yield Surface]], [[Plastic Corrector]], [[von Mises Yield Criterion]], [[Drucker Prager Model]], [[Lundborg Strength Model]], [[Modified Lundborg Model]]
