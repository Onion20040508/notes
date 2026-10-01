---
subject: math
type: theorem
source: "[[Group Theory]]"
aliases: ["MATH 493 28.3", "orbit-stabilizer"]
tags: [group-theory, hub]
---
![[§28 Orbit–Stabilizer#^thm-28-3]]

## Treated in
- [[§28 Orbit–Stabilizer#^thm-28-3|Theorem §28.3: Orbit–Stabilizer]], in [[§28 Orbit–Stabilizer]]

## Its proof uses
- [[§24 Stabilizers and Fixed Points#^prop-24-1|Proposition §24.1: The Stabilizer Is a Subgroup]]
- [[§27 The Index and Lagrange's Theorem#^def-27-1|Definition §27.1: Index]]
- [[§27 The Index and Lagrange's Theorem#^thm-27-2|Theorem §27.2: Lagrange]]
- [[§28 Orbit–Stabilizer#^prop-28-2|Proposition §28.2: The Orbit Bijection]]

## Used in (Group Theory)
- [[§28 Orbit–Stabilizer#^ex-28-1|Example §28.1: A Group of Order 8 Acting on a Four-Petal Figure]]
- [[§28 Orbit–Stabilizer#^thm-28-6|Theorem §28.6: Burnside's Lemma]]
- [[§30 Examples꞉ Linear Groups and the Cube#^prop-30-3|Proposition §30.3: Rotational Symmetries of the Cube]]
- [[§32 Conjugation as an Action and the Class Equation#^cor-32-2|Corollary §32.2: Class Sizes Divide the Group Order]]

## Connections
- **Used for.** Class sizes divide |G| ([[§32 Conjugation as an Action and the Class Equation#^cor-32-2|§32.2]]), hence the [[Class Equation]]. Also [[Burnside's Lemma]], the 24 rotations of the cube (6 faces, each with a stabilizer of order 4; [[§30 Examples꞉ Linear Groups and the Cube#^prop-30-3|§30.3]]), and n! = (n − 1)! · n from the point stabilizer in Sₙ ([[§28 Orbit–Stabilizer#^cor-28-5|§28.5]]).
- **Structural form.** Each orbit Gx is in natural bijection with G/Stab(x), and every G/H arises this way ([[§28 Orbit–Stabilizer#^rem-28-1|The Structural Picture]], [[§29 G Acting on Coset Spaces#^prop-29-1|§29.1]]). Stabilizers along an orbit are conjugate ([[§24 Stabilizers and Fixed Points#^prop-24-2|§24.2]]).
- **Same idea elsewhere.** O₃(ℝ) acting on ℝ³ has the spheres as orbits, with Stab(e₁) ≅ O₂(ℝ) ([[§30 Examples꞉ Linear Groups and the Cube#^prop-30-2|§30.2]]). In 590, the map π₁(B, b₀) → p⁻¹(b₀) of [[Properties of the Lifting Correspondence]] can be read as the orbit map of e₀ under the (right) monodromy action of π₁(B, b₀) on the fiber, an action the 590 notes do not set up; the stabilizer of e₀ is $p_*\pi_1(E, e_0)$. So the map is onto when E is path-connected (one orbit) and bijective when E is simply connected (trivial stabilizer).
- **Coming later in the course.** The Sylow theorems are proved by counting orbits of actions on subgroups and cosets.
- **Topological version.** For a continuous transitive action the orbit bijection is continuous, and a homeomorphism when G/H is compact and X Hausdorff: [[Homogeneous Spaces Are Coset Spaces]] (591 Thm. §7.8), e.g. S² ≅ SO(3)/SO(2).
