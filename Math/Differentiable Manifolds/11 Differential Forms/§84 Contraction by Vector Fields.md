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
> - The Lie derivative along $\mathbf{X}$, the operation that $d$ and $\iota_\mathbf{X}$ combine to give in Cartan's magic formula: [[§72 Lie Derivatives#^def-72-2|Def. §72.2]]; for forms, [[§85 Lie Derivatives of Forms#^def-85-1|Def. §85.1]], and the formula, [[§86 Cartan's Magic Formula#^thm-86-2|Thm. §86.2]].

The first slot is a convention. There is a point-by-point version: for a vector $v \in T_pM$, $\iota_v : \Lambda^k T_p^{\ast}M \to \Lambda^{k-1} T_p^{\ast}M$ inserts $v$ in the first slot, and $(\iota_\mathbf{X}\alpha)_p = \iota_{\mathbf{X}_p}\alpha_p$. For $k = 0$ there is no slot for a vector field, so the expression makes no sense; it is very convenient to define it to be zero. The operators $\iota_\mathbf{X}$ go down by one in degree, $\Omega^k(M) \to \Omega^{k-1}(M)$, on a single manifold; the properties of the map $\alpha \mapsto \iota_\mathbf{X}\alpha$ will be studied later.

> [!theorem] Lemma §84.1: Contraction Gives a Smooth Form
> *(Not from lecture; filled in.)* For $\alpha \in \Omega^k(M)$ and $\mathbf{X} \in \mathfrak{X}(M)$, $\iota_\mathbf{X}\alpha$ is a smooth $(k-1)$-form, and $\iota_\mathbf{X}\alpha$ is linear in $\alpha$, and $C^\infty(M)$-linear in $\mathbf{X}$: $\iota_{f\mathbf{X} + \mathbf{Y}}\alpha = f\, \iota_\mathbf{X}\alpha + \iota_\mathbf{Y}\alpha$.

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
> *(Lecture 33, an observation.)* If $\alpha, \beta \in \Omega^k(M)$ satisfy $\alpha(\mathbf{X}_1, \ldots, \mathbf{X}_k) = \beta(\mathbf{X}_1, \ldots, \mathbf{X}_k)$ for all $\mathbf{X}_1, \ldots, \mathbf{X}_k \in \mathfrak{X}(M)$, then $\alpha = \beta$: the full contractions with all vector fields determine the form.

^prop-84-3

> [!proof]+ Proof
> *(Lecture 33: every tangent vector can be extended to a vector field, as in the homework, Theorem [[§65 Partitions of Unity#^thm-65-11|§65.11]]; the extension of a single vector is filled in.)* Let $p \in M$ and $v^1, \ldots, v^k \in T_pM$. Each $v^j$ extends to a smooth field: in a chart $(U, (x^i))$ at $p$ write $v^j = \sum_i a^i \partial_i|_p$, take a bump function $\chi$ at $p$ supported in $U$ (Corollary [[§56 Vector Fields#^cor-56-7|§56.7]]), and let $\mathbf{X}_j = \chi \sum_i a^i \partial_i$ on $U$ and $0$ outside $U$; it is smooth, since $\chi$ vanishes near the boundary of $U$ in $M$, and $\mathbf{X}_j|_p = v^j$ because $\chi(p) = 1$. Then $\alpha_p(v^1, \ldots, v^k) = \alpha(\mathbf{X}_1, \ldots, \mathbf{X}_k)(p) = \beta(\mathbf{X}_1, \ldots, \mathbf{X}_k)(p) = \beta_p(v^1, \ldots, v^k)$.

^pf-84-3

*Uses:* [[§65 Partitions of Unity#^thm-65-11|§65.11]], [[§56 Vector Fields#^cor-56-7|§56.7]]

*The global formula for $d$.* One reason to be interested in contractions is the *global formula* for $d$. For a one-form $\alpha$, $d\alpha$ is a two-form, so it can be contracted twice: putting the fields $\mathbf{X}$ and $\mathbf{Y}$ inside gives a function, and that function has a formula in terms of $\alpha$ alone.

> [!theorem] Theorem §84.4: Global Formula for $d$ on One-Forms
> Let $\alpha \in \Omega^1(M)$ and $\mathbf{X}, \mathbf{Y} \in \mathfrak{X}(M)$. Then
>
> $$
> d\alpha(\mathbf{X}, \mathbf{Y}) = \mathbf{X}\big(\alpha(\mathbf{Y})\big) - \mathbf{Y}\big(\alpha(\mathbf{X})\big) - \alpha\big([\mathbf{X}, \mathbf{Y}]\big) .
> $$
>
> *Lee: Proposition 14.29*

^thm-84-4

> [!proof]+ Proof (to be filled after the homework)
> *(Lecture 33 gave the following plan, without the computations.)* Denote the right-hand side by $\mathcal{R}(\mathbf{X}, \mathbf{Y})$; $\alpha$ is fixed and does not enter the notation.
>
> 1. *First,* show that $\mathcal{R}(f\mathbf{X}, g\mathbf{Y}) = fg\, \mathcal{R}(\mathbf{X}, \mathbf{Y})$ for all $f, g \in C^\infty(M)$. If the theorem is to be true, this must hold: $d\alpha$ is a form, pointwise linear, so the $f$ and the $g$ come out of the left-hand side. It is a computation with the Leibniz rule, in which all the derivatives of $f$ and $g$ cancel.
> 2. *Second,* check the identity for $\mathbf{X} = \partial/\partial x^a$ and $\mathbf{Y} = \partial/\partial x^b$ in a coordinate system $(x^1, \ldots, x^m)$. These fields commute, so the bracket term goes away.
>
> These two imply the general case, because in coordinates any $\mathbf{X}$ and $\mathbf{Y}$ are linear combinations of the coordinate fields with smooth coefficients, and the right-hand side is linear over $C^\infty$.
>
> The two computations were not done on the board. The formula for $k$-forms is the reading of the last problem of the current homework, so they are written out here after it is handed in.

^pf-84-4

> [!remark]- Connections
> - The Lie bracket: [[§58 Lie Bracket and Lie Algebra#^def-58-1|Def. §58.1]]; in coordinates, where the coordinate fields commute: [[§58 Lie Bracket and Lie Algebra#^prop-58-2|§58.2]].
> - $d$ in coordinates: [[§81 The Exterior Derivative#^cor-81-6|§81.6]].

*Reading the formula.* There are three terms, each a function. First, contract $\alpha$ with $\mathbf{Y}$, which gives the function $\alpha(\mathbf{Y})$, and apply $\mathbf{X}$ to it as an operator. Second, the same in the other order: contract with $\mathbf{X}$, then apply $\mathbf{Y}$. Third, the two fields have a commutator, the Lie bracket $[\mathbf{X}, \mathbf{Y}]$ (Definition [[§58 Lie Bracket and Lie Algebra#^def-58-1|§58.1]]), another field, and $\alpha$ can be contracted with it. The gain: there is no $d$ on the right-hand side, only $\alpha$ by itself. The price: $\mathbf{X}$ and $\mathbf{Y}$ must be fields, and the right-hand side is not a pointwise calculation, since it differentiates. For $k$-forms there is a formula of the same kind, with many more ways of contracting on the right (Lee, Proposition 14.32); it was assigned as reading, and is not written here.

*Convention.* The formula depends on the determinant convention for the wedge product (the remark *Two Conventions for the Wedge Product* in [[§77 The Wedge Product|§77]]), which is also Lee's; with the Alt convention a factor $\frac12$ appears on the left.
