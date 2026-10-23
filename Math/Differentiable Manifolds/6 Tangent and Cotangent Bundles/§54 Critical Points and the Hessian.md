---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 6
section: 54
tags: [differentiable-manifolds, math591]
---
← [[§53 One-Forms]] · ↑ [[· 6 Tangent and Cotangent Bundles]] · [[§55 Morse Functions and the Zero Section]] →

*Stage: fields — The second derivatives of a function at a critical point form a symmetric bilinear form on the tangent space, the Hessian; nondegenerate critical points and Morse functions.*

*Assignment 5, Problem 3, with what its proof contains. Not from lecture. The problem: the section $p \mapsto (p, df_p)$ of $T^{\ast}M$ is transverse to the zero section exactly when every critical point of $f$ has a nondegenerate Hessian; and what is the critical set of a Morse function? The Hessian, the splitting of $T(T^{\ast}M)$ along the zero section, and the second proofs are filled in around the submitted solution.*

Throughout, $M$ is a smooth manifold of dimension $m$ and $f : M \to \mathbb{R}$ is smooth. Its set of critical points is $\operatorname{Crit}(f) = \{\, p \in M : df_p = 0 \,\}$ (Definition [[§36 Submersions#^def-36-5|§36.5]]), the set of critical points in the sense of Definition [[§36 Submersions#^def-36-3|§36.3]], by Proposition [[§36 Submersions#^prop-36-2|§36.2]].

## The Hessian Matrix

> [!definition] Definition §54.1: Hessian Matrix
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

^def-54-1

The function $f_\varphi$ is smooth on the open set $\varphi(U)$ (Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-1|§19.1]]), so its mixed partials are equal (Clairaut's theorem), and $H_p$ is symmetric, $H_{ij}(p) = H_{ji}(p)$. This is part (2) of the next proposition, which rewrites $H_p$ upstairs, on $M$.

> [!theorem] Proposition §54.1: Forms of the Hessian Matrix
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

^prop-54-1

> [!proof]+ Proof
> *(Assignment 5, Problem 3: the submitted solution's description of the Hessian, written out.)* Write $g_j = \partial f/\partial x^j : U \to \mathbb{R}$ for $j = 1, \ldots, m$.
>
> *(1)* For $q \in U$, Proposition [[§32 The Cotangent Space#^prop-32-2|§32.2]] with $D = \partial/\partial x^j|_q$ gives $df_q(\partial/\partial x^j|_q) = \partial f/\partial x^j(q) = g_j(q)$. By Proposition [[§53 One-Forms#^prop-53-2|§53.2]], $df$ is a one-form with $df = \sum_j g_j\, dx^j$ on $U$, and $g_j(q) = df_q(\partial/\partial x^j|_q)$ is exactly the $j$-th coefficient function of Proposition [[§53 One-Forms#^prop-53-1|§53.1]] for $\theta = df$. Lemma [[§29 Coordinate Derivations and the Basis Theorem#^lem-29-1|§29.1]], applied to the restriction of $f$ to $U$, gives that $g_j$ is smooth on $U$ and that
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
> the last step by Definition [[§54 Critical Points and the Hessian#^def-54-1|§54.1]].
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

^pf-54-1

*Uses:* [[§32 The Cotangent Space#^prop-32-2|§32.2]], [[§53 One-Forms#^prop-53-2|§53.2]], [[§53 One-Forms#^prop-53-1|§53.1]], [[§29 Coordinate Derivations and the Basis Theorem#^lem-29-1|§29.1]], [[§29 Coordinate Derivations and the Basis Theorem#^def-29-2|Def. §29.2]], [[§54 Critical Points and the Hessian#^def-54-1|Def. §54.1]], [[§19 Smooth Functions and Smooth Maps#^prop-19-1|§19.1]], [[§33 Covectors in Coordinates#^lem-33-1|§33.1]], [[§33 Covectors in Coordinates#^cor-33-2|§33.2]], [[§7 The Regular Value Theorem#^def-7-1|Def. §7.1]]

> [!theorem] Proposition §54.2: Change of Coordinates for the Hessian
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

^prop-54-2

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
> (iii) By Definitions [[§29 Coordinate Derivations and the Basis Theorem#^def-29-2|§29.2]] and [[§54 Critical Points and the Hessian#^def-54-1|§54.1]] in the chart $\psi$, $\partial f/\partial y^k(p) = \partial f_\psi/\partial r^k(\tau(a))$ and $H^{(y)}_{kl}(p) = \partial^2 f_\psi/\partial r^k \partial r^l(\tau(a))$.
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
> At $r = a$ the left side is $H^{(x)}_{ij}(p)$ (Definition [[§54 Critical Points and the Hessian#^def-54-1|§54.1]]), and by (ii) and (iii) the right side is
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

^pf-54-2

*Uses:* [[§17 Differentiable Structures#^lem-17-6|§17.6]], [[§17 Differentiable Structures#^def-17-4|Def. §17.4]], [[§29 Coordinate Derivations and the Basis Theorem#^def-29-1|Def. §29.1]], [[§19 Smooth Functions and Smooth Maps#^def-19-2|Def. §19.2]], [[§29 Coordinate Derivations and the Basis Theorem#^lem-29-1|§29.1]], [[§29 Coordinate Derivations and the Basis Theorem#^def-29-2|Def. §29.2]], [[§54 Critical Points and the Hessian#^def-54-1|Def. §54.1]], [[§36 Submersions#^prop-36-2|§36.2]], [[§30 The Differential in Coordinates#^cor-30-4|§30.4]]

> [!example] Example §54.1: The Hessian Matrix Depends on the Chart
> Away from critical points the second sum is genuinely there. On $M = \mathbb{R}$ take $f(t) = t$ and $p = 0$, and two charts on $U = (-\tfrac12, \infty)$: $\varphi = \mathrm{id}_U$, with coordinate $x$, and $\psi(t) = t + t^2$, with coordinate $y$. Then $H^{(x)}(0) = 0$ but $H^{(y)}(0) = -2$.

^ex-54-1

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
> *Check against Proposition [[§54 Critical Points and the Hessian#^prop-54-2|§54.2]].* $J = \partial y/\partial x(0) = \psi'(0) = 1$, $\partial f/\partial y(0) = f_\psi'(0) = 1$ and $\partial^2 y/\partial x^2(0) = \psi''(0) = 2$, so the formula gives $H^{(x)}(0) = 1 \cdot 1 \cdot (-2) + 1 \cdot 2 = 0$, as it should. The point $0$ is not critical, $df_0 \neq 0$; even the rank of the Hessian matrix there, $0$ in one chart and $1$ in the other, depends on the chart.

^pf-ex-54-1

*Uses:* [[§17 Differentiable Structures#^def-17-4|Def. §17.4]], [[§17 Differentiable Structures#^thm-17-5|§17.5]], [[§54 Critical Points and the Hessian#^prop-54-2|§54.2]]

## The Hessian at a Critical Point

At a critical point the transformation law is $H^{(x)}_p = J^{\mathsf T} H^{(y)}_p J$, the law of a bilinear form, and the Hessian matrix becomes the matrix of a chart-free object.

> [!theorem] Proposition §54.3: The Hessian at a Critical Point Is Well Defined
> Let $p \in \operatorname{Crit}(f)$ and $v, w \in T_pM$. For a smooth chart $(U, \varphi = (x^1, \ldots, x^m))$ at $p$, let $v^i = v[x^i]$ and $w^j = w[x^j]$ be the components of $v$ and $w$ (Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]]). Then the number
>
> $$
> \sum_{i,j=1}^m H_{ij}(p)\, v^i\, w^j
> $$
>
> is the same for every chart at $p$; and, as a function of $(v, w)$, it is bilinear and symmetric.

^prop-54-3

> [!proof]+ Proof
> *(Not from lecture; filled in.)* *Independence of the chart.* Let $(V, \psi = (y^1, \ldots, y^m))$ be a second chart at $p$, write $v^{(y)k} = v[y^k]$ and $w^{(y)l} = w[y^l]$ for the components in it, and let $J_{ki} = \partial y^k/\partial x^i(p)$ as in Proposition [[§54 Critical Points and the Hessian#^prop-54-2|§54.2]]. First, the components transform by $J$: Corollary [[§30 The Differential in Coordinates#^cor-30-4|§30.4]](2), applied to the charts $\varphi = (x^i)$ and $\psi = (y^k)$ at $p$ and the vector $v$, gives
>
> $$
> v^{(y)k} = v\big[y^k\big] = \sum_{i=1}^m \frac{\partial y^k}{\partial x^i}(p)\, v\big[x^i\big] = \sum_{i=1}^m J_{ki}\, v^i ,
> $$
>
> and, applied to $w$, likewise $w^{(y)l} = \sum_j J_{lj}\, w^j$. Substituting, expanding the product of the two sums, and then using Proposition [[§54 Critical Points and the Hessian#^prop-54-2|§54.2]] at the critical point $p$ ($\sum_{k,l} J_{ki} H^{(y)}_{kl}(p) J_{lj} = H^{(x)}_{ij}(p)$):
>
> $$
> \sum_{k,l} H^{(y)}_{kl}(p)\, v^{(y)k}\, w^{(y)l} = \sum_{k,l} H^{(y)}_{kl}(p) \Big(\sum_i J_{ki}\, v^i\Big)\Big(\sum_j J_{lj}\, w^j\Big) = \sum_{i,j} \Big(\sum_{k,l} J_{ki}\, H^{(y)}_{kl}(p)\, J_{lj}\Big) v^i w^j = \sum_{i,j} H^{(x)}_{ij}(p)\, v^i w^j .
> $$
>
> So the two charts give the same number.
>
> *Bilinear.* The maps $v \mapsto v^i = v[x^i]$ are linear, because tangent vectors are added and scaled pointwise (Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-2|§28.2]]): $(av + bv')[x^i] = a\,v[x^i] + b\,v'[x^i]$. For fixed $w$ the number $\sum_{i,j} H_{ij}(p)\, v^i w^j$ is a linear combination of the $v^i$ with coefficients $\sum_j H_{ij}(p) w^j$, hence linear in $v$; for fixed $v$ it is likewise linear in $w$.
>
> *Symmetric.* By Proposition [[§54 Critical Points and the Hessian#^prop-54-1|§54.1]](2), $H_{ij}(p) = H_{ji}(p)$, so exchanging the names of the summation indices,
>
> $$
> \sum_{i,j} H_{ij}(p)\, w^i v^j = \sum_{i,j} H_{ji}(p)\, w^j v^i = \sum_{i,j} H_{ij}(p)\, v^i w^j .
> $$

^pf-54-3

*Uses:* [[§54 Critical Points and the Hessian#^prop-54-2|§54.2]], [[§30 The Differential in Coordinates#^cor-30-4|§30.4]], [[§28 Derivations and the Abstract Tangent Space#^def-28-2|Def. §28.2]], [[§54 Critical Points and the Hessian#^prop-54-1|§54.1]]

> [!definition] Definition §54.2: Hessian at a Critical Point
> Let $p \in \operatorname{Crit}(f)$. The **Hessian** of $f$ at $p$ is the symmetric bilinear form
>
> $$
> \operatorname{Hess}_p f : T_pM \times T_pM \longrightarrow \mathbb{R}, \qquad \operatorname{Hess}_p f(v, w) = \sum_{i,j=1}^m H_{ij}(p)\, v^i\, w^j, \quad v^i = v[x^i],\ w^j = w[x^j],
> $$
>
> computed in any smooth chart $(U, \varphi = (x^i))$ at $p$; it does not depend on the chart, and is bilinear and symmetric, by Proposition [[§54 Critical Points and the Hessian#^prop-54-3|§54.3]]. In matrix form, with $H_p$ the Hessian matrix of the chart (Definition [[§54 Critical Points and the Hessian#^def-54-1|§54.1]]),
>
> $$
> \operatorname{Hess}_p f(v, w) = \begin{pmatrix} v^1 & \cdots & v^m \end{pmatrix} H_p \begin{pmatrix} w^1 \\ \vdots \\ w^m \end{pmatrix} .
> $$
> On the coordinate basis, $\operatorname{Hess}_p f\big(\partial/\partial x^i|_p, \partial/\partial x^j|_p\big) = H_{ij}(p)$.

^def-54-2

The last formula holds because the components of $\partial/\partial x^i|_p$ are $\partial/\partial x^i|_p[x^l] = \delta^l_i$ (Lemma [[§33 Covectors in Coordinates#^lem-33-1|§33.1]]: the $dx^l|_p$ form the basis dual to the $\partial/\partial x^i|_p$, and $\partial/\partial x^i|_p[x^l] = dx^l|_p(\partial/\partial x^i|_p)$ by Proposition [[§32 The Cotangent Space#^prop-32-2|§32.2]]), so only the term with $l = i$, $l' = j$ survives in $\sum_{l,l'} H_{ll'}(p)\, \delta^l_i\, \delta^{l'}_j$. At a point that is not critical no such form exists: by Example [[§54 Critical Points and the Hessian#^ex-54-1|§54.1]] the matrices of two charts need not even have the same rank.

> [!definition] Definition §54.3: Nondegenerate Critical Point
> A critical point $p$ of $f$ is **nondegenerate** if $\operatorname{Hess}_p f$ is a non-degenerate pairing (Definition [[§21 Linear Algebra Toolkit#^def-21-5|§21.5]]): the linear maps
>
> $$
> (\operatorname{Hess}_p f)^\flat : T_pM \longrightarrow T_p^{\ast}M, \quad v \longmapsto \operatorname{Hess}_p f(v, \cdot\,), \qquad (\operatorname{Hess}_p f)^\sharp : T_pM \longrightarrow T_p^{\ast}M, \quad w \longmapsto \operatorname{Hess}_p f(\cdot\,, w)
> $$
>
> (Definition [[§21 Linear Algebra Toolkit#^def-21-4|§21.4]]) are injective. Otherwise $p$ is **degenerate**.

^def-54-3

The next proposition makes the condition concrete. Since $\operatorname{Hess}_p f$ is symmetric, it is the injectivity of $(\operatorname{Hess}_p f)^\flat$ alone — equivalently, as $\dim T_pM = \dim T_p^{\ast}M = m$, its bijectivity — and, equivalently, $\det H_p \neq 0$ in some, hence every, chart at $p$.

> [!theorem] Proposition §54.4: The Hessian as a Map $T_pM \to T_p^{\ast}M$
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

^prop-54-4

> [!proof]+ Proof
> *(Not from lecture; filled in. Condition (f) is the form in which the submitted solution of Assignment 5, Problem 3 uses nondegeneracy.)* By Definition [[§54 Critical Points and the Hessian#^def-54-2|§54.2]], $B$ is a symmetric bilinear form on $T_pM$ with $B(\partial/\partial x^i|_p, \partial/\partial x^j|_p) = H_{ij}(p)$ (the formula after that definition).
>
> *(1) The map $B^\sharp$.* For each $j$, $B^\sharp(\partial/\partial x^j|_p) = B(\cdot\,, \partial/\partial x^j|_p)$ is a covector (Definition [[§21 Linear Algebra Toolkit#^def-21-4|§21.4]]). Its components (Definition [[§33 Covectors in Coordinates#^def-33-1|§33.1]]) are its values on the basis vectors, $B(\partial/\partial x^i|_p, \partial/\partial x^j|_p) = H_{ij}(p)$. So, by Corollary [[§33 Covectors in Coordinates#^cor-33-2|§33.2]] and Proposition [[§54 Critical Points and the Hessian#^prop-54-1|§54.1]](3),
>
> $$
> B^\sharp\Big(\frac{\partial}{\partial x^j}\Big|_p\Big) = \sum_{i=1}^m H_{ij}(p)\, dx^i\big|_p = d\Big(\frac{\partial f}{\partial x^j}\Big)_p .
> $$
>
> This step does not use the symmetry of $B$.
>
> *(1) The map $B^\flat$.* Symmetry gives, for every $w \in T_pM$, $B^\flat(w) = B(w, \cdot\,) = B(\cdot\,, w) = B^\sharp(w)$; so $B^\flat = B^\sharp$. With the index $j$ of the last display renamed $i$, and using $H_{ji} = H_{ij}$ (Proposition [[§54 Critical Points and the Hessian#^prop-54-1|§54.1]](2)),
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
> *(d) $\Leftrightarrow$ (e).* (e) includes (d). Conversely, if (d) holds, then (b) holds; $B^\flat$ is defined without charts, and the equivalence (b) $\Leftrightarrow$ (d) holds in every smooth chart at $p$, so $\det H_p \neq 0$ in every chart. (This also follows from $\det H^{(x)}_p = (\det J)^2 \det H^{(y)}_p$ with $\det J \neq 0$, Proposition [[§54 Critical Points and the Hessian#^prop-54-2|§54.2]].)
>
> *(b) $\Leftrightarrow$ (f).* A linear map is injective exactly when it carries a basis to linearly independent vectors (a linear combination of the images is the image of the same combination of the basis vectors). By (1), $B^\flat$ carries the basis $\partial/\partial x^1|_p, \ldots, \partial/\partial x^m|_p$ of $T_pM$ (Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]]) to $d(\partial f/\partial x^1)_p, \ldots, d(\partial f/\partial x^m)_p$.

^pf-54-4

*Uses:* [[§54 Critical Points and the Hessian#^def-54-2|Def. §54.2]], [[§21 Linear Algebra Toolkit#^def-21-4|Def. §21.4]], [[§33 Covectors in Coordinates#^def-33-1|Def. §33.1]], [[§33 Covectors in Coordinates#^cor-33-2|§33.2]], [[§54 Critical Points and the Hessian#^prop-54-1|§54.1]], [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]], [[§21 Linear Algebra Toolkit#^def-21-5|Def. §21.5]], [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]], [[§33 Covectors in Coordinates#^lem-33-1|§33.1]], [[§54 Critical Points and the Hessian#^prop-54-2|§54.2]]

> [!definition] Definition §54.4: Morse Function
> A smooth function $f : M \to \mathbb{R}$ is a **Morse function** if every critical point of $f$ is nondegenerate (Definition [[§54 Critical Points and the Hessian#^def-54-3|§54.3]]). A function without critical points is a Morse function.

^def-54-4

> [!definition] Definition §54.5: Morse Index
> Let $p \in \operatorname{Crit}(f)$. The **index** of $f$ at $p$ (the **Morse index**) is the number of negative eigenvalues, counted with multiplicity, of the Hessian matrix $H_p$ (Definition [[§54 Critical Points and the Hessian#^def-54-1|§54.1]]) in a smooth chart at $p$. It does not depend on the chart.

^def-54-5

> [!proof]+ Proof (not given in this course)
> *(Not from lecture; Sylvester's law is not proved here.)* At a critical point $p$, $H^{(x)}_p = J^{\mathsf T} H^{(y)}_p J$ with $J$ invertible (Proposition [[§54 Critical Points and the Hessian#^prop-54-2|§54.2]]). By *Sylvester's law of inertia*, a real symmetric matrix $H$ and $J^{\mathsf T} H J$, $J$ invertible, have the same numbers of positive, negative and zero eigenvalues. So the number of negative eigenvalues of $H_p$ does not depend on the chart.

^pf-def-54-5

*Uses:* [[§54 Critical Points and the Hessian#^prop-54-2|§54.2]]

> [!remark] Remark: The Morse Lemma
> *(Not from lecture; not proved here.)* For instance $f = x^2 - y^2$ on $\mathbb{R}^2$ has the single critical point $0$, with $H_0 = \mathrm{diag}(2, -2)$: nondegenerate, of index $1$ (Definition [[§54 Critical Points and the Hessian#^def-54-5|§54.5]]). The *Morse lemma* says that near a nondegenerate critical point $p$ of index $\lambda$ there is a chart $(y^1, \ldots, y^m)$ centred at $p$ in which
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

^rem-54-1
