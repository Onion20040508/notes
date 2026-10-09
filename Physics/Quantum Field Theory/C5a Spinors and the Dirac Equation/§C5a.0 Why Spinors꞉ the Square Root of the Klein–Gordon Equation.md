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

Why does a spin-$\frac12$ field need four components and a set of anticommuting matrices? Dirac asked for a relativistic wave equation of first order whose square is the Klein–Gordon operator ([[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^mod-c1b-2-6|Model §C1b.2.6]]). This section derives what that requirement forces: the Clifford relation (Theorem §C5a.0.1), coefficients that cannot commute (Theorem §C5a.0.2), matrices of even size at least four (Theorem §C5a.0.3), and two components only when there is no mass (Theorem §C5a.0.4). It then lists what the $\gamma$'s are used for and maps the chapter. The structures themselves are built in §C5a.1–§C5a.7 and, as mathematics, in CB: the Clifford relation, its modules and their dimension are [[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules|§CB.10]]–[[§CB.12 Complex Clifford Algebras and Clifford Modules|§CB.12]], shown below where this section uses them; nothing is proved twice. The converse direction, from the Clifford relation to the Klein–Gordon equation, is [[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-8|Theorem §C5a.7.8]]; in relativistic quantum mechanics the same argument is [[§C13.2★ The Dirac Equation#^thm-c13-2-2|QM Theorem §C13.2.2]].

*Conventions* ([[Larsen PHY 513]]): natural units; $g = \operatorname{diag}(+,-,-,-)$, $\partial^2 = g^{\mu\nu}\partial_\mu\partial_\nu$, $p^2 = g^{\mu\nu}p_\mu p_\nu$; repeated Greek indices are summed unless "no sum" is written; $\mathbb 1_n$ is the $n\times n$ identity; $\psi$ is a classical field (no hat).

## The mathematics used here

Theorem §C5a.0.1 derives the defining relation of the Dirac matrices, and in the form of Theorem §CB.10.10: a Clifford module is a set of anticommuting square roots, which is the equivalence of its parts 2 and 3:

![[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^def-cb-10-11]]

![[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^thm-cb-10-10]]

![[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^pf-cb-10-10]]

Step 6 of its derivation reads off the squares and the anticommutation as the first consequences of the relation:

![[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^thm-cb-10-12]]

![[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^der-cb-10-12]]

## The requirement and the Clifford relation

