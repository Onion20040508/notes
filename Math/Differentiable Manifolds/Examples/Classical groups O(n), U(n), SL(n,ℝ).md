---
subject: math
type: example
source: "[[Differentiable Manifolds]]"
tags: ["math591", "workhorse"]
---
The classical matrix groups $\mathrm{GL}(n,\mathbb{R})$, $\mathrm{SL}(n,\mathbb{R})$, $\mathrm{O}(n)$, $\mathrm{SO}(n)$ and $\mathrm{U}(n)$, topologized as subsets of a Euclidean space of matrices: “our friends for the semester.” $\mathrm{GL}(n,\mathbb{R})$ is open in the space of matrices, and $\mathrm{SL}$, $\mathrm{O}$ and $\mathrm{U}$ are cut out by matrix equations ($\det g = 1$, $gg^{\mathsf T} = I$, $gg^* = I$), so the regular value theorem makes them manifolds, Jacobi's formula and the curve method compute the differentials, and the tangent spaces at the identity (trace-zero, skew-symmetric and skew-Hermitian matrices) are the future Lie algebras. Acting on $\mathbb{R}^n$, on spheres and on subspaces, they also produce the course's orbit spaces and homogeneous spaces. Their algebra (subgroups, the determinant homomorphism) is in [[Matrix groups GLₙ, SLₙ and O(n)]] (MATH 493). Its uses in MATH 591:

