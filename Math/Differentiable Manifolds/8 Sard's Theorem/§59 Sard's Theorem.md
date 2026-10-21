---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 8
section: 59
tags: [differentiable-manifolds, math591]
---
← [[§58 Sets of Measure Zero]] · ↑ [[· 8 Sard's Theorem]] · [[§60 Parametric Transversality]] →

*Stage: analysis — Almost every value of a smooth map is regular.*

> [!remark] Remark: Recall: Regular and Singular Values
> For $F : M \to N$ smooth, $q \in N$ is a regular value if $dF_p$ is onto for every $p \in F^{-1}(q)$ (Definition [[§36 Submersions#^def-36-4|§36.4]]); in particular every $q \notin F(M)$ is a regular value. A value that is not regular is a *singular value* — Uribe's word in Lecture 19; “critical value” in Definition [[§36 Submersions#^def-36-4|§36.4]] and in Lee. Likewise $p \in M$ is a critical (singular) point if $dF_p$ is not onto (Definition [[§36 Submersions#^def-36-3|§36.3]]).

^rem-59-1

> [!theorem] Theorem §59.1: Sard's Theorem
> Let $F : M \to N$ be a smooth map, and
>
> $$
> S = \{\, q \in N : q \text{ is not a regular value of } F \,\},
> $$
>
> the set of singular values. Then $S$ has measure zero in $N$ (Definition [[§58 Sets of Measure Zero#^def-58-2|§58.2]]).
>
> *Lee: Theorem 6.10*

^thm-59-1

> [!remark]- Connections
> - "Measure zero" is Lebesgue-null: outer measure [[§10 Lebesgue Outer Measure#^def-10-4|551 Def. §10.4]]; so the regular values of a smooth map are of full measure (almost every value is regular).

“So almost all values are regular … and this is going to have a lot of applications. Trust me, we're going to see them. They're very cute.”

![[m591-59-1.svg]]

The simplest picture: $f(x) = x^3 - 3x$ on $M = N = \mathbb{R}$. The critical points are $x = \pm 1$, where $f' = 0$, so the singular values are just $f(\pm 1) = \mp 2$, two points, a set of measure zero. Every other $c$ is a regular value: at each of its preimages the slope is nonzero.

> [!proof]+ Proof
> *(Not given in lecture — “it's a big theorem. It's a long proof” — filled in, following Lee's proof of Theorem 6.10.)* Write $m = \dim M$, $n = \dim N$, and $C \subseteq M$ for the set of critical points, so that $S = F(C)$. We prove, by induction on $m$, the statement for all smooth maps between manifolds with $\dim M = m$.
>
> *$m = 0$.* If $n = 0$, every $dF_p$ is onto the zero space, so $S = \varnothing$. If $n \ge 1$, $M$ is countable (a second-countable discrete space), so $S \subseteq F(M)$ is countable; a point of $\mathbb{R}^n$ lies in cubes of arbitrarily small volume, so a countable set has measure zero by Lemma [[§58 Sets of Measure Zero#^lem-58-1|§58.1]](2), in every chart of $N$.
>
> *Reduction to Euclidean space.* Suppose $m \ge 1$ and the theorem holds whenever the domain has dimension $< m$. If $n = 0$ there is nothing to prove, so let $n \ge 1$. Each $p \in M$ has a chart $(U_p, \varphi_p)$ with $F(U_p)$ inside the domain of a chart $(V_p, \psi_p)$ of $N$ (shrink a chart at $p$ into $F^{-1}(V_p)$, by continuity). By Lemma [[§58 Sets of Measure Zero#^lem-58-3|§58.3]] countably many $U_i = U_{p_i}$ cover $M$, so $S = \bigcup_i F(C \cap U_i)$. In the charts, $\hat F_i = \psi_i \circ F \circ \varphi_i^{-1} : \varphi_i(U_i) \to \mathbb{R}^n$, and since charts are diffeomorphisms (Proposition [[§28 Derivations and the Abstract Tangent Space#^prop-28-9|§28.9]]), $p$ is a critical point of $F$ exactly when $\varphi_i(p)$ is one of $\hat F_i$; so $\psi_i\big(F(C \cap U_i)\big)$ is the set of singular values of $\hat F_i$. If that set has measure zero in $\mathbb{R}^n$, then $F(C \cap U_i)$, covered by the single chart $(V_i, \psi_i)$, has measure zero in $N$, and so does the countable union $S$ (Proposition [[§58 Sets of Measure Zero#^prop-58-4|§58.4]]). So it suffices to treat $F : U \to \mathbb{R}^n$, $U \subseteq \mathbb{R}^m$ open, with $C = \{ x : \operatorname{rank} DF(x) < n \}$, where $DF(x)$ is the $n \times m$ Jacobian
>
> $$
> DF(x) = \begin{pmatrix}
> \dfrac{\partial F^1}{\partial x^1}(x) & \cdots & \dfrac{\partial F^1}{\partial x^m}(x) \\
> \vdots & \ddots & \vdots \\
> \dfrac{\partial F^n}{\partial x^1}(x) & \cdots & \dfrac{\partial F^n}{\partial x^m}(x)
> \end{pmatrix} .
> $$ 
>
> *A filtration of $C$.* For $k \ge 1$ let $C_k \subseteq C$ be the set of $x \in C$ at which all partial derivatives of $F$ of orders $1, \ldots, k$ vanish, so $C \supseteq C_1 \supseteq C_2 \supseteq \cdots$. These sets are closed in $U$: $C$ is where all $n \times n$ minors of $DF$ vanish, and $C_k$ is cut out of $C$ by finitely many more continuous functions. Fix an integer $k_0 \ge 1$ with $k_0 > m/n - 1$, that is, $n(k_0 + 1) > m$ (for instance $k_0 = \max(1, \lfloor m/n \rfloor)$; the condition $k_0 \ge 1$ matters when $m < n$). Then
>
> $$
> C = (C \setminus C_1) \cup \bigcup_{k=1}^{k_0 - 1} (C_k \setminus C_{k+1}) \cup C_{k_0},
> $$
>
> and it suffices to show that the image of each piece has measure zero.
>
> *Step 1: $F(C \setminus C_1)$ has measure zero.* If $n = 1$ then $C \setminus C_1 = \varnothing$: a nonzero first partial at $x$ makes the $1 \times m$ matrix $DF(x)$ have rank $1$. Let $n \ge 2$. Replacing $U$ by the open set $U \setminus C_1$, we may assume $C_1 = \varnothing$. Let $a \in C$. Some first partial of $F$ is nonzero at $a$; renumbering coordinates, $\partial F^1/\partial x^1(a) \neq 0$. Then $h(x) = (F^1(x), x^2, \ldots, x^m)$ has invertible derivative at $a$, so by the inverse function theorem (Theorem [[§35 Local Diffeomorphisms#^thm-35-1|§35.1]]) it is a diffeomorphism from an open $W_a \ni a$ onto an open set; choose a closed ball $K_a \ni a$ in $W_a$ with $a$ in its interior. *(Computed; not from lecture.)* The derivative of $h$ is upper triangular,
>
> $$
> Dh(a) = \begin{pmatrix}
> \dfrac{\partial F^1}{\partial x^1}(a) & \dfrac{\partial F^1}{\partial x^2}(a) & \cdots & \dfrac{\partial F^1}{\partial x^m}(a) \\
> 0 & 1 & \cdots & 0 \\
> \vdots & \vdots & \ddots & \vdots \\
> 0 & 0 & \cdots & 1
> \end{pmatrix},
> $$
>
> so $\det Dh(a) = \partial F^1/\partial x^1(a) \neq 0$. In the coordinates $(u, v) = h(x)$, $u \in \mathbb{R}$, $v \in \mathbb{R}^{m-1}$, the map $G = F \circ h^{-1}$ has the form $G(u, v) = (u, G^2(u,v), \ldots, G^n(u, v))$, so
>
> $$
> DG(u, v) = \begin{pmatrix} 1 & 0 \\ \ast & \big(\partial G^i/\partial v^j\big) \end{pmatrix},
> $$
>
> and $(u, v)$ is a critical point of $G$ exactly when the $(n-1) \times (m-1)$ block has rank $< n - 1$. For $c \in \mathbb{R}$ let $G_c(v) = (G^2(c, v), \ldots, G^n(c, v))$, defined on the open set $\{ v : (c, v) \in h(W_a) \} \subseteq \mathbb{R}^{m-1}$; then $(c, v)$ is a critical point of $G$ exactly when $v$ is a critical point of $G_c$. The set $F(C \cap K_a) = G(h(C \cap K_a))$ is compact ($C \cap K_a$ is closed in the compact $K_a$), and its slice at $u = c$ consists of points $(c, G_c(v))$ with $v$ a critical point of $G_c$: it lies in $\{c\} \times$ (the singular values of $G_c$), which has measure zero in $\mathbb{R}^{n-1}$ by the induction hypothesis, $G_c$ having an $(m-1)$-dimensional domain. By Lemma [[§58 Sets of Measure Zero#^lem-58-5|§58.5]], $F(C \cap K_a)$ has measure zero. The interiors of the $K_a$ cover $C$, so countably many do (Lemma [[§58 Sets of Measure Zero#^lem-58-3|§58.3]]), and $F(C \setminus C_1)$ is a countable union of sets of measure zero.
>
> *Step 2: $F(C_k \setminus C_{k+1})$ has measure zero, $k \ge 1$.* Replacing $U$ by $U \setminus C_{k+1}$, we may assume that at each $a \in C_k$ some partial derivative of order $k + 1$ of $F$ is nonzero. So there is a $k$-th order partial derivative $y = \partial^\alpha F^i$, $|\alpha| = k$, with $dy_a \neq 0$. Choose an open $V_a \ni a$ on which $dy \neq 0$. Then $0$ is a regular value of $y|_{V_a}$, and $Y = \{ x \in V_a : y(x) = 0 \}$ is a regular submanifold of $V_a$ of dimension $m - 1$ (Theorem [[§37 Regular Submanifolds#^thm-37-12|§37.12]]). All $k$-th order partials of $F$ vanish on $C_k$, so $C_k \cap V_a \subseteq Y$. At $p \in C_k \cap V_a$, all first partials vanish ($k \ge 1$), so $dF_p = 0$, and $d(F|_Y)_p = dF_p \circ d\iota_p = 0$ is not onto $\mathbb{R}^n$, $n \ge 1$ (chain rule, $\iota : Y \to U$ the inclusion, smooth by Lemma [[§37 Regular Submanifolds#^lem-37-5|§37.5]]). So $F(C_k \cap V_a)$ lies in the set of singular values of $F|_Y : Y \to \mathbb{R}^n$, which has measure zero by the induction hypothesis. Countably many $V_a$ cover $C_k$, so $F(C_k \setminus C_{k+1})$ has measure zero.
>
> *Step 3: $F(C_{k_0})$ has measure zero.* By the reduction in the proof of Lemma [[§58 Sets of Measure Zero#^lem-58-2|§58.2]], it suffices to show that $F(C_{k_0} \cap E)$ has measure zero for a closed cube $E \subseteq U$, of side $R$. Let $A > 0$ bound the absolute values of all partial derivatives of order $k_0 + 1$ of $F$ on $E$ (continuous functions on a compact set; taking $A > 0$ keeps the cubes below nondegenerate). If $x' \in C_{k_0} \cap E$ and $x \in E$, Taylor's theorem along the segment from $x'$ to $x$, which lies in the convex set $E$, applied to each component $F^i$, has no terms of orders $1, \ldots, k_0$, so
>
> $$
> |F^i(x) - F^i(x')| \le \sum_{|\beta| = k_0 + 1} \frac{A}{\beta!}\, |(x - x')^\beta| \le A'\, \|x - x'\|_\infty^{k_0 + 1},
> $$
>
> with $A'$ depending only on $A$, $k_0$ and $m$. Divide $E$ into $K^m$ closed cubes $E_1, \ldots, E_{K^m}$ of side $R/K$. If $E_j$ contains a point $x'_j \in C_{k_0}$, then $F(E_j)$ lies in the closed cube of side $2A'(R/K)^{k_0 + 1}$ centred at $F(x'_j)$. So $F(C_{k_0} \cap E)$ lies in at most $K^m$ cubes of total volume
>
> $$
> K^m \big(2A'\big)^n \Big(\frac{R}{K}\Big)^{n(k_0 + 1)} = \big(2A'\big)^n R^{\,n(k_0 + 1)}\, K^{\,m - n(k_0 + 1)} ,
> $$
>
> which tends to $0$ as $K \to \infty$ because $n(k_0 + 1) > m$. By Lemma [[§58 Sets of Measure Zero#^lem-58-1|§58.1]](3), $F(C_{k_0} \cap E)$ has measure zero.
>
> Steps 1–3 cover all of $C$, which completes the induction.

^pf-59-1

*Uses:* [[§58 Sets of Measure Zero#^lem-58-1|§58.1]], [[§58 Sets of Measure Zero#^lem-58-3|§58.3]], [[§28 Derivations and the Abstract Tangent Space#^prop-28-9|§28.9]], [[§58 Sets of Measure Zero#^prop-58-4|§58.4]], [[§35 Local Diffeomorphisms#^thm-35-1|§35.1]], [[§58 Sets of Measure Zero#^lem-58-5|§58.5]], [[§37 Regular Submanifolds#^thm-37-12|§37.12]], [[§37 Regular Submanifolds#^lem-37-5|§37.5]], [[§58 Sets of Measure Zero#^lem-58-2|§58.2]]

> [!theorem] Corollary §59.2: Maps from Lower Dimension
> If $F : M \to N$ is smooth and $\dim M < \dim N$, then the regular values of $F$ are exactly the points of $N \setminus F(M)$, and $F(M)$ has measure zero in $N$.
>
> *Lee: Corollary 6.11*

^cor-59-2

> [!remark]- Connections
> - A measure-theory relative: the graph of a measurable function has measure zero, [[§26 Applications of Tonelli's Theorem#^cor-26-4|551 §26.4]].

> [!proof]+ Proof
> *(Lecture 19.)* “By linear algebra, no point in the image can be a regular value, because … the dimensions don't work out”: for $p \in M$, the image of $dF_p : T_pM \to T_{F(p)}N$ has dimension at most $\dim M < \dim N$ (Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-9|§29.9]]), so $dF_p$ is never onto. So the regular values are exactly the points with empty preimage — “this is a vacuous thing” — and $F(M)$ is the set of singular values, of measure zero by Sard's theorem.

^pf-59-2

*Uses:* [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-9|§29.9]]

“That's one observation, but there will be many other nice applications of this.” For instance, a smooth curve $\gamma : \mathbb{R} \to \mathbb{R}^2$ never fills an open set of the plane: its image has measure zero, and so does every subset of it (Lemma [[§58 Sets of Measure Zero#^lem-58-1|§58.1]](1)), while an open set does not (Lemma [[§58 Sets of Measure Zero#^lem-58-1|§58.1]](4)) — in contrast with continuous space-filling curves.

**Transcription note (Lecture 19).** Page 50 of the handwritten notes states the image lemma for “$F : U \to \mathbb{R}^n$, $U \subseteq \mathbb{R}^m$ open”. As written, with $m$ unrestricted, it is false for $m > n$: the projection $\mathbb{R}^2 \to \mathbb{R}$, $(x, y) \mapsto x$, maps the $x$-axis, of measure zero in $\mathbb{R}^2$, onto $\mathbb{R}$. Lemma [[§58 Sets of Measure Zero#^lem-58-2|§58.2]] takes $m = n$, as Lee does and as the application to transition maps needs. (For $m < n$ the conclusion holds for every $S$, by Corollary [[§59 Sard's Theorem#^cor-59-2|§59.2]].)
