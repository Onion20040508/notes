---
type: section
subject: "[[Functional Analysis]]"
chapter: 4
section: 16
tags: [functional-analysis, math556]
---
← [[§15 ℝⁿ, C［a,b］ and ℓᵖ]] · ↑ [[· 4 Infinite-Dimensional Spaces꞉ ℓᵖ, Lᵖ, and Compactness]] · [[§17 Hölder's Inequality for Sequences]] →

*Stage: norms — Tools. The inequalities that make $\|\cdot\|_p$ a norm: Young, then Hölder ([[§17 Hölder's Inequality for Sequences|§17]]), then Minkowski ([[§18 Minkowski's Inequality and the Spaces ℓᵖ|§18]]).*

> [!theorem] Proposition §16.1: Cauchy–Schwarz in $\mathbb{R}^n$
> For $x, y \in \mathbb{R}^n$, with $\|x\| = \bigl(x_1^2 + \cdots + x_n^2\bigr)^{1/2}$,
>
> $$
> |x \cdot y| \le \|x\|\, \|y\|.
> $$

^prop-16-1

> [!proof]+ Proof
> Recalled without proof in lecture. The inequality is the case $p = q = 2$ of Hölder's inequality in $\mathbb{F}^n$ (Corollary [[§17 Hölder's Inequality for Sequences#^cor-17-2|§17.2]] in [[§17 Hölder's Inequality for Sequences|§17]], whose proof uses Young's inequality and not this proposition): by the triangle inequality for finite sums and that corollary,
>
> $$
> |x \cdot y| = \Bigl| \sum_{i=1}^n x_i y_i \Bigr| \le \sum_{i=1}^n |x_i y_i| \le \|x\|_2\, \|y\|_2 = \|x\|\, \|y\|.
> $$
>
> It is also the case $X = \mathbb{R}^n$, $(x, y) = x \cdot y$, of the Cauchy–Schwarz inequality in an inner product space (Theorem [[§23 Cauchy–Schwarz and the Induced Norm#^thm-23-1|§23.1]] in [[§23 Cauchy–Schwarz and the Induced Norm|§23]]). The standard direct arguments are via the [[§16 Means and Young's Inequality#^lem-16-2|elementary inequality below]] or the discriminant of $t \mapsto \|x + ty\|^2$.

^pf-16-1

*Uses:* [[§17 Hölder's Inequality for Sequences#^cor-17-2|§17.2]], [[§23 Cauchy–Schwarz and the Induced Norm#^thm-23-1|§23.1]]

> [!remark]- Connections
> - Home of the inequality: [[Cauchy–Schwarz inequality|LADR 6.14]]; the $p = 2$ case of [[Hölder's Inequality|551 §34.5]].
> - Re-proved for every inner product space in [[§23 Cauchy–Schwarz and the Induced Norm#^thm-23-1|§23.1]]; for infinite sequences it is the case $p = q = 2$ of [[§17 Hölder's Inequality for Sequences#^thm-17-1|§17.1]].

> [!theorem] Lemma §16.2: Arithmetic–Geometric Mean, Two Variables
> For all real $a, b$, $2ab \le a^2 + b^2$; equivalently, for $a, b \ge 0$,
>
> $$
> \sqrt{ab} \le \tfrac{1}{2}(a + b).
> $$

^lem-16-2

> [!proof]+ Proof
> $0 \le (a - b)^2 = a^2 - 2ab + b^2$. For the second form, apply the first to $\sqrt{a}, \sqrt{b}$.

^pf-16-2

The second form says that the geometric mean of two non-negative numbers is at most their arithmetic mean. Young's inequality is the weighted version: give $a$ weight $1 - \theta$ and $b$ weight $\theta$ in both averages.

> [!theorem] Lemma §16.3: Young's Inequality
> For all $\theta \in [0, 1]$ and all $a, b \ge 0$,
>
> $$
> a^{1 - \theta}\, b^{\theta} \le (1 - \theta)\, a + \theta\, b.
> $$

^lem-16-3

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
> which is concavity of $\ln$: the chord joining $(a, \ln a)$ and $(b, \ln b)$ lies below the graph. The point on the chord above $(1-\theta)a + \theta b$ has height $(1-\theta)\ln a + \theta \ln b$ by linearity of the chord, and the graph point above it has height $\ln\bigl((1-\theta)a + \theta b\bigr)$. (Proof of this inequality: put $c = (1-\theta)a + \theta b > 0$. For every $s > 0$, $\ln s \le s - 1$, because $s - 1 - \ln s$ has derivative $1 - 1/s$, which is negative on $(0,1)$ and positive on $(1,\infty)$, so its minimum is its value $0$ at $s = 1$. With $s = t/c$ this gives $\ln t \le \ln c + (t - c)/c$ for all $t > 0$. Apply it at $t = a$ and at $t = b$, multiply by $1-\theta$ and $\theta$, and add: $(1-\theta)\ln a + \theta\ln b \le \ln c + \bigl((1-\theta)a + \theta b - c\bigr)/c = \ln c$. The concavity form of the same fact is in the [[§34 Normed Linear Spaces and Lᵖ Spaces#^lem-34-4|MATH 551 notes]].)

^pf-16-3

*Uses:* [[§34 Normed Linear Spaces and Lᵖ Spaces#^lem-34-4|551 §34.4]]

![[m556-11-1.svg]]
*Young's inequality is the case of the chord lying below the concave graph of $\ln$; the black dot is the graph value, the red dot the chord value.*

> [!remark]- Connections
> - Home in Measure Theory: [[§34 Normed Linear Spaces and Lᵖ Spaces#^lem-34-4|551 §34.4]] (the same inequality with the weights $\theta$, $1 - \theta$ exchanged, proved by the same concavity argument and drawn with the same figure).
> - Used for Hölder's inequality: [[§17 Hölder's Inequality for Sequences#^thm-17-1|§17.1]] (sequences), [[§19 The Function Spaces Lᵖ(Ω)#^lem-19-7|§19.7]] (continuous functions), [[Hölder's Inequality|551 §34.5]] (measurable functions).
