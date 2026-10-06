---
type: section
subject: "[[Multivariable Analysis]]"
chapter: 4
section: "15e"
tags: [multivariable-analysis, math452]
---
← [[§15 Multivariable Integration]] · ↑ [[· 4 Integration on Flat Domains]] · [[§16 Line Integrals and Green's Theorem]] →

### Extension to General Domains

The proofs above assume $D^*$ is a rectangle. We now extend to arbitrary Jordan measurable domains.

> [!theorem] Proposition §15.15: Boundary Squares Have Vanishing Total Area
> Let $D \subseteq \mathbb{R}^2$ be a bounded Jordan measurable set. Enclose $D$ in a rectangle $R$ and partition $R$ into $N^2$ squares of side $1/N$. Let $B_N$ denote the set of **boundary squares** (those that intersect $\partial D$).
>
> Then:
>
> $$
> \lim_{N \to \infty} \#(B_N) \cdot \frac{1}{N^2} = 0.
> $$

^prop-15-15

> [!proof]+ Proof
> Since $D$ is [[§15 Multivariable Integration#^def-15-14|Jordan measurable]], $\partial D$ has [[§15 Multivariable Integration#^def-15-13|Jordan measure zero]]. Thus for any $\varepsilon > 0$, there exist finitely many rectangles $R_1, \ldots, R_K$ with:
>
> $$
> \partial D \subseteq \bigcup_{k=1}^K R_k \quad \text{and} \quad \sum_{k=1}^K \text{Area}(R_k) < \varepsilon.
> $$
>
> A boundary square $S$ satisfies $S \cap \partial D \neq \emptyset$, so $S$ must intersect at least one $R_k$.
>
> For $N$ large enough (specifically, $1/N$ smaller than the minimum side length of the $R_k$'s), each $R_k$ can intersect at most $C \cdot N^2 \cdot \text{Area}(R_k)$ squares of side $1/N$, where $C$ is a universal constant.
>
> Therefore:
>
> $$
> \#(B_N) \leq C \cdot N^2 \cdot \sum_{k=1}^K \text{Area}(R_k) < C \cdot N^2 \cdot \varepsilon.
> $$
>
> Hence:
>
> $$
> \#(B_N) \cdot \frac{1}{N^2} < C \cdot \varepsilon.
> $$
>
> Since $\varepsilon > 0$ was arbitrary, the limit is zero.

^pf-15-15

*Uses:* [[§15 Multivariable Integration#^def-15-13|Def. §15.13]], [[§15 Multivariable Integration#^def-15-14|Def. §15.14]]

> [!theorem] Proposition §15.16: $C^1$ Diffeomorphisms Preserve Jordan Measurability
> Let $D^* \subseteq \mathbb{R}^2$ be bounded and Jordan measurable. Let $\Phi: \overline{D^*} \to \mathbb{R}^2$ be a $C^1$ map. Then $\Phi(\partial D^*)$ has Jordan measure zero.
>
> In particular, if $\Phi$ is a $C^1$ diffeomorphism onto $D = \Phi(D^*)$, then $D$ is Jordan measurable.

^prop-15-16

> [!proof]+ Proof
> Here we use that $\Phi$ extends to a $C^1$ map on an open set $U \supseteq \overline{D^*}$ (this is what “$C^1$ on $\overline{D^*}$” means). Choose $r > 0$ such that the compact set $K = \{p : \operatorname{dist}(p, \overline{D^*}) \leq r\}$ lies in $U$ ([[Heine–Borel Theorem|Heine–Borel]]), and let $L > 0$ bound the [[§27 Consequences of Singular Value Decomposition#^ladr-7-86|operator norm]] of $D\Phi$ on $K$. If $p, q \in \overline{D^*}$ with $\|p - q\| \leq r$, the segment from $p$ to $q$ lies in $K$, so the [[§9 Taylor's Theorem for Multivariable Functions#^thm-9-4|mean value theorem]] applied to $t \mapsto \mathbf{c} \cdot \Phi(p + t(q - p))$, where $\mathbf{c}$ is the unit vector in the direction of $\Phi(q) - \Phi(p)$, gives
>
> $$
> \|\Phi(p) - \Phi(q)\| \leq L \|p - q\| \quad \text{for } p, q \in \overline{D^*} \text{ with } \|p - q\| \leq r.
> $$
>
> Let $\varepsilon > 0$. Enclose $D^*$ in a rectangle, partition it into squares of side $1/N$, and let $B_N$ be the set of boundary squares; they cover $\partial D^*$. By [[§15 Multivariable Integration#^prop-15-15|Proposition §15.15]] we may choose $N$ with $\sqrt{2}/N \leq r$ and $\#(B_N)/N^2 < \varepsilon / (8L^2)$.
>
> For each $S \in B_N$, the set $S \cap \overline{D^*}$ has diameter at most $\sqrt{2}/N \leq r$, so its image $\Phi(S \cap \overline{D^*})$ has diameter at most $\sqrt{2}L/N$. Hence it lies in a square $\tilde{S}$ of side $2\sqrt{2}L/N$ (centered at any point of the image), with $\text{Area}(\tilde{S}) = 8L^2/N^2$.
>
> Therefore:
>
> $$
> \Phi(\partial D^*) \subseteq \bigcup_{S \in B_N} \Phi(S \cap \overline{D^*}) \subseteq \bigcup_{S \in B_N} \tilde{S}, \qquad \sum_{S \in B_N} \text{Area}(\tilde{S}) = \frac{8L^2 \, \#(B_N)}{N^2} < \varepsilon.
> $$
>
> Since $\partial D = \Phi(\partial D^*)$ (for a bijection), this shows $\partial D$ has Jordan measure zero, so $D$ is Jordan measurable.

^pf-15-16

*Uses:* [[Heine–Borel Theorem|590 §15.12]], [[§9 Taylor's Theorem for Multivariable Functions#^thm-9-4|§9.4]], [[§15 Multivariable Integration#^def-15-13|Def. §15.13]], [[§15 Multivariable Integration#^def-15-14|Def. §15.14]], [[§15 Multivariable Integration#^prop-15-15|Prop. §15.15]]

> [!remark]- Connections
> - Lebesgue analogue: a continuous map sending null sets to null sets preserves measurability, [[§18 Differentiation Theory#^thm-18-21|551 Thm. §18.21]].

> [!theorem] Theorem §15.17: Change of Variables — General Jordan Measurable Domains
> Let $D^* \subseteq \mathbb{R}^2$ be bounded and Jordan measurable. Let $\Phi: \overline{D^*} \to \overline{D}$ be a $C^1$ bijection with $C^1$ inverse, where $D = \Phi(D^*)$.
>
> Write $\Phi(u, v) = (\varphi(u, v), \psi(u, v)) = (x, y)$, and assume $J = \varphi_u \psi_v - \varphi_v \psi_u \neq 0$ on $D^*$.
>
> If $f$ is continuous on $\overline{D}$, then:
>
> $$
> \boxed{\iint_D f(x, y) \, dx \, dy = \iint_{D^*} f(\varphi(u, v), \psi(u, v)) \cdot |J(u, v)| \, du \, dv}
> $$

^thm-15-17

> [!proof]+ Proof
> Enclose $D^*$ in a rectangle $R^* = [a, b] \times [c, d]$. Partition $R^*$ into squares of side $\Delta = 1/2^m$. Classify each square $S_{ij}$ as:
> - **Interior:** $S_{ij} \subseteq D^{\ast}$
> - **Exterior:** $S_{ij} \cap D^{\ast} = \emptyset$
> - **Boundary:** $S_{ij} \cap \partial D^{\ast} \neq \emptyset$ and $S_{ij} \cap D^{\ast} \neq \emptyset$
>
> Define the inner and outer Riemann sums:
>
> $$
> \begin{aligned}
> S_m^{\text{inner}} &= \sum_{\text{interior } S_{ij}} f(\varphi(u_{ij}), \psi(u_{ij})) \cdot |J(u_{ij})| \cdot \Delta^2, \\
> S_m^{\text{outer}} &= \sum_{\text{interior or boundary } S_{ij}} f(\varphi(u_{ij}), \psi(u_{ij})) \cdot |J(u_{ij})| \cdot \Delta^2.
> \end{aligned}
> $$
>
> Since $f \circ \Phi$ and $|J|$ are continuous on $\overline{D^*}$, they are bounded ([[Continuous Image of a Compact Space is Compact|continuous image of compact is compact]]): $|f \circ \Phi| \leq M_f$ and $|J| \leq M_J$.
>
> The difference between outer and inner sums is:
>
> $$
> |S_m^{\text{outer}} - S_m^{\text{inner}}| \leq M_f \cdot M_J \cdot \#(\text{boundary squares}) \cdot \Delta^2.
> $$
>
> By [[§15 Multivariable Integration#^prop-15-15|Proposition §15.15]], this tends to zero as $m \to \infty$.
>
> For interior squares, the proof of [[§15 Multivariable Integration#^thm-15-14|Theorem §15.14]] applies verbatim: each interior square maps to a curvilinear region with area $|J| \cdot \Delta^2 + O(\varepsilon \cdot \Delta^2)$.
>
> Therefore, both $S_m^{\text{inner}}$ and $S_m^{\text{outer}}$ converge to the same limit:
>
> $$
> \lim_{m \to \infty} S_m^{\text{inner}} = \lim_{m \to \infty} S_m^{\text{outer}} = \iint_{D^*} f(\varphi, \psi) \cdot |J| \, du \, dv.
> $$
>
> On the other side, the same argument for the images (using that $D$ is Jordan measurable by [[§15 Multivariable Integration#^prop-15-16|Proposition §15.16]]) shows:
>
> $$
> \iint_D f(x, y) \, dx \, dy = \lim_{m \to \infty} \sum_{\text{interior } \Sigma_{ij}} f(x_{ij}, y_{ij}) \cdot \text{Area}(\Sigma_{ij})
> $$
>
> where $\Sigma_{ij} = \Phi(S_{ij})$.
>
> Since $\text{Area}(\Sigma_{ij}) = |J(u_{ij})| \cdot \Delta^2 + O(\varepsilon \cdot \Delta^2)$ by the error analysis in [[§15 Multivariable Integration#^thm-15-14|Theorem §15.14]], the two limits are equal.

^pf-15-17

*Uses:* [[Continuous Image of a Compact Space is Compact|590 §15.3]], [[§15 Multivariable Integration#^prop-15-15|§15.15]], [[§15 Multivariable Integration#^prop-15-16|§15.16]], [[§15 Multivariable Integration#^thm-15-14|§15.14]], [[§15 Multivariable Integration#^def-15-11|Def. §15.11]]

> [!remark]- Connections
> - The $n$-dimensional version is [[§15 Multivariable Integration#^thm-15-20|Theorem §15.20]]; in forms language it becomes $\int_{\Phi(D^*)} \omega = \int_{D^*} \Phi^*\omega$ for orientation-preserving $\Phi$ ([[§22 The Algebra of Differential Forms#^def-22-3|pullback, Def. §22.3]]).
> - Used to parametrize surfaces and compute surface area: [[Surface Area via the Gram Matrix|Theorem §18.1]].
> - Computational version: [[§106 Change of Variables in Multiple Integrals#^thm-106-1|Calc Thm. §106.1]] (with worked examples).

> [!theorem] Proposition §15.18: Isolated Zeros of the Jacobian
> The change of variables formula remains valid if $J = 0$ at finitely many isolated points $p_1, \ldots, p_n \in D^*$, provided $J$ does not change sign on $D^*$.

^prop-15-18

> [!proof]+ Proof
> For $\varepsilon > 0$, define $D^*_\varepsilon = D^* \setminus \bigcup_{k=1}^n B_\varepsilon(p_k)$ ([[§2 Open and Closed Sets#^def-2-1|Def. §2.1]]).
>
> On $D^*_\varepsilon$, we have $J \neq 0$, so [[Change of Variables Formula (multiple integrals)|Theorem §15.17]] applies:
>
> $$
> \iint_{\Phi(D^*_\varepsilon)} f \, dx \, dy = \iint_{D^*_\varepsilon} f(\varphi, \psi) \cdot |J| \, du \, dv.
> $$
>
> As $\varepsilon \to 0$:
> - The left side converges to $\iint_D f \, dx \, dy$ since we remove sets of measure $O(\varepsilon^2)$.
> - The right side converges to $\iint_{D^*} f(\varphi, \psi) \cdot |J| \, du \, dv$ for the same reason.
>
> This is particularly important for polar coordinates, where $J = r$ vanishes at $r = 0$.

^pf-15-18

*Uses:* [[§2 Open and Closed Sets#^def-2-1|Def. §2.1]], [[Change of Variables Formula (multiple integrals)|§15.17]], [[§15 Multivariable Integration#^thm-15-4|§15.4]]

### Geometric Interpretation and Higher Dimensions

> [!theorem] Proposition §15.19: Determinants Measure Volume Distortion
> Let $T: \mathbb{R}^n \to \mathbb{R}^n$ be a linear map represented by matrix $A$. Then for any bounded Jordan measurable set $E \subseteq \mathbb{R}^n$ (in Lebesgue theory: any Lebesgue measurable set):
>
> $$
> \text{Vol}_n(T(E)) = |\det(A)| \cdot \text{Vol}_n(E).
> $$
>
> In particular, a unit $n$-cube maps to a parallelepiped of volume $|\det(A)|$.

^prop-15-19

*The course omits the proof; see [[§34 Determinants#^ladr-9-61|LADR 9.61]], and for $n = 2$ Part I of the first proof of [[§15 Multivariable Integration#^thm-15-14|Theorem §15.14]] (the image of a rectangle).*

> [!remark]- Connections
> - This is [[§34 Determinants#^ladr-9-61|LADR 9.61]] ($T$ changes volume by factor of $|\det T|$), proved there via polar decomposition and singular values ([[§34 Determinants#^ladr-9-60|LADR 9.60]]); the matrix and operator determinants agree by [[§34 Determinants#^ladr-9-53|LADR 9.53]].
> - For $n = 2$ this is Part I of the first proof of [[§15 Multivariable Integration#^thm-15-14|Theorem §15.14]].
> - For Lebesgue measure the identity $m(T(R)) = |\det T|\, m(R)$ on rectangles is proved by elementary row operations inside [[§18 Differentiation Theory#^thm-18-22|551 Thm. §18.22]] (linear maps preserve null sets).
> - The case n = 3 with worked examples: [[§83 The Cross Product#^thm-83-10|Calc Thm. §83.10]] (volume of a parallelepiped as a determinant).
> - Computational version for n = 2, 3: [[§22 Cramer’s Rule, Volume, and Linear Transformations#^thm-22-4|235 Thm. §22.4]] (determinants as area or volume), [[§22 Cramer’s Rule, Volume, and Linear Transformations#^thm-22-5|235 Thm. §22.5]] and [[§22 Cramer’s Rule, Volume, and Linear Transformations#^thm-22-6|235 Thm. §22.6]] (a linear map multiplies area or volume by its absolute determinant), with worked areas.

This proposition explains why the Jacobian determinant appears in the change of variables formula: locally, the transformation $\Phi$ is approximated by its linearization $J_\Phi$ ([[§6 Differentiability#^def-6-2|Def. §6.2]]), and $|\det(J_\Phi)| = |J|$ measures the local volume distortion.

> [!theorem] Theorem §15.20: Change of Variables in $\mathbb{R}^n$
> Let $D^* \subseteq \mathbb{R}^n$ be bounded and Jordan measurable. Let $\Phi: \overline{D^*} \to \overline{D}$ be a $C^1$ diffeomorphism with Jacobian matrix
>
> $$
> J_\Phi = \frac{\partial(x_1, \ldots, x_n)}{\partial(u_1, \ldots, u_n)} = \begin{pmatrix} \frac{\partial x_1}{\partial u_1} & \cdots & \frac{\partial x_1}{\partial u_n} \\ \vdots & \ddots & \vdots \\ \frac{\partial x_n}{\partial u_1} & \cdots & \frac{\partial x_n}{\partial u_n} \end{pmatrix}.
> $$
>
> If $\det(J_\Phi) \neq 0$ on $D^*$ and $f$ is continuous on $\overline{D}$, then:
>
> $$
> \int_D f(\mathbf{x}) \, d\mathbf{x} = \int_{D^*} f(\Phi(\mathbf{u})) \cdot |\det(J_\Phi(\mathbf{u}))| \, d\mathbf{u}.
> $$

^thm-15-20

*The notes omit the proof: it follows the same structure as the 2D case ([[§15 Multivariable Integration#^pf-15-14-3|Proof 3]] generalizes most directly: decompose into $n$ primitive transformations).*

> [!remark]- Connections
> - Linear-algebra core: [[§34 Determinants#^ladr-9-61|LADR 9.61]] for the local volume factor and [[§34 Determinants#^ladr-9-49|LADR 9.49]] (det is multiplicative) for composing primitive transformations.
> - In $\mathbb{R}^3$: the spherical volume element used in [[§19 The Laplacian in Spherical Coordinates|§19]]; for general dimension it underlies the [[Divergence Theorem in ℝⁿ|Divergence Theorem in ℝⁿ]] and, as pullback of $n$-forms, the [[Generalized Stokes' Theorem|Generalized Stokes' Theorem]].
> - The smooth version of the diffeomorphisms allowed here is [[§16 Differentiable Structures#^def-16-3|591 Def. §16.3]], where diffeomorphisms of open subsets of ℝⁿ are the transition maps between charts.
> - Computational version: [[§106 Change of Variables in Multiple Integrals#^thm-106-2|Calc Thm. §106.2]] (n = 3, with worked examples), with cylindrical and spherical coordinates in [[§104 Triple Integrals in Cylindrical Coordinates#^thm-104-1|Calc Thm. §104.1]] and [[§105 Triple Integrals in Spherical Coordinates#^thm-105-2|Calc Thm. §105.2]].
> - The linear case, where the Jacobian is constant: [[§22 Cramer’s Rule, Volume, and Linear Transformations#^thm-22-6|235 Thm. §22.6]] (with worked areas, n = 2, 3).

### Common Coordinate Systems and Worked Examples

> [!example] Example §15.4: Polar Coordinates
> The transformation $x = r\cos\theta$, $y = r\sin\theta$ maps $(r, \theta) \in [0, \infty) \times [0, 2\pi)$ to $(x, y) \in \mathbb{R}^2$.
>
> The Jacobian is:
>
> $$
> J = \det \begin{pmatrix} \cos\theta & -r\sin\theta \\ \sin\theta & r\cos\theta \end{pmatrix} = r\cos^2\theta + r\sin^2\theta = r.
> $$
>
> Therefore: $dx \, dy = r \, dr \, d\theta$.
>
> Note: $J = r$ vanishes on the whole segment $\{0\} \times [0, 2\pi)$ (all of which maps to the origin), not at isolated points, and the domain is unbounded, so [[§15 Multivariable Integration#^prop-15-18|Proposition §15.18]] does not apply as stated. Its exhaustion argument still works: apply the formula on the region $\varepsilon \leq r \leq R$, where $J \neq 0$, and let $\varepsilon \to 0$ (the removed disk has area $\pi\varepsilon^2$) and, for unbounded domains, $R \to \infty$.

^ex-15-4

> [!remark]- Connections
> - Same Jacobian as [[§13 The Inverse Function Theorem#^ex-13-4|Ex. §13.4]]; derived from scratch by polar rectangles in [[§15 Multivariable Integration#^thm-15-7|Theorem §15.7]].
> - Worked examples: [[§100 Double Integrals in Polar Coordinates#^thm-100-1|Calc Thm. §100.1]], and the Jacobian computation in [[§106 Change of Variables in Multiple Integrals#^ex-106-2|Calc Ex. §106.2]].

> [!example] Example §15.5: Elliptical Coordinates
> For an ellipse with semi-axes $a$ and $b$: $x = ar\cos\theta$, $y = br\sin\theta$.
>
> The Jacobian is:
>
> $$
> J = \det \begin{pmatrix} a\cos\theta & -ar\sin\theta \\ b\sin\theta & br\cos\theta \end{pmatrix} = abr\cos^2\theta + abr\sin^2\theta = abr.
> $$
>
> Therefore: $dx \, dy = abr \, dr \, d\theta$.
>
> This is useful for integrating over elliptical regions.

^ex-15-5

> [!example] Example §15.6: Spherical Coordinates in $\mathbb{R}^3$
> The transformation $x = \rho\sin\phi\cos\theta$, $y = \rho\sin\phi\sin\theta$, $z = \rho\cos\phi$ has Jacobian:
>
> $$
> J = \rho^2 \sin\phi.
> $$
>
> Therefore: $dx \, dy \, dz = \rho^2 \sin\phi \, d\rho \, d\phi \, d\theta$.

^ex-15-6

> [!remark]- Connections
> - The same coordinates parametrize the sphere in [[§18 Surface Integrals#^ex-18-1|Ex. §18.1]] and give the Laplacian in [[§19 The Laplacian in Spherical Coordinates#^thm-19-1|Theorem §19.1]].
> - Worked examples: [[§106 Change of Variables in Multiple Integrals#^ex-106-5|Calc Ex. §106.5]] (same Jacobian), used in [[§105 Triple Integrals in Spherical Coordinates#^thm-105-2|Calc Thm. §105.2]].

We now demonstrate the change of variables formula with two complete computations.

> [!example] Example §15.7: The Gaussian Integral via Polar Coordinates
> **Goal:** Compute $I = \displaystyle\int_{-\infty}^{\infty} e^{-x^2} \, dx$ ([[§36 Improper Integrals#^def-36-2|improper integral]]).
>
> *The trick:* We cannot evaluate $I$ directly (no elementary antiderivative for $e^{-x^2}$), but we *can* evaluate $I^2$.
>
> **Step 1: Square the integral.**
>
> $$
> I^2 = \left( \int_{-\infty}^{\infty} e^{-x^2} \, dx \right)\left( \int_{-\infty}^{\infty} e^{-y^2} \, dy \right) = \iint_{\mathbb{R}^2} e^{-(x^2 + y^2)} \, dx \, dy.
> $$
>
> The second equality uses [[§15 Multivariable Integration#^thm-15-12|Fubini's theorem]] to combine the product of two single integrals into a double integral.
>
> **Step 2: Change to polar coordinates.**
>
> Apply $x = r\cos\theta$, $y = r\sin\theta$ with $J = r$, so $dx \, dy = r \, dr \, d\theta$ ([[§15 Multivariable Integration#^ex-15-4|Ex. §15.4]]). Also, $x^2 + y^2 = r^2$.
>
> The domain $\mathbb{R}^2$ corresponds to $r \in [0, \infty)$, $\theta \in [0, 2\pi)$:
>
> $$
> I^2 = \int_0^{2\pi} \int_0^{\infty} e^{-r^2} \cdot r \, dr \, d\theta.
> $$
>
> **Step 3: Evaluate the inner integral.**
>
> The substitution $u = r^2$, $du = 2r \, dr$ ([[§15 Multivariable Integration#^lem-15-13|Lemma §15.13]]) gives:
>
> $$
> \int_0^{\infty} e^{-r^2} \cdot r \, dr = \frac{1}{2} \int_0^{\infty} e^{-u} \, du = \frac{1}{2} \left[ -e^{-u} \right]_0^{\infty} = \frac{1}{2}.
> $$
>
> **Step 4: Evaluate the outer integral.**
>
> $$
> I^2 = \int_0^{2\pi} \frac{1}{2} \, d\theta = \pi.
> $$
>
> Here $\iint_{\mathbb{R}^2}$ is an improper integral, and Steps 1–2 are justified by exhaustion. On the square $[-R, R]^2$, Fubini gives $\big(\int_{-R}^{R} e^{-x^2}\, dx\big)^2$; on the disk of radius $R$, polar coordinates (as in [[§15 Multivariable Integration#^ex-15-4|Example §15.4]]) give $\int_0^{2\pi}\int_0^R e^{-r^2} r\, dr\, d\theta = \pi(1 - e^{-R^2})$. Since the integrand is positive and the disk of radius $R$ lies in $[-R, R]^2$, which lies in the disk of radius $\sqrt{2}R$,
>
> $$
> \pi(1 - e^{-R^2}) \leq \left( \int_{-R}^{R} e^{-x^2} \, dx \right)^2 \leq \pi(1 - e^{-2R^2}),
> $$
>
> and letting $R \to \infty$ gives $I^2 = \pi$.
>
> **Conclusion:** Since $I > 0$ (the integrand is positive), we obtain:
>
> $$
> \boxed{\int_{-\infty}^{\infty} e^{-x^2} \, dx = \sqrt{\pi}}
> $$
>
> This result is fundamental in probability theory (the normalization constant of the Gaussian distribution) and in physics (partition functions, path integrals).

^ex-15-7

> [!remark]- Connections
> - Pays off the debt taken “on credit” in MATH 451: [[§36 Improper Integrals#^ex-36-4|The normal distribution]] (451 Ex. §36.4).
> - Worked examples: [[§56 Probability#^prop-56-3|Calc Prop. §56.3]] uses this integral to show the normal density integrates to 1.
> - Used in Quantum Mechanics: the Gaussian integral and its continuation to complex width (the Fresnel integrals) behind the free propagator — [[§C4.1 Propagators#^thm-c4-1-3|QM Theorem §C4.1.3]].
> - Computational version: [[§28★ The Error Function#^prop-28-1|341 Prop. §28.1]] (the same polar-coordinates computation, squeezing the square between quarter disks, gives $\operatorname{erf}(\infty)=1$).

> [!example] Example §15.8: Area of an Ellipse
> **Goal:** Compute the area of the ellipse $D = \left\{ (x,y) : \dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} \leq 1 \right\}$.
>
> **Step 1: Choose the coordinate transformation.**
>
> Use elliptical coordinates ([[§15 Multivariable Integration#^ex-15-5|Ex. §15.5]]): $x = ar\cos\theta$, $y = br\sin\theta$. The Jacobian is $J = abr$.
>
> The ellipse $D$ corresponds to $D^* = \{(r, \theta) : 0 \leq r \leq 1, \, 0 \leq \theta < 2\pi\}$.
>
> **Verification:** Under this map, $\dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} = r^2\cos^2\theta + r^2\sin^2\theta = r^2 \leq 1$. ✓
>
> **Step 2: Apply the [[Change of Variables Formula (multiple integrals)|change of variables formula]].**
>
> $$
> \text{Area}(D) = \iint_D 1 \, dx \, dy = \iint_{D^*} 1 \cdot |J| \, dr \, d\theta = \int_0^{2\pi} \int_0^1 abr \, dr \, d\theta.
> $$
>
> **Step 3: Evaluate.**
>
> $$
> \int_0^{2\pi} \int_0^1 abr \, dr \, d\theta = ab \int_0^{2\pi} \left[ \frac{r^2}{2} \right]_0^1 d\theta = ab \int_0^{2\pi} \frac{1}{2} \, d\theta = \frac{ab}{2} \cdot 2\pi = \pi ab.
> $$
>
> **Conclusion:**
>
> $$
> \boxed{\text{Area of the ellipse } \frac{x^2}{a^2} + \frac{y^2}{b^2} \leq 1 \text{ is } \pi ab}
> $$
>
> **Sanity check:** When $a = b = R$, this gives $\pi R^2$, the area of a circle of radius $R$. ✓

^ex-15-8
