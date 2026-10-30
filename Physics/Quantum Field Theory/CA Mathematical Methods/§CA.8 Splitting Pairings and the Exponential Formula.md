---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: CA
section: CA.8
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§CA.7 Pairings, Diagrams and Symmetry Factors]] · ↑ [[· CA Mathematical Methods]]

*Sources: the user's PHY 513 notes, Ch. 14 §14.7 (Derivation "The factorization at second order") · Peskin & Schroeder, An Introduction to Quantum Field Theory, §4.4, p. 98 · Yu Zhao-Huan, 量子场论讲义, §10.5.1, eqs. (10.192)–(10.196) · proofs written here; every count checked by enumeration (`qft-C/tools/l14/enumerate_pairings.py`).*

A sum over the pairings of external points and vertex legs splits into the part that touches the external points and a vacuum part. This section makes the split a bijection of sets ([[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-1|Theorem §CA.8.1]]) and turns it into a factorization of exponential generating series ([[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-2|Theorem §CA.8.2]]): the factor $\frac{1}{k!}$ of the series is exactly what makes the choice of the vacuum vertices a product. This is the combinatorics behind the cancellation of vacuum bubbles ([[§C6.11 The iε Limit and Vacuum Bubbles|§C6.11]]). Pairings, labelled diagrams $X_{E,n}$, their multigraphs and the relabelling group are defined in [[§CA.7 Pairings, Diagrams and Symmetry Factors|§CA.7]], with the counting of the pairings of one diagram. As there, statements are made for vertices with four half-edges.

## Splitting a pairing at the external points

