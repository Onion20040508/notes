---
type: subject
discipline: physics
courses: ["PHY 287 (UMass, M. Kandula, Fall 2023)", "PHY 306 (Stony Brook, F. Ringer, Spring 2025)"]
textbooks: ["OpenStax, University Physics Vol. 2", "Schroeder, An Introduction to Thermal Physics", "Blundell & Blundell, Concepts in Thermal Physics", "Schwartz, Physics 181 Statistical Mechanics lectures"]
conventions: "[[University Physics]]"
status: levels A and B done
tags: [subject, thermal-and-statistical-physics]
---
# Thermal and Statistical Physics

Temperature, heat, the kinetic theory of gases and the laws of thermodynamics, then statistical mechanics, in three levels: **A** introductory (University Physics Vol. 2; PHY 287), **B** upper-level (PHY 306; Schroeder; Blundell; Schwartz's statistical-mechanics lectures; the user's own notes), **C** graduate. Statements are marked by layer: *principles* (assumed), *laws* (empirical, with their range), *theorems* (derived, with a derivation and a *Uses:* line) and *models* (idealisations). The mechanics it uses is in [[Classical Mechanics]]. At level B, ★ marks material beyond the course (PHY 306: its syllabus, problem sets and the user's notes): whole sections are starred in the lists below, and folded ★ callouts inside a section are side topics.

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
  A2 -->|9| A3
  A1 -->|4| A4
  A2 -->|5| A4
  A3 -->|18| A4
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
  B10 -->|10| B13
  B3 -->|6| B13
  B4 -->|4| B13
  B6 -->|2| B13
  B7 -->|4| B13
  B8 -->|2| B13
  A2 -->|4| B2
  A3 -->|14| B2
  A4 -->|17| B2
  B1 -->|16| B2
  A1 -->|1| B3
  A2 -->|2| B3
  A3 -->|8| B3
  A4 -->|2| B3
  B1 -->|13| B3
  B2 -->|12| B3
  A1 -->|1| B4
  A2 -->|2| B4
  A1 -->|4| B5
  A2 -->|11| B5
  B4 -->|22| B5
  A1 -->|1| B6
  A2 -->|5| B6
  A3 -->|6| B6
  A4 -->|6| B6
  B1 -->|2| B6
  B2 -->|8| B6
  B3 -->|2| B6
  B4 -->|12| B6
  B1 -->|2| B7
  B2 -->|2| B7
  B3 -->|15| B7
  B4 -->|6| B7
  B6 -->|26| B7
  A2 -->|1| B8
  A3 -->|2| B8
  B4 -->|2| B8
  B6 -->|2| B8
  B7 -->|32| B8
  A2 -->|3| B9
  A3 -->|2| B9
  A4 -->|2| B9
  B1 -->|2| B9
  B3 -->|15| B9
  B4 -->|2| B9
  B7 -->|6| B9
  B8 -->|3| B9
  A3 -.->|2| A1
  A3 -.->|4| A2
  B5 -.->|2| A2
  B8 -.->|2| A2
  A4 -.->|1| A3
  B2 -.->|4| A4
  B6 -.->|4| A4
  B12 -.->|1| B10
  B13 -.->|1| B10
  B3 -.->|7| B2
  B6 -.->|9| B3
  B7 -.->|5| B3
  B9 -.->|1| B3
  B8 -.->|1| B4
  B6 -.->|3| B5
  B7 -.->|1| B6
  B8 -.->|6| B6
  B8 -.->|3| B7
  B10 -.->|1| B8
```

## Planned
Chapters without notes yet; sources in brackets (∅ = no typed source).

**Level C — graduate** (levels A and B are written, above)
C1 Foundations: Liouville, ergodicity [Schwartz, brief] · C2 Ising model, mean field, Landau theory [∅] · C3 Critical phenomena and the renormalization group [∅] · C4 Fluctuations and linear response [∅] · C5 Non-equilibrium: Boltzmann, Langevin, Onsager [∅] · C6 Density matrix [∅] (the density operator and quantum statistical mechanics are developed in [[· C11 Density Matrices and Entanglement|QM C11]])
