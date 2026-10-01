---
type: section
subject: "[[Applied Linear Algebra]]"
chapter: 5
section: 36
lay: "5.5"
aliases: ["Lay 5.5"]
tags: [applied-linear-algebra, math235]
---
← [[§35 Eigenvectors and Linear Transformations]] · ↑ [[· 5 Matrix Eigenvalues and Eigenvectors]] · [[§37 Discrete Dynamical Systems]] →

*Lay, Section 5.5 · MATH 235 lecture L21.*

The characteristic equation of an $n \times n$ matrix has exactly $n$ roots, counting multiplicities, once complex roots are allowed ([[§33 The Characteristic Equation#^rem-33-1|Remark: Complex Roots]]). A real matrix with a non-real eigenvalue has no real eigenvector for it, but letting the matrix act on $\mathbb{C}^n$ produces complex eigenvectors, and their real and imaginary parts carry real information. For a real matrix, complex eigenvalues come in conjugate pairs. The main theorem shows what a complex eigenvalue means geometrically. A real $2 \times 2$ matrix with eigenvalue $a - bi$, $b \ne 0$, is similar to $\begin{bmatrix} a & -b \\ b & a \end{bmatrix}$, a rotation combined with a scaling by $|\lambda|$. This "hidden rotation" explains the periodic, spiralling or vibrating behavior of many real systems. Complex arithmetic is in [[§53 Complex Numbers|§53]].

## Complex Eigenvalues and Eigenvectors

> [!definition] Definition §36.1: Complex Eigenvalue and Eigenvector
> Let $A$ be an $n \times n$ matrix, with real or complex entries, acting on the space $\mathbb{C}^n$ of $n$-tuples of complex numbers. The eigenvalue–eigenvector theory developed for $\mathbb{R}^n$ applies equally well to $\mathbb{C}^n$: a complex scalar $\lambda$ satisfies $\det(A - \lambda I) = 0$ if and only if there is a nonzero vector $\mathbf{x}$ in $\mathbb{C}^n$ such that $A\mathbf{x} = \lambda\mathbf{x}$. We call $\lambda$ a **(complex) eigenvalue** and $\mathbf{x}$ a **(complex) eigenvector** corresponding to $\lambda$.
>
> Matrix algebra carries over to complex entries and scalars; for instance, $A(c\mathbf{x} + d\mathbf{y}) = cA\mathbf{x} + dA\mathbf{y}$ for $\mathbf{x}, \mathbf{y}$ in $\mathbb{C}^n$ and $c, d$ in $\mathbb{C}$. The term **complex eigenvalue** refers to an eigenvalue $\lambda = a + bi$ with $b \ne 0$.
>
> *Lay: 5.5 (text)*

^def-36-1

> [!example] Example §36.1: Rotations Have No Real Eigenvectors
> **(a)** $A = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}$ rotates the plane $\mathbb{R}^2$ counterclockwise through a quarter-turn. Its action is periodic: after four quarter-turns every vector is back where it started. No nonzero vector is mapped to a multiple of itself, so $A$ has no eigenvectors in $\mathbb{R}^2$ and no real eigenvalues. Indeed, the characteristic equation is $\det\begin{bmatrix} -\lambda & -1 \\ 1 & -\lambda \end{bmatrix} = \lambda^2 + 1 = 0$, with only the complex roots $\lambda = i$ and $\lambda = -i$. On $\mathbb{C}^2$,
>
> $$
> \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}\begin{bmatrix} 1 \\ -i \end{bmatrix} = \begin{bmatrix} i \\ 1 \end{bmatrix} = i\begin{bmatrix} 1 \\ -i \end{bmatrix}, \qquad
> \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}\begin{bmatrix} 1 \\ i \end{bmatrix} = \begin{bmatrix} -i \\ 1 \end{bmatrix} = -i\begin{bmatrix} 1 \\ i \end{bmatrix} .
> $$
>
> So $i$ and $-i$ are eigenvalues, with eigenvectors $(1, -i)$ and $(1, i)$.
>
> **(b)** (Lecture.) $A = \begin{bmatrix} 0 & 1 \\ -4 & 0 \end{bmatrix}$ has $\det(A - \lambda I) = \det\begin{bmatrix} -\lambda & 1 \\ -4 & -\lambda \end{bmatrix} = \lambda^2 + 4 = (\lambda - 2i)(\lambda + 2i)$, using $i^2 = -1$. Its eigenvalues are the complex numbers $\pm 2i$.
>
> *Lay: Example 5.5.1; Source: 235 lecture L21*

