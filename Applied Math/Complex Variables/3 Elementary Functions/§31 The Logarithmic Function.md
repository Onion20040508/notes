---
type: section
subject: "[[Complex Variables]]"
chapter: 3
section: 31
bc: "31"
aliases: ["B&C 31"]
tags: [complex-variables, math342]
---
← [[§30 The Exponential Function]] · ↑ [[· 3 Elementary Functions]] · [[§32 Examples (The Logarithmic Function)]] →

*Brown–Churchill, Section 31.*

The logarithm is defined by solving $e^w = z$. Because $e^w$ has period $2\pi i$, a nonzero $z$ has infinitely many logarithms, $\ln|z| + i\arg z$, one for each value of $\arg z$: $\log z$ is a *multiple-valued* function, and $e^{\log z} = z$ holds while $\log(e^z) = z$ holds only up to a multiple of $2\pi i$. Choosing $\operatorname{Arg} z$ gives the single-valued principal value $\operatorname{Log} z$, which reduces to $\ln x$ for $x > 0$. Branches, derivatives and identities follow in [[§33 Branches and Derivatives of Logarithms|§33]] and [[§34 Some Identities Involving Logarithms|§34]]; [[§32 Examples (The Logarithmic Function)|§32]] holds B&C's examples.

## Solving e^w = z

> [!theorem] Theorem §31.1: The Solutions of e^w = z
> Let $z$ be a nonzero complex number, $z = re^{i\Theta}$ with $r = |z|$ and $\Theta = \operatorname{Arg} z$ $(-\pi < \Theta \le \pi)$. Then
>
> $$
> e^w = z \qquad (1)
> $$
>
> holds if and only if $w$ has one of the values
>
> $$
> w = \ln r + i(\Theta + 2n\pi) \qquad (n = 0, \pm1, \pm2, \ldots) .
> $$
>
> For $z = 0$, equation (1) has no solution.
>
> *B&C: Sec. 31 (text)*

^thm-31-1

