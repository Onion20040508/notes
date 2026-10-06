---
type: section
subject: "[[Complex Variables]]"
chapter: 8
section: "96★"
bc: "96"
aliases: ["B&C 96"]
tags: [complex-variables, math342, extension]
---
← [[§95a The Integral of 1∕(√x (x² + 1))]] · ↑ [[· 8★ Mapping by Elementary Functions]] · [[§97★ The Transformation w = 1∕z]] →

*Brown–Churchill, Section 96.*
★ *Beyond MAT 342: the course skipped this section or left it optional; it is included from Brown–Churchill.*

Chapter 8 returns to the picture of [[§13 Functions and Mappings|§13]] and [[§14 The Mapping w = z²|§14]]: a function of $z$ is studied through the way it carries curves and regions of the $z$ plane onto the $w$ plane. The simplest maps are the linear ones, $w = Az + B$, which rotate, stretch and shift the plane without changing the shape of any figure. They are the building blocks of every later construction: a linear fractional transformation is two of them with $1/z$ in between ([[§99★ Linear Fractional Transformations|§99]]), and in the applications of Chapters 10–11 they move a region into standard position before a harder map is applied.

## Rotation, Expansion and Translation

> [!definition] Definition §96.1: Linear Transformation
> Let $A$ and $B$ be complex constants with $A \ne 0$. The mapping
>
> $$
> w = Az + B \qquad (A \ne 0) \qquad (5)
> $$
>
> is the general (nonconstant) **linear transformation**. Its two special cases are
>
> $$
> w = Az \quad (1) \qquad\text{and}\qquad w = z + B , \quad (3)
> $$
>
> and (5) is the composition of $Z = Az$ followed by $w = Z + B$.
>
> *B&C: Sec. 96 (text)*

^def-96-1

> [!theorem] Proposition §96.1: Geometry of a Linear Transformation
> Write $A = a\exp(i\alpha)$ with $a = |A| > 0$, and $z = r\exp(i\theta)$.
> 1. The mapping $w = Az$ sends $z \ne 0$ to
>
>    $$
>    w = (ar)\exp[i(\alpha + \theta)] : \qquad (2)
>    $$
>
>    it expands or contracts the radius vector of $z$ by the factor $a$ and rotates it through the angle $\alpha$ about the origin. The image of any region is geometrically similar to it.
> 2. With $w = u + iv$, $z = x + iy$ and $B = b_1 + ib_2$, the mapping $w = z + B$ sends $(x, y)$ to
>
>    $$
>    (u, v) = (x + b_1,\ y + b_2) , \qquad (4)
>    $$
>
>    the translation by the vector representing $B$. The image of any region is congruent to it.
> 3. Consequently $w = Az + B$ is, for $z \ne 0$, an expansion or contraction and a rotation, followed by a translation.
>
> *B&C: Sec. 96 (text)*

^prop-96-1

> [!proof]+ Proof
> 1. Moduli multiply and arguments add in exponential form: $Az = a e^{i\alpha} \cdot r e^{i\theta} = (ar)e^{i(\alpha + \theta)}$, which is (2). For any two points, $|Az_1 - Az_2| = |A|\,|z_1 - z_2| = a|z_1 - z_2|$, so every distance in a figure is multiplied by the same factor $a$; together with the rotation this is exactly a similarity. (B&C asserts the similarity; this distance identity is why it holds.)
> 2. $z + B = (x + b_1) + i(y + b_2)$, which is (4). Here $|(z_1 + B) - (z_2 + B)| = |z_1 - z_2|$: distances are unchanged, so images are congruent.
> 3. By Definition §96.1, $w = Az + B$ is $Z = Az$ followed by $w = Z + B$; apply parts 1 and 2 in turn.

^pf-96-1

