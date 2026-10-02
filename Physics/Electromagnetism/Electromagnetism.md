---
type: subject
discipline: physics
courses: ["PHY 182 (UMass, S. Hertel)", "PHY 422 (UMass, A. Thamm, Spring 2024)", "PHY 505 (UMich, J. Wells, Fall 2025)"]
textbooks: ["OpenStax, University Physics Vol. 2", "Griffiths, Introduction to Electrodynamics (4th ed.)", "Nelson, PHYS 5516 notes (EMP)", "Zangwill, Modern Electrodynamics", "Likharev, Essential Graduate Physics — Classical Electrodynamics (supplement)"]
conventions: "[[University Physics]]"
status: levels A, B and C (C1–C7) done
tags: [subject, electromagnetism]
---
# Electromagnetism

Electric and magnetic fields, their sources, circuits, induction and electromagnetic waves, in three levels: **A** introductory (University Physics Vol. 2; PHY 182), **B** upper-level (Griffiths; PHY 422; Nelson's PHYS 5516 notes, Schwartz's Physics 15c lectures and McDonald's note as supplements), **C** graduate (PHY 505; Zangwill; the user's PHY 505 notes, the PHY 505 typed notes (earlier offering) and the series Part III; Likharev as a supplement), which starts from the Maxwell action and then rebuilds electrostatics at graduate depth. Statements are marked by layer: *principles* (assumed), *laws* (empirical, with their range), *theorems* (derived, with a derivation and a *Uses:* line) and *models* (idealisations). The mechanics it uses is in [[Classical Mechanics]]; optics is in [[Oscillations, Waves and Optics]], which also owns plane waves in media, the Fresnel equations, dispersion and skin depth; the covariant formulation and relativistic electrodynamics are at level C here. At level B, ★ marks material beyond the course (PHY 422: Griffiths ch. 1–9, its homework and exams): whole sections are starred in the lists below, and folded ★ callouts inside a section are side topics.

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

## Level B — upper
- [[· B1 Vector Calculus for Electrodynamics]]
- [[· B2 Electrostatics]]
- [[· B3 Boundary-Value Problems]]
- [[· B4 The Multipole Expansion]]
- [[· B5 Electric Fields in Matter]]
- [[· B6 Magnetostatics]]
- [[· B7 Magnetic Fields in Matter]]
- [[· B8 Electrodynamics]]
- [[· B9 Conservation Laws]]
- [[· B10 Electromagnetic Waves]] (★ §B10.3, §B10.4)
- [[· B11★ Potentials and Radiation]]

