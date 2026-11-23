---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 11
section: 84
tags: [differentiable-manifolds, math591]
---
← [[§83 The First Cohomology of the Circle]] · ↑ [[· 11 Differential Forms]] · [[§85 Lie Derivatives of Forms]] →

*Stage: forms — Inserting a vector field into the first slot of a form lowers the degree by one; full contraction evaluates the form on fields; the global formula for $d$ on one-forms.*

*(Lecture 33.)* Back to operations with forms, which will have consequences for de Rham theory. Forms and vector fields can now be combined, doing things with both at the same time. The first such operation is the contraction by a vector field.

> [!definition] Definition §84.1: Contraction by a Vector Field
> Let $\alpha \in \Omega^k(M)$ and $\mathbf{X} \in \mathfrak{X}(M)$, with $k \ge 1$. The **contraction** of $\alpha$ by $\mathbf{X}$ is the $(k-1)$-form $\iota_\mathbf{X}\alpha \in \Omega^{k-1}(M)$ defined at each $p \in M$ by
>
> $$
> (\iota_\mathbf{X}\alpha)_p(v^1, \ldots, v^{k-1}) = \alpha_p\big(\mathbf{X}_p, v^1, \ldots, v^{k-1}\big) \qquad \text{for all } v^1, \ldots, v^{k-1} \in T_pM :
> $$
>
> the value $\mathbf{X}_p$ is inserted in the first slot. For $k = 0$, $\alpha = f \in C^\infty(M)$, define $\iota_\mathbf{X} f = 0$. Lee calls this interior multiplication and also writes $\mathbf{X} \mathbin{\lrcorner} \alpha = \iota_\mathbf{X}\alpha$.
>
> *Lee: Ch. 14, Interior Multiplication (Lemma 14.13 for vector spaces)*

^def-84-1

