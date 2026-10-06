---
type: section
subject: "[[Linear Algebra]]"
chapter: 8
section: 32
aliases: ["LADR 8 (examples revisited)"]
tags: [linear-algebra]
---
← [[§31 Trace꞉ A Connection Between Matrices and Operators]] · ↑ [[· 8 Operators on Complex Vector Spaces]] · [[§32 Bilinear Forms and Quadratic Forms]] →

Two operators on $\F^3$ recur through Chapter 8: $T(z_1,z_2,z_3)=(4z_2,0,5z_3)$, and $T(z_1,z_2,z_3)=(6z_1+3z_2+4z_3,\ 6z_2+2z_3,\ 7z_3)$ with $\mathcal{M}(T)=\begin{pmatrix}6&3&4\\0&6&2\\0&0&7\end{pmatrix}$. Each part gathers one of them in course order; the items themselves stay in their sections.

## The operator (4z₂, 0, 5z₃)

Here $\nullsp T+\range T$ is not direct, but $\F^3=\nullsp T^3\oplus\range T^3$ ([[§28 Generalized Eigenvectors and Nilpotent Operators#^ladr-8-4|8.4]]). Its eigenvectors are not enough to span, but its generalized eigenvectors for $0$ and $5$ are, and $\C^3=G(0,T)\oplus G(5,T)$.

![[§28 Generalized Eigenvectors and Nilpotent Operators#^ladr-8-6]]

![[§28 Generalized Eigenvectors and Nilpotent Operators#^ladr-8-6-fig]]

![[§28 Generalized Eigenvectors and Nilpotent Operators#^ladr-8-10]]

![[§29 Generalized Eigenspace Decomposition#^ladr-8-21]]

## The operator (6z₁ + 3z₂ + 4z₃, 6z₂ + 2z₃, 7z₃)

Chapter 5 showed it is not diagonalizable. Here its eigenvalues $6,7$ have multiplicities $2$ and $1$, its characteristic polynomial $(z-6)^2(z-7)$ equals the minimal polynomial, and a basis of generalized eigenvectors gives a block diagonal matrix.

![[§29 Generalized Eigenspace Decomposition#^ladr-8-24]]

![[§29 Generalized Eigenspace Decomposition#^ladr-8-27]]

![[§29 Generalized Eigenspace Decomposition#^ladr-8-38]]

*Chain: earlier in [[§17 Diagonalizable Operators#^ladr-5-61|Chapter 5]]*
