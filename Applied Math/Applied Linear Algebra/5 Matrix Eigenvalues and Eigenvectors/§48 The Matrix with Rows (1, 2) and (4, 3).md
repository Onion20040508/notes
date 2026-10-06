---
type: section
subject: "[[Applied Linear Algebra]]"
chapter: 5
section: 48
tags: [applied-linear-algebra, math235]
---
← [[§47 Iterative Estimates for Eigenvalues]] · ↑ [[· 5 Matrix Eigenvalues and Eigenvectors]] · [[§49 Inner Product, Length, and Orthogonality]] →

*Lay, Sections 5.1 and 5.3 (examples revisited) · MATH 235 lecture L18.*

## The Matrix with Rows (1, 2) and (4, 3)

The matrix $A = \begin{bmatrix} 1 & 2 \\ 4 & 3 \end{bmatrix}$ is the lecture's running example in Chapter 5. The items stay in their sections; here they are gathered in course order.

First its powers map the closed first quadrant onto ever narrower wedges, the lecture's motivation for eigenvectors.

![[§40 Eigenvectors and Eigenvalues#^rem-40-1]]

Its eigenvalues $5$ and $-1$, with eigenvectors $(1, 2)$ and $(1, -1)$, then give $A^{10}\mathbf{e}_1$ and explain the shrinking wedges.

![[§40 Eigenvectors and Eigenvalues#^ex-40-5]]

The same eigenvectors, as the columns of $M$, diagonalize it in [[§42 Diagonalization|§42]]: $M^{-1}AM = \operatorname{diag}(5, -1)$.
