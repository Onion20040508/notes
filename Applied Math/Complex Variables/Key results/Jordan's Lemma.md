---
subject: math
type: theorem
source: "[[Complex Variables]]"
aliases: ["MAT 342 88.2"]
tags: [complex-variables, hub]
---
![[§88★ Jordan's Lemma#^thm-88-2]]

## Treated in
- [[§88★ Jordan's Lemma#^thm-88-2|Theorem §88.2: Jordan's Lemma]], in [[§88★ Jordan's Lemma]]

## Its proof uses
- [[§30 The Exponential Function#^prop-30-1|Proposition §30.1: Modulus and Argument of e^z]]
- [[§44 Contour Integrals#^def-44-1|Definition §44.1: Contour Integral]]
- [[§47 Upper Bounds for Moduli of Contour Integrals#^lem-47-1|Lemma §47.1: Modulus of an Integral of w(t)]]
- [[§88★ Jordan's Lemma#^lem-88-1|Lemma §88.1: Jordan's Inequality]]

## Used in (Complex Variables)
- [[§87 Improper Integrals from Fourier Analysis#^ex-87-2|Example §87.2: The Integral of cos ax/(x² + 1)]]
- [[§89★ An Indented Path#^ex-89-1|Example §89.1: Dirichlet's Integral]]

## Connections
- Jordan's lemma is what makes the Fourier transform of a function decaying only like $1/x$ computable by residues: the Fourier integral of [[§14 Fourier Integral#^def-14-1|341 Def. §14.1]] in its complex form [[§15★ Complex Methods#^thm-15-2|341 Thm. §15.2]], whose outer integral is likewise a symmetric limit $\lim_{L\to\infty}\int_{-L}^{L}$. For example, Example §88.1 below with $3$ replaced by $1$ and $2$ by $x$ gives $\frac2\pi\int_0^\infty\frac{\lambda\sin\lambda x}{1 + \lambda^2}\,d\lambda = e^{-x}$ $(x > 0)$, the representation of [[§14 Fourier Integral#^ex-14-4|341 Ex. §14.4]](b).
