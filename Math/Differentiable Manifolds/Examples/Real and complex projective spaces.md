---
subject: math
type: example
source: "[[Differentiable Manifolds]]"
tags: ["math591", "workhorse"]
---
Real projective space $\mathbb{RP}^n = S^n/\{\pm 1\}$ and complex projective space $\mathbb{CP}^n = S^{2n+1}/S^1$, equivalently the spaces of real and complex lines through the origin in $\mathbb{R}^{n+1}$ and $\mathbb{C}^{n+1}$. They are “one of the main examples of manifolds”: $\mathbb{CP}^n$ is the course's model quotient, shown Hausdorff first by the Hausdorff criterion and again as the orbit space of a compact group, then given the standard atlas of homogeneous-coordinate charts that makes it a compact complex manifold; $\mathbb{RP}^n$ runs in parallel and is the case $k = 1$ of the [[Grassmannians]]. In low dimension they are spheres, $\mathbb{CP}^1 \cong S^2$ and $\mathbb{RP}^1 \cong S^1$. The quotient map $S^{2n+1} \to \mathbb{CP}^n$ has its own note, [[The Hopf fibration]], and the topology of $\mathbb{RP}^2$, including $\pi_1 \cong \mathbb{Z}/2\mathbb{Z}$, is in [[Projective plane]] (MATH 590). Its uses in MATH 591:

