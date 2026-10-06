---
type: section
subject: "[[Single Variable Analysis]]"
section: "22a"
chapter: 3
tags: [real-analysis, math451, examples]
---
← [[§22 More on Metric Spaces꞉ Connectedness]] · ↑ [[· 3 Continuity]] · [[§23 Power Series]] →

The square root $f(x) = \sqrt{x}$ on $[0, +\infty)$ appears three times in this chapter. Each time it shows how $\delta$ depends on the point: the function is steep near $0$ and flat far out. The items stay in their sections; they are gathered here in course order.

## Continuity at Every Point (§17)

The $(\varepsilon, \delta)$ proof needs $\delta = \varepsilon\sqrt{x_0}$ for $x_0 > 0$ and a separate argument, $\delta = \varepsilon^2$, at $x_0 = 0$. So $\delta$ shrinks as $x_0$ approaches $0$, which raises the question of uniform continuity.

![[§17 Continuous Functions#^ex-17-3]]

## Uniformly Continuous, Yet with Unbounded Derivative (§19)

On $[0,1]$ the closed-interval theorem gives uniform continuity, although $f'(x) = \tfrac{1}{2\sqrt x}$ is unbounded. So a bounded derivative is sufficient for uniform continuity but not necessary.

![[§19 Uniform Continuity#^rem-19-4]]

## Uniformly Continuous on the Whole Half-Line (§19)

The closed-interval theorem on $[0,1]$, the bounded-derivative theorem on $[1, +\infty)$ and the gluing lemma at $c = 1$ together cover $[0, +\infty)$.

![[§19 Uniform Continuity#^ex-19-5]]

*Chain: earlier in [[§8 A Discussion About Proofs#^ex-8-8|Example §8.8]] (square roots preserve limits) · later in [[§28 Basic Properties of the Derivative#^ex-28-1|Example §28.1]] (the square root of the absolute value is not differentiable at 0)*
