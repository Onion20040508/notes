---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 7
section: 51
tags: [differentiable-manifolds, math591]
---
← [[§50 Lie Bracket and Lie Algebra]] · ↑ [[· 7 Vector Fields and Lie Groups]] · [[§52 Lie Groups and Left-Invariant Vector Fields]] →

*Stage: fields — Vector fields cannot be pushed forward along an arbitrary smooth map, but two fields can be related by one; related fields have related brackets, and a diffeomorphism carries fields and brackets across.*

*Lecture 17. “Back to vector fields … we're currently taking the operator point of view. Later on, we'll talk about them as generators of dynamics.” Recap: every [[§48 Vector Fields#^def-48-1|vector field]] defines a [[§48 Vector Fields#^def-48-5|derivation]] of $C^\infty(M)$, and conversely ([[§48 Vector Fields#^lem-48-3|Lemma §48.3]], [[§48 Vector Fields#^prop-48-7|Proposition §48.7]]); so the [[§50 Lie Bracket and Lie Algebra#^def-50-1|commutator]] of two fields is again a field ([[§50 Lie Bracket and Lie Algebra#^lem-50-1|Lemma §50.1]]). Officially, a vector field is a smooth section of the tangent bundle ([[§48 Vector Fields#^def-48-1|Definition §48.1]]).*

> [!remark] Remark: Vector Fields Do Not Push Forward
> Given a [[§19 Smooth Functions and Smooth Maps#^def-19-3|smooth map]] $F : M \to N$, “in general, we cannot push forward or pull back vector fields”: vector fields have no functorial properties, “as opposed to [[§47 One-Forms#^def-47-1|differential forms]], … they can always be [[§47 One-Forms#^def-47-4|pulled back]].” Single tangent vectors *can* be [[§28 Derivations and the Abstract Tangent Space#^def-28-6|pushed forward]], by $dF_p$; the trouble is assembling the results into a field on $N$.
> - If $F$ is not injective, two points $p_1 \ne p_2$ with $F(p_1) = F(p_2) = q$ give two candidates $dF_{p_1}(\mathbf{X}_{p_1})$ and $dF_{p_2}(\mathbf{X}_{p_2})$ at $q$, in general different: “which one am I going to push …? It's a multi-valued object.”
> - If $F$ is not surjective, a point $q' \notin F(M)$ gets no candidate at all: “I would have no way of defining [the field] outside the image.”

^rem-51-1

![[m591-49-2.svg]]
*Why a vector field cannot be pushed forward along an arbitrary smooth map $F$: two points $p_1 \ne p_2$ with $F(p_1) = F(p_2) = q$ give two candidates at $q$, and a point $q' \notin F(M)$ gets none.*

The exception is a [[§19 Smooth Functions and Smooth Maps#^def-19-4|diffeomorphism]], where each $q \in N$ is $F(p)$ for exactly one $p$.

> [!remark] Remark: Notation: $dF_p$
> *Lecture 17:* “I'm going to switch the notation to $dF$ … $dF$ will replace $F_{\ast}$. It's a more common notation.” From here on the [[§28 Derivations and the Abstract Tangent Space#^def-28-6|pushforward]] of [[§28 Derivations and the Abstract Tangent Space#^def-28-6|Definition §28.6]] is written
>
> $$
> dF_p = F_{\ast p} : T_pM \to T_{F(p)}N ,
> $$
>
> as in Lee. It agrees with the [[§22 The Differential of a Map Between Vector Spaces#^def-22-5|differential of a map between vector spaces]] ([[§22 The Differential of a Map Between Vector Spaces#^def-22-5|Definition §22.5]]) under the identification $v \leftrightarrow D_v|_a$ of [[§30 The Differential in Coordinates#^cor-30-6|Corollary §30.6]] ([[§30 The Differential in Coordinates#^rem-30-3|§30, Remark]]), so the two uses of $dF_p$ do not clash. Earlier sections keep $F_{\ast p}$.

^rem-51-2

> [!definition] Definition §51.1: Pushforward of a Vector Field by a Diffeomorphism
> Let $F : M \to N$ be a [[§19 Smooth Functions and Smooth Maps#^def-19-4|diffeomorphism]] and $\mathbf{X} \in \mathfrak{X}(M)$. The **pushforward** of $\mathbf{X}$ is the [[§36 Fibrations#^def-36-2|section]] $F_{\ast}\mathbf{X}$ of $TN$ given by
>
> $$
> (F_{\ast}\mathbf{X})_q = dF_{F^{-1}(q)}\big(\mathbf{X}_{F^{-1}(q)}\big), \qquad q \in N .
> $$
>
> *Lee: Ch. 8, Pushforwards of Vector Fields*

^def-51-1

It is smooth, so $F_{\ast}\mathbf{X} \in \mathfrak{X}(N)$: this is [[§51 Related Vector Fields#^prop-51-2|Proposition §51.2]] below. “However, it can happen that you have … fields that are related by $F$, that correspond to one another … It's something that you don't construct. It's something that happens.”

> [!definition] Definition §51.2: $F$-Related Vector Fields
> Let $F : M \to N$ be [[§19 Smooth Functions and Smooth Maps#^def-19-3|smooth]], $\mathbf{X} \in \mathfrak{X}(M)$ and $\mathbf{Y} \in \mathfrak{X}(N)$. Then $\mathbf{X}$ and $\mathbf{Y}$ are **$F$-related** if
>
> $$
> dF_p(\mathbf{X}_p) = \mathbf{Y}_{F(p)} \in T_{F(p)}N \qquad \text{for every } p \in M .
> $$
>
> *Lee: Ch. 8, Vector Fields and Smooth Maps*

^def-51-2

The definition was completed in class by a student: push the value of $\mathbf{X}$ at $p$ forward, “and if it happens that every time I do that, I get the value of $\mathbf{Y}$ at the same point, then we say that the two vector fields are related by $F$.” No injectivity or surjectivity is assumed. Points outside $F(M)$ impose nothing on $\mathbf{Y}$, and two points with the same image must push forward to the same vector. “It's a very useful notion at times.”

> [!example] Example §51.1: Fields Related by a Projection
> Let $\pi : \mathbb{R}^2 \to \mathbb{R}$, $\pi(x, y) = x$, and $\mathbf{Y} = b(x)\, \dfrac{d}{dx}$ with $b \in C^\infty(\mathbb{R})$ — “any vector field on $\mathbb{R}$ I can write like this.” The fields on $\mathbb{R}^2$ that are [[§51 Related Vector Fields#^def-51-2|π-related]] to $\mathbf{Y}$ are exactly
>
> $$
> \mathbf{X} = b(x)\, \frac{\partial}{\partial x} + c(x, y)\, \frac{\partial}{\partial y}, \qquad c \in C^\infty(\mathbb{R}^2) \text{ arbitrary.}
> $$

^ex-51-1

> [!proof]+ Proof
> *(Lecture 17, as a question to the class: “What can I put in the blanks here?” The first component “has to be this guy”; the second, “anything”. The computation is filled in.)* Write $\mathbf{X} = a\, \partial_x + c\, \partial_y$. For $g \in C^\infty(\mathbb{R})$, $d\pi\big(\partial_x|_{(x,y)}\big)[g] = \partial_x (g \circ \pi)(x,y) = g'(x)$ and $d\pi\big(\partial_y|_{(x,y)}\big)[g] = \partial_y\, g(x) = 0$. So $d\pi_{(x,y)}(\mathbf{X}_{(x,y)}) = a(x, y)\, \frac{d}{dx}\big|_x$, and this equals $\mathbf{Y}_x = b(x)\, \frac{d}{dx}\big|_x$ for all $(x, y)$ exactly when $a(x, y) = b(x)$.

^pf-ex-51-1

*Uses:* [[§51 Related Vector Fields#^def-51-2|Def. §51.2]], [[§28 Derivations and the Abstract Tangent Space#^def-28-6|Def. §28.6]], [[§48 Vector Fields#^prop-48-1|§48.1]]

“All I care about is the horizontal component … they all should be the same” along each vertical line, the fibre $\pi^{-1}(x)$, “corresponding to the value down here.”

![[m591-49-3.svg]]
*Fields on $\mathbb{R}^2$ that are $\pi$-related to $\mathbf{Y} = b(x)\,\frac{d}{dx}$: along each fibre $\pi^{-1}(x)$ (dashed) the horizontal part (dotted) is $b(x)$, and the vertical part is arbitrary.*

*The operator viewpoint.* The definition is geometric — “arrows”. There is an equivalent characterization in terms of operators, using the pullback of functions, $F^{\ast}g = g \circ F$.

> [!theorem] Proposition §51.1: Related Fields as Operators
> Let $F : M \to N$ be [[§19 Smooth Functions and Smooth Maps#^def-19-3|smooth]], $\mathbf{X} \in \mathfrak{X}(M)$ and $\mathbf{Y} \in \mathfrak{X}(N)$. Then $\mathbf{X}$ and $\mathbf{Y}$ are [[§51 Related Vector Fields#^def-51-2|F-related]] if and only if
>
> $$
> \mathbf{X}(g \circ F) = (\mathbf{Y}g) \circ F \qquad \text{for every } g \in C^\infty(N),
> $$
>
> that is, $\mathbf{X} \circ F^{\ast} = F^{\ast} \circ \mathbf{Y}$: the pullback $F^{\ast}$ intertwines $\mathbf{X}$ and $\mathbf{Y}$ as [[§48 Vector Fields#^def-48-5|derivations]].
>
> *Lee: Proposition 8.16*

^prop-51-1

![[m591-49-4.svg]]
*The pullback $F^{\ast}$ intertwines the two fields as operators: the square commutes exactly when $\mathbf{X}$ and $\mathbf{Y}$ are $F$-related.*

> [!proof]+ Proof
> *(Lecture 17, “let's have a peek at the proof”; the step for the converse is filled in.)* Let $g \in C^\infty(N)$ and $p \in M$. By the definition of the pushforward ([[§28 Derivations and the Abstract Tangent Space#^def-28-6|Definition §28.6]]) — “we pull back germs, so we push forward derivations” —
>
> $$
> \mathbf{X}(g \circ F)(p) = \mathbf{X}_p[g \circ F] = dF_p(\mathbf{X}_p)[g],
> \qquad
> \big((\mathbf{Y}g) \circ F\big)(p) = \mathbf{Y}_{F(p)}[g] .
> $$
>
> If the fields are $F$-related the right-hand sides agree, for every $g$ and $p$. Conversely, if the left-hand sides agree for every $g \in C^\infty(N)$, the two [[§28 Derivations and the Abstract Tangent Space#^def-28-1|derivations]] $dF_p(\mathbf{X}_p)$ and $\mathbf{Y}_{F(p)}$ at $F(p)$ agree on every global function, hence on every [[§27 Germs#^def-27-2|germ]] at $F(p)$, since every germ has a global representative ([[§48 Vector Fields#^cor-48-5|Corollary §48.5]]); so they are equal. “It's a trivial if and only if once you realize” this.

^pf-51-1

*Uses:* [[§51 Related Vector Fields#^def-51-2|Def. §51.2]], [[§28 Derivations and the Abstract Tangent Space#^def-28-6|Def. §28.6]], [[§28 Derivations and the Abstract Tangent Space#^def-28-1|Def. §28.1]], [[§48 Vector Fields#^cor-48-5|§48.5]]

> [!theorem] Proposition §51.2: Pushforward by a Diffeomorphism
> Let $F : M \to N$ be a [[§19 Smooth Functions and Smooth Maps#^def-19-4|diffeomorphism]] and $\mathbf{X} \in \mathfrak{X}(M)$. Then the [[§51 Related Vector Fields#^def-51-1|pushforward]] $F_{\ast}\mathbf{X}$ is smooth, it is the unique vector field on $N$ that is [[§51 Related Vector Fields#^def-51-2|F-related]] to $\mathbf{X}$, and for every $g \in C^\infty(N)$
>
> $$
> (F_{\ast}\mathbf{X})\, g = \big(\mathbf{X}(g \circ F)\big) \circ F^{-1} .
> $$
>
> *Lee: Proposition 8.19, Corollary 8.21*

^prop-51-2

> [!proof]+ Proof
> *(Not from lecture; filled in.)* For $q \in N$ put $p = F^{-1}(q)$. Then $(F_{\ast}\mathbf{X})_q[g] = dF_p(\mathbf{X}_p)[g] = \mathbf{X}_p[g \circ F] = \mathbf{X}(g \circ F)(F^{-1}(q))$, which is the formula. Its right side is smooth, as $\mathbf{X}(g \circ F)$ is smooth ([[§48 Vector Fields#^lem-48-3|Lemma §48.3]]) and $F^{-1}$ is smooth; so $F_{\ast}\mathbf{X}$ is smooth by [[§48 Vector Fields#^lem-48-8|Lemma §48.8]]. It is $F$-related to $\mathbf{X}$ by its definition. If $\mathbf{Y}$ is also $F$-related to $\mathbf{X}$, then $\mathbf{Y}_q = \mathbf{Y}_{F(p)} = dF_p(\mathbf{X}_p) = (F_{\ast}\mathbf{X})_q$ for every $q$, since $F$ is onto.

^pf-51-2

*Uses:* [[§51 Related Vector Fields#^def-51-1|Def. §51.1]], [[§51 Related Vector Fields#^def-51-2|Def. §51.2]], [[§28 Derivations and the Abstract Tangent Space#^def-28-6|Def. §28.6]], [[§19 Smooth Functions and Smooth Maps#^def-19-4|Def. §19.4]], [[§48 Vector Fields#^lem-48-3|§48.3]], [[§19 Smooth Functions and Smooth Maps#^lem-19-4|§19.4]], [[§48 Vector Fields#^lem-48-8|§48.8]]

*“Now the reason I wanted to do it this way”* — through operators — is the following proposition.

> [!theorem] Proposition §51.3: Naturality of the Bracket
> Let $F : M \to N$ be [[§19 Smooth Functions and Smooth Maps#^def-19-3|smooth]], $\mathbf{X}_1, \mathbf{X}_2 \in \mathfrak{X}(M)$ and $\mathbf{Y}_1, \mathbf{Y}_2 \in \mathfrak{X}(N)$. If $\mathbf{X}_i$ is [[§51 Related Vector Fields#^def-51-2|F-related]] to $\mathbf{Y}_i$ for $i = 1, 2$, then the [[§50 Lie Bracket and Lie Algebra#^def-50-1|bracket]] $[\mathbf{X}_1, \mathbf{X}_2]$ is $F$-related to $[\mathbf{Y}_1, \mathbf{Y}_2]$.
>
> *Lee: Proposition 8.30*

^prop-51-3

> [!proof]+ Proof
> *(Omitted in Lecture 17 as an exercise: “it's just a matter of chasing the definitions … being $F$-related means that $F^{\ast}$ commutes with the derivations. So you just play with the symbols; it all comes out.” Filled in.)* Let $g \in C^\infty(N)$. Applying [[§51 Related Vector Fields#^prop-51-1|Proposition §51.1]] twice,
>
> $$
> \mathbf{X}_1\mathbf{X}_2(g \circ F) = \mathbf{X}_1\big((\mathbf{Y}_2 g) \circ F\big) = (\mathbf{Y}_1\mathbf{Y}_2 g) \circ F ,
> $$
>
> and in the same way $\mathbf{X}_2\mathbf{X}_1(g \circ F) = (\mathbf{Y}_2\mathbf{Y}_1 g) \circ F$. Subtracting, $[\mathbf{X}_1, \mathbf{X}_2](g \circ F) = \big([\mathbf{Y}_1, \mathbf{Y}_2]\, g\big) \circ F$, and [[§51 Related Vector Fields#^prop-51-1|Proposition §51.1]] again gives the claim.

^pf-51-3

*Uses:* [[§51 Related Vector Fields#^prop-51-1|§51.1]], [[§50 Lie Bracket and Lie Algebra#^def-50-1|Def. §50.1]], [[§50 Lie Bracket and Lie Algebra#^lem-50-1|§50.1]]

On omitting this proof: “In a class like this, you cannot prove everything. First of all, there is no time, and second, you would be bored to tears. … But on the other hand, if we just say, oh, you can read the proof, then you don't get a feeling for the subject. So there is a line there somewhere, or a zone, where you have to prove enough, but not too much.” Feedback on where that line should sit is “always welcome.”

> [!theorem] Corollary §51.4: Diffeomorphisms Preserve Brackets
> If $F : M \to N$ is a [[§19 Smooth Functions and Smooth Maps#^def-19-4|diffeomorphism]] and $\mathbf{X}_1, \mathbf{X}_2 \in \mathfrak{X}(M)$, then $F_{\ast}[\mathbf{X}_1, \mathbf{X}_2] = [F_{\ast}\mathbf{X}_1, F_{\ast}\mathbf{X}_2]$.
>
> *Lee: Corollary 8.31*

^cor-51-4

> [!proof]+ Proof
> *(Not from lecture; filled in.)* Each $\mathbf{X}_i$ is $F$-related to $F_{\ast}\mathbf{X}_i$, so $[\mathbf{X}_1, \mathbf{X}_2]$ is $F$-related to $[F_{\ast}\mathbf{X}_1, F_{\ast}\mathbf{X}_2]$ by [[§51 Related Vector Fields#^prop-51-3|Proposition §51.3]]. The only field $F$-related to $[\mathbf{X}_1, \mathbf{X}_2]$ is $F_{\ast}[\mathbf{X}_1, \mathbf{X}_2]$ ([[§51 Related Vector Fields#^prop-51-2|Proposition §51.2]]).

^pf-51-4

*Uses:* [[§51 Related Vector Fields#^prop-51-3|§51.3]], [[§51 Related Vector Fields#^prop-51-2|§51.2]], [[§51 Related Vector Fields#^def-51-1|Def. §51.1]], [[§51 Related Vector Fields#^def-51-2|Def. §51.2]]
