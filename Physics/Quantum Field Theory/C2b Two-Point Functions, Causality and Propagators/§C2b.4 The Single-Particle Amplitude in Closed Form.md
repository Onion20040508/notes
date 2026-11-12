---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C2b
section: C2b.4
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C2b.3 Explicit Forms of the Wightman Function]] · ↑ [[· C2b Two-Point Functions, Causality and Propagators]] · [[§C2b.5 Microcausality and the Commutator Function]] →

*Sources: the user's PHY 513 notes, Ch. 2 §2.2 (the closed form of the relativistic amplitude, both routes, and its checks), §2.4 (units) and Ch. 5 §5.4 · PHY 513 Lecture 2 (Larsen), Part A · Peskin & Schroeder §2.1, p. 14 · DLMF §10.17, §10.27.*

What are the exact values of the single-particle amplitude of [[§C1a.3 Causal Structure and the Causality of a Single Particle|§C1a.3]]? The amplitude $U$ of one relativistic particle ([[§C1a.3 Causal Structure and the Causality of a Single Particle#^def-c1a-3-1|Def. §C1a.3.1]]) is the same mode integral as $D_W$ with the weight $1/2E_{\mathbf p}$ replaced by $1$. [[§C1a.3 Causal Structure and the Causality of a Single Particle|§C1a.3]] showed with the lecture's saddle point that it leaks outside the light cone; with the Wightman function in hand, its exact values everywhere follow by one time derivative of the closed forms of [[§C2b.3 Explicit Forms of the Wightman Function|§C2b.3]]: $U$ is a time derivative of $D_W$ (Theorem §C2b.4.1), one analytic function in the lower half-plane (Theorem §C2b.4.2), and its boundary values outside and inside the light cone are Theorems §C2b.4.3 and §C2b.4.5. The causal object of the field theory, the commutator, follows in [[§C2b.5 Microcausality and the Commutator Function|§C2b.5]].

**Setup.** Theorems §C2b.4.1–§C2b.4.5 concern a different system from the rest of the chapter, one free particle in single-particle quantum mechanics with $\hat H = E(\hat{\mathbf P})$ and states of weight $1$ ([[§C1a.3 Causal Structure and the Causality of a Single Particle#^def-c1a-3-1|Def. §C1a.3.1]]; [[§C1a.3 Causal Structure and the Causality of a Single Particle#^mod-c1a-3-2|Model §C1a.3.2]]); its amplitude $U$ is a time derivative of $D_W$, the two-point function of the free real field ([[§C2a.1 Canonical Quantization of Fields#^mod-c2a-1-1|Model §C2a.1.1]]) in the free vacuum $|0\rangle$. Every evaluation is exact (asymptotic forms are marked); $m > 0$ unless stated, the massless case stated where it differs.

*Conventions* ([[Larsen PHY 513]]): $\hbar = c = 1$, $g = \operatorname{diag}(+, -, -, -)$, $E_{\mathbf p} = \sqrt{\mathbf p^2 + m^2}$, $r = |\mathbf x|$, $x^2 = t^2 - r^2$; $z$ is a complex time with $\operatorname{Im}z < 0$, and real times are reached as $z = t - i\varepsilon$, $\varepsilon \to 0^+$.

> [!theorem] Theorem §C2b.4.1: The Single-Particle Amplitude Is a Time Derivative of the Wightman Function
> With $U(z, \mathbf x)$ the analytic single-particle amplitude of [[§C1a.3 Causal Structure and the Causality of a Single Particle#^thm-c1a-3-5|Theorem §C1a.3.5]] and $W$ the analytic Wightman function of [[§C2b.2 The Wightman Function#^thm-c2b-2-5|Theorem §C2b.2.5]], for $\operatorname{Im}z < 0$,
>
> $$
> U(z, \mathbf x) = 2i\,\partial_zW(z, \mathbf x), \qquad U = 2i\,\partial_tD_W \quad\text{in } \mathcal S'(\mathbb R^4).
> $$
>
> *Model:* one free particle in single-particle quantum mechanics, $\hat H = E(\hat{\mathbf P})$ ([[§C1a.3 Causal Structure and the Causality of a Single Particle#^mod-c1a-3-2|Model §C1a.3.2]]), not a field; *applies:* exact, an identity of the analytic functions $U$ and $W$; $D_W$ is read as the free field's vacuum value in $|0\rangle$ ([[§C2a.1 Canonical Quantization of Fields#^mod-c2a-1-1|Model §C2a.1.1]]).
>
> *Source: derived here, from the user's PHY 513 notes, Ch. 2 §2.2 (Step 2 of Derivation "The relativistic amplitude in closed form": $U_E = -2\partial_\tau D_E$) and Ch. 5 §5.4*

^thm-c2b-4-1

> [!derivation]- Derivation
> **Step 1** (relation to $W$). $W(z, \mathbf x) = \int\frac{d^3p}{(2\pi)^3\,2E_{\mathbf p}}e^{-iE_{\mathbf p}z + i\mathbf p\cdot\mathbf x}$. Differentiating under the integral (allowed by Step 3 of [[§C2b.2 The Wightman Function#^der-c2b-2-5|Derivation §C2b.2.5]]): $\partial_z\frac{e^{-iE_{\mathbf p}z}}{2E_{\mathbf p}} = \frac{-iE_{\mathbf p}}{2E_{\mathbf p}}e^{-iE_{\mathbf p}z} = -\frac i2e^{-iE_{\mathbf p}z}$. So $\partial_zW = -\frac i2U$, i.e. $U = 2i\,\partial_zW$.
>
> **Step 2** (on $\mathbb R^4$). $U = \lim U(t - i\varepsilon, \mathbf x)$ in $\mathcal S'(\mathbb R^4)$ ([[§C1a.3 Causal Structure and the Causality of a Single Particle#^thm-c1a-3-5|Theorem §C1a.3.5]]). By [[§C2b.2 The Wightman Function#^thm-c2b-2-5|Theorem §C2b.2.5]], $D_W = \lim W(t - i\varepsilon, \mathbf x)$ in $\mathcal S'(\mathbb R^4)$, and the distributional derivative is continuous under such limits ([[§CA.2 Generalized Functions#^thm-ca-2-5|Theorem §CA.2.5]]): $\partial_tD_W = \lim\,(\partial_zW)(t - i\varepsilon, \cdot) = -\frac i2\lim U(t - i\varepsilon, \cdot) = -\frac i2U$.
>
> **What the derivation shows.**
> - $U$ and $D_W$ are the same mode integral with weights $1$ and $1/2E_{\mathbf p}$: the difference is the relativistic normalization of the states ([[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-1|Def. §C2a.4.1]]).
> - Every explicit form of $U$ is a time derivative of one in [[§C2b.3 Explicit Forms of the Wightman Function|§C2b.3]]; no new Bessel integral is needed. (The user's notes reach the same point through $U_E = -2\partial_\tau D_E$ at imaginary time, which is Step 1 at $z = -i\tau$.)
> - Used next: the closed forms (Theorems §C2b.4.2–§C2b.4.5) and the forward–backward decomposition ([[§C2b.5 Microcausality and the Commutator Function#^thm-c2b-5-7|Theorem §C2b.5.7]]).

^der-c2b-4-1

*Uses:* [[§C1a.3 Causal Structure and the Causality of a Single Particle#^thm-c1a-3-5|Theorem §C1a.3.5]], [[§C2b.2 The Wightman Function#^thm-c2b-2-5|Theorem §C2b.2.5]], [[§CA.2 Generalized Functions#^thm-ca-2-5|Theorem §CA.2.5]]

> [!theorem] Theorem §C2b.4.2: The Relativistic Amplitude in the Lower Half-Plane
> For $\operatorname{Im}z < 0$, with $r = |\mathbf x|$,
>
> $$
> U(z, \mathbf x) = \frac{i\,m^2\,z\,K_2(ms)}{2\pi^2s^2}, \qquad s = \sqrt{r^2 - z^2}\quad\text{(principal branch, }\operatorname{Re}s > 0\text{)},
> $$
>
> with $K_2$ of [[§CA.6 Gaussian Integrals, Stationary Phase and Bessel Functions#^def-ca-6-2|Def. §CA.6.2]] and $s$ as in [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-2|Theorem §C2b.3.2]], and $U = iz/\pi^2(r^2 - z^2)^2$ for $m = 0$. Every value of $U$ at real time is a boundary value of this one function: outside the light cone [[§C2b.4 The Single-Particle Amplitude in Closed Form#^thm-c2b-4-3|Theorem §C2b.4.3]], inside it [[§C2b.4 The Single-Particle Amplitude in Closed Form#^thm-c2b-4-5|Theorem §C2b.4.5]].
>
> *Model:* one free particle in single-particle quantum mechanics, $\hat H = E(\hat{\mathbf P})$ ([[§C1a.3 Causal Structure and the Causality of a Single Particle#^mod-c1a-3-2|Model §C1a.3.2]]), not a field; *applies:* exact, a statement about the analytic function $U$ of [[§C1a.3 Causal Structure and the Causality of a Single Particle#^thm-c1a-3-5|Theorem §C1a.3.5]]; $m = 0$ included; states of weight $1$ (not relativistically normalized).
>
> *Source: the user's PHY 513 notes, Ch. 2 §2.2 (Derivation "The relativistic amplitude in closed form", Step 5: the same function on the imaginary-time ray, $U_E(\tau, r) = \frac{m^2\tau}{2\pi^2R^2}K_2(mR)$, then "continue back") · stated here for the whole lower half-plane, as Theorem §C2b.3.2 is for $W$*

^thm-c2b-4-2

> [!derivation]- Derivation
> **Step 1** ($W$ in the lower half-plane). By [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-2|Theorem §C2b.3.2]], for $\operatorname{Im}z < 0$, $W(z, \mathbf x) = \frac{m}{4\pi^2}\,G(s)$ with $G(s) = \frac{K_1(ms)}{s}$ and $s = \sqrt{r^2 - z^2}$ (principal branch, $\operatorname{Re}s > 0$), an analytic function of $z$.
>
> **Step 2** (two derivatives). $\partial_zs = \frac{-2z}{2s} = -\frac zs$. With $w = ms$, $G = m\,w^{-1}K_1(w)$, and $\frac{d}{dw}\bigl[w^{-1}K_1(w)\bigr] = -w^{-1}K_2(w)$ ([[§CA.6 Gaussian Integrals, Stationary Phase and Bessel Functions#^thm-ca-6-4|Theorem §CA.6.4]], 1 with $\nu = 1$), so $\frac{dG}{ds} = m\cdot m\cdot\bigl(-w^{-1}K_2(w)\bigr) = -\frac{mK_2(ms)}{s}$.
>
> **Step 3** (the amplitude in the lower half-plane). By the chain rule and [[§C2b.4 The Single-Particle Amplitude in Closed Form#^thm-c2b-4-1|Theorem §C2b.4.1]],
>
> $$
> \partial_zW = \frac{m}{4\pi^2}\cdot\Bigl(-\frac{mK_2(ms)}{s}\Bigr)\cdot\Bigl(-\frac zs\Bigr) = \frac{m^2z\,K_2(ms)}{4\pi^2s^2}, \qquad U(z, \mathbf x) = 2i\,\partial_zW = \frac{i\,m^2z\,K_2(ms)}{2\pi^2s^2} .
> $$
>
> ⚑ By-product: this one analytic function of $z$ gives $U$ at every real point as a boundary value → the spacelike values, [[§C2b.4 The Single-Particle Amplitude in Closed Form#^thm-c2b-4-3|Theorem §C2b.4.3]]; the timelike values, [[§C2b.4 The Single-Particle Amplitude in Closed Form#^thm-c2b-4-5|Theorem §C2b.4.5]].
>
> **Step 4** ($m = 0$). Theorem §C2b.3.2 gives $W = \frac{1}{4\pi^2(r^2 - z^2)}$, so $\partial_zW = \frac{2z}{4\pi^2(r^2 - z^2)^2}$ and $U = 2i\,\partial_zW = \frac{iz}{\pi^2(r^2 - z^2)^2}$.
>
> **Step 5** (the imaginary-time ray). At $z = -i\tau$, $\tau > 0$: $s = \sqrt{r^2 + \tau^2} = R$ and $U(-i\tau, \mathbf x) = \frac{i\,m^2(-i\tau)K_2(mR)}{2\pi^2R^2} = \frac{m^2\tau}{2\pi^2R^2}K_2(mR)$, real and positive: the function $U_E$ of the user's notes.
>
> **What the derivation shows.**
> - No Bessel integral was evaluated here; the $K_1$ of Theorem §C2b.3.1 and one differentiation suffice.
> - $U$ has the structure of $W$: one analytic function of $s^2 = r^2 - z^2$ times the factor $z$, singular only at $s^2 = 0$ (the light cone) and across the cut $s^2 < 0$ (the timelike region).
> - Used next: the boundary values at real time (Theorems §C2b.4.3 and §C2b.4.5).

^der-c2b-4-2

*Uses:* [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-2|Theorem §C2b.3.2]], [[§C2b.4 The Single-Particle Amplitude in Closed Form#^thm-c2b-4-1|Theorem §C2b.4.1]], [[§CA.6 Gaussian Integrals, Stationary Phase and Bessel Functions#^thm-ca-6-4|Theorem §CA.6.4]], [[§CA.6 Gaussian Integrals, Stationary Phase and Bessel Functions#^def-ca-6-2|Def. §CA.6.2]]

> [!theorem] Theorem §C2b.4.3: The Relativistic Amplitude at Spacelike Separation
> For $r > |t|$, with $\rho = \sqrt{r^2 - t^2} = \sqrt{-x^2}$,
>
> $$
> U(t, \mathbf x) = \frac{i\,m^2\,t}{2\pi^2\rho^2}\,K_2(m\rho),
> $$
>
> a smooth function there ($K_2$: [[§CA.6 Gaussian Integrals, Stationary Phase and Bessel Functions#^def-ca-6-2|Def. §CA.6.2]]), purely imaginary and odd in $t$, depending on the point only through the invariant $\rho$ and the factor $t$. Equivalently (cut representation, absolutely convergent), $U = \frac{i}{2\pi^2r}\int_m^\infty d\varrho\,\varrho\,e^{-\varrho r}\sinh\bigl(t\sqrt{\varrho^2 - m^2}\bigr)$. For $m\rho \ll 1$, $U \simeq it/\pi^2\rho^4$; for $m = 0$ the formula $U = it/\pi^2(r^2 - t^2)^2$ is exact at every point off the light cone.
>
> *Model:* one free particle in single-particle quantum mechanics, $\hat H = E(\hat{\mathbf P})$ ([[§C1a.3 Causal Structure and the Causality of a Single Particle#^mod-c1a-3-2|Model §C1a.3.2]]), not a field; *applies:* exact; $m > 0$ for the $K_2$ form, $m = 0$ stated separately; states of weight $1$ (not relativistically normalized).
>
> *Source: the user's PHY 513 notes, Ch. 2 §2.2 (Derivations "The relativistic amplitude in closed form" and "The same result directly from the radial integral"; checks (i)–(ii)) · PHY 513 Lecture 2, Part A ("The exact radial integral: a Bessel function")*

^thm-c2b-4-3

> [!derivation]- Derivation
> **Step 1** (the spacelike limit). Put $z = t - i\varepsilon$ in [[§C2b.4 The Single-Particle Amplitude in Closed Form#^thm-c2b-4-2|Theorem §C2b.4.2]]: $s^2 = r^2 - t^2 + 2i\varepsilon t + \varepsilon^2 \to \rho^2 > 0$, away from the cut of $\sqrt{\ }$ and of $K_2$ (as in Steps 1–2 of [[§C2b.3 Explicit Forms of the Wightman Function#^der-c2b-3-3|Derivation §C2b.3.3]]). The function there is continuous at these $s^2$, so the limit is locally uniform on the open set $\{r > |t|\}$; integrated against a test function supported in that set it converges to the integral of the limit, so the distribution $U$ is this function there ([[§CA.2 Generalized Functions#^def-ca-2-6|Def. §CA.2.6]]; the same argument as Step 6 of [[§C2b.3 Explicit Forms of the Wightman Function#^der-c2b-3-2|Derivation §C2b.3.2]]). With $s \to \rho$, $z \to t$: the formula of the theorem.
>
> **Step 2** (imaginary and odd). $K_2(x) = \int_0^\infty e^{-x\cosh u}\cosh2u\,du > 0$ for $x > 0$ ([[§CA.6 Gaussian Integrals, Stationary Phase and Bessel Functions#^def-ca-6-2|Def. §CA.6.2]]), and $\rho$ is even in $t$; so $U/i$ is real with the sign of $t$.
>
> **Step 3** (short distance). $K_2(w) \simeq \frac12\Gamma(2)(2/w)^2 = 2/w^2$ for $w \to 0$ ([[§CA.6 Gaussian Integrals, Stationary Phase and Bessel Functions#^thm-ca-6-4|Theorem §CA.6.4]], 3), so $U \simeq \frac{im^2t}{2\pi^2\rho^2}\cdot\frac{2}{m^2\rho^2} = \frac{it}{\pi^2\rho^4}$.
>
> **Step 4** ($m = 0$). By Theorem §C2b.4.2, $U(z, \mathbf x) = \frac{iz}{\pi^2(r^2 - z^2)^2}$ in the lower half-plane. The boundary value at $z = t - i\varepsilon$ is $\frac{it}{\pi^2(r^2 - t^2)^2}$ at every point with $r \neq |t|$, inside the cone as well, since only $(r^2 - z^2)^2$ appears.
>
> ⚑ By-product: for $m = 0$ the leak outside the cone is a power law with no length scale at all; for $m > 0$ it is cut off at $\rho \sim 1/m$ → [[§C1a.3 Causal Structure and the Causality of a Single Particle#^thm-c1a-3-7|Theorem §C1a.3.7]].
>
> **What the derivation shows.**
> - Relativistic kinematics did not cure the leak: $K_2 > 0$, so $U \ne 0$ at every spacelike point with $t \neq 0$.
> - The spacelike values are the boundary value of the lower-half-plane function at positive $s^2$, where no cut is met: an ordinary smooth function.
> - A second, independent route below finds the same function without analytic continuation.

^der-c2b-4-3

*Uses:* [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-2|Theorem §C2b.3.2]], [[§C2b.4 The Single-Particle Amplitude in Closed Form#^thm-c2b-4-1|Theorem §C2b.4.1]], [[§CA.6 Gaussian Integrals, Stationary Phase and Bessel Functions#^thm-ca-6-4|Theorem §CA.6.4]], [[§CA.6 Gaussian Integrals, Stationary Phase and Bessel Functions#^def-ca-6-2|Def. §CA.6.2]], [[§C2b.4 The Single-Particle Amplitude in Closed Form#^thm-c2b-4-2|Theorem §C2b.4.2]], [[§CA.2 Generalized Functions#^def-ca-2-6|Def. §CA.2.6]]

> [!derivation]- Derivation (second route: around the branch cut, in real variables)
> This is the user's head-on computation of the lecture's integral; it shows where the spacelike condition enters. Take $r > |t|$ and keep $z = t - i\varepsilon$, $\varepsilon > 0$, until Step 5.
>
> **Step 1** (start). By [[§C1a.3 Causal Structure and the Causality of a Single Particle#^thm-c1a-3-6|Theorem §C1a.3.6]], $U(z, r) = \frac{1}{4\pi^2ir}\int_{-\infty}^\infty dp\;p\,e^{i(pr - zE_p)}$, absolutely convergent.
>
> **Step 2** (the branch). As a function of complex $p$, $E_p = \sqrt{p^2 + m^2}$ has branch points at $\pm im$; take the cuts along the imaginary axis from $im$ to $i\infty$ and from $-im$ to $-i\infty$, with the branch positive on the real axis. On the upper half-plane minus its cut $E_p$ is analytic, $E_p = p + O(1/p)$ for $\operatorname{Re}p > 0$ and $E_p = -p + O(1/p)$ for $\operatorname{Re}p < 0$ as $|p| \to \infty$. On the lips, $p = i\varrho \pm 0$ with $\varrho > m$: $E_p = +is$ just right of the cut and $-is$ just left, $s = \sqrt{\varrho^2 - m^2} > 0$ ([[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-3|Theorem §C2b.3.3]], second route, Step 5).
>
> **Step 3** (the arc vanishes exactly outside the cone). On $p = Le^{i\theta}$, $0 \le \theta \le \pi/2$: $i(pr - zE_p) = ip(r - t + i\varepsilon) + O(1/L)$, of real part $-L\bigl[(r - t)\sin\theta + \varepsilon\cos\theta\bigr] + O(1/L)$. For $\pi/2 \le \theta \le \pi$: $i(pr - zE_p) = ip(r + t - i\varepsilon) + O(1/L)$, of real part $-L\bigl[(r + t)\sin\theta + \varepsilon|\cos\theta|\bigr] + O(1/L)$. If $r > |t|$ both brackets are at least $c = \min(r - |t|, \varepsilon) > 0$ (since $\sin\theta + |\cos\theta| \ge 1$), so on the arc $|p\,e^{i(pr - zE_p)}| \le C\,L\,e^{-cL}$, and the arc integral is at most $\pi L\cdot CLe^{-cL} \to 0$ (ML, [[§CA.5 Contour Integration#^thm-ca-5-6|Theorem §CA.5.6]]). If $r < |t|$, one bracket is negative near $\theta = \pi/2$ and the arc grows: the contour cannot be closed.
>
> ⚑ By-product: the damping $\varepsilon > 0$ is needed on the arc near $\theta = 0$ and $\pi$, where $\sin\theta \to 0$; the factor $p$, which does not tend to zero, rules out Jordan's lemma without it ([[§CA.5 Contour Integration#^cau-ca-5-1|§CA.5, Caution: Jordan's lemma needs g → 0]]). The spacelike condition $r > |t|$ is exactly the condition for the arc to vanish.
>
> **Step 4** (the keyhole). Integrate counterclockwise around $[-L, L]$, the arc to $iL$, down the right lip to $im$, around a small circle at $im$, up the left lip to $iL$, and the arc to $-L$ ([[§CA.5 Contour Integration#^thm-ca-5-8|Theorem §CA.5.8]]; the contour of the figure in [[§CA.5 Contour Integration|§CA.5]]). The integrand is analytic inside, so the total is $0$ ([[§CA.5 Contour Integration#^thm-ca-5-2|Theorem §CA.5.2]]). The small circle contributes $O(\delta)$ (bounded integrand, length $2\pi\delta$), the arcs $\to 0$ by Step 3. On the lips $p = i\varrho$, $dp = i\,d\varrho$, $p = i\varrho$:
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
> ⚑ By-product: this is the cut representation stated in [[§C2b.4 The Single-Particle Amplitude in Closed Form#^thm-c2b-4-3|Theorem §C2b.4.3]]; in it $U$ is manifestly imaginary, odd in $t$, zero at $t = 0$ for $r > 0$ (as $U(0, \cdot) = \delta^3$ requires) and absolutely convergent; its exponent $-\varrho r + t\sqrt{\varrho^2 - m^2}$ is real, and its maximum is the saddle point → [[§C1a.3 Causal Structure and the Causality of a Single Particle#^thm-c1a-3-7|Theorem §C1a.3.7]], second route.
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
> **Step 8** (the Bessel function). $\sinh(2v + 2\chi) = \sinh2v\cosh2\chi + \cosh2v\sinh2\chi$. The first term is odd in $v$ and absolutely integrable: it gives $0$. The second gives $\sinh2\chi\int_{-\infty}^\infty\cosh2v\,e^{-m\rho\cosh v}dv = 2\sinh2\chi\,K_2(m\rho)$ ([[§CA.6 Gaussian Integrals, Stationary Phase and Bessel Functions#^def-ca-6-2|Def. §CA.6.2]], $\nu = 2$). With $\sinh2\chi = 2\sinh\chi\cosh\chi = 2tr/\rho^2$ the integral is $\frac{m^2}{4}\cdot2\cdot\frac{2tr}{\rho^2}K_2(m\rho) = \frac{m^2tr}{\rho^2}K_2(m\rho)$.
>
> **Step 9** (assemble). $U = \frac{i}{2\pi^2r}\cdot\frac{m^2tr}{\rho^2}K_2(m\rho) = \frac{i\,m^2t}{2\pi^2\rho^2}K_2(m\rho)$.
>
> **What the derivation shows.**
> - The two routes share no intermediate step, so their agreement is a check of both.
> - The rapidity $\chi$ makes visible that only the invariant $\rho$ and the boost-covariant factor $t$ appear.
> - The user's notes state the arc condition without the damping factor; with the factor $p$ in the integrand the damping is what makes the arc vanish (Step 3).
>
> *Source: the user's PHY 513 notes, Ch. 2 §2.2 (Derivation "The same result directly from the radial integral", Steps 1–3, and Fig. 2.2)*

*Uses:* [[§C1a.3 Causal Structure and the Causality of a Single Particle#^thm-c1a-3-6|Theorem §C1a.3.6]], [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-3|Theorem §C2b.3.3]], [[§CA.5 Contour Integration#^thm-ca-5-2|Theorem §CA.5.2]], [[§CA.5 Contour Integration#^thm-ca-5-6|Theorem §CA.5.6]], [[§CA.5 Contour Integration#^thm-ca-5-8|Theorem §CA.5.8]], [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|Theorem §CA.1.1]], [[§CA.6 Gaussian Integrals, Stationary Phase and Bessel Functions#^def-ca-6-2|Def. §CA.6.2]]

> [!theorem] Theorem §C2b.4.4: The Spacelike Amplitude at Large Distance
> For $r > |t|$ and $m\rho \gg 1$, $\rho = \sqrt{r^2 - t^2}$,
>
> $$
> U(t, \mathbf x) = \frac{i\,m^{3/2}\,t}{(2\pi\rho)^{3/2}\,\rho}\,e^{-m\rho}\Bigl(1 + \frac{15}{8m\rho} + O\bigl((m\rho)^{-2}\bigr)\Bigr) ,
> $$
>
> and $U \neq 0$ at every spacelike point with $t \neq 0$. The leading term is the saddle-point result of [[§C1a.3 Causal Structure and the Causality of a Single Particle#^thm-c1a-3-7|Theorem §C1a.3.7]].
>
> *Model:* one free particle in single-particle quantum mechanics, $\hat H = E(\hat{\mathbf P})$ ([[§C1a.3 Causal Structure and the Causality of a Single Particle#^mod-c1a-3-2|Model §C1a.3.2]]), not a field; *applies:* $m > 0$, asymptotic in $m\rho \gg 1$.
>
> *Source: the user's PHY 513 notes, Ch. 2 §2.2 (check (iii) of Derivation "The relativistic amplitude in closed form") · PHY 513 Lecture 2, Part A ("Quantum Causality is Violated") · PS §2.1, p. 14*

^thm-c2b-4-4

> [!derivation]- Derivation
> **Step 1** (the large-argument form). $K_2(w) = \sqrt{\pi/2w}\,e^{-w}\bigl[1 + \frac{4\cdot2^2 - 1}{8w} + \cdots\bigr] = \sqrt{\pi/2w}\,e^{-w}\bigl[1 + \frac{15}{8w} + \cdots\bigr]$ ([[§CA.6 Gaussian Integrals, Stationary Phase and Bessel Functions#^thm-ca-6-4|Theorem §CA.6.4]], 2 with $\nu = 2$).
>
> **Step 2** (insert). Into [[§C2b.4 The Single-Particle Amplitude in Closed Form#^thm-c2b-4-3|Theorem §C2b.4.3]] with $w = m\rho$:
>
> $$
> \frac{im^2t}{2\pi^2\rho^2}\sqrt{\frac{\pi}{2m\rho}} = \frac{i\,m^{3/2}\,t\,\sqrt\pi}{2^{3/2}\,\pi^2\,\rho^{5/2}} = \frac{i\,m^{3/2}\,t}{2^{3/2}\pi^{3/2}\rho^{5/2}} = \frac{i\,m^{3/2}\,t}{(2\pi\rho)^{3/2}\rho} .
> $$
>
> **Step 3** (nonzero). $K_2(m\rho) > 0$ (Step 2 of Derivation §C2b.4.3), so the asymptotic form only describes the size of a function that vanishes nowhere off $t = 0$.
>
> **What the derivation shows.**
> - Outside the cone the amplitude is small on the scale $1/m$ but not zero: single-particle relativistic quantum mechanics violates [[§C1a.3 Causal Structure and the Causality of a Single Particle#^pr-c1a-3-1|Principle §C1a.3.1]]. Relativistic kinematics was not the error; there is no algebra mistake to find.
> - The relative correction $15/8m\rho$ is the $\nu = 2$ case of the same series that gives $3/8mr$ for $D_W$ ([[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-3|Theorem §C2b.3.3]]).

^der-c2b-4-4

*Uses:* [[§C2b.4 The Single-Particle Amplitude in Closed Form#^thm-c2b-4-3|Theorem §C2b.4.3]], [[§CA.6 Gaussian Integrals, Stationary Phase and Bessel Functions#^thm-ca-6-4|Theorem §CA.6.4]]

> [!theorem] Theorem §C2b.4.5: The Relativistic Amplitude at Timelike Separation
> For $|t| > r$, with $\tau = \sqrt{t^2 - r^2}$,
>
> $$
> U(t, \mathbf x) = \frac{m^2\,t}{4\pi\tau^2}\,H^{(2)}_2(m\tau)\quad (t > 0), \qquad U(-t, \mathbf x) = \overline{U(t, \mathbf x)} ,
> $$
>
> an oscillating function ($H^{(2)}_2$: [[§CA.6 Gaussian Integrals, Stationary Phase and Bessel Functions#^def-ca-6-2|Def. §CA.6.2]]; imaginary argument: [[§CA.6 Gaussian Integrals, Stationary Phase and Bessel Functions#^thm-ca-6-5|Theorem §CA.6.5]], 3), $U \simeq \frac{m^{3/2}t}{(2\pi\tau)^{3/2}\tau}\,e^{-i(m\tau - 5\pi/4)}$ for $t > 0$, $m\tau \gg 1$. On the light cone $U$ is singular and is defined only as the boundary value of [[§C1a.3 Causal Structure and the Causality of a Single Particle#^thm-c1a-3-5|Theorem §C1a.3.5]].
>
> *Model:* one free particle in single-particle quantum mechanics, $\hat H = E(\hat{\mathbf P})$ ([[§C1a.3 Causal Structure and the Causality of a Single Particle#^mod-c1a-3-2|Model §C1a.3.2]]), not a field; *applies:* exact, $m > 0$; the asymptotic form for $m\tau \gg 1$.
>
> *Source: the user's PHY 513 notes, Ch. 2 §2.2 (check (iv) of Derivation "The relativistic amplitude in closed form"; connection formula from DLMF §10.27, checked numerically there) · DLMF §10.17 (Hankel asymptotics)*

^thm-c2b-4-5

> [!derivation]- Derivation
> **Step 1** (the limit of $s$). In [[§C2b.4 The Single-Particle Amplitude in Closed Form#^thm-c2b-4-2|Theorem §C2b.4.2]] put $z = t - i\varepsilon$ with $t > r$: $s^2 = r^2 - t^2 + 2i\varepsilon t + \varepsilon^2 \to -\tau^2 + i0$, and the principal root of $-\tau^2 + i0$ is $+i\tau$ ([[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-4|Theorem §C2b.3.4]], Step 1). The limit is locally uniform in the open timelike region, so it is the restriction of the distribution $U$ there, as in Step 1 of Derivation §C2b.4.3.
>
> **Step 2** ($t > 0$). With $s = i\tau$, $s^2 = -\tau^2$:
>
> $$
> U = \frac{i\,m^2t\,K_2(im\tau)}{2\pi^2(-\tau^2)} = -\frac{i\,m^2t}{2\pi^2\tau^2}K_2(im\tau) .
> $$
>
> The connection formula $K_\nu(ix) = \frac\pi2(-i)^{\nu+1}H^{(2)}_\nu(x)$ for $x > 0$ ([[§CA.6 Gaussian Integrals, Stationary Phase and Bessel Functions#^thm-ca-6-5|Theorem §CA.6.5]], 3) with $\nu = 2$ and $(-i)^3 = i$ gives $K_2(im\tau) = \frac{i\pi}{2}H^{(2)}_2(m\tau)$, so $U = -\frac{im^2t}{2\pi^2\tau^2}\cdot\frac{i\pi}{2}H^{(2)}_2 = \frac{m^2t}{4\pi\tau^2}H^{(2)}_2(m\tau)$.
>
> **Step 3** ($t < 0$). By [[§C1a.3 Causal Structure and the Causality of a Single Particle#^thm-c1a-3-3|Theorem §C1a.3.3]], $\overline{U(t, \mathbf x)} = \int\frac{d^3p}{(2\pi)^3}e^{+iE_{\mathbf p}t - i\mathbf p\cdot\mathbf x} = U(-t, -\mathbf x)$ (complex conjugation of the transform of $e^{-iE_{\mathbf p}t}$, an identity in $\mathcal S'$). $E_{\mathbf p}$ is even in $\mathbf p$, so $U(-t, \cdot)$ is even in $\mathbf x$ (substitute $\mathbf p \to -\mathbf p$, Jacobian $1$: [[§CA.4 Fourier Transforms and Fourier Tricks#^thm-ca-4-6|Theorem §CA.4.6]], 1), and $U(-t, -\mathbf x) = U(-t, \mathbf x)$.
>
> **Step 4** (late proper times). $H^{(2)}_2(x) \simeq \sqrt{2/\pi x}\,e^{-i(x - 5\pi/4)}$ for $x \to \infty$ (DLMF §10.17), so $|U| \simeq \frac{m^2t}{4\pi\tau^2}\sqrt{\frac{2}{\pi m\tau}} = \frac{\sqrt2\,m^{3/2}t}{4\pi^{3/2}\tau^{5/2}} = \frac{m^{3/2}t}{(2\pi\tau)^{3/2}\tau}$, using $\sqrt2/4 = 2^{-3/2}$.
>
> **Step 5** (the cone). The function of Theorem §C2b.4.2 blows up as $s \to 0$: by Step 3 of Derivation §C2b.4.3, $U \simeq iz/\pi^2(r^2 - z^2)^2$ near the cone, a double pole in $r^2 - z^2$. At real $t$ it has no value on the cone and exists there only as the limit in $\mathcal S'$ of [[§C1a.3 Causal Structure and the Causality of a Single Particle#^thm-c1a-3-5|Theorem §C1a.3.5]]; by [[§C2b.4 The Single-Particle Amplitude in Closed Form#^thm-c2b-4-1|Theorem §C2b.4.1]] its singular part is $2i\partial_t$ of the light-cone singularity of $D_W$ ([[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-6|Theorem §C2b.3.6]], 2).
>
> **What the derivation shows.**
> - Inside and outside the cone are the two sides of the cut of one analytic function: $K_2$ decay outside becomes Hankel oscillation inside, as $K_1$ does for $D_W$ ([[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-4|Theorem §C2b.3.4]]).
> - The moduli inside and outside have the same form, $m^{3/2}|t|\,\sigma^{-5/2}(2\pi)^{-3/2}$ with $\sigma = \tau$ or $\rho$; only the exponential differs, a phase inside and a damping outside.

^der-c2b-4-5

*Uses:* [[§C2b.4 The Single-Particle Amplitude in Closed Form#^thm-c2b-4-3|Theorem §C2b.4.3]], [[§C2b.4 The Single-Particle Amplitude in Closed Form#^thm-c2b-4-2|Theorem §C2b.4.2]], [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-4|Theorem §C2b.3.4]], [[§CA.6 Gaussian Integrals, Stationary Phase and Bessel Functions#^thm-ca-6-5|Theorem §CA.6.5]], [[§C1a.3 Causal Structure and the Causality of a Single Particle#^thm-c1a-3-3|Theorem §C1a.3.3]], [[§CA.4 Fourier Transforms and Fourier Tricks#^thm-ca-4-6|Theorem §CA.4.6]], [[§C1a.3 Causal Structure and the Causality of a Single Particle#^thm-c1a-3-5|Theorem §C1a.3.5]], [[§C2b.4 The Single-Particle Amplitude in Closed Form#^thm-c2b-4-1|Theorem §C2b.4.1]], [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-6|Theorem §C2b.3.6]]

![[ph-qft-c1-3-1.svg]]
*The single-particle amplitude at fixed $mt = 3$ (units $m = 1$): inside the cone (shaded) the Hankel form of Theorem §C2b.4.5, outside the $K_2$ form of Theorem §C2b.4.3 with its leading asymptotic term (dashed, Theorem §C2b.4.4; Theorem §C1a.3.7). It is singular on the cone and leaks outside it over the Compton wavelength $1/m$. Adapted from the user's PHY 513 notes, Fig. 2.3; recomputed from the closed forms, which were checked against the mode integral at complex $t$.*

> [!example] Example §C2b.4.1: Units Restored in the Single-Particle Amplitude
> Restore $\hbar$ and $c$ in $U = \frac{im^2t}{2\pi^2\rho^2}K_2(m\rho)$ and in the nonrelativistic prefactor $(m/2\pi it)^{3/2}$, and read off the range of the leak for an electron.
>
> **Step 1** (target). $U(t, \cdot) \to \delta^3$ ([[§C1a.3 Causal Structure and the Causality of a Single Particle#^thm-c1a-3-3|Theorem §C1a.3.3]]), so $U$ has dimension $L^{-3}$, mass dimension $3$ ([[§C1a.2 Natural Units and Dimensional Analysis#^thm-c1a-2-3|Theorem §C1a.2.3]], 4).
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

^ex-c2b-4-1

> [!abstract]- Mathematical background
> Proved in CA; each line says what the physics above relies on.
>
> - [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|Theorem §CA.1.1]] — dominated convergence: the damping $\varepsilon$ is removed under the integral of the cut representation (second route of Theorem §C2b.4.3, Step 5).
> - [[§CA.2 Generalized Functions#^def-ca-2-6|Def. §CA.2.6]] (support and singular support) states where $U$ is a function: everywhere except the light cone.
> - [[§CA.2 Generalized Functions#^thm-ca-2-5|Theorem §CA.2.5]] — derivatives commute with distributional limits: $U = 2i\,\partial_tD_W$ as a boundary value (Theorem §C2b.4.1).
> - [[§CA.4 Fourier Transforms and Fourier Tricks#^thm-ca-4-6|Theorem §CA.4.6]], 1 — relabelling $\mathbf p \to -\mathbf p$ with Jacobian $1$: $U(-t, \cdot)$ is even in $\mathbf x$ (Theorem §C2b.4.5).
> - [[§CA.5 Contour Integration#^thm-ca-5-2|Theorem §CA.5.2]] — Cauchy's theorem for the keyhole contour of the second route.
> - [[§CA.5 Contour Integration#^thm-ca-5-6|Theorem §CA.5.6]], [[§CA.5 Contour Integration#^cau-ca-5-1|§CA.5, Caution: Jordan's lemma needs g → 0]] — closing the contour: with the factor $p$ in the integrand the arcs vanish only with the damping $\varepsilon$, and only outside the light cone.
> - [[§CA.5 Contour Integration#^thm-ca-5-8|Theorem §CA.5.8]] — integrals around a branch cut: the two lips of the cut from $im$ (second route).
> - [[§CA.6 Gaussian Integrals, Stationary Phase and Bessel Functions#^def-ca-6-2|Def. §CA.6.2]] — $K_\nu$ by its integral representation, with $H^{(2)}_\nu$: the functions of every closed form here.
> - [[§CA.6 Gaussian Integrals, Stationary Phase and Bessel Functions#^thm-ca-6-4|Theorem §CA.6.4]] — properties of $K_\nu$: the derivative identity that turns $K_1$ into $K_2$, and the small- and large-argument forms ($2/w^2$; $e^{-m\rho}$ with the correction $15/8m\rho$).
> - [[§CA.6 Gaussian Integrals, Stationary Phase and Bessel Functions#^thm-ca-6-5|Theorem §CA.6.5]], 3 — $K_\nu(ix)$ in terms of $H^{(2)}_\nu$: the timelike form.

> [!remark]- Connections
> - The exact amplitude confirms the lecture's saddle point: its leading term at large distance is the estimate found there, and the leak outside the light cone is real, a violation of the causality principle by single-particle relativistic quantum mechanics — [[§C1a.3 Causal Structure and the Causality of a Single Particle#^thm-c1a-3-7|Theorem §C1a.3.7]], [[§C1a.3 Causal Structure and the Causality of a Single Particle#^pr-c1a-3-1|Principle §C1a.3.1]].
> - $U$ and $D_W$ are one mode integral with the weights $1$ and $1/2E_{\mathbf p}$; in the field theory the average of forward and backward propagation is causal, and the leak is the time derivative of the vacuum correlation $D_1$ — [[§C2b.5 Microcausality and the Commutator Function#^thm-c2b-5-7|Theorem §C2b.5.7]], [[§C2b.5 Microcausality and the Commutator Function#^thm-c2b-5-5|Theorem §C2b.5.5]].
> - Restoring $\hbar$ and $c$ in $U$ is a worked instance of the procedure, and the nonrelativistic prefactor is the free propagator of quantum mechanics — [[P4 Restoring ħ and c|P4]], [[§C4.1 Propagators#^thm-c4-1-4|QM Theorem §C4.1.4]].
