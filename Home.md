---
title: "MPM for Hypervelocity Asteroid Impacts — Concept Map"
paper: "The Material Point Method (MPM) for simulating hypervelocity impact on asteroids"
authors: "Xiaoran Yan, Patrick Michel, Ruichen Ni, Yifei Jiao, Junfeng Li"
year: 2026
---

# MPM for Hypervelocity Asteroid Impacts

A comprehensive concept map of the MPM framework for simulating hypervelocity impacts on asteroids.

## 1. Core Framework

- [[Material Point Method]] — The fundamental numerical method
- [[MPM Discretization]] — Material points and background grid discretization
- [[MPM Algorithm Steps]] — The explicit MUSL solution scheme
- [[GIMP Method]] — Generalized Interpolation for noise mitigation
- [[Leapfrog Integrator]] — Explicit time integration

## 2. Material Models (Constitutive Equations)

- [[Stress Tensor Decomhttps://github.com/cb-geo/mpmposition]] — Deviatoric + hydrostatic components
- [[Strength Models]] — Yield criteria and plastic flow
  - [[von Mises Yield Criterion]] — J2 flow theory
  - [[Drucker Prager Model]] — Pressure-dependent strength
  - [[Lundborg Strength Model]] — Pressure-dependent with upper limit
  - [[Modified Lundborg Model]] — C¹ continuous smoothed yield surface
- [[Equation of State]] — Pressure-density-energy relation
  - [[Tillotson EOS]] — The primary EOS used
  - [[Tillotson States]] — Compressed, cold/hot expanded, mixing region, vapor
  - [[Sound Speed in Solids]] — Bulk and longitudinal wave speed
- [[Damage Models]] — Material failure and fracture
  - [[Grady Kipp Fracture Model]] — Weibull flaw distribution
  - [[Weibull Distribution]] — Statistical strength theory
  - [[Weibull Parameters]] — k, m characterization
  - [[Resolution Independent Flaw Init]] — Poisson statistics approach
  - [[Brittle Fracture Criterion]] — Maximum principal stress

## 3. Plasticity Theory

- [[Plastic Flow Law]] — Return mapping algorithm
- [[Yield Surface]] — The boundary of elastic-plastic behavior
- [[Plastic Corrector]] — Stress return to yield surface
- [[Associated vs Non Associated Flow]] — Plastic potential

## 4. Governing Equations

- [[Conservation Laws]] — Mass, momentum, energy
- [[Updated Lagrangian Formulation]] — Reference configuration
- [[Jaumann Stress Rate]] — Objective stress rate
- [[Rate of Deformation Tensor]] — Kinematic condition
- [[Weak Form Formulation]] — Virtual work principle

## 5. Numerical Methods Context

- [[Comparison with SPH]] — Smoothed Particle Hydrodynamics
- [[Comparison with Grid Methods]] — CTH, iSALE
- [[Comparison with FDEM]] — Combined Finite-Discrete Element
- [[Cell Crossing Noise]] — MPM numerical challenge

## 6. Fragment Identification

- [[Fragment Search Algorithm]] — Density-based clustering
- [[Fragment Kinematics]] — Mass, velocity, angular momentum

## 7. Validation & Benchmarks

- [[Laboratory Impact Experiments]] — Nakamura & Fujiwara (1991)
- [[Nominal Benchmark Case]] — Basalt target + nylon projectile
- [[Discretization Convergence Study]] — Resolution independence
- [[Cumulative Mass Distribution]] — Fragment statistics
- [[Mass Velocity Distribution]] — Fragment kinematics
- [[Sensitivity on Impact Conditions]] — Angle, velocity, mass variations
- [[Sensitivity on Material Models]] — Damage and strength variations

## 8. Asteroid-Scale Application

- [[Asteroid Collision Simulation]] — 25 km target, 3.3 km projectile
- [[Eros Like Remnant]] — Formation of large coherent fragment
- [[DART Mission]] — Kinetic impactor on Dimorphos
- [[Hayabusa2 Mission]] — Artificial crater on Ryugu

## 9. Asteroid Science

- [[Hypervelocity Impact]] — Extreme collision phenomena
- [[Catastrophic Disruption]] — Global destruction threshold
- [[Gravitational Reaccumulation]] — Post-fragmentation phase
- [[Rubble Pile Asteroids]] — Gravitational aggregates
- [[Fractured Monolith]] — Shattered but intact bodies
- [[Asteroid Families]] — Collisional origin
- [[Planetary Defense]] — Kinetic impactor deflection

## 10. Discussion & Conclusions

- [[Interplay Material Models and Dynamics]] — Model-physics relationship
- [[MPM Unique Capabilities]] — Interface tracking, contact, boundary conditions
- [[Future Research Directions]] — Rubble-pile impact, regolith, binary asteroids
t fragment tracking and contact handling could provide better predictions for DART-like scenari