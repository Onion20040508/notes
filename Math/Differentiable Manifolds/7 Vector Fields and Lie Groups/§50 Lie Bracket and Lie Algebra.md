---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 7
section: 50
tags: [differentiable-manifolds, math591]
---
← [[§49 Differential Operators]] · ↑ [[· 7 Vector Fields and Lie Groups]] · [[§51 Related Vector Fields]] →

*Stage: fields — Two vector fields, composed as operators, give a second-order operator; their commutator cancels the second derivatives and is again a vector field, so $\mathfrak{X}(M)$ is a Lie algebra.*

*Lecture 16. “Who cares? There is one reason we care … when we look at commutators.”*

> [!definition] Definition §50.1: The Lie Bracket of Vector Fields
> For $\mathbf{X}, \mathbf{Y} \in \mathfrak{X}(M)$, regarded as [[§48 Vector Fields#^lem-48-3|operators]] on $C^\infty(M)$ ([[§48 Vector Fields#^def-48-4|Definition §48.4]]), the **commutator** or **Lie bracket** is the operator
>
> $$
> [\mathbf{X}, \mathbf{Y}](f) = \mathbf{X}\big(\mathbf{Y}(f)\big) - \mathbf{Y}\big(\mathbf{X}(f)\big), \qquad f \in C^\infty(M).
> $$
>
> *Lee: Ch. 8, Lie Brackets*

^def-50-1

Each composite $\mathbf{X} \circ \mathbf{Y}$ is a second-order operator, in $\mathrm{Diff}_2(M)$ ([[§49 Differential Operators#^def-49-3|Definition §49.3]]) — “you get second derivatives in local coordinates” — but “something very, very nice happens when you look at the commutator.”

> [!theorem] Lemma §50.1: The Bracket of Vector Fields Is a Vector Field
> $[\mathbf{X}, \mathbf{Y}]$ is a [[§48 Vector Fields#^def-48-5|derivation]] of $C^\infty(M)$; hence, by [[§48 Vector Fields#^prop-48-7|Proposition §48.7]], it is a [[§48 Vector Fields#^def-48-1|vector field]].
>
> *Lee: Lemma 8.25*

^lem-50-1

> [!proof]+ Proof
> *(Lecture 16 — “tedious algebra … the key thing is the product rule.”)* Linearity is clear, as a difference of composites of linear maps. For the product rule, apply the [[§48 Vector Fields#^lem-48-3|product rule]] for $\mathbf{Y}$ and then for $\mathbf{X}$:
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

^pf-50-1

*Uses:* [[§50 Lie Bracket and Lie Algebra#^def-50-1|Def. §50.1]], [[§48 Vector Fields#^def-48-5|Def. §48.5]], [[§48 Vector Fields#^lem-48-3|§48.3]], [[§48 Vector Fields#^prop-48-7|§48.7]]

> [!example] Example §50.1: A Bracket in the Plane
> On $\mathbb{R}^2$ with coordinates $(x, y)$, let $\mathbf{X} = a\, \partial_x$ and $\mathbf{Y} = b\, \partial_y$ with $a, b \in C^\infty(\mathbb{R}^2)$. Then
>
> $$
> [\mathbf{X}, \mathbf{Y}] = a\, \frac{\partial b}{\partial x}\, \frac{\partial}{\partial y} \;-\; b\, \frac{\partial a}{\partial y}\, \frac{\partial}{\partial x} .
> $$

^ex-50-1

> [!proof]+ Proof
> *(Lecture 16 — “an exercise in multivariable calculus.”)* Apply both composites to a function $f$ and use the product rule:
>
> $$
> \mathbf{X}\mathbf{Y}f = a\, \partial_x(b\, \partial_y f) = a\, \frac{\partial b}{\partial x}\, \frac{\partial f}{\partial y} + ab\, \frac{\partial^2 f}{\partial x\, \partial y}, \qquad
> \mathbf{Y}\mathbf{X}f = b\, \frac{\partial a}{\partial y}\, \frac{\partial f}{\partial x} + ba\, \frac{\partial^2 f}{\partial y\, \partial x} .
> $$
>
> The second derivatives are [[Schwarz–Clairaut Theorem|equal]] and cancel in the difference, leaving the stated first-order operator.

^pf-ex-50-1

*Uses:* [[§50 Lie Bracket and Lie Algebra#^def-50-1|Def. §50.1]], [[Schwarz–Clairaut Theorem|452 §6.1]]

> [!theorem] Proposition §50.2: The Bracket in Coordinates
> In a chart with $\mathbf{X} = \sum_i X^i\, \partial_i$ and $\mathbf{Y} = \sum_i Y^i\, \partial_i$, where $\partial_i = \partial/\partial x^i$,
>
> $$
> [\mathbf{X}, \mathbf{Y}] = \sum_j \big( \mathbf{X}(Y^j) - \mathbf{Y}(X^j) \big)\, \partial_j = \sum_j \sum_i \Big( X^i\, \frac{\partial Y^j}{\partial x^i} - Y^i\, \frac{\partial X^j}{\partial x^i} \Big)\, \partial_j .
> $$
>
> *Lee: Proposition 8.26*

^prop-50-2

> [!proof]+ Proof
> *(Not from lecture; filled in — [[§50 Lie Bracket and Lie Algebra#^ex-50-1|Example §50.1]] is the case $\mathbf{X} = a\,\partial_x$, $\mathbf{Y} = b\,\partial_y$.)* The $j$-th coefficient of a vector field is its value on the coordinate function $x^j$ ([[§48 Vector Fields#^prop-48-1|Proposition §48.1]]), and $[\mathbf{X}, \mathbf{Y}](x^j) = \mathbf{X}(\mathbf{Y}x^j) - \mathbf{Y}(\mathbf{X}x^j) = \mathbf{X}(Y^j) - \mathbf{Y}(X^j)$. The second form expands $\mathbf{X}(Y^j) = \sum_i X^i\, \partial Y^j/\partial x^i$.

^pf-50-2

*Uses:* [[§50 Lie Bracket and Lie Algebra#^def-50-1|Def. §50.1]], [[§50 Lie Bracket and Lie Algebra#^lem-50-1|§50.1]], [[§48 Vector Fields#^prop-48-1|§48.1]]

> [!definition] Definition §50.2: Lie Algebra
> A (real) **Lie algebra** $\mathfrak{g}$ is a real [[§2 Definition of Vector Space#^ladr-1-20|vector space]] together with a [[§38 Tensor Products#^ladr-9-77|bilinear]], skew-symmetric operation $[\cdot,\cdot] : \mathfrak{g} \times \mathfrak{g} \to \mathfrak{g}$, the **Lie bracket**, satisfying the **Jacobi identity**
>
> $$
> [X, [Y, Z]] + [Y, [Z, X]] + [Z, [X, Y]] = 0 \qquad \text{for all } X, Y, Z \in \mathfrak{g}.
> $$
>
> *Lee: Ch. 8, Lie Algebras*

^def-50-2

> [!remark]- Connections
> - In classical mechanics the Poisson bracket is bilinear, antisymmetric and satisfies the Jacobi identity ([[§B8.1 Poisson Brackets#^thm-b8-1-2|CM Theorem §B8.1.2]]), so the phase-space functions form a Lie algebra: [[§B8.1 Poisson Brackets#^rem-b8-1-1|CM Remark: The structure behind the four rules]].
> - In quantum mechanics the commutator of operators has the same algebra, Jacobi identity included: [[§B2.4 Commutators and the Generalized Uncertainty Principle#^thm-b2-4-1|QM Theorem §B2.4.1]].

The three terms come from one by permuting $X, Y, Z$ cyclically: “move $Y$ to the left position, $Z$ one over to the left, and $X$ jumps to the last position.”

> [!theorem] Proposition §50.3: Commutators of an Associative Product
> Let $A$ be a real vector space with a bilinear *associative* product $(X, Y) \mapsto X \ast Y$. Then the commutator $[X, Y] = X \ast Y - Y \ast X$ is bilinear, skew-symmetric, and satisfies the [[§50 Lie Bracket and Lie Algebra#^def-50-2|Jacobi identity]]; so $(A, [\cdot,\cdot])$ is a [[§50 Lie Bracket and Lie Algebra#^def-50-2|Lie algebra]].

^prop-50-3

> [!proof]+ Proof
> *(Stated in Lecture 16 as “a general fact”; filled in. “The key thing is that it be an associative product.”)* Bilinearity and skew-symmetry are immediate. By associativity, triple products can be written without parentheses, and
>
> $$
> [X, [Y, Z]] = XYZ - XZY - YZX + ZYX .
> $$
>
> Permuting cyclically gives $[Y,[Z,X]] = YZX - YXZ - ZXY + XZY$ and $[Z,[X,Y]] = ZXY - ZYX - XYZ + YXZ$. In the sum each of the six words $XYZ, XZY, YZX, ZYX, YXZ, ZXY$ appears once with each sign, so the sum is $0$.

^pf-50-3

*Uses:* [[§50 Lie Bracket and Lie Algebra#^def-50-2|Def. §50.2]]

> [!example] Example §50.2: Matrices
> $\operatorname{Mat}(n, \mathbb{R})$, with the commutator $[A, B] = AB - BA$ of matrix multiplication, is a [[§50 Lie Bracket and Lie Algebra#^def-50-2|Lie algebra]], by [[§50 Lie Bracket and Lie Algebra#^prop-50-3|Proposition §50.3]].

^ex-50-2

> [!theorem] Corollary §50.4: Vector Fields Form a Lie Algebra
> $\big(\mathfrak{X}(M), [\cdot,\cdot]\big)$ is a [[§50 Lie Bracket and Lie Algebra#^def-50-2|Lie algebra]].
>
> *Lee: Proposition 8.28*

^cor-50-4

> [!proof]+ Proof
> *(Lecture 16: the bracket of fields “comes from the product, which is the composition, which is associative.” Filled in.)* The linear operators on $C^\infty(M)$ form an associative algebra under composition, so by [[§50 Lie Bracket and Lie Algebra#^prop-50-3|Proposition §50.3]] their commutator satisfies the Jacobi identity. By [[§50 Lie Bracket and Lie Algebra#^lem-50-1|Lemma §50.1]], $\mathfrak{X}(M)$, identified with the derivations, is closed under it; so the identity holds on $\mathfrak{X}(M)$.

^pf-50-4

*Uses:* [[§50 Lie Bracket and Lie Algebra#^def-50-1|Def. §50.1]], [[§50 Lie Bracket and Lie Algebra#^def-50-2|Def. §50.2]], [[§50 Lie Bracket and Lie Algebra#^prop-50-3|§50.3]], [[§50 Lie Bracket and Lie Algebra#^lem-50-1|§50.1]], [[§48 Vector Fields#^lem-48-3|§48.3]], [[§48 Vector Fields#^prop-48-7|§48.7]]

“Which I don't recommend you check by hand. It's a big computation.” The Lie algebra $\mathfrak{X}(M)$ is infinite-dimensional (for $\dim M \ge 1$). The finite-dimensional Lie algebras of [[§52 Lie Groups and Left-Invariant Vector Fields|§52]] sit inside it.

The bracket of two vector fields is one instance of a general fact about the ring of differential operators ([[§49 Differential Operators|§49]]): a commutator is always of lower order than the composites it is made from.

> [!theorem] Proposition §50.5: Commutators Lower the Order
> For operators $P, Q$ write $[P, Q] = P \circ Q - Q \circ P$, as in [[§50 Lie Bracket and Lie Algebra#^def-50-1|Definition §50.1]]. For the generators of $\mathrm{Diff}(M)$ ([[§49 Differential Operators#^def-49-2|Definition §49.2]]), with $g, h \in C^\infty(M)$ and $\mathbf{X}, \mathbf{Y} \in \mathfrak{X}(M)$:
> 1. $[m_g, m_h] = 0$;
> 2. $[D_\mathbf{X}, m_g] = m_{\mathbf{X}g}$;
> 3. $[D_\mathbf{X}, D_\mathbf{Y}] = D_{[\mathbf{X}, \mathbf{Y}]}$.
>
> Consequently, if $P \in \mathrm{Diff}_k(M)$ and $Q \in \mathrm{Diff}_l(M)$, then $[P, Q] \in \mathrm{Diff}_{k+l-1}(M)$ ([[§49 Differential Operators#^def-49-3|Definition §49.3]]).

^prop-50-5

> [!proof]+ Proof
> *(Not from lecture; filled in.)* (1) is [[§49 Differential Operators#^prop-49-1|Proposition §49.1]], (2) is [[§49 Differential Operators#^prop-49-2|Proposition §49.2]] (2), and (3) is [[§50 Lie Bracket and Lie Algebra#^lem-50-1|Lemma §50.1]], read with $D_\mathbf{X}$ written out. So for generators $A, B$ of orders $a, b \in \{0, 1\}$ ($0$ for a multiplication, $1$ for a vector field), $[A, B] \in \mathrm{Diff}_{a+b-1}(M)$. Two identities, checked by expanding (each side of the first is $PQR - QRP$),
>
> $$
> [P, Q \circ R] = [P, Q] \circ R + Q \circ [P, R], \qquad [P \circ Q, R] = P \circ [Q, R] + [P, R] \circ Q ,
> $$
>
> carry this to composites, using [[§49 Differential Operators#^prop-49-3|Proposition §49.3]] (2).
>
> *A generator against a composite.* Let $A$ have order $a$ and $B = B_1 \circ \cdots \circ B_s$ be a composite of generators of orders $b_i$, $l = \sum_i b_i$. By induction on $s$ ($s = 0$: $[A, \mathrm{id}] = 0$), with $B' = B_2 \circ \cdots \circ B_s$,
>
> $$
> [A, B_1 \circ B'] = [A, B_1] \circ B' + B_1 \circ [A, B'] \in \mathrm{Diff}_{a + b_1 - 1} \circ \mathrm{Diff}_{l - b_1} + \mathrm{Diff}_{b_1} \circ \mathrm{Diff}_{a + l - b_1 - 1} \subseteq \mathrm{Diff}_{a + l - 1} .
> $$
>
> *A composite against a composite.* Let $A = A_1 \circ \cdots \circ A_r$ have orders $a_i$, $k = \sum_i a_i$; by induction on $r$ ($r = 0$: $[\mathrm{id}, B] = 0$), with $A' = A_2 \circ \cdots \circ A_r$,
>
> $$
> [A_1 \circ A', B] = A_1 \circ [A', B] + [A_1, B] \circ A' \in \mathrm{Diff}_{a_1} \circ \mathrm{Diff}_{k - a_1 + l - 1} + \mathrm{Diff}_{a_1 + l - 1} \circ \mathrm{Diff}_{k - a_1} \subseteq \mathrm{Diff}_{k + l - 1} .
> $$
>
> *Sums.* The commutator is bilinear. A $P \in \mathrm{Diff}_k(M)$ is a sum of composites with $k' \le k$ vector-field factors, a $Q \in \mathrm{Diff}_l(M)$ one of composites with $l' \le l$, and each $[\text{composite}, \text{composite}]$ lies in $\mathrm{Diff}_{k' + l' - 1} \subseteq \mathrm{Diff}_{k + l - 1}$ ([[§49 Differential Operators#^prop-49-3|Proposition §49.3]] (1)).

^pf-50-5

*Uses:* [[§50 Lie Bracket and Lie Algebra#^def-50-1|Def. §50.1]], [[§49 Differential Operators#^def-49-2|Def. §49.2]], [[§49 Differential Operators#^def-49-3|Def. §49.3]], [[§49 Differential Operators#^prop-49-1|§49.1]], [[§49 Differential Operators#^prop-49-2|§49.2]], [[§50 Lie Bracket and Lie Algebra#^lem-50-1|§50.1]], [[§49 Differential Operators#^prop-49-3|§49.3]]

So two differential operators commute “up to lower order”. For $k = l = 1$, applied to $D_\mathbf{X}$ and $D_\mathbf{Y}$, the second-order parts of $\mathbf{X} \circ \mathbf{Y}$ and $\mathbf{Y} \circ \mathbf{X}$ cancel, as in [[§50 Lie Bracket and Lie Algebra#^ex-50-1|Example §50.1]]; what is left lies in $\mathrm{Diff}_1(M)$ and kills constants, and is the vector field $[\mathbf{X}, \mathbf{Y}]$ ([[§49 Differential Operators#^prop-49-3|Proposition §49.3]] (4)).

> [!example] Example §50.3: The Cross Product
> $\mathbb{R}^3$ with the [[§96 The Cross Product#^def-96-1|cross product]] is a [[§50 Lie Bracket and Lie Algebra#^def-50-2|Lie algebra]], and the [[§25 The Geometric Tangent Space#^def-25-3|hat map]] of [[§25 The Geometric Tangent Space#^def-25-3|Definition §25.3]] is an isomorphism of Lie algebras onto $\operatorname{Skew}(3, \mathbb{R}) = \mathfrak{so}(3)$ with the [[§50 Lie Bracket and Lie Algebra#^ex-50-2|matrix commutator]]:
>
> $$
> [\hat a, \hat b] = \hat a \hat b - \hat b \hat a = \widehat{a \times b} .
> $$

^ex-50-3

> [!proof]+ Proof
> *(Lecture 16 mentioned only that the cross product satisfies the Jacobi identity — “if you want to be really mean to your 215 students, give them the Jacobi identity for the cross product. Don't do that.” The proof via the hat map is filled in.)* By the [[§96 The Cross Product#^thm-96-8|identity]] $u \times (v \times w) = v\,(u \cdot w) - w\,(u \cdot v)$, for every $x \in \mathbb{R}^3$
>
> $$
> [\hat a, \hat b]\, x = a \times (b \times x) - b \times (a \times x) = b\,(a \cdot x) - a\,(b \cdot x) = (a \times b) \times x = \widehat{a \times b}\, x .
> $$
>
> $\operatorname{Skew}(3,\mathbb{R})$ is closed under the commutator ($[A,B]^{\mathsf T} = [B^{\mathsf T}, A^{\mathsf T}] = [B, A] = -[A,B]$ for skew $A, B$), so it is a Lie algebra by [[§50 Lie Bracket and Lie Algebra#^ex-50-2|Example §50.2]]. The hat map is a linear isomorphism carrying $\times$ to the commutator, so the cross product inherits bilinearity, skew-symmetry and the Jacobi identity — without the big computation.

^pf-ex-50-3

*Uses:* [[§25 The Geometric Tangent Space#^def-25-3|Def. §25.3]], [[§96 The Cross Product#^thm-96-8|Calc §96.8]], [[§50 Lie Bracket and Lie Algebra#^ex-50-2|Ex. §50.2]], [[§50 Lie Bracket and Lie Algebra#^def-50-2|Def. §50.2]]

> [!remark]- Connections
> - The cross product and its algebraic properties, proved by components: [[§96 The Cross Product#^def-96-1|Calc Def. §96.1]], [[§96 The Cross Product#^thm-96-8|Calc §96.8]].
> - The same computation for the infinitesimal rotations of quantum mechanics: [[§C5.1 Rotations and the Angular-Momentum Commutation Relations#^thm-c5-1-1|QM Theorem §C5.1.1]], with [[§C5.1 Rotations and the Angular-Momentum Commutation Relations#^rem-c5-1-1|QM ★ Remark: The Lie algebra of SO(3)]].

The classical groups through the course: defined in [[§11 Topological Groups and Classical Matrix Groups|Topological Groups and Classical Matrix Groups]], with the examples of [[§16 The Classical Groups|The Classical Groups]]; topological manifolds as level sets in [[§12 The Classical Groups Are Topological Manifolds#^thm-12-6|Classical Groups Are Manifolds]]; $\mathrm{SO}(2)$ and $\mathrm{SO}(3)$ acting on $\mathbb{R}^2$ and $\mathbb{R}^3$ in [[§13 Group Actions and Orbit Spaces#^ex-13-4|the rotations of the plane]] and [[§13 Group Actions and Orbit Spaces#^ex-13-5|the rotations of space]], and $\mathrm{SO}(3)$ on $S^2$ in [[§14 Homogeneous Spaces#^ex-14-2|the isotropy of the north pole]] and [[§14 Homogeneous Spaces#^ex-14-3|the sphere as a homogeneous space]]; $\mathrm{O}(n)$ acting on the Grassmannians in [[§15 The Topology of G∕H and Real Grassmannians#^cor-15-8|Grassmannians as Homogeneous Spaces]]; smooth manifolds in [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-23-1|the orthogonal group]] and [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-23-2|the unitary group]]; their tangent spaces at the identity in [[§25 The Geometric Tangent Space#^thm-25-5|The Classical Groups]], with [[§25 The Geometric Tangent Space#^ex-25-4|the infinitesimal rotations]]; the double cover $\mathrm{SU}(2) \to \mathrm{SO}(3)$ in [[§42 SU(2) → SO(3)꞉ The Double Cover#^thm-42-4|The Double Cover]]; the Lie algebra $\mathfrak{so}(3)$ and the cross product in [[§50 Lie Bracket and Lie Algebra#^ex-50-3|Ex. §50.3]]; and Lie groups in [[§52 Lie Groups and Left-Invariant Vector Fields#^prop-52-1|§52.1]].
