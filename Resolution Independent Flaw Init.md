# Resolution-Independent Flaw Initialization

A new approach proposed in this paper (Section 3.3) using Poisson statistics to initialize the Weibull flaw distribution reliably and independently of discretization precision.

### Problems with Classical Approach
1. Total number of flaws n_tot depends on discretization (n_tot = n_p·ln(n_p))
2. Average activation strain becomes precision-dependent
3. May be inefficient for large particle sets (Ševeček, 2021)

### The New Four-Step Method

**Step 1 — Determine n_tot**
- Based on physical object sizes: pebbles, regolith grains, or crystal substructure
- Must be sufficiently large: n_tot > 100 n_p

**Step 2 — Determine ε_min,p (active strain)**
- Smallest activation strain varies by an order of magnitude across particles
- Range: ε_min,p ∈ [(10^m/kV)^{−1/m}, (1/kV)^{−1/m}]
- Random seed determines each particle's value
- Average active strain: ε̄_min = 10m/(m+1)·ε_min,V

**Step 3 — Determine n_f,p (flaw count per particle)**
- Flaw assignment follows binomial distribution B(n_tot, 1/n_p)
- Since n_tot is large and P_s·n_tot > 100:
  - Approximated as normal distribution N(P_s·n_tot, P_s·n_tot·(1−P_s))
- Generate random seed → standard normal table → map to normal → n_f,p

**Step 4 — Determine ε_max,p (largest activation strain)**
- N_max,p (biggest flaw number) follows exponential distribution
- N_max,p = n_tot − ln(x)/ln(1−1/n_p) where x is a random seed
- ε_max,p = (N_max,p/kV)^{1/m}

### Benefits
- Resolution-independent: no effect on discretization precision (validated in Section 4.1.1)
- More efficient for large particle sets
- Physically motivated by actual material substructure

Link to: [[Grady Kipp Fracture Model]], [[Weibull Distribution]], [[Weibull Parameters]], [[Discretization Convergence Study]]
