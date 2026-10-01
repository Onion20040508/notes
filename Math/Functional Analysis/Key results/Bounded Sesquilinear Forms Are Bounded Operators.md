---
subject: math
type: theorem
source: "[[Functional Analysis]]"
aliases: ["MATH 556 23.1", "B(x,y) = (x, Ay)"]
tags: [functional-analysis, hub]
---
![[§23 Sesquilinear Forms and the Lax–Milgram Theorem#^thm-23-1]]

## Treated in
- [[§23 Sesquilinear Forms and the Lax–Milgram Theorem#^thm-23-1|Theorem §23.1: Bounded Sesquilinear Forms are Bounded Operators]], in [[§23 Sesquilinear Forms and the Lax–Milgram Theorem]]

## Its proof uses
- [[§16 Definition and Examples#^def-16-1|Definition §16.1: Inner Product; Scalar Product]]
- [[§17 Cauchy–Schwarz and the Induced Norm#^thm-17-1|Theorem §17.1: Cauchy–Schwarz]]
- [[§21 Boundedness and Continuity#^prop-21-1|Proposition §21.1: The Operator Norm]]
- [[§21 Boundedness and Continuity#^def-21-2|Definition §21.2: Bounded Linear Map; Operator Norm]]
- [[§22 Dual Spaces#^thm-22-2|Theorem §22.2: Riesz Representation Theorem, with Norms]]
- [[§23 Sesquilinear Forms and the Lax–Milgram Theorem#^def-23-1|Definition §23.1: Sesquilinear Form; Bounded Form]]

## Used in (Functional Analysis)
- (not cited later in the course)

## Connections
- **How.** For fixed y, x ↦ B(x, y) is a bounded linear functional, so by Riesz with norms ([[§22 Dual Spaces#^thm-22-2|§22.2]]) it equals (x, Ay) for a unique Ay. Uniqueness makes A linear, and taking x = Ay gives ‖Ay‖ ≤ M‖y‖.
- **Finite dimensions.** On ℝⁿ every bilinear form is (x, Ay) for the matrix A = (B(e_i, e_j)) ([[§23 Sesquilinear Forms and the Lax–Milgram Theorem#^ex-23-1|Ex. §23.1]]); this is LADR's matrix of a bilinear form ([[§32 Bilinear Forms and Quadratic Forms#^ladr-9-4|LADR 9.4]]). In infinite dimensions Wu avoided the infinite matrix and used the Riesz representation instead.
- **Used for.** It is the first step of [[Lax–Milgram Theorem|Lax–Milgram]]: conditions (1)–(3) produce A, and coercivity is then used to show that A is one-to-one and onto ([[§23 Sesquilinear Forms and the Lax–Milgram Theorem#^rem-23-1|Remark §23]]).
