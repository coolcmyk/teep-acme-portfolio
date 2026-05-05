# Comparison with Grid-Based Methods

Traditional Eulerian and Lagrangian grid-based hydrocodes commonly used in planetary impact science.

### Grid-Based Codes
- **CTH** (McGlaun et al., 1990): Eulerian, widely used
- **iSALE** (Wünnemann et al., 2006; Elbeshausen et al., 2009): Eulerian with some Lagrangian features

### Eulerian Methods

**Advantages**:
- No mesh distortion (grid is fixed)
- Stable for large deformations
- Well-established in shock physics

**Disadvantages**:
- Convection term difficult to solve accurately
- Difficulty tracking material boundaries and interfaces
- Advective remapping smears sharp interfaces
- History-dependent variables require special treatment
- Fragmentation tracking is challenging

### Lagrangian Methods

**Advantages**:
- Material interfaces naturally tracked
- History-dependent variables straightforward
- No convection term

**Disadvantages**:
- Grid distortion in large deformations
- Element entanglement
- Requires remeshing for extreme events

### MPM's Hybrid Solution
MPM combines the advantages of BOTH:
- Lagrangian material points → track interfaces, history, avoid convection
- Eulerian background grid → avoid mesh distortion, handle large deformations
- Grid reset each step → no element entanglement
- Grid-based neighbor localization → efficient

### What MPM Avoids
- **Eulerian problems**: No advective remapping, no smeared interfaces
- **Lagrangian problems**: No mesh tangling, no remeshing needed

Link to: [[Material Point Method]], [[Comparison with SPH]], [[Comparison with FDEM]]
