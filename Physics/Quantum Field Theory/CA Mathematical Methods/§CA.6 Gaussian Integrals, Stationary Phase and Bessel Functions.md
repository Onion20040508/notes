---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: CA
section: CA.6
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§CA.5 Contour Integration]] · ↑ [[· CA Mathematical Methods]] · [[§CA.7 Boundary Values, iε Limits and Fundamental Solutions]] →

*Sources: the user's PHY 513 notes, App. A §§A.6–A.8 and the saddle-point computation of Ch. 2 §2.2 · DLMF §§10.25–10.40 and Abramowitz & Stegun §9.6–9.7 (cited in the user's notes).*

The two-point functions of the free field are Gaussian integrals in disguise, evaluated at a saddle or summed into a modified Bessel function $K_\nu$. The Gaussian integral with complex $a$ and $b$ is proved here ([[§CA.6 Gaussian Integrals, Stationary Phase and Bessel Functions#^thm-ca-6-1|Theorem §CA.6.1]]; the same result, with the Fresnel limit, is [[§C4.1 Propagators#^thm-c4-1-3|QM Theorem §C4.1.3]]). Two tools have their homes elsewhere and are only recalled, as pointers on which no proof of this section rests: the stationary-phase formula ([[§C4.2 The Feynman Path Integral#^thm-c4-2-5|QM Theorem §C4.2.5]]) and Stirling's formula, in which Laplace's method appears inline ([[§B4.1 Probability Distributions and the Gaussian#^thm-b4-1-5|TH Theorem §B4.1.5]]). New here: the Gamma function ([[§CA.6 Gaussian Integrals, Stationary Phase and Bessel Functions#^def-ca-6-1|Def. §CA.6.1]]), the $n$-dimensional Gaussian Fourier transform with Schwinger's parametrization, steepest descent through a *complex* saddle and why it fixes the exponential factor, and the function $K_\nu$ with everything the course uses derived from one integral representation. The single evaluation of a two-point function in terms of $K_1$ is [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-1|Theorem §C2b.3.1]]; this section supplies its tools.

## Gaussian integrals

The one-dimensional Gaussian integral with complex $a$ and $b$ comes first: every later integral of this section is reduced to it. It is proved from the real Gaussian integral of the Math vault and Cauchy's theorem, so that this chapter rests on no physics note. [[§C4.1 Propagators#^thm-c4-1-3|QM Theorem §C4.1.3]] states the same formula, for $\operatorname{Re}a > 0$ and complex $b$, extended there by the identity theorem from real $a$, and adds the Fresnel limit $\operatorname{Re}a \to 0^+$ on the imaginary axis; the home of the Fresnel limit and of the propagator that uses it stays there.

> [!theorem] Theorem §CA.6.1: The Gaussian Integral with Complex a and b
> For complex $a$ with $\operatorname{Re}a > 0$ and complex $b$,
>
> $$
> \int_{-\infty}^{\infty}d\xi\,e^{-a\xi^2 + b\xi} = \sqrt{\frac\pi a}\,e^{b^2/4a} ,
> $$
>
> with the principal root $\sqrt a$ (the one with positive real part). In particular $\int_{-\infty}^{\infty}d\xi\,e^{-a\xi^2} = \sqrt{\pi/a}$ for real $a > 0$.
>
> *Source: the user's PHY 513 notes, App. A §A.6 · proved here from [[§25 Change of Variables on General Domains#^ex-25-4|452 Example §25.4]] and Cauchy's theorem · the same result: [[§C4.1 Propagators#^thm-c4-1-3|QM Theorem §C4.1.3]]*

^thm-ca-6-1

> [!derivation]- Derivation
> **Step 1** (real $a > 0$, $b = 0$). $\int_{-\infty}^{\infty}e^{-x^2}dx = \sqrt\pi$ ([[§25 Change of Variables on General Domains#^ex-25-4|452 Example §25.4]]); the substitution $x = \sqrt a\,\xi$, $dx = \sqrt a\,d\xi$, gives $\int_{-\infty}^{\infty}e^{-a\xi^2}d\xi = \sqrt{\pi/a}$.
>
> **Step 2** (real $a > 0$, complex $b$). Complete the square with $c = b/2a$: $-a\xi^2 + b\xi = -a(\xi - c)^2 + b^2/4a$ (expand: $-a\xi^2 + 2ac\xi - ac^2 + b^2/4a$, and $ac^2 = b^2/4a$). So $\int_{-R}^{R}e^{-a\xi^2 + b\xi}d\xi = e^{b^2/4a}\int_{-R - c}^{R - c}e^{-a\zeta^2}d\zeta$ with $\zeta = \xi - c$, the integral taken along the horizontal segment from $-R - c$ to $R - c$. The function $e^{-a\zeta^2}$ is analytic in the whole plane, so by Cauchy's theorem ([[§CA.5 Contour Integration#^thm-ca-5-2|Theorem §CA.5.2]]) on the parallelogram with vertices $-R$, $R$, $R - c$, $-R - c$,
>
> $$
> \int_{-R - c}^{R - c}e^{-a\zeta^2}d\zeta = \int_{-R}^{R}e^{-a\zeta^2}d\zeta + \int_{R}^{R - c}e^{-a\zeta^2}d\zeta - \int_{-R}^{-R - c}e^{-a\zeta^2}d\zeta .
> $$
>
> On the two sides $\zeta = \pm R - \sigma c$, $0 \le \sigma \le 1$, and $\operatorname{Re}\zeta^2 = (\pm R - \sigma\operatorname{Re}c)^2 - \sigma^2(\operatorname{Im}c)^2 \ge (R - |c|)^2 - |c|^2$ for $R > |c|$, so $|e^{-a\zeta^2}| \le e^{-a(R - |c|)^2 + a|c|^2}$ and each side, of length $|c|$, contributes at most $|c|\,e^{-a(R - |c|)^2 + a|c|^2} \to 0$ (ML, [[§CA.5 Contour Integration#^thm-ca-5-1|Theorem §CA.5.1]]). As $R \to \infty$: $\int_{-\infty}^{\infty}e^{-a\xi^2 + b\xi}d\xi = e^{b^2/4a}\sqrt{\pi/a}$ by Step 1.
>
> **Step 3** (complex $a$, $\operatorname{Re}a > 0$). Write $a = |a|e^{i\theta}$ with $|\theta| < \frac\pi2$, and rotate the path: on the ray $\xi = \rho e^{-i\theta/2}$ the exponent $a\xi^2 = |a|\rho^2$ is real. The integrand is analytic in the whole plane, so by Cauchy's theorem the integral over $[-R, R]$ equals the integral over the rotated segment from $-Re^{-i\theta/2}$ to $Re^{-i\theta/2}$ plus the two arcs $\xi = \pm Re^{i\varphi}$ that join their ends, with $\varphi$ between $0$ and $-\theta/2$. On the arcs $\operatorname{Re}(a\xi^2) = |a|R^2\cos(\theta + 2\varphi) \ge |a|R^2\cos\theta$, because $\theta + 2\varphi$ lies between $\theta$ and $0$; so the integrand is at most $e^{-|a|R^2\cos\theta + |b|R}$ and each arc, of length at most $\frac\pi4R$, tends to $0$ (ML). On the rotated line put $\xi = e^{-i\theta/2}x$, $d\xi = e^{-i\theta/2}dx$, $x$ real:
>
> $$
> \int_{-\infty}^{\infty}d\xi\,e^{-a\xi^2 + b\xi} = e^{-i\theta/2}\int_{-\infty}^{\infty}dx\,e^{-|a|x^2 + be^{-i\theta/2}x} = e^{-i\theta/2}\sqrt{\frac{\pi}{|a|}}\,\exp\frac{b^2e^{-i\theta}}{4|a|} = \sqrt{\frac\pi a}\,e^{b^2/4a} ,
> $$
>
> by Step 2 with $|a|$ and $be^{-i\theta/2}$ in place of $a$ and $b$; $\sqrt a = \sqrt{|a|}\,e^{i\theta/2}$ is the principal root and $e^{-i\theta}/|a| = 1/a$. This is the statement of [[§C4.1 Propagators#^thm-c4-1-3|QM Theorem §C4.1.3]], proved there by analytic continuation in $a$.
>
> **What the derivation shows.**
> - Three moves: the real integral, a shift of the contour (completing the square), a rotation of the contour; each contour move is Cauchy's theorem with an ML estimate of the pieces at infinity.
> - Assumption used: $\operatorname{Re}a > 0$, which makes the integral converge absolutely and the arcs vanish. On the boundary $\operatorname{Re}a = 0$ the integral converges only conditionally (the Fresnel limit, [[§C4.1 Propagators#^thm-c4-1-3|QM Theorem §C4.1.3]]).
> - Used next: the $n$-dimensional Gaussian and Schwinger's parametrization (Theorem §CA.6.2), the Gaussian step of Laplace's method (Theorem §CA.6.3), and, in advance, Fourier inversion ([[§CA.4 Fourier Transforms and Fourier Tricks#^thm-ca-4-1|Theorem §CA.4.1]]).

^der-ca-6-1

*Uses:* [[§25 Change of Variables on General Domains#^ex-25-4|452 Example §25.4]], [[§CA.5 Contour Integration#^thm-ca-5-2|Theorem §CA.5.2]], [[§CA.5 Contour Integration#^thm-ca-5-1|Theorem §CA.5.1]]

> [!definition] Definition §CA.6.1: The Gamma Function
> For $\nu > 0$ the **Gamma function** is
>
> $$
> \Gamma(\nu) \equiv \int_0^\infty du\,u^{\nu - 1}e^{-u} ,
> $$
>
> an integral that converges at $u = 0$ because $\nu > 0$ and at infinity because of $e^{-u}$. Values used: $\Gamma(1) = 1$; $\Gamma(\nu + 1) = \nu\,\Gamma(\nu)$ (integrate by parts: $\int_0^\infty u^\nu e^{-u}du = [-u^\nu e^{-u}]_0^\infty + \nu\int_0^\infty u^{\nu - 1}e^{-u}du$), hence $\Gamma(n + 1) = n!$; and $\Gamma(\tfrac12) = \sqrt\pi$ (substitute $u = x^2$: $\Gamma(\tfrac12) = 2\int_0^\infty e^{-x^2}dx$, [[§CA.6 Gaussian Integrals, Stationary Phase and Bessel Functions#^thm-ca-6-1|Theorem §CA.6.1]]).
>
> *Source: the user's PHY 513 notes, App. A §A.6 (Schwinger parametrization), §A.8 (small argument of $K_\nu$) · the same definition: [[§B4.1 Probability Distributions and the Gaussian#^def-b4-1-5|TH Def. §B4.1.5]]*

^def-ca-6-1

> [!theorem] Theorem §CA.6.2: Gaussian Integrals in n Dimensions; Schwinger Parametrization
> 1. For $\operatorname{Re}s > 0$ and $\mathbf x \in \mathbb R^n$,
>
> $$
> \int\frac{d^np}{(2\pi)^n}\,e^{-s\mathbf p^2 + i\mathbf p\cdot\mathbf x} = \frac{1}{(4\pi s)^{n/2}}\,e^{-\mathbf x^2/4s} .
> $$
>
> 2. For $\operatorname{Re}A > 0$ and $\nu > 0$, $\dfrac1A = \displaystyle\int_0^\infty ds\,e^{-sA}$ and $\dfrac{1}{A^\nu} = \dfrac{1}{\Gamma(\nu)}\displaystyle\int_0^\infty ds\,s^{\nu - 1}e^{-sA}$, with the Gamma function $\Gamma(\nu)$ of [[§CA.6 Gaussian Integrals, Stationary Phase and Bessel Functions#^def-ca-6-1|Def. §CA.6.1]].
>
> *Source: the user's PHY 513 notes, App. A §A.6 (eq. (gaussianN)), Ch. 2 §2.2 (Step 3 of Derivation "The relativistic amplitude in closed form")*

^thm-ca-6-2

> [!derivation]- Derivation
> **Step 1** (factorize). $\mathbf p^2 = \sum_kp_k^2$ and $\mathbf p\cdot\mathbf x = \sum_kp_kx_k$, so the integrand is a product of $n$ one-dimensional integrands and the integral is the product $\prod_{k=1}^n\int\frac{dp_k}{2\pi}e^{-sp_k^2 + ip_kx_k}$ (absolutely convergent since $\operatorname{Re}s > 0$).
>
> **Step 2** (one factor). By [[§CA.6 Gaussian Integrals, Stationary Phase and Bessel Functions#^thm-ca-6-1|Theorem §CA.6.1]] with $a = s$, $b = ix_k$: $\int\frac{dp_k}{2\pi}e^{-sp_k^2 + ip_kx_k} = \frac{1}{2\pi}\sqrt{\frac\pi s}\,e^{(ix_k)^2/4s} = \frac{1}{\sqrt{4\pi s}}\,e^{-x_k^2/4s}$.
>
> **Step 3** (multiply). $\prod_k(4\pi s)^{-1/2}e^{-x_k^2/4s} = (4\pi s)^{-n/2}e^{-\mathbf x^2/4s}$.
>
> **Step 4** (part 2, $\nu = 1$). $\int_0^\infty e^{-sA}ds = \bigl[-e^{-sA}/A\bigr]_0^\infty = 1/A$; the boundary term at $\infty$ vanishes because $|e^{-sA}| = e^{-s\operatorname{Re}A}$.
>
> **Step 5** (part 2, general $\nu$). For real $A > 0$ substitute $u = sA$, $ds = du/A$: $\int_0^\infty s^{\nu-1}e^{-sA}ds = A^{-\nu}\int_0^\infty u^{\nu-1}e^{-u}du = \Gamma(\nu)A^{-\nu}$ ([[§CA.6 Gaussian Integrals, Stationary Phase and Bessel Functions#^def-ca-6-1|Def. §CA.6.1]]). Both sides are analytic in $A$ on $\operatorname{Re}A > 0$ (principal branch of $A^{-\nu}$), so they agree there ([[§CA.5 Contour Integration#^thm-ca-5-3|Theorem §CA.5.3]]).
>
> **What the derivation shows.**
> - With $s$ read as a proper time, $e^{-s\mathbf p^2}$ is a heat kernel; Schwinger's trick trades a denominator that couples the components for an exponential that factorizes → [[§CA.6 Gaussian Integrals, Stationary Phase and Bessel Functions#^rem-ca-6-1|Remark: Why the parametrization helps]].
> - Used in: the Euclidean evaluation of the Wightman function ([[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-1|Theorem §C2b.3.1]], Steps 3–4), with $n = 1$ and $n = 3$; the nonrelativistic single-particle amplitude ([[§C1a.3 Causal Structure and the Causality of a Single Particle#^thm-c1a-3-4|Theorem §C1a.3.4]]).

^der-ca-6-2

*Uses:* [[§CA.6 Gaussian Integrals, Stationary Phase and Bessel Functions#^thm-ca-6-1|Theorem §CA.6.1]], [[§CA.6 Gaussian Integrals, Stationary Phase and Bessel Functions#^def-ca-6-1|Def. §CA.6.1]], [[§CA.5 Contour Integration#^thm-ca-5-3|Theorem §CA.5.3]]

> [!remark] Remark: Why the parametrization helps
> Schwinger's trick trades a denominator, which couples the components of $\mathbf p$ through $\mathbf p^2 + m^2$, for an exponential, which factorizes. Every momentum integral then becomes a product of one-dimensional Gaussians, and the remaining single integral over $s$ is where the special function appears: for the Euclidean propagator it is $\int ds\,s^{-2}e^{-sm^2 - R^2/4s}$, a $K_1$ ([[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-1|Theorem §C2b.3.1]]). With $s$ read as a proper time, $e^{-s\mathbf p^2}$ is a heat kernel, the Euclidean version of the free propagator of [[§C4.1 Propagators#^thm-c4-1-4|QM Theorem §C4.1.4]]; loop integrals (the second semester, planned: PHY 513 Lecture 17, slide 26) are done the same way.
>
> *Source: the user's PHY 513 notes, Ch. 2 §2.2, App. A §A.6*

^rem-ca-6-1

## Saddle points

*Recall* ([[§C4.2 The Feynman Path Integral#^thm-c4-2-5|QM Theorem §C4.2.5]]): if a large phase $S = \lambda\sigma$ has a single nondegenerate real stationary point $p_0$, then $\int f\,e^{iS}\,dp \simeq f(p_0)\,e^{iS(p_0)}\sqrt{2\pi/|S''(p_0)|}\;e^{i\frac\pi4\operatorname{sgn}S''(p_0)}$, and regions without a stationary point contribute less than any power of $1/\lambda$. The user's notes derive it the same way (integration by parts away from $p_0$, the Fresnel integral near it); the home stays in QM.

> [!theorem] Theorem §CA.6.3: Steepest Descent and Laplace's Method
> Let $I(\lambda) = \int f(p)\,e^{\lambda\Phi(p)}\,dp$ with $\lambda \gg 1$ and $f$, $\Phi$ independent of $\lambda$.
> 1. *(Laplace)* If $\Phi$ is real with a single nondegenerate interior maximum at $p_0$, then $I \simeq f(p_0)\,e^{\lambda\Phi(p_0)}\sqrt{2\pi/\lambda|\Phi''(p_0)|}$.
> 2. *(Steepest descent)* If $f$ and $\Phi$ are analytic and the contour can be deformed, without crossing a singularity and with negligible ends, through a complex saddle $\Phi'(p_0) = 0$, then $I \simeq f(p_0)\,e^{\lambda\Phi(p_0)}\,e^{i\theta}\sqrt{2\pi/\lambda|\Phi''(p_0)|}$, where $\theta$ is the direction with $\Phi''(p_0)e^{2i\theta} < 0$.
>
> In both cases $|I| \propto e^{\lambda\operatorname{Re}\Phi(p_0)}$: for $\Phi = iS$ with no real stationary point, $I$ is exponentially small, $|I| \propto e^{-\operatorname{Im}S(p_0)}$; the saddle alone fixes the exponent, and everything else changes only the prefactor, by relative corrections $O(1/\lambda)$.
>
> *Source: the user's PHY 513 notes, App. A §A.7 (Principle "Stationary phase and steepest descent", Derivation, Step 3)*

^thm-ca-6-3

> [!derivation]- Derivation
> **Step 1** (Laplace: localize). Near $p_0$, $\Phi(p) = \Phi(p_0) - \frac12|\Phi''(p_0)|(p - p_0)^2 + O((p - p_0)^3)$. Outside $|p - p_0| < \delta$ the integrand is smaller than at $p_0$ by a factor $e^{-c\lambda}$ for some $c > 0$, so only a neighbourhood contributes.
>
> **Step 2** (Laplace: the Gaussian). In the neighbourhood, with $u = p - p_0$, the width that contributes is $u \sim \lambda^{-1/2}$; replace $f$ by $f(p_0)$ (error $O(\lambda^{-1/2})$ relative, $O(\lambda^{-1})$ after the odd term integrates to zero) and drop the cubic term (relative $O(\lambda^{-1})$ likewise), and extend the Gaussian to the whole line (exponentially small error):
>
> $$
> I \simeq f(p_0)\,e^{\lambda\Phi(p_0)}\int_{-\infty}^{\infty}du\,e^{-\frac12\lambda|\Phi''(p_0)|u^2} = f(p_0)\,e^{\lambda\Phi(p_0)}\sqrt{\frac{2\pi}{\lambda|\Phi''(p_0)|}},
> $$
>
> by the real Gaussian integral ([[§CA.6 Gaussian Integrals, Stationary Phase and Bessel Functions#^thm-ca-6-1|Theorem §CA.6.1]]) with $a = \frac12\lambda|\Phi''|$. (The orders of the errors in this step are stated, not proved.)
> <!-- S6 (2026-11-12): searched ~/Notes/Math and ~/Notes/Applied Math for "Laplace's method", "Watson", "steepest descent", "asymptotic expansion": no theorem with remainder estimates in the vault (TH Theorem §B4.1.5 uses the method inline for Stirling's formula, QM Theorem §C4.2.5 states stationary phase). The error terms stay stated, not estimated. -->
>
> **Step 3** (steepest descent: move the contour). By Cauchy's theorem ([[§CA.5 Contour Integration#^thm-ca-5-2|Theorem §CA.5.2]]) move the real line through $p_0$; by hypothesis no singularity is crossed and the ends contribute nothing.
>
> **Step 4** (the direction). Near $p_0$, $\Phi \simeq \Phi(p_0) + \frac12\Phi''(p_0)(p - p_0)^2$. Put $p - p_0 = e^{i\theta}q$, $q$ real, $dp = e^{i\theta}dq$, with $\theta$ chosen so that $\Phi''(p_0)e^{2i\theta} = -|\Phi''(p_0)|$. Along this line $\operatorname{Im}\Phi$ is stationary (no oscillation) and $\operatorname{Re}\Phi$ falls off as fast as possible: the steepest-descent path.
>
> **Step 5** (the Gaussian again). The integral is now the real Gaussian of Step 2 times $e^{i\theta}$.
>
> **What the derivation shows.**
> - The factor $e^{\lambda\Phi(p_0)}$ depends on $p_0$ alone; the Gaussian width, the next Taylor terms and the variation of $f$ change only the prefactor.
> - If the saddle sits on a branch cut, Step 3 fails → [[§CA.6 Gaussian Integrals, Stationary Phase and Bessel Functions#^rem-ca-6-2|Remark: When the saddle sits on a branch cut]].
> - Used in: the large-argument form of $K_\nu$ ([[§CA.6 Gaussian Integrals, Stationary Phase and Bessel Functions#^ex-ca-6-1|Example §CA.6.1]], Theorem §CA.6.4) and the exponent of the Wightman function outside the light cone ([[§C2b.3 Explicit Forms of the Wightman Function#^ex-c2b-3-1|Example §C2b.3.1]]); the leak of the single-particle amplitude ([[§C1a.3 Causal Structure and the Causality of a Single Particle#^thm-c1a-3-7|Theorem §C1a.3.7]], second route).

^der-ca-6-3

*Uses:* [[§CA.6 Gaussian Integrals, Stationary Phase and Bessel Functions#^thm-ca-6-1|Theorem §CA.6.1]], [[§CA.5 Contour Integration#^thm-ca-5-2|Theorem §CA.5.2]]

> [!remark] Remark: When the saddle sits on a branch cut
> Then $\Phi$ is not analytic at $p_0$, and part 2 does not apply as stated. Wrap the contour around the cut instead ([[§CA.5 Contour Integration#^thm-ca-5-8|Theorem §CA.5.8]]): the discontinuity is an integral along the cut with a *real* exponent, to which Laplace's method (part 1) applies directly. The maximum of that real exponent is the same point, and the two answers agree. This is the situation of the two-point functions outside the light cone ([[§C2b.3 Explicit Forms of the Wightman Function#^ex-c2b-3-1|Example §C2b.3.1]] and the figure of [[§CA.5 Contour Integration|§CA.5]]).
>
> *Source: the user's PHY 513 notes, App. A §A.7 ("When the saddle sits on a branch cut"), Ch. 2 §2.2*

^rem-ca-6-2

> [!example] Example §CA.6.1: Laplace's Method for an Integral with a Double-Exponential Weight
> For $z > 0$ and real $\nu$, find the leading behaviour and the first correction, as $z \to \infty$, of
>
> $$
> F_\nu(z) = \int_0^\infty du\;e^{-z\cosh u}\cosh(\nu u) .
> $$
>
> (This integral is the function $K_\nu(z)$ defined next, [[§CA.6 Gaussian Integrals, Stationary Phase and Bessel Functions#^def-ca-6-2|Def. §CA.6.2]]; nothing about $K_\nu$ is used here.)
>
> **Step 1** (the maximum). The integrand is even in $u$, so $F_\nu = \frac12\int_{-\infty}^{\infty}$, and the exponent $-z\cosh u = \lambda\Phi(u)$, with $\lambda = z$ and $\Phi = -\cosh u$, has its single maximum at the interior point $u = 0$: $\Phi(0) = -1$, $\Phi''(0) = -1$. By [[§CA.6 Gaussian Integrals, Stationary Phase and Bessel Functions#^thm-ca-6-3|Theorem §CA.6.3]], 1 with $f = \cosh\nu u$, $f(0) = 1$: $F_\nu(z) \simeq \frac12e^{-z}\sqrt{2\pi/z} = \sqrt{\pi/2z}\,e^{-z}$.
>
> **Step 2** (expand around the maximum). Write $\cosh u = 1 + \frac{u^2}{2} + \frac{u^4}{24} + \cdots$ and $\cosh\nu u = 1 + \frac{\nu^2u^2}{2} + \cdots$; only $u \lesssim z^{-1/2}$ contributes, so expand everything but the Gaussian:
>
> $$
> F_\nu(z) = e^{-z}\int_0^\infty du\,e^{-zu^2/2}\Bigl[1 + \tfrac12\nu^2u^2 - \tfrac1{24}zu^4 + O(u^4, zu^6)\Bigr].
> $$
>
> **Step 3** (moments). $\int_0^\infty e^{-zu^2/2}\{1, u^2, u^4\}du = \sqrt{\pi/2z}\,\{1, z^{-1}, 3z^{-2}\}$: half of $\int_{-\infty}^{\infty}e^{-au^2}du = \sqrt{\pi/a}$ ([[§CA.6 Gaussian Integrals, Stationary Phase and Bessel Functions#^thm-ca-6-1|Theorem §CA.6.1]]) at $a = z/2$, and of its derivatives $-\frac{d}{da}$ and $\frac{d^2}{da^2}$, $\frac12\sqrt\pi\,a^{-3/2}$ and $\frac34\sqrt\pi\,a^{-5/2}$ (differentiation under the integral, [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|Theorem §CA.1.1]], 2). So
>
> $$
> F_\nu(z) \simeq \sqrt{\frac{\pi}{2z}}\,e^{-z}\Bigl[1 + \frac{\nu^2}{2z} - \frac{3}{24z} + \cdots\Bigr] = \sqrt{\frac{\pi}{2z}}\,e^{-z}\Bigl[1 + \frac{4\nu^2 - 1}{8z} + \cdots\Bigr] ,
> $$
>
> since $\frac{\nu^2}{2} - \frac18 = \frac{4\nu^2 - 1}{8}$. Dropped: terms of relative order $z^{-2}$.
>
> *Source: the user's PHY 513 notes, App. A §A.8 ("Large z: Laplace's method")*

^ex-ca-6-1

## The modified Bessel function $K_\nu$

> [!definition] Definition §CA.6.2: Modified Bessel Function of the Second Kind
> For $\operatorname{Re}z > 0$ and real $\nu$,
>
> $$
> K_\nu(z) = \int_0^\infty du\;e^{-z\cosh u}\cosh(\nu u), \qquad\text{so that}\qquad \int_{-\infty}^{\infty}du\,\cosh u\;e^{-z\cosh u} = 2K_1(z) .
> $$
>
> $K_\nu = K_{-\nu}$ is analytic in $z$ and continues analytically to $\mathbb C \setminus (-\infty, 0]$. The ordinary Bessel functions $J_\nu$, $Y_\nu$ and the Hankel function $H^{(2)}_\nu = J_\nu - iY_\nu$ are the oscillating solutions of Bessel's equation, to which $K_\nu$ turns at imaginary argument (Theorem §CA.6.5).
>
> *Source: the user's PHY 513 notes, App. A §A.8 (eq. (Kintegral)), Ch. 2 §2.2 (Principle "Recall: modified Bessel functions") · DLMF §10.25, §10.32.9*

^def-ca-6-2

> [!theorem] Theorem §CA.6.4: Properties of $K_\nu$
> 1. *Recursion and derivatives:* $K_{\nu+1} - K_{\nu-1} = \frac{2\nu}{z}K_\nu$, $K_\nu' = -\frac12(K_{\nu+1} + K_{\nu-1})$; in particular $K_0' = -K_1$ and $\frac{d}{dz}\bigl[z^{-\nu}K_\nu(z)\bigr] = -z^{-\nu}K_{\nu+1}(z)$.
> 2. *Large argument:* $K_\nu(z) \simeq \sqrt{\dfrac{\pi}{2z}}\,e^{-z}\Bigl[1 + \dfrac{4\nu^2 - 1}{8z} + \cdots\Bigr]$.
> 3. *Small argument:* $K_\nu(z) \simeq \frac12\Gamma(\nu)(2/z)^\nu$ for $\nu > 0$ ($\Gamma$: [[§CA.6 Gaussian Integrals, Stationary Phase and Bessel Functions#^def-ca-6-1|Def. §CA.6.1]]); more precisely $K_1(z) = \frac1z + \frac z2\ln\frac z2 + O(z)$ and $K_0(z) = -\ln\frac z2 - \gamma_E + O(z^2\ln z)$.
>
> *Source: the user's PHY 513 notes, App. A §A.8 (Definition and Derivation "Everything about $K_\nu$ from the integral representation"), Ch. 5 §5.7 (the $K_1$ series) · DLMF §10.29, §10.31, §10.40*

^thm-ca-6-4

> [!derivation]- Derivation
> **Step 1** (derivative). Differentiate under the integral ([[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|Theorem §CA.1.1]]; dominated by $\cosh u\cosh\nu u\,e^{-z_0\cosh u}$ for $\operatorname{Re}z \ge z_0 > 0$): $K_\nu' = -\int_0^\infty\cosh u\cosh\nu u\,e^{-z\cosh u}du$. With $\cosh u\cosh\nu u = \frac12[\cosh(\nu + 1)u + \cosh(\nu - 1)u]$, $K_\nu' = -\frac12(K_{\nu+1} + K_{\nu-1})$.
>
> **Step 2** (difference). $\cosh(\nu + 1)u - \cosh(\nu - 1)u = 2\sinh u\sinh\nu u$, and $\sinh u\,e^{-z\cosh u} = -\frac1z\frac{d}{du}e^{-z\cosh u}$. Integrate by parts:
>
> $$
> K_{\nu+1} - K_{\nu-1} = -\frac2z\int_0^\infty\sinh\nu u\,\frac{d}{du}e^{-z\cosh u}\,du = -\frac2z\Bigl[\sinh\nu u\,e^{-z\cosh u}\Bigr]_0^\infty + \frac{2\nu}{z}\int_0^\infty\cosh\nu u\,e^{-z\cosh u}du = \frac{2\nu}{z}K_\nu ;
> $$
>
> the boundary term vanishes at $0$ ($\sinh0 = 0$) and at $\infty$ (the double exponential wins).
>
> **Step 3** (combine). Adding Step 1 and half of Step 2: $K_\nu' = -K_{\nu+1} + \frac\nu zK_\nu$. Then $\frac{d}{dz}(z^{-\nu}K_\nu) = z^{-\nu}K_\nu' - \nu z^{-\nu-1}K_\nu = -z^{-\nu}K_{\nu+1}$. For $\nu = 0$, Step 1 with $K_{-1} = K_1$ gives $K_0' = -K_1$.
>
> **Step 4** (large $z$: Laplace). By [[§CA.6 Gaussian Integrals, Stationary Phase and Bessel Functions#^def-ca-6-2|Def. §CA.6.2]], $K_\nu(z)$ is the integral $F_\nu(z)$ of [[§CA.6 Gaussian Integrals, Stationary Phase and Bessel Functions#^ex-ca-6-1|Example §CA.6.1]]: the exponent $-z\cosh u$ is maximal at $u = 0$ ([[§CA.6 Gaussian Integrals, Stationary Phase and Bessel Functions#^thm-ca-6-3|Theorem §CA.6.3]], 1), and expanding everything but the Gaussian around it (Steps 1–2 there) gives $K_\nu(z) = e^{-z}\int_0^\infty du\,e^{-zu^2/2}\bigl[1 + \tfrac12\nu^2u^2 - \tfrac1{24}zu^4 + O(u^4, zu^6)\bigr]$.
>
> **Step 5** (moments). Step 3 of [[§CA.6 Gaussian Integrals, Stationary Phase and Bessel Functions#^ex-ca-6-1|Example §CA.6.1]]: $K_\nu = \sqrt{\pi/2z}\,e^{-z}\bigl[1 + \frac{\nu^2}{2z} - \frac{3}{24z} + \cdots\bigr]$, and $\frac{\nu^2}{2} - \frac18 = \frac{4\nu^2 - 1}{8}$. Dropped: terms of relative order $z^{-2}$.
>
> **Step 6** (small $z$). Now large $u$ dominates, up to $u \simeq \ln(2/z)$, where $\cosh u \simeq \frac12e^u$ and $\cosh\nu u \simeq \frac12e^{\nu u}$. Substitute $w = \frac12ze^u$, $du = dw/w$: $K_\nu \simeq \frac12\int du\,e^{\nu u}e^{-\frac12ze^u} = \frac12\bigl(\frac2z\bigr)^\nu\int_{z/2}^\infty w^{\nu-1}e^{-w}dw \to \frac12\Gamma(\nu)\bigl(\frac2z\bigr)^\nu$ ([[§CA.6 Gaussian Integrals, Stationary Phase and Bessel Functions#^def-ca-6-1|Def. §CA.6.1]]). Dropped: the region $u = O(1)$, which contributes $O(1)$, subleading to $z^{-\nu}$ for $\nu > 0$.
>
> **Step 7** (logarithms). The terms $\frac z2\ln\frac z2$ in $K_1$ and $-\ln\frac z2 - \gamma_E$ in $K_0$ are the standard series (DLMF §10.31), not derived here; they are consistent with $K_0' = -K_1$ at leading order ($\frac{d}{dz}(-\ln z) = -1/z$).
> <!-- S6 (2026-11-12): searched ~/Notes/Math and ~/Notes/Applied Math (Ordinary Differential Equations, Fourier Series and PDEs, Complex Variables) for "modified Bessel", "K_0", "Frobenius" series of Bessel's equation of the second kind: no home in the vault. The logarithmic terms stay quoted from DLMF. -->
>
> **What the derivation shows.**
> - Everything used in the course follows from the single integral representation.
> - The two ends of $K_1$ are the physics of the two-point function: $1/z$ is the massless light-cone singularity ([[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-5|Theorem §C2b.3.5]]), $e^{-z}$ the Compton-length decay ([[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-3|Theorem §C2b.3.3]]).

^der-ca-6-4

*Uses:* [[§CA.6 Gaussian Integrals, Stationary Phase and Bessel Functions#^def-ca-6-2|Def. §CA.6.2]], [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|Theorem §CA.1.1]], [[§CA.6 Gaussian Integrals, Stationary Phase and Bessel Functions#^thm-ca-6-3|Theorem §CA.6.3]], [[§CA.6 Gaussian Integrals, Stationary Phase and Bessel Functions#^ex-ca-6-1|Example §CA.6.1]], [[§CA.6 Gaussian Integrals, Stationary Phase and Bessel Functions#^def-ca-6-1|Def. §CA.6.1]]

> [!theorem] Theorem §CA.6.5: Further Representations; Imaginary Argument
> 1. For $m, r > 0$: $\displaystyle\int_m^\infty\frac{e^{-\rho r}\,d\rho}{\sqrt{\rho^2 - m^2}} = K_0(mr)$ and $\displaystyle\int_m^\infty\frac{\rho\,e^{-\rho r}\,d\rho}{\sqrt{\rho^2 - m^2}} = mK_1(mr)$.
> 2. For $x > 0$: $K_0(x) = \displaystyle\int_0^\infty\cos(x\sinh v)\,dv = \int_0^\infty\frac{\cos xt}{\sqrt{t^2 + 1}}\,dt$ (conditionally convergent).
> 3. For $x > 0$: $K_\nu(ix) = \frac\pi2(-i)^{\nu+1}H^{(2)}_\nu(x)$; in particular $K_1(ix) = -\frac\pi2\bigl[J_1(x) - iY_1(x)\bigr]$.
> 4. For $x \to \infty$: $J_1(x) \simeq \sqrt{2/\pi x}\,\cos(x - 3\pi/4)$ and $Y_1(x) \simeq \sqrt{2/\pi x}\,\sin(x - 3\pi/4)$.
>
> *Source: the user's PHY 513 notes, Ch. 5 §5.4 and §5.7 · Abramowitz & Stegun 9.6.21, 9.6.4 · DLMF §10.27, §10.32, §10.17*

^thm-ca-6-5

> [!derivation]- Derivation
> **Step 1** (part 1). Substitute $\rho = m\cosh u$, $u: 0 \to \infty$: $d\rho = m\sinh u\,du$ and $\sqrt{\rho^2 - m^2} = m\sinh u$, so $\frac{d\rho}{\sqrt{\rho^2 - m^2}} = du$ and $\frac{\rho\,d\rho}{\sqrt{\rho^2 - m^2}} = m\cosh u\,du$; $e^{-\rho r} = e^{-mr\cosh u}$. [[§CA.6 Gaussian Integrals, Stationary Phase and Bessel Functions#^def-ca-6-2|Def. §CA.6.2]] with $\nu = 0$ and $\nu = 1$.
>
> **Step 2** (part 2: the two forms). Substitute $t = \sinh v$, $dt = \cosh v\,dv = \sqrt{t^2 + 1}\,dv$. Convergence: Dirichlet's test ([[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-2|Theorem §CA.1.2]]).
>
> **Step 3** (part 2: the value). A table integral (A&S 9.6.21). It also follows from the keyhole computation of the equal-time Wightman function, which shows $\int_{-\infty}^\infty\frac{e^{ipr}dp}{\sqrt{p^2 + m^2}} = 2K_0(mr)$ ([[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-3|Theorem §C2b.3.3]], second route, Steps 6–7); the imaginary part of the left side vanishes by oddness, and its real part is $2\int_0^\infty\frac{\cos pr\,dp}{\sqrt{p^2 + m^2}}$, which with $p = mt$ is $2\int_0^\infty\frac{\cos(mrt)}{\sqrt{t^2 + 1}}dt$.
>
> **Step 4** (parts 3–4). The connection formula (DLMF 10.27.8) and the Hankel asymptotics (DLMF 10.17.3) are quoted; the user's notes checked 3 numerically.
> <!-- S6 (2026-11-12): searched ~/Notes/Math and ~/Notes/Applied Math for "Hankel function", "modified Bessel", "connection formula", "Y_1": no statement or proof in the vault (342 §66 has $J_n$ as Laurent coefficients only). Parts 3–4 and the table value of Step 3 stay quoted (DLMF, Abramowitz & Stegun). -->
>
> **Step 5** (consistency check of 3 with 4). From 4, $J_1 - iY_1 \simeq \sqrt{2/\pi x}\,e^{-i(x - 3\pi/4)}$; then 3 gives $K_1(ix) \simeq -\sqrt{\pi/2x}\,e^{3\pi i/4}e^{-ix} = \sqrt{\pi/2x}\,e^{-i\pi/4}e^{-ix}$, which is the large-argument form of [[§CA.6 Gaussian Integrals, Stationary Phase and Bessel Functions#^thm-ca-6-4|Theorem §CA.6.4]], 2 at $z = ix$, since $\sqrt{1/i} = e^{-i\pi/4}$.
>
> **What the derivation shows.**
> - Part 1 is the cut integral of the equal-time Wightman function and, before differentiation, PS eq. (2.52).
> - Part 3 is how $K_1$'s decay outside the light cone becomes the oscillation of $J_1$, $Y_1$ inside ([[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-4|Theorem §C2b.3.4]]).

^der-ca-6-5

*Uses:* [[§CA.6 Gaussian Integrals, Stationary Phase and Bessel Functions#^def-ca-6-2|Def. §CA.6.2]], [[§CA.6 Gaussian Integrals, Stationary Phase and Bessel Functions#^thm-ca-6-4|Theorem §CA.6.4]], [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-2|Theorem §CA.1.2]]

> [!remark] Remark: One Gaussian in three costumes
> The large-$z$ form of $K_\nu$ is Laplace's method at $u = 0$ ([[§CA.6 Gaussian Integrals, Stationary Phase and Bessel Functions#^ex-ca-6-1|Example §CA.6.1]]); the exponent $e^{-m\rho}$ of [[§C2b.3 Explicit Forms of the Wightman Function#^ex-c2b-3-1|Example §C2b.3.1]] is steepest descent through a complex saddle; and the $K_1$ of the Euclidean propagator came from Schwinger's Gaussian. They are the same Gaussian integral in different clothing, and they agree: the saddle-point prefactor of Example §C2b.3.1 is exactly the leading term of Theorem §CA.6.4, 2.
>
> *Source: the user's PHY 513 notes, App. A §A.8 ("Large z: Laplace's method"), Ch. 2 §2.2*

^rem-ca-6-3

> [!remark]- Connections
> - The integral $\int_m^\infty e^{-\rho r}d\rho/\sqrt{\rho^2 - m^2} = K_0(mr)$ of Theorem §CA.6.5 is the same integral as the eikonal phase of a Yukawa potential, $\int_b^\infty e^{-\mu r}dr/\sqrt{r^2 - b^2} = K_0(\mu b)$ ([[§C10.2 The Eikonal Approximation and the Optical Theorem#^rem-c10-2-5|QM Remark: Yukawa and Coulomb eikonal phases]]), and its logarithm at small argument is the Coulomb phase there; QM §C10.2 pointed to Mathematical Methods for $K_0$, which is this note.
> - Laplace's method is how Stirling's formula is proved ([[§B4.1 Probability Distributions and the Gaussian#^thm-b4-1-5|TH Theorem §B4.1.5]]) and why the canonical ensemble is sharply peaked ([[§B7.2 Free Energy from the Partition Function|TH §B7.2]]); the Gamma function in the small-$z$ form of $K_\nu$ is [[§B4.1 Probability Distributions and the Gaussian#^def-b4-1-5|TH Def. §B4.1.5]].
> - Stationary phase is the classical limit of the path integral ([[§C4.2 The Feynman Path Integral#^thm-c4-2-5|QM Theorem §C4.2.5]]), the Fresnel-zone construction of optics ([[§B11.3 Fresnel Diffraction and Zone Plates#^thm-b11-3-2|WO Theorem §B11.3.2]]) and the eikonal approximation ([[§C10.2 The Eikonal Approximation and the Optical Theorem|QM §C10.2]]); the complex saddle of Example §C2b.3.1 is the field-theory analogue of tunnelling under a barrier, where WKB's exponent $e^{-\int|p|\,dx}$ is likewise a saddle value ([[§B9.4 Tunnelling and the Connection Formulas|QM §B9.4]]).
> - The $n$-dimensional Gaussian with $s = it/2m$ is the free nonrelativistic propagator ([[§C4.1 Propagators#^thm-c4-1-4|QM Theorem §C4.1.4]]); with $s$ real it is the heat kernel of diffusion ([[§B4.2 Random Walks, the Central Limit Theorem and Diffusion#^thm-b4-2-7|TH Theorem §B4.2.7]]). [[§C1a.3 Causal Structure and the Causality of a Single Particle#^thm-c1a-3-4|Theorem §C1a.3.4]] uses it for the single-particle amplitude, and QFT C11 (planned) for Gaussian path integrals.
> - The same $K_\nu$ counts the particles produced by a source switched on over a time $T$ ([[§C2b.9 Particle Production by a Classical Source#^ex-c2b-9-1|Example §C2b.9.1]]): both integrate over the mass shell in hyperbolic variables.
> - Laplace's method (Theorem §CA.6.3) at the large parameter $N^2$ solves the eigenvalue gas of a random matrix: it gives the semicircle as the saddle point ([[§R3.4 The Semicircle Law II꞉ Stieltjes Transform and Coulomb Gas#^thm-r3-4-5|Thesis Thm. §R3.4.5]]) and the free energy of the gas pushed against a wall, which sets the probability that a random mass matrix has no tachyon ([[§R3.5 Edges and Extremes꞉ The Smallest Eigenvalue#^thm-r3-5-2c|Thesis Thm. §R3.5.2c]], [[§R3.5 Edges and Extremes꞉ The Smallest Eigenvalue#^thm-r3-5-3|Thesis Thm. §R3.5.3]]).
> - **Used in** (C1a–C1b places): Theorem §CA.6.2 — the nonrelativistic amplitude ([[§C1a.3 Causal Structure and the Causality of a Single Particle#^thm-c1a-3-4|Theorem §C1a.3.4]]); Def. §CA.6.2 and Theorem §CA.6.4 — the relativistic amplitude at spacelike separation and its leak ([[§C2b.4 The Single-Particle Amplitude in Closed Form#^thm-c2b-4-3|Theorem §C2b.4.3]]); Theorem §CA.6.3, Remark: When the saddle sits on a branch cut, and Example §C2b.3.1 — the saddle-point route to the leak ([[§C1a.3 Causal Structure and the Causality of a Single Particle#^thm-c1a-3-7|Theorem §C1a.3.7]]); Theorem §CA.6.5 — the timelike amplitude ([[§C2b.4 The Single-Particle Amplitude in Closed Form#^thm-c2b-4-5|Theorem §C2b.4.5]]).
> - **Used in** (Electromagnetism C places): Def. §CA.6.2 and Theorems §CA.6.4–§CA.6.5 — modified Bessel functions in cylindrical boundary-value problems: the four kinds of Bessel function, the separated solutions, and what boundary-value problems need of them ([[§C6.3 Separation in Cylindrical and Polar Coordinates#^def-c6-3-1|EM Def. §C6.3.1]], [[§C6.3 Separation in Cylindrical and Polar Coordinates#^thm-c6-3-1|EM Theorem §C6.3.1]], [[§C6.3 Separation in Cylindrical and Polar Coordinates#^thm-c6-3-2|EM Theorem §C6.3.2]]).
> - **Used in** (C2b places): Def. §CA.6.2 — [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-1|Theorem §C2b.3.1]], [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-2|Theorem §C2b.3.2]], [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-3|Theorem §C2b.3.3]], [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-4|Theorem §C2b.3.4]], [[§C2b.4 The Single-Particle Amplitude in Closed Form#^thm-c2b-4-5|Theorem §C2b.4.5]], [[§C2b.9 Particle Production by a Classical Source#^ex-c2b-9-1|Example §C2b.9.1]], [[§C2b.4 The Single-Particle Amplitude in Closed Form#^thm-c2b-4-2|Theorem §C2b.4.2]]; Theorem §CA.6.2 — [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-1|Theorem §C2b.3.1]]; Theorem §CA.6.4 — [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-1|Theorem §C2b.3.1]], [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-3|Theorem §C2b.3.3]], [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-5|Theorem §C2b.3.5]], [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-6|Theorem §C2b.3.6]], [[§C2b.4 The Single-Particle Amplitude in Closed Form#^thm-c2b-4-4|Theorem §C2b.4.4]], [[§C2b.8 Wick Rotation and the Two-Point Family#^thm-c2b-8-4|Theorem §C2b.8.4]], [[§C2b.9 Particle Production by a Classical Source#^ex-c2b-9-1|Example §C2b.9.1]], [[§C2b.4 The Single-Particle Amplitude in Closed Form#^thm-c2b-4-2|Theorem §C2b.4.2]]; Theorem §CA.6.5 — [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-3|Theorem §C2b.3.3]], [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-4|Theorem §C2b.3.4]]; Theorem §CA.6.1 — [[§C2b.9 Particle Production by a Classical Source#^ex-c2b-9-1|Example §C2b.9.1]]; Theorem §CA.6.3 — [[§C2b.3 Explicit Forms of the Wightman Function#^ex-c2b-3-1|Example §C2b.3.1]]; Remark: When the saddle sits on a branch cut — [[§C2b.3 Explicit Forms of the Wightman Function#^ex-c2b-3-1|Example §C2b.3.1]].
> - Wick's vacuum values have the form of the moment formula of a Gaussian (Isserlis), the sum over pairings of products of covariances — [[§CA.8 Pairings, Diagrams and Symmetry Factors#^rem-ca-8-1|§CA.8, ★ Remark: The same sum is the moment formula of a Gaussian]].
