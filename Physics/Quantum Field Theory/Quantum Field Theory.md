---
type: subject
discipline: physics
courses: ["PHY 513 (UMich, F. Larsen, Fall 2026)"]
textbooks: ["Peskin & Schroeder, An Introduction to Quantum Field Theory", "Yu Zhao-Huan (余钊焕), Lecture Notes on Quantum Field Theory (量子场论讲义)", "Schwartz, Quantum Field Theory and the Standard Model (further reading)"]
conventions: "[[Larsen PHY 513]]"
status: level C — C1a, C1b, C2a, C2b, C3, C4, C5a, C5b (§C5b.1–§C5b.4, §C5b.7, §C5b.9 taught; §C5b.5, §C5b.6, §C5b.8 drafts), C9 (§C9.1, §C9.3–§C9.4 parity, taught; ★ §C9.2 scalar parity), CA written
tags: [subject, quantum-field-theory]
---
# Quantum Field Theory

Relativistic quantum field theory at the graduate level (**C**, PHY 513, Larsen, Fall 2026; textbook Peskin & Schroeder). Chapters follow Yu Zhao-Huan's lecture notes (余钊焕《量子场论讲义》), whose chapter numbers they keep: fields are organized by spin after the Poincaré group, and interactions are treated once for all fields. Each concept has one home: statements are short boxes, derivations are folded under them, explanations are titled remarks, and hidden connections are collected in each note's Connections. Multi-step procedures have their own notes in Procedures/, linked from every place they are carried out. Statements are marked by layer: *principles* (postulated), *theorems* (derived, with a derivation and a *Uses:* line) and *models* (idealized systems). ★ marks material beyond the PHY 513 syllabus; a *draft* banner marks syllabus topics written ahead of the lectures. Relativity is in [[Relativity]], one-particle quantum mechanics in [[Quantum Mechanics]]. Procedures: [[P1 Canonical Quantization]], [[P2 Green's Functions by Contour Integration]]. Reference card: [[Scalar Field Card]]. The course order, lecture by lecture, is in [[PHY 513 Course Log]]; conventions in [[Larsen PHY 513]].

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
  C1a -->|27| C1b
  C1a -->|3| C2a
  C1b -->|10| C2a
  C1a -->|20| C2b
  C1b -->|3| C2b
  C2a -->|87| C2b
  C1a -->|74| C3
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
  C3 -->|99| C5a
  C1b -->|26| C5b
  C2a -->|89| C5b
  C2b -->|117| C5b
  C3 -->|8| C5b
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
  C1b -.->|22| C1a
  C2a -.->|4| C1a
  C2b -.->|19| C1a
  C3 -.->|11| C1a
  C5a -.->|10| C1a
  C9 -.->|2| C1a
  CA -.->|45| C1a
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
  C5a -.->|21| C3
  C5b -.->|2| C3
  C9 -.->|4| C3
  CA -.->|11| C3
  C5a -.->|1| C4
  C5b -.->|9| C4
  CA -.->|150| C4
  C5b -.->|35| C5a
  C9 -.->|1| C5a
  CA -.->|7| C5a
  CA -.->|121| C5b
  CA -.->|26| C9
```

## Planned
Chapters without notes yet (Yu's numbering).

**Level C — PHY 513 (Larsen, Fall 2026; Peskin & Schroeder; Yu)**
C6 Interactions of quantum fields · C7 Feynman diagrams · C8 Quantum electrodynamics · C9 Discrete symmetries and Majorana fields (started: parity, §C9.1–§C9.4; charge conjugation, time reversal, CPT and Majorana fields pending) · C10 The S-matrix and correlation functions · C11 Path-integral quantization
