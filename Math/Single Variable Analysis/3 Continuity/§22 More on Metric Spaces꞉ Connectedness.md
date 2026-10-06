---
type: section
subject: "[[Single Variable Analysis]]"
section: 22
chapter: 3
tags: [real-analysis, math451]
---
← [[§21 More on Metric Spaces꞉ Continuity]] · ↑ [[· 3 Continuity]] · [[§23 Power Series]] →

Given a subset $S \subseteq \mathbb{R}$, when should we consider it *connected*? Intervals — $(a,b)$, $[a,b]$, $(a,b]$, $[a,b)$ — should count: they are like unbroken strings, and we can travel from any point to any other continuously. How about $\mathbb{Q}$? Probably not: we cannot move continuously from one rational to another without leaving $\mathbb{Q}$. There are several ways to make this precise; here is one.

> [!definition] Definition §22.1: Path-Connected
> A metric space $(X,d)$ is called **path-connected** if for every two points $x, y \in X$ there exists a continuous map
>
> $$
> f: [0,1] \to X \qquad \text{with} \qquad f(0) = x, \quad f(1) = y
> $$
>
> — a continuous, unbroken path from $x$ to $y$.

^def-22-1

> [!remark]- Connections
> - Path-connectedness for topological spaces, [[§14 Connected Subspaces of ℝ#^def-14-3|590 Def. §14.3]], which implies connectedness, [[§14 Connected Subspaces of ℝ#^thm-14-4|590 Thm. §14.4]].

> [!theorem] Proposition §22.1: The Rationals Are Not Path-Connected
> $\mathbb{Q}$ (with the metric from $\mathbb{R}$) is not path-connected. In fact, every continuous map $f: [0,1] \to \mathbb{Q}$ is constant.

^prop-22-1

> [!proof]+ Proof
> View $f$ as a continuous map $[0,1] \to \mathbb{R}$ whose image happens to lie in $\mathbb{Q}$. By [[§18 Properties of Continuous Functions#^cor-18-5|Corollary §18.5]], $f([0,1])$ is a closed bounded interval. But which closed intervals are contained in $\mathbb{Q}$? Only the degenerate ones $[c,c] = \{c\}$: any interval with more than one point contains irrationals ([[§17 Continuous Functions#^rem-17-4|density of the irrationals, §17]]). So $f$ is constant — and no path can join two *distinct* rational numbers.

^pf-22-1

*Uses:* [[§18 Properties of Continuous Functions#^cor-18-5|§18.5]], [[§17 Continuous Functions#^rem-17-4|§17 Rem. (density of the irrationals)]]

> [!remark] Remark: Connectedness
> Path-connectedness is one way to make the idea precise. The other standard one is connectedness: no separation into two disjoint nonempty open subsets, [[§13 Connected Spaces#^def-13-1|590 Def. §13.1]]. Path-connected spaces are connected, [[§14 Connected Subspaces of ℝ#^thm-14-4|590 Thm. §14.4]], and the intervals of $\mathbb{R}$ are connected, [[§14 Connected Subspaces of ℝ#^cor-14-2|590 Cor. §14.2]]. A continuous image of a connected space is connected, [[Continuous Image of a Connected Space is Connected|590 Thm. §13.3]], which gives the [[Intermediate Value Theorem]] in its general form, [[§14 Connected Subspaces of ℝ#^thm-14-3|590 Thm. §14.3]]. In this course the corresponding facts on $[a,b]$ are the IVT itself and [[§18 Properties of Continuous Functions#^cor-18-5|Corollary §18.5]] (the image of $[a,b]$ is a closed interval), which is what the proof above uses.

^rem-22-1
