---
type: section
subject: "[[Calculus]]"
chapter: 3
section: 21
stewart: "3.5"
aliases: ["Stewart 3.5"]
tags: [calculus]
---
← [[§20 The Chain Rule]] · ↑ [[· 3 Differentiation Rules]] · [[§22 Derivatives of Logarithmic and Inverse Trigonometric Functions]] →

*Stewart, Section 3.5.*

Many curves are given by an equation in $x$ and $y$, such as $x^2 + y^2 = 25$ or $x^3 + y^3 = 6xy$, rather than by a formula $y = f(x)$. Such an equation defines $y$ as one or several functions of $x$ *implicitly*, and solving for $y$ may be hard or impossible. Implicit differentiation finds $dy/dx$ anyway: differentiate both sides of the equation with respect to $x$, treating $y$ as a function of $x$ (so the Chain Rule, [[§20 The Chain Rule#^thm-20-2|Theorem §20.2]], applies to every term containing $y$), and solve for $dy/dx$. The method gives tangent lines to such curves and, applied twice, second derivatives. In [[§22 Derivatives of Logarithmic and Inverse Trigonometric Functions|§22]] it gives the derivatives of inverse functions ([[§22 Derivatives of Logarithmic and Inverse Trigonometric Functions#^thm-22-8|Theorem §22.8]]).

## Implicitly Defined Functions

The functions met so far are given *explicitly*, $y = f(x)$, for example $y = \sqrt{x^3 + 1}$ or $y = x\sin x$. Other functions are defined by a relation between $x$ and $y$, such as

$$
x^2 + y^2 = 25 \qquad (1) \qquad\qquad\text{or}\qquad\qquad x^3 + y^3 = 6xy . \qquad (2)
$$

Solving (1) for $y$ gives $y = \pm\sqrt{25 - x^2}$. So two of the functions determined by (1) are $f(x) = \sqrt{25 - x^2}$ and $g(x) = -\sqrt{25 - x^2}$, whose graphs are the upper and lower semicircles of the circle $x^2 + y^2 = 25$. Equation (2) is the **folium of Descartes**. It defines $y$ as several functions of $x$, but solving it for $y$ by hand is not practical.

> [!definition] Definition §21.1: Function Defined Implicitly
> A function $f$ is **defined implicitly** by an equation in $x$ and $y$ if the equation becomes true for every $x$ in the domain of $f$ when $y$ is replaced by $f(x)$. For example, $f$ is defined implicitly by Equation 2 if
>
> $$
> x^3 + [f(x)]^3 = 6x f(x) \qquad\text{for all } x \text{ in the domain of } f .
> $$
>
> *Stewart: 3.5 (text)*

^def-21-1

> [!remark]- Connections
> - When does an equation $F(x, y) = 0$ define $y$ as a differentiable function of $x$ near a point? The Implicit Function Theorem answers this ($F_y \ne 0$ at the point) and gives the formula $dy/dx = -F_x/F_y$: [[§15 The Implicit Function Theorem#^thm-15-1|452 Thm. §15.1]]. In Calculus the same formula appears with partial derivatives in [[§110 The Chain Rule#^thm-110-4|Theorem §110.4]] (Stewart 14.5).

## Implicit Differentiation

> [!remark] Remark: Method — Implicit Differentiation
> Assume that the equation determines $y$ implicitly as a differentiable function of $x$. (Stewart makes this assumption throughout the section and its exercises.)
> 1. Differentiate both sides of the equation with respect to $x$.
> 2. Whenever a term contains $y$, remember that $y$ is a function of $x$: by the Chain Rule, $\frac{d}{dx}[g(y)] = g'(y)\,\frac{dy}{dx}$, e.g. $\frac{d}{dx}(y^2) = 2y\,\frac{dy}{dx}$. Products such as $xy$ need the Product Rule: $\frac{d}{dx}(xy) = y + x\,\frac{dy}{dx}$.
> 3. Collect the terms containing $dy/dx$ (also written $y'$) on one side and solve for $dy/dx$. The result is usually in terms of both $x$ and $y$.
> 4. For the slope at a point $(a, b)$ of the curve, substitute $x = a$, $y = b$.
> 5. For $y''$, differentiate the expression for $y'$ implicitly again, substitute the expression for $y'$, and simplify with the original equation.

^rem-21-1

> [!example] Example §21.1: The Tangent Line to a Circle
> If $x^2 + y^2 = 25$, find $dy/dx$. Then find an equation of the tangent to the circle at the point $(3, 4)$.
>
> **Solution 1 (implicitly).** Differentiate both sides with respect to $x$:
>
> $$
> \frac{d}{dx}(x^2 + y^2) = \frac{d}{dx}(25), \qquad \frac{d}{dx}(x^2) + \frac{d}{dx}(y^2) = 0 .
> $$
>
> Since $y$ is a function of $x$, the Chain Rule gives $\dfrac{d}{dx}(y^2) = \dfrac{d}{dy}(y^2)\,\dfrac{dy}{dx} = 2y\,\dfrac{dy}{dx}$. Thus
>
> $$
> 2x + 2y\,\frac{dy}{dx} = 0, \qquad \frac{dy}{dx} = -\frac{x}{y} .
> $$
>
> At $(3, 4)$, $dy/dx = -\frac34$, so the tangent line is
>
> $$
> y - 4 = -\tfrac34 (x - 3) \qquad\text{or}\qquad 3x + 4y = 25 .
> $$
>
> **Solution 2 (explicitly).** The point $(3, 4)$ lies on the upper semicircle $y = \sqrt{25 - x^2}$, so take $f(x) = \sqrt{25 - x^2}$. By the Chain Rule,
>
> $$
> f'(x) = \tfrac12 (25 - x^2)^{-1/2} \frac{d}{dx}(25 - x^2) = \tfrac12 (25 - x^2)^{-1/2}(-2x) = -\frac{x}{\sqrt{25 - x^2}} ,
> $$
>
> and $f'(3) = -3/\sqrt{25 - 9} = -\frac34$, as before. Even when the equation can be solved for $y$, implicit differentiation may be easier.
>
> **The formula works for every branch.** $dy/dx = -x/y$ is correct whichever function $y$ the equation determines. For $y = f(x) = \sqrt{25 - x^2}$ it gives $-x/\sqrt{25 - x^2}$; for $y = g(x) = -\sqrt{25 - x^2}$ it gives
>
> $$
> \frac{dy}{dx} = -\frac{x}{y} = -\frac{x}{-\sqrt{25 - x^2}} = \frac{x}{\sqrt{25 - x^2}} .
> $$
>
> (Geometrically: the radius to $(x, y)$ has slope $y/x$, and the tangent is perpendicular to it, with slope $-x/y$.)
>
> *Stewart: Example 3.5.1 and Note 1*

^ex-21-1

> [!example] Example §21.2: The Folium of Descartes
> (a) Find $y'$ if $x^3 + y^3 = 6xy$. (b) Find the tangent to the folium at the point $(3, 3)$. (c) At what point in the first quadrant is the tangent line horizontal?
>
> **(a)** Differentiate both sides with respect to $x$, using the Chain Rule on $y^3$ and the Product Rule on $6xy$:
>
> $$
> 3x^2 + 3y^2 y' = 6xy' + 6y, \qquad\text{or}\qquad x^2 + y^2 y' = 2xy' + 2y .
> $$
>
> Collect the terms with $y'$:
>
> $$
> y^2 y' - 2xy' = 2y - x^2, \qquad (y^2 - 2x)\,y' = 2y - x^2, \qquad y' = \frac{2y - x^2}{y^2 - 2x} .
> $$
>
> **(b)** At $x = y = 3$ (which is on the curve: $27 + 27 = 54 = 6 \cdot 9$),
>
> $$
> y' = \frac{2 \cdot 3 - 3^2}{3^2 - 2 \cdot 3} = \frac{-3}{3} = -1 ,
> $$
>
> so the tangent is $y - 3 = -1(x - 3)$, or $x + y = 6$.
>
> **(c)** The tangent is horizontal where $y' = 0$, that is, where $2y - x^2 = 0$ (provided $y^2 - 2x \ne 0$). Substitute $y = \frac12 x^2$ into the equation of the curve:
>
> $$
> x^3 + \big(\tfrac12 x^2\big)^3 = 6x\big(\tfrac12 x^2\big), \qquad x^3 + \tfrac18 x^6 = 3x^3, \qquad x^6 = 16x^3 .
> $$
>
> In the first quadrant $x \ne 0$, so $x^3 = 16$ and $x = 16^{1/3} = 2^{4/3}$. Then $y = \frac12 (2^{8/3}) = 2^{5/3}$. Check: $y^2 - 2x = 2^{10/3} - 2^{7/3} \ne 0$. So the tangent is horizontal at $\big(2^{4/3}, 2^{5/3}\big) \approx (2.5198, 3.1748)$.
>
> *Stewart: Example 3.5.2*

^ex-21-2

![[m233-18-1.svg]]
*The folium of Descartes $x^3 + y^3 = 6xy$ (blue) with its tangent $x + y = 6$ at $(3, 3)$ (red) and its horizontal tangent at $(2^{4/3}, 2^{5/3})$ (green). Near most points the curve is the graph of a function $y = f(x)$, and $y' = (2y - x^2)/(y^2 - 2x)$ is the slope of that local branch. The formula fails where $y^2 = 2x$: at the origin, where the curve crosses itself, and at the rightmost point of the loop, where the tangent is vertical.*

*Chain:* [[§110 The Chain Rule#^ex-110-5|Chapter 14]] →

> [!remark]- Remark: Why Not Solve for y?
> There is a formula for the three solutions of a cubic equation, like the quadratic formula but much more complicated. Applied to $x^3 + y^3 = 6xy$ (or done by a computer), it gives three functions determined by the equation:
>
> $$
> y = f(x) = \sqrt[3]{-\tfrac12 x^3 + \sqrt{\tfrac14 x^6 - 8x^3}} + \sqrt[3]{-\tfrac12 x^3 - \sqrt{\tfrac14 x^6 - 8x^3}}
> $$
>
> and
>
> $$
> y = \tfrac12 \left[ -f(x) \pm \sqrt{-3} \left( \sqrt[3]{-\tfrac12 x^3 + \sqrt{\tfrac14 x^6 - 8x^3}} - \sqrt[3]{-\tfrac12 x^3 - \sqrt{\tfrac14 x^6 - 8x^3}} \right) \right] .
> $$
>
> Implicit differentiation saves an enormous amount of work here. For an equation such as $y^5 + 3x^2 y^2 + 5x^4 = 12$ it is the only option: Abel (1824) proved that there is no general formula in radicals for the roots of a polynomial of degree $5$, and Galois proved the same for every degree $n \ge 5$. Implicit differentiation works for such equations just as easily.

^rem-21-2

> [!example] Example §21.3: A Transcendental Equation
> Find $y'$ if $\sin(x + y) = y^2 \cos x$.
>
> Differentiate implicitly with respect to $x$: the Chain Rule on the left, the Product and Chain Rules on the right.
>
> $$
> \cos(x + y) \cdot (1 + y') = y^2(-\sin x) + (\cos x)(2yy') .
> $$
>
> Collect the terms that involve $y'$:
>
> $$
> \cos(x + y) + y^2 \sin x = (2y\cos x)\,y' - \cos(x + y)\,y' ,
> \qquad
> y' = \frac{y^2 \sin x + \cos(x + y)}{2y\cos x - \cos(x + y)} .
> $$
>
> As a check: the origin is on the curve ($\sin 0 = 0 = 0^2 \cos 0$), and there $y' = \dfrac{0 + 1}{0 - 1} = -1$, matching a computer graph of the curve, whose slope at the origin is about $-1$.
>
> *Stewart: Example 3.5.3*

^ex-21-3

## Second Derivatives of Implicit Functions

> [!example] Example §21.4: The Second Derivative on a Fat Circle
> Find $y''$ if $x^4 + y^4 = 16$.
>
> Differentiating implicitly, $4x^3 + 4y^3 y' = 0$, so
>
> $$
> y' = -\frac{x^3}{y^3} . \qquad (3)
> $$
>
> Differentiate this with the Quotient Rule, remembering that $y$ is a function of $x$ (so $\frac{d}{dx}(y^3) = 3y^2 y'$):
>
> $$
> y'' = \frac{d}{dx}\left( -\frac{x^3}{y^3} \right) = -\frac{y^3\,\frac{d}{dx}(x^3) - x^3\,\frac{d}{dx}(y^3)}{(y^3)^2} = -\frac{y^3 \cdot 3x^2 - x^3(3y^2 y')}{y^6} .
> $$
>
> Substitute Equation 3:
>
> $$
> y'' = -\frac{3x^2 y^3 - 3x^3 y^2 \left( -\dfrac{x^3}{y^3} \right)}{y^6} = -\frac{3(x^2 y^4 + x^6)}{y^7} = -\frac{3x^2(y^4 + x^4)}{y^7} .
> $$
>
> Since $x$ and $y$ satisfy $x^4 + y^4 = 16$, this simplifies to
>
> $$
> y'' = -\frac{3x^2(16)}{y^7} = -48\,\frac{x^2}{y^7} .
> $$
>
> The curve $x^4 + y^4 = 16$ is a stretched and flattened version of the circle $x^2 + y^2 = 4$, a "fat circle". By (3), $y' = -(x/y)^3$: it starts very steep near the left and right ends, where $|x/y|$ is large, and quickly becomes very flat, where $|x/y| < 1$.
>
> *Stewart: Example 3.5.4*

^ex-21-4
