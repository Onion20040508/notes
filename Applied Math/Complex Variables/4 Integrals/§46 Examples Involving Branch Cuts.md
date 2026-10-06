---
type: section
subject: "[[Complex Variables]]"
chapter: 4
section: 46
bc: "46"
aliases: ["B&C 46"]
tags: [complex-variables, math342]
---
← [[§45 Some Examples (Contour Integrals)]] · ↑ [[· 4 Integrals]] · [[§47 Upper Bounds for Moduli of Contour Integrals]] →

*Brown–Churchill, Section 46 · MAT 342 HW 5.*

The integrand of a contour integral is often a branch of a multiple-valued function such as $z^{1/2}$, $z^{-1+i}$ or $z^i$ ([[§35 The Power Function#^def-35-1|Definition §35.1]]), and the contour may contain points of the branch cut, where the branch is not even defined. The integral still exists as long as $f[z(t)]z'(t)$ is piecewise continuous, which only requires one-sided limits at those points. On the contour, the branch is written in terms of the parameter, $\log z = \ln R + i\theta$ with $\theta$ in the branch's range, and the integral becomes an integral of exponentials in $\theta$. The examples also show that the value depends on the branch chosen.

## Two Examples

> [!example] Example §46.1: A Branch of z^(1/2) Along a Semicircle Starting on the Cut
> Let $C$ be the semicircular path $z = 3e^{i\theta}$ $(0 \le \theta \le \pi)$ from $z = 3$ to $z = -3$. The branch
>
> $$
> f(z) = z^{1/2} = \exp\Big(\frac12\log z\Big) \qquad (|z| > 0,\ 0 < \arg z < 2\pi)
> $$
>
> of $z^{1/2}$ is not defined at the initial point $z = 3$ of $C$, which lies on its branch cut ([[§33 Branches and Derivatives of Logarithms#^def-33-3|Definition §33.3]]). Nevertheless the integral
>
> $$
> I = \int_C z^{1/2}\,dz \qquad (1)
> $$
>
> exists, because its integrand is piecewise continuous on $C$. Indeed, when $z(\theta) = 3e^{i\theta}$ with $0 < \theta \le \pi$,
>
> $$
> f[z(\theta)] = \exp\Big[\frac12(\ln 3 + i\theta)\Big] = \sqrt3\,e^{i\theta/2} ,
> $$
>
> so
>
> $$
> f[z(\theta)]\,z'(\theta) = \sqrt3\,e^{i\theta/2}\,3ie^{i\theta} = 3\sqrt3\,ie^{i3\theta/2} = -3\sqrt3\sin\frac{3\theta}{2} + i3\sqrt3\cos\frac{3\theta}{2} \qquad (0 < \theta \le \pi) .
> $$
>
> The right-hand limits of the real and imaginary parts at $\theta = 0$ exist, being $0$ and $3\sqrt3$. So $f[z(\theta)]z'(\theta)$ is continuous on $0 \le \theta \le \pi$ once its value at $\theta = 0$ is defined as $i3\sqrt3$, and
>
> $$
> I = 3\sqrt3\,i\int_0^{\pi} e^{i3\theta/2}\,d\theta = 3\sqrt3\,i\cdot\frac{2}{3i}e^{i3\theta/2}\bigg]_0^{\pi} = 2\sqrt3\big(e^{i3\pi/2} - 1\big) = 2\sqrt3(-i - 1) ,
> $$
>
> that is,
>
> $$
> I = -2\sqrt3(1 + i) \approx -3.4641 - 3.4641i . \qquad (2)
> $$
>
> *B&C: Sec. 46, Example 1*

^ex-46-1

> [!example] Example §46.2: The Principal Branch of z^(−1+i) Around the Unit Circle
> Using the principal branch
>
> $$
> f(z) = z^{-1+i} = \exp\big[(-1 + i)\operatorname{Log} z\big] \qquad (|z| > 0,\ -\pi < \operatorname{Arg} z < \pi)
> $$
>
> evaluate
>
> $$
> I = \int_C z^{-1+i}\,dz , \qquad (3)
> $$
>
> where $C$ is the positively oriented unit circle $z = e^{i\theta}$ $(-\pi \le \theta \le \pi)$. It begins and ends at $z = -1$, on the branch cut. When $z(\theta) = e^{i\theta}$ with $-\pi < \theta < \pi$, $\operatorname{Log} z = \ln 1 + i\theta = i\theta$, and
>
> $$
> f[z(\theta)]\,z'(\theta) = e^{(-1+i)(i\theta)}\,ie^{i\theta} = e^{-i\theta - \theta}\,ie^{i\theta} = ie^{-\theta} . \qquad (4)
> $$
>
> This is piecewise continuous on $-\pi \le \theta \le \pi$ (it has one-sided limits at $\pm\pi$), so the integral exists:
>
> $$
> I = i\int_{-\pi}^{\pi} e^{-\theta}\,d\theta = i\big[-e^{-\theta}\big]_{-\pi}^{\pi} = i\big(e^{\pi} - e^{-\pi}\big) = 2i\sinh\pi \approx 23.0975i .
> $$
>
> *B&C: Sec. 46, Example 2*

^ex-46-2

![[m342-46-1.svg]]
*Contours that touch a branch cut (dashed) only at their endpoints. Left: Example §46.1, the semicircle $z = 3e^{i\theta}$ from $3$ to $-3$; the branch $0 < \arg z < 2\pi$ of $z^{1/2}$ is cut along the positive real axis, so it is undefined at the initial point $3$, but $f[z(\theta)]$ has a limit there as $\theta \to 0^+$. Right: Example §46.2, the unit circle starting and ending at $-1$ on the principal cut; along the circle the integrand $f[z(\theta)]z'(\theta) = ie^{-\theta}$ has the finite end values $ie^{\pi}$ and $ie^{-\pi}$, which is all the integral needs.*

> [!remark] Remark: Method — Integrating a Branch by Parametrization
> 1. **Write the branch along $C$.** On $z = Re^{i\theta}$, a branch with range $\alpha < \arg z < \alpha + 2\pi$ has $\log z = \ln R + i\theta$, where $\theta$ must be taken in that range; then $z^c = \exp(c\log z) = \exp\big(c(\ln R + i\theta)\big)$. If the parameter interval of $C$ is not inside the range, shift $\theta$ by $2\pi$ on the part that is outside, or split $C$ where it meets the cut.
> 2. **Check the cut.** Points of $C$ on the branch cut are allowed if $f[z(\theta)]z'(\theta)$ has one-sided limits there; the integral is then the integral of a piecewise continuous function.
> 3. **Integrate** the resulting combination of exponentials $e^{k\theta}$ in $\theta$, with antiderivatives $e^{k\theta}/k$.
> 4. **The value depends on the branch** (Example §46.4) and, if $C$ crosses a cut, it is generally not given by an antiderivative of the branch along $C$; compare [[§48 Antiderivatives#^ex-48-4|Example §48.4]], where a branch is replaced by another one that agrees with it on $C$.

^rem-46-1

## Course and Exercise Examples

> [!example] Example §46.3: zⁱ Along Two Half Circles, with Two Branches
> Compute $\int_C z^i\,dz$ in two situations.
>
> **(a)** $C$ is the semicircle from $-i$ to $i$ through the fourth and first quadrants, and $z^i = e^{i\operatorname{Log} z}$ is the principal branch. Take $z = e^{it}$ $(-\frac\pi2 \le t \le \frac\pi2)$. Then $\operatorname{Log} z = it$, $z^i = e^{i\cdot it} = e^{-t}$, $z' = ie^{it}$, and
>
> $$
> \int_C z^i\,dz = \int_{-\pi/2}^{\pi/2} ie^{(i-1)t}\,dt = \frac{i}{i - 1}\Big[e^{(i-1)t}\Big]_{-\pi/2}^{\pi/2} = \frac{i}{i - 1}\Big(ie^{-\pi/2} + ie^{\pi/2}\Big) = \frac{-2\cosh(\pi/2)}{i - 1} = (1 + i)\cosh\frac\pi2 ,
> $$
>
> using $e^{(i-1)\pi/2} = ie^{-\pi/2}$, $e^{-(i-1)\pi/2} = -ie^{\pi/2}$ and $1/(i - 1) = -(1 + i)/2$. Numerically $2.5092(1 + i)$.
>
> **(b)** $C$ is the semicircle from $-i$ to $i$ through the third and second quadrants, and $z^i = e^{i\log z}$ with $\log z = \ln r + i\theta$, $0 < \theta < 2\pi$. Now $C$ is $z = e^{it}$ with $t$ decreasing from $\frac{3\pi}{2}$ to $\frac\pi2$; the representation $z = e^{it}$ $(\frac\pi2 \le t \le \frac{3\pi}{2})$ runs from $i$ to $-i$ and represents $-C$. On it $\log z = it$ (as $t$ lies in the range $(0, 2\pi)$), $z^i = e^{-t}$, and
>
> $$
> \int_{-C} z^i\,dz = \int_{\pi/2}^{3\pi/2} ie^{(i-1)t}\,dt = \frac{i}{i - 1}\Big(e^{(i-1)3\pi/2} - e^{(i-1)\pi/2}\Big) = \frac{i}{i - 1}\Big(-ie^{-3\pi/2} - ie^{-\pi/2}\Big) = -\frac{(1 + i)\big(e^{-\pi/2} + e^{-3\pi/2}\big)}{2} .
> $$
>
> By property (6) of [[§44 Contour Integrals#^thm-44-2|Theorem §44.2]],
>
> $$
> \int_C z^i\,dz = \frac{(1 + i)\big(e^{-\pi/2} + e^{-3\pi/2}\big)}{2} = (1 + i)\,e^{-\pi}\cosh\frac\pi2 \approx 0.1084(1 + i) .
> $$
>
> **Why not the principal branch in (b)?** The principal branch is defined only for $-\pi < \operatorname{Arg} z < \pi$, and the semicircle in (b) crosses its cut at $z = -1$. There the principal values jump: approaching $-1$ through the second quadrant, $\operatorname{Arg} z \to \pi$ and $z^i = e^{-\operatorname{Arg} z} \to e^{-\pi}$; through the third quadrant, $\operatorname{Arg} z \to -\pi$ and $z^i \to e^{\pi}$. The branch with $0 < \theta < 2\pi$ is continuous on all of $C$. (The principal-branch integrand is still piecewise continuous, and splitting $C$ at $-1$ would give the different value $(\cosh\frac\pi2 - \sinh\pi) + i(\sinh\pi + \cosh\frac\pi2) \approx -9.040 + 14.058i$; it is just not the integral of a branch that is analytic along $C$.)
>
> *Source: 342 HW 5, Problem 3*

^ex-46-3

> [!example] Example §46.4: The Value Depends on the Branch
> Let $C$ be the positively oriented unit circle $|z| = 1$.
>
> **(a)** For the principal branch $z^{-3/4} = \exp\big[-\frac34\operatorname{Log} z\big]$ $(|z| > 0, -\pi < \operatorname{Arg} z < \pi)$, use $z = e^{i\theta}$ $(-\pi \le \theta \le \pi)$: $f[z(\theta)]z'(\theta) = e^{-3i\theta/4}\,ie^{i\theta} = ie^{i\theta/4}$, so
>
> $$
> \int_C f(z)\,dz = \int_{-\pi}^{\pi} ie^{i\theta/4}\,d\theta = 4\Big[e^{i\theta/4}\Big]_{-\pi}^{\pi} = 4\big(e^{i\pi/4} - e^{-i\pi/4}\big) = 8i\sin\frac\pi4 = 4\sqrt2\,i .
> $$
>
> **(b)** For the branch $z^{-3/4} = \exp\big[-\frac34\log z\big]$ $(|z| > 0, 0 < \arg z < 2\pi)$, use $z = e^{i\theta}$ $(0 \le \theta \le 2\pi)$; the integrand is again $ie^{i\theta/4}$, now over $[0, 2\pi]$:
>
> $$
> \int_C g(z)\,dz = 4\Big[e^{i\theta/4}\Big]_0^{2\pi} = 4\big(e^{i\pi/2} - 1\big) = -4 + 4i .
> $$
>
> The two branches differ by the factor $e^{-3\pi i/2} = i$ on the lower half of the circle and agree on the upper half, and the integrals differ. In general the value of an integral of a power function depends on the branch that is used.
>
> *B&C: Sec. 46, Exercise 9*

^ex-46-4
