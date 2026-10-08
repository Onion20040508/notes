---
type: subject
discipline: physics
courses: ["PHY 513 (UMich, F. Larsen, Fall 2026)"]
textbooks: ["Peskin & Schroeder, An Introduction to Quantum Field Theory", "Yu Zhao-Huan (余钊焕), Lecture Notes on Quantum Field Theory (量子场论讲义)", "Schwartz, Quantum Field Theory and the Standard Model (further reading)"]
conventions: "[[Larsen PHY 513]]"
status: level C — C1a, C1b, C2a, C2b, C3, C4, C5a, C5b (§C5b.1–§C5b.4, §C5b.7, §C5b.9 taught; §C5b.5, §C5b.6, §C5b.8 drafts), C9 (§C9.1, §C9.3–§C9.4 parity, taught; ★ §C9.2 scalar parity), CA written, CB skeleton (all statements in reading order; proofs being filled)
tags: [subject, quantum-field-theory]
---
# Quantum Field Theory

Relativistic quantum field theory at the graduate level (**C**, PHY 513, Larsen, Fall 2026; textbook Peskin & Schroeder). Chapters follow Yu Zhao-Huan's lecture notes (余钊焕《量子场论讲义》), whose chapter numbers they keep: fields are organized by spin after the Poincaré group, and interactions are treated once for all fields. Each concept has one home: statements are short boxes, derivations are folded under them, explanations are titled remarks, and hidden connections are collected in each note's Connections. Multi-step procedures have their own notes in Procedures/, linked from every place they are carried out. Statements are marked by layer: *principles* (postulated), *theorems* (derived, with a derivation and a *Uses:* line) and *models* (idealized systems). ★ marks material beyond the PHY 513 syllabus; a *draft* banner marks syllabus topics written ahead of the lectures. Relativity is in [[Relativity]], one-particle quantum mechanics in [[Quantum Mechanics]]. Procedures: [[P1 Canonical Quantization]], [[P2 Green's Functions by Contour Integration]]. Reference card: [[Scalar Field Card]]. Two mathematics chapters collect the tools the physics uses: [[· CA Mathematical Methods]] (limits, generalized functions, Fourier transforms, contours) and [[· CB Lie Groups, Lie Algebras and Representations]] (Lie groups and algebras, complexification, representations, Clifford algebras and the spin groups). The course order, lecture by lecture, is in [[PHY 513 Course Log]]; conventions in [[Larsen PHY 513]].

## Level C — graduate
- [[· C1a Preliminaries]]
- [[· C1b Classical Field Theory]]
- [[· C2a The Quantum Scalar Field]]
- [[· C2b Two-Point Functions, Causality and Propagators]]
- [[· C3 Poincaré Symmetry and Particle States]] (★ §C3.6, §C3.7)
- [[· C4 The Quantum Vector Field]] (★ §C4.2, §C4.3, §C4.4, §C4.5)
- [[· C5a Spinors and the Dirac Equation]]
- [[· C5b The Quantum Spinor Field]]
- [[· C9 Discrete Symmetries and Majorana Fields]] (★ §C9.2)
- [[· CA Mathematical Methods]]
- [[· CB Lie Groups, Lie Algebras and Representations]] (★ §CB.19)

### How the chapters build on each other
Arrows point from a chapter to the chapters that use it; labels count the citations from statements, derivations and *Uses:* lines. Dashed arrows are forward references.

```mermaid
graph TD
  C1a["C1a Preliminaries"]
  C1b["C1b Classical Field Theory"]
  C2a["C2a The Quantum Scalar Field"]
  C2b["C2b Two-Point Functions, Causality and Propagators"]
  C3["C3 Poincaré Symmetry and Particle States"]
  C4["C4 The Quantum Vector Field"]
  C5a["C5a Spinors and the Dirac Equation"]
  C5b["C5b The Quantum Spinor Field"]
  C9["C9 Discrete Symmetries and Majorana Fields"]
  CA["CA Mathematical Methods"]
  CB["CB Lie Groups, Lie Algebras and Representations"]
  C1a -->|27| C1b
  C1a -->|3| C2a
  C1b -->|10| C2a
  C1a -->|20| C2b
  C1b -->|3| C2b
  C2a -->|87| C2b
  C1a -->|53| C3
  C1b -->|20| C3
  C2a -->|34| C3
  C2b -->|14| C3
  C1a -->|39| C4
  C1b -->|108| C4
  C2a -->|93| C4
  C2b -->|61| C4
  C3 -->|67| C4
  C1a -->|62| C5a
  C1b -->|93| C5a
  C2a -->|1| C5a
  C3 -->|31| C5a
  C1b -->|26| C5b
  C2a -->|89| C5b
  C2b -->|117| C5b
  C3 -->|7| C5b
  C4 -->|1| C5b
  C5a -->|165| C5b
  C1a -->|11| C9
  C1b -->|6| C9
  C2a -->|40| C9
  C2b -->|2| C9
  C5a -->|49| C9
  C5b -->|17| C9
  C1a -->|2| CA
  C1b -->|3| CA
  C2a -->|7| CA
  C2b -->|43| CA
  C1a -->|59| CB
  C1b -->|1| CB
  C2a -->|1| CB
  C3 -->|54| CB
  C5a -->|90| CB
  C5b -->|1| CB
  CA -->|2| CB
  C1b -.->|22| C1a
  C2a -.->|4| C1a
  C2b -.->|19| C1a
  C3 -.->|7| C1a
  C5a -.->|10| C1a
  C9 -.->|2| C1a
  CA -.->|45| C1a
  CB -.->|5| C1a
  C2a -.->|22| C1b
  C2b -.->|4| C1b
  C3 -.->|6| C1b
  C4 -.->|3| C1b
  C5a -.->|4| C1b
  C5b -.->|2| C1b
  CA -.->|32| C1b
  C2b -.->|18| C2a
  C3 -.->|3| C2a
  C5b -.->|2| C2a
  CA -.->|197| C2a
  CA -.->|429| C2b
  C4 -.->|5| C3
  C5a -.->|10| C3
  C5b -.->|1| C3
  C9 -.->|4| C3
  CA -.->|11| C3
  CB -.->|67| C3
  C5a -.->|1| C4
  C5b -.->|9| C4
  CA -.->|150| C4
  C5b -.->|35| C5a
  C9 -.->|1| C5a
  CA -.->|7| C5a
  CB -.->|68| C5a
  CA -.->|121| C5b
  CB -.->|1| C5b
  CA -.->|26| C9
```

## Planned
Chapters without notes yet (Yu's numbering).

**Level C — PHY 513 (Larsen, Fall 2026; Peskin & Schroeder; Yu)**
C6 Interactions of quantum fields · C7 Feynman diagrams · C8 Quantum electrodynamics · C9 Discrete symmetries and Majorana fields (started: parity, §C9.1–§C9.4; charge conjugation, time reversal, CPT and Majorana fields pending) · C10 The S-matrix and correlation functions · C11 Path-integral quantization

**Mathematics chapter CB** (started 2026-10-08; sections renumbered §CB.0–§CB.20 for "option 1", physics refers to mathematics): [[· CB Lie Groups, Lie Algebras and Representations]] has its full logical chain (every definition and theorem, in order, with course boxes embedded) and proofs, except those still marked *Proof (to be filled)* (the Lie correspondence in §CB.2, Bargmann's theorem in §CB.18, Mackey and Wigner–Mackey in §CB.19★); the mathematical statements of C3 moved into CB in batch B1 (2026-10-08; C3 regrouped into §C3.1–§C3.5 with "The mathematics used here" blocks), those of C1a, C5a and C9 move in batches B2–B3, and §CB.0 (linear algebra in components) is filled then; §CB.20 Grassmann algebras is completed with C11.
