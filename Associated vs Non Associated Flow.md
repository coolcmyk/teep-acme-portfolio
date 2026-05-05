# Associated vs Non-Associated Flow

Classification of plastic flow rules based on the relationship between the yield function and the plastic potential.

### Associated Flow
- Plastic potential ψ ≡ f (same as yield function)
- Flow direction: r = ∂f/∂σ (normal to yield surface)
- Also called **normality rule**
- Used in von Mises (J2 flow theory)
- Appropriate for metals and pressure-insensitive materials
- Guarantees uniqueness and stability (Drucker's postulate)

### Non-Associated Flow
- Plastic potential ψ ≠ f (different from yield function)
- Flow direction: r = ∂ψ/∂σ (NOT normal to yield surface)
- Used for geological materials (rocks, soils)
- Captures shear-dilatant behavior: volumetric strain during shear
- Important for pressure-dependent materials where friction and dilatancy differ

### In This Paper
- Modified Lundborg model uses **non-associated flow**
- Plastic potential: ψ = τ − q_ψ·p  (Eq. 46)
- q_ψ: dilatancy coefficient (dilatancy angle)
- Used value: q_ψ = 0.256
- While the yield function uses: q_φ (friction angle, typically larger)

### Why Non-Associated for Geomaterials?
- Rocks exhibit less dilation than predicted by associated flow
- Friction angle > dilatancy angle in most geological materials
- Associated flow would overpredict volumetric expansion
- Using different potentials gives more realistic material response

Link to: [[Plastic Flow Law]], [[Plastic Corrector]], [[Modified Lundborg Model]], [[Drucker Prager Model]]
