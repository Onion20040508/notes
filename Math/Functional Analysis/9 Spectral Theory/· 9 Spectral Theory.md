---
type: chapter
subject: "[[Functional Analysis]]"
chapter: 9
tags: [chapter, functional-analysis]
---
# 9 Spectral Theory
↑ [[Functional Analysis]]

The eigenvalues of a matrix $A$ are the numbers $\lambda$ for which $\lambda I - A$ fails to be invertible. In infinite dimensions $\lambda I - M$ can fail to be invertible in more than one way, and the set of such $\lambda$, the spectrum of $M$, takes over the role of the eigenvalues. The inverse $(\lambda I - M)^{-1}$, where it exists, is a function of the complex variable $\lambda$ with values in the Banach space $\mathcal{L}(X, X)$, and complex analysis for functions with values in a Banach space is the tool for studying it. [[§47 Weak and Strong Analyticity|§47]] provides the tool: such a function can be tested for analyticity in the norm or through functionals, as convergence was in [[· 8 Weak Convergence|Chapter 8]], and here the two tests agree (Dunford's theorem). [[§48 The Resolvent and the Spectrum|§48]] defines the resolvent set, the resolvent and the spectrum, divides the spectrum into its point, continuous and residual parts, and computes them for multiplication by $t$ on $C[0,1]$ and on $L^2[0,1]$. [[§49 Elementary Spectral Theory|§49]] proves the first general facts about the spectrum of a bounded operator: operators close to an invertible operator are invertible, so the resolvent set is open; the resolvent is an analytic function on it; and the spectrum is a nonempty, closed and bounded subset of $\mathbb{C}$.

**Builds on:** [[· 3 Normed Linear Spaces|3 Normed Linear Spaces]] (1), [[· 5 Inner Product Spaces|5 Inner Product Spaces]] (2), [[· 6 Bounded Linear Maps|6 Bounded Linear Maps]] (7), [[· 7 Inverses, Open Maps, and Baire Category|7 Inverses, Open Maps, and Baire Category]] (5), [[· 8 Weak Convergence|8 Weak Convergence]] (3)
**Used by:** —
**Builds on (other subjects):** [[Measure Theory]] (1)

## Sections
- [[§47 Weak and Strong Analyticity]]
- [[§48 The Resolvent and the Spectrum]]
- [[§49 Elementary Spectral Theory]]

## Central results
- [[Dunford's Theorem]] (§47.3)
- [[Neumann Series]] (§49.3)
- [[First Resolvent Identity]] (§49.6)
- [[The Spectrum Is Nonempty, Closed and Bounded]] (§49.8)

## Load-bearing results
Ranked by how many later results depend on them (through the proofs' citations).
- [[§49 Elementary Spectral Theory#^lem-49-1|Lemma §49.1: One-Sided Inverses]]: 7 later results
- [[§49 Elementary Spectral Theory#^lem-49-2|Lemma §49.2: Inverses, Products and Commuting Factors]]: 6 later results
- [[Neumann Series|Lemma §49.3: The Neumann Series]]: 4 later results
- [[§49 Elementary Spectral Theory#^lem-49-4|Lemma §49.4: Perturbation of an Invertible Operator]]: 3 later results
