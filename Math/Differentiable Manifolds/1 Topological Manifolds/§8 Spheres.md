---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 1
section: 8
tags: [differentiable-manifolds, math591]
---
← [[§7 The Regular Value Theorem]] · ↑ [[· 1 Topological Manifolds]] · [[§9 Complex Projective Space]] →

*Thread: examples — The sphere, the first manifold of the course, in one place: $S^2$ by hemisphere charts, every $S^n$ by the same argument, and two overlapping charts whose transition map is already smooth.*

The sphere through the course: a topological manifold with hemisphere charts in *this section*; the homogeneous space $\mathrm{SO}(3)/\mathrm{SO}(2)$ in [[§14 Homogeneous Spaces#^ex-14-3|the sphere as a homogeneous space]]; the Riemann sphere $\mathbb{CP}^1$ in [[§18 Projective Spaces as Smooth Manifolds#^prop-18-4|the Riemann sphere]]; its geometric tangent spaces in [[§25 The Geometric Tangent Space#^ex-25-1|the tangent space of the sphere]] and its transverse intersection with a plane in [[§26 Transversality#^ex-26-1|the sphere and the plane re-read]]; the double cover $S^n \to \mathbb{RP}^n$ and the Hopf fibration $S^{2n+1} \to \mathbb{CP}^n$ in [[§40 Projective Spaces and the Hopf Fibration|Projective Spaces and the Hopf Fibration]]; and $S^3 = \mathrm{SU}(2)$ in [[§41 The Unit Quaternions and SU(2)#^prop-41-5|the unit quaternions as SU(2)]].

> [!example] Example §8.1: $S^2$ is a Topological $2$-Manifold
> Let $S^2 = \{x \in \mathbb{R}^3 \mid |x| = 1\}$ with the subspace topology.
> - *$T_2$ and second countable:* $S^2$ is a metric space (restriction of the Euclidean metric), hence $T_2$; and a subspace of a second countable space is second countable (intersect a countable basis of $\mathbb{R}^3$ with $S^2$).
> - *Locally Euclidean:* let $p = (p_1, p_2, p_3) \in S^2$. Since $|p| = 1$, some coordinate of $p$ is nonzero. Upon relabeling coordinates (and possibly replacing $z$ by $-z$), we may assume **WLOG that the $z$-coordinate of $p$ is positive**. Let
>
>   $$
>   U = \{(x, y, z) \in S^2 \mid z > 0\} \quad \text{(the open northern hemisphere)},
>   $$
>
>   $$
>   \varphi : U \to \mathbb{R}^2, \qquad (x, y, z) \mapsto (x, y).
>   $$
>
>   $U$ is open in $S^2$ (preimage of $(0, \infty)$ under the continuous coordinate function $z$), and $p \in U$.
>
>   **Claim:** $\varphi$ is a homeomorphism of $U$ onto the open unit disk $D = \{(x, y) \mid x^2 + y^2 < 1\} \subseteq \mathbb{R}^2$.
>
> *Lee: Example 1.4*

^ex-8-1

> [!proof]+ Proof of Claim (not given in lecture)
> *Image:* for $(x, y, z) \in U$, $x^2 + y^2 = 1 - z^2 < 1$ since $0 < z \le 1$, so $\varphi(U) \subseteq D$. Conversely, for $(x, y) \in D$, the point $(x, y, \sqrt{1 - x^2 - y^2})$ lies in $U$ and maps to $(x, y)$; so $\varphi(U) = D$.
>
> *Injective:* if $(x, y, z), (x, y, z') \in U$, then $z = \sqrt{1 - x^2 - y^2} = z'$, using $z, z' > 0$.
>
> *Continuous with continuous inverse:* $\varphi$ is the restriction of the projection $\mathbb{R}^3 \to \mathbb{R}^2$, hence continuous. The inverse $\varphi^{-1} : D \to U$, $(x, y) \mapsto (x, y, \sqrt{1 - x^2 - y^2})$, is continuous as a map into $\mathbb{R}^3$ (each component is continuous on $D$), hence continuous into the subspace $U$.
>
> Since $D$ is open in $\mathbb{R}^2$, [[§2 Topological Manifolds#^prop-2-3|Proposition §2.3]] shows $S^2$ is locally Euclidean of dimension $2$ at $p$.

^pf-ex-8-1

*Uses:* [[§2 Topological Manifolds#^prop-2-3|§2.3]], [[§1 Point-Set Topology Review#^prop-1-6|§1.6]], [[§1 Point-Set Topology Review#^prop-1-5|§1.5]] (4), [[§10 Continuous Functions#^thm-10-4|590 §10.4]], [[§22 Countability Axioms#^thm-22-3|590 §22.3]]

![[m591-2-1.svg]]
*The hemisphere chart: projection $(x,y,z) \mapsto (x,y)$ carries the open northern hemisphere $U = \{z > 0\}$ homeomorphically onto the open unit disk in $\mathbb{R}^2$.*

> [!theorem] Proposition §8.1: Spheres Are Topological Manifolds
> $S^n = \{x \in \mathbb{R}^{n+1} \mid |x| = 1\}$ is a topological $n$-manifold.
>
> *Lee: Example 1.4*

^prop-8-1

> [!proof]+ Proof
> As in [[§8 Spheres#^ex-8-1|Example §8.1]], $S^n$ is a metric space (restriction of the Euclidean metric), hence Hausdorff, and second countable: intersecting a countable basis of $\mathbb{R}^{n+1}$ with $S^n$ gives a countable basis. The $2(n+1)$ open hemispheres $U_i^{\pm} = \{x \in S^n \mid \pm x_i > 0\}$ cover $S^n$, since every point has a nonzero coordinate. On $U_i^\pm$, the map $\varphi_i^\pm$ forgetting the $i$-th coordinate is continuous and lands in the open unit ball $B^n$, because the remaining coordinates satisfy $\sum_{j \ne i} x_j^2 = 1 - x_i^2 < 1$. Its inverse inserts $\pm\sqrt{1 - |y|^2}$ in slot $i$ and is continuous. So each $\varphi_i^\pm$ is a homeomorphism onto the open set $B^n \subseteq \mathbb{R}^n$, and [[§2 Topological Manifolds#^prop-2-3|Proposition §2.3]] applies.

^pf-8-1

*Uses:* [[§8 Spheres#^ex-8-1|Ex. §8.1]], [[§2 Topological Manifolds#^def-2-2|Def. §2.2]], [[§2 Topological Manifolds#^prop-2-3|§2.3]], [[§1 Point-Set Topology Review#^prop-1-6|§1.6]], [[§22 Countability Axioms#^thm-22-3|590 §22.3]]

> [!remark]- Connections
> - The hemisphere charts as an atlas: [[§17 Differentiable Structures#^def-17-6|Def. §17.6]]; the circle case with its smooth atlases is [[§17 Differentiable Structures#^ex-17-2|Ex. §17.2]].

> [!remark] Remark
> This is the argument of [[§8 Spheres#^ex-8-1|Example §8.1]], for every $n$ (Lee, Example 1.4). The hemisphere charts will be our first example of an *atlas*, and the maps between overlapping charts ([[§2 Topological Manifolds#Charts and Transition Functions|§2, Charts and Transition Functions]]) will turn out to be smooth.

^rem-8-1

> [!example] Example §8.2: Two Hemisphere Charts on $S^2$
> Take $U = \{z > 0\}$ with $\varphi(x, y, z) = (x, y)$ and $V = \{x > 0\}$ with $\psi(x, y, z) = (y, z)$, both charts onto the open unit disk. Then $U \cap V = \{x > 0, z > 0\}$, $\varphi(U \cap V) = \{(x, y) \in D \mid x > 0\}$, and
>
> $$
> \psi \circ \varphi^{-1}(x, y) = \psi\big(x, y, \sqrt{1 - x^2 - y^2}\big) = \big(y, \sqrt{1 - x^2 - y^2}\big).
> $$
>
> Note that this map is not merely continuous but $C^\infty$ on its (open) domain, since $1 - x^2 - y^2 > 0$ there. This is no accident, and it is the point of Definition [[§17 Differentiable Structures#^def-17-4|§17.4]].

^ex-8-2

*Uses:* [[§8 Spheres#^ex-8-1|Ex. §8.1]], [[§2 Topological Manifolds#^def-2-4|Def. §2.4]]