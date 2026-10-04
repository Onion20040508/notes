---
subject: math
type: theorem
source: "[[Functional Analysis]]"
aliases: ["MATH 556 22.4", "H = Y ⊕ Y⊥", "Lax §6.2, Thm 3"]
tags: [functional-analysis, hub]
---
![[§22 Projection and Orthogonal Decomposition#^thm-22-4]]

## Treated in
- [[§22 Projection and Orthogonal Decomposition#^thm-22-4|Theorem §22.4: Orthogonal Decomposition]], in [[§22 Projection and Orthogonal Decomposition]]

## Its proof uses
- [[§2 Linear Maps, Convexity, and Linear Functionals#^def-2-3|Definition §2.3: Convex Set]]
- [[§20 Definition and Examples#^def-20-1|Definition §20.1: Inner Product; Scalar Product]]
- [[§22 Projection and Orthogonal Decomposition#^def-22-1|Definition §22.1: Orthogonality; Orthogonal Complement]]
- [[§22 Projection and Orthogonal Decomposition#^thm-22-2|Theorem §22.2: Closest Point in a Closed Convex Set]]
- [[§22 Projection and Orthogonal Decomposition#^def-22-2|Definition §22.2: Internal Direct Sum]]
- [[§22 Projection and Orthogonal Decomposition#^prop-22-3|Proposition §22.3: M^⊥ is a Closed Subspace]]

## Used in (Functional Analysis)
- [[§22 Projection and Orthogonal Decomposition#^thm-22-6|Theorem §22.6: The Double Complement]]
- [[§22 Projection and Orthogonal Decomposition#^prop-22-7|Proposition §22.7: Even and Odd Functions]]
- [[§23 Bounded Linear Functionals and the Riesz Representation Theorem#^lem-23-4|Lemma §23.4: The Kernel Has Codimension One]]
- [[§24 Orthonormal Sets and Bases#^prop-24-9|Proposition §24.9: Lax's Definition of Orthonormal Base Agrees]]
- [[§31 The Completeness Relation#^prop-31-1|Proposition §31.1: Finite Sums of Outer Products are Projections]]
- [[§32 Position Eigenstates and Continuous Resolutions#^prop-32-5|Proposition §32.5: The Spectral Projections of Position]]
- [[§33 Bound States Need Not Be Complete꞉ Hydrogen#^cor-33-2|Corollary §33.2: Bound States are Not Complete]]

## Connections
- **How.** Apply [[Closest Point in a Closed Convex Set]] to K = Y, then perturb the minimizer. ‖v‖² ≤ ‖v − ty‖² for all t forces (v, y) = 0, with t = se^(iθ) chosen to make the linear term real (step (ii) of [[Functional Analysis Problem-Solving Techniques#^rem-t11|Technique 11]], and [[Functional Analysis Problem-Solving Techniques#^rem-t8|Technique 8]]). Uniqueness comes from Y ∩ Y⊥ = {0}. For (2), test x ∈ (Y⊥)⊥ against its own Y⊥-component.
- **Why closed and complete.** For the non-closed c₀₀ ⊂ ℓ², c₀₀⊥ = {0}, and both (1) and (2) fail ([[§22 Projection and Orthogonal Decomposition#^rem-22-5|Remark §22]]). For an arbitrary set M, (M⊥)⊥ is the closed span ([[§22 Projection and Orthogonal Decomposition#^thm-22-6|§22.6]]). Without completeness only the inclusion of the closed span in (M⊥)⊥ survives ([[§22 Projection and Orthogonal Decomposition#^rem-22-7|Remark §22]]).
- **Used for.** It keeps the promise of [[X ≅ X∕Y ⊕ Y]]: for closed Y in a Hilbert space, Y⊥ is a complement and models the quotient ([[§1 Linear Spaces#^cor-1-13|§1.13]]). The kernel of a nonzero bounded functional has a one-dimensional orthogonal complement ([[§23 Bounded Linear Functionals and the Riesz Representation Theorem#^lem-23-4|§23.4]]), which gives the [[Riesz Representation Theorem (Hilbert spaces)]]. Other uses are the even/odd splitting of L²[−1,1] ([[§22 Projection and Orthogonal Decomposition#^prop-22-7|§22.7]]) and the orthogonal projections of the companion chapter ([[§31 The Completeness Relation#^def-31-2|Def. §31.2]]), including the spectral projections of position ([[§32 Position Eigenstates and Continuous Resolutions#^prop-32-5|§32.5]]) and the incompleteness of hydrogen's bound states ([[§33 Bound States Need Not Be Complete꞉ Hydrogen#^cor-33-2|§33.2]]).
- **Finite dimensions.** In LADR, V = U ⊕ U⊥ ([[§21 Orthogonal Complements and Minimization Problems#^ladr-6-49|LADR 6.49]]) and (U⊥)⊥ = U ([[§21 Orthogonal Complements and Minimization Problems#^ladr-6-52|LADR 6.52]]), with projection P_U ([[§21 Orthogonal Complements and Minimization Problems#^ladr-6-55|LADR 6.55]]); every subspace is closed there and no limit is needed. In a bare normed space [[Riesz's Lemma]] is the substitute, giving a unit vector at distance ≥ ½ instead of an orthogonal one.
- **Also in [[Applied Linear Algebra]]:** [[§42 Orthogonal Projections#^thm-42-1|235 Thm. §42.1]] (the ℝⁿ case, with the projection computed from an orthogonal basis) and [[§42 Orthogonal Projections#^thm-42-3|235 Thm. §42.3]] (the projection is the closest point), with worked examples.
