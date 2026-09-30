---
subject: math
type: example
source: "[[Group Theory]]"
tags: ["math493", "workhorse"]
---
The general linear group $GL_n(k)$ of invertible $n \times n$ matrices over a field $k$, with its subgroups $SL_n(k)$ (determinant $1$), $O(n)$ ($A^{\mathsf{T}}A = I$) and $SO(n)$. Alongside $S_n$ it is one of the two fundamental families of non-abelian groups, and it contains copies of essentially every group in the course, since every finite group embeds in some $GL_n(k)$ through permutation matrices. The determinant is the model homomorphism and character: its kernel $SL_n$ is normal, $GL_n/SL_n \cong k^\times$, and conjugacy in $GL_n$ is similarity of matrices. Its uses in MATH 493:

- $GL_n(k)$ is a group, non-abelian for $n \geq 2$ ([[§3 Basic Examples of Groups#^def-3-6|§3]])
- The subgroups $SL_n(k)$, $O(n)$ and $SO(n)$ ([[§3 Basic Examples of Groups#^def-3-7|§3]])
- $S_n$ and $GL_n(k)$ are the two fundamental non-abelian families ([[§3 Basic Examples of Groups#^rem-3-2|§3]])
- A zoo of subgroups of $GL_2(\mathbb{R})$ and $GL_3(\mathbb{R})$ ([[§5 A Zoo of Subgroups#^ex-5-4|§5]])
- $GL_n(\mathbb{R})$ contains copies of essentially every group we meet ([[§5 A Zoo of Subgroups#^rem-5-3|§5]])
- $\det$ is a homomorphism with kernel $SL_n$ ([[§15 Homomorphisms#^ex-15-1|§15]])
- Permutation matrices give an injective homomorphism $S_n \to GL_n(k)$ ([[§19 Polynomial Rings, Permutation Matrices, and Representations#^prop-19-5|§19]])
- A representation is a homomorphism into $GL_n(k)$ ([[§19 Polynomial Rings, Permutation Matrices, and Representations#^def-19-6|§19]])
- The sign factors as $\operatorname{sgn} = \det \circ M$ ([[§20 The Sign Homomorphism and the Alternating Group#^rem-20-2|§20]])
- $GL_n(k)$ acts on $k^n$ ([[§23 Actions#^ex-23-2|§23]])
- Every finite group is a matrix group ([[§23 Actions#^cor-23-6|§23]])
- $GL_3(\mathbb{R})$ acting on $\mathbb{R}^3$: two orbits, and the stabilizer of $e_1$ ([[§30 Examples꞉ Linear Groups and the Cube#^prop-30-1|§30]])
- $GL_3$ versus $O_3$: orbits and stabilizers compared ([[§30 Examples꞉ Linear Groups and the Cube#^rem-30-1|§30]])
- $O_3(\mathbb{R})$ acting on $\mathbb{R}^3$: the orbits are spheres ([[§30 Examples꞉ Linear Groups and the Cube#^prop-30-2|§30]])
- Conjugacy in $GL_n(\mathbb{C})$ is similarity ([[§31 Conjugacy Classes#^def-31-3|§31]])
- The conjugacy class of $\operatorname{diag}(3, 4)$: trace $7$, determinant $12$ ([[§31 Conjugacy Classes#^prop-31-3|§31]])
- Scalar matrices are central; Jordan form in general ([[§31 Conjugacy Classes#^rem-31-1|§31]])
- Conjugacy classes of matrices as orbits of $GL_n(\mathbb{C})$ ([[§32 Conjugation as an Action and the Class Equation#^rem-32-2|§32]])
- $SL_n(\mathbb{R}) = \operatorname{Ker}(\det)$ is normal ([[§36 Sources of Normal Subgroups#^ex-36-2|§36]])
- Normal and non-normal subgroups of $GL_2(\mathbb{R})$ ([[§36 Sources of Normal Subgroups#^prop-36-8|§36]])
- $GL_n(k)/SL_n(k) \cong k^\times$ ([[§38 The First Isomorphism Theorem#^ex-38-1|§38]])
- The projective special linear group $PSL_n(F) = SL_n(F)/Z$ ([[§39 Simple Groups#^def-39-2|§39]])
- $PSL_n(F)$ is simple, with two exceptions ([[§39 Simple Groups#^thm-39-13|§39]])
- The exceptions: $PSL_2(\mathbb{F}_2) \cong S_3$ and $PSL_2(\mathbb{F}_3) \cong A_4$ ([[§39 Simple Groups#^ex-39-3|§39]])
- $\det$ is a character of $GL_n(k)$ ([[§40 Characters#^ex-40-1|§40]])
- Characters are the representations into $GL_1(k) = k^\times$ ([[§40 Characters#^rem-40-4|§40]])

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
![[§19 Polynomial Rings, Permutation Matrices, and Representations#^prop-19-5]]

## A representation is a homomorphism into $GL_n(k)$
![[§19 Polynomial Rings, Permutation Matrices, and Representations#^def-19-6]]

## The sign factors as $\operatorname{sgn} = \det \circ M$
![[§20 The Sign Homomorphism and the Alternating Group#^rem-20-2]]

## $GL_n(k)$ acts on $k^n$
![[§23 Actions#^ex-23-2]]

## Every finite group is a matrix group
![[§23 Actions#^cor-23-6]]

## $GL_3(\mathbb{R})$ acting on $\mathbb{R}^3$: two orbits, and the stabilizer of $e_1$
![[§30 Examples꞉ Linear Groups and the Cube#^prop-30-1]]

## $GL_3$ versus $O_3$: orbits and stabilizers compared
![[§30 Examples꞉ Linear Groups and the Cube#^rem-30-1]]

## $O_3(\mathbb{R})$ acting on $\mathbb{R}^3$: the orbits are spheres
![[§30 Examples꞉ Linear Groups and the Cube#^prop-30-2]]

## Conjugacy in $GL_n(\mathbb{C})$ is similarity
![[§31 Conjugacy Classes#^def-31-3]]

## The conjugacy class of $\operatorname{diag}(3, 4)$: trace $7$, determinant $12$
![[§31 Conjugacy Classes#^prop-31-3]]

## Scalar matrices are central; Jordan form in general
![[§31 Conjugacy Classes#^rem-31-1]]

## Conjugacy classes of matrices as orbits of $GL_n(\mathbb{C})$
![[§32 Conjugation as an Action and the Class Equation#^rem-32-2]]

## $SL_n(\mathbb{R}) = \operatorname{Ker}(\det)$ is normal
![[§36 Sources of Normal Subgroups#^ex-36-2]]

## Normal and non-normal subgroups of $GL_2(\mathbb{R})$
![[§36 Sources of Normal Subgroups#^prop-36-8]]

## $GL_n(k)/SL_n(k) \cong k^\times$
![[§38 The First Isomorphism Theorem#^ex-38-1]]

## The projective special linear group $PSL_n(F) = SL_n(F)/Z$
![[§39 Simple Groups#^def-39-2]]

## $PSL_n(F)$ is simple, with two exceptions
![[§39 Simple Groups#^thm-39-13]]

## The exceptions: $PSL_2(\mathbb{F}_2) \cong S_3$ and $PSL_2(\mathbb{F}_3) \cong A_4$
![[§39 Simple Groups#^ex-39-3]]

## $\det$ is a character of $GL_n(k)$
![[§40 Characters#^ex-40-1]]

## Characters are the representations into $GL_1(k) = k^\times$
![[§40 Characters#^rem-40-4]]
