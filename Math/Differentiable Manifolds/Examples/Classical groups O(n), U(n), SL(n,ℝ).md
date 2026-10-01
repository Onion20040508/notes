---
subject: math
type: example
source: "[[Differentiable Manifolds]]"
tags: ["math591", "workhorse"]
---
The classical matrix groups $\mathrm{GL}(n,\mathbb{R})$, $\mathrm{SL}(n,\mathbb{R})$, $\mathrm{O}(n)$, $\mathrm{SO}(n)$ and $\mathrm{U}(n)$, topologized as subsets of a Euclidean space of matrices: “our friends for the semester.” $\mathrm{GL}(n,\mathbb{R})$ is open in the space of matrices, and $\mathrm{SL}$, $\mathrm{O}$ and $\mathrm{U}$ are cut out by matrix equations ($\det g = 1$, $gg^{\mathsf T} = I$, $gg^* = I$), so the regular value theorem makes them manifolds, Jacobi's formula and the curve method compute the differentials, and the tangent spaces at the identity (trace-zero, skew-symmetric and skew-Hermitian matrices) are the future Lie algebras. Acting on $\mathbb{R}^n$, on spheres and on subspaces, they also produce the course's orbit spaces and homogeneous spaces. Their algebra (subgroups, the determinant homomorphism) is in [[Matrix groups GLₙ, SLₙ and O(n)]] (MATH 493). Its uses in MATH 591:

