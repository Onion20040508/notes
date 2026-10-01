---
type: subject
discipline: physics
courses: ["PHY 181 (UMass, Fall 2022)", "PHY 421 (UMass, Fall 2023)"]
textbooks: ["OpenStax, University Physics Vol. 1", "Marion & Thornton, Classical Dynamics", "Landau & Lifshitz, Mechanics"]
conventions: "[[University Physics]]"
status: level A in progress
tags: [subject, classical-mechanics]
---
# Classical Mechanics

The mechanics of particles, rigid bodies and fluids, in three levels: **A** introductory (University Physics Vol. 1; PHY 181), **B** upper-level (Newtonian, Lagrangian and Hamiltonian mechanics; PHY 421, the series Part II), **C** graduate (classical field theory and beyond). Statements are marked by layer: *principles* (assumed), *laws* (empirical, with their range), *theorems* (derived, with a derivation and a *Uses:* line) and *models* (idealisations). Oscillations, waves and sound are in [[Oscillations, Waves and Optics]]; relativistic mechanics in Relativity.

## Level A — introductory
- [[· A1 Units, Measurement and Vectors]]
- [[· A2 Kinematics]]
- [[· A3 Newton's Laws of Motion]]
- [[· A4 Work and Energy]]
- [[· A5 Linear Momentum and Collisions]]
- [[· A6 Rotation]]
- [[· A7 Static Equilibrium and Elasticity]]
- [[· A8 Gravitation]]
- [[· A9 Fluid Mechanics]]

### How the chapters build on each other
Arrows point from a chapter to the chapters that use it; labels count the citations from statements, derivations and *Uses:* lines. Dashed arrows are forward references.

```mermaid
graph TD
  A1["A1 Units, Measurement and Vectors"]
  A2["A2 Kinematics"]
  A3["A3 Newton's Laws of Motion"]
  A4["A4 Work and Energy"]
  A5["A5 Linear Momentum and Collisions"]
  A6["A6 Rotation"]
  A7["A7 Static Equilibrium and Elasticity"]
  A8["A8 Gravitation"]
  A9["A9 Fluid Mechanics"]
  A1 -->|10| A2
  A2 -->|6| A3
  A3 -->|5| A4
  A3 -->|9| A5
  A4 -->|1| A5
  A1 -->|6| A6
  A2 -->|5| A6
  A3 -->|7| A6
  A4 -->|11| A6
  A5 -->|5| A6
  A1 -->|1| A7
  A5 -->|4| A7
  A6 -->|6| A7
  A1 -->|1| A8
  A2 -->|7| A8
  A3 -->|8| A8
  A4 -->|9| A8
  A6 -->|3| A8
  A2 -->|1| A9
  A3 -->|3| A9
  A4 -->|5| A9
  A7 -->|1| A9
  A8 -->|2| A9
  A3 -.->|2| A2
  A8 -.->|3| A2
  A6 -.->|1| A3
  A7 -.->|1| A3
  A9 -.->|1| A3
  A8 -.->|2| A4
  A7 -.->|2| A6
  A9 -.->|1| A8
```

## Planned
Chapters without notes yet; sources in brackets (∅ = no typed source).

**Level B — upper (PHY 421, Marion & Thornton, series Part II)**
B1 Newtonian mechanics and conservation theorems · B2 Central forces and orbits · B3 Systems of particles, rigid bodies about an axis · B4 Collisions and scattering [Landau] · B5 Calculus of variations [series II] · B6 Lagrangian mechanics, constraints, Noether [series II] · B7 Hamiltonian mechanics, phase space, Liouville [series II] · B8 Poisson brackets, canonical transformations, Hamilton–Jacobi [series II] · B9 Non-inertial frames [∅] · B10 3D rigid bodies, Euler equations, tops [∅]

**Level C — graduate**
C1 Classical field theory [series III; PHY 505 typed notes] · C2 Elasticity and fluids as field theories [PHY 505 typed notes] · C3 Action-angle variables, adiabatic invariants, perturbation theory [∅] · C4 Nonlinear dynamics and chaos [∅] · C5 Geometric mechanics [∅]

PHY 421's lecture notes are handwritten scans, so level B is planned from the typed sources: the series Part II, the PHY 421 homework sets, and Marion & Thornton.
