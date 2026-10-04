---
type: section
subject: "[[Complex Variables]]"
chapter: 3
section: 36
bc: "36"
aliases: ["B&C 36"]
tags: [complex-variables, math342]
---
← [[§35 The Power Function]] · ↑ [[· 3 Elementary Functions]] · [[§37 The Trigonometric Functions sin z and cos z]] →

*Brown–Churchill, Section 36 · MAT 342 HW 4.*

This section evaluates powers $z^c = e^{c\log z}$ ([[§35 The Power Function#^def-35-1|Definition §35.1]]). Imaginary powers can be real, and infinitely many: every value of $i^i$ is a positive real number. A rational power $z^{m/n}$ has finitely many values, and its principal branch is analytic on the plane cut along the negative real axis. Laws of exponents that combine different bases can fail for principal values, by a factor $e^{\pm 2\pi c i}$, because the principal logarithm of a product can be off by $\pm 2\pi i$ ([[§34 Some Identities Involving Logarithms#^ex-34-3|Example §34.3]]).

> [!remark] Remark: Method — Evaluating z^c
> 1. Compute all values of $\log z = \ln|z| + i(\Theta + 2n\pi)$ ([[§31 The Logarithmic Function#^rem-31-1|Remark: Method — Computing log z and Log z]]).
> 2. Multiply by $c$ and separate real and imaginary parts: $c\log z = X_n + iY_n$.
> 3. Then $z^c = e^{X_n}(\cos Y_n + i\sin Y_n)$. If $c$ is real, all values have the same modulus $|z|^c$; if $c$ is not real, the moduli $e^{X_n}$ change with $n$.
> 4. Count: for $c = m/n$ in lowest terms the values repeat with period $n$ in the index, so there are $n$ of them; for irrational or nonreal $c$ there are infinitely many.
> 5. The principal value takes $n = 0$ (that is, $\operatorname{Log} z$).

^rem-36-1

## Values of Powers

> [!example] Example §36.1: i^i Is Real
> Consider the power function $i^i = e^{i\log i}$. Since
>
> $$
> \log i = \ln 1 + i\Big(\frac\pi2 + 2n\pi\Big) = \Big(2n + \frac12\Big)\pi i \qquad (n = 0, \pm1, \pm2, \ldots) ,
> $$
>
> we have
>
> $$
> i^i = \exp\Big[i\Big(2n + \frac12\Big)\pi i\Big] = \exp\Big[-\Big(2n + \frac12\Big)\pi\Big] \qquad (n = 0, \pm1, \pm2, \ldots)
> $$
>
> and
>
> $$
> \text{P.V. } i^i = \exp\Big(-\frac\pi2\Big) \approx 0.2079 .
> $$
>
> The values of $i^i$ are all real numbers: $i \cdot i = -1$ turns the purely imaginary logarithm into a real exponent. They form a doubly infinite geometric sequence with ratio $e^{2\pi}$.
>
> *B&C: Sec. 36, Example 1*

^ex-36-1

> [!example] Example §36.2: (−1)^1/π and (−1)^i
> Recall $\log(-1) = \ln 1 + i(\pi + 2n\pi) = (2n + 1)\pi i$ $(n = 0, \pm1, \pm2, \ldots)$, [[§32 Examples (The Logarithmic Function)#^ex-32-2|Example §32.2]].
>
> **(a)** A real irrational exponent:
>
> $$
> (-1)^{1/\pi} = \exp\Big[\frac1\pi\log(-1)\Big] = \exp[(2n + 1)i] \qquad (n = 0, \pm1, \pm2, \ldots) .
> $$
>
> All values lie on the unit circle, at the angles $\pm1, \pm3, \pm5, \ldots$ radians; since $\pi$ is irrational, no two coincide.
>
> **(b)** An imaginary exponent:
>
> $$
> (-1)^i = \exp[i\log(-1)] = \exp[i(2n + 1)\pi i] = e^{-(2n + 1)\pi} \qquad (n = 0, \pm1, \pm2, \ldots) .
> $$
>
> The principal value exists, as for every power of a nonzero number: it uses $\operatorname{Log}(-1) = \pi i$ ($n = 0$), and $\text{P.V. } (-1)^i = e^{-\pi} \approx 0.0432$.
>
> *B&C: Sec. 36, Example 2; Source: 342 HW 4, Problem 1(c)*

^ex-36-2

> [!example] Example §36.3: Three Ways to (−1 + √3 i)^3/2
> **(a) By [[§35 The Power Function#^def-35-1|Definition §35.1]].** $-1 + \sqrt3\,i = 2e^{i2\pi/3}$, so $\log(-1 + \sqrt3\,i) = \ln 2 + i\big(\frac{2\pi}{3} + 2n\pi\big)$, and
>
> $$
> (-1 + \sqrt3\,i)^{3/2} = \exp\Big[\frac32\ln 2 + i(\pi + 3n\pi)\Big] = 2^{3/2}e^{i(3n + 1)\pi} = 2\sqrt2\,(-1)^{3n + 1} = \pm 2\sqrt2 ,
> $$
>
> with $-2\sqrt2$ for even $n$ (in particular the principal value, $n = 0$) and $+2\sqrt2$ for odd $n$.
>
> **(b) Square roots first.** The square roots of $2e^{i2\pi/3}$ are $\sqrt2\,e^{i(\pi/3 + k\pi)}$, $k = 0, 1$ ([[§10 Roots of Complex Numbers#^thm-10-2|Theorem §10.2]]). Cubing,
>
> $$
> \big[(-1 + \sqrt3\,i)^{1/2}\big]^3 = 2\sqrt2\,e^{i(\pi + 3k\pi)} = \mp 2\sqrt2 \qquad (k = 0, 1) .
> $$
>
> **(c) Cube first.** $(-1 + \sqrt3\,i)^3 = 2^3e^{i2\pi} = 8$, whose square roots are $\pm\sqrt8 = \pm 2\sqrt2$.
>
> All three give the same two values $\pm2\sqrt2$.
>
> *B&C: Sec. 36, Exercises 3 and 4; Source: 342 HW 4*

^ex-36-3

## The Principal Branch of z^2/3

> [!example] Example §36.4: The Principal Branch of z^2/3
> The principal branch of $z^{2/3}$ can be written
>
> $$
> \exp\Big(\frac23\operatorname{Log} z\Big) = \exp\Big(\frac23\ln r + \frac23 i\Theta\Big) = \sqrt[3]{r^2}\exp\Big(i\frac{2\Theta}{3}\Big) .
> $$
>
> Thus
>
> $$
> \text{P.V. } z^{2/3} = \sqrt[3]{r^2}\cos\frac{2\Theta}{3} + i\sqrt[3]{r^2}\sin\frac{2\Theta}{3} .
> $$
>
> This function is analytic in the domain $r > 0$, $-\pi < \Theta < \pi$. One can see this directly from [[§24★ Polar Coordinates#^thm-24-3|Theorem §24.3]]: with $u = r^{2/3}\cos\frac{2\Theta}{3}$ and $v = r^{2/3}\sin\frac{2\Theta}{3}$, the partial derivatives
>
> $$
> ru_r = \frac23 r^{2/3}\cos\frac{2\Theta}{3} = v_\Theta, \qquad u_\Theta = -\frac23 r^{2/3}\sin\frac{2\Theta}{3} = -rv_r
> $$
>
> are continuous and satisfy the polar Cauchy–Riemann equations throughout the domain. [[§35 The Power Function#^thm-35-2|Theorem §35.2]] also gives the derivative, $\frac{d}{dz}z^{2/3} = \frac23 z^{-1/3}$ (principal branches on both sides).
>
> *B&C: Sec. 36, Example 3*

^ex-36-4

## Laws of Exponents with Principal Values

While familiar laws of exponents used in calculus often carry over to complex analysis, there are exceptions when certain numbers are involved.

> [!example] Example §36.5: (z₁z₂)^i Versus z₁^i z₂^i
> Consider $z_1 = 1 + i$, $z_2 = 1 - i$, $z_3 = -1 - i$, and take principal values of all powers.
>
> **A case where the law holds.** Since $z_1z_2 = 2$,
>
> $$
> (z_1z_2)^i = 2^i = e^{i\operatorname{Log} 2} = e^{i(\ln 2 + i0)} = e^{i\ln 2} ,
> $$
>
> and
>
> $$
> z_1^i = e^{i\operatorname{Log}(1 + i)} = e^{i(\ln\sqrt2 + i\pi/4)} = e^{-\pi/4}e^{i(\ln 2)/2}, \qquad z_2^i = e^{i\operatorname{Log}(1 - i)} = e^{i(\ln\sqrt2 - i\pi/4)} = e^{\pi/4}e^{i(\ln 2)/2} .
> $$
>
> Thus
>
> $$
> (z_1z_2)^i = z_1^iz_2^i , \qquad (1)
> $$
>
> as might be expected.
>
> **A case where it fails.** Since $z_2z_3 = (1 - i)(-1 - i) = -2$,
>
> $$
> (z_2z_3)^i = (-2)^i = e^{i\operatorname{Log}(-2)} = e^{i(\ln 2 + i\pi)} = e^{-\pi}e^{i\ln 2}, \qquad z_3^i = e^{i\operatorname{Log}(-1 - i)} = e^{i(\ln\sqrt2 - i3\pi/4)} = e^{3\pi/4}e^{i(\ln 2)/2} .
> $$
>
> Hence
>
> $$
> (z_2z_3)^i = \big[e^{\pi/4}e^{i(\ln 2)/2}\big]\big[e^{3\pi/4}e^{i(\ln 2)/2}\big]e^{-2\pi}, \qquad\text{or}\qquad (z_2z_3)^i = z_2^iz_3^i\,e^{-2\pi} . \qquad (2)
> $$
>
> **Why.** In the first case $\operatorname{Arg} z_1 + \operatorname{Arg} z_2 = \frac\pi4 - \frac\pi4 = 0$, so $\operatorname{Log}(z_1z_2) = \operatorname{Log} z_1 + \operatorname{Log} z_2$. In the second, $\operatorname{Arg} z_2 + \operatorname{Arg} z_3 = -\frac\pi4 - \frac{3\pi}{4} = -\pi$, which is not a principal argument, and $\operatorname{Log}(z_2z_3) = \operatorname{Log} z_2 + \operatorname{Log} z_3 + 2\pi i$ ([[§34 Some Identities Involving Logarithms#^ex-34-3|Example §34.3]], $N = 1$). Multiplying by $i$ and exponentiating turns the extra $2\pi i$ into the factor $e^{i \cdot 2\pi i} = e^{-2\pi}$.
>
> *B&C: Sec. 36, Example 4*

^ex-36-5
