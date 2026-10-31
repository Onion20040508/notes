---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C6a
section: C6a.6
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C6a.5 Normal Ordering and Contractions]] · ↑ [[· C6a Interactions and Correlation Functions]] · [[§C6a.7 Feynman Diagrams for Correlation Functions]] →

*Sources: the user's PHY 513 notes, Ch. 14 §14.2 (Principle "Wick's theorem", Derivations "Proof by induction (filled in)" and "Four fields", Principle "Vacuum expectation values: complete contractions", paragraphs "Contracting two pairs", "Theorem and application") · PHY 513 Lecture 14 (Larsen, 26 Oct 2026), Part A, slides 9–10, and transcript · Peskin & Schroeder, An Introduction to Quantum Field Theory, §4.3, pp. 89–90, eqs. (4.38)–(4.41) · Yu Zhao-Huan, 量子场论讲义, §6.3.1, eqs. (6.166)–(6.168); §6.3.2 (optional reading): lemma (6.169)–(6.170) with proof (6.171)–(6.185), proof of the theorem (6.186)–(6.193).*

For two fields the time-ordered product is the normal-ordered product plus one contraction ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-6|Theorem §C2b.6.6]]). For $n$ fields every misplaced $\hat\phi^+$ must be moved past every $\hat\phi^-$, each move costs a $c$-number ([[§C6a.5 Normal Ordering and Contractions#^thm-c6a-5-2|Theorem §C6a.5.2]]), and time ordering turns each cost into a Feynman propagator. Wick's theorem says what the total is: the normal-ordered product plus every way of contracting pairs ([[§C6a.5 Normal Ordering and Contractions#^def-c6a-5-1|Def. §C6a.5.1]]). In the vacuum only the terms with every field contracted survive, so a free vacuum expectation value is a sum over pairings of the fields. The proof is an induction on the number of fields, built on a lemma about appending one more field of earlier time. Yu treats this in §6.3, eqs. (6.166)–(6.193), for bosons and fermions, and proves it with the same lemma (6.169); PS prove it by prepending the latest field instead (eq. (4.41)), kept here as a second proof.

*Conventions* ([[Larsen PHY 513]]): as in [[§C6a.5 Normal Ordering and Contractions|§C6a.5]]: $\hat\phi_i \equiv \hat\phi_I(x_i)$, free fields; $D_{ij} \equiv D_F(x_i - x_j)$ where it saves space; a hat over a factor, $\widehat{\hat\phi_k}$, is avoided: "$\prod_{i\ne k}$" or "omit $\hat\phi_k$" is written out.

The pairings and their number, from [[§CA.7 Pairings, Diagrams and Symmetry Factors|§CA.7]], are the two pieces of mathematics used:

![[§CA.7 Pairings, Diagrams and Symmetry Factors#^def-ca-7-1]]

![[§CA.7 Pairings, Diagrams and Symmetry Factors#^thm-ca-7-1]]

## The lemma

> [!theorem] Lemma §C6a.6.1: Appending a Field of Earlier Time
> Let $x_b^0 \le x_i^0$ for $i = 1, \dots, n$. Then
> 1. $\displaystyle:\!\hat\phi_1\cdots\hat\phi_n\!:\;\hat\phi_b = \,:\!\hat\phi_1\cdots\hat\phi_n\hat\phi_b\!: + \sum_{k=1}^nD_F(x_k - x_b)\,:\!\prod_{i\ne k}\hat\phi_i\!: ,$
>
> the normal-ordered product of all $n + 1$ fields plus the contraction of $\hat\phi_b$ with each of the others, the rest normal ordered ([[§C6a.5 Normal Ordering and Contractions#^def-c6a-5-1|Def. §C6a.5.1]]);
> 2. the same holds when the product on the left already carries $c$-number factors from earlier contractions among $\hat\phi_1, \dots, \hat\phi_n$: they multiply every term on the right.
>
> *Source: PHY 513 Lecture 14, slide 9 ("$N(\phi_1\dots\phi_{n-1})\phi_n = N(\phi_1\dots\phi_{n-1}\phi_n)$ + contract $\phi_n$ with any other $\phi$"; the condition on the times is implicit there, [[§C6a.6 Wick's Theorem#^cau-c6a-6-1|Caution: The lemma needs the earliest time]]) · Yu §6.3.2, eqs. (6.169)–(6.170) · proof written here (shorter than Yu's four steps (6.171)–(6.185))*

^lem-c6a-6-1

> [!derivation]- Derivation
> **Step 1** (split the new field and expand $M$). $\hat\phi_b = \hat\phi_b^+ + \hat\phi_b^-$ ([[§C2b.1 Heisenberg Fields#^thm-c2b-1-5|Theorem §C2b.1.5]]), and ([[§C6a.5 Normal Ordering and Contractions#^thm-c6a-5-1|Theorem §C6a.5.1]], 1)
>
> $$
> M \equiv \,:\!\hat\phi_1\cdots\hat\phi_n\!: = \sum_{A\subseteq\{1,\dots,n\}}M_A, \qquad M_A = \prod_{i\in A}\hat\phi_i^-\prod_{j\notin A}\hat\phi_j^+ ;
> $$
>
> for $n = 2$: $M = \underbrace{\hat\phi_1^+\hat\phi_2^+}_{A = \varnothing} + \underbrace{\hat\phi_2^-\hat\phi_1^+}_{A = \{2\}} + \underbrace{\hat\phi_1^-\hat\phi_2^+}_{A = \{1\}} + \underbrace{\hat\phi_1^-\hat\phi_2^-}_{A = \{1,2\}}$.
>
> **Step 2** (the $\hat\phi_b^+$ part is already ordered). In $M_A\hat\phi_b^+$ every $\hat\phi^-$ stands left of every $\hat\phi^+$:
>
> $$
> M_A\,\hat\phi_b^+ = \prod_{i\in A}\hat\phi_i^-\;\Bigl(\prod_{j\notin A}\hat\phi_j^+\Bigr)\hat\phi_b^+ = \bigl(\text{the term of } :\!\hat\phi_1\cdots\hat\phi_n\hat\phi_b\!: \text{ with set } A,\ b \notin A\bigr) .
> $$
>
> **Step 3** (move $\hat\phi_b^-$ to the front). $M_A\hat\phi_b^- = \hat\phi_b^-M_A + [M_A, \hat\phi_b^-]$, and $\hat\phi_b^-M_A = \bigl(\hat\phi_b^-\prod_{i\in A}\hat\phi_i^-\bigr)\prod_{j\notin A}\hat\phi_j^+$ is the term of $:\!\hat\phi_1\cdots\hat\phi_n\hat\phi_b\!:$ with set $A \cup \{b\}$. Summing Steps 2 and 3 over $A$ collects all $2^{n+1}$ terms of $:\!\hat\phi_1\cdots\hat\phi_n\hat\phi_b\!:$:
>
> $$
> M\hat\phi_b = \sum_A\bigl(M_A\hat\phi_b^+ + \hat\phi_b^-M_A\bigr) + \sum_A[M_A, \hat\phi_b^-] = \,:\!\hat\phi_1\cdots\hat\phi_n\hat\phi_b\!:\, + \sum_A[M_A, \hat\phi_b^-] .
> $$
>
> **Step 4** (the commutator is a derivation). For a product, $[F_1F_2\cdots F_r, G] = \sum_sF_1\cdots F_{s-1}[F_s, G]F_{s+1}\cdots F_r$. With $G = \hat\phi_b^-$: $[\hat\phi_i^-, \hat\phi_b^-] = 0$ and $[\hat\phi_j^+, \hat\phi_b^-] = D_W(x_j - x_b)\mathbf 1$ ([[§C6a.5 Normal Ordering and Contractions#^thm-c6a-5-2|Theorem §C6a.5.2]]), a number, which can be pulled out. For $n = 2$, term by term:
>
> $$
> \begin{aligned}
> A = \varnothing\colon&\quad [\hat\phi_1^+\hat\phi_2^+, \hat\phi_b^-] = \hat\phi_1^+\,D_W(x_2 - x_b) + D_W(x_1 - x_b)\,\hat\phi_2^+ ,\\
> A = \{2\}\colon&\quad [\hat\phi_2^-\hat\phi_1^+, \hat\phi_b^-] = \hat\phi_2^-\,D_W(x_1 - x_b) + 0 ,\\
> A = \{1\}\colon&\quad [\hat\phi_1^-\hat\phi_2^+, \hat\phi_b^-] = \hat\phi_1^-\,D_W(x_2 - x_b) + 0 ,\\
> A = \{1,2\}\colon&\quad [\hat\phi_1^-\hat\phi_2^-, \hat\phi_b^-] = 0 .
> \end{aligned}
> $$
>
> In general, one term for each $\hat\phi_k^+$ in $M_A$:
>
> $$
> [M_A, \hat\phi_b^-] = \sum_{k\notin A}D_W(x_k - x_b)\;\prod_{i\in A}\hat\phi_i^-\prod_{j\notin A,\,j\ne k}\hat\phi_j^+ .
> $$
>
> **Step 5** (resum over $A$). For $n = 2$, collect the four lines of Step 4 by the $D_W$ they carry:
>
> $$
> \sum_A[M_A, \hat\phi_b^-] = D_W(x_1 - x_b)\bigl(\hat\phi_2^+ + \hat\phi_2^-\bigr) + D_W(x_2 - x_b)\bigl(\hat\phi_1^+ + \hat\phi_1^-\bigr) = D_W(x_1 - x_b):\!\hat\phi_2\!: + D_W(x_2 - x_b):\!\hat\phi_1\!: .
> $$
>
> In general, exchange the sums, $\sum_A\sum_{k\notin A} = \sum_k\sum_{A\not\ni k}$. For fixed $k$ the subsets $A$ of $\{1, \dots, n\}$ not containing $k$ are exactly the subsets of $\{1, \dots, n\}\setminus\{k\}$, and the summand is the $A$-term of $:\!\prod_{i\ne k}\hat\phi_i\!:$ ([[§C6a.5 Normal Ordering and Contractions#^thm-c6a-5-1|Theorem §C6a.5.1]], 1, for $n - 1$ fields):
>
> $$
> \sum_A[M_A, \hat\phi_b^-] = \sum_{k=1}^nD_W(x_k - x_b)\,:\!\prod_{i\ne k}\hat\phi_i\!: .
> $$
>
> **Step 6** (the time condition). [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-2|Theorem §C2b.6.2]] with $\xi = x_k - x_b$:
>
> $$
> D_F(\xi) = \theta(\xi^0)\,D_W(\xi) + \theta(-\xi^0)\,D_W(-\xi) = D_W(\xi) \qquad (\xi^0 > 0) .
> $$
>
> For $\xi^0 = 0$ the separation is spacelike or zero and the commutator function vanishes there ([[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-5|Theorem §C2b.4.5]]): $D_W(\xi) - D_W(-\xi) = iD(\xi) = 0$, so $D_W(\xi) = D_W(-\xi) = D_F(\xi)$ again. With the bracket $\overbracket{\hat\phi_k\hat\phi_b} = D_F(x_k - x_b)$ ([[§C6a.5 Normal Ordering and Contractions#^def-c6a-5-1|Def. §C6a.5.1]]), Steps 3 and 5 give part 1; for $n = 2$:
>
> $$
> :\!\hat\phi_1\hat\phi_2\!:\,\hat\phi_b = \,:\!\hat\phi_1\hat\phi_2\hat\phi_b\!:\, + \overbracket{\hat\phi_1\hat\phi_b}\,:\!\hat\phi_2\!:\, + \overbracket{\hat\phi_2\hat\phi_b}\,:\!\hat\phi_1\!: .
> $$
>
> ⚑ By-product: Steps 1–5 never used the times. Without the condition the lemma holds with $D_W(x_k - x_b)$ in place of $D_F(x_k - x_b)$ → [[§C6a.6 Wick's Theorem#^thm-c6a-6-4|★ Theorem §C6a.6.4]].
>
> **Step 7** (earlier contractions, part 2). A $c$-number factor commutes with every operator, so it can be taken out before Step 1 and put back on every term.
>
> **What the derivation shows.**
> - "Each $\hat\phi^-$ on the wrong side has to be fixed, and each fix costs a $D_F$" (the user's notes): the fixes are the commutators of Step 4, and the time condition turns $D_W$ into $D_F$.
> - Used next: the induction step of Wick's theorem (Theorem §C6a.6.2).

^der-c6a-6-1

*Uses:* [[§C2b.1 Heisenberg Fields#^thm-c2b-1-5|Theorem §C2b.1.5]], [[§C6a.5 Normal Ordering and Contractions#^thm-c6a-5-1|Theorem §C6a.5.1]], [[§C6a.5 Normal Ordering and Contractions#^thm-c6a-5-2|Theorem §C6a.5.2]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-2|Theorem §C2b.6.2]], [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-5|Theorem §C2b.4.5]]

> [!caution] Caution: The lemma needs the earliest time
> Slide 9 states the induction step as "$N(\phi_1\dots\phi_{n-1})\phi_n = N(\phi_1\dots\phi_{n-1}\phi_n)$ + contract $\phi_n$ with any other $\phi$", where "contract" means $D_F$. This holds when $\phi_n$ has the earliest time, which is how it is used in the induction ([[§C6a.6 Wick's Theorem#^lem-c6a-6-1|Lemma §C6a.6.1]]; Yu (6.169) states the condition $x_b^0 \le x_1^0, \dots, x_n^0$). For general times the added terms are $D_W(x_i - x_n)$, not $D_F$.
>
> *Source: PHY 513 Lecture 14, slide 9 (page image) · Yu §6.3.2, eq. (6.169)*

^cau-c6a-6-1

## The theorem

> [!theorem] Theorem §C6a.6.2: Wick's Theorem
> For free fields at any points $x_1, \dots, x_n$:
> 1. the time-ordered product is the normal-ordered product plus all possible contractions,
>
> $$
> T\{\hat\phi_1\cdots\hat\phi_n\} = \sum_{C}\;\prod_{\{i,j\}\in C}D_F(x_i - x_j)\;:\!\prod_{k\notin\cup C}\hat\phi_k\!: ,
> $$
>
> the sum over all sets $C$ of disjoint pairs of $\{1, \dots, n\}$, including $C = \varnothing$;
> 2. spelled out: the fully normal-ordered term; plus every way of contracting one pair, the remaining $n - 2$ fields normal ordered; plus every way of contracting two pairs, the rest normal ordered; and so on, down to the terms in which every field is contracted, which exist only for $n$ even. For example, the term with the two pairs $\{1,2\}$, $\{3,4\}$ contracted is $D_F(x_1 - x_2)D_F(x_3 - x_4)$, and the term with $\{1,3\}$ contracted is $D_F(x_1 - x_3):\!\prod_{k\ne1,3}\hat\phi_k\!:$.
>
> This is an operator identity, valid in any state.
>
> *Source: PHY 513 Lecture 14, slide 9 ("Wick's Theorem: General Rule") · the user's PHY 513 notes, Ch. 14 §14.2 (Principle "Wick's theorem", eq. (wick); a principle there, a theorem here because it is derived) · PS §4.3, eq. (4.38) · Yu §6.3.1, eq. (6.166)*

^thm-c6a-6-2

> [!derivation]- Derivation
> **Step 1** (both sides are symmetric). For a permutation $\pi$ of the labels:
>
> $$
> T\{\hat\phi_{\pi(1)}\cdots\hat\phi_{\pi(n)}\} = T\{\hat\phi_1\cdots\hat\phi_n\}, \qquad D_F(x_i - x_j) = D_F(x_j - x_i), \qquad :\!\hat\phi_{\pi(1)}\cdots\hat\phi_{\pi(n)}\!: = \,:\!\hat\phi_1\cdots\hat\phi_n\!:
> $$
>
> ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-1|Theorem §C2b.6.1]], 1, for any number of fields: $T$ orders by time labels; [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-2|Theorem §C2b.6.2]]; [[§C6a.5 Normal Ordering and Contractions#^thm-c6a-5-1|Theorem §C6a.5.1]], 3), and $C \mapsto \pi(C)$ maps the sets of disjoint pairs of $\{1, \dots, n\}$ bijectively onto themselves. So both sides of part 1 are unchanged, and it suffices to prove the identity for $x_1^0 \ge x_2^0 \ge \cdots \ge x_n^0$. (Fields at equal times commute, [[§C6a.2 The Interaction Picture#^thm-c6a-2-2|Theorem §C6a.2.2]], 1, so ties do not matter.)
>
> **Step 2** (start). $n = 1$: $T\{\hat\phi_1\} = \hat\phi_1 = \,:\!\hat\phi_1\!:$. $n = 2$: [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-6|Theorem §C2b.6.6]].
>
> **Step 3** (peel off the earliest field). With the times ordered, $T\{\hat\phi_1\cdots\hat\phi_n\} = \hat\phi_1\cdots\hat\phi_n = T\{\hat\phi_1\cdots\hat\phi_{n-1}\}\,\hat\phi_n$.
>
> **Step 4** (induction hypothesis). Assume the theorem for $n - 1$ fields:
>
> $$
> T\{\hat\phi_1\cdots\hat\phi_n\} = \sum_{C'}\;\prod_{\{i,j\}\in C'}D_F(x_i - x_j)\;:\!\prod_{k\in R(C')}\hat\phi_k\!:\;\hat\phi_n ,
> $$
>
> $C'$ over the sets of disjoint pairs of $\{1, \dots, n-1\}$, $R(C')$ the uncontracted indices.
>
> **Step 5** (apply the lemma term by term). $x_n^0 \le x_k^0$ for all $k$, so [[§C6a.6 Wick's Theorem#^lem-c6a-6-1|Lemma §C6a.6.1]], 2, gives for each $C'$
>
> $$
> \prod_{C'}D_F\;\Bigl[:\!\prod_{k\in R(C')}\hat\phi_k\,\hat\phi_n\!: + \sum_{l\in R(C')}D_F(x_l - x_n)\,:\!\prod_{k\in R(C'),\,k\ne l}\hat\phi_k\!:\Bigr] .
> $$
>
> **Step 6** (each term exactly once). Every set $C$ of disjoint pairs of $\{1, \dots, n\}$ is of exactly one of two kinds: $n$ uncontracted, $C = C'$ with $C'$ a set of pairs of $\{1, \dots, n-1\}$, which is the first term of Step 5; or $n$ paired with some $l$, $C = C'\cup\{\{l, n\}\}$ with $l \notin\cup C'$, which is the $l$-term of the sum in Step 5. Conversely each term of Step 5 is of one of these forms for exactly one $C$. So Step 5 summed over $C'$ is the right side of part 1 for $n$ fields.
>
> **Step 7** (the case $n = 3$ written out). With $\overbracket{\hat\phi_i\hat\phi_j} = D_F(x_i - x_j)$ ([[§C6a.5 Normal Ordering and Contractions#^def-c6a-5-1|Def. §C6a.5.1]]) and $x_1^0 \ge x_2^0 \ge x_3^0$: the induction hypothesis for $\{1, 2\}$ has $C' = \varnothing$ and $C' = \{\{1,2\}\}$, and the lemma acts on each:
>
> $$
> \begin{aligned}
> T\{\hat\phi_1\hat\phi_2\hat\phi_3\} = T\{\hat\phi_1\hat\phi_2\}\,\hat\phi_3 &= \bigl(:\!\hat\phi_1\hat\phi_2\!:\, + \overbracket{\hat\phi_1\hat\phi_2}\bigr)\,\hat\phi_3\\
> &= \underbrace{:\!\hat\phi_1\hat\phi_2\hat\phi_3\!:}_{C = \varnothing} + \underbrace{\overbracket{\hat\phi_1\hat\phi_3}:\!\hat\phi_2\!:}_{C = \{13\}} + \underbrace{\overbracket{\hat\phi_2\hat\phi_3}:\!\hat\phi_1\!:}_{C = \{23\}} \quad\text{(from } C' = \varnothing\text{)}\\
> &\quad + \underbrace{\overbracket{\hat\phi_1\hat\phi_2}:\!\hat\phi_3\!:}_{C = \{12\}} \quad\text{(from } C' = \{12\}\text{, no } l \text{ left)} ,
> \end{aligned}
> $$
>
> the four sets of disjoint pairs of $\{1, 2, 3\}$, each once ($1 + 3 = 4$ terms).
>
> ⚑ By-product: the number of terms is $\sum_k\binom n{2k}(2k - 1)!!$ (choose the $2k$ contracted fields, then pair them, [[§CA.7 Pairings, Diagrams and Symmetry Factors#^thm-ca-7-1|Theorem §CA.7.1]]); for $n = 4$: $1 + 6 + 3 = 10$ ([[§C6a.6 Wick's Theorem#^ex-c6a-6-1|Example §C6a.6.1]]).
>
> **What the derivation shows.**
> - "It's just an induction proof" (the lecture): messy on a blackboard, but the only input is that each reordering costs a number, $D_W$, and that time ordering makes it $D_F$.
> - The order in which the field is added matters only through the lemma's time condition; the result is symmetric.
> - Used next: vacuum expectation values (Theorem §C6a.6.3).

^der-c6a-6-2

*Uses:* [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-1|Theorem §C2b.6.1]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-2|Theorem §C2b.6.2]], [[§C6a.5 Normal Ordering and Contractions#^thm-c6a-5-1|Theorem §C6a.5.1]], [[§C6a.2 The Interaction Picture#^thm-c6a-2-2|Theorem §C6a.2.2]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-6|Theorem §C2b.6.6]], [[§C6a.6 Wick's Theorem#^lem-c6a-6-1|Lemma §C6a.6.1]]

> [!derivation]- Derivation (second route: prepending the latest field, PS)
> This is the proof of PS §4.3, eq. (4.41), filled in as in the user's notes ("Proof by induction (filled in)").
>
> **Step 1** (order). As in Step 1 above, assume $x_1^0 \ge x_2^0 \ge \cdots \ge x_n^0$. Then $\hat\phi_1$ stands to the left: $T\{\hat\phi_1\cdots\hat\phi_n\} = \hat\phi_1\,T\{\hat\phi_2\cdots\hat\phi_n\}$, and by the induction hypothesis
>
> $$
> T\{\hat\phi_1\cdots\hat\phi_n\} = (\hat\phi_1^- + \hat\phi_1^+)\sum_{C'}\prod_{C'}D_F\;:\!\prod_{k\in R(C')}\hat\phi_k\!: ,
> $$
>
> $C'$ over the sets of disjoint pairs of $\{2, \dots, n\}$.
>
> **Step 2** ($\hat\phi_1^-$). It already stands to the left, where normal order wants it: $\hat\phi_1^-\,:\!\prod_{R}\hat\phi_k\!: = \,:\!\hat\phi_1^-\prod_R\hat\phi_k\!:$ (each term of [[§C6a.5 Normal Ordering and Contractions#^thm-c6a-5-1|Theorem §C6a.5.1]], 1, keeps its $\hat\phi^-$'s on the left).
>
> **Step 3** ($\hat\phi_1^+$). It must be moved to the right through the normal-ordered product. It commutes with every $\hat\phi^+$ and with each $\hat\phi_k^-$ it leaves the number $[\hat\phi_1^+, \hat\phi_k^-] = D_W(x_1 - x_k)$ ([[§C6a.5 Normal Ordering and Contractions#^thm-c6a-5-2|Theorem §C6a.5.2]]). The commutator is a derivation, and resumming over the subsets as in Step 5 of [[§C6a.6 Wick's Theorem#^der-c6a-6-1|Derivation §C6a.6.1]],
>
> $$
> \hat\phi_1^+\,:\!\prod_{k\in R}\hat\phi_k\!: = \,:\!\prod_{k\in R}\hat\phi_k\!:\,\hat\phi_1^+ + \sum_{l\in R}D_W(x_1 - x_l)\,:\!\prod_{k\in R,\,k\ne l}\hat\phi_k\!: .
> $$
>
> The first term is $:\!\hat\phi_1^+\prod_R\hat\phi_k\!:$ (a $\hat\phi^+$ on the right is in order).
>
> **Step 4** (latest time). $x_1^0 \ge x_l^0$, so $D_W(x_1 - x_l) = D_F(x_1 - x_l)$ (as in Step 6 of Derivation §C6a.6.1).
>
> **Step 5** (collect). Steps 2 and 3 add to $:\!\hat\phi_1\prod_R\hat\phi_k\!:$; the sum of Step 3 contracts $\hat\phi_1$ with each uncontracted field. Contractions among $2, \dots, n$ came from the induction hypothesis and ride along; those involving $\hat\phi_1$ come from the commutators. Each set of pairs of $\{1, \dots, n\}$ appears once (the bijection of Step 6 above, with $1$ in place of $n$). For $n = 3$, with $\overbracket{\hat\phi_i\hat\phi_j} = D_F(x_i - x_j)$:
>
> $$
> \begin{aligned}
> T\{\hat\phi_1\hat\phi_2\hat\phi_3\} &= (\hat\phi_1^- + \hat\phi_1^+)\bigl(:\!\hat\phi_2\hat\phi_3\!:\, + \overbracket{\hat\phi_2\hat\phi_3}\bigr)\\
> &= \underbrace{:\!\hat\phi_1^-\hat\phi_2\hat\phi_3\!: + :\!\hat\phi_1^+\hat\phi_2\hat\phi_3\!:}_{:\hat\phi_1\hat\phi_2\hat\phi_3:} + \overbracket{\hat\phi_1\hat\phi_2}:\!\hat\phi_3\!: + \overbracket{\hat\phi_1\hat\phi_3}:\!\hat\phi_2\!: + \overbracket{\hat\phi_2\hat\phi_3}\underbrace{(\hat\phi_1^- + \hat\phi_1^+)}_{:\hat\phi_1:} ,
> \end{aligned}
> $$
>
> the two middle terms from $\hat\phi_1^+:\!\hat\phi_2\hat\phi_3\!: = \,:\!\hat\phi_2\hat\phi_3\!:\hat\phi_1^+ + D_W(x_1 - x_2):\!\hat\phi_3\!: + D_W(x_1 - x_3):\!\hat\phi_2\!:$ (Step 3) and Step 4.
>
> **What the derivation shows.**
> - PS move the *latest* field to the right through the rest; Yu and slide 9 append the *earliest* field and move its $\hat\phi^-$ to the left. Both pay one $D_W$ per misplaced pair, which the extreme time turns into $D_F$.

^der-c6a-6-2b

> [!example] Example §C6a.6.1: Four Fields
> For four fields, Wick's theorem ([[§C6a.6 Wick's Theorem#^thm-c6a-6-2|Theorem §C6a.6.2]]) has $1 + 6 + 3 = 10$ terms. With the bracket $\overbracket{\hat\phi_i\hat\phi_j} = D_F(x_i - x_j) \equiv D_{ij}$ ([[§C6a.5 Normal Ordering and Contractions#^def-c6a-5-1|Def. §C6a.5.1]]; inside $:\;:$ the fields may be reordered, [[§C6a.5 Normal Ordering and Contractions#^thm-c6a-5-1|Theorem §C6a.5.1]], 3, so each contracted pair is written side by side):
>
> $$
> \begin{aligned}
> T\{\hat\phi_1\hat\phi_2\hat\phi_3\hat\phi_4\} ={}& :\!\hat\phi_1\hat\phi_2\hat\phi_3\hat\phi_4\!: &&\text{no pair: } 1\text{ term}\\
> &+ \overbracket{\hat\phi_1\hat\phi_2}:\!\hat\phi_3\hat\phi_4\!: + \overbracket{\hat\phi_1\hat\phi_3}:\!\hat\phi_2\hat\phi_4\!: + \overbracket{\hat\phi_1\hat\phi_4}:\!\hat\phi_2\hat\phi_3\!: &&\text{one pair: } \tbinom42 = 6\text{ terms}\\
> &+ \overbracket{\hat\phi_2\hat\phi_3}:\!\hat\phi_1\hat\phi_4\!: + \overbracket{\hat\phi_2\hat\phi_4}:\!\hat\phi_1\hat\phi_3\!: + \overbracket{\hat\phi_3\hat\phi_4}:\!\hat\phi_1\hat\phi_2\!:\\
> &+ \overbracket{\hat\phi_1\hat\phi_2}\,\overbracket{\hat\phi_3\hat\phi_4} + \overbracket{\hat\phi_1\hat\phi_3}\,\overbracket{\hat\phi_2\hat\phi_4} + \overbracket{\hat\phi_1\hat\phi_4}\,\overbracket{\hat\phi_2\hat\phi_3} &&\text{two pairs: } 3!! = 3\text{ terms}\\
> ={}& :\!\hat\phi_1\hat\phi_2\hat\phi_3\hat\phi_4\!:\\
> &+ D_{12}:\!\hat\phi_3\hat\phi_4\!: + D_{13}:\!\hat\phi_2\hat\phi_4\!: + D_{14}:\!\hat\phi_2\hat\phi_3\!: + D_{23}:\!\hat\phi_1\hat\phi_4\!: + D_{24}:\!\hat\phi_1\hat\phi_3\!: + D_{34}:\!\hat\phi_1\hat\phi_2\!:\\
> &+ D_{12}D_{34} + D_{13}D_{24} + D_{14}D_{23} .
> \end{aligned}
> $$
>
> The six pairs are $\{1,2\}, \{1,3\}, \{1,4\}, \{2,3\}, \{2,4\}, \{3,4\}$, and the three ways of splitting four fields into two pairs are $\{12\}\{34\}$, $\{13\}\{24\}$, $\{14\}\{23\}$ ([[§CA.7 Pairings, Diagrams and Symmetry Factors#^thm-ca-7-1|Theorem §CA.7.1]]). On the slides and in PS (eq. (4.39)) the brackets are drawn over the fields in their written order; the figure below draws them so.
>
> *Source: PHY 513 Lecture 14, slide 10 ("One contraction: $D_F(x_1 - x_2)N(\phi_3\phi_4) + \dots$ (6 terms total). Two contractions: $D_F(x_1 - x_2)D_F(x_3 - x_4) + \dots$ (3 terms total)") · the user's PHY 513 notes, Ch. 14 §14.2 (Derivation "Four fields") · PS §4.3, eq. (4.39) · Yu §6.3.1, eq. (6.167)*

^ex-c6a-6-1

![[ph-qft-c6-6-1.svg]]
*Wick's theorem for four fields as on slide 10 and in PS eq. (4.39): a bracket over a pair is its contraction $D_F(x_i - x_j)$, the rest normal ordered ($N(\cdots)$ = the colons of these notes). Top: no contraction; middle: the six one-pair terms; bottom: the three complete contractions $(12)(34)$, $(13)(24)$, $(14)(23)$, with brackets of different heights where pairs cross or nest. Added figure.*

> [!remark] Remark: Contracting several pairs
> Asked in the lecture: does "contracting two pairs" simply mean two Feynman propagators? Yes. Each contraction is a $D_F$, so a term with two contractions is a product of two $D_F$'s times the normal-ordered product of the remaining fields; the contracted pairs need not be adjacent in the written product ($D_{13}:\!\hat\phi_2\hat\phi_4\!:$ in [[§C6a.6 Wick's Theorem#^ex-c6a-6-1|Example §C6a.6.1]]; PS p. 89: "When the contraction symbol connects two operators that are not adjacent, we still define it to give a factor of $D_F$").
>
> *Source: PHY 513 Lecture 14, slide 10, and transcript · the user's PHY 513 notes, Ch. 14 §14.2 · PS §4.3, p. 89*

^rem-c6a-6-1

## Vacuum expectation values

> [!theorem] Theorem §C6a.6.3: Free Vacuum Values Are Sums over Pairings
> For free fields at points $x_1, \dots, x_n$,
>
> $$
> \langle0|T\{\hat\phi_1\cdots\hat\phi_n\}|0\rangle = \sum_{P\in\mathcal P(\{1,\dots,n\})}\;\prod_{\{i,j\}\in P}D_F(x_i - x_j) ,
> $$
>
> the sum over all pairings of the $n$ fields ([[§CA.7 Pairings, Diagrams and Symmetry Factors#^def-ca-7-1|Def. §CA.7.1]]), the "complete contractions". It has $(n - 1)!!$ terms for $n$ even (3, 15, 105 for $n = 4, 6, 8$) and is zero for $n$ odd.
>
> *Source: PHY 513 Lecture 14, slide 10 ("$\langle0|T(\phi_1\dots\phi_n)|0\rangle$ = all complete contractions") · the user's PHY 513 notes, Ch. 14 §14.2 (Principle "Vacuum expectation values: complete contractions", eq. (wickvev)) · PS §4.3, eq. (4.40) · Yu §6.3.1, eq. (6.168); §10.5.1, after eq. (10.187) ("完全缩并", complete contraction)*

^thm-c6a-6-3

> [!derivation]- Derivation
> **Step 1** (Wick: time order → normal order plus contractions). [[§C6a.6 Wick's Theorem#^thm-c6a-6-2|Theorem §C6a.6.2]], 1, with $\overbracket{\hat\phi_i\hat\phi_j} = D_F(x_i - x_j)$ ([[§C6a.5 Normal Ordering and Contractions#^def-c6a-5-1|Def. §C6a.5.1]]), sorted by the number $k$ of contracted pairs:
>
> $$
> T\{\hat\phi_1\cdots\hat\phi_n\} = \,:\!\hat\phi_1\cdots\hat\phi_n\!:\, + \sum_{\{i,j\}}\overbracket{\hat\phi_i\hat\phi_j}\,:\!\prod_{k\ne i,j}\hat\phi_k\!:\, + \sum_{\{i,j\},\{k,l\}}\overbracket{\hat\phi_i\hat\phi_j}\,\overbracket{\hat\phi_k\hat\phi_l}\,:\!\cdots\!:\, + \cdots ,
> $$
>
> with $\binom n2$ one-pair terms, $\frac12\binom n2\binom{n-2}2$ two-pair terms, and so on.
>
> **Step 2** (take the vacuum value; normal-ordered remainders vanish). The contractions are numbers and come out of $\langle0|\cdots|0\rangle$; every remainder with $r \ge 1$ fields vanishes ([[§C6a.5 Normal Ordering and Contractions#^thm-c6a-5-1|Theorem §C6a.5.1]], 2):
>
> $$
> \langle0|:\!\hat\phi_1\cdots\hat\phi_n\!:|0\rangle = 0, \qquad \overbracket{\hat\phi_i\hat\phi_j}\,\langle0|:\!\textstyle\prod_{k\ne i,j}\hat\phi_k\!:|0\rangle = 0 \ (n > 2), \qquad \dots, \qquad \Bigl(\prod_{\{i,j\}\in C}\overbracket{\hat\phi_i\hat\phi_j}\Bigr)\langle0|:\!\textstyle\prod_{k\notin\cup C}\hat\phi_k\!:|0\rangle = 0 \ (r \ge 1) .
> $$
>
> Only the terms with every field contracted survive, and for them the remainder is the empty product, $:\;: = \mathbf 1$, with $\langle0|\mathbf 1|0\rangle = 1$:
>
> $$
> \langle0|T\{\hat\phi_1\cdots\hat\phi_n\}|0\rangle = \sum_{C\text{ covering }\{1,\dots,n\}}\;\prod_{\{i,j\}\in C}\overbracket{\hat\phi_i\hat\phi_j} = \sum_{C\text{ covering }\{1,\dots,n\}}\;\prod_{\{i,j\}\in C}D_F(x_i - x_j) .
> $$
>
> **Step 3** (these are the pairings). A set of disjoint pairs covering all of $\{1, \dots, n\}$ is a pairing ([[§CA.7 Pairings, Diagrams and Symmetry Factors#^def-ca-7-1|Def. §CA.7.1]]). A set $C$ of $k$ pairs leaves $r = n - 2k$ fields; for $n$ odd, $r$ is odd, so $r \ge 1$ for every $C$ and every term vanishes. For $n$ even their number is $(n - 1)!!$ ([[§CA.7 Pairings, Diagrams and Symmetry Factors#^thm-ca-7-1|Theorem §CA.7.1]]): $n = 4$, the three of [[§C6a.6 Wick's Theorem#^ex-c6a-6-2|Example §C6a.6.2]]; $n = 6$, the fifteen listed in [[§C6a.7 Feynman Diagrams for Correlation Functions#^der-c6a-7-1|Derivation §C6a.7.1]].
>
> ⚑ By-product: for $n$ odd "there is always a field left over, too many $\hat a$'s or too many $\hat a^\dagger$'s" (the lecture) — the operator reason behind the counting reason.
>
> **What the derivation shows.**
> - Every free correlator is fixed by the two-point function $D_F$; the work of perturbation theory is combinatorics.
> - Used next: Feynman diagrams ([[§C6a.7 Feynman Diagrams for Correlation Functions|§C6a.7]]).

^der-c6a-6-3

*Uses:* [[§C6a.6 Wick's Theorem#^thm-c6a-6-2|Theorem §C6a.6.2]], [[§C6a.5 Normal Ordering and Contractions#^thm-c6a-5-1|Theorem §C6a.5.1]], [[§CA.7 Pairings, Diagrams and Symmetry Factors#^thm-ca-7-1|Theorem §CA.7.1]]

![[ph-qft-ca-7-2.svg]]
*Pairings ([[§CA.7 Pairings, Diagrams and Symmetry Factors#^def-ca-7-1|Def. §CA.7.1]]) drawn as arcs. (a) The three pairings of four points. (b) The step of the proof of [[§CA.7 Pairings, Diagrams and Symmetry Factors#^thm-ca-7-1|Theorem §CA.7.1]]: the partner of the first point has $2k-1$ choices, and the remaining $2k-2$ points are paired in $(2k-3)!!$ ways, here $5\cdot3 = 15$. (c) An odd set has no pairing. Each pairing is one term of a free vacuum value (Theorem §C6a.6.3).*

> [!example] Example §C6a.6.2: The Free Four-Point Function
> Write $\overbracket{\hat\phi_i\hat\phi_j} = D_F(x_i - x_j) \equiv D_{ij}$ ([[§C6a.5 Normal Ordering and Contractions#^def-c6a-5-1|Def. §C6a.5.1]]).
>
> **Step 1** (time order → normal order plus contractions). By Wick's theorem ([[§C6a.6 Wick's Theorem#^thm-c6a-6-2|Theorem §C6a.6.2]]; the ten terms of [[§C6a.6 Wick's Theorem#^ex-c6a-6-1|Example §C6a.6.1]]),
>
> $$
> \begin{aligned}
> T\{\hat\phi_1\hat\phi_2\hat\phi_3\hat\phi_4\} ={}& :\!\hat\phi_1\hat\phi_2\hat\phi_3\hat\phi_4\!: &&\text{no pair: 1 term}\\
> &+ \overbracket{\hat\phi_1\hat\phi_2}:\!\hat\phi_3\hat\phi_4\!: + \overbracket{\hat\phi_1\hat\phi_3}:\!\hat\phi_2\hat\phi_4\!: + \overbracket{\hat\phi_1\hat\phi_4}:\!\hat\phi_2\hat\phi_3\!: &&\text{one pair: 6 terms}\\
> &+ \overbracket{\hat\phi_2\hat\phi_3}:\!\hat\phi_1\hat\phi_4\!: + \overbracket{\hat\phi_2\hat\phi_4}:\!\hat\phi_1\hat\phi_3\!: + \overbracket{\hat\phi_3\hat\phi_4}:\!\hat\phi_1\hat\phi_2\!:\\
> &+ \overbracket{\hat\phi_1\hat\phi_2}\,\overbracket{\hat\phi_3\hat\phi_4} + \overbracket{\hat\phi_1\hat\phi_3}\,\overbracket{\hat\phi_2\hat\phi_4} + \overbracket{\hat\phi_1\hat\phi_4}\,\overbracket{\hat\phi_2\hat\phi_3} . &&\text{two pairs: 3 terms}
> \end{aligned}
> $$
>
> **Step 2** (take the vacuum value term by term). $\langle0|\cdots|0\rangle$ is linear and the brackets are numbers, so they come out:
>
> $$
> \begin{aligned}
> \langle0|T\{\hat\phi_1\hat\phi_2\hat\phi_3\hat\phi_4\}|0\rangle ={}& \langle0|:\!\hat\phi_1\hat\phi_2\hat\phi_3\hat\phi_4\!:|0\rangle + \overbracket{\hat\phi_1\hat\phi_2}\,\langle0|:\!\hat\phi_3\hat\phi_4\!:|0\rangle + \dots + \overbracket{\hat\phi_3\hat\phi_4}\,\langle0|:\!\hat\phi_1\hat\phi_2\!:|0\rangle\\
> &+ \bigl(\overbracket{\hat\phi_1\hat\phi_2}\,\overbracket{\hat\phi_3\hat\phi_4} + \overbracket{\hat\phi_1\hat\phi_3}\,\overbracket{\hat\phi_2\hat\phi_4} + \overbracket{\hat\phi_1\hat\phi_4}\,\overbracket{\hat\phi_2\hat\phi_3}\bigr)\langle0|0\rangle .
> \end{aligned}
> $$
>
> **Step 3** (the normal-ordered terms vanish). Split each field, $\hat\phi_i = \hat\phi_i^+ + \hat\phi_i^-$, with $\hat\phi^+|0\rangle = 0$ and $\langle0|\hat\phi^- = 0$ ([[§C2b.1 Heisenberg Fields#^thm-c2b-1-5|Theorem §C2b.1.5]]). For two fields the normal-ordered product has four terms, each with the $+$ parts on the right ([[§C6a.5 Normal Ordering and Contractions#^thm-c6a-5-1|Theorem §C6a.5.1]], 1):
>
> $$
> \langle0|:\!\hat\phi_k\hat\phi_l\!:|0\rangle = \langle0|\bigl(\hat\phi_k^+\hat\phi_l^+ + \hat\phi_k^-\hat\phi_l^+ + \hat\phi_l^-\hat\phi_k^+ + \hat\phi_k^-\hat\phi_l^-\bigr)|0\rangle = 0 + 0 + 0 + 0 :
> $$
>
> the first three end in a $\hat\phi^+$ acting on $|0\rangle$, the last begins with a $\hat\phi^-$ acting on $\langle0|$. The same holds for each of the $2^4 = 16$ terms of $:\!\hat\phi_1\hat\phi_2\hat\phi_3\hat\phi_4\!:$, so all seven normal-ordered terms of Step 2 vanish ([[§C6a.5 Normal Ordering and Contractions#^thm-c6a-5-1|Theorem §C6a.5.1]], 2).
>
> **Step 4** (the complete contractions survive). With $\langle0|0\rangle = 1$, each bracket replaced by its $D_F$:
>
> $$
> \begin{aligned}
> \langle0|T\{\hat\phi_1\hat\phi_2\hat\phi_3\hat\phi_4\}|0\rangle &= \overbracket{\hat\phi_1\hat\phi_2}\,\overbracket{\hat\phi_3\hat\phi_4} + \overbracket{\hat\phi_1\hat\phi_3}\,\overbracket{\hat\phi_2\hat\phi_4} + \overbracket{\hat\phi_1\hat\phi_4}\,\overbracket{\hat\phi_2\hat\phi_3}\\
> &= D_F(x_1 - x_2)D_F(x_3 - x_4) + D_F(x_1 - x_3)D_F(x_2 - x_4) + D_F(x_1 - x_4)D_F(x_2 - x_3) ,
> \end{aligned}
> $$
>
> one term for each of the $3!! = 3$ pairings of $\{1, 2, 3, 4\}$ ([[§CA.7 Pairings, Diagrams and Symmetry Factors#^thm-ca-7-1|Theorem §CA.7.1]]).
>
> **Step 5** (three fields). For $n = 3$ Wick's theorem has $1 + 3 = 4$ terms, each keeping at least one field inside the colons:
>
> $$
> T\{\hat\phi_1\hat\phi_2\hat\phi_3\} = \,:\!\hat\phi_1\hat\phi_2\hat\phi_3\!:\, + \overbracket{\hat\phi_1\hat\phi_2}\,(\hat\phi_3^+ + \hat\phi_3^-) + \overbracket{\hat\phi_1\hat\phi_3}\,(\hat\phi_2^+ + \hat\phi_2^-) + \overbracket{\hat\phi_2\hat\phi_3}\,(\hat\phi_1^+ + \hat\phi_1^-) ,
> $$
>
> and $\langle0|(\hat\phi_k^+ + \hat\phi_k^-)|0\rangle = 0 + 0$, $\langle0|:\!\hat\phi_1\hat\phi_2\hat\phi_3\!:|0\rangle = 0$ as in Step 3, so $\langle0|T\{\hat\phi_1\hat\phi_2\hat\phi_3\}|0\rangle = 0$.
>
> (The user's notes check both on an operator model, a lattice field with three Fock-space modes.)
>
> *Source: PHY 513 Lecture 14, slide 10 · PS §4.3, eq. (4.40) · Yu §6.3.1, eq. (6.168) · the user's PHY 513 notes, Ch. 14 §14.2 (numerical check)*

^ex-c6a-6-2

> [!remark] Remark: Theorem and application
> Wick's theorem is the operator statement ([[§C6a.6 Wick's Theorem#^thm-c6a-6-2|Theorem §C6a.6.2]]), valid in any state; "the theorem itself is a little bit stronger because it tells us about the field without having put it in a particular state." The application in this course is almost always the vacuum value ([[§C6a.6 Wick's Theorem#^thm-c6a-6-3|Theorem §C6a.6.3]]): "the reason to introduce normal order was because it was really easy to take it in the vacuum state." The full operator form is used when the states are not the vacuum, as for scattering states (QFT C10, planned).
>
> *Source: PHY 513 Lecture 14, transcript · the user's PHY 513 notes, Ch. 14 §14.2 (paragraph "Theorem and application")*

^rem-c6a-6-2

> [!caution] Caution: In what sense Wick's theorem holds
> Both sides of [[§C6a.6 Wick's Theorem#^thm-c6a-6-2|Theorem §C6a.6.2]] are operator-valued distributions in $(x_1, \dots, x_n)$. The identity holds after smearing every point with a test function, at distinct points ([[§C6a.5 Normal Ordering and Contractions#^cau-c6a-5-3|§C6a.5, Caution: In what sense these identities hold]]). The time-ordered product at distinct points with equal times is fixed by the equal-time commutation of the fields ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-1|Theorem §C2b.6.1]], 2). Perturbation theory applies the theorem to products in which several fields sit at the same point, the four fields of a vertex:
>
> $$
> T\{\hat\phi_x\hat\phi_y\,\hat\phi_I(z)^4\} \ni \overbracket{\hat\phi_x\hat\phi_y}\;\overbracket{\hat\phi_{z_1}\hat\phi_{z_2}}\;\overbracket{\hat\phi_{z_3}\hat\phi_{z_4}}\Big|_{z_a = z} = D_F(x - y)\,D_F(0)^2 .
> $$
>
> The contractions among them, $D_F(0)$, are then formal symbols for a divergent quantity (§C6a.5, Caution, item 2), made finite only in a regularized theory ([[§C6a.10 Feynman Rules in Momentum Space#^rem-c6a-10-1|§C6a.10, Remark: The first ultraviolet divergence]]).
>
> *Source: written here*

^cau-c6a-6-2

> [!theorem]- ★ Theorem §C6a.6.4: Wick's Theorem for Ordinary Products
> For free fields at any points $x_1, \dots, x_n$, with no time ordering,
>
> $$
> \hat\phi_1\cdots\hat\phi_n = \sum_C\;\prod_{\{i<j\}\in C}D_W(x_i - x_j)\;:\!\prod_{k\notin\cup C}\hat\phi_k\!:, \qquad \langle0|\hat\phi_1\cdots\hat\phi_n|0\rangle = \sum_P\;\prod_{\{i<j\}\in P}D_W(x_i - x_j) ,
> $$
>
> $C$ over the sets of disjoint pairs, $P$ over the pairings ([[§CA.7 Pairings, Diagrams and Symmetry Factors#^def-ca-7-1|Def. §CA.7.1]]), each pair with the earlier-written field first. Since $D_W(-\xi) = \overline{D_W(\xi)} \ne D_W(\xi)$ in general ([[§C2b.2 The Wightman Function#^thm-c2b-2-4|Theorem §C2b.2.4]]), the order inside each pair matters, unlike for $D_F$. Every Wightman function of the free field is fixed by $D_W$ ([[§C2b.2 The Wightman Function#^def-c2b-2-1|Def. §C2b.2.1]]). Beyond the course.
>
> *Source: written here (the induction of Theorem §C6a.6.2 with the lemma's ⚑ by-product)*

^thm-c6a-6-4

> [!derivation]- Derivation
> **Step 1** (the lemma without the time condition). Steps 1–5 of [[§C6a.6 Wick's Theorem#^der-c6a-6-1|Derivation §C6a.6.1]] never used the times (its ⚑ by-product):
>
> $$
> :\!\hat\phi_1\cdots\hat\phi_{n-1}\!:\,\hat\phi_n = \,:\!\hat\phi_1\cdots\hat\phi_n\!:\, + \sum_{k=1}^{n-1}D_W(x_k - x_n)\,:\!\prod_{i\ne k,\,n}\hat\phi_i\!: ,
> $$
>
> and the same with earlier $c$-number factors riding along (Step 7 there).
>
> **Step 2** (start). $n = 1$: $\hat\phi_1 = \,:\!\hat\phi_1\!:$. $n = 2$: Step 1 with $n = 2$, $\hat\phi_1\hat\phi_2 = \,:\!\hat\phi_1\hat\phi_2\!:\, + D_W(x_1 - x_2)$ ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-6|Theorem §C2b.6.6]]).
>
> **Step 3** (induction). Assume the statement for $n - 1$ fields and multiply by $\hat\phi_n$ on the right:
>
> $$
> \hat\phi_1\cdots\hat\phi_n = \sum_{C'}\prod_{\{i<j\}\in C'}D_W(x_i - x_j)\;:\!\prod_{k\in R(C')}\hat\phi_k\!:\;\hat\phi_n = \sum_{C'}\prod_{C'}D_W\Bigl[:\!\prod_{k\in R(C')}\hat\phi_k\,\hat\phi_n\!: + \sum_{l\in R(C')}D_W(x_l - x_n)\,:\!\prod_{k\in R(C'),\,k\ne l}\hat\phi_k\!:\Bigr] ,
> $$
>
> $C'$ over the sets of disjoint pairs of $\{1, \dots, n - 1\}$, $R(C')$ the uncontracted indices. Every new pair is $\{l, n\}$ with $l < n$ and carries $D_W(x_l - x_n)$, the earlier-written field first. Each set $C$ of pairs of $\{1, \dots, n\}$ appears exactly once (the bijection of Step 6 of [[§C6a.6 Wick's Theorem#^der-c6a-6-2|Derivation §C6a.6.2]]).
>
> **Step 4** ($n = 3$ written out). Step 3 from $\hat\phi_1\hat\phi_2 = \,:\!\hat\phi_1\hat\phi_2\!:\, + D_W(x_1 - x_2)$:
>
> $$
> \hat\phi_1\hat\phi_2\hat\phi_3 = \,:\!\hat\phi_1\hat\phi_2\hat\phi_3\!:\, + D_W(x_1 - x_3):\!\hat\phi_2\!: + D_W(x_2 - x_3):\!\hat\phi_1\!: + D_W(x_1 - x_2):\!\hat\phi_3\!: .
> $$
>
> **Step 5** (vacuum value). $\langle0|:\!\cdots\!:|0\rangle = 0$ for a nonempty remainder ([[§C6a.5 Normal Ordering and Contractions#^thm-c6a-5-1|Theorem §C6a.5.1]], 2), so only the pairings survive. For $n = 4$:
>
> $$
> \langle0|\hat\phi_1\hat\phi_2\hat\phi_3\hat\phi_4|0\rangle = D_W(x_1 - x_2)D_W(x_3 - x_4) + D_W(x_1 - x_3)D_W(x_2 - x_4) + D_W(x_1 - x_4)D_W(x_2 - x_3) .
> $$
>
> **What the derivation shows.**
> - Time ordering is needed only to turn each $D_W$ into the even $D_F$. Without it the same combinatorics hold, but each pair remembers which field stood to the left.

^der-c6a-6-4

*Uses:* [[§C6a.6 Wick's Theorem#^der-c6a-6-1|Derivation §C6a.6.1]], [[§C6a.6 Wick's Theorem#^der-c6a-6-2|Derivation §C6a.6.2]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-6|Theorem §C2b.6.6]], [[§C6a.5 Normal Ordering and Contractions#^thm-c6a-5-1|Theorem §C6a.5.1]], [[§C2b.2 The Wightman Function#^thm-c2b-2-4|Theorem §C2b.2.4]], [[§CA.7 Pairings, Diagrams and Symmetry Factors#^def-ca-7-1|Def. §CA.7.1]]

> [!remark] Remark: Yu's route
> Yu §6.3 treats boson and fermion fields together, with a sign $\epsilon_{ab}$ for every exchange of two fermion fields (eqs. (6.140)–(6.143), (6.155), (6.163)), and defines the contraction as the vacuum expectation value of the time-ordered product (6.161), which equals PS's commutator definition (4.35). He proves the lemma ([[§C6a.6 Wick's Theorem#^lem-c6a-6-1|Lemma §C6a.6.1]]) in four steps: the $\Phi_b^{(+)}$ part (6.171)–(6.172); an induction over the positive-frequency factors (6.175)–(6.181); the general term (6.182)–(6.185); prior contractions (6.170). The theorem then follows by induction for $x_1^0 \ge \cdots \ge x_n^0$ (6.186)–(6.190) and, for any order, by exchanging fields in $T$ and $\mathsf N$ alike, which produces the same sign on both sides (6.191)–(6.193). Slide 9 follows Yu's direction (append the earliest field); PS (4.41) prepend the latest. Fermionic Wick contractions, with their signs, enter with QED (QFT C7, planned).
>
> *Source: Yu §6.3.1–§6.3.2, pp. 218–227 · PS §4.3, p. 90 · PHY 513 Lecture 14, slide 9*

^rem-c6a-6-3

> [!remark]- Connections
> - The vacuum value of Wick's theorem has the form of the moment formula of a Gaussian: free fields are Gaussian, with covariance $D_F$, and in the path integral this is literal — [[§CA.7 Pairings, Diagrams and Symmetry Factors#^rem-ca-7-1|§CA.7, ★ Remark: The same sum is the moment formula of a Gaussian]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^rem-c2b-6-4|§C2b.6, Remark: Preview: the propagator as a Gaussian covariance]].
> - At coincident points the two-field case produced the zero-point energy; at a vertex of $\phi^4$ theory the same coincident contractions produce the first loops — [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-8|Theorem §C2b.6.8]], [[§C6a.7 Feynman Diagrams for Correlation Functions#^thm-c6a-7-1|Theorem §C6a.7.1]].
> - The inputs of the theorem in perturbation theory are the terms of the Dyson series, products of free fields with four at each interaction point — [[§C6a.3 The Time-Evolution Operator and Time Ordering#^ex-c6a-3-1|Example §C6a.3.1]], [[§C6a.4 The Interacting Vacuum and the Two-Point Function#^thm-c6a-4-7|Theorem §C6a.4.7]].
> - In the non-relativistic many-body problem the same theorem, for ladder operators, organizes perturbation theory around a Fermi sea or a condensate — [[§C12.2★ Second Quantization|QM §C12.2★]].
