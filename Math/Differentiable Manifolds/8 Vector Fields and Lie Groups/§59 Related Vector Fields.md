---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 8
section: 59
tags: [differentiable-manifolds, math591]
---
← [[§58 Lie Bracket and Lie Algebra]] · ↑ [[· 8 Vector Fields and Lie Groups]] · [[§60 Lie Groups and Left-Invariant Vector Fields]] →

*Stage: fields — Vector fields cannot be pushed forward along an arbitrary smooth map, but two fields can be related by one; related fields have related brackets, and a diffeomorphism carries fields and brackets across.*

*Lecture 17. Back to vector fields, still from the operator point of view; vector fields as generators of dynamics come later. Recap: every [[§56 Vector Fields#^def-56-1|vector field]] defines a [[§56 Vector Fields#^def-56-7|derivation]] of $C^\infty(M)$, and conversely (Lemma [[§56 Vector Fields#^lem-56-4|§56.4]], Proposition [[§56 Vector Fields#^prop-56-10|§56.10]]); so the [[§58 Lie Bracket and Lie Algebra#^def-58-1|commutator]] of two fields is again a field (Lemma [[§58 Lie Bracket and Lie Algebra#^lem-58-1|§58.1]]). Officially, a vector field is a smooth section of the tangent bundle (Definition [[§56 Vector Fields#^def-56-1|§56.1]]).*

> [!remark] Remark: Vector Fields Do Not Push Forward
> Given a [[§19 Smooth Functions and Smooth Maps#^def-19-3|smooth map]] $F : M \to N$, in general vector fields can be neither pushed forward nor pulled back: vector fields have no functorial properties, as opposed to [[§53 One-Forms#^def-53-1|differential forms]], which can always be [[§53 One-Forms#^def-53-8|pulled back]]. Single tangent vectors *can* be [[§28 Derivations and the Abstract Tangent Space#^def-28-6|pushed forward]], by $dF_p$; the trouble is assembling the results into a field on $N$.
> - If $F$ is not injective, two points $p_1 \ne p_2$ with $F(p_1) = F(p_2) = q$ give two candidates $dF_{p_1}(\mathbf{X}_{p_1})$ and $dF_{p_2}(\mathbf{X}_{p_2})$ at $q$, in general different, so the would-be pushforward is multi-valued.
> - If $F$ is not surjective, a point $q' \notin F(M)$ gets no candidate at all, so nothing defines the field outside the image.

^rem-59-1

![[m591-49-2.svg]]
*Why a vector field cannot be pushed forward along an arbitrary smooth map $F$: two points $p_1 \ne p_2$ with $F(p_1) = F(p_2) = q$ give two candidates at $q$, and a point $q' \notin F(M)$ gets none.*

The exception is a [[§19 Smooth Functions and Smooth Maps#^def-19-4|diffeomorphism]], where each $q \in N$ is $F(p)$ for exactly one $p$.

> [!remark] Remark: Notation: $dF_p$
> *Lecture 17* switches to the more common notation $dF$, which replaces $F_\ast$. From here on the [[§28 Derivations and the Abstract Tangent Space#^def-28-6|pushforward]] of Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-6|§28.6]] is written
>
> $$
> dF_p = F_{\ast p} : T_pM \to T_{F(p)}N ,
> $$
>
> as in Lee. It agrees with the [[§22 The Differential of a Map Between Vector Spaces#^def-22-5|differential of a map between vector spaces]] (Definition [[§22 The Differential of a Map Between Vector Spaces#^def-22-5|§22.5]]) under the identification $v \leftrightarrow D_v|_a$ of Corollary [[§30 The Differential in Coordinates#^cor-30-6|§30.6]] (the remark in [[§30 The Differential in Coordinates|§30]]), so the two uses of $dF_p$ do not clash. Earlier sections keep $F_{\ast p}$. Both notations are used below, with the same meaning: $\iota_{\ast p} = d\iota_p$, $(L_g)_{\ast h} = d(L_g)_h$ and $F_{\ast p} = dF_p$.

^rem-59-2

> [!definition] Definition §59.1: Pushforward of a Vector Field by a Diffeomorphism
> Let $F : M \to N$ be a [[§19 Smooth Functions and Smooth Maps#^def-19-4|diffeomorphism]] and $\mathbf{X} \in \mathfrak{X}(M)$. The **pushforward** of $\mathbf{X}$ is the rough section $F_{\ast}\mathbf{X}$ of $TN$ (Definition [[§45 Fibrations#^def-45-5|§45.5]]) given by
>
> $$
> (F_{\ast}\mathbf{X})_q = dF_{F^{-1}(q)}\big(\mathbf{X}_{F^{-1}(q)}\big), \qquad q \in N .
> $$
>
> *Lee: Ch. 8, Pushforwards of Vector Fields*

^def-59-1

![[m591-49-a2.gif|440]]

*(Not from lecture; animation added, vault only.)* A diffeomorphism $F_s$ (a family chosen for the picture) bends the plane, grid and all, while $\mathbf{X} = \partial_x$ is carried along. The arrow at $F_s(p)$ is $d(F_s)_p(\mathbf{X}_p)$: it rides to the new point and turns and stretches with the grid. The result is $(F_s)_\ast\mathbf{X}$.

It is smooth, so $F_{\ast}\mathbf{X} \in \mathfrak{X}(N)$: this is [[§59 Related Vector Fields#^prop-59-2|Proposition §59.2]] below. For a general $F$, however, a field on $M$ and a field on $N$ can still be related by $F$, corresponding to one another: relatedness is not a construction but something that may happen.

> [!definition] Definition §59.2: $F$-Related Vector Fields
> Let $F : M \to N$ be [[§19 Smooth Functions and Smooth Maps#^def-19-3|smooth]], $\mathbf{X} \in \mathfrak{X}(M)$ and $\mathbf{Y} \in \mathfrak{X}(N)$. Then $\mathbf{X}$ and $\mathbf{Y}$ are **$F$-related** if
>
> $$
> dF_p(\mathbf{X}_p) = \mathbf{Y}_{F(p)} \in T_{F(p)}N \qquad \text{for every } p \in M .
> $$
>
> *Lee: Ch. 8, Vector Fields and Smooth Maps*

^def-59-2

![[m591-49-a3.gif|420]]

*(Not from lecture; animation added, vault only.)* $F : \mathbb{R} \to S^1$, $F(t) = e^{it}$, with $\mathbb{R}$ drawn as a helix over the circle. The field $\mathbf{X} = \frac{d}{dt}$ (blue arrows along the helix) and $\mathbf{Y} = \partial_\theta$ (red) are $F$-related: $dF_t(\mathbf{X}_t) = \mathbf{Y}_{F(t)}$ at every $t$. The definition needs only that, not injectivity: both turns of the helix over a point give the same red arrow.

In words: push the value of $\mathbf{X}$ at $p$ forward; if every time this gives the value of $\mathbf{Y}$ at the image point $F(p)$, the two vector fields are related by $F$. No injectivity or surjectivity is assumed. Points outside $F(M)$ impose nothing on $\mathbf{Y}$, and two points with the same image must push forward to the same vector.
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
> Let $\pi : \mathbb{R}^2 \to \mathbb{R}$, $\pi(x, y) = x$, and $\mathbf{Y} = b(x)\, \dfrac{d}{dx}$ with $b \in C^\infty(\mathbb{R})$ — every vector field on $\mathbb{R}$ can be written like this. The fields on $\mathbb{R}^2$ that are [[§59 Related Vector Fields#^def-59-2|π-related]] to $\mathbf{Y}$ are exactly
>
> $$
> \mathbf{X} = b(x)\, \frac{\partial}{\partial x} + c(x, y)\, \frac{\partial}{\partial y}, \qquad c \in C^\infty(\mathbb{R}^2) \text{ arbitrary.}
> $$

^ex-59-1

> [!proof]+ Proof
> *(Lecture 17, as a question to the class: which components can a $\pi$-related field have? The first component is forced to be $b(x)$; the second is arbitrary. The computation is filled in.)* By Proposition [[§56 Vector Fields#^prop-56-1|§56.1]] in the standard chart of $\mathbb{R}^2$, every vector field on $\mathbb{R}^2$ can be written $\mathbf{X} = a\, \partial_x + c\, \partial_y$ with $a, c \in C^\infty(\mathbb{R}^2)$. Since $\pi(x, y) = x$, Definition [[§59 Related Vector Fields#^def-59-2|§59.2]] says that $\mathbf{X}$ is $\pi$-related to $\mathbf{Y}$ if and only if $d\pi_{(x,y)}(\mathbf{X}_{(x,y)}) = \mathbf{Y}_x$ for every $(x, y)$. So compute the left side.
>
> *The pushforwards of the coordinate vectors.* Let $[g]$ be a germ at $x$ on $\mathbb{R}$. The function $g \circ \pi$ is $(x', y') \mapsto g(x')$. By Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-6|§28.6]] and then Definition [[§29 Coordinate Derivations and the Basis Theorem#^def-29-3|§29.3]] in the standard chart,
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
> This equals $\mathbf{Y}_x = b(x)\, \frac{d}{dx}\big|_x$ if and only if $\big(a(x,y) - b(x)\big)\, \frac{d}{dx}\big|_x = 0$, that is, if and only if $a(x, y) = b(x)$, because $d/dx|_x \ne 0$ (it is a basis of $T_x\mathbb{R}$, Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-8|§29.8]]). So the fields $\pi$-related to $\mathbf{Y}$ are those with $a(x, y) = b(x)$ for all $(x, y)$, and $c$ is not constrained. Conversely, for every $c \in C^\infty(\mathbb{R}^2)$ the rough section $b(x)\,\partial_x + c\,\partial_y$ of $T\mathbb{R}^2$ has smooth coefficients ($(x, y) \mapsto b(x)$ is $b \circ \pi$), so it is a vector field (Proposition [[§56 Vector Fields#^prop-56-1|§56.1]]), and by the computation it is $\pi$-related to $\mathbf{Y}$.

^pf-ex-59-1

*Uses:* [[§59 Related Vector Fields#^def-59-2|Def. §59.2]], [[§28 Derivations and the Abstract Tangent Space#^def-28-6|Def. §28.6]], [[§56 Vector Fields#^prop-56-1|§56.1]], [[§29 Coordinate Derivations and the Basis Theorem#^def-29-3|Def. §29.3]], [[§32 The Cotangent Space#^def-32-2|Def. §32.2]], [[§28 Derivations and the Abstract Tangent Space#^prop-28-5|§28.5]], [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-8|§29.8]]

Only the horizontal component matters, and it must be the same along each vertical line, the fibre $\pi^{-1}(x)$, equal to the value of $\mathbf{Y}$ at $x$ below.

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
> that is, $\mathbf{X} \circ F^{\ast} = F^{\ast} \circ \mathbf{Y}$: the pullback $F^{\ast}$ intertwines $\mathbf{X}$ and $\mathbf{Y}$ as [[§56 Vector Fields#^def-56-7|derivations]].
>
> *Lee: Proposition 8.16*

^prop-59-1

![[m591-49-4.svg]]
*The pullback $F^{\ast}$ intertwines the two fields as operators: the square commutes exactly when $\mathbf{X}$ and $\mathbf{Y}$ are $F$-related.*

> [!proof]+ Proof
> *(Lecture 17, a sketch of the proof; the step for the converse is filled in.)* The two forms of the condition are the same, since $(\mathbf{X} \circ F^{\ast})(g) = \mathbf{X}(g \circ F)$ and $(F^{\ast} \circ \mathbf{Y})(g) = (\mathbf{Y}g) \circ F$; and both sides are functions on $M$, so the condition says that they agree at every $p \in M$, for every $g$. Let $g \in C^\infty(N)$ and $p \in M$. The value at $p$ of a field applied to a function is the tangent vector at $p$ applied to its germ (Definition [[§56 Vector Fields#^def-56-8|§56.8]]). With this, and the definition of the pushforward (Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-6|§28.6]]) for $D = \mathbf{X}_p$ — germs pull back, so derivations push forward —
>
> $$
> \mathbf{X}(g \circ F)(p) = \mathbf{X}_p[g \circ F] = dF_p(\mathbf{X}_p)[g],
> \qquad
> \big((\mathbf{Y}g) \circ F\big)(p) = (\mathbf{Y}g)\big(F(p)\big) = \mathbf{Y}_{F(p)}[g] .
> $$
>
> *Related implies intertwining.* If the fields are $F$-related, then $dF_p(\mathbf{X}_p) = \mathbf{Y}_{F(p)}$ (Definition [[§59 Related Vector Fields#^def-59-2|§59.2]]), so the right-hand sides agree, for every $g$ and $p$; that is, $\mathbf{X}(g \circ F) = (\mathbf{Y}g) \circ F$.
>
> *Intertwining implies related.* Conversely, suppose $\mathbf{X}(g \circ F) = (\mathbf{Y}g) \circ F$ for every $g \in C^\infty(N)$, and fix $p \in M$. By the display, the two derivations $dF_p(\mathbf{X}_p)$ and $\mathbf{Y}_{F(p)}$ at $F(p)$ agree on every global function $g$. Every germ $[h]$ at $F(p)$ has a global representative $g \in C^\infty(N)$, $[g] = [h]$ (Corollary [[§56 Vector Fields#^cor-56-8|§56.8]]), so
>
> $$
> dF_p(\mathbf{X}_p)[h] = dF_p(\mathbf{X}_p)[g] = \mathbf{Y}_{F(p)}[g] = \mathbf{Y}_{F(p)}[h] .
> $$
>
> So the two derivations agree on every germ, and are equal as maps on $C^\infty_{F(p)}(N)$: $dF_p(\mathbf{X}_p) = \mathbf{Y}_{F(p)}$. As $p$ was arbitrary, the fields are $F$-related.

^pf-59-1

*Uses:* [[§59 Related Vector Fields#^def-59-2|Def. §59.2]], [[§28 Derivations and the Abstract Tangent Space#^def-28-6|Def. §28.6]], [[§28 Derivations and the Abstract Tangent Space#^def-28-1|Def. §28.1]], [[§56 Vector Fields#^cor-56-8|§56.8]], [[§56 Vector Fields#^lem-56-4|§56.4]], [[§56 Vector Fields#^def-56-8|Def. §56.8]]

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
> *(Not from lecture; filled in.)* Four things are claimed: the formula, smoothness, $F$-relatedness, and uniqueness. Here $(F_\ast\mathbf{X})\,g$ denotes the function $q \mapsto (F_\ast\mathbf{X})_q[g]$ on $N$, as in Lemma [[§56 Vector Fields#^lem-56-11|§56.11]].
>
> *The formula.* For $q \in N$ put $p = F^{-1}(q)$. By Definition [[§59 Related Vector Fields#^def-59-1|§59.1]], then Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-6|§28.6]] with $D = \mathbf{X}_p$, then Lemma [[§56 Vector Fields#^lem-56-4|§56.4]],
>
> $$
> (F_\ast\mathbf{X})_q[g] = dF_p(\mathbf{X}_p)[g] = \mathbf{X}_p[g \circ F] = \mathbf{X}(g \circ F)(p) = \big(\mathbf{X}(g \circ F) \circ F^{-1}\big)(q) ,
> $$
>
> which is the formula.
>
> *Smoothness.* At each $q$, $(F_\ast\mathbf{X})_q = dF_p(\mathbf{X}_p)$ lies in $T_{F(p)}N = T_qN$, so $F_\ast\mathbf{X}$ is a rough section of $TN$. In the formula, $g \circ F \in C^\infty(M)$ (Lemma [[§19 Smooth Functions and Smooth Maps#^lem-19-5|§19.5]]), so $\mathbf{X}(g \circ F)$ is smooth (Lemma [[§56 Vector Fields#^lem-56-4|§56.4]]); and $F^{-1}$ is smooth because $F$ is a diffeomorphism (Definition [[§19 Smooth Functions and Smooth Maps#^def-19-4|§19.4]]), so the composite $\mathbf{X}(g \circ F) \circ F^{-1}$ is smooth (Lemma [[§19 Smooth Functions and Smooth Maps#^lem-19-5|§19.5]]). This holds for every $g \in C^\infty(N)$, so $F_\ast\mathbf{X}$ is smooth by Lemma [[§56 Vector Fields#^lem-56-11|§56.11]].
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

*Uses:* [[§59 Related Vector Fields#^def-59-1|Def. §59.1]], [[§59 Related Vector Fields#^def-59-2|Def. §59.2]], [[§28 Derivations and the Abstract Tangent Space#^def-28-6|Def. §28.6]], [[§19 Smooth Functions and Smooth Maps#^def-19-4|Def. §19.4]], [[§56 Vector Fields#^lem-56-4|§56.4]], [[§19 Smooth Functions and Smooth Maps#^lem-19-5|§19.5]], [[§56 Vector Fields#^lem-56-11|§56.11]]

The reason for the characterization through operators is the following proposition.

> [!theorem] Proposition §59.3: Naturality of the Bracket
> Let $F : M \to N$ be [[§19 Smooth Functions and Smooth Maps#^def-19-3|smooth]], $\mathbf{X}_1, \mathbf{X}_2 \in \mathfrak{X}(M)$ and $\mathbf{Y}_1, \mathbf{Y}_2 \in \mathfrak{X}(N)$. If $\mathbf{X}_i$ is [[§59 Related Vector Fields#^def-59-2|F-related]] to $\mathbf{Y}_i$ for $i = 1, 2$, then the [[§58 Lie Bracket and Lie Algebra#^def-58-1|bracket]] $[\mathbf{X}_1, \mathbf{X}_2]$ is $F$-related to $[\mathbf{Y}_1, \mathbf{Y}_2]$.
>
> *Lee: Proposition 8.30*

^prop-59-3

> [!proof]+ Proof
> *(Omitted in Lecture 17 as an exercise in chasing the definitions: being $F$-related means that $F^{\ast}$ commutes with the derivations. Filled in.)* The brackets $[\mathbf{X}_1, \mathbf{X}_2] \in \mathfrak{X}(M)$ and $[\mathbf{Y}_1, \mathbf{Y}_2] \in \mathfrak{X}(N)$ are vector fields (Lemma [[§58 Lie Bracket and Lie Algebra#^lem-58-1|§58.1]]). By Proposition [[§59 Related Vector Fields#^prop-59-1|§59.1]], it suffices to show
>
> $$
> [\mathbf{X}_1, \mathbf{X}_2](g \circ F) = \big([\mathbf{Y}_1, \mathbf{Y}_2]\, g\big) \circ F \qquad \text{for every } g \in C^\infty(N).
> $$
>
> Let $g \in C^\infty(N)$. The same proposition, applied to the pairs $(\mathbf{X}_i, \mathbf{Y}_i)$, gives $\mathbf{X}_i(h \circ F) = (\mathbf{Y}_i h) \circ F$ for every $h \in C^\infty(N)$ and $i = 1, 2$.
>
> *The composite $\mathbf{X}_1\mathbf{X}_2$.* Apply this first for $i = 2$ with $h = g$, and then for $i = 1$ with $h = \mathbf{Y}_2 g$, which lies in $C^\infty(N)$ by Lemma [[§56 Vector Fields#^lem-56-4|§56.4]]:
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

*Uses:* [[§59 Related Vector Fields#^prop-59-1|§59.1]], [[§58 Lie Bracket and Lie Algebra#^def-58-1|Def. §58.1]], [[§58 Lie Bracket and Lie Algebra#^lem-58-1|§58.1]], [[§56 Vector Fields#^lem-56-4|§56.4]]

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
> 1. *Section to operator.* $(\mathbf{X}f)(p) = \mathbf{X}_p[f]$, a derivation of $C^\infty(M)$: $\mathbf{X}(fg) = f\,\mathbf{X}g + g\,\mathbf{X}f$ (Lemma [[§56 Vector Fields#^lem-56-4|§56.4]]); $\mathbf{X}f$ is smooth for every smooth $f$ exactly when $\mathbf{X}$ is smooth (Lemma [[§56 Vector Fields#^lem-56-11|§56.11]]).
> 2. *Operator to section.* Every derivation of $C^\infty(M)$ is a vector field: $\mathbf{X}_p[f] = (\mathbf{X}\tilde f)(p)$ for a global $\tilde f$ with the same germ at $p$, which exists by bump functions and does not depend on the choice (Corollary [[§56 Vector Fields#^cor-56-8|§56.8]], Lemma [[§56 Vector Fields#^lem-56-9|§56.9]], Proposition [[§56 Vector Fields#^prop-56-10|§56.10]]).
> 3. *Section to components.* On $U$, $\mathbf{X}^j = \mathbf{X}(x^j)$, that is, $\mathbf{X}^j(p) = \mathbf{X}_p[x^j] = dx^j|_p(\mathbf{X}_p)$.
> 4. *Components to section.* $\mathbf{X}_p = \sum_j \mathbf{X}^j(p)\, \partial/\partial x^j|_p$, smooth if and only if all $\mathbf{X}^j$ are (Proposition [[§56 Vector Fields#^prop-56-1|§56.1]]); then $\mathbf{X}f = \sum_j \mathbf{X}^j\, \partial f/\partial x^j$.
>
> *The same three faces for:*
> - *the bracket.* Globally $[\mathbf{X}, \mathbf{Y}]f = \mathbf{X}(\mathbf{Y}f) - \mathbf{Y}(\mathbf{X}f)$ (Definition [[§58 Lie Bracket and Lie Algebra#^def-58-1|§58.1]]). Pointwise $[\mathbf{X}, \mathbf{Y}]_p[f] = \mathbf{X}_p[\mathbf{Y}f] - \mathbf{Y}_p[\mathbf{X}f]$, which needs the global function $\mathbf{Y}f$, not only the vector $\mathbf{Y}_p$. In components $[\mathbf{X}, \mathbf{Y}]^j = \mathbf{X}(\mathbf{Y}^j) - \mathbf{Y}(\mathbf{X}^j) = \sum_i \big(\mathbf{X}^i\, \partial \mathbf{Y}^j/\partial x^i - \mathbf{Y}^i\, \partial \mathbf{X}^j/\partial x^i\big)$ (Proposition [[§58 Lie Bracket and Lie Algebra#^prop-58-2|§58.2]]).
> - *$F$-related fields.* Pointwise $F_{\ast p}\mathbf{X}_p = \mathbf{Y}_{F(p)}$ (Definition [[§59 Related Vector Fields#^def-59-2|§59.2]]). Globally $\mathbf{X}(g \circ F) = (\mathbf{Y}g) \circ F$ for all $g$ (Proposition [[§59 Related Vector Fields#^prop-59-1|§59.1]]). In components $\mathbf{Y}^i(F(p)) = \sum_j \frac{\partial F^i}{\partial x^j}(p)\, \mathbf{X}^j(p)$. For a diffeomorphism, $\mathbf{Y} = F_\ast\mathbf{X}$ with $(F_\ast\mathbf{X})_q = dF_{F^{-1}(q)}\big(\mathbf{X}_{F^{-1}(q)}\big)$ (Definition [[§59 Related Vector Fields#^def-59-1|§59.1]]).
> - *one-forms.* Pointwise $\theta_p \in T_p^{\ast}M$; globally the function $p \mapsto \theta_p(\mathbf{X}_p)$ for each vector field $\mathbf{X}$; in components $\theta_j = \theta(\partial/\partial x^j)$ and $\theta = \sum_j \theta_j\, dx^j$ (Proposition [[§53 One-Forms#^prop-53-1|§53.1]]). For $\theta = df$, $df(\mathbf{X}) = \mathbf{X}f$.
> - *the tangent bundle.* The section $\mathbf{X}$ in the standard chart of $TM$ ([[§51 The Tangent Bundle|§51]]) is $p \mapsto (x^1, \ldots, x^m, \mathbf{X}^1, \ldots, \mathbf{X}^m)$, with transition $(r, v) \mapsto (\tau(r), \tau'(r)v)$, $\tau$ the transition function of the base.

^rem-59-3

*Lecture 21 opened with the last problem of the midterm.*

> [!definition] Definition §59.3: Vector Field Tangent to a Submanifold
> Let $S \subseteq M$ be a regular submanifold, $\iota : S \hookrightarrow M$ the inclusion, and $\mathbf{X} \in \mathfrak{X}(M)$. Then $\mathbf{X}$ is **tangent to $S$** if
>
> $$
> \mathbf{X}_p \in \iota_{\ast p}(T_pS) \qquad \text{for every } p \in S .
> $$
>
> Identifying $T_pS$ with the subspace $\iota_{\ast p}(T_pS) \subseteq T_pM$ (Proposition [[§37 Regular Submanifolds#^prop-37-9|§37.9]]), this reads $\mathbf{X}_p \in T_pS$ for every $p \in S$. Nothing is required at points of $M \setminus S$.
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
> (Proposition [[§56 Vector Fields#^prop-56-1|§56.1]]). Then $\mathbf{X}_p \in T_pS$ for every $p \in S \cap U$ if and only if $g^a(x, 0) = 0$ for every $a$ and every point $(x, 0)$ of $S \cap U$: along $S$, there is no $y$ component.

^lem-59-5

> [!proof]+ Proof
> *(Not from lecture; the step the proof of Proposition [[§59 Related Vector Fields#^prop-59-7|§59.7]] uses, written out.)* Let $p \in S \cap U$. By Proposition [[§37 Regular Submanifolds#^prop-37-9|§37.9]], applied to the adapted chart with the coordinates along $S$ listed first, $\iota_{\ast p}(T_pS) = \operatorname{Span}\{ \partial/\partial x^1|_p, \ldots, \partial/\partial x^k|_p \}$. The $m$ vectors $\partial/\partial x^i|_p$, $\partial/\partial y^a|_p$ form a basis of $T_pM$ (Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-8|§29.8]]), and
>
> $$
> \mathbf{X}_p = \sum_i f^i(p)\, \frac{\partial}{\partial x^i}\Big|_p + \sum_a g^a(p)\, \frac{\partial}{\partial y^a}\Big|_p .
> $$
>
> Since coefficients in a basis are unique, $\mathbf{X}_p$ lies in the span of the $\partial/\partial x^i|_p$ exactly when every $g^a(p) = 0$. The points of $S \cap U$ are those with $y = 0$, so the condition for all $p \in S \cap U$ is $g^a(x, 0) = 0$ for all $a$.

^pf-59-5

*Uses:* [[§37 Regular Submanifolds#^prop-37-9|§37.9]], [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-8|§29.8]]

> [!theorem] Proposition §59.6: Restricting a Tangent Field to the Submanifold
> Let $S \subseteq M$ be a regular submanifold of dimension $k$, $\iota : S \hookrightarrow M$ the inclusion, and $\mathbf{X} \in \mathfrak{X}(M)$ tangent to $S$ (Definition [[§59 Related Vector Fields#^def-59-3|§59.3]]). Then there is a unique smooth vector field $\mathbf{X}|_S \in \mathfrak{X}(S)$ that is $\iota$-related to $\mathbf{X}$ (Definition [[§59 Related Vector Fields#^def-59-2|§59.2]]):
>
> $$
> \iota_{\ast p}\big( (\mathbf{X}|_S)_p \big) = \mathbf{X}_p \qquad \text{for every } p \in S .
> $$
>
> In an adapted chart $(U, (x, y))$ as in Lemma [[§59 Related Vector Fields#^lem-59-5|§59.5]], where $\mathbf{X} = \sum_i f^i\, \partial/\partial x^i + \sum_a g^a\, \partial/\partial y^a$,
>
> $$
> \mathbf{X}|_S = \sum_{i=1}^k (f^i \circ \iota)\, \frac{\partial}{\partial x^i}\Big|^S \qquad \text{on } S \cap U ,
> $$
>
> in the induced chart $x|_{S \cap U}$ of $S$.
>
> *Lee: Proposition 8.23*

^prop-59-6

> [!proof]+ Proof
> *(Cited from Lee in the submitted solution of Assignment 8, Problem 5; the proof is filled in.)*
>
> *The vectors.* Let $p \in S$. The map $\iota_{\ast p}$ is injective (Proposition [[§37 Regular Submanifolds#^prop-37-9|§37.9]]) and $\mathbf{X}_p$ lies in its image, so there is exactly one $v_p \in T_pS$ with $\iota_{\ast p}(v_p) = \mathbf{X}_p$. So there is exactly one map $p \mapsto v_p$ with the required property; put $(\mathbf{X}|_S)_p = v_p$. It remains to show that it is smooth.
>
> *Smoothness.* Let $p \in S$ and let $(U, (x, y))$ be an adapted chart at $p$. By Lemma [[§59 Related Vector Fields#^lem-59-5|§59.5]], $g^a = 0$ on $S \cap U$, so for $q \in S \cap U$, by Proposition [[§37 Regular Submanifolds#^prop-37-9|§37.9]] and the linearity of $\iota_{\ast q}$,
>
> $$
> \mathbf{X}_q = \sum_{i=1}^k f^i(q)\, \frac{\partial}{\partial x^i}\Big|_q = \sum_{i=1}^k f^i(q)\, \iota_{\ast q}\Big( \frac{\partial}{\partial x^i}\Big|^S_q \Big) = \iota_{\ast q}\Big( \sum_{i=1}^k f^i(q)\, \frac{\partial}{\partial x^i}\Big|^S_q \Big) .
> $$
>
> By the uniqueness of $v_q$, $(\mathbf{X}|_S)_q = \sum_i f^i(q)\, \partial/\partial x^i|^S_q$: the coefficients of $\mathbf{X}|_S$ in the chart $x|_{S \cap U}$ of $S$ are the functions $f^i \circ \iota$ on $S \cap U$, smooth as composites of smooth maps (Lemma [[§37 Regular Submanifolds#^lem-37-5|§37.5]](1), Lemma [[§19 Smooth Functions and Smooth Maps#^lem-19-5|§19.5]]). By Proposition [[§56 Vector Fields#^prop-56-1|§56.1]], $\mathbf{X}|_S$ is smooth on $S \cap U$. Such sets cover $S$.

^pf-59-6

*Uses:* [[§37 Regular Submanifolds#^prop-37-9|§37.9]], [[§59 Related Vector Fields#^lem-59-5|§59.5]], [[§37 Regular Submanifolds#^lem-37-5|§37.5]], [[§19 Smooth Functions and Smooth Maps#^lem-19-5|§19.5]], [[§56 Vector Fields#^prop-56-1|§56.1]]

> [!theorem] Proposition §59.7: Brackets of Fields Tangent to a Submanifold
> Let $S \subseteq M$ be a regular submanifold and $\mathbf{X}, \mathbf{Y} \in \mathfrak{X}(M)$ tangent to $S$ (Definition [[§59 Related Vector Fields#^def-59-3|§59.3]]). Then $[\mathbf{X}, \mathbf{Y}]$ is also tangent to $S$.
>
> *Lee: Corollary 8.32*

^prop-59-7

> [!proof]+ Proof
> *(Lecture 21, in outline; the bookkeeping is filled in.)* Use adapted coordinates: near $p \in S$ take a slice chart $(x, y) = (x^1, \ldots, x^k, y^1, \ldots, y^{m-k})$ with $S = \{ y = 0 \}$ (Definitions [[§37 Regular Submanifolds#^def-37-2|§37.2]] and [[§37 Regular Submanifolds#^def-37-3|§37.3]]); on the exam, $M$ was two-dimensional, but $x$ and $y$ may be vector-valued: neither the dimension nor the codimension matters. Write
>
> $$
> \mathbf{X} = \sum_i f^i\, \frac{\partial}{\partial x^i} + \sum_a g^a\, \frac{\partial}{\partial y^a}, \qquad
> \mathbf{Y} = \sum_i u^i\, \frac{\partial}{\partial x^i} + \sum_a v^a\, \frac{\partial}{\partial y^a} .
> $$
>
> By Lemma [[§59 Related Vector Fields#^lem-59-5|§59.5]], tangency says $g^a(x, 0) = 0$ and $v^a(x, 0) = 0$: there is no $y$ component along $S$. We show the $\partial/\partial y^b$ components of $[\mathbf{X}, \mathbf{Y}]$ have the same property. By Proposition [[§58 Lie Bracket and Lie Algebra#^prop-58-2|§58.2]], that component is
>
> $$
> \mathbf{X}(v^b) - \mathbf{Y}(g^b) = \sum_i f^i\, \frac{\partial v^b}{\partial x^i} + \sum_a g^a\, \frac{\partial v^b}{\partial y^a} - \sum_i u^i\, \frac{\partial g^b}{\partial x^i} - \sum_a v^a\, \frac{\partial g^b}{\partial y^a} .
> $$
>
> Evaluate at $y = 0$. The terms with $\partial/\partial x^i$ vanish for one reason: a partial with respect to $x$ at $y = 0$ is computed by first setting $y = 0$ and then differentiating in $x$, and with $y = 0$ the function is already zero — $\frac{\partial v^b}{\partial x^i}(x, 0) = \frac{\partial}{\partial x^i}\big(v^b(x, 0)\big) = 0$, and likewise for $g^b$. The terms with $\partial/\partial y^a$ vanish for a different reason: the partials $\partial v^b/\partial y^a$ and $\partial g^b/\partial y^a$ need not be zero, but their coefficients $g^a(x, 0)$ and $v^a(x, 0)$ are. So the $y$-components of $[\mathbf{X}, \mathbf{Y}]$ vanish on $S$, and $[\mathbf{X}, \mathbf{Y}]_p \in T_pS$ for $p \in S$.

^pf-59-7

*Uses:* [[§37 Regular Submanifolds#^def-37-2|Def. §37.2]], [[§37 Regular Submanifolds#^def-37-3|Def. §37.3]], [[§58 Lie Bracket and Lie Algebra#^prop-58-2|§58.2]], [[§59 Related Vector Fields#^lem-59-5|§59.5]]

> [!proof]+ Second proof, through related fields
> *(Lee's proof of Corollary 8.32; it is the route of the submitted solution of Assignment 8, Problem 5.)* By Proposition [[§59 Related Vector Fields#^prop-59-6|§59.6]], $\mathbf{X}|_S$ and $\mathbf{Y}|_S$ are smooth vector fields on $S$, $\iota$-related to $\mathbf{X}$ and to $\mathbf{Y}$. By the naturality of the bracket (Proposition [[§59 Related Vector Fields#^prop-59-3|§59.3]], with $F = \iota$), $[\mathbf{X}|_S, \mathbf{Y}|_S]$ is $\iota$-related to $[\mathbf{X}, \mathbf{Y}]$: for every $p \in S$,
>
> $$
> [\mathbf{X}, \mathbf{Y}]_p = \iota_{\ast p}\big( [\mathbf{X}|_S, \mathbf{Y}|_S]_p \big) \in \iota_{\ast p}(T_pS) .
> $$
>
> So $[\mathbf{X}, \mathbf{Y}]$ is tangent to $S$.

^pf-59-7-2

*Uses:* [[§59 Related Vector Fields#^prop-59-6|§59.6]], [[§59 Related Vector Fields#^prop-59-3|§59.3]]

![[m591-56-5.svg]]
*A field tangent to $S$, near $S$. Left: $S$ in $M$ and the domain $U$ of a slice chart $\varphi = (x, y)$. Right: in the chart, $\varphi(S \cap U) = \{y = 0\}$, and $\mathbf{X} = f\,\partial_x + g\,\partial_y$ is tangent to $S$ exactly when $g(x, 0) = 0$: on the slice its arrows point along it.*

**Comparison with Lee.** Lee proves this (Corollary 8.32) with related fields: on $S$, $\mathbf{X}$ and $\mathbf{Y}$ restrict to fields $\iota$-related to them (Proposition [[§59 Related Vector Fields#^prop-59-6|§59.6]]), and the naturality of the bracket (Proposition [[§59 Related Vector Fields#^prop-59-3|§59.3]]) applied to the inclusion $\iota : S \to M$ does the rest; this is the second proof above. The coordinate proof is the one given in class.

**Transcription note (Lecture 21).** Page 55 of the handwritten notes records the $\partial_y$ component of $[f\partial_x, v\partial_y]$ as $\partial v/\partial x|_{y = 0}$; it is $f\, \partial v/\partial x|_{y = 0}$, which vanishes for the same reason.

> [!theorem] Corollary §59.8: Restriction Commutes with the Bracket
> Let $S \subseteq M$ be a regular submanifold and $\mathbf{X}, \mathbf{Y} \in \mathfrak{X}(M)$ tangent to $S$. Then
>
> $$
> [\mathbf{X}, \mathbf{Y}]\big|_S = \big[ \mathbf{X}|_S, \mathbf{Y}|_S \big] .
> $$

^cor-59-8

> [!proof]+ Proof
> *(Not from lecture; a by-product of the second proof of Proposition [[§59 Related Vector Fields#^prop-59-7|§59.7]].)* By that proof, $[\mathbf{X}|_S, \mathbf{Y}|_S]$ is a smooth vector field on $S$ that is $\iota$-related to $[\mathbf{X}, \mathbf{Y}]$, and $[\mathbf{X}, \mathbf{Y}]$ is tangent to $S$. By the uniqueness in Proposition [[§59 Related Vector Fields#^prop-59-6|§59.6]], applied to the field $[\mathbf{X}, \mathbf{Y}]$, it is $[\mathbf{X}, \mathbf{Y}]|_S$.

^pf-59-8

*Uses:* [[§59 Related Vector Fields#^prop-59-7|§59.7]], [[§59 Related Vector Fields#^prop-59-6|§59.6]]

> [!theorem] Corollary §59.9: A Necessary Condition for an Integral Submanifold
> Let $S \subseteq M$ be a regular submanifold of dimension $k$, with inclusion $\iota$, and let $\mathbf{X}_1, \ldots, \mathbf{X}_k \in \mathfrak{X}(M)$ be tangent to $S$. If $p \in S$ and the vectors $(\mathbf{X}_1)_p, \ldots, (\mathbf{X}_k)_p$ are linearly independent, then they form a basis of $\iota_{\ast p}(T_pS)$, and
>
> $$
> [\mathbf{X}_i, \mathbf{X}_j]_p \in \operatorname{Span}\big\{ (\mathbf{X}_1)_p, \ldots, (\mathbf{X}_k)_p \big\} \qquad \text{for all } i, j .
> $$
>
> *Lee: Proposition 19.3*

^cor-59-9

> [!proof]+ Proof
> *(Assignment 8, Problem 5: the argument of the submitted solution, for $k$ fields.)* Since $\iota_{\ast p}$ is injective (Proposition [[§37 Regular Submanifolds#^prop-37-9|§37.9]]), $\iota_{\ast p}(T_pS)$ has dimension $k$. The $k$ vectors $(\mathbf{X}_i)_p$ lie in it, because the fields are tangent to $S$ (Definition [[§59 Related Vector Fields#^def-59-3|§59.3]]), and are linearly independent; so they form a basis of it. By Proposition [[§59 Related Vector Fields#^prop-59-7|§59.7]], each $[\mathbf{X}_i, \mathbf{X}_j]$ is tangent to $S$, so $[\mathbf{X}_i, \mathbf{X}_j]_p \in \iota_{\ast p}(T_pS)$, the span of that basis.

^pf-59-9

*Uses:* [[§37 Regular Submanifolds#^prop-37-9|§37.9]], [[§59 Related Vector Fields#^def-59-3|Def. §59.3]], [[§59 Related Vector Fields#^prop-59-7|§59.7]]

Read in the other direction: if at some point the fields are independent and one of their brackets leaves their span, then no $k$-dimensional regular submanifold through that point is tangent to all of them. For $k = 1$ the condition is empty, since $[\mathbf{X}, \mathbf{X}] = 0$, in agreement with the existence of integral curves (Theorem [[§68 Local Existence and Uniqueness#^thm-68-2|§68.2]]). For commuting fields it holds trivially; their flows commute (Theorem [[§72 Lie Derivatives#^thm-72-9|§72.9]], later). That the condition, imposed at every point, is also sufficient for integral submanifolds to exist is the Frobenius theorem (Lee, Chapter 19), which is not part of these notes.

> [!example] Example §59.2: Two Fields in $\mathbb{R}^3$ with No Integral Surface
> On $\mathbb{R}^3$, with coordinates $(x, y, z)$, let
>
> $$
> \mathbf{X} = \frac{\partial}{\partial x} - \frac{y}{2}\, \frac{\partial}{\partial z}, \qquad \mathbf{Y} = \frac{\partial}{\partial y} + \frac{x}{2}\, \frac{\partial}{\partial z} .
> $$
>
> 1. $[\mathbf{X}, \mathbf{Y}] = \partial/\partial z$.
> 2. There is no non-empty regular submanifold $S \subseteq \mathbb{R}^3$ of dimension two such that $\mathbf{X}$ and $\mathbf{Y}$ are both tangent to $S$.
> 3. The flows of $\mathbf{X}$ and $\mathbf{Y}$ are $\varphi_s(x, y, z) = (x + s,\ y,\ z - \tfrac{ys}{2})$ and $\psi_t(x, y, z) = (x,\ y + t,\ z + \tfrac{xt}{2})$, and
>
> $$
> \psi_{-t} \circ \varphi_{-s} \circ \psi_t \circ \varphi_s(0, 0, 0) = (0, 0, st) .
> $$
>
> So integral curves have no analogue for a general pair of vector fields, with surfaces in place of curves: at every point the plane $\operatorname{Span}\{\mathbf{X}_p, \mathbf{Y}_p\}$ is defined, but no surface is tangent to all these planes.
>
> *Lee: cf. Example 19.1(d)*

^ex-59-2

> [!remark]- Connections
> - $\mathbf{X}$, $\mathbf{Y}$ and $\partial/\partial z$ are the left-invariant vector fields of the Heisenberg group: [[§71 The Exponential Map#^ex-71-4|Ex. §71.4]].
> - The open path of part (3) is the bracket as the failure of flows to commute: [[§72 Lie Derivatives#^prop-72-12|§72.12]]; commuting fields have commuting flows: [[§72 Lie Derivatives#^thm-72-9|§72.9]].

> [!proof]+ Proof
> *(Assignment 8, Problem 5: the submitted solution. Part (3) is not from the assignment.)*
>
> *(1).* Write $\mathbf{X} = \sum_i \mathbf{X}^i\, \partial_i$ and $\mathbf{Y} = \sum_i \mathbf{Y}^i\, \partial_i$ with respect to $\partial_x, \partial_y, \partial_z$: $(\mathbf{X}^1, \mathbf{X}^2, \mathbf{X}^3) = (1, 0, -\tfrac{y}{2})$ and $(\mathbf{Y}^1, \mathbf{Y}^2, \mathbf{Y}^3) = (0, 1, \tfrac{x}{2})$. By Proposition [[§58 Lie Bracket and Lie Algebra#^prop-58-2|§58.2]], $[\mathbf{X}, \mathbf{Y}] = \sum_i \big( \mathbf{X}(\mathbf{Y}^i) - \mathbf{Y}(\mathbf{X}^i) \big)\, \partial_i$, and
>
> $$
> \mathbf{X}(\mathbf{Y}^1) - \mathbf{Y}(\mathbf{X}^1) = 0, \qquad \mathbf{X}(\mathbf{Y}^2) - \mathbf{Y}(\mathbf{X}^2) = 0, \qquad \mathbf{X}(\mathbf{Y}^3) - \mathbf{Y}(\mathbf{X}^3) = \mathbf{X}\Big(\frac{x}{2}\Big) + \mathbf{Y}\Big(\frac{y}{2}\Big) = \frac12 + \frac12 = 1 .
> $$
>
> *(2).* Suppose $S$ is such a submanifold, and let $p = (x, y, z) \in S$. The vectors $\mathbf{X}_p$ and $\mathbf{Y}_p$ are linearly independent, since their $(\partial_x, \partial_y)$-components are $(1, 0)$ and $(0, 1)$. By Corollary [[§59 Related Vector Fields#^cor-59-9|§59.9]], with $k = 2$, $[\mathbf{X}, \mathbf{Y}]_p \in \operatorname{Span}\{\mathbf{X}_p, \mathbf{Y}_p\}$. But for $a, b \in \mathbb{R}$,
>
> $$
> a\,\mathbf{X}_p + b\,\mathbf{Y}_p = a\, \frac{\partial}{\partial x}\Big|_p + b\, \frac{\partial}{\partial y}\Big|_p + \Big( -\frac{ay}{2} + \frac{bx}{2} \Big) \frac{\partial}{\partial z}\Big|_p ,
> $$
>
> and if this equals $[\mathbf{X}, \mathbf{Y}]_p = \partial/\partial z|_p$, comparing the $\partial_x$ and $\partial_y$ components gives $a = b = 0$, and then the left side is $0 \neq \partial/\partial z|_p$. This contradiction shows that no such $S$ exists. (The submitted solution obtains $[\mathbf{X}, \mathbf{Y}]_p \in \iota_{\ast p}(T_pS)$ by restricting $\mathbf{X}$ and $\mathbf{Y}$ to $S$ and using the naturality of the bracket: the second proof of Proposition [[§59 Related Vector Fields#^prop-59-7|§59.7]].)
>
> *(3).* By Proposition [[§67 Integral Curves#^prop-67-2|§67.2]], a curve $(x(s), y(s), z(s))$ is an integral curve of $\mathbf{X}$ if and only if $\dot x = 1$, $\dot y = 0$, $\dot z = -y/2$; the solution starting at $(x, y, z)$ is $(x + s,\ y,\ z - \tfrac{ys}{2})$, defined for all $s$. Likewise for $\mathbf{Y}$: $\dot x = 0$, $\dot y = 1$, $\dot z = x/2$, with solution $(x,\ y + t,\ z + \tfrac{xt}{2})$. Following the four flows from the origin,
>
> $$
> (0, 0, 0) \ \xrightarrow{\ \varphi_s\ }\ (s, 0, 0) \ \xrightarrow{\ \psi_t\ }\ \big(s, t, \tfrac{st}{2}\big) \ \xrightarrow{\ \varphi_{-s}\ }\ \big(0, t, \tfrac{st}{2} + \tfrac{ts}{2}\big) = (0, t, st) \ \xrightarrow{\ \psi_{-t}\ }\ (0, 0, st) .
> $$

^pf-ex-59-2

*Uses:* [[§58 Lie Bracket and Lie Algebra#^prop-58-2|§58.2]], [[§59 Related Vector Fields#^cor-59-9|§59.9]], [[§59 Related Vector Fields#^prop-59-7|§59.7]], [[§67 Integral Curves#^prop-67-2|§67.2]]

The path of (3) is tangent to the planes $\operatorname{Span}\{\mathbf{X}, \mathbf{Y}\}$ on each of its four legs, and its shadow in the $(x, y)$-plane is a closed rectangle; but the path does not close: it climbs by $st$, the area of the rectangle, in the direction of $[\mathbf{X}, \mathbf{Y}] = \partial/\partial z$. This is the bracket as the failure of the flows to commute (Proposition [[§72 Lie Derivatives#^prop-72-12|§72.12]], later). It also gives a second reason, in outline, why no surface is tangent to the planes. A surface $S$ through the origin tangent to them would contain the path for all small $s$ and $t$, because an integral curve of $\mathbf{X}$ or $\mathbf{Y}$ that starts on $S$ stays on $S$ for a short time: it is the integral curve of the restricted field of Proposition [[§59 Related Vector Fields#^prop-59-6|§59.6]] (by Proposition [[§70 Complete Vector Fields#^prop-70-10|§70.10]], later, and uniqueness). Then $S$ would contain points $(0, 0, st)$ of the $z$-axis arbitrarily close to the origin; but the tangent plane of $S$ at the origin is horizontal, so near the origin $S$ is a graph over the $(x, y)$-plane and meets the $z$-axis only at the origin. The fields $\mathbf{X}$, $\mathbf{Y}$ and $\partial/\partial z$ are the left-invariant vector fields of the Heisenberg group (Example [[§71 The Exponential Map#^ex-71-4|§71.4]], later).*

![[m591-77-3.svg]]

*(Not from lecture; figure added.)* The planes $\operatorname{Span}\{\mathbf{X}_p, \mathbf{Y}_p\}$ of Example [[§59 Related Vector Fields#^ex-59-2|§59.2]] at points of the plane $z = 0$ (they do not depend on $z$): horizontal at the origin, and tilting more the farther $p$ is from the $z$-axis. Red: the path of part (3) for $s = t = 1.4$, tangent to the planes on each leg; its shadow (dashed) is a closed rectangle of area $st$, but the path ends at height $st$ above its starting point.

![[m591-77-a3.gif|520]]

*(Not from lecture; animation added, vault only.)* The path of part (3) traced leg by leg, for $s = t = 1.4$: the flow of $\mathbf{X}$, of $\mathbf{Y}$, of $\mathbf{X}$ backwards, of $\mathbf{Y}$ backwards. Its shadow in the $(x, y)$-plane (dashed) closes up; the path itself ends at height $st$ above the point where it started.

> [!theorem] Lemma §59.10: Vector Fields on a Submanifold Extend Locally
> Let $S \subseteq M$ be a regular submanifold of dimension $k$, $\iota : S \hookrightarrow M$ the inclusion, and $\mathbf{X} \in \mathfrak{X}(S)$. Let $(U, (x, y))$ be an adapted chart with $S \cap U = \{y = 0\}$ and image a product $V \times W$, $\vec 0 \in W$ (Lemma [[§37 Regular Submanifolds#^lem-37-6|§37.6]], where the codimension is $m - k$), and $\pi : U \to U \cap S$ the retraction of Lemma [[§37 Regular Submanifolds#^lem-37-7|§37.7]]. Write $\mathbf{X} = \sum_{i=1}^k \mathbf{X}^i\, \partial/\partial x^i|^S$ on $U \cap S$, in the induced chart $x|_{U \cap S}$ of $S$. Then
>
> $$
> \mathbf{Y} = \sum_{i=1}^k (\mathbf{X}^i \circ \pi)\, \frac{\partial}{\partial x^i} \in \mathfrak{X}(U)
> $$
>
> satisfies $\mathbf{Y}_p = \iota_{\ast p}(\mathbf{X}_p)$ for every $p \in U \cap S$. In particular $\mathbf{Y}$ is tangent to $S$ (Definition [[§59 Related Vector Fields#^def-59-3|§59.3]]).

^lem-59-10

> [!proof]+ Proof
> *(Assignment 7, Problem 1: the submitted solution, the step “the local extension”.)* *$\mathbf{Y}$ is smooth.* Since $\mathbf{X}$ is a smooth vector field on $S$, its coefficients $\mathbf{X}^i$ in the chart $x|_{U \cap S}$ of $S$ are smooth functions on $U \cap S$ (Proposition [[§56 Vector Fields#^prop-56-1|§56.1]], on the manifold $S$). By Lemma [[§37 Regular Submanifolds#^lem-37-8|§37.8]], each $\mathbf{X}^i \circ \pi$ is smooth on $U$; the coefficients of $\partial/\partial y^a$ are $0$, also smooth. By Proposition [[§56 Vector Fields#^prop-56-1|§56.1]], $\mathbf{Y} \in \mathfrak{X}(U)$.
>
> *$\mathbf{Y}$ extends $\mathbf{X}$.* Let $p \in U \cap S$. Since $\pi(p) = p$, the coefficients of $\mathbf{Y}_p$ are $\mathbf{X}^i(p)$ for $i \le k$ and $0$ for the $\partial/\partial y^a$. By linearity of $\iota_{\ast p}$ and Proposition [[§37 Regular Submanifolds#^prop-37-9|§37.9]] (with $x^1, \ldots, x^k$ the coordinates of $S$), $\iota_{\ast p}(\partial/\partial x^i|^S_p) = \partial/\partial x^i|_p$, so
>
> $$
> \iota_{\ast p}(\mathbf{X}_p) = \sum_{i=1}^k \mathbf{X}^i(p)\, \iota_{\ast p}\Big(\frac{\partial}{\partial x^i}\Big|^S_p\Big) = \sum_{i=1}^k \mathbf{X}^i(p)\, \frac{\partial}{\partial x^i}\Big|_p = \mathbf{Y}_p .
> $$
>
> *Tangency* *(filled in)*: $\mathbf{Y}_p = \iota_{\ast p}(\mathbf{X}_p) \in \iota_{\ast p}(T_pS)$ for $p \in U \cap S$; equivalently, $\mathbf{Y}$ has no $\partial/\partial y$ component at all (Lemma [[§59 Related Vector Fields#^lem-59-5|§59.5]]).

^pf-59-10

*Uses:* [[§56 Vector Fields#^prop-56-1|§56.1]], [[§37 Regular Submanifolds#^lem-37-8|§37.8]], [[§37 Regular Submanifolds#^prop-37-9|§37.9]], [[§59 Related Vector Fields#^lem-59-5|§59.5]]

The local extension depends on the chart; a global one is glued from local ones with a partition of unity, in Theorem [[§65 Partitions of Unity#^thm-65-11|§65.11]].
