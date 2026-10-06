---
type: section
subject: "[[Complex Variables]]"
chapter: 2
section: 13
bc: "13"
aliases: ["B&C 13"]
tags: [complex-variables, math342]
---
← [[§12★ Regions in the Complex Plane]] · ↑ [[· 2 Analytic Functions]] · [[§14 The Mapping w = z²]] →

*Brown–Churchill, Section 13.*

Chapter 2 develops a theory of differentiation for functions of a complex variable, and this section fixes the vocabulary. A function $f$ of $z = x + iy$ is the same thing as a pair of real functions $u(x, y)$, $v(x, y)$ of two real variables, and much of the chapter consists of translating statements about $f$ into statements about $u$ and $v$ and back. Since both $z$ and $w = f(z)$ live in planes, a complex function has no graph that can be drawn; instead one draws the $z$ plane and the $w$ plane side by side and thinks of $f$ as a **mapping** that carries points, curves and regions of the first onto the second. This point of view returns in Chapters 8–11★, where mappings by elementary functions solve problems in electrostatics, steady heat flow and fluid flow.

## Functions of a Complex Variable

> [!definition] Definition §13.1: Function of a Complex Variable
> Let $S$ be a set of complex numbers. A **function** $f$ defined on $S$ is a rule that assigns to each $z$ in $S$ a complex number $w$. The number $w$ is the **value** of $f$ at $z$, denoted $f(z)$, so that $w = f(z)$. The set $S$ is the **domain of definition** of $f$.
>
> Both a domain of definition and a rule are needed for a function to be well defined. When the domain of definition is not mentioned, the largest possible set is taken.
>
> *B&C: Sec. 13 (text)*

^def-13-1

