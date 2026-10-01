---
type: section
subject: "[[Group Theory]]"
chapter: 1
section: 2
tags: [group-theory, math493]
---
← [[§1 The Definition of a Group]] · ↑ [[· 1 Groups and Subgroups]] · [[§3 Basic Examples of Groups]] →

*Source: WS 1.1–1.4*

*Reference: Pinter Ch. 4, Thms. 1–3.*

> [!theorem] Proposition §2.1: Cancellation, and What the Mixed Hypothesis Really Gives
> Let $g, h_1, h_2 \in G$.
> 1. **(Left cancellation)** If $g h_1 = g h_2$, then $h_1 = h_2$. (Likewise, $h_1 g = h_2 g$ implies $h_1 = h_2$: **right cancellation**.)
> 2. **(Mixed hypothesis — the worksheet's second part)** If $g h_1 = h_2 g$, then $h_2 = g h_1 g^{-1}$. In general this does *not* force $h_1 = h_2$ (see the example [[§2 First Consequences of the Axioms#^ex-2-1|The Mixed Hypothesis Does Not Cancel]], below); rather, $h_1 = h_2$ holds if and only if $g h_1 = h_1 g$, i.e. iff $g$ and $h_1$ commute.
>
> *Source: WS 1.1*

^prop-2-1

> [!proof]+ Proof
> **(1)** Suppose $g h_1 = g h_2$. Multiply both sides on the left by $g^{-1}$, which exists by axiom (2):
>
> $$ g^{-1} (g h_1) = g^{-1} (g h_2). $$
>
> By associativity (axiom (3)), $(g^{-1} g) h_1 = (g^{-1} g) h_2$, so by axiom (2), $e \cdot h_1 = e \cdot h_2$, and by axiom (1), $h_1 = h_2$.
>
> For right cancellation, suppose $h_1 g = h_2 g$. Multiplying both sides on the *right* by $g^{-1}$ and applying axioms (3), (2), (1) in the same order:
>
> $$ h_1 = h_1 (g g^{-1}) = (h_1 g) g^{-1} = (h_2 g) g^{-1} = h_2 (g g^{-1}) = h_2. $$
>
> **(2)** Suppose $g h_1 = h_2 g$. Multiplying both sides on the *right* by $g^{-1}$:
>
> $$ g h_1 g^{-1} = h_2 (g g^{-1}) = h_2. $$
>
> Now, if $h_1 = h_2$, substituting into the hypothesis gives $g h_1 = h_1 g$. Conversely, if $g h_1 = h_1 g$, then $h_2 = g h_1 g^{-1} = h_1 (g g^{-1}) = h_1$. So under the mixed hypothesis, $h_1 = h_2 \iff g h_1 = h_1 g$.

^pf-2-1

*Uses:* [[§1 The Definition of a Group#^def-1-1|Def. §1.1]]

> [!example] Example §2.1: The Mixed Hypothesis Does Not Cancel
> In $S_3$, take $g = (1\,2)$, $h_1 = (2\,3)$, $h_2 = (1\,3)$. Computing (right factor first):
>
> $$ g h_1 = (1\,2)(2\,3) = (1\,2\,3), \qquad h_2 g = (1\,3)(1\,2) = (1\,2\,3), $$
>
> so $g h_1 = h_2 g$ — yet $h_1 = (2\,3) \neq (1\,3) = h_2$. Consistently with [[§2 First Consequences of the Axioms#^prop-2-1|part (2)]], $h_2 = g h_1 g^{-1}$: conjugating the swap $2 \leftrightarrow 3$ by the relabeling $1 \leftrightarrow 2$ produces the swap $1 \leftrightarrow 3$.
>
> *Source: WS 1.1*

^ex-2-1

![[m493-2-1.svg]]
*Conjugation relabels. The top row is $h_1 = (2\,3)$ (blue); the gray arrows are the relabeling $g = (1\,2)$. Carried along $g$, the swap $2 \leftrightarrow 3$ becomes the swap of $g(2) = 1$ and $g(3) = 3$, i.e. $h_2 = g h_1 g^{-1} = (1\,3)$ (red). Across-then-down equals down-then-across, which is $g h_1 = h_2 g$ — and still $h_1 \neq h_2$.*

> [!remark]- Connections
> - Revisited with cycle notation: [[§12 Multiplying and Conjugating Cycles#^ex-12-2|The Mixed Hypothesis of WS 1.1, Revisited]]; the general rule: [[§12 Multiplying and Conjugating Cycles#^prop-12-1|Conjugation Relabels a Cycle]].

> [!remark] Remark: Left vs. Right; Conjugation
> The moral of [[§2 First Consequences of the Axioms#^prop-2-1|part (2)]]: in a non-abelian group, “multiply both sides by $g^{-1}$” is only valid on the *same side* of both expressions; multiplying on opposite sides transports an element to its *conjugate* $g h g^{-1}$ instead of cancelling it. In an abelian group the mixed hypothesis *does* give $h_1 = h_2$. Conjugation — and the way conjugating a permutation “relabels” the objects it moves, as in [[§2 First Consequences of the Axioms#^ex-2-1|The Mixed Hypothesis Does Not Cancel]] — will become a central tool later ([[§35 Normal Subgroups#^def-35-1|normal subgroups]], [[§31 Conjugacy Classes#^def-31-1|conjugacy classes]]).

^rem-2-1

> [!theorem] Proposition §2.2: Uniqueness of the Identity
> $G$ contains exactly one element $e$ obeying condition (1) of the [[§1 The Definition of a Group#^def-1-1|definition of a group]].
>
> *Source: WS 1.2*

^prop-2-2

> [!proof]+ Proof
> Suppose $e$ and $e'$ both obey condition (1). Evaluate the single product $e * e'$ in two ways. Since $e'$ satisfies (1) (with $g = e$): $e * e' = e$. Since $e$ satisfies (1) (with $g = e'$): $e * e' = e'$. Hence $e = e * e' = e'$.

^pf-2-2

*Uses:* [[§1 The Definition of a Group#^def-1-1|Def. §1.1]]

> [!theorem] Proposition §2.3: Uniqueness of Inverses
> For each $g \in G$, there is exactly one element $g^{-1} \in G$ obeying condition (2) of the [[§1 The Definition of a Group#^def-1-1|definition of a group]].
>
> *Source: WS 1.3*

^prop-2-3

> [!proof]+ Proof
> Suppose $h$ and $h'$ both obey condition (2) for $g$, i.e. $g h = h g = e$ and $g h' = h' g = e$. Then $g h = e = g h'$, so by left cancellation ([[§2 First Consequences of the Axioms#^prop-2-1|Cancellation, §2.1]]), $h = h'$.
>
> *Alternative direct computation (avoiding [[§2 First Consequences of the Axioms#^prop-2-1|WS 1.1]]):*
>
> $$ h = h \cdot e = h (g h') = (h g) h' = e \cdot h' = h'. $$

^pf-2-3

*Uses:* [[§2 First Consequences of the Axioms#^prop-2-1|§2.1]], [[§1 The Definition of a Group#^def-1-1|Def. §1.1]]

> [!remark]- Connections
> - Both uniqueness facts (§2.2, §2.3) appear in MATH 590 as a single remark: [[§21 Algebra Prerequisites꞉ Groups#^rem-21-2|Uniqueness of Identity and Inverses]]; the linear-algebra version: [[§10 Invertibility and Isomorphisms#^ladr-3-60|Inverse is unique]].

> [!remark] Remark: The Uniqueness Technique
> [[§2 First Consequences of the Axioms#^prop-2-3|WS 1.3]] gives the standard technique for computing inverses: since the inverse of $x$ is *unique*, to prove $y = x^{-1}$ it suffices to verify that $y$ satisfies the defining property $x y = y x = e$. [[§2 First Consequences of the Axioms#^prop-2-4|WS 1.4]] and [[§4 Subgroups#^prop-4-5|1.5]] below, and the identity $(AB)^{-1} = B^{-1} A^{-1}$ for [[§10 Invertibility and Isomorphisms#^ladr-3-80|matrices]], are all proved this way. (Compare the [[§21 Algebra Prerequisites꞉ Groups#^prop-21-4|590 notes]], where the same pattern proves bijectivity via a two-sided inverse.)

^rem-2-2

> [!theorem] Proposition §2.4: Inverse of a Product
> For all $g, h \in G$:  $(gh)^{-1} = h^{-1} g^{-1}$.
>
> *Source: WS 1.4*

^prop-2-4

> [!proof]+ Proof
> By [[§2 First Consequences of the Axioms#^prop-2-3|WS 1.3]], it suffices to verify that $h^{-1} g^{-1}$ satisfies the defining property of the inverse of $gh$:
>
> $$ (gh)(h^{-1} g^{-1}) = g (h h^{-1}) g^{-1} = g \cdot e \cdot g^{-1} = g g^{-1} = e, $$
>
> $$ (h^{-1} g^{-1})(gh) = h^{-1} (g^{-1} g) h = h^{-1} \cdot e \cdot h = h^{-1} h = e. $$
>
> Since the inverse of $gh$ is unique and $h^{-1}g^{-1}$ satisfies its defining property, $(gh)^{-1} = h^{-1} g^{-1}$.

^pf-2-4

*Uses:* [[§2 First Consequences of the Axioms#^prop-2-3|§2.3]], [[§1 The Definition of a Group#^def-1-1|Def. §1.1]]

> [!remark]- Connections
> - The matrix case $(AC)^{-1} = C^{-1}A^{-1}$, proved the same way: [[§10 Invertibility and Isomorphisms#^ladr-3-80|LADR 3.80]].

> [!theorem] Corollary §2.5: Inverse of a Product of $n$ Elements
> For $g_1, \ldots, g_n \in G$:  $(g_1 g_2 \cdots g_n)^{-1} = g_n^{-1} \cdots g_2^{-1} g_1^{-1}$.

^cor-2-5

> [!proof]+ Proof
> Induct on $n$, the case $n = 2$ being [[§2 First Consequences of the Axioms#^prop-2-4|the proposition]]: $(g_1 \cdots g_n)^{-1} = \big((g_1 \cdots g_{n-1})g_n\big)^{-1} = g_n^{-1}(g_1 \cdots g_{n-1})^{-1} = g_n^{-1}g_{n-1}^{-1} \cdots g_1^{-1}$.

^pf-2-5

*Uses:* [[§2 First Consequences of the Axioms#^prop-2-4|§2.4]], [[§1 The Definition of a Group#^prop-1-1|§1.1]], [[§1 The Set ℕ of Natural Numbers#^thm-1-1|451 §1.1]]

> [!remark] Remark: Socks and Shoes
> The order reversal is forced in non-abelian groups: to undo “put on socks, then shoes,” remove shoes first.

^rem-2-3

> [!theorem] Proposition §2.6: One-Sided Inverses Suffice
> Let $a, b \in G$.
> 1. If $ab = e$, then $b = a^{-1}$ and $a = b^{-1}$. Consequently $ab = e$ implies $ba = e$.
> 2. $(a^{-1})^{-1} = a$.
>
> *Source: cf. Pinter Ch. 4, Thm. 2–3*

^prop-2-6

> [!proof]+ Proof
> **(1)** If $ab = e$, then $ab = a a^{-1}$, so $b = a^{-1}$ by left cancellation ([[§2 First Consequences of the Axioms#^prop-2-1|Cancellation, §2.1]]). Likewise $ab = e = b^{-1} b$ gives $a = b^{-1}$ by right cancellation. Then $ba = a^{-1} a = e$.
>
> **(2)** The element $a$ satisfies $a^{-1} a = a a^{-1} = e$, which is the defining property of the inverse of $a^{-1}$; by uniqueness of inverses ([[§2 First Consequences of the Axioms#^prop-2-3|Uniqueness of Inverses, §2.3]]), $(a^{-1})^{-1} = a$.

^pf-2-6

*Uses:* [[§2 First Consequences of the Axioms#^prop-2-1|§2.1]], [[§2 First Consequences of the Axioms#^prop-2-3|§2.3]]

> [!remark] Remark: Why One-Sided Suffices Here but Not in General
> In a group, checking $ab = e$ alone certifies $b = a^{-1}$; the other equation $ba = e$ comes free. This is special to groups (it uses that $a$ already *has* a two-sided inverse). In monoids — e.g. functions $X \to X$ under composition for infinite $X$ — a one-sided inverse need not be two-sided: the shift $n \mapsto n + 1$ on $\mathbb{N}$ has a left inverse but no right inverse.

^rem-2-4

> [!remark]- Connections
> - For linear maps between spaces of the same finite dimension one-sided also suffices, for a different reason (dimension): [[§10 Invertibility and Isomorphisms#^ladr-3-68|ST = I ⟺ TS = I]]; the infinite-dimensional shifts on $\mathbb{F}^\infty$ fail it exactly like the shift on $\mathbb{N}$ ([[§10 Invertibility and Isomorphisms#^ladr-3-65|LADR 3.65]]).
> - Functions: a left inverse gives injectivity, a right inverse surjectivity: [[§21 Algebra Prerequisites꞉ Groups#^prop-21-4|Bijectivity via Two-Sided Inverse]].

> [!theorem] Proposition §2.7: Unique Solvability of Linear Equations
> Let $a, b \in G$. The equation $ax = b$ has exactly one solution $x \in G$, namely $x = a^{-1} b$; and $xa = b$ has exactly one solution, namely $x = b a^{-1}$.
>
> *Source: cf. Pinter Ch. 4*

^prop-2-7

> [!proof]+ Proof
> **Existence:** $a(a^{-1} b) = (a a^{-1}) b = b$. **Uniqueness:** if $ax = b = ax'$, then $x = x'$ by left cancellation. The equation $xa = b$ is handled symmetrically with right cancellation.

^pf-2-7

*Uses:* [[§1 The Definition of a Group#^def-1-1|Def. §1.1]], [[§2 First Consequences of the Axioms#^prop-2-1|§2.1]]

> [!theorem] Corollary §2.8: Latin Square Property
> In the multiplication table of a finite group, every element appears exactly once in each row and exactly once in each column; that is, the table is a *Latin square*.

^cor-2-8

> [!proof]+ Proof
> In the row of $a$, the element $b$ appears in column $x$ iff $ax = b$, and by [[§2 First Consequences of the Axioms#^prop-2-7|Unique Solvability]] this has exactly one solution: existence gives “at least once,” uniqueness (cancellation) “at most once.” Columns are handled the same way with $xa = b$.

^pf-2-8

*Uses:* [[§2 First Consequences of the Axioms#^prop-2-7|§2.7]]

> [!remark]- Connections
> - Multiplication tables are defined and computed in [[§14 Multiplication Tables#^def-14-1|Multiplication Table]]; the unit-group analogue (finiteness plus cancellation): [[§8 Invertibility and Unit Groups#^prop-8-2|Multiplication by a Nonzero Class Permutes the Nonzero Classes]].

> [!remark] Remark: The Converse Fails
> A Latin square need not be a group table, since associativity is not encoded row by row. The property is visible in the $S_3$ table ([[§10 Cycle Notation and the Group S₃#^ex-10-1|§10.1]]).

^rem-2-5
