---
type: section
subject: "[[Linear Algebra]]"
chapter: 5
section: 19
aliases: ["LADR 5 (examples revisited)"]
tags: [linear-algebra]
---
← [[§18 Commuting Operators]] · ↑ [[· 5 Eigenvalues and Eigenvectors]] · [[§19 Inner Products and Norms]] →

Three examples recur through Chapter 5: the operator on $\F^5$ whose matrix is a companion matrix, the operator $T(x,y,z)=(2x+y,\ 5y+3z,\ 8z)$ on $\F^3$, and the diagonal matrix $\operatorname{diag}(8,5,5)$. Each part gathers one of them in course order; the items themselves stay in their sections.

## The companion operator on F⁵

Its minimal polynomial $z^5-6z+3$ comes from the fast method of [[§15 The Minimal Polynomial#^ladr-5-24|5.24]]. Its eigenvalues are the zeros of that polynomial, which can only be computed numerically; they are distinct, so the operator is diagonalizable.

![[§15 The Minimal Polynomial#^ladr-5-26]]

![[§15 The Minimal Polynomial#^ladr-5-28]]

![[§17 Diagonalizable Operators#^ladr-5-60]]

## The operator (2x + y, 5y + 3z, 8z)

Its standard matrix is upper triangular with diagonal $2,5,8$, so these are its eigenvalues ([[§16 Upper-Triangular Matrices#^ladr-5-41|5.41]]). Three distinct eigenvalues make it diagonalizable ([[§17 Diagonalizable Operators#^ladr-5-58|5.58]]), and its eigenbasis computes $T^{100}$.

![[§16 Upper-Triangular Matrices#^ladr-5-36]]

![[§16 Upper-Triangular Matrices#^ladr-5-42]]

![[§16 Upper-Triangular Matrices#^ladr-5-41-fig]]

![[§17 Diagonalizable Operators#^ladr-5-59]]

## The diagonal matrix diag(8, 5, 5)

Its eigenvalues are $8$ and $5$, and the eigenvalue $5$ has a $2$-dimensional eigenspace. The same matrix pictures the proof that commuting diagonalizable operators are diagonal in a common basis ([[§18 Commuting Operators#^ladr-5-76|5.76]]).

![[§17 Diagonalizable Operators#^ladr-5-49]]

![[§17 Diagonalizable Operators#^ladr-5-53]]

![[§18 Commuting Operators#^ladr-5-76-fig]]
