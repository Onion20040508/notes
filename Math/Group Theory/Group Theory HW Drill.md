---
type: review
subject: "[[Group Theory]]"
tags: [group-theory, math493, review]
---
↑ [[Group Theory]] · [[Group Theory Midterm Review|Midterm Review]] · [[Group Theory Notes Drill|Notes Drill]]

# Problem Set Drill (PS1–PS6)

Midterm: Thursday, October 22, 6:00–8:00 PM (topic list on Canvas). Every Friday quiz was "one fairly straightforward problem from each homework", so the problem sets are the best model of exam questions. Every problem of Problem Sets 1–6 is broken here into small questions, in order. All six sets are submitted.

**How to drill.**
1. Read the statement and try the questions top to bottom on paper, closed book.
2. **[def]** marks a definition to state exactly; **[why]** asks what breaks without a hypothesis.
3. Tick a question when you can answer it without looking.
4. When all the questions of a problem are ticked, write the full proof in one go.
5. Only open **Hints** when stuck. It lists the definitions and results involved (linked to the notes), the strategy (codes G1–G14, listed at the end) and a note on your submitted solution.

## Problem Set 1 (due 9/10)

### PS1.1 Concepts seen before

Which of the following concepts have you seen defined before? groups, group actions, rings, modules, fields, vector spaces, monoids, categories.

^ps1-1

- [ ] Q1 **[def]** State the group axioms. Which axiom do you drop to get a monoid?
- [ ] Q2 **[def]** State the definition of a (left) action of $G$ on a set $X$, with both axioms.
- [ ] Q3 **[def]** State the notes' provisional definitions of a commutative ring and of a field. Why is $k^\times = k \setminus \{0\}$ a group under multiplication?
- [ ] Q4 **[why]** Give a monoid that is not a group, such as $(\mathbb{Z}, \cdot)$ or $(\mathbb{Z}_{\geq 0}, +)$. Which axiom fails? How does passing to the units fix this (compare $U_n$ inside $(\mathbb{Z}/n\mathbb{Z}, \cdot)$)?
- [ ] Q5 Explain how a vector space is a module over a field, and how an abelian group is a module over $\mathbb{Z}$.

