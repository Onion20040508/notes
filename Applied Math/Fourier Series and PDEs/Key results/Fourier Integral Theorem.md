---
subject: math
type: theorem
source: "[[Fourier Series and PDEs]]"
aliases: ["MAT 341 18.1", "Fourier integral representation"]
tags: [fourier-series-and-pdes, hub]
---
![[§18 Fourier Integral#^thm-18-1]]

## Treated in
- [[§18 Fourier Integral#^thm-18-1|Theorem §18.1: Fourier Integral Representation Theorem]], in [[§18 Fourier Integral]]

## Its proof uses
- (no proof in the notes)

## Used in (Fourier Series and PDEs)
- [[§18 Fourier Integral#^cor-18-2|Corollary §18.2: Cosine and Sine Integrals Converge]]
- [[§19★ Complex Methods#^thm-19-2|Theorem §19.2: Complex Form of the Fourier Integral]]
- [[§33 Infinite Rod#^thm-33-2|Theorem §33.2: Fourier Integral Solution of the Infinite Rod Problem]]

## Connections
- The coefficient integrals (9) of [[§18 Fourier Integral#^def-18-1|Definition §18.1]] converge absolutely, since $|f(x)\cos\lambda x| \le |f(x)|$ ([[§36 Improper Integrals#^thm-36-2|451 Thm. §36.2]]), and $|A(\lambda)|, |B(\lambda)| \le \frac1\pi\int|f|$. In complex form this is the boundedness of the Fourier transform from $L^1$ to $L^\infty$, [[§26 Boundedness and Continuity#^ex-26-2|556 Ex. §26.2]], where dominated convergence ([[§23 The Dominated Convergence Theorem#^thm-23-3|551 Thm. §23.3]]) also shows that $A$ and $B$ are continuous.
- The two analytic facts a proof needs: $A(\lambda), B(\lambda) \to 0$ as $\lambda \to \infty$ (the Riemann–Lebesgue lemma for absolutely integrable $f$, via the density of step functions, [[§24 The L¹ Space and Density Theorems#^thm-24-6|551 Thm. §24.6]]; the series version is [[§16★ Proof of Convergence#^lem-16-3|Lemma §16.3]]), and the exchange of the $x$- and $\lambda$-integrations in Exercise 1.9.8, which is Fubini's theorem on $\mathbb{R} \times [0, L]$, [[§25 Invariance Properties and Fubini's Theorem#^thm-25-6|551 Thm. §25.6]].
- Used in Complex Variables: inverting the Laplace transform by the Bromwich integral is this theorem in disguise (its complex form, [[§19★ Complex Methods#^thm-19-2|Theorem §19.2]], applied to $e^{-\gamma t}f(t)$ extended by zero to $t < 0$), [[§95★ Inverse Laplace Transforms#^thm-95-4|342 Thm. §95.4]], whose proof is complete relative to it.
