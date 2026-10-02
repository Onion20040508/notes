---
type: section
subject: "[[Complex Variables]]"
chapter: 2
section: 28
bc: "28"
aliases: ["B&C 28"]
tags: [complex-variables, math342, extension]
---
← [[§27★ Harmonic Functions]] · ↑ [[· 2 Analytic Functions]] · [[§29★ Reflection Principle]] →

*Brown–Churchill, Section 28.*
★ *Beyond MAT 342: the course skipped this section or left it optional; it is included from Brown–Churchill.*

An analytic function on a domain is far more rigid than a differentiable function of real variables: its values on any small disk, or even on a short line segment, determine it everywhere in the domain. This section proves that fact, using a result on zeros from Ch. 6 ([[§82 Zeros of Analytic Functions#^thm-82-3|Theorem §82.3]]) and a chain of overlapping disks along a polygonal path. It then introduces analytic continuation: extending an analytic function to a larger domain, which can be done in at most one way. B&C notes that these two sections are not central to the later chapters and can be read when needed; the uniqueness theorem is used in the reflection principle ([[§29★ Reflection Principle#^thm-29-1|Theorem §29.1]]) and justifies extending real identities, such as $\sin^2x + \cos^2x = 1$, to complex arguments.

## Uniqueness

> [!theorem] Lemma §28.1: Vanishing on a Subdomain or Segment
> Suppose that
>
> **(a)** a function $f$ is analytic throughout a domain $D$;
>
> **(b)** $f(z) = 0$ at each point $z$ of a domain or line segment contained in $D$.
>
> Then $f(z) \equiv 0$ in $D$; that is, $f(z)$ is identically equal to zero throughout $D$.
>
> *B&C: Sec. 28, Lemma*

^lem-28-1

> [!proof]+ Proof
> Let $f$ be as stated and let $z_0$ be any point of the subdomain or line segment where $f(z) = 0$. Let $P$ be any other point of $D$.
>
> **A polygonal line and a radius.** Since $D$ is a connected open set ([[§12★ Regions in the Complex Plane#^def-12-4|Definition §12.4]]), there is a polygonal line $L$, consisting of a finite number of line segments joined end to end and lying entirely in $D$, that extends from $z_0$ to $P$. Let $d$ be the shortest distance from points on $L$ to the boundary of $D$, unless $D$ is the entire plane; in that case $d$ may be any positive number. (B&C takes for granted that $d > 0$; here is why. $L$ is closed and bounded, and the boundary of $D$ is a closed set disjoint from $L$, because $L \subset D$ and $D$ is open. The distance from a point $z$ to the boundary is a continuous function of $z$, positive on $L$, so it attains a positive minimum on $L$.)
>
> **The disks lie in $D$.** If $z \in L$ and $|w - z| < d$, then $w \in D$. Otherwise the segment from $z$ (in $D$) to $w$ (not in $D$) would contain a boundary point of $D$: the last point $z + t^*(w - z)$, $t^* = \sup\{t \in [0, 1] : z + s(w - z) \in D \text{ for } 0 \le s \le t\}$, is a limit of points of $D$ and is not in the open set $D$ (else $t^*$ could be increased, or $t^* = 1$ and $w \in D$). That boundary point would be at distance less than $d$ from $z \in L$, contradicting the choice of $d$.
>
> **A chain of neighborhoods.** Form a finite sequence of points
>
> $$
> z_0, z_1, z_2, \ldots, z_{n-1}, z_n
> $$
>
> along $L$, where the point $z_n$ coincides with $P$ and where each point is sufficiently close to the adjacent ones that
>
> $$
> |z_k - z_{k-1}| < d \qquad (k = 1, 2, \ldots, n)
> $$
>
> (possible because $L$ has finite length: divide each of its segments into pieces of length less than $d$). Let $N_k$ be the neighborhood of radius $d$ centered at $z_k$ ($k = 0, 1, \ldots, n$). By the previous step these neighborhoods are all contained in $D$, and the center $z_k$ of each $N_k$ ($k = 1, \ldots, n$) lies in the preceding neighborhood $N_{k-1}$.
>
> **Propagation.** By [[§82 Zeros of Analytic Functions#^thm-82-3|Theorem §82.3]], proved in Ch. 6 without using this section: *if $f$ is analytic throughout a neighborhood $N_0$ of $z_0$ and $f(z) = 0$ at each point of a domain or line segment containing $z_0$, then $f(z) \equiv 0$ in $N_0$.* So $f \equiv 0$ in $N_0$. But the point $z_1$ lies in $N_0$, so $f = 0$ on the domain $N_0$, which contains $z_1$; and $f$ is analytic in $N_1 \subset D$. A second application of the same theorem gives $f \equiv 0$ in $N_1$. Continuing in this manner, we arrive at $f \equiv 0$ in $N_n$. Since $N_n$ is centered at $P$, $f(P) = 0$, and since $P$ was arbitrary, $f \equiv 0$ in $D$.

^pf-28-1

*Uses:* [[§12★ Regions in the Complex Plane#^def-12-4|Def. §12.4]], [[§82 Zeros of Analytic Functions#^thm-82-3|§82.3]], [[§18 Properties of Continuous Functions#^thm-18-1|451 Thm. §18.1]] (extreme value theorem, applied on the segments of $L$)

![[m342-28-1.svg]]
*The proof of Lemma §28.1. The function vanishes on a short segment through $z_0$ (green). A polygonal line $L$ (blue) joins $z_0$ to $P$ inside $D$; the disks $N_k$ of radius $d$, the distance from $L$ to the boundary, stay inside $D$, and each is centered at a point of the previous one. Theorem §82.3 carries "$f \equiv 0$" from each disk to the next, all the way to $P$.*

> [!remark]- Connections
> - The "$d > 0$" step is the standard fact that a compact set and a disjoint closed set are at positive distance; compactness of $L$ is [[§15 Compact Spaces#^thm-15-12|590 Thm. §15.12]] (Heine–Borel). The propagation step is a connectedness argument in disguise: the set where $f$ vanishes identically nearby is open and closed in $D$, [[§13 Connected Spaces#^def-13-1|590 Def. §13.1]].

Suppose now that two functions $f$ and $g$ are analytic in the same domain $D$ and that $f(z) = g(z)$ at each point $z$ of some domain or line segment contained in $D$. The difference $h(z) = f(z) - g(z)$ is also analytic in $D$, and $h(z) = 0$ throughout the subdomain or along the line segment. According to the lemma, $h(z) \equiv 0$ throughout $D$. We thus arrive at the following important theorem.

> [!theorem] Theorem §28.2: Uniquely Determined Analytic Functions
> A function that is analytic in a domain $D$ is uniquely determined over $D$ by its values in a domain, or along a line segment, contained in $D$.
>
> *B&C: Sec. 28, Theorem*

^thm-28-2

> [!proof]+ Proof
> Let $f$ and $g$ be analytic in $D$ with $f(z) = g(z)$ at each point of a domain or line segment contained in $D$. Then $h = f - g$ is analytic in $D$ ([[§25 Analytic Functions#^prop-25-1|Proposition §25.1]]) and $h(z) = 0$ throughout the subdomain or along the segment. By Lemma §28.1, $h \equiv 0$ in $D$, so $f(z) = g(z)$ at each point of $D$.

^pf-28-2

*Uses:* [[§28★ Uniquely Determined Analytic Functions#^lem-28-1|§28.1]], [[§25 Analytic Functions#^prop-25-1|§25.1]]

A more general result, sometimes called the **coincidence principle**, is straightforward to prove.

> [!theorem] Theorem §28.3: Coincidence Principle
> If two functions $f$ and $g$ are analytic in the same domain $D$ and if $f(z) = g(z)$ on a subset of $D$ that has a limit point $z_0$ in $D$, then $f(z) = g(z)$ everywhere in $D$.
>
> *B&C: Sec. 28 (text)*

^thm-28-3

*B&C omits the proof (it cites Boas, Silverman and Markushevich); it follows from [[§82 Zeros of Analytic Functions#^thm-82-2|Theorem §82.2]], proved in Ch. 6 without using this section: $h = f - g$ vanishes at $z_0$ by continuity and is not nonzero throughout any deleted neighborhood of $z_0$, so $h \equiv 0$ in a neighborhood of $z_0$, and Lemma §28.1 applies.*

## Analytic Continuation

> [!definition] Definition §28.1: Analytic Continuation
> Let $D_1$ and $D_2$ be domains whose intersection $D_1 \cap D_2$, the set of points that lie in both, is not empty, and let $f_1$ be analytic in $D_1$. If there is a function $f_2$, analytic in $D_2$, such that $f_2(z) = f_1(z)$ for each $z$ in $D_1 \cap D_2$, then $f_2$ is called an **analytic continuation** of $f_1$ into the second domain $D_2$.
>
> *B&C: Sec. 28 (text)*

^def-28-1

> [!theorem] Proposition §28.4: Uniqueness and Gluing of Continuations
> Let $f_2$ be an analytic continuation of $f_1$ from a domain $D_1$ into a domain $D_2$.
>
> **(a)** It is unique: not more than one function can be analytic in $D_2$ and assume the value $f_1(z)$ at each point $z$ of $D_1 \cap D_2$.
>
> **(b)** The function
>
> $$
> F(z) = \begin{cases} f_1(z) & \text{when } z \text{ is in } D_1, \\ f_2(z) & \text{when } z \text{ is in } D_2 \end{cases}
> $$
>
> is well defined and analytic in the union $D_1 \cup D_2$, the domain consisting of all points that lie in either $D_1$ or $D_2$.
>
> *B&C: Sec. 28 (text)*

^prop-28-4

> [!proof]+ Proof
> **(a)** If $f_2$ and $g_2$ are both analytic in $D_2$ and both equal $f_1$ on $D_1 \cap D_2$, they agree on that set. It is open and not empty, so it contains a neighborhood of one of its points, a domain contained in $D_2$; by Theorem §28.2, $f_2 = g_2$ throughout $D_2$.
>
> **(b)** On $D_1 \cap D_2$ the two formulas give the same value, so $F$ is well defined. Each point of $D_1 \cup D_2$ has a neighborhood inside $D_1$ or inside $D_2$, on which $F$ coincides with the analytic function $f_1$ or $f_2$; so $F$ has a derivative there. Finally $D_1 \cup D_2$ is open, and connected: two points of $D_1 \cup D_2$ can each be joined by a polygonal line to a common point of $D_1 \cap D_2$, within $D_1$ or $D_2$.

^pf-28-4

*Uses:* [[§28★ Uniquely Determined Analytic Functions#^thm-28-2|§28.2]], [[§28★ Uniquely Determined Analytic Functions#^def-28-1|Def. §28.1]], [[§12★ Regions in the Complex Plane#^def-12-4|Def. §12.4]]

> [!definition] Definition §28.2: Elements
> In Proposition §28.4(b), $F$ is the analytic continuation into $D_1 \cup D_2$ of either $f_1$ or $f_2$, and $f_1$ and $f_2$ are called **elements** of $F$.
>
> *B&C: Sec. 28 (text)*

^def-28-2

However, if there is an analytic continuation $f_3$ of $f_2$ from $D_2$ into a domain $D_3$ that intersects $D_1$, it is *not* necessarily true that $f_3(z) = f_1(z)$ for each $z$ in $D_1 \cap D_3$: continuing along different routes can lead to different functions. Example §28.2 shows this.

## Examples

> [!example] Example §28.1: Constant on a Neighborhood Means Constant
> Show that if $f(z)$ is analytic and not constant throughout a domain $D$, then it cannot be constant throughout any neighborhood lying in $D$.
>
> Suppose $f(z)$ has a constant value $w_0$ throughout some neighborhood $N$ lying in $D$. The constant function $g(z) = w_0$ is analytic in $D$, and $f = g$ on the domain $N$. By Theorem §28.2, $f = g$ throughout $D$, so $f$ is constant in $D$, contrary to the hypothesis.
>
> *B&C: Sec. 29, Exercise 1*

^ex-28-1

> [!example] Example §28.2: Continuing the Square Root Around the Origin
> Start with
>
> $$
> f_1(z) = \sqrt r\,e^{i\theta/2} \qquad (r > 0,\ 0 < \theta < \pi) ,
> $$
>
> analytic in the upper half plane by [[§24★ Polar Coordinates#^ex-24-2|Example §24.2]].
>
> **Across the negative real axis.** The function
>
> $$
> f_2(z) = \sqrt r\,e^{i\theta/2} \qquad \Big(r > 0,\ \frac\pi2 < \theta < 2\pi\Big)
> $$
>
> is analytic in its domain $D_2$ (Example §24.2, restricted to part of the branch with $\alpha = \pi/2$). The intersection $D_1 \cap D_2$ is the second quadrant $\frac\pi2 < \theta < \pi$, where both formulas use the same $\theta$ and so agree. So $f_2$ is an analytic continuation of $f_1$ across the negative real axis into the lower half plane.
>
> **Back into the first quadrant.** The function
>
> $$
> f_3(z) = \sqrt r\,e^{i\theta/2} \qquad \Big(r > 0,\ \pi < \theta < \frac{5\pi}{2}\Big)
> $$
>
> is analytic in its domain $D_3$, and $D_2 \cap D_3$ is the lower half plane $\pi < \theta < 2\pi$, where $f_3 = f_2$. So $f_3$ is an analytic continuation of $f_2$ across the positive real axis into the first quadrant. But a point of the first quadrant has polar angle $\phi \in (0, \frac\pi2)$ for $f_1$ and $\theta = \phi + 2\pi$ for $f_3$, so there
>
> $$
> f_3(z) = \sqrt r\,e^{i(\phi + 2\pi)/2} = e^{i\pi}\sqrt r\,e^{i\phi/2} = -f_1(z) .
> $$
>
> **The direct route.** The function
>
> $$
> f_4(z) = \sqrt r\,e^{i\theta/2} \qquad (r > 0,\ -\pi < \theta < \pi)
> $$
>
> agrees with $f_1$ on the upper half plane, the intersection of their domains, so it is the analytic continuation of $f_1$ across the positive real axis into the lower half plane (unique, by Proposition §28.4). In the lower half plane, $f_4$ uses $\theta \in (-\pi, 0)$ and $f_2$ uses $\theta + 2\pi$, so $f_2 = -f_4$ there. Continuing $f_1$ into the lower half plane clockwise (across the positive real axis) and counterclockwise (across the negative real axis) gives the two different functions $f_4$ and $-f_4$: the square root cannot be continued to a single analytic function on any domain that surrounds the origin.
>
> *B&C: Sec. 29, Exercises 2 and 3*

^ex-28-2

> [!example] Example §28.3: Real Identities Extend to the Plane
> Accepting that $\cosh^2x - \sinh^2x = 1$ and $\sinh x + \cosh x = e^x$ for real $x$, show that
>
> $$
> \cosh^2z - \sinh^2z = 1 \qquad\text{and}\qquad \sinh z + \cosh z = e^z \qquad\text{for all complex } z .
> $$
>
> The functions $e^z$, $\sinh z = (e^z - e^{-z})/2$ and $\cosh z = (e^z + e^{-z})/2$ ([[§30 The Exponential Function#^thm-30-3|Theorem §30.3]], [[§39★ Hyperbolic Functions#^def-39-1|Definition §39.1]]) are entire and reduce to the real functions of calculus on the real axis. So
>
> $$
> h_1(z) = \cosh^2z - \sinh^2z - 1 \qquad\text{and}\qquad h_2(z) = \sinh z + \cosh z - e^z
> $$
>
> are entire ([[§25 Analytic Functions#^prop-25-1|Proposition §25.1]]), and both vanish at every real $x$, in particular along the segment $[0, 1]$ of the real axis. By Lemma §28.1 with $D = \mathbb{C}$, $h_1 \equiv 0$ and $h_2 \equiv 0$.
>
> The same argument transfers to complex arguments every identity between entire functions that holds on a segment of the real axis, such as $\sin^2z + \cos^2z = 1$ ([[§37 The Trigonometric Functions sin z and cos z#^ex-37-1|Example §37.1]](c)). For an identity in two variables, such as $\cos(z_1 + z_2) = \cos z_1\cos z_2 - \sin z_1\sin z_2$, apply it twice: for fixed real $z_2$ both sides are entire in $z_1$ and agree for real $z_1$, hence for all $z_1$; then for fixed complex $z_1$ both sides are entire in $z_2$ and agree for real $z_2$, hence for all $z_2$.
>
> *B&C: Sec. 39, Exercise 14*

^ex-28-3