> [!proof]+ Proof
> Write $w = u + iv$. By [[§30 The Exponential Function#^def-30-1|Definition §30.1]], equation (1) becomes
>
> $$
> e^ue^{iv} = re^{i\Theta} .
> $$
>
> Both sides are exponential forms of nonzero numbers, with moduli $e^u$ and $r$. By [[§10 Roots of Complex Numbers#^prop-10-1|Proposition §10.1]] on the equality of two nonzero complex numbers in exponential form, this holds if and only if
>
> $$
> e^u = r \qquad\text{and}\qquad v = \Theta + 2n\pi
> $$
>
> for some integer $n$. Since $r > 0$, the equation $e^u = r$ is the same as $u = \ln r$. So (1) holds if and only if $w = \ln r + i(\Theta + 2n\pi)$ for some integer $n$. If $z = 0$, there is no solution because $e^w \ne 0$ ([[§30 The Exponential Function#^prop-30-1|Proposition §30.1]]).

^pf-31-1

*Uses:* [[§30 The Exponential Function#^def-30-1|Def. §30.1]], [[§30 The Exponential Function#^prop-30-1|§30.1]], [[§10 Roots of Complex Numbers#^prop-10-1|§10.1]], [[§6 Logarithmic and Inverse Trigonometric Functions#^cor-6-3|Calc Cor. §6.3]] ($e^u = r \iff u = \ln r$)

## The Logarithm and Its Principal Value

> [!definition] Definition §31.1: The Logarithmic Function
> The (multiple-valued) **logarithmic function** of a nonzero complex variable $z = re^{i\Theta}$ $(-\pi < \Theta \le \pi)$ is
>
> $$
> \log z = \ln r + i(\Theta + 2n\pi) \qquad (n = 0, \pm1, \pm2, \ldots) . \qquad (2)
> $$
>
> Equivalently, $\log z = \ln|z| + i\arg z$: the real part is the real logarithm of the modulus, and the imaginary parts are the arguments of $z$.
>
> *B&C: Sec. 31, Equation (2)*

^def-31-1

When $z = x > 0$, (2) becomes $\log x = \ln x + 2n\pi i$ $(n = 0, \pm1, \pm2, \ldots)$, and the identity (3) below reduces to the familiar identity of calculus

$$
e^{\ln x} = x \qquad (x > 0) . \qquad (4)
$$

That is what suggests (2) as the definition.

> [!remark]- Connections
> - The real logarithm and the identities $e^{\ln x} = x$, $\ln(e^x) = x$: [[§6 Logarithmic and Inverse Trigonometric Functions#^def-6-2|Calc Def. §6.2]], [[§6 Logarithmic and Inverse Trigonometric Functions#^cor-6-3|Calc Cor. §6.3]]; built from $\ln x = \int_1^x dt/t$ in [[§144 The Logarithm Defined as an Integral#^def-144-1|Calc Def. §144.1]]. On the positive real axis $\ln x$ is a single-valued inverse of $e^x$ because $e^x$ is one-to-one there; in the plane $e^z$ is not one-to-one (period $2\pi i$), and this is why $\log z$ is multiple-valued.

> [!theorem] Proposition §31.2: Exponential and Logarithm as Inverses
> For every nonzero $z$ and every value of $\log z$,
>
> $$
> e^{\log z} = z \qquad (z \ne 0) . \qquad (3)
> $$
>
> In the other order, for every $z$,
>
> $$
> \log(e^z) = z + 2n\pi i \qquad (n = 0, \pm1, \pm2, \ldots) , \qquad (5)
> $$
>
> meaning that the values of $\log(e^z)$ are exactly the numbers $z + 2n\pi i$; so $\log(e^z)$ is not just $z$.
>
> *B&C: Sec. 31, Equations (3) and (5)*

^prop-31-2

> [!proof]+ Proof
> **(3)** By Theorem §31.1, every value $w$ of $\log z$ in (2) solves $e^w = z$.
>
> **(5)** Write $z = x + iy$. By (2) in the form $\log\zeta = \ln|\zeta| + i\arg\zeta$, applied to $\zeta = e^z$, and by [[§30 The Exponential Function#^prop-30-1|Proposition §30.1]] ($|e^z| = e^x$, $\arg(e^z) = y + 2n\pi$),
>
> $$
> \log(e^z) = \ln|e^z| + i\arg(e^z) = \ln(e^x) + i(y + 2n\pi) = (x + iy) + 2n\pi i \qquad (n = 0, \pm1, \pm2, \ldots) .
> $$

^pf-31-2

*Uses:* [[§31 The Logarithmic Function#^thm-31-1|§31.1]], [[§31 The Logarithmic Function#^def-31-1|Def. §31.1]], [[§30 The Exponential Function#^prop-30-1|§30.1]]

> [!definition] Definition §31.2: Principal Value Log z
> The **principal value** of $\log z$ is the value obtained from (2) when $n = 0$, denoted $\operatorname{Log} z$:
>
> $$
> \operatorname{Log} z = \ln r + i\Theta \qquad (r = |z| > 0,\ \Theta = \operatorname{Arg} z) . \qquad (6)
> $$
>
> $\operatorname{Log} z$ is well defined and single-valued for $z \ne 0$, and
>
> $$
> \log z = \operatorname{Log} z + 2n\pi i \qquad (n = 0, \pm1, \pm2, \ldots) . \qquad (7)
> $$
>
> For $z = x > 0$, $\operatorname{Log} z = \ln x$: the principal value reduces to the logarithm of calculus.
>
> *B&C: Sec. 31, Equations (6) and (7)*

^def-31-2

$\operatorname{Log} z$ is defined at every $z \ne 0$, including the negative real axis (where $\Theta = \pi$), but it is not continuous there; the single-valued, analytic pieces of $\log z$ are the branches of [[§33 Branches and Derivatives of Logarithms#^def-33-1|Definition §33.1]].

> [!remark] Remark: Method — Computing log z and Log z
> 1. Find $r = |z|$ and the principal argument $\Theta = \operatorname{Arg} z$, with $-\pi < \Theta \le \pi$ (from a sketch: for $z = x + iy$ in the left half plane $\Theta$ is not $\tan^{-1}(y/x)$, but that angle shifted by $\pm\pi$).
> 2. All values: $\log z = \ln r + i(\Theta + 2n\pi)$. Any argument may be used in place of $\Theta$; the set of values is the same.
> 3. Principal value: $\operatorname{Log} z = \ln r + i\Theta$. Here it *matters* that $\Theta$ is the principal argument.
> 4. Check: $e^{\ln r + i\Theta} = re^{i\Theta} = z$.

^rem-31-1

## Examples

The worked examples of Sections 31–32 are in [[§32 Examples (The Logarithmic Function)|§32]]; the three below are from B&C's exercises and show the cases not covered there.

> [!example] Example §31.1: Principal Values Log(−ei) and Log(1 − i)
> **(a)** $-ei$ lies on the negative imaginary axis: $r = e$ and $\Theta = -\pi/2$. Hence
>
> $$
> \operatorname{Log}(-ei) = \ln e + i\Big(-\frac\pi2\Big) = 1 - \frac\pi2 i .
> $$
>
> **(b)** $1 - i$ lies in the fourth quadrant: $r = \sqrt2$ and $\Theta = -\pi/4$. Hence
>
> $$
> \operatorname{Log}(1 - i) = \ln\sqrt2 - \frac\pi4 i = \frac12\ln 2 - \frac\pi4 i .
> $$
>
> *B&C: Sec. 33, Exercise 1*

^ex-31-1

> [!example] Example §31.2: A Positive Number Has Infinitely Many Logarithms
> For $z = e$ we have $r = e$, $\Theta = 0$, so by (2)
>
> $$
> \log e = \ln e + i(0 + 2n\pi) = 1 + 2n\pi i \qquad (n = 0, \pm1, \pm2, \ldots) .
> $$
>
> Only one of these values is real, the principal value $\operatorname{Log} e = 1$, which is the calculus value $\ln e$. The others differ from it by multiples of $2\pi i$, as (7) says. Likewise, for $z = i$ ($r = 1$, $\Theta = \pi/2$),
>
> $$
> \log i = \ln 1 + i\Big(\frac\pi2 + 2n\pi\Big) = \Big(2n + \frac12\Big)\pi i \qquad (n = 0, \pm1, \pm2, \ldots) ,
> $$
>
> all pure imaginary, with $\operatorname{Log} i = \frac\pi2 i$.
>
> *B&C: Sec. 33, Exercise 2(a), (b)*

^ex-31-2

> [!example] Example §31.3: Solving log z = iπ/2
> Find all $z$ such that some value of $\log z$ equals $i\pi/2$.
>
> If $\log z = i\pi/2$ for one of its values, then by (3)
>
> $$
> z = e^{\log z} = e^{i\pi/2} = \cos\frac\pi2 + i\sin\frac\pi2 = i .
> $$
>
> Conversely, $i\pi/2 = \operatorname{Log} i$ is a value of $\log i$ (Example §31.2). So the only root is $z = i$. Exponentiating is the general method: the equation $\log z = w_0$ has exactly one root, $z = e^{w_0}$, for every $w_0$.
>
> *B&C: Sec. 33, Exercise 8*

^ex-31-3
