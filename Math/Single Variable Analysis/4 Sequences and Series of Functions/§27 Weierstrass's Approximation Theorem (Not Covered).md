---
type: section
subject: "[[Single Variable Analysis]]"
section: 27
chapter: 4
tags: [real-analysis, math451]
---
← [[§26 Differentiation and Integration of Power Series]] · ↑ [[· 4 Sequences and Series of Functions]] · [[§27a The Power Sequence xⁿ]] →

This section of the book — every continuous function on $[a,b]$ is a uniform limit of polynomials — was not covered in lecture. The heading is kept for alignment of numbering.

> [!remark] Remark: The Statement, and Where It Is Used
> In the language of [[§24 Uniform Convergence#^def-24-2|uniform convergence (Def. §24.2)]] the theorem says: if $f: [a,b] \to \mathbb{R}$ is continuous, then for every $\varepsilon > 0$ there is a polynomial $p$ with $|f(x) - p(x)| < \varepsilon$ for all $x \in [a,b]$; equivalently, some sequence of polynomials converges to $f$ uniformly on $[a,b]$. It is the converse direction of [[§24 Uniform Convergence#^thm-24-2|Theorem §24.2]] for polynomials: uniform limits of continuous functions are continuous, and every continuous function on $[a,b]$ arises this way. No proof is given in the vault.
> - Used in Functional Analysis: approximating $f'$ uniformly by a polynomial shows that $C^2[a,b]$ is dense in $C^1[a,b]$ for the norm $\max|f| + \max|f'|$, in the proof of [[§13 The Completion of a Normed Space#^prop-13-4|556 Prop. §13.4]].
> - Used in PDEs: with it, polynomials are dense in $C[-1, 1]$, so the normalized Legendre polynomials form an orthonormal basis of $L^2[-1, 1]$; see the Connections of [[§61★ Legendre Series and Zonal Harmonics#^thm-61-1|341 Thm. §61.1]].
> - Used in the honors-thesis notes: since polynomials approximate every continuous function uniformly on $[-L,L]$, a probability measure supported there is determined by its moments, and convergence of moments implies weak convergence, the moment method behind Wigner's semicircle law ([[§R2.7 Weak Convergence, Characteristic Functions and Concentration#^thm-r2-7-9|Thesis Thm. §R2.7.9]], [[§R2.7 Weak Convergence, Characteristic Functions and Concentration#^thm-r2-7-10|Thesis Thm. §R2.7.10]]).
> - Taylor polynomials ([[§31 Taylor's Theorem#^thm-31-2|§31.2]]) give uniform approximation only for functions with controlled derivatives; the theorem needs no differentiability at all.

^rem-27-1
