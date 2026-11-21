---
subject: math
type: theorem
source: "[[Functional Analysis]]"
aliases: ["MATH 556 49.6", "resolvent identity", "Lax §17.2"]
tags: [functional-analysis, hub]
---
![[§49 Elementary Spectral Theory#^lem-49-6]]

## Treated in
- [[§49 Elementary Spectral Theory#^lem-49-6|Lemma §49.6: The First Resolvent Identity]], in [[§49 Elementary Spectral Theory]]

## Its proof uses
- [[§49 Elementary Spectral Theory#^lem-49-2|Lemma §49.2: Inverses, Products and Commuting Factors]]

## Used in (Functional Analysis)
- [[§49 Elementary Spectral Theory#^prop-49-7|Proposition §49.7: The Resolvent is Analytic]]
- [[§49 Elementary Spectral Theory#^thm-49-8|Theorem §49.8: The Spectrum is Nonempty, Closed and Bounded]]

## Connections
- **What it says.** For $\lambda, \mu \in \rho(M)$: $(\lambda I - M)^{-1} - (\mu I - M)^{-1} = (\mu - \lambda)(\lambda I - M)^{-1}(\mu I - M)^{-1}$, and the two resolvents commute.
- **How.** Multiply the difference by $\lambda I - M$ on the left and by $\mu I - M$ on the right; the result is $(\mu - \lambda) I$.
- **Used for.** It turns a difference of resolvents into a product with the small factor $\mu - \lambda$: continuity and the derivative $-(zI - M)^{-2}$ of the resolvent ([[§49 Elementary Spectral Theory#^prop-49-7|Prop. §49.7]]), and the final contradiction in [[The Spectrum Is Nonempty, Closed and Bounded]].
- **The resolvent.** [[§48 The Resolvent and the Spectrum#^def-48-2|Def. §48.2]].
- **In Lax.** §17.2, (24), where it is called the resolvent identity and is used for the functional calculus.
