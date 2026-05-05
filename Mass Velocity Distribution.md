# Mass-Velocity Distribution

The relationship between fragment mass and 3D velocity, characterizing the kinematic outcome of an impact event (Fig. 10).

### Experimental Data
- Nakamura & Fujiwara (1991): measured fragment velocities from side-view films
- 3σ error bars quantify uncertainty in mass and velocity
- Inner fragments (smaller, slower) omitted due to recognition difficulty
- Fitted power-law: V(m_f) = 6.4·(m_f/M_tar)^{−0.155}

### Key Observations
- General downward trend: larger fragments have lower velocity
- Core fragment (largest) has the lowest velocity
- Smaller fragments span a wide range of velocities

### Nominal Case Comparison (Fig. 10)
- **MPM simulation**: captures the general downward trend
- **Core fragment velocity**: 2.056 m/s (MPM) vs 1.35 m/s (experiment), 1.352 m/s (SPH)
- MPM overestimates core velocity but still within 3σ confidence interval
- Numerical scatter expected for individual fragments

### Why Core Velocity Differs
- Possible factors: GIMP over-suppression, strength model differences, plastic correction approach
- Despite deviation, the overall simulation aligns with empirical observations

### Angular Velocity
- Not included in comparison: measurement method not explicitly stated in referenced literature
- MPM can compute angular velocities per fragment (Eq. 20) for future studies

Link to: [[Cumulative Mass Distribution]], [[Fragment Kinematics]], [[Laboratory Impact Experiments]], [[Nominal Benchmark Case]]
