---
type: section
subject: "[[Measure Theory]]"
chapter: 5
section: 18
tags: [measure-theory, math551]
---
← [[§18a Lebesgue's Differentiation Theorem]] · ↑ [[· 5 Differentiation and the FTC]] · [[§18c Absolute Continuity]] →

This section answers [[§18 Differentiation Theory#^rem-18-1|the central question]] of the chapter: for $f \in L$, the integral function $F(x) = \int_a^x f$ satisfies $F' = f$ a.e. The averaging argument needs the measurability of $(x, t) \mapsto f(x + t)$, which comes from measurability under continuous and linear maps.

## Measurability Under Continuous and Linear Maps

> [!theorem] Theorem §18.20: Continuous Maps Preserve Bounded Closed Sets
> Let $T: \mathbb{R}^n \to \mathbb{R}^n$ be a continuous map. Then for every bounded closed set $F \subseteq \mathbb{R}^n$, the image $T(F)$ is bounded and closed.

^thm-18-20

> [!proof]+ Proof
> Since $F$ is bounded and closed in $\mathbb{R}^n$, $F$ is compact ([[§6 Open Covers and the Heine–Borel Theorem#^thm-6-4|Heine–Borel]]). Since $T$ is continuous, $T(F)$ is compact ([[Continuous Image of a Compact Space is Compact]]). Since $\mathbb{R}^n$ is a metric space, compact subsets are bounded and closed ([[Heine–Borel Theorem]]).

^pf-18-20

*Uses:* [[§6 Open Covers and the Heine–Borel Theorem#^thm-6-4|§6.4]], [[Continuous Image of a Compact Space is Compact|590 §15.3]], [[Heine–Borel Theorem|590 §15.12]]

> [!theorem] Theorem §18.21: Continuous Maps Preserving Null Sets Preserve Measurability
> Let $T: \mathbb{R}^n \to \mathbb{R}^n$ be a continuous map. Assume $T$ maps measure-zero sets to measure-zero sets: $m^*(Z) = 0 \implies m^*(T(Z)) = 0$. Then for every $E \in \mathcal{M}(\mathbb{R}^n)$, we have $T(E) \in \mathcal{M}(\mathbb{R}^n)$.

^thm-18-21

> [!proof]+ Proof
> Write $E = \bigcup_{m=1}^{\infty} F_m \cup Z$, where each $F_m$ is bounded and closed with $m(F_m) < \infty$, and $m(Z) = 0$ ([[Inner Regularity of Lebesgue Measure|§11.10]], as in the proof of [[§17a Applications of Tonelli's Theorem#^thm-17-8|§17.8]]). Then $T(E) = \bigcup_{m=1}^{\infty} T(F_m) \cup T(Z)$. By [[§18b Differentiating the Integral#^thm-18-20|the previous theorem]], each $T(F_m)$ is bounded and closed, hence [[§11 Borel Sets and Measure Spaces#^cor-11-7|measurable]]. By hypothesis, $m^*(T(Z)) = 0$, so $T(Z)$ is [[§10 Lebesgue Measurable Sets#^ex-10-1|measurable]]. A countable union of measurable sets is measurable, so $T(E) \in \mathcal{M}(\mathbb{R}^n)$.

^pf-18-21

*Uses:* [[Inner Regularity of Lebesgue Measure|§11.10]], [[§18b Differentiating the Integral#^thm-18-20|§18.20]], [[§11 Borel Sets and Measure Spaces#^cor-11-7|§11.7]], [[§10 Lebesgue Measurable Sets#^ex-10-1|Ex. §10.1]], [[Lebesgue Measurable Sets Form a σ-Algebra|§10.3]]

> [!remark]- Connections
> - MATH 452 analogue for Jordan content: [[§15 Multivariable Integration#^prop-15-16|C¹ Diffeomorphisms Preserve Jordan Measurability]] (452 §15.16).
> - Applied to AC functions via [[§18d The Fundamental Theorem of Calculus for Lebesgue Integrals#^thm-18-19|§18.19]] (for $n = 1$) and to linear maps via [[§18b Differentiating the Integral#^thm-18-22|§18.22]].

> [!theorem] Theorem §18.22: Linear Maps Preserve Null Sets
> Let $T: \mathbb{R}^n \to \mathbb{R}^n$ be a linear map. Then $m^*(Z) = 0 \implies m^*(T(Z)) = 0$.

^thm-18-22

> [!proof]+ Proof
> **Case 1: $T$ is not invertible.** Then $\det T = 0$ ([[Invertible ⟺ nonzero determinant|LADR 9.50]]), so $T(\mathbb{R}^n)$ is a proper linear subspace of $\mathbb{R}^n$ (dimension $< n$). A $k$-dimensional subspace of $\mathbb{R}^n$ with $k < n$ has $n$-dimensional Lebesgue measure zero (it is contained in a countable union of “flat” rectangles with one side of length $0$). Since $T(Z) \subseteq T(\mathbb{R}^n)$, we have $m^{\ast}(T(Z)) = 0$.
>
> **Case 2: $T$ is invertible.** We show $m(T(R)) = |\!\det T|\,m(R)$ for any rectangle $R$, then use L-coverings.
>
> *Measure of parallelotopes.* Factor $T$ into elementary row operations (which generate all invertible linear maps: [[§12 The Inverse of a Matrix#^thm-12-8|235 Thm. §12.8]]): scaling one coordinate by $c$ multiplies volume by $|c|$ and determinant by $c$; adding a multiple of one coordinate to another is a shear with determinant $1$ that preserves volume (by [[Fubini's Theorem (Lebesgue)|Fubini]]: the cross-sectional area at each height is unchanged); swapping two coordinates has determinant $-1$ and preserves volume. Since both $m(T(\cdot))$ and $|\!\det T|\,m(\cdot)$ are multiplicative under composition ([[§34 Determinants#^ladr-9-49|LADR 9.49]]), $m(T(R)) = |\!\det T|\,m(R)$. (Here the composition step needs the volume formula for images of general sets, not only of rectangles, since after the first factor the image of $R$ is no longer a rectangle. What the null-set argument below actually uses is $m^{\ast}(E(A)) \leq |\!\det E|\,m^{\ast}(A)$ for each elementary map $E$ and every $A \subseteq \mathbb{R}^n$: for scalings and swaps this holds because $E$ maps L-coverings to L-coverings, scaling each volume by $|\!\det E|$, and for a shear one applies the cross-section argument to an open $G \supseteq A$ with $m(G) \leq m^{\ast}(A) + \varepsilon$, whose image $E(G)$ is open with the same cross-sectional measures. Composing gives $m^{\ast}(T(A)) \leq |\!\det T|\,m^{\ast}(A)$; the equality for all measurable sets is [[§34 Determinants#^ladr-9-61|LADR 9.61]].)
>
> *Null sets.* For any $\varepsilon > 0$, choose an [[§9 Lebesgue Outer Measure#^def-9-3|L-covering]] $\{R_j\}_{j=1}^{\infty}$ of $Z$ with $\sum m(R_j) < \varepsilon$. Then $\{T(R_j)\}$ covers $T(Z)$, so by [[Properties of Lebesgue Outer Measure|subadditivity]]:
>
> $$
> m^*(T(Z)) \leq \sum_{j=1}^{\infty} m(T(R_j)) = |\!\det T| \sum_{j=1}^{\infty} m(R_j) < |\!\det T|\,\varepsilon.
> $$
>
> Since $\varepsilon > 0$ is arbitrary, $m^*(T(Z)) = 0$.

^pf-18-22

*Uses:* [[Invertible ⟺ nonzero determinant|LADR 9.50]], [[§9 Lebesgue Outer Measure#^def-9-4|Def. §9.4]], [[Fubini's Theorem (Lebesgue)|§17.6]], [[§34 Determinants#^ladr-9-49|LADR 9.49]], [[§9 Lebesgue Outer Measure#^def-9-3|Def. §9.3]], [[Properties of Lebesgue Outer Measure|§9.1]]

> [!remark]- Connections
> - The formula $m(T(R)) = \vert\det T\vert\, m(R)$ is [[§34 Determinants#^ladr-9-61|LADR 9.61]] (a linear map scales volume by the absolute value of its determinant), which LADR proves via singular values ([[§27 Consequences of Singular Value Decomposition#^ladr-7-111|LADR 7.111]]) rather than elementary operations.
> - In MATH 452 it is [[§15 Multivariable Integration#^prop-15-19|Determinants Measure Volume Distortion]] (452 §15.19), the linear case of the [[Change of Variables Formula (multiple integrals)]].

> [!theorem] Corollary §18.23: Composition with Invertible Linear Maps Preserves Measurability
> Let $f$ be a measurable function on $\mathbb{R}^n$ and $T: \mathbb{R}^n \to \mathbb{R}^n$ an invertible linear map. Then $f \circ T$ is measurable on $\mathbb{R}^n$.

^cor-18-23

> [!proof]+ Proof
> For any $\alpha \in \mathbb{R}$:
>
> $$
> \{x \in \mathbb{R}^n : (f \circ T)(x) > \alpha\} = (f \circ T)^{-1}((\alpha, \infty)) = T^{-1}(f^{-1}((\alpha, \infty))).
> $$
>
> Since $f$ is [[§12 Measurable Functions#^def-12-2|measurable]], $A = f^{-1}((\alpha, \infty)) \in \mathcal{M}(\mathbb{R}^n)$. Since $T^{-1}$ is an invertible linear map (hence continuous and [[§18b Differentiating the Integral#^thm-18-22|preserving null sets]]), $T^{-1}(A) \in \mathcal{M}(\mathbb{R}^n)$ by [[§18b Differentiating the Integral#^thm-18-21|the theorem above]]. So $f \circ T$ is measurable.

^pf-18-23

*Uses:* [[§12 Measurable Functions#^def-12-2|Def. §12.2]], [[§18b Differentiating the Integral#^thm-18-22|§18.22]], [[§18b Differentiating the Integral#^thm-18-21|§18.21]]

> [!theorem] Proposition §18.24: Measurability of $f(x + t)$ on $\mathbb{R}^2$
> If $f$ is a measurable function on $\mathbb{R}$, then $(x, t) \mapsto f(x + t)$ is a measurable function on $\mathbb{R}^2$.

^prop-18-24

> [!proof]+ Proof
> Define $F: \mathbb{R}^2 \to \mathbb{R}$ by $F(x, y) = f(x)$. Then $F$ is measurable on $\mathbb{R}^2$: for each $\alpha$, $\{(x,y) : F(x,y) > \alpha\} = \{x : f(x) > \alpha\} \times \mathbb{R}$, which is measurable ([[§17a Applications of Tonelli's Theorem#^thm-17-8|product of a measurable set with ℝ]]).
>
> Define the invertible linear map $T: \mathbb{R}^2 \to \mathbb{R}^2$ by $T(x, t) = (x + t,\; x - t)$, so $T^{-1}(u, v) = ((u+v)/2,\; (u-v)/2)$. Then:
>
> $$
> F(T(x, t)) = F(x + t,\; x - t) = f(x + t).
> $$
>
> By [[§18b Differentiating the Integral#^cor-18-23|the corollary above]], $F \circ T$ is measurable on $\mathbb{R}^2$.

^pf-18-24

*Uses:* [[§12 Measurable Functions#^def-12-2|Def. §12.2]], [[§17a Applications of Tonelli's Theorem#^thm-17-8|§17.8]], [[§18b Differentiating the Integral#^cor-18-23|§18.23]]

## Differentiating the Integral: $F'(x) = f(x)$ A.E.

The other direction of the FTC asks: if we *start* with an integrable function and form its integral, can we recover it by differentiating?

> [!theorem] Lemma §18.25: Averaging Lemma
> Let $f \in L(\mathbb{R})$. Define the **average function**:
>
> $$
> F_h(x) = \frac{1}{h}\int_0^h f(x + t)\,dt \qquad (h > 0).
> $$
>
> Then $\lim_{h \to 0} \int_{\mathbb{R}} |F_h(x) - f(x)|\,dx = 0$, i.e., $F_h \to f$ in $L^1(\mathbb{R})$.

^lem-18-25

> [!proof]+ Proof
> *$F_h \in L^1(\mathbb{R})$*: By the triangle inequality and [[Tonelli's Theorem|Tonelli]] (swapping the order of integration):
>
> $$
> \int_{\mathbb{R}} |F_h(x)|\,dx \leq \frac{1}{h}\int_0^h \int_{\mathbb{R}} |f(x+t)|\,dx\,dt = \frac{1}{h}\int_0^h \|f\|_1\,dt = \|f\|_1 < \infty,
> $$
>
> where we used [[§17 Invariance Properties and Fubini's Theorem#^thm-17-1|translation invariance]] ($\int |f(x+t)|\,dx = \int |f(x)|\,dx = \|f\|_1$). So $F_h \in L^1(\mathbb{R})$.
>
> *$\|F_h - f\|_1 \to 0$*: Note:
>
> $$
> F_h(x) - f(x) = \frac{1}{h}\int_0^h f(x+t)\,dt - f(x) = \frac{1}{h}\int_0^h \bigl(f(x+t) - f(x)\bigr)\,dt.
> $$
>
> Therefore:
>
> $$
> \int_{\mathbb{R}} |F_h(x) - f(x)|\,dx \leq \frac{1}{h}\int_0^h \int_{\mathbb{R}} |f(x+t) - f(x)|\,dx\,dt,
> $$
>
> where we used the triangle inequality under the integral and swapped the order of integration (justified by Tonelli, since $g(x,t) = |f(x+t) - f(x)|$ is measurable on $\mathbb{R}^2$).
>
> *Measurability of $g$*: By [[§18b Differentiating the Integral#^prop-18-24|the proposition above]], $(x, t) \mapsto f(x+t)$ is measurable on $\mathbb{R}^2$. Since $f(x)$ is also measurable on $\mathbb{R}^2$ (constant in $t$), $g(x, t) = |f(x+t) - f(x)|$ is [[§12 Measurable Functions#^thm-12-3|measurable]].
>
> By the [[§17 Invariance Properties and Fubini's Theorem#^thm-17-2|average continuity theorem]] ([[§17 Invariance Properties and Fubini's Theorem|§17]]), for every $\varepsilon > 0$ there exists $\delta > 0$ such that $|t| < \delta$ implies $\int_{\mathbb{R}} |f(x+t) - f(x)|\,dx < \varepsilon$. So for $0 < h < \delta$:
>
> $$
> \int_{\mathbb{R}} |F_h(x) - f(x)|\,dx \leq \frac{1}{h}\int_0^h \varepsilon\,dt = \varepsilon.
> $$

^pf-18-25

*Uses:* [[Tonelli's Theorem|§17.3]], [[§15 The General Lebesgue Integral#^prop-15-3|§15.3]], [[§17 Invariance Properties and Fubini's Theorem#^thm-17-1|§17.1]], [[§16 The L¹ Space and Density Theorems#^def-16-1|Def. §16.1]], [[§18b Differentiating the Integral#^prop-18-24|§18.24]], [[§12 Measurable Functions#^thm-12-3|§12.3]], [[§17 Invariance Properties and Fubini's Theorem#^thm-17-2|§17.2]]

> [!theorem] Theorem §18.26: Differentiation of the Integral
> Let $f \in L(\mathbb{R})$. Define $F(x) = \int_a^x f(t)\,dt$. Then $F$ is differentiable a.e. and $F'(x) = f(x)$ a.e.

^thm-18-26

> [!proof]+ Proof
> By the [[§18b Differentiating the Integral#^lem-18-25|Averaging Lemma]], $F_h \to f$ in $L^1$ as $h \to 0$. In particular, there exists a sequence $h_n \to 0$ such that $F_{h_n} \to f$ pointwise a.e. (every $L^1$-convergent sequence has a pointwise a.e. convergent subsequence; [[§19a Lᵖ as a Banach Space#^cor-19-17|§19.17]]).
>
> But:
>
> $$
> F_{h_n}(x) = \frac{1}{h_n}\int_0^{h_n} f(x+t)\,dt = \frac{1}{h_n}\int_x^{x+h_n} f(t)\,dt = \frac{F(x + h_n) - F(x)}{h_n}.
> $$
>
> So $\frac{F(x+h_n) - F(x)}{h_n} \to f(x)$ a.e. along the sequence $\{h_n\}$.
>
> To promote this to a full derivative (limit as $h \to 0$, not just along a sequence): we already know $F \in BV([a,b])$ (by the [[§18 Differentiation Theory#^thm-18-8|Total Variation Theorem]]), hence $F$ is differentiable a.e. (by [[Lebesgue's Differentiation Theorem for Monotone Functions|Lebesgue's theorem]]; [[§18a Lebesgue's Differentiation Theorem#^cor-18-10|§18.10]]). Where $F'(x)$ exists, it must equal $f(x)$ (since the subsequential limit $f(x)$ is the only possible limit). Therefore $F'(x) = f(x)$ a.e.

^pf-18-26

*Uses:* [[§18b Differentiating the Integral#^lem-18-25|§18.25]], [[§19a Lᵖ as a Banach Space#^cor-19-17|§19.17]], [[§18 Differentiation Theory#^thm-18-8|§18.8]], [[Lebesgue's Differentiation Theorem for Monotone Functions|§18.9]], [[§18a Lebesgue's Differentiation Theorem#^cor-18-10|§18.10]]

> [!remark]- Connections
> - MATH 451 counterpart: FTC II ([[§34 Fundamental Theorem of Calculus#^thm-34-4|451 §34.4]]) gives $F'(x_0) = f(x_0)$ at every point where $f$ is continuous; here continuity is dropped at the cost of “a.e.”.
> - Completes the proof of [[Fundamental Theorem of Calculus for Lebesgue Integrals|the FTC for Lebesgue integrals]] ([[§18d The Fundamental Theorem of Calculus for Lebesgue Integrals#^thm-18-13|§18.13]]).

> [!definition] Definition §18.5: Lebesgue Point
> Let $f \in L(\mathbb{R})$ and define $F(x) = \int_a^x f(t)\,dt$. A point $x_0$ is called a **Lebesgue point** of $f$ if $F'(x_0)$ exists and $F'(x_0) = f(x_0)$, i.e.:
>
> $$
> \lim_{h \to 0} \frac{1}{h}\int_0^h f(x_0 + t)\,dt = f(x_0).
> $$
>
> [[§18b Differentiating the Integral#^thm-18-26|The theorem above]] shows that a.e. point is a Lebesgue point of $f$. (This is weaker than the standard notion of a Lebesgue point, which asks that $\lim_{h \to 0} \frac{1}{2h}\int_{-h}^{h} |f(x_0 + t) - f(x_0)|\,dt = 0$; that stronger property also holds at a.e. point, but it is not needed here.)

^def-18-5

![[m551-18-7.svg]]
*Averages over shrinking windows. With $F_h(x_0) = \frac1h\int_0^h f(x_0 + t)\,dt$ as in the [[§18b Differentiating the Integral#^lem-18-25|Averaging Lemma]], the average height of $f$ (blue) over $[x_0, x_0 + h]$ is the dashed level, and over the shorter window $[x_0, x_0 + h']$ it is the red one. Each average is a difference quotient of the integral function, so $x_0$ is a Lebesgue point exactly when these averages tend to $f(x_0)$ as the window shrinks; by [[§18b Differentiating the Integral#^thm-18-26|Theorem §18.26]] this happens at a.e. $x_0$.*
