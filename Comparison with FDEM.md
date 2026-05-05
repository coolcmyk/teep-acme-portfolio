# Comparison with FDEM

The Combined Finite-Discrete Element Method (FDEM) is another approach that bridges continuum mechanics and discrete particle interactions.

### What is FDEM?
(Munjiza et al., 1995)
- Combines finite element continuum modeling with discrete element interactions
- Models transition from continuum deformation to fracture
- After fracture: elements become discrete interacting bodies
- Naturally transitions from continuum fracturing to discrete fragment interactions

### Comparison with MPM

| Aspect | FDEM | MPM |
|--------|------|-----|
| Continuum phase | Finite elements | Material points on grid |
| Fracture treatment | Element separation | Damage variable on particles |
| Post-fracture | Discrete elements with contact | Material points remain; fragments identified via clustering |
| Contact handling | DEM-based contact laws | Grid-based contact (non-slip) |
| Deformation limits | Element distortion before fracture | No distortion limit (grid reset) |
| Implementation | Requires element splitting/removal | Damage variable handles weakening |

### MPM Advantages
- Explicit fragment tracking without element splitting
- Continuous damage variable (0→1) rather than binary element separation
- Grid reset avoids mesh distortion in pre-fracture regime
- Efficient spatial localization

### Future Direction
The paper suggests MPM can be directly coupled with DEM codes for long-term gravitational evolution studies, providing a seamless alternative to FDEM or SPH-DEM.

Link to: [[Material Point Method]], [[Comparison with SPH]], [[Comparison with Grid Methods]], [[Fragment Search Algorithm]]
