# Plastic Corrector

The numerical algorithm that adjusts the stress state from the elastic trial solution back to the physically admissible yield surface.

### When Triggered
- Compute elastic trial stress σ* (assuming purely elastic response)
- Evaluate yield function f(σ*) 
- If f(σ*) > 0: plastic loading — correction needed
- If f(σ*) ≤ 0: elastic response — no correction

### Two Approaches Compared

#### 1. Simplified Radial Return (Deviatoric Stress Scaling)
Used in classical shock-physics codes (Jutzi et al., 2015):
- Simply multiply deviatoric stress by σ_Y/τ*:
  s = (σ_Y/τ*)·s*
- Only corrects shear stress components
- Does NOT correct pressure
- FAILS to follow yield surface normal
- Decouples volumetric and deviatoric plastic strain increments

#### 2. Plastic Flow Correction (This Work)
Based on plastic flow theory with analytical derivation:
- Corrects BOTH shear and pressure simultaneously
- Strictly follows yield surface normal
- Couples volumetric and deviatoric plastic strain

**For Modified Lundborg** (Eqs. 5a-5d):
```
Δλ = f(σ*)/(G + K·q_ψ·H)        [plastic multiplier]
p   = p* + K·q_ψ·Δλ             [pressure correction]
τ   = τ* − G·Δλ                 [shear correction]
s   = s* · (τ/τ*)               [deviatoric stress scaling]
```
Where H = [(1−D)μ_i/(1+μ_i·p/(Y_m−Y₀))² + D·μ_d/(1+μ_d·p/Y_m)²]·(1−Q/Q_melt)

Solution requires iteration: substitute Δλ into p equation, solve for p, then back-substitute.

### Visual Comparison (Fig. 2b)
The enlarged view in Fig. 2(b) shows how the plastic flow correction path differs from the simplified stress scaling path in the p–τ plane.

Link to: [[Plastic Flow Law]], [[Yield Surface]], [[Modified Lundborg Model]], [[Strength Models]]
