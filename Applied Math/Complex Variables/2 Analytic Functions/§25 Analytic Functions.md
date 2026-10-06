---
type: section
subject: "[[Complex Variables]]"
chapter: 2
section: 25
bc: "25"
aliases: ["B&C 25"]
tags: [complex-variables, math342]
---
← [[§24★ Polar Coordinates]] · ↑ [[· 2 Analytic Functions]] · [[§26 Further Examples (Analytic Functions)]] →

*Brown–Churchill, Section 25 · MAT 342 HW 3.*

A function differentiable at a single point, or along a curve, has no useful structure; the theory of complex variables is about functions differentiable on whole open sets. Such functions are called analytic. This section defines analytic functions, entire functions and singular points, shows that analyticity survives sums, products, quotients and composition, and proves the first rigidity property: an analytic function with zero derivative on a domain is constant. Every later theorem of the course, from Cauchy–Goursat to the residue theorem, is about analytic functions.

## Analytic and Entire Functions

> [!definition] Definition §25.1: Analytic Function
> A function $f$ of the complex variable $z$ is **analytic in an open set** $S$ if it has a derivative everywhere in that set. It is **analytic at a point** $z_0$ if it is analytic in some neighborhood of $z_0$.
>
> If $f$ is analytic at $z_0$, it is analytic at *each* point of some neighborhood of $z_0$ (a neighborhood is open, so each of its points has a smaller neighborhood inside it). If we speak of a function that is analytic in a set $S$ that is not open, it is to be understood that $f$ is analytic in an open set containing $S$. The terms **regular** and **holomorphic** are also used for analytic.
>
> *B&C: Sec. 25 (text)*

^def-25-1

> [!definition] Definition §25.2: Entire Function
> An **entire** function is a function that is analytic at each point in the entire (finite) plane.
>
> *B&C: Sec. 25 (text)*

^def-25-2

