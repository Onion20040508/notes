---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 14.3", "G/H ≅ X", "Lee Theorem 21.18"]
tags: [differentiable-manifolds, hub]
---
![[§15 The Topology of G∕H and Real Grassmannians#^thm-15-3]]

## Treated in
- [[§15 The Topology of G∕H and Real Grassmannians#^thm-15-3|Theorem §15.3: Homogeneous Spaces Are Homeomorphic to Coset Spaces]], in [[§15 The Topology of G∕H and Real Grassmannians]]

## Its proof uses
- [[§1 Point-Set Topology Review#^prop-1-8|Proposition §1.8: Compactness]]
- [[§3 Subspaces and Products#^thm-3-10|Theorem §3.10: Universal Property of the Product]]
- [[§5 Quotient Maps#^cor-5-2|Corollary §5.2: The Form Used in Practice]]
- [[§14 Homogeneous Spaces#^def-14-4|Definition §14.4: Orbit Map]]
- [[§14 Homogeneous Spaces#^lem-14-5|Lemma §14.5: Homogeneous Spaces Are Coset Spaces]]
- [[§15 The Topology of G∕H and Real Grassmannians#^cor-15-2|Corollary §15.2: π Is a Quotient Map]]

## Its proof uses (other subjects)
- [[Bijection from Compact to Hausdorff is a Homeomorphism]] (Topology)
- [[Continuous Image of a Compact Space is Compact]] (Topology)

## Used in (Differentiable Manifolds)
- [[§18 Projective Spaces as Smooth Manifolds#^prop-18-6|Proposition §18.6: The Two Topologies on ℝPⁿ Agree]]

## Connections
- **Used for.** S¹ ≅ ℝ/ℤ ([[§15 The Topology of G∕H and Real Grassmannians#^ex-15-1|Ex. §15.1]]), where G = ℝ is not compact but G/H is, and S² ≅ SO(3)/SO(2) as spaces ([[§14 Homogeneous Spaces#^ex-14-3|Ex. §14.3]]). Read in reverse it puts a topology on a set with a transitive action ([[§15 The Topology of G∕H and Real Grassmannians#^def-15-2|Def. §15.2]]), which is how the Grassmannians get theirs ([[§15 The Topology of G∕H and Real Grassmannians#^cor-15-8|§15.8]]); for lines this agrees with the quotient topology of ℝPⁿ ([[§18 Projective Spaces as Smooth Manifolds#^prop-18-6|§18.6]]).
- **Where the hypotheses fail.** ℝ with the discrete topology acting on ℝ by translation gives a continuous bijection ℝ_disc → ℝ that is not a homeomorphism; there G/H is not compact ([[§15 The Topology of G∕H and Real Grassmannians#^ex-15-2|Ex. §15.2]]). Isotropy groups are closed when points of X are closed ([[§14 Homogeneous Spaces#^thm-14-2|§14.2]]), and can fail to be otherwise: ℝ acting on ℝ/ℚ has isotropy group ℚ ([[§14 Homogeneous Spaces#^ex-14-1|Ex. §14.1]]).
- **Same idea elsewhere.** The underlying bijection is 493's orbit bijection G/Stab(x) → Gx ([[§30 Orbit–Stabilizer#^prop-30-2|493 §30.2]]), behind the [[Orbit–Stabilizer Theorem]]; the heuristic dim G/H = dim G − dim H ([[§25 The Geometric Tangent Space#^rem-25-9|§25, Remark]]) plays the role of |Gx| = |G|/|Stab(x)|. Part (2) is 590's [[Bijection from Compact to Hausdorff is a Homeomorphism]], applied to the map that the orbit map induces on G/H ([[Universal Property of Quotient Maps]]).
- **Coming later in the course.** For a Lie group acting smoothly and transitively on a manifold, Φ is a diffeomorphism with no compactness hypothesis (Lee Theorem 21.18).
