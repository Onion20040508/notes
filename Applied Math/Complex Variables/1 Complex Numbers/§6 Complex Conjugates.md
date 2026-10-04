---
type: section
subject: "[[Complex Variables]]"
chapter: 1
section: 6
bc: "6"
aliases: ["B&C 6"]
tags: [complex-variables, math342]
---
← [[§5 Triangle Inequality]] · ↑ [[· 1 Complex Numbers]] · [[§7 Exponential Form]] →

*Brown–Churchill, Section 6 · MAT 342 HW 1.*

The conjugate $\bar z = x - iy$ is the mirror image of $z$ in the real axis. Conjugation respects all four arithmetic operations, recovers the real and imaginary parts as $(z + \bar z)/2$ and $(z - \bar z)/(2i)$, and is tied to the modulus by the single identity $z\bar z = |z|^2$. That identity is the reason division works by "multiplying by the conjugate", and it gives one-line proofs of $|z_1z_2| = |z_1||z_2|$ and of the triangle inequality. Conjugates are also the natural way to write curves: a condition on $x$ and $y$ becomes a condition on $z$ and $\bar z$.

## The Conjugate

> [!definition] Definition §6.1: Complex Conjugate
> The **complex conjugate**, or simply the conjugate, of $z = x + iy$ is the complex number
>
> $$
> \bar z = x - iy . \qquad (1)
> $$
>
> It is represented by the point $(x, -y)$, the reflection in the real axis of the point $(x, y)$ representing $z$. Directly from (1) and the definition of the modulus, $\bar{\bar z} = z$ and $|\bar z| = |z|$ for all $z$.
>
> *B&C: Sec. 6, Equation (1)*

^def-6-1

> [!theorem] Theorem §6.1: Conjugates of Sums, Differences, Products and Quotients
> For all complex numbers $z_1$, $z_2$,
>
> $$
> \overline{z_1 + z_2} = \bar z_1 + \bar z_2 , \qquad (2) \qquad\qquad \overline{z_1 - z_2} = \bar z_1 - \bar z_2 , \qquad (3)
> $$
>
> $$
> \overline{z_1z_2} = \bar z_1\,\bar z_2 , \qquad (4) \qquad\qquad \overline{\Big(\frac{z_1}{z_2}\Big)} = \frac{\bar z_1}{\bar z_2} \quad (z_2 \ne 0) . \qquad (5)
> $$
>
> *B&C: Sec. 6, Equations (2)–(5)*

^thm-6-1

> [!proof]+ Proof
> Let $z_1 = x_1 + iy_1$, $z_2 = x_2 + iy_2$.
>
> **(2), (3)** $\overline{z_1 \pm z_2} = (x_1 \pm x_2) - i(y_1 \pm y_2) = (x_1 - iy_1) \pm (x_2 - iy_2) = \bar z_1 \pm \bar z_2$.
>
> **(4)** (B&C: "easy to show"; Exercise 3.) Since $z_1z_2 = (x_1x_2 - y_1y_2) + i(y_1x_2 + x_1y_2)$,
>
> $$
> \overline{z_1z_2} = (x_1x_2 - y_1y_2) - i(y_1x_2 + x_1y_2) ,
> $$
>
> while, by the product rule (8) of §1,
>
> $$
> \bar z_1\,\bar z_2 = (x_1 - iy_1)(x_2 - iy_2) = \big(x_1x_2 - (-y_1)(-y_2)\big) + i\big((-y_1)x_2 + x_1(-y_2)\big) = (x_1x_2 - y_1y_2) - i(y_1x_2 + x_1y_2) .
> $$
>
> **(5)** Let $w = z_1/z_2$, so that $z_1 = wz_2$. By (4), $\bar z_1 = \bar w\,\bar z_2$. Since $z_2 \ne 0$, also $\bar z_2 \ne 0$ (as $\bar{\bar z}_2 = z_2$), and dividing gives $\bar w = \bar z_1/\bar z_2$.

^pf-6-1

