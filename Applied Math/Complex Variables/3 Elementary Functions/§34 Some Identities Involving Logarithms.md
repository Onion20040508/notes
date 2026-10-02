---
type: section
subject: "[[Complex Variables]]"
chapter: 3
section: 34
bc: "34"
aliases: ["B&C 34"]
tags: [complex-variables, math342]
---
← [[§33 Branches and Derivatives of Logarithms]] · ↑ [[· 3 Elementary Functions]] · [[§35 The Power Function]] →

*Brown–Churchill, Section 34 · MAT 342 HW 4.*

The laws $\log(z_1z_2) = \log z_1 + \log z_2$ and $\log(z_1/z_2) = \log z_1 - \log z_2$ hold for the multiple-valued logarithm, read as statements about sets of values exactly like $\arg(z_1z_2) = \arg z_1 + \arg z_2$ in [[§9 Arguments of Products and Quotients#^thm-9-1|Theorem §9.1]]. With principal values they can fail, by $\pm 2\pi i$, and the error is controlled exactly. The section also expresses integer powers and $n$th roots through the logarithm, $z^n = e^{n\log z}$ and $z^{1/n} = \exp\big(\frac1n\log z\big)$, which is what suggests the definition $z^c = e^{c\log z}$ of the general power, [[§35 The Power Function#^def-35-1|Definition §35.1]].

## Products and Quotients

> [!theorem] Theorem §34.1: The Logarithm of a Product
> If $z_1$ and $z_2$ are any two nonzero complex numbers, then
>
> $$
> \log(z_1z_2) = \log z_1 + \log z_2 , \qquad (1)
> $$
>
> interpreted in the same way as the statement
>
> $$
> \arg(z_1z_2) = \arg z_1 + \arg z_2 \qquad (2)
> $$
>
> of [[§9 Arguments of Products and Quotients#^thm-9-1|Theorem §9.1]]: if values of two of the three logarithms are specified, then there is a value of the third such that (1) holds.
>
> *B&C: Sec. 34, Equation (1)*

^thm-34-1

> [!proof]+ Proof
> Since $|z_1z_2| = |z_1||z_2|$ and these moduli are positive real numbers, the real logarithm gives
>
> $$
> \ln|z_1z_2| = \ln|z_1| + \ln|z_2| .
> $$
>
> Combining this with (2),
>
> $$
> \ln|z_1z_2| + i\arg(z_1z_2) = \big(\ln|z_1| + i\arg z_1\big) + \big(\ln|z_2| + i\arg z_2\big) . \qquad (3)
> $$
>
> The three bracketed expressions are $\log(z_1z_2)$, $\log z_1$ and $\log z_2$ ([[§31 The Logarithmic Function#^def-31-1|Definition §31.1]]), and the real parts in (3) match exactly, so (3) is (1) with the same meaning as (2). In detail: if values $\ln|z_1| + i\theta_1$ and $\ln|z_2| + i\theta_2$ of $\log z_1$ and $\log z_2$ are specified, then by (2) $\theta_1 + \theta_2$ is a value of $\arg(z_1z_2)$, so $\ln|z_1z_2| + i(\theta_1 + \theta_2)$ is a value of $\log(z_1z_2)$ satisfying (1). If instead values $\ln|z_1z_2| + i\varphi$ of $\log(z_1z_2)$ and $\ln|z_1| + i\theta_1$ of $\log z_1$ are specified, then by (2) $\varphi - \theta_1$ is a value of $\arg z_2$, and $\ln|z_2| + i(\varphi - \theta_1)$ is the required value of $\log z_2$; the remaining case is symmetric.

^pf-34-1

*Uses:* [[§31 The Logarithmic Function#^def-31-1|Def. §31.1]], [[§9 Arguments of Products and Quotients#^thm-9-1|§9.1]], [[§5 Inverse Functions and Logarithms#^thm-5-5|Calc Thm. §5.5]] (laws of logarithms)

> [!remark]- Connections
> - The real law $\ln(xy) = \ln x + \ln y$: [[§5 Inverse Functions and Logarithms#^thm-5-5|Calc Thm. §5.5]], proved rigorously from $\ln x = \int_1^x dt/t$ in [[§121 The Logarithm Defined as an Integral#^thm-121-2|Calc Thm. §121.2]]. Theorem §34.1 is that law for the moduli plus the addition of arguments, [[§53 Complex Numbers#^thm-53-5|235 Thm. §53.5]] (the product has the sum of the arguments, "possibly shifted by $\pm2\pi$").

> [!theorem] Theorem §34.2: The Logarithm of a Quotient
> If $z_1$ and $z_2$ are nonzero, then
>
> $$
> \log\Big(\frac{z_1}{z_2}\Big) = \log z_1 - \log z_2 , \qquad (4)
> $$
>
> interpreted in the same way as (1).
>
> *B&C: Sec. 34, Equation (4)*

^thm-34-2

> [!proof]+ Proof
> B&C leaves this to the exercises (Exercise 2(a)); here is the argument. Since $|z_1/z_2| = |z_1|/|z_2|$, $\ln|z_1/z_2| = \ln|z_1| - \ln|z_2|$. By [[§9 Arguments of Products and Quotients#^cor-9-2|Corollary §9.2]], $\arg(z_1/z_2) = \arg z_1 - \arg z_2$, in the same sense as (2). Hence
>
> $$
> \ln\Big|\frac{z_1}{z_2}\Big| + i\arg\Big(\frac{z_1}{z_2}\Big) = \big(\ln|z_1| + i\arg z_1\big) - \big(\ln|z_2| + i\arg z_2\big) ,
> $$
>
> which is (4), read exactly as (3) was read in the proof of Theorem §34.1.

^pf-34-2

*Uses:* [[§31 The Logarithmic Function#^def-31-1|Def. §31.1]], [[§9 Arguments of Products and Quotients#^cor-9-2|§9.2]], [[§34 Some Identities Involving Logarithms#^thm-34-1|§34.1]]

> [!example] Example §34.1: z₁ = z₂ = −1
> Take $z_1 = z_2 = -1$, so $z_1z_2 = 1$. By [[§32 Examples (The Logarithmic Function)#^ex-32-2|Example §32.2]], $\log 1 = 2n\pi i$ and $\log(-1) = (2n + 1)\pi i$ $(n = 0, \pm1, \pm2, \ldots)$.
>
> **Equation (1) holds.** Specify $\log(z_1z_2) = 0$ and $\log z_1 = \pi i$. Then (1) is satisfied when the value $\log z_2 = -\pi i$ is chosen: $0 = \pi i + (-\pi i)$.
>
> **Principal values fail.** If principal values are used in all three terms,
>
> $$
> \operatorname{Log}(z_1z_2) = \operatorname{Log} 1 = 0 \qquad\text{and}\qquad \operatorname{Log} z_1 + \operatorname{Log} z_2 = \pi i + \pi i = 2\pi i .
> $$
>
> So statement (1) is not always true when principal values are used in all three terms.
>
> *B&C: Sec. 34, Example 1*

^ex-34-1

> [!example] Example §34.2: Principal Values in the Right Half Plane
> Let $z_1$ and $z_2$ be nonzero complex numbers to the right of the imaginary axis, $\operatorname{Re} z_1 > 0$ and $\operatorname{Re} z_2 > 0$. Then
>
> $$
> \operatorname{Log}(z_1z_2) = \operatorname{Log} z_1 + \operatorname{Log} z_2 .
> $$
>
> Indeed, $z_1 = r_1\exp(i\Theta_1)$ and $z_2 = r_2\exp(i\Theta_2)$ with
>
> $$
> -\frac\pi2 < \Theta_1 < \frac\pi2 \qquad\text{and}\qquad -\frac\pi2 < \Theta_2 < \frac\pi2 .
> $$
>
> The important point is that then $-\pi < \Theta_1 + \Theta_2 < \pi$. Since $\Theta_1 + \Theta_2$ is an argument of $z_1z_2$ ([[§9 Arguments of Products and Quotients#^thm-9-1|Theorem §9.1]]) and lies in $(-\pi, \pi]$, it is the principal one: $\operatorname{Arg}(z_1z_2) = \Theta_1 + \Theta_2$. Consequently
>
> $$
> \operatorname{Log}(z_1z_2) = \ln|z_1z_2| + i\operatorname{Arg}(z_1z_2) = \ln(r_1r_2) + i(\Theta_1 + \Theta_2) = (\ln r_1 + i\Theta_1) + (\ln r_2 + i\Theta_2) = \operatorname{Log} z_1 + \operatorname{Log} z_2 .
> $$
>
> *B&C: Sec. 34, Example 2*

^ex-34-2

> [!example] Example §34.3: How Much Can Log(z₁z₂) Differ from Log z₁ + Log z₂?
> Show that for any two nonzero $z_1$, $z_2$,
>
> $$
> \operatorname{Log}(z_1z_2) = \operatorname{Log} z_1 + \operatorname{Log} z_2 + 2N\pi i ,
> $$
>
> where $N$ is one of $0, \pm1$, and find $N$.
>
> Write $z_1 = r_1e^{i\Theta_1}$, $z_2 = r_2e^{i\Theta_2}$ with $-\pi < \Theta_1, \Theta_2 \le \pi$. Then $\Theta_1 + \Theta_2$ is an argument of $z_1z_2$, and
>
> $$
> -2\pi < \Theta_1 + \Theta_2 \le 2\pi .
> $$
>
> The principal argument is the unique argument in $(-\pi, \pi]$, so $\operatorname{Arg}(z_1z_2) = \Theta_1 + \Theta_2 + 2N\pi$, where $N$ is the integer that brings $\Theta_1 + \Theta_2$ into $(-\pi, \pi]$:
>
> $$
> N = \begin{cases} 1, & -2\pi < \Theta_1 + \Theta_2 \le -\pi, \\ 0, & -\pi < \Theta_1 + \Theta_2 \le \pi, \\ -1, & \pi < \Theta_1 + \Theta_2 \le 2\pi. \end{cases}
> $$
>
> Hence
>
> $$
> \operatorname{Log}(z_1z_2) = \ln(r_1r_2) + i(\Theta_1 + \Theta_2 + 2N\pi) = \operatorname{Log} z_1 + \operatorname{Log} z_2 + 2N\pi i .
> $$
>
> The endpoints matter: for $z_1 = z_2 = -i$, $\Theta_1 + \Theta_2 = -\pi$, and $z_1z_2 = -1$ has $\operatorname{Arg} = \pi$, so $N = 1$: $\operatorname{Log}(-1) = \pi i = -\frac\pi2 i - \frac\pi2 i + 2\pi i$. In Example §34.1, $\Theta_1 + \Theta_2 = 2\pi$ and $N = -1$; in Example §34.2, $N = 0$.
>
> *B&C: Sec. 34, Exercise 1; Source: 342 HW 4*

^ex-34-3

## Integer Powers and Roots

Two further properties of $\log z$ prepare the power function of [[§35 The Power Function#^def-35-1|Definition §35.1]].

> [!theorem] Proposition §34.3: Integer Powers
> If $z$ is a nonzero complex number, then
>
> $$
> z^n = e^{n\log z} \qquad (n = 0, \pm1, \pm2, \ldots) \qquad (5)
> $$
>
> for any value of $\log z$ that is taken. When $n = 1$ this is $e^{\log z} = z$, [[§31 The Logarithmic Function#^prop-31-2|Proposition §31.2]].
>
> *B&C: Sec. 34, Equation (5)*

^prop-34-3

> [!proof]+ Proof
> Write $z = re^{i\theta}$, where $\theta$ is the argument used in the chosen value $\log z = \ln r + i\theta$. Then $n\log z = n\ln r + in\theta$, and by [[§30 The Exponential Function#^def-30-1|Definition §30.1]]
>
> $$
> e^{n\log z} = e^{n\ln r}e^{in\theta} = r^ne^{in\theta} ,
> $$
>
> since $e^{n\ln r} = (e^{\ln r})^n = r^n$ for real $r > 0$. On the other hand $z^n = (re^{i\theta})^n = r^ne^{in\theta}$ for every integer $n$ ([[§8 Products and Powers in Exponential Form#^thm-8-2|Theorem §8.2]]). The two sides agree.

^pf-34-3

*Uses:* [[§30 The Exponential Function#^def-30-1|Def. §30.1]], [[§8 Products and Powers in Exponential Form#^thm-8-2|§8.2]], [[§121 The Logarithm Defined as an Integral#^thm-121-6|Calc Thm. §121.6]]

> [!theorem] Proposition §34.4: Roots
> If $z \ne 0$, then
>
> $$
> z^{1/n} = \exp\Big(\frac1n\log z\Big) \qquad (n = 1, 2, \ldots) . \qquad (6)
> $$
>
> That is, the right side has exactly $n$ distinct values, and they are the $n$th roots of $z$. The property is also valid when $n$ is a negative integer.
>
> *B&C: Sec. 34, Equation (6); Exercise 4*

^prop-34-4

> [!proof]+ Proof
> Write $z = r\exp(i\Theta)$, where $\Theta = \operatorname{Arg} z$. By the definition (2) of $\log z$, [[§31 The Logarithmic Function#^def-31-1|Definition §31.1]],
>
> $$
> \exp\Big(\frac1n\log z\Big) = \exp\Big[\frac1n\ln r + \frac{i(\Theta + 2k\pi)}{n}\Big] \qquad (k = 0, \pm1, \pm2, \ldots) .
> $$
>
> Thus, since $e^{\frac1n\ln r} = \sqrt[n]{r}$ (the positive root),
>
> $$
> \exp\Big(\frac1n\log z\Big) = \sqrt[n]{r}\exp\Big[i\Big(\frac\Theta n + \frac{2k\pi}{n}\Big)\Big] \qquad (k = 0, \pm1, \pm2, \ldots) . \qquad (7)
> $$
>
> The factor $\exp(i2k\pi/n)$ depends only on the remainder of $k$ on division by $n$, and takes distinct values for $k = 0, 1, \ldots, n - 1$; so the right side of (7) has exactly $n$ values. It is the expression for the $n$th roots of $z$ found in [[§10 Roots of Complex Numbers#^thm-10-2|Theorem §10.2]], so it can be written $z^{1/n}$. This is (6).
>
> **Negative $n$.** (B&C's Exercise 4.) Let $n = -m$ with $m = 1, 2, \ldots$; here $z^{1/n}$ means $(z^{1/m})^{-1}$, the set of reciprocals of the $m$th roots (B&C's convention in Sec. 11, Exercise 9, extending [[§10 Roots of Complex Numbers#^def-10-1|Definition §10.1]]). By [[§30 The Exponential Function#^thm-30-2|Theorem §30.2]], $1/e^w = e^{-w}$, so for each value of $\log z$
>
> $$
> \exp\Big(\frac1n\log z\Big) = \exp\Big(-\frac1m\log z\Big) = \Big[\exp\Big(\frac1m\log z\Big)\Big]^{-1} ,
> $$
>
> and as $\log z$ runs through its values, the bracket runs through the $m$th roots of $z$, by the case already proved. So the left side runs through $(z^{1/m})^{-1} = z^{1/n}$.

^pf-34-4

*Uses:* [[§31 The Logarithmic Function#^def-31-1|Def. §31.1]], [[§30 The Exponential Function#^def-30-1|Def. §30.1]], [[§30 The Exponential Function#^thm-30-2|§30.2]], [[§10 Roots of Complex Numbers#^thm-10-2|§10.2]], [[§10 Roots of Complex Numbers#^def-10-1|Def. §10.1]]

> [!example] Example §34.4: log(z^1/n) = (1/n) log z
> Let $z = re^{i\Theta}$ $(-\pi < \Theta \le \pi)$ and let $n$ be a positive integer. Show that the set of values of $\log(z^{1/n})$ is the set of values of $\frac1n\log z$. (For $z = i$, $n = 2$ this is [[§32 Examples (The Logarithmic Function)#^ex-32-4|Example §32.4]](a).)
>
> **The left side.** The $n$th roots of $z$ are $c_k = \sqrt[n]{r}\exp\big[i\frac{\Theta + 2k\pi}{n}\big]$, $k = 0, 1, \ldots, n - 1$. The number $\frac{\Theta + 2k\pi}{n}$ is an argument of $c_k$, and adding multiples of $2\pi = \frac{2pn\pi}{n}$ gives all of them, so
>
> $$
> \log c_k = \frac1n\ln r + i\frac{\Theta + 2(pn + k)\pi}{n} \qquad (p = 0, \pm1, \pm2, \ldots) .
> $$
>
> Hence all values of $\log(z^{1/n})$ are
>
> $$
> \log(z^{1/n}) = \frac1n\ln r + i\frac{\Theta + 2(pn + k)\pi}{n} \qquad (p = 0, \pm1, \pm2, \ldots;\ k = 0, 1, \ldots, n - 1) .
> $$
>
> **The right side.** $\frac1n\log z = \frac1n\ln r + i\frac{\Theta + 2q\pi}{n}$ $(q = 0, \pm1, \pm2, \ldots)$.
>
> **Comparison.** Every integer $q$ can be written uniquely as $q = pn + k$ with $p$ an integer and $k \in \{0, 1, \ldots, n - 1\}$ (division with remainder), and every such $pn + k$ is an integer. So the two sets of values coincide:
>
> $$
> \log(z^{1/n}) = \frac1n\log z ,
> $$
>
> where, corresponding to a value of $\log(z^{1/n})$ taken on the left, the appropriate value of $\log z$ is to be selected on the right, and conversely.
>
> *B&C: Sec. 34, Exercise 5*

^ex-34-4
