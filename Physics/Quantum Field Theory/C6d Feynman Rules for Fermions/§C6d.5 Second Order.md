---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C6d
section: C6d.5
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C6d.4 First Order]] · ↑ [[· C6d Feynman Rules for Fermions]] · [[§C6d.6 Momentum-Space Feynman Rules]] →

*Sources: PHY 513 Lecture 17 (Larsen, 4 Nov 2026), slides 19–20, 23, and transcript (from about 61 min) · the user's PHY 513 notes, Lecture 17 update, §17.6 (paragraph "The order", Derivation "The relative sign (filled in)", Principle "Fermion–fermion scattering in Yukawa theory", eq. (ffamp), Figure "ffscatt", paragraphs "Reading the result", "The relative sign from antisymmetry", "The overall sign is a convention" (replaced by "The overall sign" in the Lecture 18 update, Part 2 (a)), Caution "Slips in the handwritten notes for this example") · Peskin & Schroeder, An Introduction to Quantum Field Theory, §4.7, pp. 116–120, eqs. (4.113)–(4.116), (4.118)–(4.119) · Yu Zhao-Huan, 量子场论讲义, §7.1.2, eqs. (7.59)–(7.103), Fig. 7.3–7.11, pp. 273–287 (the 14 terms and the processes (1)–(8); $\psi\psi \to \psi\psi$: (7.78)–(7.82), Fig. 7.4–7.5) (page images checked); §7.2, eqs. (7.105)–(7.107), p. 289.*

