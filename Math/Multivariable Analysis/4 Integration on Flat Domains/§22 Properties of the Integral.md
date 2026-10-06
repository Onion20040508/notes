---
type: section
subject: "[[Multivariable Analysis]]"
chapter: 4
section: 22
tags: [multivariable-analysis, math452]
---
← [[§21 The Definition of the Integral]] · ↑ [[· 4 Integration on Flat Domains]] · [[§23 Fubini's Theorem]] →

## Properties of the Integral

Throughout, assume $D$ is bounded and Jordan measurable, and all functions are integrable on $D$. In the proofs, $S_{\mathcal{T}}^+(f)$ and $S_{\mathcal{T}}^-(f)$ denote the upper and lower sums $U(f, \mathcal{T})$ and $L(f, \mathcal{T})$ of [[§21 The Definition of the Integral#^def-21-2|Def. §21.2]] and [[§21 The Definition of the Integral#^def-21-3|Def. §21.3]].

> [!theorem] Theorem §22.1: Scalar Multiplication
> If $f$ is integrable on $D$ and $c \in \mathbb{R}$, then $cf$ is integrable on $D$ and:
>
> $$
> \iint_D cf \, dA = c \iint_D f \, dA.
> $$

^thm-22-1

> [!proof]+ Proof
> Assume $c > 0$ (the case $c < 0$ is similar, and $c = 0$ is trivial).
>
> For any partition $\mathcal{T}$:
>
> $$
> S_{\mathcal{T}}^+(cf) = \sum_{i=1}^{N} \sup_{(x,y) \in D_i} (cf) \cdot |D_i| = \sum_{i=1}^{N} c \cdot \sup_{(x,y) \in D_i} f \cdot |D_i| = c \cdot S_{\mathcal{T}}^+(f).
> $$
>
> Similarly, $S_{\mathcal{T}}^-(cf) = c \cdot S_{\mathcal{T}}^-(f)$.
>
> Therefore:
>
> $$
> S_{\mathcal{T}}^+(cf) - S_{\mathcal{T}}^-(cf) = c \cdot \left( S_{\mathcal{T}}^+(f) - S_{\mathcal{T}}^-(f) \right).
> $$
>
> Since $f$ is integrable, $S_{\mathcal{T}}^+(f) - S_{\mathcal{T}}^-(f) \to 0$ as $\|\mathcal{T}\| \to 0$, so the same holds for $cf$.
>
> To evaluate: choose sample points $(\xi_i, \eta_i) \in D_i$. Then:
>
> $$
> \sum_{i=1}^{N} cf(\xi_i, \eta_i) |D_i| = c \sum_{i=1}^{N} f(\xi_i, \eta_i) |D_i| \xrightarrow{\|\mathcal{T}\| \to 0} c \iint_D f \, dA.
> $$

^pf-22-1

*Uses:* [[§21 The Definition of the Integral#^def-21-2|Def. §21.2]], [[§21 The Definition of the Integral#^def-21-3|Def. §21.3]], [[§21 The Definition of the Integral#^def-21-6|Def. §21.6]], [[§21 The Definition of the Integral#^rem-21-6|§21 Rem. (Evaluating the Integral)]]

> [!remark]- Connections
> - Computational version: [[§116 Double Integrals Over General Regions#^thm-116-3|Calc Thm. §116.3]] (linearity and comparison).

> [!theorem] Theorem §22.2: Additivity in the Integrand
> If $f$ and $g$ are integrable on $D$, then $f + g$ is integrable on $D$ and:
>
> $$
> \iint_D (f + g) \, dA = \iint_D f \, dA + \iint_D g \, dA.
> $$

^thm-22-2

> [!proof]+ Proof
> **Step 1: Bound the upper sums.**
>
> For any $(x, y) \in D_i$: $f(x,y) + g(x,y) \leq \sup_{D_i} f + \sup_{D_i} g$.
>
> Taking sup over $(x, y) \in D_i$: $\sup_{D_i}(f + g) \leq \sup_{D_i} f + \sup_{D_i} g$.
>
> Therefore:
>
> $$
> S_{\mathcal{T}}^+(f + g) = \sum_{i=1}^{N} \sup_{D_i}(f + g) \cdot |D_i| \leq \sum_{i=1}^{N} \left( \sup_{D_i} f + \sup_{D_i} g \right) |D_i| = S_{\mathcal{T}}^+(f) + S_{\mathcal{T}}^+(g).
> $$
>
> **Step 2: Bound the lower sums.**
>
> Similarly: $\inf_{D_i}(f + g) \geq \inf_{D_i} f + \inf_{D_i} g$.
>
> Therefore:
>
> $$
> S_{\mathcal{T}}^-(f + g) \geq S_{\mathcal{T}}^-(f) + S_{\mathcal{T}}^-(g).
> $$
>
> **Step 3: Integrability.**
>
> Combining:
>
> $$
> S_{\mathcal{T}}^-(f) + S_{\mathcal{T}}^-(g) \leq S_{\mathcal{T}}^-(f + g) \leq S_{\mathcal{T}}^+(f + g) \leq S_{\mathcal{T}}^+(f) + S_{\mathcal{T}}^+(g).
> $$
>
> Since $f$ and $g$ are integrable, both $S_{\mathcal{T}}^+(f) - S_{\mathcal{T}}^-(f) \to 0$ and $S_{\mathcal{T}}^+(g) - S_{\mathcal{T}}^-(g) \to 0$.
>
> By the [[Squeeze Theorem|squeeze theorem]], $S_{\mathcal{T}}^+(f+g) - S_{\mathcal{T}}^-(f+g) \to 0$, so $f + g$ is integrable.
>
> **Step 4: Evaluate the integral.**
>
> Choose sample points $(\xi_i, \eta_i) \in D_i$:
>
> $$
> \sum_{i=1}^{N} (f + g)(\xi_i, \eta_i) |D_i| = \sum_{i=1}^{N} f(\xi_i, \eta_i) |D_i| + \sum_{i=1}^{N} g(\xi_i, \eta_i) |D_i|.
> $$
>
> As $\|\mathcal{T}\| \to 0$:
>
> $$
> \iint_D (f + g) \, dA = \iint_D f \, dA + \iint_D g \, dA.
> $$

^pf-22-2

*Uses:* [[§21 The Definition of the Integral#^def-21-2|Def. §21.2]], [[§21 The Definition of the Integral#^def-21-3|Def. §21.3]], [[§21 The Definition of the Integral#^def-21-6|Def. §21.6]], [[§21 The Definition of the Integral#^rem-21-6|§21 Rem. (Evaluating the Integral)]], [[Squeeze Theorem|451 §8.1]]

> [!remark]- Connections
> - Together with [[§22 Properties of the Integral#^thm-22-1|Theorem §22.1]], the 2D version of [[§33 Properties of the Riemann Integral#^thm-33-2|Linearity]] (451 §33.2).
> - Computational version: [[§116 Double Integrals Over General Regions#^thm-116-3|Calc Thm. §116.3]] (linearity and comparison).

> [!theorem] Theorem §22.3: Additivity over Domains
> Let $A$ and $B$ be Jordan measurable, almost disjoint sets. If $f$ is integrable on $A$, $B$, and $A \cup B$, then:
>
> $$
> \iint_{A \cup B} f \, dA = \iint_A f \, dA + \iint_B f \, dA.
> $$

^thm-22-3

> [!proof]+ Proof
> Let $\mathcal{T}_A$ be a partition of $A$ and $\mathcal{T}_B$ be a partition of $B$.
>
> Then $\mathcal{T}_A \cup \mathcal{T}_B$ is a partition of $A \cup B$ (since $A$ and $B$ are almost disjoint).
>
> If $\|\mathcal{T}_A\| \to 0$ and $\|\mathcal{T}_B\| \to 0$, then $\|\mathcal{T}_A \cup \mathcal{T}_B\| \to 0$.
>
> Suppose $\mathcal{T}_A$ has $N$ pieces and $\mathcal{T}_B$ has $M$ pieces. Then for sample points:
>
> $$
> \sum_{i=1}^{N+M} f(\xi_i, \eta_i) |D_i| = \underbrace{\sum_{i=1}^{N} f(\xi_i, \eta_i) |D_i|}_{\text{sum over } \mathcal{T}_A} + \underbrace{\sum_{i=1}^{M} f(\xi_i, \eta_i) |D_i|}_{\text{sum over } \mathcal{T}_B}.
> $$
>
> Taking $\|\mathcal{T}_A\|, \|\mathcal{T}_B\| \to 0$:
>
> $$
> \iint_{A \cup B} f \, dA = \iint_A f \, dA + \iint_B f \, dA.
> $$

^pf-22-3

*Uses:* [[§20 Multivariable Integration#^def-20-8|Def. §20.8]], [[§21 The Definition of the Integral#^def-21-1|Def. §21.1]], [[§21 The Definition of the Integral#^def-21-5|Def. §21.5]], [[§21 The Definition of the Integral#^rem-21-6|§21 Rem. (Evaluating the Integral)]]

> [!remark]- Connections
> - 1D version: [[§33 Properties of the Riemann Integral#^thm-33-5|Additivity over Subintervals]] (451 §33.5), where the “almost disjoint” pieces $[a,c]$ and $[c,b]$ share only the point $c$.
> - Lebesgue version for countably many disjoint measurable pieces: [[§22 The General Lebesgue Integral#^thm-22-4|551 Thm. §22.4]].
> - Computational version: [[§116 Double Integrals Over General Regions#^thm-116-4|Calc Thm. §116.4]].

> [!remark] Remark: On the Intersection and Integrability
> A subtle point in the proof: when we combine $\mathcal{T}_A \cup \mathcal{T}_B$, pieces from $\mathcal{T}_A$ and $\mathcal{T}_B$ may overlap on $A \cap B$ (which lies in the boundaries since $A$ and $B$ are almost disjoint).
>
> Why doesn't this cause problems?
> - Since $A$ and $B$ are almost disjoint, $A \cap B \subseteq \partial A \cup \partial B$: a common point cannot be interior to both sets, so it is a boundary point of at least one of them.
> - For Jordan measurable sets, the boundary has Jordan content zero ([[§20 Multivariable Integration#^rem-20-2|§20 Remark]]), so $\partial A \cup \partial B$ does too: $|A \cap B| = 0$.
> - Any contribution from the intersection region has measure zero and doesn't affect the integral.
>
> More precisely, if a piece $D_i \in \mathcal{T}_A$ overlaps with a piece $D_j \in \mathcal{T}_B$, their overlap $D_i \cap D_j$ has Jordan content zero (it's contained in $A \cap B$). So even if we “double-count” this region, it contributes zero to both sums.
>
> This is why we need the hypothesis that $A$ and $B$ are **Jordan measurable** (not just arbitrary sets) — the boundary must have content zero for the additivity to work cleanly.

^rem-22-7

> [!remark] Remark
> To evaluate the integral, we only need *one* sequence of partitions whose mesh goes to zero. The limit is the same regardless of how we partition or where we choose sample points.

^rem-22-8

### Comparison / Mean-Value Property

> [!theorem] Theorem §22.4: Comparison Theorem
> If $f$ and $g$ are integrable on $D$ and $f \leq g$ on $D$, then:
>
> $$
> \iint_D f \, dA \leq \iint_D g \, dA.
> $$

^thm-22-4

> [!proof]+ Proof
> It suffices to show: if $f \geq 0$ on $D$, then $\iint_D f \, dA \geq 0$.
>
> This follows directly from the definition: for any partition $\mathcal{T}$ and sample points $(\xi_i, \eta_i) \in D_i$:
>
> $$
> \sum_{i=1}^{N} f(\xi_i, \eta_i) |D_i| \geq 0
> $$
>
> since each $f(\xi_i, \eta_i) \geq 0$ and $|D_i| \geq 0$.
>
> Taking the limit as $\|\mathcal{T}\| \to 0$ preserves the inequality.
>
> For the general case: if $f \leq g$, then $g - f \geq 0$, so $\iint_D (g - f) \, dA \geq 0$, which gives $\iint_D g \, dA \geq \iint_D f \, dA$.

^pf-22-4

*Uses:* [[§21 The Definition of the Integral#^rem-21-6|§21 Rem. (Evaluating the Integral)]], [[§22 Properties of the Integral#^thm-22-1|§22.1]], [[§22 Properties of the Integral#^thm-22-2|§22.2]]

> [!remark]- Connections
> - 1D version: [[§33 Properties of the Riemann Integral#^thm-33-3|Monotonicity of the Integral]] (451 §33.3).
> - Computational version: [[§116 Double Integrals Over General Regions#^thm-116-3|Calc Thm. §116.3]] (linearity and comparison).

> [!theorem] Corollary §22.5: Absolute Value Inequality
> If $f$ is integrable on $D$, then $|f|$ is integrable and:
>
> $$
> \left| \iint_D f \, dA \right| \leq \iint_D |f| \, dA.
> $$

^cor-22-5

> [!proof]+ Proof
> First, $|f|$ is integrable: since $\big||f(p)| - |f(q)|\big| \leq |f(p) - f(q)|$, on each piece $D_i$ of a partition the oscillation of $|f|$ is at most that of $f$, so, by [[§21 The Definition of the Integral#^def-21-6|Def. §21.6]], $\sum_i (\sup_{D_i}|f| - \inf_{D_i}|f|)|D_i| \leq \sum_i (M_i - m_i)|D_i| \to 0$ (as in the one-dimensional case, [[§33 Properties of the Riemann Integral#^thm-33-4|451 §33.4]]).
>
> Since $-|f| \leq f \leq |f|$, by the [[§22 Properties of the Integral#^thm-22-4|comparison theorem]]:
>
> $$
> -\iint_D |f| \, dA \leq \iint_D f \, dA \leq \iint_D |f| \, dA.
> $$

^pf-22-5

*Uses:* [[§22 Properties of the Integral#^thm-22-4|§22.4]], [[§21 The Definition of the Integral#^def-21-6|Def. §21.6]], [[§33 Properties of the Riemann Integral#^thm-33-4|451 §33.4]]

> [!remark]- Connections
> - 1D version: [[§33 Properties of the Riemann Integral#^thm-33-4|Absolute Values]] (451 §33.4), whose oscillation argument for the integrability of $|f|$ the proof here repeats.

### Iterated Integrals: The Simple Case

Consider the simple case where $D = [a, b] \times [c, d]$ is a rectangle.

Suppose $f$ is integrable on $D$. Partition:
- $[a, b]$ into $N$ pieces of width $h = \frac{b-a}{N}$
- $[c, d]$ into $M$ pieces of width $k = \frac{d-c}{M}$

This gives $N \times M$ small rectangles $D_{ij} = [a + (i-1)h, a + ih] \times [c + (j-1)k, c + jk]$.

The Riemann sum is:

$$
\sum_{i=1}^{N} \sum_{j=1}^{M} f(a + (i-1)h + \theta h, c + (j-1)k + \lambda k) \cdot hk
$$

for some $\theta, \lambda \in [0, 1]$ (or we can choose any sample point in $D_{ij}$).

Taking $h, k \to 0$ (i.e., $N, M \to \infty$):

$$
\iint_D f(x, y) \, dA = \int_a^b \int_c^d f(x, y) \, dy \, dx = \int_c^d \int_a^b f(x, y) \, dx \, dy.
$$

### Change of Variables: Polar Coordinates

> [!theorem] Theorem §22.6: Change of Variables to Polar Coordinates
> Let $D^* = \{(r, \theta) : a \leq r \leq b, \alpha \leq \theta \leq \beta\}$, with $0 \leq a < b$ and $\alpha < \beta \leq \alpha + 2\pi$, be a region in polar coordinates, and let $D \subseteq \mathbb{R}^2$ be its image under the transformation $x = r\cos\theta$, $y = r\sin\theta$.
>
> If $f$ is continuous on $D$, then:
>
> $$
> \iint_D f(x, y) \, dx\, dy = \int_\alpha^\beta \int_a^b f(r\cos\theta, r\sin\theta) \cdot r \, dr \, d\theta.
> $$
>
> The factor $r$ is the absolute value of the Jacobian ([[§16 The Inverse Function Theorem#^ex-16-4|Ex. §16.4]]): $\left| \dfrac{\partial(x, y)}{\partial(r, \theta)} \right| = r$.

^thm-22-6

> [!proof]+ Proof
> We prove this directly from the definition of the integral by computing areas of polar rectangles.
>
> **Step 1: Partition the polar region.**
>
> Partition:
> - $[a, b]$ into $M$ pieces of width $k = \frac{b-a}{M}$: radii $r_i = a + ik$ for $i = 0, 1, \ldots, M$.
> - $[\alpha, \beta]$ into $N$ pieces of width $h = \frac{\beta - \alpha}{N}$: angles $\theta_j = \alpha + jh$ for $j = 0, 1, \ldots, N$.
>
> This gives $M \times N$ polar rectangles $D_{ij}^*$ with:
> - Inner radius: $r_{i-1} = a + (i-1)k$
> - Outer radius: $r_i = a + ik$
> - Angular span: from $\theta_{j-1} = \alpha + (j-1)h$ to $\theta_j = \alpha + jh$
>
> **Step 2: Compute the area of each polar rectangle.**
>
> The area of a circular sector with radii $r_1$ to $r_2$ and angle $\Delta\theta$ is:
>
> $$
> \text{Area} = \frac{\Delta\theta}{2\pi} \cdot \pi r_2^2 - \frac{\Delta\theta}{2\pi} \cdot \pi r_1^2 = \frac{\Delta\theta}{2}(r_2^2 - r_1^2).
> $$
>
> For the $(i, j)$-th polar rectangle with $r_1 = a + (i-1)k$, $r_2 = a + ik$, $\Delta\theta = h$:
>
> $$
> |D_{ij}| = \frac{h}{2}\left( (a + ik)^2 - (a + (i-1)k)^2 \right).
> $$
>
> **Step 3: Expand the area formula.**
>
> $$
> \begin{aligned}
> (a + ik)^2 - (a + (i-1)k)^2 &= \left[ a^2 + 2aik + i^2k^2 \right] - \left[ a^2 + 2a(i-1)k + (i-1)^2k^2 \right] \\
> &= 2ak + \left( i^2 - (i-1)^2 \right) k^2 \\
> &= 2ak + (2i - 1)k^2.
> \end{aligned}
> $$
>
> Therefore:
>
> $$
> |D_{ij}| = \frac{h}{2}\left( 2ak + (2i-1)k^2 \right) = hk \left( a + \frac{(2i-1)k}{2} \right) = hk \cdot \bar{r}_i
> $$
>
> where $\bar{r}_i = a + (i - \frac{1}{2})k$ is the midpoint radius of the $i$-th annular strip.
>
> **Step 4: Form the Riemann sum.**
>
> Choose sample points in polar coordinates: $(\bar{r}_i, \bar{\theta}_j)$ where $\bar{r}_i = a + (i - \frac{1}{2})k$ and $\bar{\theta}_j = \alpha + (j - \frac{1}{2})h$.
>
> In Cartesian coordinates, these are:
>
> $$
> (x_{ij}, y_{ij}) = (\bar{r}_i \cos\bar{\theta}_j, \bar{r}_i \sin\bar{\theta}_j).
> $$
>
> The Riemann sum for $\iint_D f(x, y) \, dA$ is:
>
> $$
> \sum_{i=1}^{M} \sum_{j=1}^{N} f(x_{ij}, y_{ij}) \cdot |D_{ij}| = \sum_{i=1}^{M} \sum_{j=1}^{N} f(\bar{r}_i \cos\bar{\theta}_j, \bar{r}_i \sin\bar{\theta}_j) \cdot \bar{r}_i \cdot hk.
> $$
>
> **Step 5: Recognize as a Riemann sum in $(r, \theta)$.**
>
> Define $g(r, \theta) = f(r\cos\theta, r\sin\theta) \cdot r$. Then:
>
> $$
> \sum_{i=1}^{M} \sum_{j=1}^{N} f(\bar{r}_i \cos\bar{\theta}_j, \bar{r}_i \sin\bar{\theta}_j) \cdot \bar{r}_i \cdot hk = \sum_{i=1}^{M} \sum_{j=1}^{N} g(\bar{r}_i, \bar{\theta}_j) \cdot hk.
> $$
>
> This is exactly a Riemann sum for $\iint_{D^*} g(r, \theta) \, dr\, d\theta$ over the rectangle $[a, b] \times [\alpha, \beta]$.
>
> **Step 6: Take the limit.**
>
> As $M, N \to \infty$ (i.e., $h, k \to 0$):
>
> $$
> \iint_D f(x, y) \, dx\, dy = \lim_{M, N \to \infty} \sum_{i=1}^{M} \sum_{j=1}^{N} g(\bar{r}_i, \bar{\theta}_j) \cdot hk = \iint_{D^*} g(r, \theta) \, dr\, d\theta.
> $$
>
> By [[Fubini's Theorem|Fubini's theorem]] on the rectangle $[a, b] \times [\alpha, \beta]$:
>
> $$
> \iint_D f(x, y) \, dx\, dy = \int_\alpha^\beta \int_a^b f(r\cos\theta, r\sin\theta) \cdot r \, dr \, d\theta.
> $$

^pf-22-6

*Uses:* [[§21 The Definition of the Integral#^def-21-7|Def. §21.7]], [[§21 The Definition of the Integral#^rem-21-6|§21 Rem. (Evaluating the Integral)]], [[Fubini's Theorem|§23.1]]

> [!remark]- Connections
> - Special case of the general [[§24 The Change of Variables Formula#^thm-24-2|Change of Variables Formula]] (§24.2, §15.17), revisited in [[§25 Change of Variables on General Domains#^ex-25-1|Ex. §25.1]].
> - In forms language the factor $r$ is the pullback $dx \wedge dy = r\,dr \wedge d\theta$: [[§37 The Algebra of Differential Forms#^ex-37-4|Ex. §37.4]].
> - Computational version: [[§117 Double Integrals in Polar Coordinates#^thm-117-1|Calc Thm. §117.1]] (with worked examples); with f ≡ 1 it gives the area of a polar region, [[§76 Calculus in Polar Coordinates#^thm-76-2|Calc Thm. §76.2]].

> [!remark] Remark: The Jacobian
> The factor $r$ appearing in the integrand is the **Jacobian** ([[§16 The Inverse Function Theorem#^def-16-1|Def. §16.1]]) of the polar coordinate transformation:
>
> $$
> x = r\cos\theta, \quad y = r\sin\theta.
> $$
>
> $$
> J = \frac{\partial(x, y)}{\partial(r, \theta)} = \det \begin{pmatrix} \dfrac{\partial x}{\partial r} & \dfrac{\partial x}{\partial \theta} \\[8pt] \dfrac{\partial y}{\partial r} & \dfrac{\partial y}{\partial \theta} \end{pmatrix} = \det \begin{pmatrix} \cos\theta & -r\sin\theta \\ \sin\theta & r\cos\theta \end{pmatrix} = r\cos^2\theta + r\sin^2\theta = r.
> $$
>
> The proof above shows *why* the Jacobian appears: it measures how the transformation distorts area. A small rectangle $dr \times d\theta$ in polar coordinates maps to a region of area approximately $r \cdot dr \cdot d\theta$ in Cartesian coordinates.

^rem-22-9

![[m452-15-4.svg]]
*The Jacobian of the polar map $\Phi(r,\theta) = (r\cos\theta, r\sin\theta)$. Top: two equal cells $dr \times d\theta$ in the $(r,\theta)$ plane, one at small $r$ (green) and one at large $r$ (red). Their images are annular cells, and the outer image is wider, because arc length is $r\,d\theta$. Bottom: zoomed in, the red image cell is nearly the rectangle spanned by $\boldsymbol{\Phi}_r\,dr$ and $\boldsymbol{\Phi}_\theta\,d\theta$ (drawn to scale). Its sides are orthogonal, with lengths $dr$ and $r_0\,d\theta$, so its area is $r_0\,dr\,d\theta$ and $|J| = r_0$. The factor $r$ in every polar integral is literally the width of the cell. At $r = 0$ the tangential side collapses, $J = 0$, and $\Phi$ is not invertible there (all $\theta$ give the same point): the hypothesis of the [[Inverse Function Theorem (several variables)|Inverse Function Theorem]] fails exactly where polar coordinates fail.*

*Continued in [[§23 Fubini's Theorem]]: Fubini's theorem on rectangles and on Type I and Type II regions.*
