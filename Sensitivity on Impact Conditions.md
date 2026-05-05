# Sensitivity on Impact Conditions

Systematic exploration of how variations in impact parameters affect simulation outcomes (Section 4.1.4, Table 2).

### Parameters Varied

**Impact Angle** (α from surface normal):
- 0° (vertical): Momentum equivalent to 30° normal component with 0.91 kg·m/s → intense fragmentation, core mass < ¼ of nominal
- 30° (nominal)
- 45°: Normal component effectively reduced to 0.52 kg·m/s equivalent → insufficient for shell-like damage, no core formed

**Impact Velocity**:
- 2.7 km/s (reduced momentum): No core; largest fragment larger but faster
- 3.2 km/s (nominal): Core formed
- 3.7 km/s (increased momentum): Smaller core with higher velocity

**Projectile Mass** (by adjusting density, constant volume):
- 0.175 g (reduced): Core formed, larger mass, similar velocity
- 0.213 g (nominal)
- 0.225 g (increased): Core formed, smaller mass, higher velocity

### Key Findings

**Momentum Correlation**:
- Core formation and size directly correlate with initial projectile momentum
- Higher momentum → smaller core, higher velocity (more fracture severity)
- Too low momentum → no core (stress wave too weak for shell-like damage)

**Velocity Sensitivity > Mass Sensitivity**:
- Outcomes more sensitive to velocity than mass for equal momentum changes
- May be related to time step: velocity affects integration stability (Δt_cr constraint)

**General Principle**:
- Fragment distribution follows relationship with momentum component NORMAL to impact point
- Vertical impact = high normal component → intense fragmentation

Link to: [[Nominal Benchmark Case]], [[Laboratory Impact Experiments]], [[Sensitivity on Material Models]]
