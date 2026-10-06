---
type: section
subject: "[[Complex Variables]]"
chapter: 1
section: 7
bc: "7"
aliases: ["B&C 7"]
tags: [complex-variables, math342]
---
← [[§6 Complex Conjugates]] · ↑ [[· 1 Complex Numbers]] · [[§8 Products and Powers in Exponential Form]] →

*Brown–Churchill, Section 7 · MAT 342 HW 1.*

Polar coordinates describe a nonzero complex number by its distance $r = |z|$ from the origin and an angle $\theta$, so that $z = r(\cos\theta + i\sin\theta)$. The angle is not unique: any two choices differ by a multiple of $2\pi$, and the whole set of them is the multiple-valued $\arg z$. Singling out the value in $-\pi < \theta \le \pi$ gives the principal argument $\operatorname{Arg} z$, the first of the many "principal branches" of the subject; the choice of interval, and its jump across the negative real axis, will matter for logarithms and powers in [[§31 The Logarithmic Function|§31]]–[[§36 Examples (The Power Function)|§36]]. Euler's formula $e^{i\theta} = \cos\theta + i\sin\theta$ compresses the polar form to $z = re^{i\theta}$, the exponential form in which multiplication, powers and roots become easy ([[§8 Products and Powers in Exponential Form|§8]]–[[§10 Roots of Complex Numbers|§10]]).

## Polar Form and Arguments

> [!definition] Definition §7.1: Polar Form
> Let $r$ and $\theta$ be polar coordinates of the point $(x, y)$ corresponding to a **nonzero** complex number $z = x + iy$. Since $x = r\cos\theta$ and $y = r\sin\theta$, $z$ can be written in **polar form** as
>
> $$
> z = r(\cos\theta + i\sin\theta) . \qquad (1)
> $$
>
> In complex analysis $r$ is not allowed to be negative: $r = |z|$, the length of the radius vector for $z$. When $z = 0$ the coordinate $\theta$ is undefined, so it is understood that $z \ne 0$ whenever polar coordinates are used.
>
> *B&C: Sec. 7, Equations (1)–(2)*

^def-7-1

