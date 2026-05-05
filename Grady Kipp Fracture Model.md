# Grady-Kipp Fracture Model

(Grady & Kipp, 1980; implemented in SPH by Benz & Asphaug, 1994)

A continuum fracture model for brittle solids based on the statistical distribution and dynamical propagation of incipient cracks.

### Core Assumptions
- Material contains a Weibull-distributed set of incipient flaws (see [[Weibull Distribution]])
- Flaws activate when local tensile strain exceeds their threshold
- Once activated, cracks grow at constant velocity c_g
- Each crack relieves stress in a volume ≈ its circumscribing sphere (Walsh, 1965)

### Key Equations

**Flaw activation** (Eq. 17):
n_act,p = n_f,p · (ε_eff,p / ε_min,p)^m_p

**Effective local tensile strain** (Eq. 18):
ε_eff,p = σ_max,p / ((1−D_p)·E_Y)

The (1−D_p) term in the denominator accounts for reduced load-bearing cross-sectional area due to existing damage — cracks propagate in the remaining intact material matrix.

**Damage growth rate** (Eq. 19):
d(D^{1/3})/dt = n_act · c_g / R_s

- c_g = 0.4 c_p: crack growth velocity (40% of longitudinal wave speed)
- R_s: effective radius of the subvolume when fully damaged
- Damage accumulation per particle is constrained to D_max = (n_act,p/n_f,p)^{1/3}

### Physical Behavior
- Naturally reproduces spallation (tensile fracture below surfaces)
- Stress response to damage is delayed by one time step → viscous-like filtering effect
- Produces core-shaped unfailed regions in impact simulations

### This Paper's Improvements
See [[Resolution Independent Flaw Init]] for the new Poisson-statistics-based initialization method.

Link to: [[Damage Models]], [[Weibull Distribution]], [[Weibull Parameters]], [[Resolution Independent Flaw Init]], [[Damage Variable D]]