> [!example] Example §25.1: 1/z, |z|² and Polynomials
> - $f(z) = 1/z$ is analytic at each nonzero point in the finite plane, since its derivative $f'(z) = -1/z^2$ exists at such a point ([[§19 Derivatives#^ex-19-1|Example §19.1]]), and the set $z \ne 0$ is open.
> - $f(z) = |z|^2$ is not analytic anywhere: its derivative exists only at $z = 0$ ([[§19 Derivatives#^ex-19-3|Example §19.3]]; [[§23 Sufficient Conditions for Differentiability#^ex-23-2|Example §23.2]]), and not throughout any neighborhood.
> - Since the derivative of a polynomial exists everywhere ([[§20 Rules for Differentiation#^ex-20-2|Example §20.2]]), **every polynomial is an entire function**.
>
> *B&C: Sec. 25, Examples*

^ex-25-1

**Necessary and sufficient conditions.** A necessary, but by no means sufficient, condition for $f$ to be analytic in a domain $D$ is the continuity of $f$ throughout $D$, since a function is continuous wherever it is differentiable ([[§19 Derivatives#^thm-19-1|Theorem §19.1]]). Satisfaction of the Cauchy–Riemann equations throughout $D$ is also necessary ([[§21 Cauchy–Riemann Equations#^thm-21-1|Theorem §21.1]]), but not sufficient. Sufficient conditions for analyticity in $D$ are provided by [[§23 Sufficient Conditions for Differentiability#^thm-23-1|Theorem §23.1]] and [[§24★ Polar Coordinates#^thm-24-3|Theorem §24.3]], applied at every point of $D$. Other useful sufficient conditions come from the rules for differentiation.

> [!theorem] Proposition §25.1: Sums, Products and Quotients
> If two functions are analytic in a domain $D$, their sum and their product are both analytic in $D$. Their quotient is analytic in $D$ provided the function in the denominator does not vanish at any point in $D$. In particular, the quotient $P(z)/Q(z)$ of two polynomials is analytic in any domain throughout which $Q(z) \ne 0$.
>
> *B&C: Sec. 25 (text)*

^prop-25-1

> [!proof]+ Proof
> Let $f$ and $g$ be analytic in $D$ and let $z \in D$. Both have derivatives at $z$, so by [[§20 Rules for Differentiation#^thm-20-2|Theorem §20.2]] $f + g$ and $fg$ have derivatives at $z$:
>
> $$
> (f + g)'(z) = f'(z) + g'(z), \qquad (fg)'(z) = f(z)g'(z) + f'(z)g(z) .
> $$
>
> If moreover $g(z) \ne 0$, the quotient rule of [[§20 Rules for Differentiation#^thm-20-2|Theorem §20.2]] gives
>
> $$
> \Big(\frac fg\Big)'(z) = \frac{g(z)f'(z) - f(z)g'(z)}{[g(z)]^2} .
> $$
>
> Since this holds at every point of the open set $D$, the three functions are analytic in $D$. Polynomials are entire (Example §25.1), so $P/Q$ is analytic wherever $Q \ne 0$ throughout a domain.

^pf-25-1

*Uses:* [[§20 Rules for Differentiation#^thm-20-2|§20.2]], [[§25 Analytic Functions#^ex-25-1|Ex. §25.1]]

> [!theorem] Proposition §25.2: Compositions
> A composition of two analytic functions is analytic. More precisely, suppose that $f(z)$ is analytic in a domain $D$ and that the image ([[§13 Functions and Mappings#^def-13-5|Definition §13.5]]) of $D$ under the transformation $w = f(z)$ is contained in the domain of definition of a function $g(w)$ that is analytic there. Then the composition $g[f(z)]$ is analytic in $D$, with derivative
>
> $$
> \frac{d}{dz}g[f(z)] = g'[f(z)]\,f'(z) .
> $$
>
> *B&C: Sec. 25 (text)*

^prop-25-2

> [!proof]+ Proof
> Let $z \in D$. Then $f$ has a derivative at $z$, and $g$ has a derivative at $f(z)$, a point of the open set on which $g$ is analytic. By the chain rule, [[§20 Rules for Differentiation#^thm-20-4|Theorem §20.4]], $g \circ f$ has a derivative at $z$ equal to $g'[f(z)]f'(z)$. This holds at every point of $D$.

^pf-25-2

*Uses:* [[§20 Rules for Differentiation#^thm-20-4|§20.4]]

## Zero Derivative Means Constant

The following property of analytic functions is especially useful, in addition to being expected.

> [!theorem] Theorem §25.3: Zero Derivative on a Domain
> If $f'(z) = 0$ everywhere in a domain $D$, then $f(z)$ must be constant throughout $D$.
>
> *B&C: Sec. 25, Theorem*

^thm-25-3

> [!proof]+ Proof
> Write $f(z) = u(x, y) + iv(x, y)$.
>
> **All partial derivatives vanish.** Since $f'(z) = 0$ in $D$, the formula $f'(z) = u_x + iv_x$ of [[§21 Cauchy–Riemann Equations#^thm-21-1|Theorem §21.1]] gives $u_x + iv_x = 0$; and, in view of the Cauchy–Riemann equations, $v_y - iu_y = 0$ (this is the formula $f'(z_0) = v_y - iu_y$ of [[§21 Cauchy–Riemann Equations#^thm-21-1|Theorem §21.1]]). Consequently
>
> $$
> u_x = u_y = 0 \qquad\text{and}\qquad v_x = v_y = 0
> $$
>
> at each point in $D$.
>
> **$u$ is constant along any segment in $D$.** Let $L$ be a line segment extending from a point $P$ to a point $P'$ and lying entirely in $D$. Let $s$ denote the distance along $L$ from $P$ and $\mathbf U$ the unit vector along $L$ in the direction of increasing $s$. The directional derivative $du/ds$ can be written as the dot product
>
> $$
> \frac{du}{ds} = (\operatorname{grad} u)\cdot\mathbf U , \qquad (1)
> $$
>
> where $\operatorname{grad} u = u_x\mathbf i + u_y\mathbf j$ is the gradient vector (2). (Formula (1) requires $u$ to be differentiable; it is, because its partial derivatives exist and are continuous, being identically zero, throughout the open set $D$.) Because $u_x$ and $u_y$ are zero everywhere in $D$, $\operatorname{grad} u$ is the zero vector at all points of $L$, and $du/ds = 0$ along $L$. A function of the single variable $s$ with zero derivative on an interval is constant there, so $u$ is constant on $L$: $u(P) = u(P')$.
>
> **$u$ is constant in $D$.** Any two points $P$ and $Q$ in $D$ are connected by a polygonal line in $D$, a finite number of line segments joined end to end, since $D$ is a domain ([[§12★ Regions in the Complex Plane#^def-12-4|Definition §12.4]]). Applying the previous step to each segment in turn, the values of $u$ at $P$ and $Q$ are the same. So there is a real constant $a$ such that $u(x, y) = a$ throughout $D$. Similarly, $v(x, y) = b$, and $f(z) = a + bi$ at each point of $D$: $f(z) = c$ where $c = a + bi$.

^pf-25-3

*Uses:* [[§21 Cauchy–Riemann Equations#^thm-21-1|§21.1]], [[§12★ Regions in the Complex Plane#^def-12-4|Def. §12.4]], [[§6 Differentiability#^thm-6-2|452 Thm. §6.2]], [[§7 Directional Derivatives#^thm-7-1|452 Thm. §7.1]] (directional derivative formula), [[§29 The Mean Value Theorem#^cor-29-4|451 Cor. §29.4]] (vanishing derivative)

> [!remark]- Connections
> - The one-variable case is [[§29 The Mean Value Theorem#^cor-29-4|451 Cor. §29.4]]; the proof above reduces to it along each segment. Connectedness is essential: on the open set $|z| < 1$ or $|z - 3| < 1$, the function equal to $0$ on the first disk and $1$ on the second has $f' = 0$ but is not constant. B&C's polygonal connectedness implies connectedness in the topological sense, [[§13 Connected Spaces#^def-13-1|590 Def. §13.1]].

## Singular Points

> [!definition] Definition §25.3: Singular Point
> If a function $f$ fails to be analytic at a point $z_0$ but is analytic at some point in every neighborhood of $z_0$, then $z_0$ is called a **singular point**, or **singularity**, of $f$.
>
> *B&C: Sec. 25 (text)*

^def-25-3

> [!example] Example §25.2: Singular Points of 1/z and |z|²
> The point $z = 0$ is a singular point of $f(z) = 1/z$: $f$ is not analytic at $0$ (it is not even defined there), but every neighborhood of $0$ contains nonzero points, where $f$ is analytic (Example §25.1). The function $f(z) = |z|^2$, on the other hand, has **no** singular points: it is nowhere analytic, so the second condition of Definition §25.3 fails at every point. Singular points play an important role from Ch. 6 on, where they are classified ([[§74 Isolated Singular Points#^def-74-1|Definition §74.1]], [[§78 The Three Types of Isolated Singular Points|§78]]).
>
> *B&C: Sec. 25 (text)*

^ex-25-2

> [!example] Example §25.3: Differentiable on a Line, Analytic Nowhere
> Where is $f(z) = x^2 - iy^2$ differentiable? Where is it analytic?
>
> Here $u = x^2$, $v = -y^2$, and
>
> $$
> u_x = 2x, \quad u_y = 0, \qquad v_x = 0, \quad v_y = -2y ,
> $$
>
> all continuous everywhere. The equation $u_y = -v_x$ reads $0 = 0$ and always holds; $u_x = v_y$ reads $2x = -2y$. So the Cauchy–Riemann equations hold exactly on the line $y = -x$, and by [[§23 Sufficient Conditions for Differentiability#^thm-23-1|Theorem §23.1]] $f$ is differentiable at every point of this line and nowhere else, with
>
> $$
> f'(x - ix) = u_x + iv_x = 2x .
> $$
>
> But $f$ is **analytic nowhere**: every neighborhood of a point of the line contains points off the line, where $f'$ does not exist, so no point has a neighborhood throughout which $f$ is differentiable. (Note that $f$ is continuous everywhere: continuity is necessary for analyticity, not sufficient.) Compare B&C's Exercise 3(b) of Sec. 24, $f(z) = x^2 + iy^2$, which is differentiable exactly on $y = x$ with $f'(x + ix) = 2x$.
>
> *Source: 342 HW 3, Q2(d)*

^ex-25-3
