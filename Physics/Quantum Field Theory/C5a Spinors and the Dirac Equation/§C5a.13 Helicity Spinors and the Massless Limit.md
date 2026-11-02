---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C5a
section: C5a.13
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C5a.12 Normalization and Spin Sums]] · ↑ [[· C5a Spinors and the Dirac Equation]] · [[§C5a.14 Gamma-Matrix Technology]] →

*Sources: the user's PHY 513 notes, Ch. 9 §9.3 (Derivation "Example: the helicity basis (Problem Set 5, Problem 6)") and "Correspondence with Yu", Ch. 7 §7.7 · the user's write-up of PHY 513, Problem Set 5, Problem 6 (submitted) · Peskin & Schroeder, An Introduction to Quantum Field Theory, §3.3, eqs. (3.52)–(3.54) and p. 47 · Yu Zhao-Huan, 量子场论讲义, §5.4.2, eqs. (5.158)–(5.199), (5.213) · the user's pre-course notes, §5.4 ("Helicity spinors in the Weyl representation"; note "Rest frame, and what ω_λω_{−λ} = m means").*

Which basis of two-spinors makes the spinors simplest, and what happens at $m = 0$? The spinors $u^s(p)$, $v^s(p)$ of [[§C5a.11 The Spinors u(p), v(p) and Their Dirac Conjugates#^thm-c5a-11-1|Theorem §C5a.11.1]] and [[§C5a.11 The Spinors u(p), v(p) and Their Dirac Conjugates#^thm-c5a-11-3|Theorem §C5a.11.3]] hold for any spin basis, with the same two-spinors in every frame ([[§C5a.11 The Spinors u(p), v(p) and Their Dirac Conjugates#^rem-c5a-11-1|§C5a.11, Remark: The same ξ in every frame]]). This section chooses the helicity basis, the eigenvectors of $\hat{\mathbf p}\cdot\boldsymbol\sigma$, in which no matrix square root is needed (Problem Set 5, Problem 6), writes $u_\pm$ and $v$ in it, and takes the massless and high-energy limit, where helicity becomes chirality ([[§C3.7★ Massless Particles and Helicity|§C3.7★]]). The normalizations and spin sums it uses are [[§C5a.12 Normalization and Spin Sums|§C5a.12]].

**Setup.** As in [[§C5a.12 Normalization and Spin Sums|§C5a.12]], with the helicity basis fixed: the c-number spinors $u^s(p)$, $v^s(p)$ of the free Dirac field ([[§C5a.7 The Dirac Equation and Its Lagrangian#^mod-c5a-7-3|Model §C5a.7.3]]), on shell with $p^0 = E_{\mathbf p}$, normalized as in [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^def-c5a-10-4|Def. §C5a.10.4]]; every $m \ge 0$ unless a box says $m > 0$. The results are exact algebraic identities.

*Conventions* as in [[§C5a.12 Normalization and Spin Sums|§C5a.12]].

## Helicity spinors

> [!definition] Definition §C5a.13.1: Helicity of a Dirac Spinor
> For $\mathbf p \neq 0$ the **helicity** operator on Dirac spinors is the spin along the direction of motion,
>
> $$
> h \equiv \hat{\mathbf p}\cdot\mathbf S = \frac12\begin{pmatrix}\hat{\mathbf p}\cdot\boldsymbol\sigma & 0\\ 0 & \hat{\mathbf p}\cdot\boldsymbol\sigma\end{pmatrix},
> $$
>
> with $\mathbf S = \frac12\operatorname{diag}(\boldsymbol\sigma, \boldsymbol\sigma)$ the spin matrices ([[§C5a.3 The Lorentz Action on Spinor Space#^def-c5a-3-2|Def. §C5a.3.2]]) of [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^thm-c5a-10-4|Theorem §C5a.10.4]]. A spinor with $h = +\frac12$ ($-\frac12$) is called right-handed (left-handed). This is the spinor counterpart of the helicity of states, [[§C3.7★ Massless Particles and Helicity#^def-c3-7-1|Def. §C3.7.1]].
>
> *Source: PS §3.3, eq. (3.54) · the user's write-up of PHY 513, Problem Set 5, Problem 6 (statement) · the user's PHY 513 notes, Ch. 9 §9.3 (Derivation "Example: the helicity basis") · Yu §5.4.2, eqs. (5.158)–(5.161)*

^def-c5a-13-1

> [!definition] Definition §C5a.13.2: Helicity Two-Spinors
> For $\mathbf p \neq 0$ the **helicity two-spinors** $\xi_\pm(\hat{\mathbf p}) \in \mathbb C^2$ are normalized eigenvectors of $\hat{\mathbf p}\cdot\boldsymbol\sigma$, the two-component block of the helicity operator of [[§C5a.13 Helicity Spinors and the Massless Limit#^def-c5a-13-1|Def. §C5a.13.1]]:
>
> $$
> (\hat{\mathbf p}\cdot\boldsymbol\sigma)\,\xi_\pm = \pm\xi_\pm, \qquad \xi_\pm^\dagger\xi_\pm = 1 ,
> $$
>
> each fixed up to a phase.
>
> *Source: PS §3.3, eq. (3.54) · the user's write-up of PHY 513, Problem Set 5, Problem 6 (statement) · Yu §5.4.2, eqs. (5.158)–(5.161)*

^def-c5a-13-2

> [!theorem] Theorem §C5a.13.1: The Helicity Two-Spinors
> For $\hat{\mathbf p} = (\sin\theta\cos\varphi, \sin\theta\sin\varphi, \cos\theta)$, $0 \le \theta \le \pi$, the helicity two-spinors ([[§C5a.13 Helicity Spinors and the Massless Limit#^def-c5a-13-2|Def. §C5a.13.2]]) with phases chosen to reduce to $(1, 0)^{\mathsf T}$ and $(0, 1)^{\mathsf T}$ for $\hat{\mathbf p} = +\hat{\mathbf z}$ are
>
> $$
> \xi_+(\hat{\mathbf p}) = \begin{pmatrix}\cos\frac\theta2\\ e^{i\varphi}\sin\frac\theta2\end{pmatrix}, \qquad \xi_-(\hat{\mathbf p}) = \begin{pmatrix}-e^{-i\varphi}\sin\frac\theta2\\ \cos\frac\theta2\end{pmatrix} .
> $$
>
> They are an orthonormal and complete spin basis ([[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^def-c5a-10-3|Def. §C5a.10.3]]).
>
> *Source: the user's write-up of PHY 513, Problem Set 5, Problem 6 (submitted) · the user's PHY 513 notes, Ch. 9 §9.3 (Derivation "Example: the helicity basis (Problem Set 5, Problem 6)") · Yu §5.4.2, eqs. (5.162)–(5.175) (Cartesian form)*

^thm-c5a-13-1

> [!derivation]- Derivation
> This is the user's submitted solution of PHY 513, Problem Set 5, Problem 6.
>
> **Step 1** (the operator). With the Pauli matrices, $\hat{\mathbf p}\cdot\boldsymbol\sigma = \sin\theta\cos\varphi\,\sigma^1 + \sin\theta\sin\varphi\,\sigma^2 + \cos\theta\,\sigma^3$; adding the three matrices entry by entry, the off-diagonal entries are $\sin\theta(\cos\varphi \mp i\sin\varphi) = \sin\theta\,e^{\mp i\varphi}$:
>
> $$
> \hat{\mathbf p}\cdot\boldsymbol\sigma = \begin{pmatrix}\cos\theta & \sin\theta\,e^{-i\varphi}\\ \sin\theta\,e^{i\varphi} & -\cos\theta\end{pmatrix} .
> $$
>
> The helicity equation $(\hat{\mathbf p}\cdot\boldsymbol\sigma/2)\xi = \pm\frac12\xi$, with the $\frac12$ cancelled, is $(\hat{\mathbf p}\cdot\boldsymbol\sigma)\xi = \lambda\xi$, $\lambda = \pm1$. Check: $\det(\hat{\mathbf p}\cdot\boldsymbol\sigma - \lambda) = (\cos\theta - \lambda)(-\cos\theta - \lambda) - \sin^2\theta = \lambda^2 - \cos^2\theta - \sin^2\theta = \lambda^2 - 1$, zero for $\lambda = \pm1$.
>
> **Step 2** (remove $\varphi$). With $\xi = (x, y)$, the rows are $x\cos\theta + y\sin\theta\,e^{-i\varphi} = \lambda x$ and $x\sin\theta\,e^{i\varphi} - y\cos\theta = \lambda y$. Substitute $x = e^{-i\varphi/2}x'$, $y = e^{i\varphi/2}y'$: the first row becomes $e^{-i\varphi/2}(x'\cos\theta + y'\sin\theta) = \lambda e^{-i\varphi/2}x'$ (since $e^{i\varphi/2}e^{-i\varphi} = e^{-i\varphi/2}$), the second $e^{i\varphi/2}(x'\sin\theta - y'\cos\theta) = \lambda e^{i\varphi/2}y'$. Cancelling the phases,
>
> $$
> x'\cos\theta + y'\sin\theta = \lambda x', \qquad x'\sin\theta - y'\cos\theta = \lambda y' .
> $$
>
> **Step 3** (solve, in a form valid at $\theta = 0$). For $\lambda = +1$ the second equation is $x'\sin\theta = y'(1 + \cos\theta)$; for $\lambda = -1$ the first is $y'\sin\theta = -x'(1 + \cos\theta)$ (for $\sin\theta \neq 0$ each row implies the other, since $\frac{1 - \cos\theta}{\sin\theta}\cdot\frac{1 + \cos\theta}{\sin\theta} = 1$; the forms divided by $\sin\theta$ fail at $\theta = 0$, where the phases are to be fixed, so the undivided ones are kept). Solutions:
>
> $$
> \lambda = +1:\ \begin{pmatrix}x'\\ y'\end{pmatrix} = c_+\begin{pmatrix}1 + \cos\theta\\ \sin\theta\end{pmatrix}, \qquad \lambda = -1:\ \begin{pmatrix}x'\\ y'\end{pmatrix} = c_-\begin{pmatrix}-\sin\theta\\ 1 + \cos\theta\end{pmatrix} .
> $$
>
> Multiplying back the phases: $\xi_+ = c_+(e^{-i\varphi/2}(1 + \cos\theta),\ e^{i\varphi/2}\sin\theta)$, $\xi_- = c_-(-e^{-i\varphi/2}\sin\theta,\ e^{i\varphi/2}(1 + \cos\theta))$.
>
> **Step 4** (normalize). $\xi_+^\dagger\xi_+ = |c_+|^2\bigl((1 + \cos\theta)^2 + \sin^2\theta\bigr) = |c_+|^2(1 + 2\cos\theta + \cos^2\theta + \sin^2\theta) = |c_+|^2(2 + 2\cos\theta)$ (the phases $e^{\pm i\varphi/2}$ cancel against their conjugates), and the same for $\xi_-$. With the half-angle identities $1 + \cos\theta = 2\cos^2\frac\theta2$, $\sin\theta = 2\sin\frac\theta2\cos\frac\theta2$: $2 + 2\cos\theta = 4\cos^2\frac\theta2$, so for $0 \le \theta < \pi$, $c_+ = e^{i\alpha}/(2\cos\frac\theta2)$, $c_- = e^{i\beta}/(2\cos\frac\theta2)$, phases $\alpha, \beta$ free. Substituting the half-angle forms into the components, the factor $2\cos\frac\theta2$ cancels:
>
> $$
> \xi_+ = e^{i\alpha}\begin{pmatrix}e^{-i\varphi/2}\cos\frac\theta2\\ e^{i\varphi/2}\sin\frac\theta2\end{pmatrix}, \qquad \xi_- = e^{i\beta}\begin{pmatrix}-e^{-i\varphi/2}\sin\frac\theta2\\ e^{i\varphi/2}\cos\frac\theta2\end{pmatrix} .
> $$
>
> **Step 5** (fix the phases). At $\theta = 0$: $\xi_+ = e^{i\alpha}(e^{-i\varphi/2}, 0)$, $\xi_- = e^{i\beta}(0, e^{i\varphi/2})$. These are $(1, 0)$ and $(0, 1)$ for $\alpha = \varphi/2$, $\beta = -\varphi/2$, which gives the statement. ⚑ By-product: this phase choice is singular at $\theta = \pi$ → [[§C5a.13 Helicity Spinors and the Massless Limit#^cau-c5a-13-1|Caution: No phase convention is smooth on the whole sphere]].
>
> **Step 6** (direct check for all $0 \le \theta \le \pi$, which also covers $\theta = \pi$ excluded in Step 4). With $\sin\theta\cos\frac\theta2 - \cos\theta\sin\frac\theta2 = \sin(\theta - \frac\theta2) = \sin\frac\theta2$ and $\cos\theta\cos\frac\theta2 + \sin\theta\sin\frac\theta2 = \cos\frac\theta2$:
>
> $$
> (\hat{\mathbf p}\cdot\boldsymbol\sigma)\xi_+ = \begin{pmatrix}\cos\theta\cos\frac\theta2 + \sin\theta\sin\frac\theta2\\ e^{i\varphi}(\sin\theta\cos\frac\theta2 - \cos\theta\sin\frac\theta2)\end{pmatrix} = \xi_+, \qquad (\hat{\mathbf p}\cdot\boldsymbol\sigma)\xi_- = \begin{pmatrix}e^{-i\varphi}(\sin\theta\cos\frac\theta2 - \cos\theta\sin\frac\theta2)\\ -(\sin\theta\sin\frac\theta2 + \cos\theta\cos\frac\theta2)\end{pmatrix} = -\xi_- ,
> $$
>
> and $\xi_\pm^\dagger\xi_\pm = \cos^2\frac\theta2 + \sin^2\frac\theta2 = 1$. (End of the user's solution.)
>
> **Step 7** (orthogonality and completeness). $\xi_+^\dagger\xi_- = \cos\frac\theta2(-e^{-i\varphi}\sin\frac\theta2) + e^{-i\varphi}\sin\frac\theta2\cos\frac\theta2 = 0$; also automatic, as eigenvectors of the Hermitian $\hat{\mathbf p}\cdot\boldsymbol\sigma$ with eigenvalues $+1 \neq -1$. Two orthonormal vectors in $\mathbb C^2$ form a basis, and completeness follows as in [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^def-c5a-10-3|Def. §C5a.10.3]].
>
> **What the derivation shows**
> - The phase substitution of Step 2 removes $\varphi$ from the equations; $\varphi$ re-enters only through the phase convention.
> - These are the spin-$\frac12$ eigenspinors along an axis of Quantum Mechanics ([[§B6.1 Spin One-Half and the Pauli Matrices#^thm-b6-1-5|QM Theorem §B6.1.5]]); Griffiths' $\chi_-^{(r)}$ is $-\xi_-$, a different phase convention.

^der-c5a-13-1

*Uses:* [[§B6.1 Spin One-Half and the Pauli Matrices#^def-b6-1-2|QM Def. §B6.1.2]], [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^def-c5a-10-3|Def. §C5a.10.3]]

> [!derivation]- Derivation (second route: Yu's Cartesian form)
> Yu writes $\xi_+(\mathbf p) = \frac1{\sqrt{2|\mathbf p|(|\mathbf p| + p^3)}}\bigl(|\mathbf p| + p^3,\ p^1 + ip^2\bigr)$ and $\xi_-(\mathbf p) = \frac1{\sqrt{2|\mathbf p|(|\mathbf p| + p^3)}}\bigl(-p^1 + ip^2,\ |\mathbf p| + p^3\bigr)$ (5.162) and checks the eigenvalue equations, orthonormality and completeness by direct multiplication (5.170)–(5.175). In angles: $|\mathbf p| + p^3 = |\mathbf p|(1 + \cos\theta) = 2|\mathbf p|\cos^2\frac\theta2$; $p^1 \pm ip^2 = |\mathbf p|\sin\theta\,e^{\pm i\varphi} = 2|\mathbf p|\sin\frac\theta2\cos\frac\theta2\,e^{\pm i\varphi}$; the prefactor is $1/\sqrt{4|\mathbf p|^2\cos^2\frac\theta2} = 1/(2|\mathbf p|\cos\frac\theta2)$ for $\theta < \pi$. Dividing, $\xi_+ = (\cos\frac\theta2, e^{i\varphi}\sin\frac\theta2)$ and $\xi_- = (-e^{-i\varphi}\sin\frac\theta2, \cos\frac\theta2)$: the same spinors with the same phases. Yu's form is singular at $p^3 = -|\mathbf p|$ ($\theta = \pi$), the same point as in Step 4 above.
>
> *Source: Yu §5.4.2, eqs. (5.160)–(5.175) · the user's PHY 513 notes, Ch. 9 §9.3 ("These ξ± are exactly Yu's helicity states ξ_λ (5.162), written in angles")*

> [!caution] Caution: No phase convention is smooth on the whole sphere
> At $\theta = \pi$ the spinors of [[§C5a.13 Helicity Spinors and the Massless Limit#^thm-c5a-13-1|Theorem §C5a.13.1]] are $\xi_+ = (0, e^{i\varphi})$, $\xi_- = (-e^{-i\varphi}, 0)$: they depend on $\varphi$, which is meaningless at the south pole, so the phase convention is discontinuous there. Any other smooth phase choice fails somewhere: the helicity eigenvector, as a function of $\hat{\mathbf p}$ on the sphere, cannot be given a global continuous phase. It is the same obstruction as for the rotation $R(\hat{\mathbf p})$ in [[§C3.7★ Massless Particles and Helicity#^def-c3-7-1|Def. §C3.7.1]] ("no choice is continuous on the whole sphere"), and it carries Berry's phase of a spin $\frac12$ ([[§C9.4 Time-Dependent Perturbation Theory, Sudden and Adiabatic Limits#^thm-c9-4-8|QM Theorem §C9.4.8]]). Physical results (spin sums, $|{\rm amplitudes}|^2$) do not depend on the phases.
>
> *Source: the user's PHY 513 notes, Ch. 9 §9.3 ("at θ = π the phase convention is singular, a feature of any smooth choice of phase on the sphere") · the user's write-up of PHY 513, Problem Set 5, Problem 6 (the division by cos(θ/2))*

^cau-c5a-13-1

> [!theorem] Theorem §C5a.13.2: Helicity Spinors u±
> With $\xi^s = \xi_\pm(\hat{\mathbf p})$ in [[§C5a.11 The Spinors u(p), v(p) and Their Dirac Conjugates#^thm-c5a-11-1|Theorem §C5a.11.1]], the square roots act as numbers:
>
> $$
> u_\pm(p) = \begin{pmatrix}\sqrt{E_{\mathbf p} \mp |\mathbf p|}\;\xi_\pm\\ \sqrt{E_{\mathbf p} \pm |\mathbf p|}\;\xi_\pm\end{pmatrix}, \qquad h\,u_\pm = \pm\tfrac12\,u_\pm .
> $$
>
> With Yu's abbreviation $\omega_\lambda \equiv \sqrt{E_{\mathbf p} + \lambda|\mathbf p|}$, $u_\lambda(p) = (\omega_{-\lambda}\xi_\lambda, \omega_\lambda\xi_\lambda)$ for $\lambda = \pm$, with $\omega_\lambda\omega_{-\lambda} = m$ (names in other sources: [[§C5a.11 The Spinors u(p), v(p) and Their Dirac Conjugates#^cau-c5a-11-2|§C5a.11, Caution: Names for the plane-wave spinors]]). All normalizations and the spin sum of this section hold for them.
>
> *Model:* [[§C5a.7 The Dirac Equation and Its Lagrangian#^mod-c5a-7-3|Model §C5a.7.3]]; *applies:* as in the opening, helicity basis, $\mathbf p \ne 0$.
>
> *Source: the user's PHY 513 notes, Ch. 9 §9.3 (Derivation "Example: the helicity basis", part "The Dirac spinors") · Yu §5.4.2, eqs. (5.165)–(5.181) · the user's pre-course notes, §5.4 · PS §3.3, eqs. (3.52)–(3.54)*

^thm-c5a-13-2

> [!derivation]- Derivation
> **Step 1** (the matrices on $\xi_\pm$). $p\cdot\sigma\,\xi_\pm = (E - |\mathbf p|\,\hat{\mathbf p}\cdot\boldsymbol\sigma)\xi_\pm = (E \mp |\mathbf p|)\xi_\pm$ and $p\cdot\bar\sigma\,\xi_\pm = (E \pm |\mathbf p|)\xi_\pm$ ([[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^def-c5a-10-2|Def. §C5a.10.2]], [[§C5a.13 Helicity Spinors and the Massless Limit#^def-c5a-13-1|Def. §C5a.13.1]], [[§C5a.13 Helicity Spinors and the Massless Limit#^def-c5a-13-2|Def. §C5a.13.2]]).
>
> **Step 2** (the roots on $\xi_\pm$). $\xi_\pm$ lies in the range of the projector $\Pi_\pm$, so by the spectral form of [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^def-c5a-10-5|Def. §C5a.10.5]], $\sqrt{p\cdot\sigma}\,\xi_\pm = \sqrt{E \mp |\mathbf p|}\,\xi_\pm$ and $\sqrt{p\cdot\bar\sigma}\,\xi_\pm = \sqrt{E \pm |\mathbf p|}\,\xi_\pm$. Inserting into $u^s(p)$ gives the stated $u_\pm$; with $\lambda = \pm1$ these are $\omega_{-\lambda}$ and $\omega_\lambda$, and $\omega_\lambda\omega_{-\lambda} = \sqrt{E^2 - \mathbf p^2} = m$.
>
> **Step 3** (helicity). $h$ acts on each half by $\frac12\hat{\mathbf p}\cdot\boldsymbol\sigma$, and each half of $u_\pm$ is a number times $\xi_\pm$: $h\,u_\pm = \pm\frac12u_\pm$.
>
> **Step 4** (normalizations). $\xi_\pm$ is an orthonormal spin basis ([[§C5a.13 Helicity Spinors and the Massless Limit#^thm-c5a-13-1|Theorem §C5a.13.1]]), so Theorems §C5a.12.1, §C5a.12.2 and §C5a.12.7 apply unchanged; e.g. $u_\pm^\dagger u_\pm = (E \mp |\mathbf p|) + (E \pm |\mathbf p|) = 2E$ and $\bar u_\pm u_\pm = 2\sqrt{E \mp |\mathbf p|}\sqrt{E \pm |\mathbf p|} = 2m$.
>
> **What the derivation shows**
> - In a basis of eigenvectors of $\hat{\mathbf p}\cdot\boldsymbol\sigma$ no matrix square root is needed: the only matrix in $p\cdot\sigma$ is $\mathbf p\cdot\boldsymbol\sigma$.
> - For $\mathbf p = p\hat{\mathbf z}$, $\xi_\pm = (1, 0), (0, 1)$ and these are PS's (3.52)–(3.53).
> - Used next: the massless limit ([[§C5a.13 Helicity Spinors and the Massless Limit#^thm-c5a-13-4|Theorem §C5a.13.4]]).

^der-c5a-13-2

*Uses:* [[§C5a.11 The Spinors u(p), v(p) and Their Dirac Conjugates#^thm-c5a-11-1|Theorem §C5a.11.1]], [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^def-c5a-10-2|Def. §C5a.10.2]], [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^def-c5a-10-5|Def. §C5a.10.5]], [[§C5a.13 Helicity Spinors and the Massless Limit#^def-c5a-13-1|Def. §C5a.13.1]], [[§C5a.13 Helicity Spinors and the Massless Limit#^def-c5a-13-2|Def. §C5a.13.2]], [[§C5a.13 Helicity Spinors and the Massless Limit#^thm-c5a-13-1|Theorem §C5a.13.1]]

> [!theorem] Theorem §C5a.13.3: The v Spinors in the Helicity Basis
> With $\eta^s = \lambda\,\xi_{-\lambda}$ ($\lambda = \pm$) in [[§C5a.11 The Spinors u(p), v(p) and Their Dirac Conjugates#^thm-c5a-11-3|Theorem §C5a.11.3]],
>
> $$
> v_\lambda(p) = \begin{pmatrix}\lambda\,\omega_\lambda\,\xi_{-\lambda}\\ -\lambda\,\omega_{-\lambda}\,\xi_{-\lambda}\end{pmatrix}, \qquad h\,v_\lambda(p) = -\tfrac\lambda2\,v_\lambda(p) ,
> $$
>
> Yu's choice; $\{\lambda\xi_{-\lambda}\}$ is an orthonormal spin basis, so $\bar vv = -2m$, $v^\dagger v = 2E$ and $\sum_\lambda v\bar v = \slashed{p} - m$ hold for it.
>
> *Model:* [[§C5a.7 The Dirac Equation and Its Lagrangian#^mod-c5a-7-3|Model §C5a.7.3]]; *applies:* as in the opening, helicity basis with Yu's choice $\eta^s = \lambda\,\xi_{-\lambda}$, $\mathbf p \ne 0$.
>
> *Source: Yu §5.4.2, eqs. (5.192)–(5.199), (5.213) · the user's pre-course notes, §5.4 · the user's PHY 513 notes, Ch. 9, "Correspondence with Yu" ("his v(p, λ) (5.196) is our (vspinor) with η^s = λξ_{−λ}")*

^thm-c5a-13-3

> [!derivation]- Derivation
> **Step 1** (the roots on $\xi_{-\lambda}$). By Step 2 of [[§C5a.13 Helicity Spinors and the Massless Limit#^der-c5a-13-2|Derivation §C5a.13.2]] with $\lambda \to -\lambda$: $\sqrt{p\cdot\sigma}\,\xi_{-\lambda} = \sqrt{E - (-\lambda)|\mathbf p|}\,\xi_{-\lambda} = \omega_\lambda\xi_{-\lambda}$ and $\sqrt{p\cdot\bar\sigma}\,\xi_{-\lambda} = \omega_{-\lambda}\xi_{-\lambda}$.
>
> **Step 2** (insert). $v = (\sqrt{p\cdot\sigma}\,\lambda\xi_{-\lambda},\ -\sqrt{p\cdot\bar\sigma}\,\lambda\xi_{-\lambda}) = (\lambda\omega_\lambda\xi_{-\lambda},\ -\lambda\omega_{-\lambda}\xi_{-\lambda})$.
>
> **Step 3** (helicity of the column). $(\hat{\mathbf p}\cdot\boldsymbol\sigma)\xi_{-\lambda} = -\lambda\,\xi_{-\lambda}$, so $h\,v_\lambda(p) = -\frac\lambda2v_\lambda(p)$.
>
> **Step 4** (orthonormal basis). $(\lambda\xi_{-\lambda})^\dagger(\lambda'\xi_{-\lambda'}) = \lambda\lambda'\delta_{\lambda\lambda'} = \delta_{\lambda\lambda'}$ ($\lambda^2 = 1$; [[§C5a.13 Helicity Spinors and the Massless Limit#^thm-c5a-13-1|Theorem §C5a.13.1]]). Theorems §C5a.12.3, §C5a.12.4 and §C5a.12.8 then apply.
>
> **What the derivation shows**
> - ⚑ By-product: the column $v_\lambda(p)$ has helicity $-\lambda/2$, yet it is labelled $\lambda$: the label is the helicity of the *antiparticle* that its coefficient creates, which is opposite to that of the column. This is shown only after quantization (Yu §5.5.4; [[§C5b.4 Fermions, Fock Space and the Pauli Principle|§C5b.4]]; [[§C9.8 Physical Spin versus Wave-Function Spin#^thm-c9-8-3|Theorem §C9.8.3]]); the factor $\lambda$ is a phase convention.
> - With $-i\sigma^2 = \begin{pmatrix}0 & -1\\ 1 & 0\end{pmatrix}$ and [[§C5a.13 Helicity Spinors and the Massless Limit#^thm-c5a-13-1|Theorem §C5a.13.1]]: $-i\sigma^2\xi_+^* = (-e^{-i\varphi}\sin\frac\theta2, \cos\frac\theta2) = \xi_-$ and $-i\sigma^2\xi_-^* = (-\cos\frac\theta2, -e^{i\varphi}\sin\frac\theta2) = -\xi_+$, i.e. $\lambda\xi_{-\lambda} = -i\sigma^2\xi_\lambda^*$: Yu's $v$ spinor is built from the conjugate-spin two-spinor, the pairing that charge conjugation makes systematic: $\lambda\xi_{-\lambda} = \xi^{-s}$ for $\lambda = \pm \leftrightarrow s = 1, 2$, the course's choice from Lecture 12 on ([[§C9.6 Charge Conjugation on Oscillators and Spinors#^def-c9-6-5|Def. §C9.6.5]]; [[§C9.8 Physical Spin versus Wave-Function Spin#^rem-c9-8-6|§C9.8, Remark: The choice η^s = ξ^{−s} in these notes, Peskin–Schroeder and Yu]]).

^der-c5a-13-3

*Uses:* [[§C5a.11 The Spinors u(p), v(p) and Their Dirac Conjugates#^thm-c5a-11-3|Theorem §C5a.11.3]], [[§C5a.13 Helicity Spinors and the Massless Limit#^der-c5a-13-2|Derivation §C5a.13.2]], [[§C5a.13 Helicity Spinors and the Massless Limit#^thm-c5a-13-1|Theorem §C5a.13.1]]

> [!remark] Remark: The helicity of a massive particle depends on the frame
> For $m > 0$ one can boost to a frame moving faster than the particle along $\hat{\mathbf p}$. There the momentum points the other way and the spin is unchanged, so the helicity flips: $u_+$ in one frame is a left-handed spinor in the other. Helicity is conserved by free motion ($h$ commutes with the free Dirac Hamiltonian, [[§C13.3★ Solutions of the Dirac Equation and the Hydrogen Atom#^thm-c13-3-1|QM Theorem §C13.3.1]]) but is not Lorentz invariant. For a massless particle no such boost exists, and helicity is a Lorentz invariant label ([[§C3.7★ Massless Particles and Helicity#^thm-c3-7-5|Theorem §C3.7.5]]).
>
> *Source: PS §3.3, p. 47 · the user's PHY 513 notes, Ch. 7 §7.7*

^rem-c5a-13-1

## The massless and high-energy limit

> [!theorem] Theorem §C5a.13.4: The Massless and High-Energy Limit: Helicity Becomes Chirality
> 1. For $m = 0$: $u_+(p) = \sqrt{2E_{\mathbf p}}\begin{pmatrix}0\\ \xi_+\end{pmatrix}$, $u_-(p) = \sqrt{2E_{\mathbf p}}\begin{pmatrix}\xi_-\\ 0\end{pmatrix}$, and $\gamma^5u_\pm = \pm u_\pm$ ($\gamma^5 = \operatorname{diag}(-\mathbb 1, \mathbb 1)$ in the chiral basis, [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-1|Theorem §C5a.5.1]], 1): positive helicity lives entirely in the right-handed Weyl half $\psi_R$, negative helicity in $\psi_L$ ([[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-1|Theorem §C5a.5.1]]); helicity $\pm\frac12$ equals chirality $\pm1$ (divided by 2).
> 2. For $m > 0$, $E_{\mathbf p} \gg m$: the dominant half has amplitude $\sqrt{E + |\mathbf p|} = \sqrt{2E}\,(1 + O(m^2/E^2))$ and the other half $\sqrt{E - |\mathbf p|} = m/\sqrt{E + |\mathbf p|} \approx m/\sqrt{2E}$, so $u_\pm \to \sqrt{2E}\,(0, \xi_+)$, $\sqrt{2E}\,(\xi_-, 0)$ with corrections of relative size $m/2E$.
> 3. The $v$'s of [[§C5a.13 Helicity Spinors and the Massless Limit#^thm-c5a-13-3|Theorem §C5a.13.3]] at $m = 0$: $v(p, +) = \sqrt{2E}(\xi_-, 0)$, $v(p, -) = \sqrt{2E}(0, \xi_+)$: the column of helicity $-\lambda/2$ sits in the Weyl half of that helicity.
>
> *Model:* [[§C5a.7 The Dirac Equation and Its Lagrangian#^mod-c5a-7-3|Model §C5a.7.3]], and for $m = 0$ the Weyl fields ([[§C5a.8 The Weyl Form and the Weyl Equations#^mod-c5a-8-3|Model §C5a.8.3]]); *applies:* helicity basis; parts 1 and 3 exact at $m = 0$, part 2 for $m > 0$, $E_{\mathbf p} \gg m$, up to relative corrections $m/2E_{\mathbf p}$.
>
> *Source: the user's PHY 513 notes, Ch. 9 §9.3 ("For E ≫ m, u₊ → √(2E)(0, ξ₊) … the origin of the names") · PS §3.3, eqs. (3.52)–(3.53) and p. 47 · the user's pre-course notes, §5.4 (note "Rest frame, and what ω_λω_{−λ} = m means")*

^thm-c5a-13-4

> [!derivation]- Derivation
> **Step 1** ($m = 0$). $E_{\mathbf p} = |\mathbf p|$, so $\sqrt{E - |\mathbf p|} = 0$ and $\sqrt{E + |\mathbf p|} = \sqrt{2E}$. In [[§C5a.13 Helicity Spinors and the Massless Limit#^thm-c5a-13-2|Theorem §C5a.13.2]]: $u_+ = (0, \sqrt{2E}\,\xi_+)$, $u_- = (\sqrt{2E}\,\xi_-, 0)$ (the formula holds at $m = 0$ by [[§C5a.11 The Spinors u(p), v(p) and Their Dirac Conjugates#^thm-c5a-11-1|Theorem §C5a.11.1]], 2).
>
> **Step 2** (chirality). In the chiral basis $\gamma^5 = \operatorname{diag}(-\mathbb 1, \mathbb 1)$, the upper half being $\psi_L$ and the lower $\psi_R$ ([[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-1|Theorem §C5a.5.1]]). So $\gamma^5u_+ = (0, \sqrt{2E}\xi_+) = +u_+$ and $\gamma^5u_- = (-\sqrt{2E}\xi_-, 0) = -u_-$; the chirality projectors $P_{R,L} = \frac12(\mathbb 1 \pm \gamma^5)$ ([[§C5a.5 Chirality and Weyl Spinors#^def-c5a-5-1|Def. §C5a.5.1]]) keep $u_+$ and $u_-$ respectively. Part 1.
>
> **Step 3** (high energy). $E - |\mathbf p| = \frac{(E - |\mathbf p|)(E + |\mathbf p|)}{E + |\mathbf p|} = \frac{m^2}{E + |\mathbf p|}$, multiplying and dividing by $E + |\mathbf p| > 0$, so $\sqrt{E - |\mathbf p|} = m/\sqrt{E + |\mathbf p|}$. And $|\mathbf p| = \sqrt{E^2 - m^2} = E(1 - m^2/2E^2 + O(m^4/E^4))$, so $E + |\mathbf p| = 2E(1 - m^2/4E^2 + \dots)$ and $\sqrt{E + |\mathbf p|} = \sqrt{2E}(1 + O(m^2/E^2))$. The ratio of the small to the large half is $m/(E + |\mathbf p|) \approx m/2E$. Part 2.
>
> **Step 4** ($v$). At $m = 0$, $\omega_+ = \sqrt{2E}$, $\omega_- = 0$; [[§C5a.13 Helicity Spinors and the Massless Limit#^thm-c5a-13-3|Theorem §C5a.13.3]] gives $v(p, +) = (\omega_+\xi_-, -\omega_-\xi_-) = \sqrt{2E}(\xi_-, 0)$ and $v(p, -) = (-\omega_-\xi_+, \omega_+\xi_+) = \sqrt{2E}(0, \xi_+)$. Part 3.
>
> **What the derivation shows**
> - At $m = 0$ each helicity spinor occupies a single Weyl block: the solutions of the Weyl equations have fixed helicity ([[§C5a.8 The Weyl Form and the Weyl Equations#^thm-c5a-8-4|Theorem §C5a.8.4]]), and the Lorentz invariance of chirality ($\gamma^5$ commutes with $\Lambda_{1/2}$) is the Lorentz invariance of massless helicity ([[§C3.7★ Massless Particles and Helicity#^thm-c3-7-5|Theorem §C3.7.5]]).
> - The $\sqrt m$ convention keeps the spinors finite as $m \to 0$ (PS, p. 47).
> - ⚑ By-product: the wrong-chirality amplitude is $m/\sqrt{E + |\mathbf p|}$, linear in $m$ → [[§C5a.13 Helicity Spinors and the Massless Limit#^rem-c5a-13-2|Remark: The mass is what connects the two chiral blocks]].

^der-c5a-13-4

*Uses:* [[§C5a.13 Helicity Spinors and the Massless Limit#^thm-c5a-13-2|Theorem §C5a.13.2]], [[§C5a.13 Helicity Spinors and the Massless Limit#^thm-c5a-13-3|Theorem §C5a.13.3]], [[§C5a.11 The Spinors u(p), v(p) and Their Dirac Conjugates#^thm-c5a-11-1|Theorem §C5a.11.1]], [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-1|Theorem §C5a.5.1]], [[§C5a.5 Chirality and Weyl Spinors#^def-c5a-5-1|Def. §C5a.5.1]]

> [!remark] Remark: The mass is what connects the two chiral blocks
> In $u_\lambda(p) = (\omega_{-\lambda}\xi_\lambda, \omega_\lambda\xi_\lambda)$ the two Weyl blocks have sizes $\omega_{-\lambda}$ and $\omega_\lambda$ with $\omega_\lambda\omega_{-\lambda} = m$: the "wrong" chirality is present with amplitude $m/\omega_\lambda$. At rest both blocks are equal ([[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^thm-c5a-10-3|Theorem §C5a.10.3]]); boosting shrinks one and grows the other; at $m = 0$ one vanishes. This is the plane-wave form of the Dirac equation in Weyl components, where only $m$ couples $\psi_L$ and $\psi_R$ ([[§C5a.8 The Weyl Form and the Weyl Equations#^thm-c5a-8-2|Theorem §C5a.8.2]]). Chirality is Lorentz invariant but, for $m > 0$, not conserved; helicity is conserved by free motion but, for $m > 0$, frame dependent ([[§C5a.13 Helicity Spinors and the Massless Limit#^rem-c5a-13-1|Remark: The helicity of a massive particle depends on the frame]]); at $m = 0$ they coincide and both are good labels. Interactions that couple to one chirality (the vector coupling $\bar\psi\gamma^\mu\psi$ preserves chirality) therefore suppress helicity flips by powers of $m/E$ — the helicity structure of QED amplitudes at high energy (Lecture 20; QFT C8, planned).
>
> *Source: the user's pre-course notes, §5.4 (note "Rest frame, and what ω_λω_{−λ} = m means": "the mass, divided by the energy scale, is the amplitude with which the 'wrong' chirality is populated") · PS §3.3, p. 47*

^rem-c5a-13-2

> [!abstract]- Mathematical background
> Proved in CB; each line says what the physics above relies on.
>
> In the massless limit helicity becomes chirality, the eigenvalue of $\gamma^5$, whose eigenspaces are the Weyl halves:
> - [[§CB.12 Clifford Algebras꞉ Grading, Basis and the Volume Element#^def-cb-12-14|Def. §CB.12.14]] — $\gamma^5 = i\gamma^0\gamma^1\gamma^2\gamma^3$ (Def. §C5a.5.1).
> - [[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-18-4|Theorem §CB.18.4]] with [[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^pf-cb-18-4|Proof]] — the eigenspaces of $\gamma^5$ are the Weyl halves $(\frac12, 0)$, $(0, \frac12)$ in every basis ([[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-1|Theorem §C5a.5.1]]).

> [!remark]- Connections
> - The helicity two-spinors are the spin-up and spin-down spinors along $\hat{\mathbf p}$ of [[§B6.1 Spin One-Half and the Pauli Matrices#^thm-b6-1-5|QM Theorem §B6.1.5]] (Bloch-sphere angles of [[§B6.1 Spin One-Half and the Pauli Matrices#^thm-b6-1-6|QM Theorem §B6.1.6]]); their phase singularity at the south pole is the one behind Berry's phase ([[§C9.4 Time-Dependent Perturbation Theory, Sudden and Adiabatic Limits#^thm-c9-4-8|QM Theorem §C9.4.8]]) and behind the discontinuous $R(\hat{\mathbf p})$ of [[§C3.7★ Massless Particles and Helicity#^def-c3-7-1|Def. §C3.7.1]].
> - Helicity = chirality at $m = 0$ is the field-level statement of [[§C3.7★ Massless Particles and Helicity#^thm-c3-7-5|Theorem §C3.7.5]]: the Weyl representations $(\frac12, 0)$ and $(0, \frac12)$ ([[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^thm-c3-2-8|Theorem §C3.2.8]]) carry helicity $-\frac12$ and $+\frac12$ particles; a single Weyl field describes the neutrino of [[§C3.7★ Massless Particles and Helicity#^rem-c3-7-2|§C3.7★, Remark: Parity pairs λ with −λ]] ([[§C5a.8 The Weyl Form and the Weyl Equations#^mod-c5a-8-3|Model §C5a.8.3]]).
