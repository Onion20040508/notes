---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C5a
section: C5a.11
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost]] · ↑ [[· C5a Spinors and the Dirac Equation]] · [[§C5a.12 Normalization and Spin Sums]] →

*Sources: the user's PHY 513 notes, Ch. 9 §9.3 (Principle "The positive-frequency solutions"; paragraph "The same ξ in every frame"), §9.4 (Derivation "Check: u(p) solves the Dirac equation in every frame"; Derivation "Normalization II: ūu", the row ū), §9.5 (Derivation "The v spinors: the four steps again"; Derivation "Normalizations of the v's", the row v̄; Caution "η means two things"), §9.6 (paragraph "The Dirac equation, from both sides"), and the paragraph "Correspondence with Yu" · PHY 513 Lecture 9 (Larsen), Parts A, B ("Practical Manipulations", "Normalization II", "Completeness for Dirac Spinors") and C · Peskin & Schroeder, An Introduction to Quantum Field Theory, §3.3, eqs. (3.50), (3.59), (3.61)–(3.62), p. 46 · Yu Zhao-Huan, 量子场论讲义, §5.4.2, eqs. (5.147)–(5.157), (5.165)–(5.191) · the user's pre-course notes, §5.4 · PHY 513, Problem Set 6, Problem 3(c)–(d) and comments (Larsen; the user's solutions).*

