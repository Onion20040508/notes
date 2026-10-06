---
type: section
subject: "[[Single Variable Analysis]]"
section: 21
chapter: 3
tags: [real-analysis, math451]
---
← [[§20 Limits of Functions]] · ↑ [[· 3 Continuity]] · [[§22 More on Metric Spaces꞉ Connectedness]] →

The next two sections generalize what we have learned to metric spaces. (They are important, but discussing them in full would take many lectures; the lecture touched only the key definitions and one theorem.)

> [!definition] Definition §21.1: Continuous Maps Between Metric Spaces
> Let $(X, d_X)$ and $(Y, d_Y)$ be [[§13 Some Topological Concepts in Metric Spaces#^def-13-1|metric spaces]]. A map $f: X \to Y$ is **continuous at $x_0 \in X$** if for every $\varepsilon > 0$ there exists $\delta > 0$ such that for every $x \in X$,
>
> $$
> d_X(x, x_0) < \delta \quad \Longrightarrow \quad d_Y\bigl(f(x), f(x_0)\bigr) < \varepsilon.
> $$

^def-21-1

Taking $X = \mathbb{R}$ (or $\Omega \subseteq \mathbb{R}$) and $Y = \mathbb{R}$ with $d(x,y) = |x-y|$ recovers the earlier notion — the metric-space version is a simple generalization, with each absolute value replaced by the appropriate distance.

> [!remark]- Connections
> - The case X = ℝ², Y = ℝ with Euclidean distance is 452's continuity, [[§3 Continuity and Limits of Functions#^def-3-1|452 Def. §3.1]].
> - Continuity between topological spaces (preimages of open sets are open), [[§10 Continuous Functions#^def-10-1|590 Def. §10.1]], agrees with this for metric spaces by [[§12 Metric Topology#^thm-12-7|590 Thm. §12.7]].
> - The case X = Y = ℂ with d(z, w) = |z − w|: [[§18 Continuity#^def-18-1|342 Def. §18.1]] (continuity of complex functions, with worked examples).

> [!remark] Remark: Where the Metric-Space Theory Continues
> The theorems that make this definition useful are proved in Topology for metric (and general topological) spaces:
> - $\varepsilon$–$\delta$ continuity is equivalent to the open-set definition, [[§12 Metric Topology#^thm-12-7|590 Thm. §12.7]], and to sequential continuity, [[§12 Metric Topology#^thm-12-9|590 Thm. §12.9]]; the case of $\mathbb{R}$ is [[§17 Continuous Functions#^thm-17-1|Theorem §17.1]].
> - A continuous image of a compact space is compact, [[Continuous Image of a Compact Space is Compact|590 Thm. §18.3]]: the abstract form of the [[Extreme Value Theorem]].
> - A continuous function on a compact metric space is uniformly continuous ([[§18 Compact Spaces#^rem-18-1|590 §18, Remark: Why Compactness Matters]], stated there); the case of $[a,b]$ is [[§19 Uniform Continuity#^thm-19-1|Theorem §19.1]].

^rem-21-1
