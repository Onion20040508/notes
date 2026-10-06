---
type: section
subject: "[[Applied Linear Algebra]]"
chapter: 2
section: 20
lay: "2.7"
aliases: ["Lay 2.7"]
tags: [applied-linear-algebra, math235]
---
← [[§19 The Leontief Input–Output Model]] · ↑ [[· 2 Matrix Algebra]] · [[§21 Subspaces of ℝⁿ]] →

*Lay, Section 2.7.*

A picture on a screen is stored as a list of points, the columns of a data matrix $D$, together with information about which points are joined by segments. A linear transformation with matrix $A$ moves the whole picture at once: the columns of $AD$ are the images of the points, and segments go to segments. Translations are not linear, but in homogeneous coordinates, where $(x, y)$ is stored as $(x, y, 1)$, they become $3 \times 3$ matrix multiplications too. Then every movement of a figure, scaling, rotating, reflecting and translating in any order, is a single matrix, the product of the steps in reverse order. The same device in 3D, with $4 \times 4$ matrices, also handles the perspective projection of a three-dimensional scene onto the screen.

## Transforming a Figure

> [!example] Example §20.1: Shearing and Scaling the Letter N
> **(a) The data matrix.** The capital letter N is determined by eight vertices, whose coordinates are stored as the columns of a data matrix:
>
> $$
> D = \begin{bmatrix} 0 & .5 & .5 & 6 & 6 & 5.5 & 5.5 & 0 \\ 0 & 0 & 6.42 & 0 & 8 & 8 & 1.58 & 8 \end{bmatrix}
> \qquad \begin{matrix} \text{vertices } 1, \ldots, 8 \\ (x\text{-coordinates on top}) \end{matrix}
> $$
>
> Consecutive vertices are joined by segments, and vertex 8 is joined to vertex 1. (In general one must also specify which vertices are connected; Lay omits this detail.)
>
> **(b) A shear.** Describe the effect of the shear $\mathbf{x} \mapsto A\mathbf{x}$, $A = \begin{bmatrix} 1 & .25 \\ 0 & 1 \end{bmatrix}$, on the N. By the definition of matrix multiplication, the columns of $AD$ are the images of the vertices: each point $(x, y)$ goes to $(x + .25y, y)$, so
>
> $$
> AD = \begin{bmatrix} 0 & .5 & 2.105 & 6 & 8 & 7.5 & 5.895 & 2 \\ 0 & 0 & 6.420 & 0 & 8 & 8 & 1.580 & 8 \end{bmatrix} .
> $$
>
> (For instance vertex 3: $.5 + .25(6.42) = .5 + 1.605 = 2.105$.) Joining the image vertices in the same pattern gives an italic N.
>
> **(c) A composite.** The italic N looks a bit too wide. Shrink its width with the scaling $S = \begin{bmatrix} .75 & 0 \\ 0 & 1 \end{bmatrix}$, which multiplies $x$-coordinates by $.75$. The shear followed by the scaling has matrix (note the order)
>
> $$
> SA = \begin{bmatrix} .75 & 0 \\ 0 & 1 \end{bmatrix}\begin{bmatrix} 1 & .25 \\ 0 & 1 \end{bmatrix} = \begin{bmatrix} .75 & .1875 \\ 0 & 1 \end{bmatrix},
> $$
>
> and the final figure is given by the data matrix $(SA)D$.
>
> *Lay: Examples 2.7.1–2.7.3*

^ex-20-1

