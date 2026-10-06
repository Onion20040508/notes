---
type: subject
discipline: applied math
course: MATH 233 (UMass Amherst)
term: Spring 2023
instructor: Maria Nikolaou
textbook: "Stewart, Clegg & Watson, Calculus: Early Transcendentals, 9th ed."
status: completed
aliases: ["MATH 233", "Stewart", "Calculus III", "Multivariable Calculus"]
tags: [subject, calculus]
---
# Calculus

Single-variable and multivariable calculus, following James Stewart, Daniel Clegg and Saleem Watson, *Calculus: Early Transcendentals*, 9th edition (Cengage, 2021), section by section: §1–§137 are Stewart's Sections 1.1–16.9 in order (each note's alias gives the Stewart number, e.g. "Stewart 2.5"), and §139–§144 are his Appendices A–E and G (the proofs of Appendix F are written out in the sections of the theorems they prove). Chapters 12–16 are MATH 233 (UMass Amherst, Spring 2023, Maria Nikolaou); its practice exams and reviews supply worked examples (*Source: 233 …*).

These are the computational notes: every definition and result Stewart states, every proof he gives, his methods, and a lean selection of worked examples. The rigorous theory lives in the Math subjects — limits, continuity, derivatives, the integral and series in [[Single Variable Analysis]], several variables and vector calculus in [[Multivariable Analysis]], vectors and determinants in [[Linear Algebra]] — and the main items here carry a folded *Connections* callout pointing to their rigorous treatment.

## How the chapters build on each other
Solid arrows: a chapter's proofs and examples rely on the earlier chapter (arrows implied by others are omitted; exact counts are in each chapter note). Dashed arrows labelled "on credit": results used before they are proved. Dashed arrows to the Math subjects: where the rigorous treatment is, labelled with the number of *Connections* links (only arrows with 3 or more are drawn).

```mermaid
graph TD
  C1["1 Functions and Models"]
  C2["2 Limits and Derivatives"]
  C3["3 Differentiation Rules"]
  C4["4 Applications of Differentiation"]
  C5["5 Integrals"]
  C6["6 Applications of Integration"]
  C7["7 Techniques of Integration"]
  C8["8 Further Applications of Integration"]
  C9["9 Differential Equations"]
  C10["10 Parametric Equations and Polar Coordinates"]
  C11["11 Sequences, Series, and Power Series"]
  C12["12 Vectors and the Geometry of Space"]
  C13["13 Vector Functions"]
  C14["14 Partial Derivatives"]
  C15["15 Multiple Integrals"]
  C16["16 Vector Calculus"]
  C17["17 Background from the Appendices"]
  X0["Logic and Proofs (250)"]
  X1["Single Variable Analysis (451)"]
  X2["Multivariable Analysis (452)"]
  X3["Linear Algebra (LADR)"]
  X4["Measure Theory (551)"]
  X5["Topology (590)"]
  X6["Applied Linear Algebra (235)"]
  X9["Fourier Series and PDEs (341)"]
  X8["Ordinary Differential Equations (331)"]
  X10["Complex Variables (342)"]
  C1 --> C2
  C2 --> C3
  C3 --> C4
  C4 --> C5
  C5 --> C6
  C6 --> C7
  C6 --> C12
  C7 --> C8
  C7 --> C9
  C7 --> C11
  C8 --> C10
  C10 --> C13
  C10 --> C17
  C12 --> C13
  C13 --> C14
  C14 --> C15
  C15 --> C16
  C2 -.->|on credit| C1
  C3 -.->|on credit| C2
  C4 -.->|on credit| C2
  C4 -.->|on credit| C3
  C7 -.->|on credit| C5
  C7 -.->|on credit| C6
  C8 -.->|on credit| C3
  C8 -.->|on credit| C7
  C9 -.->|on credit| C3
  C9 -.->|on credit| C4
  C11 -.->|on credit| C4
  C11 -.->|on credit| C5
  C11 -.->|on credit| C10
  C14 -.->|on credit| C12
  C15 -.->|on credit| C7
  C15 -.->|on credit| C8
  C16 -.->|on credit| C7
  C17 -.->|on credit| C1
  C17 -.->|on credit| C2
  C17 -.->|on credit| C3
  C17 -.->|on credit| C7
  C17 -.->|on credit| C10
  C17 -.->|on credit| C11
  C17 -.->|on credit| C12
  C1 -.->|5| X6
  C1 -.->|3| X10
  C1 -.->|3| X3
  C1 -.->|12| X0
  C1 -.->|12| X1
  C2 -.->|47| X1
  C2 -.->|3| X5
  C3 -.->|7| X10
  C3 -.->|5| X2
  C3 -.->|7| X8
  C3 -.->|11| X1
  C4 -.->|3| X4
  C4 -.->|18| X1
  C5 -.->|4| X4
  C5 -.->|15| X1
  C6 -.->|3| X2
  C6 -.->|3| X1
  C7 -.->|3| X10
  C7 -.->|4| X9
  C7 -.->|3| X2
  C7 -.->|6| X8
  C7 -.->|6| X1
  C8 -.->|6| X2
  C8 -.->|11| X1
  C9 -.->|39| X8
  C9 -.->|12| X1
  C10 -.->|6| X2
  C11 -.->|5| X6
  C11 -.->|10| X10
  C11 -.->|3| X9
  C11 -.->|4| X8
  C11 -.->|48| X1
  C12 -.->|20| X6
  C12 -.->|15| X3
  C12 -.->|3| X2
  C13 -.->|3| X10
  C13 -.->|6| X2
  C13 -.->|3| X1
  C14 -.->|4| X6
  C14 -.->|4| X10
  C14 -.->|5| X9
  C14 -.->|3| X3
  C14 -.->|42| X2
  C14 -.->|3| X1
  C15 -.->|3| X6
  C15 -.->|8| X9
  C15 -.->|10| X4
  C15 -.->|26| X2
  C16 -.->|12| X10
  C16 -.->|56| X2
  C16 -.->|4| X8
  C17 -.->|4| X6
  C17 -.->|7| X10
  C17 -.->|4| X3
  C17 -.->|7| X0
  C17 -.->|13| X1
```

