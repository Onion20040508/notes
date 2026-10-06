---
subject: math
type: theorem
source: "[[Functional Analysis]]"
aliases: ["MATH 556 25.4", "H = Y ⊕ Y⊥", "Lax §6.2, Thm 3"]
tags: [functional-analysis, hub]
---
![[§25 Projection and Orthogonal Decomposition#^thm-25-4]]

## Treated in
- [[§25 Projection and Orthogonal Decomposition#^thm-25-4|Theorem §25.4: Orthogonal Decomposition]], in [[§25 Projection and Orthogonal Decomposition]]

## Its proof uses
- [[§3 Linear Maps, Convexity, and Linear Functionals#^def-3-3|Definition §3.3: Convex Set]]
- [[§22 Definition and Examples#^def-22-1|Definition §22.1: Inner Product; Scalar Product]]
- [[§25 Projection and Orthogonal Decomposition#^def-25-1|Definition §25.1: Orthogonality]]
- [[§25 Projection and Orthogonal Decomposition#^def-25-2|Definition §25.2: Orthogonal Complement]]
- [[§25 Projection and Orthogonal Decomposition#^thm-25-2|Theorem §25.2: Closest Point in a Closed Convex Set]]
- [[§25 Projection and Orthogonal Decomposition#^def-25-3|Definition §25.3: Internal Direct Sum]]
- [[§25 Projection and Orthogonal Decomposition#^prop-25-3|Proposition §25.3: M^perp is a Closed Subspace]]

## Used in (Functional Analysis)
- [[§25 Projection and Orthogonal Decomposition#^thm-25-6|Theorem §25.6: The Double Complement]]
- [[§25 Projection and Orthogonal Decomposition#^prop-25-7|Proposition §25.7: Even and Odd Functions]]
- [[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^lem-26-3|Lemma §26.3: The Kernel Has Codimension One]]
- [[§27 Orthonormal Sets and Bases#^prop-27-9|Proposition §27.9: Lax's Definition of Orthonormal Base Agrees]]
- [[§35 The Completeness Relation#^prop-35-1|Proposition §35.1: Finite Sums of Outer Products are Projections]]
- [[§36 Position Eigenstates and Continuous Resolutions#^prop-36-5|Proposition §36.5: The Spectral Projections of Position]]
- [[§37 Bound States Need Not Be Complete꞉ Hydrogen#^cor-37-2|Corollary §37.2: Bound States are Not Complete]]

## Connections
- **How.** Apply [[Closest Point in a Closed Convex Set]] to K = Y, then perturb the minimizer. ‖v‖² ≤ ‖v − ty‖² for all t forces (v, y) = 0, with t = se^(iθ) chosen to make the linear term real (step (ii) of [[Functional Analysis Problem-Solving Techniques#^rem-t11|Technique 11]], and [[Functional Analysis Problem-Solving Techniques#^rem-t8|Technique 8]]). Uniqueness comes from Y ∩ Y⊥ = {0}. For (2), test x ∈ (Y⊥)⊥ against its own Y⊥-component.
- **Why closed and complete.** For the non-closed c₀₀ ⊂ ℓ², c₀₀⊥ = {0}, and both (1) and (2) fail ([[§25 Projection and Orthogonal Decomposition#^rem-25-5|Remark §25]]). For an arbitrary set M, (M⊥)⊥ is the closed span ([[§25 Projection and Orthogonal Decomposition#^thm-25-6|§25.6]]). Without completeness only the inclusion of the closed span in (M⊥)⊥ survives ([[§25 Projection and Orthogonal Decomposition#^rem-25-7|Remark §25]]).
- **Used for.** It keeps the promise of [[X ≅ X∕Y ⊕ Y]]: for closed Y in a Hilbert space, Y⊥ is a complement and models the quotient ([[§2 Quotient Spaces and Complements#^cor-2-8|§2.8]]). The kernel of a nonzero bounded functional has a one-dimensional orthogonal complement ([[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^lem-26-3|§26.3]]), which gives the [[Riesz Representation Theorem (Hilbert spaces)]]. Other uses are the even/odd splitting of L²[−1,1] ([[§25 Projection and Orthogonal Decomposition#^prop-25-7|§25.7]]) and the orthogonal projections of the companion chapter ([[§35 The Completeness Relation#^def-35-4|Def. §35.4]]), including the spectral projections of position ([[§36 Position Eigenstates and Continuous Resolutions#^prop-36-5|§36.5]]) and the incompleteness of hydrogen's bound states ([[§37 Bound States Need Not Be Complete꞉ Hydrogen#^cor-37-2|§37.2]]).
- **Finite dimensions.** In LADR, V = U ⊕ U⊥ ([[§22 Orthogonal Complements and Minimization Problems#^ladr-6-49|LADR 6.49]]) and (U⊥)⊥ = U ([[§22 Orthogonal Complements and Minimization Problems#^ladr-6-52|LADR 6.52]]), with projection P_U ([[§22 Orthogonal Complements and Minimization Problems#^ladr-6-55|LADR 6.55]]); every subspace is closed there and no limit is needed. In a bare normed space [[Riesz's Lemma]] is the substitute, giving a unit vector at distance ≥ ½ instead of an orthogonal one.
- **Also in [[Applied Linear Algebra]]:** [[§52 Orthogonal Projections#^thm-52-1|235 Thm. §52.1]] (the ℝⁿ case, with the projection computed from an orthogonal basis) and [[§52 Orthogonal Projections#^thm-52-3|235 Thm. §52.3]] (the projection is the closest point), with worked examples.
