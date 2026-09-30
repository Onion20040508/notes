---
type: section
subject: "[[Multivariable Analysis]]"
chapter: 1
section: 1
tags: [multivariable-analysis, math452]
---
↑ [[Multivariable Analysis — 1 Foundations]] · [[Multivariable Analysis §2 Open and Closed Sets]] →

> [!definition] Definition §1.1: Convergence of Sequences in $\mathbb{R}^n$
> A sequence $(a_n) \subset \mathbb{R}^n$ **converges** to $A \in \mathbb{R}^n$ if
>
> $$
> \forall\, \varepsilon > 0,\; \exists\, N \in \mathbb{N},\; \forall\, n \geq N: \quad |a_n - A| < \varepsilon.
> $$
>
> For vectors in $\mathbb{R}^2$, the distance is $|(a_n, b_n) - (A, B)| = \sqrt{(a_n - A)^2 + (b_n - B)^2}$.

^def-1-1

> [!remark]- Connections
> - MATH 451 versions: [[Single Variable Analysis §7 Limits of Sequences#^def-7-2|Convergence of a Sequence]] in $\mathbb{R}$, and [[Single Variable Analysis §13 Some Topological Concepts in Metric Spaces#^def-13-2|Convergence in a Metric Space]] with the [[Single Variable Analysis §13 Some Topological Concepts in Metric Spaces#^ex-13-3|Euclidean distance]].
> - Topological version (neighborhoods instead of $\varepsilon$): [[Topology §7 Interior and Closure#^def-7-4|Convergence]] in MATH 590.

> [!example] Example §1.1
> Show that $(e^{-n}\cos(n), e^{-n}\sin(n)) \to (0, 0)$.
>
> **Scratch work:** Compute the distance:
>
> $$
> |(e^{-n}\cos(n), e^{-n}\sin(n)) - (0, 0)| = \sqrt{e^{-2n}\cos^2(n) + e^{-2n}\sin^2(n)} = e^{-n}.
> $$
>
> We need $e^{-n} < \varepsilon$, i.e., $n > \ln(1/\varepsilon)$.

^ex-1-1

> [!proof]+ Proof
> Let $\varepsilon > 0$. Without loss of generality, assume $\varepsilon < 1$. Let $N = \lfloor \ln(1/\varepsilon) \rfloor + 1$. Then for all $n \geq N$, we have $n > \ln(1/\varepsilon)$, so $e^{-n} < \varepsilon$. Therefore
>
> $$
> |(e^{-n}\cos(n), e^{-n}\sin(n)) - (0, 0)| = e^{-n} < \varepsilon.
> $$

^pf-ex-1-1

*Uses:* [[Multivariable Analysis §1 Sequences and Limits in ℝⁿ#^def-1-1|Def. §1.1]]
