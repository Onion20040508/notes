---
subject: math
type: theorem
source: "[[Functional Analysis]]"
aliases: ["MATH 556 28.1", "B(x,y) = (x, Ay)", "Lax cf.\ Ch. 31, Thm 1"]
tags: [functional-analysis, hub]
---
![[§28 Sesquilinear Forms and the Lax–Milgram Theorem#^thm-28-1]]

## Treated in
- [[§28 Sesquilinear Forms and the Lax–Milgram Theorem#^thm-28-1|Theorem §28.1: Bounded Sesquilinear Forms are Bounded Operators]], in [[§28 Sesquilinear Forms and the Lax–Milgram Theorem]]

## Its proof uses
- [[§20 Definition and Examples#^def-20-1|Definition §20.1: Inner Product; Scalar Product]]
- [[§21 Cauchy–Schwarz and the Induced Norm#^thm-21-1|Theorem §21.1: Cauchy–Schwarz]]
- [[§26 Boundedness and Continuity#^prop-26-1|Proposition §26.1: The Operator Norm]]
- [[§26 Boundedness and Continuity#^def-26-2|Definition §26.2: Bounded Linear Map; Operator Norm]]
- [[§27 Dual Spaces#^thm-27-2|Theorem §27.2: Riesz Representation Theorem, with Norms]]
- [[§28 Sesquilinear Forms and the Lax–Milgram Theorem#^def-28-1|Definition §28.1: Sesquilinear Form; Bounded Form]]

## Used in (Functional Analysis)
- (not cited later in the course)

## Connections
- **How.** For fixed y, x ↦ B(x, y) is a bounded linear functional, so by Riesz with norms ([[§27 Dual Spaces#^thm-27-2|§27.2]]) it equals (x, Ay) for a unique Ay. Uniqueness makes A linear, and taking x = Ay gives ‖Ay‖ ≤ M‖y‖.
- **Finite dimensions.** On ℝⁿ every bilinear form is (x, Ay) for the matrix A = (B(e_i, e_j)) ([[§28 Sesquilinear Forms and the Lax–Milgram Theorem#^ex-28-1|Ex. §28.1]]); this is LADR's matrix of a bilinear form ([[§35 Bilinear Forms and Quadratic Forms#^ladr-9-4|LADR 9.4]]). In infinite dimensions Wu avoided the infinite matrix and used the Riesz representation instead.
- **Used for.** It is the first step of [[Lax–Milgram Theorem|Lax–Milgram]]: conditions (1)–(3) produce A, and coercivity is then used to show that A is one-to-one and onto ([[§28 Sesquilinear Forms and the Lax–Milgram Theorem#^rem-28-1|Remark §28]]).
