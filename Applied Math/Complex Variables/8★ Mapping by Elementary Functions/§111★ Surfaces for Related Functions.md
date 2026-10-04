---
type: section
subject: "[[Complex Variables]]"
chapter: 8
section: 111
bc: "111"
aliases: ["B&C 111"]
tags: [complex-variables, math342, extension]
---
← [[§110★ Riemann Surfaces]] · ↑ [[· 8★ Mapping by Elementary Functions]] · [[§112★ Preservation of Angles and Scale Factors]] →

*Brown–Churchill, Section 111.*
★ *Beyond MAT 342: the course skipped this section or left it optional; it is included from Brown–Churchill.*

With several branch points, a Riemann surface is built from cuts that join branch points in pairs, or run from a branch point to infinity, so that a circuit around a whole cut leaves the function unchanged. The bookkeeping is done with one angle per branch point: the value is unchanged exactly when the total change of the angles is a multiple of $4\pi$ (for a square root). This section builds two-sheeted surfaces for $(z^2 - 1)^{1/2}$, whose cut is the segment of [[§109★ Square Roots of Polynomials|§109]], and for $[z(z^2 - 1)]^{1/2}$, where the point at infinity is itself a branch point. The examples include the surface for $z + (z^2 - 1)^{1/2}$, the inverse of the Joukowski map $z = \frac12(w + 1/w)$.

> [!remark] Remark: Method — Building a Riemann Surface for a Root
> For $f(z) = [p(z)]^{1/n}$, or a product of such factors:
> 1. **Branch points.** These are the zeros (and poles) of odd multiplicity for a square root, and the point at infinity if $f(1/z)$ has a branch point at $z = 0$. Introduce $z - z_k = r_ke^{i\theta_k}$ for each finite one, so that $\arg f$ is a fixed combination of the $\theta_k$.
> 2. **Sheets.** One sheet per value: $n$ sheets for an $n$th root.
> 3. **Cuts.** Join the branch points in pairs, or to $\infty$, by cuts such that a circuit around any whole cut changes $\arg f$ by a multiple of $2\pi$.
> 4. **Angle ranges and gluing.** Give the angles definite ranges on each sheet, and join the lower edge of each slit on one sheet to the upper edge of the same slit on the sheet where the angles continue.

^rem-111-1

## Two Square Roots of Cubic and Quadratic Polynomials

