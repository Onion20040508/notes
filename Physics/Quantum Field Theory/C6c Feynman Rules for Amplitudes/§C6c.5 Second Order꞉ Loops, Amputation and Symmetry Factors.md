---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C6c
section: C6c.5
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C6c.4 First Order꞉ Enumerate, then Filter]] · ↑ [[· C6c Feynman Rules for Amplitudes]] · [[§C6c.6 Feynman Rules for Amplitudes]] →

*Sources: Yu Zhao-Huan, 量子场论讲义, §7.1.2, pp. 273–286 (the $14$ second-order terms of Yukawa theory, eqs. (7.60)–(7.73); boxed rule p. 275 with its footnote); §7.3, pp. 294–296, eqs. (7.126)–(7.132), Fig. 7.15 · Peskin & Schroeder, An Introduction to Quantum Field Theory, §4.6, pp. 112–114, eqs. (4.101)–(4.102) and the figure on p. 114 · PHY 513 Lecture 16 (Larsen, 2 Nov 2026), Part C, slides 22, 25–26, and transcript · PHY 513 Lecture 14 (Larsen, 26 Oct 2026), slide 17 · the user's PHY 513 notes, Lecture 16 update, §16.7–§16.8 · PHY 513, Problem Set 8, Problem 2(c) (the user's solution, submitted 2026-10-30).*

At second order two vertices appear, and with them loops, corrections on external legs and diagrams with symmetries. [[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^thm-c6c-5-1|Theorem §C6c.5.1]] sorts every second-order term of $\phi^4$ theory by its structure and says what becomes of it, as Yu does for his $14$ Yukawa terms; the $\frac{1}{2!}$ is cancelled by the exchange of the two vertices ([[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^thm-c6c-5-2|Theorem §C6c.5.2]]). Corrections on an external leg are not scattering and are cut off by amputation ([[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^def-c6c-5-1|Def. §C6c.5.1]], [[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^thm-c6c-5-3|Theorem §C6c.5.3]]); what remains for $2 \to 2$ is the one-loop amplitude with $S = 2$ ([[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^ex-c6c-5-1|Example §C6c.5.1]], Lecture 16, slide 25). Yu's self-energies as matrix elements are [[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^ex-c6c-5-2|★ Example §C6c.5.2]]. The section ends with the symmetry factor when the particles are held fixed: "$S$ simpler" ([[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^thm-c6c-5-4|Theorem §C6c.5.4]]), saturated vertices ([[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^thm-c6c-5-5|Theorem §C6c.5.5]]) and trees ([[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^thm-c6c-5-6|Theorem §C6c.5.6]]). [[§C6c.6 Feynman Rules for Amplitudes|§C6c.6]] collects the rules. The Yukawa version is [[§C6d.5 Fermion–Fermion Scattering|§C6d.5]].

