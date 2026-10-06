---
type: section
subject: "[[Multivariable Analysis]]"
chapter: 1
section: 2
tags: [multivariable-analysis, math452]
---
← [[§1 Sequences and Limits in ℝⁿ]] · ↑ [[· 1 Foundations]] · [[§3 Continuity and Limits of Functions]] →

> [!definition] Definition §2.1: Open Ball
> The **open ball** (spherical neighborhood) centered at $x \in \mathbb{R}^n$ with radius $r > 0$ is
>
> $$
> B(x, r) := \{y \in \mathbb{R}^n : |y - x| < r\}.
> $$
>
> Alternative notations: $B_r(x)$ or simply $B_n$ when the center is understood.

^def-2-1

> [!remark]- Connections
> - The ε-ball of a general metric: [[§11 Metric Topology#^def-11-2|590 Def. §11.2]].
> - Same definition in 551's review of the topology of ℝⁿ: [[§5 Topology of ℝⁿ#^def-5-1|551 Def. §5.1]].
> - Computational version: [[§12★ Regions in the Complex Plane#^def-12-1|342 Def. §12.1]] (ε neighborhoods and deleted neighborhoods in the complex plane, the case n = 2).

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

![[m452-2-2.svg]]
*Why balls and squares are interchangeable: the square neighborhood of side $2\delta$ (red) contains the ball $B((x_0,y_0),\delta)$ and is contained in the ball $B((x_0,y_0),\sqrt2\,\delta)$ (blue, dashed). So every ball contains a square and every square contains a ball around the same center, and "interior point", "open", "boundary point" come out the same with either kind of neighborhood.*

> [!remark]- Connections
> - Square neighborhoods are the balls of the [[§11 Metric Topology#^ex-11-2|square metric]]; the precise form of this remark is [[§11 Metric Topology#^thm-11-2|Euclidean and Square Metrics Induce Same Topology]] (MATH 590), resting on the inequality of [[§13 Some Topological Concepts in Metric Spaces#^prop-13-1|Equivalence of the Two Distances]] (MATH 451).

> [!definition] Definition §2.3: Interior Point
> Let $E \subseteq \mathbb{R}^n$ and $x \in \mathbb{R}^n$.
> - $x$ is an **interior point** of $E$ if $\exists\, \varepsilon > 0$ such that $B(x, \varepsilon) \subseteq E$.

^def-2-3

> [!definition] Definition §2.3: Exterior Point
> Let $E \subseteq \mathbb{R}^n$ and $x \in \mathbb{R}^n$.
> - $x$ is an **exterior point** of $E$ if $\exists\, \varepsilon > 0$ such that $B(x, \varepsilon) \subseteq E^c$.

^def-2-new1

> [!definition] Definition §2.3: Boundary Point
> Let $E \subseteq \mathbb{R}^n$ and $x \in \mathbb{R}^n$.
> - $x$ is a **boundary point** of $E$ if for all $\varepsilon > 0$: $B(x, \varepsilon) \cap E \neq \emptyset$ and $B(x, \varepsilon) \cap E^c \neq \emptyset$.

^def-2-new2

![[m452-2-1.svg]]
*The three cases of Definition [[§2 Open and Closed Sets#^def-2-3|§2.3]]–[[§2 Open and Closed Sets#^def-2-new2|§2.3]] (interior, exterior and boundary points), with the open balls $B(x,\varepsilon)$ dashed. An interior point has a ball entirely inside $E$ (green, filled); an exterior point has a ball entirely inside $E^c$ (green, empty); at a boundary point every ball, however small, meets both $E$ and $E^c$ (red).*

> [!remark]- Connections
> - Interior in a topological space, the largest open subset: [[§7 Interior and Closure#^def-7-1|590 Def. §7.1]].
> - Computational version: [[§12★ Regions in the Complex Plane#^def-12-2|342 Def. §12.2]] (interior, exterior and boundary points of a set in the complex plane, with worked examples).

> [!example] Example §2.1
> For $E = [0, 1)$, the points $0$ and $1$ are both boundary points.

^ex-2-1

> [!definition] Definition §2.4: Open Set
> Let $E \subseteq \mathbb{R}^n$.
> - $E$ is **open** if every point of $E$ is an interior point.

^def-2-4

> [!definition] Definition §2.4: Closed Set
> Let $E \subseteq \mathbb{R}^n$.
> - $E$ is **closed** if $E$ contains all its boundary points.

^def-2-new3

> [!remark]- Connections
> - MATH 451 metric-space version: [[§13 Some Topological Concepts in Metric Spaces#^def-13-5|Open and Closed Subsets]].
> - MATH 590: the open sets of the [[§11 Metric Topology#^def-11-3|metric topology]] with [[§11 Metric Topology#^def-11-2|ε-balls]]; a [[§6 Closed Sets and Limit Points#^def-6-1|closed set]] is the complement of an open set.
> - Computational version: [[§12★ Regions in the Complex Plane#^def-12-3|342 Def. §12.3]] (open and closed sets in the complex plane).

> [!remark] Notation
> $\partial E$ denotes the set of boundary points of $E$.

^rem-2-2

> [!definition] Definition §2.5: Closure
> The **closure** of $E$ is $\overline{E} := E \cup \partial E$, the smallest closed set containing $E$.

^def-2-5

> [!remark]- Connections
> - MATH 451: [[§13 Some Topological Concepts in Metric Spaces#^def-13-6|Closure]] in a metric space.
> - MATH 590: [[§7 Interior and Closure#^def-7-1|Interior and Closure]] in any topological space, and the [[Closure Characterization]] (every neighborhood meets $E$, as in the boundary-point condition above).
> - Computational version: [[§12★ Regions in the Complex Plane#^def-12-3|342 Def. §12.3]] (closure of a set in the complex plane).
