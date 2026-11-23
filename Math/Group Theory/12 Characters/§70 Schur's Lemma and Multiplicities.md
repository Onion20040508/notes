---
type: section
subject: "[[Group Theory]]"
chapter: 12
section: 70
tags: [group-theory, math493]
---
← [[§69 Dual Representations]] · ↑ [[· 12 Characters]] · [[§71 The Character Table]] →

*Source: Lecture and Worksheet 17, *Dimensions of hom spaces, and Schur's lemma* (Mon Nov 16): WS 17.1–17.5; Problem Set 10, Problem 10.3 (submitted), in the last subsection. Reference: Axler, *Linear Algebra Done Right* (existence of eigenvalues).*

Throughout this section, unless something else is said, $G$ is a finite group, $k$ is a field containing $\mathbb{Q}$, and all representations are finite-dimensional representations of $G$ over $k$. Under these hypotheses there are two main results so far. The first is Maschke's theorem (Theorem [[§62 Direct Sums and Maschke's Theorem#^thm-62-10|§62.10]]), by which every representation is a direct sum of simple representations (Corollary [[§65 Simple Representations#^cor-65-3|§65.3]]). The second is the formula

$$
\dim\operatorname{Hom}_G(V, W) = \frac{1}{|G|}\sum_{g \in G} \chi_V(g^{-1})\,\chi_W(g)
$$

