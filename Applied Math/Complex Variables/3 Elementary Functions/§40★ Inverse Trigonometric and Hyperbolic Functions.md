---
type: section
subject: "[[Complex Variables]]"
chapter: 3
section: 40
bc: "40"
aliases: ["B&C 40"]
tags: [complex-variables, math342, extension]
---
← [[§39★ Hyperbolic Functions]] · ↑ [[· 3 Elementary Functions]] · [[§41 Derivatives of Functions w(t)]] →

*Brown–Churchill, Section 40.*
★ *Beyond MAT 342: the course skipped this section or left it optional; it is included from Brown–Churchill.*

Since $\sin w$, $\cos w$, $\tan w$ and their hyperbolic counterparts are rational functions of $e^{iw}$ or $e^w$, the equation $z = \sin w$ is a quadratic equation for $e^{iw}$, and solving it and taking logarithms expresses $\sin^{-1}z$ as a logarithm: $\sin^{-1}z = -i\log\big[iz + (1 - z^2)^{1/2}\big]$. All six inverse functions arise this way. They are multiple-valued, with infinitely many values at each point, and become single-valued analytic functions once branches of the square root and the logarithm are chosen. Their derivatives are the formulas of calculus, with the sign of the square root now tied to the branch. The inverse sine is the conformal map of [[§106★ Some Related Mappings|§106★]] and of the flows through slits in Chapter 10.

## The Inverse Sine

> [!definition] Definition §40.1: Inverse Trigonometric and Hyperbolic Functions
> For a complex number $z$, we write
>
> $$
> w = \sin^{-1}z \qquad\text{when}\qquad z = \sin w ;
> $$
>
> that is, the values of $\sin^{-1}z$ are all the numbers $w$ with $\sin w = z$. The inverse functions $\cos^{-1}z$, $\tan^{-1}z$, $\sinh^{-1}z$, $\cosh^{-1}z$ and $\tanh^{-1}z$ are defined in the same way. A common alternative notation is $\arcsin z$, etc.
>
> *B&C: Sec. 40 (text)*

^def-40-1

> [!theorem] Proposition §40.1: The Inverse Sine as a Logarithm
> For every complex $z$,
>
> $$
> \sin^{-1}z = -i\log\big[iz + (1 - z^2)^{1/2}\big] , \qquad (2)
> $$
>
> where $(1 - z^2)^{1/2}$ is the double-valued square root and $\log$ the multiple-valued logarithm: the values of $\sin^{-1}z$ are the numbers $-i\log W$, where $W$ runs through the two numbers $iz + (1 - z^2)^{1/2}$ and $\log W$ through all logarithms of each. In particular $\sin^{-1}z$ has infinitely many values at each point $z$.
>
> *B&C: Sec. 40, Equations (1) and (2)*

^prop-40-1

