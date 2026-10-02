---
type: section
subject: "[[Complex Variables]]"
chapter: 3
section: 39
bc: "39"
aliases: ["B&C 39"]
tags: [complex-variables, math342, extension]
---
← [[§38 Zeros and Singularities of Trigonometric Functions]] · ↑ [[· 3 Elementary Functions]] · [[§40★ Inverse Trigonometric and Hyperbolic Functions]] →

*Brown–Churchill, Section 39.*
★ *Beyond MAT 342: the course skipped this section or left it optional; it is included from Brown–Churchill.*

The hyperbolic sine and cosine of a complex variable are defined by the formulas of calculus, $\sinh z = \frac12(e^z - e^{-z})$ and $\cosh z = \frac12(e^z + e^{-z})$. In the complex plane they are not new functions: $\sinh z = -i\sin(iz)$ and $\cosh z = \cos(iz)$, so they are $\sin$ and $\cos$ viewed along the imaginary axis. Every identity, the period $2\pi i$, and the zeros (all on the imaginary axis) follow from [[§37 The Trigonometric Functions sin z and cos z|§37]] and [[§38 Zeros and Singularities of Trigonometric Functions|§38]] by this rotation. The functions appear wherever a trigonometric function is evaluated off the real axis, for instance in the components (13)–(14) of $\sin z$ and $\cos z$.

## Definitions and Relations to sin and cos

> [!definition] Definition §39.1: Hyperbolic Sine and Cosine
> The **hyperbolic sine and cosine functions** of a complex variable $z$ are
>
> $$
> \sinh z = \frac{e^z - e^{-z}}{2}, \qquad \cosh z = \frac{e^z + e^{-z}}{2} . \qquad (1)
> $$
>
> *B&C: Sec. 39, Equation (1)*

^def-39-1

