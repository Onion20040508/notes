---
subject: math
type: theorem
source: "[[Applied Linear Algebra]]"
aliases: ["MATH 235 42.1"]
tags: [applied-linear-algebra, hub]
---
![[§42 Diagonalization#^thm-42-1]]

## Treated in
- [[§42 Diagonalization#^thm-42-1|Theorem §42.1: The Diagonalization Theorem]], in [[§42 Diagonalization]]

## Its proof uses
- [[§12 Matrix Operations#^def-12-5|Definition §12.5: Matrix Product]]
- [[§16 Characterizations of Invertible Matrices#^thm-16-1|Theorem §16.1: The Invertible Matrix Theorem]]
- [[§40 Eigenvectors and Eigenvalues#^def-40-1|Definition §40.1: Eigenvector and Eigenvalue]]
- [[§42 Diagonalization#^def-42-1|Definition §42.1: Diagonalizable Matrix]]

## Used in (Applied Linear Algebra)
- [[§42 Diagonalization#^thm-42-2|Theorem §42.2: Distinct Eigenvalues Imply Diagonalizable]]
- [[§42 Diagonalization#^thm-42-3|Theorem §42.3: Diagonalizability and Multiplicities]]
- [[§45 Discrete Dynamical Systems#^thm-45-4|Theorem §45.4: Decoupling by a Change of Variable]]
- [[§46 Applications to Differential Equations#^thm-46-3|Theorem §46.3: General Solution for Diagonalizable A]]

## Connections
- Rigorous treatment: [[§17 Diagonalizable Operators#^ladr-5-50|LADR 5.50]] (an operator is diagonalizable if it has a diagonal matrix in *some* basis) and [[§17 Diagonalizable Operators#^ladr-5-55|LADR 5.55]] (equivalent: a basis of eigenvectors; $V$ is the direct sum of the eigenspaces; the eigenspace dimensions add up to $\dim V$). Axler's (a) $\Leftrightarrow$ (b) is the operator form of $AP = PD$; that $D = P^{-1}AP$ is the matrix of $\mathbf{x} \mapsto A\mathbf{x}$ in the basis of columns of $P$ is [[§43 Eigenvectors and Linear Transformations#^thm-43-2|Theorem §43.2]].
- A further criterion with no counterpart in Lay: diagonalizable $\Leftrightarrow$ the minimal polynomial ([[§15 The Minimal Polynomial#^ladr-5-24|LADR 5.24]]) has distinct linear factors, [[§17 Diagonalizable Operators#^ladr-5-62|LADR 5.62]].
- **Also in [[Ordinary Differential Equations]]:** [[§39★ Fundamental Matrices#^thm-39-7|331 Thm. §39.7]] (ODE version with worked examples: diagonalizing $A$ uncouples $\mathbf{x}' = A\mathbf{x}$ and gives $e^{At} = \mathbf{T}e^{Dt}\mathbf{T}^{-1}$, [[§39★ Fundamental Matrices#^thm-39-8|331 Thm. §39.8]]); the eigenvector solutions $\mathbf{v}e^{\lambda t}$ form a fundamental set, [[§37 Homogeneous Linear Systems with Constant Coefficients#^thm-37-2|331 Thm. §37.2]].
