---
type: section
subject: "[[Functional Analysis]]"
chapter: 4
section: 21
tags: [functional-analysis, math556]
---
← [[§20 Compactness and the Unit Ball]] · ↑ [[· 4 Infinite-Dimensional Spaces꞉ ℓᵖ, Lᵖ, and Compactness]] · [[§22 Definition and Examples]] →

*Stage: norms — Examples revisited. $\ell^p$ and $L^p$ side by side, and what Chapter 4 adds about $\mathbb{R}^n$ and $C[a,b]$.*

## ℝⁿ

Chapter 4 starts and ends in $\mathbb{R}^n$. Cauchy–Schwarz in $\mathbb{R}^n$ opens the chain Young–Hölder–Minkowski, and Hölder on $\mathbb{R}^n$ or $\mathbb{C}^n$ is the finitely supported case of Hölder for sequences ([[§17 Hölder's Inequality for Sequences#^rem-17-2|remark]]). The closed unit ball of $\mathbb{F}^n$ is compact under any norm, and by [[§20 Compactness and the Unit Ball#^thm-20-5|the unit ball theorem]] this happens only in finite dimension.

![[§16 Means and Young's Inequality#^prop-16-1]]

![[§20 Compactness and the Unit Ball#^ex-20-1]]

*Chain:* ← [[§15 ℝⁿ, C［a,b］ and ℓᵖ|Chapter 3]] · [[§29 Sequence and Function Spaces|Chapter 5]] →

## C[a,b]

Here $C[a,b]$ is the space from which $L^p$ is built. Continuous functions are not dense in $L^\infty$, but for $1 \le p < \infty$ the completion of $C[a,b]$ in the $L^p$ norm is $L^p[a,b]$, which proves the claim of Chapter 3. In Riesz's lemma, the functions in $C[0,1]$ vanishing at $0$ show that the constant $\theta = 1$ cannot be attained.

![[§19 The Function Spaces Lᵖ(Ω)#^prop-19-5]]

![[§19 The Function Spaces Lᵖ(Ω)#^prop-19-8]]

![[§20 Compactness and the Unit Ball#^prop-20-4]]

*Chain:* ← [[§15 ℝⁿ, C［a,b］ and ℓᵖ|Chapter 3]] · [[§29 Sequence and Function Spaces|Chapter 5]] →

## ℓᵖ

[[§17 Hölder's Inequality for Sequences|Hölder]] and [[§18 Minkowski's Inequality and the Spaces ℓᵖ|Minkowski]] for sequences build $\ell^p$. The spaces are nested, with norms that are not equivalent; each is a Banach space; and the unit vectors $e_j$ show that the closed unit ball of $\ell^p$ is not compact.

![[§18 Minkowski's Inequality and the Spaces ℓᵖ#^prop-18-4]]

![[§18 Minkowski's Inequality and the Spaces ℓᵖ#^thm-18-5]]

![[§20 Compactness and the Unit Ball#^ex-20-2]]

*Chain:* ← [[§15 ℝⁿ, C［a,b］ and ℓᵖ|Chapter 3]] · [[§29 Sequence and Function Spaces|Chapter 5]] →

## Lᵖ

[[§19 The Function Spaces Lᵖ(Ω)|The Lᵖ section]] repeats the construction for functions, with the integral as a weighted sum, and the results pair off:
- Hölder: [[§17 Hölder's Inequality for Sequences#^thm-17-1|sequences]], [[§19 The Function Spaces Lᵖ(Ω)#^thm-19-1|functions]]
- Minkowski: [[§18 Minkowski's Inequality and the Spaces ℓᵖ#^thm-18-1|sequences]], [[§19 The Function Spaces Lᵖ(Ω)#^thm-19-2|functions]]
- the space: [[§18 Minkowski's Inequality and the Spaces ℓᵖ#^def-18-1|sequences]], [[§19 The Function Spaces Lᵖ(Ω)#^def-19-1|functions]]
- Banach: [[§18 Minkowski's Inequality and the Spaces ℓᵖ#^thm-18-5|sequences]], [[§19 The Function Spaces Lᵖ(Ω)#^thm-19-3|functions]]

What has no sequence counterpart is density, and with it the first case of the pattern “true for $p < \infty$, false for $p = \infty$” ([[§19 The Function Spaces Lᵖ(Ω)#^rem-19-3|remark]]).

![[§19 The Function Spaces Lᵖ(Ω)#^rem-19-1]]

![[§19 The Function Spaces Lᵖ(Ω)#^thm-19-3]]

![[§19 The Function Spaces Lᵖ(Ω)#^thm-19-4]]

*Chain:* ← [[§15 ℝⁿ, C［a,b］ and ℓᵖ|Chapter 3]] · [[§29 Sequence and Function Spaces|Chapter 5]] →
