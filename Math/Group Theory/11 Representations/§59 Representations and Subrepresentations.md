---
type: section
subject: "[[Group Theory]]"
chapter: 11
section: 59
tags: [group-theory, math493]
---
← [[§58 Semidirect Products]] · ↑ [[· 11 Representations]] · [[§60 Direct Sums and Maschke's Theorem]] →

*Source: Lecture and Worksheet 13 (Mon Nov 2). Not covered in the Pinter chapters used so far.*

> [!definition] Definition §59.1: Representation
> Let $G$ be a group and $k$ a field. A **representation** of $G$ (over $k$) is a $k$-vector space $V$ together with an action of $G$ on $V$ by linear maps. That is, $\star: G \times V \to V$ satisfies, for $g, g_1, g_2 \in G$, $v, v_1, v_2 \in V$ and $c \in k$:
>
> $$
> \begin{aligned}&\text{action axioms:} && e \star v = v, && g_1 \star (g_2 \star v) = (g_1g_2) \star v; \\
> &\text{linearity axioms:} && g \star (v_1 + v_2) = g \star v_1 + g \star v_2, && g \star (cv) = c\,(g \star v).\end{aligned}
> $$
>
> One often writes $gv$ for $g \star v$.
>
> *Source: lecture 11/2; WS 13*

^def-59-1

The linearity axioms say exactly that, for each fixed $g$, the map $v \mapsto g \star v$ is linear; the action axioms are those of an action on the set $V$ (Definition [[§25 Actions#^def-25-1|§25.1]]). *(Not from class.)* Problem Set 1 already used the word, for a homomorphism $G \to GL_n(k)$ (Definition [[§20 Polynomial Rings, Permutation Matrices, and Representations#^def-20-7|§20.7]]); Proposition [[§59 Representations and Subrepresentations#^prop-59-1|§59.1]] below shows the two definitions agree.

> [!theorem] Proposition §59.1: Representations Are Homomorphisms to $GL(V)$
> A representation of $G$ on $V$ is the same thing as a group homomorphism $\rho: G \to GL(V)$, the group of invertible linear maps $V \to V$ under composition. The correspondence is $\rho(g)(v) = g \star v$.
>
> *Source: WS 13.1*

^prop-59-1

> [!proof]+ Proof
> *Idea:* The action axioms are the homomorphism property; the linearity axioms say each $\rho(g)$ is linear.
>
> *(Worksheet session 11/2.)* Given a representation, let $\rho(g): V \to V$ be $v \mapsto g \star v$, which is linear by the linearity axioms. The action axioms say $\rho(e) = \mathrm{id}_V$ and $\rho(g_1g_2) = \rho(g_1) \circ \rho(g_2)$. In particular $\rho(g)\rho(g^{-1}) = \rho(e) = \mathrm{id}_V = \rho(g^{-1})\rho(g)$, so $\rho(g)$ is invertible and $\rho: G \to GL(V)$ is a homomorphism. Conversely, given a homomorphism $\rho$, the rule $g \star v := \rho(g)(v)$ satisfies the action axioms because $\rho$ is a homomorphism (so $\rho(e) = \mathrm{id}_V$, Proposition [[§15 Homomorphisms#^prop-15-1|§15.1]]), and the linearity axioms because each $\rho(g)$ is linear. The two constructions are inverse to each other. This is the linear version of Theorem [[§25 Actions#^thm-25-3|§25.3]], Actions Are Homomorphisms to $S_X$.

^pf-59-1

*Uses:* [[§15 Homomorphisms#^prop-15-1|§15.1]], [[§25 Actions#^thm-25-3|§25.3]]

> [!remark] Remark: Notation and Matrices
> One writes $\rho_V(g)$ when it is necessary to say which representation is meant. If $V$ has a basis $v_1, \ldots, v_n$, each $\rho(g)$ becomes an invertible $n \times n$ matrix, and the representation becomes a homomorphism $G \to GL_n(k)$. So a representation can be written down by giving the matrices $\rho(g)$ for $g \in G$. As usual, column $j$ of the matrix of $\rho(g)$ records $g \star v_j$ in terms of the basis.
>
> *Source: WS 13*

^rem-59-1

> [!example] Example §59.1: The Trivial Representation
> Let $V = k$, one-dimensional, with $g \star v = v$ for all $g$ and $v$. In matrices, $\rho(g) = [\,1\,]$, the $1 \times 1$ identity matrix, for every $g \in G$.
>
> *Source: WS 13.2*

^ex-59-1

> [!example] Example §59.2: One-Dimensional Representations and Characters
> Since $GL_1(k) = k^\times$, a one-dimensional representation is the same thing as a character $\chi: G \to k^\times$ (Definition [[§46 Characters#^def-46-1|§46.1]]). For example, the sign (Definition [[§21 The Sign Homomorphism and the Alternating Group#^def-21-2|§21.2]], a homomorphism by Theorem [[§21 The Sign Homomorphism and the Alternating Group#^thm-21-3|§21.3]]) gives the **sign representation** of $S_n$ on $k$, $\sigma \star v = \operatorname{sgn}(\sigma)\,v$. The trivial representation is the trivial character.
>
> *Source: not from class*

^ex-59-2

> [!definition] Definition §59.2: Permutation Representation
> Let $G$ act on a set $X$. Let $kX$ be the vector space with basis $\{e_x : x \in X\}$: its elements are formal sums $\sum_{x \in X} a_x e_x$ with $a_x \in k$ and $a_x = 0$ for all but finitely many $x$. The **permutation representation** is
>
> $$
> g \star \sum_{x \in X} a_x e_x = \sum_{x \in X} a_x e_{g \star x}.
> $$
>
> *Source: WS 13.3*

^def-59-2

> [!theorem] Proposition §59.2: The Permutation Representation Is a Representation
> 1. $kX$ with this rule is a representation of $G$.
> 2. For $S_3$ acting on $\{1, 2, 3\}$, in the basis $e_1, e_2, e_3$,
>
> $$
> \rho\big((1\,2\,3)\big) = \begin{pmatrix} 0 & 0 & 1 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \end{pmatrix}.
> $$
>
> *Source: WS 13.3*

^prop-59-2

> [!proof]+ Proof
> *Idea:* The rule moves basis vectors as the action moves points, so the action axioms for $X$ give those for $kX$.
>
> *(Worksheet session 11/2.)* **(1)** The rule is linear in the coefficients $a_x$, so the linearity axioms hold. For the action axioms, $e \star \sum a_x e_x = \sum a_x e_{e \star x} = \sum a_x e_x$, and
>
> $$
> g_1 \star \Big(g_2 \star \sum_x a_x e_x\Big) = g_1 \star \sum_x a_x e_{g_2 \star x} = \sum_x a_x e_{g_1 \star (g_2 \star x)} = \sum_x a_x e_{(g_1g_2) \star x} = (g_1g_2) \star \sum_x a_x e_x,
> $$
>
> using the action axiom for $X$.
>
> **(2)** $(1\,2\,3)$ sends $e_1 \mapsto e_2$, $e_2 \mapsto e_3$, $e_3 \mapsto e_1$; these are the three columns. For $X = \{1, \ldots, n\}$ and $G = S_n$, $\rho(\sigma)$ is the permutation matrix $M(\sigma)$ (Definition [[§20 Polynomial Rings, Permutation Matrices, and Representations#^def-20-6|§20.6]]), and the homomorphism $\sigma \mapsto M(\sigma)$ found there is this representation.

^pf-59-2

*Uses:* [[§20 Polynomial Rings, Permutation Matrices, and Representations#^def-20-6|Def. §20.6]]

*(Not from class.)* For $X = \{1, \ldots, n\}$ and $G = S_n$ this is the permutation representation $\sigma \mapsto M(\sigma)$ of Problem Set 1 (Definition [[§20 Polynomial Rings, Permutation Matrices, and Representations#^def-20-8|§20.8]]). For finite $X$ the permutation representation is the composite of the homomorphism $G \to S_X$ of the action (Theorem [[§25 Actions#^thm-25-3|§25.3]]) with $\sigma \mapsto T_\sigma$, $S_X \to GL(k^X)$ (Proposition [[§20 Polynomial Rings, Permutation Matrices, and Representations#^prop-20-4|§20.4]]): it is “the action, made linear”.

> [!definition] Definition §59.3: Subrepresentation
> Let $V$ be a representation of $G$. A **subrepresentation** of $V$ is a subspace $U \subseteq V$ with $g \star u \in U$ for all $g \in G$ and $u \in U$ (a $G$-invariant subspace).
>
> *Source: WS 13*

^def-59-3

A subrepresentation is itself a representation of $G$, by restricting the action: the axioms hold in $U$ because they hold in $V$. $\{0\}$ and $V$ are always subrepresentations.

> [!example] Example §59.3: Two Subrepresentations of $k\{1,2,3\}$
> Let $S_3$ act on $k\{1,2,3\} = k^3$ as in WS 13.3, so $\sigma$ permutes the coordinates.
>
> 1. $U_1 = k\,(1,1,1)$, the span of the all-ones vector. Permuting coordinates fixes $(1,1,1)$, so $U_1$ is a subrepresentation, and every $g$ acts as the identity: in the basis $(1,1,1)$, $\rho_{U_1}(g) = [\,1\,]$. So $U_1$ is a copy of the trivial representation.
> 2. $U_2 = \{(x, y, z) : x + y + z = 0\}$, the vectors whose coordinates sum to $0$ (the [[§22 Orthogonal Complements and Minimization Problems#^ladr-6-46|orthogonal complement]] of $U_1$ for the dot product). Permuting coordinates does not change their sum, so $U_2$ is a subrepresentation, though its vectors are not fixed. It is two-dimensional, with basis
>
> $$
> f_1 = (1, -1, 0), \qquad f_2 = (1, 0, -1).
> $$
>
> For example, $(1\,2) \star f_1 = (-1, 1, 0) = -f_1$ and $(1\,2) \star f_2 = (0, 1, -1) = -f_1 + f_2$, so $\rho_{U_2}\big((1\,2)\big) = \left(\begin{smallmatrix} -1 & -1 \\ 0 & 1 \end{smallmatrix}\right)$. All six matrices, in this basis:
>
> \begin{center}
> \renewcommand{\arraystretch}{1.35}\setlength{\tabcolsep}{4pt}
> \begin{tabular}{c|cccccc}
> $g$ & $e$ & $(1\,2)$ & $(1\,3)$ & $(2\,3)$ & $(1\,2\,3)$ & $(1\,3\,2)$ \ \hline
> $\rho_{U_2}(g)$ & $\left(\begin{smallmatrix} 1 & 0 \\ 0 & 1 \end{smallmatrix}\right)$ & $\left(\begin{smallmatrix} -1 & -1 \\ 0 & 1 \end{smallmatrix}\right)$ & $\left(\begin{smallmatrix} 1 & 0 \\ -1 & -1 \end{smallmatrix}\right)$ & $\left(\begin{smallmatrix} 0 & 1 \\ 1 & 0 \end{smallmatrix}\right)$ & $\left(\begin{smallmatrix} -1 & -1 \\ 1 & 0 \end{smallmatrix}\right)$ & $\left(\begin{smallmatrix} 0 & 1 \\ -1 & -1 \end{smallmatrix}\right)$ \\
> trace & $2$ & $0$ & $0$ & $0$ & $-1$ & $-1$ \\
> det & $1$ & $-1$ & $-1$ & $-1$ & $1$ & $1$
> \end{tabular}
> \end{center}
> (The table, apart from $(1\,2)$, is not from class; checked by computer.) Other boards used other bases, such as $(1,-1,0), (0,1,-1)$, and got different matrices.
>
> *Source: WS 13.4; board 11/2*

^ex-59-3

**Transcription note (board 11/2).** With $f_1 = (1,-1,0)$, $f_2 = (1,0,-1)$, the handwritten notes write $(1\,2) \star f_2 = f_1$ and first record the matrix $\left(\begin{smallmatrix} -1 & 1 \\ 0 & 0 \end{smallmatrix}\right)$. In fact $(1\,2) \star f_2 = (0,1,-1) = -f_1 + f_2$, and the matrix is $\left(\begin{smallmatrix} -1 & -1 \\ 0 & 1 \end{smallmatrix}\right)$, the third matrix on the board. The first one has determinant $0$, so it cannot be the matrix of $(1\,2)$ in any basis: the lecture's trace and determinant check (trace $0$, determinant $-1$) catches it.

![[m493-59-1.svg]]

*(Not from lecture; figure added.)* $S_3$ permutes the coordinate axes of $\mathbb{R}^3$, so it permutes $e_1, e_2, e_3$ and maps the triangle they span to itself. The line $U_1$ through $(1,1,1)$ (red) is fixed pointwise, and the plane $U_2 = \{x + y + z = 0\}$ (blue) perpendicular to it is mapped to itself, though not pointwise: $f_1 = e_1 - e_2$ and $f_2 = e_1 - e_3$ lie in it. The hexagon marks a piece of the plane $U_2$; its vertices lie on the lines through the six vectors $e_i - e_j$.

![[m493-59-2.svg]]

*(Not from lecture; figure added.)* The plane $U_2$ seen face on, along $(1,1,1)$. The projections of $e_1, e_2, e_3$ form an equilateral triangle, and $S_3$ acts on $U_2$ as the symmetry group of that triangle: $(1\,2)$ is the reflection in the dashed red line, and $(1\,2\,3)$ is the rotation by $120^\circ$ taking $1 \to 2 \to 3$. A reflection has trace $0$ and determinant $-1$; a rotation by $120^\circ$ has trace $2\cos 120^\circ = -1$ and determinant $1$: the rows of the table, in any basis.

![[m493-59-a1.gif|560]]

*(Not from lecture; animation added, vault only.)* The six matrices of the table, moving: each $g \ne e$ acts on the plane $U_2$, seen face on, as a symmetry of the triangle of the projected $e_1, e_2, e_3$ (vertex labels follow the points). The reflections $(1\,2)$, $(1\,3)$, $(2\,3)$ fold across the dashed red mirror, the $3$-cycles rotate by $120^\circ$; the blue arrows are $g f_1$, $g f_2$ (grey: $f_1$, $f_2$), and the panel gives the matrix in the basis $(f_1, f_2)$ with its trace and determinant, as in the table.

> [!remark] Remark: Checking Answers in Different Bases
> Matrices of the same linear map in different bases are conjugate, $M' = PMP^{-1}$, so they can look different. To compare answers from different boards, compare invariants of conjugation: the **determinant**, the **trace** ([[§33 Trace꞉ A Connection Between Matrices and Operators#^ladr-8-50|independent of the basis]], LADR 8.50), and more generally the characteristic polynomial. For $U_2$, every board found determinant $-1$ and trace $0$ for $(1\,2)$, trace $2$ for the identity, and trace $-1$ for the $3$-cycles; this is how the lecturer checked the boards. Note that $\det \rho_{U_2}(g) = \operatorname{sgn}(g)$ in the table. Traces will return later in the course.
>
> *Source: lecture 11/2*

^rem-59-2

> [!theorem] Proposition §59.3: When $k\{1,2,3\} = U_1 \oplus U_2$
> $k\{1,2,3\}$ is the (internal) [[§3 Subspaces#^ladr-1-41|direct sum]] of $U_1$ and $U_2$ if and only if $3 \neq 0$ in $k$. If $3 = 0$ in $k$ (for example $k = \mathbb{F}_3$), then $U_1 \subseteq U_2$.
>
> *Source: WS 13.5; board 11/2*

^prop-59-3

> [!proof]+ Proof
> *Idea:* Put bases of $U_1$ and $U_2$ side by side; the direct sum holds exactly when the resulting $3 \times 3$ matrix is invertible, and its determinant is $3$.
>
> *(Board 11/2.)* $k^3 = U_1 \oplus U_2$ means $U_1 \cap U_2 = \{0\}$ and $U_1 + U_2 = k^3$ ([[§3 Subspaces#^ladr-1-46|LADR 1.46]]), i.e. every vector can be written uniquely as $c_1(1,1,1) + c_2(1,-1,0) + c_3(0,1,-1)$. (Here $(1,-1,0), (0,1,-1)$ is another basis of $U_2$.) That is the same as the matrix with these three columns being invertible, which holds iff its determinant is nonzero ([[§37 Determinants#^ladr-9-50|LADR 9.50]]):
>
> $$
> \det \begin{pmatrix} 1 & 1 & 0 \\ 1 & -1 & 1 \\ 1 & 0 & -1 \end{pmatrix} = 1 + 1 + 1 = 3.
> $$
>
> So if $3 \neq 0$ in $k$, the matrix is invertible and $k^3 = U_1 \oplus U_2$. If $3 = 0$, it is not, and indeed
>
> $$
> (1,-1,0) + 2\,(0,1,-1) = (1, 1, -2) = (1,1,1),
> $$
>
> since $-2 = 1$ when $3 = 0$: the all-ones vector lies in $U_2$. (Directly: $(1,1,1) \in U_2$ iff $1 + 1 + 1 = 0$.)

^pf-59-3

![[m493-59-3.svg]]

*(Not from lecture; figure added.)* The case $3 = 0$: the $27$ vectors of $\mathbb{F}_3^3$, coordinates $0, 1, 2$. The nine vectors with $x + y + z = 0$ form $U_2$ (blue), and the three multiples of $(1,1,1)$, which make up $U_1$ (red rings), all lie among them. So $U_1 \subseteq U_2$, $U_1 + U_2 = U_2 \neq \mathbb{F}_3^3$, and the decomposition fails.

> [!remark] Remark: Why This Is “Tricky”
> The worksheet did not say what the field is, and the answer depends on it. The lecturer's point: subrepresentations and decompositions into them are very useful, but there are subtleties, and fields in which $3 = 0$ (or $p = 0$) are part of the course. Two further observations (not from class): over $\mathbb{F}_3$, the “orthogonal complement” $U_2$ of $U_1$ contains $U_1$, so complements for a dot product need not be complements in the sense of direct sums over arbitrary fields, which is why WS 14 works over $\mathbb{R}$. And $|S_3| = 6$, so Maschke's theorem (WS 14) guarantees a complement whenever $6 \neq 0$ in $k$. Over $\mathbb{F}_2$ its hypothesis fails, yet $3 = 1 \neq 0$ and the decomposition still holds: Maschke's condition is sufficient, not necessary.
>
> *Source: lecture 11/2; the last two observations not from class*

^rem-59-3

> [!definition] Definition §59.4: Homomorphism of Representations
> Let $U$ and $V$ be representations of $G$ over the same field $k$. A **homomorphism of $G$-representations** is a $k$-linear map $\varphi: U \to V$ with
>
> $$
> \varphi\big(\rho_U(g)(u)\big) = \rho_V(g)\big(\varphi(u)\big) \qquad \text{for all } g \in G,\ u \in U,
> $$
>
> that is, $\varphi \circ \rho_U(g) = \rho_V(g) \circ \varphi$, or $\varphi(gu) = g\varphi(u)$.
>
> *Source: WS 13*

^def-59-4

> [!definition] Definition §59.5: Isomorphism of Representations
> An **isomorphism of $G$-representations** is an invertible homomorphism of $G$-representations (Definition [[§59 Representations and Subrepresentations#^def-59-4|§59.4]]).
>
> *Source: WS 13*

^def-59-5

**Transcription note (WS 13).** The worksheet prints the condition as “$\rho_V(\varphi(g)(u)) = \varphi(\rho_U(g)(v))$”, which mixes up the arguments; the definition above is the standard one, and the one the worksheet's problems use.

> [!theorem] Proposition §59.4: Kernels and Images Are Subrepresentations
> Let $\varphi: U \to V$ be a homomorphism of $G$-representations. Then
>
> 1. $\operatorname{Ker}\varphi$ is a subrepresentation of $U$;
> 2. $\operatorname{Im}\varphi$ is a subrepresentation of $V$.
>
> *Source: WS 13.6*

^prop-59-4

> [!proof]+ Proof (to be filled)
> WS 13.6 was not reached in class on 11/2.

^pf-59-4
