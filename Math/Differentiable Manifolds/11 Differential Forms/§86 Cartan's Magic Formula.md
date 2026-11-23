---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 11
section: 86
tags: [differentiable-manifolds, math591]
---
← [[§85 Lie Derivatives of Forms]] · ↑ [[· 11 Differential Forms]]

*Stage: forms — The Lie derivative of forms written with $d$ and the contraction alone: $\mathcal{L}_\mathbf{X} = d\,\iota_\mathbf{X} + \iota_\mathbf{X}\, d$. A chain homotopy, and the first step to homotopy invariance of de Rham cohomology.*

*(Lecture 34.)* Cartan's magic formula writes the Lie derivative of forms with the exterior derivative and the contraction $\iota_\mathbf{X}$ ([[§84 Contraction by Vector Fields|§84]]) alone. Contract the form by $\mathbf{X}$, which gives degree $k - 1$, and apply $d$, which returns to degree $k$; or do it in the opposite order, $d$ first, to degree $k + 1$, then $\iota_\mathbf{X}$, back to degree $k$. The sum of those two is the Lie derivative.

![[m591-81-3.svg]]

*(Figure after the board.)* Here $\mathbf{X} \in \mathfrak{X}(M)$. Two copies of the de Rham complex of one manifold $M$. The vertical arrows are $\mathcal{L}_\mathbf{X}$ (green on the board), and they commute with $d$ (Theorem [[§85 Lie Derivatives of Forms#^thm-85-4|§85.4]](3)): the squares commute. The diagonal arrows are $\iota_\mathbf{X}$, which go down one degree. Cartan's formula says that the vertical arrow out of $\Omega^k(M)$ is the sum of the two paths made of one $d$ and one $\iota_\mathbf{X}$: first $\iota_\mathbf{X}$ (the diagonal) and then the bottom $d$, plus first the top $d$ and then the next diagonal $\iota_\mathbf{X}$. There are different $d$'s and different $\iota$'s, in different degrees, all written the same way.

The proof uses one more property of the contraction, which Lecture 34 stated in the middle of the proof.

> [!theorem] Lemma §86.1: Contraction Is an Antiderivation
> For $\mathbf{X} \in \mathfrak{X}(M)$, $\alpha \in \Omega^k(M)$ and $\beta \in \Omega^l(M)$,
>
> $$
> \iota_\mathbf{X}(\alpha \wedge \beta) = (\iota_\mathbf{X}\alpha) \wedge \beta + (-1)^{|\alpha|}\, \alpha \wedge (\iota_\mathbf{X}\beta) .
> $$
>
> *Lee: Lemma 14.13(b)*

^lem-86-1

> [!proof]+ Proof (to be filled after the homework)
> *(Stated in Lecture 34.)* The proof is a computation with shuffles, pointwise, from Definition [[§77 The Wedge Product#^def-77-1|§77.1]]. The contraction is on the current homework, so the proof is written here after it is handed in.

^pf-86-1

*Uses:* [[§77 The Wedge Product#^def-77-1|Def. §77.1]]

For $k = 0$, $\alpha = f$, the formula reads $\iota_\mathbf{X}(f\beta) = f\, \iota_\mathbf{X}\beta$, consistent with $\iota_\mathbf{X} f = 0$ (Definition [[§84 Contraction by Vector Fields#^def-84-1|§84.1]]) and with Lemma [[§84 Contraction by Vector Fields#^lem-84-1|§84.1]].

> [!theorem] Theorem §86.2: Cartan's Magic Formula
> For $\mathbf{X} \in \mathfrak{X}(M)$ and $\alpha \in \Omega^k(M)$,
>
> $$
> \mathcal{L}_\mathbf{X}\alpha = d\big(\iota_\mathbf{X}\alpha\big) + \iota_\mathbf{X}\big(d\alpha\big) ,
> $$
>
> where $\iota_\mathbf{X}\alpha$ has degree $k - 1$ and $d\alpha$ has degree $k + 1$. In short, $\mathcal{L}_\mathbf{X} = d \circ \iota_\mathbf{X} + \iota_\mathbf{X} \circ d$ on $\Omega^k(M)$.
>
> *Lee: Theorem 14.35*

^thm-86-2

> [!remark]- Connections
> - The proof has the same format as the proof that the Lie derivative of a vector field is the bracket, through straightening coordinates: [[§72 Lie Derivatives#^thm-72-6|Thm. §72.6]], with [[§72 Lie Derivatives#^lem-72-5|Lem. §72.5]].
> - The contraction: [[§84 Contraction by Vector Fields#^def-84-1|Def. §84.1]]; the exterior derivative: [[§81 The Exterior Derivative#^thm-81-7|Thm. §81.7]].

The formula has several applications; the first is Corollary [[§86 Cartan's Magic Formula#^cor-86-4|§86.4]] below. In algebraic topology (MATH 592) an identity of this shape is called a *chain homotopy*: $\iota_\mathbf{X}$ is a chain homotopy between $\mathcal{L}_\mathbf{X}$ and the zero map. The proof below is different from Lee's (which uses induction on the degree, with the product rules); it has exactly the same format as the proof that the Lie derivative of a vector field is the bracket (Theorem [[§72 Lie Derivatives#^thm-72-6|§72.6]]), through the normal form of a non-vanishing field.

> [!proof]+ Proof
> *(Lecture 34; the details marked are filled in.)* Both sides are $k$-forms. Fix $p \in M$. *(Filled in.)* Both sides at $p$ depend only on $\alpha$ and $\mathbf{X}$ near $p$: the left side through the flow near $p$ for small $|t|$, the right side because $d$ and $\iota_\mathbf{X}$ are local (Corollary [[§81 The Exterior Derivative#^cor-81-6|§81.6]]; Definition [[§84 Contraction by Vector Fields#^def-84-1|§84.1]] is pointwise).
>
> *1st: $\mathbf{X}_p \neq 0$.* Work locally near $p$, in coordinates $(x^1, \ldots, x^m)$ where $\mathbf{X} = \partial/\partial x^1$ (Lemma [[§72 Lie Derivatives#^lem-72-5|§72.5]]). Both sides are linear in $\alpha$ (Theorem [[§85 Lie Derivatives of Forms#^thm-85-4|§85.4]](1) in $\alpha$; $d$ and $\iota_\mathbf{X}$ are linear), so without loss of generality $\alpha = f_A\, dx^A$ is a monomial. The left-hand side was computed in Example [[§85 Lie Derivatives of Forms#^ex-85-1|§85.1]]:
>
> $$
> \mathcal{L}_\mathbf{X}\alpha = \frac{\partial f_A}{\partial x^1}\, dx^A .
> $$
>
> For the right-hand side there are two terms. Recall that $\iota_\mathbf{X}$ inserts $\mathbf{X}$ in the first slot, so it does nothing to the function $f_A$: $\iota_\mathbf{X}\alpha = f_A\, \iota_\mathbf{X}(dx^A)$. *(Filled in.)* The form $\iota_\mathbf{X}(dx^A) = \iota_{\partial/\partial x^1}(dx^A)$ has constant coefficients: by Definition [[§84 Contraction by Vector Fields#^def-84-1|§84.1]] and Lemma [[§78 Properties of the Wedge Product#^lem-78-2|§78.2]], $(\iota_{\partial_1} dx^A)(v^1, \ldots, v^{k-1}) = \det$ of the $k \times k$ matrix whose first column is $\big(dx^{a_i}(\partial_1)\big)_i = (\delta^{a_i}_1)_i$; if $1 \notin A$ this column is zero, and if $1 \in A$ then $a_1 = 1$, the column is $e_1$, and expanding along it gives $dx^{a_2} \wedge \cdots \wedge dx^{a_k}$. Either way $d\big(\iota_\mathbf{X}(dx^A)\big) = 0$, and by the product rule (Theorem [[§81 The Exterior Derivative#^thm-81-7|§81.7]](2)),
>
> $$
> d\,\iota_\mathbf{X}\alpha = d\big(f_A\, \iota_\mathbf{X}(dx^A)\big) = df_A \wedge \iota_\mathbf{X}(dx^A) .
> $$
>
> The other term uses $d\alpha = df_A \wedge dx^A$ and Lemma [[§86 Cartan's Magic Formula#^lem-86-1|§86.1]], with $|df_A| = 1$:
>
> $$
> \iota_\mathbf{X}\, d\alpha = \iota_\mathbf{X}\big(df_A \wedge dx^A\big) = \big(\iota_\mathbf{X}\, df_A\big)\, dx^A - df_A \wedge \iota_\mathbf{X}(dx^A) .
> $$
>
> When the two are added, which is the right-hand side of Cartan's formula, the term $df_A \wedge \iota_\mathbf{X}(dx^A)$ cancels, so it never has to be computed. What remains is $(\iota_\mathbf{X}\, df_A)\, dx^A$, and since $\mathbf{X} = \partial/\partial x^1$,
>
> $$
> \iota_\mathbf{X}\, df_A = df_A\Big( \frac{\partial}{\partial x^1} \Big) = \sum_{j=1}^m \frac{\partial f_A}{\partial x^j}\, dx^j\Big( \frac{\partial}{\partial x^1} \Big) = \sum_{j=1}^m \frac{\partial f_A}{\partial x^j}\, \delta^j_1 = \frac{\partial f_A}{\partial x^1} .
> $$
>
> So the right-hand side is $\frac{\partial f_A}{\partial x^1}\, dx^A$, the left-hand side. This proves the formula on a neighbourhood of every point where $\mathbf{X}$ does not vanish.
>
> *2nd: $p \in M \setminus \operatorname{supp}\mathbf{X}$*, where $\operatorname{supp}\mathbf{X} = \overline{\{q \in M : \mathbf{X}_q \neq 0\}}$, as for functions (Definition [[§56 Vector Fields#^def-56-10|§56.10]]). Both sides are zero at $p$. *(Filled in.)* $\mathbf{X}$ vanishes on a neighbourhood $W$ of $p$, so the constant curves are its integral curves there, $\varphi_t = \mathrm{id}$ on $W$, $\alpha_p(t) = \alpha_p$ and $(\mathcal{L}_\mathbf{X}\alpha)_p = 0$; and $\iota_\mathbf{X}\alpha$ and $\iota_\mathbf{X}\,d\alpha$ vanish on $W$, so $d(\iota_\mathbf{X}\alpha)$ vanishes at $p$ as well.
>
> *The remaining points: $\mathbf{X}_p = 0$ and $p \in \operatorname{supp}\mathbf{X}$*, for instance $p$ on the boundary of the support. The formula follows by continuity. *(Filled in.)* Every neighbourhood of $p$ contains points $q$ with $\mathbf{X}_q \neq 0$, where the formula holds by the first case; both sides are smooth, in particular continuous, $k$-forms (Lemma [[§85 Lie Derivatives of Forms#^lem-85-2|§85.2]]), so in a chart at $p$ their components are continuous functions that agree at points accumulating at $p$, hence at $p$. This step, written out, is Lemma [[§85 Lie Derivatives of Forms#^lem-85-3|§85.3]], applied to the two sides of the formula.

^pf-86-2

*Uses:* [[§81 The Exterior Derivative#^cor-81-6|§81.6]], [[§84 Contraction by Vector Fields#^def-84-1|Def. §84.1]], [[§72 Lie Derivatives#^lem-72-5|§72.5]], [[§85 Lie Derivatives of Forms#^thm-85-4|§85.4]], [[§85 Lie Derivatives of Forms#^ex-85-1|Ex. §85.1]], [[§78 Properties of the Wedge Product#^lem-78-2|§78.2]], [[§81 The Exterior Derivative#^thm-81-7|§81.7]], [[§86 Cartan's Magic Formula#^lem-86-1|§86.1]], [[§56 Vector Fields#^def-56-10|Def. §56.10]], [[§85 Lie Derivatives of Forms#^lem-85-2|§85.2]], [[§85 Lie Derivatives of Forms#^lem-85-3|§85.3]]

**Transcription notes (Lecture 34).** In the handwritten notes the first term appears as $d\,\iota_\mathbf{X}\alpha = df_A \wedge d\,\iota_\mathbf{X}(dx^A)$ and the second as $\iota_\mathbf{X} d\alpha = (\iota_\mathbf{X} df_A) \wedge dx^A - df_A \wedge d\big(\iota_\mathbf{X}(dx^A)\big)$; in both places the term is $df_A \wedge \iota_\mathbf{X}(dx^A)$, with no second $d$, as said in the lecture, and it cancels. In the second case the lecture first said the complement of the support of $\alpha$, and corrected it to the support of $\mathbf{X}$. The board's last case, “$p \in \partial\operatorname{supp}(\mathbf{X})$”, should include all zeros of $\mathbf{X}$ in its support, not only the boundary points: the three cases must cover $M$, and the continuity argument applies to all of them.

![[m591-81-4.svg]]

*(Not from lecture; figure added.)* The three kinds of points in the proof of Theorem [[§86 Cartan's Magic Formula#^thm-86-2|§86.2]]: at $p_1$, $\mathbf{X}_{p_1} \neq 0$ and there are straightening coordinates; $p_2 \notin \operatorname{supp}\mathbf{X}$, where both sides are $0$; at $p_3$, $\mathbf{X}_{p_3} = 0$ but $p_3$ is a limit of points of the first kind. The points of the third kind include the boundary of the support, and also zeros of $\mathbf{X}$ inside the support (such as the origin for $x\,\partial/\partial x$ on $\mathbb{R}$).

> [!theorem] Corollary §86.3: The Lie Derivative Is Linear in the Field
> Let $\alpha \in \Omega^k(M)$.
>
> 1. $\mathcal{L}_{\mathbf{X} + c\mathbf{Y}}\alpha = \mathcal{L}_\mathbf{X}\alpha + c\,\mathcal{L}_\mathbf{Y}\alpha$ for $\mathbf{X}, \mathbf{Y} \in \mathfrak{X}(M)$ and $c \in \mathbb{R}$.
> 2. $d\,\mathcal{L}_\mathbf{X}\alpha = d\,\iota_\mathbf{X}\, d\alpha = \mathcal{L}_\mathbf{X}\, d\alpha$: Cartan's formula gives Theorem [[§85 Lie Derivatives of Forms#^thm-85-4|§85.4]](3) again.
>
> *Source: Lecture 34 · proof filled in*
>
> *Lee: Corollary 14.36*

^cor-86-3

> [!proof]+ Proof
> *(Not from lecture; filled in. Lecture 34 stated (1) together with Theorem [[§85 Lie Derivatives of Forms#^thm-85-4|§85.4]](1).)* (1) The right-hand side of Cartan's formula is linear in $\mathbf{X}$, because $\iota_{\mathbf{X} + c\mathbf{Y}} = \iota_\mathbf{X} + c\,\iota_\mathbf{Y}$ (Lemma [[§84 Contraction by Vector Fields#^lem-84-1|§84.1]]) and $d$ is linear. (2) $d \circ d = 0$ kills one term on each side: $d\,\mathcal{L}_\mathbf{X} = d\,d\,\iota_\mathbf{X} + d\,\iota_\mathbf{X}\, d = d\,\iota_\mathbf{X}\, d$ and $\mathcal{L}_\mathbf{X}\, d = d\,\iota_\mathbf{X}\, d + \iota_\mathbf{X}\, d\, d = d\,\iota_\mathbf{X}\, d$. The proof of Theorem [[§86 Cartan's Magic Formula#^thm-86-2|§86.2]] used only linearity in $\alpha$ from Theorem [[§85 Lie Derivatives of Forms#^thm-85-4|§85.4]], so there is no circularity.

^pf-86-3

*Uses:* [[§84 Contraction by Vector Fields#^lem-84-1|§84.1]], [[§86 Cartan's Magic Formula#^thm-86-2|§86.2]], [[§85 Lie Derivatives of Forms#^thm-85-4|§85.4]]

The first application concerns the maps induced on de Rham cohomology (Proposition [[§82 De Rham Cohomology#^prop-82-2|§82.2]]).

> [!theorem] Corollary §86.4: A Flow Acts Trivially on Cohomology
> Suppose $\mathbf{X}$ is complete, with flow $\varphi$. Fix $t \in \mathbb{R}$ and $k$. Then the map
>
> $$
> \varphi_t^{\ast} : H^k(M) \longrightarrow H^k(M)
> $$
>
> induced by the time-$t$ map $\varphi_t : M \to M$ (Proposition [[§82 De Rham Cohomology#^prop-82-2|§82.2]]) is the identity.
>
> *Lee: Ch. 17, Homotopy Invariance*

^cor-86-4

> [!remark]- Connections
> - Diffeomorphisms induce isomorphisms on cohomology: [[§82 De Rham Cohomology#^prop-82-2|Prop. §82.2]]; the corollary says more for the time-$t$ map of a complete field, which is homotopic to the identity through the $\varphi_s$.
> - A complete field: [[§70 Complete Vector Fields|§70]].

> [!proof]+ Proof (to be filled)
> *(Not proved in Lecture 34.)* The proof was announced for the next lecture: it uses Cartan's formula, and the form $\eta$ below is given by an integral involving $\iota_\mathbf{X}$.

^pf-86-4

*What this is saying.* Not just that $\varphi_t^{\ast}$ is invertible on cohomology (which holds for any diffeomorphism), but that it is the identity. If $\alpha \in \Omega^k(M)$ with $d\alpha = 0$, so that $[\alpha] \in H^k(M)$, then there exists $\eta \in \Omega^{k-1}(M)$ such that

$$
\varphi_t^{\ast}\alpha - \alpha = d\eta \qquad \Longleftrightarrow \qquad [\varphi_t^{\ast}\alpha] = [\alpha] .
$$

At the level of forms, $\varphi_t^{\ast}\alpha - \alpha$ is exact, so its class is zero. Any $(k-1)$-form $\eta$ with this property will do, and the proof has to produce one. This is the beginning of the homotopy invariance property of de Rham cohomology: the time-$t$ map depends smoothly on $t$, and as $t$ changes back to $0$ it is deformed continuously, through the maps $\varphi_s$, to $\varphi_0 = \mathrm{id}_M$, which induces the identity on cohomology (in fact on forms). Because $\varphi_t$ can be connected smoothly to the identity, it also induces the identity in cohomology.
