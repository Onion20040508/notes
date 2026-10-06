---
subject: math
type: example
source: "[[Differentiable Manifolds]]"
tags: ["math591", "workhorse"]
---
The classical matrix groups $\mathrm{GL}(n,\mathbb{R})$, $\mathrm{SL}(n,\mathbb{R})$, $\mathrm{O}(n)$, $\mathrm{SO}(n)$ and $\mathrm{U}(n)$, topologized as subsets of a Euclidean space of matrices: “our friends for the semester.” $\mathrm{GL}(n,\mathbb{R})$ is open in the space of matrices, and $\mathrm{SL}$, $\mathrm{O}$ and $\mathrm{U}$ are cut out by matrix equations ($\det g = 1$, $gg^{\mathsf T} = I$, $gg^* = I$), so the regular value theorem makes them manifolds, Jacobi's formula and the curve method compute the differentials, and the tangent spaces at the identity (trace-zero, skew-symmetric and skew-Hermitian matrices) are the future Lie algebras. Acting on $\mathbb{R}^n$, on spheres and on subspaces, they also produce the course's orbit spaces and homogeneous spaces. Their algebra (subgroups, the determinant homomorphism) is in [[Matrix groups GLₙ, SLₙ and O(n)]] (MATH 493). Its uses in MATH 591:

