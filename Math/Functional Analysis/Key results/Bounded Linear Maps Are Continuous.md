---
subject: math
type: theorem
source: "[[Functional Analysis]]"
aliases: ["MATH 556 30.2", "continuous iff bounded", "Lax §15.1, Thm 1"]
tags: [functional-analysis, hub]
---
![[§30 Boundedness and Continuity#^prop-30-2]]

## Treated in
- [[§30 Boundedness and Continuity#^prop-30-2|Proposition §30.2: Continuous if and only if Bounded]], in [[§30 Boundedness and Continuity]]

## Its proof uses
- [[§11 Normed Linear Spaces#^def-11-1|Definition §11.1: Norm; Normed Linear Space]]
- [[§30 Boundedness and Continuity#^def-30-1|Definition §30.1: Continuous Linear Map]]
- [[§30 Boundedness and Continuity#^def-30-2|Definition §30.2: Bounded Linear Map]]

## Used in (Functional Analysis)
- (not cited later in the course)

## Connections
- **How.** Bounded implies continuous because ‖Tx_j − Tx‖ ≤ M‖x_j − x‖; T is even Lipschitz. For the converse, if ‖Tx_n‖ > n‖x_n‖ for every n, rescale to y_n = x_n/(n‖x_n‖). Then y_n → 0 but ‖Ty_n‖ > 1, so T is not continuous at 0. No completeness is used, although Lax states the theorem for Banach spaces ([[§30 Boundedness and Continuity#^rem-30-5|Remark §30]]).
- **Same idea elsewhere.** For Y = 𝔽 this is [[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^prop-26-1|§26.1]]: a functional is bounded iff continuous iff continuous at 0. The same rescaling shows that one norm is continuous with respect to another iff ‖x‖₁ ≤ C‖x‖₂ ([[§14 New Normed Spaces from Old#^prop-14-2|§14.2]]). In the Riesz theorem, boundedness enters only to make the kernel closed ([[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^lem-26-2|§26.2]]).
- **Finite dimensions.** There every linear functional is bounded ([[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^rem-26-1|Remark §26]]), and LADR's norm of a linear map is a maximum over the unit ball ([[§28 Consequences of Singular Value Decomposition#^ladr-7-86|LADR 7.86]]). As in [[§30 Boundedness and Continuity#^prop-30-1|§30.1]], it is the smallest c with ‖Tv‖ ≤ c‖v‖ ([[§28 Consequences of Singular Value Decomposition#^ladr-7-88|LADR 7.88]]). In infinite dimensions boundedness is a real hypothesis. Point evaluation φ ↦ φ(x₀) on C_c(ℝ) is unbounded in the L² norm and is represented by no ψ ∈ L² ([[§36 Position Eigenstates and Continuous Resolutions#^prop-36-4|§36.4]]), which is why a position eigenstate is not a ket.
- **Used for.** The operator norm makes the bounded maps ℒ(X, Y) a normed space, and a Banach space when Y is complete ([[§30 Boundedness and Continuity#^thm-30-5|§30.5]]; see [[Bounded Linear Maps into a Banach Space Form a Banach Space]]).
