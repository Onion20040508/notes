---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 10
section: 71
tags: [differentiable-manifolds, math591]
---
← [[§70 Complete Vector Fields]] · ↑ [[· 10 Integral Curves and Flows]] · [[§72 Lie Derivatives]] →

*Stage: Lie groups — The integral curve of a left-invariant field through the identity is a one-parameter subgroup; following it to time $1$ defines $\exp : \mathfrak{g} \to G$, the matrix exponential for linear groups, smooth and a local diffeomorphism at $0$.*

*Lecture 26: the exponential map of Lie groups. Last time: every left-invariant field on $G$ is complete (Theorem [[§70 Complete Vector Fields#^thm-70-11|§70.11]]). The exponential map comes from the integral curve of a left-invariant field $\mathbf{X}$ starting at the identity, which is special.*

*Notation.* The Lie algebra has two incarnations: the left-invariant fields with their bracket, and the tangent space at the identity (Theorem [[§60 Lie Groups and Left-Invariant Vector Fields#^thm-60-9|§60.9]]; the remark [[§61 Lie Group Morphisms and Linear Groups#^rem-61-1|From Now On]] ($\mathfrak{g}$ is $T_eG$) in [[§61 Lie Group Morphisms and Linear Groups|§61]]). Capital letters $A, B \in T_eG = \mathfrak{g}$ are vectors at the identity, and

$$
\mathbf{X}^A = \text{the corresponding left-invariant field, with } \mathbf{X}^A_e = A, \qquad \varphi^A = \text{the flow of } \mathbf{X}^A
$$

(Definition [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-5|§60.5]]).
So $\varphi^A_t(e)$ is the integral curve of $\mathbf{X}^A$ starting at $e$, evaluated at $t$; here the superscript is the vector $A$, and the point is in parentheses. $A \mapsto \mathbf{X}^A$ is linear, since $\mathbf{X}^A_g = d(L_g)_e(A)$; in particular $\mathbf{X}^{cA} = c\,\mathbf{X}^A$.

> [!theorem] Proposition §71.1: One-Parameter Subgroups
> Let $\mathbf{X}$ be a left-invariant vector field on a Lie group $G$, with flow $\varphi$. Then for all $s, t \in \mathbb{R}$
>
> $$
> \varphi_{t+s}(e) = \varphi_s(e) \cdot \varphi_t(e),
> $$
>
> the product in $G$. So $t \mapsto \varphi_t(e)$ is a group morphism from the additive group $(\mathbb{R}, +)$ to $G$.
>
> *Lee: Theorem 20.1*

^prop-71-1

> [!proof]+ Proof
> *(Lecture 26.)* $\mathbf{X}$ is complete (Theorem [[§70 Complete Vector Fields#^thm-70-11|§70.11]]), so all these are defined. Fix $s$. $\mathbf{X}$ is $L_{\varphi_s(e)}$-related to itself, because being left-invariant means being $L_g$-related to itself for every $g$ (Lemma [[§60 Lie Groups and Left-Invariant Vector Fields#^lem-60-5|§60.5]]). So, by Proposition [[§70 Complete Vector Fields#^prop-70-10|§70.10]],
>
> $$
> t \mapsto L_{\varphi_s(e)}\big(\varphi_t(e)\big)
> $$
>
> is an integral curve of $\mathbf{X}$, and it starts at $L_{\varphi_s(e)}(e) = \varphi_s(e)$: composing an integral curve of $\mathbf{X}$ with a map gives an integral curve of a related field, and here the related field is $\mathbf{X}$ itself. So is $t \mapsto \varphi_{t+s}(e)$, an integral curve by the translation lemma (Lemma [[§67 Integral Curves#^lem-67-4|§67.4]](1)) with value $\varphi_s(e)$ at $t = 0$. Therefore, by uniqueness (Proposition [[§68 Local Existence and Uniqueness#^prop-68-3|§68.3]]), for all $t$,
>
> $$
> \varphi_{t+s}(e) = L_{\varphi_s(e)}\big(\varphi_t(e)\big) = \varphi_s(e) \cdot \varphi_t(e) .
> $$
>
> Writing out what $L$ is, the group multiplication appears explicitly for the first time.

^pf-71-1

*Uses:* [[§70 Complete Vector Fields#^thm-70-11|§70.11]], [[§60 Lie Groups and Left-Invariant Vector Fields#^lem-60-5|§60.5]], [[§70 Complete Vector Fields#^prop-70-10|§70.10]], [[§67 Integral Curves#^lem-67-4|§67.4]], [[§68 Local Existence and Uniqueness#^prop-68-3|§68.3]]

This is the case $g = \varphi^e(s)$ of $\varphi^g(t) = g\,\varphi^e(t)$ in Theorem [[§70 Complete Vector Fields#^thm-70-11|§70.11]], combined with the group law $\varphi^{\varphi^e(s)}(t) = \varphi^e(t + s)$. Since $s + t = t + s$, the elements $\varphi_s(e)$ and $\varphi_t(e)$ commute: a one-parameter subgroup is abelian, even in a non-abelian $G$.

Conversely, every smooth group morphism $\mathbb{R} \to G$ arises this way; this was not pursued in lecture. *(Filled in, for smooth morphisms.)* If $\gamma : \mathbb{R} \to G$ is a smooth group morphism and $A = \dot\gamma(0)$, then differentiating $\gamma(t + s) = \gamma(t)\gamma(s) = L_{\gamma(t)}(\gamma(s))$ in $s$ at $s = 0$ gives $\dot\gamma(t) = d(L_{\gamma(t)})_e(A) = \mathbf{X}^A_{\gamma(t)}$ (Corollary [[§31 Tangent Vectors as Velocities of Curves#^cor-31-5|§31.5]]). So $\gamma$ is the integral curve of $\mathbf{X}^A$ starting at $\gamma(0) = e$, and $\gamma(t) = \varphi^A_t(e)$. Continuous group morphisms $\mathbb{R} \to G$ are automatically smooth (Lee, Problem 20-11(a); not proved in these notes), so the same holds for them.

The one-parameter subgroup is an orbit: the left-invariant field $\mathbf{X}^A$ is complete, so it generates an $\mathbb{R}$-action (Proposition [[§70 Complete Vector Fields#^prop-70-7|§70.7]]), and $t \mapsto \varphi^A_t(e)$ is the orbit of the identity.

> [!definition] Definition §71.1: The Exponential Map
> Let $G$ be a Lie group, with Lie algebra $\mathfrak{g} = T_eG$. The **exponential map** $\exp : \mathfrak{g} \to G$ is
>
> $$
> \exp(A) = \varphi^A_t(e)\big|_{t=1}, \qquad A \in \mathfrak{g} :
> $$
>
> make $A$ into the left-invariant field $\mathbf{X}^A$, take its flow, and follow the integral curve through $e$ up to time $1$.
>
> *Lee: Ch. 20, The Exponential Map*

^def-71-1

![[m591-71-4.svg]]

*(Figure after the board.)* The group is drawn like a sphere (think of a three-sphere). The vector $A$ in the tangent space $\mathfrak{g} = T_eG$ generates a one-parameter group; following it to time one gives a point $\exp(A)$ of the group.

The name is well motivated: for subgroups of the general linear group, $\exp$ is the matrix exponential (Theorem [[§71 The Exponential Map#^thm-71-11|§71.11]] below). The essential step is the following.

> [!theorem] Proposition §71.2: Exponentials of Multiples
> For all $t \in \mathbb{R}$ and $A \in \mathfrak{g}$,
>
> $$
> \exp(tA) = \varphi^A_t(e) .
> $$
>
> So $t \mapsto \exp(tA)$ is the one-parameter subgroup of Proposition [[§71 The Exponential Map#^prop-71-1|§71.1]] for $\mathbf{X}^A$.
>
> *Lee: Proposition 20.5*

^prop-71-2

> [!proof]+ Proof
> *(Lecture 26.)* For $t = 1$ this is the definition. In general, by definition,
>
> $$
> \exp(tA) = \varphi^{tA}_s(e)\big|_{s=1} :
> $$
>
> take the field $\mathbf{X}^{tA} = t\,\mathbf{X}^A$ and flow $e$ up to $s = 1$. By the rescaling lemma (Lemma [[§67 Integral Curves#^lem-67-4|§67.4]](2)), $s \mapsto \varphi^A_{ts}(e)$ is an integral curve of $t\,\mathbf{X}^A = \mathbf{X}^{tA}$, starting at $e$: the flow of $c\mathbf{X}$ is $\varphi_{ct}$, by the chain rule. By uniqueness (Proposition [[§68 Local Existence and Uniqueness#^prop-68-3|§68.3]]) it is $s \mapsto \varphi^{tA}_s(e)$, so
>
> $$
> \exp(tA) = \varphi^{tA}_s(e)\big|_{s=1} = \varphi^A_{ts}(e)\big|_{s=1} = \varphi^A_t(e) .
> $$

^pf-71-2

*Uses:* [[§67 Integral Curves#^lem-67-4|§67.4]], [[§68 Local Existence and Uniqueness#^prop-68-3|§68.3]]

> [!theorem] Corollary §71.4: The Exponential Law on a Line
> For all $s, t \in \mathbb{R}$ and $A \in \mathfrak{g}$,
>
> $$
> \exp\big((s + t)A\big) = \exp(sA) \cdot \exp(tA) .
> $$
>
> *Lee: Proposition 20.8*

^cor-71-4

> [!proof]+ Proof
> *(Lecture 26.)* By Proposition [[§71 The Exponential Map#^prop-71-2|§71.2]], then Proposition [[§71 The Exponential Map#^prop-71-1|§71.1]], then Proposition [[§71 The Exponential Map#^prop-71-2|§71.2]] twice:
>
> $$
> \exp\big((s + t)A\big) = \varphi^A_{s+t}(e) = \varphi^A_s(e) \cdot \varphi^A_t(e) = \exp(sA) \cdot \exp(tA) .
> $$

^pf-71-4

*Uses:* [[§71 The Exponential Map#^prop-71-2|§71.2]], [[§71 The Exponential Map#^prop-71-1|§71.1]]

This explains the name: it is an exponential law. In particular $\exp(0) = e$ and $\exp(-A) = \exp(A)^{-1}$.

> [!remark] Remark: Warning: $\exp(A + B) \neq \exp(A)\exp(B)$ in General
> It is *not* true in general that
>
> $$
> \exp(A + B) = \exp(A) \cdot \exp(B) .
> $$
>
> The reason: many Lie groups are non-abelian. The plus on the left is the addition in the tangent space at the identity, which is commutative, while the group law is not; so the identity cannot hold in general. There is a famous formula for $\exp(A)\exp(B)$, the Baker–Campbell–Hausdorff formula, a complicated series of iterated brackets of $A$ and $B$. For a single direction, $A$ and $B = cA$, the identity holds (Corollary [[§71 The Exponential Map#^cor-71-4|§71.4]]); more generally, it holds if $A$ and $B$ commute, which is not easy to show and is not proved in the course. (Lee, Problem 20-8, characterizes the groups where it holds for all $A$, $B$.)
>
> *(Not from lecture.)* A concrete failure in $\mathrm{GL}(2, \mathbb{R})$, using the matrix exponential of Theorem [[§71 The Exponential Map#^thm-71-11|§71.11]], is Example [[§71 The Exponential Map#^ex-71-1|§71.1]] below.

^rem-71-1

![[m591-71-3.svg]]

*(Not from lecture; figure added.)* The two matrices of Example [[§71 The Exponential Map#^ex-71-1|§71.1]] acting on the unit square: $\exp(A)\exp(B)$ (blue) and $\exp(A + B)$ (red). Both have determinant $1$, so the parallelograms have the same area, but they are different maps.

*(Assignment 7, Problem 5.)* The exponential map of a subgroup is the restriction of that of the larger group, because the integral curves are; for a linear group this identifies $\exp$ with the matrix exponential series, completing the proof of Theorem [[§71 The Exponential Map#^thm-71-11|§71.11]] below. The series facts are those of its proof: $e^{tA} = \sum_{\ell \ge 0} \frac{t^\ell}{\ell!} A^\ell$ converges and may be differentiated term by term, $\frac{d}{dt} e^{tA} = A\, e^{tA} = e^{tA} A$.

> [!theorem] Lemma §71.6: The Matrix Exponential Is Invertible
> For $A \in \operatorname{Mat}(n, \mathbb{R})$ and $t \in \mathbb{R}$, $e^{tA}\, e^{-tA} = I$. So $e^{tA} \in \mathrm{GL}(n, \mathbb{R})$, with inverse $e^{-tA}$.

^lem-71-6

> [!proof]+ Proof
> *(Not from lecture; filled in. The outline of the proof of Theorem [[§71 The Exponential Map#^thm-71-11|§71.11]] and the submitted solution of Assignment 7, Problem 5(b), use that $e^{tA}$ is invertible without proof.)* Each entry of a product of matrix-valued curves is a sum of products of entries, so the product rule holds: $\frac{d}{dt}(B(t)C(t)) = B'(t)C(t) + B(t)C'(t)$. With $\frac{d}{dt} e^{tA} = A e^{tA} = e^{tA} A$ and, by the chain rule, $\frac{d}{dt} e^{-tA} = -A\, e^{-tA}$,
>
> $$
> \frac{d}{dt}\big(e^{tA} e^{-tA}\big) = \big(e^{tA} A\big) e^{-tA} + e^{tA}\big(-A\, e^{-tA}\big) = 0 .
> $$
>
> So every entry of $e^{tA} e^{-tA}$ is a function on $\mathbb{R}$ with zero derivative, hence constant, and at $t = 0$ the product is $I \cdot I = I$. Thus $e^{tA} e^{-tA} = I$ for all $t$; then $\det(e^{tA}) \det(e^{-tA}) = 1$, so $e^{tA}$ is invertible, and its inverse is $e^{-tA}$, since a one-sided inverse of a square matrix is the inverse.

^pf-71-6

*Uses:* [[§71 The Exponential Map#^thm-71-11|§71.11]]

> [!theorem] Lemma §71.7: Integral Curves of a Left-Invariant Field on a Lie Subgroup
> Let $H$ be a Lie group and $G \subseteq H$ a subgroup that is a Lie group with the inclusion $\iota : G \hookrightarrow H$ smooth and $d\iota_e$ injective — a Lie subgroup, as in Theorem [[§61 Lie Group Morphisms and Linear Groups#^thm-61-5|§61.5]] — so that $\mathfrak{g} = T_eG$ is identified with $d\iota_e(\mathfrak{g}) \subseteq \mathfrak{h} = T_eH$. For $A \in \mathfrak{g}$ let $\mathbf{A}^G \in \mathfrak{X}(G)$ and $\mathbf{A}^H \in \mathfrak{X}(H)$ be the left-invariant fields with $\mathbf{A}^G_e = A$ and $\mathbf{A}^H_e = d\iota_e(A)$ (the fields written $\mathbf{X}^A$ in the notation of this section, one on each group). Then $\mathbf{A}^G$ is $\iota$-related to $\mathbf{A}^H$, and for every integral curve $\gamma$ of $\mathbf{A}^G$, $\iota \circ \gamma$ is an integral curve of $\mathbf{A}^H$.

^lem-71-7

> [!proof]+ Proof
> *(Assignment 7, Problem 5(a): the submitted solution. The relatedness is also Lemma [[§61 Lie Group Morphisms and Linear Groups#^lem-61-1|§61.1]] for the morphism $\iota$, and the second statement Proposition [[§70 Complete Vector Fields#^prop-70-10|§70.10]]; the solution proves both directly.)* $\iota$ is a Lie group morphism (Definition [[§61 Lie Group Morphisms and Linear Groups#^def-61-2|§61.2]]), and by Definition [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-5|§60.5]]
>
> $$
> \mathbf{A}^G_g = d(L_g)_e(A) \quad (g \in G), \qquad \mathbf{A}^H_h = d(L_h)_e\big(d\iota_e(A)\big) \quad (h \in H),
> $$
>
> where $L_g$ and $L_h$ are left translations in $G$ and in $H$.
>
> *$\mathbf{A}^G$ is $\iota$-related to $\mathbf{A}^H$.* Let $g \in G$. For $k \in G$, since $\iota$ is a homomorphism, $\iota \circ L_g(k) = \iota(gk) = \iota(g)\iota(k) = L_{\iota(g)} \circ \iota(k)$; so $\iota \circ L_g = L_{\iota(g)} \circ \iota$ as maps $G \to H$. Differentiating at $e$ by the chain rule, with $L_g(e) = g$ and $\iota(e) = e$,
>
> $$
> d\iota_g \circ d(L_g)_e = d(L_{\iota(g)})_e \circ d\iota_e : T_eG \to T_{\iota(g)}H .
> $$
>
> Applying both sides to $A$,
>
> $$
> d\iota_g\big(\mathbf{A}^G_g\big) = d\iota_g\big(d(L_g)_e(A)\big) = d(L_{\iota(g)})_e\big(d\iota_e(A)\big) = \mathbf{A}^H_{\iota(g)} \qquad \text{for all } g \in G .
> $$
>
> *Integral curves.* Let $\gamma : J \to G$ be an integral curve of $\mathbf{A}^G$, so $\gamma'(t) = \mathbf{A}^G_{\gamma(t)}$ for $t \in J$. The curve $\iota \circ \gamma : J \to H$ is smooth, and by the chain rule and the relatedness,
>
> $$
> (\iota \circ \gamma)'(t) = d\iota_{\gamma(t)}\big(\gamma'(t)\big) = d\iota_{\gamma(t)}\big(\mathbf{A}^G_{\gamma(t)}\big) = \mathbf{A}^H_{\iota(\gamma(t))} \qquad \text{for all } t \in J .
> $$
>
> So $\iota \circ \gamma$ is an integral curve of $\mathbf{A}^H$.

^pf-71-7

*Uses:* [[§61 Lie Group Morphisms and Linear Groups#^lem-61-1|§61.1]], [[§70 Complete Vector Fields#^prop-70-10|§70.10]], [[§61 Lie Group Morphisms and Linear Groups#^def-61-2|Def. §61.2]], [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-5|Def. §60.5]]

> [!theorem] Corollary §71.8: The Exponential Map of a Lie Subgroup
> In the setting of Lemma [[§71 The Exponential Map#^lem-71-7|§71.7]], for $A \in \mathfrak{g}$ and $t \in \mathbb{R}$,
>
> $$
> \iota\big(\exp_G(tA)\big) = \exp_H\big(t\, d\iota_e(A)\big) .
> $$
>
> So the exponential map of $G$ is the restriction of that of $H$ to $\mathfrak{g} \subseteq \mathfrak{h}$, and $\exp_H(tA) \in G$ for all $t$.

^cor-71-8

> [!proof]+ Proof
> *(Filled in.)* $\mathbf{A}^G$ is complete (Theorem [[§70 Complete Vector Fields#^thm-70-11|§70.11]]), and its integral curve starting at $e$ is $\gamma(t) = \exp_G(tA)$, $t \in \mathbb{R}$ (Proposition [[§71 The Exponential Map#^prop-71-2|§71.2]]). By Lemma [[§71 The Exponential Map#^lem-71-7|§71.7]], $\iota \circ \gamma$ is an integral curve of $\mathbf{A}^H$ defined on $\mathbb{R}$ and starting at $\iota(e) = e$; so it is the maximal integral curve of $\mathbf{A}^H$ starting at $e$ (Proposition [[§69 Maximal Integral Curves and Flows#^prop-69-1|§69.1]]), which is $t \mapsto \exp_H(t\, d\iota_e(A))$ (Proposition [[§71 The Exponential Map#^prop-71-2|§71.2]]).

^pf-71-8

*Uses:* [[§70 Complete Vector Fields#^thm-70-11|§70.11]], [[§71 The Exponential Map#^prop-71-2|§71.2]], [[§71 The Exponential Map#^lem-71-7|§71.7]], [[§69 Maximal Integral Curves and Flows#^prop-69-1|§69.1]]

> [!theorem] Corollary §71.9: Lie Group Morphisms Commute with the Exponential Map
> Let $F : H \to G$ be a Lie group morphism. Then $F(\exp_H A) = \exp_G\big(dF_e(A)\big)$ for every $A \in \mathfrak{h}$.
>
> *Lee: Proposition 20.8(g)*

^cor-71-9

> [!proof]+ Proof
> *(Not from the assignment; filled in: the proof of Corollary [[§71 The Exponential Map#^cor-71-8|§71.8]] with $F$ in place of $\iota$.)* Let $\mathbf{X}^A \in \mathfrak{X}(H)$ and $\mathbf{Y}^{\tilde A} \in \mathfrak{X}(G)$, $\tilde A = dF_e(A)$, be the left-invariant extensions; they are $F$-related (Lemma [[§61 Lie Group Morphisms and Linear Groups#^lem-61-1|§61.1]]). The integral curve $t \mapsto \exp_H(tA)$ of $\mathbf{X}^A$ starting at $e$ is defined on $\mathbb{R}$ (Theorem [[§70 Complete Vector Fields#^thm-70-11|§70.11]], Proposition [[§71 The Exponential Map#^prop-71-2|§71.2]]), so $t \mapsto F(\exp_H(tA))$ is an integral curve of $\mathbf{Y}^{\tilde A}$ on $\mathbb{R}$ (Proposition [[§70 Complete Vector Fields#^prop-70-10|§70.10]]) starting at $F(e) = e$. By Proposition [[§69 Maximal Integral Curves and Flows#^prop-69-1|§69.1]] it is $t \mapsto \exp_G(t\tilde A)$ (Proposition [[§71 The Exponential Map#^prop-71-2|§71.2]]); take $t = 1$.

^pf-71-9

*Uses:* [[§71 The Exponential Map#^cor-71-8|§71.8]], [[§61 Lie Group Morphisms and Linear Groups#^lem-61-1|§61.1]], [[§70 Complete Vector Fields#^thm-70-11|§70.11]], [[§71 The Exponential Map#^prop-71-2|§71.2]], [[§70 Complete Vector Fields#^prop-70-10|§70.10]], [[§69 Maximal Integral Curves and Flows#^prop-69-1|§69.1]]

> [!theorem] Proposition §71.10: Integral Curves of Left-Invariant Fields on a Linear Group
> Let $G \subseteq \mathrm{GL}(n, \mathbb{R})$ be a linear group that is a Lie subgroup (Theorem [[§61 Lie Group Morphisms and Linear Groups#^thm-61-5|§61.5]]), with $\mathfrak{g}$ identified with a subspace of $\operatorname{Mat}(n, \mathbb{R})$, and $A \in \mathfrak{g}$. For every $g \in G$ the integral curve of the left-invariant field $\mathbf{A}^G$ (with $\mathbf{A}^G_e = A$, as in Lemma [[§71 The Exponential Map#^lem-71-7|§71.7]]) starting at $g$ is
>
> $$
> t \longmapsto g\, e^{tA} = g \Big(\sum_{\ell=0}^\infty \frac{t^\ell}{\ell!} A^\ell\Big), \qquad t \in \mathbb{R} .
> $$
>
> In particular $g\, e^{tA} \in G$ for all $t$.

^prop-71-10

> [!proof]+ Proof
> *(Assignment 7, Problem 5(b): the submitted solution, with the invertibility of $e^{tA}$ supplied by Lemma [[§71 The Exponential Map#^lem-71-6|§71.6]]; the solution takes $c(t) \in \mathrm{GL}(n, \mathbb{R})$ for granted.)* Let $\iota : G \hookrightarrow \mathrm{GL}(n, \mathbb{R})$ be the inclusion. Since $\mathrm{GL}(n, \mathbb{R})$ is open in $\operatorname{Mat}(n, \mathbb{R})$, $T_X \mathrm{GL}(n, \mathbb{R}) = \operatorname{Mat}(n, \mathbb{R})$ for each $X$ (Example [[§60 Lie Groups and Left-Invariant Vector Fields#^ex-60-1|§60.1]]); the velocity of a matrix-valued curve is its entrywise derivative, and $A \in \mathfrak{g}$ is identified with the matrix $d\iota_e(A)$. Let $\mathbf{A}^{\mathrm{GL}}$ be the left-invariant field on $\mathrm{GL}(n, \mathbb{R})$ with $\mathbf{A}^{\mathrm{GL}}_I = A$.
>
> *The field $\mathbf{A}^{\mathrm{GL}}$.* For $h \in \mathrm{GL}(n, \mathbb{R})$, $L_h(X) = hX$ is the restriction of the linear map $X \mapsto hX$ of $\operatorname{Mat}(n, \mathbb{R})$. Computing its differential along the curve $t \mapsto I + tA$, which passes through $I$ with velocity $A$,
>
> $$
> \mathbf{A}^{\mathrm{GL}}_h = d(L_h)_I(A) = \frac{d}{dt}\Big|_{t=0} h(I + tA) = \frac{d}{dt}\Big|_{t=0} (h + t\, hA) = hA ,
> $$
>
> as in Example [[§60 Lie Groups and Left-Invariant Vector Fields#^ex-60-1|§60.1]].
>
> *$t \mapsto g\,e^{tA}$ is an integral curve of $\mathbf{A}^{\mathrm{GL}}$.* Let $g \in G$ and $c(t) = g \sum_{\ell \ge 0} \frac{t^\ell}{\ell!} A^\ell$, $t \in \mathbb{R}$. By Lemma [[§71 The Exponential Map#^lem-71-6|§71.6]], $c(t) = g\, e^{tA}$ is a product of invertible matrices, so $c : \mathbb{R} \to \mathrm{GL}(n, \mathbb{R})$; and $c(0) = gI = g$. Differentiating term by term, the $\ell = 0$ term $I$ is constant, and for $\ell \ge 1$, $\frac{d}{dt}\frac{t^\ell}{\ell!} A^\ell = \frac{t^{\ell-1}}{(\ell-1)!} A^\ell$. Since left multiplication by $g$ and right multiplication by $A$ are linear and continuous, reindexing with $m = \ell - 1$ gives
>
> $$
> c'(t) = g \sum_{m=0}^\infty \frac{t^m}{m!} A^{m+1} = \Big(g \sum_{m=0}^\infty \frac{t^m}{m!} A^m\Big) A = c(t)\, A = \mathbf{A}^{\mathrm{GL}}_{c(t)} \qquad \text{for all } t \in \mathbb{R} .
> $$
>
> *Comparison with $\mathbf{A}^G$.* Left-invariant fields are complete (Theorem [[§70 Complete Vector Fields#^thm-70-11|§70.11]]), so the integral curve $\gamma$ of $\mathbf{A}^G$ starting at $g$ is defined on $\mathbb{R}$. By Lemma [[§71 The Exponential Map#^lem-71-7|§71.7]] with $H = \mathrm{GL}(n, \mathbb{R})$, $\iota \circ \gamma : \mathbb{R} \to \mathrm{GL}(n, \mathbb{R})$ is an integral curve of $\mathbf{A}^{\mathrm{GL}}$ with $\iota \circ \gamma(0) = g$. So $c$ and $\iota \circ \gamma$ are integral curves of $\mathbf{A}^{\mathrm{GL}}$ on $\mathbb{R}$ with the same starting point, and by uniqueness (Proposition [[§68 Local Existence and Uniqueness#^prop-68-3|§68.3]])
>
> $$
> c(t) = \iota(\gamma(t)) \qquad \text{for all } t \in \mathbb{R} .
> $$
>
> Hence $c(t) \in G$ for all $t$, and $c$ is the integral curve of $\mathbf{A}^G$ starting at $g$.

^pf-71-10

*Uses:* [[§71 The Exponential Map#^lem-71-6|§71.6]], [[§60 Lie Groups and Left-Invariant Vector Fields#^ex-60-1|Ex. §60.1]], [[§70 Complete Vector Fields#^thm-70-11|§70.11]], [[§71 The Exponential Map#^lem-71-7|§71.7]], [[§68 Local Existence and Uniqueness#^prop-68-3|§68.3]]

> [!theorem] Theorem §71.11: The Exponential Map of a Linear Group
> Let $G \subseteq \mathrm{GL}(n, \mathbb{R})$ be a linear group (Definition [[§61 Lie Group Morphisms and Linear Groups#^def-61-1|§61.1]]) that is a Lie subgroup (Theorem [[§61 Lie Group Morphisms and Linear Groups#^thm-61-5|§61.5]]), and $A \in \mathfrak{g}$, a matrix. Then
>
> $$
> \exp(A) = \sum_{\ell=0}^\infty \frac{1}{\ell!} A^\ell ,
> $$
>
> the series converging in any norm on $\operatorname{Mat}(n, \mathbb{R})$.
>
> *Lee: Proposition 20.2, Example 20.4*

^thm-71-11

> [!proof]+ Proof (outline from Lecture 26; the general case from Assignment 7, Problem 5)
> *(The lecture gave the case $G = \mathrm{GL}(n, \mathbb{R})$ in outline; the series facts are an exercise, and the case of a general $G \subseteq \mathrm{GL}(n, \mathbb{R})$ needs an extra argument, which is part of the homework: Proposition [[§71 The Exponential Map#^prop-71-10|§71.10]], Assignment 7, Problem 5(b).)* The method is once again uniqueness. Show it first for $G = \mathrm{GL}(n, \mathbb{R})$. Define $e^A = \sum_{\ell \ge 0} A^\ell / \ell!$. Then
>
> $$
> \frac{d}{dt}\, e^{tA} = A\, e^{tA} = e^{tA} A ,
> $$
>
> by manipulating the series: it converges strongly enough in norm to be differentiated term by term; differentiating $t^\ell$ brings out a factor $\ell$, which cancels against $\ell!$, and the resulting shift of index produces the extra factor $A$, which can be put on the left or on the right. So $\gamma(t) = e^{tA}$ is a curve in $\mathrm{GL}(n, \mathbb{R})$ (it is invertible, Lemma [[§71 The Exponential Map#^lem-71-6|§71.6]]), and
>
> $$
> \frac{d}{dt}\gamma(t) = e^{tA} A = d\big(L_{e^{tA}}\big)_e(A) = \mathbf{X}^A_{e^{tA}} ,
> $$
>
> because $L_{e^{tA}} : g \mapsto e^{tA} g$ is the restriction to $\mathrm{GL}(n, \mathbb{R})$ of a linear map, so it is its own differential (Example [[§60 Lie Groups and Left-Invariant Vector Fields#^ex-60-1|§60.1]]). With $\gamma(0) = e$, $\gamma$ is the integral curve of $\mathbf{X}^A$ starting at $e$:
>
> $$
> \left\{ \begin{aligned} \tfrac{d}{dt}\gamma(t) &= \mathbf{X}^A_{\gamma(t)} \\ \gamma(0) &= e \end{aligned} \right.
> \qquad \Longrightarrow \qquad e^{tA} = \varphi^A_t(e) ,
> $$
>
> and at $t = 1$, $e^A = \exp(A)$ by Definition [[§71 The Exponential Map#^def-71-1|§71.1]]. For a general $G \subseteq \mathrm{GL}(n, \mathbb{R})$: by Proposition [[§71 The Exponential Map#^prop-71-10|§71.10]] with $g = e = I$, the integral curve of the left-invariant field $\mathbf{X}^A$ on $G$ starting at $e$ is $t \mapsto e^{tA}$, and at $t = 1$, $\exp(A) = e^A$ by Definition [[§71 The Exponential Map#^def-71-1|§71.1]]. *(Completed with Assignment 7, Problem 5.)*

^pf-71-11

*Uses:* [[§60 Lie Groups and Left-Invariant Vector Fields#^ex-60-1|Ex. §60.1]], [[§71 The Exponential Map#^def-71-1|Def. §71.1]], [[§71 The Exponential Map#^prop-71-10|§71.10]], [[§71 The Exponential Map#^lem-71-6|§71.6]]

> [!example] Example §71.1: $\exp(A + B) \neq \exp(A)\exp(B)$ for Two Nilpotent Matrices
> *(Not from lecture.)* In $\mathrm{GL}(2, \mathbb{R})$, for $A = \begin{psmallmatrix} 0 & 1 \\ 0 & 0 \end{psmallmatrix}$ and $B = \begin{psmallmatrix} 0 & 0 \\ 1 & 0 \end{psmallmatrix}$,
>
> $$
> \exp(A)\exp(B) = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix} \neq \begin{pmatrix} \cosh 1 & \sinh 1 \\ \sinh 1 & \cosh 1 \end{pmatrix} = \exp(A + B) ,
> $$
>
> a concrete failure of the identity of the [[§71 The Exponential Map#^rem-71-1|warning]] above. Here $[A, B] = AB - BA = \begin{psmallmatrix} 1 & 0 \\ 0 & -1 \end{psmallmatrix} \neq 0$.
>
> *The exponential is the series.* For $G = \mathrm{GL}(2, \mathbb{R})$, $\mathfrak{g} = \operatorname{Mat}(2, \mathbb{R})$ (Example [[§60 Lie Groups and Left-Invariant Vector Fields#^ex-60-1|§60.1]]), and Theorem [[§71 The Exponential Map#^thm-71-11|§71.11]] gives $\exp(C) = \sum_{\ell \ge 0} C^\ell/\ell!$.
>
> *$\exp(A)\exp(B)$.* $A^2 = B^2 = 0$, so all higher powers vanish and $\exp(A) = I + A$, $\exp(B) = I + B$:
>
> $$
> \exp(A)\exp(B) = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}\begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix} = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}.
> $$
>
> *$\exp(A + B)$.* $A + B = \begin{psmallmatrix} 0 & 1 \\ 1 & 0 \end{psmallmatrix}$ has $(A + B)^2 = I$, so $(A + B)^{2k} = I$ and $(A + B)^{2k+1} = A + B$. Splitting the series into even and odd terms,
>
> $$
> \exp(A + B) = \Big(\sum_{k \ge 0} \frac{1}{(2k)!}\Big) I + \Big(\sum_{k \ge 0} \frac{1}{(2k+1)!}\Big)(A + B) = \cosh 1\; I + \sinh 1\; (A + B) = \begin{pmatrix} \cosh 1 & \sinh 1 \\ \sinh 1 & \cosh 1 \end{pmatrix}.
> $$
>
> *They differ.* The top-left entries are $2$ and $\cosh 1 = (e + e^{-1})/2 < (3 + 1)/2 = 2$.
>
> *The bracket.* $AB = \begin{psmallmatrix} 1 & 0 \\ 0 & 0 \end{psmallmatrix}$ and $BA = \begin{psmallmatrix} 0 & 0 \\ 0 & 1 \end{psmallmatrix}$, so $[A, B] = \begin{psmallmatrix} 1 & 0 \\ 0 & -1 \end{psmallmatrix} \neq 0$: $A$ and $B$ do not commute.

^ex-71-1

> [!remark]- Connections
> - Ordinary differential equations: $x(t) = e^{tA}x_0$ solves $x' = Ax$ — [[Matrix Exponential Solution]]. Here the same series is the integral curve of the left-invariant field $\mathbf{X}^A_g = gA$ on $\mathrm{GL}(n, \mathbb{R})$, i.e. the solution of the matrix equation $\gamma' = \gamma A$, $\gamma(0) = I$.

*Uses:* [[§60 Lie Groups and Left-Invariant Vector Fields#^ex-60-1|Ex. §60.1]], [[§71 The Exponential Map#^thm-71-11|§71.11]]

For many groups, but not for all groups, $\exp$ is surjective: for instance for all unitary groups, and more generally for compact connected groups, a fact that needs proof. But globally it is not one-to-one for a compact group: the exponential wraps the tangent space around the group, as $t \mapsto e^{it}$ wraps $\mathfrak{u}(1) = i\mathbb{R}$ around $\mathrm{U}(1)$. *(Not from lecture.)* Surjectivity can fail: $\exp$ takes values in the identity component, so it misses $\mathrm{O}(n) \setminus \mathrm{SO}(n)$; and even for the connected group $\mathrm{SL}(2, \mathbb{R})$ the matrix $\begin{psmallmatrix} -1 & 1 \\ 0 & -1 \end{psmallmatrix}$ is not an exponential.

![[m591-71-1.svg]]

*(Not from lecture; figure added.)* Wrapping the tangent space around the group, for $G = \mathrm{U}(1)$: $\mathfrak{u}(1) = i\mathbb{R}$, and $\exp(ti) = e^{it}$ (Theorem [[§71 The Exponential Map#^thm-71-11|§71.11]] with $n = 1$, complex). The segment $[0, 2\pi i]$ (blue) goes once around the circle and $[-\pi i, 0]$ (red) covers the lower half again: $\exp$ is onto but not one-to-one, while near $0$ it is one-to-one, as Proposition [[§71 The Exponential Map#^prop-71-12|§71.12]] guarantees in general.

What is always true is the following local statement.

> [!theorem] Proposition §71.12: Smoothness and the Differential at $0$
> $\exp : \mathfrak{g} \to G$ is smooth, and $d(\exp)_0 = \mathrm{Id}_{\mathfrak{g}}$, under the identifications $T_0\mathfrak{g} = \mathfrak{g}$ (Corollary [[§30 The Differential in Coordinates#^cor-30-6|§30.6]]) and $T_eG = \mathfrak{g}$. Hence $\exp$ is a local diffeomorphism at $0 \in \mathfrak{g} = T_eG$: it maps some open neighbourhood of $0$ diffeomorphically onto an open neighbourhood of $e$.
>
> *Lee: Proposition 20.8*

^prop-71-12

> [!proof]+ Proof
> *(Lecture 26. Smoothness is awkward to prove directly, but there is a neat trick. The smoothness of the field $\mathbf{V}$, not gone into in lecture, is filled in.)*
>
> *1. Smoothness.* The flow evaluated at time one has to be considered as a function of $A$, which is new: so far only one vector field at a time has been considered. The trick, also used for variations, is to put together all the $\mathbf{X}^A$ as a single field over a larger space that includes the parameters, $G \times \mathfrak{g}$. Define
>
> $$
> \mathbf{V}_{(g, A)} = \big(\mathbf{X}^A_g, 0\big) \in T_gG \oplus T_A\mathfrak{g} = T_{(g, A)}(G \times \mathfrak{g}) ,
> $$
>
> using Theorem [[§31 Tangent Vectors as Velocities of Curves#^thm-31-7|§31.7]], and $T_A\mathfrak{g} = \mathfrak{g}$, by the vector space structure. In the second slot one simply puts zero.
>
> *Claim: $\mathbf{V}$ is smooth* (this is where the smoothness of left multiplication is used). *(Filled in.)* By Lemma [[§56 Vector Fields#^lem-56-11|§56.11]] it suffices that $\mathbf{V}h$ is smooth for every $h \in C^\infty(G \times \mathfrak{g})$. With $\iota_A : G \to G \times \mathfrak{g}$, $x \mapsto (x, A)$, Theorem [[§31 Tangent Vectors as Velocities of Curves#^thm-31-7|§31.7]] gives $\mathbf{V}_{(g,A)} = (\iota_A)_{\ast}\mathbf{X}^A_g$, so
>
> $$
> (\mathbf{V}h)(g, A) = \mathbf{X}^A_g\big[h(\cdot, A)\big] = d(L_g)_e(A)\big[h(\cdot, A)\big] = A\big[x \mapsto h(gx, A)\big] .
> $$
>
> Let $\psi(g, x, A) = h(gx, A)$, smooth on $G \times G \times \mathfrak{g}$ because multiplication is smooth (Definition [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-1|§60.1]]). Take a chart $(W, y^1, \ldots, y^m)$ of $G$ at $e$ and write $A = \sum_j A^j\, \partial/\partial y^j|_e$; the coefficients $A^j$ are linear, hence smooth, functions of $A \in \mathfrak{g}$. Then
>
> $$
> (\mathbf{V}h)(g, A) = \sum_{j=1}^m A^j\, \frac{\partial \psi}{\partial y^j}(g, e, A) ,
> $$
>
> the partial derivatives of $\psi$ in the coordinates $y^j$ of the middle factor, which are smooth on $G \times W \times \mathfrak{g}$. So $\mathbf{V}h$ is smooth. (This is the trick of Proposition [[§60 Lie Groups and Left-Invariant Vector Fields#^prop-60-8|§60.8]], now with $A$ varying too.)
>
> *$\mathbf{V}$ is complete* — because each $\mathbf{X}^A$ is, and the integration only takes place in the $G$ variable; the $\mathfrak{g}$ variable plays no role. For $(g, A) \in G \times \mathfrak{g}$, the curve $t \mapsto \big(\varphi^A_t(g), A\big)$ has velocity $\big(\mathbf{X}^A_{\varphi^A_t(g)}, 0\big) = \mathbf{V}_{(\varphi^A_t(g), A)}$ (Theorem [[§31 Tangent Vectors as Velocities of Curves#^thm-31-7|§31.7]]: the components of a velocity are the velocities of the components), it starts at $(g, A)$, and it is defined for all $t$, since $\mathbf{X}^A$ is complete. So the flow of $\mathbf{V}$ is
>
> $$
> \Phi : \mathbb{R} \times G \times \mathfrak{g} \longrightarrow G \times \mathfrak{g}, \qquad (t, g, A) \longmapsto \big(\varphi^A_t(g), A\big),
> $$
>
> which is smooth (Theorem [[§69 Maximal Integral Curves and Flows#^thm-69-4|§69.4]](2)). Now put $t = 1$, $g = e$, and project:
>
> ![[m591-71-5.svg]]
>
> $$
> A \longmapsto \varphi^A_1(e) = \exp(A) .
> $$
>
> The composite is $\exp$, so $\exp$ is smooth.
>
> *2. The differential at $0$.* We want $d(\exp)_0 : T_0\mathfrak{g} = \mathfrak{g} \to T_eG = \mathfrak{g}$ invertible; in fact it is the identity. The differential of a map is computed with curves (Corollary [[§31 Tangent Vectors as Velocities of Curves#^cor-31-5|§31.5]]). The straight line $t \mapsto tA$ in $\mathfrak{g}$ is at $0$ when $t = 0$, with velocity $A$; so, with Proposition [[§71 The Exponential Map#^prop-71-2|§71.2]],
>
> $$
> d(\exp)_0(A) = \frac{d}{dt}\Big|_{t=0} \exp(tA) = \frac{d}{dt}\Big|_{t=0} \varphi^A_t(e) = \mathbf{X}^A_e = A .
> $$
>
> *3. Local diffeomorphism.* $d(\exp)_0$ is bijective, so by the inverse function theorem, in the form of the proof of Theorem [[§35 Local Diffeomorphisms#^thm-35-2|§35.2]] ($\Leftarrow$) at the single point $0$, $\exp$ restricts to a diffeomorphism from an open neighbourhood of $0$ onto an open neighbourhood of $e$.

^pf-71-12

*Uses:* [[§31 Tangent Vectors as Velocities of Curves#^thm-31-7|§31.7]], [[§56 Vector Fields#^lem-56-11|§56.11]], [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-1|Def. §60.1]], [[§60 Lie Groups and Left-Invariant Vector Fields#^prop-60-8|§60.8]], [[§69 Maximal Integral Curves and Flows#^thm-69-4|§69.4]], [[§31 Tangent Vectors as Velocities of Curves#^cor-31-5|§31.5]], [[§71 The Exponential Map#^prop-71-2|§71.2]], [[§35 Local Diffeomorphisms#^thm-35-2|§35.2]]

**Transcription note (board 11/4).** The board writes $\exp : \mathfrak{g} \to A$ in the statement (for $G$), $\mathbf{V}_{(g,A)} \in (T_gG) \times \mathfrak{g} = T_A\mathfrak{g}$ (the space is $T_{(g,A)}(G \times \mathfrak{g})$), and the flow as $(t, g, A) \mapsto (\varphi^A_t(g), 0)$; the second component of the flow is $A$, which the field leaves unchanged, as above.

![[m591-71-2.svg]]

*(Not from lecture; figure added.)* $\exp$ for the group $G = \{(a, b) : a > 0\}$ of affine maps $x \mapsto ax + b$ of the example after Theorem [[§70 Complete Vector Fields#^thm-70-11|§70.11]]. With $A = (u, v) \in \mathfrak{g}$ (meaning $\mathbf{X}^A_e = (u, v)$ in the coordinates $(a, b)$), the one-parameter subgroup is $\varphi^A_t(e) = \big(e^{ut}, \tfrac{v}{u}(e^{ut} - 1)\big)$, so $\exp(u, v) = \big(e^u, \tfrac{v}{u}(e^u - 1)\big)$ ($= (1, v)$ if $u = 0$). Lines $u = \text{const}$ (blue) go to the horizontal lines $a = e^u$, lines $v = \text{const}$ (red) to curves crossing the row $a = 1$ at $b = v$, and each one-parameter subgroup is a straight ray $b = \tfrac{v}{u}(a - 1)$ through $e$, run at exponential speed; near $0$ the grid is barely distorted, which is $d(\exp)_0 = \mathrm{Id}$. Here $\exp$ is even a diffeomorphism of $\mathfrak{g}$ onto $G$: given $(a, b)$, $u = \log a$ and $v = bu/(a - 1)$.

![[m591-71-a1.gif|620]]

*(Not from lecture; animation added, vault only.)* $\exp$ as “follow the one-parameter subgroup to time $1$”, in the same group. Left: $24$ vectors $A$ on a circle in $\mathfrak{g}$, scaled by $\tau$. Right: the points $\exp(\tau A) = \varphi^A_\tau(e)$ (Proposition [[§71 The Exponential Map#^prop-71-2|§71.2]]) moving out from $e$ along their one-parameter subgroups, straight rays at exponential speed; at $\tau = 1$ the red curve is the image of the circle under $\exp$. For small $\tau$ it is nearly a round circle, which is $d(\exp)_0 = \mathrm{Id}$.

The term exponential map comes up again in Riemannian geometry (MATH 635), for any manifold with a Riemannian structure. There, a tangent vector is the initial data of a geodesic, which one follows to time $1$. To exponentiate geometrically one needs a way of launching a curve from a tangent vector: here the one-parameter subgroups do this, in Riemannian geometry the geodesics. Next topic: Lie derivatives.
