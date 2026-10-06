---
type: section
subject: "[[Complex Variables]]"
chapter: 3
section: 35
bc: "35"
aliases: ["B&C 35"]
tags: [complex-variables, math342]
---
← [[§34 Some Identities Involving Logarithms]] · ↑ [[· 3 Elementary Functions]] · [[§36 Examples (The Power Function)]] →

*Brown–Churchill, Section 35 · MAT 342 HW 4.*

A complex power is defined through the logarithm, $z^c = e^{c\log z}$, so it inherits the multiple values of $\log z$: one value when $c$ is an integer, $n$ values when $c = 1/n$, and in general infinitely many. Choosing a branch of $\log z$ gives a branch of $z^c$, analytic on the cut plane with the expected derivative $cz^{c - 1}$, and the principal branch uses $\operatorname{Log} z$. Reading the same formula with the roles exchanged defines exponentials $c^z = e^{z\log c}$ with any nonzero base. Examples are in [[§36 Examples (The Power Function)|§36]]; the power $z^{\pi/\alpha}$ that opens a wedge of angle $\alpha$ into a half plane is a basic tool of conformal mapping ([[§107★ Mappings by z²|§107★]], [[§121★ Temperatures in a Quadrant|§121★]]).

## The Power z^c

> [!definition] Definition §35.1: The Power Function
> When $z \ne 0$ and the exponent $c$ is any complex number, the **power function** $z^c$ is defined by
>
> $$
> z^c = e^{c\log z} \qquad (z \ne 0) . \qquad (1)
> $$
>
> Because of the logarithm, $z^c$ is in general multiple-valued: one value for each value of $\log z$.
>
> *B&C: Sec. 35, Equation (1)*

^def-35-1

