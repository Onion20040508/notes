---
type: section
subject: "[[Complex Variables]]"
chapter: 1
section: 8
bc: "8"
aliases: ["B&C 8"]
tags: [complex-variables, math342]
---
← [[§7 Exponential Form]] · ↑ [[· 1 Complex Numbers]] · [[§9 Arguments of Products and Quotients]] →

*Brown–Churchill, Section 8 · MAT 342 HW 1.*

The addition formulas of trigonometry say exactly that $e^{i\theta_1}e^{i\theta_2} = e^{i(\theta_1 + \theta_2)}$: the symbol $e^{i\theta}$ obeys the law of exponents. In exponential form, therefore, multiplication multiplies moduli and adds arguments, and division divides moduli and subtracts arguments. Geometrically, multiplying by $re^{i\theta}$ scales the plane by $r$ and rotates it through $\theta$. Iterating gives $z^n = r^ne^{in\theta}$ for every integer $n$, and with $r = 1$ de Moivre's formula, which packages the multiple-angle identities of trigonometry. Powers of a number given in rectangular form are best computed this way.

## Products and Quotients

> [!theorem] Theorem §8.1: Products and Quotients in Exponential Form
> For real $\theta_1$, $\theta_2$,
>
> $$
> e^{i\theta_1}e^{i\theta_2} = e^{i(\theta_1 + \theta_2)} .
> $$
>
> Hence, if $z_1 = r_1e^{i\theta_1}$ and $z_2 = r_2e^{i\theta_2}$,
>
> $$
> z_1z_2 = (r_1r_2)e^{i(\theta_1 + \theta_2)} , \qquad (1) \qquad\qquad \frac{z_1}{z_2} = \frac{r_1}{r_2}e^{i(\theta_1 - \theta_2)} , \qquad (2)
> $$
>
> and the inverse of any nonzero $z = re^{i\theta}$ is
>
> $$
> z^{-1} = \frac1z = \frac1re^{-i\theta} . \qquad (3)
> $$
>
> *B&C: Sec. 8, Equations (1)–(3)*

^thm-8-1