*Uses:* [[§6 Complex Conjugates#^def-6-1|Def. §6.1]], [[§1 Sums and Products#^prop-1-2|§1.2]], [[§3 Further Algebraic Properties#^def-3-1|Def. §3.1]]

> [!remark]- Connections
> - Linear Algebra's conjugate and its properties: [[§13 Polynomials#^ladr-4-2|LADR 4.2]], [[§13 Polynomials#^ladr-4-4|LADR 4.4]]. Computational version: [[§53 Complex Numbers#^def-53-3|235 Def. §53.3]], [[§53 Complex Numbers#^thm-53-3|235 Thm. §53.3]].

> [!theorem] Proposition §6.2: Real and Imaginary Parts Through Conjugates
> For $z = x + iy$, $z + \bar z = 2x$ and $z - \bar z = 2iy$. Hence
>
> $$
> \operatorname{Re} z = \frac{z + \bar z}{2} \qquad\text{and}\qquad \operatorname{Im} z = \frac{z - \bar z}{2i} . \qquad (6)
> $$
>
> *B&C: Sec. 6, Equation (6)*

^prop-6-2

> [!proof]+ Proof
> $(x + iy) + (x - iy) = 2x$ and $(x + iy) - (x - iy) = 2iy$; divide by $2$ and by $2i$.

^pf-6-2

*Uses:* [[§6 Complex Conjugates#^def-6-1|Def. §6.1]]

## Conjugates and Moduli

> [!theorem] Proposition §6.3: z Times Its Conjugate
> For every complex number $z$,
>
> $$
> z\bar z = |z|^2 , \qquad (7)
> $$
>
> where each side equals $x^2 + y^2$.
>
> *B&C: Sec. 6, Equation (7)*

^prop-6-3

> [!proof]+ Proof
> By (8) of §1, $(x + iy)(x - iy) = \big(x^2 - y(-y)\big) + i\big(yx + x(-y)\big) = x^2 + y^2$, which is $|z|^2$ by (1) of §4.

^pf-6-3

*Uses:* [[§6 Complex Conjugates#^def-6-1|Def. §6.1]], [[§1 Sums and Products#^prop-1-2|§1.2]], [[§4 Vectors and Moduli#^def-4-1|Def. §4.1]]

Identity (7) explains the [[§3 Further Algebraic Properties#^rem-3-1|Method — Dividing Complex Numbers]]: to find $z_1/z_2$, multiply numerator and denominator by $\bar z_2$, so that the denominator becomes the real number $|z_2|^2$. In particular $z^{-1} = \bar z/|z|^2$ for $z \ne 0$, which is formula (6) of §2.

> [!theorem] Theorem §6.4: Moduli of Products and Quotients
> For all complex numbers $z_1$, $z_2$,
>
> $$
> |z_1z_2| = |z_1||z_2| , \qquad (8) \qquad\qquad \Big|\frac{z_1}{z_2}\Big| = \frac{|z_1|}{|z_2|} \quad (z_2 \ne 0) . \qquad (9)
> $$
>
> *B&C: Sec. 6, Equations (8)–(9); Exercise 5*

^thm-6-4

> [!proof]+ Proof
> Identity (7) turns properties of conjugates into properties of moduli. By (7), (4) and the commutative and associative laws,
>
> $$
> |z_1z_2|^2 = (z_1z_2)\big(\overline{z_1z_2}\big) = (z_1z_2)(\bar z_1\,\bar z_2) = (z_1\bar z_1)(z_2\bar z_2) = |z_1|^2|z_2|^2 = \big(|z_1||z_2|\big)^2 ,
> $$
>
> and since a modulus is never negative, (8) follows. For (9) (B&C: "verified in a similar way"), by (7), (5) and the quotient rule (12) of §3,
>
> $$
> \Big|\frac{z_1}{z_2}\Big|^2 = \frac{z_1}{z_2}\cdot\frac{\bar z_1}{\bar z_2} = \frac{z_1\bar z_1}{z_2\bar z_2} = \frac{|z_1|^2}{|z_2|^2} ,
> $$
>
> and taking nonnegative square roots gives (9). (Identity (8) was proved in coordinates in [[§5 Triangle Inequality#^prop-5-4|Proposition §5.4]]; the conjugate proof avoids the expansion.)

^pf-6-4

*Uses:* [[§6 Complex Conjugates#^thm-6-1|§6.1]], [[§6 Complex Conjugates#^prop-6-3|§6.3]], [[§3 Further Algebraic Properties#^prop-3-3|§3.3]], [[§2 Basic Algebraic Properties#^thm-2-1|§2.1]]

> [!remark]- Remark: The Triangle Inequality Through Conjugates
> B&C's Exercise 15 derives the triangle inequality ([[§5 Triangle Inequality#^thm-5-1|Theorem §5.1]]) from (7). By (7) and (2),
>
> $$
> |z_1 + z_2|^2 = (z_1 + z_2)(\bar z_1 + \bar z_2) = z_1\bar z_1 + \big(z_1\bar z_2 + \overline{z_1\bar z_2}\big) + z_2\bar z_2 ,
> $$
>
> using $\overline{z_1\bar z_2} = \bar z_1z_2$ by (4). By (6) and (3) of §4, and (8),
>
> $$
> z_1\bar z_2 + \overline{z_1\bar z_2} = 2\operatorname{Re}(z_1\bar z_2) \le 2|z_1\bar z_2| = 2|z_1||z_2| .
> $$
>
> Hence $|z_1 + z_2|^2 \le |z_1|^2 + 2|z_1||z_2| + |z_2|^2 = (|z_1| + |z_2|)^2$, and the triangle inequality follows by taking square roots. In coordinates, $\operatorname{Re}(z_1\bar z_2) = x_1x_2 + y_1y_2$ is the dot product of the two vectors, which is how the proof of Theorem §5.1 was written.

^rem-6-1

## Examples

> [!example] Example §6.1: Dividing by Way of the Conjugate
> **(a)** Compute $\dfrac{-1 + 3i}{2 - i}$. **(b)** Let $z = 2 - 3i$ and $w = 3 + i$. Write $\dfrac{z + 2w}{1 - z\bar w}$ in the form $a + bi$.
>
> **(a)** Multiply numerator and denominator by $\overline{2 - i} = 2 + i$:
>
> $$
> \frac{-1 + 3i}{2 - i} = \frac{(-1 + 3i)(2 + i)}{(2 - i)(2 + i)} = \frac{-5 + 5i}{|2 - i|^2} = \frac{-5 + 5i}{5} = -1 + i .
> $$
>
> **(b)** The numerator is $z + 2w = 2 - 3i + 6 + 2i = 8 - i$. With $\bar w = 3 - i$,
>
> $$
> z\bar w = (2 - 3i)(3 - i) = 6 - 2i - 9i + 3i^2 = 3 - 11i, \qquad 1 - z\bar w = -2 + 11i .
> $$
>
> Multiplying by the conjugate $-2 - 11i$ of the denominator, with $|-2 + 11i|^2 = 4 + 121 = 125$,
>
> $$
> \frac{8 - i}{-2 + 11i} = \frac{(8 - i)(-2 - 11i)}{125} = \frac{-16 - 88i + 2i + 11i^2}{125} = \frac{-27 - 86i}{125} = -\frac{27}{125} - \frac{86}{125}i .
> $$
>
> *B&C: Sec. 6, Example 1; Source: 342 HW 1, Problem 1*

^ex-6-1

> [!example] Example §6.2: An Identity Between Moduli
> Show that $|(2\bar z + 5)(\sqrt2 - i)| = \sqrt3\,|2z + 5|$.
>
> By (8), $|(2\bar z + 5)(\sqrt2 - i)| = |2\bar z + 5|\,|\sqrt2 - i|$, and $|\sqrt2 - i| = \sqrt{2 + 1} = \sqrt3$. Since $2$ and $5$ are real, (2) and (4) give $\overline{2z + 5} = 2\bar z + 5$, so $|2\bar z + 5| = |\overline{2z + 5}| = |2z + 5|$. Together, $|(2\bar z + 5)(\sqrt2 - i)| = \sqrt3\,|2z + 5|$.
>
> *B&C: Sec. 6, Exercise 1(d); Source: 342 HW 1*

^ex-6-2

> [!example] Example §6.3: A Circle Written With z̄
> Sketch the set $|2\bar z + i| = 4$.
>
> A number and its conjugate have the same modulus, and by (2) and (4) $\overline{2\bar z + i} = 2z - i$. So the condition is $|2z - i| = 4$. By (8), $|2z - i| = |2|\,\big|z - \frac i2\big| = 2\big|z - \frac i2\big|$, and the condition becomes
>
> $$
> \Big|z - \frac i2\Big| = 2 :
> $$
>
> the circle with center $\frac i2 = (0, \frac12)$ and radius $2$. It meets the imaginary axis at $\frac52 i$ and $-\frac32 i$.
>
> *B&C: Sec. 6, Exercise 2(b); Source: 342 HW 1*

^ex-6-3

> [!example] Example §6.4: Bounds on a Disk
> **(a)** If $|z| < 2$, then $|z^3 + 3z^2 - 2z + 1| < 25$. **(b)** If $|z| \le 1$, then $|\operatorname{Re}(2 + \bar z + z^3)| \le 4$.
>
> **(a)** By (8), $|z^2| = |z|^2$ and $|z^3| = |z|^3$. By the generalized triangle inequality (4) of §5,
>
> $$
> |z^3 + 3z^2 - 2z + 1| \le |z|^3 + 3|z|^2 + 2|z| + 1 < 8 + 12 + 4 + 1 = 25 .
> $$
>
> **(b)** By (3) of §4, then (4) of §5, then $|\bar z| = |z|$ and $|z^3| = |z|^3$,
>
> $$
> |\operatorname{Re}(2 + \bar z + z^3)| \le |2 + \bar z + z^3| \le 2 + |\bar z| + |z^3| = 2 + |z| + |z|^3 \le 2 + 1 + 1 = 4 .
> $$
>
> The bound in (b) is sharp: at $z = 1$, $\operatorname{Re}(2 + 1 + 1) = 4$. The bound $25$ in (a) is not: on $|z| < 2$ the modulus stays below $17$, its value at $z = 2$ (by the maximum modulus principle, [[§59 Maximum Modulus Principle#^cor-59-4|Corollary §59.4]], the largest value over $|z| \le 2$ is taken on the circle $|z| = 2$, and a numerical search of the circle gives $17$, at $z = 2$).
>
> *B&C: Sec. 6, Example 2 and Exercise 7; Source: 342 HW 1 (part (b))*

^ex-6-4
