---
type: chapter
subject: "[[Calculus]]"
chapter: 16
tags: [chapter, calculus]
---
# 16 Vector Calculus
↑ [[Calculus]]

*Stewart, Chapter 16 · MATH 233 (UMass, Spring 2023).*

**Builds on:** [[· 5 Integrals|5 Integrals]] (6), [[· 8 Further Applications of Integration|8 Further Applications of Integration]] (1), [[· 12 Vectors and the Geometry of Space|12 Vectors and the Geometry of Space]] (4), [[· 13 Vector Functions|13 Vector Functions]] (4), [[· 14 Partial Derivatives|14 Partial Derivatives]] (11), [[· 15 Multiple Integrals|15 Multiple Integrals]] (11)
**Used by:** [[· 7 Techniques of Integration|7 Techniques of Integration]] (3)
**Developed further in (other subjects):** [[Topology]] (1), [[Multivariable Analysis]] (56), [[Fourier Series and PDEs]] (2), [[Ordinary Differential Equations]] (4), [[Complex Variables]] (11)

## Sections
- [[§107 Vector Fields]] — Stewart 16.1
- [[§108 Line Integrals]] — Stewart 16.2
- [[§109 The Fundamental Theorem for Line Integrals]] — Stewart 16.3
- [[§110 Green's Theorem]] — Stewart 16.4
- [[§111 Curl and Divergence]] — Stewart 16.5
- [[§112 Parametric Surfaces and Their Areas]] — Stewart 16.6
- [[§113 Surface Integrals]] — Stewart 16.7
- [[§114 Stokes' Theorem]] — Stewart 16.8
- [[§115 The Divergence Theorem]] — Stewart 16.9

## Summary of the fundamental theorems

*Stewart, Section 16.10.* The main results of Chapter 16 are higher-dimensional versions of the Fundamental Theorem of Calculus. In each, the left side integrates a "derivative" over a region, and the right side involves only the values of the original function on the *boundary* of the region. (Hypotheses omitted; see the linked statements.)

| Theorem | Formula | Region and its boundary |
|---|---|---|
| Fundamental Theorem of Calculus ([[§36 The Fundamental Theorem of Calculus\|§36]]) | $\displaystyle\int_a^b F'(x)\,dx = F(b) - F(a)$ | interval $[a, b]$; endpoints $a$, $b$ |
| Fundamental Theorem for Line Integrals ([[§109 The Fundamental Theorem for Line Integrals#^thm-109-1\|Theorem §109.1]]) | $\displaystyle\int_C \nabla f \cdot d\mathbf{r} = f(\mathbf{r}(b)) - f(\mathbf{r}(a))$ | curve $C$; endpoints $\mathbf{r}(a)$, $\mathbf{r}(b)$ |
| Green's Theorem ([[§110 Green's Theorem#^thm-110-1\|Theorem §110.1]]) | $\displaystyle\iint_D \left( \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right) dA = \int_C P\,dx + Q\,dy$ | plane region $D$; boundary curve $C$, counterclockwise |
| Stokes' Theorem ([[§114 Stokes' Theorem#^thm-114-1\|Theorem §114.1]]) | $\displaystyle\iint_S \operatorname{curl}\mathbf{F} \cdot d\mathbf{S} = \int_C \mathbf{F} \cdot d\mathbf{r}$ | oriented surface $S$ with normal $\mathbf{n}$; boundary curve $C$, positively oriented |
| Divergence Theorem ([[§115 The Divergence Theorem#^thm-115-1\|Theorem §115.1]]) | $\displaystyle\iiint_E \operatorname{div}\mathbf{F}\,dV = \iint_S \mathbf{F} \cdot d\mathbf{S}$ | solid $E$; boundary surface $S$, outward normal |

Related forms: the vector forms of Green's Theorem, $\oint_C \mathbf{F} \cdot \mathbf{T}\,ds = \iint_D (\operatorname{curl}\mathbf{F}) \cdot \mathbf{k}\,dA$ ([[§111 Curl and Divergence#^thm-111-4|Theorem §111.4]], the flat case of Stokes) and $\oint_C \mathbf{F} \cdot \mathbf{n}\,ds = \iint_D \operatorname{div}\mathbf{F}\,dA$ ([[§111 Curl and Divergence#^thm-111-5|Theorem §111.5]], the flat case of the Divergence Theorem). All five are cases of the [[Generalized Stokes' Theorem]] $\int_M d\omega = \int_{\partial M} \omega$ ([[§23 The Generalized Stokes' Theorem#^thm-23-1|452 Thm. §23.1]]).

Companion facts that the theorems rest on or imply:
- $\operatorname{curl}(\nabla f) = \mathbf{0}$ ([[§111 Curl and Divergence#^thm-111-1|Theorem §111.1]]) and $\operatorname{div}(\operatorname{curl}\mathbf{F}) = 0$ ([[§111 Curl and Divergence#^thm-111-3|Theorem §111.3]]).
- Conservative $\Leftrightarrow$ path independent $\Leftrightarrow$ zero around closed paths ([[§109 The Fundamental Theorem for Line Integrals#^thm-109-2|Theorem §109.2]], [[§109 The Fundamental Theorem for Line Integrals#^thm-109-3|Theorem §109.3]]); tests: $P_y = Q_x$ on a simply-connected plane region ([[§110 Green's Theorem#^thm-110-5|Theorem §110.5]]), $\operatorname{curl}\mathbf{F} = \mathbf{0}$ on $\mathbb{R}^3$ ([[§114 Stokes' Theorem#^thm-114-4|Theorem §114.4]]).
- Curl as circulation per unit area ([[§114 Stokes' Theorem#^thm-114-3|Theorem §114.3]]) and divergence as flux per unit volume ([[§115 The Divergence Theorem#^thm-115-3|Theorem §115.3]]).

## Central results
- [[Fundamental Theorem for Line Integrals]] (§109.1)
- [[Test for Conservative Fields]] (§110.5)

## Load-bearing results
Ranked by how many later results depend on them (through the proofs' citations).
- [[§108 Line Integrals#^thm-108-2|Theorem §108.2: Evaluating Line Integrals with Respect to x and y]]: 26 later results
- [[§108 Line Integrals#^thm-108-1|Theorem §108.1: Evaluating a Line Integral with Respect to Arc Length]]: 24 later results
- [[§108 Line Integrals#^thm-108-4|Theorem §108.4: Reversing the Orientation]]: 23 later results
- [[§108 Line Integrals#^thm-108-5|Theorem §108.5: Evaluating Line Integrals in Space]]: 23 later results
