---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: CA
section: CA.6
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§CA.5 Gaussian Integrals, Stationary Phase and Bessel Functions]] · ↑ [[· CA Mathematical Methods]]

*Sources: the user's PHY 513 notes, App. A §A.4 (limits), §A.5 (the Sokhotski–Plemelj formula, eq. (SP); the half-residue lemma; Caution "What the formula does and does not say"; worked example (iii)), Ch. 5 §§5.4, 5.7, Ch. 6 §§6.1–6.3, §6.9 · PHY 513, Problem Set 4, eq. (11) · standard results stated here, where marked: Hörmander, The Analysis of Linear Partial Differential Operators I, §§3.1, 3.3, 4.2, 7.3; Gel'fand & Shilov, Generalized Functions, Vol. 1, Ch. I and III; Streater & Wightman, PCT, Spin and Statistics, and All That, Ch. 2.*

Every $i\varepsilon$ of the propagators, the Wightman function defined from the lower half-plane and every Green's function are limits that exist only as generalized functions. This section states them with the tools they need, all of them earlier in the chapter: generalized functions and the principal value ([[§CA.2 Generalized Functions|§CA.2]], [[§CA.2 Generalized Functions#^def-ca-2-10|Def. §CA.2.10]]), Fourier transforms of tempered distributions ([[§CA.3 Fourier Transforms and Fourier Tricks|§CA.3]]), and Cauchy's theorem with the half-residue lemma ([[§CA.4 Contour Integration|§CA.4]]). It contains the boundary values of analytic functions with the Sokhotski–Plemelj formula, which is how every $i\varepsilon$ of [[§C2b.5 Green's Functions and Contours|§C2b.5]]–[[§C2b.7 Wick Rotation and the Two-Point Family|§C2b.7]] is read, the damping factors that produce an $i\varepsilon$ and the $i\varepsilon$ limits of the propagator denominators, and fundamental solutions, of which every Green's function is one. Each statement lists in Connections the places that use it.

## Boundary values of analytic functions


> [!theorem] Theorem §CA.6.1: Boundary Values of Analytic Functions Are Distributions
> 1. Let $F$ be analytic on the strip $0 < \operatorname{Im}z < y_0$ with $|F(x + iy)| \le C(1 + |x|)^Ny^{-k}$ there. Then $F(x + i0) \equiv \lim_{y\to0^+}F(\cdot + iy)$ exists in $\mathcal S'(\mathbb R)$, and it is the $(k + 1)$-th derivative of a continuous, polynomially bounded function. The same holds from below.
> 2. In $n$ variables: if $F$ is analytic on the tube $\mathbb R^n + i\Gamma$ over an open convex cone $\Gamma$, with a bound polynomial in $x$ and in the inverse distance to the boundary, then $\lim_{\eta\to0,\ \eta\in\Gamma}F(\cdot + i\eta)$ exists in $\mathcal S'(\mathbb R^n)$ and does not depend on the direction of approach within $\Gamma$.
>
> *Source: standard; stated here (Hörmander I, §3.1; Streater & Wightman, Ch. 2) · the user's PHY 513 notes, App. A §A.4 (limits; the boundary value defining the Wightman function), Ch. 5 §5.4*

^thm-ca-6-1

> [!derivation]- Derivation
> Part 1; take $y_0 = 2$ and the upper side.
>
> **Step 1** (primitives). The strip is simply connected, so $F$ has analytic primitives ([[§CA.4 Contour Integration#^thm-ca-4-2|Theorem §CA.4.2]]: integrals between two points do not depend on the path). Put $z_{\ast} = i$ and define $G_0 = F$, $G_{j+1}(z) = \int_{z_{\ast}}^zG_j(w)\,dw$; then $G_{k+1}^{(k+1)} = F$.
>
> **Step 2** (each integration lowers the blow-up by one). Integrate along the path $z_{\ast} \to x + i \to x + iy$, horizontal, then vertical. If $|G_j(x + it)| \le C_j(1 + |x|)^{M_j}t^{-k_j}$ for $0 < t \le 1$, the horizontal piece is at most $C_j(1 + |x|)^{M_j + 1}$ and the vertical piece is $\int_y^1C_j(1 + |x|)^{M_j}t^{-k_j}dt$, which is $\le C(1 + |x|)^{M_j}y^{-(k_j - 1)}$ if $k_j \ge 2$, $\le C(1 + |x|)^{M_j}(1 + \ln\frac1y)$ if $k_j = 1$, and bounded if $k_j = 0$. After $k$ integrations $|G_k| \le C(1 + |x|)^{M}(1 + \ln\frac1y)$.
>
> **Step 3** (continuity up to the axis). $G_{k+1}(x + iy) = G_{k+1}(x + i) - i\int_y^1G_k(x + it)\,dt$, and $|G_k(x + it)| \le C(1 + |x|)^M(1 + \ln\frac1t)$ is integrable at $t = 0$. By dominated convergence $G_{k+1}(x + iy) \to G(x)$ as $y \to 0^+$, $G$ is continuous, and $|G_{k+1}(x + iy)| \le C'(1 + |x|)^{M + 1}$ uniformly in $0 < y \le 1$.
>
> **Step 4** (pair with a test function). On a horizontal line the complex derivative is $\partial_x$, so for $\varphi \in \mathcal S$, with $k + 1$ integrations by parts (the boundary terms vanish: $G_j$ grow polynomially, $\varphi^{(i)}$ decay faster than any power),
>
> $$
> \int dx\,F(x + iy)\,\varphi(x) = \int dx\,\partial_x^{k+1}G_{k+1}(x + iy)\,\varphi(x) = (-1)^{k+1}\int dx\,G_{k+1}(x + iy)\,\varphi^{(k+1)}(x) .
> $$
>
> **Step 5** (the limit). The integrand converges pointwise to $G(x)\varphi^{(k+1)}(x)$ and is bounded by $C'(1 + |x|)^{M+1}|\varphi^{(k+1)}(x)|$, integrable and independent of $y$. By dominated convergence the pairing tends to $(-1)^{k+1}\int G\varphi^{(k+1)} = \partial^{k+1}T_G[\varphi]$ ([[§CA.2 Generalized Functions#^def-ca-2-4|Def. §CA.2.4]]), a tempered distribution by [[§CA.2 Generalized Functions#^thm-ca-2-1|Theorem §CA.2.1]], 2.
>
> ⚑ By-product: every boundary value is a finite-order derivative of a continuous function, the order fixed by how fast $F$ blows up at the real axis. Example: $|1/(x + iy)| \le y^{-1}$, $k = 1$, and $1/(x + i0)$ is the derivative of $\log(x + i0)$ ([[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-3|Theorem §CA.6.3]]).
>
> **Step 6** (part 2; sketch). Fix $\eta \in \Gamma$ and run Steps 1–5 in the single complex variable $\tau$ of $F(x + \tau\eta)$, uniformly in $x$; independence of the direction follows because $F$ is analytic between any two directions of $\Gamma$ (Hörmander I, §3.1).
>
> **What the derivation shows.**
> - The "$+i0$" of a boundary value is a limit in $\mathcal S'$; nothing is assigned a value at $\varepsilon = 0$. Analyticity and a polynomial bound are all that is needed.
> - Instances in C2a–C2b: the Wightman function from the lower half $\xi^0$-plane ([[§C2b.2 The Wightman Function#^thm-c2b-2-5|Theorem §C2b.2.5]]), $1/(x \pm i0)$, and the Feynman propagator, analytic in $p^0$ off the two shifted poles.

^der-ca-6-1

*Uses:* [[§CA.4 Contour Integration#^thm-ca-4-2|Theorem §CA.4.2]], [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|Theorem §CA.1.1]], [[§CA.2 Generalized Functions#^def-ca-2-4|Def. §CA.2.4]], [[§CA.2 Generalized Functions#^thm-ca-2-1|Theorem §CA.2.1]]

> [!theorem] Theorem §CA.6.2: Sokhotski–Plemelj Formula
> As generalized functions, for $\varepsilon \to 0^+$,
>
> $$
> \frac{1}{x - x_0 \pm i\varepsilon} \longrightarrow \mathcal P\frac{1}{x - x_0} \mp i\pi\,\delta(x - x_0) .
> $$
>
> Mnemonic: the pole of $1/(x - x_0 - i\varepsilon)$ lies *above* the real path and gives $+i\pi$; a pole below gives $-i\pi$.
>
> *Source: the user's PHY 513 notes, App. A §A.5, eq. (SP) and Derivation "The Sokhotski–Plemelj formula, derived directly" · PHY 513, Problem Set 4, eq. (11)*

^thm-ca-6-2

> [!derivation]- Derivation
> Take the lower sign with $s = x - x_0$; the upper sign is the complex conjugate. Let $\varphi$ be a test function vanishing outside $[-L, L]$.
>
> **Step 1** (split at finite $\varepsilon$). Multiply numerator and denominator by $s + i\varepsilon$:
>
> $$
> \frac{1}{s - i\varepsilon} = \frac{s + i\varepsilon}{s^2 + \varepsilon^2} = \underbrace{\frac{s}{s^2 + \varepsilon^2}}_{\text{real, odd}} + i\,\underbrace{\frac{\varepsilon}{s^2 + \varepsilon^2}}_{\text{real, even}} .
> $$
>
> Both pieces are bounded for $\varepsilon > 0$, but neither has a pointwise limit at $s = 0$, where both are of order $1/\varepsilon$.
>
> **Step 2** (imaginary part: substitute). With $s = \varepsilon u$, $ds = \varepsilon\,du$: $\int\varphi(s)\frac{\varepsilon\,ds}{s^2 + \varepsilon^2} = \int\varphi(\varepsilon u)\frac{du}{1 + u^2}$.
>
> **Step 3** (imaginary part: limit). $\varphi(\varepsilon u) \to \varphi(0)$ for every $u$, and $|\varphi(\varepsilon u)|/(1 + u^2) \le \sup|\varphi|/(1 + u^2)$, integrable and independent of $\varepsilon$. By dominated convergence ([[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|Theorem §CA.1.1]]) the integral tends to $\varphi(0)\int\frac{du}{1 + u^2} = \pi\varphi(0)$ ([[§CA.4 Contour Integration#^ex-ca-4-1|Example §CA.4.1]]). So $\frac{\varepsilon}{s^2 + \varepsilon^2} \to \pi\delta(s)$: the Lorentzian is a nascent delta function of area $\pi$.
>
> **Step 4** (real part: subtract $\varphi(0)$). On $[-L, L]$, $\int_{-L}^L\varphi(0)\frac{s\,ds}{s^2 + \varepsilon^2} = 0$ by oddness, so
>
> $$
> \int_{-L}^{L}\varphi(s)\frac{s\,ds}{s^2 + \varepsilon^2} = \int_{-L}^{L}\frac{\varphi(s) - \varphi(0)}{s}\cdot\frac{s^2}{s^2 + \varepsilon^2}\,ds .
> $$
>
> **Step 5** (real part: limit). The difference quotient $[\varphi(s) - \varphi(0)]/s$ is bounded (by $\sup|\varphi'|$), and $0 \le s^2/(s^2 + \varepsilon^2) \le 1$ tends to $1$ for every $s \ne 0$. By dominated convergence the integral tends to $\int_{-L}^L\frac{\varphi(s) - \varphi(0)}{s}ds = \mathcal P\!\int\frac{\varphi}{s}$ ([[§CA.2 Generalized Functions#^def-ca-2-10|Def. §CA.2.10]]).
>
> ⚑ By-product: the subtraction of $\varphi(0)$ must be done on a bounded symmetric interval. The user's notes write these integrals over all of $\mathbb R$, where the subtracted $\varphi(0)/s$ is not integrable at infinity and would need a symmetric limit there as well; the bounded interval is the safe form.
>
> **Step 6** (assemble). $\frac{1}{s - i\varepsilon} \to \mathcal P\frac1s + i\pi\delta(s)$, the lower sign of the formula; conjugating gives the upper.
>
> **What the derivation shows.**
> - The real part is the principal value and the imaginary part the delta function, and nothing else enters; a smooth symmetric cutoff gives the same answer as the sharp one in the definition.
> - The factor $\pi$ is the area of the Lorentzian, the same $\pi$ that $\int du/(1 + u^2)$ gives by residues.
> - Used in: the massless commutator ([[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-8|Theorem §C2b.4.8]]), the differences of Green's functions on the shell ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-11|Theorem §C2b.6.11]]), the principal function ([[§C2b.7 Wick Rotation and the Two-Point Family#^thm-c2b-7-5|Theorem §C2b.7.5]]).

^der-ca-6-2

*Uses:* [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|Theorem §CA.1.1]], [[§CA.2 Generalized Functions#^def-ca-2-10|Def. §CA.2.10]], [[§CA.4 Contour Integration#^ex-ca-4-1|Example §CA.4.1]]

> [!derivation]- Derivation (second route: the half-residue lemma)
> **Step 1.** For integrands $f = g/(x - x_0)$ with $g$ analytic near $x_0$ (every propagator integrand is of this kind), a small semicircle passing above the pole gives $\mathcal P\!\int f - i\pi g(x_0)$ and one passing below gives $\mathcal P\!\int f + i\pi g(x_0)$ ([[§CA.4 Contour Integration#^thm-ca-4-7|Theorem §CA.4.7]]).
>
> **Step 2.** By Cauchy's theorem ([[§CA.4 Contour Integration#^thm-ca-4-2|Theorem §CA.4.2]]), keeping the path on the real axis with the pole moved down to $x_0 - i\varepsilon$, i.e. the denominator $x - x_0 + i\varepsilon$, equals passing above the pole: the upper sign, $\mathcal P - i\pi\delta$. Moving the pole up gives the lower sign.
>
> **What the derivation shows.**
> - The two prescriptions differ by a full loop, $2\pi i\,g(x_0)$, and the principal value is their average. This route needs analyticity of $g$; the direct route works for every test function.
>
> *Source: the user's PHY 513 notes, App. A §A.5 (Derivation "The half-residue lemma")*

*Uses:* [[§CA.4 Contour Integration#^thm-ca-4-7|Theorem §CA.4.7]], [[§CA.4 Contour Integration#^thm-ca-4-2|Theorem §CA.4.2]]

> [!caution] Caution: What the formula does and does not say
> Pointwise it is empty: at $x \ne x_0$, $\delta = 0$ and $\mathcal P\frac{1}{x - x_0}$ acts as $\frac{1}{x - x_0}$, so it reads $\frac{1}{x - x_0} = \frac{1}{x - x_0}$. Its whole content sits at $x = x_0$, where $\frac{1}{s \mp i\varepsilon} \sim \pm\frac{i}{\varepsilon}$ has no value; what it specifies is what that divergence does under an integral. So an $i\varepsilon$ expression may be evaluated at $\varepsilon = 0$ wherever its denominator does not vanish, and the formula is needed only where it does.
>
> *Source: the user's PHY 513 notes, App. A §A.5 (Caution "What the formula does and does not say")*

^cau-ca-6-1

> [!theorem] Theorem §CA.6.3: Logarithm and Powers at the Real Axis
> With the principal branch of $\log$ (cut along the negative real axis), as distributions on $\mathbb R$:
> 1. $\log(x \pm i0) = \ln|x| \pm i\pi\,\theta(-x)$;
> 2. $\dfrac{d}{dx}\log(x \pm i0) = \dfrac{1}{x \pm i0} = \mathcal P\dfrac1x \mp i\pi\,\delta(x)$;
> 3. $\dfrac{1}{(x \pm i0)^2} \equiv -\dfrac{d}{dx}\dfrac{1}{x \pm i0} = -\dfrac{d}{dx}\mathcal P\dfrac1x \pm i\pi\,\delta'(x)$.
>
> *Source: standard; stated here (Gel'fand & Shilov 1, Ch. I)*

^thm-ca-6-3

> [!derivation]- Derivation
> **Step 1** (pointwise limit). For $x > 0$, $\log(x \pm iy) \to \ln x$. For $x < 0$, $\log(x \pm iy) = \ln|x \pm iy| + i\arg(x \pm iy)$, and $\arg(x + iy) \to \pi$, $\arg(x - iy) \to -\pi$ as $y \to 0^+$ (the points approach the cut from above and from below). So the limit is $\ln|x| \pm i\pi\theta(-x)$ for $x \ne 0$.
>
> **Step 2** (domination). For $0 < y < 1$: $|x| \le |x \pm iy| \le |x| + 1$, so $\ln|x| \le \ln|x \pm iy| \le \ln(1 + |x|)$ and $|\log(x \pm iy)| \le |\ln|x|| + \ln(1 + |x|) + \pi$. This bound times $|\varphi|$ is integrable ($\ln|x|$ is integrable at $0$). By dominated convergence the pairing converges to that of $\ln|x| \pm i\pi\theta(-x)$: part 1, the case $k = 0$ of [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-1|Theorem §CA.6.1]].
>
> **Step 3** (part 2: differentiate the limit). For $y > 0$, $\frac{d}{dx}\log(x \pm iy) = \frac{1}{x \pm iy}$. Derivatives commute with distributional limits ([[§CA.2 Generalized Functions#^thm-ca-2-5|Theorem §CA.2.5]], 2), so $\frac{d}{dx}\log(x \pm i0) = \lim\frac{1}{x \pm iy} = \frac{1}{x \pm i0}$.
>
> **Step 4** (part 2: differentiate the right side). $\frac{d}{dx}\theta(-x) = -\delta(x)$ ([[§CA.2 Generalized Functions#^thm-ca-2-4|Theorem §CA.2.4]], 2, with the substitution $x \to -x$ of [[§CA.2 Generalized Functions#^thm-ca-2-6|Theorem §CA.2.6]], 1). For $\ln|x|$, by Def. §CA.2.4 and two integrations by parts on $(-\infty, -\delta]$ and $[\delta, \infty)$:
>
> $$
> -\int\ln|x|\,\varphi'(x)\,dx = \lim_{\delta\to0^+}\Bigl[\ln\delta\,\bigl(\varphi(\delta) - \varphi(-\delta)\bigr) + \int_{|x| > \delta}\frac{\varphi(x)}{x}\,dx\Bigr] = \mathcal P\!\!\int\frac{\varphi(x)}{x}\,dx ,
> $$
>
> since $|\varphi(\delta) - \varphi(-\delta)| \le 2\delta\sup|\varphi'|$ and $\delta\ln\delta \to 0$. So $\frac{d}{dx}\ln|x| = \mathcal P\frac1x$, and $\frac{1}{x \pm i0} = \mathcal P\frac1x \mp i\pi\delta(x)$.
>
> ⚑ By-product: this is the Sokhotski–Plemelj formula by a third route ([[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-2|Theorem §CA.6.2]]): differentiate the logarithm's jump.
>
> **Step 5** (part 3). For $y > 0$, $\frac{d}{dx}\frac{1}{x \pm iy} = -\frac{1}{(x \pm iy)^2}$; take the limit with Theorem §CA.2.5, 2, and differentiate part 2: $-\frac{d}{dx}\bigl[\mathcal P\frac1x \mp i\pi\delta\bigr] = -\frac{d}{dx}\mathcal P\frac1x \pm i\pi\delta'$.
>
> **What the derivation shows.**
> - The logarithm is the mildest boundary value (a function, $k = 0$); every negative power follows from it by differentiation, and the $\pm i\pi$ is the jump of the argument across the cut.
> - The logarithms in the Wightman function near the light cone ([[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-5|Theorem §C2b.3.5]]) are of this kind.

^der-ca-6-3

*Uses:* [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-1|Theorem §CA.6.1]], [[§CA.2 Generalized Functions#^thm-ca-2-5|Theorem §CA.2.5]], [[§CA.2 Generalized Functions#^thm-ca-2-4|Theorem §CA.2.4]], [[§CA.2 Generalized Functions#^thm-ca-2-6|Theorem §CA.2.6]], [[§CA.2 Generalized Functions#^def-ca-2-10|Def. §CA.2.10]]

> [!theorem] Theorem §CA.6.4: The Light-Cone Boundary Value
> On $\mathbb R^4$, with $t = x^0$, $r = |\mathbf x|$ and $F_\varepsilon(x) = 1/\bigl(-(t - i\varepsilon)^2 + r^2\bigr)$:
> 1. $F_\varepsilon$ converges as $\varepsilon \to 0^+$ in $\mathcal S'(\mathbb R^4)$; the limit is written $1/(-x^2 + i0\,x^0)$, since $-(t - i\varepsilon)^2 + r^2 = -x^2 + 2i\varepsilon t + \varepsilon^2$.
> 2. Its imaginary part is $-\pi\operatorname{sgn}(x^0)\,\delta(x^2)$ (with $\delta(x^2)$ as in [[§CA.2 Generalized Functions#^thm-ca-2-7|Theorem §CA.2.7]], 2); its real part is $-\mathcal P\frac{1}{x^2} \equiv -\frac{1}{2r}\bigl[\mathcal P\frac{1}{t - r} - \mathcal P\frac{1}{t + r}\bigr]$, which is the function $-1/x^2$ off the cone.
> 3. Its singular support is the light cone $x^2 = 0$, and it is Lorentz invariant.
>
> *Source: standard; stated here (Gel'fand & Shilov 1, Ch. III; Streater & Wightman, Ch. 2) · the user's PHY 513 notes, Ch. 5 §§5.4, 5.7 (the massless Wightman and commutator functions)*

^thm-ca-6-4

> [!derivation]- Derivation
> **Step 1** (analytic, with a bound). Write $z = t - iy$, $y > 0$. Then $z^2 - r^2 = (z - r)(z + r)$, and each factor has imaginary part $-y$, so $|z^2 - r^2| \ge y^2$: $F$ is analytic in the lower half $t$-plane at each $\mathbf x$, with $|F| \le y^{-2}$ ($k = 2$, $N = 0$ in [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-1|Theorem §CA.6.1]]).
>
> **Step 2** (a second primitive, uniform in $\mathbf x$). For $r > 0$ define $G(z, r) = \frac{1}{2r}\int_{-r}^{r}\log(z - s)\,ds$, the average of $\log(z - s)$ over $s \in [-r, r]$. Differentiating under the integral,
>
> $$
> \partial_zG = \frac{1}{2r}\int_{-r}^{r}\frac{ds}{z - s} = \frac{1}{2r}\bigl[\log(z + r) - \log(z - r)\bigr], \qquad \partial_z^2G = \frac{1}{2r}\Bigl[\frac{1}{z + r} - \frac{1}{z - r}\Bigr] = \frac{-1}{z^2 - r^2} = F .
> $$
>
> **Step 3** (the bound on $G$; sketch — the full estimate is standard and not written out here). By Step 2 of [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-3|Theorem §CA.6.3]], for $0 < y < 1$, $|\log(t - s - iy)| \le |\ln|t - s|| + \ln(1 + |t| + r) + \pi$. Averaging over $s \in [-r, r]$: $|G(t - iy, r)| \le \frac{1}{2r}\int_{-r}^{r}|\ln|t - s||\,ds + \ln(1 + |t| + r) + \pi \le C\bigl(1 + |\ln r| + \ln(1 + |t| + r)\bigr)$, because the average of $|\ln|u||$ over an interval of length $2r$ is at most $1 + |\ln r|$ up to a constant. This bound is independent of $y$ and locally integrable on $\mathbb R^4$ ($|\ln r|$ is integrable against $d^3x$).
>
> **Step 4** (pair and take the limit). For $\varphi \in \mathcal S(\mathbb R^4)$, integrate by parts twice in $t$ at fixed $\mathbf x$ (boundary terms vanish: $G$ grows logarithmically):
>
> $$
> \int d^4x\,F_\varepsilon\,\varphi = \int d^3x\int dt\,G(t - i\varepsilon, r)\,\partial_t^2\varphi(t, \mathbf x) .
> $$
>
> As $\varepsilon \to 0^+$, $G(t - i\varepsilon, r) \to G(t - i0, r)$ for almost every $(t, \mathbf x)$ (part 1 of Theorem §CA.6.3 inside the average), dominated by Step 3 times $|\partial_t^2\varphi|$. By dominated convergence the limit exists and equals $\partial_t^2$ of the locally integrable, polynomially bounded function $G(t - i0, r)$: a tempered distribution. This is part 1.
>
> **Step 5** (part 2: partial fractions at fixed $r > 0$). $F_\varepsilon = -\frac{1}{2r}\Bigl[\frac{1}{t - r - i\varepsilon} - \frac{1}{t + r - i\varepsilon}\Bigr]$. By Sokhotski–Plemelj in $t$ ([[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-2|Theorem §CA.6.2]], lower sign: $\frac{1}{s - i0} = \mathcal P\frac1s + i\pi\delta(s)$),
>
> $$
> F_0 = -\frac{1}{2r}\Bigl[\mathcal P\frac{1}{t - r} - \mathcal P\frac{1}{t + r}\Bigr] - \frac{i\pi}{2r}\bigl[\delta(t - r) - \delta(t + r)\bigr] .
> $$
>
> **Step 6** (part 2: identify the delta terms). By [[§CA.2 Generalized Functions#^thm-ca-2-6|Theorem §CA.2.6]], 2, $\delta(t^2 - r^2) = [\delta(t - r) + \delta(t + r)]/2r$; multiplying by $\operatorname{sgn}t$, which is $+1$ at $t = r$ and $-1$ at $t = -r$, gives $\operatorname{sgn}(t)\delta(t^2 - r^2) = [\delta(t - r) - \delta(t + r)]/2r$. So the imaginary part is $-\pi\operatorname{sgn}(x^0)\delta(x^2)$. The $\mathbf x$-integral near $r = 0$ converges: the delta terms give $\int d^3x\,\varphi(\pm r, \mathbf x)/2r$ as in [[§CA.2 Generalized Functions#^thm-ca-2-7|Theorem §CA.2.7]], 2, and the bracket of principal values is $h(r) - h(-r)$ with $h(s) = \mathcal P\!\int dt\,\varphi(t, \mathbf x)/(t - s)$ smooth in $s$, so it is $O(r)$ and the $\frac{1}{2r}$ is harmless.
>
> **Step 7** (part 3; invariance sketch). Off the cone, $F_\varepsilon \to -1/x^2$ uniformly with all derivatives on compact sets, so the limit is smooth there; on the cone the delta term of part 2 is not smooth. For invariance: $1/(-z\cdot z)$, $z = x - i\eta$, is analytic on the tube $\eta \in V_+$ (the open forward cone), because $\operatorname{Im}(z\cdot z) = -2x\cdot\eta$ and $\operatorname{Re}(z\cdot z) = x^2 - \eta^2$ cannot both vanish there: $x\cdot\eta = 0$ with $\eta$ timelike forces $x^2 \le 0$, so $\operatorname{Re} < 0$. A proper orthochronous $\Lambda$ maps the tube to itself and leaves $z\cdot z$ unchanged; the boundary value does not depend on the direction of approach within $V_+$ ([[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-1|Theorem §CA.6.1]], 2), so approaching along $(\varepsilon, \mathbf 0)$ or along $\Lambda(\varepsilon, \mathbf 0)$ gives the same distribution.
>
> **What the derivation shows.**
> - $\frac{1}{4\pi^2}\cdot\frac{1}{-x^2 + i0\,x^0}$ is the massless Wightman function; its imaginary part, $-\frac{1}{4\pi}\operatorname{sgn}(x^0)\delta(x^2)$, is half the massless commutator function, and its real part gives the Hadamard function ([[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-8|Theorem §C2b.4.8]]).
> - The "$-i\varepsilon x^0$" prescription is a boundary value from the forward tube, which is why it is Lorentz invariant although it singles out $x^0$.

^der-ca-6-4

*Uses:* [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-1|Theorem §CA.6.1]], [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-2|Theorem §CA.6.2]], [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-3|Theorem §CA.6.3]], [[§CA.2 Generalized Functions#^thm-ca-2-6|Theorem §CA.2.6]], [[§CA.2 Generalized Functions#^thm-ca-2-7|Theorem §CA.2.7]], [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|Theorem §CA.1.1]]

## Damping factors and iε

> [!theorem] Theorem §CA.6.5: Damping Factors: the Transform of the Step Function
> For real $\omega$ and $\varepsilon > 0$, $\int_0^\infty dt\,e^{i\omega t - \varepsilon t} = \dfrac{i}{\omega + i\varepsilon}$. As $\varepsilon \to 0^+$, in $\mathcal S'(\mathbb R)$,
>
> $$
> \tilde\theta(\omega) = \int dt\,\theta(t)\,e^{i\omega t} = \frac{i}{\omega + i0} = i\,\mathcal P\frac1\omega + \pi\,\delta(\omega) .
> $$
>
> Conversely $\int\frac{d\omega}{2\pi}e^{-i\omega t}\frac{i}{\omega + i\varepsilon} = \theta(t)\,e^{-\varepsilon t}$: a damping factor on $t > 0$ puts the pole below the real axis.
>
> *Source: standard; stated here · the user's PHY 513 notes, App. A §A.5 (worked example (iii)), Ch. 6 §6.9 (poles moved off the axis)*

^thm-ca-6-5

> [!derivation]- Derivation
> **Step 1** (finite ε). $\int_0^\infty e^{(i\omega - \varepsilon)t}dt = \Bigl[\frac{e^{(i\omega - \varepsilon)t}}{i\omega - \varepsilon}\Bigr]_0^\infty = 0 - \frac{1}{i\omega - \varepsilon} = \frac{1}{\varepsilon - i\omega}$; the upper limit vanishes because $|e^{(i\omega - \varepsilon)t}| = e^{-\varepsilon t}$. Multiplying numerator and denominator by $i$: $\frac{i}{i\varepsilon + \omega} = \frac{i}{\omega + i\varepsilon}$.
>
> **Step 2** (regulated step function). $\theta_\varepsilon(t) = \theta(t)e^{-\varepsilon t} \to \theta$ in $\mathcal S'$ (dominated convergence, $|\theta_\varepsilon\varphi| \le |\varphi|$). Its transform is the function of Step 1, so by [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-2|Theorem §CA.3.2]], 2, $\tilde\theta = \lim_{\varepsilon\to0^+}\frac{i}{\omega + i\varepsilon}$.
>
> **Step 3** (Sokhotski–Plemelj). $\frac{1}{\omega + i\varepsilon} \to \mathcal P\frac1\omega - i\pi\delta(\omega)$ ([[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-2|Theorem §CA.6.2]], upper sign), so $\frac{i}{\omega + i\varepsilon} \to i\mathcal P\frac1\omega + \pi\delta(\omega)$.
>
> **Step 4** (check). $\theta = \frac12 + \frac12\operatorname{sgn}$. The transform of $\frac12$ is $\frac12\cdot2\pi\delta(\omega) = \pi\delta(\omega)$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]], $n = 1$), the even part. The odd part, $\frac12\widetilde{\operatorname{sgn}} = i\mathcal P\frac1\omega$, is the transform of $\frac12\operatorname{sgn}$: Steps 1–3 applied to $\theta(-t)$ give $-\frac{i}{\omega - i0}$, and $\widetilde{\operatorname{sgn}} = \frac{i}{\omega + i0} + \frac{i}{\omega - i0} = 2i\mathcal P\frac1\omega$.
>
> **Step 5** (converse). $\frac{1}{2\pi}\int d\omega\,e^{-i\omega t}\frac{i}{\omega + i\varepsilon}$ has its pole at $\omega = -i\varepsilon$. For $t > 0$, $|e^{-i\omega t}| = e^{t\operatorname{Im}\omega}$ decays in the lower half-plane: close downward, clockwise ([[§CA.4 Contour Integration#^thm-ca-4-6|Theorem §CA.4.6]], Jordan, since $\frac{i}{2\pi(\omega + i\varepsilon)} \to 0$), enclosing the pole with residue $\frac{i}{2\pi}e^{-i(-i\varepsilon)t} = \frac{i}{2\pi}e^{-\varepsilon t}$; the integral is $-2\pi i\cdot\frac{i}{2\pi}e^{-\varepsilon t} = e^{-\varepsilon t}$. For $t < 0$ close upward: no pole, $0$. Together $\theta(t)e^{-\varepsilon t}$ ([[§CA.4 Contour Integration#^ex-ca-4-2|Example §CA.4.2]] is the same computation).
>
> **What the derivation shows.**
> - "$i\varepsilon$ from damping": a factor $e^{-\varepsilon t}$ that makes $\int_0^\infty$ converge moves the pole to $\omega = -i\varepsilon$, below the axis; the side of the pole encodes the direction of time.
> - The real part $\pi\delta(\omega)$ is the mean value $\frac12$ of the step; the principal value is its jump.
> - Used next: the iε of every propagator denominator ([[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-6|Theorem §CA.6.6]]).

^der-ca-6-5

*Uses:* [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-2|Theorem §CA.3.2]], [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-2|Theorem §CA.6.2]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]], [[§CA.4 Contour Integration#^thm-ca-4-6|Theorem §CA.4.6]]

> [!theorem] Theorem §CA.6.6: The iε Limits of the Propagator Denominators
> For $m > 0$, as $\varepsilon \to 0^+$, in $\mathcal S'(\mathbb R^4)$:
> 1. $\dfrac{1}{p^2 - m^2 + i\varepsilon} \to \mathcal P\dfrac{1}{p^2 - m^2} - i\pi\,\delta(p^2 - m^2)$, so $\dfrac{i}{p^2 - m^2 + i\varepsilon} \to i\,\mathcal P\dfrac{1}{p^2 - m^2} + \pi\,\delta(p^2 - m^2)$; complex conjugate for $-i\varepsilon$.
> 2. $\dfrac{1}{(p^0 + i\varepsilon)^2 - \mathbf p^2 - m^2} \to \mathcal P\dfrac{1}{p^2 - m^2} - i\pi\operatorname{sgn}(p^0)\,\delta(p^2 - m^2)$; complex conjugate for $p^0 - i\varepsilon$.
> 3. Replacing $\varepsilon$ by $\varepsilon\,c(\mathbf p)$ with $c$ smooth and positive (for example $2E_{\mathbf p}\varepsilon \to \varepsilon$) does not change the limits.
>
> Here $\mathcal P\frac{1}{p^2 - m^2} \equiv \frac{1}{2E_{\mathbf p}}\bigl[\mathcal P\frac{1}{p^0 - E_{\mathbf p}} - \mathcal P\frac{1}{p^0 + E_{\mathbf p}}\bigr]$, applied in $p^0$ at fixed $\mathbf p$.
>
> *Source: the user's PHY 513 notes, Ch. 6 §6.9 (Derivation "The distributional version: Sokhotski–Plemelj"; "only the sign of the infinitesimal matters") · justified here*

^thm-ca-6-6

> [!derivation]- Derivation
> **Step 1** (factor at fixed $\mathbf p$). $p^2 - m^2 + i\varepsilon = (p^0)^2 - (E_{\mathbf p}^2 - i\varepsilon) = (p^0 - E_\varepsilon)(p^0 + E_\varepsilon)$ with $E_\varepsilon = \sqrt{E_{\mathbf p}^2 - i\varepsilon}$ (principal root). Writing $E_\varepsilon = a - ib$: $a^2 - b^2 = E_{\mathbf p}^2$ and $2ab = \varepsilon$, so $b = \varepsilon/2a > 0$ and $a = E_{\mathbf p} + O(\varepsilon^2)$.
>
> **Step 2** (partial fractions). $\frac{1}{(p^0)^2 - E_\varepsilon^2} = \frac{1}{2E_\varepsilon}\Bigl[\frac{1}{p^0 - E_\varepsilon} - \frac{1}{p^0 + E_\varepsilon}\Bigr]$; check: the numerator is $(p^0 + E_\varepsilon) - (p^0 - E_\varepsilon) = 2E_\varepsilon$.
>
> **Step 3** (Sokhotski–Plemelj in $p^0$). $p^0 - E_\varepsilon = p^0 - a + ib$, so $\frac{1}{p^0 - E_\varepsilon} \to \mathcal P\frac{1}{p^0 - E_{\mathbf p}} - i\pi\delta(p^0 - E_{\mathbf p})$; $p^0 + E_\varepsilon = p^0 + a - ib$, so $\frac{1}{p^0 + E_\varepsilon} \to \mathcal P\frac{1}{p^0 + E_{\mathbf p}} + i\pi\delta(p^0 + E_{\mathbf p})$ ([[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-2|Theorem §CA.6.2]]). The shift of the real part, $a - E_{\mathbf p} = O(\varepsilon^2)$, is harmless: $\int dp^0\frac{\varphi(p^0)}{p^0 - a + ib} = \int ds\frac{\varphi(s + a - E_{\mathbf p})}{s - E_{\mathbf p} + ib}$ with $s = p^0 - a + E_{\mathbf p}$, and $\varphi(\cdot + a - E_{\mathbf p}) \to \varphi$ in $\mathcal S$.
>
> **Step 4** (combine). $\frac{1}{2E_\varepsilon} \to \frac{1}{2E_{\mathbf p}}$, and
>
> $$
> \frac{1}{2E_{\mathbf p}}\Bigl[\mathcal P\frac{1}{p^0 - E_{\mathbf p}} - \mathcal P\frac{1}{p^0 + E_{\mathbf p}}\Bigr] - i\pi\,\frac{\delta(p^0 - E_{\mathbf p}) + \delta(p^0 + E_{\mathbf p})}{2E_{\mathbf p}} = \mathcal P\frac{1}{p^2 - m^2} - i\pi\,\delta(p^2 - m^2) ,
> $$
>
> the last by [[§CA.2 Generalized Functions#^thm-ca-2-6|Theorem §CA.2.6]], 2. Multiplying by $i$ gives the second form of part 1.
>
> **Step 5** (from $p^0$ to $\mathbb R^4$; sketch). Steps 1–4 hold at each $\mathbf p$. To integrate over $\mathbf p$ against $\varphi \in \mathcal S(\mathbb R^4)$ one needs a bound uniform in $\varepsilon$: the derivation of Sokhotski–Plemelj bounds the $p^0$-pairing by $C\sup_{p^0}(1 + |p^0|)^2(|\varphi| + |\partial_0\varphi|)$, and since $E_{\mathbf p} \ge m$ the constant is uniform in $\mathbf p$; for Schwartz $\varphi$ this decays faster than any power of $|\mathbf p|$, and dominated convergence in $\mathbf p$ finishes.
>
> **Step 6** (part 2). $(p^0 + i\varepsilon)^2 - E_{\mathbf p}^2 = (p^0 - E_{\mathbf p} + i\varepsilon)(p^0 + E_{\mathbf p} + i\varepsilon)$: both poles, $\pm E_{\mathbf p} - i\varepsilon$, are below the axis, and the partial fractions are exact with $2E_{\mathbf p}$: $\frac{1}{2E_{\mathbf p}}\Bigl[\frac{1}{p^0 - E_{\mathbf p} + i\varepsilon} - \frac{1}{p^0 + E_{\mathbf p} + i\varepsilon}\Bigr]$. Each term has the upper sign of Sokhotski–Plemelj, so the limit is
>
> $$
> \frac{1}{2E_{\mathbf p}}\Bigl[\mathcal P\frac{1}{p^0 - E_{\mathbf p}} - \mathcal P\frac{1}{p^0 + E_{\mathbf p}}\Bigr] - i\pi\,\frac{\delta(p^0 - E_{\mathbf p}) - \delta(p^0 + E_{\mathbf p})}{2E_{\mathbf p}} = \mathcal P\frac{1}{p^2 - m^2} - i\pi\operatorname{sgn}(p^0)\,\delta(p^2 - m^2) .
> $$
>
> **Step 7** (part 3). At fixed $\mathbf p$, $c(\mathbf p)$ is a positive constant, and Steps 1–3 only use $b > 0$ and $b \to 0$; the uniformity of Step 5 holds if $c$ is bounded above and below on bounded sets of $\mathbf p$ and grows at most polynomially.
>
> **What the derivation shows.**
> - The $i\varepsilon$ denominators are limits in $\mathcal S'$; they agree with $1/(p^2 - m^2)$ off the mass shell and differ only on it, by $\delta(p^2 - m^2)$ or $\operatorname{sgn}(p^0)\delta(p^2 - m^2)$: so $\varepsilon = 0$ may be set wherever $p^2 \ne m^2$ ([[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^cau-ca-6-1|§CA.6, Caution: What the formula does and does not say]]).
> - Both shell terms are Lorentz invariant ([[§CA.2 Generalized Functions#^thm-ca-2-7|Theorem §CA.2.7]]): the Feynman prescription is manifestly so, the retarded one under orthochronous transformations only.
> - Used in: the Feynman propagator and the differences on the shell ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-9|Theorem §C2b.6.9]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-11|Theorem §C2b.6.11]]), the family relations ([[§C2b.7 Wick Rotation and the Two-Point Family#^thm-c2b-7-5|Theorem §C2b.7.5]]).

^der-ca-6-6

*Uses:* [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-2|Theorem §CA.6.2]], [[§CA.2 Generalized Functions#^thm-ca-2-6|Theorem §CA.2.6]], [[§CA.2 Generalized Functions#^thm-ca-2-7|Theorem §CA.2.7]], [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|Theorem §CA.1.1]]

## Fundamental solutions

> [!definition] Definition §CA.6.1: Fundamental Solution
> For a linear differential operator $P(\partial)$ with constant coefficients on $\mathbb R^n$, a **fundamental solution** is a distribution $G$ with $P(\partial)G = -i\,\delta^n$ in the sense of [[§CA.2 Generalized Functions#^def-ca-2-4|Def. §CA.2.4]], i.e. $G[P(-\partial)\varphi] = -i\varphi(0)$ for every $\varphi \in \mathcal D$. For the Klein–Gordon operator, $(\partial^2 + m^2)G = -i\delta^4$; the factor $-i$ is the Peskin–Schroeder normalization, $G = -i\times$ the mathematicians' fundamental solution.
>
> *Source: the user's PHY 513 notes, Ch. 6 §6.2 (Principle "The Green's function is a linear map, and there is one per boundary condition") · standard (Hörmander I, §§3.3, 7.3)*

^def-ca-6-1

> [!theorem] Theorem §CA.6.7: Fundamental Solutions Differ by Homogeneous Solutions
> 1. If $G_1$, $G_2$ are fundamental solutions of $P(\partial)$, then $H = G_1 - G_2$ solves $P(\partial)H = 0$ as a distribution; conversely $G_1 + H$ is a fundamental solution for every distributional solution $H$ of the homogeneous equation.
> 2. For tempered $G$, $H$ and the Klein–Gordon operator, $(m^2 - p^2)\tilde G = -i$ and $(m^2 - p^2)\tilde H = 0$, so $\operatorname{supp}\tilde H$ lies on the mass shell $p^2 = m^2$.
> 3. A homogeneous solution of the Klein–Gordon equation supported at one point is zero: two fundamental solutions that agree away from a point agree everywhere.
>
> *Source: the user's PHY 513 notes, Ch. 6 §6.2 (one Green's function per boundary condition), §6.3 (Principle "Free fields live on the mass shell") · standard*

^thm-ca-6-7

> [!derivation]- Derivation
> **Step 1** (part 1). Derivatives of distributions are linear (Def. §CA.2.4), so $P(\partial)H = P(\partial)G_1 - P(\partial)G_2 = -i\delta + i\delta = 0$; and $P(\partial)(G_1 + H) = -i\delta + 0$.
>
> **Step 2** (part 2: Fourier side). By the derivative rule in $\mathcal S'$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-5|Theorem §CA.3.5]], 3), $\partial^2 + m^2 \to m^2 - p^2$; and $\tilde\delta^4 = 1$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-2|Theorem §CA.3.2]], 3). So the equations become $(m^2 - p^2)\tilde G = -i$ and $(m^2 - p^2)\tilde H = 0$.
>
> **Step 3** (part 2: support). Let $\varphi \in \mathcal D(\mathbb R^4)$ vanish near the shell. Then $\psi = \varphi/(m^2 - p^2)$ is again in $\mathcal D$ (the denominator does not vanish on the support of $\varphi$), and
>
> $$
> \tilde H[\varphi] = \tilde H\bigl[(m^2 - p^2)\psi\bigr] = \bigl((m^2 - p^2)\tilde H\bigr)[\psi] = 0 .
> $$
>
> So $\tilde H$ vanishes on the open set off the shell ([[§CA.2 Generalized Functions#^def-ca-2-3|Def. §CA.2.3]]).
>
> ⚑ By-product: a solution of the free equation has no Fourier components off the mass shell, as a statement about distributions → [[§C2b.1 Heisenberg Fields#^thm-c2b-1-3|Theorem §C2b.1.3]].
>
> **Step 4** (part 3). If $\operatorname{supp}H \subseteq \{a\}$, then $H = \sum_{|\alpha| \le N}c_\alpha\partial^\alpha\delta(x - a)$ ([[§CA.2 Generalized Functions#^thm-ca-2-2|Theorem §CA.2.2]]). Its transform is $e^{ip\cdot a}Q(p)$ with $Q$ a polynomial: each $\partial^\alpha\delta$ transforms into a monomial in the components of $p$ times a constant, and the translation gives the phase ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-5|Theorem §CA.3.5]], 1). The equation $(m^2 - p^2)e^{ip\cdot a}Q(p) = 0$ for all $p$ forces $(m^2 - p^2)Q(p) = 0$ as a polynomial, and since $m^2 - p^2$ is not the zero polynomial, $Q = 0$: all $c_\alpha = 0$.
>
> **What the derivation shows.**
> - Choosing a Green's function is choosing which homogeneous solution, built on the mass shell, to add; contours are this choice in momentum space ([[§C2b.5 Green's Functions and Contours#^thm-c2b-5-3|Theorem §C2b.5.3]]).
> - The differences $\tilde D_F - \tilde D_{\bar F}$ and $\tilde D_R - \tilde D_A$ are supported on the shell for this reason ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-11|Theorem §C2b.6.11]]).
> - Part 3 removes the δ-ambiguity in extending $\theta(x^0)D(x)$ across $x = 0$ ([[§CA.2 Generalized Functions#^thm-ca-2-8|Theorem §CA.2.8]]).

^der-ca-6-7

*Uses:* [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^def-ca-6-1|Def. §CA.6.1]], [[§CA.2 Generalized Functions#^def-ca-2-4|Def. §CA.2.4]], [[§CA.2 Generalized Functions#^def-ca-2-3|Def. §CA.2.3]], [[§CA.2 Generalized Functions#^thm-ca-2-2|Theorem §CA.2.2]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-2|Theorem §CA.3.2]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-5|Theorem §CA.3.5]]

> [!theorem] Theorem §CA.6.8: Convolution with a Fundamental Solution Solves the Sourced Equation
> If $G$ is a fundamental solution of $P(\partial)$ and $j \in \mathcal D(\mathbb R^n)$, then $\phi(x) \equiv i\,G\bigl[j(x - \cdot)\bigr]$ is smooth and $P(\partial)\phi = j$. In the physicists' notation, $\phi(x) = i\int d^ny\,G(x - y)\,j(y)$.
>
> *Source: the user's PHY 513 notes, Ch. 6 §§6.1–6.2 (eq. (greensolution); the Green's function as the map $j \mapsto \phi$) · standard (Hörmander I, §4.2)*

^thm-ca-6-8

> [!derivation]- Derivation
> **Step 1** (the definition is the familiar integral). For $G = T_g$, $G[j(x - \cdot)] = \int d^ny\,g(y)\,j(x - y)$, and the substitution $y \to x - y$ (Jacobian $1$) turns it into $\int d^ny\,g(x - y)\,j(y)$. For general $G$, $y \mapsto j(x - y)$ is a test function for each $x$, so $G[j(x - \cdot)]$ is defined.
>
> **Step 2** (smoothness). The difference quotient $[j(x + he_k - y) - j(x - y)]/h$ converges to $(\partial_kj)(x - y)$ in $\mathcal D$ as $h \to 0$ (all supports in one bounded set; Taylor's theorem with a remainder uniform in $y$ for every derivative). By continuity of $G$, $\partial_k\,G[j(x - \cdot)] = G[(\partial_kj)(x - \cdot)]$. Repeating, $\phi$ is smooth.
>
> **Step 3** (move the derivative onto $G$). $(\partial_kj)(x - y) = -\partial_{y_k}[j(x - y)]$, so by [[§CA.2 Generalized Functions#^def-ca-2-4|Def. §CA.2.4]]
>
> $$
> G\bigl[(\partial_kj)(x - \cdot)\bigr] = -G\bigl[\partial_{y_k}j(x - \cdot)\bigr] = (\partial_kG)\bigl[j(x - \cdot)\bigr] .
> $$
>
> Applying this to each derivative in $P(\partial)$: $P(\partial)\,G[j(x - \cdot)] = (P(\partial)G)[j(x - \cdot)]$.
>
> **Step 4** (use the equation). $(P(\partial)G)[j(x - \cdot)] = -i\,\delta[j(x - \cdot)] = -i\,j(x - 0) = -i\,j(x)$. Multiplying by $i$: $P(\partial)\phi = j$.
>
> **What the derivation shows.**
> - The Green's function is the linear map $j \mapsto \phi$, and "$G(x - y)$" its kernel ([[§CA.2 Generalized Functions#^rem-ca-2-3|Remark: What the language buys in field theory]]); the $i$ in the solution formula undoes the $-i$ of the normalization.
> - Sources that are test functions, smooth and switched on and off, give smooth fields; this is the hypothesis on $j$ in [[§C2b.5 Green's Functions and Contours#^mod-c2b-5-1|Model §C2b.5.1]] and [[§C2b.8 Particle Production by a Classical Source|§C2b.8]].

^der-ca-6-8

*Uses:* [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^def-ca-6-1|Def. §CA.6.1]], [[§CA.2 Generalized Functions#^def-ca-2-4|Def. §CA.2.4]]

> [!remark]- Connections
> - The imaginary part of Sokhotski–Plemelj is the Lorentzian nascent delta function of [[§B4.4 Fourier Transforms and the Delta Function#^def-b4-4-2|WO Def. §B4.4.2]]; the same Lorentzian is the line shape of a ringing oscillator ([[§B4.4 Fourier Transforms and the Delta Function#^ex-b4-4-1|WO Example §B4.4.1]]), whose width is the $\varepsilon$ that a damped mode carries ([[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-5|Theorem §CA.6.5]]).
> - Sokhotski–Plemelj was used inline before it had a home: the level shift (principal value) and decay rate ($-i\pi\delta$, Fermi's golden rule) of [[§C9.6 The Interaction Picture and the Atom–Field Interaction|QM §C9.6]], and the imaginary part of the resolvent behind the optical theorem in [[§C10.2 The Eikonal Approximation and the Optical Theorem|QM §C10.2]]. In field theory it gives the differences of Green's functions on the mass shell ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-11|Theorem §C2b.6.11]]) and the massless commutator function ([[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-8|Theorem §C2b.4.8]]).
> - Theorem §CA.6.2 applied to a spectrum is Stieltjes inversion: the imaginary part of the resolvent trace at $x + i\varepsilon$ is the eigenvalue density smoothed by a Lorentzian, the tool of the semicircle law ([[§R3.4 The Semicircle Law II꞉ Stieltjes Transform and Coulomb Gas#^thm-r3-4-3|Thesis Thm. §R3.4.3]]); its δ part gives the golden-rule width of a level coupled to many others ([[§R4.2 Nearly Diagonal Matrices꞉ Gershgorin and Perturbation Theory#^thm-r4-2-8|Thesis Thm. §R4.2.8]]).
> - The damping factor of Theorem §CA.6.5 is the impulse response of a damped oscillator seen from the frequency side ([[§B4.4 Fourier Transforms and the Delta Function#^thm-b4-4-6|WO Theorem §B4.4.6]]) and the adiabatic switching $e^{\eta t}$, $\eta \to 0^+$, of time-dependent perturbation theory ([[§C9.6 The Interaction Picture and the Atom–Field Interaction|QM §C9.6]]).
> - Boundary values, the $i\varepsilon$ limits and fundamental solutions are where the three tools before them meet: distributions ([[§CA.2 Generalized Functions|§CA.2]]), Fourier transforms of distributions ([[§CA.3 Fourier Transforms and Fourier Tricks|§CA.3]]) and contour deformation with the half-residue lemma ([[§CA.4 Contour Integration#^thm-ca-4-7|Theorem §CA.4.7]]); the procedure that chains them for every propagator is [[P2 Green's Functions by Contour Integration|P2]].
> - **Used in**, statement by statement (C2a–C2b items):
>   - Caution: What the formula does and does not say ($i\varepsilon$ only matters at zeros): the principal function, dropping $i\varepsilon$ after a Wick rotation — [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-4|Theorem §C2b.5.4]], [[§C2b.7 Wick Rotation and the Two-Point Family#^thm-c2b-7-1|Theorem §C2b.7.1]], [[§C2b.7 Wick Rotation and the Two-Point Family#^thm-c2b-7-4|Theorem §C2b.7.4]], [[§C2b.7 Wick Rotation and the Two-Point Family#^rem-c2b-7-2|§C2b.7, Remark: The two-point functions at a glance]].
>   - Theorem §CA.6.1 (boundary values): $D_W$ from the lower half-plane — [[§C2b.2 The Wightman Function#^thm-c2b-2-3|Theorem §C2b.2.3]], [[§C2b.2 The Wightman Function#^thm-c2b-2-5|Theorem §C2b.2.5]], [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-4|Theorem §C2b.3.4]].
>   - Theorem §CA.6.2 (Sokhotski–Plemelj): [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-8|Theorem §C2b.4.8]], [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-4|Theorem §C2b.5.4]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-10|Theorem §C2b.6.10]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-11|Theorem §C2b.6.11]], [[§C2b.7 Wick Rotation and the Two-Point Family#^thm-c2b-7-5|Theorem §C2b.7.5]].
>   - Theorem §CA.6.3 (logarithms and powers): the light-cone singularity — [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-5|Theorem §C2b.3.5]], [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-6|Theorem §C2b.3.6]].
>   - Theorem §CA.6.4 (light-cone boundary value): massless $D_W$, $D$, $D_1$ — [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-5|Theorem §C2b.3.5]], [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-6|Theorem §C2b.3.6]], [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-8|Theorem §C2b.4.8]], [[§C2b.7 Wick Rotation and the Two-Point Family#^thm-c2b-7-4|Theorem §C2b.7.4]].
>   - Def. §CA.6.1, Theorems §CA.6.7–§CA.6.8 (fundamental solutions): Green's functions, contours as boundary conditions, the sourced field — [[§C2b.5 Green's Functions and Contours#^rem-c2b-5-1|§C2b.5, Remark: What a Green's "function" is]], [[§C2b.1 Heisenberg Fields#^thm-c2b-1-3|Theorem §C2b.1.3]], [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-4|Theorem §C2b.5.4]], [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-6|Theorem §C2b.5.6]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-4|Theorem §C2b.6.4]], [[§C2b.8 Particle Production by a Classical Source#^thm-c2b-8-1|Theorem §C2b.8.1]], [[§C2b.8 Particle Production by a Classical Source#^thm-c2b-8-4|Theorem §C2b.8.4]].
>   - Theorem §CA.6.5 (damping, $\tilde\theta$): the retarded function, the $i\varepsilon$ from switching — [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-3|Theorem §C2b.3.3]].
>   - Theorem §CA.6.6 ($i\varepsilon$ limits): $D_F$ and $D_R$ in momentum space as limits in $\mathcal S'$ — [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-2|Theorem §C2b.6.2]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-9|Theorem §C2b.6.9]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-10|Theorem §C2b.6.10]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-11|Theorem §C2b.6.11]], [[§C2b.7 Wick Rotation and the Two-Point Family#^thm-c2b-7-4|Theorem §C2b.7.4]], [[§C2b.7 Wick Rotation and the Two-Point Family#^thm-c2b-7-5|Theorem §C2b.7.5]], [[P2 Green's Functions by Contour Integration#^p2-3|P2, step 3]].
> - **Used in**, statement by statement (C1a–C1b items):
>   - Theorem §CA.6.1 (boundary values): [[§C1a.5 Vectors, Tensors and Index Notation#^rem-c1a-5-3|§C1a.5, Remark: In what sense 1/x² is harmonic, and where the source sits]].
>   - Theorem §CA.6.4 (light-cone boundary value): [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-8|Theorem §C1a.5.8]], [[§C1a.5 Vectors, Tensors and Index Notation#^rem-c1a-5-3|§C1a.5, Remark: In what sense 1/x² is harmonic, and where the source sits]].
> - **Used in**, statement by statement (C4 items):
>   - Def. §CA.6.1 (Fundamental Solution): [[§C4.2★ The Proca Field#^thm-c4-2-8|Theorem §C4.2.8]], [[§C4.2★ The Proca Field#^thm-c4-2-9|Theorem §C4.2.9]], [[§C4.2★ The Proca Field|§C4.2★]].
>   - Theorem §CA.6.2 (Sokhotski–Plemelj Formula): [[§C4.9 Vector-Field Propagators#^rem-c4-9-2|§C4.9, Remark: The sign of the photon propagator and negative norm]], [[§C4.9 Vector-Field Propagators#^thm-c4-9-7|Theorem §C4.9.7]], [[§C4.9 Vector-Field Propagators|§C4.9]].
>   - Theorem §CA.6.3 (Logarithm and Powers at the Real Axis): [[§C4.9 Vector-Field Propagators#^rem-c4-9-3|§C4.9, Remark: Why the ξ-term is allowed: Faddeev–Popov]], [[§C4.9 Vector-Field Propagators#^thm-c4-9-8|Theorem §C4.9.8]], [[§C4.9 Vector-Field Propagators|§C4.9]].
>   - Theorem §CA.6.4 (The Light-Cone Boundary Value): [[§C4.9 Vector-Field Propagators#^thm-c4-9-5|Theorem §C4.9.5]], [[§C4.9 Vector-Field Propagators|§C4.9]].
>   - Theorem §CA.6.8 (Convolution with a Fundamental Solution Solves the Sourced Equation): [[§C4.2★ The Proca Field#^thm-c4-2-8|Theorem §C4.2.8]], [[§C4.2★ The Proca Field#^thm-c4-2-9|Theorem §C4.2.9]].
>   - Theorem §CA.6.6 (The iε Limits of the Propagator Denominators): [[§C4.9 Vector-Field Propagators#^rem-c4-9-2|§C4.9, Remark: The sign of the photon propagator and negative norm]], [[§C4.9 Vector-Field Propagators#^thm-c4-9-7|Theorem §C4.9.7]], [[§C4.9 Vector-Field Propagators|§C4.9]].
> - **Used in**, statement by statement (C5a–C5b items):
>   - Theorem §CA.6.6 ($i\varepsilon$ limits): $S_F$ as a limit in $\mathcal S'$ — [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-3|Theorem §C5b.8.3]], [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-4|Theorem §C5b.8.4]], [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-5|Theorem §C5b.8.5]].
> - **Used in**, statement by statement (Electromagnetism C items):
>   - Def. §CA.6.1, Theorems §CA.6.7–§CA.6.8 (fundamental solutions): the Coulomb potential, the Green functions of Poisson's equation, the Lorenz-gauge and Proca solutions — [[§C1.3 Gauge Symmetry and Charge Conservation#^ex-c1-3-2|EM ★ Example §C1.3.2]], [[§C1.4 Gauge Fixing and the Two Polarizations#^thm-c1-4-1|EM Theorem §C1.4.1]], [[§C2.1 The Static Limit and the Field of a Charge Distribution#^rem-c2-1-1|EM Remark: The Coulomb potential as a fundamental solution]], [[§C7.3 Green Functions for Poisson’s Equation#^def-c7-3-1|EM Def. §C7.3.1]], [[§C7.3 Green Functions for Poisson’s Equation#^thm-c7-3-1|EM Theorem §C7.3.1]], [[§C7.3 Green Functions for Poisson’s Equation#^thm-c7-3-4|EM Theorem §C7.3.4]].
>   - Theorem §CA.6.5 (damping): the two-tube electron lens by a Fourier integral — [[§C6.3 Separation in Cylindrical and Polar Coordinates#^ex-c6-3-1|EM Example §C6.3.1]].
