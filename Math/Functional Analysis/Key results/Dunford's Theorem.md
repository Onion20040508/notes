---
subject: math
type: theorem
source: "[[Functional Analysis]]"
aliases: ["MATH 556 47.3", "weak and strong analyticity", "weakly analytic implies strongly analytic", "Lax §11.4, Thm 4"]
tags: [functional-analysis, hub]
---
![[§47 Weak and Strong Analyticity#^thm-47-3]]

## Treated in
- [[§47 Weak and Strong Analyticity#^thm-47-3|Theorem §47.3: Dunford's Theorem]], in [[§47 Weak and Strong Analyticity]]

## Its proof uses
- [[§31 Dual Spaces#^cor-31-1|Corollary §31.1: The Dual is Always a Banach Space]]
- [[§37 Separable Duals and Reflexive Spaces#^prop-37-5|Proposition §37.5: The Canonical Embedding X → X'']]
- [[§42 Uniform Boundedness and Approximation#^thm-42-6|Theorem §42.6: Uniform Boundedness Principle]]
- [[§47 Weak and Strong Analyticity#^def-47-1|Definition §47.1: Strongly Analytic Function]]
- [[§47 Weak and Strong Analyticity#^lem-47-2|Lemma §47.2: A Cauchy Criterion for Limits as h → 0]]

## Used in (Functional Analysis)
- (not cited later in the course)

## Connections
- **What it says.** A function of a complex variable with values in a Banach space $X$ is analytic in the norm of $X$ ([[§47 Weak and Strong Analyticity#^def-47-1|Def. §47.1]]) as soon as $\ell(f(z))$ is an analytic scalar function for every $\ell \in X'$ ([[§47 Weak and Strong Analyticity#^def-47-2|Def. §47.2]]). The converse is immediate ([[§47 Weak and Strong Analyticity#^prop-47-1|Prop. §47.1]]), so the two notions agree.
- **How.** For each functional the [[Cauchy Integral Formula]] on a circle around the point writes the difference of two difference quotients as one contour integral, and the [[ML-Inequality]] bounds it by a constant $M(\ell)$ times the difference of the increments. The [[Uniform Boundedness Principle]], applied on $X'$ to the vectors viewed as functionals ([[Functional Analysis Problem-Solving Techniques#^rem-t29|T29]]), replaces the constants $M(\ell)$ by one constant in the norm. The difference quotients are then Cauchy, and completeness gives the limit ([[§47 Weak and Strong Analyticity#^lem-47-2|Lem. §47.2]]).
- **Why the hypotheses.** Completeness of $X$ is used only for the last step; the estimate holds in any normed space ([[§47 Weak and Strong Analyticity#^rem-47-3|Rem. in §47]]).
- **Contrast.** For sequences, weak convergence is strictly weaker than strong convergence in infinite dimensions ([[§43 Weak and Weak-Star Convergence#^ex-43-1|Ex. §43.1]]); for analyticity there is no such gap.
- **Used for.** The resolvent $\lambda \mapsto (\lambda I - M)^{-1}$ ([[§48 The Resolvent and the Spectrum#^def-48-2|Def. §48.2]]), a function with values in $\mathcal{L}(X, X)$.
- **An example checked both ways.** [[§47 Weak and Strong Analyticity#^ex-47-1|Ex. §47.1]] ($f(z) = (1, z, z^2, \ldots)$ in $\ell^2$).
- **In Lax.** §11.4, Thm 4, with the same proof.
