---
type: section
subject: "[[Calculus]]"
chapter: 3
section: 24
stewart: "3.11"
aliases: ["Stewart 3.11"]
tags: [calculus]
---
← [[§23 Linear Approximations and Differentials]] · ↑ [[· 3 Differentiation Rules]] · [[§25 Maximum and Minimum Values]] →

*Stewart, Section 3.11.*

Certain combinations of $e^x$ and $e^{-x}$ occur so often that they have names: the hyperbolic sine, cosine, tangent and their reciprocals. They behave much like the trigonometric functions, with the hyperbola $x^2 - y^2 = 1$ in place of the circle $x^2 + y^2 = 1$: they satisfy similar identities, and their derivatives match the trigonometric ones up to some signs. Their inverses can be written with logarithms, and differentiating them gives new antiderivatives that are used in Chapter 7. The hanging cable (catenary) is the best-known application.

## Hyperbolic Functions and Their Derivatives

> [!definition] Definition §24.1: The Hyperbolic Functions
> $$
> \begin{aligned}
> \sinh x &= \frac{e^x - e^{-x}}{2} & \operatorname{csch} x &= \frac{1}{\sinh x} \\
> \cosh x &= \frac{e^x + e^{-x}}{2} & \operatorname{sech} x &= \frac{1}{\cosh x} \\
> \tanh x &= \frac{\sinh x}{\cosh x} & \coth x &= \frac{\cosh x}{\sinh x}
> \end{aligned}
> $$
>
> These are the **hyperbolic functions**: **hyperbolic sine**, **hyperbolic cosine**, and so on.
>
> *Stewart: 3.11, Definition of the Hyperbolic Functions*

^def-24-1