^ex-36-1

> [!example] Example §36.2: Complex Eigenvectors
> Let $A = \begin{bmatrix} .5 & -.6 \\ .75 & 1.1 \end{bmatrix}$. Find the eigenvalues of $A$ and a basis for each eigenspace.
>
> **Eigenvalues.** The characteristic equation is
>
> $$
> 0 = \det\begin{bmatrix} .5 - \lambda & -.6 \\ .75 & 1.1 - \lambda \end{bmatrix} = (.5 - \lambda)(1.1 - \lambda) - (-.6)(.75) = \lambda^2 - 1.6\lambda + 1 .
> $$
>
> By the quadratic formula, $\lambda = \tfrac12\big[1.6 \pm \sqrt{(-1.6)^2 - 4}\big] = \tfrac12\big[1.6 \pm \sqrt{-1.44}\big] = .8 \pm .6i$.
>
> **Eigenvector for $\lambda = .8 - .6i$.**
>
> $$
> A - (.8 - .6i)I = \begin{bmatrix} .5 - .8 + .6i & -.6 \\ .75 & 1.1 - .8 + .6i \end{bmatrix} = \begin{bmatrix} -.3 + .6i & -.6 \\ .75 & .3 + .6i \end{bmatrix} . \qquad (1)
> $$
>
> Row reduction with complex arithmetic is unpleasant, but it is not needed. Since $.8 - .6i$ is an eigenvalue, the system
>
> $$
> (-.3 + .6i)x_1 - .6x_2 = 0, \qquad .75x_1 + (.3 + .6i)x_2 = 0 \qquad (2)
> $$
>
> has a nontrivial solution, so *both equations determine the same relationship between $x_1$ and $x_2$* (the matrix (1) is not invertible, so its rows are linearly dependent in $\mathbb{C}^2$: one is a complex multiple of the other). Use the second: $.75x_1 = (-.3 - .6i)x_2$, so $x_1 = (-.4 - .8i)x_2$. Choosing $x_2 = 5$ to clear the decimals gives $x_1 = -2 - 4i$, and a basis for the eigenspace is
>
> $$
> \mathbf{v}_1 = \begin{bmatrix} -2 - 4i \\ 5 \end{bmatrix} .
> $$
>
> **Eigenvector for $\lambda = .8 + .6i$.** The same calculation gives $\mathbf{v}_2 = \begin{bmatrix} -2 + 4i \\ 5 \end{bmatrix}$. Check:
>
> $$
> A\mathbf{v}_2 = \begin{bmatrix} .5(-2 + 4i) - .6(5) \\ .75(-2 + 4i) + 1.1(5) \end{bmatrix} = \begin{bmatrix} -4 + 2i \\ 4 + 3i \end{bmatrix}, \qquad (.8 + .6i)\mathbf{v}_2 = \begin{bmatrix} -1.6 + 3.2i - 1.2i + 2.4i^2 \\ 4 + 3i \end{bmatrix} = \begin{bmatrix} -4 + 2i \\ 4 + 3i \end{bmatrix} .
> $$
>
> The eigenvalues $.8 \mp .6i$ are complex conjugates, and so are the eigenvectors: $\mathbf{v}_2 = \overline{\mathbf{v}_1}$ (Theorem §36.2).
>
> *Lay: Examples 5.5.2 and 5.5.5*

^ex-36-2

> [!remark] Remark: Method — A Complex Eigenvector of a 2 × 2 Matrix
> Let $\lambda$ be a (complex) eigenvalue of the $2 \times 2$ matrix $A$, and let $(p, q)$ be a row of $A - \lambda I$ that is not zero.
> 1. The equation $px_1 + qx_2 = 0$ alone determines the eigenspace; the other row is a complex multiple of this one and can be ignored.
> 2. Take $\mathbf{v} = \begin{bmatrix} -q \\ p \end{bmatrix}$ (or any nonzero multiple; scale to clear decimals).
> 3. For a real $A$, the eigenvector for $\bar\lambda$ is $\overline{\mathbf{v}}$ (Theorem §36.2), so only one of the two needs computing.
>
> For example, with the second row $(.75,\ .3 + .6i)$ of (1), step 2 gives $(-.3 - .6i,\ .75)$, which is $\frac{3}{20}\mathbf{v}_1$.

^rem-36-1