> [!remark]- Connections
> - The real hyperbolic functions, their identities and derivatives: [[§24 Hyperbolic Functions#^def-24-1|Calc Def. §24.1]], [[§24 Hyperbolic Functions#^thm-24-1|Calc Thm. §24.1]], [[§24 Hyperbolic Functions#^thm-24-2|Calc Thm. §24.2]]. All of them extend to complex $z$, either by the same computations from (1) or by the relations (3)–(4) below.

> [!theorem] Proposition §39.1: sinh z and cosh z Are Entire
> $\sinh z$ and $\cosh z$ are entire, and
>
> $$
> \frac{d}{dz}\sinh z = \cosh z, \qquad \frac{d}{dz}\cosh z = \sinh z . \qquad (2)
> $$
>
> *B&C: Sec. 39, Equation (2)*

^prop-39-1

> [!proof]+ Proof
> (B&C's Exercise 1.) $e^z$ and $e^{-z}$ are entire, with derivatives $e^z$ and $-e^{-z}$ ([[§30 The Exponential Function#^thm-30-3|Theorem §30.3]] and the chain rule), so their linear combinations (1) are entire, and
>
> $$
> \frac{d}{dz}\sinh z = \frac{e^z + e^{-z}}{2} = \cosh z, \qquad \frac{d}{dz}\cosh z = \frac{e^z - e^{-z}}{2} = \sinh z .
> $$

^pf-39-1

*Uses:* [[§39★ Hyperbolic Functions#^def-39-1|Def. §39.1]], [[§30 The Exponential Function#^thm-30-3|§30.3]], [[§20 Rules for Differentiation|§20]] (chain rule)

> [!theorem] Proposition §39.2: Hyperbolic and Trigonometric Functions
> For all $z$,
>
> $$
> -i\sinh(iz) = \sin z, \qquad \cosh(iz) = \cos z , \qquad (3)
> $$
>
> $$
> -i\sin(iz) = \sinh z, \qquad \cos(iz) = \cosh z . \qquad (4)
> $$
>
> Consequently $\sinh z$ and $\cosh z$ are periodic with period $2\pi i$.
>
> *B&C: Sec. 39, Equations (3) and (4)*

^prop-39-2

> [!proof]+ Proof
> By (1) and the definitions (1) of [[§37 The Trigonometric Functions sin z and cos z#^def-37-1|§37]], using $-\frac i2 = \frac{1}{2i}$:
>
> $$
> -i\sinh(iz) = -i\,\frac{e^{iz} - e^{-iz}}{2} = \frac{e^{iz} - e^{-iz}}{2i} = \sin z, \qquad \cosh(iz) = \frac{e^{iz} + e^{-iz}}{2} = \cos z ,
> $$
>
> $$
> -i\sin(iz) = -i\,\frac{e^{i(iz)} - e^{-i(iz)}}{2i} = -\frac{e^{-z} - e^{z}}{2} = \sinh z, \qquad \cos(iz) = \frac{e^{-z} + e^{z}}{2} = \cosh z .
> $$
>
> **Period.** By (4) and the period $2\pi$ of $\sin$ and $\cos$ ([[§37 The Trigonometric Functions sin z and cos z#^cor-37-4|Corollary §37.4]]), $\sinh(z + 2\pi i) = -i\sin(iz - 2\pi) = -i\sin(iz) = \sinh z$ and $\cosh(z + 2\pi i) = \cos(iz - 2\pi) = \cos(iz) = \cosh z$.

^pf-39-2

*Uses:* [[§39★ Hyperbolic Functions#^def-39-1|Def. §39.1]], [[§37 The Trigonometric Functions sin z and cos z#^def-37-1|Def. §37.1]], [[§37 The Trigonometric Functions sin z and cos z#^cor-37-4|§37.4]]

## Identities

> [!theorem] Proposition §39.3: Hyperbolic Identities
> For all complex $z$, $z_1$, $z_2$, and $z = x + iy$:
>
> $$
> \sinh(-z) = -\sinh z, \qquad \cosh(-z) = \cosh z , \qquad (5)
> $$
>
> $$
> \cosh^2z - \sinh^2z = 1 , \qquad (6)
> $$
>
> $$
> \sinh(z_1 + z_2) = \sinh z_1\cosh z_2 + \cosh z_1\sinh z_2 , \qquad (7)
> $$
>
> $$
> \cosh(z_1 + z_2) = \cosh z_1\cosh z_2 + \sinh z_1\sinh z_2 , \qquad (8)
> $$
>
> $$
> \sinh z = \sinh x\cos y + i\cosh x\sin y , \qquad (9)
> $$
>
> $$
> \cosh z = \cosh x\cos y + i\sinh x\sin y , \qquad (10)
> $$
>
> $$
> |\sinh z|^2 = \sinh^2x + \sin^2y , \qquad (11)
> $$
>
> $$
> |\cosh z|^2 = \sinh^2x + \cos^2y . \qquad (12)
> $$
>
> *B&C: Sec. 39, Equations (5)–(12)*

^prop-39-3

> [!proof]- Proof
> These follow directly from (1), but more easily from the trigonometric identities of [[§37 The Trigonometric Functions sin z and cos z|§37]] with the relations (3) and (4). Note that (4) gives $\sin(iz) = i\sinh z$, and (3) with $z$ real gives $\cosh(iy) = \cos y$ and $\sinh(iy) = i\sin y$.
>
> **(5)** Replacing $z$ by $-z$ in (1) interchanges $e^z$ and $e^{-z}$.
>
> **(6)** (B&C's Example 1.) Start from $\sin^2z + \cos^2z = 1$ (equation (9) of [[§37 The Trigonometric Functions sin z and cos z#^cor-37-4|§37]]). Using (3) to replace $\sin z$ and $\cos z$,
>
> $$
> -\sinh^2(iz) + \cosh^2(iz) = 1 .
> $$
>
> This holds for every $z$; replacing $z$ by $-iz$ (so that $iz$ becomes $z$) gives (6).
>
> **(7)** By (4), the addition formula (5) of §37, and (4) again,
>
> $$
> \sinh(z_1 + z_2) = -i\sin(iz_1 + iz_2) = -i\big[\sin(iz_1)\cos(iz_2) + \cos(iz_1)\sin(iz_2)\big] = \sinh z_1\cosh z_2 + \cosh z_1\sinh z_2 .
> $$
>
> **(8)** Likewise, with (6) of §37 and $\sin(iz_k) = i\sinh z_k$,
>
> $$
> \cosh(z_1 + z_2) = \cos(iz_1 + iz_2) = \cos(iz_1)\cos(iz_2) - \sin(iz_1)\sin(iz_2) = \cosh z_1\cosh z_2 - (i\sinh z_1)(i\sinh z_2) ,
> $$
>
> which is (8).
>
> **(9), (10)** Put $z_1 = x$, $z_2 = iy$ in (7) and (8) and use $\cosh(iy) = \cos y$, $\sinh(iy) = i\sin y$:
>
> $$
> \sinh(x + iy) = \sinh x\cos y + i\cosh x\sin y, \qquad \cosh(x + iy) = \cosh x\cos y + i\sinh x\sin y .
> $$
>
> **(11)** By (9) and (6) (for real $x$), $|\sinh z|^2 = \sinh^2x\cos^2y + \cosh^2x\sin^2y = \sinh^2x(1 - \sin^2y) + (1 + \sinh^2x)\sin^2y = \sinh^2x + \sin^2y$.
>
> **(12)** (B&C's Example 2, using the second relation (4).) Since $iz = i(x + iy) = -y + ix$,
>
> $$
> |\cosh z|^2 = |\cos(iz)|^2 = |\cos(-y + ix)|^2 .
> $$
>
> By (16) of [[§37 The Trigonometric Functions sin z and cos z#^prop-37-6|§37]], $|\cos(x + iy)|^2 = \cos^2x + \sinh^2y$, so $|\cos(-y + ix)|^2 = \cos^2(-y) + \sinh^2x = \cos^2y + \sinh^2x$, which is (12).

^pf-39-3

*Uses:* [[§39★ Hyperbolic Functions#^prop-39-2|§39.2]], [[§37 The Trigonometric Functions sin z and cos z#^thm-37-3|§37.3]], [[§37 The Trigonometric Functions sin z and cos z#^cor-37-4|§37.4]], [[§37 The Trigonometric Functions sin z and cos z#^prop-37-6|§37.6]]

## Zeros

The zeros are presented as a theorem, for comparison with [[§38 Zeros and Singularities of Trigonometric Functions#^thm-38-1|Theorem §38.1]] and because they matter in later chapters (poles of $\tanh z$ and $\operatorname{sech} z$).

> [!theorem] Theorem §39.4: Zeros of sinh z and cosh z
> The zeros of $\sinh z$ and $\cosh z$ in the complex plane all lie on the imaginary axis. To be specific,
>
> $$
> \sinh z = 0 \quad\text{if and only if}\quad z = n\pi i \quad (n = 0, \pm1, \pm2, \ldots)
> $$
>
> and
>
> $$
> \cosh z = 0 \quad\text{if and only if}\quad z = \Big(\frac\pi2 + n\pi\Big)i \quad (n = 0, \pm1, \pm2, \ldots) .
> $$
>
> *B&C: Sec. 39, Theorem*

^thm-39-4

> [!proof]+ Proof
> (B&C's Exercise 8: an immediate consequence of (4) and Theorem §38.1.) By (4), $\sinh z = -i\sin(iz)$, so $\sinh z = 0$ if and only if $\sin(iz) = 0$, that is, $iz = n\pi$, or $z = -n\pi i$; as $n$ runs through the integers so does $-n$, giving $z = n\pi i$. Similarly $\cosh z = \cos(iz) = 0$ if and only if $iz = \frac\pi2 + n\pi$, that is, $z = -\big(\frac\pi2 + n\pi\big)i = \big(\frac\pi2 + m\pi\big)i$ with $m = -n - 1$.

^pf-39-4

*Uses:* [[§39★ Hyperbolic Functions#^prop-39-2|§39.2]], [[§38 Zeros and Singularities of Trigonometric Functions#^thm-38-1|§38.1]]

## The Other Hyperbolic Functions

> [!definition] Definition §39.2: tanh, coth, sech, csch
> The **hyperbolic tangent** of $z$ is
>
> $$
> \tanh z = \frac{\sinh z}{\cosh z} , \qquad (16)
> $$
>
> analytic in every domain in which $\cosh z \ne 0$. The functions $\coth z$, $\operatorname{sech} z$ and $\operatorname{csch} z$ are the reciprocals of $\tanh z$, $\cosh z$ and $\sinh z$, respectively.
>
> *B&C: Sec. 39, Equation (16)*

^def-39-2

> [!theorem] Proposition §39.5: Derivatives of tanh, coth, sech, csch
> Where the functions are analytic,
>
> $$
> \frac{d}{dz}\tanh z = \operatorname{sech}^2z, \qquad \frac{d}{dz}\coth z = -\operatorname{csch}^2z , \qquad (17)
> $$
>
> $$
> \frac{d}{dz}\operatorname{sech} z = -\operatorname{sech} z\tanh z, \qquad \frac{d}{dz}\operatorname{csch} z = -\operatorname{csch} z\coth z . \qquad (18)
> $$
>
> These are the same as the formulas of calculus for a real variable.
>
> *B&C: Sec. 39, Equations (17) and (18)*

^prop-39-5

> [!proof]+ Proof
> (B&C's Exercise 11 and "straightforward to verify".) By the quotient rule, (2) and (6):
>
> $$
> \frac{d}{dz}\tanh z = \frac{\cosh^2z - \sinh^2z}{\cosh^2z} = \frac{1}{\cosh^2z}, \qquad \frac{d}{dz}\coth z = \frac{\sinh^2z - \cosh^2z}{\sinh^2z} = -\frac{1}{\sinh^2z} ,
> $$
>
> $$
> \frac{d}{dz}\frac{1}{\cosh z} = -\frac{\sinh z}{\cosh^2z} = -\operatorname{sech} z\tanh z, \qquad \frac{d}{dz}\frac{1}{\sinh z} = -\frac{\cosh z}{\sinh^2z} = -\operatorname{csch} z\coth z .
> $$

^pf-39-5

*Uses:* [[§39★ Hyperbolic Functions#^prop-39-1|§39.1]], [[§39★ Hyperbolic Functions#^prop-39-3|§39.3]], [[§20 Rules for Differentiation|§20]] (quotient rule)

## Examples

> [!example] Example §39.1: Zeros, Singularities and Period of tanh z
> **Zeros and singularities.** $\tanh z = \sinh z/\cosh z$ is analytic except where $\cosh z = 0$, and vanishes where $\sinh z = 0$ (the two never vanish together, by (6)). By Theorem §39.4 its zeros are $z = n\pi i$ and its singularities are $z = \big(\frac\pi2 + n\pi\big)i$ $(n = 0, \pm1, \pm2, \ldots)$, all on the imaginary axis.
>
> **Period $\pi i$.** By (4) and (10), (11) of [[§37 The Trigonometric Functions sin z and cos z#^cor-37-4|§37]],
>
> $$
> \sinh(z + \pi i) = -i\sin(iz - \pi) = i\sin(iz) = -\sinh z, \qquad \cosh(z + \pi i) = \cos(iz - \pi) = -\cosh z ,
> $$
>
> so $\tanh(z + \pi i) = \frac{-\sinh z}{-\cosh z} = \tanh z$.
>
> **Relation to $\tan$.** By (4), $\tanh z = \frac{-i\sin(iz)}{\cos(iz)} = -i\tan(iz)$, which turns the result just found into $\tan(w + \pi) = \tan w$ ([[§38 Zeros and Singularities of Trigonometric Functions#^prop-38-2|Proposition §38.2]]) with $w = iz$.
>
> *B&C: Sec. 39, Exercises 7, 9 and 10*

^ex-39-1

> [!example] Example §39.2: sinh z = i and cosh z = ½
> Use (9) and (10) and equate real and imaginary parts, as in [[§38 Zeros and Singularities of Trigonometric Functions#^ex-38-3|Example §38.3]].
>
> **(a)** $\sinh z = i$ means $\sinh x\cos y = 0$ and $\cosh x\sin y = 1$. If $\sinh x = 0$, then $x = 0$ and $\sin y = 1$, so $y = \frac\pi2 + 2n\pi$. If $\cos y = 0$, then $\sin y = \pm1$, and $\cosh x\sin y = 1$ with $\cosh x \ge 1$ forces $\sin y = 1$ and $\cosh x = 1$, so again $x = 0$, $y = \frac\pi2 + 2n\pi$. Hence
>
> $$
> z = \Big(2n + \frac12\Big)\pi i \qquad (n = 0, \pm1, \pm2, \ldots) .
> $$
>
> **(b)** $\cosh z = \frac12$ means $\cosh x\cos y = \frac12$ and $\sinh x\sin y = 0$. If $\sin y = 0$, then $\cos y = \pm1$ and $|\cosh x\cos y| = \cosh x \ge 1 > \frac12$: impossible. So $\sinh x = 0$, $x = 0$, and $\cos y = \frac12$, $y = \pm\frac\pi3 + 2n\pi$:
>
> $$
> z = \Big(2n \pm \frac13\Big)\pi i \qquad (n = 0, \pm1, \pm2, \ldots) .
> $$
>
> Both answers lie on the imaginary axis, where $\sinh(iy) = i\sin y$ and $\cosh(iy) = \cos y$.
>
> *B&C: Sec. 39, Exercise 16*

^ex-39-2

> [!example] Example §39.3: cosh z = −2
> By (10), $\cosh x\cos y = -2$ and $\sinh x\sin y = 0$. If $\sinh x = 0$, then $x = 0$ and $\cos y = -2$: impossible. So $\sin y = 0$, $y = n\pi$, $\cos y = (-1)^n$, and $(-1)^n\cosh x = -2$ forces $n$ odd and $\cosh x = 2$, that is, $x = \pm\cosh^{-1}2 = \pm\ln(2 + \sqrt3)$ ([[§24 Hyperbolic Functions#^thm-24-3|Calc Thm. §24.3]]). Hence
>
> $$
> z = \pm\ln(2 + \sqrt3) + (2n + 1)\pi i \qquad (n = 0, \pm1, \pm2, \ldots) .
> $$
>
> Compare $\cos z = 2$, whose roots are $z = 2n\pi \pm i\ln(2 + \sqrt3)$ (B&C Sec. 38, Exercise 16): since $\cosh z = \cos(iz)$, the equation $\cosh z = -2$ is $\cos(iz) = -2$, and the roots of $\cos w = -2$ are those of $\cos w = 2$ shifted by $\pi$ (by (11) of §37), $w = (2n + 1)\pi \pm i\ln(2 + \sqrt3)$; dividing by $i$ gives the list above.
>
> *B&C: Sec. 39, Exercise 17*

^ex-39-3
