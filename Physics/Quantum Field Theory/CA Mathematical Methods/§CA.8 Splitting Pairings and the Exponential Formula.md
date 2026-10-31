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

*Sources: the user's PHY 513 notes, Ch. 14 §14.7 (Derivation "The factorization at second order") · Peskin & Schroeder, An Introduction to Quantum Field Theory, §4.4, pp. 96–98, eqs. (4.50)–(4.52) · Yu Zhao-Huan, 量子场论讲义, §10.5.1, eqs. (10.192)–(10.196) · the user's note "Symmetry Factors and the Orbit–Stabilizer Theorem" (Oct 2026), §6, §8 · PHY 513, Problem Set 8, Problems 1(b), 2(c), 3(c) · proofs written here; every count checked by enumeration (`qft-C/tools/l14/enumerate_pairings.py`).*

A sum over the pairings of external points and vertex legs splits into the part that touches the external points and a vacuum part. This section makes the split a bijection of sets ([[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-1|Theorem §CA.8.1]]) and turns it into a factorization of exponential generating series ([[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-2|Theorem §CA.8.2]]): the factor $\frac{1}{k!}$ of the series is exactly what makes the choice of the vacuum vertices a product. This is the combinatorics behind the cancellation of vacuum bubbles ([[§C6a.11 The iε Limit and Vacuum Bubbles|§C6a.11]]). Pairings, labelled diagrams $X_{E,n}$, their multigraphs and the relabelling group are defined in [[§CA.7 Pairings, Diagrams and Symmetry Factors|§CA.7]], with the counting of the pairings of one diagram. A vacuum sum weighted by $1/S$ is the exponential of its connected part ([[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-3|Theorem §CA.8.3]]). As in §CA.7, statements are made for vertices with four half-edges; the last subsection extends the counting to other vertices: other valences, several types, legs of different kinds ([[§CA.8 Splitting Pairings and the Exponential Formula#^def-ca-8-2|Def. §CA.8.2]], [[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-4|Theorem §CA.8.4]]).

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
> - Used in: the cancellation of vacuum bubbles to all orders ([[§C6a.11 The iε Limit and Vacuum Bubbles#^thm-c6a-11-4|Theorem §C6a.11.4]]).

^der-ca-8-2

*Uses:* [[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-1|Theorem §CA.8.1]]

## Vacuum diagrams exponentiate

> [!theorem] Theorem §CA.8.3: The Exponential Formula
> Let $R$ be a commutative ring containing $\mathbb Q$, and $w$ an $R$-valued function on the vacuum labelled diagrams $\bigsqcup_{n\ge0}\mathcal P(X_{\varnothing,n})$ ([[§CA.7 Pairings, Diagrams and Symmetry Factors#^def-ca-7-2|Def. §CA.7.2]]) that is constant on the orbits of $G_n$ ([[§CA.7 Pairings, Diagrams and Symmetry Factors#^def-ca-7-3|Def. §CA.7.3]]), equal to $1$ on the empty pairing, and multiplicative over connected components: if the components of the multigraph $\Gamma(P)$ have vertex sets $B_1, \dots, B_c$, then $w(P) = \prod_iw(\rho_{B_i}P|_{B_i})$, $\rho_B$ the order-preserving renaming of $B$ onto $[|B|]$. Then, in $R[\![t]\!]$, with $D$ running over the vacuum diagrams and $C$ over the connected ones (orbits, [[§CA.7 Pairings, Diagrams and Symmetry Factors#^def-ca-7-4|Def. §CA.7.4]]), $n(\cdot)$ the number of vertices:
> 1. $$\sum_D\frac{w(D)}{S(D)}\,t^{n(D)} = \exp\Bigl(\sum_C\frac{w(C)}{S(C)}\,t^{n(C)}\Bigr) ;$$
> 2. if $D$ consists of $n_i$ copies of the pairwise distinct connected diagrams $C_i$, then $S(D) = \prod_in_i!\,S(C_i)^{n_i}$.
>
> *Source: PS §4.4, pp. 96–97, eqs. (4.50)–(4.52) ("the exponentiation of the disconnected diagrams"; "The $1/n_i!$ is the symmetry factor coming from interchanging the $n_i$ copies of $V_i$") · the user's PHY 513 notes, Ch. 14 §14.7 ("the bubbles exponentiate, $\sum$ bubbles $= \exp(\sum$ connected bubbles$)$") · PHY 513, Problem Set 8, Problem 3(c) (the same mechanism for one-legged source vertices: $S_m = 2^m\,m!$) · stated for pairings and proved here*

^thm-ca-8-3

> [!derivation]- Derivation
> **Step 1** (components). For $P \in \mathcal P(X_{\varnothing,n})$ the vertex sets of the components of $\Gamma(P)$ form a set partition $\pi(P)$ of $[n]$; no block joins two components, so $P = \bigsqcup_{B\in\pi(P)}P|_B$ with each $P|_B$ a pairing of $B\times[4]$ with connected multigraph. Conversely a partition $\pi$ and connected pairings $Q_B$ of $B\times[4]$ give $P = \bigsqcup_BQ_B$ with $\pi(P) = \pi$ (as in Step 3 of [[§CA.8 Splitting Pairings and the Exponential Formula#^der-ca-8-1|Derivation §CA.8.1]]). So
>
> $$
> \mathcal P(X_{\varnothing,n}) \;\longleftrightarrow\; \bigsqcup_{\pi\in\Pi_n}\;\prod_{B\in\pi}\mathcal P_{\rm conn}(B\times[4]) ,
> $$
>
> $\Pi_n$ the set partitions of $[n]$. Example $n = 2$: the dumbbell and the melon have $\pi = \{\{1,2\}\}$, two figure-eights $\pi = \{\{1\},\{2\}\}$.
>
> **Step 2** (labelled sums). With $a_n = \sum_{P\in\mathcal P(X_{\varnothing,n})}w(P)$ and $c_k = \sum_{Q\in\mathcal P_{\rm conn}(X_{\varnothing,k})}w(Q)$, Step 1, multiplicativity and the renaming bijections $\rho_B$ give
>
> $$
> a_n = \sum_{\pi\in\Pi_n}\prod_{B\in\pi}c_{|B|}, \qquad\text{e.g.}\quad a_2 = c_2 + c_1^2 .
> $$
>
> **Step 3** (exponential generating series). In $R[\![u]\!]$,
>
> $$
> \exp\Bigl(\sum_{k\ge1}\frac{c_ku^k}{k!}\Bigr) = \sum_{m\ge0}\frac{1}{m!}\sum_{k_1,\dots,k_m\ge1}\prod_{i=1}^m\frac{c_{k_i}u^{k_i}}{k_i!} = \sum_{n\ge0}\frac{u^n}{n!}\sum_{m\ge0}\frac{1}{m!}\sum_{k_1+\dots+k_m = n}\frac{n!}{k_1!\cdots k_m!}\prod_ic_{k_i} .
> $$
>
> The multinomial $\frac{n!}{k_1!\cdots k_m!}$ counts the ordered lists $(B_1, \dots, B_m)$ of disjoint sets covering $[n]$ with $|B_i| = k_i$; a partition with $m$ (distinct, nonempty) blocks is listed $m!$ times. So the coefficient of $\frac{u^n}{n!}$ is $\sum_{\pi\in\Pi_n}\prod_Bc_{|B|} = a_n$ (Step 2). For $n = 2$: $m = 1$ gives $c_2$, $m = 2$ gives $\frac12\cdot\frac{2!}{1!\,1!}c_1^2 = c_1^2$. Hence $\sum_n\frac{a_nu^n}{n!} = \exp\bigl(\sum_k\frac{c_ku^k}{k!}\bigr)$.
>
> **Step 4** (to diagrams). Put $u = t/4!$. By [[§CA.7 Pairings, Diagrams and Symmetry Factors#^thm-ca-7-7|Theorem §CA.7.7]],
>
> $$
> \frac{a_nu^n}{n!} = \frac{t^n}{n!\,(4!)^n}\sum_Pw(P) = t^n\sum_{D:\,n\text{ vertices}}\frac{w(D)}{S(D)} ,
> $$
>
> and, since connectedness is a property of the multigraph and so of the orbit ([[§CA.7 Pairings, Diagrams and Symmetry Factors#^thm-ca-7-8|Theorem §CA.7.8]]), the same theorem for $w\cdot\mathbf 1_{\rm conn}$ gives $\frac{c_ku^k}{k!} = t^k\sum_{C:\,k\text{ vertices}}\frac{w(C)}{S(C)}$. Step 3 is part 1 ($n = 0$: the empty diagram, $w = 1$, $S = 1$).
>
> **Step 5** (part 2). Take $R = \mathbb Q[y_C]$, one indeterminate per connected diagram, and $w(P) = \prod_{\text{components}}y_{[\text{component}]}$: constant on orbits and multiplicative. A diagram is its multigraph up to renaming the vertices (Theorem §CA.7.8), so it is determined by the multiset of its components, and $D = \{C_i^{\,n_i}\}$ is the only diagram with $w(D) = \prod_iy_{C_i}^{n_i}$. Part 1 reads
>
> $$
> \sum_D\frac{\prod_iy_{C_i}^{n_i}}{S(D)}\,t^{n(D)} = \prod_C\exp\Bigl(\frac{y_Ct^{n(C)}}{S(C)}\Bigr) = \prod_C\sum_{m\ge0}\frac{1}{m!}\Bigl(\frac{y_Ct^{n(C)}}{S(C)}\Bigr)^m ,
> $$
>
> and the monomial $\prod_iy_{C_i}^{n_i}$ appears on the right only from $m = n_i$ in the factor of $C_i$ and $m = 0$ elsewhere, with coefficient $\prod_i\frac{1}{n_i!\,S(C_i)^{n_i}}$. Comparing: $S(D) = \prod_in_i!\,S(C_i)^{n_i}$.
>
> **Step 6** (check, $w \equiv 1$). Enumeration gives $\sum_D\frac1S = \frac18, \frac{35}{384}, \frac{385}{3072}$ for $n = 1, 2, 3$ and $\sum_C\frac1S = \frac18, \frac1{12}, \frac{11}{96}$ (connected: figure-eight; dumbbell $\frac1{16}$ + melon $\frac1{48}$; four diagrams with $S = 24, 32, 48, 48$). At $n = 2$:
>
> $$
> \frac1{12} + \frac12\Bigl(\frac18\Bigr)^2 = \frac{32}{384} + \frac{3}{384} = \frac{35}{384}, \qquad S(\text{two figure-eights}) = 2!\cdot8^2 = 128 ;
> $$
>
> at $n = 3$, $\frac{11}{96} + \frac18\cdot\frac1{12} + \frac16\bigl(\frac18\bigr)^3 = \frac{385}{3072}$ (`qft-C/tools/hw8/check_hw8.py`).
>
> **What the derivation shows.**
> - The $\frac{1}{n!}$ of the exponential series is what turns "choose which vertices form which component" into a product; the $\frac{1}{n_i!}$ that remains is the permutation of identical components.
> - Used in: the bubbles exponentiate and the vacuum energy density ([[§C6a.11 The iε Limit and Vacuum Bubbles#^der-c6a-11-4b|Derivation §C6a.11.4, second route]], [[§C6a.11 The iε Limit and Vacuum Bubbles#^thm-c6a-11-6|Theorem §C6a.11.6]]); the source vertices of [[§C6b.9 Particle Production by a Classical Source꞉ the Diagrammatic Route|§C6b.9]] (with [[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-4|Theorem §CA.8.4]], 4).

^der-ca-8-3

*Uses:* [[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-1|Theorem §CA.8.1]], [[§CA.7 Pairings, Diagrams and Symmetry Factors#^thm-ca-7-7|Theorem §CA.7.7]], [[§CA.7 Pairings, Diagrams and Symmetry Factors#^thm-ca-7-8|Theorem §CA.7.8]]

## Other vertices

The statements so far are for vertices with four legs of one kind. Cubic and mixed interactions, the complex scalar's $\hat\phi^\dagger\hat\phi$ legs and one-legged source vertices need the same counting with other leg sets.

> [!definition] Definition §CA.8.2: Labelled Diagrams with General Vertices
> **Vertex data**: a finite set $K$ of **kinds** with a symmetric relation $\smile$ on $K$ (which kinds may be paired), and vertex **types** $t$, each with legs $L_t = \{1, \dots, r_t\}$ and a kind $\kappa_t(a) \in K$ for each leg. For external points $E$ with kinds $\kappa(e)$ and numbers $\mathbf n = (n_t)_t$ of vertices of each type, the half-edges are
>
> $$
> X_{E,\mathbf n} = E \;\sqcup\; \bigsqcup_t\bigl(\{t\}\times[n_t]\times L_t\bigr) ,
> $$
>
> a **labelled diagram** is a pairing of $X_{E,\mathbf n}$ ([[§CA.7 Pairings, Diagrams and Symmetry Factors#^def-ca-7-1|Def. §CA.7.1]]) all of whose blocks $\{h, h'\}$ have $\kappa(h)\smile\kappa(h')$, and $\mathcal P_\smile(X_{E,\mathbf n})$ is their set. The **leg group** of type $t$ is $H_t = \{\tau \in \operatorname{Sym}(L_t) : \kappa_t\circ\tau = \kappa_t\}$, and the **relabelling group** is
>
> $$
> G_{\mathbf n} = \prod_t\bigl((H_t)^{n_t} \rtimes S_{n_t}\bigr) ,
> $$
>
> each factor acting on the half-edges of its type as in [[§CA.7 Pairings, Diagrams and Symmetry Factors#^def-ca-7-3|Def. §CA.7.3]], external points fixed. Diagram, automorphism group and $S(P) = |\operatorname{Stab}_{G_{\mathbf n}}(P)|$ as in [[§CA.7 Pairings, Diagrams and Symmetry Factors#^def-ca-7-4|Def. §CA.7.4]].
>
> *Source: the user's note "Symmetry Factors and the Orbit–Stabilizer Theorem" (Oct 2026), §8, Remark "The same proof for other vertices" · PHY 513, Problem Set 8, Problems 1(b), 2(c), 3(c) · made precise here*

^def-ca-8-2

> [!theorem] Theorem §CA.8.4: Orbit Counting for General Vertices
> In the setting of [[§CA.8 Splitting Pairings and the Exponential Formula#^def-ca-8-2|Def. §CA.8.2]], with $m_{t,k}$ the number of legs of kind $k$ of type $t$:
> 1. $G_{\mathbf n}$ acts on $\mathcal P_\smile(X_{E,\mathbf n})$, and $|G_{\mathbf n}| = \prod_tn_t!\,|H_t|^{n_t}$ with $|H_t| = \prod_km_{t,k}!$.
> 2. $|G_{\mathbf n}\cdot P| = |G_{\mathbf n}|/S(P)$, and $\frac{1}{|G_{\mathbf n}|}\sum_Pf(P) = \sum_D\frac{f(D)}{S(D)}$ for $f$ constant on orbits ([[§CA.7 Pairings, Diagrams and Symmetry Factors#^thm-ca-7-5|Theorem §CA.7.5]], [[§CA.7 Pairings, Diagrams and Symmetry Factors#^thm-ca-7-7|Theorem §CA.7.7]] with $G_{\mathbf n}$).
> 3. Every element of $\operatorname{Stab}(P)$ maps each leg to a leg of the same kind, fixes every leg paired with an external point, and fixes the vertex of such a leg.
> 4. For one type of valence $r \ge 1$ with one kind of leg and $E = \varnothing$, [[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-3|Theorem §CA.8.3]] holds with $(4!)^n$ replaced by $(r!)^n$.
>
> | interaction | kinds, legs | $\lvert G_{\mathbf n}\rvert$ |
> |---|---|---|
> | $\frac{\lambda}{4!}\phi^4$ | one kind, 4 legs | $n!\,(4!)^n$ |
> | $\frac{g}{3!}\phi^3$ | one kind, 3 legs | $n!\,(3!)^n$ |
> | $\frac{g}{3!}\phi^3 + \frac{\lambda}{4!}\phi^4$ | two types | $n_3!\,(3!)^{n_3}\,n_4!\,(4!)^{n_4}$ |
> | $\frac{\lambda}{4}(\phi^\dagger\phi)^2$ | $\phi\smile\phi^\dagger$ only; legs $\phi, \phi, \phi^\dagger, \phi^\dagger$ | $n!\,(2!\,2!)^n$ |
> | $j\phi$ (source) | one kind, 1 leg | $n!$ |
> | $\mu\Phi\phi^2$ | $\Phi\smile\Phi$, $\phi\smile\phi$; legs $\Phi, \phi, \phi$ | $n!\,(1!\,2!)^n$ |
>
> *Source: the user's note "Symmetry Factors and the Orbit–Stabilizer Theorem" (Oct 2026), §6 (Proposition "Constraints and standard elements of Stab(P)", (i)–(ii)), §8 (Remark "The same proof for other vertices": "the inverse prefactor is $|G|$, diagrams are orbits, and $S = |G|/N = |\operatorname{Stab}(P)|$") · PHY 513, Problem Set 8, Problems 1(b), 2(c), 3(c) · proof written here*

^thm-ca-8-4

> [!derivation]- Derivation
> **Step 1** (action). For one type, the formula $(\tau, \sigma)\cdot(t, v, a) = (t, \sigma(v), \tau_{\sigma(v)}(a))$ is an action by Steps 1–3 of [[§CA.7 Pairings, Diagrams and Symmetry Factors#^der-ca-7-3|Derivation §CA.7.3]] with $S_4$ replaced by $H_t$; different types are permuted independently. Since $\kappa_t(\tau(a)) = \kappa_t(a)$, every $g$ preserves kinds, $\kappa(gh) = \kappa(h)$, so a block with $\kappa(h)\smile\kappa(h')$ goes to one with $\kappa(gh)\smile\kappa(gh')$: $g$ maps $\mathcal P_\smile$ to itself ([[§CA.7 Pairings, Diagrams and Symmetry Factors#^lem-ca-7-2|Lemma §CA.7.2]]).
>
> **Step 2** (order). $H_t = \prod_k\operatorname{Sym}(\kappa_t^{-1}(k))$, so $|H_t| = \prod_km_{t,k}!$; the semidirect and direct products have the product sets as underlying sets: $|G_{\mathbf n}| = \prod_t|H_t|^{n_t}\,n_t!$. Complex scalar: $m_\phi = m_{\phi^\dagger} = 2$, $|G| = n!\,(2!\,2!)^n$, e.g. $32$ for $n = 2$.
>
> **Step 3** (part 2). [[§30 Orbit–Stabilizer#^thm-30-3|493 Thm. §30.3]] for $G_{\mathbf n}$ acting on the finite set $\mathcal P_\smile$, then Steps 1–2 of [[§CA.7 Pairings, Diagrams and Symmetry Factors#^der-ca-7-7|Derivation §CA.7.7]] with $|G_{\mathbf n}|$ for $n!\,(4!)^n$.
>
> **Step 4** (part 3). Kinds: Step 1. If $\{e, h\} \in P$ and $g\cdot P = P$, then $\{ge, gh\} = \{e, gh\} \in P$; the only block containing $e$ is $\{e, h\}$, so $gh = h$. If $h$ is a leg of the vertex $(t, v)$, then $gh$ is a leg of $(t, \sigma_t(v))$, so $\sigma_t(v) = v$.
>
> **Step 5** (part 4). [[§CA.8 Splitting Pairings and the Exponential Formula#^der-ca-8-3|Derivation §CA.8.3]] used of the leg sets only that a pairing splits along the components (Step 1) and Theorem §CA.7.7 with $|G_n| = n!\,(4!)^n$ (Step 4); with $r$ legs, $u = t/r!$ and $|G_n| = n!\,(r!)^n$ by part 2. For $r = 1$: $2m$ vertices, $(2m - 1)!!$ pairings, all of them $m$ disjoint lines, one orbit, so
>
> $$
> S = \frac{(2m)!}{(2m - 1)!!} = 2^m\,m! = m!\,S(\text{one line})^m, \qquad S(\text{one line}) = 2 ,
> $$
>
> part 2 of Theorem §CA.8.3 ($m = 1, \dots, 4$: $2, 8, 48, 384$, enumerated).
>
> **What the derivation shows.**
> - "Divide by $S$" depends on the interaction only through $|G_{\mathbf n}|$, which is the inverse of the prefactor $\prod_t\frac{1}{n_t!}\bigl(\prod_k\frac{1}{m_{t,k}!}\bigr)^{n_t}$ when the Lagrangian is normalized with those factorials.
> - The product formula of [[§CA.7 Pairings, Diagrams and Symmetry Factors#^thm-ca-7-9|Theorem §CA.7.9]] changes with kinds: a loop whose two ends have different kinds cannot be flipped, and only parallel lines of the same kinds at both ends can be permuted (the oriented diagrams of [[§C6a.9 Symmetry Factors in Practice|§C6a.9]]).
> - Checked by enumeration (`qft-C/tools/hw8/check_hw8.py`): complex scalar $|G| = 4, 32$; cubic–quartic $|G| = 3!\,4! = 144$.

^der-ca-8-4

*Uses:* [[§CA.7 Pairings, Diagrams and Symmetry Factors#^der-ca-7-3|Derivation §CA.7.3]], [[§CA.7 Pairings, Diagrams and Symmetry Factors#^thm-ca-7-7|Theorem §CA.7.7]], [[§30 Orbit–Stabilizer#^thm-30-3|493 Thm. §30.3]], [[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-3|Theorem §CA.8.3]]

> [!remark]- Connections
> - The objects split here, labelled diagrams and their multigraphs, are those of §CA.7; the split respects the relabelling group, since attachment is a property of the multigraph — [[§CA.7 Pairings, Diagrams and Symmetry Factors#^def-ca-7-2|Def. §CA.7.2]], [[§CA.7 Pairings, Diagrams and Symmetry Factors#^def-ca-7-3|Def. §CA.7.3]].
> - The exponential formula is the combinatorial core of "log of the partition function = connected diagrams"; the same identity, $\sum_\pi\prod_Bc_{|B|}$ against $\exp\sum c_ku^k/k!$, counts set partitions (Bell numbers for $c_k = 1$) — [[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-3|Theorem §CA.8.3]].
> - **Used in** (C6a and C6b places): Definition §CA.8.1, Theorems §CA.8.1–§CA.8.2 — the factorization of the numerator and the cancellation of vacuum bubbles ([[§C6a.11 The iε Limit and Vacuum Bubbles#^thm-c6a-11-4|Theorem §C6a.11.4]], [[§C6a.11 The iε Limit and Vacuum Bubbles#^thm-c6a-11-5|Theorem §C6a.11.5]]); Theorem §CA.8.3 — the bubbles exponentiate, the vacuum energy density, the source vertices ([[§C6a.11 The iε Limit and Vacuum Bubbles#^der-c6a-11-4b|Derivation §C6a.11.4, second route]], [[§C6a.11 The iε Limit and Vacuum Bubbles#^thm-c6a-11-6|Theorem §C6a.11.6]], [[§C6a.11 The iε Limit and Vacuum Bubbles#^thm-c6a-11-7|Theorem §C6a.11.7]], [[§C6b.9 Particle Production by a Classical Source꞉ the Diagrammatic Route|§C6b.9]]); Definition §CA.8.2, Theorem §CA.8.4 — other vertices ([[§C6a.8 Position-Space Feynman Rules#^rem-c6a-8-2|§C6a.8, Remark: The same proof for other vertices]]), oriented lines ([[§C6a.9 Symmetry Factors in Practice#^thm-c6a-9-1|Theorem §C6a.9.1]]), scattering diagrams and vertex factors ([[§C6b.8 Amplitudes from Correlation Functions#^thm-c6b-8-3|Theorem §C6b.8.3]], [[§C6b.8 Amplitudes from Correlation Functions#^thm-c6b-8-4|Theorem §C6b.8.4]]), source vertices ([[§C6b.9 Particle Production by a Classical Source꞉ the Diagrammatic Route|§C6b.9]]).
