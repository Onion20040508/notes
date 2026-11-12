---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C1a
section: C1a.6
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C1a.5 Vectors, Tensors and Index Notation]] · ↑ [[· C1a Preliminaries]] · [[§C1a.7 Infinitesimal Lorentz Transformations and Generators]] →

*Sources: the user's PHY 513 notes, Ch. 2 §2.3 ("Derivatives") · PHY 513, Problem Set 1, Problem 6, and Problem Set 2, Problem 4(a), as recorded in the user's notes · Yu Zhao-Huan, 量子场论讲义, §1.4, eqs. (1.90)–(1.92).*

How does one differentiate in index notation, with respect to the coordinates, to any four-vector and to the components of a tensor, without losing a sign or a factor of two? [[§C1a.5 Vectors, Tensors and Index Notation|§C1a.5]] is the index algebra this section computes with: index positions, the derivative $\partial_\mu$ and the d'Alembertian $\partial^2$ ([[§C1a.5 Vectors, Tensors and Index Notation#^def-c1a-5-1|Def. §C1a.5.1]]), the contraction as a plain sum ([[§C1a.5 Vectors, Tensors and Index Notation#^cau-c1a-5-1|§C1a.5, Caution: A contraction is a plain sum; the signs live in the components]]) and the metric as the map between vectors and covectors ([[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-2|Theorem §C1a.5.2]]); that the gradient is a covector is Relativity's ([[§B2.2 Tensors and the Covariance Principle#^thm-b2-2-6|REL Theorem §B2.2.6]]). This section adds the calculus with indices: the basic derivative identities and plane waves, functions of $x^2$, Taylor expansion as the generator of translations, and derivatives with respect to four-vectors and tensor components, the tool behind every Euler–Lagrange equation and Noether current of [[§C1b.2 The Action Principle and the Euler–Lagrange Equations|§C1b.2]]–[[§C1b.8 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor|§C1b.8]]. Where the calculus meets generalized functions (the plane-wave rule under a Fourier integral, $1/x^2$ across the light cone, the second variation of the action), the statements are proved in [[· CA Mathematical Methods|CA]], linked from each box and listed at the end.

**Setup.** No physical system: differentiation on Minkowski space in the conventions of [[§C1a.5 Vectors, Tensors and Index Notation|§C1a.5]] ($\hbar = c = 1$, $g = \operatorname{diag}(+,-,-,-)$), valid in any relativistic theory, classical or quantum. Each statement says how differentiable its functions are, and the variables differentiated with respect to are independent components (for a momentum: off the mass shell).

## Coordinates, plane waves and functions of x²

> [!theorem] Theorem §C1a.6.1: Basic Derivative Identities
>
> $$
> \partial_\mu x^\nu = \delta^\nu{}_\mu, \qquad \partial^\mu x^\nu = g^{\mu\nu}, \qquad \partial_\mu x^\mu = 4, \qquad \partial_\mu(x^2) = 2x_\mu, \qquad \partial_\mu\partial_\nu(x^2) = 2g_{\mu\nu},
> $$
>
> and for a plane wave with $k\cdot x = \omega t - \mathbf k\cdot\mathbf x$,
>
> $$
> \partial_\mu e^{-ik\cdot x} = -ik_\mu\,e^{-ik\cdot x}, \qquad \partial^\mu e^{-ik\cdot x} = -ik^\mu\,e^{-ik\cdot x}, \qquad \partial^2\,e^{-ik\cdot x} = -k^2\,e^{-ik\cdot x} :
> $$
>
> the derivative pulls down the *lower*-index momentum $k_\mu = (\omega, -\mathbf k)$.
>
> *Source: the user's PHY 513 notes, Ch. 2 §2.3, eqs. (dxsquared), (partialtransform); Derivation "Differentiating with respect to any four-vector" ("Plane waves") · Yu §1.4, eq. (1.90)*

^thm-c1a-6-1

> [!derivation]- Derivation
> **1. Coordinates.** The $x^\nu$ are independent variables: $\partial x^\nu/\partial x^\mu$ is $1$ for $\nu = \mu$ and $0$ otherwise, $\delta^\nu{}_\mu$. Raising, $\partial^\mu x^\nu = g^{\mu\rho}\delta^\nu{}_\rho = g^{\mu\nu}$; contracting, $\delta^\mu{}_\mu = 1 + 1 + 1 + 1 = 4$, no signs (a plain sum).
>
> **2. The square.** $x^2 = g_{\alpha\beta}x^\alpha x^\beta$, so by the product rule $\partial_\mu(x^2) = g_{\alpha\beta}(\delta^\alpha{}_\mu x^\beta + x^\alpha\delta^\beta{}_\mu) = g_{\mu\beta}x^\beta + g_{\alpha\mu}x^\alpha = 2x_\mu$. In components: $\partial_\mu(t^2 - \mathbf x^2) = (2t, -2\mathbf x) = 2x_\mu$, the signs of the lower-index vector appearing by themselves. Once more: $\partial_\nu(2x_\mu) = 2g_{\mu\alpha}\delta^\alpha{}_\nu = 2g_{\mu\nu}$.
>
> **3. Plane wave.** $\partial_\mu(k_\alpha x^\alpha) = k_\alpha\delta^\alpha{}_\mu = k_\mu$ (constant $k$), and the chain rule gives $\partial_\mu e^{-ik\cdot x} = -ik_\mu e^{-ik\cdot x}$; raising, $-ik^\mu$; then $\partial_\mu\partial^\mu e^{-ik\cdot x} = (-ik_\mu)(-ik^\mu)e^{-ik\cdot x} = -k^2e^{-ik\cdot x}$.
>
> **What the derivation shows**
> - Index placement is self-consistent: "an upper index in the denominator counts as a lower index", and both sides of each identity carry the same free indices.
> - *Sense of the plane-wave rule in field theory.* For a single plane wave the identities hold pointwise. Under a Fourier integral, $f(x) = \int\frac{d^4k}{(2\pi)^4}\tilde f(k)e^{-ik\cdot x}$, the statement $\partial_\mu \leftrightarrow -ik_\mu$ is the derivative rule of the Fourier transform, an identity in $\mathcal S$ and, by duality, in $\mathcal S'$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^def-ca-3-1|Def. §CA.3.1]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-4|Theorem §CA.3.4]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-5|Theorem §CA.3.5]]); this is how $(\partial^2 + m^2) \to m^2 - k^2$ turns the Klein–Gordon equation into algebra.
> - Used next: Theorem §C1a.6.2; the Heisenberg field and the Wightman function ([[§C2b.2 The Wightman Function#^thm-c2b-2-4|Theorem §C2b.2.4]], step 1).

^der-c1a-6-1

*Uses:* [[§C1a.5 Vectors, Tensors and Index Notation#^def-c1a-5-1|Def. §C1a.5.1]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-4|Theorem §CA.3.4]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-5|Theorem §CA.3.5]]

> [!caution] Caution: The Hessian is not the wave operator
> - $\partial_\mu\partial_\nu f$ is the four-dimensional Hessian: a symmetric $(0,2)$ tensor with two free indices, not a scalar; it needs something to contract with.
> - $\partial_\mu\partial^\mu f = g^{\mu\nu}\partial_\mu\partial_\nu f = (\partial_t^2 - \nabla^2)f$ is its trace with the metric: the one invariant operator, $\partial^2$.
> - $\sum_\mu\partial_\mu\partial_\mu f = (\partial_t^2 + \nabla^2)f$, the trace without the metric, is not a tensor expression and never occurs; two lower indices summed is the error the notation exists to expose.
>
> Contracted with anything antisymmetric the Hessian vanishes, $\partial_\mu\partial_\nu F^{\mu\nu} = 0$ ([[§B2.2 Tensors and the Covariance Principle#^thm-b2-2-5|REL Theorem §B2.2.5]], 2): that one line is why $\partial_\mu F^{\mu\nu} = J^\nu$ forces $\partial_\nu J^\nu = 0$.
>
> *Source: the user's PHY 513 notes, Ch. 2 §2.3 (Caution "The Hessian is not the wave operator")*

^cau-c1a-6-1

> [!theorem] Theorem §C1a.6.2: The d'Alembertian of a Function of x²
> Let $\rho = x^2$ and $f$ twice differentiable on an interval of $\rho$ values. Where $\rho$ lies in that interval,
>
> $$
> \partial_\mu f(\rho) = 2x_\mu f'(\rho), \qquad \partial^2 f(\rho) = 8f'(\rho) + 4\rho f''(\rho) \quad\bigl(\text{in } d \text{ spacetime dimensions: } 2d\,f' + 4\rho f''\bigr),
> $$
>
> so $\partial^2\rho = 8$, $\partial^2\rho^2 = 24\rho$, $x^\mu\partial_\mu f = 2\rho f'$. The functions of $\rho$ alone with $\partial^2 f = 0$ on $\rho > 0$ or on $\rho < 0$ are $f = c_1/\rho + c_2$; in particular $\partial^2(1/x^2) = 0$ wherever $x^2 \ne 0$.
>
> *Source: the user's PHY 513 notes, Ch. 2 §2.3 (Derivation "Derivatives of functions of x² (Problem Set 1)"), eq. (boxf) · PHY 513, Problem Set 1, Problem 6*

^thm-c1a-6-2

> [!derivation]- Derivation
> **1. First derivative.** Chain rule with [[§C1a.6 Calculus with Indices#^thm-c1a-6-1|Theorem §C1a.6.1]]: $\partial_\mu f(\rho) = f'(\rho)\,\partial_\mu\rho = 2x_\mu f'(\rho)$.
>
> **2. Second derivative.** $\partial^2 f = \partial^\mu(2x_\mu f') = 2(\partial^\mu x_\mu)f' + 2x_\mu\,\partial^\mu f'$. The first term: $\partial^\mu x_\mu = \delta^\mu{}_\mu = d$ ($= 4$). The second: $\partial^\mu f'(\rho) = 2x^\mu f''(\rho)$ by step 1 applied to $f'$, so $2x_\mu\cdot2x^\mu f'' = 4\rho f''$. Total: $2d\,f' + 4\rho f''$.
>
> **3. Checks.** $f = \rho$: $f' = 1$, $f'' = 0$, $\partial^2\rho = 8$. $f = \rho^2$: $8\cdot2\rho + 4\rho\cdot2 = 24\rho$, and then $(\partial^2)^2\rho^2 = 24\cdot8 = 192$. $x^\mu\partial_\mu f = x^\mu2x_\mu f' = 2\rho f'$.
>
> **4. Harmonic functions of $\rho$.** $\partial^2 f = 0$ reads $4\rho f'' = -8f'$, i.e. $(f')'/f' = -2/\rho$ where $f' \ne 0$, so $f' = c\,\rho^{-2}$ and $f = c_1/\rho + c_2$ (with $c_1 = -c$); in $d$ dimensions $f' \propto \rho^{-d/2}$, $f \propto \rho^{1 - d/2}$. Directly: $f = 1/\rho$ has $f' = -\rho^{-2}$, $f'' = 2\rho^{-3}$, and $8(-\rho^{-2}) + 4\rho(2\rho^{-3}) = 0$. ⚑ By-product: the computation holds only where $\rho \ne 0$; on the light cone $1/x^2$ is not even locally integrable → Remark below, and [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-4|Theorem §CA.6.4]].
>
> **What the derivation shows**
> - The dimension enters only through $\partial^\mu x_\mu = d$.
> - $1/x^2$ is the massless two-point function up to a constant; that it is harmonic off the cone is the massless Klein–Gordon equation for it there ([[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-1|Theorem §C2b.3.1]], $m = 0$).
> - Used next: the distributional statement on all of $\mathbb R^4$ (Remark below).

^der-c1a-6-2

*Uses:* [[§C1a.6 Calculus with Indices#^thm-c1a-6-1|Theorem §C1a.6.1]], [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-4|Theorem §CA.6.4]]

> [!remark] Remark: In what sense 1/x² is harmonic, and where the source sits
> [[§C1a.6 Calculus with Indices#^thm-c1a-6-2|Theorem §C1a.6.2]] is a pointwise statement off the cone $x^2 = 0$. Across the cone $1/x^2$ behaves like $1/u$ near $u = 0$, is not locally integrable, and defines no distribution by itself. Distributions are obtained only as boundary values of the analytic function $1/(z^2 - \mathbf x^2)$, $z = t - i\varepsilon$ or $t(1 - i\varepsilon)$ ([[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-1|Theorem §CA.6.1]], [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-4|Theorem §CA.6.4]]), and different boundary values satisfy different equations on all of $\mathbb R^4$: the Wightman boundary value $-\frac{1}{4\pi^2}\frac{1}{x^2 - i0\,x^0}$, the massless $D_W$ ([[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-6|Theorem §C2b.3.6]]), solves $\partial^2 D_W = 0$ in $\mathcal S'$ ([[§C2b.2 The Wightman Function#^thm-c2b-2-4|Theorem §C2b.2.4]]); the Feynman boundary value $-\frac{1}{4\pi^2}\frac{1}{x^2 - i0}$, the massless $D_F$ ([[§C2b.7 Wick Rotation and the Two-Point Family#^thm-c2b-7-3|Theorem §C2b.7.3]]), solves $\partial^2 D_F = -i\delta^4(x)$ ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-5|Theorem §C2b.6.5]]). The pointwise computation cannot tell them apart; the source of the Green's function sits at the tip $x = 0$ of the cone, invisible to a calculation done where $x^2 \ne 0$.
>
> *Source: the user's PHY 513 notes, Ch. 2 §2.3 (Derivation "Derivatives of functions of x²", last paragraph) · the distributional statement assembled here from §C2b.2–§C2b.7*

^rem-c1a-6-1

## Taylor expansion

> [!theorem] Theorem §C1a.6.3: Taylor Expansion in Index Notation
> 1. If $f$ is real-analytic at $x$, then for small $a$
>
> $$
> f(x + a) = \sum_{n=0}^\infty\frac{1}{n!}\,a^{\nu_1}\cdots a^{\nu_n}\,\partial_{\nu_1}\cdots\partial_{\nu_n}f(x) \equiv e^{a\cdot\partial}f(x), \qquad a\cdot\partial = a^\nu\partial_\nu ;
> $$
>
> for $f \in C^{N+1}$ the sum to $n = N$ holds with remainder $O(|a|^{N+1})$.
> 2. Grouping the $n!/(k_0!\cdots k_3!)$ ordered index strings with $k_\nu$ copies of $\nu$ gives the multi-index form $\sum_{k}\frac{(a^0)^{k_0}\cdots(a^3)^{k_3}}{k_0!\cdots k_3!}\partial_0^{k_0}\cdots\partial_3^{k_3}f$.
> 3. On a plane wave the series is exact for all $a$: $e^{a\cdot\partial}e^{-ik\cdot x} = e^{-ik\cdot a}e^{-ik\cdot x}$. With $\hat p_\mu = i\partial_\mu$ (so $\hat p^0 = i\partial_t$ and $\hat p^j = -i\partial_j$, Quantum Mechanics' $-i\nabla$), $e^{a\cdot\partial} = e^{-ia\cdot\hat p}$: $a\cdot\partial$ generates translations.
>
> *Source: the user's PHY 513 notes, Ch. 2 §2.3 (Derivation "Taylor expansion in index notation"), eqs. (taylorindex), (taylormulti)*

^thm-c1a-6-3

> [!derivation]- Derivation
> **1. Reduce to one variable.** Let $g(s) = f(x + sa)$. By the chain rule $g'(s) = a^\nu\partial_\nu f(x + sa)$, and by induction $g^{(n)}(s) = a^{\nu_1}\cdots a^{\nu_n}\partial_{\nu_1}\cdots\partial_{\nu_n}f(x + sa)$: each derivative in $s$ brings down one more $a^\nu\partial_\nu$.
>
> **2. Taylor in $s$.** Taylor's theorem for $g$ at $s = 0$, evaluated at $s = 1$ ([[§31 Taylor's Theorem#^thm-31-2|451 Thm. §31.2]]; equivalently [[§11 Taylor's Theorem for Multivariable Functions#^thm-11-2|452 Thm. §11.2]]): $f(x + a) = \sum_{n=0}^N\frac{1}{n!}g^{(n)}(0) + R_N$ with $R_N = O(|a|^{N+1})$ for $f \in C^{N+1}$. For real-analytic $f$ the series converges to $f(x + a)$ for $|a|$ inside the radius of convergence. ⚑ By-product: for a merely smooth $f$ the infinite series need not converge to $f$; "$e^{a\cdot\partial}$" is then a statement order by order, which is all field theory uses for infinitesimal translations.
>
> **3. Multi-index form.** In $a^{\nu_1}\cdots a^{\nu_n}\partial_{\nu_1}\cdots\partial_{\nu_n}f$ the sum runs over all ordered strings $(\nu_1, \dots, \nu_n)$. Partial derivatives commute and the $a$'s are numbers, so a string with $k_\nu$ copies of each $\nu$ contributes $(a^0)^{k_0}\cdots(a^3)^{k_3}\partial_0^{k_0}\cdots\partial_3^{k_3}f$, and there are $n!/(k_0!\cdots k_3!)$ such strings. Dividing by $n!$ gives the multi-index coefficients; at second order in two variables, $\frac12a^\nu a^\rho\partial_\nu\partial_\rho f = \frac12(a^1)^2\partial_1^2f + a^1a^2\partial_1\partial_2f + \frac12(a^2)^2\partial_2^2f$, the textbook's mixed term with its factor $2$ cancelling the $\frac12$.
>
> **4. Plane waves.** By [[§C1a.6 Calculus with Indices#^thm-c1a-6-1|Theorem §C1a.6.1]], $\partial_{\nu_1}\cdots\partial_{\nu_n}e^{-ik\cdot x} = (-i)^nk_{\nu_1}\cdots k_{\nu_n}e^{-ik\cdot x}$, so the $n$-th term is $\frac{1}{n!}(-ik\cdot a)^ne^{-ik\cdot x}$, and the exponential series converges for every $a$: $e^{-ik\cdot a}e^{-ik\cdot x} = e^{-ik\cdot(x + a)}$.
>
> **5. The generator.** With $\hat p_\mu = i\partial_\mu$, $a^\nu\partial_\nu = -i\,a^\nu\hat p_\nu = -i\,a\cdot\hat p$; on $e^{-ik\cdot x}$, $\hat p_\mu$ has eigenvalue $k_\mu$, so $\hat p^0 = i\partial_t$ is the energy and $\hat p^j = -i\partial_j$ the momentum. (The user's PHY 513 notes write $\hat p_\nu = -i\partial_\nu$ and $e^{ia\cdot\hat p}$; the two signs compensate, but that $\hat p$ has eigenvalue $-k_\mu$ on $e^{-ik\cdot x}$.)
>
> **What the derivation shows**
> - The bookkeeping of the multinomial coefficients is done by the dummy indices; there is no matrix-notation barrier at third order.
> - $a\cdot\partial$ is the infinitesimal translation; its Noether charge is the four-momentum ([[§C1b.7 Spacetime Symmetries꞉ Energy and Momentum|§C1b.7]]), and on quantum fields $[\hat\phi, \hat{\mathbf P}] = -i\nabla\hat\phi$ ([[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-5|Theorem §C2a.3.5]]).
> - For a field with indices the expansion acts componentwise, $A^\mu(x + a) = A^\mu + a^\nu\partial_\nu A^\mu + \dots$: translations act alike on every field, while Lorentz transformations add a matrix on the index ([[§C1b.1 Fields and Their Transformation Laws#^thm-c1b-1-2|Theorem §C1b.1.2]]).

^der-c1a-6-3

*Uses:* [[§C1a.6 Calculus with Indices#^thm-c1a-6-1|Theorem §C1a.6.1]], [[§31 Taylor's Theorem#^thm-31-2|451 Thm. §31.2]], [[§11 Taylor's Theorem for Multivariable Functions#^thm-11-2|452 Thm. §11.2]]

> [!remark] Remark: Three expansions, not one
> Classical field theory uses Taylor's theorem in three different variables, and they must be kept apart: in the **coordinates**, $f(x + a) = f + a^\nu\partial_\nu f + \dots$, for spacetime symmetries ([[§C1a.6 Calculus with Indices#^thm-c1a-6-3|Theorem §C1a.6.3]]); in a **parameter** $\alpha$, $\phi'_\alpha = \phi + \alpha\,\Delta\phi + O(\alpha^2)$, which defines the generator $\Delta\phi$ ([[§C1b.5 Noether's Theorem#^def-c1b-5-3|Def. §C1b.5.3]]); and in the **field**, $\mathcal L(\phi + \delta\phi, \partial\phi + \partial\delta\phi) = \mathcal L + \frac{\partial\mathcal L}{\partial\phi}\delta\phi + \frac{\partial\mathcal L}{\partial(\partial_\mu\phi)}\partial_\mu\delta\phi + \dots$, the variation ([[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^def-c1b-2-3|Def. §C1b.2.3]]), whose first order gives the Euler–Lagrange equation and whose second order, the kernel $(\partial^2 + m^2)\delta^4(x - y)$ for the free field (a distribution in $x$ and $y$, [[§CA.2 Generalized Functions#^thm-ca-2-11|Theorem §CA.2.11]]), is the operator inverted by the propagator ([[§C2b.5 Green's Functions and Contours|§C2b.5]]).
>
> *Source: the user's PHY 513 notes, Ch. 2 §2.3 (Derivation "Taylor expansion in index notation", "Three expansions, not one")*

^rem-c1a-6-2

## Derivatives with respect to vectors and tensor components

> [!theorem] Theorem §C1a.6.4: Derivatives with Respect to a Four-Vector
> For a function of the four independent components $a^\mu$ of a four-vector:
> 1. $\partial/\partial a^\mu$ transforms as a covector and $\partial/\partial a_\mu$ as a vector: the index of the denominator flips height.
> 2. The identity map in its four index forms:
>
> $$
> \frac{\partial a^\nu}{\partial a^\mu} = \delta^\nu{}_\mu, \qquad \frac{\partial a_\nu}{\partial a_\mu} = \delta_\nu{}^\mu, \qquad \frac{\partial a_\nu}{\partial a^\mu} = g_{\mu\nu}, \qquad \frac{\partial a^\nu}{\partial a_\mu} = g^{\mu\nu} .
> $$
>
> 3. $\dfrac{\partial(a_\nu a^\nu)}{\partial a^\mu} = 2a_\mu$, $\ \dfrac{\partial(b_\nu a^\nu)}{\partial a^\mu} = b_\mu$; and for $\mathcal L = \frac12\partial_\nu\phi\,\partial^\nu\phi$, $\ \dfrac{\partial\mathcal L}{\partial(\partial_\mu\phi)} = \partial^\mu\phi$.
>
> The components must be independent: on the mass shell $p^0$ is a function of $\mathbf p$, and $\partial/\partial p^\mu$ must be taken before the constraint is imposed.
>
> *Source: the user's PHY 513 notes, Ch. 2 §2.3 (Derivation "Differentiating with respect to any four-vector"), eq. (vectorderivs) · Yu §1.4, eqs. (1.90)–(1.92)*

^thm-c1a-6-4

> [!derivation]- Derivation
> **1. Transformation.** If $a' = \Lambda a$, then $a = \Lambda^{-1}a'$ and $\partial a^\nu/\partial a'^\mu = (\Lambda^{-1})^\nu{}_\mu$; by the chain rule $\partial/\partial a'^\mu = (\Lambda^{-1})^\nu{}_\mu\,\partial/\partial a^\nu = \Lambda_\mu{}^\nu\,\partial/\partial a^\nu$, the covector law ([[§B2.2 Tensors and the Covariance Principle#^def-b2-2-1|REL Def. §B2.2.1]]; derived from multilinearity in [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-14|Theorem §CB.0.14]]). Nothing used that $a$ is a coordinate; for $a = x$ it is [[§B2.2 Tensors and the Covariance Principle#^thm-b2-2-6|REL Theorem §B2.2.6]]. Raising gives the vector law for $\partial/\partial a_\mu$.
>
> **2. The four forms.** The first is the independence of the four $a^\mu$. The second is the same for the four $a_\mu$, which are equally independent. The third: $a_\nu = g_{\nu\rho}a^\rho$ with constant $g$, so $\partial a_\nu/\partial a^\mu = g_{\nu\rho}\delta^\rho{}_\mu = g_{\nu\mu}$. The fourth: $a^\nu = g^{\nu\rho}a_\rho$, so $\partial a^\nu/\partial a_\mu = g^{\nu\rho}\delta_\rho{}^\mu = g^{\nu\mu}$. In components the last two are $+1$ on the time entry and $-1$ on the spatial diagonal, since $a_0 = a^0$ and $a_i = -a^i$.
>
> **3. The factor of two.** $a_\nu a^\nu = g_{\nu\rho}a^\nu a^\rho$; differentiate both factors (rename before differentiating, [[§B2.2 Tensors and the Covariance Principle#^cau-b2-2-1|REL Caution: The grammar of indices, for higher rank]]): $g_{\nu\rho}(\delta^\nu{}_\mu a^\rho + a^\nu\delta^\rho{}_\mu) = a_\mu + a_\mu = 2a_\mu$, not $a_\mu$. For $b_\nu a^\nu$ only one factor depends on $a$: $b_\nu\delta^\nu{}_\mu = b_\mu$.
>
> **4. The Lagrangian.** Treat the four $\partial_\nu\phi$ as the independent variables $a_\nu$ and write $\mathcal L = \frac12g^{\nu\rho}a_\nu a_\rho$. Step 3 with all heights flipped gives $\partial\mathcal L/\partial a_\mu = \frac12\cdot2g^{\mu\rho}a_\rho = \partial^\mu\phi$. Treating $\partial_\mu\phi$ and $\partial^\mu\phi$ as independent would lose the factor $2$: they are the same four numbers up to signs.
>
> **What the derivation shows**
> - Safe procedure: choose one set of components as the variables, express everything in them with $g$, then differentiate.
> - Momentum derivatives $\partial/\partial p^\mu$ act on off-shell functions; acting on $e^{-ip\cdot x}$ they bring down $-ix_\mu$, the Fourier dual of $\partial_\mu \to -ip_\mu$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-4|Theorem §CA.3.4]]).
> - $\partial_\mu$ acts on the argument of a field, not on a constant four-vector multiplying it: $\partial_\mu(a^\nu\phi) = a^\nu\partial_\mu\phi$ for constant $a$, with an extra $(\partial_\mu a^\nu)\phi$ if $a^\nu(x)$ is itself a field ([[§C1b.1 Fields and Their Transformation Laws|§C1b.1]]).
> - Used next: the Euler–Lagrange equations of every scalar model ([[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-4|Theorem §C1b.2.4]]), the canonical momentum ([[§C1b.4 Hamiltonian Field Theory#^def-c1b-4-1|Def. §C1b.4.1]]).

^der-c1a-6-4

*Uses:* [[§B2.2 Tensors and the Covariance Principle#^def-b2-2-1|REL Def. §B2.2.1]], [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-14|Theorem §CB.0.14]], [[§B2.2 Tensors and the Covariance Principle#^thm-b2-2-6|REL Theorem §B2.2.6]], [[§B2.2 Tensors and the Covariance Principle#^cau-b2-2-1|REL Caution: The grammar of indices, for higher rank]]

> [!theorem] Theorem §C1a.6.5: Derivatives with Respect to Tensor Components
> 1. For independent components, the derivative is a product of deltas, slot by slot: $\dfrac{\partial T^\alpha{}_\beta}{\partial T^\mu{}_\nu} = \delta^\alpha{}_\mu\delta_\beta{}^\nu$, $\ \dfrac{\partial(\partial_\alpha A_\beta)}{\partial(\partial_\mu A_\nu)} = \delta_\alpha{}^\mu\delta_\beta{}^\nu$.
> 2. Hence $\dfrac{\partial(T_{\alpha\beta}T^{\alpha\beta})}{\partial T_{\mu\nu}} = 2T^{\mu\nu}$, $\ \dfrac{\partial(T_{\alpha\beta}U^{\alpha\beta})}{\partial T_{\mu\nu}} = U^{\mu\nu}$, $\ \dfrac{\partial T^\alpha{}_\alpha}{\partial T_{\mu\nu}} = g^{\mu\nu}$.
> 3. For an antisymmetric $F$ only six components are independent; with $\alpha < \beta$ labelling them, $\partial F_{\mu\nu}/\partial F_{\alpha\beta} = \delta^\alpha_\mu\delta^\beta_\nu - \delta^\alpha_\nu\delta^\beta_\mu$. Either convention gives $\delta(F_{\alpha\beta}F^{\alpha\beta}) = 2F^{\alpha\beta}\delta F_{\alpha\beta}$.
> 4. With $F_{\alpha\beta} = \partial_\alpha A_\beta - \partial_\beta A_\alpha$ as a function of the sixteen independent $\partial_\mu A_\nu$,
>
> $$
> \frac{\partial(F_{\alpha\beta}F^{\alpha\beta})}{\partial(\partial_\mu A_\nu)} = 4F^{\mu\nu} .
> $$
>
> *Source: the user's PHY 513 notes, Ch. 2 §2.3 (Derivation "Differentiating with respect to tensor components") · PHY 513, Problem Set 2, Problem 4(a), as the user's notes record its index moves*

^thm-c1a-6-5

> [!derivation]- Derivation
> **1. Deltas.** The components are the variables; the derivative of a variable with respect to itself is $1$ and with respect to any other $0$. "$1$ if $\alpha = \mu$ and $\beta = \nu$, else $0$" is, as a function of the four indices, $\delta^\alpha{}_\mu\delta_\beta{}^\nu$ (index heights placed by the rule of [[§C1a.6 Calculus with Indices#^thm-c1a-6-4|Theorem §C1a.6.4]]: the denominator's indices flip). The other pairing $\delta^\alpha{}_\nu\delta^\mu{}_\beta$ would assert that $T_{\mu\nu}$ and $T_{\nu\mu}$ are one variable.
>
> **2. Corollaries.** $T_{\alpha\beta}T^{\alpha\beta} = g^{\alpha\gamma}g^{\beta\delta}T_{\alpha\beta}T_{\gamma\delta}$; both factors respond: $g^{\alpha\gamma}g^{\beta\delta}(\delta_\alpha{}^\mu\delta_\beta{}^\nu T_{\gamma\delta} + T_{\alpha\beta}\delta_\gamma{}^\mu\delta_\delta{}^\nu) = T^{\mu\nu} + T^{\mu\nu}$. With $U$ fixed only one factor responds: $U^{\mu\nu}$. And $T^\alpha{}_\alpha = g^{\alpha\beta}T_{\alpha\beta}$ gives $g^{\mu\nu}$.
>
> **3. Antisymmetric components.** $F_{21} = -F_{12}$ is not a separate variable, so $\partial F_{21}/\partial F_{12} = -1$, which is the stated formula with $(\alpha\beta) = (12)$, $(\mu\nu) = (21)$. If instead all sixteen $F_{\alpha\beta}$ are treated as independent and summed over ordered pairs, each true variable is counted twice. Either way, under $F \to F + \delta F$ with $\delta F$ antisymmetric, $\delta(F_{\alpha\beta}F^{\alpha\beta}) = \delta F_{\alpha\beta}F^{\alpha\beta} + F_{\alpha\beta}\delta F^{\alpha\beta} = 2F^{\alpha\beta}\delta F_{\alpha\beta}$ (seesaw in the second term): the variation is the safety net, since $\delta F$ inherits the symmetry of $F$.
>
> **4. Through the potential.** $\delta F_{\alpha\beta} = \delta(\partial_\alpha A_\beta) - \delta(\partial_\beta A_\alpha)$, so
>
> $$
> \delta(F_{\alpha\beta}F^{\alpha\beta}) = 2F^{\alpha\beta}\delta(\partial_\alpha A_\beta) - 2F^{\alpha\beta}\delta(\partial_\beta A_\alpha) = 2F^{\alpha\beta}\delta(\partial_\alpha A_\beta) + 2F^{\beta\alpha}\delta(\partial_\beta A_\alpha) = 4F^{\alpha\beta}\delta(\partial_\alpha A_\beta) ,
> $$
>
> using $F^{\alpha\beta} = -F^{\beta\alpha}$ in the second term and renaming the dummies $\alpha \leftrightarrow \beta$ in it. The coefficient of the independent $\delta(\partial_\mu A_\nu)$ is $4F^{\mu\nu}$.
>
> **What the derivation shows**
> - Every kinetic term in the course is quadratic, $\frac12$ or $\frac14$ times a square, and its derivative picks up the factor $2$ of item 2.
> - Item 4 gives, for $\mathcal L = -\frac14F_{\alpha\beta}F^{\alpha\beta}$, $\partial\mathcal L/\partial(\partial_\mu A_\nu) = -F^{\mu\nu}$: the Euler–Lagrange equation of Maxwell's theory and its canonical energy–momentum tensor use exactly this ([[§C1b.2 The Action Principle and the Euler–Lagrange Equations|§C1b.2]], [[§C1b.8 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^ex-c1b-8-2|Example §C1b.8.2]]).
> - Differentiating with respect to the sixteen $\partial_\mu A_\nu$, which are genuinely independent, avoids the counting issue of item 3 altogether.

^der-c1a-6-5

*Uses:* [[§C1a.6 Calculus with Indices#^thm-c1a-6-4|Theorem §C1a.6.4]]

> [!abstract]- Mathematical background
> Proved in CB and CA; each line says what the physics above relies on.
>
> Theorem §C1a.6.4, 1 reads the covector law of $\partial/\partial a^\mu$ off the chain rule; it is the law that multilinearity forces on every lower index ([[§C1a.5 Vectors, Tensors and Index Notation|§C1a.5]], "Tensors as multilinear maps"):
> - [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-14|Theorem §CB.0.14]] with [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^der-cb-0-14|its derivation]] — the transformation law follows from multilinearity: one $\Lambda$ per upper and one $\Lambda^{-1}$ per lower index.
>
> The calculus with indices meets generalized functions in three places: the plane-wave rule under a Fourier integral (Theorem §C1a.6.1, Theorem §C1a.6.4), the function $1/x^2$ across the light cone (Theorem §C1a.6.2 and the remark after it), and the second variation of the action (Remark: Three expansions, not one):
> - [[§CA.3 Fourier Transforms and Fourier Tricks#^def-ca-3-1|Def. §CA.3.1]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-4|Theorem §CA.3.4]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-5|Theorem §CA.3.5]] — the Fourier convention and the derivative rule $\partial_\mu \leftrightarrow -ik_\mu$, valid in $\mathcal S$ and for every tempered distribution.
> - [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-1|Theorem §CA.6.1]], [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-4|Theorem §CA.6.4]] — boundary values of analytic functions are distributions, and the light-cone boundary value $1/(-x^2 + i0\,x^0)$ exists in $\mathcal S'(\mathbb R^4)$ with singular support on the cone: the only sense in which $1/x^2$ is defined across $x^2 = 0$.
> - [[§CA.2 Generalized Functions#^thm-ca-2-11|Theorem §CA.2.11]] — the kernel theorem: $(\partial^2 + m^2)\delta^4(x - y)$ is one distribution in $x$ and $y$ together.

> [!remark]- Connections
> - $\partial_\mu$ carries a lower index because the differential of a function is a covector, the cotangent-space statement of manifold theory — [[§32 The Cotangent Space#^def-32-4|591 Def. §32.4]], [[§B2.2 Tensors and the Covariance Principle#^rem-b2-2-5|REL Remark: Why the gradient carries a lower index]].
> - The plane-wave rule $\partial_\mu \to -ik_\mu$ is the derivative rule of the Fourier transform, valid in $\mathcal S'$; it turns every free field equation into an algebraic mass-shell condition — [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-4|Theorem §CA.3.4]], [[§C2b.1 Heisenberg Fields#^thm-c2b-1-3|Theorem §C2b.1.3]].
> - $1/x^2$, harmonic off the cone, is the massless two-point function; the source of its Green's-function boundary value sits at the tip of the cone — [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-6|Theorem §C2b.3.6]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-5|Theorem §C2b.6.5]].
> - $e^{a\cdot\partial}$ is Quantum Mechanics' translation operator $e^{-i\mathbf a\cdot\hat{\mathbf P}}$ extended to time, with $\hbar = 1$ — [[§C2.2 Translation and Momentum as Its Generator#^pr-c2-2-4|QM Principle §C2.2.4]]; on quantum fields the same translation is generated by the Hilbert-space $\hat P^\mu$, $\hat\Phi(x + a) = e^{i\hat P\cdot a}\hat\Phi(x)e^{-i\hat P\cdot a}$ — [[§C3.5 Covariant Quantum Fields and the Free Scalar's Representation#^thm-c3-5-2|Theorem §C3.5.2]].