> [!remark]- Connections
> - Polar coordinates in Calculus: [[§65 Polar Coordinates#^def-65-1|Calc Def. §65.1]] and the conversion formulas [[§65 Polar Coordinates#^thm-65-2|Calc Thm. §65.2]]. Calculus allows $r < 0$; here $r = |z| \ge 0$ always, and all the freedom is in $\theta$.
> - Earlier treatment of the argument and polar form: [[§53 Complex Numbers#^def-53-6|235 Def. §53.6]].

> [!definition] Definition §7.2: Argument
> The real number $\theta$ in the polar form (1) is the angle, in radians, that $z$ makes with the positive real axis when $z$ is interpreted as a radius vector. It has infinitely many possible values, including negative ones, that differ by integral multiples of $2\pi$; they can be determined from $\tan\theta = y/x$ once the quadrant containing $z$ is specified. Each value of $\theta$ is an **argument** of $z$, and the set of all such values is denoted by $\arg z$.
>
> *B&C: Sec. 7, Equations (1)–(2)*

^def-7-new1

> [!definition] Definition §7.3: Principal Argument
> The **principal value** of $\arg z$, denoted $\operatorname{Arg} z$, is the unique value $\Theta$ with $-\pi < \Theta \le \pi$. Then
>
> $$
> \arg z = \operatorname{Arg} z + 2n\pi \qquad (n = 0, \pm1, \pm2, \ldots) . \qquad (2)
> $$
>
> When $z$ is a negative real number, $\operatorname{Arg} z = \pi$, not $-\pi$.
>
> *B&C: Sec. 7, Equations (1)–(2)*

^def-7-new2

Equation (2) also shows that $\operatorname{Arg} z$ may be replaced by any particular value of $\arg z$: if $\theta_0$ is one value, $\arg z = \theta_0 + 2n\pi$ ($n = 0, \pm1, \ldots$).

> [!definition] Definition §7.2: Euler's Formula
> The symbol $e^{i\theta}$, or $\exp(i\theta)$, is defined by **Euler's formula**
>
> $$
> e^{i\theta} = \cos\theta + i\sin\theta , \qquad (3)
> $$
>
> where $\theta$ is measured in radians, with the agreement $e^{-i\theta} = e^{i(-\theta)}$.
>
> *B&C: Sec. 7, Equations (3)–(4)*

^def-7-2

> [!remark]- Connections
> - Ordinary Differential Equations also takes Euler's formula as a definition, motivated by the power series of $e^x$, $\cos x$, $\sin x$: [[§15 Complex Roots of the Characteristic Equation#^def-15-1|331 Def. §15.1]]; see also [[§53 Complex Numbers#^rem-53-1|235 Remark: Euler's Formula]]. In this subject the choice of the symbol is justified in [[§30 The Exponential Function#^def-30-1|Definition §30.1]], where $e^z$ is defined for all complex $z$ and (3) becomes a special case.

> [!definition] Definition §7.5: Exponential Form
> Euler's formula (3) allows the polar form (1) to be written more compactly in **exponential form**:
>
> $$
> z = re^{i\theta} . \qquad (4)
> $$
>
> *B&C: Sec. 7, Equations (3)–(4)*

^def-7-new3

With $r = 1$, (4) says that the numbers $e^{i\theta}$ lie on the circle centered at the origin with radius $1$, at the point reached by turning through the angle $\theta$ from the positive real axis. Their values can therefore be read off that circle without reference to Euler's formula ([[§7 Exponential Form#^ex-7-3|Example §7.3]]).

> [!remark] Remark: Method — Writing z in Exponential Form
> To write $z = x + iy \ne 0$ as $re^{i\theta}$ and find $\operatorname{Arg} z$:
> 1. **Modulus:** $r = |z| = \sqrt{x^2 + y^2}$.
> 2. **Quadrant:** read it off the signs of $x$ and $y$ (on an axis, read $\theta$ off directly: $0$, $\frac\pi2$, $\pi$, $-\frac\pi2$).
> 3. **Angle:** find the acute reference angle $\alpha = \tan^{-1}|y/x|$, then the angle in the right quadrant: $\alpha$, $\pi - \alpha$, $-\pi + \alpha$ or $-\alpha$ in quadrants I, II, III, IV. This value lies in $(-\pi, \pi]$, so it is $\operatorname{Arg} z$.
> 4. **All arguments:** $\arg z = \operatorname{Arg} z + 2n\pi$, and $z = r\exp[i(\operatorname{Arg} z + 2n\pi)]$ for every integer $n$.
>
> The value $\tan^{-1}(y/x)$ of a calculator lies in $(-\frac\pi2, \frac\pi2)$, so it equals $\operatorname{Arg} z$ only in the right half plane $x > 0$; for $-1 - i$ it gives $\frac\pi4$, a value of $\arg(1 + i)$, not of $\arg(-1 - i)$.

^rem-7-1

## Circles in Exponential Form

> [!theorem] Proposition §7.1: Parametrizing a Circle
> The equation
>
> $$
> z = Re^{i\theta} \qquad (0 \le \theta \le 2\pi) \qquad (7)
> $$
>
> is a parametric representation of the circle $|z| = R$: as $\theta$ increases from $0$ to $2\pi$, the point $z$ starts from the positive real axis and traverses the circle once counterclockwise. More generally, the circle $|z - z_0| = R$, with center $z_0$ and radius $R$, has the parametric representation
>
> $$
> z = z_0 + Re^{i\theta} \qquad (0 \le \theta \le 2\pi) . \qquad (8)
> $$
>
> *B&C: Sec. 7, Equations (7)–(8)*

^prop-7-1

> [!proof]+ Proof
> B&C see this from Figs. 7 and 8; here is the argument. For each $\theta$, $|Re^{i\theta}| = R\sqrt{\cos^2\theta + \sin^2\theta} = R$, so $z = z_0 + Re^{i\theta}$ satisfies $|z - z_0| = R$. Conversely, if $|z - z_0| = R > 0$, then $z - z_0 \ne 0$ has modulus $R$ and some argument $\theta$ in $[0, 2\pi)$, so $z - z_0 = Re^{i\theta}$ by Definition §7.1. As $\theta$ increases, the point $(R\cos\theta, R\sin\theta)$ turns counterclockwise about the origin, starting at $(R, 0)$ and returning to it at $\theta = 2\pi$; adding the fixed vector $z_0$ translates this motion to the circle about $z_0$. Vectorially, $z$ is the sum of the fixed vector $z_0$ and a vector of length $R$ whose angle of inclination $\theta$ varies from $0$ to $2\pi$.

^pf-7-1

*Uses:* [[§7 Exponential Form#^def-7-1|Def. §7.1]], [[§7 Exponential Form#^def-7-2|Def. §7.2]], [[§7 Exponential Form#^def-7-new3|Def. §7.5]], [[§4 Vectors and Moduli#^def-4-2|Def. §4.2]], [[§119 Trigonometry#^thm-119-4|Calc Thm. §119.4]] ($\cos^2\theta + \sin^2\theta = 1$)

This parametrization is the standard contour of the subject: the circle in Cauchy's integral formula ([[§54 Cauchy Integral Formula#^thm-54-1|Theorem §54.1]]) and in the residue theorem is traversed as $z = z_0 + Re^{i\theta}$.

## Examples

> [!example] Example §7.1: The Number −1 − i
> Find $\operatorname{Arg}(-1 - i)$, $\arg(-1 - i)$ and the exponential form of $-1 - i$.
>
> **Modulus and quadrant.** $r = |-1 - i| = \sqrt2$, and $-1 - i$ lies in the third quadrant, with reference angle $\frac\pi4$.
>
> **Principal argument.** The angle in the third quadrant within $(-\pi, \pi]$ is $-\pi + \frac\pi4$:
>
> $$
> \operatorname{Arg}(-1 - i) = -\frac{3\pi}{4} .
> $$
>
> Because of the restriction $-\pi < \Theta \le \pi$, it is **not** true that $\operatorname{Arg}(-1 - i) = \frac{5\pi}{4}$, although $\frac{5\pi}{4}$ is a value of $\arg(-1 - i)$.
>
> **All arguments.** By (2), $\arg(-1 - i) = -\frac{3\pi}{4} + 2n\pi$ ($n = 0, \pm1, \ldots$), which is the same set as $\frac{5\pi}{4} + 2n\pi$.
>
> **Exponential form.**
>
> $$
> -1 - i = \sqrt2\exp\Big[i\Big(-\frac{3\pi}{4}\Big)\Big] = \sqrt2\,e^{-i3\pi/4} , \qquad (5)
> $$
>
> and this is only one of infinitely many possibilities:
>
> $$
> -1 - i = \sqrt2\exp\Big[i\Big(-\frac{3\pi}{4} + 2n\pi\Big)\Big] \qquad (n = 0, \pm1, \pm2, \ldots) . \qquad (6)
> $$
>
> *B&C: Sec. 7, Examples 1 and 2*

^ex-7-1

> [!example] Example §7.2: The Number 1 − √3 i
> Write $z = 1 - \sqrt3\,i$ in exponential form, and find $\arg z$, $|z|$ and $\operatorname{Arg} z$.
>
> **Modulus.** $|z| = \sqrt{1^2 + (\sqrt3)^2} = 2$.
>
> **Angle.** $x = 1 > 0$ and $y = -\sqrt3 < 0$, so $z$ is in the fourth quadrant, with reference angle $\tan^{-1}\sqrt3 = \frac\pi3$. The angle in the fourth quadrant within $(-\pi, \pi]$ is $-\frac\pi3$. Check: $2\big(\cos(-\frac\pi3) + i\sin(-\frac\pi3)\big) = 2\big(\frac12 - \frac{\sqrt3}{2}i\big) = 1 - \sqrt3\,i$.
>
> **Answer.**
>
> $$
> z = 2e^{-i\pi/3}, \qquad \arg z = -\frac\pi3 + 2n\pi \ (n = 0, \pm1, \ldots), \qquad \operatorname{Arg} z = -\frac\pi3 .
> $$
>
> The principal value is negative here: $\operatorname{Arg} z = -\frac\pi3$, not $\frac\pi3$ (which is $\operatorname{Arg}\bar z$) and not $\frac{5\pi}{3}$ (which is a value of $\arg z$ outside $(-\pi, \pi]$).
>
> *Source: 342 HW 1, Problem 3(a)*

^ex-7-2

> [!example] Example §7.3: Values of e^(iθ) From the Unit Circle
> **(a)** It is geometrically obvious that $e^{i\pi} = -1$, $e^{-i\pi/2} = -i$ and $e^{-i4\pi} = 1$: turning from $1$ through a half turn counterclockwise, a quarter turn clockwise, and two full turns clockwise lands at $-1$, $-i$ and $1$.
>
> **(b)** Using the fact that $|e^{i\theta} - 1|$ is the distance between the points $e^{i\theta}$ and $1$, find a value of $\theta$ in $0 \le \theta < 2\pi$ with $|e^{i\theta} - 1| = 2$.
>
> Both points lie on the unit circle, whose diameter is $2$, so the distance $2$ is attained only when $e^{i\theta}$ is the point diametrically opposite $1$, namely $-1$. Hence $\theta = \pi$. Algebraically: $|e^{i\theta} - 1|^2 = (\cos\theta - 1)^2 + \sin^2\theta = 2 - 2\cos\theta$, which equals $4$ exactly when $\cos\theta = -1$, that is, $\theta = \pi$ in $[0, 2\pi)$.
>
> *B&C: Sec. 7 (text); Sec. 9, Exercise 4*

^ex-7-3