> [!remark]- Connections
> - Their power series, $\cosh x = \sum \frac{x^{2n}}{(2n)!}$ and $\sinh x = \sum \frac{x^{2n+1}}{(2n+1)!}$, are the even and odd halves of the series of $e^x$: [[§31 Taylor's Theorem#^ex-31-1|451 Ex. §31.1]] (and the Maclaurin series of $e^x$ in Calculus, [[§78 Taylor and Maclaurin Series#^thm-78-6|Theorem §78.6]]). Compare $\cos$ and $\sin$, which have the same series with alternating signs.

> [!remark] Remark: Graphs and Applications
> **Graphs.** $\sinh x = \frac12 e^x - \frac12 e^{-x}$ and $\cosh x = \frac12 e^x + \frac12 e^{-x}$ can be sketched by adding the graphs of $\pm\frac12 e^{\pm x}$. $\sinh$ has domain $\mathbb{R}$ and range $\mathbb{R}$; $\cosh$ has domain $\mathbb{R}$ and range $[1, \infty)$, with minimum $\cosh 0 = 1$. $\tanh$ has horizontal asymptotes $y = \pm 1$ (Stewart, Exercise 27): $\tanh x = \dfrac{1 - e^{-2x}}{1 + e^{-2x}} \to 1$ as $x \to \infty$, and $\tanh$ is odd.
>
> **Applications.** Hyperbolic functions describe the gradual absorption or extinction of light, velocity, electricity or radioactivity. A heavy flexible cable (such as an overhead power line) suspended between two points at the same height takes the shape of a **catenary** (Latin *catena*, "chain")
>
> $$
> y = c + a\cosh(x/a) .
> $$
>
> The velocity of a water wave of length $L$ moving across water of depth $d$ is modeled by
>
> $$
> v = \sqrt{\frac{gL}{2\pi}\tanh\left( \frac{2\pi d}{L} \right)} ,
> $$
>
> where $g$ is the acceleration due to gravity.

^rem-24-1

> [!remark]- Connections
> - See also: [[§3★ Boundary Value Problems#^ex-3-2|341 Ex. §3.2]] (the catenary derived: for a cable hanging under its own weight the equation of [[§3★ Boundary Value Problems#^prop-3-1|341 Prop. §3.1]] becomes $u'' = \mu\sqrt{1 + (u')^2}$, solved with $\sinh^{-1}$).

> [!theorem] Theorem §24.1: Hyperbolic Identities
> $$
> \begin{aligned}
> \sinh(-x) &= -\sinh x & \cosh(-x) &= \cosh x \\
> \cosh^2 x - \sinh^2 x &= 1 & 1 - \tanh^2 x &= \operatorname{sech}^2 x
> \end{aligned}
> $$
>
> $$
> \sinh(x + y) = \sinh x\cosh y + \cosh x\sinh y, \qquad \cosh(x + y) = \cosh x\cosh y + \sinh x\sinh y .
> $$
>
> *Stewart: 3.11, Hyperbolic Identities (Example 3.11.1; Exercises 11–16)*

^thm-24-1

> [!proof]+ Proof
> Stewart proves the second line in Example 3.11.1 and leaves the others as exercises.
>
> **Parity.** $\sinh(-x) = \dfrac{e^{-x} - e^{x}}{2} = -\sinh x$ and $\cosh(-x) = \dfrac{e^{-x} + e^{x}}{2} = \cosh x$.
>
> **$\cosh^2 x - \sinh^2 x = 1$.** Expanding the squares (with $e^x e^{-x} = 1$),
>
> $$
> \cosh^2 x - \sinh^2 x = \left( \frac{e^x + e^{-x}}{2} \right)^2 - \left( \frac{e^x - e^{-x}}{2} \right)^2 = \frac{e^{2x} + 2 + e^{-2x}}{4} - \frac{e^{2x} - 2 + e^{-2x}}{4} = \frac44 = 1 .
> $$
>
> **$1 - \tanh^2 x = \operatorname{sech}^2 x$.** Divide both sides of $\cosh^2 x - \sinh^2 x = 1$ by $\cosh^2 x$ (which is $\ge 1$, so not $0$):
>
> $$
> 1 - \frac{\sinh^2 x}{\cosh^2 x} = \frac{1}{\cosh^2 x}, \qquad\text{that is,}\qquad 1 - \tanh^2 x = \operatorname{sech}^2 x .
> $$
>
> **Addition formulas.** Note $\cosh x + \sinh x = e^x$ and $\cosh x - \sinh x = e^{-x}$. Then
>
> $$
> \begin{aligned}
> \sinh x\cosh y + \cosh x\sinh y &= \tfrac14 \big[ (e^x - e^{-x})(e^y + e^{-y}) + (e^x + e^{-x})(e^y - e^{-y}) \big] \\
> &= \tfrac14 \big[ 2e^{x+y} - 2e^{-(x+y)} \big] = \sinh(x + y) ,
> \end{aligned}
> $$
>
> since the mixed terms $e^{x-y}$ and $e^{-x+y}$ cancel. In the same way, $\cosh x\cosh y + \sinh x\sinh y = \frac14 \big[ 2e^{x+y} + 2e^{-(x+y)} \big] = \cosh(x + y)$.

^pf-24-1

*Uses:* [[§24 Hyperbolic Functions#^def-24-1|Def. §24.1]]

> [!remark] Remark: Why "Hyperbolic"
> For any real $t$, the point $P(\cos t, \sin t)$ lies on the unit circle $x^2 + y^2 = 1$, because $\cos^2 t + \sin^2 t = 1$; $t$ is the radian measure of the angle $POQ$ with $Q = (1, 0)$, and also twice the area of the circular sector $POQ$. That is why the trigonometric functions are sometimes called *circular* functions. Likewise, the point $P(\cosh t, \sinh t)$ lies on the right branch of the hyperbola $x^2 - y^2 = 1$, because $\cosh^2 t - \sinh^2 t = 1$ and $\cosh t \ge 1$. Now $t$ is not the measure of an angle, but it turns out (Stewart states this without proof; it is a computation with integrals) that $t$ is twice the area of the hyperbolic sector between $OQ$, $OP$ and the hyperbola, just as in the circular case.

^rem-24-2

![[m233-24-1.svg]]
*Circular and hyperbolic functions. Left: $(\cos t, \sin t)$ on the circle $x^2 + y^2 = 1$; the shaded sector has area $t/2$. Right: $(\cosh t, \sinh t)$ on the hyperbola $x^2 - y^2 = 1$; the shaded hyperbolic sector also has area $t/2$, but as $t \to \infty$ the point runs off along the asymptote $y = x$ (dashed) instead of returning.*

> [!theorem] Theorem §24.2: Derivatives of Hyperbolic Functions
> $$
> \begin{aligned}
> \frac{d}{dx}(\sinh x) &= \cosh x & \frac{d}{dx}(\operatorname{csch} x) &= -\operatorname{csch} x \coth x \\
> \frac{d}{dx}(\cosh x) &= \sinh x & \frac{d}{dx}(\operatorname{sech} x) &= -\operatorname{sech} x \tanh x \\
> \frac{d}{dx}(\tanh x) &= \operatorname{sech}^2 x & \frac{d}{dx}(\coth x) &= -\operatorname{csch}^2 x
> \end{aligned}
> $$
>
> Note the analogy with the trigonometric formulas ([[§16 Derivatives of Trigonometric Functions#^thm-16-4|Theorem §16.4]]), but some signs differ: $\cosh' = +\sinh$, while $\cos' = -\sin$.
>
> *Stewart: 3.11, Table 1*

^thm-24-2

> [!proof]+ Proof
> Stewart computes the first and leaves the rest as exercises. By $\frac{d}{dx}(e^{-x}) = -e^{-x}$ (Chain Rule),
>
> $$
> \frac{d}{dx}(\sinh x) = \frac{d}{dx}\left( \frac{e^x - e^{-x}}{2} \right) = \frac{e^x + e^{-x}}{2} = \cosh x, \qquad
> \frac{d}{dx}(\cosh x) = \frac{e^x - e^{-x}}{2} = \sinh x .
> $$
>
> The other four follow by the Quotient Rule and Theorem §24.1:
>
> $$
> \begin{aligned}
> \frac{d}{dx}\left( \frac{\sinh x}{\cosh x} \right) &= \frac{\cosh^2 x - \sinh^2 x}{\cosh^2 x} = \frac{1}{\cosh^2 x} = \operatorname{sech}^2 x , &
> \frac{d}{dx}\left( \frac{1}{\sinh x} \right) &= -\frac{\cosh x}{\sinh^2 x} = -\operatorname{csch} x \coth x , \\
> \frac{d}{dx}\left( \frac{1}{\cosh x} \right) &= -\frac{\sinh x}{\cosh^2 x} = -\operatorname{sech} x \tanh x , &
> \frac{d}{dx}\left( \frac{\cosh x}{\sinh x} \right) &= \frac{\sinh^2 x - \cosh^2 x}{\sinh^2 x} = -\frac{1}{\sinh^2 x} = -\operatorname{csch}^2 x .
> \end{aligned}
> $$

^pf-24-2

*Uses:* [[§24 Hyperbolic Functions#^def-24-1|Def. §24.1]], [[§24 Hyperbolic Functions#^thm-24-1|§24.1]], [[§14 Derivatives of Polynomials and Exponential Functions#^thm-14-6|§14.6]], [[§17 The Chain Rule#^cor-17-4|§17.4]], [[§15 The Product and Quotient Rules#^thm-15-2|§15.2]]

> [!example] Example §24.1: Combining with the Chain Rule
> If $y = \cosh\sqrt{x}$, find $dy/dx$.
>
> By Theorem §24.2 and the Chain Rule,
>
> $$
> \frac{dy}{dx} = \frac{d}{dx}\big(\cosh\sqrt{x}\big) = \sinh\sqrt{x} \cdot \frac{d}{dx}\sqrt{x} = \frac{\sinh\sqrt{x}}{2\sqrt{x}} .
> $$
>
> *Stewart: Example 3.11.2*

^ex-24-1

## Inverse Hyperbolic Functions and Their Derivatives

$\sinh$ and $\tanh$ are one-to-one (they are increasing, since their derivatives $\cosh x$ and $\operatorname{sech}^2 x$ are positive), so they have inverse functions. $\cosh$ is not one-to-one, but restricted to $[0, \infty)$ it is one-to-one and takes every value in its range $[1, \infty)$.

> [!definition] Definition §24.2: Inverse Hyperbolic Functions
> $$
> \begin{aligned}
> y = \sinh^{-1} x &\iff \sinh y = x \\
> y = \cosh^{-1} x &\iff \cosh y = x \ \text{ and } \ y \ge 0 \\
> y = \tanh^{-1} x &\iff \tanh y = x
> \end{aligned}
> $$
>
> So $\sinh^{-1}$ has domain $\mathbb{R}$ and range $\mathbb{R}$; $\cosh^{-1}$ has domain $[1, \infty)$ and range $[0, \infty)$; $\tanh^{-1}$ has domain $(-1, 1)$ and range $\mathbb{R}$. The remaining inverse hyperbolic functions are defined similarly (Stewart, Exercise 32): $\operatorname{csch}^{-1} x$ for $x \ne 0$, $\operatorname{sech}^{-1} x$ for $0 < x \le 1$ with values $\ge 0$, and $\coth^{-1} x$ for $|x| > 1$.
>
> *Stewart: 3.11, Equation 2*

^def-24-2

Since the hyperbolic functions are built from exponentials, their inverses can be written with logarithms.

> [!theorem] Theorem §24.3: Inverse Hyperbolic Functions as Logarithms
> $$
> \begin{aligned}
> \sinh^{-1} x &= \ln\big( x + \sqrt{x^2 + 1} \big), & x &\in \mathbb{R} \qquad (3) \\
> \cosh^{-1} x &= \ln\big( x + \sqrt{x^2 - 1} \big), & x &\ge 1 \qquad (4) \\
> \tanh^{-1} x &= \tfrac12 \ln\left( \frac{1 + x}{1 - x} \right), & -1 &< x < 1 \qquad (5)
> \end{aligned}
> $$
>
> *Stewart: 3.11, Formulas 3–5 (Example 3.11.3; Exercises 30 and 31)*

^thm-24-3

> [!proof]+ Proof
> **Formula 3** (Stewart's Example 3.11.3). Let $y = \sinh^{-1} x$. Then
>
> $$
> x = \sinh y = \frac{e^y - e^{-y}}{2}, \qquad\text{so}\qquad e^y - 2x - e^{-y} = 0 ,
> $$
>
> or, multiplying by $e^y$, $e^{2y} - 2xe^y - 1 = 0$. This is a quadratic equation in $e^y$: $(e^y)^2 - 2x(e^y) - 1 = 0$. By the quadratic formula,
>
> $$
> e^y = \frac{2x \pm \sqrt{4x^2 + 4}}{2} = x \pm \sqrt{x^2 + 1} .
> $$
>
> Now $e^y > 0$, but $x - \sqrt{x^2 + 1} < 0$ because $x \le |x| < \sqrt{x^2 + 1}$. So the minus sign is inadmissible, $e^y = x + \sqrt{x^2 + 1}$, and $y = \ln(e^y) = \ln\big(x + \sqrt{x^2 + 1}\big)$.
>
> **Formula 4** (Exercise 30). Let $y = \cosh^{-1} x$, so $x = \cosh y$ with $y \ge 0$. As above, $e^{2y} - 2xe^y + 1 = 0$, so $e^y = x \pm \sqrt{x^2 - 1}$. Since $y \ge 0$, $e^y \ge 1$. The two roots have product $1$, so the smaller one, $x - \sqrt{x^2 - 1}$, is at most $1$, with equality only when $x = 1$ (when the roots coincide). So $e^y = x + \sqrt{x^2 - 1}$ and $y = \ln\big(x + \sqrt{x^2 - 1}\big)$.
>
> **Formula 5** (Exercise 31). Let $y = \tanh^{-1} x$, so
>
> $$
> x = \tanh y = \frac{e^y - e^{-y}}{e^y + e^{-y}} = \frac{e^{2y} - 1}{e^{2y} + 1} .
> $$
>
> Then $xe^{2y} + x = e^{2y} - 1$, so $e^{2y}(1 - x) = 1 + x$ and, since $|x| < 1$, $e^{2y} = \dfrac{1 + x}{1 - x} > 0$. Hence $y = \frac12 \ln\dfrac{1 + x}{1 - x}$.

^pf-24-3

*Uses:* [[§24 Hyperbolic Functions#^def-24-1|Def. §24.1]], [[§24 Hyperbolic Functions#^def-24-2|Def. §24.2]], [[§5 Inverse Functions and Logarithms#^cor-5-6|§5.6]] ($\ln$ is the inverse of $e^x$)

> [!theorem] Theorem §24.4: Derivatives of Inverse Hyperbolic Functions
> $$
> \begin{aligned}
> \frac{d}{dx}(\sinh^{-1} x) &= \frac{1}{\sqrt{1 + x^2}} & \frac{d}{dx}(\operatorname{csch}^{-1} x) &= -\frac{1}{|x|\sqrt{x^2 + 1}} \\
> \frac{d}{dx}(\cosh^{-1} x) &= \frac{1}{\sqrt{x^2 - 1}} & \frac{d}{dx}(\operatorname{sech}^{-1} x) &= -\frac{1}{x\sqrt{1 - x^2}} \\
> \frac{d}{dx}(\tanh^{-1} x) &= \frac{1}{1 - x^2} & \frac{d}{dx}(\coth^{-1} x) &= \frac{1}{1 - x^2}
> \end{aligned}
> $$
>
> The formulas for $\tanh^{-1}$ and $\coth^{-1}$ look identical, but their domains have no numbers in common: $\tanh^{-1} x$ is defined for $|x| < 1$, $\coth^{-1} x$ for $|x| > 1$.
>
> *Stewart: 3.11, Table 6 (Example 3.11.4)*

^thm-24-4

> [!proof]+ Proof
> The inverse hyperbolic functions are differentiable because the hyperbolic functions are differentiable with nonzero derivative on the relevant intervals ([[§19 Derivatives of Logarithmic and Inverse Trigonometric Functions#^thm-19-1|Theorem §19.1]], from Appendix F), except at the endpoint $x = 1$ of $\cosh^{-1}$ and $\operatorname{sech}^{-1}$. So implicit differentiation applies. (Alternatively, differentiate Formulas 3–5; see Example §24.2.)
>
> **$\sinh^{-1}$** (Stewart's Example 3.11.4, Solution 1). Let $y = \sinh^{-1} x$, so $\sinh y = x$. Differentiating implicitly, $\cosh y\,\dfrac{dy}{dx} = 1$. Since $\cosh^2 y - \sinh^2 y = 1$ and $\cosh y \ge 0$, $\cosh y = \sqrt{1 + \sinh^2 y}$, so
>
> $$
> \frac{dy}{dx} = \frac{1}{\cosh y} = \frac{1}{\sqrt{1 + \sinh^2 y}} = \frac{1}{\sqrt{1 + x^2}} .
> $$
>
> Stewart leaves the others as exercises; they go the same way, with Theorems §24.1 and §24.2.
>
> **$\cosh^{-1}$.** $\cosh y = x$ with $y \ge 0$ gives $\sinh y\,y' = 1$. For $y \ge 0$, $\sinh y \ge 0$, so $\sinh y = \sqrt{\cosh^2 y - 1} = \sqrt{x^2 - 1}$ and $y' = 1/\sqrt{x^2 - 1}$ ($x > 1$).
>
> **$\tanh^{-1}$.** $\tanh y = x$ gives $\operatorname{sech}^2 y\,y' = 1$, and $\operatorname{sech}^2 y = 1 - \tanh^2 y = 1 - x^2$, so $y' = 1/(1 - x^2)$.
>
> **$\operatorname{csch}^{-1}$.** $\operatorname{csch} y = x$ gives $-\operatorname{csch} y \coth y\,y' = 1$. Here $\operatorname{csch} y \coth y = \cosh y / \sinh^2 y > 0$, and $\coth^2 y = 1 + \operatorname{csch}^2 y$ (divide $\cosh^2 y - \sinh^2 y = 1$ by $\sinh^2 y$), so $\operatorname{csch} y \coth y = |\operatorname{csch} y|\,|\coth y| = |x|\sqrt{1 + x^2}$ and $y' = -1/\big(|x|\sqrt{x^2 + 1}\big)$.
>
> **$\operatorname{sech}^{-1}$.** $\operatorname{sech} y = x$ with $y \ge 0$ gives $-\operatorname{sech} y \tanh y\,y' = 1$. For $y \ge 0$, $\tanh y = \sqrt{1 - \operatorname{sech}^2 y} = \sqrt{1 - x^2}$, so $y' = -1/\big(x\sqrt{1 - x^2}\big)$ ($0 < x < 1$).
>
> **$\coth^{-1}$.** $\coth y = x$ gives $-\operatorname{csch}^2 y\,y' = 1$, and $\operatorname{csch}^2 y = \coth^2 y - 1 = x^2 - 1$, so $y' = -1/(x^2 - 1) = 1/(1 - x^2)$.

^pf-24-4

*Uses:* [[§19 Derivatives of Logarithmic and Inverse Trigonometric Functions#^thm-19-1|§19.1]], [[§24 Hyperbolic Functions#^thm-24-1|§24.1]], [[§24 Hyperbolic Functions#^thm-24-2|§24.2]], [[§24 Hyperbolic Functions#^def-24-2|Def. §24.2]], [[§18 Implicit Differentiation#^rem-18-1|§18]] (implicit differentiation)

> [!example] Example §24.2: Differentiating the Logarithmic Form
> Verify $\dfrac{d}{dx}(\sinh^{-1} x) = \dfrac{1}{\sqrt{1 + x^2}}$ from Formula 3 instead.
>
> By Corollary §19.4 and the Chain Rule,
>
> $$
> \begin{aligned}
> \frac{d}{dx}\ln\big( x + \sqrt{x^2 + 1} \big) &= \frac{1}{x + \sqrt{x^2 + 1}}\,\frac{d}{dx}\big( x + \sqrt{x^2 + 1} \big) = \frac{1}{x + \sqrt{x^2 + 1}} \left( 1 + \frac{x}{\sqrt{x^2 + 1}} \right) \\
> &= \frac{\sqrt{x^2 + 1} + x}{\big( x + \sqrt{x^2 + 1} \big)\sqrt{x^2 + 1}} = \frac{1}{\sqrt{x^2 + 1}} .
> \end{aligned}
> $$
>
> *Stewart: Example 3.11.4 (Solution 2)*

^ex-24-2

> [!example] Example §24.3: An Inverse Hyperbolic Function of a Trigonometric Function
> Find $\dfrac{d}{dx}\big[\tanh^{-1}(\sin x)\big]$.
>
> By Theorem §24.4 and the Chain Rule (note $|\sin x| < 1$ is needed, i.e. $\cos x \ne 0$),
>
> $$
> \frac{d}{dx}\big[\tanh^{-1}(\sin x)\big] = \frac{1}{1 - (\sin x)^2}\,\frac{d}{dx}(\sin x) = \frac{\cos x}{1 - \sin^2 x} = \frac{\cos x}{\cos^2 x} = \sec x .
> $$
>
> *Stewart: Example 3.11.5*

^ex-24-3
