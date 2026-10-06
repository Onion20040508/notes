---
type: section
subject: "[[Measure Theory]]"
chapter: 3
section: 13
tags: [measure-theory, math551]
---
← [[§13 Egorov's and Lusin's Theorems]] · ↑ [[· 3 Measure Theory]] · [[§14 The Lebesgue Integral for Simple Functions]] →

Chapter 3 returns to a few objects again and again: the rationals, the Vitali set, the Cantor set, the power sequence $x^k$, and sequences whose mass escapes to infinity. This section gathers their appearances in the chapter.

## The Rationals ℚ

Countable sets, $\mathbb{Q}$ in particular, have outer measure zero; the rationals also define the relation $x \sim y \iff x - y \in \mathbb{Q}$ behind the Vitali set ([[§11b The Vitali Set and the Cantor Set#^def-11-10|Definition §11.10]], embedded below).

![[§9 Lebesgue Outer Measure#^ex-9-2]]

*Chain:* ← [[§8a The Rationals ℚ|Chapter 2]] · [[§18 Differentiation Theory#^ex-18-1|Chapter 5]] →

## The Vitali Set

A set $V \subseteq [0,1]$ containing exactly one point from each class of $x \sim y \iff x - y \in \mathbb{Q}$, chosen with the Axiom of Choice. Its rational translates are pairwise disjoint and cover $[0,1]$ inside $[-1,2]$, so it cannot be measurable; it is why measurability has to be tested against every set. All its appearances are listed in [[Vitali set]].

![[§10 Lebesgue Measurable Sets#^rem-10-2]]

![[§11 Borel Sets and Measure Spaces#^rem-11-2]]

![[§11b The Vitali Set and the Cantor Set#^def-11-10]]

![[§11b The Vitali Set and the Cantor Set#^def-11-12]]

![[§11b The Vitali Set and the Cantor Set#^prop-11-19]]

![[§11b The Vitali Set and the Cantor Set#^thm-11-20]]

![[§11b The Vitali Set and the Cantor Set#^rem-11-6]]

*Chain:* [[§14a Consequences of the Monotone Convergence Theorem#^rem-14-7|Chapter 4]] →

## The Cantor Set

The middle-thirds Cantor set is closed, hence Borel and measurable (the Borel-hierarchy remark above), compact, null and uncountable, so it separates "small in measure" from "small in cardinality". All its appearances are listed in [[Cantor set and Cantor function]].

![[§11b The Vitali Set and the Cantor Set#^def-11-13]]

![[§11b The Vitali Set and the Cantor Set#^prop-11-21]]

![[§11b The Vitali Set and the Cantor Set#^rem-11-7]]

*Chain:* [[§18e The Cantor Function|Chapter 5]] →

## Escaping Mass

Sets and functions whose mass slides off to infinity show that the finiteness hypotheses of continuity of measure from above and of Egorov's theorem cannot be dropped. All its appearances are listed in [[Escaping mass sequences]].

![[§11a Approximation and Continuity of Measure#^rem-11-5]]

![[§13 Egorov's and Lusin's Theorems#^rem-13-1]]

*Chain:* [[§17b Escaping Mass Sequences|Chapter 4]] →

## The Power Sequence xᵏ

The sequence $f_k(x) = x^k$ on $[0,1]$ converges pointwise but not uniformly; the non-uniformity is confined near $x = 1$, so deleting an interval of length $\delta$ restores uniform convergence, as Egorov's theorem promises in general.

![[§12b Simple Functions and Modes of Convergence#^ex-12-4]]

![[§13 Egorov's and Lusin's Theorems#^ex-13-1]]

*Chain:* only in this chapter; its MATH 451 appearance is listed in [[Power sequence xᵏ]].
