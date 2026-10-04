---
subject: math
type: theorem
source: "[[Applied Linear Algebra]]"
aliases: ["MATH 235 34.1"]
tags: [applied-linear-algebra, hub]
---
![[§34 Diagonalization#^thm-34-1]]

## Treated in
- [[§34 Diagonalization#^thm-34-1|Theorem §34.1: The Diagonalization Theorem]], in [[§34 Diagonalization]]

## Its proof uses
- [[§11 Matrix Operations#^def-11-3|Definition §11.3: Matrix Product]]
- [[§13 Characterizations of Invertible Matrices#^thm-13-1|Theorem §13.1: The Invertible Matrix Theorem]]
- [[§32 Eigenvectors and Eigenvalues#^def-32-1|Definition §32.1: Eigenvector and Eigenvalue]]
- [[§34 Diagonalization#^def-34-1|Definition §34.1: Diagonalizable Matrix]]

## Used in (Applied Linear Algebra)
- [[§34 Diagonalization#^thm-34-2|Theorem §34.2: Distinct Eigenvalues Imply Diagonalizable]]
- [[§34 Diagonalization#^thm-34-3|Theorem §34.3: Diagonalizability and Multiplicities]]
- [[§37 Discrete Dynamical Systems#^thm-37-4|Theorem §37.4: Decoupling by a Change of Variable]]
- [[§38 Applications to Differential Equations#^thm-38-3|Theorem §38.3: General Solution for Diagonalizable A]]
- [[§48★ Diagonalization of Symmetric Matrices#^ex-48-1|Example §48.1: Diagonalizing a Symmetric Matrix with Distinct Eigenvalues]]

## Connections
- Rigorous treatment: [[§17 Diagonalizable Operators#^ladr-5-50|LADR 5.50]] (an operator is diagonalizable if it has a diagonal matrix in *some* basis) and [[§17 Diagonalizable Operators#^ladr-5-55|LADR 5.55]] (equivalent: a basis of eigenvectors; $V$ is the direct sum of the eigenspaces; the eigenspace dimensions add up to $\dim V$). Axler's (a) $\Leftrightarrow$ (b) is the operator form of $AP = PD$; that $D = P^{-1}AP$ is the matrix of $\mathbf{x} \mapsto A\mathbf{x}$ in the basis of columns of $P$ is [[§35 Eigenvectors and Linear Transformations#^thm-35-2|Theorem §35.2]].
- A further criterion with no counterpart in Lay: diagonalizable $\Leftrightarrow$ the minimal polynomial has distinct linear factors, [[§17 Diagonalizable Operators#^ladr-5-62|LADR 5.62]].
- **Also in [[Ordinary Differential Equations]]:** [[§33★ Fundamental Matrices#^thm-33-7|331 Thm. §33.7]] (ODE version with worked examples: diagonalizing $A$ uncouples $\mathbf{x}' = A\mathbf{x}$ and gives $e^{At} = \mathbf{T}e^{Dt}\mathbf{T}^{-1}$, [[§33★ Fundamental Matrices#^thm-33-8|331 Thm. §33.8]]).
