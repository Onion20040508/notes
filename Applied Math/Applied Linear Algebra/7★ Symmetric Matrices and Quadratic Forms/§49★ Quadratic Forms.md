---
type: section
subject: "[[Applied Linear Algebra]]"
chapter: 7
section: 49
lay: "7.2"
aliases: ["Lay 7.2"]
tags: [applied-linear-algebra, math235, extension]
---
← [[§48★ Diagonalization of Symmetric Matrices]] · ↑ [[· 7★ Symmetric Matrices and Quadratic Forms]] · [[§50★ Constrained Optimization]] →

*Lay, Section 7.2.*
★ *Beyond MATH 235: the course ended with inner products (Ch. 6); Chapter 7 is included from Lay as the continuation.*

A quadratic form is a homogeneous polynomial of degree two in $n$ variables, such as $x_1^2 - 8x_1x_2 - 5x_2^2$; every one can be written $\mathbf{x}^T A \mathbf{x}$ with $A$ symmetric. Quadratic forms appear as energies in physics, as second-order terms of Taylor expansions, as variances in statistics. The cross-product terms $x_ix_j$ make a form hard to read. The Principal Axes Theorem removes them: the orthogonal diagonalization $A = PDP^T$ of §48 is exactly a rotation of coordinates $\mathbf{x} = P\mathbf{y}$ after which the form is $\lambda_1 y_1^2 + \cdots + \lambda_n y_n^2$. Two consequences follow at once: the level curves of a two-variable form are conics whose axes are the eigenvectors, and the sign behaviour of the form (positive definite, negative definite, indefinite) is read off from the signs of the eigenvalues.

## Quadratic Forms

> [!definition] Definition §49.1: Quadratic Form
> A **quadratic form** on $\mathbb{R}^n$ is a function $Q$ defined on $\mathbb{R}^n$ whose value at a vector $\mathbf{x}$ in $\mathbb{R}^n$ can be computed by an expression of the form
>
> $$
> Q(\mathbf{x}) = \mathbf{x}^T A \mathbf{x} ,
> $$
>
> where $A$ is an $n \times n$ symmetric matrix. The matrix $A$ is called the **matrix of the quadratic form**.
>
> The simplest nonzero quadratic form is $Q(\mathbf{x}) = \mathbf{x}^T I \mathbf{x} = \|\mathbf{x}\|^2$. In general
>
> $$
> \mathbf{x}^T A \mathbf{x} = \sum_{i=1}^n a_{ii} x_i^2 + \sum_{i < j} 2a_{ij}\, x_i x_j :
> $$
>
> the diagonal entries are the coefficients of the squares, and the **cross-product term** $x_ix_j$ ($i \ne j$) has coefficient $a_{ij} + a_{ji} = 2a_{ij}$. Conversely, to write a given form as $\mathbf{x}^T A \mathbf{x}$, put the coefficient of $x_i^2$ in position $(i, i)$ and split the coefficient of $x_ix_j$ evenly between positions $(i, j)$ and $(j, i)$.
>
> *Lay: 7.2, Definition and text*

^def-49-1

