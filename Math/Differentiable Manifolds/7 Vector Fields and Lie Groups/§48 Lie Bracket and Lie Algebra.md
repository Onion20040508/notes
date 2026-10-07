---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 7
section: 48
tags: [differentiable-manifolds, math591]
---
← [[§47 Vector Fields]] · ↑ [[· 7 Vector Fields and Lie Groups]] · [[§49 Lie Groups and Left-Invariant Vector Fields]] →

*Stage: fields — Two vector fields, composed as operators, give a second-order operator; their commutator cancels the second derivatives and is again a vector field, so $\mathfrak{X}(M)$ is a Lie algebra.*

*Lecture 16. “Who cares? There is one reason we care … when we look at commutators.”*

> [!definition] Definition §48.1: The Lie Bracket of Vector Fields
> For $\mathbf{X}, \mathbf{Y} \in \mathfrak{X}(M)$, regarded as [[§47 Vector Fields#^lem-47-2|operators]] on $C^\infty(M)$ ([[§47 Vector Fields#^def-47-4|Definition §47.4]]), the **commutator** or **Lie bracket** is the operator
>
> $$
> [\mathbf{X}, \mathbf{Y}](f) = \mathbf{X}\big(\mathbf{Y}(f)\big) - \mathbf{Y}\big(\mathbf{X}(f)\big), \qquad f \in C^\infty(M).
> $$
>
> *Lee: Ch. 8, Lie Brackets*

^def-48-1

Each composite $\mathbf{X} \circ \mathbf{Y}$ is a [[§47 Vector Fields#^def-47-11|second-order operator]] — “you get second derivatives in local coordinates” — but “something very, very nice happens when you look at the commutator.”

> [!theorem] Lemma §48.1: The Bracket of Vector Fields Is a Vector Field
> $[\mathbf{X}, \mathbf{Y}]$ is a [[§47 Vector Fields#^def-47-5|derivation]] of $C^\infty(M)$; hence, by [[§47 Vector Fields#^prop-47-7|Proposition §47.7]], it is a [[§47 Vector Fields#^def-47-1|vector field]].
>
> *Lee: Lemma 8.25*

^lem-48-1

> [!proof]+ Proof
> *(Lecture 16 — “tedious algebra … the key thing is the product rule.”)* Linearity is clear, as a difference of composites of linear maps. For the product rule, apply the [[§47 Vector Fields#^lem-47-2|product rule]] for $\mathbf{Y}$ and then for $\mathbf{X}$:
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

^pf-48-1

*Uses:* [[§48 Lie Bracket and Lie Algebra#^def-48-1|Def. §48.1]], [[§47 Vector Fields#^def-47-5|Def. §47.5]], [[§47 Vector Fields#^lem-47-2|§47.2]], [[§47 Vector Fields#^prop-47-7|§47.7]]

> [!example] Example §48.1: A Bracket in the Plane
> On $\mathbb{R}^2$ with coordinates $(x, y)$, let $\mathbf{X} = a\, \partial_x$ and $\mathbf{Y} = b\, \partial_y$ with $a, b \in C^\infty(\mathbb{R}^2)$. Then
>
> $$
> [\mathbf{X}, \mathbf{Y}] = a\, \frac{\partial b}{\partial x}\, \frac{\partial}{\partial y} \;-\; b\, \frac{\partial a}{\partial y}\, \frac{\partial}{\partial x} .
> $$

^ex-48-1

> [!proof]+ Proof
> *(Lecture 16 — “an exercise in multivariable calculus.”)* Apply both composites to a function $f$ and use the product rule:
>
> $$
> \mathbf{X}\mathbf{Y}f = a\, \partial_x(b\, \partial_y f) = a\, \frac{\partial b}{\partial x}\, \frac{\partial f}{\partial y} + ab\, \frac{\partial^2 f}{\partial x\, \partial y}, \qquad
> \mathbf{Y}\mathbf{X}f = b\, \frac{\partial a}{\partial y}\, \frac{\partial f}{\partial x} + ba\, \frac{\partial^2 f}{\partial y\, \partial x} .
> $$
>
> The second derivatives are [[Schwarz–Clairaut Theorem|equal]] and cancel in the difference, leaving the stated first-order operator.

^pf-ex-48-1

*Uses:* [[§48 Lie Bracket and Lie Algebra#^def-48-1|Def. §48.1]], [[Schwarz–Clairaut Theorem|452 §6.1]]

> [!theorem] Proposition §48.2: The Bracket in Coordinates
> In a chart with $\mathbf{X} = \sum_i X^i\, \partial_i$ and $\mathbf{Y} = \sum_i Y^i\, \partial_i$, where $\partial_i = \partial/\partial x^i$,
>
> $$
> [\mathbf{X}, \mathbf{Y}] = \sum_j \big( \mathbf{X}(Y^j) - \mathbf{Y}(X^j) \big)\, \partial_j = \sum_j \sum_i \Big( X^i\, \frac{\partial Y^j}{\partial x^i} - Y^i\, \frac{\partial X^j}{\partial x^i} \Big)\, \partial_j .
> $$
>
> *Lee: Proposition 8.26*

^prop-48-2

> [!proof]+ Proof
> *(Not from lecture; filled in — [[§48 Lie Bracket and Lie Algebra#^ex-48-1|Example §48.1]] is the case $\mathbf{X} = a\,\partial_x$, $\mathbf{Y} = b\,\partial_y$.)* The $j$-th coefficient of a vector field is its value on the coordinate function $x^j$ ([[§47 Vector Fields#^prop-47-1|Proposition §47.1]]), and $[\mathbf{X}, \mathbf{Y}](x^j) = \mathbf{X}(\mathbf{Y}x^j) - \mathbf{Y}(\mathbf{X}x^j) = \mathbf{X}(Y^j) - \mathbf{Y}(X^j)$. The second form expands $\mathbf{X}(Y^j) = \sum_i X^i\, \partial Y^j/\partial x^i$.

^pf-48-2

*Uses:* [[§48 Lie Bracket and Lie Algebra#^def-48-1|Def. §48.1]], [[§48 Lie Bracket and Lie Algebra#^lem-48-1|§48.1]], [[§47 Vector Fields#^prop-47-1|§47.1]]

> [!definition] Definition §48.2: Lie Algebra
> A (real) **Lie algebra** $\mathfrak{g}$ is a real [[§2 Definition of Vector Space#^ladr-1-20|vector space]] together with a [[§38 Tensor Products#^ladr-9-77|bilinear]], skew-symmetric operation $[\cdot,\cdot] : \mathfrak{g} \times \mathfrak{g} \to \mathfrak{g}$, the **Lie bracket**, satisfying the **Jacobi identity**
>
> $$
> [X, [Y, Z]] + [Y, [Z, X]] + [Z, [X, Y]] = 0 \qquad \text{for all } X, Y, Z \in \mathfrak{g}.
> $$
>
> *Lee: Ch. 8, Lie Algebras*

^def-48-2

> [!remark]- Connections
> - In classical mechanics the Poisson bracket is bilinear, antisymmetric and satisfies the Jacobi identity ([[§B8.1 Poisson Brackets#^thm-b8-1-2|CM Theorem §B8.1.2]]), so the phase-space functions form a Lie algebra: [[§B8.1 Poisson Brackets#^rem-b8-1-1|CM Remark: The structure behind the four rules]].
> - In quantum mechanics the commutator of operators has the same algebra, Jacobi identity included: [[§B2.4 Commutators and the Generalized Uncertainty Principle#^thm-b2-4-1|QM Theorem §B2.4.1]].

The three terms come from one by permuting $X, Y, Z$ cyclically: “move $Y$ to the left position, $Z$ one over to the left, and $X$ jumps to the last position.”

> [!theorem] Proposition §48.3: Commutators of an Associative Product
> Let $A$ be a real vector space with a bilinear *associative* product $(X, Y) \mapsto X \ast Y$. Then the commutator $[X, Y] = X \ast Y - Y \ast X$ is bilinear, skew-symmetric, and satisfies the [[§48 Lie Bracket and Lie Algebra#^def-48-2|Jacobi identity]]; so $(A, [\cdot,\cdot])$ is a [[§48 Lie Bracket and Lie Algebra#^def-48-2|Lie algebra]].

^prop-48-3

> [!proof]+ Proof
> *(Stated in Lecture 16 as “a general fact”; filled in. “The key thing is that it be an associative product.”)* Bilinearity and skew-symmetry are immediate. By associativity, triple products can be written without parentheses, and
>
> $$
> [X, [Y, Z]] = XYZ - XZY - YZX + ZYX .
> $$
>
> Permuting cyclically gives $[Y,[Z,X]] = YZX - YXZ - ZXY + XZY$ and $[Z,[X,Y]] = ZXY - ZYX - XYZ + YXZ$. In the sum each of the six words $XYZ, XZY, YZX, ZYX, YXZ, ZXY$ appears once with each sign, so the sum is $0$.

^pf-48-3

*Uses:* [[§48 Lie Bracket and Lie Algebra#^def-48-2|Def. §48.2]]

> [!example] Example §48.2: Matrices
> $\operatorname{Mat}(n, \mathbb{R})$, with the commutator $[A, B] = AB - BA$ of matrix multiplication, is a [[§48 Lie Bracket and Lie Algebra#^def-48-2|Lie algebra]], by [[§48 Lie Bracket and Lie Algebra#^prop-48-3|Proposition §48.3]].

^ex-48-2

> [!theorem] Corollary §48.4: Vector Fields Form a Lie Algebra
> $\big(\mathfrak{X}(M), [\cdot,\cdot]\big)$ is a [[§48 Lie Bracket and Lie Algebra#^def-48-2|Lie algebra]].
>
> *Lee: Proposition 8.28*

^cor-48-4

> [!proof]+ Proof
> *(Lecture 16: the bracket of fields “comes from the product, which is the composition, which is associative.” Filled in.)* The linear operators on $C^\infty(M)$ form an associative algebra under composition, so by [[§48 Lie Bracket and Lie Algebra#^prop-48-3|Proposition §48.3]] their commutator satisfies the Jacobi identity. By [[§48 Lie Bracket and Lie Algebra#^lem-48-1|Lemma §48.1]], $\mathfrak{X}(M)$, identified with the derivations, is closed under it; so the identity holds on $\mathfrak{X}(M)$.

^pf-48-4

*Uses:* [[§48 Lie Bracket and Lie Algebra#^def-48-1|Def. §48.1]], [[§48 Lie Bracket and Lie Algebra#^def-48-2|Def. §48.2]], [[§48 Lie Bracket and Lie Algebra#^prop-48-3|§48.3]], [[§48 Lie Bracket and Lie Algebra#^lem-48-1|§48.1]], [[§47 Vector Fields#^lem-47-2|§47.2]], [[§47 Vector Fields#^prop-47-7|§47.7]]

“Which I don't recommend you check by hand. It's a big computation.” The Lie algebra $\mathfrak{X}(M)$ is infinite-dimensional (for $\dim M \ge 1$). The finite-dimensional Lie algebras of the [[§49 Lie Groups and Left-Invariant Vector Fields|next section]] sit inside it.

> [!example] Example §48.3: The Cross Product
> $\mathbb{R}^3$ with the [[§96 The Cross Product#^def-96-1|cross product]] is a [[§48 Lie Bracket and Lie Algebra#^def-48-2|Lie algebra]], and the [[§25 The Geometric Tangent Space#^def-25-3|hat map]] of [[§25 The Geometric Tangent Space#^def-25-3|Definition §25.3]] is an isomorphism of Lie algebras onto $\operatorname{Skew}(3, \mathbb{R}) = \mathfrak{so}(3)$ with the [[§48 Lie Bracket and Lie Algebra#^ex-48-2|matrix commutator]]:
>
> $$
> [\hat a, \hat b] = \hat a \hat b - \hat b \hat a = \widehat{a \times b} .
> $$

^ex-48-3

> [!proof]+ Proof
> *(Lecture 16 mentioned only that the cross product satisfies the Jacobi identity — “if you want to be really mean to your 215 students, give them the Jacobi identity for the cross product. Don't do that.” The proof via the hat map is filled in.)* By the [[§96 The Cross Product#^thm-96-8|identity]] $u \times (v \times w) = v\,(u \cdot w) - w\,(u \cdot v)$, for every $x \in \mathbb{R}^3$
>
> $$
> [\hat a, \hat b]\, x = a \times (b \times x) - b \times (a \times x) = b\,(a \cdot x) - a\,(b \cdot x) = (a \times b) \times x = \widehat{a \times b}\, x .
> $$
>
> $\operatorname{Skew}(3,\mathbb{R})$ is closed under the commutator ($[A,B]^{\mathsf T} = [B^{\mathsf T}, A^{\mathsf T}] = [B, A] = -[A,B]$ for skew $A, B$), so it is a Lie algebra by [[§48 Lie Bracket and Lie Algebra#^ex-48-2|Example §48.2]]. The hat map is a linear isomorphism carrying $\times$ to the commutator, so the cross product inherits bilinearity, skew-symmetry and the Jacobi identity — without the big computation.

^pf-ex-48-3

*Uses:* [[§25 The Geometric Tangent Space#^def-25-3|Def. §25.3]], [[§96 The Cross Product#^thm-96-8|Calc §96.8]], [[§48 Lie Bracket and Lie Algebra#^ex-48-2|Ex. §48.2]], [[§48 Lie Bracket and Lie Algebra#^def-48-2|Def. §48.2]]

> [!remark]- Connections
> - The cross product and its algebraic properties, proved by components: [[§96 The Cross Product#^def-96-1|Calc Def. §96.1]], [[§96 The Cross Product#^thm-96-8|Calc §96.8]].
> - The same computation for the infinitesimal rotations of quantum mechanics: [[§C5.1 Rotations and the Angular-Momentum Commutation Relations#^thm-c5-1-1|QM Theorem §C5.1.1]], with [[§C5.1 Rotations and the Angular-Momentum Commutation Relations#^rem-c5-1-1|QM ★ Remark: The Lie algebra of SO(3)]].

The classical groups through the course: defined in [[§11 Topological Groups and Classical Matrix Groups|Topological Groups and Classical Matrix Groups]], with the examples of [[§16 The Classical Groups|The Classical Groups]]; topological manifolds as level sets in [[§12 The Classical Groups Are Topological Manifolds#^thm-12-6|Classical Groups Are Manifolds]]; $\mathrm{SO}(2)$ and $\mathrm{SO}(3)$ acting on $\mathbb{R}^2$ and $\mathbb{R}^3$ in [[§13 Group Actions and Orbit Spaces#^ex-13-4|the rotations of the plane]] and [[§13 Group Actions and Orbit Spaces#^ex-13-5|the rotations of space]], and $\mathrm{SO}(3)$ on $S^2$ in [[§14 Homogeneous Spaces#^ex-14-2|the isotropy of the north pole]] and [[§14 Homogeneous Spaces#^ex-14-3|the sphere as a homogeneous space]]; $\mathrm{O}(n)$ acting on the Grassmannians in [[§15 The Topology of G∕H and Real Grassmannians#^cor-15-8|Grassmannians as Homogeneous Spaces]]; smooth manifolds in [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-23-1|the orthogonal group]] and [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-23-2|the unitary group]]; their tangent spaces at the identity in [[§25 The Geometric Tangent Space#^thm-25-5|The Classical Groups]], with [[§25 The Geometric Tangent Space#^ex-25-4|the infinitesimal rotations]]; the double cover $\mathrm{SU}(2) \to \mathrm{SO}(3)$ in [[§41 SU(2) → SO(3)꞉ The Double Cover#^thm-41-4|The Double Cover]]; the Lie algebra $\mathfrak{so}(3)$ and the cross product in [[§48 Lie Bracket and Lie Algebra#^ex-48-3|Ex. §48.3]]; and Lie groups in [[§49 Lie Groups and Left-Invariant Vector Fields#^prop-49-1|§49.1]].
