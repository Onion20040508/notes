---
type: subject
discipline: physics
courses: ["PHY 284 (UMass, S. Hertel, Spring 2024)", "PHY 308 (Stony Brook, J. Pérez Ríos, Spring 2025)", "PHY 511 (UMich, A. Pierce, Fall 2025)", "PHY 512 (UMich, Winter 2026)"]
textbooks: ["OpenStax, University Physics Vol. 3", "Tipler & Llewellyn, Modern Physics", "Griffiths & Schroeter, Introduction to Quantum Mechanics (3rd ed.)", "Zwiebach, MIT 8.04 lecture notes", "Fleisch, A Student's Guide to the Schrödinger Equation", "Greensite, Physics 430 lecture notes", "Sakurai & Napolitano, Modern Quantum Mechanics (3rd ed.)", "Likharev, Essential Graduate Physics — Quantum Mechanics"]
conventions: "[[University Physics]]"
status: levels A, B and C done
tags: [subject, quantum-mechanics]
---
# Quantum Mechanics

The quantum behaviour of light and matter and its applications to atoms, molecules, solids, nuclei and particles, in three levels: **A** introductory (University Physics Vol. 3 ch. 6–11; Tipler & Llewellyn; PHY 284), **B** upper-level (PHY 308; Griffiths & Schroeter; Zwiebach's MIT 8.04 notes, Fleisch and Greensite as supplements; the user's own Potential solutions, WKB and Classical notes), **C** graduate (PHY 511–512; Sakurai & Napolitano; the user's 511 final review and lecture-notes series Part IV; Griffiths & Schroeter and Likharev as supplements; hydrogen and radiation in Gaussian units). Statements are marked by layer: *principles* (assumed), *laws* (empirical, with their range), *theorems* (derived, with a derivation and a *Uses:* line) and *models* (idealisations). Special relativity is in [[Relativity]]; the Hilbert-space mathematics is in [[Functional Analysis]]. At levels B and C, ★ marks material beyond the course (PHY 308, resp. PHY 511–512: their syllabi, homework and the user's notes): whole chapters and sections are starred in the lists below, and folded ★ callouts inside a section are side topics. Level B is wave-function-centred, level C ket-and-operator-centred: where both treat a result, C links the B home and says what changes.

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
- [[· C8★ Symmetries in Quantum Mechanics]]
- [[· C9 Approximation Methods]]
- [[· C10 Scattering Theory]]
- [[· C11 Density Matrices and Entanglement]] (★ §C11.4, §C11.5)
- [[· C12★ Identical Particles and Second Quantization]]
- [[· C13★ Relativistic Quantum Mechanics]]

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
  C8["C8★ Symmetries in Quantum Mechanics"]
  C9["C9 Approximation Methods"]
  C10["C10 Scattering Theory"]
  C11["C11 Density Matrices and Entanglement"]
  C12["C12★ Identical Particles and Second Quantization"]
  C13["C13★ Relativistic Quantum Mechanics"]
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
  B2 -->|24| C1
  B5 -->|2| C1
  B6 -->|4| C1
  B7 -->|1| C1
  B1 -->|1| C10
  B5 -->|1| C10
  B9 -->|2| C10
  C1 -->|2| C10
  C2 -->|4| C10
  C3 -->|2| C10
  C4 -->|6| C10
  C5 -->|4| C10
  C6 -->|12| C10
  C7 -->|3| C10
  C9 -->|5| C10
  B2 -->|2| C11
  B6 -->|5| C11
  C1 -->|15| C11
  C2 -->|2| C11
  C3 -->|9| C11
  C4 -->|4| C11
  C9 -->|1| C11
  B6 -->|2| C12
  B7 -->|3| C12
  B8 -->|4| C12
  C1 -->|4| C12
  C2 -->|2| C12
  C3 -->|5| C12
  B1 -->|1| C13
  B6 -->|7| C13
  B8 -->|3| C13
  C12 -->|3| C13
  C2 -->|1| C13
  C4 -->|7| C13
  C5 -->|6| C13
  C6 -->|2| C13
  C7 -->|2| C13
  C8 -->|1| C13
  B2 -->|18| C2
  C1 -->|2| C2
  B1 -->|1| C3
  B2 -->|14| C3
  B3 -->|6| C3
  B4 -->|9| C3
  B5 -->|1| C3
  B6 -->|6| C3
  B9 -->|2| C3
  C1 -->|7| C3
  C2 -->|13| C3
  B1 -->|1| C4
  B4 -->|4| C4
  B6 -->|1| C4
  C2 -->|10| C4
  C3 -->|10| C4
  B2 -->|2| C5
  B5 -->|8| C5
  B6 -->|4| C5
  C2 -->|5| C5
  C3 -->|2| C5
  B5 -->|23| C6
  B8 -->|1| C6
  C1 -->|1| C6
  C2 -->|1| C6
  C5 -->|10| C6
  B5 -->|2| C7
  B6 -->|9| C7
  C1 -->|1| C7
  C5 -->|23| C7
  B2 -->|4| C8
  B3 -->|2| C8
  B5 -->|8| C8
  B7 -->|1| C8
  C2 -->|10| C8
  C3 -->|8| C8
  C5 -->|12| C8
  C6 -->|6| C8
  C7 -->|8| C8
  A5 -->|2| C9
  B2 -->|2| C9
  B6 -->|5| C9
  B8 -->|9| C9
  B9 -->|5| C9
  C1 -->|14| C9
  C2 -->|2| C9
  C3 -->|18| C9
  C4 -->|3| C9
  C5 -->|4| C9
  C6 -->|3| C9
  C7 -->|14| C9
  C8 -->|4| C9
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
  C3 -.->|5| C2
  C4 -.->|1| C2
  C5 -.->|1| C3
  C9 -.->|2| C3
  C6 -.->|1| C5
  C7 -.->|1| C6
```

## Planned
No chapters planned. Not covered at level C: the general (Racah) formula for Clebsch–Gordan coefficients, Young tableaux and a proof of spin–statistics; quantized fields continue in [[Quantum Field Theory I]].
