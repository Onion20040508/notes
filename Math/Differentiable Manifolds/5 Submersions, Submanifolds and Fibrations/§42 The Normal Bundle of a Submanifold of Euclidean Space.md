---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 5
section: 42
tags: [differentiable-manifolds, math591]
---
← [[§41 Examples of Fibrations]] · ↑ [[· 5 Submersions, Submanifolds and Fibrations]] · [[§43 Immersions]] →

*Stage: bundles — The vectors perpendicular to a submanifold of $\mathbb{R}^n$, collected into an $n$-dimensional manifold that fibres over it; its endpoint map and focal points; and, through the dot product, normal vectors as conormal covectors.*

*Assignment 5, Problem 5.* A submanifold $M \subseteq \mathbb{R}^n$ has, at each of its points, the vectors perpendicular to it; collecting all pairs (point, perpendicular vector) gives the *normal bundle*. Part (a) of the problem shows that it is a manifold of dimension $n$, whatever the dimension of $M$; part (b) introduces the endpoint map and finds the focal points of a parabola. The normal bundle is the Euclidean shadow of the conormal bundle (the remark *The Conormal Bundle* in [[§39 Transversality and Lagrange Multipliers|§39]]; Definition [[§55 Morse Functions and the Zero Section#^def-55-1|§55.1]], later, in [[§54 Critical Points and the Hessian|§54]]): Uribe's “if we had a metric … this would be the normal space” (the remark *No Normal Vectors Without a Metric* in [[§37 Regular Submanifolds|§37]]) is realized here by the dot product of $\mathbb{R}^n$, and Proposition [[§42 The Normal Bundle of a Submanifold of Euclidean Space#^prop-42-3|§42.3]] makes the identification explicit. That the projection to $M$ is a fibration (Proposition [[§42 The Normal Bundle of a Submanifold of Euclidean Space#^prop-42-2|§42.2]]) — which is why the normal bundle stands next to the examples of fibrations ([[§41 Examples of Fibrations|§41]]) — and what focal points mean geometrically (the remark *Focal Points Are Centres of Curvature* below), are added.

*Three meanings of “normal”.* *(Not from lecture.)* For a regular submanifold $S$ of a manifold $M$ and $p \in S$, three spaces in these notes carry the name:

1. the *conormal space* $N_pS \subseteq T_p^{\ast}M$, the covectors that vanish on $\iota_{\ast p}(T_pS)$ (Definition [[§37 Regular Submanifolds#^def-37-4|§37.4]], [[§37 Regular Submanifolds|§37]], Lecture 12) — intrinsic, defined without any metric;
2. the *normal space* $T_pM/\iota_{\ast p}(T_pS)$, a quotient (Definition [[§39 Transversality and Lagrange Multipliers#^def-39-2|§39.2]], [[§39 Transversality and Lagrange Multipliers|§39]]) — also intrinsic; $N_pS$ consists of the covectors that vanish on $\iota_{\ast p}(T_pS)$, which are the same as the linear forms on this quotient;
3. for a submanifold of Euclidean space — in this section, following the assignment, the submanifold is called $M$ and the ambient space is $\mathbb{R}^n$ — the *Euclidean normal space* $(T^{\mathrm{geo}}_pM)^\perp \subseteq \mathbb{R}^n$ of vectors perpendicular to $M$ (Definition [[§42 The Normal Bundle of a Submanifold of Euclidean Space#^def-42-1|§42.1]]), studied here; it needs the dot product.

With the dot product the three agree: $(T^{\mathrm{geo}}_pM)^\perp$ is a complement of $T^{\mathrm{geo}}_pM$ in $\mathbb{R}^n$, so it maps isomorphically onto the quotient $\mathbb{R}^n/T^{\mathrm{geo}}_pM$, which is the normal space $T_p\mathbb{R}^n/\iota_{\ast p}(T_pM)$ under $w \mapsto D_w|_p$; and $v \mapsto \xi_v$ maps it isomorphically onto the conormal space $N_pM$ (Proposition [[§42 The Normal Bundle of a Submanifold of Euclidean Space#^prop-42-3|§42.3]]).

## The Normal Bundle

*Setting.* Throughout this section $M \subseteq \mathbb{R}^n$ is a regular submanifold of dimension $m < n$, that is, of codimension $n - m$ (Definition [[§37 Regular Submanifolds#^def-37-2|§37.2]]), and $v \cdot w = \sum_l v^l w^l$ is the dot product of $\mathbb{R}^n$. Tangent spaces are the geometric ones: for $p \in M$, $T^{\mathrm{geo}}_pM \subseteq \mathbb{R}^n$ is the set of velocities $\gamma'(0)$ of smooth curves $\gamma$ in $\mathbb{R}^n$ with $\gamma(0) = p$ that stay in $M$ (Definition [[§25 The Geometric Tangent Space#^def-25-1|§25.1]], whose formula makes sense verbatim for any subset of $\mathbb{R}^n$). This is the assignment's “$T_pM$ identified with the ambient tangent space”; its identification with $\iota_{\ast p}(T_pM)$ is the remark *The Tangent Spaces Match* in [[§37 Regular Submanifolds|§37]]. It is computed in an adapted chart: $(U, \varphi = (x^1, \ldots, x^n))$ is a smooth chart of $\mathbb{R}^n$ adapted to $M$ (Definition [[§37 Regular Submanifolds#^def-37-3|§37.3]]), so that

$$
U \cap M = \{\, q \in U : x^{m+1}(q) = \cdots = x^n(q) = 0 \,\},
$$

and

$$
G = (G^1, \ldots, G^{n-m}) = (x^{m+1}, \ldots, x^n) : U \to \mathbb{R}^{n-m}, \qquad J(q) = G'(q) \quad (q \in U),
$$

the $(n-m) \times n$ Jacobian of $G$ in the standard coordinates of $\mathbb{R}^n$, whose $s$-th row is the gradient $\nabla G^s(q)$ (Definitions [[§7 The Regular Value Theorem#^def-7-1|§7.1]] and [[§33 Covectors in Coordinates#^def-33-2|§33.2]]). Every point of $M$ lies in such a chart (Definition [[§37 Regular Submanifolds#^def-37-2|§37.2]]). The facts about such a chart that are used throughout are collected in Lemma [[§37 Regular Submanifolds#^lem-37-10|§37.10]] ([[§37 Regular Submanifolds|§37]]):

1. $\varphi'(q)$ is invertible and $J(q)$ has rank $n - m$, for every $q \in U$;
2. $T^{\mathrm{geo}}_qM = \ker J(q)$, of dimension $m$, for every $q \in U \cap M$;
3. the vectors $X_j(q) = \dfrac{\partial \varphi^{-1}}{\partial r^j}\big(\varphi(q)\big)$, $j = 1, \ldots, m$, form a basis of $T^{\mathrm{geo}}_qM$, for every $q \in U \cap M$;
4. the gradients $\nabla G^1(q), \ldots, \nabla G^{n-m}(q)$ form a basis of the orthogonal complement $(T^{\mathrm{geo}}_qM)^\perp$, for every $q \in U \cap M$.

> [!definition] Definition §42.1: Normal Bundle
> Let $M \subseteq \mathbb{R}^n$ be a regular submanifold of dimension $m < n$. For $p \in M$ write
>
> $$
> (T^{\mathrm{geo}}_pM)^\perp = \{\, v \in \mathbb{R}^n : v \cdot w = 0 \text{ for all } w \in T^{\mathrm{geo}}_pM \,\}
> $$
>
> for the orthogonal complement of the geometric tangent space with respect to the dot product. The **normal bundle** of $M$ is
>
> $$
> \mathcal{N} = \{\, (p, v) \in \mathbb{R}^n \times \mathbb{R}^n : p \in M \text{ and } v \in (T^{\mathrm{geo}}_pM)^\perp \,\} \subseteq \mathbb{R}^{2n},
> $$
>
> with the **projection** $\pi : \mathcal{N} \to M$, $\pi(p, v) = p$. Its fibre over $p$ is $\pi^{-1}(p) = \{p\} \times (T^{\mathrm{geo}}_pM)^\perp$, a copy of the normal space at $p$.
>
> *Lee: Ch. 6, Tubular Neighborhoods*

^def-42-1

> [!theorem] Proposition §42.1: The Normal Bundle Is a Submanifold
> $\mathcal{N}$ is a regular submanifold of $\mathbb{R}^{2n} = \mathbb{R}^n \times \mathbb{R}^n$ of codimension $n$, hence a smooth manifold of dimension $n$ with the induced structure (Proposition [[§37 Regular Submanifolds#^prop-37-3|§37.3]]).
>
> *Lee: Ch. 6, Tubular Neighborhoods*

^prop-42-1

> [!proof]+ Proof
> *(Assignment 5, Problem 5(a); the student's route, following the hint. Two steps are completed: that the first $m$ coordinate vectors span the tangent space is proved, in Lemma [[§37 Regular Submanifolds#^lem-37-10|§37.10]](3) (cited in Step 1(ii)), and the Jacobian, which the hint computes in the coordinates $(x, v)$, is converted to the standard coordinates of $\mathbb{R}^{2n}$, so that the external description of [[§20 Manifolds in Euclidean Space|§20]] applies.)* By the last statement of Proposition [[§37 Regular Submanifolds#^prop-37-9|§37.9]], applied to $X = \mathcal{N} \subseteq \mathbb{R}^{2n} = \mathbb{R}^{n+k}$ with $k = n$, it suffices to describe $\mathcal{N}$ externally near each of its points (Definition [[§20 Manifolds in Euclidean Space#^def-20-1|§20.1]]): for each $(p_0, v_0) \in \mathcal{N}$ we need an open $W \ni (p_0, v_0)$ in $\mathbb{R}^{2n}$ and a smooth $F : W \to \mathbb{R}^n$ having $\vec 0$ as a regular value with $\mathcal{N} \cap W = F^{-1}(\vec 0)$. Fix $(p_0, v_0) \in \mathcal{N}$. Then $p_0 \in M$, so there is an adapted chart $(U, \varphi = (x^1, \ldots, x^n))$ at $p_0$ as in the Setting; put $W = U \times \mathbb{R}^n$, open in $\mathbb{R}^{2n}$ as a product of open sets, and containing $(p_0, v_0)$.
>
> *Step 1: the vector fields $X_j$.* For $q \in U$ and $j = 1, \ldots, n$ put
>
> $$
> X_j(q) = \frac{\partial \varphi^{-1}}{\partial r^j}\big(\varphi(q)\big) \in \mathbb{R}^n ,
> $$
>
> the $j$-th column of the Jacobian $(\varphi^{-1})'(\varphi(q))$, with components $X_j^l(q)$, $l = 1, \ldots, n$. This is the hint's coordinate field $\partial/\partial x^j$ “regarded as a vector field on $U$ in the sense of Calc III”: the velocity of the $j$-th coordinate line $t \mapsto \varphi^{-1}(\varphi(q) + t e_j)$ at $t = 0$, by the chain rule. Each $X_j^l$ is smooth on $U$, as the composite of the smooth $\varphi$ with the partial derivative $\partial(\varphi^{-1})^l/\partial r^j$ of the smooth map $\varphi^{-1}$.
>
> 1. [(i)] *$X_1(q), \ldots, X_n(q)$ form a basis of $\mathbb{R}^n$, for every $q \in U$.* By Lemma [[§37 Regular Submanifolds#^lem-37-10|§37.10]](1), $\varphi'(q)$ is invertible, and the chain rule applied to $\varphi \circ \varphi^{-1} = \mathrm{id}_{\varphi(U)}$ at $\varphi(q)$ gives $\varphi'(q)\,(\varphi^{-1})'(\varphi(q)) = I_n$; so $(\varphi^{-1})'(\varphi(q))$ is the inverse of $\varphi'(q)$, hence invertible, and its columns $X_1(q), \ldots, X_n(q)$ form a basis of $\mathbb{R}^n$. In particular $X_1(q), \ldots, X_m(q)$ are linearly independent at every $q \in U$, not only on $M$; this is what Step 4 uses.
> 2. [(ii)] *For $q \in U \cap M$, $X_1(q), \ldots, X_m(q)$ form a basis of $T^{\mathrm{geo}}_qM$.* This is Lemma [[§37 Regular Submanifolds#^lem-37-10|§37.10]](3), for the chart $(U, \varphi)$ and the point $q$:
>
> $$
> T^{\mathrm{geo}}_qM = \operatorname{Span}\{X_1(q), \ldots, X_m(q)\}.
> $$
>
> The submitted solution quotes this span from the computation of Problem 2 for the inclusion of a regular submanifold in an adapted chart: $\iota_{\ast q}(T_qM) = \operatorname{Span}\{\partial/\partial x^1|_q, \ldots, \partial/\partial x^m|_q\}$ (Proposition [[§37 Regular Submanifolds#^prop-37-6|§37.6]]), read in $\mathbb{R}^n$ through the remark *The Tangent Spaces Match* in [[§37 Regular Submanifolds|§37]].
>
> *Step 2: the map $F$.* Define $F : W = U \times \mathbb{R}^n \to \mathbb{R}^n$ by
>
> $$
> F(q, v) = \big( x^{m+1}(q), \ldots, x^n(q),\ y^1(q, v), \ldots, y^m(q, v) \big), \qquad y^j(q, v) = X_j(q) \cdot v = \sum_{l=1}^n X_j^l(q)\, v^l .
> $$
>
> It is smooth: its first $n - m$ components are components of the smooth chart $\varphi$, and each $y^j$ is a sum of products of the smooth functions $X_j^l(q)$ and the coordinates $v^l$.
>
> *Step 3: $F^{-1}(\vec 0) = \mathcal{N} \cap W$.* For $(q, v) \in W$,
>
> $$
> \begin{aligned}F(q, v) = \vec 0 &\iff x^{m+s}(q) = 0 \ (1 \le s \le n - m) \ \text{ and } \ X_j(q) \cdot v = 0 \ (1 \le j \le m) \\
> &\iff q \in U \cap M \ \text{ and } \ X_j(q) \cdot v = 0 \ (1 \le j \le m) \\
> &\iff q \in U \cap M \ \text{ and } \ v \in (T^{\mathrm{geo}}_qM)^\perp \\
> &\iff (q, v) \in \mathcal{N} \cap W .\end{aligned}
> $$
>
> The first equivalence is the definition of $F$. The second is the adapted-chart description $U \cap M = \{x^{m+1} = \cdots = x^n = 0\}$, with $q \in U$. For the third, $q \in U \cap M$, so $T^{\mathrm{geo}}_qM = \operatorname{Span}\{X_1(q), \ldots, X_m(q)\}$ by Step 1(ii); a vector $v$ is orthogonal to every element $\sum_j c_j X_j(q)$ of this span if and only if it is orthogonal to each $X_j(q)$, because $v \cdot \sum_j c_j X_j(q) = \sum_j c_j\, \big(v \cdot X_j(q)\big)$ by linearity of the dot product (“if” by this formula, “only if” by taking $c = e_j$). The fourth is Definition [[§42 The Normal Bundle of a Submanifold of Euclidean Space#^def-42-1|§42.1]], together with $q \in U$ and $W = U \times \mathbb{R}^n$.
>
> *Step 4: the Jacobian in the coordinates $(x, v)$ (the submitted computation).* On $W$ use the coordinates $(x, v) = (x^1(q), \ldots, x^n(q), v^1, \ldots, v^n)$, i.e. the map $\varphi \times \mathrm{id} : W \to \varphi(U) \times \mathbb{R}^n$, $(q, v) \mapsto (\varphi(q), v)$, a bijection with inverse $\varphi^{-1} \times \mathrm{id}$; in them the $x$'s and the $v$'s are independent variables. The coordinate representation of $F$ is $\tilde F = F \circ (\varphi^{-1} \times \mathrm{id}) : \varphi(U) \times \mathbb{R}^n \to \mathbb{R}^n$,
>
> $$
> \tilde F(r, v) = \Big( r^{m+1}, \ldots, r^n,\ \tilde X_1(r) \cdot v, \ldots, \tilde X_m(r) \cdot v \Big), \qquad \tilde X_j(r) = \frac{\partial \varphi^{-1}}{\partial r^j}(r),
> $$
>
> using $x^{m+s}(\varphi^{-1}(r)) = r^{m+s}$ and $X_j(\varphi^{-1}(r)) = \tilde X_j(r)$. Its partial derivatives at $(r, v)$, for $1 \le i, l \le n$, are as follows.
> - The component $r^{m+s}$ ($1 \le s \le n - m$) depends only on $r$, and is the $(m+s)$-th coordinate:
>
> $$
> \frac{\partial r^{m+s}}{\partial r^i} = \delta^{m+s}_i, \qquad \frac{\partial r^{m+s}}{\partial v^l} = 0 .
> $$
>
> - The component $\tilde y^j(r, v) = \tilde X_j(r) \cdot v = \sum_l \tilde X_j^l(r)\, v^l$: differentiating each term by the product rule, with $v$ independent of $r$ and $\tilde X_j$ independent of $v$,
>
> $$
> \frac{\partial \tilde y^j}{\partial r^i} = \sum_{l=1}^n v^l\, \frac{\partial^2 (\varphi^{-1})^l}{\partial r^i\, \partial r^j}(r), \qquad \frac{\partial \tilde y^j}{\partial v^l} = \tilde X_j^l(r) .
> $$
>
> Grouping the columns as $(r^1, \ldots, r^m)$, $(r^{m+1}, \ldots, r^n)$, $(v^1, \ldots, v^n)$, the $n \times 2n$ Jacobian at $(\varphi(q), v)$ is therefore
>
> $$
> \tilde F'\big(\varphi(q), v\big) = \begin{pmatrix} 0_{(n-m) \times m} & I_{n-m} & 0_{(n-m) \times n} \\ \ast & \ast & X(q) \end{pmatrix},
> $$
>
> where the entries $\ast$ are the second-derivative sums above, and $X(q)$ is the $m \times n$ matrix whose $j$-th row is $X_j(q)^{\mathsf T} = \big(X_j^1(q), \ldots, X_j^n(q)\big)$ (recall $\tilde X_j(\varphi(q)) = X_j(q)$).
> Written out, with the partials of the $\tilde y^j$ taken at $(\varphi(q), v)$,
>
> $$
> \tilde F'\big(\varphi(q), v\big) = \left(\begin{array}{ccc|ccc|ccc} 0 & \cdots & 0 & 1 & \cdots & 0 & 0 & \cdots & 0 \\ \vdots & & \vdots & \vdots & \ddots & \vdots & \vdots & & \vdots \\ 0 & \cdots & 0 & 0 & \cdots & 1 & 0 & \cdots & 0 \\ \hline \dfrac{\partial \tilde y^1}{\partial r^1} & \cdots & \dfrac{\partial \tilde y^1}{\partial r^m} & \dfrac{\partial \tilde y^1}{\partial r^{m+1}} & \cdots & \dfrac{\partial \tilde y^1}{\partial r^n} & X_1^1(q) & \cdots & X_1^n(q) \\ \vdots & & \vdots & \vdots & & \vdots & \vdots & & \vdots \\ \dfrac{\partial \tilde y^m}{\partial r^1} & \cdots & \dfrac{\partial \tilde y^m}{\partial r^m} & \dfrac{\partial \tilde y^m}{\partial r^{m+1}} & \cdots & \dfrac{\partial \tilde y^m}{\partial r^n} & X_m^1(q) & \cdots & X_m^n(q) \end{array}\right) ,
> $$
>
> with $n - m$ rows above the line and $m$ below, and $m$, $n - m$, $n$ columns in the three groups.
>
> *It has rank $n$.* Write the $s$-th of the first $n - m$ rows as $(0, e_s, 0)$, with $e_s \in \mathbb{R}^{n-m}$, and the $j$-th of the last $m$ rows as $(\ast, \ast, X_j(q)^{\mathsf T})$, and suppose a linear combination of the rows vanishes:
>
> $$
> \sum_{s=1}^{n-m} c_s\, (0, e_s, 0) + \sum_{j=1}^m b_j\, \big(\ast, \ast, X_j(q)^{\mathsf T}\big) = 0, \qquad c_s, b_j \in \mathbb{R}.
> $$
>
> In the last $n$ columns the first $n - m$ rows have zeros, so these columns give $\sum_j b_j X_j(q)^{\mathsf T} = 0$; since $X_1(q), \ldots, X_m(q)$ are linearly independent (Step 1(i)), $b_1 = \cdots = b_m = 0$. With all $b_j = 0$, columns $m+1, \ldots, n$ give $\sum_s c_s e_s = 0$, so $c_1 = \cdots = c_{n-m} = 0$. So the $n$ rows are linearly independent, and $\tilde F'(\varphi(q), v)$ has rank $n$ (Definition [[§7 The Regular Value Theorem#^def-7-2|§7.2]]).
>
> *Step 5: back to the standard coordinates.* On $W$, $F = \tilde F \circ (\varphi \times \mathrm{id})$, and $\varphi \times \mathrm{id}$ is smooth with the block-diagonal Jacobian
>
> $$
> (\varphi \times \mathrm{id})'(q, v) = \begin{pmatrix} \varphi'(q) & 0 \\ 0 & I_n \end{pmatrix},
> $$
>
> which is invertible, with inverse $\operatorname{diag}\big((\varphi^{-1})'(\varphi(q)), I_n\big)$, by Step 1(i) (Lemma [[§37 Regular Submanifolds#^lem-37-10|§37.10]](1) and the chain rule). By the chain rule,
>
> $$
> F'(q, v) = \tilde F'\big(\varphi(q), v\big)\, (\varphi \times \mathrm{id})'(q, v) .
> $$
>
> Multiplying on the right by an invertible matrix does not change the image: $\operatorname{im}(AB) = A(\operatorname{im} B) = A(\mathbb{R}^{2n}) = \operatorname{im} A$ when $B$ is onto. So $F'(q, v)$ has the same image as $\tilde F'(\varphi(q), v)$, which is all of $\mathbb{R}^n$ by Step 4. Thus every point of $W$ is a regular point of $F$ (Definition [[§7 The Regular Value Theorem#^def-7-3|§7.3]]), and in particular $\vec 0$ is a regular value of $F$ on $W$ (Definition [[§7 The Regular Value Theorem#^def-7-4|§7.4]], applied on the open set $W$ as in Corollary [[§7 The Regular Value Theorem#^cor-7-4|§7.4]]).
>
> *Step 6: conclusion.* By Steps 2, 3 and 5, $W$ is an open neighbourhood of $(p_0, v_0)$ in $\mathbb{R}^{2n}$, $F : W \to \mathbb{R}^n$ is smooth with $\vec 0$ as a regular value, and $\mathcal{N} \cap W = F^{-1}(\vec 0)$: $\mathcal{N}$ is described externally near $(p_0, v_0)$ (Definition [[§20 Manifolds in Euclidean Space#^def-20-1|§20.1]], with $n + k = 2n$ and $k = n$). As $(p_0, v_0) \in \mathcal{N}$ was arbitrary, Proposition [[§37 Regular Submanifolds#^prop-37-9|§37.9]] gives that $\mathcal{N}$ is a regular submanifold of $\mathbb{R}^{2n}$ of codimension $n$, and by Proposition [[§37 Regular Submanifolds#^prop-37-3|§37.3]] it is a smooth manifold of dimension $2n - n = n$.
>
> *The submitted ending.* The solution as submitted concludes without leaving the coordinates $(x, v)$. By Theorem [[§30 The Differential in Coordinates#^thm-30-2|§30.2]], $\tilde F'(\varphi(q), v)$ is the matrix of $F_{\ast(q,v)}$, so by Step 4 $F$ is a submersion on the open submanifold $W$ of $\mathbb{R}^{2n}$, and the regular value theorem for manifolds (Theorem [[§38 The Regular Value Theorem for Manifolds#^thm-38-2|§38.2]]) makes $F^{-1}(\vec 0) = \mathcal{N} \cap W$ a regular submanifold of $W$ of codimension $n$. An adapted chart $(W', \theta)$ of $W$ at $(p_0, v_0)$ is a smooth chart of $\mathbb{R}^{2n}$ (Proposition [[§17 Differentiable Structures#^prop-17-7|§17.7]](2)), and since $W' \subseteq W$,
>
> $$
> W' \cap \mathcal{N} = W' \cap \mathcal{N} \cap W = W' \cap F^{-1}(\vec 0) ,
> $$
>
> so it is adapted to $\mathcal{N}$ in $\mathbb{R}^{2n}$ (Definition [[§37 Regular Submanifolds#^def-37-3|§37.3]]), with $n$ vanishing coordinates. The two endings are the same argument: Proposition [[§37 Regular Submanifolds#^prop-37-9|§37.9]] packages the passage from a regular level set to an adapted chart.

^pf-42-1

*Uses:* [[§37 Regular Submanifolds#^lem-37-10|§37.10]], [[§37 Regular Submanifolds#^prop-37-9|§37.9]], [[§20 Manifolds in Euclidean Space#^def-20-1|Def. §20.1]], [[§37 Regular Submanifolds#^prop-37-6|§37.6]], [[§42 The Normal Bundle of a Submanifold of Euclidean Space#^def-42-1|Def. §42.1]], [[§7 The Regular Value Theorem#^def-7-2|Def. §7.2]], [[§7 The Regular Value Theorem#^def-7-3|Def. §7.3]], [[§7 The Regular Value Theorem#^def-7-4|Def. §7.4]], [[§7 The Regular Value Theorem#^cor-7-4|§7.4]], [[§37 Regular Submanifolds#^prop-37-3|§37.3]], [[§30 The Differential in Coordinates#^thm-30-2|§30.2]], [[§38 The Regular Value Theorem for Manifolds#^thm-38-2|§38.2]], [[§17 Differentiable Structures#^prop-17-7|§17.7]], [[§37 Regular Submanifolds#^def-37-3|Def. §37.3]]

> [!theorem] Proposition §42.2: The Normal Bundle Is a Fibration
> Let $(U, \varphi = (x^1, \ldots, x^n))$ be a chart of $\mathbb{R}^n$ adapted to $M$, with $G = (x^{m+1}, \ldots, x^n)$ and $J(q) = G'(q)$ as in the Setting, and let $\mathcal{N}$ carry the smooth structure of Proposition [[§42 The Normal Bundle of a Submanifold of Euclidean Space#^prop-42-1|§42.1]].
>
> 1. For $q \in U \cap M$ the gradients $\nabla G^1(q), \ldots, \nabla G^{n-m}(q)$, the rows of $J(q)$, form a basis of $(T^{\mathrm{geo}}_qM)^\perp$; and for every $q \in U$ the $(n-m) \times (n-m)$ matrix $J(q) J(q)^{\mathsf T}$ is invertible.
> 2. The map
>
> $$
> \Phi_U : \pi^{-1}(U \cap M) \longrightarrow (U \cap M) \times \mathbb{R}^{n-m}, \qquad \Phi_U(q, v) = \Big(q,\ \big(J(q) J(q)^{\mathsf T}\big)^{-1} J(q)\, v\Big),
> $$
>
> is a diffeomorphism, with inverse $(q, c) \mapsto \big(q, J(q)^{\mathsf T} c\big)$, and $\mathrm{pr}_1 \circ \Phi_U = \pi|_{\pi^{-1}(U \cap M)}$. On each fibre $\pi^{-1}(q) = \{q\} \times (T^{\mathrm{geo}}_qM)^\perp$ it is a linear isomorphism $(T^{\mathrm{geo}}_qM)^\perp \to \mathbb{R}^{n-m}$.
> 3. $\pi : \mathcal{N} \to M$ is a fibration with fibre $\mathbb{R}^{n-m}$ (Definition [[§40 Fibrations#^def-40-1|§40.1]]), the maps $\Phi_U$ of (2), over all adapted charts, being local trivializations.

^prop-42-2

> [!proof]+ Proof
> *(Not from the assignment; filled in.)* Throughout, $M$ carries its induced structure as a regular submanifold of $\mathbb{R}^n$, $U \cap M$ is open in $M$ (subspace topology, $U$ being open in $\mathbb{R}^n$) and is an open submanifold of $M$ (Definition [[§37 Regular Submanifolds#^def-37-1|§37.1]]), and $(U \cap M) \times \mathbb{R}^{n-m}$ is a product manifold (Definition [[§19 Smooth Functions and Smooth Maps#^def-19-7|§19.7]]).
>
> *$\pi$ is smooth, and $\pi^{-1}(U \cap M)$.* Let $\iota_{\mathcal{N}} : \mathcal{N} \to \mathbb{R}^{2n}$ be the inclusion, smooth by Lemma [[§37 Regular Submanifolds#^lem-37-5|§37.5]](1), and $\mathrm{pr} : \mathbb{R}^{2n} \to \mathbb{R}^n$, $\mathrm{pr}(p, v) = p$, which is linear, hence smooth. Then $\pi = \mathrm{pr} \circ \iota_{\mathcal{N}}$ as maps into $\mathbb{R}^n$, smooth as a composite (Lemma [[§19 Smooth Functions and Smooth Maps#^lem-19-5|§19.5]]); its values lie in $M$ by Definition [[§42 The Normal Bundle of a Submanifold of Euclidean Space#^def-42-1|§42.1]], so $\pi$ is smooth as a map into $M$ (Lemma [[§37 Regular Submanifolds#^lem-37-5|§37.5]](2)). Next,
>
> $$
> \mathcal{N}_U := \pi^{-1}(U \cap M) = \{\, (q, v) \in \mathcal{N} : q \in U \,\} = \mathcal{N} \cap (U \times \mathbb{R}^n),
> $$
>
> the first equality because $\pi(q, v) = q$ and $q \in M$ for every $(q, v) \in \mathcal{N}$. It is open in $\mathcal{N}$, being the intersection of $\mathcal{N}$ with an open set of $\mathbb{R}^{2n}$, and is an open submanifold of $\mathcal{N}$.
>
> *(1) The gradients span the normal space.* Fix $q \in U \cap M$. By Lemma [[§37 Regular Submanifolds#^lem-37-10|§37.10]](4), for the chart $(U, \varphi)$ and the point $q$, the $n - m$ gradients $\nabla G^1(q), \ldots, \nabla G^{n-m}(q)$ — the rows of $J(q)$ (Definition [[§7 The Regular Value Theorem#^def-7-1|§7.1]]) — form a basis of $(T^{\mathrm{geo}}_qM)^\perp$; in particular $\dim (T^{\mathrm{geo}}_qM)^\perp = n - m$. In matrix form, since $J(q)^{\mathsf T} c = \sum_s c^s\, \nabla G^s(q)$ for $c = (c^1, \ldots, c^{n-m}) \in \mathbb{R}^{n-m}$ (the columns of $J(q)^{\mathsf T}$ are the rows of $J(q)$):
>
> $$
> (T^{\mathrm{geo}}_qM)^\perp = \{\, J(q)^{\mathsf T} c : c \in \mathbb{R}^{n-m} \,\}, \qquad c \mapsto J(q)^{\mathsf T} c \ \text{ injective}. \tag{$\flat$}
> $$
>
> *The Gram matrix.* Now let $q \in U$ be arbitrary; $J(q)$ still has rank $n - m$ (Lemma [[§37 Regular Submanifolds#^lem-37-10|§37.10]](1)), so $c \mapsto J(q)^{\mathsf T} c$ is injective (its columns are the independent rows of $J(q)$). If $J(q) J(q)^{\mathsf T} c = 0$, then
>
> $$
> 0 = c \cdot \big(J(q) J(q)^{\mathsf T} c\big) = c^{\mathsf T} J(q) J(q)^{\mathsf T} c = \big(J(q)^{\mathsf T} c\big) \cdot \big(J(q)^{\mathsf T} c\big) = \big|J(q)^{\mathsf T} c\big|^2 ,
> $$
>
> so $J(q)^{\mathsf T} c = 0$, and $c = 0$ by injectivity. A square matrix with zero kernel is invertible (Proposition [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]](1)). ($J J^{\mathsf T}$ is the Gram matrix of the gradients: its $(s, s')$ entry is $\nabla G^s(q) \cdot \nabla G^{s'}(q)$.)
> Written out,
>
> $$
> J(q) J(q)^{\mathsf T} = \begin{pmatrix} \nabla G^1(q) \cdot \nabla G^1(q) & \cdots & \nabla G^1(q) \cdot \nabla G^{n-m}(q) \\ \vdots & \ddots & \vdots \\ \nabla G^{n-m}(q) \cdot \nabla G^1(q) & \cdots & \nabla G^{n-m}(q) \cdot \nabla G^{n-m}(q) \end{pmatrix} .
> $$
>
> *(2) The map and its inverse.* For $q \in U$ put $A(q) = \big(J(q) J(q)^{\mathsf T}\big)^{-1} J(q)$, an $(n-m) \times n$ matrix. Its entries are smooth functions on $U$: the entries of $J(q)$ are partial derivatives $\partial x^{m+s}/\partial r^l(q)$ of components of the smooth chart $\varphi$; those of $J J^{\mathsf T}$ are sums of products of these; and by the cofactor formula $(J J^{\mathsf T})^{-1} = \operatorname{adj}(J J^{\mathsf T}) / \det(J J^{\mathsf T})$, each entry of the inverse is a polynomial in the entries of $J J^{\mathsf T}$ divided by $\det(J J^{\mathsf T})$, which is smooth and, by (1), nowhere zero on $U$. Define
>
> $$
> \Phi_U(q, v) = \big(q, A(q)\, v\big) \quad \big((q, v) \in \mathcal{N}_U\big), \qquad \Theta_U(q, c) = \big(q, J(q)^{\mathsf T} c\big) \quad \big((q, c) \in (U \cap M) \times \mathbb{R}^{n-m}\big).
> $$
>
> *Targets.* For $(q, v) \in \mathcal{N}_U$, $q \in U \cap M$, so $\Phi_U(q, v) \in (U \cap M) \times \mathbb{R}^{n-m}$. For $q \in U \cap M$ and $c \in \mathbb{R}^{n-m}$, $J(q)^{\mathsf T} c \in (T^{\mathrm{geo}}_qM)^\perp$ by $(\flat)$, so $(q, J(q)^{\mathsf T} c) \in \mathcal{N}$, and it lies in $\mathcal{N}_U$ since $q \in U$.
>
> *Mutually inverse.* For $(q, c) \in (U \cap M) \times \mathbb{R}^{n-m}$,
>
> $$
> \Phi_U\big(\Theta_U(q, c)\big) = \Big(q,\ \big(J J^{\mathsf T}\big)^{-1} J\, J^{\mathsf T} c\Big) = \Big(q,\ \big(J J^{\mathsf T}\big)^{-1} \big(J J^{\mathsf T}\big) c\Big) = (q, c),
> $$
>
> with $J = J(q)$. For $(q, v) \in \mathcal{N}_U$, $v \in (T^{\mathrm{geo}}_qM)^\perp$, so by $(\flat)$ $v = J^{\mathsf T} c$ for some $c \in \mathbb{R}^{n-m}$, and
>
> $$
> \Theta_U\big(\Phi_U(q, v)\big) = \Big(q,\ J^{\mathsf T} \big(J J^{\mathsf T}\big)^{-1} J\, v\Big) = \Big(q,\ J^{\mathsf T} \big(J J^{\mathsf T}\big)^{-1} \big(J J^{\mathsf T}\big) c\Big) = \big(q, J^{\mathsf T} c\big) = (q, v).
> $$
>
> So $\Phi_U$ is a bijection with inverse $\Theta_U$.
>
> *Commuting triangle and linearity on fibres.* $\mathrm{pr}_1\big(\Phi_U(q, v)\big) = q = \pi(q, v)$ for every $(q, v) \in \mathcal{N}_U$. On the fibre $\pi^{-1}(q) = \{q\} \times (T^{\mathrm{geo}}_qM)^\perp$, $\Phi_U$ is $v \mapsto A(q)\, v$ in the second component, a linear map; it is a bijection onto $\mathbb{R}^{n-m}$, because $\Phi_U$ and $\Theta_U$ are mutually inverse and both keep the first component $q$, so that $c \mapsto J(q)^{\mathsf T} c$ is its inverse.
>
> *$\Phi_U$ is smooth.* Let $\varphi_M = (x^1, \ldots, x^m)|_{U \cap M}$ be the induced chart of $M$ (Proposition [[§37 Regular Submanifolds#^prop-37-3|§37.3]]); its domain is all of $U \cap M$, so it is also a chart of the open submanifold $U \cap M$ (Proposition [[§17 Differentiable Structures#^prop-17-7|§17.7]](2)), with image $V_M = \varphi_M(U \cap M)$ open in $\mathbb{R}^m$. With the identity chart of $\mathbb{R}^{n-m}$ it gives the product chart $\big((U \cap M) \times \mathbb{R}^{n-m}, \varphi_M \times \mathrm{id}\big)$, whose domain is the whole product (Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-10|§19.10]]); so $\varphi_M \times \mathrm{id} : (U \cap M) \times \mathbb{R}^{n-m} \to V_M \times \mathbb{R}^{n-m}$ is a diffeomorphism (Proposition [[§28 Derivations and the Abstract Tangent Space#^prop-28-9|§28.9]]). Now
>
> $$
> (\varphi_M \times \mathrm{id}) \circ \Phi_U(q, v) = \big(x^1(q), \ldots, x^m(q),\ A(q)\, v\big) = \hat\Phi(q, v), \qquad \hat\Phi : U \times \mathbb{R}^n \to \mathbb{R}^m \times \mathbb{R}^{n-m},
> $$
>
> where $\hat\Phi$ is defined by the same formula on all of $U \times \mathbb{R}^n$ and is smooth, its components being components of $\varphi$ and sums of products of the smooth entries of $A(q)$ with the coordinates $v^l$. The inclusion $\iota_U : \mathcal{N}_U \to U \times \mathbb{R}^n$ is smooth: the inclusion $\mathcal{N}_U \to \mathcal{N}$ is smooth (Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-6|§19.6]](1)), and so is $\iota_{\mathcal{N}}$; their composite $\mathcal{N}_U \to \mathbb{R}^{2n}$ takes values in the open set $U \times \mathbb{R}^n$, hence is smooth into it (Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-6|§19.6]](3)). So $\hat\Phi \circ \iota_U$ is smooth (Lemma [[§19 Smooth Functions and Smooth Maps#^lem-19-5|§19.5]]); it takes values in the open set $V_M \times \mathbb{R}^{n-m}$ of $\mathbb{R}^n$, hence is smooth into it (Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-6|§19.6]](3)); and
>
> $$
> \Phi_U = (\varphi_M \times \mathrm{id})^{-1} \circ \big(\hat\Phi \circ \iota_U\big)
> $$
>
> is a composite of smooth maps, hence smooth.
>
> *$\Theta_U$ is smooth.* First, $\varphi_M^{-1}(r) = \varphi^{-1}(r, \vec 0)$ for $r \in V_M$: such an $r$ is $\varphi_M(q) = \big(x^1(q), \ldots, x^m(q)\big)$ for a $q \in U \cap M$, and $x^{m+1}(q) = \cdots = x^n(q) = 0$ by the description of $U \cap M$ in the Setting, so $\varphi(q) = (r, \vec 0)$ and $\varphi_M^{-1}(r) = q = \varphi^{-1}(r, \vec 0)$. So for $(r, c) \in V_M \times \mathbb{R}^{n-m}$,
>
> $$
> \Theta_U \circ (\varphi_M \times \mathrm{id})^{-1}(r, c) = \Big(\varphi^{-1}(r, \vec 0),\ J\big(\varphi^{-1}(r, \vec 0)\big)^{\mathsf T} c\Big) =: \hat\Theta(r, c) \in \mathbb{R}^{2n},
> $$
>
> and $\hat\Theta : V_M \times \mathbb{R}^{n-m} \to \mathbb{R}^{2n}$ is smooth: $r \mapsto (r, \vec 0)$ is linear with values in $\varphi(U)$ for $r \in V_M$, $\varphi^{-1}$ is smooth on $\varphi(U)$, and the entries of $J$ are smooth on $U$. Hence $\Theta_U = \hat\Theta \circ (\varphi_M \times \mathrm{id})$ is smooth as a map into $\mathbb{R}^{2n}$ (Lemma [[§19 Smooth Functions and Smooth Maps#^lem-19-5|§19.5]]). Its values lie in $\mathcal{N}$ (*Targets* above), so it is smooth into $\mathcal{N}$ (Lemma [[§37 Regular Submanifolds#^lem-37-5|§37.5]](2)), and they lie in the open subset $\mathcal{N}_U$, so it is smooth into $\mathcal{N}_U$ (Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-6|§19.6]](3)).
>
> So $\Phi_U$ is a smooth bijection with smooth inverse $\Theta_U$, a diffeomorphism (Definition [[§19 Smooth Functions and Smooth Maps#^def-19-4|§19.4]]).
>
> *(3) The fibration.* The sets $U \cap M$, over all charts $(U, \varphi)$ of $\mathbb{R}^n$ adapted to $M$, are open in $M$ and cover $M$, since every point of $M$ lies in an adapted chart (Definition [[§37 Regular Submanifolds#^def-37-2|§37.2]]). The projection $\pi$ is smooth (first paragraph), and over each $U \cap M$ the map $\Phi_U$ of (2) is a diffeomorphism $\pi^{-1}(U \cap M) \to (U \cap M) \times \mathbb{R}^{n-m}$ with $\mathrm{pr}_1 \circ \Phi_U = \pi|_{\pi^{-1}(U \cap M)}$. This is Definition [[§40 Fibrations#^def-40-1|§40.1]] with total space $\mathcal{N}$, base $M$, fibre $\mathbb{R}^{n-m}$ and the cover $\{U \cap M\}$.

^pf-42-2

*Uses:* [[§37 Regular Submanifolds#^def-37-1|Def. §37.1]], [[§19 Smooth Functions and Smooth Maps#^def-19-7|Def. §19.7]], [[§37 Regular Submanifolds#^lem-37-5|§37.5]], [[§19 Smooth Functions and Smooth Maps#^lem-19-5|§19.5]], [[§42 The Normal Bundle of a Submanifold of Euclidean Space#^def-42-1|Def. §42.1]], [[§37 Regular Submanifolds#^lem-37-10|§37.10]], [[§7 The Regular Value Theorem#^def-7-1|Def. §7.1]], [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]], [[§37 Regular Submanifolds#^prop-37-3|§37.3]], [[§17 Differentiable Structures#^prop-17-7|§17.7]], [[§19 Smooth Functions and Smooth Maps#^prop-19-10|§19.10]], [[§28 Derivations and the Abstract Tangent Space#^prop-28-9|§28.9]], [[§19 Smooth Functions and Smooth Maps#^prop-19-6|§19.6]], [[§19 Smooth Functions and Smooth Maps#^def-19-4|Def. §19.4]], [[§37 Regular Submanifolds#^def-37-2|Def. §37.2]], [[§40 Fibrations#^def-40-1|Def. §40.1]]

The trivialization is the recipe of the remark *Where Explicit Trivializations Come From* in [[§41 Examples of Fibrations|§41]]: a basis of each fibre that depends smoothly on the base point — here the gradients $\nabla G^s(q)$ — and, for a vector $v$ of the fibre, its components $c = (J J^{\mathsf T})^{-1} J v$ in that basis, $v = \sum_s c^s\, \nabla G^s(q)$. The gradients are the vectors that the dot product attaches to the covectors $dG^s|_q = dx^{m+s}|_q$: by Proposition [[§33 Covectors in Coordinates#^prop-33-3|§33.3]], applied to the smooth function $h = G^s$ on the open set $U$, $\xi_{\nabla G^s(q)} = dG^s|_q$, that is, for $w \in \mathbb{R}^n$,

$$
dG^s|_q\big(D_w|_q\big) = D_w|_q[G^s] = \nabla G^s(q) \cdot w
$$

(the middle expression by Proposition [[§32 The Cotangent Space#^prop-32-2|§32.2]], the last by Proposition [[§30 The Differential in Coordinates#^prop-30-5|§30.5]]). Those covectors form a basis of the conormal space $N_qM$ (Proposition [[§37 Regular Submanifolds#^prop-37-8|§37.8]]; for a general defining map, Proposition [[§39 Transversality and Lagrange Multipliers#^prop-39-5|§39.5]]). So (1) is the basis of the conormal space, read through the metric; Proposition [[§42 The Normal Bundle of a Submanifold of Euclidean Space#^prop-42-3|§42.3]] below says this for every point and for the whole bundle.

## The Endpoint Map and Focal Points

> [!definition] Definition §42.2: Endpoint Map
> The **endpoint map** of $M$ is
>
> $$
> E : \mathcal{N} \to \mathbb{R}^n, \qquad E(p, v) = p + v ,
> $$
>
> the endpoint of the normal vector $v$ drawn from $p$. It is smooth: $E = L \circ \iota_{\mathcal{N}}$, where $\iota_{\mathcal{N}} : \mathcal{N} \to \mathbb{R}^{2n}$ is the inclusion, smooth by Lemma [[§37 Regular Submanifolds#^lem-37-5|§37.5]](1), and $L(p, v) = p + v$ is linear, hence smooth; a composite of smooth maps is smooth (Lemma [[§19 Smooth Functions and Smooth Maps#^lem-19-5|§19.5]]).
>
> *Lee: Ch. 6, Tubular Neighborhoods*

^def-42-2

> [!definition] Definition §42.3: Focal Point
> A point $q \in \mathbb{R}^n$ is a **focal point** of $M$ if $q = E(p, v)$ for some critical point $(p, v) \in \mathcal{N}$ of the endpoint map $E$ (Definition [[§42 The Normal Bundle of a Submanifold of Euclidean Space#^def-42-2|§42.2]]), that is, for some $(p, v)$ at which $E_{\ast(p,v)} : T_{(p,v)}\mathcal{N} \to T_q\mathbb{R}^n$ (written $dE_{(p,v)}$ in the assignment) is not of maximal rank. Since $\dim \mathcal{N} = n = \dim \mathbb{R}^n$ (Proposition [[§42 The Normal Bundle of a Submanifold of Euclidean Space#^prop-42-1|§42.1]]), maximal rank means rank $n$, so $(p, v)$ is critical exactly when $E_{\ast(p,v)}$ is not onto — a critical point in the sense of Definition [[§36 Submersions#^def-36-3|§36.3]] — equivalently (Proposition [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]](1)) not bijective.

^def-42-3

> [!example] Example §42.1: Focal Points of the Parabola
> Let $M = \{(x, y) \in \mathbb{R}^2 : y = x^2\}$. The set of focal points of $M$ is the image of the smooth curve
>
> $$
> \mathbf{r} : \mathbb{R} \to \mathbb{R}^2, \qquad \mathbf{r}(a) = \Big(-4a^3,\ 3a^2 + \tfrac12\Big),
> $$
>
> where $\mathbf{r}(a) = E(p, v)$ for the unique critical point $(p, v)$ of $E$ with $p = (a, a^2)$: the focal point on the normal line to the parabola at $(a, a^2)$.

^ex-42-1

> [!proof]+ Working out the example
> *(Assignment 5, Problem 5(b), as submitted; the smoothness of the parametrization and the passage from $E_\ast$ to a Jacobian are made explicit.)* In this example $(x, y)$ are the standard coordinates of $\mathbb{R}^2$, so $n = 2$ and $m = 1$.
>
> *$M$ is a submanifold.* $M = g^{-1}(0)$ for $g(x, y) = y - x^2$, $g : \mathbb{R}^2 \to \mathbb{R}$, whose Jacobian $g'(x, y) = (-2x, 1)$ is nonzero, i.e. has rank $1$, at every point. So $0$ is a regular value (Definition [[§7 The Regular Value Theorem#^def-7-4|§7.4]]), and $M = g^{-1}(0)$ is an external description of $M$ near each of its points with $W = \mathbb{R}^2$ (Definition [[§20 Manifolds in Euclidean Space#^def-20-1|§20.1]]). By Proposition [[§37 Regular Submanifolds#^prop-37-9|§37.9]], $M$ is a regular submanifold of $\mathbb{R}^2$ of codimension $1$, i.e. of dimension $1$; and by Proposition [[§42 The Normal Bundle of a Submanifold of Euclidean Space#^prop-42-1|§42.1]], $\mathcal{N}$ is a regular submanifold of $\mathbb{R}^4$ of dimension $2$.
>
> *Tangent and normal spaces.* Every $p \in M$ is $p = (a, a^2)$ for a unique $a \in \mathbb{R}$, namely its first coordinate. By Theorem [[§25 The Geometric Tangent Space#^thm-25-3|§25.3]] with $W = \mathbb{R}^2$, $F = g$, $c = 0$,
>
> $$
> T^{\mathrm{geo}}_pM = \ker g'(p) = \{\, (u, w) : -2a\, u + w = 0 \,\} = \{\, (u, 2a\, u) : u \in \mathbb{R} \,\} = \operatorname{Span}\{(1, 2a)\}.
> $$
>
> (The submission finds the same line as the velocity of the curve $t \mapsto (a + t, (a + t)^2)$ in $M$ at $t = 0$, which is $(1, 2a)$, together with $\dim M = 1$.) The vector $(-2a, 1)$ is nonzero and
>
> $$
> (-2a, 1) \cdot (1, 2a) = -2a + 2a = 0 ,
> $$
>
> so it lies in $(T^{\mathrm{geo}}_pM)^\perp$; and $\dim (T^{\mathrm{geo}}_pM)^\perp = n - m = 2 - 1 = 1$, by Proposition [[§42 The Normal Bundle of a Submanifold of Euclidean Space#^prop-42-2|§42.2]](1) (equivalently Lemma [[§37 Regular Submanifolds#^lem-37-10|§37.10]](4)) for the adapted chart $\varphi$ below, in which $(T^{\mathrm{geo}}_pM)^\perp$ has a basis of $n - m = 1$ vector, the gradient $\nabla G^1(p) = \nabla g(p)$. Hence
>
> $$
> (T^{\mathrm{geo}}_pM)^\perp = \operatorname{Span}\{(-2a, 1)\}, \qquad \mathcal{N} = \Big\{\, \big((a, a^2),\ \lambda(-2a, 1)\big) : a, \lambda \in \mathbb{R} \,\Big\}.
> $$
>
> Note that $(-2a, 1) = \nabla g(p)$, as Proposition [[§42 The Normal Bundle of a Submanifold of Euclidean Space#^prop-42-2|§42.2]](1) predicts: $\varphi(x, y) = (x, y - x^2)$ is a chart of $\mathbb{R}^2$ adapted to $M$ with $U = \mathbb{R}^2$ and $G = g$. *(Computed; not from lecture.)* Its Jacobian is $\varphi'(x, y) = \begin{pmatrix} 1 & 0 \\ -2x & 1 \end{pmatrix}$, with determinant $1$; the second row is $\nabla g(x, y) = (-2x, 1)$. Indeed $\varphi$ is a diffeomorphism of $\mathbb{R}^2$ onto itself, smooth with the smooth inverse $(x, z) \mapsto (x, z + x^2)$, so $(\mathbb{R}^2, \varphi) = (\mathbb{R}^2, \varphi \circ \mathrm{id})$ is a smooth chart by Lemma [[§17 Differentiable Structures#^lem-17-6|§17.6]](2), applied to the identity chart of $\mathbb{R}^2$ and the diffeomorphism $\varphi$; and its second coordinate $y - x^2 = g(x, y)$ vanishes exactly on $M$ (Definition [[§37 Regular Submanifolds#^def-37-3|§37.3]], with $k = 1$). It is the chart $\Phi$ of the proof of Proposition [[§37 Regular Submanifolds#^prop-37-9|§37.9]], graph $\Rightarrow$ slice, for $h(x) = x^2$.
>
> *A global parametrization of $\mathcal{N}$.* Define
>
> $$
> \Psi : \mathbb{R}^2 \to \mathcal{N}, \qquad \Psi(a, \lambda) = \big((a, a^2),\ \lambda(-2a, 1)\big) = \big(a,\ a^2,\ -2\lambda a,\ \lambda\big).
> $$
>
> - *Smooth.* As a map into $\mathbb{R}^4$ its components are polynomials, so it is smooth; its values lie in $\mathcal{N}$ by the description of $\mathcal{N}$ just found, so it is smooth into $\mathcal{N}$ (Lemma [[§37 Regular Submanifolds#^lem-37-5|§37.5]](2)).
> - *Bijective.* It is onto $\mathcal{N}$ by that description. It is injective: if $\Psi(a, \lambda) = \Psi(a', \lambda')$, the first coordinates give $a = a'$ and the fourth give $\lambda = \lambda'$.
> - *Its differential is bijective.* The Jacobian of $\Psi$ as a map into $\mathbb{R}^4$,
>
> $$
> D\Psi(a, \lambda) = \begin{pmatrix} 1 & 0 \\ 2a & 0 \\ -2\lambda & -2a \\ 0 & 1 \end{pmatrix},
> $$
>
> has rank $2$, since its first and fourth rows form $I_2$; so $D\Psi(a, \lambda) u = 0$ forces $u = 0$. With $\iota_{\mathcal{N}} : \mathcal{N} \to \mathbb{R}^4$ the inclusion, $\iota_{\mathcal{N}} \circ \Psi$ is $\Psi$ regarded as a map into $\mathbb{R}^4$, and its differential corresponds to $D\Psi(a, \lambda)$ (Proposition [[§30 The Differential in Coordinates#^prop-30-5|§30.5]]). By the Chain Rule (Theorem [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]]), $(\iota_{\mathcal{N}})_{\ast} \circ \Psi_{\ast(a,\lambda)} = (\iota_{\mathcal{N}} \circ \Psi)_{\ast(a,\lambda)}$, which is injective; so $\Psi_{\ast(a,\lambda)}$ is injective (if $\Psi_{\ast}u = 0$ then $(\iota_{\mathcal{N}} \circ \Psi)_{\ast}u = 0$, so $u = 0$). It is a linear map between spaces of the same dimension $2$, $T_{(a,\lambda)}\mathbb{R}^2$ and $T_{\Psi(a,\lambda)}\mathcal{N}$ (Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-9|§29.9]]), hence bijective (Proposition [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]](1)).
>
> By Corollary [[§35 Local Diffeomorphisms#^cor-35-3|§35.3]] (a smooth bijection with bijective differential everywhere; this is where the inverse function theorem, Theorem [[§35 Local Diffeomorphisms#^thm-35-1|§35.1]], enters), $\Psi : \mathbb{R}^2 \to \mathcal{N}$ is a diffeomorphism, and $\Psi^{-1}$ is a global chart of $\mathcal{N}$: its transition maps with any smooth chart $\chi$ of $\mathcal{N}$ are $\chi \circ \Psi$ and $\Psi^{-1} \circ \chi^{-1}$, smooth as composites of smooth maps. (In the language of Proposition [[§42 The Normal Bundle of a Submanifold of Euclidean Space#^prop-42-2|§42.2]], $\Psi(a, \lambda) = \Theta_U\big((a, a^2), \lambda\big)$ with $G = g$: the normal bundle of the parabola is trivial.)
>
> *The endpoint map in coordinates.* Put
>
> $$
> \hat E = E \circ \Psi : \mathbb{R}^2 \to \mathbb{R}^2, \qquad \hat E(a, \lambda) = (a, a^2) + \lambda(-2a, 1) = \big(a - 2\lambda a,\ a^2 + \lambda\big).
> $$
>
> By the Chain Rule, $\hat E_{\ast(a,\lambda)} = E_{\ast\Psi(a,\lambda)} \circ \Psi_{\ast(a,\lambda)}$. Since $\Psi_{\ast(a,\lambda)}$ is a bijection onto $T_{\Psi(a,\lambda)}\mathcal{N}$, the two maps $\hat E_{\ast(a,\lambda)}$ and $E_{\ast\Psi(a,\lambda)}$ have the same image; so $E_{\ast\Psi(a,\lambda)}$ is onto iff $\hat E_{\ast(a,\lambda)}$ is onto, iff (Proposition [[§30 The Differential in Coordinates#^prop-30-5|§30.5]]) the $2 \times 2$ Jacobian $D\hat E(a, \lambda)$ has rank $2$, iff $\det D\hat E(a, \lambda) \neq 0$.
>
> *Critical points of $E$.* Differentiating the components $a - 2\lambda a$ and $a^2 + \lambda$ with respect to $a$ and $\lambda$,
>
> $$
> D\hat E(a, \lambda) = \begin{pmatrix} 1 - 2\lambda & -2a \\ 2a & 1 \end{pmatrix}, \qquad \det D\hat E(a, \lambda) = (1 - 2\lambda)\cdot 1 - (-2a)(2a) = 1 - 2\lambda + 4a^2 .
> $$
>
> So $\Psi(a, \lambda)$ is a critical point of $E$ (Definition [[§42 The Normal Bundle of a Submanifold of Euclidean Space#^def-42-3|§42.3]]) if and only if $1 - 2\lambda + 4a^2 = 0$, that is,
>
> $$
> \lambda = \frac{4a^2 + 1}{2} .
> $$
>
> For each $a$ there is exactly one such $\lambda$, and every point of $\mathcal{N}$ is $\Psi(a, \lambda)$ for exactly one $(a, \lambda)$; so the critical points of $E$ are exactly the points $\Psi\big(a, \tfrac{4a^2+1}{2}\big)$, one over each $p = (a, a^2) \in M$.
>
> *The focal points.* A point of $\mathbb{R}^2$ is a focal point iff it is $E(\Psi(a, \lambda)) = \hat E(a, \lambda)$ with $\lambda = \frac{4a^2+1}{2}$, for some $a \in \mathbb{R}$. Substituting,
>
> $$
> a - 2\lambda a = a - a(4a^2 + 1) = -4a^3, \qquad a^2 + \lambda = a^2 + 2a^2 + \tfrac12 = 3a^2 + \tfrac12 .
> $$
>
> So the set of focal points is the image of $\mathbf{r}(a) = \big(-4a^3, 3a^2 + \frac12\big)$, a smooth curve, its components being polynomials in $a$; and $\mathbf{r}(a) = E(p, v)$ for the critical point over $p = (a, a^2)$.
>
> *Shape.* $\mathbf{r}(-a) = \big(4a^3, 3a^2 + \frac12\big)$ is the reflection of $\mathbf{r}(a)$ in the $y$-axis, so the curve is symmetric about the axis of the parabola. Its velocity $\mathbf{r}'(a) = (-12a^2, 6a)$ vanishes only at $a = 0$, where the curve has a cusp at $\mathbf{r}(0) = (0, \frac12)$ (the remark *Focal Points Are Centres of Curvature* gives its equation, $(y - \frac12)^3 = \frac{27}{16}x^2$).

^pf-ex-42-1

*Uses:* [[§7 The Regular Value Theorem#^def-7-4|Def. §7.4]], [[§20 Manifolds in Euclidean Space#^def-20-1|Def. §20.1]], [[§37 Regular Submanifolds#^prop-37-9|§37.9]], [[§42 The Normal Bundle of a Submanifold of Euclidean Space#^prop-42-1|§42.1]], [[§25 The Geometric Tangent Space#^thm-25-3|§25.3]], [[§42 The Normal Bundle of a Submanifold of Euclidean Space#^prop-42-2|§42.2]], [[§37 Regular Submanifolds#^lem-37-10|§37.10]], [[§17 Differentiable Structures#^lem-17-6|§17.6]], [[§37 Regular Submanifolds#^def-37-3|Def. §37.3]], [[§37 Regular Submanifolds#^lem-37-5|§37.5]], [[§30 The Differential in Coordinates#^prop-30-5|§30.5]], [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]], [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-9|§29.9]], [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]], [[§35 Local Diffeomorphisms#^cor-35-3|§35.3]], [[§35 Local Diffeomorphisms#^thm-35-1|§35.1]], [[§42 The Normal Bundle of a Submanifold of Euclidean Space#^def-42-3|Def. §42.3]]

![[m591-39-1.svg]]

*The parabola $y = x^2$ (blue, drawn for $|x| \le 1.6$) and its set of focal points, the curve $\mathbf{r}$ (red, drawn for $|a| \le 0.82$). The red curve is symmetric about the $y$-axis and has a cusp at $(0, \frac12)$ (the dot), the focal point over the vertex; as $|a|$ grows the focal points move out and up, $\mathbf{r}(a)$ lying on the normal line at $(a, a^2)$, on the concave side. The cusp is not the optical focus $(0, \frac14)$ of the parabola: “focal” here refers to the endpoint map, and the remark *Focal Points Are Centres of Curvature* explains what these points are.*

![[m591-39-a1.gif|460]]

*(Not from lecture; animation added, vault only.)* The normal line (red) at $(a, a^2)$ as $a$ runs from $-0.9$ to $0.9$ and back; earlier normals are gray. The focal point $\mathbf{r}(a) = (-4a^3, 3a^2 + \tfrac12)$ on the current normal, where neighbouring normals meet, traces the curve of focal points (blue), the envelope of the normals.

![[m591-39-a2.gif|420]]

*(Not from lecture; animation added, vault only.)* The endpoint map $E(p, v) = p + v$ on normal vectors $v = r\,n_p$ of fixed length $r$, for all $p$ on $y = x^2$ ($n_p$ the upward unit normal): the offset curves as $r$ grows to $1.6$. For $r < \frac12$, the radius of curvature at the vertex, they are smooth; beyond it two cusps (blue) appear and ride on the curve of focal points (dashed), the critical values of $E$.

> [!remark] Remark: Focal Points Are Centres of Curvature
> *(Not from the assignment.)* At the critical point over $p = (a, a^2)$ the normal vector is $v = \lambda(-2a, 1)$ with $\lambda = \frac{1 + 4a^2}{2}$, of length
>
> $$
> |v| = \lambda\, \big|(-2a, 1)\big| = \frac{1 + 4a^2}{2}\, \sqrt{1 + 4a^2} = \frac{(1 + 4a^2)^{3/2}}{2} .
> $$
>
> This is the radius of curvature of the graph $y = f(x)$ at $x = a$, $R = (1 + f'(a)^2)^{3/2} / |f''(a)|$, for $f(x) = x^2$: $f'(a) = 2a$ and $f''(a) = 2$ give $R = (1 + 4a^2)^{3/2}/2$. And $v$ points to the concave (upper) side, since $\lambda > 0$ and $(-2a, 1)$ has positive second component. So the focal point $p + v$ on the normal line at $p$ is the *centre of curvature*, the centre of the osculating circle at $p$, and the curve $\mathbf{r}$ of focal points is the *evolute* of the parabola. As a check, the classical formula for the centre of curvature of a graph, $\big(a - f'(1 + f'^2)/f'',\ f + (1 + f'^2)/f''\big)$, gives
>
> $$
> \Big(a - \frac{2a(1 + 4a^2)}{2},\ a^2 + \frac{1 + 4a^2}{2}\Big) = \Big(-4a^3,\ 3a^2 + \tfrac12\Big) = \mathbf{r}(a).
> $$
>
> *The evolute as a curve.* From $x = -4a^3$ and $y - \frac12 = 3a^2$: $(y - \frac12)^3 = 27a^6$ and $x^2 = 16a^6$, so
>
> $$
> \Big(y - \tfrac12\Big)^3 = \tfrac{27}{16}\, x^2 ,
> $$
>
> a semicubical parabola with its cusp at $(0, \frac12)$. Conversely every point of this curve is on $\mathbf{r}$: given $(x, y)$ with $(y - \frac12)^3 = \frac{27}{16}x^2$, let $a$ be the real cube root of $-x/4$; then $-4a^3 = x$, and $y - \frac12 = \big(\frac{27}{16}x^2\big)^{1/3} = 3\,(x/4)^{2/3} = 3a^2$. The cusp is the centre of curvature at the vertex, where the radius of curvature is $R = \frac12$: the osculating circle there is $x^2 + (y - \frac12)^2 = \frac14$.
>
> *In general* (stated, not proved here): for a submanifold $M \subseteq \mathbb{R}^n$, $(p, v) \in \mathcal{N}$ is a critical point of $E$ if and only if $1$ is an eigenvalue of the shape operator (second fundamental form) of $M$ at $p$ in the normal direction $v$, and the dimension of $\ker E_{\ast(p,v)}$ is the multiplicity of that eigenvalue (Milnor, *Morse Theory*, §6). For a curve in the plane the shape operator in the direction of a normal $v$ is multiplication by $\kappa\, (v \cdot \mathbf{n})$, with $\kappa$ the curvature and $\mathbf{n}$ the unit normal toward the concave side; so the focal point on each normal line is at distance $|v| = 1/\kappa$ on the concave side, the centre of curvature, as found above. For the parabola, $\kappa = 2/(1 + 4a^2)^{3/2}$.

^rem-42-1

## Normal and Conormal

> [!theorem] Proposition §42.3: Normal and Conormal Spaces
> Let $M \subseteq \mathbb{R}^n$ be a regular submanifold of dimension $m < n$, $p \in M$, and $v \mapsto \xi_v$, $\xi_v(D_w|_p) = v \cdot w$, the isomorphism $\mathbb{R}^n \to T_p^{\ast}\mathbb{R}^n$ given by the dot product (Proposition [[§33 Covectors in Coordinates#^prop-33-3|§33.3]]).
>
> 1. It restricts to an isomorphism
>
> $$
> (T^{\mathrm{geo}}_pM)^\perp \xrightarrow{\ \cong\ } N_pM, \qquad v \mapsto \xi_v ,
> $$
>
> of the Euclidean normal space onto the conormal space of $M$ in $\mathbb{R}^n$ (Definition [[§37 Regular Submanifolds#^def-37-4|§37.4]]), both of dimension $n - m$.
> 2. In a chart $(U, \varphi)$ of $\mathbb{R}^n$ at $p$ adapted to $M$, with $G = (x^{m+1}, \ldots, x^n)$ as in the Setting of [[§42 The Normal Bundle of a Submanifold of Euclidean Space|§42]], it sends the gradient $\nabla G^s(p)$ to the differential $dG^s|_p = dx^{m+s}|_p$, for $s = 1, \ldots, n - m$: the basis of $(T^{\mathrm{geo}}_pM)^\perp$ of Proposition [[§42 The Normal Bundle of a Submanifold of Euclidean Space#^prop-42-2|§42.2]](1) to the basis of $N_pM$ of Proposition [[§37 Regular Submanifolds#^prop-37-8|§37.8]].
> 3. Fibre by fibre, $(p, v) \mapsto (p, \xi_v)$ maps the normal bundle $\mathcal{N}$ bijectively onto the set $\{\, (p, \xi) : p \in M,\ \xi \in N_pM \,\}$, linearly on each fibre.

^prop-42-3

> [!proof]+ Proof
> *(Not from the assignment; filled in.)* Fix $p \in M$ and a chart $(U, \varphi)$ of $\mathbb{R}^n$ at $p$ adapted to $M$, with $G$ and $J$ as in the Setting (every point of $M$ lies in one, Definition [[§37 Regular Submanifolds#^def-37-2|§37.2]]).
>
> *The tangent space of $M$ inside $T_p\mathbb{R}^n$.* By Corollary [[§30 The Differential in Coordinates#^cor-30-6|§30.6]] every tangent vector of $\mathbb{R}^n$ at $p$ is $D_w|_p$ for a unique $w \in \mathbb{R}^n$. Under $w \mapsto D_w|_p$ the subspace $\iota_{\ast p}(T_pM)$ is $T^{\mathrm{geo}}_pM$ (the remark *The Tangent Spaces Match* in [[§37 Regular Submanifolds|§37]]). In detail: by Lemma [[§37 Regular Submanifolds#^lem-37-10|§37.10]](1), $J(q) = G'(q)$ has rank $n - m$ for every $q \in U$, so $\vec 0$ is a regular value of $G : U \to \mathbb{R}^{n-m}$ (Definition [[§7 The Regular Value Theorem#^def-7-4|§7.4]]), and $U \cap M = G^{-1}(\vec 0)$ by the description of $U \cap M$ in the Setting. Proposition [[§38 The Regular Value Theorem for Manifolds#^prop-38-4|§38.4]](2), with $W = U$, $F = G$, $c = \vec 0$ and $S = U \cap M$, says that the image of $T_p(U \cap M)$ in $T_pU$ is $\ker J(p)$ under $w \mapsto D_w|_p$; and $\ker J(p) = T^{\mathrm{geo}}_pM$ by Lemma [[§37 Regular Submanifolds#^lem-37-10|§37.10]](2). Since $U \cap M$ is open in $M$ and $U$ is open in $\mathbb{R}^n$, these tangent spaces are those of $M$ and $\mathbb{R}^n$ (Lemma [[§28 Derivations and the Abstract Tangent Space#^lem-28-8|§28.8]]). So
>
> $$
> \iota_{\ast p}(T_pM) = \big\{\, D_w|_p : w \in T^{\mathrm{geo}}_pM \,\big\} .
> $$
>
> *(1)* By Proposition [[§33 Covectors in Coordinates#^prop-33-3|§33.3]], $v \mapsto \xi_v$ is a linear isomorphism $\mathbb{R}^n \to T_p^{\ast}\mathbb{R}^n$. For $v \in \mathbb{R}^n$, by Definition [[§37 Regular Submanifolds#^def-37-4|§37.4]] and the description of $\iota_{\ast p}(T_pM)$ just obtained,
>
> $$
> \xi_v \in N_pM \iff \xi_v\big(D_w|_p\big) = 0 \ \text{ for all } w \in T^{\mathrm{geo}}_pM \iff v \cdot w = 0 \ \text{ for all } w \in T^{\mathrm{geo}}_pM \iff v \in (T^{\mathrm{geo}}_pM)^\perp .
> $$
>
> So the isomorphism maps $(T^{\mathrm{geo}}_pM)^\perp$ into $N_pM$, injectively, as the restriction of an injective map; and onto $N_pM$: every $\xi \in N_pM$ is $\xi_v$ for some $v \in \mathbb{R}^n$, $v \mapsto \xi_v$ being onto, and this $v$ lies in $(T^{\mathrm{geo}}_pM)^\perp$ by the equivalence. A restriction of a linear map is linear, so $(T^{\mathrm{geo}}_pM)^\perp \to N_pM$ is a linear isomorphism. Both spaces have dimension $n - m$: $(T^{\mathrm{geo}}_pM)^\perp$ by Proposition [[§42 The Normal Bundle of a Submanifold of Euclidean Space#^prop-42-2|§42.2]](1), which gives it a basis of $n - m$ gradients, and $N_pM$ by Proposition [[§37 Regular Submanifolds#^prop-37-8|§37.8]], $n - m$ being the codimension of $M$ in $\mathbb{R}^n$.
>
> *(2)* $G^s = x^{m+s}$ is a smooth function on the open set $U$, so Proposition [[§33 Covectors in Coordinates#^prop-33-3|§33.3]], applied to $h = G^s$, gives $\xi_{\nabla G^s(p)} = dG^s|_p$, with $T_p^{\ast}U = T_p^{\ast}\mathbb{R}^n$ (Lemma [[§28 Derivations and the Abstract Tangent Space#^lem-28-8|§28.8]]); explicitly, for $w \in \mathbb{R}^n$,
>
> $$
> \xi_{\nabla G^s(p)}\big(D_w|_p\big) = \nabla G^s(p) \cdot w = D_w|_p[G^s] = dG^s|_p\big(D_w|_p\big),
> $$
>
> as in the paragraph after Proposition [[§42 The Normal Bundle of a Submanifold of Euclidean Space#^prop-42-2|§42.2]]. By Proposition [[§42 The Normal Bundle of a Submanifold of Euclidean Space#^prop-42-2|§42.2]](1) the $\nabla G^s(p)$ form a basis of $(T^{\mathrm{geo}}_pM)^\perp$, and by Proposition [[§37 Regular Submanifolds#^prop-37-8|§37.8]] (the adapted chart $(U, \varphi)$ has codimension $n - m$, so its last $n - m$ coordinates are $x^{m+1}, \ldots, x^n$) the $dx^{m+s}|_p = dG^s|_p$ form a basis of $N_pM$.
>
> *(3)* By Definition [[§42 The Normal Bundle of a Submanifold of Euclidean Space#^def-42-1|§42.1]], $(p, v) \in \mathcal{N}$ means $p \in M$ and $v \in (T^{\mathrm{geo}}_pM)^\perp$; then $\xi_v \in N_pM$ by (1), so the map takes values in the set $\{(p, \xi) : p \in M,\ \xi \in N_pM\}$. It is injective: if $(p, \xi_v) = (p', \xi_{v'})$, then $p = p'$, and $\xi_v = \xi_{v'}$ in $T_p^{\ast}\mathbb{R}^n$ gives $v = v'$ by (1). It is onto: given $p \in M$ and $\xi \in N_pM$, (1) gives $v \in (T^{\mathrm{geo}}_pM)^\perp$ with $\xi_v = \xi$, and $(p, v) \in \mathcal{N}$ is mapped to $(p, \xi)$. It keeps the base point $p$, and on the fibre over $p$ it is the linear map $v \mapsto \xi_v$ of (1).

^pf-42-3

*Uses:* [[§37 Regular Submanifolds#^def-37-2|Def. §37.2]], [[§30 The Differential in Coordinates#^cor-30-6|§30.6]], [[§37 Regular Submanifolds#^lem-37-10|§37.10]], [[§7 The Regular Value Theorem#^def-7-4|Def. §7.4]], [[§38 The Regular Value Theorem for Manifolds#^prop-38-4|§38.4]], [[§28 Derivations and the Abstract Tangent Space#^lem-28-8|§28.8]], [[§33 Covectors in Coordinates#^prop-33-3|§33.3]], [[§37 Regular Submanifolds#^def-37-4|Def. §37.4]], [[§42 The Normal Bundle of a Submanifold of Euclidean Space#^prop-42-2|§42.2]], [[§37 Regular Submanifolds#^prop-37-8|§37.8]], [[§42 The Normal Bundle of a Submanifold of Euclidean Space#^def-42-1|Def. §42.1]]

> [!remark] Remark: Normal Bundle and Conormal Bundle
> *(Not from the assignment.)* The set $\{(p, \xi) : p \in M,\ \xi \in N_pM\}$ of Proposition [[§42 The Normal Bundle of a Submanifold of Euclidean Space#^prop-42-3|§42.3]](3) is the conormal bundle $N^{\ast}M$ of $M \subseteq \mathbb{R}^n$, announced in the remark *The Conormal Bundle* in [[§39 Transversality and Lagrange Multipliers|§39]] and defined later, in [[§55 Morse Functions and the Zero Section|§55]] (Definition [[§55 Morse Functions and the Zero Section#^def-55-1|§55.1]]), once the cotangent bundle $T^{\ast}\mathbb{R}^n$ is available. So $\mathcal{N}$ is the conormal bundle read through the metric of $\mathbb{R}^n$. This is Uribe's remark that with an inner product the conormal space “would be the normal space” (the remark *No Normal Vectors Without a Metric* in [[§37 Regular Submanifolds|§37]]), and it is why both bundles have dimension $n$: $m$ dimensions of base point, plus $n - m$ of normal vector or conormal covector.

^rem-42-2
