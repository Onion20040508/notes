---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C5a
section: C5a.0
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C4.9 Vector-Field Propagators]] · ↑ [[· C5a Spinors and the Dirac Equation]] · [[§C5a.1 Spinor Space and the Clifford Action]] →

*Sources: Peskin & Schroeder, An Introduction to Quantum Field Theory, §3.2, pp. 40–44, eqs. (3.22)–(3.23), (3.28)–(3.32), (3.36)–(3.44), and §3.4, pp. 49–50 · the user's PHY 513 notes, Ch. 7 §7.4.6, Ch. 8 §8.1, §8.6, §8.9–§8.11, Ch. 9 §9.6, Ch. 10 §10.5 · PHY 513 Lectures 7–10 (Larsen) · Yu Zhao-Huan, 量子场论讲义, §1.1, §5.2–§5.3, eqs. (5.110)–(5.115) · the user's pre-course notes, §5.1 ("A $2\times2$ realization fails"), §5.3 · Axler, Linear Algebra Done Right (the vault's Linear Algebra notes), linked where used · the forcing direction of the arguments and their organization written here.*

Why does a spin-$\frac12$ field need four components and a set of anticommuting matrices? Dirac asked for a relativistic wave equation of first order whose square is the Klein–Gordon operator ([[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^mod-c1b-2-6|Model §C1b.2.6]]). This section derives what that requirement forces: the Clifford relation (Theorem §C5a.0.1), coefficients that cannot commute (Theorem §C5a.0.2), matrices of even size at least four (Theorem §C5a.0.3), and two components only when there is no mass (Theorem §C5a.0.4). It then lists what the $\gamma$'s are used for and maps the chapter. The structures themselves are built in §C5a.1–§C5a.7: where something is proved there, it is linked here, not proved again. The converse direction, from the Clifford relation to the Klein–Gordon equation, is [[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-8|Theorem §C5a.7.8]]; in relativistic quantum mechanics the same argument is [[§C13.2★ The Dirac Equation#^thm-c13-2-2|QM Theorem §C13.2.2]].

*Conventions* ([[Larsen PHY 513]]): natural units; $g = \operatorname{diag}(+,-,-,-)$, $\partial^2 = g^{\mu\nu}\partial_\mu\partial_\nu$, $p^2 = g^{\mu\nu}p_\mu p_\nu$; repeated Greek indices are summed unless "no sum" is written; $\mathbb 1_n$ is the $n\times n$ identity; $\psi$ is a classical field (no hat).

## The requirement and the Clifford relation

> [!theorem] Theorem §C5a.0.1: Squaring a First-Order Equation
> Let $\gamma^0, \dots, \gamma^3$ be constant complex $n\times n$ matrices and $m \ge 0$. The following are equivalent:
> 1. $i\gamma^\mu\partial_\mu - m$ is a factor of the Klein–Gordon operator ([[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^mod-c1b-2-6|Model §C1b.2.6]]): $(-i\gamma^\nu\partial_\nu - m)(i\gamma^\mu\partial_\mu - m)\psi = (\partial^2 + m^2)\psi$ for every $C^2$ function $\psi : \mathbb R^4 \to \mathbb C^n$;
> 2. $(p_\mu\gamma^\mu)^2 = p^2\,\mathbb 1_n$ for every $p \in \mathbb R^4$;
> 3. the Clifford relation $\{\gamma^\mu, \gamma^\nu\} = 2g^{\mu\nu}\,\mathbb 1_n$ ([[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-7|Def. §C5a.1.7]]); in components, $(\gamma^0)^2 = \mathbb 1_n$, $(\gamma^i)^2 = -\mathbb 1_n$ and $\gamma^\mu\gamma^\nu = -\gamma^\nu\gamma^\mu$ for $\mu \ne \nu$.
>
> The condition does not involve $m$: it is the same for every mass, $m = 0$ included.
>
> *Source: PS §3.2, p. 43 (the product, in the direction Dirac ⇒ Klein–Gordon) · Yu §5.3, eq. (5.110) (the same) · the user's PHY 513 notes, Ch. 8 §8.1 (paragraph "Square to ±1, or square root?"), §8.11 ("in momentum space $(\gamma\cdot p)^2 = p^2\mathbb 1$") · the equivalence, with the plane-wave and polarization steps, written here*

^thm-c5a-0-1

> [!derivation]- Derivation
> **1. Expand the product into its four terms.** The $\gamma$'s are constant, so derivatives pass through them, and $m$ is a number, so it commutes with everything:
>
> $$
> (-i\gamma^\nu\partial_\nu)(i\gamma^\mu\partial_\mu) = \gamma^\nu\gamma^\mu\partial_\nu\partial_\mu, \quad (-i\gamma^\nu\partial_\nu)(-m) = +im\gamma^\nu\partial_\nu, \quad (-m)(i\gamma^\mu\partial_\mu) = -im\gamma^\mu\partial_\mu, \quad (-m)(-m) = m^2 ,
> $$
>
> using $(-i)(i) = 1$. Renaming the dummy index $\mu \to \nu$ in the third term shows that the two middle terms are the same operator with opposite signs: they cancel. So the left side of 1 is $(\gamma^\nu\gamma^\mu\partial_\nu\partial_\mu + m^2)\psi$. (This is step 2 of [[§C5a.7 The Dirac Equation and Its Lagrangian#^der-c5a-7-8|Derivation §C5a.7.8]], which uses nothing about the $\gamma$'s but their constancy.) ⚑ By-product: the terms linear in $m$ cancel whatever the $\gamma$'s are, and $m^2$ appears on both sides of 1, so the condition is on the $\gamma$'s alone → last sentence of the statement.
>
> **2. Symmetrize.** For $\psi \in C^2$, $\partial_\nu\partial_\mu\psi = \partial_\mu\partial_\nu\psi$. Let $T = \gamma^\nu\gamma^\mu\partial_\nu\partial_\mu$. Renaming the dummies $\nu \leftrightarrow \mu$, $T = \gamma^\mu\gamma^\nu\partial_\mu\partial_\nu = \gamma^\mu\gamma^\nu\partial_\nu\partial_\mu$; averaging the two forms,
>
> $$
> T = \tfrac12\bigl(\gamma^\nu\gamma^\mu + \gamma^\mu\gamma^\nu\bigr)\partial_\nu\partial_\mu = \tfrac12\{\gamma^\nu, \gamma^\mu\}\,\partial_\nu\partial_\mu .
> $$
>
> With $\partial^2 = g^{\nu\mu}\partial_\nu\partial_\mu$, condition 1 becomes $B^{\nu\mu}\partial_\nu\partial_\mu\psi = 0$ for every $\psi$, where
>
> $$
> B^{\nu\mu} \equiv \tfrac12\{\gamma^\nu, \gamma^\mu\} - g^{\nu\mu}\,\mathbb 1_n = B^{\mu\nu} .
> $$
>
> **3. (3) ⇒ (1).** If 3 holds, every $B^{\nu\mu} = 0$, and step 2 holds for every $\psi$.
>
> **4. (1) ⇒ (2): plane waves.** Take $\psi(x) = w\,e^{-ip\cdot x}$ with a constant column $w \in \mathbb C^n$ and $p \in \mathbb R^4$; it is $C^2$, with $\partial_\mu\psi = -ip_\mu\psi$ and $\partial_\nu\partial_\mu\psi = (-ip_\nu)(-ip_\mu)\psi = -p_\nu p_\mu\psi$. Step 2 gives $-B^{\nu\mu}p_\nu p_\mu\,w\,e^{-ip\cdot x} = 0$; the exponential never vanishes, so $B^{\nu\mu}p_\nu p_\mu w = 0$ for every $w$, i.e. the matrix $B^{\nu\mu}p_\nu p_\mu$ is $0$. Now expand the square: $(p_\mu\gamma^\mu)^2 = p_\nu p_\mu\gamma^\nu\gamma^\mu$, and $p_\nu p_\mu$ is symmetric, so as in step 2 only the symmetric part survives:
>
> $$
> (p_\mu\gamma^\mu)^2 = \tfrac12p_\nu p_\mu\{\gamma^\nu, \gamma^\mu\} = p_\nu p_\mu\bigl(g^{\nu\mu}\mathbb 1_n + B^{\nu\mu}\bigr) = p^2\,\mathbb 1_n + 0 .
> $$
>
> **5. (2) ⇒ (3): polarization.** By the middle equality of step 4, condition 2 says $Q(p) \equiv B^{\nu\mu}p_\nu p_\mu = 0$ for every $p$; since $p \in \mathbb R^4$ is arbitrary, so are its lower components $p_\mu$. Fix $\mu$ and take $p_\mu = 1$, all other components $0$: $Q = B^{\mu\mu} = 0$ (no sum). Fix $\mu \ne \nu$ and take $p_\mu = p_\nu = 1$, the other two $0$: $Q = B^{\mu\mu} + B^{\nu\nu} + B^{\mu\nu} + B^{\nu\mu} = 0 + 0 + 2B^{\mu\nu}$, by the previous case and $B^{\nu\mu} = B^{\mu\nu}$. So every $B^{\mu\nu} = 0$: $\{\gamma^\mu, \gamma^\nu\} = 2g^{\mu\nu}\mathbb 1_n$.
>
> **6. Components.** For $\mu = \nu$: $2(\gamma^\mu)^2 = 2g^{\mu\mu}\mathbb 1_n$ (no sum), so $(\gamma^0)^2 = \mathbb 1_n$ and $(\gamma^i)^2 = -\mathbb 1_n$. For $\mu \ne \nu$: $g^{\mu\nu} = 0$, so $\gamma^\mu\gamma^\nu + \gamma^\nu\gamma^\mu = 0$. (These are part 1 of [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-5|Theorem §C5a.1.5]], there read off the relation in the same way.)
>
> **What the derivation shows**
> - The Clifford relation is not an additional postulate: it is the requirement "a first-order square root of the Klein–Gordon operator" written as an identity among the coefficients. [[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-8|Theorem §C5a.7.8]] is the direction (3) ⇒ every solution solves Klein–Gordon.
> - Assumptions used: constant coefficients; $C^2$ fields (for $\partial_\mu\partial_\nu = \partial_\nu\partial_\mu$); the coefficient of $m$ normalized to $\mathbb 1_n$. An invertible coefficient $M$, $(i\gamma^\mu\partial_\mu - mM)\psi = 0$, is removed by multiplying with $M^{-1}$, which replaces $\gamma^\mu$ by $M^{-1}\gamma^\mu$.
> - The requirement is an identity of operators, as in Dirac, PS and Yu: the first-order operator must be a factor. This section does not use the weaker-looking demand that only the solutions satisfy Klein–Gordon.
> - Condition 2 is the precise form of "$p_\mu\gamma^\mu$ is a square root of $p^2$" ([[§C5a.1 Spinor Space and the Clifford Action#^rem-c5a-1-4|§C5a.1, Remark: A square root of p²]]).
> - Used next: what the relation forces on the $\gamma$'s (Theorems §C5a.0.2–§C5a.0.3); the two-component case (Theorem §C5a.0.4).

^der-c5a-0-1

*Uses:* [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^mod-c1b-2-6|Model §C1b.2.6]], [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-7|Def. §C5a.1.7]], [[§C5a.7 The Dirac Equation and Its Lagrangian#^der-c5a-7-8|Derivation §C5a.7.8]]

## Why matrices, and why four by four

> [!theorem] Theorem §C5a.0.2: The Coefficients Cannot Commute
> Let $\gamma^0, \dots, \gamma^3$ satisfy the Clifford relation ([[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation#^thm-c5a-0-1|Theorem §C5a.0.1]], 3) in an associative algebra with unit $1 \ne 0$: numbers, $n\times n$ matrices, or linear maps on a vector space. Then
> 1. each $\gamma^\mu$ is invertible, with $(\gamma^\mu)^{-1} = g^{\mu\mu}\gamma^\mu$ (no sum);
> 2. $\gamma^\mu\gamma^\nu \ne \gamma^\nu\gamma^\mu$ for every $\mu \ne \nu$.
>
> Hence the $\gamma$'s cannot be numbers: a one-component field has no first-order equation that squares to Klein–Gordon. And no basis makes all four $n\times n$ Dirac matrices diagonal at once.
>
> *Source: PS §3.2, p. 41 ("There is no fourth $2\times2$ matrix … that anticommutes with the three Pauli sigma matrices", the matrix version) · the user's PHY 513 notes, Ch. 8 §8.1 ("Square to ±1, or square root?") · the argument written here*

^thm-c5a-0-2

> [!derivation]- Derivation
> **1. Inverses.** By Theorem §C5a.0.1, 3, $(\gamma^\mu)^2 = g^{\mu\mu}1$ (no sum), with $g^{\mu\mu} = \pm1$, so $(g^{\mu\mu})^2 = 1$. Then $\gamma^\mu\cdot g^{\mu\mu}\gamma^\mu = g^{\mu\mu}(\gamma^\mu)^2 = (g^{\mu\mu})^2\,1 = 1$, and the same with the factors in the other order: $(\gamma^\mu)^{-1} = g^{\mu\mu}\gamma^\mu$.
>
> **2. Assume two of them commute.** Suppose $\gamma^\mu\gamma^\nu = \gamma^\nu\gamma^\mu$ for some $\mu \ne \nu$. Then $\{\gamma^\mu, \gamma^\nu\} = \gamma^\mu\gamma^\nu + \gamma^\mu\gamma^\nu = 2\gamma^\mu\gamma^\nu$, while the relation gives $\{\gamma^\mu, \gamma^\nu\} = 2g^{\mu\nu}1 = 0$, because $g$ is diagonal. So $\gamma^\mu\gamma^\nu = 0$.
>
> **3. Then one of them vanishes.** Multiply $\gamma^\mu\gamma^\nu = 0$ on the left by $(\gamma^\mu)^{-1}$ (step 1): $\gamma^\nu = (\gamma^\mu)^{-1}\gamma^\mu\gamma^\nu = (\gamma^\mu)^{-1}\cdot0 = 0$.
>
> **4. Contradiction.** Then $(\gamma^\nu)^2 = 0$, but the relation demands $(\gamma^\nu)^2 = g^{\nu\nu}1 = \pm1 \ne 0$, because $1 \ne 0$. So no two distinct $\gamma$'s commute: part 2.
>
> **5. Numbers.** Complex numbers commute, so by step 4 no four (indeed no two) complex numbers satisfy the relation: for $n = 1$ condition 3 of Theorem §C5a.0.1 has no solution, and therefore neither has condition 1.
>
> **6. No common diagonal form.** Diagonal matrices commute: $\operatorname{diag}(a_1, \dots, a_n)\operatorname{diag}(b_1, \dots, b_n) = \operatorname{diag}(a_1b_1, \dots, a_nb_n) = \operatorname{diag}(b_1, \dots, b_n)\operatorname{diag}(a_1, \dots, a_n)$. If one basis made all $\gamma^\mu$ diagonal, they would commute, against part 2. Since a change of basis changes the matrices by $U(\cdot)U^{-1}$ and keeps the relation ([[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-7|Theorem §C5a.1.7]]), this holds in every basis: the Dirac maps have no common eigenbasis.
>
> **What the derivation shows**
> - Only the relation and $1 \ne 0$ were used, and only two of the $\gamma$'s: the conclusion holds in any spacetime dimension with at least one time and one space direction (Example §C5a.0.1).
> - So $\psi$ has more than one component, and the $\gamma$'s mix the components: this is where spinor components come from. The same three steps show that $\gamma^0$ and $\gamma^5$ are never diagonal together ([[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-7|Theorem §C5a.5.7]]).
> - Used next: the size of the matrices (Theorem §C5a.0.3).

^der-c5a-0-2

*Uses:* [[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation#^thm-c5a-0-1|Theorem §C5a.0.1]], [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-7|Theorem §C5a.1.7]]

> [!theorem] Theorem §C5a.0.3: The Smallest Coefficients Are 4×4 Matrices
> Let $\gamma^0, \dots, \gamma^3$ be complex $n\times n$ matrices satisfying the Clifford relation ([[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation#^thm-c5a-0-1|Theorem §C5a.0.1]], 3). Then
> 1. each $\gamma^\mu$ is traceless; $\gamma^0$ is diagonalizable with eigenvalues $+1$ and $-1$, each $n/2$ times, and each $\gamma^i$ with $+i$ and $-i$, each $n/2$ times; in particular **$n$ is even**;
> 2. $n \ge 4$;
> 3. $n = 4$ occurs: the chiral matrices ([[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-11|Def. §C5a.1.11]]) satisfy the relation ([[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-10|Theorem §C5a.1.10]]).
>
> So the smallest first-order square root of the Klein–Gordon operator acts on columns $\psi \in \mathbb C^4$.
>
> *Source: PS §3.2, p. 41 ("these matrices must be at least 4 × 4") · the user's PHY 513 notes, Ch. 8 §8.1 ("four is the smallest dimension in which (clifford) can be solved") · the user's pre-course notes, §5.1 ("Since at most $N^2$ matrices of size $N\times N$ are independent, $N \ge 4$") · the evenness and the direct $2\times2$ argument written out here*

^thm-c5a-0-3

> [!derivation]- Derivation
> **1. Traceless.** Fix $\mu$ and pick $\nu \ne \mu$. By anticommutation and Theorem §C5a.0.2, 1, $(\gamma^\nu)^{-1}\gamma^\mu\gamma^\nu = -(\gamma^\nu)^{-1}\gamma^\nu\gamma^\mu = -\gamma^\mu$. Take the trace and use its cyclicity ([[§33 Trace꞉ A Connection Between Matrices and Operators#^ladr-8-49|LADR Thm. 8.49]]): $\operatorname{tr}\gamma^\mu = -\operatorname{tr}\bigl((\gamma^\nu)^{-1}\gamma^\mu\gamma^\nu\bigr) = -\operatorname{tr}\bigl(\gamma^\mu\gamma^\nu(\gamma^\nu)^{-1}\bigr) = -\operatorname{tr}\gamma^\mu$, so $\operatorname{tr}\gamma^\mu = 0$. (This is the case $|A| = 1$ of step 3 of [[§C5a.1 Spinor Space and the Clifford Action#^der-c5a-1-6|Derivation §C5a.1.6]], which proves it for every product of distinct $\gamma$'s in any size $n$.)
>
> **2. Eigenvalues of γ⁰.** $(\gamma^0)^2 = \mathbb 1_n$, so the minimal polynomial of $\gamma^0$ divides $z^2 - 1 = (z - 1)(z + 1)$, which has distinct zeros; hence $\gamma^0$ is diagonalizable with eigenvalues in $\{1, -1\}$ ([[§17 Diagonalizable Operators#^ladr-5-62|LADR Thm. 5.62]]). Let $n_+$, $n_-$ be their multiplicities: $n_+ + n_- = n$. The trace is the sum of the eigenvalues with multiplicity ([[§33 Trace꞉ A Connection Between Matrices and Operators#^ladr-8-52|LADR Thm. 8.52]]), so step 1 gives $n_+ - n_- = 0$. Hence $n_+ = n_- = n/2$, and $n$ is even. ⚑ By-product: $n$ is even → part 1 of the statement. ([[§C5a.1 Spinor Space and the Clifford Action#^der-c5a-1-8|Derivation §C5a.1.8]] runs the same argument once $n = 4$ is known.)
>
> **3. Eigenvalues of γⁱ.** $(\gamma^i)^2 = -\mathbb 1_n$: the minimal polynomial divides $z^2 + 1 = (z - i)(z + i)$, again with distinct zeros, so $\gamma^i$ is diagonalizable with eigenvalues in $\{i, -i\}$; the trace gives $i(n_+ - n_-) = 0$, so $n_+ = n_- = n/2$.
>
> **4. At least four.** The sixteen ordered products $\gamma^{\mu_1}\cdots\gamma^{\mu_k}$ ($\mu_1 < \dots < \mu_k$, including $\mathbb 1_n$) are linearly independent in the $n^2$-dimensional space of $n\times n$ matrices, so $n^2 \ge 16$, $n \ge 4$ ([[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-6|Theorem §C5a.1.6]], part 3, proved there for every $n$; not repeated). Steps 2 and 4 together leave $n \in \{4, 6, 8, \dots\}$.
>
> **5. Four occurs.** [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-10|Theorem §C5a.1.10]] checks all ten conditions of the relation for the chiral matrices; Example §C5a.0.2 below carries out the square $(p_\mu\gamma^\mu)^2$ for them.
>
> **What the derivation shows**
> - Only the relation was used, so the bounds hold for every first-order square root of the Klein–Gordon operator (Theorem §C5a.0.1).
> - Sizes $n = 6, 10, \dots$ pass both tests here; that every size is in fact a multiple of four is the structure of the Clifford algebra ([[§C5a.1 Spinor Space and the Clifford Action#^rem-c5a-1-5|§C5a.1, ★ Remark: The complexified Clifford algebra is the full matrix algebra]]).
> - Used next: spinor space as the space the $\gamma$'s act on ([[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-1|Def. §C5a.1.1]]); its uniqueness is Pauli's theorem ([[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-12|Theorem §C5a.1.12]]).

^der-c5a-0-3

> [!derivation]- Derivation (second route: n = 2 directly, by expanding in Pauli matrices)
> **1. Traceless 2×2 matrices.** $\mathbb 1_2, \sigma^1, \sigma^2, \sigma^3$ are a basis of the $2\times2$ complex matrices, with $\operatorname{tr}\mathbb 1_2 = 2$ and $\operatorname{tr}\sigma^i = 0$ ([[§B6.1 Spin One-Half and the Pauli Matrices#^thm-b6-1-4|QM Theorem §B6.1.4]]). So $\gamma = a_0\mathbb 1_2 + \mathbf a\cdot\boldsymbol\sigma$ has $\operatorname{tr}\gamma = 2a_0$. By step 1 above each $\gamma^\mu$ is traceless, so $\gamma^\mu = \mathbf a^\mu\cdot\boldsymbol\sigma = \sum_ia^\mu_i\sigma^i$ with $\mathbf a^\mu \in \mathbb C^3$.
>
> **2. Anticommutators of such matrices.** With $\sigma^i\sigma^j = \delta^{ij}\mathbb 1_2 + i\varepsilon^{ijk}\sigma^k$ (QM Theorem §B6.1.4), for $\mathbf a, \mathbf b \in \mathbb C^3$:
>
> $$
> \{\mathbf a\cdot\boldsymbol\sigma, \mathbf b\cdot\boldsymbol\sigma\} = \sum_{i,j}a_ib_j\bigl(\sigma^i\sigma^j + \sigma^j\sigma^i\bigr) = \sum_{i,j}a_ib_j\bigl(2\delta^{ij}\mathbb 1_2 + i\varepsilon^{ijk}\sigma^k + i\varepsilon^{jik}\sigma^k\bigr) = 2\,(\mathbf a\cdot\mathbf b)\,\mathbb 1_2 ,
> $$
>
> where $\mathbf a\cdot\mathbf b \equiv \sum_ia_ib_i$ (no complex conjugation), and the $\varepsilon$ terms cancel because $\varepsilon^{jik} = -\varepsilon^{ijk}$.
>
> **3. The relation as a condition on vectors.** By step 2, $\{\gamma^\mu, \gamma^\nu\} = 2g^{\mu\nu}\mathbb 1_2$ says $\mathbf a^\mu\cdot\mathbf a^\nu = g^{\mu\nu}$ for $\mu, \nu = 0, \dots, 3$.
>
> **4. Four vectors in ℂ³ are dependent.** $\mathbb C^3$ is spanned by three vectors, so a linearly independent list has at most three ([[§4 Span and Linear Independence#^ladr-2-22|LADR Thm. 2.22]]): there are $c_0, \dots, c_3$, not all $0$, with $\sum_\mu c_\mu\mathbf a^\mu = 0$.
>
> **5. Contradiction.** Dot this with $\mathbf a^\nu$ and use step 3: $0 = \sum_\mu c_\mu\,\mathbf a^\mu\cdot\mathbf a^\nu = \sum_\mu c_\mu g^{\mu\nu} = c_\nu g^{\nu\nu}$ (no sum; $g$ is diagonal) for each $\nu$. Since $g^{\nu\nu} = \pm1$, every $c_\nu = 0$, against step 4. So no four $2\times2$ matrices satisfy the relation.
>
> **What the derivation shows**
> - This is PS's parenthesis "there is no fourth $2\times2$ matrix that anticommutes with the three Pauli sigma matrices" made explicit, and the user's pre-course remark "a $2\times2$ realization fails".
> - Three vectors with $\mathbf a^\mu\cdot\mathbf a^\nu = g^{\mu\nu}$ do exist in $\mathbb C^3$: with one time and two space directions, $2\times2$ matrices suffice → Example §C5a.0.1.
> - The mechanism, anticommuting matrices are linearly independent, is the same as in the sixteen-products bound ([[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-6|Theorem §C5a.1.6]]); here it is applied to the four $\gamma$'s themselves inside a three-dimensional space.

^der-c5a-0-3b

*Uses:* [[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation#^thm-c5a-0-1|Theorem §C5a.0.1]], [[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation#^thm-c5a-0-2|Theorem §C5a.0.2]], [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-6|Theorem §C5a.1.6]], [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-10|Theorem §C5a.1.10]], [[§33 Trace꞉ A Connection Between Matrices and Operators#^ladr-8-49|LADR Thm. 8.49]], [[§33 Trace꞉ A Connection Between Matrices and Operators#^ladr-8-52|LADR Thm. 8.52]], [[§17 Diagonalizable Operators#^ladr-5-62|LADR Thm. 5.62]], [[§4 Span and Linear Independence#^ladr-2-22|LADR Thm. 2.22]], [[§B6.1 Spin One-Half and the Pauli Matrices#^thm-b6-1-4|QM Theorem §B6.1.4]]

> [!example] Example §C5a.0.1: Two-Component Square Roots in 1+1 and 2+1 Dimensions
> With fewer $\gamma$'s, $2\times2$ matrices suffice. In $1+1$ dimensions, $g = \operatorname{diag}(1, -1)$, take
>
> $$
> \gamma^0 = \sigma^1, \qquad \gamma^1 = i\sigma^2 .
> $$
>
> *Computation.* With the Pauli product rule ([[§B6.1 Spin One-Half and the Pauli Matrices#^thm-b6-1-4|QM Theorem §B6.1.4]]): $(\sigma^1)^2 = \mathbb 1_2 = g^{00}\mathbb 1_2$; $(i\sigma^2)^2 = i^2(\sigma^2)^2 = -\mathbb 1_2 = g^{11}\mathbb 1_2$; $\sigma^1(i\sigma^2) + (i\sigma^2)\sigma^1 = i(\sigma^1\sigma^2 + \sigma^2\sigma^1) = i(i\sigma^3 - i\sigma^3) = 0$. So for $p = (p^0, p^1)$, with $p_0 = p^0$ and $p_1 = -p^1$, $p_\mu\gamma^\mu = p^0\sigma^1 - p^1\,i\sigma^2$, and its square has four terms,
>
> $$
> (p_\mu\gamma^\mu)^2 = (p^0)^2(\sigma^1)^2 + (p^1)^2(i\sigma^2)^2 - p^0p^1\,i\bigl(\sigma^1\sigma^2 + \sigma^2\sigma^1\bigr) = \bigl((p^0)^2 - (p^1)^2\bigr)\mathbb 1_2 = p^2\,\mathbb 1_2 .
> $$
>
> In $2 + 1$ dimensions, $g = \operatorname{diag}(1, -1, -1)$, add $\gamma^2 = i\sigma^3$: $(i\sigma^3)^2 = -\mathbb 1_2$, $\{\sigma^1, i\sigma^3\} = i\{\sigma^1, \sigma^3\} = 0$, $\{i\sigma^2, i\sigma^3\} = -\{\sigma^2, \sigma^3\} = 0$. In the vector form of the second route (Derivation §C5a.0.3, second route) these are $\mathbf a^0 = (1, 0, 0)$, $\mathbf a^1 = (0, i, 0)$, $\mathbf a^2 = (0, 0, i)$, with $\mathbf a^\mu\cdot\mathbf a^\mu = 1, -1, -1$ and mutually orthogonal. A fourth vector orthogonal to all three would be $0$, so the third space direction of $3 + 1$ dimensions forces $4\times4$.
>
> *Source: PS §3.2, pp. 40–41 (three-dimensional Euclidean space, $\gamma^j = i\sigma^j$, $\{\gamma^i, \gamma^j\} = -2\delta^{ij}$) · the user's pre-course notes, §5.1 ("one can set $\gamma^i = i\sigma^i$, but no fourth $2\times2$ matrix anticommutes with all three") · the $1+1$ and $2+1$ matrices written here*

^ex-c5a-0-1

> [!example] Example §C5a.0.2: Carrying Out the Square in the Chiral Basis
> In the chiral basis ([[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-11|Def. §C5a.1.11]]) the square $(p_\mu\gamma^\mu)^2 = p^2\,\mathbb 1_4$ of Theorem §C5a.0.1, 2 can be computed directly. With $\sigma^\mu$, $\bar\sigma^\mu$ of [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-10|Def. §C5a.1.10]], write $p\cdot\sigma \equiv p_\mu\sigma^\mu = p^0\mathbb 1_2 - \mathbf p\cdot\boldsymbol\sigma$ and $p\cdot\bar\sigma \equiv p_\mu\bar\sigma^\mu = p^0\mathbb 1_2 + \mathbf p\cdot\boldsymbol\sigma$ (for any $p$, not only on shell as in [[§C5a.9 Plane-Wave Solutions#^def-c5a-9-2|Def. §C5a.9.2]]).
>
> *Computation.*
> 1. Block form: $p_\mu\gamma^\mu = \begin{pmatrix}0 & p\cdot\sigma\\ p\cdot\bar\sigma & 0\end{pmatrix}$.
> 2. Block product: $(p_\mu\gamma^\mu)^2 = \begin{pmatrix}0\cdot0 + (p\cdot\sigma)(p\cdot\bar\sigma) & 0\cdot(p\cdot\sigma) + (p\cdot\sigma)\cdot0\\ (p\cdot\bar\sigma)\cdot0 + 0\cdot(p\cdot\bar\sigma) & (p\cdot\bar\sigma)(p\cdot\sigma) + 0\cdot0\end{pmatrix} = \operatorname{diag}\bigl((p\cdot\sigma)(p\cdot\bar\sigma),\ (p\cdot\bar\sigma)(p\cdot\sigma)\bigr)$.
> 3. Upper block, all four terms: $(p^0 - \mathbf p\cdot\boldsymbol\sigma)(p^0 + \mathbf p\cdot\boldsymbol\sigma) = (p^0)^2 + p^0\,\mathbf p\cdot\boldsymbol\sigma - p^0\,\mathbf p\cdot\boldsymbol\sigma - (\mathbf p\cdot\boldsymbol\sigma)^2 = (p^0)^2 - (\mathbf p\cdot\boldsymbol\sigma)^2$; the number $p^0$ commutes with $\boldsymbol\sigma$.
> 4. The Pauli square: $(\mathbf p\cdot\boldsymbol\sigma)^2 = \sum_{i,j}p^ip^j\sigma^i\sigma^j = \sum_{i,j}p^ip^j\bigl(\delta^{ij}\mathbb 1_2 + i\varepsilon^{ijk}\sigma^k\bigr) = |\mathbf p|^2\,\mathbb 1_2 + i\sum_k\Bigl(\sum_{i,j}\varepsilon^{ijk}p^ip^j\Bigr)\sigma^k = |\mathbf p|^2\,\mathbb 1_2$; the bracket vanishes because $\varepsilon^{ijk}$ is antisymmetric and $p^ip^j$ symmetric in $ij$ ([[§B6.1 Spin One-Half and the Pauli Matrices#^thm-b6-1-4|QM Theorem §B6.1.4]]).
> 5. So the upper block is $\bigl((p^0)^2 - |\mathbf p|^2\bigr)\mathbb 1_2 = p^2\,\mathbb 1_2$. The lower block $(p^0 + \mathbf p\cdot\boldsymbol\sigma)(p^0 - \mathbf p\cdot\boldsymbol\sigma)$ has the same four terms with the middle two in the other order: $p^2\,\mathbb 1_2$. Hence $(p_\mu\gamma^\mu)^2 = p^2\,\mathbb 1_4$.
>
> Neither block alone is a square: $(p\cdot\sigma)^2 = (p^0)^2 + |\mathbf p|^2 - 2p^0\,\mathbf p\cdot\boldsymbol\sigma \ne p^2\mathbb 1_2$. It is the product of $p\cdot\sigma$ with its partner $p\cdot\bar\sigma$ that gives $p^2$, which is the pair identity of [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-9|Theorem §C5a.1.9]], part 2; for all ten index pairs at once see [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-10|Theorem §C5a.1.10]].
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.1 (Derivation "Checking the Dirac algebra in the chiral basis"), §8.10 (Definition "The four-component Pauli matrices"), §8.11 ("in momentum space $(\gamma\cdot p)^2 = p^2\mathbb 1$, checked numerically") · PS §3.2, eq. (3.42) · the momentum-space computation written here*

^ex-c5a-0-2

## Two components and the mass

> [!theorem] Theorem §C5a.0.4: Two Components Suffice Only without Mass
> Let $\psi_L, \psi_R, \chi : \mathbb R^4 \to \mathbb C^2$ be $C^2$, and $\sigma^\mu$, $\bar\sigma^\mu$ as in [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-10|Def. §C5a.1.10]].
> 1. *Massless.* If $i\bar\sigma^\mu\partial_\mu\psi_L = 0$ (the Weyl equation, [[§C5a.7 The Dirac Equation and Its Lagrangian#^mod-c5a-7-11|Model §C5a.7.11]]), then $\partial^2\psi_L = 0$; likewise $i\sigma^\mu\partial_\mu\psi_R = 0$ implies $\partial^2\psi_R = 0$.
> 2. *Massive pair.* If $i\bar\sigma^\mu\partial_\mu\psi_L = m\psi_R$ and $i\sigma^\mu\partial_\mu\psi_R = m\psi_L$ (the Dirac equation in chiral blocks, [[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-10|Theorem §C5a.7.10]]), then $(\partial^2 + m^2)\psi_L = 0$ and $(\partial^2 + m^2)\psi_R = 0$.
> 3. *No massive single field.* Let $m > 0$, and let $A^\mu$, $B^\mu$, $C$ be constant $2\times2$ matrices with $(iB^\nu\partial_\nu + C)(iA^\mu\partial_\mu - m)\chi = -(\partial^2 + m^2)\chi$ for every $\chi$. Then $C = m\mathbb 1_2$ and $B^\mu = A^\mu$, so the $A^\mu$ would satisfy the Clifford relation, which no $2\times2$ matrices do ([[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation#^thm-c5a-0-3|Theorem §C5a.0.3]]). For $m = 0$ the factor $B^\mu = \sigma^\mu$, different from $A^\mu = \bar\sigma^\mu$, works (part 1).
>
> *Source: PS §3.2, pp. 43–44, eqs. (3.39)–(3.44) ("The two Lorentz group representations $\psi_L$ and $\psi_R$ are mixed by the mass term", p. 44) · Yu §5.3, eqs. (5.113)–(5.115) · the user's PHY 513 notes, Ch. 8 §8.10 (Derivation "The Dirac equation in two-component form"; Principle "The Weyl equations") · parts 1–2 as squares, and part 3, written here*

^thm-c5a-0-4

> [!derivation]- Derivation
> **1. The pair identity as an operator.** Expand $(i\sigma^\nu\partial_\nu)(i\bar\sigma^\mu\partial_\mu) = i^2\sigma^\nu\bar\sigma^\mu\partial_\nu\partial_\mu = -\sigma^\nu\bar\sigma^\mu\partial_\nu\partial_\mu$. On $C^2$ functions $\partial_\nu\partial_\mu$ is symmetric, so as in step 2 of Derivation §C5a.0.1 only the symmetric part survives: $-\frac12\bigl(\sigma^\nu\bar\sigma^\mu + \sigma^\mu\bar\sigma^\nu\bigr)\partial_\nu\partial_\mu = -g^{\nu\mu}\partial_\nu\partial_\mu\,\mathbb 1_2 = -\partial^2$, by $\sigma^\mu\bar\sigma^\nu + \sigma^\nu\bar\sigma^\mu = 2g^{\mu\nu}\mathbb 1_2$ ([[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-9|Theorem §C5a.1.9]], part 2). In the same way, with the second identity of that part, $(i\bar\sigma^\nu\partial_\nu)(i\sigma^\mu\partial_\mu) = -\partial^2$.
>
> **2. Part 1.** Apply $i\sigma^\nu\partial_\nu$ to $0 = i\bar\sigma^\mu\partial_\mu\psi_L$: by step 1, $0 = -\partial^2\psi_L$. For $\psi_R$ apply $i\bar\sigma^\nu\partial_\nu$ to $0 = i\sigma^\mu\partial_\mu\psi_R$.
>
> **3. Part 2.** Apply $i\sigma^\nu\partial_\nu$ to the first equation. The left side is $-\partial^2\psi_L$ (step 1); the right side is $m\,i\sigma^\nu\partial_\nu\psi_R = m\cdot m\psi_L$ by the second equation. So $-\partial^2\psi_L = m^2\psi_L$, i.e. $(\partial^2 + m^2)\psi_L = 0$. Apply $i\bar\sigma^\nu\partial_\nu$ to the second equation: $-\partial^2\psi_R = m\,i\bar\sigma^\nu\partial_\nu\psi_L = m^2\psi_R$. Each half needs the other: the equation for $\psi_L$ closes only through $\psi_R$.
>
> **4. Part 3: expand.** The four terms of the product, with constant $A$, $B$, $C$:
>
> $$
> (iB^\nu\partial_\nu)(iA^\mu\partial_\mu) = -B^\nu A^\mu\partial_\nu\partial_\mu, \quad (iB^\nu\partial_\nu)(-m) = -imB^\nu\partial_\nu, \quad C(iA^\mu\partial_\mu) = iCA^\mu\partial_\mu, \quad C(-m) = -mC .
> $$
>
> **5. Part 3: plane waves.** Apply both sides to $\chi = w\,e^{-ip\cdot x}$ ($w \in \mathbb C^2$, $p \in \mathbb R^4$), with $\partial_\mu \to -ip_\mu$: the four terms give $B^\nu A^\mu p_\nu p_\mu$, $-mB^\nu p_\nu$, $CA^\mu p_\mu$ and $-mC$, and the right side gives $-(-p^2 + m^2) = p^2 - m^2$. Since $w$ is arbitrary, for every $p$
>
> $$
> B^\nu A^\mu p_\nu p_\mu + \bigl(CA^\mu - mB^\mu\bigr)p_\mu - mC = \bigl(p^2 - m^2\bigr)\mathbb 1_2 .
> $$
>
> **6. Part 3: compare powers.** Replace $p$ by $tp$, $t \in \mathbb R$: both sides are polynomials in $t$ of degree at most two, equal for all $t$, so their coefficients agree. Order $t^0$: $-mC = -m^2\mathbb 1_2$, so $C = m\mathbb 1_2$ (here $m > 0$ is used). Order $t^1$: $(mA^\mu - mB^\mu)p_\mu = 0$ for every $p$, so $B^\mu = A^\mu$. Order $t^2$: $A^\nu A^\mu p_\nu p_\mu = p^2\mathbb 1_2$, i.e. $(p_\mu A^\mu)^2 = p^2\mathbb 1_2$ for every $p$, which by Theorem §C5a.0.1 (2 ⇒ 3) is the Clifford relation for the $2\times2$ matrices $A^\mu$. Theorem §C5a.0.3 (second route) excludes it. ⚑ By-product: the mass forces the second factor to be the first with the sign of $m$ flipped → part 3 of the statement.
>
> **7. Part 3 for m = 0.** Orders $t^0$ and $t^1$ now say only $CA^\mu = 0$, which $C = 0$ satisfies, and order $t^2$ asks $\frac12(B^\nu A^\mu + B^\mu A^\nu) = g^{\nu\mu}\mathbb 1_2$, a condition on the *pair* $(B, A)$. Theorem §C5a.1.9, part 2, says $(B, A) = (\sigma, \bar\sigma)$ satisfies it: this is step 1.
>
> **What the derivation shows**
> - Without mass, a two-component field has a first-order square root of $\partial^2$, because the second factor may use different matrices ($\sigma$ after $\bar\sigma$). With mass, the second factor must repeat the first, and the first would then need four anticommuting $2\times2$ matrices. The massive equation therefore needs a second two-component field, coupled through $m$: the pair of part 2, which is the Dirac equation with $\psi = (\psi_L, \psi_R)$, four components.
> - Assumptions: constant coefficients, complex-linear equations, $C^2$ fields. A Majorana mass pairs $\psi_L$ with its own complex conjugate ($\sigma^2\psi_L^{\ast}$ transforms like a right-handed spinor, PS eq. (3.38)); such an equation is not complex-linear, so part 3 does not apply to it ([[§C5a.7 The Dirac Equation and Its Lagrangian#^rem-c5a-7-7|§C5a.7, ★ Remark: A Majorana mass needs no second field]]).
> - Stacking $\sigma$ and $\bar\sigma$ off-diagonally is exactly the chiral $\gamma^\mu$ ([[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-11|Def. §C5a.1.11]]): the pair condition of step 7 for $2\times2$ blocks is the Clifford relation for $4\times4$ matrices (Example §C5a.0.2).
> - Used next: Remark "Why not two-component spinors?" below; the Weyl fields and their helicity ([[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-12|Theorem §C5a.7.12]]).

^der-c5a-0-4

*Uses:* [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-10|Def. §C5a.1.10]], [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-9|Theorem §C5a.1.9]], [[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation#^thm-c5a-0-1|Theorem §C5a.0.1]], [[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation#^thm-c5a-0-3|Theorem §C5a.0.3]], [[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-10|Theorem §C5a.7.10]], [[§C5a.7 The Dirac Equation and Its Lagrangian#^mod-c5a-7-11|Model §C5a.7.11]]

## From γ to spinor space

> [!remark] Remark: Why the Dirac maps: the logic runs from γ to spinor space
> Read in Dirac's direction, the first objects of this chapter come in a forced order. A first-order equation that squares to Klein–Gordon needs the Clifford relation (Theorem §C5a.0.1), hence coefficients that do not commute (Theorem §C5a.0.2), hence matrices, at least $4\times4$ (Theorem §C5a.0.3). Then $\gamma^\mu\partial_\mu\psi$ must make sense, so $\psi(x)$ lies in the space the $\gamma$'s act on: spinor space $V$ with its Dirac maps ([[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-1|Def. §C5a.1.1]], [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-9|Def. §C5a.1.9]]), unique up to isomorphism ([[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-14|Theorem §C5a.1.14]]). Four is what the $\gamma$'s need, not the number of states: at fixed $\mathbf p$ and fixed sign of the frequency the equation leaves a two-dimensional space of columns ([[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-2|Theorem §C5a.9.2]]), the two spin states of the rest frame ([[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-3|Theorem §C5a.9.3]]; [[§C5a.9 Plane-Wave Solutions#^rem-c5a-9-2|§C5a.9, Remark: Two of each kind, and what they will describe]]); the other sign gives the antiparticle after quantization ([[§C5b.2 Mode Expansion and the Anticommutator Algebra|§C5b.2]]).
>
> The course builds the same objects in the opposite order. PS §3.2 introduces the $\gamma$'s as "a trick due to Dirac" for writing down a representation of the Lorentz algebra (p. 40) and finds the first-order equation afterwards, "stronger" than Klein–Gordon (pp. 42–43); Lecture 7, the user's notes (Ch. 8 §8.1, the logic (i)–(v)) and §C5a.1–§C5a.7 follow PS. Dirac's own motivation was the negative probability density of the Klein–Gordon equation, which comes from its second time derivative (Yu §1.1).
>
> *Source: Yu §1.1 · PS §3.2, pp. 40–43 · the user's PHY 513 notes, Ch. 8 §8.1 · PHY 513 Lecture 8, Part C ("Klein-Gordon is necessary but not sufficient")*

^rem-c5a-0-1

> [!remark] ★ Remark: The Clifford algebra is the algebra of square roots of p²
> **The algebra.** On Minkowski space $M$ ([[§C1a.5 Vectors, Tensors and Index Notation#^def-c1a-5-1|Def. §C1a.5.1]]) the metric $g$ is a symmetric bilinear form with quadratic form $q(v) = g(v, v)$ ([[§35 Bilinear Forms and Quadratic Forms#^ladr-9-9|LADR Def. 9.9]], [[§35 Bilinear Forms and Quadratic Forms#^ladr-9-18|LADR Def. 9.18]]). The **Clifford algebra** $\mathrm{Cl}(1,3)$ is the associative algebra with unit generated by the vectors $v \in M$, added as in $M$, subject to the single relation
>
> $$
> v\,v = g(v, v)\,1 \qquad (v \in M) :
> $$
>
> every vector is a square root of its own length squared. Replacing $v$ by $v + w$ gives $vw + wv = 2g(v, w)\,1$; on a basis $e_\mu$ of $M$, with $\gamma_\mu$ the image of $e_\mu$ and $\gamma^\mu = g^{\mu\nu}\gamma_\nu$, this is $\{\gamma^\mu, \gamma^\nu\} = 2g^{\mu\nu}$ ([[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-7|Def. §C5a.1.7]]). Dirac's requirement, a first-order factor of the Klein–Gordon operator, is exactly this relation ([[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation#^thm-c5a-0-1|Theorem §C5a.0.1]]): $\mathrm{Cl}(1,3)$ is the algebra of square roots of $p^2$ with no further relations.
>
> **Universal property.** If $A$ is an associative algebra with unit and $f : M \to A$ is linear with $f(v)^2 = g(v, v)\,1$ for all $v$, then $f$ extends uniquely to an algebra homomorphism $\mathrm{Cl}(1,3) \to A$. A choice of Dirac matrices is such an $f$, $f(p) = \slashed{p} = p_\mu\gamma^\mu$, into $A = M_4(\mathbb C)$; the Dirac maps are one into $\operatorname{End}(V)$ ([[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-9|Def. §C5a.1.9]]). Compare the tensor product, which turns bilinear maps into linear ones ([[§38 Tensor Products#^ladr-9-79|LADR Thm. 9.79]]); the construction of $\mathrm{Cl}(1,3)$ as a quotient of the tensor algebra is not in the vault. After complexification $\mathrm{Cl}(1,3)\otimes\mathbb C \cong M_4(\mathbb C)$ ([[§C5a.1 Spinor Space and the Clifford Action#^rem-c5a-1-5|§C5a.1, ★ Remark: The complexified Clifford algebra is the full matrix algebra]]).
>
> **What the relation induces.**
>
> | structure | how the relation gives it | home |
> |---|---|---|
> | spinor space | $\mathrm{Cl}(1,3)\otimes\mathbb C \cong M_4(\mathbb C)$ has one irreducible module, $\mathbb C^4$: a four-dimensional space with Dirac maps, unique up to isomorphism (Pauli) | [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-1\|Def. §C5a.1.1]], [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-6\|Theorem §C5a.1.6]], [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-14\|Theorem §C5a.1.14]] |
> | the Lorentz action | Lorentz transformations preserve $g$, so $\Lambda^\mu{}_\nu\gamma^\nu$ satisfy the relation again, and Pauli's theorem gives $\Lambda_{1/2}$ with $\Lambda_{1/2}^{-1}\gamma^\mu\Lambda_{1/2} = \Lambda^\mu{}_\nu\gamma^\nu$, unique up to a factor; near the identity it is generated by $S^{\mu\nu} = \frac i4[\gamma^\mu, \gamma^\nu]$ (the even part); the leftover sign is the double cover | [[§C5a.3 The Lorentz Action on Spinor Space#^def-c5a-3-1\|Def. §C5a.3.1]], [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-2\|Theorem §C5a.3.2]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-11\|Theorem §C5a.4.11]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-7\|Theorem §C5a.4.7]] |
> | chirality | $\gamma^5 = i\gamma^0\gamma^1\gamma^2\gamma^3$ is the volume element (the product of an orthonormal basis, normalized to square to $1$); it anticommutes with each $\gamma^\mu$, hence commutes with every $S^{\mu\nu}$, so its eigenspaces $V_L$, $V_R$ are Lorentz invariant: the Weyl halves | [[§C5a.5 Chirality and Weyl Spinors#^def-c5a-5-1\|Def. §C5a.5.1]], [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-1\|Theorem §C5a.5.1]], [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-2\|Theorem §C5a.5.2]] |
>
> **What it does not induce.** The relation involves no complex conjugation, so it says nothing about $\psi^\dagger$. The Dirac form $h_D(\chi, \psi) = \chi^\dagger\gamma^0\psi$ is an added structure, a Hermitian form on $V$ ([[§C5a.2 The Dirac Form#^def-c5a-2-4|Def. §C5a.2.4]]); requiring the Dirac maps to be self-adjoint for it fixes it up to a real factor ([[§C5a.2 The Dirac Form#^thm-c5a-2-2|Theorem §C5a.2.2]]). It gives the Dirac conjugate $\bar\psi$ ([[§C5a.2 The Dirac Form#^def-c5a-2-5|Def. §C5a.2.5]]), the real bilinears ([[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-5|Theorem §C5a.6.5]]) and a Lagrangian that is real up to a divergence ([[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-7|Theorem §C5a.7.7]]). In a basis the same fact appears as Hermiticity, $\gamma^{\mu\dagger} = \gamma^0\gamma^\mu\gamma^0$, a choice of basis and not a consequence of the algebra ([[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-11|Theorem §C5a.1.11]]).
>
> *Source: written here, on the concrete content of Theorem §C5a.0.1; no course source states the Clifford algebra of a quadratic form or its universal property, and the vault has no Math home for Clifford algebras · the relation: PS §3.2, eq. (3.22) and p. 43; the user's PHY 513 notes, Ch. 8 §8.1 · the rows: the homes linked in the table*

^rem-c5a-0-2

## What the γ's are for

> [!remark] Remark: Four jobs of the γ's
> Once the $\gamma$'s exist they do four different jobs, and every later use of a $\gamma$ is one of them.
>
> | job | formula | home |
> |---|---|---|
> | (i) square root of Klein–Gordon | $(\gamma\cdot p)^2 = p^2$; $(-i\slashed{\partial} - m)(i\slashed{\partial} - m) = \partial^2 + m^2$ | [[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation#^thm-c5a-0-1\|Theorem §C5a.0.1]], [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-5\|Theorem §C5a.1.5]], [[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-8\|Theorem §C5a.7.8]] |
> | (ii) build the Lorentz action on spinors | $S^{\mu\nu} = \frac i4[\gamma^\mu, \gamma^\nu]$ obey the Lorentz algebra by the Clifford relation alone; $\Lambda_{1/2} = \exp(-\frac i2\omega_{\mu\nu}S^{\mu\nu})$; the half angle and the sign of a $2\pi$ rotation come from these generators | [[§C5a.3 The Lorentz Action on Spinor Space#^def-c5a-3-1\|Def. §C5a.3.1]], [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-2\|Theorem §C5a.3.2]], [[§C5a.3 The Lorentz Action on Spinor Space#^def-c5a-3-2\|Def. §C5a.3.2]], [[§C5a.3 The Lorentz Action on Spinor Space#^rem-c5a-3-1\|§C5a.3, Remark: Why half the angle]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-7\|Theorem §C5a.4.7]] |
> | (iii) turn pairs of spinors into tensors | $\Lambda_{1/2}^{-1}\gamma^\mu\Lambda_{1/2} = \Lambda^\mu{}_\nu\gamma^\nu$: each $\gamma$ between $\bar\psi$ and $\psi$ carries one vector index | [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-11\|Theorem §C5a.4.11]], [[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-3\|Theorem §C5a.6.3]], [[§C5a.6 The Dirac Conjugate and the Bilinears#^def-c5a-6-2\|Def. §C5a.6.2]] |
> | — scalar | $\bar\psi\psi$, the mass term | [[§C5a.7 The Dirac Equation and Its Lagrangian#^mod-c5a-7-3\|Model §C5a.7.3]] |
> | — vector | $\bar\psi\gamma^\mu\psi$; $\bar\psi\gamma^0\psi = \psi^\dagger\psi$ is the charge density | [[§C5a.8 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-8-3\|Theorem §C5a.8.3]] |
> | — antisymmetric tensor | $\bar\psi\sigma^{\mu\nu}\psi$; the magnetic moment, through the Gordon identity | [[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-9\|Theorem §C5a.11.9]], [[§C5a.11 Gamma-Matrix Technology#^rem-c5a-11-2\|§C5a.11, Remark: What the Gordon identity says]] |
> | — axial vector, pseudoscalar | $\bar\psi\gamma^\mu\gamma^5\psi$, $\bar\psi i\gamma^5\psi$ | [[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-4\|Theorem §C5a.6.4]], [[§C5a.8 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-8-4\|Theorem §C5a.8.4]] |
> | — even the conjugate | $\bar\psi = \psi^\dagger\gamma^0$ needs a $\gamma$, because $\psi^\dagger\psi$ is not invariant | [[§C5a.2 The Dirac Form#^def-c5a-2-5\|Def. §C5a.2.5]], [[§C5a.6 The Dirac Conjugate and the Bilinears#^rem-c5a-6-1\|§C5a.6, Remark: Why ψ†ψ is not a scalar]] |
> | (iv) dynamics and computation | $H_{\text{s.p.}} = \gamma^0(-i\boldsymbol\gamma\cdot\nabla + m)$ and $\hat H = \int d^3x\,\hat\psi^\dagger H_{\text{s.p.}}\hat\psi$ | [[§C5a.7 The Dirac Equation and Its Lagrangian#^def-c5a-7-3\|Def. §C5a.7.3]], [[§C5b.1 Canonical Quantization of the Dirac Field#^mod-c5b-1-2\|Model §C5b.1.2]], [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-5\|Theorem §C5b.3.5]] |
> | — spin sums and traces | $\sum_su^s\bar u^s = \slashed{p} + m$, $\sum_sv^s\bar v^s = \slashed{p} - m$; traces of products of $\gamma$'s | [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-7\|Theorem §C5a.10.7]], [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-8\|Theorem §C5a.10.8]], [[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-3\|Theorem §C5a.11.3]] |
> | — chirality projectors | $P_{L,R} = \frac12(1 \mp \gamma^5)$ | [[§C5a.5 Chirality and Weyl Spinors#^def-c5a-5-2\|Def. §C5a.5.2]] |
> | — the QED coupling | $-e\bar\psi\gamma^\mu\psi A_\mu$: every vertex carries a $\gamma^\mu$ | QFT C8 (planned) |
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.1 (Definition "The spinor generators"; Derivation "Proof of the claim (Problem Set 4, Problem 5)"), §8.6 (Principle "What the covariance argument proves": "sandwiching $\gamma^\mu$ between spinor matrices performs a vector Lorentz transformation on its index"), §8.9 (Fermion bilinears: "the structure of a magnetic-moment interaction"), Ch. 9 §9.6 (paragraph "What the Gordon identity says"), Ch. 10 §10.5 · PHY 513 Lecture 7, Part B; Lecture 8, Part A (slides "'Transformation' of $\gamma^\mu$") and Part B ("Fermion Bilinears"); Lecture 9, Part B (completeness); Lecture 10 (slide "The (Single-Particle) Hamiltonian") · PS §3.2, eqs. (3.23), (3.29)–(3.30), (3.32); §3.4, pp. 49–50 · the grouping into four jobs written here*

^rem-c5a-0-3

> [!remark] Remark: Why not two-component spinors?
> - **Without mass, two components suffice.** The Weyl equation $i\bar\sigma^\mu\partial_\mu\psi_L = 0$ squares to $\partial^2\psi_L = 0$, because the second factor may use the partner matrices $\sigma^\mu$ ([[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation#^thm-c5a-0-4|Theorem §C5a.0.4]], 1; [[§C5a.7 The Dirac Equation and Its Lagrangian#^mod-c5a-7-11|Model §C5a.7.11]]).
> - **With mass, they do not.** A massive first-order equation for one two-component field cannot square to Klein–Gordon (Theorem §C5a.0.4, 3). The Dirac pair closes only through the partner, $\psi_L$ through $\psi_R$ and back (Theorem §C5a.0.4, 2); in the Lagrangian the kinetic terms keep the chiralities apart and the mass term $-m(\psi_L^\dagger\psi_R + \psi_R^\dagger\psi_L)$ joins them ([[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-9|Theorem §C5a.7.9]]; [[§C5a.5 Chirality and Weyl Spinors#^rem-c5a-5-2|§C5a.5, Remark: Kinematics allows one handedness, a mass needs both]]). The exception is a Majorana mass ([[§C5a.7 The Dirac Equation and Its Lagrangian#^rem-c5a-7-7|§C5a.7, ★ Remark: A Majorana mass needs no second field]]).
> - **Parity exchanges the two.** The parity map $\mathbf J \mapsto \mathbf J$, $\mathbf K \mapsto -\mathbf K$ exchanges $\mathbf J_+ \leftrightarrow \mathbf J_-$, so it carries $(\frac12, 0)$ to $(0, \frac12)$, and a space with a parity operator contains both with equal multiplicity ([[§CB.15 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-15-9|Theorem §CB.15.9]]). How parity acts on Dirac spinors, by the block swap $\gamma^0$, is derived in [[§C9.3 Parity on States, Spinors and the Dirac Field#^thm-c9-3-3|Theorem §C9.3.3]] and [[§C9.3 Parity on States, Spinors and the Dirac Field#^def-c9-3-2|Def. §C9.3.2]].
>
> So a fermion with a Dirac mass, in a theory that respects parity, needs both chiralities, $(\frac12, 0)\oplus(0, \frac12)$ ([[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-4|Theorem §C5a.3.4]]); the four-component formalism packages them as $\psi = (\psi_L, \psi_R)$, with $\gamma$'s that map each half to the other.
>
> *Source: PS §3.2, p. 44 ("The two Lorentz group representations $\psi_L$ and $\psi_R$ are mixed by the mass term in the Dirac equation") · the user's PHY 513 notes, Ch. 7 §7.4.6 (paragraph "Parity and conjugation exchange the two copies"), Ch. 8 §8.10 (figure: "the equation of motion couples them, through the mass and only through it") · PHY 513 Lecture 7, Part B ("Mass couples ξ and η") · Yu §5.3, eqs. (5.113)–(5.115)*

^rem-c5a-0-4

## The chapter map

> [!remark] Remark: The structure of spinor space, layer by layer
> Layer 0 is the square root of $p^2$: the motivation of this section, which makes the $\gamma$'s and spinor space necessary. Each later layer adds one structure to the previous ones and is used by everything after it.
>
> | layer | structure on $V$ | what it gives | where |
> |---|---|---|---|
> | 0 | none yet: the requirement that a first-order equation square to the Klein–Gordon operator | the Clifford relation $(\gamma\cdot p)^2 = p^2$, hence anticommuting matrices and a space for them to act on | [[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation#^thm-c5a-0-1\|Theorem §C5a.0.1]]–[[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation#^thm-c5a-0-4\|§C5a.0.4]] |
> | 1 | a four-dimensional complex vector space, its bases and change-of-basis matrices $U$ | components $\psi_a$, matrices, the rules $\psi \to U\psi$, $M \to UMU^{-1}$ | [[§C5a.1 Spinor Space and the Clifford Action\|§C5a.1]] |
> | 2 | the Clifford action: maps $\Gamma^\mu$ with $\{\Gamma^\mu, \Gamma^\nu\} = 2g^{\mu\nu}$ | Dirac matrices, the chiral basis, Pauli's theorem: one spinor space up to isomorphism | [[§C5a.1 Spinor Space and the Clifford Action\|§C5a.1]] |
> | 3 | the Dirac form $h_D(\chi, \psi) = \chi^\dagger\gamma^0\psi$, signature $(2, 2)$ | the Dirac conjugate $\bar\psi$; which changes of basis are allowed (unitary) | [[§C5a.2 The Dirac Form\|§C5a.2]] |
> | 4 | the Lorentz algebra acting through $S^{\mu\nu} = \frac i4[\Gamma^\mu, \Gamma^\nu]$ | the Dirac representation, a **spinor representation**, $(\frac12, 0)\oplus(0, \frac12)$ | [[§C5a.3 The Lorentz Action on Spinor Space\|§C5a.3]] |
> | 5 | the group: $SL(2, \mathbb C)$ acting on $V$ by $\Lambda_{1/2}$, together with $SO^+(1,3)$ on spacetime | Weyl matrices, the double cover, $\gamma^\mu$ as an invariant tensor | [[§C5a.4 SL(2,C) and the Group Action on Spinor Space\|§C5a.4]] |
> | 6 | the chirality grading by $\Gamma^5$: $V = V_L\oplus V_R$ | Weyl spinors, spinor indices, choosing a basis | [[§C5a.5 Chirality and Weyl Spinors\|§C5a.5]] |
> | 7 | the Dirac form under the Lorentz group | $\bar\psi\chi$ invariant, the sixteen bilinears | [[§C5a.6 The Dirac Conjugate and the Bilinears\|§C5a.6]] |
> | 8 | fields $\psi : M \to V$ | the Dirac equation and Lagrangian, canonical structure, plane waves, spin sums | [[§C5a.7 The Dirac Equation and Its Lagrangian\|§C5a.7]]–[[§C5a.10 Normalization, Spin Sums and Helicity\|§C5a.10]] |
>
> The $\gamma$-matrix identities used in amplitudes are collected in [[§C5a.11 Gamma-Matrix Technology|§C5a.11]]. The lectures take the same route in a different grouping: Lecture 7, Part B gives the Dirac algebra, the generators and $\Lambda_{1/2}$ (layers 2, 4, 5) and the halves under rotations and boosts (layer 6); Lecture 8, Part A the covariance of $\gamma^\mu$ (layer 5) and the Dirac equation, Part B the conjugate and the Lagrangian (layers 3, 7, 8), Part C the Weyl equations (layers 6, 8); $\gamma^5$ came with Problem Set 5. Layer 1 and the basis-change material are written here; the order follows Peskin–Schroeder §3.2.
>
> *Source: PS §3.2, pp. 40–44 (the order) · PHY 513 Lectures 7–8 (the lecture route) · the user's PHY 513 notes, Ch. 8 §8.1 (the logic (i)–(v) of the section) · the layered organization written here*

^rem-c5a-0-5

> [!remark]- Connections
> - Theorem §C5a.0.1 and Dirac ⇒ Klein–Gordon are the two directions of one equivalence: the Clifford relation is exactly the condition for a first-order factor of the Klein–Gordon operator — [[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation#^thm-c5a-0-1|Theorem §C5a.0.1]], [[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-8|Theorem §C5a.7.8]].
> - Relativistic quantum mechanics runs the same forcing argument for a four-component wave function, compressed and with $\hbar$, $c$; this section is its field-theory home, with the equivalence to $(\gamma\cdot p)^2 = p^2$, the non-commutativity step, the direct $2\times2$ count and the massless/massive contrast added — [[§C13.2★ The Dirac Equation#^thm-c13-2-2|QM Theorem §C13.2.2]], [[§C13.2★ The Dirac Equation#^rem-c13-2-1|QM, Remark: The square root of the Klein–Gordon operator]].
> - Pauli's $(\boldsymbol\sigma\cdot\mathbf p)^2 = |\mathbf p|^2$ is the square root in three Euclidean dimensions; adding a time direction costs nothing in $2\times2$ (Example §C5a.0.1), adding the third space direction forces $4\times4$ — [[§B6.1 Spin One-Half and the Pauli Matrices#^thm-b6-1-4|QM Theorem §B6.1.4]], [[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation#^ex-c5a-0-1|Example §C5a.0.1]].
> - The dimension bounds rest on one mechanism, that anticommuting matrices are linearly independent: four $\gamma$'s in the three-dimensional span of the Pauli matrices, or sixteen products in $M_n(\mathbb C)$ — [[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation#^der-c5a-0-3b|Derivation §C5a.0.3 (second route)]], [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-6|Theorem §C5a.1.6]], [[§4 Span and Linear Independence#^ladr-2-22|LADR Thm. 2.22]].
> - The massless two-component square root pairs $\sigma$ with $\bar\sigma$; stacked into one $4\times4$ matrix the pair becomes the chiral $\gamma^\mu$, and the massless solutions have fixed helicity — [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-10|Theorem §C5a.1.10]], [[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-12|Theorem §C5a.7.12]].
> - The same squaring, run on the Green's function, makes the Dirac propagator $(i\slashed{\partial} + m)$ times the scalar one — [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-3|Theorem §C5b.8.3]].