- Definition: $\mathbb{CP}^n = S^{2n+1}/{\sim}$, with $z \sim \xi z$ for $\xi \in S^1$ ([[§9 Complex Projective Space#^def-9-1|§9]])
- $\mathbb{CP}^n$ is Hausdorff and second countable ([[§9 Complex Projective Space#^prop-9-1|§9]])
- $\mathbb{CP}^n$ is compact ([[§9 Complex Projective Space#^prop-9-2|§9]])
- $\mathbb{CP}^n$ as the space of complex lines, $(\mathbb{C}^{n+1} \setminus \{0\})/\mathbb{C}^\times$ ([[§9 Complex Projective Space#^prop-9-3|§9]])
- Why the origin must be removed before dividing by $\mathbb{C}^\times$ ([[§9 Complex Projective Space#^ex-9-1|§9]])
- $\mathbb{CP}^n = S^{2n+1}/\mathrm{U}(1)$ is an orbit space ([[§13 Group Actions and Orbit Spaces#^ex-13-3|§13]])
- Hausdorffness of $\mathbb{CP}^n$ as a case of the compact-group criterion ([[§13 Group Actions and Orbit Spaces#^rem-13-9|§13]])
- $\mathbb{RP}^{n-1}$ is the Grassmannian of lines $\mathrm{Gr}_1(\mathbb{R}^n)$ ([[§15 The Topology of G∕H and Real Grassmannians#^def-15-3|§15]])
- The index: $\mathrm{Gr}_1(\mathbb{R}^n) = \mathbb{RP}^{n-1} \cong S^{n-1}/\{\pm I\}$ ([[§15 The Topology of G∕H and Real Grassmannians#^rem-15-3|§15]])
- Homogeneous coordinates $[z_0 : \cdots : z_n]$ ([[§18 Projective Spaces as Smooth Manifolds#^def-18-1|§18]])
- The standard charts $\varphi_i([z]) = (z_k/z_i)_{k \neq i}$ on $U_i = \{z_i \neq 0\}$ ([[§18 Projective Spaces as Smooth Manifolds#^def-18-2|§18]])
- Each $\varphi_i$ is a homeomorphism onto $\mathbb{C}^n$ ([[§18 Projective Spaces as Smooth Manifolds#^prop-18-1|§18]])
- The standard atlas is smooth, so $\mathbb{CP}^n$ is a compact $2n$-manifold ([[§18 Projective Spaces as Smooth Manifolds#^thm-18-2|§18]])
- $\mathbb{CP}^n$ is a complex manifold of complex dimension $n$ ([[§18 Projective Spaces as Smooth Manifolds#^cor-18-3|§18]])
- $\mathbb{CP}^1$ is the Riemann sphere $S^2$ ([[§18 Projective Spaces as Smooth Manifolds#^prop-18-4|§18]])
- For $n = 1$ the transition $w \mapsto 1/w$ is the complex stereographic transition ([[§18 Projective Spaces as Smooth Manifolds#^rem-18-2|§18]])
- $\mathbb{RP}^n$ is a compact smooth $n$-manifold with the same kind of atlas ([[§18 Projective Spaces as Smooth Manifolds#^cor-18-5|§18]])
- The quotient and Grassmannian topologies on $\mathbb{RP}^n$ agree, and $\mathbb{RP}^1 \cong S^1$ ([[§18 Projective Spaces as Smooth Manifolds#^prop-18-6|§18]])
- Dimension check: $\mathbb{CP}^n = \mathrm{U}(n+1)/(\mathrm{U}(1) \times \mathrm{U}(n))$ has dimension $2n$ ([[§25 The Geometric Tangent Space#^rem-25-9|§25]])
- Regular level sets of the moment map $\mathbb{CP}^n \to \mathbb{R}^n$, computed in one chart ([[§30 The Differential in Coordinates#^rem-30-5|§30]])
- $S^n \to \mathbb{RP}^n$ is a two-to-one local diffeomorphism ([[§40 Projective Spaces and the Hopf Fibration#^ex-40-1|§39]])
- $S^n \to \mathbb{RP}^n$ is a covering map ([[§33 Local Diffeomorphisms#^rem-33-2|§33]])

## Definition: $\mathbb{CP}^n = S^{2n+1}/{\sim}$, with $z \sim \xi z$ for $\xi \in S^1$
![[§9 Complex Projective Space#^def-9-1]]

## $\mathbb{CP}^n$ is Hausdorff and second countable
![[§9 Complex Projective Space#^prop-9-1]]

## $\mathbb{CP}^n$ is compact
![[§9 Complex Projective Space#^prop-9-2]]

## $\mathbb{CP}^n$ as the space of complex lines, $(\mathbb{C}^{n+1} \setminus \{0\})/\mathbb{C}^\times$
![[§9 Complex Projective Space#^prop-9-3]]

## Why the origin must be removed before dividing by $\mathbb{C}^\times$
![[§9 Complex Projective Space#^ex-9-1]]

## $\mathbb{CP}^n = S^{2n+1}/\mathrm{U}(1)$ is an orbit space
![[§13 Group Actions and Orbit Spaces#^ex-13-3]]

## Hausdorffness of $\mathbb{CP}^n$ as a case of the compact-group criterion
![[§13 Group Actions and Orbit Spaces#^rem-13-9]]

## $\mathbb{RP}^{n-1}$ is the Grassmannian of lines $\mathrm{Gr}_1(\mathbb{R}^n)$
![[§15 The Topology of G∕H and Real Grassmannians#^def-15-3]]

## The index: $\mathrm{Gr}_1(\mathbb{R}^n) = \mathbb{RP}^{n-1} \cong S^{n-1}/\{\pm I\}$
![[§15 The Topology of G∕H and Real Grassmannians#^rem-15-3]]

## Homogeneous coordinates $[z_0 : \cdots : z_n]$
![[§18 Projective Spaces as Smooth Manifolds#^def-18-1]]

## The standard charts $\varphi_i([z]) = (z_k/z_i)_{k \neq i}$ on $U_i = \{z_i \neq 0\}$
![[§18 Projective Spaces as Smooth Manifolds#^def-18-2]]

## Each $\varphi_i$ is a homeomorphism onto $\mathbb{C}^n$
![[§18 Projective Spaces as Smooth Manifolds#^prop-18-1]]

## The standard atlas is smooth, so $\mathbb{CP}^n$ is a compact $2n$-manifold
![[§18 Projective Spaces as Smooth Manifolds#^thm-18-2]]

## $\mathbb{CP}^n$ is a complex manifold of complex dimension $n$
![[§18 Projective Spaces as Smooth Manifolds#^cor-18-3]]

## $\mathbb{CP}^1$ is the Riemann sphere $S^2$
![[§18 Projective Spaces as Smooth Manifolds#^prop-18-4]]

## For $n = 1$ the transition $w \mapsto 1/w$ is the complex stereographic transition
![[§18 Projective Spaces as Smooth Manifolds#^rem-18-2]]

## $\mathbb{RP}^n$ is a compact smooth $n$-manifold with the same kind of atlas
![[§18 Projective Spaces as Smooth Manifolds#^cor-18-5]]

## The quotient and Grassmannian topologies on $\mathbb{RP}^n$ agree, and $\mathbb{RP}^1 \cong S^1$
![[§18 Projective Spaces as Smooth Manifolds#^prop-18-6]]

## Dimension check: $\mathbb{CP}^n = \mathrm{U}(n+1)/(\mathrm{U}(1) \times \mathrm{U}(n))$ has dimension $2n$
![[§25 The Geometric Tangent Space#^rem-25-9]]

## Regular level sets of the moment map $\mathbb{CP}^n \to \mathbb{R}^n$, computed in one chart
![[§30 The Differential in Coordinates#^rem-30-5]]

## $S^n \to \mathbb{RP}^n$ is a two-to-one local diffeomorphism
![[§40 Projective Spaces and the Hopf Fibration#^ex-40-1]]

## $S^n \to \mathbb{RP}^n$ is a covering map
![[§33 Local Diffeomorphisms#^rem-33-2]]