> [!remark]- Connections
> - The slots of a linear $k$-form: [[§75 Multilinear Algebra#^def-75-1|Def. §75.1]].
> - The Lie derivative along $\mathbf{X}$, the operation that $d$ and $\iota_\mathbf{X}$ combine to give in Cartan's magic formula: [[§72 Lie Derivatives#^def-72-2|Def. §72.2]]; for forms, [[§85 Lie Derivatives of Forms#^def-85-2|Def. §85.2]], and the formula, [[§86 Cartan's Magic Formula#^thm-86-2|Thm. §86.2]].

The first slot is a convention. There is a point-by-point version: for a vector $v \in T_pM$, $\iota_v : \Lambda^k T_p^{\ast}M \to \Lambda^{k-1} T_p^{\ast}M$ inserts $v$ in the first slot, and $(\iota_\mathbf{X}\alpha)_p = \iota_{\mathbf{X}_p}\alpha_p$. For $k = 0$ there is no slot for a vector field, so the expression makes no sense; it is very convenient to define it to be zero. The operators $\iota_\mathbf{X}$ go down by one in degree, $\Omega^k(M) \to \Omega^{k-1}(M)$, on a single manifold; the properties of the map $\alpha \mapsto \iota_\mathbf{X}\alpha$ will be studied later.

> [!theorem] Lemma §84.1: Contraction Gives a Smooth Form
> For $\alpha \in \Omega^k(M)$ and $\mathbf{X} \in \mathfrak{X}(M)$, $\iota_\mathbf{X}\alpha$ is a smooth $(k-1)$-form, and $\iota_\mathbf{X}\alpha$ is linear in $\alpha$, and $C^\infty(M)$-linear in $\mathbf{X}$: $\iota_{f\mathbf{X} + \mathbf{Y}}\alpha = f\, \iota_\mathbf{X}\alpha + \iota_\mathbf{Y}\alpha$.
>
> *Source: not from lecture · filled in*

^lem-84-1

> [!proof]+ Proof
> At each $p$, $(v^1, \ldots, v^{k-1}) \mapsto \alpha_p(\mathbf{X}_p, v^1, \ldots, v^{k-1})$ is multilinear, because $\alpha_p$ is, and alternating, because exchanging two of the $v^i$ exchanges two entries of $\alpha_p$ (Definition [[§75 Multilinear Algebra#^def-75-1|§75.1]]); so $(\iota_\mathbf{X}\alpha)_p \in \Lambda^{k-1} T_p^{\ast}M$. The linearity statements hold pointwise, by the multilinearity of $\alpha_p$. For smoothness, let $(U, (x^i))$ be a chart, $\mathbf{X} = \sum_i \mathbf{X}^i \partial_i$ on $U$ with smooth $\mathbf{X}^i$ (Proposition [[§56 Vector Fields#^prop-56-1|§56.1]]), and $C = \{c_1 < \cdots < c_{k-1}\}$. The $dx^C$-component of $\iota_\mathbf{X}\alpha$ (Definition [[§80 Differential Forms on Manifolds#^def-80-3|§80.3]]) is
>
> $$
> (\iota_\mathbf{X}\alpha)(\partial_{c_1}, \ldots, \partial_{c_{k-1}}) = \sum_i \mathbf{X}^i\; \alpha(\partial_i, \partial_{c_1}, \ldots, \partial_{c_{k-1}}) ,
> $$
>
> and $\alpha(\partial_i, \partial_{c_1}, \ldots, \partial_{c_{k-1}})$ is $0$ if $i \in C$ and $\pm f_{C \cup \{i\}}$ otherwise (Lemma [[§75 Multilinear Algebra#^lem-75-1|§75.1]]: sort the arguments). So the components are smooth on $U$, and $\iota_\mathbf{X}\alpha$ is smooth (Definition [[§80 Differential Forms on Manifolds#^def-80-4|§80.4]]).

^pf-84-1

*Uses:* [[§75 Multilinear Algebra#^def-75-1|Def. §75.1]], [[§56 Vector Fields#^prop-56-1|§56.1]], [[§80 Differential Forms on Manifolds#^def-80-3|Def. §80.3]], [[§75 Multilinear Algebra#^lem-75-1|§75.1]], [[§80 Differential Forms on Manifolds#^def-80-4|Def. §80.4]]

![[m591-80-4.svg]]

*(Not from lecture; diagram added.)* On one manifold $M$, $d$ raises the degree by one and $\iota_\mathbf{X}$ lowers it by one. The board drew the arrows $\iota_\mathbf{X}$ diagonally into the diagram of the induced maps (after Proposition [[§82 De Rham Cohomology#^prop-82-2|§82.2]]), to be used for Cartan's magic formula, announced for the next lecture; since the contraction acts on a single manifold, they are drawn here on the de Rham complex of $M$ alone.

*Contracting all the way.* If $\mathbf{X}_1, \ldots, \mathbf{X}_k$ are $k$ vector fields, the contraction can be repeated: contract $\alpha$ once by $\mathbf{X}_1$, then the result by $\mathbf{X}_2$, and so on, all the way down to a $0$-form, a function.

> [!theorem] Proposition §84.2: Full Contraction Is Evaluation
> For $\alpha \in \Omega^k(M)$ and $\mathbf{X}_1, \ldots, \mathbf{X}_k \in \mathfrak{X}(M)$,
>
> $$
> \iota_{\mathbf{X}_k} \cdots \iota_{\mathbf{X}_2}\, \iota_{\mathbf{X}_1}\alpha = \alpha(\mathbf{X}_1, \ldots, \mathbf{X}_k) \in C^\infty(M), \qquad \alpha(\mathbf{X}_1, \ldots, \mathbf{X}_k)(p) = \alpha_p\big(\mathbf{X}_1|_p, \ldots, \mathbf{X}_k|_p\big) ,
> $$
>
> the function obtained by pointwise evaluation of $\alpha$ on the fields: at each point, evaluate $\alpha$ and each of the fields $\mathbf{X}_j$ at that point; the scalar obtained is a function of the point.

^prop-84-2

> [!proof]+ Proof
> *(Filled in.)* By induction on $j$,
>
> $$
> (\iota_{\mathbf{X}_j} \cdots \iota_{\mathbf{X}_1}\alpha)_p(v^{j+1}, \ldots, v^k) = \alpha_p(\mathbf{X}_1|_p, \ldots, \mathbf{X}_j|_p, v^{j+1}, \ldots, v^k) :
> $$
>
> contracting by $\mathbf{X}_{j+1}$ inserts $\mathbf{X}_{j+1}|_p$ in the first remaining slot, which is slot $j + 1$ of $\alpha_p$. For $j = k$ no slots remain. The function is smooth by Lemma [[§84 Contraction by Vector Fields#^lem-84-1|§84.1]], applied $k$ times.

^pf-84-2

*Uses:* [[§84 Contraction by Vector Fields#^lem-84-1|§84.1]]

**Transcription note (Lecture 33).** The handwritten notes give the iterated contraction the target $\Omega^1(M)$, and write $(\iota_\mathbf{X}\alpha)_p(\ldots) = \alpha(\mathbf{X}_p, \ldots)$. After $k$ contractions a $k$-form has degree $0$: the target is $\Omega^0(M) = C^\infty(M)$; and the form evaluated at $p$ is $\alpha_p$.

> [!theorem] Proposition §84.3: A Form Is Determined by Its Values on Vector Fields
> If $\alpha, \beta \in \Omega^k(M)$ satisfy $\alpha(\mathbf{X}_1, \ldots, \mathbf{X}_k) = \beta(\mathbf{X}_1, \ldots, \mathbf{X}_k)$ for all $\mathbf{X}_1, \ldots, \mathbf{X}_k \in \mathfrak{X}(M)$, then $\alpha = \beta$: the full contractions with all vector fields determine the form.
>
> *Source: Lecture 33 · observation*

^prop-84-3

> [!proof]+ Proof
> *(Lecture 33: every tangent vector can be extended to a vector field, as in the homework, Theorem [[§65 Partitions of Unity#^thm-65-11|§65.11]]; the extension of a single vector is filled in.)* Let $p \in M$ and $v^1, \ldots, v^k \in T_pM$. Each $v^j$ extends to a smooth field: in a chart $(U, (x^i))$ at $p$ write $v^j = \sum_i a^i \partial_i|_p$, take a bump function $\chi$ at $p$ supported in $U$ (Corollary [[§56 Vector Fields#^cor-56-7|§56.7]]), and let $\mathbf{X}_j = \chi \sum_i a^i \partial_i$ on $U$ and $0$ outside $U$; it is smooth, since $\chi$ vanishes near the boundary of $U$ in $M$, and $\mathbf{X}_j|_p = v^j$ because $\chi(p) = 1$. Then $\alpha_p(v^1, \ldots, v^k) = \alpha(\mathbf{X}_1, \ldots, \mathbf{X}_k)(p) = \beta(\mathbf{X}_1, \ldots, \mathbf{X}_k)(p) = \beta_p(v^1, \ldots, v^k)$.

^pf-84-3

*Uses:* [[§65 Partitions of Unity#^thm-65-11|§65.11]], [[§56 Vector Fields#^cor-56-7|§56.7]]

*The global formula for $d$.* One reason to be interested in contractions is the *global formula* for $d$. For a one-form $\alpha$, $d\alpha$ is a two-form, so it can be contracted twice: putting the fields $\mathbf{X}$ and $\mathbf{Y}$ inside gives a function, and that function has a formula in terms of $\alpha$ alone.

Lecture 33 stated the next lemma as the first step of the proof of Theorem [[§84 Contraction by Vector Fields#^thm-84-5|§84.5]]; the computation was not done on the board.

> [!theorem] Lemma §84.4: The Right-Hand Side of the Global Formula Is Bilinear over Functions
> Let $\alpha \in \Omega^1(M)$, and for $\mathbf{X}, \mathbf{Y} \in \mathfrak{X}(M)$ put
>
> $$
> \mathcal{R}(\mathbf{X}, \mathbf{Y}) = \mathbf{X}\big(\alpha(\mathbf{Y})\big) - \mathbf{Y}\big(\alpha(\mathbf{X})\big) - \alpha\big([\mathbf{X}, \mathbf{Y}]\big) \in C^\infty(M) .
> $$
>
> 1. $\mathcal{R}$ is additive in $\mathbf{X}$ and in $\mathbf{Y}$.
> 2. $\mathcal{R}(f\mathbf{X}, g\mathbf{Y}) = fg\, \mathcal{R}(\mathbf{X}, \mathbf{Y})$ for all $f, g \in C^\infty(M)$.
> 3. $[f\mathbf{X}, g\mathbf{Y}] = fg\, [\mathbf{X}, \mathbf{Y}] + f\, (\mathbf{X}g)\, \mathbf{Y} - g\, (\mathbf{Y}f)\, \mathbf{X}$.
>
> *Source: Lecture 33 · filled in*

^lem-84-4

> [!proof]+ Proof
> *(Written out after Assignment 9; the lecture gave the statement.)* *(1)* Each term of $\mathcal{R}$ is additive in $\mathbf{X}$ and in $\mathbf{Y}$: $\alpha$ is pointwise linear, $\mathbf{X} \mapsto \mathbf{X}h$ is additive, and the bracket is bilinear.
>
> *(3) and (2).* Since $\alpha$ is pointwise linear, $\alpha(g\mathbf{Y}) = g\, \alpha(\mathbf{Y})$. The Leibniz rule for the derivation $\mathbf{X}$ (Lemma [[§56 Vector Fields#^lem-56-4|§56.4]]) gives
>
> $$
> f\mathbf{X}\big(g\, \alpha(\mathbf{Y})\big) = f\, (\mathbf{X}g)\, \alpha(\mathbf{Y}) + fg\, \mathbf{X}\big(\alpha(\mathbf{Y})\big), \qquad g\mathbf{Y}\big(f\, \alpha(\mathbf{X})\big) = g\, (\mathbf{Y}f)\, \alpha(\mathbf{X}) + gf\, \mathbf{Y}\big(\alpha(\mathbf{X})\big) .
> $$
>
> For the bracket, for every function $h$,
>
> $$
> [f\mathbf{X}, g\mathbf{Y}]h = f\mathbf{X}\big(g\, \mathbf{Y}h\big) - g\mathbf{Y}\big(f\, \mathbf{X}h\big) = f\, (\mathbf{X}g)\, \mathbf{Y}h + fg\, \mathbf{X}\mathbf{Y}h - g\, (\mathbf{Y}f)\, \mathbf{X}h - gf\, \mathbf{Y}\mathbf{X}h ,
> $$
>
> so $[f\mathbf{X}, g\mathbf{Y}] = fg\, [\mathbf{X}, \mathbf{Y}] + f\, (\mathbf{X}g)\, \mathbf{Y} - g\, (\mathbf{Y}f)\, \mathbf{X}$, and
>
> $$
> \alpha\big([f\mathbf{X}, g\mathbf{Y}]\big) = fg\, \alpha\big([\mathbf{X}, \mathbf{Y}]\big) + f\, (\mathbf{X}g)\, \alpha(\mathbf{Y}) - g\, (\mathbf{Y}f)\, \alpha(\mathbf{X}) .
> $$
>
> Subtracting, the terms $f\, (\mathbf{X}g)\, \alpha(\mathbf{Y})$ and $g\, (\mathbf{Y}f)\, \alpha(\mathbf{X})$ cancel, and $\mathcal{R}(f\mathbf{X}, g\mathbf{Y}) = fg\, \mathcal{R}(\mathbf{X}, \mathbf{Y})$.

^pf-84-4

*Uses:* [[§56 Vector Fields#^lem-56-4|§56.4]]

> [!theorem] Theorem §84.5: Global Formula for $d$ on One-Forms
> Let $\alpha \in \Omega^1(M)$ and $\mathbf{X}, \mathbf{Y} \in \mathfrak{X}(M)$. Then
>
> $$
> d\alpha(\mathbf{X}, \mathbf{Y}) = \mathbf{X}\big(\alpha(\mathbf{Y})\big) - \mathbf{Y}\big(\alpha(\mathbf{X})\big) - \alpha\big([\mathbf{X}, \mathbf{Y}]\big) .
> $$
>
> *Lee: Proposition 14.29*

^thm-84-5

> [!proof]+ Proof
> *(Lecture 33 gave the following plan, without the computations; they are written out below, after Assignment 9.)* Denote the right-hand side by $\mathcal{R}(\mathbf{X}, \mathbf{Y})$; $\alpha$ is fixed and does not enter the notation.
>
> 1. *First,* show that $\mathcal{R}(f\mathbf{X}, g\mathbf{Y}) = fg\, \mathcal{R}(\mathbf{X}, \mathbf{Y})$ for all $f, g \in C^\infty(M)$. If the theorem is to be true, this must hold: $d\alpha$ is a form, pointwise linear, so the $f$ and the $g$ come out of the left-hand side. It is a computation with the Leibniz rule, in which all the derivatives of $f$ and $g$ cancel.
> 2. *Second,* check the identity for $\mathbf{X} = \partial/\partial x^a$ and $\mathbf{Y} = \partial/\partial x^b$ in a coordinate system $(x^1, \ldots, x^m)$. These fields commute, so the bracket term goes away.
>
> These two imply the general case, because in coordinates any $\mathbf{X}$ and $\mathbf{Y}$ are linear combinations of the coordinate fields with smooth coefficients, and the right-hand side is linear over $C^\infty$.
>
> *The first step* is Lemma [[§84 Contraction by Vector Fields#^lem-84-4|§84.4]](2). The left-hand side has the same property, pointwise: $d\alpha(f\mathbf{X}, g\mathbf{Y})(p) = f(p)\, g(p)\, (d\alpha)_p(\mathbf{X}_p, \mathbf{Y}_p)$. Both sides are additive in $\mathbf{X}$ and in $\mathbf{Y}$ (Lemma [[§84 Contraction by Vector Fields#^lem-84-4|§84.4]](1)).
>
> *The second step.* Let $(U, (x^1, \ldots, x^m))$ be a chart, $\partial_a = \partial/\partial x^a$, and $\alpha = \sum_j \alpha_j\, dx^j$ on $U$. The coordinate fields commute, $[\partial_a, \partial_b] = 0$ (Proposition [[§58 Lie Bracket and Lie Algebra#^prop-58-2|§58.2]], with constant components), and $\alpha(\partial_b) = \alpha_b$, so $\mathcal{R}(\partial_a, \partial_b) = \partial_a \alpha_b - \partial_b \alpha_a$. On the other side, $d\alpha = \sum_{i, j} \partial_i \alpha_j\; dx^i \wedge dx^j$ (Corollary [[§81 The Exterior Derivative#^cor-81-6|§81.6]]), and $(dx^i \wedge dx^j)(\partial_a, \partial_b) = \delta^i_a \delta^j_b - \delta^i_b \delta^j_a$ (Lemma [[§78 Properties of the Wedge Product#^lem-78-2|§78.2]]), so
>
> $$
> d\alpha(\partial_a, \partial_b) = \partial_a \alpha_b - \partial_b \alpha_a = \mathcal{R}(\partial_a, \partial_b) .
> $$
>
> *Conclusion.* Both sides at a point $p$ depend only on $\alpha$, $\mathbf{X}$ and $\mathbf{Y}$ near $p$: the left side is pointwise, and on the right, $(\mathbf{X}h)(p) = \mathbf{X}_p[h]$ depends only on the germ of $h$, while the bracket commutes with restriction to open sets (Corollary [[§59 Related Vector Fields#^cor-59-8|§59.8]]). So both sides may be computed on a chart domain $U \ni p$, with $\alpha|_U$, $\mathbf{X}|_U$, $\mathbf{Y}|_U$, and the two steps hold on the manifold $U$. There $\mathbf{X} = \sum_a \mathbf{X}^a \partial_a$ and $\mathbf{Y} = \sum_b \mathbf{Y}^b \partial_b$ with smooth coefficients, and by Lemma [[§84 Contraction by Vector Fields#^lem-84-4|§84.4]](1) and (2),
>
> $$
> \mathcal{R}(\mathbf{X}, \mathbf{Y}) = \sum_{a, b} \mathbf{X}^a \mathbf{Y}^b\, \mathcal{R}(\partial_a, \partial_b) = \sum_{a, b} \mathbf{X}^a \mathbf{Y}^b\, d\alpha(\partial_a, \partial_b) = d\alpha(\mathbf{X}, \mathbf{Y}) \quad \text{on } U .
> $$

^pf-84-5

*Uses:* [[§84 Contraction by Vector Fields#^lem-84-4|§84.4]], [[§58 Lie Bracket and Lie Algebra#^prop-58-2|§58.2]], [[§81 The Exterior Derivative#^cor-81-6|§81.6]], [[§78 Properties of the Wedge Product#^lem-78-2|§78.2]], [[§59 Related Vector Fields#^cor-59-8|§59.8]]

> [!remark]- Connections
> - The Lie bracket: [[§58 Lie Bracket and Lie Algebra#^def-58-1|Def. §58.1]]; in coordinates, where the coordinate fields commute: [[§58 Lie Bracket and Lie Algebra#^prop-58-2|§58.2]].
> - $d$ in coordinates: [[§81 The Exterior Derivative#^cor-81-6|§81.6]].

> [!example] Example §84.1: A Check of the Global Formula
> For $\alpha = u\, dv$ with functions $u, v \in C^\infty(M)$, $d\alpha = du \wedge dv$, so by Lemma [[§78 Properties of the Wedge Product#^lem-78-2|§78.2]]
>
> $$
> d\alpha(\mathbf{X}, \mathbf{Y}) = (\mathbf{X}u)(\mathbf{Y}v) - (\mathbf{Y}u)(\mathbf{X}v) .
> $$
>
> The right-hand side of Theorem [[§84 Contraction by Vector Fields#^thm-84-5|§84.5]] is $\mathbf{X}(u\, \mathbf{Y}v) - \mathbf{Y}(u\, \mathbf{X}v) - u\, [\mathbf{X}, \mathbf{Y}]v$. By the Leibniz rule this is $(\mathbf{X}u)(\mathbf{Y}v) + u\, \mathbf{X}\mathbf{Y}v - (\mathbf{Y}u)(\mathbf{X}v) - u\, \mathbf{Y}\mathbf{X}v - u\, (\mathbf{X}\mathbf{Y}v - \mathbf{Y}\mathbf{X}v)$, and the terms with $u$ undifferentiated cancel: the two sides agree. Every one-form is locally a sum of forms $u\, dv$, and Lee proves the theorem from this case.
>
> *Source: not from lecture*

^ex-84-1

*Reading the formula.* There are three terms, each a function. First, contract $\alpha$ with $\mathbf{Y}$, which gives the function $\alpha(\mathbf{Y})$, and apply $\mathbf{X}$ to it as an operator. Second, the same in the other order: contract with $\mathbf{X}$, then apply $\mathbf{Y}$. Third, the two fields have a commutator, the Lie bracket $[\mathbf{X}, \mathbf{Y}]$ (Definition [[§58 Lie Bracket and Lie Algebra#^def-58-1|§58.1]]), another field, and $\alpha$ can be contracted with it. The gain: there is no $d$ on the right-hand side, only $\alpha$ by itself. The price: $\mathbf{X}$ and $\mathbf{Y}$ must be fields, and the right-hand side is not a pointwise calculation, since it differentiates. For $k$-forms there is a formula of the same kind, with many more ways of contracting on the right (Lee, Proposition 14.32); it was assigned as reading, and is stated as Theorem [[§84 Contraction by Vector Fields#^thm-84-6|§84.6]] below.

*Convention.* The formula depends on the determinant convention for the wedge product (the remark *Two Conventions for the Wedge Product* in [[§77 The Wedge Product|§77]]), which is also Lee's; with the Alt convention a factor $\frac12$ appears on the left.

## The Global Formula for $k$-Forms

> [!theorem] Theorem §84.6: Global Formula for $d$ on $k$-Forms
> Let $\omega \in \Omega^k(M)$ and $\mathbf{X}_0, \ldots, \mathbf{X}_k \in \mathfrak{X}(M)$. Then
>
> $$
> \begin{aligned}d\omega(\mathbf{X}_0, \ldots, \mathbf{X}_k) ={}& \sum_{i=0}^{k} (-1)^{i}\; \mathbf{X}_i\Big( \omega\big(\mathbf{X}_0, \ldots, \widehat{\mathbf{X}_i}, \ldots, \mathbf{X}_k\big) \Big) \\
> &+ \sum_{0 \le i < j \le k} (-1)^{i+j}\; \omega\big( [\mathbf{X}_i, \mathbf{X}_j], \mathbf{X}_0, \ldots, \widehat{\mathbf{X}_i}, \ldots, \widehat{\mathbf{X}_j}, \ldots, \mathbf{X}_k \big) ,\end{aligned}
> $$
>
> where the hats mean that the fields are left out.
>
> *Source: Lecture 33 · reading · Assignment 9, Problem 4(c)*
>
> *Lee: Proposition 14.32*

^thm-84-6

> [!proof]+ Proof (not given in this course)
> The formula was assigned as reading (Lee, Proposition 14.32). Lee numbers the fields $\mathbf{X}_1, \ldots, \mathbf{X}_{k+1}$ and has the sign $(-1)^{i-1}$ in the first sum; numbering from $0$ turns it into $(-1)^i$ and leaves $(-1)^{i+j}$ unchanged, since $i + j$ changes by $2$. For $k = 1$ the formula is Theorem [[§84 Contraction by Vector Fields#^thm-84-5|§84.5]]: $d\alpha(\mathbf{X}_0, \mathbf{X}_1) = \mathbf{X}_0\big(\alpha(\mathbf{X}_1)\big) - \mathbf{X}_1\big(\alpha(\mathbf{X}_0)\big) - \alpha\big([\mathbf{X}_0, \mathbf{X}_1]\big)$.

^pf-84-6

*Uses:* [[§84 Contraction by Vector Fields#^thm-84-5|§84.5]]

## Assignment 9, Problem 4: Left-Invariant Forms

*From Assignment 9, Problem 4 (submitted). On a Lie group, the forms that are invariant under all left translations are determined by their value at the identity, the exterior derivative preserves them, and on them $d$ becomes an algebraic operator built from the Lie bracket. The steps of the submitted solution that are general statements are stated as lemmas.*

Throughout, $G$ is a Lie group with identity $e$, $L_g$ is left translation by $g$ (Definition [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-2|§60.2]]), $\mathfrak{g} = T_eG$ with the bracket of Definition [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-6|§60.6]], and for $v \in \mathfrak{g}$, $\mathbf{X}^v$ is the left-invariant extension, $\mathbf{X}^v_g = d(L_g)_e v$ (Definition [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-5|§60.5]]). So $\Lambda^k\mathfrak{g}^{\ast} = \Lambda^k T_e^{\ast}G$ is the space of alternating $k$-linear maps on $T_eG$.

> [!definition] Definition §84.2: Left-Invariant Form
> A $k$-form $\omega$ on $G$ is **left-invariant** if $L_g^{\ast}\omega = \omega$ for all $g \in G$. The set of all smooth left-invariant $k$-forms is denoted $\Omega^k_G$; it is a linear subspace of $\Omega^k(G)$, because each $L_g^{\ast}$ is linear (Proposition [[§80 Differential Forms on Manifolds#^prop-80-5|§80.5]](1)).
>
> *Source: Assignment 9, Problem 4*

^def-84-2

> [!remark]- Connections
> - The same notion for vector fields, and the extension of a vector at $e$: [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-3|Def. §60.3]], [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-5|Def. §60.5]], [[§60 Lie Groups and Left-Invariant Vector Fields#^thm-60-9|Thm. §60.9]].

The definition makes sense for $k$-forms that are not assumed smooth (Definition [[§80 Differential Forms on Manifolds#^def-80-1|§80.1]]), since the pullback is defined pointwise (Definition [[§80 Differential Forms on Manifolds#^def-80-9|§80.9]]); this is used for the forms $\omega^\eta$ below before they are known to be smooth.

> [!theorem] Lemma §84.7: Left-Invariance at a Point
> Let $\omega$ be a $k$-form on $G$, not assumed smooth.
>
> 1. $\omega$ is left-invariant if and only if, for all $g, h \in G$ and $v^1, \ldots, v^k \in T_hG$,
>
> $$
> \omega_{gh}\big( d(L_g)_h v^1, \ldots, d(L_g)_h v^k \big) = \omega_h(v^1, \ldots, v^k) .
> $$
>
> 2. For every $g \in G$, $d(L_g)_e : T_eG \to T_gG$ is a linear isomorphism, with inverse $d(L_{g^{-1}})_g$.
> 3. If $\omega$ is left-invariant, then for all $g \in G$ and $w^1, \ldots, w^k \in T_gG$,
>
> $$
> \omega_g(w^1, \ldots, w^k) = \omega_e\big( d(L_{g^{-1}})_g w^1, \ldots, d(L_{g^{-1}})_g w^k \big) ,
> $$
>
> that is, $\omega_g = \big(d(L_{g^{-1}})_g\big)^{\ast}\omega_e$. So a left-invariant form is determined by its value at $e$.
>
> *Source: Assignment 9, Problem 4(a) · submitted solution*

^lem-84-7

> [!proof]+ Proof
> *(The submitted solution.)* *(1)* $L_g(h) = gh$, so $d(L_g)_h : T_hG \to T_{gh}G$, and by Definition [[§80 Differential Forms on Manifolds#^def-80-9|§80.9]] the left-hand side of the displayed equation is $(L_g^{\ast}\omega)_h(v^1, \ldots, v^k)$. So the equation for all $h$ and all vectors is $L_g^{\ast}\omega = \omega$.
>
> *(2)* Since $L_{g^{-1}} \circ L_g = \mathrm{id}_G$ and $L_g \circ L_{g^{-1}} = \mathrm{id}_G$, with $L_g(e) = g$ and $L_{g^{-1}}(g) = e$, the chain rule (Theorem [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]]) gives
>
> $$
> d(L_{g^{-1}})_g \circ d(L_g)_e = \mathrm{id}_{T_eG}, \qquad d(L_g)_e \circ d(L_{g^{-1}})_g = \mathrm{id}_{T_gG} .
> $$
>
> *(3)* Put $v^i = d(L_{g^{-1}})_g w^i \in T_eG$, so that $w^i = d(L_g)_e v^i$ by (2). By (1) with $h = e$, $\omega_g(w^1, \ldots, w^k) = \omega_g\big(d(L_g)_e v^1, \ldots, d(L_g)_e v^k\big) = \omega_e(v^1, \ldots, v^k)$.

^pf-84-7

*Uses:* [[§80 Differential Forms on Manifolds#^def-80-9|Def. §80.9]], [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]]

> [!theorem] Lemma §84.8: A Left-Invariant Form on Left-Invariant Fields Is Constant
> Let $\omega$ be a left-invariant $k$-form on $G$, not assumed smooth, and $v_1, \ldots, v_k \in \mathfrak{g}$. Then the function $g \mapsto \omega_g\big(\mathbf{X}^{v_1}_g, \ldots, \mathbf{X}^{v_k}_g\big)$ on $G$ is constant, equal to $\omega_e(v_1, \ldots, v_k)$.
>
> *Source: Assignment 9, Problem 4(c) · submitted solution*

^lem-84-8

> [!proof]+ Proof
> *(The submitted solution, where this makes the first sum of the global formula vanish.)* By Lemma [[§84 Contraction by Vector Fields#^lem-84-7|§84.7]](3) and $\mathbf{X}^{v_l}_g = d(L_g)_e v_l$,
>
> $$
> \omega_g\big(\mathbf{X}^{v_1}_g, \ldots, \mathbf{X}^{v_k}_g\big) = \omega_e\big( d(L_{g^{-1}})_g\, d(L_g)_e v_1, \ldots, d(L_{g^{-1}})_g\, d(L_g)_e v_k \big) = \omega_e(v_1, \ldots, v_k) ,
> $$
>
> since $d(L_{g^{-1}})_g \circ d(L_g)_e = \mathrm{id}_{T_eG}$ (Lemma [[§84 Contraction by Vector Fields#^lem-84-7|§84.7]](2)). The value does not depend on $g$.

^pf-84-8

*Uses:* [[§84 Contraction by Vector Fields#^lem-84-7|§84.7]]

> [!theorem] Proposition §84.9: Left-Invariant Forms and Forms on the Lie Algebra
> The map
>
> $$
> \Phi : \Omega^k_G \longrightarrow \Lambda^k\mathfrak{g}^{\ast}, \qquad \Phi(\omega) = \omega_e ,
> $$
>
> is an isomorphism of vector spaces. Its inverse is $\Psi(\eta) = \omega^\eta$, where for $g \in G$ and $w^1, \ldots, w^k \in T_gG$
>
> $$
> \omega^\eta_g(w^1, \ldots, w^k) = \eta\big( d(L_{g^{-1}})_g w^1, \ldots, d(L_{g^{-1}})_g w^k \big) .
> $$
>
> In particular $\dim \Omega^k_G = \binom{n}{k}$ for $n = \dim G$.
>
> *Source: Assignment 9, Problem 4(a)*

^prop-84-9

> [!proof]+ Proof
> *(Assignment 9, Problem 4(a), as submitted. The assignment does not ask for the smoothness of $\omega^\eta$; it is filled in at the end.)* *$\Phi$ is linear and injective.* $(a\omega + b\omega')_e = a\,\omega_e + b\,\omega'_e$. If $\omega_e = 0$, then $\omega_g = 0$ for every $g$ by Lemma [[§84 Contraction by Vector Fields#^lem-84-7|§84.7]](3), so $\omega = 0$.
>
> *The map back.* For $\eta \in \Lambda^k\mathfrak{g}^{\ast}$, the formula for $\omega^\eta_g$ reads Lemma [[§84 Contraction by Vector Fields#^lem-84-7|§84.7]](3) as a definition. Since $\eta$ is alternating and $k$-linear and $d(L_{g^{-1}})_g$ is linear, $\omega^\eta_g \in \Lambda^k T_g^{\ast}G$: $\omega^\eta$ is a $k$-form on $G$. It depends linearly on $\eta$.
>
> *$\omega^\eta$ is left-invariant.* Let $g, h \in G$ and $v^1, \ldots, v^k \in T_hG$. Since $L_{(gh)^{-1}} \circ L_g = L_{h^{-1}g^{-1}g} = L_{h^{-1}}$ and $L_g(h) = gh$, the chain rule gives $d(L_{(gh)^{-1}})_{gh} \circ d(L_g)_h = d(L_{h^{-1}})_h$. Hence
>
> $$
> \begin{aligned}\omega^\eta_{gh}\big( d(L_g)_h v^1, \ldots, d(L_g)_h v^k \big) &= \eta\big( d(L_{(gh)^{-1}})_{gh}\, d(L_g)_h v^1, \ldots, d(L_{(gh)^{-1}})_{gh}\, d(L_g)_h v^k \big) \\
> &= \eta\big( d(L_{h^{-1}})_h v^1, \ldots, d(L_{h^{-1}})_h v^k \big) = \omega^\eta_h(v^1, \ldots, v^k) ,\end{aligned}
> $$
>
> which is left-invariance by Lemma [[§84 Contraction by Vector Fields#^lem-84-7|§84.7]](1).
>
> *$\Phi \circ \Psi = \mathrm{id}$.* Since $L_{e^{-1}} = L_e = \mathrm{id}_G$, $d(L_{e^{-1}})_e = \mathrm{id}_{T_eG}$, so $\omega^\eta_e = \eta$. *$\Psi \circ \Phi = \mathrm{id}$.* For $\omega \in \Omega^k_G$, the definition of $\omega^{\omega_e}$ and Lemma [[§84 Contraction by Vector Fields#^lem-84-7|§84.7]](3) give $\omega^{\omega_e}_g = \omega_g$ for every $g$.
>
> *$\omega^\eta$ is smooth* *(not from the assignment; filled in)*. Let $(e_1, \ldots, e_n)$ be a basis of $\mathfrak{g}$ and $\mathbf{X}_i = \mathbf{X}^{e_i}$, smooth vector fields on $G$ (Proposition [[§60 Lie Groups and Left-Invariant Vector Fields#^prop-60-8|§60.8]]); at each $g$ the vectors $\mathbf{X}_i|_g = d(L_g)_e e_i$ form a basis of $T_gG$ (Lemma [[§84 Contraction by Vector Fields#^lem-84-7|§84.7]](2)). Let $(U, (x^j))$ be a chart of $G$. On $U$, $\mathbf{X}_i = \sum_j a^j_i\, \partial/\partial x^j$ with smooth $a^j_i$ (Proposition [[§56 Vector Fields#^prop-56-1|§56.1]]), and the matrix $a = (a^j_i)$ is invertible at each point. Its inverse $b = a^{-1}$ has smooth entries, by the cofactor formula: each entry is a polynomial in the $a^j_i$ divided by $\det a \neq 0$. So $\partial/\partial x^j = \sum_i b^i_j\, \mathbf{X}_i$ on $U$, and by multilinearity the component functions of $\omega^\eta$ in the chart (Definition [[§80 Differential Forms on Manifolds#^def-80-3|§80.3]]) are
>
> $$
> \omega^\eta\Big( \frac{\partial}{\partial x^{a_1}}, \ldots, \frac{\partial}{\partial x^{a_k}} \Big) = \sum_{i_1, \ldots, i_k} b^{i_1}_{a_1} \cdots b^{i_k}_{a_k}\; \omega^\eta\big( \mathbf{X}_{i_1}, \ldots, \mathbf{X}_{i_k} \big) = \sum_{i_1, \ldots, i_k} b^{i_1}_{a_1} \cdots b^{i_k}_{a_k}\; \eta(e_{i_1}, \ldots, e_{i_k}) ,
> $$
>
> by Lemma [[§84 Contraction by Vector Fields#^lem-84-8|§84.8]]. These are smooth, so $\omega^\eta \in \Omega^k(G)$ (Definition [[§80 Differential Forms on Manifolds#^def-80-4|§80.4]]), and $\omega^\eta \in \Omega^k_G$.
>
> *The dimension.* $\dim \Lambda^k\mathfrak{g}^{\ast} = \binom{n}{k}$ (Proposition [[§75 Multilinear Algebra#^prop-75-6|§75.6]]).

^pf-84-9

*Uses:* [[§84 Contraction by Vector Fields#^lem-84-7|§84.7]], [[§60 Lie Groups and Left-Invariant Vector Fields#^prop-60-8|§60.8]], [[§56 Vector Fields#^prop-56-1|§56.1]], [[§80 Differential Forms on Manifolds#^def-80-3|Def. §80.3]], [[§84 Contraction by Vector Fields#^lem-84-8|§84.8]], [[§80 Differential Forms on Manifolds#^def-80-4|Def. §80.4]], [[§75 Multilinear Algebra#^prop-75-6|§75.6]]

> [!theorem] Proposition §84.10: The Exterior Derivative Preserves Left-Invariant Forms
> $d$ maps $\Omega^k_G$ into $\Omega^{k+1}_G$.
>
> *Source: Assignment 9, Problem 4(b)*

^prop-84-10

> [!proof]+ Proof
> *(Assignment 9, Problem 4(b), as submitted.)* Let $\omega \in \Omega^k_G$. For every $g \in G$, $L_g^{\ast}(d\omega) = d(L_g^{\ast}\omega) = d\omega$: the first equality is the naturality of $d$ (Theorem [[§81 The Exterior Derivative#^thm-81-7|§81.7]](4)) for the smooth map $L_g : G \to G$, and the second is $L_g^{\ast}\omega = \omega$.

^pf-84-10

*Uses:* [[§81 The Exterior Derivative#^thm-81-7|§81.7]]

> [!theorem] Theorem §84.11: The Exterior Derivative on the Lie Algebra
> Under the isomorphisms $\Phi$ of Proposition [[§84 Contraction by Vector Fields#^prop-84-9|§84.9]], $d : \Omega^k_G \to \Omega^{k+1}_G$ corresponds to the operator
>
> $$
> D = \Phi \circ d \circ \Psi : \Lambda^k\mathfrak{g}^{\ast} \longrightarrow \Lambda^{k+1}\mathfrak{g}^{\ast}, \qquad D\eta = \big(d\omega^\eta\big)_e ,
> $$
>
> and for $v_0, \ldots, v_k \in \mathfrak{g}$
>
> $$
> (D\eta)(v_0, \ldots, v_k) = \sum_{0 \le i < j \le k} (-1)^{i+j}\; \eta\big( [v_i, v_j], v_0, \ldots, \widehat{v_i}, \ldots, \widehat{v_j}, \ldots, v_k \big) .
> $$
>
> *Source: Assignment 9, Problem 4(c)*

^thm-84-11

> [!proof]+ Proof
> *(Assignment 9, Problem 4(c), as submitted.)* By Proposition [[§84 Contraction by Vector Fields#^prop-84-10|§84.10]], $d\omega^\eta \in \Omega^{k+1}_G$, so $D$ is well defined and $d\omega^\eta = \Psi(D\eta)$. Let $v_0, \ldots, v_k \in \mathfrak{g}$ and $\mathbf{X}_i = \mathbf{X}^{v_i}$, so that $\mathbf{X}_i|_e = v_i$. Since the value of a form at $e$ depends only on the vectors at $e$,
>
> $$
> (D\eta)(v_0, \ldots, v_k) = (d\omega^\eta)_e(v_0, \ldots, v_k) = \big( d\omega^\eta(\mathbf{X}_0, \ldots, \mathbf{X}_k) \big)(e) .
> $$
>
> *The global formula.* By Theorem [[§84 Contraction by Vector Fields#^thm-84-6|§84.6]],
>
> $$
> \begin{aligned}d\omega^\eta(\mathbf{X}_0, \ldots, \mathbf{X}_k) ={}& \sum_{i=0}^{k} (-1)^{i}\; \mathbf{X}_i\Big( \omega^\eta\big(\mathbf{X}_0, \ldots, \widehat{\mathbf{X}_i}, \ldots, \mathbf{X}_k\big) \Big) \\
> &+ \sum_{0 \le i < j \le k} (-1)^{i+j}\; \omega^\eta\big( [\mathbf{X}_i, \mathbf{X}_j], \mathbf{X}_0, \ldots, \widehat{\mathbf{X}_i}, \ldots, \widehat{\mathbf{X}_j}, \ldots, \mathbf{X}_k \big) .\end{aligned}
> $$
>
> *The first sum vanishes.* By Lemma [[§84 Contraction by Vector Fields#^lem-84-8|§84.8]], for each $i$ the function
>
> $$
> \omega^\eta\big(\mathbf{X}_0, \ldots, \widehat{\mathbf{X}_i}, \ldots, \mathbf{X}_k\big) = \eta(v_0, \ldots, \widehat{v_i}, \ldots, v_k)
> $$
>
> is constant on $G$, and a vector field applied to a constant function gives $0$.
>
> *The second sum at $e$.* Using $\omega^\eta_e = \eta$, $\mathbf{X}_l|_e = v_l$ and $[\mathbf{X}_i, \mathbf{X}_j]_e = [v_i, v_j]$ (Definition [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-6|§60.6]]),
>
> $$
> \omega^\eta\big( [\mathbf{X}_i, \mathbf{X}_j], \mathbf{X}_0, \ldots, \widehat{\mathbf{X}_i}, \ldots, \widehat{\mathbf{X}_j}, \ldots, \mathbf{X}_k \big)(e) = \eta\big( [v_i, v_j], v_0, \ldots, \widehat{v_i}, \ldots, \widehat{v_j}, \ldots, v_k \big) .
> $$
>
> Adding these terms with their signs gives the formula.

^pf-84-11

*Uses:* [[§84 Contraction by Vector Fields#^prop-84-10|§84.10]], [[§84 Contraction by Vector Fields#^thm-84-6|§84.6]], [[§84 Contraction by Vector Fields#^lem-84-8|§84.8]], [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-6|Def. §60.6]]

> [!theorem] Corollary §84.12: The Operator $D$ in Low Degrees
> 1. For $k = 0$: $D = 0$ on $\Lambda^0\mathfrak{g}^{\ast} = \mathbb{R}$. The left-invariant functions are the constants.
> 2. For $k = 1$: $(D\eta)(v, w) = -\eta([v, w])$ for $\eta \in \mathfrak{g}^{\ast}$. Equivalently, for a left-invariant one-form $\theta$ and left-invariant fields $\mathbf{X}, \mathbf{Y}$: $d\theta(\mathbf{X}, \mathbf{Y}) = -\theta([\mathbf{X}, \mathbf{Y}])$.
> 3. $D \circ D = 0$.
> 4. For $\eta \in \mathfrak{g}^{\ast}$: $\big(D(D\eta)\big)(u, v, w) = \eta\big( {[}[u, v], w] + {[}[v, w], u] + {[}[w, u], v] \big)$. So on $\mathfrak{g}^{\ast}$ the identity $D \circ D = 0$ is the Jacobi identity.
>
> *Source: not from the assignment*

^cor-84-12

> [!proof]+ Proof
> *(Not from the assignment; filled in. The formula of Theorem [[§84 Contraction by Vector Fields#^thm-84-11|§84.11]] is read off for small $k$, together with what $d \circ d = 0$ gives.)* *(1)* For $k = 0$ the sum over $i < j$ in $\{0\}$ is empty. A left-invariant function $f$ satisfies $f \circ L_g = f$, so $f(g) = f(L_g(e)) = f(e)$. *(2)* For $k = 1$ the only pair is $(i, j) = (0, 1)$, with sign $(-1)^{0+1} = -1$: $(D\eta)(v_0, v_1) = -\eta([v_0, v_1])$. For $\theta = \omega^\eta$, $\mathbf{X} = \mathbf{X}^v$ and $\mathbf{Y} = \mathbf{X}^w$, both sides of the second formula are constant functions, by Lemma [[§84 Contraction by Vector Fields#^lem-84-8|§84.8]]: $d\theta$ is left-invariant (Proposition [[§84 Contraction by Vector Fields#^prop-84-10|§84.10]]), and $[\mathbf{X}, \mathbf{Y}]$ is a left-invariant field (Corollary [[§60 Lie Groups and Left-Invariant Vector Fields#^cor-60-6|§60.6]]). Their values at $e$ are $(D\eta)(v, w)$ and $-\eta([v, w])$. *(3)* $D \circ D = \Phi \circ d \circ \Psi \circ \Phi \circ d \circ \Psi = \Phi \circ d \circ d \circ \Psi = 0$, by $\Psi \circ \Phi = \mathrm{id}$ and $d \circ d = 0$ (Theorem [[§81 The Exterior Derivative#^thm-81-7|§81.7]](3)). *(4)* By the formula for $k = 2$ and then (2),
>
> $$
> \begin{aligned}\big(D(D\eta)\big)(v_0, v_1, v_2) &= -(D\eta)([v_0, v_1], v_2) + (D\eta)([v_0, v_2], v_1) - (D\eta)([v_1, v_2], v_0) \\
> &= \eta\big({[}[v_0, v_1], v_2]\big) - \eta\big({[}[v_0, v_2], v_1]\big) + \eta\big({[}[v_1, v_2], v_0]\big) ,\end{aligned}
> $$
>
> and $-{[}[v_0, v_2], v_1] = {[}[v_2, v_0], v_1]$. By (3) the left side is $0$ for every $\eta$, which says that the sum of the three double brackets is $0$: the Jacobi identity of $\mathfrak{g}$ (Corollary [[§60 Lie Groups and Left-Invariant Vector Fields#^cor-60-6|§60.6]]).

^pf-84-12

*Uses:* [[§84 Contraction by Vector Fields#^lem-84-8|§84.8]], [[§84 Contraction by Vector Fields#^prop-84-10|§84.10]], [[§60 Lie Groups and Left-Invariant Vector Fields#^cor-60-6|§60.6]], [[§81 The Exterior Derivative#^thm-81-7|§81.7]], [[§84 Contraction by Vector Fields#^thm-84-11|§84.11]]

> [!definition] Definition §84.3: Lie Algebra Cohomology
> The formula of Theorem [[§84 Contraction by Vector Fields#^thm-84-11|§84.11]] uses only the bracket, so it defines operators $D : \Lambda^k\mathfrak{g}^{\ast} \to \Lambda^{k+1}\mathfrak{g}^{\ast}$ for any finite-dimensional Lie algebra $\mathfrak{g}$. The **cohomology of the Lie algebra** $\mathfrak{g}$ is
>
> $$
> H^k(\mathfrak{g}) = \frac{\ker\big( D : \Lambda^k\mathfrak{g}^{\ast} \to \Lambda^{k+1}\mathfrak{g}^{\ast} \big)}{\operatorname{im}\big( D : \Lambda^{k-1}\mathfrak{g}^{\ast} \to \Lambda^k\mathfrak{g}^{\ast} \big)} .
> $$
>
> *Source: Assignment 9, Problem 4(c)*

^def-84-3

> [!remark]- Connections
> - De Rham cohomology, of which this is the left-invariant part on a Lie group: [[§82 De Rham Cohomology|§82]].

For the Lie algebra of a Lie group, $D \circ D = 0$ by Corollary [[§84 Contraction by Vector Fields#^cor-84-12|§84.12]](3), so the image is contained in the kernel, as for de Rham cohomology (Lemma [[§82 De Rham Cohomology#^lem-82-1|§82.1]]); for an abstract Lie algebra $D \circ D = 0$ follows from the Jacobi identity, a computation not done here. $H^k(\mathfrak{g})$ is the cohomology of the complex of left-invariant forms on $G$, a subcomplex of the de Rham complex of $G$.

> [!example] Example §84.2: Lie Algebra Cohomology in the Simplest Cases
> 1. If $\mathfrak{g}$ is abelian, all brackets vanish, so $D = 0$ and $H^k(\mathfrak{g}) = \Lambda^k\mathfrak{g}^{\ast}$, of dimension $\binom{n}{k}$. On the group $\mathbb{R}^n$ the left-invariant forms are the forms $\sum_A c_A\, dx^A$ with constant coefficients, and they are all closed.
> 2. For any $\mathfrak{g}$, $H^0(\mathfrak{g}) = \mathbb{R}$, and $H^1(\mathfrak{g}) = \{\eta \in \mathfrak{g}^{\ast} : \eta([v, w]) = 0 \text{ for all } v, w\}$, the linear functions that vanish on all brackets: by Corollary [[§84 Contraction by Vector Fields#^cor-84-12|§84.12]], $D$ is zero in degree $0$, so nothing is divided out in degree $1$, and $D\eta = 0$ means $\eta([v, w]) = 0$.
>
> *Source: not from the assignment*

^ex-84-2
