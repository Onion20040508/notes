---
type: section
subject: "[[Group Theory]]"
chapter: 11
section: 64
tags: [group-theory, math493]
---
← [[§63 Simple Representations]] · ↑ [[· 11 Representations]] · [[§65 Characters of Representations]] →

*Source: Lecture and Worksheet 15 (Mon Nov 9); Problem Set 8, Problem 8.5 (submitted Thu Nov 5) for the trace. Reference: Axler, *Linear Algebra Done Right* (projections, trace).*

By [[§63 Simple Representations|§63]], representations of a finite group over $\mathbb{R}$ break into simple pieces (Corollary [[§63 Simple Representations#^cor-63-2|§63.2]]; over any field in which $|G| \neq 0$, Corollary [[§63 Simple Representations#^cor-63-3|§63.3]]), and the remaining question is what the simple representations are. The main tool is the character, the function $g \mapsto \operatorname{Tr} \rho_V(g)$ ([[§65 Characters of Representations|§65]]). This section starts with a first use of it: the dimension of the space of invariant vectors is the average of the traces.

A representation always contains the vectors that no element of $G$ moves. For a finite group, averaging over $G$ is an idempotent onto these vectors. So they split off as a direct summand, and their number, the dimension of that summand, is the average of the traces of the matrices $\rho_V(g)$. Worksheet 15 opens with the linear algebra: idempotents (Definition [[§60 Direct Sums and Maschke's Theorem#^def-60-2|§60.2]]) and WS 15.1, that an idempotent splits $V$ as kernel $\oplus$ image (Proposition [[§60 Direct Sums and Maschke's Theorem#^prop-60-6|§60.6]]). Both are in [[§60 Direct Sums and Maschke's Theorem|§60]], with the proof from Problem Set 9 and the lecture's remark on what needs a basis. This section starts with the trace of a matrix (Problem Set 8, Problem 8.5) and the trace of an idempotent.

> [!definition] Definition §64.1: Trace of a Matrix
> Let $M$ be a square $n \times n$ matrix with entries in a field $k$. The **trace** of $M$ is the sum of its diagonal entries,
>
> $$
> \operatorname{Tr}(M) = \sum_{i=1}^n M_{ii}.
> $$
>
> *Source: PS 8.5*

^def-64-1

> [!remark]- Connections
> - Linear Algebra: [[§33 Trace꞉ A Connection Between Matrices and Operators#^ladr-8-47|LADR 8.47]].

> [!theorem] Proposition §64.1: The Trace of a Product in Either Order
> Let $A$ be an $m \times n$ matrix and let $B$ be an $n \times m$ matrix. Then $\operatorname{Tr}(AB) = \operatorname{Tr}(BA)$.
>
> *Source: PS 8.5(1)*

^prop-64-1

> [!proof]+ Proof
> *Idea:* Both traces are the sum of the products $A_{ik}B_{ki}$ over all pairs $(i, k)$.
>
> *(Problem Set 8, Problem 8.5(1), as submitted.)* The product $AB$ is an $m \times m$ matrix with $(AB)_{ii} = \sum_{k=1}^n A_{ik}B_{ki}$, and $BA$ is an $n \times n$ matrix with $(BA)_{kk} = \sum_{i=1}^m B_{ki}A_{ik}$. Exchanging the two finite sums and using $A_{ik}B_{ki} = B_{ki}A_{ik}$,
>
> $$
> \operatorname{Tr}(AB) = \sum_{i=1}^m (AB)_{ii} = \sum_{i=1}^m \sum_{k=1}^n A_{ik}B_{ki} = \sum_{k=1}^n \sum_{i=1}^m B_{ki}A_{ik} = \sum_{k=1}^n (BA)_{kk} = \operatorname{Tr}(BA).
> $$

^pf-64-1

> [!remark]- Connections
> - Linear Algebra: [[§33 Trace꞉ A Connection Between Matrices and Operators#^ladr-8-49|LADR 8.49]].

> [!example] Example §64.1: Products of Different Sizes with the Same Trace
> *(Not from class.)* Take $m = 1$ and $n = 2$, with
>
> $$
> A = \begin{pmatrix} 1 & 2 \end{pmatrix}, \qquad B = \begin{pmatrix} 3 \\ 4 \end{pmatrix}, \qquad AB = \begin{pmatrix} 11 \end{pmatrix}, \qquad BA = \begin{pmatrix} 3 & 6 \\ 4 & 8 \end{pmatrix}.
> $$
>
> The matrices $AB$ and $BA$ have different sizes, but $\operatorname{Tr}(AB) = 11 = 3 + 8 = \operatorname{Tr}(BA)$, as Proposition [[§64 Invariant Vectors#^prop-64-1|§64.1]] says.

^ex-64-1

> [!theorem] Corollary §64.2: Conjugate Matrices Have the Same Trace
> Let $M$ be an $n \times n$ matrix and let $S$ be an invertible $n \times n$ matrix. Then $\operatorname{Tr}(SMS^{-1}) = \operatorname{Tr}(M)$.
>
> *Source: PS 8.5(2)*

^cor-64-2

> [!proof]+ Proof
> *(Problem Set 8, Problem 8.5(2), as submitted.)* Applying (1) (Proposition [[§64 Invariant Vectors#^prop-64-1|§64.1]]) with the $n \times n$ matrices $A = S^{-1}$ and $B = SM$,
>
> $$
> \operatorname{Tr}(M) = \operatorname{Tr}(S^{-1}SM) = \operatorname{Tr}\big(S^{-1}(SM)\big) = \operatorname{Tr}\big((SM)S^{-1}\big) = \operatorname{Tr}(SMS^{-1}).
> $$

^pf-64-2

*Uses:* [[§64 Invariant Vectors#^prop-64-1|§64.1]]

> [!remark]- Connections
> - Linear Algebra: [[§33 Trace꞉ A Connection Between Matrices and Operators#^ladr-8-50|LADR 8.50]], where it is used to show that the trace of an operator does not depend on the basis.

> [!theorem] Proposition §64.3: The Trace of a Diagonalizable Matrix
> Let $M$ be a diagonalizable $n \times n$ matrix with eigenvalues $\lambda_1, \lambda_2, \ldots, \lambda_n$, listed with multiplicity. Then
>
> $$
> \operatorname{Tr}(M) = \lambda_1 + \lambda_2 + \cdots + \lambda_n.
> $$
>
> *Source: PS 8.5(3)*

^prop-64-3

> [!proof]+ Proof
> *Idea:* $M$ is conjugate to the diagonal matrix of its eigenvalues, and conjugation does not change the trace.
>
> *(Problem Set 8, Problem 8.5(3), as submitted.)* Since $M$ is diagonalizable, there is an invertible $n \times n$ matrix $P$ with
>
> $$
> M = PDP^{-1}, \qquad D = \operatorname{diag}(\lambda_1, \lambda_2, \dots, \lambda_n),
> $$
>
> where the diagonal entries of $D$ are the eigenvalues of $M$, listed with multiplicity. By (2) (Corollary [[§64 Invariant Vectors#^cor-64-2|§64.2]]), applied with $S = P$ and the matrix $D$ in place of $M$,
>
> $$
> \operatorname{Tr}(M) = \operatorname{Tr}(PDP^{-1}) = \operatorname{Tr}(D) = \sum_{i=1}^n D_{ii} = \lambda_1 + \lambda_2 + \cdots + \lambda_n.
> $$

^pf-64-3

*Uses:* [[§64 Invariant Vectors#^cor-64-2|§64.2]]

> [!remark]- Connections
> - Linear Algebra: [[§33 Trace꞉ A Connection Between Matrices and Operators#^ladr-8-52|LADR 8.52]] proves the same formula over $\mathbb{C}$ without assuming that the matrix is diagonalizable.

> [!definition] Definition §64.2: Trace of a Linear Map
> Let $V$ be a finite-dimensional vector space over $k$ and $T: V \to V$ linear. The **trace** $\operatorname{Tr}(T) \in k$ is the trace (Definition [[§64 Invariant Vectors#^def-64-1|§64.1]]) of the matrix of $T$ in a basis of $V$.
>
> *Source: not from class; used in WS 15*

^def-64-2

The trace does not depend on the basis. The matrices $M$, $M'$ of $T$ in two bases are conjugate, $M' = SMS^{-1}$, and $\operatorname{Tr}(SMS^{-1}) = \operatorname{Tr}(M)$ by Corollary [[§64 Invariant Vectors#^cor-64-2|§64.2]] (PS 8.5(2)). Compare the remark *Checking Answers in Different Bases* in [[§59 Representations and Subrepresentations|§59]]. The trace is linear: $\operatorname{Tr}(aT + bT') = a\operatorname{Tr}(T) + b\operatorname{Tr}(T')$, since matrices of linear maps in a fixed basis add and scale entrywise.

> [!remark]- Connections
> - Linear Algebra: [[§33 Trace꞉ A Connection Between Matrices and Operators#^ladr-8-47|LADR 8.47]] (trace of a matrix), [[§33 Trace꞉ A Connection Between Matrices and Operators#^ladr-8-51|LADR 8.51]] (trace of an operator); independence of the basis, [[§33 Trace꞉ A Connection Between Matrices and Operators#^ladr-8-50|LADR 8.50]], from [[§33 Trace꞉ A Connection Between Matrices and Operators#^ladr-8-49|LADR 8.49]], $\operatorname{Tr}(AB) = \operatorname{Tr}(BA)$.

> [!theorem] Proposition §64.4: The Trace of an Idempotent
> Let $V$ be a finite-dimensional vector space over $k$ and $\pi: V \to V$ idempotent (Definition [[§60 Direct Sums and Maschke's Theorem#^def-60-2|§60.2]]). Then
>
> $$
> \operatorname{Tr}(\pi) = (\dim \operatorname{Im}\pi) \cdot 1_k.
> $$
>
> In particular, if $\mathbb{Q} \subseteq k$, then $\operatorname{Tr}(\pi) = \dim \operatorname{Im}\pi$.
>
> *Source: WS 15.2; worksheet session 11/9*

^prop-64-4

> [!proof]+ Proof
> *Idea:* In a basis adapted to $V = \operatorname{Ker}\pi \oplus \operatorname{Im}\pi$, the matrix of $\pi$ is diagonal with entries $1, \ldots, 1, 0, \ldots, 0$.
>
> *(Worksheet session 11/9; uses WS 15.1.)* Every $y \in \operatorname{Im}(\pi)$ is $y = \pi(u)$, so $\pi(y) = \pi^2(u) = \pi(u) = y$: $\pi$ is the identity on its image (Lemma [[§60 Direct Sums and Maschke's Theorem#^lem-60-5|§60.5]]). Choose a basis $y_1, \ldots, y_r$ of $\operatorname{Im}(\pi)$ and $x_1, \ldots, x_s$ of $\operatorname{Ker}(\pi)$. By WS 15.1 (An Idempotent Splits the Space, Proposition [[§60 Direct Sums and Maschke's Theorem#^prop-60-6|§60.6]]) and Bases of a Direct Sum (WS 14.1, Proposition [[§60 Direct Sums and Maschke's Theorem#^prop-60-1|§60.1]]), together they form a basis of $V$. Since $\pi(y_i) = y_i$ and $\pi(x_j) = 0$, in this basis the matrix of $\pi$ is $\operatorname{diag}(1, \ldots, 1, 0, \ldots, 0)$ with $r$ ones, so
>
> $$
> \operatorname{Tr}(\pi) = \underbrace{1_k + \cdots + 1_k}_{r} = r \cdot 1_k, \qquad r = \dim \operatorname{Im}(\pi).
> $$
>
> The trace does not depend on the basis (the paragraph after Definition [[§64 Invariant Vectors#^def-64-2|§64.2]]). *(Not from class.)* If $\mathbb{Q} \subseteq k$, the element $r \cdot 1_k$ is the rational number $r$.

^pf-64-4

*Uses:* [[§60 Direct Sums and Maschke's Theorem#^lem-60-5|§60.5]], [[§60 Direct Sums and Maschke's Theorem#^prop-60-6|§60.6]], [[§60 Direct Sums and Maschke's Theorem#^prop-60-1|§60.1]], [[§64 Invariant Vectors#^def-64-2|Def. §64.2]]

> [!example] Example §64.2: The Trace Sees the Dimension Only Modulo $p$
> *(Not from class.)* Over $\mathbb{F}_2$, the identity map of $\mathbb{F}_2^2$ is idempotent with image of dimension $2$, but its trace is $1 + 1 = 0$. In general, over a field in which $p = 0$, Proposition [[§64 Invariant Vectors#^prop-64-4|§64.4]] determines $\dim \operatorname{Im}\pi$ only modulo $p$. This is why Worksheet 15 assumes $\mathbb{Q} \subseteq k$: then $r \cdot 1_k = r$, and the trace recovers the dimension (the remark *Why the Field Should Contain $\mathbb{Q}$* below).

^ex-64-2

> [!definition] Definition §64.3: Invariant Vectors
> Let $G$ be a group and $V$ a representation of $G$. The **invariant vectors** of $V$ are
>
> $$
> V^G = \{v \in V : g(v) = v \text{ for all } g \in G\}.
> $$
>
> *Source: WS 15; lecture 11/9*

^def-64-3

> [!theorem] Lemma §64.5: $V^G$ Is a Subrepresentation
> $V^G$ is a subrepresentation of $V$, and every $g \in G$ acts on it as the identity.
>
> *Source: lecture 11/9 (stated); proof not from class*

^lem-64-5

> [!proof]+ Proof
> *(Not from class; filled in.)* $0 \in V^G$, since $g0 = 0$ by linearity. If $v, w \in V^G$ and $a, b \in k$, then $g(av + bw) = a\,gv + b\,gw = av + bw$ for every $g$, so $V^G$ is a subspace. If $v \in V^G$, then $gv = v \in V^G$, so $V^G$ is $G$-stable, and $g$ acts on it as the identity.

^pf-64-5

> [!definition] Definition §64.4: The Averaging Operator
> Let $G$ be a finite group, $k$ a field in which $|G| \neq 0$, and $V$ a representation of $G$ over $k$. The **averaging operator** is
>
> $$
> \pi: V \to V, \qquad \pi(v) = \frac{1}{|G|}\sum_{g \in G} g(v).
> $$
>
> *Source: WS 15; lecture 11/9*

^def-64-4

$\pi$ is linear, being an average of linear maps. Worksheet 15 and the lecture assume from here on that $G$ is finite and that the field contains $\mathbb{Q}$, which forces $|G| \neq 0$. The remark *Only $|G|$ Was Inverted* below explains which steps need which hypothesis.

> [!theorem] Proposition §64.6: The Image of the Average Is the Invariants
> In the setting of Definition [[§64 Invariant Vectors#^def-64-4|§64.4]]:
>
> 1. $\pi(v) = v$ for every $v \in V^G$;
> 2. $\operatorname{Im}(\pi) = V^G$.
>
> *Source: WS 15.3; board 11/9*

^prop-64-6

> [!proof]+ Proof
> *Idea:* Applying $h$ to the average re-indexes the sum; on an invariant vector every term of the sum is $v$.
>
> *(Board 11/9.)* *$\operatorname{Im}(\pi) \subseteq V^G$.* Let $v = \pi(u) = \frac{1}{|G|}\sum_g g(u)$, and let $h \in G$. By linearity and the action axiom,
>
> $$
> h(v) = \frac{1}{|G|} \sum_{g \in G} (hg)(u) = \frac{1}{|G|} \sum_{k \in G} k(u) = \pi(u) = v,
> $$
>
> because as $g$ runs over $G$, so does $k = hg$: left multiplication by $h$ is a bijection of $G$, with inverse $k \mapsto h^{-1}k$. This is the averaging trick again, as in WS 14.8 ($G$ Preserves the Averaged Inner Product, Proposition [[§61 Invariant Inner Products and Maschke over ℝ#^prop-61-5|§61.5]]).
>
> *$V^G \subseteq \operatorname{Im}(\pi)$, and (1).* If $v \in V^G$, then every $g(v) = v$, so
>
> $$
> \pi(v) = \frac{1}{|G|}(v + \cdots + v) = \frac{1}{|G|}\,\big(|G| \cdot 1_k\big)\,v = v;
> $$
>
> hence $v = \pi(v) \in \operatorname{Im}(\pi)$.

^pf-64-6

*Uses:* [[§61 Invariant Inner Products and Maschke over ℝ#^prop-61-5|§61.5]]

> [!theorem] Proposition §64.7: The Average Is Idempotent
> In the setting of Definition [[§64 Invariant Vectors#^def-64-4|§64.4]], $\pi^2 = \pi$.
>
> *Source: WS 15.4; board 11/9*

^prop-64-7

> [!proof]+ Proof
> *(Board 11/9.)* Let $v \in V$. Then $\pi(v) \in \operatorname{Im}(\pi) = V^G$ by WS 15.3 (Proposition [[§64 Invariant Vectors#^prop-64-6|§64.6]](2)), and the second half of that proof shows $\pi(w) = w$ for every $w \in V^G$ (part (1)). So $\pi(\pi(v)) = \pi(v)$.

^pf-64-7

*Uses:* [[§64 Invariant Vectors#^prop-64-6|§64.6]]

> [!proof]+ Second proof (double sum)
> *(The lecture mentioned this route as the more computational alternative; written out here.)* Expanding both averages and using $h(g(v)) = (hg)(v)$,
>
> $$
> \pi(\pi(v)) = \frac{1}{|G|}\sum_{h \in G} h\Big(\frac{1}{|G|}\sum_{g \in G} g(v)\Big) = \frac{1}{|G|^2}\sum_{h \in G}\,\sum_{g \in G} (hg)(v).
> $$
>
> For fixed $h$, as $g$ runs over $G$ so does $k = hg$, so the inner sum is $\sum_{k \in G} k(v)$ for every $h$. Hence
>
> $$
> \pi(\pi(v)) = \frac{1}{|G|^2}\,\big(|G| \cdot 1_k\big) \sum_{k \in G} k(v) = \frac{1}{|G|}\sum_{k \in G} k(v) = \pi(v).
> $$

^pf-64-7-2

> [!theorem] Corollary §64.8: Invariants Split Off
> In the setting of Definition [[§64 Invariant Vectors#^def-64-4|§64.4]],
>
> $$
> V = V^G \oplus \operatorname{Ker}(\pi).
> $$
>
> Moreover $\pi$ is a homomorphism of representations, so $\operatorname{Ker}(\pi)$ is a subrepresentation, and this is a decomposition of $V$ into two subrepresentations.
>
> *Source: WS 15.5; board 11/9; the second sentence not from class*

^cor-64-8

> [!proof]+ Proof
> *(Board 11/9.)* $\pi$ is idempotent (WS 15.4, Proposition [[§64 Invariant Vectors#^prop-64-7|§64.7]]), so $V = \operatorname{Ker}(\pi) \oplus \operatorname{Im}(\pi)$ (WS 15.1, Proposition [[§60 Direct Sums and Maschke's Theorem#^prop-60-6|§60.6]]), and $\operatorname{Im}(\pi) = V^G$ (WS 15.3, Proposition [[§64 Invariant Vectors#^prop-64-6|§64.6]](2)).
>
> *$\pi$ is a homomorphism of representations.* *(Not from class; filled in.)* Let $g \in G$ and $v \in V$. Right multiplication $h \mapsto hg$ is a bijection $G \to G$, so
>
> $$
> \pi(gv) = \frac{1}{|G|}\sum_{h \in G} (hg)(v) = \frac{1}{|G|}\sum_{k \in G} k(v) = \pi(v).
> $$
>
> On the other hand $g\pi(v) = \pi(v)$, since $\pi(v) \in V^G$. So $\pi(gv) = g\pi(v)$. Hence $\operatorname{Ker}(\pi)$ is a subrepresentation (Kernels and Images Are Subrepresentations, Proposition [[§59 Representations and Subrepresentations#^prop-59-4|§59.4]](1)), and so is $V^G$ (Lemma [[§64 Invariant Vectors#^lem-64-5|§64.5]]).

^pf-64-8

*Uses:* [[§64 Invariant Vectors#^prop-64-7|§64.7]], [[§60 Direct Sums and Maschke's Theorem#^prop-60-6|§60.6]], [[§64 Invariant Vectors#^prop-64-6|§64.6]], [[§59 Representations and Subrepresentations#^prop-59-4|§59.4]], [[§64 Invariant Vectors#^lem-64-5|§64.5]]

> [!remark] Remark: Only $|G|$ Was Inverted
> So far the only integer divided by is $|G|$, so WS 15.3–15.5 hold whenever $|G| \neq 0$ in the field, exactly Maschke's hypothesis. Since $\operatorname{Ker}(\pi)$ is also a subrepresentation (Corollary [[§64 Invariant Vectors#^cor-64-8|§64.8]]), this is Maschke's theorem for the particular subrepresentation $V^G$, with an explicit complement and no choice of an auxiliary idempotent. The problem set shows how to use the same idea to split off any subrepresentation: the proof of Maschke's theorem (Theorem [[§60 Direct Sums and Maschke's Theorem#^thm-60-10|§60.10]]) averages an arbitrary idempotent onto $U$, and Proposition [[§64 Invariant Vectors#^prop-64-9|§64.9]] below shows that this is the averaging operator of another representation.
>
> *Source: lecture 11/9; the subrepresentation $\operatorname{Ker}\pi$ and the last sentence not from class*

^rem-64-1

> [!theorem] Proposition §64.9: Homomorphisms Are the Invariant Vectors of $\operatorname{Hom}(W, W')$
> Let $W$ and $W'$ be representations of $G$ over $k$, and let $\operatorname{Hom}(W, W')$ be the vector space of linear maps $W \to W'$.
>
> 1. $(g \cdot A)(w) = g\,A(g^{-1}w)$ defines a representation of $G$ on $\operatorname{Hom}(W, W')$.
> 2. $\operatorname{Hom}(W, W')^G$ is the set of homomorphisms of representations $W \to W'$.
> 3. If $G$ is finite and $|G| \neq 0$ in $k$, the averaging operator of $\operatorname{Hom}(W, W')$ sends $P$ to the map $\pi$ of Averaging a Linear Map over $G$ (Lemma [[§60 Direct Sums and Maschke's Theorem#^lem-60-9|§60.9]]).
>
> *Source: not from class*

^prop-64-9

> [!proof]+ Proof
> *(Not from class; filled in.)* **(1)** $g \cdot A$ is linear, as the composition of the linear maps $w \mapsto g^{-1}w$, $A$, and $w' \mapsto gw'$. *Linearity in $A$:* $(g \cdot (aA + bB))(w) = g\big(aA(g^{-1}w) + bB(g^{-1}w)\big) = a\,(g \cdot A)(w) + b\,(g \cdot B)(w)$, since $g$ acts linearly on $W'$. *Action axioms:* $(e \cdot A)(w) = A(w)$, and
>
> $$
> \big(g_1 \cdot (g_2 \cdot A)\big)(w) = g_1\, (g_2 \cdot A)(g_1^{-1}w) = g_1g_2\, A(g_2^{-1}g_1^{-1}w) = (g_1g_2)\, A\big((g_1g_2)^{-1}w\big) = \big((g_1g_2) \cdot A\big)(w).
> $$
>
> **(2)** $g \cdot A = A$ for all $g$ means $g\,A(g^{-1}w) = A(w)$ for all $g \in G$ and $w \in W$. Since $w \mapsto g^{-1}w$ is a bijection of $W$, we may write $w = gu$ with $u \in W$ arbitrary, and the condition becomes $g\,A(u) = A(gu)$ for all $g$ and $u$. This is the definition of a homomorphism of representations (Definition [[§59 Representations and Subrepresentations#^def-59-4|§59.4]]).
>
> **(3)** By Definition [[§64 Invariant Vectors#^def-64-4|§64.4]] for the representation $\operatorname{Hom}(W, W')$, the average of $P$ is the map
>
> $$
> w \mapsto \frac{1}{|G|}\sum_{g \in G} (g \cdot P)(w) = \frac{1}{|G|}\sum_{g \in G} g\,P(g^{-1}w) = \frac{1}{|G|}\sum_{h \in G} h^{-1}P(hw),
> $$
>
> substituting $h = g^{-1}$; inversion is a bijection of $G$. This is $\pi(w)$.

^pf-64-9

*Uses:* [[§59 Representations and Subrepresentations#^def-59-4|Def. §59.4]], [[§64 Invariant Vectors#^def-64-4|Def. §64.4]]

So Lemma [[§60 Direct Sums and Maschke's Theorem#^lem-60-9|§60.9]] is Proposition [[§64 Invariant Vectors#^prop-64-6|§64.6]] for the representation $\operatorname{Hom}(W, W')$. Averaging lands in the invariant vectors, which are the homomorphisms, and it fixes the vectors that are already invariant. In the proof of Maschke's theorem, $\pi$ is the average of the idempotent $P$ in this sense.

> [!theorem] Theorem §64.10: Dimension of the Invariants
> Let $G$ be a finite group, $k$ a field containing $\mathbb{Q}$, and $V$ a finite-dimensional representation of $G$ over $k$. Then
>
> $$
> \dim V^G = \frac{1}{|G|}\sum_{g \in G} \operatorname{Tr}\rho_V(g).
> $$
>
> *Source: WS 15.6; board 11/9*

^thm-64-10

> [!proof]+ Proof
> *Idea:* $\dim V^G$ is the trace of the averaging operator, and the trace is linear.
>
> *(Board 11/9.)* Since $\mathbb{Q} \subseteq k$, $|G| \cdot 1_k$ is the nonzero rational number $|G|$, so $\pi$ is defined. Since $\pi$ is idempotent with image $V^G$ (WS 15.3–15.4, Propositions [[§64 Invariant Vectors#^prop-64-6|§64.6]] and [[§64 Invariant Vectors#^prop-64-7|§64.7]]), WS 15.2 (Proposition [[§64 Invariant Vectors#^prop-64-4|§64.4]], with $\mathbb{Q} \subseteq k$) gives $\dim V^G = \dim \operatorname{Im}(\pi) = \operatorname{Tr}(\pi)$. The trace is linear (adding matrices adds traces, scaling scales them), so
>
> $$
> \operatorname{Tr}(\pi) = \operatorname{Tr}\Big( \frac{1}{|G|} \sum_{g \in G} \rho_V(g) \Big) = \frac{1}{|G|} \sum_{g \in G} \operatorname{Tr} \rho_V(g).
> $$

^pf-64-10

*Uses:* [[§64 Invariant Vectors#^prop-64-6|§64.6]], [[§64 Invariant Vectors#^prop-64-7|§64.7]], [[§64 Invariant Vectors#^prop-64-4|§64.4]]

> [!remark] Remark: Why the Field Should Contain $\mathbb{Q}$
> If the field has characteristic $p$ with $p \nmid |G|$, every step above still works, but the conclusion is weaker than it looks. $\dim V^G$ is an integer, and the formula only says that its image in the field equals the average of the traces computed in the field, so it determines $\dim V^G$ modulo $p$ (Example [[§64 Invariant Vectors#^ex-64-2|§64.2]]). For a group of order $60$ over a field in which $7 = 0$, dividing by $60$ is fine, but one learns $\dim V^G$ only mod $7$. When the field contains $\mathbb{Q}$, distinct integers stay distinct, and the formula computes $\dim V^G$ exactly.
>
> *Source: lecture 11/9*

^rem-64-2

The lecture remarked that the formula resembles Burnside's Lemma (Theorem [[§30 Orbit–Stabilizer#^thm-30-7|§30.7]], PS 3.3) and left the connection to think about. It is an instance:

> [!theorem] Corollary §64.11: Burnside's Lemma from the Trace Formula
> Let a finite group $G$ act on a finite set $X$, let $\mathbb{Q} \subseteq k$, and let $kX$ be the permutation representation (Definition [[§59 Representations and Subrepresentations#^def-59-2|§59.2]]).
>
> 1. $\operatorname{Tr}\rho_{kX}(g) = |\operatorname{Fix}(g)|$, the number of $x \in X$ with $gx = x$.
> 2. The orbit sums $s_O = \sum_{x \in O} e_x$, one for each orbit $O$, form a basis of $(kX)^G$. So $\dim (kX)^G = |G \backslash X|$, the number of orbits.
> 3. Hence $|G \backslash X| = \frac{1}{|G|}\sum_{g \in G} |\operatorname{Fix}(g)|$, which is Burnside's Lemma (Theorem [[§30 Orbit–Stabilizer#^thm-30-7|§30.7]]).
>
> *Source: the connection raised in lecture 11/9; the proof not from class*

^cor-64-11

> [!proof]+ Proof
> *Idea:* Counting orbits is counting invariant vectors of a permutation representation.
>
> *(Not from class; filled in.)* **(1)** In the basis $(e_x)_{x \in X}$, $g e_x = e_{gx}$, so the matrix of $\rho(g)$ has the entry $1$ in position $(gx, x)$ and $0$ elsewhere in column $x$. Its diagonal entry in position $(x, x)$ is $1$ if $gx = x$ and $0$ otherwise, so $\operatorname{Tr}\rho_{kX}(g) = |\operatorname{Fix}(g)| \cdot 1_k = |\operatorname{Fix}(g)|$.
>
> **(2)** Let $v = \sum_{x} a_x e_x$. Then, substituting $y = gx$,
>
> $$
> gv = \sum_{x \in X} a_x e_{gx} = \sum_{y \in X} a_{g^{-1}y}\, e_y.
> $$
>
> So $gv = v$ for all $g$ if and only if $a_{g^{-1}y} = a_y$ for all $g \in G$ and $y \in X$, that is, if and only if $x \mapsto a_x$ is constant on each orbit, since $x$ and $y$ lie in the same orbit exactly when $x = g^{-1}y$ for some $g$. Such a $v$ is $\sum_O a_O\, s_O$, with $a_O$ the common value on $O$. So the orbit sums span $(kX)^G$. Each $s_O$ is invariant, by the criterion just proved. They are linearly independent, because distinct orbits are disjoint, so distinct $s_O$ involve disjoint sets of basis vectors $e_x$, and each $s_O \neq 0$ since orbits are nonempty.
>
> **(3)** By Theorem [[§64 Invariant Vectors#^thm-64-10|§64.10]] with $V = kX$, using (1) and (2),
>
> $$
> |G \backslash X| = \dim (kX)^G = \frac{1}{|G|}\sum_{g \in G} \operatorname{Tr}\rho_{kX}(g) = \frac{1}{|G|}\sum_{g \in G} |\operatorname{Fix}(g)|.
> $$
>
> Both sides are rational numbers, and $\mathbb{Q} \subseteq k$, so this is the equality of Burnside's Lemma.

^pf-64-11

*Uses:* [[§64 Invariant Vectors#^thm-64-10|§64.10]]

> [!remark]- Connections
> - The first proof of Burnside's Lemma counts the pairs $(g, x)$ with $gx = x$ by orbit–stabilizer: [[§30 Orbit–Stabilizer#^thm-30-7|Thm. §30.7]], from [[493 Problem Set 3#^hw-3-3|Problem Set 3, Problem 3.3]].

Worksheet 15's formula therefore generalizes Burnside's Lemma from permutation representations to all finite-dimensional representations, with the number of fixed points replaced by the trace.

## Examples

> [!example] Example §64.3: The Trivial and the Sign Representation
> *(Not from class.)* Let $\mathbb{Q} \subseteq k$.
>
> 1. If $G$ acts trivially on $V$ (Example [[§59 Representations and Subrepresentations#^ex-59-1|§59.1]]), then $V^G = V$ and $\operatorname{Tr}\rho_V(g) = \operatorname{Tr}(\mathrm{id}_V) = \dim V$ for every $g$, so Theorem [[§64 Invariant Vectors#^thm-64-10|§64.10]] reads $\dim V = \frac{1}{|G|} \cdot |G| \dim V$.
> 2. Let $n \geq 2$ and let $S_n$ act on $k$ by $\sigma \cdot c = \operatorname{sgn}(\sigma)\,c$, the sign representation (Example [[§59 Representations and Subrepresentations#^ex-59-2|§59.2]]). An invariant $c$ satisfies $-c = (1\,2) \cdot c = c$, so $2c = 0$ and $c = 0$: $k^{S_n} = \{0\}$. On the other side $\operatorname{Tr}\rho(\sigma) = \operatorname{sgn}(\sigma)$, and $\sum_{\sigma \in S_n} \operatorname{sgn}(\sigma) = 0$, since the even permutations $A_n$ and the odd permutations, the other coset of $A_n$, have $n!/2$ elements each. So both sides of the theorem are $0$.

^ex-64-3

> [!example] Example §64.4: $S_3$ on $k^3$ and on the Plane $x + y + z = 0$
> *(Not from class.)* Let $\mathbb{Q} \subseteq k$, let $S_3$ permute the coordinates of $k^3 = k\{1,2,3\}$, and let $U_1 = k(1,1,1)$ and $U_2 = \{x + y + z = 0\}$ be the subrepresentations of Example [[§59 Representations and Subrepresentations#^ex-59-3|§59.3]].
>
> 1. *Invariant vectors.* If $(x, y, z)$ is invariant, then $(1\,2)$ gives $x = y$ and $(2\,3)$ gives $y = z$; conversely the constant vectors are fixed by every permutation. So $(k^3)^{S_3} = U_1$.
> 2. *The averaging operator.* As $\sigma$ runs over $S_3$, $\sigma(i)$ takes each value $j$ exactly twice: the $\sigma$ with $\sigma(i) = j$ form a coset of the stabilizer of $i$, which has $2$ elements. So
>
> $$
> \pi(e_i) = \frac16 \sum_{\sigma \in S_3} e_{\sigma(i)} = \frac{2}{6}(e_1 + e_2 + e_3), \qquad \pi(x, y, z) = \frac{x + y + z}{3}\,(1, 1, 1).
> $$
>
> Its matrix is $\frac13$ times the all-ones matrix, $\operatorname{Ker}\pi = U_2$, and Corollary [[§64 Invariant Vectors#^cor-64-8|§64.8]] is the decomposition $k^3 = U_1 \oplus U_2$ of When $k\{1,2,3\} = U_1 \oplus U_2$ (Proposition [[§59 Representations and Subrepresentations#^prop-59-3|§59.3]]).
> 3. *The count.* $\rho(\sigma)$ is a permutation matrix, so its trace is the number of fixed points of $\sigma$ (Corollary [[§64 Invariant Vectors#^cor-64-11|§64.11]](1)): $3$ for $e$, $1$ for each of the three transpositions, $0$ for each of the two $3$-cycles. So
>
> $$
> \frac16\big(3 + 3 \cdot 1 + 2 \cdot 0\big) = 1 = \dim U_1.
> $$
>
> 4. *The plane.* In a basis $(1,1,1), b_1, b_2$ with $b_1, b_2$ a basis of $U_2$, every $\rho(\sigma)$ is block diagonal (Proposition [[§60 Direct Sums and Maschke's Theorem#^prop-60-2|§60.2]]) with blocks $[\,1\,]$ and $\rho_{U_2}(\sigma)$. So $\operatorname{Tr}\rho_{U_2}(\sigma) = \operatorname{Tr}\rho(\sigma) - 1$, which is $2$, $0$ (transpositions) and $-1$ ($3$-cycles). Then
>
> $$
> \frac16\big(2 + 3 \cdot 0 + 2 \cdot (-1)\big) = 0 = \dim U_2^{S_3},
> $$
>
> as it must be: $U_2^{S_3} = U_2 \cap U_1 = \{0\}$, since $3 \neq 0$ in $k$.

^ex-64-4

![[m493-63-1.svg]]

*(Not from lecture; figure added.)* The averaging operator of Example [[§64 Invariant Vectors#^ex-64-4|§64.4]] over $k = \mathbb{R}$, for $v = (1.5, 0.35, -0.65)$. Permuting the coordinates of $v$ gives six points (blue), its orbit. All of them have coordinate sum $1.2$, so they lie in the plane $x + y + z = 1.2$, where they form a hexagon. $\pi(v)$, the average of the six, is the centre of mass of the hexagon (red, $(0.4, 0.4, 0.4)$), and it lies on the line $U_1 = \mathbb{R}(1,1,1)$ of invariant vectors. The orange arrow $\pi(v) - v$ is parallel to the plane $x + y + z = 0$, so $v - \pi(v) \in U_2 = \operatorname{Ker}\pi$: this is the decomposition $v = \pi(v) + (v - \pi(v))$ of $\mathbb{R}^3 = U_1 \oplus U_2$.
