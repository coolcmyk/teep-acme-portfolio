# Comparison with SPH

Smoothed Particle Hydrodynamics (SPH) is the other major particle-based method used in asteroid impact simulations. Both MPM and SPH are mesh-free in their Lagrangian particle representation.

### SPH Codes Used for Asteroids
- **Bern SPH** (Benz & Asphaug, 1994, 1995; Jutzi et al., 2008; Jutzi, 2015)
- **Spheral** (Owen et al., 1998)
- **Miluphcuda** (Schäfer et al., 2016)

### Key Differences

| Aspect | SPH | MPM |
|--------|-----|-----|
| Density representation | Smoothing kernel for physical density interpolation | Dirac delta as quadrature tool |
| Neighbor search | Requires finding neighbor particles (computationally expensive) | Grid-based localization (efficient) |
| Boundary conditions | Difficult to impose specific BCs | Natural via background grid nodes |
| Tensile instability | Known issue (Monaghan, 2000) | Not present (grid provides structure) |
| Contact mechanics | Difficult (particle interpenetration) | Natural via grid-based contact algorithm |
| Fragment tracking | Requires post-processing (α-shape) | Explicit via material point connectivity |
| Advection | Handled by particle motion | No advection (history on material points) |
| Computational cost | Higher for neighbor search | Lower for equivalent resolution |

### SPH Strengths
- Well-established in planetary science
- Extensively validated and benchmarked
- Large body of existing results
- Natural for self-gravitating problems

### MPM Strengths
- No tensile instability
- Natural contact and boundary condition handling
- Explicit fragment tracking
- Efficient spatial localization via grid
- Moves beyond idealized targets to complex real-world structures

### Benchmarking in This Paper
The MPM framework is benchmarked against SPH results from Benz & Asphaug (1994, 1995) using the same Nakamura-Fujiwara (1991) laboratory impact experiments.

Link to: [[Material Point Method]], [[MPM Discretization]], [[Laboratory Impact Experiments]]
