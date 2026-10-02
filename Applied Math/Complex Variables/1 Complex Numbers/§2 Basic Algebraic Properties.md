---
type: section
subject: "[[Complex Variables]]"
chapter: 1
section: 2
bc: "2"
aliases: ["B&C 2"]
tags: [complex-variables, math342]
---
← [[§1 Sums and Products]] · ↑ [[· 1 Complex Numbers]] · [[§3 Further Algebraic Properties]] →

*Brown–Churchill, Section 2.*

The two operations of [[§1 Sums and Products|§1]] obey the same basic laws as real arithmetic: they are commutative and associative, multiplication distributes over addition, $0$ and $1$ are identities, and every number has an additive inverse and, if it is not $0$, a multiplicative inverse. In the language of algebra, $\mathbb{C}$ is a field. Each law is checked by writing both sides as pairs and using the same law for real numbers; the one item that needs a computation is the multiplicative inverse, found by solving a $2 \times 2$ linear system. These laws are what justify computing with $x + iy$ "as if everything were real".

## The Laws of Arithmetic

> [!theorem] Theorem §2.1: Commutative, Associative and Distributive Laws
> For all complex numbers $z, z_1, z_2, z_3$:
>
> $$
> z_1 + z_2 = z_2 + z_1, \qquad z_1z_2 = z_2z_1 , \qquad (1)
> $$
>
> $$
> (z_1 + z_2) + z_3 = z_1 + (z_2 + z_3), \qquad (z_1z_2)z_3 = z_1(z_2z_3) , \qquad (2)
> $$
>
> $$
> z(z_1 + z_2) = zz_1 + zz_2 . \qquad (3)
> $$
>
> *B&C: Sec. 2, Equations (1)–(3)*

^thm-2-1

