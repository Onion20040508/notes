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

*Uses:* [[§20 Manifolds in Euclidean Space#^def-20-1|Def. §20.1]], [[§20 Manifolds in Euclidean Space#^def-20-2|Def. §20.2]], [[§7 The Regular Value Theorem#^def-7-4|Def. §7.4]], [[§7 The Regular Value Theorem#^thm-7-1|§7.1]], [[§17 Differentiable Structures#^ex-17-2|Ex. §17.2]], [[§17 Differentiable Structures#^ex-17-4|Ex. §17.4]]

![[m591-9-1.svg]]
*The circle described externally, as the zero set of $F = x^2 + y^2 - 1$ with nonvanishing gradient, and internally, as the image of $\alpha(\theta) = (\cos\theta, \sin\theta)$ on $(0,\pi)$.*

> [!remark]- Connections
> - The same circle in 452: [[Unit circle and unit sphere]], solved for $y$ near $(0,1)$ by the implicit function theorem in [[§15 The Implicit Function Theorem#^ex-15-1|452 Ex. §15.1]].

> [!theorem] Proposition §24.1: The Three Circle Atlases Define One Smooth Structure
> The four-chart atlas ([[§17 Differentiable Structures#^ex-17-2|Ex. §17.2]]), the angle atlas ([[§17 Differentiable Structures#^ex-17-4|Ex. §17.4]]) and the stereographic atlas ([[§17 Differentiable Structures#^ex-17-3|Ex. §17.3]]) on $S^1$ are pairwise compatible. All three generate the smooth structure that Proposition [[§20 Manifolds in Euclidean Space#^prop-20-2|§20.2]] gives $S^1 = F^{-1}(1)$, $F(x,y) = x^2 + y^2$.

^prop-24-1

> [!proof]+ Proof
> *The graph charts are the four projection charts.* Here $F(x,y) = x^2 + y^2$, $c = 1$, $n = k = 1$, and $F'(x,y) = (2x \ \ 2y)$. At a point of $S^1$ with $y \neq 0$ the column $\partial F/\partial y = 2y$ is nonzero, and one solves for $y$ in terms of $x$; at a point with $x \neq 0$, for $x$ in terms of $y$. What the construction before Proposition [[§20 Manifolds in Euclidean Space#^prop-20-2|§20.2]] needs of the box is that the equation be equivalent to the graph of a smooth function there, and the boxes may be taken as large as that allows: on $(-1,1) \times (0,\infty)$,
>
> $$
> x^2 + y^2 = 1 \iff y = \sqrt{1 - x^2}
> $$
>
> (the positive root, as $y > 0$), with $\sqrt{1-x^2}$ smooth because $1 - x^2 > 0$; likewise $y = -\sqrt{1-x^2}$ on $(-1,1) \times (-\infty,0)$, and $x = \pm\sqrt{1-y^2}$ on $(0,\infty) \times (-1,1)$ and $(-\infty,0) \times (-1,1)$. The corresponding graph charts are the projections $(x,y) \mapsto x$ on the upper and lower half-circles and $(x,y) \mapsto y$ on the right and left ones, i.e. $\varphi_2, \varphi_4, \varphi_1, \varphi_3$ of Example [[§17 Differentiable Structures#^ex-17-2|§17.2]]; every point of $S^1$ has $x \neq 0$ or $y \neq 0$, so they cover. So for $S^1$ the graph charts of Proposition [[§20 Manifolds in Euclidean Space#^prop-20-2|§20.2]] are the four projection charts, so that atlas $\mathcal{A}$ is the four-chart atlas, and the smooth structure in question is the maximal atlas $\overline{\mathcal{A}}$ it generates (Theorem [[§17 Differentiable Structures#^thm-17-5|§17.5]]).
>
> *What has to be shown.* It suffices to show that every chart $(V, \chi)$ of the other two atlases is compatible with every chart $(U, \varphi)$ of $\mathcal{A}$. All such charts then lie in the maximal atlas $\overline{\mathcal{A}}$ (Theorem [[§17 Differentiable Structures#^thm-17-5|§17.5]], which describes $\overline{\mathcal{A}}$ as exactly the charts compatible with every chart of $\mathcal{A}$), and any two charts of an atlas are compatible — which is how Proposition [[§17 Differentiable Structures#^prop-17-2|§17.2]] is circumvented. Both claims then follow. *Pairwise compatible:* a chart of one of the three atlases and a chart of another both belong to the atlas $\overline{\mathcal{A}}$, hence are compatible (Definition [[§17 Differentiable Structures#^def-17-6|§17.6]]); so any two of the three atlases are compatible (Definition [[§17 Differentiable Structures#^def-17-7|§17.7]]). *One structure:* each of the three atlases $\mathcal{B}$ is contained in $\overline{\mathcal{A}}$, which is a maximal atlas; by the uniqueness in Theorem [[§17 Differentiable Structures#^thm-17-5|§17.5]], $\overline{\mathcal{A}}$ is the maximal atlas containing $\mathcal{B}$, i.e. the structure $\mathcal{B}$ generates (Definition [[§17 Differentiable Structures#^def-17-9|§17.9]]).
>
> The charts $(V, \chi)$ to be checked are $\sigma_N$ on $S^1 \setminus \{N\}$ and $\sigma_S$ on $S^1 \setminus \{S\}$ (Example [[§17 Differentiable Structures#^ex-17-3|§17.3]]), and $\varphi_a$ on $U_a = S^1 \setminus \{(1,0)\}$ and $\varphi_b$ on $U_b = S^1 \setminus \{(-1,0)\}$ (Example [[§17 Differentiable Structures#^ex-17-4|§17.4]]). Each such $\chi$ has two properties.
> - [(a)] $\chi^{-1}$ is smooth as a map into $\mathbb{R}^2$: it is $\theta \mapsto (\cos\theta, \sin\theta)$ for the angle charts, $u \mapsto \big(2u,\, u^2 - 1\big)/(u^2+1)$ for $\sigma_N$, and similarly for $\sigma_S$. Explicitly, $\sigma_S(x,y) = \sigma_N(x,-y)$, so $\sigma_S^{-1}$ is $\sigma_N^{-1}$ followed by the reflection $(x,y) \mapsto (x,-y)$:
>
> $$
> \sigma_S^{-1}(u) = \Big( \frac{2u}{u^2+1},\, \frac{1-u^2}{u^2+1} \Big);
> $$
>
>     one checks that this point lies on $S^1$, as $(2u)^2 + (1-u^2)^2 = (1+u^2)^2$, and that $\sigma_S$ of it is $\frac{2u/(u^2+1)}{1 + (1-u^2)/(u^2+1)} = \frac{2u/(u^2+1)}{2/(u^2+1)} = u$. The components of $\sigma_N^{-1}$ and $\sigma_S^{-1}$ are rational functions whose denominator $u^2 + 1 \ge 1$ never vanishes, and $\cos$, $\sin$ are smooth; so each $\chi^{-1}$ is smooth.
> - [(b)] $\chi$ is the restriction to $V$ of a smooth function $\hat\chi$ on an open subset of $\mathbb{R}^2$ containing $V$. For $\sigma_N = x/(1-y)$ take $\{y < 1\}$, and for $\sigma_S = x/(1+y)$ take $\{y > -1\}$. (On these open sets the denominators do not vanish, so the quotients are smooth; and they contain the domains, since on $S^1$ we have $y^2 \le x^2 + y^2 = 1$, with $y = 1$ only at $N$ and $y = -1$ only at $S$.) For an angle chart take a smooth branch of the argument on the plane minus a closed ray: for values in $(-\pi, \pi)$, $\theta = 2\arctan\big(y/(x + \sqrt{x^2+y^2})\big)$, and other ranges follow by rotating and adding a constant. In detail, let
>
> $$
> \Theta(x,y) = 2\arctan\frac{y}{x + \sqrt{x^2+y^2}} \qquad \text{on } \mathbb{R}^2 \setminus \{(x,0) \mid x \le 0\}.
> $$
>
>     It is smooth there: $\sqrt{x^2+y^2}$ is smooth away from the origin, and the denominator is positive — if $y \neq 0$ then $\sqrt{x^2+y^2} > |x| \ge -x$, and if $y = 0$ then $x > 0$ and the denominator is $2x$. At $(\cos\theta, \sin\theta)$ with $\theta \in (-\pi,\pi)$, the half-angle formulas $1 + \cos\theta = 2\cos^2(\theta/2)$ and $\sin\theta = 2\sin(\theta/2)\cos(\theta/2)$ give $y/(x + \sqrt{x^2+y^2}) = \sin\theta/(1 + \cos\theta) = \tan(\theta/2)$, and $\theta/2 \in (-\pi/2, \pi/2)$, the range of $\arctan$; so $\Theta(\cos\theta, \sin\theta) = \theta$. *For $\varphi_b$* (values in $(\pi, 3\pi)$): if $\theta \in (\pi,3\pi)$ then $\theta - 2\pi \in (-\pi,\pi)$ has the same cosine and sine, so $\varphi_b = \Theta + 2\pi$ on $U_b$; take $\hat\chi = \Theta + 2\pi$, smooth on $\mathbb{R}^2 \setminus \{(x,0) \mid x \le 0\}$, which contains $U_b$ because that ray meets $S^1$ only at $(-1,0)$. *For $\varphi_a$* (values in $(0, 2\pi)$): if $\theta \in (0,2\pi)$ then $(-\cos\theta, -\sin\theta) = (\cos(\theta-\pi), \sin(\theta-\pi))$ with $\theta - \pi \in (-\pi,\pi)$, so $\Theta(-x,-y) = \theta - \pi$; take $\hat\chi(x,y) = \Theta(-x,-y) + \pi$ (rotation by $\pi$, then the constant $\pi$), smooth on $\mathbb{R}^2 \setminus \{(x,0) \mid x \ge 0\}$, which contains $U_a$ because that ray meets $S^1$ only at $(1,0)$.
>
> *Compatibility.* Fix such a $(V, \chi)$ and a chart $(U, \varphi)$ of $\mathcal{A}$; if $U \cap V = \emptyset$ there is nothing to check (Definition [[§17 Differentiable Structures#^def-17-4|§17.4]]). Here $\varphi = \pi|_U$, where $\pi : \mathbb{R}^2 \to \mathbb{R}$ is the linear projection $(x,y) \mapsto x$ or $(x,y) \mapsto y$, and $\varphi^{-1}$ is one of $t \mapsto (t, \pm\sqrt{1-t^2})$, $t \mapsto (\pm\sqrt{1-t^2}, t)$ on $(-1,1)$ — a smooth parametrization (observation (1) in the proof of Proposition [[§20 Manifolds in Euclidean Space#^prop-20-2|§20.2]]), smooth because $1 - t^2 > 0$. We must show that the transition function $\varphi \circ \chi^{-1} : \chi(U \cap V) \to \varphi(U \cap V)$ is a diffeomorphism (Definition [[§17 Differentiable Structures#^def-17-3|§17.3]]). It is a bijection, being the composite of the bijections $\chi^{-1} : \chi(U \cap V) \to U \cap V$ and $\varphi : U \cap V \to \varphi(U \cap V)$, with inverse $\chi \circ \varphi^{-1}$; so it remains to see that both are smooth. On the overlap, $\varphi \circ \chi^{-1} = \pi \circ \chi^{-1}$ with $\pi$ a linear projection, which is smooth by (a): $\chi^{-1}$ takes values in $U \cap V$, where $\varphi = \pi$, and a composite of the smooth $\chi^{-1}$ with the linear $\pi$ is smooth. And $\chi \circ \varphi^{-1} = \hat\chi \circ \varphi^{-1}$ is smooth by (b), $\varphi^{-1}$ being a smooth parametrization: $\varphi^{-1}$ takes values in $U \cap V \subseteq V$, where $\hat\chi = \chi$, and these values lie in the open domain of $\hat\chi$, so $\hat\chi \circ \varphi^{-1}$ is a composite of smooth maps between open subsets of Euclidean spaces. Hence $(V, \chi)$ and $(U, \varphi)$ are compatible, which is what had to be shown.
^pf-24-1

*Uses:* [[§20 Manifolds in Euclidean Space#^prop-20-2|§20.2]], [[§20 Manifolds in Euclidean Space#^lem-20-3|§20.3]], [[§17 Differentiable Structures#^ex-17-2|Ex. §17.2]], [[§17 Differentiable Structures#^ex-17-3|Ex. §17.3]], [[§17 Differentiable Structures#^ex-17-4|Ex. §17.4]], [[§17 Differentiable Structures#^def-17-4|Def. §17.4]], [[§17 Differentiable Structures#^thm-17-5|§17.5]], [[§17 Differentiable Structures#^prop-17-2|§17.2]], [[Multivariable Chain Rule|452 §12.2]], [[§17 Differentiable Structures#^def-17-6|Def. §17.6]], [[§17 Differentiable Structures#^def-17-7|Def. §17.7]], [[§17 Differentiable Structures#^def-17-9|Def. §17.9]], [[§17 Differentiable Structures#^def-17-3|Def. §17.3]]