Definition (1) is consistent with what is already known: it gives the usual $z^n$ when $c = n$ $(n = 0, \pm1, \pm2, \ldots)$, by [[§34 Some Identities Involving Logarithms#^prop-34-3|Proposition §34.3]], and the $n$th roots when $c = 1/n$ $(n = \pm1, \pm2, \ldots)$, by [[§34 Some Identities Involving Logarithms#^prop-34-4|Proposition §34.4]]. Definition (1) is in fact suggested by those particular choices of $c$.

> [!remark]- Connections
> - For a real base $b > 0$, calculus defines $b^x = e^{x\ln b}$, [[§121 The Logarithm Defined as an Integral#^def-121-5|Calc Def. §121.5]]. Definitions (1) and (4) below are the same formula with $\ln$ replaced by the multiple-valued $\log$, and their principal values restrict to it on the positive real axis, since $\operatorname{Log} x = \ln x$.

> [!theorem] Proposition §35.1: Reciprocal of a Power
> For $z \ne 0$,
>
> $$
> \frac{1}{z^c} = z^{-c} ,
> $$
>
> in the sense that each value of the left side, computed with a value of $\log z$, is the value of the right side computed with the same value of $\log z$.
>
> *B&C: Sec. 35 (text)*

^prop-35-1

> [!proof]+ Proof
> By $1/e^w = e^{-w}$ ([[§30 The Exponential Function#^thm-30-2|Theorem §30.2]]),
>
> $$
> \frac{1}{z^c} = \frac{1}{\exp(c\log z)} = \exp(-c\log z) = z^{-c} .
> $$

^pf-35-1

*Uses:* [[§35 The Power Function#^def-35-1|Def. §35.1]], [[§30 The Exponential Function#^thm-30-2|§30.2]]

When a specific branch ([[§33 Branches and Derivatives of Logarithms#^def-33-1|Definition §33.1]])

$$
\log z = \ln r + i\theta \qquad (r > 0,\ \alpha < \theta < \alpha + 2\pi)
$$

of the logarithm is used, $\log z$ is single-valued and analytic in the indicated domain. With that branch, the function (1) is single-valued and analytic in the same domain; it is called a **branch** of $z^c$ ([[§33 Branches and Derivatives of Logarithms#^def-33-2|Definition §33.2]]).

> [!theorem] Theorem §35.2: Derivative of a Branch of z^c
> When a branch $\log z = \ln r + i\theta$ $(r > 0,\ \alpha < \theta < \alpha + 2\pi)$ is used in (1), the function $z^c$ is single-valued and analytic in the domain $|z| > 0$, $\alpha < \arg z < \alpha + 2\pi$, and
>
> $$
> \frac{d}{dz}z^c = cz^{c - 1} \qquad (|z| > 0,\ \alpha < \arg z < \alpha + 2\pi) , \qquad (2)
> $$
>
> where $z^{c - 1}$ is computed with the same branch of $\log z$.
>
> *B&C: Sec. 35, Equation (2)*

^thm-35-2

> [!proof]+ Proof
> $z^c = \exp(c\log z)$ is the composition of the entire function $\exp$ with the function $c\log z$, which is single-valued and analytic in the domain ([[§33 Branches and Derivatives of Logarithms#^thm-33-1|Theorem §33.1]]). So it is single-valued and analytic there, and by the chain rule ([[§20 Rules for Differentiation#^thm-20-4|Theorem §20.4]]), $\frac{d}{dw}e^w = e^w$ and $\frac{d}{dz}\log z = \frac1z$,
>
> $$
> \frac{d}{dz}z^c = \frac{d}{dz}\exp(c\log z) = \frac cz\exp(c\log z) .
> $$
>
> Now recall that $z = \exp(\log z)$ ([[§31 The Logarithmic Function#^prop-31-2|Proposition §31.2]]). By (6) of [[§30 The Exponential Function#^thm-30-2|Theorem §30.2]],
>
> $$
> \frac{d}{dz}z^c = c\,\frac{\exp(c\log z)}{\exp(\log z)} = c\exp[(c - 1)\log z] = cz^{c - 1} .
> $$

^pf-35-2

*Uses:* [[§35 The Power Function#^def-35-1|Def. §35.1]], [[§33 Branches and Derivatives of Logarithms#^thm-33-1|§33.1]], [[§30 The Exponential Function#^thm-30-2|§30.2]], [[§30 The Exponential Function#^thm-30-3|§30.3]], [[§31 The Logarithmic Function#^prop-31-2|§31.2]], [[§20 Rules for Differentiation#^thm-20-4|§20.4]]

> [!definition] Definition §35.2: Principal Value and Principal Branch of z^c
> The **principal value** of $z^c$ occurs when $\log z$ is replaced by $\operatorname{Log} z$ in definition (1):
>
> $$
> \text{P.V. } z^c = e^{c\operatorname{Log} z} . \qquad (3)
> $$
>
> Equation (3) also defines the **principal branch** of $z^c$ on the domain $|z| > 0$, $-\pi < \operatorname{Arg} z < \pi$.
>
> *B&C: Sec. 35, Equation (3)*

^def-35-2

## Exponentials with Base c

> [!definition] Definition §35.3: Exponential Function with Base c
> According to definition (1), the **exponential function with base $c$**, where $c$ is any nonzero complex constant, is
>
> $$
> c^z = e^{z\log c} . \qquad (4)
> $$
>
> In general $c^z$ is multiple-valued, one function of $z$ for each value of $\log c$.
>
> *B&C: Sec. 35, Equation (4)*

^def-35-3

Although $e^z$ is, in general, multiple-valued according to (4), with values $e^{z(1 + 2n\pi i)}$ ([[§31 The Logarithmic Function#^ex-31-2|Example §31.2]]), the usual interpretation of $e^z$ ([[§30 The Exponential Function#^def-30-1|Definition §30.1]]) is the one obtained when the principal value of the logarithm is taken, because $\operatorname{Log} e = 1$.

> [!theorem] Proposition §35.3: Derivative of c^z
> When a value of $\log c$ is specified, $c^z$ is an entire function of $z$, and
>
> $$
> \frac{d}{dz}c^z = c^z\log c . \qquad (5)
> $$
>
> *B&C: Sec. 35, Equation (5)*

^prop-35-3

> [!proof]+ Proof
> With $\log c$ a fixed number, $z\log c$ is entire, and $c^z = e^{z\log c}$ is a composition of entire functions, hence entire. By the chain rule,
>
> $$
> \frac{d}{dz}c^z = \frac{d}{dz}e^{z\log c} = e^{z\log c}\log c = c^z\log c .
> $$

^pf-35-3

*Uses:* [[§35 The Power Function#^def-35-3|Def. §35.3]], [[§30 The Exponential Function#^thm-30-3|§30.3]], [[§20 Rules for Differentiation#^thm-20-4|§20.4]]

## Examples

B&C's examples of Section 35 are in [[§36 Examples (The Power Function)|§36]]. The examples below are its exercises on the definitions themselves.

> [!example] Example §35.1: The Principal nth Root Is the Principal Value of z^1/n
> Show that the principal $n$th root of a nonzero $z_0$ defined in [[§10 Roots of Complex Numbers#^def-10-new1|Definition §10.2]] is the principal value of $z_0^{1/n}$ defined by (3).
>
> Write $z_0 = r_0e^{i\Theta_0}$ with $\Theta_0 = \operatorname{Arg} z_0$. The principal root of [[§10 Roots of Complex Numbers#^def-10-new1|Definition §10.2]] is the root $c_0 = \sqrt[n]{r_0}\exp\big(i\frac{\Theta_0}{n}\big)$ (the one with $k = 0$). By (3) with $c = 1/n$ and $\operatorname{Log} z_0 = \ln r_0 + i\Theta_0$,
>
> $$
> \text{P.V. } z_0^{1/n} = \exp\Big(\frac1n\operatorname{Log} z_0\Big) = \exp\Big(\frac1n\ln r_0\Big)\exp\Big(i\frac{\Theta_0}{n}\Big) = \sqrt[n]{r_0}\exp\Big(i\frac{\Theta_0}{n}\Big) = c_0 .
> $$
>
> It matters that $\Theta_0$ is the *principal* argument on both sides; with another argument $\Theta_0 + 2k\pi$ one gets the other roots $c_k$.
>
> *B&C: Sec. 36, Exercise 5; Source: 342 HW 4*

^ex-35-1

> [!example] Example §35.2: Moduli of Powers
> **(a)** If $z \ne 0$ and $a$ is real, then $|z^a| = \exp(a\ln|z|) = |z|^a$, for every value of $z^a$, where the principal value of $|z|^a$ is taken. Indeed, $z^a = \exp(a\ln|z| + ia\theta)$ for some argument $\theta$, and by [[§30 The Exponential Function#^prop-30-1|Proposition §30.1]] its modulus is $\exp(a\ln|z|)$, because $a\theta$ is real. And the principal value of $|z|^a$ is $\exp(a\operatorname{Log}|z|) = \exp(a\ln|z|)$.
>
> **(b)** For complex $c = a + bi$ $(c \ne 0, \pm1, \pm2, \ldots$, so that $i^c$ is multiple-valued$)$, the values of $|i^c|$ are all the same if and only if $c$ is real. With $\log i = \big(2n + \frac12\big)\pi i$,
>
> $$
> i^c = \exp\Big[(a + bi)\Big(2n + \frac12\Big)\pi i\Big] = \exp\Big[-b\Big(2n + \frac12\Big)\pi\Big]\exp\Big[ia\Big(2n + \frac12\Big)\pi\Big] ,
> $$
>
> so $|i^c| = \exp\big[-b\big(2n + \frac12\big)\pi\big]$, which is independent of $n$ exactly when $b = 0$.
>
> *B&C: Sec. 36, Exercises 6 and 7*

^ex-35-2

> [!example] Example §35.3: Laws of Exponents for Principal Values
> Let $z \ne 0$ and let all powers be principal values. Then
>
> $$
> \text{(a) } z^{c_1}z^{c_2} = z^{c_1 + c_2}, \qquad \text{(b) } \frac{z^{c_1}}{z^{c_2}} = z^{c_1 - c_2}, \qquad \text{(c) } (z^c)^n = z^{cn} \quad (n = 1, 2, \ldots) .
> $$
>
> All three use one and the same number $\operatorname{Log} z$ on both sides. (a) By (3) and (5) of [[§30 The Exponential Function#^thm-30-2|Theorem §30.2]], $z^{c_1}z^{c_2} = e^{c_1\operatorname{Log} z}e^{c_2\operatorname{Log} z} = e^{(c_1 + c_2)\operatorname{Log} z} = z^{c_1 + c_2}$. (b) Likewise by (6) of that theorem. (c) By induction on $n$ with (a): $(z^c)^{n + 1} = (z^c)^nz^c = z^{cn}z^c = z^{c(n + 1)}$.
>
> Contrast: laws in which *different* numbers are raised to a power can fail for principal values, because $\operatorname{Log}(z_1z_2)$ need not be $\operatorname{Log} z_1 + \operatorname{Log} z_2$; see [[§36 Examples (The Power Function)#^ex-36-5|Example §36.5]].
>
> *B&C: Sec. 36, Exercise 8*

^ex-35-3

> [!example] Example §35.4: The Derivative of c^f(z)
> If $f'(z)$ exists and a value of $\log c$ is fixed, then $c^{f(z)} = e^{f(z)\log c}$ and, by the chain rule and (5),
>
> $$
> \frac{d}{dz}c^{f(z)} = e^{f(z)\log c}\,f'(z)\log c = c^{f(z)}f'(z)\log c .
> $$
>
> For example, with the principal value $\operatorname{Log} 2 = \ln 2$, $\frac{d}{dz}2^{z^2} = 2z\ln 2\cdot 2^{z^2}$.
>
> *B&C: Sec. 36, Exercise 9*

^ex-35-4