- $\mathrm{U}(n)$ is not a holomorphic level set, so it must be treated over $\mathbb{R}$ ([[§7 The Regular Value Theorem#^rem-7-9|§7]])
- $\mathrm{GL}(n,\mathbb{R})$ is a topological group ([[§11 Topological Groups and Classical Matrix Groups#^prop-11-4|§11]])
- $\mathrm{GL}(n,\mathbb{R})$ has exactly two components ([[§16 The Classical Groups#^thm-16-2|§16]])
- $g \in \mathrm{O}(n)$ iff $g^{\mathsf T}g = I$, so $\det g = \pm 1$ ([[§11 Topological Groups and Classical Matrix Groups#^prop-11-5|§11]])
- $\mathrm{SO}(n)$ is a proper subgroup of $\mathrm{O}(n)$: reflections ([[§16 The Classical Groups#^ex-16-1|§16]])
- The complex groups $\mathrm{GL}(n,\mathbb{C})$ and $\mathrm{U}(n)$ ([[§11 Topological Groups and Classical Matrix Groups#^def-11-9|§11]], [[§11 Topological Groups and Classical Matrix Groups#^def-11-10|§11]])
- $\mathrm{U}(1)$ is the circle ([[§11 Topological Groups and Classical Matrix Groups#^ex-11-3|§11]])
- The classical groups are topological manifolds ([[§12 The Classical Groups Are Topological Manifolds#^thm-12-6|§12]])
- Jacobi's formula for the derivative of $\det$ ([[§12 The Classical Groups Are Topological Manifolds#^prop-12-1|§12]])
- $1$ is a regular value of $\det$ ([[§12 The Classical Groups Are Topological Manifolds#^cor-12-3|§12]])
- $\mathrm{SL}(n,\mathbb{R})$ is a manifold of dimension $n^2 - 1$ ([[§12 The Classical Groups Are Topological Manifolds#^cor-12-5|§12]])
- Dimension count: one equation for $\mathrm{SL}$, $\tfrac{n(n+1)}{2}$ for $\mathrm{O}(n)$ ([[§12 The Classical Groups Are Topological Manifolds#^rem-12-3|§12]])
- Matrix groups act on column vectors ([[§13 Group Actions and Orbit Spaces#^ex-13-1|§13]])
- $\mathrm{SO}(2)$ acting on $\mathbb{R}^2$: the orbit space is $[0, \infty)$ ([[§13 Group Actions and Orbit Spaces#^ex-13-4|§13]])
- $\mathrm{SO}(3)$ acting on $\mathbb{R}^3$: the orbits are spheres ([[§13 Group Actions and Orbit Spaces#^ex-13-5|§13]])
- The isotropy of the north pole under $\mathrm{SO}(3)$ is $\mathrm{SO}(2)$ ([[§14 Homogeneous Spaces#^ex-14-2|§14]])
- $S^2 \cong \mathrm{SO}(3)/\mathrm{SO}(2)$ ([[§14 Homogeneous Spaces#^ex-14-3|§14]])
- Grassmannians are homogeneous spaces $\mathrm{O}(n)/(\mathrm{O}(k) \times \mathrm{O}(n-k))$ ([[§15 The Topology of G∕H and Real Grassmannians#^cor-15-8|§15]])
- $\mathrm{O}(n)$ is a smooth manifold of dimension $\tfrac{n(n-1)}{2}$ ([[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-23-1|§23]])
- For $\mathrm{O}(n)$, the kernel of the differential is $g \cdot \operatorname{Skew}(n,\mathbb{R})$ ([[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^prop-23-1|§23]])
- Two readings of $\dim \mathrm{O}(n)$: level-set count and kernel count ([[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^rem-23-3|§23]])
- $\mathrm{SO}(n)$ is a smooth manifold and $\mathrm{O}(n)$ is compact ([[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^cor-23-2|§23]])
- $\mathrm{U}(n)$ is a smooth manifold of dimension $n^2$ ([[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-23-2|§23]])
- $\mathrm{U}(n)$ is compact ([[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^cor-23-5|§23]])
- $T_I\mathrm{O}(n) = \operatorname{Skew}(n,\mathbb{R})$ ([[§25 The Geometric Tangent Space#^ex-25-2|§25]])
- $T_I\mathrm{U}(n) = \mathfrak{u}(n)$, the skew-Hermitian matrices ([[§25 The Geometric Tangent Space#^ex-25-3|§25]])
- Summary: dimensions and tangent spaces of the classical groups ([[§25 The Geometric Tangent Space#^thm-25-5|§25]])
- The adjoint action of $G$ on its tangent space at $I$ ([[§25 The Geometric Tangent Space#^prop-25-6|§25]])
- $\mathrm{SO}(3)$ and infinitesimal rotations: the hat map ([[§25 The Geometric Tangent Space#^ex-25-4|§25]])
- Dimension checks through homogeneous spaces of classical groups ([[§25 The Geometric Tangent Space#^rem-25-9|§25]])

## $\mathrm{U}(n)$ is not a holomorphic level set, so it must be treated over $\mathbb{R}$
![[§7 The Regular Value Theorem#^rem-7-9]]

## $\mathrm{GL}(n,\mathbb{R})$ is a topological group
![[§11 Topological Groups and Classical Matrix Groups#^prop-11-4]]

## $\mathrm{GL}(n,\mathbb{R})$ has exactly two components
![[§16 The Classical Groups#^thm-16-2]]

## $g \in \mathrm{O}(n)$ iff $g^{\mathsf T}g = I$, so $\det g = \pm 1$
![[§11 Topological Groups and Classical Matrix Groups#^prop-11-5]]

## $\mathrm{SO}(n)$ is a proper subgroup of $\mathrm{O}(n)$: reflections
![[§16 The Classical Groups#^ex-16-1]]

## The complex groups $\mathrm{GL}(n,\mathbb{C})$ and $\mathrm{U}(n)$
![[§11 Topological Groups and Classical Matrix Groups#^def-11-9]]

![[§11 Topological Groups and Classical Matrix Groups#^def-11-10]]

## $\mathrm{U}(1)$ is the circle
![[§11 Topological Groups and Classical Matrix Groups#^ex-11-3]]

## The classical groups are topological manifolds
![[§12 The Classical Groups Are Topological Manifolds#^thm-12-6]]

## Jacobi's formula for the derivative of $\det$
![[§12 The Classical Groups Are Topological Manifolds#^prop-12-1]]

## $1$ is a regular value of $\det$
![[§12 The Classical Groups Are Topological Manifolds#^cor-12-3]]

## $\mathrm{SL}(n,\mathbb{R})$ is a manifold of dimension $n^2 - 1$
![[§12 The Classical Groups Are Topological Manifolds#^cor-12-5]]

## Dimension count: one equation for $\mathrm{SL}$, $\tfrac{n(n+1)}{2}$ for $\mathrm{O}(n)$
![[§12 The Classical Groups Are Topological Manifolds#^rem-12-3]]

## Matrix groups act on column vectors
![[§13 Group Actions and Orbit Spaces#^ex-13-1]]

## $\mathrm{SO}(2)$ acting on $\mathbb{R}^2$: the orbit space is $[0, \infty)$
![[§13 Group Actions and Orbit Spaces#^ex-13-4]]

## $\mathrm{SO}(3)$ acting on $\mathbb{R}^3$: the orbits are spheres
![[§13 Group Actions and Orbit Spaces#^ex-13-5]]

## The isotropy of the north pole under $\mathrm{SO}(3)$ is $\mathrm{SO}(2)$
![[§14 Homogeneous Spaces#^ex-14-2]]

## $S^2 \cong \mathrm{SO}(3)/\mathrm{SO}(2)$
![[§14 Homogeneous Spaces#^ex-14-3]]

## Grassmannians are homogeneous spaces $\mathrm{O}(n)/(\mathrm{O}(k) \times \mathrm{O}(n-k))$
![[§15 The Topology of G∕H and Real Grassmannians#^cor-15-8]]

## $\mathrm{O}(n)$ is a smooth manifold of dimension $\tfrac{n(n-1)}{2}$
![[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-23-1]]

## For $\mathrm{O}(n)$, the kernel of the differential is $g \cdot \operatorname{Skew}(n,\mathbb{R})$
![[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^prop-23-1]]

## Two readings of $\dim \mathrm{O}(n)$: level-set count and kernel count
![[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^rem-23-3]]

## $\mathrm{SO}(n)$ is a smooth manifold and $\mathrm{O}(n)$ is compact
![[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^cor-23-2]]

## $\mathrm{U}(n)$ is a smooth manifold of dimension $n^2$
![[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-23-2]]

## $\mathrm{U}(n)$ is compact
![[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^cor-23-5]]

## $T_I\mathrm{O}(n) = \operatorname{Skew}(n,\mathbb{R})$
![[§25 The Geometric Tangent Space#^ex-25-2]]

## $T_I\mathrm{U}(n) = \mathfrak{u}(n)$, the skew-Hermitian matrices
![[§25 The Geometric Tangent Space#^ex-25-3]]

## Summary: dimensions and tangent spaces of the classical groups
![[§25 The Geometric Tangent Space#^thm-25-5]]

## The adjoint action of $G$ on its tangent space at $I$
![[§25 The Geometric Tangent Space#^prop-25-6]]

## $\mathrm{SO}(3)$ and infinitesimal rotations: the hat map
![[§25 The Geometric Tangent Space#^ex-25-4]]

## Dimension checks through homogeneous spaces of classical groups
![[§25 The Geometric Tangent Space#^rem-25-9]]
