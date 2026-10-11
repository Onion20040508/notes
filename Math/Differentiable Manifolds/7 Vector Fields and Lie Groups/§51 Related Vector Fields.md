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
> *(Lecture 17, as a question to the class: “What can I put in the blanks here?” The first component “has to be this guy”; the second, “anything”. The computation is filled in.)* By Proposition [[§48 Vector Fields#^prop-48-1|§48.1]] in the standard chart of $\mathbb{R}^2$, every vector field on $\mathbb{R}^2$ can be written $\mathbf{X} = a\, \partial_x + c\, \partial_y$ with $a, c \in C^\infty(\mathbb{R}^2)$. Since $\pi(x, y) = x$, Definition [[§51 Related Vector Fields#^def-51-2|§51.2]] says that $\mathbf{X}$ is $\pi$-related to $\mathbf{Y}$ if and only if $d\pi_{(x,y)}(\mathbf{X}_{(x,y)}) = \mathbf{Y}_x$ for every $(x, y)$. So compute the left side.
>
> *The pushforwards of the coordinate vectors.* Let $[g]$ be a germ at $x$ on $\mathbb{R}$. The function $g \circ \pi$ is $(x', y') \mapsto g(x')$. By Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-6|§28.6]] and then Definition [[§29 Coordinate Derivations and the Basis Theorem#^def-29-2|§29.2]] in the standard chart,
>
> $$
> d\pi\big(\partial_x|_{(x,y)}\big)[g] = \partial_x|_{(x,y)}[g \circ \pi] = \partial_x (g \circ \pi)(x,y) = g'(x) = \frac{d}{dx}\Big|_x [g], \qquad
> d\pi\big(\partial_y|_{(x,y)}\big)[g] = \partial_y|_{(x,y)}[g \circ \pi] = \partial_y\, g(x) = 0 ,
> $$
>
> where $d/dx|_x$ is the coordinate derivation of $\mathbb{R}$ at $x$ (Definition [[§32 The Cotangent Space#^def-32-2|§32.2]], with the coordinate written $x$), and $\partial_y\, g(x) = 0$ because $g(x)$ does not depend on $y$. Derivations that agree on every germ are equal, so $d\pi(\partial_x|_{(x,y)}) = d/dx|_x$ and $d\pi(\partial_y|_{(x,y)}) = 0$.
>
> *The condition.* $d\pi_{(x,y)}$ is linear (Proposition [[§28 Derivations and the Abstract Tangent Space#^prop-28-5|§28.5]]), so
>
> $$
> d\pi_{(x,y)}(\mathbf{X}_{(x,y)}) = a(x, y)\, d\pi\big(\partial_x|_{(x,y)}\big) + c(x, y)\, d\pi\big(\partial_y|_{(x,y)}\big) = a(x, y)\, \frac{d}{dx}\Big|_x .
> $$
>
> This equals $\mathbf{Y}_x = b(x)\, \frac{d}{dx}\big|_x$ if and only if $\big(a(x,y) - b(x)\big)\, \frac{d}{dx}\big|_x = 0$, that is, if and only if $a(x, y) = b(x)$, because $d/dx|_x \ne 0$ (it is a basis of $T_x\mathbb{R}$, Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-5|§29.5]]). So the fields $\pi$-related to $\mathbf{Y}$ are those with $a(x, y) = b(x)$ for all $(x, y)$, and $c$ is not constrained. Conversely, for every $c \in C^\infty(\mathbb{R}^2)$ the section $b(x)\,\partial_x + c\,\partial_y$ has smooth coefficients ($(x, y) \mapsto b(x)$ is $b \circ \pi$), so it is a vector field (Proposition [[§48 Vector Fields#^prop-48-1|§48.1]]), and by the computation it is $\pi$-related to $\mathbf{Y}$.
^pf-ex-51-1

*Uses:* [[§51 Related Vector Fields#^def-51-2|Def. §51.2]], [[§28 Derivations and the Abstract Tangent Space#^def-28-6|Def. §28.6]], [[§48 Vector Fields#^prop-48-1|§48.1]], [[§29 Coordinate Derivations and the Basis Theorem#^def-29-2|Def. §29.2]], [[§32 The Cotangent Space#^def-32-2|Def. §32.2]], [[§28 Derivations and the Abstract Tangent Space#^prop-28-5|§28.5]], [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-5|§29.5]]

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
> *(Lecture 17, “let's have a peek at the proof”; the step for the converse is filled in.)* The two forms of the condition are the same, since $(\mathbf{X} \circ F^{\ast})(g) = \mathbf{X}(g \circ F)$ and $(F^{\ast} \circ \mathbf{Y})(g) = (\mathbf{Y}g) \circ F$; and both sides are functions on $M$, so the condition says that they agree at every $p \in M$, for every $g$. Let $g \in C^\infty(N)$ and $p \in M$. The value at $p$ of a field applied to a function is the tangent vector at $p$ applied to its germ (Lemma [[§48 Vector Fields#^lem-48-3|§48.3]]). With this, and the definition of the pushforward (Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-6|§28.6]]) for $D = \mathbf{X}_p$ — “we pull back germs, so we push forward derivations” —
>
> $$
> \mathbf{X}(g \circ F)(p) = \mathbf{X}_p[g \circ F] = dF_p(\mathbf{X}_p)[g],
> \qquad
> \big((\mathbf{Y}g) \circ F\big)(p) = (\mathbf{Y}g)\big(F(p)\big) = \mathbf{Y}_{F(p)}[g] .
> $$
>
> *Related implies intertwining.* If the fields are $F$-related, then $dF_p(\mathbf{X}_p) = \mathbf{Y}_{F(p)}$ (Definition [[§51 Related Vector Fields#^def-51-2|§51.2]]), so the right-hand sides agree, for every $g$ and $p$; that is, $\mathbf{X}(g \circ F) = (\mathbf{Y}g) \circ F$.
>
> *Intertwining implies related.* Conversely, suppose $\mathbf{X}(g \circ F) = (\mathbf{Y}g) \circ F$ for every $g \in C^\infty(N)$, and fix $p \in M$. By the display, the two derivations $dF_p(\mathbf{X}_p)$ and $\mathbf{Y}_{F(p)}$ at $F(p)$ agree on every global function $g$. Every germ $[h]$ at $F(p)$ has a global representative $g \in C^\infty(N)$, $[g] = [h]$ (Corollary [[§48 Vector Fields#^cor-48-5|§48.5]]), so
>
> $$
> dF_p(\mathbf{X}_p)[h] = dF_p(\mathbf{X}_p)[g] = \mathbf{Y}_{F(p)}[g] = \mathbf{Y}_{F(p)}[h] .
> $$
>
> So the two derivations agree on every germ, and are equal as maps on $C^\infty_{F(p)}(N)$: $dF_p(\mathbf{X}_p) = \mathbf{Y}_{F(p)}$. As $p$ was arbitrary, the fields are $F$-related. “It's a trivial if and only if once you realize” this.
^pf-51-1

*Uses:* [[§51 Related Vector Fields#^def-51-2|Def. §51.2]], [[§28 Derivations and the Abstract Tangent Space#^def-28-6|Def. §28.6]], [[§28 Derivations and the Abstract Tangent Space#^def-28-1|Def. §28.1]], [[§48 Vector Fields#^cor-48-5|§48.5]], [[§48 Vector Fields#^lem-48-3|§48.3]]

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
> *(Not from lecture; filled in.)* Four things are claimed: the formula, smoothness, $F$-relatedness, and uniqueness. Here $(F_\ast\mathbf{X})\,g$ denotes the function $q \mapsto (F_\ast\mathbf{X})_q[g]$ on $N$, as in Lemma [[§48 Vector Fields#^lem-48-8|§48.8]].
>
> *The formula.* For $q \in N$ put $p = F^{-1}(q)$. By Definition [[§51 Related Vector Fields#^def-51-1|§51.1]], then Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-6|§28.6]] with $D = \mathbf{X}_p$, then Lemma [[§48 Vector Fields#^lem-48-3|§48.3]],
>
> $$
> (F_\ast\mathbf{X})_q[g] = dF_p(\mathbf{X}_p)[g] = \mathbf{X}_p[g \circ F] = \mathbf{X}(g \circ F)(p) = \big(\mathbf{X}(g \circ F) \circ F^{-1}\big)(q) ,
> $$
>
> which is the formula.
>
> *Smoothness.* At each $q$, $(F_\ast\mathbf{X})_q = dF_p(\mathbf{X}_p)$ lies in $T_{F(p)}N = T_qN$, so $F_\ast\mathbf{X}$ is a section of $TN$. In the formula, $g \circ F \in C^\infty(M)$ (Lemma [[§19 Smooth Functions and Smooth Maps#^lem-19-4|§19.4]]), so $\mathbf{X}(g \circ F)$ is smooth (Lemma [[§48 Vector Fields#^lem-48-3|§48.3]]); and $F^{-1}$ is smooth because $F$ is a diffeomorphism (Definition [[§19 Smooth Functions and Smooth Maps#^def-19-4|§19.4]]), so the composite $\mathbf{X}(g \circ F) \circ F^{-1}$ is smooth (Lemma [[§19 Smooth Functions and Smooth Maps#^lem-19-4|§19.4]]). This holds for every $g \in C^\infty(N)$, so $F_\ast\mathbf{X}$ is smooth by Lemma [[§48 Vector Fields#^lem-48-8|§48.8]].
>
> *$F$-related.* For $p \in M$, $F^{-1}(F(p)) = p$, so Definition [[§51 Related Vector Fields#^def-51-1|§51.1]] at $q = F(p)$ reads $(F_\ast\mathbf{X})_{F(p)} = dF_p(\mathbf{X}_p)$. This is Definition [[§51 Related Vector Fields#^def-51-2|§51.2]] with $\mathbf{Y} = F_\ast\mathbf{X}$.
>
> *Uniqueness.* If $\mathbf{Y} \in \mathfrak{X}(N)$ is also $F$-related to $\mathbf{X}$, let $q \in N$. Since $F$ is onto, $q = F(p)$ with $p = F^{-1}(q)$, and by Definition [[§51 Related Vector Fields#^def-51-2|§51.2]] and then Definition [[§51 Related Vector Fields#^def-51-1|§51.1]],
>
> $$
> \mathbf{Y}_q = \mathbf{Y}_{F(p)} = dF_p(\mathbf{X}_p) = (F_\ast\mathbf{X})_q .
> $$
>
> This holds for every $q$, so $\mathbf{Y} = F_\ast\mathbf{X}$.
^pf-51-2

*Uses:* [[§51 Related Vector Fields#^def-51-1|Def. §51.1]], [[§51 Related Vector Fields#^def-51-2|Def. §51.2]], [[§28 Derivations and the Abstract Tangent Space#^def-28-6|Def. §28.6]], [[§19 Smooth Functions and Smooth Maps#^def-19-4|Def. §19.4]], [[§48 Vector Fields#^lem-48-3|§48.3]], [[§19 Smooth Functions and Smooth Maps#^lem-19-4|§19.4]], [[§48 Vector Fields#^lem-48-8|§48.8]]

*“Now the reason I wanted to do it this way”* — through operators — is the following proposition.

> [!theorem] Proposition §51.3: Naturality of the Bracket
> Let $F : M \to N$ be [[§19 Smooth Functions and Smooth Maps#^def-19-3|smooth]], $\mathbf{X}_1, \mathbf{X}_2 \in \mathfrak{X}(M)$ and $\mathbf{Y}_1, \mathbf{Y}_2 \in \mathfrak{X}(N)$. If $\mathbf{X}_i$ is [[§51 Related Vector Fields#^def-51-2|F-related]] to $\mathbf{Y}_i$ for $i = 1, 2$, then the [[§50 Lie Bracket and Lie Algebra#^def-50-1|bracket]] $[\mathbf{X}_1, \mathbf{X}_2]$ is $F$-related to $[\mathbf{Y}_1, \mathbf{Y}_2]$.
>
> *Lee: Proposition 8.30*

^prop-51-3

> [!proof]+ Proof
> *(Omitted in Lecture 17 as an exercise: “it's just a matter of chasing the definitions \ldots being $F$-related means that $F^{\ast}$ commutes with the derivations. So you just play with the symbols; it all comes out.” Filled in.)* The brackets $[\mathbf{X}_1, \mathbf{X}_2] \in \mathfrak{X}(M)$ and $[\mathbf{Y}_1, \mathbf{Y}_2] \in \mathfrak{X}(N)$ are vector fields (Lemma [[§50 Lie Bracket and Lie Algebra#^lem-50-1|§50.1]]). By Proposition [[§51 Related Vector Fields#^prop-51-1|§51.1]], it suffices to show
>
> $$
> [\mathbf{X}_1, \mathbf{X}_2](g \circ F) = \big([\mathbf{Y}_1, \mathbf{Y}_2]\, g\big) \circ F \qquad \text{for every } g \in C^\infty(N).
> $$
>
> Let $g \in C^\infty(N)$. The same proposition, applied to the pairs $(\mathbf{X}_i, \mathbf{Y}_i)$, gives $\mathbf{X}_i(h \circ F) = (\mathbf{Y}_i h) \circ F$ for every $h \in C^\infty(N)$ and $i = 1, 2$.
>
> *The composite $\mathbf{X}_1\mathbf{X}_2$.* Apply this first for $i = 2$ with $h = g$, and then for $i = 1$ with $h = \mathbf{Y}_2 g$, which lies in $C^\infty(N)$ by Lemma [[§48 Vector Fields#^lem-48-3|§48.3]]:
>
> $$
> \mathbf{X}_1\mathbf{X}_2(g \circ F) = \mathbf{X}_1\big((\mathbf{Y}_2 g) \circ F\big) = (\mathbf{Y}_1\mathbf{Y}_2 g) \circ F .
> $$
>
> *The composite $\mathbf{X}_2\mathbf{X}_1$.* Apply it first for $i = 1$ with $h = g$, and then for $i = 2$ with $h = \mathbf{Y}_1 g$:
>
> $$
> \mathbf{X}_2\mathbf{X}_1(g \circ F) = \mathbf{X}_2\big((\mathbf{Y}_1 g) \circ F\big) = (\mathbf{Y}_2\mathbf{Y}_1 g) \circ F .
> $$
>
> *Subtracting.* By Definition [[§50 Lie Bracket and Lie Algebra#^def-50-1|§50.1]], and since $u \circ F - v \circ F = (u - v) \circ F$ for functions $u, v$ on $N$,
>
> $$
> [\mathbf{X}_1, \mathbf{X}_2](g \circ F) = (\mathbf{Y}_1\mathbf{Y}_2 g) \circ F - (\mathbf{Y}_2\mathbf{Y}_1 g) \circ F = \big(\mathbf{Y}_1\mathbf{Y}_2 g - \mathbf{Y}_2\mathbf{Y}_1 g\big) \circ F = \big([\mathbf{Y}_1, \mathbf{Y}_2]\, g\big) \circ F ,
> $$
>
> and Proposition [[§51 Related Vector Fields#^prop-51-1|§51.1]] again, with $\mathbf{X} = [\mathbf{X}_1, \mathbf{X}_2]$ and $\mathbf{Y} = [\mathbf{Y}_1, \mathbf{Y}_2]$, gives the claim.
^pf-51-3

*Uses:* [[§51 Related Vector Fields#^prop-51-1|§51.1]], [[§50 Lie Bracket and Lie Algebra#^def-50-1|Def. §50.1]], [[§50 Lie Bracket and Lie Algebra#^lem-50-1|§50.1]], [[§48 Vector Fields#^lem-48-3|§48.3]]

On omitting this proof: “In a class like this, you cannot prove everything. First of all, there is no time, and second, you would be bored to tears. … But on the other hand, if we just say, oh, you can read the proof, then you don't get a feeling for the subject. So there is a line there somewhere, or a zone, where you have to prove enough, but not too much.” Feedback on where that line should sit is “always welcome.”

> [!theorem] Corollary §51.4: Diffeomorphisms Preserve Brackets
> If $F : M \to N$ is a [[§19 Smooth Functions and Smooth Maps#^def-19-4|diffeomorphism]] and $\mathbf{X}_1, \mathbf{X}_2 \in \mathfrak{X}(M)$, then $F_{\ast}[\mathbf{X}_1, \mathbf{X}_2] = [F_{\ast}\mathbf{X}_1, F_{\ast}\mathbf{X}_2]$.
>
> *Lee: Corollary 8.31*

^cor-51-4

> [!proof]+ Proof
> *(Not from lecture; filled in.)* By Proposition [[§51 Related Vector Fields#^prop-51-2|§51.2]], each $F_\ast\mathbf{X}_i$ is a vector field on $N$ and $\mathbf{X}_i$ is $F$-related to $F_\ast\mathbf{X}_i$, for $i = 1, 2$. So Proposition [[§51 Related Vector Fields#^prop-51-3|§51.3]], with $\mathbf{Y}_i = F_\ast\mathbf{X}_i$, shows that $[\mathbf{X}_1, \mathbf{X}_2]$ is $F$-related to $[F_\ast\mathbf{X}_1, F_\ast\mathbf{X}_2]$. On the other hand $[\mathbf{X}_1, \mathbf{X}_2] \in \mathfrak{X}(M)$ (Lemma [[§50 Lie Bracket and Lie Algebra#^lem-50-1|§50.1]]), so Proposition [[§51 Related Vector Fields#^prop-51-2|§51.2]], applied to this field, says that the only field on $N$ that is $F$-related to $[\mathbf{X}_1, \mathbf{X}_2]$ is $F_\ast[\mathbf{X}_1, \mathbf{X}_2]$. Both $[F_\ast\mathbf{X}_1, F_\ast\mathbf{X}_2]$ and $F_\ast[\mathbf{X}_1, \mathbf{X}_2]$ are such fields, so they are equal.
^pf-51-4

*Uses:* [[§51 Related Vector Fields#^prop-51-3|§51.3]], [[§51 Related Vector Fields#^prop-51-2|§51.2]], [[§51 Related Vector Fields#^def-51-1|Def. §51.1]], [[§51 Related Vector Fields#^def-51-2|Def. §51.2]], [[§50 Lie Bracket and Lie Algebra#^lem-50-1|§50.1]]
