# Damage Variable D

A scalar state variable (0 ≤ D ≤ 1) representing the degree of material degradation due to fracture.

### Definition
- D = 0: completely intact (undamaged) material
- D = 1: fully failed/fractured material
- Intermediate values: partially damaged (microcracks present but material still cohesive)

### Effect on Stress (Eq. 14)
σ = (1−D)·s_E − p*·I
- s_E: elastic deviatoric stress (without damage consideration)
- p* = (1−D)p for tensile cases; p* = p for compressive cases (Benz & Asphaug, 1994)

Damage reduces the effective load-bearing capacity of the material.

### Effect on Strength (Eq. 4, Eq. 49)
σ_Y = (1−D)·σ_Y^i + D·σ_Y^d
- Interpolates between intact (σ_Y^i) and fully damaged (σ_Y^d) yield surfaces

### Damage Growth
- Governed by the Grady-Kipp model: d(D^{1/3})/dt = n_act·c_g/R_s (Eq. 19)
- Upper limit per particle: D_max = (n_act,p/n_f,p)^{1/3}
- Not allowed to decrease (irreversible)

### Failure Threshold
- In post-processing: D > 0.9 considered "failed"
- Compensates for insufficient damage development due to time truncation

### Damage Modes
1. **Accumulation mode**: gradual growth via crack propagation; stress updated next time step
2. **Brittle fracture mode**: instantaneous D → 1 when maximum principal stress exceeds threshold

Link to: [[Damage Models]], [[Grady Kipp Fracture Model]], [[Brittle Fracture Criterion]], [[Stress Tensor Decomposition]]