> [!theorem] Theorem §C5a.0.1: Squaring a First-Order Equation
> Let $\gamma^0, \dots, \gamma^3$ be constant complex $n\times n$ matrices and $m \ge 0$. The following are equivalent:
> 1. $i\gamma^\mu\partial_\mu - m$ is a factor of the Klein–Gordon operator ([[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^mod-c1b-2-6|Model §C1b.2.6]]): $(-i\gamma^\nu\partial_\nu - m)(i\gamma^\mu\partial_\mu - m)\psi = (\partial^2 + m^2)\psi$ for every $C^2$ function $\psi : \mathbb R^4 \to \mathbb C^n$;
> 2. $(p_\mu\gamma^\mu)^2 = p^2\,\mathbb 1_n$ for every $p \in \mathbb R^4$;
> 3. the Clifford relation $\{\gamma^\mu, \gamma^\nu\} = 2g^{\mu\nu}\,\mathbb 1_n$ ([[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^def-cb-10-11|Def. §CB.10.11]]); in components, $(\gamma^0)^2 = \mathbb 1_n$, $(\gamma^i)^2 = -\mathbb 1_n$ and $\gamma^\mu\gamma^\nu = -\gamma^\nu\gamma^\mu$ for $\mu \ne \nu$.
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
> **6. Components.** For $\mu = \nu$: $2(\gamma^\mu)^2 = 2g^{\mu\mu}\mathbb 1_n$ (no sum), so $(\gamma^0)^2 = \mathbb 1_n$ and $(\gamma^i)^2 = -\mathbb 1_n$. For $\mu \ne \nu$: $g^{\mu\nu} = 0$, so $\gamma^\mu\gamma^\nu + \gamma^\nu\gamma^\mu = 0$. (These are part 1 of [[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^thm-cb-10-12|Theorem §CB.10.12]], there read off the relation in the same way.)
>
> **What the derivation shows**
> - The Clifford relation is not an additional postulate: it is the requirement "a first-order square root of the Klein–Gordon operator" written as an identity among the coefficients. [[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-8|Theorem §C5a.7.8]] is the direction (3) ⇒ every solution solves Klein–Gordon.
> - Assumptions used: constant coefficients; $C^2$ fields (for $\partial_\mu\partial_\nu = \partial_\nu\partial_\mu$); the coefficient of $m$ normalized to $\mathbb 1_n$. An invertible coefficient $M$, $(i\gamma^\mu\partial_\mu - mM)\psi = 0$, is removed by multiplying with $M^{-1}$, which replaces $\gamma^\mu$ by $M^{-1}\gamma^\mu$.
> - The requirement is an identity of operators, as in Dirac, PS and Yu: the first-order operator must be a factor. This section does not use the weaker-looking demand that only the solutions satisfy Klein–Gordon.
> - Condition 2 is the precise form of "$p_\mu\gamma^\mu$ is a square root of $p^2$" ([[§C5a.1 Spinor Space and the Clifford Action#^rem-c5a-1-2|§C5a.1, Remark: A square root of p²]]).
> - Used next: what the relation forces on the $\gamma$'s (Theorems §C5a.0.2–§C5a.0.3); the two-component case (Theorem §C5a.0.4).

^der-c5a-0-1

*Uses:* [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^mod-c1b-2-6|Model §C1b.2.6]], [[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^def-cb-10-11|Def. §CB.10.11]], [[§C5a.7 The Dirac Equation and Its Lagrangian#^der-c5a-7-8|Derivation §C5a.7.8]]

### The mathematics used here: why matrices, and why four by four

Theorem §C5a.0.2 rests on the fact that Clifford generators in any unital algebra are invertible and never commute, so that no basis diagonalizes them all:

![[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^thm-cb-10-15]]

![[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^der-cb-10-15]]

Theorem §C5a.0.3 takes the size bound from the matrix form of the theorem on irreducible modules, proved by traces, with a direct route for $2\times2$ matrices; the bound uses the sixteen products:

![[§CB.11 Clifford Algebras꞉ Grading, Basis and the Volume Element#^thm-cb-11-8]]

![[§CB.11 Clifford Algebras꞉ Grading, Basis and the Volume Element#^der-cb-11-8]]

![[§CB.12 Complex Clifford Algebras and Clifford Modules#^thm-cb-12-9]]

![[§CB.12 Complex Clifford Algebras and Clifford Modules#^der-cb-12-9]]

![[§CB.12 Complex Clifford Algebras and Clifford Modules#^der-cb-12-9b]]

With fewer $\gamma$'s, two components suffice (the contrast drawn in Theorem §C5a.0.4 and the Connections):

![[§CB.11 Clifford Algebras꞉ Grading, Basis and the Volume Element#^ex-cb-11-18]]

The $4\times4$ solution is unique up to a change of basis (used next, in §C5a.1):

![[§CB.12 Complex Clifford Algebras and Clifford Modules#^thm-cb-12-12]]

![[§CB.12 Complex Clifford Algebras and Clifford Modules#^der-cb-12-12]]

## Why matrices, and why four by four

> [!theorem] Theorem §C5a.0.2: The Coefficients Cannot Commute
> Let $\gamma^0, \dots, \gamma^3$ satisfy the Clifford relation ([[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation#^thm-c5a-0-1|Theorem §C5a.0.1]], 3). They are invertible and no two of them commute ([[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^thm-cb-10-15|Theorem §CB.10.15]], 1–2). Hence the $\gamma$'s cannot be numbers: a one-component field has no first-order equation that squares to Klein–Gordon. And no basis makes all four $n\times n$ Dirac matrices diagonal at once (Theorem §CB.10.15, 3).
>
> *Source: PS §3.2, p. 41 ("There is no fourth $2\times2$ matrix … that anticommutes with the three Pauli sigma matrices", the matrix version) · the user's PHY 513 notes, Ch. 8 §8.1 ("Square to ±1, or square root?") · the argument written here*

^thm-c5a-0-2

> [!derivation]- Derivation
> **1. Numbers.** Complex numbers commute, so by Theorem §CB.10.15, 2 no four (indeed no two) complex numbers satisfy the relation: for $n = 1$ condition 3 of Theorem §C5a.0.1 has no solution, and therefore neither has condition 1.
>
> **What the derivation shows**
> - So $\psi$ has more than one component, and the $\gamma$'s mix the components: this is where spinor components come from. The same argument (Derivation §CB.10.15, steps 2–4) shows that $\gamma^0$ and $\gamma^5$ are never diagonal together ([[§CB.11 Clifford Algebras꞉ Grading, Basis and the Volume Element#^thm-cb-11-15|Theorem §CB.11.15]]).
> - Used next: the size of the matrices (Theorem §C5a.0.3).

^der-c5a-0-2

*Uses:* [[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation#^thm-c5a-0-1|Theorem §C5a.0.1]], [[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^thm-cb-10-15|Theorem §CB.10.15]]

> [!theorem] Theorem §C5a.0.3: The Smallest Coefficients Are 4×4 Matrices
> Let $\gamma^0, \dots, \gamma^3$ be complex $n\times n$ matrices satisfying the Clifford relation ([[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation#^thm-c5a-0-1|Theorem §C5a.0.1]], 3). Then $n$ is even and $n \ge 4$ ([[§CB.12 Complex Clifford Algebras and Clifford Modules#^thm-cb-12-9|Theorem §CB.12.9]]), and $n = 4$ occurs: the chiral matrices ([[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-3|Def. §C5a.1.3]]) satisfy the relation ([[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-2|Theorem §C5a.1.2]]).
>
> So the smallest first-order square root of the Klein–Gordon operator acts on columns $\psi \in \mathbb C^4$.
>
> *Source: PS §3.2, p. 41 ("these matrices must be at least 4 × 4") · the user's PHY 513 notes, Ch. 8 §8.1 ("four is the smallest dimension in which (clifford) can be solved") · the user's pre-course notes, §5.1 ("Since at most $N^2$ matrices of size $N\times N$ are independent, $N \ge 4$") · the evenness and the direct $2\times2$ argument written out here*

^thm-c5a-0-3

> [!derivation]- Derivation
> **1. Four occurs.** [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-2|Theorem §C5a.1.2]] checks all ten conditions of the relation for the chiral matrices; Example §C5a.0.1 below carries out the square $(p_\mu\gamma^\mu)^2$ for them.
>
> **What the derivation shows**
> - Only the relation was used, so the bounds hold for every first-order square root of the Klein–Gordon operator (Theorem §C5a.0.1); their proof is Theorem §CB.12.9, with a second route for $n = 2$ by expanding in Pauli matrices.
> - Used next: spinor space as the space the $\gamma$'s act on ([[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-1|Def. §C5a.1.1]]); its uniqueness is Pauli's theorem ([[§CB.12 Complex Clifford Algebras and Clifford Modules#^thm-cb-12-12|Theorem §CB.12.12]]).

^der-c5a-0-3

*Uses:* [[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation#^thm-c5a-0-1|Theorem §C5a.0.1]], [[§CB.12 Complex Clifford Algebras and Clifford Modules#^thm-cb-12-9|Theorem §CB.12.9]], [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-2|Theorem §C5a.1.2]]

> [!example] Example §C5a.0.1: Carrying Out the Square in the Chiral Basis
> In the chiral basis ([[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-3|Def. §C5a.1.3]]) the square $(p_\mu\gamma^\mu)^2 = p^2\,\mathbb 1_4$ of Theorem §C5a.0.1, 2 can be computed directly. With $\sigma^\mu$, $\bar\sigma^\mu$ of [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-2|Def. §C5a.1.2]], write $p\cdot\sigma \equiv p_\mu\sigma^\mu = p^0\mathbb 1_2 - \mathbf p\cdot\boldsymbol\sigma$ and $p\cdot\bar\sigma \equiv p_\mu\bar\sigma^\mu = p^0\mathbb 1_2 + \mathbf p\cdot\boldsymbol\sigma$ (for any $p$, not only on shell as in [[§C5a.9 Plane-Wave Solutions#^def-c5a-9-2|Def. §C5a.9.2]]).
>
> *Computation.*
> 1. Block form: $p_\mu\gamma^\mu = \begin{pmatrix}0 & p\cdot\sigma\\ p\cdot\bar\sigma & 0\end{pmatrix}$.
> 2. Block product: $(p_\mu\gamma^\mu)^2 = \begin{pmatrix}0\cdot0 + (p\cdot\sigma)(p\cdot\bar\sigma) & 0\cdot(p\cdot\sigma) + (p\cdot\sigma)\cdot0\\ (p\cdot\bar\sigma)\cdot0 + 0\cdot(p\cdot\bar\sigma) & (p\cdot\bar\sigma)(p\cdot\sigma) + 0\cdot0\end{pmatrix} = \operatorname{diag}\bigl((p\cdot\sigma)(p\cdot\bar\sigma),\ (p\cdot\bar\sigma)(p\cdot\sigma)\bigr)$.
> 3. Upper block, all four terms: $(p^0 - \mathbf p\cdot\boldsymbol\sigma)(p^0 + \mathbf p\cdot\boldsymbol\sigma) = (p^0)^2 + p^0\,\mathbf p\cdot\boldsymbol\sigma - p^0\,\mathbf p\cdot\boldsymbol\sigma - (\mathbf p\cdot\boldsymbol\sigma)^2 = (p^0)^2 - (\mathbf p\cdot\boldsymbol\sigma)^2$; the number $p^0$ commutes with $\boldsymbol\sigma$.
> 4. The Pauli square: $(\mathbf p\cdot\boldsymbol\sigma)^2 = \sum_{i,j}p^ip^j\sigma^i\sigma^j = \sum_{i,j}p^ip^j\bigl(\delta^{ij}\mathbb 1_2 + i\varepsilon^{ijk}\sigma^k\bigr) = |\mathbf p|^2\,\mathbb 1_2 + i\sum_k\Bigl(\sum_{i,j}\varepsilon^{ijk}p^ip^j\Bigr)\sigma^k = |\mathbf p|^2\,\mathbb 1_2$; the bracket vanishes because $\varepsilon^{ijk}$ is antisymmetric and $p^ip^j$ symmetric in $ij$ ([[§B6.1 Spin One-Half and the Pauli Matrices#^thm-b6-1-4|QM Theorem §B6.1.4]]).
> 5. So the upper block is $\bigl((p^0)^2 - |\mathbf p|^2\bigr)\mathbb 1_2 = p^2\,\mathbb 1_2$. The lower block $(p^0 + \mathbf p\cdot\boldsymbol\sigma)(p^0 - \mathbf p\cdot\boldsymbol\sigma)$ has the same four terms with the middle two in the other order: $p^2\,\mathbb 1_2$. Hence $(p_\mu\gamma^\mu)^2 = p^2\,\mathbb 1_4$.
>
> Neither block alone is a square: $(p\cdot\sigma)^2 = (p^0)^2 + |\mathbf p|^2 - 2p^0\,\mathbf p\cdot\boldsymbol\sigma \ne p^2\mathbb 1_2$. It is the product of $p\cdot\sigma$ with its partner $p\cdot\bar\sigma$ that gives $p^2$, which is the pair identity of [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-1|Theorem §C5a.1.1]], part 2; for all ten index pairs at once see [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-2|Theorem §C5a.1.2]].
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.1 (Derivation "Checking the Dirac algebra in the chiral basis"), §8.10 (Definition "The four-component Pauli matrices"), §8.11 ("in momentum space $(\gamma\cdot p)^2 = p^2\mathbb 1$, checked numerically") · PS §3.2, eq. (3.42) · the momentum-space computation written here*

^ex-c5a-0-1

## Two components and the mass

> [!theorem] Theorem §C5a.0.4: Two Components Suffice Only without Mass
> Let $\psi_L, \psi_R, \chi : \mathbb R^4 \to \mathbb C^2$ be $C^2$, and $\sigma^\mu$, $\bar\sigma^\mu$ as in [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-2|Def. §C5a.1.2]].
> 1. *Massless.* If $i\bar\sigma^\mu\partial_\mu\psi_L = 0$ (the Weyl equation, [[§C5a.7 The Dirac Equation and Its Lagrangian#^mod-c5a-7-11|Model §C5a.7.11]]), then $\partial^2\psi_L = 0$; likewise $i\sigma^\mu\partial_\mu\psi_R = 0$ implies $\partial^2\psi_R = 0$.
> 2. *Massive pair.* If $i\bar\sigma^\mu\partial_\mu\psi_L = m\psi_R$ and $i\sigma^\mu\partial_\mu\psi_R = m\psi_L$ (the Dirac equation in chiral blocks, [[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-10|Theorem §C5a.7.10]]), then $(\partial^2 + m^2)\psi_L = 0$ and $(\partial^2 + m^2)\psi_R = 0$.
> 3. *No massive single field.* Let $m > 0$, and let $A^\mu$, $B^\mu$, $C$ be constant $2\times2$ matrices with $(iB^\nu\partial_\nu + C)(iA^\mu\partial_\mu - m)\chi = -(\partial^2 + m^2)\chi$ for every $\chi$. Then $C = m\mathbb 1_2$ and $B^\mu = A^\mu$, so the $A^\mu$ would satisfy the Clifford relation, which no $2\times2$ matrices do ([[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation#^thm-c5a-0-3|Theorem §C5a.0.3]]). For $m = 0$ the factor $B^\mu = \sigma^\mu$, different from $A^\mu = \bar\sigma^\mu$, works (part 1).
>
> *Source: PS §3.2, pp. 43–44, eqs. (3.39)–(3.44) ("The two Lorentz group representations $\psi_L$ and $\psi_R$ are mixed by the mass term", p. 44) · Yu §5.3, eqs. (5.113)–(5.115) · the user's PHY 513 notes, Ch. 8 §8.10 (Derivation "The Dirac equation in two-component form"; Principle "The Weyl equations") · parts 1–2 as squares, and part 3, written here*

^thm-c5a-0-4

> [!derivation]- Derivation
> **1. The pair identity as an operator.** Expand $(i\sigma^\nu\partial_\nu)(i\bar\sigma^\mu\partial_\mu) = i^2\sigma^\nu\bar\sigma^\mu\partial_\nu\partial_\mu = -\sigma^\nu\bar\sigma^\mu\partial_\nu\partial_\mu$. On $C^2$ functions $\partial_\nu\partial_\mu$ is symmetric, so as in step 2 of Derivation §C5a.0.1 only the symmetric part survives: $-\frac12\bigl(\sigma^\nu\bar\sigma^\mu + \sigma^\mu\bar\sigma^\nu\bigr)\partial_\nu\partial_\mu = -g^{\nu\mu}\partial_\nu\partial_\mu\,\mathbb 1_2 = -\partial^2$, by $\sigma^\mu\bar\sigma^\nu + \sigma^\nu\bar\sigma^\mu = 2g^{\mu\nu}\mathbb 1_2$ ([[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-1|Theorem §C5a.1.1]], part 2). In the same way, with the second identity of that part, $(i\bar\sigma^\nu\partial_\nu)(i\sigma^\mu\partial_\mu) = -\partial^2$.
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
> **6. Part 3: compare powers.** Replace $p$ by $tp$, $t \in \mathbb R$: both sides are polynomials in $t$ of degree at most two, equal for all $t$, so their coefficients agree. Order $t^0$: $-mC = -m^2\mathbb 1_2$, so $C = m\mathbb 1_2$ (here $m > 0$ is used). Order $t^1$: $(mA^\mu - mB^\mu)p_\mu = 0$ for every $p$, so $B^\mu = A^\mu$. Order $t^2$: $A^\nu A^\mu p_\nu p_\mu = p^2\mathbb 1_2$, i.e. $(p_\mu A^\mu)^2 = p^2\mathbb 1_2$ for every $p$, which by Theorem §C5a.0.1 (2 ⇒ 3) is the Clifford relation for the $2\times2$ matrices $A^\mu$. Theorem §CB.12.9 (second route, for $2\times2$ matrices) excludes it. ⚑ By-product: the mass forces the second factor to be the first with the sign of $m$ flipped → part 3 of the statement.
>
> **7. Part 3 for m = 0.** Orders $t^0$ and $t^1$ now say only $CA^\mu = 0$, which $C = 0$ satisfies, and order $t^2$ asks $\frac12(B^\nu A^\mu + B^\mu A^\nu) = g^{\nu\mu}\mathbb 1_2$, a condition on the *pair* $(B, A)$. Theorem §C5a.1.1, part 2, says $(B, A) = (\sigma, \bar\sigma)$ satisfies it: this is step 1.
>
> **What the derivation shows**
> - Without mass, a two-component field has a first-order square root of $\partial^2$, because the second factor may use different matrices ($\sigma$ after $\bar\sigma$). With mass, the second factor must repeat the first, and the first would then need four anticommuting $2\times2$ matrices. The massive equation therefore needs a second two-component field, coupled through $m$: the pair of part 2, which is the Dirac equation with $\psi = (\psi_L, \psi_R)$, four components.
> - Assumptions: constant coefficients, complex-linear equations, $C^2$ fields. A Majorana mass pairs $\psi_L$ with its own complex conjugate ($\sigma^2\psi_L^{\ast}$ transforms like a right-handed spinor, PS eq. (3.38)); such an equation is not complex-linear, so part 3 does not apply to it ([[§C5a.7 The Dirac Equation and Its Lagrangian#^rem-c5a-7-7|§C5a.7, ★ Remark: A Majorana mass needs no second field]]).
> - Stacking $\sigma$ and $\bar\sigma$ off-diagonally is exactly the chiral $\gamma^\mu$ ([[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-3|Def. §C5a.1.3]]): the pair condition of step 7 for $2\times2$ blocks is the Clifford relation for $4\times4$ matrices (Example §C5a.0.1).
> - Used next: Remark "Why not two-component spinors?" below; the Weyl fields and their helicity ([[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-12|Theorem §C5a.7.12]]).

^der-c5a-0-4

*Uses:* [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-2|Def. §C5a.1.2]], [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-1|Theorem §C5a.1.1]], [[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation#^thm-c5a-0-1|Theorem §C5a.0.1]], [[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation#^thm-c5a-0-3|Theorem §C5a.0.3]], [[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-10|Theorem §C5a.7.10]], [[§C5a.7 The Dirac Equation and Its Lagrangian#^mod-c5a-7-11|Model §C5a.7.11]]

### The mathematics used here: from γ to spinor space

The remarks below need the basis-free form of the Clifford action, the Dirac maps on one spinor space, and its uniqueness:

![[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^def-cb-10-13]]

![[§CB.12 Complex Clifford Algebras and Clifford Modules#^thm-cb-12-14]]

![[§CB.12 Complex Clifford Algebras and Clifford Modules#^der-cb-12-14]]

The ★ remark "What the Clifford relation induces" starts from the algebra the relation generates:

![[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^rem-cb-10-1]]

## From γ to spinor space

> [!remark] Remark: Why the Dirac maps: the logic runs from γ to spinor space
> Read in Dirac's direction, the first objects of this chapter come in a forced order. A first-order equation that squares to Klein–Gordon needs the Clifford relation (Theorem §C5a.0.1), hence coefficients that do not commute (Theorem §C5a.0.2), hence matrices, at least $4\times4$ (Theorem §C5a.0.3). Then $\gamma^\mu\partial_\mu\psi$ must make sense, so $\psi(x)$ lies in the space the $\gamma$'s act on: spinor space $V$ with its Dirac maps ([[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-1|Def. §C5a.1.1]], [[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^def-cb-10-13|Def. §CB.10.13]]), unique up to isomorphism ([[§CB.12 Complex Clifford Algebras and Clifford Modules#^thm-cb-12-14|Theorem §CB.12.14]]). Four is what the $\gamma$'s need, not the number of states: at fixed $\mathbf p$ and fixed sign of the frequency the equation leaves a two-dimensional space of columns ([[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-2|Theorem §C5a.9.2]]), the two spin states of the rest frame ([[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-3|Theorem §C5a.9.3]]; [[§C5a.9 Plane-Wave Solutions#^rem-c5a-9-2|§C5a.9, Remark: Two of each kind, and what they will describe]]); the other sign gives the antiparticle after quantization ([[§C5b.2 Mode Expansion and the Anticommutator Algebra|§C5b.2]]).
>
> The course builds the same objects in the opposite order. PS §3.2 introduces the $\gamma$'s as "a trick due to Dirac" for writing down a representation of the Lorentz algebra (p. 40) and finds the first-order equation afterwards, "stronger" than Klein–Gordon (pp. 42–43); Lecture 7, the user's notes (Ch. 8 §8.1, the logic (i)–(v)) and §C5a.1–§C5a.7 follow PS. Dirac's own motivation was the negative probability density of the Klein–Gordon equation, which comes from its second time derivative (Yu §1.1).
>
> *Source: Yu §1.1 · PS §3.2, pp. 40–43 · the user's PHY 513 notes, Ch. 8 §8.1 · PHY 513 Lecture 8, Part C ("Klein-Gordon is necessary but not sufficient")*

^rem-c5a-0-1

> [!remark] ★ Remark: What the Clifford relation induces
> **The algebra.** The relation $\{\gamma^\mu, \gamma^\nu\} = 2g^{\mu\nu}$ generates the Clifford algebra $\mathrm{Cl}(1,3)$, the algebra of square roots of $p^2$ with no further relations, and a choice of Dirac matrices or Dirac maps is a homomorphism out of it ([[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^rem-cb-10-1|§CB.10, ★ Remark: The Clifford algebra is the algebra of square roots of p²]]; in general [[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^def-cb-10-6|Def. §CB.10.6]], [[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^thm-cb-10-7|Theorem §CB.10.7]]).
>
> **What the relation induces.**
>
> | structure | how the relation gives it | home |
> |---|---|---|
> | spinor space | $\mathrm{Cl}(1,3)\otimes\mathbb C \cong M_4(\mathbb C)$ has one irreducible module, $\mathbb C^4$: a four-dimensional space with Dirac maps, unique up to isomorphism (Pauli) | [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-1\|Def. §C5a.1.1]], [[§CB.11 Clifford Algebras꞉ Grading, Basis and the Volume Element#^thm-cb-11-8\|Theorem §CB.11.8]], [[§CB.12 Complex Clifford Algebras and Clifford Modules#^thm-cb-12-14\|Theorem §CB.12.14]] |
> | the Lorentz action | Lorentz transformations preserve $g$, so $\Lambda^\mu{}_\nu\gamma^\nu$ satisfy the relation again, and Pauli's theorem gives $\Lambda_{1/2}$ with $\Lambda_{1/2}^{-1}\gamma^\mu\Lambda_{1/2} = \Lambda^\mu{}_\nu\gamma^\nu$, unique up to a factor; near the identity it is generated by $S^{\mu\nu} = \frac i4[\gamma^\mu, \gamma^\nu]$ (the even part); the leftover sign is the double cover | [[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-13-15\|Def. §CB.13.15]], [[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-13-17\|Theorem §CB.13.17]], [[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-17-7\|Theorem §CB.17.7]], [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-7\|Theorem §CB.15.7]] |
> | chirality | $\gamma^5 = i\gamma^0\gamma^1\gamma^2\gamma^3$ is the volume element (the product of an orthonormal basis, normalized to square to $1$); it anticommutes with each $\gamma^\mu$, hence commutes with every $S^{\mu\nu}$, so its eigenspaces $V_L$, $V_R$ are Lorentz invariant: the Weyl halves | [[§CB.11 Clifford Algebras꞉ Grading, Basis and the Volume Element#^def-cb-11-13\|Def. §CB.11.13]], [[§CB.11 Clifford Algebras꞉ Grading, Basis and the Volume Element#^thm-cb-11-14\|Theorem §CB.11.14]], [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-1\|Theorem §C5a.5.1]] |
>
> **What it does not induce.** The relation involves no complex conjugation, so it says nothing about $\psi^\dagger$. The Dirac form $h_D(\chi, \psi) = \chi^\dagger\gamma^0\psi$ is an added structure, a Hermitian form on $V$ ([[§CB.12 Complex Clifford Algebras and Clifford Modules#^def-cb-12-15|Def. §CB.12.15]]); requiring the Dirac maps to be self-adjoint for it fixes it up to a real factor ([[§CB.12 Complex Clifford Algebras and Clifford Modules#^thm-cb-12-16|Theorem §CB.12.16]]). It gives the Dirac conjugate $\bar\psi$ ([[§C5a.2 The Dirac Form#^def-c5a-2-1|Def. §C5a.2.1]]), the real bilinears ([[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-4|Theorem §C5a.6.4]]) and a Lagrangian that is real up to a divergence ([[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-7|Theorem §C5a.7.7]]). In a basis the same fact appears as Hermiticity, $\gamma^{\mu\dagger} = \gamma^0\gamma^\mu\gamma^0$, a choice of basis and not a consequence of the algebra ([[§C5a.2 The Dirac Form#^thm-c5a-2-1|Theorem §C5a.2.1]]).
>
> *Source: written here, on the concrete content of Theorem §C5a.0.1; no course source states the Clifford algebra of a quadratic form or its universal property, and the vault has no Math home for Clifford algebras · the relation: PS §3.2, eq. (3.22) and p. 43; the user's PHY 513 notes, Ch. 8 §8.1 · the rows: the homes linked in the table*

^rem-c5a-0-2

### The mathematics used here: parity

The remark "Why not two-component spinors?" uses that parity exchanges the two copies of the Lorentz algebra:

![[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-10]]

![[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^der-cb-16-10]]

## What the γ's are for

> [!remark] Remark: Four jobs of the γ's
> Once the $\gamma$'s exist they do four different jobs, and every later use of a $\gamma$ is one of them.
>
> | job | formula | home |
> |---|---|---|
> | (i) square root of Klein–Gordon | $(\gamma\cdot p)^2 = p^2$; $(-i\slashed{\partial} - m)(i\slashed{\partial} - m) = \partial^2 + m^2$ | [[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation#^thm-c5a-0-1\|Theorem §C5a.0.1]], [[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^thm-cb-10-12\|Theorem §CB.10.12]], [[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-8\|Theorem §C5a.7.8]] |
> | (ii) build the Lorentz action on spinors | $S^{\mu\nu} = \frac i4[\gamma^\mu, \gamma^\nu]$ obey the Lorentz algebra by the Clifford relation alone; $\Lambda_{1/2} = \exp(-\frac i2\omega_{\mu\nu}S^{\mu\nu})$; the half angle and the sign of a $2\pi$ rotation come from these generators | [[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-13-15\|Def. §CB.13.15]], [[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-13-17\|Theorem §CB.13.17]], [[§C5a.3 The Lorentz Action on Spinor Space#^def-c5a-3-1\|Def. §C5a.3.1]], [[§C5a.3 The Lorentz Action on Spinor Space#^rem-c5a-3-1\|§C5a.3, Remark: Why half the angle]], [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-7\|Theorem §CB.15.7]] |
> | (iii) turn pairs of spinors into tensors | $\Lambda_{1/2}^{-1}\gamma^\mu\Lambda_{1/2} = \Lambda^\mu{}_\nu\gamma^\nu$: each $\gamma$ between $\bar\psi$ and $\psi$ carries one vector index | [[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-17-7\|Theorem §CB.17.7]], [[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-2\|Theorem §C5a.6.2]], [[§C5a.6 The Dirac Conjugate and the Bilinears#^def-c5a-6-2\|Def. §C5a.6.2]] |
> | — scalar | $\bar\psi\psi$, the mass term | [[§C5a.7 The Dirac Equation and Its Lagrangian#^mod-c5a-7-3\|Model §C5a.7.3]] |
> | — vector | $\bar\psi\gamma^\mu\psi$; $\bar\psi\gamma^0\psi = \psi^\dagger\psi$ is the charge density | [[§C5a.8 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-8-3\|Theorem §C5a.8.3]] |
> | — antisymmetric tensor | $\bar\psi\sigma^{\mu\nu}\psi$; the magnetic moment, through the Gordon identity | [[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-9\|Theorem §C5a.11.9]], [[§C5a.11 Gamma-Matrix Technology#^rem-c5a-11-2\|§C5a.11, Remark: What the Gordon identity says]] |
> | — axial vector, pseudoscalar | $\bar\psi\gamma^\mu\gamma^5\psi$, $\bar\psi i\gamma^5\psi$ | [[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-3\|Theorem §C5a.6.3]], [[§C5a.8 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-8-4\|Theorem §C5a.8.4]] |
> | — even the conjugate | $\bar\psi = \psi^\dagger\gamma^0$ needs a $\gamma$, because $\psi^\dagger\psi$ is not invariant | [[§C5a.2 The Dirac Form#^def-c5a-2-1\|Def. §C5a.2.1]], [[§C5a.6 The Dirac Conjugate and the Bilinears#^rem-c5a-6-1\|§C5a.6, Remark: Why ψ†ψ is not a scalar]] |
> | (iv) dynamics and computation | $H_{\text{s.p.}} = \gamma^0(-i\boldsymbol\gamma\cdot\nabla + m)$ and $\hat H = \int d^3x\,\hat\psi^\dagger H_{\text{s.p.}}\hat\psi$ | [[§C5a.7 The Dirac Equation and Its Lagrangian#^def-c5a-7-3\|Def. §C5a.7.3]], [[§C5b.1 Canonical Quantization of the Dirac Field#^mod-c5b-1-2\|Model §C5b.1.2]], [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-5\|Theorem §C5b.3.5]] |
> | — spin sums and traces | $\sum_su^s\bar u^s = \slashed{p} + m$, $\sum_sv^s\bar v^s = \slashed{p} - m$; traces of products of $\gamma$'s | [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-7\|Theorem §C5a.10.7]], [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-8\|Theorem §C5a.10.8]], [[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-3\|Theorem §C5a.11.3]] |
> | — chirality projectors | $P_{L,R} = \frac12(1 \mp \gamma^5)$ | [[§C5a.5 Chirality and Weyl Spinors#^def-c5a-5-1\|Def. §C5a.5.1]] |
> | — the QED coupling | $-e\bar\psi\gamma^\mu\psi A_\mu$: every vertex carries a $\gamma^\mu$ | QFT C8 (planned) |
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.1 (Definition "The spinor generators"; Derivation "Proof of the claim (Problem Set 4, Problem 5)"), §8.6 (Principle "What the covariance argument proves": "sandwiching $\gamma^\mu$ between spinor matrices performs a vector Lorentz transformation on its index"), §8.9 (Fermion bilinears: "the structure of a magnetic-moment interaction"), Ch. 9 §9.6 (paragraph "What the Gordon identity says"), Ch. 10 §10.5 · PHY 513 Lecture 7, Part B; Lecture 8, Part A (slides "'Transformation' of $\gamma^\mu$") and Part B ("Fermion Bilinears"); Lecture 9, Part B (completeness); Lecture 10 (slide "The (Single-Particle) Hamiltonian") · PS §3.2, eqs. (3.23), (3.29)–(3.30), (3.32); §3.4, pp. 49–50 · the grouping into four jobs written here*

^rem-c5a-0-3

> [!remark] Remark: Why not two-component spinors?
> - **Without mass, two components suffice.** The Weyl equation $i\bar\sigma^\mu\partial_\mu\psi_L = 0$ squares to $\partial^2\psi_L = 0$, because the second factor may use the partner matrices $\sigma^\mu$ ([[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation#^thm-c5a-0-4|Theorem §C5a.0.4]], 1; [[§C5a.7 The Dirac Equation and Its Lagrangian#^mod-c5a-7-11|Model §C5a.7.11]]).
> - **With mass, they do not.** A massive first-order equation for one two-component field cannot square to Klein–Gordon (Theorem §C5a.0.4, 3). The Dirac pair closes only through the partner, $\psi_L$ through $\psi_R$ and back (Theorem §C5a.0.4, 2); in the Lagrangian the kinetic terms keep the chiralities apart and the mass term $-m(\psi_L^\dagger\psi_R + \psi_R^\dagger\psi_L)$ joins them ([[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-9|Theorem §C5a.7.9]]; [[§C5a.5 Chirality and Weyl Spinors#^rem-c5a-5-2|§C5a.5, Remark: Kinematics allows one handedness, a mass needs both]]). The exception is a Majorana mass ([[§C5a.7 The Dirac Equation and Its Lagrangian#^rem-c5a-7-7|§C5a.7, ★ Remark: A Majorana mass needs no second field]]).
> - **Parity exchanges the two.** The parity map $\mathbf J \mapsto \mathbf J$, $\mathbf K \mapsto -\mathbf K$ exchanges $\mathbf J_+ \leftrightarrow \mathbf J_-$, so it carries $(\frac12, 0)$ to $(0, \frac12)$, and a space with a parity operator contains both with equal multiplicity ([[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-10|Theorem §CB.16.10]]). How parity acts on Dirac spinors, by the block swap $\gamma^0$, is derived in [[§C9.3 Parity on States, Spinors and the Dirac Field#^thm-c9-3-3|Theorem §C9.3.3]] and [[§C9.3 Parity on States, Spinors and the Dirac Field#^def-c9-3-2|Def. §C9.3.2]].
>
> So a fermion with a Dirac mass, in a theory that respects parity, needs both chiralities, $(\frac12, 0)\oplus(0, \frac12)$ ([[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-2|Theorem §C5a.3.2]]); the four-component formalism packages them as $\psi = (\psi_L, \psi_R)$, with $\gamma$'s that map each half to the other.
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
> - Pauli's $(\boldsymbol\sigma\cdot\mathbf p)^2 = |\mathbf p|^2$ is the square root in three Euclidean dimensions; adding a time direction costs nothing in $2\times2$ (Example §CB.11.18), adding the third space direction forces $4\times4$ — [[§B6.1 Spin One-Half and the Pauli Matrices#^thm-b6-1-4|QM Theorem §B6.1.4]], [[§CB.11 Clifford Algebras꞉ Grading, Basis and the Volume Element#^ex-cb-11-18|Example §CB.11.18]].
> - The dimension bounds rest on one mechanism, that anticommuting matrices are linearly independent: four $\gamma$'s in the three-dimensional span of the Pauli matrices, or sixteen products in $M_n(\mathbb C)$ — [[§CB.12 Complex Clifford Algebras and Clifford Modules#^der-cb-12-9b|Derivation §CB.12.9 (second route)]], [[§CB.11 Clifford Algebras꞉ Grading, Basis and the Volume Element#^thm-cb-11-8|Theorem §CB.11.8]], [[§4 Span and Linear Independence#^ladr-2-22|LADR Thm. 2.22]].
> - The massless two-component square root pairs $\sigma$ with $\bar\sigma$; stacked into one $4\times4$ matrix the pair becomes the chiral $\gamma^\mu$, and the massless solutions have fixed helicity — [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-2|Theorem §C5a.1.2]], [[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-12|Theorem §C5a.7.12]].
> - The same squaring, run on the Green's function, makes the Dirac propagator $(i\slashed{\partial} + m)$ times the scalar one — [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-3|Theorem §C5b.8.3]].