Which spinors does the boost of the rest-frame solutions give, and what are their Dirac conjugates? [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost|§C5a.10]] solved the Dirac equation in the rest frame ([[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^thm-c5a-10-3|Theorem §C5a.10.3]]) and built the boost $\Lambda_{1/2}(p)$ from rest to momentum $p$ ([[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^thm-c5a-10-8|Theorem §C5a.10.8]]) out of the Hermitian square roots $\sqrt{p\cdot\sigma}$, $\sqrt{p\cdot\bar\sigma}$ ([[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^def-c5a-10-5|Def. §C5a.10.5]]); the spinors are normalized as in [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^def-c5a-10-4|Def. §C5a.10.4]]. This section applies the boost: the positive-frequency spinors $u^s(p)$ and the negative-frequency spinors $v^s(p)$, then their Dirac conjugates $\bar u^s(p)$, $\bar v^s(p)$ ([[§C5a.2 The Dirac Form#^def-c5a-2-1|Def. §C5a.2.1]]) as rows in their own right, and the same spinors in the Dirac basis (Problem Set 6, Problem 3). Their normalizations and spin sums are [[§C5a.12 Normalization and Spin Sums|§C5a.12]]; the field built from them is [[§C5b.2 Mode Expansion and the Anticommutator Algebra|§C5b.2]].

**Setup.** Classical, free and on shell: the plane-wave solutions of the free Dirac equation ([[§C5a.7 The Dirac Equation and Its Lagrangian#^mod-c5a-7-3|Model §C5a.7.3]]), with $p^0 = +E_{\mathbf p}$; $u^s(p)$, $v^s(p)$ are c-number columns, normalized as in [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^def-c5a-10-4|Def. §C5a.10.4]] ($\bar u^ru^s = 2m\,\delta^{rs}$, $u^{r\dagger}u^s = 2E_{\mathbf p}\delta^{rs}$). Rest-frame statements need $m > 0$; the formulas for $u$, $v$ and their conjugates hold for every $m \ge 0$. The quantum field uses these same spinors as its mode functions ([[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-1|Theorem §C5b.2.1]]).

*Conventions* ([[Larsen PHY 513]]): as in [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost|§C5a.10]].

## The spinors u(p), v(p) and their Dirac conjugates

> [!theorem] Theorem §C5a.11.1: The Positive-Frequency Spinors u(p)
> For every $\mathbf p \in \mathbb R^3$ and $s = 1, 2$, with $p^0 = E_{\mathbf p}$ and a spin basis $\xi^s$ ([[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^def-c5a-10-3|Def. §C5a.10.3]]),
>
> $$
> u^s(p) = \begin{pmatrix}\sqrt{p\cdot\sigma}\;\xi^s\\ \sqrt{p\cdot\bar\sigma}\;\xi^s\end{pmatrix}, \qquad \psi(x) = u^s(p)\,e^{-ip\cdot x}\ \text{ solves the Dirac equation},\quad (\slashed{p} - m)\,u^s(p) = 0 .
> $$
>
> 1. For $m > 0$, $u^s(p) = \Lambda_{1/2}(p)\,u^s_0$ ([[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^thm-c5a-10-8|Theorem §C5a.10.8]]) with $u_0^s = \sqrt m(\xi^s, \xi^s)$ ([[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^thm-c5a-10-3|Theorem §C5a.10.3]]): the rest-frame solution boosted; $u^1$, $u^2$ span $\ker(\slashed{p} - m)$.
> 2. The formula holds for every direction of $\mathbf p$ and also for $m = 0$, where there is no rest frame and it is checked directly; then $u^1$, $u^2$ span $\ker\slashed{p}$.
>
> Names in other sources: [[§C5a.11 The Spinors u(p), v(p) and Their Dirac Conjugates#^cau-c5a-11-2|Caution: Names for the plane-wave spinors]].
>
> *Model:* [[§C5a.7 The Dirac Equation and Its Lagrangian#^mod-c5a-7-3|Model §C5a.7.3]]; *applies:* c-number spinors, on shell $p^0 = E_{\mathbf p}$, normalization of [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^def-c5a-10-4|Def. §C5a.10.4]]; part 1 for $m > 0$, part 2 every $m \ge 0$; exact.
>
> *Source: the user's PHY 513 notes, Ch. 9 §9.3 (Principle "The positive-frequency solutions"), §9.4 (Derivation "Check: u(p) solves the Dirac equation in every frame") · PHY 513 Lecture 9, Part A ("General Solution to Dirac Equation") and Part B ("Practical Manipulations") · PS §3.3, eqs. (3.50), (3.59) · Yu §5.4.2, eq. (5.157)*

^thm-c5a-11-1

> [!derivation]- Derivation
> **Step 1** (start at rest). By [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^thm-c5a-10-3|Theorem §C5a.10.3]] and [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^thm-c5a-10-1|Theorem §C5a.10.1]], $\psi_0(x) = u^s_0\,e^{-ik\cdot x}$ solves the Dirac equation, $k = (m, \mathbf 0)$.
>
> **Step 2** (covariance). If $\psi$ solves the Dirac equation, so does $\psi'(x) = \Lambda_{1/2}\,\psi(\Lambda^{-1}x)$ for every $\Lambda$ ([[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-1|Theorem §C5a.7.1]]). Take $\Lambda = L(p)$ of [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^thm-c5a-10-8|Theorem §C5a.10.8]]:
>
> $$
> \psi'(x) = \Lambda_{1/2}(p)\,u^s_0\;e^{-ik\cdot(L(p)^{-1}x)} .
> $$
>
> **Step 3** (the exponent). Lorentz transformations preserve the Minkowski product ([[§C1a.4 The Lorentz Group#^def-c1a-4-1|Def. §C1a.4.1]]): $k\cdot(L^{-1}x) = (Lk)\cdot(LL^{-1}x) = p\cdot x$, with $Lk = p$. So $\psi'(x) = \Lambda_{1/2}(p)u^s_0\,e^{-ip\cdot x}$: a positive-frequency plane wave of momentum $p$, and by Theorem §C5a.10.1 its column solves $(\slashed{p} - m)\Lambda_{1/2}(p)u^s_0 = 0$.
>
> **Step 4** (multiply the matrices). With [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^thm-c5a-10-8|Theorem §C5a.10.8]], block by block,
>
> $$
> \Lambda_{1/2}(p)\,u^s_0 = \begin{pmatrix}\sqrt{p\cdot\sigma/m}\;\sqrt m\,\xi^s\\ \sqrt{p\cdot\bar\sigma/m}\;\sqrt m\,\xi^s\end{pmatrix} = \begin{pmatrix}\sqrt{p\cdot\sigma}\;\xi^s\\ \sqrt{p\cdot\bar\sigma}\;\xi^s\end{pmatrix} = u^s(p) ,
> $$
>
> using $\sqrt{A/m} = \sqrt A/\sqrt m$ (Step 4 of [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^der-c5a-10-8|Derivation §C5a.10.8]]). ⚑ By-product: the $\sqrt m$ of the rest frame has cancelled the $1/\sqrt m$ of the boost; no $m$ is left, so the formula can be read at $m = 0$ → part 2, and the reason for the $\sqrt m$ convention → [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^def-c5a-10-4|Def. §C5a.10.4]].
>
> **Step 5** (they span). $\Lambda_{1/2}(p)$ is invertible (an exponential), so it maps the two independent $u^1_0$, $u^2_0$ to two independent $u^1(p)$, $u^2(p)$, which lie in the two-dimensional $\ker(\slashed{p} - m)$ ([[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^thm-c5a-10-2|Theorem §C5a.10.2]]) and therefore span it. Part 1.
>
> **What the derivation shows**
> - The construction is: solve where the problem is simplest (rest frame), then transport with the group; the same idea defines the one-particle states $|p, \sigma\rangle = U(L(p))|k, \sigma\rangle$ ([[§C3.6★ Particle States and the Little Group#^thm-c3-6-5|Theorem §C3.6.5]]).
> - Assumption $m > 0$ (rest frame, $1/\sqrt m$); the massless case needs the second route.
> - Used next: the Dirac conjugate $\bar u^s(p)$ ([[§C5a.11 The Spinors u(p), v(p) and Their Dirac Conjugates#^thm-c5a-11-2|Theorem §C5a.11.2]]); $v(p)$ by the same four steps ([[§C5a.11 The Spinors u(p), v(p) and Their Dirac Conjugates#^thm-c5a-11-3|Theorem §C5a.11.3]]); normalizations ([[§C5a.12 Normalization and Spin Sums|§C5a.12]]); mode expansion ([[§C5b.2 Mode Expansion and the Anticommutator Algebra|§C5b.2]]).

^der-c5a-11-1

*Uses:* [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^thm-c5a-10-1|Theorem §C5a.10.1]], [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^thm-c5a-10-2|Theorem §C5a.10.2]], [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^thm-c5a-10-3|Theorem §C5a.10.3]], [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^thm-c5a-10-8|Theorem §C5a.10.8]], [[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-1|Theorem §C5a.7.1]], [[§C1a.4 The Lorentz Group#^def-c1a-4-1|Def. §C1a.4.1]]

> [!derivation]- Derivation (second route: direct check with the square-root identities, valid for m ≥ 0)
> **Step 1** (the matrix times the column). With the chiral form of $\slashed{p}$ ([[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^def-c5a-10-2|Def. §C5a.10.2]]), block multiplication gives
>
> $$
> \slashed{p}\,u^s(p) = \begin{pmatrix}0 & p\cdot\sigma\\ p\cdot\bar\sigma & 0\end{pmatrix}\begin{pmatrix}\sqrt{p\cdot\sigma}\,\xi^s\\ \sqrt{p\cdot\bar\sigma}\,\xi^s\end{pmatrix} = \begin{pmatrix}(p\cdot\sigma)\sqrt{p\cdot\bar\sigma}\,\xi^s\\ (p\cdot\bar\sigma)\sqrt{p\cdot\sigma}\,\xi^s\end{pmatrix} .
> $$
>
> **Step 2** (split one factor into two roots). Write $p\cdot\sigma = \sqrt{p\cdot\sigma}\sqrt{p\cdot\sigma}$ in the upper entry and $p\cdot\bar\sigma = \sqrt{p\cdot\bar\sigma}\sqrt{p\cdot\bar\sigma}$ in the lower one ([[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^thm-c5a-10-7|Theorem §C5a.10.7]], 1), and pair the inner root with its neighbour:
>
> $$
> \slashed{p}\,u^s(p) = \begin{pmatrix}\sqrt{p\cdot\sigma}\,\bigl(\sqrt{p\cdot\sigma}\sqrt{p\cdot\bar\sigma}\bigr)\xi^s\\ \sqrt{p\cdot\bar\sigma}\,\bigl(\sqrt{p\cdot\bar\sigma}\sqrt{p\cdot\sigma}\bigr)\xi^s\end{pmatrix} = m\begin{pmatrix}\sqrt{p\cdot\sigma}\,\xi^s\\ \sqrt{p\cdot\bar\sigma}\,\xi^s\end{pmatrix} = m\,u^s(p) ,
> $$
>
> by Theorem §C5a.10.7, 3. So $(\slashed{p} - m)u^s(p) = 0$; with Theorem §C5a.10.1, $u^s(p)e^{-ip\cdot x}$ solves the Dirac equation.
>
> **Step 3** ($m = 0$: they span). No step divided by $m$, so Steps 1–2 hold at $m = 0$. There $\sqrt{p\cdot\sigma} = \sqrt{2|\mathbf p|}\,\Pi_-$ and $\sqrt{p\cdot\bar\sigma} = \sqrt{2|\mathbf p|}\,\Pi_+$ ([[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^def-c5a-10-5|Def. §C5a.10.5]] with $E = |\mathbf p|$), so $u(\xi) = \sqrt{2|\mathbf p|}(\Pi_-\xi, \Pi_+\xi)$. The map $\xi \mapsto (\Pi_-\xi, \Pi_+\xi)$ is injective (if both parts vanish, $\xi = \Pi_-\xi + \Pi_+\xi = 0$), so $u^1$, $u^2$ are independent and span the two-dimensional $\ker\slashed{p}$ ([[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^thm-c5a-10-2|Theorem §C5a.10.2]], 3). Part 2.
>
> **What the derivation shows**
> - Had the formula been given at the outset, this would be the proof; the boost is how it was found.
> - It never uses the direction of $\mathbf p$ or $m > 0$, which is why the formula is stated for all $\mathbf p$ and $m \ge 0$.

^der-c5a-11-1b

*Uses:* [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^def-c5a-10-2|Def. §C5a.10.2]], [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^def-c5a-10-5|Def. §C5a.10.5]], [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^thm-c5a-10-7|Theorem §C5a.10.7]], [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^thm-c5a-10-1|Theorem §C5a.10.1]], [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^thm-c5a-10-2|Theorem §C5a.10.2]]

> [!derivation]- Derivation (third route: solving for the lower half, Yu)
> **Step 1** (two-component equations). Write $u = (f, g)$. With the chiral form of $\slashed{p}$, $(\slashed{p} - m)u = \bigl((p\cdot\sigma)g - mf,\ (p\cdot\bar\sigma)f - mg\bigr) = 0$, Yu's (5.149)–(5.150).
>
> **Step 2** (solve the second). For $m > 0$, $g = \frac{p\cdot\bar\sigma}m\,f$ (5.151).
>
> **Step 3** (the first is then automatic). Substituting, $(p\cdot\sigma)g - mf = \frac{(p\cdot\sigma)(p\cdot\bar\sigma)}m f - mf = \frac{m^2}m f - mf = 0$ by [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^thm-c5a-10-7|Theorem §C5a.10.7]], 2 (Yu's (5.155) derives the same product from $\sigma^\mu\bar\sigma^\nu + \sigma^\nu\bar\sigma^\mu = 2g^{\mu\nu}$). So every $f \in \mathbb C^2$ gives a solution $u = (f, \frac{p\cdot\bar\sigma}m f)$ (5.157): two independent ones.
>
> **Step 4** (match to the boost form). Choose $f = \sqrt{p\cdot\sigma}\,\xi$. Then $g = \frac1m(p\cdot\bar\sigma)\sqrt{p\cdot\sigma}\,\xi = \frac1m\sqrt{p\cdot\bar\sigma}\bigl(\sqrt{p\cdot\bar\sigma}\sqrt{p\cdot\sigma}\bigr)\xi = \sqrt{p\cdot\bar\sigma}\,\xi$ (Theorem §C5a.10.7, 1 and 3): $u = u(p)$ of the statement. Yu fixes $f$ instead by the normalization and a helicity choice ([[§C5a.13 Helicity Spinors and the Massless Limit#^thm-c5a-13-2|Theorem §C5a.13.2]]).
>
> *Source: Yu §5.4.2, eqs. (5.147)–(5.157) · the user's pre-course notes, §5.4 · the user's PHY 513 notes, Ch. 9, "Correspondence with Yu"*

*Uses:* [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^def-c5a-10-2|Def. §C5a.10.2]], [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^thm-c5a-10-7|Theorem §C5a.10.7]]

> [!theorem] Theorem §C5a.11.2: The Dirac Conjugate of u(p)
> For the spinors $u^s(p)$ of [[§C5a.11 The Spinors u(p), v(p) and Their Dirac Conjugates#^thm-c5a-11-1|Theorem §C5a.11.1]], every $\mathbf p$ and $m \ge 0$, the Dirac conjugate ([[§C5a.2 The Dirac Form#^def-c5a-2-1|Def. §C5a.2.1]]) is the row
>
> $$
> \bar u^s(p) \equiv u^{s\dagger}(p)\,\gamma^0 = \bigl(\xi^{s\dagger}\sqrt{p\cdot\bar\sigma},\ \xi^{s\dagger}\sqrt{p\cdot\sigma}\bigr), \qquad \bar u^s(p)\,(\slashed{p} - m) = 0 ,
> $$
>
> with the two Hermitian roots of [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^def-c5a-10-5|Def. §C5a.10.5]] in exchanged places relative to the column $u^s(p)$.
> 1. $\bar u^s(p)$ is a $1\times4$ row, the functional $h_D(u^s(p), \cdot\,)$ of the Dirac form ([[§C5a.2 The Dirac Form#^def-c5a-2-1|Def. §C5a.2.1]]): $\bar u^s(p)\,w$ is a number for every column $w$, e.g. $\bar u^r(p)\,u^s(p) = 2m\,\delta^{rs}$ ([[§C5a.12 Normalization and Spin Sums#^thm-c5a-12-2|Theorem §C5a.12.2]]).
> 2. The Dirac equation acts from the right: $\bar u^s(p)\,\slashed{p} = m\,\bar u^s(p)$, with $\slashed{p}$ of [[§C5a.7 The Dirac Equation and Its Lagrangian#^def-c5a-7-2|Def. §C5a.7.2]].
> 3. At rest, $p = (m, \mathbf 0)$ with $m > 0$: $\bar u^s_0 = \sqrt m\,(\xi^{s\dagger}, \xi^{s\dagger}) = u_0^{s\dagger}$.
>
> *Model:* [[§C5a.7 The Dirac Equation and Its Lagrangian#^mod-c5a-7-3|Model §C5a.7.3]]; *applies:* c-number spinors, on shell, normalization of [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^def-c5a-10-4|Def. §C5a.10.4]], every $m \ge 0$ (part 3: $m > 0$).
>
> *Source: PHY 513 Lecture 9, Part B ("Normalization II": $\bar u(p) = u^\dagger(p)\gamma^0$; "Completeness for Dirac Spinors": the row $(\xi^{s\dagger}\sqrt{p\cdot\bar\sigma}, \xi^{s\dagger}\sqrt{p\cdot\sigma})$) · the user's PHY 513 notes, Ch. 9 §9.4 (Derivation "Normalization II: ūu": the Dirac conjugate "exchanges the two halves of the row"), §9.6 (Derivation "Proof of the Gordon identity", paragraph "The Dirac equation, from both sides") · PS §3.3, eqs. (3.55)–(3.56) and the row in the spin sum, p. 48 · Yu §5.4.2, eq. (5.205) (helicity basis) · the user's pre-course notes, §5.4 (note "Checking the spin sums": "$\gamma^0$ swaps the blocks of $u^\dagger$") · the rest-frame check and the third route written here*

^thm-c5a-11-2

> [!derivation]- Derivation
> **Step 1** (the roots pass through the dagger). $p\cdot\sigma = E_{\mathbf p}\mathbb 1 - p^i\sigma^i$ and $p\cdot\bar\sigma = E_{\mathbf p}\mathbb 1 + p^i\sigma^i$ ([[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^def-c5a-10-2|Def. §C5a.10.2]]) have real coefficients $E_{\mathbf p}$, $p^i$ and Hermitian $\sigma^i$ ([[§B6.1 Spin One-Half and the Pauli Matrices#^thm-b6-1-4|QM Theorem §B6.1.4]]), so they are Hermitian; their eigenvalues $E_{\mathbf p} \mp |\mathbf p| \ge 0$ make them positive operators ([[§25 Positive Operators#^ladr-7-38|LADR Thm. 7.38]], (b) ⇒ (a)). Their roots are the positive square roots ([[§25 Positive Operators#^ladr-7-39|LADR 7.39]]), and a positive operator is self-adjoint ([[§25 Positive Operators#^ladr-7-34|LADR Def. 7.34]]). Concretely, the spectral form of [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^def-c5a-10-5|Def. §C5a.10.5]] is a combination of the Hermitian projectors $\Pi_\pm$ with the real coefficients $\sqrt{E_{\mathbf p} \mp |\mathbf p|}$ (and $\sqrt m\,\mathbb 1$ at $\mathbf p = 0$). With $(AB)^\dagger = B^\dagger A^\dagger$,
>
> $$
> \bigl(\sqrt{p\cdot\sigma}\,\xi^s\bigr)^\dagger = \xi^{s\dagger}\bigl(\sqrt{p\cdot\sigma}\bigr)^\dagger = \xi^{s\dagger}\sqrt{p\cdot\sigma}, \qquad \bigl(\sqrt{p\cdot\bar\sigma}\,\xi^s\bigr)^\dagger = \xi^{s\dagger}\bigl(\sqrt{p\cdot\bar\sigma}\bigr)^\dagger = \xi^{s\dagger}\sqrt{p\cdot\bar\sigma} .
> $$
>
> ⚑ By-product: a root moves from the left of $\xi^s$ to the right of $\xi^{s\dagger}$ unchanged; without Hermiticity it would become $(\sqrt{p\cdot\sigma})^\dagger$, and the identities of [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^thm-c5a-10-7|Theorem §C5a.10.7]] would not apply → [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^def-c5a-10-5|Def. §C5a.10.5]].
>
> **Step 2** (dagger of the column, block by block). The Hermitian conjugate of a column transposes it into a row and conjugates each entry. For a column with two-component halves $a$, $b$, the entries of $a$ fill the first two places of the row and those of $b$ the last two, so $\begin{pmatrix}a\\ b\end{pmatrix}^\dagger = (a^\dagger,\ b^\dagger)$. With $a = \sqrt{p\cdot\sigma}\,\xi^s$, $b = \sqrt{p\cdot\bar\sigma}\,\xi^s$ ([[§C5a.11 The Spinors u(p), v(p) and Their Dirac Conjugates#^thm-c5a-11-1|Theorem §C5a.11.1]]) and Step 1,
>
> $$
> u^{s\dagger}(p) = \bigl(\xi^{s\dagger}\sqrt{p\cdot\sigma},\ \xi^{s\dagger}\sqrt{p\cdot\bar\sigma}\bigr) .
> $$
>
> **Step 3** ($\gamma^0$ swaps the halves). In the chiral basis $\gamma^0 = \begin{pmatrix}0 & \mathbb 1\\ \mathbb 1 & 0\end{pmatrix}$ ([[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-4|Def. §C5a.1.4]]). A row times a block matrix is $(c, d)\begin{pmatrix}A & B\\ C & D\end{pmatrix} = (cA + dC,\ cB + dD)$; here $(a^\dagger, b^\dagger)\gamma^0 = (a^\dagger\cdot0 + b^\dagger\mathbb 1,\ a^\dagger\mathbb 1 + b^\dagger\cdot0) = (b^\dagger, a^\dagger)$. Hence
>
> $$
> \bar u^s(p) = u^{s\dagger}(p)\,\gamma^0 = \bigl(\xi^{s\dagger}\sqrt{p\cdot\bar\sigma},\ \xi^{s\dagger}\sqrt{p\cdot\sigma}\bigr) .
> $$
>
> It is $1\times4$ (two $1\times2$ blocks), so its product with a column $w = (w_1, w_2)$ is the number $\xi^{s\dagger}\sqrt{p\cdot\bar\sigma}\,w_1 + \xi^{s\dagger}\sqrt{p\cdot\sigma}\,w_2$, the value $h_D(u^s(p), w) = u^{s\dagger}\gamma^0w$ of the Dirac form. The formula and part 1.
>
> **Step 4** (the conjugate equation, directly). By the rule of Step 3 with the chiral form $\slashed{p} = \begin{pmatrix}0 & p\cdot\sigma\\ p\cdot\bar\sigma & 0\end{pmatrix}$ ([[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^def-c5a-10-2|Def. §C5a.10.2]]), $(c, d)\,\slashed{p} = \bigl(d\,(p\cdot\bar\sigma),\ c\,(p\cdot\sigma)\bigr)$. With $c = \xi^{s\dagger}\sqrt{p\cdot\bar\sigma}$ and $d = \xi^{s\dagger}\sqrt{p\cdot\sigma}$,
>
> $$
> \bar u^s(p)\,\slashed{p} = \Bigl(\xi^{s\dagger}\sqrt{p\cdot\sigma}\,(p\cdot\bar\sigma),\ \ \xi^{s\dagger}\sqrt{p\cdot\bar\sigma}\,(p\cdot\sigma)\Bigr) .
> $$
>
> Split each unrooted factor into two roots, $p\cdot\bar\sigma = \sqrt{p\cdot\bar\sigma}\sqrt{p\cdot\bar\sigma}$ and $p\cdot\sigma = \sqrt{p\cdot\sigma}\sqrt{p\cdot\sigma}$ ([[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^thm-c5a-10-7|Theorem §C5a.10.7]], 1), and pair the first root with its left neighbour:
>
> $$
> \sqrt{p\cdot\sigma}\,(p\cdot\bar\sigma) = \bigl(\sqrt{p\cdot\sigma}\sqrt{p\cdot\bar\sigma}\bigr)\sqrt{p\cdot\bar\sigma} = m\sqrt{p\cdot\bar\sigma}, \qquad \sqrt{p\cdot\bar\sigma}\,(p\cdot\sigma) = \bigl(\sqrt{p\cdot\bar\sigma}\sqrt{p\cdot\sigma}\bigr)\sqrt{p\cdot\sigma} = m\sqrt{p\cdot\sigma}
> $$
>
> by Theorem §C5a.10.7, 3. So $\bar u^s(p)\,\slashed{p} = m\bigl(\xi^{s\dagger}\sqrt{p\cdot\bar\sigma},\ \xi^{s\dagger}\sqrt{p\cdot\sigma}\bigr) = m\,\bar u^s(p)$. The $m$ in $\slashed{p} - m$ stands for $m\,\mathbb 1_4$, and a row times $\mathbb 1_4$ is the row, so $\bar u^s(p)(\slashed{p} - m) = m\,\bar u^s(p) - m\,\bar u^s(p) = 0$. No step divides by $m$: valid for $m \ge 0$. Part 2.
>
> **Step 5** (rest frame). At $p = (m, \mathbf 0)$, $m > 0$: $p\cdot\sigma = p\cdot\bar\sigma = m\,\mathbb 1$ (Def. §C5a.10.2 with $\mathbf p = 0$) and both roots are $\sqrt m\,\mathbb 1$ (Def. §C5a.10.5), so Step 3 gives $\bar u^s_0 = \sqrt m\,(\xi^{s\dagger}, \xi^{s\dagger})$. Directly from $u_0^s = \sqrt m(\xi^s, \xi^s)$ ([[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^thm-c5a-10-3|Theorem §C5a.10.3]]): $u_0^{s\dagger} = \sqrt m(\xi^{s\dagger}, \xi^{s\dagger})$ ($\sqrt m$ is real), and the swap of two equal halves changes nothing, so $\bar u_0^s = u_0^{s\dagger}$. Check of part 2 at rest, with $\slashed{p} - m = m\begin{pmatrix}-\mathbb 1 & \mathbb 1\\ \mathbb 1 & -\mathbb 1\end{pmatrix}$ (Step 1 of [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^der-c5a-10-3|Derivation §C5a.10.3]]) and the row rule of Step 3:
>
> $$
> \bar u^s_0\,(\slashed{p} - m) = m\sqrt m\,\bigl(-\xi^{s\dagger} + \xi^{s\dagger},\ \ \xi^{s\dagger} - \xi^{s\dagger}\bigr) = (0,\ 0) .
> $$
>
> Part 3. ⚑ By-product: at rest $\bar u_0 = u_0^\dagger$, so $\bar u_0u_0 = u_0^\dagger u_0 = 2m\,\xi^\dagger\xi$: the invariant normalization and the frame-dependent one agree in the rest frame, where $2E_{\mathbf p} = 2m$ → [[§C5a.12 Normalization and Spin Sums#^thm-c5a-12-1|Theorem §C5a.12.1]], [[§C5a.12 Normalization and Spin Sums#^thm-c5a-12-2|Theorem §C5a.12.2]].
>
> **What the derivation shows**
> - The bar does two things: the dagger reverses the order (each Hermitian root moves to the right of $\xi^{s\dagger}$), and $\gamma^0$ exchanges the halves. So in every product $\bar u(\cdots)u$ a $\sqrt{p\cdot\bar\sigma}$ meets a $\sqrt{p\cdot\sigma}$, which Theorem §C5a.10.7, 3 turns into $m$; in $u^\dagger u$ equal roots meet and give $p\cdot\sigma + p\cdot\bar\sigma = 2E_{\mathbf p}$.
> - The row is a plane-wave solution of the conjugate Dirac equation $i\,\partial_\mu\bar\psi\,\gamma^\mu + m\bar\psi = 0$ ([[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-6|Theorem §C5a.7.6]], 2): for $\bar\psi = \bar u^s(p)\,e^{+ip\cdot x}$, $i\partial_\mu e^{ip\cdot x} = -p_\mu e^{ip\cdot x}$, and the equation becomes $-\bar u^s(p)(\slashed{p} - m)\,e^{ip\cdot x} = 0$, which is part 2. The conjugate of a positive-frequency wave carries $e^{+ip\cdot x}$.
> - Assumptions: $p$ real, on the forward mass shell (for Hermitian positive roots); the chiral basis for the explicit row. The equation $\bar u(\slashed{p} - m) = 0$ needs neither the row nor $m > 0$ (second route).
> - Used in: $\bar uu = 2m$, $\bar uv = 0$ and the spin sum $\sum_s u^s\bar u^s = \slashed{p} + m$ ([[§C5a.12 Normalization and Spin Sums#^thm-c5a-12-2|Theorem §C5a.12.2]], [[§C5a.12 Normalization and Spin Sums#^thm-c5a-12-5|Theorem §C5a.12.5]], [[§C5a.12 Normalization and Spin Sums#^thm-c5a-12-7|Theorem §C5a.12.7]]); the conjugate field ([[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-2|Theorem §C5b.2.2]]); the Gordon identity ([[§C5a.14 Gamma-Matrix Technology#^thm-c5a-14-9|Theorem §C5a.14.9]]).

^der-c5a-11-2

*Uses:* [[§C5a.2 The Dirac Form#^def-c5a-2-1|Def. §C5a.2.1]], [[§C5a.11 The Spinors u(p), v(p) and Their Dirac Conjugates#^thm-c5a-11-1|Theorem §C5a.11.1]], [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^def-c5a-10-2|Def. §C5a.10.2]], [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^def-c5a-10-5|Def. §C5a.10.5]], [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^thm-c5a-10-7|Theorem §C5a.10.7]], [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^thm-c5a-10-3|Theorem §C5a.10.3]], [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-4|Def. §C5a.1.4]], [[§B6.1 Spin One-Half and the Pauli Matrices#^thm-b6-1-4|QM Theorem §B6.1.4]], [[§25 Positive Operators#^ladr-7-34|LADR Def. 7.34]], [[§25 Positive Operators#^ladr-7-38|LADR Thm. 7.38]], [[§25 Positive Operators#^ladr-7-39|LADR 7.39]]

> [!derivation]- Derivation (second route: the Hermitian conjugate of the Dirac equation)
> This route uses only $(\slashed{p} - m)\,u^s(p) = 0$ ([[§C5a.11 The Spinors u(p), v(p) and Their Dirac Conjugates#^thm-c5a-11-1|Theorem §C5a.11.1]]) and the Hermiticity of the $\gamma$'s, not the explicit column.
>
> **Step 1** (dagger of the equation). For a matrix $M$ and a column $w$, $(Mw)^\dagger = w^\dagger M^\dagger$, and the dagger of the zero column is the zero row. So $(\slashed{p} - m)\,u^s = 0$ gives $u^{s\dagger}(\slashed{p} - m)^\dagger = 0$.
>
> **Step 2** (dagger of the matrix). The $p_\mu$ and $m$ are real numbers and $\mathbb 1^\dagger = \mathbb 1$, so $(p_\mu\gamma^\mu - m\,\mathbb 1)^\dagger = p_\mu\gamma^{\mu\dagger} - m\,\mathbb 1$. Insert $\gamma^{\mu\dagger} = \gamma^0\gamma^\mu\gamma^0$ ([[§C5a.2 The Dirac Form#^thm-c5a-2-1|Theorem §C5a.2.1]]) and $\mathbb 1 = \gamma^0\gamma^0$ ([[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-1|Theorem §C5a.1.1]]):
>
> $$
> (\slashed{p} - m)^\dagger = \gamma^0\,(p_\mu\gamma^\mu)\,\gamma^0 - m\,\gamma^0\gamma^0 = \gamma^0\,(\slashed{p} - m)\,\gamma^0 .
> $$
>
> **Step 3** (multiply by $\gamma^0$ on the right). Step 1 becomes $u^{s\dagger}\gamma^0(\slashed{p} - m)\gamma^0 = 0$. Multiplying on the right by $\gamma^0$ and using $(\gamma^0)^2 = \mathbb 1$ gives $u^{s\dagger}\gamma^0(\slashed{p} - m) = 0$, i.e. $\bar u^s(p)\,(\slashed{p} - m) = 0$ by the definition of the bar ([[§C5a.2 The Dirac Form#^def-c5a-2-1|Def. §C5a.2.1]]).
>
> **What the derivation shows**
> - In the language of the Dirac form this is $\overline{\gamma^\mu\chi} = \bar\chi\gamma^\mu$, the self-adjointness of the Dirac maps ([[§C5a.2 The Dirac Form#^thm-c5a-2-2|Theorem §C5a.2.2]], 1): the bar of $(\slashed{p} - m)u$ is $\bar u(\slashed{p} - m)$, because the bar is conjugate-linear and the coefficients $p_\mu$, $m$ are real.
> - It holds for every solution of $(\slashed{p} - m)w = 0$, in every Hermitian basis, $\gamma^{\mu\dagger} = \gamma^0\gamma^\mu\gamma^0$ ([[§C5a.2 The Dirac Form#^thm-c5a-2-1|Theorem §C5a.2.1]]), and for $m \ge 0$.
> - Assumption: $p_\mu$ and $m$ real (Step 2); for a complex momentum the conjugate equation would carry $p_\mu^{\ast}$.
>
> *Source: the user's PHY 513 notes, Ch. 9 §9.6 (Derivation "Proof of the Gordon identity", paragraph "The Dirac equation, from both sides")*

^der-c5a-11-2b

*Uses:* [[§C5a.11 The Spinors u(p), v(p) and Their Dirac Conjugates#^thm-c5a-11-1|Theorem §C5a.11.1]], [[§C5a.2 The Dirac Form#^thm-c5a-2-1|Theorem §C5a.2.1]], [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-1|Theorem §C5a.1.1]], [[§C5a.2 The Dirac Form#^def-c5a-2-1|Def. §C5a.2.1]]

> [!derivation]- Derivation (third route: the bar carries the inverse boost, m > 0)
> **Step 1** (the bar of a boosted column). $u^s(p) = \Lambda_{1/2}(p)\,u_0^s$ ([[§C5a.11 The Spinors u(p), v(p) and Their Dirac Conjugates#^thm-c5a-11-1|Theorem §C5a.11.1]], 1). With $\Lambda_{1/2}^\dagger\gamma^0 = \gamma^0\Lambda_{1/2}^{-1}$ ([[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-4|Theorem §C5a.3.4]], 2),
>
> $$
> \bar u^s(p) = u_0^{s\dagger}\,\Lambda_{1/2}(p)^\dagger\,\gamma^0 = u_0^{s\dagger}\,\gamma^0\,\Lambda_{1/2}(p)^{-1} = \bar u_0^s\,\Lambda_{1/2}(p)^{-1} ,
> $$
>
> the plane-wave case of [[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-1|Theorem §C5a.6.1]].
>
> **Step 2** (the inverse boost). $\Lambda_{1/2}(p) = \operatorname{diag}\bigl(\sqrt{p\cdot\sigma/m}, \sqrt{p\cdot\bar\sigma/m}\bigr)$ ([[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^thm-c5a-10-8|Theorem §C5a.10.8]]). By [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^thm-c5a-10-7|Theorem §C5a.10.7]], 3, and $\sqrt{A/m} = \sqrt A/\sqrt m$ (Step 4 of [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^der-c5a-10-8|Derivation §C5a.10.8]]), $\sqrt{p\cdot\sigma/m}\,\sqrt{p\cdot\bar\sigma/m} = \frac1m\sqrt{p\cdot\sigma}\sqrt{p\cdot\bar\sigma} = \mathbb 1$, and the same in the other order: each block's inverse is the other root. The inverse of a block-diagonal matrix is block-diagonal with the inverse blocks, so $\Lambda_{1/2}(p)^{-1} = \operatorname{diag}\bigl(\sqrt{p\cdot\bar\sigma/m}, \sqrt{p\cdot\sigma/m}\bigr)$.
>
> **Step 3** (multiply). With $\bar u_0^s = \sqrt m(\xi^{s\dagger}, \xi^{s\dagger})$ ([[§C5a.11 The Spinors u(p), v(p) and Their Dirac Conjugates#^der-c5a-11-2|Derivation §C5a.11.2]], Step 5), block by block,
>
> $$
> \bar u^s(p) = \sqrt m\,\bigl(\xi^{s\dagger},\ \xi^{s\dagger}\bigr)\begin{pmatrix}\sqrt{p\cdot\bar\sigma}/\sqrt m & 0\\ 0 & \sqrt{p\cdot\sigma}/\sqrt m\end{pmatrix} = \bigl(\xi^{s\dagger}\sqrt{p\cdot\bar\sigma},\ \xi^{s\dagger}\sqrt{p\cdot\sigma}\bigr) ,
> $$
>
> the formula of the statement.
>
> **What the derivation shows**
> - ⚑ By-product: $\Lambda_{1/2}(p)^{-1}$ is the spinor boost to the reversed momentum $\tilde p = (E_{\mathbf p}, -\mathbf p)$. By Def. §C5a.10.2, $\tilde p\cdot\sigma = E_{\mathbf p} + \mathbf p\cdot\boldsymbol\sigma = p\cdot\bar\sigma$ and $\tilde p\cdot\bar\sigma = p\cdot\sigma$, so $\Lambda_{1/2}(p)^{-1} = \Lambda_{1/2}(\tilde p)$: the spinor form of $L(p)^{-1} = L(\tilde p)$ for the pure boosts of Theorem §C5a.10.8 (rapidity $-\eta$ along $\hat{\mathbf p}$ is rapidity $\eta$ along $-\hat{\mathbf p}$).
> - So the exchange of the roots in $\bar u^s(p) = \bar u^s_0\,\Lambda_{1/2}(\tilde p)$ is the transformation law of the bar (inverse matrix, from the right), $\sqrt{p\cdot\bar\sigma} = \sqrt{\tilde p\cdot\sigma}$, not an accident of the chiral $\gamma^0$.

^der-c5a-11-2c

*Uses:* [[§C5a.11 The Spinors u(p), v(p) and Their Dirac Conjugates#^thm-c5a-11-1|Theorem §C5a.11.1]], [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^thm-c5a-10-8|Theorem §C5a.10.8]], [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^thm-c5a-10-7|Theorem §C5a.10.7]], [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-4|Theorem §C5a.3.4]], [[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-1|Theorem §C5a.6.1]]

> [!remark] Remark: The same ξ in every frame
> The $\xi^s$ in $u^s(p)$ are the ones chosen in the rest frame: the boost multiplies each half of $u_0$ by a matrix from the left, so the rest-frame $\xi^s$ is what stands to the right of $\sqrt{p\cdot\sigma}$ and $\sqrt{p\cdot\bar\sigma}$ in every frame. In particular $\xi = (1, 0)$ means "spin up along $z$ *in the rest frame*", not in the frame where the particle moves. The standard basis is one choice; a basis of spin along $\mathbf p$ is often better, and in it no matrix square root is ever needed ([[§C5a.13 Helicity Spinors and the Massless Limit#^thm-c5a-13-2|Theorem §C5a.13.2]]).
>
> *Source: the user's PHY 513 notes, Ch. 9 §9.3 (paragraph "The same ξ in every frame") · PS §3.3, p. 46*

^rem-c5a-11-1

> [!theorem] Theorem §C5a.11.3: The Negative-Frequency Spinors v(p)
> For every $\mathbf p$ and $s = 1, 2$, with a spin basis $\eta^s$ ([[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^def-c5a-10-3|Def. §C5a.10.3]]; from Lecture 12 on $\eta^s = \xi^{-s}$, [[§C9.6 Charge Conjugation on Oscillators and Spinors#^def-c9-6-5|Def. §C9.6.5]]),
>
> $$
> v^s(p) = \begin{pmatrix}\sqrt{p\cdot\sigma}\;\eta^s\\ -\sqrt{p\cdot\bar\sigma}\;\eta^s\end{pmatrix}, \qquad \psi(x) = v^s(p)\,e^{+ip\cdot x}\ \text{ solves the Dirac equation},\quad (\slashed{p} + m)\,v^s(p) = 0 .
> $$
>
> For $m > 0$, $v^s(p) = \Lambda_{1/2}(p)\,v^s_0$ ([[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^thm-c5a-10-8|Theorem §C5a.10.8]]) with $v^s_0 = \sqrt m(\eta^s, -\eta^s)$ ([[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^thm-c5a-10-3|Theorem §C5a.10.3]]), and $v^1$, $v^2$ span $\ker(\slashed{p} + m)$; the $u$'s and $v$'s together are the four eigenvectors of $\slashed{p}$. The formula also holds for $m = 0$, where $v^1, v^2$ span the same $\ker\slashed{p}$ as $u^1, u^2$.
>
> *Model:* [[§C5a.7 The Dirac Equation and Its Lagrangian#^mod-c5a-7-3|Model §C5a.7.3]]; *applies:* c-number spinors, on shell $p^0 = E_{\mathbf p}$, normalization of [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^def-c5a-10-4|Def. §C5a.10.4]], every $m \ge 0$ (the boost from rest: $m > 0$); exact.
>
> *Source: the user's PHY 513 notes, Ch. 9 §9.5 (Derivation "The v spinors: the four steps again") · PHY 513 Lecture 9, Part C (Steps 1–4) · PS §3.3, eqs. (3.61)–(3.62) · Yu §5.4.2, eqs. (5.182)–(5.191)*

^thm-c5a-11-3

> [!derivation]- Derivation
> The four steps of Lecture 9 again; differences from the $u$ case are marked.
>
> **Step 1** (ansatz). $\psi = v(p)e^{+ip\cdot x}$ with $p^0 = +E_{\mathbf p}$ ([[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^def-c5a-10-1|Def. §C5a.10.1]]). *Difference:* the sign of the exponent.
>
> **Step 2** (eigenvalue problem). [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^thm-c5a-10-1|Theorem §C5a.10.1]], 2: $(\slashed{p} + m)v = 0$, the eigenvalue $-m$ of $\slashed{p}$. *Difference:* $-m$ instead of $+m$, from $i\cdot(+i) = -1$.
>
> **Step 3** (rest frame). [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^thm-c5a-10-3|Theorem §C5a.10.3]]: $v_0^s = \sqrt m(\eta^s, -\eta^s)$. *Difference:* the lower half is minus the upper half.
>
> **Step 4** (boost). As in Steps 2–3 of [[§C5a.11 The Spinors u(p), v(p) and Their Dirac Conjugates#^der-c5a-11-1|Derivation §C5a.11.1]], $\Lambda_{1/2}(p)v_0^s\,e^{+ik\cdot(L^{-1}x)} = \Lambda_{1/2}(p)v_0^s\,e^{+ip\cdot x}$ is a solution, the Minkowski product being invariant whatever the sign in front of it. The boost acts on each half separately and the minus sign rides along:
>
> $$
> \Lambda_{1/2}(p)\,v_0^s = \begin{pmatrix}\sqrt{p\cdot\sigma/m}\;\sqrt m\,\eta^s\\ \sqrt{p\cdot\bar\sigma/m}\;(-\sqrt m\,\eta^s)\end{pmatrix} = \begin{pmatrix}\sqrt{p\cdot\sigma}\;\eta^s\\ -\sqrt{p\cdot\bar\sigma}\;\eta^s\end{pmatrix} = v^s(p) .
> $$
>
> They span $\ker(\slashed{p} + m)$ by the argument of Step 5 there, with [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^thm-c5a-10-2|Theorem §C5a.10.2]], 2.
>
> **Step 5** (direct check, $m \ge 0$). As in [[§C5a.11 The Spinors u(p), v(p) and Their Dirac Conjugates#^der-c5a-11-1b|Derivation §C5a.11.1 (second route)]], with the sign of the lower entry carried:
>
> $$
> \slashed{p}\,v^s = \begin{pmatrix}(p\cdot\sigma)\bigl(-\sqrt{p\cdot\bar\sigma}\bigr)\eta^s\\ (p\cdot\bar\sigma)\sqrt{p\cdot\sigma}\,\eta^s\end{pmatrix} = \begin{pmatrix}-\sqrt{p\cdot\sigma}\bigl(\sqrt{p\cdot\sigma}\sqrt{p\cdot\bar\sigma}\bigr)\eta^s\\ \sqrt{p\cdot\bar\sigma}\bigl(\sqrt{p\cdot\bar\sigma}\sqrt{p\cdot\sigma}\bigr)\eta^s\end{pmatrix} = -m\begin{pmatrix}\sqrt{p\cdot\sigma}\,\eta^s\\ -\sqrt{p\cdot\bar\sigma}\,\eta^s\end{pmatrix} = -m\,v^s ,
> $$
>
> by [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^thm-c5a-10-7|Theorem §C5a.10.7]]. At $m = 0$, $v(\eta) = \sqrt{2|\mathbf p|}(\Pi_-\eta, -\Pi_+\eta)$; as $\eta$ ranges over $\mathbb C^2$ this is the same space $\{(\Pi_-a, \Pi_+b)\}$ as the $u$'s ([[§C5a.11 The Spinors u(p), v(p) and Their Dirac Conjugates#^der-c5a-11-1b|Derivation §C5a.11.1 (second route)]], Step 3), since $-\Pi_+\eta$ runs over the whole range of $\Pi_+$. ⚑ By-product: at $m = 0$ "$u$" and "$v$" are the same columns; only the exponent tells a positive- from a negative-frequency solution → [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^thm-c5a-10-2|Theorem §C5a.10.2]], 3.
>
> **What the derivation shows**
> - Every difference between $v$ and $u$ is one sign, traced to the exponent; the boost matrix is the same.
> - With $u^1, u^2$ (eigenvalue $+m$) the $v^1, v^2$ (eigenvalue $-m$) complete a basis of $\mathbb C^4$ for $m > 0$ ([[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^thm-c5a-10-2|Theorem §C5a.10.2]], 2); the completeness relation that expresses this is [[§C5a.12 Normalization and Spin Sums#^thm-c5a-12-10|Theorem §C5a.12.10]].
> - Which $\eta^s$ goes with which spin state of the antiparticle is decided at quantization (PS §3.5 finds that the spin assignment is reversed for the antiparticle, eq. (3.112); Yu chooses $\eta = \lambda\xi_{-\lambda}$ in the helicity basis, [[§C5a.13 Helicity Spinors and the Massless Limit#^thm-c5a-13-3|Theorem §C5a.13.3]]; [[§C5b.4 Fermions, Fock Space and the Pauli Principle|§C5b.4]]). Lecture 12 fixes $\eta^s = \xi^{-s}$ ([[§C9.6 Charge Conjugation on Oscillators and Spinors#^def-c9-6-5|Def. §C9.6.5]]), the same choice as Peskin–Schroeder's (3.136) and Yu's, with which $\hat b^{s\dagger}$ creates an antiparticle of physical spin $s$ ([[§C9.8 Physical Spin versus Wave-Function Spin#^thm-c9-8-3|Theorem §C9.8.3]]).
> - Used next: the Dirac conjugate $\bar v^s(p)$ ([[§C5a.11 The Spinors u(p), v(p) and Their Dirac Conjugates#^thm-c5a-11-4|Theorem §C5a.11.4]]).

^der-c5a-11-3

*Uses:* [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^def-c5a-10-1|Def. §C5a.10.1]], [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^thm-c5a-10-1|Theorem §C5a.10.1]], [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^thm-c5a-10-2|Theorem §C5a.10.2]], [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^thm-c5a-10-3|Theorem §C5a.10.3]], [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^thm-c5a-10-7|Theorem §C5a.10.7]], [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^thm-c5a-10-8|Theorem §C5a.10.8]], [[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-1|Theorem §C5a.7.1]]

> [!theorem] Theorem §C5a.11.4: The Dirac Conjugate of v(p)
> For the spinors $v^s(p)$ of [[§C5a.11 The Spinors u(p), v(p) and Their Dirac Conjugates#^thm-c5a-11-3|Theorem §C5a.11.3]], every $\mathbf p$ and $m \ge 0$, the Dirac conjugate ([[§C5a.2 The Dirac Form#^def-c5a-2-1|Def. §C5a.2.1]]) is the row
>
> $$
> \bar v^s(p) \equiv v^{s\dagger}(p)\,\gamma^0 = \bigl(-\eta^{s\dagger}\sqrt{p\cdot\bar\sigma},\ \eta^{s\dagger}\sqrt{p\cdot\sigma}\bigr), \qquad \bar v^s(p)\,(\slashed{p} + m) = 0 ,
> $$
>
> with the Hermitian roots of [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^def-c5a-10-5|Def. §C5a.10.5]].
> 1. The minus sign, in the lower half of the column $v^s(p)$, sits in the upper half of the row: the dagger leaves it in place (it is real), and $\gamma^0$ moves it.
> 2. The Dirac equation acts from the right with the eigenvalue of the column: $\bar v^s(p)\,\slashed{p} = -m\,\bar v^s(p)$.
> 3. At rest, $p = (m, \mathbf 0)$ with $m > 0$: $\bar v^s_0 = \sqrt m\,(-\eta^{s\dagger}, \eta^{s\dagger}) = -v_0^{s\dagger}$.
>
> *Model:* [[§C5a.7 The Dirac Equation and Its Lagrangian#^mod-c5a-7-3|Model §C5a.7.3]]; *applies:* c-number spinors, on shell, normalization of [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^def-c5a-10-4|Def. §C5a.10.4]], every $m \ge 0$ (part 3: $m > 0$).
>
> *Source: PHY 513 Lecture 9, Part C ("Normalization of v's": "$\gamma^0$ exchanges lower and upper entry, so an overall sign"; "Bonus Material: Orthogonality of u and v": the row $(\eta^\dagger\sqrt{p\cdot\sigma}, -\eta^\dagger\sqrt{p\cdot\bar\sigma})$ times $\gamma^0$) · the user's PHY 513 notes, Ch. 9 §9.5 (Derivation "Normalizations of the v's": $\bar v^r(p) = (-\eta^{r\dagger}\sqrt{p\cdot\bar\sigma}, \eta^{r\dagger}\sqrt{p\cdot\sigma})$) · PS §3.3, eqs. (3.62)–(3.64), (3.67) (the row is not displayed there) · Yu §5.4.2, eq. (5.206) (helicity basis) · the user's pre-course notes, §5.4 (note "Checking the spin sums") · the equation $\bar v(\slashed{p} + m) = 0$, the rest-frame check and the third route written here*

^thm-c5a-11-4

> [!derivation]- Derivation
> **Step 1** (the roots pass through the dagger). Both roots are Hermitian: real combinations of the Hermitian projectors $\Pi_\pm$ ([[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^def-c5a-10-5|Def. §C5a.10.5]]; Step 1 of [[§C5a.11 The Spinors u(p), v(p) and Their Dirac Conjugates#^der-c5a-11-2|Derivation §C5a.11.2]]). With $(AB)^\dagger = B^\dagger A^\dagger$ and, for the number $-1$, $(-1)^{\ast} = -1$,
>
> $$
> \bigl(\sqrt{p\cdot\sigma}\,\eta^s\bigr)^\dagger = \eta^{s\dagger}\sqrt{p\cdot\sigma}, \qquad \bigl(-\sqrt{p\cdot\bar\sigma}\,\eta^s\bigr)^\dagger = (-1)^{\ast}\,\eta^{s\dagger}\bigl(\sqrt{p\cdot\bar\sigma}\bigr)^\dagger = -\eta^{s\dagger}\sqrt{p\cdot\bar\sigma} .
> $$
>
> **Step 2** (dagger of the column, block by block). As for any column with halves $a$, $b$, $\begin{pmatrix}a\\ b\end{pmatrix}^\dagger = (a^\dagger,\ b^\dagger)$: transposition puts the entries of $a$ in the first two places of the row and those of $b$ in the last two, and each entry is conjugated. With $a = \sqrt{p\cdot\sigma}\,\eta^s$ and $b = -\sqrt{p\cdot\bar\sigma}\,\eta^s$ ([[§C5a.11 The Spinors u(p), v(p) and Their Dirac Conjugates#^thm-c5a-11-3|Theorem §C5a.11.3]]) and Step 1,
>
> $$
> v^{s\dagger}(p) = \bigl(\eta^{s\dagger}\sqrt{p\cdot\sigma},\ -\eta^{s\dagger}\sqrt{p\cdot\bar\sigma}\bigr) .
> $$
>
> The minus sign is still in the second half: the dagger moved nothing.
>
> **Step 3** ($\gamma^0$ swaps the halves). With $\gamma^0 = \begin{pmatrix}0 & \mathbb 1\\ \mathbb 1 & 0\end{pmatrix}$ ([[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-4|Def. §C5a.1.4]]) and the row rule $(c, d)\begin{pmatrix}A & B\\ C & D\end{pmatrix} = (cA + dC,\ cB + dD)$, $(a^\dagger, b^\dagger)\gamma^0 = (a^\dagger\cdot0 + b^\dagger\mathbb 1,\ a^\dagger\mathbb 1 + b^\dagger\cdot0) = (b^\dagger, a^\dagger)$. Hence
>
> $$
> \bar v^s(p) = v^{s\dagger}(p)\,\gamma^0 = \bigl(-\eta^{s\dagger}\sqrt{p\cdot\bar\sigma},\ \eta^{s\dagger}\sqrt{p\cdot\sigma}\bigr) .
> $$
>
> ⚑ By-product: the minus sign has a single origin, the relation "lower half = minus upper half" of the rest-frame solution $v_0^s$ ([[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^thm-c5a-10-3|Theorem §C5a.10.3]], from the eigenvalue $-m$, i.e. from the exponent $e^{+ip\cdot x}$); the boost carries it into the lower half of $v^s(p)$ (Step 4 of [[§C5a.11 The Spinors u(p), v(p) and Their Dirac Conjugates#^der-c5a-11-3|Derivation §C5a.11.3]]), the dagger keeps it there, and $\gamma^0$ moves it to the upper half of the row. Paired with the column $v^s$, whose sign is in the lower half, each term of $\bar v v$ carries it once → [[§C5a.12 Normalization and Spin Sums#^cau-c5a-12-1|Caution: The sign of v̄v]]. The formula and part 1.
>
> **Step 4** (the conjugate equation, directly). As in Step 4 of [[§C5a.11 The Spinors u(p), v(p) and Their Dirac Conjugates#^der-c5a-11-2|Derivation §C5a.11.2]], $(c, d)\,\slashed{p} = \bigl(d\,(p\cdot\bar\sigma),\ c\,(p\cdot\sigma)\bigr)$ for the chiral $\slashed{p}$ ([[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^def-c5a-10-2|Def. §C5a.10.2]]). Now $c = -\eta^{s\dagger}\sqrt{p\cdot\bar\sigma}$ and $d = \eta^{s\dagger}\sqrt{p\cdot\sigma}$:
>
> $$
> \bar v^s(p)\,\slashed{p} = \Bigl(\eta^{s\dagger}\sqrt{p\cdot\sigma}\,(p\cdot\bar\sigma),\ \ -\eta^{s\dagger}\sqrt{p\cdot\bar\sigma}\,(p\cdot\sigma)\Bigr) .
> $$
>
> The two products are the ones of that step, $\sqrt{p\cdot\sigma}\,(p\cdot\bar\sigma) = m\sqrt{p\cdot\bar\sigma}$ and $\sqrt{p\cdot\bar\sigma}\,(p\cdot\sigma) = m\sqrt{p\cdot\sigma}$ ([[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^thm-c5a-10-7|Theorem §C5a.10.7]], 1 and 3: split the unrooted factor into two roots, pair the first with its left neighbour). So
>
> $$
> \bar v^s(p)\,\slashed{p} = \bigl(m\,\eta^{s\dagger}\sqrt{p\cdot\bar\sigma},\ \ -m\,\eta^{s\dagger}\sqrt{p\cdot\sigma}\bigr) = -m\,\bigl(-\eta^{s\dagger}\sqrt{p\cdot\bar\sigma},\ \eta^{s\dagger}\sqrt{p\cdot\sigma}\bigr) = -m\,\bar v^s(p) ,
> $$
>
> and $\bar v^s(p)(\slashed{p} + m) = -m\,\bar v^s(p) + m\,\bar v^s(p) = 0$ ($m$ standing for $m\,\mathbb 1_4$). ⚑ By-product: the eigenvalue $-m$ is the relative minus sign between the two halves of the row. Multiplying by $\slashed{p}$ exchanges the halves ($d$ goes first), which moves the minus sign to the second half; pulling out $-1$ restores the row. For $\bar u$, with no relative sign, the same exchange gives $+m$. No step divides by $m$: valid for $m \ge 0$. Part 2.
>
> **Step 5** (rest frame). At $p = (m, \mathbf 0)$, $m > 0$, both roots are $\sqrt m\,\mathbb 1$ (Defs. §C5a.10.2 and §C5a.10.5 with $\mathbf p = 0$), so Step 3 gives $\bar v_0^s = \sqrt m\,(-\eta^{s\dagger}, \eta^{s\dagger})$. Directly from $v_0^s = \sqrt m(\eta^s, -\eta^s)$ ([[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^thm-c5a-10-3|Theorem §C5a.10.3]]): $v_0^{s\dagger} = \sqrt m(\eta^{s\dagger}, -\eta^{s\dagger})$, and the swap of two opposite halves gives $\sqrt m(-\eta^{s\dagger}, \eta^{s\dagger}) = -v_0^{s\dagger}$. Check of part 2 at rest, with $\slashed{p} + m = m\begin{pmatrix}\mathbb 1 & \mathbb 1\\ \mathbb 1 & \mathbb 1\end{pmatrix}$ (Step 1 of [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^der-c5a-10-3|Derivation §C5a.10.3]]) and the row rule:
>
> $$
> \bar v_0^s\,(\slashed{p} + m) = m\sqrt m\,\bigl(-\eta^{s\dagger} + \eta^{s\dagger},\ \ -\eta^{s\dagger} + \eta^{s\dagger}\bigr) = (0,\ 0) .
> $$
>
> Part 3. ⚑ By-product: at rest $\bar v_0 = -v_0^\dagger$, so $\bar v_0v_0 = -v_0^\dagger v_0 = -2m\,\eta^\dagger\eta$: the negative sign of $\bar vv$ is already there at rest, where $\bar u_0 = +u_0^\dagger$ → [[§C5a.12 Normalization and Spin Sums#^thm-c5a-12-4|Theorem §C5a.12.4]].
>
> **What the derivation shows**
> - Every difference from $\bar u^s(p)$ ([[§C5a.11 The Spinors u(p), v(p) and Their Dirac Conjugates#^thm-c5a-11-2|Theorem §C5a.11.2]]) is the one sign of $v^s(p)$, moved from the lower half of the column to the upper half of the row; the exchange of the roots is the same.
> - The row is a plane-wave solution of the conjugate Dirac equation ([[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-6|Theorem §C5a.7.6]], 2): for $\bar\psi = \bar v^s(p)\,e^{-ip\cdot x}$, $i\partial_\mu e^{-ip\cdot x} = p_\mu e^{-ip\cdot x}$, and $i\,\partial_\mu\bar\psi\,\gamma^\mu + m\bar\psi = \bar v^s(p)(\slashed{p} + m)\,e^{-ip\cdot x} = 0$ is part 2.
> - Assumptions as for $\bar u$: $p$ real on the forward mass shell, chiral basis for the explicit row; the equation $\bar v(\slashed{p} + m) = 0$ holds in every Hermitian basis (second route).
> - Used in: $\bar vv = -2m$, $\bar vu = 0$ and the spin sum $\sum_s v^s\bar v^s = \slashed{p} - m$ ([[§C5a.12 Normalization and Spin Sums#^thm-c5a-12-4|Theorem §C5a.12.4]], [[§C5a.12 Normalization and Spin Sums#^thm-c5a-12-5|Theorem §C5a.12.5]], [[§C5a.12 Normalization and Spin Sums#^thm-c5a-12-8|Theorem §C5a.12.8]]); the conjugate field ([[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-2|Theorem §C5b.2.2]]).

^der-c5a-11-4

*Uses:* [[§C5a.2 The Dirac Form#^def-c5a-2-1|Def. §C5a.2.1]], [[§C5a.11 The Spinors u(p), v(p) and Their Dirac Conjugates#^thm-c5a-11-3|Theorem §C5a.11.3]], [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^def-c5a-10-2|Def. §C5a.10.2]], [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^def-c5a-10-5|Def. §C5a.10.5]], [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^thm-c5a-10-7|Theorem §C5a.10.7]], [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^thm-c5a-10-3|Theorem §C5a.10.3]], [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-4|Def. §C5a.1.4]], [[§C5a.11 The Spinors u(p), v(p) and Their Dirac Conjugates#^der-c5a-11-2|Derivation §C5a.11.2]]

> [!derivation]- Derivation (second route: the Hermitian conjugate of the Dirac equation)
> This route uses only $(\slashed{p} + m)\,v^s(p) = 0$ ([[§C5a.11 The Spinors u(p), v(p) and Their Dirac Conjugates#^thm-c5a-11-3|Theorem §C5a.11.3]]) and the Hermiticity of the $\gamma$'s.
>
> **Step 1** (dagger of the equation). $(Mw)^\dagger = w^\dagger M^\dagger$ and the dagger of the zero column is the zero row, so $(\slashed{p} + m)\,v^s = 0$ gives $v^{s\dagger}(\slashed{p} + m)^\dagger = 0$.
>
> **Step 2** (dagger of the matrix). With $p_\mu$, $m$ real and $\mathbb 1^\dagger = \mathbb 1$, $(p_\mu\gamma^\mu + m\,\mathbb 1)^\dagger = p_\mu\gamma^{\mu\dagger} + m\,\mathbb 1$. Insert $\gamma^{\mu\dagger} = \gamma^0\gamma^\mu\gamma^0$ ([[§C5a.2 The Dirac Form#^thm-c5a-2-1|Theorem §C5a.2.1]]) and $\mathbb 1 = \gamma^0\gamma^0$ ([[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-1|Theorem §C5a.1.1]]):
>
> $$
> (\slashed{p} + m)^\dagger = \gamma^0\,(p_\mu\gamma^\mu)\,\gamma^0 + m\,\gamma^0\gamma^0 = \gamma^0\,(\slashed{p} + m)\,\gamma^0 .
> $$
>
> The sign of $m$ is unchanged: $m$ is real, so the dagger cannot flip it.
>
> **Step 3** (multiply by $\gamma^0$ on the right). Step 1 becomes $v^{s\dagger}\gamma^0(\slashed{p} + m)\gamma^0 = 0$; multiplying on the right by $\gamma^0$ and using $(\gamma^0)^2 = \mathbb 1$ gives $v^{s\dagger}\gamma^0(\slashed{p} + m) = 0$, i.e. $\bar v^s(p)\,(\slashed{p} + m) = 0$ ([[§C5a.2 The Dirac Form#^def-c5a-2-1|Def. §C5a.2.1]]).
>
> **What the derivation shows**
> - ⚑ By-product: the $+m$ of the conjugate equation is inherited unchanged from the column equation, whose sign came from the exponent $e^{+ip\cdot x}$ ([[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^thm-c5a-10-1|Theorem §C5a.10.1]], 2); the bar never changes the eigenvalue, only the side on which $\slashed{p}$ acts.
> - The bar of $(\slashed{p} + m)v$ is $\bar v(\slashed{p} + m)$ by the self-adjointness of the Dirac maps for the Dirac form ([[§C5a.2 The Dirac Form#^thm-c5a-2-2|Theorem §C5a.2.2]], 1); valid in every Hermitian basis and for $m \ge 0$. Assumption: $p_\mu$, $m$ real.
>
> *Source: the user's PHY 513 notes, Ch. 9 §9.6 (paragraph "The Dirac equation, from both sides", there for $u$), carried out here for $v$*

^der-c5a-11-4b

*Uses:* [[§C5a.11 The Spinors u(p), v(p) and Their Dirac Conjugates#^thm-c5a-11-3|Theorem §C5a.11.3]], [[§C5a.2 The Dirac Form#^thm-c5a-2-1|Theorem §C5a.2.1]], [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-1|Theorem §C5a.1.1]], [[§C5a.2 The Dirac Form#^def-c5a-2-1|Def. §C5a.2.1]]

> [!derivation]- Derivation (third route: the bar carries the inverse boost, m > 0)
> **Step 1** (the bar of a boosted column). $v^s(p) = \Lambda_{1/2}(p)\,v_0^s$ ([[§C5a.11 The Spinors u(p), v(p) and Their Dirac Conjugates#^thm-c5a-11-3|Theorem §C5a.11.3]]). With $\Lambda_{1/2}^\dagger\gamma^0 = \gamma^0\Lambda_{1/2}^{-1}$ ([[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-4|Theorem §C5a.3.4]], 2), $\bar v^s(p) = v_0^{s\dagger}\Lambda_{1/2}(p)^\dagger\gamma^0 = v_0^{s\dagger}\gamma^0\Lambda_{1/2}(p)^{-1} = \bar v_0^s\,\Lambda_{1/2}(p)^{-1}$.
>
> **Step 2** (the inverse boost). $\Lambda_{1/2}(p)^{-1} = \operatorname{diag}\bigl(\sqrt{p\cdot\bar\sigma}/\sqrt m,\ \sqrt{p\cdot\sigma}/\sqrt m\bigr) = \Lambda_{1/2}(\tilde p)$ ([[§C5a.11 The Spinors u(p), v(p) and Their Dirac Conjugates#^der-c5a-11-2c|Derivation §C5a.11.2, third route]], Step 2): the same matrix as for $u$, since the boost does not know which spinor it acts on.
>
> **Step 3** (multiply). With $\bar v_0^s = \sqrt m(-\eta^{s\dagger}, \eta^{s\dagger})$ (Step 5 of the first derivation), block by block,
>
> $$
> \bar v^s(p) = \sqrt m\,\bigl(-\eta^{s\dagger},\ \eta^{s\dagger}\bigr)\begin{pmatrix}\sqrt{p\cdot\bar\sigma}/\sqrt m & 0\\ 0 & \sqrt{p\cdot\sigma}/\sqrt m\end{pmatrix} = \bigl(-\eta^{s\dagger}\sqrt{p\cdot\bar\sigma},\ \eta^{s\dagger}\sqrt{p\cdot\sigma}\bigr) ,
> $$
>
> the formula of the statement: the minus sign of $\bar v_0^s$ rides along, as it did for the column.

*Uses:* [[§C5a.11 The Spinors u(p), v(p) and Their Dirac Conjugates#^thm-c5a-11-3|Theorem §C5a.11.3]], [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-4|Theorem §C5a.3.4]], [[§C5a.11 The Spinors u(p), v(p) and Their Dirac Conjugates#^der-c5a-11-2c|Derivation §C5a.11.2, third route]]

> [!caution] Caution: η means two things
> The lecture, the slides and Peskin–Schroeder use $\eta$ both for the rapidity and for the two-spinor in $v$. Here $\eta^s$, with a spin index, is always the two-spinor; the rapidity never carries an index. In C9 a third use appears, the parity phases $\eta_a$, $\eta_b$ ([[§C9.3 Parity on States, Spinors and the Dirac Field#^cau-c9-3-2|§C9.3, Caution: η means three things]]). The two-spinor itself is fixed from Lecture 12 on as $\eta^s = \xi^{-s}$ ([[§C9.6 Charge Conjugation on Oscillators and Spinors#^def-c9-6-5|Def. §C9.6.5]]).
>
> *Source: the user's PHY 513 notes, Ch. 9 §9.5 (Caution "η means two things")*

^cau-c5a-11-1

> [!caution] Caution: Names for the plane-wave spinors
> These notes write $u^s(p)$, $v^s(p)$, with the on-shell four-momentum as argument and $s = 1, 2$ labelling the spin basis $\xi^s$, $\eta^s$ ([[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^def-c5a-10-3|Def. §C5a.10.3]]), as Lecture 9, the user's PHY 513 notes and Peskin–Schroeder (eqs. (3.50), (3.62)) do; a second spin index is $r$. In the helicity basis they write $u_\lambda(p)$, $v_\lambda(p)$, $\lambda = \pm$ ([[§C5a.13 Helicity Spinors and the Massless Limit#^thm-c5a-13-2|Theorem §C5a.13.2]], [[§C5a.13 Helicity Spinors and the Massless Limit#^thm-c5a-13-3|Theorem §C5a.13.3]]). Yu and the user's pre-course notes use only the helicity basis and write $u(p, \lambda)$, $v(p, \lambda)$ (Yu §5.4.2). Quantum Mechanics, after Sakurai, writes $u^{(\pm)}(\mathbf p)$ for the positive- and negative-energy solutions of one particle ([[§C13.3★ Solutions of the Dirac Equation and the Hydrogen Atom#^thm-c13-3-1|QM Theorem §C13.3.1]]); its $u^{(-)}(\mathbf p)$ corresponds to $v^s(\tilde p)$ here, $\tilde p = (E_{\mathbf p}, -\mathbf p)$, up to the change of basis and normalization. Earlier drafts of this vault also wrote $u(p, s)$, $u(\mathbf p)$ and $v(p, \lambda)$.
>
> *Source: Lecture 9, Parts A and C · the user's PHY 513 notes, Ch. 9 §§9.3–9.5 · PS §3.3, eqs. (3.50), (3.62) · Yu §5.4.2, eqs. (5.157), (5.165)–(5.181) · Sakurai, as in QM §C13.3★*

^cau-c5a-11-2

> [!remark] Remark: In what sense a general solution is a superposition of these plane waves
> A plane wave $u(p)e^{-ip\cdot x}$ is a smooth, bounded solution: a tempered distribution, not a square-integrable wave function (as for $e^{-ip\cdot x}$ in [[§C2a.4 Particles and Relativistic Normalization#^cau-c2a-4-1|§C2a.4, Caution: Plane-wave states are not normalizable]]). A solution with Cauchy data whose spatial Fourier transform is a wave packet (Schwartz) is an absolutely convergent integral over $\mathbf p$ of $u^s(p)e^{-ip\cdot x}$ and $v^s(p)e^{+ip\cdot x}$ with wave-packet coefficients: for $m > 0$ the spinors are smooth and polynomially bounded ([[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^thm-c5a-10-6|Theorem §C5a.10.6]]), so a coefficient times a spinor is again a wave packet, and the integrals and their $x$-derivatives may be exchanged ([[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|Theorem §CA.1.1]]). Any tempered solution has a spacetime Fourier transform supported on the two sheets $p^0 = \pm E_{\mathbf p}$ of the mass shell, where the Dirac equation acts as the matrix $\pm\slashed{p}$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-2|Theorem §CA.3.2]], [[§CA.2 Generalized Functions#^thm-ca-2-7|Theorem §CA.2.7]]). For the quantum field the coefficients become operators, and the superposition holds as an operator-valued distribution, i.e. after smearing with test functions ([[§CA.2 Generalized Functions#^def-ca-2-11|Def. §CA.2.11]]; the field: [[§C5b.2 Mode Expansion and the Anticommutator Algebra|§C5b.2]]). The massless spinors are continuous but not smooth at $\mathbf p = 0$; they are still integrable against wave packets.
>
> *Source: the user's PHY 513 notes, Ch. 9 §9.1 (Derivation "Step 1": "each of its four components is a superposition of plane waves"), with the sense supplied from [[§C2a.2 Mode Expansion and the Mode Algebra#^der-c2a-2-2|Derivation §C2a.2.2]]*

^rem-c5a-11-2

> [!remark] Remark: What the field theory adds to the free Dirac spinors of Quantum Mechanics
> Quantum Mechanics solves the free Dirac equation as a wave equation for one particle, in the Dirac basis, with $u^{(\pm)}$ of energy $\pm E_{\mathbf p}$ normalized to $u^\dagger u = 2E_{\mathbf p}/(E_{\mathbf p} + mc^2)$ ([[§C13.3★ Solutions of the Dirac Equation and the Hydrogen Atom#^thm-c13-3-1|QM Theorem §C13.3.1]]; matrix conventions [[§C13.2★ The Dirac Equation#^cau-c13-2-1|QM Caution: Dirac matrices]]). The field theory changes three things:
> - **The negative-energy solutions are relabelled**, not interpreted as states: $u^{(-)}(\mathbf p)e^{i(\mathbf p\cdot\mathbf x + E_{\mathbf p}t)}$ is $v^s(\tilde p)e^{+i\tilde p\cdot x}$ with $\tilde p = (E_{\mathbf p}, -\mathbf p)$, a positive-$p^0$ label for a coefficient that becomes an antiparticle creation operator, instead of a Dirac sea ([[§C13.2★ The Dirac Equation#^rem-c13-2-7|QM Remark: The Dirac sea, the positron, and CPT]]).
> - **The construction comes from the Lorentz group**: solve at rest, boost with $\Lambda_{1/2}$; this needs the chiral basis, in which boosts are block-diagonal.
> - **The normalization is covariant**: $\bar uu = 2m$ in every frame and $u^\dagger u = 2E_{\mathbf p}$, the energy weight of relativistically normalized states ([[§C5a.12 Normalization and Spin Sums|§C5a.12]]).
>
> Dictionary: with $\psi_{\rm D} = U_D\psi$, $U_D = \frac1{\sqrt2}\begin{pmatrix}\mathbb 1 & \mathbb 1\\ -\mathbb 1 & \mathbb 1\end{pmatrix}$ (Larsen's matrix, [[§C5a.5 Chirality and Weyl Spinors#^ex-c5a-5-1|Example §C5a.5.1]]), the chiral $\gamma^\mu$ become $U_D\gamma^\mu U_D^\dagger$: $\gamma^0_{\rm D} = \operatorname{diag}(\mathbb 1, -\mathbb 1)$, $\gamma^i_{\rm D} = \begin{pmatrix}0 & \sigma^i\\ -\sigma^i & 0\end{pmatrix}$, so $\alpha^i = \gamma^0_{\rm D}\gamma^i_{\rm D}$ and $\beta = \gamma^0_{\rm D}$ are the Quantum Mechanics matrices. With the explicit roots of [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^thm-c5a-10-6|Theorem §C5a.10.6]] the spinor becomes ([[§C5a.11 The Spinors u(p), v(p) and Their Dirac Conjugates#^ex-c5a-11-1|Example §C5a.11.1]], worked step by step there)
>
> $$
> U_D\,u(p) = \sqrt{E_{\mathbf p} + m}\begin{pmatrix}\xi\\ \dfrac{\boldsymbol\sigma\cdot\mathbf p}{E_{\mathbf p} + m}\,\xi\end{pmatrix} ,
> $$
>
> which is the Quantum Mechanics $u^{(+)}$ times $\sqrt{E_{\mathbf p} + m}$ (with $c = 1$): the same solution, normalized to $u^\dagger u = (E + m)\cdot\frac{2E}{E + m} = 2E$.
>
> *Source: the user's PHY 513 notes, Ch. 8 (paragraph "Negative energy, antiparticles"), Ch. 9 §9.4 · the user's pre-course notes, §5.4 · Sakurai §8.2.2 as used in [[§C13.3★ Solutions of the Dirac Equation and the Hydrogen Atom|QM §C13.3★]]; the change of basis computed here*

^rem-c5a-11-3

> [!example] Example §C5a.11.1: The Plane-Wave Spinors in the Dirac Basis
> In the Dirac basis ([[§C5a.5 Chirality and Weyl Spinors#^ex-c5a-5-1|Example §C5a.5.1]]: $\gamma_D^0 = \operatorname{diag}(\mathbb 1, -\mathbb 1)$, $\gamma_D^i = \begin{pmatrix}0&\sigma^i\\-\sigma^i&0\end{pmatrix}$, components $\psi_D = U_D\psi$), the positive-frequency spinor of [[§C5a.11 The Spinors u(p), v(p) and Their Dirac Conjugates#^thm-c5a-11-1|Theorem §C5a.11.1]] is
>
> $$
> u_D(p) = U_D\,u(p) = \frac{1}{\sqrt{E_{\mathbf p} + m}}\begin{pmatrix}(E_{\mathbf p} + m)\,\xi\\ \boldsymbol\sigma\cdot\mathbf p\;\xi\end{pmatrix}, \qquad \bar u^r_D(p)\,u^s_D(p) = 2m\,\delta^{rs}\quad\text{for } \xi^{r\dagger}\xi^s = \delta^{rs} ,
> $$
>
> the normalization of [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^def-c5a-10-4|Def. §C5a.10.4]] ($\bar uu = 2m$ for $\xi^\dagger\xi = 1$), with $\bar u_D = u_D^\dagger\gamma_D^0$ ([[§C5a.2 The Dirac Form#^def-c5a-2-1|Def. §C5a.2.1]]). Here $\boldsymbol\sigma\cdot\mathbf p = \sum_ip^i\sigma^i$ is the three-vector product, not the contraction $p\cdot\sigma = E_{\mathbf p} - \boldsymbol\sigma\cdot\mathbf p$ of [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^def-c5a-10-2|Def. §C5a.10.2]].
>
> *Reading* (the comments after Problem 3 of Problem Set 6): at rest, $\mathbf p = 0$, the lower components vanish, $u_D = \sqrt{2m}\,(\xi, 0)$; for $|\mathbf p| \ll m$ they are smaller than the upper ones by $|\mathbf p|/2m$, and the two "large" upper components are the two-component wave function of a spin-½ particle of nonrelativistic quantum mechanics ([[§C13.2★ The Dirac Equation#^thm-c13-2-5|QM Theorem §C13.2.5]]) — why the Dirac basis is used at low energy ([[§C5a.5 Chirality and Weyl Spinors#^rem-c5a-5-5|§C5a.5, Remark: Why each basis is used]]).
>
> *Source: PHY 513, Problem Set 6, Problem 3(c)–(d) and the comments after Problem 3 (statement, Larsen; solution as the user wrote it) · Sakurai §8.2.2 as used in [[§C13.3★ Solutions of the Dirac Equation and the Hydrogen Atom|QM §C13.3★]] (the same spinor with another normalization)*

^ex-c5a-11-1

> [!derivation]- Derivation (the user's solution of Problem Set 6, Problem 3(c): the spinor)
> **1. The chiral-basis spinor.** $u(p) = \bigl(\sqrt{p\cdot\sigma}\,\xi,\ \sqrt{p\cdot\bar\sigma}\,\xi\bigr)$ ([[§C5a.11 The Spinors u(p), v(p) and Their Dirac Conjugates#^thm-c5a-11-1|Theorem §C5a.11.1]]), with $p\cdot\sigma = E_{\mathbf p}\mathbb 1 - \mathbf p\cdot\boldsymbol\sigma$ and $p\cdot\bar\sigma = E_{\mathbf p}\mathbb 1 + \mathbf p\cdot\boldsymbol\sigma$: the lowered index $p_i = -p^i$ gives the minus sign. In $\mathbf p\cdot\boldsymbol\sigma = \boldsymbol\sigma\cdot\mathbf p = \sum_ip^i\sigma^i$ the order does not matter, the $p^i$ being numbers.
>
> **2. The change of basis keeps it a solution.** $u_D = U_Du$ ([[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-2|Theorem §C5a.1.2]], one factor $U_D$ for one spinor index), and with $\gamma_D^\mu = U_D\gamma^\mu U_D^\dagger$, $U_D^\dagger U_D = \mathbb 1$ ([[§C5a.5 Chirality and Weyl Spinors#^ex-c5a-5-1|Example §C5a.5.1]], step 2 of its second-route derivation):
>
> $$
> \bigl(\gamma_D^\mu p_\mu - m\mathbb 1\bigr)U_Du(p) = U_D\bigl(\gamma^\mu p_\mu - m\mathbb 1\bigr)U_D^\dagger U_D\,u(p) = U_D\bigl(\gamma^\mu p_\mu - m\mathbb 1\bigr)u(p) = 0
> $$
>
> ([[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-2|Theorem §C5a.7.2]]).
>
> **3. The block product.**
>
> $$
> u_D(p) = \frac1{\sqrt2}\begin{pmatrix}\mathbb 1&\mathbb 1\\-\mathbb 1&\mathbb 1\end{pmatrix}\begin{pmatrix}\sqrt{p\cdot\sigma}\,\xi\\ \sqrt{p\cdot\bar\sigma}\,\xi\end{pmatrix} = \frac1{\sqrt2}\begin{pmatrix}\bigl(\sqrt{p\cdot\sigma} + \sqrt{p\cdot\bar\sigma}\bigr)\xi\\ \bigl(-\sqrt{p\cdot\sigma} + \sqrt{p\cdot\bar\sigma}\bigr)\xi\end{pmatrix} .
> $$
>
> **4. The square roots (the user's route).** $\sqrt{p\cdot\sigma} = (p\cdot\sigma + m\mathbb 1)/\sqrt{2(E_{\mathbf p} + m)}$ and likewise for $p\cdot\bar\sigma$ ([[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^thm-c5a-10-6|Theorem §C5a.10.6]], $m > 0$), checked by squaring. First, with $\sigma^i\sigma^j = \delta^{ij}\mathbb 1 + i\epsilon^{ijk}\sigma^k$ ([[§B6.1 Spin One-Half and the Pauli Matrices#^thm-b6-1-4|QM Theorem §B6.1.4]]), the $\epsilon$ term is antisymmetric in $i, j$ and $p^ip^j$ symmetric, so
>
> $$
> (\boldsymbol\sigma\cdot\mathbf p)^2 = \sum_{i,j}\bigl(\delta^{ij}\mathbb 1 + i\epsilon^{ijk}\sigma^k\bigr)p^ip^j = |\mathbf p|^2\,\mathbb 1 .
> $$
>
> Then, with $E_{\mathbf p}^2 - |\mathbf p|^2 = m^2$: $(p\cdot\sigma)^2 = E_{\mathbf p}^2\mathbb 1 + |\mathbf p|^2\mathbb 1 - 2E_{\mathbf p}\,\mathbf p\cdot\boldsymbol\sigma = 2E_{\mathbf p}(E_{\mathbf p}\mathbb 1 - \mathbf p\cdot\boldsymbol\sigma) - m^2\mathbb 1 = 2E_{\mathbf p}\,(p\cdot\sigma) - m^2\mathbb 1$, so, all terms expanded,
>
> $$
> (p\cdot\sigma + m\mathbb 1)^2 = 2E_{\mathbf p}\,(p\cdot\sigma) - m^2\mathbb 1 + 2m\,(p\cdot\sigma) + m^2\mathbb 1 = 2(E_{\mathbf p} + m)\,(p\cdot\sigma) .
> $$
>
> $p\cdot\sigma + m\mathbb 1$ has eigenvalues $E_{\mathbf p} \mp |\mathbf p| + m > 0$, so this is the positive root ([[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^def-c5a-10-5|Def. §C5a.10.5]]). The second identity follows with $\mathbf p \to -\mathbf p$. (Derivation §C5a.10.6 reaches $(p\cdot\sigma)^2 = 2E_{\mathbf p}\,p\cdot\sigma - m^2$ by Cayley–Hamilton instead of the Pauli product.)
>
> **5. Sum and difference.** $p\cdot\sigma + p\cdot\bar\sigma = 2E_{\mathbf p}\mathbb 1$ and $p\cdot\bar\sigma - p\cdot\sigma = 2\,\mathbf p\cdot\boldsymbol\sigma$; the $m\mathbb 1$ terms add in the upper entry and cancel in the lower one:
>
> $$
> u_D(p) = \frac1{\sqrt2}\,\frac1{\sqrt{2(E_{\mathbf p} + m)}}\begin{pmatrix}\bigl(p\cdot\sigma + m\mathbb 1 + p\cdot\bar\sigma + m\mathbb 1\bigr)\xi\\ \bigl(-p\cdot\sigma - m\mathbb 1 + p\cdot\bar\sigma + m\mathbb 1\bigr)\xi\end{pmatrix} = \frac1{2\sqrt{E_{\mathbf p} + m}}\begin{pmatrix}2(E_{\mathbf p} + m)\,\xi\\ 2\,\mathbf p\cdot\boldsymbol\sigma\,\xi\end{pmatrix} = \frac1{\sqrt{E_{\mathbf p} + m}}\begin{pmatrix}(E_{\mathbf p} + m)\,\xi\\ \boldsymbol\sigma\cdot\mathbf p\,\xi\end{pmatrix} .
> $$
>
> **What the derivation shows**
> - The Dirac-basis halves are the sum and the difference of the Weyl halves; at rest $p\cdot\sigma = p\cdot\bar\sigma = m\mathbb 1$, the Weyl halves are equal ([[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^thm-c5a-10-3|Theorem §C5a.10.3]]) and the difference vanishes: the "small" components measure how unequal the two chiralities are.
> - Assumption: $m > 0$ (Theorem §C5a.10.6); the final formula is continuous at $m = 0$ for $\mathbf p \neq 0$, $u_D = |\mathbf p|^{-1/2}(|\mathbf p|\xi, \boldsymbol\sigma\cdot\mathbf p\,\xi)$.
> - Same spinor, other normalization: Quantum Mechanics' $u^{(+)}$ is $u_D/\sqrt{E_{\mathbf p} + m}$ ([[§C5a.11 The Spinors u(p), v(p) and Their Dirac Conjugates#^rem-c5a-11-3|Remark: What the field theory adds to the free Dirac spinors of Quantum Mechanics]]).

^der-ex-c5a-11-1

> [!derivation]- Derivation (the user's solution of Problem Set 6, Problem 3(d): the normalization)
> **1. The bar in the Dirac basis.** $U_D$ is unitary, so the Dirac conjugate keeps its form, $\bar u_D = u_D^\dagger\gamma_D^0$ ([[§C5a.2 The Dirac Form#^thm-c5a-2-3|Theorem §C5a.2.3]]). The $\sigma^i$ are Hermitian and the $p^i$ real, so $(\boldsymbol\sigma\cdot\mathbf p\,\xi)^\dagger = \xi^\dagger(\boldsymbol\sigma\cdot\mathbf p)^\dagger = \xi^\dagger\,\boldsymbol\sigma\cdot\mathbf p$, and with $\gamma_D^0 = \operatorname{diag}(\mathbb 1, -\mathbb 1)$
>
> $$
> \bar u_D(p) = \frac1{\sqrt{E_{\mathbf p} + m}}\Bigl((E_{\mathbf p} + m)\,\xi^\dagger,\ \xi^\dagger\,\boldsymbol\sigma\cdot\mathbf p\Bigr)\begin{pmatrix}\mathbb 1&0\\0&-\mathbb 1\end{pmatrix} = \frac1{\sqrt{E_{\mathbf p} + m}}\Bigl((E_{\mathbf p} + m)\,\xi^\dagger,\ -\xi^\dagger\,\boldsymbol\sigma\cdot\mathbf p\Bigr) .
> $$
>
> **2. Row times column.**
>
> $$
> \bar u^r_D(p)\,u^s_D(p) = \frac1{E_{\mathbf p} + m}\,\xi^{r\dagger}\Bigl((E_{\mathbf p} + m)^2\,\mathbb 1 - (\boldsymbol\sigma\cdot\mathbf p)^2\Bigr)\xi^s .
> $$
>
> **3. Insert and expand.** $(\boldsymbol\sigma\cdot\mathbf p)^2 = |\mathbf p|^2\mathbb 1$ (step 4 above), $\xi^{r\dagger}\xi^s = \delta^{rs}$ and $|\mathbf p|^2 = E_{\mathbf p}^2 - m^2$:
>
> $$
> \bar u^r_Du^s_D = \frac{\delta^{rs}}{E_{\mathbf p} + m}\Bigl(E_{\mathbf p}^2 + m^2 + 2E_{\mathbf p}m - E_{\mathbf p}^2 + m^2\Bigr) = \frac{\delta^{rs}}{E_{\mathbf p} + m}\,2m(E_{\mathbf p} + m) = 2m\,\delta^{rs} .
> $$
>
> **What the derivation shows**
> - In the Dirac basis $\bar uu$ is (upper)$^2$ minus (lower)$^2$: the Dirac form has signature $(2, 2)$ ([[§C5a.2 The Dirac Form|§C5a.2]]), made diagonal by this basis. The same steps with a plus sign give $u_D^\dagger u_D = \bigl((E_{\mathbf p} + m)^2 + |\mathbf p|^2\bigr)/(E_{\mathbf p} + m) = 2E_{\mathbf p}$.
> - The result is the chiral-basis $\bar uu = 2m$ ([[§C5a.12 Normalization and Spin Sums#^thm-c5a-12-2|Theorem §C5a.12.2]]) carried over: a unitary change of basis preserves the Dirac form (Theorem §C5a.2.3), so the computation is a check, not a new normalization.

^der-ex-c5a-11-1b

*Uses:* [[§C5a.11 The Spinors u(p), v(p) and Their Dirac Conjugates#^thm-c5a-11-1|Theorem §C5a.11.1]], [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^thm-c5a-10-6|Theorem §C5a.10.6]], [[§C5a.5 Chirality and Weyl Spinors#^ex-c5a-5-1|Example §C5a.5.1]], [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-2|Theorem §C5a.1.2]], [[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-2|Theorem §C5a.7.2]], [[§C5a.2 The Dirac Form#^thm-c5a-2-3|Theorem §C5a.2.3]], [[§B6.1 Spin One-Half and the Pauli Matrices#^thm-b6-1-4|QM Theorem §B6.1.4]], [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^def-c5a-10-4|Def. §C5a.10.4]]

> [!abstract]- Mathematical background
> Proved in CB; each line says what the physics above relies on.
>
> Every check that $u$ and $v$ solve the Dirac equation, and every product of $\gamma$'s below, uses the Clifford relation:
> - [[§CB.11 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^thm-cb-11-12|Theorem §CB.11.12]] with [[§CB.11 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^der-cb-11-12|Derivation]] — squares, anticommutation, $\slashed p\slashed p = p^2$ ([[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-1|Theorem §C5a.1.1]]).
>
> The Dirac conjugates of $u$ and $v$ use the Dirac form in a Hermitian basis, the self-adjointness of the Dirac maps for it, and the pseudo-unitarity of $\Lambda_{1/2}$; Example §C5a.11.1 changes to the Dirac basis by the change-of-basis rules:
> - [[§CB.13 Complex Clifford Algebras and Clifford Modules#^def-cb-13-11|Def. §CB.13.11]], [[§CB.13 Complex Clifford Algebras and Clifford Modules#^def-cb-13-15|Def. §CB.13.15]] — Hermitian basis and the Dirac form $h_D(\chi, \psi) = \chi^\dagger\gamma^0\psi$ ([[§C5a.2 The Dirac Form#^thm-c5a-2-1|Theorem §C5a.2.1]], [[§C5a.2 The Dirac Form#^def-c5a-2-1|Def. §C5a.2.1]]).
> - [[§CB.13 Complex Clifford Algebras and Clifford Modules#^thm-cb-13-16|Theorem §CB.13.16]] with [[§CB.13 Complex Clifford Algebras and Clifford Modules#^der-cb-13-16|Derivation]] — $\overline{\gamma^\mu\chi} = \bar\chi\gamma^\mu$: the Dirac maps are self-adjoint for $h_D$ (the bars of $(\slashed p \mp m)$ below); physics form: [[§C5a.2 The Dirac Form#^thm-c5a-2-2|Theorem §C5a.2.2]].
> - [[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-18-13|Theorem §CB.18.13]] with [[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^der-cb-18-13|Derivation]], [[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^der-cb-18-13b|Derivation (second route)]] — $\Lambda_{1/2}^\dagger\gamma^0 = \gamma^0\Lambda_{1/2}^{-1}$ (the boosted conjugates $\bar u^s(p)$, $\bar v^s(p)$; [[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-1|Theorem §C5a.6.1]]); physics form: [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-4|Theorem §C5a.3.4]].
> - [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-5|Theorem §CB.0.5]] with [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^der-cb-0-5|Derivation]] — $\psi' = U\psi$, $M' = UMU^{-1}$ (Example §C5a.11.1; [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-2|Theorem §C5a.1.2]]).

> [!remark]- Connections
> - The bar of a boosted spinor carries the inverse boost, and for the pure boosts used here $\Lambda_{1/2}(p)^{-1} = \Lambda_{1/2}(\tilde p)$, $\tilde p = (E_{\mathbf p}, -\mathbf p)$ ([[§C5a.11 The Spinors u(p), v(p) and Their Dirac Conjugates#^der-c5a-11-2c|Derivation §C5a.11.2, third route]]). With $\Lambda_{1/2}(p)$ Hermitian this explains the orthogonality at opposite momenta of [[§C5a.12 Normalization and Spin Sums#^thm-c5a-12-6|Theorem §C5a.12.6]] for $m > 0$: $u^{r\dagger}(p)\,v^s(\tilde p) = u_0^{r\dagger}\Lambda_{1/2}(p)\,\Lambda_{1/2}(p)^{-1}v_0^s = u_0^{r\dagger}v_0^s = m(\xi^{r\dagger}\eta^s - \xi^{r\dagger}\eta^s) = 0$, the rest-frame orthogonality transported by a boost and its inverse.