![[m235-17-1.svg]]
*[[§20 Applications to Computer Graphics#^ex-20-1|Example §20.1]]. Left: the regular N with its eight vertices. Middle: the sheared N, data matrix $AD$; each vertex moves right by a quarter of its height (dashed: the original). Right: the composite $SA$, which also squeezes the width by the factor $.75$. Only the vertices are transformed; the segments between them are redrawn, which is legitimate because linear maps send segments to segments.*

> [!remark] Remark: Why Figures Are Built from Segments
> The standard transformations of computer graphics map line segments onto line segments (for a linear $T$, the segment $\{(1 - t)\mathbf{p} + t\mathbf{q} : 0 \le t \le 1\}$ goes to $\{(1 - t)T(\mathbf{p}) + tT(\mathbf{q})\}$, the segment between the images; Lay's Exercise 27 in Section 1.8, [[§9 Introduction to Linear Transformations|§9]]). So once the vertices of an object have been transformed, their images can be joined by the appropriate segments to produce the image of the whole object. Curved letters are stored with additional formulas for the curves, and curves are often approximated by short segments.

^rem-20-1

## Homogeneous Coordinates

Translating an object does not correspond directly to matrix multiplication, because a translation $\mathbf{x} \mapsto \mathbf{x} + \mathbf{p}$ ($\mathbf{p} \ne \mathbf{0}$) is not linear: it does not send $\mathbf{0}$ to $\mathbf{0}$. The standard way around this is to add a coordinate.

> [!definition] Definition §20.1: Homogeneous Coordinates in the Plane
> Each point $(x, y)$ in $\mathbb{R}^2$ is identified with the point $(x, y, 1)$ on the plane in $\mathbb{R}^3$ that lies one unit above the $xy$-plane. We say that $(x, y)$ has **homogeneous coordinates** $(x, y, 1)$. For instance, $(0, 0)$ has homogeneous coordinates $(0, 0, 1)$. Homogeneous coordinates of points are not added or multiplied by scalars, but they can be transformed by multiplication by $3 \times 3$ matrices.
>
> *Lay: 2.7 (text)*

^def-20-1

> [!theorem] Proposition §20.1: Translations and Linear Maps in Homogeneous Coordinates
> **(a)** The translation $(x, y) \mapsto (x + h, y + k)$ is written in homogeneous coordinates as $(x, y, 1) \mapsto (x + h, y + k, 1)$, and is computed by matrix multiplication:
>
> $$
> \begin{bmatrix} 1 & 0 & h \\ 0 & 1 & k \\ 0 & 0 & 1 \end{bmatrix}\begin{bmatrix} x \\ y \\ 1 \end{bmatrix} = \begin{bmatrix} x + h \\ y + k \\ 1 \end{bmatrix} .
> $$
>
> **(b)** A linear transformation of $\mathbb{R}^2$ with standard matrix $A$ is represented in homogeneous coordinates by the partitioned matrix $\begin{bmatrix} A & 0 \\ 0 & 1 \end{bmatrix}$. Typical examples:
>
> $$
> \underbrace{\begin{bmatrix} \cos\varphi & -\sin\varphi & 0 \\ \sin\varphi & \cos\varphi & 0 \\ 0 & 0 & 1 \end{bmatrix}}_{\substack{\text{counterclockwise rotation} \\ \text{about the origin, angle } \varphi}}, \qquad
> \underbrace{\begin{bmatrix} 0 & 1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{bmatrix}}_{\text{reflection through } y = x}, \qquad
> \underbrace{\begin{bmatrix} s & 0 & 0 \\ 0 & t & 0 \\ 0 & 0 & 1 \end{bmatrix}}_{\text{scale } x \text{ by } s \text{ and } y \text{ by } t} .
> $$
>
> **(c)** The composite of such transformations is represented by the product of their $3 \times 3$ matrices, in reverse order.
>
> *Lay: 2.7, Examples 4 and 5 and text*

^prop-20-1

> [!proof]+ Proof
> (a) is the displayed multiplication, done by the row–column rule. For (b), block multiplication ([[§17 Partitioned Matrices#^prop-17-2|Proposition §17.2]]) gives
>
> $$
> \begin{bmatrix} A & 0 \\ 0 & 1 \end{bmatrix}\begin{bmatrix} \mathbf{x} \\ 1 \end{bmatrix} = \begin{bmatrix} A\mathbf{x} + 0 \\ 0 + 1 \end{bmatrix} = \begin{bmatrix} A\mathbf{x} \\ 1 \end{bmatrix},
> $$
>
> the homogeneous coordinates of $A\mathbf{x}$. (c) If $M_1$ and $M_2$ represent two transformations, applying $M_1$ and then $M_2$ to $(x, y, 1)$ gives $M_2(M_1\mathbf{v}) = (M_2M_1)\mathbf{v}$ by [[§12 Matrix Operations#^thm-12-2|Theorem §12.2]], and the last coordinate stays $1$ at each step.

^pf-20-1

*Uses:* [[§17 Partitioned Matrices#^prop-17-2|§17.2]], [[§12 Matrix Operations#^thm-12-2|§12.2]]

> [!example] Example §20.2: Composite Transformations in Homogeneous Coordinates
> **(a)** Find the $3 \times 3$ matrix of the composite transformation: a scaling by $.3$, then a rotation of $90^\circ$ about the origin, and finally a translation that adds $(-.5, 2)$ to each point of a figure.
>
> For $\varphi = \pi/2$, $\sin\varphi = 1$ and $\cos\varphi = 0$. By [[§20 Applications to Computer Graphics#^prop-20-1|Proposition §20.1]], the three steps take $(x, y, 1)$ successively to
>
> $$
> \begin{bmatrix} .3 & 0 & 0 \\ 0 & .3 & 0 \\ 0 & 0 & 1 \end{bmatrix}\begin{bmatrix} x \\ y \\ 1 \end{bmatrix}, \qquad
> \begin{bmatrix} 0 & -1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{bmatrix}\begin{bmatrix} .3 & 0 & 0 \\ 0 & .3 & 0 \\ 0 & 0 & 1 \end{bmatrix}\begin{bmatrix} x \\ y \\ 1 \end{bmatrix}, \qquad
> \begin{bmatrix} 1 & 0 & -.5 \\ 0 & 1 & 2 \\ 0 & 0 & 1 \end{bmatrix}\begin{bmatrix} 0 & -1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{bmatrix}\begin{bmatrix} .3 & 0 & 0 \\ 0 & .3 & 0 \\ 0 & 0 & 1 \end{bmatrix}\begin{bmatrix} x \\ y \\ 1 \end{bmatrix} .
> $$
>
> The matrix of the composite is
>
> $$
> \begin{bmatrix} 1 & 0 & -.5 \\ 0 & 1 & 2 \\ 0 & 0 & 1 \end{bmatrix}\begin{bmatrix} 0 & -1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{bmatrix}\begin{bmatrix} .3 & 0 & 0 \\ 0 & .3 & 0 \\ 0 & 0 & 1 \end{bmatrix}
> = \begin{bmatrix} 0 & -1 & -.5 \\ 1 & 0 & 2 \\ 0 & 0 & 1 \end{bmatrix}\begin{bmatrix} .3 & 0 & 0 \\ 0 & .3 & 0 \\ 0 & 0 & 1 \end{bmatrix}
> = \begin{bmatrix} 0 & -.3 & -.5 \\ .3 & 0 & 2 \\ 0 & 0 & 1 \end{bmatrix} .
> $$
>
> **(b)** Rotation of a figure about a point $\mathbf{p} = (p_1, p_2)$ through an angle $\varphi$ is done by translating the figure by $-\mathbf{p}$, rotating about the origin, and translating back by $\mathbf{p}$. With $c = \cos\varphi$, $s = \sin\varphi$, its matrix in homogeneous coordinates is
>
> $$
> \begin{bmatrix} 1 & 0 & p_1 \\ 0 & 1 & p_2 \\ 0 & 0 & 1 \end{bmatrix}\begin{bmatrix} c & -s & 0 \\ s & c & 0 \\ 0 & 0 & 1 \end{bmatrix}\begin{bmatrix} 1 & 0 & -p_1 \\ 0 & 1 & -p_2 \\ 0 & 0 & 1 \end{bmatrix}
> = \begin{bmatrix} 1 & 0 & p_1 \\ 0 & 1 & p_2 \\ 0 & 0 & 1 \end{bmatrix}\begin{bmatrix} c & -s & -cp_1 + sp_2 \\ s & c & -sp_1 - cp_2 \\ 0 & 0 & 1 \end{bmatrix}
> = \begin{bmatrix} c & -s & p_1 - cp_1 + sp_2 \\ s & c & p_2 - sp_1 - cp_2 \\ 0 & 0 & 1 \end{bmatrix} .
> $$
>
> As a check, $\mathbf{p}$ itself is fixed: the first coordinate of the image of $(p_1, p_2, 1)$ is $cp_1 - sp_2 + p_1 - cp_1 + sp_2 = p_1$, and similarly the second is $p_2$.
>
> For instance (Lay's Practice Problem), to rotate points through $-30^\circ$ about $\mathbf{p} = (-2, 6)$, take $c = \cos(-30^\circ) = \sqrt3/2$ and $s = \sin(-30^\circ) = -.5$: then $p_1 - cp_1 + sp_2 = -2 + \sqrt3 - 3 = \sqrt3 - 5$ and $p_2 - sp_1 - cp_2 = 6 - 1 - 3\sqrt3 = 5 - 3\sqrt3$, so the matrix is
>
> $$
> \begin{bmatrix} 1 & 0 & -2 \\ 0 & 1 & 6 \\ 0 & 0 & 1 \end{bmatrix}\begin{bmatrix} \sqrt3/2 & 1/2 & 0 \\ -1/2 & \sqrt3/2 & 0 \\ 0 & 0 & 1 \end{bmatrix}\begin{bmatrix} 1 & 0 & 2 \\ 0 & 1 & -6 \\ 0 & 0 & 1 \end{bmatrix}
> = \begin{bmatrix} \sqrt3/2 & 1/2 & \sqrt3 - 5 \\ -1/2 & \sqrt3/2 & -3\sqrt3 + 5 \\ 0 & 0 & 1 \end{bmatrix} .
> $$
>
> *Lay: Example 2.7.6; 2.7, Practice Problem*

^ex-20-2

## 3D Computer Graphics

Three-dimensional graphics is used, for instance, in molecular modeling: a biologist rotates and translates a simulated drug molecule to fit it into an active site of a protein, increasingly in virtual reality, with tactile feedback or a helmet with one small screen for each eye.

> [!definition] Definition §20.2: Homogeneous Coordinates in Space
> By analogy with the 2D case, $(x, y, z, 1)$ are homogeneous coordinates for the point $(x, y, z)$ in $\mathbb{R}^3$. More generally, $(X, Y, Z, H)$ are **homogeneous coordinates** for $(x, y, z)$ if $H \ne 0$ and
>
> $$
> x = \frac{X}{H}, \qquad y = \frac{Y}{H}, \qquad z = \frac{Z}{H} . \tag{1}
> $$
>
> So every nonzero scalar multiple of $(x, y, z, 1)$ gives homogeneous coordinates for $(x, y, z)$. For instance, both $(10, -6, 14, 2)$ and $(-15, 9, -21, -3)$ are homogeneous coordinates for $(5, -3, 7)$.
>
> *Lay: 2.7 (text)*

^def-20-2

> [!example] Example §20.3: Rotating and Translating in Space
> Give $4 \times 4$ matrices for (a) the rotation about the $y$-axis through $30^\circ$, and (b) the translation by $\mathbf{p} = (-6, 4, 5)$. (By convention, a positive angle is counterclockwise when looking toward the origin from the positive half of the axis of rotation, here the $y$-axis.)
>
> **(a)** First the $3 \times 3$ rotation matrix, column by column. $\mathbf{e}_1$ rotates down toward the negative $z$-axis, stopping at $(\cos 30^\circ, 0, -\sin 30^\circ) = (\sqrt3/2, 0, -.5)$. $\mathbf{e}_2$, on the axis, does not move. $\mathbf{e}_3$ rotates down toward the positive $x$-axis, stopping at $(\sin 30^\circ, 0, \cos 30^\circ) = (.5, 0, \sqrt3/2)$. By [[§10 The Matrix of a Linear Transformation#^thm-10-1|Theorem §10.1]] the standard matrix is
>
> $$
> \begin{bmatrix} \sqrt3/2 & 0 & .5 \\ 0 & 1 & 0 \\ -.5 & 0 & \sqrt3/2 \end{bmatrix}, \qquad\text{so in homogeneous coordinates}\qquad
> A = \begin{bmatrix} \sqrt3/2 & 0 & .5 & 0 \\ 0 & 1 & 0 & 0 \\ -.5 & 0 & \sqrt3/2 & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix} .
> $$
>
> **(b)** We want $(x, y, z, 1) \mapsto (x - 6, y + 4, z + 5, 1)$. The matrix that does this is
>
> $$
> \begin{bmatrix} 1 & 0 & 0 & -6 \\ 0 & 1 & 0 & 4 \\ 0 & 0 & 1 & 5 \\ 0 & 0 & 0 & 1 \end{bmatrix} .
> $$
>
> *Lay: Example 2.7.7*

^ex-20-3

## Perspective Projections

A three-dimensional object is shown on the two-dimensional screen by projecting it onto a viewing plane. For simplicity let the $xy$-plane be the screen, and put the viewer's eye on the positive $z$-axis at $(0, 0, d)$.

> [!definition] Definition §20.3: Perspective Projection
> The **perspective projection** with **center of projection** $(0, 0, d)$ maps each point $(x, y, z)$ (with $z \ne d$) onto the image point $(x^{\ast}, y^{\ast}, 0)$ such that the two points and the center of projection lie on one line.
>
> *Lay: 2.7 (text)*

^def-20-3

> [!theorem] Proposition §20.2: The Matrix of a Perspective Projection
> The perspective projection with center $(0, 0, d)$ is
>
> $$
> x^* = \frac{x}{1 - z/d}, \qquad y^* = \frac{y}{1 - z/d},
> $$
>
> and in homogeneous coordinates it is given by the matrix
>
> $$
> P = \begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & -1/d & 1 \end{bmatrix}, \qquad
> P\begin{bmatrix} x \\ y \\ z \\ 1 \end{bmatrix} = \begin{bmatrix} x \\ y \\ 0 \\ 1 - z/d \end{bmatrix} .
> $$
>
> *Lay: 2.7 (text)*

^prop-20-2

> [!proof]+ Proof
> Look at the $xz$-plane. The line from the eye $(0, 0, d)$ through $(x, \cdot, z)$ meets the screen $z = 0$ at $x^*$. The right triangle with legs $d$ (from the eye down to the screen) and $x^*$ is similar to the right triangle with legs $d - z$ (from the eye down to the level of the point) and $x$. So
>
> $$
> \frac{x^*}{d} = \frac{x}{d - z} \qquad\text{and}\qquad x^* = \frac{dx}{d - z} = \frac{x}{1 - z/d} .
> $$
>
> The same argument in the $yz$-plane gives $y^* = y/(1 - z/d)$. (The picture has $0 < x$ and $z < d$; the formulas hold for all points with $z \ne d$, as the parametrization shows: the line through $(0, 0, d)$ and $(x, y, z)$ consists of the points $(tx,\ ty,\ d + t(z - d))$, and the third coordinate is $0$ exactly when $t = d/(d - z)$, which gives $x^* = dx/(d - z)$ and $y^* = dy/(d - z)$.) So $(x, y, z, 1)$ must go to $\big(\frac{x}{1 - z/d}, \frac{y}{1 - z/d}, 0, 1\big)$. Scaling by $1 - z/d$, we may instead use $(x, y, 0, 1 - z/d)$ as homogeneous coordinates for the image ([[§20 Applications to Computer Graphics#^def-20-2|Definition §20.2]]), and the displayed product shows that $P$ produces exactly these coordinates.

^pf-20-2

*Uses:* [[§20 Applications to Computer Graphics#^def-20-2|Def. §20.2]], [[§20 Applications to Computer Graphics#^def-20-3|Def. §20.3]]

> [!example] Example §20.4: The Perspective Image of a Box
> Let $S$ be the box with vertices $(3, 1, 5)$, $(5, 1, 5)$, $(5, 0, 5)$, $(3, 0, 5)$, $(3, 1, 4)$, $(5, 1, 4)$, $(5, 0, 4)$, $(3, 0, 4)$. Find the image of $S$ under the perspective projection with center $(0, 0, 10)$.
>
> Let $D$ be the data matrix of $S$ in homogeneous coordinates. With $d = 10$, the data matrix of the image is
>
> $$
> PD = \begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & -1/10 & 1 \end{bmatrix}
> \begin{bmatrix} 3 & 5 & 5 & 3 & 3 & 5 & 5 & 3 \\ 1 & 1 & 0 & 0 & 1 & 1 & 0 & 0 \\ 5 & 5 & 5 & 5 & 4 & 4 & 4 & 4 \\ 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 \end{bmatrix}
> = \begin{bmatrix} 3 & 5 & 5 & 3 & 3 & 5 & 5 & 3 \\ 1 & 1 & 0 & 0 & 1 & 1 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ .5 & .5 & .5 & .5 & .6 & .6 & .6 & .6 \end{bmatrix} .
> $$
>
> (The last row is $1 - z/10$: $.5$ for $z = 5$, $.6$ for $z = 4$.) To get $\mathbb{R}^3$ coordinates, use (1): divide the top three entries of each column by its fourth entry. For example vertex 1 gives $(3/.5, 1/.5, 0) = (6, 2, 0)$ and vertex 6 gives $(5/.6, 1/.6, 0) \approx (8.3, 1.7, 0)$. Altogether the image vertices are
>
> $$
> \begin{bmatrix} 6 & 10 & 10 & 6 & 5 & 8.3 & 8.3 & 5 \\ 2 & 2 & 0 & 0 & 1.7 & 1.7 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \end{bmatrix} .
> $$
>
> The near face ($z = 5$, closer to the eye) appears larger than the far face ($z = 4$), as perspective demands.
>
> *Lay: Example 2.7.8*

^ex-20-4

> [!remark]- Remark: Numerical Note
> Continuous movement of 3D objects requires intensive computation with $4 \times 4$ matrices, particularly when surfaces are rendered realistically with texture and lighting. High-end graphics boards have $4 \times 4$ matrix operations and graphics algorithms built into their chips, and perform the billions of matrix multiplications per second needed for realistic color animation in 3D games. (Further reading: Foley, van Dam, Feiner and Hughes, *Computer Graphics: Principles and Practice*, Chapters 5 and 6.)

^rem-20-2
