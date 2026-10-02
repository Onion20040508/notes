---
type: subject
discipline: physics
courses: ["PHY 513 (UMich, F. Larsen, Fall 2026)"]
textbooks: ["Peskin & Schroeder, An Introduction to Quantum Field Theory", "Yu Zhao-Huan (余钊焕), Lecture Notes on Quantum Field Theory (量子场论讲义)", "Schwartz, Quantum Field Theory and the Standard Model (further reading)"]
conventions: "[[Larsen PHY 513]]"
status: level C pilot (C2, CA)
tags: [subject, quantum-field-theory]
---
# Quantum Field Theory

Relativistic quantum field theory at the graduate level (**C**, PHY 513, Larsen, Fall 2026; textbook Peskin & Schroeder). Chapters follow Yu Zhao-Huan's lecture notes (余钊焕《量子场论讲义》), whose chapter numbers they keep: fields are organized by spin after the Poincaré group, and interactions are treated once for all fields. Each concept has one home: statements are short boxes, derivations are folded under them, explanations are titled remarks, and hidden connections are collected in each note's Connections. Multi-step procedures have their own notes in Procedures/, linked from every place they are carried out. Statements are marked by layer: *principles* (postulated), *theorems* (derived, with a derivation and a *Uses:* line) and *models* (idealized systems). ★ marks material beyond the PHY 513 syllabus; a *draft* banner marks syllabus topics written ahead of the lectures. Relativity is in [[Relativity]], one-particle quantum mechanics in [[Quantum Mechanics]]. Procedures: [[P1 Canonical Quantization]], [[P2 Green's Functions by Contour Integration]]. Reference card: [[Scalar Field Card]]. The course order, lecture by lecture, is in [[PHY 513 Course Log]]; conventions in [[Larsen PHY 513]].

## Level C — graduate
- [[· C1 Preliminaries]]
- [[· C2 The Quantum Scalar Field]]
- [[· C3 Poincaré Symmetry and Particle States]] (★ §C3.5, §C3.6)
- [[· C5 The Quantum Spinor Field]]
- [[· CA Mathematical Methods]]

### How the chapters build on each other
Arrows point from a chapter to the chapters that use it; labels count the citations from statements, derivations and *Uses:* lines. Dashed arrows are forward references.

```mermaid
graph TD
  C1["C1 Preliminaries"]
  C2["C2 The Quantum Scalar Field"]
  C3["C3 Poincaré Symmetry and Particle States"]
  C5["C5 The Quantum Spinor Field"]
  CA["CA Mathematical Methods"]
  C1 -->|13| C2
  C1 -->|103| C3
  C2 -->|48| C3
  C1 -->|110| C5
  C2 -->|138| C5
  C3 -->|88| C5
  C1 -->|5| CA
  C2 -->|50| CA
  C2 -.->|62| C1
  C3 -.->|24| C1
  CA -.->|105| C1
  C3 -.->|1| C2
  CA -.->|572| C2
  CA -.->|11| C3
  CA -.->|95| C5
```

## Planned
Chapters without notes yet (Yu's numbering).

**Level C — PHY 513 (Larsen, Fall 2026; Peskin & Schroeder; Yu)**
C1 Preliminaries: why QFT, natural units, Lorentz group, tensors, action, Noether · C3 Poincaré symmetry and particle states (★ Wigner) · C4 The quantum vector field (★ Proca) · C5 The quantum spinor field · C6 Interactions of quantum fields · C7 Feynman diagrams · C8 Quantum electrodynamics · C9 Discrete symmetries and Majorana fields · C10 The S-matrix and correlation functions · C11 Path-integral quantization
