---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 8
section: 61
tags: [differentiable-manifolds, math591]
---
← [[§60 Lie Groups and Left-Invariant Vector Fields]] · ↑ [[· 8 Vector Fields and Lie Groups]] · [[§62 Sets of Measure Zero]] →

*Stage: symmetry — Maps of Lie groups induce maps of Lie algebras that preserve brackets; for a linear group the bracket is the matrix commutator.*

*Lecture 18. “Next, we want to talk about Lie group morphisms and the Lie algebra, because we can do something now that we couldn't before.”*

> [!remark] Remark: From Now On: $\mathfrak{g}$ Is $T_eG$
> “From now on, as you can imagine, we will identify” the Lie algebra with the tangent space at the identity, $\mathfrak{g} \cong T_eG$ by $\mathrm{ev}$ (Theorem [[§60 Lie Groups and Left-Invariant Vector Fields#^thm-60-7|§60.7]]), as vector spaces, “keeping in mind that the Lie bracket comes from … commuting left-invariant fields.” That is Definition [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-4|§60.4]] read through Definition [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-6|§60.6]]: to compute the bracket of $A, B \in T_eG$,
>
> 1. extend $A$ and $B$ to the left-invariant fields $\mathbf{X}^A$, $\mathbf{X}^B$, their left-invariant extensions (Definition [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-5|§60.5]]; they lie in $\mathfrak{g}$ by Proposition [[§60 Lie Groups and Left-Invariant Vector Fields#^prop-60-6|§60.6]]);
> 2. take the commutator $[\mathbf{X}^A, \mathbf{X}^B]$ of vector fields;
> 3. evaluate it at the identity: $[A, B] = [\mathbf{X}^A, \mathbf{X}^B]_e$.
>
> “That's the definition.” Elements of $T_eG$ are now written with capital letters: “I really kind of think of them as matrices.”

^rem-61-1

> [!definition] Definition §61.1: Linear Group
> A **linear group**, or **matrix group**, is a Lie group $G$ (Definition [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-1|§60.1]]) that is a subgroup of $\mathrm{GL}(n,\mathbb{R})$ or $\mathrm{GL}(n,\mathbb{C})$ for some $n$, with matrix multiplication as its group product — for instance each classical group of Proposition [[§60 Lie Groups and Left-Invariant Vector Fields#^prop-60-1|§60.1]].

^def-61-1

> [!remark] Remark: Nonlinear Groups
> Matrix groups “are called linear groups, by the way” (Definition [[§61 Lie Group Morphisms and Linear Groups#^def-61-1|§61.1]]). “And not every Lie group is isomorphic to a matrix group … the nonlinear groups arise naturally from making covers” of matrix groups. *(Filled in: the standard example is the universal cover of $\mathrm{SL}(2,\mathbb{R})$, a Lie group isomorphic to no group of matrices.)* The question of Lecture 17, restated: for a matrix group, “can we identify the bracket directly on the tangent space at the identity?” The answer is the matrix commutator (Theorem [[§60 Lie Groups and Left-Invariant Vector Fields#^thm-60-8|§60.8]]); to get there, the course uses the general idea below.

^rem-61-2

> [!definition] Definition §61.2: Lie Group Morphism
> Let $H$ and $G$ be [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-1|Lie groups]]. A **Lie group morphism** (homomorphism) $F : H \to G$ is a map that is both [[§19 Smooth Functions and Smooth Maps#^def-19-3|smooth]] and a [[§15 Homomorphisms#^def-15-1|group morphism]]: $F(gh) = F(g)F(h)$ for all $g, h \in H$.
>
> *Lee: Ch. 7, Lie Group Homomorphisms*

^def-61-2

A Lie group is “a manifold and a group, and the various maps are smooth”, so a morphism “preserves both structures.” In particular $F(e_H) = e_G$. *(Filled in: $F(e_H) = F(e_He_H) = F(e_H)F(e_H)$; multiply on the left by $F(e_H)^{-1}$.)* So $F$ has a differential at the identity,

$$
dF_e : T_{e}H \longrightarrow T_{e}G, \qquad \text{that is,} \qquad dF_e : \mathfrak{h} \longrightarrow \mathfrak{g},
$$

a linear map between the Lie algebras, and “the natural question is whether this map preserves commutators.”

> [!definition] Definition §61.3: Lie Algebra Morphism
> Let $\mathfrak{h}$ and $\mathfrak{g}$ be Lie algebras (Definition [[§58 Lie Bracket and Lie Algebra#^def-58-2|§58.2]]). A **Lie algebra morphism** is a linear map $\phi : \mathfrak{h} \to \mathfrak{g}$ that preserves brackets: $\phi([A, B]) = [\phi(A), \phi(B)]$ for all $A, B \in \mathfrak{h}$.
>
> *Lee: Ch. 8, Induced Lie Algebra Homomorphisms*

^def-61-3

> [!theorem] Lemma §61.1: Left-Invariant Fields Related by a Morphism
> Let $F : H \to G$ be a Lie group morphism (Definition [[§61 Lie Group Morphisms and Linear Groups#^def-61-2|§61.2]]) and $A \in T_eH$, and put $\tilde A = dF_e(A) \in T_eG$. Let $\mathbf{X}^A \in \mathfrak{X}(H)$ and $\mathbf{Y}^{\tilde A} \in \mathfrak{X}(G)$ be the left-invariant extensions of $A$ and of $\tilde A$ (Definition [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-5|§60.5]]; smooth by Proposition [[§60 Lie Groups and Left-Invariant Vector Fields#^prop-60-6|§60.6]]). Then $\mathbf{X}^A$ and $\mathbf{Y}^{\tilde A}$ are $F$-related (Definition [[§59 Related Vector Fields#^def-59-2|§59.2]]):
>
> $$
> dF_h\big(\mathbf{X}^A_h\big) = \mathbf{Y}^{\tilde A}_{F(h)} \in T_{F(h)}G \qquad \text{for every } h \in H .
> $$
>
> *Lee: proof of Theorem 8.44*

^lem-61-1

> [!proof]+ Proof
> *(Lecture 18: the “claim” in the proof that Lie group morphisms preserve brackets. The final diagram chase, left to the class as the lecture ran out of time, is completed.)* Fix $h \in H$; the displayed equality is to be shown. *$F(e) = e$.* As noted after Definition [[§61 Lie Group Morphisms and Linear Groups#^def-61-2|§61.2]], $F(e_H) = F(e_He_H) = F(e_H)F(e_H)$, and multiplying on the left by $F(e_H)^{-1}$ gives $F(e_H) = e_G$; so $dF_e$ maps $T_eH$ to $T_eG$, and $\tilde A \in T_eG$.
>
> *The square.* “We have to use very much that $F$ is a group morphism.” Consider the square
>
> $$
> F \circ L_h = L_{F(h)} \circ F : H \to G .
> $$
>
> It commutes: for $x \in H$, $F(L_h(x)) = F(hx) = F(h)F(x) = L_{F(h)}(F(x))$, where $L$ is “always left multiplication in the corresponding group.” Differentiate it at $e \in H$. Since $L_h(e) = h$ and $F(e) = e$, the chain rule (Theorem [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]]) gives the commutative square of differentials
>
> $$
> dF_h \circ d(L_h)_e = d\big(L_{F(h)}\big)_e \circ dF_e : T_eH \to T_{F(h)}G .
> $$
>
> *The chase.* *(Completed.)* “Chase where $A$ goes under this diagram”:
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
> *(Lecture 18 — “kind of a soft proof”.)* “Since the bracket is defined in terms of vector fields, I have to pass to vector fields to do the proof.” For $A \in T_eH$ let $\mathbf{X}^A \in \mathfrak{X}(H)$ be the left-invariant extension of $A$, the left-invariant field with $\mathbf{X}^A_e = A$; put $\tilde A = dF_e(A) \in T_eG$, and let $\mathbf{Y}^{\tilde A} \in \mathfrak{X}(G)$ be the left-invariant extension of $\tilde A$, with $\mathbf{Y}^{\tilde A}_e = \tilde A$ (Definition [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-5|§60.5]] and Proposition [[§60 Lie Groups and Left-Invariant Vector Fields#^prop-60-6|§60.6]], applied to $H$ and to $G$).
>
> *Claim.* $\mathbf{X}^A$ and $\mathbf{Y}^{\tilde A}$ are $F$-related (Definition [[§59 Related Vector Fields#^def-59-2|§59.2]]).
>
> *The proposition follows from the claim.* Let also $B \in T_eH$ and $\tilde B = dF_e(B)$. By the claim, $\mathbf{X}^A$ is $F$-related to $\mathbf{Y}^{\tilde A}$ and $\mathbf{X}^B$ to $\mathbf{Y}^{\tilde B}$, so by Proposition [[§59 Related Vector Fields#^prop-59-3|§59.3]], $[\mathbf{X}^A, \mathbf{X}^B]$ is $F$-related to $[\mathbf{Y}^{\tilde A}, \mathbf{Y}^{\tilde B}]$. Evaluate at $e \in H$, using $F(e) = e$:
>
> $$
> dF_e\big([\mathbf{X}^A, \mathbf{X}^B]_e\big) = [\mathbf{Y}^{\tilde A}, \mathbf{Y}^{\tilde B}]_{F(e)} = [\mathbf{Y}^{\tilde A}, \mathbf{Y}^{\tilde B}]_e .
> $$
>
> By Definition [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-6|§60.6]] the left side is $dF_e([A, B])$ and the right side is $[\tilde A, \tilde B] = [dF_e(A), dF_e(B)]$: “that's exactly” the proposition. “So the fight is to prove the claim”: it is Lemma [[§61 Lie Group Morphisms and Linear Groups#^lem-61-1|§61.1]], applied to $F$ and $A$, whose proof is the diagram chase above.

^pf-61-2

*Uses:* [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-5|Def. §60.5]], [[§60 Lie Groups and Left-Invariant Vector Fields#^prop-60-6|§60.6]], [[§59 Related Vector Fields#^def-59-2|Def. §59.2]], [[§59 Related Vector Fields#^prop-59-3|§59.3]], [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-6|Def. §60.6]], [[§61 Lie Group Morphisms and Linear Groups#^lem-61-1|§61.1]]

Next: the commutator, “first for the general linear group, and then … for any linear group” (Theorem [[§60 Lie Groups and Left-Invariant Vector Fields#^thm-60-8|§60.8]]).

**Transcription note (Lecture 18).** Page 47 of the handwritten notes begins the proof with “take $A \in T_hH$”; $A \in T_eH$. Page 48 writes the second field as $\mathbf{Y}^{\hat B}$ in one place; it is $\mathbf{Y}^{\tilde B}$, with $\tilde B = dF_e(B)$.

## The Bracket of a Matrix Group

*Lecture 19 began with a review, “just because last time was a little bit complex”: the Lie algebra $\mathfrak{g}$ of left-invariant fields, closed under commutators (Corollary [[§60 Lie Groups and Left-Invariant Vector Fields#^cor-60-4|§60.4]]); the isomorphism $\mathrm{ev} : \mathfrak{g} \to T_eG$ with inverse $A \mapsto \mathbf{X}^A$ (Theorem [[§60 Lie Groups and Left-Invariant Vector Fields#^thm-60-7|§60.7]]), including the check that $\mathbf{X}^A$ is left-invariant (Lemma [[§60 Lie Groups and Left-Invariant Vector Fields#^lem-60-5|§60.5]](2)); and the bracket on $T_eG$, “I keep forgetting to do it, but it's important to write it” (Definition [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-6|§60.6]]), defined so that $\mathrm{ev}$ is an isomorphism of Lie algebras.*

> [!remark] Remark: The Lie Algebra in Practice
> “In practice, when you say, `What's the Lie algebra of the orthogonal group?', the answer is never `some left-invariant fields', right? The answer is always: well, it's the tangent space at the identity” — with the bracket of Definition [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-6|§60.6]], which for matrix groups is the matrix commutator (Theorem [[§61 Lie Group Morphisms and Linear Groups#^thm-61-3|§61.3]] below). The notation $\mathfrak{gl}(d, \mathbb{R}) = T_I\mathrm{GL}(d,\mathbb{R}) = \operatorname{Mat}(d,\mathbb{R})$ is standard.

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
> *(Lecture 19.)* “By assumption, $G$ is included in some general linear group … as a Lie subgroup, and the differential of the inclusion map at the identity is the inclusion” $di_I : T_IG \hookrightarrow \mathfrak{gl}(d, \mathbb{R})$. The inclusion is a Lie group morphism (Definition [[§61 Lie Group Morphisms and Linear Groups#^def-61-2|§61.2]]): smooth by hypothesis, and a group morphism because the product on $G$ is matrix multiplication. So by Proposition [[§61 Lie Group Morphisms and Linear Groups#^prop-61-2|§61.2]], for $A, B \in T_IG$,
>
> $$
> di_I\big([A, B]_G\big) = \big[di_I(A), di_I(B)\big]_{\mathrm{GL}(d,\mathbb{R})} = di_I(A)\, di_I(B) - di_I(B)\, di_I(A),
> $$
>
> the last step by Theorem [[§60 Lie Groups and Left-Invariant Vector Fields#^thm-60-8|§60.8]]. Under the identification of $T_IG$ with its image, which $di_I$ injective makes legitimate, this is $[A, B] = AB - BA$. “If we know that the bracket for the general linear group is a commutator, then for every linear group, it's got to be the commutator too, … just some algebra.” *(Filled in: a regular submanifold qualifies, since $i$ is smooth by Lemma [[§37 Regular Submanifolds#^lem-37-5|§37.5]](1), with coordinate representation $r \mapsto (r, \vec 0)$ in an adapted chart, whose differential is injective.)*

^pf-61-3

*Uses:* [[§61 Lie Group Morphisms and Linear Groups#^def-61-2|Def. §61.2]], [[§61 Lie Group Morphisms and Linear Groups#^prop-61-2|§61.2]], [[§60 Lie Groups and Left-Invariant Vector Fields#^thm-60-8|§60.8]], [[§37 Regular Submanifolds#^lem-37-5|§37.5]]

In particular $di_I(T_IG)$ is closed under the matrix commutator, as the image of a bracket. Lecture 19 checked this directly in one case: “we have a theorem, but it's good to check.”

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
> *(Lecture 19.)* $[A, B]^{\mathsf T} = (AB - BA)^{\mathsf T} = B^{\mathsf T}A^{\mathsf T} - A^{\mathsf T}B^{\mathsf T} = (-B)(-A) - (-A)(-B) = BA - AB = -[A, B]$. “You can do the same for the unitary [group] — that was the homework problem. Instead of transpose, you have star, complex transpose conjugate, and the same computation works.”

^pf-ex-61-1

**Transcription note (Lecture 19).** Page 49 of the handwritten notes writes the evaluation map as $\mathfrak{g} \to T_eM$ and its inverse from $T_eM$; the group is $G$, so $T_eG$. The definition of the bracket there reads “$[A, B] = [\mathbf{X}^A, \mathbf{X}^B]$”; the field bracket is evaluated at the identity, $[A, B] = [\mathbf{X}^A, \mathbf{X}^B]_e$ (Definition [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-6|§60.6]]), as Uribe said in lecture (“now we go back by evaluating at $e$”).