> [!proof]+ Proof
> B&C say these "follow easily" from the definitions and verify the first one in its Example; here are all five. Write $z = (x, y)$ and $z_k = (x_k, y_k)$, and use [[§1 Sums and Products#^def-1-3|Definition §1.3]] together with the corresponding laws for real numbers.
>
> **Commutative laws** (B&C's Example and Exercise 5).
>
> $$
> z_1 + z_2 = (x_1 + x_2,\ y_1 + y_2) = (x_2 + x_1,\ y_2 + y_1) = z_2 + z_1 ,
> $$
>
> $$
> z_1z_2 = (x_1x_2 - y_1y_2,\ y_1x_2 + x_1y_2) = (x_2x_1 - y_2y_1,\ y_2x_1 + x_2y_1) = z_2z_1 .
> $$
>
> **Associative law for addition** (Exercise 6(a)). Both sides equal $(x_1 + x_2 + x_3,\ y_1 + y_2 + y_3)$, by associativity of real addition.
>
> **Associative law for multiplication.** With $z_1z_2 = (x_1x_2 - y_1y_2,\ y_1x_2 + x_1y_2)$,
>
> $$
> (z_1z_2)z_3 = \big(x_1x_2x_3 - y_1y_2x_3 - y_1x_2y_3 - x_1y_2y_3,\ \ y_1x_2x_3 + x_1y_2x_3 + x_1x_2y_3 - y_1y_2y_3\big) ,
> $$
>
> and with $z_2z_3 = (x_2x_3 - y_2y_3,\ y_2x_3 + x_2y_3)$,
>
> $$
> z_1(z_2z_3) = \big(x_1x_2x_3 - x_1y_2y_3 - y_1y_2x_3 - y_1x_2y_3,\ \ y_1x_2x_3 - y_1y_2y_3 + x_1y_2x_3 + x_1x_2y_3\big) .
> $$
>
> The two pairs contain the same four terms in each component.
>
> **Distributive law** (Exercise 6(b)). Since $z_1 + z_2 = (x_1 + x_2,\ y_1 + y_2)$,
>
> $$
> z(z_1 + z_2) = \big(x(x_1 + x_2) - y(y_1 + y_2),\ y(x_1 + x_2) + x(y_1 + y_2)\big) = (xx_1 - yy_1,\ yx_1 + xy_1) + (xx_2 - yy_2,\ yx_2 + xy_2) = zz_1 + zz_2 .
> $$

^pf-2-1

*Uses:* [[§1 Sums and Products#^def-1-3|Def. §1.3]]

> [!remark]- Connections
> - These, with the identities and inverses below, are the field axioms. Linear Algebra proves the same list the same way, by reduction to $\mathbb{R}$: [[§1 Rⁿ and Cⁿ#^ladr-1-3|LADR 1.3]].
> - The earlier computational treatment states the laws without proof: [[§53 Complex Numbers#^thm-53-1|235 Thm. §53.1]].

By the commutative law for multiplication, $iy = yi$, so one may write $z = x + yi$ instead of $z = x + iy$. By the associative laws, a sum $z_1 + z_2 + z_3$ or a product $z_1z_2z_3$ is well defined without parentheses, as with real numbers.

## Identities and Inverses

> [!theorem] Theorem §2.2: The Identities 0 and 1
> The additive identity $0 = (0, 0)$ and the multiplicative identity $1 = (1, 0)$ for real numbers carry over to the complex numbers:
>
> $$
> z + 0 = z \qquad\text{and}\qquad z \cdot 1 = z \qquad (4)
> $$
>
> for every complex number $z$. Moreover, $0$ and $1$ are the only complex numbers with these properties.
>
> *B&C: Sec. 2, Equation (4) and Exercise 8*

^thm-2-2

> [!proof]+ Proof
> For $z = (x, y)$: $(x, y) + (0, 0) = (x, y)$ and $(x, y)(1, 0) = (x \cdot 1 - y \cdot 0,\ y \cdot 1 + x \cdot 0) = (x, y)$.
>
> **Uniqueness of $0$** (Exercise 8(a)). Suppose $(x, y) + (u, v) = (x, y)$ for some $z = (x, y)$. Then $x + u = x$ and $y + v = y$, so $(u, v) = (0, 0)$. So even a single $z$ determines the additive identity.
>
> **Uniqueness of $1$** (Exercise 8(b)). Suppose $(x, y)(u, v) = (x, y)$ for some $z = (x, y) \ne 0$. Then
>
> $$
> xu - yv = x, \qquad yu + xv = y ,
> $$
>
> a linear system for $u, v$ with determinant $x \cdot x - (-y) \cdot y = x^2 + y^2 \ne 0$. It therefore has exactly one solution, and $(u, v) = (1, 0)$ is a solution. So $(u, v) = (1, 0)$.

^pf-2-2

*Uses:* [[§1 Sums and Products#^def-1-3|Def. §1.3]]

> [!theorem] Theorem §2.3: Additive Inverse
> Each complex number $z = (x, y)$ has an **additive inverse**
>
> $$
> -z = (-x, -y) , \qquad (5)
> $$
>
> satisfying $z + (-z) = 0$, and it is the only number with this property.
>
> *B&C: Sec. 2, Equation (5)*

^thm-2-3

> [!proof]+ Proof
> $(x, y) + (-x, -y) = (0, 0)$. Conversely, $(x, y) + (u, v) = (0, 0)$ means $x + u = 0$ and $y + v = 0$, that is, $u = -x$ and $v = -y$.

^pf-2-3

*Uses:* [[§1 Sums and Products#^def-1-3|Def. §1.3]]

> [!theorem] Theorem §2.4: Multiplicative Inverse
> For any nonzero complex number $z = (x, y)$ there is exactly one number $z^{-1}$ with $zz^{-1} = 1$, namely
>
> $$
> z^{-1} = \Big(\frac{x}{x^2 + y^2},\ \frac{-y}{x^2 + y^2}\Big) \qquad (z \ne 0) . \qquad (6)
> $$
>
> The inverse is not defined when $z = 0$.
>
> *B&C: Sec. 2, Equation (6)*

^thm-2-4

> [!proof]+ Proof
> We seek real numbers $u, v$ with $(x, y)(u, v) = (1, 0)$. By (4) of §1, this is the pair of linear simultaneous equations
>
> $$
> xu - yv = 1, \qquad yu + xv = 0 .
> $$
>
> Its determinant is $x^2 + y^2$, which is positive because $z \ne 0$ means $(x, y) \ne (0, 0)$. So the system has exactly one solution, and by Cramer's rule
>
> $$
> u = \frac{1 \cdot x - (-y) \cdot 0}{x^2 + y^2} = \frac{x}{x^2 + y^2}, \qquad v = \frac{x \cdot 0 - y \cdot 1}{x^2 + y^2} = \frac{-y}{x^2 + y^2} .
> $$
>
> For $z = 0$, $x^2 + y^2 = 0$ and (6) makes no sense; indeed $0 \cdot w = 0 \ne 1$ for every $w$ ([[§1 Sums and Products#^rem-1-1|§1, Remark: Computing With i]]), so $0$ has no inverse.

^pf-2-4

*Uses:* [[§1 Sums and Products#^def-1-3|Def. §1.3]], [[§1 Sums and Products#^rem-1-1|§1 Remark]] ($z \cdot 0 = 0$)

In conjugate form the inverse is $z^{-1} = \bar z/|z|^2$ ([[§6 Complex Conjugates#^prop-6-3|Proposition §6.3]]); compare [[§53 Complex Numbers#^prop-53-4|235 Prop. §53.4]].

## Examples

> [!example] Example §2.1: Distributing Over Three Terms
> Use the associative law for addition and the distributive law to show $z(z_1 + z_2 + z_3) = zz_1 + zz_2 + zz_3$.
>
> By associativity $z_1 + z_2 + z_3 = (z_1 + z_2) + z_3$. Applying (3) twice,
>
> $$
> z\big((z_1 + z_2) + z_3\big) = z(z_1 + z_2) + zz_3 = (zz_1 + zz_2) + zz_3 = zz_1 + zz_2 + zz_3 .
> $$
>
> *B&C: Sec. 2, Exercise 7*

^ex-2-1

> [!example] Example §2.2: Squaring a Binomial
> Show that $(1 + z)^2 = 1 + 2z + z^2$.
>
> By the distributive law (3) (and commutativity (1), to distribute from the right as well),
>
> $$
> (1 + z)(1 + z) = 1(1 + z) + z(1 + z) = (1 + z) + (z + z^2) = 1 + (z + z) + z^2 ,
> $$
>
> using (4) and associativity. Finally $z + z = 2z$: with $z = (x, y)$, $(2, 0)(x, y) = (2x, 2y) = (x, y) + (x, y)$. The general binomial formula is [[§3 Further Algebraic Properties#^thm-3-4|Theorem §3.4]].
>
> *B&C: Sec. 2, Exercise 3*

^ex-2-2

> [!example] Example §2.3: Minus Signs
> **(a)** Use $-1 = (-1, 0)$ and $z = (x, y)$ to show $(-1)z = -z$. **(b)** Use $i = (0, 1)$ and $y = (y, 0)$ to show $-(iy) = (-i)y$, so that the additive inverse of $z = x + iy$ can be written $-z = -x - iy$ without ambiguity.
>
> **(a)** By (4) of §1, $(-1, 0)(x, y) = \big((-1)x - 0 \cdot y,\ 0 \cdot x + (-1)y\big) = (-x, -y)$, which is $-z$ by (5).
>
> **(b)** On one side, $iy = (0, 1)(y, 0) = (0, y)$, so $-(iy) = (0, -y)$ by (5). On the other, $-i = (0, -1)$ by (5), and
>
> $$
> (-i)y = (0, -1)(y, 0) = \big(0 \cdot y - (-1) \cdot 0,\ (-1)y + 0 \cdot 0\big) = (0, -y) .
> $$
>
> So the two readings of "$-iy$" agree, and $-z = (-x, -y) = (-x) + (-iy) = -x - iy$.
>
> *B&C: Sec. 2, Exercises 9 and 10*

^ex-2-3