> [!proof]+ Proof
> **Law of exponents.** By Euler's formula, the product rule (8) of [[§1 Sums and Products#^prop-1-2|Proposition §1.2]], and the addition formulas for cosine and sine,
>
> $$
> \begin{aligned}
> e^{i\theta_1}e^{i\theta_2} &= (\cos\theta_1 + i\sin\theta_1)(\cos\theta_2 + i\sin\theta_2) \\
> &= (\cos\theta_1\cos\theta_2 - \sin\theta_1\sin\theta_2) + i(\sin\theta_1\cos\theta_2 + \cos\theta_1\sin\theta_2) \\
> &= \cos(\theta_1 + \theta_2) + i\sin(\theta_1 + \theta_2) = e^{i(\theta_1 + \theta_2)} .
> \end{aligned}
> $$
>
> **(1)** By the commutative and associative laws, $z_1z_2 = r_1e^{i\theta_1}r_2e^{i\theta_2} = r_1r_2\,e^{i\theta_1}e^{i\theta_2} = (r_1r_2)e^{i(\theta_1 + \theta_2)}$.
>
> **(2)** By the law of exponents, $e^{i\theta_2}e^{-i\theta_2} = e^{i0} = 1$. Multiplying numerator and denominator by $e^{-i\theta_2}$ (the cancellation law of [[§3 Further Algebraic Properties#^prop-3-3|Proposition §3.3]]) and using (12) of [[§3 Further Algebraic Properties#^prop-3-3|Proposition §3.3]],
>
> $$
> \frac{z_1}{z_2} = \frac{r_1e^{i\theta_1}}{r_2e^{i\theta_2}} = \frac{r_1}{r_2}\cdot\frac{e^{i\theta_1}e^{-i\theta_2}}{e^{i\theta_2}e^{-i\theta_2}} = \frac{r_1}{r_2}\cdot\frac{e^{i(\theta_1 - \theta_2)}}{e^{i0}} = \frac{r_1}{r_2}e^{i(\theta_1 - \theta_2)} .
> $$
>
> **(3)** Apply (2) with $z_1 = 1 = 1e^{i0}$: $\dfrac1z = \dfrac{1e^{i0}}{re^{i\theta}} = \dfrac1re^{i(0 - \theta)} = \dfrac1re^{-i\theta}$.

^pf-8-1

*Uses:* [[§7 Exponential Form#^def-7-2|Def. §7.2]], [[§7 Exponential Form#^def-7-new3|Def. §7.5]], [[§1 Sums and Products#^prop-1-2|§1.2]], [[§119 Trigonometry#^thm-119-6|Calc Thm. §119.6]] (addition formulas), [[§2 Basic Algebraic Properties#^thm-2-1|§2.1]], [[§3 Further Algebraic Properties#^prop-3-3|§3.3]]

> [!remark]- Connections
> - The same theorem in the computational treatment: [[§53 Complex Numbers#^thm-53-5|235 Thm. §53.5]]; in matrix form, multiplication by $re^{i\theta}$ is $r$ times the rotation matrix through $\theta$, [[§53 Complex Numbers#^rem-53-3|235 Remark: Complex Numbers as 2 × 2 Matrices]].

Expressions (1), (2) and (3) are easily remembered by applying the usual algebraic rules for real numbers and $e^x$. Read geometrically, (1) says that multiplying a number by $z_2 = r_2e^{i\theta_2}$ stretches its radius vector by the factor $r_2$ and rotates it counterclockwise through the angle $\theta_2$. Multiplication by $i = e^{i\pi/2}$ is the rotation through $90°$ found in [[§1 Sums and Products#^ex-1-2|Example §1.2]].

## Integer Powers

> [!definition] Definition §8.1: Integer Powers
> For a complex number $z$ and $n = 1, 2, \ldots$, the powers are $z^1 = z$, $z^2 = zz$, $z^{n+1} = z^nz$ (as in [[§1 Sums and Products#^prop-1-2|Proposition §1.2]]). For $z \ne 0$, also $z^0 = 1$, and for negative integers $n = -1, -2, \ldots$,
>
> $$
> z^n = (z^{-1})^m \qquad\text{where } m = -n = 1, 2, \ldots .
> $$
>
> *B&C: Sec. 8 (text)*

^def-8-1

> [!theorem] Theorem §8.2: Integer Powers in Exponential Form
> If $z = re^{i\theta}$ is nonzero, then
>
> $$
> z^n = r^ne^{in\theta} \qquad (n = 0, \pm1, \pm2, \ldots) . \qquad (4)
> $$
>
> *B&C: Sec. 8, Equation (4)*

^thm-8-2

> [!proof]+ Proof
> **Positive $n$**, by induction. For $n = 1$, (4) is $z = re^{i\theta}$. If (4) is valid for $n = m$, then by the product formula (1),
>
> $$
> z^{m+1} = z^mz = r^me^{im\theta}\,re^{i\theta} = (r^mr)e^{i(m\theta + \theta)} = r^{m+1}e^{i(m+1)\theta} .
> $$
>
> **$n = 0$.** With the convention $z^0 = 1$, both sides equal $1$: $r^0e^{i0} = 1$.
>
> **Negative $n$.** Let $n = -m$ with $m = 1, 2, \ldots$. By (3), $z^{-1} = \frac1re^{i(-\theta)}$, a number in exponential form with modulus $1/r$ and argument $-\theta$. Applying the positive case to it,
>
> $$
> z^n = (z^{-1})^m = \Big[\frac1re^{i(-\theta)}\Big]^m = \Big(\frac1r\Big)^me^{im(-\theta)} = \Big(\frac1r\Big)^{-n}e^{i(-n)(-\theta)} = r^ne^{in\theta} .
> $$
>
> So (4) holds for all integral powers.

^pf-8-2

*Uses:* [[§8 Products and Powers in Exponential Form#^def-8-1|Def. §8.1]], [[§8 Products and Powers in Exponential Form#^thm-8-1|§8.1]]

> [!theorem] Corollary §8.3: de Moivre's Formula
> For every real $\theta$,
>
> $$
> (e^{i\theta})^n = e^{in\theta} \qquad (n = 0, \pm1, \pm2, \ldots) , \qquad (5)
> $$
>
> that is,
>
> $$
> (\cos\theta + i\sin\theta)^n = \cos n\theta + i\sin n\theta \qquad (n = 0, \pm1, \pm2, \ldots) . \qquad (6)
> $$
>
> *B&C: Sec. 8, Equations (5)–(6)*

^cor-8-3

> [!proof]+ Proof
> Take $r = 1$ in (4), and write both sides of (5) with Euler's formula to get (6).

^pf-8-3

*Uses:* [[§8 Products and Powers in Exponential Form#^thm-8-2|§8.2]], [[§7 Exponential Form#^def-7-2|Def. §7.2]]

> [!remark]- Connections
> - De Moivre's theorem for positive $n$, proved by the same induction: [[§53 Complex Numbers#^thm-53-6|235 Thm. §53.6]].

## Examples

> [!example] Example §8.1: A Power in Rectangular Form
> Put $(-1 + i)^7$ in rectangular form.
>
> Here $|-1 + i| = \sqrt2$ and $-1 + i$ is in the second quadrant with reference angle $\frac\pi4$, so $-1 + i = \sqrt2\,e^{i3\pi/4}$. By (4),
>
> $$
> (-1 + i)^7 = \big(\sqrt2\,e^{i3\pi/4}\big)^7 = 2^{7/2}e^{i21\pi/4} = \big(2^3e^{i5\pi}\big)\big(2^{1/2}e^{i\pi/4}\big) ,
> $$
>
> splitting $\frac{21\pi}{4} = 5\pi + \frac\pi4$ by the law of exponents. Because $2^3e^{i5\pi} = 8(-1) = -8$ and
>
> $$
> 2^{1/2}e^{i\pi/4} = \sqrt2\Big(\cos\frac\pi4 + i\sin\frac\pi4\Big) = \sqrt2\Big(\frac{1}{\sqrt2} + \frac{i}{\sqrt2}\Big) = 1 + i ,
> $$
>
> we arrive at $(-1 + i)^7 = -8(1 + i)$.
>
> *B&C: Sec. 8, Example 1*

^ex-8-1

> [!example] Example §8.2: Fifth Powers of 1 ∓ √3 i
> Compute **(a)** $(1 - \sqrt3\,i)^5$ and **(b)** $(1 + \sqrt3\,i)^5$.
>
> **(a)** By [[§7 Exponential Form#^ex-7-2|Example §7.2]], $1 - \sqrt3\,i = 2e^{-i\pi/3}$. By (4),
>
> $$
> (1 - \sqrt3\,i)^5 = 2^5e^{-i5\pi/3} = 32e^{i\pi/3} = 32\Big(\frac12 + \frac{\sqrt3}{2}i\Big) = 16 + 16\sqrt3\,i ,
> $$
>
> since $-\frac{5\pi}{3} + 2\pi = \frac\pi3$ and $e^{i2\pi} = 1$.
>
> **(b)** The number $1 + \sqrt3\,i$ is the conjugate of $1 - \sqrt3\,i$, and the conjugate of a product is the product of the conjugates ((4) of [[§6 Complex Conjugates#^thm-6-1|Theorem §6.1]], applied four times), so $\bar z^5 = \overline{z^5}$. Hence, from (a),
>
> $$
> (1 + \sqrt3\,i)^5 = \overline{16 + 16\sqrt3\,i} = 16 - 16\sqrt3\,i = 32e^{-i\pi/3} .
> $$
>
> *Source: 342 HW 1, Problem 3(b)–(c)*

^ex-8-2

> [!example] Example §8.3: Multiple-Angle Identities
> **(a)** Formula (6) with $n = 2$ gives $(\cos\theta + i\sin\theta)^2 = \cos 2\theta + i\sin 2\theta$, or
>
> $$
> \cos^2\theta - \sin^2\theta + i\,2\sin\theta\cos\theta = \cos 2\theta + i\sin 2\theta .
> $$
>
> Equating real parts and then imaginary parts gives the familiar identities $\cos 2\theta = \cos^2\theta - \sin^2\theta$ and $\sin 2\theta = 2\sin\theta\cos\theta$.
>
> **(b)** With $n = 3$, expand the left side of (6) by the binomial formula ([[§3 Further Algebraic Properties#^thm-3-4|Theorem §3.4]]), using $i^2 = -1$, $i^3 = -i$:
>
> $$
> (\cos\theta + i\sin\theta)^3 = \cos^3\theta + 3i\cos^2\theta\sin\theta - 3\cos\theta\sin^2\theta - i\sin^3\theta .
> $$
>
> Equating real and imaginary parts with $\cos 3\theta + i\sin 3\theta$:
>
> $$
> \cos 3\theta = \cos^3\theta - 3\cos\theta\sin^2\theta, \qquad \sin 3\theta = 3\cos^2\theta\sin\theta - \sin^3\theta .
> $$
>
> *B&C: Sec. 8, Example 2; Sec. 9, Exercise 10*

^ex-8-3
