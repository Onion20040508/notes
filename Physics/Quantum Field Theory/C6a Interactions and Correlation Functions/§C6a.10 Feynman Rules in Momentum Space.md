---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C6a
section: C6a.10
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C6a.9 Symmetry Factors in Practice]] · ↑ [[· C6a Interactions and Correlation Functions]] · [[§C6a.11 The iε Limit and Vacuum Bubbles]] →

*Sources: the user's PHY 513 notes, Ch. 14 §14.6 (Derivation "From position space to momentum space", Principle "Feynman rules in momentum space", paragraph "The momentum-space two-point function") · PHY 513 Lecture 14 (Larsen, 26 Oct 2026), Part B, slides 19–20, slide 25 (bottom), and transcript · Peskin & Schroeder, An Introduction to Quantum Field Theory, §4.4, pp. 94–95, eqs. (4.46)–(4.47) · Yu Zhao-Huan, 量子场论讲义, §7.2, pp. 287–288 (rules 8, 10, 11 of the momentum-space rules of Yukawa theory); §7.3, p. 296 (the $\phi^4$ vertex); §10.5.1, eqs. (10.198)–(10.203).*

The position-space rules ([[§C6a.8 Position-Space Feynman Rules#^thm-c6a-8-2|Theorem §C6a.8.2]]) leave an integral $\int d^4z$ at every vertex. Writing every propagator in its four-momentum form ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-9|Theorem §C2b.6.9]]; slide 19, PS eq. (4.46))
$$
D_F(x - y) = \int\frac{d^4p}{(2\pi)^4}\,\frac{i}{p^2 - m^2 + i\varepsilon}\,e^{-ip\cdot(x-y)}
$$
and thinking of its two plane waves as belonging to the two ends of the line, the vertex integrals can be done: each produces a delta function of the momenta that meet there, momentum conservation. What is left is a product of propagators $i/(p^2 - m^2 + i\varepsilon)$ and vertex factors $-i\lambda$, with an integral over each momentum that conservation does not fix. Yu states momentum-space rules in §7.2 for $T$-matrix elements of Yukawa theory (external lines are factors $1$, $u$, $v$ instead of $e^{-ip\cdot x}$, and the amplitude $i\mathcal M$ is separated from an overall $(2\pi)^4\delta^4(p_i - p_f)$), adds the $\phi^4$ vertex on p. 296, and obtains the correlation-function version by Fourier transforming $G^{(n)}$ in §10.5.1 (eqs. (10.198)–(10.203)).

*Conventions* ([[Larsen PHY 513]]): $\tilde D_F(p) = \frac{i}{p^2 - m^2 + i\varepsilon}$; a momentum $p$ assigned to a line from $a$ to $b$ means the factor $e^{-ip\cdot a}$ at $a$ and $e^{+ip\cdot b}$ at $b$ ("$p$ flows from $a$ to $b$"); a momentum flowing *into* a point $z$ carries $e^{+ip\cdot z}$ there.

## The mathematics used here

The plane waves meeting at a vertex integrate to a delta function:

![[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3]]

Doing the space(time) integral before the momentum integrals is an exchange of integrals, justified for wave packets and, for the propagators here, after smearing the external points:

![[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-6]]

and momenta are relabelled and their directions reversed freely:

![[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7]]

## Momentum conservation at the vertices

> [!theorem] Theorem §C6a.10.1: Momentum Is Conserved at Every Vertex
> At a vertex $z$ where four lines with momenta $p_1, \dots, p_4$ flowing *into* $z$ end, the $z$-dependence of the diagram is $e^{i(p_1 + p_2 + p_3 + p_4)\cdot z}$, and the vertex integral is
>
> $$
> \int d^4z\;e^{i(p_1 + p_2 + p_3 + p_4)\cdot z} = (2\pi)^4\,\delta^4(p_1 + p_2 + p_3 + p_4) ,
> $$
>
> an identity of tempered distributions in the momenta ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]]): the four-momentum flowing into every vertex is zero. A loop, a line from $z$ back to $z$, contributes $e^{+ik\cdot z}e^{-ik\cdot z} = 1$ and no momentum.
>
> *Source: PHY 513 Lecture 14, slide 19 · the user's PHY 513 notes, Ch. 14 §14.6 (Derivation "From position space to momentum space") · PS §4.4, eq. (4.47) (with $p_4$ drawn leaving: $(2\pi)^4\delta^{(4)}(p_1 + p_2 + p_3 - p_4)$)*

^thm-c6a-10-1

