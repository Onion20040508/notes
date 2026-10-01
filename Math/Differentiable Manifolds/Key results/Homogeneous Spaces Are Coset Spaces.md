---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 7.8", "G/H ≅ X", "Lee Theorem 21.18"]
tags: [differentiable-manifolds, hub]
---
![[§7 Homogeneous Spaces#^thm-7-8]]

## Treated in
- [[§7 Homogeneous Spaces#^thm-7-8|Theorem §7.8: Homogeneous Spaces Are Homeomorphic to Coset Spaces]], in [[§7 Homogeneous Spaces]]

## Its proof uses
- [[§1 Point-Set Topology Review#^prop-1-8|Proposition §1.8: Compactness]]
- [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^thm-3-10|Theorem §3.10: Universal Property of the Product]]
- [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^cor-3-19|Corollary §3.19: The Form Used in Practice]]
- [[§7 Homogeneous Spaces#^def-7-3|Definition §7.3: Orbit Map]]
- [[§7 Homogeneous Spaces#^lem-7-5|Lemma §7.5: Homogeneous Spaces Are Coset Spaces]]
- [[§7 Homogeneous Spaces#^cor-7-7|Corollary §7.7: pi Is a Quotient Map]]

## Its proof uses (other subjects)
- [[Bijection from Compact to Hausdorff is a Homeomorphism]] (Topology)
- [[Continuous Image of a Compact Space is Compact]] (Topology)

## Used in (Differentiable Manifolds)
- [[§7 Homogeneous Spaces#^ex-7-4|Example §7.4: The Circle as ℝ/ℤ]]
- [[§7 Homogeneous Spaces#^ex-7-5|Example §7.5: A Continuous Bijection That Is Not a Homeomorphism]]
- [[§8 Differentiable Structures#^prop-8-11|Proposition §8.11: The Two Topologies on mathbbRP^n Agree]]

## Connections
- **Used for.** S¹ ≅ ℝ/ℤ ([[§7 Homogeneous Spaces#^ex-7-4|Ex. §7.4]]), where G = ℝ is not compact but G/H is, and S² ≅ SO(3)/SO(2) as spaces ([[§7 Homogeneous Spaces#^ex-7-3|Ex. §7.3]]). Read in reverse it puts a topology on a set with a transitive action ([[§7 Homogeneous Spaces#^def-7-7|Def. §7.7]]), which is how the Grassmannians get theirs ([[§7 Homogeneous Spaces#^cor-7-13|§7.13]]); for lines this agrees with the quotient topology of ℝPⁿ ([[§8 Differentiable Structures#^prop-8-11|§8.11]]).
- **Where the hypotheses fail.** ℝ with the discrete topology acting on ℝ by translation gives a continuous bijection ℝ_disc → ℝ that is not a homeomorphism; there G/H is not compact ([[§7 Homogeneous Spaces#^ex-7-5|Ex. §7.5]]). Isotropy groups are closed only when points of X are closed: ℝ acting on ℝ/ℚ has isotropy group ℚ ([[§7 Homogeneous Spaces#^ex-7-1|Ex. §7.1]]).
- **Same idea elsewhere.** The underlying bijection is 493's orbit bijection G/Stab(x) → Gx ([[§28 Orbit–Stabilizer#^prop-28-2|493 §28.2]]), behind the [[Orbit–Stabilizer Theorem]]; the heuristic dim G/H = dim G − dim H ([[§11 Tangent Spaces I꞉ The Geometric Picture#^rem-11-9|§11, Remark]]) plays the role of |Gx| = |G|/|Stab(x)|. Part (2) is 590's [[Bijection from Compact to Hausdorff is a Homeomorphism]], applied to the map that the orbit map induces on G/H ([[Universal Property of Quotient Maps]]).
- **Coming later in the course.** For a Lie group acting smoothly and transitively on a manifold, Φ is a diffeomorphism with no compactness hypothesis (Lee Theorem 21.18).
