# Fragment Search Algorithm

A post-processing algorithm for identifying and statistically analyzing impact fragments from the set of material points after MPM simulation.

### Fragment Definition
A fragment is a contiguous region of **unfailed** material points (D < 0.9) bounded by a perimeter of **failed** points (D ≥ 0.9) (Benz & Asphaug, 1994).

### Algorithm Steps

**1. Labeling Extendable Points**
- Based on density-based spatial clustering (DBSCAN; Ester et al., 1996)
- Point is "extendable" if it has enough unfailed neighbors
- Prevents spurious connections via narrow "necks"

**2. Grid-Based Friends-of-Friends Search**
- Uses the background grid from MPM for rapid neighbor localization
- Material points are distinctly maintained without spatial overlap
- Algorithm assesses the ratio of unfailed material points within each grid cell
- Classifies adjacent extendable points → adds non-extendable points → adds failed layer

**3. Sequential Numbering**
- Start from an unassigned extendable point
- Expand to all connected extendable points
- Include adjacent non-extendable points
- Add surrounding failed layer as boundary
- Assign fragment ID and repeat for remaining points

**4. Handling Dust**
- Points not incorporated into any fragment (non-extendable or failed without connection)
- Considered finely fractured to dust (below resolution threshold)
- Not assigned fragment numbers

### Advantages of Grid-Based Approach
- Exploits the MPM background grid for efficient spatial localization
- No need for external contouring algorithms (α-shape in SPH)
- Fragment shape inherently determined by material point arrangement

### Fragment Kinematics
After identification, fragment kinematic quantities are computed (see [[Fragment Kinematics]]):
- Mass m_f
- Center of mass x_fc
- Linear momentum P_f
- Angular momentum L_fc
- Angular velocity ω_f

### Nominal Case Result
The algorithm generated 826 fragments from the laboratory-scale impact simulation, with the core mass at 24.6% of target mass.

Link to: [[Fragment Kinematics]], [[Cumulative Mass Distribution]], [[Mass Velocity Distribution]], [[Laboratory Impact Experiments]]
