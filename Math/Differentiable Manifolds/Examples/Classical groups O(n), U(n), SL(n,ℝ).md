---
subject: math
type: example
source: "[[Differentiable Manifolds]]"
tags: ["math591", "workhorse"]
---
The classical matrix groups $\mathrm{GL}(n,\mathbb{R})$, $\mathrm{SL}(n,\mathbb{R})$, $\mathrm{O}(n)$, $\mathrm{SO}(n)$ and $\mathrm{U}(n)$, topologized as subsets of a Euclidean space of matrices: “our friends for the semester.” $\mathrm{GL}(n,\mathbb{R})$ is open in the space of matrices, and $\mathrm{SL}$, $\mathrm{O}$ and $\mathrm{U}$ are cut out by matrix equations ($\det g = 1$, $gg^{\mathsf T} = I$, $gg^* = I$), so the regular value theorem makes them manifolds, Jacobi's formula and the curve method compute the differentials, and the tangent spaces at the identity (trace-zero, skew-symmetric and skew-Hermitian matrices) are the future Lie algebras. Acting on $\mathbb{R}^n$, on spheres and on subspaces, they also produce the course's orbit spaces and homogeneous spaces. Their algebra (subgroups, the determinant homomorphism) is in [[Matrix groups GLₙ, SLₙ and O(n)]] (MATH 493). Its uses in MATH 591:

