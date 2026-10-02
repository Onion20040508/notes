---
type: section
subject: "[[Complex Variables]]"
chapter: 3
section: 32
bc: "32"
aliases: ["B&C 32"]
tags: [complex-variables, math342]
---
← [[§31 The Logarithmic Function]] · ↑ [[· 3 Elementary Functions]] · [[§33 Branches and Derivatives of Logarithms]] →

*Brown–Churchill, Section 32 · MAT 342 HW 4.*

This section computes logarithms with [[§31 The Logarithmic Function#^def-31-1|Definition §31.1]] and [[§31 The Logarithmic Function#^def-31-2|Definition §31.2]] and tests which laws of the real logarithm survive. Negative numbers now have logarithms, $\log(-1) = (2n + 1)\pi i$. The identity $\ln(x^k) = k\ln x$ survives only in part: $\operatorname{Log}(z^2) = 2\operatorname{Log} z$ can fail because doubling a principal argument can leave the interval $(-\pi, \pi]$, and for the multiple-valued $\log$ the sets $\log(i^2)$ and $2\log i$ differ, while $\log(i^{1/2})$ and $\frac12\log i$ agree. The general rules behind these examples are in [[§34 Some Identities Involving Logarithms|§34]].

## Values of log z

The method is [[§31 The Logarithmic Function#^rem-31-1|Remark: Method — Computing log z and Log z]].

> [!example] Example §32.1: Logarithms of Points Below the Real Axis
> **(a)** If $z = -1 - \sqrt3\,i$, then $r = 2$ and $\Theta = -2\pi/3$ (third quadrant, so not $\tan^{-1}\sqrt3 = \pi/3$ but $\pi/3 - \pi$). Hence
>
> $$
> \log(-1 - \sqrt3\,i) = \ln 2 + i\Big(-\frac{2\pi}{3} + 2n\pi\Big) = \ln 2 + 2\Big(n - \frac13\Big)\pi i \qquad (n = 0, \pm1, \pm2, \ldots) .
> $$
>
> **(b)** $z = 1 - \sqrt3\,i = 2e^{-i\pi/3}$: $r = 2$, $\Theta = -\pi/3$. So
>
> $$
> \log(1 - \sqrt3\,i) = \ln 2 + i\Big(-\frac\pi3 + 2n\pi\Big) \quad (n = 0, \pm1, \pm2, \ldots), \qquad \operatorname{Log}(1 - \sqrt3\,i) = \ln 2 - \frac\pi3 i .
> $$
>
> **(c)** $z = -1 - i = \sqrt2\,e^{-i3\pi/4}$: $r = \sqrt2$, $\Theta = -3\pi/4$. So
>
> $$
> \log(-1 - i) = \frac12\ln 2 + i\Big(-\frac{3\pi}{4} + 2n\pi\Big) \quad (n = 0, \pm1, \pm2, \ldots), \qquad \operatorname{Log}(-1 - i) = \frac12\ln 2 - \frac{3\pi}{4} i .
> $$
>
> In (c) the angle $5\pi/4$ is also an argument of $-1 - i$ and gives a value of $\log(-1 - i)$ (the one with $n = 1$), but not the principal value, since $5\pi/4 > \pi$. It is the value of the branch with $0 < \theta < 2\pi$, [[§33 Branches and Derivatives of Logarithms#^ex-33-2|Example §33.2]].
>
> *B&C: Sec. 32, Example 1; Source: 342 HW 4, Problem 1(a) and first part of 1(b)*

^ex-32-1

> [!example] Example §32.2: log 1 and log(−1)
> **(a)** For $z = 1$: $r = 1$, $\Theta = 0$, so
>
> $$
> \log 1 = \ln 1 + i(0 + 2n\pi) = 2n\pi i \qquad (n = 0, \pm1, \pm2, \ldots) .
> $$
>
> As anticipated, $\operatorname{Log} 1 = 0$.
>
> **(b)** Calculus has no logarithm of a negative number, but now there are infinitely many. For $z = -1$: $r = 1$, $\Theta = \pi$, so
>
> $$
> \log(-1) = \ln 1 + i(\pi + 2n\pi) = (2n + 1)\pi i \qquad (n = 0, \pm1, \pm2, \ldots) ,
> $$
>
> and $\operatorname{Log}(-1) = \pi i$. All values are pure imaginary, because $|-1| = 1$.
>
> *B&C: Sec. 32, Examples 2 and 3*

^ex-32-2

## Which Laws of Logarithms Survive

Special care must be taken in expecting familiar properties of $\ln x$ to carry over to $\log z$ and $\operatorname{Log} z$.

> [!example] Example §32.3: Log of a Power with Principal Values
> **(a)** The identity
>
> $$
> \operatorname{Log}[(1 + i)^2] = 2\operatorname{Log}(1 + i) \qquad (1)
> $$
>
> is valid, since $(1 + i)^2 = 2i$ and
>
> $$
> \operatorname{Log}[(1 + i)^2] = \operatorname{Log}(2i) = \ln 2 + i\frac\pi2, \qquad 2\operatorname{Log}(1 + i) = 2\Big(\ln\sqrt2 + i\frac\pi4\Big) = \ln 2 + i\frac\pi2 .
> $$
>
> **(b)** On the other hand,
>
> $$
> \operatorname{Log}[(-1 + i)^2] \ne 2\operatorname{Log}(-1 + i) , \qquad (2)
> $$
>
> because $(-1 + i)^2 = -2i$ and
>
> $$
> \operatorname{Log}[(-1 + i)^2] = \operatorname{Log}(-2i) = \ln 2 - i\frac\pi2, \qquad 2\operatorname{Log}(-1 + i) = 2\Big(\ln\sqrt2 + i\frac{3\pi}{4}\Big) = \ln 2 + i\frac{3\pi}{2} .
> $$
>
> The two sides differ by $2\pi i$: twice the principal argument $3\pi/4$ is $3\pi/2$, an argument of $-2i$ but not the principal one.
>
> **(c)** The same happens with a cube: $i^3 = -i$, so
>
> $$
> \operatorname{Log}(i^3) = \operatorname{Log}(-i) = \ln 1 - \frac\pi2 i = -\frac\pi2 i, \qquad 3\operatorname{Log} i = 3\Big(\ln 1 + \frac\pi2 i\Big) = \frac{3\pi}{2}i ,
> $$
>
> and $\operatorname{Log}(i^3) \ne 3\operatorname{Log} i$.
>
> In general $k\operatorname{Log} z$ is *a* value of $\log(z^k)$ (its imaginary part $k\operatorname{Arg} z$ is an argument of $z^k$), and it is the principal value exactly when $-\pi < k\operatorname{Arg} z \le \pi$.
>
> *B&C: Sec. 32, Example 4; Sec. 33, Exercise 3; Source: 342 HW 4 (optional problems)*

^ex-32-3

For the multiple-valued $\log$, an identity between two multiple-valued expressions means that the two *sets* of values are the same.

> [!example] Example §32.4: log(i^1/2) = ½ log i, but log(i²) ≠ 2 log i
> **(a)** The two square roots of $i = e^{i\pi/2}$ are $e^{i\pi/4}$ and $e^{i5\pi/4}$ ([[§10 Roots of Complex Numbers#^thm-10-2|Theorem §10.2]]: $e^{i(\pi/2 + 2k\pi)/2}$, $k = 0, 1$). Their logarithms are
>
> $$
> \log(e^{i\pi/4}) = \ln 1 + i\Big(\frac\pi4 + 2n\pi\Big) = \Big(2n + \frac14\Big)\pi i, \qquad \log(e^{i5\pi/4}) = \ln 1 + i\Big(\frac{5\pi}{4} + 2n\pi\Big) = \Big((2n + 1) + \frac14\Big)\pi i ,
> $$
>
> for $n = 0, \pm1, \pm2, \ldots$. (For the second, $5\pi/4$ is an argument of $e^{i5\pi/4}$; adding all multiples of $2\pi$ gives every argument, so it may replace the principal one.) As $n$ runs through the integers, $2n$ runs through the even and $2n + 1$ through the odd integers, so together
>
> $$
> \log(i^{1/2}) = \Big(n + \frac14\Big)\pi i \qquad (n = 0, \pm1, \pm2, \ldots) .
> $$
>
> On the other side, $\log i = \big(2n + \frac12\big)\pi i$ ([[§31 The Logarithmic Function#^ex-31-2|Example §31.2]]), so
>
> $$
> \frac12\log i = \Big(n + \frac14\Big)\pi i \qquad (n = 0, \pm1, \pm2, \ldots) .
> $$
>
> The two sets coincide:
>
> $$
> \log(i^{1/2}) = \frac12\log i . \qquad (3)
> $$
>
> **(b)** But
>
> $$
> \log(i^2) \ne 2\log i , \qquad (4)
> $$
>
> because $\log(i^2) = \log(-1) = (2n + 1)\pi i$ (Example §32.2), while
>
> $$
> 2\log i = 2\Big[\ln 1 + i\Big(\frac\pi2 + 2n\pi\Big)\Big] = (4n + 1)\pi i \qquad (n = 0, \pm1, \pm2, \ldots) .
> $$
>
> The set $\{(4n + 1)\pi i\}$ is only part of $\{(2n + 1)\pi i\}$: it misses $-\pi i, 3\pi i, \ldots$. Doubling the set $\log i$ doubles the spacing $2\pi$ between its values, so it cannot fill out a set with spacing $2\pi$. Halving, as in (a), halves the spacing, and the two square roots supply the missing values.
>
> Comparing (3) and (4): familiar properties of logarithms are sometimes, but not always, true in complex analysis. The general statement behind (3) is $\log(z^{1/n}) = \frac1n\log z$, [[§34 Some Identities Involving Logarithms#^ex-34-4|Example §34.4]].
>
> *B&C: Sec. 32, Example 5; Sec. 33, Exercise 5; Source: 342 HW 4 (optional problems)*

^ex-32-4
