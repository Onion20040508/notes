---
subject: math
type: theorem
source: "[[Multivariable Analysis]]"
aliases: ["MATH 452 25.3", "change of variables", "Jacobian formula"]
tags: [multivariable-analysis, hub]
---
![[§25 Change of Variables on General Domains#^thm-25-3]]

## Treated in
- [[§25 Change of Variables on General Domains#^thm-25-3|Theorem §25.3: Change of Variables — General Jordan Measurable Domains]], in [[§25 Change of Variables on General Domains]]

## Its proof uses
- [[§21 The Definition of the Integral#^def-21-7|Definition §21.7: The Integral]]
- [[§24 The Change of Variables Formula#^thm-24-2|Theorem §24.2: Change of Variables Formula — Rectangular Case]]
- [[§25 Change of Variables on General Domains#^prop-25-1|Proposition §25.1: Boundary Squares Have Vanishing Total Area]]
- [[§25 Change of Variables on General Domains#^prop-25-2|Proposition §25.2: C¹ Diffeomorphisms Preserve Jordan Measurability]]

## Its proof uses (other subjects)
- [[Continuous Image of a Compact Space is Compact]] (Topology)

## Used in (Multivariable Analysis)
- [[§25 Change of Variables on General Domains#^ex-25-5|Example §25.5: Area of an Ellipse]]
- [[§25 Change of Variables on General Domains#^prop-25-4|Proposition §25.4: Isolated Zeros of the Jacobian]]
- [[§37 The Algebra of Differential Forms#^ex-37-4|Example §37.4: Pullback for Change of Variables (§15)]]

## Connections
- **Linear algebra core.** For a linear map this is [[§37 Determinants#^ladr-9-61|LADR 9.61]]: T changes volume by the factor |det T| ([[§25 Change of Variables on General Domains#^prop-25-5|Proposition §25.5]]). The C¹ case applies this to the derivative on each small square, which is the [[§24 The Change of Variables Formula#^thm-24-2|rectangular case]] (§24.2), proved with [[Multivariable Taylor's Theorem]] and the [[Multivariable Chain Rule]].
- **Generalizes.** The one-variable substitution rule [[§24 The Change of Variables Formula#^lem-24-1|Lemma §24.1]], which comes from the [[Fundamental Theorem of Calculus]] and the 451 [[§28 Basic Properties of the Derivative#^thm-28-3|chain rule]], and the [[§22 Properties of the Integral#^thm-22-6|polar formula]] (§22.6), where |J| = r. The ℝⁿ version is [[§25 Change of Variables on General Domains#^thm-25-6|Theorem §25.6]].
- **Where hypotheses matter.** J ≠ 0 is the hypothesis of the [[Inverse Function Theorem (several variables)]]. The formula survives [[§25 Change of Variables on General Domains#^prop-25-4|isolated zeros of J]] (§25.4) as long as J does not change sign. Jordan measurability of the image comes from [[§25 Change of Variables on General Domains#^prop-25-2|Proposition §25.2]]. The bounds on f∘Φ and |J| come from compactness of the closure ([[Continuous Image of a Compact Space is Compact]]).
- **In forms language.** The integrand f·|J| du dv is the pullback of f dx∧dy up to sign ([[§37 The Algebra of Differential Forms#^ex-37-4|Pullback for Change of Variables]]). Dropping the absolute value gives the signed version, where the sign of J records orientation ([[§24 The Change of Variables Formula#^rem-24-14|Orientation and Area]]).
- **Lebesgue version (pieces).** 551 proves translation invariance of the integral ([[§25 Invariance Properties and Fubini's Theorem#^thm-25-1|551 Thm. §25.1]]); for linear maps, m(T(R)) = |det T| m(R) on rectangles inside the proof of [[§30 Differentiating the Integral#^thm-30-3|551 Thm. §30.3]] (linear maps preserve null sets), and measurability of $f \circ T$ for invertible $T$, [[§30 Differentiating the Integral#^cor-30-4|551 Cor. §30.4]].
- **Also in [[Calculus]]:** [[§124 Change of Variables in Multiple Integrals#^thm-124-1|Calc Thm. §124.1]] and [[§124 Change of Variables in Multiple Integrals#^thm-124-2|Calc Thm. §124.2]] (computational treatment with worked examples).
- **Also in [[Applied Linear Algebra]]:** [[§28 Determinants as Area or Volume#^thm-28-3|235 Thm. §28.3]] and [[§28 Determinants as Area or Volume#^thm-28-4|235 Thm. §28.4]] (the linear case: a linear map multiplies area or volume by its absolute determinant, with worked examples).
