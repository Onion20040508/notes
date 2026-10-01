---
subject: math
type: theorem
source: "[[Multivariable Analysis]]"
aliases: ["MATH 452 15.17", "change of variables", "Jacobian formula"]
tags: [multivariable-analysis, hub]
---
![[§15 Multivariable Integration#^thm-15-17]]

## Treated in
- [[§15 Multivariable Integration#^thm-15-17|Theorem §15.17: Change of Variables — General Jordan Measurable Domains]], in [[§15 Multivariable Integration]]

## Its proof uses
- [[§15 Multivariable Integration#^def-15-11|Definition §15.11: The Integral]]
- [[§15 Multivariable Integration#^thm-15-14|Theorem §15.14: Change of Variables Formula — Rectangular Case]]
- [[§15 Multivariable Integration#^prop-15-15|Proposition §15.15: Boundary Squares Have Vanishing Total Area]]
- [[§15 Multivariable Integration#^prop-15-16|Proposition §15.16: C¹ Diffeomorphisms Preserve Jordan Measurability]]

## Its proof uses (other subjects)
- [[Continuous Image of a Compact Space is Compact]] (Topology)

## Used in (Multivariable Analysis)
- [[§15 Multivariable Integration#^ex-15-8|Example §15.8: Area of an Ellipse]]
- [[§15 Multivariable Integration#^prop-15-18|Proposition §15.18: Isolated Zeros of the Jacobian]]
- [[§22 The Algebra of Differential Forms#^ex-22-4|Example §22.4: Pullback for Change of Variables (§15)]]

## Connections
- **Linear algebra core.** For a linear map this is [[§34 Determinants#^ladr-9-61|LADR 9.61]]: T changes volume by the factor |det T| ([[§15 Multivariable Integration#^prop-15-19|Proposition §15.19]]). The C¹ case applies this to the derivative on each small square, which is the [[§15 Multivariable Integration#^thm-15-14|rectangular case]] (§15.14), proved with [[Multivariable Taylor's Theorem]] and the [[Multivariable Chain Rule]].
- **Generalizes.** The one-variable substitution rule [[§15 Multivariable Integration#^lem-15-13|Lemma §15.13]], which comes from the [[Fundamental Theorem of Calculus]] and the 451 chain rule, and the [[§15 Multivariable Integration#^thm-15-7|polar formula]] (§15.7), where |J| = r. The ℝⁿ version is [[§15 Multivariable Integration#^thm-15-20|Theorem §15.20]].
- **Where hypotheses matter.** J ≠ 0 is the hypothesis of the [[Inverse Function Theorem (several variables)]]. The formula survives [[§15 Multivariable Integration#^prop-15-18|isolated zeros of J]] (§15.18) as long as J does not change sign. Jordan measurability of the image comes from [[§15 Multivariable Integration#^prop-15-16|Proposition §15.16]]. The bounds on f∘Φ and |J| come from compactness of the closure ([[Continuous Image of a Compact Space is Compact]]).
- **In forms language.** The integrand f·|J| du dv is the pullback of f dx∧dy up to sign ([[§22 The Algebra of Differential Forms#^ex-22-4|Pullback for Change of Variables]]). Dropping the absolute value gives the signed version, where the sign of J records orientation ([[§15 Multivariable Integration#^rem-15-14|Orientation and Area]]).
- Lebesgue-measure pieces proved in 551: translation invariance of the integral ([[§17 Invariance Properties and Fubini's Theorem#^thm-17-1|551 Thm. §17.1]]); for linear maps, $m(T(R)) = |\det T|\, m(R)$ on rectangles inside the proof of [[§18 Differentiation Theory#^thm-18-22|551 Thm. §18.22]] (linear maps preserve null sets), and measurability of $f \circ T$ for invertible $T$, [[§18 Differentiation Theory#^cor-18-23|551 Cor. §18.23]].
