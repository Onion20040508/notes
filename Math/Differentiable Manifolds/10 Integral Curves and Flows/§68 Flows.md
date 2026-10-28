---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 10
section: 68
tags: [differentiable-manifolds, math591]
---
← [[§67 Integral Curves]] · ↑ [[· 10 Integral Curves and Flows]]

*Stage: dynamics — All integral curves at once: the maximal curves through every point assemble into one smooth map on an open domain in $\mathbb{R} \times M$.*

*Lecture 23, the last minutes: “Let me tell you the bigger picture of what actually is happening, and then we'll see how much of that we get to prove … We'll prove a big chunk of this on Friday.”*

> [!theorem] Theorem §68.1: Maximal Integral Curves and the Flow
> Let $M$ be a smooth manifold and $\mathbf{X} \in \mathfrak{X}(M)$.
>
> 1. For every $p \in M$ there is a unique *maximal* integral curve of $\mathbf{X}$ starting at $p$, maximal with respect to its domain. Write it $\varphi_p$ and its domain $(\alpha(p), \beta(p))$, where $\alpha(p) \in [-\infty, 0)$ and $\beta(p) \in (0, +\infty]$: “$\alpha$ or $\beta$ may be $\pm\infty$.”
> 2. Let
>
> $$
> \mathcal{D} = \bigcup_{p \in M} \big(\alpha(p), \beta(p)\big) \times \{p\} \ \subseteq\ \mathbb{R} \times M, \qquad \varphi : \mathcal{D} \longrightarrow M, \quad (t, p) \longmapsto \varphi_p(t).
> $$
>
> Then $\mathcal{D}$ is open in $\mathbb{R} \times M$, and $\varphi$ is smooth.
>
> *Lee: Theorem 9.12*

^thm-68-1

> [!proof]+ Proof (to be filled)
> To be proved in Lecture 24. Uribe's indication for (1): “by uniqueness and something called the translation lemma, which is very easy to see,” there is “only one way to continue the curve forwards in time and then backwards in time until either you never stop or you run into the edge of the manifold.” Openness of $\mathcal{D}$ “is surprisingly long to prove.”

^pf-68-1

$\varphi$ is “just flowing, like we were doing before”, except that the domain of the time variable depends on the point, as in Example [[§67 Integral Curves#^ex-67-2|§67.2]]. The theorem is the local picture of Theorem [[§67 Integral Curves#^thm-67-3|§67.3]], with its rectangles $(-\varepsilon, \varepsilon) \times U$, put together on the whole manifold. In the two examples:
- Rotation (Example [[§67 Integral Curves#^ex-67-1|§67.1]]): $\alpha \equiv -\infty$, $\beta \equiv +\infty$, $\mathcal{D} = \mathbb{R} \times \mathbb{R}^2$.
- Escape (Example [[§67 Integral Curves#^ex-67-2|§67.2]]): $\alpha \equiv -\infty$, $\beta(x, y) = 1/(xy)$, so $\mathcal{D} = \{ (t, (x, y)) : x, y > 0,\ t\,xy < 1 \}$, open, and $\varphi(t, (x, y)) = \big(x/(1 - xyt),\ y\big)$, smooth on $\mathcal{D}$.

![[m591-68-1.svg]]

*(Not from lecture; figure added.)* The flow domain of Example [[§67 Integral Curves#^ex-67-2|§67.2]], sliced at $y_0 = 1$. Over each initial point $p = (x_0, 1)$ the domain is the vertical half-line $t < 1/x_0$, open at the top. These segments fill the region below the hyperbola $t = 1/x_0$, which is open.
