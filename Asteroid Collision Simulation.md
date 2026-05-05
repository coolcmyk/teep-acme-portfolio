# Asteroid Collision Simulation

A pseudo-catastrophic collision scenario used to validate MPM at asteroid scales (Section 4.2, Fig. 11).

### Setup
- **Target**: S-type basalt spheroid, 25 km diameter, ~2.7 g/cm³, mass ~2.2×10¹⁶ kg
- **Projectile**: S-type basalt spheroid, 3.3 km diameter, ~2.69 g/cm³, mass ~5.1×10¹³ kg
- **Impact velocity**: 5 km/s
- **Impact angle**: 45°

### Why Idealized?
- Real asteroids have irregular shapes and potential differentiation
- Spherical homogeneous geometry provides controlled baseline
- Isolates effects of material models
- Directly benchmarkable against SPH studies (Michel & Richardson, 2013)

### Material Variations (4 Cases)

**Case Labels**: [strength model][damage strength]
- a1: Linear hardening + low damage strength (~0.4 MPa)
- a2: Linear hardening + high damage strength (~40 MPa)
- b1: Modified Lundborg + low damage strength (~0.4 MPa)
- b2: Modified Lundborg + high damage strength (~40 MPa)

### Strength Model Parameters (Table 6)
| Parameter | Linear Hardening | Modified Lundborg |
|-----------|-----------------|-------------------|
| σ_Y | 3500 MPa | — |
| E^p | 5.31 MPa | — |
| μ_i | — | 1.5 |
| μ_d | — | 0.8 |
| Y₀ | — | 90 MPa |
| Y_m | — | 1500 MPa |
| q_ψ | — | 0.256 |

### Damage Parameters (Table 7)
| Case | Target k | Target σ̄_max | Projectile k | Projectile σ̄_max |
|------|----------|-------------|--------------|-----------------|
| Low (1) | 3.0×10³⁹ | ~0.4 MPa | 3.0×10³⁹ | ~0.85 MPa |
| High (2) | 5.0×10²² | ~40 MPa | 1.5×10²⁵ | ~41 MPa |

### Simulation Duration
- Nominal: 100 s
- Focus snapshot: 15 s (stress wave speed = 4.435 km/s, ~5.6 s to traverse target diameter)
- After ~2 reflections, stress waves no longer cause significant damage accumulation

### Key Results
- Low damage strength (cases a1, b1): complete failure of both bodies → rubble pile formation
- High damage strength (cases a2, b2): large undamaged fragments survive
- Modified Lundborg (b2): largest remnant is prolate, 16 km max dimension → resembles Eros
- Strength model choice has minor effect on damage patterns but affects velocity fields (shear banding)

Link to: [[Eros Like Remnant]], [[Weibull Parameters]], [[Fractured Monolith]], [[Rubble Pile Asteroids]]