*Uses:* [[§96★ Linear Transformations#^def-96-1|Def. §96.1]], [[§8 Products and Powers in Exponential Form#^thm-8-1|§8.1]] (products in exponential form)

> [!remark]- Connections
> - In real coordinates, multiplication by $A = a_1 + ia_2$ is the matrix $\begin{bmatrix} a_1 & -a_2 \\ a_2 & a_1\end{bmatrix}$, a scaling by $|A|$ composed with a rotation through $\operatorname{Arg} A$: [[§44 Complex Eigenvalues#^prop-44-3|235 Prop. §44.3]]. So $w = Az + B$ is an affine map of $\mathbb{R}^2$ whose linear part is a rotation–scaling matrix.

> [!remark] Remark: Method — Building a Linear Transformation Between Two Regions
> To carry a region (strip, half plane, rectangle) onto a congruent or similar one:
> 1. **Rotate.** Choose $\alpha$ so that the boundary directions of the first region turn into those of the second. A rotation through $\pi/2$ is multiplication by $i$, through $-\pi/4$ multiplication by $e^{-i\pi/4}$.
> 2. **Scale.** Choose $a > 0$ as the ratio of corresponding widths. Then $A = ae^{i\alpha}$.
> 3. **Translate.** Choose $B$ so that one boundary point lands where it should.
> 4. **Check** the images of a corner or a boundary line, and of one interior point, by writing $u$ and $v$ in terms of $x$ and $y$.
>
> To find the image of a given region instead, solve $w = Az + B$ for $z = (w - B)/A$ and substitute into the inequalities that describe the region.

^rem-96-1

## Examples

> [!example] Example §96.1: A Rectangle under w = (1 + i)z + 2
> Find the image of the rectangle with vertices $0$, $1$, $1 + 2i$, $2i$ under
>
> $$
> w = (1 + i)z + 2 . \qquad (6)
> $$
>
> Write (6) as the composition
>
> $$
> Z = (1 + i)z \qquad\text{and}\qquad w = Z + 2 . \qquad (7)
> $$
>
> Since $1 + i = \sqrt2\exp(i\pi/4)$, the first map is $Z = (\sqrt2 r)\exp[i(\theta + \pi/4)]$: it expands each radius vector by $\sqrt2$ and rotates it counterclockwise through $\pi/4$. The second is a translation two units to the right. On the vertices:
>
> | $z$ | $Z = (1 + i)z$ | $w = Z + 2$ |
> |---|---|---|
> | $0$ | $0$ | $2$ |
> | $1$ | $1 + i$ | $3 + i$ |
> | $1 + 2i$ | $(1 + i)(1 + 2i) = -1 + 3i$ | $1 + 3i$ |
> | $2i$ | $-2 + 2i$ | $2i$ |
>
> The image is the rectangle with these four vertices: its sides have lengths $\sqrt2$ and $2\sqrt2$ (for example $|(3 + i) - 2| = \sqrt2$), the original lengths $1$ and $2$ times $\sqrt2$, and they make angles $\pi/4$ and $3\pi/4$ with the $u$ axis.
>
> *B&C: Sec. 96, Example*

^ex-96-1

![[m342-96-1.svg]]
*The rectangle $0 \le x \le 1$, $0 \le y \le 2$ under $w = (1 + i)z + 2$, in two steps: $Z = (1 + i)z$ stretches by $\sqrt2$ and turns by $\pi/4$ about $O$, then $w = Z + 2$ shifts two units right. The image is similar to the original, never distorted.*

> [!example] Example §96.2: Rotation by i
> **(a)** The map $w = iz$ is the rotation through $\pi/2$, because $i = 1 \cdot \exp(i\pi/2)$ (Proposition §96.1 with $a = 1$, $\alpha = \pi/2$). In coordinates, $iz = i(x + iy) = -y + ix$, so
>
> $$
> u = -y, \qquad v = x .
> $$
>
> The infinite strip $0 < x < 1$ ($y$ arbitrary) therefore goes onto $0 < v < 1$ ($u$ arbitrary): the vertical strip is turned into a horizontal one.
>
> **(b)** The map $w = iz + i$ has $u = -y$, $v = x + 1$. As $(x, y)$ runs over the half plane $x > 0$, $v = x + 1$ runs over $v > 1$ and $u = -y$ over all reals; and each $(u, v)$ with $v > 1$ comes from exactly one point, $x = v - 1 > 0$, $y = -u$. So $w = iz + i$ maps $x > 0$ onto the half plane $v > 1$.
>
> *B&C: Sec. 96, Exercises 1 and 2*

^ex-96-2

> [!example] Example §96.3: Constructing a Linear Map Between Two Strips
> Find a linear transformation that maps the semi-infinite strip $x > 0$, $0 < y < 2$ onto the strip $-1 < u < 1$, $v > 0$.
>
> Both strips have width $2$, so no scaling is needed. The first opens to the right and the second opens upward, so rotate through $\pi/2$: by Example §96.2, $Z = iz$ has $X = -y$, $Y = x$, and maps the strip onto $-2 < X < 0$, $Y > 0$. Translating one unit right gives the required strip. Hence
>
> $$
> w = iz + 1 , \qquad u = 1 - y, \quad v = x .
> $$
>
> Check: $0 < y < 2 \iff -1 < u < 1$, and $x > 0 \iff v > 0$; the corner $z = 0$ goes to $w = 1$ and the corner $z = 2i$ to $w = -1$.
>
> *B&C: Sec. 96, Exercise 3*

^ex-96-3

> [!example] Example §96.4: Half Planes under Rotation–Scalings
> **(a)** Under $w = (1 + i)z$, the inverse is $z = w/(1 + i) = \tfrac12(1 - i)(u + iv) = \tfrac12\big[(u + v) + i(v - u)\big]$, so $y = \tfrac12(v - u)$. The half plane $y > 0$ goes onto $v > u$, the half plane above the line $v = u$. This agrees with the geometry: the boundary $y = 0$ is turned through $\pi/4$ onto the line $v = u$.
>
> **(b)** Under $w = (1 - i)z$, the inverse is $z = w/(1 - i) = \tfrac12(1 + i)(u + iv) = \tfrac12\big[(u - v) + i(u + v)\big]$, so $y = \tfrac12(u + v)$. The half plane $y > 1$ goes onto $u + v > 2$. Check: $1 - i = \sqrt2\exp(-i\pi/4)$, and the boundary point $z = i$ goes to $(1 - i)i = 1 + i$, which lies on $u + v = 2$.
>
> *B&C: Sec. 96, Exercises 4 and 5*

^ex-96-4