Surprisingly, the matrix of Example §36.2 acts essentially as a rotation, which becomes visible when the iterates of a point are plotted.

> [!example] Example §36.3: Iterates Lie on an Ellipse
> With $A = \begin{bmatrix} .5 & -.6 \\ .75 & 1.1 \end{bmatrix}$ and $\mathbf{x}_0 = (2, 0)$, compute $\mathbf{x}_{k+1} = A\mathbf{x}_k$:
>
> $$
> \mathbf{x}_1 = \begin{bmatrix} .5 & -.6 \\ .75 & 1.1 \end{bmatrix}\begin{bmatrix} 2 \\ 0 \end{bmatrix} = \begin{bmatrix} 1.0 \\ 1.5 \end{bmatrix}, \qquad
> \mathbf{x}_2 = \begin{bmatrix} .5 & -.6 \\ .75 & 1.1 \end{bmatrix}\begin{bmatrix} 1.0 \\ 1.5 \end{bmatrix} = \begin{bmatrix} .5 - .9 \\ .75 + 1.65 \end{bmatrix} = \begin{bmatrix} -.4 \\ 2.4 \end{bmatrix}, \qquad \ldots
> $$
>
> The points $\mathbf{x}_0, \mathbf{x}_1, \mathbf{x}_2, \ldots$ circle the origin counterclockwise along an elliptical orbit and never settle down. The reason is Example §36.4 below: $A$ is a pure rotation in a suitable coordinate system.
>
> *Lay: Example 5.5.3*

^ex-36-3

![[m235-36-1.svg]]
*The iterates $\mathbf{x}_0, \ldots, \mathbf{x}_8$ (large dots) and $\mathbf{x}_9, \ldots, \mathbf{x}_{60}$ (small dots) of $\mathbf{x}_0 = (2, 0)$ under $A = \begin{bmatrix} .5 & -.6 \\ .75 & 1.1 \end{bmatrix}$. Each step is a rotation through about $36.9°$ (the argument of $.8 + .6i$) in the coordinates given by $\operatorname{Re}\mathbf{v}_1$ and $\operatorname{Im}\mathbf{v}_1$ (gray), so the orbit is an ellipse rather than a circle. The points never repeat exactly ($36.87°$ is not a rational fraction of $360°$); they fill out the ellipse.*

## Real and Imaginary Parts of Vectors

> [!definition] Definition §36.2: Conjugate, Real and Imaginary Parts of a Vector
> The **complex conjugate** of a complex vector $\mathbf{x}$ in $\mathbb{C}^n$ is the vector $\overline{\mathbf{x}}$ in $\mathbb{C}^n$ whose entries are the complex conjugates of the entries of $\mathbf{x}$. The **real and imaginary parts** of $\mathbf{x}$ are the vectors $\operatorname{Re}\mathbf{x}$ and $\operatorname{Im}\mathbf{x}$ in $\mathbb{R}^n$ formed from the real and imaginary parts of the entries of $\mathbf{x}$, so that $\mathbf{x} = \operatorname{Re}\mathbf{x} + i\operatorname{Im}\mathbf{x}$ and $\overline{\mathbf{x}} = \operatorname{Re}\mathbf{x} - i\operatorname{Im}\mathbf{x}$. For example,
>
> $$
> \mathbf{x} = \begin{bmatrix} 3 - i \\ i \\ 2 + 5i \end{bmatrix} = \begin{bmatrix} 3 \\ 0 \\ 2 \end{bmatrix} + i\begin{bmatrix} -1 \\ 1 \\ 5 \end{bmatrix}: \quad \operatorname{Re}\mathbf{x} = \begin{bmatrix} 3 \\ 0 \\ 2 \end{bmatrix}, \quad \operatorname{Im}\mathbf{x} = \begin{bmatrix} -1 \\ 1 \\ 5 \end{bmatrix}, \quad \overline{\mathbf{x}} = \begin{bmatrix} 3 + i \\ -i \\ 2 - 5i \end{bmatrix} .
> $$
>
> For an $m \times n$ matrix $B$ with possibly complex entries, $\overline{B}$ denotes the matrix of the conjugates of its entries.
>
> *Lay: 5.5 (text); Example 5.5.4*

^def-36-2

