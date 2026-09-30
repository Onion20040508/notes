---
subject: "[[Single Variable Analysis]]"
section: 22
chapter: 3
tags: [real-analysis, math451]
---
← [[§21 More on Metric Spaces꞉ Continuity]] · ↑ [[3 Continuity]] · [[§23 Power Series]] →

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

> [!theorem] Proposition §22.1: The Rationals Are Not Path-Connected
> $\mathbb{Q}$ (with the metric from $\mathbb{R}$) is not path-connected. In fact, every continuous map $f: [0,1] \to \mathbb{Q}$ is constant.

^prop-22-1

> [!proof]+ Proof
> View $f$ as a continuous map $[0,1] \to \mathbb{R}$ whose image happens to lie in $\mathbb{Q}$. By the corollary of §18, $f([0,1])$ is a closed bounded interval. But which closed intervals are contained in $\mathbb{Q}$? Only the degenerate ones $[c,c] = \{c\}$: any interval with more than one point contains irrationals (density, §17). So $f$ is constant — and no path can join two *distinct* rational numbers.

^pf-22-1
