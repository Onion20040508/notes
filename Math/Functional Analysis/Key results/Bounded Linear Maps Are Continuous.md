---
subject: math
type: theorem
source: "[[Functional Analysis]]"
aliases: ["MATH 556 21.2", "continuous iff bounded", "Lax §15.1, Thm 1"]
tags: [functional-analysis, hub]
---
![[§21 Boundedness and Continuity#^prop-21-2]]

## Treated in
- [[§21 Boundedness and Continuity#^prop-21-2|Proposition §21.2: Continuous if and only if Bounded]], in [[§21 Boundedness and Continuity]]

## Its proof uses
- [[§8 Normed Linear Spaces#^def-8-1|Definition §8.1: Norm; Normed Linear Space]]
- [[§21 Boundedness and Continuity#^def-21-1|Definition §21.1: Continuous Linear Map]]
- [[§21 Boundedness and Continuity#^def-21-2|Definition §21.2: Bounded Linear Map; Operator Norm]]

## Used in (Functional Analysis)
- (not cited later in the course)

## Connections
- **How.** Bounded implies continuous because ‖Tx_j − Tx‖ ≤ M‖x_j − x‖; T is even Lipschitz. For the converse, if ‖Tx_n‖ > n‖x_n‖ for every n, rescale to y_n = x_n/(n‖x_n‖). Then y_n → 0 but ‖Ty_n‖ > 1, so T is not continuous at 0. No completeness is used, although Lax states the theorem for Banach spaces ([[§21 Boundedness and Continuity#^rem-21-5|Remark §21]]).
- **Same idea elsewhere.** For Y = 𝔽 this is [[§19 Bounded Linear Functionals and the Riesz Representation Theorem#^prop-19-1|§19.1]]: a functional is bounded iff continuous iff continuous at 0. The same rescaling shows that one norm is continuous with respect to another iff ‖x‖₁ ≤ C‖x‖₂ ([[§10 New Normed Spaces from Old#^prop-10-2|§10.2]]). In the Riesz theorem, boundedness enters only to make the kernel closed ([[§19 Bounded Linear Functionals and the Riesz Representation Theorem#^lem-19-3|§19.3]]).
- **Finite dimensions.** There every linear functional is bounded ([[§19 Bounded Linear Functionals and the Riesz Representation Theorem#^rem-19-1|Remark §19]]), and LADR's norm of a linear map is a maximum over the unit ball ([[§27 Consequences of Singular Value Decomposition#^ladr-7-86|LADR 7.86]]). As in [[§21 Boundedness and Continuity#^prop-21-1|§21.1]], it is the smallest c with ‖Tv‖ ≤ c‖v‖ ([[§27 Consequences of Singular Value Decomposition#^ladr-7-88|LADR 7.88]]). In infinite dimensions boundedness is a real hypothesis. Point evaluation φ ↦ φ(x₀) on C_c(ℝ) is unbounded in the L² norm and is represented by no ψ ∈ L² ([[§26 Position Eigenstates and Continuous Resolutions#^prop-26-4|§26.4]]), which is why a position eigenstate is not a ket.
- **Used for.** The operator norm makes the bounded maps ℒ(X, Y) a normed space, and a Banach space when Y is complete ([[§21 Boundedness and Continuity#^thm-21-5|§21.5]]; the proof of the second part is still to come).
