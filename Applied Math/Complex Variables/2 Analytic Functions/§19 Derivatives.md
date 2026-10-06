---
type: section
subject: "[[Complex Variables]]"
chapter: 2
section: 19
bc: "19"
aliases: ["B&C 19"]
tags: [complex-variables, math342]
---
← [[§18 Continuity]] · ↑ [[· 2 Analytic Functions]] · [[§20 Rules for Differentiation]] →

*Brown–Churchill, Section 19 · MAT 342 HW 3.*

The derivative of a complex function is defined by the same difference quotient as in calculus, but the increment $\Delta z$ now tends to $0$ through the plane, from every direction at once. This makes complex differentiability a far stronger condition than it looks. The function $\bar z$, whose real and imaginary parts are as smooth as can be, has a derivative nowhere, and $|z|^2$ has one at the single point $0$. The examples of this section show how to detect such failures by comparing horizontal and vertical approaches, and the one general fact proved is that a derivative forces continuity. Systematizing the horizontal and vertical comparison gives the Cauchy–Riemann equations of [[§21 Cauchy–Riemann Equations#^thm-21-1|Theorem §21.1]].

## The Derivative

> [!definition] Definition §19.1: Derivative
> Let $f$ be a function whose domain of definition contains a neighborhood $|z - z_0| < \varepsilon$ of a point $z_0$. The **derivative** of $f$ at $z_0$ is the limit
>
> $$
> f'(z_0) = \lim_{z\to z_0}\frac{f(z) - f(z_0)}{z - z_0} , \qquad (1)
> $$
>
> and $f$ is **differentiable at $z_0$** when $f'(z_0)$ exists.
>
> With the new complex variable $\Delta z = z - z_0$ ($z \ne z_0$) the definition reads
>
> $$
> f'(z_0) = \lim_{\Delta z\to0}\frac{f(z_0 + \Delta z) - f(z_0)}{\Delta z} . \qquad (2)
> $$
>
> Dropping the subscript on $z_0$ and writing $\Delta w = f(z + \Delta z) - f(z)$ for the change in $w = f(z)$, and $dw/dz$ for $f'(z)$,
>
> $$
> \frac{dw}{dz} = \lim_{\Delta z\to0}\frac{\Delta w}{\Delta z} . \qquad (3)
> $$
>
> *B&C: Sec. 19, definitions (1)–(3)*

^def-19-1

Forms (1) and (2) are equivalent by [[§15 Limits#^prop-15-3|Proposition §15.3]]. Because $f$ is defined throughout a neighborhood of $z_0$, the number $f(z_0 + \Delta z)$ is always defined for $|\Delta z|$ sufficiently small.

> [!remark]- Connections
> - Formally the same as the real derivative, [[§28 Basic Properties of the Derivative#^def-28-1|451 Def. §28.1]], with $x$ replaced by $z$. It is not the same as differentiability of $(u, v)$ as a map of $\mathbb{R}^2$, [[§7 Differentiability#^def-7-1|452 Def. §7.1]]: Example §19.2 below is real-differentiable everywhere and complex-differentiable nowhere. The exact relation is the Cauchy–Riemann equations of [[§21 Cauchy–Riemann Equations#^thm-21-1|Theorem §21.1]] and [[§23 Sufficient Conditions for Differentiability#^thm-23-1|Theorem §23.1]].

> [!example] Example §19.1: The Derivative of 1/z
> Let $f(z) = 1/z$. At each nonzero point $z$,
>
> $$
> \lim_{\Delta z\to0}\frac{\Delta w}{\Delta z} = \lim_{\Delta z\to0}\Big(\frac{1}{z + \Delta z} - \frac1z\Big)\frac{1}{\Delta z} = \lim_{\Delta z\to0}\frac{z - (z + \Delta z)}{(z + \Delta z)z\,\Delta z} = \lim_{\Delta z\to0}\frac{-1}{(z + \Delta z)z} ,
> $$
>
> provided these limits exist (for $0 < |\Delta z| < |z|$ the point $z + \Delta z$ is nonzero, so the quotients are defined). As $\Delta z \to 0$, $(z + \Delta z)z \to z^2 \ne 0$, so by the limit theorems of [[§16 Theorems on Limits#^thm-16-2|Theorem §16.2]] the last limit exists:
>
> $$
> \frac{dw}{dz} = -\frac{1}{z^2}, \qquad\text{or}\qquad f'(z) = -\frac{1}{z^2} \qquad (z \ne 0) .
> $$
>
> *B&C: Sec. 19, Example 1*

^ex-19-1

> [!example] Example §19.2: z̄ Is Nowhere Differentiable
> Let $f(z) = \bar z$. Then
>
> $$
> \frac{\Delta w}{\Delta z} = \frac{\overline{z + \Delta z} - \bar z}{\Delta z} = \frac{\bar z + \overline{\Delta z} - \bar z}{\Delta z} = \frac{\overline{\Delta z}}{\Delta z} . \qquad (4)
> $$
>
> If the limit of $\Delta w/\Delta z$ exists, it can be found by letting $\Delta z = (\Delta x, \Delta y)$ approach $(0, 0)$ in any manner. As $\Delta z$ approaches $(0, 0)$ horizontally, through the points $(\Delta x, 0)$ of the real axis,
>
> $$
> \overline{\Delta z} = \overline{\Delta x + i0} = \Delta x - i0 = \Delta x + i0 = \Delta z ,
> $$
>
> and (4) gives $\Delta w/\Delta z = \Delta z/\Delta z = 1$. So if the limit exists, its value is $1$. But as $\Delta z$ approaches $(0, 0)$ vertically, through the points $(0, \Delta y)$ of the imaginary axis,
>
> $$
> \overline{\Delta z} = \overline{0 + i\Delta y} = 0 - i\Delta y = -(0 + i\Delta y) = -\Delta z ,
> $$
>
> and (4) gives $\Delta w/\Delta z = -\Delta z/\Delta z = -1$. So the limit must be $-1$ if it exists. Since limits are unique ([[§15 Limits#^thm-15-1|Theorem §15.1]]), $dw/dz$ does not exist; and since $z$ was arbitrary, it exists nowhere. (The quotient (4) is the function $z/\bar z$ of [[§15 Limits#^ex-15-2|Example §15.2]] turned upside down.)
>
> *B&C: Sec. 19, Example 2*

^ex-19-2

> [!example] Example §19.3: |z|² Is Differentiable Only at 0
> Consider the real-valued function $f(z) = |z|^2$. Here
>
> $$
> \frac{\Delta w}{\Delta z} = \frac{|z + \Delta z|^2 - |z|^2}{\Delta z} = \frac{(z + \Delta z)\overline{(z + \Delta z)} - z\bar z}{\Delta z} ;
> $$
>
> and since $\overline{z + \Delta z} = \bar z + \overline{\Delta z}$, multiplying out ($z\bar z$ cancels) gives
>
> $$
> \frac{\Delta w}{\Delta z} = \bar z + \overline{\Delta z} + z\,\frac{\overline{\Delta z}}{\Delta z} . \qquad (5)
> $$
>
> Proceeding as in Example §19.2, where the horizontal and vertical approaches gave $\overline{\Delta z} = \Delta z$ and $\overline{\Delta z} = -\Delta z$,
>
> $$
> \frac{\Delta w}{\Delta z} = \bar z + \Delta z + z \quad\text{when}\quad \Delta z = (\Delta x, 0), \qquad \frac{\Delta w}{\Delta z} = \bar z - \Delta z - z \quad\text{when}\quad \Delta z = (0, \Delta y) .
> $$
>
> As $\Delta z \to 0$ these tend to $\bar z + z$ and $\bar z - z$. If the limit of $\Delta w/\Delta z$ exists, uniqueness of limits gives $\bar z + z = \bar z - z$, that is, $z = 0$. So $dw/dz$ cannot exist if $z \ne 0$.
>
> At $z = 0$, expression (5) reduces to $\Delta w/\Delta z = \overline{\Delta z}$, which tends to $0$ (its modulus is $|\Delta z|$). So $dw/dz$ exists **only** at $z = 0$, and its value there is $0$.
>
> *B&C: Sec. 19, Example 3*

^ex-19-3

> [!remark] Remark: What |z|² Shows
> Example §19.3 illustrates three facts, the first two of which may be surprising.
> 1. A function $f(z) = u(x, y) + iv(x, y)$ can be differentiable at a point $z = (x, y)$ but nowhere else in any neighborhood of that point.
> 2. Since $u(x, y) = x^2 + y^2$ and $v(x, y) = 0$ when $f(z) = |z|^2$, the real and imaginary components of a function of a complex variable can have continuous partial derivatives of all orders at a point, and yet the function may not be differentiable there.
> 3. The components $u = x^2 + y^2$ and $v = 0$ are continuous everywhere, so $f$ is continuous everywhere ([[§18 Continuity#^thm-18-4|Theorem §18.4]]), but $f'(z)$ does not exist at any nonzero point: **continuity at a point does not imply the existence of the derivative there.**

^rem-19-1

The converse does hold.

> [!theorem] Theorem §19.1: Differentiable Implies Continuous
> If $f'(z_0)$ exists, then $f$ is continuous at $z_0$.
>
> *B&C: Sec. 19 (text)*

^thm-19-1

> [!proof]+ Proof
> Assume that $f'(z_0)$ exists. For $z \ne z_0$, $f(z) - f(z_0) = \dfrac{f(z) - f(z_0)}{z - z_0}\,(z - z_0)$, and both factors have limits as $z \to z_0$. By the product rule (9) of [[§16 Theorems on Limits#^thm-16-2|Theorem §16.2]],
>
> $$
> \lim_{z\to z_0}\big[f(z) - f(z_0)\big] = \lim_{z\to z_0}\frac{f(z) - f(z_0)}{z - z_0}\,\lim_{z\to z_0}(z - z_0) = f'(z_0)\cdot0 = 0 ,
> $$
>
> from which, adding the constant $f(z_0)$ by the sum rule (8), $\lim_{z\to z_0} f(z) = f(z_0)$. Since $f$ is defined at $z_0$, this is the statement of continuity of $f$ at $z_0$ ([[§18 Continuity#^def-18-1|Definition §18.1]]).

^pf-19-1

*Uses:* [[§19 Derivatives#^def-19-1|Def. §19.1]], [[§16 Theorems on Limits#^thm-16-2|§16.2]], [[§16 Theorems on Limits#^cor-16-3|§16.3]], [[§18 Continuity#^def-18-1|Def. §18.1]]

> [!remark]- Connections
> - The real version and its proof: [[§28 Basic Properties of the Derivative#^thm-28-1|451 Thm. §28.1]].

## Showing That a Derivative Does Not Exist

> [!remark] Remark: Method — Showing That f′(z₀) Does Not Exist
> 1. Write the difference quotient $\Delta w/\Delta z = \big(f(z_0 + \Delta z) - f(z_0)\big)/\Delta z$ and simplify it, isolating expressions in $\overline{\Delta z}$, $\operatorname{Re}\Delta z$, $\operatorname{Im}\Delta z$ or $|\Delta z|$.
> 2. Let $\Delta z \to 0$ **horizontally** ($\Delta z = \Delta x$, so $\overline{\Delta z} = \Delta z$) and **vertically** ($\Delta z = i\Delta y$, so $\overline{\Delta z} = -\Delta z$). If the two limits differ, $f'(z_0)$ does not exist, by uniqueness of limits.
> 3. If they agree, this proves nothing: also try other directions $\Delta z = te^{i\theta}$, such as the diagonal ([[§22 Examples (Cauchy–Riemann Equations)#^ex-22-3|Example §22.3]]). To prove that $f'(z_0)$ *does* exist, simplify $\Delta w/\Delta z$ into a form whose limit follows from the limit theorems, as in Example §19.1 and at $z = 0$ in Example §19.3.
>
> Step 2 done once and for all, at every point, gives the Cauchy–Riemann equations ([[§21 Cauchy–Riemann Equations#^thm-21-1|Theorem §21.1]]).

^rem-19-2

> [!example] Example §19.4: Re z and Im z Are Nowhere Differentiable
> Show that $f'(z)$ does not exist at any point when (a) $f(z) = \operatorname{Re} z$; (b) $f(z) = \operatorname{Im} z$.
>
> **(a)** Since $\operatorname{Re}(z + \Delta z) = \operatorname{Re} z + \operatorname{Re}\Delta z$,
>
> $$
> \frac{\Delta w}{\Delta z} = \frac{\operatorname{Re}(z + \Delta z) - \operatorname{Re} z}{\Delta z} = \frac{\operatorname{Re}\Delta z}{\Delta z} = \frac{\Delta x}{\Delta x + i\Delta y} .
> $$
>
> Horizontally ($\Delta y = 0$) this is $\Delta x/\Delta x = 1$; vertically ($\Delta x = 0$) it is $0/(i\Delta y) = 0$. The limits $1$ and $0$ differ, so $f'(z)$ does not exist, at any $z$.
>
> **(b)** Similarly
>
> $$
> \frac{\Delta w}{\Delta z} = \frac{\operatorname{Im}\Delta z}{\Delta z} = \frac{\Delta y}{\Delta x + i\Delta y} ,
> $$
>
> which is $0$ horizontally and $\Delta y/(i\Delta y) = -i$ vertically. So $f'(z)$ exists nowhere.
>
> Both functions are real-valued. For a real-valued function the horizontal difference quotient $\Delta w/\Delta x$ is real and the vertical one $\Delta w/(i\Delta y)$ is purely imaginary, so the only possible value of a derivative is $0$; compare [[§26 Further Examples (Analytic Functions)#^ex-26-5|Example §26.5]], where a real-valued function with a derivative everywhere turns out to be constant.
>
> *B&C: Sec. 20, Exercise 8; Source: 342 HW 3 (part (a))*

^ex-19-4

Geometric interpretations of derivatives of functions of a complex variable are not as immediate as for functions of a real variable; B&C defers them to Chapter 9, where $f'(z_0) \ne 0$ is shown to mean that $f$ rotates all directions at $z_0$ by $\arg f'(z_0)$ and stretches all short segments by $|f'(z_0)|$ ([[§112★ Preservation of Angles and Scale Factors#^thm-112-1|Theorem §112.1]], [[§112★ Preservation of Angles and Scale Factors#^prop-112-4|Proposition §112.4]]).
