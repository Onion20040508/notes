---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 6
section: 52
tags: [differentiable-manifolds, math591]
---
← [[§51 One-Forms]] · ↑ [[· 6 Tangent and Cotangent Bundles]] · [[§53 Vector Fields]] →

*Stage: fields — The second derivatives of a function at a critical point form a symmetric bilinear form on the tangent space, the Hessian; it is nondegenerate at every critical point exactly when the one-form $df$, as a section of $T^{\ast}M$, is transverse to the zero section, and then the critical points are isolated.*

*Assignment 5, Problem 3, with what its proof contains. Not from lecture. The problem: the section $p \mapsto (p, df_p)$ of $T^{\ast}M$ is transverse to the zero section exactly when every critical point of $f$ has a nondegenerate Hessian; and what is the critical set of a Morse function? The Hessian, the splitting of $T(T^{\ast}M)$ along the zero section, and the second proofs are filled in around the submitted solution.*

Throughout, $M$ is a smooth manifold of dimension $m$ and $f : M \to \mathbb{R}$ is smooth. Its set of critical points is $\operatorname{Crit}(f) = \{\, p \in M : df_p = 0 \,\}$ (Definition [[§36 Submersions#^def-36-5|§36.5]]), the set of critical points in the sense of Definition [[§36 Submersions#^def-36-3|§36.3]], by Proposition [[§36 Submersions#^prop-36-2|§36.2]].

## The Hessian Matrix

> [!definition] Definition §52.1: Hessian Matrix
> Let $(U, \varphi = (x^1, \ldots, x^m))$ be a smooth chart of $M$, $p \in U$, and $f_\varphi = f \circ \varphi^{-1} : \varphi(U) \to \mathbb{R}$ the coordinate representation of $f$ (Definition [[§29 Coordinate Derivations and the Basis Theorem#^def-29-1|§29.1]](3)). The **Hessian matrix** of $f$ at $p$ in the chart is the $m \times m$ matrix $H_p = \big(H_{ij}(p)\big)$ of second partial derivatives of $f_\varphi$ at $\varphi(p)$:
>
> $$
> H_{ij}(p) = \frac{\partial^2 f_\varphi}{\partial r^i\, \partial r^j}\big(\varphi(p)\big), \qquad i, j = 1, \ldots, m,
> $$
>
> also written $\partial^2 f/\partial x^i \partial x^j(p)$. Written out,
>
> $$
> H_p = \begin{pmatrix}
> \dfrac{\partial^2 f_\varphi}{\partial r^1\, \partial r^1}\big(\varphi(p)\big) & \cdots & \dfrac{\partial^2 f_\varphi}{\partial r^1\, \partial r^m}\big(\varphi(p)\big) \\
> \vdots & \ddots & \vdots \\
> \dfrac{\partial^2 f_\varphi}{\partial r^m\, \partial r^1}\big(\varphi(p)\big) & \cdots & \dfrac{\partial^2 f_\varphi}{\partial r^m\, \partial r^m}\big(\varphi(p)\big)
> \end{pmatrix} .
> $$
> It depends on the chart in general. Only the values of $f$ on $U$ enter, so the definition applies verbatim to a function smooth on an open set containing $U$.

^def-52-1

The function $f_\varphi$ is smooth on the open set $\varphi(U)$ (Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-1|§19.1]]), so its mixed partials are equal (Clairaut's theorem), and $H_p$ is symmetric, $H_{ij}(p) = H_{ji}(p)$. This is part (2) of the next proposition, which rewrites $H_p$ upstairs, on $M$.

> [!theorem] Proposition §52.1: Forms of the Hessian Matrix
> Let $(U, \varphi = (x^1, \ldots, x^m))$ be a smooth chart and $p \in U$.
>
> 1. For each $j$, the function $\partial f/\partial x^j : U \to \mathbb{R}$, $q \mapsto \partial f/\partial x^j(q) = df_q\big(\partial/\partial x^j|_q\big)$, is the $j$-th coefficient of the one-form $df = \sum_j (\partial f/\partial x^j)\, dx^j$ on $U$. It is smooth on $U$, and
>
> $$
> H_{ij}(p) = \frac{\partial}{\partial x^i}\Big|_p \Big[\frac{\partial f}{\partial x^j}\Big] = \frac{\partial}{\partial x^i}\Big(\frac{\partial f}{\partial x^j}\Big)(p) .
> $$
>
> 2. $H_p$ is symmetric: $H_{ij}(p) = H_{ji}(p)$.
> 3. For each $j$,
>
> $$
> d\Big(\frac{\partial f}{\partial x^j}\Big)_p = \sum_{i=1}^m H_{ij}(p)\, dx^i\big|_p ,
> $$
>
> so the $j$-th column of $H_p$ lists the components (Definition [[§33 Covectors in Coordinates#^def-33-1|§33.1]]) of the covector $d(\partial f/\partial x^j)_p$. And the map
>
> $$
> \Phi = \Big(\frac{\partial f}{\partial x^1}, \ldots, \frac{\partial f}{\partial x^m}\Big) \circ \varphi^{-1} : \varphi(U) \longrightarrow \mathbb{R}^m
> $$
>
> is smooth, with Jacobian $\Phi'\big(\varphi(p)\big) = H_p$.

^prop-52-1

> [!proof]+ Proof
> *(Assignment 5, Problem 3: the submitted solution's description of the Hessian, written out.)* Write $g_j = \partial f/\partial x^j : U \to \mathbb{R}$ for $j = 1, \ldots, m$.
>
> *(1)* For $q \in U$, Proposition [[§32 The Cotangent Space#^prop-32-2|§32.2]] with $D = \partial/\partial x^j|_q$ gives $df_q(\partial/\partial x^j|_q) = \partial f/\partial x^j(q) = g_j(q)$. By Proposition [[§51 One-Forms#^prop-51-2|§51.2]], $df$ is a one-form with $df = \sum_j g_j\, dx^j$ on $U$, and $g_j(q) = df_q(\partial/\partial x^j|_q)$ is exactly the $j$-th coefficient function of Proposition [[§51 One-Forms#^prop-51-1|§51.1]] for $\theta = df$. Lemma [[§29 Coordinate Derivations and the Basis Theorem#^lem-29-1|§29.1]], applied to the restriction of $f$ to $U$, gives that $g_j$ is smooth on $U$ and that
>
> $$
> g_j \circ \varphi^{-1} = \frac{\partial f_\varphi}{\partial r^j} \qquad \text{on } \varphi(U). \tag{$\ast$}
> $$
> Now apply Definition [[§29 Coordinate Derivations and the Basis Theorem#^def-29-2|§29.2]] to the function $g_j$ at $p$: its coordinate representation is $g_j \circ \varphi^{-1}$, so, using $(\ast)$,
>
> $$
> \frac{\partial}{\partial x^i}\Big|_p [g_j] = \frac{\partial (g_j \circ \varphi^{-1})}{\partial r^i}\big(\varphi(p)\big) = \frac{\partial}{\partial r^i}\Big(\frac{\partial f_\varphi}{\partial r^j}\Big)\big(\varphi(p)\big) = \frac{\partial^2 f_\varphi}{\partial r^i\, \partial r^j}\big(\varphi(p)\big) = H_{ij}(p),
> $$
>
> the last step by Definition [[§52 Critical Points and the Hessian#^def-52-1|§52.1]].
>
> *(2)* $f_\varphi$ is smooth on the open set $\varphi(U)$ (Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-1|§19.1]]), so by equality of mixed partials (Clairaut's theorem) $\partial^2 f_\varphi/\partial r^i \partial r^j = \partial^2 f_\varphi/\partial r^j \partial r^i$ on $\varphi(U)$; at $\varphi(p)$ this reads $H_{ij}(p) = H_{ji}(p)$.
>
> *(3)* By (1), $g_j$ is smooth on $U$, so Lemma [[§33 Covectors in Coordinates#^lem-33-1|§33.1]] applies to it at $p$:
>
> $$
> d(g_j)_p = \sum_{i=1}^m \frac{\partial g_j}{\partial x^i}(p)\, dx^i\big|_p = \sum_{i=1}^m H_{ij}(p)\, dx^i\big|_p ,
> $$
>
> the second step by (1). By Corollary [[§33 Covectors in Coordinates#^cor-33-2|§33.2]] the coefficients of a covector in the dual basis are its components and are unique; so the $i$-th component of $d(g_j)_p$ is $d(g_j)_p(\partial/\partial x^i|_p) = H_{ij}(p)$, the entry of $H_p$ in row $i$ and column $j$. As $i$ runs from $1$ to $m$ these are the entries of the $j$-th column. For the Jacobian: the $j$-th component of $\Phi$ is $\Phi^j = g_j \circ \varphi^{-1} = \partial f_\varphi/\partial r^j$ by $(\ast)$, a smooth function on $\varphi(U)$; a map into $\mathbb{R}^m$ with smooth components is smooth. By Definition [[§7 The Regular Value Theorem#^def-7-1|§7.1]], the entry of $\Phi'(\varphi(p))$ in row $j$ and column $i$ is
>
> $$
> \frac{\partial \Phi^j}{\partial r^i}\big(\varphi(p)\big) = \frac{\partial}{\partial r^i}\Big(\frac{\partial f_\varphi}{\partial r^j}\Big)\big(\varphi(p)\big) = H_{ij}(p) = H_{ji}(p),
> $$
>
> the last step by (2). So $\Phi'(\varphi(p))$ and $H_p$ have the same entry $H_{ji}(p)$ in row $j$ and column $i$, for all $i, j$: $\Phi'(\varphi(p)) = H_p$. (Without (2) the Jacobian would be the transpose of $H_p$.)

^pf-52-1

*Uses:* [[§32 The Cotangent Space#^prop-32-2|§32.2]], [[§51 One-Forms#^prop-51-2|§51.2]], [[§51 One-Forms#^prop-51-1|§51.1]], [[§29 Coordinate Derivations and the Basis Theorem#^lem-29-1|§29.1]], [[§29 Coordinate Derivations and the Basis Theorem#^def-29-2|Def. §29.2]], [[§52 Critical Points and the Hessian#^def-52-1|Def. §52.1]], [[§19 Smooth Functions and Smooth Maps#^prop-19-1|§19.1]], [[§33 Covectors in Coordinates#^lem-33-1|§33.1]], [[§33 Covectors in Coordinates#^cor-33-2|§33.2]], [[§7 The Regular Value Theorem#^def-7-1|Def. §7.1]]

> [!theorem] Proposition §52.2: Change of Coordinates for the Hessian
> Let $(U, \varphi = (x^1, \ldots, x^m))$ and $(V, \psi = (y^1, \ldots, y^m))$ be smooth charts at $p$, with Hessian matrices $H^{(x)}_p$ and $H^{(y)}_p$ of $f$ at $p$, and let $J$ be the $m \times m$ matrix with entry
>
> $$
> J_{ki} = \frac{\partial y^k}{\partial x^i}(p) \qquad \text{in row } k \text{ and column } i .
> \]
> Written out,
> \[
> J = \begin{pmatrix}
> \dfrac{\partial y^1}{\partial x^1}(p) & \cdots & \dfrac{\partial y^1}{\partial x^m}(p) \\
> \vdots & \ddots & \vdots \\
> \dfrac{\partial y^m}{\partial x^1}(p) & \cdots & \dfrac{\partial y^m}{\partial x^m}(p)
> \end{pmatrix} .
> $$
>
> Then, for all $i, j$,
>
> $$
> H^{(x)}_{ij}(p) = \sum_{k,l=1}^m J_{ki}\, J_{lj}\, H^{(y)}_{kl}(p) \;+\; \sum_{k=1}^m \frac{\partial f}{\partial y^k}(p)\, \frac{\partial^2 y^k}{\partial x^i\, \partial x^j}(p),
> $$
>
> where $\partial^2 y^k/\partial x^i \partial x^j(p) = \partial/\partial x^i|_p\big[\partial y^k/\partial x^j\big]$ is the Hessian matrix of the function $y^k$ in the chart $\varphi$ restricted to $U \cap V$. In matrix form, $H^{(x)}_p = J^{\mathsf T} H^{(y)}_p J + \sum_k \frac{\partial f}{\partial y^k}(p)\, \Big(\frac{\partial^2 y^k}{\partial x^i \partial x^j}(p)\Big)_{i,j}$. If $p$ is a critical point of $f$, the second sum vanishes:
>
> $$
> H^{(x)}_p = J^{\mathsf T} H^{(y)}_p\, J ,
> $$
>
> and then, $J$ being invertible, $\det H^{(x)}_p = (\det J)^2 \det H^{(y)}_p$.

^prop-52-2

> [!proof]+ Proof
> *(Not from lecture; filled in. The idea: write $f_\varphi = f_\psi \circ \tau$ for the transition map $\tau$ and differentiate twice downstairs.)* Three things are claimed: the formula, its simplification at a critical point, and the determinant identity.
>
> *Setting up.* Restrict both charts to $U \cap V \ni p$; the restrictions are smooth charts by Lemma [[§17 Differentiable Structures#^lem-17-6|§17.6]](1), applied to the open subset $U \cap V$ of $U$ and of $V$. This changes neither the Hessian matrices at $p$ nor any partial derivative at $p$: these are ordinary partial derivatives at $\varphi(p)$ or $\psi(p)$ of coordinate representations, which only get restricted to an open set around that point. So assume $U = V$. Let $\tau = \psi \circ \varphi^{-1} : \varphi(U) \to \psi(U)$ be the transition map, smooth because the charts are compatible (Definition [[§17 Differentiable Structures#^def-17-4|§17.4]]), with components $\tau^k = r^k \circ \tau$. Put $a = \varphi(p)$, so $\tau(a) = \psi(p)$.
>
> *Three translations between upstairs and downstairs.* (i) $f_\varphi = f_\psi \circ \tau$ on $\varphi(U)$: for $r \in \varphi(U)$, $\varphi^{-1}(r) \in U$, so $f_\psi(\tau(r)) = f\big(\psi^{-1}(\psi(\varphi^{-1}(r)))\big) = f(\varphi^{-1}(r)) = f_\varphi(r)$. (ii) $y^k \circ \varphi^{-1} = r^k \circ \psi \circ \varphi^{-1} = \tau^k$ (Definition [[§29 Coordinate Derivations and the Basis Theorem#^def-29-1|§29.1]](2) for $\psi$), a smooth function on $\varphi(U)$; so $y^k$ is smooth on $U$ (Definition [[§19 Smooth Functions and Smooth Maps#^def-19-2|§19.2]], with the chart $\varphi$), with coordinate representation $(y^k)_\varphi = \tau^k$. Lemma [[§29 Coordinate Derivations and the Basis Theorem#^lem-29-1|§29.1]], applied to $y^k \in C^\infty(U)$, gives that $\partial y^k/\partial x^j$ is smooth on $U$ and, for every $q \in U$,
>
> $$
> \frac{\partial y^k}{\partial x^j}(q) = \frac{\partial \tau^k}{\partial r^j}\big(\varphi(q)\big), \quad\text{that is,}\quad \frac{\partial y^k}{\partial x^j} \circ \varphi^{-1} = \frac{\partial \tau^k}{\partial r^j} \ \text{ on } \varphi(U) ;
> $$
>
> in particular $J_{kj} = \partial \tau^k/\partial r^j(a)$, and applying Definition [[§29 Coordinate Derivations and the Basis Theorem#^def-29-2|§29.2]] once more, now to the smooth function $\partial y^k/\partial x^j$ on $U$,
>
> $$
> \frac{\partial^2 y^k}{\partial x^i\, \partial x^j}(p) = \frac{\partial}{\partial r^i}\Big(\frac{\partial y^k}{\partial x^j} \circ \varphi^{-1}\Big)(a) = \frac{\partial^2 \tau^k}{\partial r^i\, \partial r^j}(a) .
> $$
>
> (iii) By Definitions [[§29 Coordinate Derivations and the Basis Theorem#^def-29-2|§29.2]] and [[§52 Critical Points and the Hessian#^def-52-1|§52.1]] in the chart $\psi$, $\partial f/\partial y^k(p) = \partial f_\psi/\partial r^k(\tau(a))$ and $H^{(y)}_{kl}(p) = \partial^2 f_\psi/\partial r^k \partial r^l(\tau(a))$.
>
> *Differentiating twice.* By (i) and the chain rule in $\mathbb{R}^m$, for $r \in \varphi(U)$,
>
> $$
> \frac{\partial f_\varphi}{\partial r^j}(r) = \sum_{l=1}^m \frac{\partial f_\psi}{\partial r^l}\big(\tau(r)\big)\, \frac{\partial \tau^l}{\partial r^j}(r) .
> $$
>
> Differentiate this with respect to $r^i$. Each term is a product of the two smooth functions $r \mapsto \partial f_\psi/\partial r^l(\tau(r))$ and $\partial \tau^l/\partial r^j$; by the product rule, and the chain rule once more for the first factor, $\frac{\partial}{\partial r^i}\big[\frac{\partial f_\psi}{\partial r^l}(\tau(r))\big] = \sum_k \frac{\partial^2 f_\psi}{\partial r^k \partial r^l}(\tau(r))\, \frac{\partial \tau^k}{\partial r^i}(r)$, so
>
> $$
> \frac{\partial^2 f_\varphi}{\partial r^i\, \partial r^j}(r) = \sum_{l=1}^m \sum_{k=1}^m \frac{\partial^2 f_\psi}{\partial r^k\, \partial r^l}\big(\tau(r)\big)\, \frac{\partial \tau^k}{\partial r^i}(r)\, \frac{\partial \tau^l}{\partial r^j}(r) \;+\; \sum_{l=1}^m \frac{\partial f_\psi}{\partial r^l}\big(\tau(r)\big)\, \frac{\partial^2 \tau^l}{\partial r^i\, \partial r^j}(r) .
> $$
>
> At $r = a$ the left side is $H^{(x)}_{ij}(p)$ (Definition [[§52 Critical Points and the Hessian#^def-52-1|§52.1]]), and by (ii) and (iii) the right side is
>
> $$
> \sum_{k,l} H^{(y)}_{kl}(p)\, J_{ki}\, J_{lj} \;+\; \sum_{l} \frac{\partial f}{\partial y^l}(p)\, \frac{\partial^2 y^l}{\partial x^i\, \partial x^j}(p) ;
> $$
>
> renaming the summation index $l$ to $k$ in the second sum gives the formula. In matrix form, the first sum is $\sum_{k,l} (J^{\mathsf T})_{ik}\, H^{(y)}_{kl}\, J_{lj} = (J^{\mathsf T} H^{(y)}_p J)_{ij}$, by the definition of matrix multiplication.
>
> *At a critical point.* If $p$ is critical, then $\partial f/\partial y^k(p) = 0$ for every $k$ (Proposition [[§36 Submersions#^prop-36-2|§36.2]], in the chart $\psi$), so every term of the second sum is $0$ and $H^{(x)}_p = J^{\mathsf T} H^{(y)}_p J$.
>
> *The determinant.* $J = \big[\partial y^k/\partial x^i(p)\big]$ is invertible, with inverse $\big[\partial x^i/\partial y^k(p)\big]$: Corollary [[§30 The Differential in Coordinates#^cor-30-4|§30.4]](3), applied to the charts $\varphi$ and $\psi$ at $p$. The determinant is multiplicative and $\det J^{\mathsf T} = \det J$, so $\det H^{(x)}_p = \det J^{\mathsf T} \det H^{(y)}_p \det J = (\det J)^2 \det H^{(y)}_p$.

^pf-52-2

*Uses:* [[§17 Differentiable Structures#^lem-17-6|§17.6]], [[§17 Differentiable Structures#^def-17-4|Def. §17.4]], [[§29 Coordinate Derivations and the Basis Theorem#^def-29-1|Def. §29.1]], [[§19 Smooth Functions and Smooth Maps#^def-19-2|Def. §19.2]], [[§29 Coordinate Derivations and the Basis Theorem#^lem-29-1|§29.1]], [[§29 Coordinate Derivations and the Basis Theorem#^def-29-2|Def. §29.2]], [[§52 Critical Points and the Hessian#^def-52-1|Def. §52.1]], [[§36 Submersions#^prop-36-2|§36.2]], [[§30 The Differential in Coordinates#^cor-30-4|§30.4]]

> [!example] Example §52.1: The Hessian Matrix Depends on the Chart
> Away from critical points the second sum is genuinely there. On $M = \mathbb{R}$ take $f(t) = t$ and $p = 0$, and two charts on $U = (-\tfrac12, \infty)$: $\varphi = \mathrm{id}_U$, with coordinate $x$, and $\psi(t) = t + t^2$, with coordinate $y$. Then $H^{(x)}(0) = 0$ but $H^{(y)}(0) = -2$.

^ex-52-1

> [!proof]+ Working out the example
> *$\psi$ is a smooth chart.* On $U$, $\psi'(t) = 1 + 2t > 0$, so $\psi$ is strictly increasing, a bijection of $U$ onto $(-\tfrac14, \infty)$ (as $\psi(-\tfrac12) = -\tfrac14$ and $\psi(t) \to \infty$), with inverse $\psi^{-1}(s) = \tfrac12\big(-1 + \sqrt{1 + 4s}\big)$, smooth because $1 + 4s > 0$. So $\psi$ is a diffeomorphism between open subsets of $\mathbb{R}$, and its transition maps with the global chart $\mathrm{id}_\mathbb{R}$, namely $\psi$ and $\psi^{-1}$, are smooth: $(U, \psi)$ is compatible with the standard atlas (Definition [[§17 Differentiable Structures#^def-17-4|§17.4]]), hence a smooth chart (Theorem [[§17 Differentiable Structures#^thm-17-5|§17.5]]).
>
> *The two Hessians.* In $\varphi$, $f_\varphi(r) = r$, so $H^{(x)}(0) = f_\varphi''(0) = 0$. In $\psi$, $f_\psi(s) = f(\psi^{-1}(s)) = \psi^{-1}(s) = \tfrac12\big(-1 + (1 + 4s)^{1/2}\big)$, whose derivatives are
>
> $$
> f_\psi'(s) = (1 + 4s)^{-1/2}, \qquad f_\psi''(s) = -2\,(1 + 4s)^{-3/2},
> $$
>
> so, at $\psi(0) = 0$, $H^{(y)}(0) = f_\psi''(0) = -2$.
>
> *Check against Proposition [[§52 Critical Points and the Hessian#^prop-52-2|§52.2]].* $J = \partial y/\partial x(0) = \psi'(0) = 1$, $\partial f/\partial y(0) = f_\psi'(0) = 1$ and $\partial^2 y/\partial x^2(0) = \psi''(0) = 2$, so the formula gives $H^{(x)}(0) = 1 \cdot 1 \cdot (-2) + 1 \cdot 2 = 0$, as it should. The point $0$ is not critical, $df_0 \neq 0$; even the rank of the Hessian matrix there, $0$ in one chart and $1$ in the other, depends on the chart.

^pf-ex-52-1

*Uses:* [[§17 Differentiable Structures#^def-17-4|Def. §17.4]], [[§17 Differentiable Structures#^thm-17-5|§17.5]], [[§52 Critical Points and the Hessian#^prop-52-2|§52.2]]

## The Hessian at a Critical Point

At a critical point the transformation law is $H^{(x)}_p = J^{\mathsf T} H^{(y)}_p J$, the law of a bilinear form, and the Hessian matrix becomes the matrix of a chart-free object.

> [!theorem] Proposition §52.3: The Hessian at a Critical Point Is Well Defined
> Let $p \in \operatorname{Crit}(f)$ and $v, w \in T_pM$. For a smooth chart $(U, \varphi = (x^1, \ldots, x^m))$ at $p$, let $v^i = v[x^i]$ and $w^j = w[x^j]$ be the components of $v$ and $w$ (Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]]). Then the number
>
> $$
> \sum_{i,j=1}^m H_{ij}(p)\, v^i\, w^j
> $$
>
> is the same for every chart at $p$; and, as a function of $(v, w)$, it is bilinear and symmetric.

^prop-52-3

> [!proof]+ Proof
> *(Not from lecture; filled in.)* *Independence of the chart.* Let $(V, \psi = (y^1, \ldots, y^m))$ be a second chart at $p$, write $v^{(y)k} = v[y^k]$ and $w^{(y)l} = w[y^l]$ for the components in it, and let $J_{ki} = \partial y^k/\partial x^i(p)$ as in Proposition [[§52 Critical Points and the Hessian#^prop-52-2|§52.2]]. First, the components transform by $J$: Corollary [[§30 The Differential in Coordinates#^cor-30-4|§30.4]](2), applied to the charts $\varphi = (x^i)$ and $\psi = (y^k)$ at $p$ and the vector $v$, gives
>
> $$
> v^{(y)k} = v\big[y^k\big] = \sum_{i=1}^m \frac{\partial y^k}{\partial x^i}(p)\, v\big[x^i\big] = \sum_{i=1}^m J_{ki}\, v^i ,
> $$
>
> and, applied to $w$, likewise $w^{(y)l} = \sum_j J_{lj}\, w^j$. Substituting, expanding the product of the two sums, and then using Proposition [[§52 Critical Points and the Hessian#^prop-52-2|§52.2]] at the critical point $p$ ($\sum_{k,l} J_{ki} H^{(y)}_{kl}(p) J_{lj} = H^{(x)}_{ij}(p)$):
>
> $$
> \sum_{k,l} H^{(y)}_{kl}(p)\, v^{(y)k}\, w^{(y)l} = \sum_{k,l} H^{(y)}_{kl}(p) \Big(\sum_i J_{ki}\, v^i\Big)\Big(\sum_j J_{lj}\, w^j\Big) = \sum_{i,j} \Big(\sum_{k,l} J_{ki}\, H^{(y)}_{kl}(p)\, J_{lj}\Big) v^i w^j = \sum_{i,j} H^{(x)}_{ij}(p)\, v^i w^j .
> $$
>
> So the two charts give the same number.
>
> *Bilinear.* The maps $v \mapsto v^i = v[x^i]$ are linear, because tangent vectors are added and scaled pointwise (Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-2|§28.2]]): $(av + bv')[x^i] = a\,v[x^i] + b\,v'[x^i]$. For fixed $w$ the number $\sum_{i,j} H_{ij}(p)\, v^i w^j$ is a linear combination of the $v^i$ with coefficients $\sum_j H_{ij}(p) w^j$, hence linear in $v$; for fixed $v$ it is likewise linear in $w$.
>
> *Symmetric.* By Proposition [[§52 Critical Points and the Hessian#^prop-52-1|§52.1]](2), $H_{ij}(p) = H_{ji}(p)$, so exchanging the names of the summation indices,
>
> $$
> \sum_{i,j} H_{ij}(p)\, w^i v^j = \sum_{i,j} H_{ji}(p)\, w^j v^i = \sum_{i,j} H_{ij}(p)\, v^i w^j .
> $$

^pf-52-3

*Uses:* [[§52 Critical Points and the Hessian#^prop-52-2|§52.2]], [[§30 The Differential in Coordinates#^cor-30-4|§30.4]], [[§28 Derivations and the Abstract Tangent Space#^def-28-2|Def. §28.2]], [[§52 Critical Points and the Hessian#^prop-52-1|§52.1]]

> [!definition] Definition §52.2: Hessian at a Critical Point
> Let $p \in \operatorname{Crit}(f)$. The **Hessian** of $f$ at $p$ is the symmetric bilinear form
>
> $$
> \operatorname{Hess}_p f : T_pM \times T_pM \longrightarrow \mathbb{R}, \qquad \operatorname{Hess}_p f(v, w) = \sum_{i,j=1}^m H_{ij}(p)\, v^i\, w^j, \quad v^i = v[x^i],\ w^j = w[x^j],
> $$
>
> computed in any smooth chart $(U, \varphi = (x^i))$ at $p$; it does not depend on the chart, and is bilinear and symmetric, by Proposition [[§52 Critical Points and the Hessian#^prop-52-3|§52.3]]. In matrix form, with $H_p$ the Hessian matrix of the chart (Definition [[§52 Critical Points and the Hessian#^def-52-1|§52.1]]),
>
> $$
> \operatorname{Hess}_p f(v, w) = \begin{pmatrix} v^1 & \cdots & v^m \end{pmatrix} H_p \begin{pmatrix} w^1 \\ \vdots \\ w^m \end{pmatrix} .
> $$
> On the coordinate basis, $\operatorname{Hess}_p f\big(\partial/\partial x^i|_p, \partial/\partial x^j|_p\big) = H_{ij}(p)$.

^def-52-2

The last formula holds because the components of $\partial/\partial x^i|_p$ are $\partial/\partial x^i|_p[x^l] = \delta^l_i$ (Lemma [[§33 Covectors in Coordinates#^lem-33-1|§33.1]]: the $dx^l|_p$ form the basis dual to the $\partial/\partial x^i|_p$, and $\partial/\partial x^i|_p[x^l] = dx^l|_p(\partial/\partial x^i|_p)$ by Proposition [[§32 The Cotangent Space#^prop-32-2|§32.2]]), so only the term with $l = i$, $l' = j$ survives in $\sum_{l,l'} H_{ll'}(p)\, \delta^l_i\, \delta^{l'}_j$. At a point that is not critical no such form exists: by Example [[§52 Critical Points and the Hessian#^ex-52-1|§52.1]] the matrices of two charts need not even have the same rank.

> [!definition] Definition §52.3: Nondegenerate Critical Point
> A critical point $p$ of $f$ is **nondegenerate** if $\operatorname{Hess}_p f$ is a non-degenerate pairing (Definition [[§21 Linear Algebra Toolkit#^def-21-5|§21.5]]): the linear maps
>
> $$
> (\operatorname{Hess}_p f)^\flat : T_pM \longrightarrow T_p^{\ast}M, \quad v \longmapsto \operatorname{Hess}_p f(v, \cdot\,), \qquad (\operatorname{Hess}_p f)^\sharp : T_pM \longrightarrow T_p^{\ast}M, \quad w \longmapsto \operatorname{Hess}_p f(\cdot\,, w)
> $$
>
> (Definition [[§21 Linear Algebra Toolkit#^def-21-4|§21.4]]) are injective. Otherwise $p$ is **degenerate**.

^def-52-3

The next proposition makes the condition concrete. Since $\operatorname{Hess}_p f$ is symmetric, it is the injectivity of $(\operatorname{Hess}_p f)^\flat$ alone — equivalently, as $\dim T_pM = \dim T_p^{\ast}M = m$, its bijectivity — and, equivalently, $\det H_p \neq 0$ in some, hence every, chart at $p$.

> [!theorem] Proposition §52.4: The Hessian as a Map $T_pM \to T_p^{\ast}M$
> Let $p \in \operatorname{Crit}(f)$, $B = \operatorname{Hess}_p f$, and $(U, \varphi = (x^1, \ldots, x^m))$ a smooth chart at $p$, with Hessian matrix $H_p$.
>
> 1. For each $j$,
>
> $$
> B^\sharp\Big(\frac{\partial}{\partial x^j}\Big|_p\Big) = \sum_{i=1}^m H_{ij}(p)\, dx^i\big|_p = d\Big(\frac{\partial f}{\partial x^j}\Big)_p ;
> $$
>
> and $B^\flat = B^\sharp$, so that, for each $i$,
>
> $$
> B^\flat\Big(\frac{\partial}{\partial x^i}\Big|_p\Big) = \sum_{j=1}^m H_{ij}(p)\, dx^j\big|_p = d\Big(\frac{\partial f}{\partial x^i}\Big)_p .
> $$
>
> The matrix of $B^\flat : T_pM \to T_p^{\ast}M$ in the bases $\partial/\partial x^i|_p$ and $dx^j|_p$ is $H_p$.
> 2. The following are equivalent:
>   - (a) $p$ is nondegenerate;
>   - (b) $B^\flat$ is injective;
>   - (c) $B^\flat$ is bijective;
>   - (d) $\det H_p \neq 0$ in the chart $\varphi$;
>   - (e) $\det H_p \neq 0$ in every smooth chart at $p$;
>   - (f) the covectors $d(\partial f/\partial x^1)_p, \ldots, d(\partial f/\partial x^m)_p$ are linearly independent.

^prop-52-4

> [!proof]+ Proof
> *(Not from lecture; filled in. Condition (f) is the form in which the submitted solution of Assignment 5, Problem 3 uses nondegeneracy.)* By Definition [[§52 Critical Points and the Hessian#^def-52-2|§52.2]], $B$ is a symmetric bilinear form on $T_pM$ with $B(\partial/\partial x^i|_p, \partial/\partial x^j|_p) = H_{ij}(p)$ (the formula after that definition).
>
> *(1) The map $B^\sharp$.* For each $j$, $B^\sharp(\partial/\partial x^j|_p) = B(\cdot\,, \partial/\partial x^j|_p)$ is a covector (Definition [[§21 Linear Algebra Toolkit#^def-21-4|§21.4]]). Its components (Definition [[§33 Covectors in Coordinates#^def-33-1|§33.1]]) are its values on the basis vectors, $B(\partial/\partial x^i|_p, \partial/\partial x^j|_p) = H_{ij}(p)$. So, by Corollary [[§33 Covectors in Coordinates#^cor-33-2|§33.2]] and Proposition [[§52 Critical Points and the Hessian#^prop-52-1|§52.1]](3),
>
> $$
> B^\sharp\Big(\frac{\partial}{\partial x^j}\Big|_p\Big) = \sum_{i=1}^m H_{ij}(p)\, dx^i\big|_p = d\Big(\frac{\partial f}{\partial x^j}\Big)_p .
> $$
>
> This step does not use the symmetry of $B$.
>
> *(1) The map $B^\flat$.* Symmetry gives, for every $w \in T_pM$, $B^\flat(w) = B(w, \cdot\,) = B(\cdot\,, w) = B^\sharp(w)$; so $B^\flat = B^\sharp$. With the index $j$ of the last display renamed $i$, and using $H_{ji} = H_{ij}$ (Proposition [[§52 Critical Points and the Hessian#^prop-52-1|§52.1]](2)),
>
> $$
> B^\flat\Big(\frac{\partial}{\partial x^i}\Big|_p\Big) = B^\sharp\Big(\frac{\partial}{\partial x^i}\Big|_p\Big) = \sum_{j=1}^m H_{ji}(p)\, dx^j\big|_p = \sum_{j=1}^m H_{ij}(p)\, dx^j\big|_p = d\Big(\frac{\partial f}{\partial x^i}\Big)_p .
> $$
>
> By Proposition [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]](3), the matrix of $B^\flat$ in the bases $\partial/\partial x^i|_p$ and $dx^j|_p$ has in column $i$ the coordinates of this covector, $H_{i1}(p), \ldots, H_{im}(p)$, which are $H_{1i}(p), \ldots, H_{mi}(p)$ by symmetry: it is $H_p$.
>
> *(2), (a) $\Leftrightarrow$ (b).* By Definition [[§21 Linear Algebra Toolkit#^def-21-5|§21.5]], (a) says that $B^\flat$ and $B^\sharp$ are injective. As $B^\sharp = B^\flat$ by (1), left and right non-degeneracy are the same condition, the injectivity of $B^\flat$.
>
> *(b) $\Leftrightarrow$ (c).* $\dim T_pM = m$ (Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]]) and $\dim T_p^{\ast}M = m$ (Lemma [[§33 Covectors in Coordinates#^lem-33-1|§33.1]]); a linear map between spaces of the same finite dimension is injective if and only if it is bijective (Proposition [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]](1)).
>
> *(b) $\Leftrightarrow$ (d).* A linear map between spaces of dimension $m$ is injective exactly when its matrix in a pair of bases is invertible, that is, has nonzero determinant. By (1) the matrix of $B^\flat$ in the bases of the chart $\varphi$ is $H_p$, so $B^\flat$ is injective if and only if $\det H_p \neq 0$.
>
> *(d) $\Leftrightarrow$ (e).* (e) includes (d). Conversely, if (d) holds, then (b) holds; $B^\flat$ is defined without charts, and the equivalence (b) $\Leftrightarrow$ (d) holds in every smooth chart at $p$, so $\det H_p \neq 0$ in every chart. (This also follows from $\det H^{(x)}_p = (\det J)^2 \det H^{(y)}_p$ with $\det J \neq 0$, Proposition [[§52 Critical Points and the Hessian#^prop-52-2|§52.2]].)
>
> *(b) $\Leftrightarrow$ (f).* A linear map is injective exactly when it carries a basis to linearly independent vectors (a linear combination of the images is the image of the same combination of the basis vectors). By (1), $B^\flat$ carries the basis $\partial/\partial x^1|_p, \ldots, \partial/\partial x^m|_p$ of $T_pM$ (Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]]) to $d(\partial f/\partial x^1)_p, \ldots, d(\partial f/\partial x^m)_p$.

^pf-52-4

*Uses:* [[§52 Critical Points and the Hessian#^def-52-2|Def. §52.2]], [[§21 Linear Algebra Toolkit#^def-21-4|Def. §21.4]], [[§33 Covectors in Coordinates#^def-33-1|Def. §33.1]], [[§33 Covectors in Coordinates#^cor-33-2|§33.2]], [[§52 Critical Points and the Hessian#^prop-52-1|§52.1]], [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]], [[§21 Linear Algebra Toolkit#^def-21-5|Def. §21.5]], [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]], [[§33 Covectors in Coordinates#^lem-33-1|§33.1]], [[§52 Critical Points and the Hessian#^prop-52-2|§52.2]]

> [!definition] Definition §52.4: Morse Function
> A smooth function $f : M \to \mathbb{R}$ is a **Morse function** if every critical point of $f$ is nondegenerate (Definition [[§52 Critical Points and the Hessian#^def-52-3|§52.3]]). A function without critical points is a Morse function.

^def-52-4

> [!definition] Definition §52.5: Morse Index
> Let $p \in \operatorname{Crit}(f)$. The **index** of $f$ at $p$ (the **Morse index**) is the number of negative eigenvalues, counted with multiplicity, of the Hessian matrix $H_p$ (Definition [[§52 Critical Points and the Hessian#^def-52-1|§52.1]]) in a smooth chart at $p$. It does not depend on the chart.

^def-52-5

> [!proof]+ Proof (not given in this course)
> *(Not from lecture; Sylvester's law is not proved here.)* At a critical point $p$, $H^{(x)}_p = J^{\mathsf T} H^{(y)}_p J$ with $J$ invertible (Proposition [[§52 Critical Points and the Hessian#^prop-52-2|§52.2]]). By *Sylvester's law of inertia*, a real symmetric matrix $H$ and $J^{\mathsf T} H J$, $J$ invertible, have the same numbers of positive, negative and zero eigenvalues. So the number of negative eigenvalues of $H_p$ does not depend on the chart.

^pf-def-52-5

*Uses:* [[§52 Critical Points and the Hessian#^prop-52-2|§52.2]]

> [!remark] Remark: The Morse Lemma
> *(Not from lecture; not proved here.)* For instance $f = x^2 - y^2$ on $\mathbb{R}^2$ has the single critical point $0$, with $H_0 = \mathrm{diag}(2, -2)$: nondegenerate, of index $1$ (Definition [[§52 Critical Points and the Hessian#^def-52-5|§52.5]]). The *Morse lemma* says that near a nondegenerate critical point $p$ of index $\lambda$ there is a chart $(y^1, \ldots, y^m)$ centred at $p$ in which
>
> $$
> f = f(p) - (y^1)^2 - \cdots - (y^\lambda)^2 + (y^{\lambda+1})^2 + \cdots + (y^m)^2 ;
> $$
>
> so nondegenerate critical points look, up to a change of chart, like the critical point of a nondegenerate quadratic form. Neither Sylvester's law nor the Morse lemma is proved in these notes.
> *(Computed; not from lecture.)* In the chart of the Morse lemma the Hessian matrix at $p$ is block diagonal,
>
> $$
> H_p = \begin{pmatrix} -2\, I_\lambda & 0 \\ 0 & 2\, I_{m-\lambda} \end{pmatrix},
> $$
>
> with exactly $\lambda$ negative eigenvalues, the index.

^rem-52-1

## The Cotangent Bundle Along the Zero Section

*Notation.* Let $(U, \varphi = (x^1, \ldots, x^m))$ be a smooth chart of $M$ and $(T^{\ast}U, \hat\varphi)$ the chart of $T^{\ast}M$ over $U$ (Definition [[§50 The Cotangent Bundle#^def-50-5|§50.5]]). Its $2m$ coordinate functions (Definition [[§29 Coordinate Derivations and the Basis Theorem#^def-29-1|§29.1]](2)) are, at a point $(q, \alpha) \in T^{\ast}U$,

$$
\bar x^i(q, \alpha) = x^i(q), \quad\text{that is, } \bar x^i = x^i \circ \pi, \qquad\qquad \xi_j(q, \alpha) = \alpha\Big(\frac{\partial}{\partial x^j}\Big|_q\Big),
$$

the coordinates of the base point and the components of the covector $\alpha$ (Definition [[§33 Covectors in Coordinates#^def-33-1|§33.1]]). The bar distinguishes the function $\bar x^i$ on $T^{\ast}U$ from the function $x^i$ on $U$; the notes elsewhere write $x^i$ for both (Definition [[§33 Covectors in Coordinates#^def-33-1|§33.1]]). By Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]], the coordinate derivations $\partial/\partial \bar x^1|_{(q,\alpha)}, \ldots, \partial/\partial \bar x^m|_{(q,\alpha)}, \partial/\partial \xi_1|_{(q,\alpha)}, \ldots, \partial/\partial \xi_m|_{(q,\alpha)}$ form a basis of $T_{(q,\alpha)}(T^{\ast}M)$, and every $w$ in it is

$$
w = \sum_{i=1}^m w\big[\bar x^i\big]\, \frac{\partial}{\partial \bar x^i}\Big|_{(q,\alpha)} + \sum_{j=1}^m w\big[\xi_j\big]\, \frac{\partial}{\partial \xi_j}\Big|_{(q,\alpha)} .
$$

In this section covectors at a point are named $\alpha$ or $\eta$, keeping the letters $\xi_j$ for the coordinate functions; the value of the function $\xi_j$ at $(p, \eta)$ is the $j$-th component $\eta_j$ of $\eta$. The image of the zero section $\zeta$ (Definition [[§50 The Cotangent Bundle#^def-50-3|§50.3]]) is written

$$
\mathcal{Z} = \zeta(M) = \{\, (p, 0) : p \in M \,\} \subseteq T^{\ast}M .
$$

> [!theorem] Proposition §52.5: The Zero Section Is a Regular Submanifold
> 1. $\mathcal{Z}$ is a regular submanifold of $T^{\ast}M$ of codimension $m$, and every standard chart $(T^{\ast}U, \hat\varphi)$ is adapted to it:
>
> $$
> \mathcal{Z} \cap T^{\ast}U = \{\, (q, \alpha) \in T^{\ast}U : \xi_1(q, \alpha) = \cdots = \xi_m(q, \alpha) = 0 \,\} .
> $$
>
> 2. $\zeta : M \to T^{\ast}M$ is smooth, and for $p \in U$, $\ \zeta_{\ast p}\big(\partial/\partial x^i|_p\big) = \partial/\partial \bar x^i|_{(p,0)}$.
> 3. For $p \in M$, the tangent space $T_{(p,0)}\mathcal{Z}$, identified with its image under the inclusion $\iota : \mathcal{Z} \hookrightarrow T^{\ast}M$ as in Proposition [[§37 Regular Submanifolds#^prop-37-6|§37.6]], is
>
> $$
> T_{(p,0)}\mathcal{Z} = \operatorname{Span}\Big\{ \frac{\partial}{\partial \bar x^1}\Big|_{(p,0)}, \ldots, \frac{\partial}{\partial \bar x^m}\Big|_{(p,0)} \Big\} = \zeta_{\ast p}(T_pM) .
> $$

^prop-52-5

> [!proof]+ Proof
> *(Assignment 5, Problem 3: the warm-up of the problem, and the submitted solution's description of $T\mathcal{Z}$, written out.)*
>
> *(1)* This is Corollary [[§50 The Cotangent Bundle#^cor-50-3|§50.3]](3), in the present notation. Its proof: a point of $\mathcal{Z}$ is $(p, 0)$, and it lies in $T^{\ast}U$ for any chart $(U, \varphi)$ at $p$. For $(q, \alpha) \in T^{\ast}U$, $\alpha = \sum_j \xi_j(q, \alpha)\, dx^j|_q$ (Corollary [[§33 Covectors in Coordinates#^cor-33-2|§33.2]]), and the $dx^j|_q$ are a basis (Lemma [[§33 Covectors in Coordinates#^lem-33-1|§33.1]]), so $\alpha = 0$ exactly when $\xi_1(q, \alpha) = \cdots = \xi_m(q, \alpha) = 0$. Hence $\mathcal{Z} \cap T^{\ast}U$ is cut out by the vanishing of the last $m$ of the $2m$ coordinates of $\hat\varphi$, which says that $\hat\varphi$ is adapted to $\mathcal{Z}$ (Definition [[§37 Regular Submanifolds#^def-37-3|§37.3]]), and $\mathcal{Z}$ is a regular submanifold of codimension $m$ (Definition [[§37 Regular Submanifolds#^def-37-2|§37.2]], with $2m$ coordinates and $k = m$).
>
> *(2)* $\zeta$ is the zero one-form, $\zeta(q) = (q, 0)$: a section of $T^{\ast}M$ whose coefficient functions in every chart, $q \mapsto 0(\partial/\partial x^j|_q) = 0$, are constant, hence smooth, so $\zeta$ is smooth by Proposition [[§51 One-Forms#^prop-51-1|§51.1]](3). By Proposition [[§51 One-Forms#^prop-51-1|§51.1]](2), with $\theta = \zeta$ and all $\theta_j = 0$, its coordinate representation in the charts $(U, \varphi)$ and $(T^{\ast}U, \hat\varphi)$ is
>
> $$
> \hat\varphi \circ \zeta \circ \varphi^{-1}(r) = (r, 0, \ldots, 0), \qquad r \in \varphi(U) .
> $$
>
> Its Jacobian is the $2m \times m$ matrix $\binom{I_m}{0}$: the first $m$ components are $r^k$, with $\partial r^k/\partial r^i = \delta^k_i$, and the last $m$ are the constant $0$. Written out, the first $m$ rows forming $I_m$ and the last $m$ rows zero,
>
> $$
> \begin{pmatrix} I_m \\ 0 \end{pmatrix}
> =
> \begin{pmatrix}
> 1 & \cdots & 0 \\
> \vdots & \ddots & \vdots \\
> 0 & \cdots & 1 \\
> 0 & \cdots & 0 \\
> \vdots & & \vdots \\
> 0 & \cdots & 0
> \end{pmatrix} .
> $$
> By Theorem [[§30 The Differential in Coordinates#^thm-30-2|§30.2]], applied to $\zeta$ with the source chart $\varphi$ and the target chart $\hat\varphi$, whose $2m$ coordinate functions are $\bar x^1, \ldots, \bar x^m, \xi_1, \ldots, \xi_m$, the $i$-th column of this matrix gives
>
> $$
> \zeta_{\ast p}\Big(\frac{\partial}{\partial x^i}\Big|_p\Big) = \sum_{k=1}^m \delta^k_i\, \frac{\partial}{\partial \bar x^k}\Big|_{(p,0)} + \sum_{j=1}^m 0 \cdot \frac{\partial}{\partial \xi_j}\Big|_{(p,0)} = \frac{\partial}{\partial \bar x^i}\Big|_{(p,0)} .
> $$
>
> *(3)* By (1), $\hat\varphi$ is an adapted chart at $(p, 0)$ whose first $2m - m = m$ coordinate functions are $\bar x^1, \ldots, \bar x^m$. Proposition [[§37 Regular Submanifolds#^prop-37-6|§37.6]], applied to $\mathcal{Z} \subseteq T^{\ast}M$ with this chart, gives $\iota_\ast(T_{(p,0)}\mathcal{Z}) = \operatorname{Span}\{\partial/\partial \bar x^1|_{(p,0)}, \ldots, \partial/\partial \bar x^m|_{(p,0)}\}$. By (2), the linear map $\zeta_{\ast p}$ carries the basis $\partial/\partial x^i|_p$ of $T_pM$ (Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]]) to these $m$ vectors; the image of a linear map is spanned by the images of a basis, so $\zeta_{\ast p}(T_pM)$ is the same span.

^pf-52-5

*Uses:* [[§50 The Cotangent Bundle#^cor-50-3|§50.3]], [[§33 Covectors in Coordinates#^cor-33-2|§33.2]], [[§33 Covectors in Coordinates#^lem-33-1|§33.1]], [[§37 Regular Submanifolds#^def-37-3|Def. §37.3]], [[§37 Regular Submanifolds#^def-37-2|Def. §37.2]], [[§51 One-Forms#^prop-51-1|§51.1]], [[§30 The Differential in Coordinates#^thm-30-2|§30.2]], [[§37 Regular Submanifolds#^prop-37-6|§37.6]], [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]]

The zero section is the first of a family of submanifolds of $T^{\ast}M$, one for each regular submanifold $S$ of $M$: put all the conormal spaces of $S$ together, as the cotangent spaces are put together in $T^{\ast}M$. *(Not from the assignment; the conormal spaces are those of [[§37 Regular Submanifolds|§37]], see the remark *The Conormal Bundle* there.)*

> [!definition] Definition §52.6: Conormal Bundle
> Let $S \subseteq M$ be a regular submanifold. The **conormal bundle** of $S$ is the subset
>
> $$
> N^{\ast}S = \{\, (p, \alpha) \in T^{\ast}M : p \in S,\ \alpha \in N_pS \,\}
> $$
>
> of $T^{\ast}M$: the conormal spaces $N_pS$ (Definition [[§37 Regular Submanifolds#^def-37-4|§37.4]]), $p \in S$, put together, as the cotangent spaces are put together in $T^{\ast}M$ (Definition [[§50 The Cotangent Bundle#^def-50-1|§50.1]]).

^def-52-6

> [!theorem] Proposition §52.6: The Conormal Bundle Is a Regular Submanifold
> Let $S \subseteq M$ be a regular submanifold of codimension $k$, $(U, \varphi = (x^1, \ldots, x^m))$ a smooth chart of $M$ adapted to $S$ (Definition [[§37 Regular Submanifolds#^def-37-3|§37.3]]), and $(\bar x^i, \xi_j)$ the standard coordinates on $T^{\ast}U$.
>
> 1. In the chart $(T^{\ast}U, \hat\varphi)$,
>
> $$
> N^{\ast}S \cap T^{\ast}U = \{\, (q, \alpha) \in T^{\ast}U : \bar x^{m-k+1} = \cdots = \bar x^m = 0 \ \text{ and } \ \xi_1 = \cdots = \xi_{m-k} = 0 \ \text{ at } (q, \alpha) \,\} :
> $$
>
> $k + (m - k) = m$ of the $2m$ coordinates of $\hat\varphi$ are set equal to $0$.
> 2. $N^{\ast}S$ is a regular submanifold of $T^{\ast}M$ of codimension $m$, hence of dimension $2m - m = m$, whatever $k$ is. The standard chart $\hat\varphi$ over an adapted chart, with its coordinates reordered so that these $m$ come last, is adapted to $N^{\ast}S$.

^prop-52-6

> [!proof]+ Proof
> *(Not from the assignment; filled in.)*
>
> *(1)* Let $(q, \alpha) \in T^{\ast}U$, so $q \in U$. By Definition [[§52 Critical Points and the Hessian#^def-52-6|§52.6]], $(q, \alpha) \in N^{\ast}S$ if and only if $q \in S$ and $\alpha \in N_qS$; we translate both conditions into the coordinates of $\hat\varphi$. *The point.* The chart is adapted, so $q \in U \cap S$ if and only if $x^{m-k+1}(q) = \cdots = x^m(q) = 0$ (Definition [[§37 Regular Submanifolds#^def-37-3|§37.3]]); as $\bar x^i(q, \alpha) = x^i(q)$, this says $\bar x^{m-k+1} = \cdots = \bar x^m = 0$ at $(q, \alpha)$. *The covector.* For $q \in U \cap S$, the same chart is a chart adapted to $S$ at $q$, and Proposition [[§37 Regular Submanifolds#^prop-37-8|§37.8]](1) (the description of $N_qS$ in an adapted chart at $q$) gives: $\alpha \in N_qS$ if and only if its components $\alpha(\partial/\partial x^i|_q)$ vanish for $i \le m - k$. As $\xi_i(q, \alpha) = \alpha(\partial/\partial x^i|_q)$, this says $\xi_1 = \cdots = \xi_{m-k} = 0$ at $(q, \alpha)$. Together the two translations give the displayed description.
>
> *(2)* By Corollary [[§50 The Cotangent Bundle#^cor-50-3|§50.3]](1), $T^{\ast}M$ is a smooth manifold of dimension $2m$, and $(T^{\ast}U, \hat\varphi)$ is one of its smooth charts (Proposition [[§50 The Cotangent Bundle#^prop-50-2|§50.2]]). Let $(p, \alpha) \in N^{\ast}S$. Since $p \in S$, there is a chart $(U, \varphi)$ of $M$ at $p$ adapted to $S$ (Definition [[§37 Regular Submanifolds#^def-37-2|§37.2]]), and then $(p, \alpha) \in T^{\ast}U$. By (1), $N^{\ast}S \cap T^{\ast}U$ is cut out in the chart $\hat\varphi$ by setting $m$ of its $2m$ coordinates equal to the constant $0$. Proposition [[§37 Regular Submanifolds#^prop-37-2|§37.2]], applied to the subset $N^{\ast}S$ of the manifold $T^{\ast}M$ with this chart (any $m$ of the coordinates, (2) there; the constants all $0$), gives a chart with the same domain $T^{\ast}U$ adapted to $N^{\ast}S$, of codimension $m$: $\hat\varphi$ with its coordinates permuted so that the $m$ vanishing ones come last. So every point of $N^{\ast}S$ lies in the domain of a chart of $T^{\ast}M$ adapted to $N^{\ast}S$, and $N^{\ast}S$ is a regular submanifold of $T^{\ast}M$ of codimension $m$ (Definition [[§37 Regular Submanifolds#^def-37-2|§37.2]]), of dimension $2m - m = m$ (Proposition [[§37 Regular Submanifolds#^prop-37-3|§37.3]]).

^pf-52-6

*Uses:* [[§52 Critical Points and the Hessian#^def-52-6|Def. §52.6]], [[§37 Regular Submanifolds#^def-37-3|Def. §37.3]], [[§37 Regular Submanifolds#^prop-37-8|§37.8]], [[§50 The Cotangent Bundle#^cor-50-3|§50.3]], [[§50 The Cotangent Bundle#^prop-50-1|§50.1]], [[§37 Regular Submanifolds#^def-37-2|Def. §37.2]], [[§37 Regular Submanifolds#^prop-37-2|§37.2]], [[§37 Regular Submanifolds#^prop-37-3|§37.3]], [[§50 The Cotangent Bundle#^prop-50-2|§50.2]]

> [!remark] Remark: Extreme Cases of the Conormal Bundle
> *(Not from the assignment.)* The dimension of $N^{\ast}S$ is $m$ whatever the codimension $k$ of $S$ is. The two extreme values of $k$:
>
> 1. $S = M$ (codimension $0$, Proposition [[§37 Regular Submanifolds#^prop-37-4|§37.4]]): $N_pM = 0$, since a covector vanishing on all of $T_pM$ is zero, and $N^{\ast}M = \mathcal{Z}$ is the zero section, cut out by $\xi_1 = \cdots = \xi_m = 0$ (Proposition [[§52 Critical Points and the Hessian#^prop-52-5|§52.5]](1));
> 2. $S = \{p\}$ (codimension $m$): $T_p\{p\} = 0$, so $N_p\{p\} = T_p^{\ast}M$, and $N^{\ast}\{p\} = \pi^{-1}(p)$ is the fibre over $p$, cut out by $\bar x^1 = \cdots = \bar x^m = 0$ in a chart with $\varphi(p) = 0$.
>
> In the language of symplectic geometry, not developed in these notes, $N^{\ast}S$ is a Lagrangian submanifold of $T^{\ast}M$ — the cotangent side where, in Uribe's words in the remark *No Normal Vectors Without a Metric*, Hamiltonian mechanics takes place.

^rem-52-2

> [!theorem] Corollary §52.7: Critical Points of a Restriction and the Conormal Bundle
> Let $S \subseteq M$ be a regular submanifold, $\Phi : M \to \mathbb{R}$ smooth, and $s_\Phi : M \to T^{\ast}M$, $s_\Phi(p) = (p, d\Phi_p)$, the one-form $d\Phi$ (Proposition [[§51 One-Forms#^prop-51-2|§51.2]]) regarded as a map. Then
>
> $$
> \operatorname{Crit}\big(\Phi|_S\big) = s_\Phi^{-1}\big(N^{\ast}S\big) :
> $$
>
> the critical points of the restriction are where the graph of $d\Phi$ meets the conormal bundle.

^cor-52-7

> [!proof]+ Proof
> *(Not from the assignment; filled in.)* Both sides are subsets of $S$: the left side because $\Phi|_S$ is a function on $S$ (Definition [[§36 Submersions#^def-36-5|§36.5]]), the right side because $s_\Phi(p) = (p, d\Phi_p) \in N^{\ast}S$ forces $p \in S$ (Definition [[§52 Critical Points and the Hessian#^def-52-6|§52.6]]). For $p \in S$, Definition [[§52 Critical Points and the Hessian#^def-52-6|§52.6]] gives
>
> $$
> p \in s_\Phi^{-1}\big(N^{\ast}S\big) \iff (p, d\Phi_p) \in N^{\ast}S \iff d\Phi_p \in N_pS ,
> $$
>
> and Proposition [[§37 Regular Submanifolds#^prop-37-18|§37.18]](3), applied to $\Phi$ and $f = \Phi|_S$, says that $d\Phi_p \in N_pS$ if and only if $p$ is a critical point of $\Phi|_S$, that is, $p \in \operatorname{Crit}(\Phi|_S)$.

^pf-52-7

*Uses:* [[§36 Submersions#^def-36-5|Def. §36.5]], [[§52 Critical Points and the Hessian#^def-52-6|Def. §52.6]], [[§37 Regular Submanifolds#^prop-37-18|§37.18]]

> [!remark] Remark: Critical Points and Lagrange Multipliers in the Conormal Bundle
> *(Not from the assignment.)* For $S = M$ the conormal bundle is the zero section (the remark *Extreme Cases of the Conormal Bundle*), and Corollary [[§52 Critical Points and the Hessian#^cor-52-7|§52.7]] reads $\operatorname{Crit}(\Phi) = s_\Phi^{-1}(\mathcal{Z})$: this is the starting point of the next subsection, Proposition [[§52 Critical Points and the Hessian#^prop-52-10|§52.10]](1) later in this section, where $s_\Phi$ is transverse to the zero section exactly when $\Phi$ is a Morse function (Theorem [[§52 Critical Points and the Hessian#^thm-52-11|§52.11]]). *Lagrange multipliers.* For $S = G^{-1}(0)$, each fibre $N_pS$ has the basis $dG^1|_p, \ldots, dG^k|_p$ (Proposition [[§37 Regular Submanifolds#^prop-37-19|§37.19]]), so $(p, \lambda) \mapsto \big(p, \sum_j \lambda_j\, dG^j|_p\big)$ is a bijection $S \times \mathbb{R}^k \to N^{\ast}S$; at a critical point $p$, the multipliers $\lambda_1, \ldots, \lambda_k$ of Theorem [[§37 Regular Submanifolds#^thm-37-20|§37.20]] are the coordinates of the point $(p, d\Phi_p) \in N^{\ast}S$ in its fibre, in this basis.

^rem-52-3

> [!theorem] Lemma §52.8: The Fibre Inclusion of $T^{\ast}M$
> Let $p \in M$, give $T_p^{\ast}M$ its standard smooth structure (Definition [[§22 The Differential of a Map Between Vector Spaces#^def-22-4|§22.4]]), and let $(U, \varphi = (x^1, \ldots, x^m))$ be a chart at $p$. Then $L_p : T_p^{\ast}M \to \mathbb{R}^m$, $L_p(\eta) = (\eta_1, \ldots, \eta_m)$ with $\eta_j = \eta\big(\partial/\partial x^j|_p\big)$, is a smooth chart of $T_p^{\ast}M$, and the fibre inclusion
>
> $$
> \iota_p : T_p^{\ast}M \longrightarrow T^{\ast}M, \qquad \iota_p(\eta) = (p, \eta),
> $$
>
> is smooth; in the charts $L_p$ and $\hat\varphi$ it is $b \mapsto (\varphi(p), b)$.

^lem-52-8

> [!proof]+ Proof
> *(Not from lecture; filled in.)* Let $L_p : T_p^{\ast}M \to \mathbb{R}^m$, $L_p(\eta) = (\eta_1, \ldots, \eta_m)$, be the map to components. It is linear, since covectors are evaluated pointwise (Definition [[§21 Linear Algebra Toolkit#^def-21-1|§21.1]]), and bijective, with inverse $b \mapsto \sum_j b_j\, dx^j|_p$ (Corollary [[§33 Covectors in Coordinates#^cor-33-2|§33.2]]); so it is a linear coordinate system (Definition [[§22 The Differential of a Map Between Vector Spaces#^def-22-1|§22.1]]), hence a smooth chart of $T_p^{\ast}M$ (Definition [[§22 The Differential of a Map Between Vector Spaces#^def-22-4|§22.4]]). The image of $\iota_p$ lies in $T^{\ast}U$, and by the inverse formula of Definition [[§50 The Cotangent Bundle#^def-50-5|§50.5]] (the point $\varphi^{-1}(\varphi(p)) = p$ with the covector $\sum_j b_j\, dx^j|_p$),
>
> $$
> \hat\varphi \circ \iota_p \circ L_p^{-1}(b) = \hat\varphi\Big(p, \sum_{j=1}^m b_j\, dx^j\big|_p\Big) = \big(\varphi(p), b\big), \qquad b \in \mathbb{R}^m ,
> $$
>
> a smooth map (constant first components, identity last components). And $\iota_p = \hat\varphi^{-1} \circ (\hat\varphi \circ \iota_p \circ L_p^{-1}) \circ L_p$ is continuous, a composite of continuous maps ($\hat\varphi$ is a homeomorphism, Proposition [[§50 The Cotangent Bundle#^prop-50-2|§50.2]]). So $\iota_p$ is smooth (Definition [[§19 Smooth Functions and Smooth Maps#^def-19-3|§19.3]], with the charts $L_p$ and $\hat\varphi$).

^pf-52-8

*Uses:* [[§21 Linear Algebra Toolkit#^def-21-1|Def. §21.1]], [[§33 Covectors in Coordinates#^cor-33-2|§33.2]], [[§22 The Differential of a Map Between Vector Spaces#^def-22-1|Def. §22.1]], [[§22 The Differential of a Map Between Vector Spaces#^def-22-4|Def. §22.4]], [[§50 The Cotangent Bundle#^def-50-5|Def. §50.5]], [[§50 The Cotangent Bundle#^prop-50-2|§50.2]], [[§19 Smooth Functions and Smooth Maps#^def-19-3|Def. §19.3]]

> [!theorem] Proposition §52.9: The Vertical Space of $T^*M$ Along the Zero Section
> Let $p \in M$, $(U, \varphi)$ a chart at $p$, and $(\bar x^i, \xi_j)$ the standard coordinates on $T^{\ast}U$.
>
> 1. $\pi_{\ast(p,0)}\big(\partial/\partial \bar x^i|_{(p,0)}\big) = \partial/\partial x^i|_p$ and $\pi_{\ast(p,0)}\big(\partial/\partial \xi_j|_{(p,0)}\big) = 0$. Hence the vertical space (Definition [[§38 Fibrations#^def-38-5|§38.5]]) is
>
> $$
> V_{(p,0)} = \ker \pi_{\ast(p,0)} = \operatorname{Span}\Big\{ \frac{\partial}{\partial \xi_1}\Big|_{(p,0)}, \ldots, \frac{\partial}{\partial \xi_m}\Big|_{(p,0)} \Big\}, \qquad \dim V_{(p,0)} = m .
> $$
>
> 2. Give $T_p^{\ast}M$ its standard smooth structure (Definition [[§22 The Differential of a Map Between Vector Spaces#^def-22-4|§22.4]]). The fibre inclusion $\iota_p : T_p^{\ast}M \to T^{\ast}M$, $\iota_p(\eta) = (p, \eta)$, is smooth, and the map
>
> $$
> j_p : T_p^{\ast}M \longrightarrow T_{(p,0)}(T^{\ast}M), \qquad j_p(\eta) = (\iota_p)_{\ast0}\big(D_\eta|_0\big),
> $$
>
> where $D_\eta|_0 \in T_0(T_p^{\ast}M)$ is the directional derivative of Corollary [[§30 The Differential in Coordinates#^cor-30-6|§30.6]], is a linear isomorphism of $T_p^{\ast}M$ onto $V_{(p,0)}$, given in coordinates by
>
> $$
> j_p(\eta) = \sum_{j=1}^m \eta_j\, \frac{\partial}{\partial \xi_j}\Big|_{(p,0)}, \qquad \eta_j = \eta\Big(\frac{\partial}{\partial x^j}\Big|_p\Big) .
> $$
>
> 3. $T_{(p,0)}(T^{\ast}M) = T_{(p,0)}\mathcal{Z} \oplus V_{(p,0)}$: every $w \in T_{(p,0)}(T^{\ast}M)$ is uniquely
>
> $$
> w = w^{\mathrm{hor}} + j_p\big(w^{\mathrm{ver}}\big), \qquad w^{\mathrm{hor}} \in T_{(p,0)}\mathcal{Z}, \quad w^{\mathrm{ver}} \in T_p^{\ast}M ;
> $$
>
> $w^{\mathrm{ver}}$ is the **vertical part** of $w$. In coordinates, if $w = \sum_i a^i\, \partial/\partial \bar x^i|_{(p,0)} + \sum_j b_j\, \partial/\partial \xi_j|_{(p,0)}$, then $w^{\mathrm{hor}} = \sum_i a^i\, \partial/\partial \bar x^i|_{(p,0)}$ and $w^{\mathrm{ver}} = \sum_j b_j\, dx^j|_p$.
>
> The space $V_{(p,0)}$, the map $j_p$ and the splitting are defined without charts; the coordinates only compute them. So, canonically, $T_{(p,0)}(T^{\ast}M) \cong T_{(p,0)}\mathcal{Z} \oplus T_p^{\ast}M$.

^prop-52-9

> [!proof]+ Proof
> *(Not from lecture; filled in. The submitted solution uses the basis $\partial/\partial \bar x^i, \partial/\partial \xi_j$ directly; this proposition says what the two halves of the basis span.)*
>
> *(1)* By Corollary [[§50 The Cotangent Bundle#^cor-50-3|§50.3]](1), $\pi$ is smooth and its coordinate representation in the charts $\hat\varphi$ and $\varphi$ is $(r, b) \mapsto r$, with Jacobian the $m \times 2m$ matrix $(I_m \mid 0)$: the $k$-th component $r^k$ has partial derivative $\delta^k_i$ with respect to the $i$-th of the first $m$ variables and $0$ with respect to each of the last $m$. Written out, the first $m$ columns forming $I_m$ and the last $m$ columns zero,
>
> $$
> \left(\begin{array}{c|c} I_m & 0 \end{array}\right)
> =
> \left(\begin{array}{ccc|ccc}
> 1 & \cdots & 0 & 0 & \cdots & 0 \\
> \vdots & \ddots & \vdots & \vdots & & \vdots \\
> 0 & \cdots & 1 & 0 & \cdots & 0
> \end{array}\right) .
> $$
>
> By Theorem [[§30 The Differential in Coordinates#^thm-30-2|§30.2]], applied to $\pi$ with the source chart $\hat\varphi$ (coordinates $\bar x^1, \ldots, \xi_m$) and the target chart $\varphi$, with $\pi(T^{\ast}U) \subseteq U$, the columns of this matrix give
>
> $$
> \pi_{\ast(p,0)}\Big(\frac{\partial}{\partial \bar x^i}\Big|_{(p,0)}\Big) = \sum_{k=1}^m \delta^k_i\, \frac{\partial}{\partial x^k}\Big|_p = \frac{\partial}{\partial x^i}\Big|_p, \qquad \pi_{\ast(p,0)}\Big(\frac{\partial}{\partial \xi_j}\Big|_{(p,0)}\Big) = \sum_{k=1}^m 0 \cdot \frac{\partial}{\partial x^k}\Big|_p = 0 .
> $$
>
> Now let $w = \sum_i a^i\, \partial/\partial \bar x^i|_{(p,0)} + \sum_j b_j\, \partial/\partial \xi_j|_{(p,0)}$ be any tangent vector at $(p, 0)$. By linearity, $\pi_{\ast(p,0)}w = \sum_i a^i\, \partial/\partial x^i|_p$, which is $0$ exactly when all $a^i = 0$, the $\partial/\partial x^i|_p$ being a basis (Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]]). So $\ker \pi_{\ast(p,0)}$ consists of the combinations of the $\partial/\partial \xi_j|_{(p,0)}$ alone; these $m$ vectors are part of a basis, hence independent, and $\dim V_{(p,0)} = m$.
>
> *(2) $\iota_p$ is smooth* by Lemma [[§52 Critical Points and the Hessian#^lem-52-8|§52.8]], which also gives the chart $L_p(\eta) = (\eta_1, \ldots, \eta_m)$ of $T_p^{\ast}M$ used below.
>
> *(2) The formula for $j_p$.* Let $\eta \in T_p^{\ast}M$ and $E = j_p(\eta)$, a derivation at $\iota_p(0) = (p, 0)$. By the universal formula (Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]]) in the chart $\hat\varphi$, $E = \sum_i E[\bar x^i]\, \partial/\partial \bar x^i|_{(p,0)} + \sum_j E[\xi_j]\, \partial/\partial \xi_j|_{(p,0)}$, so it suffices to compute the values of $E$ on the coordinate functions. For a function $g$ smooth near $(p, 0)$, the definition of the pushforward (Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-6|§28.6]]) and of $D_\eta|_0$ (Corollary [[§30 The Differential in Coordinates#^cor-30-6|§30.6]]) give
>
> $$
> E[g] = D_\eta|_0\big[g \circ \iota_p\big] = \frac{d}{dt}\Big|_{t=0}\, g\big(\iota_p(t\eta)\big) = \frac{d}{dt}\Big|_{t=0}\, g(p, t\eta) .
> $$
>
> For $g = \bar x^i$: $\bar x^i(p, t\eta) = x^i(p)$ does not depend on $t$, so $E[\bar x^i] = 0$. For $g = \xi_j$: $\xi_j(p, t\eta) = (t\eta)(\partial/\partial x^j|_p) = t\,\eta_j$, since covectors are scaled pointwise, so $E[\xi_j] = \eta_j$. Hence $j_p(\eta) = \sum_j \eta_j\, \partial/\partial \xi_j|_{(p,0)}$.
>
> *(2) $j_p$ is an isomorphism onto $V_{(p,0)}$.* $j_p$ is linear, as the composite of the linear map $\eta \mapsto D_\eta|_0$ (Corollary [[§30 The Differential in Coordinates#^cor-30-6|§30.6]]) and the linear map $(\iota_p)_{\ast0}$ (Theorem [[§30 The Differential in Coordinates#^thm-30-2|§30.2]]). By the formula, $j_p$ is $L_p$ followed by the map $b \mapsto \sum_j b_j\, \partial/\partial \xi_j|_{(p,0)}$, which is a bijection of $\mathbb{R}^m$ onto $V_{(p,0)}$ because, by (1), the $\partial/\partial \xi_j|_{(p,0)}$ are a basis of $V_{(p,0)}$; and $L_p$ is bijective. So $j_p$ is a linear bijection of $T_p^{\ast}M$ onto $V_{(p,0)}$. (Without coordinates, the image lies in $V_{(p,0)}$ because $\pi \circ \iota_p$ is the constant map to $p$: Lemma [[§28 Derivations and the Abstract Tangent Space#^lem-28-10|§28.10]], applied with $F = \pi$ and $\iota = \iota_p$ at the point $0 \in T_p^{\ast}M$, gives $\pi_{\ast(p,0)} \circ (\iota_p)_{\ast0} = (\pi \circ \iota_p)_{\ast0} = 0$.)
>
> *(3)* $\pi : T^{\ast}M \to M$ is smooth (Corollary [[§50 The Cotangent Bundle#^cor-50-3|§50.3]](1)) and $\zeta$ is a smooth map with $\pi \circ \zeta = \mathrm{id}_M$ (Proposition [[§52 Critical Points and the Hessian#^prop-52-5|§52.5]](2)). Proposition [[§38 Fibrations#^prop-38-5|§38.5]], applied with $E = T^{\ast}M$ and $s = \zeta$ at $\zeta(p) = (p, 0)$, gives
>
> $$
> T_{(p,0)}(T^{\ast}M) = \zeta_{\ast p}(T_pM) \oplus V_{(p,0)} = T_{(p,0)}\mathcal{Z} \oplus j_p(T_p^{\ast}M),
> $$
>
> the second form by Proposition [[§52 Critical Points and the Hessian#^prop-52-5|§52.5]](3) and (2) above. So every $w$ is uniquely $w^{\mathrm{hor}} + u$ with $w^{\mathrm{hor}} \in T_{(p,0)}\mathcal{Z}$ and $u \in V_{(p,0)}$, and $u = j_p(w^{\mathrm{ver}})$ for a unique $w^{\mathrm{ver}} \in T_p^{\ast}M$, since $j_p$ is a bijection onto $V_{(p,0)}$. (In coordinates the direct sum is also visible directly: the two spans are those of the two halves of a basis.) For the coordinate formula, let $w = \sum_i a^i\, \partial/\partial \bar x^i|_{(p,0)} + \sum_j b_j\, \partial/\partial \xi_j|_{(p,0)}$ and $\eta = \sum_j b_j\, dx^j|_p$, whose components are $\eta_j = b_j$ (Corollary [[§33 Covectors in Coordinates#^cor-33-2|§33.2]]). By (2), $j_p(\eta) = \sum_j b_j\, \partial/\partial \xi_j|_{(p,0)}$, so
>
> $$
> w = \Big(\sum_{i=1}^m a^i\, \frac{\partial}{\partial \bar x^i}\Big|_{(p,0)}\Big) + j_p(\eta),
> $$
>
> with the first summand in $T_{(p,0)}\mathcal{Z}$ by Proposition [[§52 Critical Points and the Hessian#^prop-52-5|§52.5]](3). By uniqueness of the decomposition, $w^{\mathrm{hor}} = \sum_i a^i\, \partial/\partial \bar x^i|_{(p,0)}$ and $w^{\mathrm{ver}} = \eta$. Finally, $\pi$, $\zeta$, $\iota_p$ and $D_\eta|_0$ are all defined without charts, hence so are $V_{(p,0)} = \ker \pi_{\ast(p,0)}$, $T_{(p,0)}\mathcal{Z} = \zeta_{\ast p}(T_pM)$, $j_p$ and the decomposition.

^pf-52-9

*Uses:* [[§50 The Cotangent Bundle#^cor-50-3|§50.3]], [[§30 The Differential in Coordinates#^thm-30-2|§30.2]], [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]], [[§21 Linear Algebra Toolkit#^def-21-1|Def. §21.1]], [[§33 Covectors in Coordinates#^cor-33-2|§33.2]], [[§22 The Differential of a Map Between Vector Spaces#^def-22-1|Def. §22.1]], [[§22 The Differential of a Map Between Vector Spaces#^def-22-4|Def. §22.4]], [[§50 The Cotangent Bundle#^def-50-5|Def. §50.5]], [[§50 The Cotangent Bundle#^prop-50-2|§50.2]], [[§19 Smooth Functions and Smooth Maps#^def-19-3|Def. §19.3]], [[§28 Derivations and the Abstract Tangent Space#^def-28-6|Def. §28.6]], [[§30 The Differential in Coordinates#^cor-30-6|§30.6]], [[§28 Derivations and the Abstract Tangent Space#^lem-28-10|§28.10]], [[§52 Critical Points and the Hessian#^prop-52-5|§52.5]], [[§38 Fibrations#^prop-38-5|§38.5]], [[§52 Critical Points and the Hessian#^lem-52-8|§52.8]]

## The Differential of $df$ and Transversality

> [!theorem] Proposition §52.10: The Differential of $df$ at a Critical Point
> Let $s_f : M \to T^{\ast}M$, $s_f(p) = (p, df_p)$, be the one-form $df$ regarded as a map.
>
> 1. $s_f$ is a smooth section of $\pi : T^{\ast}M \to M$, and $s_f^{-1}(\mathcal{Z}) = \operatorname{Crit}(f)$.
> 2. In a chart $(U, \varphi = (x^i))$ and the standard coordinates on $T^{\ast}U$, for every $q \in U$,
>
> $$
> (s_f)_{\ast q}\Big(\frac{\partial}{\partial x^i}\Big|_q\Big) = \frac{\partial}{\partial \bar x^i}\Big|_{s_f(q)} + \sum_{j=1}^m H_{ij}(q)\, \frac{\partial}{\partial \xi_j}\Big|_{s_f(q)} ;
> $$
>
> the matrix of $(s_f)_{\ast q}$ in the coordinate bases is the $2m \times m$ matrix $\binom{I_m}{H_q}$.
> Written out, with rows indexed by $\bar x^1, \ldots, \bar x^m, \xi_1, \ldots, \xi_m$ and columns by $\partial/\partial x^1|_q, \ldots, \partial/\partial x^m|_q$,
>
> $$
> \left(\begin{array}{c} I_m \\ \hline H_q \end{array}\right)
> =
> \left(\begin{array}{ccc}
> 1 & \cdots & 0 \\
> \vdots & \ddots & \vdots \\
> 0 & \cdots & 1 \\ \hline
> H_{11}(q) & \cdots & H_{1m}(q) \\
> \vdots & \ddots & \vdots \\
> H_{m1}(q) & \cdots & H_{mm}(q)
> \end{array}\right) .
> $$
> 3. If $p \in \operatorname{Crit}(f)$, then $s_f(p) = (p, 0)$, and for $v \in T_pM$, in the splitting of Proposition [[§52 Critical Points and the Hessian#^prop-52-9|§52.9]](3),
>
> $$
> (s_f)_{\ast p}v = \zeta_{\ast p}v + j_p\big(\operatorname{Hess}_p f(v, \cdot\,)\big):
> $$
>
> the vertical part of $(s_f)_{\ast p}v$ is $\operatorname{Hess}_p f(v, \cdot\,) = (\operatorname{Hess}_p f)^\flat(v) \in T_p^{\ast}M$.

^prop-52-10

> [!proof]+ Proof
> *(Assignment 5, Problem 3: the submitted solution's computation of $w_i = (s_f)_{\ast p}(\partial/\partial x^i|_p)$, written out; (3) is filled in.)*
>
> *(1)* By Proposition [[§51 One-Forms#^prop-51-2|§51.2]], $df$ is a one-form, that is (Definition [[§51 One-Forms#^def-51-1|§51.1]]), a smooth map $M \to T^{\ast}M$ with $\pi \circ df = \mathrm{id}_M$; this map is $s_f$. A point $p$ lies in $s_f^{-1}(\mathcal{Z})$ exactly when $(p, df_p) = (p, 0)$, i.e. $df_p = 0$, i.e. $p \in \operatorname{Crit}(f)$.
>
> *(2)* By Proposition [[§51 One-Forms#^prop-51-1|§51.1]](2), with $\theta = df$, whose coefficient functions are $\partial f/\partial x^j$ (Proposition [[§52 Critical Points and the Hessian#^prop-52-1|§52.1]](1)), the coordinate representation of $s_f$ in the charts $\varphi$ and $\hat\varphi$ is
>
> $$
> \hat\varphi \circ s_f \circ \varphi^{-1}(r) = \Big(r,\ \frac{\partial f}{\partial x^1}\big(\varphi^{-1}(r)\big), \ldots, \frac{\partial f}{\partial x^m}\big(\varphi^{-1}(r)\big)\Big) = \big(r, \Phi(r)\big), \qquad r \in \varphi(U),
> $$
>
> with $\Phi$ the map of Proposition [[§52 Critical Points and the Hessian#^prop-52-1|§52.1]](3). Its Jacobian at $\varphi(q)$ has as top $m \times m$ block the Jacobian of $r \mapsto r$, the identity, and as bottom block $\Phi'(\varphi(q)) = H_q$ (Proposition [[§52 Critical Points and the Hessian#^prop-52-1|§52.1]](3), at the point $q$); its entry in row $m + j$ and column $i$ is therefore $H_{ji}(q) = H_{ij}(q)$. By Theorem [[§30 The Differential in Coordinates#^thm-30-2|§30.2]], applied to $s_f$ with the source chart $\varphi$ and the target chart $\hat\varphi$ (admissible, as $s_f(U) \subseteq T^{\ast}U$), with coordinate functions $\bar x^1, \ldots, \bar x^m, \xi_1, \ldots, \xi_m$, this is the matrix of $(s_f)_{\ast q}$, and its $i$-th column gives
>
> $$
> (s_f)_{\ast q}\Big(\frac{\partial}{\partial x^i}\Big|_q\Big) = \sum_{k=1}^m \delta^k_i\, \frac{\partial}{\partial \bar x^k}\Big|_{s_f(q)} + \sum_{j=1}^m H_{ij}(q)\, \frac{\partial}{\partial \xi_j}\Big|_{s_f(q)} = \frac{\partial}{\partial \bar x^i}\Big|_{s_f(q)} + \sum_{j=1}^m H_{ij}(q)\, \frac{\partial}{\partial \xi_j}\Big|_{s_f(q)} .
> $$
>
> (This is the submitted computation: $\bar x^k \circ s_f = x^k$ and $\xi_j \circ s_f = \partial f/\partial x^j$, whose $x^i$-partials at $q$ are $\delta^k_i$ and $H_{ij}(q)$.)
>
> *(3)* $s_f(p) = (p, df_p) = (p, 0)$ since $p$ is critical. Write $v = \sum_i v^i\, \partial/\partial x^i|_p$, $v^i = v[x^i]$ (Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]]). By linearity of $(s_f)_{\ast p}$ and (2) at $q = p$,
>
> $$
> (s_f)_{\ast p}v = \sum_{i=1}^m v^i\, \frac{\partial}{\partial \bar x^i}\Big|_{(p,0)} + \sum_{j=1}^m \Big(\sum_{i=1}^m H_{ij}(p)\, v^i\Big) \frac{\partial}{\partial \xi_j}\Big|_{(p,0)} .
> $$
>
> By the coordinate formula of Proposition [[§52 Critical Points and the Hessian#^prop-52-9|§52.9]](3), its horizontal part is $\sum_i v^i\, \partial/\partial \bar x^i|_{(p,0)}$, which is $\zeta_{\ast p}v$ by Proposition [[§52 Critical Points and the Hessian#^prop-52-5|§52.5]](2) and linearity, and its vertical part is the covector $\eta = \sum_j \big(\sum_i H_{ij}(p)\, v^i\big)\, dx^j|_p$, with components $\eta_j = \sum_i H_{ij}(p)\, v^i$ (Corollary [[§33 Covectors in Coordinates#^cor-33-2|§33.2]]). On the other hand, $\operatorname{Hess}_p f(v, \cdot\,) = (\operatorname{Hess}_p f)^\flat(v)$ (Definition [[§21 Linear Algebra Toolkit#^def-21-4|§21.4]]), and $(\operatorname{Hess}_p f)^\flat$ is linear with $(\operatorname{Hess}_p f)^\flat(\partial/\partial x^i|_p) = \sum_j H_{ij}(p)\, dx^j|_p$ (Proposition [[§52 Critical Points and the Hessian#^prop-52-4|§52.4]](1)); so
>
> $$
> \operatorname{Hess}_p f(v, \cdot\,) = \sum_{i=1}^m v^i\, (\operatorname{Hess}_p f)^\flat\Big(\frac{\partial}{\partial x^i}\Big|_p\Big) = \sum_{i=1}^m v^i \sum_{j=1}^m H_{ij}(p)\, dx^j\big|_p = \sum_{j=1}^m \Big(\sum_{i=1}^m H_{ij}(p)\, v^i\Big) dx^j\big|_p = \eta ,
> $$
>
> and the vertical part is $\eta = \operatorname{Hess}_p f(v, \cdot\,)$.

^pf-52-10

*Uses:* [[§51 One-Forms#^prop-51-2|§51.2]], [[§51 One-Forms#^def-51-1|Def. §51.1]], [[§51 One-Forms#^prop-51-1|§51.1]], [[§52 Critical Points and the Hessian#^prop-52-1|§52.1]], [[§30 The Differential in Coordinates#^thm-30-2|§30.2]], [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]], [[§52 Critical Points and the Hessian#^prop-52-9|§52.9]], [[§52 Critical Points and the Hessian#^prop-52-5|§52.5]], [[§33 Covectors in Coordinates#^cor-33-2|§33.2]], [[§21 Linear Algebra Toolkit#^def-21-4|Def. §21.4]], [[§52 Critical Points and the Hessian#^prop-52-4|§52.4]]

So along the zero section the differential of $df$ consists of two pieces: the horizontal piece is the differential of the zero section, the same for every $f$, and the vertical piece is the Hessian. This is what makes the next theorem work.

> [!theorem] Theorem §52.11: Transversality to the Zero Section
> Let $f : M \to \mathbb{R}$ be smooth. Then $s_f \pitchfork \mathcal{Z}$ (Definition [[§37 Regular Submanifolds#^def-37-5|§37.5]]) if and only if every critical point of $f$ is nondegenerate, that is, if and only if $f$ is a Morse function. More precisely, for $p \in \operatorname{Crit}(f)$,
>
> $$
> (s_f)_{\ast p}(T_pM) + T_{(p,0)}\mathcal{Z} = T_{(p,0)}(T^{\ast}M) \iff p \text{ is nondegenerate} .
> $$

^thm-52-11

> [!proof]+ Proof
> *(Assignment 5, Problem 3(a). This proof runs through the vectors of the submitted solution and the splitting of Proposition [[§52 Critical Points and the Hessian#^prop-52-9|§52.9]]; the submitted determinant follows as the second proof.)*
>
> *Reduction to one critical point.* By Proposition [[§52 Critical Points and the Hessian#^prop-52-5|§52.5]](1), $\mathcal{Z}$ is a regular submanifold of $T^{\ast}M$, and $s_f$ is smooth with $s_f^{-1}(\mathcal{Z}) = \operatorname{Crit}(f)$ (Proposition [[§52 Critical Points and the Hessian#^prop-52-10|§52.10]](1)), and $s_f(p) = (p, 0)$ for $p \in \operatorname{Crit}(f)$. By Definition [[§37 Regular Submanifolds#^def-37-5|§37.5]], $s_f \pitchfork \mathcal{Z}$ means that the displayed equality of subspaces of $T_{(p,0)}(T^{\ast}M)$ holds at every $p \in \operatorname{Crit}(f)$, with $T_{(p,0)}\mathcal{Z}$ standing for its image under the inclusion. So it suffices to prove the displayed equivalence for one $p \in \operatorname{Crit}(f)$. Fix it, a chart $(U, \varphi = (x^i))$ at $p$, and the standard coordinates on $T^{\ast}U$. Write $A = (s_f)_{\ast p}(T_pM) + T_{(p,0)}\mathcal{Z}$ and $T = T_{(p,0)}(T^{\ast}M)$.
>
> *The vectors.* Put
>
> $$
> z_i = \frac{\partial}{\partial \bar x^i}\Big|_{(p,0)}, \qquad w_i = (s_f)_{\ast p}\Big(\frac{\partial}{\partial x^i}\Big|_p\Big), \qquad u_i = w_i - z_i \qquad (i = 1, \ldots, m).
> $$
>
> The $z_i$ span $T_{(p,0)}\mathcal{Z}$ (Proposition [[§52 Critical Points and the Hessian#^prop-52-5|§52.5]](3)). The $w_i$ span $(s_f)_{\ast p}(T_pM)$, the images of the basis $\partial/\partial x^i|_p$ under a linear map. By Proposition [[§52 Critical Points and the Hessian#^prop-52-10|§52.10]](2) at $q = p$,
>
> $$
> u_i = w_i - z_i = \sum_{j=1}^m H_{ij}(p)\, \frac{\partial}{\partial \xi_j}\Big|_{(p,0)} \in V_{(p,0)} ,
> $$
>
> and by Proposition [[§52 Critical Points and the Hessian#^prop-52-10|§52.10]](3) with $v = \partial/\partial x^i|_p$ (whose image under $\zeta_{\ast p}$ is $z_i$), $u_i = j_p\big(\operatorname{Hess}_p f(\partial/\partial x^i|_p, \cdot\,)\big)$.
>
> *$A$ in terms of the $u_i$.* The sum of two subspaces is the span of the union of spanning sets, so $A = \operatorname{Span}\{w_1, \ldots, w_m, z_1, \ldots, z_m\}$. This equals $\operatorname{Span}\{u_1, \ldots, u_m, z_1, \ldots, z_m\}$: each $u_i = w_i - z_i$ lies in the first span, and each $w_i = u_i + z_i$ in the second. Hence
>
> $$
> A = T_{(p,0)}\mathcal{Z} + S_H, \qquad S_H = \operatorname{Span}\{u_1, \ldots, u_m\} \subseteq V_{(p,0)} .
> $$
>
> *$A = T$ if and only if $S_H = V_{(p,0)}$.* If $S_H = V_{(p,0)}$, then $A = T_{(p,0)}\mathcal{Z} + V_{(p,0)} = T$ by Proposition [[§52 Critical Points and the Hessian#^prop-52-9|§52.9]](3). Conversely, suppose $A = T$ and let $\nu \in V_{(p,0)}$. Then $\nu \in A$, so $\nu = z + u$ with $z \in T_{(p,0)}\mathcal{Z}$ and $u \in S_H \subseteq V_{(p,0)}$. Then $z = \nu - u \in V_{(p,0)}$, so $z \in T_{(p,0)}\mathcal{Z} \cap V_{(p,0)} = \{0\}$, the sum of Proposition [[§52 Critical Points and the Hessian#^prop-52-9|§52.9]](3) being direct. So $\nu = u \in S_H$, and $V_{(p,0)} \subseteq S_H$; the other inclusion holds by construction.
>
> *$S_H = V_{(p,0)}$ if and only if $p$ is nondegenerate.* Let $B = \operatorname{Hess}_p f$. Since $u_i = j_p\big(B^\flat(\partial/\partial x^i|_p)\big)$ and $j_p \circ B^\flat$ is linear, $S_H$ is the image of $j_p \circ B^\flat : T_pM \to V_{(p,0)}$ (the image of a linear map is spanned by the images of a basis). As $j_p : T_p^{\ast}M \to V_{(p,0)}$ is a bijection (Proposition [[§52 Critical Points and the Hessian#^prop-52-9|§52.9]](2)), $S_H = V_{(p,0)}$ if and only if $B^\flat : T_pM \to T_p^{\ast}M$ is onto. Both spaces have dimension $m$, so $B^\flat$ is onto if and only if it is bijective (Proposition [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]](1)), which holds if and only if $p$ is nondegenerate (Proposition [[§52 Critical Points and the Hessian#^prop-52-4|§52.4]](2), (a) $\Leftrightarrow$ (c)).
>
> Chaining the three equivalences, $A = T$ if and only if $p$ is nondegenerate. As $p \in \operatorname{Crit}(f)$ was arbitrary, $s_f \pitchfork \mathcal{Z}$ if and only if every critical point is nondegenerate, which is Definition [[§52 Critical Points and the Hessian#^def-52-4|§52.4]]. (If $\operatorname{Crit}(f) = \emptyset$, both sides hold vacuously.)

^pf-52-11

*Uses:* [[§52 Critical Points and the Hessian#^prop-52-9|§52.9]], [[§52 Critical Points and the Hessian#^prop-52-5|§52.5]], [[§52 Critical Points and the Hessian#^prop-52-10|§52.10]], [[§37 Regular Submanifolds#^def-37-5|Def. §37.5]], [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]], [[§52 Critical Points and the Hessian#^prop-52-4|§52.4]], [[§52 Critical Points and the Hessian#^def-52-4|Def. §52.4]]

> [!proof]+ Second proof (Assignment 5, Problem 3(a): the block determinant)
> *(The submitted solution.)* Fix $p \in \operatorname{Crit}(f)$, a chart $(U, \varphi)$ at $p$, and $z_i$, $w_i$ as in the first proof, so that $A = (s_f)_{\ast p}(T_pM) + T_{(p,0)}\mathcal{Z} = \operatorname{Span}\{w_1, \ldots, w_m, z_1, \ldots, z_m\}$. The space $T_{(p,0)}(T^{\ast}M)$ has dimension $2m$ (Corollary [[§50 The Cotangent Bundle#^cor-50-3|§50.3]](1) and Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]]); so $A$ is all of it if and only if these $2m$ vectors span it, if and only if they are linearly independent (Proposition [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]](1), applied to the linear map $\mathbb{R}^{2m} \to T_{(p,0)}(T^{\ast}M)$ sending the standard basis to the $2m$ vectors), if and only if the $2m \times 2m$ matrix $A_p$ whose columns are their coordinates in the basis $\partial/\partial \bar x^1, \ldots, \partial/\partial \bar x^m, \partial/\partial \xi_1, \ldots, \partial/\partial \xi_m$ at $(p, 0)$ is invertible. By Proposition [[§52 Critical Points and the Hessian#^prop-52-10|§52.10]](2), the column of $w_i$ has $e_i$ on top and $(H_{i1}(p), \ldots, H_{im}(p))^{\mathsf T}$ below, which is the $i$-th column of $H_p$ by symmetry (Proposition [[§52 Critical Points and the Hessian#^prop-52-1|§52.1]](2)); the column of $z_i$ has $e_i$ on top and $0$ below. So
>
> $$
> A_p = \begin{pmatrix} I_m & I_m \\ H_p & 0 \end{pmatrix}, \qquad \det A_p = \det I_m \cdot \det\big(0 - H_p\, I_m^{-1}\, I_m\big) = \det(-H_p) = (-1)^m \det H_p ,
> $$
>
> by the determinant formula for a block matrix $\begin{pmatrix} P & Q \\ R & S \end{pmatrix}$ with $P$ invertible, $\det P \cdot \det(S - R P^{-1} Q)$. Directly, by column operations: subtracting column $m + i$ from column $i$, for $i = 1, \ldots, m$, does not change the determinant and gives $\begin{pmatrix} 0 & I_m \\ H_p & 0 \end{pmatrix}$; moving each of the last $m$ columns past the first $m$ columns takes $m \cdot m$ exchanges of adjacent columns, each changing the sign, and gives $\begin{pmatrix} I_m & 0 \\ 0 & H_p \end{pmatrix}$, of determinant $\det H_p$; so $\det A_p = (-1)^{m^2} \det H_p = (-1)^m \det H_p$, as $m^2$ and $m$ have the same parity. Hence $A = T_{(p,0)}(T^{\ast}M)$ if and only if $\det H_p \neq 0$, if and only if $p$ is nondegenerate (Proposition [[§52 Critical Points and the Hessian#^prop-52-4|§52.4]](2), (a) $\Leftrightarrow$ (d)).
>
> *Some chart or every chart.* The problem asks for the Hessian to be non-degenerate “for every critical point $p$ and any chart.” The transversality condition at $p$ involves no chart, and the computation holds in whichever chart at $p$ was fixed; so if $s_f \pitchfork \mathcal{Z}$, then $\det H_p \neq 0$ in every chart at $p$, and conversely $\det H_p \neq 0$ in a single chart at $p$ already gives the transversality condition at $p$. (This is the chart-independence of $\det H_p \neq 0$, Proposition [[§52 Critical Points and the Hessian#^prop-52-4|§52.4]](2), (d) $\Leftrightarrow$ (e), found again.)

^pf-52-11-2

*Uses:* [[§50 The Cotangent Bundle#^cor-50-3|§50.3]], [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]], [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]], [[§52 Critical Points and the Hessian#^prop-52-10|§52.10]], [[§52 Critical Points and the Hessian#^prop-52-1|§52.1]], [[§52 Critical Points and the Hessian#^prop-52-4|§52.4]]

> [!remark]- Connections
> - The same picture for a restriction $\Phi|_S$: critical points are where the graph of $d\Phi$ meets the conormal bundle of $S$, the remark [[§37 Regular Submanifolds#^rem-37-5|The Conormal Bundle]] (§37); the zero section is the case $S = M$.

> [!example] Example §52.2: Transverse and Tangent: $x^2$ and $x^3$
> On $M = \mathbb{R}$, with the global chart $\mathrm{id}$ and coordinate $x$, and the standard coordinates $(\bar x, \xi)$ on $T^{\ast}\mathbb{R}$, the section $s_f$ is $x \mapsto (x, f'(x))$ in coordinates, its image is the graph $\{\xi = f'(\bar x)\}$, and $\mathcal{Z} = \{\xi = 0\}$.
>
> 1. $f = x^2$: $\operatorname{Crit}(f) = \{0\}$, $H(0) = f''(0) = 2 \neq 0$, and $s_f \pitchfork \mathcal{Z}$: the line $\xi = 2\bar x$ crosses $\xi = 0$ at an angle. $f$ is a Morse function.
> 2. $f = x^3$: $\operatorname{Crit}(f) = \{0\}$, $H(0) = f''(0) = 0$, and $s_f$ is not transverse to $\mathcal{Z}$: the parabola $\xi = 3\bar x^2$ is tangent to $\xi = 0$ at the origin. $f$ is not a Morse function.

^ex-52-2

> [!proof]+ Working out the example
> In the chart $\mathrm{id}$, $f_{\mathrm{id}} = f$, so $\partial f/\partial x = f'$ and $H(x) = f''(x)$ (Definition [[§52 Critical Points and the Hessian#^def-52-1|§52.1]]); the coordinate representation of $s_f$ is $x \mapsto (x, f'(x))$ (Proposition [[§51 One-Forms#^prop-51-1|§51.1]](2), with $\theta = df$, whose coefficient is $\partial f/\partial x = f'$), and $\operatorname{Crit}(f) = \{x : f'(x) = 0\}$ (Proposition [[§36 Submersions#^prop-36-2|§36.2]]). In the notation of the proof of Theorem [[§52 Critical Points and the Hessian#^thm-52-11|§52.11]], $z_1 = \partial/\partial \bar x|_{(0,0)}$ and $w_1 = \partial/\partial \bar x|_{(0,0)} + f''(0)\, \partial/\partial \xi|_{(0,0)}$ (Proposition [[§52 Critical Points and the Hessian#^prop-52-10|§52.10]](2)). (1) $f'(x) = 2x$ vanishes only at $0$, and $w_1 - z_1 = 2\, \partial/\partial \xi|_{(0,0)}$, so $z_1, w_1$ span the $2$-dimensional $T_{(0,0)}(T^{\ast}\mathbb{R})$. (2) $f'(x) = 3x^2$ vanishes only at $0$, $f''(0) = 0$, so $w_1 = z_1$ and $z_1, w_1$ span only a line: the transversality condition fails at the critical point $0$.

^pf-ex-52-2

*Uses:* [[§52 Critical Points and the Hessian#^def-52-1|Def. §52.1]], [[§51 One-Forms#^prop-51-1|§51.1]], [[§36 Submersions#^prop-36-2|§36.2]], [[§52 Critical Points and the Hessian#^thm-52-11|§52.11]], [[§52 Critical Points and the Hessian#^prop-52-10|§52.10]]

> [!remark] Remark: Review Session: Why the Hessian Needs a Critical Point
> *Review session, Oct 16, in answer to “is there a careful definition of the Hessian?” — “That's a beautiful question.”* The fact: for $f : M \to \mathbb{R}$, $\operatorname{Hess}_p f$ is only *intrinsically* defined if $df_p = 0$. If $df_p = 0$ it is a well-defined quadratic form, a symmetric bilinear form on $T_pM$ (Proposition [[§52 Critical Points and the Hessian#^prop-52-3|§52.3]]); if $df_p \neq 0$ it is not: “of course you can write everything in coordinates and take the Hessian in coordinates. But … when you change coordinates, the new Hessian would involve first derivatives of $f$. So it doesn't transform as a quadratic form” (Proposition [[§52 Critical Points and the Hessian#^prop-52-2|§52.2]], Example [[§52 Critical Points and the Hessian#^ex-52-1|§52.1]]).
>
> “And there's a beautiful geometric reason,” in $T^{\ast}M$. At a critical point $p$ the section $S_f = s_f(M)$ meets the zero section $\mathcal{Z}$ at $(p, 0)$, and along $\mathcal{Z}$ the tangent space of $T^{\ast}M$ splits canonically into the part tangent to $\mathcal{Z}$ and the vertical part, the tangent space to the fibre, which is $T_p^{\ast}M$ itself (Proposition [[§52 Critical Points and the Hessian#^prop-52-9|§52.9]]): $T_{(p,0)}(T^{\ast}M) = \zeta_{\ast p}(T_pM) \oplus j_p(T_p^{\ast}M)$. “This is the crucial thing that allows you to identify the quadratic form”: push $v \in T_pM$ forward by $s_f$; the vertical component of $(s_f)_{\ast p}v$ is the covector $\operatorname{Hess}_p f(v, \cdot)$ (Proposition [[§52 Critical Points and the Hessian#^prop-52-10|§52.10]]). *(Filled in.)* Away from the zero section the vertical space is still canonical, but there is no canonical complement to project along, so “the vertical component of $(s_f)_{\ast p}v$” depends on the chart — the geometric counterpart of the first-derivative term in the transformation law. Uribe ran out of time here; the full argument is the one already in these notes.

^rem-52-4

![[m591-52-1.svg]]

The picture from the review session. At $(p, 0)$ the tangent vector $(s_f)_{\ast p}v$ to $S_f$ splits into a part along the zero section, $\zeta_{\ast p}v$, and a vertical part in the fibre $T_p^{\ast}M$; the vertical part is $\operatorname{Hess}_p f(v, \cdot)$.

**Transcription note (review session).** Page 52 of the handwritten notes writes the key identification as “$T_pZ \cong T_p^{\ast}M$”. The tangent space of the zero section is $T_p\mathcal{Z} \cong T_pM$; it is the *vertical* space at $(p,0)$, equivalently the quotient $T_{(p,0)}(T^{\ast}M)/T_p\mathcal{Z}$, that is canonically $T_p^{\ast}M$ (Proposition [[§52 Critical Points and the Hessian#^prop-52-9|§52.9]]).

## Critical Points of Morse Functions

> [!theorem] Corollary §52.12: Critical Points of a Morse Function Are Isolated
> Let $f$ be a Morse function on $M$. Then $\operatorname{Crit}(f)$ is a regular submanifold of $M$ of codimension $m$, that is, of dimension $0$. Every critical point $p$ has an open neighbourhood $W$ in $M$ with $W \cap \operatorname{Crit}(f) = \{p\}$; so $\operatorname{Crit}(f)$ is discrete in the subspace topology.

^cor-52-12

> [!proof]+ Proof (Assignment 5, Problem 3(b))
> *(The submitted solution, written out.)* By Theorem [[§52 Critical Points and the Hessian#^thm-52-11|§52.11]], $s_f \pitchfork \mathcal{Z}$, since every critical point is nondegenerate. Theorem [[§37 Regular Submanifolds#^thm-37-15|§37.15]], applied to the smooth map $s_f : M \to T^{\ast}M$ and the regular submanifold $\mathcal{Z}$ of codimension $m$ (Proposition [[§52 Critical Points and the Hessian#^prop-52-5|§52.5]](1)), shows that $s_f^{-1}(\mathcal{Z}) = \operatorname{Crit}(f)$ (Proposition [[§52 Critical Points and the Hessian#^prop-52-10|§52.10]](1)) is a regular submanifold of $M$ of codimension $m$, the codimension of $\mathcal{Z}$ in $T^{\ast}M$ (indeed $2m - m$). Its dimension is $m - m = 0$ (Proposition [[§37 Regular Submanifolds#^prop-37-3|§37.3]]).
>
> *Isolated.* Let $p \in \operatorname{Crit}(f)$. By Definition [[§37 Regular Submanifolds#^def-37-2|§37.2]] with $k = m$, so that all $m$ coordinates are cut, there is a smooth chart $(W, \theta = (\theta^1, \ldots, \theta^m))$ of $M$ at $p$ with
>
> $$
> W \cap \operatorname{Crit}(f) = \{\, q \in W : \theta^1(q) = \cdots = \theta^m(q) = 0 \,\} = \theta^{-1}(0) .
> $$
>
> Since $p \in W \cap \operatorname{Crit}(f)$, $\theta(p) = 0$; since $\theta$ is injective, $\theta^{-1}(0) = \{p\}$. So $W \cap \operatorname{Crit}(f) = \{p\}$, with $W$ open in $M$.
>
> *Discrete.* $\{p\} = W \cap \operatorname{Crit}(f)$ is open in the subspace topology of $\operatorname{Crit}(f)$, for every $p$; so every subset of $\operatorname{Crit}(f)$, a union of such singletons, is open. With the induced structure, $\operatorname{Crit}(f)$ is a $0$-dimensional manifold, hence a countable discrete space (Proposition [[§2 Topological Manifolds#^prop-2-5|§2.5]]).

^pf-52-12

*Uses:* [[§52 Critical Points and the Hessian#^thm-52-11|§52.11]], [[§37 Regular Submanifolds#^thm-37-15|§37.15]], [[§52 Critical Points and the Hessian#^prop-52-5|§52.5]], [[§52 Critical Points and the Hessian#^prop-52-10|§52.10]], [[§37 Regular Submanifolds#^prop-37-3|§37.3]], [[§37 Regular Submanifolds#^def-37-2|Def. §37.2]], [[§2 Topological Manifolds#^prop-2-5|§2.5]]

> [!proof]+ Second proof, by the inverse function theorem
> *(Not from the submitted solution; filled in. It uses only that the one point $p$ is nondegenerate.)* Let $p \in \operatorname{Crit}(f)$ and $(U, \varphi)$ a chart at $p$, and let $\Phi = (\partial f/\partial x^1, \ldots, \partial f/\partial x^m) \circ \varphi^{-1} : \varphi(U) \to \mathbb{R}^m$, smooth by Proposition [[§52 Critical Points and the Hessian#^prop-52-1|§52.1]](3).
>
> *The critical points in $U$ are the zeros of $\Phi$, transported.* For $q \in U$, $\Phi(\varphi(q)) = \big(\partial f/\partial x^1(q), \ldots, \partial f/\partial x^m(q)\big)$, and $q$ is critical exactly when all these partials vanish (Proposition [[§36 Submersions#^prop-36-2|§36.2]]). So $q \in \operatorname{Crit}(f) \cap U$ if and only if $\Phi(\varphi(q)) = 0$.
>
> *$\Phi$ is injective near $\varphi(p)$.* By Proposition [[§52 Critical Points and the Hessian#^prop-52-1|§52.1]](3), $\Phi'(\varphi(p)) = H_p$, which is invertible because $p$ is nondegenerate ($\det H_p \neq 0$, Proposition [[§52 Critical Points and the Hessian#^prop-52-4|§52.4]](2)). The set $\varphi(U)$ is open in $\mathbb{R}^m$, so the Inverse Function Theorem (Theorem [[§35 Local Diffeomorphisms#^thm-35-1|§35.1]]) gives an open set $U_0 \ni \varphi(p)$ in $\varphi(U)$ on which $\Phi$ is injective (it is a bijection of $U_0$ onto an open set $V_0$).
>
> *Conclusion.* Put $W = \varphi^{-1}(U_0)$, open in $U$ because $\varphi$ is continuous, hence open in $M$ (Lemma [[§3 Subspaces and Products#^lem-3-2|§3.2]]), and containing $p$. If $q \in W \cap \operatorname{Crit}(f)$, then $\Phi(\varphi(q)) = 0 = \Phi(\varphi(p))$ with $\varphi(q), \varphi(p) \in U_0$, so $\varphi(q) = \varphi(p)$ by injectivity, and $q = p$ since $\varphi$ is injective. So $W \cap \operatorname{Crit}(f) = \{p\}$. As $p$ was arbitrary, $\operatorname{Crit}(f)$ is discrete, as in the first proof. (In words: near a nondegenerate critical point the map $\Phi$ is a local diffeomorphism, so $0$ is hit only once.)

^pf-52-12-2

*Uses:* [[§52 Critical Points and the Hessian#^prop-52-1|§52.1]], [[§36 Submersions#^prop-36-2|§36.2]], [[§52 Critical Points and the Hessian#^prop-52-4|§52.4]], [[§35 Local Diffeomorphisms#^thm-35-1|§35.1]], [[§3 Subspaces and Products#^lem-3-2|§3.2]]

The converse fails: in Example [[§52 Critical Points and the Hessian#^ex-52-2|§52.2]](2), $0$ is an isolated critical point of $x^3$ but a degenerate one. And without nondegeneracy critical points need not be isolated at all: every point is critical for a constant function.

> [!theorem] Corollary §52.13: Morse Functions on Compact Manifolds
> Let $f$ be a Morse function on $M$.
>
> 1. $\operatorname{Crit}(f)$ is closed in $M$.
> 2. If $M$ is compact, then $\operatorname{Crit}(f)$ is finite.

^cor-52-13

> [!proof]+ Proof
> *(Not from lecture; filled in. Part (1) does not use that $f$ is Morse.)*
>
> *(1)* This is Corollary [[§36 Submersions#^cor-36-8|§36.8]]: the set of critical points of any smooth function on $M$ is closed in $M$; that $f$ is Morse is not used. (Two direct arguments. First: let $q \in M \setminus \operatorname{Crit}(f)$ and $(U, \varphi)$ a chart at $q$. Since $df_q \neq 0$, some $\partial f/\partial x^j(q)$ is nonzero (Proposition [[§36 Submersions#^prop-36-2|§36.2]]). The function $\partial f/\partial x^j$ is smooth, hence continuous, on $U$ (Lemma [[§29 Coordinate Derivations and the Basis Theorem#^lem-29-1|§29.1]]), so $O = \{q' \in U : \partial f/\partial x^j(q') \neq 0\}$, the preimage of the open set $\mathbb{R} \setminus \{0\}$, is open in $U$, hence in $M$ (Lemma [[§3 Subspaces and Products#^lem-3-2|§3.2]]). It contains $q$, and every $q' \in O$ is a regular point, by Proposition [[§36 Submersions#^prop-36-2|§36.2]] again; so $M \setminus \operatorname{Crit}(f)$ is open. Second: $\operatorname{Crit}(f) = s_f^{-1}(\mathcal{Z})$ (Proposition [[§52 Critical Points and the Hessian#^prop-52-10|§52.10]](1)) with $s_f$ continuous, and $\mathcal{Z}$ is closed in $T^{\ast}M$, its complement meeting each $T^{\ast}U$ in the open set $\hat\varphi^{-1}\big(\varphi(U) \times (\mathbb{R}^m \setminus \{0\})\big)$.)
>
> *(2)* By (1), $\operatorname{Crit}(f)$ is a closed subset of the compact space $M$, hence compact (Proposition [[§1 Point-Set Topology Review#^prop-1-8|§1.8]](5)). By Corollary [[§52 Critical Points and the Hessian#^cor-52-12|§52.12]], each $p \in \operatorname{Crit}(f)$ has an open neighbourhood $W_p$ in $M$ with $W_p \cap \operatorname{Crit}(f) = \{p\}$. The sets $W_p \cap \operatorname{Crit}(f) = \{p\}$, $p \in \operatorname{Crit}(f)$, are open in the subspace topology of $\operatorname{Crit}(f)$ and cover it. By compactness finitely many of them cover it: $\operatorname{Crit}(f) = \{p_1\} \cup \cdots \cup \{p_N\}$. So $\operatorname{Crit}(f)$ is finite. (Equivalently: an infinite subset of a compact space has an accumulation point, and an accumulation point of $\operatorname{Crit}(f)$ would lie in $\operatorname{Crit}(f)$ by (1) without being isolated.)

^pf-52-13

*Uses:* [[§36 Submersions#^cor-36-8|§36.8]], [[§36 Submersions#^prop-36-2|§36.2]], [[§29 Coordinate Derivations and the Basis Theorem#^lem-29-1|§29.1]], [[§3 Subspaces and Products#^lem-3-2|§3.2]], [[§52 Critical Points and the Hessian#^prop-52-10|§52.10]], [[§1 Point-Set Topology Review#^prop-1-8|§1.8]], [[§52 Critical Points and the Hessian#^cor-52-12|§52.12]]

## The Hessian from the Zero Section

*Lecture 20, the day of the midterm. “What I want to do today and Friday is go over certain topics that … don't fit in the narrative of vector fields. … Math doesn't exist as a narrative, right? It's all there at the same time, and we make stories about it, because that's what people do.” Vector fields resume, from the dynamical point of view, on Monday. First the Hessian: “I mentioned something last time, but I didn't write anything down … Let's take the time to do it.”*

*The claim* (Proposition [[§52 Critical Points and the Hessian#^prop-52-3|§52.3]] and Definition [[§52 Critical Points and the Hessian#^def-52-2|§52.2]]): if $f : M \to \mathbb{R}$ is smooth and $df_p = 0$, there is a well-defined quadratic form, a symmetric bilinear form $\operatorname{Hess}_p f : T_pM \times T_pM \to \mathbb{R}$, whose matrix in any coordinates is $\big(\partial^2 f/\partial x^i \partial x^j(p)\big)$. “You can always, in any coordinate system, at any point, write this matrix, but it doesn't define a coordinate-independent quadratic form unless you are at a critical point.” Lecture 20 explained why, coordinate-free.

*The observation that makes it go.* At a point $(p, 0)$ of the zero section $\mathcal{Z}$ of $T^{\ast}M$, the zero section and the fibre $\pi^{-1}(p) = T_p^{\ast}M$ are transverse and complementary, so (Proposition [[§52 Critical Points and the Hessian#^prop-52-9|§52.9]])

$$
T_{(p,0)}(T^{\ast}M) = T_{(p,0)}\mathcal{Z} \oplus T_{(p,0)}\pi^{-1}(p) \cong T_pM \oplus T_p^{\ast}M ,
$$

“without choosing any coordinates”: the zero section is naturally $M$, and the tangent space to the fibre, a vector space, is the fibre itself. Now consider the section $s_f : M \to T^{\ast}M$, $q \mapsto (q, df_q)$, of the homework. If $df_p = 0$, then $s_f(p) = (p, 0)$, and $\operatorname{Im}(s_f)_{\ast p} \subseteq T_{(p,0)}(T^{\ast}M) = T_pM \oplus T_p^{\ast}M$.

> [!theorem] Proposition §52.14: The Hessian as the Graph of $(s_f)_{\ast p}$
> Let $f : M \to \mathbb{R}$ be smooth and $p \in \operatorname{Crit}(f)$. In the splitting $T_{(p,0)}(T^{\ast}M) = T_pM \oplus T_p^{\ast}M$ above, $\operatorname{Im}(s_f)_{\ast p}$ is the graph of a unique linear map $h_p : T_pM \to T_p^{\ast}M$, and
>
> $$
> \operatorname{Hess}_p f(u, v) = h_p(u)(v), \qquad u, v \in T_pM .
> $$
>
> In a chart, the matrix of $(s_f)_{\ast p}$ is $\binom{I}{H_p}$, with $H_p = \big(\partial^2 f/\partial x^i \partial x^j(p)\big)$ the block of $h_p$.

^prop-52-14

> [!proof]+ Proof
> *(Lecture 20, with the details Uribe skipped — “I will skip the details” — filled in from the propositions already in these notes.)* *A graph.* Since $s_f$ is a section, $\pi \circ s_f = \mathrm{id}_M$, so $\pi_{\ast(p,0)} \circ (s_f)_{\ast p} = \mathrm{id}$ by the chain rule. The projection onto the first summand of the splitting is $\pi_{\ast(p,0)}$ (it kills the vertical summand, Proposition [[§52 Critical Points and the Hessian#^prop-52-9|§52.9]](1), and is the identity on $T_{(p,0)}\mathcal{Z} \cong T_pM$, as $\pi \circ \zeta = \mathrm{id}_M$). So $(s_f)_{\ast p}u = (u, h_p(u))$ for a unique $h_p(u) \in T_p^{\ast}M$, and $h_p$ is linear because $(s_f)_{\ast p}$ is: the image “passes the vertical line test”, an $m$-dimensional subspace that is the graph of $h_p$. “For example, if $f$ is constant, then this is zero, and you get just the horizontal.”
>
> *The Hessian.* “A map from a vector space to its dual … is the same as a bilinear map”: $(u, v) \mapsto h_p(u)(v)$. By Proposition [[§52 Critical Points and the Hessian#^prop-52-10|§52.10]](3), the vertical component of $(s_f)_{\ast p}u$ is $\operatorname{Hess}_p f(u, \cdot\,)$, so $h_p(u) = \operatorname{Hess}_p f(u, \cdot\,)$. In coordinates, the matrix of $(s_f)_{\ast p}$ is $\binom{I}{H_p}$ (Proposition [[§52 Critical Points and the Hessian#^prop-52-10|§52.10]](2), the homework computation), and “once you unravel everything … the matrix of $h_p$ in the induced coordinates is just this bottom” block.

^pf-52-14

*Uses:* [[§52 Critical Points and the Hessian#^prop-52-9|§52.9]], [[§52 Critical Points and the Hessian#^prop-52-10|§52.10]]

![[m591-52-2.svg]]

The splitting at a point of the zero section, and the image of $(s_f)_{\ast p}$ in it: a line through the origin that “passes the vertical line test”, the graph of $h_p$. Its slope is the Hessian: $h_p(u) = \operatorname{Hess}_p f(u, \cdot\,)$. A line through the origin is such a graph exactly when it meets the vertical axis (the fibre direction) only in $0$.

*Away from a critical point.* The horizontal summand “has nothing to do with $f$. It's just because … we have the zero section, and then we have the fibre, and they're just sitting there”; at $(p, df_p)$ with $df_p \neq 0$ the fibre is still there, but there is no zero section through the point. A student asked why one cannot use some other section through $(p, df_p)$: “Yeah, you can put a section, but you have to make a choice … because you make a choice, you don't have a well-defined” Hessian. In coordinates (“which we haven't done much of”), with two charts $(x^i)$ and $(y^j)$, $\partial f/\partial x^i = \sum_j (\partial y^j/\partial x^i)\, \partial f/\partial y^j$, and differentiating again,

$$
\frac{\partial^2 f}{\partial x^k \partial x^i} = \sum_j \frac{\partial^2 y^j}{\partial x^k \partial x^i}\, \frac{\partial f}{\partial y^j} + \sum_{j,l} \frac{\partial y^j}{\partial x^i}\, \frac{\partial y^l}{\partial x^k}\, \frac{\partial^2 f}{\partial y^l \partial y^j} :
$$

the first sum “will not go away in general”, so the matrix “doesn't transform like a quadratic form unless these guys are zero” (Proposition [[§52 Critical Points and the Hessian#^prop-52-2|§52.2]]).

> [!remark] Remark: Natural Is Not Canonical
> “Natural is not the same thing as canonical. This was [drilled] into me when I was your age. *Canonical* means that this is how we do it: we follow the canon, an established set of traditions. *Natural* means that this is how nature does it. It's not a convention. It's just sitting there, in the mathematical world.” The splitting $T_{(p,0)}(T^{\ast}M) = T_pM \oplus T_p^{\ast}M$ “is natural. It's not canonical.”

^rem-52-5

*Jets.* “In the same sort of direction”: for every $k$ the quotient of germs by a power of $I_p$ makes sense, generalizing $T_p^{\ast}M \cong I_p/I_p^2$ (Theorem [[§34 The Cotangent Space from Germs#^thm-34-4|§34.4]]).

> [!definition] Definition §52.7: Jets
> Let $p \in M$ and $k \ge 0$. The space of **$k$-jets** at $p$ is
>
> $$
> J^k_p = C^\infty_p(M) \big/ I_p^{k+1},
> $$
>
> where $I_p^{k+1}$ is spanned by products of $k + 1$ germs vanishing at $p$. The class of a germ is its $k$-jet.

^def-52-7

> [!definition] Definition §52.8: Multi-Index Notation
> A **multi-index** is an $m$-tuple $\alpha = (\alpha_1, \ldots, \alpha_m)$ of integers $\alpha_i \ge 0$, with **order** $|\alpha| = \alpha_1 + \cdots + \alpha_m$ and $\alpha! = \alpha_1! \cdots \alpha_m!$. In a chart $(U, (x^1, \ldots, x^m))$, with $\partial_i = \partial/\partial x^i$ acting on $C^\infty(U)$,
>
> $$
> \partial^\alpha = \partial_1^{\alpha_1} \circ \cdots \circ \partial_m^{\alpha_m}, \qquad (x - c)^\alpha = (x^1 - c^1)^{\alpha_1} \cdots (x^m - c^m)^{\alpha_m} \quad (c \in \mathbb{R}^m),
> $$
>
> and $\partial^{(0, \ldots, 0)} = \mathrm{id}$. Write $\beta \le \alpha$ if $\beta_i \le \alpha_i$ for every $i$, and $e_j$ for the multi-index with $1$ in place $j$ and $0$ elsewhere.

^def-52-8

> [!theorem] Lemma §52.15: Derivatives of Monomials
> Let $(U, \varphi = (x^1, \ldots, x^m))$ be a chart, $p \in U$, $c = \varphi(p)$, and $\alpha$, $\beta$ multi-indices. On $U$,
>
> $$
> \partial^\alpha (x - c)^\beta = \begin{cases} \dfrac{\beta!}{(\beta - \alpha)!}\, (x - c)^{\beta - \alpha} & \text{if } \alpha \le \beta, \\[4pt] 0 & \text{otherwise,} \end{cases}
> $$
>
> with $(\beta - \alpha)_i = \beta_i - \alpha_i$. In particular $\partial^\alpha (x - c)^\beta(p) = \beta!$ if $\alpha = \beta$ and $0$ if $\alpha \ne \beta$; so the coefficients of a polynomial $P = \sum_{|\beta| \le k} c_\beta\, (x - c)^\beta$ are $c_\beta = \partial^\beta P(p)/\beta!$.

^lem-52-15

> [!proof]+ Proof
> *(Not from lecture; filled in.)* Partial derivatives on $U$ are computed from coordinate representations: $(\partial_i u) \circ \varphi^{-1} = \partial(u \circ \varphi^{-1})/\partial r^i$ (Definition [[§29 Coordinate Derivations and the Basis Theorem#^def-29-2|§29.2]]), so, applying this $|\alpha|$ times, $(\partial^\alpha u) \circ \varphi^{-1} = \partial^{|\alpha|}(u \circ \varphi^{-1})/\partial r^\alpha$. In coordinates, $(x - c)^\beta \circ \varphi^{-1}(r) = \prod_i (r^i - c^i)^{\beta_i}$, a product of factors each depending on one variable, so
>
> $$
> \frac{\partial^{|\alpha|}}{\partial r^\alpha} \prod_{i=1}^m (r^i - c^i)^{\beta_i} = \prod_{i=1}^m \frac{\partial^{\alpha_i}}{\partial (r^i)^{\alpha_i}} (r^i - c^i)^{\beta_i}, \qquad \frac{\partial^{\alpha_i}}{\partial (r^i)^{\alpha_i}} (r^i - c^i)^{\beta_i} = \begin{cases} \dfrac{\beta_i!}{(\beta_i - \alpha_i)!} (r^i - c^i)^{\beta_i - \alpha_i} & \alpha_i \le \beta_i, \\ 0 & \alpha_i > \beta_i . \end{cases}
> $$
>
> That is, $\partial^\alpha (x - c)^\beta = \frac{\beta!}{(\beta - \alpha)!} (x - c)^{\beta - \alpha}$ if $\alpha \le \beta$, and $0$ otherwise. At $x = c$, i.e. at the point $p$, the factor $(r^i - c^i)^{\beta_i - \alpha_i}$ is $1$ if $\alpha_i = \beta_i$ and $0$ if $\alpha_i < \beta_i$; so $\partial^\alpha (x - c)^\beta(p)$ vanishes unless $\alpha = \beta$, where it is $\beta!$. For the last statement, apply $\partial^\alpha$ to $P$ and evaluate at $p$: $\partial^\alpha P(p) = \sum_\beta c_\beta\, \partial^\alpha (x - c)^\beta(p) = c_\alpha\, \alpha!$.

^pf-52-15

*Uses:* [[§29 Coordinate Derivations and the Basis Theorem#^def-29-2|Def. §29.2]]

> [!theorem] Proposition §52.16: Jets Are Taylor Polynomials
> In a chart $(x^1, \ldots, x^m)$ centred at $p$, two germs have the same $k$-jet if and only if their partial derivatives of all orders $\le k$ agree at $p$, that is, their Taylor polynomials of degree $k$ at $p$ agree. So $J^k_p$ is isomorphic to the space of polynomials of degree $\le k$ in $m$ variables.

^prop-52-16

> [!proof]+ Proof
> *(Lecture 20: “this just isolates … the partial sum of the Taylor series. You kill derivatives of order $k+1$ and higher.” Filled in.)* It suffices to show that $[g] \in I_p^{k+1}$ if and only if all partials of $g$ of orders $0, \ldots, k$ vanish at $p$. *Only if.* A product $g_1 \cdots g_{k+1}$ of germs vanishing at $p$: by the Leibniz rule, a partial derivative of order $\le k$ of the product is a sum of products in each of which some factor $g_i$ is not differentiated, and so vanishes at $p$; sums of such products behave the same. *If.* Applying Hadamard's lemma (Lemma [[§29 Coordinate Derivations and the Basis Theorem#^lem-29-3|§29.3]]) repeatedly to the coefficient functions, as in the proof of Lemma [[§29 Coordinate Derivations and the Basis Theorem#^lem-29-4|§29.4]], gives, on a ball about $p$,
>
> $$
> g = \sum_{|\alpha| \le k} \frac{\partial^\alpha g(p)}{\alpha!}\, x^\alpha + \sum_{|\beta| = k+1} x^\beta\, g_\beta
> $$
>
> with $g_\beta$ smooth. If all $\partial^\alpha g(p)$ with $|\alpha| \le k$ vanish, then $[g] = \sum_\beta [x^\beta][g_\beta]$, and each $x^\beta$, $|\beta| = k+1$, is a product of $k + 1$ coordinate functions vanishing at $p$; so $[g] \in I_p^{k+1}$. Finally, a polynomial $P = \sum_{|\beta| \le k} c_\beta\, x^\beta$ is the Taylor polynomial of its own germ, since $\partial^\beta P(p)/\beta! = c_\beta$ (Lemma [[§52 Critical Points and the Hessian#^lem-52-15|§52.15]], with $c = 0$ for the chart centred at $p$); so the map from $J^k_p$ to Taylor polynomials is onto.

^pf-52-16

*Uses:* [[§29 Coordinate Derivations and the Basis Theorem#^lem-29-3|§29.3]], [[§29 Coordinate Derivations and the Basis Theorem#^lem-29-4|§29.4]], [[§52 Critical Points and the Hessian#^lem-52-15|§52.15]]

![[m591-52-3.svg]]

*(Not from lecture; figure added.)* The jets of a function $f$ of one variable at $p$, drawn as its Taylor polynomials (Proposition [[§52 Critical Points and the Hessian#^prop-52-16|§52.16]]): the $0$-jet $T_0$ is the value $f(p)$, the $1$-jet $T_1$ the tangent line, the $2$-jet $T_2$ the osculating parabola. Two germs have the same $k$-jet when their difference lies in $I_p^{k+1}$, that is, vanishes to order $k + 1$ at $p$. For $k = 1$, removing the value leaves $I_p/I_p^2 \cong T_p^{\ast}M$ (Theorem [[§34 The Cotangent Space from Germs#^thm-34-4|§34.4]]): the $1$-jet of a germ vanishing at $p$ is its differential.

“This is called a space of jets … they are useful in some circles. If you take $k = 2$, you can package the information contained in the function — the value, the first derivative, the second derivative — in some abstract object.” But “within them you cannot separate naturally the first and the second partials, unless you have a special situation” — a critical point being the special situation that gives the Hessian.

**Transcription note (Lecture 20).** Page 53 of the handwritten notes writes the jet space as $C^\infty_p(M)/I_p^k$, which keeps derivatives through order $k - 1$; Uribe corrected it in lecture (“maybe I should put $k + 1$ here”), and the $k$-jet is $C^\infty_p(M)/I_p^{k+1}$. The splitting there is written at “$(0, p)$”; in these notes the point of the zero section over $p$ is $(p, 0)$.
