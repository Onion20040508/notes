---
type: section
subject: "[[Complex Variables]]"
chapter: 1
section: 1
bc: "1"
aliases: ["B&C 1"]
tags: [complex-variables, math342]
---
↑ [[· 1 Complex Numbers]] · [[§2 Basic Algebraic Properties]] →

*Brown–Churchill, Section 1.*

Brown–Churchill define a complex number as an ordered pair of real numbers, that is, a point of the plane, and give the plane two operations: addition, which is vector addition, and a multiplication designed so that $(0, 1)(0, 1) = (-1, 0)$. Writing $i$ for $(0, 1)$ turns every pair into $x + iy$, and the product formula becomes ordinary algebra with the single rule $i^2 = -1$. The ordered-pair definition settles what $i$ "is": a point of the plane with a specified multiplication, not a mysterious square root. Everything in the subject is built on these two operations.

## Complex Numbers as Points of the Plane

> [!definition] Definition §1.1: Complex Numbers and the Complex Plane
> **Complex numbers** are ordered pairs $(x, y)$ of real numbers, interpreted as points of the **complex plane** (the $z$ plane) with rectangular coordinates $x$ and $y$. A complex number is customarily denoted by $z$:
>
> $$
> z = (x, y) . \qquad (1)
> $$
>
> - The real number $x$ is identified with the point $(x, 0)$ of the **real axis**, so the real numbers form a subset of the complex numbers: $x = (x, 0)$.
> - The numbers $(0, y)$ with $y \ne 0$ are **pure imaginary numbers**, and the $y$ axis is the **imaginary axis**.
>
> *B&C: Sec. 1 (text)*

^def-1-1

> [!definition] Definition §1.2: Real and Imaginary Parts; Equality
> For $z = (x, y)$, the real numbers $x$ and $y$ are the **real part** and the **imaginary part** of $z$:
>
> $$
> x = \operatorname{Re} z, \qquad y = \operatorname{Im} z . \qquad (2)
> $$
>
> Two complex numbers are **equal**, $z_1 = z_2$, when they have the same real parts and the same imaginary parts, that is, when they are the same point of the plane.
>
> *B&C: Sec. 1 (text)*

^def-1-2

> [!definition] Definition §1.3: Sum and Product
> The **sum** and **product** of $z_1 = (x_1, y_1)$ and $z_2 = (x_2, y_2)$ are
>
> $$
> (x_1, y_1) + (x_2, y_2) = (x_1 + x_2,\ y_1 + y_2), \qquad (3)
> $$
>
> $$
> (x_1, y_1)(x_2, y_2) = (x_1x_2 - y_1y_2,\ y_1x_2 + x_1y_2) . \qquad (4)
> $$
>
> *B&C: Sec. 1, Equations (3) and (4)*

^def-1-3

The sum is the familiar addition of vectors in $\mathbb{R}^2$. The product is new: it is not a dot product (which gives a real number) or a cross product (which leaves the plane), but a way of multiplying two points of the plane to obtain a third. Its geometric meaning, rotation and scaling, appears in [[§8 Products and Powers in Exponential Form|§8]].

> [!theorem] Proposition §1.1: ℂ Extends ℝ
> Restricted to the real numbers $(x, 0)$, the operations (3) and (4) are the usual addition and multiplication of real numbers:
>
> $$
> (x_1, 0) + (x_2, 0) = (x_1 + x_2, 0), \qquad (x_1, 0)(x_2, 0) = (x_1x_2, 0) .
> $$
>
> So the complex number system is a natural extension of the real number system.
>
> *B&C: Sec. 1 (text)*

^prop-1-1

> [!proof]+ Proof
> Put $y_1 = y_2 = 0$ in (3) and (4): the sum is $(x_1 + x_2, 0 + 0)$ and the product is $(x_1x_2 - 0 \cdot 0,\ 0 \cdot x_2 + x_1 \cdot 0) = (x_1x_2, 0)$.

^pf-1-1

