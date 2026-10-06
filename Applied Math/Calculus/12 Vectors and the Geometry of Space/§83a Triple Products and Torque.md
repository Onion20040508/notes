---
type: section
subject: "[[Calculus]]"
chapter: 12
section: "83a"
stewart: "12.4"
aliases: ["Stewart 12.4 (cont.)"]
tags: [calculus, math233]
---
← [[§83 The Cross Product]] · ↑ [[· 12 Vectors and the Geometry of Space]] · [[§84 Equations of Lines and Planes]] →

*Stewart, Section 12.4 · MATH 233 (UMass, Spring 2023): Midterm 1 Practice Questions (Q3), Practice Exam 1 (Q1(a)), Exam 1 Review (Q1(d)–(g)), SI Midterm 1 Problem Set (Q3(a), Q5(a)).*

The scalar triple product $\mathbf{a} \cdot (\mathbf{b} \times \mathbf{c})$ is a determinant and measures the volume of a parallelepiped. The section ends with torque, the cross product of a position vector and a force.

## Triple Products

> [!definition] Definition §83.3: Scalar Triple Product
> The product $\mathbf{a} \cdot (\mathbf{b} \times \mathbf{c})$ of Property 5 is the **scalar triple product** of $\mathbf{a}$, $\mathbf{b}$ and $\mathbf{c}$.
>
> *Stewart: 12.4 (text)*

^def-83-3

> [!definition] Definition §83.4: Vector Triple Product
> The product $\mathbf{a} \times (\mathbf{b} \times \mathbf{c})$ of Property 6 is the **vector triple product**.
>
> *Stewart: 12.4 (text)*

^def-83-new1

> [!definition] Definition §83.5: Coplanar Vectors
> Vectors that lie in the same plane (when represented with a common initial point) are **coplanar**.
>
> *Stewart: 12.4 (text)*

^def-83-new2

> [!theorem] Theorem §83.9: The Scalar Triple Product as a Determinant
> $$
> \mathbf{a} \cdot (\mathbf{b} \times \mathbf{c}) = \begin{vmatrix} a_1 & a_2 & a_3 \\ b_1 & b_2 & b_3 \\ c_1 & c_2 & c_3 \end{vmatrix} .
> $$
>
> *Stewart: 12.4, Equation 13*

^thm-83-9