- $\mathrm{U}(n)$ is not a holomorphic level set, so it must be treated over $\mathbb{R}$ ([[§7 The Regular Value Theorem#^rem-7-9|§7]])
- $\mathrm{GL}(n,\mathbb{R})$ is a topological group ([[§10 Topological Groups and Classical Matrix Groups#^prop-10-4|§10]])
- $\mathrm{GL}(n,\mathbb{R})$ has exactly two components ([[§15 The Classical Groups#^thm-15-2|§15]])
- $g \in \mathrm{O}(n)$ iff $g^{\mathsf T}g = I$, so $\det g = \pm 1$ ([[§10 Topological Groups and Classical Matrix Groups#^prop-10-5|§10]])
- $\mathrm{SO}(n)$ is a proper subgroup of $\mathrm{O}(n)$: reflections ([[§15 The Classical Groups#^ex-15-1|§15]])
- The complex groups $\mathrm{GL}(n,\mathbb{C})$ and $\mathrm{U}(n)$ ([[§10 Topological Groups and Classical Matrix Groups#^def-10-8|§10]])
- $\mathrm{U}(1)$ is the circle ([[§10 Topological Groups and Classical Matrix Groups#^ex-10-3|§10]])
- The classical groups are topological manifolds ([[§11 The Classical Groups Are Topological Manifolds#^thm-11-6|§11]])
- Jacobi's formula for the derivative of $\det$ ([[§11 The Classical Groups Are Topological Manifolds#^prop-11-1|§11]])
- $1$ is a regular value of $\det$ ([[§11 The Classical Groups Are Topological Manifolds#^cor-11-3|§11]])
- $\mathrm{SL}(n,\mathbb{R})$ is a manifold of dimension $n^2 - 1$ ([[§11 The Classical Groups Are Topological Manifolds#^cor-11-5|§11]])
- Dimension count: one equation for $\mathrm{SL}$, $\tfrac{n(n+1)}{2}$ for $\mathrm{O}(n)$ ([[§11 The Classical Groups Are Topological Manifolds#^rem-11-3|§11]])
- Matrix groups act on column vectors ([[§12 Group Actions and Orbit Spaces#^ex-12-1|§12]])
- $\mathrm{SO}(2)$ acting on $\mathbb{R}^2$: the orbit space is $[0, \infty)$ ([[§12 Group Actions and Orbit Spaces#^ex-12-4|§12]])
- $\mathrm{SO}(3)$ acting on $\mathbb{R}^3$: the orbits are spheres ([[§12 Group Actions and Orbit Spaces#^ex-12-5|§12]])
- The isotropy of the north pole under $\mathrm{SO}(3)$ is $\mathrm{SO}(2)$ ([[§13 Homogeneous Spaces#^ex-13-2|§13]])
- $S^2 \cong \mathrm{SO}(3)/\mathrm{SO}(2)$ ([[§13 Homogeneous Spaces#^ex-13-3|§13]])
- Grassmannians are homogeneous spaces $\mathrm{O}(n)/(\mathrm{O}(k) \times \mathrm{O}(n-k))$ ([[§14 The Topology of G∕H and Real Grassmannians#^cor-14-8|§14]])
- $\mathrm{O}(n)$ is a smooth manifold of dimension $\tfrac{n(n-1)}{2}$ ([[§22 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-22-1|§22]])
- For $\mathrm{O}(n)$, the kernel of the differential is $g \cdot \operatorname{Skew}(n,\mathbb{R})$ ([[§22 The Orthogonal and Unitary Groups as Smooth Manifolds#^prop-22-1|§22]])
- Two readings of $\dim \mathrm{O}(n)$: level-set count and kernel count ([[§22 The Orthogonal and Unitary Groups as Smooth Manifolds#^rem-22-3|§22]])
- $\mathrm{SO}(n)$ is a smooth manifold and $\mathrm{O}(n)$ is compact ([[§22 The Orthogonal and Unitary Groups as Smooth Manifolds#^cor-22-2|§22]])
- $\mathrm{U}(n)$ is a smooth manifold of dimension $n^2$ ([[§22 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-22-2|§22]])
- $\mathrm{U}(n)$ is compact ([[§22 The Orthogonal and Unitary Groups as Smooth Manifolds#^cor-22-5|§22]])
- $T_I\mathrm{O}(n) = \operatorname{Skew}(n,\mathbb{R})$ ([[§23 Tangent Spaces I꞉ The Geometric Picture#^ex-23-2|§23]])
- $T_I\mathrm{U}(n) = \mathfrak{u}(n)$, the skew-Hermitian matrices ([[§23 Tangent Spaces I꞉ The Geometric Picture#^ex-23-3|§23]])
- Summary: dimensions and tangent spaces of the classical groups ([[§23 Tangent Spaces I꞉ The Geometric Picture#^thm-23-5|§23]])
- The adjoint action of $G$ on its tangent space at $I$ ([[§23 Tangent Spaces I꞉ The Geometric Picture#^prop-23-6|§23]])
- $\mathrm{SO}(3)$ and infinitesimal rotations: the hat map ([[§23 Tangent Spaces I꞉ The Geometric Picture#^ex-23-4|§23]])
- Dimension checks through homogeneous spaces of classical groups ([[§23 Tangent Spaces I꞉ The Geometric Picture#^rem-23-9|§23]])

## $\mathrm{U}(n)$ is not a holomorphic level set, so it must be treated over $\mathbb{R}$
![[§7 The Regular Value Theorem#^rem-7-9]]

## $\mathrm{GL}(n,\mathbb{R})$ is a topological group
![[§10 Topological Groups and Classical Matrix Groups#^prop-10-4]]

## $\mathrm{GL}(n,\mathbb{R})$ has exactly two components
![[§15 The Classical Groups#^thm-15-2]]

## $g \in \mathrm{O}(n)$ iff $g^{\mathsf T}g = I$, so $\det g = \pm 1$
![[§10 Topological Groups and Classical Matrix Groups#^prop-10-5]]

## $\mathrm{SO}(n)$ is a proper subgroup of $\mathrm{O}(n)$: reflections
![[§15 The Classical Groups#^ex-15-1]]

## The complex groups $\mathrm{GL}(n,\mathbb{C})$ and $\mathrm{U}(n)$
![[§10 Topological Groups and Classical Matrix Groups#^def-10-8]]

## $\mathrm{U}(1)$ is the circle
![[§10 Topological Groups and Classical Matrix Groups#^ex-10-3]]

## The classical groups are topological manifolds
![[§11 The Classical Groups Are Topological Manifolds#^thm-11-6]]

## Jacobi's formula for the derivative of $\det$
![[§11 The Classical Groups Are Topological Manifolds#^prop-11-1]]

## $1$ is a regular value of $\det$
![[§11 The Classical Groups Are Topological Manifolds#^cor-11-3]]

## $\mathrm{SL}(n,\mathbb{R})$ is a manifold of dimension $n^2 - 1$
![[§11 The Classical Groups Are Topological Manifolds#^cor-11-5]]

## Dimension count: one equation for $\mathrm{SL}$, $\tfrac{n(n+1)}{2}$ for $\mathrm{O}(n)$
![[§11 The Classical Groups Are Topological Manifolds#^rem-11-3]]

## Matrix groups act on column vectors
![[§12 Group Actions and Orbit Spaces#^ex-12-1]]

## $\mathrm{SO}(2)$ acting on $\mathbb{R}^2$: the orbit space is $[0, \infty)$
![[§12 Group Actions and Orbit Spaces#^ex-12-4]]

## $\mathrm{SO}(3)$ acting on $\mathbb{R}^3$: the orbits are spheres
![[§12 Group Actions and Orbit Spaces#^ex-12-5]]

## The isotropy of the north pole under $\mathrm{SO}(3)$ is $\mathrm{SO}(2)$
![[§13 Homogeneous Spaces#^ex-13-2]]

## $S^2 \cong \mathrm{SO}(3)/\mathrm{SO}(2)$
![[§13 Homogeneous Spaces#^ex-13-3]]

## Grassmannians are homogeneous spaces $\mathrm{O}(n)/(\mathrm{O}(k) \times \mathrm{O}(n-k))$
![[§14 The Topology of G∕H and Real Grassmannians#^cor-14-8]]

## $\mathrm{O}(n)$ is a smooth manifold of dimension $\tfrac{n(n-1)}{2}$
![[§22 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-22-1]]

## For $\mathrm{O}(n)$, the kernel of the differential is $g \cdot \operatorname{Skew}(n,\mathbb{R})$
![[§22 The Orthogonal and Unitary Groups as Smooth Manifolds#^prop-22-1]]

## Two readings of $\dim \mathrm{O}(n)$: level-set count and kernel count
![[§22 The Orthogonal and Unitary Groups as Smooth Manifolds#^rem-22-3]]

## $\mathrm{SO}(n)$ is a smooth manifold and $\mathrm{O}(n)$ is compact
![[§22 The Orthogonal and Unitary Groups as Smooth Manifolds#^cor-22-2]]

## $\mathrm{U}(n)$ is a smooth manifold of dimension $n^2$
![[§22 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-22-2]]

## $\mathrm{U}(n)$ is compact
![[§22 The Orthogonal and Unitary Groups as Smooth Manifolds#^cor-22-5]]

## $T_I\mathrm{O}(n) = \operatorname{Skew}(n,\mathbb{R})$
![[§23 Tangent Spaces I꞉ The Geometric Picture#^ex-23-2]]

## $T_I\mathrm{U}(n) = \mathfrak{u}(n)$, the skew-Hermitian matrices
![[§23 Tangent Spaces I꞉ The Geometric Picture#^ex-23-3]]

## Summary: dimensions and tangent spaces of the classical groups
![[§23 Tangent Spaces I꞉ The Geometric Picture#^thm-23-5]]

## The adjoint action of $G$ on its tangent space at $I$
![[§23 Tangent Spaces I꞉ The Geometric Picture#^prop-23-6]]

## $\mathrm{SO}(3)$ and infinitesimal rotations: the hat map
![[§23 Tangent Spaces I꞉ The Geometric Picture#^ex-23-4]]

## Dimension checks through homogeneous spaces of classical groups
![[§23 Tangent Spaces I꞉ The Geometric Picture#^rem-23-9]]
