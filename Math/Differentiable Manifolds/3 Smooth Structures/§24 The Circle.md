---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 3
section: 24
tags: [differentiable-manifolds, math591]
---
← [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds]] · ↑ [[· 3 Smooth Structures]] · [[§25 The Geometric Tangent Space]] →

*Thread: examples — The circle in one place: its external, graph and internal descriptions, and the one smooth structure defined by its three atlases.*

The circle through the course: the circle group $\mathrm{U}(1)$ in [[§11 Topological Groups and Classical Matrix Groups#^ex-11-3|U(1) is the circle]]; the homogeneous space $\mathbb{R}/\mathbb{Z}$ in [[§15 The Topology of G∕H and Real Grassmannians#^ex-15-1|the circle as R/Z]]; three atlases — four charts, stereographic and angle — in [[§17 Differentiable Structures#^ex-17-2|the four-chart atlas]], [[§17 Differentiable Structures#^ex-17-3|the stereographic atlas]] and [[§17 Differentiable Structures#^ex-17-4|the angle atlas]], with [[§17 Differentiable Structures#^rem-17-9|three atlases and one structure]]; $\mathbb{RP}^1$ homeomorphic to it in [[§18 Projective Spaces as Smooth Manifolds#^prop-18-6|The Two Topologies on RPⁿ Agree]]; its external, graph and internal descriptions, and the one smooth structure of its three atlases, in *this section*; and covered by a line, a local diffeomorphism that is not injective, in [[§33 Local Diffeomorphisms#^ex-33-1|the circle covered by a line]].

> [!example] Example §24.1: The Circle in Three Descriptions
> Near the point $p = (0,1)$ of $S^1 \subseteq \mathbb{R}^2$ (here $n = k = 1$):
> - **External:** $F(x,y) = x^2 + y^2 - 1$, with $\nabla F = (2x, 2y) \neq 0$ on $S^1$, so $0$ is a regular value and $S^1 = F^{-1}(0)$.
> - **Graph:** on $(-1,1) \times (0,\infty)$, $S^1$ is the graph of $h(x) = \sqrt{1-x^2}$ — which is the chart $\varphi_2$ of [[§17 Differentiable Structures#^ex-17-2|Ex. §17.2]], read backwards.
> - **Internal:** $\alpha(\theta) = (\cos\theta, \sin\theta)$ on $\theta \in (0,\pi)$, with $\alpha'(\theta) = (-\sin\theta, \cos\theta) \neq 0$ — the angle chart of [[§17 Differentiable Structures#^ex-17-4|Ex. §17.4]], read backwards.
>
> The three are related exactly as in the proof of [[§20 Manifolds in Euclidean Space#^thm-20-1|Theorem §20.1]]: $h$ comes from $F$ by the implicit function theorem, and $\alpha$ comes from $h$ by $x \mapsto (x, h(x))$ followed by the reparametrization $x = \cos\theta$.

^ex-24-1

*Uses:* [[§20 Manifolds in Euclidean Space#^def-20-1|Def. §20.1]], [[§7 The Regular Value Theorem#^def-7-4|Def. §7.4]], [[§7 The Regular Value Theorem#^thm-7-1|§7.1]], [[§17 Differentiable Structures#^ex-17-2|Ex. §17.2]], [[§17 Differentiable Structures#^ex-17-4|Ex. §17.4]]

![[m591-9-1.svg]]
*The circle described externally, as the zero set of $F = x^2 + y^2 - 1$ with nonvanishing gradient, and internally, as the image of $\alpha(\theta) = (\cos\theta, \sin\theta)$ on $(0,\pi)$.*

> [!remark]- Connections
> - The same circle in 452: [[Unit circle and unit sphere]], solved for $y$ near $(0,1)$ by the implicit function theorem in [[§15 The Implicit Function Theorem#^ex-15-1|452 Ex. §15.1]].

> [!theorem] Proposition §24.1: The Three Circle Atlases Define One Smooth Structure
> The four-chart atlas ([[§17 Differentiable Structures#^ex-17-2|Ex. §17.2]]), the angle atlas ([[§17 Differentiable Structures#^ex-17-4|Ex. §17.4]]) and the stereographic atlas ([[§17 Differentiable Structures#^ex-17-3|Ex. §17.3]]) on $S^1$ are pairwise compatible. All three generate the smooth structure that Proposition [[§20 Manifolds in Euclidean Space#^prop-20-2|§20.2]] gives $S^1 = F^{-1}(1)$, $F(x,y) = x^2 + y^2$.

^prop-24-1

> [!proof]+ Proof
> For $S^1$ the graph charts of Proposition [[§20 Manifolds in Euclidean Space#^prop-20-2|§20.2]] are the four projection charts, so that atlas $\mathcal{A}$ is the four-chart atlas. It suffices to show that every chart $(V, \chi)$ of the other two atlases is compatible with every chart $(U, \varphi)$ of $\mathcal{A}$. All such charts then lie in the maximal atlas $\overline{\mathcal{A}}$ (Theorem [[§17 Differentiable Structures#^thm-17-5|§17.5]]), and any two charts of an atlas are compatible — which is how Proposition [[§17 Differentiable Structures#^prop-17-2|§17.2]] is circumvented.
>
> Each such $\chi$ has two properties.
> - (a) $\chi^{-1}$ is smooth as a map into $\mathbb{R}^2$: it is $\theta \mapsto (\cos\theta, \sin\theta)$ for the angle charts, $u \mapsto \big(2u,\, u^2 - 1\big)/(u^2+1)$ for $\sigma_N$, and similarly for $\sigma_S$.
> - (b) $\chi$ is the restriction to $V$ of a smooth function $\hat\chi$ on an open subset of $\mathbb{R}^2$ containing $V$. For $\sigma_N = x/(1-y)$ take $\{y < 1\}$, and for $\sigma_S = x/(1+y)$ take $\{y > -1\}$. For an angle chart take a smooth branch of the argument on the plane minus a closed ray: for values in $(-\pi, \pi)$, $\theta = 2\arctan\big(y/(x + \sqrt{x^2+y^2})\big)$, and other ranges follow by rotating and adding a constant.
>
> On the overlap, $\varphi \circ \chi^{-1} = \pi \circ \chi^{-1}$ with $\pi$ a linear projection, which is smooth by (a). And $\chi \circ \varphi^{-1} = \hat\chi \circ \varphi^{-1}$ is smooth by (b), $\varphi^{-1}$ being a smooth parametrization.

^pf-24-1

*Uses:* [[§20 Manifolds in Euclidean Space#^prop-20-2|§20.2]], [[§20 Manifolds in Euclidean Space#^lem-20-3|§20.3]], [[§17 Differentiable Structures#^ex-17-2|Ex. §17.2]], [[§17 Differentiable Structures#^ex-17-3|Ex. §17.3]], [[§17 Differentiable Structures#^ex-17-4|Ex. §17.4]], [[§17 Differentiable Structures#^def-17-4|Def. §17.4]], [[§17 Differentiable Structures#^thm-17-5|§17.5]], [[§17 Differentiable Structures#^prop-17-2|§17.2]], [[Multivariable Chain Rule|452 §12.2]]
