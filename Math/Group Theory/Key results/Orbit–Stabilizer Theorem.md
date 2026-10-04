---
subject: math
type: theorem
source: "[[Group Theory]]"
aliases: ["MATH 493 28.3", "orbit-stabilizer"]
tags: [group-theory, hub]
---
![[§30 Orbit–Stabilizer#^thm-30-3]]

## Treated in
- [[§30 Orbit–Stabilizer#^thm-30-3|Theorem §30.3: Orbit–Stabilizer]], in [[§30 Orbit–Stabilizer]]

## Its proof uses
- [[§26 Stabilizers and Fixed Points#^prop-26-1|Proposition §26.1: The Stabilizer Is a Subgroup]]
- [[§29 The Index and Lagrange's Theorem#^def-29-1|Definition §29.1: Index]]
- [[§29 The Index and Lagrange's Theorem#^thm-29-2|Theorem §29.2: Lagrange]]
- [[§30 Orbit–Stabilizer#^prop-30-2|Proposition §30.2: The Orbit Bijection]]

## Used in (Group Theory)
- [[§30 Orbit–Stabilizer#^ex-30-1|Example §30.1: A Group of Order 8 Acting on a Four-Petal Figure]]
- [[§30 Orbit–Stabilizer#^thm-30-6|Theorem §30.6: Burnside's Lemma]]
- [[§32 Linear Groups, the Cube, S₃ and A₄#^prop-32-3|Proposition §32.3: Rotational Symmetries of the Cube]]
- [[§34 Conjugation as an Action and the Class Equation#^cor-34-2|Corollary §34.2: Class Sizes Divide the Group Order]]

## Connections
- **Used for.** Class sizes divide |G| ([[§34 Conjugation as an Action and the Class Equation#^cor-34-2|§34.2]]), hence the [[Class Equation]]. Also [[Burnside's Lemma]], the 24 rotations of the cube (6 faces, each with a stabilizer of order 4; [[§32 Linear Groups, the Cube, S₃ and A₄#^prop-32-3|§32.3]]), and n! = (n − 1)! · n from the point stabilizer in Sₙ ([[§30 Orbit–Stabilizer#^cor-30-5|§30.5]]).
- **Structural form.** Each orbit Gx is in natural bijection with G/Stab(x), and every G/H arises this way ([[§30 Orbit–Stabilizer#^rem-30-1|The Structural Picture]], [[§31 G Acting on Coset Spaces#^prop-31-1|§31.1]]). Stabilizers along an orbit are conjugate ([[§26 Stabilizers and Fixed Points#^prop-26-2|§26.2]]).
- **Same idea elsewhere.** O₃(ℝ) acting on ℝ³ has the spheres as orbits, with Stab(e₁) ≅ O₂(ℝ) ([[§32 Linear Groups, the Cube, S₃ and A₄#^prop-32-2|§32.2]]). In 590, the map π₁(B, b₀) → p⁻¹(b₀) of [[Properties of the Lifting Correspondence]] can be read as the orbit map of e₀ under the (right) monodromy action of π₁(B, b₀) on the fiber, an action the 590 notes do not set up; the stabilizer of e₀ is $p_{\ast}\pi_1(E, e_0)$. So the map is onto when E is path-connected (one orbit) and bijective when E is simply connected (trivial stabilizer).
- **Coming later in the course.** The Sylow theorems are proved by counting orbits of actions on subgroups and cosets.
- **Topological version.** For a continuous transitive action the orbit bijection is continuous, and a homeomorphism when G/H is compact and X Hausdorff: [[Homogeneous Spaces Are Coset Spaces]] (591 Thm. §7.8), e.g. S² ≅ SO(3)/SO(2).