**Setup and scope.** As in [[§C6c.4 First Order꞉ Enumerate, then Filter|§C6c.4]]: [[§C6a.0 Setups and Observables#^mod-c6a-0-3|Model §C6a.0.3]] with $\phi^4$, the second-order terms of $\langle f|\hat S|i\rangle$ between free relativistic states over $|0\rangle$ ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^pr-c6b-1-3|Principle §C6b.1.3]]). The loop amplitude of [[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^ex-c6c-5-1|Example §C6c.5.1]] is the $\lambda^2$ term of $\mathcal M$ with the prescription's scope: corrections on external legs are removed by amputation and return beyond lowest order as $\sqrt Z$ and the physical mass ([[§C6c.1 Amplitudes from Correlation Functions#^cau-c6c-1-2|§C6c.1, Caution: The rule is stated at lowest order]]; second semester). The counting statements ([[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^thm-c6c-5-1|Theorem §C6c.5.1]], [[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^thm-c6c-5-2|Theorem §C6c.5.2]], [[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^thm-c6c-5-4|Theorem §C6c.5.4]]–[[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^thm-c6c-5-6|Theorem §C6c.5.6]]) are exact combinatorics.

## The terms of second order

> [!theorem] Theorem §C6c.5.1: The Second-Order Terms of φ⁴ Theory
> In $\phi^4$ theory ([[§C6a.1 From Free to Interacting Fields#^mod-c6a-1-1|Model §C6a.1.1]]) the second-order term of the Dyson series is
>
> $$
> i\hat T^{(2)} = \frac{1}{2!}\Bigl(\frac{-i\lambda}{4!}\Bigr)^2\int d^4x\,d^4y\;T\{\hat\phi_I(x)^4\,\hat\phi_I(y)^4\} .
> $$
>
> Each of its $764$ Wick terms ([[§C6a.6 Wick's Theorem#^thm-c6a-6-2|Theorem §C6a.6.2]]) is fixed by the number $j$ of contractions between $x$ and $y$ and the numbers $a_x$, $a_y$ of contractions within each vertex; the $8 - 2j - 2a_x - 2a_y$ uncontracted fields take the particles ([[§C6c.3 Wick's Theorem between Particle States#^thm-c6c-3-2|Theorem §C6c.3.2]]). The classes, with $S$ the symmetry factor with the particles held fixed ([[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-5|Theorem §C6c.4.5]]):
>
> | $j$ | $(a_x, a_y)$ | Wick terms | particles | diagram, $S$ | fate |
> |---|---|---|---|---|---|
> | $0$ | any | $10\cdot10 = 100$ | $0$–$8$ | two first-order pieces | not one process: each piece its own delta ([[§C6c.3 Wick's Theorem between Particle States#^thm-c6c-3-3\|Theorem §C6c.3.3]], [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-6\|Theorem §C6c.4.6]]) |
> | $1$ | $(0, 0)$ | $16$ | $6$ | ★ tree, one internal line, $S = 1$ | ★ $3 \to 3$ and $4 \to 2$ allowed, $2 \to 4$ above $\sqrt s = 4m$; $1 \leftrightarrow 5$, $0 \leftrightarrow 6$ forbidden |
> | $1$ | $(1, 0)$, $(0, 1)$ | $96$ | $4$ | loop on an external leg, $S = 2$ | not amputated ([[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^thm-c6c-5-3\|Theorem §C6c.5.3]], 1) |
> | $1$ | $(1, 1)$ | $144$ | $2$ | chain of two tadpoles, $S = 4$ | ★ $1 \to 1$ forward, not amputated; $0 \leftrightarrow 2$ forbidden |
> | $2$ | $(0, 0)$ | $72$ | $4$ | one loop between the vertices, $S = 2$ | $2 \to 2$ in the $s$, $t$, $u$ channels ([[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^ex-c6c-5-1\|Example §C6c.5.1]]); $1 \leftrightarrow 3$, $0 \leftrightarrow 4$ forbidden |
> | $2$ | $(1, 0)$, $(0, 1)$ | $144$ | $2$ | snowman, $S = 4$ | ★ $1 \to 1$ forward; $0 \leftrightarrow 2$ forbidden |
> | $2$ | $(1, 1)$ | $72$ | $0$ | vacuum bubble, $S = 16$ ([[§C6a.9 Symmetry Factors in Practice#^ex-c6a-9-3\|Example §C6a.9.3]]) | a phase |
> | $3$ | $(0, 0)$ | $96$ | $2$ | sunset, $S = 6$ | ★ $1 \to 1$ forward; $0 \leftrightarrow 2$ forbidden |
> | $4$ | $(0, 0)$ | $24$ | $0$ | melon, $S = 48$ ([[§C6a.9 Symmetry Factors in Practice#^ex-c6a-9-2\|Example §C6a.9.2]]) | a phase |
>
> The $4$-particle and vacuum rows are taught (Lecture 16, slide 25; Lecture 14); the rows marked ★ are Yu's matrix elements beyond the course ($2$-particle rows: [[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^ex-c6c-5-2\|★ Example §C6c.5.2]]; as correlation functions the chain, snowman and sunset are taught, [[§C6a.9 Symmetry Factors in Practice#^ex-c6a-9-4\|Example §C6a.9.4]]). At second order the only new scattering of two equal-mass particles is the one-loop $2 \to 2$.
>
> *Model:* [[§C6a.0 Setups and Observables#^mod-c6a-0-3|Model §C6a.0.3]] with $\phi^4$; *applies:* second order of the Dyson series between free relativistic states over $|0\rangle$ ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^pr-c6b-1-3|Principle §C6b.1.3]]); exact as a statement about the Wick terms, the fates with the kinematic filter of [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-2|Theorem §C6c.4.2]] (equal masses $m > 0$).
>
> *Source: Yu §7.3, eq. (7.126) and pp. 294–296 (the self-energy terms (7.127)–(7.132) with their combinatorial factors $4\cdot4\cdot3\cdot3$, $4\cdot4\cdot6$, $6\cdot6\cdot2$); §7.1.2, pp. 273–274 (Yukawa theory: the $14$ terms (7.60)–(7.73) sorted in the same way) · PS §4.6, eqs. (4.101)–(4.102), p. 112 · PHY 513 Lecture 16, slide 25 · the term count: the ⚑ by-product of [[§C6a.6 Wick's Theorem#^der-c6a-6-2|Derivation §C6a.6.2]] · table written here (2026-11-05)*

^thm-c6c-5-1

> [!derivation]- Derivation
> **Step 1** (count of a class). A Wick term of $T\{\hat\phi_I(x)^4\hat\phi_I(y)^4\}$ with the eight factors labelled is a set of disjoint pairs ([[§C6a.6 Wick's Theorem#^thm-c6a-6-2|Theorem §C6a.6.2]]). For given $(j, a_x, a_y)$: choose the $j$ legs at $x$ and the $j$ legs at $y$ that are joined across, $\binom4j^2$ ways, and match them, $j!$; among the $4 - j$ other legs at $x$ choose $2a_x$ and pair them, $\binom{4 - j}{2a_x}(2a_x - 1)!!$ ([[§CA.7 Pairings, Diagrams and Symmetry Factors#^thm-ca-7-1|Theorem §CA.7.1]]); the same at $y$. So
>
> $$
> N(j, a_x, a_y) = \binom4j^2j!\;\binom{4 - j}{2a_x}(2a_x - 1)!!\;\binom{4 - j}{2a_y}(2a_y - 1)!! ,
> $$
>
> with $(-1)!! = 1$ and $N = 0$ when $2a > 4 - j$.
>
> **Step 2** (the rows). $j = 0$: per vertex $1 + \binom42 + 3 = 1 + 6 + 3 = 10$ ($a = 0, 1, 2$), so $10\cdot10 = 100$. $j = 1$: $\binom41^2\cdot1! = 16$; $a = 0$: $1$, $a = 1$: $\binom32 = 3$; so $(0,0)$: $16$, $(1,0)$ and $(0,1)$: $16\cdot3 + 16\cdot3 = 96$, $(1,1)$: $16\cdot3\cdot3 = 144$ (Yu: $4\cdot4\cdot3\cdot3$). $j = 2$: $\binom42^2\cdot2! = 72$; $a = 0$: $1$, $a = 1$: $\binom22 = 1$; so $(0,0)$: $72$, $(1,0)$ and $(0,1)$: $72 + 72 = 144$ (Yu: $6\cdot6\cdot2$ twice), $(1,1)$: $72$. $j = 3$: $\binom43^2\cdot3! = 96$ (Yu: $4\cdot4\cdot6$). $j = 4$: $4! = 24$.
>
> **Step 3** (total). $100 + 16 + 96 + 144 + 72 + 144 + 72 + 96 + 24 = 764 = \sum_k\binom8{2k}(2k - 1)!! = 1 + 28 + 70\cdot3 + 28\cdot15 + 105$, the count of the ⚑ of [[§C6a.6 Wick's Theorem#^der-c6a-6-2|Derivation §C6a.6.2]] for $n = 8$: every term is in exactly one row.
>
> **Step 4** (particles and connectedness). The uncontracted legs number $(4 - j - 2a_x) + (4 - j - 2a_y)$ and must all take particles ([[§C6c.3 Wick's Theorem between Particle States#^thm-c6c-3-2|Theorem §C6c.3.2]], 1). For $j = 0$ no line joins $x$ and $y$: two pieces, each with its own delta ([[§C6c.3 Wick's Theorem between Particle States#^thm-c6c-3-3|Theorem §C6c.3.3]]). For $j \ge 1$ the diagram is connected.
>
> **Step 5** ($S$). By [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-5|Theorem §C6c.4.5]], $S = 2!\,(4!)^2/(\text{full contractions giving the diagram}) = 1152/(N\cdot A)$, $A$ the number of ways to attach the particles to the free legs with the diagram fixed:
> - $j = 1$, $(0,0)$, $3 \to 3$ with given triples at the two vertices: which vertex holds which triple ($2$), each triple on three legs ($3!\cdot3!$): $A = 72$ per triple choice, $N\cdot A = 16\cdot72 = 1152$, $S = 1$;
> - $j = 1$, $(1,0)$, one particle at $x$, three at $y$: $A = 1\cdot3! = 6$ per assignment, and the mirror $(0,1)$: $N\cdot A = 96\cdot6 = 576$, $S = 2$;
> - $j = 1$, $(1,1)$: $k$ in at one free leg and out at the other, $A = 2$: $144\cdot2 = 288$, $S = 4$;
> - $j = 2$, $(0,0)$, $2 \to 2$ in one channel: which vertex holds $p_A, p_B$ ($2$), each pair on two legs ($2\cdot2$): $A = 8$, $72\cdot8 = 576$, $S = 2$ (as [[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^ex-c6c-5-1|Example §C6c.5.1]], Step 2);
> - $j = 2$, $(1,0)$ and $(0,1)$: both particles at the vertex without the loop, $A = 2$: $144\cdot2 = 288$, $S = 4$;
> - $j = 2$, $(1,1)$: $A = 1$, $S = 1152/72 = 16$; $j = 3$: $A = 2$, $96\cdot2 = 192$, $S = 6$; $j = 4$: $S = 1152/24 = 48$.
>
> **Step 6** (fates). Kinematics of each process by [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-2|Theorem §C6c.4.2]] (equal masses): $1 \to n$, $n \to 1$ with $n \ge 2$ and $0 \leftrightarrow n$ forbidden, $1 \to 1$ forward; $2 \to 4$ needs $\sqrt s > 4m$ (Step 3 of [[§C6c.4 First Order꞉ Enumerate, then Filter#^der-c6c-4-3|Derivation §C6c.4.3]]). The loop on a leg is cut off by amputation ([[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^thm-c6c-5-3|Theorem §C6c.5.3]], 1); vacuum pieces are phases ([[§C6a.11 The iε Limit and Vacuum Bubbles#^thm-c6a-11-3|Theorem §C6a.11.3]]).
>
> **What the derivation shows.**
> - The bookkeeping by $(j, a_x, a_y)$ is Yu's: every class is one diagram shape, and its Wick count times the particle attachments is $1152/S$ ([[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-5|Theorem §C6c.4.5]]); the $\frac{1}{2!}$ is always cancelled by the exchange $x \leftrightarrow y$ when particles are present ([[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^thm-c6c-5-2|Theorem §C6c.5.2]]).

^der-c6c-5-1

*Uses:* [[§C6a.6 Wick's Theorem#^thm-c6a-6-2|Theorem §C6a.6.2]], [[§CA.7 Pairings, Diagrams and Symmetry Factors#^thm-ca-7-1|Theorem §CA.7.1]], [[§C6a.6 Wick's Theorem#^der-c6a-6-2|Derivation §C6a.6.2]], [[§C6c.3 Wick's Theorem between Particle States#^thm-c6c-3-2|Theorem §C6c.3.2]], [[§C6c.3 Wick's Theorem between Particle States#^thm-c6c-3-3|Theorem §C6c.3.3]], [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-5|Theorem §C6c.4.5]], [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-2|Theorem §C6c.4.2]], [[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^thm-c6c-5-3|Theorem §C6c.5.3]], [[§C6a.11 The iε Limit and Vacuum Bubbles#^thm-c6a-11-3|Theorem §C6a.11.3]]

> [!theorem] Theorem §C6c.5.2: The 1/n! Cancels the Relabellings of the Vertices
> In $\phi^4$ theory let $D$ be a diagram of order $n$ of $\langle f|\hat S|i\rangle$, the particles labelled and held fixed, and $\Gamma_D$ its group of vertex permutations that are part of a symmetry of $D$ ([[§C6a.9 Symmetry Factors in Practice#^thm-c6a-9-1|Theorem §C6a.9.1]]).
> 1. The $n!$ permutations of the vertex labels $z_1, \dots, z_n$ map the contractions of $D$ to contractions of $D$ with the same integral; they give $n!/|\Gamma_D|$ different contraction patterns from each one.
> 2. If no symmetry of $D$ exchanges vertices ($\Gamma_D$ trivial), the $n!$ relabelled terms are all different and their sum cancels the $\frac{1}{n!}$ of the Dyson series exactly. This holds whenever every vertex is fixed by the particles, in particular when every vertex carries a particle, and for all second-order diagrams with particles ([[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^thm-c6c-5-1|Theorem §C6c.5.1]]): the two terms related by $x \leftrightarrow y$ give $2!$ against $\frac{1}{2!}$.
> 3. Otherwise a factor $\frac{1}{|\Gamma_D|}$ of the $\frac{1}{n!}$ is left over and is part of $\frac1S$; this happens only for vertices that carry no particle, e.g. vacuum bubbles (the melon, $S = 48 = 2\cdot4!$, [[§C6a.9 Symmetry Factors in Practice#^ex-c6a-9-2|Example §C6a.9.2]]).
>
> *Equivalently,* for correlation functions: the ⚑ by-product of [[§C6a.8 Position-Space Feynman Rules#^der-c6a-8-1|Derivation §C6a.8.1]] (the $\frac{1}{n!}$ cancels the $n!$ ways of naming the vertices, completely exactly when $\operatorname{Aut}$ is trivial).
>
> *Model:* [[§C6a.0 Setups and Observables#^mod-c6a-0-3|Model §C6a.0.3]] with $\phi^4$, any polynomial interaction with $n!$ replaced by $\prod_tn_t!$ ([[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-4|Theorem §CA.8.4]]); *applies:* every order of the Dyson series between free relativistic states (or between external points).
>
> *Source: Yu §7.1.2, p. 275 (boxed: "the $1/n!$ in $iT^{(n)}$ of eq. (7.4) is cancelled exactly by the $n!$ caused by the exchange symmetry of the spacetime coordinates"; footnote: "this rule does not apply to the bubble diagrams below that have nontrivial symmetry factors"); §7.3, eqs. (7.128), (7.130), (7.131) (the $x \leftrightarrow y$ pairs) · the ⚑ of [[§C6a.8 Position-Space Feynman Rules#^der-c6a-8-1|Derivation §C6a.8.1]] (promoted here 2026-11-05)*

^thm-c6c-5-2

> [!derivation]- Derivation
> **Step 1** (relabelling the vertices). In $\frac{1}{n!}\bigl(\frac{-i\lambda}{4!}\bigr)^n\int d^4z_1\cdots d^4z_n\,\langle f|T\{\hat\phi_I(z_1)^4\cdots\hat\phi_I(z_n)^4\}|i\rangle$ substitute $z_l \to z_{\pi(l)}$ for $\pi \in S_n$: the Jacobian is $1$, the measure $d^4z_1\cdots d^4z_n$ is unchanged, and $T\{\cdots\}$ is symmetric in the bosonic factors $\hat\phi_I(z_l)^4$. So a contraction pattern $P$ and its relabelled pattern $\pi P$ give the same integral.
>
> **Step 2** (part 1: how many distinct). The relabelling group is $G = S_n \ltimes (S_4)^n$, $|G| = n!\,(4!)^n$ ([[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-4|Theorem §CA.8.4]], 1), and $\operatorname{Stab}(P)$ the symmetries of $D$ with the particles fixed, $|\operatorname{Stab}(P)| = S(D)$. Let $\rho: G \to S_n$ forget the leg permutations; $\rho(\operatorname{Stab}(P)) = \Gamma_D$ and $\ker\rho\cap\operatorname{Stab}(P) = \operatorname{Stab}(P)\cap(S_4)^n$. Hence
>
> $$
> |G\cdot P| = \frac{n!\,(4!)^n}{S(D)} = \frac{n!}{|\Gamma_D|}\cdot\frac{(4!)^n}{|\operatorname{Stab}(P)\cap(S_4)^n|} , \qquad S(D) = |\Gamma_D|\cdot|\operatorname{Stab}(P)\cap(S_4)^n| ,
> $$
>
> and the first factor counts the patterns that differ by a vertex relabelling not undone by a symmetry.
>
> **Step 3** (part 2). If $\Gamma_D = \{e\}$, the first factor is $n!$ and cancels the $\frac{1}{n!}$; the second cancels the $\frac{1}{(4!)^n}$ up to the line part of $S$ ([[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-4|Theorem §C6c.4.4]], [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-5|Theorem §C6c.4.5]]). Every element of $\operatorname{Stab}(P)$ fixes each vertex that carries a particle ([[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-4|Theorem §CA.8.4]], 3), so $\Gamma_D$ moves only vertices without particles. At second order with particles, at least one vertex carries a particle, and the other is then fixed too (it is the only other vertex): $\Gamma_D$ is trivial for every row of [[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^thm-c6c-5-1|Theorem §C6c.5.1]] with particles. Example (Yu (7.128), the chain): the contractions with $k$ entering at $x$ and with $k$ entering at $y$ are the two terms $x \leftrightarrow y$, equal after Step 1, and $\frac{1}{2!}\cdot2 = 1$.
>
> **Step 4** (part 3). If $\Gamma_D \ne \{e\}$, only $\frac{n!}{|\Gamma_D|}$ distinct relabellings exist and $\frac{1}{n!}\cdot\frac{n!}{|\Gamma_D|} = \frac{1}{|\Gamma_D|}$ remains, a factor of $\frac1S$ by Step 2. The melon (two vertices, four lines between them, no particles): exchanging the vertices is a symmetry, $|\Gamma_D| = 2$, and the lines give $4!$, $S = 2\cdot24 = 48$.
>
> **What the derivation shows.**
> - Yu's footnote is part 3: the $\frac{1}{n!}$ survives in part only when a symmetry moves vertices, which with particles held fixed needs vertices without particles.

^der-c6c-5-2

*Uses:* [[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-4|Theorem §CA.8.4]], [[§C6a.9 Symmetry Factors in Practice#^thm-c6a-9-1|Theorem §C6a.9.1]], [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-4|Theorem §C6c.4.4]], [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-5|Theorem §C6c.4.5]], [[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^thm-c6c-5-1|Theorem §C6c.5.1]]

## Amputation

> [!definition] Definition §C6c.5.1: Amputation of an External Leg
> In a diagram with external particles, start at the tip of an external leg (the end at the particle) and go into the diagram to the **last point at which the diagram can be cut by removing one propagator** such that the cut separates the leg, with everything that hangs on it, from the rest. **Amputating** the leg removes everything between the tip and that cut: the particle is then joined, by a line without propagator, directly to the vertex beyond the cut. A diagram is **amputated** if no leg has anything to remove, i.e. no propagator separates a part holding a single particle from the rest.
>
> What is removed is "interaction corrects external state. Not an interaction between different states" (slide 26). A tree whose vertices all have $r_v \ge 3$ legs is amputated: removing an internal line leaves on each side a vertex with at least two further branches, each ending at a particle, so no line separates a single particle.
>
> *Model:* any (combinatorics); *applies:* diagrams of $S$-matrix elements and of correlation functions alike (for a correlation function the removed part includes the external propagator: [[§C6c.1 Amplitudes from Correlation Functions#^thm-c6c-1-1|Theorem §C6c.1.1]]); the removed corrections are not zero: beyond lowest order they return as $\sqrt Z$ per external line and the physical mass ([[§C6c.1 Amplitudes from Correlation Functions#^cau-c6c-1-2|§C6c.1, Caution: The rule is stated at lowest order]]; second semester).
>
> *Source: PHY 513 Lecture 16, slide 26 ("Some diagrams encode 'interaction corrects external state' … Amputation: exclude such diagrams. General rule for where to amputate external leg: go from tip to last point where diagram can be cut by removing one propagator. Corrections to external wave functions are interesting and studied in 2nd semester") · the user's PHY 513 notes, Lecture 16 update, §16.7, Definition "Connected and amputated" and paragraph "Why amputated" · PHY 513 Lecture 16, transcript ("What amputation means is that in these kind of diagrams … nothing happens between out here and into the vertex") · PS §4.6, p. 113 ("Starting from the tip of each external leg, find the last point at which the diagram can be cut by removing a single propagator, such that this operation separates the leg from the rest of the diagram. Cut there.") and the figure on p. 114*

^def-c6c-5-1

![[ph-qft-c6b-3-1.svg]]
*Amputation ([[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^def-c6c-5-1|Def. §C6c.5.1]]). (a) Slide 26: a loop at $z_1$ on the leg of $A$; removing the propagator $z_1z$ separates the leg with its loop. (b) Two loops on the leg: two propagators separate it; the cut is made at the last one, next to the vertex $z$, and both loops go. (c) What remains in both cases is the vertex $-i\lambda$ with $A$ attached directly. Added figure.*

> [!theorem] Theorem §C6c.5.3: External-Leg Corrections Are Removed by Amputation; the Rest Is the T-Matrix Element
> In the expansion of [[§C6c.3 Wick's Theorem between Particle States#^thm-c6c-3-3|Theorem §C6c.3.3]], keep the terms with one piece holding all particles (the others are not scattering: [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-6|Theorem §C6c.4.6]]). Then
> 1. a part hanging on one external leg, separated from the rest by one propagator, is a correction of the external state; its propagator carries the on-shell momentum of the particle, $\frac{i}{k^2 - m^2}\big|_{k^2 = m^2}$, and it is removed by amputation ([[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^def-c6c-5-1|Def. §C6c.5.1]]);
> 2. the rest, the fully connected amputated diagrams, is $\langle f|i\hat T|i\rangle = (2\pi)^4\delta^4(\sum k - \sum p)\,i\mathcal M$ at the order considered ([[§C6c.6 Feynman Rules for Amplitudes#^thm-c6c-6-3|Theorem §C6c.6.3]]).
>
> "Connected" and "amputated" are therefore consequences of the expansion, not assumptions.
>
> *Model:* [[§C6a.0 Setups and Observables#^mod-c6a-0-3|Model §C6a.0.3]]; *applies:* any polynomial interaction, every order, with the prescription of [[§C6b.1 The S-Matrix and the Invariant Amplitude#^pr-c6b-1-3|Principle §C6b.1.3]] (and its scope); the external-state corrections of part 1 return beyond lowest order as $\sqrt Z$ and the physical mass ([[§C2b.1 Heisenberg Fields#^cau-c2b-1-3|§C2b.1, Caution: With interactions, the one-particle matrix element carries √Z]]; [[§C6c.1 Amplitudes from Correlation Functions#^cau-c6c-1-2|§C6c.1, Caution: The rule is stated at lowest order]]; second semester).
>
> *Source: PHY 513 Lecture 16, slides 25–26 (slide 25: "self-energy: wave function of external state corrected from free to interacting") · PS §4.6, eqs. (4.101)–(4.102) ("Only *fully connected* diagrams, in which all external lines are connected to each other, contribute to the $T$-matrix", p. 111) · the user's PHY 513 notes, Lecture 16 update, §16.7 ("Why connected", "Why amputated") · proof written here*

^thm-c6c-5-3

> [!derivation]- Derivation
> **Step 1** (part 1). Let a propagator $\ell$ separate a part $X$ holding a single particle, of momentum $k$, from the rest. Step 2 of [[§C6c.3 Wick's Theorem between Particle States#^der-c6c-3-3|Derivation §C6c.3.3]] applied to $X$, with $\ell$ as its second external line, fixes the momentum of $\ell$ to $k$, so $\ell$ contributes
>
> $$
> \frac{i}{k^2 - m^2 + i\varepsilon}\Big|_{k^2 = m^2} = \frac{i}{i\varepsilon} \xrightarrow{\varepsilon\to0^+} \infty
> $$
>
> (PS (4.102): "$\frac{1}{p'^2 - m^2}\big|_{p' = p_B} = \frac{1}{0}$"). $X$ turns the free particle into the dressed one ("self-energy: wave function of external state corrected from free to interacting", slide 25), not a scattering between different particles; the amputation of [[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^def-c6c-5-1|Def. §C6c.5.1]] removes it.
>
> **Step 2** (part 2). What is left has one piece, so one overall delta (Step 2 of [[§C6c.3 Wick's Theorem between Particle States#^der-c6c-3-3|Derivation §C6c.3.3]]), and no external-state part: by [[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-3|Def. §C6b.1.3]] its sum is $(2\pi)^4\delta^4(\sum k - \sum p)\,i\mathcal M$.
>
> **What the derivation shows.**
> - "Connected" and "amputated" are not extra assumptions: disconnected terms are the $\mathbb 1$, bubbles or smaller processes (each piece its own delta), and external-leg parts are state corrections with an on-shell propagator (stated in the theorem).

^der-c6c-5-3

*Uses:* [[§C6c.3 Wick's Theorem between Particle States#^thm-c6c-3-3|Theorem §C6c.3.3]], [[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^def-c6c-5-1|Def. §C6c.5.1]], [[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-3|Def. §C6b.1.3]]

*Procedure:* [[P6 Tree Amplitude from a Lagrangian#^p6-3|P6, step 3]]

## Second-order examples

> [!example] Example §C6c.5.1: φφ → φφ at Order λ²
> ![[ph-qft-c6b-3-3.svg]]
>
> In $\phi^4$ theory ([[§C6a.1 From Free to Interacting Fields#^mod-c6a-1-1|Model §C6a.1.1]]) the connected, amputated diagrams of $p_A + p_B \to p_1 + p_2$ at order $\lambda^2$ are exactly the three loops (a)–(c), each with $S = 2$, and with $P_s = p_A + p_B$, $P_t = p_A - p_1$, $P_u = p_A - p_2$ the momentum through the loop,
>
> $$
> i\mathcal M^{(2)} = \frac{(-i\lambda)^2}{2}\sum_{P = P_s, P_t, P_u}\int\frac{d^4q}{(2\pi)^4}\,\frac{i}{q^2 - m^2 + i\varepsilon}\,\frac{i}{(P - q)^2 - m^2 + i\varepsilon} ;
> $$
>
> (d)–(f) are not diagrams of $i\mathcal M$. "A total of three diagrams at that order. It's not a humongous number."
>
> **Step 1** (legs and lines). Two quartic vertices, four particles: $\sum r_v = 8 = 4 + 2I$, $I = 2$; connected, $L = I - V + 1 = 1$ ([[§C6a.12 Feynman Rules for Polynomial Interactions#^thm-c6a-12-3|Theorem §C6a.12.3]], 1–2). With $e_v$ particles at vertex $v$, the free legs number $(4 - e_1) + (4 - e_2) = 2I = 4$, so $e_1 + e_2 = 4$:
> - $(e_1, e_2) = (4, 0)$: $v_2$ closes on itself, the figure-eight beside the vertex, (d): not connected ([[§C6a.12 Feynman Rules for Polynomial Interactions#^thm-c6a-12-3|Theorem §C6a.12.3]], 3), a vacuum bubble ([[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-6|Theorem §C6c.4.6]], 1);
> - $(3, 1)$: the free leg of $v_1$ goes to $v_2$, the two other free legs of $v_2$ close a loop: a loop on the leg of the single particle at $v_2$, (f), four such diagrams; removing the line $v_2v_1$ separates that particle with its loop: not amputated ([[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^def-c6c-5-1|Def. §C6c.5.1]]);
> - $(2, 2)$ with a loop at each vertex: two pieces; one incoming and one outgoing particle at each vertex gives (e), two forward pieces, the $\mathbb 1$ ([[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-6|Theorem §C6c.4.6]], 2); $p_A$, $p_B$ at one vertex gives $\delta^4(p_A + p_B)$, zero on shell ([[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-2|Theorem §C6c.4.2]], 1);
> - $(2, 2)$ with both lines between $v_1$ and $v_2$: connected and amputated; a diagram is the partner of $p_A$ at its vertex, $p_B$ (a), $p_1$ (b), $p_2$ (c).
>
> **Step 2** ($S$). The particles are fixed; the only symmetry is the exchange of the two parallel lines: $S = 2$. Count: $|G| = 2!\,(4!)^2 = 1152$ relabellings, $576$ pairings per channel (the fish of [[§C6a.9 Symmetry Factors in Practice#^ex-c6a-9-5|Example §C6a.9.5]] (c), with particles for external points), $1152/576 = 2$.
>
> **Step 3** (momenta). Each particle enters its vertex as a plane wave ([[§C6c.2 Contractions with External Particles#^thm-c6c-2-4|Theorem §C6c.2.4]]), each line in its Fourier form, and every vertex integral conserves four-momentum ([[§C6a.10 Feynman Rules in Momentum Space#^thm-c6a-10-1|Theorem §C6a.10.1]], [[§C6a.12 Feynman Rules for Polynomial Interactions#^thm-c6a-12-5|Theorem §C6a.12.5]]); in (a) $P_s$ enters the vertex of $p_A$, $p_B$ and leaves as $q$ and $P_s - q$ on the two lines; the vertex delta fixes the second line, the other vertex gives the overall $\delta^4(p_A + p_B - p_1 - p_2)$, and one integral $\int\frac{d^4q}{(2\pi)^4}$ is left ($L = 1$). In (b) the vertex of $p_A$ and $p_1$ passes $P_t = p_A - p_1$ into the loop, in (c) $P_u = p_A - p_2$. Each diagram: $\frac12(-i\lambda)^2\int\frac{d^4q}{(2\pi)^4}\frac{i}{q^2 - m^2 + i\varepsilon}\frac{i}{(P - q)^2 - m^2 + i\varepsilon}$; the sum is the statement.
>
> **Step 4** (what the integral does at large $q$). The integrand falls like $\frac{1}{q^4}$, and $\int\frac{d^4q}{q^4}$ diverges logarithmically: making sense of it is renormalization (second semester). The dependence on $P_s^2 = s$, $P_t^2 = t$, $P_u^2 = u$ ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-7|Theorem §C6b.1.7]]) is the energy dependence the first order lacks.
>
> *Source: PHY 513 Lecture 16, slide 25 (the $s$-channel loop as the connected example; "2nd and 3rd diagram are not connected"), slide 26, and transcript ("total of three diagrams at that order. It's not a humongous number") · the user's PHY 513 notes, Lecture 16 update, §16.8 "Example: $2 \to 2$ at order $\lambda^2$" (eq. (oneloop), "The symmetry factor $2$ (filled in)", "Looking ahead") and Figure "connamp" · PS §4.6, eq. (4.101), p. 112*

^ex-c6c-5-1

> [!example]- ★ Example §C6c.5.2: The Three Second-Order Self-Energies as Matrix Elements: S = 4, 6, 4
> ![[ph-qft-c6c-5-1.svg]]
>
> In $\phi^4$ theory ([[§C6a.1 From Free to Interacting Fields#^mod-c6a-1-1|Model §C6a.1.1]]) the second-order one-particle matrix elements $\langle\mathbf k'|i\hat T^{(2)}|\mathbf k\rangle$ come from the three $2$-particle rows of [[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^thm-c6c-5-1|Theorem §C6c.5.1]] (Yu's $iT^{(2)}_1$, $iT^{(2)}_2$, $iT^{(2)}_3$):
>
> | diagram | Wick count | $\frac{1}{2!}(\frac{1}{4!})^2\times$ count | $\times$ attachments | $S$ |
> |---|---|---|---|---|
> | (a) chain: $k \to x$ (loop) $\to y$ (loop) $\to k'$ | $4\cdot4\cdot3\cdot3 = 144$ | $\frac{1}{2!}\cdot\frac14$ | $\cdot2 = \frac14$ | $4 = 2\cdot2$ |
> | (b) sunset: three lines between $x$ and $y$ | $4\cdot4\cdot6 = 96$ | $\frac{1}{2!}\cdot\frac16$ | $\cdot2 = \frac16$ | $6 = 3!$ |
> | (c) snowman: $k$, $k'$ at $x$, two lines to $y$, loop at $y$ | $6\cdot6\cdot2\cdot2 = 144$ | $\frac18$ | $\cdot2 = \frac14$ | $4 = 2!\cdot2$ |
>
> so that, with $D_F(0)$ formal as in [[§C6c.4 First Order꞉ Enumerate, then Filter#^ex-c6c-4-2|Example §C6c.4.2]],
>
> $$
> \begin{aligned}
> \langle\mathbf k'|i\hat T^{(2)}_{(a)}|\mathbf k\rangle &= \frac{(-i\lambda)^2}{4}\,D_F(0)^2\;\frac{i}{k^2 - m^2 + i\varepsilon}\;(2\pi)^4\delta^4(k - k') ,\\
> \langle\mathbf k'|i\hat T^{(2)}_{(b)}|\mathbf k\rangle &= \frac{(-i\lambda)^2}{6}\int d^4z\;e^{-ik\cdot z}D_F(z)^3\;(2\pi)^4\delta^4(k - k') ,\\
> \langle\mathbf k'|i\hat T^{(2)}_{(c)}|\mathbf k\rangle &= \frac{(-i\lambda)^2}{4}\,D_F(0)\int d^4z\;D_F(z)^2\;(2\pi)^4\delta^4(k - k') .
> \end{aligned}
> $$
>
> All three are forward ($k' = k$): no scattering. (a) is not amputated, and its middle propagator is on shell, $\frac{i}{k^2 - m^2}\big|_{k^2 = m^2} = \frac{i}{i\varepsilon}$; (b) and (c) are second-order corrections of the mass.
>
> **Step 1** (the chain, Yu (7.127)–(7.128)). Contract one $\hat\phi(x)$ with one $\hat\phi(y)$ ($4\cdot4$ ways), then two of the remaining three $\hat\phi(x)$ ($\binom32 = 3$) and two of the remaining three $\hat\phi(y)$ ($3$): $144$ terms, each $D_F(x - y)D_F(0)^2\,{:}\hat\phi(x)\hat\phi(y){:}$, and $\frac{1}{2!}\frac{144}{(4!)^2} = \frac{1}{2!}\cdot\frac{144}{576} = \frac{1}{2!}\cdot\frac14$. Between $\langle\mathbf k'|$ and $|\mathbf k\rangle$ ([[§C6c.2 Contractions with External Particles#^thm-c6c-2-3|Theorem §C6c.2.3]], $n = 1$ twice):
>
> $$
> \langle\mathbf k'|{:}\hat\phi(x)\hat\phi(y){:}|\mathbf k\rangle = e^{ik'\cdot y}e^{-ik\cdot x} + e^{ik'\cdot x}e^{-ik\cdot y} ;
> $$
>
> the two terms are exchanged by $x \leftrightarrow y$, give equal integrals (Step 1 of [[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^der-c6c-5-2|Derivation §C6c.5.2]]), and $\frac{1}{2!}\cdot2 = 1$:
>
> $$
> \frac{(-i\lambda)^2}{4}D_F(0)^2\int d^4x\,d^4y\;e^{-ik\cdot x}\,D_F(x - y)\,e^{ik'\cdot y} = \frac{(-i\lambda)^2}{4}D_F(0)^2\,\tilde D_F(k)\,(2\pi)^4\delta^4(k - k') ,
> $$
>
> by Step 2 of [[§C6c.1 Amplitudes from Correlation Functions#^der-c6c-1-2|Derivation §C6c.1.2]] with $q_x = -k$, $q_y = k'$ and $\tilde D_F(-k) = \tilde D_F(k) = \frac{i}{k^2 - m^2 + i\varepsilon}$. $S = 1152/(144\cdot2) = 4$: each loop $2$ ([[§C6a.9 Symmetry Factors in Practice#^thm-c6a-9-1|Theorem §C6a.9.1]]).
>
> **Step 2** (the sunset, Yu (7.129)–(7.130)). Choose three $\hat\phi(x)$ and three $\hat\phi(y)$ ($\binom43^2 = 16$) and match them ($3! = 6$): $96$ terms $D_F(x - y)^3\,{:}\hat\phi(x)\hat\phi(y){:}$, $\frac{1}{2!}\frac{96}{576} = \frac{1}{2!}\cdot\frac16$. The same two attachments as in Step 1 and $\frac{1}{2!}\cdot2 = 1$:
>
> $$
> \frac{(-i\lambda)^2}{6}\int d^4x\,d^4y\;e^{-ik\cdot x}D_F(x - y)^3e^{ik'\cdot y} .
> $$
>
> Substitute $x = y + z$ (Jacobian $1$, $d^4x = d^4z$ at fixed $y$): the integrand becomes $e^{i(k' - k)\cdot y}e^{-ik\cdot z}D_F(z)^3$, and $\int d^4y\,e^{i(k' - k)\cdot y} = (2\pi)^4\delta^4(k - k')$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]]). $S = 1152/(96\cdot2) = 6$: the three parallel lines, $3!$.
>
> **Step 3** (the snowman, Yu (7.131)–(7.132)). Join two $\hat\phi(x)$ to two $\hat\phi(y)$ ($\binom42^2\cdot2! = 72$) and close the last two $\hat\phi(y)$ ($1$): $72$ terms $D_F(x - y)^2D_F(0)\,{:}\hat\phi(x)^2{:}$, and $72$ more with $x \leftrightarrow y$; the two sets give equal integrals and $\frac{1}{2!}\cdot\frac{144}{576} = \frac18$. Between the states the two free $\hat\phi(x)$ take $k$ and $k'$ in $2$ ways ([[§C6c.2 Contractions with External Particles#^thm-c6c-2-3|Theorem §C6c.2.3]]), each $e^{i(k' - k)\cdot x}$:
>
> $$
> \frac{(-i\lambda)^2}{8}\cdot2\int d^4x\,d^4y\;e^{i(k' - k)\cdot x}D_F(x - y)^2D_F(0) = \frac{(-i\lambda)^2}{4}D_F(0)\int d^4z\,D_F(z)^2\;(2\pi)^4\delta^4(k - k') ,
> $$
>
> with $y = x - z$ at fixed $x$ (Jacobian $1$, $x - y = z$) and $\int d^4x\,e^{i(k' - k)\cdot x} = (2\pi)^4\delta^4(k - k')$. $S = 1152/(144\cdot2) = 4$: the loop at $y$ ($2$) and the two parallel lines ($2!$).
>
> **Step 4** (fate). Each carries $\delta^4(k - k')$: forward only ([[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-2|Theorem §C6c.4.2]], 4), part of the $\mathbb 1$ of $\hat S$ ([[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-6|Theorem §C6c.4.6]], 2). (b) depends on $k$ through $\int d^4z\,e^{-ik\cdot z}D_F(z)^3$ and corrects the mass and the normalization $Z$; (c) is momentum independent and only shifts the mass; (a) is a tadpole on each side of an on-shell propagator: removing the line $x$–$y$ separates a single particle with its loop, so it is a correction of the external state ([[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^thm-c6c-5-3|Theorem §C6c.5.3]], 1). The same three diagrams with external points $x_1$, $x_2$ in place of the particles are the taught correlator corrections of [[§C6a.9 Symmetry Factors in Practice#^ex-c6a-9-4|Example §C6a.9.4]], with the same $S$.
>
> *Source: Yu §7.3, eqs. (7.126)–(7.132), Fig. 7.15 (beyond the course as $T$-matrix elements; the symmetry factors $2\cdot2 = 4$, $3! = 6$, $2\cdot2 = 4$ read off the diagrams) · [[§C6a.9 Symmetry Factors in Practice#^ex-c6a-9-4|Example §C6a.9.4]] (Lecture 14)*

^ex-c6c-5-2

## Symmetry factors with the particles held fixed

> [!theorem] Theorem §C6c.5.4: With the Particles Held Fixed, S Comes Only from Self-Loops, Parallel Lines and Vertices without Particles
> Let $D$ be a diagram of an $S$-matrix element, the particles labelled and never relabelled, and $S(D)$ its symmetry factor ([[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-5|Theorem §C6c.4.5]]). Every symmetry of $D$
> 1. fixes each particle, each leg joined to a particle, and the vertex of that leg;
> 2. if it is not the identity, does at least one of: exchange the two ends of a self-loop (a line from a vertex to itself); permute lines that join the same two vertices; move a vertex that carries no particle.
>
> So $S(D) = |\Gamma_D|\prod_v2^{\ell(v)}\ell(v)!\prod_{\{u,w\}}m(u,w)!$ ([[§C6a.9 Symmetry Factors in Practice#^thm-c6a-9-1|Theorem §C6a.9.1]]) with $\Gamma_D$ acting only on vertices without particles: "$\mathcal M$ has less symmetry than the Green's function ⇒ $S$ simpler". A diagram in which every vertex carries a particle and no two vertices are joined by two lines or by a self-loop has $S = 1$; trees: [[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^thm-c6c-5-6|Theorem §C6c.5.6]].
>
> *Model:* any (combinatorics); *applies:* diagrams of $S$-matrix elements and of amplitudes ([[§C6c.6 Feynman Rules for Amplitudes#^def-c6c-6-1|Def. §C6c.6.1]]), any vertex types ([[§CA.8 Splitting Pairings and the Exponential Formula#^def-ca-8-2|Def. §CA.8.2]]).
>
> *Source: PHY 513 Lecture 16, slide 22 ("$\mathcal M$ has less symmetry than Green's function ⇒ $S$ simpler") · Yu §7.3, p. 294 ("for tree diagrams contributing to scattering or decay the symmetry factor is 1; loop diagrams may have nontrivial symmetry factors") · from the last sentence of the former Step 4 of [[§C6c.6 Feynman Rules for Amplitudes#^der-c6c-6-3|Derivation §C6c.6.3]] (now [[§C6c.4 First Order꞉ Enumerate, then Filter#^der-c6c-4-5|Derivation §C6c.4.5]], Step 2), promoted 2026-11-05*

^thm-c6c-5-4

> [!derivation]- Derivation
> **Step 1** (part 1). [[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-4|Theorem §CA.8.4]], 3: an element of $\operatorname{Stab}(P)$ maps each leg to a leg of the same kind, fixes every leg paired with an external point (here a particle, never relabelled), and fixes the vertex of such a leg.
>
> **Step 2** (part 2). Let $g \ne e$ be a symmetry. It moves some half-edge $h$; by Step 1, $h$ is not joined to a particle, so $h$ is an end of an internal line or of a self-loop, at a vertex $v$.
> - If $g$ moves $v$, then $v$ carries no particle (Step 1): $g$ moves a vertex without particles.
> - If $g$ fixes $v$, it maps $h$ to another leg $h'$ of $v$. If $h$ and $h'$ are the two ends of one self-loop at $v$, $g$ exchanges them. Otherwise let $h$ belong to a line to $w$ and $h'$ to a line to $w'$ (possibly $w = v$ for a self-loop, then $h'$ is on another self-loop at $v$). $g$ maps the line of $h$ to the line of $h'$, so it maps $w$ to $w'$. If $w' = w$, $g$ permutes two lines joining the same two vertices ($v$, $w$; for $w = v$ two self-loops at $v$). If $w' \ne w$, $g$ moves the vertex $w$, which by Step 1 carries no particle.
>
> **Step 3** (the formula). [[§C6a.9 Symmetry Factors in Practice#^thm-c6a-9-1|Theorem §C6a.9.1]] with the particles as the fixed external points: $\Gamma_D$ permutes vertices preserving every $\ell(v)$ and $m(u,w)$ and fixing the external points; by Step 1 it fixes every vertex holding a particle.
>
> **Step 4** (the case $S = 1$). If every vertex carries a particle, $\Gamma_D = \{e\}$ by Step 1; with no self-loops and every $m(u,w) \le 1$ the product in Step 3 is $1$.
>
> **What the derivation shows.**
> - Compared with a correlation function, an amplitude has no external propagators and no loops on external legs, and the particles pin the vertices they sit on; what can still be symmetric sits inside loops ([[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^ex-c6c-5-1|Example §C6c.5.1]]: two parallel lines, $S = 2$).

^der-c6c-5-4

*Uses:* [[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-4|Theorem §CA.8.4]], [[§C6a.9 Symmetry Factors in Practice#^thm-c6a-9-1|Theorem §C6a.9.1]]

*Procedure:* [[P5 Symmetry Factor of a Diagram#^p5-5|P5, step 5]]

> [!theorem] Theorem §C6c.5.5: Vertices Saturated by External Lines Give S = 1
> If every vertex $v$ of a diagram has valence $r_v \ge 2$ and at least $r_v - 1$ of its legs joined to external points, then $S = 1$; equivalently $N_D = |G|$ ([[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-4|Theorem §CA.8.4]]). In particular every tree diagram with one internal line has $S = 1$.
>
> *Model:* any (combinatorics); *applies:* any diagram with the stated valences, any vertex types.
>
> *Source: PHY 513, Problem Set 8, Problem 2(c) (the user's argument: "each vertex has exactly one internal leg … The external particles are never relabeled, so an element of $\mathrm{Stab}(P)$ fixes every leg joined to an external particle. The internal leg is then the only remaining leg at its vertex, so it is fixed as well") · PHY 513 Lecture 14, slide 17 ("Reordering of legs = topologically distinct diagram ⇒ S = 1")*

^thm-c6c-5-5

> [!derivation]- Derivation
> **Step 1** (vertices fixed). Let $g \in \operatorname{Stab}(P)$. Each leg joined to an external point is fixed, and so is its vertex ([[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-4|Theorem §CA.8.4]], 3). Every vertex has $r_v - 1 \ge 1$ such legs, so $g$ permutes no vertices.
>
> **Step 2** (legs fixed). $g$ maps the legs of $v$ to legs of $v$; at least $r_v - 1$ are fixed, so the remaining one (if any) is mapped to itself. Hence $g$ fixes every half-edge: $g = e$, $S = |\operatorname{Stab}(P)| = 1$.
>
> **Step 3** (count). $N_D = |G|/S = |G|$. Example (one cubic and one quartic vertex, five external particles, two on the cubic and three on the quartic vertex): the two at the cubic vertex attach in $3\cdot2$ ways, the three at the quartic vertex in $4\cdot3\cdot2$, the remaining two legs pair in one way: $N_D = 6\cdot24 = 144 = 3!\,4! = |G|$.

^der-c6c-5-5

*Uses:* [[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-4|Theorem §CA.8.4]]

*Procedure:* [[P5 Symmetry Factor of a Diagram#^p5-5|P5, step 5]]

> [!theorem] Theorem §C6c.5.6: Tree Diagrams of a Process Have S = 1
> Every fully connected tree diagram of a process — the particles labelled and never relabelled, every vertex of valence $r_v \ge 3$ — has symmetry factor $S = 1$: each tree contributes with its full vertex factors ([[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-4|Theorem §C6c.4.4]]) and no $\frac1S$, and it arises from exactly $|G|$ contractions ([[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-5|Theorem §C6c.4.5]]). For one internal line this is [[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^thm-c6c-5-5|Theorem §C6c.5.5]].
>
> *Model:* any (combinatorics); *applies:* any polynomial interaction ([[§C6a.12 Feynman Rules for Polynomial Interactions#^def-c6a-12-1|Def. §C6a.12.1]]), any order, tree diagrams of $S$-matrix elements and amplitudes ([[§C6c.6 Feynman Rules for Amplitudes#^def-c6c-6-1|Def. §C6c.6.1]]).
>
> *Source: Yu §7.3, p. 294 ("for tree diagrams contributing to scattering or decay processes the symmetry factor is 1") · PHY 513 Lecture 14, slide 17 ("Reordering of legs = topologically distinct diagram ⇒ S = 1") · PHY 513, Problem Set 8, Problem 2(c) · proof: the former Step 4 of [[§C6c.6 Feynman Rules for Amplitudes#^der-c6c-6-2|Derivation §C6c.6.2]] (the clause "with symmetry factor $S = 1$ for every tree diagram" of [[§C6c.6 Feynman Rules for Amplitudes#^thm-c6c-6-2|Theorem §C6c.6.2]]), moved here 2026-11-05*

^thm-c6c-5-6

> [!derivation]- Derivation
> **Step 1** ($S = 1$ for a tree). Let $D$ be a fully connected diagram without loops (a tree) and $g \in \operatorname{Stab}(P)$. Every leaf of the tree is an external particle (a vertex with a single line would have valence one). Removing an internal line $e$ splits the particles into two nonempty sets $E_1(e) \sqcup E_2(e)$, and different lines give different splits (two lines of a tree are separated by a vertex with a third branch, which holds a particle). $g$ fixes every particle ([[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-4|Theorem §CA.8.4]], 3), so it maps each line to the line with the same split, i.e. to itself, with its ends on their own sides: every line and every vertex is fixed. A tree has no two lines between the same vertices, so the legs of a fixed vertex are fixed too: $g = e$, $S = |\operatorname{Stab}(P)| = 1$ (for one internal line this is [[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^thm-c6c-5-5|Theorem §C6c.5.5]]).
>
> **Step 2** (the count). By orbit–stabilizer ([[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-4|Theorem §CA.8.4]], 2), $|G\cdot P| = |G|/S = |G|$: the prefactor $\frac{1}{|G|}\prod_t(-ig_t)^{n_t}$ of the Dyson series times $|G|$ leaves $\prod_t(-ig_t\prod_km_{t,k}!)^{n_t}$ divided by nothing. Checks: [[§C6c.6 Feynman Rules for Amplitudes#^ex-c6c-6-1|Example §C6c.6.1]] (orbits of $72 = 2!\,(3!)^2$), [[§C6c.6 Feynman Rules for Amplitudes#^ex-c6c-6-2|Example §C6c.6.2]] (orbits of $144 = 3!\,4!$).
>
> **What the derivation shows.**
> - Without loops every line is pinned by the particles on its two sides; symmetries need loops ([[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^thm-c6c-5-4|Theorem §C6c.5.4]]).

^der-c6c-5-6

*Uses:* [[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-4|Theorem §CA.8.4]], [[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^thm-c6c-5-5|Theorem §C6c.5.5]]

*Procedure:* [[P6 Tree Amplitude from a Lagrangian#^p6-4|P6, step 4]]

> [!abstract]- Mathematical background
> Proved in CA; each line says what the physics above relies on.
>
> - [[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-4|Theorem §CA.8.4]] — the relabelling group and orbit–stabilizer behind $\frac1S$ and behind $S = 1$ for trees.

> [!remark]- Connections
> - The second-order bubbles and self-energies are the correlator diagrams of Lecture 14 with particles in place of external points — [[§C6a.9 Symmetry Factors in Practice#^ex-c6a-9-2|Example §C6a.9.2]], [[§C6a.9 Symmetry Factors in Practice#^ex-c6a-9-3|Example §C6a.9.3]], [[§C6a.9 Symmetry Factors in Practice#^ex-c6a-9-4|Example §C6a.9.4]].
> - In Yukawa theory the second order has no symmetry factors and a relative sign between diagrams — [[§C6d.5 Fermion–Fermion Scattering|§C6d.5]], [[§C6d.4 Feynman Rules for Yukawa Theory#^thm-c6d-4-3|§C6d.4, Theorem §C6d.4.3]].
> - $S = 1$ for trees is what lets a tree amplitude be read off a Lagrangian without counting — [[P6 Tree Amplitude from a Lagrangian|P6]].
> - Amputated leg corrections are not zero: they return as $\sqrt Z$ per external line and the physical mass, the LSZ formula — [[§C6c.1 Amplitudes from Correlation Functions#^cau-c6c-1-2|§C6c.1, Caution: The rule is stated at lowest order]].
