---
type: review
subject: "[[Group Theory]]"
tags: [group-theory, math493, review]
---
↑ [[Group Theory]] · [[Group Theory Midterm Review|Midterm Review]] · [[Group Theory HW Drill|Problem Set Drill]]

# Notes Drill: definitions, core proofs, worksheet problems

The companion of the [[Group Theory HW Drill|Problem Set Drill]] for everything in the notes that the problem sets do not cover:
- every definition, with the standard examples it is tested on;
- the core proofs: every worksheet problem, every result proved or stated in lecture, and the famous theorems;
- **results Speyer left as an exercise in class**, tagged **[class exercise, date]**.

Questions are ordered so that answering them in turn reproduces the definition or the proof:
- **[state]** and **[def]**: state exactly, with every hypothesis;
- **[why]**: what fails without a hypothesis.

The route of each proof in the notes is folded under **Hints**. Results that are problem-set problems point to the Problem Set Drill instead of repeating them.

**Priorities.** Inside each topic, entries are grouped by where they come from. Work top-down and stop at Priority 2 if time is short.
1. **Problem sets**: the entry is a problem-set problem or extends one.
2. **Worksheets and lectures**: a worksheet problem, or stated or done in lecture, or left there as an exercise.
3. **Problem-set technique**: filled in by the notes, but its proof uses a strategy the problem sets drill often (G2, G3, G4, G6, G8, G10).
4. **Notes only**: Pinter, MATH 412 or "not from class" fill-ins; optional before the midterm.

Entries: 51 problem sets, 182 worksheets and lectures, 10 problem-set technique, 60 notes only.

# T1. Groups and subgroups

## Definitions T1

### Priority 1 · problem sets (directly or extended)

#### Direct product · P1

$G \times H$ is the set of pairs with $(g_1, h_1)(g_2, h_2) = (g_1g_2, h_1h_2)$, identity $(e_G, e_H)$ and inverse $(g^{-1}, h^{-1})$, see Definition [[§3 Basic Examples of Groups#^def-3-2|§3.2]]. *Source: WS 1 (examples); [[Group Theory HW Drill#^ps1-4|PS1.4]].*

^nd-def-3-2

- [ ] Q1 **[def]** State the operation, identity and inverse of $G \times H$.
- [ ] Q2 **[example]** Name the elements of $\mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/2\mathbb{Z}$ and their orders. Is it cyclic?
- [ ] Q3 **[use]** When is $G \times H$ abelian?
- [ ] Q4 **[why]** Why is $\mathbb{Z}/4\mathbb{Z} \not\cong \mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/2\mathbb{Z}$, although both have four elements?

> [!tip]- Hints: where it lives, examples
> - Definition [[§3 Basic Examples of Groups#^def-3-2|§3.2]]; the group axioms and the universal property: Proposition [[§18 Conjugation, Products, and Pointwise Products#^prop-18-3|§18.3]] ([[Group Theory HW Drill#^ps1-4|PS1.4]]).
> - $\mathbb{Z}/4\mathbb{Z}$ vs Klein four: Proposition [[§16 Isomorphisms#^prop-16-3|§16.3]](2); $U_8 \cong \mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/2\mathbb{Z}$, Proposition [[§16 Isomorphisms#^prop-16-8|§16.8]].

### Priority 2 · worksheets and lectures

#### Group · P2

A group is a set $G$ with a binary operation $\ast : G \times G \to G$ having an identity $e$, inverses $g^{-1}$ with $gg^{-1} = g^{-1}g = e$, and associativity, see Definition [[§1 The Definition of a Group#^def-1-1|§1.1]]. *Source: WS 1 (definition at the top).*

^nd-def-1-1

- [ ] Q1 **[def]** State the three axioms in the worksheet's order. Which object does axiom (2) refer to, and why must axiom (1) come first?
- [ ] Q2 **[example]** Which of $(\mathbb{N}, +)$, $(\mathbb{Z}, \times)$, $(\mathbb{R}_{\geq 0}, \times)$, $(\mathbb{R}_{>0}, \times)$, $(\mathbb{Z}/n\mathbb{Z} \setminus \{[0]\}, \times)$ are groups? Which axiom fails each time?
- [ ] Q3 **[why]** Closure is not listed as an axiom. Where is it hidden in the definition?
- [ ] Q4 **[use]** In the table of groups and non-groups, which axiom is usually the one to check, and why is associativity almost never the issue?

> [!tip]- Hints: where it lives, examples
> - Definition [[§1 The Definition of a Group#^def-1-1|§1.1]]; notation (which symbol for $\ast$, $e$ vs $1$) in remark [[§1 The Definition of a Group#^rem-1-1|Notation]].
> - Example [[§3 Basic Examples of Groups#^ex-3-1|§3.1]] (groups and non-groups); $\mathbb{Z}/n\mathbb{Z} \setminus \{[0]\}$ is a group iff $n$ is prime.
> - Closure is the phrase "binary operation $G \times G \to G$".

#### Abelian group · P2

$G$ is abelian (commutative) if $ab = ba$ for all $a, b \in G$; commutativity is not a group axiom, see Definition [[§1 The Definition of a Group#^def-1-2|§1.2]]. *Source: WS 3 (restated); notes.*

^nd-def-1-2

- [ ] Q1 **[def]** State the definition, and the convention about writing $+$ and $0$.
- [ ] Q2 **[example]** Name two families of non-abelian groups, with the smallest index at which they become non-abelian, and give an explicit pair of non-commuting elements in each.
- [ ] Q3 **[use]** Which three maps $G \to G$ or $G \times G \to G$ are homomorphisms exactly when $G$ is abelian?
- [ ] Q4 **[why]** Why does the mixed hypothesis $gh_1 = h_2g$ give $h_1 = h_2$ in an abelian group but not in $S_3$?

> [!tip]- Hints: where it lives, examples
> - Definition [[§1 The Definition of a Group#^def-1-2|§1.2]]; commuting pairs, Definition [[§16 Isomorphisms#^def-16-2|§16.2]]; the $+$ convention, remark [[§1 The Definition of a Group#^rem-1-1|Notation]].
> - Non-abelian: $S_n$ ($n \geq 3$), with $(1\,2)(2\,3) \neq (2\,3)(1\,2)$; $GL_n(k)$ ($n \geq 2$), with two elementary matrices, verification after Definition [[§3 Basic Examples of Groups#^def-3-6|§3.6]].
> - Characterizations: Proposition [[§18 Conjugation, Products, and Pointwise Products#^prop-18-4|§18.4]], Proposition [[§18 Conjugation, Products, and Pointwise Products#^prop-18-5|§18.5]]; mixed hypothesis: Proposition [[§2 First Consequences of the Axioms#^prop-2-1|§2.1]].

#### The additive groups ℤ, ℚ, ℝ · P2

Each of $\mathbb{Z}$, $\mathbb{Q}$, $\mathbb{R}$ is an abelian group under $+$, with identity $0$ and inverse $-a$; none is a group under multiplication, see Definition [[§3 Basic Examples of Groups#^def-3-1|§3.1]]. *Source: WS 1 (examples).*

^nd-def-3-1

- [ ] Q1 **[def]** State the identity and inverse in $(\mathbb{Z}, +)$ and say where associativity comes from.
- [ ] Q2 **[why]** Why is $(\mathbb{Q}, \times)$ not a group, and why is $(\mathbb{Z} \setminus \{0\}, \times)$ still not a group?
- [ ] Q3 **[example]** Is $1$ of finite order in $(\mathbb{Z}, +)$? Which subgroup does it generate?
- [ ] Q4 **[use]** What are all the subgroups of $(\mathbb{Z}, +)$? Give three different kinds of subgroups of $(\mathbb{R}, +)$.

> [!tip]- Hints: where it lives, examples
> - Definition [[§3 Basic Examples of Groups#^def-3-1|§3.1]]; $1$ has infinite order, remark [[§4 Subgroups#^rem-4-4|Where Finiteness Enters]].
> - Subgroups of $\mathbb{Z}$: Proposition [[§5 A Zoo of Subgroups#^prop-5-1|§5.1]]; of $\mathbb{R}$: Example [[§5 A Zoo of Subgroups#^ex-5-2|§5.2]] and Proposition [[§5 A Zoo of Subgroups#^prop-5-3|§5.3]].

#### Field (provisional) · P2

A field is a set $k$ with $+$ and $\cdot$ such that $(k, +)$ and $(k \setminus \{0\}, \cdot)$ are abelian groups and $\cdot$ distributes over $+$, see Definition [[§3 Basic Examples of Groups#^def-3-3|§3.3]]. *Source: WS 1 (examples); notes.*

^nd-def-3-3

- [ ] Q1 **[def]** State the three conditions.
- [ ] Q2 **[example]** Give three fields and one commutative ring that is not a field.
- [ ] Q3 **[use]** Prove from the axioms that $a \cdot 0 = 0$ and that $ab = 0$ forces $a = 0$ or $b = 0$.
- [ ] Q4 **[why]** For which $n$ is $\mathbb{Z}/n\mathbb{Z}$ a field? Which nonzero class has no inverse in $\mathbb{Z}/6\mathbb{Z}$?

> [!tip]- Hints: where it lives, examples
> - Definition [[§3 Basic Examples of Groups#^def-3-3|§3.3]]; Proposition [[§3 Basic Examples of Groups#^prop-3-1|§3.1]] ($a \cdot 0 = a(0+0)$, cancel in $(k, +)$).
> - Proposition [[§8 Invertibility and Unit Groups#^prop-8-4|§8.4]]: $\mathbb{Z}/n\mathbb{Z}$ is a field iff $n$ is prime; in $\mathbb{Z}/6\mathbb{Z}$, $[2][3] = [0]$.

#### Multiplicative group of a field · P2

$k^\times = (k \setminus \{0\}, \cdot)$ is a group by condition (2) of the field definition, see Definition [[§3 Basic Examples of Groups#^def-3-4|§3.4]]. *Source: WS 1 (examples).*

^nd-def-3-4

- [ ] Q1 **[def]** Define $k^\times$. Which field axiom makes it a group?
- [ ] Q2 **[example]** What is $\mathbb{F}_p^\times$ as a set, and what is its other name?
- [ ] Q3 **[use]** To what product is $\mathbb{R}^\times$ isomorphic, and through which map?
- [ ] Q4 **[why]** Why is $(\mathbb{R}, \times)$ not a group, while $(\mathbb{R}_{>0}, \times)$ is?

> [!tip]- Hints: where it lives, examples
> - Definition [[§3 Basic Examples of Groups#^def-3-4|§3.4]]; $\mathbb{F}_p^\times = U_p$, Proposition [[§8 Invertibility and Unit Groups#^prop-8-4|§8.4]].
> - $\mathbb{R}^\times \cong \mathbb{R}_{>0} \times \mathbb{Z}/2\mathbb{Z}$ by $x \mapsto (|x|, \text{sign})$, Proposition [[§16 Isomorphisms#^prop-16-9|§16.9]] (WS 2.8).

#### Symmetric groups · P2

$S_X$ is the group of bijections $X \to X$ under composition, right factor applied first; $S_n = S_{\{1, \ldots, n\}}$ has $n!$ elements and is non-abelian for $n \geq 3$, see Definition [[§3 Basic Examples of Groups#^def-3-5|§3.5]]. *Source: WS 1, WS 2 (examples).*

^nd-def-3-5

- [ ] Q1 **[def]** Define $S_X$ and the product $\sigma\tau$. Which factor is applied first?
- [ ] Q2 **[use]** Why is a composite of bijections a bijection? Which worksheet identity gives the inverse of $\sigma\tau$?
- [ ] Q3 **[use]** Why does $S_n$ have $n!$ elements?
- [ ] Q4 **[example]** Compute $(1\,2)(2\,3)$ and $(2\,3)(1\,2)$. What does this show?
- [ ] Q5 **[why]** Why is $S_2$ abelian? Why does every bijection of a finite set have finite order, while the shift $n \mapsto n+1$ in $S_{\mathbb{Z}}$ does not?

> [!tip]- Hints: where it lives, examples
> - Definition [[§3 Basic Examples of Groups#^def-3-5|§3.5]] and its verification (closure by $\tau^{-1}\sigma^{-1}$, as in WS 1.4).
> - $(1\,2)(2\,3) = (1\,2\,3)$, $(2\,3)(1\,2) = (1\,3\,2)$: Example [[§10 Cycle Notation and the Group S₃#^ex-10-1|§10.1]]; convention, remark [[§10 Cycle Notation and the Group S₃#^rem-10-1|Convention Warning]].
> - Infinite sets: remark [[§12 Multiplying and Conjugating Cycles#^rem-12-2|Finite Sets Only]].

#### General linear group · P2

$GL_n(k)$ is the group of invertible $n \times n$ matrices over a field $k$ under matrix multiplication; it is non-abelian for $n \geq 2$, see Definition [[§3 Basic Examples of Groups#^def-3-6|§3.6]]. *Source: WS 1 (examples).*

^nd-def-3-6

- [ ] Q1 **[def]** Define $GL_n(k)$; give its identity and inverses.
- [ ] Q2 **[use]** Prove closure in two ways (two-sided inverse; determinant).
- [ ] Q3 **[use]** Give two reasons why matrix multiplication is associative.
- [ ] Q4 **[example]** Give two elements of $GL_2(k)$ that do not commute. Do they still fail to commute over $\mathbb{F}_2$?
- [ ] Q5 **[why]** Name four subgroups of $GL_2(\mathbb{R})$ that are copies of groups met elsewhere.

> [!tip]- Hints: where it lives, examples
> - Definition [[§3 Basic Examples of Groups#^def-3-6|§3.6]] with its verification; closure by $(AB)(B^{-1}A^{-1}) = I_n$.
> - $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$, $\begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix}$.
> - Copies: scalars ($\mathbb{R}^\times$), $\begin{pmatrix} 1 & t \\ 0 & 1 \end{pmatrix}$ ($(\mathbb{R}, +)$), $SO(2)$ (rotations), permutation matrices ($S_2$): Example [[§5 A Zoo of Subgroups#^ex-5-4|§5.4]].

#### Special linear group · P2

$SL_n(k) = \{A \in GL_n(k) : \det A = 1\}$, see Definition [[§3 Basic Examples of Groups#^def-3-7|§3.7]]. *Source: notes; WS 1.7.*

^nd-def-3-7

- [ ] Q1 **[def]** Define $SL_n(k)$.
- [ ] Q2 **[use]** Check the three subgroup conditions using $\det$.
- [ ] Q3 **[use]** Of which homomorphism is $SL_n(\mathbb{R})$ the kernel? What is the image?
- [ ] Q4 **[why]** Is $\{A : \det A = 2\}$ a subgroup? Which condition fails first?

> [!tip]- Hints: where it lives, examples
> - Definition [[§3 Basic Examples of Groups#^def-3-7|§3.7]]; verification in Example [[§5 A Zoo of Subgroups#^ex-5-4|§5.4]].
> - Kernel of $\det : GL_n(\mathbb{R}) \to \mathbb{R}^\times$, onto via $\operatorname{diag}(\lambda, 1, \ldots, 1)$: Example [[§15 Homomorphisms#^ex-15-1|§15.1]](1).

#### Orthogonal group · P2

$O(n) = \{A \in GL_n(\mathbb{R}) : A^{\mathsf{T}}A = I_n\}$, see Definition [[§3 Basic Examples of Groups#^def-3-8|§3.8]]. *Source: notes; WS 1.7.*

^nd-def-3-8

- [ ] Q1 **[def]** Define $O(n)$.
- [ ] Q2 **[use]** Prove closure under products and under inverses.
- [ ] Q3 **[example]** Why is every permutation matrix in $O(n)$?
- [ ] Q4 **[why]** What are the possible determinants of $A \in O(n)$, and why?

> [!tip]- Hints: where it lives, examples
> - Definition [[§3 Basic Examples of Groups#^def-3-8|§3.8]]; verification in Example [[§5 A Zoo of Subgroups#^ex-5-4|§5.4]]: $(AB)^{\mathsf{T}}AB = B^{\mathsf{T}}B$, and $A^{-1} = A^{\mathsf{T}}$.
> - Permutation matrices: $M(\sigma)^{-1} = M(\sigma)^{\mathsf{T}}$, Proposition [[§20 Polynomial Rings, Permutation Matrices, and Representations#^prop-20-5|§20.5]].
> - $\det(A)^2 = \det(A^{\mathsf{T}}A) = 1$.

#### Special orthogonal group · P2

$SO(n) = O(n) \cap SL_n(\mathbb{R})$, see Definition [[§3 Basic Examples of Groups#^def-3-9|§3.9]]. *Source: notes; WS 1.7.*

^nd-def-3-9

- [ ] Q1 **[def]** Define $SO(n)$.
- [ ] Q2 **[use]** Why is it a subgroup without any new computation?
- [ ] Q3 **[example]** Describe $SO(2)$ explicitly; what is $R_\theta R_\varphi$?
- [ ] Q4 **[why]** Which cyclic groups sit inside $SO(2)$, and why does this show $GL_2(\mathbb{R})$ contains elements of every finite order?

> [!tip]- Hints: where it lives, examples
> - Definition [[§3 Basic Examples of Groups#^def-3-9|§3.9]]; intersections of subgroups, Proposition [[§4 Subgroups#^prop-4-3|§4.3]].
> - $R_\theta$ rotation matrices, $R_\theta R_\varphi = R_{\theta + \varphi}$; $\langle R_{2\pi/n} \rangle \cong C_n$: Example [[§5 A Zoo of Subgroups#^ex-5-4|§5.4]].

#### Subgroup · P2

$H \subseteq G$ is a subgroup if $e_G \in H$, $h \in H \Rightarrow h^{-1} \in H$, and $h_1, h_2 \in H \Rightarrow h_1h_2 \in H$, see Definition [[§4 Subgroups#^def-4-1|§4.1]]. *Source: WS 1.*

^nd-def-4-1

- [ ] Q1 **[def]** State the three conditions, then the one-step test.
- [ ] Q2 **[use]** If $H \subseteq G$ is closed under the operation and is a group in its own right, why is its identity $e_G$?
- [ ] Q3 **[example]** Is $2\mathbb{Z} \cup 3\mathbb{Z}$ a subgroup of $\mathbb{Z}$? Is $2\mathbb{Z} \cap 3\mathbb{Z}$?
- [ ] Q4 **[example]** Is $\{(x, y) \in \mathbb{Z}^2 : x \equiv y \pmod 2\}$ a subgroup? Is it of the form $m\mathbb{Z} \times n\mathbb{Z}$?
- [ ] Q5 **[why]** In the one-step test, why is "nonempty" needed?

> [!tip]- Hints: where it lives, examples
> - Definition [[§4 Subgroups#^def-4-1|§4.1]]; Proposition [[§4 Subgroups#^prop-4-1|§4.1]], Proposition [[§4 Subgroups#^prop-4-2|§4.2]], Proposition [[§4 Subgroups#^prop-4-3|§4.3]].
> - Union fails: $2 + 3 = 5$. Checkerboard: Example [[§5 A Zoo of Subgroups#^ex-5-1|§5.1]].
> - $\varnothing$ satisfies the one-step condition vacuously but contains no identity.

#### Integer powers · P2

$g^0 = e$, $g^n = g^{n-1}g$ for $n \geq 1$, and $g^{-n} = (g^{-1})^n$, see Definition [[§4 Subgroups#^def-4-2|§4.2]]. *Source: lecture 9/9.*

^nd-def-4-2

- [ ] Q1 **[def]** State the definition. Why is $g^n$ unambiguous?
- [ ] Q2 **[use]** State the three exponent laws.
- [ ] Q3 **[why]** Why does $(gh)^2 = g^2h^2$ fail in general? Give the $S_3$ example.
- [ ] Q4 **[example]** In additive notation, what is $g^n$? What does $g^{-n}$ become?

> [!tip]- Hints: where it lives, examples
> - Definition [[§4 Subgroups#^def-4-2|§4.2]]; generalized associativity, Proposition [[§1 The Definition of a Group#^prop-1-1|§1.1]]; Lemma [[§4 Subgroups#^lem-4-4|§4.4]].
> - Remark [[§4 Subgroups#^rem-4-1|Two Non-Laws]]: $g = (1\,2)$, $h = (2\,3)$, $(gh)^2 = (1\,3\,2) \neq e$.

#### Subgroup generated by an element · P2

$\langle g \rangle = \{g^k : k \in \mathbb{Z}\}$, see Definition [[§4 Subgroups#^def-4-3|§4.3]]. *Source: WS 1.*

^nd-def-4-3

- [ ] Q1 **[def]** Define $\langle g \rangle$.
- [ ] Q2 **[example]** List $\langle (1\,2\,3) \rangle$ in $S_3$, $\langle 2 \rangle$ in $U_7$, and $\langle 6 \rangle$ in $\mathbb{Z}$.
- [ ] Q3 **[use]** In which two senses is $\langle g \rangle$ the "smallest" subgroup containing $g$?
- [ ] Q4 **[why]** Why is $\langle g \rangle$ abelian even when $G$ is not?

> [!tip]- Hints: where it lives, examples
> - Definition [[§4 Subgroups#^def-4-3|§4.3]]; Proposition [[§4 Subgroups#^prop-4-5|§4.5]] (WS 1.5), Proposition [[§4 Subgroups#^prop-4-6|§4.6]].
> - $\langle 2 \rangle = \{1, 2, 4\}$ in $U_7$ (Example [[§15 Homomorphisms#^ex-15-2|§15.2]]).

#### Word in generators · P2

A word in $g_1, \ldots, g_k$ is a finite product $g_{m_1}^{n_1} \cdots g_{m_N}^{n_N}$ ($N \geq 0$, indices in any order with repeats, $n_i \in \mathbb{Z}$); the empty word is $e$, see Definition [[§4 Subgroups#^def-4-4|§4.4]]. *Source: WS 1.6.*

^nd-def-4-4

- [ ] Q1 **[def]** Define a word, including the empty word.
- [ ] Q2 **[example]** Write $(g_1g_2)^2$ and $g_2g_1$ as words. Why is $g_2g_1$ not of the form $g_1^{a}g_2^{b}$?
- [ ] Q3 **[use]** How are the inverse of a word and the product of two words again words?
- [ ] Q4 **[why]** In $S_3$, $(1\,2)(2\,3)(1\,2) = (1\,3)$. What does this say about reduced words?

> [!tip]- Hints: where it lives, examples
> - Definition [[§4 Subgroups#^def-4-4|§4.4]]; Example [[§4 Subgroups#^ex-4-1|§4.1]] (WS 1.6), where the inverse reverses order and negates exponents (WS 1.4).

#### Subgroup generated by several elements · P2

$\langle g_1, \ldots, g_k \rangle$ is the set of all words in $g_1, \ldots, g_k$ (equivalently, products of letters $g_i^{\pm 1}$), see Definition [[§4 Subgroups#^def-4-5|§4.5]]. *Source: WS 1.6.*

^nd-def-4-5

- [ ] Q1 **[def]** State the definition, and the variant with exponents in $\{-1, 1\}$.
- [ ] Q2 **[use]** State the top-down characterization.
- [ ] Q3 **[example]** What is $\langle a, b \rangle$ in $\mathbb{Z}$? What is $\langle (1\,2), (2\,3) \rangle$ in $S_3$?
- [ ] Q4 **[why]** Why does the fixed-order set $\{g_1^{n_1} \cdots g_k^{n_k}\}$ work in an abelian group but not in general?
- [ ] Q5 **[example]** Which generating sets of $S_n$ and $A_n$ appear in the notes?

> [!tip]- Hints: where it lives, examples
> - Definition [[§4 Subgroups#^def-4-5|§4.5]]; Proposition [[§4 Subgroups#^prop-4-7|§4.7]]; remark [[§4 Subgroups#^rem-4-2|Two Checks on the Definition]].
> - $\langle a, b \rangle = \gcd(a, b)\mathbb{Z}$: Corollary [[§5 A Zoo of Subgroups#^cor-5-2|§5.2]].
> - $S_n$: Theorem [[§21 The Sign Homomorphism and the Alternating Group#^thm-21-7|§21.7]]; $A_n$: Theorem [[§21 The Sign Homomorphism and the Alternating Group#^thm-21-9|§21.9]].

#### Order of a group · P2

The order $|G|$ of a group is its number of elements (possibly infinite), see Definition [[§4 Subgroups#^def-4-6|§4.6]]. *Source: WS 3; cf. MATH 412.*

^nd-def-4-6

- [ ] Q1 **[def]** Define $|G|$.
- [ ] Q2 **[example]** Give $|S_n|$, $|\mathbb{Z}/n\mathbb{Z}|$, $|U_n|$, $|A_n|$.
- [ ] Q3 **[use]** How is $|\langle g \rangle|$ related to $\operatorname{ord}(g)$?
- [ ] Q4 **[why]** Is $|G| = |H|$ enough for $G \cong H$? Give two groups of order $4$ and two of order $6$ that are not isomorphic.

> [!tip]- Hints: where it lives, examples
> - Definition [[§4 Subgroups#^def-4-6|§4.6]]; remark [[§4 Subgroups#^rem-4-5|Two Meanings of Order]].
> - $|U_n| = \varphi(n)$: Definition [[§8 Invertibility and Unit Groups#^def-8-3|§8.3]]; $|A_n| = n!/2$: Proposition [[§21 The Sign Homomorphism and the Alternating Group#^prop-21-5|§21.5]].
> - $\mathbb{Z}/4\mathbb{Z}$ vs $U_8$; $\mathbb{Z}/6\mathbb{Z}$ vs $S_3$: Proposition [[§16 Isomorphisms#^prop-16-3|§16.3]].

#### Order of an element · P2

$g$ has finite order if $g^N = e$ for some $N \geq 1$, and $\operatorname{ord}(g)$ is the least such $N$; otherwise $g$ has infinite order, see Definition [[§4 Subgroups#^def-4-7|§4.7]]. *Source: WS 3; cf. MATH 412.*

^nd-def-4-7

- [ ] Q1 **[def]** State the definition. Which element has order $1$?
- [ ] Q2 **[example]** Orders of $(1\,2\,3)$, of $(1\,5\,4)(3\,7\,6)$, of $(1\,2)(3\,4\,5)$, of $2$ in $U_7$, of $3$ in $U_7$, of $1$ in $\mathbb{Z}$.
- [ ] Q3 **[use]** If $g^m = e$, what can you say about $m$ relative to $\operatorname{ord}(g)$? Which theorem gives this?
- [ ] Q4 **[use]** What is $\operatorname{ord}(g^k)$ if $\operatorname{ord}(g) = n$?
- [ ] Q5 **[why]** Why must every element of a finite group have finite order? Where does the argument fail for $\mathbb{Z}$?

> [!tip]- Hints: where it lives, examples
> - Definition [[§4 Subgroups#^def-4-7|§4.7]]; Proposition [[§4 Subgroups#^prop-4-8|§4.8]] (pigeonhole).
> - Kernel of $k \mapsto g^k$ is $\operatorname{ord}(g)\mathbb{Z}$: Proposition [[§17 Cyclic Groups#^prop-17-3|§17.3]](2); $\operatorname{ord}(g^k) = n/\gcd(n, k)$: Proposition [[§17 Cyclic Groups#^prop-17-5|§17.5]].
> - Disjoint cycles: order is the lcm, Proposition [[§11 Disjoint Cycle Decomposition#^prop-11-4|§11.4]].

#### Cyclic group · P2

$G$ is cyclic if $G = \langle g \rangle$ for some $g$ (a generator); e.g. $\mathbb{Z}/n\mathbb{Z} = \langle [1] \rangle$ and $\mathbb{Z} = \langle 1 \rangle$, see Definition [[§4 Subgroups#^def-4-8|§4.8]]. *Source: WS 3; cf. MATH 412.*

^nd-def-4-8

- [ ] Q1 **[def]** Define cyclic and generator.
- [ ] Q2 **[use]** State the classification of cyclic groups.
- [ ] Q3 **[example]** Is $U_7$ cyclic? $U_8$? $U_{10}$? $U_{15}$? Give a generator when it exists.
- [ ] Q4 **[why]** Why is every cyclic group abelian? Is every abelian group cyclic?
- [ ] Q5 **[use]** How many generators does $\mathbb{Z}/12\mathbb{Z}$ have, and which?

> [!tip]- Hints: where it lives, examples
> - Definition [[§4 Subgroups#^def-4-8|§4.8]]; Theorem [[§17 Cyclic Groups#^thm-17-1|§17.1]], Corollary [[§17 Cyclic Groups#^cor-17-2|§17.2]], Corollary [[§17 Cyclic Groups#^cor-17-6|§17.6]].
> - $U_7 = \langle 3 \rangle$, $U_8$ not cyclic: Proposition [[§16 Isomorphisms#^prop-16-8|§16.8]]; $U_{10} = \langle 3 \rangle$, $U_{15}$ not cyclic: Example [[§22 The Structure of Uₙ#^ex-22-1|§22.1]].

## Proofs T1

### Priority 1 · problem sets (directly or extended)

#### Generated subgroups of ℤ and Bézout · P1

For $a, b$ not both $0$ with $d = \gcd(a, b)$: $\langle a, b \rangle = a\mathbb{Z} + b\mathbb{Z} = d\mathbb{Z}$; hence $ax + by = d$ is solvable, and $\langle a, b \rangle = \mathbb{Z}$ iff $\gcd(a, b) = 1$, see Corollary [[§5 A Zoo of Subgroups#^cor-5-2|§5.2]]. *Source: cf. Pinter Ch. 5, 22; assumed on PS 1.*

^nd-cor-5-2

- [ ] Q1 **[state]** State the corollary, including Bézout.
- [ ] Q2 Why is $\langle a, b \rangle = \{ax + by\}$ in additive notation?
- [ ] Q3 By the classification, $\langle a, b \rangle = e\mathbb{Z}$ with $e > 0$. Why is $e \leq d$?
- [ ] Q4 Why is $d \leq e$?
- [ ] Q5 **[why]** Trace the dependency chain from well-ordering to "$U_n$ is a group". Which results of Chapter 2 rest on Bézout?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G14 (Bézout from the classification of subgroups of $\mathbb{Z}$).
> - $a, b \in e\mathbb{Z}$ so $e$ is a common divisor; $e = ax + by$ so $d \mid e$.
> - Remark [[§5 A Zoo of Subgroups#^rem-5-1|The Dependency of U_n on Bézout]] and remark [[§9 Euclid's Lemma, Unique Factorization, and the Chinese Remainder Theorem#^rem-9-1|The Dependency Chain]].

### Priority 2 · worksheets and lectures

#### Generalized associativity · P2

All parenthesizations of $g_1 \cdots g_n$ give the same element, so parentheses may be dropped, see Proposition [[§1 The Definition of a Group#^prop-1-1|§1.1]]. *Source: notes (used implicitly from WS 1 on).*

^nd-prop-1-1

- [ ] Q1 **[state]** State the proposition. With which canonical product $L_n$ is every parenthesization compared?
- [ ] Q2 What is the outermost multiplication of a parenthesization, and what does the induction hypothesis say about its two factors?
- [ ] Q3 Case $j = n-1$: why is the product already $L_n$?
- [ ] Q4 Case $j < n-1$: write $B = B'g_n$ and use axiom (3) once. Why is $AB'$ equal to $L_{n-1}$?
- [ ] Q5 **[why]** Where is this used silently? (Think of $g^n$ and of words.)

> [!tip]- Hints: route of the proof in the notes
> - Strategy: strong induction on $n$ (no G-code; axiom manipulation).
> - Outermost product $A \cdot B$ with $A$ on $g_1 \cdots g_j$; induction makes $A = L_j$ and $B$ left-normed.
> - $A(B'g_n) = (AB')g_n = L_{n-1}g_n = L_n$.
> - Used in Definition [[§4 Subgroups#^def-4-2|§4.2]] and Definition [[§4 Subgroups#^def-4-4|§4.4]].

#### Cancellation and the mixed hypothesis · P2

If $gh_1 = gh_2$ (or $h_1g = h_2g$) then $h_1 = h_2$; if $gh_1 = h_2g$ then $h_2 = gh_1g^{-1}$, and $h_1 = h_2$ iff $g$ and $h_1$ commute, see Proposition [[§2 First Consequences of the Axioms#^prop-2-1|§2.1]]. *Source: WS 1.1.*

^nd-prop-2-1

- [ ] Q1 **[state]** State both parts, including the "iff" in part (2).
- [ ] Q2 Prove left cancellation, naming the axiom used at each of the three steps.
- [ ] Q3 For right cancellation, on which side do you multiply by $g^{-1}$?
- [ ] Q4 From $gh_1 = h_2g$, derive $h_2 = gh_1g^{-1}$. Then prove both directions of "$h_1 = h_2 \iff gh_1 = h_1g$".
- [ ] Q5 **[why]** Give the counterexample in $S_3$ with $gh_1 = h_2g$ but $h_1 \neq h_2$. How does "conjugation relabels a cycle" predict $h_2$ without multiplying?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: multiply both sides on the same side by $g^{-1}$; G6 (conjugation) for part (2).
> - $g^{-1}(gh_1) = (g^{-1}g)h_1 = eh_1 = h_1$.
> - Example [[§2 First Consequences of the Axioms#^ex-2-1|§2.1]]: $g = (1\,2)$, $h_1 = (2\,3)$, $h_2 = (1\,3)$; Example [[§13 The Symmetric Group S₃#^ex-13-1|§13.1]] via Proposition [[§12 Multiplying and Conjugating Cycles#^prop-12-1|§12.1]].

#### Uniqueness of the identity · P2

$G$ has exactly one element satisfying the identity axiom, see Proposition [[§2 First Consequences of the Axioms#^prop-2-2|§2.2]]. *Source: WS 1.2.*

^nd-prop-2-2

- [ ] Q1 **[state]** State the proposition.
- [ ] Q2 Suppose $e$ and $e'$ both satisfy axiom (1). Which single product do you evaluate in two ways?
- [ ] Q3 Which of $e$, $e'$ plays the role of "identity" and which of "$g$" in each evaluation?
- [ ] Q4 **[why]** Does the proof use inverses or associativity? Would it work in a monoid?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: evaluate one product two ways (uniqueness technique).
> - $e = e \ast e' = e'$: first because $e'$ is an identity, then because $e$ is.

#### Uniqueness of inverses · P2

Each $g$ has exactly one inverse, see Proposition [[§2 First Consequences of the Axioms#^prop-2-3|§2.3]]. *Source: WS 1.3.*

^nd-prop-2-3

- [ ] Q1 **[state]** State the proposition.
- [ ] Q2 Give the proof via left cancellation.
- [ ] Q3 Give the direct computation $h = he = \cdots = h'$ that avoids WS 1.1.
- [ ] Q4 **[why]** State the "uniqueness technique" this proposition licenses. Which later results are proved by it?
- [ ] Q5 **[why]** Where does the direct computation use associativity, and why does it need both $hg = e$ and $gh' = e$?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: uniqueness technique (remark [[§2 First Consequences of the Axioms#^rem-2-2|The Uniqueness Technique]]).
> - $gh = e = gh'$, cancel $g$; or $h = h(gh') = (hg)h' = h'$.
> - Used for Proposition [[§2 First Consequences of the Axioms#^prop-2-4|§2.4]], Proposition [[§2 First Consequences of the Axioms#^prop-2-6|§2.6]](2), $(AB)^{-1} = B^{-1}A^{-1}$.

#### Inverse of a product · P2

$(gh)^{-1} = h^{-1}g^{-1}$, and $(g_1 \cdots g_n)^{-1} = g_n^{-1} \cdots g_1^{-1}$, see Proposition [[§2 First Consequences of the Axioms#^prop-2-4|§2.4]] and Corollary [[§2 First Consequences of the Axioms#^cor-2-5|§2.5]]. *Source: WS 1.4.*

^nd-prop-2-4

- [ ] Q1 **[state]** State the formula for two and for $n$ factors.
- [ ] Q2 By WS 1.3, what exactly must be verified? Do both products.
- [ ] Q3 Prove the $n$-factor version by induction on $n$.
- [ ] Q4 **[why]** When is $(gh)^{-1} = g^{-1}h^{-1}$ for all $g, h$? Give a counterexample in $S_3$.
- [ ] Q5 Where is the formula used in Chapter 1 (closure of $S_X$ and $GL_n$; inverse of a word)?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: uniqueness technique.
> - $(gh)(h^{-1}g^{-1}) = g(hh^{-1})g^{-1} = e$ and the other side.
> - Abelian iff inversion is a homomorphism, Proposition [[§18 Conjugation, Products, and Pointwise Products#^prop-18-4|§18.4]]; remark [[§4 Subgroups#^rem-4-1|Two Non-Laws]].

#### One-sided inverses suffice · P2

If $ab = e$ then $b = a^{-1}$ and $a = b^{-1}$, so $ba = e$; and $(a^{-1})^{-1} = a$, see Proposition [[§2 First Consequences of the Axioms#^prop-2-6|§2.6]]. *Source: cf. Pinter Ch. 4; used for WS 2.9.*

^nd-prop-2-6

- [ ] Q1 **[state]** State both parts.
- [ ] Q2 From $ab = e$, why is $b = a^{-1}$? Which cancellation do you use, and against which product?
- [ ] Q3 Why is $a = b^{-1}$? Conclude $ba = e$.
- [ ] Q4 Prove $(a^{-1})^{-1} = a$ by the uniqueness technique.
- [ ] Q5 **[why]** Why does this fail in a monoid? Give the shift on $\mathbb{N}$.

> [!tip]- Hints: route of the proof in the notes
> - $ab = e = aa^{-1}$, cancel on the left; $ab = e = b^{-1}b$, cancel on the right.
> - Remark [[§2 First Consequences of the Axioms#^rem-2-4|Why One-Sided Suffices Here]]; used in Proposition [[§15 Homomorphisms#^prop-15-1|§15.1]].

#### Unique solvability and the Latin square property · P2

$ax = b$ has exactly one solution $x = a^{-1}b$ and $xa = b$ exactly one, $x = ba^{-1}$; hence each element occurs exactly once in every row and column of a finite group's table, see Proposition [[§2 First Consequences of the Axioms#^prop-2-7|§2.7]] and Corollary [[§2 First Consequences of the Axioms#^cor-2-8|§2.8]]. *Source: cf. Pinter Ch. 4; used in WS 2.*

^nd-prop-2-7

- [ ] Q1 **[state]** State the proposition and the corollary.
- [ ] Q2 Prove existence and uniqueness for $ax = b$.
- [ ] Q3 In the row of $a$, translate "$b$ appears in column $x$" into an equation. Which half gives "at least once", which "at most once"?
- [ ] Q4 **[why]** Is every Latin square a group table? Which axiom is invisible row by row?
- [ ] Q5 Use the corollary to fill in a missing entry of the $U_8$ table quickly.

> [!tip]- Hints: route of the proof in the notes
> - Existence $a(a^{-1}b) = b$; uniqueness by left cancellation (Proposition [[§2 First Consequences of the Axioms#^prop-2-1|§2.1]]).
> - Remark [[§2 First Consequences of the Axioms#^rem-2-5|The Converse Fails]] (associativity); tables in Definition [[§14 Multiplication Tables#^def-14-1|§14.1]].

#### Exponent laws · P2

For all $m, n \in \mathbb{Z}$: $(g^n)^{-1} = g^{-n}$, $g^mg^n = g^{m+n}$, $(g^m)^n = g^{mn}$, see Lemma [[§4 Subgroups#^lem-4-4|§4.4]]. *Source: lecture 9/9; cf. Pinter Ch. 10.*

^nd-lem-4-4

- [ ] Q1 **[state]** State the three laws.
- [ ] Q2 Step 0: why does $g$ commute with $g^n$ ($n \geq 0$)?
- [ ] Q3 Prove $g^mg^n = g^{m+n}$ for $m, n \geq 0$ by induction on $n$.
- [ ] Q4 Prove $(g^n)^{-1} = (g^{-1})^n$ for $n \geq 0$; where are WS 1.4 and Step 0 (for $g^{-1}$) used?
- [ ] Q5 Mixed signs, $m \geq 0 \geq n$ with $m + n \geq 0$: which positive-exponent identity do you multiply by $g^n$?
- [ ] Q6 Prove $(g^m)^n = g^{mn}$, first for $n \geq 0$, then $n < 0$.
- [ ] Q7 **[why]** Why do the laws concern a single element? Which identity for two elements fails, and when does it hold?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: induction on the exponent, then reduce negative cases to $g^{-1}$.
> - Step 1: $g^mg^{n+1} = (g^mg^n)g$. Step 2: $(g^ng)^{-1} = g^{-1}(g^n)^{-1}$.
> - Mixed, $m + n \geq 0$: $g^{m+n}g^{-n} = g^m$, multiply on the right by $g^n = (g^{-n})^{-1}$.
> - Remark [[§4 Subgroups#^rem-4-1|Two Non-Laws]]; Proposition [[§18 Conjugation, Products, and Pointwise Products#^prop-18-4|§18.4]].

#### ⟨g⟩ is a subgroup · P2

$\langle g \rangle = \{g^k : k \in \mathbb{Z}\}$ is a subgroup of $G$, see Proposition [[§4 Subgroups#^prop-4-5|§4.5]]. *Source: WS 1.5.*

^nd-prop-4-5

- [ ] Q1 **[state]** State the proposition.
- [ ] Q2 Identity: which power is $e$?
- [ ] Q3 Inverses: which exponent law?
- [ ] Q4 Closure: which exponent law?
- [ ] Q5 **[why]** Why is $\{g^k : k \geq 0\}$ not always a subgroup? When is it?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G1 with Lemma [[§4 Subgroups#^lem-4-4|§4.4]].
> - $e = g^0$; $(g^k)^{-1} = g^{-k}$; $g^mg^n = g^{m+n}$.
> - Nonnegative powers fail in $\mathbb{Z}$ ($\{0, 1, 2, \ldots\}$); they suffice when $g$ has finite order, since $g^{-1} = g^{\operatorname{ord}(g) - 1}$.

#### Defining ⟨g₁,…,g_k⟩ · P2

The right definition of $\langle g_1, \ldots, g_k \rangle$ is the set of all words; products of powers in a fixed order fail, see Example [[§4 Subgroups#^ex-4-1|§4.1]]. *Source: WS 1.6.*

^nd-ex-4-1

- [ ] Q1 **[state]** What does WS 1.6 ask, and what is the answer?
- [ ] Q2 Why does $\{g_1^{n_1}g_2^{n_2}\}$ fail? Compute this set in $S_3$ for $g_1 = (1\,2)$, $g_2 = (2\,3)$ and find an element of $\langle g_1, g_2 \rangle$ missing from it.
- [ ] Q3 Necessity: why does every subgroup containing the $g_i$ contain every word?
- [ ] Q4 Sufficiency: why is the set of words a subgroup?
- [ ] Q5 **[why]** Why can reduced words still fail to be unique? Give the $S_3$ relation.

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G10 (compute in $S_3$) for the counterexample; G1 for sufficiency.
> - Fixed-order set $= \{e, g_1, g_2, g_1g_2\}$; $(g_1g_2)^2 = g_2g_1 = (1\,3\,2)$ is missing.
> - Inverse of a word: reverse and negate (WS 1.4). Relation $(1\,2)(2\,3)(1\,2) = (1\,3)$.

#### Subgroups of ℤ · P2

The subgroups of $(\mathbb{Z}, +)$ are exactly $n\mathbb{Z}$, $n = 0, 1, 2, \ldots$, pairwise distinct, see Proposition [[§5 A Zoo of Subgroups#^prop-5-1|§5.1]]. *Source: WS 1.7.*

^nd-prop-5-1

- [ ] Q1 **[state]** State the classification.
- [ ] Q2 Why is each $n\mathbb{Z}$ a subgroup?
- [ ] Q3 Let $H \neq \{0\}$. Why does $H$ contain a positive integer? Define $n$.
- [ ] Q4 Given $h \in H$, divide by $n$. Why is the remainder in $H$, and why must it be $0$?
- [ ] Q5 Why are the $n\mathbb{Z}$ pairwise distinct?
- [ ] Q6 **[why]** Which property of $\mathbb{Z}$ (absent in $\mathbb{R}$) makes "smallest positive element" exist? What happens in $\mathbb{R}$?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: smallest positive element plus division algorithm (G14).
> - $r = h - qn \in H$, $0 \leq r < n$, so $r = 0$ by minimality.
> - Lemma [[§6 Divisibility and Congruence#^lem-6-1|§6.1]]; in $\mathbb{R}$ the infimum may be $0$: Proposition [[§5 A Zoo of Subgroups#^prop-5-3|§5.3]]. Remark [[§9 Euclid's Lemma, Unique Factorization, and the Chinese Remainder Theorem#^rem-9-2|The Division-Algorithm Pattern]].

#### Subgroups of ℤ² · P2

Subgroups of $\mathbb{Z}^2$ include cyclic ones $\langle (a, b) \rangle$, products $m\mathbb{Z} \times n\mathbb{Z}$, and rank-two lattices not of product form such as $\langle (1,1), (1,-1) \rangle = \{(x, y) : x \equiv y \pmod 2\}$, see Example [[§5 A Zoo of Subgroups#^ex-5-1|§5.1]]. *Source: WS 1.7.*

^nd-ex-5-1

- [ ] Q1 **[state]** List four families of subgroups of $\mathbb{Z}^2$.
- [ ] Q2 Why is $m\mathbb{Z} \times n\mathbb{Z}$ a subgroup?
- [ ] Q3 Prove $\langle (1,1), (1,-1) \rangle = \{(x, y) : x \equiv y \pmod 2\}$, both inclusions.
- [ ] Q4 **[why]** Why is this checkerboard subgroup not of the form $m\mathbb{Z} \times n\mathbb{Z}$?
- [ ] Q5 What theorem (not yet proved) says every subgroup of $\mathbb{Z}^2$ needs at most two generators?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G1 componentwise; explicit coefficients.
> - $a(1,1) + b(1,-1) = (a+b, a-b)$; conversely $a = (x+y)/2$, $b = (x-y)/2$.
> - Contains $(1,1)$ but not $(1,0)$. Remark [[§5 A Zoo of Subgroups#^rem-5-2|Forward Pointer: Rank]].

#### Subgroups of ℝ: list and dichotomy · P2

Subgroups of $(\mathbb{R}, +)$ include $a\mathbb{Z}$, $\mathbb{Q}$, $\mathbb{Z}[\tfrac12]$, $a\mathbb{Z} + b\mathbb{Z}$; every $H \neq \{0\}$ is either $a\mathbb{Z}$ for a unique $a > 0$ or dense, and $\mathbb{Z} + \sqrt2\,\mathbb{Z}$ is dense, see Example [[§5 A Zoo of Subgroups#^ex-5-2|§5.2]], Proposition [[§5 A Zoo of Subgroups#^prop-5-3|§5.3]] and Example [[§5 A Zoo of Subgroups#^ex-5-3|§5.3]]. *Source: WS 1.7 (list); dichotomy from the notes.*

^nd-prop-5-3

- [ ] Q1 **[state]** List four kinds of subgroups of $\mathbb{R}$ and state the dichotomy.
- [ ] Q2 Let $P$ be the positive elements of $H$ and $a = \inf P$. If $a > 0$, why is $a \in H$? (Find two elements of $P$ in $(a, 2a)$.)
- [ ] Q3 Still $a > 0$: show $H = a\mathbb{Z}$ using $\lfloor h/a \rfloor$.
- [ ] Q4 If $a = 0$, show every interval $(x - \varepsilon, x + \varepsilon)$ meets $H$.
- [ ] Q5 **[why]** Why is $\mathbb{Z} + \sqrt2\,\mathbb{Z}$ not cyclic, hence dense?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: infimum replaces "smallest positive element"; then the division-algorithm pattern.
> - $a < h' < h < 2a$ gives $0 < h - h' < a$, contradiction.
> - $a = 0$: pick $h \in P$ with $h < \varepsilon$, take $q = \lfloor x/h \rfloor$.
> - $H = a\mathbb{Z}$ would give $\sqrt2 = n/m$.

#### Subgroups of GL₂(ℝ) and GL₃(ℝ) · P2

$GL_n(\mathbb{R})$ ($n = 2, 3$) contains $SL_n$, scalars, diagonal, upper-triangular and unipotent matrices, $O(n)$, $SO(n)$, permutation matrices, $GL_n(\mathbb{Q})$, $GL_n(\mathbb{Z})$, cyclic subgroups and block copies, see Example [[§5 A Zoo of Subgroups#^ex-5-4|§5.4]]. *Source: WS 1.7.*

^nd-ex-5-4

- [ ] Q1 **[state]** List at least eight subgroups of $GL_2(\mathbb{R})$.
- [ ] Q2 For upper-triangular and unipotent matrices, why are products and inverses again of the same kind?
- [ ] Q3 Why is $GL_n(\mathbb{Z}) = \{A \text{ integer} : \det A = \pm 1\}$ a subgroup? What does Cramer's rule give?
- [ ] Q4 Which subgroup "is" $(\mathbb{R}, +)$, which "is" $\mathbb{R}^\times$, which "is" $S_n$, which "is" $C_n$?
- [ ] Q5 **[why]** Is the set of matrices with $\det A > 0$ a subgroup? With $\det A < 0$? With integer entries?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G1 for each item; G10.
> - Back-substitution for triangular inverses; Cramer for $\mathbb{Q}$ and $\mathbb{Z}$.
> - $\begin{pmatrix} 1 & t \\ 0 & 1 \end{pmatrix}$; $\lambda I_n$; permutation matrices; $\langle R_{2\pi/n} \rangle$. Remark [[§5 A Zoo of Subgroups#^rem-5-3|Summary of WS 1.7]].

### Priority 3 · filled in, using a technique the problem sets drill

#### Elements of a finite group have finite order · P3

In a finite group every $g$ has $g^N = e$ for some $N \geq 1$, and $\operatorname{ord}(g) \leq |G|$, see Proposition [[§4 Subgroups#^prop-4-8|§4.8]]. *Source: notes.*

^nd-prop-4-8

- [ ] Q1 **[state]** State the proposition.
- [ ] Q2 Which $|G| + 1$ elements do you consider, and why must two coincide?
- [ ] Q3 From $g^i = g^j$ with $i < j$, derive a positive exponent killing $g$, with a bound.
- [ ] Q4 Why does a least such exponent exist?
- [ ] Q5 **[why]** Where does the argument fail for $1 \in \mathbb{Z}$? What stronger statement needs Lagrange?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: pigeonhole (finiteness), then well-ordering.
> - $g^{j-i} = e$ with $1 \leq j - i \leq |G|$.
> - Remark [[§4 Subgroups#^rem-4-4|Where Finiteness Enters]]; $\operatorname{ord}(g) \mid |G|$ is G3 (Lagrange).

### Priority 4 · notes only (Pinter, MATH 412, not from class)

#### No zero divisors in a field · P4

In a field $a \cdot 0 = 0$, and $ab = 0$ implies $a = 0$ or $b = 0$, see Proposition [[§3 Basic Examples of Groups#^prop-3-1|§3.1]]. *Source: notes.*

^nd-prop-3-1

- [ ] Q1 **[state]** State the proposition.
- [ ] Q2 Prove $a \cdot 0 = 0$. In which group do you cancel?
- [ ] Q3 If $ab = 0$ and $a \neq 0$, show $b = 0$.
- [ ] Q4 **[why]** Why does this show closure of $k \setminus \{0\}$ is consistent rather than an extra assumption? Which $\mathbb{Z}/n\mathbb{Z}$ has zero divisors?

> [!tip]- Hints: route of the proof in the notes
> - $a \cdot 0 = a(0+0) = a \cdot 0 + a \cdot 0$; cancel in $(k, +)$.
> - $b = (a^{-1}a)b = a^{-1}(ab) = a^{-1} \cdot 0 = 0$.
> - Remark [[§3 Basic Examples of Groups#^rem-3-1|Consistency of the Field Axioms]]; $[2][3] = [0]$ in $\mathbb{Z}/6\mathbb{Z}$, Proposition [[§8 Invertibility and Unit Groups#^prop-8-4|§8.4]].

#### A subset that is a group is a subgroup · P4

A subgroup is a group with the same identity and inverses; conversely a subset closed under the operation that is a group under it has identity $e_G$ and the same inverses, so is a subgroup, see Proposition [[§4 Subgroups#^prop-4-1|§4.1]]. *Source: notes.*

^nd-prop-4-1

- [ ] Q1 **[state]** State both directions.
- [ ] Q2 Let $e$ be the identity of $H$. Show $e = e_G$: which equation in $G$ do you cancel?
- [ ] Q3 Show the inverse of $h$ in $H$ equals $h^{-1}$ in $G$.
- [ ] Q4 **[why]** Why is closure under the operation assumed separately?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G1 (subgroup test), via cancellation and uniqueness of inverses.
> - $ee = e = ee_G$ in $G$, cancel $e$ on the left.
> - $hh' = h'h = e = e_G$, then Proposition [[§2 First Consequences of the Axioms#^prop-2-3|§2.3]].

#### Equivalent subgroup criteria · P4

For $H \subseteq G$: subgroup $\iff$ nonempty and closed under inverses and products $\iff$ nonempty and $a, b \in H \Rightarrow ab^{-1} \in H$, see Proposition [[§4 Subgroups#^prop-4-2|§4.2]]. *Source: cf. Pinter Ch. 5.*

^nd-prop-4-2

- [ ] Q1 **[state]** State the three equivalent conditions.
- [ ] Q2 Prove (2) $\Rightarrow$ (3).
- [ ] Q3 For (3) $\Rightarrow$ (1): get $e$, then inverses, then products, in that order. Which element do you plug in at each step?
- [ ] Q4 Where is $(b^{-1})^{-1} = b$ used?
- [ ] Q5 **[why]** Use the one-step test to show $\operatorname{Ker}\varphi$ is a subgroup in one line.

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G1 (one-step test).
> - $e = aa^{-1}$; $b^{-1} = eb^{-1}$; $ab = a(b^{-1})^{-1}$; Proposition [[§2 First Consequences of the Axioms#^prop-2-6|§2.6]](2).

#### Intersections of subgroups · P4

Any nonempty intersection of subgroups is a subgroup; unions need not be, see Proposition [[§4 Subgroups#^prop-4-3|§4.3]]. *Source: cf. Pinter Ch. 5.*

^nd-prop-4-3

- [ ] Q1 **[state]** State the proposition.
- [ ] Q2 Check the three conditions for $K = \bigcap_i H_i$.
- [ ] Q3 **[why]** Why is $2\mathbb{Z} \cup 3\mathbb{Z}$ not a subgroup? Which condition fails?
- [ ] Q4 Where is the proposition used (top-down $\langle S \rangle$; $SO(n)$)?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G1; each condition is checked "coordinatewise in $i$".
> - Used in Proposition [[§4 Subgroups#^prop-4-7|§4.7]] and Definition [[§3 Basic Examples of Groups#^def-3-9|§3.9]].

#### ⟨g⟩ is the smallest subgroup containing g · P4

Every subgroup containing $g$ contains $\langle g \rangle$; and $\langle g \rangle$ is abelian, see Proposition [[§4 Subgroups#^prop-4-6|§4.6]]. *Source: notes.*

^nd-prop-4-6

- [ ] Q1 **[state]** State the proposition.
- [ ] Q2 Why does $H \ni g$ contain $g^n$ for $n \geq 0$, and $g^{-n}$?
- [ ] Q3 Why is $\langle g \rangle$ abelian?
- [ ] Q4 **[why]** Where is minimality used later (subgroups of cyclic groups; $\langle C \rangle \subseteq A_n$)?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G1 plus induction.
> - $g^n$ by closure; $g^{-n} = (g^{-1})^n$; $g^mg^n = g^{m+n} = g^ng^m$.
> - Used in Theorem [[§17 Cyclic Groups#^thm-17-4|§17.4]] and Theorem [[§21 The Sign Homomorphism and the Alternating Group#^thm-21-9|§21.9]].

#### Top-down characterization of ⟨g₁,…,g_k⟩ · P4

$\langle g_1, \ldots, g_k \rangle$ is the smallest subgroup containing the $g_i$ and equals the intersection of all such subgroups, see Proposition [[§4 Subgroups#^prop-4-7|§4.7]]. *Source: notes.*

^nd-prop-4-7

- [ ] Q1 **[state]** State the proposition.
- [ ] Q2 Why is the set of words the smallest such subgroup?
- [ ] Q3 Let $K$ be the intersection. Why $K \subseteq \langle g_1, \ldots, g_k \rangle$, and why the reverse inclusion?
- [ ] Q4 **[why]** Which description is "bottom-up" and which "top-down"? Which is better for proving $\langle C \rangle \subseteq A_n$?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G1 and minimality.
> - Intersection is a subgroup (Proposition [[§4 Subgroups#^prop-4-3|§4.3]]) containing the $g_i$; $\langle g_1, \ldots, g_k \rangle$ is one of the intersected subgroups.
> - Remark [[§4 Subgroups#^rem-4-3|Bottom-Up versus Top-Down]].

# T2. Arithmetic modulo n

## Definitions T2

### Priority 1 · problem sets (directly or extended)

#### Greatest common divisor; coprime · P1

$\gcd(a, b)$ is the largest positive integer dividing both $a$ and $b$ (not both zero); $a, b$ are coprime if $\gcd(a, b) = 1$, see Definition [[§8 Invertibility and Unit Groups#^def-8-1|§8.1]]. *Source: notes; [[Group Theory HW Drill#^ps1-6|PS1.6]].*

^nd-def-8-1

- [ ] Q1 **[def]** Define $\gcd$ and coprime.
- [ ] Q2 **[example]** $\gcd(12, 18)$, $\gcd(3, 8)$, $\gcd(a, p)$ for $1 \leq a \leq p - 1$.
- [ ] Q3 **[use]** State Bézout. How does $ax + by = 1$ certify $\gcd(a, b) = 1$?
- [ ] Q4 **[why]** Why is $\gcd(a + kn, n) = \gcd(a, n)$? Where is this needed?

> [!tip]- Hints: where it lives, examples
> - Definition [[§8 Invertibility and Unit Groups#^def-8-1|§8.1]]; Corollary [[§5 A Zoo of Subgroups#^cor-5-2|§5.2]].
> - Common divisors of $(a, n)$ and $(a + kn, n)$ coincide: membership in $U_n$ is well defined, Proposition [[§8 Invertibility and Unit Groups#^prop-8-3|§8.3]].

#### Invertibility modulo n · P1

$a$ (or $[a]$) is invertible modulo $n$ if $ax \equiv 1 \pmod n$ for some $x$; $[x] = [a]^{-1}$, see Definition [[§8 Invertibility and Unit Groups#^def-8-2|§8.2]]. *Source: WS 1 (examples); [[Group Theory HW Drill#^ps1-6-1|PS1.6(1)]].*

^nd-def-8-2

- [ ] Q1 **[def]** State the definition.
- [ ] Q2 **[example]** Which classes are invertible modulo $8$? Why is $[2]$ not (parity argument)?
- [ ] Q3 **[example]** Find $[7]^{-1}$ modulo $26$ by the extended Euclidean algorithm.
- [ ] Q4 **[use]** Solve $3x \equiv 5 \pmod 7$. What goes wrong with $4x \equiv 1$ and $4x \equiv 2 \pmod 6$?
- [ ] Q5 **[why]** Why can classes have inverses when integers do not?

> [!tip]- Hints: where it lives, examples
> - Definition [[§8 Invertibility and Unit Groups#^def-8-2|§8.2]]; criterion Proposition [[§8 Invertibility and Unit Groups#^prop-8-1|§8.1]].
> - Example [[§8 Invertibility and Unit Groups#^ex-8-1|§8.1]] (mod $8$: $1 + 8k$ is odd), Example [[§8 Invertibility and Unit Groups#^ex-8-3|§8.3]] ($[7]^{-1} = [15]$), Example [[§8 Invertibility and Unit Groups#^ex-8-4|§8.4]].
> - Remark [[§8 Invertibility and Unit Groups#^rem-8-1|Why Integers Have No Inverses]].

#### The unit group Uₙ · P1

$U_n = (\mathbb{Z}/n\mathbb{Z})^\times = \{[a] : \gcd(a, n) = 1\}$ with $[a][b] := [ab]$, an abelian group with identity $[1]$, see Definition [[§8 Invertibility and Unit Groups#^def-8-4|§8.4]]. *Source: WS 1 (examples); [[Group Theory HW Drill#^ps1-6-2|PS1.6(2)]].*

^nd-def-8-4

- [ ] Q1 **[def]** Define $U_n$ and its operation.
- [ ] Q2 **[example]** List $U_5$, $U_8$, $U_9$, $U_{10}$, $U_{12}$, and give an inverse table for $U_7$.
- [ ] Q3 **[use]** Which are cyclic: $U_5$, $U_7$, $U_8$, $U_{10}$, $U_{15}$? Give generators or a reason.
- [ ] Q4 **[why]** Why is $\gcd(a, n) = 1$ the right membership condition (two descriptions of the same set)?
- [ ] Q5 **[use]** To which product does $U_n$ decompose by the CRT?

> [!tip]- Hints: where it lives, examples
> - Definition [[§8 Invertibility and Unit Groups#^def-8-4|§8.4]]; Example [[§8 Invertibility and Unit Groups#^ex-8-5|§8.5]], Example [[§8 Invertibility and Unit Groups#^ex-8-2|§8.2]].
> - Proposition [[§16 Isomorphisms#^prop-16-7|§16.7]], Proposition [[§16 Isomorphisms#^prop-16-8|§16.8]], Example [[§22 The Structure of Uₙ#^ex-22-1|§22.1]].
> - Invertibility criterion Proposition [[§8 Invertibility and Unit Groups#^prop-8-1|§8.1]]; Theorem [[§22 The Structure of Uₙ#^thm-22-2|§22.2]].

### Priority 2 · worksheets and lectures

#### Divisibility · P2

$n \mid m$ means $m = kn$ for some $k \in \mathbb{Z}$; it is a statement, not a number, see Definition [[§6 Divisibility and Congruence#^def-6-1|§6.1]]. *Source: class discussion (Sept 2, 4); notes.*

^nd-def-6-1

- [ ] Q1 **[def]** State the definition. Which number goes on the left?
- [ ] Q2 **[example]** True or false: $3 \mid 12$, $5 \mid -20$, $4 \mid 6$, $0 \mid 0$, $7 \mid 0$.
- [ ] Q3 **[use]** Show: if $d \mid a$ and $d \mid b$ then $d \mid ax + by$. Where is this used (gcd arguments)?
- [ ] Q4 **[why]** Why is $n \mid a$ equivalent to $a \bmod n = 0$?

> [!tip]- Hints: where it lives, examples
> - Definition [[§6 Divisibility and Congruence#^def-6-1|§6.1]]; remainders, Definition [[§6 Divisibility and Congruence#^def-6-2|§6.2]].
> - Linear combinations: Invertibility Criterion, Proposition [[§8 Invertibility and Unit Groups#^prop-8-1|§8.1]] (direction $\Rightarrow$); Corollary [[§5 A Zoo of Subgroups#^cor-5-2|§5.2]].

#### Congruence modulo n · P2

$a \equiv b \pmod n$ means $n \mid a - b$, see Definition [[§6 Divisibility and Congruence#^def-6-3|§6.3]]. *Source: WS 1 (examples); class discussion.*

^nd-def-6-3

- [ ] Q1 **[def]** State the definition.
- [ ] Q2 **[example]** Check $14 \equiv 2 \pmod{12}$ and $-1 \equiv 4 \pmod 5$.
- [ ] Q3 **[use]** Prove congruence is an equivalence relation directly from the definition.
- [ ] Q4 **[why]** Show $a \equiv b \pmod n$ iff $a \bmod n = b \bmod n$. Why does $|r - r'| < n$ force $r = r'$?

> [!tip]- Hints: where it lives, examples
> - Definition [[§6 Divisibility and Congruence#^def-6-3|§6.3]]; Proposition [[§6 Divisibility and Congruence#^prop-6-2|§6.2]].
> - Transitivity: $a - c = (a - b) + (b - c) = (k + l)n$.

#### Residue classes · P2

The residue class of $a$ is $[a] = a + n\mathbb{Z} = \{b : b \equiv a \pmod n\}$; there are exactly $n$ classes $[0], \ldots, [n-1]$, see Definition [[§6 Divisibility and Congruence#^def-6-4|§6.4]]. *Source: WS 1; notes.*

^nd-def-6-4

- [ ] Q1 **[def]** Define $[a]$ and "representative".
- [ ] Q2 **[example]** List some elements of $[3]$ modulo $5$; which other names does this class have?
- [ ] Q3 **[use]** When is $[a] = [b]$? Why are there exactly $n$ classes?
- [ ] Q4 **[why]** What is the "clock picture" of $\mathbb{Z}/12\mathbb{Z}$? Which later construction generalizes $a + n\mathbb{Z}$?

> [!tip]- Hints: where it lives, examples
> - Definition [[§6 Divisibility and Congruence#^def-6-4|§6.4]]; Proposition [[§6 Divisibility and Congruence#^prop-6-2|§6.2]]; remark [[§6 Divisibility and Congruence#^rem-6-1|The Clock Picture]].
> - $a + n\mathbb{Z}$ is a coset of the subgroup $n\mathbb{Z}$ (Chapter 6).

#### The cyclic group ℤ/nℤ · P2

$\mathbb{Z}/n\mathbb{Z} = \{[a]\}$ with $[a] + [b] := [a + b]$ is an abelian group of order $n$, identity $[0]$, $-[a] = [-a]$, also written $C_n$, see Definition [[§7 The Group ℤ∕nℤ#^def-7-1|§7.1]]. *Source: WS 1 (examples); WS 2.*

^nd-def-7-1

- [ ] Q1 **[def]** Define $\mathbb{Z}/n\mathbb{Z}$ and its operation.
- [ ] Q2 **[use]** What must be checked before $[a] + [b] := [a + b]$ is an operation?
- [ ] Q3 **[example]** Why is $\mathbb{Z}/n\mathbb{Z}$ cyclic? Which classes generate $\mathbb{Z}/12\mathbb{Z}$?
- [ ] Q4 **[why]** Why is $(\mathbb{Z}/n\mathbb{Z}, \times)$ not a group, and what is the fix?
- [ ] Q5 **[use]** Of which homomorphism is $n\mathbb{Z}$ the kernel?

> [!tip]- Hints: where it lives, examples
> - Definition [[§7 The Group ℤ∕nℤ#^def-7-1|§7.1]]; Proposition [[§7 The Group ℤ∕nℤ#^prop-7-1|§7.1]].
> - $\langle [1] \rangle$; generators $[1], [5], [7], [11]$: Example [[§17 Cyclic Groups#^ex-17-1|§17.1]].
> - $[0]$ has no inverse; restrict to $U_n$, Definition [[§8 Invertibility and Unit Groups#^def-8-4|§8.4]]. Reduction $x \mapsto [x]$: Example [[§15 Homomorphisms#^ex-15-1|§15.1]](2).

#### Well-defined · P2

A rule on equivalence classes computed from a representative is well defined if equivalent representatives give the same value; only then is it a function on classes, see Definition [[§7 The Group ℤ∕nℤ#^def-7-2|§7.2]]. *Source: notes; recurs from WS 2 on.*

^nd-def-7-2

- [ ] Q1 **[def]** State the definition, for one class and for several classes.
- [ ] Q2 **[example]** Show that $[a] + [b] := [a + b]$ and $[a][b] := [ab]$ are well defined modulo $n$.
- [ ] Q3 **[why]** Is $[a] \mapsto a$ (from $\mathbb{Z}/n\mathbb{Z}$ to $\mathbb{Z}$) well defined? Is $\mathbb{Z}/4\mathbb{Z} \to U_5$, $[k] \mapsto 2^k$? Is $\mathbb{Z}/3\mathbb{Z} \to U_5$, $[k] \mapsto 2^k$?
- [ ] Q4 **[use]** What is the general criterion for a homomorphism $\mathbb{Z} \to G$ to descend to $\mathbb{Z}/n\mathbb{Z}$?

> [!tip]- Hints: where it lives, examples
> - Definition [[§7 The Group ℤ∕nℤ#^def-7-2|§7.2]]; Proposition [[§7 The Group ℤ∕nℤ#^prop-7-1|§7.1]]; Proposition [[§8 Invertibility and Unit Groups#^prop-8-3|§8.3]].
> - $2^4 \equiv 1 \pmod 5$ but $2^3 \not\equiv 1$; Lemma [[§7 The Group ℤ∕nℤ#^lem-7-2|§7.2]](2): need $\varphi(n) = e$.
> - Strategy G2 (well-definedness on representatives).

### Priority 4 · notes only (Pinter, MATH 412, not from class)

#### Quotient and remainder; a mod n · P4

For $n \geq 1$, $a = qn + r$ with $0 \leq r < n$; $q$ is the quotient, $r = a \bmod n$ the remainder, see Definition [[§6 Divisibility and Congruence#^def-6-2|§6.2]]. *Source: notes.*

^nd-def-6-2

- [ ] Q1 **[def]** State the definition. Which lemma makes it meaningful?
- [ ] Q2 **[example]** Compute $14 \bmod 12$, $25 \bmod 8$, $-7 \bmod 5$.
- [ ] Q3 **[use]** How does the remainder detect congruence?
- [ ] Q4 **[why]** Why is $-7 \bmod 5 = 3$ and not $-2$?

> [!tip]- Hints: where it lives, examples
> - Definition [[§6 Divisibility and Congruence#^def-6-2|§6.2]]; Lemma [[§6 Divisibility and Congruence#^lem-6-1|§6.1]]; Proposition [[§6 Divisibility and Congruence#^prop-6-2|§6.2]](1).
> - $-7 = (-2) \cdot 5 + 3$, and $0 \leq r < n$ is required.

#### Euler's totient · P4

$\varphi(n)$ is the number of $1 \leq a \leq n$ with $\gcd(a, n) = 1$, i.e. $|U_n|$, see Definition [[§8 Invertibility and Unit Groups#^def-8-3|§8.3]]. *Source: notes.*

^nd-def-8-3

- [ ] Q1 **[def]** Define $\varphi(n)$.
- [ ] Q2 **[example]** Compute $\varphi(8)$, $\varphi(9)$, $\varphi(12)$, $\varphi(p)$, $\varphi(p^a)$.
- [ ] Q3 **[use]** State the totient formula and the isomorphism it comes from.
- [ ] Q4 **[why]** Why is $\varphi$ not monotone? How many generators does a cyclic group of order $n$ have?

> [!tip]- Hints: where it lives, examples
> - Definition [[§8 Invertibility and Unit Groups#^def-8-3|§8.3]]; Example [[§8 Invertibility and Unit Groups#^ex-8-5|§8.5]]; Corollary [[§22 The Structure of Uₙ#^cor-22-3|§22.3]].
> - Generators: Corollary [[§17 Cyclic Groups#^cor-17-6|§17.6]](1).

## Proofs T2

### Priority 1 · problem sets (directly or extended)

#### Invertibility criterion · P1

$[a]$ is invertible modulo $n$ iff $\gcd(a, n) = 1$, Proposition [[§8 Invertibility and Unit Groups#^prop-8-1|§8.1]] → drilled as [[Group Theory HW Drill#^ps1-6-1|PS1.6(1)]].

#### Uₙ is a group · P1

$U_n$ with $[a][b] = [ab]$ is a well-defined abelian group, Proposition [[§8 Invertibility and Unit Groups#^prop-8-3|§8.3]] → drilled as [[Group Theory HW Drill#^ps1-6-2|PS1.6(2)]].

#### Chinese remainder theorem · P1

For $\gcd(m, n) = 1$, $[x]_{mn} \mapsto ([x]_m, [x]_n)$ is a well-defined bijective homomorphism $\mathbb{Z}/mn\mathbb{Z} \to \mathbb{Z}/m\mathbb{Z} \times \mathbb{Z}/n\mathbb{Z}$; the same for pairwise coprime $m_1, \ldots, m_k$, see Theorem [[§9 Euclid's Lemma, Unique Factorization, and the Chinese Remainder Theorem#^thm-9-3|§9.3]]. *Source: cf. Pinter Ch. 23; MATH 412; assumed on [[Group Theory HW Drill#^ps1-6|PS1.6]].*

^nd-thm-9-3

- [ ] Q1 **[state]** State the theorem in map form and in "simultaneous congruences" form.
- [ ] Q2 Well-defined and homomorphism: one line each.
- [ ] Q3 Injective: from $m \mid x - y$ and $n \mid x - y$, derive $mn \mid x - y$. Which lemma?
- [ ] Q4 Surjective: by counting, and constructively with $mu + nv = 1$. Check $x = s\,mu + r\,nv$.
- [ ] Q5 Solve $x \equiv 2 \pmod 3$, $x \equiv 3 \pmod 5$.
- [ ] Q6 **[why]** Why is $\gcd(m, n) = 1$ needed? Is $\mathbb{Z}/4\mathbb{Z} \cong \mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/2\mathbb{Z}$?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G2 then G14.
> - $x - y = mt$, $n \mid mt$, Euclid gives $n \mid t$.
> - Example [[§9 Euclid's Lemma, Unique Factorization, and the Chinese Remainder Theorem#^ex-9-1|§9.1]] ($x = 8$). $\mathbb{Z}/4\mathbb{Z} \not\cong (\mathbb{Z}/2\mathbb{Z})^2$ by Proposition [[§16 Isomorphisms#^prop-16-3|§16.3]](2).
> - Induction on $k$: $\gcd(m_1 \cdots m_{k-1}, m_k) = 1$ (Lemma [[§22 The Structure of Uₙ#^lem-22-1|§22.1]]).

### Priority 2 · worksheets and lectures

#### ℤ/nℤ is a group · P2

$[a] + [b] := [a + b]$ is well defined, and $\mathbb{Z}/n\mathbb{Z}$ is an abelian group of order $n$, see Proposition [[§7 The Group ℤ∕nℤ#^prop-7-1|§7.1]]. *Source: WS 1 (examples); class discussion.*

^nd-prop-7-1

- [ ] Q1 **[state]** State the proposition, with identity and inverses.
- [ ] Q2 What exactly is to be checked for well-definedness? Do it with $a' = a + kn$, $b' = b + ln$.
- [ ] Q3 Given well-definedness, why are associativity and commutativity inherited?
- [ ] Q4 Why is $|\mathbb{Z}/n\mathbb{Z}| = n$?
- [ ] Q5 **[why]** Give a rule on residue classes that is not well defined.

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G2 (well-definedness on representatives).
> - $a' + b' = (a + b) + (k + l)n$.
> - $([a] + [b]) + [c] = [(a + b) + c]$.
> - Non-example: $[a] \mapsto a$, or $[k] \mapsto 2^k$ on $\mathbb{Z}/3\mathbb{Z} \to U_5$.

#### ℤ/nℤ is a field iff n is prime · P2

For $n \geq 2$, $\mathbb{Z}/n\mathbb{Z}$ is a field iff $n$ is prime; then it is $\mathbb{F}_p$ with $\mathbb{F}_p^\times = U_p$, see Proposition [[§8 Invertibility and Unit Groups#^prop-8-4|§8.4]]. *Source: notes; WS 1 (examples).*

^nd-prop-8-4

- [ ] Q1 **[state]** State the proposition.
- [ ] Q2 Which field axioms hold for every $n$, and why does everything reduce to "every nonzero class is invertible"?
- [ ] Q3 If $n = p$ is prime, why is every nonzero class a unit?
- [ ] Q4 If $n = ab$ with $1 < a, b < n$, exhibit a nonzero non-unit and a zero divisor.
- [ ] Q5 **[why]** Why is "$[1] \neq [0]$" needed, i.e. why is $n \geq 2$ assumed?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G14 (invertibility criterion).
> - Ring axioms inherited from $\mathbb{Z}$ as for $U_n$; Proposition [[§8 Invertibility and Unit Groups#^prop-8-1|§8.1]] with $\gcd(a, p) = 1$.
> - $[a][b] = [0]$ with $\gcd(a, n) = a$; compare Proposition [[§3 Basic Examples of Groups#^prop-3-1|§3.1]].

#### Unique prime factorization · P2

Every $n \geq 2$ is a product of primes, unique up to order, see Theorem [[§9 Euclid's Lemma, Unique Factorization, and the Chinese Remainder Theorem#^thm-9-2|§9.2]]. *Source: cf. Pinter Ch. 22; MATH 412; used in WS 2.8 and §22.*

^nd-thm-9-2

- [ ] Q1 **[state]** State the theorem in both forms.
- [ ] Q2 Existence: which induction, and what is the inductive step?
- [ ] Q3 Uniqueness: from $p_1 \cdots p_k = q_1 \cdots q_l$, why is $p_1$ some $q_j$?
- [ ] Q4 How does induction finish uniqueness?
- [ ] Q5 **[why]** Where does the course use uniqueness (structure of $\mathbb{Q}^\times$; pairwise coprime $P_i$ in $U_n$)?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: strong induction plus Euclid (G14).
> - $p_1 \mid q_1 \cdots q_l$, Euclid repeatedly, $p_1 = q_j$ since $q_j$ is prime; cancel.
> - Proposition [[§16 Isomorphisms#^prop-16-9|§16.9]](2); Theorem [[§22 The Structure of Uₙ#^thm-22-2|§22.2]].

### Priority 3 · filled in, using a technique the problem sets drill

#### Descent lemma for ℤ/nℤ · P3

A function $f : \mathbb{Z} \to X$ factors as $\bar f([k]) = f(k)$ iff $f(k) = f(k + n)$ for all $k$, uniquely; for a homomorphism $\varphi : \mathbb{Z} \to G$ this is $\varphi(n) = e$, i.e. $n\mathbb{Z} \subseteq \operatorname{Ker}\varphi$, and then $\bar\varphi$ is a homomorphism, see Lemma [[§7 The Group ℤ∕nℤ#^lem-7-2|§7.2]]. *Source: notes (template for every later well-definedness argument).*

^nd-lem-7-2

- [ ] Q1 **[state]** State both parts.
- [ ] Q2 Prove ($\Rightarrow$) of (1).
- [ ] Q3 Prove ($\Leftarrow$): why does $f(k) = f(k + mn)$ hold for all $m \in \mathbb{Z}$, including $m < 0$? Why is $\bar f$ unique?
- [ ] Q4 For a homomorphism, why is $\varphi(k + n) = \varphi(k)$ for all $k$ equivalent to $\varphi(n) = e$, and to $n\mathbb{Z} \subseteq \operatorname{Ker}\varphi$?
- [ ] Q5 Why is $\bar\varphi$ a homomorphism?
- [ ] Q6 **[why]** List three places where this lemma replaces a well-definedness check. What is its general form for $G/N$?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G2; G5 for the general form (maps out of $G/N$ when $N \subseteq \operatorname{Ker}$).
> - $\bar f([k]) := f(k)$ is unambiguous since $k' = k + mn$.
> - $\varphi(k + n) = \varphi(k)\varphi(n)$; kernels are subgroups.
> - Remark [[§7 The Group ℤ∕nℤ#^rem-7-1|Where This Is Used]]: Proposition [[§16 Isomorphisms#^prop-16-7|§16.7]], Theorem [[§17 Cyclic Groups#^thm-17-1|§17.1]], Proposition [[§17 Cyclic Groups#^prop-17-3|§17.3]].

### Priority 4 · notes only (Pinter, MATH 412, not from class)

#### Division algorithm · P4

For $n > 0$ and $m \in \mathbb{Z}$ there are unique $q, r$ with $m = qn + r$, $0 \leq r < n$, see Lemma [[§6 Divisibility and Congruence#^lem-6-1|§6.1]]. *Source: cf. Pinter Ch. 10; used throughout.*

^nd-lem-6-1

- [ ] Q1 **[state]** State the lemma.
- [ ] Q2 Existence: which set do you take the least element of, and why is it nonempty?
- [ ] Q3 Why is the least element $r$ smaller than $n$?
- [ ] Q4 Uniqueness: from $qn + r = q'n + r'$, why is $q = q'$?
- [ ] Q5 **[why]** List three proofs in the notes that run "take the smallest positive element, then divide".

> [!tip]- Hints: route of the proof in the notes
> - Strategy: well-ordering (G14).
> - $\{m - kn\} \cap \mathbb{Z}_{\geq 0}$, nonempty with $k = -|m|$; if $r \geq n$ then $r - n$ is smaller.
> - $(q - q')n = r' - r$ with $|r' - r| < n$.
> - Proposition [[§5 A Zoo of Subgroups#^prop-5-1|§5.1]], Theorem [[§17 Cyclic Groups#^thm-17-4|§17.4]], Proposition [[§17 Cyclic Groups#^prop-17-3|§17.3]](2); remark [[§9 Euclid's Lemma, Unique Factorization, and the Chinese Remainder Theorem#^rem-9-2|The Division-Algorithm Pattern]].

#### Congruence is an equivalence relation · P4

$a \equiv b \pmod n$ iff $a \bmod n = b \bmod n$; and congruence is reflexive, symmetric, transitive, see Proposition [[§6 Divisibility and Congruence#^prop-6-2|§6.2]]. *Source: notes.*

^nd-prop-6-2

- [ ] Q1 **[state]** State both parts.
- [ ] Q2 Prove (1): write $a = qn + r$, $b = q'n + r'$. Both directions.
- [ ] Q3 Prove the three properties directly.
- [ ] Q4 **[why]** Why does (1) give (2) "for free"? How many classes are there, and why?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: division algorithm.
> - $n \mid (a - b) - (q - q')n = r - r'$ with $|r - r'| < n$.
> - "Same remainder" is visibly an equivalence relation; one class per remainder.

#### Multiplication by a nonzero class permutes the nonzero classes mod p · P4

For $p$ prime and $p \nmid a$, $[x] \mapsto [a][x]$ is a bijection of $\{[1], \ldots, [p-1]\}$; so $[a]$ is invertible, see Proposition [[§8 Invertibility and Unit Groups#^prop-8-2|§8.2]]. *Source: notes.*

^nd-prop-8-2

- [ ] Q1 **[state]** State the proposition.
- [ ] Q2 Why do the products $ax$ ($1 \leq x \leq p-1$) avoid $[0]$? Which lemma?
- [ ] Q3 Why are they pairwise distinct?
- [ ] Q4 Why does this force some $ax \equiv 1$?
- [ ] Q5 **[why]** Why does the same argument fail in $\mathbb{Z}$? Where else does "finiteness plus cancellation" appear?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: pigeonhole with cancellation (G14).
> - Euclid's lemma, Lemma [[§9 Euclid's Lemma, Unique Factorization, and the Chinese Remainder Theorem#^lem-9-1|§9.1]]: $p \mid a(i - j)$ gives $p \mid i - j$.
> - $p - 1$ distinct values in a set of size $p - 1$. Remark [[§8 Invertibility and Unit Groups#^rem-8-2|Finiteness Plus Cancellation]]; compare Proposition [[§4 Subgroups#^prop-4-8|§4.8]].

#### Euclid's lemma · P4

If $\gcd(c, a) = 1$ and $c \mid ab$ then $c \mid b$; in particular a prime dividing $ab$ divides $a$ or $b$, see Lemma [[§9 Euclid's Lemma, Unique Factorization, and the Chinese Remainder Theorem#^lem-9-1|§9.1]]. *Source: cf. Pinter Ch. 22; used in §8, §17, §22.*

^nd-lem-9-1

- [ ] Q1 **[state]** State both forms.
- [ ] Q2 Write the Bézout relation for $\gcd(c, a) = 1$ and multiply by $b$. Why does $c$ divide both terms?
- [ ] Q3 Deduce the prime case: why does $p \nmid a$ give $\gcd(p, a) = 1$?
- [ ] Q4 **[why]** Give a counterexample when $c$ is not coprime to $a$ (or not prime). Name two proofs in the notes that use the general form.

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G14 (Bézout).
> - $b = cbx + aby$.
> - E.g. $6 \mid 4 \cdot 3$ but $6 \nmid 4$, $6 \nmid 3$. Used in Proposition [[§17 Cyclic Groups#^prop-17-5|§17.5]] and Theorem [[§9 Euclid's Lemma, Unique Factorization, and the Chinese Remainder Theorem#^thm-9-3|§9.3]].

# T3. Permutations

## Definitions T3

### Priority 2 · worksheets and lectures

#### Two-line notation · P2

$\sigma \in S_n$ is recorded as the array with top row $1, \ldots, n$ and bottom row $\sigma(1), \ldots, \sigma(n)$, see Definition [[§10 Cycle Notation and the Group S₃#^def-10-1|§10.1]]. *Source: notes; WS 2.*

^nd-def-10-1

- [ ] Q1 **[def]** State two-line notation. What does column $i$ say?
- [ ] Q2 **[example]** Write $(1\,3)$ and $(1\,3\,2)$ in two-line notation.
- [ ] Q3 **[use]** How do you read off $\sigma^{-1}$ from two-line notation?
- [ ] Q4 **[why]** Why does two-line notation determine $\sigma$ but hide its cycle structure?

> [!tip]- Hints: where it lives, examples
> - Definition [[§10 Cycle Notation and the Group S₃#^def-10-1|§10.1]]; the six elements of $S_3$ in Example [[§10 Cycle Notation and the Group S₃#^ex-10-1|§10.1]].
> - Inverse: swap the rows and re-sort the columns.

#### Cycle notation · P2

$(a_1\,a_2\,\cdots\,a_r)$ is the permutation $a_1 \mapsto a_2 \mapsto \cdots \mapsto a_r \mapsto a_1$ fixing all else (an $r$-cycle; a $2$-cycle is a transposition); a cycle can start at any entry, see Definition [[§10 Cycle Notation and the Group S₃#^def-10-2|§10.2]]. *Source: WS 2 (cycle notation).*

^nd-def-10-2

- [ ] Q1 **[def]** Define an $r$-cycle and a transposition. Why is $(1\,2\,3) = (2\,3\,1)$?
- [ ] Q2 **[example]** Compute $(1\,2\,3)(2\,4)$ and $(1\,3)(2\,5\,4)(1\,2\,3\,5)$ by the tracking algorithm.
- [ ] Q3 **[example]** Compute $(1\,2\,3\,4\,5)^2$ without tracking.
- [ ] Q4 **[why]** Under the left-to-right convention, what would $(1\,2)(2\,3)$ be? Which convention does the course use?
- [ ] Q5 **[use]** What is the inverse of a cycle?

> [!tip]- Hints: where it lives, examples
> - Definition [[§10 Cycle Notation and the Group S₃#^def-10-2|§10.2]]; Example [[§12 Multiplying and Conjugating Cycles#^ex-12-1|§12.1]] ($(1\,2\,4\,3)$, $(1\,5\,3\,4\,2)$, $(1\,3\,5\,2\,4)$).
> - Remark [[§10 Cycle Notation and the Group S₃#^rem-10-1|Convention Warning]]: right factor first, $(1\,2)(2\,3) = (1\,2\,3)$.
> - Reverse the loop: Proposition [[§11 Disjoint Cycle Decomposition#^prop-11-4|§11.4]](1).

### Priority 4 · notes only (Pinter, MATH 412, not from class)

#### Disjoint cycles · P4

Cycles are disjoint if no element appears in two of them, see Definition [[§11 Disjoint Cycle Decomposition#^def-11-1|§11.1]]. *Source: notes (cf. Pinter Ch. 8).*

^nd-def-11-1

- [ ] Q1 **[def]** Define disjoint for two cycles and for a family.
- [ ] Q2 **[use]** State the two facts about disjoint cycles used everywhere (commuting; order).
- [ ] Q3 **[example]** Decompose $1 \mapsto 5, 2 \mapsto 2, 3 \mapsto 7, 4 \mapsto 1, 5 \mapsto 4, 6 \mapsto 3, 7 \mapsto 6$ into disjoint cycles, give its inverse and order.
- [ ] Q4 **[why]** Do $(1\,2)$ and $(2\,3)$ commute? What does this say about uniqueness of non-disjoint factorizations?

> [!tip]- Hints: where it lives, examples
> - Definition [[§11 Disjoint Cycle Decomposition#^def-11-1|§11.1]]; Lemma [[§11 Disjoint Cycle Decomposition#^lem-11-2|§11.2]], Proposition [[§11 Disjoint Cycle Decomposition#^prop-11-4|§11.4]].
> - Example [[§11 Disjoint Cycle Decomposition#^ex-11-1|§11.1]]: $(1\,5\,4)(3\,7\,6)$, inverse $(1\,4\,5)(3\,6\,7)$, order $3$.
> - Remark [[§12 Multiplying and Conjugating Cycles#^rem-12-1|Cycles Need Not Be Disjoint]].

## Proofs T3

### Priority 2 · worksheets and lectures

#### Subgroups of S₃ · P2

$S_3$ has exactly six subgroups: $\{e\}$, $\langle (1\,2) \rangle$, $\langle (1\,3) \rangle$, $\langle (2\,3) \rangle$, $\langle (1\,2\,3) \rangle$, $S_3$, of orders $1, 2, 2, 2, 3, 6$, see Proposition [[§13 The Symmetric Group S₃#^prop-13-1|§13.1]]. *Source: WS 1.7.*

^nd-prop-13-1

- [ ] Q1 **[state]** List the six subgroups with their orders.
- [ ] Q2 Step 1: show the product of two distinct transpositions in $S_3$ is a $3$-cycle.
- [ ] Q3 If $H$ contains no $3$-cycle, why is $H$ trivial or $\langle \tau \rangle$ for one transposition?
- [ ] Q4 If $H$ contains a $3$-cycle but no transposition, why is $H = \langle (1\,2\,3) \rangle$?
- [ ] Q5 If $H$ contains a $3$-cycle $\sigma$ and a transposition $\tau$, show $e, \sigma, \sigma^2, \tau, \tau\sigma, \tau\sigma^2$ are distinct.
- [ ] Q6 **[why]** The classification did not use Lagrange. How would Lagrange shorten it? Which of the six are normal?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G10 (compute in $S_3$), closure and cancellation.
> - $(x\,y)(x\,z) = (x\,z\,y)$.
> - $\tau\sigma^i = \sigma^j$ would make $\tau$ a power of $\sigma$: fixed-point count.
> - Remark [[§13 The Symmetric Group S₃#^rem-13-1|Preview of Lagrange]]; orders divide $6$ (G3).

### Priority 3 · filled in, using a technique the problem sets drill

#### Conjugation relabels a cycle · P3

$\sigma(a_1\,\cdots\,a_r)\sigma^{-1} = (\sigma(a_1)\,\cdots\,\sigma(a_r))$, so conjugation preserves cycle type, see Proposition [[§12 Multiplying and Conjugating Cycles#^prop-12-1|§12.1]]. *Source: notes (cf. Pinter Ch. 8); used constantly later.*

^nd-prop-12-1

- [ ] Q1 **[state]** State the formula and the consequence for cycle type.
- [ ] Q2 Evaluate $\sigma\tau\sigma^{-1}$ at $\sigma(a_i)$.
- [ ] Q3 Evaluate it at $y$ not of the form $\sigma(a_i)$.
- [ ] Q4 For a product of disjoint cycles, why does conjugating factor by factor work, and why do the relabelled cycles stay disjoint?
- [ ] Q5 **[why]** Compute $(1\,2)(2\,3)(1\,2)^{-1}$ with no multiplication. Where is this used later (conjugacy classes in $S_n$, $3$-cycles in a normal subgroup)?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G6 (conjugation preserves structure).
> - $(\sigma\tau\sigma^{-1})(\sigma(a_i)) = \sigma(a_{i+1})$; $\sigma^{-1}(y) \notin \{a_i\}$ is fixed by $\tau$.
> - $c_\sigma$ is a homomorphism (Proposition [[§18 Conjugation, Products, and Pointwise Products#^prop-18-1|§18.1]]); $\sigma$ injective.
> - Example [[§13 The Symmetric Group S₃#^ex-13-1|§13.1]]: $(1\,3)$.

### Priority 4 · notes only (Pinter, MATH 412, not from class)

#### An r-cycle has order r · P4

An $r$-cycle $(a_1\,\cdots\,a_r)$ has order $r$, see Lemma [[§11 Disjoint Cycle Decomposition#^lem-11-1|§11.1]]. *Source: notes (cf. Pinter Ch. 8).*

^nd-lem-11-1

- [ ] Q1 **[state]** State the lemma.
- [ ] Q2 What does $c^m$ do to $a_i$ and to elements outside the cycle? Prove it by induction.
- [ ] Q3 Why is $c^m \neq e$ for $0 < m < r$, and why is $c^r = e$?
- [ ] Q4 **[why]** What is the order of a product of two non-disjoint cycles, e.g. $(1\,2)(2\,3)$? Why does the lemma not apply?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: induction on $m$; indices mod $r$.
> - $c^m(a_1) = a_{1+m} \neq a_1$ for $0 < m < r$.
> - $(1\,2)(2\,3) = (1\,2\,3)$ has order $3$, not $\operatorname{lcm}(2,2)$.

#### Disjoint cycles commute · P4

If $c$ and $d$ are disjoint cycles then $cd = dc$, see Lemma [[§11 Disjoint Cycle Decomposition#^lem-11-2|§11.2]]. *Source: notes (cf. Pinter Ch. 8).*

^nd-lem-11-2

- [ ] Q1 **[state]** State the lemma.
- [ ] Q2 If $x$ is moved by $c$, why are $x$ and $c(x)$ both fixed by $d$? Compute $cd(x)$ and $dc(x)$.
- [ ] Q3 What about $x$ moved by neither?
- [ ] Q4 **[why]** Give two non-disjoint cycles that do not commute and two that do.

> [!tip]- Hints: route of the proof in the notes
> - Strategy: pointwise check on three kinds of $x$.
> - $c(x)$ lies in $c$'s loop, which $d$ does not touch.
> - $(1\,2)(2\,3) \neq (2\,3)(1\,2)$; but $(1\,2\,3)$ commutes with its square.

#### Disjoint cycle decomposition · P4

Every $\sigma \in S_n$ is a product of disjoint cycles, unique up to order of factors and starting points, see Theorem [[§11 Disjoint Cycle Decomposition#^thm-11-3|§11.3]]. *Source: cf. Pinter Ch. 8, Thm. 1.*

^nd-thm-11-3

- [ ] Q1 **[state]** State the theorem, with the uniqueness clause.
- [ ] Q2 Following $a, \sigma(a), \sigma^2(a), \ldots$: why must the sequence return to $a$ (not merely repeat)?
- [ ] Q3 Why are $a, \sigma(a), \ldots, \sigma^{r-1}(a)$ distinct, and why are two loops either equal or disjoint?
- [ ] Q4 Why is $\sigma = c_1 \cdots c_k$?
- [ ] Q5 Uniqueness: why is the loop through $a$ determined by $\sigma$?
- [ ] Q6 **[why]** Why does the theorem fail for $S_X$ with $X$ infinite?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: pigeonhole, then cancel (injectivity) to get $\sigma^{j-i}(a) = a$.
> - Each element has exactly one outgoing arrow, so overlapping loops coincide.
> - On each loop $\sigma$ agrees with $c_i$, other $c_j$ fix it; disjoint cycles commute (Lemma [[§11 Disjoint Cycle Decomposition#^lem-11-2|§11.2]]).
> - Remark [[§12 Multiplying and Conjugating Cycles#^rem-12-2|Finite Sets Only]]: the shift on $\mathbb{Z}$.

#### Computing with disjoint cycles · P4

For $\sigma = c_1 \cdots c_k$ disjoint of lengths $r_i$: $\sigma^{-1} = c_1^{-1} \cdots c_k^{-1}$ (each loop reversed), $\sigma^m = c_1^m \cdots c_k^m$, and $\operatorname{ord}(\sigma) = \operatorname{lcm}(r_1, \ldots, r_k)$, see Proposition [[§11 Disjoint Cycle Decomposition#^prop-11-4|§11.4]]. *Source: notes (cf. Pinter Ch. 8).*

^nd-prop-11-4

- [ ] Q1 **[state]** State the three parts.
- [ ] Q2 Why is $(c_1 \cdots c_k)^m = c_1^m \cdots c_k^m$? What fails for non-commuting factors?
- [ ] Q3 Why is $\sigma^m = e$ iff every $c_i^m = e$?
- [ ] Q4 Conclude the order is the lcm, using Lemma §11.1.
- [ ] Q5 **[why]** What are the orders of elements of $S_5$? Is there an element of order $6$ in $S_5$? Of order $6$ in $S_4$?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: disjoint supports separate the factors.
> - $c_i^m$ act on disjoint sets; $r_i \mid m$ for all $i$ iff $\operatorname{lcm} \mid m$ (Lemma [[§11 Disjoint Cycle Decomposition#^lem-11-1|§11.1]]).
> - $(1\,2)(3\,4\,5)$ has order $6$; $S_4$ has none.

#### Every permutation is a product of transpositions · P4

$(a_1\,a_2\,\cdots\,a_r) = (a_1\,a_r)(a_1\,a_{r-1})\cdots(a_1\,a_2)$, so every permutation is a product of transpositions, see Proposition [[§12 Multiplying and Conjugating Cycles#^prop-12-2|§12.2]]. *Source: cf. Pinter Ch. 8.*

^nd-prop-12-2

- [ ] Q1 **[state]** State the identity and the conclusion.
- [ ] Q2 Track $a_1$, then $a_i$ ($2 \leq i < r$), then $a_r$ through the product, right factor first.
- [ ] Q3 Why does the theorem on disjoint cycles finish the proof? What is the identity a product of?
- [ ] Q4 **[why]** Is the factorization unique? What about the number of factors? Which later result settles its parity?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: tracking algorithm; then G7 (generators).
> - $a_i \mapsto a_1$ under $(a_1\,a_i)$, then $\mapsto a_{i+1}$ under $(a_1\,a_{i+1})$.
> - Theorem [[§11 Disjoint Cycle Decomposition#^thm-11-3|§11.3]]; parity: Corollary [[§21 The Sign Homomorphism and the Alternating Group#^cor-21-4|§21.4]], remark [[§12 Multiplying and Conjugating Cycles#^rem-12-1|Cycles Need Not Be Disjoint]].

# T4. Homomorphisms and isomorphisms

## Definitions T4

### Priority 1 · problem sets (directly or extended)

#### Automorphisms and Aut(G) · P1

An automorphism of $G$ is an isomorphism $G \to G$; $\operatorname{Aut}(G)$ is a group under composition, a subgroup of $S_G$, see Definition [[§18 Conjugation, Products, and Pointwise Products#^def-18-1|§18.1]]. *Source: notes; [[Group Theory HW Drill#^ps1-2|PS1.2]].*

^nd-def-18-1

- [ ] Q1 **[def]** Define $\operatorname{Aut}(G)$ and its operation.
- [ ] Q2 **[use]** Why is $\operatorname{Aut}(G)$ a subgroup of $S_G$?
- [ ] Q3 **[example]** Give a non-identity automorphism of $\mathbb{Z}$ and of any abelian group.
- [ ] Q4 **[why]** Why is $g \mapsto g^{-1}$ an automorphism only for abelian $G$?

> [!tip]- Hints: where it lives, examples
> - Definition [[§18 Conjugation, Products, and Pointwise Products#^def-18-1|§18.1]]; Proposition [[§16 Isomorphisms#^prop-16-1|§16.1]], Proposition [[§16 Isomorphisms#^prop-16-2|§16.2]].
> - Inversion: Proposition [[§18 Conjugation, Products, and Pointwise Products#^prop-18-4|§18.4]](3).

#### Conjugation · P1

Conjugation by $a$ is $c_a : G \to G$, $c_a(g) = aga^{-1}$, see Definition [[§18 Conjugation, Products, and Pointwise Products#^def-18-2|§18.2]]. *Source: [[Group Theory HW Drill#^ps1-2|PS1.2]]; WS 3.*

^nd-def-18-2

- [ ] Q1 **[def]** Define $c_a$.
- [ ] Q2 **[use]** Show $c_a$ is a homomorphism. Which "trick" is used?
- [ ] Q3 **[example]** Compute $c_{(1\,2)}((2\,3))$ in $S_3$.
- [ ] Q4 **[why]** What is $c_a$ in an abelian group? What does $c_a \neq \operatorname{id}$ measure?

> [!tip]- Hints: where it lives, examples
> - Definition [[§18 Conjugation, Products, and Pointwise Products#^def-18-2|§18.2]]; Proposition [[§18 Conjugation, Products, and Pointwise Products#^prop-18-1|§18.1]] (insert $a^{-1}a$).
> - Proposition [[§12 Multiplying and Conjugating Cycles#^prop-12-1|§12.1]]; remark [[§18 Conjugation, Products, and Pointwise Products#^rem-18-1|Earlier Occurrences of Conjugation]].

#### Inner automorphism · P1

The maps $c_a$ are automorphisms, called the inner automorphisms of $G$, see Definition [[§18 Conjugation, Products, and Pointwise Products#^def-18-4|§18.4]]. *Source: [[Group Theory HW Drill#^ps1-2|PS1.2]]; notes.*

^nd-def-18-4

- [ ] Q1 **[def]** Define inner automorphism.
- [ ] Q2 **[use]** Of which homomorphism $G \to \operatorname{Aut}(G)$ are the inner automorphisms the image?
- [ ] Q3 **[example]** What are the inner automorphisms of an abelian group?
- [ ] Q4 **[why]** Is every automorphism inner? Consider $\mathbb{Z}/3\mathbb{Z}$.

> [!tip]- Hints: where it lives, examples
> - Definition [[§18 Conjugation, Products, and Pointwise Products#^def-18-4|§18.4]]; Proposition [[§18 Conjugation, Products, and Pointwise Products#^prop-18-1|§18.1]](3): $c_ac_b = c_{ab}$.
> - $\mathbb{Z}/3\mathbb{Z}$: only inner automorphism is $\operatorname{id}$, but $x \mapsto -x$ is an automorphism.

#### Hom(G, H) · P1

$\operatorname{Hom}(G, H)$ is the set of all homomorphisms $G \to H$, see Definition [[§18 Conjugation, Products, and Pointwise Products#^def-18-5|§18.5]]. *Source: [[Group Theory HW Drill#^ps1-3|PS1.3]].*

^nd-def-18-5

- [ ] Q1 **[def]** Define $\operatorname{Hom}(G, H)$.
- [ ] Q2 **[use]** When is $\operatorname{Hom}(G, H)$ a group under pointwise product?
- [ ] Q3 **[example]** Describe $\operatorname{Hom}(\mathbb{Z}, G)$ by where $1$ goes.
- [ ] Q4 **[why]** Why is $\operatorname{Hom}(G, H)$ never empty?

> [!tip]- Hints: where it lives, examples
> - Definition [[§18 Conjugation, Products, and Pointwise Products#^def-18-5|§18.5]]; Proposition [[§18 Conjugation, Products, and Pointwise Products#^prop-18-2|§18.2]] ($H$ abelian).
> - $k \mapsto g^k$: Proposition [[§17 Cyclic Groups#^prop-17-3|§17.3]](1); trivial homomorphism $g \mapsto e_H$.

#### Pointwise product · P1

For $\alpha, \beta \in \operatorname{Hom}(G, H)$, $(\alpha\beta)(g) = \alpha(g)\beta(g)$, see Definition [[§18 Conjugation, Products, and Pointwise Products#^def-18-6|§18.6]]. *Source: [[Group Theory HW Drill#^ps1-3|PS1.3]].*

^nd-def-18-6

- [ ] Q1 **[def]** Define the pointwise product.
- [ ] Q2 **[use]** Where exactly does commutativity of $H$ enter the proof that $\alpha\beta$ is a homomorphism?
- [ ] Q3 **[example]** What is $\operatorname{id} \cdot \operatorname{id}$? And $\pi_1 \cdot \pi_2$ on $G \times G$?
- [ ] Q4 **[why]** Give a non-homomorphic pointwise product in $S_3$.

> [!tip]- Hints: where it lives, examples
> - Definition [[§18 Conjugation, Products, and Pointwise Products#^def-18-6|§18.6]]; Proposition [[§18 Conjugation, Products, and Pointwise Products#^prop-18-2|§18.2]].
> - $\operatorname{id}\cdot\operatorname{id} = (g \mapsto g^2)$; $\pi_1 \cdot \pi_2 = \nabla$, remark [[§18 Conjugation, Products, and Pointwise Products#^rem-18-2|Relation between [[Group Theory HW Drill#^ps1-3-2|PS1.3(2)]] and [[Group Theory HW Drill#^ps1-4-3|PS1.4(3)]]]].

#### Structure maps of a product · P1

Projections $\pi_1, \pi_2$, inclusions $\iota_1(g) = (g, e_H)$, $\iota_2(h) = (e_G, h)$, diagonal $\Delta(g) = (g, g)$, multiplication $\nabla(g, h) = gh$, see Definition [[§18 Conjugation, Products, and Pointwise Products#^def-18-7|§18.7]]. *Source: [[Group Theory HW Drill#^ps1-4|PS1.4]].*

^nd-def-18-7

- [ ] Q1 **[def]** Define the six maps.
- [ ] Q2 **[use]** Which are always homomorphisms, which injective, which surjective?
- [ ] Q3 **[use]** State the componentwise criterion for $\varphi : K \to G \times H$ to be a homomorphism.
- [ ] Q4 **[why]** When is $\nabla$ a homomorphism? Give the evaluation that proves "only if".

> [!tip]- Hints: where it lives, examples
> - Definition [[§18 Conjugation, Products, and Pointwise Products#^def-18-7|§18.7]]; Proposition [[§18 Conjugation, Products, and Pointwise Products#^prop-18-3|§18.3]] ([[Group Theory HW Drill#^ps1-4-1|PS1.4(1)]]–(2)); Proposition [[§18 Conjugation, Products, and Pointwise Products#^prop-18-4|§18.4]] ([[Group Theory HW Drill#^ps1-4-3|PS1.4(3)]]).
> - $\nabla((g,h)(g,h)) = g^2h^2$ vs $(gh)^2$.

### Priority 2 · worksheets and lectures

#### Multiplication table · P2

For finite $G = \{g_1, \ldots, g_n\}$, the multiplication (Cayley) table has $g_ig_j$ in row $g_i$, column $g_j$; for composition, the column element is applied first, see Definition [[§14 Multiplication Tables#^def-14-1|§14.1]]. *Source: WS 2.*

^nd-def-14-1

- [ ] Q1 **[def]** State the definition and the row/column convention for $S_n$.
- [ ] Q2 **[use]** Why is every row and every column a permutation of $G$?
- [ ] Q3 **[use]** How do you read off from a table: abelian, the identity, inverses, elements of order $2$?
- [ ] Q4 **[example]** In the $S_3$ table, what is in row $(1\,2)$, column $(2\,3)$, and in row $(2\,3)$, column $(1\,2)$?
- [ ] Q5 **[why]** Why can a table "look like" another after relabelling? Which isomorphism does the $\mathbb{Z}/4\mathbb{Z}$ and $U_5$ pair illustrate?

> [!tip]- Hints: where it lives, examples
> - Definition [[§14 Multiplication Tables#^def-14-1|§14.1]]; Latin square property Corollary [[§2 First Consequences of the Axioms#^cor-2-8|§2.8]].
> - Example [[§14 Multiplication Tables#^ex-14-1|§14.1]] ($\mathbb{Z}/4\mathbb{Z}$, $U_5$); Example [[§14 Multiplication Tables#^ex-14-5|§14.5]] ($S_3$: $(1\,2\,3)$ and $(1\,3\,2)$).
> - Remark [[§16 Isomorphisms#^rem-16-5|Reading the Isomorphism off the Tables]].

#### Group homomorphism · P2

$\varphi : G \to H$ is a homomorphism if $\varphi(g_1g_2) = \varphi(g_1)\varphi(g_2)$ for all $g_1, g_2$, see Definition [[§15 Homomorphisms#^def-15-1|§15.1]]. *Source: WS 2.*

^nd-def-15-1

- [ ] Q1 **[def]** State the definition; which operation is on each side?
- [ ] Q2 **[example]** Check that $\det$, reduction $\mathbb{Z} \to \mathbb{Z}/n\mathbb{Z}$, $x \mapsto |x|$ on $\mathbb{R}^\times$, $x \mapsto 10^x$, and $k \mapsto 2^k$ on $\mathbb{Z}/4\mathbb{Z} \to U_5$ are homomorphisms.
- [ ] Q3 **[use]** Why need one not require $\varphi(e) = e$ and $\varphi(g^{-1}) = \varphi(g)^{-1}$ in the definition?
- [ ] Q4 **[why]** Is $g \mapsto g^2$ a homomorphism $S_3 \to S_3$? Is $g \mapsto g^{-1}$? When are they?
- [ ] Q5 **[use]** Is a composite of homomorphisms a homomorphism?

> [!tip]- Hints: where it lives, examples
> - Definition [[§15 Homomorphisms#^def-15-1|§15.1]]; Example [[§15 Homomorphisms#^ex-15-1|§15.1]]; Proposition [[§15 Homomorphisms#^prop-15-1|§15.1]] (WS 2.9).
> - Proposition [[§18 Conjugation, Products, and Pointwise Products#^prop-18-4|§18.4]]; Proposition [[§16 Isomorphisms#^prop-16-2|§16.2]](1).

#### Image · P2

$\operatorname{Im}(\varphi) = \{\varphi(g) : g \in G\} \subseteq H$, see Definition [[§15 Homomorphisms#^def-15-2|§15.2]]. *Source: WS 2.10.*

^nd-def-15-2

- [ ] Q1 **[def]** Define the image.
- [ ] Q2 **[example]** Image of $\det$ on $GL_n(\mathbb{R})$; of $\mathbb{Z}/6\mathbb{Z} \to U_7$, $k \mapsto 2^k$; of $x \mapsto 10^x$; of $\operatorname{sgn}$.
- [ ] Q3 **[use]** Why is the image a subgroup? When does it equal $H$?
- [ ] Q4 **[why]** Must the image be normal? (Think of $\langle (1\,2) \rangle \hookrightarrow S_3$.)

> [!tip]- Hints: where it lives, examples
> - Definition [[§15 Homomorphisms#^def-15-2|§15.2]]; Example [[§15 Homomorphisms#^ex-15-1|§15.1]], Example [[§15 Homomorphisms#^ex-15-2|§15.2]] ($\{1, 2, 4\}$).
> - Proposition [[§15 Homomorphisms#^prop-15-2|§15.2]]; remark [[§15 Homomorphisms#^rem-15-1|Kernels Are Normal: A Preview]].

#### Kernel · P2

$\operatorname{Ker}(\varphi) = \{g \in G : \varphi(g) = e_H\}$, see Definition [[§15 Homomorphisms#^def-15-3|§15.3]]. *Source: WS 2.10.*

^nd-def-15-3

- [ ] Q1 **[def]** Define the kernel.
- [ ] Q2 **[example]** Kernels of $\det$, of reduction mod $n$, of $x \mapsto |x|$ on $\mathbb{R}^\times$, of $\operatorname{sgn}$, of $k \mapsto g^k$.
- [ ] Q3 **[use]** State the injectivity criterion. Why does it not exist for arbitrary maps of sets?
- [ ] Q4 **[why]** In $\mathbb{Z}/6\mathbb{Z} \to U_7$, $k \mapsto 2^k$, compare $|\operatorname{Ker}|\,|\operatorname{Im}|$ with $|\mathbb{Z}/6\mathbb{Z}|$. Coincidence?
- [ ] Q5 **[use]** Why are kernels normal (preview)?

> [!tip]- Hints: where it lives, examples
> - Definition [[§15 Homomorphisms#^def-15-3|§15.3]]; Example [[§15 Homomorphisms#^ex-15-1|§15.1]]; $A_n = \operatorname{Ker}\operatorname{sgn}$, Definition [[§21 The Sign Homomorphism and the Alternating Group#^def-21-3|§21.3]]; $N\mathbb{Z}$, Proposition [[§17 Cyclic Groups#^prop-17-3|§17.3]](2).
> - Proposition [[§15 Homomorphisms#^prop-15-3|§15.3]]; remark [[§15 Homomorphisms#^rem-15-2|Kernel as the Measure of Non-Injectivity]].
> - Example [[§15 Homomorphisms#^ex-15-2|§15.2]]: $3 \cdot 2 = 6$ (G5, first isomorphism theorem later).

#### Isomorphism · P2

An isomorphism is a bijective homomorphism; $G \cong H$ if one exists, see Definition [[§16 Isomorphisms#^def-16-1|§16.1]]. *Source: WS 2.*

^nd-def-16-1

- [ ] Q1 **[def]** State the definition.
- [ ] Q2 **[use]** Why does the inverse automatically preserve the operation? Contrast with homeomorphisms.
- [ ] Q3 **[example]** Give three isomorphisms from the worksheets, and three pairs of equal-order non-isomorphic groups.
- [ ] Q4 **[why]** Why do matching invariants never prove $G \cong H$? What must be done instead?

> [!tip]- Hints: where it lives, examples
> - Definition [[§16 Isomorphisms#^def-16-1|§16.1]]; Proposition [[§16 Isomorphisms#^prop-16-1|§16.1]]; remark [[§16 Isomorphisms#^rem-16-1|Contrast with Topology]].
> - $\mathbb{Z}/4\mathbb{Z} \cong U_5$, $U_7 \cong \mathbb{Z}/6\mathbb{Z}$, $U_8 \cong (\mathbb{Z}/2\mathbb{Z})^2$, $\mathbb{R}^\times \cong \mathbb{R}_{>0} \times \mathbb{Z}/2\mathbb{Z}$; $S_3 \not\cong \mathbb{Z}/6\mathbb{Z}$, $U_8 \not\cong \mathbb{Z}/4\mathbb{Z}$.
> - Remark [[§16 Isomorphisms#^rem-16-3|Using Invariants]].

#### Commuting elements · P2

$g_1, g_2$ commute if $g_1g_2 = g_2g_1$; $G$ is commutative if all pairs commute, see Definition [[§16 Isomorphisms#^def-16-2|§16.2]]. *Source: WS 2.6.*

^nd-def-16-2

- [ ] Q1 **[def]** State the definition.
- [ ] Q2 **[example]** Which pairs of elements of $S_3$ commute?
- [ ] Q3 **[use]** How does "commutative" pass through an isomorphism?
- [ ] Q4 **[why]** If $g$ and $h_1$ commute and $gh_1 = h_2g$, what is $h_2$? Which later notion collects the elements commuting with everything?

> [!tip]- Hints: where it lives, examples
> - Definition [[§16 Isomorphisms#^def-16-2|§16.2]]; Proposition [[§16 Isomorphisms#^prop-16-3|§16.3]](1).
> - In $S_3$: an element commutes only with its own powers (and $e$ with all).
> - Proposition [[§2 First Consequences of the Axioms#^prop-2-1|§2.1]](2); centre $Z(G)$, Proposition [[§16 Isomorphisms#^prop-16-6|§16.6]].

#### Conjugate elements · P2

$g, g'$ are conjugate if $g' = aga^{-1}$ for some $a$, see Definition [[§18 Conjugation, Products, and Pointwise Products#^def-18-3|§18.3]]. *Source: WS 3 (conjugacy classes); notes.*

^nd-def-18-3

- [ ] Q1 **[def]** State the definition.
- [ ] Q2 **[use]** Why do conjugate elements have the same order?
- [ ] Q3 **[example]** Are $(1\,2)$ and $(1\,3)$ conjugate in $S_3$? Are $(1\,2)$ and $(1\,2\,3)$?
- [ ] Q4 **[why]** In an abelian group, what are the conjugates of $g$?

> [!tip]- Hints: where it lives, examples
> - Definition [[§18 Conjugation, Products, and Pointwise Products#^def-18-3|§18.3]]; Proposition [[§16 Isomorphisms#^prop-16-4|§16.4]](3) applied to $c_a$.
> - Cycle type: Proposition [[§12 Multiplying and Conjugating Cycles#^prop-12-1|§12.1]] (G6).

## Proofs T4

### Priority 1 · problem sets (directly or extended)

#### Further isomorphism invariants (centre, proper subgroups) · P1

An isomorphism maps central elements to central elements, $\varphi(Z(G)) = Z(H)$, and carries proper nontrivial subgroups to proper nontrivial subgroups, Proposition [[§16 Isomorphisms#^prop-16-6|§16.6]] → drilled as [[Group Theory HW Drill#^ps2-2|PS2.2]].

#### Conjugation is an automorphism · P1

$c_a$ is a homomorphism ([[Group Theory HW Drill#^ps1-2|PS1.2]]), an automorphism with inverse $c_{a^{-1}}$, and $c_ac_b = c_{ab}$, Proposition [[§18 Conjugation, Products, and Pointwise Products#^prop-18-1|§18.1]] → drilled as [[Group Theory HW Drill#^ps1-2|PS1.2]].

#### Pointwise products of homomorphisms · P1

If $H$ is abelian, $\operatorname{Hom}(G, H)$ is an abelian group under pointwise product; otherwise $g \mapsto g^2 = \operatorname{id}\cdot\operatorname{id}$ fails, Proposition [[§18 Conjugation, Products, and Pointwise Products#^prop-18-2|§18.2]] → drilled as [[Group Theory HW Drill#^ps1-3|PS1.3]].

#### The product and its universal property · P1

$G \times H$ is a group, abelian iff both factors are; projections and inclusions are homomorphisms; $\varphi : K \to G \times H$ is a homomorphism iff both components are; $\Delta$ is an injective homomorphism, Proposition [[§18 Conjugation, Products, and Pointwise Products#^prop-18-3|§18.3]] → drilled as [[Group Theory HW Drill#^ps1-4-1|PS1.4(1)]]–(2).

#### Characterizations of abelian groups · P1

$G$ is abelian iff $\nabla$ is a homomorphism iff inversion is iff squaring is, Proposition [[§18 Conjugation, Products, and Pointwise Products#^prop-18-4|§18.4]] → drilled as [[Group Theory HW Drill#^ps1-4-3|PS1.4(3)]] (squaring also in [[Group Theory HW Drill#^ps1-3-2|PS1.3(2)]]).

#### Characterizations of abelian groups, worksheet form · P1

$G$ is abelian iff $g \mapsto g^{-1}$ is a homomorphism, iff $g \mapsto g^2$ is, iff $\mu(g, h) = gh$ is a homomorphism $G \times G \to G$, see Proposition [[§18 Conjugation, Products, and Pointwise Products#^prop-18-5|§18.5]]. *Source: WS 3.4 (same as [[Group Theory HW Drill#^ps1-4-3|PS1.4(3)]] for $\mu = \nabla$).*

^nd-prop-18-5

- [ ] Q1 **[state]** State the three equivalences.
- [ ] Q2 (1): translate "inversion is a homomorphism" into an identity; why is it exactly commutativity (why do $g^{-1}, h^{-1}$ range over all of $G$)?
- [ ] Q3 (2): translate "squaring is a homomorphism" and cancel. On which sides?
- [ ] Q4 (3): the worksheet route specializes $\mu((g,h)(g',h')) = \mu(g,h)\mu(g',h')$; which specialization gives $g'h = hg'$? (The evaluation at $(g,h), (g,h)$ is drilled as [[Group Theory HW Drill#^ps1-4-3|PS1.4(3)]].)
- [ ] Q5 **[why]** Give one pair in $S_3$ that breaks all three maps at once.

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G10 for the counterexample; cancellation.
> - $(gh)^{-1} = h^{-1}g^{-1}$ always (Proposition [[§2 First Consequences of the Axioms#^prop-2-4|§2.4]]).
> - $ghgh = gghh \Rightarrow hg = gh$.
> - $g = e$, $h' = e$; $g = (1\,2)$, $h = (2\,3)$; same as Proposition [[§18 Conjugation, Products, and Pointwise Products#^prop-18-4|§18.4]].

### Priority 2 · worksheets and lectures

#### Table of ℤ/6ℤ · P2

The addition table of $\mathbb{Z}/6\mathbb{Z}$: each row is the previous one shifted left; it is symmetric and $0$ sits in row $a$ at column $6 - a$, see Example [[§14 Multiplication Tables#^ex-14-2|§14.2]]. *Source: WS 2.1.*

^nd-ex-14-2

- [ ] Q1 **[state]** Write out the table.
- [ ] Q2 How does the table show the group is abelian, and where are the inverses?
- [ ] Q3 Which elements have order $1, 2, 3, 6$? Which generate?
- [ ] Q4 **[why]** Compare with the $S_3$ table: which visible feature already shows $S_3 \not\cong \mathbb{Z}/6\mathbb{Z}$?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G14 (arithmetic mod $6$).
> - Generators $1, 5$ ($\varphi(6) = 2$), Corollary [[§17 Cyclic Groups#^cor-17-6|§17.6]].
> - Symmetry of the table; Proposition [[§16 Isomorphisms#^prop-16-3|§16.3]](1).

#### Table of U₇ · P2

The multiplication table of $U_7$ is symmetric and the position of $1$ in each row gives the inverse: $2^{-1} = 4$, $3^{-1} = 5$, $6^{-1} = 6$, see Example [[§14 Multiplication Tables#^ex-14-3|§14.3]]. *Source: WS 2.2.*

^nd-ex-14-3

- [ ] Q1 **[state]** Write out the table.
- [ ] Q2 Read off all inverses and the elements of order $2$.
- [ ] Q3 Read the row of $3$ as successive powers: what do you find? And the row of $2$?
- [ ] Q4 **[why]** Why does the table prove $U_7$ is cyclic, i.e. $U_7 \cong \mathbb{Z}/6\mathbb{Z}$?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G14; G10.
> - $3$ has order $6$, $2$ has order $3$: remark [[§16 Isomorphisms#^rem-16-6|Reading Cyclicity off a Table]], Proposition [[§16 Isomorphisms#^prop-16-8|§16.8]](2).

#### Table of U₈ · P2

The multiplication table of $U_8 = \{1, 3, 5, 7\}$ is symmetric with diagonal all $1$: every element is its own inverse, see Example [[§14 Multiplication Tables#^ex-14-4|§14.4]]. *Source: WS 2.3.*

^nd-ex-14-4

- [ ] Q1 **[state]** Write out the table.
- [ ] Q2 What does the diagonal show?
- [ ] Q3 Compute $3 \cdot 5$, $3 \cdot 7$, $5 \cdot 7$ mod $8$. What pattern (product of two non-identity elements) appears?
- [ ] Q4 **[why]** Why is $U_8$ not cyclic, although $|U_8| = |U_5| = 4$?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G14; G10.
> - Product of two distinct non-identity elements is the third: Klein four-group, Proposition [[§16 Isomorphisms#^prop-16-8|§16.8]](1).
> - No element of order $4$, Corollary [[§17 Cyclic Groups#^cor-17-2|§17.2]].

#### Table of S₃ · P2

With rows and columns ordered $e, (1\,2), (1\,3), (2\,3), (1\,2\,3), (1\,3\,2)$ and the column element applied first, the table of $S_3$ is not symmetric, see Example [[§14 Multiplication Tables#^ex-14-5|§14.5]]. *Source: WS 2.4.*

^nd-ex-14-5

- [ ] Q1 **[state]** Fill in the row of $(1\,2)$ and the row of $(1\,2\,3)$.
- [ ] Q2 State the convention: which element is applied first, row or column?
- [ ] Q3 Where does $e$ appear on the diagonal and where off it? What does this say about inverses?
- [ ] Q4 Which $2 \times 2$ or $3 \times 3$ blocks show closed subsets (subgroups)?
- [ ] Q5 **[why]** Which entry pair proves non-commutativity? What would change under the left-to-right convention?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G10 (compute in $S_3$) by tracking, right factor first.
> - Row $(1\,2)$: $(1\,2), e, (1\,3\,2), (1\,2\,3), (2\,3), (1\,3)$.
> - Same table in Example [[§10 Cycle Notation and the Group S₃#^ex-10-1|§10.1]]; remark [[§10 Cycle Notation and the Group S₃#^rem-10-1|Convention Warning]].

#### Homomorphisms preserve identity and inverses · P2

$\varphi(e_G) = e_H$ and $\varphi(g^{-1}) = \varphi(g)^{-1}$, see Proposition [[§15 Homomorphisms#^prop-15-1|§15.1]]. *Source: WS 2.9.*

^nd-prop-15-1

- [ ] Q1 **[state]** State the proposition.
- [ ] Q2 Prove $\varphi(e_G) = e_H$: which equation in $H$ do you cancel?
- [ ] Q3 Prove $\varphi(g^{-1}) = \varphi(g)^{-1}$: which result lets one equation suffice?
- [ ] Q4 **[why]** For a map between monoids preserving products, can $\varphi(e)$ fail to be the identity? Why does the group case work?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: cancellation, then one-sided inverses.
> - $\varphi(e) = \varphi(e)\varphi(e)$, cancel (Proposition [[§2 First Consequences of the Axioms#^prop-2-1|§2.1]]).
> - $\varphi(g)\varphi(g^{-1}) = e_H$, Proposition [[§2 First Consequences of the Axioms#^prop-2-6|§2.6]].
> - E.g. the zero map $(\mathbb{Z}, \times) \to (\mathbb{Z}, \times)$ sends $1 \mapsto 0$.

#### Image and kernel are subgroups · P2

$\operatorname{Im}(\varphi) \leq H$ and $\operatorname{Ker}(\varphi) \leq G$, see Proposition [[§15 Homomorphisms#^prop-15-2|§15.2]]. *Source: WS 2.10.*

^nd-prop-15-2

- [ ] Q1 **[state]** State the proposition (note: the worksheet's "subgroup of $G$" for the image is a typo for $H$).
- [ ] Q2 Image: check identity, inverses, products. Which part of WS 2.9 is used?
- [ ] Q3 Kernel: check the three conditions.
- [ ] Q4 **[why]** Which kernel is $A_n$, which is $SL_n(\mathbb{R})$, which is $n\mathbb{Z}$? Is the image of a homomorphism always normal?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G1 with Proposition [[§15 Homomorphisms#^prop-15-1|§15.1]].
> - $\varphi(g)\varphi(g') = \varphi(gg')$; $\varphi(gg') = e_He_H$.
> - Generalization: Proposition [[§15 Homomorphisms#^prop-15-4|§15.4]].

#### Images and preimages of subgroups · P2

For $G' \leq G$, $\varphi(G') \leq H$; for $H' \leq H$, $\varphi^{-1}(H') \leq G$; if $\varphi$ is injective, $G' \to \varphi(G')$ is an isomorphism and $G' \mapsto \varphi(G')$ is injective on subgroups, see Proposition [[§15 Homomorphisms#^prop-15-4|§15.4]]. *Source: notes; WS 6 later.*

^nd-prop-15-4

- [ ] Q1 **[state]** State the three parts.
- [ ] Q2 Prove (1) by the three conditions.
- [ ] Q3 Prove (2). Which special case gives the kernel?
- [ ] Q4 Prove (3): why is $\varphi(G_1') = \varphi(G_2')$ enough to get $G_1' = G_2'$?
- [ ] Q5 **[why]** Where is (3) used to transport subgroup lattices through isomorphisms?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G1; G9 later (correspondence).
> - $\varphi(g_1')\varphi(g_2') = \varphi(g_1'g_2')$; $\varphi(g_1g_2) \in H'$ as $H'$ is a subgroup.
> - Used in Proposition [[§16 Isomorphisms#^prop-16-6|§16.6]](2) ([[Group Theory HW Drill#^ps2-2|PS2.2]]).

#### Two isomorphism invariants · P2

If $G \cong H$ and $G$ is commutative, so is $H$; if $g^2 = e$ for all $g \in G$, then $h^2 = e$ for all $h \in H$; hence $S_3 \not\cong \mathbb{Z}/6\mathbb{Z}$ and $\mathbb{Z}/4\mathbb{Z} \not\cong \mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/2\mathbb{Z}$, see Proposition [[§16 Isomorphisms#^prop-16-3|§16.3]]. *Source: WS 2.6.*

^nd-prop-16-3

- [ ] Q1 **[state]** State the two invariants and the two consequences.
- [ ] Q2 What is the general method for proving two groups are not isomorphic?
- [ ] Q3 Prove (1) by contradiction using $\varphi^{-1}$.
- [ ] Q4 Prove (2) for $h = \varphi(g)$.
- [ ] Q5 Deduce the two consequences; which elements witness each failure?
- [ ] Q6 **[why]** Give a third invariant that also separates $S_3$ from $\mathbb{Z}/6\mathbb{Z}$.

> [!tip]- Hints: route of the proof in the notes
> - Strategy: transport a property through $\varphi$ or $\varphi^{-1}$.
> - $\varphi^{-1}(h_1h_2) = \varphi^{-1}(h_2h_1)$, then injectivity.
> - $h^2 = \varphi(g^2) = \varphi(e_G) = e_H$; $1 + 1 = 2 \neq 0$ in $\mathbb{Z}/4\mathbb{Z}$.
> - Centre sizes $6$ vs $1$ (remark [[§16 Isomorphisms#^rem-16-4|Using These to Distinguish Groups]]); an element of order $6$ (Proposition [[§16 Isomorphisms#^prop-16-5|§16.5]]).

#### Isomorphism invariants · P2

An isomorphism preserves $|G|$, abelianness, the sets $\{g : g^n = e\}$ (bijectively), the number of elements of each order, and cyclicity ($G = \langle g \rangle$ iff $H = \langle \varphi(g) \rangle$), see Proposition [[§16 Isomorphisms#^prop-16-5|§16.5]]. *Source: notes; isomorphism invariants were the topic of class on Fri Sept 4 (course log).*

^nd-prop-16-5

- [ ] Q1 **[state]** List the five invariants.
- [ ] Q2 Prove (3) using Proposition §16.4 for $\varphi$ and $\varphi^{-1}$.
- [ ] Q3 Prove (5).
- [ ] Q4 Use (4) to show $U_8 \not\cong \mathbb{Z}/4\mathbb{Z}$ and $U_{15} \not\cong \mathbb{Z}/8\mathbb{Z}$.
- [ ] Q5 **[why]** Do $\mathbb{Z}/4\mathbb{Z} \times \mathbb{Z}/2\mathbb{Z}$ and $\mathbb{Z}/8\mathbb{Z}$ share invariant (1)? Which invariant separates them?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: transport through $\varphi$ and $\varphi^{-1}$.
> - Proposition [[§16 Isomorphisms#^prop-16-4|§16.4]](3); $h = \varphi(g^k) = \varphi(g)^k$.
> - Remark [[§16 Isomorphisms#^rem-16-3|Using Invariants]]; $U_{15} \cong \mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/4\mathbb{Z}$ (Example [[§22 The Structure of Uₙ#^ex-22-1|§22.1]]) has no element of order $8$.

#### ℤ/4ℤ ≅ U₅ · P2

$\varphi : \mathbb{Z}/4\mathbb{Z} \to U_5$, $k \mapsto 2^k$ is an isomorphism ($0, 1, 2, 3 \mapsto 1, 2, 4, 3$), see Proposition [[§16 Isomorphisms#^prop-16-7|§16.7]]. *Source: WS 2.5.*

^nd-prop-16-7

- [ ] Q1 **[state]** State the isomorphism with its values.
- [ ] Q2 Well-defined: what must hold when $k' = k + 4m$, and which congruence gives it? Why do the values lie in $U_5$?
- [ ] Q3 Homomorphism: which operation is on each side?
- [ ] Q4 Bijective: why does listing values suffice?
- [ ] Q5 **[why]** Why would $k \mapsto 4^k$ fail to be an isomorphism (and is it even well defined)? What does the classification of cyclic groups say about this example?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G2 (well-definedness), then G14.
> - $2^4 = 16 \equiv 1 \pmod 5$: Lemma [[§7 The Group ℤ∕nℤ#^lem-7-2|§7.2]].
> - $4^k$ is well defined ($4^4 \equiv 1$) but $4$ has order $2$: image $\{1, 4\}$.
> - Remark [[§17 Cyclic Groups#^rem-17-1|WS 2.5 and WS 2.7(2) as Instances]].

#### U₈ and U₇ · P2

$U_8 \cong \mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/2\mathbb{Z}$, hence $U_8 \not\cong \mathbb{Z}/4\mathbb{Z}$; and $U_7 \cong \mathbb{Z}/6\mathbb{Z}$ via $k \mapsto 3^k$, see Proposition [[§16 Isomorphisms#^prop-16-8|§16.8]]. *Source: WS 2.7.*

^nd-prop-16-8

- [ ] Q1 **[state]** Answer both questions of WS 2.7 with the maps.
- [ ] Q2 Give the bijection $U_8 \to (\mathbb{Z}/2\mathbb{Z})^2$. Why does checking unordered pairs suffice for the homomorphism property?
- [ ] Q3 Give the direct one-line proof that $U_8 \not\cong \mathbb{Z}/4\mathbb{Z}$.
- [ ] Q4 List the powers of $3$ mod $7$. Why is $k \mapsto 3^k$ well defined on $\mathbb{Z}/6\mathbb{Z}$?
- [ ] Q5 **[why]** Why does $2$ not work in place of $3$ for $U_7$?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G10, G2; invariants (Proposition [[§16 Isomorphisms#^prop-16-3|§16.3]](2)).
> - $1, 3, 5, 7 \mapsto (0,0), (1,0), (0,1), (1,1)$; both groups abelian.
> - $3^6 \equiv 1$; $3^k$: $1, 3, 2, 6, 4, 5$.
> - $2$ has order $3$: Example [[§15 Homomorphisms#^ex-15-2|§15.2]].

#### Structure of ℝ^× and ℚ^× · P2

$\mathbb{R}^\times \cong \mathbb{R}_{>0} \times \mathbb{Z}/2\mathbb{Z}$ and $\mathbb{Q}^\times \cong \mathbb{Z}^{\oplus\infty} \times \mathbb{Z}/2\mathbb{Z}$, see Proposition [[§16 Isomorphisms#^prop-16-9|§16.9]]. *Source: WS 2.8.*

^nd-prop-16-9

- [ ] Q1 **[state]** State both isomorphisms; define $\mathbb{Z}^{\oplus\infty}$.
- [ ] Q2 For $\mathbb{R}^\times$: define $\varphi(x) = (|x|, s(x))$. Why is $s(xy) = s(x) + s(y)$ in $\mathbb{Z}/2\mathbb{Z}$? Give the inverse map.
- [ ] Q3 For $\mathbb{Q}^\times$: which theorem gives the unique expression $q = \pm \prod p_i^{a_i}$ with $a_i \in \mathbb{Z}$?
- [ ] Q4 Why is $q \mapsto ((a_i), s(q))$ a homomorphism, injective, and surjective?
- [ ] Q5 **[why]** Why must only finitely many $a_i$ be nonzero, i.e. why not all integer sequences?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: split into "size" and "sign".
> - "Negative times negative is positive" is $[1] + [1] = [0]$.
> - Theorem [[§9 Euclid's Lemma, Unique Factorization, and the Chinese Remainder Theorem#^thm-9-2|§9.2]], extended by clearing denominators.
> - A rational has finitely many prime factors. Remark [[§16 Isomorphisms#^rem-16-7|Interpretation]].

#### Classification of cyclic groups · P2

If $G = \langle g \rangle$ with $\operatorname{ord}(g) = n$, then $G = \{e, \ldots, g^{n-1}\}$ and $\mathbb{Z}/n\mathbb{Z} \to G$, $k \mapsto g^k$ is an isomorphism; if $g$ has infinite order, $\mathbb{Z} \to G$, $k \mapsto g^k$ is an isomorphism; cyclic groups are isomorphic iff they have the same order, see Theorem [[§17 Cyclic Groups#^thm-17-1|§17.1]]. *Source: cf. MATH 412; WS 3.1 is the worksheet form.*

^nd-thm-17-1

- [ ] Q1 **[state]** State the theorem in both cases and the consequence.
- [ ] Q2 Why is $\varphi(k) = g^k$ a surjective homomorphism $\mathbb{Z} \to G$?
- [ ] Q3 Finite case: show $\operatorname{Ker}\varphi = n\mathbb{Z}$.
- [ ] Q4 Descend to $\mathbb{Z}/n\mathbb{Z}$ and show the result is injective.
- [ ] Q5 Infinite case: why are the powers pairwise distinct?
- [ ] Q6 **[why]** Deduce $\operatorname{ord}(g) = |\langle g \rangle|$. Why does this show $U_8$ is not cyclic?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G5 (kernel) and G2 (descent); G14 for the kernel.
> - $k = qn + r$, $g^k = g^r$; minimality of $n$.
> - Lemma [[§7 The Group ℤ∕nℤ#^lem-7-2|§7.2]]; Proposition [[§15 Homomorphisms#^prop-15-3|§15.3]].
> - $g^k = g^l$, $k < l$ gives $g^{l-k} = e$.

#### The homomorphism k ↦ gᵏ and ⟨g⟩ ≅ ℤ/Nℤ · P2

$\varphi_g : \mathbb{Z} \to G$, $k \mapsto g^k$ is a homomorphism; if $\operatorname{ord}(g) = N$ then $\operatorname{Ker}\varphi_g = N\mathbb{Z}$ and $\langle g \rangle \cong \mathbb{Z}/N\mathbb{Z}$ via $[k] \mapsto g^k$; if $g$ has infinite order, $\operatorname{Ker}\varphi_g = \{0\}$ and $\langle g \rangle \cong \mathbb{Z}$, see Proposition [[§17 Cyclic Groups#^prop-17-3|§17.3]]. *Source: WS 3.1.*

^nd-prop-17-3

- [ ] Q1 **[state]** State the four parts (including the modification for infinite order).
- [ ] Q2 (1): which exponent law? What is the image?
- [ ] Q3 (2): prove $g^k = e$ iff $N \mid k$.
- [ ] Q4 (3): prove well-definedness of $[k] \mapsto g^k$ directly, then injectivity.
- [ ] Q5 (4): why is the kernel $\{0\}$ when $g$ has infinite order?
- [ ] Q6 **[why]** In what sense is "infinite order" the same as "order $0$" here?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G5, G2, G14.
> - $g^{k + Nm} = g^k(g^N)^m = g^k$; Lemma [[§7 The Group ℤ∕nℤ#^lem-7-2|§7.2]].
> - $g^k = e$ with $k \neq 0$ gives $g^{|k|} = e$.
> - $\mathbb{Z}/0\mathbb{Z} = \mathbb{Z}$; remark [[§17 Cyclic Groups#^rem-17-2|Relation to the Classification]].

### Priority 3 · filled in, using a technique the problem sets drill

#### Homomorphisms and orders of elements · P3

$\varphi(g^k) = \varphi(g)^k$; if $\operatorname{ord}(g) = n$ then $\operatorname{ord}(\varphi(g)) \mid n$; if $\varphi$ is injective, $\varphi(g)$ has the same order as $g$, see Proposition [[§16 Isomorphisms#^prop-16-4|§16.4]]. *Source: notes.*

^nd-prop-16-4

- [ ] Q1 **[state]** State the three parts.
- [ ] Q2 Prove (1) for $k \geq 0$ and for $k < 0$.
- [ ] Q3 Prove (2): why does $\varphi(g)$ have finite order $d \leq n$, and why $d \mid n$?
- [ ] Q4 Prove (3): compare the sets $\{k \geq 1 : g^k = e\}$ and $\{k \geq 1 : \varphi(g)^k = e\}$.
- [ ] Q5 **[why]** Is there a nontrivial homomorphism $\mathbb{Z}/3\mathbb{Z} \to \mathbb{Z}/4\mathbb{Z}$? Why must $\varphi(g)$ have order dividing both?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: division algorithm on exponents (G14), G3 flavour.
> - $n = qd + r$, $e = \varphi(g)^n = \varphi(g)^r$, so $r = 0$.
> - Injectivity: $\varphi(g)^k = \varphi(e)$ iff $g^k = e$.

#### Cyclic iff there is an element of order |G| · P3

A group of finite order $n$ is cyclic iff it has an element of order $n$; those elements are exactly the generators, see Corollary [[§17 Cyclic Groups#^cor-17-2|§17.2]]. *Source: notes; cf. MATH 412.*

^nd-cor-17-2

- [ ] Q1 **[state]** State the corollary.
- [ ] Q2 Which identity from the classification is the key?
- [ ] Q3 Prove both directions.
- [ ] Q4 **[why]** Why does the argument need $G$ finite? Is $\mathbb{Q}$ cyclic, although it has elements of infinite order?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G3 flavour (counting).
> - $\operatorname{ord}(g) = |\langle g \rangle|$ (Theorem [[§17 Cyclic Groups#^thm-17-1|§17.1]]); a subset with $|G|$ elements is $G$.
> - $\mathbb{Q}$: $\langle a/b \rangle$ misses $a/(2b)$.

#### Generators and subgroups of a finite cyclic group · P3

In $G = \langle g \rangle$ of order $n$: $g^k$ generates iff $\gcd(k, n) = 1$ (so there are $\varphi(n)$ generators); for each $d \mid n$ there is exactly one subgroup of order $d$, $\langle g^{n/d} \rangle$, and no others, see Corollary [[§17 Cyclic Groups#^cor-17-6|§17.6]]. *Source: cf. Pinter Ch. 11.*

^nd-cor-17-6

- [ ] Q1 **[state]** State both parts.
- [ ] Q2 Prove (1) from the order of a power.
- [ ] Q3 Existence in (2): compute $\operatorname{ord}(g^{n/d})$.
- [ ] Q4 Uniqueness in (2): if $|H| = d$, why is $H = \langle g^m \rangle$ with $m \mid n$, and why $m = n/d$?
- [ ] Q5 **[example]** List the subgroups and generators of $\mathbb{Z}/12\mathbb{Z}$.
- [ ] Q6 **[why]** Why are there no subgroups of other orders? Does a non-cyclic group of order $4$ have a unique subgroup of order $2$?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G14, G3 (Lagrange for "no other orders").
> - Proposition [[§17 Cyclic Groups#^prop-17-5|§17.5]], Corollary [[§17 Cyclic Groups#^cor-17-2|§17.2]], Theorem [[§17 Cyclic Groups#^thm-17-4|§17.4]] ($g^n = e \in H$ gives $m \mid n$).
> - Example [[§17 Cyclic Groups#^ex-17-1|§17.1]]; $U_8$ has three subgroups of order $2$.

### Priority 4 · notes only (Pinter, MATH 412, not from class)

#### Injectivity via the kernel · P4

$\varphi$ is injective iff $\operatorname{Ker}\varphi = \{e_G\}$; surjective iff $\operatorname{Im}\varphi = H$; hence an isomorphism iff both, see Proposition [[§15 Homomorphisms#^prop-15-3|§15.3]]. *Source: notes.*

^nd-prop-15-3

- [ ] Q1 **[state]** State the three parts.
- [ ] Q2 Prove ($\Rightarrow$) of (2).
- [ ] Q3 Prove ($\Leftarrow$): rewrite $\varphi(g_1) = \varphi(g_2)$ as a statement about the kernel.
- [ ] Q4 **[why]** Is $\mathbb{Z}/6\mathbb{Z} \to U_7$, $k \mapsto 2^k$ injective? Read it off from the kernel.

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G5 (kernels).
> - $\varphi(g_1g_2^{-1}) = \varphi(g_1)\varphi(g_2)^{-1} = e_H$.
> - Example [[§15 Homomorphisms#^ex-15-2|§15.2]]: kernel $\{0, 3\}$; remark [[§15 Homomorphisms#^rem-15-2|Kernel as the Measure of Non-Injectivity]].

#### The inverse of an isomorphism is an isomorphism · P4

If $\varphi : G \to H$ is a bijective homomorphism, $\varphi^{-1}$ is a homomorphism, see Proposition [[§16 Isomorphisms#^prop-16-1|§16.1]]. *Source: notes.*

^nd-prop-16-1

- [ ] Q1 **[state]** State the proposition.
- [ ] Q2 Put $g_i = \varphi^{-1}(h_i)$. Compute $\varphi(g_1g_2)$ and apply $\varphi^{-1}$.
- [ ] Q3 **[why]** Why does the analogous statement fail for continuous bijections? Give the example.
- [ ] Q4 Where is the proposition used (symmetry of $\cong$; WS 2.6(1))?

> [!tip]- Hints: route of the proof in the notes
> - $\varphi(g_1g_2) = h_1h_2$, so $\varphi^{-1}(h_1h_2) = g_1g_2$.
> - Remark [[§16 Isomorphisms#^rem-16-1|Contrast with Topology]]: $[0, 2\pi) \to S^1$.
> - Proposition [[§16 Isomorphisms#^prop-16-2|§16.2]], Proposition [[§16 Isomorphisms#^prop-16-3|§16.3]].

#### Composition; ≅ is an equivalence relation · P4

Composites of homomorphisms (isomorphisms) are homomorphisms (isomorphisms), and $\cong$ is reflexive, symmetric and transitive, see Proposition [[§16 Isomorphisms#^prop-16-2|§16.2]]. *Source: notes.*

^nd-prop-16-2

- [ ] Q1 **[state]** State both parts.
- [ ] Q2 Prove that $\psi \circ \varphi$ is a homomorphism.
- [ ] Q3 Which result gives each of reflexivity, symmetry, transitivity?
- [ ] Q4 **[why]** How is transitivity used to get $U_8 \not\cong \mathbb{Z}/4\mathbb{Z}$ from $U_8 \cong (\mathbb{Z}/2\mathbb{Z})^2$?

> [!tip]- Hints: route of the proof in the notes
> - $\psi(\varphi(g_1g_2)) = \psi(\varphi(g_1))\psi(\varphi(g_2))$.
> - Identity map; Proposition [[§16 Isomorphisms#^prop-16-1|§16.1]]; part (1).
> - Proposition [[§16 Isomorphisms#^prop-16-8|§16.8]](1).

#### Subgroups of cyclic groups are cyclic · P4

If $G = \langle g \rangle$ and $H \leq G$, $H \neq \{e\}$, then $H = \langle g^m \rangle$ with $m$ the least positive exponent with $g^m \in H$, and every $t$ with $g^t \in H$ is a multiple of $m$, see Theorem [[§17 Cyclic Groups#^thm-17-4|§17.4]]. *Source: cf. Pinter Ch. 11; MATH 412.*

^nd-thm-17-4

- [ ] Q1 **[state]** State the theorem.
- [ ] Q2 Why does $H$ contain a positive power of $g$? Define $m$.
- [ ] Q3 Given $g^t \in H$, divide $t$ by $m$; why is $g^r \in H$, and why $r = 0$?
- [ ] Q4 **[why]** Which earlier result is the case $G = \mathbb{Z}$? Why is cyclicity of $G$ needed? Give a non-cyclic subgroup of an abelian group.

> [!tip]- Hints: route of the proof in the notes
> - Strategy: smallest positive exponent plus division algorithm (G14).
> - $g^r = g^t(g^m)^{-q} \in H$.
> - Proposition [[§5 A Zoo of Subgroups#^prop-5-1|§5.1]]; the checkerboard $\langle (1,1), (1,-1) \rangle \leq \mathbb{Z}^2$ (Example [[§5 A Zoo of Subgroups#^ex-5-1|§5.1]]) is not cyclic.

#### The order of a power · P4

If $\operatorname{ord}(g) = n$ then $\operatorname{ord}(g^k) = n/\gcd(n, k)$, see Proposition [[§17 Cyclic Groups#^prop-17-5|§17.5]]. *Source: cf. Pinter Ch. 10, Ex. F.*

^nd-prop-17-5

- [ ] Q1 **[state]** State the formula.
- [ ] Q2 Write $n = dn'$, $k = dk'$. Why is $(g^k)^m = e$ iff $n \mid km$?
- [ ] Q3 Why is $n \mid km$ iff $n' \mid m$? Which lemma?
- [ ] Q4 **[example]** Orders of $[8]$ in $\mathbb{Z}/12\mathbb{Z}$, of $(1\,2\,3\,4\,5\,6)^4$, of $3^2$ in $U_7$.
- [ ] Q5 **[why]** What goes wrong if one forgets $\gcd(n', k') = 1$?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G14.
> - Exponents killing $g$ are $n\mathbb{Z}$ (Proposition [[§17 Cyclic Groups#^prop-17-3|§17.3]](2)); Euclid's lemma Lemma [[§9 Euclid's Lemma, Unique Factorization, and the Chinese Remainder Theorem#^lem-9-1|§9.1]].
> - $12/\gcd(12, 8) = 3$; $6/\gcd(6, 4) = 3$; $6/2 = 3$.

# T5. Signs, matrices and unit groups

## Definitions T5

### Priority 1 · problem sets (directly or extended)

#### Polynomial ring in several variables · P1

$k[x_1, \ldots, x_n]$ is the set of finite $k$-linear combinations of monomials $x_1^{a_1} \cdots x_n^{a_n}$, equal iff all coefficients agree, with coefficientwise addition and multiplication by expanding, see Definition [[§20 Polynomial Rings, Permutation Matrices, and Representations#^def-20-1|§20.1]]. *Source: [[Group Theory HW Drill#^ps1-5|PS1.5]]; notes.*

^nd-def-20-1

- [ ] Q1 **[def]** Define a monomial and a polynomial; when are two polynomials equal?
- [ ] Q2 **[example]** Write $\Delta$ for $n = 3$ and expand $(x_1 - x_2)(x_1 - x_3)$.
- [ ] Q3 **[use]** Why can the notes divide $\sigma \cdot \Delta$ by $\Delta$?
- [ ] Q4 **[why]** Why are polynomials treated as formal expressions, not functions? (Think of $x^p - x$ over $\mathbb{F}_p$.)

> [!tip]- Hints: where it lives, examples
> - Definition [[§20 Polynomial Rings, Permutation Matrices, and Representations#^def-20-1|§20.1]]; remark [[§20 Polynomial Rings, Permutation Matrices, and Representations#^rem-20-1|k as a Ring]].
> - $\sigma \cdot \Delta = \pm \Delta$ with $\Delta \neq 0$: Theorem [[§21 The Sign Homomorphism and the Alternating Group#^thm-21-2|§21.2]].
> - Over $\mathbb{F}_p$ the nonzero polynomial $x^p - x$ vanishes at every point.

#### The action of Sₙ on polynomials · P1

$(\sigma \cdot f)(x_1, \ldots, x_n) = f(x_{\sigma(1)}, \ldots, x_{\sigma(n)})$: $\sigma$ renames $x_i$ as $x_{\sigma(i)}$, see Definition [[§20 Polynomial Rings, Permutation Matrices, and Representations#^def-20-3|§20.3]]. *Source: [[Group Theory HW Drill#^ps1-5|PS1.5]] ("the obvious way").*

^nd-def-20-3

- [ ] Q1 **[def]** State the definition.
- [ ] Q2 **[example]** For $\sigma = (1\,2\,3)$, compute $\sigma \cdot (x_1 + 2x_2 + 3x_3)$ and $\sigma \cdot (x_1 - x_2)$.
- [ ] Q3 **[use]** State the compatibility rules $e \cdot f = f$, $\sigma \cdot (\tau \cdot f) = (\sigma\tau) \cdot f$. Why do they make this an action?
- [ ] Q4 **[why]** Why does the rule "replace $x_i$ by $x_{\sigma(i)}$" give $\sigma \cdot (\tau \cdot f) = (\sigma\tau) \cdot f$ and not $(\tau\sigma) \cdot f$? Track the variable in position $i$.

> [!tip]- Hints: where it lives, examples
> - Definition [[§20 Polynomial Rings, Permutation Matrices, and Representations#^def-20-3|§20.3]]; Example [[§20 Polynomial Rings, Permutation Matrices, and Representations#^ex-20-1|§20.1]]; Proposition [[§20 Polynomial Rings, Permutation Matrices, and Representations#^prop-20-1|§20.1]].
> - Remark [[§20 Polynomial Rings, Permutation Matrices, and Representations#^rem-20-4|Group Actions]].

#### Permutation matrix · P1

$M(\sigma)$ is the matrix of the linear map $e_i \mapsto e_{\sigma(i)}$: column $i$ has its single $1$ in row $\sigma(i)$, see Definition [[§20 Polynomial Rings, Permutation Matrices, and Representations#^def-20-6|§20.6]]. *Source: [[Group Theory HW Drill#^ps1-5|PS1.5]]; lecture 9/9.*

^nd-def-20-6

- [ ] Q1 **[def]** Define $M(\sigma)$ and give the entry formula.
- [ ] Q2 **[example]** Write $M((1\,2\,3))$ and $M((1\,4\,2\,3))$ and their action on a column vector.
- [ ] Q3 **[use]** How do you read $\sigma$ off a matrix, by columns and by rows?
- [ ] Q4 **[why]** With the row convention, what changes about $M(\sigma)M(\tau)$? Does it change $\det M(\sigma)$?
- [ ] Q5 **[use]** What are $M(\sigma)^{-1}$ and $\det M(\sigma)$?

> [!tip]- Hints: where it lives, examples
> - Definition [[§20 Polynomial Rings, Permutation Matrices, and Representations#^def-20-6|§20.6]]; Example [[§20 Polynomial Rings, Permutation Matrices, and Representations#^ex-20-2|§20.2]] (recipe: columns $e_{\sigma(1)}, \ldots, e_{\sigma(n)}$).
> - Remark [[§20 Polynomial Rings, Permutation Matrices, and Representations#^rem-20-3|Row vs. Column Convention]]; Proposition [[§20 Polynomial Rings, Permutation Matrices, and Representations#^prop-20-5|§20.5]]; $\det M(\sigma) = \operatorname{sgn}\sigma$ (Definition [[§21 The Sign Homomorphism and the Alternating Group#^def-21-2|§21.2]]).

#### Permutation representation · P1

The permutation representation of $S_n$ is $\sigma \mapsto M(\sigma)$, $S_n \to GL_n(k)$; its image is the group of permutation matrices, see Definition [[§20 Polynomial Rings, Permutation Matrices, and Representations#^def-20-8|§20.8]]. *Source: [[Group Theory HW Drill#^ps1-5|PS1.5]]; lecture 9/9; WS 1.7.*

^nd-def-20-8

- [ ] Q1 **[def]** State the definition.
- [ ] Q2 **[use]** Why is it an injective homomorphism? What is the one identity to check?
- [ ] Q3 **[use]** How does composing with $\det$ give the sign?
- [ ] Q4 **[why]** How does this show every subgroup of $S_n$ is a matrix group? What does it give combined with Cayley's theorem later?

> [!tip]- Hints: where it lives, examples
> - Definition [[§20 Polynomial Rings, Permutation Matrices, and Representations#^def-20-8|§20.8]]; Proposition [[§20 Polynomial Rings, Permutation Matrices, and Representations#^prop-20-5|§20.5]]; Proposition [[§20 Polynomial Rings, Permutation Matrices, and Representations#^prop-20-4|§20.4]] for any finite set $X$.
> - Remark [[§21 The Sign Homomorphism and the Alternating Group#^rem-21-2|Speyer's Presentation]] ($\operatorname{sgn} = \det \circ M$).

#### Inversions of a permutation · P1

An inversion of $\sigma$ is a pair $i < j$ with $\sigma(i) > \sigma(j)$; $\operatorname{inv}(\sigma)$ counts them; an adjacent inversion is a $k$ with $\sigma(k) > \sigma(k+1)$, see Definition [[§21 The Sign Homomorphism and the Alternating Group#^def-21-1|§21.1]]. *Source: [[Group Theory HW Drill#^ps1-5-1|PS1.5(1)]].*

^nd-def-21-1

- [ ] Q1 **[def]** Define inversion, $\operatorname{inv}(\sigma)$, adjacent inversion.
- [ ] Q2 **[example]** Compute $\operatorname{inv}$ of $(1\,2)$, $(1\,3)$, $(1\,2\,3)$, $(1\,3\,2)$ in $S_3$ and their signs.
- [ ] Q3 **[use]** What does one adjacent swap do to $\operatorname{inv}$? What is $\operatorname{inv}$ of the sorted sequence?
- [ ] Q4 **[why]** Why is $\operatorname{inv}((1\,n)) = 2n - 3$ odd? Check against the sign of a transposition.

> [!tip]- Hints: where it lives, examples
> - Definition [[§21 The Sign Homomorphism and the Alternating Group#^def-21-1|§21.1]]; Lemma [[§21 The Sign Homomorphism and the Alternating Group#^lem-21-1|§21.1]].
> - $\operatorname{inv}$: $1, 3, 2, 2$ for $(1\,2), (1\,3), (1\,2\,3), (1\,3\,2)$.
> - $(1\,n)$: sequence $n, 2, \ldots, n-1, 1$: $(n-1) + (n-2)$ inversions.

#### Sign; even and odd permutations · P1

$\operatorname{sgn}(\sigma) = \det M(\sigma) = (-1)^{\operatorname{inv}(\sigma)} = \sigma \cdot \Delta / \Delta \in \{\pm 1\}$; $\sigma$ is even if $\operatorname{sgn}\sigma = 1$, odd if $-1$, see Definition [[§21 The Sign Homomorphism and the Alternating Group#^def-21-2|§21.2]]. *Source: [[Group Theory HW Drill#^ps1-5-2|PS1.5(2)]] (written $\varepsilon$); lecture 9/9 (written $\operatorname{sgn}$).*

^nd-def-21-2

- [ ] Q1 **[def]** Give the three formulas for $\operatorname{sgn}$ and define even and odd.
- [ ] Q2 **[example]** Signs of a transposition, a $3$-cycle, a $4$-cycle, $(1\,2)(3\,4)$, $(1\,5\,4)(3\,7\,6)$.
- [ ] Q3 **[use]** How do you compute $\operatorname{sgn}$ from the cycle type?
- [ ] Q4 **[why]** Why is it legitimate to define the sign by any of the three formulas? Why does the definition not use a factorization into transpositions?

> [!tip]- Hints: where it lives, examples
> - Definition [[§21 The Sign Homomorphism and the Alternating Group#^def-21-2|§21.2]]; Theorem [[§21 The Sign Homomorphism and the Alternating Group#^thm-21-2|§21.2]]; Corollary [[§21 The Sign Homomorphism and the Alternating Group#^cor-21-4|§21.4]] ($(-1)^{r-1}$ per $r$-cycle).
> - Remark [[§21 The Sign Homomorphism and the Alternating Group#^rem-21-1|Parity, Settled]].

#### The alternating group Aₙ · P1

$A_n = \operatorname{Ker}(\operatorname{sgn}) = \{\sigma \in S_n : \operatorname{sgn}\sigma = 1\}$, see Definition [[§21 The Sign Homomorphism and the Alternating Group#^def-21-3|§21.3]]. *Source: [[Group Theory HW Drill#^ps1-5|PS1.5]].*

^nd-def-21-3

- [ ] Q1 **[def]** Define $A_n$.
- [ ] Q2 **[example]** List $A_3$ and the cycle types in $A_4$; give $|A_4|$ and $|A_5|$.
- [ ] Q3 **[use]** Why is $A_n$ a subgroup without checking the axioms? Name a generating set.
- [ ] Q4 **[why]** Why is $A_n$ the stabilizer of $\Delta$, and why does this need $2 \neq 0$?

> [!tip]- Hints: where it lives, examples
> - Definition [[§21 The Sign Homomorphism and the Alternating Group#^def-21-3|§21.3]]; kernels are subgroups (Proposition [[§15 Homomorphisms#^prop-15-2|§15.2]]).
> - $A_3 = \langle (1\,2\,3) \rangle$; $A_4$: $e$, eight $3$-cycles, three double transpositions; Proposition [[§21 The Sign Homomorphism and the Alternating Group#^prop-21-5|§21.5]].
> - Theorem [[§21 The Sign Homomorphism and the Alternating Group#^thm-21-9|§21.9]]; Corollary [[§21 The Sign Homomorphism and the Alternating Group#^cor-21-10|§21.10]].

### Priority 4 · notes only (Pinter, MATH 412, not from class)

#### Commutative ring (provisional) · P4

A commutative ring is $(R, +, \cdot)$ with $(R, +)$ abelian and $\cdot$ associative, commutative, unital and distributive; nonzero elements need not be invertible, see Definition [[§20 Polynomial Rings, Permutation Matrices, and Representations#^def-20-2|§20.2]]. *Source: notes.*

^nd-def-20-2

- [ ] Q1 **[def]** State the axioms. Which field axiom is dropped?
- [ ] Q2 **[example]** Give three commutative rings that are not fields.
- [ ] Q3 **[use]** Why is $k[x_1, \ldots, x_n]$ not a field?
- [ ] Q4 **[why]** Is $\mathbb{Z}/6\mathbb{Z}$ a commutative ring? A field? Which elements are units?

> [!tip]- Hints: where it lives, examples
> - Definition [[§20 Polynomial Rings, Permutation Matrices, and Representations#^def-20-2|§20.2]]; remark [[§20 Polynomial Rings, Permutation Matrices, and Representations#^rem-20-1|k as a Ring]] ($x_1 g = 1$ impossible by degree).
> - $\mathbb{Z}$, $k[x]$, $\mathbb{Z}/6\mathbb{Z}$ with units $U_6 = \{1, 5\}$ (Proposition [[§8 Invertibility and Unit Groups#^prop-8-4|§8.4]]).

#### Symmetric polynomial · P4

$f$ is symmetric if $\sigma \cdot f = f$ for all $\sigma \in S_n$, see Definition [[§20 Polynomial Rings, Permutation Matrices, and Representations#^def-20-4|§20.4]]. *Source: notes.*

^nd-def-20-4

- [ ] Q1 **[def]** State the definition.
- [ ] Q2 **[example]** Name the elementary symmetric polynomials $e_1, e_2, e_3$ in three variables.
- [ ] Q3 **[use]** Why does it suffice to check $\sigma \cdot f = f$ for $\sigma$ in a generating set? Which two permutations suffice in $S_3$?
- [ ] Q4 **[why]** Is $\Delta$ symmetric? Is $\Delta^2$?

> [!tip]- Hints: where it lives, examples
> - Definition [[§20 Polynomial Rings, Permutation Matrices, and Representations#^def-20-4|§20.4]]; Example [[§20 Polynomial Rings, Permutation Matrices, and Representations#^ex-20-1|§20.1]]; strategy G7 (work on generators).
> - $(1\,2)$ and $(1\,2\,3)$ generate $S_3$; $\Delta$ is alternating, $\Delta^2$ symmetric (remark [[§21 The Sign Homomorphism and the Alternating Group#^rem-21-3|The Origin of the Names]]).

#### Standard basis of kⁿ · P4

$e_i$ has $1$ in position $i$ and $0$ elsewhere; every $v$ is uniquely $\sum v_ie_i$, see Definition [[§20 Polynomial Rings, Permutation Matrices, and Representations#^def-20-5|§20.5]]. *Source: notes.*

^nd-def-20-5

- [ ] Q1 **[def]** Define $e_i$ and the coordinates of $v$.
- [ ] Q2 **[use]** How is $\{1, \ldots, n\}$ identified with the standard basis, and why does that let $S_n$ act on $k^n$?
- [ ] Q3 **[use]** What is the $i$-th column of a matrix in terms of $e_i$?
- [ ] Q4 **[why]** Why do two linear maps that agree on $e_1, \ldots, e_n$ agree everywhere?

> [!tip]- Hints: where it lives, examples
> - Definition [[§20 Polynomial Rings, Permutation Matrices, and Representations#^def-20-5|§20.5]]; Theorem [[§20 Polynomial Rings, Permutation Matrices, and Representations#^thm-20-2|§20.2]]; Corollary [[§20 Polynomial Rings, Permutation Matrices, and Representations#^cor-20-3|§20.3]].

#### Representation · P4

A representation of $G$ is a homomorphism $G \to GL_n(k)$ (more generally $G \to GL(V)$), see Definition [[§20 Polynomial Rings, Permutation Matrices, and Representations#^def-20-7|§20.7]]. *Source: notes; second half of the course.*

^nd-def-20-7

- [ ] Q1 **[def]** State the definition.
- [ ] Q2 **[example]** Give two representations of $S_n$, one of dimension $n$ and one of dimension $1$.
- [ ] Q3 **[example]** Give a representation of $\mathbb{Z}/n\mathbb{Z}$ in $GL_2(\mathbb{R})$ and of $(\mathbb{R}, +)$ in $GL_2(\mathbb{R})$.
- [ ] Q4 **[why]** Why is a $1$-dimensional representation the same as a homomorphism to $k^\times$?

> [!tip]- Hints: where it lives, examples
> - Definition [[§20 Polynomial Rings, Permutation Matrices, and Representations#^def-20-7|§20.7]]; Definition [[§20 Polynomial Rings, Permutation Matrices, and Representations#^def-20-8|§20.8]]; $\operatorname{sgn}$ into $GL_1 = \mathbb{Q}^\times$ (remark [[§21 The Sign Homomorphism and the Alternating Group#^rem-21-3|The Origin of the Names]]).
> - Rotations $[k] \mapsto R_{2\pi k/n}$; $t \mapsto \begin{pmatrix} 1 & t \\ 0 & 1 \end{pmatrix}$ (Example [[§5 A Zoo of Subgroups#^ex-5-4|§5.4]]).
> - $GL_1(k) = k^\times$.

#### Alternating polynomial · P4

$f \in \mathbb{Q}[x_1, \ldots, x_n]$ is alternating if $\sigma \cdot f = \operatorname{sgn}(\sigma) f$ for all $\sigma$; $\Delta$ is alternating, see Definition [[§21 The Sign Homomorphism and the Alternating Group#^def-21-4|§21.4]]. *Source: notes.*

^nd-def-21-4

- [ ] Q1 **[def]** State the definition; compare with symmetric.
- [ ] Q2 **[example]** Why is $\Delta$ alternating? Is $x_1 - x_2$ alternating in $\mathbb{Q}[x_1, x_2, x_3]$?
- [ ] Q3 **[use]** If $f$ is alternating, what is $f^2$? What is the product of an alternating and a symmetric polynomial?
- [ ] Q4 **[why]** Why do the names "symmetric group" and "alternating group" come from polynomials?

> [!tip]- Hints: where it lives, examples
> - Definition [[§21 The Sign Homomorphism and the Alternating Group#^def-21-4|§21.4]]; Theorem [[§21 The Sign Homomorphism and the Alternating Group#^thm-21-2|§21.2]].
> - $(1\,3) \cdot (x_1 - x_2) = x_3 - x_2 \neq -(x_1 - x_2)$.
> - Remark [[§21 The Sign Homomorphism and the Alternating Group#^rem-21-3|The Origin of the Names]].

## Proofs T5

### Priority 1 · problem sets (directly or extended)

#### Compatibility of the action with composition · P1

$e \cdot f = f$ and $\sigma \cdot (\tau \cdot f) = (\sigma\tau) \cdot f$; each $f \mapsto \sigma \cdot f$ respects sums and products, see Proposition [[§20 Polynomial Rings, Permutation Matrices, and Representations#^prop-20-1|§20.1]]. *Source: notes (needed for [[Group Theory HW Drill#^ps1-5|PS1.5]]).*

^nd-prop-20-1

- [ ] Q1 **[state]** State the proposition.
- [ ] Q2 In $\tau \cdot f = f(x_{\tau(1)}, \ldots, x_{\tau(n)})$, which variable sits in position $i$, and what does $\sigma$ rename it to?
- [ ] Q3 Conclude $\sigma \cdot (\tau \cdot f) = (\sigma\tau) \cdot f$.
- [ ] Q4 **[why]** Where is this used in the proof that $\operatorname{sgn}$ is a homomorphism via $\Delta$ (an alternative to the determinant route)?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: track one position (G11 flavour: an action).
> - $x_{\tau(i)} \mapsto x_{\sigma(\tau(i))} = x_{(\sigma\tau)(i)}$.
> - $(\sigma\tau) \cdot \Delta = \sigma \cdot (\operatorname{sgn}(\tau)\Delta) = \operatorname{sgn}(\tau)\operatorname{sgn}(\sigma)\Delta$, using that $\sigma$ respects scalar multiples. Remark [[§20 Polynomial Rings, Permutation Matrices, and Representations#^rem-20-4|Group Actions]].

#### σ ↦ M(σ) is an injective homomorphism · P1

$M(\sigma\tau) = M(\sigma)M(\tau)$, $M(e) = I_n$, $M(\sigma)^{-1} = M(\sigma^{-1}) = M(\sigma)^{\mathsf{T}}$, and $\sigma \mapsto M(\sigma)$ is injective, see Proposition [[§20 Polynomial Rings, Permutation Matrices, and Representations#^prop-20-5|§20.5]]. *Source: lecture 9/9 (the one thing "needing proof" for $\operatorname{sgn} = \det \circ M$); [[Group Theory HW Drill#^ps1-5|PS1.5]].*

^nd-prop-20-5

- [ ] Q1 **[state]** State the proposition.
- [ ] Q2 Prove $M(\sigma)M(\tau) = M(\sigma\tau)$ on basis vectors. Which convention makes the order come out right?
- [ ] Q3 Why is $M(\sigma^{-1}) = M(\sigma)^{\mathsf{T}}$? Conclude permutation matrices are orthogonal.
- [ ] Q4 Why is the map injective?
- [ ] Q5 **[why]** With the row convention, which identity holds instead? Why does $\det$ not care?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G7 (check on $e_i$).
> - $M(\sigma)M(\tau)e_i = M(\sigma)e_{\tau(i)} = e_{\sigma(\tau(i))}$.
> - $M(\sigma)_{ji} = 1$ iff $i = \sigma^{-1}(j)$.
> - Remark [[§20 Polynomial Rings, Permutation Matrices, and Representations#^rem-20-3|Row vs. Column Convention]]: $M(\sigma)M(\tau) = M(\tau\sigma)$.

#### Sorting by adjacent swaps · P1

Swapping an adjacent inversion lowers $\operatorname{inv}$ by exactly $1$; no adjacent inversion iff sorted; bubble sort takes exactly $\operatorname{inv}$ swaps; swapping positions $k, k+1$ of the sequence of $\rho$ gives the sequence of $\rho \circ (k\ k{+}1)$, see Lemma [[§21 The Sign Homomorphism and the Alternating Group#^lem-21-1|§21.1]]. *Source: notes (lemma for [[Group Theory HW Drill#^ps1-5-1|PS1.5(1)]], (3)).*

^nd-lem-21-1

- [ ] Q1 **[state]** State the four parts.
- [ ] Q2 (1): write $\operatorname{inv} = \sum_v L(v)$. Which $L$ values change when an adjacent inversion $p > q$ is swapped, and by how much?
- [ ] Q3 (2): why does "no adjacent inversion" give "no inversion at all"?
- [ ] Q4 (4): why is swapping positions $k, k+1$ the same as composing with $(k\ k{+}1)$ on the right, not the left?
- [ ] Q5 **[why]** Why does a swap at a non-adjacent inversion not necessarily change $\operatorname{inv}$ by exactly $1$? Try $3, 2, 1 \to 1, 2, 3$.

> [!tip]- Hints: route of the proof in the notes
> - Strategy: count inversions at their later entry.
> - $L(p)$ unchanged, $L(q)$ drops by $1$, others unchanged.
> - Transitivity of $<$ along the sequence.
> - New entry at position $k$ is $\rho(k+1) = (\rho \circ (k\ k{+}1))(k)$.

#### Three formulas for the sign · P1

$\sigma \cdot \Delta / \Delta = (-1)^{\operatorname{inv}(\sigma)} = \det M(\sigma)$, Theorem [[§21 The Sign Homomorphism and the Alternating Group#^thm-21-2|§21.2]] → drilled as [[Group Theory HW Drill#^ps1-5-1|PS1.5(1)]].

#### The sign is a homomorphism · P1

$\operatorname{sgn} : S_n \to \{\pm 1\}$ is a homomorphism, Theorem [[§21 The Sign Homomorphism and the Alternating Group#^thm-21-3|§21.3]] → drilled as [[Group Theory HW Drill#^ps1-5-2|PS1.5(2)]].

#### Adjacent transpositions from (1 j)'s · P1

For $k \geq 2$, $(k\ k{+}1) = (1\,k)(1\ k{+}1)(1\,k)$, see Lemma [[§21 The Sign Homomorphism and the Alternating Group#^lem-21-6|§21.6]]. *Source: notes (lemma for [[Group Theory HW Drill#^ps1-5-3|PS1.5(3)]]).*

^nd-lem-21-6

- [ ] Q1 **[state]** State the identity.
- [ ] Q2 Track $1$, $k$, $k+1$ through the three factors, right first.
- [ ] Q3 Why is the result the same under either composition convention?
- [ ] Q4 **[why]** Read the identity as a conjugation: which relabelling does $(1\,k)$ perform on $(1\ k{+}1)$?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G6 (conjugation relabels), G7.
> - The word is a palindrome.
> - $(1\,k)(1\ k{+}1)(1\,k)^{-1} = (k\ k{+}1)$ by Proposition [[§12 Multiplying and Conjugating Cycles#^prop-12-1|§12.1]].

#### Generators of Sₙ · P1

Every $\sigma$ is a product of exactly $\operatorname{inv}(\sigma)$ adjacent transpositions; $S_n$ is generated by the adjacent transpositions and by the $(1\,j)$, Theorem [[§21 The Sign Homomorphism and the Alternating Group#^thm-21-7|§21.7]] → drilled as [[Group Theory HW Drill#^ps1-5-3|PS1.5(3)]].

#### Products of two (1 j)'s · P1

For $k \geq 3$, $(1\,k)(1\,2) = (1\,2\,k)$ and $(1\,2)(1\,k) = (1\,2\,k)^{-1}$; for distinct $j, k \geq 3$, $(1\,j)(1\,k) = (1\,2\,j)(1\,2\,k)^{-1}$, see Lemma [[§21 The Sign Homomorphism and the Alternating Group#^lem-21-8|§21.8]]. *Source: notes (lemma for [[Group Theory HW Drill#^ps1-5-4|PS1.5(4)]]).*

^nd-lem-21-8

- [ ] Q1 **[state]** State the three identities.
- [ ] Q2 Verify $(1\,k)(1\,2) = (1\,2\,k)$ by tracking.
- [ ] Q3 Derive the third identity by inserting $(1\,2)(1\,2) = e$.
- [ ] Q4 **[why]** Why does this show every product of two transpositions of the form $(1\,j)$ lies in $\langle (1\,2\,k) \rangle_k$? Why are inverses not needed as separate generators?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G7.
> - $1 \mapsto 2$, $2 \mapsto 1 \mapsto k$, $k \mapsto 1$.
> - $(1\,j)(1\,2)\cdot(1\,2)(1\,k)$; $(1\,2\,k)^{-1} = (1\,2\,k)^2$.

#### Generators of Aₙ · P1

For $n \geq 3$, $A_n$ is generated by the $3$-cycles $(1\,2\,k)$, $3 \leq k \leq n$, Theorem [[§21 The Sign Homomorphism and the Alternating Group#^thm-21-9|§21.9]] → drilled as [[Group Theory HW Drill#^ps1-5-4|PS1.5(4)]].

#### Coprime to each factor, coprime to the product · P1

If $\gcd(m, P) = \gcd(m, Q) = 1$ then $\gcd(m, PQ) = 1$; likewise for $P_1, \ldots, P_r$, see Lemma [[§22 The Structure of Uₙ#^lem-22-1|§22.1]]. *Source: notes (lemma for [[Group Theory HW Drill#^ps1-6-3|PS1.6(3)]]).*

^nd-lem-22-1

- [ ] Q1 **[state]** State the lemma.
- [ ] Q2 Multiply the two Bézout relations. Which expression for $1$ results?
- [ ] Q3 How does this certify $\gcd(m, PQ) = 1$? How does induction give $r$ factors?
- [ ] Q4 **[why]** Which earlier computation is the same with the roles exchanged?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G14 (Bézout).
> - $1 = m(mxu + xQv + Pyu) + PQ(yv)$.
> - Closure of $U_n$, Proposition [[§8 Invertibility and Unit Groups#^prop-8-3|§8.3]].

#### Uₙ as a product of prime-power unit groups · P1

For $n = \prod p_i^{a_i}$, $[m]_n \mapsto ([m]_{P_1}, \ldots, [m]_{P_r})$ is an isomorphism $U_n \to \prod U_{P_i}$, Theorem [[§22 The Structure of Uₙ#^thm-22-2|§22.2]] → drilled as [[Group Theory HW Drill#^ps1-6-3|PS1.6(3)]].

#### Euler's totient formula · P1

$\varphi(n) = \prod \varphi(p_i^{a_i}) = \prod (p_i - 1)p_i^{a_i - 1}$, see Corollary [[§22 The Structure of Uₙ#^cor-22-3|§22.3]]. *Source: notes (from [[Group Theory HW Drill#^ps1-6-3|PS1.6(3)]]).*

^nd-cor-22-3

- [ ] Q1 **[state]** State the formula.
- [ ] Q2 Why is the first equality the theorem on $U_n$?
- [ ] Q3 Count the non-units modulo $p^a$.
- [ ] Q4 **[example]** Compute $\varphi(15)$, $\varphi(24)$, $\varphi(100)$. Describe $U_{15}$ and $U_{24}$ as products of cyclic groups.
- [ ] Q5 **[why]** Why is $\varphi(mn) = \varphi(m)\varphi(n)$ false without $\gcd(m, n) = 1$? Test $m = n = 2$.

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G14 (CRT), counting.
> - Theorem [[§22 The Structure of Uₙ#^thm-22-2|§22.2]]; multiples of $p$ in $[0, p^a)$: $p^{a-1}$ of them.
> - $8$, $8$, $40$; Example [[§22 The Structure of Uₙ#^ex-22-1|§22.1]]: $U_{15} \cong \mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/4\mathbb{Z}$, $U_{24} \cong (\mathbb{Z}/2\mathbb{Z})^3$.
> - $\varphi(4) = 2 \neq 1 = \varphi(2)^2$.

### Priority 3 · filled in, using a technique the problem sets drill

#### Parity of a permutation · P3

Every transposition is odd; a product of $m$ transpositions has sign $(-1)^m$, so the parity of the number of transpositions is independent of the factorization; an $r$-cycle has sign $(-1)^{r-1}$, see Corollary [[§21 The Sign Homomorphism and the Alternating Group#^cor-21-4|§21.4]]. *Source: notes; settles the "parity" claim of §12; used later (characters of $S_n$, $A_n$).*

^nd-cor-21-4

- [ ] Q1 **[state]** State the three parts.
- [ ] Q2 Why is $\det M((a\ b)) = -1$?
- [ ] Q3 Why does $\sigma = t_1 \cdots t_m$ give $\operatorname{sgn}\sigma = (-1)^m$, and why does this make the parity of $m$ independent of the factorization?
- [ ] Q4 Why is the sign of an $r$-cycle $(-1)^{r-1}$? Which factorization?
- [ ] Q5 **[why]** Can $e$ be written as a product of three transpositions? Why is parity an invariant while the number of factors is not?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G8 (a character, $\operatorname{sgn}$, computed on generators); G7.
> - $M((a\ b))$ is $I_n$ with two columns exchanged.
> - $\operatorname{sgn}$ is defined without factorizations (remark [[§21 The Sign Homomorphism and the Alternating Group#^rem-21-1|Parity, Settled]]).
> - $(a_1 \cdots a_r) = (a_1\,a_r)\cdots(a_1\,a_2)$, Proposition [[§12 Multiplying and Conjugating Cycles#^prop-12-2|§12.2]].

#### Aₙ is the stabilizer of Δ · P3

$\sigma \cdot \Delta = \Delta$ iff $\sigma \in A_n$, see Corollary [[§21 The Sign Homomorphism and the Alternating Group#^cor-21-10|§21.10]]. *Source: notes.*

^nd-cor-21-10

- [ ] Q1 **[state]** State the corollary.
- [ ] Q2 Which formula for $\sigma \cdot \Delta$ do you use?
- [ ] Q3 Why is $-\Delta \neq \Delta$ over $\mathbb{Q}$?
- [ ] Q4 **[why]** Over a field with $2 = 0$, what would the stabilizer of $\Delta$ be?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G8 (kernel of the sign character).
> - $\sigma \cdot \Delta = \operatorname{sgn}(\sigma)\Delta$, $\Delta \neq 0$ (Theorem [[§21 The Sign Homomorphism and the Alternating Group#^thm-21-2|§21.2]]).
> - $2\Delta \neq 0$; in characteristic $2$, $-\Delta = \Delta$, so all of $S_n$.

### Priority 4 · notes only (Pinter, MATH 412, not from class)

#### Linear extension · P4

Given a basis $b_1, \ldots, b_n$ of $V$ and any $w_1, \ldots, w_n \in W$, there is exactly one linear $T$ with $T(b_i) = w_i$, namely $T(\sum c_ib_i) = \sum c_iw_i$, see Theorem [[§20 Polynomial Rings, Permutation Matrices, and Representations#^thm-20-2|§20.2]]. *Source: notes (linear algebra).*

^nd-thm-20-2

- [ ] Q1 **[state]** State the theorem and the matrix statement.
- [ ] Q2 Existence: why is $T$ a well-defined function, and why linear?
- [ ] Q3 Uniqueness: why must any linear $T'$ with $T'(b_i) = w_i$ equal $T$?
- [ ] Q4 **[why]** Which hypothesis (spanning or independence) gives existence of the formula, and which gives well-definedness?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: unique coordinates; G7 (determined by values on generators).
> - $T(v + \lambda v') = \sum (c_i + \lambda c_i')w_i$.
> - Spanning: every $v$ has an expression; independence: it is unique.

#### Permutations of the basis give invertible linear maps · P4

$T_\sigma(e_i) = e_{\sigma(i)}$ defines a unique linear map with $T_\sigma T_\tau = T_{\sigma\tau}$ and inverse $T_{\sigma^{-1}}$; its matrix is $M(\sigma)$, see Corollary [[§20 Polynomial Rings, Permutation Matrices, and Representations#^cor-20-3|§20.3]]. *Source: notes.*

^nd-cor-20-3

- [ ] Q1 **[state]** State the corollary.
- [ ] Q2 Prove $T_\sigma T_\tau = T_{\sigma\tau}$ on basis vectors; which uniqueness statement finishes?
- [ ] Q3 Deduce that $T_\sigma$ is invertible.
- [ ] Q4 **[why]** Which property of $\sigma$ is used (only that it is a bijection of the index set)? Why does the same construction work for any finite set $X$?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G7 (check on a basis).
> - $T_\sigma T_\tau(e_i) = e_{\sigma\tau(i)}$; Theorem [[§20 Polynomial Rings, Permutation Matrices, and Representations#^thm-20-2|§20.2]].
> - Remark [[§20 Polynomial Rings, Permutation Matrices, and Representations#^rem-20-2|From a Set to a Vector Space]]; Proposition [[§20 Polynomial Rings, Permutation Matrices, and Representations#^prop-20-4|§20.4]].

#### Permutation representation of S_X · P4

For a finite set $X$, $\sigma \mapsto T_\sigma$ ($T_\sigma(e_x) = e_{\sigma(x)}$) is an injective homomorphism $S_X \to GL(k^X)$, see Proposition [[§20 Polynomial Rings, Permutation Matrices, and Representations#^prop-20-4|§20.4]]. *Source: notes; used later for "every finite group is a matrix group".*

^nd-prop-20-4

- [ ] Q1 **[state]** State the proposition.
- [ ] Q2 Why does $T_\sigma$ exist and why is $\sigma \mapsto T_\sigma$ a homomorphism?
- [ ] Q3 Why is it injective?
- [ ] Q4 **[why]** Combined with Cayley's theorem, what does this give for an arbitrary finite group $G$, and in which dimension?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G7 (basis vectors), G11 (actions as homomorphisms).
> - Linear Extension; agree on basis vectors; $e_{\sigma(x)} = e_{\tau(x)}$ forces $\sigma = \tau$.
> - $G \hookrightarrow S_G \hookrightarrow GL_{|G|}(k)$ (Chapter 6).

#### Size of Aₙ · P4

For $n \geq 2$, $\operatorname{sgn}$ is surjective and $|A_n| = n!/2$, see Proposition [[§21 The Sign Homomorphism and the Alternating Group#^prop-21-5|§21.5]]. *Source: notes.*

^nd-prop-21-5

- [ ] Q1 **[state]** State the proposition.
- [ ] Q2 Why is $\operatorname{sgn}$ surjective?
- [ ] Q3 Show $\sigma \mapsto (1\,2)\sigma$ is a bijection $A_n \to S_n \setminus A_n$.
- [ ] Q4 **[why]** What happens for $n = 1$? Give a second proof using $|G| = |\operatorname{Ker}|\,|\operatorname{Im}|$ (later) or cosets.

> [!tip]- Hints: route of the proof in the notes
> - Strategy: explicit bijection; later G5 ($[S_n : A_n] = 2$).
> - $\operatorname{sgn}((1\,2)\sigma) = -\operatorname{sgn}\sigma$; the map is its own inverse.
> - $S_1 = A_1 = \{e\}$; $\operatorname{sgn}$ is not onto.

# T6. Actions, cosets, Lagrange, orbit–stabilizer

## Definitions T6

### Priority 1 · problem sets (directly or extended)

#### The point stabilizer in $S_n$ · P1

$H = \{\sigma \in S_n : \sigma(n) = n\} = \operatorname{Stab}(n) \cong S_{n-1}$, of order $(n-1)!$, see Definition [[§30 Orbit–Stabilizer#^def-30-1|§30.1]]. *Source: [[Group Theory HW Drill#^ps2-1|PS2.1]].*

^nd-def-30-1

- [ ] Q1 **[def]** Define $H$ and check directly that it is a subgroup.
- [ ] Q2 **[example]** List $H$ for $n = 3$.
- [ ] Q3 **[use]** Why is $H \cong S_{n-1}$, and what is $[S_n : H]$?
- [ ] Q4 **[why]** Is $H$ normal in $S_n$ for $n \geq 3$? Which conjugate of $H$ is $\operatorname{Stab}(i)$?

> [!tip]- Hints: where it lives, examples
> - Cosets: Proposition [[§30 Orbit–Stabilizer#^prop-30-4|§30.4]] ([[Group Theory HW Drill#^ps2-1|PS2.1]]); conjugates: Proposition [[§26 Stabilizers and Fixed Points#^prop-26-2|§26.2]] gives $\operatorname{Stab}(\sigma(n)) = \sigma H \sigma^{-1}$.

### Priority 2 · worksheets and lectures

#### Equivalence relation · P2

A relation $\sim$ on $X$ (a subset of $X \times X$) that is reflexive, symmetric and transitive, see Definition [[§24 Equivalence Relations and Partitions#^def-24-1|§24.1]]. *Source: lecture 9/11; cf. Pinter Ch. 12.*

^nd-def-24-1

- [ ] Q1 **[def]** State the three axioms of an equivalence relation.
- [ ] Q2 **[example]** Why are equality and congruence mod $n$ equivalence relations, while $\leq$ on $\mathbb{Z}$ and divisibility are not? Which axiom fails?
- [ ] Q3 **[example]** For $H \leq G$, which subgroup axiom gives each of reflexivity, symmetry and transitivity of $g_1^{-1}g_2 \in H$?
- [ ] Q4 **[why]** Why is a relation the same thing as a subset of $X \times X$?

> [!tip]- Hints: where it lives, examples
> - The model case is $\mathbb{Z}$ with $H = n\mathbb{Z}$; the general case is congruence modulo a subgroup, Definition [[§28 Left and Right Cosets#^def-28-1|§28.1]].
> - Order relations fail symmetry.

#### Equivalence class · P2

$R_x = \{y \in X : x \sim y\}$, which contains $x$, see Definition [[§24 Equivalence Relations and Partitions#^def-24-2|§24.2]]. *Source: lecture 9/11.*

^nd-def-24-2

- [ ] Q1 **[def]** Define the equivalence class $R_x$.
- [ ] Q2 **[example]** What are the classes of congruence mod $n$ on $\mathbb{Z}$, and of $\equiv_\ell \pmod H$ on $G$?
- [ ] Q3 **[use]** Why does $x \in R_x$ hold? Which axiom?
- [ ] Q4 **[why]** Why do the classes of the orbit relation equal the orbits $Gx$?

> [!tip]- Hints: where it lives, examples
> - Classes of $\equiv_\ell$ are the left cosets, Proposition [[§28 Left and Right Cosets#^prop-28-2|§28.2]].
> - Classes of the orbit relation are orbits, Proposition [[§27 Orbits#^prop-27-2|§27.2]].

#### Partition · P2

A collection of nonempty subsets (parts) of $X$ with every element in exactly one part, $X = \bigsqcup_i X_i$, see Definition [[§24 Equivalence Relations and Partitions#^def-24-3|§24.3]]. *Source: lecture 9/11.*

^nd-def-24-3

- [ ] Q1 **[def]** Define a partition of $X$.
- [ ] Q2 **[example]** Give the partition of $S_3$ into left cosets of $\{e, (1\,2)\}$.
- [ ] Q3 **[example]** Give the partition of $\mathbb{R}^3$ into $O_3(\mathbb{R})$-orbits.
- [ ] Q4 **[why]** Why must the parts be nonempty for the dictionary with equivalence relations to work?

> [!tip]- Hints: where it lives, examples
> - Cosets of $\{e, (1\,2)\}$: Example [[§28 Left and Right Cosets#^ex-28-1|§28.1]].
> - Orbits of $O_3$: Proposition [[§32 Linear Groups, the Cube, S₃ and A₄#^prop-32-2|§32.2]].

#### Action (left action) · P2

A map $\star : G \times X \to X$ with $(g_1g_2) \star x = g_1 \star (g_2 \star x)$ and $e \star x = x$, see Definition [[§25 Actions#^def-25-1|§25.1]]. *Source: WS 4.*

^nd-def-25-1

- [ ] Q1 **[def]** State the two axioms of an action of $G$ on $X$.
- [ ] Q2 **[example]** Check the axioms for: $S_X$ on $X$; $GL_n(k)$ on $k^n$; $G$ on itself by left multiplication; $G$ on itself by conjugation; the trivial action.
- [ ] Q3 **[example]** For conjugation $g \star x = gxg^{-1}$, which identity about $c_g$ is the first axiom?
- [ ] Q4 **[why]** Why is $e \star x = x$ an axiom and not a consequence? Give the lecture's example with $G = \{e\}$, $X = \{0, 1\}$.
- [ ] Q5 **[use]** Which theorem turns an action into a homomorphism $G \to S_X$?

> [!tip]- Hints: where it lives, examples
> - Examples [[§25 Actions#^ex-25-2|§25.2]]; the independence of the identity axiom is Example [[§25 Actions#^ex-25-1|§25.1]] ($e \star 0 = e \star 1 = 0$, a monoid action).
> - Dictionary with homomorphisms: Theorem [[§25 Actions#^thm-25-3|§25.3]].

#### Right action · P2

A map $X \times G \to X$ with $x \star (g_2g_1) = (x \star g_2) \star g_1$ and $x \star e = x$, see Definition [[§25 Actions#^def-25-2|§25.2]]. *Source: WS 4.*

^nd-def-25-2

- [ ] Q1 **[def]** State the axioms of a right action. In which order do the factors act?
- [ ] Q2 **[example]** Why is $g \star h := gh$ ($h \in H$) a right action of $H$ on $G$, and what are its orbits?
- [ ] Q3 **[use]** How do you turn a left action into a right action (WS 4.1)?
- [ ] Q4 **[why]** Why is $(x, g) \mapsto gx$ (without inverse) not a right action for non-abelian $G$?

> [!tip]- Hints: where it lives, examples
> - Right multiplication by $H$ has orbits the left cosets $gH$: Proposition [[§28 Left and Right Cosets#^prop-28-1|§28.1]].
> - Conversion $x \star g = g^{-1}x$: Proposition [[§25 Actions#^prop-25-1|§25.1]].

#### Arrow notation · P2

$f : X \to Y$ (function between sets), $x \mapsto y$ (an element sent to an element), $G \curvearrowright X$ (left action) and $X \curvearrowleft G$ (right action), see Definition [[§25 Actions#^def-25-3|§25.3]]. *Source: lecture.*

^nd-def-25-3

- [ ] Q1 **[def]** What does each of $\to$, $\mapsto$, $\curvearrowright$ denote?
- [ ] Q2 **[example]** Write the left-multiplication action of $G$ on $G/H$ with the correct arrows.
- [ ] Q3 **[why]** Why is an action not a function $G \to X$? What two equivalent kinds of map is it?

> [!tip]- Hints: where it lives, examples
> - An action is $G \times X \to X$, equivalently a homomorphism $G \to S_X$ (Theorem [[§25 Actions#^thm-25-3|§25.3]]).
> - The group is written on the side from which it acts: $G \backslash X$, $X/G$.

#### Kernel of an action · P2

$\{g \in G : g \star x = x \text{ for all } x\}$, the kernel of $\varphi : G \to S_X$, see Definition [[§25 Actions#^def-25-4|§25.4]]. *Source: notes; WS 4.*

^nd-def-25-4

- [ ] Q1 **[def]** Define the kernel of an action in both languages.
- [ ] Q2 **[example]** For $\mathbb{Z}/4\mathbb{Z}$ acting on $\{1, 2\}$ by swapping for odd $k$, what is the kernel?
- [ ] Q3 **[example]** For the cube group acting on the three colours, name non-identity elements of the kernel.
- [ ] Q4 **[use]** Why is the kernel of an action a normal subgroup?
- [ ] Q5 **[why]** What is the kernel of left multiplication of $G$ on $G/H$? (Normal core.)

> [!tip]- Hints: where it lives, examples
> - Examples [[§25 Actions#^ex-25-3|§25.3]] and [[§32 Linear Groups, the Cube, S₃ and A₄#^ex-32-1|§32.1]].
> - Kernels are normal: Proposition [[§39 Sources of Normal Subgroups#^prop-39-2|§39.2]]; the normal core is Proposition [[§39 Sources of Normal Subgroups#^prop-39-6|§39.6]].

#### Stabilizer · P2

$\operatorname{Stab}(x) = \{g \in G : g \star x = x\}$, a subset of $G$, see Definition [[§26 Stabilizers and Fixed Points#^def-26-1|§26.1]]. *Source: WS 4.*

^nd-def-26-1

- [ ] Q1 **[def]** Define $\operatorname{Stab}(x)$. Is it a subset of $G$ or of $X$?
- [ ] Q2 **[example]** Stabilizer of $n$ in $S_n$; of $e_1$ under $GL_3(\mathbb{R})$ and under $O_3(\mathbb{R})$.
- [ ] Q3 **[example]** Stabilizer of $eH$ for $G$ acting on $G/H$; of $g$ for $G$ acting on itself by conjugation.
- [ ] Q4 **[why]** How do the stabilizers of $x$ and $g \star x$ compare?

> [!tip]- Hints: where it lives, examples
> - $\operatorname{Stab}(n) \cong S_{n-1}$: Definition [[§30 Orbit–Stabilizer#^def-30-1|§30.1]]; $GL_3$, $O_3$: Propositions [[§32 Linear Groups, the Cube, S₃ and A₄#^prop-32-1|§32.1]], [[§32 Linear Groups, the Cube, S₃ and A₄#^prop-32-2|§32.2]].
> - $\operatorname{Stab}(eH) = H$: Proposition [[§31 G Acting on Coset Spaces#^prop-31-1|§31.1]]; conjugation gives the centralizer, Definition [[§34 Conjugation as an Action and the Class Equation#^def-34-1|§34.1]].
> - $\operatorname{Stab}(g \star x) = g \operatorname{Stab}(x) g^{-1}$: Proposition [[§26 Stabilizers and Fixed Points#^prop-26-2|§26.2]].

#### Fixed points · P2

$\operatorname{Fix}(g) = \{x \in X : g \star x = x\} \subseteq X$; $g \in \operatorname{Stab}(x) \iff x \in \operatorname{Fix}(g)$, see Definition [[§26 Stabilizers and Fixed Points#^def-26-2|§26.2]]. *Source: WS 4.*

^nd-def-26-2

- [ ] Q1 **[def]** Define $\operatorname{Fix}(g)$ and state its relation to stabilizers.
- [ ] Q2 **[example]** In $S_3$ acting on $\{1, 2, 3\}$, how many fixed points do $e$, a transposition, a $3$-cycle have?
- [ ] Q3 **[example]** For conjugation, what is $\operatorname{Fix}(g)$?
- [ ] Q4 **[use]** Which counting formula averages $|\operatorname{Fix}(g)|$, and which set is counted twice in its proof?
- [ ] Q5 **[why]** For a $p$-group acting on $X$, what is the congruence between $|X|$ and $|X^P|$ (the fixed points of all of $P$)?

> [!tip]- Hints: where it lives, examples
> - Burnside, Theorem [[§30 Orbit–Stabilizer#^thm-30-6|§30.6]]; Examples [[§30 Orbit–Stabilizer#^ex-30-3|§30.3]].
> - $p$-group fixed points: Proposition [[§51 p-Groups and Sylow Subgroups#^prop-51-1|§51.1]].

#### Orbit · P2

$Gx = \{g \star x : g \in G\} \subseteq X$, see Definition [[§27 Orbits#^def-27-1|§27.1]]. *Source: WS 4.*

^nd-def-27-1

- [ ] Q1 **[def]** Define the orbit $Gx$.
- [ ] Q2 **[example]** Orbits of $GL_3(\mathbb{R})$ and of $O_3(\mathbb{R})$ on $\mathbb{R}^3$.
- [ ] Q3 **[example]** Orbits of the conjugation action; of $H$ acting on $G$ by right multiplication.
- [ ] Q4 **[why]** Why do orbits partition $X$, and how does $|Gx|$ relate to $|G|$?

> [!tip]- Hints: where it lives, examples
> - Conjugation orbits are conjugacy classes (Definition [[§33 Conjugacy Classes#^def-33-1|§33.1]]); right-multiplication orbits are left cosets (Proposition [[§28 Left and Right Cosets#^prop-28-1|§28.1]]).
> - Partition: Proposition [[§27 Orbits#^prop-27-1|§27.1]]; size: Theorem [[§30 Orbit–Stabilizer#^thm-30-3|§30.3]].

#### Orbit space · P2

The set of orbits, $G \backslash X$ for a left action and $X/G$ for a right action, see Definition [[§27 Orbits#^def-27-2|§27.2]]. *Source: WS 4.*

^nd-def-27-2

- [ ] Q1 **[def]** Define the orbit space of a left action and of a right action.
- [ ] Q2 **[example]** Why is $G/H$ (left cosets) the orbit space of a right action? Of which action?
- [ ] Q3 **[use]** What does Burnside's lemma compute about $G \backslash X$?
- [ ] Q4 **[why]** Why is the orbit space a partition of $X$ (and not just a set of subsets)?

> [!tip]- Hints: where it lives, examples
> - $G/H$ and $H \backslash G$: Proposition [[§28 Left and Right Cosets#^prop-28-1|§28.1]].
> - Burnside: Theorem [[§30 Orbit–Stabilizer#^thm-30-6|§30.6]]; partition: Proposition [[§27 Orbits#^prop-27-1|§27.1]].

#### Orbit space notation · P2

$G \backslash X = \{Gx : x \in X\}$ for a left action and $X/G = \{xG : x \in X\}$ for a right action, "like a quotient", the group written on the side it acts from, see Definition [[§27 Orbits#^def-27-4|§27.4]]. *Source: lecture.*

^nd-def-27-4

- [ ] Q1 **[def]** Write the two orbit-space notations. On which side is the group written?
- [ ] Q2 **[example]** Identify $O_3 \backslash \mathbb{R}^3$ with $\mathbb{R}_{\geq 0}$.
- [ ] Q3 **[example]** Which of $G/H$, $H \backslash G$ is the set of left cosets, and why is the notation consistent?
- [ ] Q4 **[why]** Why is it called "like a quotient", and when is $G/H$ actually a quotient group?

> [!tip]- Hints: where it lives, examples
> - Spheres about the origin: Proposition [[§32 Linear Groups, the Cube, S₃ and A₄#^prop-32-2|§32.2]].
> - $G/N$ is a group for $N$ normal: Theorem [[§40 Quotient Groups#^thm-40-1|§40.1]].

#### Transitive action · P2

Only one orbit: $Gx = X$ for some (equivalently every) $x$, see Definition [[§27 Orbits#^def-27-3|§27.3]]. *Source: WS 4.*

^nd-def-27-3

- [ ] Q1 **[def]** Define a transitive action. Why does "some $x$" imply "every $x$"?
- [ ] Q2 **[example]** Why is $G$ acting on $G/H$ transitive? $S_n$ on $\{1, \ldots, n\}$? The cube group on faces?
- [ ] Q3 **[example]** Is $GL_3(\mathbb{R})$ on $\mathbb{R}^3$ transitive? On $\mathbb{R}^3 \setminus \{0\}$?
- [ ] Q4 **[why]** For a transitive action of finite $G$, what does orbit–stabilizer give for $|X|$?

> [!tip]- Hints: where it lives, examples
> - $G/H$: Proposition [[§31 G Acting on Coset Spaces#^prop-31-1|§31.1]]; cube: Proposition [[§32 Linear Groups, the Cube, S₃ and A₄#^prop-32-3|§32.3]].
> - $|X| = [G : \operatorname{Stab}(x)]$, which divides $|G|$.

#### Congruence modulo a subgroup · P2

$g_1 \equiv_\ell g_2 \pmod H$ iff $g_1^{-1}g_2 \in H$; $g_1 \equiv_r g_2 \pmod H$ iff $g_1g_2^{-1} \in H$, see Definition [[§28 Left and Right Cosets#^def-28-1|§28.1]]. *Source: lecture 9/11.*

^nd-def-28-1

- [ ] Q1 **[def]** Define left and right congruence modulo $H$.
- [ ] Q2 **[example]** For $G = \mathbb{Z}$, $H = n\mathbb{Z}$, write both relations additively. Why do they coincide?
- [ ] Q3 **[use]** Why are both equivalence relations? Which subgroup property is used for each axiom?
- [ ] Q4 **[why]** Why do the two relations agree when $G$ is abelian, and what are their classes in general?

> [!tip]- Hints: where it lives, examples
> - Classes: Proposition [[§28 Left and Right Cosets#^prop-28-2|§28.2]].
> - $\mathbb{Z}$ case: ordinary congruence (remark [[§28 Left and Right Cosets#^rem-28-1|§28]]).

#### Left and right cosets · P2

$gH = \{gh : h \in H\}$ and $Hg = \{hg : h \in H\}$, see Definition [[§28 Left and Right Cosets#^def-28-2|§28.2]]. *Source: lecture 9/11.*

^nd-def-28-2

- [ ] Q1 **[def]** Define $gH$ and $Hg$.
- [ ] Q2 **[example]** Compute $(1\,3)H$ and $H(1\,3)$ for $H = \{e, (1\,2)\} \leq S_3$.
- [ ] Q3 **[use]** State the criterion for $g_1H = g_2H$.
- [ ] Q4 **[example]** In $S_n$ with $H = \operatorname{Stab}(n)$, which datum of $\alpha$ does $\alpha H$ record? Which does $H\alpha$ record?
- [ ] Q5 **[why]** For which subgroups do left and right cosets coincide?

> [!tip]- Hints: where it lives, examples
> - Example [[§28 Left and Right Cosets#^ex-28-1|§28.1]]; [[Group Theory HW Drill#^ps2-1|PS2.1]] is Proposition [[§30 Orbit–Stabilizer#^prop-30-4|§30.4]].
> - $gH = Hg$ for all $g$ is normality, Theorem [[§38 Normal Subgroups#^thm-38-3|§38.3]].

#### Index · P2

$[G : H]$ is the number of left cosets of $H$ in $G$, in $\mathbb{Z}_{>0} \cup \{\infty\}$; $G/H$ is the set of left cosets, $H \backslash G$ the set of right cosets, see Definition [[§29 The Index and Lagrange's Theorem#^def-29-1|§29.1]]. *Source: lecture 9/11.*

^nd-def-29-1

- [ ] Q1 **[def]** Define $[G : H]$, $G/H$ and $H \backslash G$.
- [ ] Q2 **[example]** Compute $[S_n : \operatorname{Stab}(n)]$, $[\mathbb{Z} : n\mathbb{Z}]$, $[S_n : A_n]$.
- [ ] Q3 **[use]** Why may the index equally be defined with right cosets?
- [ ] Q4 **[why]** Give a subgroup of infinite index in an infinite group, and one of finite index.

> [!tip]- Hints: where it lives, examples
> - Left/right bijection $gH \mapsto Hg^{-1}$: Proposition [[§28 Left and Right Cosets#^prop-28-3|§28.3]].
> - $[S_n : \operatorname{Stab}(n)] = n$: Corollary [[§30 Orbit–Stabilizer#^cor-30-5|§30.5]].

### Priority 4 · notes only (Pinter, MATH 412, not from class)

#### Faithful action · P4

The action is faithful if its kernel is $\{e\}$, see Definition [[§25 Actions#^def-25-5|§25.5]]. *Source: notes.*

^nd-def-25-5

- [ ] Q1 **[def]** Define a faithful action.
- [ ] Q2 **[example]** Why is left multiplication of $G$ on itself faithful? Why is the cube group on its faces faithful?
- [ ] Q3 **[example]** Give a non-faithful action (colours of the cube, or the trivial action).
- [ ] Q4 **[why]** What does faithfulness buy: which embedding follows?

> [!tip]- Hints: where it lives, examples
> - Faithful gives $G \hookrightarrow S_X$: Proposition [[§25 Actions#^prop-25-4|§25.4]].
> - Faces of the cube: Proposition [[§32 Linear Groups, the Cube, S₃ and A₄#^prop-32-4|§32.4]].

## Proofs T6

### Priority 2 · worksheets and lectures

#### Equivalence classes partition a set · P2

For an equivalence relation, $R_{x_1} \cap R_{x_2} \neq \varnothing \iff R_{x_1} = R_{x_2} \iff x_1 \sim x_2$, and $\bigcup_x R_x = X$, see Proposition [[§24 Equivalence Relations and Partitions#^prop-24-1|§24.1]]. *Source: lecture 9/11.*

^nd-prop-24-1

- [ ] Q1 **[state]** State the three equivalent conditions and the covering statement.
- [ ] Q2 From $y \in R_{x_1} \cap R_{x_2}$, deduce $x_1 \sim x_2$. Which axioms?
- [ ] Q3 From $x_1 \sim x_2$, show $R_{x_2} \subseteq R_{x_1}$; why does the reverse inclusion follow?
- [ ] Q4 Why do the classes cover $X$?
- [ ] Q5 **[why]** Where is symmetry needed? Which later results are this proposition applied to cosets and orbits?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: unwind the definitions; the three axioms used once each.
> - $x_1 \sim y$, $y \sim x_2$ (symmetry) give $x_1 \sim x_2$ (transitivity); covering is reflexivity.
> - Applied in Propositions [[§28 Left and Right Cosets#^prop-28-2|§28.2]] and [[§27 Orbits#^prop-27-2|§27.2]].

#### Partitions come from equivalence relations · P2

Every partition comes from a unique equivalence relation, "same part", see Proposition [[§24 Equivalence Relations and Partitions#^prop-24-2|§24.2]]. *Source: lecture 9/11 ("I leave [it] for you").* **[class exercise, 9/11]**

^nd-prop-24-2

- [ ] Q1 **[state]** State the proposition, including uniqueness.
- [ ] Q2 Define the relation from a partition $X = \bigsqcup X_i$.
- [ ] Q3 Check reflexive, symmetric, transitive. Where is disjointness of the parts used?
- [ ] Q4 Why are its classes exactly the parts?
- [ ] Q5 Why is the relation unique?
- [ ] Q6 **[why]** Which axiom of a partition (covering, disjointness, nonemptiness) does each step use?

> [!tip]- Hints: route of the proof in the notes
> - Transitivity: two parts both containing $y$ coincide by disjointness.
> - Uniqueness: an equivalence relation is determined by its classes ($x \sim y$ iff $y \in R_x$).

#### A left action gives a right action · P2

If $(g, x) \mapsto gx$ is a left action, then $x \star g := g^{-1}x$ is a right action, see Proposition [[§25 Actions#^prop-25-1|§25.1]]. *Source: WS 4.1.*

^nd-prop-25-1

- [ ] Q1 **[state]** State the proposition and the right-action axioms to be checked.
- [ ] Q2 Check $x \star e = x$.
- [ ] Q3 Compute $(x \star g_2) \star g_1$ and show it equals $x \star (g_2g_1)$. Which identity about inverses is used?
- [ ] Q4 **[why]** Why does $x \star g := gx$ fail to be a right action in general? Where else does the same inversion appear (cosets)?

> [!tip]- Hints: route of the proof in the notes
> - $(x \star g_2) \star g_1 = g_1^{-1}(g_2^{-1}x) = (g_2g_1)^{-1}x$ (socks and shoes).
> - Same trick: the bijection $gH \mapsto Hg^{-1}$, Proposition [[§28 Left and Right Cosets#^prop-28-3|§28.3]].

#### Each group element acts bijectively · P2

$e \star x = x$, and $\hat g : x \mapsto g \star x$ is a bijection with inverse $\widehat{g^{-1}}$, see Proposition [[§25 Actions#^prop-25-2|§25.2]]. *Source: WS 4.2.*

^nd-prop-25-2

- [ ] Q1 **[state]** State both parts.
- [ ] Q2 Compute $\widehat{g^{-1}}(\hat g(x))$ step by step, naming the axiom used at each equality.
- [ ] Q3 Why does a two-sided inverse make $\hat g$ a bijection?
- [ ] Q4 **[why]** Which axiom fails in the lecture's monoid example, and why is $\hat e$ there not a bijection?

> [!tip]- Hints: route of the proof in the notes
> - $\widehat{g^{-1}}(\hat g(x)) = (g^{-1}g) \star x = e \star x = x$, and symmetrically.
> - Example [[§25 Actions#^ex-25-1|§25.1]]: $\hat e^2 = \hat e \neq \operatorname{id}$.

#### Actions are homomorphisms to $S_X$ · P2

An action of $G$ on $X$ is the same thing as a homomorphism $\varphi : G \to S_X$, via $\varphi(g) = \hat g$ and $g \star x = \varphi(g)(x)$, see Theorem [[§25 Actions#^thm-25-3|§25.3]]. *Source: WS 4.3.*

^nd-thm-25-3

- [ ] Q1 **[state]** State the three parts of the theorem.
- [ ] Q2 Action to homomorphism: why does $\varphi(g)$ lie in $S_X$? (Which earlier proposition?)
- [ ] Q3 Show $\varphi(g_1g_2) = \varphi(g_1) \circ \varphi(g_2)$ by evaluating at $x$. Which axiom is this literally?
- [ ] Q4 Homomorphism to action: verify both axioms. Where do you use that the operation of $S_X$ is composition, and that a homomorphism sends $e$ to $\operatorname{id}_X$?
- [ ] Q5 Why are the two constructions mutually inverse?
- [ ] Q6 **[why]** What does the homomorphism language add (kernels, images, Cayley)?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G11 (actions as homomorphisms $G \to S_X$).
> - Bijectivity: Proposition [[§25 Actions#^prop-25-2|§25.2]]; product: $(g_1g_2) \star x = g_1 \star (g_2 \star x)$.
> - Converse: $\varphi(g_1g_2)(x) = \varphi(g_1)(\varphi(g_2)(x))$, $\varphi(e) = \operatorname{id}_X$.

#### The stabilizer is a subgroup · P2

$\operatorname{Stab}(x) \leq G$ for every $x \in X$, see Proposition [[§26 Stabilizers and Fixed Points#^prop-26-1|§26.1]]. *Source: WS 4.4.*

^nd-prop-26-1

- [ ] Q1 **[state]** State the proposition. (What is the worksheet's typo?)
- [ ] Q2 Why is $e \in \operatorname{Stab}(x)$?
- [ ] Q3 Closure under products: compute $(gh) \star x$.
- [ ] Q4 Closure under inverses: apply $g^{-1}$ to $g \star x = x$.
- [ ] Q5 **[why]** Give a second proof: $\operatorname{Stab}(x)$ is the preimage of which subgroup of $S_X$ under $\varphi$?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G1 (subgroup test).
> - $x = g^{-1} \star (g \star x) = g^{-1} \star x$.

#### Stabilizers of points in the same orbit are conjugate · P2

$\operatorname{Stab}(g \star x) = g \operatorname{Stab}(x) g^{-1}$, and $c_g$ restricts to an isomorphism $\operatorname{Stab}(x) \to \operatorname{Stab}(g \star x)$, see Proposition [[§26 Stabilizers and Fixed Points#^prop-26-2|§26.2]] and Corollary [[§26 Stabilizers and Fixed Points#^cor-26-3|§26.3]]. *Source: WS 4.5.*

^nd-prop-26-2

- [ ] Q1 **[state]** State the equality of sets and the corollary.
- [ ] Q2 ($\subseteq$) For $h \in \operatorname{Stab}(g \star x)$, show $g^{-1}hg \in \operatorname{Stab}(x)$.
- [ ] Q3 ($\supseteq$) For $h = gg_0g^{-1}$ with $g_0 \in \operatorname{Stab}(x)$, compute $h \star (g \star x)$.
- [ ] Q4 Why is $c_g : \operatorname{Stab}(x) \to \operatorname{Stab}(g \star x)$ an isomorphism?
- [ ] Q5 **[why]** Apply it to $S_n$: what is $\operatorname{Stab}(\sigma(n))$? And to $G/H$: what is $\operatorname{Stab}(g'H)$?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G6 (conjugation preserves structure).
> - $hg = gg_0$, so $h \star (g \star x) = g \star (g_0 \star x) = g \star x$.
> - Used in Proposition [[§31 G Acting on Coset Spaces#^prop-31-1|§31.1]](3).

#### Orbits partition $X$; the orbit relation · P2

Two orbits are equal or disjoint, so $X$ is the disjoint union of the orbits; equivalently "$y = g \star x$ for some $g$" is an equivalence relation with classes the orbits, see Proposition [[§27 Orbits#^prop-27-1|§27.1]] and Proposition [[§27 Orbits#^prop-27-2|§27.2]]. *Source: WS 4.6.*

^nd-prop-27-1

- [ ] Q1 **[state]** State both propositions.
- [ ] Q2 If $z = g \star x = h \star y$, express $x$ as an element of $Gy$, and conclude $Gx \subseteq Gy$.
- [ ] Q3 Why do the orbits cover $X$?
- [ ] Q4 Second proof: check the three axioms for the orbit relation. Which group axiom gives each?
- [ ] Q5 **[why]** Which group axioms make orbits partition $X$? (Would a monoid action work?)

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G4 (orbits partition).
> - $x = (g^{-1}h) \star y$, so $a \star x = (ag^{-1}h) \star y$.
> - Reflexive $e$, symmetric $g^{-1}$, transitive $hg$; then Proposition [[§24 Equivalence Relations and Partitions#^prop-24-1|§24.1]].

#### Cosets are orbits · P2

$H$ acts on $G$ on the right by multiplication with orbits the left cosets ($G/H$), and on the left with orbits the right cosets ($H \backslash G$); so $[G : H] = |G/H|$, see Proposition [[§28 Left and Right Cosets#^prop-28-1|§28.1]]. *Source: lecture.*

^nd-prop-28-1

- [ ] Q1 **[state]** State the three parts.
- [ ] Q2 Which group axioms are the right-action axioms for $g \star h = gh$?
- [ ] Q3 Compute the orbit of $g$ under the right action of $H$.
- [ ] Q4 **[why]** Why is $G/H$ written with $H$ on the right? How does this explain that the cosets partition $G$ without a separate proof?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G4.
> - $g(h_1h_2) = (gh_1)h_2$ and $ge = g$; orbit $\{gh : h \in H\} = gH$.
> - Partition follows from Proposition [[§27 Orbits#^prop-27-1|§27.1]].

#### Cosets are the equivalence classes · P2

$\equiv_\ell \pmod H$ and $\equiv_r \pmod H$ are equivalence relations with classes the left and right cosets, so $G$ is the disjoint union of its left (and of its right) cosets, see Proposition [[§28 Left and Right Cosets#^prop-28-2|§28.2]]. *Source: lecture 9/11.*

^nd-prop-28-2

- [ ] Q1 **[state]** State the proposition.
- [ ] Q2 Prove reflexivity, symmetry, transitivity of $\equiv_\ell$; name the subgroup property used in each.
- [ ] Q3 Show the class of $g$ is $gH$.
- [ ] Q4 State the resulting coset criterion $g_1H = g_2H \iff$ ?
- [ ] Q5 **[why]** Where would the proof break if $H$ were only a subset closed under products?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G1 (subgroup properties) then Proposition [[§24 Equivalence Relations and Partitions#^prop-24-1|§24.1]].
> - Transitive: $g_1^{-1}g_3 = (g_1^{-1}g_2)(g_2^{-1}g_3)$.
> - $g^{-1}g' = h \iff g' = gh$.

#### The natural bijection $G/H \to H \backslash G$ · P2

$gH \mapsto Hg^{-1}$ is a well-defined bijection with inverse $Hg \mapsto g^{-1}H$, so left and right cosets are equinumerous; $gH \mapsto Hg$ is not well defined, see Proposition [[§28 Left and Right Cosets#^prop-28-3|§28.3]] and Example [[§28 Left and Right Cosets#^ex-28-2|§28.2]]. *Source: lecture 9/11 ("I'll leave for you as an exercise"; "That's actually a very good exercise").* **[class exercise, 9/11]**

^nd-prop-28-3

- [ ] Q1 **[state]** State the proposition and what is to be checked.
- [ ] Q2 Translate $gH = g'H$ and $Hg^{-1} = Hg'^{-1}$ into membership conditions in $H$. Why do they coincide?
- [ ] Q3 Why does this give well-definedness and injectivity at once? Why is the map surjective?
- [ ] Q4 Show $gH \mapsto Hg$ is not well defined, using $(1\,3)H = (1\,2\,3)H$ in $S_3$ with $H = \{e, (1\,2)\}$.
- [ ] Q5 **[why]** Why is the inverse unavoidable? Relate it to WS 4.1 and to $\alpha(n)$ versus $\alpha^{-1}(n)$ in $S_n$.

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G2 (well-definedness on representatives).
> - Both conditions read $g^{-1}g' \in H$.
> - Counterexample: $H(1\,3) = \{(1\,3), (1\,3\,2)\} \neq H(1\,2\,3) = \{(1\,2\,3), (2\,3)\}$.
> - Why $g^{-1}$: remark [[§30 Orbit–Stabilizer#^rem-30-3|§30]] and Proposition [[§30 Orbit–Stabilizer#^prop-30-4|§30.4]].

#### All cosets have the same size · P2

$\#(gH) = |H| = \#(Hg)$, see Proposition [[§29 The Index and Lagrange's Theorem#^prop-29-1|§29.1]]. *Source: lecture 9/11.*

^nd-prop-29-1

- [ ] Q1 **[state]** State the proposition (including the infinite case).
- [ ] Q2 Write the bijection $H \to gH$. Why is it surjective?
- [ ] Q3 Why is it injective? (Which group property?)
- [ ] Q4 **[why]** Why is this the key step of Lagrange? Is $gH$ a subgroup when $g \notin H$?

> [!tip]- Hints: route of the proof in the notes
> - $h \mapsto gh$; injective by left cancellation.
> - $gH$ with $g \notin H$ does not contain $e$.

#### Lagrange's theorem · P2

$|G| = |H| \cdot [G : H]$ (both sides finite together); so $|H|$ divides $|G|$ for finite $G$, see Theorem [[§29 The Index and Lagrange's Theorem#^thm-29-2|§29.2]]. *Source: lecture 9/11.*

^nd-thm-29-2

- [ ] Q1 **[state]** State Lagrange's theorem precisely, including the meaning for infinite groups.
- [ ] Q2 Which partition of $G$ do you use, and which proposition gives it?
- [ ] Q3 Which proposition says the parts all have $|H|$ elements?
- [ ] Q4 Count to conclude.
- [ ] Q5 **[why]** The converse fails: show $A_4$ (order $12$) has no subgroup of order $6$.

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G3 (Lagrange and divisibility).
> - Partition: Proposition [[§28 Left and Right Cosets#^prop-28-2|§28.2]]; sizes: Proposition [[§29 The Index and Lagrange's Theorem#^prop-29-1|§29.1]].
> - $A_4$: Example [[§29 The Index and Lagrange's Theorem#^ex-29-1|§29.1]]: index $2$ is normal, so $g^2 \in H$ for all $g$, so all eight $3$-cycles lie in $H$.

#### Order of an element divides $|G|$; Fermat's little theorem · P2

For finite $G$, $\operatorname{ord}(g) \mid |G|$ and $g^{|G|} = e$; hence $a^{p-1} \equiv 1 \pmod p$ for $p \nmid a$, see Corollary [[§29 The Index and Lagrange's Theorem#^cor-29-3|§29.3]] and Corollary [[§29 The Index and Lagrange's Theorem#^cor-29-4|§29.4]]. *Source: lecture 9/11.*

^nd-cor-29-3

- [ ] Q1 **[state]** State both corollaries.
- [ ] Q2 Which subgroup do you apply Lagrange to, and what is its order?
- [ ] Q3 Deduce $g^{|G|} = e$.
- [ ] Q4 For Fermat: which group, of which order, contains $[a]$?
- [ ] Q5 **[why]** What is Euler's generalization ($U_n$, order $\varphi(n)$)? Why does $p \nmid a$ matter?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G3 and G14.
> - $|\langle g \rangle| = \operatorname{ord}(g)$; $|G| = \operatorname{ord}(g)k$.
> - $(\mathbb{Z}/p\mathbb{Z})^\times$ has $p - 1$ elements.

#### Cauchy's theorem · P2

If $p$ is a prime dividing $|G|$, then $G$ has an element of order $p$, see Theorem [[§29 The Index and Lagrange's Theorem#^thm-29-6|§29.6]]. *Source: stated in lecture 10/12; cf. Pinter Ch. 13. Proof pending in the notes.*

^nd-thm-29-6

- [ ] Q1 **[state]** State Cauchy's theorem.
- [ ] Q2 **[why]** In what sense is it a partial converse to Lagrange? Why does the full converse fail?
- [ ] Q3 How is it used: why does a Sylow $p$-subgroup argument or the classification of groups of order $p^2$ and $pq$ need elements of order $p$?
- [ ] Q4 **[why]** Name the two standard proof routes (class equation; $\mathbb{Z}/p\mathbb{Z}$ acting on $p$-tuples with product $e$).

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G12 (prime-power counting).
> - Proof pending; it also follows from Sylow I (Theorem [[§52 The Sylow Theorems#^thm-52-4|§52.4]]): a nontrivial $p$-group contains an element of order $p$.

#### When two group elements move $x$ to the same place · P2

$g_1 \star x = g_2 \star x \iff g_1^{-1}g_2 \in \operatorname{Stab}(x) \iff g_1\operatorname{Stab}(x) = g_2\operatorname{Stab}(x)$, see Proposition [[§30 Orbit–Stabilizer#^prop-30-1|§30.1]]. *Source: WS 5.1.*

^nd-prop-30-1

- [ ] Q1 **[state]** State the three equivalent conditions.
- [ ] Q2 (1) $\Leftrightarrow$ (2): which element do you apply to both sides?
- [ ] Q3 (2) $\Leftrightarrow$ (3): which coset criterion is this?
- [ ] Q4 **[why]** Read it for $S_n$ acting on $\{1, \ldots, n\}$ and $x = n$: which [[Group Theory HW Drill#^ps2-1|PS2.1]] statement is it?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G2.
> - Apply $g_1^{-1}$; then $g_1H = g_2H \iff g_1^{-1}g_2 \in H$ (Proposition [[§28 Left and Right Cosets#^prop-28-2|§28.2]]).

#### The orbit bijection · P2

$G/\operatorname{Stab}(x) \to Gx$, $g\operatorname{Stab}(x) \mapsto g \star x$, is well defined and bijective, see Proposition [[§30 Orbit–Stabilizer#^prop-30-2|§30.2]]. *Source: WS 5.2.*

^nd-prop-30-2

- [ ] Q1 **[state]** State the proposition.
- [ ] Q2 Well defined: if $g_1H = g_2H$ with $H = \operatorname{Stab}(x)$, show $g_1 \star x = g_2 \star x$.
- [ ] Q3 Injective: from $g_1 \star x = g_2 \star x$, deduce $g_1H = g_2H$.
- [ ] Q4 Surjective: why is every point of $Gx$ hit?
- [ ] Q5 **[why]** Why are Q2 and Q3 one "if and only if"? Draw the triangle $G \to Gx$ factoring through $G/\operatorname{Stab}(x)$.

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G2 and G4.
> - $g_1 = g_2h$, $h \star x = x$; injectivity applies $g_2^{-1}$.
> - Both directions are Proposition [[§30 Orbit–Stabilizer#^prop-30-1|§30.1]].

#### Orbit–stabilizer theorem · P2

$|G| = |Gx| \cdot |\operatorname{Stab}(x)|$ (in the sense of Lagrange); for finite $G$ every orbit size divides $|G|$, see Theorem [[§30 Orbit–Stabilizer#^thm-30-3|§30.3]]. *Source: WS 5.3; lecture example (four-petal figure).*

^nd-thm-30-3

- [ ] Q1 **[state]** State orbit–stabilizer.
- [ ] Q2 Which bijection gives $|Gx| = [G : \operatorname{Stab}(x)]$?
- [ ] Q3 Why is $\operatorname{Stab}(x)$ a subgroup, so that Lagrange applies? Conclude.
- [ ] Q4 Check it on the lecture's four-petal figure ($|G| = 8$): orbit and stabilizer of a petal tip, and of the centre.
- [ ] Q5 Check it on the cube: faces, edge midpoints, vertices, colours.
- [ ] Q6 **[why]** Which later results are instances (class sizes divide $|G|$, $[S_n : \operatorname{Stab}(n)] = n$, Burnside, fixed points mod $p$)?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G4 (orbit–stabilizer and counting).
> - Proposition [[§30 Orbit–Stabilizer#^prop-30-2|§30.2]], Proposition [[§26 Stabilizers and Fixed Points#^prop-26-1|§26.1]], Theorem [[§29 The Index and Lagrange's Theorem#^thm-29-2|§29.2]].
> - Petals: Example [[§30 Orbit–Stabilizer#^ex-30-1|§30.1]] ($8 = 4 \cdot 2$); cube: Proposition [[§32 Linear Groups, the Cube, S₃ and A₄#^prop-32-3|§32.3]].

#### The action of $G$ on $G/H$ · P2

$g \star g'H = gg'H$ is a well-defined transitive action with $\operatorname{Stab}(eH) = H$ and $\operatorname{Stab}(g'H) = g'Hg'^{-1}$, see Proposition [[§31 G Acting on Coset Spaces#^prop-31-1|§31.1]]. *Source: WS 5.4.*

^nd-prop-31-1

- [ ] Q1 **[state]** State the three parts.
- [ ] Q2 Well defined: if $g'H = g''H$, show $gg'H = gg''H$.
- [ ] Q3 Check the action axioms.
- [ ] Q4 Transitivity: which $g$ moves $g'H$ to $g''H$? Compute $\operatorname{Stab}(eH)$.
- [ ] Q5 Deduce $\operatorname{Stab}(g'H)$ from the conjugate-stabilizer proposition.
- [ ] Q6 **[why]** Why does this make "orbits" and "coset spaces" the same objects? What is the kernel of this action, and which theorem ([[Group Theory HW Drill#^ps3-2|PS3.2]]) uses it?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G2 then G11.
> - $(gg')^{-1}(gg'') = g'^{-1}g'' \in H$; $g = g''g'^{-1}$; $gH = H \iff g \in H$.
> - Corollary [[§26 Stabilizers and Fixed Points#^cor-26-3|§26.3]]; kernel $\bigcap_g gHg^{-1}$, Proposition [[§39 Sources of Normal Subgroups#^prop-39-6|§39.6]] and Theorem [[§39 Sources of Normal Subgroups#^thm-39-5|§39.5]].

#### $GL_3(\mathbb{R})$ acting on $\mathbb{R}^3$ · P2

Two orbits, $\{0\}$ and $\mathbb{R}^3 \setminus \{0\}$; $\operatorname{Stab}(e_1)$ is the invertible matrices with first column $e_1$, see Proposition [[§32 Linear Groups, the Cube, S₃ and A₄#^prop-32-1|§32.1]]. *Source: WS 4.7.*

^nd-prop-32-1

- [ ] Q1 **[state]** State the orbits and the stabilizer of $e_1$.
- [ ] Q2 Why is $\{0\}$ an orbit?
- [ ] Q3 For $v \neq 0$, construct $P \in GL_3(\mathbb{R})$ with $Pe_1 = v$.
- [ ] Q4 Why does $Ae_1 = e_1$ mean "first column $e_1$"? Why is $A$ invertible iff the lower block $B$ is?
- [ ] Q5 **[why]** Compare with $O_3$: why is the $O_3$-stabilizer smaller and its orbit (a sphere) smaller?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G10 (compute in a concrete group).
> - Extend $v$ to a basis $(v, v_2, v_3)$; $\det A = \det B$ by expanding along the first column.
> - Remark [[§32 Linear Groups, the Cube, S₃ and A₄#^rem-32-1|§32]] ($GL_3$ versus $O_3$).

#### $O_3(\mathbb{R})$ acting on $\mathbb{R}^3$ · P2

Orbits $\{0\}$ and the spheres $S_r$; $\operatorname{Stab}(e_1) \cong O_2(\mathbb{R})$ (block matrices $\operatorname{diag}(1, B)$), see Proposition [[§32 Linear Groups, the Cube, S₃ and A₄#^prop-32-2|§32.2]]. *Source: WS 4.8, lecture.*

^nd-prop-32-2

- [ ] Q1 **[state]** State the orbits and $\operatorname{Stab}(e_1)$.
- [ ] Q2 Why does $A \in O_3$ preserve lengths? Conclude each orbit lies in one sphere.
- [ ] Q3 Given $|v| = |w| = r > 0$, build an orthogonal $A$ with $Av = w$.
- [ ] Q4 Why does first column $e_1$ force first row $(1, 0, 0)$ for orthogonal $A$?
- [ ] Q5 **[why]** Why is $O_3 \backslash \mathbb{R}^3 \leftrightarrow \mathbb{R}_{\geq 0}$?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G10.
> - $(Av)^{\mathsf{T}}(Aw) = v^{\mathsf{T}}w$; $A = QP^{\mathsf{T}}$ from two orthonormal bases (Gram–Schmidt).
> - The other columns are orthogonal to $e_1$.

#### Rotational symmetries of the cube · P2

The rotation group $G$ of the cube has order $24$; orbits/stabilizers: faces $6 \cdot 4$, edge midpoints $12 \cdot 2$, vertices $8 \cdot 3$, colours $3 \cdot 8$; with reflections $|G_{\mathrm{all}}| = 48$; the action on faces is faithful, so $G \hookrightarrow S_6$, see Proposition [[§32 Linear Groups, the Cube, S₃ and A₄#^prop-32-3|§32.3]] and Proposition [[§32 Linear Groups, the Cube, S₃ and A₄#^prop-32-4|§32.4]]. *Source: WS 4.9, lecture; faithfulness is a question raised in class.*

^nd-prop-32-3

- [ ] Q1 **[state]** State $|G|$ and the orbit/stabilizer table.
- [ ] Q2 Compute $|G|$ by orbit–stabilizer on faces: orbit size, and which rotations fix a face?
- [ ] Q3 Identify the stabilizer of an edge midpoint and of a vertex. Check $|\text{orbit}| \cdot |\text{Stab}| = 24$ in each row.
- [ ] Q4 Why is the colour row a different set $X$? What is the stabilizer of a colour (order $8$)?
- [ ] Q5 Why is the action on faces faithful? Why is the action on colours not faithful?
- [ ] Q6 **[why]** With reflections, why $48$? Which set does the (not-from-class) isomorphism $G \cong S_4$ use?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G4 and G11.
> - Face stabilizer: rotations by $0, 90, 180, 270$ degrees; edge: one $180^\circ$ rotation; vertex: $120^\circ$ rotations.
> - Faithful: fixing $e_1, e_2, e_3$ forces the identity (linearity); $180^\circ$ face rotations fix each colour (Example [[§32 Linear Groups, the Cube, S₃ and A₄#^ex-32-1|§32.1]]).
> - Body diagonals: Theorem [[§32 Linear Groups, the Cube, S₃ and A₄#^thm-32-5|§32.5]] (proof pending).

### Priority 4 · notes only (Pinter, MATH 412, not from class)

#### Faithful actions embed $G$ in $S_X$ · P4

A faithful action gives an injective $\varphi : G \to S_X$, so $G \cong \varphi(G)$; if $|X| = n$, $G$ embeds in $S_n$, see Proposition [[§25 Actions#^prop-25-4|§25.4]]. *Source: notes.*

^nd-prop-25-4

- [ ] Q1 **[state]** State the proposition.
- [ ] Q2 Why does trivial kernel give injectivity?
- [ ] Q3 Why is an injective homomorphism an isomorphism onto its image?
- [ ] Q4 Given a bijection $f : \{1, \ldots, n\} \to X$, write the isomorphism $S_X \to S_n$ and check it is a homomorphism.
- [ ] Q5 **[why]** Why does a non-faithful action not embed $G$? What does it embed instead (First Isomorphism Theorem)?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G11.
> - $\sigma \mapsto f^{-1} \sigma f$, inverse $\tau \mapsto f \tau f^{-1}$.
> - Non-faithful: $G/\ker \hookrightarrow S_X$ (Theorem [[§41 The First and Second Isomorphism Theorems#^thm-41-1|§41.1]]).

#### Cayley's theorem · P4

Theorem [[§25 Actions#^thm-25-5|§25.5]] → drilled as [[493 Problem Set 3#^hw-3-1|PS3.1]] (part (1)).

#### Every finite group is a matrix group · P4

Corollary [[§25 Actions#^cor-25-6|§25.6]] → drilled as [[493 Problem Set 3#^hw-3-1|PS3.1]] (part (2)).

#### Groups of prime order · P4

Theorem [[§29 The Index and Lagrange's Theorem#^thm-29-7|§29.7]] and Corollary [[§29 The Index and Lagrange's Theorem#^cor-29-8|§29.8]] → drilled as [[493 Problem Set 2#^hw-2-5|PS2.5]].

#### Index of an intersection · P4

Proposition [[§29 The Index and Lagrange's Theorem#^prop-29-9|§29.9]] and Example [[§29 The Index and Lagrange's Theorem#^ex-29-2|§29.2]] → drilled as [[493 Problem Set 5#^hw-5-1|PS5.1]].

#### Left cosets of the point stabilizer record $\alpha(n)$ · P4

Proposition [[§30 Orbit–Stabilizer#^prop-30-4|§30.4]] and Corollary [[§30 Orbit–Stabilizer#^cor-30-5|§30.5]] → drilled as [[493 Problem Set 2#^hw-2-1|PS2.1]].

#### Burnside's lemma · P4

Theorem [[§30 Orbit–Stabilizer#^thm-30-6|§30.6]] → drilled as [[493 Problem Set 3#^hw-3-3|PS3.3]].

# T7. Conjugacy, the center, the class equation, p-groups

## Definitions T7

### Priority 1 · problem sets (directly or extended)

#### Centralizer · P1

$C_G(g) = \{h \in G : hg = gh\}$ (PS 3 writes $Z(g)$, PS 5 writes $Z_G(g)$), see Definition [[§34 Conjugation as an Action and the Class Equation#^def-34-1|§34.1]]. *Source: notes; PS 3.*

^nd-def-34-1

- [ ] Q1 **[def]** Define $C_G(g)$.
- [ ] Q2 **[example]** Compute $C_{S_3}((1\,2))$ and $C_{S_3}((1\,2\,3))$; check $|\operatorname{Conj}(g)| \cdot |C_G(g)| = 6$.
- [ ] Q3 **[use]** Why is $C_G(g)$ a subgroup? (As which stabilizer?)
- [ ] Q4 **[why]** How is $Z(G)$ expressed through centralizers, and when is $C_G(g) = G$?

> [!tip]- Hints: where it lives, examples
> - Stabilizer under conjugation: Proposition [[§34 Conjugation as an Action and the Class Equation#^prop-34-1|§34.1]].
> - $Z(G) = \bigcap_g C_G(g)$: remark [[§34 Conjugation as an Action and the Class Equation#^rem-34-1|§34]].

#### $p$-group · P1

A group of order $p^k$ for a prime $p$ and some $k \geq 0$, see Definition [[§35 The Center#^def-35-3|§35.3]]. *Source: notes ([[Group Theory HW Drill#^ps3-5|PS3.5]]).*

^nd-def-35-3

- [ ] Q1 **[def]** Define a $p$-group.
- [ ] Q2 **[example]** Which of $\mathbb{Z}/8\mathbb{Z}$, $D_4$, $K$, $S_3$, the unitriangular matrices in $GL_3(\mathbb{F}_p)$ are $p$-groups (for which $p$)?
- [ ] Q3 **[use]** State the two main facts about a $p$-group $P$: its center, and fixed points of a $P$-action modulo $p$.
- [ ] Q4 **[why]** Is the trivial group a $p$-group? Why does the center theorem need $k \geq 1$?

> [!tip]- Hints: where it lives, examples
> - Theorem [[§35 The Center#^thm-35-3|§35.3]], Proposition [[§51 p-Groups and Sylow Subgroups#^prop-51-1|§51.1]].
> - Unitriangular: Proposition [[§51 p-Groups and Sylow Subgroups#^prop-51-5|§51.5]].

### Priority 2 · worksheets and lectures

#### Conjugacy class · P2

$\operatorname{Conj}(g) = \{hgh^{-1} : h \in G\}$, the set of conjugates $c_h(g)$ of $g$, see Definition [[§33 Conjugacy Classes#^def-33-1|§33.1]]. *Source: WS 3.*

^nd-def-33-1

- [ ] Q1 **[def]** Define $\operatorname{Conj}(g)$.
- [ ] Q2 **[example]** List the conjugacy classes of $S_3$ and give the class sizes of $S_4$.
- [ ] Q3 **[example]** What is $\operatorname{Conj}(g)$ in an abelian group? What is $\operatorname{Conj}(3I)$ in $GL_2(\mathbb{C})$?
- [ ] Q4 **[use]** Of which action are the conjugacy classes the orbits, and why do they partition $G$?
- [ ] Q5 **[why]** Why is a normal subgroup a union of conjugacy classes, and why must $\{e\}$ be one of them?

> [!tip]- Hints: where it lives, examples
> - Example [[§33 Conjugacy Classes#^ex-33-2|§33.2]] ($1 + 3 + 2$; $1, 6, 3, 8, 6$).
> - Conjugation action: Proposition [[§34 Conjugation as an Action and the Class Equation#^prop-34-1|§34.1]]; normal subgroups: Proposition [[§39 Sources of Normal Subgroups#^prop-39-7|§39.7]].

#### Cycle type · P2

The partition $\lambda(\sigma) = (r_1 \geq \cdots \geq r_k)$ of $n$ given by the cycle lengths of $\sigma \in S_n$ (fixed points as $1$-cycles), see Definition [[§33 Conjugacy Classes#^def-33-2|§33.2]]. *Source: notes (WS 3).*

^nd-def-33-2

- [ ] Q1 **[def]** Define the cycle type of $\sigma \in S_n$.
- [ ] Q2 **[example]** Cycle types of $(1\,2\,3)(4\,5)$, $(1\,2)$ and $e$ in $S_5$.
- [ ] Q3 **[example]** List the five cycle types in $S_4$ with class sizes; which are even?
- [ ] Q4 **[use]** How does cycle type determine order and sign?
- [ ] Q5 **[why]** Why is conjugacy in $A_n$ finer than cycle type? Give $(1\,2\,3)$ and $(1\,3\,2)$ in $A_4$.

> [!tip]- Hints: where it lives, examples
> - Theorem [[§33 Conjugacy Classes#^thm-33-3|§33.3]]: classes of $S_n$ are cycle types.
> - $A_4$: Example [[§43 Simple Groups#^ex-43-1|§43.1]]; $A_5$: Example [[§44 Conjugacy in a Normal Subgroup#^ex-44-1|§44.1]].

#### Similar matrices · P2

$X, Y$ are similar if $X = SYS^{-1}$ for some $S \in GL_n(\mathbb{C})$; similar matrices have the same characteristic polynomial, see Definition [[§33 Conjugacy Classes#^def-33-3|§33.3]]. *Source: lecture 9/9.*

^nd-def-33-3

- [ ] Q1 **[def]** Define similarity, and relate it to conjugacy in $GL_n(\mathbb{C})$.
- [ ] Q2 **[use]** Prove that similar matrices have the same characteristic polynomial.
- [ ] Q3 **[example]** Are $3I$ and $\begin{pmatrix} 3 & 1 \\ 0 & 3 \end{pmatrix}$ similar? Do they have the same characteristic polynomial?
- [ ] Q4 **[why]** Which invariant classifies conjugacy classes in general (Jordan form), and when does the characteristic polynomial suffice?

> [!tip]- Hints: where it lives, examples
> - $\det(xI - SYS^{-1}) = \det(S(xI - Y)S^{-1})$.
> - Distinct eigenvalues: Proposition [[§33 Conjugacy Classes#^prop-33-4|§33.4]]; repeated eigenvalue: remark [[§33 Conjugacy Classes#^rem-33-1|§33]].

#### Central element · P2

$z$ is central if $zg = gz$ for all $g \in G$, see Definition [[§35 The Center#^def-35-1|§35.1]]. *Source: WS 3.*

^nd-def-35-1

- [ ] Q1 **[def]** Define a central element.
- [ ] Q2 **[example]** Which elements of $GL_n(\mathbb{C})$ are central (scalars)? Which of $S_3$?
- [ ] Q3 **[use]** Characterize central elements by their conjugacy class.
- [ ] Q4 **[why]** Why is $e$ always central, and why does that make the class equation start with $|Z(G)| \geq 1$?

> [!tip]- Hints: where it lives, examples
> - Proposition [[§35 The Center#^prop-35-1|§35.1]] (WS 3.5).

#### Center · P2

$Z(G)$ is the set of central elements, see Definition [[§35 The Center#^def-35-2|§35.2]]. *Source: WS 3.*

^nd-def-35-2

- [ ] Q1 **[def]** Define $Z(G)$.
- [ ] Q2 **[example]** $Z(S_3)$, $Z(S_4)$, $Z(\text{abelian } G)$, $Z(GL_2(\mathbb{R}))$.
- [ ] Q3 **[use]** Why is $Z(G)$ a normal subgroup? Of which homomorphism is it the kernel?
- [ ] Q4 **[why]** For a $p$-group, why is $Z(G) \neq \{e\}$, and how does one central element $z \neq e$ start the classification of groups of order $p^2$?

> [!tip]- Hints: where it lives, examples
> - Kernel of $h \mapsto c_h$: Proposition [[§34 Conjugation as an Action and the Class Equation#^prop-34-1|§34.1]], remark [[§35 The Center#^rem-35-1|§35]].
> - Theorem [[§35 The Center#^thm-35-3|§35.3]]; Theorem [[§51 p-Groups and Sylow Subgroups#^thm-51-7|§51.7]].

## Proofs T7

### Priority 1 · problem sets (directly or extended)

#### The conjugation action · P1

$h \star g = hgh^{-1}$ is an action with orbits $\operatorname{Conj}(g)$, stabilizers $C_G(g)$, one-point orbits the central elements, and kernel $Z(G)$, see Proposition [[§34 Conjugation as an Action and the Class Equation#^prop-34-1|§34.1]]. *Source: notes ([[Group Theory HW Drill#^ps3-4|PS3.4]] background).*

^nd-prop-34-1

- [ ] Q1 **[state]** State the four claims (orbit, stabilizer, one-point orbits, kernel).
- [ ] Q2 Check the action axioms.
- [ ] Q3 Why is the stabilizer $C_G(g)$, and why is it a subgroup?
- [ ] Q4 Why is the orbit $\{g\}$ iff $g$ is central?
- [ ] Q5 Identify the homomorphism $G \to S_G$ and its kernel and image.
- [ ] Q6 **[why]** Deduce with orbit–stabilizer that class sizes divide $|G|$ ([[Group Theory HW Drill#^ps3-4-1|PS3.4(1)]]).

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G4 and G11.
> - $h_1(h_2gh_2^{-1})h_1^{-1} = (h_1h_2)g(h_1h_2)^{-1}$; $hgh^{-1} = g \iff hg = gh$.
> - Image: inner automorphisms; kernel: $Z(G)$.

#### Groups of order 4 are abelian · P1

Every group of order $4$ is abelian, see Proposition [[§34 Conjugation as an Action and the Class Equation#^prop-34-6|§34.6]]. *Source: not from class (used in WS 9.1 for $K$, and in [[Group Theory HW Drill#^ps3-6|PS3.6]]).*

^nd-prop-34-6

- [ ] Q1 **[state]** State the proposition.
- [ ] Q2 Which element orders are possible, and why?
- [ ] Q3 If some element has order $4$, conclude.
- [ ] Q4 Otherwise $x^2 = e$ for all $x$: show $ab = ba$.
- [ ] Q5 **[why]** Name the two groups of order $4$. Why does this exclude $|G| = 4$ in [[Group Theory HW Drill#^ps3-6|PS3.6]]?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G3.
> - $ab = (ab)^{-1} = b^{-1}a^{-1} = ba$.
> - $\mathbb{Z}/4\mathbb{Z}$ and $K$; abelian means $4$ singleton classes (Corollary [[§34 Conjugation as an Action and the Class Equation#^cor-34-7|§34.7]]).

### Priority 2 · worksheets and lectures

#### Conjugation relabels the entries · P2

$\sigma(a_1\ \cdots\ a_r)\sigma^{-1} = (\sigma(a_1)\ \cdots\ \sigma(a_r))$, and for a product of disjoint cycles $\sigma$ is applied to every entry, preserving cycle type, see Lemma [[§33 Conjugacy Classes#^lem-33-1|§33.1]]. *Source: WS 3 (via §12).*

^nd-lem-33-1

- [ ] Q1 **[state]** State the lemma for one cycle and for a disjoint product.
- [ ] Q2 One cycle: compute $(\sigma c\sigma^{-1})(\sigma(a_i))$, and explain why a point not of the form $\sigma(a_i)$ is fixed.
- [ ] Q3 Product: why does $\sigma c_1 \cdots c_k \sigma^{-1} = (\sigma c_1\sigma^{-1}) \cdots (\sigma c_k\sigma^{-1})$?
- [ ] Q4 Why are the relabelled cycles still disjoint?
- [ ] Q5 **[why]** Why does this make conjugation preserve order and sign?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G6 (conjugation preserves cycle type).
> - Insert $\sigma^{-1}\sigma$ between factors; $\sigma$ is injective, so disjoint supports stay disjoint.

#### Conjugacy class of $(1\,2)$ in $S_n$ · P2

$\operatorname{Conj}((1\,2))$ is the set of all $\binom{n}{2}$ transpositions, see Proposition [[§33 Conjugacy Classes#^prop-33-2|§33.2]]. *Source: WS 3.2.*

^nd-prop-33-2

- [ ] Q1 **[state]** State the proposition.
- [ ] Q2 ($\subseteq$) Compute $\tau(1\,2)\tau^{-1}$.
- [ ] Q3 ($\supseteq$) Given $(i\ j)$, which $\tau$ conjugates $(1\,2)$ to it?
- [ ] Q4 Count the transpositions.
- [ ] Q5 **[why]** Use orbit–stabilizer to find $|C_{S_n}((1\,2))|$. Why is the class of $(1\,2)$ in $A_n$ not defined?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G6.
> - $\tau(1\,2)\tau^{-1} = (\tau(1)\ \tau(2))$ by Lemma [[§33 Conjugacy Classes#^lem-33-1|§33.1]]; choose $\tau(1) = i$, $\tau(2) = j$.
> - $|C| = n!/\binom{n}{2} = 2(n-2)!$.

#### Conjugacy classes in $S_n$ are cycle types · P2

$\sigma, \sigma'$ are conjugate in $S_n$ iff $\lambda(\sigma) = \lambda(\sigma')$; classes correspond to partitions of $n$, see Theorem [[§33 Conjugacy Classes#^thm-33-3|§33.3]]. *Source: notes (WS 3).*

^nd-thm-33-3

- [ ] Q1 **[state]** State the theorem.
- [ ] Q2 ($\Rightarrow$) Which lemma gives it?
- [ ] Q3 ($\Leftarrow$) With both decompositions written in the same length order, define $\tau$ by $\tau(a_{i,j}) = b_{i,j}$. Why is $\tau$ a well-defined bijection?
- [ ] Q4 Compute $\tau\sigma\tau^{-1}$.
- [ ] Q5 Find $\tau$ with $\tau(1\,2\,3)(4\,5)\tau^{-1} = (2\,5\,1)(3\,4)$. Is $\tau$ unique?
- [ ] Q6 **[why]** Why can the theorem fail in $A_n$? Which extra condition (centralizer meets $S_n \setminus A_n$) decides it?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G6.
> - Both entry lists enumerate $\{1, \ldots, n\}$ without repetition, so $\tau$ matches them.
> - Example [[§33 Conjugacy Classes#^ex-33-1|§33.1]]; $A_n$: Proposition [[§44 Conjugacy in a Normal Subgroup#^prop-44-1|§44.1]].

#### Conjugacy class of a diagonal matrix · P2

The class of $D = \operatorname{diag}(3, 4)$ in $GL_2(\mathbb{C})$ is $\{A : \det(xI - A) = (x-3)(x-4)\} = \{A : \operatorname{tr}A = 7, \det A = 12\}$, see Proposition [[§33 Conjugacy Classes#^prop-33-4|§33.4]]. *Source: WS 3.3.*

^nd-prop-33-4

- [ ] Q1 **[state]** State the proposition.
- [ ] Q2 ($\subseteq$) Why does $A = SDS^{-1}$ have characteristic polynomial $(x-3)(x-4)$?
- [ ] Q3 ($\supseteq$) Choose eigenvectors $v_3, v_4$. Why are they independent?
- [ ] Q4 With $S = [v_3 \mid v_4]$, show $AS = SD$.
- [ ] Q5 Why is the condition equivalent to $\operatorname{tr}A = 7$, $\det A = 12$, and why is such $A$ invertible?
- [ ] Q6 **[why]** Where are distinct eigenvalues used? What goes wrong for $3I$?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G10.
> - Independence: apply $A$ to $av_3 + bv_4 = 0$ and subtract.
> - Remark [[§33 Conjugacy Classes#^rem-33-1|§33]]: $\operatorname{Conj}(3I) = \{3I\}$, and $\begin{pmatrix} 3 & 1 \\ 0 & 3 \end{pmatrix}$ is not similar to $3I$.

#### Central iff singleton conjugacy class · P2

$z$ is central iff $\operatorname{Conj}(z) = \{z\}$, see Proposition [[§35 The Center#^prop-35-1|§35.1]]. *Source: WS 3.5.*

^nd-prop-35-1

- [ ] Q1 **[state]** State the proposition.
- [ ] Q2 Why is $z \in \operatorname{Conj}(z)$ always?
- [ ] Q3 Translate $\operatorname{Conj}(z) = \{z\}$ into $gzg^{-1} = z$ for all $g$, then into $gz = zg$.
- [ ] Q4 **[why]** In action language, the center is the set of fixed points of which action?

> [!tip]- Hints: route of the proof in the notes
> - Multiply $gzg^{-1} = z$ on the right by $g$.
> - Remark [[§34 Conjugation as an Action and the Class Equation#^rem-34-2|§34]].

#### The center is a subgroup · P2

$Z(G)$ is an abelian subgroup of $G$, and $Z(G) = G$ iff $G$ is abelian, see Proposition [[§35 The Center#^prop-35-2|§35.2]]. *Source: WS 3.6.*

^nd-prop-35-2

- [ ] Q1 **[state]** State the proposition.
- [ ] Q2 Check $e \in Z(G)$ and closure under products (write out the chain of equalities).
- [ ] Q3 Closure under inverses: from $zg = gz$, deduce $z^{-1}g = gz^{-1}$.
- [ ] Q4 Why is $Z(G)$ abelian, and why $Z(G) = G$ iff $G$ abelian?
- [ ] Q5 **[why]** Give the second proof via a kernel. Which stronger conclusion does it give?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G1, or G5 (kernel of $h \mapsto c_h$).
> - Multiply $zg = gz$ by $z^{-1}$ on both sides.
> - Remark [[§35 The Center#^rem-35-1|§35]]: kernels are normal.

### Priority 3 · filled in, using a technique the problem sets drill

#### The class equation · P3

$|G| = |Z(G)| + \sum_{i=1}^r [G : C_G(g_i)]$ over representatives of the non-singleton classes, each summand a divisor of $|G|$ greater than $1$, see Theorem [[§34 Conjugation as an Action and the Class Equation#^thm-34-4|§34.4]]. *Source: cf. Pinter Ch. 15, Ex. G (used for $p$-groups and Sylow).*

^nd-thm-34-4

- [ ] Q1 **[state]** State the class equation.
- [ ] Q2 Which partition of $G$ do you count?
- [ ] Q3 Why are the one-element classes exactly $\{z\}$, $z \in Z(G)$?
- [ ] Q4 Why does each non-singleton class have size $[G : C_G(g_i)]$, a divisor of $|G|$ bigger than $1$?
- [ ] Q5 Write the class equations of $S_3$ and $S_4$.
- [ ] Q6 **[why]** Why does it immediately give $p \mid |Z(G)|$ for a $p$-group?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G4.
> - Orbits partition (Proposition [[§27 Orbits#^prop-27-1|§27.1]]); one-point orbits (Proposition [[§34 Conjugation as an Action and the Class Equation#^prop-34-1|§34.1]](3)); sizes (Corollary [[§34 Conjugation as an Action and the Class Equation#^cor-34-2|§34.2]]).
> - Example [[§34 Conjugation as an Action and the Class Equation#^ex-34-1|§34.1]]: $6 = 1 + 3 + 2$, $24 = 1 + 6 + 3 + 8 + 6$.

#### $p$ divides the order of the center · P3

If $|G| = p^k$, $k \geq 1$, then $p \mid |Z(G)|$, so $|Z(G)| \geq p$, see Corollary [[§35 The Center#^cor-35-4|§35.4]]. *Source: notes.*

^nd-cor-35-4

- [ ] Q1 **[state]** State the corollary.
- [ ] Q2 Write the class equation for $G$. Why is every $[G : C_G(g_i)]$ a positive power of $p$?
- [ ] Q3 Conclude $p \mid |Z(G)|$.
- [ ] Q4 Why does $|Z(G)| \geq 1$ upgrade to $|Z(G)| \geq p$?
- [ ] Q5 **[why]** For $|G| = p^2$, which values can $|Z(G)|$ take a priori? Compare with the route of [[Group Theory HW Drill#^ps6-3|PS6.3]], which needs only one central $z \neq e$.

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G12 (prime-power counting) via G4.
> - Theorem [[§34 Conjugation as an Action and the Class Equation#^thm-34-4|§34.4]]; divisors of $p^k$ are powers of $p$.
> - Theorem [[§51 p-Groups and Sylow Subgroups#^thm-51-7|§51.7]] ([[Group Theory HW Drill#^ps6-3|PS6.3]]) uses Theorem [[§35 The Center#^thm-35-3|§35.3]] (one central $z \neq e$), not this corollary.

### Priority 4 · notes only (Pinter, MATH 412, not from class)

#### Class sizes divide the group order; reciprocal class equation · P4

Corollaries [[§34 Conjugation as an Action and the Class Equation#^cor-34-2|§34.2]] and [[§34 Conjugation as an Action and the Class Equation#^cor-34-3|§34.3]] → drilled as [[493 Problem Set 3#^hw-3-4|PS3.4]].

#### Three conjugacy classes force order at most $6$ · P4

Proposition [[§34 Conjugation as an Action and the Class Equation#^prop-34-5|§34.5]] and Corollary [[§34 Conjugation as an Action and the Class Equation#^cor-34-7|§34.7]] → drilled as [[493 Problem Set 3#^hw-3-6|PS3.6]].

#### Groups of prime-power order have nontrivial center · P4

Theorem [[§35 The Center#^thm-35-3|§35.3]] → drilled as [[493 Problem Set 3#^hw-3-5|PS3.5]].

# T8. Normal subgroups, quotients, isomorphism theorems, simple groups

## Definitions T8

### Priority 2 · worksheets and lectures

#### Normal subgroup · P2

$H \leq G$ is normal, $H \trianglelefteq G$, if $gHg^{-1} \subseteq H$ for all $g \in G$, i.e. $ghg^{-1} \in H$ for all $g \in G$, $h \in H$, see Definition [[§38 Normal Subgroups#^def-38-1|§38.1]]. *Source: lecture 9/21; WS 6.*

^nd-def-38-1

- [ ] Q1 **[def]** Define a normal subgroup. Why is "$\subseteq$" enough (rather than "$=$")?
- [ ] Q2 **[example]** Normal: $A_n \trianglelefteq S_n$, $SL_n \trianglelefteq GL_n$, $Z(G) \trianglelefteq G$, $K \trianglelefteq S_4$, every subgroup of an abelian group. Give the reason for each.
- [ ] Q3 **[example]** Not normal: $\{e, (1\,2)\} \leq S_3$; the diagonal matrices in $GL_2(\mathbb{R})$; $\{e, (1\,2)(3\,4)\} \leq S_4$.
- [ ] Q4 **[use]** List four equivalent conditions (conjugates, cosets, conjugacy classes, coset multiplication).
- [ ] Q5 **[why]** Why is normality exactly what makes $G/H$ a group? Is normality transitive?

> [!tip]- Hints: where it lives, examples
> - Characterizations: Proposition [[§38 Normal Subgroups#^prop-38-2|§38.2]], Theorem [[§38 Normal Subgroups#^thm-38-3|§38.3]], Proposition [[§39 Sources of Normal Subgroups#^prop-39-7|§39.7]].
> - Examples [[§39 Sources of Normal Subgroups#^ex-39-1|§39.1]], [[§39 Sources of Normal Subgroups#^ex-39-2|§39.2]], [[§38 Normal Subgroups#^ex-38-1|§38.1]]; not transitive: Example [[§39 Sources of Normal Subgroups#^ex-39-4|§39.4]] ([[Group Theory HW Drill#^ps6-1|PS6.1]]).

#### The Klein four-group $K$ · P2

$K = \{e, (1\,2)(3\,4), (1\,3)(2\,4), (1\,4)(2\,3)\} \subseteq S_4$, see Definition [[§39 Sources of Normal Subgroups#^def-39-1|§39.1]]. *Source: lecture 9/30.*

^nd-def-39-1

- [ ] Q1 **[def]** List the elements of $K$.
- [ ] Q2 **[example]** Why is $K$ an abelian subgroup isomorphic to $\mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/2\mathbb{Z}$ (and to $U_8$)?
- [ ] Q3 **[use]** Why is $K$ normal in $S_4$ (two reasons: class sizes; kernel of the pair-partition map)?
- [ ] Q4 **[why]** Why does $K$ show that $A_4$ is not simple and that the $A_n$ simplicity proof needs $n \geq 5$?

> [!tip]- Hints: where it lives, examples
> - Proposition [[§39 Sources of Normal Subgroups#^prop-39-8|§39.8]]; Example [[§39 Sources of Normal Subgroups#^ex-39-3|§39.3]] ($1 + 3 = 4$).
> - Kernel of $S_4 \to S_3$: Proposition [[§43 Simple Groups#^prop-43-10|§43.10]]; remark [[§43 Simple Groups#^rem-43-7|§43]] (why $n \geq 5$).

#### Quotient group · P2

For $N \trianglelefteq G$, $G/N = \{gN\}$ with $(g_1N)(g_2N) = (g_1g_2)N$, and canonical projection $\pi(g) = gN$, see Definition [[§40 Quotient Groups#^def-40-1|§40.1]]. *Source: lecture 9/25.*

^nd-def-40-1

- [ ] Q1 **[def]** Define $G/N$ and $\pi$.
- [ ] Q2 **[example]** Identify $\mathbb{Z}/n\mathbb{Z}$, $G/G$, $G/\{e\}$, $S_3/A_3$, $S_n/A_n$, $GL_n(k)/SL_n(k)$, $S_4/K$.
- [ ] Q3 **[use]** What are the identity, inverses and order of $G/N$?
- [ ] Q4 **[why]** Why must $N$ be normal for the operation to make sense? What fails for $\{e, (1\,2)\} \leq S_3$?

> [!tip]- Hints: where it lives, examples
> - Examples [[§40 Quotient Groups#^ex-40-1|§40.1]], [[§41 The First and Second Isomorphism Theorems#^ex-41-1|§41.1]]; $S_4/K \cong S_3$: Proposition [[§43 Simple Groups#^prop-43-10|§43.10]].
> - Well-definedness: Proposition [[§37 Multiplying Cosets#^prop-37-1|§37.1]].

#### Set of representatives · P2

$S \subseteq G$ meeting every coset of $N$ in exactly one element, i.e. $G = \bigsqcup_{s \in S} sN$, so $s \mapsto sN$ is a bijection $S \to G/N$, see Definition [[§40 Quotient Groups#^def-40-2|§40.2]]. *Source: lecture 10/2.*

^nd-def-40-2

- [ ] Q1 **[def]** Define a set of representatives for $G/N$.
- [ ] Q2 **[example]** Give one for $(\mathbb{Z}/4\mathbb{Z})/\{0, 2\}$ and for $S_3/A_3$. Which one is a subgroup?
- [ ] Q3 **[use]** How do you multiply in $G/N$ using $S$?
- [ ] Q4 **[why]** Why can no subgroup of $\mathbb{Z}/4\mathbb{Z}$ be a set of representatives for $\{0, 2\}$?

> [!tip]- Hints: where it lives, examples
> - Proposition [[§40 Quotient Groups#^prop-40-3|§40.3]]; Examples [[§40 Quotient Groups#^ex-40-2|§40.2]], [[§40 Quotient Groups#^ex-40-3|§40.3]]; remark [[§40 Quotient Groups#^rem-40-3|§40]].

#### The product set $HN$ · P2

$HN = \{hn : h \in H, n \in N\}$ for subgroups $H, N$, see Definition [[§41 The First and Second Isomorphism Theorems#^def-41-1|§41.1]]. *Source: lecture 10/2.*

^nd-def-41-1

- [ ] Q1 **[def]** Define $HN$.
- [ ] Q2 **[example]** In $S_3$, compute $AB$ for $A = \langle (1\,2) \rangle$, $B = \langle (1\,3) \rangle$. Is it a subgroup?
- [ ] Q3 **[use]** When is $HN$ a subgroup, and what is $|HN|$ for finite $H, N$?
- [ ] Q4 **[why]** Compute $SL_2(\mathbb{R})Z$ for $Z$ the scalar matrices.

> [!tip]- Hints: where it lives, examples
> - Lemma [[§41 The First and Second Isomorphism Theorems#^lem-41-3|§41.3]], Example [[§41 The First and Second Isomorphism Theorems#^ex-41-2|§41.2]], Corollary [[§41 The First and Second Isomorphism Theorems#^cor-41-6|§41.6]], Lemma [[§52 The Sylow Theorems#^lem-52-8|§52.8]].
> - $GL_2^+(\mathbb{R})$: Example [[§45 S₃, S₄, A₄ and A₅#^ex-45-3|§45.3]].

#### Simple group · P2

$G$ is simple if it has exactly two normal subgroups, $\{e\}$ and $G$ (so $G \neq \{e\}$), see Definition [[§43 Simple Groups#^def-43-1|§43.1]]. *Source: lecture 9/21, 9/28; WS 7.*

^nd-def-43-1

- [ ] Q1 **[def]** Define a simple group. Why is the trivial group not simple?
- [ ] Q2 **[example]** Simple: $\mathbb{Z}/p\mathbb{Z}$, $A_5$, $A_n$ ($n \geq 5$), $PSL_n(F)$ (with two exceptions). Not simple: $S_n$ ($n \geq 3$), $A_4$, $\mathbb{Z}$, $\mathbb{Z}/6\mathbb{Z}$.
- [ ] Q3 **[use]** What can a homomorphism out of a simple group be?
- [ ] Q4 **[why]** Why does a non-normal proper subgroup not count against simplicity? Why are simple groups "building blocks"?

> [!tip]- Hints: where it lives, examples
> - Theorem [[§43 Simple Groups#^thm-43-1|§43.1]], Proposition [[§43 Simple Groups#^prop-43-6|§43.6]], Theorem [[§43 Simple Groups#^thm-43-9|§43.9]], Corollary [[§43 Simple Groups#^cor-43-11|§43.11]].
> - Homomorphisms out: Proposition [[§43 Simple Groups#^prop-43-3|§43.3]].

#### Projective special linear group · P2

$PSL_n(F) = SL_n(F)/Z$ with $Z = \{\zeta I_n : \zeta^n = 1\}$ the scalar matrices in $SL_n(F)$, see Definition [[§43 Simple Groups#^def-43-2|§43.2]]. *Source: WS 7.*

^nd-def-43-2

- [ ] Q1 **[def]** Define $Z$ and $PSL_n(F)$.
- [ ] Q2 **[use]** Why is $Z$ normal in $SL_n(F)$?
- [ ] Q3 **[example]** What is $Z$ for $SL_2(\mathbb{R})$? Identify $PSL_2(\mathbb{F}_2)$ and $PSL_2(\mathbb{F}_3)$.
- [ ] Q4 **[why]** Why is $PSL_1(F)$ not simple? Which two $PSL_2$ are the exceptions, and why are they not simple?

> [!tip]- Hints: where it lives, examples
> - Scalars are central. $Z = \{\pm I_2\}$ in $SL_2(\mathbb{R})$; Example [[§45 S₃, S₄, A₄ and A₅#^ex-45-3|§45.3]] gives $GL_2^+(\mathbb{R})/\text{scalars} \cong PSL_2(\mathbb{R})$.
> - Example [[§43 Simple Groups#^ex-43-3|§43.3]]: $PSL_2(\mathbb{F}_2) \cong S_3$, $PSL_2(\mathbb{F}_3) \cong A_4$.

## Proofs T8

### Priority 1 · problem sets (directly or extended)

#### Abelian simple groups · P1

An abelian group is simple iff it is $\cong \mathbb{Z}/p\mathbb{Z}$, $p$ prime, see Theorem [[§43 Simple Groups#^thm-43-1|§43.1]]. *Source: lecture 9/21; ($\Leftarrow$) is WS 7.3; the second proof of ($\Rightarrow$) is [[Group Theory HW Drill#^ps6-2|PS6.2]] (drilled as [[493 Problem Set 6#^hw-6-2|PS6.2]]).*

^nd-thm-43-1

- [ ] Q1 **[state]** State the theorem.
- [ ] Q2 ($\Leftarrow$) Why does a group of prime order have no proper nontrivial subgroups?
- [ ] Q3 ($\Rightarrow$) Pick $g \neq e$. Why is $\langle g \rangle = G$?
- [ ] Q4 Why is $G$ not infinite cyclic?
- [ ] Q5 If $|G| = n = ab$ with $1 < a < n$, which subgroup is proper, nontrivial and normal?
- [ ] Q6 **[why]** Where is "abelian" used? Why is it not enough for a non-abelian group to have no proper nontrivial normal cyclic subgroup?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G3 and G13.
> - Abelian: every subgroup normal; $\mathbb{Z} \supsetneq 2\mathbb{Z}$; $g^a$ has order $b$.
> - Corollary [[§29 The Index and Lagrange's Theorem#^cor-29-8|§29.8]].

### Priority 2 · worksheets and lectures

#### When coset multiplication is well defined · P2

$(g_1H)(g_2H) := (g_1g_2)H$ is well defined on $G/H$ iff $gHg^{-1} \subseteq H$ for all $g$, see Proposition [[§37 Multiplying Cosets#^prop-37-1|§37.1]]; a second proof of ($\Leftarrow$) multiplies cosets as sets, see remark [[§38 Normal Subgroups#^rem-38-3|§38]]. *Source: lecture 9/21; second proof lecture 9/25.*

^nd-prop-37-1

- [ ] Q1 **[state]** State the proposition. What exactly does "well defined" mean here?
- [ ] Q2 Translate the hypotheses $u_1H = u_2H$, $v_1H = v_2H$ and the conclusion into membership in $H$.
- [ ] Q3 Factor $(u_1v_1)^{-1}(u_2v_2)$ so that one factor is visibly in $H$. What remains to be in $H$?
- [ ] Q4 ($\Leftarrow$) Which $g$ do you use?
- [ ] Q5 ($\Rightarrow$) Which choice of $u_1, u_2, v_1, v_2$ produces $ghg^{-1} \in H$?
- [ ] Q6 Give the set-product proof: $g_1g_2N = g_1Ng_2' = \cdots$. Which characterization of normality does it use?
- [ ] Q7 **[why]** Show directly that coset multiplication is not well defined for $H = \{e, (1\,2)\} \leq S_3$.

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G2 (well-definedness on representatives).
> - $(u_1v_1)^{-1}(u_2v_2) = (v_1^{-1}(u_1^{-1}u_2)v_1)(v_1^{-1}v_2)$.
> - ($\Rightarrow$): $u_1 = e$, $u_2 = h$, $v_1 = v_2 = g^{-1}$.
> - Second proof uses $g_2'N = Ng_2'$ (Proposition [[§38 Normal Subgroups#^prop-38-2|§38.2]]).

#### First examples of normal subgroups · P2

Every subgroup of an abelian group is normal; $\{e\}$ and $G$ are normal in $G$, see Proposition [[§38 Normal Subgroups#^prop-38-1|§38.1]]. *Source: lecture 9/21.*

^nd-prop-38-1

- [ ] Q1 **[state]** State both parts.
- [ ] Q2 Prove (1) in one line.
- [ ] Q3 Prove (2).
- [ ] Q4 **[why]** Where must you look for a non-normal subgroup? Give the smallest example.

> [!tip]- Hints: route of the proof in the notes
> - $ghg^{-1} = hgg^{-1} = h$.
> - Non-abelian group, proper nontrivial subgroup: $\{e, (1\,2)\} \leq S_3$ (remark [[§38 Normal Subgroups#^rem-38-1|§38]]).

#### Characterizations of normality · P2

For $H \leq G$, TFAE: $gHg^{-1} \subseteq H$ for all $g$; $gHg^{-1} = H$ for all $g$; $gH = Hg$ for all $g$; the set of left cosets equals the set of right cosets, see Proposition [[§38 Normal Subgroups#^prop-38-2|§38.2]]. *Source: lecture 9/21, 9/25.*

^nd-prop-38-2

- [ ] Q1 **[state]** State the four conditions.
- [ ] Q2 (1) $\Rightarrow$ (2): to show $H \subseteq gHg^{-1}$, apply (1) to which element?
- [ ] Q3 (2) $\Leftrightarrow$ (3): what does "multiply a set equality by $g$" mean, and why is it legitimate?
- [ ] Q4 (4) $\Rightarrow$ (3): why is the left coset $gH$, which is some right coset, equal to $Hg$?
- [ ] Q5 Give the direct (1) $\Rightarrow$ (3) argument from lecture 9/25.
- [ ] Q6 **[why]** Why is "for all $g$" essential? (Find $g$ with $gH = Hg$ for a non-normal $H$.)

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G6.
> - $h' = g^{-1}hg \in H$, so $h = gh'g^{-1}$.
> - Right cosets partition $G$ and the one containing $g$ is $Hg$.
> - Direct: $gn = (gng^{-1})g$ and $ng = g(g^{-1}ng)$.

#### Five characterizations of normality · P2

For $N \leq G$, TFAE: (1) $gNg^{-1} = N$ for all $g$; (2) $N$ is a union of conjugacy classes; (3) all points of $G/N$ have the same stabilizer for $G \curvearrowright G/N$; (4) every left coset is a right coset; (5) coset multiplication is well defined, see Theorem [[§38 Normal Subgroups#^thm-38-3|§38.3]]. *Source: WS 6.1. Proof pending in the notes (four of the five links are proved elsewhere).*

^nd-thm-38-3

- [ ] Q1 **[state]** State the five conditions.
- [ ] Q2 **[why]** Which earlier results already prove (1) $\Leftrightarrow$ (4), (1) $\Leftrightarrow$ (5) and (1) $\Leftrightarrow$ (2)?
- [ ] Q3 For (3): what is $\operatorname{Stab}(gN)$ for the action on $G/N$? Why does "all stabilizers equal" mean $gNg^{-1} = N$?
- [ ] Q4 **[use]** Which condition do you use to prove: index $2$ is normal; $A_5$ is simple; $G/N$ is a group?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G6, G13.
> - Remark [[§38 Normal Subgroups#^rem-38-4|§38]] maps each condition to its proof: Proposition [[§38 Normal Subgroups#^prop-38-2|§38.2]], Proposition [[§37 Multiplying Cosets#^prop-37-1|§37.1]], Proposition [[§39 Sources of Normal Subgroups#^prop-39-7|§39.7]].
> - (3): $\operatorname{Stab}(gN) = gNg^{-1}$ and $\operatorname{Stab}(eN) = N$ (Proposition [[§31 G Acting on Coset Spaces#^prop-31-1|§31.1]]).

#### A non-normal subgroup and index-2 examples · P2

$\{e, (1\,2)\}$ is not normal in $S_3$; $\langle (1\,2\,3) \rangle \trianglelefteq S_3$ and $A_n \trianglelefteq S_n$ have index $2$, see Example [[§38 Normal Subgroups#^ex-38-1|§38.1]] and Example [[§39 Sources of Normal Subgroups#^ex-39-1|§39.1]]. *Source: lecture 9/21; WS 6.2.*

^nd-ex-38-1

- [ ] Q1 **[state]** State which subgroups of $S_3$ are normal, and which are not.
- [ ] Q2 Show $\{e, (1\,2)\}$ is not normal in two ways: by cosets and by one conjugation.
- [ ] Q3 Why is $\langle (1\,2\,3) \rangle$ normal without any computation?
- [ ] Q4 Why is $A_n$ normal in $S_n$ (two proofs)?
- [ ] Q5 **[why]** Why would $\langle (1\,2\,3) \rangle$ have been a poor choice for a non-normal example?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G10 and G13.
> - $(1\,3)(1\,2)(1\,3)^{-1} = (2\,3)$; $(1\,3)H \neq H(1\,3)$ (Example [[§28 Left and Right Cosets#^ex-28-1|§28.1]]).
> - Index $2$ (Proposition [[§39 Sources of Normal Subgroups#^prop-39-1|§39.1]]); $A_n = \operatorname{Ker}\operatorname{sgn}$.

#### Subgroups of index 2 are normal · P2

If $[G : H] = 2$ then $H \trianglelefteq G$, see Proposition [[§39 Sources of Normal Subgroups#^prop-39-1|§39.1]]. *Source: lecture 9/21.*

^nd-prop-39-1

- [ ] Q1 **[state]** State the proposition.
- [ ] Q2 What are the two left cosets? Why is the second the complement $G \setminus H$?
- [ ] Q3 Why are there exactly two right cosets, and what are they?
- [ ] Q4 Which characterization of normality concludes?
- [ ] Q5 **[why]** Is a subgroup of index $3$ necessarily normal? (Look in $S_3$.) Where is index $2$ used later ($A_4$ has no subgroup of order $6$)?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G13.
> - Left/right counts agree (Proposition [[§28 Left and Right Cosets#^prop-28-3|§28.3]]); condition (4) of Proposition [[§38 Normal Subgroups#^prop-38-2|§38.2]].
> - Index $3$: $\{e, (1\,2)\} \leq S_3$; $A_4$: Example [[§29 The Index and Lagrange's Theorem#^ex-29-1|§29.1]].

#### Kernels are normal · P2

$\operatorname{Ker}\varphi \trianglelefteq G_1$ for every homomorphism $\varphi : G_1 \to G_2$, see Proposition [[§39 Sources of Normal Subgroups#^prop-39-2|§39.2]]. *Source: lecture 9/21; WS 6.4.*

^nd-prop-39-2

- [ ] Q1 **[state]** State the proposition.
- [ ] Q2 Why is the kernel a subgroup?
- [ ] Q3 For $h \in \operatorname{Ker}\varphi$, compute $\varphi(ghg^{-1})$.
- [ ] Q4 Give three examples: $A_n$, $SL_n$, $Z(G)$ (as kernels of what?).
- [ ] Q5 **[why]** What is the converse, and how is it proved?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G5 (kernels and the First Isomorphism Theorem).
> - $\varphi(g)\,e\,\varphi(g)^{-1} = e$.
> - Examples [[§39 Sources of Normal Subgroups#^ex-39-2|§39.2]]; converse: Proposition [[§40 Quotient Groups#^prop-40-2|§40.2]].

#### Images need not be normal · P2

The inclusion $\langle (1\,2) \rangle \to S_3$ has non-normal image, see Proposition [[§39 Sources of Normal Subgroups#^prop-39-3|§39.3]]. *Source: WS 6.5; lecture 9/25.*

^nd-prop-39-3

- [ ] Q1 **[state]** State the proposition with the example.
- [ ] Q2 Why is the inclusion a homomorphism?
- [ ] Q3 Why is its image not normal?
- [ ] Q4 **[why]** Why does the proof that kernels are normal not dualize to images? Which consequence for homomorphisms into simple groups (WS 7.2)?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G10.
> - $(1\,3)(1\,2)(1\,3)^{-1} = (2\,3)$.
> - Remark [[§43 Simple Groups#^rem-43-4|§43]]; Proposition [[§43 Simple Groups#^prop-43-4|§43.4]].

#### Preimages and images of normal subgroups · P2

For $N \trianglelefteq G$: preimages $\varphi^{-1}(N)$ under $\varphi : F \to G$ are normal; images $\psi(N)$ need not be normal, but are normal if $\psi$ is surjective, see Proposition [[§39 Sources of Normal Subgroups#^prop-39-4|§39.4]]. *Source: WS 6.6. Proof pending in the notes.*

^nd-prop-39-4

- [ ] Q1 **[state]** State the three parts.
- [ ] Q2 **[why]** Give a counterexample for (2). Where does surjectivity enter (3)?
- [ ] Q3 For (1): if $x \in \varphi^{-1}(N)$ and $f \in F$, what is $\varphi(fxf^{-1})$?
- [ ] Q4 **[use]** Where are (1) and (3) used: the correspondence theorem, $\pi(A) \trianglelefteq G/N$ for $A \trianglelefteq G$?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G9 (move properties along maps).
> - (2): $N = \langle (1\,2) \rangle \trianglelefteq \langle (1\,2) \rangle$ included in $S_3$; (3): every element of $H$ is $\psi(g)$, so $\psi(g)\psi(n)\psi(g)^{-1} = \psi(gng^{-1})$.
> - Compare Proposition [[§42 The Correspondence and Third Isomorphism Theorems#^prop-42-1|§42.1]].

#### $K$ is an abelian subgroup of $S_4$ · P2

$K \leq S_4$ is abelian and isomorphic to $\mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/2\mathbb{Z}$, see Proposition [[§39 Sources of Normal Subgroups#^prop-39-8|§39.8]]. *Source: not from class (used for $S_4$, $A_4$ throughout).*

^nd-prop-39-8

- [ ] Q1 **[state]** State the proposition.
- [ ] Q2 Why does each non-identity element of $K$ square to $e$?
- [ ] Q3 Compute $(1\,2)(3\,4) \cdot (1\,3)(2\,4)$. Why is the product of two distinct non-identity elements the third?
- [ ] Q4 Write the isomorphism to $\mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/2\mathbb{Z}$.
- [ ] Q5 **[why]** Why is $K$ not cyclic, and why does this distinguish it from $\mathbb{Z}/4\mathbb{Z}$?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G10.
> - Disjoint transpositions commute; every element is its own inverse.

#### Normal subgroups of $S_3$ and $S_4$ · P2

The normal subgroups of $S_3$ are $\{e\}, A_3, S_3$; those of $S_4$ are $\{e\}, K, A_4, S_4$, see Example [[§39 Sources of Normal Subgroups#^ex-39-3|§39.3]]. *Source: notes (class sizes from WS 3).*

^nd-ex-39-3

- [ ] Q1 **[state]** List the normal subgroups of $S_3$ and of $S_4$.
- [ ] Q2 For $S_3$: which unions of classes ($1, 3, 2$) containing $e$ have order dividing $6$?
- [ ] Q3 For $S_4$: which unions of classes ($1, 6, 3, 8, 6$) containing $e$ have order dividing $24$? Which classes make up $K$ and $A_4$?
- [ ] Q4 Why is each candidate actually a subgroup?
- [ ] Q5 **[why]** Why is "union of classes with order dividing $|G|$" only a necessary condition? Why is $\{e, (1\,2)(3\,4)\}$ not normal in $S_4$?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G13.
> - Proposition [[§39 Sources of Normal Subgroups#^prop-39-7|§39.7]] and Lagrange; $1 + 3 = 4$, $1 + 3 + 8 = 12$.
> - $\{e, (1\,2)(3\,4)\}$: [[Group Theory HW Drill#^ps6-1|PS6.1]], Example [[§39 Sources of Normal Subgroups#^ex-39-4|§39.4]].

#### Normal subgroups of $GL_2(\mathbb{R})$ · P2

Diagonal and upper triangular invertible matrices are not normal; $SL_2(\mathbb{R})$ and $\{\pm I_2\}$ are normal, see Proposition [[§39 Sources of Normal Subgroups#^prop-39-9|§39.9]]. *Source: WS 6.3. Proof pending in the notes.*

^nd-prop-39-9

- [ ] Q1 **[state]** State the four claims.
- [ ] Q2 **[why]** Why are $SL_2(\mathbb{R})$ and $\{\pm I_2\}$ normal (kernel; central)?
- [ ] Q3 Conjugate $\operatorname{diag}(1, 2)$ by $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$: is the result diagonal?
- [ ] Q4 Conjugate an upper triangular matrix by $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$: is the result upper triangular?
- [ ] Q5 **[use]** Where do $SL_2(\mathbb{R})$ and the scalars reappear (Second Isomorphism Theorem, $PSL_2$)?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G10 and G5.
> - Proof pending; the computations in Q3–Q4 are one natural route.
> - Example [[§45 S₃, S₄, A₄ and A₅#^ex-45-3|§45.3]].

#### $G/N$ is a group · P2

For $N \trianglelefteq G$, coset multiplication makes $G/N$ a group with identity $N$, inverses $g^{-1}N$, and $|G/N| = |G|/|N|$, see Theorem [[§40 Quotient Groups#^thm-40-1|§40.1]]. *Source: lecture 9/25 ("You should then check the two axioms").* **[class exercise, 9/25]**

^nd-thm-40-1

- [ ] Q1 **[state]** State the theorem.
- [ ] Q2 Which proposition makes the operation well defined?
- [ ] Q3 Check associativity, identity and inverses by computing with representatives.
- [ ] Q4 Why is $|G/N| = |G|/|N|$?
- [ ] Q5 **[why]** Which step fails if $N$ is only a subgroup? Why is checking the axioms "almost obvious" while well-definedness is the real issue?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G2.
> - Proposition [[§37 Multiplying Cosets#^prop-37-1|§37.1]]; each axiom reduces to the axiom in $G$.
> - Count: Lagrange (Theorem [[§29 The Index and Lagrange's Theorem#^thm-29-2|§29.2]]).

#### Every normal subgroup is a kernel · P2

For $N \trianglelefteq G$, $\pi : G \to G/N$ is a surjective homomorphism with $\operatorname{Ker}\pi = N$, see Proposition [[§40 Quotient Groups#^prop-40-2|§40.2]]. *Source: lecture 9/25.*

^nd-prop-40-2

- [ ] Q1 **[state]** State the proposition.
- [ ] Q2 Why is $\pi$ a homomorphism, and why surjective?
- [ ] Q3 Compute $\operatorname{Ker}\pi$. Which coset criterion?
- [ ] Q4 **[why]** Combine with "kernels are normal": what is the dictionary between normal subgroups and homomorphisms out of $G$?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G5.
> - $\pi(g) = N \iff gN = N \iff g \in N$.
> - Remark [[§40 Quotient Groups#^rem-40-2|§40]].

#### Multiplying through representatives · P2

If $S$ is a set of representatives and $s_1s_2 = s_3n$ ($s_3 \in S$, $n \in N$, unique), then $(s_1N)(s_2N) = s_3N$, see Proposition [[§40 Quotient Groups#^prop-40-3|§40.3]]. *Source: lecture 10/2.*

^nd-prop-40-3

- [ ] Q1 **[state]** State the proposition.
- [ ] Q2 Why do $s_3$ and $n$ exist and why are they unique?
- [ ] Q3 Conclude $(s_1N)(s_2N) = s_3N$.
- [ ] Q4 Write the tables of $(\mathbb{Z}/4\mathbb{Z})/\{0, 2\}$ with $S = \{0, 1\}$ and of $S_3/A_3$ with $S = \{e, (2\,3)\}$.
- [ ] Q5 **[why]** Why does a product leave $S$ in the first example but not in the second?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G2.
> - $n := s_3^{-1}s_1s_2 \in N$.
> - Examples [[§40 Quotient Groups#^ex-40-2|§40.2]], [[§40 Quotient Groups#^ex-40-3|§40.3]]: $S$ is a subgroup only in the second.

#### Representatives forming a subgroup · P2

If a set of representatives $S$ for $G/N$ is a subgroup, then $S \cap N = \{e\}$ and $s \mapsto sN$ is an isomorphism $S \cong G/N$, see Proposition [[§40 Quotient Groups#^prop-40-4|§40.4]] and Corollary [[§41 The First and Second Isomorphism Theorems#^cor-41-7|§41.7]]. *Source: lecture 10/2.*

^nd-prop-40-4

- [ ] Q1 **[state]** State the proposition.
- [ ] Q2 Why is $S \to G/N$ a homomorphism, and why a bijection?
- [ ] Q3 Why is $S \cap N = \{e\}$?
- [ ] Q4 Second proof via the Second Isomorphism Theorem: what are $SN$ and $S \cap N$?
- [ ] Q5 **[why]** Give the two examples: $S_3/A_3 \cong \langle (2\,3) \rangle$, and $(\mathbb{Z}/4\mathbb{Z})/\{0, 2\}$ where no subgroup works.

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G9.
> - Restriction of $\pi$; fibres of $\pi$ are cosets.
> - $SN = G$, $S \cap N = \{e\}$, so $S \cong SN/N = G/N$.

#### First Isomorphism Theorem · P2

For $\alpha : G \to H$ with $N = \operatorname{Ker}\alpha$, $I = \operatorname{Im}\alpha$, the map $\beta(gN) = \alpha(g)$ is a well-defined isomorphism $G/N \to I$, see Theorem [[§41 The First and Second Isomorphism Theorems#^thm-41-1|§41.1]]. *Source: lecture 9/25.*

^nd-thm-41-1

- [ ] Q1 **[state]** State the First Isomorphism Theorem.
- [ ] Q2 Well defined: if $gN = g'N$, show $\alpha(g) = \alpha(g')$.
- [ ] Q3 Injective: from $\alpha(g) = \alpha(g')$, deduce $gN = g'N$.
- [ ] Q4 Surjective and homomorphism.
- [ ] Q5 Apply it: $S_n/A_n$, $GL_n(k)/SL_n(k)$, $(\mathbb{Z}/6\mathbb{Z})/\{0, 3\}$, $G/Z(G)$.
- [ ] Q6 **[why]** Why are "images of $G$" the same as "quotients of $G$"? Why is the image not normal in $H$ in general?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G5 and G2.
> - $g = g'n \Rightarrow \alpha(g) = \alpha(g')$; $h = g^{-1}g' \in N$.
> - Examples [[§41 The First and Second Isomorphism Theorems#^ex-41-1|§41.1]]; remark [[§41 The First and Second Isomorphism Theorems#^rem-41-1|§41]].

#### $|G| = |\operatorname{Ker}\alpha| \cdot |\operatorname{Im}\alpha|$ · P2

For finite $G$ and a homomorphism $\alpha$, $|G| = |\operatorname{Ker}\alpha| \cdot |\operatorname{Im}\alpha|$, see Corollary [[§41 The First and Second Isomorphism Theorems#^cor-41-2|§41.2]]. *Source: lecture 9/25.*

^nd-cor-41-2

- [ ] Q1 **[state]** State the corollary.
- [ ] Q2 Prove it from the First Isomorphism Theorem.
- [ ] Q3 Use it to find $|\operatorname{Ker}|$ for the pair-partition map $S_4 \to S_3$.
- [ ] Q4 **[why]** Explain the analogy with rank–nullity over $\mathbb{F}_p$: why a product here and a sum there?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G5 with G3.
> - $|\operatorname{Im}\alpha| = |G/\operatorname{Ker}\alpha|$; $24/6 = 4$.
> - Remark [[§41 The First and Second Isomorphism Theorems#^rem-41-2|§41]].

#### Restricting a homomorphism · P2

The restriction $f|_{X'}$ of a homomorphism to a subgroup is a homomorphism with kernel $\operatorname{Ker}f \cap X'$, see Lemma [[§41 The First and Second Isomorphism Theorems#^lem-41-4|§41.4]]. *Source: lecture 10/5.*

^nd-lem-41-4

- [ ] Q1 **[state]** State the lemma.
- [ ] Q2 Why does the restriction preserve products?
- [ ] Q3 Compute the kernel.
- [ ] Q4 **[why]** Where is it used: the two kernels in the Second Isomorphism Theorem, and $\operatorname{Ker}(\alpha|_{A_4}) = K$?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G5.
> - Remark [[§41 The First and Second Isomorphism Theorems#^rem-41-4|§41]]; Proposition [[§43 Simple Groups#^prop-43-10|§43.10]].

#### Second Isomorphism Theorem · P2

For $N \trianglelefteq G$, $H \leq G$: $H \cap N \trianglelefteq H$, $N \trianglelefteq HN$, $\pi(H) = \pi(HN)$ and $H/(H \cap N) \cong HN/N$, see Theorem [[§41 The First and Second Isomorphism Theorems#^thm-41-5|§41.5]]. *Source: lecture 10/2, 10/5; WS 8.2.*

^nd-thm-41-5

- [ ] Q1 **[state]** State the Second Isomorphism Theorem and draw the diamond.
- [ ] Q2 Show $\pi(H) = \pi(HN)$.
- [ ] Q3 Restrict $\pi$ to $H$: kernel? Conclusion?
- [ ] Q4 Restrict $\pi$ to $HN$: kernel? Conclusion?
- [ ] Q5 Apply it: $S_3$ with $N = A_3$, $H = \langle (1\,2) \rangle$; $S_4$ with $N = K$, $H = \operatorname{Stab}(4)$; $GL_2^+(\mathbb{R})$ with $SL_2(\mathbb{R})$ and the scalars.
- [ ] Q6 **[why]** Why is $HN$ needed (and not $H$) on the right? What is the linear algebra shadow?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G5 twice, G9.
> - $\pi(hn) = \pi(h)$ since $n \in \operatorname{Ker}\pi$; kernels $H \cap N$ and $HN \cap N = N$ (Lemma [[§41 The First and Second Isomorphism Theorems#^lem-41-4|§41.4]]).
> - Examples [[§45 S₃, S₄, A₄ and A₅#^ex-45-1|§45.1]], [[§45 S₃, S₄, A₄ and A₅#^ex-45-3|§45.3]]; remark [[§41 The First and Second Isomorphism Theorems#^rem-41-5|§41]].

#### The order of $SN$ · P2

For $N \trianglelefteq G$, $S \leq G$ finite, $|SN| = |S||N|/|S \cap N|$, see Corollary [[§41 The First and Second Isomorphism Theorems#^cor-41-6|§41.6]]. *Source: WS 8.3. Proof pending in the notes.*

^nd-cor-41-6

- [ ] Q1 **[state]** State the corollary.
- [ ] Q2 **[why]** Which isomorphism and which application of Lagrange give it in two lines?
- [ ] Q3 **[use]** Where is the general version (no normality needed for the count) used in the Sylow chapter?
- [ ] Q4 **[why]** What is the analogue for subspaces, $\dim(L_1 + L_2)$?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G3 with G5.
> - $|SN|/|N| = |SN/N| = |S/(S \cap N)| = |S|/|S \cap N|$.
> - Lemma [[§52 The Sylow Theorems#^lem-52-8|§52.8]] is the counting version for any two subgroups; remark [[§41 The First and Second Isomorphism Theorems#^rem-41-5|§41]].

#### Images of subgroups containing $N$ · P2

For $N \subseteq A \leq G$, $\pi(A) = A/N$ is a subgroup of $G/N$, normal iff $A \trianglelefteq G$, see Proposition [[§42 The Correspondence and Third Isomorphism Theorems#^prop-42-1|§42.1]]. *Source: WS 8.4; lecture 10/5.*

^nd-prop-42-1

- [ ] Q1 **[state]** State both parts.
- [ ] Q2 Why is $\pi(A)$ a subgroup?
- [ ] Q3 ($\Leftarrow$) Compute $(gN)\pi(a)(gN)^{-1}$.
- [ ] Q4 ($\Rightarrow$) From $\pi(gag^{-1}) \in \pi(A)$, write $gag^{-1} = a'n$. Why does this lie in $A$?
- [ ] Q5 **[why]** Where is $N \subseteq A$ needed? Give a counterexample without it ($N = A_3$, $A = \langle (1\,2) \rangle$ in $S_3$).

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G9.
> - $\pi(A) = \operatorname{Im}(\pi|_A)$; $\pi(g)\pi(a)\pi(g)^{-1} = \pi(gag^{-1})$.
> - Only in ($\Rightarrow$): $a'n \in A$ because $N \subseteq A$. For the counterexample, $\pi(\langle (1\,2) \rangle) = S_3/A_3$ is normal.

#### Preimages of subgroups of $G/N$ · P2

For $B \leq G/N$, $\pi^{-1}(B)$ is a subgroup containing $N$; it is normal iff $B$ is, see Proposition [[§42 The Correspondence and Third Isomorphism Theorems#^prop-42-2|§42.2]]. *Source: WS 8.5; (1) lecture 10/5; (2) to be filled (not done in class).*

^nd-prop-42-2

- [ ] Q1 **[state]** State both parts.
- [ ] Q2 (1) Why does $\pi^{-1}(B)$ contain $N$ (hence $e$)?
- [ ] Q3 (1) Check closure under products and inverses.
- [ ] Q4 (2) **[why]** (pending) Which earlier result gives "$B$ normal $\Rightarrow$ $\pi^{-1}(B)$ normal" at once, and which gives the converse via $\pi(\pi^{-1}(B)) = B$?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G1 and G9.
> - $\pi(n) = e \in B$; $\pi(g_1g_2) = \pi(g_1)\pi(g_2)$.
> - (2): preimages of normal subgroups are normal (Proposition [[§39 Sources of Normal Subgroups#^prop-39-4|§39.4]](1)); conversely Proposition [[§42 The Correspondence and Third Isomorphism Theorems#^prop-42-1|§42.1]] with $A = \pi^{-1}(B)$.

#### The Correspondence Theorem · P2

$A \mapsto \pi(A)$ and $B \mapsto \pi^{-1}(B)$ are mutually inverse bijections between subgroups of $G$ containing $N$ and subgroups of $G/N$, preserving normality, see Theorem [[§42 The Correspondence and Third Isomorphism Theorems#^thm-42-3|§42.3]]. *Source: WS 8 ("third/fourth isomorphism theorem"). Proof pending in the notes.*

^nd-thm-42-3

- [ ] Q1 **[state]** State the Correspondence Theorem.
- [ ] Q2 **[why]** What has to be checked: $\pi(\pi^{-1}(B)) = B$ (which property of $\pi$?) and $\pi^{-1}(\pi(A)) = A$ (where is $N \subseteq A$ used)?
- [ ] Q3 **[use]** List the six subgroups of $S_4$ containing $K$ via $S_4/K \cong S_3$. Which are normal?
- [ ] Q4 **[why]** Why does the theorem fail for subgroups not containing $N$?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G9.
> - Pieces: Propositions [[§42 The Correspondence and Third Isomorphism Theorems#^prop-42-1|§42.1]] and [[§42 The Correspondence and Third Isomorphism Theorems#^prop-42-2|§42.2]]; $\pi^{-1}(\pi(A)) = AN = A$.
> - Example [[§45 S₃, S₄, A₄ and A₅#^ex-45-2|§45.2]]: $K$, $A_4$, $S_4$, three of order $8$.

#### Quotients along the correspondence; Third Isomorphism Theorem · P2

For $N \subseteq A_1 \subseteq A_2$: $A_2/A_1 \leftrightarrow B_2/B_1$, $A_1 \trianglelefteq A_2 \iff B_1 \trianglelefteq B_2$, and then $A_2/A_1 \cong B_2/B_1$; in particular $(G/N)/(K/N) \cong G/K$ for $N \subseteq K$ normal, see Proposition [[§42 The Correspondence and Third Isomorphism Theorems#^prop-42-4|§42.4]] and Theorem [[§42 The Correspondence and Third Isomorphism Theorems#^thm-42-5|§42.5]]. *Source: WS 8.6; third theorem named in lecture 10/2, not covered. Proofs pending in the notes.*

^nd-prop-42-4

- [ ] Q1 **[state]** State WS 8.6 and the Third Isomorphism Theorem.
- [ ] Q2 **[why]** For the Third Isomorphism Theorem, which surjective homomorphism $G/N \to G/K$ do you write down, and what is its kernel?
- [ ] Q3 Why is $gN \mapsto gK$ well defined?
- [ ] Q4 **[use]** Which special case of WS 8.6 is the Third Isomorphism Theorem?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G5 and G2.
> - $gN \mapsto gK$ is well defined as $N \subseteq K$; its kernel is $K/N$; First Isomorphism Theorem.
> - Remark [[§42 The Correspondence and Third Isomorphism Theorems#^rem-42-3|§42]]: $A_1 = K$, $A_2 = G$.

#### Homomorphisms out of and into a simple group · P2

A homomorphism out of a simple group is injective or trivial (WS 7.1); into a simple group it need not be surjective or trivial, e.g. $\mathbb{Z}/3\mathbb{Z} \to A_5$ (WS 7.2); but if the image is normal it is surjective or trivial, see Proposition [[§43 Simple Groups#^prop-43-3|§43.3]], Proposition [[§43 Simple Groups#^prop-43-4|§43.4]] and Corollary [[§43 Simple Groups#^cor-43-5|§43.5]]. *Source: WS 7.1, 7.2; lecture 9/28.*

^nd-prop-43-3

- [ ] Q1 **[state]** State WS 7.1, WS 7.2 and the corollary.
- [ ] Q2 Prove WS 7.1 from the kernel.
- [ ] Q3 For WS 7.2, why is $[k] \mapsto (1\,2\,3)^k$ a well-defined homomorphism into $A_5$, and why is it neither trivial nor surjective?
- [ ] Q4 Prove the corollary.
- [ ] Q5 **[why]** Why does WS 7.1 not dualize?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G5 and G13.
> - Kernel is normal, so $\{e\}$ or $G$; $(1\,2\,3)$ has order $3$ and is even.
> - Remark [[§43 Simple Groups#^rem-43-4|§43]]: images need not be normal.

#### $A_5$ is simple · P2

With class sizes $1, 20, 15, 12, 12$, $A_5$ is simple, see Proposition [[§43 Simple Groups#^prop-43-6|§43.6]]. *Source: WS 7.4; class 9/30.*

^nd-prop-43-6

- [ ] Q1 **[state]** State the class sizes of $A_5$ and the conclusion.
- [ ] Q2 Why is a normal subgroup $N$ a union of conjugacy classes containing $\{e\}$?
- [ ] Q3 List the possible values $1 + s$.
- [ ] Q4 Compare with the divisors of $60$. Conclude.
- [ ] Q5 **[why]** Why do the $5$-cycles split into two classes of $12$ in $A_5$ (while the $3$-cycles do not)?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G13.
> - Proposition [[§39 Sources of Normal Subgroups#^prop-39-7|§39.7]] and Lagrange; only $1$ and $60$ survive.
> - Splitting: Example [[§44 Conjugacy in a Normal Subgroup#^ex-44-1|§44.1]], [[Group Theory HW Drill#^ps5-2|PS5.2]] (Proposition [[§44 Conjugacy in a Normal Subgroup#^prop-44-2|§44.2]]).

#### 3-cycles are conjugate in $A_n$ for $n \geq 5$ · P2

For $n \geq 5$ any two $3$-cycles are conjugate by an element of $A_n$, see Lemma [[§43 Simple Groups#^lem-43-8|§43.8]]. *Source: lecture 9/30 ("detail to check").* **[class exercise, 9/30]**

^nd-lem-43-8

- [ ] Q1 **[state]** State the lemma.
- [ ] Q2 Choose $g \in S_n$ with $g(i\,j\,k)g^{-1} = (i'\,j'\,k')$. How?
- [ ] Q3 If $g$ is odd, which even $g'$ works instead? Why does it still conjugate correctly?
- [ ] Q4 Where is $n \geq 5$ used?
- [ ] Q5 **[why]** Show it fails for $n = 4$: $(1\,2\,3)$ and $(1\,3\,2)$ are not conjugate in $A_4$.

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G6.
> - Replace $g$ by $g(x\,y)$ with $x, y \notin \{i, j, k\}$; $(x\,y)$ commutes with $(i\,j\,k)$.
> - $n = 4$: Example [[§43 Simple Groups#^ex-43-1|§43.1]].

#### $A_n$ is simple for $n \geq 5$ · P2

For $n \geq 5$ and $\{e\} \neq N \trianglelefteq A_n$: pick $g \in N \setminus \{e\}$ and a $3$-cycle not commuting with it; the commutator $h = g(i\,j\,k)g^{-1}(i\,j\,k)^{-1} \in N$ has type $3$, $2+2$, $5$ or $3+3$; each case yields a $3$-cycle in $N$, so $N = A_n$, see Theorem [[§43 Simple Groups#^thm-43-9|§43.9]]. *Source: WS 7.5; lecture 9/28, 9/30 (the $5$-cycle and $3+3$ cases were "left to check", handout).* **[class exercise, 9/30]**

^nd-thm-43-9

- [ ] Q1 **[state]** State the theorem and the strategy (first goal, second goal, big goal).
- [ ] Q2 Step 1: given $g \neq e$, choose $i, j, k$ so that $(i\,j\,k)$ does not commute with $g$.
- [ ] Q3 Step 2: why is $h \in N$ and $h \neq e$?
- [ ] Q4 Step 3: why does $h$ move at most $6$ points, and why are the only possible types $3$, $2+2$, $5$, $3+3$?
- [ ] Q5 Step 4: in each case, conjugate $h$ by a $3$-cycle $t$ and form $hh'^{-1}$. Do the $2+2$ case ($t = (c\,d\,x)$) and the $5$-cycle case ($t = (a\,b\,c)$).
- [ ] Q6 Step 5: why does one $3$-cycle in $N$ give all of $A_n$?
- [ ] Q7 **[why]** Where is $n \geq 5$ used (twice), and why must it be, given $A_4$?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G13 and G7 (generators: $3$-cycles generate $A_n$).
> - Step 1: $j, k \notin \{i, g(i)\}$; step 2: $h = g \cdot [(i\,j\,k)g^{-1}(i\,j\,k)^{-1}]$, the bracket a conjugate of $g^{-1}$.
> - Step 4: $(a\,b)(c\,d)(a\,b)(d\,x) = (c\,d\,x)$; $5$-cycle gives $(a\,d\,b)$; $3+3$ gives a $5$-cycle (or directly $(f\,e\,d)$, remark [[§43 Simple Groups#^rem-43-5|§43]]).
> - Step 5: Lemma [[§43 Simple Groups#^lem-43-8|§43.8]]; remark [[§43 Simple Groups#^rem-43-7|§43]].

#### The pair-partition homomorphism $S_4 \to S_3$ · P2

$S_4$ acting on the three pair-partitions of $\{1, 2, 3, 4\}$ gives a surjection $\alpha : S_4 \to S_3$ with kernel $K$; so $S_4/K \cong S_3$ and $A_4/K \cong \mathbb{Z}/3\mathbb{Z}$, see Proposition [[§43 Simple Groups#^prop-43-10|§43.10]]. *Source: lecture 9/30 ("you can check all the transpositions").* **[class exercise, 9/30]**

^nd-prop-43-10

- [ ] Q1 **[state]** State the proposition.
- [ ] Q2 Why is this an action, giving $\alpha$?
- [ ] Q3 Surjective: what does a transposition $(a\,b)$ do to the three pair-partitions?
- [ ] Q4 Kernel: why $|\operatorname{Ker}\alpha| = 4$, and why does $K \subseteq \operatorname{Ker}\alpha$?
- [ ] Q5 Why is $A_4/K \cong A_3$?
- [ ] Q6 **[why]** Give the second route to $S_4/K \cong S_3$ via the Second Isomorphism Theorem with $H = \operatorname{Stab}(4)$.

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G11 and G5.
> - $(3\,4)$ fixes $\{\{1,2\},\{3,4\}\}$ and swaps the other two; transpositions generate $S_3$.
> - $24/6 = 4$; restrict to $A_4$ (Lemma [[§41 The First and Second Isomorphism Theorems#^lem-41-4|§41.4]]); $12/4 = 3$.
> - Example [[§45 S₃, S₄, A₄ and A₅#^ex-45-1|§45.1]](2).

#### In $A_4$, $(1\,2\,3)$ and $(1\,3\,2)$ are not conjugate · P2

$\alpha|_{A_4} : A_4 \to A_3$ is a character separating $(1\,2\,3)$ and $(1\,3\,2)$, see Example [[§43 Simple Groups#^ex-43-1|§43.1]]. *Source: lecture 9/30 ("You can check they're not conjugate").* **[class exercise, 9/30]**

^nd-ex-43-1

- [ ] Q1 **[state]** State the claim.
- [ ] Q2 Why is $\alpha|_{A_4}$ a character, and why are characters constant on conjugacy classes?
- [ ] Q3 Why is $\alpha((1\,2\,3)) \neq \alpha((1\,3\,2))$?
- [ ] Q4 **[why]** Give a second proof by counting: what is $|C_{A_4}((1\,2\,3))|$ and hence the $A_4$-class size?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G8 (characters).
> - Proposition [[§46 Characters#^prop-46-1|§46.1]]; in a group of order $3$ no non-identity element is its own inverse.
> - Counting: $C_{A_4}((1\,2\,3)) = \langle (1\,2\,3) \rangle$, so the class has $12/3 = 4$ elements, not all $8$ three-cycles.

#### The field $\mathbb{F}_9$; classification of finite fields · P2

$\mathbb{F}_9 = \{a + bi : a, b \in \mathbb{F}_3\}$, $i^2 = -1$, is a field with $9$ elements, unlike $\mathbb{Z}/9\mathbb{Z}$; every finite field has $p^m$ elements and there is exactly one of each prime-power order, see Example [[§43 Simple Groups#^ex-43-2|§43.2]] and Theorem [[§43 Simple Groups#^thm-43-12|§43.12]]. *Source: lecture 9/30 (classification stated for culture, not proved).*

^nd-ex-43-2

- [ ] Q1 **[state]** State the classification of finite fields.
- [ ] Q2 Why is $a^2 + b^2 \neq 0$ in $\mathbb{F}_3$ unless $a = b = 0$? Write $(a + bi)^{-1}$.
- [ ] Q3 Why is $\mathbb{Z}/9\mathbb{Z}$ not a field?
- [ ] Q4 **[why]** Why does this appear in a group theory course (the family $PSL_n(\mathbb{F}_q)$)?

> [!tip]- Hints: route of the proof in the notes
> - Squares in $\mathbb{F}_3$ are $0, 1, 1$; $(a - bi)/(a^2 + b^2)$; $[3][3] = [0]$.
> - Remark [[§43 Simple Groups#^rem-43-8|§43]].

#### $PSL_n(F)$ is simple · P2

$PSL_n(F)$ is simple for $n \geq 2$ except $PSL_2(\mathbb{F}_2) \cong S_3$ and $PSL_2(\mathbb{F}_3) \cong A_4$, see Theorem [[§43 Simple Groups#^thm-43-13|§43.13]] and Example [[§43 Simple Groups#^ex-43-3|§43.3]]. *Source: WS 7; lecture 9/28. Proof pending (too long for a worksheet).*

^nd-thm-43-13

- [ ] Q1 **[state]** State the theorem with its exceptions.
- [ ] Q2 **[why]** Why are the two exceptions not simple?
- [ ] Q3 **[use]** Name the three families of simple groups met in the course.
- [ ] Q4 **[why]** What is the analogue for $PSL_n$ of step 1 in the $A_n$ proof (centralizer viewpoint)?

> [!tip]- Hints: route of the proof in the notes
> - $A_3 \trianglelefteq S_3$, $K \trianglelefteq A_4$.
> - $\mathbb{Z}/p\mathbb{Z}$, $A_n$ ($n \geq 5$), $PSL_n(F)$ (remark [[§43 Simple Groups#^rem-43-9|§43]]); centralizer view in remark [[§43 Simple Groups#^rem-43-5|§43]].

#### $GL_2^+(\mathbb{R})$, $SL_2(\mathbb{R})$ and the scalars · P2

With $N = SL_2(\mathbb{R})$ and $Z$ the scalars in $GL_2(\mathbb{R})$: $N \cap Z = \{\pm I_2\}$, $NZ = GL_2^+(\mathbb{R})$, so $GL_2^+(\mathbb{R})/Z \cong PSL_2(\mathbb{R})$ and $GL_2^+(\mathbb{R})/SL_2(\mathbb{R}) \cong \mathbb{R}_{>0}$, see Example [[§45 S₃, S₄, A₄ and A₅#^ex-45-3|§45.3]]. *Source: lecture 10/5.*

^nd-ex-45-3

- [ ] Q1 **[state]** State the two isomorphisms.
- [ ] Q2 Why are $SL_2(\mathbb{R})$ and $Z$ normal in $GL_2(\mathbb{R})$?
- [ ] Q3 Compute $SL_2(\mathbb{R}) \cap Z$.
- [ ] Q4 Show $SL_2(\mathbb{R})Z = GL_2^+(\mathbb{R})$ (both inclusions).
- [ ] Q5 Apply the Second Isomorphism Theorem twice, with each subgroup in the normal role.
- [ ] Q6 **[why]** Why is $Z/\{\pm I_2\} \cong \mathbb{R}_{>0}$? Why does the product land only in $\det > 0$?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G9 and G10.
> - $\det(zI_2) = z^2$; $g = (\sqrt{d}\,I_2)(g/\sqrt{d})$.
> - $zI_2 \mapsto z^2$ has kernel $\{\pm I_2\}$.

### Priority 4 · notes only (Pinter, MATH 412, not from class)

#### A normal subgroup inside a subgroup of finite index · P4

Theorem [[§39 Sources of Normal Subgroups#^thm-39-5|§39.5]] (with the normal core, Proposition [[§39 Sources of Normal Subgroups#^prop-39-6|§39.6]]) → drilled as [[493 Problem Set 3#^hw-3-2|PS3.2]] and [[493 Problem Set 4#^hw-4-3|PS4.3]].

#### Normal subgroups are unions of conjugacy classes · P4

$H \leq G$ is normal iff it is a union of conjugacy classes, see Proposition [[§39 Sources of Normal Subgroups#^prop-39-7|§39.7]]. *Source: cf. Pinter Ch. 14 (used for $A_5$ simple, normal subgroups of $S_4$).*

^nd-prop-39-7

- [ ] Q1 **[state]** State the proposition.
- [ ] Q2 Rewrite "$ghg^{-1} \in H$ for all $g, h$" in terms of $\operatorname{Conj}(h)$.
- [ ] Q3 Why is a subset containing the full orbit of each of its points a union of orbits?
- [ ] Q4 **[why]** Turn this into a test: which three constraints on $|N|$ (sum of class sizes, contains the class $\{e\}$, divides $|G|$) do you use?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G13.
> - Conjugacy classes are orbits of conjugation (Proposition [[§34 Conjugation as an Action and the Class Equation#^prop-34-1|§34.1]]).

#### Normality is not transitive · P4

Example [[§39 Sources of Normal Subgroups#^ex-39-4|§39.4]] → drilled as [[493 Problem Set 6#^hw-6-1|PS6.1]].

#### $HN$ is a subgroup when $N$ is normal · P4

Lemma [[§41 The First and Second Isomorphism Theorems#^lem-41-3|§41.3]] and Example [[§41 The First and Second Isomorphism Theorems#^ex-41-2|§41.2]] → drilled as [[493 Problem Set 4#^hw-4-1|PS4.1]]. (Lecture 10/2: "This is going [to be] homework"; also WS 8.1.)

#### $S_n$ is not simple for $n \geq 3$ · P4

$A_n$ is a proper nontrivial normal subgroup of $S_n$ for $n \geq 3$, see Corollary [[§43 Simple Groups#^cor-43-2|§43.2]]. *Source: notes.*

^nd-cor-43-2

- [ ] Q1 **[state]** State the corollary.
- [ ] Q2 Why is $A_n$ normal?
- [ ] Q3 Why is it nontrivial for $n \geq 3$, and proper?
- [ ] Q4 **[why]** What about $S_2$? Is it simple?

> [!tip]- Hints: route of the proof in the notes
> - Index $2$; $(1\,2\,3) = (1\,3)(1\,2)$ is even; $(1\,2)$ is odd.
> - $S_2 \cong \mathbb{Z}/2\mathbb{Z}$ is simple.

#### Which $A_n$ are simple · P4

$A_n$ is simple iff $n = 3$ or $n \geq 5$, see Corollary [[§43 Simple Groups#^cor-43-11|§43.11]]. *Source: notes.*

^nd-cor-43-11

- [ ] Q1 **[state]** State the corollary.
- [ ] Q2 Treat $n = 1, 2$; $n = 3$; $n = 4$; $n \geq 5$, citing the result used in each case.
- [ ] Q3 **[why]** Why is $A_3$ simple but not "interesting"? Which is the smallest non-abelian simple group?

> [!tip]- Hints: route of the proof in the notes
> - Trivial groups are not simple; $A_3$ has prime order; $K \trianglelefteq A_4$; Theorem [[§43 Simple Groups#^thm-43-9|§43.9]].
> - Theorem [[§43 Simple Groups#^thm-43-7|§43.7]] (not from class): order $60$.

#### Conjugacy in a normal subgroup · P4

Proposition [[§44 Conjugacy in a Normal Subgroup#^prop-44-1|§44.1]], Proposition [[§44 Conjugacy in a Normal Subgroup#^prop-44-2|§44.2]] and Example [[§44 Conjugacy in a Normal Subgroup#^ex-44-2|§44.2]] → drilled as [[493 Problem Set 5#^hw-5-2|PS5.2]].

# T9. Characters, commutators, solvable groups

## Definitions T9

### Priority 1 · problem sets (directly or extended)

#### Character · P1

A homomorphism $\chi : G \to A$ into an abelian group $A$ (most often $A = k^\times$), see Definition [[§46 Characters#^def-46-1|§46.1]]. *Source: lecture 9/23 ("for now"); PS 2.*

^nd-def-46-1

- [ ] Q1 **[def]** Define a character. Which hypothesis on the target is essential?
- [ ] Q2 **[example]** Give four: $\operatorname{sgn}$, $\det$, the trivial character, $\mathbb{Z}/4\mathbb{Z} \to U_5$, $k \mapsto 2^k$; and the restriction of the pair-partition map to $A_4 \to A_3$.
- [ ] Q3 **[use]** What are the two basic constraints (conjugacy classes; commutators)?
- [ ] Q4 **[why]** Why is the identity $S_3 \to S_3$ not a character, and how does it violate the constraints? What will "character" mean later in the course?

> [!tip]- Hints: where it lives, examples
> - Examples [[§46 Characters#^ex-46-1|§46.1]]; Proposition [[§46 Characters#^prop-46-1|§46.1]], Proposition [[§47 Commutators#^prop-47-1|§47.1]].
> - Remarks [[§46 Characters#^rem-46-3|§46]] (non-abelian target), [[§46 Characters#^rem-46-2|§46]] (trace of a representation).

#### Commutator · P1

$h = g_1g_2g_1^{-1}g_2^{-1}$ for some $g_1, g_2 \in G$, see Definition [[§47 Commutators#^def-47-1|§47.1]]. *Source: [[Group Theory HW Drill#^ps2-4|PS2.4]].*

^nd-def-47-1

- [ ] Q1 **[def]** Define a commutator. Why is $e$ always one?
- [ ] Q2 **[example]** Write $(i\,j\,k)$ as a commutator in $S_n$; why is $(i\,j)$ not one?
- [ ] Q3 **[use]** Why is the inverse of a commutator a commutator, and the conjugate of a commutator a commutator?
- [ ] Q4 **[why]** Why is $G$ abelian iff $e$ is the only commutator? Is a product of commutators always a commutator?

> [!tip]- Hints: where it lives, examples
> - [[Group Theory HW Drill#^ps2-4|PS2.4]]: Propositions [[§47 Commutators#^prop-47-2|§47.2]], [[§47 Commutators#^prop-47-3|§47.3]]; [[Group Theory HW Drill#^ps5-4|PS5.4]]: Example [[§47 Commutators#^ex-47-2|§47.2]].

#### Commutator subgroup · P1

$[G, G] = D(G)$ is the subgroup generated by all commutators, see Definition [[§47 Commutators#^def-47-2|§47.2]]. *Source: [[Group Theory HW Drill#^ps4-4|PS4.4]]; WS 9.*

^nd-def-47-2

- [ ] Q1 **[def]** Define $[G, G]$. Why "generated by"?
- [ ] Q2 **[example]** Compute $D(S_n)$ ($n \geq 2$), $D(A_4)$, $D(A_n)$ ($n \geq 5$), $D(\text{abelian})$.
- [ ] Q3 **[use]** Why is $D(G)$ normal, and contained in every kernel of a character?
- [ ] Q4 **[why]** Why is $D(G)$ the smallest normal subgroup with abelian quotient?

> [!tip]- Hints: where it lives, examples
> - Theorem [[§47 Commutators#^thm-47-5|§47.5]] ($D(S_n) = A_n$), Example [[§49 The Derived Series#^ex-49-1|§49.1]] ($D(A_4) = K$), Theorem [[§47 Commutators#^thm-47-10|§47.10]].
> - Proposition [[§47 Commutators#^prop-47-4|§47.4]], Proposition [[§47 Commutators#^prop-47-11|§47.11]].

#### Abelianization · P1

$G^{\mathrm{ab}} = G/[G, G]$, see Definition [[§47 Commutators#^def-47-3|§47.3]]. *Source: [[Group Theory HW Drill#^ps4-4|PS4.4]].*

^nd-def-47-3

- [ ] Q1 **[def]** Define $G^{\mathrm{ab}}$. What makes the quotient defined?
- [ ] Q2 **[example]** Compute $S_n^{\mathrm{ab}}$ for $n \geq 2$ and $A_5^{\mathrm{ab}}$.
- [ ] Q3 **[use]** Why is $G^{\mathrm{ab}}$ abelian, and why is it the largest abelian quotient?
- [ ] Q4 **[why]** How do characters of $G$ correspond to characters of $G^{\mathrm{ab}}$?

> [!tip]- Hints: where it lives, examples
> - Example [[§47 Commutators#^ex-47-1|§47.1]]: $S_n/A_n \cong \{\pm 1\}$; Proposition [[§47 Commutators#^prop-47-6|§47.6]] ([[Group Theory HW Drill#^ps4-4-2|PS4.4(2)]]).
> - Remark [[§47 Commutators#^rem-47-6|§47]].

### Priority 2 · worksheets and lectures

#### Solvable group · P2

$G$ is solvable if there is a chain $\{e\} = G_0 \trianglelefteq G_1 \trianglelefteq \cdots \trianglelefteq G_N = G$, each $G_{j-1}$ normal in $G_j$ with $G_j/G_{j-1}$ abelian, see Definition [[§48 Solvable Groups#^def-48-1|§48.1]]. *Source: WS 9.*

^nd-def-48-1

- [ ] Q1 **[def]** Define a solvable group.
- [ ] Q2 **[example]** Chains for an abelian group, $S_3$, $S_4$.
- [ ] Q3 **[use]** Is solvability inherited by subgroups and quotients? How is it tested mechanically?
- [ ] Q4 **[why]** Why must $G_{j-1}$ be normal only in $G_j$, not in $G$? Why are $A_n$, $S_n$ ($n \geq 5$) not solvable?

> [!tip]- Hints: where it lives, examples
> - Remark [[§48 Solvable Groups#^rem-48-1|§48]]; Proposition [[§48 Solvable Groups#^prop-48-1|§48.1]].
> - Propositions [[§48 Solvable Groups#^prop-48-2|§48.2]], [[§48 Solvable Groups#^prop-48-3|§48.3]]; Theorem [[§49 The Derived Series#^thm-49-1|§49.1]]; Corollary [[§49 The Derived Series#^cor-49-2|§49.2]].

#### Derived series · P2

$D_0(G) = G$, $D_{k+1}(G) = D(D_k(G))$: $G \trianglerighteq D(G) \trianglerighteq D(D(G)) \trianglerighteq \cdots$, see Definition [[§49 The Derived Series#^def-49-1|§49.1]]. *Source: WS 9.*

^nd-def-49-1

- [ ] Q1 **[def]** Define the derived series.
- [ ] Q2 **[example]** Derived series of $S_3$, $S_4$, $S_5$.
- [ ] Q3 **[use]** Why is each term normal in the previous one with abelian quotient?
- [ ] Q4 **[why]** Why does a finite group's series either reach $\{e\}$ or get stuck? What can happen for infinite groups?

> [!tip]- Hints: where it lives, examples
> - Example [[§49 The Derived Series#^ex-49-1|§49.1]]; remark [[§49 The Derived Series#^rem-49-2|§49]] ("crank").

## Proofs T9

### Priority 1 · problem sets (directly or extended)

#### Properties of the commutator subgroup · P1

$[G, G] \trianglelefteq G$; every character is trivial on $[G, G]$; $[G, G] = \{e\}$ iff $G$ abelian, see Proposition [[§47 Commutators#^prop-47-4|§47.4]]. *Source: (1) is [[Group Theory HW Drill#^ps4-4-1|PS4.4(1)]] and WS 9.4 (→ drilled as [[493 Problem Set 4#^hw-4-4|PS4.4]]); (2), (3) notes.*

^nd-prop-47-4

- [ ] Q1 **[state]** State the three parts.
- [ ] Q2 (2): why does $\operatorname{Ker}\chi$ contain $[G, G]$ once it contains every commutator?
- [ ] Q3 (3): prove both directions.
- [ ] Q4 **[why]** Use (2) to show $[S_n, S_n] \subseteq A_n$. Why is $\subseteq \operatorname{Ker}$ for one character not enough to compute $[G, G]$?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G8 (characters and commutators).
> - $\operatorname{Ker}\chi$ is a subgroup containing the generators.
> - Equality $[S_n, S_n] = A_n$ needs the $3$-cycles (Theorem [[§47 Commutators#^thm-47-5|§47.5]], [[Group Theory HW Drill#^ps4-5|PS4.5]]).

### Priority 2 · worksheets and lectures

#### Abelian quotients and commutators · P2

For $N \trianglelefteq H$: $H/N$ abelian $\iff$ every commutator of $H$ lies in $N$ $\iff$ $D(H) \subseteq N$, see Proposition [[§47 Commutators#^prop-47-11|§47.11]]. *Source: lecture 10/9.*

^nd-prop-47-11

- [ ] Q1 **[state]** State the three equivalent conditions.
- [ ] Q2 (1) $\Leftrightarrow$ (2): compute $(gN)(hN)(gN)^{-1}(hN)^{-1}$ in $H/N$.
- [ ] Q3 (2) $\Leftrightarrow$ (3): why does "contains all commutators" mean "contains $D(H)$"?
- [ ] Q4 **[why]** Deduce that $H^{\mathrm{ab}}$ is the largest abelian quotient. Where is this used in solvability proofs?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G8.
> - The commutator of cosets is the coset of the commutator; $D(H)$ is the smallest subgroup containing the commutators.
> - Used in Propositions [[§48 Solvable Groups#^prop-48-2|§48.2]], [[§48 Solvable Groups#^prop-48-3|§48.3]] and Theorem [[§49 The Derived Series#^thm-49-1|§49.1]]; remark [[§47 Commutators#^rem-47-6|§47]].

#### $S_3$ and $S_4$ are solvable · P2

The chains $\{e\} \trianglelefteq A_3 \trianglelefteq S_3$ and $\{e\} \trianglelefteq K \trianglelefteq A_4 \trianglelefteq S_4$ have abelian quotients, see Proposition [[§48 Solvable Groups#^prop-48-1|§48.1]]. *Source: WS 9.1.*

^nd-prop-48-1

- [ ] Q1 **[state]** State the proposition with the two chains.
- [ ] Q2 For $S_3$: why is $A_3 \trianglelefteq S_3$, and what are the two quotients?
- [ ] Q3 For $S_4$: why is $K \trianglelefteq A_4$ with $A_4/K \cong \mathbb{Z}/3\mathbb{Z}$?
- [ ] Q4 Why are $S_4/A_4$ and $K$ abelian?
- [ ] Q5 **[why]** Why can the chain for $S_4$ not be shortened to $\{e\} \trianglelefteq A_4 \trianglelefteq S_4$?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G9 and G10.
> - Index $2$ (Proposition [[§39 Sources of Normal Subgroups#^prop-39-1|§39.1]]); pair-partition map (Proposition [[§43 Simple Groups#^prop-43-10|§43.10]]); order $4$ is abelian (Proposition [[§34 Conjugation as an Action and the Class Equation#^prop-34-6|§34.6]]).
> - $A_4$ is not abelian.

#### Subgroups of solvable groups are solvable · P2

If $G$ is solvable with chain $(G_j)$ and $S \leq G$, then $(S \cap G_j)$ is a chain for $S$ with abelian quotients, see Proposition [[§48 Solvable Groups#^prop-48-2|§48.2]]. *Source: WS 9.2; lecture 10/7, 10/9.*

^nd-prop-48-2

- [ ] Q1 **[state]** State the proposition and the candidate chain.
- [ ] Q2 Normality: for $g \in S \cap G_{j-1}$, $h \in S \cap G_j$, why is $hgh^{-1} \in S \cap G_{j-1}$?
- [ ] Q3 Abelian quotient, first proof: which homomorphism $S \cap G_j \to G_j/G_{j-1}$, with which kernel?
- [ ] Q4 Abelian quotient, second proof (lecture 10/9): why does every commutator of $S \cap G_j$ lie in $S \cap G_{j-1}$?
- [ ] Q5 **[why]** Deduce: $S_n$ is not solvable for $n \geq 5$ once $A_n$ is not.

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G9 (move properties along subgroups) and G8.
> - Kernel $(S \cap G_j) \cap G_{j-1}$ by Lemma [[§41 The First and Second Isomorphism Theorems#^lem-41-4|§41.4]]; image a subgroup of an abelian group.
> - Second proof: Proposition [[§47 Commutators#^prop-47-11|§47.11]].

#### Quotients of solvable groups are solvable · P2

If $G$ is solvable and $\pi : G \to Q$ is surjective, then $(\pi(G_j))$ is a chain for $Q$ with abelian quotients, see Proposition [[§48 Solvable Groups#^prop-48-3|§48.3]]. *Source: WS 9.3; lecture 10/9.*

^nd-prop-48-3

- [ ] Q1 **[state]** State the proposition and the candidate chain.
- [ ] Q2 Why are the $\pi(G_j)$ subgroups with $\pi(G_0) = \{e\}$ and $\pi(G_N) = Q$? Where is surjectivity used?
- [ ] Q3 Normality: compute $\pi(g)\pi(h)\pi(g)^{-1}$.
- [ ] Q4 Abelian quotients: why do commutators of $\pi(G_j)$ lie in $\pi(G_{j-1})$?
- [ ] Q5 **[why]** Why is "$\pi(G_j)/\pi(G_{j-1}) \cong G_j/G_{j-1}$" false? Give the example $N = G$.

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G9 and G8.
> - $\pi(ghg^{-1}h^{-1}) \in \pi(G_{j-1})$ by Proposition [[§47 Commutators#^prop-47-11|§47.11]].
> - Remark [[§48 Solvable Groups#^rem-48-2|§48]] (do not cancel $N$).

#### Subquotients: an injection and a surjection · P2

$(S \cap G_j)/(S \cap G_{j-1}) \hookrightarrow G_j/G_{j-1}$ and $G_j/G_{j-1} \twoheadrightarrow \pi(G_j)/\pi(G_{j-1})$ are well-defined homomorphisms, see Proposition [[§48 Solvable Groups#^prop-48-4|§48.4]]. *Source: lecture 10/9.*

^nd-prop-48-4

- [ ] Q1 **[state]** State both maps and what they prove.
- [ ] Q2 (1): which homomorphism induces the injection, and why is it well defined and injective?
- [ ] Q3 (2): define $\varphi : G_j \to \pi(G_j)/\pi(G_{j-1})$. Why is $G_{j-1} \subseteq \operatorname{Ker}\varphi$, and why is the induced map well defined and surjective?
- [ ] Q4 **[why]** Why do subgroups and homomorphic images of abelian groups being abelian finish WS 9.2 and 9.3? What is the lecture's advice instead of chasing isomorphism formulas?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G2 and G5.
> - (1) First Isomorphism Theorem on $x \mapsto xG_{j-1}$; (2) $y = xn$ gives $\varphi(y) = \varphi(x)$.
> - Remark [[§48 Solvable Groups#^rem-48-2|§48]].

#### Solvability via the derived series · P2

$G$ is solvable iff $D_N(G) = \{e\}$ for some $N$, see Theorem [[§49 The Derived Series#^thm-49-1|§49.1]]. *Source: WS 9.6; lecture 10/9 ($\Leftarrow$), 10/12 ($\Rightarrow$).*

^nd-thm-49-1

- [ ] Q1 **[state]** State the theorem.
- [ ] Q2 ($\Leftarrow$) Why is the derived series, read upwards, a chain with abelian quotients?
- [ ] Q3 ($\Rightarrow$) State the claim $D_k(G) \subseteq G_{N-k}$ and the two facts used.
- [ ] Q4 Prove fact (1): $H \subseteq K$ implies $D(H) \subseteq D(K)$.
- [ ] Q5 Do the induction step.
- [ ] Q6 **[why]** In words, how fast does the derived series descend compared to any abelian chain? Why does this give an algorithm?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G8 and G9.
> - ($\Leftarrow$) Propositions [[§47 Commutators#^prop-47-4|§47.4]] and [[§47 Commutators#^prop-47-6|§47.6]] applied to $D_k(G)$.
> - ($\Rightarrow$) $D_k(G) = D(D_{k-1}(G)) \subseteq D(G_{N-k+1}) \subseteq G_{N-k}$ by fact (1), then Proposition [[§47 Commutators#^prop-47-11|§47.11]].

#### $A_n$ and $S_n$ are not solvable for $n \geq 5$ · P2

For $n \geq 5$ neither $A_n$ nor $S_n$ is solvable, so $S_n$ is solvable iff $n \leq 4$; the derived series of $S_n$ is $S_n \trianglerighteq A_n \trianglerighteq A_n \cdots$, of $S_4$ it is $S_4 \trianglerighteq A_4 \trianglerighteq K \trianglerighteq \{e\}$, see Corollary [[§49 The Derived Series#^cor-49-2|§49.2]] and Example [[§49 The Derived Series#^ex-49-1|§49.1]]. *Source: not from class (the standard consequence of simplicity and WS 9).*

^nd-cor-49-2

- [ ] Q1 **[state]** State the corollary.
- [ ] Q2 Given a chain for $A_n$, take the largest $j$ with $G_j \neq A_n$. Why is $G_j = \{e\}$, and why is that a contradiction?
- [ ] Q3 Why does $S_n$ then fail to be solvable, and why is $S_n$ solvable for $n \leq 4$?
- [ ] Q4 Second route: compute $D(A_4) = K$ (one commutator plus normality) and $D(A_n) = A_n$ for $n \geq 5$.
- [ ] Q5 **[why]** Why does the simplicity route need $n \geq 5$? What happens to the argument for $A_4$ (which normal subgroup breaks it)?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G9 and G13.
> - Simplicity: Theorem [[§43 Simple Groups#^thm-43-9|§43.9]]; subgroups: Proposition [[§48 Solvable Groups#^prop-48-2|§48.2]]; Proposition [[§48 Solvable Groups#^prop-48-1|§48.1]].
> - $(1\,2\,3)(1\,2\,4)(1\,2\,3)^{-1}(1\,2\,4)^{-1} = (1\,2)(3\,4)$; $D(A_n) = A_n$ by Theorem [[§47 Commutators#^thm-47-10|§47.10]].

### Priority 4 · notes only (Pinter, MATH 412, not from class)

#### Characters are constant on conjugacy classes · P4

Proposition [[§46 Characters#^prop-46-1|§46.1]] → drilled as [[493 Problem Set 2#^hw-2-4|PS2.4]].

#### A common eigenvector yields a character · P4

Theorem [[§46 Characters#^thm-46-2|§46.2]] and Example [[§46 Characters#^ex-46-2|§46.2]] → drilled as [[493 Problem Set 2#^hw-2-3|PS2.3]] (also shown in lecture 9/23: the sign as the eigenvalue on $\Delta$).

#### Characters kill commutators; 3-cycles are and transpositions are not commutators · P4

Propositions [[§47 Commutators#^prop-47-1|§47.1]], [[§47 Commutators#^prop-47-2|§47.2]], [[§47 Commutators#^prop-47-3|§47.3]] → drilled as [[493 Problem Set 2#^hw-2-4|PS2.4]].

#### The commutator subgroup and characters of $S_n$ · P4

Theorem [[§47 Commutators#^thm-47-5|§47.5]] (with Example [[§47 Commutators#^ex-47-1|§47.1]] and Corollary [[§47 Commutators#^cor-47-7|§47.7]]) → drilled as [[493 Problem Set 4#^hw-4-5|PS4.5]].

#### The abelianization is abelian · P4

Proposition [[§47 Commutators#^prop-47-6|§47.6]] → drilled as [[493 Problem Set 4#^hw-4-4|PS4.4]] (also WS 9.5).

#### Normal subgroups with trivial intersection commute · P4

Proposition [[§47 Commutators#^prop-47-8|§47.8]] → drilled as [[493 Problem Set 4#^hw-4-2|PS4.2]].

#### Characters of $A_n$ are trivial for $n \geq 5$ · P4

Lemma [[§47 Commutators#^lem-47-9|§47.9]] and Theorem [[§47 Commutators#^thm-47-10|§47.10]] → drilled as [[493 Problem Set 5#^hw-5-3|PS5.3]].

#### Products of commutators that are not commutators · P4

Example [[§47 Commutators#^ex-47-2|§47.2]] → drilled as [[493 Problem Set 5#^hw-5-4|PS5.4]].

# T10. The Sylow theorems

## Definitions T10

### Priority 2 · worksheets and lectures

#### $p$-subgroup · P2

A subgroup of $G$ which is a $p$-group (order $p^j$), see Definition [[§51 p-Groups and Sylow Subgroups#^def-51-1|§51.1]]. *Source: WS 10.*

^nd-def-51-1

- [ ] Q1 **[def]** Define a $p$-subgroup (recall the definition of a $p$-group).
- [ ] Q2 **[example]** List the $2$-subgroups and $3$-subgroups of $S_3$; give a $2$-subgroup of $S_4$ of each order $1, 2, 4, 8$.
- [ ] Q3 **[use]** What is the key fact about a $p$-group acting on a set of size prime to $p$?
- [ ] Q4 **[why]** Why is every $p$-subgroup contained in a Sylow $p$-subgroup?

> [!tip]- Hints: where it lives, examples
> - Definition [[§35 The Center#^def-35-3|§35.3]]; Example [[§51 p-Groups and Sylow Subgroups#^ex-51-1|§51.1]].
> - Fixed points: Proposition [[§51 p-Groups and Sylow Subgroups#^prop-51-1|§51.1]]; containment: Proposition [[§52 The Sylow Theorems#^prop-52-5|§52.5]](1).

#### Sylow $p$-subgroup · P2

For $|G| = p^km$ with $p \nmid m$, a subgroup of order $p^k$, see Definition [[§51 p-Groups and Sylow Subgroups#^def-51-2|§51.2]]. *Source: WS 10.*

^nd-def-51-2

- [ ] Q1 **[def]** Define a Sylow $p$-subgroup.
- [ ] Q2 **[example]** Sylow subgroups of $S_3$ ($p = 2, 3$), of $S_4$ ($p = 2, 3$), of $S_5$ ($p = 5$), of $GL_2(\mathbb{F}_5)$ ($p = 5$).
- [ ] Q3 **[example]** What is the Sylow $p$-subgroup when $p \nmid |G|$? When $G$ is a $p$-group?
- [ ] Q4 **[use]** State the three Sylow theorems in one line each.
- [ ] Q5 **[why]** Why is a Sylow $p$-subgroup of $GL_n(\mathbb{F}_p)$ of order $p^{\binom{n}{2}}$?

> [!tip]- Hints: where it lives, examples
> - Example [[§51 p-Groups and Sylow Subgroups#^ex-51-1|§51.1]] ($3, 1$ and $3, 4$), Example [[§52 The Sylow Theorems#^ex-52-1|§52.1]] ($n_5 = 6$), Example [[§51 p-Groups and Sylow Subgroups#^ex-51-2|§51.2]].
> - Theorems [[§52 The Sylow Theorems#^thm-52-4|§52.4]], [[§52 The Sylow Theorems#^thm-52-6|§52.6]], [[§52 The Sylow Theorems#^thm-52-9|§52.9]]; order: Proposition [[§51 p-Groups and Sylow Subgroups#^prop-51-4|§51.4]].

## Proofs T10

### Priority 1 · problem sets (directly or extended)

#### Internal direct products · P1

If $H, L \leq G$ commute elementwise, $H \cap L = \{e\}$ and $|H||L| = |G|$, then $(h, l) \mapsto hl$ is an isomorphism $H \times L \to G$; elementwise commuting holds if $H$ is central, or if $H, L$ are both normal with trivial intersection, see Lemma [[§51 p-Groups and Sylow Subgroups#^lem-51-6|§51.6]]. *Source: from [[Group Theory HW Drill#^ps6-3-5|PS6.3(5)]] (central case, drilled as [[493 Problem Set 6#^hw-6-3|PS6.3]]); the normal case is used for order $pq$.*

^nd-lem-51-6

- [ ] Q1 **[state]** State the lemma with its three hypotheses and the two sufficient conditions.
- [ ] Q2 Why is $\varphi$ a homomorphism? Where is condition (1) used?
- [ ] Q3 Why is $\varphi$ injective, and why bijective?
- [ ] Q4 Normal case: show $hlh^{-1}l^{-1} \in H \cap L$ by grouping it two ways.
- [ ] Q5 **[why]** Why is "both normal" needed? Find $H, L \leq S_3$ with $H \cap L = \{e\}$ and $|H||L| = 6$ but $S_3 \not\cong H \times L$.

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G5 and G12.
> - $hh'll' = hlh'l'$; $hl = e$ gives $h = l^{-1} \in H \cap L$.
> - Same computation as [[Group Theory HW Drill#^ps4-2|PS4.2]] (Proposition [[§47 Commutators#^prop-47-8|§47.8]]). Counterexample: $A_3$ and $\langle (1\,2) \rangle$.

### Priority 2 · worksheets and lectures

#### Fixed points of a $p$-group action · P2

If a $p$-group $P$ acts on a finite set $X$ with $|X| \not\equiv 0 \pmod p$, then $P$ fixes a point of $X$, see Proposition [[§51 p-Groups and Sylow Subgroups#^prop-51-1|§51.1]]. *Source: WS 10.1. Proof pending in the notes.*

^nd-prop-51-1

- [ ] Q1 **[state]** State the proposition.
- [ ] Q2 **[why]** What are the possible orbit sizes of a $P$-action, by orbit–stabilizer? Which orbits have size $\not\equiv 0 \pmod p$?
- [ ] Q3 Deduce $|X| \equiv |X^P| \pmod p$, and conclude.
- [ ] Q4 **[use]** Where is it used: Lemma §52.1, and (in the same form) the count $|X| \equiv |X^P|$ in Sylow III?
- [ ] Q5 **[why]** Does the conclusion hold if $|X| \equiv 0 \pmod p$? (Take $P$ acting on itself.)

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G4 and G12 (fixed points mod $p$).
> - Orbit sizes divide $|P| = p^k$; the counting argument appears written out inside the proof of Theorem [[§52 The Sylow Theorems#^thm-52-9|§52.9]].
> - Used in Lemma [[§52 The Sylow Theorems#^lem-52-1|§52.1]].

#### Sylow subgroups of $S_3$ and $S_4$ · P2

$S_3$: three Sylow $2$-subgroups $\langle (i\,j) \rangle$, one Sylow $3$-subgroup $A_3$; $S_4$: three Sylow $2$-subgroups $K \cup \tau K$ of order $8$, four Sylow $3$-subgroups, see Example [[§51 p-Groups and Sylow Subgroups#^ex-51-1|§51.1]]. *Source: lecture 10/12 (the counts are not from class).*

^nd-ex-51-1

- [ ] Q1 **[state]** List the Sylow subgroups of $S_3$ and $S_4$ for $p = 2, 3$.
- [ ] Q2 Why are the Sylow $2$-subgroups of $S_4$ exactly the order-$8$ subgroups containing $K$? (Which theorem lists them?)
- [ ] Q3 Why are there four Sylow $3$-subgroups of $S_4$? (Count $3$-cycles.)
- [ ] Q4 Check $n_p \equiv 1 \pmod p$ and $n_p \mid m$ in each case.
- [ ] Q5 **[why]** Which Sylow subgroup of $S_3$ is normal, and why does that block the $pq$ argument for $|G| = 6$?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G10 and G12.
> - Correspondence for $S_4$ and $K$: Example [[§45 S₃, S₄, A₄ and A₅#^ex-45-2|§45.2]]; eight $3$-cycles, two per subgroup.
> - Remark [[§52 The Sylow Theorems#^rem-52-3|§52]] ($3 \equiv 1 \pmod 2$).

#### The unitriangular matrices are a Sylow $p$-subgroup of $GL_n(\mathbb{F}_p)$ · P2

The upper unitriangular matrices form a Sylow $p$-subgroup $P$ of $GL_n(\mathbb{F}_p)$, see Proposition [[§51 p-Groups and Sylow Subgroups#^prop-51-5|§51.5]]. *Source: WS 10.2. Proof pending in the notes.*

^nd-prop-51-5

- [ ] Q1 **[state]** State the proposition.
- [ ] Q2 **[why]** What has to be shown: that $P$ is a subgroup, and that $|P| = p^{\binom{n}{2}}$. Why is that the right order?
- [ ] Q3 Count $P$: how many free entries are there?
- [ ] Q4 Why is a product of unitriangular matrices unitriangular, and why is the inverse unitriangular?
- [ ] Q5 **[use]** Why does the whole proof of Sylow I rest on this proposition? Check it for $n = 2$, $p = 5$.

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G10 and G12.
> - $\binom{n}{2}$ entries above the diagonal; diagonal of a product is the product of diagonals.
> - Proposition [[§51 p-Groups and Sylow Subgroups#^prop-51-4|§51.4]]; Example [[§51 p-Groups and Sylow Subgroups#^ex-51-2|§51.2]]; Theorem [[§52 The Sylow Theorems#^thm-52-4|§52.4]].

#### A Sylow 5-subgroup of $GL_2(\mathbb{F}_5)$ · P2

$|GL_2(\mathbb{F}_5)| = 480 = 2^5 \cdot 3 \cdot 5$, and $\langle u \rangle$, $u = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$, is a Sylow $5$-subgroup, see Example [[§51 p-Groups and Sylow Subgroups#^ex-51-2|§51.2]]. *Source: lecture 10/14.*

^nd-ex-51-2

- [ ] Q1 **[state]** State the order of $GL_2(\mathbb{F}_5)$ and the Sylow $5$-subgroup.
- [ ] Q2 Compute $|GL_2(\mathbb{F}_5)|$ by counting columns.
- [ ] Q3 Compute $u^j$ and the order of $u$.
- [ ] Q4 **[why]** Why is $\langle u \rangle$ the unitriangular group for $n = 2$? Find a second Sylow $5$-subgroup (lower unitriangular) and the element conjugating one to the other.

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G10.
> - $(25 - 1)(25 - 5) = 480$; $u^j = \begin{pmatrix} 1 & j \\ 0 & 1 \end{pmatrix}$.
> - Conjugate by $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ (Sylow II, Theorem [[§52 The Sylow Theorems#^thm-52-6|§52.6]]).

#### $p$-subgroups lie in a conjugate of a Sylow subgroup · P2

If $\Pi$ is a Sylow $p$-subgroup of $\Gamma$ and $P \leq \Gamma$ a $p$-subgroup, then $P \subseteq \gamma\Pi\gamma^{-1}$ for some $\gamma$, see Lemma [[§52 The Sylow Theorems#^lem-52-1|§52.1]]. *Source: lecture 10/12.*

^nd-lem-52-1

- [ ] Q1 **[state]** State the lemma.
- [ ] Q2 Which set does $P$ act on, and why is its size prime to $p$?
- [ ] Q3 Which proposition gives a fixed coset $\gamma\Pi$?
- [ ] Q4 What is $\operatorname{Stab}(\gamma\Pi)$, and why does that give the conclusion?
- [ ] Q5 **[why]** Which unproved step does this rest on? Which two later results are this lemma (Sylow II, WS 10.5(1))?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G4, G11, G12.
> - $X = \Gamma/\Pi$, $|X| = m$; Proposition [[§51 p-Groups and Sylow Subgroups#^prop-51-1|§51.1]].
> - $\operatorname{Stab}(\gamma\Pi) = \gamma\Pi\gamma^{-1}$ (Proposition [[§31 G Acting on Coset Spaces#^prop-31-1|§31.1]](3)).

#### $p$-subgroups of $GL_n(\mathbb{F}_p)$ are conjugate into unitriangular matrices · P2

Every $p$-subgroup $Q \leq GL_n(\mathbb{F}_p)$ satisfies $\gamma^{-1}Q\gamma \subseteq P$ (unitriangular) for some $\gamma$, see Corollary [[§52 The Sylow Theorems#^cor-52-2|§52.2]]. *Source: lecture 10/12.*

^nd-cor-52-2

- [ ] Q1 **[state]** State the corollary.
- [ ] Q2 Which two results combine to prove it?
- [ ] Q3 How do you pass from $Q \subseteq \gamma P\gamma^{-1}$ to $\gamma^{-1}Q\gamma \subseteq P$?
- [ ] Q4 **[why]** Interpret it as a change of basis: why is it surprising (a subgroup of order $16$ of $GL_{10^6}(\mathbb{F}_2)$)?

> [!tip]- Hints: route of the proof in the notes
> - Proposition [[§51 p-Groups and Sylow Subgroups#^prop-51-5|§51.5]] and Lemma [[§52 The Sylow Theorems#^lem-52-1|§52.1]].
> - Remark [[§52 The Sylow Theorems#^rem-52-2|§52]].

#### Sylow subgroups of a subgroup · P2

If $\Pi$ is a Sylow $p$-subgroup of $\Gamma$ and $G \leq \Gamma$, then $G \cap \gamma\Pi\gamma^{-1}$ is a Sylow $p$-subgroup of $G$ for some $\gamma \in \Gamma$, see Proposition [[§52 The Sylow Theorems#^prop-52-3|§52.3]]. *Source: WS 10.3; class 10/14.*

^nd-prop-52-3

- [ ] Q1 **[state]** State both parts.
- [ ] Q2 Let $G$ act on $X = \Gamma/\Pi$. Why is some $G$-orbit of size prime to $p$?
- [ ] Q3 Compute $\operatorname{Stab}_G(\gamma\Pi)$.
- [ ] Q4 With $|G| = p^ln$, show by orbit–stabilizer that $p^l$ divides $|G \cap \gamma\Pi\gamma^{-1}|$.
- [ ] Q5 Why is $|G \cap \gamma\Pi\gamma^{-1}|$ a power $p^j$, and why $j \leq l$? Conclude $j = l$.
- [ ] Q6 **[why]** Compare with Lemma §52.1: what replaces the fixed point when $G$ is not a $p$-group?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G4 and G12.
> - Orbits partition $X$ and $p \nmid m = |X|$.
> - $h\gamma\Pi = \gamma\Pi \iff h \in \gamma\Pi\gamma^{-1}$; subgroup of $\gamma\Pi\gamma^{-1}$ (order $p^k$) and of $G$ (order $p^ln$).

#### The First Sylow Theorem · P2

Every finite group has a Sylow $p$-subgroup, see Theorem [[§52 The Sylow Theorems#^thm-52-4|§52.4]]. *Source: WS 10.4; class 10/14.*

^nd-thm-52-4

- [ ] Q1 **[state]** State Sylow I.
- [ ] Q2 Into which group $\Gamma$ do you embed $G$, and by which corollary?
- [ ] Q3 Which Sylow $p$-subgroup of $\Gamma$ is explicit?
- [ ] Q4 Apply WS 10.3 and pull back along the isomorphism $G \cong G'$.
- [ ] Q5 **[why]** Which step is still unproved in the notes? Why does Sylow I imply Cauchy's theorem?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G11 (embeddings into $GL_n$) and G12.
> - Corollary [[§25 Actions#^cor-25-6|§25.6]]; Proposition [[§51 p-Groups and Sylow Subgroups#^prop-51-5|§51.5]]; Proposition [[§52 The Sylow Theorems#^prop-52-3|§52.3]].
> - A Sylow subgroup of order $p^k$, $k \geq 1$, contains an element of order $p$ (take a power of any non-identity element).

#### $p$-subgroups and conjugates of a Sylow subgroup · P2

For a Sylow $p$-subgroup $P$ ($|P| = p^k$): every $p$-subgroup $Q$ lies in some $gPg^{-1}$; every subgroup $H$ with $p^k \mid |H|$ contains some $gPg^{-1}$, see Proposition [[§52 The Sylow Theorems#^prop-52-5|§52.5]]. *Source: WS 10.5; board 10/14.*

^nd-prop-52-5

- [ ] Q1 **[state]** State both parts.
- [ ] Q2 (1): which lemma is it?
- [ ] Q3 (2): why is $p^k$ the largest power of $p$ dividing $|H|$?
- [ ] Q4 (2): take a Sylow $p$-subgroup $Q$ of $H$; why is $Q = gPg^{-1}$?
- [ ] Q5 **[why]** Why is "every $p$-subgroup lies in a Sylow subgroup" a strengthening of Sylow I?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G12.
> - Lemma [[§52 The Sylow Theorems#^lem-52-1|§52.1]] with $\Gamma = G$, $\Pi = P$; Sylow I for $H$; equal orders.

#### The Second Sylow Theorem · P2

Any two Sylow $p$-subgroups are conjugate: $P_2 = gP_1g^{-1}$, see Theorem [[§52 The Sylow Theorems#^thm-52-6|§52.6]]. *Source: WS 10.6; lecture 10/16 ("by 10.3").*

^nd-thm-52-6

- [ ] Q1 **[state]** State Sylow II.
- [ ] Q2 Apply WS 10.3(2) with $\Gamma = G$, $\Pi = P_1$ and which subgroup in the role of $G$?
- [ ] Q3 Why is the resulting Sylow subgroup of $P_2$ equal to $P_2$, giving $P_2 \subseteq gP_1g^{-1}$?
- [ ] Q4 Why is the inclusion an equality?
- [ ] Q5 **[why]** Give the alternative one-line proof from WS 10.5(1). Why are all Sylow $p$-subgroups isomorphic?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G12 and G6.
> - Proposition [[§52 The Sylow Theorems#^prop-52-3|§52.3]] with $P_2$; $|gP_1g^{-1}| = |P_1| = |P_2|$.
> - Alternative: Proposition [[§52 The Sylow Theorems#^prop-52-5|§52.5]](1) with $Q = P_2$.

#### A normal Sylow subgroup is the only one · P2

A Sylow $p$-subgroup $P$ is normal iff it is the only Sylow $p$-subgroup ($n_p = 1$), see Corollary [[§52 The Sylow Theorems#^cor-52-7|§52.7]]. *Source: lecture 10/16 for (1); (2) not stated in lecture, used for order $15$.*

^nd-cor-52-7

- [ ] Q1 **[state]** State both directions.
- [ ] Q2 (1): use Sylow II.
- [ ] Q3 (2): why is $gPg^{-1}$ a Sylow $p$-subgroup for every $g$?
- [ ] Q4 **[why]** Which direction is used to prove a group is not simple from $n_p = 1$? Find $n_3$ for $A_4$: is its Sylow $3$-subgroup normal?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G12 and G13.
> - $Q = gPg^{-1} = P$; conjugation preserves order.
> - $A_4$: four Sylow $3$-subgroups, so not normal.

#### The order of a product of subgroups · P2

For finite $H, K \leq G$, $|HK| = |H||K|/|H \cap K|$, see Lemma [[§52 The Sylow Theorems#^lem-52-8|§52.8]]. *Source: not from lecture, filled in (the lecture uses it in Sylow III).*

^nd-lem-52-8

- [ ] Q1 **[state]** State the lemma. Is normality needed?
- [ ] Q2 Consider $\mu : H \times K \to HK$. Why is it surjective?
- [ ] Q3 For fixed $hk$, show the preimages are exactly $(hd, d^{-1}k)$, $d \in H \cap K$.
- [ ] Q4 Conclude the formula.
- [ ] Q5 **[why]** Why is $HK$ not always a subgroup even though the formula holds? Check with $A = \langle (1\,2) \rangle$, $B = \langle (1\,3) \rangle$ in $S_3$.

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G3 (counting fibres).
> - $d = h^{-1}h' = kk'^{-1} \in H \cap K$.
> - $|AB| = 4$ does not divide $6$ (Example [[§41 The First and Second Isomorphism Theorems#^ex-41-2|§41.2]]).

#### The Third Sylow Theorem · P2

The number $n_p$ of Sylow $p$-subgroups is $\equiv 1 \pmod p$, see Theorem [[§52 The Sylow Theorems#^thm-52-9|§52.9]]. *Source: stated on WS 10; lecture 10/16.*

^nd-thm-52-9

- [ ] Q1 **[state]** State Sylow III.
- [ ] Q2 Let $G$ act on the set $X$ of Sylow $p$-subgroups by conjugation, and restrict to a fixed $P \in X$. Why is $|X| \equiv |X^P| \pmod p$?
- [ ] Q3 Why is $P \in X^P$?
- [ ] Q4 Suppose $Q \neq P$ is fixed by $P$. Show $PQ$ is a subgroup.
- [ ] Q5 Compute $|PQ| = p^{2k - j}$ with $j < k$, and derive a contradiction.
- [ ] Q6 **[why]** Where is Sylow II used (or not) in this proof? Where is "$P$ normalizes $Q$" used?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G12 and G4.
> - $P$-orbit sizes divide $p^k$; singletons are fixed points.
> - $(x_1q_1)(x_2q_2) = (x_1x_2)(x_2^{-1}q_1x_2)q_2$; Lemma [[§52 The Sylow Theorems#^lem-52-8|§52.8]]; $p^{2k-j}$ does not divide $|G|$ (Lagrange).
> - Sylow II only makes the $G$-action transitive; the count uses only $P$.

#### The number of Sylow subgroups divides $|G|$ · P2

$n_p$ divides $|G|$, in fact $n_p \mid m$ where $|G| = p^km$; with Sylow III, $n_p \mid m$ and $n_p \equiv 1 \pmod p$, see Corollary [[§52 The Sylow Theorems#^cor-52-10|§52.10]]. *Source: lecture 10/16 ($n_p \mid |G|$); $n_p \mid m$ not from lecture.*

^nd-cor-52-10

- [ ] Q1 **[state]** State the corollary.
- [ ] Q2 Why is the conjugation action on $X$ transitive?
- [ ] Q3 Apply orbit–stabilizer: $|G| = n_p \cdot |\operatorname{Stab}_G(P)|$.
- [ ] Q4 Why does $P \subseteq \operatorname{Stab}_G(P)$ give $n_p \mid m$?
- [ ] Q5 **[why]** Use both constraints to find $n_3$, $n_5$ for $|G| = 15$, and $n_2$, $n_3$ for $|G| = 12$ (list the options).

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G12 and G4.
> - Sylow II; $p^k \mid |\operatorname{Stab}_G(P)|$ by Lagrange.
> - $|G| = 12$: $n_2 \in \{1, 3\}$, $n_3 \in \{1, 4\}$.

#### The Sylow 5-subgroups of $S_5$ · P2

$S_5$ has $n_5 = 6$ Sylow $5$-subgroups, see Example [[§52 The Sylow Theorems#^ex-52-1|§52.1]]. *Source: lecture 10/16.*

^nd-ex-52-1

- [ ] Q1 **[state]** State $n_5$ for $S_5$.
- [ ] Q2 Why is a Sylow $5$-subgroup cyclic of order $5$, and why are its non-identity elements $5$-cycles?
- [ ] Q3 Count the $5$-cycles.
- [ ] Q4 Why do two distinct Sylow $5$-subgroups meet only in $e$? Conclude $n_5 = 24/4$.
- [ ] Q5 **[why]** Check $n_5 \equiv 1 \pmod 5$ and $n_5 \mid 24$. Is a Sylow $5$-subgroup normal in $S_5$?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G12 and G10.
> - Theorem [[§29 The Index and Lagrange's Theorem#^thm-29-7|§29.7]]; $(1\,a\,b\,c\,d)$ gives $4! = 24$.
> - Intersection has order dividing $5$, not $5$.

#### Groups of order 15 · P2

Every group of order $15$ is cyclic, see Example [[§52 The Sylow Theorems#^ex-52-2|§52.2]]. *Source: lecture 10/16.*

^nd-ex-52-2

- [ ] Q1 **[state]** State the result.
- [ ] Q2 Find $n_3$ and $n_5$ from the Sylow constraints.
- [ ] Q3 Why are $P_3$, $P_5$ normal with trivial intersection?
- [ ] Q4 Which lemma splits $G \cong P_3 \times P_5$?
- [ ] Q5 Why is $\mathbb{Z}/3\mathbb{Z} \times \mathbb{Z}/5\mathbb{Z} \cong \mathbb{Z}/15\mathbb{Z}$?
- [ ] Q6 **[why]** Which step fails for order $6$?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G12, then G14 (CRT).
> - Corollaries [[§52 The Sylow Theorems#^cor-52-10|§52.10]], [[§52 The Sylow Theorems#^cor-52-7|§52.7]]; Lemma [[§51 p-Groups and Sylow Subgroups#^lem-51-6|§51.6]].
> - Order $6$: $n_2 = 3$ is allowed (remark [[§52 The Sylow Theorems#^rem-52-3|§52]]).

#### Groups of order $pq$ · P2

For primes $p < q$ with $q \not\equiv 1 \pmod p$, every group of order $pq$ is cyclic, see Proposition [[§52 The Sylow Theorems#^prop-52-11|§52.11]]. *Source: lecture 10/16 ("same for $|G| = pq$"); filled in.* **[class exercise, 10/16]**

^nd-prop-52-11

- [ ] Q1 **[state]** State the proposition with its hypothesis.
- [ ] Q2 Show $n_q = 1$. Which inequality is used?
- [ ] Q3 Show $n_p = 1$. Where is $q \not\equiv 1 \pmod p$ used?
- [ ] Q4 Conclude with internal direct products and CRT.
- [ ] Q5 **[why]** Why can the hypothesis not be dropped ($S_3$)? Which orders below $50$ does the result cover (e.g. $15, 33, 35$)?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: G12, G14.
> - Divisors of $pq$ are $1, p, q, pq$; mod $q$: $p \not\equiv 1$ since $1 < p < q$.
> - Lemma [[§51 p-Groups and Sylow Subgroups#^lem-51-6|§51.6]]; remark [[§52 The Sylow Theorems#^rem-52-3|§52]].

### Priority 4 · notes only (Pinter, MATH 412, not from class)

#### The order of $GL_n(\mathbb{F}_p)$ · P4

Lemma [[§51 p-Groups and Sylow Subgroups#^lem-51-3|§51.3]] and Proposition [[§51 p-Groups and Sylow Subgroups#^prop-51-4|§51.4]] (with Lemma [[§51 p-Groups and Sylow Subgroups#^lem-51-2|§51.2]]) → drilled as [[493 Problem Set 6#^hw-6-4|PS6.4]].

#### Groups of order $p^2$ · P4

Theorem [[§51 p-Groups and Sylow Subgroups#^thm-51-7|§51.7]] and Corollary [[§51 p-Groups and Sylow Subgroups#^cor-51-8|§51.8]] → drilled as [[493 Problem Set 6#^hw-6-3|PS6.3]].
