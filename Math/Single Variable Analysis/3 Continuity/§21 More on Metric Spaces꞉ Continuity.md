---
subject: "[[Single Variable Analysis]]"
section: 21
chapter: 3
tags: [real-analysis, math451]
---
← [[§20 Limits of Functions]] · ↑ [[3 Continuity]] · [[§22 More on Metric Spaces꞉ Connectedness]] →

The next two sections generalize what we have learned to metric spaces. (They are important, but discussing them in full would take many lectures; the lecture touched only the key definitions and one theorem.)

> [!definition] Definition §21.1: Continuous Maps Between Metric Spaces
> Let $(X, d_X)$ and $(Y, d_Y)$ be metric spaces. A map $f: X \to Y$ is **continuous at $x_0 \in X$** if for every $\varepsilon > 0$ there exists $\delta > 0$ such that for every $x \in X$,
>
> $$
> d_X(x, x_0) < \delta \quad \Longrightarrow \quad d_Y\bigl(f(x), f(x_0)\bigr) < \varepsilon.
> $$

^def-21-1

Taking $X = \mathbb{R}$ (or $\Omega \subseteq \mathbb{R}$) and $Y = \mathbb{R}$ with $d(x,y) = |x-y|$ recovers the earlier notion — the metric-space version is a simple generalization, with each absolute value replaced by the appropriate distance.
