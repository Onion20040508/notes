---
subject: math
type: theorem
source: "[[Functional Analysis]]"
aliases: ["MATH 556 49.8", "the spectrum is compact", "spectrum is nonempty", "Lax §17.1, Thm 4"]
tags: [functional-analysis, hub]
---
![[§49 Elementary Spectral Theory#^thm-49-8]]

## Treated in
- [[§49 Elementary Spectral Theory#^thm-49-8|Theorem §49.8: The Spectrum is Nonempty, Closed and Bounded]], in [[§49 Elementary Spectral Theory]]

## Its proof uses
- [[§36 Duality in Normed Spaces#^cor-36-3|Corollary §36.3: Bounded Functionals Separate Points]]
- [[§47 Weak and Strong Analyticity#^prop-47-1|Proposition §47.1: Strongly Analytic Functions are Weakly Analytic]]
- [[§49 Elementary Spectral Theory#^lem-49-2|Lemma §49.2: Inverses, Products and Commuting Factors]]
- [[§49 Elementary Spectral Theory#^prop-49-5|Proposition §49.5: The Resolvent Set is Open and Contains ∣lambda∣ > ∣M∣]]
- [[§49 Elementary Spectral Theory#^lem-49-6|Lemma §49.6: The First Resolvent Identity]]
- [[§49 Elementary Spectral Theory#^prop-49-7|Proposition §49.7: The Resolvent is Analytic]]

## Used in (Functional Analysis)
- (not cited later in the course)

## Connections
- **What it says.** For a bounded operator $M$ on a Banach space $X \neq \{0\}$ over $\mathbb{C}$, $\sigma(M)$ is a nonempty, closed and bounded subset of $\mathbb{C}$, contained in the disk $|\lambda| \le \|M\|$.
- **How.** Closed and bounded come from the [[Neumann Series]] ([[§49 Elementary Spectral Theory#^prop-49-5|Prop. §49.5]]). Nonempty: if $\rho(M) = \mathbb{C}$, each $\ell((zI - M)^{-1})$ is a bounded entire function, hence constant by [[Liouville's Theorem]]; functionals separate points, so the resolvent is constant, which contradicts the [[First Resolvent Identity]]. Method: [[Functional Analysis Problem-Solving Techniques#^rem-t36|T36]].
- **Why the hypotheses.** Complex scalars (Liouville): a rotation of $\mathbb{R}^2$ has no real point in its spectrum ([[§48 The Resolvent and the Spectrum#^ex-48-2|Ex. §48.2]]). $X \neq \{0\}$ for the last step. Details: [[§49 Elementary Spectral Theory#^rem-49-3|Rem. in §49]].
- **What it does not say.** A point of the spectrum need not be an eigenvalue: multiplication by $t$ has spectrum $[0,1]$ and no eigenvalues ([[§48 The Resolvent and the Spectrum#^ex-48-3|Ex. §48.3]], [[§48 The Resolvent and the Spectrum#^ex-48-4|Ex. §48.4]]). The spectrum need not be convex.
- **In finite dimensions.** Every operator on a complex vector space has an eigenvalue, [[§15 The Minimal Polynomial#^ladr-5-19|LADR 5.19]].
- **In Lax.** §17.1, Thm 4(i) (Gelfand), proved by integrating the Laurent series of the resolvent at $\infty$; the nonemptiness is attributed to A. E. Taylor.
