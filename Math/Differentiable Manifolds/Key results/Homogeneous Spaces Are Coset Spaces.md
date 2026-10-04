---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 14.3", "G/H ≅ X", "Lee Theorem 21.18"]
tags: [differentiable-manifolds, hub]
---
![[§14 The Topology of G∕H and Real Grassmannians#^thm-14-3]]

## Treated in
- [[§14 The Topology of G∕H and Real Grassmannians#^thm-14-3|Theorem §14.3: Homogeneous Spaces Are Homeomorphic to Coset Spaces]], in [[§14 The Topology of G∕H and Real Grassmannians]]

## Its proof uses
- [[§1 Point-Set Topology Review#^prop-1-8|Proposition §1.8: Compactness]]
- [[§3 Subspaces and Products#^thm-3-10|Theorem §3.10: Universal Property of the Product]]
- [[§5 Quotient Maps#^cor-5-2|Corollary §5.2: The Form Used in Practice]]
- [[§13 Homogeneous Spaces#^def-13-3|Definition §13.3: Orbit Map]]
- [[§13 Homogeneous Spaces#^lem-13-5|Lemma §13.5: Homogeneous Spaces Are Coset Spaces]]
- [[§14 The Topology of G∕H and Real Grassmannians#^cor-14-2|Corollary §14.2: π Is a Quotient Map]]

## Its proof uses (other subjects)
- [[Bijection from Compact to Hausdorff is a Homeomorphism]] (Topology)
- [[Continuous Image of a Compact Space is Compact]] (Topology)

## Used in (Differentiable Manifolds)
- [[§14 The Topology of G∕H and Real Grassmannians#^ex-14-1|Example §14.1: The Circle as ℝ/ℤ]]
- [[§14 The Topology of G∕H and Real Grassmannians#^ex-14-2|Example §14.2: A Continuous Bijection That Is Not a Homeomorphism]]
- [[§17 Projective Spaces as Smooth Manifolds#^prop-17-6|Proposition §17.6: The Two Topologies on ℝPⁿ Agree]]

## Connections
- **Used for.** S¹ ≅ ℝ/ℤ ([[§14 The Topology of G∕H and Real Grassmannians#^ex-14-1|Ex. §14.1]]), where G = ℝ is not compact but G/H is, and S² ≅ SO(3)/SO(2) as spaces ([[§13 Homogeneous Spaces#^ex-13-3|Ex. §13.3]]). Read in reverse it puts a topology on a set with a transitive action ([[§14 The Topology of G∕H and Real Grassmannians#^def-14-2|Def. §14.2]]), which is how the Grassmannians get theirs ([[§14 The Topology of G∕H and Real Grassmannians#^cor-14-8|§14.8]]); for lines this agrees with the quotient topology of ℝPⁿ ([[§17 Projective Spaces as Smooth Manifolds#^prop-17-6|§17.6]]).
- **Where the hypotheses fail.** ℝ with the discrete topology acting on ℝ by translation gives a continuous bijection ℝ_disc → ℝ that is not a homeomorphism; there G/H is not compact ([[§14 The Topology of G∕H and Real Grassmannians#^ex-14-2|Ex. §14.2]]). Isotropy groups are closed when points of X are closed ([[§13 Homogeneous Spaces#^thm-13-2|§13.2]]), and can fail to be otherwise: ℝ acting on ℝ/ℚ has isotropy group ℚ ([[§13 Homogeneous Spaces#^ex-13-1|Ex. §13.1]]).
- **Same idea elsewhere.** The underlying bijection is 493's orbit bijection G/Stab(x) → Gx ([[§28 Orbit–Stabilizer#^prop-28-2|493 §28.2]]), behind the [[Orbit–Stabilizer Theorem]]; the heuristic dim G/H = dim G − dim H ([[§23 Tangent Spaces I꞉ The Geometric Picture#^rem-23-9|§23, Remark]]) plays the role of |Gx| = |G|/|Stab(x)|. Part (2) is 590's [[Bijection from Compact to Hausdorff is a Homeomorphism]], applied to the map that the orbit map induces on G/H ([[Universal Property of Quotient Maps]]).
- **Coming later in the course.** For a Lie group acting smoothly and transitively on a manifold, Φ is a diffeomorphism with no compactness hypothesis (Lee Theorem 21.18).
