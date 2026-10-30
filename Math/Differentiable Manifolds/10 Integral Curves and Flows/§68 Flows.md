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

> [!proof]+ Proof of (1) (Lecture 24); (2) to be filled
> Part (1) was proved in Lecture 24: Proposition [[§68 Flows#^prop-68-2|§68.2]], in [[§68 Flows#Maximal Domains and Completeness|Maximal Domains and Completeness]] below. Part (2) is to be proved. Uribe's indication for (1), in Lecture 23: “by uniqueness and something called the translation lemma, which is very easy to see,” there is “only one way to continue the curve forwards in time and then backwards in time until either you never stop or you run into the edge of the manifold.” Openness of $\mathcal{D}$ “is surprisingly long to prove.”

^pf-68-1

*Uses:* [[§68 Flows#^prop-68-2|§68.2]]

$\varphi$ is “just flowing, like we were doing before”, except that the domain of the time variable depends on the point, as in Example [[§67 Integral Curves#^ex-67-2|§67.2]]. The theorem is the local picture of Theorem [[§67 Integral Curves#^thm-67-3|§67.3]], with its rectangles $(-\varepsilon, \varepsilon) \times U$, put together on the whole manifold. In the two examples:
- Rotation (Example [[§67 Integral Curves#^ex-67-1|§67.1]]): $\alpha \equiv -\infty$, $\beta \equiv +\infty$, $\mathcal{D} = \mathbb{R} \times \mathbb{R}^2$.
- Escape (Example [[§67 Integral Curves#^ex-67-2|§67.2]]): $\alpha \equiv -\infty$, $\beta(x, y) = 1/(xy)$, so $\mathcal{D} = \{ (t, (x, y)) : x, y > 0,\ t\,xy < 1 \}$, open, and $\varphi(t, (x, y)) = \big(x/(1 - xyt),\ y\big)$, smooth on $\mathcal{D}$.

![[m591-68-1.svg]]

*(Not from lecture; figure added.)* The flow domain of Example [[§67 Integral Curves#^ex-67-2|§67.2]], sliced at $y_0 = 1$. Over each initial point $p = (x_0, 1)$ the domain is the vertical half-line $t < 1/x_0$, open at the top. These segments fill the region below the hyperbola $t = 1/x_0$, which is open.

## Maximal Domains and Completeness

*Lecture 24. “What this allows us to do” — uniqueness on the common domain, Proposition [[§67 Integral Curves#^prop-67-6|§67.6]] — “is to define the maximal domain of an integral curve, given an initial condition.”*

> [!definition] Definition §68.1: Maximal Domain
> Let $\mathbf{X} \in \mathfrak{X}(M)$ and $p \in M$. Define
>
> $$
> \big(\alpha(p), \beta(p)\big) = \bigcup_{I} I ,
> $$
>
> the union over the domains $I$ of all integral curves of $\mathbf{X}$ starting at $p$:
> an open interval containing $0$, possibly infinite or semi-infinite. It is the **maximal domain** of integral curves of $\mathbf{X}$ starting at $p$.
>
> *Lee: Theorem 9.12*

^def-68-1

The union is nonempty, since an integral curve starting at $p$ exists (Theorem [[§67 Integral Curves#^thm-67-4|§67.4]]). Each domain $I$ is an open interval containing $0$, “because it starts at $p$”, so the union is an open interval containing $0$. “So it's something that is very harmless to take.”

> [!theorem] Proposition §68.2: The Maximal Integral Curve
> Let $\mathbf{X} \in \mathfrak{X}(M)$ and $p \in M$. There is an integral curve $\varphi_p : (\alpha(p), \beta(p)) \to M$ of $\mathbf{X}$ starting at $p$, and every integral curve $c : I \to M$ starting at $p$ satisfies $I \subseteq (\alpha(p), \beta(p))$ and $c = \varphi_p|_I$. So $(\alpha(p), \beta(p))$ is the largest possible domain of such a curve, and $\varphi_p$ is the unique maximal integral curve starting at $p$. This proves Theorem [[§68 Flows#^thm-68-1|§68.1]](1).
>
> *Lee: Theorem 9.12*

^prop-68-2

> [!proof]+ Proof
> *(Lecture 24: “How do you define it? Well, I take a point $t$ here. It's in some $I$, so there is some integral curve defined in the neighbourhood of that. I define it by that, and it doesn't matter which $I$ I chose, by the previous lemma.” Details filled in.)* For $t \in (\alpha(p), \beta(p))$, choose an integral curve $c : I \to M$ starting at $p$ with $t \in I$, and set $\varphi_p(t) = c(t)$. *Well defined:* if $c' : I' \to M$ is another, then $c$ and $c'$ agree at time $0$, so by Proposition [[§67 Integral Curves#^prop-67-6|§67.6]] they agree on $I \cap I' \ni t$. *An integral curve:* near each $t$, $\varphi_p$ equals the smooth curve $c$ on the open interval $I \ni t$, so $\varphi_p$ is smooth and $\dot\varphi_p(t) = \dot c(t) = \mathbf{X}_{c(t)} = \mathbf{X}_{\varphi_p(t)}$, since velocity at $t$ only depends on the curve near $t$. And $\varphi_p(0) = p$. *Maximal:* if $c : I \to M$ starts at $p$, then $I$ is one of the domains in the union, so $I \subseteq (\alpha(p), \beta(p))$, and $c = \varphi_p|_I$ by the definition of $\varphi_p$.

^pf-68-2

*Uses:* [[§67 Integral Curves#^prop-67-6|§67.6]]

“The uniqueness is absolutely fantastic for the theory.” The maximal domains were computed in the examples: $(-\infty, 1/(x_0y_0))$ for Example [[§67 Integral Curves#^ex-67-2|§67.2]], $(-\infty, -x_0)$ for Example [[§67 Integral Curves#^ex-67-3|§67.3]], and $\mathbb{R}$ for the rotation and Euler fields.

![[m591-68-2.svg]]

*(Not from lecture; figure added.)* The maximal domains of Example [[§67 Integral Curves#^ex-67-3|§67.3]], assembled into the set $\mathcal{D} = \{ (t, x_0) : x_0 < 0,\ t < -x_0 \}$ of Theorem [[§68 Flows#^thm-68-1|§68.1]](2), an open set. Compare the flow domain of Example [[§67 Integral Curves#^ex-67-2|§67.2]] above: there $\beta(p) = 1/(x_0y_0)$ blows up as $x_0 \to 0$, here $\beta(x_0) = -x_0$ shrinks to $0$ at the end of $M$. Neither field is complete.

> [!definition] Definition §68.2: Complete Vector Field
> $\mathbf{X} \in \mathfrak{X}(M)$ is **complete** if $(\alpha(p), \beta(p)) = \mathbb{R}$ for every $p \in M$.
>
> *Lee: Ch. 9, Complete Vector Fields*

^def-68-2

“This is the case where there are no headaches … you can go forever, and backwards in time as well, forever.” (“The existential question is: the time domain of the universe — is it complete?”) The rotation field and the Euler field are complete; the fields of Examples [[§67 Integral Curves#^ex-67-2|§67.2]] and [[§67 Integral Curves#^ex-67-3|§67.3]] are not.

“When you're doing theory, you wonder: are there results that have the conclusion ‘this vector field is complete’? It's hard to tell in general.” “A very powerful-seeming little result”:

> [!theorem] Lemma §68.3: Uniform Time Lemma
> Let $\mathbf{X} \in \mathfrak{X}(M)$. If there is $\varepsilon > 0$ such that $(-\varepsilon, \varepsilon) \subseteq (\alpha(p), \beta(p))$ for every $p \in M$, then $\mathbf{X}$ is complete.
>
> *Lee: Lemma 9.15*

^lem-68-3

> [!proof]+ Proof (to be filled)
> To be proved in Lecture 25 (“I'll prove this on Monday”).

^pf-68-3

![[m591-68-3.svg]]

*(Figure after the board.)* “The horizontal line is $M$, and then you have $\mathbb{R}$ here”: over each $p$, the maximal domain $(\alpha(p), \beta(p))$, between the graphs $t = \beta(p) > 0$ and $t = \alpha(p) < 0$. The lemma's hypothesis is that a uniform strip $(-\varepsilon, \varepsilon) \times M$ fits inside; its conclusion is that the whole of $\mathbb{R} \times M$ does. (“I always reverse the cartoon axes. Someday I'll learn.”)

Announced for Monday, as consequences of Lemma [[§68 Flows#^lem-68-3|§68.3]]:
- every vector field on a compact manifold is complete: “compactness will assure that there is a uniform time” (Lee, Corollary 9.17);
- every left-invariant vector field on a Lie group is complete, “because you're going to be able to translate solutions” (Lee, Theorem 9.18).
