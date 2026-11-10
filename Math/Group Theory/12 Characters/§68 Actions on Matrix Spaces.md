---
type: section
subject: "[[Group Theory]]"
chapter: 12
section: 68
tags: [group-theory, math493]
---
← [[§67 Characters of Representations]] · ↑ [[· 12 Characters]]

*Source: Worksheet 16 (handed out Mon Nov 9). The worksheet's problems and its theorem are stated here; the lecture on it has not been held yet, so all proofs are filled in and will be replaced by the board proofs. Reference: Axler, *Linear Algebra Done Right* (matrices of linear maps, eigenvalues).*

Theorem [[§66 Invariant Vectors#^thm-66-10|§66.10]] computes the dimension of the invariant vectors of any representation from its character. This section applies it to the representation $\operatorname{Hom}(V, W)$, whose invariant vectors are the homomorphisms of representations $V \to W$ (Proposition [[§66 Invariant Vectors#^prop-66-9|§66.9]]). The result is a formula for the number of independent homomorphisms between two representations in terms of their characters. Over $\mathbb{R}$ and $\mathbb{C}$ the formula simplifies, because there $\chi_V(g^{-1})$ is $\chi_V(g)$ or its complex conjugate.

> [!definition] Definition §68.1: The Representation $\operatorname{Hom}(V, W)$
> Let $V$ and $W$ be representations of a group $G$ over $k$, and let $\operatorname{Hom}(V, W)$ be the vector space of linear maps from $V$ to $W$. For $g \in G$ and $\alpha \in \operatorname{Hom}(V, W)$ set
>
> $$
> g \ast \alpha = \rho_W(g) \circ \alpha \circ \rho_V(g^{-1}).
> $$
>
> *Source: WS 16*

^def-68-1

**Transcription note.** Worksheet 16 prints $g \ast \alpha = \rho_V(g) \circ \alpha \circ \rho_W(g^{-1})$. For $\alpha: V \to W$ these maps cannot be composed unless $V = W$: $\rho_W(g^{-1})$ acts on $W$, but $\alpha$ is defined on $V$. With $V$ and $W$ exchanged, as in Definition [[§68 Actions on Matrix Spaces#^def-68-1|§68.1]], the composition makes sense, and the invariant maps are the $\alpha$ with $\alpha \circ \rho_V = \rho_W \circ \alpha$, as the worksheet says next. This is the action $(g \cdot A)(w) = g\,A(g^{-1}w)$ of Proposition [[§66 Invariant Vectors#^prop-66-9|§66.9]](1). The exchange also affects WS 16.2 (Proposition [[§68 Actions on Matrix Spaces#^prop-68-3|§68.3]]) but not the worksheet's theorem (Theorem [[§68 Actions on Matrix Spaces#^thm-68-4|§68.4]]).

> [!theorem] Proposition §68.1: $\operatorname{Hom}(V, W)$ Is a Representation
> The rule of Definition [[§68 Actions on Matrix Spaces#^def-68-1|§68.1]] is an action of $G$ on $\operatorname{Hom}(V, W)$ by linear maps. So $\operatorname{Hom}(V, W)$ is a representation of $G$.
>
> *Source: WS 16.1*

^prop-68-1

> [!proof]+ Proof
> *(Filled in.)* This is Proposition [[§66 Invariant Vectors#^prop-66-9|§66.9]](1), with $V$, $W$ in place of $W$, $W'$: there the action is written $(g \cdot A)(w) = g\,A(g^{-1}w)$, which is $\big(\rho_W(g) \circ A \circ \rho_V(g^{-1})\big)(w)$. In the present notation the check of the action axioms reads as follows. Since $\rho_V(e) = \mathrm{id}_V$ and $\rho_W(e) = \mathrm{id}_W$, $e \ast \alpha = \alpha$. Since $\rho_V$ and $\rho_W$ are homomorphisms (Proposition [[§61 Representations and Subrepresentations#^prop-61-1|§61.1]]),
>
> $$
> g \ast (h \ast \alpha) = \rho_W(g)\,\rho_W(h) \circ \alpha \circ \rho_V(h^{-1})\,\rho_V(g^{-1}) = \rho_W(gh) \circ \alpha \circ \rho_V\big((gh)^{-1}\big) = (gh) \ast \alpha.
> $$
>
> Each map $\alpha \mapsto g \ast \alpha$ is linear, because composition with a fixed linear map on either side is linear in $\alpha$.

^pf-68-1

*Uses:* [[§66 Invariant Vectors#^prop-66-9|§66.9]], [[§61 Representations and Subrepresentations#^prop-61-1|§61.1]]

> [!definition] Definition §68.2: $\operatorname{Hom}_G(V, W)$
> Let $V$ and $W$ be representations of $G$. The set of homomorphisms of $G$-representations $V \to W$ (Definition [[§61 Representations and Subrepresentations#^def-61-4|§61.4]]), that is, of linear maps $\alpha: V \to W$ with $\alpha \circ \rho_V(g) = \rho_W(g) \circ \alpha$ for all $g \in G$, is written $\operatorname{Hom}_G(V, W)$.
>
> *Source: WS 16*

^def-68-2

By Proposition [[§66 Invariant Vectors#^prop-66-9|§66.9]](2), $\operatorname{Hom}_G(V, W)$ is the space of invariant vectors $\operatorname{Hom}(V, W)^G$ of the representation of Definition [[§68 Actions on Matrix Spaces#^def-68-1|§68.1]]. In particular it is a subspace of $\operatorname{Hom}(V, W)$ (Lemma [[§66 Invariant Vectors#^lem-66-5|§66.5]]).

> [!theorem] Lemma §68.2: The Trace of $\alpha \mapsto S \circ \alpha \circ R$
> Let $V$ and $W$ be finite-dimensional vector spaces over $k$, and let $R: V \to V$ and $S: W \to W$ be linear. The map
>
> $$
> T: \operatorname{Hom}(V, W) \to \operatorname{Hom}(V, W), \qquad T(\alpha) = S \circ \alpha \circ R,
> $$
>
> is linear, and $\operatorname{Tr}(T) = \operatorname{Tr}(S)\operatorname{Tr}(R)$.
>
> *Source: not from class; the computation behind WS 16.2*

^lem-68-2

> [!proof]+ Proof
> *Idea:* In the basis of matrix units $E_{ij}$, the coefficient of $E_{ij}$ in $S E_{ij} R$ is $S_{ii}R_{jj}$, and the sum of these over all $i, j$ factors.
>
> *(Filled in, following the worksheet's hint to name the matrices.)* $T$ is linear, since composition with fixed linear maps is linear in $\alpha$. Choose a basis $v_1, \ldots, v_n$ of $V$ and a basis $w_1, \ldots, w_m$ of $W$. Sending a linear map to its matrix in these bases identifies $\operatorname{Hom}(V, W)$ with the space of $m \times n$ matrices, and composition of maps becomes the product of matrices (Axler, Ch. 3). Write $R = (R_{jl})$, an $n \times n$ matrix, and $S = (S_{ki})$, an $m \times m$ matrix. Then $T$ becomes $X \mapsto SXR$ on $m \times n$ matrices.
>
> A basis of the $m \times n$ matrices is given by the matrix units $E_{ij}$, $1 \leq i \leq m$, $1 \leq j \leq n$, where $E_{ij}$ has the entry $1$ in position $(i, j)$ and $0$ elsewhere; every matrix $X$ is $\sum_{i,j} X_{ij}E_{ij}$, so the coefficient of $E_{ij}$ in $X$ is the entry $X_{ij}$. The $(k, l)$ entry of $SE_{ij}R$ is
>
> $$
> (SE_{ij}R)_{kl} = \sum_{a, b} S_{ka}\,(E_{ij})_{ab}\,R_{bl} = S_{ki}R_{jl},
> $$
>
> because $(E_{ij})_{ab}$ is $1$ for $(a, b) = (i, j)$ and $0$ otherwise. The diagonal entry of the matrix of $T$ at the basis vector $E_{ij}$ is the coefficient of $E_{ij}$ in $T(E_{ij}) = SE_{ij}R$, that is, its $(i, j)$ entry $S_{ii}R_{jj}$. The trace of $T$ is the sum of these diagonal entries (Definition [[§66 Invariant Vectors#^def-66-2|§66.2]]):
>
> $$
> \operatorname{Tr}(T) = \sum_{i=1}^m \sum_{j=1}^n S_{ii}R_{jj} = \Big(\sum_{i=1}^m S_{ii}\Big)\Big(\sum_{j=1}^n R_{jj}\Big) = \operatorname{Tr}(S)\operatorname{Tr}(R).
> $$

^pf-68-2

*Uses:* [[§66 Invariant Vectors#^def-66-2|Def. §66.2]]

> [!theorem] Proposition §68.3: The Character of $\operatorname{Hom}(V, W)$
> Let $V$ and $W$ be finite-dimensional representations of $G$ over $k$. Then for every $g \in G$
>
> $$
> \chi_{\operatorname{Hom}(V, W)}(g) = \operatorname{Tr}\rho_{\operatorname{Hom}(V, W)}(g) = \big(\operatorname{Tr}\rho_W(g)\big)\big(\operatorname{Tr}\rho_V(g^{-1})\big) = \chi_W(g)\,\chi_V(g^{-1}).
> $$
>
> *Source: WS 16.2, with $V$ and $W$ exchanged (see the transcription note above)*

^prop-68-3

> [!proof]+ Proof
> *(Filled in.)* By Definition [[§68 Actions on Matrix Spaces#^def-68-1|§68.1]], $\rho_{\operatorname{Hom}(V, W)}(g)$ is the map $\alpha \mapsto S \circ \alpha \circ R$ with $S = \rho_W(g)$ and $R = \rho_V(g^{-1})$. By Lemma [[§68 Actions on Matrix Spaces#^lem-68-2|§68.2]] its trace is $\operatorname{Tr}(S)\operatorname{Tr}(R) = \chi_W(g)\,\chi_V(g^{-1})$ (Definition [[§67 Characters of Representations#^def-67-1|§67.1]]).

^pf-68-3

*Uses:* [[§68 Actions on Matrix Spaces#^def-68-1|Def. §68.1]], [[§68 Actions on Matrix Spaces#^lem-68-2|§68.2]], [[§67 Characters of Representations#^def-67-1|Def. §67.1]]

Worksheet 16.2 prints $\operatorname{Tr}\rho_{\operatorname{Hom}(V, W)}(g) = (\operatorname{Tr}\rho_V(g))(\operatorname{Tr}\rho_W(g^{-1}))$, which is the formula for the action as the worksheet prints it. The two versions differ by replacing $g$ with $g^{-1}$, and they have the same sum over $G$. So the theorem holds as printed.

> [!theorem] Theorem §68.4: Dimension of $\operatorname{Hom}_G(V, W)$
> Let $k$ be a field containing $\mathbb{Q}$, let $G$ be a finite group, and let $V$ and $W$ be finite-dimensional representations of $G$ over $k$, with characters $\chi_V$ and $\chi_W$. Then
>
> $$
> \dim \operatorname{Hom}_G(V, W) = \frac{1}{|G|}\sum_{g \in G} \chi_V(g)\,\chi_W(g^{-1}).
> $$
>
> *Source: WS 16, theorem*

^thm-68-4

> [!proof]+ Proof
> *Idea:* $\operatorname{Hom}_G(V, W)$ is the space of invariant vectors of $\operatorname{Hom}(V, W)$, whose dimension is the average of the character of $\operatorname{Hom}(V, W)$.
>
> *(Filled in, along the worksheet's outline.)* $\operatorname{Hom}(V, W)$ is a finite-dimensional representation of $G$ (Proposition [[§68 Actions on Matrix Spaces#^prop-68-1|§68.1]]; its dimension is $\dim V \cdot \dim W$, the number of matrix units in the proof of Lemma [[§68 Actions on Matrix Spaces#^lem-68-2|§68.2]]), and $\operatorname{Hom}_G(V, W) = \operatorname{Hom}(V, W)^G$ (Proposition [[§66 Invariant Vectors#^prop-66-9|§66.9]](2)). By Dimension of the Invariants (Theorem [[§66 Invariant Vectors#^thm-66-10|§66.10]]) and Proposition [[§68 Actions on Matrix Spaces#^prop-68-3|§68.3]],
>
> $$
> \dim \operatorname{Hom}_G(V, W) = \frac{1}{|G|}\sum_{g \in G} \chi_{\operatorname{Hom}(V, W)}(g) = \frac{1}{|G|}\sum_{g \in G} \chi_W(g)\,\chi_V(g^{-1}).
> $$
>
> Inversion $g \mapsto g^{-1}$ is a bijection of $G$, so the sum does not change when $g$ is replaced by $g^{-1}$ in every term:
>
> $$
> \frac{1}{|G|}\sum_{g \in G} \chi_W(g)\,\chi_V(g^{-1}) = \frac{1}{|G|}\sum_{g \in G} \chi_W(g^{-1})\,\chi_V(g).
> $$

^pf-68-4

*Uses:* [[§68 Actions on Matrix Spaces#^prop-68-1|§68.1]], [[§68 Actions on Matrix Spaces#^lem-68-2|§68.2]], [[§66 Invariant Vectors#^prop-66-9|§66.9]], [[§66 Invariant Vectors#^thm-66-10|§66.10]], [[§68 Actions on Matrix Spaces#^prop-68-3|§68.3]]

> [!theorem] Corollary §68.5: Homomorphisms in Both Directions
> In the setting of Theorem [[§68 Actions on Matrix Spaces#^thm-68-4|§68.4]], $\dim \operatorname{Hom}_G(V, W) = \dim \operatorname{Hom}_G(W, V)$.
>
> *Source: not from class*

^cor-68-5

> [!proof]+ Proof
> *(Not from class.)* By Theorem [[§68 Actions on Matrix Spaces#^thm-68-4|§68.4]] for the pair $(W, V)$, $\dim \operatorname{Hom}_G(W, V) = \frac{1}{|G|}\sum_{g} \chi_W(g)\,\chi_V(g^{-1})$. The last display of the proof of Theorem [[§68 Actions on Matrix Spaces#^thm-68-4|§68.4]] shows that this equals $\frac{1}{|G|}\sum_{g} \chi_V(g)\,\chi_W(g^{-1}) = \dim \operatorname{Hom}_G(V, W)$.

^pf-68-5

*Uses:* [[§68 Actions on Matrix Spaces#^thm-68-4|§68.4]]

## Characters at $g^{-1}$ over $\mathbb{R}$ and $\mathbb{C}$

The formula of Theorem [[§68 Actions on Matrix Spaces#^thm-68-4|§68.4]] simplifies when the field is $\mathbb{R}$ or $\mathbb{C}$.

> [!theorem] Proposition §68.6: Characters of Real Representations at Inverses
> Let $G$ be a finite group and $V$ a finite-dimensional representation of $G$ over $\mathbb{R}$. Choose a basis of $V$ in which $G$ acts by orthogonal matrices (Corollary [[§63 Invariant Inner Products and Maschke over ℝ#^cor-63-7|§63.7]]). In this basis, for every $g \in G$,
>
> $$
> \rho_V(g^{-1}) = \rho_V(g)^{-1} = \rho_V(g)^T.
> $$
>
> Consequently $\chi_V(g^{-1}) = \chi_V(g)$ for every $g \in G$.
>
> *Source: WS 16.3*

^prop-68-6

> [!proof]+ Proof
> *(Filled in.)* *Why such a basis exists.* This is Finite Groups Act by Orthogonal Matrices (Corollary [[§63 Invariant Inner Products and Maschke over ℝ#^cor-63-7|§63.7]]): $G$ preserves the averaged inner product (Proposition [[§63 Invariant Inner Products and Maschke over ℝ#^prop-63-5|§63.5]]), and in a basis that is orthonormal for it every $\rho_V(g)$ is an orthogonal matrix.
>
> *The two equalities.* Since $\rho_V$ is a homomorphism (Proposition [[§61 Representations and Subrepresentations#^prop-61-1|§61.1]]), $\rho_V(g^{-1})\rho_V(g) = \rho_V(e) = I$, so $\rho_V(g^{-1}) = \rho_V(g)^{-1}$. Write $M = \rho_V(g)$. It is orthogonal, $M^TM = I$, so $M^{-1} = M^T$.
>
> *The characters.* A matrix and its transpose have the same diagonal entries, so $\operatorname{Tr}(M^T) = \operatorname{Tr}(M)$ (Definition [[§66 Invariant Vectors#^def-66-1|§66.1]]). The trace of a linear map does not depend on the basis (Corollary [[§66 Invariant Vectors#^cor-66-2|§66.2]]), so it may be computed in this basis:
>
> $$
> \chi_V(g^{-1}) = \operatorname{Tr}\rho_V(g^{-1}) = \operatorname{Tr}(M^T) = \operatorname{Tr}(M) = \chi_V(g).
> $$

^pf-68-6

*Uses:* [[§63 Invariant Inner Products and Maschke over ℝ#^cor-63-7|§63.7]], [[§63 Invariant Inner Products and Maschke over ℝ#^prop-63-5|§63.5]], [[§61 Representations and Subrepresentations#^prop-61-1|§61.1]], [[§66 Invariant Vectors#^def-66-1|Def. §66.1]], [[§66 Invariant Vectors#^cor-66-2|§66.2]]

> [!theorem] Proposition §68.7: Complex Matrices of Finite Order
> Let $A$ be an $n \times n$ complex matrix with $A^m = I$ for some positive integer $m$.
>
> 1. $A$ is diagonalizable, and every eigenvalue $\lambda$ of $A$ satisfies $\lambda^m = 1$; in particular $|\lambda| = 1$.
> 2. $\operatorname{Tr}(A^{-1}) = \overline{\operatorname{Tr}(A)}$.
>
> *Source: WS 16.4*

^prop-68-7

> [!proof]+ Proof
> *Idea:* $A$ generates a representation of the finite group $\mathbb{Z}/m\mathbb{Z}$ on $\mathbb{C}^n$; Maschke's theorem splits off one eigenvector at a time. On the unit circle, $\lambda^{-1} = \bar\lambda$.
>
> *(Filled in; the worksheet's hint for (2) is to use the eigenvalues.)* $A$ is invertible, with inverse $A^{m-1}$.
>
> **(1) Eigenvalues.** Let $Av = \lambda v$ with $v \neq 0$. Then $v = A^mv = \lambda^m v$, so $\lambda^m = 1$. Taking absolute values, $|\lambda|^m = 1$, and $|\lambda|$ is a nonnegative real number, so $|\lambda| = 1$.
>
> **(1) Diagonalizable.** We show by induction on $\dim U$ that every subspace $U \subseteq \mathbb{C}^n$ with $AU \subseteq U$ has a basis of eigenvectors of $A$; the case $U = \mathbb{C}^n$ is the claim. If $U = \{0\}$ there is nothing to show. Let $U \neq \{0\}$. The rule $j \mapsto (A|_U)^j$ is well defined on $j \bmod m$, because $A^m = I$, and it is a homomorphism $\mathbb{Z}/m\mathbb{Z} \to GL(U)$. So $U$ is a representation of the finite group $\mathbb{Z}/m\mathbb{Z}$ over $\mathbb{C}$ (Proposition [[§61 Representations and Subrepresentations#^prop-61-1|§61.1]]), and its subrepresentations are the subspaces $U' \subseteq U$ with $AU' \subseteq U'$ (such a subspace is preserved by every power of $A$). A linear map from a nonzero finite-dimensional complex vector space to itself has an eigenvector (Axler, Ch. 5); let $v \in U$ be an eigenvector of $A|_U$. The line $\mathbb{C}v$ is a subrepresentation. Since $|\mathbb{Z}/m\mathbb{Z}| = m \neq 0$ in $\mathbb{C}$, Maschke's theorem (Theorem [[§62 Direct Sums and Maschke's Theorem#^thm-62-10|§62.10]]) gives a subrepresentation $U'$ with $U = \mathbb{C}v \oplus U'$. Then $AU' \subseteq U'$ and $\dim U' = \dim U - 1$, so by induction $U'$ has a basis of eigenvectors of $A$. Together with $v$ it is a basis of $U$ (Bases of a Direct Sum, Proposition [[§62 Direct Sums and Maschke's Theorem#^prop-62-1|§62.1]]).
>
> **(2)** By (1) there is an invertible matrix $P$ with $A = PDP^{-1}$, $D = \operatorname{diag}(\lambda_1, \ldots, \lambda_n)$, where the $\lambda_i$ are the eigenvalues of $A$ with multiplicity. Then $A^{-1} = PD^{-1}P^{-1}$ with $D^{-1} = \operatorname{diag}(\lambda_1^{-1}, \ldots, \lambda_n^{-1})$. Since $|\lambda_i| = 1$, $\lambda_i\overline{\lambda_i} = |\lambda_i|^2 = 1$, so $\lambda_i^{-1} = \overline{\lambda_i}$. By The Trace of a Diagonalizable Matrix (Proposition [[§66 Invariant Vectors#^prop-66-3|§66.3]], PS 8.5(3)), applied to $A^{-1}$ and to $A$,
>
> $$
> \operatorname{Tr}(A^{-1}) = \sum_{i=1}^n \lambda_i^{-1} = \sum_{i=1}^n \overline{\lambda_i} = \overline{\sum_{i=1}^n \lambda_i} = \overline{\operatorname{Tr}(A)}.
> $$

^pf-68-7

*Uses:* [[§61 Representations and Subrepresentations#^prop-61-1|§61.1]], [[§62 Direct Sums and Maschke's Theorem#^thm-62-10|§62.10]], [[§62 Direct Sums and Maschke's Theorem#^prop-62-1|§62.1]], [[§66 Invariant Vectors#^prop-66-3|§66.3]]

> [!remark]- Connections
> - Linear Algebra: an operator on a nonzero finite-dimensional complex vector space has an eigenvalue (Axler, Ch. 5). A second route to (1): the [[§15 The Minimal Polynomial#^ladr-5-24|minimal polynomial]] of $A$ divides $x^m - 1$, which has $m$ distinct roots, and an operator whose minimal polynomial has distinct roots is diagonalizable.

![[m493-66-1.svg]]

*(Not from lecture; figure added.)* Proposition [[§68 Actions on Matrix Spaces#^prop-68-7|§68.7]] for $A = \operatorname{diag}(\lambda_1, \lambda_2)$ with $\lambda_1 = e^{2\pi i/6}$ and $\lambda_2 = e^{2\pi i \cdot 2/6}$, so that $A^6 = I$. The eigenvalues of a matrix with $A^6 = I$ are among the six marked points of the unit circle. Inverting a point of the unit circle reflects it in the real axis (dashed), which is complex conjugation. So the eigenvalues of $A^{-1}$ (red) are the conjugates of those of $A$ (blue), and the two traces are conjugate: $i\sqrt{3}$ and $-i\sqrt{3}$.

> [!theorem] Corollary §68.8: Characters of Complex Representations at Inverses
> Let $G$ be a finite group and $V$ a finite-dimensional complex representation of $G$. Then for every $g \in G$
>
> $$
> \chi_V(g^{-1}) = \overline{\chi_V(g)}.
> $$
>
> *Source: WS 16.5*

^cor-68-8

> [!proof]+ Proof
> *(Filled in.)* Choose a basis of $V$ and let $A$ be the matrix of $\rho_V(g)$ in it. Let $m = |G|$. Then $g^m = e$ (Corollary [[§29 The Index and Lagrange's Theorem#^cor-29-3|§29.3]]), so $A^m$ is the matrix of $\rho_V(g)^m = \rho_V(g^m) = \rho_V(e)$, the identity matrix. The matrix of $\rho_V(g^{-1}) = \rho_V(g)^{-1}$ is $A^{-1}$. By Proposition [[§68 Actions on Matrix Spaces#^prop-68-7|§68.7]](2),
>
> $$
> \chi_V(g^{-1}) = \operatorname{Tr}(A^{-1}) = \overline{\operatorname{Tr}(A)} = \overline{\chi_V(g)}.
> $$

^pf-68-8

*Uses:* [[§29 The Index and Lagrange's Theorem#^cor-29-3|§29.3]], [[§68 Actions on Matrix Spaces#^prop-68-7|§68.7]]

> [!proof]+ Second proof (unitary matrices; outline)
> *(The route Worksheet 16 mentions for readers who know sesquilinear forms. It rests on the statement in the remark *Why Not Bilinear, and Unitary Matrices* in [[§64 Sesquilinear and Hermitian Forms|§64]], whose averaging argument is not written out in these notes.)* A finite group acting on a finite-dimensional complex vector space preserves a positive definite Hermitian form, and in a basis that is orthonormal for it (Proposition [[§64 Sesquilinear and Hermitian Forms#^prop-64-4|§64.4]]) every $M = \rho_V(g)$ is unitary, $M^\dagger M = I$ (Definition [[§64 Sesquilinear and Hermitian Forms#^def-64-4|§64.4]]). As in the proof of Proposition [[§68 Actions on Matrix Spaces#^prop-68-6|§68.6]], $\rho_V(g^{-1}) = M^{-1} = M^\dagger$. The diagonal entries of $M^\dagger = \bar M^T$ are the conjugates of those of $M$, so $\chi_V(g^{-1}) = \operatorname{Tr}(M^\dagger) = \overline{\operatorname{Tr}(M)} = \overline{\chi_V(g)}$.

^pf-68-8-2

*Uses:* [[§64 Sesquilinear and Hermitian Forms#^prop-64-4|§64.4]], [[§64 Sesquilinear and Hermitian Forms#^def-64-4|Def. §64.4]], [[§68 Actions on Matrix Spaces#^prop-68-6|§68.6]]

> [!theorem] Corollary §68.9: Dimension of $\operatorname{Hom}_G(V, W)$ over $\mathbb{R}$ and $\mathbb{C}$
> Let $G$ be a finite group and let $V$, $W$ be finite-dimensional representations of $G$ over $k$.
>
> 1. If $k = \mathbb{R}$, then $\dim \operatorname{Hom}_G(V, W) = \dfrac{1}{|G|}\displaystyle\sum_{g \in G} \chi_V(g)\,\chi_W(g)$.
> 2. If $k = \mathbb{C}$, then $\dim \operatorname{Hom}_G(V, W) = \dfrac{1}{|G|}\displaystyle\sum_{g \in G} \chi_V(g)\,\overline{\chi_W(g)}$.
>
> *Source: WS 16: the simplification announced before WS 16.3; the two formulas are not printed on the worksheet*

^cor-68-9

> [!proof]+ Proof
> *(Filled in.)* Both fields contain $\mathbb{Q}$, so Theorem [[§68 Actions on Matrix Spaces#^thm-68-4|§68.4]] applies. Substitute $\chi_W(g^{-1}) = \chi_W(g)$ over $\mathbb{R}$ (Proposition [[§68 Actions on Matrix Spaces#^prop-68-6|§68.6]]) and $\chi_W(g^{-1}) = \overline{\chi_W(g)}$ over $\mathbb{C}$ (Corollary [[§68 Actions on Matrix Spaces#^cor-68-8|§68.8]]).

^pf-68-9

*Uses:* [[§68 Actions on Matrix Spaces#^thm-68-4|§68.4]], [[§68 Actions on Matrix Spaces#^prop-68-6|§68.6]], [[§68 Actions on Matrix Spaces#^cor-68-8|§68.8]]

> [!example] Example §68.1: Homomorphisms between Representations of $S_3$
> *(Not from class.)* Over $\mathbb{R}$, take the characters of $S_3$ from Example [[§67 Characters of Representations#^ex-67-1|§67.1]], as values on the classes of $e$, $(1\,2)$, $(1\,2\,3)$, of sizes $1$, $3$, $2$: trivial $(1, 1, 1)$, sign $(1, -1, 1)$, $U = (1,1,1)^\perp$ with $(2, 0, -1)$, and $\mathbb{R}^3$ with $(3, 1, 0)$. A sum over $G$ of a function that is constant on [[§33 Conjugacy Classes#^def-33-1|conjugacy classes]] is the sum over the classes of (class size) $\times$ (value). By Corollary [[§68 Actions on Matrix Spaces#^cor-68-9|§68.9]](1):
>
> 1. $\dim \operatorname{Hom}_G(U, U) = \frac16(1 \cdot 4 + 3 \cdot 0 + 2 \cdot 1) = 1$. The homomorphisms $U \to U$ are the multiples of the identity.
> 2. $\dim \operatorname{Hom}_G(\mathrm{triv}, U) = \frac16(1 \cdot 2 + 3 \cdot 0 + 2 \cdot (-1)) = 0$, and $\dim \operatorname{Hom}_G(\mathrm{triv}, \mathrm{sign}) = \frac16(1 - 3 + 2) = 0$: the only homomorphism is $0$.
> 3. $\dim \operatorname{Hom}_G(\mathrm{sign}, \mathrm{sign}) = \frac16(1 + 3 + 2) = 1$.
> 4. $\dim \operatorname{Hom}_G(\mathbb{R}^3, \mathbb{R}^3) = \frac16(1 \cdot 9 + 3 \cdot 1 + 2 \cdot 0) = 2$. Two independent homomorphisms are the identity and the averaging operator $\pi$ of Example [[§66 Invariant Vectors#^ex-66-4|§66.4]], whose matrix is $\frac13$ times the all-ones matrix; $\pi$ commutes with every $\rho(g)$ (the proof of Corollary [[§66 Invariant Vectors#^cor-66-8|§66.8]]) and is not a multiple of the identity.

^ex-68-1
