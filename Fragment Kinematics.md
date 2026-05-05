# Fragment Kinematics

The computation of kinematic quantities for each identified fragment, assuming rigid body motion (Eq. 20).

### Fragment Mass
m_f = Σ m_p
Sum of masses of all material points in the fragment.

### Center of Mass
x_fc = (Σ m_p·x_p) / m_f
Mass-weighted average position vector.

### Linear Momentum
P_f = Σ m_p·v_p
Sum of momenta of all points in the fragment.

### Angular Momentum
L_fc = Σ (x_p × m_p·v_p) − x_fc × P_f
Angular momentum referred to the center of mass.

### Angular Velocity
ω_f = J_c^{−1}·L_fc
Where J_c is the inertia matrix of the fragment referred to the center of mass coordinate system.

### Fragment Velocity
v_f = P_f/m_f
The center-of-mass translational velocity.

### Usage
These quantities are used to:
- Plot mass-velocity distributions ([[Mass Velocity Distribution]])
- Compute cumulative mass distributions ([[Cumulative Mass Distribution]])
- Compare with experimental data
- Provide initial conditions for gravitational reaccumulation (N-body/DEM) simulations

### Nominal Case Results
- Core fragment mass: 24.6% of target
- Core fragment velocity: 2.056 m/s
- Experimental core velocity: 1.35 m/s
- SPH core velocity: 1.352 m/s

The MPM core velocity is higher but still within the 3σ experimental confidence interval.

Link to: [[Fragment Search Algorithm]], [[Cumulative Mass Distribution]], [[Mass Velocity Distribution]]
