---
type: section
subject: "[[Functional Analysis]]"
chapter: 4
section: 11
tags: [functional-analysis, math556]
---
← [[§10 New Normed Spaces from Old]] · ↑ [[· 4 Infinite-Dimensional Spaces꞉ ℓᵖ, Lᵖ, and Compactness]] · [[§12 Hölder's Inequality for Sequences]] →

*Stage: norms — Tools. The inequalities that make $\|\cdot\|_p$ a norm: Young, then Hölder ([[§12 Hölder's Inequality for Sequences|§12]]), then Minkowski ([[§13 Minkowski's Inequality and the Spaces ℓᵖ|§13]]).*

> [!theorem] Proposition §11.1: Cauchy–Schwarz in $\mathbb{R}^n$
> For $x, y \in \mathbb{R}^n$, with $\|x\| = \bigl(x_1^2 + \cdots + x_n^2\bigr)^{1/2}$,
>
> $$
> |x \cdot y| \le \|x\|\, \|y\|.
> $$

^prop-11-1

> [!proof]+ Proof
> Recalled without proof in lecture; the standard argument is via the [[§11 Means and Young's Inequality#^lem-11-2|elementary inequality below]] or the discriminant of $t \mapsto \|x + ty\|^2$. See the [[Hölder's Inequality|MATH 551 notes]].

^pf-11-1

> [!remark]- Connections
> - Home of the inequality: [[Cauchy–Schwarz inequality|LADR 6.14]]; the $p = 2$ case of [[Hölder's Inequality|551 §19.5]].
> - Re-proved for every inner product space in [[§17 Cauchy–Schwarz and the Induced Norm#^thm-17-1|§17.1]]; for infinite sequences it is the case $p = q = 2$ of [[§12 Hölder's Inequality for Sequences#^thm-12-1|§12.1]].

> [!theorem] Lemma §11.2: Arithmetic–Geometric Mean, Two Variables
> For all real $a, b$, $2ab \le a^2 + b^2$; equivalently, for $a, b \ge 0$,
>
> $$
> \sqrt{ab} \le \tfrac{1}{2}(a + b).
> $$

^lem-11-2

> [!proof]+ Proof
> $0 \le (a - b)^2 = a^2 - 2ab + b^2$. For the second form, apply the first to $\sqrt{a}, \sqrt{b}$.

^pf-11-2

The second form says that the geometric mean of two non-negative numbers is at most their arithmetic mean. Young's inequality is the weighted version: give $a$ weight $1 - \theta$ and $b$ weight $\theta$ in both averages.

> [!theorem] Lemma §11.3: Young's Inequality
> For all $\theta \in [0, 1]$ and all $a, b \ge 0$,
>
> $$
> a^{1 - \theta}\, b^{\theta} \le (1 - \theta)\, a + \theta\, b.
> $$

^lem-11-3

> [!proof]+ Proof
> If $a = 0$ or $b = 0$ (with the convention $0^0 = 1$ at the endpoints $\theta \in \{0,1\}$), the left side is at most the right side directly; and for $\theta = 0$ or $\theta = 1$ both sides agree. So let $a, b > 0$ and $\theta \in (0,1)$. Since $\ln$ is increasing, the claim is equivalent to
>
> $$
> \ln\bigl(a^{1-\theta} b^{\theta}\bigr) \le \ln\bigl((1-\theta) a + \theta b\bigr),
> $$
>
> and since $\ln$ turns products into sums, the left side is $(1 - \theta) \ln a + \theta \ln b$. So the claim is
>
> $$
> (1 - \theta) \ln a + \theta \ln b \le \ln\bigl((1 - \theta) a + \theta b\bigr),
> $$
>
> which is concavity of $\ln$: the chord joining $(a, \ln a)$ and $(b, \ln b)$ lies below the graph. The point on the chord above $(1-\theta)a + \theta b$ has height $(1-\theta)\ln a + \theta \ln b$ by linearity of the chord, and the graph point above it has height $\ln\bigl((1-\theta)a + \theta b\bigr)$. (Concavity of $\ln$: $(\ln t)'' = -1/t^2 < 0$; see the [[§19 Normed Linear Spaces and Lᵖ Spaces#^lem-19-4|MATH 551 notes]] for the chord characterization.)

^pf-11-3

*Uses:* [[§19 Normed Linear Spaces and Lᵖ Spaces#^lem-19-4|551 §19.4]]

![[m556-11-1.svg]]
*Young's inequality is the case of the chord lying below the concave graph of $\ln$; the black dot is the graph value, the red dot the chord value.*

> [!remark]- Connections
> - Home in Measure Theory: [[§19 Normed Linear Spaces and Lᵖ Spaces#^lem-19-4|551 §19.4]] (the same inequality with the weights $\theta$, $1 - \theta$ exchanged, proved by the same concavity argument and drawn with the same figure).
> - Used for Hölder's inequality: [[§12 Hölder's Inequality for Sequences#^thm-12-1|§12.1]] (sequences), [[§14 The Function Spaces Lᵖ(Ω)#^lem-14-7|§14.7]] (continuous functions), [[Hölder's Inequality|551 §19.5]] (measurable functions).