## Level C — graduate
- [[· C1 Electrodynamics from an Action]]
- [[· C2 Foundations of Electrostatics]]
- [[· C3 Electric Multipoles]]
- [[· C4 Conductors and Capacitance]]
- [[· C5 Dielectric Matter]]
- [[· C6 Laplace's Equation]] (★ §C6.4)
- [[· C7 Poisson's Equation]] (★ §C7.5)

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
  B1["B1 Vector Calculus for Electrodynamics"]
  B2["B2 Electrostatics"]
  B3["B3 Boundary-Value Problems"]
  B4["B4 The Multipole Expansion"]
  B5["B5 Electric Fields in Matter"]
  B6["B6 Magnetostatics"]
  B7["B7 Magnetic Fields in Matter"]
  B8["B8 Electrodynamics"]
  B9["B9 Conservation Laws"]
  B10["B10 Electromagnetic Waves"]
  B11["B11★ Potentials and Radiation"]
  C1["C1 Electrodynamics from an Action"]
  C2["C2 Foundations of Electrostatics"]
  C3["C3 Electric Multipoles"]
  C4["C4 Conductors and Capacitance"]
  C5["C5 Dielectric Matter"]
  C6["C6 Laplace's Equation"]
  C7["C7 Poisson's Equation"]
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
  A1 -->|2| B10
  A10 -->|2| B10
  A12 -->|1| B10
  A4 -->|2| B10
  A5 -->|1| B10
  B1 -->|3| B10
  B3 -->|5| B10
  B5 -->|1| B10
  B6 -->|1| B10
  B7 -->|1| B10
  B8 -->|14| B10
  B9 -->|14| B10
  B1 -->|17| B11
  B2 -->|7| B11
  B4 -->|3| B11
  B6 -->|9| B11
  B8 -->|2| B11
  B9 -->|2| B11
  A1 -->|14| B2
  A2 -->|2| B2
  A3 -->|8| B2
  A4 -->|2| B2
  B1 -->|25| B2
  A2 -->|3| B3
  A3 -->|5| B3
  B1 -->|8| B3
  B2 -->|6| B3
  A1 -->|5| B4
  A3 -->|5| B4
  B1 -->|6| B4
  B2 -->|3| B4
  B3 -->|4| B4
  A2 -->|2| B5
  A4 -->|3| B5
  B1 -->|21| B5
  B2 -->|13| B5
  B3 -->|7| B5
  B4 -->|5| B5
  A1 -->|2| B6
  A5 -->|1| B6
  A7 -->|9| B6
  A8 -->|4| B6
  B1 -->|25| B6
  B2 -->|7| B6
  B3 -->|4| B6
  B4 -->|3| B6
  A2 -->|2| B7
  A8 -->|4| B7
  B1 -->|19| B7
  B2 -->|1| B7
  B5 -->|11| B7
  B6 -->|19| B7
  A10 -->|2| B8
  A12 -->|4| B8
  A5 -->|1| B8
  A6 -->|2| B8
  A7 -->|2| B8
  A9 -->|1| B8
  B1 -->|9| B8
  B2 -->|12| B8
  B3 -->|2| B8
  B5 -->|9| B8
  B6 -->|29| B8
  B7 -->|7| B8
  B1 -->|4| B9
  B5 -->|3| B9
  B6 -->|10| B9
  B7 -->|2| B9
  B8 -->|7| B9
  B1 -->|9| C1
  B10 -->|2| C1
  B11 -->|8| C1
  B8 -->|2| C1
  B9 -->|13| C1
  A2 -->|3| C2
  B1 -->|16| C2
  B11 -->|2| C2
  B2 -->|13| C2
  B3 -->|6| C2
  B6 -->|3| C2
  B8 -->|2| C2
  B9 -->|1| C2
  C1 -->|12| C2
  B1 -->|6| C3
  B2 -->|5| C3
  B3 -->|7| C3
  B4 -->|7| C3
  B5 -->|1| C3
  C2 -->|17| C3
  A2 -->|1| C4
  A4 -->|4| C4
  B2 -->|11| C4
  B3 -->|8| C4
  B9 -->|1| C4
  C2 -->|25| C4
  C3 -->|2| C4
  B1 -->|19| C5
  B2 -->|11| C5
  B3 -->|6| C5
  B4 -->|11| C5
  B5 -->|25| C5
  B7 -->|1| C5
  B9 -->|2| C5
  C2 -->|6| C5
  C3 -->|5| C5
  C4 -->|2| C5
  B1 -->|4| C6
  B10 -->|1| C6
  B2 -->|2| C6
  B3 -->|12| C6
  B5 -->|1| C6
  C2 -->|7| C6
  C3 -->|3| C6
  C4 -->|6| C6
  B1 -->|7| C7
  B2 -->|2| C7
  B3 -->|15| C7
  B4 -->|1| C7
  B5 -->|1| C7
  C2 -->|5| C7
  C3 -->|5| C7
  C4 -->|2| C7
  C6 -->|47| C7
  A2 -.->|2| A1
  A4 -.->|1| A1
  A7 -.->|1| A1
  A11 -.->|1| A10
  B8 -.->|2| A10
  B10 -.->|3| A12
  B5 -.->|2| A12
  B7 -.->|2| A12
  B8 -.->|1| A12
  B9 -.->|2| A12
  A5 -.->|1| A2
  B1 -.->|1| A2
  B2 -.->|1| A2
  B3 -.->|2| A2
  A12 -.->|1| A4
  B2 -.->|2| A4
  B3 -.->|2| A4
  B6 -.->|1| A8
  A12 -.->|1| A9
  B2 -.->|1| B1
  B3 -.->|2| B1
  B11 -.->|1| B2
  B3 -.->|2| B2
  B5 -.->|1| B2
  B11 -.->|1| B6
  B8 -.->|3| B6
  B9 -.->|2| B6
  B8 -.->|2| B7
  B10 -.->|2| B8
  B11 -.->|2| B8
  C2 -.->|2| C1
  C5 -.->|1| C1
  C6 -.->|1| C1
  C3 -.->|1| C2
  C4 -.->|5| C2
  C5 -.->|1| C2
  C6 -.->|3| C2
  C7 -.->|2| C2
  C5 -.->|7| C3
  C6 -.->|6| C3
  C6 -.->|9| C4
  C7 -.->|1| C4
  C6 -.->|2| C5
  C7 -.->|5| C6
```

## Planned
Chapters without notes yet; sources in brackets (∅ = no typed source).

**Level C — beyond PHY 505 (★)**
C8★ Gauge fields beyond the vacuum: media from the action, monopoles and Dirac quantization, Chern–Simons [PHY 505 typed notes ch. 8; Jackson §6.11–6.12] · C9★ Radiation from moving charges beyond Griffiths: retarded Green function, covariant Liénard–Wiechert, multipole radiation, synchrotron and Cherenkov radiation, Abraham–Lorentz–Dirac [Zangwill ch. 20, 23; Likharev ch. 8, 10; Nelson ch. 41–44] · C10★ Guided waves and cavities [Zangwill ch. 19; Likharev §7.5–7.8] · magnetostatics II and quasistatics [Zangwill ch. 9–14] (optional)