> [!example] Example §111.1: A Riemann Surface for (z² − 1)^(1/2)
> Describe a Riemann surface for the double-valued function
>
> $$
> f(z) = (z^2 - 1)^{1/2} = \sqrt{r_1r_2}\exp\frac{i(\theta_1 + \theta_2)}{2} , \qquad (1)
> $$
>
> where $z - 1 = r_1\exp(i\theta_1)$ and $z + 1 = r_2\exp(i\theta_2)$.
>
> A branch with the segment $P_2P_1$ between the branch points $z = \pm1$ as branch cut is the function $F$ of [[§109★ Square Roots of Polynomials#^def-109-1|Definition §109.1]]: (1) with $r_k > 0$, $0 \le \theta_k < 2\pi$ and $r_1 + r_2 > 2$. The surface has two sheets $R_0$ and $R_1$, both cut along $P_2P_1$; the lower edge of the slit in $R_0$ is joined to the upper edge in $R_1$, and the lower edge in $R_1$ to the upper edge in $R_0$.
>
> **On $R_0$**, let $\theta_1$ and $\theta_2$ range from $0$ to $2\pi$. If a point on $R_0$ describes a simple closed curve enclosing the segment once counterclockwise, both $\theta_1$ and $\theta_2$ change by $2\pi$, so $(\theta_1 + \theta_2)/2$ changes by $2\pi$ and the value of $f$ is unchanged: the point stays on $R_0$ (it never crosses the slit). If it passes twice around just $z = 1$, it crosses onto $R_1$ and back onto $R_0$; $\theta_1$ changes by $4\pi$ and $\theta_2$ not at all, so again $(\theta_1 + \theta_2)/2$ changes by $2\pi$. The same holds for two circuits around $z = -1$. So on $R_0$ the angles may be changed by the same multiple of $2\pi$, or one of them by a multiple of $4\pi$: in either case the total change is an even multiple of $2\pi$.
>
> **On $R_1$.** A path starting on $R_0$ that goes once around just one branch point crosses onto $R_1$ and does not return. One angle has changed by $2\pi$, the other not. So on $R_1$ one angle ranges from $2\pi$ to $4\pi$ and the other from $0$ to $2\pi$; their sum ranges from $2\pi$ to $4\pi$, and $\arg f = (\theta_1 + \theta_2)/2$ ranges from $\pi$ to $2\pi$. The ranges are extended as on $R_0$. Since the extra $2\pi$ in the sum changes $e^{i(\theta_1 + \theta_2)/2}$ by the factor $e^{i\pi} = -1$, the values on $R_1$ are those of the other branch, $-F$.
>
> The double-valued function (1) is thus a single-valued function of the points of the surface. Each sheet, with the edges of its slit, is mapped by $w = f(z)$ onto the entire $w$ plane: $R_0$ by $F$ onto the plane minus $[-i, i]$ ([[§109★ Square Roots of Polynomials#^thm-109-3|Theorem §109.3]]), its upper edge onto $[0, i]$ (values $i\sqrt{1 - x^2}$) and its lower edge onto $[-i, 0]$; and $R_1$ likewise by $-F$.
>
> *B&C: Sec. 111, Example 1*

^ex-111-1

![[m342-111-1.svg]]
*The coordinates used in §111. Left: for $(z^2 - 1)^{1/2}$ the cut (orange) joins the branch points $P_2 = -1$ and $P_1 = 1$, and $\arg f = \frac12(\theta_1 + \theta_2)$; a loop around the whole cut changes $\theta_1$ and $\theta_2$ by $2\pi$ each and leaves $f$ unchanged. Right: for $[z(z^2 - 1)]^{1/2}$ the branch points are $-1, 0, 1$ and $\infty$, and the cuts $L_2$ from $-1$ to $0$ and $L_1$ from $1$ to $\infty$ pair them off.*

> [!example] Example §111.2: A Riemann Surface for [z(z² − 1)]^(1/2)
> Consider
>
> $$
> f(z) = [z(z^2 - 1)]^{1/2} = \sqrt{rr_1r_2}\exp\frac{i(\theta + \theta_1 + \theta_2)}{2} , \qquad (2)
> $$
>
> with $z = re^{i\theta}$, $z - 1 = r_1e^{i\theta_1}$, $z + 1 = r_2e^{i\theta_2}$. The points $z = 0, \pm1$ are branch points.
>
> **Infinity is a branch point.** If $z$ describes a circuit enclosing all three points, each of the three angles changes by $2\pi$, so $\arg f$ changes by $3\pi$ and the value changes sign. So a cut must run from one of the finite branch points to infinity. Equivalently, $f(1/z) = \big[(1 - z^2)/z^3\big]^{1/2}$ has a branch point at $z = 0$: a small circuit around $0$ changes $\arg\big[(1 - z^2)/z^3\big]$ by $-6\pi$ and so changes the sign of $f(1/z)$.
>
> **The surface.** Cut two sheets along the segment $L_2$ from $z = -1$ to $z = 0$ and along the part $L_1$ of the real axis to the right of $z = 1$. On $R_0$ let each of $\theta, \theta_1, \theta_2$ range from $0$ to $2\pi$, and on $R_1$ from $2\pi$ to $4\pi$; on either sheet the angles may be changed by multiples of $2\pi$ as long as their sum changes by a multiple of $4\pi$, which leaves $f$ unaltered. Join the lower edges in $R_0$ of the slits along $L_1$ and $L_2$ to the upper edges in $R_1$ of the same slits, and the lower edges in $R_1$ to the upper edges in $R_0$. A circuit around $L_2$ alone (enclosing $0$ and $-1$) changes $\theta + \theta_2$ by $4\pi$ and leaves the value unchanged, so the cuts are consistent. One branch of $f$ is given by its values on $R_0$ and the other by its values on $R_1$, which differ by the factor $e^{i\cdot 3\pi} = -1$.
>
> **Three points over each value.** Corresponding to each point of this surface there is one value $w = f(z)$; conversely, for a given $w$ the equation $z(z^2 - 1) = w^2$ is a cubic with three roots (counted with multiplicity). Over each root $z$ lie two points of the surface, carrying the values $\pm\sqrt{z(z^2 - 1)}$, and exactly one of them carries $w$ (if $w \ne 0$). So in general each $w$ comes from three points of the surface.
>
> *B&C: Sec. 111, Example 2 and Exercise 2*

^ex-111-2

## Examples

> [!example] Example §111.3: A Three-Sheeted Surface for (z − 1)^(1/3)
> Write $z - 1 = \rho e^{i\theta}$. The function $w = (z - 1)^{1/3} = \sqrt[3]{\rho}\,e^{i\theta/3}$ has three values, with branch points $z = 1$ and $z = \infty$. Take three sheets $R_0, R_1, R_2$, each cut along the ray $x \ge 1$ from the branch point, with $0 \le \theta \le 2\pi$ on $R_0$, $2\pi \le \theta \le 4\pi$ on $R_1$ and $4\pi \le \theta \le 6\pi$ on $R_2$. Join the lower edge of the slit in $R_0$ to the upper edge in $R_1$, the lower edge in $R_1$ to the upper edge in $R_2$, and the lower edge in $R_2$ to the upper edge in $R_0$ (allowed, since adding $6\pi$ to $\theta$ multiplies $e^{i\theta/3}$ by $e^{2\pi i} = 1$). A closed curve around $z = 1$ must wind three times around it.
>
> Since $\arg w = \theta/3$, the sheet $R_k$ goes onto the sector
>
> $$
> \frac{2k\pi}{3} \le \arg w \le \frac{2(k + 1)\pi}{3} \qquad (k = 0, 1, 2) :
> $$
>
> each sheet onto one third of the $w$ plane.
>
> *B&C: Sec. 111, Exercise 1*

^ex-111-3

> [!example] Example §111.4: A Riemann Surface for ((z − 1)/z)^(1/2)
> Write $z = re^{i\theta}$ and $z - 1 = r_1e^{i\theta_1}$, so that
>
> $$
> f(z) = \Big(\frac{z - 1}{z}\Big)^{1/2} = \sqrt{\frac{r_1}{r}}\exp\frac{i(\theta_1 - \theta)}{2} .
> $$
>
> The finite branch points are $z = 0$ and $z = 1$: a small circuit around either changes one angle by $2\pi$ and the sign of $f$. The point at infinity is not a branch point: $f(1/z) = (1 - z)^{1/2}$, and near $z = 0$ the factor $1 - z$ stays near $1$, so each branch of $f(1/z)$ is analytic there. Equivalently, a circuit enclosing both $0$ and $1$ changes $\theta_1$ and $\theta$ by $2\pi$ each and leaves $\theta_1 - \theta$ unchanged.
>
> So cut two sheets $R_0$, $R_1$ along the segment $0 \le x \le 1$. On $R_0$ let $\theta$ and $\theta_1$ range over $[0, 2\pi)$; on $R_1$ let one of them be increased by $2\pi$, which changes $(\theta_1 - \theta)/2$ by $\pm\pi$ and $f$ by the factor $-1$. Join the lower edge of the slit in $R_0$ to the upper edge in $R_1$, and the lower edge in $R_1$ to the upper edge in $R_0$. The function is single-valued on this surface, the branch on $R_0$ tending to $1$ at infinity and that on $R_1$ to $-1$.
>
> *B&C: Sec. 111, Exercise 3*

^ex-111-4

> [!example] Example §111.5: The Surface for z + (z² − 1)^(1/2) and the Joukowski Map
> The surface of Example §111.1 is also a Riemann surface for $g(z) = z + (z^2 - 1)^{1/2}$. Let $f_0 = F$ be the branch of $(z^2 - 1)^{1/2}$ on $R_0$, so $-f_0$ is the branch on $R_1$, and let $g_0 = z + f_0$, $g_1 = z - f_0$ be the branches of $g$ on the two sheets.
>
> **(a) $g_0 = 1/g_1$.** $g_0g_1 = z^2 - f_0^2 = z^2 - (z^2 - 1) = 1$.
>
> **(b) $|g_0| \ge 1$.** Write $f_0(z) = \sqrt{r_1r_2}\exp\frac{i\theta_1}{2}\exp\frac{i\theta_2}{2}$ ($0 \le \theta_k < 2\pi$) and note $2z = r_1e^{i\theta_1} + r_2e^{i\theta_2}$. Then
>
> $$
> g_0(z) = \frac12\Big(\sqrt{r_1}\exp\frac{i\theta_1}{2} + \sqrt{r_2}\exp\frac{i\theta_2}{2}\Big)^2 ,
> $$
>
> since the square expands to $r_1e^{i\theta_1} + r_2e^{i\theta_2} + 2\sqrt{r_1r_2}\,e^{i(\theta_1 + \theta_2)/2} = 2z + 2f_0$. Hence
>
> $$
> |g_0(z)| = \sqrt{g_0(z)\overline{g_0(z)}} = \frac12\Big|\sqrt{r_1}e^{i\theta_1/2} + \sqrt{r_2}e^{i\theta_2/2}\Big|^2 = \frac12\Big[r_1 + r_2 + 2\sqrt{r_1r_2}\cos\frac{\theta_1 - \theta_2}{2}\Big] .
> $$
>
> Now $r_1 + r_2 \ge 2$ (triangle inequality, as in Definition §109.1), and $|\theta_1 - \theta_2| \le \pi$ because $\theta_1 - \theta_2$ is the angle at $z$ subtended by the segment $[-1, 1]$, so $\cos\frac{\theta_1 - \theta_2}{2} \ge 0$. Therefore $|g_0(z)| \ge 1$, with equality only when $r_1 + r_2 = 2$ and $|\theta_1 - \theta_2| = \pi$, that is, on the edges of the cut.
>
> **(c) The mapping.** By (a) and (b), $|g_1| = 1/|g_0| \le 1$. So $w = z + (z^2 - 1)^{1/2}$ maps the sheet $R_0$ into $|w| \ge 1$, the sheet $R_1$ into $|w| \le 1$, and the cut onto the circle $|w| = 1$ (the upper edge of the slit in $R_0$ at $x$ goes to $x + i\sqrt{1 - x^2}$, the lower edge to $x - i\sqrt{1 - x^2}$). It maps $R_0$ **onto** $|w| \ge 1$: given $|w| > 1$, put $z = \frac12(w + 1/w)$. The numbers $g_0(z)$, $g_1(z)$ are the roots of $t^2 - 2zt + 1 = 0$ (their sum is $2z$ and product $1$), and so are $w$, $1/w$; the root of modulus $> 1$ is $g_0(z) = w$. Likewise $R_1$ goes onto $|w| \le 1$. So $w = z + (z^2 - 1)^{1/2}$ is an inverse of the transformation
>
> $$
> z = \frac12\Big(w + \frac1w\Big) ,
> $$
>
> half of the map of [[§98★ Mappings by 1∕z#^ex-98-4|Example §98.4]]: that map takes circles $|w| = \rho_0 \ne 1$ onto ellipses with foci $\pm1$ (after the factor $\frac12$), and the surface of Example §111.1 is exactly what is needed to invert it on both sides of the unit circle.
>
> *B&C: Sec. 111, Exercises 4 and 5*

^ex-111-5
