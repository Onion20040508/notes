---
subject: math
type: theorem
source: "[[Functional Analysis]]"
aliases: ["MATH 556 49.3", "geometric series for operators", "perturbation of an invertible operator", "Lax §17.1"]
tags: [functional-analysis, hub]
---
![[§49 Elementary Spectral Theory#^lem-49-3]]

## Treated in
- [[§49 Elementary Spectral Theory#^lem-49-3|Lemma §49.3: The Neumann Series]], in [[§49 Elementary Spectral Theory]]

## Its proof uses
- [[§30 Boundedness and Continuity#^thm-30-8|Theorem §30.8: ℒ(X, Y) is a Normed Linear Space]]
- [[§46 The Transpose#^prop-46-9|Proposition §46.9: Composition and Transpose]]
- [[§49 Elementary Spectral Theory#^lem-49-2|Lemma §49.2: Inverses, Products and Commuting Factors]]

## Used in (Functional Analysis)
- [[§49 Elementary Spectral Theory#^lem-49-4|Lemma §49.4: Perturbation of an Invertible Operator]]
- [[§49 Elementary Spectral Theory#^prop-49-5|Proposition §49.5: The Resolvent Set is Open and Contains ∣lambda∣ > ∣M∣]]

## Connections
- **What it says.** If $\|A\| < 1$ in $\mathcal{L}(X, X)$, $X$ a Banach space, then $I - A$ is invertible, $(I - A)^{-1} = \sum_n A^n$, and $\|(I - A)^{-1}\| \le 1/(1 - \|A\|)$: the geometric series $\frac{1}{1 - x} = \sum x^n$ for operators.
- **How.** The partial sums are Cauchy because $\|A^n\| \le \|A\|^n$, and $\mathcal{L}(X, X)$ is complete ([[Bounded Linear Maps into a Banach Space Form a Banach Space]]); the products with $I - A$ telescope to $I - A^{m+1}$.
- **The form used most.** Perturbation of an invertible operator, [[§49 Elementary Spectral Theory#^lem-49-4|Lem. §49.4]]: if $K$ is invertible and $\|A\| < 1/\|K^{-1}\|$, then $K - A = K(I - K^{-1}A)$ is invertible, with $\|(K - A)^{-1}\| \le \|K^{-1}\| / (1 - \|K^{-1}\|\,\|A\|)$. So the invertible operators form an open set ([[§49 Elementary Spectral Theory#^rem-49-1|Rem. in §49]]).
- **Used for.** The resolvent set is open and contains $|\lambda| > \|M\|$ ([[§49 Elementary Spectral Theory#^prop-49-5|Prop. §49.5]]); the local bound in the analyticity of the resolvent ([[§49 Elementary Spectral Theory#^prop-49-7|Prop. §49.7]]); the decay of the resolvent at infinity in [[The Spectrum Is Nonempty, Closed and Bounded]]. Method: [[Functional Analysis Problem-Solving Techniques#^rem-t35|T35]].
- **Why the hypotheses.** Completeness of $X$ makes $\mathcal{L}(X, X)$ complete, which is what the series needs.
- **In Lax.** §17.1, (9)–(9′) and Thm 2, for a Banach algebra with unit.
