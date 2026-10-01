---
subject: math
type: example
source: "[[Differentiable Manifolds]]"
tags: ["math591", "workhorse"]
---
Real projective space $\mathbb{RP}^n = S^n/\{\pm 1\}$ and complex projective space $\mathbb{CP}^n = S^{2n+1}/S^1$, equivalently the spaces of real and complex lines through the origin in $\mathbb{R}^{n+1}$ and $\mathbb{C}^{n+1}$. They are “one of the main examples of manifolds”: $\mathbb{CP}^n$ is the course's model quotient, shown Hausdorff first by the Hausdorff criterion and again as the orbit space of a compact group, then given the standard atlas of homogeneous-coordinate charts that makes it a compact complex manifold; $\mathbb{RP}^n$ runs in parallel and is the case $k = 1$ of the [[Grassmannians]]. In low dimension they are spheres, $\mathbb{CP}^1 \cong S^2$ and $\mathbb{RP}^1 \cong S^1$. The quotient map $S^{2n+1} \to \mathbb{CP}^n$ has its own note, [[The Hopf fibration]], and the topology of $\mathbb{RP}^2$, including $\pi_1 \cong \mathbb{Z}/2\mathbb{Z}$, is in [[Projective plane]] (MATH 590). Its uses in MATH 591:

