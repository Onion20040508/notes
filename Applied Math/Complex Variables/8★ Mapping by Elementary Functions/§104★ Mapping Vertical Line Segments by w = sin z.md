---
type: section
subject: "[[Complex Variables]]"
chapter: 8
section: "104★"
bc: "104"
aliases: ["B&C 104"]
tags: [complex-variables, math342, extension]
---
← [[§103★ Mappings by the Exponential Function]] · ↑ [[· 8★ Mapping by Elementary Functions]] · [[§105★ Mapping Horizontal Line Segments by w = sin z]] →

*Brown–Churchill, Section 104.*
★ *Beyond MAT 342: the course skipped this section or left it optional; it is included from Brown–Churchill.*

Under $w = \sin z$, vertical lines go onto branches of hyperbolas, all with foci $\pm1$. Sweeping the semi-infinite strip $-\pi/2 \le x \le \pi/2$, $y \ge 0$ by vertical half lines shows that $\sin z$ maps it one to one onto the upper half plane. This is one of the standard maps of Chapter 10: it turns a problem in a slot (two parallel walls and a base) into a problem in a half plane, and its confocal hyperbolas and ellipses ([[§105★ Mapping Horizontal Line Segments by w = sin z|§105]]) are the field lines and equipotentials of a charged strip.

## Vertical Lines

