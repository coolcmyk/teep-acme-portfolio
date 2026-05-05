# Brittle Fracture Criterion

A simplified, instantaneous failure mode for materials under extreme tensile loading.

### Mechanism
- Material particle immediately fails (D → 1) when:
  σ_max ≥ σ₀
- σ_max: maximum principal stress (after principal axis transformation)
- σ₀: critical fracture strength threshold

### Behavior
- Complete failure occurs in the same time step the stress threshold is reached
- Instantaneous stress release upon failure
- Produces severe, widespread fragmentation with many small irregular fragments

### Comparison with Damage Accumulation Mode

| Aspect | Brittle Fracture | Damage Accumulation |
|--------|-----------------|-------------------|
| Failure timing | Instantaneous | Gradual (over timesteps) |
| Stress response | Immediate release | Delayed by one time step |
| Effect on shock waves | No filtering | Viscous-like filtering |
| Typical outcome | Many small fragments | Spallation, core formation |
| Physical realism | Less realistic for geological materials | More realistic |

### When Used
- Alternative damage mode in the MPM code
- Useful for materials that fail catastrophically rather than through progressive damage
- Always produces more severe damage than equivalent-strength Weibull accumulation

Link to: [[Damage Models]], [[Damage Variable D]], [[Grady Kipp Fracture Model]]
