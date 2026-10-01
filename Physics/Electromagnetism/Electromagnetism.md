---
type: subject
discipline: physics
courses: ["PHY 182 (UMass, S. Hertel)", "PHY 422 (UMass, A. Thamm, Spring 2024)", "PHY 505 (UMich, J. Wells, Fall 2025)"]
textbooks: ["OpenStax, University Physics Vol. 2", "Griffiths, Introduction to Electrodynamics", "Zangwill, Modern Electrodynamics"]
conventions: "[[University Physics]]"
status: level A in progress
tags: [subject, electromagnetism]
---
# Electromagnetism

Electric and magnetic fields, their sources, circuits, induction and electromagnetic waves, in three levels: **A** introductory (University Physics Vol. 2; PHY 182), **B** upper-level (Griffiths; PHY 422), **C** graduate (PHY 505; the series Part III). Statements are marked by layer: *principles* (assumed), *laws* (empirical, with their range), *theorems* (derived, with a derivation and a *Uses:* line) and *models* (idealisations). The mechanics it uses is in [[Classical Mechanics]]; optics is in Oscillations, Waves and Optics; the covariant formulation and relativistic electrodynamics are at level C here.

## Level A — introductory
- [[· A1 Electric Charges and Fields]]
- [[· A2 Gauss's Law]]
- [[· A3 Electric Potential]]
- [[· A4 Capacitance]]
- [[· A5 Current and Resistance]]
- [[· A6 Direct-Current Circuits]]
- [[· A7 Magnetic Forces and Fields]]
- [[· A8 Sources of Magnetic Fields]]
- [[· A9 Electromagnetic Induction]]
- [[· A10 Inductance]]
- [[· A11 Alternating-Current Circuits]]
- [[· A12 Electromagnetic Waves]]

### How the chapters build on each other
Arrows point from a chapter to the chapters that use it; labels count the citations from statements, derivations and *Uses:* lines. Dashed arrows are forward references.

```mermaid
graph TD
  A1["A1 Electric Charges and Fields"]
  A2["A2 Gauss's Law"]
  A3["A3 Electric Potential"]
  A4["A4 Capacitance"]
  A5["A5 Current and Resistance"]
  A6["A6 Direct-Current Circuits"]
  A7["A7 Magnetic Forces and Fields"]
  A8["A8 Sources of Magnetic Fields"]
  A9["A9 Electromagnetic Induction"]
  A10["A10 Inductance"]
  A11["A11 Alternating-Current Circuits"]
  A12["A12 Electromagnetic Waves"]
  A3 -->|2| A10
  A4 -->|4| A10
  A5 -->|4| A10
  A6 -->|7| A10
  A8 -->|6| A10
  A9 -->|8| A10
  A10 -->|8| A11
  A4 -->|3| A11
  A5 -->|6| A11
  A6 -->|9| A11
  A8 -->|1| A11
  A9 -->|3| A11
  A1 -->|5| A12
  A10 -->|2| A12
  A2 -->|2| A12
  A4 -->|2| A12
  A7 -->|5| A12
  A8 -->|1| A12
  A1 -->|11| A2
  A1 -->|10| A3
  A2 -->|14| A3
  A1 -->|4| A4
  A2 -->|5| A4
  A3 -->|17| A4
  A1 -->|2| A5
  A3 -->|3| A5
  A1 -->|2| A6
  A3 -->|6| A6
  A4 -->|3| A6
  A5 -->|15| A6
  A1 -->|1| A7
  A3 -->|2| A7
  A5 -->|5| A7
  A5 -->|1| A8
  A7 -->|4| A8
  A3 -->|3| A9
  A5 -->|7| A9
  A6 -->|8| A9
  A7 -->|8| A9
  A8 -->|2| A9
  A2 -.->|2| A1
  A4 -.->|1| A1
  A7 -.->|1| A1
  A11 -.->|1| A10
  A5 -.->|1| A2
  A12 -.->|1| A4
  A12 -.->|1| A9
```

## Planned
Chapters without notes yet; sources in brackets (∅ = no typed source).

**Level B — upper (PHY 422, Griffiths)**
B1 Electrostatics: field, potential, energy · B2 Boundary-value problems: Laplace, uniqueness, images, separation of variables · B3 Multipole expansion · B4 Dielectrics · B5 Magnetostatics, vector potential · B6 Magnetization · B7 Induction, Maxwell's equations, conservation laws · B8 EM waves in vacuum and matter [PHY 300, Fowles 1] · B9 Potentials and radiation [Schwartz 15c lectures; otherwise ∅]
PHY 422's lecture notes are handwritten scans; level B is planned from the typed PHY 422 homework sets and solutions and Griffiths.

**Level C — graduate (PHY 505)**
C1 Electrostatics II: Green's functions, capacitance matrix [PHY 505 HW; Zangwill] · C2 Multipoles II [PHY 505 HW8; the user's multipole-lattice paper] · C3 Covariant electrodynamics [series Part III; PHY 505 typed notes] · C4 Media from the action, monopoles, Chern–Simons [PHY 505 typed notes] · C5 Radiation from moving charges [∅] · C6 Waveguides and cavities [∅]