By [[§37 The Trigonometric Functions sin z and cos z#^prop-37-5|Proposition §37.5]], $\sin z = \sin x\cosh y + i\cos x\sinh y$, so the transformation $w = \sin z$, $w = u + iv$, reads

$$
u = \sin x\cosh y, \qquad v = \cos x\sinh y . \qquad (1)
$$

> [!theorem] Proposition §104.1: Vertical Lines Go onto Hyperbolas
> Under $w = \sin z$:
> 1. If $0 < c_1 < \pi/2$, the line $x = c_1$ is mapped one to one onto the right-hand branch of the hyperbola
>
>    $$
>    \frac{u^2}{\sin^2 c_1} - \frac{v^2}{\cos^2 c_1} = 1 , \qquad (3)
>    $$
>
>    whose foci are $w = \pm\sqrt{\sin^2 c_1 + \cos^2 c_1} = \pm1$. As the point $(c_1, y)$ moves up the entire line, its image moves up the entire branch; the top half ($y > 0$) of the line goes onto the top half ($v > 0$) of the branch.
> 2. If $-\pi/2 < c_1 < 0$, the same holds with the left-hand branch of (3).
> 3. The $y$ axis is mapped one to one onto the $v$ axis, by $(0, y) \mapsto (0, \sinh y)$, the positive $y$ axis going onto the positive $v$ axis.
>
> *B&C: Sec. 104 (text); Sec. 106, Exercise 5*

^prop-104-1

> [!proof]+ Proof
> On the line $x = c_1$, equations (1) give the parametric representation
>
> $$
> u = \sin c_1\cosh y, \qquad v = \cos c_1\sinh y \qquad (-\infty < y < \infty) . \qquad (2)
> $$
>
> For $0 < |c_1| < \pi/2$, both $\sin c_1$ and $\cos c_1$ are nonzero, and
>
> $$
> \frac{u^2}{\sin^2 c_1} - \frac{v^2}{\cos^2 c_1} = \cosh^2 y - \sinh^2 y = 1 ,
> $$
>
> so every image point lies on (3). Since $\cosh y > 0$, $u$ has the sign of $\sin c_1$: the image lies on the right-hand branch when $c_1 > 0$ and on the left-hand branch when $c_1 < 0$. Since $\cos c_1 > 0$, $v = \cos c_1\sinh y$ is a continuous, strictly increasing function of $y$ with range all of $\mathbb{R}$. On a given branch a point is determined by its $v$ coordinate ($u = \pm|\sin c_1|\sqrt{1 + v^2/\cos^2 c_1}$, sign fixed by the branch). So $y \mapsto (u, v)$ is one to one onto the branch, moving upward, and $y > 0 \iff v > 0$. For $c_1 = 0$, (1) gives $u = 0$, $v = \sinh y$, a strictly increasing bijection of $\mathbb{R}$ onto $\mathbb{R}$.

^pf-104-1

*Uses:* [[§37 The Trigonometric Functions sin z and cos z#^prop-37-5|§37.5]]

> [!remark] Remark: Method — Sweeping a Region by Curves
> This is B&C's standard way of proving that a map takes one region onto another.
> 1. **Sweep** the region by a one-parameter family of curves (here the vertical half lines), and find the image of each one, with the map one to one along it.
> 2. **Fill.** Show that the image curves are pairwise disjoint and together fill the target region. A clean way is to find a function of $w$ that is constant on each image curve and takes each parameter value once (below: $|w + 1| - |w - 1|$, constant on hyperbolas with foci $\pm1$).
> 3. **Boundary.** Follow the boundary separately; it often goes onto the boundary of the target with folds or identifications.
>
> Then each target point lies on exactly one image curve and is the image of exactly one point of that curve: the map is one to one and onto.

^rem-104-1

## The Half Strip onto the Half Plane

> [!example] Example §104.1: A Half Strip onto the Upper Half Plane
> Show that $w = \sin z$ is a one to one mapping of the semi-infinite strip $-\pi/2 \le x \le \pi/2$, $y \ge 0$ onto the upper half $v \ge 0$ of the $w$ plane.
>
> **The boundary** goes onto the real axis one to one. On $BA$ ($x = \pi/2$, $y \ge 0$), (1) gives $u = \cosh y$, $v = 0$: as $(\pi/2, y)$ moves up from $B$, its image $(\cosh y, 0)$ moves right from $B' = 1$. On $DB$ ($y = 0$, $-\pi/2 \le x \le \pi/2$), the images $(\sin x, 0)$ move right from $D' = -1$ to $B' = 1$. On $DE$ ($x = -\pi/2$, $y \ge 0$), the images $(-\cosh y, 0)$ move left from $D'$. So the boundary goes onto the whole real axis, $E'D'B'A'$, each point once.
>
> **The interior** $-\pi/2 < x < \pi/2$, $y > 0$ is swept by the vertical half lines $x = c_1$, $y > 0$. By Proposition §104.1, each goes one to one onto the top half of a branch of (3), or onto the positive $v$ axis when $c_1 = 0$; all of these lie in $v > 0$. As the half line $L$ ($0 < c_1 < \pi/2$) moves left toward the $y$ axis, its image $L'$ opens up and its vertex $(\sin c_1, 0)$ tends to $0$; as $L$ approaches $BA$, $L'$ closes down around $B'A'$ and its vertex tends to $1$. Similarly for $M$ and $M'$ on the left.
>
> That the images are distinct and fill $v > 0$ (B&C reads it from this picture) follows from the focal property of hyperbolas: a branch of (3) with foci $\pm1$ and vertex $\sin c_1$ is the set of $w$ with
>
> $$
> |w + 1| - |w - 1| = 2\sin c_1 ,
> $$
>
> the right branch for $c_1 > 0$, the left for $c_1 < 0$, and the $v$ axis ($|w + 1| = |w - 1|$) for $c_1 = 0$. For $w$ with $v > 0$, the triangle inequality is strict ($w$ is not on the line through $\pm1$), so $s = \frac12\big(|w + 1| - |w - 1|\big)$ lies in $(-1, 1)$, and there is exactly one $c_1 \in (-\pi/2, \pi/2)$ with $\sin c_1 = s$. So $w$ lies on the image of exactly one half line, and on it is the image of exactly one point. Hence the interior goes one to one onto $v > 0$, and with the boundary the closed half strip goes one to one onto $v \ge 0$.
>
> *B&C: Sec. 104, Example*

^ex-104-1

![[m342-104-1.svg]]
*$w = \sin z$ on the half strip $|x| \le \frac\pi2$, $y \ge 0$. The vertical half lines $x = \pm0.4, \pm0.8, \pm1.2$ (blue) go onto the upper halves of hyperbolas with foci $\pm1$, and the positive $y$ axis (green) onto the positive $v$ axis. The base $DB$ (red) goes onto the segment $[-1, 1]$, and the two walls (black) onto the rest of the real axis: the boundary of the strip is unfolded onto the boundary of the half plane.*

> [!example] Example §104.2: The Right Half of the Strip
> The right-hand half $0 \le x \le \pi/2$, $y \ge 0$ of the strip goes onto the first quadrant $u \ge 0$, $v \ge 0$.
>
> By (1), for $y \ge 0$ and $|x| \le \pi/2$, $u = \sin x\cosh y$ has the sign of $x$. So under the one to one map of Example §104.1, the part $x \ge 0$ goes onto the part $u \ge 0$ of the closed upper half plane: the half lines $x = c_1$ ($0 < c_1 < \pi/2$) onto the top halves of right branches, the positive $y$ axis onto the positive $v$ axis, the segment $0 \le x \le \pi/2$ of the base onto $0 \le u \le 1$, and the wall $x = \pi/2$ onto $u \ge 1$.
>
> *B&C: Sec. 104 (text)*

^ex-104-2

> [!example] Example §104.3: Lines Beyond π/2
> Show that a line $x = c_1$ with $\pi/2 < c_1 < \pi$ is mapped one to one onto the right-hand branch of (3), the upper and lower halves of the line going onto the lower and upper halves of the branch.
>
> Equations (2) still hold, and still $u^2/\sin^2 c_1 - v^2/\cos^2 c_1 = 1$. Now $\sin c_1 > 0$, so $u > 0$: the right-hand branch (the same hyperbola as for $\pi - c_1$, since $\sin^2$ and $\cos^2$ agree). But $\cos c_1 < 0$, so $v = \cos c_1\sinh y$ is strictly **decreasing** from $\infty$ to $-\infty$. As in Proposition §104.1 the map is one to one onto the branch, now traversed downward: $y > 0$ goes onto $v < 0$ and $y < 0$ onto $v > 0$. This agrees with the identity $\sin(\pi - \bar z) = \overline{\sin z}$: the point $c_1 + iy$ is $\pi - \bar z$ for $z = (\pi - c_1) + iy$, so its image is the mirror image, in the $u$ axis, of the image of $(\pi - c_1, y)$.
>
> *B&C: Sec. 106, Exercise 6*

^ex-104-3
