---
subject: math
type: theorem
source: "[[Functional Analysis]]"
aliases: ["MATH 556 28.1", "B(x,y) = (x, Ay)", "Lax cf.\ Ch. 31, Thm 1"]
tags: [functional-analysis, hub]
---
![[§32 Sesquilinear Forms and the Lax–Milgram Theorem#^thm-32-1]]

## Treated in
- [[§32 Sesquilinear Forms and the Lax–Milgram Theorem#^thm-32-1|Theorem §32.1: Bounded Sesquilinear Forms are Bounded Operators]], in [[§32 Sesquilinear Forms and the Lax–Milgram Theorem]]

## Its proof uses
- [[§22 Definition and Examples#^def-22-1|Definition §22.1: Inner Product; Scalar Product]]
- [[§23 Cauchy–Schwarz and the Induced Norm#^thm-23-1|Theorem §23.1: Cauchy–Schwarz]]
- [[§30 Boundedness and Continuity#^prop-30-1|Proposition §30.1: The Operator Norm]]
- [[§30 Boundedness and Continuity#^def-30-2|Definition §30.2: Bounded Linear Map; Operator Norm]]
- [[§31 Dual Spaces#^thm-31-2|Theorem §31.2: Riesz Representation Theorem, with Norms]]
- [[§32 Sesquilinear Forms and the Lax–Milgram Theorem#^def-32-1|Definition §32.1: Sesquilinear Form; Bounded Form]]

## Used in (Functional Analysis)
- (not cited later in the course)

## Connections
- **How.** For fixed y, x ↦ B(x, y) is a bounded linear functional, so by Riesz with norms ([[§31 Dual Spaces#^thm-31-2|§31.2]]) it equals (x, Ay) for a unique Ay. Uniqueness makes A linear, and taking x = Ay gives ‖Ay‖ ≤ M‖y‖.
- **Finite dimensions.** On ℝⁿ every bilinear form is (x, Ay) for the matrix A = (B(e_i, e_j)) ([[§32 Sesquilinear Forms and the Lax–Milgram Theorem#^ex-32-1|Ex. §32.1]]); this is LADR's matrix of a bilinear form ([[§35 Bilinear Forms and Quadratic Forms#^ladr-9-4|LADR 9.4]]). In infinite dimensions Wu avoided the infinite matrix and used the Riesz representation instead.
- **Used for.** It is the first step of [[Lax–Milgram Theorem|Lax–Milgram]]: conditions (1)–(3) produce A, and coercivity is then used to show that A is one-to-one and onto ([[§32 Sesquilinear Forms and the Lax–Milgram Theorem#^rem-32-1|Remark §32]]).
