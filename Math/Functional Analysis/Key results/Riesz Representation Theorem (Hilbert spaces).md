---
subject: math
type: theorem
source: "[[Functional Analysis]]"
aliases: ["MATH 556 26.4", "Lax §6.3, Thm 4"]
tags: [functional-analysis, hub]
---
![[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^thm-26-4]]

## Treated in
- [[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^thm-26-4|Theorem §26.4: Riesz Representation Theorem]], in [[§26 Bounded Linear Functionals and the Riesz Representation Theorem]]

## Its proof uses
- [[§22 Definition and Examples#^def-22-1|Definition §22.1: Inner Product; Scalar Product]]
- [[§23 Cauchy–Schwarz and the Induced Norm#^thm-23-1|Theorem §23.1: Cauchy–Schwarz]]
- [[§25 Projection and Orthogonal Decomposition#^def-25-1|Definition §25.1: Orthogonality]]
- [[§25 Projection and Orthogonal Decomposition#^def-25-2|Definition §25.2: Orthogonal Complement]]
- [[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^def-26-1|Definition §26.1: Bounded Linear Functional]]
- [[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^lem-26-3|Lemma §26.3: The Kernel Has Codimension One]]

## Used in (Functional Analysis)
- [[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^prop-26-5|Proposition §26.5: Minimizing a Quadratic Functional over a Closed Convex Set]]
- [[§31 Dual Spaces#^thm-31-2|Theorem §31.2: Riesz Representation Theorem, with Norms]]
- [[§32 Sesquilinear Forms and the Lax–Milgram Theorem#^thm-32-2|Theorem §32.2: Lax–Milgram]]
- [[§35 Bras, Kets, and the Riesz Map#^thm-35-2|Theorem §35.2: The Riesz Map]]

## Connections
- **How.** The idea is the picture from ℝⁿ: a is a normal vector to the hyperplane ker ℓ. Boundedness makes N = ker ℓ closed ([[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^lem-26-2|§26.2]]). The [[Orthogonal Decomposition Theorem]] gives H = N ⊕ N⊥ with N⊥ one-dimensional ([[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^lem-26-3|§26.3]]), and a = conj(ℓ(x₀))·x₀/‖x₀‖² for any nonzero x₀ ∈ N⊥. Lax argues instead that two functionals with the same null space are proportional ([[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^rem-26-5|Remark §26]]).
- **Why the hypotheses.** Boundedness is used only to make the kernel closed, and completeness only through the orthogonal decomposition. The physicists' “every functional is a bra” is false without them ([[§35 Bras, Kets, and the Riesz Map#^rem-35-3|Remark §35]]). Point evaluation on C_c(ℝ) is unbounded in the L² norm and is represented by no ψ ∈ L² ([[§37 Position Eigenstates and Continuous Resolutions#^prop-37-4|§37.4]]), so a position eigenstate |x₀⟩ is not a ket.
- **Finite dimensions.** This is LADR's [[Riesz representation theorem]] (6.42), revisited through orthogonal projection in [[§22 Orthogonal Complements and Minimization Problems#^ladr-6-58|LADR 6.58]]. There every functional is bounded.
- **With norms.** ‖ℓ‖ = ‖a‖, so the dual of a Hilbert space is the space itself ([[§31 Dual Spaces#^thm-31-2|§31.2]], [[§31 Dual Spaces#^cor-31-3|§31.3]]); for other spaces the dual is usually different, e.g. (Lᵖ)′ = Lᵖ′ ([[§31 Dual Spaces#^thm-31-4|§31.4]]). [[Lax–Milgram Theorem|Lax–Milgram]] extends the theorem to forms that are not symmetric.
- **Same idea elsewhere.** The Riesz map a ↦ (·, a) is a conjugate-linear isometric bijection H → H* ([[§35 Bras, Kets, and the Riesz Map#^thm-35-2|§35.2]]). A finite-dimensional space is isomorphic to its dual only after choosing a basis ([[§21 Linear Algebra Toolkit#^prop-21-2|591 §21.2]]); the inner product removes the choice. In 591's terms a real inner product is a non-degenerate pairing ([[Non-Degenerate Pairings]]).
