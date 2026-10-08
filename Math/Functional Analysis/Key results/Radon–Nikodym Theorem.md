---
subject: math
type: theorem
source: "[[Functional Analysis]]"
aliases: ["MATH 556 35.1", "Radon-Nikodym"]
tags: [functional-analysis, hub]
---
![[§35 Measures and the Radon–Nikodym Theorem#^thm-35-1]]

## Treated in
- [[§35 Measures and the Radon–Nikodym Theorem#^thm-35-1|Theorem §35.1: Radon–Nikodym]], in [[§35 Measures and the Radon–Nikodym Theorem]]

## Its proof uses
- [[§23 Cauchy–Schwarz and the Induced Norm#^thm-23-1|Theorem §23.1: Cauchy–Schwarz]]
- [[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^def-26-1|Definition §26.1: Bounded Linear Functional]]
- [[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^thm-26-4|Theorem §26.4: Riesz Representation Theorem]]
- [[§35 Measures and the Radon–Nikodym Theorem#^rem-35-1|Remark: Facts Assumed from Measure Theory]]
- [[§35 Measures and the Radon–Nikodym Theorem#^def-35-4|Definition §35.4: Finite Measure]]
- [[§35 Measures and the Radon–Nikodym Theorem#^def-35-5|Definition §35.5: Absolute Continuity]]

## Its proof uses (other subjects)
- [[Continuity of Measure]] (Measure Theory)
- [[Monotone Convergence Theorem (Lebesgue)]] (Measure Theory)
- [[§13 Approximation and Continuity of Measure#^prop-13-4|551 §13.4: Continuity of Measure from Below]]
- [[§20 The Lebesgue Integral for Simple Functions#^thm-20-7|551 §20.7: Monotone Convergence Theorem (MCT)]]

## Used in (Functional Analysis)
- (not cited later in the course)

## Connections
- **What it says.** If $\nu \ll \mu$ for finite measures, then $\nu$ has a density with respect to $\mu$: $\nu(E) = \int_E g\, d\mu$, $g = d\nu/d\mu$ ([[§35 Measures and the Radon–Nikodym Theorem#^def-35-6|Def. §35.6]]). The converse direction, a non-negative integrable $g$ defining an absolutely continuous measure, is Measure Theory's measure induced by a function ([[§21 Consequences of the Monotone Convergence Theorem#^def-21-1|551 Def. §21.1]]).
- **Plan of the proof (von Neumann).** Represent the bounded functional $f \mapsto \int f\, d\mu$ on $L^2(\mu + \nu)$ by the [[Riesz Representation Theorem (Hilbert spaces)|Riesz representation theorem]]; testing the identity with indicator functions ([[Functional Analysis Problem-Solving Techniques#^rem-t21|Technique 21]]) gives $0 < g_0 \le 1$, absolute continuity is used to fix $g_0$ on a null set, and $g = (1 - g_0)/g_0$, with a truncation and the [[Monotone Convergence Theorem (Lebesgue)|monotone convergence theorem]] at the end.
- **Home.** Measure Theory (MATH 551) does not state the theorem; this is its only statement in the vault. Measure Theory's absolute continuity ([[§31 Absolute Continuity#^def-31-1|551 Def. §31.1]]) is the version for functions.