## Chapters
- [[· 1 Functions and Models]]
- [[· 2 Limits and Derivatives]]
- [[· 3 Differentiation Rules]]
- [[· 4 Applications of Differentiation]]
- [[· 5 Integrals]]
- [[· 6 Applications of Integration]]
- [[· 7 Techniques of Integration]]
- [[· 8 Further Applications of Integration]]
- [[· 9 Differential Equations]]
- [[· 10 Parametric Equations and Polar Coordinates]]
- [[· 11 Sequences, Series, and Power Series]]
- [[· 12 Vectors and the Geometry of Space]]
- [[· 13 Vector Functions]]
- [[· 14 Partial Derivatives]]
- [[· 15 Multiple Integrals]]
- [[· 16 Vector Calculus]]
- [[· 17 Background from the Appendices]]

## Central results
- [[Limit Laws]] (§8.1)
- [[Product Rule]] (§15.1)
- [[Quotient Rule]] (§15.2)
- [[Chain Rule]] (§17.2)
- [[Derivative of an Inverse Function]] (§19.1)
- [[Fermat's Theorem on Local Extrema]] (§25.2)
- [[Rolle's Theorem]] (§26.1)
- [[L'Hospital's Rule]] (§28.2)
- [[Substitution Rule]] (§38.1)
- [[Integration by Parts]] (§44.1)
- [[Arc Length Formula]] (§52.1)
- [[Test for Divergence]] (§70.5)
- [[Integral Test]] (§71.1)
- [[Direct Comparison Test]] (§72.1)
- [[Alternating Series Test]] (§73.1)
- [[Ratio Test]] (§74.1)
- [[Taylor's Inequality]] (§78.4)
- [[Fundamental Theorem for Line Integrals]] (§109.1)
- [[Test for Conservative Fields]] (§110.5)

## Course record (MATH 233)
| Exam | Coverage | Notes |
|---|---|---|
| Exam 1 (March 29, 2023) | Stewart 12.1–12.6, 13.1–13.4, 14.1–14.6 | §93–§111 |
| Exam 2 (April 25, 2023) | 14.7, 14.8, 15.1–15.8 | §113–§123 |
| Final (May 23, 2023) | cumulative, emphasis on Chapter 16 | §93–§137 |

Prerequisite: MATH 132 (Calculus II); Chapters 1–11 are included as the single-variable foundation.

## Rigorous treatment
Number of *Connections* links from these notes to each Math subject: [[Single Variable Analysis]] (203), [[Multivariable Analysis]] (163), [[Ordinary Differential Equations]] (63), [[Complex Variables]] (52), [[Applied Linear Algebra]] (43), [[Linear Algebra]] (28), [[Fourier Series and PDEs]] (28), [[Measure Theory]] (20), [[Logic and Proofs]] (19), [[Topology]] (7), [[Differentiable Manifolds]] (2).
