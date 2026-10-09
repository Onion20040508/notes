---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 7
section: 49
tags: [differentiable-manifolds, math591]
---
← [[§48 Vector Fields]] · ↑ [[· 7 Vector Fields and Lie Groups]] · [[§50 Lie Groups and Left-Invariant Vector Fields]] →

*Stage: fields — Two vector fields, composed as operators, give a second-order operator; their commutator cancels the second derivatives and is again a vector field, so $\mathfrak{X}(M)$ is a Lie algebra.*

*Lecture 16. “Who cares? There is one reason we care … when we look at commutators.”*

> [!definition] Definition §49.1: The Lie Bracket of Vector Fields
> For $\mathbf{X}, \mathbf{Y} \in \mathfrak{X}(M)$, regarded as [[§48 Vector Fields#^lem-48-2|operators]] on $C^\infty(M)$ ([[§48 Vector Fields#^def-48-4|Definition §48.4]]), the **commutator** or **Lie bracket** is the operator
>
> $$
> [\mathbf{X}, \mathbf{Y}](f) = \mathbf{X}\big(\mathbf{Y}(f)\big) - \mathbf{Y}\big(\mathbf{X}(f)\big), \qquad f \in C^\infty(M).
> $$
>
> *Lee: Ch. 8, Lie Brackets*

^def-49-1

Each composite $\mathbf{X} \circ \mathbf{Y}$ is a [[§48 Vector Fields#^def-48-11|second-order operator]] — “you get second derivatives in local coordinates” — but “something very, very nice happens when you look at the commutator.”

> [!theorem] Lemma §49.1: The Bracket of Vector Fields Is a Vector Field
> $[\mathbf{X}, \mathbf{Y}]$ is a [[§48 Vector Fields#^def-48-5|derivation]] of $C^\infty(M)$; hence, by [[§48 Vector Fields#^prop-48-7|Proposition §48.7]], it is a [[§48 Vector Fields#^def-48-1|vector field]].
>
> *Lee: Lemma 8.25*

^lem-49-1

> [!proof]+ Proof
> *(Lecture 16 — “tedious algebra … the key thing is the product rule.”)* Linearity is clear, as a difference of composites of linear maps. For the product rule, apply the [[§48 Vector Fields#^lem-48-2|product rule]] for $\mathbf{Y}$ and then for $\mathbf{X}$:
>
> $$
> \mathbf{X}\big(\mathbf{Y}(fg)\big) = \mathbf{X}\big(f\, \mathbf{Y}g + g\, \mathbf{Y}f\big) = \mathbf{X}f\; \mathbf{Y}g + f\, \mathbf{X}\mathbf{Y}g + \mathbf{X}g\; \mathbf{Y}f + g\, \mathbf{X}\mathbf{Y}f .
> $$
>
> The same expression with $\mathbf{X}$ and $\mathbf{Y}$ exchanged is $\mathbf{Y}f\, \mathbf{X}g + f\,\mathbf{Y}\mathbf{X}g + \mathbf{Y}g\,\mathbf{X}f + g\,\mathbf{Y}\mathbf{X}f$. Subtracting, the first-order cross terms $\mathbf{X}f\,\mathbf{Y}g$ and $\mathbf{X}g\,\mathbf{Y}f$ cancel, leaving
>
> $$
> [\mathbf{X}, \mathbf{Y}](fg) = f\, [\mathbf{X}, \mathbf{Y}](g) + g\, [\mathbf{X}, \mathbf{Y}](f).
> $$

^pf-49-1

*Uses:* [[§49 Lie Bracket and Lie Algebra#^def-49-1|Def. §49.1]], [[§48 Vector Fields#^def-48-5|Def. §48.5]], [[§48 Vector Fields#^lem-48-2|§48.2]], [[§48 Vector Fields#^prop-48-7|§48.7]]

> [!example] Example §49.1: A Bracket in the Plane
> On $\mathbb{R}^2$ with coordinates $(x, y)$, let $\mathbf{X} = a\, \partial_x$ and $\mathbf{Y} = b\, \partial_y$ with $a, b \in C^\infty(\mathbb{R}^2)$. Then
>
> $$
> [\mathbf{X}, \mathbf{Y}] = a\, \frac{\partial b}{\partial x}\, \frac{\partial}{\partial y} \;-\; b\, \frac{\partial a}{\partial y}\, \frac{\partial}{\partial x} .
> $$

^ex-49-1

> [!proof]+ Proof
> *(Lecture 16 — “an exercise in multivariable calculus.”)* Apply both composites to a function $f$ and use the product rule:
>
> $$
> \mathbf{X}\mathbf{Y}f = a\, \partial_x(b\, \partial_y f) = a\, \frac{\partial b}{\partial x}\, \frac{\partial f}{\partial y} + ab\, \frac{\partial^2 f}{\partial x\, \partial y}, \qquad
> \mathbf{Y}\mathbf{X}f = b\, \frac{\partial a}{\partial y}\, \frac{\partial f}{\partial x} + ba\, \frac{\partial^2 f}{\partial y\, \partial x} .
> $$
>
> The second derivatives are [[Schwarz–Clairaut Theorem|equal]] and cancel in the difference, leaving the stated first-order operator.

^pf-ex-49-1

*Uses:* [[§49 Lie Bracket and Lie Algebra#^def-49-1|Def. §49.1]], [[Schwarz–Clairaut Theorem|452 §6.1]]

> [!theorem] Proposition §49.2: The Bracket in Coordinates
> In a chart with $\mathbf{X} = \sum_i X^i\, \partial_i$ and $\mathbf{Y} = \sum_i Y^i\, \partial_i$, where $\partial_i = \partial/\partial x^i$,
>
> $$
> [\mathbf{X}, \mathbf{Y}] = \sum_j \big( \mathbf{X}(Y^j) - \mathbf{Y}(X^j) \big)\, \partial_j = \sum_j \sum_i \Big( X^i\, \frac{\partial Y^j}{\partial x^i} - Y^i\, \frac{\partial X^j}{\partial x^i} \Big)\, \partial_j .
> $$
>
> *Lee: Proposition 8.26*

^prop-49-2

> [!proof]+ Proof
> *(Not from lecture; filled in — [[§49 Lie Bracket and Lie Algebra#^ex-49-1|Example §49.1]] is the case $\mathbf{X} = a\,\partial_x$, $\mathbf{Y} = b\,\partial_y$.)* The $j$-th coefficient of a vector field is its value on the coordinate function $x^j$ ([[§48 Vector Fields#^prop-48-1|Proposition §48.1]]), and $[\mathbf{X}, \mathbf{Y}](x^j) = \mathbf{X}(\mathbf{Y}x^j) - \mathbf{Y}(\mathbf{X}x^j) = \mathbf{X}(Y^j) - \mathbf{Y}(X^j)$. The second form expands $\mathbf{X}(Y^j) = \sum_i X^i\, \partial Y^j/\partial x^i$.

^pf-49-2

*Uses:* [[§49 Lie Bracket and Lie Algebra#^def-49-1|Def. §49.1]], [[§49 Lie Bracket and Lie Algebra#^lem-49-1|§49.1]], [[§48 Vector Fields#^prop-48-1|§48.1]]

> [!definition] Definition §49.2: Lie Algebra
> A (real) **Lie algebra** $\mathfrak{g}$ is a real [[§2 Definition of Vector Space#^ladr-1-20|vector space]] together with a [[§38 Tensor Products#^ladr-9-77|bilinear]], skew-symmetric operation $[\cdot,\cdot] : \mathfrak{g} \times \mathfrak{g} \to \mathfrak{g}$, the **Lie bracket**, satisfying the **Jacobi identity**
>
> $$
> [X, [Y, Z]] + [Y, [Z, X]] + [Z, [X, Y]] = 0 \qquad \text{for all } X, Y, Z \in \mathfrak{g}.
> $$
>
> *Lee: Ch. 8, Lie Algebras*

^def-49-2

> [!remark]- Connections
> - In classical mechanics the Poisson bracket is bilinear, antisymmetric and satisfies the Jacobi identity ([[§B8.1 Poisson Brackets#^thm-b8-1-2|CM Theorem §B8.1.2]]), so the phase-space functions form a Lie algebra: [[§B8.1 Poisson Brackets#^rem-b8-1-1|CM Remark: The structure behind the four rules]].
> - In quantum mechanics the commutator of operators has the same algebra, Jacobi identity included: [[§B2.4 Commutators and the Generalized Uncertainty Principle#^thm-b2-4-1|QM Theorem §B2.4.1]].

The three terms come from one by permuting $X, Y, Z$ cyclically: “move $Y$ to the left position, $Z$ one over to the left, and $X$ jumps to the last position.”

> [!theorem] Proposition §49.3: Commutators of an Associative Product
> Let $A$ be a real vector space with a bilinear *associative* product $(X, Y) \mapsto X \ast Y$. Then the commutator $[X, Y] = X \ast Y - Y \ast X$ is bilinear, skew-symmetric, and satisfies the [[§49 Lie Bracket and Lie Algebra#^def-49-2|Jacobi identity]]; so $(A, [\cdot,\cdot])$ is a [[§49 Lie Bracket and Lie Algebra#^def-49-2|Lie algebra]].

^prop-49-3

> [!proof]+ Proof
> *(Stated in Lecture 16 as “a general fact”; filled in. “The key thing is that it be an associative product.”)* Bilinearity and skew-symmetry are immediate. By associativity, triple products can be written without parentheses, and
>
> $$
> [X, [Y, Z]] = XYZ - XZY - YZX + ZYX .
> $$
>
> Permuting cyclically gives $[Y,[Z,X]] = YZX - YXZ - ZXY + XZY$ and $[Z,[X,Y]] = ZXY - ZYX - XYZ + YXZ$. In the sum each of the six words $XYZ, XZY, YZX, ZYX, YXZ, ZXY$ appears once with each sign, so the sum is $0$.

^pf-49-3

*Uses:* [[§49 Lie Bracket and Lie Algebra#^def-49-2|Def. §49.2]]

> [!example] Example §49.2: Matrices
> $\operatorname{Mat}(n, \mathbb{R})$, with the commutator $[A, B] = AB - BA$ of matrix multiplication, is a [[§49 Lie Bracket and Lie Algebra#^def-49-2|Lie algebra]], by [[§49 Lie Bracket and Lie Algebra#^prop-49-3|Proposition §49.3]].

^ex-49-2

> [!theorem] Corollary §49.4: Vector Fields Form a Lie Algebra
> $\big(\mathfrak{X}(M), [\cdot,\cdot]\big)$ is a [[§49 Lie Bracket and Lie Algebra#^def-49-2|Lie algebra]].
>
> *Lee: Proposition 8.28*

^cor-49-4

> [!proof]+ Proof
> *(Lecture 16: the bracket of fields “comes from the product, which is the composition, which is associative.” Filled in.)* The linear operators on $C^\infty(M)$ form an associative algebra under composition, so by [[§49 Lie Bracket and Lie Algebra#^prop-49-3|Proposition §49.3]] their commutator satisfies the Jacobi identity. By [[§49 Lie Bracket and Lie Algebra#^lem-49-1|Lemma §49.1]], $\mathfrak{X}(M)$, identified with the derivations, is closed under it; so the identity holds on $\mathfrak{X}(M)$.

^pf-49-4

*Uses:* [[§49 Lie Bracket and Lie Algebra#^def-49-1|Def. §49.1]], [[§49 Lie Bracket and Lie Algebra#^def-49-2|Def. §49.2]], [[§49 Lie Bracket and Lie Algebra#^prop-49-3|§49.3]], [[§49 Lie Bracket and Lie Algebra#^lem-49-1|§49.1]], [[§48 Vector Fields#^lem-48-2|§48.2]], [[§48 Vector Fields#^prop-48-7|§48.7]]

“Which I don't recommend you check by hand. It's a big computation.” The Lie algebra $\mathfrak{X}(M)$ is infinite-dimensional (for $\dim M \ge 1$). The finite-dimensional Lie algebras of the [[§50 Lie Groups and Left-Invariant Vector Fields|next section]] sit inside it.

> [!example] Example §49.3: The Cross Product
> $\mathbb{R}^3$ with the [[§96 The Cross Product#^def-96-1|cross product]] is a [[§49 Lie Bracket and Lie Algebra#^def-49-2|Lie algebra]], and the [[§25 The Geometric Tangent Space#^def-25-3|hat map]] of [[§25 The Geometric Tangent Space#^def-25-3|Definition §25.3]] is an isomorphism of Lie algebras onto $\operatorname{Skew}(3, \mathbb{R}) = \mathfrak{so}(3)$ with the [[§49 Lie Bracket and Lie Algebra#^ex-49-2|matrix commutator]]:
>
> $$
> [\hat a, \hat b] = \hat a \hat b - \hat b \hat a = \widehat{a \times b} .
> $$

^ex-49-3

> [!proof]+ Proof
> *(Lecture 16 mentioned only that the cross product satisfies the Jacobi identity — “if you want to be really mean to your 215 students, give them the Jacobi identity for the cross product. Don't do that.” The proof via the hat map is filled in.)* By the [[§96 The Cross Product#^thm-96-8|identity]] $u \times (v \times w) = v\,(u \cdot w) - w\,(u \cdot v)$, for every $x \in \mathbb{R}^3$
>
> $$
> [\hat a, \hat b]\, x = a \times (b \times x) - b \times (a \times x) = b\,(a \cdot x) - a\,(b \cdot x) = (a \times b) \times x = \widehat{a \times b}\, x .
> $$
>
> $\operatorname{Skew}(3,\mathbb{R})$ is closed under the commutator ($[A,B]^{\mathsf T} = [B^{\mathsf T}, A^{\mathsf T}] = [B, A] = -[A,B]$ for skew $A, B$), so it is a Lie algebra by [[§49 Lie Bracket and Lie Algebra#^ex-49-2|Example §49.2]]. The hat map is a linear isomorphism carrying $\times$ to the commutator, so the cross product inherits bilinearity, skew-symmetry and the Jacobi identity — without the big computation.

^pf-ex-49-3

*Uses:* [[§25 The Geometric Tangent Space#^def-25-3|Def. §25.3]], [[§96 The Cross Product#^thm-96-8|Calc §96.8]], [[§49 Lie Bracket and Lie Algebra#^ex-49-2|Ex. §49.2]], [[§49 Lie Bracket and Lie Algebra#^def-49-2|Def. §49.2]]

> [!remark]- Connections
> - The cross product and its algebraic properties, proved by components: [[§96 The Cross Product#^def-96-1|Calc Def. §96.1]], [[§96 The Cross Product#^thm-96-8|Calc §96.8]].
> - The same computation for the infinitesimal rotations of quantum mechanics: [[§C5.1 Rotations and the Angular-Momentum Commutation Relations#^thm-c5-1-1|QM Theorem §C5.1.1]], with [[§C5.1 Rotations and the Angular-Momentum Commutation Relations#^rem-c5-1-1|QM ★ Remark: The Lie algebra of SO(3)]].

The classical groups through the course: defined in [[§11 Topological Groups and Classical Matrix Groups|Topological Groups and Classical Matrix Groups]], with the examples of [[§16 The Classical Groups|The Classical Groups]]; topological manifolds as level sets in [[§12 The Classical Groups Are Topological Manifolds#^thm-12-6|Classical Groups Are Manifolds]]; $\mathrm{SO}(2)$ and $\mathrm{SO}(3)$ acting on $\mathbb{R}^2$ and $\mathbb{R}^3$ in [[§13 Group Actions and Orbit Spaces#^ex-13-4|the rotations of the plane]] and [[§13 Group Actions and Orbit Spaces#^ex-13-5|the rotations of space]], and $\mathrm{SO}(3)$ on $S^2$ in [[§14 Homogeneous Spaces#^ex-14-2|the isotropy of the north pole]] and [[§14 Homogeneous Spaces#^ex-14-3|the sphere as a homogeneous space]]; $\mathrm{O}(n)$ acting on the Grassmannians in [[§15 The Topology of G∕H and Real Grassmannians#^cor-15-8|Grassmannians as Homogeneous Spaces]]; smooth manifolds in [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-23-1|the orthogonal group]] and [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-23-2|the unitary group]]; their tangent spaces at the identity in [[§25 The Geometric Tangent Space#^thm-25-5|The Classical Groups]], with [[§25 The Geometric Tangent Space#^ex-25-4|the infinitesimal rotations]]; the double cover $\mathrm{SU}(2) \to \mathrm{SO}(3)$ in [[§42 SU(2) → SO(3)꞉ The Double Cover#^thm-42-4|The Double Cover]]; the Lie algebra $\mathfrak{so}(3)$ and the cross product in [[§49 Lie Bracket and Lie Algebra#^ex-49-3|Ex. §49.3]]; and Lie groups in [[§50 Lie Groups and Left-Invariant Vector Fields#^prop-50-1|§50.1]].

## Related Vector Fields

*Lecture 17. “Back to vector fields … we're currently taking the operator point of view. Later on, we'll talk about them as generators of dynamics.” Recap: every [[§48 Vector Fields#^def-48-1|vector field]] defines a [[§48 Vector Fields#^def-48-5|derivation]] of $C^\infty(M)$, and conversely ([[§48 Vector Fields#^lem-48-2|Lemma §48.2]], [[§48 Vector Fields#^prop-48-7|Proposition §48.7]]); so the [[§49 Lie Bracket and Lie Algebra#^def-49-1|commutator]] of two fields is again a field ([[§49 Lie Bracket and Lie Algebra#^lem-49-1|Lemma §49.1]]). Officially, a vector field is a smooth section of the tangent bundle ([[§48 Vector Fields#^def-48-1|Definition §48.1]]).*

> [!remark] Remark: Vector Fields Do Not Push Forward
> Given a [[§19 Smooth Functions and Smooth Maps#^def-19-3|smooth map]] $F : M \to N$, “in general, we cannot push forward or pull back vector fields”: vector fields have no functorial properties, “as opposed to [[§47 One-Forms#^def-47-1|differential forms]], … they can always be [[§47 One-Forms#^def-47-4|pulled back]].” Single tangent vectors *can* be [[§28 Derivations and the Abstract Tangent Space#^def-28-6|pushed forward]], by $dF_p$; the trouble is assembling the results into a field on $N$.
> - If $F$ is not injective, two points $p_1 \ne p_2$ with $F(p_1) = F(p_2) = q$ give two candidates $dF_{p_1}(\mathbf{X}_{p_1})$ and $dF_{p_2}(\mathbf{X}_{p_2})$ at $q$, in general different: “which one am I going to push …? It's a multi-valued object.”
> - If $F$ is not surjective, a point $q' \notin F(M)$ gets no candidate at all: “I would have no way of defining [the field] outside the image.”

^rem-49-1

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

^rem-49-2

> [!definition] Definition §49.3: Pushforward of a Vector Field by a Diffeomorphism
> Let $F : M \to N$ be a [[§19 Smooth Functions and Smooth Maps#^def-19-4|diffeomorphism]] and $\mathbf{X} \in \mathfrak{X}(M)$. The **pushforward** of $\mathbf{X}$ is the [[§36 Fibrations#^def-36-2|section]] $F_{\ast}\mathbf{X}$ of $TN$ given by
>
> $$
> (F_{\ast}\mathbf{X})_q = dF_{F^{-1}(q)}\big(\mathbf{X}_{F^{-1}(q)}\big), \qquad q \in N .
> $$
>
> *Lee: Ch. 8, Pushforwards of Vector Fields*

^def-49-3

It is smooth, so $F_{\ast}\mathbf{X} \in \mathfrak{X}(N)$: this is [[§49 Lie Bracket and Lie Algebra#^prop-49-6|Proposition §49.6]] below. “However, it can happen that you have … fields that are related by $F$, that correspond to one another … It's something that you don't construct. It's something that happens.”

> [!definition] Definition §49.4: $F$-Related Vector Fields
> Let $F : M \to N$ be [[§19 Smooth Functions and Smooth Maps#^def-19-3|smooth]], $\mathbf{X} \in \mathfrak{X}(M)$ and $\mathbf{Y} \in \mathfrak{X}(N)$. Then $\mathbf{X}$ and $\mathbf{Y}$ are **$F$-related** if
>
> $$
> dF_p(\mathbf{X}_p) = \mathbf{Y}_{F(p)} \in T_{F(p)}N \qquad \text{for every } p \in M .
> $$
>
> *Lee: Ch. 8, Vector Fields and Smooth Maps*

^def-49-4

The definition was completed in class by a student: push the value of $\mathbf{X}$ at $p$ forward, “and if it happens that every time I do that, I get the value of $\mathbf{Y}$ at the same point, then we say that the two vector fields are related by $F$.” No injectivity or surjectivity is assumed. Points outside $F(M)$ impose nothing on $\mathbf{Y}$, and two points with the same image must push forward to the same vector. “It's a very useful notion at times.”

> [!example] Example §49.4: Fields Related by a Projection
> Let $\pi : \mathbb{R}^2 \to \mathbb{R}$, $\pi(x, y) = x$, and $\mathbf{Y} = b(x)\, \dfrac{d}{dx}$ with $b \in C^\infty(\mathbb{R})$ — “any vector field on $\mathbb{R}$ I can write like this.” The fields on $\mathbb{R}^2$ that are [[§49 Lie Bracket and Lie Algebra#^def-49-4|π-related]] to $\mathbf{Y}$ are exactly
>
> $$
> \mathbf{X} = b(x)\, \frac{\partial}{\partial x} + c(x, y)\, \frac{\partial}{\partial y}, \qquad c \in C^\infty(\mathbb{R}^2) \text{ arbitrary.}
> $$

^ex-49-4

> [!proof]+ Proof
> *(Lecture 17, as a question to the class: “What can I put in the blanks here?” The first component “has to be this guy”; the second, “anything”. The computation is filled in.)* Write $\mathbf{X} = a\, \partial_x + c\, \partial_y$. For $g \in C^\infty(\mathbb{R})$, $d\pi\big(\partial_x|_{(x,y)}\big)[g] = \partial_x (g \circ \pi)(x,y) = g'(x)$ and $d\pi\big(\partial_y|_{(x,y)}\big)[g] = \partial_y\, g(x) = 0$. So $d\pi_{(x,y)}(\mathbf{X}_{(x,y)}) = a(x, y)\, \frac{d}{dx}\big|_x$, and this equals $\mathbf{Y}_x = b(x)\, \frac{d}{dx}\big|_x$ for all $(x, y)$ exactly when $a(x, y) = b(x)$.

^pf-ex-49-4

*Uses:* [[§49 Lie Bracket and Lie Algebra#^def-49-4|Def. §49.4]], [[§28 Derivations and the Abstract Tangent Space#^def-28-6|Def. §28.6]], [[§48 Vector Fields#^prop-48-1|§48.1]]

“All I care about is the horizontal component … they all should be the same” along each vertical line, the fibre $\pi^{-1}(x)$, “corresponding to the value down here.”

![[m591-49-3.svg]]
*Fields on $\mathbb{R}^2$ that are $\pi$-related to $\mathbf{Y} = b(x)\,\frac{d}{dx}$: along each fibre $\pi^{-1}(x)$ (dashed) the horizontal part (dotted) is $b(x)$, and the vertical part is arbitrary.*

*The operator viewpoint.* The definition is geometric — “arrows”. There is an equivalent characterization in terms of operators, using the pullback of functions, $F^{\ast}g = g \circ F$.

> [!theorem] Proposition §49.5: Related Fields as Operators
> Let $F : M \to N$ be [[§19 Smooth Functions and Smooth Maps#^def-19-3|smooth]], $\mathbf{X} \in \mathfrak{X}(M)$ and $\mathbf{Y} \in \mathfrak{X}(N)$. Then $\mathbf{X}$ and $\mathbf{Y}$ are [[§49 Lie Bracket and Lie Algebra#^def-49-4|F-related]] if and only if
>
> $$
> \mathbf{X}(g \circ F) = (\mathbf{Y}g) \circ F \qquad \text{for every } g \in C^\infty(N),
> $$
>
> that is, $\mathbf{X} \circ F^{\ast} = F^{\ast} \circ \mathbf{Y}$: the pullback $F^{\ast}$ intertwines $\mathbf{X}$ and $\mathbf{Y}$ as [[§48 Vector Fields#^def-48-5|derivations]].
>
> *Lee: Proposition 8.16*

^prop-49-5

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
> If the fields are $F$-related the right-hand sides agree, for every $g$ and $p$. Conversely, if the left-hand sides agree for every $g \in C^\infty(N)$, the two [[§28 Derivations and the Abstract Tangent Space#^def-28-1|derivations]] $dF_p(\mathbf{X}_p)$ and $\mathbf{Y}_{F(p)}$ at $F(p)$ agree on every global function, hence on every [[§27 Germs#^def-27-2|germ]] at $F(p)$, since every germ has a global representative ([[§48 Vector Fields#^cor-48-4|Corollary §48.4]]); so they are equal. “It's a trivial if and only if once you realize” this.

^pf-49-5

*Uses:* [[§49 Lie Bracket and Lie Algebra#^def-49-4|Def. §49.4]], [[§28 Derivations and the Abstract Tangent Space#^def-28-6|Def. §28.6]], [[§28 Derivations and the Abstract Tangent Space#^def-28-1|Def. §28.1]], [[§48 Vector Fields#^cor-48-4|§48.4]]

> [!theorem] Proposition §49.6: Pushforward by a Diffeomorphism
> Let $F : M \to N$ be a [[§19 Smooth Functions and Smooth Maps#^def-19-4|diffeomorphism]] and $\mathbf{X} \in \mathfrak{X}(M)$. Then the [[§49 Lie Bracket and Lie Algebra#^def-49-3|pushforward]] $F_{\ast}\mathbf{X}$ is smooth, it is the unique vector field on $N$ that is [[§49 Lie Bracket and Lie Algebra#^def-49-4|F-related]] to $\mathbf{X}$, and for every $g \in C^\infty(N)$
>
> $$
> (F_{\ast}\mathbf{X})\, g = \big(\mathbf{X}(g \circ F)\big) \circ F^{-1} .
> $$
>
> *Lee: Proposition 8.19, Corollary 8.21*

^prop-49-6

> [!proof]+ Proof
> *(Not from lecture; filled in.)* For $q \in N$ put $p = F^{-1}(q)$. Then $(F_{\ast}\mathbf{X})_q[g] = dF_p(\mathbf{X}_p)[g] = \mathbf{X}_p[g \circ F] = \mathbf{X}(g \circ F)(F^{-1}(q))$, which is the formula. Its right side is smooth, as $\mathbf{X}(g \circ F)$ is smooth ([[§48 Vector Fields#^lem-48-2|Lemma §48.2]]) and $F^{-1}$ is smooth; so $F_{\ast}\mathbf{X}$ is smooth by [[§48 Vector Fields#^lem-48-8|Lemma §48.8]]. It is $F$-related to $\mathbf{X}$ by its definition. If $\mathbf{Y}$ is also $F$-related to $\mathbf{X}$, then $\mathbf{Y}_q = \mathbf{Y}_{F(p)} = dF_p(\mathbf{X}_p) = (F_{\ast}\mathbf{X})_q$ for every $q$, since $F$ is onto.

^pf-49-6

*Uses:* [[§49 Lie Bracket and Lie Algebra#^def-49-3|Def. §49.3]], [[§49 Lie Bracket and Lie Algebra#^def-49-4|Def. §49.4]], [[§28 Derivations and the Abstract Tangent Space#^def-28-6|Def. §28.6]], [[§19 Smooth Functions and Smooth Maps#^def-19-4|Def. §19.4]], [[§48 Vector Fields#^lem-48-2|§48.2]], [[§19 Smooth Functions and Smooth Maps#^lem-19-4|§19.4]], [[§48 Vector Fields#^lem-48-8|§48.8]]

*“Now the reason I wanted to do it this way”* — through operators — is the following proposition.

> [!theorem] Proposition §49.7: Naturality of the Bracket
> Let $F : M \to N$ be [[§19 Smooth Functions and Smooth Maps#^def-19-3|smooth]], $\mathbf{X}_1, \mathbf{X}_2 \in \mathfrak{X}(M)$ and $\mathbf{Y}_1, \mathbf{Y}_2 \in \mathfrak{X}(N)$. If $\mathbf{X}_i$ is [[§49 Lie Bracket and Lie Algebra#^def-49-4|F-related]] to $\mathbf{Y}_i$ for $i = 1, 2$, then the [[§49 Lie Bracket and Lie Algebra#^def-49-1|bracket]] $[\mathbf{X}_1, \mathbf{X}_2]$ is $F$-related to $[\mathbf{Y}_1, \mathbf{Y}_2]$.
>
> *Lee: Proposition 8.30*

^prop-49-7

> [!proof]+ Proof
> *(Omitted in Lecture 17 as an exercise: “it's just a matter of chasing the definitions … being $F$-related means that $F^{\ast}$ commutes with the derivations. So you just play with the symbols; it all comes out.” Filled in.)* Let $g \in C^\infty(N)$. Applying [[§49 Lie Bracket and Lie Algebra#^prop-49-5|Proposition §49.5]] twice,
>
> $$
> \mathbf{X}_1\mathbf{X}_2(g \circ F) = \mathbf{X}_1\big((\mathbf{Y}_2 g) \circ F\big) = (\mathbf{Y}_1\mathbf{Y}_2 g) \circ F ,
> $$
>
> and in the same way $\mathbf{X}_2\mathbf{X}_1(g \circ F) = (\mathbf{Y}_2\mathbf{Y}_1 g) \circ F$. Subtracting, $[\mathbf{X}_1, \mathbf{X}_2](g \circ F) = \big([\mathbf{Y}_1, \mathbf{Y}_2]\, g\big) \circ F$, and [[§49 Lie Bracket and Lie Algebra#^prop-49-5|Proposition §49.5]] again gives the claim.

^pf-49-7

*Uses:* [[§49 Lie Bracket and Lie Algebra#^prop-49-5|§49.5]], [[§49 Lie Bracket and Lie Algebra#^def-49-1|Def. §49.1]], [[§49 Lie Bracket and Lie Algebra#^lem-49-1|§49.1]]

On omitting this proof: “In a class like this, you cannot prove everything. First of all, there is no time, and second, you would be bored to tears. … But on the other hand, if we just say, oh, you can read the proof, then you don't get a feeling for the subject. So there is a line there somewhere, or a zone, where you have to prove enough, but not too much.” Feedback on where that line should sit is “always welcome.”

> [!theorem] Corollary §49.8: Diffeomorphisms Preserve Brackets
> If $F : M \to N$ is a [[§19 Smooth Functions and Smooth Maps#^def-19-4|diffeomorphism]] and $\mathbf{X}_1, \mathbf{X}_2 \in \mathfrak{X}(M)$, then $F_{\ast}[\mathbf{X}_1, \mathbf{X}_2] = [F_{\ast}\mathbf{X}_1, F_{\ast}\mathbf{X}_2]$.
>
> *Lee: Corollary 8.31*

^cor-49-8

> [!proof]+ Proof
> *(Not from lecture; filled in.)* Each $\mathbf{X}_i$ is $F$-related to $F_{\ast}\mathbf{X}_i$, so $[\mathbf{X}_1, \mathbf{X}_2]$ is $F$-related to $[F_{\ast}\mathbf{X}_1, F_{\ast}\mathbf{X}_2]$ by [[§49 Lie Bracket and Lie Algebra#^prop-49-7|Proposition §49.7]]. The only field $F$-related to $[\mathbf{X}_1, \mathbf{X}_2]$ is $F_{\ast}[\mathbf{X}_1, \mathbf{X}_2]$ ([[§49 Lie Bracket and Lie Algebra#^prop-49-6|Proposition §49.6]]).

^pf-49-8

*Uses:* [[§49 Lie Bracket and Lie Algebra#^prop-49-7|§49.7]], [[§49 Lie Bracket and Lie Algebra#^prop-49-6|§49.6]], [[§49 Lie Bracket and Lie Algebra#^def-49-3|Def. §49.3]], [[§49 Lie Bracket and Lie Algebra#^def-49-4|Def. §49.4]]
