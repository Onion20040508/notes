---
type: section
subject: "[[Complex Variables]]"
chapter: 8
section: 110
bc: "110"
aliases: ["B&C 110"]
tags: [complex-variables, math342, extension]
---
← [[§109★ Square Roots of Polynomials]] · ↑ [[· 8★ Mapping by Elementary Functions]] · [[§111★ Surfaces for Related Functions]] →

*Brown–Churchill, Section 110.*
★ *Beyond MAT 342: the course skipped this section or left it optional; it is included from Brown–Churchill.*

A multiple-valued function such as $\log z$ or $z^{1/2}$ becomes single-valued if its domain is replaced by a surface with several sheets lying over the plane, one sheet for each branch, glued along the branch cuts so that crossing a cut moves the point onto the next sheet. On such a **Riemann surface** the function takes one value at each point and is analytic, and the complications of choosing branches are replaced by geometry. B&C treats the idea informally, through the two basic examples: infinitely many sheets for $\log z$, two for $z^{1/2}$, joined in a way that cannot be built in three-dimensional space without self-intersection.

## The Idea

> [!definition] Definition §110.1: Riemann Surface
> A **Riemann surface** for a multiple-valued function is a generalization of the complex plane consisting of more than one sheet, the sheets being joined along cuts, such that at each point of the surface only one value of the function is assigned. Once a Riemann surface is devised for a given function, the function is single-valued on the surface, and the theory of single-valued functions applies there.
>
> *B&C: Sec. 110 (text)*

^def-110-1

In each example below, a point of a sheet has polar coordinates $r$ and $\theta$, those of its projection onto the $z$ plane, with $\theta$ restricted to a definite range of $2\pi$ radians on each sheet. When a point reaches the edge of a slit, it continues onto the sheet that is joined to that edge.

