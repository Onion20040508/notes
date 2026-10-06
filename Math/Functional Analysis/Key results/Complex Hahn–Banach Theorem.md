---
subject: math
type: theorem
source: "[[Functional Analysis]]"
aliases: ["MATH 556 9.2", "Lax §3.3, Thm 8"]
tags: [functional-analysis, hub]
---
![[§9 The Complex Hahn–Banach Theorem#^thm-9-2]]

## Treated in
- [[§9 The Complex Hahn–Banach Theorem#^thm-9-2|Theorem §9.2: Complex Hahn–Banach]], in [[§9 The Complex Hahn–Banach Theorem]]

## Its proof uses
- [[§5 Statement and Motivation#^thm-5-2|Theorem §5.2: Hahn–Banach]]
- [[§9 The Complex Hahn–Banach Theorem#^lem-9-1|Lemma §9.1: Consequences of Complex Homogeneity]]

## Used in (Functional Analysis)
- (not cited later in the course)

## Connections
- **How.** The proof reduces to the real case through real parts. u = Re ℓ is real-linear and determines ℓ by ℓ(y) = u(y) − i u(iy). Extend u by the real [[Hahn–Banach Theorem]], which applies because p is positive homogeneous and subadditive on the underlying real space ([[§9 The Complex Hahn–Banach Theorem#^lem-9-1|§9.1]]), and set L(x) = U(x) − iU(ix). The bound |L(x)| ≤ p(x) comes from rotating x by a unimodular a so that L(ax) is real and non-negative ([[Functional Analysis Problem-Solving Techniques#^rem-t8|Technique 8]]). Splitting into real and imaginary parts would only give the constant √2 ([[§9 The Complex Hahn–Banach Theorem#^rem-9-2|Remark §9]]).
- **Why the hypothesis.** Complex homogeneity p(ax) = |a|p(x) forces p ≥ 0 and p(−x) = p(x) ([[§9 The Complex Hahn–Banach Theorem#^lem-9-1|§9.1]]). It is also what undoes the rotation on the right-hand side, since |a| = 1. Seminorms and norms satisfy it ([[§11 Normed Linear Spaces#^def-11-2|Def. §11.2]]).
- **Same idea elsewhere.** The same rotation finishes the complex Cauchy–Schwarz inequality ([[§23 Cauchy–Schwarz and the Induced Norm#^thm-23-1|§23.1]], Step 4), whose finite-dimensional home is the [[Cauchy–Schwarz inequality]] (LADR 6.14). The same principle, that the real part determines everything, reduces the complex [[Jordan–von Neumann Theorem]] to the real one: Im(x, y) = Re(x, iy), just as Im ℓ(x) = −Re ℓ(ix) here ([[§24 The Parallelogram Law and Jordan–von Neumann#^rem-24-1|Remark §24]]).
