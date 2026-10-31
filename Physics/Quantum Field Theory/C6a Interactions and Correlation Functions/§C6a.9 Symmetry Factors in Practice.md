---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C6a
section: C6a.9
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C6a.8 Position-Space Feynman Rules]] · ↑ [[· C6a Interactions and Correlation Functions]] · [[§C6a.10 Feynman Rules in Momentum Space]] →

*Sources: the user's PHY 513 notes, Ch. 14 §14.5 (Principle "The symmetry factor", practical rules; Figure "Symmetry factors"; Derivation "The melon: S = 48 by counting"; paragraph "How much this matters") · PHY 513 Lecture 14 (Larsen, 26 Oct 2026), Part B, slides 17–18, and transcript · Peskin & Schroeder, An Introduction to Quantum Field Theory, §4.4, pp. 92–93, eq. (4.45) · Yu Zhao-Huan, 量子场论讲义, §7.3, eqs. (7.124)–(7.125), (7.127)–(7.128), (7.131)–(7.132), and pp. 293–294 · the user's note "Symmetry Factors and the Orbit–Stabilizer Theorem" (Oct 2026), §6 (Proposition "Constraints and standard elements of Stab(P)"), §7 (Examples "The fifteen pairings", "The diagrams of PHY 513 HW 8, Problem 1(a)"), §8 (Remark "The same proof for other vertices") · PHY 513, Problem Set 8, Problem 1 (submitted 2026-10-30; the user's solution).*

The coefficient of a diagram is $1/S$, with $S$ the order of its symmetry group ([[§C6a.8 Position-Space Feynman Rules#^thm-c6a-8-1|Theorem §C6a.8.1]]). In practice $S$ is read off the drawing as a product of local factors (loops, bundles of parallel lines) and a global one (permutations of the vertices), a rule of thumb that is in fact exact ([[§CA.7 Pairings, Diagrams and Symmetry Factors#^thm-ca-7-9|Theorem §CA.7.9]]). This section states the slides' rules in that language and works the examples of the lecture, the user's notes and PS, each both by the product rule and by counting contractions; every count was checked by enumerating the pairings. The diagrams of Problem Set 8, Problem 1(a) are worked as the user solved them (both counts and stabilizers), and a last subsection treats the oriented lines of the complex scalar (Problem 1(b)). Yu treats symmetry factors in §7.3 for the self-energy contributions $\langle\mathbf k|iT|\mathbf k\rangle$ of the $S$-operator, counting contractions with the initial and final states rather than with fixed external points; the factors agree.

*Conventions* ([[Larsen PHY 513]]): a diagram's value includes $-i\lambda\int d^4z$ per vertex and $1/S$ ([[§C6a.8 Position-Space Feynman Rules#^thm-c6a-8-2|Theorem §C6a.8.2]]); "$k$ of $N$" means $k$ of the $N = n!\,(4!)^n$ relabellings, i.e. $k$ complete contractions produce the diagram, and $S = N/k$ ([[§CA.7 Pairings, Diagrams and Symmetry Factors#^thm-ca-7-5|Theorem §CA.7.5]]).

The product rule for $S$, proved in CA (its examples there are the vacuum bubbles: [[§CA.7 Pairings, Diagrams and Symmetry Factors#^ex-ca-7-1|Example §CA.7.1]]):

![[§CA.7 Pairings, Diagrams and Symmetry Factors#^thm-ca-7-9]]

> [!remark] Remark: The slides' general rule in this language
> Slide 17 states the principle: "Reordering of legs = topologically distinct diagram ⇒ S = 1"; "If symmetry ⇒ same diagram then S = order of symmetry." The first sentence is the case $\operatorname{Aut} = 1$: every one of the $n!\,(4!)^n$ relabellings gives a different contraction, and the prefactor cancels completely. The second is [[§C6a.8 Position-Space Feynman Rules#^def-c6a-8-1|Def. §C6a.8.1]]. The user's notes' "in practice, multiply: a factor 2 for each line that begins and ends at the same vertex; $k!$ for each set of $k$ lines joining the same two vertices; the number of permutations of internal vertices that map the diagram to itself" is [[§CA.7 Pairings, Diagrams and Symmetry Factors#^thm-ca-7-9|Theorem §CA.7.9]], with one clarification: $k$ loops at the same vertex count as a set of $k$ lines joining the same two vertices (figure-eight: $2\cdot2\cdot2!$). With external points held fixed, a vertex joined to an external point cannot be moved, so "more symmetric diagrams have larger $S$; diagrams anchored to many external points have smaller $S$."
>
> *Source: PHY 513 Lecture 14, slide 17, and transcript · the user's PHY 513 notes, Ch. 14 §14.5 (Principle "The symmetry factor")*

^rem-c6a-9-1

> [!caution] Caution: Loops at one vertex are permuted too
> The user's notes' rule "a factor 2 for each line that begins and ends at the same vertex; $k!$ for each set of $k$ lines joining the same two vertices" must count $k$ loops at one vertex as a set of $k$ lines joining that vertex to itself. Read literally, the figure-eight would get only the two loop factors:
>
> $$
> 2\cdot2 = 4 \;\ne\; 8 = \frac{4!}{3} ,
> $$
>
> while [[§CA.7 Pairings, Diagrams and Symmetry Factors#^thm-ca-7-9|Theorem §CA.7.9]] gives $2^{\ell}\,\ell!$ for $\ell$ loops at one vertex, $2^2\cdot2! = 8$, in agreement with the 3 of 24 contractions ([[§C6a.9 Symmetry Factors in Practice#^ex-c6a-9-1|Example §C6a.9.1]]) and with the notes' own figure ("$S = 2^3 = 8$", three reflections). The same applies to each figure-eight of "two figure-eights" ($S = 2\cdot8\cdot8 = 128$, [[§C6a.9 Symmetry Factors in Practice#^ex-c6a-9-3|Example §C6a.9.3]]).
>
> The exchange of the two loops is a permutation of the legs at the one vertex, not of vertices. The user's note on symmetry factors and orbit–stabilizer attributes it to a vertex permutation $\tau \ne e$ (paragraph after its Proposition "Constraints and standard elements of Stab(P)"); with $n = 1$ the only vertex permutation is the identity, and the exchange is
>
> $$
> (\tau_1, \sigma) = \bigl((1\,3)(2\,4),\ \mathrm{id}\bigr), \qquad (1\,3)(2\,4)\cdot\{\{1,2\},\{3,4\}\} = \{\{3,4\},\{1,2\}\} ,
> $$
>
> an element of the kernel of the projection to vertex permutations, counted by the $\ell!$ of $2^{\ell}\,\ell!$ (Step 3 of [[§CA.7 Pairings, Diagrams and Symmetry Factors#^der-ca-7-9|Derivation §CA.7.9]]).
>
> *Source: the user's PHY 513 notes, Ch. 14 §14.5 (Principle "The symmetry factor", "In practice, multiply"; Figure "Symmetry factors") · PHY 513 Lecture 14, slide 18 ("three reflection symmetries") · the user's note "Symmetry Factors and the Orbit–Stabilizer Theorem" (Oct 2026), §6, paragraph after Proposition "Constraints and standard elements of Stab(P)"*

^cau-c6a-9-1

![[ph-qft-ca-7-5.svg]]
*The product formula of [[§CA.7 Pairings, Diagrams and Symmetry Factors#^thm-ca-7-9|Theorem §CA.7.9]]. (a) The three kinds of factor: $2^{\ell}\ell!$ for $\ell$ loops at one vertex, $m!$ for $m$ lines between two points, and $|\Gamma_P|$ for the vertex permutations that keep the drawing. (b) Four diagrams with their $S$; with external points fixed, $\Gamma_P$ can be trivial.*

## Examples

> [!example] Example §C6a.9.1: The First-Order Diagrams
> The 15 complete contractions of $\hat\phi_x\hat\phi_y\hat\phi_{z_1}\cdots\hat\phi_{z_4}$ are listed, bracket by bracket, in Step 4 of [[§C6a.7 Feynman Diagrams for Correlation Functions#^der-c6a-7-1|Derivation §C6a.7.1]]; $N = 1!\,(4!)^1 = 24$. As pairings ("the fifteen pairings of $\langle\hat\phi(x)\hat\phi(y)\hat\phi(z)^4\rangle$"): $E = \{x, y\}$, $n = 1$, write $a$ for the leg $(1, a)$ of $z$; the relabelling group is $G_1 = S_4$ acting on the legs $1, 2, 3, 4$ ([[§CA.7 Pairings, Diagrams and Symmetry Factors#^def-ca-7-3|Def. §CA.7.3]]), and
>
> $$
> |G_1| = 4! = 24, \qquad |\mathcal P(X_{E,1})| = 5!! = 5\cdot3\cdot1 = 15
> $$
>
> ([[§CA.7 Pairings, Diagrams and Symmetry Factors#^thm-ca-7-1|Theorem §CA.7.1]]). The action has two orbits, the two diagrams below. In the shorthand of the figure, $\{x1, y2, 34\}$ is the pairing $\{\{x, 1\}, \{y, 2\}, \{3, 4\}\}$.
>
> *The tadpole* (the slides' "self-energy"): $x$–$z$, $z$–$y$, one loop at $z$.
> - Counting: the contractions are
>
> $$
> \overbracket{\hat\phi_x\hat\phi_{z_a}}\,\overbracket{\hat\phi_y\hat\phi_{z_b}}\,\overbracket{\hat\phi_{z_c}\hat\phi_{z_d}} = D_F(x - z)\,D_F(y - z)\,D_F(z - z), \qquad \{c, d\} = \{1, 2, 3, 4\}\setminus\{a, b\},
> $$
>
> one for each ordered pair $(a, b)$, $a \ne b$:
>
> $$
> (a, b) \in \{(1,2), (1,3), (1,4), (2,1), (2,3), (2,4), (3,1), (3,2), (3,4), (4,1), (4,2), (4,3)\} :
> $$
>
> 12 of 24, $\frac{12}{24} = \frac12$. As an orbit: with $P_0 = \{x1, y2, 34\}$, $\tau\cdot P_0 = \{\{x, \tau(1)\}, \{y, \tau(2)\}, \{\tau(3), \tau(4)\}\}$, and $(\tau(1), \tau(2))$ runs through the 12 ordered pairs above, e.g.
>
> $$
> (1\,2)\cdot P_0 = \{x2, y1, 34\}, \qquad (2\,3)\cdot P_0 = \{x1, y3, 24\}, \qquad |G_1\cdot P_0| = 4\cdot3 = 12 .
> $$
>
> - Symmetry: for $P = P_0 = \overbracket{\hat\phi_x\hat\phi_{z_1}}\,\overbracket{\hat\phi_y\hat\phi_{z_2}}\,\overbracket{\hat\phi_{z_3}\hat\phi_{z_4}}$ the leg permutations $\tau \in S_4$ with $\tau\cdot P = P$ must fix legs 1 and 2 and preserve $\{3, 4\}$. The leg paired with an external point is fixed, because $x$ and $y$ are fixed and each lies in only one block of $P$:
>
> $$
> \{x, \tau(1)\} \in \tau\cdot P = P \;\Rightarrow\; \tau(1) = 1, \qquad \{y, \tau(2)\} \in P \;\Rightarrow\; \tau(2) = 2, \qquad\text{so}\quad \tau \in \{\mathrm{id}, (3\,4)\} ,
> $$
>
> and the loop flip is a symmetry, $(3\,4)\cdot P = \{x1, y2, 43\} = P$:
>
> $$
> \operatorname{Aut}(P) = \{\mathrm{id},\ (3\,4)\}, \qquad S = 2 = \frac{24}{12} .
> $$
>
> - Product rule ([[§CA.7 Pairings, Diagrams and Symmetry Factors#^thm-ca-7-9|Theorem §CA.7.9]]): $|\Gamma| = 1$, one loop, $m(x, z) = m(y, z) = 1$: $S = 1\cdot2^1\,1!\cdot1!\,1! = 2$ ("reflection of internal line a symmetry", slide 18).
>
> *The figure-eight* (times the line $x$–$y$): two loops at $z$.
> - Counting: the contractions are the three of row (a),
>
> $$
> \overbracket{\hat\phi_x\hat\phi_y}\,\overbracket{\hat\phi_{z_1}\hat\phi_{z_2}}\,\overbracket{\hat\phi_{z_3}\hat\phi_{z_4}},\qquad \overbracket{\hat\phi_x\hat\phi_y}\,\overbracket{\hat\phi_{z_1}\hat\phi_{z_3}}\,\overbracket{\hat\phi_{z_2}\hat\phi_{z_4}},\qquad \overbracket{\hat\phi_x\hat\phi_y}\,\overbracket{\hat\phi_{z_1}\hat\phi_{z_4}}\,\overbracket{\hat\phi_{z_2}\hat\phi_{z_3}},
> $$
>
> each $= D_F(x - y)\,D_F(z - z)^2$: $3!! = 3$ of 24, $\frac{3}{24} = \frac18$.
> - Symmetry: the $\tau \in S_4$ that map the pairing $\{\{1,2\},\{3,4\}\}$ of the legs to itself are
>
> $$
> \operatorname{Aut}(P) = \{\mathrm{id},\ (1\,2),\ (3\,4),\ (1\,2)(3\,4),\ (1\,3)(2\,4),\ (1\,4)(2\,3),\ (1\,3\,2\,4),\ (1\,4\,2\,3)\}, \qquad S = 8 = \frac{24}{3} :
> $$
>
> reverse either loop, $(1\,2)$ or $(3\,4)$, and exchange the loops, $(1\,3)(2\,4)$, with all their products. These are the permutations that preserve the partition $\{\{1,2\},\{3,4\}\}$; they form the dihedral group $D_4$ of order 8 (the symmetries of a square with corners $1, 3, 2, 4$ in cyclic order), generated by $(1\,2)$, $(3\,4)$, $(1\,3)(2\,4)$:
>
> $$
> \operatorname{Aut}(P) = \underbrace{\{\mathrm{id}, (1\,2), (3\,4), (1\,2)(3\,4)\}}_{\text{loop flips: }2^2 = 4}\;\sqcup\;(1\,3)(2\,4)\cdot\{\mathrm{id}, (1\,2), (3\,4), (1\,2)(3\,4)\} = \{\mathrm{id}, (1\,2), (3\,4), (1\,2)(3\,4)\}\sqcup\{(1\,3)(2\,4),\ (1\,4\,2\,3),\ (1\,3\,2\,4),\ (1\,4)(2\,3)\} .
> $$
>
> The loop flips give only $2^2 = 4$; the extra factor 2 is the exchange of the two loops, $(1\,3)(2\,4)\cdot\{\{1,2\},\{3,4\}\} = \{\{3,4\},\{1,2\}\}$. With one vertex it is a permutation of legs, not of vertices ($\sigma = \mathrm{id}$).
> - Product rule: $|\Gamma| = 1$, two loops at $z$: $S = 2^2\cdot2! = 8 = 2^3$ ("three reflection symmetries", slide 18).
>
> These are the two coefficients of [[§C6a.7 Feynman Diagrams for Correlation Functions#^thm-c6a-7-1|Theorem §C6a.7.1]] (slide 17: "In the example (two point function at first order): S = 8 and 2 ⇒ factors $\frac18$, $\frac12$"). Every pairing lies in one of the two orbits ([[§CA.7 Pairings, Diagrams and Symmetry Factors#^thm-ca-7-5|Theorem §CA.7.5]], [[§CA.7 Pairings, Diagrams and Symmetry Factors#^thm-ca-7-6|Corollary §CA.7.6]]):
>
> $$
> 15 = 12 + 3 = \frac{24}{2} + \frac{24}{8} = \frac{|G_1|}{S_{\rm tadpole}} + \frac{|G_1|}{S_{\text{line}\,\times\,\text{figure-eight}}} .
> $$
>
> *Source: PHY 513 Lecture 14, slides 17–18 · PS §4.4, p. 93 ($S = 2$, $S = 2\cdot2\cdot2 = 8$) · Yu §7.3, eqs. (7.124) ($S = 2$, Fig. 7.13) and (7.125) ($S = 8$, Fig. 7.14) · the user's PHY 513 notes, Ch. 14 §14.5, Figure "Symmetry factors" ("12 of 4!", "3 of 4!") · the user's note "Symmetry Factors and the Orbit–Stabilizer Theorem" (Oct 2026), Example "The fifteen pairings" (orbits, stabilizers $\{e, (3\,4)\}$ and $D_4$, the count $15 = 24/2 + 24/8$) · stabilizers checked by enumeration over $S_4$*

^ex-c6a-9-1

![[ph-qft-c6-9-2.svg]]
*The fifteen pairings of [[§C6a.9 Symmetry Factors in Practice#^ex-c6a-9-1|Example §C6a.9.1]] as two orbits of $G_1 = S_4$ (orange: leg $a$ of the vertex; $\{x1, y2, 34\}$ means the blocks $\{x, 1\}$, $\{y, 2\}$, $\{3, 4\}$). (a) Three of the 12 tadpole pairings, and the loop flip $(3\,4)$, which maps $P_0$ to itself. (b) The pairing $Q_0$ of the line times the figure-eight and three of its 8 symmetries: reverse the left loop, reverse the right loop, exchange the loops. Added figure; drawings from the user's note on symmetry factors and orbit–stabilizer (Oct 2026), Example "The fifteen pairings".*

> [!example] Example §C6a.9.2: The Melon: S = 48 by Counting
> Two vertices $z_1$, $z_2$, no external points, four lines from $z_1$ to $z_2$ (the slides' "melonic vacuum bubble (pumpkin diagram)"). Write $\hat\phi_{(v,a)}$ for the $a$-th factor of $\hat\phi_I(z_v)^4$.
>
> **Step 1** (prefactor). Second order ([[§C6a.8 Position-Space Feynman Rules#^der-c6a-8-1|Derivation §C6a.8.1]], Step 1):
>
> $$
> \frac{1}{2!}\Bigl(\frac{1}{4!}\Bigr)^2 = \frac{1}{2\cdot576} = \frac{1}{1152} :
> $$
>
> $\frac12$ from expanding the exponential to second order, $\frac{1}{4!}$ from each vertex.
>
> **Step 2** (Wick's theorem for the eight fields). By [[§C6a.6 Wick's Theorem#^thm-c6a-6-2|Theorem §C6a.6.2]],
>
> $$
> \begin{aligned}
> T\{\hat\phi_{(1,1)}\cdots\hat\phi_{(1,4)}\hat\phi_{(2,1)}\cdots\hat\phi_{(2,4)}\} ={}& :\!\hat\phi_{(1,1)}\cdots\hat\phi_{(2,4)}\!: &&1\text{ term}\\
> &+ \overbracket{\hat\phi_{(1,1)}\hat\phi_{(2,1)}}\,:\!\hat\phi_{(1,2)}\hat\phi_{(1,3)}\hat\phi_{(1,4)}\hat\phi_{(2,2)}\hat\phi_{(2,3)}\hat\phi_{(2,4)}\!: + \cdots &&\tbinom82 = 28\text{ terms}\\
> &+ \overbracket{\hat\phi_{(1,1)}\hat\phi_{(2,1)}}\,\overbracket{\hat\phi_{(1,2)}\hat\phi_{(2,2)}}\,:\!\hat\phi_{(1,3)}\hat\phi_{(1,4)}\hat\phi_{(2,3)}\hat\phi_{(2,4)}\!: + \cdots &&\tbinom84\cdot3 = 210\text{ terms}\\
> &+ \overbracket{\hat\phi_{(1,1)}\hat\phi_{(2,1)}}\,\overbracket{\hat\phi_{(1,2)}\hat\phi_{(2,2)}}\,\overbracket{\hat\phi_{(1,3)}\hat\phi_{(2,3)}}\,:\!\hat\phi_{(1,4)}\hat\phi_{(2,4)}\!: + \cdots &&\tbinom86\cdot15 = 420\text{ terms}\\
> &+ \overbracket{\hat\phi_{(1,1)}\hat\phi_{(2,1)}}\,\overbracket{\hat\phi_{(1,2)}\hat\phi_{(2,2)}}\,\overbracket{\hat\phi_{(1,3)}\hat\phi_{(2,3)}}\,\overbracket{\hat\phi_{(1,4)}\hat\phi_{(2,4)}} + \cdots &&7!! = 105\text{ terms} .
> \end{aligned}
> $$
>
> **Step 3** (vacuum value). The terms with $8$, $6$, $4$ or $2$ fields in the colons give $\langle0|:\!\cdots\!:|0\rangle = 0$ ([[§C6a.5 Normal Ordering and Contractions#^thm-c6a-5-1|Theorem §C6a.5.1]], 2); the 105 complete contractions survive.
>
> **Step 4** (the melon's contractions). A complete contraction is a melon exactly when every bracket joins a leg of $z_1$ to a leg of $z_2$. Such a contraction pairs leg $a$ of $z_1$ with leg $\pi(a)$ of $z_2$ for a permutation $\pi \in S_4$:
>
> $$
> P_\pi = \overbracket{\hat\phi_{(1,1)}\hat\phi_{(2,\pi(1))}}\,\overbracket{\hat\phi_{(1,2)}\hat\phi_{(2,\pi(2))}}\,\overbracket{\hat\phi_{(1,3)}\hat\phi_{(2,\pi(3))}}\,\overbracket{\hat\phi_{(1,4)}\hat\phi_{(2,\pi(4))}} = D_F(z_1 - z_2)^4, \qquad \pi \in S_4,
> $$
>
> e.g. $\pi = \mathrm{id}$ gives the last line of Step 2, and $\pi = (1\,2)$ gives $\overbracket{\hat\phi_{(1,1)}\hat\phi_{(2,2)}}\,\overbracket{\hat\phi_{(1,2)}\hat\phi_{(2,1)}}\,\overbracket{\hat\phi_{(1,3)}\hat\phi_{(2,3)}}\,\overbracket{\hat\phi_{(1,4)}\hat\phi_{(2,4)}}$. Distinct $\pi$ give distinct pairings, so there are $4! = 24$ melon contractions.
>
> **Step 5** (ratio).
>
> $$
> \frac{1}{1152}\cdot24 = \frac{24}{2\cdot(4!)^2} = \frac{1}{2\cdot4!} = \frac{1}{48} :
> $$
>
> one $4!$ cancels, the other and the $\frac12$ do not ("only 4! cancel", slide 18).
>
> **Step 6** (as a symmetry). The automorphisms $(\tau_1, \tau_2; \sigma)$ of $P_\pi$ ([[§CA.7 Pairings, Diagrams and Symmetry Factors#^def-ca-7-4|Def. §CA.7.4]]):
> - $\sigma = \mathrm{id}$: the block $\{(1,a), (2,\pi(a))\}$ goes to $\{(1,\tau_1(a)), (2,\tau_2\pi(a))\}$, a block of $P_\pi$ iff $\tau_2\pi(a) = \pi\tau_1(a)$ for all $a$: $\tau_2 = \pi\tau_1\pi^{-1}$, one for each of the $24$ choices of $\tau_1$;
> - $\sigma = (1\,2)$: the block goes to $\{(2,\tau_2(a)), (1,\tau_1\pi(a))\}$, a block of $P_\pi$ iff $\tau_2(a) = \pi\tau_1\pi(a)$: $\tau_2 = \pi\tau_1\pi$, again $24$.
>
> $$
> S = |\operatorname{Aut}(P_\pi)| = 24 + 24 = 48 = \frac{1152}{24} .
> $$
>
> Product rule ([[§CA.7 Pairings, Diagrams and Symmetry Factors#^thm-ca-7-9|Theorem §CA.7.9]]): the four lines form one bundle, $m(z_1, z_2) = 4$, and the two vertices can be exchanged, $|\Gamma| = 2$: $S = 2\cdot4! = 48$. The lecture's test: describe the diagram to a friend who is not looking at the blackboard, "from vertex one to vertex two, four times." The friend has $4!$ orders in which to draw the lines and can put either vertex on top; the prescription does not distinguish these, which is why they count as one diagram.
>
> *Source: PHY 513 Lecture 14, slide 18 ("Permutation symmetry of all lines ⇒ $\frac12\frac{1}{4!^2}$ but only 4! cancel"), and transcript · the user's PHY 513 notes, Ch. 14 §14.5 (Derivation "The melon: S = 48 by counting") · term counts and stabilizer checked by enumeration*

^ex-c6a-9-2

> [!example] Example §C6a.9.3: The Other Second-Order Vacuum Bubbles
> Notation and the 105 complete contractions of the eight fields as in [[§C6a.9 Symmetry Factors in Practice#^ex-c6a-9-2|Example §C6a.9.2]], Steps 2–3; $N = 1152$.
>
> *The dumbbell*: one loop at each of $z_1$, $z_2$ and two lines between them.
> - Counting: the contractions are
>
> $$
> \overbracket{\hat\phi_{(1,a)}\hat\phi_{(1,b)}}\,\overbracket{\hat\phi_{(2,c)}\hat\phi_{(2,d)}}\,\overbracket{\hat\phi_{(1,a')}\hat\phi_{(2,c')}}\,\overbracket{\hat\phi_{(1,b')}\hat\phi_{(2,d')}} = D_F(z_1 - z_1)\,D_F(z_2 - z_2)\,D_F(z_1 - z_2)^2 ,
> $$
>
> with the loop legs $\{a, b\}$ and $\{c, d\}$ each one of the six two-element subsets
>
> $$
> \{1,2\},\ \{1,3\},\ \{1,4\},\ \{2,3\},\ \{2,4\},\ \{3,4\},
> $$
>
> $\{a', b'\}$ ($a' < b'$) and $\{c', d'\}$ the complements, and $(c', d')$ one of the two orders of $\{c', d'\}$: $6\cdot6\cdot2 = 72$ of 1152, $\frac{72}{1152} = \frac{1}{16}$.
> - Product rule: $|\Gamma| = 2$ (exchanging the vertices keeps $\ell = 1$ at each and $m(z_1, z_2) = 2$), one loop at each vertex, a double line: $S = 2\cdot(2^1\,1!)(2^1\,1!)\cdot2! = 16 = \frac{1152}{72}$.
>
> *Two figure-eights*: a figure-eight at each vertex.
> - Counting: each vertex pairs its four legs among themselves in one of the three ways $\{\{1,2\},\{3,4\}\}$, $\{\{1,3\},\{2,4\}\}$, $\{\{1,4\},\{2,3\}\}$, e.g.
>
> $$
> \overbracket{\hat\phi_{(1,1)}\hat\phi_{(1,2)}}\,\overbracket{\hat\phi_{(1,3)}\hat\phi_{(1,4)}}\,\overbracket{\hat\phi_{(2,1)}\hat\phi_{(2,3)}}\,\overbracket{\hat\phi_{(2,2)}\hat\phi_{(2,4)}} = D_F(z_1 - z_1)^2\,D_F(z_2 - z_2)^2 ;
> $$
>
> $3\cdot3 = 9$ of 1152, $\frac{9}{1152} = \frac{1}{128}$.
> - Product rule: $|\Gamma| = 2$, two loops at each vertex: $S = 2\cdot(2^2\,2!)(2^2\,2!) = 2\cdot8\cdot8 = 128 = \frac{1152}{9}$.
>
> With the melon ([[§C6a.9 Symmetry Factors in Practice#^ex-c6a-9-2|Example §C6a.9.2]]) these exhaust the eight legs of two vertices:
>
> $$
> \underbrace{24}_{\text{melon}} + \underbrace{72}_{\text{dumbbell}} + \underbrace{9}_{\text{two figure-eights}} = 105 = 7!!
> $$
>
> ([[§CA.7 Pairings, Diagrams and Symmetry Factors#^ex-ca-7-1|Example §CA.7.1]]): a complete contraction with no bracket inside a vertex is a melon; with one bracket inside $z_1$, the two remaining legs of $z_1$ go to $z_2$ and $z_2$ has one inside bracket too (dumbbell); with two brackets inside $z_1$, all of $z_2$ is paired inside (two figure-eights).
>
> *Source: the user's PHY 513 notes, Ch. 14 §14.5, Figure "Symmetry factors" ($S = 2\cdot2\cdot2!\cdot2 = 16$, "72 of $2\cdot4!^2$"; $S = 8\cdot8\cdot2 = 128$, "9 of $2\cdot4!^2$") · counts checked by enumeration*

^ex-c6a-9-3

> [!example] Example §C6a.9.4: Three Second-Order Corrections to the Two-Point Function
> The fields are $\hat\phi_x$, $\hat\phi_y$ and $\hat\phi_{(v,a)}$, $v = 1, 2$, $a = 1, \dots, 4$; the surviving terms are complete contractions (Steps 3–4 of [[§C6a.8 Position-Space Feynman Rules#^der-c6a-8-1|Derivation §C6a.8.1]]); $N = 2!\,(4!)^2 = 1152$. Below, $v$ is one vertex and $w$ the other.
>
> *The snowman*: $x$ and $y$ joined to one vertex, two lines from it to the other, one loop at the other.
> - Counting: the contractions are
>
> $$
> \overbracket{\hat\phi_x\hat\phi_{(v,a)}}\,\overbracket{\hat\phi_y\hat\phi_{(v,b)}}\,\overbracket{\hat\phi_{(v,c)}\hat\phi_{(w,e)}}\,\overbracket{\hat\phi_{(v,d)}\hat\phi_{(w,f)}}\,\overbracket{\hat\phi_{(w,g)}\hat\phi_{(w,h)}} = D_F(x - z_v)D_F(y - z_v)D_F(z_v - z_w)^2D_F(z_w - z_w),
> $$
>
> with $v \in \{1, 2\}$ (2 choices), $(a, b)$ an ordered pair of distinct legs of $v$ ($4\cdot3$), $\{c, d\}$ the other two legs, $c < d$, $(e, f)$ an ordered pair of distinct legs of $w$ ($4\cdot3$), $\{g, h\}$ the rest:
>
> $$
> 2\cdot(4\cdot3)\cdot(4\cdot3) = 288 \text{ of } 1152, \qquad \frac{288}{1152} = \frac14 .
> $$
>
> The terms with $v = 2$ become those with $v = 1$ on renaming $z_1 \leftrightarrow z_2$ (Step 5 of [[§C6a.8 Position-Space Feynman Rules#^der-c6a-8-1|Derivation §C6a.8.1]]).
> - Symmetry: for $v = 1$, $(a, b) = (1, 2)$, $(c, d) = (3, 4)$, $(e, f) = (1, 2)$, $(g, h) = (3, 4)$, the vertex swap is excluded ($z_1$ is joined to $x$ and $y$) and
>
> $$
> \operatorname{Aut}(P) = \bigl\{(\mathrm{id}, \mathrm{id}),\ (\mathrm{id}, (3\,4)),\ ((3\,4), (1\,2)),\ ((3\,4), (1\,2)(3\,4))\bigr\} \quad ((\tau_1, \tau_2),\ \sigma = \mathrm{id}), \qquad S = 4 :
> $$
>
> reverse the loop at $z_2$, and exchange the two lines $z_1$–$z_2$ (which moves legs at both ends).
> - Product rule: $|\Gamma| = 1$, one loop, a double line: $S = 2\cdot2! = 4$.
>
> *The chain of two tadpoles*: $x$–$z_v$, a loop at $z_v$, $z_v$–$z_w$, a loop at $z_w$, $z_w$–$y$.
> - Counting: the contractions are
>
> $$
> \overbracket{\hat\phi_x\hat\phi_{(v,a)}}\,\overbracket{\hat\phi_{(v,b)}\hat\phi_{(v,c)}}\,\overbracket{\hat\phi_{(v,d)}\hat\phi_{(w,e)}}\,\overbracket{\hat\phi_{(w,f)}\hat\phi_{(w,g)}}\,\overbracket{\hat\phi_y\hat\phi_{(w,h)}} = D_F(x - z_v)D_F(z_v - z_v)D_F(z_v - z_w)D_F(z_w - z_w)D_F(z_w - y),
> $$
>
> with $v \in \{1, 2\}$ (2), $a$ (4), $d \ne a$ (3), $\{b, c\}$ the rest of $v$; $h$ (4), $e \ne h$ (3), $\{f, g\}$ the rest of $w$:
>
> $$
> 2\cdot4\cdot3\cdot4\cdot3 = 288 \text{ of } 1152, \qquad \frac{288}{1152} = \frac14 .
> $$
>
> - Symmetry: for $v = 1$, $a = 1$, $\{b, c\} = \{2, 3\}$, $d = 4$, $e = 4$, $\{f, g\} = \{2, 3\}$, $h = 1$, no vertex symmetry ($z_1$ is joined to $x$, $z_2$ to $y$) and
>
> $$
> \operatorname{Aut}(P) = \{\mathrm{id}, (2\,3)\}\times\{\mathrm{id}, (2\,3)\} \quad (\tau_1, \tau_2), \qquad S = 4 .
> $$
>
> - Product rule: two loops, no vertex symmetry: $S = 2\cdot2 = 4$.
>
> *The sunset*: $x$ joined to one vertex, $y$ to the other, three lines between the two vertices.
> - Counting: the contractions are
>
> $$
> \overbracket{\hat\phi_x\hat\phi_{(v,a)}}\,\overbracket{\hat\phi_y\hat\phi_{(w,e)}}\,\overbracket{\hat\phi_{(v,b)}\hat\phi_{(w,\pi(b))}}\,\overbracket{\hat\phi_{(v,c)}\hat\phi_{(w,\pi(c))}}\,\overbracket{\hat\phi_{(v,d)}\hat\phi_{(w,\pi(d))}} = D_F(x - z_v)\,D_F(z_v - z_w)^3\,D_F(z_w - y),
> $$
>
> with $v \in \{1, 2\}$ and $a$ ($x$ to a leg of either vertex, $2\cdot4$), $e$ ($y$ to a leg of the other vertex, 4), $\{b, c, d\}$ the other legs of $v$, and $\pi$ a bijection from $\{b, c, d\}$ onto the legs of $w$ other than $e$ ($3!$):
>
> $$
> 2\cdot4\cdot4\cdot3! = 192 \text{ of } 1152, \qquad \frac{192}{1152} = \frac16 .
> $$
>
> - Symmetry: for $v = 1$, $a = e = 1$, $\pi(b) = b$ on $\{2, 3, 4\}$, the vertex swap is excluded ($z_1$ is joined to $x$, $z_2$ to $y$), the legs $(1, 1)$, $(2, 1)$ are fixed, and the block $\{(1, b), (2, b)\}$ goes to $\{(1, \tau_1(b)), (2, \tau_2(b))\}$, a block iff $\tau_2(b) = \tau_1(b)$:
>
> $$
> \operatorname{Aut}(P) = \bigl\{(\rho, \rho) : \rho \in \operatorname{Sym}\{2, 3, 4\}\bigr\} \cong S_3 \quad ((\tau_1, \tau_2),\ \sigma = \mathrm{id}), \qquad S = 3! = 6 = \frac{1152}{192} :
> $$
>
> the three lines are permuted among themselves, both ends together.
> - Product rule: $|\Gamma| = 1$, a triple line: $S = 3! = 6$.
>
> *All $945$ second-order contractions.* The ten fields $\hat\phi_x$, $\hat\phi_y$, $\hat\phi_{(v,a)}$ have $9!! = 945$ complete contractions ([[§CA.7 Pairings, Diagrams and Symmetry Factors#^thm-ca-7-1|Theorem §CA.7.1]]); they split into seven diagrams ([[§CA.7 Pairings, Diagrams and Symmetry Factors#^thm-ca-7-6|Corollary §CA.7.6]]), three attached to $x$ and $y$ and four with a vacuum bubble:
>
> | diagram | contractions | $S = 1152/\text{contractions}$ |
> |---|---|---|
> | snowman | $288$ | $4$ |
> | chain of two tadpoles | $288$ | $4$ |
> | sunset | $192$ | $6$ |
> | tadpole $\times$ figure-eight | $72$ | $16 = 2\cdot8$ |
> | line $\times$ melon | $24$ | $48$ |
> | line $\times$ dumbbell | $72$ | $16$ |
> | line $\times$ two figure-eights | $9$ | $128$ |
>
> $$
> 288 + 288 + 192 + 72 + 24 + 72 + 9 = 945 = 9!! .
> $$
>
> The last four cancel against the denominator ([[§C6a.11 The iε Limit and Vacuum Bubbles#^ex-c6a-11-3|Example §C6a.11.3]], [[§C6a.11 The iε Limit and Vacuum Bubbles#^thm-c6a-11-5|Theorem §C6a.11.5]]).
>
> *Source: the user's PHY 513 notes, Ch. 14 §14.5, Figure "Symmetry factors" ($S = 2\cdot2! = 4$, $S = 2\cdot2 = 4$, "288 of $2\cdot4!^2$"; the sunset, $S = 6$) · Yu §7.3, eqs. (7.131)–(7.132) and Fig. 7.15(c) (the snowman, $S = 4$), eqs. (7.127)–(7.128) and Fig. 7.15(a) (the chain, $S = 4$), eqs. (7.129)–(7.130) and Fig. 7.15(b) (the sunset, $S = 6$) · PS §4.4, p. 93 (the sunset, $S = 3! = 6$) · PHY 513, Problem Set 8, Problem 1(a)(b) (the sunset, by counting, $N = 2\cdot4\cdot4\cdot3! = 192$, and by its stabilizer, $S_3$ on the three lines) · counts, stabilizers and the 945 checked by enumeration (`qft-C/tools/hw8/check_hw8.py`)*

^ex-c6a-9-4

> [!example] Example §C6a.9.5: The Four Diagrams of Problem Set 8, Problem 1(a)
> The user's setup: a diagram with $n$ vertices and external points $x_1, \dots, x_r$ comes from the order-$\lambda^n$ term $\frac{1}{n!}\bigl(\frac{-i\lambda}{4!}\bigr)^n\int d^4z_1\cdots d^4z_n\,\langle0|T\{\hat\phi_I(x_1)\cdots\hat\phi_I(x_r)\hat\phi_I(z_1)^4\cdots\hat\phi_I(z_n)^4\}|0\rangle$ of the numerator; if $N_D$ complete contractions produce it, all give the same integral, and ([[§C6a.8 Position-Space Feynman Rules#^thm-c6a-8-1|Theorem §C6a.8.1]])
>
> $$
> \text{diagram} = \frac{1}{S}\,(-i\lambda)^n\int d^4z_1\cdots d^4z_n\prod D_F, \qquad S = \frac{n!\,(4!)^n}{N_D} = |\operatorname{Stab}(P)| ,
> $$
>
> the second form by orbit–stabilizer ([[§CA.7 Pairings, Diagrams and Symmetry Factors#^thm-ca-7-5|Theorem §CA.7.5]]); the solution calls the number of vertices $k$ and $N_D$ simply $N$. The four diagrams (the table of the user's note on symmetry factors):
>
> | diagram | $n$ | $\lvert G_n\rvert$ | $N_D$ | $\operatorname{Stab}(P)$ | $S$ |
> |---|---|---|---|---|---|
> | (a) tadpole, 2-point | $1$ | $24$ | $4\cdot3 = 12$ | the loop flip | $2$ |
> | (b) sunset, 2-point | $2$ | $1152$ | $2\cdot4\cdot4\cdot3! = 192$ | $S_3$ on the three lines | $6$ |
> | (c) fish, 4-point | $2$ | $1152$ | $2\cdot(4\cdot3)^2\cdot2 = 576$ | $S_2$ on the two lines | $2$ |
> | (d) triangle, 6-point | $3$ | $82\,944$ | $3!\cdot(4\cdot3)^3\cdot8 = 82\,944$ | trivial | $1$ |
>
> (a) is the tadpole of [[§C6a.9 Symmetry Factors in Practice#^ex-c6a-9-1|Example §C6a.9.1]], (b) the sunset of [[§C6a.9 Symmetry Factors in Practice#^ex-c6a-9-4|Example §C6a.9.4]], counted there in the same way.
>
> *(c) The fish*: $x_1, x_2$ at one vertex, $x_3, x_4$ at the other, two lines between them.
> - Counting: the contractions are
>
> $$
> \overbracket{\hat\phi_{x_1}\hat\phi_{(v,a)}}\,\overbracket{\hat\phi_{x_2}\hat\phi_{(v,b)}}\,\overbracket{\hat\phi_{x_3}\hat\phi_{(w,e)}}\,\overbracket{\hat\phi_{x_4}\hat\phi_{(w,f)}}\,\overbracket{\hat\phi_{(v,c)}\hat\phi_{(w,g)}}\,\overbracket{\hat\phi_{(v,d)}\hat\phi_{(w,h)}} = D_F(x_1 - z_v)D_F(x_2 - z_v)\,D_F(z_v - z_w)^2\,D_F(x_3 - z_w)D_F(x_4 - z_w),
> $$
>
> with $v \in \{1, 2\}$ and $a$ ($x_1$ to a leg of either vertex, $2\cdot4$), $b \ne a$ (3), $(e, f)$ an ordered pair of distinct legs of $w$ ($4\cdot3$), $\{c, d\}$ the rest of $v$ with $c < d$, and $(g, h)$ one of the two orders of the rest of $w$ (2):
>
> $$
> 2\cdot4\cdot3\cdot4\cdot3\cdot2 = 2\cdot(4\cdot3)^2\cdot2 = 576 \text{ of } 1152, \qquad S = \frac{2!\,(4!)^2}{576} = 2 .
> $$
>
> - Symmetry: for $v = 1$, $(a, b) = (e, f) = (1, 2)$, $(c, d) = (g, h) = (3, 4)$. Exchanging $z_1, z_2$ would carry the legs paired with $x_1, x_2$ to $z_2$, so $\sigma = \mathrm{id}$; legs 1, 2 of both vertices are fixed; the blocks $\{(1,3),(2,3)\}$, $\{(1,4),(2,4)\}$ go to $\{(1,\tau_1(3)),(2,\tau_2(3))\}$, $\{(1,\tau_1(4)),(2,\tau_2(4))\}$, blocks iff $\tau_2 = \tau_1$ on $\{3, 4\}$:
>
> $$
> \operatorname{Aut}(P) = \bigl\{(\mathrm{id}, \mathrm{id}),\ ((3\,4), (3\,4))\bigr\}, \qquad S = 2 = \frac{1152}{576} :
> $$
>
> exchange the two lines, both ends together. Product rule ([[§CA.7 Pairings, Diagrams and Symmetry Factors#^thm-ca-7-9|Theorem §CA.7.9]]): $|\Gamma| = 1$, a double line, $S = 2! = 2$.
>
> *(d) The triangle*: vertices $A$, $B$, $C$ carrying the pairs $(x_1, x_2)$, $(x_3, x_4)$, $(x_5, x_6)$, joined pairwise.
> - Counting: the three pairs go to the three vertices ($3!$); each pair to two of the four legs of its vertex ($4\cdot3$ per pair); the line $AB$ uses one free leg of $A$ and one of $B$ ($2\cdot2$), the line $BC$ the last leg of $B$ and one of the two free legs of $C$ (2), and $CA$ is then fixed (1). With legs $a_1, \dots, a_4$ of $A$ etc.,
>
> $$
> \overbracket{\hat\phi_{x_1}\hat\phi_{(A,a_1)}}\,\overbracket{\hat\phi_{x_2}\hat\phi_{(A,a_2)}}\cdots\overbracket{\hat\phi_{x_6}\hat\phi_{(C,c_2)}}\;\overbracket{\hat\phi_{(A,a_3)}\hat\phi_{(B,b_4)}}\,\overbracket{\hat\phi_{(B,b_3)}\hat\phi_{(C,c_4)}}\,\overbracket{\hat\phi_{(C,c_3)}\hat\phi_{(A,a_4)}} = \prod_{i=1}^6D_F(x_i - z_{v(i)})\;D_F(z_A - z_B)D_F(z_B - z_C)D_F(z_C - z_A),
> $$
>
> $v(i)$ the vertex of $x_i$, and
>
> $$
> N_D = 3!\cdot(4\cdot3)^3\cdot(2\cdot2\cdot2\cdot1) = 82\,944, \qquad S = \frac{3!\,(4!)^3}{3!\,(4\cdot3)^3\cdot8} = \frac{(2!)^3}{8} = 1 .
> $$
>
> - Symmetry: every vertex carries external points, so $\sigma = \mathrm{id}$ and the two legs paired with external points are fixed at each vertex. What remains is the exchange of the two internal legs at a vertex. At $C$ alone, $(c_3\,c_4)$ sends $\{(B,b_3),(C,c_4)\}$ to $\{(B,b_3),(C,c_3)\}$, not a block of $P$: the line from $B$ now ends on the leg of $C$ that faced $A$, the same drawing but a different pairing (figure below, (c)–(d)). An exchange at $A$ or at $B$, alone or together with others, sends the line $\{(A,a_3),(B,b_4)\}$ to $\{(A,a_4),(B,b_4)\}$, $\{(A,a_3),(B,b_3)\}$ or $\{(A,a_4),(B,b_3)\}$, none a block of $P$. So
>
> $$
> \operatorname{Aut}(P) = \{e\}, \qquad S = 1 .
> $$
>
> Product rule: $|\Gamma| = 1$, no loops, all multiplicities 1, $S = 1$.
>
> In (b) and (c) the vertex exchange is excluded because both vertices are joined to external points (Step 3 of [[§CA.7 Pairings, Diagrams and Symmetry Factors#^der-ca-7-9|Derivation §CA.7.9]], external edges); in (d) every external leg is fixed and the internal legs cannot be exchanged.
>
> *Source: PHY 513, Problem Set 8, Problem 1(a) (the user's solution: both counts and the stabilizers, with exploded-vertex drawings) · the user's note "Symmetry Factors and the Orbit–Stabilizer Theorem" (Oct 2026), Example "The diagrams of PHY 513 HW 8, Problem 1(a)" (the table) · counts and stabilizers checked by enumeration (`qft-C/tools/hw8/check_hw8.py`)*

^ex-c6a-9-5

![[ph-qft-c6-9-3.svg]]
*The user's exploded-vertex drawings for [[§C6a.9 Symmetry Factors in Practice#^ex-c6a-9-5|Example §C6a.9.5]]: each vertex a dashed circle, its legs separate dots (orange), internal lines red. (a) Sunset: a symmetry applies the same $\pi \in S_3$ to the legs $1, 2, 3$ and $a, b, c$, permuting the three lines. (b) Fish: the only symmetry exchanges the two lines. (c) A triangle pairing $P$; (d) exchanging the two internal legs at $C$ gives the same drawing but a different pairing, so it is not a symmetry, $S = 1$. Added figure, adapted from the user's solution of PHY 513, Problem Set 8, Problem 1(a).*

> [!example] Example §C6a.9.6: PS's Cactus, a Third-Order Example
> PS's third-order contraction (eq. (4.45)): $x$–$z$, a loop at $z$, $z$–$w$, $w$–$y$, two lines from $w$ to $u$, a loop at $u$, with value
>
> $$
> \frac{1}{3!}\Bigl(\frac{-i\lambda}{4!}\Bigr)^3\int d^4z\,d^4w\,d^4u\,D_F(x - z)D_F(z - z)D_F(z - w)D_F(w - y)D_F^2(w - u)D_F(u - u)
> $$
>
> per contraction.
> - *The contractions.* Assign the roles $z, w, u$ to the vertices $1, 2, 3$ (a bijection, $3!$ ways) and write $\hat\phi_{(z,a)}$ for leg $a$ of the vertex playing $z$:
>
> $$
> \overbracket{\hat\phi_x\hat\phi_{(z,a)}}\,\overbracket{\hat\phi_{(z,b)}\hat\phi_{(z,c)}}\,\overbracket{\hat\phi_{(z,d)}\hat\phi_{(w,e)}}\,\overbracket{\hat\phi_{(w,f)}\hat\phi_y}\,\overbracket{\hat\phi_{(w,g)}\hat\phi_{(u,i)}}\,\overbracket{\hat\phi_{(w,h)}\hat\phi_{(u,j)}}\,\overbracket{\hat\phi_{(u,k)}\hat\phi_{(u,l)}},
> $$
>
> with $a$ (4), $d \ne a$ (3) and $\{b, c\}$ the rest at $z$; $e$ (4), $f \ne e$ (3) and $\{g, h\}$ the rest, $g < h$, at $w$; $(i, j)$ an ordered pair of distinct legs (4·3) and $\{k, l\}$ the rest at $u$:
>
> $$
> 3!\cdot(4\cdot3)\cdot(4\cdot3)\cdot(4\cdot3) = 6\cdot1728 = 10\,368 .
> $$
>
> - *Counting* (PS): $3!$ (interchange of vertices) $\times\;4\cdot3$ (placement of contractions into the $z$ vertex) $\times\;4\cdot3\cdot2$ (into the $w$ vertex) $\times\;4\cdot3$ (into the $u$ vertex) $\times\;\frac12$ (interchange of the $w$–$u$ contractions) $= 6\cdot12\cdot24\cdot12\cdot\frac12 = 10\,368$, the same number ($4\cdot3\cdot2\cdot\frac12 = 12$ for the two $w$–$u$ lines), "roughly 1/13 of the total of 135,135 possible full contractions of the 14 operators". The relabelling group has $3!\,(4!)^3 = 6\cdot13\,824 = 82\,944$ elements, and
>
> $$
> \frac{10\,368}{82\,944} = \frac18 .
> $$
>
> - *Symmetry*: every vertex is distinguished (only $z$ is joined to $x$, only $w$ to $y$, $u$ to neither), so $\sigma = \mathrm{id}$, and for the contraction with $(a, b, c, d) = (1, 2, 3, 4)$, $(e, f, g, h) = (1, 2, 3, 4)$, $(i, j, k, l) = (1, 2, 3, 4)$,
>
> $$
> \operatorname{Aut}(P) = \{\mathrm{id}, (2\,3)_z\}\times\{\mathrm{id}, (3\,4)_u\}\times\{\mathrm{id}, (3\,4)_w(1\,2)_u\}, \qquad S = 2\cdot2\cdot2 = 8 = \frac{82\,944}{10\,368} :
> $$
>
> reverse the loop at $z$, reverse the loop at $u$, exchange the two lines $w$–$u$.
> - *Product rule*: $2$ (loop at $z$) $\cdot\,2$ (loop at $u$) $\cdot\,2!$ (double line $w$–$u$), no vertex symmetry: $S = 8 = 2\cdot2\cdot2$ (PS p. 93: "Two factors of 2 come from lines that start and end on the same vertex … The other factor of 2 comes from the two propagators connecting $w$ to $u$").
>
> *Source: PS §4.4, pp. 92–93, eq. (4.45) and the "cactus" diagram · enumeration of the 135 135 pairings of 14 fields (10 368 produce the cactus)*

^ex-c6a-9-6

![[ph-qft-c6-9-1.svg]]
*Symmetry factors of the examples, with the number of complete contractions that produce each diagram out of the $n!\,(4!)^n$ relabellings. Top: the first-order tadpole and figure-eight; the second-order vacuum bubbles (melon, dumbbell, two figure-eights). Bottom: the snowman, the chain and the sunset, the three second-order corrections to the two-point function, and PS's third-order cactus. Added figure; diagrams adapted from the user's PHY 513 notes, Figure "Symmetry factors", and PS pp. 92–93.*

## Oriented lines: the complex scalar

In the complex scalar theory every nonzero contraction joins a $\hat\phi$ to a $\hat\phi^\dagger$ ([[§C6a.7 Feynman Diagrams for Correlation Functions#^thm-c6a-7-2|Theorem §C6a.7.2]], 3), so lines carry arrows and the relabellings may permute legs only within each kind ([[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-4|Theorem §CA.8.4]]). Problem Set 8, Problem 1(b): "symmetry factors in complex scalar theory tend to be much smaller than in real scalar theory … because particles and anti-particles are distinct."

> [!theorem] Theorem §C6a.9.1: Symmetry Factors with Oriented Lines
> For the complex scalar with $\mathcal L_{\rm int} = -\frac\lambda4(\phi^\dagger\phi)^2$ ([[§C2a.5 The Complex Scalar Field and Its Charge#^mod-c2a-5-1|Model §C2a.5.1]] plus this term), the order-$\lambda^n$ term of a numerator with external fields $\hat\phi_I(x_i)$, $\hat\phi_I^\dagger(y_j)$ is
>
> $$
> \frac{1}{n!}\Bigl(\frac{-i\lambda}{4}\Bigr)^n\int d^4z_1\cdots d^4z_n\,\langle0|T\Bigl\{\prod_i\hat\phi_I(x_i)\prod_j\hat\phi_I^\dagger(y_j)\prod_{v=1}^n\bigl(\hat\phi_I^\dagger\hat\phi_I\bigr)^2(z_v)\Bigr\}|0\rangle = \sum_D\frac{(-i\lambda)^n}{S(D)}\int d^4z_1\cdots d^4z_n\prod_{\text{lines}}D_F ,
> $$
>
> the sum over the oriented diagrams $D$ (each line from a $\hat\phi^\dagger$ end to a $\hat\phi$ end, two arrows in and two out at each vertex), with
> 1. $S(D) = \dfrac{n!\,(2!\,2!)^n}{N_D} = |\operatorname{Stab}(P)|$, $N_D$ the number of contractions producing $D$;
> 2. every symmetry maps $\hat\phi$ legs to $\hat\phi$ legs and $\hat\phi^\dagger$ legs to $\hat\phi^\dagger$ legs: it preserves every arrow.
>
> *Source: PHY 513, Problem Set 8, Problem 1(b) (the user's solution: "$\frac14 = \frac{1}{2!\,2!}$ … $|G| = k!\,(2!\,2!)^k$ is again the inverse of the prefactor … A relabeling cannot exchange a $\hat\phi$ leg with a $\hat\phi^\dagger$ leg, so a symmetry must preserve every arrow") · the user's note "Symmetry Factors and the Orbit–Stabilizer Theorem" (Oct 2026), §8 (complex-scalar bullet) · proof written here*

^thm-c6a-9-1

> [!derivation]- Derivation
> **Step 1** (prefactor). $\hat{\mathcal H}_I = \frac\lambda4(\hat\phi_I^\dagger\hat\phi_I)^2$ (no derivatives), so the order-$n$ Dyson term carries $\frac{1}{n!}\bigl(\frac{-i\lambda}{4}\bigr)^n = \frac{(-i\lambda)^n}{n!\,(2!\,2!)^n}$, and each $(\hat\phi_I^\dagger\hat\phi_I)^2(z_v) = \hat\phi_I^\dagger\hat\phi_I^\dagger\hat\phi_I\hat\phi_I(z_v)$ contributes two $\hat\phi$ legs and two $\hat\phi^\dagger$ legs (the fields at one point commute, [[§C2a.5 The Complex Scalar Field and Its Charge#^mod-c2a-5-1|Model §C2a.5.1]]).
>
> **Step 2** (Wick). The vacuum value is the sum over complete pairings of all fields, each block a contraction ([[§C6a.6 Wick's Theorem#^thm-c6a-6-3|Theorem §C6a.6.3]]). A block $\hat\phi\hat\phi$ or $\hat\phi^\dagger\hat\phi^\dagger$ is $0$ and a block $\hat\phi(a)\hat\phi^\dagger(b)$ is $D_F(a - b)$ ([[§C6a.7 Feynman Diagrams for Correlation Functions#^thm-c6a-7-2|Theorem §C6a.7.2]], 3): only the pairings of $\mathcal P_\smile$ with kinds $\hat\phi \smile \hat\phi^\dagger$ survive ([[§CA.8 Splitting Pairings and the Exponential Formula#^def-ca-8-2|Def. §CA.8.2]]):
>
> $$
> \langle0|T\{\cdots\}|0\rangle = \sum_{P\in\mathcal P_\smile}\;\prod_{\{a,b\}\in P}D_F\bigl(\mathrm{pt}(a) - \mathrm{pt}(b)\bigr) .
> $$
>
> **Step 3** (invariance). Permuting the vertices and, at each vertex, the two $\hat\phi$ legs and the two $\hat\phi^\dagger$ legs ($G_n = (S_2\times S_2)^n \rtimes S_n$) maps $\mathcal P_\smile$ to itself and, after renaming the integration variables, does not change the integral (Step 5 of [[§C6a.8 Position-Space Feynman Rules#^der-c6a-8-1|Derivation §C6a.8.1]], with $D_F$ even).
>
> **Step 4** (orbits). By [[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-4|Theorem §CA.8.4]], 1–2, $|G_n| = n!\,(2!\,2!)^n$ and the sum over each orbit $D$ is $N_D = |G_n|/S(D)$ equal terms:
>
> $$
> \frac{(-i\lambda)^n}{n!\,(2!\,2!)^n}\sum_DN_D\int\prod D_F = \sum_D\frac{(-i\lambda)^n}{S(D)}\int\prod D_F .
> $$
>
> **Step 5** (part 2). [[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-4|Theorem §CA.8.4]], 3: elements of $G_n$ preserve kinds, so a symmetry maps the $\hat\phi$ end of each line to a $\hat\phi$ end; the image of a line has its arrow the same way.
>
> **What the derivation shows.**
> - The $\frac14$ in $\frac\lambda4(\phi^\dagger\phi)^2$ plays the role of the $\frac{1}{4!}$ of $\phi^4$: it is $\frac{1}{|S_2\times S_2|}$, and the vertex factor is again $-i\lambda$ ([[§C6b.6 Amplitudes from Correlation Functions#^thm-c6b-6-3|Theorem §C6b.6.3]]).
> - Fewer relabellings are allowed, so fewer can be symmetries: a loop cannot be flipped, and two lines can be exchanged only if they run the same way.

^der-c6a-9-1

*Uses:* [[§C6a.7 Feynman Diagrams for Correlation Functions#^thm-c6a-7-2|Theorem §C6a.7.2]], [[§C6a.6 Wick's Theorem#^thm-c6a-6-3|Theorem §C6a.6.3]], [[§CA.8 Splitting Pairings and the Exponential Formula#^def-ca-8-2|Def. §CA.8.2]], [[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-4|Theorem §CA.8.4]], [[§C6a.8 Position-Space Feynman Rules#^der-c6a-8-1|Derivation §C6a.8.1]]

> [!example] Example §C6a.9.7: The Three Oriented Diagrams of Problem Set 8, Problem 1(b)
> External fields $\hat\phi^\dagger(y)$ (arrow enters the diagram) and $\hat\phi(x)$ (arrow leaves); at a vertex an arrow enters at a $\hat\phi$ leg and leaves at a $\hat\phi^\dagger$ leg. $|G_1| = 1!\,(2!\,2!) = 4$, $|G_2| = 2!\,(2!\,2!)^2 = 32$ ([[§C6a.9 Symmetry Factors in Practice#^thm-c6a-9-1|Theorem §C6a.9.1]]).
>
> *(a) Oriented tadpole*: $y \to z \to x$, a loop at $z$ from its $\hat\phi^\dagger$ leg to its $\hat\phi$ leg.
> - Symmetry: the legs joined to $y$ and $x$ are fixed; what remains is one $\hat\phi$ leg and one $\hat\phi^\dagger$ leg, the two ends of the loop. Exchanging them would reverse the arrow, i.e. exchange a $\hat\phi$ leg with a $\hat\phi^\dagger$ leg, which is not in $G_1$: $\operatorname{Stab} = \{e\}$, $S = 1$.
> - Counting: $\hat\phi^\dagger(y)$ with one of the 2 $\hat\phi$ legs, $\hat\phi(x)$ with one of the 2 $\hat\phi^\dagger$ legs, the rest forced: $N_D = 2\cdot2 = 4 = |G_1|$, $S = 1$ (the real field's tadpole has $S = 2$, [[§C6a.9 Symmetry Factors in Practice#^ex-c6a-9-1|Example §C6a.9.1]]).
>
> *(b) Oriented fish*: $\hat\phi(x_1)$, $\hat\phi^\dagger(y_1)$ at one vertex and $\hat\phi(x_2)$, $\hat\phi^\dagger(y_2)$ at the other, so at each vertex one external line in and one out; two internal lines, one from left to right and one from right to left.
> - Symmetry: both vertices carry external lines, so they are not exchanged, and the four legs joined to external lines are fixed. The only candidate is the exchange of the two internal lines, but they run in opposite directions: it would send an incoming leg to an outgoing leg at each vertex. $\operatorname{Stab} = \{e\}$, $S = 1$.
> - Counting: the vertex of $(x_1, y_1)$ (2), $y_1$ and $x_1$ to its $\hat\phi$ and $\hat\phi^\dagger$ legs ($2\cdot2$), $y_2$ and $x_2$ likewise at the other ($2\cdot2$), the internal lines forced (1): $N_D = 2\cdot4\cdot4 = 32 = |G_2|$, $S = 1$ (real fish: $S = 2$, [[§C6a.9 Symmetry Factors in Practice#^ex-c6a-9-5|Example §C6a.9.5]]).
>
> *(c) Oriented sunset*: $y$ into the left vertex, $x$ out of the right one; line ① from right to left, lines ②, ③ from left to right.
> - Symmetry: the vertices are fixed by the external lines, and so are the two legs joined to them. Lines ② and ③ both run left to right, so exchanging them (both ends together) maps outgoing legs to outgoing legs and incoming to incoming and maps the pairing to itself; ① runs the other way and cannot be exchanged with either. $\operatorname{Stab} = \{e, \rho_{23}\}$ with $\rho_{23}$ the exchange of ② and ③, $S = 2$.
> - Counting: the vertex of $y$ (2), $y$ to one of its 2 $\hat\phi$ legs, $x$ to one of the 2 $\hat\phi^\dagger$ legs of the other (2·2); the remaining $\hat\phi$ leg of the left vertex goes to the single remaining $\hat\phi^\dagger$ leg of the right one (1), and its two $\hat\phi^\dagger$ legs to the two $\hat\phi$ legs on the right (2): $N_D = 2\cdot2\cdot2\cdot2 = 16$, $S = \frac{32}{16} = 2$ (real sunset: $S = 6$).
>
> *Source: PHY 513, Problem Set 8, Problem 1(b) (the user's solution: the three stabilizers, with drawings: filled = in, open = out) · counts checked by enumeration (`qft-C/tools/hw8/check_hw8.py`; all $120$ second-order pairings of the complex two-point function have $S \in \{1, 2, 8\}$)*

^ex-c6a-9-7

![[ph-qft-c6-9-4.svg]]
*The oriented diagrams of [[§C6a.9 Symmetry Factors in Practice#^ex-c6a-9-7|Example §C6a.9.7]] with each vertex opened into its legs: filled dots are $\hat\phi$ legs, where an arrow enters the vertex; open dots are $\hat\phi^\dagger$ legs, where it leaves. (a) The loop flip would exchange a filled and an open dot: not allowed, $S = 1$. (b) The two internal lines run in opposite directions: no exchange, $S = 1$. (c) Lines ② and ③ run the same way and can be exchanged: $S = 2$. Added figure, adapted from the user's solution of PHY 513, Problem Set 8, Problem 1(b).*

> [!remark] Remark: How much this matters
> Slide 18: "Details of symmetry factors are not a high priority in this course." The lecture: "this will drive you crazy, especially the night before the exam … don't lose sleep over this … don't overthink" (Problem Set 8, posted the evening before, has some). PS: "Most people never need to evaluate a diagram with a symmetry factor greater than 2, so there's no need to worry too much about these technicalities … When in doubt, you can always determine the symmetry factor by counting equivalent contractions" (p. 93). Large symmetry factors belong to diagrams with few external points, above all the vacuum bubbles, which drop out of correlation functions ([[§C6a.11 The iε Limit and Vacuum Bubbles#^thm-c6a-11-5|Theorem §C6a.11.5]]).
>
> *Source: PHY 513 Lecture 14, slide 18, and transcript · PS §4.4, p. 93 · the user's PHY 513 notes, Ch. 14 §14.5 (paragraph "How much this matters")*

^rem-c6a-9-2

> [!caution] Caution: "In QED the symmetry factor is always S = 1" holds for diagrams with external points
> Slide 18: "In QED the symmetry factor is always $S = 1$." The lecture's reason: "if it was a more complex theory in such a way that the $\phi$'s here weren't all the same, they actually truly meant something different, then we wouldn't have these annoying factors … that is exactly what's going to happen in QED. One of them has charge plus, the other has charge minus, one has a photon, and you can't just exchange them. They have different roles … By starting with this more pedagogical example, we unfortunately get the particular complexity that's not representative of some of the theories."
>
> For vacuum bubbles the statement fails. The QED vertex $\bar\psi\gamma^\mu\psi A_\mu$ has three legs of three kinds, pairable only as $\psi\smile\bar\psi$ and $A\smile A$, so the leg group is trivial and $|G_n| = n!$ ([[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-4|Theorem §CA.8.4]], 1). At $n = 2$ the bubble with one fermion loop through both vertices and a photon line between them comes from the single pairing
>
> $$
> \bigl\{\{\psi_1, \bar\psi_2\},\ \{\psi_2, \bar\psi_1\},\ \{A_1, A_2\}\bigr\}, \qquad N_D = 1, \qquad S = \frac{2!}{1} = 2 :
> $$
>
> exchanging the two vertices maps the oriented loop and the photon line to themselves. Likewise two fermion loops joined by a photon, $\{\{\psi_1, \bar\psi_1\}, \{\psi_2, \bar\psi_2\}, \{A_1, A_2\}\}$, has $S = 2$. With an external point the slide's statement holds: a symmetry fixes the vertex of an external leg ([[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-4|Theorem §CA.8.4]], 3), hence (trivial leg group) all its legs, hence the partner leg of each and its vertex, and so on through the connected diagram: $S = 1$. Vacuum bubbles cancel ([[§C6a.11 The iε Limit and Vacuum Bubbles#^thm-c6a-11-5|Theorem §C6a.11.5]]), so the slide is right for everything that is computed.
>
> *Source: PHY 513 Lecture 14, slide 18, and transcript · PHY 513, Problem Set 8, Problem 1(b), statement ("symmetry factors are usually small and they are often 1") · the counterexample written here (recorded in `qft-C/ERRATA.md`)*

^cau-c6a-9-2

> [!remark] Remark: Yu's route
> Yu computes symmetry factors for matrix elements of the $S$-operator: the first-order self-energy $\langle\mathbf k|iT_2^{(1)}|\mathbf k\rangle$ (eq. (7.124)), where $C_4^2 = 6$ ways of contracting two of the four fields at the vertex and $A_2^2 = 2$ ways of contracting the other two with the initial and final states reduce $\frac{1}{4!}$ to $\frac12$; the first-order vacuum bubble (eq. (7.125), $\frac18$); and the second-order self-energies (eqs. (7.126)–(7.132)), among them the chain ((7.127)–(7.128), $S = 4$) and the snowman ((7.131)–(7.132), $S = 4$). In each case the two ways of contracting with the initial and final states cancel the $\frac{1}{2!}$ of the second order. He states the principle in a box: "the factor obtained by analysing the symmetry of the Feynman diagram always agrees with the factor left over in the $T$-matrix computation" (p. 293), and remarks that tree diagrams contributing to scattering or decay have $S = 1$, while loop diagrams may have nontrivial symmetry factors (p. 294).
>
> *Source: Yu §7.3, pp. 292–296*

^rem-c6a-9-3

> [!remark]- Connections
> - $S$ is the order of a stabilizer, and the product rule is the first isomorphism theorem applied to the map that forgets the legs: local symmetries form the kernel, vertex permutations the image — [[§CA.7 Pairings, Diagrams and Symmetry Factors#^thm-ca-7-9|Theorem §CA.7.9]], [[§41 The First and Second Isomorphism Theorems#^thm-41-1|493 Thm. §41.1]].
> - Identical particles in quantum mechanics are counted by the same permutation groups; a symmetry factor is the field-theory trace of indistinguishability — [[§C12.1★ Permutation Symmetry and the Symmetrization Postulate|QM §C12.1★]].
> - The vacuum bubbles carry the largest symmetry factors and are removed by the denominator of the master formula — [[§C6a.11 The iε Limit and Vacuum Bubbles#^thm-c6a-11-5|Theorem §C6a.11.5]].
> - Charged fields have fewer relabellings, hence smaller symmetry factors: the complex scalar's arrows forbid loop flips and the exchange of opposite lines, and the QED vertex has no leg permutations at all; the counting is the same orbit–stabilizer argument with leg kinds — [[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-4|Theorem §CA.8.4]], [[§C6a.9 Symmetry Factors in Practice#^thm-c6a-9-1|Theorem §C6a.9.1]], [[§C6a.9 Symmetry Factors in Practice#^cau-c6a-9-2|Caution: "In QED the symmetry factor is always S = 1" holds for diagrams with external points]].
