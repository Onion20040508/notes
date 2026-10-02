---
type: section
subject: "[[Complex Variables]]"
chapter: 4
section: 52
bc: "52"
aliases: ["B&C 52"]
tags: [complex-variables, math342]
---
← [[§51 Proof of the Theorem (Cauchy–Goursat Theorem)]] · ↑ [[· 4 Integrals]] · [[§53 Multiply Connected Domains]] →

*Brown–Churchill, Section 52 (with Exercise 5 of Section 53) · MAT 342 HW 6 · Practice Final (Fall 2002).*

The Cauchy–Goursat theorem concerns a simple closed contour and the region it encloses. In a domain without holes the contour may be any closed contour, even one that crosses itself, because the region enclosed by each of its loops lies in the domain. Combined with the theorem on antiderivatives, [[§49 Proof of the Theorem (Antiderivatives)#^thm-49-1|Theorem §49.1]], this shows that every function analytic in such a domain has an antiderivative there, and that every entire function does. These antiderivatives are what make branches of logarithms possible on domains that do not surround a singular point.

## Simply Connected Domains

> [!definition] Definition §52.1: Simply Connected Domain
> A **simply connected** domain $D$ is a domain such that every simple closed contour within it encloses only points of $D$.
>
> The set of points interior to a simple closed contour is an example. The annular domain between two concentric circles is not simply connected: a circle between them encloses points of the inner disk, which are not in the domain.
>
> *B&C: Sec. 52 (text)*

^def-52-1

> [!remark]- Connections
> - In Topology a space is simply connected if it is path connected and every loop in it can be shrunk to a point, [[§23 The Fundamental Group#^def-23-3|590 Def. §23.3]]. For domains in the plane the two definitions agree; this is a classical consequence of the Jordan curve theorem ([[§43 Contours#^thm-43-4|Theorem §43.4]], stated without proof), and the equivalence is not proved in the vault. B&C's version is the one the integral theorems use: the inside of every simple closed contour in $D$ is a region on which the Cauchy–Goursat theorem can be applied.

The closed contour in the Cauchy–Goursat theorem need not be simple when the theorem is adapted to simply connected domains; the contour can actually cross itself.

> [!theorem] Theorem §52.1: Cauchy–Goursat Theorem for Simply Connected Domains
> If a function $f$ is analytic throughout a simply connected domain $D$, then
>
> $$
> \int_C f(z)\,dz = 0 \qquad (1)
> $$
>
> for every closed contour $C$ lying in $D$.
>
> *B&C: Sec. 52, Theorem*

^thm-52-1

> [!proof]+ Proof
> *B&C proves the theorem for closed contours that intersect themselves a finite number of times, and refers to Markushevich, Vol. I, Secs. 63–65, for general contours; [[§52 Simply Connected Domains#^ex-52-2|Example §52.2]] shows one way to handle infinitely many intersections.*
>
> **$C$ simple.** Since $D$ is simply connected, every point interior to $C$ is in $D$, and so is every point of $C$. So $f$ is analytic at each point interior to and on $C$, and the Cauchy–Goursat theorem gives (1).
>
> **$C$ intersects itself finitely many times.** Then $C$ consists of a finite number of simple closed contours. (Here is why. Let $z = z(t)$, $a \le t \le b$, be $C$. If $z(t_1) = z(t_2)$ for some $t_1 < t_2$ with $(t_1, t_2) \ne (a, b)$, the part $t_1 \le t \le t_2$ is a closed contour $C'$, and the rest, $C$ with that part cut out, is a closed contour $C''$; each has fewer pairs of parameters at which it meets itself than $C$ has. Repeating finitely many times leaves closed contours with no self-intersections, that is, simple closed contours.) Each of these lies in $D$, so the integral of $f$ around it is $0$ by the first case, *regardless of its orientation*; and $\int_C f(z)\,dz$ is the sum of these integrals. When two simple closed contours $C_1$ and $C_2$ make up $C$, as in the figure after Example §52.1, for instance,
>
> $$
> \int_C f(z)\,dz = \int_{C_1} f(z)\,dz + \int_{C_2} f(z)\,dz = 0 + 0 = 0 .
> $$

^pf-52-1

*Uses:* [[§51 Proof of the Theorem (Cauchy–Goursat Theorem)#^thm-51-3|§51.3]], [[§52 Simply Connected Domains#^def-52-1|Def. §52.1]], [[§44 Contour Integrals#^thm-44-2|§44.2]]

> [!example] Example §52.1: A Contour That Crosses Itself
> If $C$ denotes any closed contour lying in the open disk $|z| < 2$, then
>
> $$
> \int_C \frac{\sin z}{(z^2 + 9)^5}\,dz = 0 .
> $$
>
> The disk is a simply connected domain (it is the set of points interior to the circle $|z| = 2$). The integrand is a quotient of entire functions, analytic except at the zeros $z = \pm 3i$ of $z^2 + 9$, which are exterior to the disk. So Theorem §52.1 applies, whether or not $C$ crosses itself. (Numerically, over circles inside the disk centered at $0.3$ and at $-0.5 - 0.6i$, the integral is $0$ to 26 digits.)
>
> *B&C: Sec. 52, Example*

^ex-52-1

![[m342-52-1.svg]]
*A closed contour $C$ in the disk $|z| < 2$ that crosses itself once: it is made up of two simple closed loops, one traversed counterclockwise and one clockwise. Each loop encloses only points of the disk, where $\sin z/(z^2 + 9)^5$ is analytic; its singular points $\pm 3i$ lie outside. So the integral around each loop is $0$, and so is the integral around $C$.*

## Antiderivatives

> [!theorem] Corollary §52.2: Antiderivatives in Simply Connected Domains
> A function $f$ that is analytic throughout a simply connected domain $D$ must have an antiderivative everywhere in $D$.
>
> *B&C: Sec. 52, Corollary 1*

^cor-52-2

> [!proof]+ Proof
> A function that is analytic on $D$ is continuous there ([[§19 Derivatives#^thm-19-1|Theorem §19.1]]). By Theorem §52.1, $\int_C f(z)\,dz = 0$ for every closed contour $C$ in $D$. By [[§49 Proof of the Theorem (Antiderivatives)#^thm-49-1|Theorem §49.1]] (a continuous function whose integrals around all closed contours in $D$ vanish has an antiderivative throughout $D$), $f$ has an antiderivative throughout $D$.

^pf-52-2

*Uses:* [[§52 Simply Connected Domains#^thm-52-1|§52.1]], [[§49 Proof of the Theorem (Antiderivatives)#^thm-49-1|§49.1]], [[§19 Derivatives#^thm-19-1|§19.1]]

> [!theorem] Corollary §52.3: Entire Functions Have Antiderivatives
> Entire functions always possess antiderivatives.
>
> *B&C: Sec. 52, Corollary 2*

^cor-52-3

> [!proof]+ Proof
> The finite plane is a simply connected domain: every simple closed contour in it encloses only points of the plane. Apply Corollary §52.2 with $D = \mathbb{C}$.

^pf-52-3

*Uses:* [[§52 Simply Connected Domains#^cor-52-2|§52.2]]

> [!remark] Remark: Simple Connectivity Is Needed
> In the punctured plane $0 < |z| < \infty$, which is not simply connected, $f(z) = 1/z$ is analytic but has no antiderivative: the integral around the unit circle is $2\pi i \ne 0$ ([[§45 Some Examples (Contour Integrals)#^ex-45-5|Example §45.5]]), while a function with an antiderivative integrates to $0$ around every closed contour ([[§49 Proof of the Theorem (Antiderivatives)#^thm-49-1|Theorem §49.1]]). On a simply connected domain that excludes $0$, such as the plane cut along a ray from the origin, $1/z$ does have an antiderivative, a branch of $\log z$; [[§52 Simply Connected Domains#^ex-52-3|Example §52.3]] constructs such branches in general.

^rem-52-1

> [!example] Example §52.2: Infinitely Many Self-Intersections
> Let $C_1$ be the path from the origin to $z = 1$ along the graph of
>
> $$
> y(x) = \begin{cases} x^3\sin(\pi/x), & 0 < x \le 1, \\ 0, & x = 0, \end{cases}
> $$
>
> a smooth arc that crosses the real axis at $x = 1, \frac12, \frac13, \ldots$ ([[§43 Contours#^ex-43-5|Example §43.5]]). Let $C_2$ be the segment of the real axis from $z = 1$ back to the origin, and $C_3$ any smooth arc from the origin to $z = 1$ that does not intersect itself and has only its end points in common with $C_1$ and $C_2$. Show that if $f$ is entire, then
>
> $$
> \int_{C_1} f(z)\,dz = \int_{C_3} f(z)\,dz, \qquad \int_{C_2} f(z)\,dz = -\int_{C_3} f(z)\,dz ,
> $$
>
> and conclude that $\int_C f(z)\,dz = 0$ for the closed contour $C = C_1 + C_2$, although $C$ intersects itself an infinite number of times.
>
> **The two equalities.** $C_1$ is the graph of a function, so it does not intersect itself; $C_3$ does not either; and they share only their end points. So $C_1$ followed by $-C_3$ (from $1$ back to $0$) is a simple closed contour. Since $f$ is entire, the Cauchy–Goursat theorem gives
>
> $$
> \int_{C_1} f(z)\,dz + \int_{-C_3} f(z)\,dz = 0, \qquad\text{that is,}\qquad \int_{C_1} f(z)\,dz = \int_{C_3} f(z)\,dz .
> $$
>
> Likewise $C_3$ followed by $C_2$ is a simple closed contour, so $\int_{C_3} f(z)\,dz + \int_{C_2} f(z)\,dz = 0$.
>
> **The conclusion.** Adding, $\int_C f(z)\,dz = \int_{C_1} f(z)\,dz + \int_{C_2} f(z)\,dz = \int_{C_3} f(z)\,dz - \int_{C_3} f(z)\,dz = 0$. The detour through $C_3$, which meets $C_1$ and $C_2$ only at their ends, replaces one closed contour with infinitely many self-intersections by two simple ones. (For an entire $f$ the result also follows at once from Corollary §52.3: with $F' = f$, every contour from $0$ to $1$ gives $F(1) - F(0)$.)
>
> *B&C: Sec. 53, Exercise 5; Source: 342 HW 6 (optional)*

^ex-52-2

> [!example] Example §52.3: A Branch of log(z − z₀) on the Inside of a Contour
> **True or false:** if $C$ is a simple closed contour and $z_0$ does not belong to the domain $D$ bounded by $C$, then there is a single valued branch of $\log(z - z_0)$ defined for all $z$ in $D$.
>
> **True.** The domain $D$ interior to $C$ is simply connected, and $1/(z - z_0)$ is analytic in $D$ because $z_0 \notin D$. By Corollary §52.2 it has an antiderivative $F$ in $D$: $F'(z) = 1/(z - z_0)$. Consider
>
> $$
> h(z) = (z - z_0)e^{-F(z)}, \qquad h'(z) = e^{-F(z)} - (z - z_0)\frac{1}{z - z_0}e^{-F(z)} = 0 \quad (z \in D) .
> $$
>
> A function whose derivative vanishes throughout a domain is constant ([[§25 Analytic Functions#^thm-25-3|Theorem §25.3]]), so $h(z) = c$, and $c \ne 0$ because neither $z - z_0$ nor $e^{-F(z)}$ vanishes in $D$. Let $\gamma$ be any value of $\log c$, so $e^\gamma = c$, and set $G(z) = F(z) + \gamma$. Then $G$ is analytic in $D$ and
>
> $$
> e^{G(z)} = e^{F(z)}\,c = e^{F(z)}(z - z_0)e^{-F(z)} = z - z_0 ,
> $$
>
> so $G$ is a single valued analytic branch of $\log(z - z_0)$ in $D$. (The same argument works in any simply connected domain not containing $z_0$; it fails in an annulus around $z_0$, where $1/(z - z_0)$ has no antiderivative.)
>
> *The key answers "True, $1/(z - z_0)$ is analytic in $D$"; the construction of the branch from an antiderivative is the step it leaves out.*
>
> *Source: 342 practice final (Fall 2002), Q8(c)*

^ex-52-3
