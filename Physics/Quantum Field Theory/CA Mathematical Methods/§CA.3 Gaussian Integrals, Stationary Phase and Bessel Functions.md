---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: CA
section: CA.3
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§CA.2 Contour Integration]] · ↑ [[· CA Mathematical Methods]]

*Sources: the user's PHY 513 notes, App. A §§A.6–A.8 and the saddle-point computation of Ch. 2 §2.2 · DLMF §§10.25–10.40 and Abramowitz & Stegun §9.6–9.7 (cited in the user's notes).*

The two-point functions of the free field are Gaussian integrals in disguise, evaluated at a saddle or summed into a modified Bessel function $K_\nu$. Two of the tools already have homes in Quantum Mechanics and are only recalled here: the Gaussian and Fresnel integrals with complex variance ([[§C4.1 Propagators#^thm-c4-1-3|QM Theorem §C4.1.3]]) and the stationary-phase formula ([[§C4.2 The Feynman Path Integral#^thm-c4-2-5|QM Theorem §C4.2.5]]); Laplace's method appears inline in Stirling's formula ([[§B4.1 Probability Distributions and the Gaussian#^thm-b4-1-5|TH Theorem §B4.1.5]]). New here: the $n$-dimensional Gaussian Fourier transform with Schwinger's parametrization, steepest descent through a *complex* saddle and why it fixes the exponential factor, and the function $K_\nu$ with everything the course uses derived from one integral representation. The single evaluation of a two-point function in terms of $K_1$ is [[§C2.5 Heisenberg Fields, Two-Point Functions and Causality#^thm-c2-5-6|Theorem §C2.5.6]]; this section supplies its tools.

## Gaussian integrals

*Recall* ([[§C4.1 Propagators#^thm-c4-1-3|QM Theorem §C4.1.3]]): for $\operatorname{Re}a > 0$ and complex $b$, $\int d\xi\,e^{-a\xi^2 + b\xi} = \sqrt{\pi/a}\,e^{b^2/4a}$ with the principal root, extended by the identity theorem from real $a$; on the imaginary axis as the Fresnel limit $\operatorname{Re}a \to 0^+$. Same result, same argument: the home stays there.

> [!theorem] Theorem §CA.3.1: Gaussian Integrals in n Dimensions; Schwinger Parametrization
> 1. For $\operatorname{Re}s > 0$ and $\mathbf x \in \mathbb R^n$,
>
> $$
> \int\frac{d^np}{(2\pi)^n}\,e^{-s\mathbf p^2 + i\mathbf p\cdot\mathbf x} = \frac{1}{(4\pi s)^{n/2}}\,e^{-\mathbf x^2/4s} .
> $$
>
> 2. For $\operatorname{Re}A > 0$ and $\nu > 0$, $\dfrac1A = \displaystyle\int_0^\infty ds\,e^{-sA}$ and $\dfrac{1}{A^\nu} = \dfrac{1}{\Gamma(\nu)}\displaystyle\int_0^\infty ds\,s^{\nu - 1}e^{-sA}$.
>
> *Source: the user's PHY 513 notes, App. A §A.6 (eq. (gaussianN)), Ch. 2 §2.2 (Step 3 of Derivation "The relativistic amplitude in closed form")*

^thm-ca-3-1

> [!derivation]- Derivation
> *1.* The integrand factorizes over the $n$ components. Each factor is [[§C4.1 Propagators#^thm-c4-1-3|QM Theorem §C4.1.3]] with $a = s$, $b = ix_k$: $\frac{1}{2\pi}\sqrt{\pi/s}\,e^{-x_k^2/4s} = (4\pi s)^{-1/2}e^{-x_k^2/4s}$.
>
> *2.* $\int_0^\infty e^{-sA}ds = 1/A$ converges because $|e^{-sA}| = e^{-s\operatorname{Re}A}$. For general $\nu$, substitute $u = sA$ for real $A > 0$ to get $\Gamma(\nu)/A^\nu$ ([[§B4.1 Probability Distributions and the Gaussian#^def-b4-1-5|TH Def. §B4.1.5]]); both sides are analytic in $A$ on $\operatorname{Re}A > 0$, so they agree there ([[§CA.2 Contour Integration#^thm-ca-2-3|Theorem §CA.2.3]]).

^der-ca-3-1

*Uses:* [[§C4.1 Propagators#^thm-c4-1-3|QM Theorem §C4.1.3]], [[§B4.1 Probability Distributions and the Gaussian#^def-b4-1-5|TH Def. §B4.1.5]], [[§CA.2 Contour Integration#^thm-ca-2-3|Theorem §CA.2.3]]

> [!remark] Remark: Why the parametrization helps
> Schwinger's trick trades a denominator, which couples the components of $\mathbf p$ through $\mathbf p^2 + m^2$, for an exponential, which factorizes. Every momentum integral then becomes a product of one-dimensional Gaussians, and the remaining single integral over $s$ is where the special function appears: for the Euclidean propagator it is $\int ds\,s^{-2}e^{-sm^2 - R^2/4s}$, a $K_1$ ([[§C2.5 Heisenberg Fields, Two-Point Functions and Causality#^thm-c2-5-6|Theorem §C2.5.6]]). With $s$ read as a proper time, $e^{-s\mathbf p^2}$ is a heat kernel, the Euclidean version of the free propagator of [[§C4.1 Propagators#^thm-c4-1-4|QM Theorem §C4.1.4]]; loop integrals (QFT C7, planned) are done the same way.
>
> *Source: the user's PHY 513 notes, Ch. 2 §2.2, App. A §A.6*

^rem-ca-3-1

## Saddle points

*Recall* ([[§C4.2 The Feynman Path Integral#^thm-c4-2-5|QM Theorem §C4.2.5]]): if a large phase $S = \lambda\sigma$ has a single nondegenerate real stationary point $p_0$, then $\int f\,e^{iS}\,dp \simeq f(p_0)\,e^{iS(p_0)}\sqrt{2\pi/|S''(p_0)|}\;e^{i\frac\pi4\operatorname{sgn}S''(p_0)}$, and regions without a stationary point contribute less than any power of $1/\lambda$. The user's notes derive it the same way (integration by parts away from $p_0$, the Fresnel integral near it); the home stays in QM.

> [!theorem] Theorem §CA.3.2: Steepest Descent and Laplace's Method
> Let $I(\lambda) = \int f(p)\,e^{\lambda\Phi(p)}\,dp$ with $\lambda \gg 1$ and $f$, $\Phi$ independent of $\lambda$.
> 1. *(Laplace)* If $\Phi$ is real with a single nondegenerate interior maximum at $p_0$, then $I \simeq f(p_0)\,e^{\lambda\Phi(p_0)}\sqrt{2\pi/\lambda|\Phi''(p_0)|}$.
> 2. *(Steepest descent)* If $f$ and $\Phi$ are analytic and the contour can be deformed, without crossing a singularity and with negligible ends, through a complex saddle $\Phi'(p_0) = 0$, then $I \simeq f(p_0)\,e^{\lambda\Phi(p_0)}\,e^{i\theta}\sqrt{2\pi/\lambda|\Phi''(p_0)|}$, where $\theta$ is the direction with $\Phi''(p_0)e^{2i\theta} < 0$.
>
> In both cases $|I| \propto e^{\lambda\operatorname{Re}\Phi(p_0)}$: for $\Phi = iS$ with no real stationary point, $I$ is exponentially small, $|I| \propto e^{-\operatorname{Im}S(p_0)}$; the saddle alone fixes the exponent, and everything else changes only the prefactor, by relative corrections $O(1/\lambda)$.
>
> *Source: the user's PHY 513 notes, App. A §A.7 (Principle "Stationary phase and steepest descent", Derivation, Step 3)*

^thm-ca-3-2

> [!derivation]- Derivation
> *1.* Near $p_0$, $\Phi = \Phi(p_0) - \frac12|\Phi''(p_0)|(p - p_0)^2 + O((p - p_0)^3)$, and only $|p - p_0| \lesssim \lambda^{-1/2}$ contributes; elsewhere the integrand is smaller by a factor $e^{-c\lambda}$. Replacing $f$ by $f(p_0)$ and extending the Gaussian to the whole line ([[§C4.1 Propagators#^thm-c4-1-3|QM Theorem §C4.1.3]], real $a$) gives the formula, with relative error $O(1/\lambda)$ from the next Taylor terms.
>
> *2.* By Cauchy's theorem ([[§CA.2 Contour Integration#^thm-ca-2-2|Theorem §CA.2.2]]) move the contour through $p_0$. Near it $\Phi \simeq \Phi(p_0) + \frac12\Phi''(p_0)(p - p_0)^2$; along $p - p_0 = e^{i\theta}q$, $q$ real, with $\Phi''(p_0)e^{2i\theta} = -|\Phi''(p_0)|$, the imaginary part of $\Phi$ is stationary (no oscillation) and the real part falls as fast as possible: the steepest-descent path. The integral is then the real Gaussian of part 1 times $dp = e^{i\theta}dq$. The factor $e^{\lambda\Phi(p_0)}$ depends on $p_0$ alone.

^der-ca-3-2

*Uses:* [[§C4.1 Propagators#^thm-c4-1-3|QM Theorem §C4.1.3]], [[§CA.2 Contour Integration#^thm-ca-2-2|Theorem §CA.2.2]]

> [!remark] Remark: When the saddle sits on a branch cut
> Then $\Phi$ is not analytic at $p_0$, and part 2 does not apply as stated. Wrap the contour around the cut instead ([[§CA.2 Contour Integration#^thm-ca-2-8|Theorem §CA.2.8]]): the discontinuity is an integral along the cut with a *real* exponent, to which Laplace's method (part 1) applies directly. The maximum of that real exponent is the same point, and the two answers agree. This is the situation of the two-point functions outside the light cone ([[§CA.3 Gaussian Integrals, Stationary Phase and Bessel Functions#^ex-ca-3-1|Example §CA.3.1]] and the figure of [[§CA.2 Contour Integration|§CA.2]]).
>
> *Source: the user's PHY 513 notes, App. A §A.7 ("When the saddle sits on a branch cut"), Ch. 2 §2.2*

^rem-ca-3-2

> [!example] Example §CA.3.1: The Exponent of the Wightman Function Outside the Light Cone
> For $0 < |t| < r$ write $\rho = \sqrt{r^2 - t^2}$ and, after the angular integral and folding onto the whole line,
>
> $$
> D_W(t, r) = \frac{1}{8\pi^2ir}\int_{-\infty}^{\infty}dp\;\frac{p}{\sqrt{p^2 + m^2}}\,e^{iS(p)}, \qquad S(p) = pr - t\sqrt{p^2 + m^2} .
> $$
>
> Find the saddle point, the exponent and the leading prefactor for $m\rho \gg 1$.
>
> *Saddle.* $S'(p) = r - pt/\sqrt{p^2 + m^2} = 0$ gives $p^2(r^2 - t^2) = -m^2r^2$. Inside the cone ($r < |t|$) the root is real, $r/t = p/E_p$: the classical velocity, and stationary phase reproduces the oscillating amplitude. Outside no real momentum has velocity $r/t > 1$, and the saddle moves to $p_0 = imr/\rho$, where $\sqrt{p_0^2 + m^2} = imt/\rho$ (the branch fixed by the Euclidean continuation of [[§C2.5 Heisenberg Fields, Two-Point Functions and Causality#^thm-c2-5-6|Theorem §C2.5.6]]). Then
>
> $$
> S(p_0) = \frac{imr^2}{\rho} - \frac{imt^2}{\rho} = im\rho, \qquad e^{iS(p_0)} = e^{-m\sqrt{r^2 - t^2}} .
> $$
>
> *Prefactor.* $S''(p_0) = -tm^2/(p_0^2 + m^2)^{3/2} = -i\rho^3/mt^2$, so $\Phi = iS$ has $\Phi''(p_0) = \rho^3/mt^2 > 0$ and the steepest-descent direction is vertical, $\theta = \pi/2$ ([[§CA.3 Gaussian Integrals, Stationary Phase and Bessel Functions#^thm-ca-3-2|Theorem §CA.3.2]]). With $f(p_0) = p_0/\sqrt{p_0^2 + m^2} = r/t$ and the Gaussian factor $i\sqrt{2\pi/\Phi''} = it\sqrt{2\pi m/\rho^3}$,
>
> $$
> D_W \simeq \frac{1}{8\pi^2ir}\cdot\frac rt\cdot e^{-m\rho}\cdot it\sqrt{\frac{2\pi m}{\rho^3}} = \frac{\sqrt m}{2(2\pi\rho)^{3/2}}\,e^{-m\rho} ,
> $$
>
> the leading term of the exact result ([[§C2.5 Heisenberg Fields, Two-Point Functions and Causality#^thm-c2-5-7|Theorem §C2.5.7]], 1, with $\sqrt{-\xi^2} = \rho$), now at any spacelike point and not only at equal times. The saddle lies on the cut from $im$ ($|p_0| > m$); on the cut the exponent of the dominant lip is the real function $-\varrho r + t\sqrt{\varrho^2 - m^2}$ of $p = i\varrho$, maximal at $\varrho = mr/\rho$ with value $-m\rho$, which is why the method is right (Remark above). As $t \to 0$ the saddle runs into the branch point $im$, where the cut representation of the equal-time computation takes over.
>
> *Source: the user's PHY 513 notes, Ch. 2 §2.2 (Derivation "Saddle point of the relativistic amplitude", done there for the single-particle amplitude, which has the same phase $S$); the prefactor for $D_W$ worked here*

^ex-ca-3-1

## The modified Bessel function $K_\nu$

> [!definition] Definition §CA.3.1: Modified Bessel Function of the Second Kind
> For $\operatorname{Re}z > 0$ and real $\nu$,
>
> $$
> K_\nu(z) = \int_0^\infty du\;e^{-z\cosh u}\cosh(\nu u), \qquad\text{so that}\qquad \int_{-\infty}^{\infty}du\,\cosh u\;e^{-z\cosh u} = 2K_1(z) .
> $$
>
> $K_\nu = K_{-\nu}$ is analytic in $z$ and continues analytically to $\mathbb C \setminus (-\infty, 0]$. The ordinary Bessel functions $J_\nu$, $Y_\nu$ and the Hankel function $H^{(2)}_\nu = J_\nu - iY_\nu$ are the oscillating solutions of Bessel's equation, to which $K_\nu$ turns at imaginary argument (Theorem §CA.3.4).
>
> *Source: the user's PHY 513 notes, App. A §A.8 (eq. (Kintegral)), Ch. 2 §2.2 (Principle "Recall: modified Bessel functions") · DLMF §10.25, §10.32.9*

^def-ca-3-1

> [!theorem] Theorem §CA.3.3: Properties of $K_\nu$
> 1. *Recursion and derivatives:* $K_{\nu+1} - K_{\nu-1} = \frac{2\nu}{z}K_\nu$, $K_\nu' = -\frac12(K_{\nu+1} + K_{\nu-1})$; in particular $K_0' = -K_1$ and $\frac{d}{dz}\bigl[z^{-\nu}K_\nu(z)\bigr] = -z^{-\nu}K_{\nu+1}(z)$.
> 2. *Large argument:* $K_\nu(z) \simeq \sqrt{\dfrac{\pi}{2z}}\,e^{-z}\Bigl[1 + \dfrac{4\nu^2 - 1}{8z} + \cdots\Bigr]$.
> 3. *Small argument:* $K_\nu(z) \simeq \frac12\Gamma(\nu)(2/z)^\nu$ for $\nu > 0$; more precisely $K_1(z) = \frac1z + \frac z2\ln\frac z2 + O(z)$ and $K_0(z) = -\ln\frac z2 - \gamma_E + O(z^2\ln z)$.
>
> *Source: the user's PHY 513 notes, App. A §A.8 (Definition and Derivation "Everything about $K_\nu$ from the integral representation"), Ch. 5 §5.7 (the $K_1$ series) · DLMF §10.29, §10.31, §10.40*

^thm-ca-3-3

> [!derivation]- Derivation
> *1.* Differentiate under the integral ([[§CA.1 Generalized Functions and Fourier Transforms#^thm-ca-1-1|Theorem §CA.1.1]]) and use $\cosh u\cosh\nu u = \frac12[\cosh(\nu + 1)u + \cosh(\nu - 1)u]$: $K_\nu' = -\frac12(K_{\nu+1} + K_{\nu-1})$. For the difference, $\cosh(\nu + 1)u - \cosh(\nu - 1)u = 2\sinh u\sinh\nu u$ and $\sinh u\,e^{-z\cosh u} = -\frac1z\frac{d}{du}e^{-z\cosh u}$; integrating by parts (no boundary terms), $K_{\nu+1} - K_{\nu-1} = \frac{2\nu}{z}K_\nu$. Adding and subtracting: $K_\nu' = -K_{\nu+1} + \frac\nu zK_\nu$, which is the last identity; $\nu = 0$ gives $K_0' = -K_1$ (using $K_{-1} = K_1$).
>
> *2.* Laplace's method ([[§CA.3 Gaussian Integrals, Stationary Phase and Bessel Functions#^thm-ca-3-2|Theorem §CA.3.2]], 1) at the maximum $u = 0$ of $-z\cosh u$, keeping the next order: with $\cosh u = 1 + \frac{u^2}2 + \frac{u^4}{24} + \cdots$ and $\cosh\nu u = 1 + \frac{\nu^2u^2}2 + \cdots$,
>
> $$
> K_\nu(z) = e^{-z}\int_0^\infty du\,e^{-zu^2/2}\Bigl[1 + \tfrac12\nu^2u^2 - \tfrac1{24}zu^4 + \cdots\Bigr] = \sqrt{\frac{\pi}{2z}}\,e^{-z}\Bigl[1 + \frac{\nu^2}{2z} - \frac{3}{24z} + \cdots\Bigr],
> $$
>
> using $\int_0^\infty e^{-zu^2/2}\{1, u^2, u^4\}du = \sqrt{\pi/2z}\,\{1, z^{-1}, 3z^{-2}\}$; and $\frac{\nu^2}{2} - \frac18 = \frac{4\nu^2 - 1}{8}$.
>
> *3.* For small $z$ the integral is dominated by large $u$, up to $u \simeq \ln(2/z)$, where $\cosh u \simeq \frac12e^u$ and $\cosh\nu u \simeq \frac12e^{\nu u}$. With $w = \frac12ze^u$, $K_\nu \simeq \frac12(2/z)^\nu\int_{z/2}^\infty w^{\nu-1}e^{-w}dw \to \frac12\Gamma(\nu)(2/z)^\nu$ ([[§B4.1 Probability Distributions and the Gaussian#^def-b4-1-5|TH Def. §B4.1.5]]); the region $u = O(1)$ adds only $O(1)$. The logarithmic terms of $K_0$ and $K_1$ are the standard series (DLMF §10.31); they are consistent with $K_0' = -K_1$.

^der-ca-3-3

*Uses:* [[§CA.1 Generalized Functions and Fourier Transforms#^thm-ca-1-1|Theorem §CA.1.1]], [[§CA.3 Gaussian Integrals, Stationary Phase and Bessel Functions#^thm-ca-3-2|Theorem §CA.3.2]], [[§B4.1 Probability Distributions and the Gaussian#^def-b4-1-5|TH Def. §B4.1.5]]

> [!theorem] Theorem §CA.3.4: Further Representations; Imaginary Argument
> 1. For $m, r > 0$: $\displaystyle\int_m^\infty\frac{e^{-\rho r}\,d\rho}{\sqrt{\rho^2 - m^2}} = K_0(mr)$ and $\displaystyle\int_m^\infty\frac{\rho\,e^{-\rho r}\,d\rho}{\sqrt{\rho^2 - m^2}} = mK_1(mr)$.
> 2. For $x > 0$: $K_0(x) = \displaystyle\int_0^\infty\cos(x\sinh v)\,dv = \int_0^\infty\frac{\cos xt}{\sqrt{t^2 + 1}}\,dt$ (conditionally convergent).
> 3. For $x > 0$: $K_\nu(ix) = \frac\pi2(-i)^{\nu+1}H^{(2)}_\nu(x)$; in particular $K_1(ix) = -\frac\pi2\bigl[J_1(x) - iY_1(x)\bigr]$.
> 4. For $x \to \infty$: $J_1(x) \simeq \sqrt{2/\pi x}\,\cos(x - 3\pi/4)$ and $Y_1(x) \simeq \sqrt{2/\pi x}\,\sin(x - 3\pi/4)$.
>
> *Source: the user's PHY 513 notes, Ch. 5 §5.4 and §5.7 · Abramowitz & Stegun 9.6.21, 9.6.4 · DLMF §10.27, §10.32, §10.17*

^thm-ca-3-4

> [!derivation]- Derivation
> *1.* Substitute $\rho = m\cosh u$: $d\rho/\sqrt{\rho^2 - m^2} = du$ and $\rho\,d\rho/\sqrt{\rho^2 - m^2} = m\cosh u\,du$, then [[§CA.3 Gaussian Integrals, Stationary Phase and Bessel Functions#^def-ca-3-1|Def. §CA.3.1]] with $\nu = 0, 1$.
>
> *2.* The two forms are related by $t = \sinh v$. The value is a table integral (A&S 9.6.21); it also follows from the keyhole computation of the equal-time Wightman function, which shows $\int_{-\infty}^\infty\frac{e^{ipr}dp}{\sqrt{p^2 + m^2}} = 2K_0(mr)$ ([[§C2.5 Heisenberg Fields, Two-Point Functions and Causality#^thm-c2-5-7|Theorem §C2.5.7]], second route), whose real part is twice the integral here with $x = mr$. Convergence: Dirichlet's test ([[§CA.1 Generalized Functions and Fourier Transforms#^thm-ca-1-2|Theorem §CA.1.2]]).
>
> *3–4.* Connection formula and asymptotics of the Hankel and Bessel functions, quoted from DLMF (10.27.8, 10.17.3); the user's notes checked 3 numerically. Consistency check: 4 gives $J_1 - iY_1 \simeq \sqrt{2/\pi x}\,e^{-i(x - 3\pi/4)}$, so 3 gives $K_1(ix) \simeq -\sqrt{\pi/2x}\,e^{3\pi i/4}e^{-ix} = \sqrt{\pi/2x}\,e^{-i\pi/4}e^{-ix}$, which is the large-argument form of [[§CA.3 Gaussian Integrals, Stationary Phase and Bessel Functions#^thm-ca-3-3|Theorem §CA.3.3]], 2 at $z = ix$, since $\sqrt{1/i} = e^{-i\pi/4}$.

^der-ca-3-4

*Uses:* [[§CA.3 Gaussian Integrals, Stationary Phase and Bessel Functions#^def-ca-3-1|Def. §CA.3.1]], [[§CA.3 Gaussian Integrals, Stationary Phase and Bessel Functions#^thm-ca-3-3|Theorem §CA.3.3]], [[§CA.1 Generalized Functions and Fourier Transforms#^thm-ca-1-2|Theorem §CA.1.2]]

> [!remark] Remark: One Gaussian in three costumes
> The large-$z$ form of $K_\nu$ is Laplace's method at $u = 0$; the exponent $e^{-m\rho}$ of Example §CA.3.1 is steepest descent through a complex saddle; and the $K_1$ of the Euclidean propagator came from Schwinger's Gaussian. They are the same Gaussian integral in different clothing, and they agree: the saddle-point prefactor of Example §CA.3.1 is exactly the leading term of Theorem §CA.3.3, 2. The behaviour at the two ends of $K_1$ is the physics of the two-point function: $1/z$ is the massless light-cone singularity, $e^{-z}$ the Compton-length decay.
>
> *Source: the user's PHY 513 notes, App. A §A.8 ("Large z: Laplace's method"), Ch. 2 §2.2*

^rem-ca-3-3

> [!remark]- Connections
> - The integral $\int_m^\infty e^{-\rho r}d\rho/\sqrt{\rho^2 - m^2} = K_0(mr)$ of Theorem §CA.3.4 is the same integral as the eikonal phase of a Yukawa potential, $\int_b^\infty e^{-\mu r}dr/\sqrt{r^2 - b^2} = K_0(\mu b)$ ([[§C10.2 The Eikonal Approximation and the Optical Theorem#^rem-c10-2-5|QM Remark: Yukawa and Coulomb eikonal phases]]), and its logarithm at small argument is the Coulomb phase there; QM §C10.2 pointed to Mathematical Methods for $K_0$, which is this note.
> - Laplace's method is how Stirling's formula is proved ([[§B4.1 Probability Distributions and the Gaussian#^thm-b4-1-5|TH Theorem §B4.1.5]]) and why the canonical ensemble is sharply peaked ([[§B7.2 Free Energy from the Partition Function|TH §B7.2]]); the Gamma function in the small-$z$ form of $K_\nu$ is [[§B4.1 Probability Distributions and the Gaussian#^def-b4-1-5|TH Def. §B4.1.5]].
> - Stationary phase is the classical limit of the path integral ([[§C4.2 The Feynman Path Integral#^thm-c4-2-5|QM Theorem §C4.2.5]]), the Fresnel-zone construction of optics ([[§B11.3 Fresnel Diffraction and Zone Plates#^thm-b11-3-2|WO Theorem §B11.3.2]]) and the eikonal approximation ([[§C10.2 The Eikonal Approximation and the Optical Theorem|QM §C10.2]]); the complex saddle of Example §CA.3.1 is the field-theory analogue of tunnelling under a barrier, where WKB's exponent $e^{-\int|p|\,dx}$ is likewise a saddle value ([[§B9.4 Tunnelling and the Connection Formulas|QM §B9.4]]).
> - The $n$-dimensional Gaussian with $s = it/2m$ is the free nonrelativistic propagator ([[§C4.1 Propagators#^thm-c4-1-4|QM Theorem §C4.1.4]]); with $s$ real it is the heat kernel of diffusion ([[§B4.2 Random Walks, the Central Limit Theorem and Diffusion#^thm-b4-2-6|TH Theorem §B4.2.6]]). QFT C1 (planned) uses it for the single-particle amplitude, and QFT C11 (planned) for Gaussian path integrals.
> - The Hankel function $H^{(2)}_\nu$ at real argument is an outgoing-type oscillation; that $K_\nu$ turns into it at imaginary argument is the analytic statement behind "decay outside the light cone, oscillation inside" ([[§C2.5 Heisenberg Fields, Two-Point Functions and Causality#^thm-c2-5-7|Theorem §C2.5.7]]).