> [!tip]- Hints: definitions, results, strategy
> **Topic and definitions.** A survey question, not a proof. These are the concepts on the list that the notes define:
> - Group: [[§1 The Definition of a Group#^def-1-1|Def §1.1]]; abelian group [[§1 The Definition of a Group#^def-1-2|Def §1.2]]
> - Group action: [[§25 Actions#^def-25-1|Def §25.1]]
> - Ring (commutative, provisional): [[§20 Polynomial Rings, Permutation Matrices, and Representations#^def-20-2|Def §20.2]]
> - Field (provisional): [[§3 Basic Examples of Groups#^def-3-3|Def §3.3]]; its multiplicative group [[§3 Basic Examples of Groups#^def-3-4|Def §3.4]]
> - Modules, vector spaces, monoids and categories are not defined in the notes.
>
> **Key results.** None. The problem-set note lists this problem without a "Treated in" line.
>
> **Strategy (no code).** Recall the definitions.
>
> **Difficulty 1.** Submitted solution: answers "groups, rings, fields, and vector spaces". There is no proof content.

### PS1.2 Conjugation is a homomorphism

Let $G$ be a group and let $a$ be an element of $G$. Show that $g \mapsto aga^{-1}$ is a group homomorphism $G \to G$.

^ps1-2

- [ ] Q1 **[def]** Define a group homomorphism. Why is there no need to check $\varphi(e) = e$ separately?
- [ ] Q2 Why does $c_a(g) = aga^{-1}$ land in $G$?
- [ ] Q3 Expand $c_a(gh)$ and insert $a^{-1}a$ between $g$ and $h$. Which axiom justifies each equality?
- [ ] Q4 Show that $c_{a^{-1}}$ is a two-sided inverse of $c_a$, so $c_a$ is an automorphism.
- [ ] Q5 Show $c_a \circ c_b = c_{ab}$. Which identity for $(ab)^{-1}$ does this use? Conclude that $a \mapsto c_a$ is a homomorphism $G \to \operatorname{Aut}(G)$.
- [ ] Q6 **[why]** The proof never uses commutativity. What is $c_a$ when $G$ is abelian? Find $a, g \in S_3$ with $c_a(g) \neq g$.
- [ ] Q7 **[why]** Is left multiplication $g \mapsto ag$ a homomorphism? Which equation fails, and for which $a$ does it hold?

> [!tip]- Hints: definitions, results, strategy
> **Topic and definitions.** Homomorphisms and conjugation.
> - Group homomorphism: [[§15 Homomorphisms#^def-15-1|Def §15.1]]
> - Conjugation by a: [[§18 Conjugation, Products, and Pointwise Products#^def-18-2|Def §18.2]]; conjugate elements [[§18 Conjugation, Products, and Pointwise Products#^def-18-3|Def §18.3]]
> - Automorphism, Aut(G): [[§18 Conjugation, Products, and Pointwise Products#^def-18-1|Def §18.1]]; inner automorphism [[§18 Conjugation, Products, and Pointwise Products#^def-18-4|Def §18.4]]
>
> **Key results.** [[§18 Conjugation, Products, and Pointwise Products#^prop-18-1|Prop §18.1]] (this problem, plus parts (2)–(3) on automorphisms); homomorphisms preserve the identity and inverses [[§15 Homomorphisms#^prop-15-1|Prop §15.1]]; inverse of a product [[§2 First Consequences of the Axioms#^prop-2-4|Prop §2.4]]; [[§18 Conjugation, Products, and Pointwise Products#^rem-18-1|Remark: Earlier Occurrences of Conjugation]].
>
> **Strategy (G6).** Insert $e = a^{-1}a$ between $g$ and $h$ and regroup. No factors are reordered.
>
> **Difficulty 1.** Submitted solution: checks that the map lands in $G$, then gives the four-step computation that inserts $a^{-1}a$. It notes that commutativity is not used. Parts (2)–(3) of Prop §18.1 were not asked and are not in the submission.

### PS1.3 Pointwise products of homomorphisms

Let $G$ and $H$ be two groups and let $\alpha: G \to H$ and $\beta: G \to H$ be group homomorphisms. For $g \in G$, define $(\alpha\beta)(g) = \alpha(g) \ast \beta(g)$.

*Parts: (1), (2).*

^ps1-3

#### (1)

If $H$ is commutative, show that $\alpha\beta$ is a group homomorphism.

^ps1-3-1

- [ ] Q1 **[def]** Define the pointwise product $\alpha\beta$. What does "$H$ commutative" mean?
- [ ] Q2 Expand $(\alpha\beta)(ab)$ using that $\alpha$ and $\beta$ are homomorphisms.
- [ ] Q3 Expand $(\alpha\beta)(a)\,(\alpha\beta)(b)$. Which pair of adjacent factors must be swapped to match Q2?
- [ ] Q4 Justify each regrouping by associativity and the swap by commutativity, then conclude.
- [ ] Q5 Show further that $\operatorname{Hom}(G, H)$ is an abelian group under the pointwise product. What is the identity? Why is $g \mapsto \alpha(g)^{-1}$ a homomorphism, and where is commutativity of $H$ used again?
- [ ] Q6 **[why]** Which hypothesis is really needed, commutativity of $G$ or of $H$? Would it be enough for every $\alpha(x)$ to commute with every $\beta(y)$?

> [!tip]- Hint (1): strategy
> **Strategy (G8).** Expand both sides. A single swap of the adjacent factors $\alpha(b)\beta(a)$ uses commutativity of $H$.

#### (2)

Give an example of two groups and two homomorphisms such that $\alpha\beta$ is not a homomorphism.

^ps1-3-2

- [ ] Q1 **[def]** Write out, with quantifiers, what it means for a map *not* to be a homomorphism.
- [ ] Q2 Why is $\operatorname{id}_H$ a homomorphism, and what map is $\operatorname{id}_H \cdot \operatorname{id}_H$?
- [ ] Q3 Show that $(ab)^2 = a^2 b^2$ forces $ab = ba$. Which cancellations do you use?
- [ ] Q4 Pick non-commuting $a, b \in S_3$ and compute $(ab)^2$ and $a^2 b^2$ explicitly.
- [ ] Q5 **[why]** By (a), $H$ must be non-abelian in any counterexample. Can $G$ be abelian? Try $G = \mathbb{Z}$ with $\alpha(m) = a^m$, $\beta(m) = b^m$, where $ab \neq ba$.

> [!tip]- Hint (2): strategy
> **Strategy (G10).** Take $\alpha = \beta = \operatorname{id}_H$ with $H$ non-abelian. Then $\alpha\beta$ is $g \mapsto g^2$.

> [!tip]- Hints: definitions and results for the whole problem
> **Topic and definitions.**
> - Hom(G, H): [[§18 Conjugation, Products, and Pointwise Products#^def-18-5|Def §18.5]]; pointwise product [[§18 Conjugation, Products, and Pointwise Products#^def-18-6|Def §18.6]]
> - Abelian group: [[§1 The Definition of a Group#^def-1-2|Def §1.2]]; homomorphism [[§15 Homomorphisms#^def-15-1|Def §15.1]]
>
> **Key results.** [[§18 Conjugation, Products, and Pointwise Products#^prop-18-2|Prop §18.2]] (this problem); squaring is a homomorphism iff the group is abelian [[§18 Conjugation, Products, and Pointwise Products#^prop-18-4|Prop §18.4]]; [[§18 Conjugation, Products, and Pointwise Products#^rem-18-2|Remark: Relation between PS 1.3(2) and PS 1.4(3)]]; cancellation [[§2 First Consequences of the Axioms#^prop-2-1|Prop §2.1]].
>
> **Difficulty** (a) 1, (b) 1. Submitted solution: (a) is a five-step chain with every equality justified (associativity twice, one commutativity swap). (b) takes $G = H$ non-abelian and $\alpha = \beta = \operatorname{id}$, reaches a contradiction by left and right cancellation, and gives the concrete case $S_3$ with $(1\,2), (1\,3)$. The notes use $(1\,2), (2\,3)$.

### PS1.4 Product groups, the diagonal and the multiplication map

Let $G$ and $H$ be two groups. The product group $G \times H$ has underlying set the Cartesian product, with multiplication $(g_1, h_1)(g_2, h_2) = (g_1 g_2, h_1 h_2)$. Define $\Delta: G \to G \times G$ by $\Delta(g) = (g, g)$, and $\nabla: G \times G \to G$ by $\nabla(g, h) = gh$.

*Parts: (1), (2), (3).*

^ps1-4

#### (1)

Check that $G \times H$ satisfies the axioms of a group.

^ps1-4-1

- [ ] Q1 **[def]** State the group axioms. Why do you first check that the formula is a binary operation on $G \times H$?
- [ ] Q2 Verify associativity componentwise.
- [ ] Q3 Identify the identity element and the inverse of $(g, h)$, checking both sides of each equation.
- [ ] Q4 Show that $G \times H$ is abelian iff both $G$ and $H$ are. For ($\Rightarrow$), use elements $(g, e_H)$.
- [ ] Q5 **[why]** Is $\mathbb{Z}/2\mathbb{Z} \times S_3$ abelian? Exhibit two elements that do not commute and explain which factor is responsible.

> [!tip]- Hint (1): strategy
> **Strategy.** Check componentwise: each axiom for $G \times H$ reduces to the same axiom in $G$ and in $H$.

#### (2)

Is $\Delta$ always a group homomorphism? If so, prove it; if not, give a counter-example.

^ps1-4-2

- [ ] Q1 **[def]** Define $\Delta$. State the homomorphism condition for a map into $G \times G$.
- [ ] Q2 Verify $\Delta(gh) = \Delta(g)\Delta(h)$ directly.
- [ ] Q3 Re-derive it from the criterion: a map into a product is a homomorphism iff both components are.
- [ ] Q4 Show $\Delta$ is injective, and that its image $\{(g, g)\}$ is a subgroup isomorphic to $G$.
- [ ] Q5 **[why]** Is the twisted diagonal $g \mapsto (g, g^{-1})$ a homomorphism? For which $G$? Compare inversion in Prop §18.4.

> [!tip]- Hint (2): strategy
> **Strategy.** Yes. Check directly, or note $\Delta = (\operatorname{id}, \operatorname{id})$ and use the componentwise criterion, Prop §18.3(3).

#### (3)

Is $\nabla$ always a group homomorphism? If so, prove it; if not, give a counter-example.

^ps1-4-3

- [ ] Q1 **[def]** Define $\nabla$ and write the homomorphism condition for general inputs $(g, h), (g', h')$.
- [ ] Q2 Show that $\nabla$ is a homomorphism when $G$ is abelian, using $\nabla = \pi_1 \cdot \pi_2$ and PS1.3(1).
- [ ] Q3 Evaluate the condition at $(g, h), (g, h)$ and show that equality forces $gh = hg$.
- [ ] Q4 Alternatively, evaluate at $(e, h), (g', e)$. What does the condition say directly?
- [ ] Q5 Give an explicit failure in $S_3$.
- [ ] Q6 **[why]** Which hypothesis makes $\nabla$ a homomorphism? Explain why the failure is a special case of PS1.3(2).

> [!tip]- Hint (3): strategy
> **Strategy (G10).** No. Evaluating at the pair $(g,h), (g,h)$ reduces the question to $(gh)^2 = g^2h^2$, which holds iff $gh = hg$.

> [!tip]- Hints: definitions and results for the whole problem
> **Topic and definitions.**
> - Direct product: [[§3 Basic Examples of Groups#^def-3-2|Def §3.2]]; group [[§1 The Definition of a Group#^def-1-1|Def §1.1]]
> - Structure maps (projections, inclusions, diagonal, multiplication map): [[§18 Conjugation, Products, and Pointwise Products#^def-18-7|Def §18.7]]
> - Homomorphism: [[§15 Homomorphisms#^def-15-1|Def §15.1]]
>
> **Key results.** [[§18 Conjugation, Products, and Pointwise Products#^prop-18-3|Prop §18.3]] (parts (1)–(2)); [[§18 Conjugation, Products, and Pointwise Products#^prop-18-4|Prop §18.4]] (part (3)); pointwise products [[§18 Conjugation, Products, and Pointwise Products#^prop-18-2|Prop §18.2]]; [[§18 Conjugation, Products, and Pointwise Products#^rem-18-2|Remark: Relation between PS 1.3(2) and PS 1.4(3)]]; images of subgroups [[§15 Homomorphisms#^prop-15-4|Prop §15.4]].
>
> **Difficulty** (a) 1, (b) 1, (c) 1. Submitted solution: (a) is a full axiom check, including that the formula is a binary operation. (b) is one line. (c) answers no: for non-abelian $G$ it evaluates at $(g,h),(g,h)$ and cancels, then gives the concrete case $S_3$ with $(1\,2), (1\,3)$. The notes add the equivalence with abelianness (Prop §18.4).

### PS1.5 The sign homomorphism and the alternating group

Let $S_n$ act on $\mathbb{Q}[x_1, \ldots, x_n]$ in the obvious way. Let $\Delta = \prod_{1 \leq i < j \leq n}(x_i - x_j)$. For $\sigma \in S_n$, let $M(\sigma)$ be the corresponding permutation matrix in $GL_n(\mathbb{Q})$. The alternating group $A_n$ is defined as the kernel of $\epsilon$.

*Parts: (1), (2), (3), (4).*

^ps1-5

#### (1)

Show that $\dfrac{\sigma(\Delta)}{\Delta} = (-1)^{\#\{(i,j) :\ 1 \leq i < j \leq n,\ \sigma(i) > \sigma(j)\}} = \det M(\sigma)$.

^ps1-5-1

- [ ] Q1 **[def]** Define $\operatorname{inv}(\sigma)$ and an adjacent inversion. Compute $\operatorname{inv}$ of $(1\,2\,3) \in S_3$, whose sequence of values is $(2, 3, 1)$.
- [ ] Q2 Write $\sigma(\Delta)$ as a product. Show that $\{i, j\} \mapsto \{\sigma(i), \sigma(j)\}$ is a bijection of the 2-element subsets of $\{1, \ldots, n\}$.
- [ ] Q3 Show that the factor $x_{\sigma(i)} - x_{\sigma(j)}$ is plus or minus the $\Delta$-factor of the image pair, with a minus sign exactly when $(i, j)$ is an inversion. Conclude $\sigma(\Delta) = (-1)^{\operatorname{inv}(\sigma)}\Delta$. Why may you divide by $\Delta$?
- [ ] Q4 Prove that swapping the entries at an adjacent inversion lowers $\operatorname{inv}$ by exactly $1$. Hint: write $\operatorname{inv}$ as the sum over values $v$ of $L(v)$, the number of larger values before $v$.
- [ ] Q5 Prove that there is no adjacent inversion iff $\operatorname{inv} = 0$. Conclude that bubble sort ends at $(1, \ldots, n)$ after exactly $\operatorname{inv}(\sigma)$ swaps.
- [ ] Q6 Translate each swap into a column swap of $M(\sigma)$ and conclude $\det M(\sigma) = (-1)^{\operatorname{inv}(\sigma)}$.
- [ ] Q7 **[why]** Does the result depend on whether column $j$ of $M(\sigma)$ is $e_{\sigma(j)}$ or its transpose is used? On the convention for how $\sigma$ acts on polynomials? Why not?

> [!tip]- Hint (1): strategy
> **Strategy.** First equality: a bijection on 2-element subsets, contributing one sign per inversion. Second equality: bubble sort, where each adjacent swap is one column swap of $M(\sigma)$.

#### (2)

We define $\epsilon(\sigma)$ to be given by any of the above formulas. Show that $\epsilon$ is a group homomorphism $S_n \to \{\pm 1\}$.

^ps1-5-2

- [ ] Q1 **[def]** Define $\epsilon$ (the notes write $\operatorname{sgn}$) and the group $\{\pm 1\}$.
- [ ] Q2 Prove $M(\sigma\tau) = M(\sigma)M(\tau)$ by comparing columns, using that $Ae_k$ is column $k$ of $A$.
- [ ] Q3 Conclude using multiplicativity of $\det$.
- [ ] Q4 **[why]** Why is the choice of formula irrelevant? Why is the inversion count alone a poor route to multiplicativity (see Ex §46.2 in PS2.3)?
- [ ] Q5 Show that $\epsilon$ is surjective for $n \geq 2$ and that $|A_n| = n!/2$.
- [ ] Q6 Deduce that the parity of the number of transpositions in a factorization of $\sigma$ is independent of the factorization.

> [!tip]- Hint (2): strategy
> **Strategy (G11).** $\epsilon = \det \circ M$ is a composite of two homomorphisms.

#### (3)

Show that $S_n$ is generated by the elements $(1\,j)$ for $2 \leq j \leq n$.

^ps1-5-3

- [ ] Q1 **[def]** Define the subgroup $\langle S \rangle$ generated by a set $S$.
- [ ] Q2 Verify $(k\ \ k{+}1) = (1\,k)(1\ \ k{+}1)(1\,k)$ by tracking elements. Why does the composition convention not matter here?
- [ ] Q3 Show that swapping positions $k, k+1$ in the sequence of values of $\rho$ gives the sequence of $\rho \circ (k\ \ k{+}1)$.
- [ ] Q4 Conclude $\sigma t_1 \cdots t_m = e$, hence $\sigma = t_m \cdots t_1$.
- [ ] Q5 Substitute Q2 into Q4. Why are no inverses needed?
- [ ] Q6 **[why]** Do $(1\,2)$ and $(3\,4)$ generate $S_4$? Which feature of the set $\{(1\,j)\}$ is missing, and where does Q2 use it?

> [!tip]- Hint (3): strategy
> **Strategy (G7).** Bubble sort writes $\sigma$ as a product of adjacent transpositions, and $(k\ \ k{+}1) = (1\,k)(1\ \ k{+}1)(1\,k)$.

#### (4)

Show that $A_n$ is generated by the elements $(1\,2\,k)$ for $3 \leq k \leq n$.

^ps1-5-4

- [ ] Q1 **[def]** Define $A_n$ as a kernel. Why is it a subgroup?
- [ ] Q2 Verify $(1\,k)(1\,2) = (1\,2\,k)$ and $(1\,2)(1\,k) = (1\,2\,k)^{-1}$. Deduce $\epsilon((1\,2\,k)) = 1$ and hence $\langle (1\,2\,k) \rangle_k \subseteq A_n$.
- [ ] Q3 For $\sigma \in A_n$, show that $\sigma$ is a product of an even number of transpositions $(1\,j)$. Why does each adjacent transposition contribute an odd number?
- [ ] Q4 Show $(1\,j)(1\,k) = (1\,2\,j)(1\,2\,k)^{-1}$ for distinct $j, k \geq 3$. Handle the cases $j = k$ and $2 \in \{j, k\}$.
- [ ] Q5 Group the factors in pairs and conclude. Why is $(1\,2\,k)^{-1}$ in the subgroup generated by the $(1\,2\,k)$?
- [ ] Q6 **[why]** Where is evenness of $\sigma$ used? What breaks in the pairing for an odd $\sigma$?

> [!tip]- Hint (4): strategy
> **Strategy (G7, G8).** For $\subseteq$, compute the sign. For $\supseteq$, write an even permutation as an even number of $(1\,j)$'s and pair them up.

> [!tip]- Hints: definitions and results for the whole problem
> **Topic and definitions.**
> - Action of S_n on polynomials: [[§20 Polynomial Rings, Permutation Matrices, and Representations#^def-20-3|Def §20.3]]; permutation matrices [[§20 Polynomial Rings, Permutation Matrices, and Representations#^def-20-6|Def §20.6]]
> - Inversions: [[§21 The Sign Homomorphism and the Alternating Group#^def-21-1|Def §21.1]]; the sign [[§21 The Sign Homomorphism and the Alternating Group#^def-21-2|Def §21.2]]; alternating group [[§21 The Sign Homomorphism and the Alternating Group#^def-21-3|Def §21.3]]
> - Kernel: [[§15 Homomorphisms#^def-15-3|Def §15.3]]; subgroup generated by several elements [[§4 Subgroups#^def-4-5|Def §4.5]]
>
> **Key results.** (1) [[§21 The Sign Homomorphism and the Alternating Group#^thm-21-2|Thm §21.2]], with the sorting lemma [[§21 The Sign Homomorphism and the Alternating Group#^lem-21-1|Lem §21.1]]. (2) [[§21 The Sign Homomorphism and the Alternating Group#^thm-21-3|Thm §21.3]], using [[§20 Polynomial Rings, Permutation Matrices, and Representations#^prop-20-5|Prop §20.5]]; consequences [[§21 The Sign Homomorphism and the Alternating Group#^cor-21-4|Cor §21.4]], [[§21 The Sign Homomorphism and the Alternating Group#^prop-21-5|Prop §21.5]]. (3) [[§21 The Sign Homomorphism and the Alternating Group#^thm-21-7|Thm §21.7]] via [[§21 The Sign Homomorphism and the Alternating Group#^lem-21-6|Lem §21.6]]. (4) [[§21 The Sign Homomorphism and the Alternating Group#^thm-21-9|Thm §21.9]] via [[§21 The Sign Homomorphism and the Alternating Group#^lem-21-8|Lem §21.8]]. Kernels are subgroups [[§15 Homomorphisms#^prop-15-2|Prop §15.2]].
>
> **Difficulty** (a) 2, (b) 1, (c) 2, (d) 2. Submitted solution: (a) proves in full both the bijection of 2-element subsets and the two bubble-sort lemmas, and states the column convention for $M$. (b) compares columns and uses multiplicativity of $\det$. (c) goes through adjacent transpositions and the sequence-of-values lemma. (d) proves both inclusions, using the parity of the number of $(1\,j)$ factors and a case analysis of pairs. It is the longest answer in the set, and §21 of the notes follows it step for step.

### PS1.6 Structure of the unit groups modulo n

You may assume Bézout's Lemma (for any integers $a, b$ there are $x, y$ with $ax + by = \gcd(a, b)$), the Chinese Remainder Theorem and unique prime factorization. (Stated without proof on the sheet: $(\mathbb{Z}/p^a\mathbb{Z})^\times$ is cyclic of order $(p-1)p^{a-1}$ for odd $p$; $(\mathbb{Z}/2^a\mathbb{Z})^\times$ is trivial for $a = 1$ and isomorphic to $\mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/2^{a-2}\mathbb{Z}$ for $a \geq 2$.)

*Parts: (1), (2), (3).*

^ps1-6

#### (1)

Let $n$ be a positive integer and $a$ another integer. Show that there exists $x$ such that $ax \equiv 1 \bmod n$ if and only if $\gcd(a, n) = 1$.

^ps1-6-1

- [ ] Q1 **[def]** Define $\gcd(a, n)$, "coprime", and "$ax \equiv 1 \bmod n$".
- [ ] Q2 ($\Leftarrow$) Use Bézout to produce $x$.
- [ ] Q3 ($\Rightarrow$) Rewrite the congruence as $ax - kn = 1$ and show that every common divisor of $a$ and $n$ divides $1$.
- [ ] Q4 Find the inverse of $[7]$ modulo $26$ by the extended Euclidean algorithm.
- [ ] Q5 **[why]** For $n = 6$, $a = 2$, show that no $x$ works. Which step of Q2 is unavailable?

> [!tip]- Hint (1): strategy
> **Strategy (G14).** ($\Leftarrow$) is Bézout. ($\Rightarrow$): a common divisor of $a$ and $n$ divides $ax - kn = 1$.

#### (2)

Let $(\mathbb{Z}/n\mathbb{Z})^\times$ be the set of residue classes $a$ modulo $n$ for which $\gcd(a, n) = 1$. Show that $(\mathbb{Z}/n\mathbb{Z})^\times$ is a group.

^ps1-6-2

- [ ] Q1 **[def]** Define $U_n$ and its operation. What does "well defined" mean here?
- [ ] Q2 Show that membership does not depend on the representative: $\gcd(a + kn, n) = \gcd(a, n)$.
- [ ] Q3 Show that $[a][b] = [ab]$ does not depend on the representatives.
- [ ] Q4 Closure: multiply $ax + ny = 1$ by $bu + nv = 1$ and read off $\gcd(ab, n) = 1$.
- [ ] Q5 Inverses: from $ax + ny = 1$, show that $[x] \in U_n$ and $[a][x] = [1]$.
- [ ] Q6 Associativity, the identity and commutativity are inherited from $\mathbb{Z}$. Why must well-definedness come first?
- [ ] Q7 **[why]** For $n = 6$, why is $\mathbb{Z}/6\mathbb{Z} \setminus \{[0]\}$ not a group under multiplication? Which axioms fail?

> [!tip]- Hint (2): strategy
> **Strategy (G2, G14).** Do two well-definedness checks, then verify the axioms. Closure comes from multiplying two Bézout identities.

#### (3)

Let $n = p_1^{a_1} \cdots p_r^{a_r}$. Define $(\mathbb{Z}/n\mathbb{Z})^\times \to \prod (\mathbb{Z}/p_i^{a_i}\mathbb{Z})^\times$ by $m \mapsto (m \bmod p_1^{a_1}, \ldots, m \bmod p_r^{a_r})$, the product of groups as in PS1.4. Show that this map is an isomorphism of groups.

^ps1-6-3

- [ ] Q1 **[def]** Define the product group $\prod_i U_{P_i}$. State the Chinese Remainder Theorem, with both its existence and its uniqueness clauses.
- [ ] Q2 Why are the $P_i$ pairwise coprime?
- [ ] Q3 Well defined: show that the image is independent of the representative (because $P_i \mid n$) and lies in the product of unit groups.
- [ ] Q4 Homomorphism: show $[ab]_{P} = [a]_P [b]_P$.
- [ ] Q5 Injective: use the uniqueness clause of the CRT, or alternatively Euclid's lemma inductively.
- [ ] Q6 Surjective: use the existence clause of the CRT, then get $\gcd(m, n) = 1$ from "coprime to each factor implies coprime to the product".
- [ ] Q7 Deduce $\varphi(n) = \prod_i (p_i - 1)p_i^{a_i - 1}$, and show $U_{15} \cong \mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/4\mathbb{Z}$.
- [ ] Q8 **[why]** Why must the moduli be coprime? Show that reduction $U_8 \to U_2 \times U_4$ is not injective.

> [!tip]- Hint (3): strategy
> **Strategy (G14, G2).** Reduction modulo $P_i = p_i^{a_i}$ respects products. The Chinese Remainder Theorem gives injectivity (uniqueness) and surjectivity (existence).

> [!tip]- Hints: definitions and results for the whole problem
> **Topic and definitions.**
> - Divisibility, congruence: [[§6 Divisibility and Congruence#^def-6-1|Def §6.1]], [[§6 Divisibility and Congruence#^def-6-3|Def §6.3]]
> - GCD, coprime: [[§8 Invertibility and Unit Groups#^def-8-1|Def §8.1]]; invertibility modulo n [[§8 Invertibility and Unit Groups#^def-8-2|Def §8.2]]
> - Unit group: [[§8 Invertibility and Unit Groups#^def-8-4|Def §8.4]]; well-defined [[§7 The Group ℤ∕nℤ#^def-7-2|Def §7.2]]
> - Direct product: [[§3 Basic Examples of Groups#^def-3-2|Def §3.2]]
>
> **Key results.** (1) [[§8 Invertibility and Unit Groups#^prop-8-1|Prop §8.1]]. (2) [[§8 Invertibility and Unit Groups#^prop-8-3|Prop §8.3]]. (3) [[§22 The Structure of Uₙ#^thm-22-2|Thm §22.2]] with [[§22 The Structure of Uₙ#^lem-22-1|Lem §22.1]]. Bézout [[§5 A Zoo of Subgroups#^cor-5-2|Cor §5.2]]; Chinese Remainder Theorem [[§9 Euclid's Lemma, Unique Factorization, and the Chinese Remainder Theorem#^thm-9-3|Thm §9.3]]; Euclid's lemma [[§9 Euclid's Lemma, Unique Factorization, and the Chinese Remainder Theorem#^lem-9-1|Lem §9.1]]; totient formula [[§22 The Structure of Uₙ#^cor-22-3|Cor §22.3]]; examples [[§22 The Structure of Uₙ#^ex-22-1|Ex §22.1]].
>
> **Difficulty** (a) 1, (b) 1, (c) 2. Submitted solution: (a) uses Bézout and divisibility. (b) does both well-definedness checks, gets closure by multiplying Bézout identities, and checks that the inverse lies in the set. (c) gets bijectivity from the CRT and proves $\gcd(m, n) = 1$ by induction for surjectivity. It adds a second injectivity proof via Euclid's lemma. The notes split the problem: (a)–(b) in §8, (c) in §22. Statement note: the sheet's "the product of groups is defined in ." has a missing cross-reference (it means Problem 1.4).
>
> ---
>
> ## Problem Set 2 (due 9/17)

### PS2.1 Cosets of a point stabilizer in the symmetric group

Let $S_n$ be the symmetric group of order $n$ (sic). Let $H = \{\sigma \in S_n : \sigma(n) = n\}$, so $H \cong S_{n-1}$.

*Parts: (1), (2).*

^ps2-1

#### (1)

Let $\alpha, \beta \in S_n$. Show that $\alpha H = \beta H$ if and only if $\alpha(n) = \beta(n)$.

^ps2-1-1

- [ ] Q1 **[def]** Define the left coset $\alpha H$. State the criterion: $\alpha H = \beta H$ iff $\beta^{-1}\alpha \in H$.
- [ ] Q2 Show that $H$ is a subgroup of $S_n$ and that restriction identifies $H \cong S_{n-1}$.
- [ ] Q3 ($\Rightarrow$) Use $\alpha \in \alpha H = \beta H$ to write $\alpha = \beta h$, then evaluate at $n$.
- [ ] Q4 ($\Leftarrow$) Show $\beta^{-1}\alpha \in H$, then $\alpha H \subseteq \beta H$. Why does symmetry give the reverse inclusion?
- [ ] Q5 Deduce that $\alpha H \mapsto \alpha(n)$ is a bijection $S_n/H \to \{1, \ldots, n\}$, so $[S_n : H] = n$ and $n! = (n-1)! \cdot n$.
- [ ] Q6 **[why]** Where does ($\Rightarrow$) use $e \in H$, and where does ($\Leftarrow$) use closure of $H$? Which subgroup property would a mere subset lack?

> [!tip]- Hint (1): strategy
> **Strategy (G2, G4).** $\alpha H = \beta H$ iff $\beta^{-1}\alpha \in H$, and $\beta^{-1}\alpha \in H$ says that $\beta^{-1}\alpha$ fixes $n$.

#### (2)

Give a similar criterion for when $\alpha^{-1}(n) = \beta^{-1}(n)$.

^ps2-1-2

- [ ] Q1 **[def]** Define the right coset $H\alpha$. State the criterion for $H\alpha = H\beta$.
- [ ] Q2 Guess the answer by applying (a) to $\alpha^{-1}, \beta^{-1}$, using $(H\alpha)^{-1} = \alpha^{-1}H$.
- [ ] Q3 ($\Rightarrow$) From $\alpha = h\beta$, derive $\alpha^{-1}h = \beta^{-1}$ and evaluate at $n$.
- [ ] Q4 ($\Leftarrow$) Show $\beta\alpha^{-1} \in H$ and $H\beta \subseteq H\alpha$.
- [ ] Q5 For $n = 3$, $\alpha = (1\,2\,3)$, $\beta = (1\,3)$, check that $\alpha H = \beta H$ but $H\alpha \neq H\beta$.
- [ ] Q6 **[why]** Why is the natural bijection between left and right cosets $gH \mapsto Hg^{-1}$ and not $gH \mapsto Hg$? Use Q5 to show that the latter is not well defined.

> [!tip]- Hint (2): strategy
> **Strategy (G2).** Right cosets: $H\alpha = H\beta$ iff $\beta\alpha^{-1} \in H$ iff $\alpha^{-1}(n) = \beta^{-1}(n)$.

> [!tip]- Hints: definitions and results for the whole problem
> **Topic and definitions.**
> - The point stabilizer in S_n: [[§30 Orbit–Stabilizer#^def-30-1|Def §30.1]]; stabilizer in general [[§26 Stabilizers and Fixed Points#^def-26-1|Def §26.1]]
> - Left and right cosets: [[§28 Left and Right Cosets#^def-28-2|Def §28.2]]; congruence modulo a subgroup [[§28 Left and Right Cosets#^def-28-1|Def §28.1]]
>
> **Key results.** [[§30 Orbit–Stabilizer#^prop-30-4|Prop §30.4]] (this problem); [[§30 Orbit–Stabilizer#^cor-30-5|Cor §30.5]] (index $n$); [[§30 Orbit–Stabilizer#^ex-30-2|Ex §30.2]]; [[§30 Orbit–Stabilizer#^rem-30-3|Remark: Why the Bijection Uses the Inverse]]; [[§30 Orbit–Stabilizer#^rem-30-4|Remark: As an Instance of Orbit–Stabilizer]]; cosets are equivalence classes [[§28 Left and Right Cosets#^prop-28-2|Prop §28.2]]; [[§30 Orbit–Stabilizer#^prop-30-1|Prop §30.1]] (WS 5.1, the general criterion); [[§28 Left and Right Cosets#^ex-28-2|Ex §28.2]].
>
> **Difficulty** (a) 1, (b) 1. Submitted solution: proves elementwise inclusion in both directions and invokes symmetry, then mirrors the argument for right cosets. The $S_3$ example appears as a remark. Statement note: "symmetric group of order $n$" on the sheet means degree $n$; the order is $n!$.

### PS2.2 Isomorphisms preserve central elements and proper subgroups

Let $G$ and $H$ be two groups and let $\phi: G \to H$ be an isomorphism, that is, a bijective homomorphism. The point is to practice using this hypothesis.

*Parts: (1), (2).*

^ps2-2

#### (1)

Let $z \in G$. If $z$ is central in $G$, meaning $zg = gz$ for all $g \in G$, then $\phi(z)$ is central in $H$.

^ps2-2-1

- [ ] Q1 **[def]** Define a central element and the center $Z(G)$.
- [ ] Q2 Given $h \in H$, which property of $\phi$ lets you write $h = \phi(g)$?
- [ ] Q3 Compute $\phi(z)h = \phi(z)\phi(g) = \cdots = h\phi(z)$, justifying each step.
- [ ] Q4 Apply the same to $\phi^{-1}$ (an isomorphism) to get $\phi(Z(G)) = Z(H)$.
- [ ] Q5 **[why]** Show that surjectivity is needed. In $\mathbb{Z}/2\mathbb{Z}$ every element is central; is the image of $[1]$ under the injective homomorphism $[k] \mapsto (1\,2)^k$ central in $S_3$?
- [ ] Q6 Use centers to show $\mathbb{Z}/6\mathbb{Z} \not\cong S_3$.

> [!tip]- Hint (1): strategy
> **Strategy.** Use surjectivity to write $h = \phi(g)$, then the homomorphism property twice.

#### (2)

Suppose that $G$ has a subgroup $G'$ other than $G$ and $\{e\}$. Show that $H$ has a subgroup $H'$ other than $H$ and $\{e\}$.

^ps2-2-2

- [ ] Q1 **[def]** Define a subgroup and state the subgroup test.
- [ ] Q2 Show $\phi(e_G) = e_H$ and $\phi(g^{-1}) = \phi(g)^{-1}$.
- [ ] Q3 Show that $\phi(G')$ is a subgroup: it contains the identity and is closed under products and inverses.
- [ ] Q4 Show $\phi(G') \neq \{e_H\}$ using injectivity.
- [ ] Q5 Show $\phi(G') \neq H$: take $g \notin G'$ and use injectivity.
- [ ] Q6 **[why]** If $\phi$ is only a surjective homomorphism, which of Q4–Q5 can fail? Test $\mathbb{Z}/4\mathbb{Z} \to \mathbb{Z}/2\mathbb{Z}$ with $G' = \{[0], [2]\}$.
- [ ] Q7 Conclude that $\mathbb{Z}/4\mathbb{Z}$ is not isomorphic to any group of prime order.

> [!tip]- Hint (2): strategy
> **Strategy (G1).** Take $H' = \phi(G')$. Injectivity gives both $H' \neq \{e\}$ and $H' \neq H$.

> [!tip]- Hints: definitions and results for the whole problem
> **Topic and definitions.**
> - Isomorphism: [[§16 Isomorphisms#^def-16-1|Def §16.1]]
> - Central element: [[§35 The Center#^def-35-1|Def §35.1]]; center [[§35 The Center#^def-35-2|Def §35.2]]
> - Subgroup: [[§4 Subgroups#^def-4-1|Def §4.1]]; subgroup criteria [[§4 Subgroups#^prop-4-2|Prop §4.2]]
>
> **Key results.** [[§16 Isomorphisms#^prop-16-6|Prop §16.6]] (this problem); images of subgroups [[§15 Homomorphisms#^prop-15-4|Prop §15.4]]; [[§15 Homomorphisms#^prop-15-1|Prop §15.1]]; the inverse of an isomorphism [[§16 Isomorphisms#^prop-16-1|Prop §16.1]]; [[§16 Isomorphisms#^rem-16-4|Remark: Using These to Distinguish Groups]]; [[§29 The Index and Lagrange's Theorem#^cor-29-8|Cor §29.8]].
>
> **Difficulty** (a) 1, (b) 1. Submitted solution: (a) is the direct computation. (b) proves the subgroup axioms for $\phi(G')$ from scratch, including $\phi(e) = e$, and uses injectivity twice. The notes add the statement $\phi(Z(G)) = Z(H)$ and the correspondence of subgroup lattices.

### PS2.3 A common eigenvector gives a character

Let $k$ be a field, $V$ a $k$-vector space, $GL(V)$ the group of invertible $k$-linear maps $V \to V$, and $G$ a subgroup of $GL(V)$. Suppose there is a nonzero $v \in V$ that is an eigenvector of every $g \in G$; write $gv = \lambda(g)v$.

*Parts: (1), (2).*

^ps2-3

#### (1)

Show that the map $\lambda: G \to k^\times$ is a group homomorphism.

^ps2-3-1

- [ ] Q1 **[def]** Define a character and $k^\times$. What does "$v$ is an eigenvector of $g$ with eigenvalue $\lambda(g)$" mean?
- [ ] Q2 Show that $\lambda(g)$ is uniquely determined: $av = bv$ with $v \neq 0$ forces $a = b$.
- [ ] Q3 Show $\lambda(g) \neq 0$ by applying $g^{-1}$.
- [ ] Q4 Compute $(g_1g_2)v = \lambda(g_1)\lambda(g_2)v$. Where do you use linearity of $g_1$, and where commutativity of $k$?
- [ ] Q5 Compare with $(g_1g_2)v = \lambda(g_1g_2)v$ and conclude.
- [ ] Q6 **[why]** Where is $v \neq 0$ used? What goes wrong for $v = 0$?

> [!tip]- Hint (1): strategy
> **Strategy (G8).** $\lambda(g) \neq 0$ because $g$ is invertible. Compute $(g_1g_2)v$ in two ways and cancel $v$.

#### (2)

Let $V$ be the vector space of degree $\binom{n}{2}$ polynomials in $x_1, \ldots, x_n$, and let $S_n \subseteq GL(V)$ act by permuting the variables. Describe a polynomial $f \in V$ that is an eigenvector for every $\sigma \in S_n$. What is the corresponding homomorphism $\lambda: S_n \to k^\times$?

^ps2-3-2

- [ ] Q1 **[def]** Define the action of $S_n$ on polynomials, and an alternating polynomial.
- [ ] Q2 Show that $\Delta$ is homogeneous of degree $\binom{n}{2}$.
- [ ] Q3 Show $\sigma\Delta = \operatorname{sgn}(\sigma)\Delta$, quoting PS1.5(1). Does that argument depend on the field?
- [ ] Q4 Conclude $\lambda = \operatorname{sgn}$, and recover from (a) that $\operatorname{sgn}$ is a homomorphism.
- [ ] Q5 Give a common eigenvector with a different character: a nonzero symmetric polynomial of degree $\binom{n}{2}$, such as $(x_1 + \cdots + x_n)^{\binom{n}{2}}$. Which character is it?
- [ ] Q6 **[why]** What is $\lambda$ when $k$ has characteristic $2$? Is $\Delta$ still a common eigenvector, and does it still detect odd permutations?

> [!tip]- Hint (2): strategy
> **Strategy (G8, G10).** $f = \Delta = \prod_{i<j}(x_i - x_j)$ is homogeneous of degree $\binom{n}{2}$, and $\lambda$ is the sign.

> [!tip]- Hints: definitions and results for the whole problem
> **Topic and definitions.**
> - Character: [[§46 Characters#^def-46-1|Def §46.1]]; multiplicative group of a field [[§3 Basic Examples of Groups#^def-3-4|Def §3.4]]
> - Action of S_n on polynomials: [[§20 Polynomial Rings, Permutation Matrices, and Representations#^def-20-3|Def §20.3]]; the sign [[§21 The Sign Homomorphism and the Alternating Group#^def-21-2|Def §21.2]]; alternating polynomial [[§21 The Sign Homomorphism and the Alternating Group#^def-21-4|Def §21.4]]
>
> **Key results.** (1) [[§46 Characters#^thm-46-2|Thm §46.2]]. (2) [[§46 Characters#^ex-46-2|Ex §46.2]], using [[§21 The Sign Homomorphism and the Alternating Group#^thm-21-2|Thm §21.2]]; [[§46 Characters#^rem-46-4|Remark: One-Dimensional Representations]]; [[§21 The Sign Homomorphism and the Alternating Group#^cor-21-10|Cor §21.10]].
>
> **Difficulty** (a) 1, (b) 1. Submitted solution: (a) checks that the values lie in $k^\times$ and that the eigenvalue is unique before proving the homomorphism property. (b) takes $\Delta$ with a degree count, gets the eigenvalue from PS1.5(1), and concludes $\lambda = \epsilon$. It quotes 1.5(a), which was proved over $\mathbb{Q}$, for an arbitrary field without comment; the sign argument there does not depend on the field. The characteristic-2 case, where $\lambda$ is trivial, is not discussed.

### PS2.4 Characters and commutators

Let $G$ and $A$ be groups with $A$ abelian, and let $\chi: G \to A$ be a homomorphism; such a $\chi$ is called a character of $G$. An element $h \in G$ is a commutator if $h = g_1g_2g_1^{-1}g_2^{-1}$ for some $g_1, g_2 \in G$.

*Parts: (1), (2), (3), (4).*

^ps2-4

#### (1)

Let $g_1$ and $g_2$ in $G$ be in the same conjugacy class. Show that $\chi(g_1) = \chi(g_2)$.

^ps2-4-1

- [ ] Q1 **[def]** Define a character and "same conjugacy class".
- [ ] Q2 Show $\chi(e_G) = e_A$.
- [ ] Q3 Explain why it suffices to prove $\chi(hgh^{-1}) = \chi(g)$ for all $g, h$.
- [ ] Q4 Compute $\chi(hgh^{-1})$, marking the step that needs $A$ abelian.
- [ ] Q5 **[why]** Drop commutativity of the target. The identity map $S_3 \to S_3$ is a homomorphism; check that it separates the conjugate elements $(1\,2)$ and $(1\,3)$. What does survive in general?

> [!tip]- Hint (1): strategy
> **Strategy (G8, G6).** It suffices to show $\chi(hgh^{-1}) = \chi(g)$. Commutativity of $A$ lets $\chi(h)$ and $\chi(h^{-1})$ meet and cancel.

#### (2)

Let $\chi: G \to A$ be a character and $h$ a commutator. Show that $\chi(h) = 1$.

^ps2-4-2

- [ ] Q1 **[def]** Define a commutator. Is $e$ a commutator?
- [ ] Q2 Expand $\chi(g_1g_2g_1^{-1}g_2^{-1})$ into four factors.
- [ ] Q3 Reorder in $A$ and show that the product is $e_A$.
- [ ] Q4 Deduce that every character is trivial on the commutator subgroup. Why does $\operatorname{Ker}\chi$ contain products of commutators too?
- [ ] Q5 **[why]** For a non-abelian target, find a homomorphism that does not kill a commutator. Try the identity map of $S_3$ and the commutator of $(1\,2)$ and $(2\,3)$.

> [!tip]- Hint (2): strategy
> **Strategy (G8).** Expand, regroup in the abelian group $A$, and cancel.

#### (3)

Let $n \geq 3$ and let $c$ be an element of $S_n$ of the form $(i\,j\,k)$. Show that $c$ is a commutator.

^ps2-4-3

- [ ] Q1 **[def]** What is a 3-cycle? Show $(i\,j\,k)^3 = e$ and $(i\,j\,k)^{-1} = (i\,k\,j)$.
- [ ] Q2 Show $(j\,k)(i\,j) = (i\,k\,j)$ by tracking elements, right factor first.
- [ ] Q3 Deduce $(j\,k)(i\,j)(j\,k)(i\,j) = (i\,k\,j)^2 = (i\,j\,k)$.
- [ ] Q4 Identify $g_1, g_2$ and check $g_1^{-1} = g_1$, $g_2^{-1} = g_2$.
- [ ] Q5 **[why]** This writes $c$ as a commutator of two transpositions, which are odd. Does it show that $c$ is a commutator of elements of $A_n$? What does Lem §47.9 need, and for which $n$?

> [!tip]- Hint (3): strategy
> **Strategy (G10).** $(j\,k)(i\,j) = (i\,k\,j)$, so $(j\,k)(i\,j)(j\,k)(i\,j) = (i\,k\,j)^2 = (i\,j\,k)$.

#### (4)

Let $s$ be an element of $S_n$ of the form $(i\,j)$. Show that $s$ is not a commutator. Hint: look at part (2).

^ps2-4-4

- [ ] Q1 **[def]** Define the sign. Why is it a character?
- [ ] Q2 Show $\operatorname{sgn}((i\,j)) = -1$, using $\det$ of a column swap.
- [ ] Q3 Apply the contrapositive of (b).
- [ ] Q4 **[why]** Can $(i\,j)$ be a product of several commutators? Combining (c) and (d) with PS1.5(4), why is $[S_n, S_n] = A_n$?

> [!tip]- Hint (4): strategy
> **Strategy (G8).** $\operatorname{sgn}$ is a character with $\operatorname{sgn}(s) = -1 \neq 1$. Apply the contrapositive of (b).

> [!tip]- Hints: definitions and results for the whole problem
> **Topic and definitions.**
> - Character: [[§46 Characters#^def-46-1|Def §46.1]]
> - Conjugacy class: [[§33 Conjugacy Classes#^def-33-1|Def §33.1]]; conjugate elements [[§18 Conjugation, Products, and Pointwise Products#^def-18-3|Def §18.3]]
> - Commutator: [[§47 Commutators#^def-47-1|Def §47.1]]; commutator subgroup [[§47 Commutators#^def-47-2|Def §47.2]]
>
> **Key results.** (1) [[§46 Characters#^prop-46-1|Prop §46.1]] and [[§46 Characters#^rem-46-3|Remark: Where Commutativity Is Needed]]. (2) [[§47 Commutators#^prop-47-1|Prop §47.1]] and [[§47 Commutators#^rem-47-1|Remark: The Contrapositive as a Tool]]. (3) [[§47 Commutators#^prop-47-2|Prop §47.2]]. (4) [[§47 Commutators#^prop-47-3|Prop §47.3]], with [[§21 The Sign Homomorphism and the Alternating Group#^cor-21-4|Cor §21.4]]. Later: [[§47 Commutators#^thm-47-5|Thm §47.5]] ($[S_n, S_n] = A_n$); [[§47 Commutators#^lem-47-9|Lem §47.9]].
>
> **Difficulty** (a) 1, (b) 1, (c) 1, (d) 1. Submitted solution: (a) writes $g_1$ and $g_2$ as conjugates of a common $g$. (c) goes through $(i\,k\,j)^2$ and $(i\,k\,j) = (j\,k)(i\,j)$. (d) computes the sign via $\det$ of a column swap.

### PS2.5 Groups of prime order

Let $p$ be a prime number and let $G$ be a group of order $p$. Show that $G$ is isomorphic to $\mathbb{Z}/p\mathbb{Z}$. Hint: let $g$ be a non-identity element of $G$. What can the order of $g$ be?

^ps2-5

- [ ] Q1 **[def]** Define the order of an element and a cyclic group.
- [ ] Q2 Show by pigeonhole that every element of a finite group has finite order.
- [ ] Q3 Show $|\langle g \rangle| = \operatorname{ord}(g)$: the list $e, g, \ldots, g^{d-1}$ is exhaustive (division algorithm) and has no repeats (minimality).
- [ ] Q4 By Lagrange $\operatorname{ord}(g) \mid p$. Exclude $\operatorname{ord}(g) = 1$.
- [ ] Q5 Conclude $\langle g \rangle = G$ by counting.
- [ ] Q6 Define $\varphi: \mathbb{Z}/p\mathbb{Z} \to G$, $[k] \mapsto g^k$. Check that it is well defined, a homomorphism, and bijective.
- [ ] Q7 **[why]** Why is primality essential? Give a group of order $4$ that is not cyclic, and say which step fails.
- [ ] Q8 Deduce that a group of prime order has no proper nontrivial subgroup and is generated by each of its non-identity elements.

> [!tip]- Hints: definitions, results, strategy
> **Topic and definitions.**
> - Order of a group, of an element: [[§4 Subgroups#^def-4-6|Def §4.6]], [[§4 Subgroups#^def-4-7|Def §4.7]]; cyclic group [[§4 Subgroups#^def-4-8|Def §4.8]]
> - Subgroup generated by an element: [[§4 Subgroups#^def-4-3|Def §4.3]]; the cyclic group Z/nZ [[§7 The Group ℤ∕nℤ#^def-7-1|Def §7.1]]
>
> **Key results.** [[§29 The Index and Lagrange's Theorem#^thm-29-7|Thm §29.7]] (this problem); finite order [[§4 Subgroups#^prop-4-8|Prop §4.8]]; Lagrange [[§29 The Index and Lagrange's Theorem#^thm-29-2|Thm §29.2]] and [[§29 The Index and Lagrange's Theorem#^cor-29-3|Cor §29.3]]; classification of cyclic groups [[§17 Cyclic Groups#^thm-17-1|Thm §17.1]]; $k \mapsto g^k$ [[§17 Cyclic Groups#^prop-17-3|Prop §17.3]]; [[§29 The Index and Lagrange's Theorem#^cor-29-8|Cor §29.8]].
>
> **Strategy (G3, G12).** $\operatorname{ord}(g) \mid p$ and $g \neq e$, so $\operatorname{ord}(g) = p$ and $\langle g \rangle = G$.
>
> **Difficulty 1.** Submitted solution: proves finite order by pigeonhole and quotes Lagrange's corollary. It lists $\langle g \rangle$ explicitly and verifies by hand that $\mathbb{Z}/p\mathbb{Z} \to G$ is well defined, a homomorphism and bijective, instead of citing the classification of cyclic groups.
>
> ---
>
> ## Problem Set 3 (due 9/24)

### PS3.1 Cayley's theorem and finite matrix groups

Let $G$ be a group with $n$ elements.

*Parts: (1), (2).*

^ps3-1

#### (1)

Show that $G$ is isomorphic to a subgroup of $S_n$.

^ps3-1-1

- [ ] Q1 **[def]** Define an action of $G$ on $X$ and the group $S_X$.
- [ ] Q2 Show that each $\hat g: x \mapsto g \star x$ is a bijection, with inverse $\widehat{g^{-1}}$.
- [ ] Q3 Show that $g \mapsto \hat g$ is a homomorphism $G \to S_X$. Which action axiom is this, literally?
- [ ] Q4 Check that left multiplication $g \star x = gx$ is an action and that it is faithful: evaluate $\hat g_1 = \hat g_2$ at $e$.
- [ ] Q5 Why is an injective homomorphism an isomorphism onto its image, and why is the image a subgroup?
- [ ] Q6 Show that a bijection $\beta: G \to \{1, \ldots, n\}$ induces an isomorphism $S_G \to S_n$, $\sigma \mapsto \beta\sigma\beta^{-1}$.
- [ ] Q7 **[why]** Why use left multiplication rather than conjugation? Find the kernel of the conjugation action, and say what it is for abelian $G$.
- [ ] Q8 Write out the Cayley embedding of $\mathbb{Z}/3\mathbb{Z}$ into $S_3$.

> [!tip]- Hint (1): strategy
> **Strategy (G11).** Left multiplication is a faithful action, giving an injective homomorphism $G \to S_G$. Relabelling gives $S_G \cong S_n$.

#### (2)

Let $k$ be a field. Show that $G$ is isomorphic to a subgroup of $GL_n(k)$.

^ps3-1-2

- [ ] Q1 **[def]** Define the permutation matrix $M(\sigma)$ and the group $GL_n(k)$.
- [ ] Q2 Show $M(\sigma\tau) = M(\sigma)M(\tau)$ and $M(e) = I$. Deduce that each $M(\sigma)$ is invertible.
- [ ] Q3 Show that $\sigma \mapsto M(\sigma)$ is injective. Where is $1 \neq 0$ in $k$ used?
- [ ] Q4 Compose $G \to S_n \to GL_n(k)$ and conclude.
- [ ] Q5 **[why]** The argument uses only $1 \neq 0$ from the field axioms. What would go wrong over the zero ring? Why is this embedding very inefficient in size (compare $|S_n| = n!$)?

> [!tip]- Hint (2): strategy
> **Strategy (G11).** Compose with the permutation representation $\sigma \mapsto M(\sigma)$, which is an injective homomorphism $S_n \to GL_n(k)$.

> [!tip]- Hints: definitions and results for the whole problem
> **Topic and definitions.**
> - Action: [[§25 Actions#^def-25-1|Def §25.1]]; symmetric groups S_X and S_n [[§3 Basic Examples of Groups#^def-3-5|Def §3.5]]
> - Kernel of an action: [[§25 Actions#^def-25-4|Def §25.4]]; faithful action [[§25 Actions#^def-25-5|Def §25.5]]
> - General linear group: [[§3 Basic Examples of Groups#^def-3-6|Def §3.6]]; permutation matrices [[§20 Polynomial Rings, Permutation Matrices, and Representations#^def-20-6|Def §20.6]]
>
> **Key results.** (1) [[§25 Actions#^thm-25-5|Thm §25.5]]. (2) [[§25 Actions#^cor-25-6|Cor §25.6]]. Actions are homomorphisms to S_X [[§25 Actions#^thm-25-3|Thm §25.3]]; each element acts bijectively [[§25 Actions#^prop-25-2|Prop §25.2]]; faithful actions embed [[§25 Actions#^prop-25-4|Prop §25.4]]; permutation representation [[§20 Polynomial Rings, Permutation Matrices, and Representations#^prop-20-5|Prop §20.5]]; images of subgroups [[§15 Homomorphisms#^prop-15-4|Prop §15.4]]; [[§25 Actions#^ex-25-3|Ex §25.3]]; [[§25 Actions#^rem-25-7|Remark: Why Cayley's Theorem Matters]].
>
> **Difficulty** (a) 1, (b) 1. Submitted solution: (a) proves the action-to-homomorphism lemma, shows that left multiplication is faithful, and writes out the relabelling isomorphism $S_G \to S_n$. (b) composes with permutation matrices and gets injectivity from $1 \neq 0$.

### PS3.2 A normal subgroup inside a subgroup of finite index

Let $G$ be a group and $H$ a subgroup with $[G : H] = n$. Show that there is a normal subgroup $N$ of $G$ with $N \subseteq H \subseteq G$ and $[G : N] \leq n!$. Hint: make a homomorphism $G \to S_n$ and think about the kernel. (The sheet prints $[G : H] \leq n!$; the intended statement is $[G : N] \leq n!$.)

^ps3-2

- [ ] Q1 **[def]** Define the index, a normal subgroup, and the kernel of an action.
- [ ] Q2 Show that $g \star (xH) = (gx)H$ is well defined and is an action on $G/H$.
- [ ] Q3 Get $\varphi: G \to S_{G/H}$ and set $N = \operatorname{Ker}\varphi$. Why is $N$ normal?
- [ ] Q4 Show $N \subseteq H$ by acting on the coset $eH$.
- [ ] Q5 Define $\bar\varphi: G/N \to S_{G/H}$ by $gN \mapsto \varphi(g)$. Check that it is well defined and injective, and conclude $[G : N] \leq |S_{G/H}| = n!$.
- [ ] Q6 Sharpen the result: $[G : N]$ divides $n!$ (apply Lagrange to $\varphi(G)$), and $N = \bigcap_x xHx^{-1}$ is the largest normal subgroup of $G$ contained in $H$.
- [ ] Q7 **[why]** Where is finiteness of $[G : H]$ used? Does $G$ need to be finite? Apply the result with $n = 2$ and deduce Prop §39.1.
- [ ] Q8 **[why]** Why not simply take $N = H$? For $H = \{e, (1\,2)\} \leq S_3$, compute $N$ and $[S_3 : N]$.

> [!tip]- Hints: definitions, results, strategy
> **Topic and definitions.**
> - Index: [[§29 The Index and Lagrange's Theorem#^def-29-1|Def §29.1]]; normal subgroup [[§38 Normal Subgroups#^def-38-1|Def §38.1]]
> - Kernel: [[§15 Homomorphisms#^def-15-3|Def §15.3]]; kernel of an action [[§25 Actions#^def-25-4|Def §25.4]]
>
> **Key results.** [[§39 Sources of Normal Subgroups#^thm-39-5|Thm §39.5]] (this problem); action on G/H [[§31 G Acting on Coset Spaces#^prop-31-1|Prop §31.1]]; [[§25 Actions#^thm-25-3|Thm §25.3]]; kernels are normal [[§39 Sources of Normal Subgroups#^prop-39-2|Prop §39.2]]; the normal core [[§39 Sources of Normal Subgroups#^prop-39-6|Prop §39.6]]; index 2 [[§39 Sources of Normal Subgroups#^prop-39-1|Prop §39.1]]; [[§41 The First and Second Isomorphism Theorems#^rem-41-3|Remark: PS 3.1 and PS 3.2 as Instances]].
>
> **Strategy (G11, G5, G2).** $G$ acts on the $n$ cosets $G/H$. Take $N$ to be the kernel of $G \to S_{G/H} \cong S_n$, and inject $G/N$ into $S_{G/H}$.
>
> **Difficulty 2.** Submitted solution: sets up the action on $G/H$ with a well-definedness check, shows the kernel is normal by a conjugation computation, gets $N \subseteq H$ from $eH$, and bounds the index with the injective map $G/N \to S_{G/H}$. A footnote records the misprint in the statement. Divisibility of $n!$ was not asked and is not proved; the notes add it in Prop §39.6.

### PS3.3 Burnside's lemma

Let $G$ be a finite group and $X$ a finite set on which $G$ acts. Show that $\frac{1}{\#G}\sum_{g \in G} \#\operatorname{Fix}(g) = \#(G\backslash X)$. Hint: count the pairs $(x, g)$ with $g(x) = x$ in two ways.

^ps3-3

- [ ] Q1 **[def]** Define $\operatorname{Fix}(g)$, $\operatorname{Stab}(x)$, the orbit $Gx$, and $G\backslash X$.
- [ ] Q2 Define $P$. Count it by second entries to get $\sum_g |\operatorname{Fix}(g)|$.
- [ ] Q3 Count $P$ by first entries to get $\sum_x |\operatorname{Stab}(x)|$.
- [ ] Q4 Apply orbit–stabilizer: $|\operatorname{Stab}(x)| = |G|/|Gx|$.
- [ ] Q5 Show that the orbits partition $X$ and that $y \in Gx$ implies $Gy = Gx$.
- [ ] Q6 Show that the terms $1/|Gx|$ over one orbit sum to $1$, and conclude.
- [ ] Q7 **[why]** Where is finiteness of $G$ and of $X$ used? Check the formula for $S_3$ acting on $\{1, 2, 3\}$.
- [ ] Q8 Apply it to the conjugation action: show that the number of conjugacy classes is the average size of a centralizer, and check this for $S_3$.

> [!tip]- Hints: definitions, results, strategy
> **Topic and definitions.**
> - Fixed points: [[§26 Stabilizers and Fixed Points#^def-26-2|Def §26.2]]; stabilizer [[§26 Stabilizers and Fixed Points#^def-26-1|Def §26.1]]
> - Orbit: [[§27 Orbits#^def-27-1|Def §27.1]]; orbit space [[§27 Orbits#^def-27-2|Def §27.2]], [[§27 Orbits#^def-27-4|Def §27.4]]
>
> **Key results.** [[§30 Orbit–Stabilizer#^thm-30-6|Thm §30.6]] (this problem); orbit–stabilizer [[§30 Orbit–Stabilizer#^thm-30-3|Thm §30.3]]; orbits partition X [[§27 Orbits#^prop-27-1|Prop §27.1]]; [[§30 Orbit–Stabilizer#^ex-30-3|Ex §30.3]].
>
> **Strategy (G4).** Count $P = \{(x, g) : g \star x = x\}$ by $g$ and by $x$. Orbit–stabilizer turns $\sum_x |\operatorname{Stab}(x)|$ into $|G| \sum_x 1/|Gx|$, and each orbit contributes $1$.
>
> **Difficulty 1.** Submitted solution: double count, then orbit–stabilizer. It proves inline that the orbit relation is an equivalence relation and that $Gy = Gx$, then regroups the sum orbit by orbit.

### PS3.4 Conjugacy classes, centralizers and the class equation

Let $G$ be a group and $g \in G$. The conjugacy class of $g$ is $\operatorname{Conj}(g) = \{hgh^{-1} : h \in G\}$, and the centralizer of $g$ is $Z(g) = \{h \in G : gh = hg\}$. Suppose that $G$ is finite.

*Parts: (1), (2).*

^ps3-4

#### (1)

Show that $\#(G) = \#\operatorname{Conj}(g) \cdot \#Z(g)$.

^ps3-4-1

- [ ] Q1 **[def]** Define $\operatorname{Conj}(g)$ and $Z(g)$. Why do the notes write $C_G(g)$ instead?
- [ ] Q2 Show that $h \star x = hxh^{-1}$ is an action. Where is $(h_1h_2)^{-1} = h_2^{-1}h_1^{-1}$ used?
- [ ] Q3 Identify the orbit of $g$ as $\operatorname{Conj}(g)$ and the stabilizer of $g$ as $Z(g)$.
- [ ] Q4 Apply orbit–stabilizer.
- [ ] Q5 **[why]** Where is finiteness of $G$ used? What statement survives for infinite $G$ (a bijection between which two sets)?
- [ ] Q6 For $S_3$, check that the class sizes are $1, 3, 2$ and the centralizer orders are $6, 2, 3$.

> [!tip]- Hint (1): strategy
> **Strategy (G4).** Orbit–stabilizer for the conjugation action: the orbit is $\operatorname{Conj}(g)$ and the stabilizer is $Z(g)$.

#### (2)

Let $g_1, \ldots, g_c$ be one representative from each conjugacy class of $G$. Prove the class equation $\sum_i \frac{1}{\#Z(g_i)} = 1$.

^ps3-4-2

- [ ] Q1 **[def]** What is a system of representatives of the conjugacy classes?
- [ ] Q2 Show that the conjugacy classes partition $G$, as orbits of an action.
- [ ] Q3 Write $|G| = \sum_i |\operatorname{Conj}(g_i)|$.
- [ ] Q4 Substitute (a) and divide by $|G|$.
- [ ] Q5 Derive the standard form $|G| = |Z(G)| + \sum [G : C_G(g_i)]$, with the sum over the non-central classes.
- [ ] Q6 **[why]** What goes wrong if two representatives come from the same class, or a class is missed? Check the equation for $S_4$: $24 = 1 + 6 + 3 + 8 + 6$.

> [!tip]- Hint (2): strategy
> **Strategy (G4).** The conjugacy classes partition $G$. Divide $|G| = \sum_i |\operatorname{Conj}(g_i)|$ by $|G|$ and use (a).

> [!tip]- Hints: definitions and results for the whole problem
> **Topic and definitions.**
> - Conjugacy class: [[§33 Conjugacy Classes#^def-33-1|Def §33.1]]
> - Centralizer (the notes write C_G(g)): [[§34 Conjugation as an Action and the Class Equation#^def-34-1|Def §34.1]]; [[§34 Conjugation as an Action and the Class Equation#^rem-34-1|Remark: Notation]]
> - Action: [[§25 Actions#^def-25-1|Def §25.1]]
>
> **Key results.** Conjugation action [[§34 Conjugation as an Action and the Class Equation#^prop-34-1|Prop §34.1]]; (1) [[§34 Conjugation as an Action and the Class Equation#^cor-34-2|Cor §34.2]]; (2) [[§34 Conjugation as an Action and the Class Equation#^cor-34-3|Cor §34.3]]; standard class equation [[§34 Conjugation as an Action and the Class Equation#^thm-34-4|Thm §34.4]]; [[§30 Orbit–Stabilizer#^thm-30-3|Thm §30.3]]; [[§27 Orbits#^prop-27-1|Prop §27.1]]; [[§34 Conjugation as an Action and the Class Equation#^ex-34-1|Ex §34.1]].
>
> **Difficulty** (a) 1, (b) 1. Submitted solution: (a) proves that conjugation is an action, identifies the orbit and the stabilizer, and applies orbit–stabilizer. (b) uses the partition argument by reference to PS3.3.

### PS3.5 Groups of prime-power order have nontrivial center

Let $p$ be a prime and let $G$ be a group of order $p^k$ for some $k \geq 1$.

*Parts: (1), (2).*

^ps3-5

#### (1)

Show that there is some $g \in G$ other than $e$ such that $\operatorname{Conj}(g) = \{g\}$.

^ps3-5-1

- [ ] Q1 **[def]** Define a $p$-group. What does $\operatorname{Conj}(g) = \{g\}$ mean?
- [ ] Q2 Show that each $|\operatorname{Conj}(g)|$ is a power of $p$, as a divisor of $p^k$.
- [ ] Q3 Show $\operatorname{Conj}(e) = \{e\}$, and write the class equation as $1 + \sum_{i \geq 2} p^{a_i} = p^k$.
- [ ] Q4 Suppose that every $a_i \geq 1$, and derive $p \mid 1$.
- [ ] Q5 Conclude that some $g_i \neq e$ has a one-element class.
- [ ] Q6 **[why]** Where is $k \geq 1$ used? Show that the conclusion fails for $S_3$, whose order is not a prime power.

> [!tip]- Hint (1): strategy
> **Strategy (G12, G4).** Every class size is a power of $p$. In $1 + \sum p^{a_i} = p^k$, not all $a_i$ can be positive, since then $p$ would divide $1$.

#### (2)

Show that this $g$ commutes with every $h \in G$.

^ps3-5-2

- [ ] Q1 **[def]** Define the centralizer and a central element.
- [ ] Q2 Show directly that $\operatorname{Conj}(g) = \{g\}$ iff $hgh^{-1} = g$ for all $h$ iff $g$ is central.
- [ ] Q3 Alternatively, use PS3.4(1): $|Z(g)| = |G|$ forces $Z(g) = G$.
- [ ] Q4 Deduce $Z(G) \neq \{e\}$, and in fact $p \mid |Z(G)|$.
- [ ] Q5 **[why]** Does (b) need $G$ to be finite, or to be a $p$-group? Which route, Q2 or Q3, needs finiteness?

> [!tip]- Hint (2): strategy
> **Strategy (G4).** A one-element class means $|Z(g)| = |G|$ by PS3.4(1). Alternatively, $hgh^{-1} = g$ for all $h$.

> [!tip]- Hints: definitions and results for the whole problem
> **Topic and definitions.**
> - p-group: [[§35 The Center#^def-35-3|Def §35.3]]
> - Central element, center: [[§35 The Center#^def-35-1|Def §35.1]], [[§35 The Center#^def-35-2|Def §35.2]]; centralizer [[§34 Conjugation as an Action and the Class Equation#^def-34-1|Def §34.1]]
>
> **Key results.** [[§35 The Center#^thm-35-3|Thm §35.3]] (this problem); [[§35 The Center#^cor-35-4|Cor §35.4]]; central iff singleton class [[§35 The Center#^prop-35-1|Prop §35.1]]; [[§34 Conjugation as an Action and the Class Equation#^cor-34-2|Cor §34.2]], [[§34 Conjugation as an Action and the Class Equation#^cor-34-3|Cor §34.3]], [[§34 Conjugation as an Action and the Class Equation#^thm-34-4|Thm §34.4]]; unique factorization [[§9 Euclid's Lemma, Unique Factorization, and the Chinese Remainder Theorem#^thm-9-2|Thm §9.2]].
>
> **Difficulty** (a) 2, (b) 1. Submitted solution: (a) gets class sizes as powers of $p$ from unique factorization, multiplies the reciprocal class equation by $p^k$, and reaches a contradiction mod $p$. (b) counts: $|Z(g)| = |G|$.

### PS3.6 Three conjugacy classes force order at most six

Let $G$ be a finite group with $3$ conjugacy classes. Show that $\#(G) \leq 6$. Hint: see Problem 3.4.

^ps3-6

- [ ] Q1 **[def]** State the reciprocal class equation and what the denominators are.
- [ ] Q2 Show that the class of $e$ is $\{e\}$ with centralizer $G$. Write $\frac1a + \frac1b + \frac1{|G|} = 1$ with $a \leq b$.
- [ ] Q3 Why is $b \leq |G|$? Show $a \leq 3$ and $a \neq 1$.
- [ ] Q4 Case $a = 2$: show $b \in \{3, 4\}$, giving $|G| = 6$ or $|G| = 4$.
- [ ] Q5 Case $a = 3$: show $b = 3$, giving $|G| = 3$.
- [ ] Q6 **[why]** Where is $b \leq |G|$ used? Without it, which inequality in Q4 is unjustified?
- [ ] Q7 Show that $|G| = 4$ does not occur (groups of order $4$ are abelian), and that orders $3$ and $6$ do occur.
- [ ] Q8 **[why]** With $c$ classes, why does the reciprocal equation still leave only finitely many possible orders (Landau's theorem)?

> [!tip]- Hints: definitions, results, strategy
> **Topic and definitions.**
> - Conjugacy class: [[§33 Conjugacy Classes#^def-33-1|Def §33.1]]; centralizer [[§34 Conjugation as an Action and the Class Equation#^def-34-1|Def §34.1]]
>
> **Key results.** [[§34 Conjugation as an Action and the Class Equation#^prop-34-5|Prop §34.5]] (this problem); reciprocal class equation [[§34 Conjugation as an Action and the Class Equation#^cor-34-3|Cor §34.3]]; [[§34 Conjugation as an Action and the Class Equation#^cor-34-7|Cor §34.7]] (only orders $3$ and $6$ occur); groups of order 4 are abelian [[§34 Conjugation as an Action and the Class Equation#^prop-34-6|Prop §34.6]]; [[§34 Conjugation as an Action and the Class Equation#^ex-34-1|Ex §34.1]].
>
> **Strategy (G4, G3).** The reciprocal class equation $\frac1a + \frac1b + \frac1{|G|} = 1$ with $a \leq b \leq |G|$ has finitely many solutions. Bound $a$, then $b$.
>
> **Difficulty 2.** Submitted solution: the same case analysis as the notes, ending with $|G| \in \{3, 4, 6\}$. It does not rule out $|G| = 4$, which the bound does not require; the notes do so in Cor §34.7.
>
> ## Problem Set 4 (due 10/1)

### PS4.1 Products of subgroups

*Parts: (1), (2).*

^ps4-1

#### (1)

Let $G$ be a group and $A, B$ subgroups of $G$, $AB = \{ab : a \in A,\ b \in B\}$. Give an example to show that $AB$ is not necessarily a subgroup of $G$.

^ps4-1-1

- [ ] Q1 **[def]** Define the product set $AB$. Is $AB = BA$ as sets in general?
- [ ] Q2 Take $A = \{e, (1\,2)\}$ and $B = \{e, (1\,3)\}$ in $S_3$. Why are both subgroups?
- [ ] Q3 List the four products $ab$ and compute $(1\,2)(1\,3)$ with right-to-left composition. Why are the four elements distinct?
- [ ] Q4 Compute $(1\,3\,2)^{-1}$ and show it is not in $AB$.
- [ ] Q5 Second route: why does $|AB| = 4$ alone rule out $AB$ being a subgroup of $S_3$?
- [ ] Q6 Compute $BA$. Does it equal $AB$?
- [ ] Q7 **[why]** Which hypothesis of Lem §41.3 fails here? Check by conjugating $(1\,2)$ by $(1\,3)$ that neither $A$ nor $B$ is normal in $S_3$.

> [!tip]- Hint (1): strategy
> **Strategy (G10, G3).** Two subgroups of $S_3$ generated by different transpositions: $AB$ has four elements and is not closed under inverses (and $4 \nmid 6$).

#### (2)

Suppose that $B$ is a normal subgroup of $G$. Show that, in this case, $AB$ is a subgroup of $G$. (The same conclusion holds if $A$ is normal; only one case needs to be written up.)

^ps4-1-2

- [ ] Q1 **[def]** State the definition of a normal subgroup and the equivalent form $gB = Bg$ for all $g$ (Thm §38.3).
- [ ] Q2 Why is $e \in AB$?
- [ ] Q3 For $ab, cd \in AB$ put $h = c^{-1}bc$. Why is $h \in B$, and why is $ab\,cd = (ac)(hd)$?
- [ ] Q4 Show $(ab)^{-1} = b^{-1}a^{-1} \in AB$ by writing it as $a^{-1}\,(ab^{-1}a^{-1})$.
- [ ] Q5 Redo the proof with the one-step test $xy^{-1} \in AB$ (Prop §4.2).
- [ ] Q6 Show $A \subseteq AB$ and $B \subseteq AB$, and that any subgroup containing $A$ and $B$ contains $AB$.
- [ ] Q7 Adapt Q3 to the case where $A$ (rather than $B$) is normal: which element do you conjugate now?
- [ ] Q8 **[why]** Point to the exact steps of Q3 and Q4 that use normality of $B$, and check that they break for the subgroups of part (1). Must $AB$ itself be normal (take $B = \{e\}$)?

> [!tip]- Hint (2): strategy
> **Strategy (G1, G6).** Check identity, closure and inverses; normality lets an element of $B$ move past an element of $A$: $bc = c\,(c^{-1}bc)$ with $c^{-1}bc \in B$.

> [!tip]- Hints: definitions and results for the whole problem
> **Topic and definitions.** Product sets of subgroups; normality.
> - Subgroup: [[§4 Subgroups#^def-4-1|Def §4.1]]; subgroup criteria [[§4 Subgroups#^prop-4-2|Prop §4.2]]
> - The product set $AB$ (written $HN$ in the notes): [[§41 The First and Second Isomorphism Theorems#^def-41-1|Def §41.1]]
> - Normal subgroup: [[§38 Normal Subgroups#^def-38-1|Def §38.1]]; equivalent forms [[§38 Normal Subgroups#^thm-38-3|Thm §38.3]]
>
> **Key results.** (1) is [[§41 The First and Second Isomorphism Theorems#^ex-41-2|Ex §41.2]]; (2) is [[§41 The First and Second Isomorphism Theorems#^lem-41-3|Lem §41.3]]. Used: multiplying cycles [[§12 Multiplying and Conjugating Cycles#^ex-12-1|Ex §12.1]], subgroups of $S_3$ [[§13 The Symmetric Group S₃#^prop-13-1|Prop §13.1]], Lagrange [[§29 The Index and Lagrange's Theorem#^thm-29-2|Thm §29.2]]. Used later by the Second Isomorphism Theorem [[§41 The First and Second Isomorphism Theorems#^thm-41-5|Thm §41.5]] and the order formula [[§41 The First and Second Isomorphism Theorems#^cor-41-6|Cor §41.6]].
>
> **Difficulty 1.** Submitted solution: (1) the $S_3$ example above with the product $(1\,2)(1\,3) = (1\,3\,2)$ traced point by point, and failure of closure under inverses; (2) a direct check of identity, closure (via $h = c^{-1}bc$) and inverses (via $a^{-1}(ab^{-1}a^{-1})$). The notes' Lem §41.3 combines the lecture's closure step with the submitted identity and inverse steps; Ex §41.2 is part (1) and adds the $4 \nmid 6$ remark.

### PS4.2 Normal subgroups with trivial intersection commute

Let $G$ be a group and let $M$ and $N$ be normal subgroups of $G$ with $M \cap N = \{e\}$. Show that, for any $m \in M$ and $n \in N$, we have $mn = nm$. Hint: write the conclusion in the form $mnm^{-1}n^{-1} = 1$.

^ps4-2

- [ ] Q1 **[def]** Define a commutator. Show $mn = nm$ if and only if $mnm^{-1}n^{-1} = e$.
- [ ] Q2 Show $mnm^{-1} \in N$, and conclude $x = (mnm^{-1})\,n^{-1} \in N$.
- [ ] Q3 Show $nm^{-1}n^{-1} \in M$, and conclude $x = m\,(nm^{-1}n^{-1}) \in M$.
- [ ] Q4 Conclude $x = e$, and derive $mn = nm$ by inserting $e = m^{-1}n^{-1}nm$.
- [ ] Q5 What does Q2–Q3 prove when $M \cap N$ is not assumed trivial? (Remark: Commutators of Normal Subgroups.)
- [ ] Q6 **[why]** Give two subgroups of $S_3$ with trivial intersection whose elements do not commute (the subgroups of Ex §41.2). Which hypothesis fails?
- [ ] Q7 **[why]** Drop $M \cap N = \{e\}$ but keep normality: take $M = N = G$ for a non-abelian $G$. What goes wrong in Q4?
- [ ] Q8 Combine with counting: if moreover $G$ is finite and $|M|\,|N| = |G|$, show $G \cong M \times N$ (Lem §51.6).

> [!tip]- Hints: definitions, results, strategy
> **Topic and definitions.**
> - Normal subgroup: [[§38 Normal Subgroups#^def-38-1|Def §38.1]]
> - Commutator: [[§47 Commutators#^def-47-1|Def §47.1]]
> - Conjugation: [[§18 Conjugation, Products, and Pointwise Products#^def-18-2|Def §18.2]]
>
> **Key results.** [[§47 Commutators#^prop-47-8|Prop §47.8]] (this problem); [[§47 Commutators#^rem-47-4|Remark: Commutators of Normal Subgroups]]; reused in the internal direct product criterion [[§54 p-Groups and Sylow Subgroups#^lem-54-6|Lem §54.6]] (second sufficient condition); the counterexample subgroups of [[§41 The First and Second Isomorphism Theorems#^ex-41-2|Ex §41.2]].
>
> **Strategy (G6, G8).** The commutator $x = mnm^{-1}n^{-1}$ lies in $N$ (group as $(mnm^{-1})\,n^{-1}$) and in $M$ (group as $m\,(nm^{-1}n^{-1})$), hence is $e$.
>
> **Difficulty 1.** Submitted solution: the two groupings of $x$, then $mn = (mnm^{-1}n^{-1})\,nm = nm$; identical to the proof of Prop §47.8.

### PS4.3 A normal subgroup inside a finite-index subgroup

Let $G$ be a group and $H$ a subgroup of $G$ with $[G : H] = n$. Show that there is a normal subgroup $N$ of $G$ with $N \subseteq H \subseteq G$ and $[G : N] \leq n!$. Hint: make a homomorphism $G \to S_n$ and think about the kernel.

^ps4-3

- [ ] Q1 **[def]** Define the index $[G : H]$ and the coset space $G/H$. Why is $G/H$ not a group in general?
- [ ] Q2 Show $g \cdot (xH) = (gx)H$ is well defined and satisfies the two action axioms.
- [ ] Q3 State and prove: an action of $G$ on $X$ gives a homomorphism $G \to S_X$ (Thm §25.3). Why does relabelling give $S_{G/H} \cong S_n$?
- [ ] Q4 **[def]** Define the kernel of an action. Why is $N = \ker\varphi$ normal in $G$?
- [ ] Q5 Show $N \subseteq H$ by looking at the coset $eH$. Describe $N$ as the intersection of the stabilizers $xHx^{-1}$ (Prop §39.6).
- [ ] Q6 Show $\bar\varphi : G/N \to S_{G/H}$, $gN \mapsto \varphi(g)$, is well defined and injective; conclude $[G : N] \leq n!$.
- [ ] Q7 Strengthen to "$[G : N]$ divides $n!$" using the First Isomorphism Theorem and Lagrange.
- [ ] Q8 **[why]** Where is finiteness of $[G : H]$ used? Is finiteness of $G$ needed?
- [ ] Q9 **[why]** Compute $N$ for $H = \{e, (1\,2)\} \leq S_3$. Why can one not simply take $N = H$?

> [!tip]- Hints: definitions, results, strategy
> **Topic and definitions.**
> - Index: [[§29 The Index and Lagrange's Theorem#^def-29-1|Def §29.1]]; left cosets [[§28 Left and Right Cosets#^def-28-2|Def §28.2]]
> - Action: [[§25 Actions#^def-25-1|Def §25.1]]; kernel of an action [[§25 Actions#^def-25-4|Def §25.4]]
> - Symmetric group $S_X$: [[§3 Basic Examples of Groups#^def-3-5|Def §3.5]]; kernel [[§15 Homomorphisms#^def-15-3|Def §15.3]]
> - Normal subgroup: [[§38 Normal Subgroups#^def-38-1|Def §38.1]]
>
> **Key results.** [[§39 Sources of Normal Subgroups#^thm-39-5|Thm §39.5]] (this problem; also PS 3.2). Used: the action on $G/H$ [[§31 G Acting on Coset Spaces#^prop-31-1|Prop §31.1]], actions are homomorphisms to $S_X$ [[§25 Actions#^thm-25-3|Thm §25.3]], kernels are normal [[§39 Sources of Normal Subgroups#^prop-39-2|Prop §39.2]]. Refinements: normal core [[§39 Sources of Normal Subgroups#^prop-39-6|Prop §39.6]], First Isomorphism Theorem [[§41 The First and Second Isomorphism Theorems#^thm-41-1|Thm §41.1]], Lagrange [[§29 The Index and Lagrange's Theorem#^thm-29-2|Thm §29.2]].
>
> **Strategy (G11, G5, G2).** Left multiplication on the $n$ cosets gives $\varphi : G \to S_{G/H} \cong S_n$; $N = \ker\varphi$ is normal, lies in $H$ (it fixes the coset $eH$), and $gN \mapsto \varphi(g)$ embeds $G/N$ in $S_n$.
>
> **Difficulty 2.** Submitted solution: verifies that the coset action is well defined, gets $\varphi$ from the lemma of PS 3.1(a), checks normality of the kernel by hand, proves $N \subseteq H$ via $eH$, and injects $G/N$ into $S_{G/H}$; remarks that $G$ need not be finite. It is the proof of Thm §39.5.

### PS4.4 The commutator subgroup and the abelianization

*Parts: (1), (2).*

^ps4-4

#### (1)

Define $D(G) = \langle ghg^{-1}h^{-1} : g, h \in G \rangle$, the subgroup generated by all commutators. Show that $D(G)$ is normal in $G$.

^ps4-4-1

- [ ] Q1 **[def]** Define $D(G)$. Why is it defined as a generated subgroup rather than as the set of commutators (Ex §47.2)?
- [ ] Q2 Describe the elements of $\langle S \rangle$ as words in $S \cup S^{-1}$. Show the inverse of a commutator is a commutator, so each $d \in D(G)$ is a product $c_1 \cdots c_k$ of commutators.
- [ ] Q3 Show $f(ghg^{-1}h^{-1})f^{-1} = \tilde g\,\tilde h\,\tilde g^{-1}\tilde h^{-1}$ with $\tilde g = fgf^{-1}$, $\tilde h = fhf^{-1}$.
- [ ] Q4 Using that conjugation by $f$ is a homomorphism (Prop §18.1), conclude $fdf^{-1} \in D(G)$.
- [ ] Q5 State the general principle behind Q2–Q4: if $fSf^{-1} \subseteq S$ for all $f \in G$, then $\langle S \rangle \trianglelefteq G$.
- [ ] Q6 **[why]** Take $S = \{(1\,2)\}$ in $S_3$. Which step of the argument fails, and is $\langle S \rangle$ normal?

> [!tip]- Hint (1): strategy
> **Strategy (G6, G7).** Check normality on generators: conjugation by $f$ is a homomorphism and carries commutators to commutators.

#### (2)

Let $G^{\mathrm{ab}} = G/D(G)$, the abelianization of $G$. Show that $G^{\mathrm{ab}}$ is abelian.

^ps4-4-2

- [ ] Q1 **[def]** Define the quotient group $G/N$ and its multiplication. Why does part (1) make $G^{\mathrm{ab}}$ a group (Thm §40.1)?
- [ ] Q2 Reduce the claim to $(ab)D = (ba)D$ for all $a, b \in G$.
- [ ] Q3 State and prove the coset criterion: $xD = yD$ if and only if $x^{-1}y \in D$.
- [ ] Q4 Show $(ab)^{-1}(ba) = b^{-1}a^{-1}ba$ is a commutator. Of which pair?
- [ ] Q5 Conclude, and give the one-line version via $(aD)(bD)(aD)^{-1}(bD)^{-1} = aba^{-1}b^{-1}D$.
- [ ] Q6 Prove the converse (Prop §47.11): if $N \trianglelefteq G$ and $G/N$ is abelian, then $D(G) \subseteq N$. So $G^{\mathrm{ab}}$ is the largest abelian quotient.
- [ ] Q7 **[why]** Is $G/N$ abelian for a normal subgroup $N$ strictly smaller than $D(G)$? Test $G = S_3$, $N = \{e\}$, and compute $D(S_3)$ and $S_n^{\mathrm{ab}}$ (Ex §47.1).

> [!tip]- Hint (2): strategy
> **Strategy (G8, G2).** In $G/D$, $(aD)(bD)(aD)^{-1}(bD)^{-1} = aba^{-1}b^{-1}D = D$; equivalently $(ab)^{-1}(ba)$ is a commutator, so $(ab)D = (ba)D$.

> [!tip]- Hints: definitions and results for the whole problem
> **Topic and definitions.**
> - Commutator: [[§47 Commutators#^def-47-1|Def §47.1]]; commutator subgroup $D(G)$ [[§47 Commutators#^def-47-2|Def §47.2]]
> - Subgroup generated by a set, words: [[§4 Subgroups#^def-4-4|Def §4.4]], [[§4 Subgroups#^def-4-5|Def §4.5]]; top-down description [[§4 Subgroups#^prop-4-7|Prop §4.7]]
> - Normal subgroup [[§38 Normal Subgroups#^def-38-1|Def §38.1]]; quotient group [[§40 Quotient Groups#^def-40-1|Def §40.1]]; abelianization [[§47 Commutators#^def-47-3|Def §47.3]]
> - Congruence modulo a subgroup: [[§28 Left and Right Cosets#^def-28-1|Def §28.1]]
>
> **Key results.** (1) is [[§47 Commutators#^prop-47-4|Prop §47.4]](1); (2) is [[§47 Commutators#^prop-47-6|Prop §47.6]] (second proof). Used: conjugation is an automorphism [[§18 Conjugation, Products, and Pointwise Products#^prop-18-1|Prop §18.1]], $G/N$ is a group [[§40 Quotient Groups#^thm-40-1|Thm §40.1]], cosets as equivalence classes [[§28 Left and Right Cosets#^prop-28-2|Prop §28.2]]. Related: [[§47 Commutators#^prop-47-11|Prop §47.11]], [[§47 Commutators#^rem-47-7|Remark: Smallest Normal Subgroup with Abelian Quotient]], [[§47 Commutators#^ex-47-1|Ex §47.1]], [[§47 Commutators#^ex-47-2|Ex §47.2]].
>
> **Difficulty 1.** Submitted solution: (1) inverse of a commutator is a commutator, conjugate of a commutator is a commutator, then conjugate a product factor by factor; (2) proves $(ba)D \subseteq (ab)D$ by an explicit element computation and swaps roles, then gives an alternative proof via the coset criterion. The alternative is the notes' second proof of Prop §47.6; part (1) is the proof of Prop §47.4(1).

### PS4.5 Characters of the symmetric group

*Parts: (1), (2), (3).*

^ps4-5

#### (1)

Let $\chi : S_n \to A$ be a character ($A$ abelian) and $a = \chi((1\,2))$. Show that $\chi((i\,j)) = a$ for any transposition $(i\,j) \in S_n$.

^ps4-5-1

- [ ] Q1 **[def]** Define a character. Show $\chi(e) = 1$ and $\chi(\sigma^{-1}) = \chi(\sigma)^{-1}$.
- [ ] Q2 Prove $\sigma\,(i\,j)\,\sigma^{-1} = (\sigma(i)\ \sigma(j))$ by tracking every point (Lem §33.1).
- [ ] Q3 Construct $\sigma \in S_n$ with $\sigma(i) = 1$, $\sigma(j) = 2$. Why is it a bijection?
- [ ] Q4 Show $\chi(\sigma(i\,j)\sigma^{-1}) = \chi((i\,j))$, and name the step that uses that $A$ is abelian.
- [ ] Q5 **[why]** The identity map $S_3 \to S_3$ is a homomorphism to a non-abelian group. Does it take the same value on $(1\,2)$ and $(1\,3)$? Which step of Q4 fails?

> [!tip]- Hint (1): strategy
> **Strategy (G6).** Conjugate $(i\,j)$ to $(1\,2)$; a character, having abelian target, is constant on conjugacy classes.

#### (2)

Show that $a^2 = 1$.

^ps4-5-2

- [ ] Q1 **[def]** Define the order of an element. What does $a^2 = 1$ say about the order of $a$ in $A$?
- [ ] Q2 Show $(1\,2)^2 = e$ and conclude $a^2 = \chi(e) = 1$.
- [ ] Q3 More generally, if $g$ has order $k$, show $\chi(g)^k = 1$.
- [ ] Q4 **[why]** Can $a = 1$ occur? Can $a \neq 1$? Give a character for each case.
- [ ] Q5 Conversely, for each $a \in A$ with $a^2 = 1$, why is there a character with $\chi((1\,2)) = a$ (Cor §47.7)?

> [!tip]- Hint (2): strategy
> **Strategy (G8).** $(1\,2)^2 = e$ and homomorphisms preserve products and the identity.

#### (3)

Show that for any $\sigma \in S_n$, $\chi(\sigma) = 1$ if $\sigma \in A_n$ and $\chi(\sigma) = a$ if $\sigma \notin A_n$. (So every character of $S_n$ is either trivial or "the sign in disguise".)

^ps4-5-3

- [ ] Q1 **[def]** Define $\operatorname{sgn}$ and $A_n$.
- [ ] Q2 State the generating set used: every $\sigma$ is a product of transpositions $(1\,j)$ (Thm §21.7).
- [ ] Q3 Show $\sigma \in A_n$ if and only if $k$ is even. Why is the parity of $k$ independent of the chosen factorization (Cor §21.4)?
- [ ] Q4 Compute $\chi(\sigma) = a^k$ and finish using $a^2 = 1$.
- [ ] Q5 Second route (Thm §47.5): show $D(S_n) = A_n$ and use that every character kills $D(S_n)$.
- [ ] Q6 **[why]** Where is $n \geq 2$ needed? What happens for $n = 1$?
- [ ] Q7 Conclude that $S_n$ ($n \geq 2$) has exactly two characters with values in $\mathbb{C}^\times$ (Remark: The Characters of Sn, Completely).

> [!tip]- Hint (3): strategy
> **Strategy (G7, G8).** Write $\sigma = t_1 \cdots t_k$ with transpositions $t_i = (1\,j_i)$; then $\chi(\sigma) = a^k$ and $\operatorname{sgn}(\sigma) = (-1)^k$.

> [!tip]- Hints: definitions and results for the whole problem
> **Topic and definitions.**
> - Character: [[§46 Characters#^def-46-1|Def §46.1]]
> - Cycle notation, transpositions: [[§10 Cycle Notation and the Group S₃#^def-10-2|Def §10.2]]; conjugate elements [[§18 Conjugation, Products, and Pointwise Products#^def-18-3|Def §18.3]]
> - Sign, even and odd permutations: [[§21 The Sign Homomorphism and the Alternating Group#^def-21-2|Def §21.2]]; alternating group [[§21 The Sign Homomorphism and the Alternating Group#^def-21-3|Def §21.3]]
>
> **Key results.** [[§47 Commutators#^thm-47-5|Thm §47.5]] (this problem: its "direct proof" paragraph). Used: conjugation relabels entries [[§33 Conjugacy Classes#^lem-33-1|Lem §33.1]], generators of $S_n$ [[§21 The Sign Homomorphism and the Alternating Group#^thm-21-7|Thm §21.7]], the sign is a homomorphism [[§21 The Sign Homomorphism and the Alternating Group#^thm-21-3|Thm §21.3]], parity [[§21 The Sign Homomorphism and the Alternating Group#^cor-21-4|Cor §21.4]]. Related: characters are constant on conjugacy classes [[§46 Characters#^prop-46-1|Prop §46.1]], [[§46 Characters#^rem-46-3|Remark: Where Commutativity Is Needed]], class of $(1\,2)$ [[§33 Conjugacy Classes#^prop-33-2|Prop §33.2]], converse [[§47 Commutators#^cor-47-7|Cor §47.7]], [[§47 Commutators#^rem-47-3|Remark: The Characters of Sn, Completely]].
>
> **Difficulty 1.** Submitted solution: proves the relabelling lemma for transpositions, builds $\sigma$ with $\sigma(i) = 1$, $\sigma(j) = 2$ explicitly, and for (3) uses the $(1\,j)$ generators and $\operatorname{sgn}(t_i) = -1$ from PS 1.5; treats $n = 1$ separately. This is the "direct proof" paragraph of Thm §47.5.
>
> ---
>
> ## Problem Set 5 (due 10/8)

### PS5.1 The index of an intersection

*Parts: (1), (2).*

^ps5-1

#### (1)

Let $G$ be a group, $H$ a subgroup with $G/H$ finite, $A$ a subgroup of $G$ and $B = A \cap H$. Show that $[A : B] \leq [G : H]$. Hint: consider the action of $B$ on $G/H$.

^ps5-1-1

- [ ] Q1 **[def]** Define $[A : B]$ and $A/B$. What does "$G/H$ finite" mean when $G$ is infinite?
- [ ] Q2 Show $aB \mapsto aH$ is well defined. Where is $B \subseteq H$ used?
- [ ] Q3 Show it is injective. Where is $a'^{-1}a \in A$ used?
- [ ] Q4 Conclude that $A/B$ is finite and $[A : B] \leq [G : H]$.
- [ ] Q5 **[def]** Action route: let $A$ act on $G/H$ by left multiplication. What is the stabilizer of the coset $eH$?
- [ ] Q6 Apply orbit–stabilizer to the $A$-orbit of $eH$ and conclude again. When does equality hold?
- [ ] Q7 **[why]** If $G/H$ is infinite, which part of Q4 has no content? Does the injection of Q2–Q3 still exist?

> [!tip]- Hint (1): strategy
> **Strategy (G2, G4).** The map $aB \mapsto aH$ is well defined and injective; equivalently, $A$ acts on $G/H$, the stabilizer of the coset $eH$ is $A \cap H$, so its orbit has $[A : B]$ elements.

#### (2)

Prove or disprove: $[A : B]$ divides $[G : H]$.

^ps5-1-2

- [ ] Q1 Normal case first: if $H \trianglelefteq G$, show $[A : A \cap H]$ divides $[G : H]$ via $A/(A \cap H) \cong AH/H \leq G/H$ (Cor §41.8). So where must a counterexample look?
- [ ] Q2 With $H = \{e, (1\,2)\}$, $A = \{e, (1\,3)\}$ in $S_3$, compute $B$, $[A : B]$ and $[G : H]$.
- [ ] Q3 List the three left cosets of $H$ explicitly.
- [ ] Q4 Orbit picture: show the $A$-orbits on $G/H$ have sizes $2$ and $1$. Why do orbit sizes of a subgroup action not have to be equal?
- [ ] Q5 **[why]** Which hypothesis of Cor §41.8 fails here, and which step of its proof breaks (is $AH$ a subgroup? compare Ex §41.2)?

> [!tip]- Hint (2): strategy
> **Strategy (G10, G3).** False: in $S_3$ take $H = \{e, (1\,2)\}$ and $A = \{e, (1\,3)\}$; then $[A : B] = 2$ and $[G : H] = 3$.

> [!tip]- Hints: definitions and results for the whole problem
> **Topic and definitions.**
> - Index: [[§29 The Index and Lagrange's Theorem#^def-29-1|Def §29.1]]; left cosets [[§28 Left and Right Cosets#^def-28-2|Def §28.2]]
> - Action [[§25 Actions#^def-25-1|Def §25.1]]; stabilizer [[§26 Stabilizers and Fixed Points#^def-26-1|Def §26.1]]; orbit [[§27 Orbits#^def-27-1|Def §27.1]]
> - Well-defined map: [[§7 The Group ℤ∕nℤ#^def-7-2|Def §7.2]]
>
> **Key results.** (1) is [[§29 The Index and Lagrange's Theorem#^prop-29-9|Prop §29.9]]; (2) is [[§29 The Index and Lagrange's Theorem#^ex-29-2|Ex §29.2]]; the normal case [[§41 The First and Second Isomorphism Theorems#^cor-41-8|Cor §41.8]]. Used: the action on $G/H$ [[§31 G Acting on Coset Spaces#^prop-31-1|Prop §31.1]], orbit–stabilizer [[§30 Orbit–Stabilizer#^thm-30-3|Thm §30.3]], Lagrange [[§29 The Index and Lagrange's Theorem#^thm-29-2|Thm §29.2]], Second Isomorphism Theorem [[§41 The First and Second Isomorphism Theorems#^thm-41-5|Thm §41.5]].
>
> **Difficulty** (1) 1, (2) 1. Submitted solution: (1) proves the injection $aB \mapsto aH$ (well defined and injective) rather than using the hinted action; (2) the $S_3$ counterexample with the cosets $H$, $(1\,3)H$, $(2\,3)H$ listed. These are Prop §29.9 and Ex §29.2; Cor §41.8 (normal case) is an addition in the notes.

### PS5.2 Conjugacy in a normal subgroup

*Parts: (1), (2), (3).*

^ps5-2

#### (1)

Let $N \trianglelefteq G$, $g \in N$, $Z_G(g) = \{h \in G : gh = hg\}$. For $h \in G$ (so $g$ and $hgh^{-1}$ are both in $N$ and conjugate in $G$), show that $hgh^{-1}$ is conjugate to $g$ in $N$ if and only if $h \in Z_G(g)N$.

^ps5-2-1

- [ ] Q1 **[def]** Define $Z_G(g)$ and the set $Z_G(g)N$. Why is $Z_G(g)N$ a subgroup (Lem §41.3)?
- [ ] Q2 What does "conjugate in $N$" mean? Why do $g$ and $hgh^{-1}$ both lie in $N$?
- [ ] Q3 ($\Rightarrow$) From $hgh^{-1} = ngn^{-1}$ with $n \in N$, show $z = n^{-1}h \in Z_G(g)$.
- [ ] Q4 Rewrite $h = nz$ as $z\,(z^{-1}nz)$ and conclude $h \in Z_G(g)N$.
- [ ] Q5 ($\Leftarrow$) For $h = zn'$, show $hgh^{-1} = n''\,g\,n''^{-1}$ with $n'' = zn'z^{-1}$.
- [ ] Q6 For $[G : N] = 2$, deduce: the $G$-class of $g$ is a single $N$-class if and only if $Z_G(g) \not\subseteq N$; otherwise it splits into two classes of equal size (Ex §44.1).
- [ ] Q7 **[why]** Point to the step in each direction that uses normality of $N$.

> [!tip]- Hint (1): strategy
> **Strategy (G6).** ($\Rightarrow$) $z = n^{-1}h$ centralizes $g$, then $h = z\,(z^{-1}nz)$; ($\Leftarrow$) for $h = zn'$, the element $zn'z^{-1} \in N$ conjugates $g$ to $hgh^{-1}$.

#### (2)

Use this criterion to show that $(1\,2\,3)$ and $(1\,3\,2)$ are conjugate in $A_5$, but $(1\,2\,3\,4\,5)$ and $(1\,2\,3\,5\,4)$ are not conjugate in $A_5$.

^ps5-2-2

- [ ] Q1 **[def]** State "conjugation relabels a cycle" (Lem §33.1). Why are 3-cycles and 5-cycles even?
- [ ] Q2 Find $h \in S_5$ with $h(1\,2\,3)h^{-1} = (1\,3\,2)$.
- [ ] Q3 Show $(4\,5) \in Z_{S_5}((1\,2\,3))$, write $h \in Z_{S_5}(g)A_5$, and extract an explicit conjugator in $A_5$.
- [ ] Q4 Show $Z_{S_5}((1\,2\,3\,4\,5)) = \langle (1\,2\,3\,4\,5) \rangle$ via $h(k+1) = h(k) + 1 \pmod 5$. Cross-check with orbit–stabilizer and the class size $24$.
- [ ] Q5 Conclude $Z_{S_5}(g)A_5 = A_5$; find the odd $h$ with $hgh^{-1} = (1\,2\,3\,5\,4)$ and finish.
- [ ] Q6 **[why]** In $A_4$ the 3-cycles $(1\,2\,3)$ and $(1\,3\,2)$ are not conjugate (Ex §43.1). Which step of Q3 fails for $n = 4$?
- [ ] Q7 Use the criterion to find the sizes of the $A_5$-classes of 3-cycles and of 5-cycles (Ex §44.1).

> [!tip]- Hint (2): strategy
> **Strategy (G10, G6).** $G = S_5$, $N = A_5$: the 3-cycle has an odd centralizing element $(4\,5)$; the 5-cycle has centralizer $\langle (1\,2\,3\,4\,5) \rangle \subseteq A_5$, so only even conjugators work.

#### (3)

Show that $\begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$ and $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ are conjugate in $GL_2(\mathbb{R})$ but not in $SL_2(\mathbb{R})$.

^ps5-2-3

- [ ] Q1 **[def]** Define $SL_2(\mathbb{R})$. Why is it normal in $GL_2(\mathbb{R})$?
- [ ] Q2 Find $h$ with $\det h = -1$ and $hAh^{-1} = B$.
- [ ] Q3 Solve $zA = Az$ entrywise to compute $Z_{GL_2(\mathbb{R})}(A)$.
- [ ] Q4 Show every element of $Z_{GL_2(\mathbb{R})}(A)\,SL_2(\mathbb{R})$ has positive determinant, and conclude.
- [ ] Q5 Interpret geometrically: $A$ and $B$ are rotations by $\mp 90^\circ$, and $h$ is a reflection.
- [ ] Q6 **[why]** Which step uses that the field is $\mathbb{R}$? Test over $\mathbb{C}$: does $\operatorname{diag}(i, -i) \in SL_2(\mathbb{C})$ conjugate $A$ to $B$?

> [!tip]- Hint (3): strategy
> **Strategy (G10, G6).** Conjugate by $h = \operatorname{diag}(-1, 1)$, of determinant $-1$; the centralizer $\{\begin{pmatrix} a & -b \\ b & a \end{pmatrix}\}$ has positive determinants, so $h \notin Z(A)\,SL_2(\mathbb{R})$.

> [!tip]- Hints: definitions and results for the whole problem
> **Topic and definitions.**
> - Centralizer $Z_G(g) = C_G(g)$: [[§34 Conjugation as an Action and the Class Equation#^def-34-1|Def §34.1]]
> - Conjugate elements [[§18 Conjugation, Products, and Pointwise Products#^def-18-3|Def §18.3]]; conjugacy class [[§33 Conjugacy Classes#^def-33-1|Def §33.1]]
> - Normal subgroup [[§38 Normal Subgroups#^def-38-1|Def §38.1]]; product set [[§41 The First and Second Isomorphism Theorems#^def-41-1|Def §41.1]]
> - $A_n$ [[§21 The Sign Homomorphism and the Alternating Group#^def-21-3|Def §21.3]]; $GL_n$ [[§3 Basic Examples of Groups#^def-3-6|Def §3.6]]; $SL_n$ [[§3 Basic Examples of Groups#^def-3-7|Def §3.7]]
>
> **Key results.** (1) is [[§44 Conjugacy in a Normal Subgroup#^prop-44-1|Prop §44.1]]; (2) is [[§44 Conjugacy in a Normal Subgroup#^prop-44-2|Prop §44.2]]; (3) is [[§44 Conjugacy in a Normal Subgroup#^ex-44-2|Ex §44.2]]. Used: conjugation relabels entries [[§33 Conjugacy Classes#^lem-33-1|Lem §33.1]], classes in $S_n$ are cycle types [[§33 Conjugacy Classes#^thm-33-3|Thm §33.3]], $HN$ is a subgroup [[§41 The First and Second Isomorphism Theorems#^lem-41-3|Lem §41.3]]. Related: the classes of $A_5$ [[§44 Conjugacy in a Normal Subgroup#^ex-44-1|Ex §44.1]], the $A_4$ contrast [[§43 Simple Groups#^ex-43-1|Ex §43.1]], 3-cycles conjugate in $A_n$ [[§43 Simple Groups#^lem-43-8|Lem §43.8]].
>
> **Difficulty** (1) 2, (2) 2, (3) 2. Submitted solution: (1) both directions by direct manipulation, as in Prop §44.1; (2) proves the general relabelling rule and the parity of a 5-cycle, uses $z = (4\,5)$ and $n' = (4\,5)(1\,2)$, computes the 5-cycle centralizer by the mod-5 argument, and uses $h = (4\,5)$; (3) $h = \operatorname{diag}(-1, 1)$, explicit centralizer, determinant argument. The notes reproduce all three (Prop §44.1, Prop §44.2, Ex §44.2) and add Ex §44.1.

### PS5.3 Characters of the alternating group

*Parts: (1), (2), (3).*

^ps5-3

#### (1)

Let $n \geq 5$ and $\psi : A_n \to A$ a character. For any 3-cycle $(i\,j\,k)$, show that $(i\,j\,k)$ is a commutator in $A_n$ (this needs $n \geq 5$).

^ps5-3-1

- [ ] Q1 **[def]** Define a commutator in a group $H$. Why does "commutator in $A_n$" require $g_1, g_2 \in A_n$?
- [ ] Q2 Verify $(i\,j\,k) = (j\,k)(i\,j)(j\,k)(i\,j)$ (Prop §47.2). Why does this not yet prove (1)?
- [ ] Q3 Using $n \geq 5$, choose $l, m$; show $g_1 = (l\,m)(j\,k)$ and $g_2 = (l\,m)(i\,j)$ are even and self-inverse.
- [ ] Q4 Compute $g_1g_2g_1^{-1}g_2^{-1}$, moving the four factors $(l\,m)$ to the front.
- [ ] Q5 **[why]** For $n = 4$: is $(1\,2\,3)$ a commutator in $A_4$? (Use the character $A_4 \to A_3$ of Remark: Small n and Simplicity.)

> [!tip]- Hint (1): strategy
> **Strategy (G10, G8).** Make the $S_n$ identity $(i\,j\,k) = (j\,k)(i\,j)(j\,k)(i\,j)$ even by multiplying both transpositions by a disjoint transposition $(l\,m)$.

#### (2)

Show that $\psi((i\,j\,k)) = 1$.

^ps5-3-2

- [ ] Q1 **[def]** Define a character, and state which property of the target the argument needs.
- [ ] Q2 Prove that $\chi(g_1g_2g_1^{-1}g_2^{-1}) = 1$ for any character $\chi$ (Prop §47.1). Where is commutativity used?
- [ ] Q3 Conclude $\psi((i\,j\,k)) = 1$ from (1).
- [ ] Q4 **[why]** Why does the same argument not show that $\operatorname{sgn}$ kills transpositions in $S_n$ (Prop §47.3)?

> [!tip]- Hint (2): strategy
> **Strategy (G8).** Characters kill commutators, since the target is abelian.

#### (3)

Show that $\psi(\sigma) = 1$ for all $\sigma \in A_n$.

^ps5-3-3

- [ ] Q1 **[def]** State the generating set used: $A_n$ is generated by the 3-cycles $(1\,2\,j)$ (Thm §21.9). Why is the inverse of a 3-cycle a 3-cycle?
- [ ] Q2 Write $\sigma = t_1 \cdots t_k$ and conclude $\psi(\sigma) = 1$ (including $k = 0$).
- [ ] Q3 Deduce $D(A_n) = A_n$ for $n \geq 5$.
- [ ] Q4 Second proof via simplicity (Thm §43.9): why is $\ker\psi$ normal, and why can it not be $\{e\}$?
- [ ] Q5 **[why]** Give nontrivial characters of $A_3$ and of $A_4$. Which step of the proof fails for $n = 3, 4$?

> [!tip]- Hint (3): strategy
> **Strategy (G7).** A homomorphism trivial on a generating set is trivial; $A_n$ is generated by 3-cycles.

> [!tip]- Hints: definitions and results for the whole problem
> **Topic and definitions.**
> - Character: [[§46 Characters#^def-46-1|Def §46.1]]; commutator [[§47 Commutators#^def-47-1|Def §47.1]]
> - $A_n$: [[§21 The Sign Homomorphism and the Alternating Group#^def-21-3|Def §21.3]]; disjoint cycles [[§11 Disjoint Cycle Decomposition#^def-11-1|Def §11.1]]
>
> **Key results.** (1) is [[§47 Commutators#^lem-47-9|Lem §47.9]]; (2)–(3) are [[§47 Commutators#^thm-47-10|Thm §47.10]]. Used: characters kill commutators [[§47 Commutators#^prop-47-1|Prop §47.1]], 3-cycles are commutators in $S_n$ [[§47 Commutators#^prop-47-2|Prop §47.2]], disjoint cycles commute [[§11 Disjoint Cycle Decomposition#^lem-11-2|Lem §11.2]], generators of $A_n$ [[§21 The Sign Homomorphism and the Alternating Group#^thm-21-9|Thm §21.9]]. Related: [[§47 Commutators#^rem-47-5|Remark: Small n and Simplicity]], transpositions are not commutators [[§47 Commutators#^prop-47-3|Prop §47.3]], $A_n$ simple [[§43 Simple Groups#^thm-43-9|Thm §43.9]], the pair-partition homomorphism [[§43 Simple Groups#^prop-43-10|Prop §43.10]].
>
> **Difficulty** (1) 2, (2) 1, (3) 1. Submitted solution: (1) cites PS 2.4(c) for $(i\,j\,k) = (j\,k)(i\,j)(j\,k)(i\,j)$ and uses $g_1 = (l\,m)(j\,k)$, $g_2 = (l\,m)(i\,j)$; (2) cites PS 2.4(b) applied to $A_n$; (3) uses the generators $(1\,2\,j)$ from PS 1.5. Integrated as Lem §47.9 and Thm §47.10.

### PS5.4 Elements of D(G) that are not commutators

*Parts: (1), (2), (3).*

^ps5-4

#### (1)

Let $p, q, r \geq 1$ and $G$ the group of real block matrices $T(A, B, C) = \begin{bmatrix} I_p & A & C \\ 0 & I_q & B \\ 0 & 0 & I_r \end{bmatrix}$ ($A$ is $p \times q$, $B$ is $q \times r$, $C$ is $p \times r$). Check that $T(A, B, C)^{-1} = T(-A, -B, AB - C)$ and that $T(A, B, C)\,T(X, Y, Z)\,T(A, B, C)^{-1}\,T(X, Y, Z)^{-1} = T(0, 0, AY - XB)$.

^ps5-4-1

- [ ] Q1 **[def]** Why is $G$ a subgroup of $GL_{p+q+r}(\mathbb{R})$?
- [ ] Q2 State the block multiplication rule and compute the product formula block by block.
- [ ] Q3 Verify that $T(-A, -B, AB - C)$ is a two-sided inverse.
- [ ] Q4 Compute $gk$, then $gkg^{-1}$, then $gkg^{-1}k^{-1}$ for $g = T(A, B, C)$, $k = T(X, Y, Z)$.
- [ ] Q5 **[why]** The $(1,3)$ block is not additive. Find $g, k$ with $AY \neq XB$, so $G$ is non-abelian. What happens to the formula if $q = 0$?

> [!tip]- Hint (1): strategy
> **Strategy (G10).** Block multiplication gives $T(A, B, C)\,T(X, Y, Z) = T(A + X,\ B + Y,\ C + Z + AY)$; everything follows from this one formula.

#### (2)

Show that $D(G)$ is the group of matrices $T(0, 0, M)$.

^ps5-4-2

- [ ] Q1 **[def]** Describe $D(G)$ as the smallest subgroup containing all commutators (Prop §4.7).
- [ ] Q2 Show $S$ is a subgroup, with $T(0, 0, M)\,T(0, 0, N) = T(0, 0, M + N)$.
- [ ] Q3 Conclude $D(G) \subseteq S$.
- [ ] Q4 Find $A$ ($p \times q$) and $Y$ ($q \times r$) with $AY = \lambda E_{st}$, and write $T(0, 0, \lambda E_{st})$ as a commutator.
- [ ] Q5 Write $T(0, 0, M)$ as a product of such elements and conclude $S \subseteq D(G)$.
- [ ] Q6 **[why]** Where is $q \geq 1$ used in Q4?

> [!tip]- Hint (2): strategy
> **Strategy (G1, G8).** ($\subseteq$) $S = \{T(0, 0, M)\}$ is a subgroup containing all commutators; ($\supseteq$) each $T(0, 0, \lambda E_{st})$ is a commutator and they generate $S$.

#### (3)

Show that if $T(0, 0, M)$ is a commutator then $\operatorname{rank}(M) \leq 2q$. In particular, if $p, r > 2q$ (e.g. $(p, q, r) = (3, 1, 3)$), then there are matrices in $D(G)$ which are not commutators.

^ps5-4-3

- [ ] Q1 **[def]** Define the rank of a matrix. Show $\operatorname{rank}(PQ) \leq q$ for $P$ of size $p \times q$ and $Q$ of size $q \times r$.
- [ ] Q2 Show $\operatorname{rank}(P_1 - P_2) \leq \operatorname{rank} P_1 + \operatorname{rank} P_2$.
- [ ] Q3 Conclude $\operatorname{rank} M \leq 2q$ for every commutator $T(0, 0, M)$.
- [ ] Q4 For $p, r > 2q$, build $M$ of rank $2q + 1$ and conclude $T(0, 0, M) \in D(G)$ is not a commutator. Make it explicit for $(3, 1, 3)$.
- [ ] Q5 **[why]** Why does the rank bound give nothing when $p \leq 2q$ or $r \leq 2q$?
- [ ] Q6 For $(p, q, r) = (3, 1, 3)$, show $T(0, 0, I_3)$ is a product of two commutators.

> [!tip]- Hint (3): strategy
> **Strategy (G10, G8).** A commutator has $M = AY - XB$ with both products factoring through $\mathbb{R}^q$, so $\operatorname{rank} M \leq q + q$.

> [!tip]- Hints: definitions and results for the whole problem
> **Topic and definitions.**
> - Commutator [[§47 Commutators#^def-47-1|Def §47.1]]; commutator subgroup [[§47 Commutators#^def-47-2|Def §47.2]]
> - Subgroup generated by a set [[§4 Subgroups#^def-4-5|Def §4.5]]; top-down description [[§4 Subgroups#^prop-4-7|Prop §4.7]]; subgroup criteria [[§4 Subgroups#^prop-4-2|Prop §4.2]]
> - $GL_n(\mathbb{R})$: [[§3 Basic Examples of Groups#^def-3-6|Def §3.6]]
>
> **Key results.** [[§47 Commutators#^ex-47-2|Ex §47.2]] (this problem); [[§47 Commutators#^prop-47-4|Prop §47.4]].
>
> **Difficulty** (1) 1, (2) 2, (3) 2. Submitted solution: introduces $T(A, B, C)$ and derives everything from the product formula; (2) uses a row of ones in $A'$ and a column of ones in $Y$, rescaled by $\lambda/q$; (3) proves the two rank inequalities and uses $M$ with $I_{2q+1}$ in the corner. Ex §47.2 is the condensed version.
>
> ---
>
> ## Problem Set 6 (due 10/15)

### PS6.1 Normality is not transitive

Let $G_3 = S_4$ and $G_2 = K = \{e, (1\,2)(3\,4), (1\,3)(2\,4), (1\,4)(2\,3)\} \subset S_4$, the Klein four-group. Give an example of a subgroup $G_1$ of $K$ which is normal in $K$ but not normal in $S_4$; so $G_1 \trianglelefteq G_2 \trianglelefteq G_3$ but $G_1$ is not normal in $G_3$.

^ps6-1

- [ ] Q1 **[def]** Define "$G_1$ is normal in $G_2$". Write out the elements of $K$.
- [ ] Q2 Show $G_1 = \{e, (1\,2)(3\,4)\}$ is a subgroup of $K$ (why does $(1\,2)(3\,4)$ square to $e$?).
- [ ] Q3 Show $G_1 \trianglelefteq K$ in one line (Prop §39.8, Prop §38.1), and again by relabelling with each element of $K$.
- [ ] Q4 Why is $K \trianglelefteq S_4$? (Union of conjugacy classes, Ex §39.3.)
- [ ] Q5 Conjugate $(1\,2)(3\,4)$ by $(1\,2\,3\,4)$ using the relabelling rule, and conclude.
- [ ] Q6 Show that none of the three subgroups of order $2$ of $K$ is normal in $S_4$ (single cycle type class, Prop §39.7).
- [ ] Q7 **[why]** The other direction does hold: if $G_1 \trianglelefteq G_3$ and $G_1 \subseteq G_2 \leq G_3$, show $G_1 \trianglelefteq G_2$. What would one need to pass normality from $G_2$ up to $G_3$, and why does conjugation by $G_3$ not preserve $G_1$ here?

> [!tip]- Hints: definitions, results, strategy
> **Topic and definitions.**
> - Normal subgroup: [[§38 Normal Subgroups#^def-38-1|Def §38.1]]
> - Klein four-group: [[§39 Sources of Normal Subgroups#^def-39-1|Def §39.1]]
> - Conjugacy class [[§33 Conjugacy Classes#^def-33-1|Def §33.1]]; cycle type [[§33 Conjugacy Classes#^def-33-2|Def §33.2]]
>
> **Key results.** [[§39 Sources of Normal Subgroups#^ex-39-4|Ex §39.4]] (this problem). Used: $K$ is an abelian subgroup [[§39 Sources of Normal Subgroups#^prop-39-8|Prop §39.8]], subgroups of abelian groups are normal [[§38 Normal Subgroups#^prop-38-1|Prop §38.1]], conjugation relabels a cycle [[§12 Multiplying and Conjugating Cycles#^prop-12-1|Prop §12.1]], $K \trianglelefteq S_4$ via [[§39 Sources of Normal Subgroups#^ex-39-3|Ex §39.3]], normal subgroups are unions of classes [[§39 Sources of Normal Subgroups#^prop-39-7|Prop §39.7]], classes in $S_n$ are cycle types [[§33 Conjugacy Classes#^thm-33-3|Thm §33.3]].
>
> **Strategy (G10, G6, G13).** $G_1 = \{e, (1\,2)(3\,4)\}$ is normal in the abelian group $K$, but conjugating by $(1\,2\,3\,4)$ relabels $(1\,2)(3\,4)$ to $(1\,4)(2\,3) \notin G_1$.
>
> **Difficulty 1.** Submitted solution: $G_1 = \{e, (1\,2)(3\,4)\}$; normality in $K$ checked by relabelling for all four elements of $K$; non-normality via $\sigma = (1\,2\,3\,4)$. The submission takes $K \trianglelefteq S_4$ from the statement without proof; Ex §39.4 adds the one-line "$K$ abelian" argument and cites Ex §39.3 for $K \trianglelefteq S_4$.

### PS6.2 Simple abelian groups

*Parts: (1), (2), (3), (4).*

^ps6-2

#### (1)

Let $A$ be a non-trivial abelian group. Show that every subgroup of $A$ is normal.

^ps6-2-1

- [ ] Q1 **[def]** Define a normal subgroup and a simple group.
- [ ] Q2 For $B \leq A$, $a \in A$, $b \in B$, show $aba^{-1} = b$.
- [ ] Q3 Deduce: an abelian $A$ is simple if and only if its only subgroups are $\{e\}$ and $A$ (and $A \neq \{e\}$).
- [ ] Q4 **[why]** Without commutativity: give a subgroup of $S_3$ that is not normal (Ex §38.1). Which line of Q2 fails?

> [!tip]- Hint (1): strategy
> **Strategy (G13).** In an abelian group $aba^{-1} = b$.

#### (2)

Let $g \in A$, $g \neq e$. If $\langle g \rangle g \neq A$, show that $A$ is not simple.

^ps6-2-2

- [ ] Q1 **[def]** Define $\langle g \rangle$. Show $\langle g \rangle g = \langle g \rangle$, so the hypothesis says $\langle g \rangle \neq A$.
- [ ] Q2 Why is $\langle g \rangle$ nontrivial?
- [ ] Q3 Conclude that $\langle g \rangle$ is a proper nontrivial normal subgroup. (The submission argues the contrapositive; set it up.)
- [ ] Q4 **[why]** Where is $g \neq e$ used? What does the hypothesis become if $g = e$?

> [!tip]- Hint (2): strategy
> **Strategy (G13).** $\langle g \rangle g = \langle g \rangle$, a nontrivial subgroup, normal by (1); if it is proper, $A$ is not simple.

#### (3)

If the order of $g$ is infinite, show that $A$ is not simple.

^ps6-2-3

- [ ] Q1 **[def]** Define "infinite order".
- [ ] Q2 Show $H = \langle g^2 \rangle \neq \{e\}$.
- [ ] Q3 Show $g \notin H$: from $g = g^{2n}$ derive $g^{2n-1} = e$ with $2n - 1 \neq 0$.
- [ ] Q4 Conclude, and compare with $2\mathbb{Z} \subsetneq \mathbb{Z}$ in the first proof of Thm §43.1.
- [ ] Q5 **[why]** Why not use $\langle g \rangle$ itself as the proper subgroup? Give $A$ with $g$ of infinite order and $\langle g \rangle = A$.

> [!tip]- Hint (3): strategy
> **Strategy (G13, G14).** $H = \langle g^2 \rangle$ is nontrivial and does not contain $g$.

#### (4)

If the order of $g$ is a finite composite number, show that $A$ is not simple. Putting (1)–(4) together, the only case where $A$ is simple is $A = \langle g \rangle \cong \mathbb{Z}/p\mathbb{Z}$, $p$ prime.

^ps6-2-4

- [ ] Q1 **[def]** Define the order $c$ of $g$, and recall $g^N = e \iff c \mid N$ (Prop §17.3).
- [ ] Q2 Pick a prime $p \mid c$ with $1 < p < c$ and show $g^p \neq e$.
- [ ] Q3 Show $g \notin \langle g^p \rangle$: from $c \mid pn - 1$ and $p \mid c$ derive $p \mid 1$. Alternatively compute $|\langle g^p \rangle| = c/p$ (Prop §17.5).
- [ ] Q4 Assemble (1)–(4): if $A$ is simple, why is $A = \langle g \rangle$ of prime order, and why is $A \cong \mathbb{Z}/p\mathbb{Z}$?
- [ ] Q5 Converse: show $\mathbb{Z}/p\mathbb{Z}$ is simple (Cor §29.8).
- [ ] Q6 **[why]** Which step fails if $c$ is prime? Which step of the whole argument fails for $A_5$ (Prop §43.6)?

> [!tip]- Hint (4): strategy
> **Strategy (G3, G14).** For a prime $p \mid c$ with $p < c$, $H = \langle g^p \rangle$ has $c/p$ elements: nontrivial and proper.

> [!tip]- Hints: definitions and results for the whole problem
> **Topic and definitions.**
> - Simple group: [[§43 Simple Groups#^def-43-1|Def §43.1]]; normal subgroup [[§38 Normal Subgroups#^def-38-1|Def §38.1]]
> - Subgroup generated by an element [[§4 Subgroups#^def-4-3|Def §4.3]]; order of an element [[§4 Subgroups#^def-4-7|Def §4.7]]; cyclic group [[§4 Subgroups#^def-4-8|Def §4.8]]
>
> **Key results.** [[§43 Simple Groups#^thm-43-1|Thm §43.1]] (its second proof is this problem); (1) is [[§38 Normal Subgroups#^prop-38-1|Prop §38.1]](1). Used: $\langle g \rangle$ is a subgroup [[§4 Subgroups#^prop-4-5|Prop §4.5]], $k \mapsto g^k$ and $\langle g \rangle \cong \mathbb{Z}/N\mathbb{Z}$ [[§17 Cyclic Groups#^prop-17-3|Prop §17.3]], order of a power [[§17 Cyclic Groups#^prop-17-5|Prop §17.5]], groups of prime order [[§29 The Index and Lagrange's Theorem#^thm-29-7|Thm §29.7]], [[§29 The Index and Lagrange's Theorem#^cor-29-8|Cor §29.8]]. Contrast: $A_5$ is simple [[§43 Simple Groups#^prop-43-6|Prop §43.6]]; a non-normal subgroup [[§38 Normal Subgroups#^ex-38-1|Ex §38.1]].
>
> **Difficulty** (1) 1, (2) 1, (3) 1, (4) 1. Submitted solution: (1) direct; (2) proved by contrapositive with the literal hypothesis $\langle g \rangle g \neq A$, showing $Ag = A$; (3) $\langle g^2 \rangle$; (4) $\langle g^p \rangle$ for a prime divisor $p$; then a conclusion paragraph, including the converse via Lagrange. The notes give this as the second proof of Thm §43.1 and remark that $\langle g \rangle g = \langle g \rangle$.

### PS6.3 Groups of order p²

*Parts: (1), (2), (3), (4), (5).*

^ps6-3

#### (1)

Let $p$ be prime and $|G| = p^2$; by PS 3.5 there is $z \neq e$ with $zg = gz$ for all $g \in G$. Show that $z$ has order $p$ or $p^2$, and that if $z$ has order $p^2$ then $G = \langle z \rangle \cong \mathbb{Z}/p^2\mathbb{Z}$.

^ps6-3-1

- [ ] Q1 **[def]** Define the order of an element. Why does it equal $|\langle z \rangle|$?
- [ ] Q2 Apply Lagrange to $\langle z \rangle$. Why are the only options $p$ and $p^2$?
- [ ] Q3 If $z$ has order $p^2$, why is $\langle z \rangle = G$?
- [ ] Q4 Show $k \mapsto z^k$ is a well-defined isomorphism $\mathbb{Z}/p^2\mathbb{Z} \to \langle z \rangle$.
- [ ] Q5 **[why]** Where are $z \neq e$ and the primality of $p$ used? List the possible orders for $|G| = 12$ to compare.

> [!tip]- Hint (1): strategy
> **Strategy (G3, G12).** The order of $z$ is $|\langle z \rangle|$, which divides $p^2$ and is not $1$.

#### (2)

Assume $z$ has order $p$. Show that $\langle z \rangle$ is normal in $G$ and $G/\langle z \rangle \cong \mathbb{Z}/p\mathbb{Z}$.

^ps6-3-2

- [ ] Q1 **[def]** Define the center $Z(G)$ and a central element.
- [ ] Q2 Show $gz^k = z^kg$ for all $k \geq 0$ by induction.
- [ ] Q3 Conclude $ghg^{-1} = h$ for $h \in \langle z \rangle$, so $\langle z \rangle \trianglelefteq G$.
- [ ] Q4 Compute $|G/\langle z \rangle| = p$ and cite PS 2.5 (Thm §29.7).
- [ ] Q5 **[why]** Why must normality of $\langle z \rangle$ be shown before writing $G/\langle z \rangle$ as a group (Thm §40.1)?

> [!tip]- Hint (2): strategy
> **Strategy (G6, G3).** Every power of the central element $z$ is central, so $\langle z \rangle \subseteq Z(G)$ is normal; the quotient has prime order $p$.

#### (3)

Let $\bar g$ generate $G/\langle z \rangle$ and let $g \in G$ be a preimage. Show that $g^p = z^a$ for some $0 \leq a < p$.

^ps6-3-3

- [ ] Q1 **[def]** What does it mean that $\bar g$ generates $G/\langle z \rangle$? Why does $\bar g$ have order $p$?
- [ ] Q2 Show $g^p\langle z \rangle = \langle z \rangle$, hence $g^p \in \langle z \rangle$.
- [ ] Q3 Write $g^p = z^m$ and reduce: $m = qp + a$ with $0 \leq a < p$ (Lem §6.1).
- [ ] Q4 Why is $g \neq e$?
- [ ] Q5 **[why]** Does $a$ depend on the chosen preimage? Replace $g$ by $gz^j$ and compute $(gz^j)^p$; which hypothesis on $z$ makes this work?

> [!tip]- Hint (3): strategy
> **Strategy (G3, G14).** $\bar g^{\,p} = \bar e$ puts $g^p$ in $\langle z \rangle$; reduce the exponent mod $p$ using $z^p = e$.

#### (4)

If $a \neq 0$, show that $G = \langle g \rangle \cong \mathbb{Z}/p^2\mathbb{Z}$.

^ps6-3-4

- [ ] Q1 **[def]** Recall: $z^a = e$ if and only if $p \mid a$.
- [ ] Q2 Show $g^p \neq e$.
- [ ] Q3 Apply the argument of (1) to $g$: order $p$ or $p^2$, hence $p^2$.
- [ ] Q4 Conclude $G = \langle g \rangle \cong \mathbb{Z}/p^2\mathbb{Z}$.
- [ ] Q5 **[why]** Where is $0 < a < p$ used (rather than just $a \neq 0$ as an integer)?

> [!tip]- Hint (4): strategy
> **Strategy (G3).** $g^p = z^a \neq e$, so the order of $g$ is not $p$; it is $p^2$.

#### (5)

If $a = 0$, show that $G \cong \mathbb{Z}/p\mathbb{Z} \times \mathbb{Z}/p\mathbb{Z}$.

^ps6-3-5

- [ ] Q1 **[def]** Define the direct product $H \times L$ and its multiplication.
- [ ] Q2 Show $g$ has order $p$.
- [ ] Q3 Show $\langle z \rangle \cap \langle g \rangle = \{e\}$ (Lagrange in $\langle g \rangle$, and $\bar g \neq \bar e$).
- [ ] Q4 Show $\varphi(h, k) = hk$ is a homomorphism. Which hypothesis is needed to swap $k$ and $h'$?
- [ ] Q5 Show $\varphi$ is injective and conclude bijectivity by counting.
- [ ] Q6 State the general criterion that this proves (Lem §51.6), with its three conditions.
- [ ] Q7 **[why]** In $S_3$, $A_3$ and $\langle (1\,2) \rangle$ meet trivially and $3 \cdot 2 = 6$. Why is $\varphi$ not an isomorphism there? Which condition of Lem §51.6 fails?
- [ ] Q8 Deduce that every group of order $p^2$ is abelian (Cor §51.8).

> [!tip]- Hint (5): strategy
> **Strategy (G3, G6).** $\langle z \rangle$ and $\langle g \rangle$ have order $p$, meet trivially, and $z$ is central, so $(h, k) \mapsto hk$ is an isomorphism $\langle z \rangle \times \langle g \rangle \to G$.

> [!tip]- Hints: definitions and results for the whole problem
> **Topic and definitions.**
> - Center [[§35 The Center#^def-35-2|Def §35.2]]; $p$-group [[§35 The Center#^def-35-3|Def §35.3]]
> - Order of an element [[§4 Subgroups#^def-4-7|Def §4.7]]; normal subgroup [[§38 Normal Subgroups#^def-38-1|Def §38.1]]; quotient group [[§40 Quotient Groups#^def-40-1|Def §40.1]]
> - Direct product: [[§3 Basic Examples of Groups#^def-3-2|Def §3.2]]
>
> **Key results.** [[§54 p-Groups and Sylow Subgroups#^thm-54-7|Thm §54.7]] (this problem); the splitting step is [[§54 p-Groups and Sylow Subgroups#^lem-54-6|Lem §54.6]]; consequence [[§54 p-Groups and Sylow Subgroups#^cor-54-8|Cor §54.8]]. Used: nontrivial center of $p$-groups (PS 3.5) [[§35 The Center#^thm-35-3|Thm §35.3]], Lagrange [[§29 The Index and Lagrange's Theorem#^thm-29-2|Thm §29.2]], groups of prime order (PS 2.5) [[§29 The Index and Lagrange's Theorem#^thm-29-7|Thm §29.7]], $\langle g \rangle \cong \mathbb{Z}/N\mathbb{Z}$ [[§17 Cyclic Groups#^prop-17-3|Prop §17.3]], division algorithm [[§6 Divisibility and Congruence#^lem-6-1|Lem §6.1]]. Context: [[§54 p-Groups and Sylow Subgroups#^rem-54-2|Remark: Groups of Order p to the k]].
>
> **Difficulty** (1) 1, (2) 1, (3) 1, (4) 1, (5) 2. Submitted solution: follows the five steps; (2) by induction on $k$; (3) via the quotient map and the division algorithm; (5) proves the trivial intersection, then that $\varphi$ is a homomorphism (using centrality) and injective, and counts. The notes split (5) off as Lem §51.6, with the "both normal" condition added (not from the problem set), and state Thm §51.7.

### PS6.4 The order of GLn(Fp)

*Parts: (1), (2).*

^ps6-4

#### (1)

Prove by induction on $k$: the number of $k$-tuples $(\vec v_1, \ldots, \vec v_k)$ in $\mathbb{F}_p^n$ which are linearly independent is $(p^n - 1)(p^n - p) \cdots (p^n - p^{k-1})$.

^ps6-4-1

- [ ] Q1 **[def]** Define linear independence of a $k$-tuple. Why is $|\mathbb{F}_p^n| = p^n$?
- [ ] Q2 Base case: show $(\vec v_1)$ is independent if and only if $\vec v_1 \neq \vec 0$.
- [ ] Q3 Show every independent $(k+1)$-tuple has an independent first $k$ entries, so it suffices to count extensions.
- [ ] Q4 Show $(\vec v_1, \ldots, \vec v_{k+1})$ is dependent if and only if $\vec v_{k+1} \in \operatorname{span}(\vec v_1, \ldots, \vec v_k)$.
- [ ] Q5 Show the span of an independent $k$-tuple has exactly $p^k$ elements.
- [ ] Q6 Conclude the inductive step. What does the formula give for $k > n$?
- [ ] Q7 **[why]** Where is it used that $\mathbb{F}_p$ is a field? Test the base case over $\mathbb{Z}/4\mathbb{Z}$: count the nonzero vectors of $(\mathbb{Z}/4\mathbb{Z})^1$ and the independent $1$-tuples.

> [!tip]- Hint (1): strategy
> **Strategy (G14, G10).** Extend an independent $k$-tuple by any vector outside its span; the span has exactly $p^k$ elements.

#### (2)

Show that $|GL_n(\mathbb{F}_p)| = (p^n - 1)(p^n - p) \cdots (p^n - p^{n-1})$.

^ps6-4-2

- [ ] Q1 **[def]** Define $GL_n(\mathbb{F}_p)$.
- [ ] Q2 Show $M \mapsto (\vec m_1, \ldots, \vec m_n)$ is a bijection from $\operatorname{Mat}_n(\mathbb{F}_p)$ to $n$-tuples of vectors.
- [ ] Q3 Show $M$ is invertible if and only if its columns are independent (Lem §51.2): write $M\vec c = \sum c_i \vec m_i$ and use rank–nullity.
- [ ] Q4 Conclude from (1) with $k = n$.
- [ ] Q5 Compute $|GL_2(\mathbb{F}_2)|$ and $|GL_2(\mathbb{F}_5)|$, and rewrite the formula as $p^{\binom{n}{2}} \prod_{k=1}^{n} (p^k - 1)$ (Prop §51.4).
- [ ] Q6 **[why]** In Q3, injective implies invertible. Which hypothesis (square matrix, finite dimension) makes this true?

> [!tip]- Hint (2): strategy
> **Strategy (G10).** A matrix is its list of columns, and it is invertible exactly when the columns are independent; apply (1) with $k = n$.

> [!tip]- Hints: definitions and results for the whole problem
> **Topic and definitions.**
> - General linear group: [[§3 Basic Examples of Groups#^def-3-6|Def §3.6]]
> - Field: [[§3 Basic Examples of Groups#^def-3-3|Def §3.3]]; $\mathbb{Z}/n\mathbb{Z}$ is a field iff $n$ is prime [[§8 Invertibility and Unit Groups#^prop-8-4|Prop §8.4]]
>
> **Key results.** (1) is [[§54 p-Groups and Sylow Subgroups#^lem-54-3|Lem §54.3]]; (2) is [[§54 p-Groups and Sylow Subgroups#^prop-54-4|Prop §54.4]], with [[§54 p-Groups and Sylow Subgroups#^lem-54-2|Lem §54.2]] (invertible iff independent columns). Used later: [[§54 p-Groups and Sylow Subgroups#^ex-54-2|Ex §54.2]] ($|GL_2(\mathbb{F}_5)| = 480$), unitriangular Sylow subgroup [[§54 p-Groups and Sylow Subgroups#^prop-54-5|Prop §54.5]].
>
> **Difficulty** (1) 2, (2) 1. Submitted solution: induction with explicit base case, the "dependent iff in the span" equivalence, and $|S| = p^k$ via the coordinate bijection; (2) via the column bijection and rank–nullity. The notes quote it as Lem §51.3 and the proof of Prop §51.4 (the rewriting as $p^{\binom{n}{2}} \prod (p^k - 1)$ is added in the notes, not from the problem set).

## Strategy codes
- **G1 Subgroup test.** One-step test $ab^{-1} \in H$; for finite subsets closure suffices; intersections, images, preimages, kernels.
- **G2 Well-definedness on representatives.** Cosets, $\mathbb{Z}/n\mathbb{Z}$, quotient groups, maps out of $G/N$: define on a representative, check independence of the choice.
- **G3 Lagrange and divisibility.** $|H|$ divides $|G|$; order of an element divides $|G|$; index multiplicativity; coprime orders force trivial intersections or trivial maps.
- **G4 Orbit–stabilizer and counting.** $|G\cdot x| = [G : G_x]$; orbits partition; class equation; Burnside; fixed points mod $p$ for $p$-groups.
- **G5 Kernels and the First Isomorphism Theorem.** Show normality as a kernel; identify a quotient $G/N$ by a surjective homomorphism with kernel $N$; $|G| = |\ker|\,|\mathrm{im}|$.
- **G6 Conjugation preserves structure.** Conjugate elements have the same order and cycle type; conjugate subgroups are isomorphic; $gHg^{-1}$; normal = union of conjugacy classes.
- **G7 Work on generators.** A homomorphism or a property is checked on generators ($S_n$ by transpositions or 3-cycles, cyclic groups by one element, $A_n$ by 3-cycles).
- **G8 Characters and commutators.** Characters kill commutators; $G/N$ abelian iff $D(G) \subseteq N$; abelianization; the sign.
- **G9 Move properties along subgroups and quotients.** Correspondence and isomorphism theorems; solvability, simplicity, normality passed between $G$, $N$, $G/N$.
- **G10 Compute in a small group.** Explicit work in $S_3$, $S_4$, $A_4$, $A_5$, $D_n$, $GL_2(\mathbb{F}_p)$, $U_n$; produce a counterexample.
- **G11 Actions as homomorphisms $G \to S_X$.** Cayley; left multiplication on $G/H$ and its kernel (normal core); embeddings into $GL_n$; faithfulness.
- **G12 Prime-power counting.** $p$-groups have nontrivial center; groups of order $p$, $p^2$, $pq$; Cauchy; Sylow counting $n_p \mid m$, $n_p \equiv 1 \pmod p$.
- **G13 Simplicity and normal-subgroup arguments.** Normal subgroups are unions of conjugacy classes (sizes add up to a divisor); index-2 subgroups are normal; a normal subgroup containing one 3-cycle contains all.
- **G14 Arithmetic in $\mathbb{Z}/n$.** Euclid, Bézout, CRT, unit groups $U_n$, orders modulo $n$.
