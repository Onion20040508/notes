---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 12.3", "G/H ≅ X", "Lee Theorem 21.18"]
tags: [differentiable-manifolds, hub]
---
![[§12 The Topology of G∕H and Real Grassmannians#^thm-12-3]]

## Treated in
- [[§12 The Topology of G∕H and Real Grassmannians#^thm-12-3|Theorem §12.3: Homogeneous Spaces Are Homeomorphic to Coset Spaces]], in [[§12 The Topology of G∕H and Real Grassmannians]]

## Its proof uses
- [[§1 Point-Set Topology Review#^prop-1-8|Proposition §1.8: Compactness]]
- [[§3 Subspaces and Products#^thm-3-10|Theorem §3.10: Universal Property of the Product]]
- [[§5 Quotient Maps#^cor-5-2|Corollary §5.2: The Form Used in Practice]]
- [[§11 Homogeneous Spaces#^def-11-3|Definition §11.3: Orbit Map]]
- [[§11 Homogeneous Spaces#^lem-11-5|Lemma §11.5: Homogeneous Spaces Are Coset Spaces]]
- [[§12 The Topology of G∕H and Real Grassmannians#^cor-12-2|Corollary §12.2: π Is a Quotient Map]]

## Its proof uses (other subjects)
- [[Bijection from Compact to Hausdorff is a Homeomorphism]] (Topology)
- [[Continuous Image of a Compact Space is Compact]] (Topology)

## Used in (Differentiable Manifolds)
- [[§12 The Topology of G∕H and Real Grassmannians#^ex-12-1|Example §12.1: The Circle as ℝ/ℤ]]
- [[§12 The Topology of G∕H and Real Grassmannians#^ex-12-2|Example §12.2: A Continuous Bijection That Is Not a Homeomorphism]]
- [[§14 Projective Spaces as Smooth Manifolds#^prop-14-6|Proposition §14.6: The Two Topologies on ℝPⁿ Agree]]

## Connections
- **Used for.** S¹ ≅ ℝ/ℤ ([[§12 The Topology of G∕H and Real Grassmannians#^ex-12-1|Ex. §12.1]]), where G = ℝ is not compact but G/H is, and S² ≅ SO(3)/SO(2) as spaces ([[§11 Homogeneous Spaces#^ex-11-3|Ex. §11.3]]). Read in reverse it puts a topology on a set with a transitive action ([[§12 The Topology of G∕H and Real Grassmannians#^def-12-2|Def. §12.2]]), which is how the Grassmannians get theirs ([[§12 The Topology of G∕H and Real Grassmannians#^cor-12-8|§12.8]]); for lines this agrees with the quotient topology of ℝPⁿ ([[§14 Projective Spaces as Smooth Manifolds#^prop-14-6|§14.6]]).
- **Where the hypotheses fail.** ℝ with the discrete topology acting on ℝ by translation gives a continuous bijection ℝ_disc → ℝ that is not a homeomorphism; there G/H is not compact ([[§12 The Topology of G∕H and Real Grassmannians#^ex-12-2|Ex. §12.2]]). Isotropy groups are closed when points of X are closed ([[§11 Homogeneous Spaces#^thm-11-2|§11.2]]), and can fail to be otherwise: ℝ acting on ℝ/ℚ has isotropy group ℚ ([[§11 Homogeneous Spaces#^ex-11-1|Ex. §11.1]]).
- **Same idea elsewhere.** The underlying bijection is 493's orbit bijection G/Stab(x) → Gx ([[§28 Orbit–Stabilizer#^prop-28-2|493 §28.2]]), behind the [[Orbit–Stabilizer Theorem]]; the heuristic dim G/H = dim G − dim H ([[§20 Tangent Spaces I꞉ The Geometric Picture#^rem-20-9|§20, Remark]]) plays the role of |Gx| = |G|/|Stab(x)|. Part (2) is 590's [[Bijection from Compact to Hausdorff is a Homeomorphism]], applied to the map that the orbit map induces on G/H ([[Universal Property of Quotient Maps]]).
- **Coming later in the course.** For a Lie group acting smoothly and transitively on a manifold, Φ is a diffeomorphism with no compactness hypothesis (Lee Theorem 21.18).