At second order two vertices appear. The Dyson term has fourteen Wick terms ([[§C6d.5 Second Order#^thm-c6d-5-1|Theorem §C6d.5.1]]), and the $\frac{1}{2!}$ is cancelled by the exchange of the two vertices ([[§C6d.5 Second Order#^thm-c6d-5-2|Theorem §C6d.5.2]]). The scattering of two particles comes only from trees: $f\bar f \to f\bar f$ ([[§C6d.5 Second Order#^ex-c6d-5-1|Example §C6d.5.1]]), $ff \to ff$ ([[§C6d.5 Second Order#^ex-c6d-5-2|Example §C6d.5.2]]) and $f\bar f \to \phi\phi$ ([[§C6d.5 Second Order#^ex-c6d-5-3|Example §C6d.5.3]]). Their relative signs follow one rule ([[§C6d.5 Second Order#^thm-c6d-5-4|Theorem §C6d.5.4]]) and are observable through the interference term ([[§C6d.5 Second Order#^thm-c6d-5-5|Theorem §C6d.5.5]]). The loops correct single particles, and the bubbles are phases ([[§C6d.5 Second Order#^ex-c6d-5-4|Example §C6d.5.4]]–[[§C6d.5 Second Order#^ex-c6d-5-8|Example §C6d.5.8]]), as for scalars ([[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors|§C6c.5]]). Yu works through the same fourteen terms in §7.1.2.

The lecture's worked example: two fermions scatter into two fermions at order $g^2$, $f(p) + f(k) \to f(p') + f(k')$. With practice the diagrams of a process are drawn directly; the lecture first did it the long way, by contractions ([[§C6d.5 Second Order#^ex-c6d-5-2|Example §C6d.5.2]]). Two diagrams appear, the $t$-channel and the $u$-channel exchange of the scalar, with a relative minus sign. That sign is physical and follows from Fermi statistics alone ([[§C6d.5 Second Order#^thm-c6d-5-3|Theorem §C6d.5.3]]); the overall sign depends on how the states are written and, with each bra the Hermitian conjugate of its ket, is physical relative to the unscattered term ([[§C6d.5 Second Order#^rem-c6d-5-1|Remark: The overall sign]], [[§C8.5 The Coulomb Potential, and Why Like Charges Repel#^thm-c8-5-6|Theorem §C8.5.6]]). Asserting only the relative minus sign, without the contractions, is not enough once the nonrelativistic limit is compared with the force between charges ([[§C6d.7 The Yukawa Potential|§C6d.7]]). PS work the same process in §4.7 (eq. (4.119)); Yu in §7.1.2 (eq. (7.82)).

**Setup.** [[§C6d.1 Yukawa Theory#^mod-c6d-1-1|Model §C6d.1.1]] at order $g^2$, the lowest order of the $2 \to 2$ processes of this section ($f\bar f \to f\bar f$, $ff \to ff$, $f\bar f \to \phi\phi$): free relativistic states over $|0\rangle$ for the in and out states, exact at this order ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^pr-c6b-1-3|Principle §C6b.1.3]]). States ordered as in [[§C6d.2 Contractions with External Fermions#^def-c6d-2-2|Def. §C6d.2.2]]: $|\mathbf p, \mathbf k\rangle = \sqrt{2E_{\mathbf p}2E_{\mathbf k}}\,\hat a^\dagger_{\mathbf p}\hat a^\dagger_{\mathbf k}|0\rangle$, $\langle\mathbf p', \mathbf k'| = \sqrt{2E_{\mathbf p'}2E_{\mathbf k'}}\,\langle0|\hat a_{\mathbf k'}\hat a_{\mathbf p'}$. Spin labels are suppressed: $u(p) \equiv u^{s_p}(p)$ and so on, each spinor carrying the spin of its particle. The one-particle matrix elements of the loop examples are forward: corrections of the external states, not processes ([[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^thm-c6c-5-3|Theorem §C6c.5.3]]).

## The second-order terms

> [!theorem] Theorem §C6d.5.1: The Fourteen Second-Order Wick Terms of Yukawa Theory
> In [[§C6d.1 Yukawa Theory#^mod-c6d-1-1|Model §C6d.1.1]] the second-order term of the Dyson series ([[§C6d.1 Yukawa Theory#^thm-c6d-1-3|Theorem §C6d.1.3]]) is
>
> $$
> i\hat T^{(2)} = \frac{(-ig)^2}{2!}\int d^4x\,d^4y\;T\bigl\{\hat{\bar\psi}\hat\psi\hat\phi(x)\;\hat{\bar\psi}\hat\psi\hat\phi(y)\bigr\} = \sum_{j=1}^{14}i\hat T^{(2)}_j ,
> $$
>
> and [[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-2|Theorem §C6d.3.2]] gives exactly $14$ nonzero Wick terms. Write $D \equiv D_F(x - y)$, $S_{xy} \equiv S_F(x - y)$; the contracted pairs, their value, the fields left for the particles, and what each term can do:
>
> | Yu | contracted | value | left for particles | diagram | processes | fate |
> |---|---|---|---|---|---|---|
> | ★ $1$ | none | $1$ | all six | two separate vertices | two first-order pieces | not one process |
> | $2$ | $\hat\phi_x\hat\phi_y$ | $D$ | $\hat{\bar\psi}_x\hat\psi_x\hat{\bar\psi}_y\hat\psi_y$ | tree, scalar exchanged | $f\bar f \to f\bar f$, $ff \to ff$, $\bar f\bar f \to \bar f\bar f$ | **scattering** |
> | ★ $3$, $4$ | $\hat\psi_x\hat{\bar\psi}_y$ / $\hat\psi_y\hat{\bar\psi}_x$ | $S_{xy}$ / $S_{yx}$ | $\hat{\bar\psi}_x\hat\phi_x\hat\phi_y\hat\psi_y$ / $x \leftrightarrow y$ | tree, fermion exchanged | $f\bar f \to \phi\phi$, $\phi\phi \to f\bar f$, $f\phi \to f\phi$, $\bar f\phi \to \bar f\phi$ | **scattering** |
> | ★ $5$, $6$ | $\hat{\bar\psi}_x\hat\psi_x$ / $\hat{\bar\psi}_y\hat\psi_y$ | $-\operatorname{tr}S_F(0)$ | $\hat\phi_x$ and $\hat{\bar\psi}_y\hat\psi_y\hat\phi_y$ / $x \leftrightarrow y$ | tadpole beside a three-leg vertex | — | not connected |
> | ★ $7$, $8$ | $\hat\phi_x\hat\phi_y$, $\hat\psi_x\hat{\bar\psi}_y$ / $\hat\phi_x\hat\phi_y$, $\hat\psi_y\hat{\bar\psi}_x$ | $D\,S_{xy}$ / $D\,S_{yx}$ | $\hat{\bar\psi}_x\hat\psi_y$ / $x \leftrightarrow y$ | fermion self-energy, one loop | $f \to f$, $\bar f \to \bar f$ | forward: external correction |
> | ★ $9$, $10$ | $\hat\phi_x\hat\phi_y$, $\hat{\bar\psi}_x\hat\psi_x$ / $\hat\phi_x\hat\phi_y$, $\hat{\bar\psi}_y\hat\psi_y$ | $-D\operatorname{tr}S_F(0)$ | $\hat{\bar\psi}_y\hat\psi_y$ / $x \leftrightarrow y$ | tadpole on a fermion line | $f \to f$, $\bar f \to \bar f$ | forward: external correction |
> | ★ $11$ | $\hat\psi_x\hat{\bar\psi}_y$, $\hat\psi_y\hat{\bar\psi}_x$ | $-\operatorname{tr}[S_{xy}S_{yx}]$ | $\hat\phi_x\hat\phi_y$ | scalar self-energy, fermion loop | $\phi \to \phi$ | forward: external correction |
> | ★ $12$ | $\hat{\bar\psi}_x\hat\psi_x$, $\hat{\bar\psi}_y\hat\psi_y$ | $(\operatorname{tr}S_F(0))^2$ | $\hat\phi_x\hat\phi_y$ | two tadpoles | — | not connected |
> | ★ $13$ | $\hat\phi_x\hat\phi_y$, $\hat\psi_x\hat{\bar\psi}_y$, $\hat\psi_y\hat{\bar\psi}_x$ | $-D\operatorname{tr}[S_{xy}S_{yx}]$ | none | vacuum bubble, $S = 2$ | — | a phase |
> | ★ $14$ | $\hat\phi_x\hat\phi_y$, $\hat{\bar\psi}_x\hat\psi_x$, $\hat{\bar\psi}_y\hat\psi_y$ | $D\,(\operatorname{tr}S_F(0))^2$ | none | two tadpoles joined, $S = 2$ | — | a phase |
>
> Row $2$ holds Lecture 17's example $ff \to ff$; the rows marked ★ are Yu's matrix elements beyond the course. The "processes" column lists the $2 \to 2$ and $1 \to 1$ processes; the others a term allows ($1 \leftrightarrow 3$, $0 \leftrightarrow 4$, $0 \leftrightarrow 2$) are forbidden by [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-2|Theorem §C6c.4.2]], as are the first-order pieces of terms $1$, $5$, $6$, $12$ except $\phi \leftrightarrow f\bar f$ ([[§C6d.4 First Order#^thm-c6d-4-5|Theorem §C6d.4.5]]). At order $g^2$ the scattering of two particles comes only from terms $2$–$4$, all trees; the loops of terms $7$–$11$ correct a single external particle, and $13$–$14$ are vacuum bubbles ([[§C6d.5 Second Order#^ex-c6d-5-8|★ Example §C6d.5.8]]).
>
> *Equivalently,* the scalar case is [[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^thm-c6c-5-1|Theorem §C6c.5.1]] ($764$ Wick terms of $\phi^4$, sorted by the same structure); here only $\hat\phi\hat\phi$ and $\hat\psi\hat{\bar\psi}$ pairs contract, which leaves $14$.
>
> *Model:* [[§C6d.1 Yukawa Theory#^mod-c6d-1-1|Model §C6d.1.1]]; *applies:* second order of the Dyson series between free relativistic states over $|0\rangle$ ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^pr-c6b-1-3|Principle §C6b.1.3]]); exact as a statement about the Wick terms, the fates with the kinematic filter (masses $m$, $m_\phi$ on shell).
>
> *Source: Yu §7.1.2, eqs. (7.59)–(7.73), pp. 273–274 ("根据 Wick 定理，上式共有 14 个非平庸的项"), and the processes (1)–(8), pp. 274–286 · row 2, $ff \to ff$: PHY 513 Lecture 17, slides 19–20; PS §4.7, pp. 116–120 · table written here*

^thm-c6d-5-1

> [!derivation]- Derivation
> **Step 1** (the nonzero pairs). Label the six fields $\hat{\bar\psi}_x, \hat\psi_x, \hat\phi_x, \hat{\bar\psi}_y, \hat\psi_y, \hat\phi_y$. By [[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-1|Theorem §C6d.3.1]] the only nonzero contractions are $\hat\phi_x\hat\phi_y$ and the four $\hat\psi\hat{\bar\psi}$ pairs $\hat\psi_x\hat{\bar\psi}_x$, $\hat\psi_x\hat{\bar\psi}_y$, $\hat\psi_y\hat{\bar\psi}_x$, $\hat\psi_y\hat{\bar\psi}_y$ ($\hat\psi\hat\psi$, $\hat{\bar\psi}\hat{\bar\psi}$ and fermion–scalar pairs vanish).
>
> **Step 2** (the sets of disjoint pairs). No pair: $1$ (term 1). One pair: $1 + 4 = 5$ (terms 2–6). Two pairs: $\hat\phi_x\hat\phi_y$ with one of the four fermion pairs, $4$ (terms 7–10), or two disjoint fermion pairs, $\{\hat\psi_x\hat{\bar\psi}_y, \hat\psi_y\hat{\bar\psi}_x\}$ or $\{\hat\psi_x\hat{\bar\psi}_x, \hat\psi_y\hat{\bar\psi}_y\}$, $2$ (terms 11, 12). Three pairs: $\hat\phi_x\hat\phi_y$ with one of these two, $2$ (terms 13, 14). Total $1 + 5 + 6 + 2 = 14$ (Yu (7.60)–(7.73)).
>
> **Step 3** (values and signs). In the written order $\hat{\bar\psi}_x\hat\psi_x\hat\phi_x\hat{\bar\psi}_y\hat\psi_y\hat\phi_y$ the fermion positions are $\hat{\bar\psi}_x(1)\,\hat\psi_x(2)\,\hat{\bar\psi}_y(3)\,\hat\psi_y(4)$. $\hat\psi_x\hat{\bar\psi}_y = (2, 3)$: adjacent, $S_{xy}$. $\hat\psi_y\hat{\bar\psi}_x$: written $\hat{\bar\psi}_x$ first, $-S_F(y - x)$, and bringing it to the front passes $\hat\psi_x$, $\hat{\bar\psi}_y$: two exchanges, $\epsilon = +1$; the remainder ${:}\hat\psi_x\hat{\bar\psi}_y{:} = -{:}\hat{\bar\psi}_y\hat\psi_x{:}$, so term 4 is $S_{yx}\,{:}\hat{\bar\psi}_y\hat\phi_y\hat\phi_x\hat\psi_x{:}$, term 3 with $x \leftrightarrow y$. A pair at one point, $(1, 2)$ or $(3, 4)$, is $-\operatorname{tr}S_F(0)$ ([[§C6d.4 First Order#^thm-c6d-4-1|Theorem §C6d.4.1]]). Term 11: $(2, 3)$ and $(1, 4)$, nested, $S_{xy}\cdot(-S_{yx})$ with the indices joined into $-\operatorname{tr}[S_{xy}S_{yx}]$ ([[§C6d.4 First Order#^thm-c6d-4-6|Theorem §C6d.4.6]], $n = 2$). Term 12: $(1, 2)$, $(3, 4)$: $(-\operatorname{tr}S_F(0))^2$. The scalar pair is $D$ and carries no sign.
>
> **Step 4** (what the remainder can meet). By [[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-5|Theorem §C6d.3.5]], 1, each field left in the normal-ordered product meets one particle; by [[§C6d.2 Contractions with External Fermions#^thm-c6d-2-1|Theorem §C6d.2.1]] a $\hat\psi$ takes an incoming $f$ or an outgoing $\bar f$, a $\hat{\bar\psi}$ an outgoing $f$ or an incoming $\bar f$, a $\hat\phi$ a scalar in or out. Term 2: two of each fermion kind: $f\bar f \to f\bar f$, $ff \to ff$, $\bar f\bar f \to \bar f\bar f$ and the forbidden $1 \leftrightarrow 3$, $0 \leftrightarrow 4$. Terms 3–4: one $\hat{\bar\psi}$, one $\hat\psi$, two $\hat\phi$. Terms 7–10: one $\hat{\bar\psi}$, one $\hat\psi$ (at different points in 7, 8; at one point in 9, 10): $f \to f$, $\bar f \to \bar f$, and $0 \leftrightarrow f\bar f$, forbidden. Term 11: two scalars: $\phi \to \phi$ and $0 \leftrightarrow \phi\phi$, forbidden. Terms 13–14: nothing.
>
> **Step 5** (the fates). Terms 1, 5, 6, 12 consist of two pieces, each with its own momentum delta ([[§C6c.3 Wick's Theorem between Particle States#^thm-c6c-3-3|Theorem §C6c.3.3]]): not one process ([[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-6|Theorem §C6c.4.6]], 2). The $1 \to 1$ elements carry $\delta^4(p - p')$: forward, corrections of the external particle ([[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-6|Theorem §C6c.4.6]], 2; [[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^thm-c6c-5-3|Theorem §C6c.5.3]], 1). Terms 13–14 have no particles: vacuum bubbles, a phase ([[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-6|Theorem §C6c.4.6]], 1); their $S = 2$ is [[§C6d.4 First Order#^thm-c6d-4-7|Theorem §C6d.4.7]].
>
> **What the derivation shows.**
> - Second-order scattering of two particles is tree level: one exchanged scalar (term 2) or one exchanged fermion (terms 3–4) → [[§C6d.5 Second Order#^ex-c6d-5-1|Example §C6d.5.1]], [[§C6d.5 Second Order#^ex-c6d-5-2|Example §C6d.5.2]], [[§C6d.5 Second Order#^ex-c6d-5-3|Example §C6d.5.3]].
> - The terms come in $x \leftrightarrow y$ pairs, or are mapped to themselves → [[§C6d.5 Second Order#^thm-c6d-5-2|Theorem §C6d.5.2]].

^der-c6d-5-1

*Uses:* [[§C6d.1 Yukawa Theory#^thm-c6d-1-3|Theorem §C6d.1.3]], [[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-2|Theorem §C6d.3.2]], [[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-1|Theorem §C6d.3.1]], [[§C6d.4 First Order#^thm-c6d-4-1|Theorem §C6d.4.1]], [[§C6d.4 First Order#^thm-c6d-4-6|Theorem §C6d.4.6]], [[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-5|Theorem §C6d.3.5]], [[§C6d.2 Contractions with External Fermions#^thm-c6d-2-1|Theorem §C6d.2.1]], [[§C6c.3 Wick's Theorem between Particle States#^thm-c6c-3-3|Theorem §C6c.3.3]], [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-6|Theorem §C6c.4.6]], [[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^thm-c6c-5-3|Theorem §C6c.5.3]], [[§C6d.4 First Order#^thm-c6d-4-7|Theorem §C6d.4.7]]

> [!theorem] Theorem §C6d.5.2: The 1/2! Cancels the Exchange x ↔ y; Vertices Move as Even Packages
> In the second-order term of [[§C6d.5 Second Order#^thm-c6d-5-1|Theorem §C6d.5.1]]:
> 1. relabelling $x \leftrightarrow y$ exchanges the two packages $\hat{\bar\psi}\hat\psi\hat\phi(x)$, $\hat{\bar\psi}\hat\psi\hat\phi(y)$ (two fermion fields each: no sign, [[§C6d.1 Yukawa Theory#^thm-c6d-1-2|Theorem §C6d.1.2]], 1) and renames the integration variables (the integral is unchanged); it maps the Wick terms $3 \leftrightarrow 4$, $5 \leftrightarrow 6$, $7 \leftrightarrow 8$, $9 \leftrightarrow 10$, and each of $1, 2, 11, 12, 13, 14$ to itself;
> 2. so the paired terms are equal, $i\hat T^{(2)}_3 + i\hat T^{(2)}_4 = 2\,i\hat T^{(2)}_3$ etc., and in the self-paired terms with particles the attachments of the particles come in pairs exchanged by $x \leftrightarrow y$ (the assignments A ↔ B and C ↔ D of [[§C6d.5 Second Order#^ex-c6d-5-2|Example §C6d.5.2]]): in every term with external particles the $\frac{1}{2!}$ is cancelled, and each diagram enters once with $(-ig)^2$;
> 3. in the vacuum bubbles, terms $13$ and $14$, nothing distinguishes $x$ from $y$: the exchange maps their single contraction pattern to itself, and the $\frac{1}{2!}$ stays, $S = 2$.
>
> This is the case $n = 2$ of [[§C6d.4 First Order#^thm-c6d-4-7|Theorem §C6d.4.7]]: the $\frac{1}{n!}$ of $i\hat T^{(n)}$ is cancelled by the $n!$ relabellings of the vertices, except for bubbles.
>
> *Equivalently,* the scalar case is [[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^thm-c6c-5-2|Theorem §C6c.5.2]]; with fermions the only new point is that relabelling moves even packages and so costs no sign.
>
> *Model:* [[§C6d.1 Yukawa Theory#^mod-c6d-1-1|Model §C6d.1.1]]; *applies:* second order of the Dyson series between free relativistic states, every term; part 3 for the bubbles.
>
> *Source: Yu §7.1.2, p. 275 (boxed: "(7.4) 式里面 $iT^{(n)}$ 中的 $1/n!$ 因子恰好与时空坐标的交换对称性引起的 $n!$ 因子抵消"; footnote 1: "不过，此规律不适用于下文中具有非平庸对称性因子的气泡图"), eqs. (7.83)–(7.84), (7.90)–(7.91), (7.93)–(7.94), (7.97)–(7.98) (the four pairs), p. 286 ("$iT^{(2)}_{13}$ 和 $iT^{(2)}_{14}$ 中的 $1/2!$ 因子未被抵消") · PS §4.7, p. 117 ("there is a second, identical term that comes from interchanging $x$ and $y$") · PHY 513 Lecture 17, slide 18 · proof written here*

^thm-c6d-5-2

> [!derivation]- Derivation
> **Step 1** (the relabelling). In $\int d^4x\,d^4y\,T\{B(x)B(y)\}$, $B = \hat{\bar\psi}_a\hat\psi_a\hat\phi$, rename $x \leftrightarrow y$: the integral becomes $\int d^4y\,d^4x\,T\{B(y)B(x)\}$, the same number, and $T\{B(y)B(x)\} = T\{B(x)B(y)\}$ because $B$ holds two fermion fields ([[§C6d.1 Yukawa Theory#^thm-c6d-1-2|Theorem §C6d.1.2]], 2). So each Wick term goes to the Wick term whose contractions are the images of its own under $x \leftrightarrow y$.
>
> **Step 2** (the images). From the table of [[§C6d.5 Second Order#^thm-c6d-5-1|Theorem §C6d.5.1]]: $\hat\psi_x\hat{\bar\psi}_y \leftrightarrow \hat\psi_y\hat{\bar\psi}_x$ (terms 3, 4; and 7, 8 together with $\hat\phi_x\hat\phi_y \leftrightarrow \hat\phi_y\hat\phi_x$); $\hat{\bar\psi}_x\hat\psi_x \leftrightarrow \hat{\bar\psi}_y\hat\psi_y$ (5, 6; 9, 10). Terms 1, 2 (no fermion pair), 11 ($\{\hat\psi_x\hat{\bar\psi}_y, \hat\psi_y\hat{\bar\psi}_x\}$), 12 ($\{\hat{\bar\psi}_x\hat\psi_x, \hat{\bar\psi}_y\hat\psi_y\}$), 13, 14 are mapped to themselves. Explicitly, term 8 $= D\cdot(-S_F(y - x))\,{:}\hat\psi_x\hat\phi_x\hat{\bar\psi}_y\hat\phi_y{:}$ (Step 3 of [[§C6d.5 Second Order#^der-c6d-5-1|Derivation §C6d.5.1]]: the pair $\hat{\bar\psi}_x\hat\psi_y$ in written order; reordering the rest, ${:}\hat\psi_x\hat{\bar\psi}_y{:} = -{:}\hat{\bar\psi}_y\hat\psi_x{:}$) $= D\,S_F(y - x)\,{:}\hat{\bar\psi}_y\hat\psi_x{:}$, term 7 $= D\,S_F(x - y)\,{:}\hat{\bar\psi}_x\hat\psi_y{:}$ with $x \leftrightarrow y$: equal after integration (Yu (7.93)).
>
> **Step 3** (attachments in self-paired terms). In term 2 between $\langle f|$ and $|i\rangle$ the four fermion fields take the four particles; renaming $x \leftrightarrow y$ maps each assignment to the assignment with the roles of the two vertices exchanged, a different assignment with the same value (Step 4 of [[§C6d.5 Second Order#^ex-c6d-5-2|Example §C6d.5.2]]). In term 11, $\langle\mathbf k'|{:}\hat\phi_x\hat\phi_y{:}|\mathbf k\rangle = e^{ik'\cdot x - ik\cdot y} + e^{ik'\cdot y - ik\cdot x}$, the two terms exchanged by $x \leftrightarrow y$. So every diagram with particles arises twice, and $\frac{1}{2!}\cdot2 = 1$.
>
> **Step 4** (bubbles). Term 13 has the single pattern $\{\hat\phi_x\hat\phi_y, \hat\psi_x\hat{\bar\psi}_y, \hat\psi_y\hat{\bar\psi}_x\}$; under $x \leftrightarrow y$ it becomes $\{\hat\phi_y\hat\phi_x, \hat\psi_y\hat{\bar\psi}_x, \hat\psi_x\hat{\bar\psi}_y\}$, the same set. Term 14 likewise. No second copy exists, and the $\frac{1}{2!}$ remains: the symmetry factor $S = 2$ of Step 4 of [[§C6d.4 First Order#^der-c6d-4-7|Derivation §C6d.4.7]].
>
> **What the derivation shows.**
> - The fermion signs never obstruct the cancellation of $\frac{1}{n!}$: packages, not single fields, are relabelled.

^der-c6d-5-2

*Uses:* [[§C6d.1 Yukawa Theory#^thm-c6d-1-2|Theorem §C6d.1.2]], [[§C6d.5 Second Order#^thm-c6d-5-1|Theorem §C6d.5.1]], [[§C6d.5 Second Order#^der-c6d-5-1|Derivation §C6d.5.1]], [[§C6d.5 Second Order#^ex-c6d-5-2|Example §C6d.5.2]], [[§C6d.4 First Order#^der-c6d-4-7|Derivation §C6d.4.7]]

## Fermion–antifermion scattering

> [!example]- ★ Example §C6d.5.1: f f̄ → f f̄ at Order g²: s- and t-Channel with a Relative Minus Sign
> ![[ph-qft-c6d-5-2.svg]]
>
> In [[§C6d.1 Yukawa Theory#^mod-c6d-1-1|Model §C6d.1.1]], for $f(p_1, s_1) + \bar f(p_2, s_2) \to f(q_1, s_1') + \bar f(q_2, s_2')$, initial state $\sqrt{4E_{\mathbf p_1}E_{\mathbf p_2}}\,\hat a^\dagger_{\mathbf p_1}\hat b^\dagger_{\mathbf p_2}|0\rangle$ and final bra its counterpart $\sqrt{4E_{\mathbf q_1}E_{\mathbf q_2}}\,\langle0|\hat b_{\mathbf q_2}\hat a_{\mathbf q_1}$ ([[§C6d.2 Contractions with External Fermions#^def-c6d-2-2|Def. §C6d.2.2]]), at order $g^2$
>
> $$
> i\mathcal M = (-ig)^2\Bigl[\bar u(q_1)v(q_2)\,\frac{i}{(p_1 + p_2)^2 - m_\phi^2 + i\varepsilon}\,\bar v(p_2)u(p_1) \;-\; \bar v(p_2)v(q_2)\,\frac{i}{(p_1 - q_1)^2 - m_\phi^2 + i\varepsilon}\,\bar u(q_1)u(p_1)\Bigr] ,
> $$
>
> the $s$-channel (annihilation into a scalar and pair creation) and the $t$-channel (scalar exchange between the fermion and the antifermion), with a **relative minus sign**, although $f$ and $\bar f$ are not identical: the two diagrams differ by exchanging the partners of the two $\hat\psi$ fields ([[§C6d.5 Second Order#^thm-c6d-5-4|Theorem §C6d.5.4]]). Spinors carry their particles' spins.
>
> **Step 1** (the term). Four external fermions and no scalar: term 2 of [[§C6d.5 Second Order#^thm-c6d-5-1|Theorem §C6d.5.1]], $\frac{(-ig)^2}{2!}\int d^4x\,d^4y\,D_F(x - y)\,{:}\hat{\bar\psi}_x\hat\psi_x\hat{\bar\psi}_y\hat\psi_y{:}$.
>
> **Step 2** (who contracts with whom, [[§C6d.2 Contractions with External Fermions#^thm-c6d-2-1|Theorem §C6d.2.1]]). The $\hat\psi$'s take $p_1$ (incoming $f$, $u$) and $q_2$ (outgoing $\bar f$, $v$); the $\hat{\bar\psi}$'s take $q_1$ (outgoing $f$, $\bar u$) and $p_2$ (incoming $\bar f$, $\bar v$). Four assignments:
>
> | | $\hat\psi_x$ | $\hat{\bar\psi}_x$ | $\hat\psi_y$ | $\hat{\bar\psi}_y$ | pattern |
> |---|---|---|---|---|---|
> | A | $p_1$ | $q_1$ | $q_2$ | $p_2$ | $t$: $f$ line at $x$, $\bar f$ line at $y$ |
> | B | $q_2$ | $p_2$ | $p_1$ | $q_1$ | $t$: A with $x \leftrightarrow y$ |
> | C | $q_2$ | $q_1$ | $p_1$ | $p_2$ | $s$: pair created at $x$, annihilated at $y$ |
> | D | $p_1$ | $p_2$ | $q_2$ | $q_1$ | $s$: C with $x \leftrightarrow y$ |
>
> **Step 3** ($\frac{1}{2!}$). B and D are A and C with $x \leftrightarrow y$: $\frac{1}{2!}(A + B + C + D) = A + C$ ([[§C6d.5 Second Order#^thm-c6d-5-2|Theorem §C6d.5.2]]).
>
> **Step 4** (signs, [[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-4|Theorem §C6d.3.4]]). Fermion string $\hat b_{\mathbf q_2}(1)\,\hat a_{\mathbf q_1}(2)\,\hat{\bar\psi}_x(3)\,\hat\psi_x(4)\,\hat{\bar\psi}_y(5)\,\hat\psi_y(6)\,\hat a^\dagger_{\mathbf p_1}(7)\,\hat b^\dagger_{\mathbf p_2}(8)$. A: pairs $(2, 3)$, $(4, 7)$, $(1, 6)$, $(5, 8)$; crossings $(4, 7)$–$(1, 6)$, $(4, 7)$–$(5, 8)$, $(1, 6)$–$(5, 8)$: **3, sign $-$**. C: pairs $(2, 3)$, $(1, 4)$, $(6, 7)$, $(5, 8)$; $(2, 3)$ inside $(1, 4)$, $(6, 7)$ inside $(5, 8)$, the two blocks apart: **0, sign $+$**.
>
> **Step 5** (values of C). In written order: $\bar u(q_1)e^{iq_1\cdot x}$, $v(q_2)e^{iq_2\cdot x}$, $u(p_1)e^{-ip_1\cdot y}$, $\bar v(p_2)e^{-ip_2\cdot y}$; the vertex at $x$ joins $\hat{\bar\psi}_x\hat\psi_x$ into $\bar u(q_1)v(q_2)$, the vertex at $y$ into $\bar v(p_2)u(p_1)$ ([[§C6d.2 Contractions with External Fermions#^thm-c6d-2-4|Theorem §C6d.2.4]]). With $D_F(x - y) = \int\frac{d^4k}{(2\pi)^4}\frac{ie^{-ik\cdot(x - y)}}{k^2 - m_\phi^2 + i\varepsilon}$ ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-9|Theorem §C2b.6.9]]), $\int d^4x\,e^{i(q_1 + q_2 - k)\cdot x} = (2\pi)^4\delta^4(q_1 + q_2 - k)$ and $\int d^4y\,e^{i(k - p_1 - p_2)\cdot y} = (2\pi)^4\delta^4(k - p_1 - p_2)$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]]); the $k$ integral sets $k = p_1 + p_2$:
>
> $$
> C = (-ig)^2\,\bar u(q_1)v(q_2)\,\frac{i}{(p_1 + p_2)^2 - m_\phi^2 + i\varepsilon}\,\bar v(p_2)u(p_1)\,(2\pi)^4\delta^4(p_1 + p_2 - q_1 - q_2) .
> $$
>
> **Step 6** (values of A). $\bar u(q_1)e^{iq_1\cdot x}$, $u(p_1)e^{-ip_1\cdot x}$, $v(q_2)e^{iq_2\cdot y}$, $\bar v(p_2)e^{-ip_2\cdot y}$; chains $\bar u(q_1)u(p_1)$ at $x$ and $\bar v(p_2)v(q_2)$ at $y$; the $x$ integral gives $k = q_1 - p_1$, and $D_F$ is even in $k$:
>
> $$
> A = -(-ig)^2\,\bar v(p_2)v(q_2)\,\frac{i}{(p_1 - q_1)^2 - m_\phi^2 + i\varepsilon}\,\bar u(q_1)u(p_1)\,(2\pi)^4\delta^4(p_1 + p_2 - q_1 - q_2) .
> $$
>
> **Step 7** (read off). $A + C = i\mathcal M\,(2\pi)^4\delta^4(\cdots)$ ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-3|Def. §C6b.1.3]]): the statement. By the rules ([[§C6d.6 Momentum-Space Feynman Rules#^thm-c6d-6-2|Theorem §C6d.6.2]]): two vertices, one scalar propagator with $s = (p_1 + p_2)^2$ or $t = (p_1 - q_1)^2$, two chains each, and the relative sign from Step 4. Yu (7.105) has the same bracket; his (7.77) has an overall $-$ from his bra $\langle0|\hat a_{\mathbf q_1}\hat b_{\mathbf q_2}$ ([[§C6d.4 First Order#^cau-c6d-4-1|§C6d.4, Caution: Yu's (7.23)–(7.24) and his order of the bra]]).
>
> *Source: Yu §7.1.2, eqs. (7.74)–(7.77), Fig. 7.3, pp. 274–277 ("这个过程的总不变振幅 $i\mathcal M = i\mathcal M_1 - i\mathcal M_2$ 是 2 个子振幅的叠加，两者之间的相对符号为负"); §7.2, eqs. (7.105)–(7.106) · beyond the course (QED's version, Bhabha scattering, is a process of C8, planned) · recomputed here in the vault's conventions*

^ex-c6d-5-1

## Fermion–fermion scattering

> [!example] Example §C6d.5.2: f f → f f at Order g², by Contractions
> ![[ph-qft-c6d-5-1.svg]]
>
> For $f(p) + f(k) \to f(p') + f(k')$ in Yukawa theory, at order $g^2$,
>
> $$
> i\mathcal M = (-ig)^2\Bigl[\bar u(p')u(p)\,\frac{i}{(p - p')^2 - m_\phi^2 + i\varepsilon}\,\bar u(k')u(k) \;-\; \bar u(k')u(p)\,\frac{i}{(p - k')^2 - m_\phi^2 + i\varepsilon}\,\bar u(p')u(k)\Bigr] ,
> $$
>
> the $t$-channel ($t = (p - p')^2$) and the $u$-channel ($u = (p - k')^2$) exchange of the scalar, with a relative minus sign.
>
> **Step 1** (the order). Four external fermions need four fermion fields: two vertices,
>
> $$
> \langle\mathbf p', \mathbf k'|\hat S|\mathbf p, \mathbf k\rangle^{(2)} = \frac{(-ig)^2}{2!}\int d^4x\,d^4y\;\langle\mathbf p', \mathbf k'|\,T\bigl\{\hat{\bar\psi}\hat\psi\hat\phi(x)\;\hat{\bar\psi}\hat\psi\hat\phi(y)\bigr\}\,|\mathbf p, \mathbf k\rangle
> $$
>
> ([[§C6d.6 Momentum-Space Feynman Rules#^thm-c6d-6-2|Theorem §C6d.6.2]], Step 1; slide 19).
>
> **Step 2** (who contracts with whom). The two scalar fields have no external partner: there is no external scalar, so they contract with each other, $\overbracket{\hat\phi(x)\hat\phi(y)} = D_F(x - y)$. The two $\hat\psi$'s must absorb the incoming particles, through their $\hat a$ parts (the $b$ parts play no role), each giving a $u$; the two $\hat{\bar\psi}$'s must emit the outgoing ones, through their $\hat a^\dagger$ parts, each giving a $\bar u$ ([[§C6d.2 Contractions with External Fermions#^thm-c6d-2-1|Theorem §C6d.2.1]]; slide 20: "$\psi$'s contract with incoming particles, $\bar\psi$'s with outgoing"). A $\hat\psi$–$\hat{\bar\psi}$ contraction would leave only two fermion fields for four particles.
>
> **Step 3** (the four assignments). $\hat\psi(x)$ absorbs $p$ or $k$, $\hat{\bar\psi}(x)$ emits $p'$ or $k'$:
>
> | | $\hat\psi(x)$ | $\hat{\bar\psi}(x)$ | $\hat\psi(y)$ | $\hat{\bar\psi}(y)$ | pattern |
> |---|---|---|---|---|---|
> | A | $p$ | $p'$ | $k$ | $k'$ | $t$: $p \to p'$ at $x$ |
> | B | $k$ | $k'$ | $p$ | $p'$ | $t$: A with $x \leftrightarrow y$ |
> | C | $p$ | $k'$ | $k$ | $p'$ | $u$: $p \to k'$ at $x$ |
> | D | $k$ | $p'$ | $p$ | $k'$ | $u$: C with $x \leftrightarrow y$ |
>
> **Step 4** ($x \leftrightarrow y$ cancels $\frac{1}{2!}$). B is A with the integration variables renamed and the packages exchanged, which costs no sign ([[§C6d.1 Yukawa Theory#^thm-c6d-1-2|Theorem §C6d.1.2]]); likewise D and C. So $\frac{1}{2!}(A + B + C + D) = A + C$ ([[§C6d.4 First Order#^thm-c6d-4-7|Theorem §C6d.4.7]]; PS p. 117: "there is a second, identical term that comes from interchanging $x$ and $y$").
>
> **Step 5** (signs). The fermion string is $\langle0|\hat a_{\mathbf k'}\hat a_{\mathbf p'}\,\hat{\bar\psi}_x\hat\psi_x\,\hat{\bar\psi}_y\hat\psi_y\,\hat a^\dagger_{\mathbf p}\hat a^\dagger_{\mathbf k}|0\rangle$, positions $1, \dots, 8$. Pattern A pairs $(2, 3)$, $(4, 7)$, $(1, 5)$, $(6, 8)$: $(4, 7)$ crosses $(1, 5)$ and $(6, 8)$, the others are nested or apart: **2 crossings, sign $+$**. Pattern C pairs $(1, 3)$, $(2, 5)$, $(4, 7)$, $(6, 8)$: $(1, 3)$–$(2, 5)$, $(2, 5)$–$(4, 7)$, $(4, 7)$–$(6, 8)$ cross: **3 crossings, sign $-$** ([[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-4|Theorem §C6d.3.4]]; figure after that theorem). (The user's notes check this with a Jordan–Wigner representation of four fermionic modes: $+1$ and $-1$.)
>
> **Step 6** (values of A). In written order the pairs give $\bar u(p')e^{ip'\cdot x}$, $u(p)e^{-ip\cdot x}$, $\bar u(k')e^{ik'\cdot y}$, $u(k)e^{-ik\cdot y}$ ([[§C6d.2 Contractions with External Fermions#^thm-c6d-2-1|Theorem §C6d.2.1]]), the spinor indices joined at each vertex into $\bar u(p')u(p)$ and $\bar u(k')u(k)$ ([[§C6d.2 Contractions with External Fermions#^thm-c6d-2-4|Theorem §C6d.2.4]]). With $D_F(x - y) = \int\frac{d^4q}{(2\pi)^4}\frac{ie^{-iq\cdot(x - y)}}{q^2 - m_\phi^2 + i\varepsilon}$ ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-9|Theorem §C2b.6.9]]),
>
> $$
> A = (-ig)^2\int\frac{d^4q}{(2\pi)^4}\,\frac{i}{q^2 - m_\phi^2 + i\varepsilon}\;\bar u(p')u(p)\,\bar u(k')u(k)\int d^4x\,e^{i(p' - p - q)\cdot x}\int d^4y\,e^{i(k' - k + q)\cdot y} .
> $$
>
> The vertex integrals are $(2\pi)^4\delta^4(p' - p - q)$ and $(2\pi)^4\delta^4(k' - k + q)$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]]); the first fixes $q = p' - p$ (equivalently $p - p'$, $D_F$ being even), the second becomes $(2\pi)^4\delta^4(p + k - p' - k')$:
>
> $$
> A = (-ig)^2\,\bar u(p')u(p)\,\frac{i}{(p - p')^2 - m_\phi^2 + i\varepsilon}\,\bar u(k')u(k)\;(2\pi)^4\delta^4(p + k - p' - k') .
> $$
>
> **Step 7** (values of C). The same with $p' \leftrightarrow k'$ in the outgoing factors: the chains $\bar u(k')u(p)$ at $x$, $\bar u(p')u(k)$ at $y$, $q = k' - p$, and the sign $-$ of Step 5:
>
> $$
> C = -(-ig)^2\,\bar u(k')u(p)\,\frac{i}{(p - k')^2 - m_\phi^2 + i\varepsilon}\,\bar u(p')u(k)\;(2\pi)^4\delta^4(p + k - p' - k') .
> $$
>
> **Step 8** (read off). $A + C = i\mathcal M\,(2\pi)^4\delta^4(\cdots)$ ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-3|Def. §C6b.1.3]]): the statement. By the rules directly ([[§C6d.6 Momentum-Space Feynman Rules#^thm-c6d-6-2|Theorem §C6d.6.2]]): two vertices $(-ig)^2$, one scalar propagator, each fermion line a chain $\bar uu$, the sign of each diagram from item 4. The chains close because the Yukawa vertex is a scalar: each vertex joins an incoming to an outgoing fermion into a number. Since $(-ig)^2\,i = -ig^2$, the bracket equals PS's form $-ig^2\bigl[\frac{\bar u(p')u(p)\,\bar u(k')u(k)}{(p' - p)^2 - m_\phi^2} - \frac{\bar u(p')u(k)\,\bar u(k')u(p)}{(p' - k)^2 - m_\phi^2}\bigr]$, with $(p' - k)^2 = (p - k')^2$ by $p + k = p' + k'$.
>
> *Equivalently,* the scalar analogue is the $t$- and $u$-channel pair of [[§C6c.6 Feynman Rules for Amplitudes#^thm-c6c-6-4|Theorem §C6c.6.4]], with relative $+$ ([[§C6d.5 Second Order#^thm-c6d-5-4|Theorem §C6d.5.4]], 3); the same term 2 of [[§C6d.5 Second Order#^thm-c6d-5-1|Theorem §C6d.5.1]] gives the $s$ and $t$ channels of $f\bar f \to f\bar f$ ([[§C6d.5 Second Order#^ex-c6d-5-1|Example §C6d.5.1]]).
>
> *Source: PHY 513 Lecture 17, slides 19–20, and transcript ("So there really are two different Orderings here"; "they are like equally good diagrams") · the user's PHY 513 notes, Lecture 17 update, §17.6, paragraph "The order", Derivation "The relative sign (filled in)", Principle "Fermion–fermion scattering in Yukawa theory", eq. (ffamp), Figure "ffscatt" · PS §4.7, pp. 116–120, eqs. (4.113)–(4.116), (4.118)–(4.119) · Yu §7.1.2, eqs. (7.78)–(7.82) · Steps 5–7 written out here · PHY 513, Problem Set 9, Problem 4(a) (the user's solution, massless fermions allowed; the same amplitude, $t$-term $+$ and $u$-term $-$, with $p_A, p_B, p_1, p_2$ for $p, k, p', k'$; the relative sign by exchange counting: [[§C6d.5 Second Order#^der-c6d-5-3b|Theorem §C6d.5.3, second route]])*

^ex-c6d-5-2

> [!theorem] Theorem §C6d.5.3: The Relative Sign from Fermi Statistics
> For identical external fermions the amplitude is antisymmetric under exchange of two final fermions together with their spins,
>
> $$
> \mathcal M\bigl(p, k \to (p', s'), (k', r')\bigr) = -\,\mathcal M\bigl(p, k \to (k', r'), (p', s')\bigr) ,
> $$
>
> and likewise for two initial fermions. In $ff \to ff$ the exchange $(p', s') \leftrightarrow (k', r')$ maps the $t$-diagram of [[§C6d.5 Second Order#^ex-c6d-5-2|Example §C6d.5.2]] onto the $u$-diagram, so the two enter with opposite signs. Which of them carries the $-$ is fixed by the order of the states ([[§C6d.5 Second Order#^rem-c6d-5-1|Remark: The overall sign]]); that they differ is not.
>
> *Generalized* in [[§C6d.5 Second Order#^thm-c6d-5-4|Theorem §C6d.5.4]]: any two contraction patterns that differ by exchanged fermion partners, identical particles or not; exchanged bosons give $+$.
>
> *Model:* [[§C6d.1 Yukawa Theory#^mod-c6d-1-1|Model §C6d.1.1]]; *applies:* any order, any theory of fermions (QED alike): a property of the states, not of the dynamics; at order $g^2$ it fixes the relative sign without any contraction bookkeeping.
>
> *Source: PHY 513 Lecture 17, slide 23 ("Relative signs enforce statistics of identical particles"), and transcript ("aren't these fermions? Therefore, if I change the two final states, it's supposed to be antisymmetric. Therefore … they better have opposite signs") · the user's PHY 513 notes, Lecture 17 update, §17.6, paragraph "The relative sign from antisymmetry" · PS §4.7, p. 120 ("The minus sign difference between these diagrams is a reflection of Fermi statistics") · Yu §7.1.2, p. 279 ("体现了交换末态全同费米子的反对称性") · proof written here*

^thm-c6d-5-3

> [!derivation]- Derivation
> **Step 1** (the states). By [[§C6d.2 Contractions with External Fermions#^def-c6d-2-2|Def. §C6d.2.2]] and $\{\hat a_{\mathbf k'}, \hat a_{\mathbf p'}\} = 0$ ([[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-4|Theorem §C5b.2.4]]),
>
> $$
> \langle(\mathbf p', s'), (\mathbf k', r')| = \sqrt{\cdots}\,\langle0|\hat a^{r'}_{\mathbf k'}\hat a^{s'}_{\mathbf p'} = -\sqrt{\cdots}\,\langle0|\hat a^{s'}_{\mathbf p'}\hat a^{r'}_{\mathbf k'} = -\langle(\mathbf k', r'), (\mathbf p', s')| :
> $$
>
> the state of two identical fermions is antisymmetric (the Pauli principle, [[§C5b.4 Fermions, Fock Space and the Pauli Principle#^thm-c5b-4-2|Theorem §C5b.4.2]]).
>
> **Step 2** (the amplitude). $\langle f|i\hat T|i\rangle$ is linear in $\langle f|$, and the delta $\delta^4(p + k - p' - k')$ is symmetric under $p' \leftrightarrow k'$; by [[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-3|Def. §C6b.1.3]], $\mathcal M$ changes sign. The initial pair: the same with $\hat a^\dagger_{\mathbf p}\hat a^\dagger_{\mathbf k} = -\hat a^\dagger_{\mathbf k}\hat a^\dagger_{\mathbf p}$.
>
> **Step 3** ($t \leftrightarrow u$). Call $\mathcal T(p', k') = \bar u(p')u(p)\frac{i}{(p - p')^2 - m_\phi^2}\bar u(k')u(k)$ the $t$-term. Exchanging $(p', s') \leftrightarrow (k', r')$ in it gives $\bar u(k')u(p)\frac{i}{(p - k')^2 - m_\phi^2}\bar u(p')u(k) = \mathcal T(k', p')$, the $u$-term. At order $g^2$ the amplitude is a combination $\alpha\,\mathcal T(p', k') + \beta\,\mathcal T(k', p')$ of the two diagrams ([[§C6d.5 Second Order#^ex-c6d-5-2|Example §C6d.5.2]], Steps 2–4: no other contraction pattern exists), with $|\alpha| = |\beta| = g^2$ from the rules. Antisymmetry under $p' \leftrightarrow k'$ requires $\beta = -\alpha$. The initial exchange $p \leftrightarrow k$ also maps $t$ onto $u$, since $(k - p')^2 = (p - k')^2$ by momentum conservation.
>
> **What the derivation shows.**
> - The relative sign is Fermi statistics in the amplitude; for bosons the same argument gives $\beta = +\alpha$ (the $t$ and $u$ channels of [[§C6c.6 Feynman Rules for Amplitudes#^thm-c6c-6-4|§C6c.6, Theorem §C6c.6.4]]). → [[§C6d.5 Second Order#^thm-c6d-5-4|Theorem §C6d.5.4]]
> - ⚑ By-product: the interference term $-2\operatorname{Re}(\mathcal M_t^{\ast}\mathcal M_u)$ of $|\mathcal M|^2$ has its sign from here (Yu (7.75)) → [[§C6d.5 Second Order#^thm-c6d-5-5|Theorem §C6d.5.5]]; cross sections (C8, planned).

^der-c6d-5-3

*Uses:* [[§C6d.2 Contractions with External Fermions#^def-c6d-2-2|Def. §C6d.2.2]], [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-4|Theorem §C5b.2.4]], [[§C5b.4 Fermions, Fock Space and the Pauli Principle#^thm-c5b-4-2|Theorem §C5b.4.2]], [[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-3|Def. §C6b.1.3]], [[§C6d.5 Second Order#^ex-c6d-5-2|Example §C6d.5.2]]

> [!derivation]- Derivation (second route: counting operator exchanges)
> The first derivation reads the relative sign off the antisymmetry of the states; this one finds it in the operator string, as in Step 5 of [[§C6d.5 Second Order#^ex-c6d-5-2|Example §C6d.5.2]], by moving operators instead of counting crossings. Labels as in the user's solution: $p_A = p$, $p_B = k$ in, $p_1 = p'$, $p_2 = k'$ out.
>
> **Step 1** (the string). With $|p_Ap_B\rangle = \hat a^\dagger_{p_A}\hat a^\dagger_{p_B}|0\rangle$ and $\langle p_1p_2| = \langle0|\hat a_{p_2}\hat a_{p_1}$, the adjoint of the ket (the course convention, [[§C6d.5 Second Order#^rem-c6d-5-1|Remark: The overall sign]]; normalization factors suppressed), the fermionic operators of the matrix element stand in the order
>
> $$
> \hat a_{p_2}\;\hat a_{p_1}\;\hat{\bar\psi}(z_1)\;\hat\psi(z_1)\;\hat{\bar\psi}(z_2)\;\hat\psi(z_2)\;\hat a^\dagger_{p_A}\;\hat a^\dagger_{p_B} ,
> $$
>
> and $\hat\phi$ commutes with all of them. Each contraction is evaluated once its two operators are adjacent, and every exchange of two fermionic operators gives a factor $-1$.
>
> **Step 2** (the $t$-diagram, $p_A$, $p_1$ at one vertex). The pairs are $(\hat a_{p_1}\hat{\bar\psi}(z_1))$, $(\hat\psi(z_1)\hat a^\dagger_{p_A})$, $(\hat a_{p_2}\hat{\bar\psi}(z_2))$, $(\hat\psi(z_2)\hat a^\dagger_{p_B})$. Move $\hat a^\dagger_{p_A}$ to the left past $\hat\psi(z_2)$ and $\hat{\bar\psi}(z_2)$ (2 exchanges),
>
> $$
> \hat a_{p_2}\;\hat a_{p_1}\;\hat{\bar\psi}(z_1)\;\hat\psi(z_1)\;\hat a^\dagger_{p_A}\;\hat{\bar\psi}(z_2)\;\hat\psi(z_2)\;\hat a^\dagger_{p_B} ,
> $$
>
> then $\hat a_{p_2}$ to the right past $\hat a_{p_1}$, $\hat{\bar\psi}(z_1)$, $\hat\psi(z_1)$, $\hat a^\dagger_{p_A}$ (4 exchanges):
>
> $$
> \bigl(\hat a_{p_1}\hat{\bar\psi}(z_1)\bigr)\bigl(\hat\psi(z_1)\hat a^\dagger_{p_A}\bigr)\bigl(\hat a_{p_2}\hat{\bar\psi}(z_2)\bigr)\bigl(\hat\psi(z_2)\hat a^\dagger_{p_B}\bigr) .
> $$
>
> $2 + 4 = 6$ exchanges: sign $+1$.
>
> **Step 3** (the $u$-diagram, $p_A$, $p_2$ at one vertex). The pairs are $(\hat a_{p_2}\hat{\bar\psi}(z_1))$, $(\hat\psi(z_1)\hat a^\dagger_{p_A})$, $(\hat a_{p_1}\hat{\bar\psi}(z_2))$, $(\hat\psi(z_2)\hat a^\dagger_{p_B})$. Move $\hat a^\dagger_{p_A}$ to the left as before (2 exchanges), then $\hat a_{p_1}$ to the right past $\hat{\bar\psi}(z_1)$, $\hat\psi(z_1)$, $\hat a^\dagger_{p_A}$ (3 exchanges):
>
> $$
> \bigl(\hat a_{p_2}\hat{\bar\psi}(z_1)\bigr)\bigl(\hat\psi(z_1)\hat a^\dagger_{p_A}\bigr)\bigl(\hat a_{p_1}\hat{\bar\psi}(z_2)\bigr)\bigl(\hat\psi(z_2)\hat a^\dagger_{p_B}\bigr) .
> $$
>
> $2 + 3 = 5$ exchanges: sign $-1$. The two diagrams enter with a relative minus sign, $t$ with $+$ and $u$ with $-$, as in [[§C6d.5 Second Order#^ex-c6d-5-2|Example §C6d.5.2]] (2 and 3 crossings there).
>
> **Step 4** (the copies with $z_1 \leftrightarrow z_2$). The bilinears $\hat{\bar\psi}\hat\psi$ are bosonic, so the copy of each contraction with the vertices exchanged has no extra sign and gives the same integral after relabelling; the $\frac{1}{2!}$ cancels ([[§C6d.5 Second Order#^thm-c6d-5-2|Theorem §C6d.5.2]]). Each adjacent pair then gives its external spinor, $(\hat a_{p_1}\hat{\bar\psi}(z_1)) \to \bar u^{s_1}(p_1)e^{ip_1\cdot z_1}$, $(\hat\psi(z_1)\hat a^\dagger_{p_A}) \to u^{s_A}(p_A)e^{-ip_A\cdot z_1}$, and so on ([[§C6d.2 Contractions with External Fermions#^thm-c6d-2-1|Theorem §C6d.2.1]]), and the vertex integrals give the amplitude of [[§C6d.5 Second Order#^ex-c6d-5-2|Example §C6d.5.2]].
>
> **What the derivation shows**
> - The relative sign is a parity of operator exchanges; it agrees with the crossing count ([[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-4|Theorem §C6d.3.4]]) and with Fermi statistics (the first derivation). Which diagram carries the $-$ depends on the order of the bra, the relative sign does not.
>
> *Source: PHY 513, Problem Set 9, Problem 4(a) (the user's solution, paragraph "Relative sign")*

^der-c6d-5-3b

*Uses:* [[§C6d.5 Second Order#^ex-c6d-5-2|Example §C6d.5.2]], [[§C6d.5 Second Order#^thm-c6d-5-2|Theorem §C6d.5.2]], [[§C6d.5 Second Order#^rem-c6d-5-1|Remark: The overall sign]], [[§C6d.2 Contractions with External Fermions#^thm-c6d-2-1|Theorem §C6d.2.1]], [[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-4|Theorem §C6d.3.4]]

> [!remark] Remark: The overall sign
> Writing $|\mathbf k, \mathbf p\rangle$ for $|\mathbf p, \mathbf k\rangle$, or $\langle\mathbf k', \mathbf p'|$ for $\langle\mathbf p', \mathbf k'|$, flips the sign of $\mathcal M$ ([[§C6d.5 Second Order#^thm-c6d-5-3|Theorem §C6d.5.3]], Step 1); $|\mathcal M|^2$, and with it every cross section, is unchanged ("Overall sign usually irrelevant (only $|\mathcal M|^2$ appears in cross-section)", slide 23). In this sense only, as a relabelling of the external state, the overall sign is a convention; the sources differ only here:
>
> | source | states | $t$-term | $u$-term |
> |---|---|---|---|
> | the user's notes (§17.6), PS (4.118)–(4.119), this section | bra the adjoint of the ket, $\langle0\vert\hat a_{\mathbf k'}\hat a_{\mathbf p'}$ | $+$ | $-$ |
> | Lecture 17, slide 20 and the board | not stated | $-$ | $+$ |
> | Yu (7.82) | bra in the order of the labels, $\langle0\vert\hat a_{\mathbf q_1}\hat a_{\mathbf q_2}$ (7.12) | $-$ | $+$ |
>
> With the bra $\langle0|\hat a_{\mathbf p'}\hat a_{\mathbf k'}$ (labels in order) the string of Step 5 of [[§C6d.5 Second Order#^ex-c6d-5-2|Example §C6d.5.2]] has the $t$-pairs $(1, 3)$, $(4, 7)$, $(2, 5)$, $(6, 8)$: three crossings, sign $-$, and the $u$-pattern two: the slide's and Yu's signs (derived here; the lecture chose its overall sign without fixing the states).
>
> This does not make the overall sign a mere convention (Lecture 18). Reordering the states also flips the overlap $\langle\mathbf p', \mathbf k'|\mathbf p, \mathbf k\rangle$, the $\mathbb 1$ of $\hat S = \mathbb 1 + i\hat T$, so the sign of $\mathcal M$ relative to that $\mathbb 1$ does not depend on the ordering: it is fixed and physical. It governs the interference with the unscattered term $\langle f|i\rangle$, enters the comparison with the Born approximation ([[§C6d.7 The Yukawa Potential#^thm-c6d-7-5|Theorem §C6d.7.5]]) and decides between attraction and repulsion. Taking each bra to be the Hermitian conjugate of its ket, $(|f\rangle)^\dagger = \langle f|$ (PS (4.118), the convention of this section), makes the identity term $+1$ and gives $\mathcal M$ this physical sign ([[§C8.5 The Coulomb Potential, and Why Like Charges Repel#^thm-c8-5-6|Theorem §C8.5.6]]). The signs inside Wick's theorem, from reordering bilinears, never cause this ambiguity: they come in packages ([[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^rem-c6d-3-1|§C6d.3, Remark: Where the fermion signs go]]).
>
> *Source: PHY 513 Lecture 17, slides 20, 23, and transcript (about 70–75 min) · the user's PHY 513 notes, Lecture 17 update, §17.6, paragraph "The overall sign is a convention" (its title before the Lecture 18 correction) · PS §4.7, p. 119, eq. (4.118), p. 120, eq. (4.119) · Yu §7.1, eq. (7.12); §7.1.2, eq. (7.82) · the crossing count for the label-ordered bra written here · the second paragraph: the user's PHY 513 notes, Lecture 18 update, Part 2 (a) (the corrected paragraph "The overall sign": "An earlier version of these notes called the overall sign a convention; Lecture 18 showed why it is not") and §18.7, paragraph "The overall sign, revisited"*

^rem-c6d-5-1

> [!caution] Caution: Slips in the handwritten notes and on slide 20 for this example
> The user's update lists three slips of the handwritten page (the page itself is not a source here):
> 1. The plane waves are written $e^{-ip\cdot x - ik\cdot y - ip'\cdot x - ik'\cdot y}$; outgoing particles give $e^{+ip'\cdot x}$, $e^{+ik'\cdot y}$ ([[§C6d.2 Contractions with External Fermions#^thm-c6d-2-1|Theorem §C6d.2.1]]), so the exponent is $-i(p - p')\cdot x - i(k - k')\cdot y$, which is what makes momentum conservation come out.
> 2. The second line has $\bar u(k)u(k)$ for $\bar u(k')u(k)$.
> 3. The result is written $(-ig)^2D_F(p - p')\bigl(\bar u(p')u(p)\bar u(k')u(k) + k \leftrightarrow p\bigr)$; the exchanged term has its own propagator, at $p - k'$, and enters with a relative minus sign; the diagrams below it carry the relative sign.
>
> Slide 20 has the analogue of item 3: "$i\mathcal M = (-ig)^2D_F(p - p')\bigl[(-)(\bar u(p')u(p))(\bar u(k')u(k)) + p \leftrightarrow k\bigr]$" factors the $t$-channel propagator out of both terms; the $p \leftrightarrow k$ image carries $D_F$ at $k - p'$, i.e. at $(p - k')^2$, as the slide's own second diagram ("$p - k'$") shows. Its first exponent, printed $e^{i(px' + k'y - px - ky)}$, means $p'\cdot x$. The lecture acknowledged that this line was not well written and that the diagrams are the better way to write it.
>
> *Source: the user's PHY 513 notes, Lecture 17 update, §17.6, Caution "Slips in the handwritten notes for this example" · PHY 513 Lecture 17, slide 20, and transcript · recorded in `qft-C/ERRATA.md`*

^cau-c6d-5-1

## Annihilation into two scalars

> [!example]- ★ Example §C6d.5.3: f f̄ → φφ at Order g²: Two Diagrams with a Relative Plus Sign
> ![[ph-qft-c6d-5-3.svg]]
>
> In [[§C6d.1 Yukawa Theory#^mod-c6d-1-1|Model §C6d.1.1]], for $f(p_1, s_1) + \bar f(p_2, s_2) \to \phi(k_1) + \phi(k_2)$, initial state $\sqrt{4E_{\mathbf p_1}E_{\mathbf p_2}}\,\hat a^\dagger_{\mathbf p_1}\hat b^\dagger_{\mathbf p_2}|0\rangle$, at order $g^2$
>
> $$
> i\mathcal M = (-ig)^2\Bigl[\bar v(p_2)\,\frac{i(\slashed p_1 - \slashed k_1 + m)}{(p_1 - k_1)^2 - m^2 + i\varepsilon}\,u(p_1) \;+\; \bar v(p_2)\,\frac{i(\slashed p_1 - \slashed k_2 + m)}{(p_1 - k_2)^2 - m^2 + i\varepsilon}\,u(p_1)\Bigr] :
> $$
>
> one fermion line from $u(p_1)$ to $\bar v(p_2)$ with an internal fermion propagator, the two scalars attached in either order, **relative sign $+$**: the diagrams differ by exchanging two identical bosons ([[§C6d.5 Second Order#^thm-c6d-5-4|Theorem §C6d.5.4]]). Both are trees; the momentum on the internal line runs along its arrow ([[§C6d.6 Momentum-Space Feynman Rules#^rem-c6d-6-1|§C6d.6, Remark: The direction of momentum on fermion lines]]).
>
> **Step 1** (the terms). Two fermions in, none out, two scalars out: one $\hat\psi$ and one $\hat{\bar\psi}$ for the particles, the other two contracted: terms 3 and 4 of [[§C6d.5 Second Order#^thm-c6d-5-1|Theorem §C6d.5.1]], and $i\hat T^{(2)}_3 + i\hat T^{(2)}_4 = 2\,i\hat T^{(2)}_3$ ([[§C6d.5 Second Order#^thm-c6d-5-2|Theorem §C6d.5.2]]):
>
> $$
> (-ig)^2\int d^4x\,d^4y\;S_F(x - y)_{ab}\,{:}\hat{\bar\psi}_{x,a}\hat\phi_x\hat\phi_y\hat\psi_{y,b}{:} .
> $$
>
> **Step 2** (the fermions, [[§C6d.2 Contractions with External Fermions#^thm-c6d-2-1|Theorem §C6d.2.1]]). $\hat\psi_y$ absorbs $f(p_1)$: $u(p_1)e^{-ip_1\cdot y}$; $\hat{\bar\psi}_x$ absorbs $\bar f(p_2)$: $\bar v(p_2)e^{-ip_2\cdot x}$. Fermion string $\hat{\bar\psi}_x(1)\,\hat\psi_x(2)\,\hat{\bar\psi}_y(3)\,\hat\psi_y(4)\,\hat a^\dagger_{\mathbf p_1}(5)\,\hat b^\dagger_{\mathbf p_2}(6)$: pairs $(2, 3)$, $(4, 5)$, $(1, 6)$, nested and apart, **no crossing** ([[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-4|Theorem §C6d.3.4]]). The chain, against the arrow from $y$ to $x$: $\bar v_a(p_2)\,S_F(x - y)_{ab}\,u_b(p_1)$ ([[§C6d.2 Contractions with External Fermions#^thm-c6d-2-4|Theorem §C6d.2.4]]).
>
> **Step 3** (the scalars). $\langle\mathbf k_1\mathbf k_2|{:}\hat\phi_x\hat\phi_y{:}|0\rangle = e^{ik_1\cdot x}e^{ik_2\cdot y} + e^{ik_2\cdot x}e^{ik_1\cdot y}$ ([[§C6c.2 Contractions with External Particles#^thm-c6c-2-3|Theorem §C6c.2.3]], $n = 2$): two attachments, both with $+$, since scalar operators commute with everything.
>
> **Step 4** (momenta). With $S_F(x - y) = \int\frac{d^4q}{(2\pi)^4}\frac{i(\slashed q + m)}{q^2 - m^2 + i\varepsilon}e^{-iq\cdot(x - y)}$ ([[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-3|Theorem §C5b.8.3]]), take the attachment with $k_1$ at $y$: the $y$ integral $\int d^4y\,e^{i(q + k_1 - p_1)\cdot y} = (2\pi)^4\delta^4(q + k_1 - p_1)$ sets $q = p_1 - k_1$, along the arrow from $y$ to $x$; the $x$ integral gives $(2\pi)^4\delta^4(p_1 + p_2 - k_1 - k_2)$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]]). The other attachment is the same with $k_1 \leftrightarrow k_2$.
>
> **Step 5** (read off). Stripping the overall delta ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-3|Def. §C6b.1.3]]) gives the statement, Yu (7.89). The amplitude is symmetric under $k_1 \leftrightarrow k_2$, as it must be for two identical bosons.
>
> *Equivalently,* the scalar analogue is the $t$- and $u$-channel pair of [[§C6c.6 Feynman Rules for Amplitudes#^thm-c6c-6-4|Theorem §C6c.6.4]], also with relative $+$; with an exchanged fermion the propagator has the numerator $\slashed q + m$.
>
> *Source: Yu §7.1.2, eqs. (7.83)–(7.89), Fig. 7.6, pp. 280–282 ("它包含 2 个拓扑不等价的子图，相对符号为正，体现了交换末态两个全同玻色子的对称性") · beyond the course (QED's version, $e^+e^- \to \gamma\gamma$, is a process of C8, planned) · recomputed here*

^ex-c6d-5-3

## Relative signs

> [!theorem] Theorem §C6d.5.4: The Relative Sign: Minus for Exchanged Fermions, Plus for Exchanged Bosons
> In [[§C6d.1 Yukawa Theory#^mod-c6d-1-1|Model §C6d.1.1]], with states as in [[§C6d.2 Contractions with External Fermions#^def-c6d-2-2|Def. §C6d.2.2]], let two full contraction patterns $P$, $P'$ of one term $\langle f|T\{\cdots\}|i\rangle$ differ only in that two fermion fields of the same kind (two $\hat\psi$'s, or two $\hat{\bar\psi}$'s) have exchanged their external partners. Then their signs ([[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-4|Theorem §C6d.3.4]]) are opposite:
>
> $$
> (-1)^{\#\text{crossings}(P')} = -\,(-1)^{\#\text{crossings}(P)} .
> $$
>
> If two scalar fields exchange their partners, the sign is unchanged. Hence:
> 1. two diagrams related by exchanging two **identical external fermions** (two incoming, or two outgoing) enter with a relative $-$: $ff \to ff$, $t$ against $u$ ([[§C6d.5 Second Order#^ex-c6d-5-2|Example §C6d.5.2]], [[§C6d.5 Second Order#^thm-c6d-5-3|Theorem §C6d.5.3]]);
> 2. the same holds whenever the exchanged partners of two $\hat\psi$'s (or two $\hat{\bar\psi}$'s) are a fermion and an antifermion, e.g. an incoming $f$ and an outgoing $\bar f$, both absorbed or emitted by $\hat\psi$: $f\bar f \to f\bar f$, $s$ against $t$ ([[§C6d.5 Second Order#^ex-c6d-5-1|Example §C6d.5.1]]);
> 3. two diagrams related by exchanging two **identical bosons** enter with a relative $+$: $f\bar f \to \phi\phi$ ([[§C6d.5 Second Order#^ex-c6d-5-3|Example §C6d.5.3]]), $\phi\phi \to \phi\phi$ ([[§C6c.6 Feynman Rules for Amplitudes#^thm-c6c-6-4|Theorem §C6c.6.4]]).
>
> The relative sign is physical: it enters $|\mathcal M|^2$ through the interference term ([[§C6d.5 Second Order#^thm-c6d-5-5|Theorem §C6d.5.5]]); the overall sign does not enter $|\mathcal M|^2$: it follows the order in which the external states are written and, with each bra the Hermitian conjugate of its ket, is physical relative to the $\mathbb 1$ of $\hat S = \mathbb 1 + i\hat T$ ([[§C6d.5 Second Order#^rem-c6d-5-1|Remark: The overall sign]], [[§C8.5 The Coulomb Potential, and Why Like Charges Repel#^thm-c8-5-6|Theorem §C8.5.6]]).
>
> *Model:* [[§C6d.1 Yukawa Theory#^mod-c6d-1-1|Model §C6d.1.1]], any theory with fermions (QED alike); *applies:* every order, free states as in [[§C6d.2 Contractions with External Fermions#^def-c6d-2-2|Def. §C6d.2.2]]; a statement about the sign factor, the values of the pairs being the reassigned wave functions.
>
> *Source: PHY 513 Lecture 17, slide 23 ("Relative signs enforce statistics of identical particles") · PS §4.7, p. 120 ("The minus sign difference between these diagrams is a reflection of Fermi statistics") · Yu §7.1.2, p. 275 (relative $-$ for $\psi\bar\psi \to \psi\bar\psi$), p. 279 (relative $-$, "体现了交换末态全同费米子的反对称性"), p. 282 (relative $+$, "体现了交换末态两个全同玻色子的对称性"); §7.2, p. 289 · generalizes [[§C6d.5 Second Order#^thm-c6d-5-3|Theorem §C6d.5.3]] (the first "What the derivation shows" bullet of [[§C6d.5 Second Order#^der-c6d-5-3|Derivation §C6d.5.3]]) · proof written here*

^thm-c6d-5-4

> [!derivation]- Derivation
> **Step 1** (the sign as a permutation). By [[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^lem-c6d-3-3|Lemma §C6d.3.3]], 1, $(-1)^{\#\text{crossings}(P)} = \operatorname{sgn}(\pi_P)$, $\pi_P$ the permutation of the fermion string that brings every pair of $P$ next to each other.
>
> **Step 2** (the exchange is a transposition). Let the two fermion fields sit at positions $i$, $j$ and their partners in $P$ at $a$, $b$: pairs $(i, a)$, $(j, b)$; in $P'$: $(i, b)$, $(j, a)$, all other pairs the same. Let $\tau$ exchange the operators at positions $a$ and $b$. Applying $\tau$ first and then $\pi_P$ brings the pairs of $P'$ next to each other: $\pi_{P'} = \pi_P\circ\tau$. If $a$ and $b$ stand on opposite sides of the fields (one in the bra, one in the ket), both new pairs come out in reversed order; restoring the row order of each is one transposition, two in all, which does not change the sign. A transposition is odd: $\operatorname{sgn}(\pi_{P'}) = -\operatorname{sgn}(\pi_P)$.
>
> **Step 3** (the values). The external partners are wave functions, $c$-numbers; in $P'$ the same wave functions are reassigned to the other field, written in the same order relative to the bra and the ket (bra operators left of all fields, ket operators right of them). So no further sign enters, and the two terms differ by $-1$ times the exchange of the arguments.
>
> **Step 4** (scalars). Scalar operators commute with all operators and do not appear in the fermion string: exchanging the partners of two $\hat\phi$'s changes no crossing, sign $+$.
>
> **Step 5** (the three cases). (1) In $ff \to ff$ the two $\hat{\bar\psi}$'s exchange the outgoing $p'$, $k'$ ($t$ ↔ $u$, Step 5 of [[§C6d.5 Second Order#^ex-c6d-5-2|Example §C6d.5.2]]: 2 and 3 crossings). (2) In $f\bar f \to f\bar f$ the two $\hat\psi$'s exchange $p_1$ (in the ket) and $q_2$ (in the bra) ($t$ ↔ $s$, Step 4 of [[§C6d.5 Second Order#^ex-c6d-5-1|Example §C6d.5.1]]: 3 and 0 crossings). (3) In $f\bar f \to \phi\phi$ the two $\hat\phi$'s exchange $k_1$, $k_2$ (Step 3 of [[§C6d.5 Second Order#^ex-c6d-5-3|Example §C6d.5.3]]).
>
> **What the derivation shows.**
> - Fermi statistics of the external states and the crossing count are one fact: the odd transposition.

^der-c6d-5-4

*Uses:* [[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^lem-c6d-3-3|Lemma §C6d.3.3]], [[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-4|Theorem §C6d.3.4]], [[§C6d.5 Second Order#^ex-c6d-5-1|Example §C6d.5.1]], [[§C6d.5 Second Order#^ex-c6d-5-2|Example §C6d.5.2]], [[§C6d.5 Second Order#^ex-c6d-5-3|Example §C6d.5.3]]

> [!theorem] Theorem §C6d.5.5: The Relative Sign Fixes the Sign of the Interference Term
> Let a process have two diagrams, $i\mathcal M = i\mathcal M_1 + \eta\,i\mathcal M_2$, with relative sign $\eta = \pm1$ ([[§C6d.5 Second Order#^thm-c6d-5-4|Theorem §C6d.5.4]]). Then
>
> $$
> |\mathcal M|^2 = |\mathcal M_1|^2 + |\mathcal M_2|^2 + 2\eta\,\operatorname{Re}\bigl(\mathcal M_1^\ast\mathcal M_2\bigr) ,
> $$
>
> so the sign of the interference term in every cross section and width ([[§C6b.5 Decay Widths#^thm-c6b-5-6|Theorem §C6b.5.6]]) is the relative sign, while an overall sign $i\mathcal M \to -i\mathcal M$ leaves $|\mathcal M|^2$ unchanged. For $f\bar f \to f\bar f$ ($\eta = -1$, [[§C6d.5 Second Order#^ex-c6d-5-1|Example §C6d.5.1]]), $|\mathcal M|^2 = |\mathcal M_1|^2 + |\mathcal M_2|^2 - (\mathcal M_1^\ast\mathcal M_2 + \mathcal M_2^\ast\mathcal M_1)$ (Yu (7.75)); for $ff \to ff$ the interference term is $-2\operatorname{Re}(\mathcal M_t^\ast\mathcal M_u)$. A wrong relative sign changes $|\mathcal M|^2$ by $4\operatorname{Re}(\mathcal M_1^\ast\mathcal M_2)$.
>
> *Model:* any amplitude that is a sum of two terms; *applies:* exact algebra; the spin sums of $|\mathcal M|^2$ act on each term.
>
> *Source: Yu §7.1.2, eq. (7.75), p. 275 ("其中两个子振幅的干涉项 $-(\mathcal M_1^\ast\mathcal M_2 + \mathcal M_2^\ast\mathcal M_1)$ 的符号由它们的相对符号决定。因此，确定相对符号对于正确地计算散射截面至关重要"); p. 268 ("如果一个过程存在多个概率振幅，则振幅之间的相对符号会影响观测量") · PHY 513 Lecture 17, slide 23 ("Overall sign usually irrelevant (only $|\mathcal M|^2$ appears in cross-section)") · from the ⚑ of [[§C6d.5 Second Order#^der-c6d-5-3|Derivation §C6d.5.3]]*

^thm-c6d-5-5

> [!derivation]- Derivation
> **Step 1** (expand). $|\mathcal M|^2 = (\mathcal M_1 + \eta\mathcal M_2)^\ast(\mathcal M_1 + \eta\mathcal M_2) = \mathcal M_1^\ast\mathcal M_1 + \eta^2\mathcal M_2^\ast\mathcal M_2 + \eta\,(\mathcal M_1^\ast\mathcal M_2 + \mathcal M_2^\ast\mathcal M_1)$, $\eta$ real.
>
> **Step 2** (simplify). $\eta^2 = 1$, and $\mathcal M_2^\ast\mathcal M_1 = (\mathcal M_1^\ast\mathcal M_2)^\ast$, so $\mathcal M_1^\ast\mathcal M_2 + \mathcal M_2^\ast\mathcal M_1 = 2\operatorname{Re}(\mathcal M_1^\ast\mathcal M_2)$.
>
> **Step 3** (overall sign). $|-\mathcal M|^2 = (-1)^2|\mathcal M|^2 = |\mathcal M|^2$. Changing $\eta$ to $-\eta$ changes $|\mathcal M|^2$ by $-4\eta\operatorname{Re}(\mathcal M_1^\ast\mathcal M_2)$.
>
> **What the derivation shows.**
> - Only the relative sign is observable; it must be taken from the contractions ([[§C6d.6 Momentum-Space Feynman Rules#^cau-c6d-6-1|§C6d.6, Caution: Relative signs still need the contractions]]).

^der-c6d-5-5

*Uses:* [[§C6d.5 Second Order#^thm-c6d-5-4|Theorem §C6d.5.4]]

## Loops and bubbles

> [!example]- ★ Example §C6d.5.4: Disconnected Second-Order Terms Do Not Contribute
> ![[ph-qft-c6d-5-4.svg]]
>
> In [[§C6d.1 Yukawa Theory#^mod-c6d-1-1|Model §C6d.1.1]], terms $5$ and $6$ of [[§C6d.5 Second Order#^thm-c6d-5-1|Theorem §C6d.5.1]] (a tadpole at one vertex) between $f(p_1)\bar f(p_2)$ and $\phi(k_1)\phi(k_2)$ give
>
> $$
> \langle\mathbf k_1\mathbf k_2|\bigl(i\hat T^{(2)}_5 + i\hat T^{(2)}_6\bigr)|\mathbf p_1, \mathbf p_2\rangle = (-ig)^2\bigl(-\operatorname{tr}S_F(0)\bigr)\,\bar v(p_2)u(p_1)\Bigl[(2\pi)^4\delta^4(k_2)\,(2\pi)^4\delta^4(p_1 + p_2 - k_1) + (k_1 \leftrightarrow k_2)\Bigr] :
> $$
>
> two pieces, a tadpole emitting one scalar and the first-order fusion $f\bar f \to \phi$ at the other vertex, each with its own momentum delta. Neither has the form $\delta^4(p_1 + p_2 - k_1 - k_2)\times(\text{smooth})$, and $\delta^4(k_2) = 0$ on shell: no contribution to $f\bar f \to \phi\phi$, which comes from terms $3$–$4$ alone ([[§C6d.5 Second Order#^ex-c6d-5-3|Example §C6d.5.3]]).
>
> **Step 1** (the terms). $i\hat T^{(2)}_5 + i\hat T^{(2)}_6 = 2\,i\hat T^{(2)}_5$ ([[§C6d.5 Second Order#^thm-c6d-5-2|Theorem §C6d.5.2]]) $= (-ig)^2\int d^4x\,d^4y\,\overbracket{\hat{\bar\psi}_x\hat\psi_x}\;{:}\hat\phi_x\,\hat{\bar\psi}_y\hat\psi_y\hat\phi_y{:}$, with $\overbracket{\hat{\bar\psi}_x\hat\psi_x} = -\operatorname{tr}S_F(0)$ ([[§C6d.4 First Order#^thm-c6d-4-1|Theorem §C6d.4.1]]).
>
> **Step 2** (attachments). $\hat\psi_y$ absorbs $f(p_1)$ ($u(p_1)e^{-ip_1\cdot y}$), $\hat{\bar\psi}_y$ absorbs $\bar f(p_2)$ ($\bar v(p_2)e^{-ip_2\cdot y}$); fermion string $\hat{\bar\psi}_x(1)\hat\psi_x(2)\hat{\bar\psi}_y(3)\hat\psi_y(4)\hat a^\dagger_{\mathbf p_1}(5)\hat b^\dagger_{\mathbf p_2}(6)$, pairs $(1, 2)$, $(4, 5)$, $(3, 6)$: no crossing. The scalars: $\hat\phi_x$, $\hat\phi_y$ take $k_1$, $k_2$ in two ways ([[§C6c.2 Contractions with External Particles#^thm-c6c-2-3|Theorem §C6c.2.3]]).
>
> **Step 3** (vertex integrals). With $k_2$ at $x$: $\int d^4x\,e^{ik_2\cdot x} = (2\pi)^4\delta^4(k_2)$ and $\int d^4y\,e^{i(k_1 - p_1 - p_2)\cdot y} = (2\pi)^4\delta^4(p_1 + p_2 - k_1)$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]]); the other attachment exchanges $k_1 \leftrightarrow k_2$.
>
> **Step 4** (fate). Two deltas for two pieces: the term is not one process ([[§C6c.3 Wick's Theorem between Particle States#^thm-c6c-3-3|Theorem §C6c.3.3]], [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-6|Theorem §C6c.4.6]], 2), and each piece is kinematically forbidden on its own unless $m_\phi > 2m$ for the fusion; the tadpole never ([[§C6d.4 First Order#^thm-c6d-4-5|Theorem §C6d.4.5]]).
>
> *Equivalently,* the scalar case is [[§C6c.3 Wick's Theorem between Particle States#^thm-c6c-3-3|Theorem §C6c.3.3]]: every connected piece carries its own delta.
>
> *Source: Yu §7.1.2, eqs. (7.90)–(7.92), Fig. 7.7, p. 283 ("每个子图都具有 2 个不相连的部分 … 这种图既不满足能动量守恒定律，也不会贡献到 $\psi\bar\psi \to \phi\phi$ 散射过程") · beyond the course · written out here*

^ex-c6d-5-4

> [!example]- ★ Example §C6d.5.5: The Fermion Self-Energies at Order g²
> ![[ph-qft-c6d-5-5.svg]]
>
> In [[§C6d.1 Yukawa Theory#^mod-c6d-1-1|Model §C6d.1.1]], between one-fermion states $\langle\mathbf p', s'|$ and $|\mathbf p, s\rangle$ the second order has two one-loop diagrams ([[§C6d.4 First Order#^def-c6d-4-4|Def. §C6d.4.4]]): (a) the fermion emits and reabsorbs a scalar (terms $7$, $8$ of [[§C6d.5 Second Order#^thm-c6d-5-1|Theorem §C6d.5.1]]), (b) a tadpole hangs on the fermion line by a scalar of zero momentum (terms $9$, $10$):
>
> $$
> \begin{aligned}
> \text{(a)}\quad &(-ig)^2\int\frac{d^4q}{(2\pi)^4}\;\bar u^{s'}(p)\,\frac{i}{(p - q)^2 - m_\phi^2 + i\varepsilon}\,\frac{i(\slashed q + m)}{q^2 - m^2 + i\varepsilon}\,u^s(p)\;(2\pi)^4\delta^4(p - p') ,\\
> \text{(b)}\quad &(-ig)^2\;\frac{i}{m_\phi^2}\operatorname{tr}S_F(0)\;\bar u^{s'}(p)u^s(p)\;(2\pi)^4\delta^4(p - p') .
> \end{aligned}
> $$
>
> Both are forward ($p' = p$): no scattering, but corrections of the external fermion (its mass and normalization), removed from $i\mathcal M$ by amputation ([[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^thm-c6c-5-3|Theorem §C6c.5.3]], 1). In (a) the loop momentum $q$ runs through the fermion line and $p - q$ through the scalar; (b) contains the closed loop of [[§C6d.4 First Order#^thm-c6d-4-6|Theorem §C6d.4.6]] at $n = 1$.
>
> **Step 1** (the terms). $i\hat T^{(2)}_7 + i\hat T^{(2)}_8 = 2\,i\hat T^{(2)}_7 = (-ig)^2\int d^4x\,d^4y\,D_F(x - y)\,S_F(x - y)_{ab}\,{:}\hat{\bar\psi}_{x,a}\hat\psi_{y,b}{:}$, and $i\hat T^{(2)}_9 + i\hat T^{(2)}_{10} = 2\,i\hat T^{(2)}_9 = (-ig)^2\int d^4x\,d^4y\,D_F(x - y)\,\bigl(-\operatorname{tr}S_F(0)\bigr)\,{:}\hat{\bar\psi}_{y,a}\hat\psi_{y,a}{:}$ ([[§C6d.5 Second Order#^thm-c6d-5-1|Theorem §C6d.5.1]], [[§C6d.5 Second Order#^thm-c6d-5-2|Theorem §C6d.5.2]]).
>
> **Step 2** (attachments and sign). (a): $\hat{\bar\psi}_x$ emits $p'$ ($\bar u^{s'}(p')e^{ip'\cdot x}$), $\hat\psi_y$ absorbs $p$ ($u^s(p)e^{-ip\cdot y}$); string $\hat a_{\mathbf p'}(1)\,\hat{\bar\psi}_x(2)\,[\hat\psi_x(3)\,\hat{\bar\psi}_y(4)]\,\hat\psi_y(5)\,\hat a^\dagger_{\mathbf p}(6)$, pairs $(1, 2)$, $(3, 4)$, $(5, 6)$: no crossing. Chain against the arrow $y \to x$: $\bar u^{s'}(p')\,S_F(x - y)\,u^s(p)$ ([[§C6d.2 Contractions with External Fermions#^thm-c6d-2-4|Theorem §C6d.2.4]]). (b): $\hat{\bar\psi}_y$, $\hat\psi_y$ take $p'$, $p$; pairs $(1, 4)$, $(2, 3)$ (the tadpole at $x$), $(5, 6)$: nested, no crossing; chain $\bar u^{s'}(p')u^s(p)$.
>
> **Step 3** (momenta in (a)). $D_F(x - y) = \int\frac{d^4k}{(2\pi)^4}\frac{ie^{-ik\cdot(x - y)}}{k^2 - m_\phi^2 + i\varepsilon}$, $S_F(x - y) = \int\frac{d^4q}{(2\pi)^4}\frac{i(\slashed q + m)e^{-iq\cdot(x - y)}}{q^2 - m^2 + i\varepsilon}$. The $x$ integral $\int d^4x\,e^{i(p' - k - q)\cdot x} = (2\pi)^4\delta^4(p' - k - q)$, the $y$ integral $(2\pi)^4\delta^4(k + q - p)$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]]); the $k$ integral sets $k = p - q$ and leaves $(2\pi)^4\delta^4(p - p')$; $q$ is not fixed: a loop momentum ([[§C6d.4 First Order#^def-c6d-4-3|Def. §C6d.4.3]]). On the support $\bar u(p') = \bar u(p)$ (Yu (7.95)–(7.96)).
>
> **Step 4** (momenta in (b)). The $x$ integral acts on $D_F$ alone: $\int d^4x\,D_F(x - y) = \int\frac{d^4k}{(2\pi)^4}\frac{ie^{ik\cdot y}}{k^2 - m_\phi^2 + i\varepsilon}(2\pi)^4\delta^4(k) = \frac{i}{-m_\phi^2}$: the scalar carries zero momentum. With $-\operatorname{tr}S_F(0)$: $\frac{-i}{m_\phi^2}\cdot(-\operatorname{tr}S_F(0)) = \frac{i}{m_\phi^2}\operatorname{tr}S_F(0)$; the $y$ integral gives $(2\pi)^4\delta^4(p - p')$ (Yu (7.97)–(7.99)).
>
> **Step 5** (fate). One incoming and one outgoing fermion at the same momentum: forward, part of the $\mathbb 1$ and of the correction of the external state ([[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-6|Theorem §C6c.4.6]], 2; [[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^thm-c6c-5-3|Theorem §C6c.5.3]], 1). Each diagram has $V = 2$, $I = 2$, $L = 1$ ([[§C6a.12 Feynman Rules for Polynomial Interactions#^thm-c6a-12-3|Theorem §C6a.12.3]]).
>
> *Equivalently,* the scalar case is [[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^ex-c6c-5-2|Example §C6c.5.2]] (the second-order self-energies of $\phi^4$ with $S = 4, 6, 4$); here every $S = 1$ ([[§C6d.4 First Order#^thm-c6d-4-7|Theorem §C6d.4.7]]).
>
> *Source: Yu §7.1.2, eqs. (7.93)–(7.99), Fig. 7.8, pp. 283–285 ("这种初末态都是同一个粒子的圈图称为该粒子的自能图 (self-energy diagram)") · beyond the course · (b) evaluated here*

^ex-c6d-5-5

> [!example]- ★ Example §C6d.5.6: The Scalar Self-Energy: a Closed Fermion Loop with n = 2
> ![[ph-qft-c6d-5-6.svg]]
>
> In [[§C6d.1 Yukawa Theory#^mod-c6d-1-1|Model §C6d.1.1]], between one-scalar states, term $11$ of [[§C6d.5 Second Order#^thm-c6d-5-1|Theorem §C6d.5.1]] gives the scalar self-energy, a fermion loop through two vertices:
>
> $$
> \langle\mathbf k'|i\hat T^{(2)}_{11}|\mathbf k\rangle = -(-ig)^2\int\frac{d^4\ell}{(2\pi)^4}\operatorname{tr}\Bigl[\frac{i(\slashed\ell + m)}{\ell^2 - m^2 + i\varepsilon}\,\frac{i(\slashed\ell + \slashed k + m)}{(\ell + k)^2 - m^2 + i\varepsilon}\Bigr]\,(2\pi)^4\delta^4(k - k') :
> $$
>
> the $-1$ and the trace of a closed loop ([[§C6d.4 First Order#^thm-c6d-4-6|Theorem §C6d.4.6]], $n = 2$), one loop momentum $\ell$, the momentum $k$ of the scalar flowing through the loop. Forward: a correction of the external scalar.
>
> **Step 1** (the term). $i\hat T^{(2)}_{11} = \frac{(-ig)^2}{2!}\int d^4x\,d^4y\,\bigl(-\operatorname{tr}[S_F(x - y)S_F(y - x)]\bigr)\,{:}\hat\phi_x\hat\phi_y{:}$ ([[§C6d.5 Second Order#^thm-c6d-5-1|Theorem §C6d.5.1]]): the pairs $\hat\psi_x\hat{\bar\psi}_y = S_F(x - y)$ and $\hat{\bar\psi}_x\hat\psi_y = -S_F(y - x)$, nested in the string $\hat{\bar\psi}_x\hat\psi_x\hat{\bar\psi}_y\hat\psi_y$, the indices joined round the loop.
>
> **Step 2** (attachments). $\langle\mathbf k'|{:}\hat\phi_x\hat\phi_y{:}|\mathbf k\rangle = e^{ik'\cdot x}e^{-ik\cdot y} + e^{ik'\cdot y}e^{-ik\cdot x}$; the two are exchanged by $x \leftrightarrow y$ and cancel the $\frac{1}{2!}$ ([[§C6d.5 Second Order#^thm-c6d-5-2|Theorem §C6d.5.2]]). Keep $e^{ik'\cdot x}e^{-ik\cdot y}$ with $(-ig)^2$.
>
> **Step 3** (momenta). $S_F(x - y) = \int\frac{d^4q_1}{(2\pi)^4}\tilde S_F(q_1)e^{-iq_1\cdot(x - y)}$, $S_F(y - x) = \int\frac{d^4q_2}{(2\pi)^4}\tilde S_F(q_2)e^{-iq_2\cdot(y - x)}$, $\tilde S_F(q) = \frac{i(\slashed q + m)}{q^2 - m^2 + i\varepsilon}$ ([[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-3|Theorem §C5b.8.3]]). The $x$ integral gives $(2\pi)^4\delta^4(k' - q_1 + q_2)$, the $y$ integral $(2\pi)^4\delta^4(q_1 - q_2 - k)$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]]). Set $\ell = q_2$; the first delta fixes $q_1 = \ell + k$ along the arrow from $y$ to $x$, the second becomes $(2\pi)^4\delta^4(k - k')$. With $\operatorname{tr}[\tilde S_F(\ell + k)\tilde S_F(\ell)] = \operatorname{tr}[\tilde S_F(\ell)\tilde S_F(\ell + k)]$ (cyclicity) the statement follows (Yu (7.100)).
>
> **Step 4** (fate). $\delta^4(k - k')$: forward, a correction of the external scalar ([[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^thm-c6c-5-3|Theorem §C6c.5.3]], 1); on an internal scalar line the same loop is the one-loop correction of $D_F$ (renormalization, second semester).
>
> *Equivalently,* the scalar loop corrections of $\phi^4$ are [[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^ex-c6c-5-2|Example §C6c.5.2]] and [[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^ex-c6c-5-1|Example §C6c.5.1]]; a boson loop has no $-1$ and no trace.
>
> *Source: Yu §7.1.2, eq. (7.100), Fig. 7.9, p. 285 ("类似于 Feynman 图 7.2(a) 和 7.2(b)，这里验证了一个普遍的结论：一个封闭的费米子圈贡献一个额外的负号，并且需要对费米子传播子的乘积求迹") · PHY 513 Lecture 17, slide 23 · beyond the course as a computed example · written out here*

^ex-c6d-5-6

> [!example]- ★ Example §C6d.5.7: A Closed Fermion Loop through Three Vertices
> ![[ph-qft-c6d-5-7.svg]]
>
> In a third-order term of [[§C6d.1 Yukawa Theory#^mod-c6d-1-1|Model §C6d.1.1]] (three scalars attached, e.g. Yu's Fig. 7.10), the fermion fields of the vertices $x$, $y$, $z$ contracted into one closed line, the string ${:}\hat{\bar\psi}_a(x)\hat\psi_a(x)\hat{\bar\psi}_b(y)\hat\psi_b(y)\hat{\bar\psi}_c(z)\hat\psi_c(z){:}$ with the three contractions $\hat\psi_x\hat{\bar\psi}_y$, $\hat\psi_y\hat{\bar\psi}_z$, $\hat{\bar\psi}_x\hat\psi_z$ gives
>
> $$
> (+1)\cdot\overbracket{\hat\psi_a(x)\hat{\bar\psi}_b(y)}\;\overbracket{\hat\psi_b(y)\hat{\bar\psi}_c(z)}\;\overbracket{\hat{\bar\psi}_a(x)\hat\psi_c(z)} = -\operatorname{tr}\bigl[S_F(x - y)\,S_F(y - z)\,S_F(z - x)\bigr] = -\operatorname{tr}\bigl[S_F(z - x)\,S_F(x - y)\,S_F(y - z)\bigr] ,
> $$
>
> [[§C6d.4 First Order#^thm-c6d-4-6|Theorem §C6d.4.6]] at $n = 3$ with the arrow $z \to y \to x \to z$; the second form is Yu's (7.101), equal by cyclicity of the trace.
>
> **Step 1** (positions). $\hat{\bar\psi}_x(1)\,\hat\psi_x(2)\,\hat{\bar\psi}_y(3)\,\hat\psi_y(4)\,\hat{\bar\psi}_z(5)\,\hat\psi_z(6)$; pairs $(2, 3)$, $(4, 5)$, $(1, 6)$: the outer arc encloses the two adjacent ones, no crossing, sign $+$ ([[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^lem-c6d-3-3|Lemma §C6d.3.3]], 1).
>
> **Step 2** (values, [[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-1|Theorem §C6d.3.1]]). $\overbracket{\hat\psi_a(x)\hat{\bar\psi}_b(y)} = S_F(x - y)_{ab}$, $\overbracket{\hat\psi_b(y)\hat{\bar\psi}_c(z)} = S_F(y - z)_{bc}$, and the outer pair written $\hat{\bar\psi}$ first, $\overbracket{\hat{\bar\psi}_a(x)\hat\psi_c(z)} = -S_F(z - x)_{ca}$.
>
> **Step 3** (the trace). The product, summed over $a$, $b$, $c$: $-S_F(x - y)_{ab}S_F(y - z)_{bc}S_F(z - x)_{ca} = -\operatorname{tr}[S_F(x - y)S_F(y - z)S_F(z - x)]$; moving the last factor to the front inside the trace gives Yu's order. Yu reaches the same by moving $\hat\psi_c(z)$ to the front past five fermion fields: $(-1)^5 = -1$.
>
> *Equivalently,* $n = 1$ is the tadpole ([[§C6d.4 First Order#^ex-c6d-4-3|Example §C6d.4.3]]), $n = 2$ the scalar self-energy ([[§C6d.5 Second Order#^ex-c6d-5-6|Example §C6d.5.6]]); the theorem for every $n$ is [[§C6d.4 First Order#^thm-c6d-4-6|Theorem §C6d.4.6]].
>
> *Source: Yu §7.1.2, eq. (7.101), Fig. 7.10, p. 286 ("确实出现了负号和求迹。这个结论显然可以推广到任意 $n$ 的情形") · PS §4.7, p. 120, eq. (4.120) (the same for four vertices) · beyond the course as an example · written out here*

^ex-c6d-5-7

> [!example]- ★ Example §C6d.5.8: The Second-Order Vacuum Bubbles Keep Their 1/2!
> ![[ph-qft-c6d-5-8.svg]]
>
> In [[§C6d.1 Yukawa Theory#^mod-c6d-1-1|Model §C6d.1.1]] the fully contracted terms $13$ and $14$ of [[§C6d.5 Second Order#^thm-c6d-5-1|Theorem §C6d.5.1]] are the vacuum bubbles
>
> $$
> i\hat T^{(2)}_{13} = \frac{(-ig)^2}{2!}\int d^4x\,d^4y\;D_F(x - y)\,\bigl(-\operatorname{tr}[S_F(x - y)S_F(y - x)]\bigr) , \qquad i\hat T^{(2)}_{14} = \frac{(-ig)^2}{2!}\int d^4x\,d^4y\;D_F(x - y)\,\bigl(\operatorname{tr}S_F(0)\bigr)^2 :
> $$
>
> (a) a fermion loop through $x$ and $y$ with a scalar line across, (b) a tadpole loop at each vertex joined by the scalar line. Their $\frac{1}{2!}$ is **not** cancelled: $S = 2$ ([[§C6d.4 First Order#^thm-c6d-4-7|Theorem §C6d.4.7]], [[§C6d.5 Second Order#^thm-c6d-5-2|Theorem §C6d.5.2]], 3). They are $c$-numbers: between any states they multiply $\langle f|i\rangle$, part of the vacuum phase.
>
> **Step 1** (values). (a): $\overbracket{\hat\phi_x\hat\phi_y} = D_F(x - y)$ and the closed loop $-\operatorname{tr}[S_F(x - y)S_F(y - x)]$ ([[§C6d.4 First Order#^thm-c6d-4-6|Theorem §C6d.4.6]], $n = 2$; Step 1 of [[§C6d.5 Second Order#^ex-c6d-5-6|Example §C6d.5.6]]). (b): two tadpoles, each $-\operatorname{tr}S_F(0)$ ([[§C6d.4 First Order#^thm-c6d-4-1|Theorem §C6d.4.1]]), product $(\operatorname{tr}S_F(0))^2$; fermion pairs $(1, 2)$, $(3, 4)$, no crossing.
>
> **Step 2** (no partner under $x \leftrightarrow y$). (a): $\{\hat\phi_x\hat\phi_y, \hat\psi_x\hat{\bar\psi}_y, \hat\psi_y\hat{\bar\psi}_x\} \mapsto \{\hat\phi_y\hat\phi_x, \hat\psi_y\hat{\bar\psi}_x, \hat\psi_x\hat{\bar\psi}_y\}$, the same pattern; (b) likewise. With no particle to tell the vertices apart, the relabelling does not produce a second copy: the factor $\frac{1}{2!} = \frac1S$ remains (Yu (7.102)–(7.103)).
>
> **Step 3** (fate). No fields are left: $i\hat T^{(2)}_{13}$, $i\hat T^{(2)}_{14}$ are numbers times $\mathbb 1$, $\langle f|i\hat T^{(2)}_{13}|i\rangle = i\hat T^{(2)}_{13}\,\langle f|i\rangle$; vacuum bubbles are omitted from $i\mathcal M$ ([[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-6|Theorem §C6c.4.6]], 1).
>
> *Equivalently,* the scalar case is [[§C6c.4 First Order꞉ Enumerate, then Filter#^ex-c6c-4-3|Example §C6c.4.3]] (the first-order bubble, $S = 8$) and [[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^thm-c6c-5-2|Theorem §C6c.5.2]], 3 (the $\frac{1}{n!}$ survives only where no particle fixes the vertices).
>
> *Source: Yu §7.1.2, eqs. (7.72)–(7.73), (7.102)–(7.103), Fig. 7.11, pp. 286–287 ("$iT^{(2)}_{13}$ 和 $iT^{(2)}_{14}$ 中的 $1/2!$ 因子未被抵消，它们实际上对应于 7.3 节讨论的 Feynman 图对称性因子"; "微扰论中所有的气泡图只会贡献一个相位因子"); p. 275, footnote 1 · beyond the course · written out here*

^ex-c6d-5-8

> [!abstract]- Mathematical background
> Proved in CA; each line says what the physics above relies on.
>
> - [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]] — the two vertex integrals give the momentum deltas that fix the exchanged momentum.

> [!remark]- Connections
> - The two diagrams are the $t$- and $u$-channels of a scalar theory, now with spinor chains and a relative sign; for identical bosons the sign would be $+$ — [[§C6c.6 Feynman Rules for Amplitudes#^thm-c6c-6-4|Theorem §C6c.6.4]], [[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-7|Theorem §C6b.1.7]].
> - In the elastic region the exchanged momentum $q = p - p'$ is spacelike, $q^2 = t \le 0$, so the scalar is off its mass shell and the propagator has no pole — [[§C6c.6 Feynman Rules for Amplitudes#^thm-c6c-6-4|Theorem §C6c.6.4]], 2.
> - Its nonrelativistic limit for distinguishable fermions is the attractive Yukawa potential; for a fermion and an antifermion the spinor products and the contraction sign both flip, and the force stays attractive — [[§C6d.7 The Yukawa Potential|§C6d.7]].
> - $|\mathcal M|^2$ summed over spins needs traces of $\gamma$ matrices; the same process in QED is Møller scattering, a process of C8 (planned) — [[§C5a.14 Gamma-Matrix Technology|§C5a.14]].
> - The fourteen Wick terms play the role of the $764$ of $\phi^4$; only $\hat\phi\hat\phi$ and $\hat\psi\hat{\bar\psi}$ contract — [[§C6d.5 Second Order#^thm-c6d-5-1|Theorem §C6d.5.1]], [[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^thm-c6c-5-1|Theorem §C6c.5.1]].
> - In QED, $f\bar f \to f\bar f$ and $f\bar f \to \gamma\gamma$ are Bhabha scattering and pair annihilation, processes of C8 (planned) — [[§C6d.5 Second Order#^ex-c6d-5-1|Example §C6d.5.1]], [[§C6d.5 Second Order#^ex-c6d-5-3|Example §C6d.5.3]].
> - The loops on single external lines are removed by amputation; beyond lowest order they return as $\sqrt Z$ and the physical masses — [[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^thm-c6c-5-3|Theorem §C6c.5.3]], [[§C6c.1 Amplitudes from Correlation Functions#^cau-c6c-1-2|§C6c.1, Caution: The rule is stated at lowest order]].