- $\mathrm{U}(n)$ is not a holomorphic level set, so it must be treated over $\mathbb{R}$ ([[§4 The Regular Value Theorem#^rem-4-9|§4]])
- $\mathrm{GL}(n,\mathbb{R})$ is a topological group ([[§5 Topological Groups and Classical Matrix Groups#^prop-5-4|§5]])
- $\mathrm{GL}(n,\mathbb{R})$ has exactly two components ([[§5 Topological Groups and Classical Matrix Groups#^thm-5-6|§5]])
- $g \in \mathrm{O}(n)$ iff $g^{\mathsf T}g = I$, so $\det g = \pm 1$ ([[§5 Topological Groups and Classical Matrix Groups#^prop-5-7|§5]])
- $\mathrm{SO}(n)$ is a proper subgroup of $\mathrm{O}(n)$: reflections ([[§5 Topological Groups and Classical Matrix Groups#^ex-5-3|§5]])
- The complex groups $\mathrm{GL}(n,\mathbb{C})$ and $\mathrm{U}(n)$ ([[§5 Topological Groups and Classical Matrix Groups#^def-5-8|§5]])
- $\mathrm{U}(1)$ is the circle ([[§5 Topological Groups and Classical Matrix Groups#^ex-5-4|§5]])
- The classical groups are topological manifolds ([[§5 Topological Groups and Classical Matrix Groups#^thm-5-8|§5]])
- Jacobi's formula for the derivative of $\det$ ([[§5 Topological Groups and Classical Matrix Groups#^prop-5-9|§5]])
- $1$ is a regular value of $\det$ ([[§5 Topological Groups and Classical Matrix Groups#^cor-5-11|§5]])
- $\mathrm{SL}(n,\mathbb{R})$ is a manifold of dimension $n^2 - 1$ ([[§5 Topological Groups and Classical Matrix Groups#^cor-5-13|§5]])
- Dimension count: one equation for $\mathrm{SL}$, $\tfrac{n(n+1)}{2}$ for $\mathrm{O}(n)$ ([[§5 Topological Groups and Classical Matrix Groups#^rem-5-5|§5]])
- Matrix groups act on column vectors ([[§6 Group Actions and Orbit Spaces#^ex-6-1|§6]])
- $\mathrm{SO}(2)$ acting on $\mathbb{R}^2$: the orbit space is $[0, \infty)$ ([[§6 Group Actions and Orbit Spaces#^ex-6-4|§6]])
- $\mathrm{SO}(3)$ acting on $\mathbb{R}^3$: the orbits are spheres ([[§6 Group Actions and Orbit Spaces#^ex-6-5|§6]])
- The isotropy of the north pole under $\mathrm{SO}(3)$ is $\mathrm{SO}(2)$ ([[§7 Homogeneous Spaces#^ex-7-2|§7]])
- $S^2 \cong \mathrm{SO}(3)/\mathrm{SO}(2)$ ([[§7 Homogeneous Spaces#^ex-7-3|§7]])
- Grassmannians are homogeneous spaces $\mathrm{O}(n)/(\mathrm{O}(k) \times \mathrm{O}(n-k))$ ([[§7 Homogeneous Spaces#^cor-7-13|§7]])
- $\mathrm{O}(n)$ is a smooth manifold of dimension $\tfrac{n(n-1)}{2}$ ([[§10 Vector Spaces and Matrix Groups#^ex-10-1|§10]])
- For $\mathrm{O}(n)$, the kernel of the differential is $g \cdot \operatorname{Skew}(n,\mathbb{R})$ ([[§10 Vector Spaces and Matrix Groups#^prop-10-12|§10]])
- Two readings of $\dim \mathrm{O}(n)$: level-set count and kernel count ([[§10 Vector Spaces and Matrix Groups#^rem-10-9|§10]])
- $\mathrm{SO}(n)$ is a smooth manifold and $\mathrm{O}(n)$ is compact ([[§10 Vector Spaces and Matrix Groups#^cor-10-13|§10]])
- $\mathrm{U}(n)$ is a smooth manifold of dimension $n^2$ ([[§10 Vector Spaces and Matrix Groups#^ex-10-2|§10]])
- $\mathrm{U}(n)$ is compact ([[§10 Vector Spaces and Matrix Groups#^cor-10-16|§10]])
- $T_I\mathrm{O}(n) = \operatorname{Skew}(n,\mathbb{R})$ ([[§11 Tangent Spaces I꞉ The Geometric Picture#^ex-11-2|§11]])
- $T_I\mathrm{U}(n) = \mathfrak{u}(n)$, the skew-Hermitian matrices ([[§11 Tangent Spaces I꞉ The Geometric Picture#^ex-11-3|§11]])
- Summary: dimensions and tangent spaces of the classical groups ([[§11 Tangent Spaces I꞉ The Geometric Picture#^thm-11-5|§11]])
- The adjoint action of $G$ on its tangent space at $I$ ([[§11 Tangent Spaces I꞉ The Geometric Picture#^prop-11-6|§11]])
- $\mathrm{SO}(3)$ and infinitesimal rotations: the hat map ([[§11 Tangent Spaces I꞉ The Geometric Picture#^ex-11-4|§11]])
- Dimension checks through homogeneous spaces of classical groups ([[§11 Tangent Spaces I꞉ The Geometric Picture#^rem-11-9|§11]])

## $\mathrm{U}(n)$ is not a holomorphic level set, so it must be treated over $\mathbb{R}$
![[§4 The Regular Value Theorem#^rem-4-9]]

## $\mathrm{GL}(n,\mathbb{R})$ is a topological group
![[§5 Topological Groups and Classical Matrix Groups#^prop-5-4]]

## $\mathrm{GL}(n,\mathbb{R})$ has exactly two components
![[§5 Topological Groups and Classical Matrix Groups#^thm-5-6]]

## $g \in \mathrm{O}(n)$ iff $g^{\mathsf T}g = I$, so $\det g = \pm 1$
![[§5 Topological Groups and Classical Matrix Groups#^prop-5-7]]

## $\mathrm{SO}(n)$ is a proper subgroup of $\mathrm{O}(n)$: reflections
![[§5 Topological Groups and Classical Matrix Groups#^ex-5-3]]

## The complex groups $\mathrm{GL}(n,\mathbb{C})$ and $\mathrm{U}(n)$
![[§5 Topological Groups and Classical Matrix Groups#^def-5-8]]

## $\mathrm{U}(1)$ is the circle
![[§5 Topological Groups and Classical Matrix Groups#^ex-5-4]]

## The classical groups are topological manifolds
![[§5 Topological Groups and Classical Matrix Groups#^thm-5-8]]

## Jacobi's formula for the derivative of $\det$
![[§5 Topological Groups and Classical Matrix Groups#^prop-5-9]]

## $1$ is a regular value of $\det$
![[§5 Topological Groups and Classical Matrix Groups#^cor-5-11]]

## $\mathrm{SL}(n,\mathbb{R})$ is a manifold of dimension $n^2 - 1$
![[§5 Topological Groups and Classical Matrix Groups#^cor-5-13]]

## Dimension count: one equation for $\mathrm{SL}$, $\tfrac{n(n+1)}{2}$ for $\mathrm{O}(n)$
![[§5 Topological Groups and Classical Matrix Groups#^rem-5-5]]

## Matrix groups act on column vectors
![[§6 Group Actions and Orbit Spaces#^ex-6-1]]

## $\mathrm{SO}(2)$ acting on $\mathbb{R}^2$: the orbit space is $[0, \infty)$
![[§6 Group Actions and Orbit Spaces#^ex-6-4]]

## $\mathrm{SO}(3)$ acting on $\mathbb{R}^3$: the orbits are spheres
![[§6 Group Actions and Orbit Spaces#^ex-6-5]]

## The isotropy of the north pole under $\mathrm{SO}(3)$ is $\mathrm{SO}(2)$
![[§7 Homogeneous Spaces#^ex-7-2]]

## $S^2 \cong \mathrm{SO}(3)/\mathrm{SO}(2)$
![[§7 Homogeneous Spaces#^ex-7-3]]

## Grassmannians are homogeneous spaces $\mathrm{O}(n)/(\mathrm{O}(k) \times \mathrm{O}(n-k))$
![[§7 Homogeneous Spaces#^cor-7-13]]

## $\mathrm{O}(n)$ is a smooth manifold of dimension $\tfrac{n(n-1)}{2}$
![[§10 Vector Spaces and Matrix Groups#^ex-10-1]]

## For $\mathrm{O}(n)$, the kernel of the differential is $g \cdot \operatorname{Skew}(n,\mathbb{R})$
![[§10 Vector Spaces and Matrix Groups#^prop-10-12]]

## Two readings of $\dim \mathrm{O}(n)$: level-set count and kernel count
![[§10 Vector Spaces and Matrix Groups#^rem-10-9]]

## $\mathrm{SO}(n)$ is a smooth manifold and $\mathrm{O}(n)$ is compact
![[§10 Vector Spaces and Matrix Groups#^cor-10-13]]

## $\mathrm{U}(n)$ is a smooth manifold of dimension $n^2$
![[§10 Vector Spaces and Matrix Groups#^ex-10-2]]

## $\mathrm{U}(n)$ is compact
![[§10 Vector Spaces and Matrix Groups#^cor-10-16]]

## $T_I\mathrm{O}(n) = \operatorname{Skew}(n,\mathbb{R})$
![[§11 Tangent Spaces I꞉ The Geometric Picture#^ex-11-2]]

## $T_I\mathrm{U}(n) = \mathfrak{u}(n)$, the skew-Hermitian matrices
![[§11 Tangent Spaces I꞉ The Geometric Picture#^ex-11-3]]

## Summary: dimensions and tangent spaces of the classical groups
![[§11 Tangent Spaces I꞉ The Geometric Picture#^thm-11-5]]

## The adjoint action of $G$ on its tangent space at $I$
![[§11 Tangent Spaces I꞉ The Geometric Picture#^prop-11-6]]

## $\mathrm{SO}(3)$ and infinitesimal rotations: the hat map
![[§11 Tangent Spaces I꞉ The Geometric Picture#^ex-11-4]]

## Dimension checks through homogeneous spaces of classical groups
![[§11 Tangent Spaces I꞉ The Geometric Picture#^rem-11-9]]
