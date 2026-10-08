---
subject: math
type: example
source: "[[Functional Analysis]]"
tags: ["math556", "workhorse"]
---
The space $C[a,b]$ of continuous functions $f : [a,b] \to \mathbb{F}$, the first function space of the course. With the supremum norm $\|f\|_\infty = \max_{[a,b]} |f|$ it is a Banach space; with the $L^p$ norm $\|f\|_p = \bigl(\int_a^b |f|^p\bigr)^{1/p}$, $1 \le p < \infty$, it is a normed space that is not complete, and its completion is $L^p[a,b]$. The two norms are not equivalent, so the one set gives two different normed spaces: the norm decides, not the set. It is the example to keep in mind for what the abstract construction of the completion does in practice, and $C^2[a,b]$ with a $C^1$ norm is a second instance of the same phenomenon. The completion for $p = 2$ is in [[L² function spaces]]. Its uses in MATH 556:

*Revisit sections:* [[§15 ℝⁿ, C［a,b］ and ℓᵖ|Chapter 3]] · [[§21 ℝⁿ, C［a,b］, ℓᵖ and Lᵖ|Chapter 4]] · [[§29 Sequence and Function Spaces|Chapter 5]] · [[§36 ℝⁿ, Cᵐ and Lᵖ|Chapter 6]]

- $C[a,b]$ with the supremum norm is a Banach space ([[§12 Completeness#^thm-12-1|§12]])
- Unlike for $\ell^p$, the candidate limit must be shown to lie in the space ([[§12 Completeness#^rem-12-1|§12]])
- $C[a,b]$ sits inside $L^p[a,b]$ via $f \mapsto [f]$ ([[§13 The Completion of a Normed Space#^rem-13-4|§13]])
- The norm decides, not the set: $L^1[a,b]$ is not the completion of $(C[a,b], \|\cdot\|_\infty)$ ([[§13 The Completion of a Normed Space#^rem-13-6|§13]])
- $C^2[a,b]$ with a $C^1$ norm ([[§13 The Completion of a Normed Space#^ex-13-1|§13]])
- $(C^2[a,b], \|\cdot\|_X)$ is not complete, and its completion is $C^1[a,b]$ ([[§13 The Completion of a Normed Space#^prop-13-4|§13]])
- $\|\cdot\|_\infty$ and $\|\cdot\|_{L^1}$ on $C[a,b]$ are not equivalent ([[§14 New Normed Spaces from Old#^rem-14-1|§14]])
- Continuous functions are not dense in $L^\infty$ ([[§19 The Function Spaces Lᵖ(Ω)#^prop-19-5|§19]])
- A continuous $h \ge 0$ with vanishing integral is identically $0$ ([[§19 The Function Spaces Lᵖ(Ω)#^lem-19-6|§19]])
- Hölder's inequality for continuous functions ([[§19 The Function Spaces Lᵖ(Ω)#^lem-19-7|§19]])
- $L^p[a,b]$ as the completion of $(C[a,b], \|\cdot\|_p)$ ([[§19 The Function Spaces Lᵖ(Ω)#^prop-19-8|§19]])
- Ramps converging to a step function: the completion is forced to contain discontinuous functions ([[§19 The Function Spaces Lᵖ(Ω)#^rem-19-4|§19]])
- In $\{f \in C[0,1] : f(0) = 0\}$ the constant $\theta = 1$ in Riesz's lemma cannot be attained ([[§20 Compactness and the Unit Ball#^prop-20-4|§20]])
- A sharp integral inequality on $C^2[a,b]$, from the $L^2$ inner product on $C[a,b]$ ([[§25 Projection and Orthogonal Decomposition#^prop-25-8|§25]])
- Differentiation is bounded from $C^m$ to $C^{m-1}$ ([[§30 Boundedness and Continuity#^ex-30-1|§30]])

## $C[a,b]$ with the supremum norm is a Banach space
![[§12 Completeness#^thm-12-1]]

## Unlike for $\ell^p$, the candidate limit must be shown to lie in the space
![[§12 Completeness#^rem-12-1]]

## $C[a,b]$ sits inside $L^p[a,b]$ via $f \mapsto [f]$
![[§13 The Completion of a Normed Space#^rem-13-4]]

## The norm decides, not the set: $L^1[a,b]$ is not the completion of $(C[a,b], \|\cdot\|_\infty)$
![[§13 The Completion of a Normed Space#^rem-13-6]]

## $C^2[a,b]$ with a $C^1$ norm
![[§13 The Completion of a Normed Space#^ex-13-1]]

## $(C^2[a,b], \|\cdot\|_X)$ is not complete, and its completion is $C^1[a,b]$
![[§13 The Completion of a Normed Space#^prop-13-4]]

## $\|\cdot\|_\infty$ and $\|\cdot\|_{L^1}$ on $C[a,b]$ are not equivalent
![[§14 New Normed Spaces from Old#^rem-14-1]]

## Continuous functions are not dense in $L^\infty$
![[§19 The Function Spaces Lᵖ(Ω)#^prop-19-5]]

## A continuous $h \ge 0$ with vanishing integral is identically $0$
![[§19 The Function Spaces Lᵖ(Ω)#^lem-19-6]]

## Hölder's inequality for continuous functions
![[§19 The Function Spaces Lᵖ(Ω)#^lem-19-7]]

## $L^p[a,b]$ as the completion of $(C[a,b], \|\cdot\|_p)$
![[§19 The Function Spaces Lᵖ(Ω)#^prop-19-8]]

## Ramps converging to a step function: the completion is forced to contain discontinuous functions
![[§19 The Function Spaces Lᵖ(Ω)#^rem-19-4]]

## In $\{f \in C[0,1] : f(0) = 0\}$ the constant $\theta = 1$ in Riesz's lemma cannot be attained
![[§20 Compactness and the Unit Ball#^prop-20-4]]

## A sharp integral inequality on $C^2[a,b]$, from the $L^2$ inner product on $C[a,b]$
![[§25 Projection and Orthogonal Decomposition#^prop-25-8]]

## Differentiation is bounded from $C^m$ to $C^{m-1}$
![[§30 Boundedness and Continuity#^ex-30-1]]
