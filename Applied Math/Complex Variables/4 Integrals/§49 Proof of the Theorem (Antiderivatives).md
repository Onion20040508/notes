---
type: section
subject: "[[Complex Variables]]"
chapter: 4
section: 49
bc: "49"
aliases: ["B&C 49"]
tags: [complex-variables, math342]
---
← [[§48 Antiderivatives]] · ↑ [[· 4 Integrals]] · [[§50 Cauchy–Goursat Theorem]] →

*Brown–Churchill, Section 49 · MAT 342 HW 5, HW 6.*

This section proves the theorem on antiderivatives stated in [[§48 Antiderivatives|§48]]: for a continuous function on a domain, having an antiderivative, having path-independent integrals, and having zero integrals around closed contours are equivalent. The proof runs around the cycle (a) $\Rightarrow$ (b) $\Rightarrow$ (c) $\Rightarrow$ (a). The first step is the fundamental theorem of calculus carried along a contour by the chain rule; the second is bookkeeping with sums of contours; the third builds the antiderivative as $F(z) = \int_{z_0}^{z} f(s)\,ds$ and differentiates it with the ML-inequality. That last construction reappears whenever the course needs an antiderivative that no formula provides, for instance on simply connected domains ([[§52 Simply Connected Domains#^cor-52-2|Corollary §52.2]]) and in Morera's theorem ([[§57 Some Consequences of the Extension#^thm-57-3|Theorem §57.3]]).

## The Theorem and Its Proof

> [!remark] Remark: The Plan of the Proof
> It is sufficient to show that (a) implies (b), that (b) implies (c), and that (c) implies (a); then, as noted in [[§48 Antiderivatives|§48]], either the statements are all true or none of them is. In (b), "namely $F(z_2) - F(z_1)$" refers to an antiderivative that exists by (a); in the step (c) $\Rightarrow$ (a) the antiderivative is constructed, and then (b) holds with it. The course covered (a) $\Rightarrow$ (b) $\Rightarrow$ (c) first; (c) $\Rightarrow$ (a) needs the ML-inequality of [[§47 Upper Bounds for Moduli of Contour Integrals#^thm-47-2|§47]].

^rem-49-1

> [!theorem] Theorem §49.1: Antiderivatives and Independence of Path
> Suppose that a function $f(z)$ is continuous in a domain $D$. If any one of the following statements is true, then so are the others:
>
> **(a)** $f(z)$ has an antiderivative $F(z)$ throughout $D$;
>
> **(b)** the integrals of $f(z)$ along contours lying entirely in $D$ and extending from any fixed point $z_1$ to any fixed point $z_2$ all have the same value, namely
>
> $$
> \int_{z_1}^{z_2} f(z)\,dz = F(z)\Big]_{z_1}^{z_2} = F(z_2) - F(z_1) ,
> $$
>
> where $F(z)$ is the antiderivative in statement (a);
>
> **(c)** the integrals of $f(z)$ around closed contours lying entirely in $D$ all have value zero.
>
> *B&C: Sec. 48, Theorem (proved in Sec. 49)*

^thm-49-1

> [!proof]- Proof
> **(a) implies (b).** Assume that $f(z)$ has an antiderivative $F(z)$ on $D$. Let $C$ be a contour from $z_1$ to $z_2$ lying in $D$.
>
> *First let $C$ be a smooth arc,* $z = z(t)$ $(a \le t \le b)$. Since $F$ is analytic at each point $z(t)$, the chain rule along an arc ([[§43 Contours#^prop-43-5|Proposition §43.5]]) gives
>
> $$
> \frac{d}{dt}F[z(t)] = F'[z(t)]\,z'(t) = f[z(t)]\,z'(t) \qquad (a \le t \le b) .
> $$
>
> The right side is continuous, since $f$ and $z'$ are. Because the fundamental theorem of calculus extends to complex-valued functions of a real variable ([[§42 Definite Integrals of Functions w(t)#^thm-42-2|Theorem §42.2]]), it follows that
>
> $$
> \int_C f(z)\,dz = \int_a^b f[z(t)]\,z'(t)\,dt = F[z(t)]\Big]_a^b = F[z(b)] - F[z(a)] .
> $$
>
> Since $z(b) = z_2$ and $z(a) = z_1$, the value of this contour integral is $F(z_2) - F(z_1)$, which is evidently independent of the contour $C$ as long as $C$ extends from $z_1$ to $z_2$ and lies entirely in $D$. That is,
>
> $$
> \int_{z_1}^{z_2} f(z)\,dz = F(z_2) - F(z_1) = F(z)\Big]_{z_1}^{z_2} \qquad (1)
> $$
>
> when $C$ is smooth.
>
> *Now let $C$ be any contour* in $D$, consisting of smooth arcs $C_k$ $(k = 1, 2, \ldots, n)$, each $C_k$ extending from a point $z_k$ to a point $z_{k+1}$ (so $z_{n+1} = z_2$). By property (7) of [[§44 Contour Integrals#^thm-44-2|Theorem §44.2]] and the smooth case,
>
> $$
> \int_C f(z)\,dz = \sum_{k=1}^{n}\int_{C_k} f(z)\,dz = \sum_{k=1}^{n}\int_{z_k}^{z_{k+1}} f(z)\,dz = \sum_{k=1}^{n}\big[F(z_{k+1}) - F(z_k)\big] .
> $$
>
> The last sum telescopes to $F(z_{n+1}) - F(z_1)$, and (1) holds for every contour in $D$. (Compare [[§45 Some Examples (Contour Integrals)#^ex-45-2|Example §45.2]].)
>
> **(b) implies (c).** Assume that integration of $f$ is independent of path in $D$. Let $C$ be a closed contour lying in $D$, $z = z(t)$ $(a \le t \le b)$ with $z(a) = z(b) = z_1$, and choose a parameter value $c$, $a < c < b$, with $z_2 = z(c)$. Let $C_1$ be the part of $C$ from $z_1$ to $z_2$ ($a \le t \le c$), and $C_2$ the reverse of the remaining part, so that $C_2$ also has initial point $z_1$ and final point $z_2$ and $C = C_1 - C_2$. By independence of path,
>
> $$
> \int_{C_1} f(z)\,dz = \int_{C_2} f(z)\,dz , \qquad (2)
> $$
>
> or, by property (6) of [[§44 Contour Integrals#^thm-44-2|Theorem §44.2]],
>
> $$
> \int_{C_1} f(z)\,dz + \int_{-C_2} f(z)\,dz = 0 . \qquad (3)
> $$
>
> By property (7), the left side is the integral of $f$ around $C = C_1 - C_2$, which therefore has value zero.
>
> **(c) implies (a).** Assume that the integrals of $f$ around closed contours in $D$ always have value zero.
>
> *Independence of path.* Let $C_1$ and $C_2$ be any two contours in $D$ from a point $z_1$ to a point $z_2$. Then $C_1 - C_2$ is a closed contour in $D$, so by (c) and properties (6)–(7) equation (3) holds, and hence (2) holds. Integration is therefore independent of path in $D$.
>
> *Definition of $F$.* Fix a point $z_0$ in $D$. Since $D$ is a domain, every point $z$ of $D$ can be joined to $z_0$ by a polygonal line lying in $D$ ([[§12★ Regions in the Complex Plane#^def-12-4|Definition §12.4]], connected open sets), and a polygonal line is a contour. (B&C uses this without comment.) So we can define
>
> $$
> F(z) = \int_{z_0}^{z} f(s)\,ds \qquad (z \in D) ,
> $$
>
> the integral along any contour in $D$ from $z_0$ to $z$; by independence of path the value does not depend on the contour chosen.
>
> *$F'(z) = f(z)$.* Fix $z$ in $D$. Since $D$ is open, some disk $|s - z| < \rho$ lies in $D$. Let $z + \Delta z$ be any point of that disk distinct from $z$. A contour from $z_0$ to $z$ followed by the line segment from $z$ to $z + \Delta z$ (which lies in the disk) is a contour in $D$ from $z_0$ to $z + \Delta z$, so by property (7)
>
> $$
> F(z + \Delta z) - F(z) = \int_{z_0}^{z + \Delta z} f(s)\,ds - \int_{z_0}^{z} f(s)\,ds = \int_z^{z + \Delta z} f(s)\,ds ,
> $$
>
> where the path of integration in the last integral is the line segment. Since $\int_z^{z + \Delta z} ds = \Delta z$ ([[§45 Some Examples (Contour Integrals)#^prop-45-1|Proposition §45.1]]), we can write
>
> $$
> f(z) = \frac{1}{\Delta z}\int_z^{z + \Delta z} f(z)\,ds ,
> $$
>
> the value $f(z)$ being a constant with respect to $s$; and it follows, by property (5), that
>
> $$
> \frac{F(z + \Delta z) - F(z)}{\Delta z} - f(z) = \frac{1}{\Delta z}\int_z^{z + \Delta z}\big[f(s) - f(z)\big]\,ds .
> $$
>
> But $f$ is continuous at the point $z$. Hence, for each positive number $\varepsilon$, a positive number $\delta$ exists such that
>
> $$
> |f(s) - f(z)| < \varepsilon \qquad\text{whenever}\qquad |s - z| < \delta .
> $$
>
> Consequently, if $0 < |\Delta z| < \min(\delta, \rho)$, every point $s$ of the segment satisfies $|s - z| \le |\Delta z| < \delta$, and the ML-inequality ([[§47 Upper Bounds for Moduli of Contour Integrals#^thm-47-2|Theorem §47.2]]), with $M = \varepsilon$ and $L = |\Delta z|$, the length of the segment, gives
>
> $$
> \Big|\frac{F(z + \Delta z) - F(z)}{\Delta z} - f(z)\Big| \le \frac{1}{|\Delta z|}\,\varepsilon|\Delta z| = \varepsilon .
> $$
>
> (B&C writes $<$; the strict form of [[§47 Upper Bounds for Moduli of Contour Integrals#^thm-47-2|Theorem §47.2]] gives that too, but $\le$ is all that is needed.) That is,
>
> $$
> \lim_{\Delta z\to0}\frac{F(z + \Delta z) - F(z)}{\Delta z} = f(z) ,
> $$
>
> or $F'(z) = f(z)$. Since $z$ was arbitrary, $F$ is an antiderivative of $f$ throughout $D$.

^pf-49-1

*Uses:* [[§43 Contours#^prop-43-5|§43.5]] (chain rule along an arc), [[§42 Definite Integrals of Functions w(t)#^thm-42-2|§42.2]] (fundamental theorem for $w(t)$), [[§44 Contour Integrals#^thm-44-2|§44.2]] (properties (5)–(7)), [[§44 Contour Integrals#^def-44-2|Def. §44.2]], [[§44 Contour Integrals#^def-44-new1|Def. §44.3]], [[§45 Some Examples (Contour Integrals)#^prop-45-1|§45.1]], [[§47 Upper Bounds for Moduli of Contour Integrals#^thm-47-2|§47.2]] (ML-inequality), [[§48 Antiderivatives#^def-48-1|Def. §48.1]], [[§48 Antiderivatives#^def-48-2|Def. §48.2]], [[§12★ Regions in the Complex Plane#^def-12-4|Def. §12.4]] (domains are polygonally connected)

![[m342-49-1.svg]]
*The construction in (c) $\Rightarrow$ (a). $F(z)$ is the integral from the base point $z_0$ to $z$ along any contour in $D$ (by (c), the choice does not matter). To differentiate at $z$, continue the contour by the short segment from $z$ to $z + \Delta z$ inside a disk about $z$ contained in $D$. Only the segment depends on $\Delta z$, and on it $f(s)$ is within $\varepsilon$ of $f(z)$, so the ML-inequality gives $\big|[F(z + \Delta z) - F(z)]/\Delta z - f(z)\big| \le \varepsilon$.*

> [!remark]- Connections
> - This is the complex form of [[§109 The Fundamental Theorem for Line Integrals#^thm-109-2|Calc Thm. §109.2]] (path independence $\Leftrightarrow$ zero around closed paths) and [[§109 The Fundamental Theorem for Line Integrals#^thm-109-3|Calc Thm. §109.3]] (path independence $\Rightarrow$ a potential exists, constructed by the same integral from a base point). Here a single complex derivative $F' = f$ replaces the two conditions $\phi_x = P$, $\phi_y = Q$, because $F' = f$ along both a horizontal and a vertical segment are the same statement.
> - The polygonal connectedness used to define $F$ is path-connectedness, [[§14 Connected Subspaces of ℝ#^def-14-3|590 Def. §14.3]]; for open subsets of the plane it is equivalent to connectedness.

> [!remark] Remark: Using the Theorem Backwards
> The implication (a) $\Rightarrow$ (c), read in reverse, proves that antiderivatives do *not* exist.
> - $f(z) = 1/z$ is continuous in the domain $|z| > 0$, but its integral around the unit circle is $2\pi i \ne 0$ ([[§45 Some Examples (Contour Integrals)#^ex-45-1|Example §45.1]]). So $1/z$ has no antiderivative throughout $|z| > 0$; in particular no branch of $\log z$ can be analytic in the whole punctured plane, which is why every branch needs a cut ([[§33 Branches and Derivatives of Logarithms#^def-33-3|Definition §33.3]]). The same holds in every domain containing a circle about $0$.
> - $f(z) = \bar z$ has $\int_{|z|=1}\bar z\,dz = 2\pi i$ ([[§44 Contour Integrals#^ex-44-2|Example §44.2]]), so it has no antiderivative in any domain containing the unit circle (consistent with $\bar z$ being nowhere analytic, while an antiderivative's derivative would be analytic, [[§57 Some Consequences of the Extension#^thm-57-1|Theorem §57.1]]).
> - The function of [[§45 Some Examples (Contour Integrals)#^ex-45-3|Example §45.3]] has different integrals along two paths with the same endpoints, so it has no antiderivative in any domain containing them.

^rem-49-2

## Examples

> [!example] Example §49.1: Powers of z − z₀ Around Closed Contours
> **(a)** Show that $\displaystyle\int_{C_0}(z - z_0)^{n-1}\,dz = 0$ $(n = \pm1, \pm2, \ldots)$ when $C_0$ is any closed contour that does not pass through $z_0$.
>
> For $n \ne 0$, the function $F(z) = (z - z_0)^n/n$ satisfies $F'(z) = (z - z_0)^{n-1}$ in the domain $z \ne z_0$ (the whole plane if $n > 0$). $C_0$ lies in that domain, so by statement (c) of Theorem §49.1 the integral is zero. (For a circle about $z_0$ this is [[§45 Some Examples (Contour Integrals)#^ex-45-5|Example §45.5]]; now the contour can be any closed contour.) The case $n = 0$, the integrand $1/(z - z_0)$, is excluded: its integral around a circle about $z_0$ is $2\pi i$.
>
> **(b)** For the circle $S$: $|z| = 2$, compute $\displaystyle\int_S (z - 3)^n\,dz$ for every integer $n$, and compare with [[§45 Some Examples (Contour Integrals)#^ex-45-5|Example §45.5]].
>
> For $n \ne -1$, part (a) (with $z_0 = 3$, which is not on $S$) gives $0$. For $n = -1$, the integrand $1/(z - 3)$ has the antiderivative
>
> $$
> F(z) = \log(z - 3) = \ln|z - 3| + i\arg(z - 3) \qquad (0 < \arg(z - 3) < 2\pi) ,
> $$
>
> analytic in the plane cut along the ray $z = 3 + x$, $x \ge 0$ ([[§33 Branches and Derivatives of Logarithms#^thm-33-1|Theorem §33.1]] and the chain rule). That ray lies in $|z| \ge 3$, so it misses $S$, and the integral is $0$ by statement (c). So $\int_S (z - 3)^n\,dz = 0$ for *every* $n$. In [[§45 Some Examples (Contour Integrals)#^ex-45-5|Example §45.5]] the case $n = -1$ gave $2\pi i$: there the point $a$ where $1/(z - a)$ fails to be analytic lies *inside* the circle, so every branch of $\log(z - a)$ has its cut crossing the circle; here the point $3$ lies outside $S$, and a cut from $3$ can avoid $S$.
>
> *B&C: Sec. 49, Exercise 3; Source: 342 HW 6; 342 HW 5, Problem 2(b)*

^ex-49-1

> [!example] Example §49.2: Antiderivatives Instead of Parametrizations
> Find antiderivatives and compute the following integrals over the given paths, without parametrizing.
>
> **(a)** $\displaystyle\int_C \cos\Big(\frac z2\Big)\,dz$, where $C = \{te^{it} : 2\pi \le t \le 4\pi\}$, a spiral arc from $z_1 = 2\pi e^{2\pi i} = 2\pi$ to $z_2 = 4\pi e^{4\pi i} = 4\pi$.
>
> $F(z) = 2\sin(z/2)$ is an antiderivative in the whole plane, so
>
> $$
> \int_C \cos\Big(\frac z2\Big)\,dz = 2\sin\frac{z}{2}\bigg]_{2\pi}^{4\pi} = 2\sin 2\pi - 2\sin\pi = 0 .
> $$
>
> **(b)** $\displaystyle\int_C \frac{z}{2z^2 - 1}\,dz$, where $C$ is formed by the segments $\{x = 0, 0 \le y \le 1\}$, $\{0 \le x \le 2, y = 1\}$, $\{x = 2, 0 \le y \le 1\}$, taken in this order: from $0$ up to $i$, across to $2 + i$, down to $2$.
>
> A formal antiderivative is $\frac14\log(2z^2 - 1)$, since $\frac{d}{dz}(2z^2 - 1) = 4z$. A branch of $\log$ must be chosen whose cut misses the image of $C$ under $w = 2z^2 - 1$:
> - on $z = iy$ $(0 \le y \le 1)$: $w = -2y^2 - 1$, which runs along the *negative real axis* from $-1$ to $-3$, so the principal branch $\operatorname{Log}$ will not do;
> - on $z = x + i$ $(0 \le x \le 2)$: $w = 2x^2 - 3 + 4xi$, with $\operatorname{Im} w = 4x \ge 0$, from $-3$ to $5 + 8i$;
> - on $z = 2 + iy$, $y$ from $1$ to $0$: $w = 7 - 2y^2 + 8yi$, with $\operatorname{Im} w = 8y \ge 0$, from $5 + 8i$ to $7$.
>
> So $w(C)$ lies in the closed upper half-plane and avoids $w = 0$. Take the branch $\log w = \ln|w| + i\Theta$ with $-\frac\pi2 < \Theta < \frac{3\pi}{2}$, cut along the negative imaginary axis. Then $G(z) = \frac14\log(2z^2 - 1)$ is analytic, with $G'(z) = \frac14\cdot\frac{4z}{2z^2 - 1} = \frac{z}{2z^2 - 1}$, on the open set of $z$ with $2z^2 - 1$ off the cut; the connected piece of that set containing $C$ is a domain in which $G$ is an antiderivative. By statement (b),
>
> $$
> \int_C \frac{z\,dz}{2z^2 - 1} = G(2) - G(0) = \frac14\big[\log 7 - \log(-1)\big] = \frac14\big(\ln 7 - i\pi\big) \approx 0.4865 - 0.7854i ,
> $$
>
> using $\log(-1) = i\pi$ in this branch. (Numerical quadrature along the three segments confirms the value.) The singular points $z = \pm1/\sqrt2$ of the integrand lie on the real axis, below the path; a path from $0$ to $2$ passing on the other side of $1/\sqrt2$ would give a different value.
>
> *Source: 342 HW 6, Problem 1*

^ex-49-2

> [!example] Example §49.3: The Principal Branch of zⁱ from −1 to 1
> Show that
>
> $$
> \int_{-1}^{1} z^i\,dz = \frac{1 + e^{-\pi}}{2}(1 - i) ,
> $$
>
> where the integrand is the principal branch $z^i = \exp(i\operatorname{Log} z)$ $(|z| > 0, -\pi < \operatorname{Arg} z < \pi)$ and the path is any contour from $-1$ to $1$ that, except for its end points, lies above the real axis.
>
> The principal branch is not defined at $-1$. As in [[§48 Antiderivatives#^ex-48-4|Example §48.4]], replace it by the branch $z^i = \exp(i\log z)$ with $-\frac\pi2 < \arg z < \frac{3\pi}{2}$, which agrees with it on the upper half-plane and at $z = 1$, and is continuous at $-1$ (with $\arg(-1) = \pi$). An antiderivative of this branch in its domain is $z^{i+1}/(i + 1) = \exp\big((1 + i)\log z\big)/(1 + i)$ ([[§35 The Power Function#^thm-35-2|Theorem §35.2]]). With $\log 1 = 0$ and $\log(-1) = i\pi$,
>
> $$
> \int_{-1}^{1} z^i\,dz = \frac{1 - e^{(1+i)i\pi}}{1 + i} = \frac{1 - e^{-\pi}e^{i\pi}}{1 + i} = \frac{1 + e^{-\pi}}{1 + i} = \frac{1 + e^{-\pi}}{2}(1 - i) \approx 0.5216(1 - i) .
> $$
>
> B&C's Exercise 6 in Sec. 46 integrates the same branch by parametrization along the upper unit semicircle from $1$ to $-1$ and gets the negative, $-\frac{1 + e^{-\pi}}{2}(1 - i)$, as path independence requires.
>
> *B&C: Sec. 49, Exercise 5*

^ex-49-3
