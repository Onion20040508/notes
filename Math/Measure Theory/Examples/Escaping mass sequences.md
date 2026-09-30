---
subject: math
type: example
source: "[[Measure Theory]]"
tags: ["math551", "workhorse"]
---
Sequences that converge to $0$ pointwise while their mass does not go away: it slides off to infinity ($\chi_{[k,k+1]}$, $\chi_{(k,\infty)}$, $[n,\infty)$), spreads out thinly ($1/k$ on $\mathbb{R}$), or piles up on a shrinking interval ($k\,\chi_{(0,1/k)}$). Each one breaks a limit theorem (continuity of measure, Egorov, MCT, Fatou) by violating its finiteness or domination hypothesis, which is why those hypotheses are there. Its uses in MATH 551:

- Continuity from above fails for $E_n = [n, \infty)$ ([[§11 Borel Sets and Measure Spaces#^rem-11-5|§11]])
- Egorov fails on $\mathbb{R}$ for $\chi_{[k,k+1]}$ ([[§13 Egorov's and Lusin's Theorems#^rem-13-1|§13]])
- Decreasing MCT fails for $\chi_{(k,\infty)}$ ([[§14 The Lebesgue Integral for Simple Functions#^rem-14-6|§14]])
- Fatou's inequality is strict for $k\,\chi_{(0,1/k)}$ ([[§14 The Lebesgue Integral for Simple Functions#^ex-14-1|§14]])
- Strategy: constant on an infinite-measure set ([[Measure Theory Problem-Solving Techniques#^rem-19-22|Techniques]])
- Homework instances: $1/k$ on $\mathbb{R}$ and $-\chi_{\{|x|>k\}}$ ([[Measure Theory Problem-Solving Techniques#^ex-19-24|Techniques]])

## Continuity from above fails for $E_n = [n, \infty)$
![[§11 Borel Sets and Measure Spaces#^rem-11-5]]

## Egorov fails on $\mathbb{R}$ for $\chi_{[k,k+1]}$
![[§13 Egorov's and Lusin's Theorems#^rem-13-1]]

## Decreasing MCT fails for $\chi_{(k,\infty)}$
![[§14 The Lebesgue Integral for Simple Functions#^rem-14-6]]

## Fatou's inequality is strict for $k\,\chi_{(0,1/k)}$
![[§14 The Lebesgue Integral for Simple Functions#^ex-14-1]]

## Strategy: constant on an infinite-measure set
![[Measure Theory Problem-Solving Techniques#^rem-19-22]]

## Homework instances: $1/k$ on $\mathbb{R}$ and $-\chi_{\{|x|>k\}}$
![[Measure Theory Problem-Solving Techniques#^ex-19-24]]
