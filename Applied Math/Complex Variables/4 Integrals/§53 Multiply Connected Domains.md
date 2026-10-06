---
type: section
subject: "[[Complex Variables]]"
chapter: 4
section: 53
bc: "53"
aliases: ["B&C 53"]
tags: [complex-variables, math342]
---
← [[§52 Simply Connected Domains]] · ↑ [[· 4 Integrals]] · [[§54 Cauchy Integral Formula]] →

*Brown–Churchill, Section 53 · MAT 342 HW 6, HW 7.*

When a function has singular points inside a contour, the Cauchy–Goursat theorem no longer gives zero, but it still says a great deal: the integral around the outer contour equals the sum of the integrals around small contours enclosing the singular points. The proof cuts the region with holes into two pieces without holes, applies the Cauchy–Goursat theorem to each, and lets the integrals along the cuts cancel. Its corollary, the principle of deformation of paths, says that a contour may be moved freely across points where the integrand is analytic without changing the integral; this is the first step of the Cauchy integral formula and of every residue computation.

> [!definition] Definition §53.1: Multiply Connected Domain
> A domain that is not simply connected ([[§52 Simply Connected Domains#^def-52-1|Definition §52.1]]) is said to be **multiply connected**.
>
> *B&C: Sec. 53 (text)*

^def-53-1

For example, the annulus between two concentric circles, and the domain inside a simple closed contour $C$ and outside finitely many disjoint simple closed contours interior to $C$, are multiply connected.

> [!theorem] Theorem §53.1: Cauchy–Goursat Theorem for Multiply Connected Domains
> Suppose that
> - (a) $C$ is a simple closed contour, described in the counterclockwise direction;
> - (b) $C_k$ ($k = 1, 2, \ldots, n$) are simple closed contours interior to $C$, all described in the clockwise direction, that are disjoint and whose interiors have no points in common.
>
> If a function $f$ is analytic on all of these contours and throughout the multiply connected domain consisting of the points inside $C$ and exterior to each $C_k$, then
>
> $$
> \int_C f(z)\,dz + \sum_{k=1}^{n}\int_{C_k} f(z)\,dz = 0 . \qquad (1)
> $$
>
> In equation (1) the direction of each path of integration is such that the multiply connected domain lies to the *left* of that path.
>
> *B&C: Sec. 53, Theorem*

^thm-53-1

> [!proof]+ Proof
> *B&C gives this as a sketch, guided by a figure with $n = 2$ (below).*
>
> **Cuts.** Introduce a polygonal path $L_1$, consisting of a finite number of line segments joined end to end, connecting the outer contour $C$ to the inner contour $C_1$; another polygonal path $L_2$ connecting $C_1$ to $C_2$; and continue in this manner, with $L_{n+1}$ connecting $C_n$ to $C$. The paths run through the multiply connected domain and do not meet each other or the contours except at their end points.
>
> **Two simple closed contours.** The cuts divide the domain into two pieces, bounded by simple closed contours $\Gamma_1$ and $\Gamma_2$. Each consists of the polygonal paths $L_k$ or $-L_k$ and pieces of $C$ and the $C_k$, and each is described in such a direction that the points enclosed by it lie to the left. (B&C takes the possibility of such cuts from the figure; for the circles and smooth contours met in practice they are easy to draw.) The points interior to $\Gamma_1$ or $\Gamma_2$ belong to the multiply connected domain, so $f$ is analytic at all points interior to and on $\Gamma_1$, and likewise for $\Gamma_2$. By the Cauchy–Goursat theorem,
>
> $$
> \int_{\Gamma_1} f(z)\,dz = 0, \qquad \int_{\Gamma_2} f(z)\,dz = 0 .
> $$
>
> **Cancellation.** Add these two equations. Each cut $L_k$ is traversed once in each direction, once as part of $\Gamma_1$ and once as part of $\Gamma_2$, so the integrals along it cancel. The pieces of $C$ in $\Gamma_1$ and $\Gamma_2$ make up all of $C$, traversed counterclockwise; the pieces of each $C_k$ make up all of $C_k$, traversed clockwise (with the domain on the left in both cases). Only the integrals along $C$ and the $C_k$ remain, and the sum is statement (1).

^pf-53-1

*Uses:* [[§51 Proof of the Theorem (Cauchy–Goursat Theorem)#^thm-51-3|§51.3]], [[§44 Contour Integrals#^thm-44-2|§44.2]]

![[m342-53-1.svg]]
*The proof for $n = 2$. The cuts $L_1$ (from $C$ to $C_1$), $L_2$ (from $C_1$ to $C_2$) and $L_3$ (from $C_2$ to $C$) split the domain into an upper piece bounded by $\Gamma_1$ and a lower piece bounded by $\Gamma_2$. The upper edges of the cuts (arrows to the right) belong to $\Gamma_1$, the lower edges (arrows to the left) to $\Gamma_2$; together they cancel. What remains is $C$ counterclockwise and $C_1$, $C_2$ clockwise, each with the domain on its left.*

> [!remark]- Connections
> - The same cutting argument proves Green's theorem for regions with holes, [[§131 Extended Versions of Green's Theorem#^thm-131-2|Calc Thm. §131.2]]: the outer boundary is counterclockwise and the inner boundaries clockwise, so that the region is always on the left. Applied with the Cauchy–Riemann equations ([[§21 Cauchy–Riemann Equations#^thm-21-1|Theorem §21.1]]), as in the proof of [[§50 Cauchy–Goursat Theorem#^thm-50-2|Theorem §50.2]], that version gives Theorem §53.1 for functions with continuous $f'$. The rigorous Green's theorem, [[§27 Line Integrals and Green's Theorem#^thm-27-1|452 Thm. §27.1]], is stated for a region bounded by one simple closed curve; it extends to regions with holes by the same cutting.

> [!theorem] Corollary §53.2: Principle of Deformation of Paths
> Let $C_1$ and $C_2$ denote positively oriented simple closed contours, where $C_1$ is interior to $C_2$. If a function $f$ is analytic in the closed region consisting of those contours and all points between them, then
>
> $$
> \int_{C_1} f(z)\,dz = \int_{C_2} f(z)\,dz . \qquad (2)
> $$
>
> *B&C: Sec. 53, Corollary*

^cor-53-2

> [!proof]+ Proof
> Apply Theorem §53.1 with $C_2$ as the outer contour, counterclockwise, and the single inner contour $-C_1$, which is $C_1$ described clockwise. Then $f$ is analytic on both contours and throughout the domain between them, and
>
> $$
> \int_{C_2} f(z)\,dz + \int_{-C_1} f(z)\,dz = 0 .
> $$
>
> Since $\int_{-C_1} f(z)\,dz = -\int_{C_1} f(z)\,dz$, this is the same as equation (2).

^pf-53-2

*Uses:* [[§53 Multiply Connected Domains#^thm-53-1|§53.1]], [[§44 Contour Integrals#^thm-44-2|§44.2]]

The name comes from the picture: if $C_1$ is continuously deformed into $C_2$, always passing through points at which $f$ is analytic, then the value of the integral of $f$ over $C_1$ never changes.

> [!remark] Remark: Method — Deforming a Contour
> To evaluate $\int_C f(z)\,dz$ around a positively oriented simple closed contour $C$:
> 1. **Locate the singular points** of $f$ (where it fails to be analytic) inside $C$. None: the integral is $0$ ([[§51 Proof of the Theorem (Cauchy–Goursat Theorem)#^thm-51-3|§51.3]]).
> 2. **One singular point $z_0$:** replace $C$ by a positively oriented circle $C_0$ about $z_0$, small enough to lie inside $C$ (Corollary §53.2). The circle can be parametrized, and $\int_{C_0}(z - z_0)^{n-1}\,dz$ is $2\pi i$ for $n = 0$ and $0$ for $n = \pm1, \pm2, \ldots$ ([[§45 Some Examples (Contour Integrals)#^ex-45-5|Example §45.5]]).
> 3. **Several singular points $z_1, \ldots, z_m$:** surround each by a small circle $C_k$, the circles disjoint and inside $C$. Theorem §53.1, with the $C_k$ reversed to the positive sense, gives $\int_C f(z)\,dz = \sum_k\int_{C_k} f(z)\,dz$, each circle taken counterclockwise.
> 4. **Evaluate the small integrals,** by parametrization or, more often, by the Cauchy integral formula ([[§54 Cauchy Integral Formula#^thm-54-1|§54.1]]) and its extension ([[§56★ Verification of the Extension (An Extension of the Cauchy Integral Formula)#^thm-56-1|§56.1]]).
>
> Before deforming, check that the closed region between the two contours contains no singular point: a small circle must lie *strictly* inside $C$.

^rem-53-1

> [!example] Example §53.1: The Integral of 1/z Around Any Contour About the Origin
> When $C$ is any positively oriented simple closed contour surrounding the origin,
>
> $$
> \int_C \frac{dz}{z} = 2\pi i .
> $$
>
> Construct a positively oriented circle $C_0$ with center at the origin and radius so small that $C_0$ lies entirely inside $C$. By [[§45 Some Examples (Contour Integrals)#^ex-45-5|Example §45.5]] (or directly: with $z = \rho e^{i\theta}$, $\int_{C_0}dz/z = \int_{-\pi}^{\pi} i\,d\theta$),
>
> $$
> \int_{C_0}\frac{dz}{z} = 2\pi i ,
> $$
>
> and since $1/z$ is analytic everywhere except at $z = 0$, it is analytic in the closed region between $C_0$ and $C$; Corollary §53.2 gives the result. The radius of $C_0$ could equally well have been so large that $C$ lies entirely inside $C_0$. (For the boundary of the square $|x| \le 1$, $|y| \le 1$, quadrature over the four sides gives $6.2831853\ldots i = 2\pi i$.)
>
> *B&C: Sec. 53, Example*

^ex-53-1

> [!example] Example §53.2: Replacing a Square by a Circle
> Let $C_1$ denote the positively oriented boundary of the square whose sides lie along the lines $x = \pm1$, $y = \pm1$, and let $C_2$ be the positively oriented circle $|z| = 4$. Explain why
>
> $$
> \int_{C_1} f(z)\,dz = \int_{C_2} f(z)\,dz
> $$
>
> when (a) $f(z) = \dfrac{1}{3z^2 + 1}$; (b) $f(z) = \dfrac{z + 2}{\sin(z/2)}$; (c) $f(z) = \dfrac{z}{1 - e^z}$.
>
> By Corollary §53.2 it suffices that $f$ be analytic in the closed region between the square and the circle, that is, that every singular point of $f$ with $|z| \le 4$ lie strictly inside the square.
>
> **(a)** $f$ is analytic except where $3z^2 + 1 = 0$, i.e. $z = \pm i/\sqrt3$. Since $1/\sqrt3 \approx 0.577 < 1$, both points lie inside the square.
>
> **(b)** $f$ is a quotient of entire functions, analytic except where $\sin(z/2) = 0$, i.e. $z/2 = n\pi$, $z = 2n\pi$ ($n = 0, \pm1, \pm2, \ldots$). Since $2\pi > 4$, the only one with $|z| \le 4$ is $z = 0$, inside the square.
>
> **(c)** $f$ is analytic except where $e^z = 1$. Writing $e^z = e^xe^{iy}$, this means $e^x = 1$ and $e^{iy} = 1$, so $x = 0$ and $y = 2n\pi$: $z = 2n\pi i$. Again only $z = 0$ has $|z| \le 4$, and it lies inside the square.
>
> (The common values, checked by quadrature on both contours, are (a) $0$, (b) $8\pi i$, (c) $0$; the exercise asks only for the equality.)
>
> *B&C: Sec. 53, Exercise 2; Source: 342 HW 6*

^ex-53-2

> [!example] Example §53.3: Powers of z − 2 − i Around a Rectangle
> Let $C$ be the boundary of the rectangle $0 \le x \le 3$, $0 \le y \le 2$, described in the positive sense. Show that
>
> $$
> \int_C (z - 2 - i)^{n-1}\,dz = \begin{cases} 0, & n = \pm1, \pm2, \ldots, \\ 2\pi i, & n = 0 . \end{cases}
> $$
>
> **The comparison circle.** The point $z_0 = 2 + i$ lies inside the rectangle, at distance $1$ from the sides $y = 0$, $y = 2$ and $x = 3$, and $2$ from $x = 0$. Let $C_0$ be the positively oriented circle $|z - 2 - i| = \frac12$; since $\frac12 < 1$, it lies entirely inside $C$. (A circle of radius $1$ would touch three sides of the rectangle, so it would not be interior to $C$ and the corollary would not apply.)
>
> **Deformation.** For $n \ge 1$, $(z - 2 - i)^{n-1}$ is a polynomial; for $n \le 0$ it is $1/(z - 2 - i)^{1-n}$, analytic except at $z_0$. In either case it is analytic in the closed region between $C_0$ and $C$, so by Corollary §53.2 and [[§45 Some Examples (Contour Integrals)#^ex-45-5|Example §45.5]] (with $R = \frac12$),
>
> $$
> \int_C (z - 2 - i)^{n-1}\,dz = \int_{C_0}(z - 2 - i)^{n-1}\,dz = \begin{cases} 0, & n = \pm1, \pm2, \ldots, \\ 2\pi i, & n = 0 . \end{cases}
> $$
>
> (Quadrature along the four sides gives $2\pi i$ for $n = 0$ and $0$ for $n = -2, -1, 1, 2$.)
>
> *B&C: Sec. 53, Exercise 3; Source: 342 HW 7*

^ex-53-3
