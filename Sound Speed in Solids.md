# Sound Speed in Solids

A critical parameter derived from the Equation of State, governing wave propagation and numerical stability.

### Bulk Sound Speed
For a 1D solid or fluid:
c_K² = ∂p/∂ρ|_S = ∂p/∂ρ|_E + (p/ρ²)·∂p/∂E|_ρ   (Eq. 12)

The isentropic derivative relates pressure change to density change.

### Wave Types in 3D Solids
- **Compressional (longitudinal) waves**: c_p = √(4G/3ρ + c_K²)   (Eq. 13)
- **Shear (transverse) waves**: propagate slower than longitudinal waves
- c_p is used as the reference sound speed in MPM calculations

### Roles of Sound Speed
1. **Plastic flow correction**: Affects Δλ through G = E_Y/(2(1+ν)) in Eq. 5a
2. **Critical time step**: Δt_cr = d_c / max(c_p + |v_p|) in Eq. 34
3. **Damage accumulation**: Crack growth velocity c_g = 0.4 c_p (Eq. 19)
4. **Artificial viscosity**: For capturing shock fronts (Neumann & Richtmyer, 1950)

Link to: [[Equation of State]], [[Tillotson EOS]], [[Critical Time Step]], [[Grady Kipp Fracture Model]]
