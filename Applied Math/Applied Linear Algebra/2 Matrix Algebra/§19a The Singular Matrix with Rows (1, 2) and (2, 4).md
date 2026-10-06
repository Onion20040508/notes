---
type: section
subject: "[[Applied Linear Algebra]]"
chapter: 2
section: "19a"
tags: [applied-linear-algebra, math235]
---
← [[§19 Dimension and Rank]] · ↑ [[· 2 Matrix Algebra]] · [[§20 Introduction to Determinants]] →

*Lay, Sections 2.1–2.2 (examples revisited) · MATH 235 lectures L7, L8, L9 · 235 checklist (2.2–2.3).*

## The Singular Matrix with Rows (1, 2) and (2, 4)

The matrix $A = \begin{bmatrix} 1 & 2 \\ 2 & 4 \end{bmatrix}$, whose second row is twice the first, is the running example in Chapter 2 of a nonzero matrix with no inverse. The items stay in their sections; here they are gathered in course order.

First it shows that a product of nonzero matrices can be zero: part (c) below finds every $2 \times 2$ matrix $X$ with $AX = 0$.

![[§11 Matrix Operations#^ex-11-3]]

Such an $X$ then shows that $A$ has no inverse, part (b) below.

![[§12 The Inverse of a Matrix#^ex-12-1]]

For the singular $A$, the matrix equation $AB = C^2$ has no solution for one right side and infinitely many for another (part (b) below, the case "$A$ singular").

![[§12 The Inverse of a Matrix#^ex-12-3]]

Finally the inversion algorithm detects the singularity: in part (c) below, the left half of $[\,A \ \ I\,]$ reduces to a matrix with only one pivot.

![[§12a Elementary Matrices and the Inversion Algorithm#^ex-12-5]]
