---
type: section
subject: "[[Multivariable Analysis]]"
chapter: 1
section: 3
tags: [multivariable-analysis, math452]
---
← [[§2 Open and Closed Sets]] · ↑ [[· 1 Foundations]] · [[§4 Partial Derivatives]] →

> [!definition] Definition §3.1: Continuity
> A function $f : \mathbb{R}^2 \to \mathbb{R}$ is **continuous** at $(x_0, y_0)$ if
>
> $$
> \forall\, \varepsilon > 0,\; \exists\, \delta > 0,\; \forall\, (x, y) \in \mathbb{R}^2: \quad |(x, y) - (x_0, y_0)| < \delta \implies |f(x, y) - f(x_0, y_0)| < \varepsilon.
> $$

^def-3-1

![[m452-3-1.svg]]
*Continuity at $(x_0, y_0)$ as a mapping statement: for every output tolerance $\varepsilon$ — the open interval from $f(x_0,y_0)-\varepsilon$ to $f(x_0,y_0)+\varepsilon$ on the real line (red, hollow endpoints) — there is an input tolerance $\delta$ whose disc $B((x_0,y_0),\delta)$ (green, dashed) is mapped entirely into that interval. The image (green bar) need not be centered or symmetric; it only needs to be trapped.*

> [!remark]- Connections
> - MATH 451: [[§17 Continuous Functions#^thm-17-1|The Epsilon-Delta Characterization]] on $\mathbb{R}$, and [[§21 More on Metric Spaces꞉ Continuity#^def-21-1|Continuous Maps Between Metric Spaces]].
> - MATH 590: [[§11 Metric Topology#^thm-11-7|ε-δ Characterization of Continuity]] shows this agrees with the open-set [[§9 Continuous Functions#^def-9-1|definition]].

> [!example] Example §3.1: Discontinuity via Path Dependence
> Consider
>
> $$
> f(x, y) = \begin{cases} \dfrac{2xy}{x^2 + y^2} & (x, y) \neq (0,0) \\[6pt] 0 & (x, y) = (0, 0). \end{cases}
> $$
>
> **Claim:** $f$ is not continuous at $(0, 0)$.
>
> **Along $x$-axis** ($y = 0$, $x \neq 0$): $|f(x, 0) - f(0, 0)| = 0 < \varepsilon$. Same for $y$-axis.
>
> **Along $y = x$:** $|f(x, x) - f(0, 0)| = \left|\dfrac{2x^2}{2x^2}\right| = 1$.
>
> Choose $\varepsilon = \tfrac{1}{2}$. No $\delta > 0$ works, so $f$ is not continuous at $(0, 0)$.

^ex-3-1

> [!remark]- Connections
> - Worked examples: the two-path test, [[§91 Limits and Continuity#^thm-91-1|Calc Thm. §91.1]], applied to xy/(x² + y²) in [[§91 Limits and Continuity#^ex-91-1|Calc Ex. §91.1]].

## Algebra of Continuous Functions

The following theorems show that continuous functions are closed under the standard algebraic operations.

> [!theorem] Theorem §3.1: Sum and Difference of Continuous Functions
> If $f, g : \mathbb{R}^2 \to \mathbb{R}$ are continuous at $(x_0, y_0)$, then $f + g$ and $f - g$ are continuous at $(x_0, y_0)$.

^thm-3-1

> [!proof]+ Proof
> We prove continuity of $f + g$; the proof for $f - g$ is similar.
>
> Let $\varepsilon > 0$. We need to find $\delta > 0$ such that
>
> $$
> |(x, y) - (x_0, y_0)| < \delta \implies |(f + g)(x, y) - (f + g)(x_0, y_0)| < \varepsilon.
> $$
>
> Since $f$ is continuous at $(x_0, y_0)$, there exists $\delta_1 > 0$ such that
>
> $$
> |(x, y) - (x_0, y_0)| < \delta_1 \implies |f(x, y) - f(x_0, y_0)| < \frac{\varepsilon}{2}.
> $$
>
> Since $g$ is continuous at $(x_0, y_0)$, there exists $\delta_2 > 0$ such that
>
> $$
> |(x, y) - (x_0, y_0)| < \delta_2 \implies |g(x, y) - g(x_0, y_0)| < \frac{\varepsilon}{2}.
> $$
>
> Let $\delta = \min\{\delta_1, \delta_2\}$. Then for $|(x, y) - (x_0, y_0)| < \delta$:
>
> $$
> \begin{aligned}
> |(f + g)(x, y) - (f + g)(x_0, y_0)| &= |f(x, y) - f(x_0, y_0) + g(x, y) - g(x_0, y_0)| \\
> &\leq |f(x, y) - f(x_0, y_0)| + |g(x, y) - g(x_0, y_0)| \\
> &< \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon.
> \end{aligned}
> $$
>
> Hence $f + g$ is continuous at $(x_0, y_0)$.

^pf-3-1

*Uses:* [[§3 Continuity and Limits of Functions#^def-3-1|Def. §3.1]], [[§3 The Set ℝ of Real Numbers#^thm-3-3|451 §3.3]]

> [!remark]- Connections
> - Computational version: [[§91 Limits and Continuity#^thm-91-5|Calc Thm. §91.5]] (with worked examples).

> [!theorem] Theorem §3.2: Product of Continuous Functions
> If $f, g : \mathbb{R}^2 \to \mathbb{R}$ are continuous at $(x_0, y_0)$, then $f \cdot g$ is continuous at $(x_0, y_0)$.

^thm-3-2

> [!proof]+ Proof
> Let $\varepsilon > 0$. We use the identity:
>
> $$
> f(x,y) g(x,y) - f(x_0, y_0) g(x_0, y_0) = f(x,y)[g(x,y) - g(x_0, y_0)] + g(x_0, y_0)[f(x,y) - f(x_0, y_0)].
> $$
>
> Since $f$ is continuous at $(x_0, y_0)$, it is bounded near $(x_0, y_0)$: there exist $\delta_1 > 0$ and $M > 0$ such that
>
> $$
> |(x, y) - (x_0, y_0)| < \delta_1 \implies |f(x, y)| \leq M.
> $$
>
> (We can take $M = |f(x_0, y_0)| + 1$ by choosing $\delta_1$ small enough.)
>
> Let $K = |g(x_0, y_0)|$. Choose $\delta_2 > 0$ such that
>
> $$
> |(x, y) - (x_0, y_0)| < \delta_2 \implies |g(x, y) - g(x_0, y_0)| < \frac{\varepsilon}{2M}.
> $$
>
> Choose $\delta_3 > 0$ such that
>
> $$
> |(x, y) - (x_0, y_0)| < \delta_3 \implies |f(x, y) - f(x_0, y_0)| < \frac{\varepsilon}{2(K + 1)}.
> $$
>
> Let $\delta = \min\{\delta_1, \delta_2, \delta_3\}$. Then for $|(x, y) - (x_0, y_0)| < \delta$:
>
> $$
> \begin{aligned}
> |f(x,y) g(x,y) - f(x_0, y_0) g(x_0, y_0)| &\leq |f(x,y)| \cdot |g(x,y) - g(x_0, y_0)| + |g(x_0, y_0)| \cdot |f(x,y) - f(x_0, y_0)| \\
> &< M \cdot \frac{\varepsilon}{2M} + K \cdot \frac{\varepsilon}{2(K + 1)} \\
> &< \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon.
> \end{aligned}
> $$
>
> Hence $f \cdot g$ is continuous at $(x_0, y_0)$.

^pf-3-2

*Uses:* [[§3 Continuity and Limits of Functions#^def-3-1|Def. §3.1]], [[§3 The Set ℝ of Real Numbers#^thm-3-3|451 §3.3]]

> [!remark]- Connections
> - Computational version: [[§91 Limits and Continuity#^thm-91-5|Calc Thm. §91.5]] (with worked examples).

> [!theorem] Theorem §3.3: Quotient of Continuous Functions
> If $f, g : \mathbb{R}^2 \to \mathbb{R}$ are continuous at $(x_0, y_0)$ and $g(x_0, y_0) \neq 0$, then $f/g$ is continuous at $(x_0, y_0)$.

^thm-3-3

> [!proof]+ Proof
> It suffices to prove that $1/g$ is continuous at $(x_0, y_0)$ (then apply the [[§3 Continuity and Limits of Functions#^thm-3-2|product rule]] to $f \cdot (1/g)$).
>
> Let $\varepsilon > 0$ and let $L = g(x_0, y_0) \neq 0$.
>
> **Step 1:** Since $g$ is continuous and $L \neq 0$, there exists $\delta_1 > 0$ such that
>
> $$
> |(x, y) - (x_0, y_0)| < \delta_1 \implies |g(x, y) - L| < \frac{|L|}{2}.
> $$
>
> This implies $|g(x, y)| > |L| - \frac{|L|}{2} = \frac{|L|}{2} > 0$, so $g(x,y) \neq 0$ near $(x_0, y_0)$.
>
> **Step 2:** We have
>
> $$
> \left|\frac{1}{g(x,y)} - \frac{1}{L}\right| = \frac{|L - g(x,y)|}{|g(x,y)| \cdot |L|} < \frac{|g(x,y) - L|}{\frac{|L|}{2} \cdot |L|} = \frac{2|g(x,y) - L|}{|L|^2}.
> $$
>
> **Step 3:** Choose $\delta_2 > 0$ such that
>
> $$
> |(x, y) - (x_0, y_0)| < \delta_2 \implies |g(x, y) - L| < \frac{\varepsilon |L|^2}{2}.
> $$
>
> Let $\delta = \min\{\delta_1, \delta_2\}$. Then for $|(x, y) - (x_0, y_0)| < \delta$:
>
> $$
> \left|\frac{1}{g(x,y)} - \frac{1}{L}\right| < \frac{2}{|L|^2} \cdot \frac{\varepsilon |L|^2}{2} = \varepsilon.
> $$
>
> Hence $1/g$ is continuous at $(x_0, y_0)$.

^pf-3-3

*Uses:* [[§3 Continuity and Limits of Functions#^def-3-1|Def. §3.1]], [[§3 Continuity and Limits of Functions#^thm-3-2|§3.2]], [[§3 The Set ℝ of Real Numbers#^thm-3-3|451 §3.3]]

> [!remark]- Connections
> - Computational version: [[§91 Limits and Continuity#^thm-91-5|Calc Thm. §91.5]] (with worked examples).

> [!theorem] Theorem §3.4: Composition of Continuous Functions
> If $\varphi, \psi : \mathbb{R}^2 \to \mathbb{R}$ are continuous at $(a, b)$, and $f : \mathbb{R}^2 \to \mathbb{R}$ is continuous at $(\varphi(a,b), \psi(a,b))$, then
>
> $$
> g(x,y) = f(\varphi(x,y), \psi(x,y))
> $$
>
> is continuous at $(a, b)$.

^thm-3-4

> [!proof]+ Proof
> Let $\varepsilon > 0$. We need to find $\delta > 0$ such that $|(x,y) - (a,b)| < \delta$ implies $|g(x,y) - g(a,b)| < \varepsilon$.
>
> **Step 1:** Since $f$ is continuous at $(\varphi(a,b), \psi(a,b))$, there exists $\sigma > 0$ such that
>
> $$
> |(\xi, \eta) - (\varphi(a,b), \psi(a,b))| < \sigma \implies |f(\xi, \eta) - f(\varphi(a,b), \psi(a,b))| < \varepsilon.
> $$
>
> **Step 2:** Since $\varphi$ is continuous at $(a,b)$, there exists $\delta_1 > 0$ such that
>
> $$
> |(x,y) - (a,b)| < \delta_1 \implies |\varphi(x,y) - \varphi(a,b)| < \frac{\sigma}{\sqrt{2}}.
> $$
>
> **Step 3:** Since $\psi$ is continuous at $(a,b)$, there exists $\delta_2 > 0$ such that
>
> $$
> |(x,y) - (a,b)| < \delta_2 \implies |\psi(x,y) - \psi(a,b)| < \frac{\sigma}{\sqrt{2}}.
> $$
>
> **Conclusion:** Let $\delta = \min\{\delta_1, \delta_2\}$. For $|(x,y) - (a,b)| < \delta$:
>
> $$
> |(\varphi(x,y), \psi(x,y)) - (\varphi(a,b), \psi(a,b))| = \sqrt{|\varphi(x,y) - \varphi(a,b)|^2 + |\psi(x,y) - \psi(a,b)|^2} < \sqrt{\frac{\sigma^2}{2} + \frac{\sigma^2}{2}} = \sigma.
> $$
>
> Hence by Step 1: $|f(\varphi(x,y), \psi(x,y)) - f(\varphi(a,b), \psi(a,b))| < \varepsilon$, i.e., $|g(x,y) - g(a,b)| < \varepsilon$.

^pf-3-4

*Uses:* [[§3 Continuity and Limits of Functions#^def-3-1|Def. §3.1]]

> [!remark]- Connections
> - MATH 451 versions: [[§17 Continuous Functions#^thm-17-3|Arithmetic of Continuous Functions]] and [[§17 Continuous Functions#^thm-17-4|Composition of Continuous Functions]].
> - MATH 590 version for arbitrary spaces: [[§9 Continuous Functions#^thm-9-4|Rules for Continuous Functions]].
> - The differentiable analogues: [[§6 Differentiability#^thm-6-6|§6.6]]–[[§6 Differentiability#^thm-6-9|§6.9]]; §3.4 is proved again as [[§10 Composition of Functions and the Chain Rule#^thm-10-1|Continuity of Composition]] in §10.
> - Computational version: [[§91 Limits and Continuity#^thm-91-5|Calc Thm. §91.5]] (b), composition with a function of one variable.

> [!remark] Remark: Summary: Algebra of Continuous Functions
> If $f$ and $g$ are continuous at $(x_0, y_0)$, then so are:
>
> | **Operation** | **Condition** |
> |:---:|:---:|
> | $f + g$ | (none) |
> | $f - g$ | (none) |
> | $f \cdot g$ | (none) |
> | $f / g$ | $g(x_0, y_0) \neq 0$ |
> | $h \circ (f, g)$ | $h$ continuous at $(f(x_0, y_0), g(x_0, y_0))$ |

^rem-3-1

> [!definition] Definition §3.2: Limit of a Function
> We write $\displaystyle\lim_{(x,y) \to (x_0, y_0)} f(x, y) = A$ if there exists $A$ such that
>
> $$
> \forall\, \varepsilon > 0,\; \exists\, \delta > 0,\; \forall\, (x, y): \quad 0 < |(x, y) - (x_0, y_0)| < \delta \implies |f(x, y) - A| < \varepsilon.
> $$

^def-3-2

> [!remark]- Connections
> - MATH 451 version: [[§20 Limits of Functions#^def-20-1|Limit of a Function Along a Set]] and its [[§20 Limits of Functions#^rem-20-1|epsilon-delta version]].
> - Computational version: [[§91 Limits and Continuity#^def-91-1|Calc Def. §91.1]] (with worked examples).

> [!example] Example §3.2: Nonexistence of Limit
> Let $f(x, y) = \dfrac{2xy}{x^2 + y^2}$ for $(x, y) \neq (0, 0)$. Then $f$ has no limit at $(0, 0)$.
>
> Along $y = kx$: $f(x, kx) = \dfrac{2kx^2}{x^2 + k^2 x^2} = \dfrac{2k}{1 + k^2}$, which depends on $k$.

^ex-3-2

![[m452-3-2.svg]]
*Level structure of $f(x,y) = \frac{2xy}{x^2+y^2}$: on each line $y = kx$ through the origin (hollow: $f$ is not defined there) $f$ is constant, equal to $\frac{2k}{1+k^2}$ — $1$ on $y = x$ (dark red), $-1$ on $y = -x$ (dark blue), $\pm\frac45$ on $y = 2x,\ \tfrac12 x$ and $y = -2x,\ -\tfrac12 x$, and $0$ on both axes. Every disc around the origin (dashed) meets all of these lines, so $f$ takes every value in $[-1,1]$ arbitrarily close to $(0,0)$ and no single limit $A$ can work.*

> [!remark]- Connections
> - Worked examples: the two-path test, [[§91 Limits and Continuity#^thm-91-1|Calc Thm. §91.1]], applied to xy/(x² + y²) in [[§91 Limits and Continuity#^ex-91-1|Calc Ex. §91.1]].

> [!definition] Definition §3.3: Big-O and Little-o Notation
> Let $\rho = \sqrt{x^2 + y^2}$.
> - $f(x, y) = O(\rho)$ means $|f(x, y)| \leq C\rho$ for some constant $C$ near the origin.
> - $f(x, y) = o(\rho)$ means $\displaystyle\lim_{\rho \to 0} \frac{f(x, y)}{\rho} = 0$ (i.e., $f$ vanishes faster than $\rho$).

^def-3-3

> [!example] Example §3.3
> $f(x, y) = x^2 + y^2 = o(\rho)$, since $\dfrac{x^2 + y^2}{\sqrt{x^2 + y^2}} = \sqrt{x^2 + y^2} \to 0$.

^ex-3-3