> [!derivation]- Derivation
> **Step 1** (each line in Fourier form). By [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-9|Theorem §C2b.6.9]], $D_F(a - b) = \int\frac{d^4p}{(2\pi)^4}\tilde D_F(p)\,e^{-ip\cdot a}e^{+ip\cdot b}$. For the four lines at $z$, with momenta oriented into $z$ and $a_j$ the other endpoint,
>
> $$
> D_F(a_j - z) = \int\frac{d^4p_j}{(2\pi)^4}\,\tilde D_F(p_j)\,e^{-ip_j\cdot a_j}\,e^{+ip_j\cdot z}, \qquad j = 1, \dots, 4 .
> $$
>
> For a loop at $z$ the two plane waves sit at the same point:
>
> $$
> D_F(z - z) = \int\frac{d^4k}{(2\pi)^4}\,\tilde D_F(k)\,e^{-ik\cdot z}e^{+ik\cdot z} = \int\frac{d^4k}{(2\pi)^4}\,\tilde D_F(k) ,
> $$
>
> independent of $z$.
>
> **Step 2** (collect the $z$-dependence). Multiplying the four lines,
>
> $$
> \prod_{j=1}^4D_F(a_j - z) = \int\prod_{j=1}^4\frac{d^4p_j}{(2\pi)^4}\,\tilde D_F(p_j)\,e^{-ip_j\cdot a_j}\;\cdot\;e^{i(p_1 + p_2 + p_3 + p_4)\cdot z} .
> $$
>
> If the vertex has a loop, two of the four lines are replaced by it:
>
> $$
> D_F(a_1 - z)\,D_F(a_2 - z)\,D_F(z - z) = \int\frac{d^4p_1}{(2\pi)^4}\frac{d^4p_2}{(2\pi)^4}\frac{d^4k}{(2\pi)^4}\,\tilde D_F(p_1)\tilde D_F(p_2)\tilde D_F(k)\,e^{-ip_1\cdot a_1}e^{-ip_2\cdot a_2}\;\cdot\;e^{i(p_1 + p_2)\cdot z} .
> $$
>
> **Step 3** (exchange and integrate). Doing the $z$-integral first, before the momentum integrals (the physicists' route of [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-6|Theorem §CA.3.6]], valid after smearing the external points), [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]] gives
>
> $$
> \int d^4z\prod_{j=1}^4D_F(a_j - z) = \int\prod_{j=1}^4\frac{d^4p_j}{(2\pi)^4}\,\tilde D_F(p_j)\,e^{-ip_j\cdot a_j}\;\int d^4z\,e^{i(p_1 + \dots + p_4)\cdot z} = \int\prod_{j=1}^4\frac{d^4p_j}{(2\pi)^4}\,\tilde D_F(p_j)\,e^{-ip_j\cdot a_j}\;(2\pi)^4\delta^4(p_1 + \dots + p_4) .
> $$
>
> ⚑ By-product: the factor is $(2\pi)^4\delta^4$, not $\delta^4$; the $(2\pi)^4$ cancels one $\frac{1}{(2\pi)^4}$ of a momentum integral when the delta is used,
>
> $$
> \int\frac{d^4p_4}{(2\pi)^4}\,(2\pi)^4\delta^4(p_1 + p_2 + p_3 + p_4)\,F(p_4) = F(-p_1 - p_2 - p_3),
> $$
>
> which is why every remaining momentum integral carries $\frac{d^4p}{(2\pi)^4}$.
>
> ⚑ By-product: $\int d^4z$ over all of $\mathbb R^4$ assumes the vertex time runs over the real axis. In the master formula it runs from $-T(1 - i\varepsilon)$ to $T(1 - i\varepsilon)$ → [[§C6a.11 The iε Limit and Vacuum Bubbles#^thm-c6a-11-1|Theorem §C6a.11.1]].
>
> **What the derivation shows.**
> - Translation invariance of the vertex integral is momentum conservation; the delta functions do the vertex integrals once and for all.

^der-c6a-10-1

*Uses:* [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-9|Theorem §C2b.6.9]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-6|Theorem §CA.3.6]]

> [!theorem] Theorem §C6a.10.2: Feynman Rules for Correlation Functions in Momentum Space
> Each diagram of [[§C6a.8 Position-Space Feynman Rules#^thm-c6a-8-2|Theorem §C6a.8.2]] equals the following expression:
>
> | element | factor |
> |---|---|
> | line (propagator) with momentum $p$ | $\dfrac{i}{p^2 - m^2 + i\varepsilon}$ |
> | vertex (four lines end) | $-i\lambda$ |
> | external point $x$, momentum $p$ entering the diagram at $x$ | $e^{-ip\cdot x}$ |
>
> 1. momentum is conserved at each vertex; the direction assigned to an internal momentum is arbitrary ([[§C6a.7 Feynman Diagrams for Correlation Functions#^thm-c6a-7-2|Theorem §C6a.7.2]], 1);
> 2. every momentum not fixed by conservation is integrated with $\int\frac{d^4p}{(2\pi)^4}$: one per independent loop, plus, for a correlation function with external points, the momenta of the external lines not fixed by the others;
> 3. the result is divided by the symmetry factor $S$ ([[§C6a.8 Position-Space Feynman Rules#^def-c6a-8-1|Def. §C6a.8.1]]).
>
> If the external points are Fourier transformed as well, the factors $e^{-ip\cdot x}$ disappear and a diagram becomes a product of propagators and vertex factors with momentum conservation.
>
> *Source: PHY 513 Lecture 14, slide 20 · the user's PHY 513 notes, Ch. 14 §14.6 (Principle "Feynman rules in momentum space") · PS §4.4, p. 95, rules 1–6 · Yu §7.2, rules 8, 10, 11 (pp. 287–288), §7.3, p. 296 (vertex $-i\lambda$, divide by $S$); §10.5.1, box after eq. (10.203) ("the Fourier transform of a multi-point correlation function corresponds to the Feynman diagrams in momentum space")*

^thm-c6a-10-2

> [!derivation]- Derivation
> **Step 1** (the diagram in position space). Take a diagram with $V$ vertices $z_1, \dots, z_V$, $I$ internal lines (between vertices, loops included) and $r$ external points. Orient each line $\ell$, from $a_\ell$ to $b_\ell$. By [[§C6a.8 Position-Space Feynman Rules#^thm-c6a-8-2|Theorem §C6a.8.2]] its value is
>
> $$
> \frac1S\prod_{v=1}^V\Bigl(-i\lambda\int d^4z_v\Bigr)\prod_\ell D_F(a_\ell - b_\ell) .
> $$
>
> **Step 2** (Fourier form of every line). Insert $D_F(a_\ell - b_\ell) = \int\frac{d^4p_\ell}{(2\pi)^4}\tilde D_F(p_\ell)\,e^{-ip_\ell\cdot a_\ell}e^{+ip_\ell\cdot b_\ell}$ (Step 1 of [[§C6a.10 Feynman Rules in Momentum Space#^der-c6a-10-1|Derivation §C6a.10.1]]). The orientation does not matter: with $p \to -p$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|Theorem §CA.3.7]], 1) and $\tilde D_F(-p) = \tilde D_F(p)$ (it depends on $p^2$ only; [[§C6a.7 Feynman Diagrams for Correlation Functions#^thm-c6a-7-2|Theorem §C6a.7.2]], 1),
>
> $$
> D_F(b - a) = \int\frac{d^4p}{(2\pi)^4}\tilde D_F(p)\,e^{-ip\cdot b}e^{+ip\cdot a} = \int\frac{d^4p}{(2\pi)^4}\tilde D_F(-p)\,e^{+ip\cdot b}e^{-ip\cdot a} = D_F(a - b) .
> $$
>
> This is rule 1's second sentence.
>
> **Step 3** (vertices). Collect the plane waves at each vertex. With $P_v = \sum_{\ell\text{ ending at }v}p_\ell - \sum_{\ell\text{ starting at }v}p_\ell$ the momentum flowing into $z_v$ (a loop at $v$ contributes $p_\ell - p_\ell = 0$),
>
> $$
> \frac1S\int\prod_\ell\frac{d^4p_\ell}{(2\pi)^4}\tilde D_F(p_\ell)\;\prod_{\text{ext. ends}}e^{\mp ip_\ell\cdot x}\;\prod_{v=1}^V\Bigl[(-i\lambda)\int d^4z_v\,e^{iP_v\cdot z_v}\Bigr] = \frac1S\int\prod_\ell\frac{d^4p_\ell}{(2\pi)^4}\tilde D_F(p_\ell)\;\prod_{\text{ext. ends}}e^{\mp ip_\ell\cdot x}\;\prod_{v=1}^V\Bigl[(-i\lambda)\,(2\pi)^4\delta^4(P_v)\Bigr]
> $$
>
> ([[§C6a.10 Feynman Rules in Momentum Space#^thm-c6a-10-1|Theorem §C6a.10.1]]): of the vertex factor $-i\lambda\int d^4z$ there remains $-i\lambda$, with conservation $P_v = 0$.
>
> **Step 4** (lines). Each line leaves $\frac{d^4p_\ell}{(2\pi)^4}\tilde D_F(p_\ell)$: the propagator rule.
>
> **Step 5** (external points). A line ending at the external point $x$ leaves its plane wave there; oriented from $x$ into the diagram it is $e^{-ip\cdot x}$: "the wave function factor for a real particle" (slide 19).
>
> **Step 6** (use the deltas). Each delta does one momentum integral, its $(2\pi)^4$ cancelling that integral's $(2\pi)^{-4}$ (⚑ of [[§C6a.10 Feynman Rules in Momentum Space#^der-c6a-10-1|Derivation §C6a.10.1]]). In a connected piece with at least one external point and at least one vertex the $V$ deltas of its vertices are independent (order the vertices along a spanning tree from an external point; each new vertex fixes the momentum of the tree line leading to it), so of its $I + r$ momentum integrals
>
> $$
> (I + r) - V
> $$
>
> remain. (A single line from $x$ to $y$ has one momentum and no delta.)
>
> ⚑ By-product: a connected graph with $N$ nodes and $M$ edges has $M - N + 1$ independent cycles. Here $N = V + r$ and $M = I + r$, so
>
> $$
> L = (I + r) - (V + r) + 1 = I - V + 1, \qquad (I + r) - V = L + r - 1 :
> $$
>
> one integral per loop and the external momenta but one, fixed by overall conservation. For the tadpole ($V = 1$, $I = 1$, $r = 2$): $L = 1$, two integrals ([[§C6a.10 Feynman Rules in Momentum Space#^ex-c6a-10-1|Example §C6a.10.1]]). Written here (the counting is not on the slides; PS p. 95 "integrate over each undetermined momentum").
>
> **Step 7** ($S$). The coefficient $1/S$ of [[§C6a.8 Position-Space Feynman Rules#^thm-c6a-8-1|Theorem §C6a.8.1]] is a number and is unchanged.
>
> **Step 8** (Fourier transform in the external points). For a factor $\int\frac{d^4p}{(2\pi)^4}e^{-ip\cdot x}F(p)$, by [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]],
>
> $$
> \int d^4x\,e^{iq\cdot x}\int\frac{d^4p}{(2\pi)^4}\,e^{-ip\cdot x}F(p) = \int\frac{d^4p}{(2\pi)^4}\,(2\pi)^4\delta^4(q - p)\,F(p) = F(q) :
> $$
>
> the external momentum becomes the transform variable and its integral and plane wave disappear, leaving the overall delta of conservation (Yu eqs. (10.199)–(10.203)).
>
> **What the derivation shows.**
> - The momentum-space rules are the position-space rules with the vertex integrals done; nothing new is assumed.
> - Loop momenta are not fixed by conservation, and their integrals are where the divergences live ([[§C6a.10 Feynman Rules in Momentum Space#^thm-c6a-10-3|Theorem §C6a.10.3]], below).

^der-c6a-10-2

*Uses:* [[§C6a.8 Position-Space Feynman Rules#^thm-c6a-8-2|Theorem §C6a.8.2]], [[§C6a.10 Feynman Rules in Momentum Space#^thm-c6a-10-1|Theorem §C6a.10.1]], [[§C6a.8 Position-Space Feynman Rules#^thm-c6a-8-1|Theorem §C6a.8.1]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|Theorem §CA.3.7]], [[§C6a.7 Feynman Diagrams for Correlation Functions#^thm-c6a-7-2|Theorem §C6a.7.2]]

> [!caution] Caution: Momentum directions
> The slides attach $e^{-ip\cdot x}$ to the start and $e^{ip\cdot y}$ to the end of a line and add the momenta at a vertex as $e^{i(p_1 + p_2 + p_3 + p_4)\cdot z}$, all four flowing in (slide 19). PS draw $p_4$ leaving the vertex, $e^{+ip_4\cdot z}$ with their sign of the exponent, and get $\delta^{(4)}(p_1 + p_2 + p_3 - p_4)$ (eq. (4.47)). Only the arrow convention differs; the content, "momentum in = momentum out", is the same. For an external point the slides' "$e^{-ipx}$ (incoming momenta)" means $p$ flows from $x$ into the diagram.
>
> *Source: PHY 513 Lecture 14, slides 19–20 · PS §4.4, eq. (4.47) and p. 95*

^cau-c6a-10-1

> [!example] Example §C6a.10.1: The Tadpole in Momentum Space
> The first-order tadpole of the two-point function ([[§C6a.7 Feynman Diagrams for Correlation Functions#^thm-c6a-7-1|Theorem §C6a.7.1]]) is
>
> $$
> -\frac{i\lambda}{2}\int d^4z\,D_F(x - z)\,D_F(z - z)\,D_F(z - y) = \int\frac{d^4p}{(2\pi)^4}\,e^{-ip\cdot(x-y)}\;\frac{i}{p^2 - m^2 + i\varepsilon}\Bigl[-\frac{i\lambda}{2}\int\frac{d^4k}{(2\pi)^4}\frac{i}{k^2 - m^2 + i\varepsilon}\Bigr]\frac{i}{p^2 - m^2 + i\varepsilon} .
> $$
>
> **Step 0** (where the left side comes from). The twelve complete contractions of class (b) in Step 4 of [[§C6a.7 Feynman Diagrams for Correlation Functions#^der-c6a-7-1|Derivation §C6a.7.1]],
>
> $$
> \overbracket{\hat\phi_x\hat\phi_{z_a}}\,\overbracket{\hat\phi_y\hat\phi_{z_b}}\,\overbracket{\hat\phi_{z_c}\hat\phi_{z_d}} = D_F(x - z)\,D_F(y - z)\,D_F(z - z) \qquad (a \ne b),
> $$
>
> each with $-\frac{i\lambda}{4!}\int d^4z$, give $-\frac{12\,i\lambda}{24}\int d^4z\,D_F(x - z)D_F(z - z)D_F(z - y)$, the left side.
>
> **Step 1** (Fourier forms). Momentum $p_1$ from $x$ to $z$, $p_2$ from $z$ to $y$, $k$ around the loop:
>
> $$
> D_F(x - z) = \int\frac{d^4p_1}{(2\pi)^4}\tilde D_F(p_1)e^{-ip_1\cdot x}e^{ip_1\cdot z},\quad D_F(z - y) = \int\frac{d^4p_2}{(2\pi)^4}\tilde D_F(p_2)e^{-ip_2\cdot z}e^{ip_2\cdot y},\quad D_F(z - z) = \int\frac{d^4k}{(2\pi)^4}\tilde D_F(k) .
> $$
>
> **Step 2** (substitute). The left side becomes
>
> $$
> -\frac{i\lambda}{2}\int d^4z\int\frac{d^4p_1}{(2\pi)^4}\frac{d^4p_2}{(2\pi)^4}\frac{d^4k}{(2\pi)^4}\,\tilde D_F(p_1)\tilde D_F(k)\tilde D_F(p_2)\,e^{-ip_1\cdot x}e^{ip_2\cdot y}\;e^{i(p_1 - p_2)\cdot z} ,
> $$
>
> the $z$-dependence being $e^{ip_1\cdot z}e^{-ip_2\cdot z} = e^{i(p_1 - p_2)\cdot z}$ (the loop's plane waves cancel).
>
> **Step 3** (the vertex). $\int d^4z\,e^{i(p_1 - p_2)\cdot z} = (2\pi)^4\delta^4(p_1 - p_2)$ ([[§C6a.10 Feynman Rules in Momentum Space#^thm-c6a-10-1|Theorem §C6a.10.1]]):
>
> $$
> -\frac{i\lambda}{2}\int\frac{d^4p_1}{(2\pi)^4}\frac{d^4p_2}{(2\pi)^4}\frac{d^4k}{(2\pi)^4}\,\tilde D_F(p_1)\tilde D_F(k)\tilde D_F(p_2)\,e^{-ip_1\cdot x}e^{ip_2\cdot y}\,(2\pi)^4\delta^4(p_1 - p_2) .
> $$
>
> **Step 4** (integrate the delta). The $p_2$-integral sets $p_2 = p_1 \equiv p$, its $(2\pi)^{-4}$ cancels the $(2\pi)^4$, and $e^{-ip\cdot x}e^{ip\cdot y} = e^{-ip\cdot(x-y)}$:
>
> $$
> -\frac{i\lambda}{2}\int\frac{d^4p}{(2\pi)^4}\frac{d^4k}{(2\pi)^4}\,\tilde D_F(p)\,\tilde D_F(k)\,\tilde D_F(p)\,e^{-ip\cdot(x-y)} ,
> $$
>
> which is the right side with $\tilde D_F(p) = \frac{i}{p^2 - m^2 + i\varepsilon}$.
>
> **Step 5** (read off). The momentum $p$ enters at $x$ and leaves at $y$, unchanged by the vertex; $k$ circulates in the loop and is integrated over, undetermined by conservation ($L = 1$, $r = 2$: two integrals, [[§C6a.10 Feynman Rules in Momentum Space#^thm-c6a-10-2|Theorem §C6a.10.2]]). The bracket is the loop with its vertex and symmetry factor.
>
> (The user's notes call this "the second-order term of the two-point function"; it is the term of first order in $\lambda$.)
>
> *Source: the user's PHY 513 notes, Ch. 14 §14.6 (Derivation "From position space to momentum space", example "the tadpole") · PHY 513 Lecture 14, slide 25 (bottom diagram)*

^ex-c6a-10-1

> [!theorem] Theorem §C6a.10.3: The Loop Factor D_F(0) Diverges Quadratically
> After the Wick rotation the loop factor of the tadpole is a Euclidean integral,
>
> $$
> D_F(0) = \int\frac{d^4k}{(2\pi)^4}\frac{i}{k^2 - m^2 + i\varepsilon} = \int\frac{d^4k_E}{(2\pi)^4}\frac{1}{k_E^2 + m^2} ,
> $$
>
> and with the cutoff $k_E \le \Lambda$
>
> $$
> D_F(0)_\Lambda = \frac{1}{16\pi^2}\Bigl[\Lambda^2 - m^2\ln\Bigl(1 + \frac{\Lambda^2}{m^2}\Bigr)\Bigr] = \frac{\Lambda^2}{16\pi^2} + O(m^2\ln\Lambda) \qquad (\Lambda \to \infty) :
> $$
>
> it diverges quadratically.
>
> *Source: PHY 513 Lecture 14, transcript ("you divide it by zero … doesn't actually make sense") · the user's PHY 513 notes, Ch. 14 §14.6 (paragraph "The momentum-space two-point function": "The loop integral over $k$ diverges at large $k$") · the cutoff evaluation written here*

^thm-c6a-10-3

> [!derivation]- Derivation
> **Step 1** (Wick rotation). [[§C2b.7 Wick Rotation and the Two-Point Family#^thm-c2b-7-1|Theorem §C2b.7.1]] with $F = 1$ (analytic everywhere; $1/(k^2 - m^2)$ decays like $1/|k^0|^2$, faster than $1/|k^0|$): $k^0 = ik_4$, $k^2 = -k_E^2$, $dk^0 = i\,dk_4$, and
>
> $$
> \int\frac{d^4k}{(2\pi)^4}\frac{i}{k^2 - m^2 + i\varepsilon} = \int\frac{i\,dk_4\,d^3k}{(2\pi)^4}\,\frac{i}{-k_E^2 - m^2} = \int\frac{d^4k_E}{(2\pi)^4}\frac{1}{k_E^2 + m^2} .
> $$
>
> **Step 2** (polar coordinates). The integrand depends on $k_E = |k_E|$ only; $d^4k_E = 2\pi^2k_E^3\,dk_E$ ($2\pi^2$ the area of the unit 3-sphere):
>
> $$
> D_F(0)_\Lambda = \frac{2\pi^2}{(2\pi)^4}\int_0^\Lambda\frac{k_E^3\,dk_E}{k_E^2 + m^2} = \frac{1}{8\pi^2}\int_0^\Lambda\frac{k_E^3\,dk_E}{k_E^2 + m^2} .
> $$
>
> **Step 3** (substitute $u = k_E^2$, $du = 2k_E\,dk_E$).
>
> $$
> \int_0^\Lambda\frac{k_E^3\,dk_E}{k_E^2 + m^2} = \frac12\int_0^{\Lambda^2}\frac{u\,du}{u + m^2} = \frac12\int_0^{\Lambda^2}\Bigl(1 - \frac{m^2}{u + m^2}\Bigr)du = \frac12\Bigl[\Lambda^2 - m^2\ln\frac{\Lambda^2 + m^2}{m^2}\Bigr] .
> $$
>
> **Step 4** (insert). $\frac{1}{8\pi^2}\cdot\frac12 = \frac{1}{16\pi^2}$, which is the statement; $m^2\ln(1 + \Lambda^2/m^2) = 2m^2\ln\Lambda + O(1)$.
>
> **What the derivation shows.**
> - The divergence is ultraviolet (large $k_E$) and quadratic; the mass only enters the subleading logarithm.

^der-c6a-10-3

*Uses:* [[§C2b.7 Wick Rotation and the Two-Point Family#^thm-c2b-7-1|Theorem §C2b.7.1]]

> [!remark] Remark: The first ultraviolet divergence
> The loop factor $D_F(0)$ diverges at large $k$, quadratically with the cutoff ([[§C6a.10 Feynman Rules in Momentum Space#^thm-c6a-10-3|Theorem §C6a.10.3]]). In position space the same divergence is the value of $D_F$ at zero separation, where $D_F(\xi)$ behaves like $-1/(4\pi^2\xi^2)$ ([[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-5|Theorem §C2b.3.5]], [[§C2b.7 Wick Rotation and the Two-Point Family#^thm-c2b-7-3|Theorem §C2b.7.3]]) and has no value ([[§CA.2 Generalized Functions#^thm-ca-2-9|Theorem §CA.2.9]]). The lecture on the bubbles: "If you actually try to do the integral, you will realize that you divide it by zero … $D_F$ of $z$ minus $z$. No, no, no, doesn't actually make sense." This is the first appearance of the ultraviolet divergences that renormalization deals with, later in the course (QFT C10, planned).
>
> *Source: PHY 513 Lecture 14, transcript · the user's PHY 513 notes, Ch. 14 §14.6 (paragraph "The momentum-space two-point function")*

^rem-c6a-10-1

> [!example]- ★ Example §C6a.10.2: The First-Order Numerator with a Normal-Ordered Interaction
> Take $\hat{\mathcal H}_{\rm int} = \frac{\lambda}{4!}:\!\hat\phi_I^4\!:$ instead of $\frac{\lambda}{4!}\hat\phi_I^4$ (a choice of these notes, not of the course or PS). Write $D_0 = D_F(0)$, $D_{xz} = D_F(x - z)$ etc.
>
> **Step 1** (normal order at one point). Wick's theorem at coincident points (formal, as in [[§C6a.6 Wick's Theorem#^cau-c6a-6-2|§C6a.6, Caution: In what sense Wick's theorem holds]]) with every bracket $= D_0$: $\hat\phi^2 = \,:\!\hat\phi^2\!: + D_0$ and $\hat\phi^4 = \,:\!\hat\phi^4\!: + 6D_0:\!\hat\phi^2\!: + 3D_0^2$ ([[§C6a.6 Wick's Theorem#^ex-c6a-6-1|Example §C6a.6.1]]: 6 one-pair and 3 two-pair terms). Hence
>
> $$
> :\!\hat\phi_I(z)^4\!: = \hat\phi_I(z)^4 - 6D_0\bigl(\hat\phi_I(z)^2 - D_0\bigr) - 3D_0^2 = \hat\phi_I(z)^4 - 6D_0\,\hat\phi_I(z)^2 + 3D_0^2 .
> $$
>
> **Step 2** (the three vacuum values). From [[§C6a.7 Feynman Diagrams for Correlation Functions#^der-c6a-7-1|Derivation §C6a.7.1]], and by Wick's theorem for four and two fields,
>
> $$
> \langle0|T\{\hat\phi_x\hat\phi_y\hat\phi_I(z)^4\}|0\rangle = 3D_{xy}D_0^2 + 12D_{xz}D_{yz}D_0, \quad \langle0|T\{\hat\phi_x\hat\phi_y\hat\phi_I(z)^2\}|0\rangle = D_{xy}D_0 + 2D_{xz}D_{yz}, \quad \langle0|T\{\hat\phi_x\hat\phi_y\}|0\rangle = D_{xy} ,
> $$
>
> the middle one from the $3!! = 3$ pairings $\overbracket{\hat\phi_x\hat\phi_y}\,\overbracket{\hat\phi_{z_1}\hat\phi_{z_2}}$, $\overbracket{\hat\phi_x\hat\phi_{z_1}}\,\overbracket{\hat\phi_y\hat\phi_{z_2}}$, $\overbracket{\hat\phi_x\hat\phi_{z_2}}\,\overbracket{\hat\phi_y\hat\phi_{z_1}}$.
>
> **Step 3** (combine).
>
> $$
> \langle0|T\{\hat\phi_x\hat\phi_y:\!\hat\phi_I(z)^4\!:\}|0\rangle = \bigl(3D_{xy}D_0^2 + 12D_{xz}D_{yz}D_0\bigr) - 6D_0\bigl(D_{xy}D_0 + 2D_{xz}D_{yz}\bigr) + 3D_0^2D_{xy} = (3 - 6 + 3)D_{xy}D_0^2 + (12 - 12)D_{xz}D_{yz}D_0 = 0 .
> $$
>
> Every one of the 15 contractions of [[§C6a.7 Feynman Diagrams for Correlation Functions#^der-c6a-7-1|Derivation §C6a.7.1]] contains a bracket $\overbracket{\hat\phi_{z_a}\hat\phi_{z_b}}$ inside the vertex, and all are removed: neither the tadpole nor the figure-eight appears, exactly the diagrams with $D_F(0)$.
>
> In general (stated, not proved here: Wick's theorem for products with normal-ordered blocks omits the contractions inside a block) no self-contraction at a vertex survives. This removes the vacuum part of $\hat\phi^4$ at a point ([[§C6a.1 From Free to Interacting Fields#^rem-c6a-1-4|§C6a.1, ★ Remark: In what sense φ̂⁴(x) is defined]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-7|Theorem §C2b.6.7]]) but not the divergences of higher loops. The course and PS keep $\hat\phi^4$ without colons.
>
> *Source: written here*

^ex-c6a-10-2

> [!remark] Remark: In what sense the momentum-space rules hold
> At fixed $\varepsilon > 0$, $\tilde D_F$ is a smooth bounded function ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-10|Theorem §C2b.6.10]], 1), so products of propagators at the same momentum (as in [[§C6a.10 Feynman Rules in Momentum Space#^ex-c6a-10-1|Example §C6a.10.1]]) are defined, and $\varepsilon \to 0^+$ is taken at the end, after integrating against the external factors. The vertex deltas are tempered distributions ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]]); in a connected piece attached to external points they are independent and can be integrated one after the other. Two things remain formal: loop integrals, which diverge until the theory is regularized (Remark: The first ultraviolet divergence), and the deltas of vacuum bubbles, where conservation at the last vertex is automatic and the delta is evaluated at zero, $(2\pi)^4\delta^4(0)$ ([[§C6a.11 The iε Limit and Vacuum Bubbles#^thm-c6a-11-3|Theorem §C6a.11.3]]).
>
> *Source: written here, from [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-10|Theorem §C2b.6.10]] and [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]] · PS §4.4, p. 96*

^rem-c6a-10-2

> [!remark] Remark: Yu's route
> Yu writes the momentum-space rules first for $T$-matrix elements of Yukawa theory (§7.2, rules 1–12, pp. 287–288). The scalar propagator $\frac{i}{p^2 - m_\phi^2 + i\epsilon}$ (rule 8), conservation at each vertex (rule 10) and $\int\frac{d^4p}{(2\pi)^4}$ for each undetermined loop momentum (rule 11) are the rules here; his external lines are factors $1$ (scalars, rules 6–7) or spinors $u$, $\bar v$, $\bar u$, $v$, because the external particles are in momentum eigenstates and an overall $(2\pi)^4\delta^4(p_i - p_f)$ is split off the amplitude. For $\phi^4$ theory he adds the vertex $-i\lambda$ and "divide by the symmetry factor" (p. 296). For correlation functions he Fourier transforms $G^{(2)}$ in the external points (eqs. (10.199)–(10.203)), where the $\delta m^2$ insertions form a geometric series that shifts the pole of the propagator (eqs. (10.204)–(10.207)); the course has no counterterm yet.
>
> *Source: Yu §7.2, pp. 286–288; §7.3, p. 296; §10.5.1, pp. 468–470*

^rem-c6a-10-3

> [!remark]- Connections
> - Momentum conservation at a vertex is translation invariance of the interaction, the same invariance that makes $\hat P$ a conserved Noether charge — [[§C1b.5 Noether's Theorem|§C1b.5]], [[§C2a.3 Energy, Momentum and the Zero-Point Energy|§C2a.3]].
> - A propagator $\frac{i}{p^2 - m^2 + i\varepsilon}$ is the Fourier transform of a Green's function, so the rules in momentum space turn integral equations into algebra, as the Fourier transform turns a linear differential equation into multiplication — [[§CA.3 Fourier Transforms and Fourier Tricks#^rem-ca-3-1|§CA.3, Remark: A linear equation becomes algebra]].
> - Loop integrals are done after the Wick rotation, in Euclidean momentum space — [[§C2b.7 Wick Rotation and the Two-Point Family#^thm-c2b-7-1|Theorem §C2b.7.1]].
> - The momentum-space two-point function through first order, without the vacuum bubble, is assembled in [[§C6a.11 The iε Limit and Vacuum Bubbles#^ex-c6a-11-4|Example §C6a.11.4]].
