---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 11
section: 79
tags: [differentiable-manifolds, math591]
---
← [[§78 Properties of the Wedge Product]] · ↑ [[· 11 Differential Forms]] · [[§80 Differential Forms on Manifolds]] →

*Stage: forms — A linear map pulls $k$-forms back; in bases the pullback is given by the $k \times k$ minors of its matrix, and in top degree by its determinant.*

*(Lecture 31.)* One more piece of linear algebra. Recall the space $\Lambda^k V^{\ast}$ of linear $k$-forms on $V$ (Definition [[§75 Multilinear Algebra#^def-75-2|§75.2]]), of dimension $\binom{m}{k}$ with $m = \dim V$ (Proposition [[§75 Multilinear Algebra#^prop-75-6|§75.6]]). Throughout this section $V$ and $W$ are real vector spaces of dimensions $m$ and $n$, and $F : V \to W$ is any linear map; the dimensions need not be equal.

> [!remark] Remark: Notation of Lecture 31
> The dictionary between the board and these notes, for this section and the next, in addition to the remarks *Notation in This Section* ([[§75 Multilinear Algebra|§75]]) and *Notation of Lecture 30* ([[§76 Shuffles|§76]]):
> - *Vectors.* The board writes $v_1, \ldots, v_k$; as before, these notes write $v^1, \ldots, v^k$ (label up).
> - *Dual bases.* $(e_1, \ldots, e_m)$ is a basis of $V$ with dual basis $(\varepsilon^1, \ldots, \varepsilon^m)$ of $V^{\ast}$, and $(f_1, \ldots, f_n)$ a basis of $W$ with dual basis $(\phi^1, \ldots, \phi^n)$ of $W^{\ast}$. The board's letter for the second dual basis is $\phi$; it is printed $\phi$ here, and $\varphi$ stays reserved for charts, as in [[§80 Differential Forms on Manifolds|§80]], where the board's chart is $\varphi = (x^1, \ldots, x^m)$.
> - *The matrix of $F$.* The board calls it $A$. Since $A$ and $B$ denote index sets, these notes write $[F]$, as in Proposition [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]](3): the $n \times m$ matrix with entry $[F]_{ij} = \phi^i(F e_j)$ in row $i$ and column $j$.
> - *Index sets.* $A = \{a_1 < \cdots < a_k\} \subseteq \{1, \ldots, m\}$ indexes the basis of $\Lambda^k V^{\ast}$, and $B = \{b_1 < \cdots < b_k\} \subseteq \{1, \ldots, n\}$ that of $\Lambda^k W^{\ast}$; $\phi^B = \phi^{b_1} \wedge \cdots \wedge \phi^{b_k}$, as for $\varepsilon^A$ (Proposition [[§78 Properties of the Wedge Product#^prop-78-4|§78.4]](4)).
> - *Components of a form on a manifold.* The board writes $f^A$ for the coefficient of $dx^A$. These notes write $f_A$, with the index down, like the components $\theta_j$ of a one-form (Proposition [[§53 One-Forms#^prop-53-1|§53.1]]) and Lee's $\omega_I$.
> - *Differentials and pullbacks.* The board's $dF_p$ is the pushforward $F_{\ast p}$ (Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-6|§28.6]]; Appendix A.1), and $(dF_p)^{\ast}$ is the pullback of Definition [[§79 Pullbacks of Linear Forms#^def-79-1|§79.1]] for the linear map $dF_p$; for $k = 1$ it is the pullback of covectors $F_p^{\ast}$ (Definition [[§34 The Cotangent Space from Germs#^def-34-3|§34.3]]). Lee writes $dF_p^{\ast}$.
> - *Degree.* $|\omega|$ is the degree of a form (Definition [[§80 Differential Forms on Manifolds#^def-80-2|§80.2]]); the notation is not Lee's.

^rem-79-1

> [!definition] Definition §79.1: Pullback of Linear Forms
> Let $F : V \to W$ be linear and $k \ge 0$. The **pullback** by $F$ is the map
>
> $$
> F^{\ast} : \Lambda^k W^{\ast} \longrightarrow \Lambda^k V^{\ast}, \qquad (F^{\ast}\beta)(v^1, \ldots, v^k) = \beta\big(F v^1, \ldots, F v^k\big) ,
> $$
>
> for $\beta \in \Lambda^k W^{\ast}$ and $v^1, \ldots, v^k \in V$.
> For $k = 0$, $F^{\ast}$ is the identity of $\Lambda^0 W^{\ast} = \mathbb{R} = \Lambda^0 V^{\ast}$.
>
> *Lee: Ch. 12, Pullbacks of Tensor Fields*

^def-79-1

> [!remark]- Connections
> - The case $k = 1$ is the dual map: [[§21 Linear Algebra Toolkit#^def-21-3|Def. §21.3]]; on a manifold, the pullback of covectors: [[§34 The Cotangent Space from Germs#^def-34-3|Def. §34.3]].
> - Applied at each point of a manifold to the differential of a smooth map: [[§80 Differential Forms on Manifolds#^def-80-9|Def. §80.9]].

$F$ pushes vectors forward, from $V$ to $W$; by duality, forms are pulled back, from $W$ to $V$: to evaluate $F^{\ast}\beta$ on vectors of $V$, push them to $W$ and evaluate $\beta$ there. This is the multilinear version of the dual map: for $k = 1$, $F^{\ast}\beta = \beta \circ F$ is the dual map of Definition [[§21 Linear Algebra Toolkit#^def-21-3|§21.3]], and on manifolds that case is the pullback of covectors (Definition [[§34 The Cotangent Space from Germs#^def-34-3|§34.3]]).

> [!theorem] Lemma §79.1: Basic Properties of the Linear Pullback
> Let $F : V \to W$ be linear and $\beta \in \Lambda^k W^{\ast}$.
>
> 1. $F^{\ast}\beta$ is a linear $k$-form on $V$: $F^{\ast}\beta \in \Lambda^k V^{\ast}$.
> 2. $F^{\ast} : \Lambda^k W^{\ast} \to \Lambda^k V^{\ast}$ is linear.

^lem-79-1

> [!proof]+ Proof
> *(Not from lecture; filled in.)* (1) Fix all entries but the $j$-th. Then $v^j \mapsto F v^j$ is linear and $\beta$ is linear in its $j$-th entry, so the composite $v^j \mapsto \beta(F v^1, \ldots, F v^j, \ldots, F v^k)$ is linear: $F^{\ast}\beta$ is multilinear. Exchanging $v^i$ and $v^j$ exchanges the entries $F v^i$ and $F v^j$ of $\beta$, which changes the sign (Definition [[§75 Multilinear Algebra#^def-75-1|§75.1]]). (2) For $\beta, \gamma \in \Lambda^k W^{\ast}$ and $c \in \mathbb{R}$, evaluating with the pointwise operations of Definition [[§75 Multilinear Algebra#^def-75-2|§75.2]],
>
> $$
> \big(F^{\ast}(\beta + c\gamma)\big)(v^1, \ldots, v^k) = \beta(F v^1, \ldots, F v^k) + c\, \gamma(F v^1, \ldots, F v^k) = \big(F^{\ast}\beta + c\, F^{\ast}\gamma\big)(v^1, \ldots, v^k) .
> $$

^pf-79-1

*Uses:* [[§75 Multilinear Algebra#^def-75-1|Def. §75.1]], [[§75 Multilinear Algebra#^def-75-2|Def. §75.2]]

*In bases.* Let $(e_1, \ldots, e_m)$ and $(f_1, \ldots, f_n)$ be bases of $V$ and $W$, with dual bases $(\varepsilon^1, \ldots, \varepsilon^m)$ of $V^{\ast}$ and $(\phi^1, \ldots, \phi^n)$ of $W^{\ast}$ (Definition [[§21 Linear Algebra Toolkit#^def-21-2|§21.2]]). For $B = \{b_1 < \cdots < b_k\} \subseteq \{1, \ldots, n\}$ put $\phi^B = \phi^{b_1} \wedge \cdots \wedge \phi^{b_k}$. The $\phi^B$ form a basis of $\Lambda^k W^{\ast}$, and the $\varepsilon^A$ a basis of $\Lambda^k V^{\ast}$ (Propositions [[§75 Multilinear Algebra#^prop-75-6|§75.6]] and [[§78 Properties of the Wedge Product#^prop-78-4|§78.4]](4)). The lecture wrote down, as an exercise, the pullback of a basis element.

> [!theorem] Proposition §79.2: Components of a Pullback
> With these bases, let $[F]$ be the $n \times m$ matrix of $F$, with entry $[F]_{ij} = \phi^i(F e_j)$ in row $i$ and column $j$ (Proposition [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]](3)). For every $k$-element subset $B = \{b_1 < \cdots < b_k\}$ of $\{1, \ldots, n\}$,
>
> $$
> F^{\ast}(\phi^B) = \sum_{A} \det\big( \phi^{b_i}(F e_{a_j}) \big)_{i, j = 1, \ldots, k}\; \varepsilon^A ,
> $$
>
> the sum over all $k$-element subsets $A = \{a_1 < \cdots < a_k\}$ of $\{1, \ldots, m\}$. The coefficient of $\varepsilon^A$ is the $k \times k$ minor of $[F]$ in the rows $b_1, \ldots, b_k$ and the columns $a_1, \ldots, a_k$.
>
> *Lee: cf. Lemma 14.16(c), Proposition 14.20*

^prop-79-2

> [!proof]+ Proof
> *(Lecture 31.)* By Lemma [[§79 Pullbacks of Linear Forms#^lem-79-1|§79.1]], $F^{\ast}(\phi^B) \in \Lambda^k V^{\ast}$, so it is a linear combination of the $\varepsilon^A$, and by Proposition [[§75 Multilinear Algebra#^prop-75-6|§75.6]] its $\varepsilon^A$-component is its value on $(e_{a_1}, \ldots, e_{a_k})$; components are always extracted in this way. By Definition [[§79 Pullbacks of Linear Forms#^def-79-1|§79.1]] and then Definition [[§75 Multilinear Algebra#^def-75-3|§75.3]], applied in $W$ to the basis $(\phi^i)$ of $W^{\ast}$,
>
> $$
> F^{\ast}(\phi^B)(e_{a_1}, \ldots, e_{a_k}) = \phi^B\big(F e_{a_1}, \ldots, F e_{a_k}\big) = \det\big( \phi^{b_i}(F e_{a_j}) \big)_{i, j = 1, \ldots, k} .
> $$
>
> (The lecture used $\phi^B = \phi^{b_1} \wedge \cdots \wedge \phi^{b_k}$ and the fact that a wedge product of one-forms evaluated on vectors is a determinant, announced there as the first problem of the next assignment. In these notes that fact is Lemma [[§78 Properties of the Wedge Product#^lem-78-2|§78.2]], and the two descriptions of $\phi^B$ agree by Proposition [[§78 Properties of the Wedge Product#^prop-78-4|§78.4]](4).) Finally, the dual basis extracts components: $F e_{a_j} = \sum_i \phi^i(F e_{a_j})\, f_i$ (Proposition [[§21 Linear Algebra Toolkit#^prop-21-2|§21.2]]), so $\phi^{b_i}(F e_{a_j})$ is the $f_{b_i}$-component of $F e_{a_j}$, the entry $[F]_{b_i a_j}$ of the matrix.

^pf-79-2

*Uses:* [[§79 Pullbacks of Linear Forms#^lem-79-1|§79.1]], [[§75 Multilinear Algebra#^prop-75-6|§75.6]], [[§79 Pullbacks of Linear Forms#^def-79-1|Def. §79.1]], [[§75 Multilinear Algebra#^def-75-3|Def. §75.3]], [[§78 Properties of the Wedge Product#^lem-78-2|§78.2]], [[§78 Properties of the Wedge Product#^prop-78-4|§78.4]], [[§21 Linear Algebra Toolkit#^prop-21-2|§21.2]]

**Transcription note (Lecture 31).** The board wrote the sum over $A \subset \{1, \ldots, k\}$ and the determinant as $\det\big(\phi^{b_i}(F(e_j))\big)$. The subsets $A$ are the $k$-element subsets of $\{1, \ldots, m\}$, and the column index is $a_j$, as in the line before on the board, $\phi^B\big(F(e_{a_1}), \ldots, F(e_{a_k})\big)$.

![[m591-78-1.svg]]

*(Not from lecture; figure added.)* Proposition [[§79 Pullbacks of Linear Forms#^prop-79-2|§79.2]] for $m = 6$, $n = 5$ and $k = 3$. The columns of $[F]$ belong to the basis vectors $e_j$ of $V$ and the rows to the covectors $\phi^i$ of $W^{\ast}$. The subset $A \subseteq \{1, \ldots, 6\}$ of $V$ picks three columns and $B \subseteq \{1, \ldots, 5\}$ three rows; the coefficient of $\varepsilon^A$ in $F^{\ast}\phi^B$ is the determinant of the entries in both (orange), with row index $i$ (from $b_i$) and column index $j$ (from $a_j$), as in Definition [[§75 Multilinear Algebra#^def-75-3|§75.3]].

![[m591-78-a1.gif|600]]

*(Not from lecture; animation added, vault only.)* The rows $B = \{2 < 4 < 5\}$ stay fixed while the column set $A$ runs through all $\binom{6}{3} = 20$ three-element subsets of $\{1, \ldots, 6\}$. Each orange $3 \times 3$ minor is the coefficient of one $\varepsilon^A$ in $F^{\ast}\phi^B$; the columns need not be adjacent.

The chosen rows and columns need not be adjacent, so the entries need not fill a block of neighbouring places of $[F]$. In linear algebra this is still called a minor, and every $k \times k$ minor of $[F]$ occurs, as the coefficient of $\varepsilon^A$ in $F^{\ast}\phi^B$ for one pair $(A, B)$.

*The important special case* is $k = m = n$: a linear map between spaces of the same dimension, and forms of top degree. Then $\dim \Lambda^m V^{\ast} = \binom{m}{m} = 1$, and there is only one subset of each kind, $A = B = \{1, \ldots, m\}$. These one-dimensional spaces will be important on manifolds.

> [!theorem] Proposition §79.3: Pullback in Top Degree
> 1. Let $\dim V = \dim W = m$, with bases as above. The one-element bases of $\Lambda^m W^{\ast}$ and $\Lambda^m V^{\ast}$ are $\phi^1 \wedge \cdots \wedge \phi^m$ and $\varepsilon^1 \wedge \cdots \wedge \varepsilon^m$, and
>
> $$
> \boxed{\; F^{\ast}\big(\phi^1 \wedge \cdots \wedge \phi^m\big) = \det [F]\;\, \varepsilon^1 \wedge \cdots \wedge \varepsilon^m \;}
> $$
>
> where $[F] = \big(\phi^i(F e_j)\big)_{i, j}$ is the $m \times m$ matrix of $F$.
>
> 2. *(Not from lecture.)* If $W = V$, then $F^{\ast}\omega = (\det F)\, \omega$ for every $\omega \in \Lambda^m V^{\ast}$; that is, $\omega(F v^1, \ldots, F v^m) = (\det F)\, \omega(v^1, \ldots, v^m)$, where $\det F$ is the determinant of the matrix of $F$ in any basis of $V$.
>
> *Lee: Proposition 14.9*

^prop-79-3

> [!remark]- Connections
> - The same determinant in the change of variables formula for multiple integrals: [[§25 Change of Variables on General Domains#^thm-25-6|452 Thm. §25.6]].
> - On manifolds, for the Jacobian of a map between manifolds of the same dimension: [[§80 Differential Forms on Manifolds#^cor-80-6|§80.6]].
> - The determinant is multiplicative, which is $(G \circ F)^{\ast} = F^{\ast} \circ G^{\ast}$ in top degree: [[§37 Determinants#^ladr-9-49|LADR 9.49]].

> [!proof]+ Proof
> (1) *(Lecture 31.)* By Proposition [[§75 Multilinear Algebra#^prop-75-6|§75.6]] with $k = m$ there is one $m$-element subset of $\{1, \ldots, m\}$, so the bases have one element each, $\phi^{\{1, \ldots, m\}} = \phi^1 \wedge \cdots \wedge \phi^m$ and $\varepsilon^{\{1, \ldots, m\}} = \varepsilon^1 \wedge \cdots \wedge \varepsilon^m$ (Proposition [[§78 Properties of the Wedge Product#^prop-78-4|§78.4]](4)). In Proposition [[§79 Pullbacks of Linear Forms#^prop-79-2|§79.2]] the sum has the single term $A = \{1, \ldots, m\}$, and the minor in all the rows and all the columns is the whole matrix.
>
> (2) *(Filled in.)* Take any basis $(e_j)$ of $V$, and use it also as the basis $(f_j)$ of $W = V$, so that $(\phi^i) = (\varepsilon^i)$ and $[F]$ is the matrix of $F$ in this basis. Since $\dim \Lambda^m V^{\ast} = 1$, $\omega = c\, \varepsilon^1 \wedge \cdots \wedge \varepsilon^m$ for some $c \in \mathbb{R}$, and by (1) and the linearity of $F^{\ast}$ (Lemma [[§79 Pullbacks of Linear Forms#^lem-79-1|§79.1]]), $F^{\ast}\omega = c \det[F]\, \varepsilon^1 \wedge \cdots \wedge \varepsilon^m = \det[F]\, \omega$. The determinant of the matrix of $F$ does not depend on the basis: in another basis the matrix is $P^{-1}[F] P$ (Proposition [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]](4)), with the same determinant.

^pf-79-3

*Uses:* [[§75 Multilinear Algebra#^prop-75-6|§75.6]], [[§78 Properties of the Wedge Product#^prop-78-4|§78.4]], [[§79 Pullbacks of Linear Forms#^prop-79-2|§79.2]], [[§79 Pullbacks of Linear Forms#^lem-79-1|§79.1]], [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]]

The formula is boxed because it is what allows top-degree forms to be integrated. It has been seen before, in the change of variables formula for multiple integrals, where the determinant of the Jacobian appears: that is the same determinant, and it is what will allow the integral of a top-degree form to be defined intrinsically (Corollary [[§80 Differential Forms on Manifolds#^cor-80-6|§80.6]] and Example [[§80 Differential Forms on Manifolds#^ex-80-2|§80.2]] below).

*(Lecture 31, later in the lecture.)* The pullback is compatible with the wedge product (Definition [[§77 The Wedge Product#^def-77-1|§77.1]]).

> [!theorem] Proposition §79.4: Pullback Preserves Wedge Products
> Let $F : V \to W$ be linear, $\alpha \in \Lambda^k W^{\ast}$ and $\beta \in \Lambda^l W^{\ast}$. Then
>
> $$
> F^{\ast}(\alpha \wedge \beta) = (F^{\ast}\alpha) \wedge (F^{\ast}\beta) .
> $$
>
> *Lee: cf. Lemma 14.16(b)*

^prop-79-4

> [!proof]+ Proof
> *(Lecture 31 gave the idea: expand by shuffles, with an $F$ inside every argument; written out.)* Let $v^1, \ldots, v^{k+l} \in V$. By Definition [[§79 Pullbacks of Linear Forms#^def-79-1|§79.1]], then Definition [[§77 The Wedge Product#^def-77-1|§77.1]] applied to the vectors $F v^1, \ldots, F v^{k+l}$ of $W$, then Definition [[§79 Pullbacks of Linear Forms#^def-79-1|§79.1]] for $\alpha$ and for $\beta$, then Definition [[§77 The Wedge Product#^def-77-1|§77.1]] in $V$:
>
> $$
> \begin{aligned}
> F^{\ast}(\alpha \wedge \beta)(v^1, \ldots, v^{k+l}) &= (\alpha \wedge \beta)\big(F v^1, \ldots, F v^{k+l}\big) \\
> &= \sum_{\sigma \in \mathrm{Sh}(k, l)} \operatorname{sgn}(\sigma)\, \alpha\big(F v^{\sigma(1)}, \ldots, F v^{\sigma(k)}\big)\, \beta\big(F v^{\sigma(k+1)}, \ldots, F v^{\sigma(k+l)}\big) \\
> &= \sum_{\sigma \in \mathrm{Sh}(k, l)} \operatorname{sgn}(\sigma)\, (F^{\ast}\alpha)\big(v^{\sigma(1)}, \ldots, v^{\sigma(k)}\big)\, (F^{\ast}\beta)\big(v^{\sigma(k+1)}, \ldots, v^{\sigma(k+l)}\big) \\
> &= \big((F^{\ast}\alpha) \wedge (F^{\ast}\beta)\big)(v^1, \ldots, v^{k+l}) .
> \end{aligned}
> $$
>
> For $k = 0$ or $l = 0$ this is the linearity of $F^{\ast}$, since the wedge product with a scalar is multiplication by it.

^pf-79-4

*Uses:* [[§79 Pullbacks of Linear Forms#^def-79-1|Def. §79.1]], [[§77 The Wedge Product#^def-77-1|Def. §77.1]]

**Transcription note (Lecture 31).** The board wrote $\alpha \in \Lambda^k W$, $\beta \in \Lambda^l W$; the forms are $\alpha \in \Lambda^k W^{\ast}$ and $\beta \in \Lambda^l W^{\ast}$, as in the remark *Notation in This Section*.
