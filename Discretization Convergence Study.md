# Discretization Convergence Study

Systematic testing of different spatial resolutions to verify the robustness and resolution-independence of the MPM code (Section 4.1.1).

### Tested Resolutions
| d_point (mm) | N_target | Notes |
|-------------|----------|-------|
| 1.6 | 27,736 | Lowest |
| 1.4 | 41,328 | |
| 1.2 | 65,752 | Core fragment not fully formed |
| 1.0 | 113,104 | |
| 0.8 | 230,144 | **Nominal precision** |
| 0.8 | 115,072 | Half-particle (symmetry) |
| 0.6 | 523,984 | Highest: slight noise artifacts |

### Key Findings

**Temporal Evolution** (Fig. 5):
- Consistent trend across all resolutions: rapid damage increase in first 20 µs, then slower growth
- Failure ratio at 100 µs converges to ~52%
- Even low-resolution discrepancies < 10%

**Spatial Distribution** (Fig. 6):
- Similar damage and velocity distributions across resolutions
- Spallation occurs in all cases
- Core-shaped fragment appears only at higher resolution (d_point ≤ 1.0 mm)
- At d_point = 1.2 mm: failure zone can't develop into closed shell → additional damage around core

**Resolution Limits**:
- Too coarse: can't capture detailed features (no closed failure shell)
- Too fine (523,984 points): cell-crossing noise accumulates → slight expansion of failure region
- Optimal: plateau where statistical variables converge

### Convergence Criteria
- Plateau in total failure ratio (~52%)
- Stabilization of fragment morphologies
- Energy conservation

### Resolution-Independent Flaws
The convergence study explicitly supports the resolution-independent nature of the new Weibull flaw initialization method (see [[Resolution Independent Flaw Init]]).

Link to: [[Nominal Benchmark Case]], [[Cell Crossing Noise]], [[Resolution Independent Flaw Init]]