> [!example] Example §110.1: A Riemann Surface for log z
> For each $z \ne 0$, $\log z = \ln r + i\theta$ has infinitely many values. Replace the $z$ plane with the origin deleted by the following surface.
> - Let $R_0$ be the punctured plane cut along the positive real axis, with $0 \le \theta \le 2\pi$ on it.
> - Let $R_1$ be cut the same way and placed in front of $R_0$, with $2\pi \le \theta \le 4\pi$; join the lower edge of the slit in $R_0$ to the upper edge of the slit in $R_1$. Continue with $R_2, R_3, \ldots$ in front, joining the lower edge of each slit to the upper edge of the next.
> - Let $R_{-1}$, with $-2\pi \le \theta \le 0$, be placed behind $R_0$, the lower edge of its slit joined to the upper edge of the slit in $R_0$; and so on for $R_{-2}, R_{-3}, \ldots$.
>
> On any continuous curve on this connected surface of infinitely many sheets, $\theta$ varies continuously along with $r$, so $\log z = \ln r + i\theta$ varies continuously and takes one value at each point. As a point makes a complete cycle counterclockwise around the origin on $R_0$, $\theta$ goes from $0$ to $2\pi$; crossing the ray $\theta = 2\pi$ it passes to $R_1$, where $\theta$ runs from $2\pi$ to $4\pi$; and so on.
>
> The points of the surface correspond one to one to the pairs $(r, \theta)$, $r > 0$, $\theta$ real; so $w = \log z = \ln r + i\theta$ maps the whole Riemann surface one to one onto the entire $w$ plane. The image of $R_0$ is the strip $0 \le v \le 2\pi$ (compare [[§102★ Examples (Mappings of the Upper Half Plane)#^ex-102-5|Example §102.5]]); as a point moves from $R_0$ onto $R_1$, its image moves up across the line $v = 2\pi$. On $R_1$, $\log z$ is the analytic continuation ([[§28★ Uniquely Determined Analytic Functions#^def-28-1|Definition §28.1]]) of the single-valued analytic function $\ln r + i\theta$ ($0 < \theta < 2\pi$) upward across the positive real axis; in this sense $\log z$ is an analytic function at all points of the surface.
>
> *B&C: Sec. 110, Example 1*

^ex-110-1

![[m342-110-1.svg]]
*A sketch of the Riemann surface for $\log z$ over the disk $|z| \le 1$, drawn with height $\theta = \operatorname{Im}\log z$: a spiral staircase in which $R_0$ (blue, $0 \le \theta \le 2\pi$) continues smoothly into $R_1$ (red, $2\pi \le \theta \le 4\pi$) and so on. The green path circles the origin once and climbs from $R_0$ onto $R_1$; above any point of the punctured plane lie infinitely many points of the surface, one on each sheet.*

> [!remark]- Connections
> - The projection of this surface onto the punctured plane is a covering map with infinitely many sheets, [[§24 Covering Spaces#^def-24-2|590 Def. §24.2]] and [[§24 Covering Spaces#^def-24-5|590 Def. §24.5]]; in the $w$ coordinate it is $w \mapsto e^w$ from $\mathbb{C}$ onto $\mathbb{C} \setminus \{0\}$, the complex form of $p\colon \mathbb{R} \to S^1$, [[§24 Covering Spaces#^thm-24-2|590 Thm. §24.2]]. B&C's sheets are the slices of the evenly covered cut plane.
> - In modern terms a Riemann surface is a connected surface with complex charts, a topological manifold of dimension $2$ ([[§2 Topological Manifolds#^def-2-2|591 Def. §2.2]]) whose transition maps are analytic.

> [!example] Example §110.2: A Riemann Surface for z^(1/2)
> For each $z \ne 0$, $z^{1/2} = \sqrt r\,e^{i\theta/2}$ has two values. Take two sheets $R_0$ and $R_1$, each cut along the positive real axis, with $R_1$ in front of $R_0$. Join the lower edge of the slit in $R_0$ to the upper edge of the slit in $R_1$, and the lower edge of the slit in $R_1$ to the upper edge of the slit in $R_0$.
>
> As a point starts from the upper edge of the slit in $R_0$ and describes a continuous circuit counterclockwise around the origin, $\theta$ increases from $0$ to $2\pi$; the point then passes onto $R_1$, where $\theta$ increases from $2\pi$ to $4\pi$; and then it passes back onto $R_0$, where $\theta$ may be taken from $4\pi$ to $6\pi$ or from $0$ to $2\pi$, a choice that does not affect $z^{1/2}$ since $e^{i(\theta + 4\pi)/2} = e^{i\theta/2}$. The value of $z^{1/2}$ where the circuit passes from $R_0$ to $R_1$ ($\sqrt r$ times $e^{i\pi} = -1$) differs from its value where it passes from $R_1$ back to $R_0$ ($\sqrt r$ times $e^{2\pi i} = 1$).
>
> This surface is closed and connected, and $z^{1/2}$ is single-valued on it for each $z \ne 0$. The edges are joined in pairs, and the points where one pair is joined are different from the points where the other pair is joined; so the surface cannot be built physically in space without passing through itself. The image of $R_0$ under $w = z^{1/2}$ is the upper half of the $w$ plane, since $\arg w = \theta/2 \in [0, \pi]$ there, and the image of $R_1$ is the lower half, since $\theta/2 \in [\pi, 2\pi]$. On either sheet the function is the analytic continuation, across the cut, of the function on the other sheet; so $z^{1/2}$ is analytic on the surface at all points except the origin.
>
> *B&C: Sec. 110, Example 2 and Exercise 3*

^ex-110-2

![[m342-110-2.svg]]
*A sketch of the Riemann surface for $z^{1/2}$ over $|z| \le 1$, with height $\operatorname{Im} z^{1/2} = \sqrt r\sin(\theta/2)$: $R_0$ (blue, $0 \le \theta \le 2\pi$) lies above the plane and $R_1$ (red, $2\pi \le \theta \le 4\pi$) below. In space the surface has to pass through itself along the positive real axis, where the two pairs of edges are joined; on the abstract surface these are different points. The green path goes twice around the origin before it closes.*

> [!definition] Definition §110.2: Branch Point of a Riemann Surface
> On the Riemann surface for $z^{1/2}$ the origin is common to both sheets, and a curve around it on the surface must wind around it twice in order to be a closed curve. A point of this kind on a Riemann surface is called a **branch point**.
>
> *B&C: Sec. 110 (text)*

^def-110-2

## Examples

> [!example] Example §110.3: Other Cuts, and the Images of the Sheets
> **(a)** The Riemann surface for $\log z$ can equally be built from sheets cut along the negative real axis: let $R_n$ carry the angles $(2n - 1)\pi \le \theta \le (2n + 1)\pi$, and join the lower edge of the slit in each $R_n$ to the upper edge of the slit in $R_{n+1}$. Its points again correspond one to one to the pairs $(r, \theta)$ with $\theta$ real, and $\log z = \ln r + i\theta$, so it is the same surface as in Example §110.1 divided differently into sheets: here $R_0$ carries the principal branch, $-\pi \le \theta \le \pi$.
>
> **(b)** On the surface of Example §110.1, the sheet $R_n$ carries $2n\pi \le \theta \le 2(n + 1)\pi$, so $w = \log z = \ln r + i\theta$ maps it onto the horizontal strip $2n\pi \le v \le 2(n + 1)\pi$; as $r$ runs over $(0, \infty)$, $u = \ln r$ runs over all reals. The strips for different $n$ tile the $w$ plane, meeting along the lines $v = 2(n + 1)\pi$, which are the images of the joined edges.
>
> *B&C: Sec. 110, Exercises 1 and 2*

^ex-110-3

> [!example] Example §110.4: A Curve Whose Image Is the Unit Circle
> Describe the curve on the Riemann surface for $z^{1/2}$ whose image under $w = z^{1/2}$ is the entire circle $|w| = 1$.
>
> On the surface, $|w| = 1$ means $\sqrt r = 1$, so the curve lies over the unit circle $|z| = 1$. Since $\arg w = \theta/2$ must run once through an interval of length $2\pi$, $\theta$ must run through $4\pi$: the curve is the unit circle traversed twice, starting from the upper edge of the slit in $R_0$, once around on $R_0$ ($0 \le \theta \le 2\pi$, image the upper semicircle) and once around on $R_1$ ($2\pi \le \theta \le 4\pi$, image the lower semicircle). It is $z = e^{i\theta}$, $0 \le \theta \le 4\pi$, with image $w = e^{i\theta/2}$.
>
> *B&C: Sec. 110, Exercise 4*

^ex-110-4

> [!example] Example §110.5: Cauchy–Goursat for a Curve That Crosses the Cut
> Let $C$ be the positively oriented circle $|z - 2| = 1$ on the Riemann surface for $z^{1/2}$, with its upper half on $R_0$ and its lower half on $R_1$. Show that $\int_C z^{1/2}\,dz = 0$.
>
> On the upper half of $C$, $\theta = \arg z$ lies in $(0, \pi/6]$ on $R_0$, and the value $\sqrt r\,e^{i\theta/2}$ is unchanged if $4\pi$ is added to $\theta$; on the lower half, which is on $R_1$, $\theta$ lies in $[4\pi - \pi/6, 4\pi)$. So along all of $C$ we may write
>
> $$
> z^{1/2} = \sqrt r\,e^{i\theta/2}, \qquad 4\pi - \frac\pi2 < \theta < 4\pi + \frac\pi2 ,
> $$
>
> with $\theta$ varying continuously. With $\Theta = \theta - 4\pi \in (-\pi/2, \pi/2)$, $e^{i\theta/2} = e^{i\Theta/2}e^{2\pi i} = e^{i\Theta/2}$: on $C$, $z^{1/2}$ is the principal branch $F_0(z)$ ([[§108★ Mappings by Branches of z^(1∕2)#^def-108-1|Definition §108.1]]). $F_0$ is analytic in the half plane $\operatorname{Re} z > 0$, a simply connected domain containing $C$ and its interior ($1 \le x \le 3$ there), so the integral is $0$ by the Cauchy–Goursat theorem ([[§51 Proof of the Theorem (Cauchy–Goursat Theorem)#^thm-51-3|Theorem §51.3]]).
>
> The same argument applies to any simple closed contour that crosses from one sheet to the other without enclosing the branch point, provided some ray from the origin misses the contour and its interior: along the contour the values come from one branch, analytic off that ray. It applies equally to other multiple-valued functions: this extends the Cauchy–Goursat theorem to integrals of multiple-valued functions along curves on their Riemann surfaces.
>
> *B&C: Sec. 110, Exercise 5*

^ex-110-5