- $\mathrm{U}(n)$ is not a holomorphic level set, so it must be treated over $\mathbb{R}$ ([[§7 The Regular Value Theorem#^rem-7-9|§4]])
- $\mathrm{GL}(n,\mathbb{R})$ is a topological group ([[§8 Topological Groups and Classical Matrix Groups#^prop-8-4|§5]])
- $\mathrm{GL}(n,\mathbb{R})$ has exactly two components ([[§8 Topological Groups and Classical Matrix Groups#^thm-8-6|§5]])
- $g \in \mathrm{O}(n)$ iff $g^{\mathsf T}g = I$, so $\det g = \pm 1$ ([[§8 Topological Groups and Classical Matrix Groups#^prop-8-7|§5]])
- $\mathrm{SO}(n)$ is a proper subgroup of $\mathrm{O}(n)$: reflections ([[§8 Topological Groups and Classical Matrix Groups#^ex-8-3|§5]])
- The complex groups $\mathrm{GL}(n,\mathbb{C})$ and $\mathrm{U}(n)$ ([[§8 Topological Groups and Classical Matrix Groups#^def-8-8|§5]])
- $\mathrm{U}(1)$ is the circle ([[§8 Topological Groups and Classical Matrix Groups#^ex-8-4|§5]])
- The classical groups are topological manifolds ([[§9 The Classical Groups Are Topological Manifolds#^thm-9-6|§5]])
- Jacobi's formula for the derivative of $\det$ ([[§9 The Classical Groups Are Topological Manifolds#^prop-9-1|§5]])
- $1$ is a regular value of $\det$ ([[§9 The Classical Groups Are Topological Manifolds#^cor-9-3|§5]])
- $\mathrm{SL}(n,\mathbb{R})$ is a manifold of dimension $n^2 - 1$ ([[§9 The Classical Groups Are Topological Manifolds#^cor-9-5|§5]])
- Dimension count: one equation for $\mathrm{SL}$, $\tfrac{n(n+1)}{2}$ for $\mathrm{O}(n)$ ([[§9 The Classical Groups Are Topological Manifolds#^rem-9-3|§5]])
- Matrix groups act on column vectors ([[§10 Group Actions and Orbit Spaces#^ex-10-1|§6]])
- $\mathrm{SO}(2)$ acting on $\mathbb{R}^2$: the orbit space is $[0, \infty)$ ([[§10 Group Actions and Orbit Spaces#^ex-10-4|§6]])
- $\mathrm{SO}(3)$ acting on $\mathbb{R}^3$: the orbits are spheres ([[§10 Group Actions and Orbit Spaces#^ex-10-5|§6]])
- The isotropy of the north pole under $\mathrm{SO}(3)$ is $\mathrm{SO}(2)$ ([[§11 Homogeneous Spaces#^ex-11-2|§7]])
- $S^2 \cong \mathrm{SO}(3)/\mathrm{SO}(2)$ ([[§11 Homogeneous Spaces#^ex-11-3|§7]])
- Grassmannians are homogeneous spaces $\mathrm{O}(n)/(\mathrm{O}(k) \times \mathrm{O}(n-k))$ ([[§12 The Topology of G∕H and Real Grassmannians#^cor-12-8|§7]])
- $\mathrm{O}(n)$ is a smooth manifold of dimension $\tfrac{n(n-1)}{2}$ ([[§19 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-19-1|§10]])
- For $\mathrm{O}(n)$, the kernel of the differential is $g \cdot \operatorname{Skew}(n,\mathbb{R})$ ([[§19 The Orthogonal and Unitary Groups as Smooth Manifolds#^prop-19-1|§10]])
- Two readings of $\dim \mathrm{O}(n)$: level-set count and kernel count ([[§19 The Orthogonal and Unitary Groups as Smooth Manifolds#^rem-19-3|§10]])
- $\mathrm{SO}(n)$ is a smooth manifold and $\mathrm{O}(n)$ is compact ([[§19 The Orthogonal and Unitary Groups as Smooth Manifolds#^cor-19-2|§10]])
- $\mathrm{U}(n)$ is a smooth manifold of dimension $n^2$ ([[§19 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-19-2|§10]])
- $\mathrm{U}(n)$ is compact ([[§19 The Orthogonal and Unitary Groups as Smooth Manifolds#^cor-19-5|§10]])
- $T_I\mathrm{O}(n) = \operatorname{Skew}(n,\mathbb{R})$ ([[§20 Tangent Spaces I꞉ The Geometric Picture#^ex-20-2|§11]])
- $T_I\mathrm{U}(n) = \mathfrak{u}(n)$, the skew-Hermitian matrices ([[§20 Tangent Spaces I꞉ The Geometric Picture#^ex-20-3|§11]])
- Summary: dimensions and tangent spaces of the classical groups ([[§20 Tangent Spaces I꞉ The Geometric Picture#^thm-20-5|§11]])
- The adjoint action of $G$ on its tangent space at $I$ ([[§20 Tangent Spaces I꞉ The Geometric Picture#^prop-20-6|§11]])
- $\mathrm{SO}(3)$ and infinitesimal rotations: the hat map ([[§20 Tangent Spaces I꞉ The Geometric Picture#^ex-20-4|§11]])
- Dimension checks through homogeneous spaces of classical groups ([[§20 Tangent Spaces I꞉ The Geometric Picture#^rem-20-9|§11]])

## $\mathrm{U}(n)$ is not a holomorphic level set, so it must be treated over $\mathbb{R}$
![[§7 The Regular Value Theorem#^rem-7-9]]

## $\mathrm{GL}(n,\mathbb{R})$ is a topological group
![[§8 Topological Groups and Classical Matrix Groups#^prop-8-4]]

## $\mathrm{GL}(n,\mathbb{R})$ has exactly two components
![[§8 Topological Groups and Classical Matrix Groups#^thm-8-6]]

## $g \in \mathrm{O}(n)$ iff $g^{\mathsf T}g = I$, so $\det g = \pm 1$
![[§8 Topological Groups and Classical Matrix Groups#^prop-8-7]]

## $\mathrm{SO}(n)$ is a proper subgroup of $\mathrm{O}(n)$: reflections
![[§8 Topological Groups and Classical Matrix Groups#^ex-8-3]]

## The complex groups $\mathrm{GL}(n,\mathbb{C})$ and $\mathrm{U}(n)$
![[§8 Topological Groups and Classical Matrix Groups#^def-8-8]]

## $\mathrm{U}(1)$ is the circle
![[§8 Topological Groups and Classical Matrix Groups#^ex-8-4]]

## The classical groups are topological manifolds
![[§9 The Classical Groups Are Topological Manifolds#^thm-9-6]]

## Jacobi's formula for the derivative of $\det$
![[§9 The Classical Groups Are Topological Manifolds#^prop-9-1]]

## $1$ is a regular value of $\det$
![[§9 The Classical Groups Are Topological Manifolds#^cor-9-3]]

## $\mathrm{SL}(n,\mathbb{R})$ is a manifold of dimension $n^2 - 1$
![[§9 The Classical Groups Are Topological Manifolds#^cor-9-5]]

## Dimension count: one equation for $\mathrm{SL}$, $\tfrac{n(n+1)}{2}$ for $\mathrm{O}(n)$
![[§9 The Classical Groups Are Topological Manifolds#^rem-9-3]]

## Matrix groups act on column vectors
![[§10 Group Actions and Orbit Spaces#^ex-10-1]]

## $\mathrm{SO}(2)$ acting on $\mathbb{R}^2$: the orbit space is $[0, \infty)$
![[§10 Group Actions and Orbit Spaces#^ex-10-4]]

## $\mathrm{SO}(3)$ acting on $\mathbb{R}^3$: the orbits are spheres
![[§10 Group Actions and Orbit Spaces#^ex-10-5]]

## The isotropy of the north pole under $\mathrm{SO}(3)$ is $\mathrm{SO}(2)$
![[§11 Homogeneous Spaces#^ex-11-2]]

## $S^2 \cong \mathrm{SO}(3)/\mathrm{SO}(2)$
![[§11 Homogeneous Spaces#^ex-11-3]]

## Grassmannians are homogeneous spaces $\mathrm{O}(n)/(\mathrm{O}(k) \times \mathrm{O}(n-k))$
![[§12 The Topology of G∕H and Real Grassmannians#^cor-12-8]]

## $\mathrm{O}(n)$ is a smooth manifold of dimension $\tfrac{n(n-1)}{2}$
![[§19 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-19-1]]

## For $\mathrm{O}(n)$, the kernel of the differential is $g \cdot \operatorname{Skew}(n,\mathbb{R})$
![[§19 The Orthogonal and Unitary Groups as Smooth Manifolds#^prop-19-1]]

## Two readings of $\dim \mathrm{O}(n)$: level-set count and kernel count
![[§19 The Orthogonal and Unitary Groups as Smooth Manifolds#^rem-19-3]]

## $\mathrm{SO}(n)$ is a smooth manifold and $\mathrm{O}(n)$ is compact
![[§19 The Orthogonal and Unitary Groups as Smooth Manifolds#^cor-19-2]]

## $\mathrm{U}(n)$ is a smooth manifold of dimension $n^2$
![[§19 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-19-2]]

## $\mathrm{U}(n)$ is compact
![[§19 The Orthogonal and Unitary Groups as Smooth Manifolds#^cor-19-5]]

## $T_I\mathrm{O}(n) = \operatorname{Skew}(n,\mathbb{R})$
![[§20 Tangent Spaces I꞉ The Geometric Picture#^ex-20-2]]

## $T_I\mathrm{U}(n) = \mathfrak{u}(n)$, the skew-Hermitian matrices
![[§20 Tangent Spaces I꞉ The Geometric Picture#^ex-20-3]]

## Summary: dimensions and tangent spaces of the classical groups
![[§20 Tangent Spaces I꞉ The Geometric Picture#^thm-20-5]]

## The adjoint action of $G$ on its tangent space at $I$
![[§20 Tangent Spaces I꞉ The Geometric Picture#^prop-20-6]]

## $\mathrm{SO}(3)$ and infinitesimal rotations: the hat map
![[§20 Tangent Spaces I꞉ The Geometric Picture#^ex-20-4]]

## Dimension checks through homogeneous spaces of classical groups
![[§20 Tangent Spaces I꞉ The Geometric Picture#^rem-20-9]]
