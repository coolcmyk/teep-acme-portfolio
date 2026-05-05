# Cumulative Mass Distribution

A statistical measure of fragment sizes from impact simulations, plotted as cumulative number N(> m_f/M_tar) vs normalized fragment mass.

### Definition
N(> m_f/M_tar): the number of fragments with mass greater than the given normalized mass value.

### Power-Law Relation (Fine Fragments)
For comminuted (finely fractured) fragments:
n(m) ∝ m^{−3/5}  (Nakamura & Fujiwara, 1991)

This appears as a straight line on a log-log plot.

### Nominal Case Results (Fig. 9)
- MPM results (orange) compared with:
  - Experiment (black circles): Nakamura & Fujiwara (1991)
  - SPH at 40 µs and 440 µs (blue asterisks)
  - Power-law relation (gray dashed line)
- Good agreement for fine fragments (normalized mass 10⁻⁵ to 10⁻³·³)
- Largest fragment: 24.6% of target mass (MPM) vs 31% (experiment), 30% (SPH)
- Relative difference ~21% — within typical 20-30% error margin for planetary hydrocodes (Pierazzo et al., 2008)

### Time Evolution Effect
- At 40 µs vs 100 µs: slight shrinkage of largest fragments
- Slight lifting of intermediate fragment distribution slope
- Due to continued damage growth breaking narrow connections

Link to: [[Mass Velocity Distribution]], [[Fragment Search Algorithm]], [[Laboratory Impact Experiments]], [[Nominal Benchmark Case]]
