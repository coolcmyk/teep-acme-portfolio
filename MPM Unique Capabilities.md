# MPM's Unique Capabilities

The specific advantages of MPM for planetary impact science, positioning it to tackle previously intractable problems (Section 5.2).

### 1. Explicit Fragment Tracking
- Lagrangian material points naturally track fragment boundaries
- No post-processing required for 3D shapes (unlike SPH's α-shape)
- Direct analysis of fragment shape statistics
- Seamless coupling with DEM codes for long-term gravitational evolution

### 2. Contact Mechanics
- Grid-based contact algorithm (Bardenhagen et al., 2001)
- Natural treatment of contact between distinct bodies or internal layers
- Inherent non-slip constraint effectively addresses contact
- Can model: boulders in rubble piles, regolith-bedrock interfaces
- Major advantage over SPH (particle interpenetration issues)

### 3. Boundary Conditions
- Regular background grid enables arbitrary boundary conditions
- **Symmetric BCs**: reduce computational load (~25% less time, same precision)
- **Transmitting BCs**: avoid wasting resources on regions with minimal stress impact
- Not easily achieved in SPH

### 4. Computational Efficiency
- Grid-based spatial localization → faster neighbor finding than SPH
- No advection calculations → faster than Eulerian methods
- Simulations run on personal desktop (i7-7700) in hours without parallelization

### 5. Discontinuity Handling
- Can model complex internal structures: layered bodies, voids, boulder assemblies
- Opens door to studying shock propagation in rubble piles vs fractured monoliths
- Enables investigation of regolith layer and subsurface void effects on impact outcome

### 6. Hybrid Formulation
- Lagrangian particles: track history, interfaces, avoid convection
- Eulerian grid: handle large deformations, avoid mesh tangling
- Best of both worlds

Link to: [[Material Point Method]], [[Comparison with SPH]], [[Comparison with Grid Methods]], [[Future Research Directions]]
