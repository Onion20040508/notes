---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 8
section: 59
tags: [differentiable-manifolds, math591]
---
← [[§58 Lie Bracket and Lie Algebra]] · ↑ [[· 8 Vector Fields and Lie Groups]] · [[§60 Lie Groups and Left-Invariant Vector Fields]] →

*Stage: fields — Vector fields cannot be pushed forward along an arbitrary smooth map, but two fields can be related by one; related fields have related brackets, and a diffeomorphism carries fields and brackets across.*

*Lecture 17. “Back to vector fields … we're currently taking the operator point of view. Later on, we'll talk about them as generators of dynamics.” Recap: every [[§56 Vector Fields#^def-56-1|vector field]] defines a [[§56 Vector Fields#^def-56-5|derivation]] of $C^\infty(M)$, and conversely ([[§56 Vector Fields#^lem-56-3|Lemma §56.3]], [[§56 Vector Fields#^prop-56-7|Proposition §56.7]]); so the [[§58 Lie Bracket and Lie Algebra#^def-58-1|commutator]] of two fields is again a field ([[§58 Lie Bracket and Lie Algebra#^lem-58-1|Lemma §58.1]]). Officially, a vector field is a smooth section of the tangent bundle ([[§56 Vector Fields#^def-56-1|Definition §56.1]]).*

> [!remark] Remark: Vector Fields Do Not Push Forward
> Given a [[§19 Smooth Functions and Smooth Maps#^def-19-3|smooth map]] $F : M \to N$, “in general, we cannot push forward or pull back vector fields”: vector fields have no functorial properties, “as opposed to [[§53 One-Forms#^def-53-1|differential forms]], … they can always be [[§53 One-Forms#^def-53-4|pulled back]].” Single tangent vectors *can* be [[§28 Derivations and the Abstract Tangent Space#^def-28-6|pushed forward]], by $dF_p$; the trouble is assembling the results into a field on $N$.
> - If $F$ is not injective, two points $p_1 \ne p_2$ with $F(p_1) = F(p_2) = q$ give two candidates $dF_{p_1}(\mathbf{X}_{p_1})$ and $dF_{p_2}(\mathbf{X}_{p_2})$ at $q$, in general different: “which one am I going to push …? It's a multi-valued object.”
> - If $F$ is not surjective, a point $q' \notin F(M)$ gets no candidate at all: “I would have no way of defining [the field] outside the image.”

^rem-59-1

![[m591-49-2.svg]]
*Why a vector field cannot be pushed forward along an arbitrary smooth map $F$: two points $p_1 \ne p_2$ with $F(p_1) = F(p_2) = q$ give two candidates at $q$, and a point $q' \notin F(M)$ gets none.*

The exception is a [[§19 Smooth Functions and Smooth Maps#^def-19-4|diffeomorphism]], where each $q \in N$ is $F(p)$ for exactly one $p$.

> [!remark] Remark: Notation: $dF_p$
> *Lecture 17:* “I'm going to switch the notation to $dF$ … $dF$ will replace $F_\ast$. It's a more common notation.” From here on the [[§28 Derivations and the Abstract Tangent Space#^def-28-6|pushforward]] of Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-6|§28.6]] is written
>
> $$
> dF_p = F_{\ast p} : T_pM \to T_{F(p)}N ,
> $$
>
> as in Lee. It agrees with the [[§22 The Differential of a Map Between Vector Spaces#^def-22-5|differential of a map between vector spaces]] (Definition [[§22 The Differential of a Map Between Vector Spaces#^def-22-5|§22.5]]) under the identification $v \leftrightarrow D_v|_a$ of Corollary [[§30 The Differential in Coordinates#^cor-30-6|§30.6]] (the remark in [[§30 The Differential in Coordinates|§30]]), so the two uses of $dF_p$ do not clash. Earlier sections keep $F_{\ast p}$.

^rem-59-2

> [!definition] Definition §59.1: Pushforward of a Vector Field by a Diffeomorphism
> Let $F : M \to N$ be a [[§19 Smooth Functions and Smooth Maps#^def-19-4|diffeomorphism]] and $\mathbf{X} \in \mathfrak{X}(M)$. The **pushforward** of $\mathbf{X}$ is the [[§40 Fibrations#^def-40-3|section]] $F_{\ast}\mathbf{X}$ of $TN$ given by
>
> $$
> (F_{\ast}\mathbf{X})_q = dF_{F^{-1}(q)}\big(\mathbf{X}_{F^{-1}(q)}\big), \qquad q \in N .
> $$
>
> *Lee: Ch. 8, Pushforwards of Vector Fields*

^def-59-1

It is smooth, so $F_{\ast}\mathbf{X} \in \mathfrak{X}(N)$: this is [[§59 Related Vector Fields#^prop-59-2|Proposition §59.2]] below. “However, it can happen that you have … fields that are related by $F$, that correspond to one another … It's something that you don't construct. It's something that happens.”

> [!definition] Definition §59.2: $F$-Related Vector Fields
> Let $F : M \to N$ be [[§19 Smooth Functions and Smooth Maps#^def-19-3|smooth]], $\mathbf{X} \in \mathfrak{X}(M)$ and $\mathbf{Y} \in \mathfrak{X}(N)$. Then $\mathbf{X}$ and $\mathbf{Y}$ are **$F$-related** if
>
> $$
> dF_p(\mathbf{X}_p) = \mathbf{Y}_{F(p)} \in T_{F(p)}N \qquad \text{for every } p \in M .
> $$
>
> *Lee: Ch. 8, Vector Fields and Smooth Maps*

^def-59-2

The definition was completed in class by a student: push the value of $\mathbf{X}$ at $p$ forward, “and if it happens that every time I do that, I get the value of $\mathbf{Y}$ at the same point, then we say that the two vector fields are related by $F$.” No injectivity or surjectivity is assumed. Points outside $F(M)$ impose nothing on $\mathbf{Y}$, and two points with the same image must push forward to the same vector. “It's a very useful notion at times.”
*(Computed; not from lecture.)* In charts $(U, (x^1, \ldots, x^m))$ of $M$ and $(V, (y^1, \ldots, y^n))$ of $N$ with $F(U) \subseteq V$, $m = \dim M$, $n = \dim N$, write $F^j = y^j \circ F$, $\mathbf{X} = \sum_i \mathbf{X}^i\, \partial/\partial x^i$ and $\mathbf{Y} = \sum_j \mathbf{Y}^j\, \partial/\partial y^j$. The matrix of $dF_p$ is the Jacobian of Theorem [[§30 The Differential in Coordinates#^thm-30-2|§30.2]], so the condition reads, at every $p \in U$,

$$
\begin{pmatrix}
\dfrac{\partial F^1}{\partial x^1}(p) & \cdots & \dfrac{\partial F^1}{\partial x^m}(p) \\
\vdots & \ddots & \vdots \\
\dfrac{\partial F^n}{\partial x^1}(p) & \cdots & \dfrac{\partial F^n}{\partial x^m}(p)
\end{pmatrix}
\begin{pmatrix} \mathbf{X}^1(p) \\ \vdots \\ \mathbf{X}^m(p) \end{pmatrix}
=
\begin{pmatrix} \mathbf{Y}^1(F(p)) \\ \vdots \\ \mathbf{Y}^n(F(p)) \end{pmatrix} .
$$

> [!example] Example §59.1: Fields Related by a Projection
> Let $\pi : \mathbb{R}^2 \to \mathbb{R}$, $\pi(x, y) = x$, and $\mathbf{Y} = b(x)\, \dfrac{d}{dx}$ with $b \in C^\infty(\mathbb{R})$ — “any vector field on $\mathbb{R}$ I can write like this.” The fields on $\mathbb{R}^2$ that are [[§59 Related Vector Fields#^def-59-2|π-related]] to $\mathbf{Y}$ are exactly
>
> $$
> \mathbf{X} = b(x)\, \frac{\partial}{\partial x} + c(x, y)\, \frac{\partial}{\partial y}, \qquad c \in C^\infty(\mathbb{R}^2) \text{ arbitrary.}
> $$

^ex-59-1

> [!proof]+ Proof
> *(Lecture 17, as a question to the class: “What can I put in the blanks here?” The first component “has to be this guy”; the second, “anything”. The computation is filled in.)* By Proposition [[§56 Vector Fields#^prop-56-1|§56.1]] in the standard chart of $\mathbb{R}^2$, every vector field on $\mathbb{R}^2$ can be written $\mathbf{X} = a\, \partial_x + c\, \partial_y$ with $a, c \in C^\infty(\mathbb{R}^2)$. Since $\pi(x, y) = x$, Definition [[§59 Related Vector Fields#^def-59-2|§59.2]] says that $\mathbf{X}$ is $\pi$-related to $\mathbf{Y}$ if and only if $d\pi_{(x,y)}(\mathbf{X}_{(x,y)}) = \mathbf{Y}_x$ for every $(x, y)$. So compute the left side.
>
> *The pushforwards of the coordinate vectors.* Let $[g]$ be a germ at $x$ on $\mathbb{R}$. The function $g \circ \pi$ is $(x', y') \mapsto g(x')$. By Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-6|§28.6]] and then Definition [[§29 Coordinate Derivations and the Basis Theorem#^def-29-2|§29.2]] in the standard chart,
>
> $$
> d\pi\big(\partial_x|_{(x,y)}\big)[g] = \partial_x|_{(x,y)}[g \circ \pi] = \partial_x (g \circ \pi)(x,y) = g'(x) = \frac{d}{dx}\Big|_x [g], \qquad
> d\pi\big(\partial_y|_{(x,y)}\big)[g] = \partial_y|_{(x,y)}[g \circ \pi] = \partial_y\, g(x) = 0 ,
> $$
>
> where $d/dx|_x$ is the coordinate derivation of $\mathbb{R}$ at $x$ (Definition [[§32 The Cotangent Space#^def-32-2|§32.2]], with the coordinate written $x$), and $\partial_y\, g(x) = 0$ because $g(x)$ does not depend on $y$. Derivations that agree on every germ are equal, so $d\pi(\partial_x|_{(x,y)}) = d/dx|_x$ and $d\pi(\partial_y|_{(x,y)}) = 0$.
> In matrix form (Theorem [[§30 The Differential in Coordinates#^thm-30-2|§30.2]]), the matrix of $d\pi_{(x,y)}$ is the $1 \times 2$ Jacobian of $\pi$, and it sends the column of components of $\mathbf{X}_{(x,y)} = a\,\partial_x + c\,\partial_y$ to
>
> $$
> \begin{pmatrix} 1 & 0 \end{pmatrix} \begin{pmatrix} a(x, y) \\ c(x, y) \end{pmatrix} = a(x, y) .
> $$
>
> *The condition.* $d\pi_{(x,y)}$ is linear (Proposition [[§28 Derivations and the Abstract Tangent Space#^prop-28-5|§28.5]]), so
>
> $$
> d\pi_{(x,y)}(\mathbf{X}_{(x,y)}) = a(x, y)\, d\pi\big(\partial_x|_{(x,y)}\big) + c(x, y)\, d\pi\big(\partial_y|_{(x,y)}\big) = a(x, y)\, \frac{d}{dx}\Big|_x .
> $$
>
> This equals $\mathbf{Y}_x = b(x)\, \frac{d}{dx}\big|_x$ if and only if $\big(a(x,y) - b(x)\big)\, \frac{d}{dx}\big|_x = 0$, that is, if and only if $a(x, y) = b(x)$, because $d/dx|_x \ne 0$ (it is a basis of $T_x\mathbb{R}$, Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]]). So the fields $\pi$-related to $\mathbf{Y}$ are those with $a(x, y) = b(x)$ for all $(x, y)$, and $c$ is not constrained. Conversely, for every $c \in C^\infty(\mathbb{R}^2)$ the section $b(x)\,\partial_x + c\,\partial_y$ has smooth coefficients ($(x, y) \mapsto b(x)$ is $b \circ \pi$), so it is a vector field (Proposition [[§56 Vector Fields#^prop-56-1|§56.1]]), and by the computation it is $\pi$-related to $\mathbf{Y}$.

^pf-ex-59-1

*Uses:* [[§59 Related Vector Fields#^def-59-2|Def. §59.2]], [[§28 Derivations and the Abstract Tangent Space#^def-28-6|Def. §28.6]], [[§56 Vector Fields#^prop-56-1|§56.1]], [[§29 Coordinate Derivations and the Basis Theorem#^def-29-2|Def. §29.2]], [[§32 The Cotangent Space#^def-32-2|Def. §32.2]], [[§28 Derivations and the Abstract Tangent Space#^prop-28-5|§28.5]], [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]]

“All I care about is the horizontal component … they all should be the same” along each vertical line, the fibre $\pi^{-1}(x)$, “corresponding to the value down here.”

![[m591-49-3.svg]]
*Fields on $\mathbb{R}^2$ that are $\pi$-related to $\mathbf{Y} = b(x)\,\frac{d}{dx}$: along each fibre $\pi^{-1}(x)$ (dashed) the horizontal part (dotted) is $b(x)$, and the vertical part is arbitrary.*

![[m591-49-a1.gif|460]]

*(Not from lecture; animation added, vault only.)* Five integral curves of a field $\pi$-related to $\mathbf{Y} = b(x)\,\frac{d}{dx}$, with $b = 0.6 + 0.4\sin 1.5x$ and $c = \sin(2y + x) + 0.4$ (chosen for the picture), all starting at $x = 0.3$. Whatever the vertical parts do, their $x$-coordinates stay equal and move exactly as the integral curve of $\mathbf{Y}$ on the base (red): $\pi$ carries integral curves of $\mathbf{X}$ to integral curves of $\mathbf{Y}$ (a standard consequence of relatedness, not stated in the notes).

*The operator viewpoint.* The definition is geometric — “arrows”. There is an equivalent characterization in terms of operators, using the pullback of functions, $F^{\ast}g = g \circ F$.

> [!theorem] Proposition §59.1: Related Fields as Operators
> Let $F : M \to N$ be [[§19 Smooth Functions and Smooth Maps#^def-19-3|smooth]], $\mathbf{X} \in \mathfrak{X}(M)$ and $\mathbf{Y} \in \mathfrak{X}(N)$. Then $\mathbf{X}$ and $\mathbf{Y}$ are [[§59 Related Vector Fields#^def-59-2|F-related]] if and only if
>
> $$
> \mathbf{X}(g \circ F) = (\mathbf{Y}g) \circ F \qquad \text{for every } g \in C^\infty(N),
> $$
>
> that is, $\mathbf{X} \circ F^{\ast} = F^{\ast} \circ \mathbf{Y}$: the pullback $F^{\ast}$ intertwines $\mathbf{X}$ and $\mathbf{Y}$ as [[§56 Vector Fields#^def-56-5|derivations]].
>
> *Lee: Proposition 8.16*

^prop-59-1

![[m591-49-4.svg]]
*The pullback $F^{\ast}$ intertwines the two fields as operators: the square commutes exactly when $\mathbf{X}$ and $\mathbf{Y}$ are $F$-related.*

> [!proof]+ Proof
> *(Lecture 17, “let's have a peek at the proof”; the step for the converse is filled in.)* The two forms of the condition are the same, since $(\mathbf{X} \circ F^{\ast})(g) = \mathbf{X}(g \circ F)$ and $(F^{\ast} \circ \mathbf{Y})(g) = (\mathbf{Y}g) \circ F$; and both sides are functions on $M$, so the condition says that they agree at every $p \in M$, for every $g$. Let $g \in C^\infty(N)$ and $p \in M$. The value at $p$ of a field applied to a function is the tangent vector at $p$ applied to its germ (Lemma [[§56 Vector Fields#^lem-56-3|§56.3]]). With this, and the definition of the pushforward (Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-6|§28.6]]) for $D = \mathbf{X}_p$ — “we pull back germs, so we push forward derivations” —
>
> $$
> \mathbf{X}(g \circ F)(p) = \mathbf{X}_p[g \circ F] = dF_p(\mathbf{X}_p)[g],
> \qquad
> \big((\mathbf{Y}g) \circ F\big)(p) = (\mathbf{Y}g)\big(F(p)\big) = \mathbf{Y}_{F(p)}[g] .
> $$
>
> *Related implies intertwining.* If the fields are $F$-related, then $dF_p(\mathbf{X}_p) = \mathbf{Y}_{F(p)}$ (Definition [[§59 Related Vector Fields#^def-59-2|§59.2]]), so the right-hand sides agree, for every $g$ and $p$; that is, $\mathbf{X}(g \circ F) = (\mathbf{Y}g) \circ F$.
>
> *Intertwining implies related.* Conversely, suppose $\mathbf{X}(g \circ F) = (\mathbf{Y}g) \circ F$ for every $g \in C^\infty(N)$, and fix $p \in M$. By the display, the two derivations $dF_p(\mathbf{X}_p)$ and $\mathbf{Y}_{F(p)}$ at $F(p)$ agree on every global function $g$. Every germ $[h]$ at $F(p)$ has a global representative $g \in C^\infty(N)$, $[g] = [h]$ (Corollary [[§56 Vector Fields#^cor-56-5|§56.5]]), so
>
> $$
> dF_p(\mathbf{X}_p)[h] = dF_p(\mathbf{X}_p)[g] = \mathbf{Y}_{F(p)}[g] = \mathbf{Y}_{F(p)}[h] .
> $$
>
> So the two derivations agree on every germ, and are equal as maps on $C^\infty_{F(p)}(N)$: $dF_p(\mathbf{X}_p) = \mathbf{Y}_{F(p)}$. As $p$ was arbitrary, the fields are $F$-related. “It's a trivial if and only if once you realize” this.

^pf-59-1

*Uses:* [[§59 Related Vector Fields#^def-59-2|Def. §59.2]], [[§28 Derivations and the Abstract Tangent Space#^def-28-6|Def. §28.6]], [[§28 Derivations and the Abstract Tangent Space#^def-28-1|Def. §28.1]], [[§56 Vector Fields#^cor-56-5|§56.5]], [[§56 Vector Fields#^lem-56-3|§56.3]]

> [!theorem] Proposition §59.2: Pushforward by a Diffeomorphism
> Let $F : M \to N$ be a [[§19 Smooth Functions and Smooth Maps#^def-19-4|diffeomorphism]] and $\mathbf{X} \in \mathfrak{X}(M)$. Then the [[§59 Related Vector Fields#^def-59-1|pushforward]] $F_{\ast}\mathbf{X}$ is smooth, it is the unique vector field on $N$ that is [[§59 Related Vector Fields#^def-59-2|F-related]] to $\mathbf{X}$, and for every $g \in C^\infty(N)$
>
> $$
> (F_{\ast}\mathbf{X})\, g = \big(\mathbf{X}(g \circ F)\big) \circ F^{-1} .
> $$
>
> *Lee: Proposition 8.19, Corollary 8.21*

^prop-59-2

> [!proof]+ Proof
> *(Not from lecture; filled in.)* Four things are claimed: the formula, smoothness, $F$-relatedness, and uniqueness. Here $(F_\ast\mathbf{X})\,g$ denotes the function $q \mapsto (F_\ast\mathbf{X})_q[g]$ on $N$, as in Lemma [[§56 Vector Fields#^lem-56-8|§56.8]].
>
> *The formula.* For $q \in N$ put $p = F^{-1}(q)$. By Definition [[§59 Related Vector Fields#^def-59-1|§59.1]], then Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-6|§28.6]] with $D = \mathbf{X}_p$, then Lemma [[§56 Vector Fields#^lem-56-3|§56.3]],
>
> $$
> (F_\ast\mathbf{X})_q[g] = dF_p(\mathbf{X}_p)[g] = \mathbf{X}_p[g \circ F] = \mathbf{X}(g \circ F)(p) = \big(\mathbf{X}(g \circ F) \circ F^{-1}\big)(q) ,
> $$
>
> which is the formula.
>
> *Smoothness.* At each $q$, $(F_\ast\mathbf{X})_q = dF_p(\mathbf{X}_p)$ lies in $T_{F(p)}N = T_qN$, so $F_\ast\mathbf{X}$ is a section of $TN$. In the formula, $g \circ F \in C^\infty(M)$ (Lemma [[§19 Smooth Functions and Smooth Maps#^lem-19-5|§19.5]]), so $\mathbf{X}(g \circ F)$ is smooth (Lemma [[§56 Vector Fields#^lem-56-3|§56.3]]); and $F^{-1}$ is smooth because $F$ is a diffeomorphism (Definition [[§19 Smooth Functions and Smooth Maps#^def-19-4|§19.4]]), so the composite $\mathbf{X}(g \circ F) \circ F^{-1}$ is smooth (Lemma [[§19 Smooth Functions and Smooth Maps#^lem-19-5|§19.5]]). This holds for every $g \in C^\infty(N)$, so $F_\ast\mathbf{X}$ is smooth by Lemma [[§56 Vector Fields#^lem-56-8|§56.8]].
>
> *$F$-related.* For $p \in M$, $F^{-1}(F(p)) = p$, so Definition [[§59 Related Vector Fields#^def-59-1|§59.1]] at $q = F(p)$ reads $(F_\ast\mathbf{X})_{F(p)} = dF_p(\mathbf{X}_p)$. This is Definition [[§59 Related Vector Fields#^def-59-2|§59.2]] with $\mathbf{Y} = F_\ast\mathbf{X}$.
>
> *Uniqueness.* If $\mathbf{Y} \in \mathfrak{X}(N)$ is also $F$-related to $\mathbf{X}$, let $q \in N$. Since $F$ is onto, $q = F(p)$ with $p = F^{-1}(q)$, and by Definition [[§59 Related Vector Fields#^def-59-2|§59.2]] and then Definition [[§59 Related Vector Fields#^def-59-1|§59.1]],
>
> $$
> \mathbf{Y}_q = \mathbf{Y}_{F(p)} = dF_p(\mathbf{X}_p) = (F_\ast\mathbf{X})_q .
> $$
>
> This holds for every $q$, so $\mathbf{Y} = F_\ast\mathbf{X}$.

^pf-59-2

*Uses:* [[§59 Related Vector Fields#^def-59-1|Def. §59.1]], [[§59 Related Vector Fields#^def-59-2|Def. §59.2]], [[§28 Derivations and the Abstract Tangent Space#^def-28-6|Def. §28.6]], [[§19 Smooth Functions and Smooth Maps#^def-19-4|Def. §19.4]], [[§56 Vector Fields#^lem-56-3|§56.3]], [[§19 Smooth Functions and Smooth Maps#^lem-19-5|§19.5]], [[§56 Vector Fields#^lem-56-8|§56.8]]

*“Now the reason I wanted to do it this way”* — through operators — is the following proposition.

> [!theorem] Proposition §59.3: Naturality of the Bracket
> Let $F : M \to N$ be [[§19 Smooth Functions and Smooth Maps#^def-19-3|smooth]], $\mathbf{X}_1, \mathbf{X}_2 \in \mathfrak{X}(M)$ and $\mathbf{Y}_1, \mathbf{Y}_2 \in \mathfrak{X}(N)$. If $\mathbf{X}_i$ is [[§59 Related Vector Fields#^def-59-2|F-related]] to $\mathbf{Y}_i$ for $i = 1, 2$, then the [[§58 Lie Bracket and Lie Algebra#^def-58-1|bracket]] $[\mathbf{X}_1, \mathbf{X}_2]$ is $F$-related to $[\mathbf{Y}_1, \mathbf{Y}_2]$.
>
> *Lee: Proposition 8.30*

^prop-59-3

> [!proof]+ Proof
> *(Omitted in Lecture 17 as an exercise: “it's just a matter of chasing the definitions … being $F$-related means that $F^{\ast}$ commutes with the derivations. So you just play with the symbols; it all comes out.” Filled in.)* The brackets $[\mathbf{X}_1, \mathbf{X}_2] \in \mathfrak{X}(M)$ and $[\mathbf{Y}_1, \mathbf{Y}_2] \in \mathfrak{X}(N)$ are vector fields (Lemma [[§58 Lie Bracket and Lie Algebra#^lem-58-1|§58.1]]). By Proposition [[§59 Related Vector Fields#^prop-59-1|§59.1]], it suffices to show
>
> $$
> [\mathbf{X}_1, \mathbf{X}_2](g \circ F) = \big([\mathbf{Y}_1, \mathbf{Y}_2]\, g\big) \circ F \qquad \text{for every } g \in C^\infty(N).
> $$
>
> Let $g \in C^\infty(N)$. The same proposition, applied to the pairs $(\mathbf{X}_i, \mathbf{Y}_i)$, gives $\mathbf{X}_i(h \circ F) = (\mathbf{Y}_i h) \circ F$ for every $h \in C^\infty(N)$ and $i = 1, 2$.
>
> *The composite $\mathbf{X}_1\mathbf{X}_2$.* Apply this first for $i = 2$ with $h = g$, and then for $i = 1$ with $h = \mathbf{Y}_2 g$, which lies in $C^\infty(N)$ by Lemma [[§56 Vector Fields#^lem-56-3|§56.3]]:
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
> *Subtracting.* By Definition [[§58 Lie Bracket and Lie Algebra#^def-58-1|§58.1]], and since $u \circ F - v \circ F = (u - v) \circ F$ for functions $u, v$ on $N$,
>
> $$
> [\mathbf{X}_1, \mathbf{X}_2](g \circ F) = (\mathbf{Y}_1\mathbf{Y}_2 g) \circ F - (\mathbf{Y}_2\mathbf{Y}_1 g) \circ F = \big(\mathbf{Y}_1\mathbf{Y}_2 g - \mathbf{Y}_2\mathbf{Y}_1 g\big) \circ F = \big([\mathbf{Y}_1, \mathbf{Y}_2]\, g\big) \circ F ,
> $$
>
> and Proposition [[§59 Related Vector Fields#^prop-59-1|§59.1]] again, with $\mathbf{X} = [\mathbf{X}_1, \mathbf{X}_2]$ and $\mathbf{Y} = [\mathbf{Y}_1, \mathbf{Y}_2]$, gives the claim.

^pf-59-3

*Uses:* [[§59 Related Vector Fields#^prop-59-1|§59.1]], [[§58 Lie Bracket and Lie Algebra#^def-58-1|Def. §58.1]], [[§58 Lie Bracket and Lie Algebra#^lem-58-1|§58.1]], [[§56 Vector Fields#^lem-56-3|§56.3]]

On omitting this proof: “In a class like this, you cannot prove everything. First of all, there is no time, and second, you would be bored to tears. … But on the other hand, if we just say, oh, you can read the proof, then you don't get a feeling for the subject. So there is a line there somewhere, or a zone, where you have to prove enough, but not too much.” Feedback on where that line should sit is “always welcome.”

> [!theorem] Corollary §59.4: Diffeomorphisms Preserve Brackets
> If $F : M \to N$ is a [[§19 Smooth Functions and Smooth Maps#^def-19-4|diffeomorphism]] and $\mathbf{X}_1, \mathbf{X}_2 \in \mathfrak{X}(M)$, then $F_{\ast}[\mathbf{X}_1, \mathbf{X}_2] = [F_{\ast}\mathbf{X}_1, F_{\ast}\mathbf{X}_2]$.
>
> *Lee: Corollary 8.31*

^cor-59-4

> [!proof]+ Proof
> *(Not from lecture; filled in.)* By Proposition [[§59 Related Vector Fields#^prop-59-2|§59.2]], each $F_\ast\mathbf{X}_i$ is a vector field on $N$ and $\mathbf{X}_i$ is $F$-related to $F_\ast\mathbf{X}_i$, for $i = 1, 2$. So Proposition [[§59 Related Vector Fields#^prop-59-3|§59.3]], with $\mathbf{Y}_i = F_\ast\mathbf{X}_i$, shows that $[\mathbf{X}_1, \mathbf{X}_2]$ is $F$-related to $[F_\ast\mathbf{X}_1, F_\ast\mathbf{X}_2]$. On the other hand $[\mathbf{X}_1, \mathbf{X}_2] \in \mathfrak{X}(M)$ (Lemma [[§58 Lie Bracket and Lie Algebra#^lem-58-1|§58.1]]), so Proposition [[§59 Related Vector Fields#^prop-59-2|§59.2]], applied to this field, says that the only field on $N$ that is $F$-related to $[\mathbf{X}_1, \mathbf{X}_2]$ is $F_\ast[\mathbf{X}_1, \mathbf{X}_2]$. Both $[F_\ast\mathbf{X}_1, F_\ast\mathbf{X}_2]$ and $F_\ast[\mathbf{X}_1, \mathbf{X}_2]$ are such fields, so they are equal.

^pf-59-4

*Uses:* [[§59 Related Vector Fields#^prop-59-3|§59.3]], [[§59 Related Vector Fields#^prop-59-2|§59.2]], [[§59 Related Vector Fields#^def-59-1|Def. §59.1]], [[§59 Related Vector Fields#^def-59-2|Def. §59.2]], [[§58 Lie Bracket and Lie Algebra#^lem-58-1|§58.1]]

*(Not from lecture; the conversion diagram of the midterm check sheet, added on request.)* A vector field $\mathbf{X}$ on $M$, pointwise, globally and in components. Chart $(U, \varphi = (x^1, \ldots, x^m))$; the numbers on the arrows refer to the remark below.

![[m591-56-4.svg]]

> [!remark] Remark: Conversion Diagram for Vector Fields
> 1. *Section to operator.* $(\mathbf{X}f)(p) = \mathbf{X}_p[f]$, a derivation of $C^\infty(M)$: $\mathbf{X}(fg) = f\,\mathbf{X}g + g\,\mathbf{X}f$ (Lemma [[§56 Vector Fields#^lem-56-3|§56.3]]); $\mathbf{X}f$ is smooth for every smooth $f$ exactly when $\mathbf{X}$ is smooth (Lemma [[§56 Vector Fields#^lem-56-8|§56.8]]).
> 2. *Operator to section.* Every derivation of $C^\infty(M)$ is a vector field: $\mathbf{X}_p[f] = (\mathbf{X}\tilde f)(p)$ for a global $\tilde f$ with the same germ at $p$, which exists by bump functions and does not depend on the choice (Corollary [[§56 Vector Fields#^cor-56-5|§56.5]], Lemma [[§56 Vector Fields#^lem-56-6|§56.6]], Proposition [[§56 Vector Fields#^prop-56-7|§56.7]]).
> 3. *Section to components.* On $U$, $X^j = \mathbf{X}(x^j)$, that is, $X^j(p) = \mathbf{X}_p[x^j] = dx^j|_p(\mathbf{X}_p)$.
> 4. *Components to section.* $\mathbf{X}_p = \sum_j X^j(p)\, \partial/\partial x^j|_p$, smooth if and only if all $X^j$ are (Proposition [[§56 Vector Fields#^prop-56-1|§56.1]]); then $\mathbf{X}f = \sum_j X^j\, \partial f/\partial x^j$.
>
> *The same three faces for:*
> - *the bracket.* Globally $[\mathbf{X}, \mathbf{Y}]f = \mathbf{X}(\mathbf{Y}f) - \mathbf{Y}(\mathbf{X}f)$ (Definition [[§58 Lie Bracket and Lie Algebra#^def-58-1|§58.1]]). Pointwise $[\mathbf{X}, \mathbf{Y}]_p[f] = \mathbf{X}_p[\mathbf{Y}f] - \mathbf{Y}_p[\mathbf{X}f]$, which needs the global function $\mathbf{Y}f$, not only the vector $\mathbf{Y}_p$. In components $[\mathbf{X}, \mathbf{Y}]^j = \mathbf{X}(Y^j) - \mathbf{Y}(X^j) = \sum_i \big(X^i\, \partial Y^j/\partial x^i - Y^i\, \partial X^j/\partial x^i\big)$ (Proposition [[§58 Lie Bracket and Lie Algebra#^prop-58-2|§58.2]]).
> - *$F$-related fields.* Pointwise $F_{\ast p}\mathbf{X}_p = \mathbf{Y}_{F(p)}$ (Definition [[§59 Related Vector Fields#^def-59-2|§59.2]]). Globally $\mathbf{X}(g \circ F) = (\mathbf{Y}g) \circ F$ for all $g$ (Proposition [[§59 Related Vector Fields#^prop-59-1|§59.1]]). In components $Y^i(F(p)) = \sum_j \frac{\partial F^i}{\partial x^j}(p)\, X^j(p)$. For a diffeomorphism, $\mathbf{Y} = F_\ast\mathbf{X}$ with $(F_\ast\mathbf{X})_q = F_{\ast}\mathbf{X}_{F^{-1}(q)}$ (Definition [[§59 Related Vector Fields#^def-59-1|§59.1]]).
> - *one-forms.* Pointwise $\theta_p \in T_p^{\ast}M$; globally the function $p \mapsto \theta_p(\mathbf{X}_p)$ for each vector field $\mathbf{X}$; in components $\theta_j = \theta(\partial/\partial x^j)$ and $\theta = \sum_j \theta_j\, dx^j$ (Proposition [[§53 One-Forms#^prop-53-1|§53.1]]). For $\theta = df$, $df(\mathbf{X}) = \mathbf{X}f$.
> - *the tangent bundle.* The section $\mathbf{X}$ in the standard chart of $TM$ ([[§51 The Tangent Bundle|§51]]) is $p \mapsto (x^1, \ldots, x^m, X^1, \ldots, X^m)$, with transition $(r, v) \mapsto (\tau(r), \tau'(r)v)$, $\tau$ the transition function of the base.

^rem-59-3

*Lecture 21 opened with the last problem of the midterm — “there's always a question that is hard, but it's okay … I hope we're still friends.”*

> [!definition] Definition §59.3: Vector Field Tangent to a Submanifold
> Let $S \subseteq M$ be a regular submanifold, $\iota : S \hookrightarrow M$ the inclusion, and $\mathbf{X} \in \mathfrak{X}(M)$. Then $\mathbf{X}$ is **tangent to $S$** if
>
> $$
> \mathbf{X}_p \in \iota_{\ast p}(T_pS) \qquad \text{for every } p \in S .
> $$
>
> Identifying $T_pS$ with the subspace $\iota_{\ast p}(T_pS) \subseteq T_pM$ (Proposition [[§37 Regular Submanifolds#^prop-37-6|§37.6]]), this reads $\mathbf{X}_p \in T_pS$ for every $p \in S$. Nothing is required at points of $M \setminus S$.
>
> *Lee: Ch. 8, Vector Fields on Submanifolds*

^def-59-3

> [!theorem] Lemma §59.5: Tangency in an Adapted Chart
> Let $S \subseteq M$ be a regular submanifold of dimension $k$, and $(U, (x, y)) = (U, (x^1, \ldots, x^k, y^1, \ldots, y^{m-k}))$ an adapted chart with $S \cap U = \{ y = 0 \}$ (Definition [[§37 Regular Submanifolds#^def-37-3|§37.3]]). Let $\mathbf{X} \in \mathfrak{X}(M)$ be written on $U$ as
>
> $$
> \mathbf{X} = \sum_{i=1}^k f^i\, \frac{\partial}{\partial x^i} + \sum_{a=1}^{m-k} g^a\, \frac{\partial}{\partial y^a}
> $$
>
> (Proposition [[§56 Vector Fields#^prop-56-1|§56.1]]). Then $\mathbf{X}_p \in T_pS$ for every $p \in S \cap U$ if and only if $g^a(x, 0) = 0$ for every $a$ and every point $(x, 0)$ of $S \cap U$: along $S$, “there is no $y$ component.”

^lem-59-5

> [!proof]+ Proof
> *(Not from lecture; the step the proof of Proposition [[§59 Related Vector Fields#^prop-59-6|§59.6]] uses, written out.)* Let $p \in S \cap U$. By Proposition [[§37 Regular Submanifolds#^prop-37-6|§37.6]], applied to the adapted chart with the coordinates along $S$ listed first, $\iota_{\ast p}(T_pS) = \operatorname{Span}\{ \partial/\partial x^1|_p, \ldots, \partial/\partial x^k|_p \}$. The $m$ vectors $\partial/\partial x^i|_p$, $\partial/\partial y^a|_p$ form a basis of $T_pM$ (Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]]), and
>
> $$
> \mathbf{X}_p = \sum_i f^i(p)\, \frac{\partial}{\partial x^i}\Big|_p + \sum_a g^a(p)\, \frac{\partial}{\partial y^a}\Big|_p .
> $$
>
> Since coefficients in a basis are unique, $\mathbf{X}_p$ lies in the span of the $\partial/\partial x^i|_p$ exactly when every $g^a(p) = 0$. The points of $S \cap U$ are those with $y = 0$, so the condition for all $p \in S \cap U$ is $g^a(x, 0) = 0$ for all $a$.

^pf-59-5

*Uses:* [[§37 Regular Submanifolds#^prop-37-6|§37.6]], [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]]

> [!theorem] Proposition §59.6: Brackets of Fields Tangent to a Submanifold
> Let $S \subseteq M$ be a regular submanifold and $\mathbf{X}, \mathbf{Y} \in \mathfrak{X}(M)$ tangent to $S$ (Definition [[§59 Related Vector Fields#^def-59-3|§59.3]]). Then $[\mathbf{X}, \mathbf{Y}]$ is also tangent to $S$.
>
> *Lee: Corollary 8.32*

^prop-59-6

> [!proof]+ Proof
> *(Lecture 21, “not in excruciating detail”; the bookkeeping is filled in.)* “Use adapted coordinates”: near $p \in S$ take a slice chart $(x, y) = (x^1, \ldots, x^k, y^1, \ldots, y^{m-k})$ with $S = \{ y = 0 \}$ (Definition [[§37 Regular Submanifolds#^def-37-2|§37.2]]); on the exam, $M$ was two-dimensional, “but they could be vector-valued … the codimension or the dimension doesn't matter.” Write
>
> $$
> \mathbf{X} = \sum_i f^i\, \frac{\partial}{\partial x^i} + \sum_a g^a\, \frac{\partial}{\partial y^a}, \qquad
> \mathbf{Y} = \sum_i u^i\, \frac{\partial}{\partial x^i} + \sum_a v^a\, \frac{\partial}{\partial y^a} .
> $$
>
> By Lemma [[§59 Related Vector Fields#^lem-59-5|§59.5]], tangency says $g^a(x, 0) = 0$ and $v^a(x, 0) = 0$: “there is no $y$ component.” We show the $\partial/\partial y^b$ components of $[\mathbf{X}, \mathbf{Y}]$ have the same property. By Proposition [[§58 Lie Bracket and Lie Algebra#^prop-58-2|§58.2]], that component is
>
> $$
> \mathbf{X}(v^b) - \mathbf{Y}(g^b) = \sum_i f^i\, \frac{\partial v^b}{\partial x^i} + \sum_a g^a\, \frac{\partial v^b}{\partial y^a} - \sum_i u^i\, \frac{\partial g^b}{\partial x^i} - \sum_a v^a\, \frac{\partial g^b}{\partial y^a} .
> $$
>
> Evaluate at $y = 0$. The terms with $\partial/\partial x^i$ vanish for one reason: “how do you evaluate the partial with respect to $x$ at $y = 0$? You fix $y$ to zero and differentiate with respect to $x$, but when I set $y$ to zero, I get zero” — $\frac{\partial v^b}{\partial x^i}(x, 0) = \frac{\partial}{\partial x^i}\big(v^b(x, 0)\big) = 0$, and likewise for $g^b$. The terms with $\partial/\partial y^a$ vanish “for a different reason”: “I don't know that these partials are zero, but these guys are” — the coefficients $g^a(x, 0)$ and $v^a(x, 0)$. So the $y$-components of $[\mathbf{X}, \mathbf{Y}]$ vanish on $S$, and $[\mathbf{X}, \mathbf{Y}]_p \in T_pS$ for $p \in S$.

^pf-59-6

*Uses:* [[§37 Regular Submanifolds#^def-37-2|Def. §37.2]], [[§58 Lie Bracket and Lie Algebra#^prop-58-2|§58.2]], [[§59 Related Vector Fields#^lem-59-5|§59.5]]

![[m591-56-5.svg]]

**Comparison with Lee.** Lee proves this (Corollary 8.32) with related fields: on $S$, $\mathbf{X}$ and $\mathbf{Y}$ restrict to fields $\iota$-related to them, and the naturality of the bracket (Proposition [[§59 Related Vector Fields#^prop-59-3|§59.3]]) applied to the inclusion $\iota : S \to M$ does the rest. The coordinate proof above is the one given in class.

**Transcription note (Lecture 21).** Page 55 of the handwritten notes records the $\partial_y$ component of $[f\partial_x, v\partial_y]$ as $\partial v/\partial x|_{y = 0}$; it is $f\, \partial v/\partial x|_{y = 0}$, which vanishes for the same reason.
