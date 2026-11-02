---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C5a
section: C5a.10
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C5a.9 Canonical Structure and Noether Currents of the Dirac Field]] · ↑ [[· C5a Spinors and the Dirac Equation]] · [[§C5a.11 The Spinors u(p), v(p) and Their Dirac Conjugates]] →

*Sources: the user's PHY 513 notes, Ch. 9 §9.1 (Plane waves and an eigenvalue problem), §9.2 (The rest frame), §9.3 (Boosting to a general frame), §9.4 (Principle "Never take the square root of a 2×2 matrix" and its proof; Derivation "Check: u(p) solves the Dirac equation in every frame"), §9.4 (Derivation "Normalization II: ūu", the row ū), §9.5 (Derivation "The v spinors: the four steps again"; Derivation "Normalizations of the v's", the row v̄), §9.6 (paragraph "The Dirac equation, from both sides"), and the paragraph "Correspondence with Yu" · PHY 513 Lecture 9 (Larsen), Parts A, B ("Normalization II", "Completeness for Dirac Spinors") and C · Peskin & Schroeder, An Introduction to Quantum Field Theory, §3.3, eqs. (3.45)–(3.51), (3.55)–(3.56), (3.58)–(3.62) · Yu Zhao-Huan, 量子场论讲义, §5.4.1–§5.4.2, eqs. (5.118)–(5.157), (5.182)–(5.191), (5.205)–(5.206) · the user's pre-course notes, §5.4 ("General form of the plane-wave solutions"; "Helicity spinors in the Weyl representation"; note "Checking the spin sums") · PHY 513, Problem Set 6, Problem 3(c)–(d) and comments (Larsen; the user's solutions).*

