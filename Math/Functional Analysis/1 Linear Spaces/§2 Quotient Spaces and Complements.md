---
type: section
subject: "[[Functional Analysis]]"
chapter: 1
section: 2
tags: [functional-analysis, math556]
---
← [[§1 Linear Spaces]] · ↑ [[· 1 Linear Spaces]] · [[§3 Linear Maps, Convexity, and Linear Functionals]] →

*Stage: algebra — Threads: dimension. The quotient stands in for an orthogonal complement until [[§25 Projection and Orthogonal Decomposition|§25]].*

## Quotient Spaces

> [!definition] Definition §2.1: Equivalence mod $Y$
> Let $X$ be a linear space and $Y$ a linear subspace of $X$. We say $x_1, x_2 \in X$ are **equivalent mod $Y$**, written
>
> $$
> x_1 \equiv x_2 \pmod{Y},
> $$
>
> if $x_1 - x_2 \in Y$.
>
> *Lax: Ch. 1, equivalence mod $Y$*

^def-2-1

> [!remark]- Connections
> - Congruence modulo a subgroup, here for the subgroup Y of the additive group of X: [[§28 Left and Right Cosets#^def-28-1|493 Def. §28.1]].

> [!definition] Definition §2.2: Equivalence Class
> For $x_0 \in X$, the **equivalence class** of $x_0$ is
>
> $$
> [x_0] = \{ x \in X \mid x - x_0 \in Y \} = x_0 + Y.
> $$
>
> *Lax: Ch. 1, quotient space*

^def-2-2

> [!remark]- Connections
> - Axler's translates: [[§11 Products and Quotients of Vector Spaces#^ladr-3-97|LADR 3.97]].
> - The classes are the cosets of Y: [[§28 Left and Right Cosets#^def-28-2|493 Def. §28.2]].

> [!definition] Definition §2.3: Quotient Space
> The **quotient space** $X / Y$ ($X$ mod $Y$) is the set of all equivalence classes (Definition [[§2 Quotient Spaces and Complements#^def-2-2|§2.2]]):
>
> $$
> X / Y = \{ [x] \mid x \in X \}.
> $$
>
> *Lax: Ch. 1, quotient space*

^def-2-3

> [!remark]- Connections
> - Axler's quotient space: [[§11 Products and Quotients of Vector Spaces#^ladr-3-99|LADR 3.99]].
> - X/Y is the quotient group of (X, +) by Y with scalar multiplication added: [[§40 Quotient Groups#^def-40-1|493 Def. §40.1]].

> [!example] Example §2.1: Geometry of Equivalence Classes
> Let $X = \mathbb{R}^2$ and let $Y$ be a line through the origin. If $x_0 = 0$ then $[x_0] = Y$. For general $x_0$, the class $[x_0] = x_0 + Y$ is the line *parallel* to $Y$ passing through the tip of the vector $x_0$: any other point $x$ on this line, dragged back by $-x_0$, lands on $Y$, i.e. $x - x_0 \in Y$. The equivalence classes are therefore the parallel translates of $Y$. They are not subspaces (they do not contain the origin unless equal to $Y$); the quotient $X / Y$ is the collection of all these parallel lines.
>
> ![[m556-1-2.svg]]
> *The class $[x_0] = x_0 + Y$ (red) is the line through $x_0$ parallel to $Y$; a point $x$ on it, moved by $-x_0$, lands on $Y$.*

^ex-2-1

> [!theorem] Proposition §2.1: $X/Y$ is a Linear Space
> The operations
>
> $$
> [x_1] + [x_2] = [x_1 + x_2], \qquad k[x] = [kx]
> $$
>
> are well defined on $X / Y$ and make $X / Y$ a linear space over $\mathbb{F}$, with zero element $[0] = Y$.
>
> *Source: HW1, Problem 1*
>
> *Lax: Ch. 1, quotient space*

^prop-2-1

> [!proof]+ Proof
> (HW1, Problem 1.) **Well-definedness.** Suppose $[x_1] = [x_1']$ and $[x_2] = [x_2']$, i.e. $x_1 - x_1' \in Y$ and $x_2 - x_2' \in Y$. Then
>
> $$
> (x_1 + x_2) - (x_1' + x_2') = (x_1 - x_1') + (x_2 - x_2') \in Y, \qquad kx_1 - kx_1' = k(x_1 - x_1') \in Y,
> $$
>
> since $Y$ is a subspace. Hence $[x_1 + x_2] = [x_1' + x_2']$ and $[kx_1] = [kx_1']$: the operations do not depend on the representatives.
>
> **The axioms.** Let $[x], [y], [z] \in X/Y$ and $a, k \in \mathbb{F}$. In each line the outer equalities are the definitions of the operations on $X/Y$, and the middle equality is the corresponding axiom of $X$.
>
> *Commutativity:* $[x] + [y] = [x + y] = [y + x] = [y] + [x]$.
>
> *Associativity:* $([x] + [y]) + [z] = [x + y] + [z] = [(x + y) + z] = [x + (y + z)] = [x] + [y + z] = [x] + ([y] + [z])$.
>
> *Additive identity:* $[0] = Y \in X/Y$, and $[x] + [0] = [x + 0] = [x] = [0 + x] = [0] + [x]$.
>
> *Additive inverse:* $[-x] \in X/Y$, and $[x] + [-x] = [x - x] = [0] = [-x + x] = [-x] + [x]$.
>
> *Compatibility of scalar multiplication:* $k(a[x]) = k[ax] = [k(ax)] = [(ka)x] = (ka)[x]$.
>
> *Distributivity over vector addition:* $k([x] + [y]) = k[x + y] = [k(x + y)] = [kx + ky] = [kx] + [ky] = k[x] + k[y]$.
>
> *Distributivity over scalar addition:* $(a + k)[x] = [(a + k)x] = [ax + kx] = [ax] + [kx] = a[x] + k[x]$.
>
> *Unit:* $1[x] = [1x] = [x]$.
>
> Hence $X/Y$ is a linear space over $\mathbb{F}$ with zero element $[0] = Y$.

^pf-2-1

*Uses:* [[§2 Quotient Spaces and Complements#^def-2-1|Def. §2.1]], [[§2 Quotient Spaces and Complements#^def-2-2|Def. §2.2]], [[§2 Quotient Spaces and Complements#^def-2-3|Def. §2.3]], [[§1 Linear Spaces#^def-1-2|Def. §1.2]], [[§1 Linear Spaces#^def-1-1|Def. §1.1]]

> [!remark]- Connections
> - The same result in linear algebra: the operations [[§11 Products and Quotients of Vector Spaces#^ladr-3-102|LADR 3.102]], and the quotient is a vector space, [[§11 Products and Quotients of Vector Spaces#^ladr-3-103|LADR 3.103]].

> [!remark] Remark
> The pattern of the verification is the same in every line: the outer equalities are the definitions of the operations on $X/Y$ and the middle equality is the corresponding axiom of $X$, e.g. $k([x_1]+[x_2]) = k[x_1+x_2] = [k(x_1+x_2)] = [kx_1+kx_2] = k[x_1]+k[x_2]$. The additive inverse is $-[x] = [-x]$.

^rem-2-1

> [!remark] Remark: Quotients and Orthogonal Complements
> In $\mathbb{R}^n$, one may think of $X / Y$ as playing the role of the orthogonal complement $Y^\perp$: each parallel translate $x_0 + Y$ meets $Y^\perp$ in exactly one point. But “orthogonal” requires an inner product, and a bare linear space has no such structure. The quotient space is the substitute that is available in full generality. Wu suggested in lecture that $(X/Y) \oplus Y \cong X$ “in some sense”; this became HW1, and the precise statement needs no inner product at all — only a subspace $W$ playing the role of $Y^\perp$. The tools are extracted below.

^rem-2-2

## Complements and the Isomorphism X ≅ X/Y ⊕ Y

Throughout this subsection $Y$ is a fixed linear subspace of $X$. The material is from HW1.

> [!definition] Definition §2.4: Complement
> A linear subspace $W \subset X$ is a **complement** of $Y$ if
>
> $$
> W \cap Y = \{0\} \qquad \text{and} \qquad W + Y = X.
> $$
>
> *Source: HW1*

^def-2-4

> [!theorem] Lemma §2.2: One-Step Enlargement
> Let $W \subset X$ be a linear subspace with $W \cap Y = \{0\}$, and let $x_0 \in X$ with $x_0 \notin W + Y$. Then $W' = W + \operatorname{span}\{x_0\}$ is a linear subspace with $W' \cap Y = \{0\}$ and $W \subsetneq W'$.
>
> *Source: HW1*

^lem-2-2

> [!proof]+ Proof
> $W'$ is a subspace as a sum of subspaces (Proposition [[§1 Linear Spaces#^prop-1-2|§1.2]]).
>
> *Strictness.* $x_0 \in W'$. If $x_0 \in W$ then $x_0 = x_0 + 0 \in W + Y$, contradicting the hypothesis; so $x_0 \in W' \setminus W$.
>
> *Intersection.* Let $w' \in W' \cap Y$, and write $w' = a x_0 + w$ with $a \in \mathbb{F}$, $w \in W$; put $y = w' \in Y$, so $a x_0 + w = y$. If $a \neq 0$, dividing by $a$ and rearranging gives
>
> $$
> x_0 = \frac{y}{a} - \frac{w}{a} \in Y + W,
> $$
>
> contradicting $x_0 \notin W + Y$. Hence $a = 0$, so $w' = w \in W \cap Y = \{0\}$. Thus $W' \cap Y = \{0\}$.

^pf-2-2

*Uses:* [[§1 Linear Spaces#^prop-1-2|§1.2]], [[§1 Linear Spaces#^prop-1-5|§1.5]]

> [!theorem] Proposition §2.3: Every Subspace Has a Complement
> For every linear subspace $Y \subset X$ there exists a complement $W$ of $Y$.
>
> *Source: HW1*

^prop-2-3

> [!proof]+ Proof
> Let $P = \{ W \subset X \text{ a linear subspace} : W \cap Y = \{0\} \}$, partially ordered by inclusion; $\{0\} \in P$. Chains in $P$ have upper bounds: the union of a chain of subspaces is a subspace (the argument in the [[§6 Proof of the Hahn–Banach Theorem#^pf-5-2|proof]] of Theorem [[§5 Statement and Motivation#^thm-5-2|§5.2]]), and it meets $Y$ only in $0$ since each member does. By Zorn's lemma (Theorem [[§6 Proof of the Hahn–Banach Theorem#^thm-6-2|§6.2]]) $P$ has a maximal element $W$. If $W + Y \neq X$, pick $x_0 \in X \setminus (W + Y)$; Lemma [[§2 Quotient Spaces and Complements#^lem-2-2|§2.2]] gives a strictly larger element of $P$, contradicting maximality. Hence $W + Y = X$, and $W$ is a complement.

^pf-2-3

*Uses:* [[§2 Quotient Spaces and Complements#^def-2-4|Def. §2.4]], [[§5 Statement and Motivation#^thm-5-2|§5.2]], [[§6 Proof of the Hahn–Banach Theorem#^thm-6-2|§6.2]], [[§2 Quotient Spaces and Complements#^lem-2-2|§2.2]]

> [!remark]- Connections
> - The finite-dimensional version, by extending a basis: [[§5 Bases#^ladr-2-33|LADR 2.33]].

> [!remark] Remark
> When $\dim X < \infty$ Zorn's lemma is unnecessary: starting from $W = \{0\}$ and applying Lemma [[§2 Quotient Spaces and Complements#^lem-2-2|§2.2]] repeatedly, $\dim W$ increases by one each time and the process stops after at most $\dim X - \dim Y$ steps.

^rem-2-3

> [!theorem] Proposition §2.4: When the Complement is Unique
> A linear subspace $Y$ of $X$ has exactly one complement if and only if $Y = \{0\}$ or $Y = X$.
>
> *Source: HW1*

^prop-2-4

> [!proof]+ Proof
> If $Y = \{0\}$, a complement $W$ satisfies $W = W + \{0\} = X$; if $Y = X$, it satisfies $W = W \cap X = \{0\}$. In both cases the complement is unique.
>
> Suppose $\{0\} \neq Y \neq X$, and let $W$ be a complement (Proposition [[§2 Quotient Spaces and Complements#^prop-2-3|§2.3]]). Then $W \neq \{0\}$, since $W + Y = X \neq Y$. Choose $0 \neq y_0 \in Y$ and $0 \neq w_0 \in W$. Applying Proposition [[§2 Quotient Spaces and Complements#^prop-2-3|§2.3]] inside the linear space $W$, the subspace $\operatorname{span}\{w_0\}$ has a complement $W_1$ in $W$: $\operatorname{span}\{w_0\} \cap W_1 = \{0\}$ and $\operatorname{span}\{w_0\} + W_1 = W$. Put
>
> $$
> W' = \operatorname{span}\{w_0 + y_0\} + W_1 .
> $$
>
> *$W' \cap Y = \{0\}$.* If $a(w_0 + y_0) + w_1 \in Y$ with $a \in \mathbb{F}$, $w_1 \in W_1$, then subtracting $a y_0 \in Y$ gives $a w_0 + w_1 \in Y \cap W = \{0\}$; so $a w_0 = -w_1 \in \operatorname{span}\{w_0\} \cap W_1 = \{0\}$, whence $a = 0$ and $w_1 = 0$.
>
> *$W' + Y = X$.* $w_0 = (w_0 + y_0) - y_0 \in W' + Y$ and $W_1 \subset W'$, so $W = \operatorname{span}\{w_0\} + W_1 \subset W' + Y$, and $X = W + Y \subset W' + Y$.
>
> *$W' \neq W$.* $w_0 + y_0 \in W'$; if it were in $W$, then $y_0 = (w_0 + y_0) - w_0 \in W \cap Y = \{0\}$, a contradiction.
>
> So $W'$ is a second complement of $Y$. (Not covered in lecture.)

^pf-2-4

*Uses:* [[§2 Quotient Spaces and Complements#^def-2-4|Def. §2.4]], [[§2 Quotient Spaces and Complements#^prop-2-3|§2.3]], [[§1 Linear Spaces#^prop-1-2|§1.2]], [[§1 Linear Spaces#^prop-1-5|§1.5]]

> [!example] Example §2.2: Complements of a Line in the Plane
> In $\mathbb{R}^2$ with $Y$ the $x$-axis, every line through the origin other than $Y$ is a complement of $Y$.
>
> *Source: HW1*

^ex-2-2

> [!remark]- Connections
> - The same example in linear algebra, in the remark “Not unique” after [[§5 Bases#^ladr-2-33|LADR 2.33]].

> [!theorem] Lemma §2.5: Unique Decomposition
> Let $W$ be a complement of $Y$. Then every $x \in X$ can be written as $x = w + y$ with $w \in W$, $y \in Y$, and this representation is unique.
>
> *Source: HW1*

^lem-2-5

> [!proof]+ Proof
> Existence is $X = W + Y$. If $w_1 + y_1 = w_2 + y_2$, then $w_1 - w_2 = y_2 - y_1$ lies in both $W$ and $Y$, hence in $W \cap Y = \{0\}$; so $w_1 = w_2$ and $y_1 = y_2$.

^pf-2-5

*Uses:* [[§2 Quotient Spaces and Complements#^def-2-4|Def. §2.4]]

This is the implication (ii)$\Rightarrow$(iii) of Proposition [[§1 Linear Spaces#^prop-1-3|§1.3]], applied to $W$ and $Y$.

> [!theorem] Theorem §2.6: $X \cong X/Y \oplus Y$
> Let $W$ be a complement of $Y$. The map
>
> $$
> M : X \to X/Y \oplus Y, \qquad M(x) = ([w], y) \quad \text{where } x = w + y,\ w \in W,\ y \in Y,
> $$
>
> is an isomorphism. Consequently $X/Y \oplus Y \cong X$, with inverse $M^{-1}([x], y) = w + y$, where $w$ is the unique element of $W$ with $[w] = [x]$.
>
> *Source: HW1*

^thm-2-6

> [!proof]+ Proof
> $M$ is well defined by Lemma [[§2 Quotient Spaces and Complements#^lem-2-5|§2.5]].
>
> *Linearity.* If $x_i = w_i + y_i$ and $a, b \in \mathbb{F}$, then $a x_1 + b x_2 = (a w_1 + b w_2) + (a y_1 + b y_2)$ with the two summands in $W$ and $Y$ respectively; by uniqueness this *is* the decomposition of $a x_1 + b x_2$, so
>
> $$
> M(a x_1 + b x_2) = \bigl([a w_1 + b w_2],\, a y_1 + b y_2\bigr) = a([w_1], y_1) + b([w_2], y_2) = a M(x_1) + b M(x_2),
> $$
>
> using the operations on $X/Y$ (Proposition [[§2 Quotient Spaces and Complements#^prop-2-1|§2.1]]) and the componentwise operations on the direct sum.
>
> *Surjectivity.* Given $([x], y)$, decompose $x = w + y'$. Then $x - w = y' \in Y$, so $[x] = [w]$, and $M(w + y) = ([w], y) = ([x], y)$.
>
> *Injectivity.* If $M(x_1) = M(x_2)$ with $x_i = w_i + y_i$, then $y_1 = y_2$ and $[w_1] = [w_2]$, i.e. $w_1 - w_2 \in Y$; also $w_1 - w_2 \in W$, so $w_1 - w_2 \in W \cap Y = \{0\}$. Hence $x_1 = x_2$.
>
> $M$ is a linear bijection, hence an isomorphism, and $M^{-1}$ is an isomorphism by Lemma [[§3 Linear Maps, Convexity, and Linear Functionals#^lem-3-1|§3.1]]. The formula for $M^{-1}$ is read off from the surjectivity computation.

^pf-2-6

*Uses:* [[§2 Quotient Spaces and Complements#^lem-2-5|§2.5]], [[§2 Quotient Spaces and Complements#^prop-2-1|§2.1]], [[§1 Linear Spaces#^def-1-4|Def. §1.4]], [[§2 Quotient Spaces and Complements#^def-2-2|Def. §2.2]], [[§2 Quotient Spaces and Complements#^def-2-3|Def. §2.3]], [[§3 Linear Maps, Convexity, and Linear Functionals#^def-3-2|Def. §3.2]], [[§3 Linear Maps, Convexity, and Linear Functionals#^lem-3-1|§3.1]]

> [!remark]- Connections
> - In finite dimensions it gives the dimension count of [[§11 Products and Quotients of Vector Spaces#^ladr-3-105|LADR 3.105]].
> - The orthogonal version for [[§23 Cauchy–Schwarz and the Induced Norm#^def-23-1|Hilbert spaces]]: [[§25 Projection and Orthogonal Decomposition#^thm-25-4|§25.4]].

> [!theorem] Corollary §2.7: A Complement is a Model of the Quotient
> If $W$ is a complement of $Y$, then the restricted quotient map $W \to X/Y$, $w \mapsto [w]$, is an isomorphism. In particular all complements of $Y$ are isomorphic to one another.
>
> *Source: HW1*

^cor-2-7

> [!proof]+ Proof
> Linearity is inherited from the quotient map. Injectivity and surjectivity are exactly the two computations in the proof of Theorem [[§2 Quotient Spaces and Complements#^thm-2-6|§2.6]]: $[w_1] = [w_2]$ forces $w_1 - w_2 \in W \cap Y = \{0\}$, and every class $[x]$ equals $[w]$ for the $W$-component $w$ of $x$.

^pf-2-7

*Uses:* [[§2 Quotient Spaces and Complements#^thm-2-6|§2.6]], [[§2 Quotient Spaces and Complements#^prop-2-1|§2.1]], [[§2 Quotient Spaces and Complements#^lem-2-5|§2.5]]

> [!remark] Remark: The Isomorphism is Not Canonical
> $M$ depends on the choice of complement $W$. The quotient $X/Y$ itself is canonical — it is built from $X$ and $Y$ alone — but identifying it with a subspace of $X$ requires choosing $W$, and different choices give different embeddings. This is the precise content of “$X/Y$ is like a complement of $Y$”: it is isomorphic to every complement, and equal to none.

^rem-2-4

![[m556-1-3.svg]]
*Quotient versus complement in $\mathbb{R}^2$. The elements of $X/Y$ are the red lines parallel to $Y$ (with $Y$ itself the zero class $[0]$). A complement $W$ (blue) is a line through $0$ that meets each class exactly once, at $w$ — this is the isomorphism $w \mapsto [w]$ of Corollary §2.7. A second complement $W'$ (green) meets the same classes at different points: $w$ and $w'$ represent the same class $[x]$, so each complement is a model of $X/Y$, and neither is $X/Y$ itself.*

> [!theorem] Corollary §2.8: Orthogonal Complement (inner products; later)
> Let $X$ carry an inner product $\langle \cdot, \cdot \rangle$ and let $Y^\perp = \{ z \in X : \langle z, y \rangle = 0 \ \forall y \in Y \}$. If $X = Y + Y^\perp$, then $Y^\perp$ is a complement of $Y$, so $X/Y \cong Y^\perp$ via $z \mapsto [z]$ and $X \cong X/Y \oplus Y$.
>
> *Source: HW1*

^cor-2-8

> [!proof]+ Proof
> If $z \in Y \cap Y^\perp$ then $\langle z, z \rangle = 0$, so $z = 0$ by positive-definiteness of the inner product (to be introduced later). With $X = Y + Y^\perp$ assumed, $Y^\perp$ is a complement; apply Corollary [[§2 Quotient Spaces and Complements#^cor-2-7|§2.7]] and Theorem [[§2 Quotient Spaces and Complements#^thm-2-6|§2.6]].

^pf-2-8

*Uses:* [[§22 Definition and Examples#^def-22-1|Def. §22.1]], [[§2 Quotient Spaces and Complements#^def-2-4|Def. §2.4]], [[§2 Quotient Spaces and Complements#^cor-2-7|§2.7]], [[§2 Quotient Spaces and Complements#^thm-2-6|§2.6]]

> [!remark]- Connections
> - The inner product and $Y^\perp$ in this course: [[§22 Definition and Examples#^def-22-1|Def. §22.1]], [[§25 Projection and Orthogonal Decomposition#^thm-25-4|§25.4]] (the orthogonal decomposition, which supplies $X = Y + Y^\perp$ for closed $Y$ in a Hilbert space).
> - In finite dimensions: [[§22 Orthogonal Complements and Minimization Problems#^ladr-6-46|LADR 6.46]], and $V = U \oplus U^\perp$ ([[§22 Orthogonal Complements and Minimization Problems#^ladr-6-49|LADR 6.49]]).

> [!remark] Remark
> The hypothesis $X = Y + Y^\perp$ holds automatically in finite dimensions, and in infinite dimensions it holds when $X$ is complete and $Y$ is closed (the orthogonal decomposition theorem, Theorem [[§25 Projection and Orthogonal Decomposition#^thm-25-4|§25.4]]). It can fail for a general subspace: in $\ell^2$ with the inner product of [[· 5 Inner Product Spaces|Chapter 5]], the finitely supported sequences form a subspace $Y$ with $Y^\perp = \{0\}$, since $(z, e_i) = z_i$, so $Y + Y^\perp = Y \neq \ell^2$. Then $Y^\perp$ is *not* a complement — although by Proposition [[§2 Quotient Spaces and Complements#^prop-2-3|§2.3]] some other complement always exists. This is why the orthogonal version is only “roughly” true, while the algebraic version (Theorem [[§2 Quotient Spaces and Complements#^thm-2-6|§2.6]]) is unconditional.

^rem-2-5
