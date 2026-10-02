---
type: section
subject: "[[Complex Variables]]"
chapter: 2
section: 15
bc: "15"
aliases: ["B&C 15"]
tags: [complex-variables, math342]
---
← [[§14 The Mapping w = z²]] · ↑ [[· 2 Analytic Functions]] · [[§16 Theorems on Limits]] →

*Brown–Churchill, Section 15 · MAT 342 HW 2.*

The limit of a function of a complex variable is defined exactly as for a real function of two variables: $f(z)$ must be within $\varepsilon$ of $w_0$ for every $z$ in a small enough *deleted disk* around $z_0$. The decisive word is "every": $z$ may approach $z_0$ from any direction and along any path, and the limit, if it exists, is unique. Together these give the standard test for non-existence: two paths of approach with different limiting values. That test is what later shows that $\bar z$ and $|z|^2$ have no derivatives ([[§19 Derivatives|§19]]) and what produces the Cauchy–Riemann equations, which compare a horizontal with a vertical approach ([[§21 Cauchy–Riemann Equations|§21]]).

## The Definition

> [!definition] Definition §15.1: Limit
> Let a function $f$ be defined at all points $z$ in some deleted neighborhood $0 < |z - z_0| < \rho$ of a point $z_0$. The statement that $f(z)$ **has the limit $w_0$ as $z$ approaches $z_0$**,
>
> $$
> \lim_{z\to z_0} f(z) = w_0 , \qquad (1)
> $$
>
> means that for each positive number $\varepsilon$ there is a positive number $\delta$ such that
>
> $$
> |f(z) - w_0| < \varepsilon \qquad\text{whenever}\qquad 0 < |z - z_0| < \delta . \qquad (2)
> $$
>
> Geometrically: for each $\varepsilon$ neighborhood $|w - w_0| < \varepsilon$ of $w_0$ there is a deleted $\delta$ neighborhood $0 < |z - z_0| < \delta$ of $z_0$ such that every point $z$ in it has its image $w = f(z)$ in the $\varepsilon$ neighborhood.
>
> *B&C: Sec. 15, definition (2)*

^def-15-1

Two remarks on the definition. The images of the points of the deleted neighborhood need not fill the $\varepsilon$ neighborhood; if $f$ has the constant value $w_0$, every image is its center. And once a $\delta$ has been found, it can be replaced by any smaller positive number, such as $\delta/2$. The value $f(z_0)$, if there is one, plays no role in (2).