- Definition: $\mathbb{CP}^n = S^{2n+1}/{\sim}$, with $z \sim \xi z$ for $\xi \in S^1$ ([[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^def-3-11|§3]])
- $\mathbb{CP}^n$ is Hausdorff and second countable ([[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^prop-3-29|§3]])
- $\mathbb{CP}^n$ is compact ([[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^prop-3-30|§3]])
- $\mathbb{CP}^n$ as the space of complex lines, $(\mathbb{C}^{n+1} \setminus \{0\})/\mathbb{C}^\times$ ([[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^prop-3-31|§3]])
- Why the origin must be removed before dividing by $\mathbb{C}^\times$ ([[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^ex-3-8|§3]])
- $\mathbb{CP}^n = S^{2n+1}/\mathrm{U}(1)$ is an orbit space ([[§6 Group Actions and Orbit Spaces#^ex-6-3|§6]])
- Hausdorffness of $\mathbb{CP}^n$ as a case of the compact-group criterion ([[§6 Group Actions and Orbit Spaces#^rem-6-9|§6]])
- $\mathbb{RP}^{n-1}$ is the Grassmannian of lines $\mathrm{Gr}_1(\mathbb{R}^n)$ ([[§7 Homogeneous Spaces#^def-7-8|§7]])
- The index: $\mathrm{Gr}_1(\mathbb{R}^n) = \mathbb{RP}^{n-1} \cong S^{n-1}/\{\pm I\}$ ([[§7 Homogeneous Spaces#^rem-7-8|§7]])
- Homogeneous coordinates $[z_0 : \cdots : z_n]$ ([[§8 Differentiable Structures#^def-8-10|§8]])
- The standard charts $\varphi_i([z]) = (z_k/z_i)_{k \neq i}$ on $U_i = \{z_i \neq 0\}$ ([[§8 Differentiable Structures#^def-8-11|§8]])
- Each $\varphi_i$ is a homeomorphism onto $\mathbb{C}^n$ ([[§8 Differentiable Structures#^prop-8-6|§8]])
- The standard atlas is smooth, so $\mathbb{CP}^n$ is a compact $2n$-manifold ([[§8 Differentiable Structures#^thm-8-7|§8]])
- $\mathbb{CP}^n$ is a complex manifold of complex dimension $n$ ([[§8 Differentiable Structures#^cor-8-8|§8]])
- $\mathbb{CP}^1$ is the Riemann sphere $S^2$ ([[§8 Differentiable Structures#^prop-8-9|§8]])
- For $n = 1$ the transition $w \mapsto 1/w$ is the complex stereographic transition ([[§8 Differentiable Structures#^rem-8-12|§8]])
- $\mathbb{RP}^n$ is a compact smooth $n$-manifold with the same kind of atlas ([[§8 Differentiable Structures#^cor-8-10|§8]])
- The quotient and Grassmannian topologies on $\mathbb{RP}^n$ agree, and $\mathbb{RP}^1 \cong S^1$ ([[§8 Differentiable Structures#^prop-8-11|§8]])
- Dimension check: $\mathbb{CP}^n = \mathrm{U}(n+1)/(\mathrm{U}(1) \times \mathrm{U}(n))$ has dimension $2n$ ([[§11 Tangent Spaces I꞉ The Geometric Picture#^rem-11-9|§11]])
- Regular level sets of the moment map $\mathbb{CP}^n \to \mathbb{R}^n$, computed in one chart ([[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^rem-12-15|§12]])
- $S^n \to \mathbb{RP}^n$ is a two-to-one local diffeomorphism ([[§14 Local Diffeomorphisms and Submersions#^ex-14-2|§14]])
- $S^n \to \mathbb{RP}^n$ is a covering map ([[§14 Local Diffeomorphisms and Submersions#^rem-14-2|§14]])

## Definition: $\mathbb{CP}^n = S^{2n+1}/{\sim}$, with $z \sim \xi z$ for $\xi \in S^1$
![[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^def-3-11]]

## $\mathbb{CP}^n$ is Hausdorff and second countable
![[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^prop-3-29]]

## $\mathbb{CP}^n$ is compact
![[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^prop-3-30]]

## $\mathbb{CP}^n$ as the space of complex lines, $(\mathbb{C}^{n+1} \setminus \{0\})/\mathbb{C}^\times$
![[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^prop-3-31]]

## Why the origin must be removed before dividing by $\mathbb{C}^\times$
![[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^ex-3-8]]

## $\mathbb{CP}^n = S^{2n+1}/\mathrm{U}(1)$ is an orbit space
![[§6 Group Actions and Orbit Spaces#^ex-6-3]]

## Hausdorffness of $\mathbb{CP}^n$ as a case of the compact-group criterion
![[§6 Group Actions and Orbit Spaces#^rem-6-9]]

## $\mathbb{RP}^{n-1}$ is the Grassmannian of lines $\mathrm{Gr}_1(\mathbb{R}^n)$
![[§7 Homogeneous Spaces#^def-7-8]]

## The index: $\mathrm{Gr}_1(\mathbb{R}^n) = \mathbb{RP}^{n-1} \cong S^{n-1}/\{\pm I\}$
![[§7 Homogeneous Spaces#^rem-7-8]]

## Homogeneous coordinates $[z_0 : \cdots : z_n]$
![[§8 Differentiable Structures#^def-8-10]]

## The standard charts $\varphi_i([z]) = (z_k/z_i)_{k \neq i}$ on $U_i = \{z_i \neq 0\}$
![[§8 Differentiable Structures#^def-8-11]]

## Each $\varphi_i$ is a homeomorphism onto $\mathbb{C}^n$
![[§8 Differentiable Structures#^prop-8-6]]

## The standard atlas is smooth, so $\mathbb{CP}^n$ is a compact $2n$-manifold
![[§8 Differentiable Structures#^thm-8-7]]

## $\mathbb{CP}^n$ is a complex manifold of complex dimension $n$
![[§8 Differentiable Structures#^cor-8-8]]

## $\mathbb{CP}^1$ is the Riemann sphere $S^2$
![[§8 Differentiable Structures#^prop-8-9]]

## For $n = 1$ the transition $w \mapsto 1/w$ is the complex stereographic transition
![[§8 Differentiable Structures#^rem-8-12]]

## $\mathbb{RP}^n$ is a compact smooth $n$-manifold with the same kind of atlas
![[§8 Differentiable Structures#^cor-8-10]]

## The quotient and Grassmannian topologies on $\mathbb{RP}^n$ agree, and $\mathbb{RP}^1 \cong S^1$
![[§8 Differentiable Structures#^prop-8-11]]

## Dimension check: $\mathbb{CP}^n = \mathrm{U}(n+1)/(\mathrm{U}(1) \times \mathrm{U}(n))$ has dimension $2n$
![[§11 Tangent Spaces I꞉ The Geometric Picture#^rem-11-9]]

## Regular level sets of the moment map $\mathbb{CP}^n \to \mathbb{R}^n$, computed in one chart
![[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^rem-12-15]]

## $S^n \to \mathbb{RP}^n$ is a two-to-one local diffeomorphism
![[§14 Local Diffeomorphisms and Submersions#^ex-14-2]]

## $S^n \to \mathbb{RP}^n$ is a covering map
![[§14 Local Diffeomorphisms and Submersions#^rem-14-2]]