> [!proof]+ Proof
> By [[§37 The Trigonometric Functions sin z and cos z#^def-37-1|Definition §37.1]], $z = \sin w$ means
>
> $$
> z = \frac{e^{iw} - e^{-iw}}{2i} .
> $$
>
> Multiplying by $2ie^{iw}$ (which is nonzero) puts this in the form
>
> $$
> (e^{iw})^2 - 2iz(e^{iw}) - 1 = 0 ,
> $$
>
> a quadratic equation in $e^{iw}$. By the quadratic formula ([[§11 Examples (Roots of Complex Numbers)#^ex-11-4|Example §11.4]]), with the double-valued square root,
>
> $$
> e^{iw} = \frac{2iz + (-4z^2 + 4)^{1/2}}{2} = iz + (1 - z^2)^{1/2} , \qquad (1)
> $$
>
> since the two square roots of $4(1 - z^2)$ are twice those of $1 - z^2$. The two roots $W$ of the quadratic have product $-1$, so neither is zero and each has logarithms. Conversely, if $e^{iw} = W$ for a root $W$, then $W^2 - 2izW - 1 = 0$, and dividing by $2iW$ gives back $\sin w = (W - W^{-1})/(2i) = z$. So $\sin w = z$ if and only if $e^{iw}$ is one of the two numbers (1), that is ([[§31 The Logarithmic Function#^thm-31-1|Theorem §31.1]]), if and only if $iw$ is a value of $\log\big[iz + (1 - z^2)^{1/2}\big]$. Multiplying by $-i$ gives (2). Each of the two numbers $W$ has infinitely many logarithms, $\operatorname{Log} W + 2n\pi i$, so $\sin^{-1}z$ has infinitely many values.

^pf-40-1

*Uses:* [[§37 The Trigonometric Functions sin z and cos z#^def-37-1|Def. §37.1]], [[§31 The Logarithmic Function#^thm-31-1|§31.1]], [[§11 Examples (Roots of Complex Numbers)#^ex-11-4|Ex. §11.4]]

> [!example] Example §40.1: The Values of sin⁻¹(−i)
> Expression (2) gives, with $z = -i$, $iz = 1$ and $1 - z^2 = 2$,
>
> $$
> \sin^{-1}(-i) = -i\log(1 \pm \sqrt2) .
> $$
>
> But
>
> $$
> \log(1 + \sqrt2) = \ln(1 + \sqrt2) + 2n\pi i \qquad\text{and}\qquad \log(1 - \sqrt2) = \ln(\sqrt2 - 1) + (2n + 1)\pi i \qquad (n = 0, \pm1, \pm2, \ldots) ,
> $$
>
> since $1 - \sqrt2 < 0$. Since
>
> $$
> \ln(\sqrt2 - 1) = \ln\frac{1}{1 + \sqrt2} = -\ln(1 + \sqrt2) ,
> $$
>
> the numbers $(-1)^n\ln(1 + \sqrt2) + n\pi i$ $(n = 0, \pm1, \pm2, \ldots)$ constitute the set of values of $\log(1 \pm \sqrt2)$: even $n$ give the values of $\log(1 + \sqrt2)$, odd $n$ those of $\log(1 - \sqrt2)$. Thus, in rectangular form,
>
> $$
> \sin^{-1}(-i) = n\pi + i(-1)^{n + 1}\ln(1 + \sqrt2) \qquad (n = 0, \pm1, \pm2, \ldots) .
> $$
>
> Check, by (13) of §37: $\sin\big(n\pi + i(-1)^{n+1}a\big) = \sin(n\pi)\cosh a + i\cos(n\pi)\sinh\big((-1)^{n+1}a\big) = i(-1)^n(-1)^{n+1}\sinh a = -i\sinh a$, and $\sinh a = 1$ for $a = \ln(1 + \sqrt2)$, since $\frac12\big((1 + \sqrt2) - (\sqrt2 - 1)\big) = 1$.
>
> *B&C: Sec. 40, Example*

^ex-40-1

## Inverse Cosine and Inverse Tangent

> [!theorem] Proposition §40.2: Inverse Cosine and Inverse Tangent as Logarithms
> For every complex $z$,
>
> $$
> \cos^{-1}z = -i\log\big[z + i(1 - z^2)^{1/2}\big] , \qquad (3)
> $$
>
> and for $z \ne \pm i$,
>
> $$
> \tan^{-1}z = \frac i2\log\frac{i + z}{i - z} . \qquad (4)
> $$
>
> (The values $\pm i$ are not taken by $\tan w$ at all.)
>
> *B&C: Sec. 40, Equations (3) and (4)*

^prop-40-2

> [!proof]+ Proof
> B&C says that the technique used for (2) applies; here are the steps (for (4), B&C's Exercise 5).
>
> **(3).** $z = \cos w = \frac12(e^{iw} + e^{-iw})$ becomes, after multiplying by $2e^{iw}$, $(e^{iw})^2 - 2z\,e^{iw} + 1 = 0$. Its roots are $e^{iw} = z + (z^2 - 1)^{1/2}$, with product $1$, so they are nonzero, and as in the proof of Proposition §40.1 every root gives solutions $w$. Since $z^2 - 1 = i^2(1 - z^2)$, the two square roots of $z^2 - 1$ are $i$ times those of $1 - z^2$, so $e^{iw} = z + i(1 - z^2)^{1/2}$, and $iw = \log\big[z + i(1 - z^2)^{1/2}\big]$, which is (3).
>
> **(4).** Write $\zeta = e^{2iw}$. By (1) of §37,
>
> $$
> \tan w = \frac{\sin w}{\cos w} = \frac{e^{iw} - e^{-iw}}{i(e^{iw} + e^{-iw})} = \frac{\zeta - 1}{i(\zeta + 1)} ,
> $$
>
> after multiplying numerator and denominator by $e^{iw}$ (and $\cos w \ne 0$ means $\zeta \ne -1$). So $\tan w = z$ if and only if $iz(\zeta + 1) = \zeta - 1$ with $\zeta \ne -1$, that is, $\zeta(1 - iz) = 1 + iz$. If $z = -i$ this says $0 = 2$, and if $z = i$ it says $2\zeta = 0$; both are impossible, since $\zeta = e^{2iw} \ne 0$. Otherwise
>
> $$
> e^{2iw} = \zeta = \frac{1 + iz}{1 - iz} = \frac{i - z}{i + z}
> $$
>
> (multiply numerator and denominator by $i$), which is nonzero and not $-1$. Hence $2iw = \log\frac{i - z}{i + z}$, and $w = \frac{1}{2i}\log\frac{i - z}{i + z} = \frac i2\Big(-\log\frac{i - z}{i + z}\Big) = \frac i2\log\frac{i + z}{i - z}$, using $\log(1/\zeta) = -\log\zeta$ (as sets; [[§34 Some Identities Involving Logarithms#^thm-34-2|Theorem §34.2]] with $z_1 = 1$).

^pf-40-2

*Uses:* [[§37 The Trigonometric Functions sin z and cos z#^def-37-1|Def. §37.1]], [[§40★ Inverse Trigonometric and Hyperbolic Functions#^prop-40-1|§40.1]], [[§31 The Logarithmic Function#^thm-31-1|§31.1]], [[§34 Some Identities Involving Logarithms#^thm-34-2|§34.2]]

The functions $\cos^{-1}z$ and $\tan^{-1}z$ are also multiple-valued. When specific branches of the square root and logarithmic functions are used, all three inverse functions become single-valued and analytic, because they are then compositions of analytic functions ([[§33 Branches and Derivatives of Logarithms#^thm-33-1|Theorem §33.1]], [[§35 The Power Function#^thm-35-2|Theorem §35.2]] for the branch of $(1 - z^2)^{1/2}$).

> [!theorem] Proposition §40.3: Derivatives of the Inverse Trigonometric Functions
> On a domain where branches are chosen as just described,
>
> $$
> \frac{d}{dz}\sin^{-1}z = \frac{1}{(1 - z^2)^{1/2}} , \qquad (5)
> $$
>
> $$
> \frac{d}{dz}\cos^{-1}z = \frac{-1}{(1 - z^2)^{1/2}} , \qquad (6)
> $$
>
> where in each case $(1 - z^2)^{1/2}$ is the same branch of the square root used in the function; the derivatives depend on that choice. In contrast,
>
> $$
> \frac{d}{dz}\tan^{-1}z = \frac{1}{1 + z^2} \qquad (7)
> $$
>
> does not depend on the manner in which $\tan^{-1}z$ is made single-valued.
>
> *B&C: Sec. 40, Equations (5)–(7)*

^prop-40-3

> [!proof]+ Proof
> (B&C's Exercises 4 and 6: "readily obtained from the logarithmic expressions".) Let $s(z)$ be a branch of $(1 - z^2)^{1/2}$, analytic and nonzero on the domain (so $z \ne \pm1$ there). Differentiating $s^2 = 1 - z^2$ gives $2ss' = -2z$, that is, $s' = -z/s$. Throughout, the derivative of a branch of $\log\zeta(z)$ is $\zeta'(z)/\zeta(z)$, by the chain rule and [[§33 Branches and Derivatives of Logarithms#^thm-33-1|Theorem §33.1]]; this does not depend on which branch of $\log$ is used.
>
> **(5).** With $\zeta = iz + s$, $\zeta' = i + s' = i - z/s = (is - z)/s$, and $is - z = i(s + iz) = i\zeta$. So
>
> $$
> \frac{d}{dz}\sin^{-1}z = -i\,\frac{\zeta'}{\zeta} = -i\cdot\frac{i\zeta}{s\zeta} = \frac1s .
> $$
>
> **(6).** With $\zeta = z + is$, $\zeta' = 1 + is' = 1 - iz/s = (s - iz)/s$, and $s - iz = -i(z + is) = -i\zeta$. So
>
> $$
> \frac{d}{dz}\cos^{-1}z = -i\,\frac{\zeta'}{\zeta} = -i\cdot\frac{-i\zeta}{s\zeta} = -\frac1s .
> $$
>
> **(7).** With $\zeta = \frac{i + z}{i - z}$, $\zeta' = \frac{(i - z) + (i + z)}{(i - z)^2} = \frac{2i}{(i - z)^2}$, so $\frac{\zeta'}{\zeta} = \frac{2i}{(i - z)(i + z)} = \frac{2i}{i^2 - z^2} = \frac{-2i}{1 + z^2}$, and
>
> $$
> \frac{d}{dz}\tan^{-1}z = \frac i2\cdot\frac{-2i}{1 + z^2} = \frac{1}{1 + z^2} .
> $$
>
> No square root occurs, and the derivative of every branch of $\log\zeta$ is $\zeta'/\zeta$, so the result is the same for every branch.

^pf-40-3

*Uses:* [[§40★ Inverse Trigonometric and Hyperbolic Functions#^prop-40-1|§40.1]], [[§40★ Inverse Trigonometric and Hyperbolic Functions#^prop-40-2|§40.2]], [[§33 Branches and Derivatives of Logarithms#^thm-33-1|§33.1]], [[§20 Rules for Differentiation#^thm-20-2|§20.2]], [[§20 Rules for Differentiation#^thm-20-4|§20.4]]

> [!remark]- Connections
> - For real $x$ in $(-1, 1)$ and the principal branches these are the calculus formulas $\frac{d}{dx}\sin^{-1}x = \frac{1}{\sqrt{1 - x^2}}$, $\frac{d}{dx}\cos^{-1}x = -\frac{1}{\sqrt{1 - x^2}}$, $\frac{d}{dx}\tan^{-1}x = \frac{1}{1 + x^2}$: [[§19 Derivatives of Logarithmic and Inverse Trigonometric Functions#^thm-19-8|Calc Thm. §19.8]], proved there by differentiating an inverse function, [[§19 Derivatives of Logarithmic and Inverse Trigonometric Functions#^thm-19-1|Calc Thm. §19.1]].

## Inverse Hyperbolic Functions

> [!theorem] Proposition §40.4: Inverse Hyperbolic Functions as Logarithms
> Inverse hyperbolic functions can be treated in a corresponding manner:
>
> $$
> \sinh^{-1}z = \log\big[z + (z^2 + 1)^{1/2}\big] , \qquad (8)
> $$
>
> $$
> \cosh^{-1}z = \log\big[z + (z^2 - 1)^{1/2}\big] , \qquad (9)
> $$
>
> and, for $z \ne \pm1$,
>
> $$
> \tanh^{-1}z = \frac12\log\frac{1 + z}{1 - z} . \qquad (10)
> $$
>
> *B&C: Sec. 40, Equations (8)–(10)*

^prop-40-4

> [!proof]+ Proof
> (B&C states these as "it turns out"; (9) is its Exercise 7.) Use [[§39★ Hyperbolic Functions#^def-39-1|Definition §39.1]] and solve for $e^w$.
>
> **(8).** $z = \sinh w = \frac12(e^w - e^{-w})$ becomes $(e^w)^2 - 2z\,e^w - 1 = 0$, so $e^w = z + (z^2 + 1)^{1/2}$ (roots with product $-1$, hence nonzero), and $w = \log\big[z + (z^2 + 1)^{1/2}\big]$.
>
> **(9).** $z = \cosh w = \frac12(e^w + e^{-w})$ becomes $(e^w)^2 - 2z\,e^w + 1 = 0$, so $e^w = z + (z^2 - 1)^{1/2}$ (roots with product $1$), and $w = \log\big[z + (z^2 - 1)^{1/2}\big]$.
>
> **(10).** $z = \tanh w = \frac{e^w - e^{-w}}{e^w + e^{-w}} = \frac{e^{2w} - 1}{e^{2w} + 1}$ becomes $e^{2w}(1 - z) = 1 + z$. For $z = \pm1$ this has no solution: for $z = 1$ it says $0 = 2$, and for $z = -1$ it says $2e^{2w} = 0$. Otherwise $e^{2w} = \frac{1 + z}{1 - z}$, and $w = \frac12\log\frac{1 + z}{1 - z}$.
>
> In each case, as in the proof of Proposition §40.1, every root of the quadratic gives solutions, since $e^w = W$ is solvable for every $W \ne 0$ ([[§31 The Logarithmic Function#^thm-31-1|Theorem §31.1]]).

^pf-40-4

*Uses:* [[§39★ Hyperbolic Functions#^def-39-1|Def. §39.1]], [[§31 The Logarithmic Function#^thm-31-1|§31.1]], [[§11 Examples (Roots of Complex Numbers)#^ex-11-4|Ex. §11.4]]

> [!remark]- Connections
> - The real formulas, with the positive square root and $\ln$: [[§24 Hyperbolic Functions#^thm-24-3|Calc Thm. §24.3]], proved by the same quadratic in $e^y$; their derivatives, [[§24 Hyperbolic Functions#^thm-24-4|Calc Thm. §24.4]]. In the complex plane the restriction $x \ge 1$ for $\cosh^{-1}x$ and $|x| < 1$ for $\tanh^{-1}x$ disappears, at the price of multiple values.

## Examples

> [!example] Example §40.2: sin z = 2, Two Ways
> **(a) Real and imaginary parts.** By (13) of §37, $\sin z = 2$ means $\sin x\cosh y = 2$ and $\cos x\sinh y = 0$. If $\sinh y = 0$, then $y = 0$ and $\sin x = 2$: impossible. So $\cos x = 0$, $x = \frac\pi2 + n\pi$, $\sin x = (-1)^n$, and $(-1)^n\cosh y = 2$ forces $n$ even and $\cosh y = 2$, $y = \pm\cosh^{-1}2 = \pm\ln(2 + \sqrt3)$.
>
> **(b) By (2).** With $z = 2$: $iz = 2i$ and $(1 - z^2)^{1/2} = (-3)^{1/2} = \pm\sqrt3\,i$, so
>
> $$
> \sin^{-1}2 = -i\log\big[(2 \pm \sqrt3)i\big] = -i\Big[\ln(2 \pm \sqrt3) + i\Big(\frac\pi2 + 2n\pi\Big)\Big] = \Big(2n + \frac12\Big)\pi - i\ln(2 \pm \sqrt3) .
> $$
>
> Since $(2 - \sqrt3)(2 + \sqrt3) = 1$, $\ln(2 - \sqrt3) = -\ln(2 + \sqrt3)$. Both ways,
>
> $$
> z = \Big(2n + \frac12\Big)\pi \pm i\ln(2 + \sqrt3) \qquad (n = 0, \pm1, \pm2, \ldots) .
> $$
>
> *B&C: Sec. 40, Exercise 2*

^ex-40-2

> [!example] Example §40.3: Values of tan⁻¹, cosh⁻¹ and tanh⁻¹
> **(a)** By (4), $\tan^{-1}(2i) = \frac i2\log\frac{3i}{-i} = \frac i2\log(-3) = \frac i2\big[\ln 3 + (2n + 1)\pi i\big] = -\Big(n + \frac12\Big)\pi + \frac i2\ln 3$. Since $-(n + \frac12) = m + \frac12$ with $m = -n - 1$,
>
> $$
> \tan^{-1}(2i) = \Big(m + \frac12\Big)\pi + \frac i2\ln 3 \qquad (m = 0, \pm1, \pm2, \ldots) .
> $$
>
> **(b)** By (4), $\tan^{-1}(1 + i) = \frac i2\log\frac{1 + 2i}{-1} = \frac i2\log(-1 - 2i)$. Here $|-1 - 2i| = \sqrt5$ and $\operatorname{Arg}(-1 - 2i) = -\pi + \tan^{-1}2$ (third quadrant), so
>
> $$
> \tan^{-1}(1 + i) = \frac i2\Big[\frac12\ln 5 + i\big(-\pi + \tan^{-1}2 + 2n\pi\big)\Big] = \frac{\pi - \tan^{-1}2}{2} + m\pi + \frac i4\ln 5 \qquad (m = 0, \pm1, \pm2, \ldots) ,
> $$
>
> with $m = -n$; numerically $\approx 1.0172 + m\pi + 0.4024i$.
>
> **(c)** By (9), $\cosh^{-1}(-1) = \log\big[-1 + (1 - 1)^{1/2}\big] = \log(-1) = (2n + 1)\pi i$ $(n = 0, \pm1, \pm2, \ldots)$. Check: $\cosh\big((2n + 1)\pi i\big) = \cos\big((2n + 1)\pi\big) = -1$.
>
> **(d)** By (10), $\tanh^{-1}0 = \frac12\log 1 = \frac12(2n\pi i) = n\pi i$ $(n = 0, \pm1, \pm2, \ldots)$: exactly the zeros of $\sinh z$ ([[§39★ Hyperbolic Functions#^thm-39-4|Theorem §39.4]]), which are the zeros of $\tanh z$.
>
> *B&C: Sec. 40, Exercise 1*

^ex-40-3
