---
type: subject
discipline: physics
courses: ["PHY 284 (UMass, S. Hertel, Spring 2024)", "PHY 308 (Stony Brook, J. Pérez Ríos, Spring 2025)", "PHY 511 (UMich, A. Pierce, Fall 2025)"]
textbooks: ["OpenStax, University Physics Vol. 3", "Tipler & Llewellyn, Modern Physics", "Griffiths & Schroeter, Introduction to Quantum Mechanics (3rd ed.)", "Zwiebach, MIT 8.04 lecture notes", "Fleisch, A Student's Guide to the Schrödinger Equation", "Greensite, Physics 430 lecture notes", "Sakurai, Modern Quantum Mechanics"]
conventions: "[[University Physics]]"
status: levels A and B done
tags: [subject, quantum-mechanics]
---
# Quantum Mechanics

The quantum behaviour of light and matter and its applications to atoms, molecules, solids, nuclei and particles, in three levels: **A** introductory (University Physics Vol. 3 ch. 6–11; Tipler & Llewellyn; PHY 284), **B** upper-level (PHY 308; Griffiths & Schroeter; Zwiebach's MIT 8.04 notes, Fleisch and Greensite as supplements; the user's own Potential solutions, WKB and Classical notes), **C** graduate (PHY 511). Statements are marked by layer: *principles* (assumed), *laws* (empirical, with their range), *theorems* (derived, with a derivation and a *Uses:* line) and *models* (idealisations). Special relativity is in [[Relativity]]; the Hilbert-space mathematics is in [[Functional Analysis]]. At level B, ★ marks material beyond the course (PHY 308: its syllabus, homework and the user's notes): whole sections are starred in the lists below, and folded ★ callouts inside a section are side topics.

## Level A — introductory
- [[· A1 The Particle Nature of Light]]
- [[· A2 The Nuclear Atom and the Bohr Model]]
- [[· A3 Matter Waves and Uncertainty]]
- [[· A4 The Schrödinger Equation in One Dimension]]
- [[· A5 Atoms and Spin]]
- [[· A6 Molecules and Solids]]
- [[· A7 Nuclear Physics]]
- [[· A8 Particle Physics and Cosmology]]

## Level B — upper
- [[· B1 Wave Mechanics]]
- [[· B2 The Formalism of Quantum Mechanics]]
- [[· B3 One-Dimensional Potentials]]
- [[· B4 The Harmonic Oscillator]]
- [[· B5 Quantum Mechanics in Three Dimensions]]
- [[· B6 Spin]]
- [[· B7 Identical Particles]] (★ §B7.3)
- [[· B8 Time-Independent Perturbation Theory]] (★ §B8.2, §B8.4)
- [[· B9 The Variational Principle and the WKB Approximation]] (★ §B9.1, §B9.2)

## Level C — graduate
- [[· C1 Fundamental Concepts]]
- [[· C2 Position, Momentum and Translation]]
- [[· C3 Quantum Dynamics]]
- [[· C4 Propagators and Path Integrals]]
- [[· C5 Rotations and Angular Momentum]]
- [[· C6 Central Potentials]]
- [[· C7 Addition of Angular Momentum and Tensor Operators]]

### How the chapters build on each other
Arrows point from a chapter to the chapters that use it; labels count the citations from statements, derivations and *Uses:* lines. Dashed arrows are forward references.

```mermaid
graph TD
  A1["A1 The Particle Nature of Light"]
  A2["A2 The Nuclear Atom and the Bohr Model"]
  A3["A3 Matter Waves and Uncertainty"]
  A4["A4 The Schrödinger Equation in One Dimension"]
  A5["A5 Atoms and Spin"]
  A6["A6 Molecules and Solids"]
  A7["A7 Nuclear Physics"]
  A8["A8 Particle Physics and Cosmology"]
  B1["B1 Wave Mechanics"]
  B2["B2 The Formalism of Quantum Mechanics"]
  B3["B3 One-Dimensional Potentials"]
  B4["B4 The Harmonic Oscillator"]
  B5["B5 Quantum Mechanics in Three Dimensions"]
  B6["B6 Spin"]
  B7["B7 Identical Particles"]
  B8["B8 Time-Independent Perturbation Theory"]
  B9["B9 The Variational Principle and the WKB Approximation"]
  C1["C1 Fundamental Concepts"]
  C2["C2 Position, Momentum and Translation"]
  C3["C3 Quantum Dynamics"]
  C4["C4 Propagators and Path Integrals"]
  C5["C5 Rotations and Angular Momentum"]
  C6["C6 Central Potentials"]
  C7["C7 Addition of Angular Momentum and Tensor Operators"]
  A1 -->|3| A2
  A1 -->|1| A3
  A2 -->|1| A3
  A3 -->|20| A4
  A1 -->|6| A5
  A2 -->|2| A5
  A3 -->|5| A5
  A4 -->|9| A5
  A3 -->|1| A6
  A4 -->|4| A6
  A5 -->|15| A6
  A1 -->|6| A8
  A3 -->|2| A8
  A5 -->|2| A8
  A7 -->|1| A8
  A3 -->|3| B1
  A4 -->|18| B1
  A3 -->|7| B2
  A4 -->|7| B2
  B1 -->|9| B2
  A3 -->|2| B3
  A4 -->|15| B3
  B1 -->|8| B3
  A4 -->|5| B4
  B1 -->|4| B4
  B2 -->|16| B4
  B3 -->|3| B4
  A3 -->|2| B5
  A4 -->|8| B5
  A5 -->|6| B5
  A6 -->|1| B5
  B1 -->|4| B5
  B2 -->|18| B5
  B3 -->|4| B5
  B4 -->|4| B5
  A4 -->|1| B6
  B1 -->|3| B6
  B2 -->|7| B6
  B5 -->|19| B6
  A4 -->|2| B7
  A5 -->|4| B7
  A6 -->|4| B7
  B2 -->|2| B7
  B3 -->|2| B7
  B5 -->|6| B7
  B6 -->|4| B7
  A5 -->|2| B8
  B2 -->|8| B8
  B5 -->|12| B8
  B6 -->|17| B8
  A4 -->|5| B9
  A7 -->|4| B9
  B1 -->|1| B9
  B2 -->|4| B9
  B3 -->|11| B9
  B5 -->|7| B9
  B7 -->|3| B9
  B8 -->|5| B9
  A5 -->|1| C1
  B2 -->|22| C1
  B5 -->|2| C1
  B6 -->|4| C1
  B7 -->|1| C1
  B2 -->|19| C2
  C1 -->|2| C2
  B1 -->|1| C3
  B2 -->|14| C3
  B3 -->|6| C3
  B4 -->|9| C3
  B5 -->|1| C3
  B6 -->|5| C3
  B9 -->|2| C3
  C1 -->|7| C3
  C2 -->|11| C3
  B1 -->|1| C4
  B4 -->|4| C4
  B6 -->|1| C4
  C2 -->|10| C4
  C3 -->|10| C4
  B2 -->|3| C5
  B5 -->|8| C5
  B6 -->|4| C5
  C2 -->|2| C5
  C3 -->|1| C5
  B5 -->|22| C6
  B8 -->|1| C6
  C1 -->|1| C6
  C2 -->|1| C6
  C5 -->|9| C6
  B5 -->|2| C7
  B6 -->|8| C7
  C1 -->|1| C7
  C5 -->|22| C7
  A3 -.->|1| A1
  A4 -.->|1| A1
  A4 -.->|1| A2
  A5 -.->|4| A2
  A7 -.->|1| A2
  A4 -.->|1| A3
  B1 -.->|1| A3
  B2 -.->|6| A3
  A5 -.->|1| A4
  B1 -.->|1| A4
  B4 -.->|1| A4
  B2 -.->|1| A5
  B5 -.->|3| A5
  B6 -.->|3| A5
  B8 -.->|4| A5
  B4 -.->|1| A6
  B7 -.->|3| A6
  A8 -.->|2| A7
  B2 -.->|3| B1
  B4 -.->|1| B2
  B5 -.->|2| B2
  B6 -.->|1| B5
  B8 -.->|2| B5
  B9 -.->|2| B5
  C2 -.->|1| C1
  C5 -.->|2| C1
  C3 -.->|7| C2
  C4 -.->|1| C2
  C5 -.->|1| C3
  C6 -.->|1| C5
  C7 -.->|1| C6
```

## Planned
Chapters without notes yet; sources in brackets (∅ = no typed source).

**Level C — graduate (PHY 511; Sakurai; the user's 511 final review; series Part IV)**
C1 Fundamental concepts: Stern–Gerlach, kets, measurement, change of basis · C2 Position, momentum, translations · C3 Dynamics: pictures, two-state systems, oscillator · C4 Propagators, path integrals, Aharonov–Bohm · C5 Rotations, SU(2)/SO(3), angular-momentum spectrum · C6 Central potentials and hydrogen · C7 Addition of angular momentum, tensor operators, Wigner–Eckart · C8 Symmetries and approximation methods: symmetry operators, parity, selection rules, time-dependent perturbation theory, Fermi's golden rule, adiabatic approximation [Griffiths ch. 6, 11; PHY 512: ∅] · C9 Scattering [Griffiths ch. 10] · C10 Density matrices and entanglement [Griffiths ch. 12] · C11 Relativistic QM [∅; bridge to QFT]
