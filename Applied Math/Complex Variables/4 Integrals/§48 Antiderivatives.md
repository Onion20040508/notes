---
type: section
subject: "[[Complex Variables]]"
chapter: 4
section: 48
bc: "48"
aliases: ["B&C 48"]
tags: [complex-variables, math342]
---
← [[§47 Upper Bounds for Moduli of Contour Integrals]] · ↑ [[· 4 Integrals]] · [[§49 Proof of the Theorem (Antiderivatives)]] →

*Brown–Churchill, Section 48 · MAT 342 HW 5.*

The examples of [[§45 Some Examples (Contour Integrals)#^rem-45-1|§45]] showed that a contour integral between two points may or may not depend on the path, and that integrals around closed paths may or may not vanish. This section states the theorem that decides when (the course called it a very important theorem): for a continuous $f$ on a domain $D$, having an antiderivative in $D$, having path-independent integrals in $D$, and having zero integrals around all closed contours in $D$ are equivalent. It extends the fundamental theorem of calculus to contour integrals, $\int_{z_1}^{z_2} f(z)\,dz = F(z_2) - F(z_1)$, which is the fastest way to evaluate most integrals of elementary functions. The theorem is proved in [[§49 Proof of the Theorem (Antiderivatives)#^thm-49-1|§49]]. The examples show the one real difficulty: an antiderivative that is a branch of a multiple-valued function, such as $\log z$ for $1/z$, is an antiderivative only off its branch cut, and the cut must be placed to miss the contour.

## Antiderivatives and Independence of Path

> [!definition] Definition §48.1: Independence of Path
> Let $f$ be continuous in a domain $D$. The integrals of $f$ are **independent of path** in $D$ if the integrals of $f$ along contours lying entirely in $D$ and extending from any fixed point $z_1$ to any fixed point $z_2$ all have the same value.
>
> *B&C: Sec. 48 (text)*

^def-48-1

> [!definition] Definition §48.2: Antiderivative
> An **antiderivative** of a continuous function $f(z)$ on a domain $D$ is a function $F(z)$ such that $F'(z) = f(z)$ for all $z$ in $D$. An antiderivative is, of necessity, analytic in $D$.
>
> *B&C: Sec. 48 (text)*

^def-48-2

> [!theorem] Proposition §48.1: Antiderivatives Differ by Constants
> An antiderivative of a given function $f(z)$ on a domain $D$ is unique except for an additive constant: if $F$ and $G$ are antiderivatives of $f$ on $D$, then $F - G$ is constant in $D$.
>
> *B&C: Sec. 48 (text)*

^prop-48-1

> [!proof]+ Proof
> The difference $F - G$ is analytic in $D$, and its derivative is $F' - G' = f - f = 0$ throughout $D$. An analytic function whose derivative is zero throughout a domain is constant there ([[§25 Analytic Functions#^thm-25-3|Theorem §25.3]]).

^pf-48-1

*Uses:* [[§48 Antiderivatives#^def-48-2|Def. §48.2]], [[§25 Analytic Functions#^thm-25-3|§25.3]]

The hypothesis that $D$ is a domain, in particular connected, matters: on two disjoint disks, $F - G$ could be a different constant on each.

## The Theorem

The theorem of this section is stated here and proved in the next, as [[§49 Proof of the Theorem (Antiderivatives)#^thm-49-1|Theorem §49.1]].

**Theorem.** *Suppose that a function $f(z)$ is continuous in a domain $D$. If any one of the following statements is true, then so are the others:*

*(a) $f(z)$ has an antiderivative $F(z)$ throughout $D$;*

*(b) the integrals of $f(z)$ along contours lying entirely in $D$ and extending from any fixed point $z_1$ to any fixed point $z_2$ all have the same value, namely*
$$
\int_{z_1}^{z_2} f(z)\,dz = F(z)\Big]_{z_1}^{z_2} = F(z_2) - F(z_1) ,
$$
*where $F(z)$ is the antiderivative in statement (a);*

*(c) the integrals of $f(z)$ around closed contours lying entirely in $D$ all have value zero.*

The theorem does *not* claim that any of these statements is true for a given function $f$. It says only that all of them are true or none of them is. Its two main uses are: when an antiderivative is known on a domain containing $C$, (b) evaluates the integral from the endpoints alone, and (c) gives $0$ around closed contours; and when an integral around some closed contour in $D$ is not zero, no antiderivative exists in $D$ (see the remark after the proof in [[§49 Proof of the Theorem (Antiderivatives)#^rem-49-2|§49]]).

> [!remark]- Connections
> - The real counterpart is the fundamental theorem for line integrals, [[§128 The Fundamental Theorem for Line Integrals#^thm-128-1|Calc Thm. §128.1]]: $\int_C \nabla\phi\cdot d\mathbf{r} = \phi(B) - \phi(A)$. An antiderivative $F$ plays the role of the potential $\phi$, for both real line integrals into which $\int_C f\,dz$ splits.

## Examples

> [!example] Example §48.1: An Entire Integrand
> The continuous function $f(z) = e^{\pi z}$ evidently has an antiderivative $F(z) = e^{\pi z}/\pi$ throughout the finite plane ([[§30 The Exponential Function#^thm-30-3|Theorem §30.3]]). Hence, along any contour,
>
> $$
> \int_i^{i/2} e^{\pi z}\,dz = \frac{e^{\pi z}}{\pi}\bigg]_i^{i/2} = \frac1\pi\big(e^{i\pi/2} - e^{i\pi}\big) = \frac1\pi(i + 1) = \frac1\pi(1 + i) .
> $$
>
> *B&C: Sec. 48, Example 1*

^ex-48-1

> [!example] Example §48.2: 1/z² Has an Antiderivative on the Punctured Plane, 1/z Does Not
> The function $f(z) = 1/z^2$, which is continuous everywhere except at the origin, has an antiderivative $F(z) = -1/z$ in the domain $|z| > 0$, consisting of the entire plane with the origin deleted. Consequently
>
> $$
> \int_C \frac{dz}{z^2} = 0
> $$
>
> when $C$ is the positively oriented unit circle $z = e^{i\theta}$ $(-\pi \le \theta \le \pi)$ about the origin, and indeed around every closed contour not passing through $0$.
>
> The integral of $f(z) = 1/z$ around the same circle *cannot* be evaluated in this way. The derivative of any branch $F(z)$ of $\log z$ is $1/z$ ([[§33 Branches and Derivatives of Logarithms#^thm-33-1|Theorem §33.1]]), but $F(z)$ is not differentiable, or even defined, along its branch cut ([[§33 Branches and Derivatives of Logarithms#^def-33-4|Definition §33.4]]). If a ray $\theta = \alpha$ from the origin is used to form the branch cut, $F'(z)$ fails to exist at the point where that ray meets the circle $C$. So $C$ does not lie in any domain throughout which $F'(z) = 1/z$, and one cannot make direct use of an antiderivative. (In fact no domain containing $C$ carries an antiderivative of $1/z$, since $\int_C dz/z = 2\pi i \ne 0$; see [[§49 Proof of the Theorem (Antiderivatives)#^rem-49-2|§49]].)
>
> *B&C: Sec. 48, Example 2*

^ex-48-2

But a combination of *two* different antiderivatives can be used to evaluate the integral of $1/z$ around $C$.

> [!example] Example §48.3: 1/z Around the Circle with Two Branches of log z
> Let $C_1$ be the *right* half $z = e^{i\theta}$ $(-\frac\pi2 \le \theta \le \frac\pi2)$ of the unit circle $C$, from $-i$ to $i$. The principal branch
>
> $$
> \operatorname{Log} z = \ln r + i\Theta \qquad (r > 0,\ -\pi < \Theta < \pi)
> $$
>
> is an antiderivative of $1/z$ in a domain containing $C_1$, so
>
> $$
> \int_{C_1}\frac{dz}{z} = \int_{-i}^{i}\frac{dz}{z} = \operatorname{Log} z\Big]_{-i}^{i} = \operatorname{Log} i - \operatorname{Log}(-i) = \Big(\ln 1 + i\frac\pi2\Big) - \Big(\ln 1 - i\frac\pi2\Big) = \pi i .
> $$
>
> Next let $C_2$ be the *left* half $z = e^{i\theta}$ $(\frac\pi2 \le \theta \le \frac{3\pi}{2})$ of the same circle, from $i$ to $-i$, and use the branch
>
> $$
> \log z = \ln r + i\theta \qquad (r > 0,\ 0 < \theta < 2\pi) ,
> $$
>
> whose cut, the positive real axis, misses $C_2$:
>
> $$
> \int_{C_2}\frac{dz}{z} = \int_i^{-i}\frac{dz}{z} = \log z\Big]_i^{-i} = \log(-i) - \log i = \Big(\ln 1 + i\frac{3\pi}{2}\Big) - \Big(\ln 1 + i\frac\pi2\Big) = \pi i .
> $$
>
> The value of the integral of $1/z$ around the entire circle $C = C_1 + C_2$ is thus
>
> $$
> \int_C\frac{dz}{z} = \int_{C_1}\frac{dz}{z} + \int_{C_2}\frac{dz}{z} = \pi i + \pi i = 2\pi i ,
> $$
>
> in agreement with [[§45 Some Examples (Contour Integrals)#^ex-45-1|Example §45.1]]. The two branches do not fit together into one antiderivative along $C$: they agree in the upper half-plane, but in the lower half-plane $\log z = \operatorname{Log} z + 2\pi i$. Following the values of the logarithm continuously once around the circle, they increase by $2\pi i$, which is exactly the integral.
>
> *B&C: Sec. 48, Example 3*

^ex-48-3

> [!example] Example §48.4: A Branch of z^(1/2), Replaced by Branches That Agree with It on the Contour
> Let the integrand be the branch
>
> $$
> f(z) = z^{1/2} = \exp\Big(\frac12\log z\Big) = \sqrt r\,e^{i\theta/2} \qquad (r > 0,\ 0 < \theta < 2\pi) \qquad (2)
> $$
>
> of the square root function, and let $C_1$ be any contour from $z = -3$ to $z = 3$ that, except for its end points, lies above the $x$ axis. The integrand is piecewise continuous on $C_1$, so the integral exists, but the branch (2) is not defined on the ray $\theta = 0$, in particular at the point $z = 3$.
>
> **Above the axis.** The branch
>
> $$
> f_1(z) = \sqrt r\,e^{i\theta/2} \qquad \Big(r > 0,\ -\frac\pi2 < \theta < \frac{3\pi}{2}\Big)
> $$
>
> is defined and continuous everywhere on $C_1$, and its values at all points of $C_1$ except $z = 3$ coincide with those of (2); so the integrand can be replaced by $f_1(z)$. An antiderivative of $f_1$ in its domain, which contains $C_1$, is
>
> $$
> F_1(z) = \frac23 z^{3/2} = \frac23 r\sqrt r\,e^{i3\theta/2} \qquad \Big(r > 0,\ -\frac\pi2 < \theta < \frac{3\pi}{2}\Big)
> $$
>
> (by the derivative of a branch of $z^c$, [[§35 The Power Function#^thm-35-2|Theorem §35.2]]: $\frac{d}{dz}\exp(\frac32\log z) = \frac32\cdot\frac1z\exp(\frac32\log z) = \frac32\exp(\frac12\log z)$ for the same branch of $\log$). At $z = 3$, $\theta = 0$; at $z = -3$, $\theta = \pi$. So
>
> $$
> \int_{C_1} z^{1/2}\,dz = \int_{-3}^{3} f_1(z)\,dz = F_1(z)\Big]_{-3}^{3} = 2\sqrt3\big(e^{i0} - e^{i3\pi/2}\big) = 2\sqrt3(1 + i) .
> $$
>
> Compare [[§46 Examples Involving Branch Cuts#^ex-46-1|Example §46.1]]: along the upper semicircle from $3$ to $-3$ the integral is $-2\sqrt3(1 + i)$, the negative, as property (6) and independence of path require.
>
> **Below the axis.** Let $C_2$ be any contour from $-3$ to $3$ that, except for its end points, lies *below* the real axis. Now replace the integrand by
>
> $$
> f_2(z) = \sqrt r\,e^{i\theta/2} \qquad \Big(r > 0,\ \frac\pi2 < \theta < \frac{5\pi}{2}\Big) ,
> $$
>
> whose values coincide with those of (2) at $z = -3$ and at all points of $C_2$ below the real axis; at $z = 3$ (where $\theta = 2\pi$) it gives the limit of (2) from below. An antiderivative is $F_2(z) = \frac23 r\sqrt r\,e^{i3\theta/2}$ with the same range of $\theta$. At $z = 3$, $\theta = 2\pi$; at $z = -3$, $\theta = \pi$. So
>
> $$
> \int_{C_2} z^{1/2}\,dz = F_2(z)\Big]_{-3}^{3} = 2\sqrt3\big(e^{i3\pi} - e^{i3\pi/2}\big) = 2\sqrt3(-1 + i) .
> $$
>
> The integral of the function (2) around the closed contour $C_2 - C_1$ is therefore $2\sqrt3(-1 + i) - 2\sqrt3(1 + i) = -4\sqrt3$. It is not zero: no single branch of $z^{1/2}$ is continuous around the origin.
>
> *B&C: Sec. 48, Example 4; Sec. 49, Exercise 4*

^ex-48-4

![[m342-48-1.svg]]
*Branch cuts (dashed) placed to miss the contour. Left, Example §48.3: the principal branch $\operatorname{Log} z$ (cut along the negative real axis, blue) is an antiderivative of $1/z$ along the right half $C_1$; the branch with $0 < \theta < 2\pi$ (cut along the positive real axis, red) along the left half $C_2$. Each half gives $\pi i$. Right, Example §48.4: contours from $-3$ to $3$ above (blue) and below (red) the real axis. The branch $f_1$ ($-\frac\pi2 < \theta < \frac{3\pi}{2}$) is cut along the negative imaginary axis and $f_2$ ($\frac\pi2 < \theta < \frac{5\pi}{2}$) along the positive imaginary axis; both agree with the given branch of $z^{1/2}$, whose cut is the positive real axis (gray), on their contour.*

> [!remark] Remark: Method — Evaluating a Contour Integral by an Antiderivative
> 1. **Find $F$** with $F'(z) = f(z)$, using the derivatives of the elementary functions.
> 2. **Find a domain $D$ containing $C$** on which $F$ is analytic and $F' = f$. For a polynomial, $e^z$, $\sin z$, $\cos z$, $D$ is the whole plane. For a branch ($\log$, $z^c$, $\log(g(z))$), place the branch cut so that it misses $C$; if $C$ ends on the cut of the given branch, replace the integrand by a branch that agrees with it on $C$ (Example §48.4).
> 3. **Evaluate** $\int_C f(z)\,dz = F(z_2) - F(z_1)$, with $F$ evaluated in the chosen branch. Around a closed contour in $D$ the integral is $0$.
> 4. **If no single branch works**, split $C$ into pieces, each with its own branch (Example §48.3).
> 5. **If $f$ has no antiderivative** on any domain containing $C$ (for instance $1/z$ around the origin, or a non-analytic $f$ such as $\bar z$), parametrize ([[§45 Some Examples (Contour Integrals)#^rem-45-2|§45]]) or, later, use the Cauchy–Goursat theorem ([[§51 Proof of the Theorem (Cauchy–Goursat Theorem)#^thm-51-3|Theorem §51.3]]) and residues ([[§76 Cauchy's Residue Theorem#^thm-76-1|Theorem §76.1]]).

^rem-48-1

> [!example] Example §48.5: Two Integrals by Antiderivatives
> Find antiderivatives and compute the integrals along paths that connect the limits of integration; in (b) the path lies in the right half-plane $\operatorname{Re} z \ge 0$. Explain why the answers depend only on the endpoints.
>
> **(a)** $\displaystyle\int_0^{\pi+i}\sin(2z)\,dz$. An antiderivative of $\sin 2z$ in the whole plane is $F(z) = -\frac12\cos 2z$ ([[§37 The Trigonometric Functions sin z and cos z#^thm-37-1|Theorem §37.1]]). Since $\cos(2\pi + 2i) = \cos 2i = \cosh 2$,
>
> $$
> \int_0^{\pi+i}\sin(2z)\,dz = -\frac12\cos(2\pi + 2i) + \frac12\cos 0 = \frac{1 - \cosh 2}{2} = -\sinh^2 1 \approx -1.3811 .
> $$
>
> **(b)** $\displaystyle\int_0^{i}\frac{dz}{z + 1}$. An antiderivative is $F(z) = \operatorname{Log}(z + 1)$, analytic except where $z + 1$ lies on the cut $(-\infty, 0]$, that is, on the ray $z \le -1$ of the real axis. The domain $D = \mathbb{C}\setminus(-\infty, -1]$ contains the closed right half-plane, hence the path, and in $D$, $F'(z) = 1/(z + 1)$. So
>
> $$
> \int_0^{i}\frac{dz}{z + 1} = \operatorname{Log}(1 + i) - \operatorname{Log} 1 = \ln\sqrt2 + i\frac\pi4 = \frac12\ln 2 + \frac{\pi}{4}i \approx 0.3466 + 0.7854i .
> $$
>
> **Why only the endpoints matter.** In each case $f$ has an antiderivative throughout a domain containing every admissible path, so by statement (b) of the theorem the integral is $F(z_2) - F(z_1)$. In (b) the restriction on the path matters: a path from $0$ to $i$ that winds once counterclockwise around $-1$ leaves $D$, and its integral is larger by $\int dz/(z + 1) = 2\pi i$ around a circle about $-1$ ([[§45 Some Examples (Contour Integrals)#^ex-45-5|Example §45.5]]).
>
> *Source: 342 HW 5, Problem 1*

^ex-48-5
