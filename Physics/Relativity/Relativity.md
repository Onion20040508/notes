---
type: subject
discipline: physics
courses: ["PHY 284 (UMass, S. Hertel, Spring 2024)", "PHY 505 (UMich, J. Wells, Fall 2025) — special-relativity part", "PHY 408 (Stony Brook, Spring 2025; audit)", "PHY 360 GR (Smith, Spring 2024; audit)"]
textbooks: ["OpenStax, University Physics Vol. 3", "Tipler & Llewellyn, Modern Physics", "Morin, Special Relativity for the Enthusiastic Beginner", "Morin, Introduction to Classical Mechanics (ch. 11–14)", "Schutz, A First Course in General Relativity", "Griffiths, Introduction to Electrodynamics (ch. 12)", "Hartle, Gravity", "Couzens, C7.5–C7.6 General Relativity 1–2 (Oxford lecture notes)", "d'Inverno & Vickers, Introducing Einstein's Relativity", "'t Hooft, Introduction to General Relativity"]
conventions: "[[University Physics]]"
status: "levels A and B done; level C (general relativity, self-study) in progress"
tags: [subject, relativity]
---
# Relativity

Special relativity from Einstein's postulates, then its covariant (tensor) form, then general relativity, in three levels: **A** introductory (University Physics Vol. 3 ch. 5; Tipler & Llewellyn ch. 1–2; Morin; PHY 284), **B** upper-level: special relativity in covariant form (the user's own PHY 505 notes and lecture-notes series Part III; PHY 505; Morin, Schutz and Griffiths ch. 12 as supplements), **C★** graduate: general relativity, self-study (no GR course taken; spine Couzens' Oxford lecture notes GR1–GR2, textbooks d'Inverno & Vickers — the textbook of UMich PHYSICS 435/535, whose syllabus serves as a scope reference — Hartle, Schutz and 't Hooft; typed PHY 360 homework as examples). Statements are marked by layer: *principles* (assumed), *laws* (empirical, with their range), *theorems* (derived, with a derivation and a *Uses:* line) and *models* (idealisations). Level B uses the signature η = diag(+1, −1, −1, −1) and keeps c explicit; level C uses η = diag(−1, 1, 1, 1) and geometric units G = c = 1, with the dictionary in §C1.2 and the register [[General Relativity Conventions]]. Newtonian mechanics is in [[Classical Mechanics]], electromagnetism in [[Electromagnetism]]; the covariant formulation of electrodynamics proper (Maxwell from a Lagrangian, the field energy–momentum tensor) is Electromagnetism level C, and §B4.2 here applies the tensor machinery to the field tensor.

## Level A — introductory
- [[· A1 Postulates and the Lorentz Transformation]]
- [[· A2 Relativistic Kinematics]]
- [[· A3 Relativistic Momentum and Energy]]

## Level B — upper
- [[· B1 Minkowski Spacetime and the Lorentz Group]]
- [[· B2 Four-Vectors and Tensors]]
- [[· B3 Relativistic Dynamics from an Action]]
- [[· B4 Fields in Special Relativity]]

## Level C★ — general relativity (self-study)
- [[· C1 From Special Relativity to Gravity]]
- [[· C2 Manifolds and Tensor Fields]]
- [[· C3 Metric, Connection and Curvature]]
- [[· C4 Matter in Curved Spacetime]]
- [[· C5 Einstein's Equations]]

### How the chapters build on each other
Arrows point from a chapter to the chapters that use it; labels count the citations from statements, derivations and *Uses:* lines. Dashed arrows are forward references.

```mermaid
graph TD
  A1["A1 Postulates and the Lorentz Transformation"]
  A2["A2 Relativistic Kinematics"]
  A3["A3 Relativistic Momentum and Energy"]
  B1["B1 Minkowski Spacetime and the Lorentz Group"]
  B2["B2 Four-Vectors and Tensors"]
  B3["B3 Relativistic Dynamics from an Action"]
  B4["B4 Fields in Special Relativity"]
  C1["C1 From Special Relativity to Gravity"]
  C2["C2 Manifolds and Tensor Fields"]
  C3["C3 Metric, Connection and Curvature"]
  C4["C4 Matter in Curved Spacetime"]
  C5["C5 Einstein's Equations"]
  A1 -->|21| A2
  A1 -->|2| A3
  A2 -->|13| A3
  A1 -->|10| B1
  A2 -->|10| B1
  A1 -->|2| B2
  A2 -->|3| B2
  A3 -->|12| B2
  B1 -->|29| B2
  A1 -->|1| B3
  A2 -->|2| B3
  A3 -->|5| B3
  B1 -->|16| B3
  B2 -->|20| B3
  A1 -->|1| B4
  A2 -->|4| B4
  A3 -->|1| B4
  B1 -->|5| B4
  B2 -->|18| B4
  B3 -->|2| B4
  A1 -->|7| C1
  A2 -->|12| C1
  A3 -->|5| C1
  B1 -->|15| C1
  B2 -->|20| C1
  B3 -->|11| C1
  B4 -->|13| C1
  B1 -->|9| C2
  B2 -->|12| C2
  C1 -->|2| C2
  B1 -->|12| C3
  B3 -->|4| C3
  C1 -->|54| C3
  C2 -->|176| C3
  A2 -->|4| C4
  B2 -->|4| C4
  B3 -->|10| C4
  B4 -->|4| C4
  C1 -->|38| C4
  C2 -->|44| C4
  C3 -->|198| C4
  B2 -->|2| C5
  B4 -->|1| C5
  C1 -->|50| C5
  C2 -->|40| C5
  C3 -->|207| C5
  C4 -->|111| C5
  A2 -.->|6| A1
  B2 -.->|1| A1
  B1 -.->|2| A2
  B2 -.->|2| A2
  C1 -.->|3| A2
  B2 -.->|1| A3
  B3 -.->|1| A3
  C1 -.->|1| B1
  C2 -.->|2| B1
  C3 -.->|1| B1
  B3 -.->|1| B2
  C1 -.->|2| B2
  C2 -.->|6| B2
  C4 -.->|1| B2
  B4 -.->|3| B3
  C2 -.->|1| B3
  C3 -.->|2| B3
  C2 -.->|1| B4
  C3 -.->|2| B4
  C3 -.->|6| C1
  C4 -.->|3| C1
  C5 -.->|2| C1
  C3 -.->|7| C2
  C5 -.->|2| C2
  C4 -.->|3| C3
  C5 -.->|3| C3
```

## Planned
Chapters without notes yet; sources in brackets. Planned: 14 chapters, 78 sections.

**Level C★ — general relativity (self-study)**
C6 The Schwarzschild solution and the classical tests [GR1 §6.1–6.2; Hartle 9–10; d'Inverno 15–16] · C7 Schwarzschild as a black hole [GR1 §6.3; d'Inverno 17] · C8 Linearised gravity and gravitational waves [Couzens GR2 §2; Schutz 9; d'Inverno 21] · C9 Relativistic stars and collapse [GR2 §3; Schutz 10] · C10 Causal structure and Penrose diagrams [GR2 §4; d'Inverno 18] · C11 Charged black holes [GR2 §5; d'Inverno 19] · C12 Rotating black holes [GR2 §6; d'Inverno 20; Hartle 15] · C13 Black-hole thermodynamics [GR2 §7] · C14 Hawking radiation and quantum fields in curved spacetime [GR2 §8–9] · C15 Cosmology [Hartle 17–19; Schutz 13; d'Inverno 24–26; 't Hooft 14 — planned only, not yet scheduled]