> [!definition] Definition §CA.8.1: Attached Vertex; Attached Labelled Diagram
> Let $P \in \mathcal P(X_{E,n})$ ([[§CA.7 Pairings, Diagrams and Symmetry Factors#^def-ca-7-2|Def. §CA.7.2]]). A vertex $v$ is **attached** if the multigraph $\Gamma(P)$ contains a path from $v$ to some external point. $P$ is **attached** if every vertex is attached; $\mathcal P_{\rm att}(X_{E,n})$ denotes the attached labelled diagrams. (For $n = 0$ every pairing of $E$ is attached; for $E = \varnothing$ and $n \ge 1$ none is.)
>
> *Source: written here (PS §4.4, p. 98: "disconnected from all external points"; Yu §10.5.1, after eq. (10.192): diagrams with every vertex connected to the external points)*

^def-ca-8-1

> [!theorem] Theorem §CA.8.1: Splitting a Pairing at the External Points
> For $P \in \mathcal P(X_{E,n})$ let $A(P) \subseteq [n]$ be its set of vertices that are not attached ([[§CA.8 Splitting Pairings and the Exponential Formula#^def-ca-8-1|Def. §CA.8.1]]), $P_{\rm att}$ the set of its blocks contained in $E \sqcup (([n]\setminus A)\times[4])$, and $P_{\rm vac}$ the set of its blocks contained in $A\times[4]$. Then
>
> $$
> P \longmapsto \bigl(A(P),\, P_{\rm att},\, P_{\rm vac}\bigr)
> $$
>
> is a bijection
>
> $$
> \mathcal P(X_{E,n}) \;\longrightarrow\; \bigsqcup_{A \subseteq [n]}\;\mathcal P_{\rm att}\bigl(E \sqcup (([n]\setminus A)\times[4])\bigr) \times \mathcal P\bigl(A\times[4]\bigr) .
> $$
>
> *Source: Yu §10.5.1, eq. (10.194) (second step: the full contractions split into a part containing the external points and a vacuum part) · stated as a bijection and proved here*

^thm-ca-8-1

> [!derivation]- Derivation
> **Step 1** (no block joins the two parts). Suppose a block $\{h, h'\}$ had $h$ at an external point or at a vertex $u \notin A$ and $h'$ at $v \in A$. A path from $u$ to $E$ followed by the edge of $\{h, h'\}$ would be a path from $v$ to $E$, so $v$ would be attached, contradicting $v \in A$. So every block lies inside $E \sqcup (([n]\setminus A)\times[4])$ or inside $A\times[4]$:
>
> $$
> P = P_{\rm att}\sqcup P_{\rm vac}, \qquad P_{\rm att}\in\mathcal P\bigl(E \sqcup (([n]\setminus A)\times[4])\bigr), \qquad P_{\rm vac}\in\mathcal P(A\times[4]) .
> $$
>
> **Step 2** ($P_{\rm att}$ is attached). Every vertex outside $A$ has a path to $E$ in $\Gamma(P)$; the path never enters $A$ (a vertex of $A$ on it would be attached), so it uses only blocks of $P_{\rm att}$. The image lies in the stated set.
>
> **Step 3** (inverse). Given $A$, an attached pairing $Q$ of $E \sqcup (([n]\setminus A)\times[4])$ and any pairing $R$ of $A\times[4]$, let
>
> $$
> \Psi(A, Q, R) = Q \sqcup R \in \mathcal P(X_{E,n}) .
> $$
>
> In $\Gamma(Q \sqcup R)$ the vertices of $A$ are joined only among themselves (blocks of $R$), so they have no path to $E$; every other vertex has one through $Q$. Hence $A(Q\sqcup R) = A$, $(Q\sqcup R)_{\rm att} = Q$, $(Q\sqcup R)_{\rm vac} = R$; conversely $\Psi(A(P), P_{\rm att}, P_{\rm vac}) = P$ (Step 1). The two maps are inverse.
>
> **Step 4** (example). $E = \{x, y\}$, $n = 2$, a tadpole at vertex 1 and a figure-eight at vertex 2 (figure below):
>
> $$
> P = \bigl\{\{x,(1,1)\},\{y,(1,2)\},\{(1,3),(1,4)\},\{(2,1),(2,2)\},\{(2,3),(2,4)\}\bigr\} \longmapsto \Bigl(\{2\},\ \bigl\{\{x,(1,1)\},\{y,(1,2)\},\{(1,3),(1,4)\}\bigr\},\ \bigl\{\{(2,1),(2,2)\},\{(2,3),(2,4)\}\bigr\}\Bigr) .
> $$
>
> **What the derivation shows.**
> - A pairing is uniquely "the part that touches the external points" together with "a vacuum part", and the vacuum part may sit on any subset of the vertices.

^der-ca-8-1

![[ph-qft-ca-7-6.svg]]
*The split of [[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-1|Theorem §CA.8.1]]. The vertex $z_2$ has no path to an external point ([[§CA.8 Splitting Pairings and the Exponential Formula#^def-ca-8-1|Def. §CA.8.1]]), so $A(P) = \{2\}$; no block joins it to the rest, and $P$ is the disjoint union of an attached pairing and a vacuum pairing.*

> [!theorem] Theorem §CA.8.2: Factorization of Sums over Pairings
> Let $R$ be a commutative ring and, for each $k \ge 0$, $f_k$ a function on $\mathcal P(X_{E,k})$ with values in $R$. Suppose there are functions $a_i$ on $\mathcal P_{\rm att}(X_{E,i})$ and $b_j$ on $\mathcal P(X_{\varnothing,j})$ such that for every $P$, with $A = A(P)$, $|A| = j$ ([[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-1|Theorem §CA.8.1]]),
>
> $$
> f_k(P) = a_{k-j}\bigl(\rho_A P_{\rm att}\bigr)\;b_j\bigl(\rho'_AP_{\rm vac}\bigr) ,
> $$
>
> where $\rho_A$, $\rho'_A$ rename the vertices of $[k]\setminus A$ and of $A$ by the order-preserving bijections onto $[k - j]$ and $[j]$. Then, in the ring of formal power series $R[\![t]\!]$,
>
> $$
> \sum_{k\ge0}\frac{t^k}{k!}\sum_{P\in\mathcal P(X_{E,k})}f_k(P) = \Bigl(\sum_{i\ge0}\frac{t^i}{i!}\sum_{Q\in\mathcal P_{\rm att}(X_{E,i})}a_i(Q)\Bigr)\Bigl(\sum_{j\ge0}\frac{t^j}{j!}\sum_{R'\in\mathcal P(X_{\varnothing,j})}b_j(R')\Bigr) .
> $$
>
> *Source: Yu §10.5.1, eqs. (10.194)–(10.196) (the same argument for the vacuum expectation values of $\phi^4$ theory) · stated for pairings and proved here*

^thm-ca-8-2

> [!derivation]- Derivation
> **Step 1** (split). By [[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-1|Theorem §CA.8.1]],
>
> $$
> \sum_{P\in\mathcal P(X_{E,k})}f_k(P) = \sum_{A\subseteq[k]}\;\sum_{Q}\;\sum_{R}a_{k-|A|}(\rho_AQ)\,b_{|A|}(\rho'_AR) ,
> $$
>
> with $Q$ over the attached pairings of $E \sqcup (([k]\setminus A)\times[4])$ and $R$ over the pairings of $A\times[4]$.
>
> **Step 2** (rename). Renaming vertices by $\rho_A$ is a bijection from the attached pairings of $E \sqcup (([k]\setminus A)\times[4])$ onto $\mathcal P_{\rm att}(X_{E,k-j})$ (attachment is a property of the multigraph and survives renaming), and $\rho'_A$ is a bijection from $\mathcal P(A\times[4])$ onto $\mathcal P(X_{\varnothing,j})$. So for $|A| = j$
>
> $$
> \sum_{Q}\sum_{R}a_{k-j}(\rho_AQ)\,b_j(\rho'_AR) = \alpha_{k-j}\,\beta_j, \qquad \alpha_i = \sum_{Q'\in\mathcal P_{\rm att}(X_{E,i})}a_i(Q'), \qquad \beta_j = \sum_{R'\in\mathcal P(X_{\varnothing,j})}b_j(R') ,
> $$
>
> independently of which $A$.
>
> **Step 3** (count the subsets). There are $\binom kj$ subsets with $|A| = j$:
>
> $$
> \sum_{P\in\mathcal P(X_{E,k})}f_k(P) = \sum_{j=0}^k\binom kj\,\alpha_{k-j}\,\beta_j .
> $$
>
> For $k = 1$ the subsets are $A = \varnothing$ and $A = \{1\}$: $\sum_Pf_1(P) = \alpha_1\beta_0 + \alpha_0\beta_1$, with $\beta_0 = b_0(\varnothing)$ the value on the empty pairing.
>
> **Step 4** (the factorials). $\frac{1}{k!}\binom kj = \frac{1}{(k-j)!\,j!}$, so
>
> $$
> \frac{1}{k!}\sum_{P\in\mathcal P(X_{E,k})}f_k(P) = \sum_{i+j=k}\frac{\alpha_i}{i!}\,\frac{\beta_j}{j!} ,
> $$
>
> which is the coefficient of $t^k$ of the product on the right (the product of formal power series, the Cauchy product; no convergence is involved).
>
> ⚑ Check: with all functions equal to 1 and $E = \{x, y\}$, the identity says $(4k+1)!! = \sum_j\binom kj\,|\mathcal P_{\rm att}(X_{E,k-j})|\,(4j-1)!!$ (with $(-1)!! = |\mathcal P(\varnothing)| = 1$). For $k = 1$:
>
> $$
> 5!! = \binom10\,|\mathcal P_{\rm att}(X_{E,1})|\cdot(-1)!! + \binom11\,|\mathcal P_{\rm att}(X_{E,0})|\cdot3!! = 1\cdot12\cdot1 + 1\cdot1\cdot3 = 15 ,
> $$
>
> the 12 tadpole pairings and the 3 with a figure-eight. Enumeration confirms the identity for $k = 1, 2, 3$.
>
> **What the derivation shows.**
> - The $\frac{1}{k!}$ of an exponential series is exactly what turns the choice of which vertices are "vacuum" into a product.
> - Only renaming and the split were used; nothing about the values of $a$ and $b$.
> - Used in: the cancellation of vacuum bubbles to all orders ([[§C6.11 The iε Limit and Vacuum Bubbles#^thm-c6-11-4|Theorem §C6.11.4]]).

^der-ca-8-2

*Uses:* [[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-1|Theorem §CA.8.1]]

<!-- HELD until Problem Set 8 is submitted (Nov 1): insertion point; see qft-C/HOLD-PS8.md and PAUSED-2026-10-08.md. -->

> [!remark]- Connections
> - The objects split here, labelled diagrams and their multigraphs, are those of §CA.7; the split respects the relabelling group, since attachment is a property of the multigraph — [[§CA.7 Pairings, Diagrams and Symmetry Factors#^def-ca-7-2|Def. §CA.7.2]], [[§CA.7 Pairings, Diagrams and Symmetry Factors#^def-ca-7-3|Def. §CA.7.3]].
> - **Used in** (C6 places): Definition §CA.8.1, Theorems §CA.8.1–§CA.8.2 — the factorization of the numerator and the cancellation of vacuum bubbles ([[§C6.11 The iε Limit and Vacuum Bubbles#^thm-c6-11-4|Theorem §C6.11.4]], [[§C6.11 The iε Limit and Vacuum Bubbles#^thm-c6-11-5|Theorem §C6.11.5]]).
