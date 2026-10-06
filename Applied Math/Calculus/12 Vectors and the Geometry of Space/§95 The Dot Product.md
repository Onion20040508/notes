---
type: section
subject: "[[Calculus]]"
chapter: 12
section: 95
stewart: "12.3"
aliases: ["Stewart 12.3"]
tags: [calculus, math233]
---
← [[§94 Vectors]] · ↑ [[· 12 Vectors and the Geometry of Space]] · [[§96 The Cross Product]] →

*Stewart, Section 12.3 · MATH 233 (UMass, Spring 2023): Midterm 1 Practice Questions (Q1, Q5).*

The dot product multiplies two vectors and returns a number: multiply corresponding components and add. Its meaning is geometric. By the Law of Cosines, $\mathbf{a} \cdot \mathbf{b} = |\mathbf{a}||\mathbf{b}|\cos\theta$, so the dot product measures angles, and in particular two vectors are perpendicular exactly when their dot product is $0$. The same formula gives the direction cosines of a vector, the projection of one vector onto another (the "shadow" of $\mathbf{b}$ on the line of $\mathbf{a}$), and the work done by a constant force. Projections reappear in the distance formulas of [[§98 Equations of Lines and Planes|§98]] (for instance [[§98 Equations of Lines and Planes#^thm-98-8|Theorem §98.8]], the distance from a point to a plane).

## The Dot Product of Two Vectors

> [!definition] Definition §111.1: Dot Product
> If $\mathbf{a} = \langle a_1, a_2, a_3 \rangle$ and $\mathbf{b} = \langle b_1, b_2, b_3 \rangle$, then the **dot product** of $\mathbf{a}$ and $\mathbf{b}$ is the number
>
> $$
> \mathbf{a} \cdot \mathbf{b} = a_1b_1 + a_2b_2 + a_3b_3 .
> $$
>
> For two-dimensional vectors, $\langle a_1, a_2 \rangle \cdot \langle b_1, b_2 \rangle = a_1b_1 + a_2b_2$. Because the result is a scalar, not a vector, the dot product is also called the **scalar product** (or **inner product**).
>
> *Stewart: 12.3, Definition 1*

^def-95-1

> [!remark]- Connections
> - The same definition on $\mathbb{R}^n$, and the model for an abstract inner product: [[§20 Inner Products and Norms#^ladr-6-1|LADR 6.1]], [[§20 Inner Products and Norms#^ladr-6-2|LADR 6.2]].
> - Matrix version: [[§49 Inner Product, Length, and Orthogonality#^def-49-1|235 Def. §49.1]] (the inner product $\mathbf{u}^T\mathbf{v}$ in $\mathbb{R}^n$, a $1 \times n$ times an $n \times 1$ matrix), with the properties of [[§95 The Dot Product#^thm-95-1|Theorem §95.1]] as [[§49 Inner Product, Length, and Orthogonality#^thm-49-1|235 Thm. §49.1]].

> [!theorem] Theorem §111.1: Properties of the Dot Product
> If $\mathbf{a}$, $\mathbf{b}$ and $\mathbf{c}$ are vectors in $V_3$ and $c$ is a scalar, then
>
> $$
> \begin{array}{ll}
> 1.\ \mathbf{a} \cdot \mathbf{a} = |\mathbf{a}|^2 & 2.\ \mathbf{a} \cdot \mathbf{b} = \mathbf{b} \cdot \mathbf{a} \\
> 3.\ \mathbf{a} \cdot (\mathbf{b} + \mathbf{c}) = \mathbf{a} \cdot \mathbf{b} + \mathbf{a} \cdot \mathbf{c} & 4.\ (c\mathbf{a}) \cdot \mathbf{b} = c(\mathbf{a} \cdot \mathbf{b}) = \mathbf{a} \cdot (c\mathbf{b}) \\
> 5.\ \mathbf{0} \cdot \mathbf{a} = 0 &
> \end{array}
> $$
>
> *Stewart: 12.3, Theorem 2*

^thm-95-1

> [!proof]+ Proof
> Write $\mathbf{a} = \langle a_1, a_2, a_3 \rangle$, $\mathbf{b} = \langle b_1, b_2, b_3 \rangle$, $\mathbf{c} = \langle c_1, c_2, c_3 \rangle$ and use [[§95 The Dot Product#^def-95-1|Definition §95.1]]. (Stewart proves 1 and 3 and leaves the rest as exercises.)
>
> 1. $\mathbf{a} \cdot \mathbf{a} = a_1^2 + a_2^2 + a_3^2 = |\mathbf{a}|^2$ by [[§94 Vectors#^thm-94-3|Theorem §94.3]].
> 2. $\mathbf{a} \cdot \mathbf{b} = a_1b_1 + a_2b_2 + a_3b_3 = b_1a_1 + b_2a_2 + b_3a_3 = \mathbf{b} \cdot \mathbf{a}$.
> 3. Since $\mathbf{b} + \mathbf{c} = \langle b_1 + c_1, b_2 + c_2, b_3 + c_3 \rangle$,
>
> $$
> \begin{aligned}
> \mathbf{a} \cdot (\mathbf{b} + \mathbf{c}) &= a_1(b_1 + c_1) + a_2(b_2 + c_2) + a_3(b_3 + c_3) \\
> &= (a_1b_1 + a_2b_2 + a_3b_3) + (a_1c_1 + a_2c_2 + a_3c_3) = \mathbf{a} \cdot \mathbf{b} + \mathbf{a} \cdot \mathbf{c} .
> \end{aligned}
> $$
>
> 4. $(c\mathbf{a}) \cdot \mathbf{b} = (ca_1)b_1 + (ca_2)b_2 + (ca_3)b_3 = c(a_1b_1 + a_2b_2 + a_3b_3) = c(\mathbf{a} \cdot \mathbf{b})$, and the same computation with $a_i(cb_i)$ gives $\mathbf{a} \cdot (c\mathbf{b}) = c(\mathbf{a} \cdot \mathbf{b})$.
> 5. $\mathbf{0} \cdot \mathbf{a} = 0a_1 + 0a_2 + 0a_3 = 0$.

^pf-95-1

*Uses:* [[§95 The Dot Product#^def-95-1|Def. §95.1]], [[§94 Vectors#^thm-94-3|§94.3]], [[§94 Vectors#^thm-94-4|§94.4]]

> [!definition] Definition §111.2: Angle Between Two Vectors
> The **angle $\theta$ between $\mathbf{a}$ and $\mathbf{b}$** is the angle, with $0 \le \theta \le \pi$, between representations of $\mathbf{a}$ and $\mathbf{b}$ that start at the origin: the angle between the segments $\overrightarrow{OA}$ and $\overrightarrow{OB}$. If $\mathbf{a}$ and $\mathbf{b}$ are parallel, then $\theta = 0$ or $\theta = \pi$.
>
> *Stewart: 12.3 (text)*

^def-95-2

> [!theorem] Theorem §111.2: The Dot Product and the Angle
> If $\theta$ is the angle between the vectors $\mathbf{a}$ and $\mathbf{b}$, then
>
> $$
> \mathbf{a} \cdot \mathbf{b} = |\mathbf{a}|\,|\mathbf{b}| \cos\theta .
> $$
>
> *Stewart: 12.3, Theorem 3*

^thm-95-2

> [!proof]+ Proof
> Let $\mathbf{a} = \overrightarrow{OA}$ and $\mathbf{b} = \overrightarrow{OB}$. Apply the Law of Cosines ([[§142 Trigonometry#^thm-142-6|Theorem §142.6]]) to the triangle $OAB$:
>
> $$
> |AB|^2 = |OA|^2 + |OB|^2 - 2|OA|\,|OB| \cos\theta . \qquad (4)
> $$
>
> (The Law of Cosines still holds in the limiting cases $\theta = 0$ or $\pi$, and $\mathbf{a} = \mathbf{0}$ or $\mathbf{b} = \mathbf{0}$, where the "triangle" is degenerate.) Here $|OA| = |\mathbf{a}|$, $|OB| = |\mathbf{b}|$, and $\overrightarrow{BA} = \mathbf{a} - \mathbf{b}$ ([[§94 Vectors#^def-94-4|Definition §94.4]]), so $|AB| = |\mathbf{a} - \mathbf{b}|$ and (4) becomes
>
> $$
> |\mathbf{a} - \mathbf{b}|^2 = |\mathbf{a}|^2 + |\mathbf{b}|^2 - 2|\mathbf{a}|\,|\mathbf{b}| \cos\theta . \qquad (5)
> $$
>
> By Properties 1, 2 and 3 of [[§95 The Dot Product#^thm-95-1|Theorem §95.1]] (with Property 4 for the minus signs), the left side is
>
> $$
> |\mathbf{a} - \mathbf{b}|^2 = (\mathbf{a} - \mathbf{b}) \cdot (\mathbf{a} - \mathbf{b}) = \mathbf{a} \cdot \mathbf{a} - \mathbf{a} \cdot \mathbf{b} - \mathbf{b} \cdot \mathbf{a} + \mathbf{b} \cdot \mathbf{b} = |\mathbf{a}|^2 - 2\,\mathbf{a} \cdot \mathbf{b} + |\mathbf{b}|^2 .
> $$
>
> Substituting in (5) and cancelling $|\mathbf{a}|^2 + |\mathbf{b}|^2$ gives $-2\,\mathbf{a} \cdot \mathbf{b} = -2|\mathbf{a}|\,|\mathbf{b}| \cos\theta$, that is, $\mathbf{a} \cdot \mathbf{b} = |\mathbf{a}|\,|\mathbf{b}| \cos\theta$.

^pf-95-2

*Uses:* [[§95 The Dot Product#^thm-95-1|§95.1]], [[§95 The Dot Product#^def-95-2|Def. §95.2]], [[§94 Vectors#^def-94-4|Def. §94.4]], [[§142 Trigonometry#^thm-142-6|§142.6]] (Law of Cosines)

> [!remark]- Connections
> - Since $|\cos\theta| \le 1$, the theorem gives $|\mathbf{a} \cdot \mathbf{b}| \le |\mathbf{a}|\,|\mathbf{b}|$, the Cauchy–Schwarz inequality, [[§20 Inner Products and Norms#^ladr-6-14|LADR 6.14]]. In $\mathbb{R}^n$ there is no picture to measure angles, and the logic runs the other way: Cauchy–Schwarz is proved first, and then $\cos\theta = \mathbf{a} \cdot \mathbf{b}/(|\mathbf{a}||\mathbf{b}|)$ is the *definition* of the angle.
> - Matrix version: [[§50 Orthogonal Complements and Angles#^thm-50-5|235 Thm. §50.5]] (the same law-of-cosines proof, and the formula as the definition of the angle for $n > 3$).

> [!theorem] Corollary §111.3: The Angle from the Dot Product
> If $\theta$ is the angle between the nonzero vectors $\mathbf{a}$ and $\mathbf{b}$, then
>
> $$
> \cos\theta = \frac{\mathbf{a} \cdot \mathbf{b}}{|\mathbf{a}|\,|\mathbf{b}|} .
> $$
>
> *Stewart: 12.3, Corollary 6*

^cor-95-3

> [!proof]+ Proof
> Divide both sides of [[§95 The Dot Product#^thm-95-2|Theorem §95.2]] by $|\mathbf{a}|\,|\mathbf{b}|$, which is nonzero because neither vector is $\mathbf{0}$.

^pf-95-3

*Uses:* [[§95 The Dot Product#^thm-95-2|§95.2]]

> [!example] Example §111.1: Dot Products and Angles
> **(a)** Directly from [[§95 The Dot Product#^def-95-1|Definition §95.1]]:
>
> $$
> \begin{aligned}
> \langle 2, 4 \rangle \cdot \langle 3, -1 \rangle &= 2(3) + 4(-1) = 2, \\
> \langle -1, 7, 4 \rangle \cdot \langle 6, 2, -\tfrac12 \rangle &= (-1)(6) + 7(2) + 4(-\tfrac12) = 6, \\
> (\mathbf{i} + 2\mathbf{j} - 3\mathbf{k}) \cdot (2\mathbf{j} - \mathbf{k}) &= 1(0) + 2(2) + (-3)(-1) = 7 .
> \end{aligned}
> $$
>
> **(b)** If $|\mathbf{a}| = 4$, $|\mathbf{b}| = 6$ and the angle between them is $\pi/3$, then by [[§95 The Dot Product#^thm-95-2|Theorem §95.2]], $\mathbf{a} \cdot \mathbf{b} = 4 \cdot 6 \cdot \cos(\pi/3) = 4 \cdot 6 \cdot \frac12 = 12$.
>
> **(c)** Find the angle between $\mathbf{a} = \langle 2, 2, -1 \rangle$ and $\mathbf{b} = \langle 5, -3, 2 \rangle$. Here
>
> $$
> |\mathbf{a}| = \sqrt{4 + 4 + 1} = 3, \qquad |\mathbf{b}| = \sqrt{25 + 9 + 4} = \sqrt{38}, \qquad \mathbf{a} \cdot \mathbf{b} = 2(5) + 2(-3) + (-1)(2) = 2 ,
> $$
>
> so by [[§95 The Dot Product#^cor-95-3|Corollary §95.3]], $\cos\theta = \dfrac{2}{3\sqrt{38}}$ and $\theta = \cos^{-1}\!\left(\dfrac{2}{3\sqrt{38}}\right) \approx 1.46$ (about $84^\circ$).
>
> *Stewart: Examples 12.3.1, 12.3.2 and 12.3.3*

^ex-95-1

> [!definition] Definition §111.3: Orthogonal Vectors
> Two nonzero vectors $\mathbf{a}$ and $\mathbf{b}$ are **perpendicular** or **orthogonal** if the angle between them is $\theta = \pi/2$. The zero vector $\mathbf{0}$ is considered to be perpendicular to all vectors.
>
> *Stewart: 12.3 (text)*

^def-95-3

> [!theorem] Theorem §111.4: Test for Orthogonality
> Two vectors $\mathbf{a}$ and $\mathbf{b}$ are orthogonal if and only if $\mathbf{a} \cdot \mathbf{b} = 0$.
>
> *Stewart: 12.3, Equation 7*

^thm-95-4

> [!proof]+ Proof
> If $\mathbf{a} = \mathbf{0}$ or $\mathbf{b} = \mathbf{0}$, both statements are true: the vectors are orthogonal by convention, and $\mathbf{a} \cdot \mathbf{b} = 0$ by Property 5 of [[§95 The Dot Product#^thm-95-1|Theorem §95.1]]. Otherwise, if the vectors are orthogonal then $\mathbf{a} \cdot \mathbf{b} = |\mathbf{a}||\mathbf{b}|\cos(\pi/2) = 0$ by [[§95 The Dot Product#^thm-95-2|Theorem §95.2]]. Conversely, if $\mathbf{a} \cdot \mathbf{b} = 0$ then $\cos\theta = 0$ by [[§95 The Dot Product#^cor-95-3|Corollary §95.3]], and the only $\theta$ in $[0, \pi]$ with $\cos\theta = 0$ is $\theta = \pi/2$.

^pf-95-4

*Uses:* [[§95 The Dot Product#^def-95-3|Def. §95.3]], [[§95 The Dot Product#^thm-95-1|§95.1]], [[§95 The Dot Product#^thm-95-2|§95.2]], [[§95 The Dot Product#^cor-95-3|§95.3]]

> [!remark]- Connections
> - Matrix version: the orthogonality test becomes the definition in $\mathbb{R}^n$, [[§49 Inner Product, Length, and Orthogonality#^def-49-5|235 Def. §49.5]], with the Pythagorean theorem [[§49 Inner Product, Length, and Orthogonality#^thm-49-4|235 Thm. §49.4]].

> [!remark] Remark: The Sign of the Dot Product
> Since $\cos\theta > 0$ for $0 \le \theta < \pi/2$ and $\cos\theta < 0$ for $\pi/2 < \theta \le \pi$, the dot product $\mathbf{a} \cdot \mathbf{b}$ (of nonzero vectors) is positive when $\theta$ is acute, $0$ when the vectors are perpendicular, and negative when $\theta$ is obtuse. It measures how far $\mathbf{a}$ and $\mathbf{b}$ point in the same direction. In the extreme cases, $\mathbf{a} \cdot \mathbf{b} = |\mathbf{a}||\mathbf{b}|$ when they point in exactly the same direction ($\theta = 0$) and $\mathbf{a} \cdot \mathbf{b} = -|\mathbf{a}||\mathbf{b}|$ when they point in opposite directions ($\theta = \pi$).

^rem-95-1

> [!example] Example §111.2: Testing and Forcing Orthogonality
> **(a)** $2\mathbf{i} + 2\mathbf{j} - \mathbf{k}$ is perpendicular to $5\mathbf{i} - 4\mathbf{j} + 2\mathbf{k}$, since
>
> $$
> (2\mathbf{i} + 2\mathbf{j} - \mathbf{k}) \cdot (5\mathbf{i} - 4\mathbf{j} + 2\mathbf{k}) = 2(5) + 2(-4) + (-1)(2) = 0 .
> $$
>
> **(b)** For which $k$ is $\mathbf{v} = \langle 1, 3, k \rangle$ orthogonal to $\langle 1, -12, -7 \rangle$? By [[§95 The Dot Product#^thm-95-4|Theorem §95.4]] we need
>
> $$
> \langle 1, 3, k \rangle \cdot \langle 1, -12, -7 \rangle = 1 - 36 - 7k = 0 ,
> $$
>
> so $-7k = 35$ and $k = -5$.
>
> *Stewart: Example 12.3.4*
> *Source: 233 Midterm 1 Practice Questions, Q5*

^ex-95-2

## Direction Angles and Direction Cosines

> [!definition] Definition §112.1: Direction Angles and Direction Cosines
> The **direction angles** of a nonzero vector $\mathbf{a}$ are the angles $\alpha$, $\beta$, $\gamma$ (in $[0, \pi]$) that $\mathbf{a}$ makes with the positive $x$-, $y$- and $z$-axes. Their cosines $\cos\alpha$, $\cos\beta$, $\cos\gamma$ are the **direction cosines** of $\mathbf{a}$.
>
> *Stewart: 12.3 (text)*

^def-95-4

> [!theorem] Proposition §112.1: Formulas for the Direction Cosines
> For a nonzero vector $\mathbf{a} = \langle a_1, a_2, a_3 \rangle$,
>
> $$
> \cos\alpha = \frac{a_1}{|\mathbf{a}|}, \qquad \cos\beta = \frac{a_2}{|\mathbf{a}|}, \qquad \cos\gamma = \frac{a_3}{|\mathbf{a}|} ,
> $$
>
> and consequently
>
> $$
> \cos^2\alpha + \cos^2\beta + \cos^2\gamma = 1, \qquad \frac{1}{|\mathbf{a}|}\,\mathbf{a} = \langle \cos\alpha, \cos\beta, \cos\gamma \rangle .
> $$
>
> So the direction cosines of $\mathbf{a}$ are the components of the unit vector in the direction of $\mathbf{a}$.
>
> *Stewart: 12.3, Equations 8–11*

^prop-95-5

> [!proof]+ Proof
> The positive $x$-axis has the direction of $\mathbf{i}$, so $\alpha$ is the angle between $\mathbf{a}$ and $\mathbf{i}$. By [[§95 The Dot Product#^cor-95-3|Corollary §95.3]], with $|\mathbf{i}| = 1$,
>
> $$
> \cos\alpha = \frac{\mathbf{a} \cdot \mathbf{i}}{|\mathbf{a}|\,|\mathbf{i}|} = \frac{a_1 \cdot 1 + a_2 \cdot 0 + a_3 \cdot 0}{|\mathbf{a}|} = \frac{a_1}{|\mathbf{a}|} ,
> $$
>
> and the same computation with $\mathbf{j}$ and $\mathbf{k}$ gives $\cos\beta$ and $\cos\gamma$. Squaring and adding,
>
> $$
> \cos^2\alpha + \cos^2\beta + \cos^2\gamma = \frac{a_1^2 + a_2^2 + a_3^2}{|\mathbf{a}|^2} = 1 .
> $$
>
> Finally $\mathbf{a} = \langle |\mathbf{a}|\cos\alpha, |\mathbf{a}|\cos\beta, |\mathbf{a}|\cos\gamma \rangle = |\mathbf{a}|\langle \cos\alpha, \cos\beta, \cos\gamma \rangle$; divide by $|\mathbf{a}|$.

^pf-95-5

*Uses:* [[§95 The Dot Product#^def-95-4|Def. §95.4]], [[§95 The Dot Product#^cor-95-3|§95.3]], [[§94 Vectors#^thm-94-3|§94.3]]

> [!example] Example §111.3: Direction Angles
> Find the direction angles of $\mathbf{a} = \langle 1, 2, 3 \rangle$.
>
> Since $|\mathbf{a}| = \sqrt{1 + 4 + 9} = \sqrt{14}$, [[§95 The Dot Product#^prop-95-5|Proposition §95.5]] gives $\cos\alpha = 1/\sqrt{14}$, $\cos\beta = 2/\sqrt{14}$, $\cos\gamma = 3/\sqrt{14}$, so
>
> $$
> \alpha = \cos^{-1}\!\Big(\frac{1}{\sqrt{14}}\Big) \approx 74^\circ, \qquad \beta = \cos^{-1}\!\Big(\frac{2}{\sqrt{14}}\Big) \approx 58^\circ, \qquad \gamma = \cos^{-1}\!\Big(\frac{3}{\sqrt{14}}\Big) \approx 37^\circ .
> $$
>
> Check: $\frac{1}{14} + \frac{4}{14} + \frac{9}{14} = 1$.
>
> *Stewart: Example 12.3.5*

^ex-95-3

## Projections

> [!definition] Definition §112.2: Vector Projection
> Let $\mathbf{a} = \overrightarrow{PQ}$ and $\mathbf{b} = \overrightarrow{PR}$ have the same initial point $P$, and let $S$ be the foot of the perpendicular from $R$ to the line containing $\overrightarrow{PQ}$. The vector with representation $\overrightarrow{PS}$ is the **vector projection of $\mathbf{b}$ onto $\mathbf{a}$**, written $\operatorname{proj}_{\mathbf{a}}\mathbf{b}$ (think of it as the shadow of $\mathbf{b}$).
>
> *Stewart: 12.3 (text)*

^def-95-5

> [!definition] Definition §95.6: Scalar Projection
> The **scalar projection of $\mathbf{b}$ onto $\mathbf{a}$** (also called the **component of $\mathbf{b}$ along $\mathbf{a}$**), written $\operatorname{comp}_{\mathbf{a}}\mathbf{b}$, is the signed magnitude of the vector projection: the number $|\mathbf{b}|\cos\theta$, where $\theta$ is the angle between $\mathbf{a}$ and $\mathbf{b}$. It is negative when $\pi/2 < \theta \le \pi$.
>
> *Stewart: 12.3 (text)*

^def-95-6

![[m233-82-1.svg]]
*The vector projection $\operatorname{proj}_{\mathbf{a}}\mathbf{b}$ (red) is the shadow of $\mathbf{b}$ on the line of $\mathbf{a}$: drop the perpendicular from the tip $R$ of $\mathbf{b}$ to that line. Its signed length is $|\mathbf{b}|\cos\theta = \operatorname{comp}_{\mathbf{a}}\mathbf{b}$. (a) For an acute angle the shadow points along $\mathbf{a}$. (b) For an obtuse angle it points against $\mathbf{a}$, and the scalar projection is negative.*

> [!theorem] Theorem §112.2: Formulas for Projections
> For $\mathbf{a} \ne \mathbf{0}$,
>
> $$
> \operatorname{comp}_{\mathbf{a}}\mathbf{b} = \frac{\mathbf{a} \cdot \mathbf{b}}{|\mathbf{a}|}, \qquad
> \operatorname{proj}_{\mathbf{a}}\mathbf{b} = \left( \frac{\mathbf{a} \cdot \mathbf{b}}{|\mathbf{a}|} \right) \frac{\mathbf{a}}{|\mathbf{a}|} = \frac{\mathbf{a} \cdot \mathbf{b}}{|\mathbf{a}|^2}\,\mathbf{a} .
> $$
>
> The vector projection is the scalar projection times the unit vector in the direction of $\mathbf{a}$. Equivalently, $\mathbf{a} \cdot \mathbf{b} = |\mathbf{a}|\,(\operatorname{comp}_{\mathbf{a}}\mathbf{b})$: the dot product is the length of $\mathbf{a}$ times the scalar projection of $\mathbf{b}$ onto $\mathbf{a}$.
>
> *Stewart: 12.3 (boxed formulas)*

^thm-95-6

> [!proof]+ Proof
> By [[§95 The Dot Product#^thm-95-2|Theorem §95.2]],
>
> $$
> \operatorname{comp}_{\mathbf{a}}\mathbf{b} = |\mathbf{b}|\cos\theta = \frac{|\mathbf{a}|\,|\mathbf{b}|\cos\theta}{|\mathbf{a}|} = \frac{\mathbf{a} \cdot \mathbf{b}}{|\mathbf{a}|} = \frac{\mathbf{a}}{|\mathbf{a}|} \cdot \mathbf{b} .
> $$
>
> The vector $\overrightarrow{PS}$ lies along the line of $\mathbf{a}$, so it is a multiple of the unit vector $\mathbf{a}/|\mathbf{a}|$. Its length is $|\mathbf{b}||\cos\theta|$ (in the right triangle $PSR$ the hypotenuse is $|\mathbf{b}|$ and the angle at $P$ is $\theta$ or $\pi - \theta$), and it points along $\mathbf{a}$ when $\theta < \pi/2$ and against $\mathbf{a}$ when $\theta > \pi/2$. In every case $\overrightarrow{PS} = (|\mathbf{b}|\cos\theta)\,\mathbf{a}/|\mathbf{a}|$, which is the stated formula. (When $\theta = \pi/2$, $S = P$ and both sides are $\mathbf{0}$.)

^pf-95-6

*Uses:* [[§95 The Dot Product#^def-95-5|Def. §95.5]], [[§95 The Dot Product#^def-95-6|Def. §95.6]], [[§95 The Dot Product#^thm-95-2|§95.2]], [[§94 Vectors#^prop-94-7|§94.7]]

> [!remark]- Connections
> - $\operatorname{proj}_{\mathbf{a}}\mathbf{b}$ is the orthogonal projection onto the line $\operatorname{span}(\mathbf{a})$, [[§22 Orthogonal Complements and Minimization Problems#^ladr-6-56|LADR 6.56]], and $\mathbf{b} = \operatorname{proj}_{\mathbf{a}}\mathbf{b} + (\mathbf{b} - \operatorname{proj}_{\mathbf{a}}\mathbf{b})$ is the orthogonal decomposition of [[§20 Inner Products and Norms#^ladr-6-13|LADR 6.13]]. The foot $S$ is the point of the line closest to $R$: [[§22 Orthogonal Complements and Minimization Problems#^ladr-6-61|LADR 6.61]].
> - Matrix version: [[§51 Orthogonal Sets#^def-51-3|235 Def. §51.3]] (projection onto a line in $\mathbb{R}^n$, $\hat{\mathbf{y}} = \frac{\mathbf{y} \cdot \mathbf{u}}{\mathbf{u} \cdot \mathbf{u}}\mathbf{u}$) and [[§51 Orthogonal Sets#^prop-51-3|235 Prop. §51.3]] (the decomposition $\mathbf{y} = \hat{\mathbf{y}} + \mathbf{z}$), worked in [[§51 Orthogonal Sets#^ex-51-2|235 Ex. §51.2]].

> [!example] Example §112.1: Projections
> **(a)** Find the scalar and vector projections of $\mathbf{b} = \langle 1, 1, 2 \rangle$ onto $\mathbf{a} = \langle -2, 3, 1 \rangle$.
>
> Here $|\mathbf{a}| = \sqrt{4 + 9 + 1} = \sqrt{14}$ and $\mathbf{a} \cdot \mathbf{b} = (-2)(1) + 3(1) + 1(2) = 3$, so by [[§95 The Dot Product#^thm-95-6|Theorem §95.6]]
>
> $$
> \operatorname{comp}_{\mathbf{a}}\mathbf{b} = \frac{3}{\sqrt{14}}, \qquad \operatorname{proj}_{\mathbf{a}}\mathbf{b} = \frac{3}{\sqrt{14}}\,\frac{\mathbf{a}}{|\mathbf{a}|} = \frac{3}{14}\,\mathbf{a} = \Big\langle -\frac37, \frac{9}{14}, \frac{3}{14} \Big\rangle .
> $$
>
> **(b)** For $\mathbf{a} = \mathbf{i} + \mathbf{j} + \mathbf{k}$ and $\mathbf{b} = \mathbf{i} - \mathbf{j} + \mathbf{k}$, find $\operatorname{proj}_{\mathbf{a}}\mathbf{b}$ and the exact angle between $\mathbf{a}$ and $\mathbf{b}$.
>
> Here $\mathbf{a} \cdot \mathbf{b} = 1 - 1 + 1 = 1$ and $|\mathbf{a}|^2 = |\mathbf{b}|^2 = 3$. So
>
> $$
> \operatorname{proj}_{\mathbf{a}}\mathbf{b} = \frac{1}{3}\,\langle 1, 1, 1 \rangle = \Big\langle \frac13, \frac13, \frac13 \Big\rangle, \qquad \cos\theta = \frac{1}{\sqrt3\,\sqrt3} = \frac13, \qquad \theta = \arccos\frac13 .
> $$
>
> *Stewart: Example 12.3.6*
> *Source: 233 Midterm 1 Practice Questions, Q1*

^ex-95-4

## Application: Work

> [!definition] Definition §95.7: Work Done by a Constant Force
> Suppose a constant force $\mathbf{F} = \overrightarrow{PR}$ moves an object from $P$ to $Q$. The **displacement vector** is $\mathbf{D} = \overrightarrow{PQ}$, and the **work** done by the force is the component of the force along $\mathbf{D}$ times the distance moved:
>
> $$
> W = (|\mathbf{F}|\cos\theta)\,|\mathbf{D}| ,
> $$
>
> where $\theta$ is the angle between $\mathbf{F}$ and $\mathbf{D}$. This extends $W = Fd$ of [[§48 Work#^def-48-2|Definition §48.2]], where the force was directed along the line of motion.
>
> *Stewart: 12.3 (text)*

^def-95-7

> [!theorem] Proposition §112.3: Work as a Dot Product
> The work done by a constant force $\mathbf{F}$ with displacement vector $\mathbf{D}$ is
>
> $$
> W = \mathbf{F} \cdot \mathbf{D} .
> $$
>
> *Stewart: 12.3, Equation 12*

^prop-95-7

> [!proof]+ Proof
> By [[§95 The Dot Product#^def-95-7|Definition §95.7]] and [[§95 The Dot Product#^thm-95-2|Theorem §95.2]], $W = |\mathbf{F}|\,|\mathbf{D}|\cos\theta = \mathbf{F} \cdot \mathbf{D}$.

^pf-95-7

*Uses:* [[§95 The Dot Product#^def-95-7|Def. §95.7]], [[§95 The Dot Product#^thm-95-2|§95.2]]

> [!example] Example §112.2: Computing Work
> **(a)** A wagon is pulled $100$ m along a horizontal path by a constant force of $70$ N, the handle held at $35^\circ$ above the horizontal. By [[§95 The Dot Product#^prop-95-7|Proposition §95.7]],
>
> $$
> W = \mathbf{F} \cdot \mathbf{D} = |\mathbf{F}|\,|\mathbf{D}|\cos 35^\circ = (70)(100)\cos 35^\circ \approx 5734\ \text{N}\cdot\text{m} = 5734\ \text{J} .
> $$
>
> **(b)** The force $\mathbf{F} = 3\mathbf{i} + 4\mathbf{j} + 5\mathbf{k}$ moves a particle from $P(2, 1, 0)$ to $Q(4, 6, 2)$. The displacement vector is $\mathbf{D} = \overrightarrow{PQ} = \langle 2, 5, 2 \rangle$, so
>
> $$
> W = \langle 3, 4, 5 \rangle \cdot \langle 2, 5, 2 \rangle = 6 + 20 + 10 = 36 ,
> $$
>
> that is, $36$ J if lengths are in meters and forces in newtons.
>
> *Stewart: Examples 12.3.7 and 12.3.8*

^ex-95-5
