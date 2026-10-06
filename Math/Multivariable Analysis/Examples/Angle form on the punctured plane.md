---
subject: math
type: example
source: "[[Multivariable Analysis]]"
tags: ["math452", "workhorse"]
---
The 1-form $\omega = \dfrac{-y\,dx + x\,dy}{x^2 + y^2}$ on $\mathbb{R}^2 \setminus \{0\}$, i.e. the vector field $\left(\dfrac{-y}{r^2}, \dfrac{x}{r^2}\right)$ circulating around the origin. Its coefficients are the partials of the polar angle $\theta$, so locally $\omega = d\theta$ and $\omega$ is closed; but $\theta$ has no continuous global choice, and $\omega$ picks up $2\pi$ around the unit circle, so it is not exact. It is the standard example showing that "closed implies exact" (curl-free implies conservative) needs a domain without holes, as in the [[Poincaré Lemma]]. The hole it detects is the one of the [[Punctured plane]] in MATH 590, where $\pi_1(\mathbb{R}^2 \setminus \{0\}) \cong \pi_1(S^1)$ ([[§34 Retractions and Fixed Points#^thm-34-2|Topology §34]]) $\cong \mathbb{Z}$ ([[Fundamental Group of the Circle]]); $\frac{1}{2\pi}\int_\gamma \omega$ is the [[§93 Argument Principle#^def-93-3|winding number]] of $\gamma$ (342 Def. §93.2). Its uses in MATH 452:

- The partials of the polar angle are $-y/r^2$ and $x/r^2$ ([[§16 The Inverse Function Theorem#^ex-16-3|§16]])
- A closed form that is not exact ([[§39 Closed and Exact Forms#^prop-39-6|§39.6]])
- Closed by direct computation; not exact because its integral around the unit circle is $2\pi$ ([[§39 Closed and Exact Forms#^pf-39-6|§39]])

## The partials of the polar angle are $-y/r^2$ and $x/r^2$
![[§16 The Inverse Function Theorem#^ex-16-3]]

## A closed form that is not exact
![[§39 Closed and Exact Forms#^prop-39-6]]

## Closed by direct computation; not exact because its integral around the unit circle is $2\pi$
![[§39 Closed and Exact Forms#^pf-39-6]]
