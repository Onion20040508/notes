---
type: section
subject: "[[Multivariable Analysis]]"
chapter: 1
section: 2
tags: [multivariable-analysis, math452]
---
← [[Multivariable Analysis §1 Sequences and Limits in ℝⁿ]] · ↑ [[Multivariable Analysis — 1 Foundations]] · [[Multivariable Analysis §3 Continuity and Limits of Functions]] →

> [!definition] Definition §2.1: Open Ball
> The **open ball** (spherical neighborhood) centered at $x \in \mathbb{R}^n$ with radius $r > 0$ is
>
> $$
> B(x, r) := \{y \in \mathbb{R}^n : |y - x| < r\}.
> $$
>
> Alternative notations: $B_r(x)$ or simply $B_n$ when the center is understood.

^def-2-1

> [!definition] Definition §2.2: Square Neighborhood
> A **square neighborhood** centered at $(x_0, y_0) \in \mathbb{R}^2$ with side length $2\delta$ is
>
> $$
> \{(x, y) \in \mathbb{R}^2 : |x - x_0| < \delta \text{ and } |y - y_0| < \delta\}.
> $$

^def-2-2

> [!remark] Remark
> Open balls and square neighborhoods are topologically equivalent for most purposes.

^rem-2-1

> [!remark]- Connections
> - Square neighborhoods are the balls of the [[Topology §11 Metric Topology#^ex-11-2|square metric]]; the precise form of this remark is [[Topology §11 Metric Topology#^thm-11-2|Euclidean and Square Metrics Induce Same Topology]] (MATH 590), resting on the inequality of [[Single Variable Analysis §13 Some Topological Concepts in Metric Spaces#^prop-13-1|Equivalence of the Two Distances]] (MATH 451).

> [!definition] Definition §2.3: Interior, Exterior, and Boundary Points
> Let $E \subseteq \mathbb{R}^n$ and $x \in \mathbb{R}^n$.
> - $x$ is an **interior point** of $E$ if $\exists\, \varepsilon > 0$ such that $B(x, \varepsilon) \subseteq E$.
> - $x$ is an **exterior point** of $E$ if $\exists\, \varepsilon > 0$ such that $B(x, \varepsilon) \subseteq E^c$.
> - $x$ is a **boundary point** of $E$ if for all $\varepsilon > 0$: $B(x, \varepsilon) \cap E \neq \emptyset$ and $B(x, \varepsilon) \cap E^c \neq \emptyset$.

^def-2-3

![[m452-2-1.svg]]
*An interior point has a ball entirely inside $E$; an exterior point has a ball entirely outside; a boundary point's every ball meets both $E$ and $E^c$.*

> [!example] Example §2.1
> For $E = [0, 1)$, the points $0$ and $1$ are both boundary points.

^ex-2-1

> [!definition] Definition §2.4: Open and Closed Sets
> Let $E \subseteq \mathbb{R}^n$.
> - $E$ is **open** if every point of $E$ is an interior point.
> - $E$ is **closed** if $E$ contains all its boundary points.

^def-2-4

> [!remark]- Connections
> - MATH 451 metric-space version: [[Single Variable Analysis §13 Some Topological Concepts in Metric Spaces#^def-13-5|Open and Closed Subsets]].
> - MATH 590: the open sets of the [[Topology §11 Metric Topology#^def-11-3|metric topology]] with [[Topology §11 Metric Topology#^def-11-2|ε-balls]]; a [[Topology §6 Closed Sets and Limit Points#^def-6-1|closed set]] is the complement of an open set.

> [!remark] Notation
> $\partial E$ denotes the set of boundary points of $E$.

^rem-2-2

> [!definition] Definition §2.5: Closure
> The **closure** of $E$ is $\overline{E} := E \cup \partial E$, the smallest closed set containing $E$.

^def-2-5

> [!remark]- Connections
> - MATH 451: [[Single Variable Analysis §13 Some Topological Concepts in Metric Spaces#^def-13-6|Closure]] in a metric space.
> - MATH 590: [[Topology §7 Interior and Closure#^def-7-1|Interior and Closure]] in any topological space, and the [[Closure Characterization]] (every neighborhood meets $E$, as in the boundary-point condition above).
