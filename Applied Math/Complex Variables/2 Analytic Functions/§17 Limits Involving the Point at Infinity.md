---
type: section
subject: "[[Complex Variables]]"
chapter: 2
section: 17
bc: "17"
aliases: ["B&C 17"]
tags: [complex-variables, math342]
---
← [[§16 Theorems on Limits]] · ↑ [[· 2 Analytic Functions]] · [[§18 Continuity]] →

*Brown–Churchill, Section 17 · MAT 342 HW 2.*

Adding a single point $\infty$ to the complex plane makes statements such as "$1/z$ becomes large near $0$" and "$(2z + i)/(z + 1)$ settles down to $2$ far out" into ordinary limit statements. The extended plane is pictured as a sphere through stereographic projection, on which $\infty$ is the north pole and its neighborhoods are the exteriors of large circles. The theorem of this section reduces every limit involving $\infty$ to a limit at a finite point, by replacing $f$ with $1/f$ or $z$ with $1/z$. The point at infinity returns as an isolated singular point in [[§74 Isolated Singular Points#^def-74-2|Definition §74.2]] and [[§77★ Residue at Infinity|§77★]], and it is essential for linear fractional transformations ([[§99★ Linear Fractional Transformations#^thm-99-4|Theorem §99.4]]), which map the extended plane one to one onto itself.

## The Extended Plane and the Riemann Sphere

> [!definition] Definition §17.1: Extended Complex Plane
> The **point at infinity**, denoted $\infty$, is a point adjoined to the complex plane; the complex plane together with this point is the **extended complex plane**.
>
> *B&C: Sec. 17 (text)*

^def-17-1

> [!definition] Definition §17.3: Riemann Sphere
> To visualize the extended complex plane, think of the complex plane as passing through the equator of a unit sphere centered at the origin. To each point $z$ of the plane there corresponds exactly one point $P$ on the sphere: the point where the line through $z$ and the north pole $N$ meets the sphere. In like manner, to each point $P$ of the sphere other than $N$ there corresponds exactly one point $z$ of the plane. Letting $N$ correspond to the point at infinity gives a one to one correspondence between the points of the sphere and the points of the extended complex plane. The sphere is the **Riemann sphere**, and the correspondence is **stereographic projection**.
>
> *B&C: Sec. 17 (text)*

^def-17-2

> [!definition] Definition §17.4: Neighborhood of Infinity
> For each small positive number $\varepsilon$, the set $|z| > 1/\varepsilon$ is a **neighborhood of $\infty$**.
>
> Hereafter "a point $z$" means a point of the finite plane; when the point at infinity is to be considered, it is mentioned specifically.
>
> *B&C: Sec. 17 (text)*

^def-17-3

The name is justified by the sphere: the exterior $|z| > 1$ of the unit circle corresponds to the upper hemisphere with the equator and $N$ deleted, and the points exterior to the circle $|z| = 1/\varepsilon$ correspond to the points of the sphere close to $N$. (B&C states this; here is the computation.)

> [!remark] Remark: Coordinates of the Stereographic Projection
> Put the sphere $\xi^2 + \eta^2 + \zeta^2 = 1$ in $(\xi, \eta, \zeta)$-space with the $z$ plane as the plane $\zeta = 0$ and $N = (0, 0, 1)$. The line from $N$ through $z = x + iy = (x, y, 0)$ consists of the points $(tx, ty, 1 - t)$, and it meets the sphere where $t^2|z|^2 + (1 - t)^2 = 1$, that is, $t\big(t(|z|^2 + 1) - 2\big) = 0$. The root $t = 0$ is $N$; the other, $t = 2/(|z|^2 + 1)$, gives
>
> $$
> P = \Big(\frac{2x}{|z|^2 + 1},\ \frac{2y}{|z|^2 + 1},\ \frac{|z|^2 - 1}{|z|^2 + 1}\Big), \qquad |P - N| = \frac{2}{\sqrt{|z|^2 + 1}} .
> $$
>
> So $P$ is in the upper hemisphere ($\zeta > 0$) exactly when $|z| > 1$, on the equator when $|z| = 1$, and $|P - N| \to 0$ exactly as $|z| \to \infty$. The neighborhood $|z| > 1/\varepsilon$ of $\infty$ corresponds to the cap $|P - N| < 2\varepsilon/\sqrt{1 + \varepsilon^2}$ around $N$: a neighborhood of $N$ on the sphere.

^rem-17-1

![[m342-17-1.svg]]
*A vertical cross-section of the Riemann sphere through $N$ and the origin. The line from $N$ through a point $z$ of the plane meets the sphere again at $P$: points outside the unit circle ($z$, red) go to the upper hemisphere, points inside ($z'$, blue) to the lower one. The neighborhood $|z| > 1/\varepsilon$ of $\infty$ (orange, on the plane) corresponds to the orange cap around $N$.*

> [!remark]- Connections
> - The extended plane is the one-point compactification of $\mathbb{C} = \mathbb{R}^2$, [[§20 Local Compactness#^def-20-3|590 Def. §20.3]], and stereographic projection is the homeomorphism with $S^2$ of [[§20 Local Compactness#^ex-20-7|590 Ex. §20.7]]. There the neighborhoods of $\infty$ are the complements of compact sets. Every compact $C \subseteq \mathbb{C}$ is bounded, hence inside some disk $|z| \le 1/\varepsilon$, so B&C's neighborhoods $|z| > 1/\varepsilon$ form a base for the same topology at $\infty$.

## Limits Involving the Point at Infinity

A meaning is given to $\lim_{z\to z_0} f(z) = w_0$ when $z_0$, or $w_0$, or both, is replaced by $\infty$: in the definition of limit ([[§15 Limits#^def-15-1|Definition §15.1]]) one simply replaces the appropriate neighborhoods of $z_0$ and $w_0$ by neighborhoods of $\infty$.

> [!definition] Definition §17.4: Limits Involving ∞
> Let $z_0$ and $w_0$ be points of the (finite) $z$ and $w$ planes.
> - $\displaystyle\lim_{z\to z_0} f(z) = \infty$ means: for each $\varepsilon > 0$ there is $\delta > 0$ such that $|f(z)| > \dfrac1\varepsilon$ whenever $0 < |z - z_0| < \delta$.
> - $\displaystyle\lim_{z\to\infty} f(z) = w_0$ means: for each $\varepsilon > 0$ there is $\delta > 0$ such that $|f(z) - w_0| < \varepsilon$ whenever $|z| > \dfrac1\delta$.
> - $\displaystyle\lim_{z\to\infty} f(z) = \infty$ means: for each $\varepsilon > 0$ there is $\delta > 0$ such that $|f(z)| > \dfrac1\varepsilon$ whenever $|z| > \dfrac1\delta$.
>
> In the last two, $f$ is assumed defined in some neighborhood of $\infty$.
>
> *B&C: Sec. 17 (text), statements (4), (5) and (6)*

^def-17-4

> [!theorem] Theorem §17.1: Reduction to Finite Limits
> If $z_0$ and $w_0$ are points in the $z$ and $w$ planes, respectively, then
>
> $$
> \lim_{z\to z_0} f(z) = \infty \qquad\text{if and only if}\qquad \lim_{z\to z_0}\frac{1}{f(z)} = 0 , \qquad (1)
> $$
>
> $$
> \lim_{z\to\infty} f(z) = w_0 \qquad\text{if and only if}\qquad \lim_{z\to0} f\Big(\frac1z\Big) = w_0 . \qquad (2)
> $$
>
> Moreover,
>
> $$
> \lim_{z\to\infty} f(z) = \infty \qquad\text{if and only if}\qquad \lim_{z\to0}\frac{1}{f(1/z)} = 0 . \qquad (3)
> $$
>
> *B&C: Sec. 17, Theorem*

^thm-17-1

B&C states the "if" halves, which are the ones used to compute limits; the proof shows that each step can be reversed.

> [!proof]+ Proof
> **(1).** Suppose the second limit in (1) holds. This means that for each positive number $\varepsilon$ there is a positive number $\delta$ such that
>
> $$
> \Big|\frac{1}{f(z)} - 0\Big| < \varepsilon \qquad\text{whenever}\qquad 0 < |z - z_0| < \delta .
> $$
>
> Since this can be written
>
> $$
> |f(z)| > \frac1\varepsilon \qquad\text{whenever}\qquad 0 < |z - z_0| < \delta , \qquad (4)
> $$
>
> we arrive at the first limit in (1). Conversely, (4) implies $f(z) \ne 0$ in the deleted neighborhood, so $1/f(z)$ is defined there and $|1/f(z)| < \varepsilon$.
>
> **(2).** Suppose the second limit in (2) holds, that is,
>
> $$
> \Big|f\Big(\frac1z\Big) - w_0\Big| < \varepsilon \qquad\text{whenever}\qquad 0 < |z - 0| < \delta .
> $$
>
> Replacing $z$ by $1/z$ (as $z$ runs over $0 < |z| < \delta$, the point $1/z$ runs over exactly $|z| > 1/\delta$), we have
>
> $$
> |f(z) - w_0| < \varepsilon \qquad\text{whenever}\qquad |z| > \frac1\delta , \qquad (5)
> $$
>
> which is the first limit in (2). The same replacement turns (5) back into the second limit.
>
> **(3).** The second limit in (3) means that
>
> $$
> \Big|\frac{1}{f(1/z)} - 0\Big| < \varepsilon \qquad\text{whenever}\qquad 0 < |z - 0| < \delta ;
> $$
>
> and replacing $z$ by $1/z$ in these inequalities gives
>
> $$
> |f(z)| > \frac1\varepsilon \qquad\text{whenever}\qquad |z| > \frac1\delta . \qquad (6)
> $$
>
> This is the definition of the first limit in (3); again every step can be reversed.

^pf-17-1

*Uses:* [[§17 Limits Involving the Point at Infinity#^def-17-4|Def. §17.4]], [[§15 Limits#^def-15-1|Def. §15.1]]

Limits involving $\infty$ are unique, as B&C's Exercise 12 asks one to observe: for $\lim_{z\to\infty} f(z) = w_0$ the proof of [[§15 Limits#^thm-15-1|Theorem §15.1]] goes through with the deleted neighborhoods of $z_0$ replaced by neighborhoods of $\infty$; and $f$ cannot tend both to $\infty$ and to a finite $w_0$, since $|f(z)| > |w_0| + 1$ and $|f(z) - w_0| < 1$ cannot hold at the same point.

> [!example] Example §17.1: Three Limits
> **(a)** $\displaystyle\lim_{z\to-1}\frac{iz + 3}{z + 1} = \infty$, since $\displaystyle\lim_{z\to-1}\frac{z + 1}{iz + 3} = \frac{0}{3 - i} = 0$, by (1).
>
> **(b)** $\displaystyle\lim_{z\to\infty}\frac{2z + i}{z + 1} = 2$, since $\displaystyle\lim_{z\to0}\frac{(2/z) + i}{(1/z) + 1} = \lim_{z\to0}\frac{2 + iz}{1 + z} = 2$, by (2).
>
> **(c)** $\displaystyle\lim_{z\to\infty}\frac{2z^3 - 1}{z^2 + 1} = \infty$, since $\displaystyle\lim_{z\to0}\frac{(1/z^2) + 1}{(2/z^3) - 1} = \lim_{z\to0}\frac{z + z^3}{2 - z^3} = 0$, by (3).
>
> In each case the reduced limit is a limit of a rational function at a point where its denominator is not zero ([[§16 Theorems on Limits#^cor-16-3|Corollary §16.3]]); the middle step multiplies numerator and denominator by $z$ in (b) and by $z^3$ in (c).
>
> *B&C: Sec. 17, Examples*

^ex-17-1

> [!example] Example §17.2: Two Limits at Infinity
> **(a)** Show that $\displaystyle\lim_{z\to\infty}\frac{4z^2}{(z - 1)^2} = 4$. By (2), consider
>
> $$
> f\Big(\frac1z\Big) = \frac{4/z^2}{(1/z - 1)^2} = \frac{4}{z^2(1/z - 1)^2} = \frac{4}{(1 - z)^2} \qquad (z \ne 0,\ z \ne 1) .
> $$
>
> As $z \to 0$, $(1 - z)^2 \to 1$, so $f(1/z) \to 4$. Hence the limit is $4$.
>
> **(b)** Show that $\displaystyle\lim_{z\to\infty}\frac{z^2 + 1}{z - 1} = \infty$. By (3), consider
>
> $$
> \frac{1}{f(1/z)} = \frac{1/z - 1}{1/z^2 + 1} = \frac{z - z^2}{1 + z^2} \qquad (\text{multiplying by } z^2) .
> $$
>
> As $z \to 0$ this tends to $0/1 = 0$. Hence the limit is $\infty$.
>
> *B&C: Sec. 18, Exercise 10(a), (c); Source: 342 HW 2*

^ex-17-2

The next consequence is used for linear fractional transformations in [[§99★ Linear Fractional Transformations#^thm-99-4|Theorem §99.4]], to make them continuous on the extended plane.

> [!theorem] Proposition §17.2: Limits of a Linear Fractional Transformation
> Let
>
> $$
> T(z) = \frac{az + b}{cz + d} \qquad (ad - bc \ne 0) .
> $$
>
> 1. If $c = 0$, then $\displaystyle\lim_{z\to\infty} T(z) = \infty$.
> 2. If $c \ne 0$, then $\displaystyle\lim_{z\to\infty} T(z) = \frac ac$ and $\displaystyle\lim_{z\to-d/c} T(z) = \infty$.
>
> *B&C: Sec. 18, Exercise 11*

^prop-17-2

> [!proof]+ Proof
> **1.** If $c = 0$, then $ad \ne 0$, so $a \ne 0$ and $d \ne 0$, and $T(z) = (az + b)/d$ is defined for all $z$. For $z \ne 0$,
>
> $$
> \frac{1}{T(1/z)} = \frac{d}{a/z + b} = \frac{dz}{a + bz} \quad\longrightarrow\quad \frac{0}{a} = 0 \qquad (z \to 0) ,
> $$
>
> by [[§16 Theorems on Limits#^cor-16-3|Corollary §16.3]] (the denominator tends to $a \ne 0$). By (3), $T(z) \to \infty$ as $z \to \infty$.
>
> **2.** Let $c \ne 0$. *At infinity:* for $z \ne 0$ near $0$,
>
> $$
> T\Big(\frac1z\Big) = \frac{a/z + b}{c/z + d} = \frac{a + bz}{c + dz} \quad\longrightarrow\quad \frac ac \qquad (z \to 0) ,
> $$
>
> since the denominator tends to $c \ne 0$; by (2), $T(z) \to a/c$ as $z \to \infty$. *At $-d/c$:* $T$ is defined for $z \ne -d/c$, and
>
> $$
> \frac{1}{T(z)} = \frac{cz + d}{az + b} \quad\longrightarrow\quad \frac{0}{a(-d/c) + b} = \frac{0}{(bc - ad)/c} = 0 \qquad (z \to -d/c) ,
> $$
>
> because the denominator tends to $(bc - ad)/c \ne 0$. By (1), $T(z) \to \infty$ as $z \to -d/c$.

^pf-17-2

*Uses:* [[§17 Limits Involving the Point at Infinity#^thm-17-1|§17.1]], [[§16 Theorems on Limits#^cor-16-3|§16.3]]

The condition $ad - bc \ne 0$ is what keeps $T$ from being constant: if $ad = bc$, then $az + b$ and $cz + d$ are proportional and $T$ takes a single value wherever it is defined.

> [!example] Example §17.3: Unbounded Sets Reach Every Neighborhood of Infinity
> Show that a set $S$ is unbounded if and only if every neighborhood of the point at infinity contains at least one point of $S$.
>
> By [[§12★ Regions in the Complex Plane#^def-12-12|Definition §12.12]], $S$ is bounded if every point of $S$ lies inside some circle $|z| = R$. So $S$ is unbounded exactly when for every $R > 0$ some point $z \in S$ has $|z| \ge R$.
>
> *If $S$ is unbounded:* given a neighborhood $|z| > 1/\varepsilon$ of $\infty$, apply this with $R = 1/\varepsilon + 1$ to get $z \in S$ with $|z| \ge 1/\varepsilon + 1 > 1/\varepsilon$.
>
> *If every neighborhood of $\infty$ meets $S$:* given $R > 0$, the neighborhood $|z| > R$ (that is, $\varepsilon = 1/R$) contains a point $z$ of $S$, and $|z| > R$. So no circle contains all of $S$, and $S$ is unbounded.
>
> *B&C: Sec. 18, Exercise 13*

^ex-17-3