> [!remark]- Connections
> - Rigorous treatment: [[§32 Bilinear Forms and Quadratic Forms#^ladr-9-18|LADR 9.18]] defines a quadratic form as $q(v) = \beta(v, v)$ for a bilinear form $\beta$, and [[§32 Bilinear Forms and Quadratic Forms#^ladr-9-21|LADR 9.21]] shows that $\beta$ can be taken symmetric and is then unique. That is why Lay can insist on a *symmetric* $A$: the even split of each cross coefficient is the unique symmetric choice ($A = \frac12(B + B^T)$ for any $B$ with $\mathbf{x}^T B\mathbf{x} = Q(\mathbf{x})$; [[§32 Bilinear Forms and Quadratic Forms#^ladr-9-22|LADR 9.22]]).

> [!example] Example §49.1: From a Matrix to a Form and Back
> **(a)** Let $\mathbf{x} = \begin{bmatrix} x_1 \\ x_2 \end{bmatrix}$. For $A = \begin{bmatrix} 4 & 0 \\ 0 & 3 \end{bmatrix}$,
>
> $$
> \mathbf{x}^T A \mathbf{x} = [\,x_1\ \ x_2\,] \begin{bmatrix} 4 & 0 \\ 0 & 3 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = [\,x_1\ \ x_2\,] \begin{bmatrix} 4x_1 \\ 3x_2 \end{bmatrix} = 4x_1^2 + 3x_2^2 .
> $$
>
> A diagonal matrix gives a form with no cross-product term.
>
> **(b)** For $A = \begin{bmatrix} 3 & -2 \\ -2 & 7 \end{bmatrix}$, watch how the two $-2$ entries enter:
>
> $$
> \mathbf{x}^T A \mathbf{x} = [\,x_1\ \ x_2\,] \begin{bmatrix} 3x_1 - 2x_2 \\ -2x_1 + 7x_2 \end{bmatrix} = x_1(3x_1 - 2x_2) + x_2(-2x_1 + 7x_2) = 3x_1^2 - 2x_1x_2 - 2x_2x_1 + 7x_2^2 = 3x_1^2 - 4x_1x_2 + 7x_2^2 .
> $$
>
> The term $-4x_1x_2$ comes from the two off-diagonal entries $-2$.
>
> **(c)** For $\mathbf{x}$ in $\mathbb{R}^3$, write $Q(\mathbf{x}) = 5x_1^2 + 3x_2^2 + 2x_3^2 - x_1x_2 + 8x_2x_3$ as $\mathbf{x}^T A \mathbf{x}$. The coefficients $5, 3, 2$ of the squares go on the diagonal. The coefficient $-1$ of $x_1x_2$ is split as $-1/2$ in positions $(1,2)$ and $(2,1)$, the coefficient $8$ of $x_2x_3$ as $4$ in positions $(2,3)$ and $(3,2)$, and the coefficient of $x_1x_3$ is $0$:
>
> $$
> Q(\mathbf{x}) = [\,x_1\ \ x_2\ \ x_3\,] \begin{bmatrix} 5 & -1/2 & 0 \\ -1/2 & 3 & 4 \\ 0 & 4 & 2 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix}.
> $$
>
> *Lay: Examples 7.2.1 and 7.2.2*

^ex-49-1

## Change of Variable in a Quadratic Form

> [!definition] Definition §49.2: Change of Variable
> If $\mathbf{x}$ represents a variable vector in $\mathbb{R}^n$, a **change of variable** is an equation of the form
>
> $$
> \mathbf{x} = P\mathbf{y}, \qquad\text{or equivalently}\qquad \mathbf{y} = P^{-1}\mathbf{x}, \qquad (1)
> $$
>
> where $P$ is an invertible matrix and $\mathbf{y}$ is a new variable vector in $\mathbb{R}^n$. Here $\mathbf{y}$ is the coordinate vector of $\mathbf{x}$ relative to the basis of $\mathbb{R}^n$ formed by the columns of $P$ ([[§26 Coordinate Systems#^def-26-1|Definition §26.1]]). It is an **orthogonal change of variable** when $P$ is orthogonal; then $\mathbf{y} = P^T \mathbf{x}$.
>
> *Lay: 7.2, Equation (1)*

^def-49-2

> [!theorem] Proposition §49.1: Change of Variable in a Quadratic Form
> If the change of variable $\mathbf{x} = P\mathbf{y}$ is made in the quadratic form $\mathbf{x}^T A \mathbf{x}$, then
>
> $$
> \mathbf{x}^T A \mathbf{x} = \mathbf{y}^T (P^T A P)\, \mathbf{y} , \qquad (2)
> $$
>
> and the new matrix of the quadratic form is the symmetric matrix $P^T A P$.
>
> *Lay: 7.2, Equation (2)*

^prop-49-1

> [!proof]+ Proof
> Substitute and use $(P\mathbf{y})^T = \mathbf{y}^T P^T$:
>
> $$
> \mathbf{x}^T A \mathbf{x} = (P\mathbf{y})^T A (P\mathbf{y}) = \mathbf{y}^T P^T A P \mathbf{y} = \mathbf{y}^T (P^T A P) \mathbf{y} .
> $$
>
> The new matrix is symmetric: $(P^T A P)^T = P^T A^T P^{TT} = P^T A P$.

^pf-49-1

*Uses:* [[§49★ Quadratic Forms#^def-49-1|Def. §49.1]], [[§11 Matrix Operations#^thm-11-7|§11.7]] (transpose of a product)

Since $A$ is symmetric, there is an *orthogonal* $P$ with $P^TAP = D$ diagonal ([[§48★ Diagonalization of Symmetric Matrices#^thm-48-2|Theorem §48.2]]), and then (2) becomes $\mathbf{y}^T D \mathbf{y}$, a form without cross-product terms.

> [!theorem] Theorem §49.2: The Principal Axes Theorem
> Let $A$ be an $n \times n$ symmetric matrix. Then there is an orthogonal change of variable, $\mathbf{x} = P\mathbf{y}$, that transforms the quadratic form $\mathbf{x}^T A \mathbf{x}$ into a quadratic form $\mathbf{y}^T D \mathbf{y}$ with no cross-product term:
>
> $$
> \mathbf{x}^T A \mathbf{x} = \mathbf{y}^T D \mathbf{y} = \lambda_1 y_1^2 + \lambda_2 y_2^2 + \cdots + \lambda_n y_n^2 ,
> $$
>
> where $\lambda_1, \dots, \lambda_n$ are the eigenvalues of $A$. One may take for $P$ any orthogonal matrix that orthogonally diagonalizes $A$.
>
> *Lay: Theorem 4 (7.2)*

^thm-49-2

> [!proof]+ Proof
> (Lay: "the proof was essentially given before Example 4".) By [[§48★ Diagonalization of Symmetric Matrices#^thm-48-2|Theorem §48.2]], $A = PDP^T$ with $P$ orthogonal and $D = \operatorname{diag}(\lambda_1, \dots, \lambda_n)$, the $\lambda_i$ being the eigenvalues of $A$. Then $P^T A P = P^T P D P^T P = D$, because $P^T P = I$. By Proposition §49.1, the change of variable $\mathbf{x} = P\mathbf{y}$ gives
>
> $$
> \mathbf{x}^T A \mathbf{x} = \mathbf{y}^T (P^T A P) \mathbf{y} = \mathbf{y}^T D \mathbf{y} = \lambda_1 y_1^2 + \cdots + \lambda_n y_n^2 ,
> $$
>
> the last step being [[§49★ Quadratic Forms#^ex-49-1|Example §49.1]](a) in $n$ variables: a diagonal matrix gives only squares.

^pf-49-2

*Uses:* [[§48★ Diagonalization of Symmetric Matrices#^thm-48-2|§48.2]], [[§49★ Quadratic Forms#^prop-49-1|§49.1]], [[§41 Orthogonal Sets#^thm-41-4|§41.4]] ($P^TP = I$), [[§49★ Quadratic Forms#^ex-49-1|Ex. §49.1]](a) (a diagonal matrix gives only squares)

> [!definition] Definition §49.3: Principal Axes
> The columns of $P$ in the Principal Axes Theorem are called the **principal axes** of the quadratic form $\mathbf{x}^T A \mathbf{x}$. They are orthonormal eigenvectors of $A$, and the vector $\mathbf{y}$ is the coordinate vector of $\mathbf{x}$ relative to the orthonormal basis of $\mathbb{R}^n$ given by these principal axes.
>
> *Lay: 7.2 (text)*

^def-49-3

> [!remark]- Connections
> - Rigorous treatment: [[§32 Bilinear Forms and Quadratic Forms#^ladr-9-23|LADR 9.23]](b), diagonalization of a quadratic form by an orthonormal basis, deduced from the bilinear-form version [[§32 Bilinear Forms and Quadratic Forms#^ladr-9-13|LADR 9.13]] and the real spectral theorem. Axler also notes (9.23(a)) that *without* the orthonormality requirement any quadratic form over any field can be diagonalized, by a non-orthogonal $P$ (completing squares).
> - Used in Calculus to bring a quadric surface to standard form by a rotation of axes: [[§85 Cylinders and Quadric Surfaces#^def-85-3|Calc Def. §85.3]].
> - PDE version: for a second-order PDE with constant coefficients, rotating the $(\xi, \eta)$-axes to the principal axes of $A\xi^2 + B\xi\eta + C\eta^2$ removes the mixed derivative, and the sign of $B^2 - 4AC$ classifies the equation as elliptic, parabolic or hyperbolic, [[§40★ Classification and Limitations#^def-40-1|341 Def. §40.1]].

> [!example] Example §49.2: Removing a Cross-Product Term
> Let $Q(\mathbf{x}) = x_1^2 - 8x_1x_2 - 5x_2^2$.
>
> **Values.** For $\mathbf{x} = (-3, 1)$, $(2, -2)$, $(1, -3)$:
>
> $$
> \begin{aligned}
> Q(-3, 1) &= (-3)^2 - 8(-3)(1) - 5(1)^2 = 9 + 24 - 5 = 28, \\
> Q(2, -2) &= (2)^2 - 8(2)(-2) - 5(-2)^2 = 4 + 32 - 20 = 16, \\
> Q(1, -3) &= (1)^2 - 8(1)(-3) - 5(-3)^2 = 1 + 24 - 45 = -20 .
> \end{aligned}
> $$
>
> **Change of variable.** The matrix of the form is $A = \begin{bmatrix} 1 & -4 \\ -4 & -5 \end{bmatrix}$. Its characteristic polynomial is $(1 - \lambda)(-5 - \lambda) - 16 = \lambda^2 + 4\lambda - 21 = (\lambda - 3)(\lambda + 7)$, so the eigenvalues are $3$ and $-7$. Row reducing $A - 3I = \begin{bmatrix} -2 & -4 \\ -4 & -8 \end{bmatrix}$ gives $x_1 = -2x_2$, eigenvector $(2, -1)$; row reducing $A + 7I = \begin{bmatrix} 8 & -4 \\ -4 & 2 \end{bmatrix}$ gives $x_2 = 2x_1$, eigenvector $(1, 2)$. These are automatically orthogonal ([[§48★ Diagonalization of Symmetric Matrices#^thm-48-1|Theorem §48.1]]). Normalizing,
>
> $$
> \lambda = 3:\ \begin{bmatrix} 2/\sqrt5 \\ -1/\sqrt5 \end{bmatrix}, \qquad
> \lambda = -7:\ \begin{bmatrix} 1/\sqrt5 \\ 2/\sqrt5 \end{bmatrix}, \qquad
> P = \begin{bmatrix} 2/\sqrt5 & 1/\sqrt5 \\ -1/\sqrt5 & 2/\sqrt5 \end{bmatrix}, \quad D = \begin{bmatrix} 3 & 0 \\ 0 & -7 \end{bmatrix}.
> $$
>
> Then $A = PDP^{-1}$ and $D = P^{-1}AP = P^TAP$, so the change of variable $\mathbf{x} = P\mathbf{y}$ gives
>
> $$
> x_1^2 - 8x_1x_2 - 5x_2^2 = \mathbf{x}^T A \mathbf{x} = (P\mathbf{y})^T A (P\mathbf{y}) = \mathbf{y}^T P^T A P \mathbf{y} = \mathbf{y}^T D \mathbf{y} = 3y_1^2 - 7y_2^2 .
> $$
>
> **Check at $\mathbf{x} = (2, -2)$.** Since $\mathbf{x} = P\mathbf{y}$, $\mathbf{y} = P^{-1}\mathbf{x} = P^T \mathbf{x}$:
>
> $$
> \mathbf{y} = \begin{bmatrix} 2/\sqrt5 & -1/\sqrt5 \\ 1/\sqrt5 & 2/\sqrt5 \end{bmatrix} \begin{bmatrix} 2 \\ -2 \end{bmatrix} = \begin{bmatrix} 6/\sqrt5 \\ -2/\sqrt5 \end{bmatrix},
> \qquad
> 3y_1^2 - 7y_2^2 = 3 \cdot \frac{36}{5} - 7 \cdot \frac45 = \frac{108 - 28}{5} = 16 ,
> $$
>
> which is $Q(2, -2)$, as computed directly. The two forms are the same function, evaluated in two coordinate systems: multiplication by $P$ carries the $\mathbf{y}$-plane to the $\mathbf{x}$-plane, and $\mathbf{y}^T D \mathbf{y}$ and $\mathbf{x}^T A \mathbf{x}$ give the same number at corresponding points.
>
> *Lay: Examples 7.2.3 and 7.2.4*

^ex-49-2

> [!remark] Remark: Method — Removing the Cross-Product Terms
> To find an orthogonal change of variable $\mathbf{x} = P\mathbf{y}$ that removes the cross-product terms from $Q(\mathbf{x})$:
> 1. Write the matrix $A$ of the form ([[§49★ Quadratic Forms#^def-49-1|Definition §49.1]]): squares on the diagonal, half of each cross coefficient off the diagonal.
> 2. Orthogonally diagonalize $A = PDP^T$ ([[§48★ Diagonalization of Symmetric Matrices#^rem-48-1|Method of §48]]).
> 3. The new form is $\mathbf{y}^T D \mathbf{y} = \lambda_1 y_1^2 + \cdots + \lambda_n y_n^2$, with $\lambda_i$ in the same order as the columns of $P$.
> 4. To evaluate at a given $\mathbf{x}$, use $\mathbf{y} = P^T\mathbf{x}$ (not $P\mathbf{x}$).

^rem-49-1

## A Geometric View of Principal Axes

> [!theorem] Proposition §49.3: Level Curves of a Quadratic Form in Two Variables
> Let $Q(\mathbf{x}) = \mathbf{x}^T A \mathbf{x}$, where $A$ is an invertible $2 \times 2$ symmetric matrix, and let $c$ be a constant. The set of all $\mathbf{x}$ in $\mathbb{R}^2$ that satisfy
>
> $$
> \mathbf{x}^T A \mathbf{x} = c \qquad (3)
> $$
>
> either is an ellipse (or circle), a hyperbola, two intersecting lines or a single point, or contains no points at all. If $A$ is diagonal, the graph is in **standard position**, $x_1^2/a^2 + x_2^2/b^2 = 1$ or $x_1^2/a^2 - x_2^2/b^2 = 1$ up to renaming. If $A$ is not diagonal, the graph is rotated out of standard position, and the principal axes (the eigenvectors of $A$) are the axes of a coordinate system $y_1, y_2$ in which it is in standard position.
>
> *Lay: 7.2 (text), "it can be shown"*

^prop-49-3

> [!proof]+ Proof
> (Lay asserts this; here is why.) By the Principal Axes Theorem, in the coordinates $\mathbf{y} = P^T\mathbf{x}$ along the principal axes, (3) reads
>
> $$
> \lambda_1 y_1^2 + \lambda_2 y_2^2 = c ,
> $$
>
> and $\lambda_1 \lambda_2 = \det D = \det A \ne 0$ (since $\det A = \det P \det D \det P^T = (\det P)^2 \det D$ and $(\det P)^2 = \det(P^TP) = 1$), so both eigenvalues are nonzero. Since $P$ is orthogonal, $\mathbf{y} \mapsto P\mathbf{y}$ preserves lengths and angles ([[§41 Orthogonal Sets#^thm-41-5|Theorem §41.5]]), so the set in the $\mathbf{x}$-plane is congruent to the set in the $\mathbf{y}$-plane, which has the axes along the coordinate axes. Now go through the cases.
> - $\lambda_1, \lambda_2$ of the same sign as $c \ne 0$: dividing by $c$ gives $y_1^2/a^2 + y_2^2/b^2 = 1$ with $a = \sqrt{c/\lambda_1}$, $b = \sqrt{c/\lambda_2}$, an ellipse (a circle if $\lambda_1 = \lambda_2$).
> - $\lambda_1, \lambda_2$ of the same sign, opposite to $c \ne 0$: the left side has the opposite sign of $c$ for every $\mathbf{y} \ne \mathbf{0}$ and is $0$ at $\mathbf{0}$, so there are no points.
> - $\lambda_1, \lambda_2$ of the same sign and $c = 0$: only $\mathbf{y} = \mathbf{0}$, a single point.
> - $\lambda_1, \lambda_2$ of opposite signs and $c \ne 0$: one coefficient has the sign of $c$ and the other not, so dividing by $c$ gives $y_1^2/a^2 - y_2^2/b^2 = 1$ or $y_2^2/b^2 - y_1^2/a^2 = 1$, a hyperbola.
> - $\lambda_1, \lambda_2$ of opposite signs and $c = 0$: say $\lambda_1 > 0 > \lambda_2$; then $\lambda_1 y_1^2 = |\lambda_2| y_2^2$, that is, $y_2 = \pm\sqrt{\lambda_1/|\lambda_2|}\, y_1$, two lines through the origin.
>
> In the $\mathbf{x}$-plane, the $y_1$- and $y_2$-axes are the lines through $\mathbf{0}$ in the directions of the columns of $P$, the principal axes.

^pf-49-3

*Uses:* [[§49★ Quadratic Forms#^thm-49-2|§49.2]], [[§41 Orthogonal Sets#^thm-41-5|§41.5]] (orthogonal matrices preserve lengths), [[§21 Properties of Determinants#^thm-21-9|§21.9]], [[§21 Properties of Determinants#^thm-21-6|§21.6]] ($\det PDP^T = (\det P)^2 \det D = \det D$), [[§118 Graphs of Second-Degree Equations#^def-118-4|Calc Def. §118.4]] (ellipse and hyperbola in standard position)

> [!example] Example §49.3: Principal Axes of an Ellipse and a Hyperbola
> **(a)** The graph of $5x_1^2 - 4x_1x_2 + 5x_2^2 = 48$ is an ellipse. Find a change of variable that removes the cross-product term from the equation.
>
> The matrix of the form is $A = \begin{bmatrix} 5 & -2 \\ -2 & 5 \end{bmatrix}$, with characteristic polynomial $(5 - \lambda)^2 - 4 = (\lambda - 3)(\lambda - 7)$. For $\lambda = 3$, $A - 3I = \begin{bmatrix} 2 & -2 \\ -2 & 2 \end{bmatrix}$ gives $x_1 = x_2$; for $\lambda = 7$, $A - 7I = \begin{bmatrix} -2 & -2 \\ -2 & -2 \end{bmatrix}$ gives $x_1 = -x_2$. The unit eigenvectors are
>
> $$
> \mathbf{u}_1 = \begin{bmatrix} 1/\sqrt2 \\ 1/\sqrt2 \end{bmatrix}, \quad \mathbf{u}_2 = \begin{bmatrix} -1/\sqrt2 \\ 1/\sqrt2 \end{bmatrix}, \qquad
> P = [\,\mathbf{u}_1\ \ \mathbf{u}_2\,] = \begin{bmatrix} 1/\sqrt2 & -1/\sqrt2 \\ 1/\sqrt2 & 1/\sqrt2 \end{bmatrix}.
> $$
>
> $P$ orthogonally diagonalizes $A$, so the change of variable $\mathbf{x} = P\mathbf{y}$ produces the form $\mathbf{y}^T D \mathbf{y} = 3y_1^2 + 7y_2^2$, and the equation becomes $3y_1^2 + 7y_2^2 = 48$, that is,
>
> $$
> \frac{y_1^2}{16} + \frac{y_2^2}{48/7} = 1 .
> $$
>
> The ellipse has semi-axes $4$ along the line $x_2 = x_1$ (direction $\mathbf{u}_1$) and $\sqrt{48/7} \approx 2.62$ along $x_2 = -x_1$ (direction $\mathbf{u}_2$). $P$ is the rotation by $45^\circ$.
>
> **(b)** The graph of $x_1^2 - 8x_1x_2 - 5x_2^2 = 16$ is $\mathbf{x}^T A \mathbf{x} = 16$ for the matrix of Example §49.2. There $\mathbf{x} = P\mathbf{y}$ turned the equation into $3y_1^2 - 7y_2^2 = 16$, a hyperbola in standard position in the $\mathbf{y}$-coordinates, with vertices at $y_1 = \pm 4/\sqrt3 \approx \pm 2.31$ on the $y_1$-axis. The positive $y_1$-axis points in the direction of the first column $(2, -1)/\sqrt5$ of $P$, and the positive $y_2$-axis in the direction of the second column $(1, 2)/\sqrt5$.
>
> *Lay: Example 7.2.5 and Figure 3*

^ex-49-3

![[m235-49-1.svg]]
*The two conics of Example §49.3, with their principal axes (green) and the unit eigenvectors $\mathbf{u}_1, \mathbf{u}_2$ (red) that span them. In the $y_1y_2$ coordinate system each curve is in standard position; the cross-product term $-4x_1x_2$ or $-8x_1x_2$ only records that the axes have been rotated away from the $x_1x_2$ axes.*

## Classifying Quadratic Forms

For $A$ an $n \times n$ matrix, $Q(\mathbf{x}) = \mathbf{x}^T A \mathbf{x}$ is a real-valued function on $\mathbb{R}^n$. For $n = 2$ its graph $z = Q(x_1, x_2)$ is a surface. For $z = 3x_1^2 + 7x_2^2$ it is a bowl (elliptic paraboloid): $Q > 0$ except at $\mathbf{0}$, and the horizontal cross-sections are ellipses. For $z = 3x_1^2$ it is a trough (parabolic cylinder): $Q \ge 0$, with $Q = 0$ along the whole $x_2$-axis. For $z = 3x_1^2 - 7x_2^2$ it is a saddle (hyperbolic paraboloid), with hyperbolas as cross-sections. For $z = -3x_1^2 - 7x_2^2$ it is an upside-down bowl: $Q < 0$ except at $\mathbf{0}$.

> [!definition] Definition §49.4: Positive Definite, Negative Definite, Indefinite
> A quadratic form $Q$ is:
> - (a) **positive definite** if $Q(\mathbf{x}) > 0$ for all $\mathbf{x} \ne \mathbf{0}$,
> - (b) **negative definite** if $Q(\mathbf{x}) < 0$ for all $\mathbf{x} \ne \mathbf{0}$,
> - (c) **indefinite** if $Q(\mathbf{x})$ assumes both positive and negative values.
>
> Also, $Q$ is **positive semidefinite** if $Q(\mathbf{x}) \ge 0$ for all $\mathbf{x}$, and **negative semidefinite** if $Q(\mathbf{x}) \le 0$ for all $\mathbf{x}$. For example, $3x_1^2 + 7x_2^2$ and $3x_1^2$ are both positive semidefinite; the first is better described as positive definite.
>
> *Lay: 7.2, Definition and text*

^def-49-4

> [!theorem] Theorem §49.4: Quadratic Forms and Eigenvalues
> Let $A$ be an $n \times n$ symmetric matrix. Then a quadratic form $\mathbf{x}^T A \mathbf{x}$ is:
> - (a) positive definite if and only if the eigenvalues of $A$ are all positive,
> - (b) negative definite if and only if the eigenvalues of $A$ are all negative, or
> - (c) indefinite if and only if $A$ has both positive and negative eigenvalues.
>
> *Lay: Theorem 5 (7.2)*

^thm-49-4

> [!proof]+ Proof
> By the Principal Axes Theorem, there is an orthogonal change of variable $\mathbf{x} = P\mathbf{y}$ such that
>
> $$
> Q(\mathbf{x}) = \mathbf{x}^T A \mathbf{x} = \mathbf{y}^T D \mathbf{y} = \lambda_1 y_1^2 + \lambda_2 y_2^2 + \cdots + \lambda_n y_n^2 , \qquad (4)
> $$
>
> where $\lambda_1, \dots, \lambda_n$ are the eigenvalues of $A$. Since $P$ is invertible, $\mathbf{x} = P\mathbf{y}$ is a one-to-one correspondence between all nonzero $\mathbf{x}$ and all nonzero $\mathbf{y}$. Thus the values of $Q(\mathbf{x})$ for $\mathbf{x} \ne \mathbf{0}$ coincide with the values of the right side of (4) for $\mathbf{y} \ne \mathbf{0}$, which are controlled by the signs of the eigenvalues. In detail (Lay says "obviously"):
> - If all $\lambda_i > 0$ and $\mathbf{y} \ne \mathbf{0}$, then every term $\lambda_i y_i^2 \ge 0$ and at least one is $> 0$, so the sum is $> 0$. Conversely, if some $\lambda_i \le 0$, then $\mathbf{y} = \mathbf{e}_i$ gives the value $\lambda_i \le 0$ at a nonzero vector. This is (a); (b) is the same with signs reversed.
> - If $\lambda_i > 0$ and $\lambda_j < 0$, then $\mathbf{y} = \mathbf{e}_i$ and $\mathbf{y} = \mathbf{e}_j$ give values of both signs. Conversely, if all $\lambda_i \ge 0$, every value of (4) is $\ge 0$, and if all $\lambda_i \le 0$ every value is $\le 0$; so values of both signs force eigenvalues of both signs. This is (c).

^pf-49-4

*Uses:* [[§49★ Quadratic Forms#^thm-49-2|§49.2]], [[§49★ Quadratic Forms#^def-49-4|Def. §49.4]]

> [!remark]- Connections
> - The second derivative test: at a critical point, $f(\mathbf{a} + \mathbf{h}) - f(\mathbf{a}) \approx \frac12 \mathbf{h}^T H \mathbf{h}$ with $H$ the (symmetric) Hessian, so a positive definite Hessian means a local minimum, negative definite a local maximum, indefinite a saddle: [[§14 Optimization and Lagrange Multipliers#^def-14-3|452 Def. §14.3]], [[§14 Optimization and Lagrange Multipliers#^thm-14-4|452 Thm. §14.4]] (hub [[Second Derivative Test in Several Variables]]); the $2 \times 2$ version with $D = f_{xx}f_{yy} - f_{xy}^2$ is [[§96 Maximum and Minimum Values#^thm-96-2|Calc Thm. §96.2]], and $D = \det H = \lambda_1\lambda_2$ and $f_{xx}$ together decide the signs of the eigenvalues. Determinant tests in $n$ variables: [[§14 Optimization and Lagrange Multipliers#^rem-14-9|452 Remark: Sylvester's Criterion]].
> - Operator version: [[§24 Positive Operators#^ladr-7-38|LADR 7.38]] — a self-adjoint $T$ with $\langle Tv, v \rangle \ge 0$ (Axler's "positive", Lay's positive semidefinite) has all eigenvalues $\ge 0$, has a positive square root, and is $R^*R$ for some $R$.

> [!theorem] Proposition §49.5: Positive Semidefinite Forms and Eigenvalues
> Let $A$ be symmetric. The quadratic form $\mathbf{x}^T A \mathbf{x}$ is positive semidefinite if and only if all eigenvalues of $A$ are nonnegative. (Likewise negative semidefinite if and only if all eigenvalues are $\le 0$.)
>
> *Lay: 7.2, Practice Problem*

^prop-49-5

> [!proof]+ Proof
> Make an orthogonal change of variable $\mathbf{x} = P\mathbf{y}$ and write $\mathbf{x}^T A \mathbf{x} = \mathbf{y}^T D \mathbf{y} = \lambda_1 y_1^2 + \cdots + \lambda_n y_n^2$ as in (4). If some eigenvalue $\lambda_i$ were negative, then $\mathbf{x}^T A \mathbf{x}$ would be negative for the $\mathbf{x}$ corresponding to $\mathbf{y} = \mathbf{e}_i$ (namely $\mathbf{x} = P\mathbf{e}_i$, the $i$th column of $P$): its value is $\lambda_i < 0$. So the eigenvalues of a positive semidefinite form are all nonnegative. Conversely, if all $\lambda_i \ge 0$, every term of the expansion is $\ge 0$, so $\mathbf{x}^T A \mathbf{x} \ge 0$ for all $\mathbf{x}$.

^pf-49-5

*Uses:* [[§49★ Quadratic Forms#^thm-49-2|§49.2]]

> [!definition] Definition §49.5: Positive Definite Matrix
> The classification of a quadratic form is often carried over to its matrix. Thus a **positive definite matrix** $A$ is a *symmetric* matrix for which the quadratic form $\mathbf{x}^T A \mathbf{x}$ is positive definite. Other terms, such as **positive semidefinite matrix**, negative definite matrix and indefinite matrix, are defined analogously.
>
> *Lay: 7.2 (text)*

^def-49-5

> [!example] Example §49.4: A Form That Looks Positive Definite
> Is $Q(\mathbf{x}) = 3x_1^2 + 2x_2^2 + x_3^2 + 4x_1x_2 + 4x_2x_3$ positive definite?
>
> Because of all the plus signs, the form "looks" positive definite. Its matrix is
>
> $$
> A = \begin{bmatrix} 3 & 2 & 0 \\ 2 & 2 & 2 \\ 0 & 2 & 1 \end{bmatrix}.
> $$
>
> Expanding $\det(A - \lambda I)$ along the first row,
>
> $$
> (3 - \lambda)\big[(2 - \lambda)(1 - \lambda) - 4\big] - 2\big[2(1 - \lambda)\big] = (3 - \lambda)(\lambda^2 - 3\lambda - 2) - 4 + 4\lambda = -\lambda^3 + 6\lambda^2 - 3\lambda - 10 ,
> $$
>
> and $-\lambda^3 + 6\lambda^2 - 3\lambda - 10 = -(\lambda - 5)(\lambda - 2)(\lambda + 1)$. The eigenvalues are $5$, $2$ and $-1$: both signs occur, so by Theorem §49.4 $Q$ is **indefinite**, not positive definite.
>
> To see a negative value, take an eigenvector for $-1$: $A + I = \begin{bmatrix} 4 & 2 & 0 \\ 2 & 3 & 2 \\ 0 & 2 & 2 \end{bmatrix}$ has null space spanned by $\mathbf{x} = (1, -2, 2)$, and
>
> $$
> Q(1, -2, 2) = 3 + 8 + 4 + 4(1)(-2) + 4(-2)(2) = 15 - 8 - 16 = -9 = -1 \cdot \|\mathbf{x}\|^2 ,
> $$
>
> while $Q(1, 0, 0) = 3 > 0$.
>
> *Lay: Example 7.2.6*

^ex-49-4

> [!remark] Remark: Method — Classifying a Quadratic Form
> 1. Write the symmetric matrix $A$ of the form.
> 2. Find the eigenvalues of $A$ (they are real by [[§48★ Diagonalization of Symmetric Matrices#^thm-48-3|Theorem §48.3]]); eigenvectors are not needed.
> 3. Read off the type from their signs (Theorem §49.4 and Proposition §49.5): all $> 0$ positive definite; all $< 0$ negative definite; both signs indefinite; all $\ge 0$ with some $= 0$ positive semidefinite (but not definite); all $\le 0$ with some $= 0$ negative semidefinite.
> 4. For a $2 \times 2$ matrix $\begin{bmatrix} a & b \\ b & d \end{bmatrix}$, $\lambda_1\lambda_2 = \det A$ and $\lambda_1 + \lambda_2 = a + d$, so: $\det A > 0$ and $a > 0$ gives positive definite, $\det A > 0$ and $a < 0$ negative definite, $\det A < 0$ indefinite (Lay's Exercises 23–24).

^rem-49-2

> [!remark]- Remark: Numerical Note — Cholesky Factorization
> A fast way to decide whether a symmetric matrix $A$ is positive definite is to attempt to factor $A = R^T R$ with $R$ upper triangular with positive diagonal entries (a slightly modified LU factorization does this). Such a **Cholesky factorization** exists if and only if $A$ is positive definite (Lay's Supplementary Exercise 7 of Chapter 7). One direction is immediate: if $A = R^TR$ with $R$ invertible, then $\mathbf{x}^TA\mathbf{x} = (R\mathbf{x})^T(R\mathbf{x}) = \|R\mathbf{x}\|^2 > 0$ for $\mathbf{x} \ne \mathbf{0}$. The operator version is [[§25 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-63|LADR 7.63]].

^rem-49-3
