---
type: section
subject: "[[Applied Linear Algebra]]"
chapter: 3
section: "22a"
lay: "3.3"
aliases: ["Lay 3.3 (cont.)"]
tags: [applied-linear-algebra, math235]
---
← [[§22 Cramer’s Rule, Volume, and Linear Transformations]] · ↑ [[· 3 Determinants]] · [[§23 Vector Spaces and Subspaces]] →

*Lay, Section 3.3 · MATH 235 lectures L11, L12, L13.*

Geometrically, $|\det A|$ is the area (in $\mathbb{R}^2$) or volume (in $\mathbb{R}^3$) of the parallelogram or parallelepiped spanned by the columns of $A$, and the linear map $\mathbf{x} \mapsto A\mathbf{x}$ multiplies every area or volume by $|\det A|$. In multivariable calculus this factor becomes the Jacobian.

## Determinants as Area or Volume

Lengths, areas and volumes in $\mathbb{R}^2$ and $\mathbb{R}^3$ are taken in their usual Euclidean sense (length and distance in $\mathbb{R}^n$ are defined in [[§40 Inner Product, Length, and Orthogonality#^def-40-2|Definition §40.2]]).

> [!theorem] Lemma §22.3: Shears Preserve Area and Volume
> Let $\mathbf{a}_1$ and $\mathbf{a}_2$ be nonzero vectors in $\mathbb{R}^2$. Then for any scalar $c$, the area of the parallelogram determined by $\mathbf{a}_1$ and $\mathbf{a}_2$ equals the area of the parallelogram determined by $\mathbf{a}_1$ and $\mathbf{a}_2 + c\mathbf{a}_1$.
>
> Likewise in $\mathbb{R}^3$: the parallelepiped determined by $\mathbf{a}_1, \mathbf{a}_2, \mathbf{a}_3$ has the same volume as the one determined by $\mathbf{a}_1, \mathbf{a}_2 + c\mathbf{a}_1, \mathbf{a}_3$.
>
> *Lay: 3.3 (boxed statement in the proof of Theorem 9)*

^lem-22-3

> [!proof]+ Proof
> **In $\mathbb{R}^2$.** If $\mathbf{a}_2$ is a multiple of $\mathbf{a}_1$, so is $\mathbf{a}_2 + c\mathbf{a}_1$, and both parallelograms are degenerate, with area $0$. Otherwise, let $L$ be the line through $\mathbf{0}$ and $\mathbf{a}_1$. Then $\mathbf{a}_2 + L$ is the line through $\mathbf{a}_2$ parallel to $L$, and $\mathbf{a}_2 + c\mathbf{a}_1$ lies on it. The points $\mathbf{a}_2$ and $\mathbf{a}_2 + c\mathbf{a}_1$ therefore have the same perpendicular distance to $L$. The two parallelograms share the base from $\mathbf{0}$ to $\mathbf{a}_1$ and have the same height, so they have the same area.
>
> **In $\mathbb{R}^3$.** The volume of the parallelepiped is the area of its base, the parallelogram in the plane $\operatorname{Span}\{\mathbf{a}_1, \mathbf{a}_3\}$, times the altitude of $\mathbf{a}_2$ above that plane. The vector $\mathbf{a}_2 + c\mathbf{a}_1$ lies in the plane $\mathbf{a}_2 + \operatorname{Span}\{\mathbf{a}_1, \mathbf{a}_3\}$, which is parallel to $\operatorname{Span}\{\mathbf{a}_1, \mathbf{a}_3\}$, so it has the same altitude. Same base, same altitude: same volume. (If $\mathbf{a}_1, \mathbf{a}_3$ are dependent, both parallelepipeds lie in a plane and have volume $0$.)

^pf-22-3

*Uses:* only Euclidean geometry (area = base × height, volume = base area × altitude)

![[m235-22-1.svg]]
*[[§22a Determinants as Area or Volume#^lem-22-3|Lemma §22.3]] in $\mathbb{R}^2$. Adding $c\,\mathbf{a}_1$ to $\mathbf{a}_2$ slides the top side of the parallelogram along the line $\mathbf{a}_2 + L$, parallel to the base $L$. The blue and the green parallelogram share the base $\mathbf{0}\mathbf{a}_1$ and the height (red), so they have equal area. Algebraically this is a column replacement, which does not change the determinant either.*

> [!theorem] Theorem §22.4: Determinants as Area or Volume
> If $A$ is a $2 \times 2$ matrix, the area of the parallelogram determined by the columns of $A$ is $|\det A|$. If $A$ is a $3 \times 3$ matrix, the volume of the parallelepiped determined by the columns of $A$ is $|\det A|$.
>
> *Lay: Theorem 9 (3.3)*

^thm-22-4

> [!proof]+ Proof
> **$2 \times 2$.** The theorem is obviously true for a diagonal matrix:
>
> $$
> \left|\det\begin{bmatrix} a & 0 \\ 0 & d \end{bmatrix}\right| = |ad| = \text{area of the rectangle with sides } \begin{bmatrix} a \\ 0 \end{bmatrix}, \begin{bmatrix} 0 \\ d \end{bmatrix} .
> $$
>
> If the columns of $A = [\mathbf{a}_1 \ \mathbf{a}_2]$ are linearly dependent, the parallelogram is degenerate (a segment or a point) with area $0$, and $\det A = 0$ ([[§21 Properties of Determinants#^cor-21-5|Corollary §21.5]]). So let $A$ be invertible. It suffices to transform $A$ into a diagonal matrix by operations that change neither $|\det A|$ nor the area of the parallelogram. Column interchanges and column replacements do not change $|\det A|$ ([[§21 Properties of Determinants#^cor-21-7|Corollary §21.7]]). Column interchanges do not change the parallelogram at all, and column replacements do not change its area ([[§22a Determinants as Area or Volume#^lem-22-3|Lemma §22.3]]; all columns stay nonzero because the matrix stays invertible). Such operations do suffice to reach a diagonal matrix (Lay says this is "easy to see"; here is why): think of them as row operations on $A^T$. Row reduction with interchanges and replacements brings the invertible matrix $A^T$ to an echelon form with nonzero diagonal entries, and further replacements, using each diagonal entry from the bottom up to clear the entries above it, make it diagonal.
>
> **$3 \times 3$.** The same argument works. The theorem is obvious for a diagonal matrix, where the parallelepiped is a box with volume $|abc|$. If the columns are dependent, the parallelepiped is flat (volume $0$) and $\det A = 0$. Otherwise column interchanges and replacements turn $A$ into a diagonal matrix without changing $|\det A|$ or, by the $\mathbb{R}^3$ part of [[§22a Determinants as Area or Volume#^lem-22-3|Lemma §22.3]], the volume.

^pf-22-4

*Uses:* [[§22 Cramer’s Rule, Volume, and Linear Transformations#^lem-22-3|§22.3]], [[§21 Properties of Determinants#^cor-21-5|§21.5]], [[§21 Properties of Determinants#^cor-21-7|§21.7]], [[§20 Introduction to Determinants#^thm-20-2|§20.2]]

> [!remark]- Connections
> - In Calculus the same facts come from the cross product: area $= |\mathbf{a} \times \mathbf{b}|$ ([[§83 The Cross Product#^cor-83-6|Calc Cor. §83.6]]) and volume $= |\mathbf{a} \cdot (\mathbf{b} \times \mathbf{c})| = |\det|$ ([[§83 The Cross Product#^thm-83-10|Calc Thm. §83.10]]); the lecture writes $\det[\mathbf{v}_1 \ \mathbf{v}_2 \ \mathbf{v}_3] = (\mathbf{v}_1 \times \mathbf{v}_2) \cdot \mathbf{v}_3$.
> - Rigorous treatment in $\mathbb{R}^n$ for every measurable set ([[§10 Lebesgue Measurable Sets#^def-10-1|551 Def. §10.1]]): [[§34 Determinants#^ladr-9-61|LADR 9.61]] (proved via the singular value decomposition, [[§34 Determinants#^ladr-9-60|LADR 9.60]]); the sign of $\det$ records orientation, which $|\det|$ forgets.

> [!example] Example §22.4: Areas of Parallelograms, Triangles and Quadrilaterals
> **(a) A parallelogram given by its vertices.** Find the area of the parallelogram with vertices $(-2, -2)$, $(0, 3)$, $(4, -1)$, $(6, 4)$. First translate it so that one vertex is the origin: subtracting $(-2, -2)$ from each vertex gives $(0, 0)$, $(2, 5)$, $(6, 1)$, $(8, 6)$, a parallelogram with the same area. It is determined by the columns of
>
> $$
> A = \begin{bmatrix} 2 & 6 \\ 5 & 1 \end{bmatrix}, \qquad |\det A| = |2 - 30| = 28,
> $$
>
> so the area is $28$. (The fourth vertex $(8, 6) = (2, 5) + (6, 1)$ confirms which vertices are adjacent to the origin.)
>
> **(b) A triangle.** The triangle with vertices $(0, 0)$, $(1, 2)$, $(-3, 1)$ is half of the parallelogram with sides $\mathbf{v}_1 = (1, 2)$ and $\mathbf{v}_2 = (-3, 1)$, so its area is
>
> $$
> \frac12\left|\det\begin{bmatrix} 1 & -3 \\ 2 & 1 \end{bmatrix}\right| = \frac12(1 + 6) = \frac72 .
> $$
>
> For a triangle not at the origin, first translate one vertex to $\mathbf{0}$, as in (a).
>
> **(c) A quadrilateral.** Cut it along a diagonal into two triangles and add their areas. For the convex quadrilateral with vertices $(0,0)$, $(4,0)$, $(5,3)$, $(1,4)$ in order, the diagonal from $(0,0)$ to $(5,3)$ gives
>
> $$
> \frac12\left|\det\begin{bmatrix} 4 & 5 \\ 0 & 3 \end{bmatrix}\right| + \frac12\left|\det\begin{bmatrix} 5 & 1 \\ 3 & 4 \end{bmatrix}\right| = \frac12 \cdot 12 + \frac12 \cdot 17 = \frac{29}{2} .
> $$
>
> *Lay: Example 3.3.4*
> *Source: 235 lecture L11 (b); 235 checklist (c)*

^ex-22-4

## Linear Transformations

For a linear transformation $T$ and a set $S$ in its domain, $T(S)$ denotes the set of images of points of $S$. When $S$ is a region bounded by a parallelogram, $S$ is also called a parallelogram.

> [!theorem] Theorem §22.5: How a Linear Transformation Changes Area and Volume
> Let $T: \mathbb{R}^2 \to \mathbb{R}^2$ be the linear transformation determined by a $2 \times 2$ matrix $A$. If $S$ is a parallelogram in $\mathbb{R}^2$, then
>
> $$
> \{\text{area of } T(S)\} = |\det A| \cdot \{\text{area of } S\} . \qquad (5)
> $$
>
> If $T$ is determined by a $3 \times 3$ matrix $A$, and if $S$ is a parallelepiped in $\mathbb{R}^3$, then
>
> $$
> \{\text{volume of } T(S)\} = |\det A| \cdot \{\text{volume of } S\} . \qquad (6)
> $$
>
> *Lay: Theorem 10 (3.3)*

^thm-22-5

> [!proof]+ Proof
> **A parallelogram at the origin.** Let $A = [\mathbf{a}_1 \ \mathbf{a}_2]$. A parallelogram at the origin determined by vectors $\mathbf{b}_1$ and $\mathbf{b}_2$ has the form
>
> $$
> S = \{s_1\mathbf{b}_1 + s_2\mathbf{b}_2 : 0 \le s_1 \le 1,\ 0 \le s_2 \le 1\} .
> $$
>
> The image of $S$ under $T$ consists of the points
>
> $$
> T(s_1\mathbf{b}_1 + s_2\mathbf{b}_2) = s_1T(\mathbf{b}_1) + s_2T(\mathbf{b}_2) = s_1A\mathbf{b}_1 + s_2A\mathbf{b}_2, \qquad 0 \le s_1, s_2 \le 1 .
> $$
>
> So $T(S)$ is the parallelogram determined by the columns of $[A\mathbf{b}_1 \ A\mathbf{b}_2] = AB$, where $B = [\mathbf{b}_1 \ \mathbf{b}_2]$. By [[§22a Determinants as Area or Volume#^thm-22-4|Theorem §22.4]] and the multiplicative property,
>
> $$
> \{\text{area of } T(S)\} = |\det AB| = |\det A| \cdot |\det B| = |\det A| \cdot \{\text{area of } S\} . \qquad (7)
> $$
>
> **Any parallelogram.** An arbitrary parallelogram has the form $\mathbf{p} + S$ with $\mathbf{p}$ a vector and $S$ a parallelogram at the origin. By linearity $T(\mathbf{p} + \mathbf{s}) = T(\mathbf{p}) + T(\mathbf{s})$, so $T$ maps $\mathbf{p} + S$ onto the translate $T(\mathbf{p}) + T(S)$ (Lay's Exercise 26). Since translation does not affect area,
>
> $$
> \{\text{area of } T(\mathbf{p} + S)\} = \{\text{area of } T(\mathbf{p}) + T(S)\} = \{\text{area of } T(S)\} = |\det A| \cdot \{\text{area of } S\} = |\det A| \cdot \{\text{area of } \mathbf{p} + S\} .
> $$
>
> **The $3 \times 3$ case** (Lay: "analogous"). A parallelepiped at the origin is $S = \{s_1\mathbf{b}_1 + s_2\mathbf{b}_2 + s_3\mathbf{b}_3 : 0 \le s_i \le 1\}$, its image is the parallelepiped determined by the columns of $AB$ with $B = [\mathbf{b}_1 \ \mathbf{b}_2 \ \mathbf{b}_3]$, and $|\det AB| = |\det A|\,|\det B|$ gives (6) by [[§22a Determinants as Area or Volume#^thm-22-4|Theorem §22.4]]; translations are handled as before.

^pf-22-5

*Uses:* [[§22 Cramer’s Rule, Volume, and Linear Transformations#^thm-22-4|§22.4]], [[§21 Properties of Determinants#^thm-21-9|§21.9]], [[§8 Introduction to Linear Transformations#^def-8-3|Def. §8.3]] (linearity)

> [!theorem] Theorem §22.6: Regions of Finite Area or Volume
> The conclusions of [[§22a Determinants as Area or Volume#^thm-22-5|Theorem §22.5]] hold whenever $S$ is a region in $\mathbb{R}^2$ with finite area or a region in $\mathbb{R}^3$ with finite volume.
>
> *Lay: 3.3 (boxed generalization of Theorem 10)*

^thm-22-6

*Lay outlines the argument (below); a proof needs the theory of area and volume. See [[§15 Multivariable Integration#^prop-15-19|452 Prop. §15.19]] and [[§34 Determinants#^ladr-9-61|LADR 9.61]].*

> [!remark] Remark: Why It Works
> A planar region $R$ with finite area can be approximated by a grid of small squares lying inside $R$; making the squares small enough, the total area of the squares is as close as desired to the area of $R$. Under $T$, each small square goes to a small parallelogram whose area is $|\det A|$ times the area of the square ([[§22a Determinants as Area or Volume#^thm-22-5|Theorem §22.5]]). So if $R'$ is the union of the squares inside $R$, the area of $T(R')$ is $|\det A|$ times the area of $R'$, and the area of $T(R')$ is close to the area of $T(R)$. A limiting process gives $\{\text{area of } T(R)\} = |\det A| \cdot \{\text{area of } R\}$. The lecture draws the same picture for an arbitrary blob $D$, and composes: applying $S$ and then $T$ multiplies volume by $|\det S|$ and then by $|\det T|$ ([[§21 Properties of Determinants#^rem-21-4|§21, Remark: Why It Works]]).

^rem-22-3

> [!remark]- Connections
> - For a nonlinear map the factor $|\det A|$ becomes the absolute value of the Jacobian determinant in the change of variables formula: [[§106 Change of Variables in Multiple Integrals#^thm-106-1|Calc Thm. §106.1]] (double integrals), [[§15 Multivariable Integration#^thm-15-20|452 Thm. §15.20]] (in $\mathbb{R}^n$). This is the "expansion rate near the poles" of Lay's chapter introduction.

> [!example] Example §22.5: Areas and Volumes of Images
> **(a) The image of a parallelogram.** Let $S$ be the parallelogram determined by $\mathbf{b}_1 = (1, 3)$ and $\mathbf{b}_2 = (5, 1)$, and let $A = \begin{bmatrix} 1 & -0.1 \\ 0 & 2 \end{bmatrix}$. The area of $S$ is $\left|\det\begin{bmatrix} 1 & 5 \\ 3 & 1 \end{bmatrix}\right| = |1 - 15| = 14$, and $\det A = 2$. By [[§22a Determinants as Area or Volume#^thm-22-5|Theorem §22.5]] the area of the image of $S$ under $\mathbf{x} \mapsto A\mathbf{x}$ is $2 \cdot 14 = 28$. Directly: $A\mathbf{b}_1 = (0.7, 6)$, $A\mathbf{b}_2 = (4.9, 2)$ and $|0.7 \cdot 2 - 4.9 \cdot 6| = |1.4 - 29.4| = 28$.
>
> **(b) The area of an ellipse.** Let $a, b > 0$ and let $E$ be the region bounded by the ellipse $\dfrac{x_1^2}{a^2} + \dfrac{x_2^2}{b^2} = 1$. Then $E$ is the image of the unit disk $D$ under $T(\mathbf{u}) = A\mathbf{u}$ with $A = \begin{bmatrix} a & 0 \\ 0 & b \end{bmatrix}$: if $\mathbf{x} = A\mathbf{u}$, then $u_1 = x_1/a$ and $u_2 = x_2/b$, so $\mathbf{u}$ is in the unit disk ($u_1^2 + u_2^2 \le 1$) if and only if $\mathbf{x}$ is in $E$ ($(x_1/a)^2 + (x_2/b)^2 \le 1$). By [[§22a Determinants as Area or Volume#^thm-22-6|Theorem §22.6]],
>
> $$
> \{\text{area of ellipse}\} = \{\text{area of } T(D)\} = |\det A| \cdot \{\text{area of } D\} = ab \cdot \pi(1)^2 = \pi ab .
> $$
>
> **(c) The volume of an ellipsoid.** In the same way $A = \operatorname{diag}(a, b, c)$ maps the unit ball onto the solid ellipsoid $\frac{x_1^2}{a^2} + \frac{x_2^2}{b^2} + \frac{x_3^2}{c^2} \le 1$, so its volume is $abc \cdot \frac43\pi = \frac43\pi abc$.
>
> *Lay: Example 3.3.5; 3.3, Practice Problem and Exercise 31*

^ex-22-5

![[m235-22-2.svg]]
*[[§22a Determinants as Area or Volume#^ex-22-5|Example §22.5]](a). The parallelogram $S$ spanned by $\mathbf{b}_1, \mathbf{b}_2$ goes to the parallelogram $T(S)$ spanned by $A\mathbf{b}_1, A\mathbf{b}_2$, the columns of $AB$. Its area is $|\det AB| = |\det A|\,|\det B| = 2 \cdot 14$.*
