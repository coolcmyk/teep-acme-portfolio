# Jaumann Stress Rate

An objective (frame-invariant) stress rate used in MPM to ensure that constitutive equations satisfy material objectivity — meaning the material response is independent of the observer's frame of reference.

### The Problem
The Cauchy stress tensor σ characterizes the actual stress state, but its time derivative σ̇ is NOT objective under rigid body rotations. Constitutive equations require objective stress rates.

### Definition (Eq. 22)
σ^∇ = σ̇ − Ω·σ − σ·Ω^T

Where:
- σ^∇: Jaumann rate (co-rotational rate) of Cauchy stress
- σ̇: material time derivative of Cauchy stress
- Ω = ½(L − L^T): spin tensor (Eq. 23)
- L = ∂v/∂x: velocity gradient

The spin tensor Ω represents the rate of rigid body rotation. By subtracting the rotational contribution, the Jaumann rate tracks only the deformation-induced stress change.

### Usage in MPM Stress Update (Eq. 35)
σ_p^{n+1} = σ_p^n + (Ω^{n+1/2}·σ_p^n + σ_p^n·(Ω^{n+1/2})^T)·Δt^{n+1/2} + σ^∇(ε̇_p^{n+1/2}, σ_p^n, etc.)·Δt^{n+1/2}

The stress update has three components:
1. Previous stress σ_p^n
2. Rotational correction using spin tensor Ω
3. Jaumann rate contribution from constitutive model

### For Deviatoric Stress (Eq. 36)
s_p^{n+1} = s_p^n + (Ω^{n+1/2}·s_p^n + s_p^n·(Ω^{n+1/2})^T)·Δt + s^∇,n+1/2·Δt

Where s^∇ = 2G(ε̇ − ⅓tr(ε̇)I) for isotropic elastic materials (Hooke's law, Eq. 37).

Link to: [[Updated Lagrangian Formulation]], [[Rate of Deformation Tensor]], [[Conservation Laws]], [[MPM Algorithm Steps]]