> [!theorem] Proposition §36.1: Conjugates and Real Parts in Matrix Algebra
> For a scalar $r$, matrices $B$, $C$ and a vector $\mathbf{x}$ (complex entries allowed, sizes compatible),
>
> $$
> \overline{r\mathbf{x}} = \bar r\,\overline{\mathbf{x}}, \qquad \overline{B\mathbf{x}} = \overline{B}\,\overline{\mathbf{x}}, \qquad \overline{BC} = \overline{B}\,\overline{C}, \qquad \overline{rB} = \bar r\,\overline{B} .
> $$
>
> If $A$ is a matrix with *real* entries and $\mathbf{x}$ is in $\mathbb{C}^n$, then
>
> $$
> \overline{A\mathbf{x}} = A\overline{\mathbf{x}}, \qquad A(\operatorname{Re}\mathbf{x}) = \operatorname{Re}(A\mathbf{x}), \qquad A(\operatorname{Im}\mathbf{x}) = \operatorname{Im}(A\mathbf{x}) .
> $$
>
> *Lay: 5.5 (text); Exercise 5.5.25*

^prop-36-1

> [!proof]+ Proof
> Each entry of $B\mathbf{x}$, $BC$, $r\mathbf{x}$, $rB$ is a sum of products of entries (and $r$). The conjugate of a sum is the sum of the conjugates and the conjugate of a product is the product of the conjugates ([[§53 Complex Numbers#^thm-53-3|Theorem §53.3]]), which gives the first four rules entry by entry.
>
> If $A$ is real, then $\overline{A} = A$, so $\overline{A\mathbf{x}} = A\overline{\mathbf{x}}$. Write $\mathbf{x} = \mathbf{u} + i\mathbf{w}$ with $\mathbf{u} = \operatorname{Re}\mathbf{x}$ and $\mathbf{w} = \operatorname{Im}\mathbf{x}$ real. Then $A\mathbf{x} = A\mathbf{u} + iA\mathbf{w}$, and $A\mathbf{u}$, $A\mathbf{w}$ are real vectors. So the real part of $A\mathbf{x}$ is $A\mathbf{u}$ and its imaginary part is $A\mathbf{w}$.

^pf-36-1

*Uses:* [[§53 Complex Numbers#^thm-53-3|§53.3]] (properties of conjugates), [[§36 Complex Eigenvalues#^def-36-2|Def. §36.2]]

## Eigenvalues and Eigenvectors of a Real Matrix That Acts on ℂⁿ

> [!theorem] Theorem §36.2: Complex Eigenvalues of a Real Matrix Come in Conjugate Pairs
> Let $A$ be an $n \times n$ matrix with real entries. If $\lambda$ is an eigenvalue of $A$ and $\mathbf{x}$ a corresponding eigenvector in $\mathbb{C}^n$, then $\bar\lambda$ is also an eigenvalue of $A$, with $\overline{\mathbf{x}}$ a corresponding eigenvector. So the complex eigenvalues of a real matrix occur in conjugate pairs.
>
> *Lay: 5.5 (text)*

^thm-36-2

> [!proof]+ Proof
> By Proposition §36.1, $A\overline{\mathbf{x}} = \overline{A\mathbf{x}} = \overline{\lambda\mathbf{x}} = \bar\lambda\,\overline{\mathbf{x}}$, and $\overline{\mathbf{x}} \ne \mathbf{0}$ because $\mathbf{x} \ne \mathbf{0}$.

^pf-36-2

*Uses:* [[§36 Complex Eigenvalues#^prop-36-1|§36.1]]

> [!remark]- Connections
> - Rigorous treatment: the non-real zeros of a polynomial with real coefficients come in conjugate pairs, [[§13 Polynomials#^ladr-4-14|LADR 4.14]] (applied to the characteristic polynomial, this gives the eigenvalue half of Theorem §36.2); over $\mathbb{R}$ such a pair is an irreducible quadratic factor, [[§13 Polynomials#^ladr-4-16|LADR 4.16]].

The next result is the basic "building block" for all real $2 \times 2$ matrices with complex eigenvalues.

> [!theorem] Proposition §36.3: Rotation–Scaling Matrices
> Let $a$ and $b$ be real, not both zero, and
>
> $$
> C = \begin{bmatrix} a & -b \\ b & a \end{bmatrix} .
> $$
>
> The eigenvalues of $C$ are $\lambda = a \pm bi$, with eigenvectors $\begin{bmatrix} 1 \\ -i \end{bmatrix}$ for $a + bi$ and $\begin{bmatrix} 1 \\ i \end{bmatrix}$ for $a - bi$. If $r = |\lambda| = \sqrt{a^2 + b^2}$, then
>
> $$
> C = r\begin{bmatrix} a/r & -b/r \\ b/r & a/r \end{bmatrix} = \begin{bmatrix} r & 0 \\ 0 & r \end{bmatrix}\begin{bmatrix} \cos\varphi & -\sin\varphi \\ \sin\varphi & \cos\varphi \end{bmatrix},
> $$
>
> where $\varphi$ is the angle between the positive $x$-axis and the ray from $(0, 0)$ through $(a, b)$, the **argument** of $a + bi$ ([[§53 Complex Numbers#^def-53-6|Definition §53.6]]). So $\mathbf{x} \mapsto C\mathbf{x}$ is the composition of a rotation through the angle $\varphi$ and a scaling by $|\lambda|$.
>
> *Lay: Example 5.5.6; Practice Problem 5.5*

^prop-36-3

> [!proof]+ Proof
> $\det(C - \lambda I) = (a - \lambda)^2 + b^2$, which is $0$ exactly when $a - \lambda = \pm bi$, that is, $\lambda = a \mp bi$. Next,
>
> $$
> C\begin{bmatrix} 1 \\ -i \end{bmatrix} = \begin{bmatrix} a + bi \\ b - ai \end{bmatrix} = (a + bi)\begin{bmatrix} 1 \\ -i \end{bmatrix}, \qquad C\begin{bmatrix} 1 \\ i \end{bmatrix} = \begin{bmatrix} a - bi \\ b + ai \end{bmatrix} = (a - bi)\begin{bmatrix} 1 \\ i \end{bmatrix},
> $$
>
> since $(a + bi)(-i) = b - ai$ and $(a - bi)i = b + ai$. Finally, $r > 0$, the point $(a/r, b/r)$ lies on the unit circle, and by the definition of $\varphi$ (polar coordinates), $a/r = \cos\varphi$ and $b/r = \sin\varphi$.

^pf-36-3

*Uses:* [[§53 Complex Numbers#^def-53-6|Def. §53.6]], [[§33 The Characteristic Equation#^thm-33-4|§33.4]]

The lecture writes $C = M_{a+bi}$, the matrix of multiplication by $a + bi$ on $\mathbb{C} = \mathbb{R}^2$ ([[§53 Complex Numbers#^rem-53-3|§53, Remark: Complex Numbers as 2 × 2 Matrices]]), and notes $M_zM_w = M_{zw}$. In particular, with $R_\varphi$ the rotation matrix, $(R_\varphi)^N = R_{N\varphi}$ and

$$
C^N = r^N R_{N\varphi} = (a^2 + b^2)^{N/2}R_{N\varphi} ,
$$

which is De Moivre's Theorem ([[§53 Complex Numbers#^thm-53-6|Theorem §53.6]]) in matrix form.

Every real $2 \times 2$ matrix with a complex eigenvalue is similar to such a $C$. The proof uses two facts: for a real matrix, $A(\operatorname{Re}\mathbf{x}) = \operatorname{Re}(A\mathbf{x})$ and $A(\operatorname{Im}\mathbf{x}) = \operatorname{Im}(A\mathbf{x})$ (Proposition §36.1), and the real and imaginary parts of an eigenvector for a complex eigenvalue are linearly independent.

> [!example] Example §36.4: The Rotation Inside A
> Let $A = \begin{bmatrix} .5 & -.6 \\ .75 & 1.1 \end{bmatrix}$, $\lambda = .8 - .6i$ and $\mathbf{v}_1 = \begin{bmatrix} -2 - 4i \\ 5 \end{bmatrix}$, as in Example §36.2. Let $P$ be the real $2 \times 2$ matrix
>
> $$
> P = [\,\operatorname{Re}\mathbf{v}_1 \;\; \operatorname{Im}\mathbf{v}_1\,] = \begin{bmatrix} -2 & -4 \\ 5 & 0 \end{bmatrix} .
> $$
>
> Then $\det P = 0 + 20 = 20$, $P^{-1} = \frac{1}{20}\begin{bmatrix} 0 & 4 \\ -5 & -2 \end{bmatrix}$, $AP = \begin{bmatrix} -1 - 3 & -2 \\ -1.5 + 5.5 & -3 \end{bmatrix} = \begin{bmatrix} -4 & -2 \\ 4 & -3 \end{bmatrix}$, and
>
> $$
> C = P^{-1}AP = \frac{1}{20}\begin{bmatrix} 0 & 4 \\ -5 & -2 \end{bmatrix}\begin{bmatrix} -4 & -2 \\ 4 & -3 \end{bmatrix} = \frac{1}{20}\begin{bmatrix} 16 & -12 \\ 12 & 16 \end{bmatrix} = \begin{bmatrix} .8 & -.6 \\ .6 & .8 \end{bmatrix} .
> $$
>
> By Proposition §36.3, $C$ is a pure rotation, since $|\lambda|^2 = (.8)^2 + (.6)^2 = 1$ (through the angle $\varphi$ with $\cos\varphi = .8$, $\sin\varphi = .6$, about $36.9°$). From $C = P^{-1}AP$,
>
> $$
> A = PCP^{-1} = P\begin{bmatrix} .8 & -.6 \\ .6 & .8 \end{bmatrix}P^{-1} .
> $$
>
> Here is the rotation "inside" $A$. The matrix $P$ provides a change of variable $\mathbf{x} = P\mathbf{u}$: the action of $A$ is a change of variable from $\mathbf{x}$ to $\mathbf{u}$, followed by a rotation, and then a return to the original variable,
>
> $$
> \mathbf{x} \xrightarrow{\ P^{-1}\ } \mathbf{u} \xrightarrow{\ C \text{ (rotation)}\ } C\mathbf{u} \xrightarrow{\ P\ } A\mathbf{x} .
> $$
>
> The rotation produces an ellipse, as in Example §36.3, instead of a circle, because the coordinate system given by the columns of $P$ is not rectangular and does not have equal unit lengths on its two axes.
>
> *Lay: Example 5.5.7*

^ex-36-4

> [!theorem] Theorem §36.4: Real 2 × 2 Matrices with a Complex Eigenvalue
> Let $A$ be a real $2 \times 2$ matrix with a complex eigenvalue $\lambda = a - bi$ ($b \ne 0$) and an associated eigenvector $\mathbf{v}$ in $\mathbb{C}^2$. Then
>
> $$
> A = PCP^{-1}, \qquad \text{where} \quad P = [\,\operatorname{Re}\mathbf{v} \;\; \operatorname{Im}\mathbf{v}\,] \quad \text{and} \quad C = \begin{bmatrix} a & -b \\ b & a \end{bmatrix} .
> $$
>
> *Lay: Theorem 9 (5.5)*

^thm-36-4

> [!proof]+ Proof
> *Lay omits the details, pointing to Exercises 25–26; this is the lecture's proof, with those two facts filled in.*
>
> **Step 1: $\operatorname{Re}\mathbf{v}$ and $\operatorname{Im}\mathbf{v}$ are linearly independent** (this step works for a real $n \times n$ matrix and $\mathbf{v}$ in $\mathbb{C}^n$). Suppose not. Since $\mathbf{v} \ne \mathbf{0}$, they are not both zero, so one is a real multiple of the other: $\operatorname{Im}\mathbf{v} = c\operatorname{Re}\mathbf{v}$ or $\operatorname{Re}\mathbf{v} = c\operatorname{Im}\mathbf{v}$ with $c$ real. Then $\mathbf{v} = (1 + ci)\operatorname{Re}\mathbf{v}$ or $\mathbf{v} = (c + i)\operatorname{Im}\mathbf{v}$: in either case $\mathbf{v} = \alpha\mathbf{w}$ with $\alpha \ne 0$ complex and $\mathbf{w} \ne \mathbf{0}$ real. Dividing $A\mathbf{v} = \lambda\mathbf{v}$ by $\alpha$ gives $A\mathbf{w} = \lambda\mathbf{w}$. The left side is a real vector. A nonzero entry $w_j$ of $\mathbf{w}$ gives the entry $\lambda w_j$ on the right, with imaginary part $-bw_j \ne 0$. This contradiction proves Step 1. In particular, $P$ is invertible.
>
> **Step 2: the columns of $AP$.** Write $\mathbf{v} = \mathbf{x} + i\mathbf{y}$ with $\mathbf{x} = \operatorname{Re}\mathbf{v}$, $\mathbf{y} = \operatorname{Im}\mathbf{v}$. Then
>
> $$
> \lambda\mathbf{v} = (a - bi)(\mathbf{x} + i\mathbf{y}) = (a\mathbf{x} + b\mathbf{y}) + i(-b\mathbf{x} + a\mathbf{y}) .
> $$
>
> Taking real and imaginary parts of $A\mathbf{v} = \lambda\mathbf{v}$, and using $A\mathbf{x} = \operatorname{Re}(A\mathbf{v})$ and $A\mathbf{y} = \operatorname{Im}(A\mathbf{v})$ (Proposition §36.1),
>
> $$
> A\mathbf{x} = a\mathbf{x} + b\mathbf{y}, \qquad A\mathbf{y} = -b\mathbf{x} + a\mathbf{y} .
> $$
>
> **Step 3.** Therefore
>
> $$
> AP = [\,A\mathbf{x} \;\; A\mathbf{y}\,] = [\,a\mathbf{x} + b\mathbf{y} \;\; -b\mathbf{x} + a\mathbf{y}\,] = [\,\mathbf{x} \;\; \mathbf{y}\,]\begin{bmatrix} a & -b \\ b & a \end{bmatrix} = PC ,
> $$
>
> and since $P$ is invertible, $A = PCP^{-1}$.

^pf-36-4

*Uses:* [[§36 Complex Eigenvalues#^prop-36-1|§36.1]], [[§36 Complex Eigenvalues#^def-36-2|Def. §36.2]], [[§13 Characterizations of Invertible Matrices|§13]] (Theorem 8: independent columns make a square matrix invertible)

> [!remark]- Connections
> - Rigorous treatment: on a real vector space, an irreducible quadratic factor $x^2 + bx + c$ ($b^2 < 4c$) of the minimal polynomial gives two-dimensional invariant subspaces without real eigenvectors, [[§15 The Minimal Polynomial#^ladr-5-33|LADR 5.33]] (and hence every operator on an odd-dimensional real space has an eigenvalue, [[§15 The Minimal Polynomial#^ladr-5-34|LADR 5.34]]). Theorem §36.4 is the explicit $2 \times 2$ form: on the plane spanned by $\operatorname{Re}\mathbf{v}$, $\operatorname{Im}\mathbf{v}$ the matrix acts as a rotation–scaling.

> [!remark] Remark: Signs and Conventions
> Lay pairs the eigenvalue $a - bi$ with $C = \begin{bmatrix} a & -b \\ b & a \end{bmatrix}$. The lecture uses the eigenvalue $\lambda = a + bi$ with eigenvector $\mathbf{v}$; then $P = [\,\operatorname{Re}\mathbf{v} \;\; \operatorname{Im}\mathbf{v}\,]$ gives $AP = P\begin{bmatrix} a & b \\ -b & a \end{bmatrix}$, that is, $P^{-1}AP = M_{a - bi}$. Both are Theorem §36.4: the eigenvector of $a + bi$ is the conjugate of the eigenvector of $a - bi$ (Theorem §36.2), and conjugating $\mathbf{v}$ changes the sign of $\operatorname{Im}\mathbf{v}$, the second column of $P$, which changes the signs of the off-diagonal entries of $C$.

^rem-36-2

> [!example] Example §36.5: Powers of a Matrix with Complex Eigenvalues
> Let $A = \begin{bmatrix} 1 & -2 \\ 1 & 3 \end{bmatrix}$. Find its eigenvalues, write $A = PCP^{-1}$ as in Theorem §36.4, and describe $A^N$ for large $N$.
>
> **Eigenvalues.** $\det(A - \lambda I) = (1 - \lambda)(3 - \lambda) + 2 = \lambda^2 - 4\lambda + 5$, so
>
> $$
> \lambda = \frac{4 \pm \sqrt{16 - 20}}{2} = 2 \pm \frac{\sqrt{-4}}{2} = 2 \pm i .
> $$
>
> **Eigenvector for $\lambda = 2 + i$.** $A - (2 + i)I = \begin{bmatrix} -1 - i & -2 \\ 1 & 1 - i \end{bmatrix}$. Multiplying the second row by $-1 - i$ gives $(-1 - i,\ (1 - i)(-1 - i)) = (-1 - i, -2)$, the first row, as expected. So the eigenspace is given by $(-1 - i)x_1 - 2x_2 = 0$, and $\mathbf{v} = \begin{bmatrix} 2 \\ -1 - i \end{bmatrix}$. (Check, second row: $2 + (1 - i)(-1 - i) = 2 + (-1 - 1) = 0$.)
>
> **The factorization.** Theorem §36.4 uses the eigenvalue $a - bi = 2 - i$ (so $a = 2$, $b = 1$) and its eigenvector $\overline{\mathbf{v}} = (2, -1 + i)$:
>
> $$
> P = \begin{bmatrix} 2 & 0 \\ -1 & 1 \end{bmatrix}, \qquad C = \begin{bmatrix} 2 & -1 \\ 1 & 2 \end{bmatrix}; \qquad
> AP = \begin{bmatrix} 1 & -2 \\ 1 & 3 \end{bmatrix}\begin{bmatrix} 2 & 0 \\ -1 & 1 \end{bmatrix} = \begin{bmatrix} 4 & -2 \\ -1 & 3 \end{bmatrix} = \begin{bmatrix} 2 & 0 \\ -1 & 1 \end{bmatrix}\begin{bmatrix} 2 & -1 \\ 1 & 2 \end{bmatrix} = PC .
> $$
>
> (The lecture uses $\mathbf{v}$ itself: $P' = [\,\operatorname{Re}\mathbf{v} \;\; \operatorname{Im}\mathbf{v}\,] = \begin{bmatrix} 2 & 0 \\ -1 & -1 \end{bmatrix}$ and $P'^{-1}AP' = \begin{bmatrix} 2 & 1 \\ -1 & 2 \end{bmatrix} = M_{2-i}$, as in Remark: Signs and Conventions.)
>
> **Powers.** $C = \sqrt5\begin{bmatrix} 2/\sqrt5 & -1/\sqrt5 \\ 1/\sqrt5 & 2/\sqrt5 \end{bmatrix} = \sqrt5\,R_\varphi$ with $\varphi = \cos^{-1}(2/\sqrt5) \approx 26.6°$, so
>
> $$
> A^N = PC^NP^{-1} = 5^{N/2}\,P R_{N\varphi}P^{-1} .
> $$
>
> The matrices $PR_{N\varphi}P^{-1}$ stay bounded (their entries are bounded combinations of $\cos N\varphi$, $\sin N\varphi$), and they do not tend to $0$ (they are invertible with determinant $1$), while $5^{N/2} \to \infty$: the iterates $A^N\mathbf{x}$ of any $\mathbf{x} \ne \mathbf{0}$ spiral outward to infinity. In the same way, for a real $2 \times 2$ matrix with complex eigenvalue $a + bi$, $b \ne 0$: $A^N \to 0$ if $a^2 + b^2 < 1$, $A^N\mathbf{x}$ grows without bound if $a^2 + b^2 > 1$, and if $a^2 + b^2 = 1$, $A$ is similar to the rotation $R_\varphi$, $\varphi = \cos^{-1}a \ne 0$, so $A^N = PR_{N\varphi}P^{-1}$ keeps turning and has no limit. These are the spiral attractor, spiral repeller and ellipse of [[§37 Discrete Dynamical Systems|§37]].
>
> *The lecture writes $PAP^{-1} = \begin{bmatrix} a & b \\ -b & a \end{bmatrix}$ and $A^N = P^{-1}(M_{2-i})^NP$; with $P$ the matrix of real and imaginary parts, the correct order is $P^{-1}AP$ and $A^N = P(M_{2-i})^NP^{-1}$.*
>
> *Source: 235 lecture L21*

^ex-36-5

> [!remark] Remark: Higher Dimensions
> The phenomenon persists in higher dimensions. If $A$ is a $3 \times 3$ real matrix with a complex eigenvalue, there is a plane in $\mathbb{R}^3$ on which $A$ acts as a rotation, possibly combined with a scaling: every vector in the plane is mapped to a vector in the same plane, and the plane is **invariant** under $A$ (it is spanned by $\operatorname{Re}\mathbf{v}$ and $\operatorname{Im}\mathbf{v}$, by Step 2 of the proof of Theorem §36.4). For example,
>
> $$
> A = \begin{bmatrix} .8 & -.6 & 0 \\ .6 & .8 & 0 \\ 0 & 0 & 1.07 \end{bmatrix}
> $$
>
> has eigenvalues $.8 \pm .6i$ and $1.07$. Any vector $\mathbf{w}_0$ in the $x_1x_2$-plane (third coordinate $0$) is rotated by $A$ into another point of that plane, and the iterates of $\mathbf{w}_0 = (2, 0, 0)$ go around a circle. A vector $\mathbf{x}_0$ not in the plane, such as $(2, 0, 1)$, has its $x_3$-coordinate multiplied by $1.07$ at each step, so its iterates spiral upward around the $x_3$-axis.
>
> *Lay: Example 5.5.8*

^rem-36-3