What are the solutions of the free Dirac equation? The equation and its covariance are [[§C5a.7 The Dirac Equation and Its Lagrangian#^def-c5a-7-1|Def. §C5a.7.1]] and [[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-1|Theorem §C5a.7.1]]; every solution solves the Klein–Gordon equation component by component ([[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-8|Theorem §C5a.7.8]]), so it is built from plane waves on the mass shell, as the scalar field was ([[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-2|Theorem §C2a.2.2]]). This section carries out Lecture 9's four steps up to the boost: a plane-wave ansatz, an eigenvalue problem, the rest frame, and a boost with the spinor matrix $\Lambda_{1/2}$ ([[§C5a.3 The Lorentz Action on Spinor Space#^def-c5a-3-1|Def. §C5a.3.1]]), written through the rapidity as $\sqrt{p\cdot\sigma}$ and $\sqrt{p\cdot\bar\sigma}$. The two positive-frequency spinors $u^s(p)$ and the two negative-frequency spinors $v^s(p)$ that this boost produces, and their Dirac conjugates $\bar u^s(p)$, $\bar v^s(p)$ ([[§C5a.2 The Dirac Form#^def-c5a-2-1|Def. §C5a.2.1]]), are [[§C5a.11 The Spinors u(p), v(p) and Their Dirac Conjugates|§C5a.11]]; their normalizations and spin sums are [[§C5a.12 Normalization and Spin Sums|§C5a.12]], the helicity basis [[§C5a.13 Helicity Spinors and the Massless Limit|§C5a.13]]; the field built from them is [[§C5b.2 Mode Expansion and the Anticommutator Algebra|§C5b.2]]. The mathematics it uses — the Clifford relation, the spinor generators and the rotation content of $(\frac12, 0)\oplus(0, \frac12)$ — is shown in the blocks below ([[§CB.11 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules|§CB.11]]–[[§CB.14 The Spin Group and the Double Cover Spin(V) → SO(V)|§CB.14]], [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)|§CB.17]], [[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵|§CB.18]]).

**Setup.** Classical, free and on shell: the plane-wave solutions of the free Dirac equation ([[§C5a.7 The Dirac Equation and Its Lagrangian#^mod-c5a-7-3|Model §C5a.7.3]]), with $p^0 = +E_{\mathbf p}$; $u^s(p)$, $v^s(p)$ are c-number columns, normalized as in [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^def-c5a-10-4|Def. §C5a.10.4]] ($\bar u^ru^s = 2m\,\delta^{rs}$, $u^{r\dagger}u^s = 2E_{\mathbf p}\delta^{rs}$). Rest-frame statements need $m > 0$; the formulas for $u$, $v$ and their conjugates hold for every $m \ge 0$. The boosts and square roots (Theorems §C5a.10.5–§C5a.10.8) are matrix statements, exact. The quantum field uses these same spinors as its mode functions ([[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-1|Theorem §C5b.2.1]]).

*Conventions* ([[Larsen PHY 513]]): chiral basis $\gamma^\mu = \begin{pmatrix}0 & \sigma^\mu\\ \bar\sigma^\mu & 0\end{pmatrix}$ ([[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-4|Def. §C5a.1.4]]) with $\sigma^\mu = (\mathbb 1, \boldsymbol\sigma)$, $\bar\sigma^\mu = (\mathbb 1, -\boldsymbol\sigma)$ ([[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-3|Def. §C5a.1.3]]); $p^0 = E_{\mathbf p} = +\sqrt{\mathbf p^2 + m^2}$ always; $\slashed{p} \equiv \gamma^\mu p_\mu$ ([[§C5a.7 The Dirac Equation and Its Lagrangian#^def-c5a-7-2|Def. §C5a.7.2]]); $\Lambda_{1/2} = \exp(-\frac i2\omega_{\mu\nu}S^{\mu\nu})$, read actively, the boost to rapidity $\eta$ along $+z$ having $\omega_{03} = -\omega_{30} = \eta$ ([[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-3|Theorem §C1a.6.3]]). Two-spinors are $\xi$, $\eta^s$ (with an index); the rapidity is $\eta$ (never with an index).

## The mathematics used here

Plane waves turn the Dirac equation into the eigenvalue problem of $\slashed{p}$, whose square is $p^2$ by the Clifford relation; Theorem §C5a.10.2 also uses $\gamma^5$:

![[§CB.11 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^def-cb-11-11]]

![[§CB.11 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^thm-cb-11-12]]

![[§CB.11 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^der-cb-11-12]]

![[§CB.12 Clifford Algebras꞉ Grading, Basis and the Volume Element#^thm-cb-12-15]]

![[§CB.12 Clifford Algebras꞉ Grading, Basis and the Volume Element#^der-cb-12-15]]

## Plane waves and an eigenvalue problem

> [!definition] Definition §C5a.10.1: Positive- and Negative-Frequency Solutions
> For $\mathbf p \in \mathbb R^3$ let $p^\mu = (E_{\mathbf p}, \mathbf p)$ with $E_{\mathbf p} = +\sqrt{\mathbf p^2 + m^2}$. A **positive-frequency plane wave** is $\psi(x) = u(p)\,e^{-ip\cdot x}$ and a **negative-frequency plane wave** is $\psi(x) = v(p)\,e^{+ip\cdot x}$, with $u(p), v(p) \in \mathbb C^4$ constant columns. In both, $p^0 = +E_{\mathbf p}$: "negative frequency" refers to the sign in the exponent, $e^{+ip\cdot x} = e^{+iE_{\mathbf p}t - i\mathbf p\cdot\mathbf x}$, never to the sign of $p^0$.
>
> *Model:* [[§C5a.7 The Dirac Equation and Its Lagrangian#^mod-c5a-7-3|Model §C5a.7.3]]; *applies:* classical plane waves, on shell $p^0 = +E_{\mathbf p}$, every $m \ge 0$; the mode functions of the quantum field ([[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-1|Theorem §C5b.2.1]]).
>
> *Source: the user's PHY 513 notes, Ch. 9 §9.1 (Principle "Positive and negative frequency: the sign is in the exponent") · PHY 513 Lecture 9, Part A, Step 1 ("Convention: always $p^0 = +\sqrt{\vec p^2 + m^2}$") and Part C · PS §3.3, eqs. (3.58), (3.61)*

^def-c5a-10-1

> [!remark] Remark: Why the sign sits in the exponent, not in p⁰
> The Klein–Gordon equation allows $e^{-ik\cdot x}$ with $k^0 = \pm E_{\mathbf k}$. The root $k^0 = -E_{\mathbf k}$ gives $e^{+iE_{\mathbf k}t + i\mathbf k\cdot\mathbf x}$, which is $e^{+ip\cdot x}$ with $p = (E_{\mathbf k}, -\mathbf k)$: the same function, relabelled by $\mathbf p = -\mathbf k$. Keeping both roots *and* both exponents would count every solution twice. The course keeps $p^0 > 0$ and puts the sign in the exponent (PS: "rather than having $p^0 < 0$"); Yu first writes the negative-energy eigenvectors $w^{(-)}(-E_{\mathbf k}, \mathbf k)$ and then makes exactly this relabelling, $v(\mathbf k) \equiv w^{(-)}(-E_{\mathbf k}, -\mathbf k)$ (5.134)–(5.137). The same relabelling turned $\tilde a_{\mathbf k}$ into $a^\dagger_{\mathbf p}$ for the scalar field ([[§C2a.2 Mode Expansion and the Mode Algebra#^der-c2a-2-2|Derivation §C2a.2.2, step 3]]), and it is the reason why, in [[§C5a.12 Normalization and Spin Sums|§C5a.12]], $u^r(p)$ is orthogonal to $v^s(\tilde p)$, $\tilde p = (E_{\mathbf p}, -\mathbf p)$, rather than to $v^s(p)$.
>
> *Source: the user's PHY 513 notes, Ch. 9 §9.1 · PS §3.3, p. 48 · Yu §5.4.1, eqs. (5.128)–(5.138)*

^rem-c5a-10-1

> [!theorem] Theorem §C5a.10.1: Plane Waves Turn the Dirac Equation into Algebra
> With $p^0 = E_{\mathbf p}$,
> 1. $u(p)\,e^{-ip\cdot x}$ solves the Dirac equation $(i\slashed{\partial} - m)\psi = 0$ ([[§C5a.7 The Dirac Equation and Its Lagrangian#^def-c5a-7-1|Def. §C5a.7.1]]) iff $(\slashed{p} - m)\,u(p) = 0$, i.e. $u(p)$ is an eigenvector of the $4\times4$ matrix $\slashed{p}$ ([[§C5a.7 The Dirac Equation and Its Lagrangian#^def-c5a-7-2|Def. §C5a.7.2]]) with eigenvalue $+m$;
> 2. $v(p)\,e^{+ip\cdot x}$ solves it iff $(\slashed{p} + m)\,v(p) = 0$, i.e. $v(p)$ is an eigenvector of $\slashed{p}$ with eigenvalue $-m$.
>
> *Model:* [[§C5a.7 The Dirac Equation and Its Lagrangian#^mod-c5a-7-3|Model §C5a.7.3]]; *applies:* classical plane waves, $p^0 = E_{\mathbf p}$, every $m \ge 0$, exact.
>
> *Source: the user's PHY 513 notes, Ch. 9 §9.1 (Derivation "Step 1: the Dirac equation becomes algebraic"), §9.5 (Steps 1–2) · PHY 513 Lecture 9, Part A, Step 2; Part C, Step 2 · PS §3.3, eq. (3.46) · Yu §5.4.2, eqs. (5.144)–(5.145), (5.183)–(5.184)*

^thm-c5a-10-1

> [!derivation]- Derivation
> **Step 1** (derivative of a plane wave). With $p\cdot x = p_\mu x^\mu$ and $\partial_\mu x^\nu = \delta_\mu{}^\nu$, $\partial_\mu(p\cdot x) = p_\mu$, so $\partial_\mu e^{\mp ip\cdot x} = \mp ip_\mu\,e^{\mp ip\cdot x}$. The column $u(p)$ is constant and passes through $\partial_\mu$.
>
> **Step 2** (positive frequency). $i\gamma^\mu\partial_\mu\bigl(u\,e^{-ip\cdot x}\bigr) = i\gamma^\mu(-ip_\mu)\,u\,e^{-ip\cdot x} = (-i^2)\gamma^\mu p_\mu u\,e^{-ip\cdot x} = \slashed{p}\,u\,e^{-ip\cdot x}$, since $-i^2 = +1$. Hence
>
> $$
> (i\slashed{\partial} - m)\bigl(u\,e^{-ip\cdot x}\bigr) = e^{-ip\cdot x}\,(\slashed{p} - m)\,u .
> $$
>
> **Step 3** (cancel the exponential). $e^{-ip\cdot x}$ is a nonzero number at every $x$, so the left side vanishes for all $x$ iff $(\slashed{p} - m)u = 0$. This is $\slashed{p}\,u = m\,u$: an eigenvalue equation, four linear equations for four unknowns with no derivatives left. Part 1.
>
> **Step 4** (negative frequency). Now $\partial_\mu e^{+ip\cdot x} = +ip_\mu e^{+ip\cdot x}$, and $i\gamma^\mu(+ip_\mu) = i^2\slashed{p} = -\slashed{p}$:
>
> $$
> (i\slashed{\partial} - m)\bigl(v\,e^{+ip\cdot x}\bigr) = e^{+ip\cdot x}\,(-\slashed{p} - m)\,v ,
> $$
>
> which vanishes for all $x$ iff $(\slashed{p} + m)v = 0$, i.e. $\slashed{p}\,v = -m\,v$. Part 2. ⚑ By-product: the sign of the eigenvalue came from the exponent, not from $p^0$, which is $+E_{\mathbf p}$ in both cases → [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^rem-c5a-10-1|Remark: Why the sign sits in the exponent]].
>
> **What the derivation shows**
> - A plane wave turns the differential operator into the matrix $\pm\slashed{p}$: the field equation in momentum space ([[§CA.3 Fourier Transforms and Fourier Tricks#^rem-ca-3-1|§CA.3, Remark: A linear equation becomes algebra]]).
> - $p^2 = m^2$ was not used: it is forced by the next theorem (a nonzero solution needs $\pm m$ to be an eigenvalue of $\slashed{p}$, and $\slashed{p}^2 = p^2$).
> - Used next: the eigenvalues of $\slashed{p}$ ([[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^thm-c5a-10-2|Theorem §C5a.10.2]]).

^der-c5a-10-1

*Uses:* [[§C5a.7 The Dirac Equation and Its Lagrangian#^def-c5a-7-1|Def. §C5a.7.1]], [[§C5a.7 The Dirac Equation and Its Lagrangian#^def-c5a-7-2|Def. §C5a.7.2]]

> [!definition] Definition §C5a.10.2: The Matrices p·σ and p·σ̄
> For a four-vector $p$, $p\cdot\sigma \equiv p_\mu\sigma^\mu$ and $p\cdot\bar\sigma \equiv p_\mu\bar\sigma^\mu$; lowering the index of $p$ supplies the sign of the spatial part:
>
> $$
> p\cdot\sigma = E_{\mathbf p} - \mathbf p\cdot\boldsymbol\sigma, \qquad p\cdot\bar\sigma = E_{\mathbf p} + \mathbf p\cdot\boldsymbol\sigma, \qquad \slashed{p} = \begin{pmatrix}0 & p\cdot\sigma\\ p\cdot\bar\sigma & 0\end{pmatrix} .
> $$
>
> Both are Hermitian $2\times2$ matrices, with eigenvalues $E_{\mathbf p} \mp |\mathbf p|$ (for $p\cdot\sigma$) and $E_{\mathbf p} \pm |\mathbf p|$ (for $p\cdot\bar\sigma$) on the eigenvectors of $\hat{\mathbf p}\cdot\boldsymbol\sigma$ with eigenvalue $\pm1$.
>
> *Source: the user's PHY 513 notes, Ch. 9 §9.3 (Derivation "Rapidity in terms of the momentum"), §9.4 (Definition "Feynman slash": chiral form of $\slashed{p}$) · PHY 513 Lecture 9, Part A ("Interpretation of Rapidity") · PS §3.3, eq. (3.50) · Yu §5.4.2, eqs. (5.148), (5.166)–(5.167)*

^def-c5a-10-2

The chiral form of $\slashed{p}$ is $\gamma^\mu = \begin{pmatrix}0 & \sigma^\mu\\ \bar\sigma^\mu & 0\end{pmatrix}$ contracted with $p_\mu$ block by block; with $p_\mu = (E_{\mathbf p}, -\mathbf p)$, $p_\mu\sigma^\mu = E_{\mathbf p}\mathbb 1 - p^i\sigma^i$. The eigenvalues: $\mathbf p\cdot\boldsymbol\sigma = |\mathbf p|\,\hat{\mathbf p}\cdot\boldsymbol\sigma$ and $(\hat{\mathbf p}\cdot\boldsymbol\sigma)^2 = \mathbb 1$, so $\hat{\mathbf p}\cdot\boldsymbol\sigma$ has eigenvalues $\pm1$ ([[§B6.1 Spin One-Half and the Pauli Matrices#^thm-b6-1-5|QM Theorem §B6.1.5]]). For $m > 0$ all four numbers $E_{\mathbf p} \pm |\mathbf p|$ are positive; for $m = 0$, $E_{\mathbf p} - |\mathbf p| = 0$.

> [!theorem] Theorem §C5a.10.2: The Eigenvalues of p̸
> Let $p^2 = m^2$, $p^0 > 0$, and $\slashed{p}$ as in [[§C5a.7 The Dirac Equation and Its Lagrangian#^def-c5a-7-2|Def. §C5a.7.2]].
> 1. $\slashed{p}^{\,2} = p^2\,\mathbb 1 = m^2\,\mathbb 1$.
> 2. For $m > 0$, $\slashed{p}$ is diagonalizable with eigenvalues $+m$ and $-m$, each of multiplicity two: $\mathbb C^4 = \ker(\slashed{p} - m) \oplus \ker(\slashed{p} + m)$, both two-dimensional. So for each $\mathbf p$ there are exactly two independent $u(p)$ and two independent $v(p)$.
> 3. For $m = 0$ and $\mathbf p \neq 0$, $\slashed{p} \neq 0$ but $\slashed{p}^{\,2} = 0$: $\slashed{p}$ is not diagonalizable, and $\ker\slashed{p}$ is two-dimensional. The equations for $u$ and for $v$ coincide, $\slashed{p}\,u = \slashed{p}\,v = 0$.
>
> *Model:* [[§C5a.7 The Dirac Equation and Its Lagrangian#^mod-c5a-7-3|Model §C5a.7.3]] (the momentum-space Dirac operator); *applies:* on shell $p^2 = m^2$, $p^0 > 0$; part 2 for $m > 0$, part 3 for $m = 0$; exact.
>
> *Source: the user's PHY 513 notes, Ch. 9 §9.1 (Derivation "Step 2: two solutions, before solving anything", with diagonalizability filled in) · PHY 513 Lecture 9, Part A, Step 2 · Yu §5.4.1, eqs. (5.118)–(5.131) · part 3 derived here*

^thm-c5a-10-2

> [!derivation]- Derivation
> **Step 1** (the square). Write the product with two dummy indices, $\slashed{p}^{\,2} = \gamma^\mu p_\mu\,\gamma^\nu p_\nu = \gamma^\mu\gamma^\nu p_\mu p_\nu$ (the components $p_\mu$ are numbers and commute with the matrices). Renaming the dummies $\mu \leftrightarrow \nu$ gives $\gamma^\nu\gamma^\mu p_\nu p_\mu = \gamma^\nu\gamma^\mu p_\mu p_\nu$, so the sum equals half of the sum of the two forms:
>
> $$
> \slashed{p}^{\,2} = \tfrac12\bigl(\gamma^\mu\gamma^\nu + \gamma^\nu\gamma^\mu\bigr)p_\mu p_\nu = \tfrac12\{\gamma^\mu, \gamma^\nu\}p_\mu p_\nu = g^{\mu\nu}p_\mu p_\nu\,\mathbb 1 = p^2\,\mathbb 1 ,
> $$
>
> by the Clifford algebra ([[§CB.11 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^def-cb-11-11|Def. §CB.11.11]]). On the mass shell $p^2 = m^2$. Part 1.
>
> **Step 2** (possible eigenvalues). If $\slashed{p}\,w = \lambda w$ with $w \neq 0$, then $m^2 w = \slashed{p}^{\,2}w = \slashed{p}(\lambda w) = \lambda^2 w$, so $\lambda^2 = m^2$: $\lambda = +m$ or $\lambda = -m$.
>
> **Step 3** (diagonalizable for $m > 0$). For any $w \in \mathbb C^4$ write
>
> $$
> w = \underbrace{\tfrac1{2m}(\slashed{p} + m)\,w}_{w_+} + \underbrace{\tfrac1{2m}(-\slashed{p} + m)\,w}_{w_-} ,
> $$
>
> which holds because the two coefficients add to $\frac1{2m}\,2m = 1$ (division by $m$: here $m > 0$ is used). Then $\slashed{p}\,w_+ = \frac1{2m}(\slashed{p}^{\,2} + m\slashed{p})w = \frac1{2m}(m^2 + m\slashed{p})w = m\,w_+$ by Step 1, and $\slashed{p}\,w_- = \frac1{2m}(-\slashed{p}^{\,2} + m\slashed{p})w = \frac1{2m}(-m^2 + m\slashed{p})w = -m\,w_-$. So every vector is a sum of eigenvectors with eigenvalues $\pm m$, and $\mathbb C^4 = \ker(\slashed{p} - m) + \ker(\slashed{p} + m)$; the sum is direct because eigenvectors of distinct eigenvalues are linearly independent. ⚑ By-product: the two maps $w \mapsto w_\pm$ are the projectors onto the two eigenspaces; in terms of the spinors they become $\frac{\pm\slashed{p} + m}{2m}$ of [[§C5a.12 Normalization and Spin Sums#^thm-c5a-12-10|Theorem §C5a.12.10]].
>
> **Step 4** (the multiplicities from the trace). The trace of a diagonalizable matrix is the sum of its eigenvalues with multiplicity. Every $\gamma^\mu$ is traceless ([[§C5a.14 Gamma-Matrix Technology#^thm-c5a-14-3|Theorem §C5a.14.3]]), so $\operatorname{tr}\slashed{p} = p_\mu\operatorname{tr}\gamma^\mu = 0$. With $n_\pm$ the dimensions of the two eigenspaces, Step 3 gives $n_+ + n_- = 4$, and the trace gives $m\,n_+ - m\,n_- = 0$, so (dividing by $m > 0$) $n_+ = n_-$, hence $n_+ = n_- = 2$. With [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^thm-c5a-10-1|Theorem §C5a.10.1]]: two independent $u$'s, two independent $v$'s. Part 2.
>
> **Step 5** ($m = 0$). Now $\slashed{p}^{\,2} = 0$ by Step 1. In the chiral form ([[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^def-c5a-10-2|Def. §C5a.10.2]]) the off-diagonal blocks are $p\cdot\sigma = |\mathbf p|(\mathbb 1 - \hat{\mathbf p}\cdot\boldsymbol\sigma)$ and $p\cdot\bar\sigma = |\mathbf p|(\mathbb 1 + \hat{\mathbf p}\cdot\boldsymbol\sigma)$, each $2|\mathbf p|$ times the projector onto one eigenvector of $\hat{\mathbf p}\cdot\boldsymbol\sigma$, of rank one; so $\slashed{p} \neq 0$ and $\operatorname{rank}\slashed{p} = 1 + 1 = 2$, $\dim\ker\slashed{p} = 4 - 2 = 2$. A diagonalizable matrix with $\slashed{p}^{\,2} = 0$ would have all eigenvalues $0$ and be the zero matrix; $\slashed{p} \neq 0$, so it is not diagonalizable. Both equations of Theorem §C5a.10.1 read $\slashed{p}\,w = 0$ at $m = 0$. Part 3. ⚑ By-product: at $m = 0$ the $u$'s and $v$'s lie in the same two-dimensional kernel; nothing but the exponent distinguishes them, and the projector decomposition of Step 3 does not exist → [[§C5a.13 Helicity Spinors and the Massless Limit#^thm-c5a-13-4|Theorem §C5a.13.4]].
>
> **What the derivation shows**
> - Only the Clifford algebra and $\operatorname{tr}\gamma^\mu = 0$ were used: the count holds in every basis of $\gamma$ matrices.
> - The assumption $m > 0$ enters twice (division in Steps 3–4); the massless case is genuinely different (Step 5).
> - The count "two of each" is the count of [[§C5a.7 The Dirac Equation and Its Lagrangian#^rem-c5a-7-3|§C5a.7, Remark: Eight candidates, four solutions]], here from eigenvalues instead of ranks; used next: explicit eigenvectors in the rest frame ([[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^thm-c5a-10-3|Theorem §C5a.10.3]]).

^der-c5a-10-2

*Uses:* [[§CB.11 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^def-cb-11-11|Def. §CB.11.11]], [[§C5a.14 Gamma-Matrix Technology#^thm-c5a-14-3|Theorem §C5a.14.3]], [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^thm-c5a-10-1|Theorem §C5a.10.1]], [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^def-c5a-10-2|Def. §C5a.10.2]]

> [!derivation]- Derivation (second route: the characteristic polynomial and the Dirac Hamiltonian, Yu and the pre-course notes)
> This route asks the question the other way round: for fixed $\mathbf k$, for which $k^0$ does $(k_\mu\gamma^\mu - m)w = 0$ have a solution $w \neq 0$?
>
> **Step 1** (a Hermitian eigenvalue problem). Write $k_\mu\gamma^\mu = k^0\gamma^0 - k^i\gamma^i$ (since $k_i = -k^i$) and multiply $(k^0\gamma^0 - k^i\gamma^i - m)w = 0$ from the left by $\gamma^0$, using $(\gamma^0)^2 = \mathbb 1$:
>
> $$
> k^0\,w = H_{\text{s.p.}}(\mathbf k)\,w, \qquad H_{\text{s.p.}}(\mathbf k) \equiv \gamma^0\gamma^i k^i + m\gamma^0 ,
> $$
>
> which is the single-particle Hamiltonian in momentum space ([[§C5a.7 The Dirac Equation and Its Lagrangian#^def-c5a-7-3|Def. §C5a.7.3]]).
>
> $H_{\text{s.p.}}(\mathbf k)$ is Hermitian: $(\gamma^0\gamma^i)^\dagger = \gamma^{i\dagger}\gamma^{0\dagger} = (-\gamma^i)\gamma^0 = \gamma^0\gamma^i$ and $\gamma^{0\dagger} = \gamma^0$ ([[§C5a.2 The Dirac Form#^thm-c5a-2-1|Theorem §C5a.2.1]]). So the $k^0$ are real, $H_{\text{s.p.}}(\mathbf k)$ is diagonalizable by a unitary matrix, and eigenvectors of distinct eigenvalues are orthogonal in $\mathbb C^4$.
>
> **Step 2** (the determinant, by $\gamma^5$). $\gamma^5$ anticommutes with each $\gamma^\mu$ and squares to $\mathbb 1$ ([[§CB.12 Clifford Algebras꞉ Grading, Basis and the Volume Element#^thm-cb-12-15|Theorem §CB.12.15]]), so $\gamma^5(k_\mu\gamma^\mu - m)\gamma^5 = -k_\mu\gamma^\mu - m$ and, taking determinants ($\det\gamma^5\cdot\det\gamma^5 = \det(\gamma^5)^2 = 1$), $\det(k_\mu\gamma^\mu - m) = \det(-k_\mu\gamma^\mu - m)$. Hence
>
> $$
> \bigl[\det(k_\mu\gamma^\mu - m)\bigr]^2 = \det\bigl[(k_\mu\gamma^\mu - m)(-k_\nu\gamma^\nu - m)\bigr] = \det\bigl[-(k_\mu\gamma^\mu)^2 - m\,k_\mu\gamma^\mu + m\,k_\nu\gamma^\nu + m^2\bigr] = \det\bigl[(m^2 - k^2)\mathbb 1\bigr] = (m^2 - k^2)^4 ,
> $$
>
> expanding the product into its four terms, cancelling the two cross terms, and using $(k_\mu\gamma^\mu)^2 = k^2$ (Step 1 of the first route). With $m^2 - k^2 = m^2 + \mathbf k^2 - (k^0)^2 = E_{\mathbf k}^2 - (k^0)^2$, $\det(k_\mu\gamma^\mu - m) = \pm\bigl(E_{\mathbf k}^2 - (k^0)^2\bigr)^2$; the sign is $+$, since both sides are polynomials in $k^0$ with leading term $(k^0)^4\det\gamma^0 = (k^0)^4$ ($\gamma^0$ of the chiral basis exchanges two pairs of basis vectors, determinant $(-1)^2 = 1$).
>
> **Step 3** (roots and multiplicities). $\det(k_\mu\gamma^\mu - m) = (E_{\mathbf k} + k^0)^2(E_{\mathbf k} - k^0)^2$ vanishes only at $k^0 = \pm E_{\mathbf k}$, each a double root. Since $\gamma^0$ is invertible, these are the double eigenvalues of the Hermitian $H_{\text{s.p.}}(\mathbf k)$, and for a Hermitian (diagonalizable) matrix the algebraic multiplicity is the dimension of the eigenspace: two eigenvectors $w^{(+)}(E_{\mathbf k}, \mathbf k)$ and two $w^{(-)}(-E_{\mathbf k}, \mathbf k)$, Yu's (5.129)–(5.131). Relabelling $\mathbf k \to -\mathbf k$ in the second pair ([[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^rem-c5a-10-1|Remark: Why the sign sits in the exponent]]) gives the two $v$'s.
>
> **What the derivation shows**
> - The same count, from $\det$ instead of $\operatorname{tr}$, and with the Hermitian Dirac Hamiltonian $H_{\text{s.p.}}(\mathbf k)$ supplying diagonalizability for free.
> - ⚑ By-product: $u^r(p)$ and $v^s(\tilde p)$ are eigenvectors of the *same* Hermitian $H_{\text{s.p.}}(\mathbf p)$ with eigenvalues $+E_{\mathbf p}$ and $-E_{\mathbf p}$, hence orthogonal in $\mathbb C^4$ → second route of [[§C5a.12 Normalization and Spin Sums#^thm-c5a-12-6|Theorem §C5a.12.6]].
> - $H_{\text{s.p.}}(\mathbf k) = \boldsymbol\alpha\cdot\mathbf k + \beta m$ with $\alpha^i = \gamma^0\gamma^i$, $\beta = \gamma^0$ is the Dirac Hamiltonian of Quantum Mechanics ([[§C13.2★ The Dirac Equation#^pr-c13-2-1|QM Principle §C13.2.1]]) in momentum space.
>
> *Source: Yu §5.4.1, eqs. (5.118)–(5.131) · the user's pre-course notes, §5.4 ("General form of the plane-wave solutions") · the user's PHY 513 notes, Ch. 9, "Correspondence with Yu"*

^der-c5a-10-2b

*Uses:* [[§C5a.2 The Dirac Form#^thm-c5a-2-1|Theorem §C5a.2.1]], [[§CB.12 Clifford Algebras꞉ Grading, Basis and the Volume Element#^thm-cb-12-15|Theorem §CB.12.15]], [[§CB.11 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^def-cb-11-11|Def. §CB.11.11]]

> [!remark] Remark: Two of each kind, and what they will describe
> Each component of a solution solves the Klein–Gordon equation, which offers eight candidate plane waves per $\mathbf p$ (two exponents times four columns); the Dirac equation keeps four, and splits them evenly, two per exponent ([[§C5a.7 The Dirac Equation and Its Lagrangian#^rem-c5a-7-3|§C5a.7, Remark: Eight candidates, four solutions]]; Theorem §C5a.10.2). Two positive-frequency solutions are what a spin-$\frac12$ particle needs: its two spin states (the rest frame below makes this explicit). The two negative-frequency solutions cannot be dropped, because a general solution needs both exponents, as for the scalar field ([[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-2|Theorem §C2a.2.2]]); after quantization their coefficients become creation operators of the antiparticle ([[§C5b.2 Mode Expansion and the Anticommutator Algebra|§C5b.2]]).
>
> *Source: the user's PHY 513 notes, Ch. 8 (Derivation "Eight candidates, four solutions" and paragraph "Negative energy, antiparticles"), Ch. 9 §9.1 · PS §3.3, p. 45*

^rem-c5a-10-2

### The mathematics used here: spin in the rest frame

Theorem §C5a.10.4 uses the spin matrices built from the spinor generators and the rotation content of $(\frac12, 0)\oplus(0, \frac12)$:

![[§CB.14 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-14-16]]

![[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-17-9]]

![[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^der-cb-17-9]]

## The rest frame

> [!theorem] Theorem §C5a.10.3: Rest-Frame Solutions
> At the standard momentum $k \equiv (m, \mathbf 0)$ ([[§C3.6★ Particle States and the Little Group#^def-c3-6-1|Def. §C3.6.1]]), $m > 0$, the solutions of [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^thm-c5a-10-1|Theorem §C5a.10.1]] are exactly
>
> $$
> u_0 = \sqrt m\begin{pmatrix}\xi\\ \xi\end{pmatrix}, \qquad v_0 = \sqrt m\begin{pmatrix}\eta^s\\ -\eta^s\end{pmatrix},
> $$
>
> for arbitrary two-component spinors $\xi$, $\eta^s$: upper half equal to the lower half for $u$, opposite to it for $v$. The factor $\sqrt m$ is a normalization convention, fixed below with the spin basis ([[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^def-c5a-10-4|Def. §C5a.10.4]]).
>
> *Model:* [[§C5a.7 The Dirac Equation and Its Lagrangian#^mod-c5a-7-3|Model §C5a.7.3]]; *applies:* c-number spinors, $m > 0$, rest frame; the factor $\sqrt m$ is the normalization of [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^def-c5a-10-4|Def. §C5a.10.4]].
>
> *Source: the user's PHY 513 notes, Ch. 9 §9.2 (Derivation "Step 3: solving in the rest frame"), §9.5 (Step 3) · PHY 513 Lecture 9, Part A, Step 3; Part C, Step 3 · PS §3.3, eq. (3.47)*

^thm-c5a-10-3

> [!derivation]- Derivation
> **Step 1** (the matrix at rest). At $p = k = (m, \mathbf 0)$, $p_\mu = (m, \mathbf 0)$ and $\slashed{p} = \gamma^0 p_0 = m\gamma^0$. In the chiral basis $\gamma^0 = \begin{pmatrix}0 & \mathbb 1\\ \mathbb 1 & 0\end{pmatrix}$ ([[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-4|Def. §C5a.1.4]]), and $m$ in $\slashed{p} - m$ multiplies $\mathbb 1_4 = \operatorname{diag}(\mathbb 1, \mathbb 1)$. In $2\times2$ blocks,
>
> $$
> \slashed{p} - m = m\begin{pmatrix}-\mathbb 1 & \mathbb 1\\ \mathbb 1 & -\mathbb 1\end{pmatrix}, \qquad \slashed{p} + m = m\begin{pmatrix}\mathbb 1 & \mathbb 1\\ \mathbb 1 & \mathbb 1\end{pmatrix} .
> $$
>
> **Step 2** ($u$). Write $u = (a, b)$ with two-component halves. $(\slashed{p} - m)u = m(-a + b,\ a - b) = 0$: both rows say $b = a$ (here $m \neq 0$ is divided out). Name the common half $\sqrt m\,\xi$: $u_0 = \sqrt m(\xi, \xi)$. The two choices $\xi = (1, 0)$, $(0, 1)$ are independent, matching the two eigenvectors of [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^thm-c5a-10-2|Theorem §C5a.10.2]].
>
> **Step 3** ($v$). $v = (c, d)$: $(\slashed{p} + m)v = m(c + d,\ c + d) = 0$, so $d = -c$; with $c = \sqrt m\,\eta^s$, $v_0 = \sqrt m(\eta^s, -\eta^s)$. ⚑ By-product: the factor $\sqrt m$ is not determined by the equation, which is linear; it is chosen so that no $m$ survives in the boosted spinors and $\bar u u = 2m$ in every frame → [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^def-c5a-10-4|Def. §C5a.10.4]].
>
> **What the derivation shows**
> - In the chiral basis the rest-frame condition is a statement about the two Weyl halves ([[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-2|Theorem §C5a.3.2]]): equal for $u$, opposite for $v$; nothing is "upper = particle, lower = antiparticle" here.
> - Assumption: $m > 0$; a massless particle has no rest frame.
> - Used next: what $\xi$ means ([[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^thm-c5a-10-4|Theorem §C5a.10.4]]) and the boost ([[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^thm-c5a-10-8|Theorem §C5a.10.8]]).

^der-c5a-10-3

*Uses:* [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^thm-c5a-10-1|Theorem §C5a.10.1]], [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-4|Def. §C5a.1.4]]

> [!theorem] Theorem §C5a.10.4: In the Rest Frame the Two-Spinor Carries the Spin
> On Dirac spinors the angular momentum is $J^k = \frac12\varepsilon^{kij}S^{ij} = \frac12\operatorname{diag}(\sigma^k, \sigma^k)$ (the spin matrices $S^k$ of [[§C5a.3 The Lorentz Action on Spinor Space#^def-c5a-3-2|Def. §C5a.3.2]]), with the spinor generators $S^{ij}$ ([[§CB.14 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-14-16|Def. §CB.14.16]]; chiral form [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-1|Theorem §C5a.3.1]]), and a rotation by $\theta$ about $\hat{\mathbf n}$ acts through the spinor matrix ([[§C5a.3 The Lorentz Action on Spinor Space#^def-c5a-3-1|Def. §C5a.3.1]]) as $\Lambda_{1/2} = \operatorname{diag}\bigl(D(\theta, \hat{\mathbf n}), D(\theta, \hat{\mathbf n})\bigr)$, $D = e^{-i\theta\,\hat{\mathbf n}\cdot\boldsymbol\sigma/2}$. Hence
>
> $$
> J^k\,u_0(\xi) = u_0\bigl(\tfrac12\sigma^k\xi\bigr), \qquad \Lambda_{1/2}\,u_0(\xi) = u_0\bigl(D\,\xi\bigr),
> $$
>
> and the same for $v_0(\eta^s)$: the rest-frame spinors transform under rotations exactly as the nonrelativistic spin-$\frac12$ two-spinor $\xi$ (or $\eta^s$). In particular $J^3u_0 = \pm\frac12u_0$ for $\xi = (1, 0)$, $(0, 1)$.
>
> *Model:* [[§C5a.7 The Dirac Equation and Its Lagrangian#^mod-c5a-7-3|Model §C5a.7.3]] (its rest-frame solutions); *applies:* c-number spinors, $m > 0$; a representation fact about rotations, independent of the normalization.
>
> *Source: the user's PHY 513 notes, Ch. 9 §9.2 (Definition "The two-spinor ξ and the spin basis"); Ch. 8 §8.1 (Derivation "The generators in the chiral basis"; paragraph "Rotations of a spinor") · PHY 513 Lecture 9, Part A, Step 3 · PS §3.3, p. 45 (after (3.47))*

^thm-c5a-10-4

> [!derivation]- Derivation
> **Step 1** (the generators). In the chiral basis $S^{ij} = \frac12\varepsilon^{ijl}\operatorname{diag}(\sigma^l, \sigma^l)$ ([[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-1|Theorem §C5a.3.1]]). Then $\frac12\varepsilon^{kij}S^{ij} = \frac14\varepsilon^{kij}\varepsilon^{ijl}\operatorname{diag}(\sigma^l, \sigma^l)$, and $\varepsilon^{kij}\varepsilon^{ijl} = \varepsilon^{kij}\varepsilon^{lij} = 2\delta^{kl}$ (cyclic $\varepsilon^{ijl} = \varepsilon^{lij}$, then the contraction of two $\varepsilon$'s over two indices), so $J^k = \frac14\cdot2\operatorname{diag}(\sigma^k, \sigma^k) = \frac12\operatorname{diag}(\sigma^k, \sigma^k)$.
>
> **Step 2** (on $u_0$). $J^k u_0 = \frac12\operatorname{diag}(\sigma^k, \sigma^k)\sqrt m(\xi, \xi) = \sqrt m(\frac12\sigma^k\xi, \frac12\sigma^k\xi) = u_0(\frac12\sigma^k\xi)$: both halves are acted on by the same $2\times2$ matrix, so the equality of the halves is preserved. For $v_0 = \sqrt m(\eta^s, -\eta^s)$ the same block acts on $\eta^s$ and on $-\eta^s$, giving $v_0(\frac12\sigma^k\eta^s)$; the relative sign rides along.
>
> **Step 3** (finite rotations). A rotation by $\theta$ about $\hat{\mathbf n}$ has $\omega_{ij} = \theta\,\varepsilon_{ijk}\hat n^k$ (lowered spatial indices; [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-3|Theorem §C1a.6.3]], 3, and [[Larsen PHY 513]]), so $-\frac i2\omega_{\mu\nu}S^{\mu\nu} = -\frac i2\theta\,\varepsilon_{ijk}\hat n^kS^{ij} = -i\theta\,\hat{\mathbf n}\cdot\mathbf J$ by Step 1, and $\Lambda_{1/2} = e^{-i\theta\hat{\mathbf n}\cdot\mathbf J} = \operatorname{diag}(D, D)$, the exponential of a block-diagonal matrix being block-diagonal with the exponentials of the blocks ([[§C5a.3 The Lorentz Action on Spinor Space#^def-c5a-3-1|Def. §C5a.3.1]]; for $\hat{\mathbf n} = \hat{\mathbf z}$ this is the half-angle rotation $\operatorname{diag}(e^{-i\theta\sigma^3/2}, e^{-i\theta\sigma^3/2})$ of [[§C5a.3 The Lorentz Action on Spinor Space#^rem-c5a-3-1|§C5a.3, Remark: Why half the angle]]). Acting on $u_0(\xi)$ as in Step 2 gives $u_0(D\xi)$. ⚑ By-product: rotations act on the label $\xi$ by the spin-$\frac12$ matrix itself, with no momentum-dependent correction, because $k$ is rotation-invariant; this is the Wigner rotation $W(R, k) = R$ → [[§C3.6★ Particle States and the Little Group#^thm-c3-6-9|Theorem §C3.6.9]].
>
> **What the derivation shows**
> - The Dirac spinor contains spin $\frac12$ twice ($\frac12\oplus\frac12$, [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-17-9|Theorem §CB.17.9]]); the Dirac equation at rest ties the two copies to one $\xi$, so the solutions carry a single spin $\frac12$.
> - The sign of $\omega_{ij}$ in Step 3 only fixes the orientation of the rotation; the statement $J^k = \frac12\operatorname{diag}(\sigma^k, \sigma^k)$ does not depend on it.
> - Used next: the spin basis ([[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^def-c5a-10-3|Def. §C5a.10.3]]); the spin of the *antiparticle* is read off only after quantization ([[§C5b.4 Fermions, Fock Space and the Pauli Principle|§C5b.4]]).

^der-c5a-10-4

*Uses:* [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-1|Theorem §C5a.3.1]], [[§C5a.3 The Lorentz Action on Spinor Space#^def-c5a-3-1|Def. §C5a.3.1]], [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-3|Theorem §C1a.6.3]]

> [!definition] Definition §C5a.10.3: Spin Basis
> A **spin basis** is an orthonormal basis $\xi^s$, $s = 1, 2$, of $\mathbb C^2$; likewise $\eta^s$ for the $v$'s:
>
> $$
> \xi^{r\dagger}\xi^s = \delta^{rs}, \qquad \sum_{s=1,2}\xi^s\xi^{s\dagger} = \mathbb 1_2 ,
> $$
>
> and the same for $\eta^s$. The standard choice is spin along $\pm z$, $\xi^1 = \xi_\uparrow = (1, 0)^{\mathsf T}$, $\xi^2 = \xi_\downarrow = (0, 1)^{\mathsf T}$; spin along any other axis (e.g. along $\mathbf p$: [[§C5a.13 Helicity Spinors and the Massless Limit#^def-c5a-13-2|Def. §C5a.13.2]]) is equally good. Results below use only orthonormality and completeness. Which basis $\eta^s$ the $v$'s use is fixed in Lecture 12: $\eta^s = \xi^{-s} = -i\sigma^2(\xi^s)^{\ast}$ ([[§C9.6 Charge Conjugation on Oscillators and Spinors#^def-c9-6-5|Def. §C9.6.5]]), so that $s$ labels the physical spin of the antiparticle ([[§C9.8 Physical Spin versus Wave-Function Spin|§C9.8]]).
>
> *Source: the user's PHY 513 notes, Ch. 9 §9.2 (Definition "The two-spinor ξ and the spin basis"), §9.4 (completeness of the $\xi^s$) · PHY 513 Lecture 9, Part A, Step 3; Part B ("Completeness for Dirac Spinors") · PS §3.3, pp. 47–49*

^def-c5a-10-3

Completeness follows from orthonormality: the matrix $\sum_s\xi^s\xi^{s\dagger}$ sends each $\xi^r$ to $\sum_s\xi^s\delta^{sr} = \xi^r$, so by linearity it is the identity on $\mathbb C^2$ — the two-dimensional case of $\sum_n|n\rangle\langle n| = \mathbb 1$ ([[§43 The Completeness Relation#^prop-43-1|556 Prop. §43.1]]). For the standard basis, $\begin{pmatrix}1\\0\end{pmatrix}(1\ 0) + \begin{pmatrix}0\\1\end{pmatrix}(0\ 1) = \begin{pmatrix}1&0\\0&0\end{pmatrix} + \begin{pmatrix}0&0\\0&1\end{pmatrix} = \mathbb 1_2$.

> [!definition] Definition §C5a.10.4: Normalization of the Spinors
> The spinors $u^s(p)$, $v^s(p)$ are **normalized** by two choices: the two-spinors $\xi^s$, $\eta^s$ form orthonormal bases ([[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^def-c5a-10-3|Def. §C5a.10.3]]), and the rest-frame solutions carry the factor $\sqrt m$ ([[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^thm-c5a-10-3|Theorem §C5a.10.3]]). Equivalently (Theorems §C5a.12.1–§C5a.12.4) $\bar u^ru^s = 2m\,\delta^{rs}$, the Lorentz-invariant form (PS's normalization condition), or $u^{r\dagger}u^s = 2E_{\mathbf p}\,\delta^{rs}$, the form that survives at $m = 0$.
>
> *Source: PS §3.3, eqs. (3.57), (3.60) and p. 48 ("for a massless particle Eq. (3.57) is trivial") · the user's PHY 513 notes, Ch. 9 §9.2 ("The factor √m is a normalization convention"), §9.4 · Yu §5.4.1, eqs. (5.140)–(5.141)*

^def-c5a-10-4

> [!caution] Caution: The slide's "angular momentum" is twice the angular momentum
> The Lecture 9 slide "Solution of the Dirac Equation: Step 3" labels $\operatorname{diag}(\sigma^k, \sigma^k)$ the angular momentum. It is $2J^k$: the angular momentum is $\frac12\operatorname{diag}(\sigma^k, \sigma^k)$ ([[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^thm-c5a-10-4|Theorem §C5a.10.4]]), with eigenvalues $\pm\frac12$, as the lecture said aloud ("the $J$ operator is a half sigma").
>
> *Source: the user's PHY 513 notes, Ch. 9 §9.2 (Caution "Two slips in the lecture materials")*

^cau-c5a-10-1

> [!remark] Remark: One spin-½ particle, not two
> Both halves of $u_0$ are spin-$\frac12$ objects, but they carry the same $\xi$, so a solution describes one spin-$\frac12$ particle, not two. Whether it is spin up or down along $z$ is the choice of $\xi$, and rotating the frame mixes the two choices (Theorem §C5a.10.4). In the chiral basis the two halves are the left- and right-handed Weyl components ([[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-2|Theorem §C5a.3.2]]); they are not "particle" and "antiparticle" — in the rest frame they are equal in size, and only a boost makes one of them dominate ([[§C5a.13 Helicity Spinors and the Massless Limit#^thm-c5a-13-4|Theorem §C5a.13.4]]).
>
> *Source: the user's PHY 513 notes, Ch. 9 §9.2 (paragraph "What 'spin ½' means here")*

^rem-c5a-10-3

## Boosting to a general frame

Rather than solve $(\slashed{p} - m)u = 0$ for general $\mathbf p$, the lecture boosts the rest-frame solution: a boost adds momentum, and $\Lambda_{1/2}$ is known. The covariance of the Dirac equation ([[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-1|Theorem §C5a.7.1]]) guarantees that the boosted plane wave is again a solution.

> [!theorem] Theorem §C5a.10.5: The Spinor Boost along z
> The spinor matrix $\Lambda_{1/2}$ ([[§C5a.3 The Lorentz Action on Spinor Space#^def-c5a-3-1|Def. §C5a.3.1]]) of the boost to rapidity $\eta$ along $+z$ ($\omega_{03} = -\omega_{30} = \eta$), with the generator $S^{03}$ of [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-1|Theorem §C5a.3.1]], is
>
> $$
> \Lambda_{1/2} = e^{-i\eta S^{03}} = \begin{pmatrix}e^{-\eta\sigma^3/2} & 0\\ 0 & e^{+\eta\sigma^3/2}\end{pmatrix}, \qquad e^{\mp\eta\sigma^3/2} = \cosh\tfrac\eta2\,\mathbb 1 \mp \sinh\tfrac\eta2\,\sigma^3 = \bigl(\cosh\eta\,\mathbb 1 \mp \sinh\eta\,\sigma^3\bigr)^{1/2} ,
> $$
>
> where $(\cdot)^{1/2}$ is the positive square root: each block is a positive-definite Hermitian matrix whose square involves the full rapidity $\eta$.
>
> *Source: the user's PHY 513 notes, Ch. 9 §9.3 (Derivation "Step 4: the spinor boost along z, as a square root", with the uniqueness of the root filled in) · PHY 513 Lecture 9, Part A, Step 4 · PS §3.3, eq. (3.49)*

^thm-c5a-10-5

> [!derivation]- Derivation
> **Step 1** (the exponent). In $-\frac i2\omega_{\mu\nu}S^{\mu\nu}$ only $(\mu, \nu) = (0, 3)$ and $(3, 0)$ contribute: $-\frac i2(\omega_{03}S^{03} + \omega_{30}S^{30}) = -\frac i2(\eta S^{03} + (-\eta)(-S^{03})) = -i\eta S^{03}$, using $S^{30} = -S^{03}$ (antisymmetry of the commutator). With $S^{03} = -\frac i2\operatorname{diag}(\sigma^3, -\sigma^3)$ ([[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-1|Theorem §C5a.3.1]]), $-i\eta S^{03} = (-i)(-\frac i2)\eta\operatorname{diag}(\sigma^3, -\sigma^3) = -\frac\eta2\operatorname{diag}(\sigma^3, -\sigma^3)$, since $(-i)(-i) = -1$.
>
> **Step 2** (block-diagonal exponential). The exponential of a block-diagonal matrix is block-diagonal with the exponentials of the blocks (each power of the matrix is block-diagonal with the powers of the blocks): $\Lambda_{1/2} = \operatorname{diag}(e^{-\eta\sigma^3/2}, e^{+\eta\sigma^3/2})$. The lower block is the upper one with $\sigma^3 \to -\sigma^3$; study the upper one.
>
> **Step 3** (the power series). $e^{-\eta\sigma^3/2} = \sum_n\frac1{n!}(-\frac\eta2)^n(\sigma^3)^n$. Since $(\sigma^3)^2 = \mathbb 1$, $(\sigma^3)^{2k} = \mathbb 1$ and $(\sigma^3)^{2k+1} = \sigma^3$. The even terms sum to $\sum_k\frac{(\eta/2)^{2k}}{(2k)!}\mathbb 1 = \cosh\frac\eta2\,\mathbb 1$, the odd ones to $-\sum_k\frac{(\eta/2)^{2k+1}}{(2k+1)!}\sigma^3 = -\sinh\frac\eta2\,\sigma^3$. Check on eigenvectors: for $\sigma^3 = +1$, $\cosh\frac\eta2 - \sinh\frac\eta2 = e^{-\eta/2}$; for $\sigma^3 = -1$, $e^{+\eta/2}$.
>
> **Step 4** (projectors). Let $P_\pm = \frac12(\mathbb 1 \pm \sigma^3)$. Then $P_\pm^2 = \frac14(\mathbb 1 \pm 2\sigma^3 + (\sigma^3)^2) = \frac12(\mathbb 1 \pm \sigma^3) = P_\pm$, $P_+P_- = \frac14(\mathbb 1 - (\sigma^3)^2) = 0$, $P_+ + P_- = \mathbb 1$, $P_+ - P_- = \sigma^3$. Writing $\cosh\frac\eta2 = \frac12(e^{\eta/2} + e^{-\eta/2})$, $\sinh\frac\eta2 = \frac12(e^{\eta/2} - e^{-\eta/2})$ and collecting,
>
> $$
> e^{-\eta\sigma^3/2} = e^{\eta/2}\,\frac{\mathbb 1 - \sigma^3}2 + e^{-\eta/2}\,\frac{\mathbb 1 + \sigma^3}2 = e^{\eta/2}P_- + e^{-\eta/2}P_+ .
> $$
>
> **Step 5** (its square). By Step 4, $(aP_- + bP_+)^2 = a^2P_-^2 + ab(P_-P_+ + P_+P_-) + b^2P_+^2 = a^2P_- + b^2P_+$, all four terms written out, the cross terms vanishing because $P_\pm$ are orthogonal projectors. With $a = e^{\eta/2}$, $b = e^{-\eta/2}$:
>
> $$
> \bigl(e^{-\eta\sigma^3/2}\bigr)^2 = e^{\eta}P_- + e^{-\eta}P_+ = \frac{e^\eta + e^{-\eta}}2\,\mathbb 1 - \frac{e^\eta - e^{-\eta}}2\,\sigma^3 = \cosh\eta\,\mathbb 1 - \sinh\eta\,\sigma^3 .
> $$
>
> **Step 6** (which square root). $e^{-\eta\sigma^3/2} = aP_- + bP_+$ is Hermitian with eigenvalues $a, b > 0$, i.e. positive definite. A positive operator has exactly one positive square root ([[§25 Positive Operators#^ladr-7-39|LADR 7.39]]), so $e^{-\eta\sigma^3/2} = (\cosh\eta - \sinh\eta\,\sigma^3)^{1/2}$ with the positive root. The lower block: $\sigma^3 \to -\sigma^3$ throughout.
>
> **What the derivation shows**
> - The square root acts on the numbers $e^{\pm\eta}$ and does nothing to the projectors; it trades the half-rapidity $\eta/2$ of the spinor for the full rapidity $\eta$ of the vector, where $E$ and $\mathbf p$ live → [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^rem-c5a-10-4|Remark: Why a square root restores the full rapidity]].
> - The two Weyl halves are boosted in opposite senses ($e^{\mp\eta\sigma^3/2}$), the hallmark of $(\frac12, 0)$ versus $(0, \frac12)$ ([[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^thm-c3-2-8|Theorem §C3.2.8]]).
> - Used next: the rapidity in terms of $p$ ([[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^thm-c5a-10-8|Theorem §C5a.10.8]]).

^der-c5a-10-5

*Uses:* [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-1|Theorem §C5a.3.1]], [[§C5a.3 The Lorentz Action on Spinor Space#^def-c5a-3-1|Def. §C5a.3.1]], [[§25 Positive Operators#^ladr-7-39|LADR 7.39]]

> [!definition] Definition §C5a.10.5: The Square Roots √(p·σ) and √(p·σ̄)
> For $p^2 = m^2 \ge 0$, $p^0 > 0$, the matrices $p\cdot\sigma$ and $p\cdot\bar\sigma$ ([[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^def-c5a-10-2|Def. §C5a.10.2]]) are positive semidefinite (positive definite for $m > 0$). $\sqrt{p\cdot\sigma}$ and $\sqrt{p\cdot\bar\sigma}$ denote their unique positive-semidefinite square roots: diagonalize, take the positive roots of the eigenvalues, transform back,
>
> $$
> \sqrt{p\cdot\sigma} = \sqrt{E_{\mathbf p} - |\mathbf p|}\;\Pi_+ + \sqrt{E_{\mathbf p} + |\mathbf p|}\;\Pi_-, \qquad \sqrt{p\cdot\bar\sigma} = \sqrt{E_{\mathbf p} + |\mathbf p|}\;\Pi_+ + \sqrt{E_{\mathbf p} - |\mathbf p|}\;\Pi_- ,
> $$
>
> with $\Pi_\pm = \frac12(\mathbb 1 \pm \hat{\mathbf p}\cdot\boldsymbol\sigma)$ the projectors onto spin $\pm\frac12$ along $\hat{\mathbf p}$ (for $\mathbf p = 0$, $\sqrt{p\cdot\sigma} = \sqrt{p\cdot\bar\sigma} = \sqrt m\,\mathbb 1$). Both roots are Hermitian, $(\sqrt{p\cdot\sigma})^\dagger = \sqrt{p\cdot\sigma}$, $(\sqrt{p\cdot\bar\sigma})^\dagger = \sqrt{p\cdot\bar\sigma}$, as every positive operator is ([[§25 Positive Operators#^ladr-7-34|LADR Def. 7.34]]).
>
> *Source: the user's PHY 513 notes, Ch. 9 §9.3 (Caution "What √(p·σ) means") · PS §3.3, after eq. (3.50) ("we take the positive root of each eigenvalue")*

^def-c5a-10-5

Existence and uniqueness of the positive square root: [[§25 Positive Operators#^ladr-7-39|LADR 7.39]]. The spectral form: $\mathbf p\cdot\boldsymbol\sigma = |\mathbf p|(\Pi_+ - \Pi_-)$ and $\mathbb 1 = \Pi_+ + \Pi_-$, so $p\cdot\sigma = (E_{\mathbf p} - |\mathbf p|)\Pi_+ + (E_{\mathbf p} + |\mathbf p|)\Pi_-$, and the square root of a combination of orthogonal projectors with nonnegative coefficients is the same combination with the square roots of the coefficients (Step 5 of [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^der-c5a-10-5|Derivation §C5a.10.5]]). Hermiticity, directly: the coefficients $\sqrt{E_{\mathbf p} \mp |\mathbf p|}$ are real (since $E_{\mathbf p} \ge |\mathbf p|$), and $\Pi_\pm^\dagger = \frac12(\mathbb 1 \pm \hat p^i\sigma^{i\dagger}) = \Pi_\pm$, the $\hat p^i$ being real and the Pauli matrices Hermitian ([[§B6.1 Spin One-Half and the Pauli Matrices#^thm-b6-1-4|QM Theorem §B6.1.4]]); a real combination of Hermitian matrices is Hermitian. This is what lets a root pass through a dagger unchanged, $(\sqrt{p\cdot\sigma}\,\xi)^\dagger = \xi^\dagger\sqrt{p\cdot\sigma}$, in the Dirac conjugates ([[§C5a.11 The Spinors u(p), v(p) and Their Dirac Conjugates#^thm-c5a-11-2|Theorem §C5a.11.2]], [[§C5a.11 The Spinors u(p), v(p) and Their Dirac Conjugates#^thm-c5a-11-4|Theorem §C5a.11.4]]).

> [!theorem] Theorem §C5a.10.6: Explicit Square Roots
> For $m > 0$,
>
> $$
> \sqrt{p\cdot\sigma} = \frac{p\cdot\sigma + m}{\sqrt{2(E_{\mathbf p} + m)}}, \qquad \sqrt{p\cdot\bar\sigma} = \frac{p\cdot\bar\sigma + m}{\sqrt{2(E_{\mathbf p} + m)}} .
> $$
>
> Consequently $u$ and $v$ below are smooth functions of $\mathbf p \in \mathbb R^3$, each entry and each derivative bounded by a polynomial in $|\mathbf p|$ (the entries grow like $\sqrt{E_{\mathbf p}}$). For $m = 0$ the same formulas hold for $\mathbf p \neq 0$, $\sqrt{p\cdot\sigma} = p\cdot\sigma/\sqrt{2|\mathbf p|}$; they are continuous at $\mathbf p = 0$ (value $0$) but not differentiable there.
>
> *Source: derived here, from the definition in the user's PHY 513 notes, Ch. 9 §9.3 (Caution "What √(p·σ) means": "well defined, but … almost never computed") · PHY 513, Problem Set 6, Problem 3(c) (used and checked by squaring, as the user wrote it: [[§C5a.11 The Spinors u(p), v(p) and Their Dirac Conjugates#^ex-c5a-11-1|Example §C5a.11.1]])*

^thm-c5a-10-6

> [!derivation]- Derivation
> **Step 1** (trace and determinant). $A \equiv p\cdot\sigma = \begin{pmatrix}E - p^3 & -(p^1 - ip^2)\\ -(p^1 + ip^2) & E + p^3\end{pmatrix}$ (writing $E = E_{\mathbf p}$). $\operatorname{tr}A = 2E$ and $\det A = (E - p^3)(E + p^3) - (p^1 - ip^2)(p^1 + ip^2) = E^2 - (p^3)^2 - (p^1)^2 - (p^2)^2 = E^2 - \mathbf p^2 = m^2$.
>
> **Step 2** (Cayley–Hamilton). Every $2\times2$ matrix obeys $A^2 - (\operatorname{tr}A)A + (\det A)\mathbb 1 = 0$, so $A^2 = 2E\,A - m^2\,\mathbb 1$.
>
> **Step 3** (an ansatz and its square). Try $B = (A + m)/c$ with a number $c > 0$. Expanding all terms, $B^2 = (A^2 + 2mA + m^2)/c^2$; inserting Step 2, $B^2 = (2EA - m^2 + 2mA + m^2)/c^2 = 2(E + m)A/c^2$, the $m^2$ terms cancelling. So $B^2 = A$ iff $c^2 = 2(E + m)$; take $c = \sqrt{2(E + m)} > 0$.
>
> **Step 4** (positivity, hence uniqueness). $B$ is Hermitian with eigenvalues $(E \mp |\mathbf p| + m)/c$, both positive (since $E \ge |\mathbf p|$ and $m > 0$). By [[§25 Positive Operators#^ladr-7-39|LADR 7.39]] it is *the* positive square root of [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^def-c5a-10-5|Def. §C5a.10.5]]. For $p\cdot\bar\sigma$ replace $\mathbf p \to -\mathbf p$ in Steps 1–4 ($\operatorname{tr}$ and $\det$ are unchanged).
>
> **Step 5** (smoothness and growth). $E_{\mathbf p} = \sqrt{\mathbf p^2 + m^2}$ is a smooth function of $\mathbf p$ for $m > 0$ (the argument of the root is $\ge m^2 > 0$), and $E_{\mathbf p} + m \ge 2m > 0$, so $1/\sqrt{2(E + m)}$ is smooth. The entries of $B$ are $\le (2E + m)/\sqrt{2(E + m)} \le \sqrt{2(E + m)}$, i.e. $O(\sqrt{E_{\mathbf p}})$, and each derivative of $E_{\mathbf p}$ is bounded, so all derivatives are polynomially bounded.
>
> **Step 6** ($m = 0$). Now $\det A = 0$ and Step 2 gives $A^2 = 2|\mathbf p|A$; $B = A/\sqrt{2|\mathbf p|}$ gives $B^2 = A$ for $\mathbf p \neq 0$, positive semidefinite with eigenvalues $0$ and $\sqrt{2|\mathbf p|}$. At $\mathbf p \to 0$ the entries are $O(|\mathbf p|^{1/2})$, continuous with value $0$, but $|\mathbf p|^{1/2}$ has no derivative at $0$. ⚑ By-product: for $m = 0$ the spinors are not smooth at $\mathbf p = 0$; integrals with wave packets are unaffected (the singularity is integrable), but they are not multipliers of $\mathcal S$ there → [[§C5a.11 The Spinors u(p), v(p) and Their Dirac Conjugates#^rem-c5a-11-2|Remark: In what sense a general solution is a superposition]].
>
> **What the derivation shows**
> - $\sqrt{p\cdot\sigma}$ is a first-degree polynomial in $p\cdot\sigma$, so it commutes with $p\cdot\sigma$ and $p\cdot\bar\sigma = 2E - p\cdot\sigma$.
> - In the Dirac (standard) basis these formulas turn $u(p)$ into the textbook form $\sqrt{E + m}\,(\xi, \frac{\boldsymbol\sigma\cdot\mathbf p}{E + m}\xi)$ → [[§C5a.11 The Spinors u(p), v(p) and Their Dirac Conjugates#^ex-c5a-11-1|Example §C5a.11.1]], [[§C5a.11 The Spinors u(p), v(p) and Their Dirac Conjugates#^rem-c5a-11-3|Remark: What the field theory adds to the free Dirac spinors of Quantum Mechanics]].
> - Assumption $m > 0$ is what makes the spinors smooth on the whole mass shell.

^der-c5a-10-6

*Uses:* [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^def-c5a-10-2|Def. §C5a.10.2]], [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^def-c5a-10-5|Def. §C5a.10.5]], [[§25 Positive Operators#^ladr-7-39|LADR 7.39]]

> [!theorem] Theorem §C5a.10.7: The Square-Root Identities
> For $p^2 = m^2 \ge 0$, $p^0 > 0$:
> 1. $\sqrt{p\cdot\sigma}\sqrt{p\cdot\sigma} = p\cdot\sigma$ and $\sqrt{p\cdot\bar\sigma}\sqrt{p\cdot\bar\sigma} = p\cdot\bar\sigma$;
> 2. $(p\cdot\sigma)(p\cdot\bar\sigma) = (p\cdot\bar\sigma)(p\cdot\sigma) = p^2 = m^2$;
> 3. $\sqrt{p\cdot\sigma}\sqrt{p\cdot\bar\sigma} = \sqrt{p\cdot\bar\sigma}\sqrt{p\cdot\sigma} = m$.
>
> These replace every square root met in practice: "never take the square root of a $2\times2$ matrix".
>
> *Source: the user's PHY 513 notes, Ch. 9 §9.4 (Principle "Never take the square root of a 2×2 matrix" and its proof, commutation filled in) · PHY 513 Lecture 9, Part B ("Practical Manipulations") · PS §3.3, eq. (3.51) · Yu §5.4.2, eqs. (5.153)–(5.155), (5.169)*

^thm-c5a-10-7

> [!derivation]- Derivation
> **Step 1** (part 1). This is the definition of the square root ([[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^def-c5a-10-5|Def. §C5a.10.5]]).
>
> **Step 2** (part 2, all terms). With [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^def-c5a-10-2|Def. §C5a.10.2]],
>
> $$
> (p\cdot\sigma)(p\cdot\bar\sigma) = (E - \mathbf p\cdot\boldsymbol\sigma)(E + \mathbf p\cdot\boldsymbol\sigma) = E^2 + E\,\mathbf p\cdot\boldsymbol\sigma - E\,\mathbf p\cdot\boldsymbol\sigma - (\mathbf p\cdot\boldsymbol\sigma)^2 = E^2 - p^ip^j\sigma^i\sigma^j .
> $$
>
> Since $p^ip^j$ is symmetric, only the symmetric part of $\sigma^i\sigma^j$ survives (rename $i \leftrightarrow j$ and average), $p^ip^j\sigma^i\sigma^j = \frac12p^ip^j\{\sigma^i, \sigma^j\} = p^ip^j\delta^{ij} = \mathbf p^2$ (Pauli matrices square to $\mathbb 1$ and anticommute for $i \neq j$: [[§B6.1 Spin One-Half and the Pauli Matrices#^thm-b6-1-4|QM Theorem §B6.1.4]]). So the product is $E^2 - \mathbf p^2 = m^2$. The other order: the cross terms are $-E\,\mathbf p\cdot\boldsymbol\sigma + E\,\mathbf p\cdot\boldsymbol\sigma$, again cancelling, and the result is the same.
>
> **Step 3** (commutation). $\sqrt{p\cdot\sigma}$ and $\sqrt{p\cdot\bar\sigma}$ are both combinations of the same projectors $\Pi_\pm$ ([[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^def-c5a-10-5|Def. §C5a.10.5]]), which commute with each other; so the two roots commute.
>
> **Step 4** (part 3). $X \equiv \sqrt{p\cdot\sigma}\sqrt{p\cdot\bar\sigma}$ is then a product of two commuting positive-semidefinite matrices: Hermitian, with eigenvalues the products of the eigenvalues on the common eigenvectors, $\sqrt{E - |\mathbf p|}\sqrt{E + |\mathbf p|} = \sqrt{E^2 - \mathbf p^2} = m$ on both $\Pi_+$ and $\Pi_-$. Hence $X = m\,\Pi_+ + m\,\Pi_- = m\,\mathbb 1$. (Equivalently: $X$ is positive semidefinite and $X^2 = (p\cdot\sigma)(p\cdot\bar\sigma) = m^2$ by Steps 2–3, and the unique positive root of $m^2\mathbb 1$ is $m\,\mathbb 1$, [[§25 Positive Operators#^ladr-7-39|LADR 7.39]].) For $m = 0$ the same computation gives $0$.
>
> **What the derivation shows**
> - Part 3 is the spinor form of $E^2 - \mathbf p^2 = m^2$: the two roots are "inverse up to $m$", $\sqrt{p\cdot\bar\sigma} = m\,(\sqrt{p\cdot\sigma})^{-1}$ for $m > 0$.
> - No step divides by $m$, so every check built on these identities covers $m = 0$.
> - Used in: [[§C5a.11 The Spinors u(p), v(p) and Their Dirac Conjugates#^der-c5a-11-1b|Derivation §C5a.11.1 (second route)]], and every normalization and spin sum of [[§C5a.12 Normalization and Spin Sums|§C5a.12]].

^der-c5a-10-7

*Uses:* [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^def-c5a-10-2|Def. §C5a.10.2]], [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^def-c5a-10-5|Def. §C5a.10.5]], [[§B6.1 Spin One-Half and the Pauli Matrices#^thm-b6-1-4|QM Theorem §B6.1.4]], [[§25 Positive Operators#^ladr-7-39|LADR 7.39]]

> [!derivation]- Derivation (second route: from the explicit roots)
> For $m > 0$, by [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^thm-c5a-10-6|Theorem §C5a.10.6]] and $c^2 = 2(E + m)$,
>
> $$
> \sqrt{p\cdot\sigma}\sqrt{p\cdot\bar\sigma} = \frac{(p\cdot\sigma + m)(p\cdot\bar\sigma + m)}{c^2} = \frac{(p\cdot\sigma)(p\cdot\bar\sigma) + m\,p\cdot\sigma + m\,p\cdot\bar\sigma + m^2}{2(E + m)} = \frac{m^2 + 2mE + m^2}{2(E + m)} = m ,
> $$
>
> expanding into four terms, then using part 2 for the first and $p\cdot\sigma + p\cdot\bar\sigma = 2E$ for the middle two. The other order gives the same four terms.

*Uses:* [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^thm-c5a-10-6|Theorem §C5a.10.6]]

> [!theorem] Theorem §C5a.10.8: The Spinor Boost from Rest to Momentum p
> Let $m > 0$ and let $L(p)$ be the pure boost along $\hat{\mathbf p}$ that takes $k = (m, \mathbf 0)$ to $p = (E_{\mathbf p}, \mathbf p)$, with rapidity $\eta$: $\cosh\eta = E_{\mathbf p}/m = \gamma$, $\sinh\eta = |\mathbf p|/m = \gamma v$. Its spinor matrix ([[§C5a.3 The Lorentz Action on Spinor Space#^def-c5a-3-1|Def. §C5a.3.1]]), the exponential of the boost generators $S^{0i}$ along $\hat{\mathbf p}$ ([[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-1|Theorem §C5a.3.1]]), is
>
> $$
> \Lambda_{1/2}(p) \equiv \exp\Bigl(-\frac\eta2\begin{pmatrix}\hat{\mathbf p}\cdot\boldsymbol\sigma & 0\\ 0 & -\hat{\mathbf p}\cdot\boldsymbol\sigma\end{pmatrix}\Bigr) = \begin{pmatrix}\sqrt{\dfrac{p\cdot\sigma}m} & 0\\[1ex] 0 & \sqrt{\dfrac{p\cdot\bar\sigma}m}\end{pmatrix} .
> $$
>
> The rapidity has disappeared from the result.
>
> *Source: the user's PHY 513 notes, Ch. 9 §9.3 (Derivations "Rapidity in terms of the momentum" and "Any direction (filled in)") · PHY 513 Lecture 9, Part A ("Interpretation of Rapidity") · PS §3.3, eqs. (3.48)–(3.50)*

^thm-c5a-10-8

> [!derivation]- Derivation
> **Step 1** (the vector boost along $\hat{\mathbf n}$). Take $\omega_{0i} = -\omega_{i0} = \eta\,\hat n^i$ for a unit vector $\hat{\mathbf n}$, all other $\omega_{\mu\nu} = 0$. In the vector representation this is $e^{\eta N}$ with $N = \hat n^iM^{0i}$ ([[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-3|Theorem §C1a.6.3]], whose part 2 gives the entries of $M^{03}$; $M^{0i}$ likewise has $1$ in the $(0, i)$ and $(i, 0)$ places). So $N(x^0, \mathbf x) = (\hat{\mathbf n}\cdot\mathbf x,\ \hat{\mathbf n}\,x^0)$, and on $k = (m, \mathbf 0)$: $Nk = (0, m\hat{\mathbf n})$, $N^2k = (m, \mathbf 0) = k$. Summing the exponential series, even powers give $\cosh\eta\,k$ and odd powers $\sinh\eta\,Nk$:
>
> $$
> e^{\eta N}k = (m\cosh\eta,\ m\sinh\eta\,\hat{\mathbf n}) .
> $$
>
> Setting this equal to $p = (E_{\mathbf p}, \mathbf p)$: $\hat{\mathbf n} = \hat{\mathbf p}$, $\cosh\eta = E_{\mathbf p}/m$, $\sinh\eta = |\mathbf p|/m$ (consistent: $\cosh^2\eta - \sinh^2\eta = (E^2 - \mathbf p^2)/m^2 = 1$). For $\hat{\mathbf n} = \hat{\mathbf z}$ this is $\gamma$ and $\gamma v$ of [[§C1a.4 The Lorentz Group#^def-c1a-4-2|Def. §C1a.4.2]].
>
> **Step 2** (the spinor exponent). With the same $\omega$, $-\frac i2\omega_{\mu\nu}S^{\mu\nu} = -i\sum_i\omega_{0i}S^{0i}$ (the $(0, i)$ and $(i, 0)$ terms are equal, as in Step 1 of [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^der-c5a-10-5|Derivation §C5a.10.5]]) $= -i\eta\hat n^i\bigl(-\frac i2\bigr)\operatorname{diag}(\sigma^i, -\sigma^i) = -\frac\eta2\operatorname{diag}(\hat{\mathbf n}\cdot\boldsymbol\sigma, -\hat{\mathbf n}\cdot\boldsymbol\sigma)$, by $S^{0i}$ of [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-1|Theorem §C5a.3.1]]. This is the stated exponential, with $\hat{\mathbf n} = \hat{\mathbf p}$.
>
> **Step 3** (every step of the $z$ case goes through). $(\hat{\mathbf n}\cdot\boldsymbol\sigma)^2 = \hat n^i\hat n^j\sigma^i\sigma^j = \hat n^i\hat n^j\delta^{ij} = \mathbb 1$ (symmetric part, as in Step 2 of [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^der-c5a-10-7|Derivation §C5a.10.7]]), which is all that Steps 2–6 of [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^der-c5a-10-5|Derivation §C5a.10.5]] used about $\sigma^3$. Replacing $\sigma^3 \to \hat{\mathbf n}\cdot\boldsymbol\sigma$ and $P_\pm \to \Pi_\pm = \frac12(\mathbb 1 \pm \hat{\mathbf n}\cdot\boldsymbol\sigma)$:
>
> $$
> e^{\mp\eta\,\hat{\mathbf n}\cdot\boldsymbol\sigma/2} = \bigl(\cosh\eta\,\mathbb 1 \mp \sinh\eta\,\hat{\mathbf n}\cdot\boldsymbol\sigma\bigr)^{1/2} .
> $$
>
> **Step 4** (insert the rapidity). By Step 1, $\cosh\eta\,\mathbb 1 \mp \sinh\eta\,\hat{\mathbf p}\cdot\boldsymbol\sigma = (E_{\mathbf p} \mp |\mathbf p|\,\hat{\mathbf p}\cdot\boldsymbol\sigma)/m = (E_{\mathbf p} \mp \mathbf p\cdot\boldsymbol\sigma)/m$, which is $p\cdot\sigma/m$ (upper sign) and $p\cdot\bar\sigma/m$ (lower sign) by [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^def-c5a-10-2|Def. §C5a.10.2]]. The positive root of $A/m$ is $\sqrt A/\sqrt m$ (its square is $A/m$ and it is positive), so the blocks are $\sqrt{p\cdot\sigma/m}$ and $\sqrt{p\cdot\bar\sigma/m}$.
>
> **What the derivation shows**
> - The rapidity is a device: it is needed in the intermediate steps and is absent from the result.
> - ⚑ By-product: $\Lambda_{1/2}$ is fixed by the group element only up to sign ([[§C5a.3 The Lorentz Action on Spinor Space#^def-c5a-3-1|Def. §C5a.3.1]]; [[§C3.3 How Fields Transform under the Lorentz Group#^rem-c3-3-4|§C3.3, Remark: Why a spinor's matrix is fixed only up to sign]]); the exponential of the boost generator, reached from $\mathbb 1$ along the boost path, picks the positive-definite sign. This fixes the overall sign of $u$ and $v$ below.
> - $\Lambda_{1/2}(p)$ is Hermitian and positive: the "boost" factor of the polar decomposition of an $SL(2, \mathbb C)$ matrix, block by block.

^der-c5a-10-8

*Uses:* [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-3|Theorem §C1a.6.3]], [[§C1a.4 The Lorentz Group#^def-c1a-4-2|Def. §C1a.4.2]], [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-1|Theorem §C5a.3.1]], [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^thm-c5a-10-5|Theorem §C5a.10.5]], [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^def-c5a-10-2|Def. §C5a.10.2]], [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^def-c5a-10-5|Def. §C5a.10.5]]

> [!remark] Remark: Why a square root restores the full rapidity
> A spinor rotates with half the angle and boosts with half the rapidity: its generators have eigenvalues $\pm\frac12$ and $\pm\frac i2$ where the vector's have $\pm1$ and $\pm i$ ([[§C5a.3 The Lorentz Action on Spinor Space#^rem-c5a-3-1|§C5a.3, Remark: Why half the angle]]). The four-momentum, a vector, depends on $\cosh\eta$ and $\sinh\eta$; the spinor on $\cosh\frac\eta2$ and $\sinh\frac\eta2$. Squaring a half-rapidity matrix doubles the rapidity (Step 5 of [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^der-c5a-10-5|Derivation §C5a.10.5]]), so the spinor matrix is the square root of a matrix linear in $E$ and $\mathbf p$. This is also why spinors are "square roots of vectors": $\bar u\gamma^\mu u = 2p^\mu$ ([[§C5a.12 Normalization and Spin Sums#^rem-c5a-12-1|§C5a.12, Remark: Why u†u depends on the frame and ūu does not]]) rebuilds the vector from two spinors.
>
> *Source: the user's PHY 513 notes, Ch. 9 §9.3 ("spinors do 'half' of what four-vectors do"); Ch. 8 §8.1 (paragraph "Why 'half'")*

^rem-c5a-10-4

> [!remark]- Connections
> - The four steps are Wigner's construction at the level of wave functions: solve at the standard momentum $k = (m, \mathbf 0)$, transport with the pure boost $L(p)$ — the same $L(p)$ that defines $|p, \sigma\rangle$ in [[§C3.6★ Particle States and the Little Group#^thm-c3-6-9|Theorem §C3.6.9]], so $\xi^s$ is the spin label $\sigma$ of the particle state and rotations act on it by the spin-$\frac12$ matrix (Theorem §C5a.10.4).
> - $\Lambda_{1/2}(p) = \operatorname{diag}(\sqrt{p\cdot\sigma/m}, \sqrt{p\cdot\bar\sigma/m})$ is positive Hermitian in each block: the "boost" factor of the polar decomposition, the $SL(2, \mathbb C)$ version of "every Lorentz transformation is a boost times a rotation" ([[§CB.3 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-3-13|Theorem §CB.3.13]] and its Connections; [[§B1.2 Lorentz Transformations and the Lorentz Group#^thm-b1-2-6|REL Theorem §B1.2.6]]); the upper block is the left-handed $SL(2, \mathbb C)$ matrix of [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^def-c5a-4-1|Def. §C5a.4.1]] (covering the vector representation, [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-2|Theorem §C5a.4.2]]).
> - The eigenvalue count (two $u$'s, two $v$'s) uses only $\slashed{p}^{\,2} = p^2$ and $\operatorname{tr}\gamma^\mu = 0$; the same "square root of $p^2$" is why the Dirac operator squares to the Klein–Gordon operator ([[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-8|Theorem §C5a.7.8]]).
> - The rest-frame projector structure, $\frac12(\mathbb 1 \pm \gamma^0)$ on $u_0$ and $v_0$, is the $\mathbf p = 0$ case of the energy projectors $\frac{\pm\slashed{p} + m}{2m}$ ([[§C5a.12 Normalization and Spin Sums#^thm-c5a-12-10|Theorem §C5a.12.10]]), the numerator of the Dirac propagator ([[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-3|Theorem §C5b.8.3]], draft).
> - The spectral form of $\sqrt{p\cdot\sigma}$ uses the spin projectors along $\hat{\mathbf p}$, $\Pi_\pm = \frac12(\mathbb 1 \pm \hat{\mathbf p}\cdot\boldsymbol\sigma)$, whose eigenvectors are the spin-along-an-axis spinors of [[§B6.1 Spin One-Half and the Pauli Matrices#^thm-b6-1-5|QM Theorem §B6.1.5]]: choosing $\xi$ among them is the helicity basis of [[§C5a.13 Helicity Spinors and the Massless Limit#^thm-c5a-13-2|Theorem §C5a.13.2]].
> - The Dirac Hamiltonian $H_{\text{s.p.}}(\mathbf k) = \boldsymbol\alpha\cdot\mathbf k + \beta m$ of the second route of Theorem §C5a.10.2 is the Quantum Mechanics Hamiltonian ([[§C13.2★ The Dirac Equation#^pr-c13-2-1|QM Principle §C13.2.1]]); its eigenvalue $-E$ is the "negative energy" that field theory reads as $v(-\mathbf p)$.
> - Math: positive square roots and their uniqueness ([[§25 Positive Operators#^ladr-7-39|LADR 7.39]]); a matrix annihilated by a polynomial with distinct roots is diagonalizable (Step 3 of Derivation §C5a.10.2 does this by hand for $x^2 - m^2$); Cayley–Hamilton for $2\times2$ matrices (Theorem §C5a.10.6).