(Theorem [[§68 Homomorphisms Between Representations#^thm-68-6|§68.6]]; for its forms over $\mathbb{R}$ and $\mathbb{C}$, which Worksheet 17 recalls, see Corollary [[§68 Homomorphisms Between Representations#^cor-68-12|§68.12]]). This section puts the two together: split $V$ and $W$ into simple representations and see what the formula says.

The hypothesis $\mathbb{Q} \subseteq k$ says that $k$ has characteristic $0$: no sum $1 + 1 + \cdots + 1$ with a positive number of terms is $0$ in $k$. It is stronger than “$k$ is infinite”. *(Example not from class.)* The field $\mathbb{F}_p(t)$ of rational functions in one variable over $\mathbb{F}_p$ is infinite, and $p = 0$ in it.

## Repeated Direct Sums

The formulas of Worksheet 17 contain sums such as $V \oplus V$. The direct sum of [[§62 Direct Sums and Maschke's Theorem|§62]] (Definition [[§62 Direct Sums and Maschke's Theorem#^def-62-1|§62.1]]) is internal: its summands are subspaces of a given space that meet only in $0$, and $V \cap V = V$. So a different construction is meant, the external direct sum of the remark [[§57 Internal and External Direct Products#^rem-57-1|Two Meanings of “Direct Sum”]] in [[§57 Internal and External Direct Products|§57]], now for representations.

> [!definition] Definition §70.1: External Direct Sum of Representations
> Let $V_1, \ldots, V_r$ be [[§61 Representations and Subrepresentations#^def-61-1|representations]] of a group $G$ over a field $k$. Their **external direct sum** $V_1 \oplus \cdots \oplus V_r$ is the set of $r$-tuples $(v_1, \ldots, v_r)$ with $v_i \in V_i$, with the operations
>
> $$
> (u_1, \ldots, u_r) + (v_1, \ldots, v_r) = (u_1 + v_1, \ldots, u_r + v_r), \qquad c\,(v_1, \ldots, v_r) = (cv_1, \ldots, cv_r),
> $$
>
> and with $G$ acting on each coordinate:
>
> $$
> g\,(v_1, \ldots, v_r) = (gv_1, \ldots, gv_r).
> $$
>
> For $r = 0$ it is the zero space $\{0\}$.
>
> *Source: lecture 11/16*

^def-70-1

*Source note.* Lecture 11/16, for $r$ copies of one representation; the general case is not from class.

> [!remark]- Connections
> - Linear Algebra: as a vector space this is the product $V_1 \times \cdots \times V_r$ of [[§11 Products and Quotients of Vector Spaces#^ladr-3-87|LADR 3.87]]; here $G$ acts on it as well.
> - The internal direct sum of two subspaces is [[§62 Direct Sums and Maschke's Theorem#^def-62-1|Definition §62.1]], of several subspaces [[§65 Simple Representations#^def-65-3|Definition §65.3]].

The external direct sum is a representation of $G$: the vector space axioms, the linearity of each $g$ and the two action axioms hold for tuples because they hold in every coordinate.

> [!definition] Definition §70.2: Repeated Direct Sum
> Let $V$ be a representation of $G$ and $a \geq 0$ an integer. The **repeated direct sum**
>
> $$
> V^{\oplus a} = \underbrace{V \oplus \cdots \oplus V}_{a \text{ copies}} = \{(v_1, \ldots, v_a) : v_1, \ldots, v_a \in V\}
> $$
>
> is the external direct sum (Definition [[§70 Schur's Lemma and Multiplicities#^def-70-1|§70.1]]) of $a$ copies of $V$, a representation of $G$. In particular $V^{\oplus 0} = \{0\}$ and $V^{\oplus 1} = V$.
>
> *Source: lecture 11/16*

^def-70-2

The underlying set of $V^{\oplus a}$ is the set $V^a$ of $a$-tuples. The notation $V^{\oplus a}$ stands for this set together with its addition, its scalar multiplication and the action of $G$: a vector space is a set together with its operations, not the set alone. In a sum such as $\bigoplus_i V_i^{\oplus a_i}$ the elements are tuples of tuples; they are read as one long tuple, with $a_1$ entries from $V_1$, then $a_2$ entries from $V_2$, and so on.

> [!theorem] Lemma §70.1: Internal Direct Sums Are External Direct Sums
> Let $W$ be a representation of $G$ and $U_1, \ldots, U_r$ [[§61 Representations and Subrepresentations#^def-61-3|subrepresentations]] with $W = U_1 \oplus \cdots \oplus U_r$ as an internal direct sum (Definition [[§65 Simple Representations#^def-65-3|§65.3]]). Then
>
> $$
> \sigma: U_1 \oplus \cdots \oplus U_r \to W, \qquad \sigma(u_1, \ldots, u_r) = u_1 + \cdots + u_r,
> $$
>
> defined on the external direct sum (Definition [[§70 Schur's Lemma and Multiplicities#^def-70-1|§70.1]]), is an isomorphism of $G$-representations (Definition [[§61 Representations and Subrepresentations#^def-61-5|§61.5]]).
>
> *Source: not from class*

^lem-70-1

> [!proof]+ Proof
> *(Not from class; filled in.)* *Linear.* $\sigma\big(c(u_i) + c'(u_i')\big) = \sum_i (cu_i + c'u_i') = c\sum_i u_i + c'\sum_i u_i' = c\,\sigma\big((u_i)\big) + c'\,\sigma\big((u_i')\big)$.
>
> *Commutes with $G$.* Each $g$ acts on $W$ by a linear map, so $\sigma\big(g(u_1, \ldots, u_r)\big) = gu_1 + \cdots + gu_r = g(u_1 + \cdots + u_r) = g\,\sigma(u_1, \ldots, u_r)$.
>
> *Bijective.* By Definition [[§65 Simple Representations#^def-65-3|§65.3]], every $w \in W$ is $u_1 + \cdots + u_r$ with $u_i \in U_i$ in exactly one way, that is, $w = \sigma(u_1, \ldots, u_r)$ for exactly one tuple.

^pf-70-1

*Uses:* [[§65 Simple Representations#^def-65-3|Def. §65.3]]

> [!theorem] Proposition §70.2: The Character of an External Direct Sum
> Let $V_1, \ldots, V_r$ be finite-dimensional representations of a group $G$ over a field $k$, and let $E = V_1 \oplus \cdots \oplus V_r$ be their external direct sum (Definition [[§70 Schur's Lemma and Multiplicities#^def-70-1|§70.1]]). Then
>
> 1. $\dim E = \dim V_1 + \cdots + \dim V_r$;
> 2. $\chi_E = \chi_{V_1} + \cdots + \chi_{V_r}$ for the characters (Definition [[§67 Characters of Representations#^def-67-1|§67.1]]).
>
> In particular $\dim V^{\oplus a} = a\dim V$ and $\chi_{V^{\oplus a}} = a\,\chi_V$.
>
> *Source: not from class; WS 18.2*

^prop-70-2

> [!proof]+ Proof
> *(Not from class; the lecture of 11/9 proved the case of an internal direct sum of two subrepresentations (Proposition [[§67 Characters of Representations#^prop-67-2|§67.2]]); for two summands this is WS 18.2.)* *Idea:* in a basis of $E$ made from bases of the $V_i$, every $g$ acts by a block diagonal matrix.
>
> *(Not from class; filled in.)* For $v \in V_i$ let $\iota_i(v) \in E$ be the tuple with $v$ in position $i$ and $0$ in all other positions. Then $(v_1, \ldots, v_r) = \iota_1(v_1) + \cdots + \iota_r(v_r)$.
>
> **(1)** Choose a basis $B_i$ of $V_i$ for every $i$. The tuples $\iota_i(b)$ with $1 \leq i \leq r$ and $b \in B_i$ form a basis of $E$: writing each $v_i$ as a combination of $B_i$ expresses $(v_1, \ldots, v_r) = \sum_i \iota_i(v_i)$ as a combination of them, and the coefficients are unique because the $i$-th coordinate of the combination determines the coefficients of the $\iota_i(b)$, $b \in B_i$. The number of these tuples is $\sum_i \dim V_i$.
>
> **(2)** Let $g \in G$ and let $M^{(i)}$ be the matrix of $\rho_{V_i}(g)$ in the basis $B_i$, so $gb = \sum_{b' \in B_i} M^{(i)}_{b'b}\,b'$ for $b \in B_i$. Since $g$ acts on each coordinate,
>
> $$
> g\,\iota_i(b) = \iota_i(gb) = \sum_{b' \in B_i} M^{(i)}_{b'b}\,\iota_i(b').
> $$
>
> So in the basis of (1) the matrix of $\rho_E(g)$ is block diagonal with the blocks $M^{(1)}, \ldots, M^{(r)}$. Its diagonal is the diagonal of $M^{(1)}$ followed by those of $M^{(2)}, \ldots, M^{(r)}$, so
>
> $$
> \chi_E(g) = \operatorname{Tr}M^{(1)} + \cdots + \operatorname{Tr}M^{(r)} = \chi_{V_1}(g) + \cdots + \chi_{V_r}(g).
> $$
>
> The last sentence of the statement is the case $V_1 = \cdots = V_a = V$.

^pf-70-2

> [!theorem] Corollary §70.3: Decomposition into Simple Representations with Multiplicities
> Let $G$ be a finite group, $k$ a field in which $|G| \neq 0$, and $V$ a finite-dimensional representation of $G$ over $k$. Then there are [[§65 Simple Representations#^def-65-1|simple]] representations $S_1, \ldots, S_r$ of $G$ over $k$, with $S_i \not\cong S_j$ for $i \neq j$, and positive integers $a_1, \ldots, a_r$ such that
>
> $$
> V \cong S_1^{\oplus a_1} \oplus \cdots \oplus S_r^{\oplus a_r},
> $$
>
> with $r = 0$ when $V = \{0\}$.
>
> *Source: lecture 11/16*

^cor-70-3

> [!proof]+ Proof
> *(Lecture 11/16, used in the proof of Lemma [[§70 Schur's Lemma and Multiplicities#^lem-70-11|§70.11]]; the proof is not from class.)* *Idea:* decompose $V$ into simple subrepresentations and collect the summands that are isomorphic to each other.
>
> *(Not from class; filled in.)* By Corollary [[§65 Simple Representations#^cor-65-3|§65.3]], $V = V_1 \oplus \cdots \oplus V_n$ (internal direct sum, Definition [[§65 Simple Representations#^def-65-3|§65.3]]) with simple subrepresentations $V_1, \ldots, V_n$.
>
> *Choosing the $S_i$.* Being isomorphic is an equivalence relation on representations (Lemma [[§61 Representations and Subrepresentations#^lem-61-5|§61.5]](3)). It divides $V_1, \ldots, V_n$ into classes of mutually isomorphic summands. Choose one summand from each class and call the chosen ones $S_1, \ldots, S_r$. They are simple and pairwise non-isomorphic, and every $V_j$ is isomorphic to exactly one of them, say to $S_{i(j)}$. Let $a_i \geq 1$ be the number of $j$ with $i(j) = i$.
>
> *The isomorphism.* For every $j$ choose an isomorphism $\beta_j: S_{i(j)} \to V_j$. The order of the summands of an internal direct sum does not matter, since addition in $V$ is commutative; so we may number the $V_j$ such that $i(1) \leq i(2) \leq \cdots \leq i(n)$. Then the external direct sum $E = S_{i(1)} \oplus \cdots \oplus S_{i(n)}$ is $S_1^{\oplus a_1} \oplus \cdots \oplus S_r^{\oplus a_r}$, read as one long tuple. The map
>
> $$
> E \to V_1 \oplus \cdots \oplus V_n \ \text{(external)}, \qquad (s_1, \ldots, s_n) \mapsto (\beta_1(s_1), \ldots, \beta_n(s_n)),
> $$
>
> is linear, bijective and commutes with $G$, because each $\beta_j$ has these three properties and all operations are coordinatewise. Composing it with the isomorphism $\sigma$ of Lemma [[§70 Schur's Lemma and Multiplicities#^lem-70-1|§70.1]] gives an isomorphism $E \to V$ (Lemma [[§61 Representations and Subrepresentations#^lem-61-5|§61.5]](1)).

^pf-70-3

*Uses:* [[§65 Simple Representations#^cor-65-3|§65.3]], [[§65 Simple Representations#^def-65-3|Def. §65.3]], [[§61 Representations and Subrepresentations#^lem-61-5|§61.5]], [[§70 Schur's Lemma and Multiplicities#^lem-70-1|§70.1]]

> [!remark]- Connections
> - Quantum Field Theory: complete reducibility of unitary representations of compact groups, [[§CB.7 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-7-16|QFT Thm. §CB.7.16]].

## $\dim\operatorname{Hom}_G$ and Direct Sums

The next proposition is stated for external direct sums. For an internal direct sum of subrepresentations the same formulas hold, because it is isomorphic to the external one (Lemma [[§70 Schur's Lemma and Multiplicities#^lem-70-1|§70.1]]) and isomorphic representations have the same character (Lemma [[§67 Characters of Representations#^lem-67-3|§67.3]]).

> [!theorem] Proposition §70.4: $\dim\operatorname{Hom}_G$ Is Additive in Each Variable
> Let $G$ be a finite group and $k$ a field containing $\mathbb{Q}$. Let $V$, $V_1$, $V_2$, $W$, $W_1$, $W_2$ be finite-dimensional representations of $G$ over $k$. The direct sums are external (Definitions [[§70 Schur's Lemma and Multiplicities#^def-70-1|§70.1]] and [[§70 Schur's Lemma and Multiplicities#^def-70-2|§70.2]]), and $\operatorname{Hom}_G$ is the space of homomorphisms of representations (Definition [[§68 Homomorphisms Between Representations#^def-68-2|§68.2]]).
>
> 1. $\dim\operatorname{Hom}_G(V, W_1 \oplus W_2) = \dim\operatorname{Hom}_G(V, W_1) + \dim\operatorname{Hom}_G(V, W_2)$, and $\dim\operatorname{Hom}_G(V_1 \oplus V_2, W) = \dim\operatorname{Hom}_G(V_1, W) + \dim\operatorname{Hom}_G(V_2, W)$.
> 2. More generally, for finite-dimensional representations $V_1, \ldots, V_m$ and $W_1, \ldots, W_n$ and integers $a_1, \ldots, a_m \geq 0$, $b_1, \ldots, b_n \geq 0$,
>
> $$
> \dim\operatorname{Hom}_G\Big(\bigoplus_{i=1}^m V_i^{\oplus a_i},\ \bigoplus_{j=1}^n W_j^{\oplus b_j}\Big) = \sum_{i=1}^m\sum_{j=1}^n a_ib_j\,\dim\operatorname{Hom}_G(V_i, W_j).
> $$
>
> *Source: WS 17.1; worksheet session 11/16*

^prop-70-4

> [!proof]+ Proof
> *Idea:* the right side of the dimension formula is linear in $\chi_V$ and in $\chi_W$, and characters add over direct sums.
>
> *(Worksheet session 11/16; the lecture's summary was that $\dim\operatorname{Hom}_G$ “acts bilinearly”.)* For functions $\chi, \psi: G \to k$ write, in this proof only,
>
> $$
> B(\chi, \psi) = \frac{1}{|G|}\sum_{g \in G} \chi(g^{-1})\,\psi(g).
> $$
>
> Each term of the sum is a product of one value of $\chi$ and one value of $\psi$, so $B$ is linear in each variable:
>
> $$
> B(c\chi + c'\chi', \psi) = c\,B(\chi, \psi) + c'\,B(\chi', \psi), \qquad B(\chi, c\psi + c'\psi') = c\,B(\chi, \psi) + c'\,B(\chi, \psi').
> $$
>
> In this notation Theorem [[§68 Homomorphisms Between Representations#^thm-68-6|§68.6]] says $\dim\operatorname{Hom}_G(V, W) = B(\chi_V, \chi_W)$.
>
> **(1)** By Proposition [[§70 Schur's Lemma and Multiplicities#^prop-70-2|§70.2]], $\chi_{W_1 \oplus W_2} = \chi_{W_1} + \chi_{W_2}$. So
>
> $$
> \dim\operatorname{Hom}_G(V, W_1 \oplus W_2) = B(\chi_V, \chi_{W_1} + \chi_{W_2}) = B(\chi_V, \chi_{W_1}) + B(\chi_V, \chi_{W_2}),
> $$
>
> which is $\dim\operatorname{Hom}_G(V, W_1) + \dim\operatorname{Hom}_G(V, W_2)$. The second equation follows in the same way from $\chi_{V_1 \oplus V_2} = \chi_{V_1} + \chi_{V_2}$ and linearity in the first variable.
>
> **(2)** By Proposition [[§70 Schur's Lemma and Multiplicities#^prop-70-2|§70.2]], the character of $\bigoplus_i V_i^{\oplus a_i}$ is $\sum_i a_i\chi_{V_i}$, and the character of $\bigoplus_j W_j^{\oplus b_j}$ is $\sum_j b_j\chi_{W_j}$. Expanding in both variables,
>
> $$
> B\Big(\sum_i a_i\chi_{V_i},\ \sum_j b_j\chi_{W_j}\Big) = \sum_{i,j} a_ib_j\,B(\chi_{V_i}, \chi_{W_j}) = \sum_{i,j} a_ib_j\,\dim\operatorname{Hom}_G(V_i, W_j).
> $$

^pf-70-4

*Uses:* [[§68 Homomorphisms Between Representations#^thm-68-6|§68.6]], [[§70 Schur's Lemma and Multiplicities#^prop-70-2|§70.2]]

> [!proof]+ Second proof of (1) (without characters)
> *(Not from class.)* This proof uses no characters, so it works for every group and every field.
>
> *Second variable.* Let $p_1: W_1 \oplus W_2 \to W_1$ and $p_2: W_1 \oplus W_2 \to W_2$ be the projections $p_i(w_1, w_2) = w_i$. They are linear and commute with $G$, since $G$ acts on each coordinate. Define
>
> $$
> \Phi: \operatorname{Hom}_G(V, W_1 \oplus W_2) \to \operatorname{Hom}_G(V, W_1) \oplus \operatorname{Hom}_G(V, W_2), \qquad \Phi(\alpha) = (p_1 \circ \alpha,\ p_2 \circ \alpha),
> $$
>
> where the target is the external direct sum of two vector spaces. The entries $p_i \circ \alpha$ are homomorphisms of representations (Lemma [[§61 Representations and Subrepresentations#^lem-61-5|§61.5]](1)), and $\Phi$ is linear. In the other direction, for $\alpha_1 \in \operatorname{Hom}_G(V, W_1)$ and $\alpha_2 \in \operatorname{Hom}_G(V, W_2)$ let
>
> $$
> \Psi(\alpha_1, \alpha_2): V \to W_1 \oplus W_2, \qquad v \mapsto (\alpha_1(v), \alpha_2(v)).
> $$
>
> It is linear, and it commutes with $G$: $(\alpha_1(gv), \alpha_2(gv)) = (g\alpha_1(v), g\alpha_2(v)) = g\,(\alpha_1(v), \alpha_2(v))$. The two maps are inverse to each other: $p_i \circ \Psi(\alpha_1, \alpha_2) = \alpha_i$, and $\Psi(p_1 \circ \alpha, p_2 \circ \alpha)(v) = (p_1(\alpha(v)), p_2(\alpha(v))) = \alpha(v)$. So $\Phi$ is an isomorphism of vector spaces, and the dimension of an external direct sum is the sum of the dimensions (Proposition [[§70 Schur's Lemma and Multiplicities#^prop-70-2|§70.2]](1)).
>
> *First variable.* Let $\iota_1: V_1 \to V_1 \oplus V_2$, $v_1 \mapsto (v_1, 0)$, and $\iota_2: V_2 \to V_1 \oplus V_2$, $v_2 \mapsto (0, v_2)$. They are linear and commute with $G$. The map
>
> $$
> \operatorname{Hom}_G(V_1 \oplus V_2, W) \to \operatorname{Hom}_G(V_1, W) \oplus \operatorname{Hom}_G(V_2, W), \qquad \alpha \mapsto (\alpha \circ \iota_1,\ \alpha \circ \iota_2),
> $$
>
> is linear, with inverse $(\alpha_1, \alpha_2) \mapsto \big((v_1, v_2) \mapsto \alpha_1(v_1) + \alpha_2(v_2)\big)$: indeed $\alpha(v_1, v_2) = \alpha(\iota_1(v_1) + \iota_2(v_2)) = (\alpha \circ \iota_1)(v_1) + (\alpha \circ \iota_2)(v_2)$, and the map $(v_1, v_2) \mapsto \alpha_1(v_1) + \alpha_2(v_2)$ is linear and commutes with $G$ because $\alpha_1$ and $\alpha_2$ do. The dimensions add as before.

^pf-70-4-2

*Uses:* [[§61 Representations and Subrepresentations#^lem-61-5|§61.5]], [[§70 Schur's Lemma and Multiplicities#^prop-70-2|§70.2]]

Applying the second proof one summand at a time shows that a homomorphism between two direct sums is a “matrix” of homomorphisms between the summands, one for each pair (summand of the source, summand of the target). This is the picture behind (2), and it is drawn in the figure after Corollary [[§70 Schur's Lemma and Multiplicities#^cor-70-9|§70.9]].

By (2), it is enough to understand $\operatorname{Hom}_G(S, T)$ for two simple representations $S$ and $T$.

## Schur's Lemma

> [!theorem] Proposition §70.5: Schur's Lemma
> Let $G$ be a group, $S$ a simple representation of $G$ (Definition [[§65 Simple Representations#^def-65-1|§65.1]]) and $V$ any representation of $G$ over the same field.
>
> 1. A [[§61 Representations and Subrepresentations#^def-61-4|homomorphism]] of $G$-representations $\alpha: S \to V$ is either injective or zero.
> 2. A homomorphism of $G$-representations $\alpha: V \to S$ is either surjective or zero.
> 3. If $S$ and $T$ are both simple, a homomorphism of $G$-representations $\alpha: S \to T$ is either an [[§61 Representations and Subrepresentations#^def-61-5|isomorphism]] or zero.
>
> *Source: WS 17.2; worksheet session 11/16*

^prop-70-5

> [!proof]+ Proof
> *Idea:* the kernel and the image of $\alpha$ are subrepresentations, and a simple representation has only two subrepresentations.
>
> *(Worksheet session 11/16; the fact it needs, Kernels and Images Are Subrepresentations, Proposition [[§61 Representations and Subrepresentations#^prop-61-4|§61.4]], was proved again on the board.)*
>
> **(1)** $\operatorname{Ker}\alpha$ is a subrepresentation of $S$ (Proposition [[§61 Representations and Subrepresentations#^prop-61-4|§61.4]](1)). Since $S$ is simple, $\operatorname{Ker}\alpha = \{0\}$ or $\operatorname{Ker}\alpha = S$. In the first case $\alpha$ is injective: if $\alpha(s) = \alpha(s')$, then $s - s' \in \operatorname{Ker}\alpha = \{0\}$. In the second case $\alpha = 0$.
>
> **(2)** $\operatorname{Im}\alpha$ is a subrepresentation of $S$ (Proposition [[§61 Representations and Subrepresentations#^prop-61-4|§61.4]](2)). Since $S$ is simple, $\operatorname{Im}\alpha = S$, and $\alpha$ is surjective, or $\operatorname{Im}\alpha = \{0\}$, and $\alpha = 0$.
>
> **(3)** Suppose $\alpha \neq 0$. By (1), applied to the simple representation $S$ and $V = T$, $\alpha$ is injective. By (2), applied to $V = S$ and the simple representation $T$, $\alpha$ is surjective. So $\alpha$ is a bijective homomorphism of $G$-representations, that is, an isomorphism (Definition [[§61 Representations and Subrepresentations#^def-61-5|§61.5]]); its inverse is again a homomorphism of $G$-representations (Lemma [[§61 Representations and Subrepresentations#^lem-61-5|§61.5]](2)).

^pf-70-5

*Uses:* [[§61 Representations and Subrepresentations#^prop-61-4|§61.4]], [[§61 Representations and Subrepresentations#^def-61-5|Def. §61.5]], [[§61 Representations and Subrepresentations#^lem-61-5|§61.5]]

> [!remark]- Connections
> - Quantum Field Theory: Schur's Lemma for representations of Lie groups and Lie algebras, [[§CB.7 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-7-4|QFT Thm. §CB.7.4]]; its first part is this proposition, its second part is [[§70 Schur's Lemma and Multiplicities#^prop-70-8|Proposition §70.8]].

![[m493-70-1.svg]]

*(Not from lecture; figure added.)* Schur's Lemma (Proposition [[§70 Schur's Lemma and Multiplicities#^prop-70-5|§70.5]]). Top: a homomorphism out of a simple representation $S$. Its kernel is a subrepresentation of $S$, and $S$ has only the subrepresentations $\{0\}$ and $S$; so either $\alpha$ embeds a copy of $S$ into $V$ (left), or the kernel (red) is all of $S$ and $\alpha = 0$ (right). Bottom: a homomorphism into $S$. Its image is a subrepresentation of $S$; so either the image (blue) is all of $S$ (left), or it is $\{0\}$ and $\alpha = 0$ (right). Between two simple representations both alternatives apply, which leaves only isomorphisms and the zero map.

> [!theorem] Corollary §70.6: Non-Isomorphic Simple Representations Have Only the Zero Homomorphism
> Let $S$ and $T$ be [[§65 Simple Representations#^def-65-1|simple]] representations of a group $G$ over the same field, with $S \not\cong T$. Then $\operatorname{Hom}_G(S, T) = \{0\}$ (Definition [[§68 Homomorphisms Between Representations#^def-68-2|§68.2]]): the only homomorphism of $G$-representations $S \to T$ is zero.
>
> *Source: WS 17.3, the first step; worksheet session 11/16*

^cor-70-6

> [!proof]+ Proof
> *(Worksheet session 11/16.)* By Schur's Lemma (Proposition [[§70 Schur's Lemma and Multiplicities#^prop-70-5|§70.5]](3)), every $\alpha \in \operatorname{Hom}_G(S, T)$ is an isomorphism or zero. There is no isomorphism $S \to T$, since $S \not\cong T$. So $\alpha = 0$.

^pf-70-6

*Uses:* [[§70 Schur's Lemma and Multiplicities#^prop-70-5|§70.5]]

> [!theorem] Proposition §70.7: $\dim\operatorname{Hom}_G$ Between Sums of Simple Representations
> Let $G$ be a finite group and $k$ a field containing $\mathbb{Q}$. Let $S_1, \ldots, S_r$ be finite-dimensional [[§65 Simple Representations#^def-65-1|simple]] representations of $G$ over $k$ with $S_i \not\cong S_j$ for $i \neq j$, and let $a_1, \ldots, a_r \geq 0$ and $b_1, \ldots, b_r \geq 0$ be integers. Then
>
> $$
> \dim\operatorname{Hom}_G\Big(\bigoplus_{i=1}^r S_i^{\oplus a_i},\ \bigoplus_{j=1}^r S_j^{\oplus b_j}\Big) = \sum_{i=1}^r a_ib_i\,\dim\operatorname{Hom}_G(S_i, S_i).
> $$
>
> *Source: WS 17.3; worksheet session 11/16*

^prop-70-7

> [!proof]+ Proof
> *(Worksheet session 11/16.)* By WS 17.1 (Proposition [[§70 Schur's Lemma and Multiplicities#^prop-70-4|§70.4]](2)) with $V_i = W_i = S_i$, the left side is
>
> $$
> \sum_{i=1}^r\sum_{j=1}^r a_ib_j\,\dim\operatorname{Hom}_G(S_i, S_j).
> $$
>
> For $i \neq j$, $\operatorname{Hom}_G(S_i, S_j) = \{0\}$ (Corollary [[§70 Schur's Lemma and Multiplicities#^cor-70-6|§70.6]]), so its dimension is $0$. Only the terms with $i = j$ remain.

^pf-70-7

*Uses:* [[§70 Schur's Lemma and Multiplicities#^prop-70-4|§70.4]], [[§70 Schur's Lemma and Multiplicities#^cor-70-6|§70.6]]

The lecture's summary: non-isomorphic simple representations behave like orthogonal vectors, and the dimension is the dot product of the two vectors of multiplicities $(a_1, \ldots, a_r)$ and $(b_1, \ldots, b_r)$, with the weights $\dim\operatorname{Hom}_G(S_i, S_i)$. Each weight is at least $1$: the identity $\mathrm{Id}_{S_i}$ is a homomorphism of representations, and it is not zero because $S_i \neq \{0\}$.

**Transcription note (WS 17).** The worksheet numbers the simple representations $S_1, \ldots, S_k$. These notes write $S_1, \ldots, S_r$, because $k$ is the field.

## Schur's Lemma over $\mathbb{C}$

Over the complex numbers the weights $\dim\operatorname{Hom}_G(S_i, S_i)$ are all equal to $1$, so they need not be kept track of.

> [!theorem] Proposition §70.8: Schur's Lemma over $\mathbb{C}$
> Let $G$ be a group and $S$ a finite-dimensional [[§65 Simple Representations#^def-65-1|simple]] representation of $G$ over $\mathbb{C}$. Then
>
> $$
> \operatorname{Hom}_G(S, S) = \mathbb{C}\,\mathrm{Id}_S,
> $$
>
> the set of multiples of the identity. In particular $\dim\operatorname{Hom}_G(S, S) = 1$.
>
> *Source: WS 17.4; board 11/16*

^prop-70-8

> [!proof]+ Proof
> *Idea:* if $\lambda$ is an eigenvalue of $\alpha$, then $\alpha - \lambda\,\mathrm{Id}$ is a homomorphism of representations that is not injective, so by Schur's Lemma it is zero.
>
> *(Board 11/16.)* The best way to show that a space is one-dimensional is to name a vector that spans it, and here there is an obvious candidate, the identity. $\operatorname{Hom}_G(S, S)$ is a subspace of $\operatorname{Hom}(S, S)$: it is the space of invariant vectors of the representation $\operatorname{Hom}(S, S)$ (Proposition [[§68 Homomorphisms Between Representations#^prop-68-3|§68.3]](2), Lemma [[§66 Invariant Vectors#^lem-66-5|§66.5]]). It contains $\mathrm{Id}_S$, since $\mathrm{Id}_S(gs) = gs = g\,\mathrm{Id}_S(s)$. So $\mathbb{C}\,\mathrm{Id}_S \subseteq \operatorname{Hom}_G(S, S)$, and it remains to show that every $\alpha \in \operatorname{Hom}_G(S, S)$ is a multiple of $\mathrm{Id}_S$.
>
> Let $\alpha \in \operatorname{Hom}_G(S, S)$. Since $S$ is simple, $S \neq \{0\}$. A linear map from a nonzero finite-dimensional complex vector space to itself has an eigenvalue ([[§15 The Minimal Polynomial#^ladr-5-19|Axler 5.19]]); this is where the field $\mathbb{C}$ is used. Let $\lambda \in \mathbb{C}$ be an eigenvalue of $\alpha$ and $v \neq 0$ an eigenvector, $\alpha(v) = \lambda v$.
>
> **(1) $\alpha - \lambda\,\mathrm{Id}_S$ is not injective.** $(\alpha - \lambda\,\mathrm{Id}_S)(v) = \alpha(v) - \lambda v = \lambda v - \lambda v = 0$, and $v \neq 0$.
>
> **(2) $\alpha = \lambda\,\mathrm{Id}_S$.** Since $\operatorname{Hom}_G(S, S)$ is a subspace containing $\alpha$ and $\mathrm{Id}_S$, the map $\alpha - \lambda\,\mathrm{Id}_S$ is a homomorphism of $G$-representations $S \to S$. By Schur's Lemma (Proposition [[§70 Schur's Lemma and Multiplicities#^prop-70-5|§70.5]](1), with $V = S$) it is injective or zero. By (1) it is not injective, so it is zero. Hence for all $s \in S$,
>
> $$
> \alpha(s) - \lambda s = 0, \qquad \text{that is,} \qquad \alpha(s) = \lambda s = \lambda\,\mathrm{Id}_S(s).
> $$
>
> *The dimension.* $\mathrm{Id}_S \neq 0$ because $S \neq \{0\}$, so $\mathbb{C}\,\mathrm{Id}_S$ is one-dimensional.

^pf-70-8

*Uses:* [[§68 Homomorphisms Between Representations#^prop-68-3|§68.3]], [[§66 Invariant Vectors#^lem-66-5|§66.5]], [[§70 Schur's Lemma and Multiplicities#^prop-70-5|§70.5]]

> [!remark]- Connections
> - Linear Algebra: every operator on a nonzero finite-dimensional complex vector space has an eigenvalue, [[§15 The Minimal Polynomial#^ladr-5-19|LADR 5.19]].
> - Quantum Field Theory: in the form “an operator commuting with an irreducible representation is a multiple of the identity”, [[§CB.7 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-7-4|QFT Thm. §CB.7.4]]; it is used there to show that central elements and Casimir operators act as scalars.

**Transcription note (WS 17.4).** The first sentence of the worksheet's Problem 17.4 says “a finite dimensional $G$-representation over the field $\mathbb{C}$”, without the word “simple”. The lecture stated the problem for a simple representation, and the statement is false without it: for $G$ acting trivially on $\mathbb{C}^2$, every linear map $\mathbb{C}^2 \to \mathbb{C}^2$ is a homomorphism of representations, and $\dim\operatorname{Hom}_G(\mathbb{C}^2, \mathbb{C}^2) = 4$. The board referred to WS 17.2(3) in step (2): a map that is not injective is not an isomorphism, so it is zero. Part (1) gives the same conclusion directly.

> [!theorem] Corollary §70.9: Multiplicities over $\mathbb{C}$
> Let $G$ be a finite group. Let $S_1, \ldots, S_r$ be finite-dimensional [[§65 Simple Representations#^def-65-1|simple]] representations of $G$ over $\mathbb{C}$ with $S_i \not\cong S_j$ for $i \neq j$, and let $a_1, \ldots, a_r \geq 0$ and $b_1, \ldots, b_r \geq 0$ be integers. Then
>
> $$
> \dim\operatorname{Hom}_G\Big(\bigoplus_{i=1}^r S_i^{\oplus a_i},\ \bigoplus_{j=1}^r S_j^{\oplus b_j}\Big) = \sum_{i=1}^r a_ib_i.
> $$
>
> *Source: WS 17.5; lecture 11/16*

^cor-70-9

> [!proof]+ Proof
> *(Lecture 11/16.)* This is WS 17.3 (Proposition [[§70 Schur's Lemma and Multiplicities#^prop-70-7|§70.7]]), in which every weight $\dim\operatorname{Hom}_G(S_i, S_i)$ equals $1$ by WS 17.4 (Proposition [[§70 Schur's Lemma and Multiplicities#^prop-70-8|§70.8]]).

^pf-70-9

*Uses:* [[§70 Schur's Lemma and Multiplicities#^prop-70-7|§70.7]], [[§70 Schur's Lemma and Multiplicities#^prop-70-8|§70.8]]

![[m493-70-2.svg]]

*(Not from lecture; figure added.)* Corollary [[§70 Schur's Lemma and Multiplicities#^cor-70-9|§70.9]] for three simple representations with multiplicities $a = (2, 1, 3)$ in the source and $b = (1, 2, 2)$ in the target. A homomorphism between the two direct sums is a “matrix” with one entry for each pair (copy in the source, copy in the target), by the second proof of Proposition [[§70 Schur's Lemma and Multiplicities#^prop-70-4|§70.4]](1) applied one summand at a time. An entry between copies of different $S_i$ is zero (Corollary [[§70 Schur's Lemma and Multiplicities#^cor-70-6|§70.6]]). An entry between two copies of the same $S_i$ is an element of $\operatorname{Hom}_G(S_i, S_i)$, which over $\mathbb{C}$ is one complex number times the identity (Proposition [[§70 Schur's Lemma and Multiplicities#^prop-70-8|§70.8]]). So the dimension is the number of cells in the coloured blocks, $2 \cdot 1 + 1 \cdot 2 + 3 \cdot 2 = 10$, the dot product of $a$ and $b$.

> [!remark] Remark: Over Other Fields the Weights Stay
> The proof of Proposition [[§70 Schur's Lemma and Multiplicities#^prop-70-8|§70.8]] needs an eigenvalue of $\alpha$ in the ground field. Over $\mathbb{R}$ a linear map need not have a real eigenvalue, and for a simple real representation $S$ the number $\dim\operatorname{Hom}_G(S, S)$ can be larger than $1$. The lecture of 11/18 gave an example, the rotation representation of $\mathbb{Z}/4\mathbb{Z}$ on $\mathbb{R}^2$, where the number is $2$ (Example [[§71 The Character Table#^ex-71-2|§71.2]]); the proofs are Problem 10.4 of Problem Set 10 (Example [[§71 The Character Table#^ex-71-3|§71.3]]). So over $\mathbb{R}$, and over a general field containing $\mathbb{Q}$, the weights $\dim\operatorname{Hom}_G(S_i, S_i)$ of Proposition [[§70 Schur's Lemma and Multiplicities#^prop-70-7|§70.7]] must be kept.
>
> *Source: lecture 11/16; lecture 11/18; PS 10.4*

^rem-70-1

*Source note.* Lecture 11/16: over $\mathbb{C}$ the weights need not be tracked; the example is from the lecture of 11/18 and PS 10.4.

## The Characters of $S_3$ and a Simplicity Test

> [!example] Example §70.1: The Character Table of $S_3$, Element by Element
> List all six elements of $S_3$ as columns, not one representative of each [[§33 Conjugacy Classes#^def-33-1|conjugacy class]] as in Example [[§67 Characters of Representations#^ex-67-1|§67.1]]. The rows are three representations over $\mathbb{R}$: the [[§61 Representations and Subrepresentations#^ex-61-1|trivial representation]] and the [[§66 Invariant Vectors#^ex-66-3|sign representation]], which are one-dimensional with every $g$ acting by the $1 \times 1$ matrix $[1]$, respectively $[\operatorname{sgn} g]$, and the two-dimensional representation $U = \{(x_1, x_2, x_3) : x_1 + x_2 + x_3 = 0\}$ with the character computed in Example [[§67 Characters of Representations#^ex-67-1|§67.1]].
>
> |  | $e$ | $(1\,2)$ | $(1\,3)$ | $(2\,3)$ | $(1\,2\,3)$ | $(1\,3\,2)$ |
> |---|---|---|---|---|---|---|
> | trivial | $1$ | $1$ | $1$ | $1$ | $1$ | $1$ |
> | sign | $1$ | $-1$ | $-1$ | $-1$ | $1$ | $1$ |
> | $U$ | $2$ | $0$ | $0$ | $0$ | $-1$ | $-1$ |
>
> 1. *The rows are orthogonal as vectors in $\mathbb{R}^6$* (observed in class): trivial $\cdot$ sign $= 1 - 1 - 1 - 1 + 1 + 1 = 0$,  trivial $\cdot\ U = 2 + 0 + 0 + 0 - 1 - 1 = 0$,  sign $\cdot\ U = 2 + 0 + 0 + 0 - 1 - 1 = 0$.
> 2. *They are not unit vectors.* Each row has dot product $6$ with itself: $1 + 1 + 1 + 1 + 1 + 1 = 6$ for the trivial and for the sign representation, and $4 + 0 + 0 + 0 + 1 + 1 = 6$ for $U$. So each row has length $\sqrt{6}$, and $6 = |S_3|$.
> 3. *What the dot products are.* On the board, each transposition is marked as its own inverse and the two $3$-cycles as inverse to each other. In $S_3$, and in every symmetric group, $g^{-1}$ has the same [[§33 Conjugacy Classes#^def-33-2|cycle type]] as $g$ and is therefore conjugate to $g$ (Theorem [[§33 Conjugacy Classes#^thm-33-3|§33.3]]), so $\chi(g^{-1}) = \chi(g)$ for every character (Proposition [[§67 Characters of Representations#^prop-67-1|§67.1]](2)), and there is no need to distinguish $\chi(g)$ from $\chi(g^{-1})$. Hence, by Theorem [[§68 Homomorphisms Between Representations#^thm-68-6|§68.6]], the dot product of the rows of $V$ and $W$ is
>
> $$
> \sum_{g \in S_3} \chi_V(g)\,\chi_W(g) = \sum_{g \in S_3} \chi_V(g^{-1})\,\chi_W(g) = 6\,\dim\operatorname{Hom}_{S_3}(V, W).
> $$
>
> 4. *Conclusion.* By (1), $\dim\operatorname{Hom}_{S_3}(V, W) = 0$ for two different rows. By (2), $\dim\operatorname{Hom}_{S_3}(V, V) = \frac{6}{6} = 1$ for each of the three rows. These are the diagonal and off-diagonal entries of the table in Example [[§68 Homomorphisms Between Representations#^ex-68-2|§68.2]].
>
> *Source: lecture 11/16*

^ex-70-1

For simple representations these two phenomena are general:

> [!theorem] Proposition §70.10: Character Sums for Simple Representations
> Let $G$ be a finite group, $k$ a field containing $\mathbb{Q}$, and $S$, $T$ finite-dimensional [[§65 Simple Representations#^def-65-1|simple]] representations of $G$ over $k$.
>
> 1. If $S \not\cong T$, then $\displaystyle\sum_{g \in G} \chi_S(g^{-1})\,\chi_T(g) = 0$.
> 2. $\displaystyle\sum_{g \in G} \chi_S(g^{-1})\,\chi_S(g) = |G| \cdot \dim\operatorname{Hom}_G(S, S)$. If $k = \mathbb{C}$, this is $|G|$.
>
> *Source: lecture 11/16*

^prop-70-10

> [!proof]+ Proof
> *(Lecture 11/16, as the explanation of the numbers $0$ and $6$ in Example [[§70 Schur's Lemma and Multiplicities#^ex-70-1|§70.1]].)* *(Lecture 11/16.)* Multiplying the formula of Theorem [[§68 Homomorphisms Between Representations#^thm-68-6|§68.6]] by $|G|$ gives $\sum_{g} \chi_V(g^{-1})\,\chi_W(g) = |G| \cdot \dim\operatorname{Hom}_G(V, W)$ for all $V$, $W$.
>
> **(1)** For $V = S$ and $W = T$ with $S \not\cong T$, $\operatorname{Hom}_G(S, T) = \{0\}$ (Corollary [[§70 Schur's Lemma and Multiplicities#^cor-70-6|§70.6]]).
>
> **(2)** Take $V = W = S$. Over $\mathbb{C}$, $\dim\operatorname{Hom}_G(S, S) = 1$ by Schur's Lemma over $\mathbb{C}$ (Proposition [[§70 Schur's Lemma and Multiplicities#^prop-70-8|§70.8]]).

^pf-70-10

*Uses:* [[§68 Homomorphisms Between Representations#^thm-68-6|§68.6]], [[§70 Schur's Lemma and Multiplicities#^cor-70-6|§70.6]], [[§70 Schur's Lemma and Multiplicities#^prop-70-8|§70.8]]

When every element of $G$ is conjugate to its inverse, as in a symmetric group, the sums in Proposition [[§70 Schur's Lemma and Multiplicities#^prop-70-10|§70.10]] are dot products of rows of the element-by-element table: different simple representations give orthogonal rows, and a simple representation with $\dim\operatorname{Hom}_G(S, S) = 1$ gives a row of squared length $|G|$.

In Example [[§70 Schur's Lemma and Multiplicities#^ex-70-1|§70.1]] the argument runs the other way. It was not yet checked in class that the three representations are simple; the computation gave $\dim\operatorname{Hom}_G(V, V) = 1$ for each of them, and this implies simplicity:

> [!theorem] Lemma §70.11: A Simplicity Test
> Let $G$ be a finite group, $k$ a field containing $\mathbb{Q}$, and $V$ a finite-dimensional representation of $G$ over $k$. If $\dim\operatorname{Hom}_G(V, V) = 1$, then $V$ is [[§65 Simple Representations#^def-65-1|simple]].
>
> *Source: board 11/16*

^lem-70-11

> [!proof]+ Proof
> *Idea:* write $V$ as a sum of simple representations with multiplicities $a_i$; then $\dim\operatorname{Hom}_G(V, V)$ is a sum of terms $a_i^2\dim\operatorname{Hom}_G(S_i, S_i) \geq 1$, and a sum of such terms equals $1$ only if there is one term, with $a_1 = 1$.
>
> *(Board 11/16.)* Since $k$ contains $\mathbb{Q}$, $|G| \neq 0$ in $k$. By Maschke's theorem, in the form of Corollary [[§70 Schur's Lemma and Multiplicities#^cor-70-3|§70.3]],
>
> $$
> V \cong E = S_1^{\oplus a_1} \oplus \cdots \oplus S_r^{\oplus a_r}
> $$
>
> with simple, pairwise non-isomorphic $S_1, \ldots, S_r$ and integers $a_i \geq 1$. Isomorphic representations have the same character (Lemma [[§67 Characters of Representations#^lem-67-3|§67.3]]), and the formula of Theorem [[§68 Homomorphisms Between Representations#^thm-68-6|§68.6]] involves only the characters, so $\dim\operatorname{Hom}_G(V, V) = \dim\operatorname{Hom}_G(E, E)$. By WS 17.3 (Proposition [[§70 Schur's Lemma and Multiplicities#^prop-70-7|§70.7]]) with $b_i = a_i$,
>
> $$
> 1 = \dim\operatorname{Hom}_G(V, V) = \sum_{i=1}^r a_i^2\,\dim\operatorname{Hom}_G(S_i, S_i).
> $$
>
> Each term is at least $1$: $a_i^2 \geq 1$ is the square of a positive integer, and $\dim\operatorname{Hom}_G(S_i, S_i) \geq 1$ because the identity $\mathrm{Id}_{S_i} \neq 0$ lies in $\operatorname{Hom}_G(S_i, S_i)$. The sum has at least one term, since an empty sum is $0 \neq 1$. A sum of $r \geq 1$ integers, each at least $1$, equals $1$ only if $r = 1$ and the single term is $1$. So $r = 1$ and $a_1^2\dim\operatorname{Hom}_G(S_1, S_1) = 1$, which forces $a_1 = 1$. Hence $V \cong S_1^{\oplus 1} = S_1$, and a representation isomorphic to a simple representation is simple (Lemma [[§61 Representations and Subrepresentations#^lem-61-5|§61.5]](4)).

^pf-70-11

*Uses:* [[§70 Schur's Lemma and Multiplicities#^cor-70-3|§70.3]], [[§67 Characters of Representations#^lem-67-3|§67.3]], [[§68 Homomorphisms Between Representations#^thm-68-6|§68.6]], [[§70 Schur's Lemma and Multiplicities#^prop-70-7|§70.7]], [[§61 Representations and Subrepresentations#^lem-61-5|§61.5]]

> [!theorem] Corollary §70.12: Simplicity over $\mathbb{C}$
> Let $G$ be a finite group and $V$ a finite-dimensional representation of $G$ over $\mathbb{C}$. Then $V$ is [[§65 Simple Representations#^def-65-1|simple]] if and only if $\dim\operatorname{Hom}_G(V, V) = 1$.
>
> *Source: not from class; WS 17.4; board 11/16*

^cor-70-12

> [!proof]+ Proof
> *(Not from class; the two directions are WS 17.4 and the lemma of the board 11/16.)* *(Not from class.)* If $V$ is simple, then $\dim\operatorname{Hom}_G(V, V) = 1$ by Schur's Lemma over $\mathbb{C}$ (Proposition [[§70 Schur's Lemma and Multiplicities#^prop-70-8|§70.8]]). The converse is Lemma [[§70 Schur's Lemma and Multiplicities#^lem-70-11|§70.11]] for $k = \mathbb{C}$.

^pf-70-12

*Uses:* [[§70 Schur's Lemma and Multiplicities#^prop-70-8|§70.8]], [[§70 Schur's Lemma and Multiplicities#^lem-70-11|§70.11]]

![[m493-70-3.svg]]

*(Not from lecture; figure added.)* The number $\dim\operatorname{Hom}_G(V, V)$ over $\mathbb{C}$ for $V \cong \bigoplus_i S_i^{\oplus a_i}$. By Corollary [[§70 Schur's Lemma and Multiplicities#^cor-70-9|§70.9]] with $b = a$ it is $\sum_i a_i^2$: the homomorphisms $V \to V$ form one $a_i \times a_i$ block of complex numbers for each $S_i$. The value $1$ occurs only for a single block of size $1$, that is, for a simple representation (Corollary [[§70 Schur's Lemma and Multiplicities#^cor-70-12|§70.12]]). The values $2$ and $3$ occur only for sums of two, respectively three, different simple representations. From $4$ on, the number alone does not determine the multiplicities. Over a general field containing $\mathbb{Q}$, each cell carries the weight $\dim\operatorname{Hom}_G(S_i, S_i) \geq 1$, and the value $1$ still occurs only for a simple representation (Lemma [[§70 Schur's Lemma and Multiplicities#^lem-70-11|§70.11]]).

> [!example] Example §70.2: The Three Representations of $S_3$ Are Simple
> By Example [[§70 Schur's Lemma and Multiplicities#^ex-70-1|§70.1]](4), each of the trivial representation, the sign representation and $U$ has $\dim\operatorname{Hom}_{S_3}(V, V) = 1$. By the simplicity test (Lemma [[§70 Schur's Lemma and Multiplicities#^lem-70-11|§70.11]], with $k = \mathbb{R}$) all three are simple.
>
> 1. They are pairwise non-isomorphic: for two different rows $\dim\operatorname{Hom}_{S_3}(V, W) = 0$, so the only homomorphism $V \to W$ is zero, and an isomorphism between nonzero representations is not zero. (Their characters are also different, and isomorphic representations have the same character, Lemma [[§67 Characters of Representations#^lem-67-3|§67.3]].)
> 2. For $U$ this is a second proof of Example [[§65 Simple Representations#^ex-65-1|§65.1]](2), where the simplicity of $U$ was shown directly: a rotation by $120^\circ$ has no real eigenvector.
> 3. The same computation applies over every field $k$ containing $\mathbb{Q}$, with $U$ the sum-zero plane in $k^3$: the three characters have the same integer values, since $k^3 = k(1,1,1) \oplus U$ whenever $3 \neq 0$ in $k$ (Proposition [[§61 Representations and Subrepresentations#^prop-61-3|§61.3]]).
>
> The lecture of 11/16 ended here. That these three are all the simple representations of $S_3$ follows from Worksheet 18 (Example [[§71 The Character Table#^ex-71-1|§71.1]]).
>
> *Source: lecture 11/16; parts (2) and (3) not from class*

^ex-70-2

> [!example] Example §70.3: The Permutation Representation of $S_3$ by Multiplicities
> The permutation representation $\mathbb{R}^3$ of $S_3$ is the internal direct sum $\mathbb{R}(1,1,1) \oplus U$ (Example [[§65 Simple Representations#^ex-65-1|§65.1]]), and $S_3$ acts trivially on $\mathbb{R}(1,1,1)$. So by Lemma [[§70 Schur's Lemma and Multiplicities#^lem-70-1|§70.1]]
>
> $$
> \mathbb{R}^3 \cong \mathrm{triv}^{\oplus 1} \oplus \mathrm{sign}^{\oplus 0} \oplus U^{\oplus 1},
> $$
>
> with multiplicities $a = (1, 0, 1)$ with respect to the three simple representations of Example [[§70 Schur's Lemma and Multiplicities#^ex-70-2|§70.2]], each of which has $\dim\operatorname{Hom}_{S_3}(S, S) = 1$. WS 17.3 (Proposition [[§70 Schur's Lemma and Multiplicities#^prop-70-7|§70.7]]) gives:
>
> 1. $\dim\operatorname{Hom}_{S_3}(\mathbb{R}^3, \mathbb{R}^3) = 1 \cdot 1 + 0 \cdot 0 + 1 \cdot 1 = 2$. This is not $1$, in accordance with $\mathbb{R}^3$ not being simple.
> 2. With $b = (1, 0, 0)$, $(0, 1, 0)$, $(0, 0, 1)$: $\dim\operatorname{Hom}_{S_3}(\mathbb{R}^3, \mathrm{triv}) = 1$, $\dim\operatorname{Hom}_{S_3}(\mathbb{R}^3, \mathrm{sign}) = 0$, $\dim\operatorname{Hom}_{S_3}(\mathbb{R}^3, U) = 1$. The dimension of the space of homomorphisms to a simple representation reads off its multiplicity.
> 3. These are the entries $1$, $0$, $1$, $2$ in the row of $\mathbb{R}^3$ in the table of Example [[§68 Homomorphisms Between Representations#^ex-68-2|§68.2]], which were computed there from the characters. As a check in the element-by-element table: the row of $\mathbb{R}^3$ is the sum of the rows of triv and $U$, namely $(3, 1, 1, 1, 0, 0)$, and its dot product with itself is $9 + 1 + 1 + 1 = 12 = 6 \cdot 2$.
>
> *Source: not from class*

^ex-70-3

## An Application: $\operatorname{Hom}(V, W)$ as a Representation of $G \times H$

*Source: Problem Set 10, Problem 10.3 (submitted); the action was announced in the lecture of Fri Nov 13.*

In this subsection $G$ and $H$ are finite groups, $V$ is a finite-dimensional representation of $G$ and $W$ a finite-dimensional representation of $H$, over the same field. As in the problem set, $X$ stands for $\operatorname{Hom}(V, W)$, the vector space of linear maps $V \to W$.

> [!definition] Definition §70.3: The Action of $G \times H$ on $\operatorname{Hom}(V, W)$
> Let $V$ be a representation of $G$ and $W$ a representation of $H$ over the same field. The **action of $G \times H$ on $\operatorname{Hom}(V, W)$**, for the direct product $G \times H$ (Definition [[§3 Basic Examples of Groups#^def-3-2|§3.2]]) and $X = \operatorname{Hom}(V, W)$, is
>
> $$
> (g, h) \ast \alpha = \rho_W(h) \circ \alpha \circ \rho_V(g^{-1}).
> $$
>
> *Source: PS 10.3; lecture 11/13 (announced)*

^def-70-3

For $H = G$, the elements $(g, g)$ act by $\rho_W(g) \circ \alpha \circ \rho_V(g^{-1})$, which is the action of $G$ on $\operatorname{Hom}(V, W)$ of Definition [[§68 Homomorphisms Between Representations#^def-68-1|§68.1]].

> [!theorem] Proposition §70.13: $\operatorname{Hom}(V, W)$ Is a Representation of $G \times H$
> The rule of Definition [[§70 Schur's Lemma and Multiplicities#^def-70-3|§70.3]] is an action of $G \times H$ on $X = \operatorname{Hom}(V, W)$ by linear maps. So $X$ is a representation of $G \times H$.
>
> *Source: PS 10.3(1)*

^prop-70-13

> [!proof]+ Proof
> *(Problem Set 10, Problem 10.3(1), as submitted.)* *Well-defined.* For $(g, h) \in G \times H$ and $\alpha \in X$, the map $(g, h) \ast \alpha = \rho_W(h) \circ \alpha \circ \rho_V(g^{-1})$ is a composition of linear maps $V \to V \to W \to W$, so it lies in $X$.
>
> *Linearity.* Since composition of linear maps is bilinear, for $\alpha, \beta \in X$ and a scalar $c$,
>
> $$
> (g, h) \ast (\alpha + c\beta) = \rho_W(h) \circ (\alpha + c\beta) \circ \rho_V(g^{-1}) = (g, h) \ast \alpha + c\,(g, h) \ast \beta .
> $$
>
> *Identity.* $(e, e) \ast \alpha = \rho_W(e) \circ \alpha \circ \rho_V(e) = \mathrm{id}_W \circ \alpha \circ \mathrm{id}_V = \alpha$.
>
> *Compatibility.* Let $(g_1, h_1), (g_2, h_2) \in G \times H$. The product in $G \times H$ is componentwise, $(g_1g_2)^{-1} = g_2^{-1}g_1^{-1}$, and $\rho_V$, $\rho_W$ are homomorphisms, so $\rho_V\big((g_1g_2)^{-1}\big) = \rho_V(g_2^{-1}) \circ \rho_V(g_1^{-1})$ and $\rho_W(h_1h_2) = \rho_W(h_1) \circ \rho_W(h_2)$. Hence, using associativity of composition,
>
> $$
> \begin{aligned}\big((g_1, h_1)(g_2, h_2)\big) \ast \alpha &= (g_1g_2, h_1h_2) \ast \alpha = \rho_W(h_1h_2) \circ \alpha \circ \rho_V\big((g_1g_2)^{-1}\big) \\
> &= \rho_W(h_1) \circ \big(\rho_W(h_2) \circ \alpha \circ \rho_V(g_2^{-1})\big) \circ \rho_V(g_1^{-1}) \\
> &= \rho_W(h_1) \circ \big((g_2, h_2) \ast \alpha\big) \circ \rho_V(g_1^{-1}) = (g_1, h_1) \ast \big((g_2, h_2) \ast \alpha\big) .\end{aligned}
> $$
>
> Therefore $\ast$ is a linear action of $G \times H$ on $X$, i.e. $X$ is a representation of $G \times H$.

^pf-70-13

> [!theorem] Proposition §70.14: The Character of $\operatorname{Hom}(V, W)$ as a Representation of $G \times H$
> Let $V$ and $W$ be finite-dimensional, and let $X = \operatorname{Hom}(V, W)$ with the action of Definition [[§70 Schur's Lemma and Multiplicities#^def-70-3|§70.3]]. Then for all $(g, h) \in G \times H$
>
> $$
> \chi_X(g, h) = \chi_V(g^{-1})\,\chi_W(h).
> $$
>
> *Source: PS 10.3(2)*

^prop-70-14

> [!proof]+ Proof
> *Idea:* in bases, $(g, h)$ acts on matrices by $Y \mapsto RYS$, whose trace is $\operatorname{Tr}(R)\operatorname{Tr}(S)$.
>
> *(Problem Set 10, Problem 10.3(2), as submitted.)* Let $m = \dim W$ and $n = \dim V$, and fix bases of $V$ and $W$. For a linear map $\beta$ between these spaces, write $[\beta]$ for its matrix in these bases. Then $\alpha \mapsto [\alpha]$ is a linear isomorphism from $X = \operatorname{Hom}(V, W)$ to the space of $m \times n$ matrices.
>
> Fix $(g, h) \in G \times H$. By definition, $\chi_X(g, h)$ is the trace of the linear operator
>
> $$
> \rho_X(g, h) \colon X \to X, \qquad \alpha \mapsto \rho_W(h) \circ \alpha \circ \rho_V(g^{-1}),
> $$
>
> on the $mn$-dimensional space $X$. Let $R = [\rho_W(h)]$, an $m \times m$ matrix, and $S = [\rho_V(g^{-1})]$, an $n \times n$ matrix. Since the matrix of a composition is the product of the matrices,
>
> $$
> \big[\rho_X(g, h)\alpha\big] = R\,[\alpha]\,S \qquad (\alpha \in X).
> $$
>
> Hence, under the isomorphism $\alpha \mapsto [\alpha]$, the operator $\rho_X(g, h)$ corresponds to $L \colon Y \mapsto RYS$ on $m \times n$ matrices, and the two have the same trace, since the trace of an operator does not depend on the basis. By the lemma on the trace of $Y \mapsto RYS$ (Lemma [[§68 Homomorphisms Between Representations#^lem-68-4|§68.4]], the computation of Worksheet 16.2), $\operatorname{Tr}(L) = \operatorname{Tr}(R)\operatorname{Tr}(S)$. Therefore
>
> $$
> \chi_X(g, h) = \operatorname{Tr}(L) = \operatorname{Tr}\big(\rho_W(h)\big)\operatorname{Tr}\big(\rho_V(g^{-1})\big) = \chi_V(g^{-1})\,\chi_W(h) .
> $$

^pf-70-14

*Uses:* [[§68 Homomorphisms Between Representations#^lem-68-4|§68.4]]

> [!theorem] Proposition §70.15: $\dim\operatorname{Hom}_{G \times H}(X, X)$ Is a Product
> Let the field contain $\mathbb{Q}$, and let $X = \operatorname{Hom}(V, W)$ with the action of Definition [[§70 Schur's Lemma and Multiplicities#^def-70-3|§70.3]]. Then
>
> $$
> \dim\operatorname{Hom}_{G \times H}(X, X) = \Big(\dim\operatorname{Hom}_G(V, V)\Big)\Big(\dim\operatorname{Hom}_H(W, W)\Big).
> $$
>
> *Source: PS 10.3(3)*

^prop-70-15

> [!proof]+ Proof
> *Idea:* the character of $X$ is a product of a function of $g$ and a function of $h$, so the sum over $G \times H$ in the dimension formula factors.
>
> *(Problem Set 10, Problem 10.3(3), as submitted.)* We use the dimension formula for spaces of homomorphisms (Worksheet 16, Theorem [[§68 Homomorphisms Between Representations#^thm-68-6|§68.6]]): for a finite group $K$ and finite-dimensional representations $Y, Z$ of $K$ over a field containing $\mathbb{Q}$,
>
> $$
> \dim \operatorname{Hom}_K(Y, Z) = \frac{1}{|K|}\sum_{k \in K} \chi_Y(k^{-1})\,\chi_Z(k) .
> $$
>
> **The group $G \times H$.** The group $G \times H$ is finite, of order $|G|\,|H|$, and $X$ is a finite-dimensional representation of it by (1). Hence
>
> $$
> \dim \operatorname{Hom}_{G \times H}(X, X) = \frac{1}{|G|\,|H|}\sum_{(g, h) \in G \times H} \chi_X\big((g, h)^{-1}\big)\,\chi_X(g, h) .
> $$
>
> **Separating the characters.** In $G \times H$, $(g, h)^{-1} = (g^{-1}, h^{-1})$, so by (2),
>
> $$
> \chi_X(g^{-1}, h^{-1}) = \chi_V(g)\,\chi_W(h^{-1}), \qquad \chi_X(g, h) = \chi_V(g^{-1})\,\chi_W(h) .
> $$
>
> Hence
>
> $$
> \chi_X\big((g, h)^{-1}\big)\,\chi_X(g, h) = \big(\chi_V(g^{-1})\,\chi_V(g)\big)\big(\chi_W(h^{-1})\,\chi_W(h)\big) .
> $$
>
> **Splitting the sum.** A finite sum over $G \times H$ of a product $a(g)\,b(h)$ factors as the product $\big(\sum_g a(g)\big)\big(\sum_h b(h)\big)$ of the two sums. Therefore
>
> $$
> \dim \operatorname{Hom}_{G \times H}(X, X) = \bigg(\frac{1}{|G|}\sum_{g \in G} \chi_V(g^{-1})\,\chi_V(g)\bigg)\bigg(\frac{1}{|H|}\sum_{h \in H} \chi_W(h^{-1})\,\chi_W(h)\bigg) .
> $$
>
> By the dimension formula applied to the group $G$ with $Y = Z = V$, and to the group $H$ with $Y = Z = W$, the two factors are $\dim \operatorname{Hom}_G(V, V)$ and $\dim \operatorname{Hom}_H(W, W)$, respectively. Hence
>
> $$
> \dim \operatorname{Hom}_{G \times H}(X, X) = \Big(\dim \operatorname{Hom}_G(V, V)\Big)\Big(\dim \operatorname{Hom}_H(W, W)\Big) .
> $$

^pf-70-15

*Uses:* [[§68 Homomorphisms Between Representations#^thm-68-6|§68.6]]

> [!theorem] Proposition §70.16: $\operatorname{Hom}(V, W)$ Is Simple over $\mathbb{C}$
> Let the field be $\mathbb{C}$, and let $V$ and $W$ be simple representations of $G$ and of $H$ (Definition [[§65 Simple Representations#^def-65-1|§65.1]]). Then $X = \operatorname{Hom}(V, W)$, with the action of Definition [[§70 Schur's Lemma and Multiplicities#^def-70-3|§70.3]], is a simple representation of $G \times H$.
>
> *Source: PS 10.3(4)*

^prop-70-16

> [!proof]+ Proof
> *Idea:* by Schur's Lemma over $\mathbb{C}$ and the product formula, $\dim\operatorname{Hom}_{G \times H}(X, X) = 1$; a proper nonzero subrepresentation would give a projection that commutes with the action and is not a multiple of the identity.
>
> *(Problem Set 10, Problem 10.3(4), as submitted; Schur's Lemma over $\mathbb{C}$ is Proposition [[§70 Schur's Lemma and Multiplicities#^prop-70-8|§70.8]], the product formula is Proposition [[§70 Schur's Lemma and Multiplicities#^prop-70-15|§70.15]], and Maschke's theorem is Theorem [[§62 Direct Sums and Maschke's Theorem#^thm-62-10|§62.10]].)* **The dimension of $\operatorname{Hom}_{G \times H}(X, X)$.** By Schur's Lemma over $\mathbb{C}$ (Worksheet 17.4), a simple finite-dimensional representation $S$ of a group $K$ over $\mathbb{C}$ satisfies $\operatorname{Hom}_K(S, S) = \mathbb{C}\,\mathrm{Id}_S$, so $\dim \operatorname{Hom}_K(S, S) = 1$. Applying this to $V$ over $G$ and to $W$ over $H$,
>
> $$
> \dim \operatorname{Hom}_G(V, V) = 1, \qquad \dim \operatorname{Hom}_H(W, W) = 1 .
> $$
>
> Since $\mathbb{C}$ contains $\mathbb{Q}$, (3) applies and gives
>
> $$
> \dim \operatorname{Hom}_{G \times H}(X, X) = 1 \cdot 1 = 1 .
> $$
>
> **$X$ is simple.** First, $X \neq 0$, since otherwise $\operatorname{Hom}_{G \times H}(X, X) = 0$ would have dimension $0$. Suppose, for contradiction, that $X$ is not simple, and let $U \subseteq X$ be a subrepresentation with $U \neq 0$ and $U \neq X$.
>
> The group $G \times H$ is finite and $|G \times H| \neq 0$ in $\mathbb{C}$, so by Maschke's theorem there is a subrepresentation $U' \subseteq X$ with $X = U \oplus U'$. Here $U' \neq 0$, since $U \neq X$.
>
> Let $P \colon X \to X$ be the projection onto $U$ along $U'$: for $x = u + u'$ with $u \in U$ and $u' \in U'$, $P(x) = u$. It is linear.
>
> *$P$ is a homomorphism of representations.* Let $(g, h) \in G \times H$ and $x = u + u'$ as above. Since $U$ and $U'$ are subrepresentations, $(g, h) \ast u \in U$ and $(g, h) \ast u' \in U'$, so $(g, h) \ast x = (g, h) \ast u + (g, h) \ast u'$ is the decomposition of $(g, h) \ast x$ in $X = U \oplus U'$. Hence
>
> $$
> P\big((g, h) \ast x\big) = (g, h) \ast u = (g, h) \ast P(x) ,
> $$
>
> and $P \in \operatorname{Hom}_{G \times H}(X, X)$.
>
> *$P$ is not a multiple of $\mathrm{Id}_X$.* Suppose $P = c\,\mathrm{Id}_X$ for some $c \in \mathbb{C}$. Choose $u \in U$ and $u' \in U'$, both nonzero. Then $u = P(u) = c\,u$ gives $c = 1$, and $0 = P(u') = c\,u'$ gives $c = 0$, a contradiction.
>
> *Conclusion.* The identity $\mathrm{Id}_X$ is a nonzero element of $\operatorname{Hom}_{G \times H}(X, X)$, and $P$ is an element of the same space that is not a multiple of it. Hence $\mathrm{Id}_X$ and $P$ are linearly independent, and $\dim \operatorname{Hom}_{G \times H}(X, X) \geq 2$, contradicting $\dim \operatorname{Hom}_{G \times H}(X, X) = 1$. Therefore $X$ is a simple representation of $G \times H$.

^pf-70-16

*Uses:* [[§70 Schur's Lemma and Multiplicities#^prop-70-8|§70.8]], [[§70 Schur's Lemma and Multiplicities#^prop-70-15|§70.15]], [[§62 Direct Sums and Maschke's Theorem#^thm-62-10|§62.10]]

The second half of this proof is a second proof of the Simplicity Test (Lemma [[§70 Schur's Lemma and Multiplicities#^lem-70-11|§70.11]]), which does not use multiplicities: if a representation $X$ is not simple and not zero, Maschke's theorem gives $X = U \oplus U'$ with both summands nonzero, and the projection onto $U$ along $U'$ is a homomorphism of representations that is not a multiple of the identity, so $\dim\operatorname{Hom}(X, X)$ over the group is at least $2$.
