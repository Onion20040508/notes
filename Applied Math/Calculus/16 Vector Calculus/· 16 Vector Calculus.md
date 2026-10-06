---
type: chapter
subject: "[[Calculus]]"
chapter: 16
tags: [chapter, calculus]
---
# 16 Vector Calculus
↑ [[Calculus]]

*Stewart, Chapter 16 · MATH 233 (UMass, Spring 2023).*

**Builds on:** [[· 3 Differentiation Rules|3 Differentiation Rules]] (1), [[· 5 Integrals|5 Integrals]] (6), [[· 7 Techniques of Integration|7 Techniques of Integration]] (1), [[· 8 Further Applications of Integration|8 Further Applications of Integration]] (1), [[· 12 Vectors and the Geometry of Space|12 Vectors and the Geometry of Space]] (5), [[· 13 Vector Functions|13 Vector Functions]] (6), [[· 14 Partial Derivatives|14 Partial Derivatives]] (12), [[· 15 Multiple Integrals|15 Multiple Integrals]] (11)
**Used by:** [[· 7 Techniques of Integration|7 Techniques of Integration]] (4)
**Developed further in (other subjects):** [[Topology]] (1), [[Multivariable Analysis]] (58), [[Fourier Series and PDEs]] (2), [[Ordinary Differential Equations]] (4), [[Complex Variables]] (12)

## Sections
- [[§125 Vector Fields]] — Stewart 16.1
- [[§126 Line Integrals]] — Stewart 16.2
- [[§127 Line Integrals of Vector Fields]] — Stewart 16.2
- [[§128 The Fundamental Theorem for Line Integrals]] — Stewart 16.3
- [[§129 Conservative Vector Fields and Potential Functions]] — Stewart 16.3
- [[§130 Green's Theorem]] — Stewart 16.4
- [[§131 Extended Versions of Green's Theorem]] — Stewart 16.4
- [[§132 Curl and Divergence]] — Stewart 16.5
- [[§133 Parametric Surfaces and Their Areas]] — Stewart 16.6
- [[§134 Surface Integrals]] — Stewart 16.7
- [[§135 Oriented Surfaces and Flux]] — Stewart 16.7
- [[§136 Stokes' Theorem]] — Stewart 16.8
- [[§137 The Divergence Theorem]] — Stewart 16.9
- [[§138 The Rotation Field]] — Stewart 16.9

## Summary of the fundamental theorems
## Summary: The Fundamental Theorems

*Stewart, Section 16.10.* The main results of Chapter 16 are higher-dimensional versions of the Fundamental Theorem of Calculus. In each, the left side integrates a "derivative" over a region, and the right side involves only the values of the original function on the *boundary* of the region. (Hypotheses omitted; see the linked statements.)

| Theorem | Formula | Region and its boundary |
|---|---|---|
| Fundamental Theorem of Calculus ([[§41 The Fundamental Theorem of Calculus\|§41]]) | $\displaystyle\int_a^b F'(x)\,dx = F(b) - F(a)$ | interval $[a, b]$; endpoints $a$, $b$ |
| Fundamental Theorem for Line Integrals ([[§128 The Fundamental Theorem for Line Integrals#^thm-128-1\|Theorem §128.1]]) | $\displaystyle\int_C \nabla f \cdot d\mathbf{r} = f(\mathbf{r}(b)) - f(\mathbf{r}(a))$ | curve $C$; endpoints $\mathbf{r}(a)$, $\mathbf{r}(b)$ |
| Green's Theorem ([[§130 Green's Theorem#^thm-130-1\|Theorem §130.1]]) | $\displaystyle\iint_D \left( \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right) dA = \int_C P\,dx + Q\,dy$ | plane region $D$; boundary curve $C$, counterclockwise |
| Stokes' Theorem ([[§136 Stokes' Theorem#^thm-136-1\|Theorem §136.1]]) | $\displaystyle\iint_S \operatorname{curl}\mathbf{F} \cdot d\mathbf{S} = \int_C \mathbf{F} \cdot d\mathbf{r}$ | oriented surface $S$ with normal $\mathbf{n}$; boundary curve $C$, positively oriented |
| Divergence Theorem ([[§137 The Divergence Theorem#^thm-137-1\|Theorem §137.1]]) | $\displaystyle\iiint_E \operatorname{div}\mathbf{F}\,dV = \iint_S \mathbf{F} \cdot d\mathbf{S}$ | solid $E$; boundary surface $S$, outward normal |

Related forms: the vector forms of Green's Theorem, $\oint_C \mathbf{F} \cdot \mathbf{T}\,ds = \iint_D (\operatorname{curl}\mathbf{F}) \cdot \mathbf{k}\,dA$ ([[§132 Curl and Divergence#^thm-132-4|Theorem §132.4]], the flat case of Stokes) and $\oint_C \mathbf{F} \cdot \mathbf{n}\,ds = \iint_D \operatorname{div}\mathbf{F}\,dA$ ([[§132 Curl and Divergence#^thm-132-5|Theorem §132.5]], the flat case of the Divergence Theorem). All five are cases of the [[Generalized Stokes' Theorem]] $\int_M d\omega = \int_{\partial M} \omega$ ([[§40 The Generalized Stokes' Theorem#^thm-40-1|452 Thm. §40.1]]).

Companion facts that the theorems rest on or imply:
- $\operatorname{curl}(\nabla f) = \mathbf{0}$ ([[§132 Curl and Divergence#^thm-132-1|Theorem §132.1]]) and $\operatorname{div}(\operatorname{curl}\mathbf{F}) = 0$ ([[§132 Curl and Divergence#^thm-132-3|Theorem §132.3]]).
- Conservative $\Leftrightarrow$ path independent $\Leftrightarrow$ zero around closed paths ([[§128 The Fundamental Theorem for Line Integrals#^thm-128-2|Theorem §128.2]], [[§128 The Fundamental Theorem for Line Integrals#^thm-128-3|Theorem §128.3]]); tests: $P_y = Q_x$ on a simply-connected plane region ([[§131 Extended Versions of Green's Theorem#^thm-131-3|Theorem §110.5]]), $\operatorname{curl}\mathbf{F} = \mathbf{0}$ on $\mathbb{R}^3$ ([[§136 Stokes' Theorem#^thm-136-4|Theorem §136.4]]).
- Curl as circulation per unit area ([[§136 Stokes' Theorem#^thm-136-3|Theorem §136.3]]) and divergence as flux per unit volume ([[§137 The Divergence Theorem#^thm-137-3|Theorem §137.3]]).

## Central results
- [[Fundamental Theorem for Line Integrals]] (§128.1)
- [[Test for Conservative Fields]] (§131.3)

## Load-bearing results
Ranked by how many later results depend on them (through the proofs' citations).
- [[§126 Line Integrals#^thm-126-2|Theorem §126.2: Evaluating Line Integrals with Respect to x and y]]: 26 later results
- [[§126 Line Integrals#^thm-126-1|Theorem §126.1: Evaluating a Line Integral with Respect to Arc Length]]: 24 later results
- [[§126 Line Integrals#^thm-126-4|Theorem §126.4: Reversing the Orientation]]: 23 later results
- [[§126 Line Integrals#^thm-126-5|Theorem §126.5: Evaluating Line Integrals in Space]]: 23 later results