> [!remark]- Connections
> - With $z = (x, y)$ and $|z - z_0|$ the Euclidean distance, (2) is word for word the limit of a function of two real variables, [[§3 Continuity and Limits of Functions#^def-3-2|452 Def. §3.2]] (computational version [[§91 Limits and Continuity#^def-91-1|Calc Def. §91.1]]), with values in $\mathbb{R}^2$ instead of $\mathbb{R}$. The one-variable ε–δ version is [[§20 Limits of Functions#^rem-20-1|451 Rem. §20.1]].

> [!theorem] Theorem §15.1: Uniqueness of Limits
> When a limit of a function $f(z)$ exists at a point $z_0$, it is unique.
>
> *B&C: Sec. 15, Theorem*

^thm-15-1

> [!proof]+ Proof
> Suppose that
>
> $$
> \lim_{z\to z_0} f(z) = w_0 \qquad\text{and}\qquad \lim_{z\to z_0} f(z) = w_1 .
> $$
>
> Then, for each positive number $\varepsilon$, there are positive numbers $\delta_0$ and $\delta_1$ such that
>
> $$
> |f(z) - w_0| < \varepsilon \quad\text{whenever}\quad 0 < |z - z_0| < \delta_0 \qquad\text{and}\qquad |f(z) - w_1| < \varepsilon \quad\text{whenever}\quad 0 < |z - z_0| < \delta_1 .
> $$
>
> Since $w_1 - w_0 = [f(z) - w_0] + [w_1 - f(z)]$, the triangle inequality gives
>
> $$
> |w_1 - w_0| \le |f(z) - w_0| + |f(z) - w_1| .
> $$
>
> Let $\delta$ be any positive number smaller than $\delta_0$ and $\delta_1$, and pick any $z$ with $0 < |z - z_0| < \delta$ at which $f$ is defined (one exists, since $f$ is defined on a whole deleted neighborhood of $z_0$). For that $z$,
>
> $$
> |w_1 - w_0| < \varepsilon + \varepsilon = 2\varepsilon .
> $$
>
> But $|w_1 - w_0|$ is a nonnegative constant, and $\varepsilon$ can be chosen arbitrarily small. (If $|w_1 - w_0| > 0$, the choice $\varepsilon = \frac12|w_1 - w_0|$ would give $|w_1 - w_0| < |w_1 - w_0|$.) Hence $w_1 - w_0 = 0$, that is, $w_1 = w_0$.

^pf-15-1

*Uses:* [[§15 Limits#^def-15-1|Def. §15.1]], [[§5 Triangle Inequality|§5]] (triangle inequality)

> [!remark]- Connections
> - The same argument for sequences of real numbers, [[§7 Limits of Sequences#^thm-7-1|451 Thm. §7.1]]. It works in any Hausdorff space, the plane being one: [[§8 Hausdorff Spaces#^thm-8-3|590 Thm. §8.3]] (for sequences; disjoint neighborhoods of $w_0 \ne w_1$ cannot both contain $f(z)$).

Definition §15.1 requires $f$ to be defined in a deleted neighborhood of $z_0$, which is always the case when $z_0$ is an interior point of a region ([[§12★ Regions in the Complex Plane|§12★]]) on which $f$ is defined. Points on the edge of the region need a modified definition.

> [!definition] Definition §15.2: Limit at a Boundary Point
> Let $f$ be defined on a region $R$, and let $z_0$ be a boundary point of $R$. Then $\lim_{z\to z_0} f(z) = w_0$ means that condition (2) holds for those points $z$ that lie **both** in $R$ and in the deleted neighborhood $0 < |z - z_0| < \delta$.
>
> *B&C: Sec. 15 (text)*

^def-15-2

Every deleted neighborhood of a boundary point of a region contains points of the region, so uniqueness (Theorem §15.1) holds for this extended limit too, with the same proof.

> [!example] Example §15.1: A Limit at a Boundary Point
> Let $f(z) = i\bar z/2$ in the open disk $|z| < 1$. Show that
>
> $$
> \lim_{z\to1} f(z) = \frac i2 , \qquad (3)
> $$
>
> the point $1$ being on the boundary of the domain of definition of $f$.
>
> When $z$ is in the disk $|z| < 1$,
>
> $$
> \Big|f(z) - \frac i2\Big| = \Big|\frac{i\bar z}{2} - \frac i2\Big| = \frac{|i|\,|\bar z - 1|}{2} = \frac{|\overline{z - 1}|}{2} = \frac{|z - 1|}{2} .
> $$
>
> Hence, for any such $z$ and each positive number $\varepsilon$,
>
> $$
> \Big|f(z) - \frac i2\Big| < \varepsilon \qquad\text{whenever}\qquad 0 < |z - 1| < 2\varepsilon .
> $$
>
> Thus condition (2) is satisfied by the points of the region $|z| < 1$ when $\delta = 2\varepsilon$ or any smaller positive number. Geometrically, the points $z$ of the disk within $2\varepsilon$ of $1$ (a lens-shaped region) are mapped into the disk of radius $\varepsilon$ about $i/2$.
>
> *B&C: Sec. 15, Example 1*

^ex-15-1

## Approach from Every Direction

If limit (1) exists, the symbol $z \to z_0$ means that $z$ is allowed to approach $z_0$ in an arbitrary manner, not just from some particular direction. Combined with uniqueness, this gives a practical test.

> [!theorem] Corollary §15.2: Two-Path Test
> Suppose that, as $z$ approaches $z_0$ through the points of a set $A$ (having $z_0$ as an accumulation point), $f(z)$ tends to $a$, and as $z$ approaches $z_0$ through the points of another set $B$, $f(z)$ tends to $b$. If $a \ne b$, then $\lim_{z\to z_0} f(z)$ does not exist.
>
> *B&C: Sec. 15 (text before Example 2)*

^cor-15-2

> [!proof]+ Proof
> If $\lim_{z\to z_0} f(z) = w_0$ existed, then condition (2) would hold for all $z$ in the deleted neighborhood, in particular for those in $A$; so $f(z) \to w_0$ as $z \to z_0$ through $A$, and by uniqueness of limits (the proof of Theorem §15.1, applied to $f$ restricted to $A$) $w_0 = a$. In the same way $w_0 = b$. This contradicts $a \ne b$.

^pf-15-2

*Uses:* [[§15 Limits#^def-15-1|Def. §15.1]], [[§15 Limits#^thm-15-1|§15.1]]

> [!remark]- Connections
> - The real two-variable version: [[§91 Limits and Continuity#^thm-91-1|Calc Thm. §91.1]], with the example $2xy/(x^2 + y^2)$, [[§3 Continuity and Limits of Functions#^ex-3-2|452 Ex. §3.2]].

> [!example] Example §15.2: z/z̄ Has No Limit at 0
> If
>
> $$
> f(z) = \frac{z}{\bar z} , \qquad (4)
> $$
>
> the limit
>
> $$
> \lim_{z\to0} f(z) \qquad (5)
> $$
>
> does not exist. If it existed, it could be found by letting $z = (x, y)$ approach the origin in any manner. When $z = (x, 0)$ is a nonzero point on the real axis,
>
> $$
> f(z) = \frac{x + i0}{x - i0} = 1 ;
> $$
>
> and when $z = (0, y)$ is a nonzero point on the imaginary axis,
>
> $$
> f(z) = \frac{0 + iy}{0 - iy} = -1 .
> $$
>
> So an approach along the real axis would give the limit $1$, an approach along the imaginary axis the limit $-1$. Since a limit is unique, limit (5) does not exist (Corollary §15.2).
>
> In polar form the picture is complete: for $z = re^{i\theta}$, $f(z) = e^{i\theta}/e^{-i\theta} = e^{2i\theta}$ depends only on the direction of approach, and every value on the unit circle is taken in every deleted neighborhood of $0$.
>
> *B&C: Sec. 15, Example 2*

^ex-15-2

> [!example] Example §15.3: Two Directions Can Agree Without a Limit
> Show that
>
> $$
> f(z) = \Big(\frac{z}{\bar z}\Big)^2
> $$
>
> has the value $1$ at all nonzero points of the real and imaginary axes, but the value $-1$ at all nonzero points of the line $y = x$; conclude that $\lim_{z\to0} f(z)$ does not exist.
>
> On the real axis, $z = (x, 0)$ with $x \ne 0$: $f(z) = (x/x)^2 = 1$. On the imaginary axis, $z = (0, y)$ with $y \ne 0$: $f(z) = \big(iy/(-iy)\big)^2 = (-1)^2 = 1$. On the line $y = x$, $z = (x, x) = x(1 + i)$ with $x \ne 0$:
>
> $$
> f(z) = \Big(\frac{x(1 + i)}{x(1 - i)}\Big)^2 = \Big(\frac{(1 + i)^2}{(1 - i)(1 + i)}\Big)^2 = \Big(\frac{2i}{2}\Big)^2 = i^2 = -1 .
> $$
>
> Every deleted neighborhood of $0$ contains points of the axes and of the line $y = x$, so by Corollary §15.2 the limit does not exist. It is **not sufficient** to consider only the nonzero points $(x, 0)$ and $(0, y)$, as in Example §15.2: here both axes give $1$. In polar form $f(z) = e^{4i\theta}$, which is $1$ for $\theta = 0, \pi/2, \pi, 3\pi/2$ and $-1$ on the diagonals.
>
> *B&C: Sec. 18, Exercise 5; Source: 342 HW 2*

^ex-15-3

Limits at a point $z_0 \ne 0$ can be moved to the origin by the substitution $\Delta z = z - z_0$. B&C leaves this as an exercise, and later uses it in [[§19 Derivatives|§19]] and [[§20 Rules for Differentiation|§20]].

> [!theorem] Proposition §15.3: Moving the Point to the Origin
> Write $\Delta z = z - z_0$. Then
>
> $$
> \lim_{z\to z_0} f(z) = w_0 \qquad\text{if and only if}\qquad \lim_{\Delta z\to0} f(z_0 + \Delta z) = w_0 .
> $$
>
> *B&C: Sec. 18, Exercise 8*

^prop-15-3

> [!proof]+ Proof
> Put $g(\Delta z) = f(z_0 + \Delta z)$; $g$ is defined in a deleted neighborhood of $0$ exactly when $f$ is defined in the deleted neighborhood of $z_0$ of the same radius. The statement $\lim_{\Delta z\to0} g(\Delta z) = w_0$ means: for each $\varepsilon > 0$ there is $\delta > 0$ with
>
> $$
> |f(z_0 + \Delta z) - w_0| < \varepsilon \qquad\text{whenever}\qquad 0 < |\Delta z - 0| < \delta .
> $$
>
> As $\Delta z$ runs over the deleted disk $0 < |\Delta z| < \delta$, the point $z = z_0 + \Delta z$ runs over exactly the deleted disk $0 < |z - z_0| < \delta$, and $|\Delta z - 0| = |z - z_0|$. So this is word for word condition (2) for $\lim_{z\to z_0} f(z) = w_0$, with the same $\delta$.

^pf-15-3

*Uses:* [[§15 Limits#^def-15-1|Def. §15.1]]

> [!example] Example §15.4: A Shifted Version of z/z̄
> Determine whether
>
> $$
> \lim_{z\to i}\frac{z - i}{\bar z + i}
> $$
>
> exists.
>
> **Direct argument.** Numerator and denominator both tend to $0$ ($z \to i$ gives $\bar z \to -i$), so no limit law applies. Approach $i$ vertically, through $z = iy$ with $y \ne 1$:
>
> $$
> \frac{iy - i}{-iy + i} = \frac{i(y - 1)}{i(1 - y)} = -1 .
> $$
>
> Approach horizontally, through $z = x + i$ with $x \ne 0$:
>
> $$
> \frac{x + i - i}{x - i + i} = \frac xx = 1 .
> $$
>
> The two approaches give different values, so by Corollary §15.2 the limit does not exist.
>
> **Why.** Since $\bar z + i = \overline{z - i}$, the function is $\Delta z/\overline{\Delta z}$ with $\Delta z = z - i$: by Proposition §15.3 the limit at $i$ is the limit at $0$ of the function of Example §15.2, which does not exist.
>
> *Source: 342 HW 2, Problem 3(b)*

^ex-15-4

> [!remark] Remark: Method — Deciding Whether a Limit Exists
> 1. **Try the limit laws first** ([[§16 Theorems on Limits|§16]]): if $f$ is built from continuous pieces and no denominator tends to $0$, the limit is the value. If a factor cancels, cancel it first ([[§16 Theorems on Limits#^ex-16-1|Example §16.1]]).
> 2. **If a $0/0$ form involving $\bar z$, $\operatorname{Re} z$, $\operatorname{Im} z$ or $|z|$ remains,** suspect non-existence. Shift the point to $0$ (Proposition §15.3) and compute $f$ along rays $z_0 + te^{i\theta}$, $t \to 0^+$; quotients such as $\overline{\Delta z}/\Delta z = e^{-2i\theta}$ depend only on the direction. Two directions with different limits settle the matter (Corollary §15.2). Check the axes **and** the diagonals (Example §15.3).
> 3. **If all directions agree,** the limit may still fail along curves; to prove that a limit exists, estimate $|f(z) - w_0|$ by a multiple of $|z - z_0|$ or another quantity tending to $0$, as in Example §15.1 and [[§18 Continuity#^ex-18-1|Example §18.1]].

^rem-15-1
