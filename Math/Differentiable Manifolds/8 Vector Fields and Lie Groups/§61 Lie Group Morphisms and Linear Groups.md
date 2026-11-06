---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 8
section: 61
tags: [differentiable-manifolds, math591]
---
← [[§60 Lie Groups and Left-Invariant Vector Fields]] · ↑ [[· 8 Vector Fields and Lie Groups]] · [[§62 Sets of Measure Zero]] →

*Stage: symmetry — Maps of Lie groups induce maps of Lie algebras that preserve brackets; for a linear group the bracket is the matrix commutator.*

*Lecture 18. Lie group morphisms and the Lie algebra, which the identification $\mathfrak{g} \cong T_eG$ now puts within reach.*

> [!remark] Remark: From Now On: $\mathfrak{g}$ Is $T_eG$
> From now on the Lie algebra is identified with the tangent space at the identity, $\mathfrak{g} \cong T_eG$ by $\mathrm{ev}$ (Theorem [[§60 Lie Groups and Left-Invariant Vector Fields#^thm-60-9|§60.9]]), as vector spaces, keeping in mind that the Lie bracket comes from commuting left-invariant fields. That is Definition [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-4|§60.4]] read through Definition [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-6|§60.6]]: to compute the bracket of $A, B \in T_eG$,
>
> 1. extend $A$ and $B$ to the left-invariant fields $\mathbf{X}^A$, $\mathbf{X}^B$, their left-invariant extensions (Definition [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-5|§60.5]]; they lie in $\mathfrak{g}$ by Proposition [[§60 Lie Groups and Left-Invariant Vector Fields#^prop-60-8|§60.8]]);
> 2. take the commutator $[\mathbf{X}^A, \mathbf{X}^B]$ of vector fields;
> 3. evaluate it at the identity: $[A, B] = [\mathbf{X}^A, \mathbf{X}^B]_e$.
>
> This is the definition. Elements of $T_eG$ are now written with capital letters, since they are thought of as matrices.

^rem-61-1

> [!definition] Definition §61.1: Linear Group
> A **linear group**, or **matrix group**, is a Lie group $G$ (Definition [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-1|§60.1]]) that is a subgroup of $\mathrm{GL}(n,\mathbb{R})$ or $\mathrm{GL}(n,\mathbb{C})$ for some $n$, with matrix multiplication as its group product — for instance each classical group of Proposition [[§60 Lie Groups and Left-Invariant Vector Fields#^prop-60-1|§60.1]].

^def-61-1

> [!remark] Remark: Nonlinear Groups
> Matrix groups are also called linear groups (Definition [[§61 Lie Group Morphisms and Linear Groups#^def-61-1|§61.1]]). Not every Lie group is isomorphic to a matrix group: nonlinear groups arise naturally as covers of matrix groups. *(Filled in: the standard example is the universal cover of $\mathrm{SL}(2,\mathbb{R})$, a Lie group isomorphic to no group of matrices.)* The question of Lecture 17, restated: for a matrix group, can the bracket be identified directly on the tangent space at the identity? The answer is the matrix commutator (Theorem [[§60 Lie Groups and Left-Invariant Vector Fields#^thm-60-10|§60.10]]); to get there, the course uses the general idea below.

^rem-61-2

> [!definition] Definition §61.2: Lie Group Morphism
> Let $H$ and $G$ be [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-1|Lie groups]]. A **Lie group morphism** (homomorphism) $F : H \to G$ is a map that is both [[§19 Smooth Functions and Smooth Maps#^def-19-3|smooth]] and a [[§15 Homomorphisms#^def-15-1|group morphism]]: $F(gh) = F(g)F(h)$ for all $g, h \in H$.
>
> *Lee: Ch. 7, Lie Group Homomorphisms*

^def-61-2

A Lie group is a manifold and a group whose group operations are smooth, so a morphism preserves both structures. In particular $F(e_H) = e_G$. *(Filled in: $F(e_H) = F(e_He_H) = F(e_H)F(e_H)$; multiply on the left by $F(e_H)^{-1}$.)* So $F$ has a differential at the identity,

$$
dF_e : T_{e}H \longrightarrow T_{e}G, \qquad \text{that is,} \qquad dF_e : \mathfrak{h} \longrightarrow \mathfrak{g},
$$

a linear map between the Lie algebras, and the natural question is whether this map preserves commutators.

> [!definition] Definition §61.3: Lie Algebra Morphism
> Let $\mathfrak{h}$ and $\mathfrak{g}$ be Lie algebras (Definition [[§58 Lie Bracket and Lie Algebra#^def-58-2|§58.2]]). A **Lie algebra morphism** is a linear map $\phi : \mathfrak{h} \to \mathfrak{g}$ that preserves brackets: $\phi([A, B]) = [\phi(A), \phi(B)]$ for all $A, B \in \mathfrak{h}$.
>
> *Lee: Ch. 8, Induced Lie Algebra Homomorphisms*

^def-61-3

> [!theorem] Lemma §61.1: Left-Invariant Fields Related by a Morphism
> Let $F : H \to G$ be a Lie group morphism (Definition [[§61 Lie Group Morphisms and Linear Groups#^def-61-2|§61.2]]) and $A \in T_eH$, and put $\tilde A = dF_e(A) \in T_eG$. Let $\mathbf{X}^A \in \mathfrak{X}(H)$ and $\mathbf{Y}^{\tilde A} \in \mathfrak{X}(G)$ be the left-invariant extensions of $A$ and of $\tilde A$ (Definition [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-5|§60.5]]; smooth by Proposition [[§60 Lie Groups and Left-Invariant Vector Fields#^prop-60-8|§60.8]]). Then $\mathbf{X}^A$ and $\mathbf{Y}^{\tilde A}$ are $F$-related (Definition [[§59 Related Vector Fields#^def-59-2|§59.2]]):
>
> $$
> dF_h\big(\mathbf{X}^A_h\big) = \mathbf{Y}^{\tilde A}_{F(h)} \in T_{F(h)}G \qquad \text{for every } h \in H .
> $$
>
> *Lee: proof of Theorem 8.44*

^lem-61-1

> [!proof]+ Proof
> *(Lecture 18: the claim in the proof that Lie group morphisms preserve brackets. The final diagram chase, left to the class, is completed.)* Fix $h \in H$; the displayed equality is to be shown. *$F(e) = e$.* As noted after Definition [[§61 Lie Group Morphisms and Linear Groups#^def-61-2|§61.2]], $F(e_H) = F(e_He_H) = F(e_H)F(e_H)$, and multiplying on the left by $F(e_H)^{-1}$ gives $F(e_H) = e_G$; so $dF_e$ maps $T_eH$ to $T_eG$, and $\tilde A \in T_eG$.
>
> *The square.* Here it is essential that $F$ is a group morphism. Consider the square
>
> $$
> F \circ L_h = L_{F(h)} \circ F : H \to G .
> $$
>
> It commutes: for $x \in H$, $F(L_h(x)) = F(hx) = F(h)F(x) = L_{F(h)}(F(x))$, where $L$ always denotes left multiplication in the corresponding group. Differentiate it at $e \in H$. Since $L_h(e) = h$ and $F(e) = e$, the chain rule (Theorem [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]]) gives the commutative square of differentials
>
> $$
> dF_h \circ d(L_h)_e = d\big(L_{F(h)}\big)_e \circ dF_e : T_eH \to T_{F(h)}G .
> $$
>
> *The chase.* *(Completed.)* Chase where $A$ goes under this diagram:
>
> $$
> \begin{aligned}
> &\text{along the bottom, then up:} && A \mapsto d(L_h)_e(A) = \mathbf{X}^A_h \mapsto dF_h(\mathbf{X}^A_h), \\
> &\text{up, then along the top:} && A \mapsto dF_e(A) = \tilde A \mapsto d(L_{F(h)})_e(\tilde A) = \mathbf{Y}^{\tilde A}_{F(h)},
> \end{aligned}
> $$
>
> both by Definition [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-5|§60.5]], for $H$ at the point $h$ and for $G$ at the point $F(h)$. The square commutes, so $dF_h(\mathbf{X}^A_h) = \mathbf{Y}^{\tilde A}_{F(h)}$; as $h$ was arbitrary, this is the claim.

^pf-61-1

*Uses:* [[§61 Lie Group Morphisms and Linear Groups#^def-61-2|Def. §61.2]], [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]], [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-5|Def. §60.5]]

![[m591-56-1.svg]]

![[m591-56-2.svg]]

![[m591-56-3.svg]]

*Top left: the group square, which commutes because $F$ is a morphism. Top right: its differential at $e$, which commutes by the chain rule. Below: where $A$ goes. Both routes end at the same vector, which is the statement that $\mathbf{X}^A$ and $\mathbf{Y}^{\tilde A}$ are $F$-related.*

> [!theorem] Proposition §61.2: Lie Group Morphisms Preserve Brackets
> Let $F : H \to G$ be a [[§61 Lie Group Morphisms and Linear Groups#^def-61-2|Lie group morphism]]. For all $A, B \in T_eH$,
>
> $$
> dF_e\big([A, B]\big) = \big[dF_e(A), dF_e(B)\big] \in T_eG ,
> $$
>
> that is, $dF_e : \mathfrak{h} \to \mathfrak{g}$ is a Lie algebra morphism (Definition [[§61 Lie Group Morphisms and Linear Groups#^def-61-3|§61.3]]).
>
> *Lee: Theorem 8.44*

^prop-61-2

> [!proof]+ Proof
> *(Lecture 18, a soft proof.)* Since the bracket is defined in terms of vector fields, the proof has to pass to vector fields. For $A \in T_eH$ let $\mathbf{X}^A \in \mathfrak{X}(H)$ be the left-invariant extension of $A$, the left-invariant field with $\mathbf{X}^A_e = A$; put $\tilde A = dF_e(A) \in T_eG$, and let $\mathbf{Y}^{\tilde A} \in \mathfrak{X}(G)$ be the left-invariant extension of $\tilde A$, with $\mathbf{Y}^{\tilde A}_e = \tilde A$ (Definition [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-5|§60.5]] and Proposition [[§60 Lie Groups and Left-Invariant Vector Fields#^prop-60-8|§60.8]], applied to $H$ and to $G$).
>
> *Claim.* $\mathbf{X}^A$ and $\mathbf{Y}^{\tilde A}$ are $F$-related (Definition [[§59 Related Vector Fields#^def-59-2|§59.2]]).
>
> *The proposition follows from the claim.* Let also $B \in T_eH$ and $\tilde B = dF_e(B)$. By the claim, $\mathbf{X}^A$ is $F$-related to $\mathbf{Y}^{\tilde A}$ and $\mathbf{X}^B$ to $\mathbf{Y}^{\tilde B}$, so by Proposition [[§59 Related Vector Fields#^prop-59-3|§59.3]], $[\mathbf{X}^A, \mathbf{X}^B]$ is $F$-related to $[\mathbf{Y}^{\tilde A}, \mathbf{Y}^{\tilde B}]$. Evaluate at $e \in H$, using $F(e) = e$:
>
> $$
> dF_e\big([\mathbf{X}^A, \mathbf{X}^B]_e\big) = [\mathbf{Y}^{\tilde A}, \mathbf{Y}^{\tilde B}]_{F(e)} = [\mathbf{Y}^{\tilde A}, \mathbf{Y}^{\tilde B}]_e .
> $$
>
> By Definition [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-6|§60.6]] the left side is $dF_e([A, B])$ and the right side is $[\tilde A, \tilde B] = [dF_e(A), dF_e(B)]$: that is exactly the proposition. So the work lies in the claim: it is Lemma [[§61 Lie Group Morphisms and Linear Groups#^lem-61-1|§61.1]], applied to $F$ and $A$, whose proof is the diagram chase above.

^pf-61-2

*Uses:* [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-5|Def. §60.5]], [[§60 Lie Groups and Left-Invariant Vector Fields#^prop-60-8|§60.8]], [[§59 Related Vector Fields#^def-59-2|Def. §59.2]], [[§59 Related Vector Fields#^prop-59-3|§59.3]], [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-6|Def. §60.6]], [[§61 Lie Group Morphisms and Linear Groups#^lem-61-1|§61.1]]

Next: the commutator, first for the general linear group, and then for any linear group (Theorem [[§60 Lie Groups and Left-Invariant Vector Fields#^thm-60-10|§60.10]]).

**Transcription note (Lecture 18).** Page 47 of the handwritten notes begins the proof with “take $A \in T_hH$”; $A \in T_eH$. Page 48 writes the second field as $\mathbf{Y}^{\hat B}$ in one place; it is $\mathbf{Y}^{\tilde B}$, with $\tilde B = dF_e(B)$.

## The Bracket of a Matrix Group

*Lecture 19 began with a review: the Lie algebra $\mathfrak{g}$ of left-invariant fields, closed under commutators (Corollary [[§60 Lie Groups and Left-Invariant Vector Fields#^cor-60-6|§60.6]]); the isomorphism $\mathrm{ev} : \mathfrak{g} \to T_eG$ with inverse $A \mapsto \mathbf{X}^A$ (Theorem [[§60 Lie Groups and Left-Invariant Vector Fields#^thm-60-9|§60.9]]), including the check that $\mathbf{X}^A$ is left-invariant (Lemma [[§60 Lie Groups and Left-Invariant Vector Fields#^lem-60-7|§60.7]](2)); and the bracket on $T_eG$ (Definition [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-6|§60.6]]), defined so that $\mathrm{ev}$ is an isomorphism of Lie algebras.*

> [!remark] Remark: The Lie Algebra in Practice
> In practice, the Lie algebra of a group such as the orthogonal group is never described as a space of left-invariant fields; it is always the tangent space at the identity — with the bracket of Definition [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-6|§60.6]], which for matrix groups is the matrix commutator (Theorem [[§61 Lie Group Morphisms and Linear Groups#^thm-61-3|§61.3]] below). The notation $\mathfrak{gl}(d, \mathbb{R}) = T_I\mathrm{GL}(d,\mathbb{R}) = \operatorname{Mat}(d,\mathbb{R})$ is standard.

^rem-61-3

> [!theorem] Theorem §61.3: The Bracket of a Linear Group
> Let $G \subseteq \mathrm{GL}(d, \mathbb{R})$ be a linear group (Definition [[§61 Lie Group Morphisms and Linear Groups#^def-61-1|§61.1]]) that is a *Lie subgroup*: the inclusion $i : G \hookrightarrow \mathrm{GL}(d, \mathbb{R})$ is smooth and $di_I$ is injective — for instance, $G$ a regular submanifold of $\operatorname{Mat}(d, \mathbb{R})$, as are the classical groups (Proposition [[§60 Lie Groups and Left-Invariant Vector Fields#^prop-60-1|§60.1]]). Identify $T_IG$ with its image $di_I(T_IG) \subseteq \mathfrak{gl}(d,\mathbb{R}) = \operatorname{Mat}(d,\mathbb{R})$. Then the Lie bracket on $T_IG$ is
>
> $$
> [A, B] = AB - BA ,
> $$
>
> with matrix multiplication.
>
> *Lee: Proposition 8.41, Theorem 8.46*

^thm-61-3

> [!proof]+ Proof
> *(Lecture 19.)* By assumption, $G$ is included in some general linear group as a Lie subgroup, and the differential of the inclusion map at the identity is the inclusion $di_I : T_IG \hookrightarrow \mathfrak{gl}(d, \mathbb{R})$. The inclusion is a Lie group morphism (Definition [[§61 Lie Group Morphisms and Linear Groups#^def-61-2|§61.2]]): smooth by hypothesis, and a group morphism because the product on $G$ is matrix multiplication. So by Proposition [[§61 Lie Group Morphisms and Linear Groups#^prop-61-2|§61.2]], for $A, B \in T_IG$,
>
> $$
> di_I\big([A, B]_G\big) = \big[di_I(A), di_I(B)\big]_{\mathrm{GL}(d,\mathbb{R})} = di_I(A)\, di_I(B) - di_I(B)\, di_I(A),
> $$
>
> the last step by Theorem [[§60 Lie Groups and Left-Invariant Vector Fields#^thm-60-10|§60.10]]. Under the identification of $T_IG$ with its image, which $di_I$ injective makes legitimate, this is $[A, B] = AB - BA$. So once the bracket of the general linear group is known to be the commutator, the bracket of every linear group is the commutator too, by algebra alone. *(Filled in: a regular submanifold qualifies, since $i$ is smooth by Lemma [[§37 Regular Submanifolds#^lem-37-5|§37.5]](1), with coordinate representation $r \mapsto (r, \vec 0)$ in an adapted chart, whose differential is injective.)*

^pf-61-3

*Uses:* [[§61 Lie Group Morphisms and Linear Groups#^def-61-2|Def. §61.2]], [[§61 Lie Group Morphisms and Linear Groups#^prop-61-2|§61.2]], [[§60 Lie Groups and Left-Invariant Vector Fields#^thm-60-10|§60.10]], [[§37 Regular Submanifolds#^lem-37-5|§37.5]]

In particular $di_I(T_IG)$ is closed under the matrix commutator, as the image of a bracket. Lecture 19 checked this directly in one case.

> [!example] Example §61.1: The Commutator of Skew-Symmetric Matrices
> $T_I\mathrm{O}(n) = \operatorname{Skew}(n, \mathbb{R}) = \{A : A^{\mathsf T} = -A\}$ (Theorem [[§25 The Geometric Tangent Space#^thm-25-5|§25.5]]). Written out, an element of $\operatorname{Skew}(n, \mathbb{R})$ has zero diagonal, and its entries below the diagonal are the negatives of those above:
>
> $$
> A = \begin{pmatrix}
> 0 & a_{12} & \cdots & a_{1n} \\
> -a_{12} & 0 & \cdots & a_{2n} \\
> \vdots & \vdots & \ddots & \vdots \\
> -a_{1n} & -a_{2n} & \cdots & 0
> \end{pmatrix} .
> $$
> If $A, B \in \operatorname{Skew}(n,\mathbb{R})$, then $[A, B] = AB - BA \in \operatorname{Skew}(n,\mathbb{R})$.

^ex-61-1

> [!proof]+ Proof
> *(Lecture 19.)* $[A, B]^{\mathsf T} = (AB - BA)^{\mathsf T} = B^{\mathsf T}A^{\mathsf T} - A^{\mathsf T}B^{\mathsf T} = (-B)(-A) - (-A)(-B) = BA - AB = -[A, B]$. The same computation works for the unitary group, with the conjugate transpose $^{\ast}$ in place of the transpose; that was a homework problem.

^pf-ex-61-1

**Transcription note (Lecture 19).** Page 49 of the handwritten notes writes the evaluation map as $\mathfrak{g} \to T_eM$ and its inverse from $T_eM$; the group is $G$, so $T_eG$. The definition of the bracket there reads “$[A, B] = [\mathbf{X}^A, \mathbf{X}^B]$”; the field bracket is evaluated at the identity, $[A, B] = [\mathbf{X}^A, \mathbf{X}^B]_e$ (Definition [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-6|§60.6]]), as stated in lecture.

*Assignment 6, Problem 3: linear vector fields on $\mathbb{R}^n$. Not from lecture. “This is a special case of a Lie group (in this case $\mathrm{GL}(n,\mathbb{R})$) acting on the right on a manifold, in this case $\mathbb{R}^n$. Such an action induces a Lie algebra homomorphism from the Lie algebra of the group to the Lie algebra of vector fields on the manifold.”*

> [!definition] Definition §61.4: Linear Vector Field
> For an $n \times n$ real matrix $A = (a_{ij})$, the **linear vector field** $\mathbf{X}^A$ on $\mathbb{R}^n$ is
>
> $$
> \mathbf{X}^A_p = pA \in T_p\mathbb{R}^n \cong \mathbb{R}^n ,
> $$
>
> where $p \in \mathbb{R}^n$ is a *row* vector and $T_p\mathbb{R}^n \cong \mathbb{R}^n$ by $v \leftrightarrow D_v|_p$ (Corollary [[§30 The Differential in Coordinates#^cor-30-6|§30.6]]).

^def-61-4

The letter is that of Example [[§60 Lie Groups and Left-Invariant Vector Fields#^ex-60-1|§60.1]] on purpose: the left-invariant field $g \mapsto gA$ on $\mathrm{GL}(n,\mathbb{R})$ is $\mathbf{X}^A$ acting on each row of $g$ (the remark *Linear Fields and the Bracket of* $\mathrm{GL}(n,\mathbb{R})$ below).

> [!theorem] Proposition §61.4: The Derivation of a Linear Field
> In the standard coordinates $p = (x^1, \ldots, x^n)$ of $\mathbb{R}^n$, with $\partial_j = \partial/\partial x^j$,
>
> $$
> \mathbf{X}^A = \sum_{j=1}^n \Big(\sum_{i=1}^n a_{ij}\,x^i\Big) \partial_j .
> $$
>
> The map $A \mapsto \mathbf{X}^A$ is linear: $\mathbf{X}^{A + B} = \mathbf{X}^A + \mathbf{X}^B$ and $\mathbf{X}^{cA} = c\,\mathbf{X}^A$ for $c \in \mathbb{R}$.

^prop-61-4

> [!proof]+ Proof
> *(Assignment 6, Problem 3; the submitted solution.)* The $j$-th entry of the row vector $pA$ is
>
> $$
> (pA)_j = \sum_{i=1}^n x^i a_{ij}.
> $$
>
> For $f \in C^\infty(\mathbb{R}^n)$, $\mathbf{X}^A f$ is the derivative of $f$ at $p$ in the direction $\mathbf{X}^A_p = pA$; by the chain rule,
>
> $$
> (\mathbf{X}^A f)(p) = \frac{d}{dt}\Big|_{t=0} f(p + t\,pA) = \sum_{j=1}^n (pA)_j\, \partial_j f(p).
> $$
>
> Hence $\mathbf{X}^A = \sum_j \big(\sum_i a_{ij}\,x^i\big) \partial_j$. The coefficients are linear in the entries of $A$, so $A \mapsto \mathbf{X}^A$ is linear.

^pf-61-4

> [!theorem] Proposition §61.5: Brackets of Linear Fields
> For any two $n \times n$ real matrices $A$, $B$,
>
> $$
> \big[\mathbf{X}^A, \mathbf{X}^B\big] = \mathbf{X}^{[A,B]}, \qquad [A, B] = AB - BA .
> $$
>
> So $A \mapsto \mathbf{X}^A$ is a Lie algebra morphism $\mathfrak{gl}(n,\mathbb{R}) \to \mathfrak{X}(\mathbb{R}^n)$ (Definition [[§61 Lie Group Morphisms and Linear Groups#^def-61-3|§61.3]]).

^prop-61-5

> [!proof]+ Proof
> *(Assignment 6, Problem 3, “show directly”; the submitted solution.)* *Computing $\mathbf{X}^A(\mathbf{X}^B f)$.* Let $f \in C^\infty(\mathbb{R}^n)$. We have $\mathbf{X}^B f = \sum_k (pB)_k\, \partial_k f$ with $(pB)_k = \sum_l b_{lk}x^l$. By the product rule,
>
> $$
> \mathbf{X}^A(\mathbf{X}^B f) = \sum_{j,k} (pA)_j\, \partial_j\big[(pB)_k\big]\, \partial_k f + \sum_{j,k} (pA)_j\,(pB)_k\, \partial_j\partial_k f.
> $$
>
> For the first sum, $\partial_j\big(\sum_l b_{lk}x^l\big) = \sum_l b_{lk}\,\delta_{jl} = b_{jk}$, so
>
> $$
> \sum_{j,k} \Big(\sum_i a_{ij}x^i\Big) b_{jk}\, \partial_k f = \sum_k \Big(\sum_i x^i \sum_j a_{ij}b_{jk}\Big) \partial_k f = \sum_k \Big(\sum_i (AB)_{ik}\,x^i\Big) \partial_k f = \mathbf{X}^{AB} f.
> $$
>
> Writing $S(A,B) = \sum_{j,k} (pA)_j\,(pB)_k\, \partial_j\partial_k f$, we get $\mathbf{X}^A(\mathbf{X}^B f) = \mathbf{X}^{AB}f + S(A,B)$, and in the same way, with $A$ and $B$ interchanged, $\mathbf{X}^B(\mathbf{X}^A f) = \mathbf{X}^{BA}f + S(B,A)$.
>
> *The second-order terms cancel.* Relabelling the summation indices $j \leftrightarrow k$, and using $\partial_k\partial_j f = \partial_j\partial_k f$ (symmetry of second derivatives, as $f$ is smooth),
>
> $$
> S(B,A) = \sum_{j,k} (pB)_j\,(pA)_k\, \partial_j\partial_k f = \sum_{j,k} (pB)_k\,(pA)_j\, \partial_k\partial_j f = \sum_{j,k} (pA)_j\,(pB)_k\, \partial_j\partial_k f = S(A,B).
> $$
>
> *Conclusion.* Therefore, using the linearity of $A \mapsto \mathbf{X}^A$ (Proposition [[§61 Lie Group Morphisms and Linear Groups#^prop-61-4|§61.4]]),
>
> $$
> [\mathbf{X}^A, \mathbf{X}^B]f = \mathbf{X}^A(\mathbf{X}^B f) - \mathbf{X}^B(\mathbf{X}^A f) = \mathbf{X}^{AB}f - \mathbf{X}^{BA}f = \mathbf{X}^{AB - BA}f = \mathbf{X}^{[A,B]}f.
> $$
>
> Since this holds for every $f \in C^\infty(\mathbb{R}^n)$, $[\mathbf{X}^A, \mathbf{X}^B] = \mathbf{X}^{[A,B]}$.
>
> *(Filled in.)* The last sentence of the statement: $A \mapsto \mathbf{X}^A$ is linear and carries the commutator to the bracket of vector fields, which is what Definition [[§61 Lie Group Morphisms and Linear Groups#^def-61-3|§61.3]] asks of a map between Lie algebras.

^pf-61-5

*Uses:* [[§61 Lie Group Morphisms and Linear Groups#^prop-61-4|§61.4]], [[§61 Lie Group Morphisms and Linear Groups#^def-61-3|Def. §61.3]]

The second-order terms cancel as they must (Lemma [[§58 Lie Bracket and Lie Algebra#^lem-58-1|§58.1]]); the shortcut of Proposition [[§58 Lie Bracket and Lie Algebra#^prop-58-2|§58.2]], which computes only the first-order part, gives the same coefficients $\sum_i (AB - BA)_{ik} x^i$ at once.

> [!remark] Remark: Linear Fields and the Bracket of $\mathrm{GL}({n,\mathbb{R}})$
> *(Not from the assignment.)* Write $g \in \operatorname{Mat}(n,\mathbb{R})$ by its rows $g_1, \ldots, g_n \in \mathbb{R}^n$. The $l$-th row of $gA$ is $g_lA$, so the left-invariant field $\mathbf{X}^A_g = gA$ of Example [[§60 Lie Groups and Left-Invariant Vector Fields#^ex-60-1|§60.1]] is the linear field $\mathbf{X}^A$ of Definition [[§61 Lie Group Morphisms and Linear Groups#^def-61-4|§61.4]] acting on each row separately, the $n$ rows being independent variables. Proposition [[§61 Lie Group Morphisms and Linear Groups#^prop-61-5|§61.5]], applied row by row, is therefore the computation of Theorem [[§60 Lie Groups and Left-Invariant Vector Fields#^thm-60-10|§60.10]]: $[\mathbf{X}^A, \mathbf{X}^B] = \mathbf{X}^{AB - BA}$, the “coordinate-free” sentence after its proof.

^rem-61-4

> [!remark] Remark: Left and Right Actions
> *(Not from the assignment; computed.)* $\mathrm{GL}(n,\mathbb{R})$ acts on row vectors on the right, $p \cdot g = pg$, and $A \mapsto \mathbf{X}^A$, $\mathbf{X}^A_p = \frac{d}{dt}\big|_{t=0}\, p\,(I + tA)$, preserves brackets. It acts on *column* vectors on the left, $g \cdot p = gp$; the corresponding fields $\mathbf{Z}_A$, $(\mathbf{Z}_A)_p = Ap$, satisfy
>
> $$
> [\mathbf{Z}_A, \mathbf{Z}_B] = \mathbf{Z}_{BA - AB} = -\,\mathbf{Z}_{[A,B]} ,
> $$
>
> an anti-homomorphism. Indeed $\mathbf{Z}_A = \sum_k \big(\sum_j a_{kj}x^j\big)\partial_k$, and the first-order part of $\mathbf{Z}_A(\mathbf{Z}_B f)$ is $\sum_{k} \big(\sum_j (Ap)_j\, b_{kj}\big)\partial_k f = \sum_k (BAp)_k\, \partial_k f = \mathbf{Z}_{BA}f$, the second-order parts cancelling as in Proposition [[§61 Lie Group Morphisms and Linear Groups#^prop-61-5|§61.5]]; so $[\mathbf{Z}_A, \mathbf{Z}_B] = \mathbf{Z}_{BA} - \mathbf{Z}_{AB}$. This is the same sign as for right-invariant fields (Theorem [[§60 Lie Groups and Left-Invariant Vector Fields#^thm-60-19|§60.19]], Example [[§60 Lie Groups and Left-Invariant Vector Fields#^ex-60-3|§60.3]]): left multiplication $X \mapsto AX$ generates right-invariant fields, and right multiplication $X \mapsto XA$ left-invariant ones. It is the lecture's aside on writing $(x)f$ (the remark *Left or Right: The Sign of the Bracket*): with maps written on the right, the right action is the one whose composites read in order, and it is the one that preserves brackets.

^rem-61-5
