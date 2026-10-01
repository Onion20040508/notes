---
subject: math
type: theorem
source: "[[Functional Analysis]]"
aliases: ["MATH 556 18.4", "H = Y ⊕ Y⊥", "Lax §6.2, Thm 3"]
tags: [functional-analysis, hub]
---
![[§18 Projection and Orthogonal Decomposition#^thm-18-4]]

## Treated in
- [[§18 Projection and Orthogonal Decomposition#^thm-18-4|Theorem §18.4: Orthogonal Decomposition]], in [[§18 Projection and Orthogonal Decomposition]]

## Its proof uses
- [[§2 Linear Maps, Convexity, and Linear Functionals#^def-2-3|Definition §2.3: Convex Set]]
- [[§16 Definition and Examples#^def-16-1|Definition §16.1: Inner Product; Scalar Product]]
- [[§18 Projection and Orthogonal Decomposition#^def-18-1|Definition §18.1: Orthogonality; Orthogonal Complement]]
- [[§18 Projection and Orthogonal Decomposition#^def-18-2|Definition §18.2: Internal Direct Sum]]
- [[§18 Projection and Orthogonal Decomposition#^thm-18-2|Theorem §18.2: Closest Point in a Closed Convex Set]]
- [[§18 Projection and Orthogonal Decomposition#^prop-18-3|Proposition §18.3: M^perp is a Closed Subspace]]

## Used in (Functional Analysis)
- [[§18 Projection and Orthogonal Decomposition#^thm-18-6|Theorem §18.6: The Double Complement]]
- [[§18 Projection and Orthogonal Decomposition#^prop-18-7|Proposition §18.7: Even and Odd Functions]]
- [[§19 Bounded Linear Functionals and the Riesz Representation Theorem#^lem-19-4|Lemma §19.4: The Kernel Has Codimension One]]
- [[§20 Orthonormal Sets and Bases#^prop-20-9|Proposition §20.9: Lax's Definition of Orthonormal Base Agrees]]
- [[§25 The Completeness Relation#^prop-25-1|Proposition §25.1: Finite Sums of Outer Products are Projections]]
- [[§26 Position Eigenstates and Continuous Resolutions#^prop-26-5|Proposition §26.5: The Spectral Projections of Position]]
- [[§27 Bound States Need Not Be Complete꞉ Hydrogen#^cor-27-2|Corollary §27.2: Bound States are Not Complete]]

## Connections
- **How.** Apply [[Closest Point in a Closed Convex Set]] to K = Y, then perturb the minimizer. ‖v‖² ≤ ‖v − ty‖² for all t forces (v, y) = 0, with t = se^(iθ) chosen to make the linear term real (step (ii) of [[Functional Analysis Problem-Solving Techniques#^rem-t11|Technique 11]], and [[Functional Analysis Problem-Solving Techniques#^rem-t8|Technique 8]]). Uniqueness comes from Y ∩ Y⊥ = {0}. For (2), test x ∈ (Y⊥)⊥ against its own Y⊥-component.
- **Why closed and complete.** For the non-closed c₀₀ ⊂ ℓ², c₀₀⊥ = {0}, and both (1) and (2) fail ([[§18 Projection and Orthogonal Decomposition#^rem-18-5|Remark §18]]). For an arbitrary set M, (M⊥)⊥ is the closed span ([[§18 Projection and Orthogonal Decomposition#^thm-18-6|§18.6]]). Without completeness only the inclusion of the closed span in (M⊥)⊥ survives ([[§18 Projection and Orthogonal Decomposition#^rem-18-7|Remark §18]]).
- **Used for.** It keeps the promise of [[X ≅ X∕Y ⊕ Y]]: for closed Y in a Hilbert space, Y⊥ is a complement and models the quotient ([[§1 Linear Spaces#^cor-1-13|§1.13]]). The kernel of a nonzero bounded functional has a one-dimensional orthogonal complement ([[§19 Bounded Linear Functionals and the Riesz Representation Theorem#^lem-19-4|§19.4]]), which gives the [[Riesz Representation Theorem (Hilbert spaces)]]. Other uses are the even/odd splitting of L²[−1,1] ([[§18 Projection and Orthogonal Decomposition#^prop-18-7|§18.7]]) and the orthogonal projections of the companion chapter ([[§25 The Completeness Relation#^def-25-2|Def. §25.2]]), including the spectral projections of position ([[§26 Position Eigenstates and Continuous Resolutions#^prop-26-5|§26.5]]) and the incompleteness of hydrogen's bound states ([[§27 Bound States Need Not Be Complete꞉ Hydrogen#^cor-27-2|§27.2]]).
- **Finite dimensions.** In LADR, V = U ⊕ U⊥ ([[§21 Orthogonal Complements and Minimization Problems#^ladr-6-49|LADR 6.49]]) and (U⊥)⊥ = U ([[§21 Orthogonal Complements and Minimization Problems#^ladr-6-52|LADR 6.52]]), with projection P_U ([[§21 Orthogonal Complements and Minimization Problems#^ladr-6-55|LADR 6.55]]); every subspace is closed there and no limit is needed. In a bare normed space [[Riesz's Lemma]] is the substitute, giving a unit vector at distance ≥ ½ instead of an orthogonal one.
