---
subject: math
type: theorem
source: "[[Fourier Series and PDEs]]"
aliases: ["MAT 341 14.1", "Fourier integral representation"]
tags: [fourier-series-and-pdes, hub]
---
![[§14 Fourier Integral#^thm-14-1]]

## Treated in
- [[§14 Fourier Integral#^thm-14-1|Theorem §14.1: Fourier Integral Representation Theorem]], in [[§14 Fourier Integral]]

## Its proof uses
- (no proof in the notes)

## Used in (Fourier Series and PDEs)
- [[§14 Fourier Integral#^cor-14-2|Corollary §14.2: Cosine and Sine Integrals Converge]]
- [[§15★ Complex Methods#^thm-15-2|Theorem §15.2: Complex Form of the Fourier Integral]]
- [[§27 Infinite Rod#^thm-27-2|Theorem §27.2: Fourier Integral Solution of the Infinite Rod Problem]]

## Connections
- The coefficient integrals (9) converge absolutely, since $|f(x)\cos\lambda x| \le |f(x)|$ ([[§36 Improper Integrals#^thm-36-2|451 Thm. §36.2]]), and $|A(\lambda)|, |B(\lambda)| \le \frac1\pi\int|f|$. In complex form this is the boundedness of the Fourier transform from $L^1$ to $L^\infty$, [[§26 Boundedness and Continuity#^ex-26-2|556 Ex. §26.2]], where dominated convergence ([[§15 The General Lebesgue Integral#^thm-15-8|551 Thm. §15.8]]) also shows that $A$ and $B$ are continuous.
- The two analytic facts a proof needs: $A(\lambda), B(\lambda) \to 0$ as $\lambda \to \infty$ (the Riemann–Lebesgue lemma for absolutely integrable $f$, via the density of step functions, [[§16 The L¹ Space and Density Theorems#^thm-16-6|551 Thm. §16.6]]; the series version is [[§12★ Proof of Convergence#^lem-12-3|Lemma §12.3]]), and the exchange of the $x$- and $\lambda$-integrations in Exercise 1.9.8, which is Fubini's theorem on $\mathbb{R} \times [0, L]$, [[§17 Invariance Properties and Fubini's Theorem#^thm-17-6|551 Thm. §17.6]].
- Used in Complex Variables: inverting the Laplace transform by the Bromwich integral is this theorem in disguise, [[§95★ Inverse Laplace Transforms#^thm-95-4|342 Thm. §95.4]], whose proof is complete relative to it.
