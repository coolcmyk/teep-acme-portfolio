# Interplay Between Material Models and Dynamic Behavior

A key contribution of this paper: the detailed exploration of how constitutive models govern simulated physical behavior across multiple levels (Section 5.1).

### Level 1: Model Paradigm → Failure Mode
The choice of model paradigm dictates the fundamental failure mechanism:
- Maximum principal stress criterion → brittle fracture (instantaneous, catastrophic)
- Damage accumulation (Grady-Kipp) → progressive spallation
- Selection MUST reflect known physics of the target material

### Level 2: Model Parameters → Strength and Response
Within a paradigm, parameters control quantitative behavior:
- Weibull k and m → average damage strength, distribution width
- Y₀ (cohesion) → onset and extent of plasticity
- Generally consistent and continuous, barring other factors
- Physically sound models preserve fundamental failure patterns across scales:
  - Both lab-scale and asteroid-scale impacts exhibit spallation and intact cores
  - Primary difference: global extent of damage (energy scaling)

### Level 3: Mathematical Formulation → Physical Fidelity
The mathematical structure of the model determines its physical accuracy:

**Example 1 — Yield Surface Smoothness**:
- J2 flow theory (non-smooth corners) → decoupled shear and compression waves → less realistic
- Modified Lundborg (C¹ continuous) → corrects both simultaneously → realistic wave propagation

**Example 2 — Damage Correction Necessity**:
- Using stress instead of effective local tensile strain to calculate activated cracks (removing the (1−D) from Eq. 18 denominator) → significantly increased material strength → unphysical
- The (1−D) correction represents the reduced load-bearing cross-sectional area due to crack propagation → physically essential

### Practical Applications
- Model library for basalt established and benchmarked
- Methodology for model validation demonstrated
- Modular code design enables future material additions (metals, ices)
- Combines experimental data with numerical analysis to reverse-engineer material properties

Link to: [[Strength Models]], [[Damage Models]], [[Modified Lundborg Model]], [[Weibull Parameters]]
