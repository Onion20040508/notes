---
type: section
subject: "[[Group Theory]]"
chapter: 6
section: 32
tags: [group-theory, math493]
---
← [[§31 G Acting on Coset Spaces]] · ↑ [[· 6 Group Actions, Cosets, and Lagrange's Theorem]] · [[§33 Conjugacy Classes]] →

*Reference: Not treated in Pinter.*

> [!theorem] Proposition §32.1: $GL_3(\mathbb{R})$ Acting on $\mathbb{R}^3$
> Let $GL_3(\mathbb{R})$ act on $\mathbb{R}^3$ by matrix multiplication.
> 1. There are exactly two orbits: $\{0\}$ and $\mathbb{R}^3 \setminus \{0\}$.
> 2. $\operatorname{Stab}(e_1) = \left\{ \begin{pmatrix} 1 & b \\ 0 & B \end{pmatrix} : b \in \mathbb{R}^{1 \times 2},\ B \in GL_2(\mathbb{R}) \right\}$, the invertible matrices whose first column is $e_1$.
>
> *Source: WS 4.7*

^prop-32-1

> [!proof]+ Proof
> **(1)** $A0 = 0$ for every $A$, so $\{0\}$ is an orbit. If $v \neq 0$, extend $v$ to a basis $(v, v_2, v_3)$ of $\mathbb{R}^3$; the matrix $P = [\,v \mid v_2 \mid v_3\,]$ is invertible and $Pe_1 = v$. Hence every nonzero vector lies in the orbit of $e_1$, and $\mathbb{R}^3 \setminus \{0\}$ is a single orbit.
>
> **(2)** $Ae_1$ is the first column of $A$, so $Ae_1 = e_1$ says exactly that the first column is $e_1$: $A = \begin{pmatrix} 1 & b \\ 0 & B \end{pmatrix}$. Expanding $\det A$ along the first column gives $\det A = \det B$, so $A$ is invertible iff $B \in GL_2(\mathbb{R})$; the row $b$ is unconstrained.

^pf-32-1

*Uses:* [[§3 Basic Examples of Groups#^def-3-6|Def. §3.6]], [[§27 Orbits#^def-27-1|Def. §27.1]], [[§26 Stabilizers and Fixed Points#^def-26-1|Def. §26.1]], [[§5 Bases#^ladr-2-32|LADR 2.32]], [[§37 Determinants#^ladr-9-50|LADR 9.50]]

> [!remark] Remark: $GL_3$ versus $O_3$
> Both stabilizers are “matrices with first column $e_1$,” but in $O_3$ orthonormality of the columns additionally forces the first *row* to be $(1,0,0)$, killing the block $b$ and restricting $B$ to $O_2$. Correspondingly the $GL_3$-orbit of $e_1$ is all nonzero vectors, while the $O_3$-orbit is only the unit sphere: a smaller group has smaller orbits and, by [[§30 Orbit–Stabilizer#^thm-30-3|orbit–stabilizer]], the two effects are linked through $|G| = |Gx|\cdot|\operatorname{Stab}(x)|$ (here in the infinite form $G/\operatorname{Stab}(x) \leftrightarrow Gx$).

^rem-32-1

> [!remark]- Connections
> - The same action for all real matrix groups in 591: [[§13 Group Actions and Orbit Spaces#^ex-13-1|591 Ex. §13.1]].

> [!theorem] Proposition §32.2: $O_3(\mathbb{R})$ Acting on $\mathbb{R}^3$
> Let $O_3(\mathbb{R}) = \{A : A^{\mathsf{T}}A = I\}$ act on $\mathbb{R}^3$ by matrix multiplication.
> 1. The orbits are $\{0\}$ and the spheres $S_r = \{v : |v| = r\}$, $r > 0$; so $O_3 \backslash \mathbb{R}^3 \leftrightarrow \mathbb{R}_{\geq 0}$, an orbit corresponding to its radius.
> 2. $\operatorname{Stab}(e_1) = \left\{ \begin{pmatrix} 1 & 0 \\ 0 & B \end{pmatrix} : B \in O_2(\mathbb{R}) \right\} \cong O_2(\mathbb{R})$, the orthogonal transformations of the plane $e_1^\perp$.
>
> *Source: WS 4.8, lecture*

^prop-32-2

> [!proof]+ Proof
> **(1)** Orthogonal matrices preserve the inner product $v^{\mathsf{T}}w$: $(Av)^{\mathsf{T}}(Aw) = v^{\mathsf{T}}A^{\mathsf{T}}Aw = v^{\mathsf{T}}w$. In particular $|Av|^2 = (Av)^{\mathsf{T}}(Av) = v^{\mathsf{T}}v = |v|^2$, so each orbit lies in a single sphere $S_r$ (or is $\{0\}$). Conversely, given $v, w$ with $|v| = |w| = r > 0$, extend $v/r$ to an orthonormal basis $(v/r, v_2, v_3)$ and $w/r$ to $(w/r, w_2, w_3)$ ([[Gram–Schmidt procedure|Gram–Schmidt]]); the matrices $P = [\,v/r \mid v_2 \mid v_3\,]$ and $Q = [\,w/r \mid w_2 \mid w_3\,]$ are orthogonal (orthonormal columns), and $A = QP^{-1} = QP^{\mathsf{T}}$ is orthogonal with $Av = Q(P^{\mathsf{T}}v) = Q(re_1) = w$. So $O_3$ acts transitively on each sphere.
>
> **(2)** $Ae_1 = e_1$ means the first column of $A$ is $e_1$. Orthonormality of the columns then forces the first row to be $(1, 0, 0)$ as well (the other columns are orthogonal to $e_1$), so $A = \begin{pmatrix} 1 & 0 \\ 0 & B \end{pmatrix}$, and $A^{\mathsf{T}}A = I$ iff $B^{\mathsf{T}}B = I$. The map $B \mapsto \begin{pmatrix} 1 & 0 \\ 0 & B \end{pmatrix}$ is an injective homomorphism $O_2 \to O_3$ (block multiplication) with image the stabilizer.

^pf-32-2

*Uses:* [[§3 Basic Examples of Groups#^def-3-8|Def. §3.8]], [[§27 Orbits#^def-27-1|Def. §27.1]], [[§27 Orbits#^def-27-2|Def. §27.2]], [[§26 Stabilizers and Fixed Points#^def-26-1|Def. §26.1]], [[§21 Orthonormal Bases#^ladr-6-36|LADR 6.36]], [[§21 Orthonormal Bases#^ladr-6-32|LADR 6.32]], [[§26 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-49|LADR 7.49]], [[§15 Homomorphisms#^def-15-1|Def. §15.1]]

![[m493-30-2.svg]]
*Left: $GL_3(\mathbb{R})$ has two orbits on $\mathbb{R}^3$, the origin (red) and everything else (blue); any $v \neq 0$ is reached from $e_1$ by an invertible $P$ with first column $v$. Right: $O_3(\mathbb{R})$ preserves length, so its orbits are the origin and the spheres $S_r$ (blue), and $e_1$ reaches only the vectors $w$ with $|w| = 1$. The stabilizer of $e_1$ acts as $O_2(\mathbb{R})$ on the plane $e_1^\perp$, moving the great circle $e_1^\perp \cap S_1$ (red) within itself.*

> [!remark]- Connections
> - In 591 the rotation version makes the unit sphere a homogeneous space, SO(3)/SO(2) ≅ S², [[§14 Homogeneous Spaces#^ex-14-3|591 Ex. §14.3]] (orbits as in [[§13 Group Actions and Orbit Spaces#^ex-13-5|591 Ex. §13.5]]); O(n) also acts transitively on the Grassmannians, [[§15 The Topology of G∕H and Real Grassmannians#^prop-15-6|591 Prop. §15.6]].
> - Used in Relativity: the orbits of the Lorentz group are hyperboloids and light cones, where those of the rotations are spheres — [[§B1.3 Causal Structure and Proper Time#^rem-b1-3-1|REL Remark: Normal forms, and the orbits of the Lorentz group]].

> [!theorem] Proposition §32.3: Rotational Symmetries of the Cube
> Let $C = [-1,1]^3 \subseteq \mathbb{R}^3$ be the cube and let $G$ be its group of rotational symmetries (the symmetries realizable by physically turning the cube; as matrices, $G = \operatorname{Sym}(C) \cap SO_3(\mathbb{R})$).
> 1. $|G| = 24$.
> 2. The orbits and stabilizers of the three points named on the worksheet, together with the action on colours, are
>
> | point | orbit | $\vert$orbit$\vert$ | $\vert\operatorname{Stab}\vert$ |
> |---|:---:|:---:|:---:|
> | $(1,0,0)$, a face centre | the $6$ face centres | $6$ | $4$ |
> | $(1,1,0)$, an edge midpoint | the $12$ edge midpoints | $12$ | $2$ |
> | $(1,1,1)$, a vertex | the $8$ vertices | $8$ | $3$ |
> | a colour (pair of opposite faces) | the $3$ colours | $3$ | $8$ |
>
> In each row $|\operatorname{orbit}| \cdot |\operatorname{Stab}| = 24 = |G|$, as orbit–stabilizer requires.
>
> 3. If reflections are allowed — i.e. $G_{\mathrm{all}} = \operatorname{Sym}(C) \cap O_3(\mathbb{R})$ — then $|G_{\mathrm{all}}| = 48$.
>
> *Source: WS 4.9, lecture*

^prop-32-3

> [!proof]+ Proof
> **(1)** Apply [[§30 Orbit–Stabilizer#^thm-30-3|orbit–stabilizer]] to the action on the six faces. The action is transitive: any face can be brought to the top, so the orbit has $6$ elements. The stabilizer of a face consists of the rotations about the axis through its centre, namely by $0^\circ, 90^\circ, 180^\circ, 270^\circ$, so $|\operatorname{Stab}| = 4$. Hence $|G| = 6 \cdot 4 = 24$. (Informally: pick the cube up and set it down again — any of $6$ faces on top, then $4$ ways to turn it.)
>
> **(2)** Each row is the same computation.
> *Face centres:* the $6$ centres form one orbit, stabilizer the $4$ rotations about that face axis.
> *Edge midpoints:* a cube has $12$ edges and every edge can be carried to every other, so the orbit has $12$ points; the stabilizer of a midpoint is generated by the $180^\circ$ rotation about the axis through that midpoint and the midpoint of the opposite edge, so it has order $2$.
> *Vertices:* there are $8$, forming one orbit; the stabilizer of a vertex is generated by the $120^\circ$ rotation about the body diagonal through it, of order $3$.
> *Colours:* colour the cube with three colours so that opposite faces match. The group permutes the $3$ colours transitively, and the stabilizer of a colour — the symmetries carrying that pair of opposite faces to itself — has order $8$: four rotations about the axis of that pair, and four more that exchange the two faces of the pair.
>
> **(3)** Same count with reflections allowed: still $6$ faces in the orbit, but now $8$ ways to place a given face (the $4$ rotations and their $4$ mirror images), so $|G_{\mathrm{all}}| = 6 \cdot 8 = 48$.

^pf-32-3

*Uses:* [[§30 Orbit–Stabilizer#^thm-30-3|§30.3]], [[§27 Orbits#^def-27-1|Def. §27.1]], [[§27 Orbits#^def-27-3|Def. §27.3]], [[§26 Stabilizers and Fixed Points#^def-26-1|Def. §26.1]]

![[m493-30-1.svg]]
*Left: a net of the three-coloured cube from lecture (opposite faces share a colour). Right: the three kinds of rotation axis, each through one of the worksheet's points — face axis through $(1,0,0)$, edge axis through $(1,1,0)$, vertex axis through $(1,1,1)$ — with the order of the rotations about it.*

> [!remark] Remark: Choosing the Set $X$
> The first three rows are orbits of the action on the cube itself, $X = C$; the fourth is not, since no point of $C$ “is” a colour — the colour row uses a different set, $X = \{\text{the three colours}\}$. A group does not come with one set attached: the same $G$ acts on many sets, and each choice exposes different structure. Different orbits of a single action also behave differently, which is why the worksheet asks about three separate points rather than about “the orbit of the cube”.

^rem-32-2

> [!theorem] Proposition §32.4: The Cube Group Embeds in $S_6$
> The action of the rotation group $G$ of the cube on its six faces is faithful. Hence the associated homomorphism $\varphi: G \to S_6$ is injective, and $G$ is isomorphic to a subgroup of $S_6$ of order $24$.
>
> *Source: question raised in class*

^prop-32-4

> [!proof]+ Proof
> A rotation fixing each of the six faces fixes each face centre, in particular $e_1, e_2, e_3$; being linear, it is the identity. So the action has trivial kernel, and the conclusion is [[§25 Actions#^prop-25-4|Faithful Actions Embed G in S_X, §25.4]].

^pf-32-4

*Uses:* [[§25 Actions#^def-25-4|Def. §25.4]], [[§25 Actions#^def-25-5|Def. §25.5]], [[§25 Actions#^prop-25-4|§25.4]], [[§20 Polynomial Rings, Permutation Matrices, and Representations#^thm-20-2|§20.2]], [[§7 Vector Space of Linear Maps#^ladr-3-4|LADR 3.4]]

> [!example] Example §32.1: A Non-Faithful Action: Colours
> The action on the three colours (pairs of opposite faces) is not faithful: every $180^\circ$ rotation about a face axis carries each pair of opposite faces to itself, so these non-identity rotations lie in the kernel of $G \to S_3$.

^ex-32-1

> [!theorem] Theorem §32.5: The Rotation Group of the Cube Is $S_4$
> The action of the rotation group $G$ of the cube on its four body diagonals gives an isomorphism $G \cong S_4$.
>
> *Source: not from class*

^thm-32-5

> [!proof]- Proof
> *[To be proved.]*

^pf-32-5

![[m493-30-3.svg]]
*The four body diagonals of $C = [-1,1]^3$, numbered $1$–$4$ at their upper ends; each joins a vertex to the opposite vertex through the centre. Every rotation of the cube permutes these four lines, which is the homomorphism $G \to S_4$ of §32.5.*

> [!remark] Remark: The Cleanest Description
> Since $|G| = 24 = |S_4|$, it is enough to show that the homomorphism $G \to S_4$ is injective, i.e. that the action on the diagonals is faithful. This identification is the cleanest description of the rotation group.

^rem-32-3

*The recurring groups as Chapter 6 saw them. $GL_3$, $O_3$ and the cube are treated in full above; the parts below gather the chapter's other appearances of each group, in order.*

## The Symmetric Group S₃

$S_3$ is the chapter's test case for cosets: its left and right cosets of $\langle (1\,2) \rangle$ differ, and recording $\alpha(3)$ and $\alpha^{-1}(3)$ explains why. It is also where $\mathbb{Z}/3\mathbb{Z}$ lands when it rotates a triangle.

![[§25 Actions#^ex-25-3]]

![[§28 Left and Right Cosets#^ex-28-1]]

![[§28 Left and Right Cosets#^ex-28-2]]

![[§29 The Index and Lagrange's Theorem#^ex-29-2]]

![[§30 Orbit–Stabilizer#^ex-30-2]]

Burnside's lemma for $S_3$ on $\{1, 2, 3\}$ and on itself is in [[§30 Orbit–Stabilizer#^ex-30-3|Burnside's Lemma in Action]] (in the cube part).

*$S_3$ elsewhere:* ← [[§23 S₃, Aₙ, Uₙ and GLₙ#The Symmetric Group S₃|Chapter 5]] · [[§36 S₃, S₄ and GLₙ#The Symmetric Group S₃|Chapter 7]] → · [[The symmetric group S₃|all appearances]]

## S₄, A₄ and the Klein Four-Group V

$A_4$ refutes the converse of Lagrange: $6$ divides $|A_4| = 12$, but $A_4$ has no subgroup of order $6$. The class sizes $1, 6, 3, 8, 6$ of $S_4$ are announced as an instance of orbit–stabilizer, and $S_4$ turns out to be the rotation group of the cube. The Klein four-group, met in [[§19 S₃, ℤ∕nℤ and Uₙ#ℤ∕nℤ and Uₙ|Chapter 4]] as $U_8 \cong \mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/2\mathbb{Z}$, is one of the two groups of order $4$.

![[§29 The Index and Lagrange's Theorem#^ex-29-1]]

![[§30 Orbit–Stabilizer#^rem-30-2]]

The two groups of order $4$ are named in [[§29 The Index and Lagrange's Theorem#^rem-29-3|A Classification, for Once]] (in the ℤ/nℤ part); [[§32 Linear Groups, the Cube, S₃ and A₄#^thm-32-5|The Rotation Group of the Cube Is S₄]] and [[§32 Linear Groups, the Cube, S₃ and A₄#^rem-32-3|The Cleanest Description]] are above in this section.

*$S_4$, $A_4$ and $V$ elsewhere:* first appearance · [[§36 S₃, S₄ and GLₙ#S₄, A₄ and the Klein Four-Group V|Chapter 7]] → · [[S₄, A₄ and the Klein four-group|all appearances]]

## ℤ∕nℤ and Uₙ
Lagrange's theorem pays off for the cyclic groups: Fermat's little theorem is Lagrange in $U_p$, and every group of prime order $p$ is $\mathbb{Z}/p\mathbb{Z}$, the chapter's one complete classification. $\mathbb{Z}/3\mathbb{Z}$ and $\mathbb{Z}/4\mathbb{Z}$ also serve as small groups acting on sets.

![[§29 The Index and Lagrange's Theorem#^cor-29-4]]

![[§29 The Index and Lagrange's Theorem#^thm-29-7]]

![[§29 The Index and Lagrange's Theorem#^rem-29-3]]

The actions of $\mathbb{Z}/3\mathbb{Z}$ on a triangle and of $\mathbb{Z}/4\mathbb{Z}$ on two points are in [[§25 Actions#^ex-25-3|Seeing the Permutations]] (in the $S_3$ part).

*$\mathbb{Z}/n\mathbb{Z}$ and $U_n$ elsewhere:* ← [[§23 S₃, Aₙ, Uₙ and GLₙ#ℤ∕nℤ and Uₙ|Chapter 5]] · [[§45 S₃, S₄, A₄ and A₅#ℤ∕nℤ and Uₙ|Chapter 8]] → · [[ℤ∕nℤ and the unit groups Uₙ|all appearances]]

## GLₙ, SLₙ and O(n)

$GL_n(k)$ acts on $k^n$, and by Cayley's theorem and permutation matrices every finite group sits inside some $GL_n(k)$. The orbits and stabilizers of $GL_3(\mathbb{R})$ and $O_3(\mathbb{R})$ on $\mathbb{R}^3$ are worked out above.

![[§25 Actions#^ex-25-2]]

![[§25 Actions#^cor-25-6]]

Above in this section: [[§32 Linear Groups, the Cube, S₃ and A₄#^prop-32-1|GL₃(ℝ) Acting on ℝ³]], [[§32 Linear Groups, the Cube, S₃ and A₄#^rem-32-1|GL₃ versus O₃]], [[§32 Linear Groups, the Cube, S₃ and A₄#^prop-32-2|O₃(ℝ) Acting on ℝ³]].

*$GL_n$ elsewhere:* ← [[§23 S₃, Aₙ, Uₙ and GLₙ#GLₙ, SLₙ and O(n)|Chapter 5]] · [[§36 S₃, S₄ and GLₙ#GLₙ, SLₙ and O(n)|Chapter 7]] → · [[Matrix groups GLₙ, SLₙ and O(n)|all appearances]]

## The Rotation Group of the Cube

The rotation group of the cube is the chapter's geometric example: one group of order $24$ acting on faces, edges, vertices, colours and body diagonals. Before the full treatment above, it appears as a group of permutations of the faces and in Burnside's count.

![[§30 Orbit–Stabilizer#^ex-30-3]]

Two rotations become permutations of the faces in [[§25 Actions#^ex-25-3|Seeing the Permutations]] (in the $S_3$ part). Above in this section: [[§32 Linear Groups, the Cube, S₃ and A₄#^prop-32-3|Rotational Symmetries of the Cube]], [[§32 Linear Groups, the Cube, S₃ and A₄#^prop-32-4|The Cube Group Embeds in S₆]], [[§32 Linear Groups, the Cube, S₃ and A₄#^ex-32-1|A Non-Faithful Action: Colours]], [[§32 Linear Groups, the Cube, S₃ and A₄#^thm-32-5|The Rotation Group of the Cube Is S₄]].

*The cube elsewhere:* only in this chapter · [[Rotation group of the cube|all appearances]]
