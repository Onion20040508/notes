---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C2b
section: C2b.3
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C2b.2 The Wightman Function]] · ↑ [[· C2b Two-Point Functions, Causality and Propagators]] · [[§C2b.4 Microcausality and the Commutator Function]] →

*Sources: the user's PHY 513 notes, Ch. 5 §§5.4, 5.7, App. A §A.3, and the Bessel computations of Ch. 2 §2.2 · PHY 513 Lecture 5 (Larsen, 16 Sep 2026; no slides, reconstructed in the user's notes) · Peskin & Schroeder §2.4, pp. 26–27 · PHY 513, Problem Set 4, Problems 2(a) and 3(a).*

What is the Wightman function of [[§C2b.2 The Wightman Function|§C2b.2]] at a given spacetime point? Its Bessel-function forms are computed here once for the whole subject: one Euclidean evaluation ([[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-1|Theorem §C2b.3.1]]) continued, through the boundary value of [[§C2b.2 The Wightman Function#^thm-c2b-2-5|Theorem §C2b.2.5]], to every spacetime point (Theorems §C2b.3.2–§C2b.3.5). The commutator function of [[§C2b.4 Microcausality and the Commutator Function|§C2b.4]] and the Feynman function of [[§C2b.7 Wick Rotation and the Two-Point Family|§C2b.7]] are read off from these forms, and so is the exact single-particle amplitude of [[§C1a.3 Causal Structure and the Causality of a Single Particle|§C1a.3]], one time derivative of $D_W$ (Theorems §C2b.3.7–§C2b.3.10).

*Conventions* ([[Larsen PHY 513]]): $\hbar = c = 1$, $g = \operatorname{diag}(+, -, -, -)$, $E_{\mathbf p} = \sqrt{\mathbf p^2 + m^2}$, $p\cdot x = E_{\mathbf p}t - \mathbf p\cdot\mathbf x$ whenever $p$ is on shell, $[a_{\mathbf p}, a_{\mathbf q}^\dagger] = (2\pi)^3\delta^3(\mathbf p - \mathbf q)$, $|\mathbf p\rangle = \sqrt{2E_{\mathbf p}}\,a_{\mathbf p}^\dagger|0\rangle$. Lecture 5 writes $\omega_{\mathbf p}$ for $E_{\mathbf p}$ ([[§C2a.1 Canonical Quantization of Fields#^cau-c2a-1-1|Caution: Eₚ, not ωₚ; π, not Π]]). Unless stated otherwise $m > 0$; the massless case is stated separately where it differs.

> [!theorem] Theorem §C2b.3.1: The Wightman Function at Imaginary Time
> For $\tau > 0$, with $p_E = (p_4, \mathbf p)$, $x_E = (\tau, \boldsymbol\xi)$, Euclidean products and $R = \sqrt{\tau^2 + \boldsymbol\xi^2}$,
>
> $$
> W(-i\tau, \boldsymbol\xi) = \int\frac{d^3p}{(2\pi)^3}\,\frac{e^{-E_{\mathbf p}\tau + i\mathbf p\cdot\boldsymbol\xi}}{2E_{\mathbf p}} = \int\frac{d^4p_E}{(2\pi)^4}\,\frac{e^{ip_E\cdot x_E}}{p_E^2 + m^2} = \frac{m}{4\pi^2R}\,K_1(mR) ,
> $$
>
> a function of the four-dimensional Euclidean distance alone; for $m = 0$ it is $1/4\pi^2R^2$. This is the single evaluation of the Bessel-$K$ integral in these notes.
>
> *Source: the user's PHY 513 notes, Ch. 2 §2.2 (Derivation "The relativistic amplitude in closed form", Steps 1–4, where it is the auxiliary function $D_E$), Ch. 5 §5.4*

^thm-c2b-3-1

> [!derivation]- Derivation
> **Step 1** (the first equality). Put $z = -i\tau$ in [[§C2b.2 The Wightman Function#^thm-c2b-2-5|Theorem §C2b.2.5]]: $-iE_{\mathbf p}z = -iE_{\mathbf p}(-i\tau) = -E_{\mathbf p}\tau$.
>
> **Step 2** (a fourth momentum, by residues). For $E > 0$ and $\tau > 0$ consider $g(p_4) = \frac{e^{ip_4\tau}}{(p_4 - iE)(p_4 + iE)}$, poles at $\pm iE$. Since $|e^{ip_4\tau}| = e^{-\tau\operatorname{Im}p_4} \le 1$ for $\operatorname{Im}p_4 \ge 0$, close the real line upward ([[P2 Green's Functions by Contour Integration#^p2-4|P2, step 4]]); on the semicircle of radius $L > E$ (a letter other than the $R$ of the statement), $|g| \le 1/(L^2 - E^2)$, so the arc is at most $\pi L/(L^2 - E^2) \to 0$ as $L \to \infty$ (ML, [[§CA.4 Contour Integration#^thm-ca-4-6|Theorem §CA.4.6]]). The closed contour is counterclockwise and encloses only $p_4 = iE$, with residue $\frac{e^{i(iE)\tau}}{2iE} = \frac{e^{-E\tau}}{2iE}$ ([[§CA.4 Contour Integration#^thm-ca-4-4|Theorem §CA.4.4]]). By the residue theorem ([[§CA.4 Contour Integration#^thm-ca-4-5|Theorem §CA.4.5]]),
>
> $$
> \int_{-\infty}^{\infty}\frac{dp_4}{2\pi}\,\frac{e^{ip_4\tau}}{p_4^2 + E^2} = \frac{1}{2\pi}\cdot2\pi i\cdot\frac{e^{-E\tau}}{2iE} = \frac{e^{-E\tau}}{2E} .
> $$
>
> With $E = E_{\mathbf p}$, $p_4^2 + E_{\mathbf p}^2 = p_4^2 + \mathbf p^2 + m^2 = p_E^2 + m^2$, and inserting this for each $\mathbf p$ gives the second equality, read as the iterated integral ($\mathbf p$ outside). (The four-dimensional integral does not converge absolutely, since $\int d^4p_E/(p_E^2 + m^2) = \infty$; as an identity in $\mathcal S'(\mathbb R^4)$ it is the transform of the bounded function $1/(p_E^2 + m^2)$, which is a tempered distribution with an inverse transform, [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-2|Theorem §CA.3.2]]. That distribution is the function computed here: the result of Step 6, $mK_1(mR)/4\pi^2R$, is smooth for $R > 0$, $\simeq 1/4\pi^2R^2$ as $R \to 0$ and exponentially decaying as $R \to \infty$, hence locally integrable in four dimensions ($\int_{R \le 1}d^4x_E/R^2 = 2\pi^2\int_0^1R\,dR < \infty$) and tempered, [[§CA.2 Generalized Functions#^thm-ca-2-1|Theorem §CA.2.1]], 2; paired with a test function $f$, the iterated integral equals $\int d^4x_E\,f\,W$ by Fubini at each fixed $x_E \ne 0$ and dominated convergence.)
>
> ⚑ By-product: the four-dimensional form is the Euclidean propagator $D_E$, whose home is [[§C2b.7 Wick Rotation and the Two-Point Family#^def-c2b-7-1|Def. §C2b.7.1]]; it is manifestly invariant under rotations of $(\tau, \boldsymbol\xi)$, so the result depends on $R$ only.
>
> **Step 3** (Schwinger parametrization for each $\mathbf p$). $\frac{1}{p_4^2 + E^2} = \int_0^\infty ds\,e^{-s(p_4^2 + E^2)}$ ([[§CA.5 Gaussian Integrals, Stationary Phase and Bessel Functions#^thm-ca-5-1|Theorem §CA.5.1]], 2). The $s$ and $p_4$ integrals may be exchanged: the modulus of the integrand has $\int ds\int dp_4\,e^{-s(p_4^2 + E^2)} = \int_0^\infty ds\,\sqrt{\pi/s}\,e^{-sE^2} < \infty$ ([[Tonelli's Theorem|551 Tonelli's theorem]], then Fubini). The $p_4$ integral is a one-dimensional Gaussian (Theorem §CA.5.1, 1 with $n = 1$):
>
> $$
> \frac{e^{-E\tau}}{2E} = \int_0^\infty ds\;e^{-sE^2}\int\frac{dp_4}{2\pi}\,e^{-sp_4^2 + ip_4\tau} = \int_0^\infty ds\;\frac{e^{-\tau^2/4s}}{(4\pi s)^{1/2}}\,e^{-sE^2} .
> $$
>
> **Step 4** (exchange with the $\mathbf p$ integral). Insert into the first form with $E^2 = \mathbf p^2 + m^2$. The modulus of the double integrand integrates to $\int_0^\infty ds\,(4\pi s)^{-1/2}e^{-\tau^2/4s}e^{-sm^2}(\pi/s)^{3/2}/(2\pi)^3$, finite because $e^{-\tau^2/4s}$ kills the small-$s$ region; so the order may be exchanged, and the $\mathbf p$ integral is a three-dimensional Gaussian (Theorem §CA.5.1, 1 with $n = 3$, $\mathbf x = \boldsymbol\xi$):
>
> $$
> W(-i\tau, \boldsymbol\xi) = \int_0^\infty ds\;\frac{e^{-\tau^2/4s}}{(4\pi s)^{1/2}}\,e^{-sm^2}\,\frac{e^{-\boldsymbol\xi^2/4s}}{(4\pi s)^{3/2}} = \frac{1}{16\pi^2}\int_0^\infty\frac{ds}{s^2}\,\exp\Bigl(-sm^2 - \frac{R^2}{4s}\Bigr).
> $$
>
> ⚑ By-product: $\tau > 0$ is what makes every exchange legitimate; at $\tau = 0$ the small-$s$ region diverges, the same divergence as Step 6 of Theorem §C2b.2.1. (Doing the Schwinger step on the four-dimensional integral at once, as the user's notes do, exchanges integrals that are not jointly absolutely convergent near $s = 0$; doing $p_4$ first, as here, avoids this.)
>
> **Step 5** (change of variables, $m > 0$). Substitute $s = \frac{R}{2m}e^u$, $u \in (-\infty, \infty)$ as $s \in (0, \infty)$. Then $sm^2 = \frac{mR}{2}e^u$, $\frac{R^2}{4s} = \frac{mR}{2}e^{-u}$, so the exponent is $-\frac{mR}{2}(e^u + e^{-u}) = -mR\cosh u$; and $ds = s\,du$, so $\frac{ds}{s^2} = \frac{du}{s} = \frac{2m}{R}e^{-u}\,du$:
>
> $$
> W = \frac{1}{16\pi^2}\cdot\frac{2m}{R}\int_{-\infty}^{\infty}du\;e^{-u}\,e^{-mR\cosh u} .
> $$
>
> **Step 6** (recognize $K_1$). $e^{-u} = \cosh u - \sinh u$. The $\sinh u$ term is odd and absolutely integrable, so it integrates to zero; the $\cosh u$ term is even, and $\int_{-\infty}^{\infty}\cosh u\,e^{-mR\cosh u}\,du = 2K_1(mR)$ ([[§CA.5 Gaussian Integrals, Stationary Phase and Bessel Functions#^def-ca-5-1|Def. §CA.5.1]]). So $W = \frac{m}{8\pi^2R}\cdot2K_1(mR) = \frac{m}{4\pi^2R}K_1(mR)$.
>
> **Step 7** ($m = 0$). Step 5 needs $m > 0$. For $m = 0$, Step 4 gives $\frac{1}{16\pi^2}\int_0^\infty\frac{ds}{s^2}e^{-R^2/4s}$; with $v = 1/s$, $dv = -ds/s^2$, this is $\frac{1}{16\pi^2}\int_0^\infty dv\,e^{-R^2v/4} = \frac{1}{16\pi^2}\cdot\frac{4}{R^2} = \frac{1}{4\pi^2R^2}$, which is also the $m \to 0$ limit of Step 6 since $K_1(z) \simeq 1/z$ ([[§CA.5 Gaussian Integrals, Stationary Phase and Bessel Functions#^thm-ca-5-3|Theorem §CA.5.3]], 3).
>
> ⚑ By-product: the $m > 0$ form and the $m = 0$ form are related by the small-argument limit of $K_1$; the massless function reappears as the light-cone singularity of the massive one → [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-5|Theorem §C2b.3.5]].
>
> **What the derivation shows.**
> - Three tools in sequence: a residue (a fourth momentum), a Gaussian (after Schwinger's parametrization), and a change of variables to the integral representation of $K_1$.
> - Four-dimensional Euclidean rotation invariance: Lorentz invariance continued to imaginary time.
> - Used next: the continuation to every $\xi$ (Theorem §C2b.3.2); the Euclidean propagator (§C2b.7, Def. §C2b.7.1); [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-7|Theorem §C2b.3.7]] obtains the single-particle amplitude as $-2\partial_\tau$ of this function.

^der-c2b-3-1

*Uses:* [[§C2b.2 The Wightman Function#^thm-c2b-2-5|Theorem §C2b.2.5]], [[§CA.4 Contour Integration#^thm-ca-4-4|Theorem §CA.4.4]], [[§CA.4 Contour Integration#^thm-ca-4-5|Theorem §CA.4.5]], [[§CA.4 Contour Integration#^thm-ca-4-6|Theorem §CA.4.6]], [[§CA.5 Gaussian Integrals, Stationary Phase and Bessel Functions#^thm-ca-5-1|Theorem §CA.5.1]], [[§CA.5 Gaussian Integrals, Stationary Phase and Bessel Functions#^def-ca-5-1|Def. §CA.5.1]], [[§CA.5 Gaussian Integrals, Stationary Phase and Bessel Functions#^thm-ca-5-3|Theorem §CA.5.3]], [[Tonelli's Theorem|551 Tonelli's theorem]]

> [!theorem] Theorem §C2b.3.2: The Wightman Function in the Lower Half-Plane
> For $\operatorname{Im}z < 0$,
>
> $$
> W(z, \boldsymbol\xi) = \frac{m\,K_1(ms)}{4\pi^2s}, \qquad s = \sqrt{\boldsymbol\xi^2 - z^2}\quad\text{(principal branch, }\operatorname{Re}s > 0\text{)},
> $$
>
> and $W = 1/4\pi^2s^2$ for $m = 0$. Every value of $D_W$ is a boundary value of this one function.
>
> *Source: the user's PHY 513 notes, Ch. 5 §5.4 (Derivation "$D_W$ everywhere, by analytic continuation", the Claim)*

^thm-c2b-3-2

> [!derivation]- Derivation
> **Step 1** (where $s^2$ goes). Write $z = a - ib$, $b > 0$. Then $\boldsymbol\xi^2 - z^2 = \boldsymbol\xi^2 - a^2 + b^2 + 2iab$. Its imaginary part $2ab$ vanishes only for $a = 0$, and there the value is $\boldsymbol\xi^2 + b^2 > 0$. So for $\operatorname{Im}z < 0$, $\boldsymbol\xi^2 - z^2$ never lies on $(-\infty, 0]$.
>
> **Step 2** (the branch). The principal square root is analytic on $\mathbb C \setminus (-\infty, 0]$ with positive real part. By Step 1, $s(z)$ is analytic on the lower half-plane, $\operatorname{Re}s > 0$, and $s \ne 0$.
>
> ⚑ By-product: the principal branch is forced by agreement with Step 4 ($s = R > 0$ on the Euclidean ray); the other branch would give $-R$.
>
> **Step 3** (the right side is analytic). $K_1$ is analytic on $\operatorname{Re}w > 0$ ([[§CA.5 Gaussian Integrals, Stationary Phase and Bessel Functions#^def-ca-5-1|Def. §CA.5.1]]); composed with $ms(z)$ and divided by $s \ne 0$ it is analytic on the lower half-plane.
>
> **Step 4** (agreement on a ray). On $z = -i\tau$, $\tau > 0$: $s = \sqrt{\boldsymbol\xi^2 + \tau^2} = R$, and the two sides agree by [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-1|Theorem §C2b.3.1]].
>
> **Step 5** (identity theorem). $W$ is analytic on the lower half-plane ([[§C2b.2 The Wightman Function#^thm-c2b-2-5|Theorem §C2b.2.5]]), which is connected, and the ray has accumulation points in it. By [[§CA.4 Contour Integration#^thm-ca-4-3|Theorem §CA.4.3]] the two functions agree everywhere there. For $m = 0$ the same argument with $1/4\pi^2s^2$.
>
> **What the derivation shows.**
> - No new integral is done: one Euclidean evaluation plus analyticity gives the function everywhere.
> - The only singularities of $W$ as a function of $s^2 = \boldsymbol\xi^2 - z^2$ are the $1/s^2$ pole at $s^2 = 0$, the light cone (Theorem §C2b.3.5), and the cut of $\sqrt{s^2}$ and $K_1$ along the negative axis, the timelike region.
> - Used next: the three boundary values (Theorems §C2b.3.3–§C2b.3.5) and the Feynman function in position space ([[§C2b.7 Wick Rotation and the Two-Point Family#^thm-c2b-7-3|Theorem §C2b.7.3]]).

^der-c2b-3-2

*Uses:* [[§C2b.2 The Wightman Function#^thm-c2b-2-5|Theorem §C2b.2.5]], [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-1|Theorem §C2b.3.1]], [[§CA.4 Contour Integration#^thm-ca-4-3|Theorem §CA.4.3]], [[§CA.5 Gaussian Integrals, Stationary Phase and Bessel Functions#^def-ca-5-1|Def. §CA.5.1]]

> [!theorem] Theorem §C2b.3.3: The Wightman Function at Spacelike Separation
> For $\xi^2 = -r^2 < 0$,
>
> $$
> D_W(\xi) = \frac{m}{4\pi^2r}\,K_1(mr), \qquad r = \sqrt{-\xi^2},
> $$
>
> a smooth, real, positive function; $\simeq 1/4\pi^2r^2$ for $mr \ll 1$, and for $mr \gg 1$
>
> $$
> D_W(\xi) \simeq \frac{\sqrt m}{2(2\pi r)^{3/2}}\,e^{-mr}\Bigl(1 + \frac{3}{8mr} + \cdots\Bigr) .
> $$
>
> *Source: the user's PHY 513 notes, Ch. 5 §5.4 · PS §2.4, eq. (2.52) · PHY 513, Problem Set 4, Problem 3(a)*

^thm-c2b-3-3

> [!derivation]- Derivation
> **Step 1** (the limit). Put $z = t - i\varepsilon$, $t = \xi^0$, in [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-2|Theorem §C2b.3.2]]: $s^2 = \boldsymbol\xi^2 - (t - i\varepsilon)^2 = \boldsymbol\xi^2 - t^2 + 2i\varepsilon t + \varepsilon^2 \to \boldsymbol\xi^2 - t^2 = r^2 > 0$.
>
> **Step 2** (smoothness). $r^2$ is a positive real number, away from the cut of $\sqrt{\ }$ and of $K_1$; the right side of Theorem §C2b.3.2 is continuous there, so the limit exists pointwise, locally uniformly in the spacelike region, and therefore also as a generalized function there: integrated against a test function supported in that open region it converges by uniform convergence, so the distribution $D_W$ of Theorem §C2b.2.5, restricted to the region ([[§CA.2 Generalized Functions#^def-ca-2-3|Def. §CA.2.3]]), is this function ([[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-6|Theorem §C2b.3.6]], 1). With $s \to r$: $D_W = mK_1(mr)/4\pi^2r$.
>
> **Step 3** (real and positive). $K_1(x) = \int_0^\infty e^{-x\cosh u}\cosh u\,du > 0$ for $x > 0$.
>
> ⚑ By-product: $D_W$ is *real* at spacelike separation; since $[\phi(x), \phi(y)] = 2i\operatorname{Im}D_W$, this is microcausality → [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-5|Theorem §C2b.4.5]], second route.
>
> **Step 4** (short distance). $K_1(x) = 1/x + O(x\ln x)$ ([[§CA.5 Gaussian Integrals, Stationary Phase and Bessel Functions#^thm-ca-5-3|Theorem §CA.5.3]], 3), so $D_W \simeq \frac{m}{4\pi^2r}\cdot\frac{1}{mr} = \frac{1}{4\pi^2r^2}$, the massless function.
>
> **Step 5** (long distance). $K_1(x) = \sqrt{\pi/2x}\,e^{-x}\bigl(1 + \frac{3}{8x} + \cdots\bigr)$ (Theorem §CA.5.3, 2 with $\nu = 1$: $(4\nu^2 - 1)/8 = 3/8$). Then
>
> $$
> \frac{m}{4\pi^2r}\sqrt{\frac{\pi}{2mr}} = \frac{\sqrt m\,\sqrt\pi}{4\sqrt2\,\pi^2\,r^{3/2}} = \frac{\sqrt m}{4\sqrt2\,\pi^{3/2}r^{3/2}} = \frac{\sqrt m}{2(2\pi)^{3/2}r^{3/2}},
> $$
>
> using $2(2\pi)^{3/2} = 4\sqrt2\,\pi^{3/2}$.
>
> ⚑ By-product: the decay length is the Compton wavelength $1/m$ ([[§B4.1 The Klein–Gordon Equation#^def-b4-1-2|REL Def. §B4.1.2]]), and the Hadamard function $D_1 = 2D_W$ is the same function → [[§C2b.4 Microcausality and the Commutator Function#^rem-c2b-4-3|Remark: Influence and correlation]].
>
> **What the derivation shows.**
> - Outside the light cone the boundary value is an ordinary smooth function; the $i\varepsilon$ is needed only to define it on and inside the cone.
> - The leak outside the cone is exponentially small but nonzero; it is a correlation, not an influence (Theorem §C2b.4.5).
> - Two further routes below compute the equal-time value directly, without analytic continuation.

^der-c2b-3-3

*Uses:* [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-2|Theorem §C2b.3.2]], [[§CA.5 Gaussian Integrals, Stationary Phase and Bessel Functions#^thm-ca-5-3|Theorem §CA.5.3]]

> [!derivation]- Derivation (second route: the contour around the branch cut, at equal times)
> This is the lecture's and PS's computation (PS eq. (2.52), Fig. 2.3), with the three points that need care made explicit. By Theorem §C2b.2.3 it suffices to take $\xi^0 = 0$, $|\boldsymbol\xi| = r$.
>
> **Step 1** (equal times). At $\xi^0 = 0$, $e^{-ip\cdot\xi} = e^{+i\mathbf p\cdot\boldsymbol\xi}$, and with the convergence factor of [[§C2b.2 The Wightman Function#^thm-c2b-2-5|Theorem §C2b.2.5]], Step 5, understood (sense: $\boldsymbol\xi \ne 0$ at $\xi^0 = 0$ is a spacelike point, where $D_W$ is a smooth function, [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-6|Theorem §C2b.3.6]], 1; its value there is the pointwise limit $\varepsilon \to 0^+$ of $W(-i\varepsilon, \boldsymbol\xi)$, and every step below is done at $\varepsilon > 0$, where the integral converges absolutely, before the limit),
>
> $$
> D_W(r) = \int\frac{d^3p}{(2\pi)^3\,2E_{\mathbf p}}\,e^{i\mathbf p\cdot\boldsymbol\xi} .
> $$
>
> **Step 2** (angular integral). Choose the polar axis of $\mathbf p$ along $\boldsymbol\xi$ (a rotation of the integration variable, Jacobian 1: [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|Theorem §CA.3.7]], 4; the frame choice of [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-9|Theorem §CA.3.9]], 3), so $\mathbf p\cdot\boldsymbol\xi = pr\cos\theta$ with $p = |\mathbf p|$, and $d^3p = p^2\sin\theta\,dp\,d\theta\,d\varphi$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-8|Theorem §CA.3.8]]). The $\varphi$ integral gives $2\pi$. Substitute $u = \cos\theta$, $du = -\sin\theta\,d\theta$; $\theta: 0 \to \pi$ becomes $u: 1 \to -1$, and the minus sign of $du$ flips the limits back: $\int_0^\pi\sin\theta\,e^{ipr\cos\theta}d\theta = \int_{-1}^1e^{ipru}du = \frac{2\sin pr}{pr}$. So
>
> $$
> D_W(r) = \frac{2\pi}{(2\pi)^3}\int_0^\infty\frac{p^2\,dp}{2E_{\mathbf p}}\,\frac{2\sin pr}{pr} = \frac{1}{4\pi^2r}\int_0^\infty dp\,\frac{p\sin pr}{\sqrt{p^2 + m^2}} .
> $$
>
> **Step 3** (fold onto the whole line). The integrand $p\sin(pr)/\sqrt{p^2 + m^2}$ is even in $p$, so $\int_0^\infty = \frac12\int_{-\infty}^\infty$. Write $\sin pr = (e^{ipr} - e^{-ipr})/2i$ and substitute $p \to -p$ in the $e^{-ipr}$ term (Jacobian $1$, limits swap back, $p \to -p$ in the prefactor; [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|Theorem §CA.3.7]], 1, applied to the damped integrand before $\varepsilon \to 0$): $-\int p\,e^{-ipr}/E\,dp = +\int p\,e^{ipr}/E\,dp$. The two terms are equal, and
>
> $$
> D_W(r) = \frac{1}{4\pi^2r}\cdot\frac12\cdot\frac{2}{2i}\int_{-\infty}^\infty dp\,\frac{p\,e^{ipr}}{\sqrt{p^2 + m^2}} = -\frac{i}{8\pi^2r}\int_{-\infty}^{\infty}dp\,\frac{p\,e^{ipr}}{\sqrt{p^2 + m^2}} .
> $$
>
> **Step 4** (why the contour cannot be closed yet). $p/\sqrt{p^2 + m^2} \to 1$, so Jordan's lemma does not apply ([[§CA.4 Contour Integration#^cau-ca-4-1|§CA.4, Caution: Jordan's lemma needs g → 0]]), and the regulator cannot be kept on the arc. The fix: $p\,e^{ipr} = -i\partial_re^{ipr}$, so
>
> $$
> D_W(r) = -\frac{i}{8\pi^2r}\cdot(-i)\frac{d}{dr}I(r) = -\frac{1}{8\pi^2r}\,I'(r), \qquad I(r) \equiv \int_{-\infty}^{\infty}\frac{e^{ipr}\,dp}{\sqrt{p^2 + m^2}},
> $$
>
> where $I$ converges for $r > 0$ (Dirichlet's test, [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-2|Theorem §CA.1.2]]); moving $d/dr$ outside is justified as in Step 4 of the third route below.
>
> **Step 5** (the branch). Write $\sqrt{p^2 + m^2} = \sqrt{p - im}\,\sqrt{p + im}$ with $\arg(p - im) \in (-\tfrac{3\pi}{2}, \tfrac\pi2)$ and $\arg(p + im) \in (-\tfrac\pi2, \tfrac{3\pi}{2})$: the cuts run up from $im$ and down from $-im$, and on the real axis the two arguments are negatives of each other, so the root is positive there. Just right of the upper cut, $p = i\rho + 0^+$ with $\rho > m$: both arguments tend to $\frac\pi2$, so $\sqrt{p^2 + m^2} \to \sqrt{\rho - m}\,e^{i\pi/4}\sqrt{\rho + m}\,e^{i\pi/4} = +i\sqrt{\rho^2 - m^2}$. Just left, $\arg(p - im) \to -\frac{3\pi}{2}$ (a point left of the upward ray has argument just above $\frac\pi2$, which lies outside the chosen range and is represented as $-\frac{3\pi}2$), so the root tends to $e^{-3\pi i/4}e^{i\pi/4}\sqrt{\rho^2 - m^2} = -i\sqrt{\rho^2 - m^2}$.
>
> ⚑ By-product: the cut is a choice; any cut from $im$ to $i\infty$ in the upper half-plane gives the same $I(r)$, but the values on the lips depend on it.
>
> **Step 6** (the keyhole). Integrate $e^{ipr}/\sqrt{p^2 + m^2}$ counterclockwise around: $[-L, L]$; the arc from $L$ to $iL$; down the right lip from $iL$ to $im$; around the circle $|p - im| = \delta$; up the left lip to $iL$; the arc from $iL$ to $-L$ ([[§CA.4 Contour Integration#^thm-ca-4-8|Theorem §CA.4.8]] and its figure). The integrand is analytic inside, so the total is $0$ (Cauchy). The arcs vanish by Jordan's lemma, since $|1/\sqrt{p^2 + m^2}| \le (L^2 - m^2)^{-1/2} \to 0$ and $r > 0$. On the small circle the integrand is $O(\delta^{-1/2})$ and the length is $2\pi\delta$: $O(\delta^{1/2}) \to 0$. On the lips $p = i\rho$, $dp = i\,d\rho$, $e^{ipr} = e^{-\rho r}$:
>
> $$
> \text{right lip: } \int_{L}^{m}\frac{i\,d\rho\,e^{-\rho r}}{+i\sqrt{\rho^2 - m^2}} = -\int_m^L\frac{e^{-\rho r}d\rho}{\sqrt{\rho^2 - m^2}}, \qquad \text{left lip: } \int_m^{L}\frac{i\,d\rho\,e^{-\rho r}}{-i\sqrt{\rho^2 - m^2}} = -\int_m^L\frac{e^{-\rho r}d\rho}{\sqrt{\rho^2 - m^2}} .
> $$
>
> They *add*. Letting $L \to \infty$, $\delta \to 0$: $I(r) - 2\int_m^\infty\frac{e^{-\rho r}d\rho}{\sqrt{\rho^2 - m^2}} = 0$.
>
> **Step 7** (the Bessel function). Substitute $\rho = m\cosh u$: $d\rho = m\sinh u\,du$ and $\sqrt{\rho^2 - m^2} = m\sinh u$, so $\frac{d\rho}{\sqrt{\rho^2 - m^2}} = du$, with $u: 0 \to \infty$. Hence $I(r) = 2\int_0^\infty e^{-mr\cosh u}du = 2K_0(mr)$ ([[§CA.5 Gaussian Integrals, Stationary Phase and Bessel Functions#^thm-ca-5-4|Theorem §CA.5.4]], 1).
>
> **Step 8** (differentiate). $I'(r) = 2mK_0'(mr) = -2mK_1(mr)$ (Theorem §CA.5.3, 1), so $D_W(r) = -\frac{1}{8\pi^2r}(-2mK_1(mr)) = \frac{m}{4\pi^2r}K_1(mr)$. Before the derivative, $-\frac{1}{8\pi^2r}I'(r) = \frac{1}{4\pi^2r}\int_m^\infty\frac{\rho\,e^{-\rho r}d\rho}{\sqrt{\rho^2 - m^2}}$ is PS eq. (2.52), whose value $mK_1(mr)$ PS leave unevaluated (Theorem §CA.5.4, 1).
>
> **What the derivation shows.**
> - The lecture's shortcut, rotating $p \to i\rho$ on the half-line, is this computation compressed: on $0 < \rho < m$ the integrand is analytic and that stretch cancels against its conjugate, and only the cut survives with the two lips adding. What the shortcut takes for granted, a vanishing quarter arc for the non-decaying kernel $p/\sqrt{p^2 + m^2}$, is what the derivative of Step 4 secures.
> - The result is manifestly real (an integral of a positive function): microcausality again.
> - The same contour with the phase $pr - t\sqrt{p^2 + m^2}$ gives the general spacelike point and its saddle ([[§CA.5 Gaussian Integrals, Stationary Phase and Bessel Functions#^ex-ca-5-1|Example §CA.5.1]]).
>
> *Source: the user's PHY 513 notes, Ch. 5 §5.4 (Derivation "Equal time, directly: the lecture's contour done carefully"), App. A §A.3 (applied to the Wightman function) · PS §2.4, eq. (2.52), Fig. 2.3*

*Uses:* [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-8|Theorem §CA.3.8]], [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-2|Theorem §CA.1.2]], [[§CA.4 Contour Integration#^thm-ca-4-6|Theorem §CA.4.6]], [[§CA.4 Contour Integration#^thm-ca-4-8|Theorem §CA.4.8]], [[§CA.5 Gaussian Integrals, Stationary Phase and Bessel Functions#^thm-ca-5-3|Theorem §CA.5.3]], [[§CA.5 Gaussian Integrals, Stationary Phase and Bessel Functions#^thm-ca-5-4|Theorem §CA.5.4]]

> [!derivation]- Derivation (third route: real variables only)
> No contours: a substitution, a table integral, and the interchange theorems of [[§CA.1 Exchanging Limits, Derivatives and Integrals|§CA.1]].
>
> **Step 1** (regulate). From Step 2 of the second route, $D_W(r) = \frac{1}{4\pi^2r}\int_0^\infty dp\,\frac{p\sin pr}{\sqrt{p^2 + m^2}} = -\frac{i}{2(2\pi)^2r}\int_0^\infty dp\,\frac{p}{\sqrt{p^2 + m^2}}(e^{ipr} - e^{-ipr})$, which does not converge. Damp both exponentials by $e^{-\varepsilon p}$ (the problem set's $r \to r \pm i\varepsilon$; a damping factor in the sense of [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-5|Theorem §CA.6.5]], removed by a pointwise limit at fixed $r > 0$ in Steps 3–4, which is legitimate because $D_W$ is a smooth function at spacelike points, [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-6|Theorem §C2b.3.6]], 1):
>
> $$
> \Delta_\varepsilon(r) \equiv \int_0^\infty dp\,\frac{p\,e^{-\varepsilon p}}{\sqrt{p^2 + m^2}}\bigl(e^{ipr} - e^{-ipr}\bigr), \qquad D_W(r) = -\frac{i}{2(2\pi)^2r}\lim_{\varepsilon\to0^+}\Delta_\varepsilon(r),
> $$
>
> absolutely convergent for $\varepsilon > 0$ since the integrand is bounded by $2e^{-\varepsilon p}$.
>
> **Step 2** (substitute). $p = m\sinh v$: $dp = m\cosh v\,dv$ and $\sqrt{p^2 + m^2} = m\cosh v$, so $\frac{p\,dp}{\sqrt{p^2 + m^2}} = m\sinh v\,dv$, and $e^{ipr} - e^{-ipr} = 2i\sin(mr\sinh v)$:
>
> $$
> \Delta_\varepsilon = \int_0^\infty dv\,e^{-m\varepsilon\sinh v}\,m\sinh v\;2i\sin(mr\sinh v) = -2i\,\partial_rF_\varepsilon(r), \qquad F_\varepsilon(r) \equiv \int_0^\infty dv\,e^{-m\varepsilon\sinh v}\cos(mr\sinh v),
> $$
>
> using $m\sinh v\,\sin(mr\sinh v) = -\partial_r\cos(mr\sinh v)$. Taking $\partial_r$ outside is [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|Theorem §CA.1.1]], 2: the $r$-derivative of the integrand is bounded, uniformly in $r$, by $m\sinh v\,e^{-m\varepsilon\sinh v}$, which is integrable.
>
> **Step 3** (limit of $F_\varepsilon$). Undo the substitution: $F_\varepsilon(r) = \int_0^\infty\frac{\cos pr}{\sqrt{p^2 + m^2}}e^{-\varepsilon p}dp$. The unregulated integral converges by Dirichlet's test and equals $K_0(mr)$ ([[§CA.5 Gaussian Integrals, Stationary Phase and Bessel Functions#^thm-ca-5-4|Theorem §CA.5.4]], 2); by Abel's theorem ([[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-2|Theorem §CA.1.2]], 2) $F_\varepsilon(r) \to K_0(mr)$. The pointwise limit $e^{-m\varepsilon\sinh v} \to 1$ alone would not justify this: the integral converges only conditionally.
>
> **Step 4** (limit of $F_\varepsilon'$, the step that needs care). Convergence of $F_\varepsilon$ says nothing about $F_\varepsilon'$. Write $\frac{p}{\sqrt{p^2 + m^2}} = 1 - g(p)$ with
>
> $$
> g(p) = \frac{m^2}{\sqrt{p^2 + m^2}\bigl(\sqrt{p^2 + m^2} + p\bigr)}, \qquad 0 \le g(p) \le \min\Bigl(1, \frac{m^2}{2p^2}\Bigr),
> $$
>
> integrable on $[0, \infty)$. With $\int_0^\infty\sin(pr)e^{-\varepsilon p}dp = \frac{r}{r^2 + \varepsilon^2}$,
>
> $$
> F_\varepsilon'(r) = -\int_0^\infty dp\,\frac{p\sin pr}{\sqrt{p^2 + m^2}}e^{-\varepsilon p} = -\frac{r}{r^2 + \varepsilon^2} + \int_0^\infty dp\,g(p)\sin(pr)\,e^{-\varepsilon p} .
> $$
>
> On $[r_0, \infty)$, $r_0 > 0$, the first term differs from $-1/r$ by at most $\varepsilon^2/r_0^3$; the second differs from its $\varepsilon = 0$ value by at most $\int_0^\infty g(p)(1 - e^{-\varepsilon p})dp$, which tends to $0$ by dominated convergence (dominated by $g$) and does not depend on $r$. So $F_\varepsilon'$ converges uniformly on $[r_0, \infty)$, and by [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-3|Theorem §CA.1.3]] its limit is $\partial_rK_0(mr) = -mK_1(mr)$.
>
> **Step 5** (assemble). $\lim\Delta_\varepsilon = -2i(-mK_1(mr)) = 2imK_1(mr)$, and $D_W(r) = -\frac{i}{2(2\pi)^2r}\cdot2imK_1(mr) = \frac{m}{4\pi^2r}K_1(mr)$.
>
> **What the derivation shows.**
> - Every exchange of a limit with an integral or a derivative is licensed by a named theorem; the one that needs uniform convergence is the derivative (Step 4).
> - The regulator $e^{-\varepsilon p}$ differs from the covariant $e^{-\varepsilon E_{\mathbf p}}$ of Theorem §C2b.2.5; at spacelike separation both limits are the same smooth function, so the choice does not matter there.
> - Three independent routes (analytic continuation, contour, real variables) give one answer.
>
> *Source: the user's PHY 513 notes, Ch. 5 §5.4 (Derivation "A third route: real variables only") · PHY 513, Problem Set 4, Problem 3(a)*

*Uses:* [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|Theorem §CA.1.1]], [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-2|Theorem §CA.1.2]], [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-3|Theorem §CA.1.3]], [[§CA.5 Gaussian Integrals, Stationary Phase and Bessel Functions#^thm-ca-5-4|Theorem §CA.5.4]]

> [!theorem] Theorem §C2b.3.4: The Wightman Function at Timelike Separation
> For $\xi^2 = \tau^2 > 0$,
>
> $$
> D_W(\xi) = \frac{m}{8\pi\tau}\Bigl[Y_1(m\tau) + i\operatorname{sgn}(\xi^0)\,J_1(m\tau)\Bigr], \qquad \tau = \sqrt{\xi^2},
> $$
>
> complex, with complex-conjugate values on the future and past sheets. At $\boldsymbol\xi = 0$ and $mt \gg 1$,
>
> $$
> D_W \simeq \frac{\sqrt m}{4\pi^2}\sqrt{\frac\pi2}\;e^{-3\pi i/4}\;t^{-3/2}\,e^{-imt} .
> $$
>
> *Source: the user's PHY 513 notes, Ch. 5 §5.4 (timelike case), §5.7 (Derivation "Explicit forms") · PS §2.4, eq. (2.51)*

^thm-c2b-3-4

> [!derivation]- Derivation
> **Step 1** (the limit of $s$). With $z = t - i\varepsilon$, $s^2 = \boldsymbol\xi^2 - t^2 + 2i\varepsilon t + \varepsilon^2 \to -\tau^2 + i0\cdot\operatorname{sgn}(t)$: for $t > 0$ the point approaches the negative real axis from above, for $t < 0$ from below. The principal root of $-\tau^2 + i0$ is $+i\tau$, of $-\tau^2 - i0$ it is $-i\tau$. So $s \to i\operatorname{sgn}(t)\,\tau$. The limit is pointwise and locally uniform in the open timelike region, so, as in Step 2 of Derivation §C2b.3.3, it is the restriction of the distribution $D_W$ there ([[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-6|Theorem §C2b.3.6]], 1).
>
> **Step 2** ($t > 0$). $D_W = \frac{mK_1(im\tau)}{4\pi^2\cdot i\tau}$. The continuation formula $K_1(ix) = -\frac\pi2\bigl[J_1(x) - iY_1(x)\bigr]$ for $x > 0$ ([[§CA.5 Gaussian Integrals, Stationary Phase and Bessel Functions#^thm-ca-5-4|Theorem §CA.5.4]], 3), with $x = m\tau$, gives
>
> $$
> D_W = \frac{m}{4\pi^2i\tau}\cdot\Bigl(-\frac\pi2\Bigr)\bigl[J_1 - iY_1\bigr] = \frac{m}{8\pi\tau}\cdot\frac{-1}{i}\bigl[J_1 - iY_1\bigr] = \frac{m}{8\pi\tau}\cdot i\bigl[J_1 - iY_1\bigr] = \frac{m}{8\pi\tau}\bigl[Y_1 + iJ_1\bigr],
> $$
>
> using $-1/i = i$.
>
> **Step 3** ($t < 0$). $D_W(\xi) = \overline{D_W(-\xi)}$ ([[§C2b.2 The Wightman Function#^thm-c2b-2-4|Theorem §C2b.2.4]], 2), and $-\xi$ has positive time component: $D_W = \frac{m}{8\pi\tau}[Y_1 - iJ_1]$. Together, the factor $\operatorname{sgn}(\xi^0)$ on $J_1$.
>
> ⚑ By-product: the values on the two sheets are complex conjugates, not equal, so $D_W(\xi) - D_W(-\xi) \ne 0$ inside the cone: the commutator does not vanish there → [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-5|Theorem §C2b.4.5]]; and $\operatorname{Re}D_W = \frac12D_1$, $\operatorname{Im}D_W = \frac12D$ → [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-9|Theorem §C2b.4.9]].
>
> **Step 4** (late times at $\boldsymbol\xi = 0$). Here $\tau = t$. With $J_1(x) \simeq \sqrt{2/\pi x}\cos(x - \frac{3\pi}4)$ and $Y_1(x) \simeq \sqrt{2/\pi x}\sin(x - \frac{3\pi}4)$ (Theorem §CA.5.4, 4), and $\theta = mt - \frac{3\pi}{4}$: $Y_1 + iJ_1 \simeq \sqrt{\frac{2}{\pi mt}}(\sin\theta + i\cos\theta) = i\sqrt{\frac{2}{\pi mt}}\,e^{-i\theta}$. Hence
>
> $$
> D_W \simeq \frac{m}{8\pi t}\cdot i\sqrt{\frac{2}{\pi mt}}\,e^{-imt}e^{3\pi i/4} = \frac{\sqrt2\,\sqrt m}{8\pi^{3/2}}\,t^{-3/2}\,e^{i(\pi/2 + 3\pi/4)}e^{-imt},
> $$
>
> and $e^{5\pi i/4} = e^{-3\pi i/4}$, $\frac{\sqrt2}{8\pi^{3/2}} = \frac{1}{4\pi^2}\sqrt{\frac\pi2}$.
>
> **Step 5** (the energy form, as PS write it). At $\boldsymbol\xi = 0$ the angular integral is $4\pi p^2dp$, and $p\,dp = E\,dE$: $D_W(t, \mathbf 0) = \frac{4\pi}{(2\pi)^3}\int_0^\infty\frac{p^2dp}{2E}e^{-iE(t - i\varepsilon)} = \frac{1}{4\pi^2}\int_m^\infty dE\,\sqrt{E^2 - m^2}\,e^{-iE(t - i\varepsilon)}$; without the $\varepsilon$ the integrand grows like $E$. As a function of $t$ this is the boundary value from $\operatorname{Im}t < 0$ of the transform of the polynomially bounded function $\theta(E - m)\sqrt{E^2 - m^2}$, a tempered distribution in $t$ ([[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-1|Theorem §CA.6.1]], 1; [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-2|Theorem §CA.3.2]]); at $t \ne 0$ it is the function of Step 4.
>
> **What the derivation shows.**
> - Inside the cone $K_1$ of imaginary argument becomes a Hankel function: oscillation instead of decay.
> - At late times only the lowest energy $E = m$ survives dephasing (PS's $e^{-imt}$), with the $t^{-3/2}$ of a spreading packet; continuing $r \to it$ in Theorem §C2b.3.3 gives the same prefactor.
> - Used next: the commutator and Hadamard functions inside the cone (Theorem §C2b.4.9).

^der-c2b-3-4

*Uses:* [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-2|Theorem §C2b.3.2]], [[§C2b.2 The Wightman Function#^thm-c2b-2-4|Theorem §C2b.2.4]], [[§CA.5 Gaussian Integrals, Stationary Phase and Bessel Functions#^thm-ca-5-4|Theorem §CA.5.4]]

> [!theorem] Theorem §C2b.3.5: The Wightman Function near the Light Cone
> As $\xi^2 \to 0$,
>
> $$
> D_W(\xi) = -\frac{1}{4\pi^2\bigl[(\xi^0 - i\varepsilon)^2 - \boldsymbol\xi^2\bigr]} + \frac{m^2}{8\pi^2}\ln\frac{ms}{2} + \cdots, \qquad s = \sqrt{\boldsymbol\xi^2 - (\xi^0 - i\varepsilon)^2} :
> $$
>
> the leading term is the massless Wightman function, exact for $m = 0$, and is a generalized function singular on the whole cone; the logarithm is locally integrable (the distributional statement is [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-6|Theorem §C2b.3.6]]).
>
> *Source: the user's PHY 513 notes, Ch. 5 §5.4 (light-cone case), §5.7 (the expansion of $K_1$) · PHY 513, Problem Set 4, Problem 2(a)*

^thm-c2b-3-5

> [!derivation]- Derivation
> **Step 1** (expand $K_1$). $K_1(w) = \frac1w + \frac w2\ln\frac w2 + O(w)$ for $w \to 0$ ([[§CA.5 Gaussian Integrals, Stationary Phase and Bessel Functions#^thm-ca-5-3|Theorem §CA.5.3]], 3). With $w = ms$ in [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-2|Theorem §C2b.3.2]]:
>
> $$
> \frac{m}{4\pi^2s}K_1(ms) = \frac{m}{4\pi^2s}\Bigl[\frac{1}{ms} + \frac{ms}{2}\ln\frac{ms}{2} + O(ms)\Bigr] = \frac{1}{4\pi^2s^2} + \frac{m^2}{8\pi^2}\ln\frac{ms}{2} + O(m^2) .
> $$
>
> **Step 2** (the leading term). $s^2 = \boldsymbol\xi^2 - z^2$ with $z = \xi^0 - i\varepsilon$, so $\frac{1}{4\pi^2s^2} = -\frac{1}{4\pi^2(z^2 - \boldsymbol\xi^2)}$. For $m = 0$ this is exact (Theorem §C2b.3.2).
>
> **Step 3** (which terms are singular). $1/s^2$ blows up on the whole cone $\xi^2 = 0$; as $\varepsilon \to 0$ it is defined only as a generalized function, the boundary value of Theorem §C2b.2.5; explicitly, $1/s^2 = 1/\bigl(-(\xi^0 - i\varepsilon)^2 + \boldsymbol\xi^2\bigr)$ is the $F_\varepsilon$ of [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-4|Theorem §CA.6.4]], whose limit is $1/(-\xi^2 + i0\,\xi^0)$ ([[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-6|Theorem §C2b.3.6]], 3). $\ln s$ diverges only logarithmically, which is locally integrable, and changes by $i\pi\operatorname{sgn}(\xi^0)/2$ across the cone, a finite jump ($\ln s = \frac12\log s^2$ with $s^2 \to -\xi^2 + i0\,\xi^0$, and $\log(x \pm i0) = \ln|x| \pm i\pi\theta(-x)$, [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-3|Theorem §CA.6.3]], 1).
>
> ⚑ By-product: the jump of $\frac{m^2}{8\pi^2}\ln s$ gives $\operatorname{Im}D_W = \frac{m^2}{16\pi}$ just inside the future cone, so the commutator function jumps by a finite amount there → [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-9|Theorem §C2b.4.9]]; and the $1/\xi^2$ singularity at coincident points is the divergence of the zero-point energy → [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-8|Theorem §C2b.6.8]].
>
> **What the derivation shows.**
> - Every massive two-point function has the massless one as its light-cone singularity: the short-distance behaviour does not know about $m$.
> - The definition by boundary values is indispensable exactly here.
> - Used next: the massless commutator and Hadamard functions by Sokhotski–Plemelj (Theorem §C2b.4.8).

^der-c2b-3-5

*Uses:* [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-2|Theorem §C2b.3.2]], [[§C2b.2 The Wightman Function#^thm-c2b-2-5|Theorem §C2b.2.5]], [[§CA.5 Gaussian Integrals, Stationary Phase and Bessel Functions#^thm-ca-5-3|Theorem §CA.5.3]]

![[ph-qft-c2-5-1.svg]]
*The Wightman function in units $m = 1$. Left: outside the light cone (equal times) it is real and positive, $1/4\pi^2r^2$ at short distance and $e^{-mr}$ beyond the Compton wavelength (Theorem §C2b.3.3); the two-term asymptotic form (with the $3/8mr$ correction) is within 2 % by $mr = 2$, the leading term alone within 14 %. Right: inside, at $\boldsymbol\xi = 0$, it oscillates as $e^{-imt}$ inside a $t^{-3/2}$ envelope (Theorem §C2b.3.4); its imaginary part is $\tfrac12D$ and its real part $\tfrac12D_1$. Adapted from the user's PHY 513 notes, Fig. 5.1.*

> [!remark] Remark: What the two regimes say
> Outside the cone $D_W$ is damped on the Compton scale $1/m$ but not zero; the prefactor $r^{-3/2}$ is the spreading of a wave in three dimensions, and continuing $r \to it$ turns $r^{-3/2}e^{-mr}$ into the timelike $e^{-3\pi i/4}t^{-3/2}e^{-imt}$. Inside, at late times only the lowest energy $E = m$ survives dephasing (PS eq. (2.51)). The exponent $e^{-m\sqrt{-\xi^2}}$ at a general spacelike point also follows from steepest descent ([[§CA.5 Gaussian Integrals, Stationary Phase and Bessel Functions#^ex-ca-5-1|Example §CA.5.1]]), and the three regimes are three boundary values of one analytic function of $s^2 = -\xi^2$ (Theorem §C2b.3.2): positive real outside, negative real inside, zero on the cone.
>
> *Source: the user's PHY 513 notes, Ch. 5 §5.4 · PS §2.4, eq. (2.51)*

^rem-c2b-3-1

> [!theorem] Theorem §C2b.3.6: The Wightman Function as a Distribution: Off the Cone and on It
> 1. On the open set $\xi^2 \ne 0$ the distribution $D_W$ ([[§C2b.2 The Wightman Function#^thm-c2b-2-2|Theorem §C2b.2.2]]) is the real-analytic function of Theorems §C2b.3.3–§C2b.3.4: $D_W[f] = \int d^4\xi\,f(\xi)\,D_W(\xi)$ for every test function $f$ supported off the light cone.
> 2. $\operatorname{sing\,supp}D_W$ is the whole light cone $\xi^2 = 0$, tip included ([[§CA.2 Generalized Functions#^def-ca-2-3|Def. §CA.2.3]]).
> 3. On all of $\mathbb R^4$, $D_W = \dfrac{1}{4\pi^2}\,\dfrac{1}{-\xi^2 + i0\,\xi^0} + L = -\dfrac{1}{4\pi^2}\,\mathcal P\frac{1}{\xi^2} - \dfrac{i}{4\pi}\operatorname{sgn}(\xi^0)\,\delta(\xi^2) + L$, with the light-cone boundary value of [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-4|Theorem §CA.6.4]] and $L$ a locally integrable function ($L = 0$ for $m = 0$) with a logarithmic singularity and a finite jump on the cone. The $-i0\,\xi^0$ is the boundary value from $\operatorname{Im}\xi^0 < 0$ written covariantly.
>
> *Source: the user's PHY 513 notes, Ch. 5 §5.4 (light-cone case, "defined only as a generalized function"), §5.7 · stated here as distributions (standard: Gel'fand & Shilov 1, Ch. III; Streater & Wightman, Ch. 2)*

^thm-c2b-3-6

> [!derivation]- Derivation
> **Step 1** (off the cone). Let $f \in \mathcal D$ be supported in $\{\xi^2 \ne 0\}$; its support is compact, so it keeps a positive distance from the cone. On it, $W(\xi^0 - i\varepsilon, \boldsymbol\xi)$ converges uniformly to the functions of [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-3|Theorem §C2b.3.3]] and [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-4|Theorem §C2b.3.4]] (Step 2 and Step 1 of their derivations: $s^2$ stays in a compact set away from $0$, approached from one side of the cut). So $\int f\,W(\cdot - i\varepsilon) \to \int f\,D_W(\xi)\,d^4\xi$, while by [[§C2b.2 The Wightman Function#^thm-c2b-2-5|Theorem §C2b.2.5]] the same integrals tend to $D_W[f]$. Part 1.
>
> **Step 2** (smooth there). Off the cone the functions are $mK_1(mr)/4\pi^2r$ with $r = \sqrt{-\xi^2} > 0$ and $\frac{m}{8\pi\tau}[Y_1 + i\operatorname{sgn}(\xi^0)J_1](m\tau)$ with $\tau = \sqrt{\xi^2} > 0$, analytic functions of $\xi$ (Bessel functions of arguments bounded away from $0$; $\operatorname{sgn}\xi^0$ is constant on each sheet). So $\operatorname{sing\,supp}D_W \subseteq \{\xi^2 = 0\}$.
>
> **Step 3** (split off the light-cone term). By [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-2|Theorem §C2b.3.2]], $W(\xi^0 - i\varepsilon, \boldsymbol\xi) = \mathcal W(s_\varepsilon^2)$ with $\mathcal W(w) = mK_1(m\sqrt w)/4\pi^2\sqrt w$ and $s_\varepsilon^2 = -(\xi^0 - i\varepsilon)^2 + \boldsymbol\xi^2 = -\xi^2 + 2i\varepsilon\xi^0 + \varepsilon^2$. Write $\mathcal W(w) = \frac{1}{4\pi^2w} + \ell(w)$. The first term at $w = s_\varepsilon^2$ is $\frac{1}{4\pi^2}F_\varepsilon$ with the $F_\varepsilon$ of [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-4|Theorem §CA.6.4]], which converges in $\mathcal S'(\mathbb R^4)$ to $\frac{1}{4\pi^2}\frac{1}{-\xi^2 + i0\,\xi^0}$ (part 1 there).
>
> **Step 4** (the remainder is mild). From $zK_1(z) = 1 + \frac{z^2}{2}\ln\frac z2\,A(z^2) + z^2B(z^2)$ with $A$, $B$ entire and $A(0) = 1$ (the series behind [[§CA.5 Gaussian Integrals, Stationary Phase and Bessel Functions#^thm-ca-5-3|Theorem §CA.5.3]], 3), $\ell(w) = \frac{m^2}{8\pi^2}\ln\frac{m\sqrt w}{2}\,A(m^2w) + \frac{m^2}{4\pi^2}B(m^2w)$, so $|\ell(w)| \le C_R(1 + |\ln|w||)$ for $|w| \le R$. Now $|s_\varepsilon^2| \ge |\xi^2|$: for $\xi^2 \le 0$ the real part $-\xi^2 + \varepsilon^2$ already exceeds $|\xi^2|$; for $\xi^2 = a > 0$, $(\xi^0)^2 \ge a$ gives $|s_\varepsilon^2|^2 = (\varepsilon^2 - a)^2 + 4\varepsilon^2(\xi^0)^2 \ge (\varepsilon^2 + a)^2$. Hence on every compact set $|\ell(s_\varepsilon^2)| \le C(1 + |\ln|\xi^2||)$, independent of $\varepsilon \le 1$, and $\ln|\xi^2|$ is locally integrable on $\mathbb R^4$ (the cone has codimension one; near $\xi = 0$, $|\xi^2|$ vanishes only quadratically). By dominated convergence ([[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|Theorem §CA.1.1]]) $\ell(s_\varepsilon^2) \to L \equiv \ell(-\xi^2 + i0\,\xi^0)$ in $L^1_{\mathrm{loc}}$, hence as distributions; since $W$ and the first term converge in $\mathcal S'$, so does $\ell(s_\varepsilon^2)$, with the same limit $L$. For $m = 0$, $\ell \equiv 0$ (Theorem §C2b.3.2).
>
> **Step 5** (the jump of $L$). Inside the future cone $\ln\sqrt{w} = \frac12\log(-\tau^2 + i0) = \ln\tau + \frac{i\pi}{2}$, outside it is real ([[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-3|Theorem §CA.6.3]], 1): a finite jump of $\frac{m^2}{8\pi^2}\cdot\frac{i\pi}{2}$ times $A(0) = 1$, the jump of Step 3 of Derivation §C2b.3.5.
>
> **Step 6** (the cone term written out). [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-4|Theorem §CA.6.4]], 2: $\frac{1}{-\xi^2 + i0\,\xi^0} = -\mathcal P\frac{1}{\xi^2} - i\pi\operatorname{sgn}(\xi^0)\,\delta(\xi^2)$. Dividing by $4\pi^2$ gives part 3.
>
> **Step 7** (the cone is singular). Near a point $\xi_0 \ne 0$ of the cone, $\operatorname{Im}D_W = -\frac{1}{4\pi}\operatorname{sgn}(\xi^0)\delta(\xi^2) + \operatorname{Im}L$, since $\mathcal P\frac{1}{\xi^2}$ is real. $\delta(\xi^2)$ is a surface measure on the cone ([[§CA.2 Generalized Functions#^thm-ca-2-7|Theorem §CA.2.7]], 2): test functions concentrating on a patch of the cone keep $\delta(\xi^2)[\varphi_n]$ fixed while $\int\varphi_n\,g \to 0$ for every locally integrable $g$. So $\operatorname{Im}D_W$ is not a locally integrable function near $\xi_0$, let alone smooth: $\xi_0 \in \operatorname{sing\,supp}D_W$. The singular support is closed, so it contains the tip. With Step 2, part 2.
>
> ⚑ By-product: the coefficient of $\delta(\xi^2)$ is $-\frac{i}{4\pi}\operatorname{sgn}(\xi^0)$, fixed by the sign of $i0\,\xi^0$; twice its imaginary part is the light-cone term $-\frac{1}{2\pi}\operatorname{sgn}(\xi^0)\delta(\xi^2)$ of the commutator function → [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-8|Theorem §C2b.4.8]], [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-9|Theorem §C2b.4.9]].
>
> **What the derivation shows.**
> - The Bessel forms are honest values of $D_W$ wherever it has values, off the cone; on the cone it has none, and the boundary value of Theorem §C2b.2.5 fixes exactly how it acts there: a principal value, a $\delta(\xi^2)$ with a definite sign, and an integrable logarithm.
> - The light-cone structure is mass independent; $m$ enters only the locally integrable remainder.
> - Used next: the support of $D$ and $D_1$ ([[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-4|Theorem §C2b.4.4]]), the product $\theta(\xi^0)D$ ([[§C2b.5 Green's Functions and Contours#^thm-c2b-5-6|Theorem §C2b.5.6]]), the coincident singularity removed by normal ordering ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-7|Theorem §C2b.6.7]]).

^der-c2b-3-6

*Uses:* [[§C2b.2 The Wightman Function#^thm-c2b-2-2|Theorem §C2b.2.2]], [[§C2b.2 The Wightman Function#^thm-c2b-2-5|Theorem §C2b.2.5]], [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-2|Theorem §C2b.3.2]], [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-3|Theorem §C2b.3.3]], [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-4|Theorem §C2b.3.4]], [[§CA.2 Generalized Functions#^def-ca-2-3|Def. §CA.2.3]], [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-4|Theorem §CA.6.4]], [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-3|Theorem §CA.6.3]], [[§CA.5 Gaussian Integrals, Stationary Phase and Bessel Functions#^thm-ca-5-3|Theorem §CA.5.3]], [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|Theorem §CA.1.1]], [[§CA.2 Generalized Functions#^thm-ca-2-7|Theorem §CA.2.7]]

## The single-particle amplitude, revisited

The amplitude $U$ of one relativistic particle ([[§C1a.3 Causal Structure and the Causality of a Single Particle#^def-c1a-3-1|Def. §C1a.3.1]]) is the same mode integral as $D_W$ with the weight $1/2E_{\mathbf p}$ replaced by $1$. [[§C1a.3 Causal Structure and the Causality of a Single Particle|§C1a.3]] showed with the lecture's saddle point that it leaks outside the light cone; with the Wightman function in hand, its exact values everywhere follow by one time derivative of the closed forms above.

> [!theorem] Theorem §C2b.3.7: The Single-Particle Amplitude Is a Time Derivative of the Wightman Function
> With $U(z, \mathbf x)$ the analytic single-particle amplitude of [[§C1a.3 Causal Structure and the Causality of a Single Particle#^thm-c1a-3-4|Theorem §C1a.3.4]] and $W$ the analytic Wightman function of [[§C2b.2 The Wightman Function#^thm-c2b-2-5|Theorem §C2b.2.5]], for $\operatorname{Im}z < 0$,
>
> $$
> U(z, \mathbf x) = 2i\,\partial_zW(z, \mathbf x), \qquad U = 2i\,\partial_tD_W \quad\text{in } \mathcal S'(\mathbb R^4).
> $$
>
> *Source: derived here, from the user's PHY 513 notes, Ch. 2 §2.2 (Step 2 of Derivation "The relativistic amplitude in closed form": $U_E = -2\partial_\tau D_E$) and Ch. 5 §5.4*

^thm-c2b-3-7

> [!derivation]- Derivation
> **Step 1** (relation to $W$). $W(z, \mathbf x) = \int\frac{d^3p}{(2\pi)^3\,2E_{\mathbf p}}e^{-iE_{\mathbf p}z + i\mathbf p\cdot\mathbf x}$. Differentiating under the integral (allowed by Step 2 of Derivation §C2b.2.5): $\partial_z\frac{e^{-iE_{\mathbf p}z}}{2E_{\mathbf p}} = \frac{-iE_{\mathbf p}}{2E_{\mathbf p}}e^{-iE_{\mathbf p}z} = -\frac i2e^{-iE_{\mathbf p}z}$. So $\partial_zW = -\frac i2U$, i.e. $U = 2i\,\partial_zW$.
>
> **Step 2** (on $\mathbb R^4$). $U = \lim U(t - i\varepsilon, \mathbf x)$ in $\mathcal S'(\mathbb R^4)$ ([[§C1a.3 Causal Structure and the Causality of a Single Particle#^thm-c1a-3-4|Theorem §C1a.3.4]]). By [[§C2b.2 The Wightman Function#^thm-c2b-2-5|Theorem §C2b.2.5]], $D_W = \lim W(t - i\varepsilon, \mathbf x)$ in $\mathcal S'(\mathbb R^4)$, and the distributional derivative is continuous under such limits ([[§CA.2 Generalized Functions#^thm-ca-2-5|Theorem §CA.2.5]]): $\partial_tD_W = \lim\,(\partial_zW)(t - i\varepsilon, \cdot) = -\frac i2\lim U(t - i\varepsilon, \cdot) = -\frac i2U$.
>
> **What the derivation shows.**
> - $U$ and $D_W$ are the same mode integral with weights $1$ and $1/2E_{\mathbf p}$: the difference is the relativistic normalization of the states ([[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-1|Def. §C2a.4.1]]).
> - Every explicit form of $U$ is a time derivative of one above; no new Bessel integral is needed. (The user's notes reach the same point through $U_E = -2\partial_\tau D_E$ at imaginary time, which is Step 1 at $z = -i\tau$.)
> - Used next: the closed forms (Theorems §C2b.3.8–§C2b.3.10) and the forward–backward decomposition ([[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-7|Theorem §C2b.4.7]]).

^der-c2b-3-7

*Uses:* [[§C1a.3 Causal Structure and the Causality of a Single Particle#^thm-c1a-3-4|Theorem §C1a.3.4]], [[§C2b.2 The Wightman Function#^thm-c2b-2-5|Theorem §C2b.2.5]], [[§CA.2 Generalized Functions#^thm-ca-2-5|Theorem §CA.2.5]]

> [!theorem] Theorem §C2b.3.8: The Relativistic Amplitude at Spacelike Separation
> For $r > |t|$, with $\rho = \sqrt{r^2 - t^2} = \sqrt{-x^2}$,
>
> $$
> U(t, \mathbf x) = \frac{i\,m^2\,t}{2\pi^2\rho^2}\,K_2(m\rho),
> $$
>
> a smooth function there, purely imaginary and odd in $t$, depending on the point only through the invariant $\rho$ and the factor $t$. Equivalently (cut representation, absolutely convergent), $U = \frac{i}{2\pi^2r}\int_m^\infty d\varrho\,\varrho\,e^{-\varrho r}\sinh\bigl(t\sqrt{\varrho^2 - m^2}\bigr)$. For $m\rho \ll 1$, $U \simeq it/\pi^2\rho^4$; for $m = 0$ the formula $U = it/\pi^2(r^2 - t^2)^2$ is exact at every point off the light cone.
>
> *Source: the user's PHY 513 notes, Ch. 2 §2.2 (Derivations "The relativistic amplitude in closed form" and "The same result directly from the radial integral"; checks (i)–(ii)) · PHY 513 Lecture 2, Part A ("The exact radial integral: a Bessel function")*

^thm-c2b-3-8

> [!derivation]- Derivation
> **Step 1** ($W$ in the lower half-plane). By [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-2|Theorem §C2b.3.2]], for $\operatorname{Im}z < 0$, $W(z, \mathbf x) = \frac{m}{4\pi^2}\,G(s)$ with $G(s) = \frac{K_1(ms)}{s}$ and $s = \sqrt{r^2 - z^2}$ (principal branch, $\operatorname{Re}s > 0$), an analytic function of $z$.
>
> **Step 2** (two derivatives). $\partial_zs = \frac{-2z}{2s} = -\frac zs$. With $w = ms$, $G = m\,w^{-1}K_1(w)$, and $\frac{d}{dw}\bigl[w^{-1}K_1(w)\bigr] = -w^{-1}K_2(w)$ ([[§CA.5 Gaussian Integrals, Stationary Phase and Bessel Functions#^thm-ca-5-3|Theorem §CA.5.3]], 1 with $\nu = 1$), so $\frac{dG}{ds} = m\cdot m\cdot\bigl(-w^{-1}K_2(w)\bigr) = -\frac{mK_2(ms)}{s}$.
>
> **Step 3** (the amplitude in the lower half-plane). By the chain rule and [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-7|Theorem §C2b.3.7]],
>
> $$
> \partial_zW = \frac{m}{4\pi^2}\cdot\Bigl(-\frac{mK_2(ms)}{s}\Bigr)\cdot\Bigl(-\frac zs\Bigr) = \frac{m^2z\,K_2(ms)}{4\pi^2s^2}, \qquad U(z, \mathbf x) = 2i\,\partial_zW = \frac{i\,m^2z\,K_2(ms)}{2\pi^2s^2} .
> $$
>
> ⚑ By-product: this one analytic function of $z$ gives $U$ at every real point as a boundary value; the timelike values are [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-10|Theorem §C2b.3.10]].
>
> **Step 4** (the spacelike limit). Put $z = t - i\varepsilon$: $s^2 = r^2 - t^2 + 2i\varepsilon t + \varepsilon^2 \to \rho^2 > 0$, away from the cut of $\sqrt{\ }$ and of $K_2$ (as in Steps 1–2 of [[§C2b.3 Explicit Forms of the Wightman Function#^der-c2b-3-3|Derivation §C2b.3.3]]). The right side of Step 3 is continuous there, so the limit is locally uniform on the open set $\{r > |t|\}$; integrated against a test function supported in that set it converges to the integral of the limit, so the distribution $U$ is this function there ([[§CA.2 Generalized Functions#^def-ca-2-3|Def. §CA.2.3]]; the same argument as [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-6|Theorem §C2b.3.6]], 1). With $s \to \rho$, $z \to t$: the formula of the theorem.
>
> **Step 5** (imaginary and odd). $K_2(x) = \int_0^\infty e^{-x\cosh u}\cosh2u\,du > 0$ for $x > 0$ ([[§CA.5 Gaussian Integrals, Stationary Phase and Bessel Functions#^def-ca-5-1|Def. §CA.5.1]]), and $\rho$ is even in $t$; so $U/i$ is real with the sign of $t$.
>
> **Step 6** (short distance). $K_2(w) \simeq \frac12\Gamma(2)(2/w)^2 = 2/w^2$ for $w \to 0$ ([[§CA.5 Gaussian Integrals, Stationary Phase and Bessel Functions#^thm-ca-5-3|Theorem §CA.5.3]], 3), so $U \simeq \frac{im^2t}{2\pi^2\rho^2}\cdot\frac{2}{m^2\rho^2} = \frac{it}{\pi^2\rho^4}$.
>
> **Step 7** ($m = 0$). Theorem §C2b.3.2 gives $W = \frac{1}{4\pi^2(r^2 - z^2)}$, so $\partial_zW = \frac{2z}{4\pi^2(r^2 - z^2)^2}$ and $U = 2i\,\partial_zW = \frac{iz}{\pi^2(r^2 - z^2)^2}$. The boundary value at $z = t - i\varepsilon$ is $\frac{it}{\pi^2(r^2 - t^2)^2}$ at every point with $r \neq |t|$, inside the cone as well, since only $(r^2 - z^2)^2$ appears.
>
> ⚑ By-product: for $m = 0$ the leak outside the cone is a power law with no length scale at all; for $m > 0$ it is cut off at $\rho \sim 1/m$ → [[§C1a.3 Causal Structure and the Causality of a Single Particle#^thm-c1a-3-6|Theorem §C1a.3.6]].
>
> **What the derivation shows.**
> - Relativistic kinematics did not cure the leak: $K_2 > 0$, so $U \ne 0$ at every spacelike point with $t \neq 0$.
> - No Bessel integral was evaluated here; the $K_1$ of Theorem §C2b.3.1 and one differentiation suffice.
> - A second, independent route below finds the same function without analytic continuation.

^der-c2b-3-8

*Uses:* [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-2|Theorem §C2b.3.2]], [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-7|Theorem §C2b.3.7]], [[§CA.5 Gaussian Integrals, Stationary Phase and Bessel Functions#^thm-ca-5-3|Theorem §CA.5.3]], [[§CA.5 Gaussian Integrals, Stationary Phase and Bessel Functions#^def-ca-5-1|Def. §CA.5.1]], [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-6|Theorem §C2b.3.6]], [[§CA.2 Generalized Functions#^def-ca-2-3|Def. §CA.2.3]]

> [!derivation]- Derivation (second route: around the branch cut, in real variables)
> This is the user's head-on computation of the lecture's integral; it shows where the spacelike condition enters. Take $r > |t|$ and keep $z = t - i\varepsilon$, $\varepsilon > 0$, until Step 5.
>
> **Step 1** (start). By [[§C1a.3 Causal Structure and the Causality of a Single Particle#^thm-c1a-3-5|Theorem §C1a.3.5]], $U(z, r) = \frac{1}{4\pi^2ir}\int_{-\infty}^\infty dp\;p\,e^{i(pr - zE_p)}$, absolutely convergent.
>
> **Step 2** (the branch). As a function of complex $p$, $E_p = \sqrt{p^2 + m^2}$ has branch points at $\pm im$; take the cuts along the imaginary axis from $im$ to $i\infty$ and from $-im$ to $-i\infty$, with the branch positive on the real axis. On the upper half-plane minus its cut $E_p$ is analytic, $E_p = p + O(1/p)$ for $\operatorname{Re}p > 0$ and $E_p = -p + O(1/p)$ for $\operatorname{Re}p < 0$ as $|p| \to \infty$. On the lips, $p = i\varrho \pm 0$ with $\varrho > m$: $E_p = +is$ just right of the cut and $-is$ just left, $s = \sqrt{\varrho^2 - m^2} > 0$ ([[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-3|Theorem §C2b.3.3]], second route, Step 5).
>
> **Step 3** (the arc vanishes exactly outside the cone). On $p = Le^{i\theta}$, $0 \le \theta \le \pi/2$: $i(pr - zE_p) = ip(r - t + i\varepsilon) + O(1/L)$, of real part $-L\bigl[(r - t)\sin\theta + \varepsilon\cos\theta\bigr] + O(1/L)$. For $\pi/2 \le \theta \le \pi$: $i(pr - zE_p) = ip(r + t - i\varepsilon) + O(1/L)$, of real part $-L\bigl[(r + t)\sin\theta + \varepsilon|\cos\theta|\bigr] + O(1/L)$. If $r > |t|$ both brackets are at least $c = \min(r - |t|, \varepsilon) > 0$ (since $\sin\theta + |\cos\theta| \ge 1$), so on the arc $|p\,e^{i(pr - zE_p)}| \le C\,L\,e^{-cL}$, and the arc integral is at most $\pi L\cdot CLe^{-cL} \to 0$ (ML, [[§CA.4 Contour Integration#^thm-ca-4-6|Theorem §CA.4.6]]). If $r < |t|$, one bracket is negative near $\theta = \pi/2$ and the arc grows: the contour cannot be closed.
>
> ⚑ By-product: the damping $\varepsilon > 0$ is needed on the arc near $\theta = 0$ and $\pi$, where $\sin\theta \to 0$; the factor $p$, which does not tend to zero, rules out Jordan's lemma without it ([[§CA.4 Contour Integration#^cau-ca-4-1|§CA.4, Caution: Jordan's lemma needs g → 0]]). The spacelike condition $r > |t|$ is exactly the condition for the arc to vanish.
>
> **Step 4** (the keyhole). Integrate counterclockwise around $[-L, L]$, the arc to $iL$, down the right lip to $im$, around a small circle at $im$, up the left lip to $iL$, and the arc to $-L$ ([[§CA.4 Contour Integration#^thm-ca-4-8|Theorem §CA.4.8]]; the contour of the figure in [[§CA.4 Contour Integration|§CA.4]]). The integrand is analytic inside, so the total is $0$ ([[§CA.4 Contour Integration#^thm-ca-4-2|Theorem §CA.4.2]]). The small circle contributes $O(\delta)$ (bounded integrand, length $2\pi\delta$), the arcs $\to 0$ by Step 3. On the lips $p = i\varrho$, $dp = i\,d\varrho$, $p = i\varrho$:
>
> $$
> \text{right lip } (E_p = is):\ i(pr - zE_p) = -\varrho r + zs, \qquad \int_L^m i\,d\varrho\,(i\varrho)\,e^{-\varrho r + zs} = \int_m^L\varrho\,e^{-\varrho r + zs}\,d\varrho ;
> $$
>
> $$
> \text{left lip } (E_p = -is):\ i(pr - zE_p) = -\varrho r - zs, \qquad \int_m^L i\,d\varrho\,(i\varrho)\,e^{-\varrho r - zs} = -\int_m^L\varrho\,e^{-\varrho r - zs}\,d\varrho .
> $$
>
> So, as $L \to \infty$, $\delta \to 0$: $\int_{-\infty}^\infty dp\,p\,e^{i(pr - zE_p)} = -\int_m^\infty\varrho\,e^{-\varrho r}\bigl(e^{zs} - e^{-zs}\bigr)d\varrho = -2\int_m^\infty\varrho\,e^{-\varrho r}\sinh(zs)\,d\varrho$.
>
> **Step 5** (remove $\varepsilon$). $|\sinh((t - i\varepsilon)s)| \le \cosh(ts) \le e^{|t|s} \le e^{|t|\varrho}$, so the integrand is dominated by $\varrho\,e^{-(r - |t|)\varrho}$, integrable and independent of $\varepsilon$ (and locally uniformly in $(t, r)$ on $r > |t|$). By dominated convergence ([[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|Theorem §CA.1.1]]), with $\frac{-2}{4\pi^2ir} = \frac{i}{2\pi^2r}$,
>
> $$
> U(t, \mathbf x) = \frac{i}{2\pi^2r}\int_m^\infty d\varrho\;\varrho\,e^{-\varrho r}\sinh\bigl(t\sqrt{\varrho^2 - m^2}\bigr) \qquad (r > |t|).
> $$
>
> ⚑ By-product: this is the cut representation stated in [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-8|Theorem §C2b.3.8]]; in it $U$ is manifestly imaginary, odd in $t$, zero at $t = 0$ for $r > 0$ (as $U(0, \cdot) = \delta^3$ requires) and absolutely convergent; its exponent $-\varrho r + t\sqrt{\varrho^2 - m^2}$ is real, and its maximum is the saddle point → [[§C1a.3 Causal Structure and the Causality of a Single Particle#^thm-c1a-3-6|Theorem §C1a.3.6]], second route.
>
> **Step 6** (hyperbolic variables). Substitute $\varrho = m\cosh w$, $w \in (0, \infty)$: $s = m\sinh w$, $d\varrho = m\sinh w\,dw$, so $\varrho\,d\varrho = m^2\cosh w\sinh w\,dw = \frac{m^2}{2}\sinh2w\,dw$. Encode the point by $r = \rho\cosh\chi$, $t = \rho\sinh\chi$, $\tanh\chi = t/r$, possible because $r > |t|$. Then $\varrho r \mp ts = m\rho(\cosh w\cosh\chi \mp \sinh w\sinh\chi) = m\rho\cosh(w \mp \chi)$, and with $\sinh(ts) = \frac12(e^{ts} - e^{-ts})$,
>
> $$
> \int_m^\infty\varrho\,e^{-\varrho r}\sinh(ts)\,d\varrho = \frac{m^2}{4}\int_0^\infty dw\,\sinh2w\Bigl[e^{-m\rho\cosh(w - \chi)} - e^{-m\rho\cosh(w + \chi)}\Bigr].
> $$
>
> **Step 7** (one integral over the line). In the first term put $v = w - \chi$: $v \in (-\chi, \infty)$, $\sinh2w = \sinh(2v + 2\chi)$. In the second put $v = -(w + \chi)$, so $w = -v - \chi$, $dw = -dv$, $w: 0 \to \infty$ becomes $v: -\chi \to -\infty$, $\cosh(w + \chi) = \cosh v$, $\sinh2w = -\sinh(2v + 2\chi)$; the second term becomes $-\int_{-\chi}^{-\infty}(-\sinh(2v + 2\chi))e^{-m\rho\cosh v}(-dv) = +\int_{-\infty}^{-\chi}\sinh(2v + 2\chi)\,e^{-m\rho\cosh v}dv$. The two pieces join:
>
> $$
> \frac{m^2}{4}\int_{-\infty}^\infty dv\,\sinh(2v + 2\chi)\,e^{-m\rho\cosh v} .
> $$
>
> **Step 8** (the Bessel function). $\sinh(2v + 2\chi) = \sinh2v\cosh2\chi + \cosh2v\sinh2\chi$. The first term is odd in $v$ and absolutely integrable: it gives $0$. The second gives $\sinh2\chi\int_{-\infty}^\infty\cosh2v\,e^{-m\rho\cosh v}dv = 2\sinh2\chi\,K_2(m\rho)$ ([[§CA.5 Gaussian Integrals, Stationary Phase and Bessel Functions#^def-ca-5-1|Def. §CA.5.1]], $\nu = 2$). With $\sinh2\chi = 2\sinh\chi\cosh\chi = 2tr/\rho^2$ the integral is $\frac{m^2}{4}\cdot2\cdot\frac{2tr}{\rho^2}K_2(m\rho) = \frac{m^2tr}{\rho^2}K_2(m\rho)$.
>
> **Step 9** (assemble). $U = \frac{i}{2\pi^2r}\cdot\frac{m^2tr}{\rho^2}K_2(m\rho) = \frac{i\,m^2t}{2\pi^2\rho^2}K_2(m\rho)$.
>
> **What the derivation shows.**
> - The two routes share no intermediate step, so their agreement is a check of both.
> - The rapidity $\chi$ makes visible that only the invariant $\rho$ and the boost-covariant factor $t$ appear.
> - The user's notes state the arc condition without the damping factor; with the factor $p$ in the integrand the damping is what makes the arc vanish (Step 3).
>
> *Source: the user's PHY 513 notes, Ch. 2 §2.2 (Derivation "The same result directly from the radial integral", Steps 1–3, and Fig. 2.2)*

*Uses:* [[§C1a.3 Causal Structure and the Causality of a Single Particle#^thm-c1a-3-5|Theorem §C1a.3.5]], [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-3|Theorem §C2b.3.3]], [[§CA.4 Contour Integration#^thm-ca-4-2|Theorem §CA.4.2]], [[§CA.4 Contour Integration#^thm-ca-4-6|Theorem §CA.4.6]], [[§CA.4 Contour Integration#^thm-ca-4-8|Theorem §CA.4.8]], [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|Theorem §CA.1.1]], [[§CA.5 Gaussian Integrals, Stationary Phase and Bessel Functions#^def-ca-5-1|Def. §CA.5.1]]

> [!theorem] Theorem §C2b.3.9: The Spacelike Amplitude at Large Distance
> For $r > |t|$ and $m\rho \gg 1$, $\rho = \sqrt{r^2 - t^2}$,
>
> $$
> U(t, \mathbf x) = \frac{i\,m^{3/2}\,t}{(2\pi\rho)^{3/2}\,\rho}\,e^{-m\rho}\Bigl(1 + \frac{15}{8m\rho} + O\bigl((m\rho)^{-2}\bigr)\Bigr) ,
> $$
>
> and $U \neq 0$ at every spacelike point with $t \neq 0$. The leading term is the saddle-point result of [[§C1a.3 Causal Structure and the Causality of a Single Particle#^thm-c1a-3-6|Theorem §C1a.3.6]].
>
> *Source: the user's PHY 513 notes, Ch. 2 §2.2 (check (iii) of Derivation "The relativistic amplitude in closed form") · PHY 513 Lecture 2, Part A ("Quantum Causality is Violated") · PS §2.1, p. 14*

^thm-c2b-3-9

> [!derivation]- Derivation
> **Step 1** (the large-argument form). $K_2(w) = \sqrt{\pi/2w}\,e^{-w}\bigl[1 + \frac{4\cdot2^2 - 1}{8w} + \cdots\bigr] = \sqrt{\pi/2w}\,e^{-w}\bigl[1 + \frac{15}{8w} + \cdots\bigr]$ ([[§CA.5 Gaussian Integrals, Stationary Phase and Bessel Functions#^thm-ca-5-3|Theorem §CA.5.3]], 2 with $\nu = 2$).
>
> **Step 2** (insert). Into [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-8|Theorem §C2b.3.8]] with $w = m\rho$:
>
> $$
> \frac{im^2t}{2\pi^2\rho^2}\sqrt{\frac{\pi}{2m\rho}} = \frac{i\,m^{3/2}\,t\,\sqrt\pi}{2^{3/2}\,\pi^2\,\rho^{5/2}} = \frac{i\,m^{3/2}\,t}{2^{3/2}\pi^{3/2}\rho^{5/2}} = \frac{i\,m^{3/2}\,t}{(2\pi\rho)^{3/2}\rho} .
> $$
>
> **Step 3** (nonzero). $K_2(m\rho) > 0$ (Step 5 of Derivation §C2b.3.8), so the asymptotic form only describes the size of a function that vanishes nowhere off $t = 0$.
>
> **What the derivation shows.**
> - Outside the cone the amplitude is small on the scale $1/m$ but not zero: single-particle relativistic quantum mechanics violates [[§C1a.3 Causal Structure and the Causality of a Single Particle#^pr-c1a-3-1|Principle §C1a.3.1]]. Relativistic kinematics was not the error; there is no algebra mistake to find.
> - The relative correction $15/8m\rho$ is the $\nu = 2$ case of the same series that gives $3/8mr$ for $D_W$ ([[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-3|Theorem §C2b.3.3]]).

^der-c2b-3-9

*Uses:* [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-8|Theorem §C2b.3.8]], [[§CA.5 Gaussian Integrals, Stationary Phase and Bessel Functions#^thm-ca-5-3|Theorem §CA.5.3]]

> [!theorem] Theorem §C2b.3.10: The Relativistic Amplitude at Timelike Separation
> For $|t| > r$, with $\tau = \sqrt{t^2 - r^2}$,
>
> $$
> U(t, \mathbf x) = \frac{m^2\,t}{4\pi\tau^2}\,H^{(2)}_2(m\tau)\quad (t > 0), \qquad U(-t, \mathbf x) = \overline{U(t, \mathbf x)} ,
> $$
>
> an oscillating function, $U \simeq \frac{m^{3/2}t}{(2\pi\tau)^{3/2}\tau}\,e^{-i(m\tau - 5\pi/4)}$ for $t > 0$, $m\tau \gg 1$. On the light cone $U$ is singular and is defined only as the boundary value of [[§C1a.3 Causal Structure and the Causality of a Single Particle#^thm-c1a-3-4|Theorem §C1a.3.4]].
>
> *Source: the user's PHY 513 notes, Ch. 2 §2.2 (check (iv) of Derivation "The relativistic amplitude in closed form"; connection formula from DLMF §10.27, checked numerically there) · DLMF §10.17 (Hankel asymptotics)*

^thm-c2b-3-10

> [!derivation]- Derivation
> **Step 1** (the limit of $s$). In Step 3 of [[§C2b.3 Explicit Forms of the Wightman Function#^der-c2b-3-8|Derivation §C2b.3.8]] put $z = t - i\varepsilon$ with $t > r$: $s^2 = r^2 - t^2 + 2i\varepsilon t + \varepsilon^2 \to -\tau^2 + i0$, and the principal root of $-\tau^2 + i0$ is $+i\tau$ ([[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-4|Theorem §C2b.3.4]], Step 1). The limit is locally uniform in the open timelike region, so it is the restriction of the distribution $U$ there, as in Step 4 of Derivation §C2b.3.8.
>
> **Step 2** ($t > 0$). With $s = i\tau$, $s^2 = -\tau^2$:
>
> $$
> U = \frac{i\,m^2t\,K_2(im\tau)}{2\pi^2(-\tau^2)} = -\frac{i\,m^2t}{2\pi^2\tau^2}K_2(im\tau) .
> $$
>
> The connection formula $K_\nu(ix) = \frac\pi2(-i)^{\nu+1}H^{(2)}_\nu(x)$ for $x > 0$ ([[§CA.5 Gaussian Integrals, Stationary Phase and Bessel Functions#^thm-ca-5-4|Theorem §CA.5.4]], 3) with $\nu = 2$ and $(-i)^3 = i$ gives $K_2(im\tau) = \frac{i\pi}{2}H^{(2)}_2(m\tau)$, so $U = -\frac{im^2t}{2\pi^2\tau^2}\cdot\frac{i\pi}{2}H^{(2)}_2 = \frac{m^2t}{4\pi\tau^2}H^{(2)}_2(m\tau)$.
>
> **Step 3** ($t < 0$). By [[§C1a.3 Causal Structure and the Causality of a Single Particle#^thm-c1a-3-2|Theorem §C1a.3.2]], $\overline{U(t, \mathbf x)} = \int\frac{d^3p}{(2\pi)^3}e^{+iE_{\mathbf p}t - i\mathbf p\cdot\mathbf x} = U(-t, -\mathbf x)$ (complex conjugation of the transform of $e^{-iE_{\mathbf p}t}$, an identity in $\mathcal S'$). $E_{\mathbf p}$ is even in $\mathbf p$, so $U(-t, \cdot)$ is even in $\mathbf x$ (substitute $\mathbf p \to -\mathbf p$, Jacobian $1$: [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|Theorem §CA.3.7]], 1), and $U(-t, -\mathbf x) = U(-t, \mathbf x)$.
>
> **Step 4** (late proper times). $H^{(2)}_2(x) \simeq \sqrt{2/\pi x}\,e^{-i(x - 5\pi/4)}$ for $x \to \infty$ (DLMF §10.17), so $|U| \simeq \frac{m^2t}{4\pi\tau^2}\sqrt{\frac{2}{\pi m\tau}} = \frac{\sqrt2\,m^{3/2}t}{4\pi^{3/2}\tau^{5/2}} = \frac{m^{3/2}t}{(2\pi\tau)^{3/2}\tau}$, using $\sqrt2/4 = 2^{-3/2}$.
>
> **Step 5** (the cone). The function of Step 3 of Derivation §C2b.3.8 blows up as $s \to 0$: by Step 6 there, $U \simeq iz/\pi^2(r^2 - z^2)^2$ near the cone, a double pole in $r^2 - z^2$. At real $t$ it has no value on the cone and exists there only as the limit in $\mathcal S'$ of [[§C1a.3 Causal Structure and the Causality of a Single Particle#^thm-c1a-3-4|Theorem §C1a.3.4]]; by [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-7|Theorem §C2b.3.7]] its singular part is $2i\partial_t$ of the light-cone singularity of $D_W$ ([[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-6|Theorem §C2b.3.6]], 3).
>
> **What the derivation shows.**
> - Inside and outside the cone are the two sides of the cut of one analytic function: $K_2$ decay outside becomes Hankel oscillation inside, as $K_1$ does for $D_W$ ([[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-4|Theorem §C2b.3.4]]).
> - The moduli inside and outside have the same form, $m^{3/2}|t|\,\sigma^{-5/2}(2\pi)^{-3/2}$ with $\sigma = \tau$ or $\rho$; only the exponential differs, a phase inside and a damping outside.

^der-c2b-3-10

*Uses:* [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-8|Theorem §C2b.3.8]], [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-4|Theorem §C2b.3.4]], [[§CA.5 Gaussian Integrals, Stationary Phase and Bessel Functions#^thm-ca-5-4|Theorem §CA.5.4]], [[§C1a.3 Causal Structure and the Causality of a Single Particle#^thm-c1a-3-2|Theorem §C1a.3.2]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|Theorem §CA.3.7]], [[§C1a.3 Causal Structure and the Causality of a Single Particle#^thm-c1a-3-4|Theorem §C1a.3.4]], [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-7|Theorem §C2b.3.7]], [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-6|Theorem §C2b.3.6]]

![[ph-qft-c1-3-1.svg]]
*The single-particle amplitude at fixed $mt = 3$ (units $m = 1$): inside the cone (shaded) the Hankel form of Theorem §C2b.3.10, outside the $K_2$ form of Theorem §C2b.3.8 with its leading asymptotic term (dashed, Theorem §C2b.3.9; Theorem §C1a.3.6). It is singular on the cone and leaks outside it over the Compton wavelength $1/m$. Adapted from the user's PHY 513 notes, Fig. 2.3; recomputed from the closed forms, which were checked against the mode integral at complex $t$.*

> [!example] Example §C2b.3.1: Units Restored in the Single-Particle Amplitude
> Restore $\hbar$ and $c$ in $U = \frac{im^2t}{2\pi^2\rho^2}K_2(m\rho)$ and in the nonrelativistic prefactor $(m/2\pi it)^{3/2}$, and read off the range of the leak for an electron.
>
> **Step 1** (target). $U(t, \cdot) \to \delta^3$ ([[§C1a.3 Causal Structure and the Causality of a Single Particle#^thm-c1a-3-2|Theorem §C1a.3.2]]), so $U$ has dimension $L^{-3}$, mass dimension $3$ ([[§C1a.2 Natural Units and Dimensional Analysis#^thm-c1a-2-3|Theorem §C1a.2.3]], 4).
>
> **Step 2** (the argument first). $K_2$ needs a pure number ([[§C1a.2 Natural Units and Dimensional Analysis#^thm-c1a-2-3|Theorem §C1a.2.3]], 2): $m\rho$ is $ML$, and the length built from $m$ is $\hbar/mc$, so $m\rho \to mc\rho/\hbar$, the separation in reduced Compton wavelengths, with $\rho = \sqrt{r^2 - c^2t^2}$ ($x^0 = ct$).
>
> **Step 3** (the prefactor). $m^2t/\rho^2$ has $M^2TL^{-2}$; the deficit to $L^{-3}$ is $M^{-2}L^{-1}T^{-1} = M^aL^{2a + b}T^{-a - b}$, so $a = -2$, $b = 3$, and the $T$ equation checks: $-a - b = -1$ ([[P4 Restoring ħ and c#^p4-4|P4, step 4]]). Hence
>
> $$
> U(t, \mathbf x) = \frac{i\,m^2c^3\,t}{2\pi^2\hbar^2\rho^2}\,K_2\Bigl(\frac{mc\rho}{\hbar}\Bigr).
> $$
>
> **Step 4** (nonrelativistic). $m/t$ is $MT^{-1}$; with $\hbar$ ($ML^2T^{-1}$) $m/\hbar t$ is $L^{-2}$, so $(m/2\pi it)^{3/2} \to (m/2\pi i\hbar t)^{3/2}$, of dimension $L^{-3}$ (a fractional power is legitimate, rule 3), and the phase becomes $e^{imr^2/2\hbar t}$, as in [[§C4.1 Propagators#^thm-c4-1-4|QM Theorem §C4.1.4]].
>
> **Step 5** (the range). Before any integral, dimensional analysis says the spacelike amplitude can depend on $\rho$ only through $mc\rho/\hbar$. For an electron $\hbar/m_ec \simeq 3.9\times10^{-13}$ m: the distance over which single-particle relativistic quantum mechanics leaks causality.
>
> *Source: the user's PHY 513 notes, Ch. 2 §2.4 (Derivation "Restoring ħ and c: the recipe", example $U$; Rule 3 example; "The scale of causality violation")*

^ex-c2b-3-1

> [!remark]- Connections
> - The Euclidean function of Theorem §C2b.3.1, integrated over Euclidean time, gives $\int d\tau\,\frac{mK_1(m\sqrt{\tau^2 + r^2})}{4\pi^2\sqrt{\tau^2 + r^2}} = \frac{e^{-mr}}{4\pi r}$, the Yukawa potential, because the $\tau$ integral sets $p_4 = 0$ and leaves the static propagator $1/(\mathbf p^2 + m^2)$: [[§B4.1 The Klein–Gordon Equation#^rem-b4-1-4|REL Remark: Static solutions and the Yukawa potential]]. The same $e^{-mr}$ sets the range of the correlations $D_1$ and of meson exchange, QFT C7 (planned).
> - Imaginary time turns $e^{-iHt}$ into $e^{-H\tau}$; for the oscillator this links propagator and partition function ([[§C4.1 Propagators#^thm-c4-1-6|QM Theorem §C4.1.6]]), and the thermal ★ remark of §C2b.4 is its field version ([[§C2b.4 Microcausality and the Commutator Function#^rem-c2b-4-6|★ Remark: Other states]]); the Bose–Einstein occupation is [[§B10.1 Bose–Einstein and Fermi–Dirac Distributions#^thm-b10-1-2|TH Theorem §B10.1.2]].
> - [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-1|Theorem §CA.6.1]] (boundary values of analytic functions) is why every value here is a limit of the one function $W$ of Theorem §C2b.3.2, and why the limit is a distribution where it is not a function.
> - [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-4|Theorem §CA.6.4]] (the light-cone boundary value $1/(-x^2 + i0\,x^0)$) is the leading singularity of $D_W$ for every mass, Theorem §C2b.3.6, 3; [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-3|Theorem §CA.6.3]] (logarithms at the real axis) gives the finite jump of the subleading term.
> - [[§CA.2 Generalized Functions#^def-ca-2-3|Def. §CA.2.3]] (support and singular support) states where $D_W$ is a function: everywhere except the light cone.
> - [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-2|Theorem §CA.3.2]] (the transform on $\mathcal S'$) gives the four-dimensional Euclidean integral of Theorem §C2b.3.1 its meaning; [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|Theorem §CA.3.7]] and [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-9|Theorem §CA.3.9]] (rotations, frame choice) reduce the equal-time integral to one dimension.
> - [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-5|Theorem §CA.6.5]] (damping factors) is the regulator $e^{-\varepsilon p}$ of the third route, removed pointwise because the target is a smooth function there.
> - [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|Theorem §CA.1.1]], [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-2|Theorem §CA.1.2]] and [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-3|Theorem §CA.1.3]] license every exchange of a limit with an integral or a derivative in the three routes and in the remainder estimate of Theorem §C2b.3.6.
