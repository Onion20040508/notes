---
type: subject
discipline: physics
courses: ["PHY 287 (UMass, M. Kandula, Fall 2023)", "PHY 306 (Stony Brook, F. Ringer, Spring 2025)", "PHY 510 (UMich, X. Mao, Fall 2026)"]
textbooks: ["OpenStax, University Physics Vol. 2", "Schroeder, An Introduction to Thermal Physics", "Blundell & Blundell, Concepts in Thermal Physics", "Schwartz, Physics 181 Statistical Mechanics lectures", "Mao, PHY 510 notes", "Sethna, Statistical Mechanics"]
conventions: "[[University Physics]]"
status: "levels A and B done; level C in progress (C0–C6)"
tags: [subject, thermal-and-statistical-physics]
---
# Thermal and Statistical Physics

Temperature, heat, the kinetic theory of gases and the laws of thermodynamics, then statistical mechanics, in three levels: **A** introductory (University Physics Vol. 2; PHY 287), **B** upper-level (PHY 306; Schroeder; Blundell; Schwartz's statistical-mechanics lectures; the user's own notes), **C** graduate (PHY 510, Mao, chapters following the course notes; conventions in [[Mao PHY 510]], lectures in [[PHY 510 Course Log]]). Statements are marked by layer: *principles* (assumed), *laws* (empirical, with their range), *theorems* (derived, with a derivation and a *Uses:* line) and *models* (idealisations). The mechanics it uses is in [[Classical Mechanics]]. At level B, ★ marks material beyond the course (PHY 306: its syllabus, problem sets and the user's notes): whole sections are starred in the lists below, and folded ★ callouts inside a section are side topics.

## Level A — introductory
- [[· A1 Temperature and Heat]]
- [[· A2 The Kinetic Theory of Gases]]
- [[· A3 The First Law of Thermodynamics]]
- [[· A4 The Second Law of Thermodynamics]]

## Level B — upper
- [[· B1 The Mathematical Toolkit of Thermodynamics]]
- [[· B2 The Laws of Thermodynamics, Formally]]
- [[· B3 Thermodynamic Potentials]] (★ §B3.4)
- [[· B4 Probability and Fluctuations]]
- [[· B5 Kinetic Theory and Transport]] (★ §B5.2, §B5.3, §B5.4)
- [[· B6 The Microcanonical Ensemble and Entropy]]
- [[· B7 The Canonical and Grand Canonical Ensembles]]
- [[· B8 The Classical Ideal Gas and Equipartition]]
- [[· B9 Phases and Phase Transitions]] (★ §B9.2, §B9.3)
- [[· B10 Quantum Statistics]]
- [[· B11★ Photons and Phonons]]
- [[· B12★ Bose–Einstein Condensation]]
- [[· B13★ Fermi Gases]]

## Level C — graduate
- [[· C0 The Arrow of Time]]
- [[· C1 Thermodynamics after Carathéodory]]
- [[· C2 The Fundamental Assumption]]
- [[· C3 Classical and Quantum Microstates]]
- [[· C4a Entropy and Ensembles]] (★ §C4a.9)
- [[· C4b Quantum Gases]] (★ §C4b.9)
- [[· C5 From Microscopic Reversibility to the Master Equation]]
- [[· C6 Random Walks, Brownian Motion and Diffusion]]

### How the chapters build on each other
Arrows point from a chapter to the chapters that use it; labels count the citations from statements, derivations and *Uses:* lines. Dashed arrows are forward references.

```mermaid
graph TD
  A1["A1 Temperature and Heat"]
  A2["A2 The Kinetic Theory of Gases"]
  A3["A3 The First Law of Thermodynamics"]
  A4["A4 The Second Law of Thermodynamics"]
  B1["B1 The Mathematical Toolkit of Thermodynamics"]
  B2["B2 The Laws of Thermodynamics, Formally"]
  B3["B3 Thermodynamic Potentials"]
  B4["B4 Probability and Fluctuations"]
  B5["B5 Kinetic Theory and Transport"]
  B6["B6 The Microcanonical Ensemble and Entropy"]
  B7["B7 The Canonical and Grand Canonical Ensembles"]
  B8["B8 The Classical Ideal Gas and Equipartition"]
  B9["B9 Phases and Phase Transitions"]
  B10["B10 Quantum Statistics"]
  B11["B11★ Photons and Phonons"]
  B12["B12★ Bose–Einstein Condensation"]
  B13["B13★ Fermi Gases"]
  C0["C0 The Arrow of Time"]
  C1["C1 Thermodynamics after Carathéodory"]
  C2["C2 The Fundamental Assumption"]
  C3["C3 Classical and Quantum Microstates"]
  C4a["C4a Entropy and Ensembles"]
  C4b["C4b Quantum Gases"]
  C5["C5 From Microscopic Reversibility to the Master Equation"]
  C6["C6 Random Walks, Brownian Motion and Diffusion"]
  A1 -->|1| A2
  A1 -->|1| A3
  A2 -->|15| A3
  A1 -->|5| A4
  A2 -->|7| A4
  A3 -->|22| A4
  A2 -->|3| B10
  B5 -->|1| B10
  B7 -->|21| B10
  B8 -->|3| B10
  B9 -->|1| B10
  A1 -->|1| B11
  A3 -->|2| B11
  A4 -->|7| B11
  B10 -->|21| B11
  B3 -->|12| B11
  B7 -->|4| B11
  B8 -->|3| B11
  B10 -->|17| B12
  B7 -->|2| B12
  B9 -->|1| B12
  B10 -->|12| B13
  B11 -->|1| B13
  B3 -->|6| B13
  B4 -->|4| B13
  B6 -->|2| B13
  B7 -->|4| B13
  B8 -->|2| B13
  A2 -->|6| B2
  A3 -->|17| B2
  A4 -->|19| B2
  B1 -->|16| B2
  A1 -->|1| B3
  A2 -->|3| B3
  A3 -->|8| B3
  A4 -->|2| B3
  B1 -->|13| B3
  B2 -->|16| B3
  A1 -->|1| B4
  A2 -->|2| B4
  A1 -->|4| B5
  A2 -->|11| B5
  B4 -->|23| B5
  A1 -->|1| B6
  A2 -->|7| B6
  A3 -->|6| B6
  A4 -->|6| B6
  B1 -->|2| B6
  B2 -->|9| B6
  B3 -->|2| B6
  B4 -->|12| B6
  B1 -->|2| B7
  B2 -->|2| B7
  B3 -->|15| B7
  B4 -->|6| B7
  B6 -->|26| B7
  A2 -->|2| B8
  A3 -->|2| B8
  B2 -->|1| B8
  B4 -->|2| B8
  B6 -->|4| B8
  B7 -->|32| B8
  A2 -->|3| B9
  A3 -->|2| B9
  A4 -->|2| B9
  B1 -->|2| B9
  B3 -->|15| B9
  B4 -->|2| B9
  B7 -->|6| B9
  B8 -->|3| B9
  A1 -->|2| C1
  A3 -->|1| C1
  A4 -->|3| C1
  B1 -->|4| C1
  B2 -->|5| C1
  B3 -->|2| C1
  B4 -->|10| C2
  B6 -->|7| C2
  C0 -->|3| C2
  C1 -->|7| C2
  B10 -->|1| C3
  B5 -->|1| C3
  B6 -->|1| C3
  B3 -->|3| C4a
  B4 -->|4| C4a
  B6 -->|8| C4a
  B7 -->|9| C4a
  C1 -->|11| C4a
  C2 -->|13| C4a
  C3 -->|3| C4a
  B10 -->|11| C4b
  B11 -->|5| C4b
  B12 -->|6| C4b
  B13 -->|4| C4b
  B8 -->|2| C4b
  C1 -->|2| C4b
  C3 -->|3| C4b
  C4a -->|13| C4b
  B5 -->|3| C5
  C0 -->|4| C5
  C1 -->|4| C5
  C3 -->|1| C5
  C4a -->|4| C5
  B4 -->|17| C6
  B5 -->|1| C6
  B8 -->|4| C6
  C2 -->|2| C6
  C4a -->|2| C6
  C5 -->|9| C6
  A2 -.->|1| A1
  A3 -.->|2| A1
  B11 -.->|1| A1
  B5 -.->|3| A1
  B9 -.->|1| A1
  A3 -.->|4| A2
  B5 -.->|5| A2
  B8 -.->|6| A2
  A4 -.->|1| A3
  B3 -.->|1| A3
  B2 -.->|4| A4
  B6 -.->|4| A4
  B11 -.->|1| B10
  B12 -.->|3| B10
  B13 -.->|2| B10
  B13 -.->|1| B11
  B3 -.->|11| B2
  B9 -.->|1| B2
  B6 -.->|10| B3
  B7 -.->|5| B3
  B9 -.->|1| B3
  B5 -.->|1| B4
  B8 -.->|1| B4
  B6 -.->|3| B5
  B7 -.->|1| B6
  B8 -.->|7| B6
  B8 -.->|3| B7
  B10 -.->|3| B8
  B11 -.->|4| B8
```

## Planned
Chapters without notes yet. Level C follows the chapters of Mao's PHY 510 notes.

**Level C — graduate** (C0–C6 are written, above; Units 1 and 2 of PHY 510)
Unit 3 chapters (emergence of order, fluctuations and criticality, complexity, physics of learning) as they are lectured. The density operator has its home in [[· C11 Density Matrices and Entanglement|QM C11]].
