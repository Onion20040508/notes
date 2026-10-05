---
type: subject
discipline: physics
courses: ["PHY 513 (UMich, F. Larsen, Fall 2026)"]
textbooks: ["Peskin & Schroeder, An Introduction to Quantum Field Theory", "Yu Zhao-Huan (余钊焕), Lecture Notes on Quantum Field Theory (量子场论讲义)", "Schwartz, Quantum Field Theory and the Standard Model (further reading)"]
conventions: "[[Larsen PHY 513]]"
status: level C — C1, C2a, C2b, C3, C4, C5a, C5b (§C5b.1–§C5b.4, §C5b.7, §C5b.9 taught; §C5b.5, §C5b.6, §C5b.8 drafts), CA written
tags: [subject, quantum-field-theory]
---
# Quantum Field Theory

Relativistic quantum field theory at the graduate level (**C**, PHY 513, Larsen, Fall 2026; textbook Peskin & Schroeder). Chapters follow Yu Zhao-Huan's lecture notes (余钊焕《量子场论讲义》), whose chapter numbers they keep: fields are organized by spin after the Poincaré group, and interactions are treated once for all fields. Each concept has one home: statements are short boxes, derivations are folded under them, explanations are titled remarks, and hidden connections are collected in each note's Connections. Multi-step procedures have their own notes in Procedures/, linked from every place they are carried out. Statements are marked by layer: *principles* (postulated), *theorems* (derived, with a derivation and a *Uses:* line) and *models* (idealized systems). ★ marks material beyond the PHY 513 syllabus; a *draft* banner marks syllabus topics written ahead of the lectures. Relativity is in [[Relativity]], one-particle quantum mechanics in [[Quantum Mechanics]]. Procedures: [[P1 Canonical Quantization]], [[P2 Green's Functions by Contour Integration]]. Reference card: [[Scalar Field Card]]. The course order, lecture by lecture, is in [[PHY 513 Course Log]]; conventions in [[Larsen PHY 513]].

## Level C — graduate
- [[· C1 Preliminaries]]
- [[· C2a The Quantum Scalar Field]]
- [[· C2b Two-Point Functions, Causality and Propagators]]
- [[· C3 Poincaré Symmetry and Particle States]] (★ §C3.5, §C3.6)
- [[· C4 The Quantum Vector Field]] (★ §C4.2, §C4.3, §C4.4)
- [[· C5a Spinors and the Dirac Equation]]
- [[· C5b The Quantum Spinor Field]]
- [[· CA Mathematical Methods]]

### How the chapters build on each other
Arrows point from a chapter to the chapters that use it; labels count the citations from statements, derivations and *Uses:* lines. Dashed arrows are forward references.

```mermaid
graph TD
  C1["C1 Preliminaries"]
  C2a["C2a The Quantum Scalar Field"]
  C2b["C2b Two-Point Functions, Causality and Propagators"]
  C3["C3 Poincaré Symmetry and Particle States"]
  C4["C4 The Quantum Vector Field"]
  C5a["C5a Spinors and the Dirac Equation"]
  C5b["C5b The Quantum Spinor Field"]
  CA["CA Mathematical Methods"]
  C1 -->|4| C2a
  C1 -->|9| C2b
  C2a -->|76| C2b
  C1 -->|103| C3
  C2a -->|34| C3
  C2b -->|14| C3
  C1 -->|104| C4
  C2a -->|88| C4
  C2b -->|51| C4
  C3 -->|66| C4
  C1 -->|114| C5a
  C2a -->|1| C5a
  C3 -->|88| C5a
  C1 -->|1| C5b
  C2a -->|87| C5b
  C2b -->|117| C5b
  C3 -->|3| C5b
  C5a -->|126| C5b
  C1 -->|5| CA
  C2a -->|7| CA
  C2b -->|43| CA
  C2a -.->|23| C1
  C2b -.->|39| C1
  C3 -.->|24| C1
  C4 -.->|3| C1
  C5a -.->|7| C1
  CA -.->|105| C1
  C2b -.->|17| C2a
  C3 -.->|1| C2a
  C5b -.->|1| C2a
  CA -.->|193| C2a
  CA -.->|379| C2b
  C4 -.->|5| C3
  C5a -.->|16| C3
  C5b -.->|1| C3
  CA -.->|11| C3
  C5a -.->|1| C4
  C5b -.->|9| C4
  CA -.->|133| C4
  C5b -.->|25| C5a
  CA -.->|6| C5a
  CA -.->|112| C5b
```

## Planned
Chapters without notes yet (Yu's numbering).

**Level C — PHY 513 (Larsen, Fall 2026; Peskin & Schroeder; Yu)**
C6 Interactions of quantum fields · C7 Feynman diagrams · C8 Quantum electrodynamics · C9 Discrete symmetries and Majorana fields · C10 The S-matrix and correlation functions · C11 Path-integral quantization