*Uses:* [[§1 Sums and Products#^def-1-3|Def. §1.3]]

## The Form x + iy

> [!theorem] Proposition §1.2: Rectangular Form and i² = −1
> Let $i$ denote the pure imaginary number $(0, 1)$. Then every complex number $z = (x, y)$ can be written
>
> $$
> z = x + iy , \qquad (5)
> $$
>
> and, with the convention $z^2 = zz$, $z^3 = z^2z$, etc.,
>
> $$
> i^2 = -1 . \qquad (6)
> $$
>
> In this notation the definitions (3) and (4) read
>
> $$
> (x_1 + iy_1) + (x_2 + iy_2) = (x_1 + x_2) + i(y_1 + y_2), \qquad (7)
> $$
>
> $$
> (x_1 + iy_1)(x_2 + iy_2) = (x_1x_2 - y_1y_2) + i(y_1x_2 + x_1y_2) . \qquad (8)
> $$
>
> *B&C: Sec. 1, Equations (5)–(8)*

^prop-1-2

> [!proof]+ Proof
> By (4), $(0, 1)(y, 0) = (0 \cdot y - 1 \cdot 0,\ 1 \cdot y + 0 \cdot 0) = (0, y)$. Hence, by (3),
>
> $$
> z = (x, y) = (x, 0) + (0, y) = (x, 0) + (0, 1)(y, 0) ,
> $$
>
> and reading $(x, 0)$ as $x$, $(y, 0)$ as $y$ (Definition §1.1) and $(0, 1)$ as $i$, this is $z = x + iy$. Next, by (4),
>
> $$
> i^2 = (0, 1)(0, 1) = (0 \cdot 0 - 1 \cdot 1,\ 1 \cdot 0 + 0 \cdot 1) = (-1, 0) = -1 .
> $$
>
> Finally, (7) and (8) are (3) and (4) with each pair $(x_k, y_k)$ written as $x_k + iy_k$.

^pf-1-2

*Uses:* [[§1 Sums and Products#^def-1-1|Def. §1.1]], [[§1 Sums and Products#^def-1-3|Def. §1.3]]

> [!remark]- Connections
> - Linear Algebra defines $\mathbb{C}$ the same way, as ordered pairs written $a + bi$ with the operations (3)–(4): [[§1 Rⁿ and Cⁿ#^ladr-1-1|LADR 1.1]], with its arithmetic in [[§1 Rⁿ and Cⁿ#^ladr-1-3|LADR 1.3]].
> - The vault's earlier, computational treatment, where $a + bi$ is introduced with $i^2 = -1$ as a rule: [[§53 Complex Numbers#^def-53-1|235 Def. §53.1]]. This subject is the fuller home.

> [!remark] Remark: Computing With i
> The right sides of (7) and (8) are exactly what one gets by manipulating the left sides as if all the symbols were real numbers and replacing $i^2$ by $-1$ whenever it occurs. That this is always legitimate rests on the commutative, associative and distributive laws of [[§2 Basic Algebraic Properties#^thm-2-1|Theorem §2.1]]; from then on, complex arithmetic is done this way. Equation (8) also shows that **any complex number times zero is zero**:
>
> $$
> z \cdot 0 = (x + iy)(0 + i0) = (x \cdot 0 - y \cdot 0) + i(y \cdot 0 + x \cdot 0) = 0 + i0 = 0 .
> $$
>
> (In electrical engineering the letter $j$ is used instead of $i$.)

^rem-1-1

## Examples

> [!example] Example §1.1: Arithmetic With Pairs
> Verify that **(a)** $(\sqrt2 - i) - i(1 - \sqrt2\,i) = -2i$; **(b)** $(2, -3)(-2, 1) = (-1, 8)$; **(c)** $(3, 1)(3, -1)\big(\frac15, \frac1{10}\big) = (2, 1)$.
>
> **(a)** By (8), $i(1 - \sqrt2\,i) = i - \sqrt2\,i^2 = \sqrt2 + i$. Subtracting real and imaginary parts (subtraction is defined in [[§3 Further Algebraic Properties#^def-3-1|Definition §3.1]]),
>
> $$
> (\sqrt2 - i) - (\sqrt2 + i) = (\sqrt2 - \sqrt2) + i(-1 - 1) = -2i .
> $$
>
> **(b)** By (4) with $x_1 = 2$, $y_1 = -3$, $x_2 = -2$, $y_2 = 1$:
>
> $$
> (2, -3)(-2, 1) = \big(2(-2) - (-3)(1),\ (-3)(-2) + 2 \cdot 1\big) = (-4 + 3,\ 6 + 2) = (-1, 8) .
> $$
>
> **(c)** First $(3, 1)(3, -1) = (9 - (1)(-1),\ 1 \cdot 3 + 3(-1)) = (10, 0)$, a real number. Then
>
> $$
> (10, 0)\Big(\frac15, \frac1{10}\Big) = \Big(10 \cdot \frac15 - 0,\ 0 + 10 \cdot \frac1{10}\Big) = (2, 1) .
> $$
>
> *B&C: Sec. 2, Exercise 1*

^ex-1-1

> [!example] Example §1.2: Multiplying by i
> Show that $\operatorname{Re}(iz) = -\operatorname{Im} z$ and $\operatorname{Im}(iz) = \operatorname{Re} z$.
>
> With $z = (x, y)$ and $i = (0, 1)$, (4) gives
>
> $$
> iz = (0, 1)(x, y) = (0 \cdot x - 1 \cdot y,\ 1 \cdot x + 0 \cdot y) = (-y, x) .
> $$
>
> So $\operatorname{Re}(iz) = -y = -\operatorname{Im} z$ and $\operatorname{Im}(iz) = x = \operatorname{Re} z$. Geometrically, $(x, y) \mapsto (-y, x)$ is the rotation of the plane through $90°$ counterclockwise; [[§8 Products and Powers in Exponential Form|§8]] explains why multiplication by $i$ must be this rotation.
>
> *B&C: Sec. 2, Exercise 2*

^ex-1-2

> [!example] Example §1.3: Checking Roots of a Quadratic
> Verify that each of the two numbers $z = 1 \pm i$ satisfies $z^2 - 2z + 2 = 0$.
>
> By (8), $(1 \pm i)^2 = 1 \pm 2i + i^2 = \pm 2i$. Hence
>
> $$
> z^2 - 2z + 2 = \pm 2i - 2(1 \pm i) + 2 = \pm 2i - 2 \mp 2i + 2 = 0 .
> $$
>
> *B&C: Sec. 2, Exercise 4*

^ex-1-3

> [!example] Example §1.4: Solving z² + z + 1 = 0 With Pairs
> Solve $z^2 + z + 1 = 0$ for $z = (x, y)$ by writing it as $(x, y)(x, y) + (x, y) + (1, 0) = (0, 0)$.
>
> By (4), $(x, y)(x, y) = (x^2 - y^2, 2xy)$, so the equation is
>
> $$
> (x^2 - y^2 + x + 1,\ 2xy + y) = (0, 0), \qquad\text{that is,}\qquad x^2 - y^2 + x + 1 = 0, \quad y(2x + 1) = 0 .
> $$
>
> **$y \ne 0$.** If $y = 0$, the first equation would say $x^2 + x + 1 = 0$ for a real $x$; but $x^2 + x + 1 = (x + \frac12)^2 + \frac34 > 0$. So no real number satisfies the equation, and $y \ne 0$.
>
> **Solve.** Then the second equation forces $2x + 1 = 0$, $x = -\frac12$, and the first becomes $\frac14 - y^2 - \frac12 + 1 = 0$, that is, $y^2 = \frac34$, $y = \pm\frac{\sqrt3}{2}$. So
>
> $$
> z = \Big(-\frac12, \pm\frac{\sqrt3}{2}\Big) = -\frac12 \pm \frac{\sqrt3}{2}\,i .
> $$
>
> These are the two non-real cube roots of unity ([[§11 Examples (Roots of Complex Numbers)#^ex-11-2|Example §11.2]]), as they must be: $z^3 - 1 = (z - 1)(z^2 + z + 1)$.
>
> *B&C: Sec. 2, Exercise 11*

^ex-1-4