The domain of definition is often a domain in the sense of [[§12★ Regions in the Complex Plane#^def-12-10|Definition §12.10]] (an open connected set), but it need not be. It is also not always convenient to distinguish in notation between a function and its values; one speaks of "the function $z^2$".

> [!example] Example §13.1: The Function 1/z
> If $f$ is defined on the set $z \ne 0$ by $w = 1/z$, it may be referred to simply as the function $w = 1/z$, or the function $1/z$. Its domain of definition is the largest set on which the rule makes sense, the punctured plane $z \ne 0$.
>
> Writing $1/z = \bar z/|z|^2$ ([[§6 Complex Conjugates#^prop-6-3|Proposition §6.3]]) separates the real and imaginary parts:
>
> $$
> \frac{1}{x + iy} = \frac{x - iy}{x^2 + y^2} = \frac{x}{x^2 + y^2} + i\,\frac{-y}{x^2 + y^2} \qquad \big((x, y) \ne (0, 0)\big) .
> $$
>
> *B&C: Sec. 13, Example 1*

^ex-13-1

Suppose that $u + iv$ is the value of $f$ at $z = x + iy$, that is, $u + iv = f(x + iy)$. Each of the real numbers $u$ and $v$ depends on the real variables $x$ and $y$.

> [!definition] Definition §13.2: Real and Imaginary Components
> A function $f$ of $z = x + iy$ can be expressed in terms of a pair of real-valued functions of the real variables $x$ and $y$,
>
> $$
> f(z) = u(x, y) + iv(x, y) . \qquad (1)
> $$
>
> If polar coordinates $r$ and $\theta$ are used instead, with $z = re^{i\theta}$ and $u + iv = f(re^{i\theta})$, one writes
>
> $$
> f(z) = u(r, \theta) + iv(r, \theta) . \qquad (2)
> $$
>
> If $v$ in (1) always has the value zero, the value of $f$ is always real, and $f$ is a **real-valued function** of a complex variable.
>
> *B&C: Sec. 13, equations (1) and (2)*

^def-13-2

> [!example] Example §13.2: z² and |z|² in Components
> **(a)** If $f(z) = z^2$, then
>
> $$
> f(x + iy) = (x + iy)^2 = x^2 - y^2 + i2xy, \qquad\text{so}\qquad u(x, y) = x^2 - y^2, \quad v(x, y) = 2xy .
> $$
>
> **(b)** In polar coordinates, with $z = re^{i\theta}$,
>
> $$
> w = (re^{i\theta})^2 = r^2e^{i2\theta} = r^2\cos 2\theta + ir^2\sin 2\theta, \qquad\text{so}\qquad u(r, \theta) = r^2\cos 2\theta, \quad v(r, \theta) = r^2\sin 2\theta .
> $$
>
> **(c)** A real-valued function that illustrates important concepts later in this chapter ([[§19 Derivatives#^ex-19-3|Example §19.3]]) is
>
> $$
> f(z) = |z|^2 = x^2 + y^2 + i0 , \qquad u(x, y) = x^2 + y^2, \quad v(x, y) = 0 .
> $$
>
> *B&C: Sec. 13, Examples 2, 3 and 4*

^ex-13-2

> [!definition] Definition §13.3: Polynomial
> If $n$ is a nonnegative integer and $a_0, a_1, \ldots, a_n$ are complex constants with $a_n \ne 0$, the function
>
> $$
> P(z) = a_0 + a_1z + a_2z^2 + \cdots + a_nz^n
> $$
>
> is a **polynomial of degree $n$**. The sum has finitely many terms, and the domain of definition is the entire $z$ plane.
>
> *B&C: Sec. 13 (text)*

^def-13-3

> [!definition] Definition §13.5: Rational Function
> Quotients $P(z)/Q(z)$ of polynomials are **rational functions**; they are defined at each point $z$ where $Q(z) \ne 0$.
>
> *B&C: Sec. 13 (text)*

^def-13-4

B&C states the definition for positive $n$; constants $a_0 \ne 0$ are the polynomials of degree $0$, which Exercise 10 of Section 20 uses. Polynomials and rational functions are elementary, but important, classes of functions of a complex variable; their limits, continuity and derivatives are found in [[§16 Theorems on Limits#^cor-16-3|Corollary §16.3]], [[§18 Continuity#^prop-18-1|Proposition §18.1]] and [[§20 Rules for Differentiation#^ex-20-2|Example §20.2]].

## Multiple-Valued Functions

> [!definition] Definition §13.6: Multiple-Valued Function
> A **multiple-valued function** is a rule that assigns more than one value to a point $z$ in the domain of definition. When multiple-valued functions are studied, usually just one of the possible values assigned at each point is taken, in a systematic manner, and a (single-valued) function is constructed from the multiple-valued one.
>
> *B&C: Sec. 13 (text)*

^def-13-5

> [!example] Example §13.3: The Principal Square Root
> Let $z$ be any nonzero complex number. By [[§10 Roots of Complex Numbers#^thm-10-2|Theorem §10.2]], $z^{1/2}$ has the two values
>
> $$
> z^{1/2} = \pm\sqrt r\exp\Big(i\frac{\Theta}{2}\Big) ,
> $$
>
> where $r = |z|$ and $\Theta$ ($-\pi < \Theta \le \pi$) is the principal value $\operatorname{Arg} z$. Choosing only the positive value of $\pm\sqrt r$ gives the single-valued function
>
> $$
> f(z) = \sqrt r\exp\Big(i\frac{\Theta}{2}\Big) \qquad (r > 0,\ -\pi < \Theta \le \pi) , \qquad (3)
> $$
>
> well defined on the set of nonzero numbers. Since zero is the only square root of zero, set $f(0) = 0$; then $f$ is well defined on the entire plane.
>
> Each value is indeed a square root: $f(z)^2 = r\exp(i\Theta) = z$. For example $f(4i) = 2e^{i\pi/4} = \sqrt2 + i\sqrt2$, and $f(-1) = e^{i\pi/2} = i$. The systematic choice has a price on the negative real axis: points just below $-1$ have $\Theta$ near $-\pi$, so their values $f(z)$ are near $e^{-i\pi/2} = -i$, not near $f(-1) = i$. So $f$ jumps across the negative real axis; such choices are studied as branches in [[§33 Branches and Derivatives of Logarithms#^def-33-2|Definition §33.2]] and [[§35 The Power Function#^def-35-3|Definition §35.3]].
>
> *B&C: Sec. 13, Example 5*

^ex-13-3

## Mappings

The graph of a real function of a real variable displays its properties, but when $w = f(z)$ with $z$ and $w$ complex there is no such convenient picture, because each of $z$ and $w$ is located in a plane rather than on a line. One can display some information by indicating pairs of corresponding points $z = (x, y)$ and $w = (u, v)$; it is generally simpler to draw the $z$ and $w$ planes separately.

> [!definition] Definition §13.6: Mapping
> When a function $f$ is thought of as carrying points of the $z$ plane to points of the $w$ plane, it is called a **mapping**, or **transformation**.
>
> *B&C: Sec. 13 (text)*

^def-13-6

> [!definition] Definition §13.7: Image and Range
> Let $f$ be a mapping with domain of definition $S$.
> - The **image** of a point $z$ in the domain of definition $S$ is the point $w = f(z)$.
> - The **image of a set** $T \subseteq S$ is the set of images of all points of $T$.
> - The **range** of $f$ is the image of the entire domain of definition $S$.
>
> *B&C: Sec. 13 (text)*

^def-13-7

> [!definition] Definition §13.8: Inverse Image
> The **inverse image** of a point $w$ under a mapping $f$ with domain of definition $S$ is the set of all points $z$ in $S$ that have $w$ as their image. It may contain just one point, many points, or none at all; the last case occurs when $w$ is not in the range of $f$.
>
> *B&C: Sec. 13 (text)*

^def-13-8

For instance, under $w = z^2$ the inverse image of $w = 4$ is $\{2, -2\}$, and under $w = 1/z$ the inverse image of $w = 0$ is empty, since $0$ is not in the range of $1/z$.

> [!example] Example §13.4: Translation, Rotation and Reflection
> Terms such as **translation**, **rotation** and **reflection** describe the dominant geometric character of certain mappings; for these it is convenient to regard the $z$ and $w$ planes as the same plane.
> - $w = z + 1 = (x + 1) + iy$ is a **translation** of each point $z$ one unit to the right.
> - Since $i = e^{i\pi/2}$, the mapping
>
> $$
> w = iz = r\exp\Big[i\Big(\theta + \frac\pi2\Big)\Big] \qquad (z = re^{i\theta})
> $$
>
>   **rotates** the radius vector of each nonzero point $z$ through a right angle about the origin, counterclockwise.
> - $w = \bar z = x - iy$ transforms each point $z = x + iy$ into its **reflection** in the real axis.
>
> *B&C: Sec. 13 (text)*

^ex-13-4

> [!remark]- Connections
> - Multiplication by a complex number of modulus one as a rotation, and by any $a + bi$ as a rotation followed by a scaling: [[§64 Complex Numbers#^ex-64-3|235 Ex. §64.3]], [[§44 Complex Eigenvalues#^prop-44-3|235 Prop. §44.3]] (the rotation–scaling matrix of $z \mapsto (a + bi)z$).

More information is usually shown by sketching images of curves and regions than by marking images of single points. The next section does this for $w = z^2$.
