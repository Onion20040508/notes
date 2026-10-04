---
subject: math
type: example
source: "[[Group Theory]]"
tags: ["math493", "workhorse"]
---
The general linear group $GL_n(k)$ of invertible $n \times n$ matrices over a field $k$, with its subgroups $SL_n(k)$ (determinant $1$), $O(n)$ ($A^{\mathsf{T}}A = I$) and $SO(n)$. Alongside $S_n$ it is one of the two fundamental families of non-abelian groups, and it contains copies of essentially every group in the course, since every finite group embeds in some $GL_n(k)$ through permutation matrices. The determinant is the model homomorphism and character: its kernel $SL_n$ is normal, $GL_n/SL_n \cong k^\times$, and conjugacy in $GL_n$ is similarity of matrices. The same groups as topological groups and manifolds (components, smooth structure, tangent spaces at the identity, homogeneous spaces) are in [[Classical groups O(n), U(n), SL(n,ℝ)]] (MATH 591). Its uses in MATH 493:

- $GL_n(k)$ is a group, non-abelian for $n \geq 2$ ([[§3 Basic Examples of Groups#^def-3-6|§3]])
- The subgroups $SL_n(k)$, $O(n)$ and $SO(n)$ ([[§3 Basic Examples of Groups#^def-3-7|§3]])
- $S_n$ and $GL_n(k)$ are the two fundamental non-abelian families ([[§3 Basic Examples of Groups#^rem-3-2|§3]])
- A zoo of subgroups of $GL_2(\mathbb{R})$ and $GL_3(\mathbb{R})$ ([[§5 A Zoo of Subgroups#^ex-5-4|§5]])
- $GL_n(\mathbb{R})$ contains copies of essentially every group we meet ([[§5 A Zoo of Subgroups#^rem-5-3|§5]])
- $\det$ is a homomorphism with kernel $SL_n$ ([[§15 Homomorphisms#^ex-15-1|§15]])
- Permutation matrices give an injective homomorphism $S_n \to GL_n(k)$ ([[§20 Polynomial Rings, Permutation Matrices, and Representations#^prop-20-5|§20]])
- A representation is a homomorphism into $GL_n(k)$ ([[§20 Polynomial Rings, Permutation Matrices, and Representations#^def-20-6|§20]])
- The sign factors as $\operatorname{sgn} = \det \circ M$ ([[§21 The Sign Homomorphism and the Alternating Group#^rem-21-2|§21]])
- $GL_n(k)$ acts on $k^n$ ([[§25 Actions#^ex-25-2|§25]])
- Every finite group is a matrix group ([[§25 Actions#^cor-25-6|§25]])
- $GL_3(\mathbb{R})$ acting on $\mathbb{R}^3$: two orbits, and the stabilizer of $e_1$ ([[§32 Linear Groups, the Cube, S₃ and A₄#^prop-32-1|§32]])
- $GL_3$ versus $O_3$: orbits and stabilizers compared ([[§32 Linear Groups, the Cube, S₃ and A₄#^rem-32-1|§32]])
- $O_3(\mathbb{R})$ acting on $\mathbb{R}^3$: the orbits are spheres ([[§32 Linear Groups, the Cube, S₃ and A₄#^prop-32-2|§32]])
- Conjugacy in $GL_n(\mathbb{C})$ is similarity ([[§33 Conjugacy Classes#^def-33-3|§33]])
- The conjugacy class of $\operatorname{diag}(3, 4)$: trace $7$, determinant $12$ ([[§33 Conjugacy Classes#^prop-33-4|§33]])
- Scalar matrices are central; Jordan form in general ([[§33 Conjugacy Classes#^rem-33-1|§33]])
- Conjugacy classes of matrices as orbits of $GL_n(\mathbb{C})$ ([[§34 Conjugation as an Action and the Class Equation#^rem-34-2|§34]])
- $SL_n(\mathbb{R}) = \operatorname{Ker}(\det)$ is normal ([[§39 Sources of Normal Subgroups#^ex-39-2|§39]])
- Normal and non-normal subgroups of $GL_2(\mathbb{R})$ ([[§39 Sources of Normal Subgroups#^prop-39-8|§39]])
- $GL_n(k)/SL_n(k) \cong k^\times$ ([[§41 The First Isomorphism Theorem#^ex-41-1|§41]])
- The projective special linear group $PSL_n(F) = SL_n(F)/Z$ ([[§43 Simple Groups#^def-43-2|§43]])
- $PSL_n(F)$ is simple, with two exceptions ([[§43 Simple Groups#^thm-43-13|§43]])
- The exceptions: $PSL_2(\mathbb{F}_2) \cong S_3$ and $PSL_2(\mathbb{F}_3) \cong A_4$ ([[§43 Simple Groups#^ex-43-3|§43]])
- $\det$ is a character of $GL_n(k)$ ([[§45 Characters#^ex-45-1|§45]])
- Characters are the representations into $GL_1(k) = k^\times$ ([[§45 Characters#^rem-45-4|§45]])

## Chapter by chapter

Revisit parts for $GL_n$, chapter by chapter: [[§5 A Zoo of Subgroups#GLₙ, SLₙ and O(n)|Chapter 1]] · [[§19 S₃, ℤ∕nℤ and Uₙ#GLₙ, SLₙ and O(n)|Chapter 4]] · [[§23 S₃, Aₙ, Uₙ and GLₙ#GLₙ, SLₙ and O(n)|Chapter 5]] · [[§32 Linear Groups, the Cube, S₃ and A₄#GLₙ, SLₙ and O(n)|Chapter 6]] · [[§36 S₃, S₄ and GLₙ#GLₙ, SLₙ and O(n)|Chapter 7]] · [[§44 S₃, S₄, A₄ and A₅#GLₙ, SLₙ and O(n)|Chapter 8]] · [[§47 S₃, Aₙ and GLₙ#GLₙ, SLₙ and O(n)|Chapter 9]].

## $GL_n(k)$ is a group, non-abelian for $n \geq 2$
![[§3 Basic Examples of Groups#^def-3-6]]

## The subgroups $SL_n(k)$, $O(n)$ and $SO(n)$
![[§3 Basic Examples of Groups#^def-3-7]]

## $S_n$ and $GL_n(k)$ are the two fundamental non-abelian families
![[§3 Basic Examples of Groups#^rem-3-2]]

## A zoo of subgroups of $GL_2(\mathbb{R})$ and $GL_3(\mathbb{R})$
![[§5 A Zoo of Subgroups#^ex-5-4]]

## $GL_n(\mathbb{R})$ contains copies of essentially every group we meet
![[§5 A Zoo of Subgroups#^rem-5-3]]

## $\det$ is a homomorphism with kernel $SL_n$
![[§15 Homomorphisms#^ex-15-1]]

## Permutation matrices give an injective homomorphism $S_n \to GL_n(k)$
![[§20 Polynomial Rings, Permutation Matrices, and Representations#^prop-20-5]]

## A representation is a homomorphism into $GL_n(k)$
![[§20 Polynomial Rings, Permutation Matrices, and Representations#^def-20-6]]

## The sign factors as $\operatorname{sgn} = \det \circ M$
![[§21 The Sign Homomorphism and the Alternating Group#^rem-21-2]]

## $GL_n(k)$ acts on $k^n$
![[§25 Actions#^ex-25-2]]

## Every finite group is a matrix group
![[§25 Actions#^cor-25-6]]

## $GL_3(\mathbb{R})$ acting on $\mathbb{R}^3$: two orbits, and the stabilizer of $e_1$
![[§32 Linear Groups, the Cube, S₃ and A₄#^prop-32-1]]

## $GL_3$ versus $O_3$: orbits and stabilizers compared
![[§32 Linear Groups, the Cube, S₃ and A₄#^rem-32-1]]

## $O_3(\mathbb{R})$ acting on $\mathbb{R}^3$: the orbits are spheres
![[§32 Linear Groups, the Cube, S₃ and A₄#^prop-32-2]]

## Conjugacy in $GL_n(\mathbb{C})$ is similarity
![[§33 Conjugacy Classes#^def-33-3]]

## The conjugacy class of $\operatorname{diag}(3, 4)$: trace $7$, determinant $12$
![[§33 Conjugacy Classes#^prop-33-4]]

## Scalar matrices are central; Jordan form in general
![[§33 Conjugacy Classes#^rem-33-1]]

## Conjugacy classes of matrices as orbits of $GL_n(\mathbb{C})$
![[§34 Conjugation as an Action and the Class Equation#^rem-34-2]]

## $SL_n(\mathbb{R}) = \operatorname{Ker}(\det)$ is normal
![[§39 Sources of Normal Subgroups#^ex-39-2]]

## Normal and non-normal subgroups of $GL_2(\mathbb{R})$
![[§39 Sources of Normal Subgroups#^prop-39-8]]

## $GL_n(k)/SL_n(k) \cong k^\times$
![[§41 The First Isomorphism Theorem#^ex-41-1]]

## The projective special linear group $PSL_n(F) = SL_n(F)/Z$
![[§43 Simple Groups#^def-43-2]]

## $PSL_n(F)$ is simple, with two exceptions
![[§43 Simple Groups#^thm-43-13]]

## The exceptions: $PSL_2(\mathbb{F}_2) \cong S_3$ and $PSL_2(\mathbb{F}_3) \cong A_4$
![[§43 Simple Groups#^ex-43-3]]

## $\det$ is a character of $GL_n(k)$
![[§45 Characters#^ex-45-1]]

## Characters are the representations into $GL_1(k) = k^\times$
![[§45 Characters#^rem-45-4]]
