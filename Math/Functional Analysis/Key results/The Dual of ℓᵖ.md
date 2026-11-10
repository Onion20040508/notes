---
subject: math
type: theorem
source: "[[Functional Analysis]]"
aliases: ["MATH 556 36.4", "dual of lp", "(lp)' = lq"]
tags: [functional-analysis, hub]
---
![[§36 Duality in Normed Spaces#^thm-36-4]]

## Treated in
- [[§36 Duality in Normed Spaces#^thm-36-4|Theorem §36.4: The Dual of ℓ^p]], in [[§36 Duality in Normed Spaces]]

## Its proof uses
- [[§17 Hölder's Inequality for Sequences#^thm-17-1|Theorem §17.1: Hölder's Inequality for Sequences]]
- [[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^prop-26-2|Proposition §26.2: Bounded Means Continuous]]
- [[§31 Dual Spaces#^ex-31-1|Example §31.1: (L²)' = L² and (ell²)' = ell²]]

## Used in (Functional Analysis)
- [[§36 Duality in Normed Spaces#^ex-36-2|Example §36.2: (ℓ^∞)' is Larger than ell¹]]
- [[§36 Duality in Normed Spaces#^cor-36-5|Corollary §36.5: The Pairing Without the Bar]]
- [[§36 Duality in Normed Spaces#^cor-36-6|Corollary §36.6: Duality Formula for the ℓ^p Norm]]
- [[§36 Duality in Normed Spaces#^prop-36-8|Proposition §36.8: The Dual of c_0]]
- [[§37 Separable Duals and Reflexive Spaces#^ex-37-4|Example §37.4: ℓ^p is Reflexive for 1 < p < ∞]]
- [[§37 Separable Duals and Reflexive Spaces#^cor-37-7|Corollary §37.7: Separability of X and X' for Reflexive X]]

## Connections
- **How.** Step 1 is Hölder ([[§17 Hölder's Inequality for Sequences#^thm-17-1|§17.1]]): each $a \in \ell^{p'}$ gives a functional of norm $\le \|a\|_{p'}$. For the converse, the candidate is forced: $a_j = \overline{\ell(e_j)}$. That $a \in \ell^{p'}$ comes from testing $\ell$ on the truncated Hölder-extremal vector and dividing out a finite sum ([[Functional Analysis Problem-Solving Techniques#^rem-t6|Technique 6]]); that $\ell = \ell_a$ comes from density of the finite sequences, which is where $p < \infty$ is used ([[Functional Analysis Problem-Solving Techniques#^rem-t19|Technique 19]]). Done in Lecture 13; it was HW6, Problem 3.
- **Fails for $p = \infty$.** $(\ell^\infty)'$ is larger than $\ell^1$: the limit functional on convergent sequences extends by Hahn–Banach and is represented by no $a \in \ell^1$ ([[§36 Duality in Normed Spaces#^ex-36-2|Ex. §36.2]]).
- **Used for.** The duality formula for the $\ell^p$ norm ([[§36 Duality in Normed Spaces#^cor-36-6|§36.6]]); $\ell^p$ is reflexive for $1 < p < \infty$ ([[§37 Separable Duals and Reflexive Spaces#^ex-37-4|Ex. §37.4]]), while $\ell^1$ is not ([[§37 Separable Duals and Reflexive Spaces#^cor-37-7|§37.7]]).
- **Same idea elsewhere.** $p = 2$ is the Riesz theorem for $\ell^2$ ([[§31 Dual Spaces#^ex-31-1|Ex. §31.1]], [[Riesz Representation Theorem (Hilbert spaces)]]). The function-space version $(L^p)' = L^{p'}$ ([[§31 Dual Spaces#^thm-31-4|§31.4]]) has the same first step, by 551's [[Hölder's Inequality]]; its converse needs the [[Radon–Nikodym Theorem]] in place of the coordinates $\ell(e_j)$ ([[§36 Duality in Normed Spaces#^rem-36-5|Remark: The Dual of Lᵖ, Revisited]]).
- **Finite dimensions.** On $\mathbb{F}^n$ every functional is $x \mapsto \sum x_j \overline{a_j}$ and the dual has the same dimension ([[§12 Duality#^ladr-3-111|LADR 3.111]], dual basis [[§12 Duality#^ladr-3-112|LADR 3.112]]). What the theorem adds is the norm: the dual of the $p$-norm is the $p'$-norm.
