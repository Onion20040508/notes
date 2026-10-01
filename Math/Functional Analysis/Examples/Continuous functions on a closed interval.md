---
subject: math
type: example
source: "[[Functional Analysis]]"
tags: ["math556", "workhorse"]
---
The space $C[a,b]$ of continuous functions $f : [a,b] \to \mathbb{F}$, the first function space of the course. With the supremum norm $\|f\|_\infty = \max_{[a,b]} |f|$ it is a Banach space; with the $L^p$ norm $\|f\|_p = \bigl(\int_a^b |f|^p\bigr)^{1/p}$, $1 \le p < \infty$, it is a normed space that is not complete, and its completion is $L^p[a,b]$. The two norms are not equivalent, so the one set gives two different normed spaces: the norm decides, not the set. It is the example to keep in mind for what the abstract construction of the completion does in practice, and $C^2[a,b]$ with a $C^1$ norm is a second instance of the same phenomenon. The completion for $p = 2$ is in [[L² function spaces]]. Its uses in MATH 556:

- $C[a,b]$ with the supremum norm is a Banach space ([[§9 Completeness#^thm-9-1|§9]])
- Unlike for $\ell^p$, the candidate limit must be shown to lie in the space ([[§9 Completeness#^rem-9-1|§9]])
- $C[a,b]$ sits inside $L^p[a,b]$ via $f \mapsto [f]$ ([[§9 Completeness#^rem-9-7|§9]])
- The norm decides, not the set: $L^1[a,b]$ is not the completion of $(C[a,b], \|\cdot\|_\infty)$ ([[§9 Completeness#^rem-9-9|§9]])
- $C^2[a,b]$ with a $C^1$ norm ([[§9 Completeness#^ex-9-2|§9]])
- $(C^2[a,b], \|\cdot\|_X)$ is not complete, and its completion is $C^1[a,b]$ ([[§9 Completeness#^prop-9-7|§9]])
- $\|\cdot\|_\infty$ and $\|\cdot\|_{L^1}$ on $C[a,b]$ are not equivalent ([[§10 New Normed Spaces from Old#^rem-10-1|§10]])
- Continuous functions are not dense in $L^\infty$ ([[§14 The Function Spaces Lᵖ(Ω)#^prop-14-5|§14]])
- A continuous $h \ge 0$ with vanishing integral is identically $0$ ([[§14 The Function Spaces Lᵖ(Ω)#^lem-14-6|§14]])
- Hölder's inequality for continuous functions ([[§14 The Function Spaces Lᵖ(Ω)#^lem-14-7|§14]])
- $L^p[a,b]$ as the completion of $(C[a,b], \|\cdot\|_p)$ ([[§14 The Function Spaces Lᵖ(Ω)#^prop-14-8|§14]])
- Ramps converging to a step function: the completion is forced to contain discontinuous functions ([[§14 The Function Spaces Lᵖ(Ω)#^rem-14-4|§14]])
- In $\{f \in C[0,1] : f(0) = 0\}$ the constant $\theta = 1$ in Riesz's lemma cannot be attained ([[§15 Compactness and the Unit Ball#^prop-15-4|§15]])
- A sharp integral inequality on $C^2[a,b]$, from the $L^2$ inner product on $C[a,b]$ ([[§18 Projection and Orthogonal Decomposition#^prop-18-8|§18]])

## $C[a,b]$ with the supremum norm is a Banach space
![[§9 Completeness#^thm-9-1]]

## Unlike for $\ell^p$, the candidate limit must be shown to lie in the space
![[§9 Completeness#^rem-9-1]]

## $C[a,b]$ sits inside $L^p[a,b]$ via $f \mapsto [f]$
![[§9 Completeness#^rem-9-7]]

## The norm decides, not the set: $L^1[a,b]$ is not the completion of $(C[a,b], \|\cdot\|_\infty)$
![[§9 Completeness#^rem-9-9]]

## $C^2[a,b]$ with a $C^1$ norm
![[§9 Completeness#^ex-9-2]]

## $(C^2[a,b], \|\cdot\|_X)$ is not complete, and its completion is $C^1[a,b]$
![[§9 Completeness#^prop-9-7]]

## $\|\cdot\|_\infty$ and $\|\cdot\|_{L^1}$ on $C[a,b]$ are not equivalent
![[§10 New Normed Spaces from Old#^rem-10-1]]

## Continuous functions are not dense in $L^\infty$
![[§14 The Function Spaces Lᵖ(Ω)#^prop-14-5]]

## A continuous $h \ge 0$ with vanishing integral is identically $0$
![[§14 The Function Spaces Lᵖ(Ω)#^lem-14-6]]

## Hölder's inequality for continuous functions
![[§14 The Function Spaces Lᵖ(Ω)#^lem-14-7]]

## $L^p[a,b]$ as the completion of $(C[a,b], \|\cdot\|_p)$
![[§14 The Function Spaces Lᵖ(Ω)#^prop-14-8]]

## Ramps converging to a step function: the completion is forced to contain discontinuous functions
![[§14 The Function Spaces Lᵖ(Ω)#^rem-14-4]]

## In $\{f \in C[0,1] : f(0) = 0\}$ the constant $\theta = 1$ in Riesz's lemma cannot be attained
![[§15 Compactness and the Unit Ball#^prop-15-4]]

## A sharp integral inequality on $C^2[a,b]$, from the $L^2$ inner product on $C[a,b]$
![[§18 Projection and Orthogonal Decomposition#^prop-18-8]]
