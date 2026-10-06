---
type: section
subject: "[[Multivariable Analysis]]"
chapter: 4
section: 21
tags: [multivariable-analysis, math452]
---
← [[§20 Multivariable Integration]] · ↑ [[· 4 Integration on Flat Domains]] · [[§22 Properties of the Integral]] →

## Definition of the Integral

Now we define the integral of a function over a Jordan measurable set, analogous to Riemann integration in one dimension ([[§32 The Definition of the Riemann Integral|451 §32]]).

> [!definition] Definition §36.2: Partition
> Let $D \subseteq \mathbb{R}^2$ be a bounded, Jordan measurable set. A **partition** of $D$ is a finite collection:
>
> $$
> \mathcal{T} = \{D_1, D_2, \ldots, D_N\}
> $$
>
> of Jordan measurable sets such that:
> 1. $\bigcup_{i=1}^{N} D_i = D$ (the pieces cover $D$)
> 2. $D_i$ and $D_j$ are almost disjoint for $i \neq j$ (interiors don't overlap)

^def-21-1

> [!definition] Definition §21.2: Upper Sum
> Given a bounded function $f: D \to \mathbb{R}$ and a partition $\mathcal{T} = \{D_1, \ldots, D_N\}$, define:
>
> $$
> M_i = \sup_{(x,y) \in D_i} f(x, y).
> $$
>
> The **upper sum** is:
>
> $$
> U(f, \mathcal{T}) = \sum_{i=1}^{N} M_i |D_i|.
> $$

^def-21-2

> [!definition] Definition §21.3: Lower Sum
> Given a bounded function $f: D \to \mathbb{R}$ and a partition $\mathcal{T} = \{D_1, \ldots, D_N\}$, define:
>
> $$
> m_i = \inf_{(x,y) \in D_i} f(x, y).
> $$
>
> The **lower sum** is:
>
> $$
> L(f, \mathcal{T}) = \sum_{i=1}^{N} m_i |D_i|.
> $$

^def-21-3

> [!remark]- Connections
> - 1D version: [[§32 The Definition of the Riemann Integral#^def-32-3|upper and lower (Darboux) sums]] (451 §32.1), with subintervals of length $t_k - t_{k-1}$ in place of pieces of area $|D_i|$.
> - The same 1D sums in 551, as the motivation for the Lebesgue integral: [[§8 Motivation꞉ The Riemann Integral#^def-8-2|551 Def. §8.2]].

> [!definition] Definition §21.4: Diameter
> The **diameter** of a set $A \subseteq \mathbb{R}^2$ is:
>
> $$
> \text{diam}(A) = \sup_{\substack{(x, y) \in A \\ (x', y') \in A}} \left| (x, y) - (x', y') \right| = \sup_{\substack{(x, y) \in A \\ (x', y') \in A}} \sqrt{(x - x')^2 + (y - y')^2}.
> $$

^def-21-4

> [!definition] Definition §21.5: Mesh
> The **mesh** (or **norm**) of a partition $\mathcal{T} = \{D_1, \ldots, D_N\}$ is:
>
> $$
> \|\mathcal{T}\| = \max_{1 \leq i \leq N} \text{diam}(D_i).
> $$
>
> This measures the “scale” of the partition — the size of the largest piece.

^def-21-5

> [!definition] Definition §21.6: Integrable Function
> A bounded function $f: D \to \mathbb{R}$ is **integrable** (or **Riemann integrable**) over $D$ if:
>
> $$
> \lim_{\|\mathcal{T}\| \to 0} \sum_{i=1}^{N} (M_i - m_i) |D_i| = 0.
> $$
>
> Equivalently, the difference between the upper and lower sums vanishes as the partition becomes finer.

^def-21-6

![[m452-15-1.svg]]
*The two Darboux staircases over the same partition $\mathcal{T}$. Left: the lower sum $L(f,\mathcal{T}) = \sum m_i |D_i|$ with $m_i = \inf_{D_i} f$ — inscribed boxes, entirely under the surface. Right: the upper sum $U(f,\mathcal{T}) = \sum M_i |D_i|$ with $M_i = \sup_{D_i} f$ — circumscribing boxes, containing the surface. Every Riemann sum with arbitrary sample points is squeezed between them: $L(f,\mathcal{T}) \leq \sum f(\boldsymbol{\xi}_i)|D_i| \leq U(f,\mathcal{T})$. Integrability is exactly the statement that the gap $\sum (M_i - m_i)|D_i|$ — the skin between the two staircases — vanishes as $\|\mathcal{T}\| \to 0$; the common limit is $\iint_D f\,dA$. This is the 2D version of the upper/lower [[§32 The Definition of the Riemann Integral#^def-32-3|Darboux sums]] from single-variable analysis (451 §32.1).*

> [!remark] Remark
> The condition says that as we refine the partition (make $\|\mathcal{T}\| \to 0$), the “error” between the upper and lower sums:
>
> $$
> U(f, \mathcal{T}) - L(f, \mathcal{T}) = \sum_{i=1}^{N} (M_i - m_i) |D_i|
> $$
>
> tends to zero. This is analogous to the Riemann criterion for integrability in one dimension ([[§32 The Definition of the Riemann Integral#^thm-32-6|451 §32.6]]).

^rem-21-4

> [!remark]- Connections
> - 1D: the [[§32 The Definition of the Riemann Integral#^thm-32-4|Cauchy criterion]] (451 §32.4) and its mesh form in [[§32 The Definition of the Riemann Integral#^thm-32-6|Equivalence of the Two Integrals]] (451 §32.6).
> - In one variable every Riemann integrable function is Lebesgue integrable with the same integral: [[§23 The Dominated Convergence Theorem#^thm-23-5|551 Thm. §23.5]].
> - Stewart's double integral over a rectangle as a limit of Riemann sums: [[§115 Double Integrals Over Rectangles#^def-115-2|Calc Def. §115.2]] (with worked examples).

> [!definition] Definition §21.7: The Integral
> If $f$ is integrable over $D$, the **integral** of $f$ over $D$ is the common limit:
>
> $$
> \iint_D f(x, y) \, dA = \lim_{\|\mathcal{T}\| \to 0} U(f, \mathcal{T}) = \lim_{\|\mathcal{T}\| \to 0} L(f, \mathcal{T}).
> $$

^def-21-7

> [!remark] Remark: Notation: $dA$, $dx\,dy$, and $dV$
> The symbol $dA$ denotes the **area element**. For rectangular partitions in Cartesian coordinates, each piece $D_i$ is a small rectangle with area $|D_i| = \Delta x \cdot \Delta y$. In the limit, we write:
>
> $$
> dA = dx \, dy.
> $$
>
> Thus, the following notations are equivalent for integrals in Cartesian coordinates:
>
> $$
> \iint_D f(x, y) \, dA = \iint_D f(x, y) \, dx \, dy.
> $$
>
> In other coordinate systems, $dA$ takes a different form. For example, in polar coordinates ([[§22 Properties of the Integral#^thm-22-6|Theorem §22.6]]):
>
> $$
> dA = r \, dr \, d\theta.
> $$
>
> For triple integrals in $\mathbb{R}^3$, we use the **volume element** $dV$:
>
> $$
> dV = dx \, dy \, dz \quad \text{(Cartesian)}, \qquad dV = r \, dr \, d\theta \, dz \quad \text{(cylindrical)}, \qquad dV = \rho^2 \sin\phi \, d\rho \, d\phi \, d\theta \quad \text{(spherical)}.
> $$
>
> The general principle: when changing coordinates via a transformation with Jacobian $J$ ([[§16 The Inverse Function Theorem#^def-16-1|Def. §16.1]]), the volume/area element transforms as:
>
> $$
> dA_{\text{new}} = |J| \, dA_{\text{old}}.
> $$

^rem-21-5

> [!remark] Remark: Evaluating the Integral
> To compute the integral, choose sample points $(\xi_i, \eta_i) \in D_i$ for each piece of the partition. Then:
>
> $$
> \iint_D f(x, y) \, dA = \lim_{\|\mathcal{T}\| \to 0} \sum_{i=1}^{N} f(\xi_i, \eta_i) |D_i|.
> $$
>
> The limit exists and equals the integral regardless of how the sample points are chosen (as long as $f$ is integrable).

^rem-21-6

> [!remark]- Connections
> - 1D: [[§32 The Definition of the Riemann Integral#^def-32-7|Riemann sums]] (451 §32.3) and their agreement with the Darboux integral, [[§32 The Definition of the Riemann Integral#^thm-32-6|451 §32.6]].
> - Stewart's double integral over a rectangle as a limit of Riemann sums: [[§115 Double Integrals Over Rectangles#^def-115-2|Calc Def. §115.2]] (with worked examples).

*Continued in [[§22 Properties of the Integral]]: linearity, additivity over domains, comparison, iterated integrals on rectangles, and polar coordinates.*
