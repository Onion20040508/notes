---
subject: math
type: theorem
source: "[[Functional Analysis]]"
aliases: ["MATH 556 23.2", "Lax §6.3, Thm 4"]
tags: [functional-analysis, hub]
---
![[§23 Bounded Linear Functionals and the Riesz Representation Theorem#^thm-23-2]]

## Treated in
- [[§23 Bounded Linear Functionals and the Riesz Representation Theorem#^thm-23-2|Theorem §23.2: Riesz Representation Theorem]], in [[§23 Bounded Linear Functionals and the Riesz Representation Theorem]]

## Its proof uses
- [[§20 Definition and Examples#^def-20-1|Definition §20.1: Inner Product; Scalar Product]]
- [[§21 Cauchy–Schwarz and the Induced Norm#^thm-21-1|Theorem §21.1: Cauchy–Schwarz]]
- [[§22 Projection and Orthogonal Decomposition#^def-22-1|Definition §22.1: Orthogonality; Orthogonal Complement]]
- [[§23 Bounded Linear Functionals and the Riesz Representation Theorem#^def-23-1|Definition §23.1: Bounded Linear Functional]]
- [[§23 Bounded Linear Functionals and the Riesz Representation Theorem#^lem-23-4|Lemma §23.4: The Kernel Has Codimension One]]

## Used in (Functional Analysis)
- [[§23 Bounded Linear Functionals and the Riesz Representation Theorem#^prop-23-5|Proposition §23.5: Minimizing a Quadratic Functional over a Closed Convex Set]]
- [[§27 Dual Spaces#^thm-27-2|Theorem §27.2: Riesz Representation Theorem, with Norms]]
- [[§30 Bras, Kets, and the Riesz Map#^thm-30-2|Theorem §30.2: The Riesz Map]]

## Connections
- **How.** The idea is the picture from ℝⁿ: a is a normal vector to the hyperplane ker ℓ. Boundedness makes N = ker ℓ closed ([[§23 Bounded Linear Functionals and the Riesz Representation Theorem#^lem-23-3|§23.3]]). The [[Orthogonal Decomposition Theorem]] gives H = N ⊕ N⊥ with N⊥ one-dimensional ([[§23 Bounded Linear Functionals and the Riesz Representation Theorem#^lem-23-4|§23.4]]), and a = conj(ℓ(x₀))·x₀/‖x₀‖² for any nonzero x₀ ∈ N⊥. Lax argues instead that two functionals with the same null space are proportional ([[§23 Bounded Linear Functionals and the Riesz Representation Theorem#^rem-23-5|Remark §23]]).
- **Why the hypotheses.** Boundedness is used only to make the kernel closed, and completeness only through the orthogonal decomposition. The physicists' “every functional is a bra” is false without them ([[§30 Bras, Kets, and the Riesz Map#^rem-30-3|Remark §30]]). Point evaluation on C_c(ℝ) is unbounded in the L² norm and is represented by no ψ ∈ L² ([[§32 Position Eigenstates and Continuous Resolutions#^prop-32-4|§32.4]]), so a position eigenstate |x₀⟩ is not a ket.
- **Finite dimensions.** This is LADR's [[Riesz representation theorem]] (6.42), revisited through orthogonal projection in [[§22 Orthogonal Complements and Minimization Problems#^ladr-6-58|LADR 6.58]]. There every functional is bounded.
- **With norms.** ‖ℓ‖ = ‖a‖, so the dual of a Hilbert space is the space itself ([[§27 Dual Spaces#^thm-27-2|§27.2]], [[§27 Dual Spaces#^cor-27-3|§27.3]]); for other spaces the dual is usually different, e.g. (Lᵖ)′ = Lᵖ′ ([[§27 Dual Spaces#^thm-27-4|§27.4]]). [[Lax–Milgram Theorem|Lax–Milgram]] extends the theorem to forms that are not symmetric.
- **Same idea elsewhere.** The Riesz map a ↦ (·, a) is a conjugate-linear isometric bijection H → H* ([[§30 Bras, Kets, and the Riesz Map#^thm-30-2|§30.2]]). A finite-dimensional space is isomorphic to its dual only after choosing a basis ([[§20 Linear Algebra Toolkit#^prop-20-2|591 §20.2]]); the inner product removes the choice. In 591's terms a real inner product is a non-degenerate pairing ([[Non-Degenerate Pairings]]).
