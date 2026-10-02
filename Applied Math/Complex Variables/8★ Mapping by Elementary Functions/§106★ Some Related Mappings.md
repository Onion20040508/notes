---
type: section
subject: "[[Complex Variables]]"
chapter: 8
section: 106
bc: "106"
aliases: ["B&C 106"]
tags: [complex-variables, math342, extension]
---
← [[§105★ Mapping Horizontal Line Segments by w = sin z]] · ↑ [[· 8★ Mapping by Elementary Functions]] · [[§107★ Mappings by z²]] →

*Brown–Churchill, Section 106.*
★ *Beyond MAT 342: the course skipped this section or left it optional; it is included from Brown–Churchill.*

Once the sine mapping is known, the cosine and the hyperbolic functions come for free: each is the sine preceded or followed by a translation or a rotation through a right angle. So the pictures of [[§104★ Mapping Vertical Line Segments by w = sin z|§104]] and [[§105★ Mapping Horizontal Line Segments by w = sin z|§105]] are simply moved around. The examples also show the other direction: $\cosh z$ factors through $e^z$ and $\frac12(Z + 1/Z)$, which gives a second proof of the half-strip mapping.

> [!remark] Remark: Method — Reducing to a Known Mapping by an Identity
> Rewrite the function with an identity as a chain of maps whose effect is known: translations and rotations ([[§96★ Linear Transformations|§96]]), $e^z$ ([[§103★ Mappings by the Exponential Function|§103]]), $\sin z$ (§104–§105), $z + 1/z$ ([[§98★ Mappings by 1∕z#^ex-98-4|Example §98.4]]). Push the region through the chain one step at a time, keeping track of boundary points.

^rem-106-1

## Cosine and the Hyperbolic Functions

> [!example] Example §106.1: The Cosine Is a Shifted Sine
> By the identity $\sin(z + \pi/2) = \cos z$ ([[§37 The Trigonometric Functions sin z and cos z#^cor-37-4|Corollary §37.4]]), the transformation $w = \cos z$ can be written successively as
>
> $$
> Z = z + \frac\pi2, \qquad w = \sin Z .
> $$
>
> So the cosine transformation is the sine transformation preceded by a translation to the right through $\pi/2$. For example, $\cos z$ maps the half strip $0 \le x \le \pi$, $y \ge 0$ one to one onto the lower half plane $v \le 0$: since $-\cos z = \sin(z - \pi/2)$, the translation $z \mapsto z - \pi/2$ carries this half strip onto the half strip $-\pi/2 \le x \le \pi/2$, $y \ge 0$ of [[§104★ Mapping Vertical Line Segments by w = sin z#^ex-104-1|Example §104.1]], which $\sin$ maps one to one onto $v \ge 0$, and the rotation $w \mapsto -w$ turns this into $v \le 0$.
>
> *B&C: Sec. 106, Example 1*

^ex-106-1

> [!example] Example §106.2: sinh z and cosh z
> By [[§39★ Hyperbolic Functions#^prop-39-2|Proposition §39.2]], $\sinh z = -i\sin(iz)$, so $w = \sinh z$ is
>
> $$
> Z = iz, \qquad W = \sin Z, \qquad w = -iW :
> $$
>
> the sine transformation between two rotations through right angles (counterclockwise before, clockwise after). Likewise $\cosh z = \cos(iz)$, so $w = \cosh z$ is essentially a cosine transformation, preceded by a rotation through $\pi/2$.
>
> *B&C: Sec. 106, Example 2*

^ex-106-2

> [!example] Example §106.3: cosh z Maps a Half Strip onto a Quadrant
> Combining the identities of Examples §106.1 and §106.2, $\cosh z = \cos(iz) = \sin(iz + \pi/2)$, so $w = \cosh z$ is
>
> $$
> Z = iz + \frac\pi2, \qquad w = \sin Z . \qquad (1)
> $$
>
> Find the image of the horizontal semi-infinite strip $x \ge 0$, $0 \le y \le \pi/2$.
>
> With $z = x + iy$, the first map gives $Z = \big(\frac\pi2 - y\big) + ix$: a rotation of the strip through a right angle in the positive direction followed by a translation $\pi/2$ to the right. So $X = \frac\pi2 - y$ runs over $[0, \pi/2]$ and $Y = x$ over $Y \ge 0$: the strip goes onto the vertical half strip $0 \le X \le \pi/2$, $Y \ge 0$. By [[§104★ Mapping Vertical Line Segments by w = sin z#^ex-104-2|Example §104.2]], $w = \sin Z$ maps that one to one onto the first quadrant $u \ge 0$, $v \ge 0$.
>
> **Corresponding boundary points** (left to the reader by B&C):
> - the segment $x = 0$, $0 \le y \le \pi/2$: $\cosh(iy) = \cos y$, so it goes onto the segment from $w = 1$ to $w = 0$;
> - the ray $y = 0$, $x \ge 0$: $\cosh x \ge 1$, so it goes onto the ray $u \ge 1$, starting at $w = 1$;
> - the ray $y = \pi/2$, $x \ge 0$: $\cosh(x + i\pi/2) = i\sinh x$, so it goes onto the positive $v$ axis, starting at $w = 0$.
>
> *B&C: Sec. 106, Example 3*

^ex-106-3

![[m342-106-1.svg]]
*$w = \cosh z$ on the half strip $x \ge 0$, $0 \le y \le \frac\pi2$. Vertical segments $x = 0.4, 0.8, 1.2, 1.6$ (blue) go onto quarter ellipses with foci $\pm1$, horizontal rays $y = \frac\pi8, \frac\pi4, \frac{3\pi}8$ (red) onto quarter branches of the confocal hyperbolas. The left edge (green) goes onto $[0, 1]$, the bottom edge (black) onto $u \ge 1$, and the top edge (orange) onto the positive $v$ axis.*

## Two More Routes to the Half Plane

> [!example] Example §106.4: cosh z Through the Exponential
> Since $\cosh z = \frac12(e^z + e^{-z})$, the transformation $w = \cosh z$ is the composition
>
> $$
> Z = e^z, \qquad W = Z + \frac1Z, \qquad w = \frac12W .
> $$
>
> Show that it maps the semi-infinite strip $x \le 0$, $0 \le y \le \pi$ onto the lower half $v \le 0$ of the $w$ plane.
>
> **Step 1.** By [[§103★ Mappings by the Exponential Function#^prop-103-1|Proposition §103.1]], $Z = e^z$ has $|Z| = e^x \le 1$ and $\arg Z = y \in [0, \pi]$: the strip goes one to one onto the closed upper half of the unit disk with $Z = 0$ removed.
>
> **Step 2.** For $Z = re^{i\theta}$,
>
> $$
> W = Z + \frac1Z = \Big(r + \frac1r\Big)\cos\theta + i\Big(r - \frac1r\Big)\sin\theta .
> $$
>
> For $0 < r < 1$ and $0 < \theta < \pi$, $\operatorname{Im} W < 0$. Conversely, given $W$ with $\operatorname{Im} W < 0$, the equation $Z + 1/Z = W$, that is $Z^2 - WZ + 1 = 0$, has two roots with product $1$; neither lies on $|Z| = 1$ (there $Z + 1/Z = 2\cos\theta$ is real), so exactly one, $Z_0$, lies in $|Z| < 1$, and since $\operatorname{Im}(Z_0 + 1/Z_0) < 0$ the formula above forces $\sin\theta > 0$. So the open half disk goes one to one onto the open lower half plane, and halving keeps $v < 0$.
>
> **Boundary.** The segment $x = 0$, $0 \le y \le \pi$ gives $Z = e^{iy}$ and $w = \cos y$: the segment from $w = 1$ to $w = -1$. The ray $y = 0$, $x \le 0$ gives $Z = e^x \in (0, 1]$ and $w = \cosh x$: the ray $u \ge 1$. The ray $y = \pi$, $x \le 0$ gives $Z = -e^x$ and $w = -\cosh x$: the ray $u \le -1$. Together they make the whole real axis, so the closed strip goes onto $v \le 0$.
>
> *B&C: Sec. 106, Exercise 10*

^ex-106-4

> [!example] Example §106.5: The Sine Half Strip Once More
> **(a)** The equation $w = \sin z$ can be written
>
> $$
> Z = i\Big(z + \frac\pi2\Big), \qquad W = \cosh Z, \qquad w = -W ,
> $$
>
> because $\cosh\big(i(z + \pi/2)\big) = \cos(z + \pi/2) = -\sin z$ (Example §106.2 and [[§37 The Trigonometric Functions sin z and cos z#^cor-37-4|Corollary §37.4]]).
>
> **(b)** For the strip $-\pi/2 \le x \le \pi/2$, $y \ge 0$, the first map gives $Z = -y + i\big(x + \frac\pi2\big)$, so $X = -y \le 0$ and $0 \le Y = x + \frac\pi2 \le \pi$: the strip of Example §106.4. That example takes it onto $\operatorname{Im} W \le 0$, and $w = -W$ takes this onto $v \ge 0$. This is the mapping of [[§104★ Mapping Vertical Line Segments by w = sin z#^ex-104-1|Example §104.1]], obtained without sweeping.
>
> *B&C: Sec. 106, Exercise 11*

^ex-106-5
