---
type: section
subject: "[[Complex Variables]]"
chapter: 1
section: 12
bc: "12"
aliases: ["B&C 12"]
tags: [complex-variables, math342, extension]
---
← [[§11 Examples (Roots of Complex Numbers)]] · ↑ [[· 1 Complex Numbers]] · [[§13 Functions and Mappings]] →

*Brown–Churchill, Section 12.*
★ *Beyond MAT 342: the course skipped this section or left it optional; it is included from Brown–Churchill.*

This section sets up the vocabulary of point sets in the plane that the rest of the subject uses constantly: neighborhoods, interior and boundary points, open and closed sets, connectedness, domains and regions, bounded sets and accumulation points. Analytic functions are defined on open sets ([[§25 Analytic Functions#^def-25-1|Definition §25.1]]); the Cauchy–Goursat theorem and the existence of antiderivatives need connected and simply connected domains ([[§49 Proof of the Theorem (Antiderivatives)#^thm-49-1|Theorem §49.1]], [[§52 Simply Connected Domains#^thm-52-1|Theorem §52.1]]); the maximum modulus principle is a statement about bounded closed regions ([[§59 Maximum Modulus Principle#^cor-59-4|Corollary §59.4]]); and the zeros of a nonzero analytic function cannot accumulate inside its domain ([[§82 Zeros of Analytic Functions#^thm-82-2|Theorem §82.2]]). All of it is the topology of the plane with the Euclidean distance $|z_1 - z_2|$, written in the language of complex numbers.

## Neighborhoods and Boundary Points

> [!definition] Definition §12.1: Neighborhood
> The **$\varepsilon$ neighborhood** of a point $z_0$ is the set
>
> $$
> |z - z_0| < \varepsilon \qquad (1)
> $$
>
> of all points $z$ lying inside but not on the circle centered at $z_0$ with a specified positive radius $\varepsilon$. When the value of $\varepsilon$ is understood or immaterial, it is called just a **neighborhood**.
>
> *B&C: Sec. 12, Equations (1)–(2)*

^def-12-1

> [!definition] Definition §12.2: Deleted Neighborhood
> A **deleted neighborhood**, or punctured disk, is the set
>
> $$
> 0 < |z - z_0| < \varepsilon \qquad (2)
> $$
>
> of all points in an $\varepsilon$ neighborhood of $z_0$ except $z_0$ itself.
>
> *B&C: Sec. 12, Equations (1)–(2)*

^def-12-new1

> [!definition] Definition §12.2: Interior Point
> Let $S$ be a set of points of the plane. A point $z_0$ is an **interior point** of $S$ if there is some neighborhood of $z_0$ that contains only points of $S$.
>
> *B&C: Sec. 12 (text)*

^def-12-2

> [!definition] Definition §12.4: Exterior Point
> Let $S$ be a set of points of the plane. A point $z_0$ is an **exterior point** of $S$ if there is a neighborhood of it containing no points of $S$.
>
> *B&C: Sec. 12 (text)*

^def-12-new2

> [!definition] Definition §12.5: Boundary Point
> Let $S$ be a set of points of the plane. If a point $z_0$ is neither an interior point nor an exterior point of $S$, it is a **boundary point** of $S$. A boundary point is therefore a point all of whose neighborhoods contain at least one point in $S$ and at least one point not in $S$. The totality of all boundary points is the **boundary** of $S$.
>
> *B&C: Sec. 12 (text)*

^def-12-new3

> [!definition] Definition §12.3: Open Set
> A set is **open** if it does not contain any of its boundary points.
>
> *B&C: Sec. 12 (text)*

^def-12-3

> [!definition] Definition §12.7: Closed Set
> A set is **closed** if it contains all of its boundary points.
>
> *B&C: Sec. 12 (text)*

^def-12-new4

> [!definition] Definition §12.8: Closure
> The **closure** of a set $S$ is the closed set consisting of all points in $S$ together with the boundary of $S$.
>
> *B&C: Sec. 12 (text)*

^def-12-new5

> [!remark]- Connections
> - The same definitions in $\mathbb{R}^n$, with open balls for neighborhoods: [[§2 Open and Closed Sets#^def-2-3|452 Def. §2.3]] (interior, exterior, boundary points), [[§2 Open and Closed Sets#^def-2-4|452 Def. §2.4]] (open and closed sets), [[§2 Open and Closed Sets#^def-2-5|452 Def. §2.5]] (closure). The plane $\mathbb{C}$ with distance $|z_1 - z_2|$ is $\mathbb{R}^2$ with its Euclidean metric ([[§4 Vectors and Moduli#^prop-4-2|Proposition §4.2]]).

> [!theorem] Proposition §12.1: Open Means Every Point Is Interior
> A set $S$ is open if and only if each of its points is an interior point.
>
> *B&C: Sec. 12, Exercise 6*

^prop-12-1

> [!proof]+ Proof
> B&C leave this as an exercise. By [[§12★ Regions in the Complex Plane#^def-12-2|Definitions §12.2]], [[§12★ Regions in the Complex Plane#^def-12-new2|§12.4]] and [[§12★ Regions in the Complex Plane#^def-12-new3|§12.5]], every point of the plane is exactly one of: an interior point, an exterior point, or a boundary point of $S$.
>
> Suppose $S$ is open and $z_0 \in S$. Then $z_0$ is not a boundary point, since $S$ contains none. Nor is it an exterior point, since every neighborhood of $z_0$ contains the point $z_0$ of $S$. So $z_0$ is an interior point.
>
> Conversely, suppose every point of $S$ is an interior point, and let $z_0$ be a boundary point of $S$. If $z_0$ were in $S$, it would be an interior point, so some neighborhood of $z_0$ would contain only points of $S$; but every neighborhood of a boundary point contains a point not in $S$. Hence $z_0 \notin S$: $S$ contains none of its boundary points and is open.

^pf-12-1

*Uses:* [[§12★ Regions in the Complex Plane#^def-12-2|Def. §12.2]], [[§12★ Regions in the Complex Plane#^def-12-new2|Def. §12.4]], [[§12★ Regions in the Complex Plane#^def-12-new3|Def. §12.5]], [[§12★ Regions in the Complex Plane#^def-12-3|Def. §12.3]]

Some sets are neither open nor closed. For a set $S$ to be not open there must be a boundary point that is contained in the set, and for $S$ to be not closed there must be a boundary point not in it ([[§12★ Regions in the Complex Plane#^ex-12-1|Example §12.1]]).

## Connected Sets, Domains and Regions

> [!definition] Definition §12.4: Connected Set
> An open set $S$ is **connected** if each pair of points $z_1$ and $z_2$ in it can be joined by a **polygonal line**, consisting of a finite number of line segments joined end to end, that lies entirely in $S$.
>
> *B&C: Sec. 12 (text)*

^def-12-4

> [!remark]- Connections
> - For open subsets of the plane, B&C's polygonal definition agrees with topological connectedness, [[§13 Connected Spaces#^def-13-1|590 Def. §13.1]]. A polygonal line is a path, so a polygonally connected set is path-connected, hence connected, [[§14 Connected Subspaces of ℝ#^thm-14-4|590 Thm. §14.4]]. Conversely, in a connected open set the points reachable from a fixed point by polygonal lines form a nonempty subset that is both open and closed in it, hence everything: the argument of [[§2 Topological Manifolds#^thm-2-8|591 Thm. §2.8]], with a segment inside a disk in place of a path in a chart.

> [!definition] Definition §12.10: Domain
> A nonempty open set that is connected is called a **domain**.
>
> *B&C: Sec. 12 (text)*

^def-12-new6

> [!definition] Definition §12.11: Region
> A domain together with some, none, or all of its boundary points is referred to as a **region**.
>
> *B&C: Sec. 12 (text)*

^def-12-new7

> [!definition] Definition §12.5: Bounded Set
> A set $S$ is **bounded** if every point of $S$ lies inside some circle $|z| = R$; otherwise it is **unbounded**.
>
> *B&C: Sec. 12 (text)*

^def-12-5

## Accumulation Points

> [!definition] Definition §12.6: Accumulation Point
> A point $z_0$ is an **accumulation point**, or limit point, of a set $S$ if each deleted neighborhood of $z_0$ contains at least one point of $S$. Thus $z_0$ is *not* an accumulation point of $S$ whenever some deleted neighborhood of $z_0$ contains no point of $S$.
>
> *B&C: Sec. 12 (text)*

^def-12-6

> [!theorem] Theorem §12.2: Closed Sets and Accumulation Points
> A set is closed if and only if it contains all of its accumulation points.
>
> *B&C: Sec. 12 (text) and Exercise 8*

^thm-12-2

> [!proof]+ Proof
> **Closed $\Rightarrow$ contains its accumulation points.** Let $S$ be closed and $z_0$ an accumulation point of $S$. If $z_0$ were not in $S$, every neighborhood of $z_0$ would contain a point of $S$ (one in the deleted neighborhood) and a point not in $S$ (namely $z_0$), so $z_0$ would be a boundary point of $S$ not in $S$. This contradicts the fact that a closed set contains all of its boundary points.
>
> **Contains its accumulation points $\Rightarrow$ closed** (B&C leave this as Exercise 8). Suppose $S$ contains each of its accumulation points, and let $z_0$ be a boundary point of $S$. If $z_0 \notin S$, then each neighborhood of $z_0$ contains a point of $S$, which is different from $z_0$; so each deleted neighborhood of $z_0$ contains a point of $S$, and $z_0$ is an accumulation point of $S$. Then $z_0 \in S$ by hypothesis, a contradiction. Hence every boundary point of $S$ lies in $S$, and $S$ is closed.

^pf-12-2

*Uses:* [[§12★ Regions in the Complex Plane#^def-12-new3|Def. §12.5]], [[§12★ Regions in the Complex Plane#^def-12-new4|Def. §12.7]], [[§12★ Regions in the Complex Plane#^def-12-6|Def. §12.6]]

> [!remark]- Connections
> - In any topological space: limit points [[§7 Interior and Closure#^def-7-3|590 Def. §7.3]], the closure as the set together with its limit points [[§7 Interior and Closure#^thm-7-4|590 Thm. §7.4]], and Theorem §12.2 as [[§7 Interior and Closure#^cor-7-5|590 Cor. §7.5]].

## Examples

> [!example] Example §12.1: Disks, a Punctured Disk, the Plane, an Annulus
> **(a)** The circle $|z| = 1$ is the boundary of each of the sets
>
> $$
> |z| < 1 \qquad\text{and}\qquad |z| \le 1 . \qquad (3)
> $$
>
> The first set is open and the second is its closure. *(B&C state this; here is why.)* If $|z_0| < 1$, the neighborhood of radius $1 - |z_0|$ lies in $|z| < 1$, since $|z| \le |z - z_0| + |z_0| < 1$ by the triangle inequality ([[§5 Triangle Inequality#^thm-5-1|Theorem §5.1]]): $z_0$ is interior. If $|z_0| > 1$, the neighborhood of radius $|z_0| - 1$ misses $|z| \le 1$, since there $|z| \ge |z_0| - |z - z_0| > 1$: $z_0$ is exterior. If $|z_0| = 1$, every neighborhood $|z - z_0| < \varepsilon$ contains $(1 - t)z_0$ (inside) and $(1 + t)z_0$ (outside) for $0 < t < \min(\varepsilon, 1)$: $z_0$ is a boundary point. So the boundary of both sets is $|z| = 1$; the first contains none of it and the second all of it.
>
> **(b)** The punctured disk $0 < |z| \le 1$ is neither open nor closed: its boundary consists of the circle $|z| = 1$ and the point $0$, and it contains the former but not the latter.
>
> **(c)** The set of all complex numbers is both open and closed, since it has no boundary points (every point is interior).
>
> **(d)** The open disk $|z| < 1$ is connected, and so is every neighborhood $|z - z_0| < \varepsilon$: the segment joining two of its points $z_1$, $z_2$ stays in it, since $|(1 - t)z_1 + tz_2 - z_0| \le (1 - t)|z_1 - z_0| + t|z_2 - z_0| < \varepsilon$ for $0 \le t \le 1$. Hence **any neighborhood is a domain**. The annulus $1 < |z| < 2$ is open and also connected, although two of its points need not be joinable by a single segment (B&C Fig. 17; see the figure below). Both sets (3) are bounded regions, while the half plane $\operatorname{Re} z \ge 0$ is unbounded.
>
> *B&C: Sec. 12 (text)*

^ex-12-1

> [!example] Example §12.2: The Set Im(1/z) > 1
> Sketch the set
>
> $$
> \operatorname{Im}\Big(\frac1z\Big) > 1 \qquad (4)
> $$
>
> and identify some of its properties.
>
> **Rewrite.** Except when $z = 0$,
>
> $$
> \frac1z = \frac{\bar z}{z\bar z} = \frac{\bar z}{|z|^2} = \frac{x - iy}{x^2 + y^2} \qquad (z = x + iy) .
> $$
>
> So (4) becomes $\dfrac{-y}{x^2 + y^2} > 1$, or, multiplying by the positive number $x^2 + y^2$,
>
> $$
> x^2 + y^2 + y < 0 .
> $$
>
> **Complete the square.** $x^2 + \big(y^2 + y + \frac14\big) < \frac14$, that is,
>
> $$
> (x - 0)^2 + \Big(y + \frac12\Big)^2 < \Big(\frac12\Big)^2 .
> $$
>
> So (4) represents the region interior to the circle centered at $z = -\frac i2$ with radius $\frac12$ (B&C Fig. 18). The excluded point $z = 0$ lies on this circle, not inside it, so excluding it changes nothing. The set is an open disk: a bounded domain, whose closure is the closed disk $|z + \frac i2| \le \frac12$.
>
> *B&C: Sec. 12, Example*

^ex-12-2

![[m342-12-1.svg]]
*Left: the annulus $1 < |z| < 2$ is a domain: any two of its points $z_1$, $z_2$ can be joined by a polygonal line inside it (red), although the straight segment between them may cross the hole. Right: the set $\operatorname{Im}(1/z) > 1$ of Example §12.2 is the open disk with center $-\frac i2$ and radius $\frac12$; its boundary circle (dashed, not in the set) passes through $0$, where $1/z$ is undefined.*

*Chain (the function 1/z): later in [[§29a The Function 1∕z|Chapter 2]] · [[§59a The Function 1∕z|Chapter 4]]*

> [!example] Example §12.3: Which Sets Are Domains
> Sketch the following sets and determine which are domains, which are neither open nor closed, and which are bounded: **(a)** $|z - 2 + i| \le 1$; **(b)** $|2z + 3| > 4$; **(c)** $\operatorname{Im} z > 1$; **(d)** $\operatorname{Im} z = 1$; **(e)** $0 \le \arg z \le \pi/4$ $(z \ne 0)$; **(f)** $|z - 4| \ge |z|$.
>
> **(a)** The closed disk with center $2 - i$ and radius $1$. It contains its boundary circle, so it is closed and not open: not a domain (it is a region). It is bounded.
>
> **(b)** By (8) of [[§6 Complex Conjugates#^thm-6-4|Theorem §6.4]], $|2z + 3| = 2\,|z + \frac32|$, so the set is $|z + \frac32| > 2$, the exterior of the circle with center $-\frac32$ and radius $2$. It is open (its complement, the closed disk, contains its boundary circle). It is connected. Let $Q$ be the boundary of the square with center $-\frac32$ and side $6$; every point of $Q$ is at distance at least $3 > 2$ from $-\frac32$, so $Q$ lies in the set. From any point $z$ of the set, follow the ray from $-\frac32$ through $z$ (inward or outward) to the point where it meets $Q$. Along this segment the distance to $-\frac32$ varies monotonically between its values at the two ends, both greater than $2$, so the segment lies in the set. Then move along $Q$, which consists of four segments. Joining two such paths along $Q$ connects any two points of the set by a polygonal line. So it is a domain. It is unbounded.
>
> **(c)** The open half plane above the line $y = 1$: open and convex (segments stay in it), hence a domain; unbounded.
>
> **(d)** The horizontal line $y = 1$. Every point of it is a boundary point (every disk around it meets points off the line), so it is closed, not open, and has empty interior: not a domain; unbounded.
>
> **(e)** The closed sector between the rays $\arg z = 0$ and $\arg z = \frac\pi4$, without the vertex. The points of the two edges are boundary points in the set, so it is not open; the vertex $0$ is a boundary point not in the set, so it is not closed. **Neither open nor closed**; unbounded.
>
> **(f)** Squaring, $|z - 4|^2 \ge |z|^2$ means $(x - 4)^2 + y^2 \ge x^2 + y^2$, that is, $-8x + 16 \ge 0$, or $x \le 2$: the closed half plane to the left of the line $x = 2$, the points at least as close to $0$ as to $4$. Closed, not open: not a domain; unbounded.
>
> So the domains are (b) and (c), only (e) is neither open nor closed, and only (a) is bounded, in agreement with B&C's answers.
>
> *B&C: Sec. 12, Exercises 1–3*

^ex-12-3

> [!example] Example §12.4: Accumulation Points
> **(a)** The origin is the only accumulation point of the set $z_n = \dfrac in$ $(n = 1, 2, \ldots)$. Every deleted neighborhood $0 < |z| < \varepsilon$ contains the points $i/n$ with $n > 1/\varepsilon$. If $z_0 \ne 0$, only finitely many $z_n$ satisfy $|z_n - z_0| < \frac12|z_0|$ (for those, $\frac1n = |z_n| > \frac12|z_0|$, so $n < 2/|z_0|$); a deleted neighborhood of $z_0$ with radius smaller than $\frac12|z_0|$ and than the distances from $z_0$ to those of these finitely many points that differ from $z_0$ contains no $z_n$.
>
> **(b)** Determine the accumulation points of: (i) $z_n = i^n$; (ii) $z_n = i^n/n$; (iii) $0 \le \arg z < \pi/2$ $(z \ne 0)$; (iv) $z_n = (-1)^n(1 + i)\dfrac{n - 1}{n}$ $(n = 1, 2, \ldots)$.
>
> (i) The values cycle through $i, -1, -i, 1$: a finite set, which has no accumulation points (a deleted neighborhood whose radius is smaller than the distances from $z_0$ to the finitely many points contains none of them).
>
> (ii) $|z_n| = \frac1n \to 0$, so every deleted neighborhood of $0$ contains $z_n$ for large $n$: $0$ is an accumulation point, and as in (a) there is no other.
>
> (iii) The set is $\{x > 0,\ y \ge 0\}$: it contains the positive real axis but not the positive imaginary axis. Its accumulation points are the points of the closed quadrant $x \ge 0$, $y \ge 0$: every such point has points of the set arbitrarily close to it, other than itself, and every other point has a neighborhood missing the quadrant.
>
> (iv) For even $n$, $z_n = \frac{n-1}{n}(1 + i) \to 1 + i$, and for odd $n$, $z_n \to -(1 + i)$; the accumulation points are $\pm(1 + i)$.
>
> *B&C: Sec. 12 (text) and Exercise 7*

^ex-12-4
