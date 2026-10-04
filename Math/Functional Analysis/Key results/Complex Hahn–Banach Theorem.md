---
subject: math
type: theorem
source: "[[Functional Analysis]]"
aliases: ["MATH 556 8.1", "Lax §3.3, Thm 8"]
tags: [functional-analysis, hub]
---
![[§8 The Complex Hahn–Banach Theorem#^thm-8-1]]

## Treated in
- [[§8 The Complex Hahn–Banach Theorem#^thm-8-1|Theorem §8.1: Complex Hahn–Banach]], in [[§8 The Complex Hahn–Banach Theorem]]

## Its proof uses
- [[§4 Statement and Motivation#^thm-4-2|Theorem §4.2: Hahn–Banach]]
- [[§8 The Complex Hahn–Banach Theorem#^lem-8-2|Lemma §8.2: Consequences of Complex Homogeneity]]

## Used in (Functional Analysis)
- (not cited later in the course)

## Connections
- **How.** The proof reduces to the real case through real parts. u = Re ℓ is real-linear and determines ℓ by ℓ(y) = u(y) − i u(iy). Extend u by the real [[Hahn–Banach Theorem]], which applies because p is positive homogeneous and subadditive on the underlying real space ([[§8 The Complex Hahn–Banach Theorem#^lem-8-2|§8.2]]), and set L(x) = U(x) − iU(ix). The bound |L(x)| ≤ p(x) comes from rotating x by a unimodular a so that L(ax) is real and non-negative ([[Functional Analysis Problem-Solving Techniques#^rem-t8|Technique 8]]). Splitting into real and imaginary parts would only give the constant √2 ([[§8 The Complex Hahn–Banach Theorem#^rem-8-2|Remark §8]]).
- **Why the hypothesis.** Complex homogeneity p(ax) = |a|p(x) forces p ≥ 0 and p(−x) = p(x) ([[§8 The Complex Hahn–Banach Theorem#^lem-8-2|§8.2]]). It is also what undoes the rotation on the right-hand side, since |a| = 1. Seminorms and norms satisfy it ([[§10 Normed Linear Spaces#^def-10-2|Def. §10.2]]).
- **Same idea elsewhere.** The same rotation finishes the complex Cauchy–Schwarz inequality ([[§21 Cauchy–Schwarz and the Induced Norm#^thm-21-1|§21.1]], Step 4), whose finite-dimensional home is the [[Cauchy–Schwarz inequality]] (LADR 6.14). The same principle, that the real part determines everything, reduces the complex [[Jordan–von Neumann Theorem]] to the real one: Im(x, y) = Re(x, iy), just as Im ℓ(x) = −Re ℓ(ix) here ([[§21 Cauchy–Schwarz and the Induced Norm#^rem-21-3|Remark §21]]).
