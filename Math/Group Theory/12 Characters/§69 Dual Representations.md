---
type: section
subject: "[[Group Theory]]"
chapter: 12
section: 69
tags: [group-theory, math493]
---
← [[§68 Homomorphisms Between Representations]] · ↑ [[· 12 Characters]]

*Source: Lecture (Fri Nov 13). Reference: Axler, *Linear Algebra Done Right*, Section 3F (duality).*

The formula $\chi_{\operatorname{Hom}(V, W)}(g) = \chi_V(g^{-1})\,\chi_W(g)$ (Proposition [[§68 Homomorphisms Between Representations#^prop-68-5|§68.5]]) has two parts: the inverse in $\chi_V(g^{-1})$, and the product. This section explains the inverse. The function $g \mapsto \chi_V(g^{-1})$ is itself a character, the character of the dual representation $V^\vee$ (Proposition [[§69 Dual Representations#^prop-69-5|§69.5]]). The product comes from tensor products, which the lecture of 11/13 only described briefly (the last subsection of this section); the course will mostly use $\operatorname{Hom}$ instead.

## Dual Spaces and Dual Bases

> [!definition] Definition §69.1: Dual Space
> Let $k$ be a field and $V$ a vector space over $k$. The **dual space** of $V$ is
>
> $$
> V^\vee = \operatorname{Hom}(V, k),
> $$
>
> the vector space of linear maps $V \to k$. It is the space $\operatorname{Hom}(V, W)$ of Definition [[§68 Homomorphisms Between Representations#^def-68-1|§68.1]] for $W = k$.
>
> *Source: lecture 11/13*

^def-69-1

> [!remark]- Connections
> - Linear Algebra: [[§12 Duality#^ladr-3-108|LADR 3.108]] (linear functional), [[§12 Duality#^ladr-3-110|LADR 3.110]] (dual space, written $V'$).
> - Differentiable Manifolds: [[§21 Linear Algebra Toolkit#^def-21-1|591 Def. §21.1]] (written $V^{\ast}$); the cotangent space of a manifold is the dual of the tangent space.
> - Functional Analysis: for a normed space the dual consists of the bounded linear functionals, [[§31 Dual Spaces#^def-31-1|556 Def. §31.1]]; in finite dimensions every linear functional is bounded.

Axler writes $V'$ for the dual space and calls its elements linear functionals; MATH 591 writes $V^\ast$.

> [!definition] Definition §69.2: Dual Basis
> Let $V$ be finite-dimensional with basis $e_1, \ldots, e_n$. Every $v \in V$ is $v = \sum_i c_ie_i$ with unique coefficients $c_i \in k$. The **dual basis** $e_1^\ast, \ldots, e_n^\ast$ consists of the maps $e_j^\ast: V \to k$ with
>
> $$
> e_j^\ast\Big(\sum_{i=1}^n c_ie_i\Big) = c_j.
> $$
>
> So $e_j^\ast$ extracts the coefficient of $e_j$. In particular $e_j^\ast(e_i) = 1$ if $i = j$, and $e_j^\ast(e_i) = 0$ if $i \neq j$.
>
> *Source: lecture 11/13*

^def-69-2

> [!remark]- Connections
> - Linear Algebra: [[§12 Duality#^ladr-3-112|LADR 3.112]]; Differentiable Manifolds: [[§21 Linear Algebra Toolkit#^def-21-2|591 Def. §21.2]].

> [!theorem] Proposition §69.1: The Dual Basis Is a Basis
> Let $V$ be finite-dimensional with basis $e_1, \ldots, e_n$, and let $e_1^\ast, \ldots, e_n^\ast$ be the dual basis (Definition [[§69 Dual Representations#^def-69-2|§69.2]]).
>
> 1. Each $e_j^\ast$ is linear, so $e_j^\ast \in V^\vee$.
> 2. Every $f \in V^\vee$ is $f = \sum_{j=1}^n f(e_j)\,e_j^\ast$.
> 3. $e_1^\ast, \ldots, e_n^\ast$ is a basis of $V^\vee$. In particular $V^\vee$ is finite-dimensional, and $\dim V^\vee = \dim V$.
>
> *Source: lecture 11/13 (stated); the proof is not from class*

^prop-69-1

> [!proof]+ Proof
> *Idea:* A linear map is determined by its values on the basis vectors $e_i$, and $e_j^\ast(e_i)$ is $1$ or $0$.
>
> *(Not from class; filled in.)* **(1)** Let $v = \sum_i c_ie_i$ and $v' = \sum_i c_i'e_i$, and let $a, a' \in k$. Then $av + a'v' = \sum_i (ac_i + a'c_i')e_i$, so
>
> $$
> e_j^\ast(av + a'v') = ac_j + a'c_j' = a\,e_j^\ast(v) + a'\,e_j^\ast(v').
> $$
>
> **(2)** Let $h = \sum_j f(e_j)\,e_j^\ast$. It is linear by (1), and $h(e_i) = \sum_j f(e_j)\,e_j^\ast(e_i) = f(e_i)$ for every $i$, because only the summand with $j = i$ is not zero. For $v = \sum_i c_ie_i$, linearity of $f$ and of $h$ gives
>
> $$
> f(v) = \sum_i c_if(e_i) = \sum_i c_ih(e_i) = h(v).
> $$
>
> **(3)** By (2) the $e_j^\ast$ span $V^\vee$. They are linearly independent: if $\sum_j a_je_j^\ast = 0$, then evaluating at $e_i$ gives $a_i = 0$, for every $i$.

^pf-69-1

> [!remark]- Connections
> - Linear Algebra: part (3) is [[§12 Duality#^ladr-3-116|LADR 3.116]] and [[§12 Duality#^ladr-3-111|LADR 3.111]]; the companion formula for vectors, $v = \sum_j e_j^{\ast}(v)\,e_j$, is [[§12 Duality#^ladr-3-114|LADR 3.114]].
> - Differentiable Manifolds: [[§21 Linear Algebra Toolkit#^prop-21-2|591 Prop. §21.2]], which has parts (2) and (3) and the formula for vectors.

Dual spaces of infinite-dimensional vector spaces are left aside in this course.

> [!example] Example §69.1: A Dual Basis in $\mathbb{R}^2$
> *(Not from class.)* Let $e_1 = (1, 0)$ and $e_2 = (1, 1)$ in $\mathbb{R}^2$. Since $(x, y) = (x - y)\,e_1 + y\,e_2$, the dual basis is
>
> $$
> e_1^\ast(x, y) = x - y, \qquad e_2^\ast(x, y) = y.
> $$
>
> 1. For the standard basis $(1, 0)$, $(0, 1)$ the first dual basis vector is $(x, y) \mapsto x$. So $e_1^\ast$ changes when $e_2$ is changed and $e_1$ is kept: the map $e_j^\ast$ depends on the whole basis, not only on $e_j$.
> 2. Written as rows, $e_1^\ast = (1, -1)$ and $e_2^\ast = (0, 1)$. These are the rows of the inverse of the matrix $P = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ whose columns are $e_1$, $e_2$: the equations $e_j^\ast(e_i) = 1$ or $0$ say that (row $j$) times (column $i$ of $P$) is the $(j, i)$ entry of the identity matrix.
>
> *Source: not from class*

^ex-69-1

![[m493-69-1.svg]]

*(Not from lecture; figure added.)* Example [[§69 Dual Representations#^ex-69-1|§69.1]]. The level lines of $e_1^\ast$ (blue) are parallel to $e_2$, and those of $e_2^\ast$ (red) are parallel to $e_1$: the map $e_1^\ast$ is $0$ on $e_2$, so it is constant along the direction of $e_2$. The vector $v = 2e_1 + e_2$ lies on the lines $e_1^\ast = 2$ and $e_2^\ast = 1$, which are its coefficients. Changing $e_2$ turns the blue lines, although $e_1$ stays the same.

> [!remark] Remark: Duals in Coordinates
> Let $V = k^n$ with the standard basis $e_1, \ldots, e_n$. Then $e_j^\ast(v) = v_j$ is the $j$-th coordinate of $v$. It can be written as the dot product $\langle e_j, v \rangle$, or as the matrix product $e_j^Tv$ of a row vector with a column vector. In coordinates one usually does not distinguish $k^n$ from its dual: an element of either is a list of $n$ numbers, written as a column for a vector and as a row for a linear map $k^n \to k$. For this reason, transposes appear whenever statements about duals are written in coordinates.
>
> The dual space itself needs no inner product or other extra structure on $V$. The dot product above is the standard symmetric bilinear form $\langle x, y \rangle = \sum_i x_iy_i$ on $k^n$. It is used only as a way of writing coordinates; positive definiteness (which is part of the definition of an inner product, Definition [[§63 Invariant Inner Products and Maschke over ℝ#^def-63-1|§63.1]]) plays no role.
>
> *Source: lecture 11/13*

^rem-69-1

## Dual Maps

> [!definition] Definition §69.3: Dual Map
> Let $\varphi: V \to W$ be a linear map of $k$-vector spaces. The **dual map** $\varphi^\vee: W^\vee \to V^\vee$ is defined by
>
> $$
> \varphi^\vee(w^\vee)(v) := w^\vee\big(\varphi(v)\big) \qquad (w^\vee \in W^\vee,\ v \in V),
> $$
>
> that is, $\varphi^\vee(w^\vee) = w^\vee \circ \varphi$. It goes in the direction opposite to $\varphi$. The symbols can be combined in only one way: $\varphi$ takes a vector of $V$ and returns a vector of $W$, and a vector of $W$ is what $w^\vee$ takes.
>
> *Source: lecture 11/13*

^def-69-3

> [!remark]- Connections
> - Linear Algebra: [[§12 Duality#^ladr-3-118|LADR 3.118]] (written $T'$); Differentiable Manifolds: [[§21 Linear Algebra Toolkit#^def-21-3|591 Def. §21.3]].

![[m493-69-2.svg]]

*(Board 11/13.)* A linear map $\varphi$ and its dual map $\varphi^\vee$ (Definition [[§69 Dual Representations#^def-69-3|§69.3]]), which goes the other way.

> [!theorem] Proposition §69.2: Duals Reverse Composition
> Let $U \xrightarrow{\alpha} V \xrightarrow{\beta} W$ be linear maps of $k$-vector spaces, and let $\varphi: V \to W$ be linear.
>
> 1. For $w^\vee \in W^\vee$ the map $\varphi^\vee(w^\vee)$ is linear, so it lies in $V^\vee$; and $\varphi^\vee: W^\vee \to V^\vee$ is linear.
> 2. $(\beta \circ \alpha)^\vee = \alpha^\vee \circ \beta^\vee$, where $W^\vee \xrightarrow{\beta^\vee} V^\vee \xrightarrow{\alpha^\vee} U^\vee$.
> 3. $(\mathrm{Id}_V)^\vee = \mathrm{Id}_{V^\vee}$.
> 4. If $\varphi$ is invertible, then $\varphi^\vee$ is invertible, and $(\varphi^\vee)^{-1} = (\varphi^{-1})^\vee$.
>
> *Source: lecture 11/13; parts (1) and (4) are not from class*

^prop-69-2

> [!proof]+ Proof
> *Idea:* $\varphi^\vee$ is composition with $\varphi$ on the right, and composing on the right with $\beta \circ \alpha$ is composing with $\beta$ first and then with $\alpha$.
>
> **(1)** *(Not from class.)* $\varphi^\vee(w^\vee) = w^\vee \circ \varphi$ is a composite of the linear maps $V \xrightarrow{\varphi} W \xrightarrow{w^\vee} k$, so it is linear. For $w_1^\vee, w_2^\vee \in W^\vee$ and $a, b \in k$, the maps $(aw_1^\vee + bw_2^\vee) \circ \varphi$ and $a(w_1^\vee \circ \varphi) + b(w_2^\vee \circ \varphi)$ both have the value $a\,w_1^\vee(\varphi(v)) + b\,w_2^\vee(\varphi(v))$ at every $v \in V$. So $\varphi^\vee(aw_1^\vee + bw_2^\vee) = a\varphi^\vee(w_1^\vee) + b\varphi^\vee(w_2^\vee)$.
>
> **(2)** *(Lecture 11/13.)* For $w^\vee \in W^\vee$,
>
> $$
> (\beta \circ \alpha)^\vee(w^\vee) = w^\vee \circ \beta \circ \alpha = (w^\vee \circ \beta) \circ \alpha = \alpha^\vee(w^\vee \circ \beta) = \alpha^\vee\big(\beta^\vee(w^\vee)\big).
> $$
>
> **(3)** For $v^\vee \in V^\vee$, $(\mathrm{Id}_V)^\vee(v^\vee) = v^\vee \circ \mathrm{Id}_V = v^\vee$.
>
> **(4)** *(Not from class.)* By (2) and (3), $\varphi^\vee \circ (\varphi^{-1})^\vee = (\varphi^{-1} \circ \varphi)^\vee = (\mathrm{Id}_V)^\vee = \mathrm{Id}_{V^\vee}$, and $(\varphi^{-1})^\vee \circ \varphi^\vee = (\varphi \circ \varphi^{-1})^\vee = (\mathrm{Id}_W)^\vee = \mathrm{Id}_{W^\vee}$.

^pf-69-2

> [!remark]- Connections
> - Linear Algebra: [[§12 Duality#^ladr-3-120|LADR 3.120]]; Differentiable Manifolds: [[§21 Linear Algebra Toolkit#^prop-21-4|591 Prop. §21.4]](1).

![[m493-69-3.svg]]

*(Board 11/13.)* Proposition [[§69 Dual Representations#^prop-69-2|§69.2]](2): the dual of the composite $\beta \circ \alpha$ is the composite of the duals in the opposite order. In the language of category theory, which the course does not use, the dual is a contravariant functor.

> [!theorem] Proposition §69.3: The Dual Map Has the Transpose Matrix
> Let $V$ have the basis $v_1, \ldots, v_m$ and $W$ the basis $w_1, \ldots, w_n$. Let $\varphi: V \to W$ be linear with matrix $A$ in these bases: $A$ is the $n \times m$ matrix with
>
> $$
> \varphi(v_i) = \sum_{j=1}^n A_{ji}\,w_j \qquad (i = 1, \ldots, m).
> $$
>
> Column $i$ of $A$ holds the coordinates of the image of the $i$-th basis vector; $j$ is the row index and $i$ the column index. Then
>
> $$
> \varphi^\vee(w_j^\ast) = \sum_{i=1}^m A_{ji}\,v_i^\ast = \sum_{i=1}^m (A^T)_{ij}\,v_i^\ast \qquad (j = 1, \ldots, n).
> $$
>
> That is, in the dual bases $w_1^\ast, \ldots, w_n^\ast$ of $W^\vee$ and $v_1^\ast, \ldots, v_m^\ast$ of $V^\vee$ (Definition [[§69 Dual Representations#^def-69-2|§69.2]]), the matrix of $\varphi^\vee$ is the transpose $A^T$, an $m \times n$ matrix.
>
> *Source: board 11/13*

^prop-69-3

> [!proof]+ Proof
> *Idea:* Evaluate $\varphi^\vee(w_j^\ast)$ on the basis vectors $v_i$; the values are its coefficients in the dual basis.
>
> *(Board 11/13.)* By the definition of the dual map and of the dual basis of $W$,
>
> $$
> \varphi^\vee(w_j^\ast)(v_i) = w_j^\ast\big(\varphi(v_i)\big) = w_j^\ast\Big(\sum_{l=1}^n A_{li}\,w_l\Big) = A_{ji}.
> $$
>
> The map $f = \varphi^\vee(w_j^\ast)$ lies in $V^\vee$, so $f = \sum_i f(v_i)\,v_i^\ast$ (Proposition [[§69 Dual Representations#^prop-69-1|§69.1]](2)). This gives $\varphi^\vee(w_j^\ast) = \sum_i A_{ji}\,v_i^\ast$.
>
> *Reading off the matrix.* The matrix of a linear map has, in row $i$ and column $j$, the coefficient of the $i$-th basis vector of the target in the image of the $j$-th basis vector of the source, as in the display for $\varphi$ in the statement. For $\varphi^\vee$ this coefficient is $A_{ji}$. In the sum $\sum_i A_{ji}\,v_i^\ast$ the summation index $i$ is in the column position of $A$, which is not where the matrix of a map has it; writing $A_{ji} = (A^T)_{ij}$ puts it in the row position. So the matrix of $\varphi^\vee$ is $A^T$.
>
> *Check of the shape.* $A$ is $n \times m$. The map $\varphi^\vee$ goes from the $n$-dimensional space $W^\vee$ to the $m$-dimensional space $V^\vee$, so its matrix must be $m \times n$.

^pf-69-3

*Uses:* [[§69 Dual Representations#^prop-69-1|§69.1]]

> [!remark]- Connections
> - Linear Algebra: [[§12 Duality#^ladr-3-132|LADR 3.132]]; Differentiable Manifolds: [[§21 Linear Algebra Toolkit#^prop-21-4|591 Prop. §21.4]](2).

**Transcription note.** The handwritten notes of 11/13 have $\varphi(w_j) = \sum_j A_{ji}w_i$, the first version on the board. Since $\varphi$ is defined on $V$, the board was corrected, after a question, to $\varphi(v_i) = \sum_j A_{ji}w_j$, the formula of the proposition. The board writes $v_i^\vee$ and $w_j^\vee$ for the dual basis vectors. These notes write $v_i^\ast$ and $w_j^\ast$, as in Definition [[§69 Dual Representations#^def-69-2|§69.2]], and keep $\vee$ for dual spaces, for dual maps, and for an arbitrary element $w^\vee$ of $W^\vee$.

> [!example] Example §69.2: A Dual Map in Coordinates
> *(Not from class.)* Let $\varphi: k^3 \to k^2$ be multiplication by $A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{pmatrix}$, and let $w^\vee = a\,e_1^\ast + b\,e_2^\ast \in (k^2)^\vee$, the row $(a \ \ b)$ (the remark *Duals in Coordinates*). Then $\varphi^\vee(w^\vee) = w^\vee \circ \varphi$ is the map $v \mapsto (a \ \ b)\,Av$, that is, the row
>
> $$
> (a \ \ b)\,A = (a + 4b \quad 2a + 5b \quad 3a + 6b).
> $$
>
> So on rows the dual map is multiplication by $A$ from the right. Its coordinates in the dual basis of $(k^3)^\vee$, written as a column, are
>
> $$
> \begin{pmatrix} a + 4b \\ 2a + 5b \\ 3a + 6b \end{pmatrix} = \begin{pmatrix} 1 & 4 \\ 2 & 5 \\ 3 & 6 \end{pmatrix}\begin{pmatrix} a \\ b \end{pmatrix} = A^T\begin{pmatrix} a \\ b \end{pmatrix},
> $$
>
> as Proposition [[§69 Dual Representations#^prop-69-3|§69.3]] says.
>
> *Source: not from class*

^ex-69-2

## The Dual Representation

> [!definition] Definition §69.4: Dual Representation
> Let $V$ be a representation of $G$ over $k$. The **dual representation** is the vector space $V^\vee$ with
>
> $$
> \rho_{V^\vee}(g) = \rho_V(g^{-1})^\vee \qquad (g \in G).
> $$
>
> Explicitly, for $f \in V^\vee$ and $v \in V$,
>
> $$
> (g \ast f)(v) = f\big(\rho_V(g^{-1})(v)\big) = f(g^{-1}v).
> $$
>
> This is the representation $\operatorname{Hom}(V, k)$ of Definition [[§68 Homomorphisms Between Representations#^def-68-1|§68.1]] for the trivial action of $G$ on $k$, since then $g \ast \alpha = \alpha \circ \rho_V(g^{-1})$.
>
> *Source: lecture 11/13; the last sentence is not from class*

^def-69-4

> [!remark]- Connections
> - Quantum Field Theory: the dual (contragredient) representation of a Lie group and of a Lie algebra, with the same formula $D^{\ast}(g) = D(g^{-1})'$: [[§CB.8 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-8-6|QFT Def. §CB.8.6]].

> [!theorem] Proposition §69.4: The Dual Representation Is a Representation
> Let $V$ be a representation of $G$ over $k$.
>
> 1. The rule $f \ast g := \rho_V(g)^\vee(f) = f \circ \rho_V(g)$ is a right action of $G$ on $V^\vee$ (Definition [[§25 Actions#^def-25-2|§25.2]]).
> 2. The rule $g \ast f := \rho_V(g^{-1})^\vee(f)$ of Definition [[§69 Dual Representations#^def-69-4|§69.4]] is a left action of $G$ on $V^\vee$ by linear maps. So $V^\vee$ is a representation of $G$.
> 3. Let $V$ be finite-dimensional, and let $M$ be the matrix of $\rho_V(g)$ in a basis of $V$. In the dual basis, the matrix of $\rho_{V^\vee}(g)$ is $(M^{-1})^T$, the inverse transpose of $M$.
>
> *Source: board 11/13*

^prop-69-4

> [!proof]+ Proof
> *Idea:* The dual reverses the order of composition, and so does inversion. Two reversals cancel.
>
> *(Board 11/13.)* **(1)** Since $\rho_V$ is a homomorphism (Proposition [[§61 Representations and Subrepresentations#^prop-61-1|§61.1]]) and the dual reverses composition (Proposition [[§69 Dual Representations#^prop-69-2|§69.2]](2)),
>
> $$
> \rho_V(gh)^\vee = \big(\rho_V(g) \circ \rho_V(h)\big)^\vee = \rho_V(h)^\vee \circ \rho_V(g)^\vee.
> $$
>
> So $(f \ast g) \ast h = \rho_V(h)^\vee\big(\rho_V(g)^\vee(f)\big) = \rho_V(gh)^\vee(f) = f \ast (gh)$, and $f \ast e = (\mathrm{Id}_V)^\vee(f) = f$ (Proposition [[§69 Dual Representations#^prop-69-2|§69.2]](3)). These are the axioms of a right action. In matrices this is the rule $(MN)^T = N^TM^T$: the transpose reverses the order of matrix multiplication.
>
> **(2)** A right action becomes a left action when the group element is replaced by its inverse (the mirror image of Proposition [[§25 Actions#^prop-25-1|§25.1]], from Worksheet 4; see the remark *Left and Right Are Interchangeable* in [[§25 Actions|§25]]). Written out: inversion also reverses products, $(gh)^{-1} = h^{-1}g^{-1}$, so
>
> $$
> \rho_{V^\vee}(gh) = \rho_V\big((gh)^{-1}\big)^\vee = \big(\rho_V(h^{-1}) \circ \rho_V(g^{-1})\big)^\vee = \rho_V(g^{-1})^\vee \circ \rho_V(h^{-1})^\vee = \rho_{V^\vee}(g) \circ \rho_{V^\vee}(h),
> $$
>
> and $\rho_{V^\vee}(e) = (\mathrm{Id}_V)^\vee = \mathrm{Id}_{V^\vee}$. Each $\rho_{V^\vee}(g)$ is linear (Proposition [[§69 Dual Representations#^prop-69-2|§69.2]](1)). So $g \ast f = \rho_{V^\vee}(g)(f)$ is a left action of $G$ on $V^\vee$ by linear maps, which is a representation (Definition [[§61 Representations and Subrepresentations#^def-61-1|§61.1]]).
>
> **(3)** The matrix of $\rho_V(g^{-1}) = \rho_V(g)^{-1}$ is $M^{-1}$. By Proposition [[§69 Dual Representations#^prop-69-3|§69.3]], applied to $\varphi = \rho_V(g^{-1}): V \to V$ with the same basis of $V$ on both sides, the matrix of $\rho_V(g^{-1})^\vee$ in the dual basis is $(M^{-1})^T$.

^pf-69-4

*Uses:* [[§61 Representations and Subrepresentations#^prop-61-1|§61.1]], [[§69 Dual Representations#^prop-69-2|§69.2]], [[§25 Actions#^prop-25-1|§25.1]], [[§61 Representations and Subrepresentations#^def-61-1|Def. §61.1]], [[§69 Dual Representations#^prop-69-3|§69.3]]

> [!theorem] Proposition §69.5: The Character of the Dual Representation
> Let $V$ be a finite-dimensional representation of $G$. Then for every $g \in G$
>
> $$
> \chi_{V^\vee}(g) = \chi_V(g^{-1}).
> $$
>
> *Source: board 11/13*

^prop-69-5

> [!proof]+ Proof
> *(Board 11/13.)* Choose a basis of $V$, and let $N$ be the matrix of $\rho_V(g^{-1})$ in it. In the dual basis the matrix of $\rho_{V^\vee}(g)$ is $N^T$ (Proposition [[§69 Dual Representations#^prop-69-4|§69.4]](3)). A matrix and its transpose have the same diagonal entries, so they have the same trace (Definition [[§66 Invariant Vectors#^def-66-1|§66.1]]):
>
> $$
> \chi_{V^\vee}(g) = \operatorname{Tr}(N^T) = \operatorname{Tr}(N) = \operatorname{Tr}\rho_V(g^{-1}) = \chi_V(g^{-1}).
> $$

^pf-69-5

*Uses:* [[§69 Dual Representations#^prop-69-4|§69.4]], [[§66 Invariant Vectors#^def-66-1|Def. §66.1]]

The same formula follows from Proposition [[§68 Homomorphisms Between Representations#^prop-68-5|§68.5]] for $W = k$ with the trivial action, where $\chi_W(g) = 1$ and $\operatorname{Hom}(V, k) = V^\vee$ as representations (Definition [[§69 Dual Representations#^def-69-4|§69.4]]).

> [!theorem] Corollary §69.6: Dual Characters over $\mathbb{R}$ and $\mathbb{C}$
> Let $G$ be a finite group and $V$ a finite-dimensional representation of $G$ over $k$.
>
> 1. If $k = \mathbb{R}$, then $\chi_{V^\vee} = \chi_V$.
> 2. If $k = \mathbb{C}$, then $\chi_{V^\vee} = \overline{\chi_V}$.
>
> *Source: lecture 11/13 (stated)*

^cor-69-6

> [!proof]+ Proof
> By Proposition [[§69 Dual Representations#^prop-69-5|§69.5]], $\chi_{V^\vee}(g) = \chi_V(g^{-1})$. Over $\mathbb{R}$ this is $\chi_V(g)$ (WS 16.3, Proposition [[§68 Homomorphisms Between Representations#^prop-68-8|§68.8]]), and over $\mathbb{C}$ it is $\overline{\chi_V(g)}$ (WS 16.5, Corollary [[§68 Homomorphisms Between Representations#^cor-68-10|§68.10]]). The lecture of 11/13 recalled these two statements without proof; their proofs in these notes are filled in.

^pf-69-6

*Uses:* [[§69 Dual Representations#^prop-69-5|§69.5]], [[§68 Homomorphisms Between Representations#^prop-68-8|§68.8]], [[§68 Homomorphisms Between Representations#^cor-68-10|§68.10]]

> [!remark] Remark: Where the Inverse Comes From
> By Proposition [[§69 Dual Representations#^prop-69-5|§69.5]], the formula of Proposition [[§68 Homomorphisms Between Representations#^prop-68-5|§68.5]] reads
>
> $$
> \chi_{\operatorname{Hom}(V, W)}(g) = \chi_{V^\vee}(g)\,\chi_W(g).
> $$
>
> The inverse belongs to $V^\vee$ alone and appears without $W$. It is forced by the requirement that the action on the dual space be a left action: whenever a group acts on a vector space by matrices, the action on the dual space, as a left action, is by the inverse transposes.
>
> *Source: lecture 11/13*

^rem-69-2

> [!remark]- Connections
> - Quantum Field Theory: the product has the same explanation, $\operatorname{Hom}(V, W) \cong V^{\ast} \otimes W$ as representations, and its invariants are the homomorphisms of representations: [[§CB.8 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-8-9|QFT Thm. §CB.8.9]].

> [!example] Example §69.3: The Dual of a Rotation Representation
> *(Not from class.)* Let $G = \mathbb{Z}/4\mathbb{Z}$ act on $V = \mathbb{R}^2$, the generator $g$ acting by the rotation by $90^\circ$, $M = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$, so that $g(x, y) = (-y, x)$ and $g^{-1}(x, y) = (y, -x)$. For the dual basis $e_1^\ast(x, y) = x$, $e_2^\ast(x, y) = y$ of the standard basis:
>
> $$
> (g \ast e_1^\ast)(x, y) = e_1^\ast(y, -x) = y, \qquad (g \ast e_2^\ast)(x, y) = e_2^\ast(y, -x) = -x.
> $$
>
> So $g \ast e_1^\ast = e_2^\ast$ and $g \ast e_2^\ast = -e_1^\ast$.
>
> 1. In the dual basis the matrix of $\rho_{V^\vee}(g)$ has the columns $(0, 1)$ and $(-1, 0)$. It is $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} = (M^{-1})^T$, as in Proposition [[§69 Dual Representations#^prop-69-4|§69.4]](3), because $M^{-1} = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$.
> 2. Here $(M^{-1})^T = M$. This holds for every [[§3 Basic Examples of Groups#^def-3-8|orthogonal matrix]] $M$, since $M^TM = I$ means $M^{-1} = M^T$. So when a group acts by orthogonal matrices in some basis, the dual representation has the same matrices in the dual basis.
> 3. The characters agree, $\chi_{V^\vee} = \chi_V$, with the values $2, 0, -2, 0$ at $e, g, g^2, g^3$, as in Corollary [[§69 Dual Representations#^cor-69-6|§69.6]](1).
>
> *Source: not from class*

^ex-69-3

![[m493-69-4.svg]]

*(Not from lecture; figure added.)* Example [[§69 Dual Representations#^ex-69-3|§69.3]]. Left: the level lines of $f = e_1^\ast$ and a vector $v$ with $f(v) = 2$. Right: the level lines of $g \ast f$. Since $(g \ast f)(gv) = f(g^{-1}gv) = f(v)$, the map $g \ast f$ takes at $gv$ the value that $f$ takes at $v$. So the level lines of $g \ast f$ are the level lines of $f$ moved by $g$. The inverse in the definition is what makes the picture of $f$ move with $g$.

> [!example] Example §69.4: The Dual of a One-Dimensional Representation
> *(Not from class.)* Let $V = k$ be the one-dimensional representation given by a character $\chi: G \to k^\times$, so $g$ acts as multiplication by $\chi(g)$ (Example [[§61 Representations and Subrepresentations#^ex-61-2|§61.2]]). The $1 \times 1$ matrix of $\rho_V(g)$ is $\chi(g)$, and its inverse transpose is $\chi(g)^{-1}$. So $V^\vee$ is the one-dimensional representation given by the character $g \mapsto \chi(g)^{-1}$.
>
> 1. For the [[§61 Representations and Subrepresentations#^ex-61-1|trivial]] and the sign representation, $\chi(g) = \pm 1$ and $\chi(g)^{-1} = \chi(g)$: each of them has the same character as its dual.
> 2. Let $G = \mathbb{Z}/3\mathbb{Z}$ and $k = \mathbb{C}$, with $\chi(j) = \omega^j$, $\omega = e^{2\pi i/3}$. The dual has the character $j \mapsto \omega^{-j} = \overline{\omega^j}$, the complex conjugate of $\chi$, as in Corollary [[§69 Dual Representations#^cor-69-6|§69.6]](2). Here $V^\vee$ is not isomorphic to $V$. An isomorphism of representations $\varphi: V \to V^\vee$ (Definition [[§61 Representations and Subrepresentations#^def-61-5|§61.5]]) would satisfy $\varphi(\omega v) = \omega^{-1}\varphi(v)$ for the generator, that is, $\omega\,\varphi(v) = \omega^{-1}\varphi(v)$; with $\varphi(v) \neq 0$ this gives $\omega^2 = 1$, which is false.
>
> *Source: not from class*

^ex-69-4

## A Word on Tensor Products

> [!remark] Remark: Tensor Products (Overview)
> The lecture of 11/13 described tensor products only in outline, without proofs. There are several ways to put two vector spaces $V$ and $W$ together.
>
> 1. The [[§62 Direct Sums and Maschke's Theorem#^def-62-1|direct sum]] $V \oplus W$ adds dimensions. A basis of it is the disjoint union of a basis of $V$ and a basis of $W$.
> 2. $\operatorname{Hom}(V, W)$ multiplies dimensions ([[§68 Homomorphisms Between Representations|§68]]).
> 3. The **tensor product** $V \otimes W$ also multiplies dimensions. In the description that depends most on bases: if $V$ has the basis $v_i$ and $W$ the basis $w_j$, then $V \otimes W$ has the basis $v_i \otimes w_j$, so its elements are the sums $\sum_{i,j} c_{ij}\,(v_i \otimes w_j)$.
>
> The symbol $\otimes$ is bilinear, so it distributes over sums of arbitrary vectors $x_i \in V$ and $y_j \in W$, not only basis vectors:
>
> $$
> \Big(\sum_i x_i\Big) \otimes \Big(\sum_j y_j\Big) = \sum_{i,j} x_i \otimes y_j.
> $$
>
> Linear maps $V \to V'$ and $W \to W'$ act on $V \otimes W$: apply them to the two factors of each term and expand the result in the bases of $V'$ and $W'$. The fact that is not obvious, and was not proved, is that all of this is independent of the bases.
>
> Tensor products are where the product in $\chi_{\operatorname{Hom}(V, W)}(g) = \chi_V(g^{-1})\,\chi_W(g)$ comes from, but the course will almost always use $\operatorname{Hom}$ instead. Tensor products are essential in quantum mechanics and quantum computing: the state space of several qubits is a tensor product with one factor for each qubit.
>
> *Source: lecture 11/13; overview only*

^rem-69-3

> [!remark]- Connections
> - Linear Algebra: Axler defines $V \otimes W$ without bases, as the space of bilinear functionals on $V' \times W'$, [[§38 Tensor Products#^ladr-9-71|LADR 9.71]]; its dimension is $\dim V \cdot \dim W$ ([[§38 Tensor Products#^ladr-9-72|LADR 9.72]]), $\otimes$ is bilinear ([[§38 Tensor Products#^ladr-9-73|LADR 9.73]]), and the $v_i \otimes w_j$ form a basis ([[§38 Tensor Products#^ladr-9-74|LADR 9.74]]).
> - Differentiable Manifolds: multilinear forms on a vector space, [[§75 Multilinear Algebra#^def-75-1|591 Def. §75.1]].
> - Quantum Field Theory: the tensor product of two representations of a group, [[§CB.8 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-8-1|QFT Def. §CB.8.1]].
