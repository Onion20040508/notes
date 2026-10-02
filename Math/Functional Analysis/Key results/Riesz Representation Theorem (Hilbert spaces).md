---
subject: math
type: theorem
source: "[[Functional Analysis]]"
aliases: ["MATH 556 19.2", "Lax §6.3, Thm 4"]
tags: [functional-analysis, hub]
---
![[§19 Bounded Linear Functionals and the Riesz Representation Theorem#^thm-19-2]]

## Treated in
- [[§19 Bounded Linear Functionals and the Riesz Representation Theorem#^thm-19-2|Theorem §19.2: Riesz Representation Theorem]], in [[§19 Bounded Linear Functionals and the Riesz Representation Theorem]]

## Its proof uses
- [[§16 Definition and Examples#^def-16-1|Definition §16.1: Inner Product; Scalar Product]]
- [[§17 Cauchy–Schwarz and the Induced Norm#^thm-17-1|Theorem §17.1: Cauchy–Schwarz]]
- [[§18 Projection and Orthogonal Decomposition#^def-18-1|Definition §18.1: Orthogonality; Orthogonal Complement]]
- [[§19 Bounded Linear Functionals and the Riesz Representation Theorem#^def-19-1|Definition §19.1: Bounded Linear Functional]]
- [[§19 Bounded Linear Functionals and the Riesz Representation Theorem#^lem-19-4|Lemma §19.4: The Kernel Has Codimension One]]

## Used in (Functional Analysis)
- [[§22 Dual Spaces#^thm-22-2|Theorem §22.2: Riesz Representation Theorem, with Norms]]
- [[§24 Bras, Kets, and the Riesz Map#^thm-24-2|Theorem §24.2: The Riesz Map]]

## Connections
- **How.** The idea is the picture from ℝⁿ: a is a normal vector to the hyperplane ker ℓ. Boundedness makes N = ker ℓ closed ([[§19 Bounded Linear Functionals and the Riesz Representation Theorem#^lem-19-3|§19.3]]). The [[Orthogonal Decomposition Theorem]] gives H = N ⊕ N⊥ with N⊥ one-dimensional ([[§19 Bounded Linear Functionals and the Riesz Representation Theorem#^lem-19-4|§19.4]]), and a = conj(ℓ(x₀))·x₀/‖x₀‖² for any nonzero x₀ ∈ N⊥. Lax argues instead that two functionals with the same null space are proportional ([[§19 Bounded Linear Functionals and the Riesz Representation Theorem#^rem-19-5|Remark §19]]).
- **Why the hypotheses.** Boundedness is used only to make the kernel closed, and completeness only through the orthogonal decomposition. The physicists' “every functional is a bra” is false without them ([[§24 Bras, Kets, and the Riesz Map#^rem-24-3|Remark §22]]). Point evaluation on C_c(ℝ) is unbounded in the L² norm and is represented by no ψ ∈ L² ([[§26 Position Eigenstates and Continuous Resolutions#^prop-26-4|§26.4]]), so a position eigenstate |x₀⟩ is not a ket.
- **Finite dimensions.** This is LADR's [[Riesz representation theorem]] (6.42), revisited through orthogonal projection in [[§21 Orthogonal Complements and Minimization Problems#^ladr-6-58|LADR 6.58]]. There every functional is bounded.
- **With norms.** ‖ℓ‖ = ‖a‖, so the dual of a Hilbert space is the space itself ([[§22 Dual Spaces#^thm-22-2|§22.2]], [[§22 Dual Spaces#^cor-22-3|§22.3]]); for other spaces the dual is usually different, e.g. (Lᵖ)′ = Lᵖ′ ([[§22 Dual Spaces#^thm-22-4|§22.4]]). [[Lax–Milgram Theorem|Lax–Milgram]] extends the theorem to forms that are not symmetric.
- **Same idea elsewhere.** The Riesz map a ↦ (·, a) is a conjugate-linear isometric bijection H → H* ([[§24 Bras, Kets, and the Riesz Map#^thm-24-2|§24.2]]). A finite-dimensional space is isomorphic to its dual only after choosing a basis ([[§17 Linear Algebra Toolkit#^prop-17-2|591 §17.2]]); the inner product removes the choice. In 591's terms a real inner product is a non-degenerate pairing ([[Non-Degenerate Pairings]]).