> [!proof]+ Proof
> The first line of (12) in the proof of [[§83 The Cross Product#^thm-83-8|Theorem §83.8]] is $a_1\begin{vmatrix} b_2 & b_3 \\ c_2 & c_3 \end{vmatrix} - a_2\begin{vmatrix} b_1 & b_3 \\ c_1 & c_3 \end{vmatrix} + a_3\begin{vmatrix} b_1 & b_2 \\ c_1 & c_2 \end{vmatrix}$, which is the determinant by [[§83 The Cross Product#^def-83-2|Definition §83.2]].

^pf-83-9

*Uses:* [[§83 The Cross Product#^thm-83-8|§83.8]], [[§83 The Cross Product#^def-83-2|Def. §83.2]]

> [!theorem] Theorem §83.10: Volume of a Parallelepiped
> The volume of the parallelepiped determined by the vectors $\mathbf{a}$, $\mathbf{b}$ and $\mathbf{c}$ is the magnitude of their scalar triple product:
>
> $$
> V = |\mathbf{a} \cdot (\mathbf{b} \times \mathbf{c})| .
> $$
>
> In particular, if $\mathbf{a} \cdot (\mathbf{b} \times \mathbf{c}) = 0$ then the parallelepiped is flat: $\mathbf{a}$, $\mathbf{b}$, $\mathbf{c}$ are coplanar.
>
> *Stewart: 12.4, Equation 14*

^thm-83-10

> [!proof]+ Proof
> Take the parallelogram spanned by $\mathbf{b}$ and $\mathbf{c}$ as the base; its area is $A = |\mathbf{b} \times \mathbf{c}|$ by [[§83 The Cross Product#^cor-83-6|Corollary §83.6]]. The vector $\mathbf{b} \times \mathbf{c}$ is perpendicular to the base ([[§83 The Cross Product#^thm-83-2|Theorem §83.2]]). If $\theta$ is the angle between $\mathbf{a}$ and $\mathbf{b} \times \mathbf{c}$, the height of the parallelepiped is $h = |\mathbf{a}||\cos\theta|$ (the absolute value is needed in case $\theta > \pi/2$). Therefore, by [[§82 The Dot Product#^thm-82-2|Theorem §82.2]],
>
> $$
> V = Ah = |\mathbf{b} \times \mathbf{c}|\,|\mathbf{a}|\,|\cos\theta| = |\mathbf{a} \cdot (\mathbf{b} \times \mathbf{c})| .
> $$
>
> (If $\mathbf{b} \times \mathbf{c} = \mathbf{0}$, then $\mathbf{b}$ and $\mathbf{c}$ are parallel or one is $\mathbf{0}$, the base has area $0$, and both sides are $0$.)

^pf-83-10

*Uses:* [[§83 The Cross Product#^cor-83-6|§83.6]], [[§83 The Cross Product#^thm-83-2|§83.2]], [[§82 The Dot Product#^thm-82-2|§82.2]]

> [!remark]- Connections
> - Together with [[§83a Triple Products and Torque#^thm-83-9|Theorem §83.9]]: $|\det|$ of the matrix with rows $\mathbf{a}, \mathbf{b}, \mathbf{c}$ is the volume of the image of the unit cube, the case $n = 3$ of [[§34 Determinants#^ladr-9-61|LADR 9.61]] ($T$ changes volume by the factor $|\det T|$); the general determinant formula is [[§34 Determinants#^ladr-9-46|LADR 9.46]].
> - Matrix version, also of [[§83 The Cross Product#^cor-83-6|Corollary §83.6]]: [[§22 Cramer’s Rule, Volume, and Linear Transformations#^thm-22-4|235 Thm. §22.4]] (area and volume as $|\det A|$ for the matrix with columns the edge vectors, proved by column operations), worked in [[§22 Cramer’s Rule, Volume, and Linear Transformations#^ex-22-4|235 Ex. §22.4]].

> [!example] Example §83.3: Triple Products by the Rules
> Let $\mathbf{a} = \mathbf{i} + \mathbf{j} + \mathbf{k}$, $\mathbf{b} = 3\mathbf{i} - 2\mathbf{j} + \mathbf{k}$, $\mathbf{c} = \mathbf{j} - 5\mathbf{k}$. Find $|\mathbf{b} \times \mathbf{c}|$, $\mathbf{a} \cdot (\mathbf{b} \times \mathbf{c})$, $\mathbf{c} \times \mathbf{c}$ and $\mathbf{a} \times (\mathbf{b} \times \mathbf{c})$.
>
> $$
> \mathbf{b} \times \mathbf{c} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ 3 & -2 & 1 \\ 0 & 1 & -5 \end{vmatrix} = (10 - 1)\mathbf{i} - (-15 - 0)\mathbf{j} + (3 - 0)\mathbf{k} = \langle 9, 15, 3 \rangle ,
> $$
>
> so $|\mathbf{b} \times \mathbf{c}| = \sqrt{81 + 225 + 9} = \sqrt{315} = 3\sqrt{35}$ and $\mathbf{a} \cdot (\mathbf{b} \times \mathbf{c}) = 9 + 15 + 3 = 27$. By [[§83 The Cross Product#^ex-83-1|Example §83.1]](b), $\mathbf{c} \times \mathbf{c} = \mathbf{0}$ with no computation. For the vector triple product, Property 6 of [[§83 The Cross Product#^thm-83-8|Theorem §83.8]] avoids a second cross product: $\mathbf{a} \cdot \mathbf{c} = 0 + 1 - 5 = -4$ and $\mathbf{a} \cdot \mathbf{b} = 3 - 2 + 1 = 2$, so
>
> $$
> \mathbf{a} \times (\mathbf{b} \times \mathbf{c}) = (\mathbf{a} \cdot \mathbf{c})\mathbf{b} - (\mathbf{a} \cdot \mathbf{b})\mathbf{c} = -4\langle 3, -2, 1 \rangle - 2\langle 0, 1, -5 \rangle = \langle -12, 6, 6 \rangle .
> $$
>
> Check directly: $\langle 1, 1, 1 \rangle \times \langle 9, 15, 3 \rangle = \langle 3 - 15,\ 9 - 3,\ 15 - 9 \rangle = \langle -12, 6, 6 \rangle$.
>
> *Source: 233 Exam 1 Review, Q1(d)–(g)*

^ex-83-3

> [!example] Example §83.4: Coplanar Vectors and a Volume
> **(a)** Show that $\mathbf{a} = \langle 1, 4, -7 \rangle$, $\mathbf{b} = \langle 2, -1, 4 \rangle$, $\mathbf{c} = \langle 0, -9, 18 \rangle$ are coplanar. By [[§83a Triple Products and Torque#^thm-83-9|Theorem §83.9]],
>
> $$
> \mathbf{a} \cdot (\mathbf{b} \times \mathbf{c}) = \begin{vmatrix} 1 & 4 & -7 \\ 2 & -1 & 4 \\ 0 & -9 & 18 \end{vmatrix}
> = 1\begin{vmatrix} -1 & 4 \\ -9 & 18 \end{vmatrix} - 4\begin{vmatrix} 2 & 4 \\ 0 & 18 \end{vmatrix} - 7\begin{vmatrix} 2 & -1 \\ 0 & -9 \end{vmatrix}
> = 1(18) - 4(36) - 7(-18) = 0 ,
> $$
>
> so the parallelepiped they determine has volume $0$ ([[§83a Triple Products and Torque#^thm-83-10|Theorem §83.10]]): they are coplanar.
>
> **(b)** Find the volume of the parallelepiped with vertices $A(3, 4, 0)$, $B(3, 1, -2)$, $C(4, 5, -3)$, $D(1, 0, -1)$, where $B$, $C$, $D$ are all adjacent to $A$. The edges from $A$ are $\overrightarrow{AB} = \langle 0, -3, -2 \rangle$, $\overrightarrow{AC} = \langle 1, 1, -3 \rangle$, $\overrightarrow{AD} = \langle -2, -4, -1 \rangle$, and
>
> $$
> \begin{vmatrix} 0 & -3 & -2 \\ 1 & 1 & -3 \\ -2 & -4 & -1 \end{vmatrix} = 0 - (-3)\big(1(-1) - (-3)(-2)\big) + (-2)\big(1(-4) - 1(-2)\big) = 3(-7) + (-2)(-2) = -17 ,
> $$
>
> so $V = |-17| = 17$.
>
> *Stewart: Example 12.4.5*
> *Source: 233 SI Midterm 1 Problem Set, Q3(a)*

^ex-83-4

> [!remark] Remark: The Vector Triple Product and Kepler
> Property 6 is used in [[§89 Motion in Space꞉ Velocity and Acceleration#^thm-89-6|Theorem §89.6]] to derive Kepler's First Law of planetary motion.

^rem-83-4

## Application: Torque

> [!definition] Definition §83.4: Torque
> Let a force $\mathbf{F}$ act on a rigid body at a point with position vector $\mathbf{r}$. The **torque** $\boldsymbol{\tau}$ (relative to the origin) is
>
> $$
> \boldsymbol{\tau} = \mathbf{r} \times \mathbf{F} .
> $$
>
> It measures the tendency of the body to rotate about the origin, and its direction is the axis of rotation. By [[§83 The Cross Product#^thm-83-4|Theorem §83.4]], $|\boldsymbol{\tau}| = |\mathbf{r}||\mathbf{F}|\sin\theta$, where $\theta$ is the angle between $\mathbf{r}$ and $\mathbf{F}$: only the component $|\mathbf{F}|\sin\theta$ of the force perpendicular to $\mathbf{r}$ causes rotation.
>
> *Stewart: 12.4 (text)*

^def-83-4

> [!example] Example §83.5: Tightening a Bolt
> A bolt is tightened by applying a $40$-N force to a $0.25$-m wrench, at an angle of $75^\circ$ to the wrench. The magnitude of the torque about the center of the bolt is
>
> $$
> |\boldsymbol{\tau}| = |\mathbf{r} \times \mathbf{F}| = |\mathbf{r}||\mathbf{F}|\sin 75^\circ = (0.25)(40)\sin 75^\circ = 10\sin 75^\circ \approx 9.66\ \text{N}\cdot\text{m} .
> $$
>
> If the bolt is right-threaded, the torque vector is $\boldsymbol{\tau} = |\boldsymbol{\tau}|\,\mathbf{n} \approx 9.66\,\mathbf{n}$, where $\mathbf{n}$ is a unit vector directed down into the page (right-hand rule).
>
> *Stewart: Example 12.4.6*

^ex-83-5
