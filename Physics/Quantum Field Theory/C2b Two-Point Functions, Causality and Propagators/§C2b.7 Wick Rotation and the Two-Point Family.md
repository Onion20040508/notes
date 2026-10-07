---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C2b
section: C2b.7
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription]] · ↑ [[· C2b Two-Point Functions, Causality and Propagators]] · [[§C2b.8 Particle Production by a Classical Source]] →

*Sources: the user's PHY 513 notes, Ch. 6 §§6.8, 6.10–6.12 and Ch. 2 §2.2 (eq. (DE)) · PHY 513 Lecture 6 (Larsen, 21 Sep 2026), Part B · Peskin & Schroeder §2.4, p. 31.*

Why is the Feynman contour singled out, and how do all the two-point functions fit together? Rotating the energy integral of the Feynman propagator of [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription|§C2b.6]] to imaginary energies gives the Euclidean propagator, whose position-space form is the Bessel function of [[§C2b.3 Explicit Forms of the Wightman Function|§C2b.3]]. The section ends with the whole family of two-point functions in one table, each row pointing to its home ([[§C2b.7 Wick Rotation and the Two-Point Family#^rem-c2b-7-2|Remark: The two-point functions at a glance]]), and the relations among them.

*Conventions* ([[Larsen PHY 513]]): Green's functions are normalized by $(\partial^2 + m^2)D_C = -i\delta^4$ (PS), so that $D_F = \langle0|T\{\hat\phi\hat\phi\}|0\rangle$ with no prefactor and $\tilde D_F = i/(p^2 - m^2 + i\varepsilon)$; Fourier conventions as in [[§CA.3 Fourier Transforms and Fourier Tricks#^def-ca-3-1|Def. §CA.3.1]]; $\xi = x - y$, $t = \xi^0$, $E = E_{\mathbf p}$.

## Wick rotation and the Euclidean propagator

> [!definition] Definition §C2b.7.1: Euclidean Propagator
> With $x_E = (\tau, \mathbf x)$, $p_E = (p_4, \mathbf p)$ and Euclidean products,
>
> $$
> D_E(x_E) \equiv \int\frac{d^4p_E}{(2\pi)^4}\,\frac{e^{ip_E\cdot x_E}}{p_E^2 + m^2} .
> $$
>
> Its denominator never vanishes, and it is invariant under four-dimensional rotations; the integral converges only as an iterated integral or in $\mathcal S'$ ([[§C2b.7 Wick Rotation and the Two-Point Family#^thm-c2b-7-4|Theorem §C2b.7.4]], 3); its value, $mK_1(mR)/4\pi^2R$ with $R = |x_E|$, is [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-1|Theorem §C2b.3.1]].
>
> *Source: the user's PHY 513 notes, Ch. 2 §2.2 (eq. (DE)), Ch. 6 §6.10 · PHY 513 Lecture 6, "Another perspective: the Euclidean Green's Function"*

^def-c2b-7-1

> [!theorem] Theorem §C2b.7.1: Wick Rotation of a Momentum Integral
> If $F$ is analytic in the first and third quadrants of the $p^0$-plane and $F(p)/(p^2 - m^2)$ decays faster than $1/|p^0|$ there, the real $p^0$-axis may be rotated counterclockwise onto $p^0 = ip_4$ without crossing a Feynman pole, and
>
> $$
> \int\frac{d^4p}{(2\pi)^4}\,\frac{i\,F(p)}{p^2 - m^2 + i\varepsilon} = \int\frac{d^4p_E}{(2\pi)^4}\,\frac{F(ip_4, \mathbf p)}{p_E^2 + m^2} .
> $$
>
> *Source: the user's PHY 513 notes, Ch. 6 §6.10 (Wick rotation, Caution "When the rotation is legitimate") · PHY 513 Lecture 6, "Another perspective: the Euclidean Green's Function"*

^thm-c2b-7-1

> [!derivation]- Derivation
> **Step 1** (where the poles are). By [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-9|Theorem §C2b.6.9]] the Feynman poles are $E - i\varepsilon$ (fourth quadrant) and $-E + i\varepsilon$ (second quadrant).
>
> **Step 2** (the closed contour). Take the real axis from $-L$ to $L$, the arc from $L$ to $iL$ (first quadrant), the imaginary axis from $iL$ down to $-iL$, and the arc from $-iL$ to $-L$ (third quadrant). It consists of two loops, around the first and third quadrants, which contain no pole; by Cauchy's theorem ([[§CA.4 Contour Integration#^thm-ca-4-2|Theorem §CA.4.2]]) the total is zero.
>
> **Step 3** (the arcs). By the assumed decay, the integrand times the arc length $\frac\pi2L$ tends to zero (ML, [[§CA.4 Contour Integration#^thm-ca-4-6|Theorem §CA.4.6]]). Hence $\int_{-\infty}^{\infty}dp^0(\cdots) = \int_{-i\infty}^{i\infty}dp^0(\cdots)$: the real axis rotated counterclockwise by $90°$.
>
> **Step 4** (substitute $p^0 = ip_4$). $p_4$ runs from $-\infty$ to $\infty$; $dp^0 = i\,dp_4$; and $p^2 - m^2 = (ip_4)^2 - \mathbf p^2 - m^2 = -(p_E^2 + m^2)$, which never vanishes, so the $i\varepsilon$ may be dropped (for each $\varepsilon > 0$ the rotation is an identity of absolutely convergent integrals, the poles $\pm(E - i\varepsilon')$ staying in the second and fourth quadrants, and the rotated integrand has no $\varepsilon$ left to take a limit of; Sokhotski–Plemelj has nothing to do away from zeros, [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^cau-ca-6-1|§CA.6, Caution: What the formula does and does not say]]). Then
>
> $$
> \frac{i\,dp^0}{p^2 - m^2 + i\varepsilon} = \frac{i\cdot i\,dp_4}{-(p_E^2 + m^2)} = \frac{dp_4}{p_E^2 + m^2} .
> $$
>
> ⚑ By-product: with a factor $e^{-ip^0t}$ present, $|e^{-ip^0t}| = e^{t\operatorname{Im}p^0}$ grows in the first quadrant for $t > 0$ (and in the third for $t < 0$), so the arcs do not vanish and the rotation of $p^0$ alone is *not* allowed in position space → [[§C2b.7 Wick Rotation and the Two-Point Family#^thm-c2b-7-2|Theorem §C2b.7.2]].
>
> **What the derivation shows.**
> - Only the Feynman prescription allows the rotation: the retarded poles $\pm E - i\varepsilon$ include one in the third quadrant.
> - On the imaginary axis energy and momentum enter symmetrically; this is how loop integrals are done (QFT C7, planned).

^der-c2b-7-1

*Uses:* [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-9|Theorem §C2b.6.9]], [[§CA.4 Contour Integration#^thm-ca-4-2|Theorem §CA.4.2]], [[§CA.4 Contour Integration#^thm-ca-4-6|Theorem §CA.4.6]], [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^cau-ca-6-1|§CA.6, Caution: What the formula does and does not say]]

> [!theorem] Theorem §C2b.7.2: The Feynman Function at Imaginary Time
> Rotating the time as well, $t = -i\tau$ with $\tau > 0$ (so that $p^0t = p_4\tau$ stays real),
>
> $$
> D_F(-i\tau, \boldsymbol\xi) = D_E(\tau, \boldsymbol\xi) .
> $$
>
> *Source: the user's PHY 513 notes, Ch. 6 §6.10 (Caution "When the rotation is legitimate") · PHY 513 Lecture 6*

^thm-c2b-7-2

> [!derivation]- Derivation
> **Step 1** (which piece). For $\operatorname{Re}\xi^0 > 0$, $D_F = D_W(\xi)$ ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-2|Theorem §C2b.6.2]]), and $D_W$ is the boundary value of the function $W(z, \boldsymbol\xi)$, analytic for $\operatorname{Im}z < 0$ ([[§C2b.2 The Wightman Function#^thm-c2b-2-5|Theorem §C2b.2.5]]). The continuation of $D_F$ from positive real time into the lower half-plane is therefore $W$. (As distributions: on the open half-space $\xi^0 > 0$, $D_F$ and $D_W$ coincide, [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-4|Theorem §C2b.6.4]], 1, and there $D_W$ is the boundary value of $W$, [[§C2b.2 The Wightman Function#^thm-c2b-2-5|Theorem §C2b.2.5]].)
>
> **Step 2** (on the ray). At $z = -i\tau$: $W(-i\tau, \boldsymbol\xi) = \int\frac{d^4p_E}{(2\pi)^4}\frac{e^{ip_E\cdot x_E}}{p_E^2 + m^2}$ ([[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-1|Theorem §C2b.3.1]], Steps 1–2), which is $D_E$ ([[§C2b.7 Wick Rotation and the Two-Point Family#^def-c2b-7-1|Def. §C2b.7.1]]).
>
> **Step 3** (the same in momentum space, as a mnemonic). At $t = -i\tau$ and $p^0 = ip_4$, $p^0t = (ip_4)(-i\tau) = p_4\tau$ stays real, and the integrand of Theorem §C2b.7.1 times $e^{-ip^0t + i\mathbf p\cdot\boldsymbol\xi}$ becomes $\frac{e^{-ip_4\tau + i\mathbf p\cdot\boldsymbol\xi}}{p_E^2 + m^2}$; $p_4 \to -p_4$ (Jacobian 1, the denominator even in $p_4$; [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|Theorem §CA.3.7]], 1) turns $e^{-ip_4\tau}$ into the $e^{ip_4\tau}$ of $D_E$. This is not a proof: with real $t$ the arcs of the rotation do not vanish (by-product of Theorem §C2b.7.1), and with $t = -i\tau$ the real-$p^0$ integral itself diverges, since $|e^{-ip^0t}| = e^{-p^0\tau}$ grows as $p^0 \to -\infty$. Time and energy must be rotated together so that $p^0t$ stays real; Steps 1–2, which continue in $t$ through $D_W$, are the proof.
>
> **What the derivation shows.**
> - Euclidean, Wightman and Feynman functions are boundary values of one analytic function; the slides' "Feynman prescription = Euclidean prescription, continued" made precise → [[§C2b.7 Wick Rotation and the Two-Point Family#^rem-c2b-7-1|Remark: Why the Feynman contour is singled out]].

^der-c2b-7-2

*Uses:* [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-2|Theorem §C2b.6.2]], [[§C2b.2 The Wightman Function#^thm-c2b-2-5|Theorem §C2b.2.5]], [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-1|Theorem §C2b.3.1]], [[§C2b.7 Wick Rotation and the Two-Point Family#^def-c2b-7-1|Def. §C2b.7.1]], [[§C2b.7 Wick Rotation and the Two-Point Family#^thm-c2b-7-1|Theorem §C2b.7.1]]

> [!theorem] Theorem §C2b.7.3: The Feynman Function in Position Space
> For all real $\xi$,
>
> $$
> D_F(\xi) = \frac{m\,K_1(ms)}{4\pi^2s}, \qquad s = \sqrt{-\xi^2 + i\varepsilon} ,
> $$
>
> even in $\xi$, real at spacelike separation, and with the same branch for both signs of $\xi^0$ inside the cone: the Feynman prescription is the infinitesimal Wick rotation $t \to t(1 - i\varepsilon)$.
>
> *Source: the user's PHY 513 notes, Ch. 6 §6.10 ("The Feynman function in position space")*

^thm-c2b-7-3

> [!derivation]- Derivation
> **Step 1** ($\xi^0 > 0$). $D_F = D_W(\xi)$, the boundary value from $z = \xi^0 - i\varepsilon$ of $W = mK_1(ms)/4\pi^2s$ with $s^2 = \boldsymbol\xi^2 - z^2$ ([[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-2|Theorem §C2b.3.2]]): $s^2 = \boldsymbol\xi^2 - (\xi^0)^2 + 2i\varepsilon\xi^0 + \varepsilon^2 = -\xi^2 + i\varepsilon'$ with $\varepsilon' = 2\varepsilon\xi^0 > 0$.
>
> **Step 2** ($\xi^0 < 0$). $D_F = D_W(-\xi)$, the boundary value at the point $-\xi$, i.e. $z = -\xi^0 - i\varepsilon$ and $\boldsymbol\xi \to -\boldsymbol\xi$: $s^2 = \boldsymbol\xi^2 - (\xi^0 + i\varepsilon)^2 = -\xi^2 - 2i\varepsilon\xi^0 - \varepsilon^2 = -\xi^2 + i\varepsilon''$ with $\varepsilon'' = -2\varepsilon\xi^0 > 0$ because $\xi^0 < 0$.
>
> **Step 3** (one formula). In both cases the infinitesimal added to $-\xi^2$ is positive: $s = \sqrt{-\xi^2 + i\varepsilon}$. (Steps 1–2 are pointwise limits at points off the light cone, where $D_F$ is a function, [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-6|Theorem §C2b.3.6]], 1; on the cone the formula is read as a distribution, [[§C2b.7 Wick Rotation and the Two-Point Family#^thm-c2b-7-4|Theorem §C2b.7.4]], 2.) The formula depends on $\xi$ only through $\xi^2$, hence it is even and invariant. Outside the cone $-\xi^2 > 0$ and $s$ is real ([[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-3|Theorem §C2b.3.3]]); inside, $s = i\tau$ for both signs of $\xi^0$.
>
> **Step 4** (infinitesimal rotation). With $t \to t(1 - i\varepsilon)$, $-\xi^2 = \mathbf r^2 - t^2 \to \mathbf r^2 - t^2(1 - 2i\varepsilon) = -\xi^2 + 2i\varepsilon t^2$: the same sign for both signs of $t$.
>
> **What the derivation shows.**
> - This is the position-space mirror of $p^2 - m^2 + i\varepsilon$: the same branch everywhere is what time ordering does.
> - Inside the cone, $D_F = \frac{m}{8\pi\tau}[Y_1(m\tau) + iJ_1(m\tau)]$ for both signs of $\xi^0$ (Theorem §C2b.3.4 with $\operatorname{sgn} \to +$).

^der-c2b-7-3

*Uses:* [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-2|Theorem §C2b.3.2]], [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-3|Theorem §C2b.3.3]], [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-4|Theorem §C2b.3.4]]

> [!remark] Remark: Why the Feynman contour is singled out
> On the imaginary axis $p^2 - m^2 = -(p_4^2 + \mathbf p^2 + m^2) < 0$: the pole problem disappears, and energy and momentum enter symmetrically. In the slides' words, the Feynman prescription is the Euclidean prescription, analytically continued to Lorentzian signature: four-dimensional rotation symmetry, which is relativity continued to imaginary time, is manifest at every step. (The slides write $p^0_E = ip^0_M$; $p^0 = ip_4$ here differs by $p_4 \to -p_4$, which the integral does not see.) The imaginary-time function is also the vacuum two-point function at imaginary time ([[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-1|Theorem §C2b.3.1]]), so Euclidean, Wightman and Feynman functions are three boundary values of one analytic function.
>
> *Source: the user's PHY 513 notes, Ch. 6 §6.10 · PHY 513 Lecture 6, "Another perspective: the Euclidean Green's Function"*

^rem-c2b-7-1

> [!theorem] Theorem §C2b.7.4: Wick Rotation Continues One Distribution
> 1. *(Momentum space)* At fixed $\mathbf p$, $\tilde D_F(\cdot, \mathbf p)$ is the boundary value in $\mathcal S'(\mathbb R)$ of $G(w) = i/(w^2 - E_{\mathbf p}^2)$, analytic in the open first and third quadrants of $w = p^0$, along $w = e^{i\vartheta}p^0$, $\vartheta \to 0^+$; on the imaginary axis $w = ip_4$, $i\,G(ip_4) = 1/(p_E^2 + m^2)$, the Euclidean integrand.
> 2. *(Position space)* With $\mathcal W(s^2) = mK_1(ms)/4\pi^2s$ ([[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-2|Theorem §C2b.3.2]]), analytic off $s^2 \in (-\infty, 0]$: $D_E = \mathcal W(R^2)$ at Euclidean points; off the light cone $D_F = \mathcal W(-\xi^2 + i0)$ and $D_W = \mathcal W(-\xi^2 + i0\,\xi^0)$; near the cone (away from $\xi = 0$) both have the singular part $\frac{1}{4\pi^2}\frac{1}{-\xi^2 + i0}$, respectively $\frac{1}{4\pi^2}\frac{1}{-\xi^2 + i0\,\xi^0}$ ([[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-4|Theorem §CA.6.4]]).
> 3. $D_E$ is a locally integrable function ($\simeq 1/4\pi^2R^2$ at $R \to 0$), the $\mathcal S'$ transform of $1/(p_E^2 + m^2)$; its singular support is the single point $x_E = 0$, where $D_F$'s is the whole cone.
>
> *Source: the user's PHY 513 notes, Ch. 6 §6.10 ("Feynman prescription = Euclidean prescription, continued"; Caution "When the rotation is legitimate") · PHY 513 Lecture 6 · stated here for distributions (standard: Osterwalder–Schrader; Streater & Wightman, Ch. 3)*

^thm-c2b-7-4

> [!derivation]- Derivation
> **Step 1** ($G$ is analytic in the open quadrants). $w^2 - E^2 = 0$ only at $w = \pm E$, on the real axis; so $G$ is analytic in the open first and third quadrants.
>
> **Step 2** (the boundary value is the Feynman distribution). On $w = e^{i\vartheta}p^0$, $w^2 - E^2 = (p^0)^2 - E^2 + i(p^0)^2\sin2\vartheta + O(\vartheta^2(p^0)^2)$: an imaginary part $\ge 0$, positive except at $p^0 = 0$, where $w^2 - E^2 = -E^2 \ne 0$. Factor $w^2 - E^2 = (w - E)(w + E)$. Near $p^0 = E$, $w - E = p^0 - E + i\vartheta p^0 + O(\vartheta^2)$ has imaginary part $\approx \vartheta E > 0$; near $p^0 = -E$, $w + E = p^0 + E + i\vartheta p^0 + O(\vartheta^2)$ has imaginary part $\approx -\vartheta E < 0$. So, with $\vartheta$ in the role of $\varepsilon$ and the $O(\vartheta^2)$ shift of the real part harmless (Step 3 of [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-6|Theorem §CA.6.6]]), the limit in $\mathcal S'(\mathbb R)$ is $\frac{i}{(p^0 - E + i0)(p^0 + E - i0)}$, the Feynman case $\sigma_+ = +1$, $\sigma_- = -1$ of [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-4|Theorem §C2b.5.4]], 1, which is $i/(p^2 - m^2 + i0) = \tilde D_F$ ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-10|Theorem §C2b.6.10]], Step 5); away from the poles the infinitesimal is irrelevant ([[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^cau-ca-6-1|§CA.6, Caution: What the formula does and does not say]]), and $|G(e^{i\vartheta}p^0)| \le C/(1 + (p^0)^2)$ uniformly for small $\vartheta$ away from them. Part 1, first half.
>
> **Step 3** (the imaginary axis). At $w = ip_4$: $w^2 - E^2 = -(p_4^2 + E^2) = -(p_E^2 + m^2)$, and with $dp^0 = i\,dp_4$, $G(ip_4)\,dp^0 = i\,G(ip_4)\,dp_4 = \frac{dp_4}{p_E^2 + m^2}$, as in Step 4 of Derivation §C2b.7.1. The rotation $\vartheta: 0 \to \frac\pi2$ through the quadrants free of poles is Theorem §C2b.7.1. Part 1.
>
> **Step 4** (position space). $\mathcal W$ is analytic for $s^2 \notin (-\infty, 0]$ (Theorem §C2b.3.2, Steps 1–3). At Euclidean points $s^2 = \tau^2 + \boldsymbol\xi^2 = R^2 > 0$: $D_E = \mathcal W(R^2)$ ([[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-1|Theorem §C2b.3.1]]). Off the cone, $D_F = \mathcal W(-\xi^2 + i0)$ is [[§C2b.7 Wick Rotation and the Two-Point Family#^thm-c2b-7-3|Theorem §C2b.7.3]], and $D_W = \mathcal W(-\xi^2 + i0\,\xi^0)$ is Theorems §C2b.3.3–§C2b.3.4. Near a point of the cone with $\xi^0 > 0$, $D_F = D_W$ there ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-4|Theorem §C2b.6.4]]), whose singular part is $\frac{1}{4\pi^2}\frac{1}{-\xi^2 + i0\,\xi^0} = \frac{1}{4\pi^2}\frac{1}{-\xi^2 + i0}$ ([[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-6|Theorem §C2b.3.6]], 3); near a point with $\xi^0 < 0$, $D_F = D_W(-\xi)$, whose singular part is the same expression with $-\xi$, again $\frac{1}{4\pi^2}\frac{1}{-\xi^2 + i0}$. Part 2.
>
> ⚑ By-product: the Feynman singular part $\frac{1}{-\xi^2 + i0} = -\mathcal P\frac{1}{\xi^2} - i\pi\delta(\xi^2)$ has the same sign of $i\pi\delta(\xi^2)$ on both halves of the cone, the position-space form of "$m^2 \to m^2 - i\varepsilon$" → [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-9|Theorem §C2b.6.9]].
>
> **Step 5** ($D_E$ as a distribution). From Theorem §C2b.3.1, $D_E = mK_1(mR)/4\pi^2R$, smooth for $R > 0$, $\simeq 1/4\pi^2R^2$ as $R \to 0$ ([[§CA.5 Gaussian Integrals, Stationary Phase and Bessel Functions#^thm-ca-5-3|Theorem §CA.5.3]], 3) and exponentially decaying as $R \to \infty$. In four dimensions $\int_{R \le 1}d^4x_E/R^2 = 2\pi^2\int_0^1R\,dR < \infty$, so $D_E$ is locally integrable and a tempered distribution ([[§CA.2 Generalized Functions#^thm-ca-2-1|Theorem §CA.2.1]], 2). Its transform is $1/(p_E^2 + m^2)$ in $\mathcal S'$, as shown in Step 2 of [[§C2b.3 Explicit Forms of the Wightman Function#^der-c2b-3-1|Derivation §C2b.3.1]] (bounded symbol, [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-2|Theorem §CA.3.2]]; iterated integral equal to $\int d^4x_E\,f\,D_E$ by Fubini and dominated convergence). The only non-smooth point is $x_E = 0$. Part 3.
>
> **What the derivation shows.**
> - Euclidean, Feynman and Wightman functions are one analytic function read on three sets: the positive real $s^2$-axis (Euclidean), and the negative real axis approached from $\operatorname{Im}s^2 > 0$ (Feynman) or from the side fixed by $\operatorname{sgn}\xi^0$ (Wightman).
> - In Euclidean signature the light cone collapses to a point: the only coincidence singularity left is $x_E = 0$, which is why loop integrals are done there.

^der-c2b-7-4

*Uses:* [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-1|Theorem §C2b.3.1]], [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-2|Theorem §C2b.3.2]], [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-6|Theorem §C2b.3.6]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-4|Theorem §C2b.6.4]], [[§C2b.7 Wick Rotation and the Two-Point Family#^thm-c2b-7-1|Theorem §C2b.7.1]], [[§C2b.7 Wick Rotation and the Two-Point Family#^thm-c2b-7-3|Theorem §C2b.7.3]], [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-4|Theorem §C2b.5.4]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-10|Theorem §C2b.6.10]], [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-6|Theorem §CA.6.6]], [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^cau-ca-6-1|§CA.6, Caution: What the formula does and does not say]], [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-4|Theorem §CA.6.4]], [[§CA.5 Gaussian Integrals, Stationary Phase and Bessel Functions#^thm-ca-5-3|Theorem §CA.5.3]], [[§CA.2 Generalized Functions#^thm-ca-2-1|Theorem §CA.2.1]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-2|Theorem §CA.3.2]]

## The two-point functions, all together

> [!remark] Remark: The two-point functions at a glance
> A summary of the family; each function is defined and derived in the box linked in the last column. With $\xi = x - y$, vacuum expectation values, "homogeneous" meaning $(\partial^2 + m^2)f = 0$ and "Green's" meaning $(\partial^2 + m^2)f = -i\delta^4$, both in $\mathcal S'$; the last column says in what sense each is a distribution:
>
> | name | definition | type | momentum space (times $\int\frac{d^4p}{(2\pi)^4}e^{-ip\cdot\xi}$) | as a distribution |
> | --- | --- | --- | --- | --- |
> | Wightman $D_W(\xi)$ | $\langle0\vert\hat\phi(x)\hat\phi(y)\vert0\rangle$ | homogeneous | $2\pi\theta(p^0)\delta(p^2 - m^2)$ | boundary value from $\operatorname{Im}\xi^0 < 0$ — [[§C2b.2 The Wightman Function#^def-c2b-2-1\|Def. §C2b.2.1]], [[§C2b.2 The Wightman Function#^thm-c2b-2-5\|Theorem §C2b.2.5]] |
> | reversed $D_W(-\xi)$ | $\langle0\vert\hat\phi(y)\hat\phi(x)\vert0\rangle$ | homogeneous | $2\pi\theta(-p^0)\delta(p^2 - m^2)$ | boundary value from $\operatorname{Im}\xi^0 > 0$, the complex conjugate — [[§C2b.2 The Wightman Function#^thm-c2b-2-4\|Theorem §C2b.2.4]] |
> | commutator $iD(\xi)$ | $\langle0\vert[\hat\phi(x), \hat\phi(y)]\vert0\rangle$ | homogeneous | $2\pi\operatorname{sgn}(p^0)\delta(p^2 - m^2)$ | difference of the two boundary values; supported in the closed cone — [[§C2b.4 Microcausality and the Commutator Function#^def-c2b-4-1\|Def. §C2b.4.1]], [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-6\|Theorem §C2b.4.6]] |
> | Hadamard $D_1(\xi)$ | $\langle0\vert\{\hat\phi(x), \hat\phi(y)\}\vert0\rangle$ | homogeneous | $2\pi\delta(p^2 - m^2)$ | sum of the two boundary values; singular on the cone — [[§C2b.4 Microcausality and the Commutator Function#^def-c2b-4-2\|Def. §C2b.4.2]], [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-4\|Theorem §C2b.4.4]] |
> | retarded $D_R(\xi)$ | $\theta(\xi^0)\,iD(\xi)$ | Green's | $\frac{i}{(p^0 + i\varepsilon)^2 - E_{\mathbf p}^2}$ | product $\theta\cdot iD$ slice by slice; the fundamental solution supported in $\xi^0 \ge 0$ — [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-5\|Theorem §C2b.5.5]], [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-6\|Theorem §C2b.5.6]] |
> | advanced $D_A(\xi)$ | $-\theta(-\xi^0)\,iD(\xi)$ | Green's | $\frac{i}{(p^0 - i\varepsilon)^2 - E_{\mathbf p}^2}$ | mirror product, supported in $\xi^0 \le 0$ — [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-7\|Theorem §C2b.5.7]] |
> | principal $\bar D(\xi)$ | $\frac12(D_R + D_A)$ | Green's | $i\,\mathcal P\frac{1}{p^2 - m^2}$ | product $\frac12\operatorname{sgn}(\xi^0)\,iD$ slice by slice; transform a principal value — [[§C2b.5 Green's Functions and Contours#^def-c2b-5-3\|Def. §C2b.5.3]], [[§CA.2 Generalized Functions#^def-ca-2-10\|Def. §CA.2.10]] |
> | Feynman $D_F(\xi)$ | $\langle0\vert T\{\hat\phi(x)\hat\phi(y)\}\vert0\rangle$ | Green's | $\frac{i}{p^2 - m^2 + i\varepsilon}$ | limit $\varepsilon \to 0^+$ in $\mathcal S'$ — [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-2\|Theorem §C2b.6.2]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-10\|Theorem §C2b.6.10]]; extension of $\theta\cdot D_W$ — [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-4\|Theorem §C2b.6.4]] |
> | anti-Feynman $D_{\bar F}(\xi)$ | $-\langle0\vert\bar T\{\hat\phi(x)\hat\phi(y)\}\vert0\rangle$ | Green's | $\frac{i}{p^2 - m^2 - i\varepsilon}$ | the conjugate limit, $-i\varepsilon$ — [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-3\|Theorem §C2b.6.3]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-10\|Theorem §C2b.6.10]]; $\bar T$ — [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^def-c2b-6-2\|Def. §C2b.6.2]] |
>
> *Source: the user's PHY 513 notes, Ch. 6 §6.11 (Definition "The family"), §6.8 (table of contours)*

^rem-c2b-7-2

> [!theorem] Theorem §C2b.7.5: Relations in the Two-Point Family
> 1. $D_R - D_A = iD$, and $\bar D = \frac12\operatorname{sgn}(\xi^0)\,iD$.
> 2. $D_F = \frac12D_1 + \bar D$ and $D_{\bar F} = -\frac12D_1 + \bar D = -\overline{D_F}$; hence $D_F - D_{\bar F} = D_1$, $\operatorname{Re}D_F = \frac12D_1$, $\operatorname{Im}D_F = \frac12\operatorname{sgn}(\xi^0)D$.
> 3. $D_F = D_R + D_W(-\xi) = D_A + D_W(\xi)$.
> 4. At spacelike separation $D_R = D_A = \bar D = 0$ and $D_F = D_W = \frac12D_1 = \dfrac{m\,K_1(mr)}{4\pi^2r}$, $r = \sqrt{-\xi^2}$.
>
> *Source: the user's PHY 513 notes, Ch. 6 §6.11 (Derivations "Relations in position space", "Relations in momentum space", "At spacelike separation"), §6.8 (eq. (Grelations))*

^thm-c2b-7-5

> [!derivation]- Derivation
> **Step 0** (the one input). $D_W(\pm\xi) = \frac12\bigl(D_1(\xi) \pm iD(\xi)\bigr)$ with $D_1$ even, $D$ odd and both real ([[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-3|Theorem §C2b.4.3]]).
>
> **Step 1** ($R$, $A$, $\bar D$). From [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-5|Theorem §C2b.5.5]] and [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-7|Theorem §C2b.5.7]], $D_R - D_A = \theta(\xi^0)iD + \theta(-\xi^0)iD = iD$, using $\theta(s) + \theta(-s) = 1$ (for slice products, [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-6|Theorem §C2b.5.6]], 1, this is $\int_0^\infty dt + \int_{-\infty}^0dt = \int dt$); and, by [[§C2b.5 Green's Functions and Contours#^def-c2b-5-3|Def. §C2b.5.3]], $\bar D = \frac12(D_R + D_A) = \frac12[\theta(\xi^0) - \theta(-\xi^0)]iD = \frac12\operatorname{sgn}(\xi^0)iD$.
>
> **Step 2** ($D_F$). $D_F = \theta(\xi^0)\cdot\frac12(D_1 + iD) + \theta(-\xi^0)\cdot\frac12(D_1 - iD) = \frac12D_1[\theta + \theta] + \frac12iD[\theta(\xi^0) - \theta(-\xi^0)] = \frac12D_1 + \bar D$.
>
> **Step 3** ($D_{\bar F}$). By [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-3|Theorem §C2b.6.3]], $D_{\bar F} = -\theta(\xi^0)\cdot\frac12(D_1 - iD) - \theta(-\xi^0)\cdot\frac12(D_1 + iD) = -\frac12D_1 + \frac12\operatorname{sgn}(\xi^0)iD = -\frac12D_1 + \bar D$. Since $D$, $D_1$ are real (as distributions, [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-4|Theorem §C2b.4.4]], 1), $\overline{D_F} = \frac12D_1 - \frac12\operatorname{sgn}(\xi^0)iD = -D_{\bar F}$.
>
> **Step 4** (consequences). Subtracting, $D_F - D_{\bar F} = D_1$. Real and imaginary parts of Step 2: $\operatorname{Re}D_F = \frac12D_1$, $\operatorname{Im}D_F = \frac12\operatorname{sgn}(\xi^0)D$.
>
> **Step 5** (part 3). $D_R + D_W(-\xi) = D_F$ is [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-2|Theorem §C2b.6.2]]. For $D_A + D_W(\xi)$: if $t > 0$ it is $0 + D_W(\xi)$; if $t < 0$ it is $-[D_W(\xi) - D_W(-\xi)] + D_W(\xi) = D_W(-\xi)$; both match $D_F$.
>
> **Step 6** (spacelike). $D = 0$ there (it vanishes as a distribution on the open spacelike region, [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-6|Theorem §C2b.4.6]], so restricted there all identities are between functions) ([[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-5|Theorem §C2b.4.5]]), so $D_R = D_A = \bar D = 0$, and $D_F = \frac12D_1 = D_W$, whose value is [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-3|Theorem §C2b.3.3]].
>
> ⚑ By-product: every function that could carry an influence vanishes at spacelike separation, and what remains is the vacuum correlation $D_1$ → [[§C2b.7 Wick Rotation and the Two-Point Family#^rem-c2b-7-4|★ Remark: Exponential clustering]].
>
> **What the derivation shows.**
> - The Feynman function is a Green's function ($\bar D$) plus a homogeneous solution ($\frac12D_1$), as Theorem §C2b.5.3 requires; the position-space derivation used only operator algebra.

^der-c2b-7-5

*Uses:* [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-3|Theorem §C2b.4.3]], [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-5|Theorem §C2b.4.5]], [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-3|Theorem §C2b.3.3]], [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-5|Theorem §C2b.5.5]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-2|Theorem §C2b.6.2]], [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-7|Theorem §C2b.5.7]]

> [!derivation]- Derivation (second route: momentum space)
> **Step 1** (retarded and advanced denominators). By [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-9|Theorem §C2b.6.9]] they are $p^2 - m^2 \pm i\varepsilon\operatorname{sgn}p^0$; by Sokhotski–Plemelj ([[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-2|Theorem §CA.6.2]]; in four variables [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-6|Theorem §CA.6.6]], 2, a limit in $\mathcal S'(\mathbb R^4)$) $\frac{1}{p^2 - m^2 \pm i\varepsilon\operatorname{sgn}p^0} = \mathcal P\frac{1}{p^2 - m^2} \mp i\pi\operatorname{sgn}(p^0)\delta(p^2 - m^2)$.
>
> **Step 2** ($\bar D$). Averaging, the delta terms cancel: $\tilde{\bar D} = i\,\mathcal P\frac{1}{p^2 - m^2}$.
>
> **Step 3** ($D_F$; [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-6|Theorem §CA.6.6]], 1). $\tilde D_F = \frac{i}{p^2 - m^2 + i\varepsilon} = i\Bigl[\mathcal P\frac{1}{p^2 - m^2} - i\pi\delta(p^2 - m^2)\Bigr] = i\,\mathcal P\frac{1}{p^2 - m^2} + \pi\delta(p^2 - m^2) = \tilde{\bar D} + \tfrac12\tilde D_1$, with $\tilde D_1 = 2\pi\delta(p^2 - m^2)$ (table).
>
> **What the derivation shows.**
> - Part 2 again, independently: the principal value is the Green's-function part, the delta function the homogeneous part. This route used only distribution theory.
>
> *Source: the user's PHY 513 notes, Ch. 6 §6.11 (Derivation "Relations in momentum space")*

*Uses:* [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-2|Theorem §CA.6.2]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-9|Theorem §C2b.6.9]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-11|Theorem §C2b.6.11]]

> [!remark] Remark: Which Green's function when
> There is no single right answer: the choice is a boundary condition, and the physical question imposes it. A source switched on in the laboratory and measured afterwards calls for the retarded function: classical radiation (the retarded potentials and Liénard–Wiechert fields are the massless retarded function, [[§B11.1★ Potentials, Gauges and Retarded Potentials#^thm-b11-1-4|EM Theorem §B11.1.4]]), linear response in condensed matter ([[§C2b.5 Green's Functions and Contours#^rem-c2b-5-4|§C2b.5, Remark: Measurable response is a retarded commutator]]), and particle production by a classical source ([[§C2b.8 Particle Production by a Classical Source|§C2b.8]]). Quantum amplitudes will turn out to involve time-ordered products, hence the Feynman function; with interactions this will be derived, not chosen (QFT C6, planned). The Feynman function treats the two orderings symmetrically, positive frequency forward and negative frequency backward in time, the reading of the two terms of the commutator in [[§C2b.4 Microcausality and the Commutator Function#^rem-c2b-4-2|§C2b.4, Remark: Two orderings that cancel]].
>
> *Source: the user's PHY 513 notes, Ch. 6 §6.12 · PS §2.4, p. 31*

^rem-c2b-7-3

> [!remark]- ★ Remark: Exponential clustering
> At spacelike separation every function that involves the commutator vanishes, and what remains is the vacuum correlation $D_1$, decaying like $r^{-3/2}e^{-mr}$. That the correlation length equals the Compton wavelength is not special to the free field: in any theory with a mass gap $m$, connected vacuum correlations at spacelike separation decay at least as fast as $e^{-mr}$ (exponential clustering, a theorem of axiomatic field theory). The Euclidean continuation shows why: in imaginary time a gap is a correlation length, as in statistical mechanics.
>
> *Source: the user's PHY 513 notes, Ch. 6 §6.11 ("At spacelike separation")*

^rem-c2b-7-4

> [!remark]- Connections
> - Wick rotation is the field version of imaginary time in quantum statistical mechanics: $e^{-i\hat Ht} \to e^{-\hat H\tau}$ links the propagator to the partition function ([[§C4.1 Propagators#^thm-c4-1-6|QM Theorem §C4.1.6]]) and the Euclidean action to a Boltzmann weight; the Euclidean propagator is the correlation function of a statistical field.
> - Euclidean, Wightman and Feynman functions are three boundary values of one analytic function: the Euclidean evaluation is [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-1|Theorem §C2b.3.1]], the boundary value [[§C2b.2 The Wightman Function#^thm-c2b-2-5|Theorem §C2b.2.5]], and the retarded function of the family is the causal commutator of [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-5|Theorem §C2b.5.5]].
> - [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-1|Theorem §CA.6.1]] (boundary values) and [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-4|Theorem §CA.6.4]] (the light-cone boundary value) are the position-space side of Theorem §C2b.7.4: $D_W$ and $D_F$ are boundary values of $\mathcal W$ from two sides, with singular parts $1/(-\xi^2 + i0\,\xi^0)$ and $1/(-\xi^2 + i0)$.
> - [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-6|Theorem §CA.6.6]] (the $i\varepsilon$ limits) is the momentum-space side: the Feynman denominator is the boundary value of the function rotated onto the Euclidean axis, and the second route of Theorem §C2b.7.5 is its Sokhotski–Plemelj split.
> - [[§CA.4 Contour Integration#^thm-ca-4-2|Theorem §CA.4.2]] and [[§CA.4 Contour Integration#^thm-ca-4-6|Theorem §CA.4.6]] (Cauchy's theorem, vanishing arcs) license the rotation of Theorem §C2b.7.1; [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^cau-ca-6-1|§CA.6, Caution: What the formula does and does not say]] is why the $i\varepsilon$ may then be dropped.
> - [[§CA.2 Generalized Functions#^thm-ca-2-1|Theorem §CA.2.1]] and [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-2|Theorem §CA.3.2]] (regular distributions, transforms in $\mathcal S'$) make $D_E$ a locally integrable function whose transform is $1/(p_E^2 + m^2)$, although the four-dimensional integral of Def. §C2b.7.1 converges only iteratively.
> - [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|Theorem §CA.3.7]] (relabelling) and [[§CA.2 Generalized Functions#^def-ca-2-10|Def. §CA.2.10]] (principal value) enter the advanced and principal entries of the family table.
> - Theorem §C2b.7.1 turns the one-loop correction to a scalar mass, $D_F$ at coincident points, into a positive integral over a four-ball, which exhibits its $\Lambda^2$ dependence on the cutoff ([[§R1.5★ Radiative Corrections, Naturalness and the Hierarchy Problem#^thm-r1-5-1|Thesis Thm. §R1.5.1]]).
