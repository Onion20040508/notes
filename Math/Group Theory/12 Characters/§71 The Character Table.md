---
type: section
subject: "[[Group Theory]]"
chapter: 12
section: 71
tags: [group-theory, math493]
---
← [[§70 Schur's Lemma and Multiplicities]] · ↑ [[· 12 Characters]] · [[§72 Representations of Cyclic Groups]] →

*Source: Lecture and Worksheet 18, *The character table* (Wed Nov 18): WS 18.1–18.4, from handwritten notes of the board; Problem Set 10, Problem 10.4 (submitted).*

Throughout this section $G$ is a finite group, $k$ is a field containing $\mathbb{Q}$, and all representations are finite-dimensional representations of $G$ over $k$. The first two problems of Worksheet 18 are results that are already proved, and each of them shortens the character table.

1. *WS 18.1: conjugate elements have the same character value.* If $g_1$ and $g_2$ are conjugate in $G$, then $\chi_V(g_1) = \chi_V(g_2)$ for every representation $V$. This is Characters Are Class Functions (Proposition [[§67 Characters of Representations#^prop-67-1|§67.1]](2)). So a character table lists each conjugacy class once. Fix representatives $g_1, g_2, \ldots, g_c$, one in each conjugacy class of $G$, and write $\operatorname{Conj}(g_i)$ for the conjugacy class of $g_i$ (Definition [[§33 Conjugacy Classes#^def-33-1|§33.1]]).
2. *WS 18.2: characters add over direct sums.* $\chi_{U \oplus V} = \chi_U + \chi_V$ (Proposition [[§67 Characters of Representations#^prop-67-2|§67.2]] for an internal direct sum, Proposition [[§70 Schur's Lemma and Multiplicities#^prop-70-2|§70.2]] for an external one). On the board: in a basis of $U$ followed by a basis of $V$,

$$
\rho_{U \oplus V}(g) = \begin{pmatrix} \rho_U(g) & 0 \\ 0 & \rho_V(g) \end{pmatrix}.
$$

Every representation is isomorphic to a direct sum $\bigoplus_j S_j^{\oplus a_j}$ of simple representations (Corollary [[§70 Schur's Lemma and Multiplicities#^cor-70-3|§70.3]]), and isomorphic representations have the same character (Lemma [[§67 Characters of Representations#^lem-67-3|§67.3]]). So every character is a sum $\sum_j a_j\chi_{S_j}$ of characters of simple representations, and a character table lists only the simple representations, each isomorphism class once.

The result is the character table of Definition [[§67 Characters of Representations#^def-67-2|§67.2]]: one column for each conjugacy class and one row for each isomorphism class of simple representations.

![[m493-71-1.svg]]

*(Board 11/18.)* The shape of a character table.

Worksheet 18 prints the character table of $S_3$ as an example. It consists of the first three rows of the table in Example [[§67 Characters of Representations#^ex-67-1|§67.1]]; the worksheet writes $W$ for the representation $\{(x_1, x_2, x_3) : x_1 + x_2 + x_3 = 0\}$, which these notes call $U$.

## Class Functions and Their Pairing

> [!definition] Definition §71.1: Class Function
> Let $G$ be a group and $k$ a field. A function $\alpha: G \to k$ is a **class function** if it is constant on every [[§33 Conjugacy Classes#^def-33-1|conjugacy class]]:
>
> $$
> \alpha(hgh^{-1}) = \alpha(g) \qquad \text{for all } g, h \in G.
> $$
>
> The class functions form a vector space over $k$ with pointwise addition and scalar multiplication, written $\operatorname{Cl}(G)$.
>
> *Source: board 11/18*

^def-71-1

*Source note.* Board 11/18, as the space $X$ of functions from the set of conjugacy classes of $G$ to $k$.

A class function is the same thing as a function on the set of conjugacy classes: its value on a class is its common value on the elements of the class. This is how the board describes the space. By WS 18.1 (Proposition [[§67 Characters of Representations#^prop-67-1|§67.1]](2)), the [[§67 Characters of Representations#^def-67-1|character]] $\chi_V$ of every representation is a class function.

**Transcription note (board 11/18).** The board calls the space of class functions $X$. These notes write $\operatorname{Cl}(G)$, because $X$ already denotes a matrix or a linear map in [[§68 Homomorphisms Between Representations|§68]].

> [!theorem] Proposition §71.1: The Dimension of the Space of Class Functions
> Let $G$ be a finite group with [[§33 Conjugacy Classes#^def-33-1|conjugacy classes]] $\operatorname{Conj}(g_1), \ldots, \operatorname{Conj}(g_c)$. For $1 \leq i \leq c$ let $\delta_i: G \to k$ be the function with $\delta_i(g) = 1$ for $g \in \operatorname{Conj}(g_i)$ and $\delta_i(g) = 0$ otherwise. Then $\delta_1, \ldots, \delta_c$ is a basis of $\operatorname{Cl}(G)$ (Definition [[§71 The Character Table#^def-71-1|§71.1]]). In particular
>
> $$
> \dim\operatorname{Cl}(G) = c,
> $$
>
> the number of conjugacy classes of $G$.
>
> *Source: board 11/18*

^prop-71-1

> [!proof]+ Proof
> *(Board 11/18 (stated: the dimension is the number of conjugacy classes); the proof is not from class.)* *(Not from class; filled in.)* The conjugacy classes are the orbits of $G$ acting on itself by conjugation, so every element of $G$ lies in exactly one of them (Orbits Partition $X$, Proposition [[§27 Orbits#^prop-27-1|§27.1]]).
>
> *Each $\delta_i$ is a class function.* $hgh^{-1}$ lies in the same conjugacy class as $g$, so $\delta_i(hgh^{-1}) = \delta_i(g)$.
>
> *Spanning.* Let $\alpha \in \operatorname{Cl}(G)$. Then $\alpha = \sum_{i=1}^c \alpha(g_i)\,\delta_i$: at an element $g \in \operatorname{Conj}(g_j)$ the right side is $\alpha(g_j)$, and $\alpha(g) = \alpha(g_j)$ because $\alpha$ is constant on $\operatorname{Conj}(g_j)$.
>
> *Independence.* If $\sum_i c_i\delta_i = 0$, then evaluating at $g_j$ gives $c_j = 0$.

^pf-71-1

*Uses:* [[§27 Orbits#^prop-27-1|§27.1]]

> [!theorem] Lemma §71.2: Sums of Class Functions over $G$
> Let $G$ be a finite group with representatives $g_1, \ldots, g_c$ of its conjugacy classes.
>
> 1. If $f: G \to k$ is a [[§71 The Character Table#^def-71-1|class function]], then $\displaystyle\sum_{g \in G} f(g) = \sum_{i=1}^c |\operatorname{Conj}(g_i)|\,f(g_i)$.
> 2. If $\alpha$ and $\beta$ are class functions, then so is $g \mapsto \alpha(g^{-1})\,\beta(g)$.
>
> *Source: board 11/18; WS 18.3*

^lem-71-2

> [!proof]+ Proof
> *(Used on the board 11/18 in WS 18.3; the proof is not from class.)* *(Not from class; filled in.)* **(1)** $G$ is the disjoint union of the classes $\operatorname{Conj}(g_i)$ (Proposition [[§27 Orbits#^prop-27-1|§27.1]]), and $f$ takes the value $f(g_i)$ at each of the $|\operatorname{Conj}(g_i)|$ elements of $\operatorname{Conj}(g_i)$.
>
> **(2)** Since $(hgh^{-1})^{-1} = hg^{-1}h^{-1}$,
>
> $$
> \alpha\big((hgh^{-1})^{-1}\big)\,\beta(hgh^{-1}) = \alpha(hg^{-1}h^{-1})\,\beta(hgh^{-1}) = \alpha(g^{-1})\,\beta(g).
> $$

^pf-71-2

*Uses:* [[§27 Orbits#^prop-27-1|§27.1]]

> [!definition] Definition §71.2: The Pairing of Class Functions
> Let $G$ be a finite group and $k$ a field in which $|G| \neq 0$. The **pairing of class functions** $\alpha, \beta \in \operatorname{Cl}(G)$ (Definition [[§71 The Character Table#^def-71-1|§71.1]]) is
>
> $$
> \langle \alpha, \beta \rangle = \frac{1}{|G|}\sum_{i=1}^c |\operatorname{Conj}(g_i)|\,\alpha(g_i^{-1})\,\beta(g_i) \in k.
> $$
>
> *Source: board 11/18*

^def-71-2

By Lemma [[§71 The Character Table#^lem-71-2|§71.2]], applied to the class function $g \mapsto \alpha(g^{-1})\beta(g)$,

$$
\langle \alpha, \beta \rangle = \frac{1}{|G|}\sum_{g \in G} \alpha(g^{-1})\,\beta(g).
$$

So the pairing does not depend on the choice of the representatives $g_i$. Worksheet 18 calls it “the correct inner product” for the rows of the character table. It is the expression $B(\alpha, \beta)$ from the proof of Proposition [[§70 Schur's Lemma and Multiplicities#^prop-70-4|§70.4]], for class functions.

> [!theorem] Proposition §71.3: The Pairing Is Bilinear and Symmetric
> Let $G$ be a finite group and $k$ a field in which $|G| \neq 0$. For class functions $\alpha, \alpha', \beta \in \operatorname{Cl}(G)$ (Definition [[§71 The Character Table#^def-71-1|§71.1]]), the pairing of Definition [[§71 The Character Table#^def-71-2|§71.2]], and $c, c' \in k$:
>
> 1. $\langle c\alpha + c'\alpha', \beta \rangle = c\,\langle \alpha, \beta \rangle + c'\,\langle \alpha', \beta \rangle$ and $\langle \beta, c\alpha + c'\alpha' \rangle = c\,\langle \beta, \alpha \rangle + c'\,\langle \beta, \alpha' \rangle$;
> 2. $\langle \alpha, \beta \rangle = \langle \beta, \alpha \rangle$.
>
> *Source: board 11/18*

^prop-71-3

> [!proof]+ Proof
> *(Board 11/18 (the symmetry, as a claim); part (1) is not from class.)* **(1)** *(Not from class; filled in.)* Each term $\alpha(g^{-1})\beta(g)$ of the sum is a product of one value of the first function and one value of the second.
>
> **(2)** *(Board 11/18.)* Inversion $g \mapsto g^{-1}$ is a bijection of $G$. Substituting $h = g^{-1}$,
>
> $$
> \langle \alpha, \beta \rangle = \frac{1}{|G|}\sum_{g \in G} \alpha(g^{-1})\,\beta(g) = \frac{1}{|G|}\sum_{h \in G} \alpha(h)\,\beta(h^{-1}) = \langle \beta, \alpha \rangle.
> $$

^pf-71-3

> [!theorem] Corollary §71.4: The Dimension Formula as a Pairing
> Let $G$ be a finite group, $k$ a field containing $\mathbb{Q}$, and $V$, $W$ finite-dimensional representations of $G$ over $k$, with characters $\chi_V$, $\chi_W$ (Definition [[§67 Characters of Representations#^def-67-1|§67.1]]). Then
>
> $$
> \dim\operatorname{Hom}_G(V, W) = \langle \chi_V, \chi_W \rangle = \frac{1}{|G|}\sum_{i=1}^c |\operatorname{Conj}(g_i)|\,\chi_V(g_i^{-1})\,\chi_W(g_i),
> $$
>
> with the pairing of Definition [[§71 The Character Table#^def-71-2|§71.2]].
>
> *Source: board 11/18, the first step of WS 18.3*

^cor-71-4

> [!proof]+ Proof
> *(Board 11/18.)* By Theorem [[§68 Homomorphisms Between Representations#^thm-68-6|§68.6]], $\dim\operatorname{Hom}_G(V, W) = \frac{1}{|G|}\sum_{g \in G} \chi_V(g^{-1})\chi_W(g)$. The characters are class functions (Proposition [[§67 Characters of Representations#^prop-67-1|§67.1]](2)), so this sum over $G$ is the sum over the conjugacy classes in Definition [[§71 The Character Table#^def-71-2|§71.2]] (Lemma [[§71 The Character Table#^lem-71-2|§71.2]]).

^pf-71-4

*Uses:* [[§68 Homomorphisms Between Representations#^thm-68-6|§68.6]], [[§67 Characters of Representations#^prop-67-1|§67.1]], [[§71 The Character Table#^def-71-2|Def. §71.2]], [[§71 The Character Table#^lem-71-2|§71.2]]

![[m493-71-2.svg]]

*(Not from lecture; figure added.)* Lemma [[§71 The Character Table#^lem-71-2|§71.2]] for $S_3$ and the character of $U$. The six elements fall into three conjugacy classes of sizes $1$, $3$, $2$, and a class function has one value on each class. So a sum over the six elements is a sum over the three classes with the class sizes as weights. The second row gives $\langle \chi_U, \chi_U \rangle = \frac{6}{6} = 1 = \dim\operatorname{Hom}_{S_3}(U, U)$ (Corollary [[§71 The Character Table#^cor-71-4|§71.4]]).

> [!remark] Remark: In What Sense the Pairing Is an Inner Product
> The pairing is bilinear and symmetric (Proposition [[§71 The Character Table#^prop-71-3|§71.3]]). Over a general field there is no notion of positivity, so it is not an inner product in the sense of Definition [[§63 Invariant Inner Products and Maschke over ℝ#^def-63-1|§63.1]]. For characters over $\mathbb{R}$ and $\mathbb{C}$ it becomes a familiar expression:
>
> 1. Over $\mathbb{R}$, $\chi_V(g^{-1}) = \chi_V(g)$ (Proposition [[§68 Homomorphisms Between Representations#^prop-68-8|§68.8]]), so $\langle \chi_V, \chi_W \rangle = \frac{1}{|G|}\sum_i |\operatorname{Conj}(g_i)|\,\chi_V(g_i)\,\chi_W(g_i)$: the dot product of the two rows, with each column weighted by the size of its conjugacy class, divided by $|G|$. For $S_3$ the weights $1$, $3$, $2$ give the dot products of the element-by-element table of Example [[§70 Schur's Lemma and Multiplicities#^ex-70-1|§70.1]], divided by $6$.
> 2. Over $\mathbb{C}$, $\chi_V(g^{-1}) = \overline{\chi_V(g)}$ (Corollary [[§68 Homomorphisms Between Representations#^cor-68-10|§68.10]]), so $\langle \chi_V, \chi_W \rangle = \frac{1}{|G|}\sum_i |\operatorname{Conj}(g_i)|\,\overline{\chi_V(g_i)}\,\chi_W(g_i)$. On characters this agrees with a Hermitian form (Definition [[§64 Sesquilinear and Hermitian Forms#^def-64-2|§64.2]]), although the pairing itself is bilinear, with $g^{-1}$ in place of a complex conjugation.
>
> *Source: not from class*

^rem-71-1

## The Rows Are Orthogonal

The next result restates Character Sums for Simple Representations (Proposition [[§70 Schur's Lemma and Multiplicities#^prop-70-10|§70.10]]) with the sum taken over the conjugacy classes.

> [!theorem] Proposition §71.5: The Rows of the Character Table Are Orthogonal
> Let $G$ be a finite group, $k$ a field containing $\mathbb{Q}$, and $U$, $V$ finite-dimensional simple representations of $G$ over $k$ (Definition [[§65 Simple Representations#^def-65-1|§65.1]]).
>
> 1. For the pairing of Definition [[§71 The Character Table#^def-71-2|§71.2]],
>
> $$
> \langle \chi_U, \chi_V \rangle = \frac{1}{|G|}\sum_{i=1}^c |\operatorname{Conj}(g_i)|\,\chi_U(g_i^{-1})\,\chi_V(g_i) = \begin{cases} \dim\operatorname{Hom}_G(U, U) & \text{if } U \cong V, \\ 0 & \text{if } U \not\cong V. \end{cases}
> $$
>
> 2. If $k = \mathbb{C}$, then
>
> $$
> \langle \chi_U, \chi_V \rangle = \begin{cases} 1 & \text{if } U \cong V, \\ 0 & \text{if } U \not\cong V. \end{cases}
> $$
>
> *Source: WS 18.3; board 11/18*

^prop-71-5

> [!proof]+ Proof
> *(Board 11/18.)* By Corollary [[§71 The Character Table#^cor-71-4|§71.4]], $\langle \chi_U, \chi_V \rangle = \dim\operatorname{Hom}_G(U, V)$.
>
> **(1)** If $U \not\cong V$, then $\operatorname{Hom}_G(U, V) = \{0\}$ (Corollary [[§70 Schur's Lemma and Multiplicities#^cor-70-6|§70.6]]). If $U \cong V$, then $\chi_V = \chi_U$ (Lemma [[§67 Characters of Representations#^lem-67-3|§67.3]]), so $\langle \chi_U, \chi_V \rangle = \langle \chi_U, \chi_U \rangle = \dim\operatorname{Hom}_G(U, U)$.
>
> **(2)** Over $\mathbb{C}$, $\dim\operatorname{Hom}_G(U, U) = 1$ by Schur's Lemma over $\mathbb{C}$ (Proposition [[§70 Schur's Lemma and Multiplicities#^prop-70-8|§70.8]]).

^pf-71-5

*Uses:* [[§71 The Character Table#^cor-71-4|§71.4]], [[§70 Schur's Lemma and Multiplicities#^cor-70-6|§70.6]], [[§67 Characters of Representations#^lem-67-3|§67.3]], [[§70 Schur's Lemma and Multiplicities#^prop-70-8|§70.8]]

In the words of the worksheet: the rows of the character table are orthogonal with the correct inner product. Over $\mathbb{C}$ they are orthonormal.

**Transcription note (WS 18.3).** The worksheet says “irreducible representations”. Under the hypotheses of this section, irreducible and simple mean the same (Proposition [[§65 Simple Representations#^prop-65-1|§65.1]]), and these notes say simple.

## Linear Independence and the Number of Simple Representations

Orthogonality limits, for the first time, the number of simple representations of $G$.

> [!theorem] Proposition §71.6: Characters of Non-Isomorphic Simple Representations Are Linearly Independent
> Let $G$ be a finite group and $k$ a field containing $\mathbb{Q}$. Let $S_1, \ldots, S_r$ be finite-dimensional simple representations of $G$ over $k$ (Definition [[§65 Simple Representations#^def-65-1|§65.1]]) with $S_i \not\cong S_j$ for $i \neq j$, and let $\chi_{S_j}$ be their characters (Definition [[§67 Characters of Representations#^def-67-1|§67.1]]). If $a_1, \ldots, a_r \in k$ satisfy
>
> $$
> \sum_{j=1}^r a_j\,\chi_{S_j} = 0,
> $$
>
> then $a_1 = a_2 = \cdots = a_r = 0$. In other words, the rows of the [[§67 Characters of Representations#^def-67-2|character table]] are linearly independent.
>
> *Source: WS 18.4(1); board 11/18*

^prop-71-6

> [!proof]+ Proof
> *Idea:* pair the relation with $\chi_{S_i}$; by orthogonality only the term with $j = i$ remains.
>
> *(Board 11/18.)* The characters $\chi_{S_j}$ lie in the space $\operatorname{Cl}(G)$ of class functions, which carries the pairing $\langle \cdot, \cdot \rangle$ (Definition [[§71 The Character Table#^def-71-2|§71.2]]). Fix $i$. Pairing both sides of $\sum_j a_j\chi_{S_j} = 0$ with $\chi_{S_i}$ and using bilinearity (Proposition [[§71 The Character Table#^prop-71-3|§71.3]](1)) and orthogonality (WS 18.3, Proposition [[§71 The Character Table#^prop-71-5|§71.5]](1)),
>
> $$
> 0 = \Big\langle \sum_{j=1}^r a_j\chi_{S_j},\ \chi_{S_i} \Big\rangle = \sum_{j=1}^r a_j\,\langle \chi_{S_j}, \chi_{S_i} \rangle = a_i \cdot \dim\operatorname{Hom}_G(S_i, S_i).
> $$
>
> The number $\dim\operatorname{Hom}_G(S_i, S_i)$ is a positive integer, since $\mathrm{Id}_{S_i} \neq 0$ lies in $\operatorname{Hom}_G(S_i, S_i)$, and a positive integer is not zero in $k$ because $k$ contains $\mathbb{Q}$. So $a_i = 0$.

^pf-71-6

*Uses:* [[§71 The Character Table#^def-71-2|Def. §71.2]], [[§71 The Character Table#^prop-71-3|§71.3]], [[§71 The Character Table#^prop-71-5|§71.5]]

**Transcription note (board 11/18, WS 18.4).** The board writes the last step as $\langle \sum_j a_j\chi_{S_j}, \chi_{S_i} \rangle = a_i = 0$, which is the case $\dim\operatorname{Hom}_G(S_i, S_i) = 1$, for instance $k = \mathbb{C}$; in general the factor $\dim\operatorname{Hom}_G(S_i, S_i)$ appears, and it is not zero. Worksheet 18.4 says “nonisomorphic representations” in (1) and (2); simple representations are meant, as in the sentence before the problem. Without simplicity (1) is false: for $S_3$ the representations $\mathrm{triv}$, $U$ and $\mathbb{R}^3$ are pairwise non-isomorphic, and $\chi_{\mathbb{R}^3} - \chi_{\mathrm{triv}} - \chi_U = 0$ (Example [[§67 Characters of Representations#^ex-67-1|§67.1]]).

> [!theorem] Corollary §71.7: At Most as Many Simple Representations as Conjugacy Classes
> Let $G$ be a finite group with $c$ [[§33 Conjugacy Classes#^def-33-1|conjugacy classes]] and $k$ a field containing $\mathbb{Q}$. If $S_1, \ldots, S_r$ are finite-dimensional [[§65 Simple Representations#^def-65-1|simple]] representations of $G$ over $k$ with $S_i \not\cong S_j$ for $i \neq j$, then
>
> $$
> r \leq c.
> $$
>
> So, up to isomorphism, $G$ has at most $c$ finite-dimensional simple representations over $k$.
>
> *Source: WS 18.4(2); board 11/18*

^cor-71-7

> [!proof]+ Proof
> *(Board 11/18.)* The characters $\chi_{S_1}, \ldots, \chi_{S_r}$ are $r$ linearly independent vectors (WS 18.4(1), Proposition [[§71 The Character Table#^prop-71-6|§71.6]]) in the space $\operatorname{Cl}(G)$, whose dimension is $c$ (Proposition [[§71 The Character Table#^prop-71-1|§71.1]]). A linearly independent list in a vector space of dimension $c$ has at most $c$ elements ([[§4 Span and Linear Independence#^ladr-2-22|Axler 2.22]]).

^pf-71-7

*Uses:* [[§71 The Character Table#^prop-71-6|§71.6]], [[§71 The Character Table#^prop-71-1|§71.1]]

> [!remark]- Connections
> - Linear Algebra: a linearly independent list is at most as long as a spanning list, [[§4 Span and Linear Independence#^ladr-2-22|LADR 2.22]].

![[m493-71-3.svg]]

*(Not from lecture; figure added.)* Corollary [[§71 The Character Table#^cor-71-7|§71.7]] for $S_3$ over $\mathbb{R}$. A class function $\alpha$ on $S_3$ has three values, and in the coordinates $y_i = \sqrt{|\operatorname{Conj}(g_i)|/6}\,\alpha(g_i)$ the pairing of two characters is the ordinary dot product in $\mathbb{R}^3$ (the remark [[§71 The Character Table#^rem-71-1|In What Sense the Pairing Is an Inner Product]], part (1)). The three characters $\chi_{\mathrm{triv}}$, $\chi_{\mathrm{sign}}$, $\chi_U$ become three perpendicular unit vectors. Three perpendicular nonzero vectors in $\mathbb{R}^3$ are linearly independent, and a fourth vector perpendicular to all three would be zero. So there is no fourth simple representation.

> [!example] Example §71.1: $S_3$ Has Exactly Three Simple Representations
> $S_3$ has $c = 3$ conjugacy classes, the [[§33 Conjugacy Classes#^def-33-2|cycle types]] (Theorem [[§33 Conjugacy Classes#^thm-33-3|§33.3]]). The [[§61 Representations and Subrepresentations#^ex-61-1|trivial representation]], the [[§66 Invariant Vectors#^ex-66-3|sign representation]] and $U$ are three pairwise non-isomorphic [[§65 Simple Representations#^def-65-1|simple]] representations, over every field $k$ containing $\mathbb{Q}$ (Example [[§70 Schur's Lemma and Multiplicities#^ex-70-2|§70.2]]). By WS 18.4(2) (Corollary [[§71 The Character Table#^cor-71-7|§71.7]]) there cannot be a fourth. This settles the question left open in Example [[§70 Schur's Lemma and Multiplicities#^ex-70-2|§70.2]].
>
> 1. *Every simple representation of $S_3$ over $k$ is isomorphic to exactly one of $\mathrm{triv}$, $\mathrm{sign}$, $U$.* Otherwise it would be a fourth simple representation, not isomorphic to these three.
> 2. *Every finite-dimensional representation $V$ of $S_3$ over $k$ is isomorphic to $\mathrm{triv}^{\oplus a} \oplus \mathrm{sign}^{\oplus b} \oplus U^{\oplus m}$* for integers $a, b, m \geq 0$, by Corollary [[§70 Schur's Lemma and Multiplicities#^cor-70-3|§70.3]] and (1). Then $\chi_V = a\,\chi_{\mathrm{triv}} + b\,\chi_{\mathrm{sign}} + m\,\chi_U$ (Proposition [[§70 Schur's Lemma and Multiplicities#^prop-70-2|§70.2]]). Each of the three has $\langle \chi_S, \chi_S \rangle = 1$ (Example [[§70 Schur's Lemma and Multiplicities#^ex-70-1|§70.1]]), so by orthogonality (Proposition [[§71 The Character Table#^prop-71-5|§71.5]])
>
> $$
> a = \langle \chi_V, \chi_{\mathrm{triv}} \rangle, \qquad b = \langle \chi_V, \chi_{\mathrm{sign}} \rangle, \qquad m = \langle \chi_V, \chi_U \rangle.
> $$
>
> 3. *A decomposition found from the character alone.* Let $V = \operatorname{Hom}(U, U)$ (Definition [[§68 Homomorphisms Between Representations#^def-68-1|§68.1]]), of dimension $4$. Its character is $\chi_U(g^{-1})\chi_U(g)$ (Proposition [[§68 Homomorphisms Between Representations#^prop-68-5|§68.5]]), with the values $4$, $0$, $1$ on the classes of $e$, $(1\,2)$, $(1\,2\,3)$, of sizes $1$, $3$, $2$. Every element of $S_3$ is conjugate to its inverse, so $\chi(g_i^{-1}) = \chi(g_i)$ in the pairing, and
>
> $$
> \begin{aligned} a &= \tfrac16\big(1 \cdot 4 \cdot 1 + 3 \cdot 0 \cdot 1 + 2 \cdot 1 \cdot 1\big) = 1, \\ b &= \tfrac16\big(1 \cdot 4 \cdot 1 + 3 \cdot 0 \cdot (-1) + 2 \cdot 1 \cdot 1\big) = 1, \\ m &= \tfrac16\big(1 \cdot 4 \cdot 2 + 3 \cdot 0 \cdot 0 + 2 \cdot 1 \cdot (-1)\big) = 1, \end{aligned}
> $$
>
> each term being (class size) $\cdot$ (value of $\chi_V$) $\cdot$ (value of the character of the simple representation).
> So $\operatorname{Hom}(U, U) \cong \mathrm{triv} \oplus \mathrm{sign} \oplus U$, and the dimensions agree: $4 = 1 + 1 + 2$. The multiplicity $a = 1$ of the trivial representation is $\dim\operatorname{Hom}(U, U)^{S_3} = \dim\operatorname{Hom}_{S_3}(U, U)$.
>
> *Source: not from class*

^ex-71-1

## The Group $\mathbb{Z}/4\mathbb{Z}$ over $\mathbb{R}$ and over $\mathbb{C}$

> [!example] Example §71.2: $\mathbb{Z}/4\mathbb{Z}$ over $\mathbb{R}$ and over $\mathbb{C}$
> Let $G = \mathbb{Z}/4\mathbb{Z}$. It is abelian, so $hgh^{-1} = g$ and every conjugacy class has one element: there are $c = 4$ conjugacy classes, $\{0\}$, $\{1\}$, $\{2\}$, $\{3\}$. Let
>
> $$
> J = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}, \qquad J^2 = \begin{pmatrix} -1 & 0 \\ 0 & -1 \end{pmatrix}, \qquad J^4 = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix},
> $$
>
> the rotation of the plane by $90^\circ$. Since $J^4 = I$, the rule $\rho_R(k) = J^k$ is well defined for $k \in \mathbb{Z}/4\mathbb{Z}$ and makes $R = \mathbb{R}^2$ a representation of $G$ (the representation of Example [[§69 Dual Representations#^ex-69-3|§69.3]]). The board lists three representations over $\mathbb{R}$: the trivial one; the one-dimensional representation in which $k$ acts by $(-1)^k$; and $R$.
>
> |  | $0$ | $1$ | $2$ | $3$ |
> |---|---|---|---|---|
> | trivial | $1$ | $1$ | $1$ | $1$ |
> | $(-1)^k$ | $1$ | $-1$ | $1$ | $-1$ |
> | $J^k$ | $2$ | $0$ | $-2$ | $0$ |
>
> 1. *The last row.* $\chi_R(k) = \operatorname{Tr}J^k$, and $J^0 = I$, $J$, $J^2 = -I$, $J^3 = -J$ have the traces $2$, $0$, $-2$, $0$.
> 2. *$\dim\operatorname{Hom}_G(R, R) = 2$* (board). The inverses of $0, 1, 2, 3$ are $0, 3, 2, 1$, and $\chi_R(3) = \chi_R(1)$, so by Corollary [[§71 The Character Table#^cor-71-4|§71.4]]
>
> $$
> \dim\operatorname{Hom}_G(R, R) = \langle \chi_R, \chi_R \rangle = \tfrac14\big(2^2 + 0^2 + (-2)^2 + 0^2\big) = 2.
> $$
>
> 3. *Over $\mathbb{R}$* (board): $R$ is simple (PS 10.4(1), Example [[§71 The Character Table#^ex-71-3|§71.3]](1)), and the board announces for Friday that the three rows are the only simple representations of $\mathbb{Z}/4\mathbb{Z}$ over $\mathbb{R}$; a proof is Proposition [[§72 Representations of Cyclic Groups#^prop-72-10|§72.10]]. So in WS 18.3(1) (Proposition [[§71 The Character Table#^prop-71-5|§71.5]](1)) the value for $U = V = R$ is $\dim\operatorname{Hom}_G(R, R) = 2$, not $1$: this is the example announced in the remark [[§70 Schur's Lemma and Multiplicities#^rem-70-1|Over Other Fields the Weights Stay]] in [[§70 Schur's Lemma and Multiplicities|§70]]. There are then three simple representations and four conjugacy classes, so the inequality of WS 18.4(2) (Corollary [[§71 The Character Table#^cor-71-7|§71.7]]) can be strict.
> 4. *Over $\mathbb{C}$* (board): the same three rules define representations over $\mathbb{C}$, with the same table. There are more representations than these, and $J^k$ acting on $\mathbb{C}^2$ is not simple; this is homework (PS 10.4(3), Example [[§71 The Character Table#^ex-71-3|§71.3]](3)). The complete table over $\mathbb{C}$, with four rows, is in Example [[§72 Representations of Cyclic Groups#^ex-72-1|§72.1]] (lecture 11/20).
> 5. *The rows are orthogonal* (check, not from class): $\langle \chi_{\mathrm{triv}}, \chi_{(-1)^k} \rangle = \frac14(1 - 1 + 1 - 1) = 0$,  $\langle \chi_{\mathrm{triv}}, \chi_R \rangle = \frac14(2 + 0 - 2 + 0) = 0$,  $\langle \chi_{(-1)^k}, \chi_R \rangle = \frac14(2 - 0 - 2 - 0) = 0$, and $\langle \chi_{\mathrm{triv}}, \chi_{\mathrm{triv}} \rangle = \langle \chi_{(-1)^k}, \chi_{(-1)^k} \rangle = \frac14 \cdot 4 = 1$.
>
> The simplicity of $R$ over $\mathbb{R}$, a basis of $\operatorname{Hom}_G(R, R)$, and a subrepresentation of $\mathbb{C}^2$ are Problem 10.4 of Problem Set 10, worked out in Example [[§71 The Character Table#^ex-71-3|§71.3]].
>
> *Source: lecture 11/18; part (5) not from class*

^ex-71-2

![[m493-71-4.svg]]

*(Not from lecture; figure added.)* The representation $R$ of Example [[§71 The Character Table#^ex-71-2|§71.2]]: $k \in \mathbb{Z}/4\mathbb{Z}$ acts on the plane by $J^k$, the rotation by $k \cdot 90^\circ$. The picture shows the images of $e_1$. The trace of the rotation by an angle $\theta$ is $2\cos\theta$, which gives the row $2$, $0$, $-2$, $0$ of the table.

> [!example] Example §71.3: The Rotation Representation of $\mathbb{Z}/4\mathbb{Z}$, Worked Out
> Let $\mathbb{Z}/4\mathbb{Z}$ act on $\mathbb{R}^2$, and by the same formula on $\mathbb{C}^2$, by $\rho(k) = J^k$ with $J = \left(\begin{smallmatrix} 0 & -1 \\ 1 & 0 \end{smallmatrix}\right)$, as in Example [[§71 The Character Table#^ex-71-2|§71.2]].
>
> 1. $\mathbb{R}^2$ is a simple representation of $\mathbb{Z}/4\mathbb{Z}$.
> 2. $\operatorname{Hom}_{\mathbb{Z}/4\mathbb{Z}}(\mathbb{R}^2, \mathbb{R}^2) = \left\{ \left(\begin{smallmatrix} a & b \\ -b & a \end{smallmatrix}\right) : a, b \in \mathbb{R} \right\}$. It is $2$-dimensional, with basis $I$, $J$.
> 3. $\mathbb{C}^2$ is not simple: $L = \operatorname{span}_{\mathbb{C}}\left\{\left(\begin{smallmatrix} 1 \\ -i \end{smallmatrix}\right)\right\}$ is a subrepresentation with $L \neq \{0\}$ and $L \neq \mathbb{C}^2$.
> 4. $\mathbb{C}^2 = L \oplus L'$ with $L' = \operatorname{span}_{\mathbb{C}}\left\{\left(\begin{smallmatrix} 1 \\ i \end{smallmatrix}\right)\right\}$. On $L$ the element $k$ acts by the scalar $i^k$, and on $L'$ by $(-i)^k$.
>
> *Source: PS 10.4(1)–(3); lecture 11/20*

^ex-71-3

> [!proof]+ Proof
> *(PS 10.4(1)–(3); part (4) is from the lecture of 11/20 (Example [[§72 Representations of Cyclic Groups#^ex-72-2|§72.2]]).)* *(Problem Set 10, Problem 10.4, as submitted.)*
>
> **(1)** Write $J = \rho(1) = \left(\begin{smallmatrix} 0 & -1 \\ 1 & 0 \end{smallmatrix}\right)$, so that $J(a, b) = (-b, a)$.
>
> **Candidates for subrepresentations.** First, $\mathbb{R}^2 \neq 0$. A subspace of $\mathbb{R}^2$ other than $0$ and $\mathbb{R}^2$ has dimension $1$, so it is a line $L = \operatorname{span}\{(a, b)\}$ with $(a, b) \neq (0, 0)$.
>
> **A stable line gives a real eigenvector.** Suppose such an $L$ is a subrepresentation. A subrepresentation is stable under every $\rho(k)$, in particular under $\rho(1) = J$. Hence $J(a, b) \in L$, i.e. $J(a, b) = \lambda\,(a, b)$ for some $\lambda \in \mathbb{R}$. Since $(a, b) \neq (0, 0)$, $\lambda$ is a real eigenvalue of $J$.
>
> **$J$ has no real eigenvalue.** A number $\lambda \in \mathbb{R}$ is an eigenvalue of $J$ if and only if $\lambda I - J$ is not injective, if and only if $\det(\lambda I - J) = 0$. The characteristic polynomial is
>
> $$
> \det(zI - J) = \det\begin{pmatrix} z & 1 \\ -1 & z \end{pmatrix} = z^2 + 1 ,
> $$
>
> and for $z \in \mathbb{R}$, $z^2 + 1 \geq 1 > 0$. So $J$ has no real eigenvalue, contradicting the previous step.
>
> Therefore $\mathbb{R}^2$ has no subrepresentation other than $0$ and $\mathbb{R}^2$, and $\mathbb{R}^2$ is a simple representation of $\mathbb{Z}/4\mathbb{Z}$.
>
> **(2)** **The condition.** Here both representations are $\mathbb{R}^2$ with $\rho(k) = J^k$, with $J$ as in (1). By the definition of $\operatorname{Hom}_G(V, W)$ (Definition [[§68 Homomorphisms Between Representations#^def-68-2|§68.2]]), a linear map $\alpha \colon \mathbb{R}^2 \to \mathbb{R}^2$ lies in $\operatorname{Hom}_{\mathbb{Z}/4\mathbb{Z}}(\mathbb{R}^2, \mathbb{R}^2)$ if and only if
>
> $$
> \alpha\big(J^k v\big) = J^k\big(\alpha(v)\big) \qquad \text{for all } k \in \mathbb{Z}/4\mathbb{Z},\ v \in \mathbb{R}^2 ,
> $$
>
> i.e. $\alpha J^k = J^k \alpha$ for $k = 0, 1, 2, 3$.
>
> **The powers of $J$.** We have
>
> $$
> J^0 = I, \qquad J^1 = J = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}, \qquad J^2 = \begin{pmatrix} -1 & 0 \\ 0 & -1 \end{pmatrix} = -I, \qquad J^3 = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix} = -J .
> $$
>
> **Reducing to one condition.** For $k = 0, 2$, $\alpha(\pm I) = \pm\alpha = (\pm I)\alpha$ holds for every $\alpha$. For $k = 1, 3$, the condition $\alpha(-J) = (-J)\alpha$ is equivalent to $\alpha J = J\alpha$. Hence
>
> $$
> \alpha \in \operatorname{Hom}_{\mathbb{Z}/4\mathbb{Z}}(\mathbb{R}^2, \mathbb{R}^2) \iff \alpha J = J\alpha .
> $$
>
> **Solving the condition.** Write $\alpha = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$ with $a, b, c, d \in \mathbb{R}$. Then
>
> $$
> \alpha J = \begin{pmatrix} b & -a \\ d & -c \end{pmatrix}, \qquad J\alpha = \begin{pmatrix} -c & -d \\ a & b \end{pmatrix} .
> $$
>
> Comparing entries, $\alpha J = J\alpha$ if and only if $b = -c$, $-a = -d$, $d = a$ and $-c = b$, i.e. if and only if $a = d$ and $b = -c$. With $a$ and $b$ as free parameters,
>
> $$
> \operatorname{Hom}_{\mathbb{Z}/4\mathbb{Z}}(\mathbb{R}^2, \mathbb{R}^2) = \left\{ \begin{pmatrix} a & b \\ -b & a \end{pmatrix} : a, b \in \mathbb{R} \right\}, \qquad \begin{pmatrix} a & b \\ -b & a \end{pmatrix} = a\,I - b\,J .
> $$
>
> **A basis.** We claim $\{I, J\}$ is a basis of $\operatorname{Hom}_{\mathbb{Z}/4\mathbb{Z}}(\mathbb{R}^2, \mathbb{R}^2)$.
> - *Membership.* $I$ (with $a = 1$, $b = 0$) and $J$ (with $a = 0$, $b = -1$) are of the form above.
> - *Spanning.* Every element of $\operatorname{Hom}_{\mathbb{Z}/4\mathbb{Z}}(\mathbb{R}^2, \mathbb{R}^2)$ equals $a\,I - b\,J$ for some $a, b \in \mathbb{R}$.
> - *Independence.* If $s\,I + t\,J = \begin{pmatrix} s & -t \\ t & s \end{pmatrix} = 0$ with $s, t \in \mathbb{R}$, then $s = t = 0$.
>
> Therefore $\{I, J\}$ is a basis, and $\dim \operatorname{Hom}_{\mathbb{Z}/4\mathbb{Z}}(\mathbb{R}^2, \mathbb{R}^2) = 2$.
>
> **(3)** Now $\mathbb{Z}/4\mathbb{Z}$ acts on $\mathbb{C}^2$ by $\rho(k) = J^k$, with $J(a, b) = (-b, a)$ for $a, b \in \mathbb{C}$.
>
> **Eigenvalues of $J$.** Over $\mathbb{C}$, the characteristic polynomial factors as
>
> $$
> \det(zI - J) = z^2 + 1 = (z - i)(z + i),
> $$
>
> so $J$ has the eigenvalues $i$ and $-i$.
>
> **An eigenvector for $i$.** For $(a, b) \in \mathbb{C}^2$, $J(a, b) = i\,(a, b)$ means $(-b, a) = (ia, ib)$, i.e. $b = -ia$ and $a = ib$; the second equation follows from the first, since $ib = -i^2 a = a$. Taking $a = 1$,
>
> $$
> v = \begin{pmatrix} 1 \\ -i \end{pmatrix}, \qquad Jv = \begin{pmatrix} i \\ 1 \end{pmatrix} = i \begin{pmatrix} 1 \\ -i \end{pmatrix} = i\,v .
> $$
>
> **The subrepresentation.** Let $L = \operatorname{span}_{\mathbb{C}}\{v\}$. For every $k \in \mathbb{Z}/4\mathbb{Z}$, $\rho(k)v = J^k v = i^k v \in L$, so $\rho(k)(cv) = c\,i^k v \in L$ for all $c \in \mathbb{C}$. Hence $L$ is stable under every $\rho(k)$, and $L$ is a subrepresentation of $\mathbb{C}^2$.
>
> **Nontrivial and proper.** Since $v \neq 0$, $\dim_\mathbb{C} L = 1$, so $L \neq 0$ and $L \neq \mathbb{C}^2$. Therefore
>
> $$
> L = \operatorname{span}_{\mathbb{C}}\left\{ \begin{pmatrix} 1 \\ -i \end{pmatrix} \right\}
> $$
>
> is a nontrivial proper subrepresentation of $\mathbb{C}^2$, and $\mathbb{C}^2$ is not simple.
>
> **(4)** *(Lecture 11/20, Example [[§72 Representations of Cyclic Groups#^ex-72-2|§72.2]]; the details are filled in.)* With $J(a, b) = (-b, a)$, $J(1, i) = (-i, 1) = -i\,(1, i)$. So $v' = (1, i)$ is an eigenvector of $J$ for the eigenvalue $-i$, and $J^kv' = (-i)^kv'$: the line $L'$ is a subrepresentation on which $k$ acts by $(-i)^k$. By (3), $k$ acts on $L$ by $i^k$. The vectors $(1, -i)$ and $(1, i)$ are linearly independent, since $\det\left(\begin{smallmatrix} 1 & 1 \\ -i & i \end{smallmatrix}\right) = 2i \neq 0$, so they form a basis of $\mathbb{C}^2$ and $\mathbb{C}^2 = L \oplus L'$.

^pf-ex-71-3

*Uses:* [[§68 Homomorphisms Between Representations#^def-68-2|Def. §68.2]], [[§72 Representations of Cyclic Groups#^ex-72-2|Ex. §72.2]]

![[m493-71-5.svg]]

*(Not from lecture; figure added.)* Part (1) of Example [[§71 The Character Table#^ex-71-3|§71.3]] as a picture. $J$ turns the plane by $90^\circ$, so it maps every line through $0$ to the perpendicular line. No line is mapped to itself, which is the geometric content of “$J$ has no real eigenvalue”.

Example [[§71 The Character Table#^ex-71-3|§71.3]] fits the results of [[§70 Schur's Lemma and Multiplicities|§70]]. Over $\mathbb{R}$ the representation is simple with $\dim\operatorname{Hom} = 2$, so the conclusion of Schur's Lemma over $\mathbb{C}$ (Proposition [[§70 Schur's Lemma and Multiplicities#^prop-70-8|§70.8]]) fails over $\mathbb{R}$, and the converse of the Simplicity Test (Lemma [[§70 Schur's Lemma and Multiplicities#^lem-70-11|§70.11]]) fails over $\mathbb{R}$ as well. Over $\mathbb{C}$ the same matrices give a sum of two non-isomorphic one-dimensional representations, with characters $i^k$ and $(-i)^k$ whose sum is the row $2$, $0$, $-2$, $0$, and $\dim\operatorname{Hom} = 1^2 + 1^2 = 2$ (Corollary [[§70 Schur's Lemma and Multiplicities#^cor-70-9|§70.9]]). The homomorphisms $k \mapsto i^k$ and $k \mapsto (-i)^k$ are the further representations over $\mathbb{C}$ mentioned on the board; the lecture of 11/20 lists all four one-dimensional complex representations of $\mathbb{Z}/4\mathbb{Z}$ and shows that there are no other simple ones ([[§72 Representations of Cyclic Groups|§72]]). The problem set suggests, as an additional challenge, the same questions for $\mathbb{Z}/m\mathbb{Z}$ acting on $\mathbb{R}^2$ by rotations by $2\pi k/m$, $m \geq 3$; this is not worked out here.
