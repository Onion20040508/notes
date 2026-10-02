---
type: section
subject: "[[Applied Linear Algebra]]"
chapter: 8
section: 53
lay: "Appendix B"
aliases: ["Lay Appendix B"]
tags: [applied-linear-algebra, math235]
---
← [[§52★ Applications to Image Processing and Statistics]] · ↑ [[· 8 Complex Numbers]]

*Lay, Appendix B · MATH 235 lecture L21.*

Complex numbers $a + bi$ are needed in linear algebra because real matrices can have non-real eigenvalues: $\begin{bmatrix} 0 & 1 \\ -4 & 0 \end{bmatrix}$ has characteristic polynomial $\lambda^2 + 4 = (\lambda - 2i)(\lambda + 2i)$ ([[§36 Complex Eigenvalues#^ex-36-1|Example §36.1]]). This appendix collects the arithmetic: addition and multiplication, the conjugate $\bar z$ and absolute value $|z|$ (with $z\bar z = |z|^2$, which gives division), and the geometry of the complex plane. In polar form, multiplication multiplies absolute values and adds arguments, so multiplying by a number of absolute value $1$ is a rotation. Powers follow by De Moivre's Theorem. The lecture adds Euler's formula $e^{i\varphi} = \cos\varphi + i\sin\varphi$ and the $2 \times 2$ real matrices that act like complex numbers.

## Arithmetic of Complex Numbers

> [!definition] Definition §53.1: Complex Numbers
> A **complex number** is a number written in the form
>
> $$
> z = a + bi ,
> $$
>
> where $a$ and $b$ are real numbers and $i$ is a formal symbol satisfying the relation $i^2 = -1$. The number $a$ is the **real part** of $z$, denoted $\operatorname{Re} z$, and $b$ is the **imaginary part** of $z$, denoted $\operatorname{Im} z$. Two complex numbers are equal if and only if their real parts are equal and their imaginary parts are equal. For example, if $z = 5 + (-2)i$, then $\operatorname{Re} z = 5$ and $\operatorname{Im} z = -2$; for simplicity we write $z = 5 - 2i$.
>
> A real number $a$ is regarded as a special complex number by identifying $a$ with $a + 0i$. The **complex number system**, denoted $\mathbb{C}$, is the set of all complex numbers together with the operations
>
> $$
> \begin{aligned}
> (a + bi) + (c + di) &= (a + c) + (b + d)i , && (1) \\
> (a + bi)(c + di) &= (ac - bd) + (ad + bc)i . && (2)
> \end{aligned}
> $$
>
> When $b = d = 0$ these reduce to ordinary addition and multiplication of real numbers.
>
> *Lay: Appendix B, Definition and Equations (1)–(2)*

^def-53-1

> [!theorem] Theorem §53.1: The Laws of Arithmetic Hold in ℂ
> The usual laws of arithmetic for $\mathbb{R}$ also hold for $\mathbb{C}$: addition and multiplication are commutative and associative, multiplication distributes over addition, $0$ and $1$ are identities, and every $z$ has an additive inverse. (Multiplicative inverses: Proposition §53.4.) For this reason, multiplication is usually computed by algebraic expansion: multiply each term by each term, use $i^2 = -1$, and collect the result in the form $a + bi$.
>
> *Lay: Appendix B (text)*

^thm-53-1

*Lay omits the proof ("it is readily checked"); each law reduces to the same law in $\mathbb{R}$ through (1)–(2), as in [[§1 Rⁿ and Cⁿ#^ladr-1-3|LADR 1.3]].*

> [!remark]- Connections
> - Rigorous treatment: [[§1 Rⁿ and Cⁿ#^ladr-1-1|LADR 1.1]] defines $\mathbb{C}$ as ordered pairs $(a, b)$ with the operations (1)–(2), which removes the vagueness of a "formal symbol $i$"; [[§1 Rⁿ and Cⁿ#^ladr-1-3|LADR 1.3]] lists and proves the field properties, and the conjugate and absolute value are [[§13 Polynomials#^ladr-4-2|LADR 4.2]].

> [!definition] Definition §53.2: Subtraction
> Subtraction of complex numbers $z_1$ and $z_2$ is defined by
>
> $$
> z_1 - z_2 = z_1 + (-1)z_2 .
> $$
>
> In particular, we write $-z$ in place of $(-1)z$.
>
> *Lay: Appendix B (text)*

^def-53-2

> [!example] Example §53.1: Multiplying Complex Numbers
> **(a)** Multiply each term of $5 - 2i$ by each term of $3 + 4i$ and use $i^2 = -1$:
>
> $$
> (5 - 2i)(3 + 4i) = 15 + 20i - 6i - 8i^2 = 15 + 14i - 8(-1) = 23 + 14i .
> $$
>
> **(b)** By formula (2) with $a = 3$, $b = 4$, $c = 7$, $d = -1$:
>
> $$
> (3 + 4i)(7 - i) = \big(3 \cdot 7 - 4 \cdot (-1)\big) + \big(3 \cdot (-1) + 4 \cdot 7\big)i = (21 + 4) + (-3 + 28)i = 25 + 25i .
> $$
>
> By expansion: $21 - 3i + 28i - 4i^2 = 21 + 25i + 4 = 25 + 25i$.
>
> *The lecture writes the real part as $21 - 4 = 17$ and gets $17 + 25i$; since $d = -1$, the term $-bd$ is $+4$, and the product is $25 + 25i$.*
>
> *Lay: Appendix B, Example 1 (part (a)); Source: 235 lecture L21 (part (b))*

^ex-53-1

> [!definition] Definition §53.3: Conjugate
> The **conjugate** of $z = a + bi$ is the complex number $\bar z$ (read "$z$ bar") defined by
>
> $$
> \bar z = a - bi .
> $$
>
> Obtain $\bar z$ from $z$ by reversing the sign of the imaginary part. For example, $\overline{-3 + 4i} = -3 - 4i$.
>
> *Lay: Appendix B, Definition; Example 2*

^def-53-3

> [!theorem] Proposition §53.2: z Times Its Conjugate
> If $z = a + bi$, then
>
> $$
> z\bar z = a^2 + b^2 . \qquad (3)
> $$
>
> In particular, $z\bar z$ is real and nonnegative, and it is $0$ only for $z = 0$.
>
> *Lay: Appendix B, Equation (3)*

^prop-53-2

> [!proof]+ Proof
> Expand, using $i^2 = -1$:
>
> $$
> z\bar z = (a + bi)(a - bi) = a^2 - abi + bai - b^2i^2 = a^2 + b^2 .
> $$
>
> (The lecture reads this as a difference of squares, $a^2 - (bi)^2$.) A sum of squares of real numbers is $\ge 0$, and it is $0$ only when $a = b = 0$.

^pf-53-2

*Uses:* [[§53 Complex Numbers#^def-53-1|Def. §53.1]], [[§53 Complex Numbers#^def-53-3|Def. §53.3]], [[§53 Complex Numbers#^thm-53-1|§53.1]]

> [!definition] Definition §53.4: Absolute Value
> Since $z\bar z$ is real and nonnegative, it has a square root. The **absolute value** (or **modulus**) of $z$ is the real number $|z|$ defined by
>
> $$
> |z| = \sqrt{z\bar z} = \sqrt{a^2 + b^2} .
> $$
>
> If $z$ is a real number, then $z = a + 0i$ and $|z| = \sqrt{a^2}$, which equals the ordinary absolute value of $a$.
>
> *Lay: Appendix B, Definition*

^def-53-4

> [!theorem] Theorem §53.3: Properties of Conjugates and Absolute Value
> For complex numbers $w$ and $z$:
> 1. $\bar z = z$ if and only if $z$ is a real number.
> 2. $\overline{w + z} = \bar w + \bar z$.
> 3. $\overline{wz} = \bar w\,\bar z$; in particular, $\overline{rz} = r\bar z$ if $r$ is a real number.
> 4. $z\bar z = |z|^2 \ge 0$.
> 5. $|wz| = |w|\,|z|$.
> 6. $|w + z| \le |w| + |z|$.
>
> *Lay: Appendix B (text)*

^thm-53-3

*Lay lists these without proof; all are proved in [[§13 Polynomials#^ladr-4-4|LADR 4.4]] (properties 1–4 are direct computations from (1)–(3); 5 follows from 3 and 4, $|wz|^2 = wz\,\overline{wz} = w\bar w\,z\bar z$; 6 is the triangle inequality).*

> [!theorem] Proposition §53.4: Reciprocals and Quotients
> If $z \ne 0$, then $|z| > 0$ and $z$ has a multiplicative inverse, denoted $1/z$ or $z^{-1}$ and given by
>
> $$
> \frac1z = z^{-1} = \frac{\bar z}{|z|^2} .
> $$
>
> A quotient $w/z$ means $w \cdot (1/z)$. In practice: multiply numerator and denominator by $\bar z$, which makes the denominator the real number $|z|^2$.
>
> *Lay: Appendix B (text)*

^prop-53-4

> [!proof]+ Proof
> By (3), $|z|^2 = a^2 + b^2 > 0$ for $z \ne 0$, so $\bar z/|z|^2$ makes sense (a complex number times the real number $1/|z|^2$). Then, by (3) again,
>
> $$
> z \cdot \frac{\bar z}{|z|^2} = \frac{z\bar z}{|z|^2} = \frac{|z|^2}{|z|^2} = 1 ,
> $$
>
> and also $\frac{\bar z}{|z|^2} \cdot z = 1$ by commutativity. So $\bar z/|z|^2$ is an inverse of $z$. It is the only one: if $zv = 1$ too, then $v = (z^{-1}z)v = z^{-1}(zv) = z^{-1}$.

^pf-53-4

*Uses:* [[§53 Complex Numbers#^prop-53-2|§53.2]], [[§53 Complex Numbers#^def-53-4|Def. §53.4]], [[§53 Complex Numbers#^thm-53-1|§53.1]]

> [!example] Example §53.2: Conjugates, Absolute Values and Quotients
> **(a)** Let $w = 3 + 4i$ and $z = 5 - 2i$. Compute $z\bar z$, $|z|$ and $w/z$.
>
> From (3), $z\bar z = 5^2 + (-2)^2 = 25 + 4 = 29$, so $|z| = \sqrt{z\bar z} = \sqrt{29}$. To compute $w/z$, multiply numerator and denominator by $\bar z = 5 + 2i$, the conjugate of the denominator; by (3) this eliminates the $i$ in the denominator:
>
> $$
> \frac wz = \frac{3 + 4i}{5 - 2i} = \frac{3 + 4i}{5 - 2i} \cdot \frac{5 + 2i}{5 + 2i} = \frac{15 + 6i + 20i + 8i^2}{5^2 + (-2)^2} = \frac{15 - 8 + 26i}{29} = \frac{7 + 26i}{29} = \frac{7}{29} + \frac{26}{29}i .
> $$
>
> **(b)** By Proposition §53.4, with $|2 + 3i|^2 = 4 + 9 = 13$,
>
> $$
> (2 + 3i)^{-1} = \frac{2 - 3i}{13} = \frac{2}{13} - \frac{3}{13}i .
> $$
>
> Check: $(2 + 3i)(2 - 3i) = 4 + 9 = 13$, so $(2 + 3i) \cdot \frac{2 - 3i}{13} = 1$.
>
> *Lay: Appendix B, Example 3 (part (a)); Source: 235 lecture L21 (part (b))*

^ex-53-2

## Geometric Interpretation

> [!definition] Definition §53.5: The Complex Plane
> Each complex number $z = a + bi$ corresponds to the point $(a, b)$ in the plane $\mathbb{R}^2$. The horizontal axis is called the **real axis**, because its points $(a, 0)$ correspond to the real numbers. The vertical axis is the **imaginary axis**, because its points $(0, b)$ correspond to the **pure imaginary numbers** $0 + bi$, or simply $bi$. In this picture:
> - the conjugate $\bar z$ is the mirror image of $z$ in the real axis;
> - the absolute value $|z|$ is the distance from $(a, b)$ to the origin;
> - addition of $z = a + bi$ and $w = c + di$ corresponds to vector addition of $(a, b)$ and $(c, d)$ in $\mathbb{R}^2$ (the parallelogram rule).
>
> *Lay: Appendix B (text; Figures 1–2)*

^def-53-5

> [!definition] Definition §53.6: Argument; Polar Form
> Let $z = a + bi$ be a nonzero complex number, and let $\varphi$ be the angle between the positive real axis and the point $(a, b)$, with $-\pi < \varphi \le \pi$. The angle $\varphi$ is called the **argument** of $z$; we write $\varphi = \arg z$. These are **polar coordinates** in $\mathbb{R}^2$: from trigonometry, $a = |z|\cos\varphi$ and $b = |z|\sin\varphi$, so
>
> $$
> z = a + bi = |z|(\cos\varphi + i\sin\varphi) .
> $$
>
> *Lay: Appendix B (text)*

^def-53-6

![[m235-53-1.svg]]
*(a) The point $z = a + bi$ at distance $|z|$ and angle $\varphi = \arg z$ from the origin; its legs are $a = |z|\cos\varphi$ and $b = |z|\sin\varphi$, and the conjugate $\bar z$ is its mirror image in the real axis. (b) Example §53.3: multiplying by $i$ (absolute value $1$, argument $\pi/2$) rotates $z = 3 + i$ through a right angle to $iz = -1 + 3i$, without changing its length.*

> [!theorem] Theorem §53.5: Multiplication and Division in Polar Form
> If $z = |z|(\cos\varphi + i\sin\varphi)$ and $w = |w|(\cos\vartheta + i\sin\vartheta)$ are nonzero, then
>
> $$
> wz = |w|\,|z|\,\big[\cos(\vartheta + \varphi) + i\sin(\vartheta + \varphi)\big] \qquad (4)
> $$
>
> and
>
> $$
> \frac wz = \frac{|w|}{|z|}\big[\cos(\vartheta - \varphi) + i\sin(\vartheta - \varphi)\big] .
> $$
>
> In words: the product of two nonzero complex numbers is given in polar form by the product of their absolute values and the sum of their arguments. The quotient of two nonzero complex numbers is given by the quotient of their absolute values and the difference of their arguments.
>
> *Lay: Appendix B, Equation (4) and boxed statement*

^thm-53-5

> [!proof]+ Proof
> (Lay: "using standard trigonometric identities ... one can verify"; here is the verification.) By (2) and the addition formulas $\cos(\vartheta + \varphi) = \cos\vartheta\cos\varphi - \sin\vartheta\sin\varphi$ and $\sin(\vartheta + \varphi) = \sin\vartheta\cos\varphi + \cos\vartheta\sin\varphi$,
>
> $$
> \begin{aligned}
> wz &= |w|\,|z|\,(\cos\vartheta + i\sin\vartheta)(\cos\varphi + i\sin\varphi) \\
> &= |w|\,|z|\,\big[(\cos\vartheta\cos\varphi - \sin\vartheta\sin\varphi) + i(\cos\vartheta\sin\varphi + \sin\vartheta\cos\varphi)\big] \\
> &= |w|\,|z|\,\big[\cos(\vartheta + \varphi) + i\sin(\vartheta + \varphi)\big] .
> \end{aligned}
> $$
>
> For the quotient, let $q = \frac{|w|}{|z|}\big[\cos(\vartheta - \varphi) + i\sin(\vartheta - \varphi)\big]$. By (4), applied to $q$ and $z$, $qz = \frac{|w|}{|z|}|z|\big[\cos(\vartheta - \varphi + \varphi) + i\sin(\vartheta - \varphi + \varphi)\big] = w$. Multiplying by $1/z$ gives $q = w/z$.

^pf-53-5

*Uses:* [[§53 Complex Numbers#^def-53-6|Def. §53.6]], [[§53 Complex Numbers#^prop-53-4|§53.4]], [[§119 Trigonometry#^thm-119-6|Calc Thm. §119.6]] (addition formulas)

Strictly, the sum $\vartheta + \varphi$ in (4) is *an* argument of $wz$; it may have to be shifted by $\pm 2\pi$ to land in $(-\pi, \pi]$.

> [!example] Example §53.3: Multiplication as Rotation
> **(a)** If $w$ has absolute value $1$, then $w = \cos\vartheta + i\sin\vartheta$, where $\vartheta$ is the argument of $w$. By (4), $wz = |z|\big[\cos(\vartheta + \varphi) + i\sin(\vartheta + \varphi)\big]$: multiplication of any nonzero number $z$ by $w$ keeps $|z|$ and adds $\vartheta$ to the argument. It simply rotates $z$ through the angle $\vartheta$.
>
> **(b)** The argument of $i = \cos\frac\pi2 + i\sin\frac\pi2$ is $\pi/2$ radians, so multiplication of $z$ by $i$ rotates $z$ through an angle of $\pi/2$ radians. For example, $3 + i$ is rotated into
>
> $$
> (3 + i)i = 3i + i^2 = -1 + 3i .
> $$
>
> Check: $|3 + i| = \sqrt{10} = |-1 + 3i|$, and the vectors $(3, 1)$ and $(-1, 3)$ are perpendicular, $(3)(-1) + (1)(3) = 0$.
>
> *Lay: Appendix B, Example 4*

^ex-53-3

## Powers of a Complex Number

Formula (4) applies when $z = w = r(\cos\varphi + i\sin\varphi)$:

$$
z^2 = r^2(\cos 2\varphi + i\sin 2\varphi), \qquad
z^3 = z \cdot z^2 = r(\cos\varphi + i\sin\varphi) \cdot r^2(\cos 2\varphi + i\sin 2\varphi) = r^3(\cos 3\varphi + i\sin 3\varphi) .
$$

> [!theorem] Theorem §53.6: De Moivre's Theorem
> If $z = r(\cos\varphi + i\sin\varphi)$, then for any positive integer $k$,
>
> $$
> z^k = r^k(\cos k\varphi + i\sin k\varphi) .
> $$
>
> *Lay: Appendix B (text)*

^thm-53-6

> [!proof]+ Proof
> (Lay shows $k = 2, 3$ and says "in general".) Induction on $k$. For $k = 1$ there is nothing to prove. If $z^k = r^k(\cos k\varphi + i\sin k\varphi)$, then by (4), applied to $z^k$ and $z$,
>
> $$
> z^{k+1} = z^k \cdot z = r^k \cdot r\,\big[\cos(k\varphi + \varphi) + i\sin(k\varphi + \varphi)\big] = r^{k+1}\big[\cos(k+1)\varphi + i\sin(k+1)\varphi\big] .
> $$

^pf-53-6

*Uses:* [[§53 Complex Numbers#^thm-53-5|§53.5]]

> [!remark] Remark: Euler's Formula
> The lecture writes the polar form with the complex exponential. Defining $e^z$ for complex $z$ by the exponential series $e^z = 1 + \frac{z}{1!} + \frac{z^2}{2!} + \frac{z^3}{3!} + \cdots$ and substituting $z = i\varphi$, the powers $i^2 = -1$, $i^3 = -i$, $i^4 = 1, \dots$ split the series into its real and imaginary terms:
>
> $$
> e^{i\varphi} = \Big(1 - \frac{\varphi^2}{2!} + \frac{\varphi^4}{4!} - \frac{\varphi^6}{6!} + \cdots\Big) + i\Big(\varphi - \frac{\varphi^3}{3!} + \frac{\varphi^5}{5!} - \frac{\varphi^7}{7!} + \cdots\Big) = \cos\varphi + i\sin\varphi ,
> $$
>
> the two series being the Maclaurin series of cosine and sine ([[§78 Taylor and Maclaurin Series#^thm-78-6|Calc Thm. §78.6]], [[§78 Taylor and Maclaurin Series#^thm-78-7|Calc Thm. §78.7]], [[§78 Taylor and Maclaurin Series#^thm-78-8|Calc Thm. §78.8]]; regrouping is allowed because the series converges absolutely). Consequences:
> - $e^{i\pi} = \cos\pi + i\sin\pi = -1$, that is, $e^{i\pi} + 1 = 0$;
> - every $z \ne 0$ is $z = |z|\,e^{i\varphi}$ with $\varphi = \arg z$;
> - $\overline{e^{i\varphi}} = \cos\varphi - i\sin\varphi = e^{-i\varphi}$, so $|e^{i\varphi}|^2 = e^{i\varphi}e^{-i\varphi} = 1$.
>
> In this notation (4) and De Moivre's Theorem read $|w|e^{i\vartheta} \cdot |z|e^{i\varphi} = |w||z|\,e^{i(\vartheta + \varphi)}$ and $(re^{i\varphi})^k = r^ke^{ik\varphi}$: the usual laws of exponents.
>
> *Source: 235 lecture L21*

^rem-53-1

> [!remark]- Connections
> - ODE version: [[§15 Complex Roots of the Characteristic Equation#^def-15-1|331 Def. §15.1]] (the complex exponential $e^{(\lambda + i\mu)t} = e^{\lambda t}(\cos\mu t + i\sin\mu t)$, which BDP takes as a definition after the same series argument, [[§15 Complex Roots of the Characteristic Equation#^rem-15-1|331 §15, Remark: Where Euler's Formula Comes From]]); its law of exponents and derivative rule, [[§15 Complex Roots of the Characteristic Equation#^prop-15-1|331 Prop. §15.1]]; used to turn complex roots of $ay'' + by' + cy = 0$ into real solutions, [[§15 Complex Roots of the Characteristic Equation#^thm-15-2|331 Thm. §15.2]].

## Complex Numbers and ℝ²

> [!remark] Remark: ℂ Is More Than ℝ²
> The elements of $\mathbb{R}^2$ and $\mathbb{C}$ are in one-to-one correspondence, $(a, b) \leftrightarrow a + bi$, and the operations of addition are essentially the same. But there is a logical distinction: in $\mathbb{R}^2$ we can only multiply a vector by a real scalar, whereas in $\mathbb{C}$ we can multiply any two complex numbers to obtain a third complex number. (The dot product in $\mathbb{R}^2$ does not count, because it produces a scalar, not an element of $\mathbb{R}^2$.) Scalar notation for elements of $\mathbb{C}$ emphasizes this distinction: the points $(2, 4)$, $(-1, 2)$, $(-3, -1)$, $(3, -2)$, $(4, 0)$ of $\mathbb{R}^2$ are written $2 + 4i$, $-1 + 2i$, $-3 - i$, $3 - 2i$, $4 + 0i$ as points of $\mathbb{C}$.

^rem-53-2

> [!remark] Remark: Complex Numbers as 2 × 2 Matrices
> Multiplication by $a + bi$ is a linear transformation of $\mathbb{R}^2 = \mathbb{C}$: by (2), $(a + bi)(x + yi) = (ax - by) + (bx + ay)i$, so its standard matrix is
>
> $$
> M_{a + bi} = \begin{bmatrix} a & -b \\ b & a \end{bmatrix}, \qquad \det M_{a+bi} = a^2 + b^2 = |a + bi|^2 .
> $$
>
> Its characteristic polynomial is $(a - \lambda)^2 + b^2 = \lambda^2 - 2a\lambda + (a^2 + b^2)$, with roots
>
> $$
> \lambda = \frac{2a \pm \sqrt{4a^2 - 4(a^2 + b^2)}}{2} = a \pm \sqrt{-b^2} = a \pm bi :
> $$
>
> the eigenvalues of $M_{a+bi}$ are $a + bi$ and its conjugate $a - bi$. With $r = \sqrt{a^2 + b^2}$, $\cos\varphi = a/r$ and $\sin\varphi = b/r$,
>
> $$
> M_{a + bi} = r \begin{bmatrix} a/r & -b/r \\ b/r & a/r \end{bmatrix} = r \begin{bmatrix} \cos\varphi & -\sin\varphi \\ \sin\varphi & \cos\varphi \end{bmatrix},
> $$
>
> a scaling by $|z|$ composed with the rotation by $\arg z$, which is Theorem §53.5 in matrix form. This is the model for every real $2 \times 2$ matrix with complex eigenvalues ([[§36 Complex Eigenvalues#^thm-36-4|Theorem §36.4]]).
>
> *Source: 235 lecture L21*

^rem-53-3

> [!remark]- Connections
> - Non-real roots of a real polynomial, and hence non-real eigenvalues of a real matrix, come in conjugate pairs $\lambda, \bar\lambda$ (take conjugates in $p(\lambda) = 0$, using properties 2–3 of Theorem §53.3): [[§13 Polynomials#^ladr-4-14|LADR 4.14]]. That every polynomial has a root in $\mathbb{C}$ is the fundamental theorem of algebra, [[§13 Polynomials#^ladr-4-12|LADR 4.12]] (hub [[Fundamental theorem of algebra, first version]]).
