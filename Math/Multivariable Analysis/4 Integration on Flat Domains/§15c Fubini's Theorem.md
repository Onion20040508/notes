---
type: section
subject: "[[Multivariable Analysis]]"
chapter: 4
section: "15c"
tags: [multivariable-analysis, math452]
---
← [[§15 Multivariable Integration]] · ↑ [[· 4 Integration on Flat Domains]] · [[§15d The Change of Variables Formula]] →

## Fubini's Theorem: Rigorous Treatment

Fubini's theorem allows us to compute double integrals as iterated single integrals and to change the order of integration. We develop this carefully.

> [!theorem] Theorem §15.8: Fubini's Theorem — Rectangle Case
> Let $f: [a, b] \times [c, d] \to \mathbb{R}$ be continuous. Then:
>
> $$
> \iint_{[a,b] \times [c,d]} f(x, y) \, dA = \int_a^b \left( \int_c^d f(x, y) \, dy \right) dx = \int_c^d \left( \int_a^b f(x, y) \, dx \right) dy.
> $$

^thm-15-8

> [!proof]+ Proof
> We prove the first equality; the second follows by symmetry.
>
> **Step 1: Setup the partitions.**
>
> Partition $[a, b]$ into $N$ equal subintervals of width $h = \frac{b-a}{N}$:
>
> $$
> a = x_0 < x_1 < \cdots < x_N = b, \quad x_i = a + ih.
> $$
>
> Partition $[c, d]$ into $M$ equal subintervals of width $k = \frac{d-c}{M}$:
>
> $$
> c = y_0 < y_1 < \cdots < y_M = d, \quad y_j = c + jk.
> $$
>
> This gives $N \times M$ small rectangles $R_{ij} = [x_{i-1}, x_i] \times [y_{j-1}, y_j]$, each with area $hk$.
>
> **Step 2: Riemann sum for the double integral.**
>
> Choose sample points $(\xi_i, \eta_j) \in R_{ij}$. The Riemann sum is:
>
> $$
> S_{N,M} = \sum_{i=1}^{N} \sum_{j=1}^{M} f(\xi_i, \eta_j) \cdot hk.
> $$
>
> As $N, M \to \infty$ (equivalently, $h, k \to 0$):
>
> $$
> S_{N,M} \to \iint_{[a,b] \times [c,d]} f(x, y) \, dA.
> $$
>
> **Step 3: Riemann sum for the iterated integral.**
>
> For the iterated integral, first fix $x = \xi_i$ and consider the inner integral:
>
> $$
> F(x) = \int_c^d f(x, y) \, dy.
> $$
>
> The [[§32 The Definition of the Riemann Integral#^def-32-new4|Riemann sum]] for $F(\xi_i)$ is:
>
> $$
> \sum_{j=1}^{M} f(\xi_i, \eta_j) \cdot k \approx F(\xi_i) = \int_c^d f(\xi_i, y) \, dy.
> $$
>
> Then the Riemann sum for the outer integral $\int_a^b F(x) \, dx$ is:
>
> $$
> \sum_{i=1}^{N} F(\xi_i) \cdot h \approx \int_a^b F(x) \, dx = \int_a^b \left( \int_c^d f(x, y) \, dy \right) dx.
> $$
>
> **Step 4: Connect the two.**
>
> Observe that:
>
> $$
> \sum_{i=1}^{N} \left( \sum_{j=1}^{M} f(\xi_i, \eta_j) \cdot k \right) h = \sum_{i=1}^{N} \sum_{j=1}^{M} f(\xi_i, \eta_j) \cdot hk = S_{N,M}.
> $$
>
> So the Riemann sum for the double integral equals the iterated Riemann sum.
>
> **Step 5: Take the limit.**
>
> Since $f$ is continuous on the compact set $[a,b] \times [c,d]$ ([[Heine–Borel Theorem|Heine–Borel]]), it is [[§15 Compact Spaces#^rem-15-1|uniformly continuous]]. This ensures:
> - The inner integral $F(x) = \int_c^d f(x, y) \, dy$ exists for each $x$ ([[§32 The Definition of the Riemann Integral#^thm-32-7|451 §32.7]]) and is continuous in $x$.
> - The Riemann sums converge uniformly.
>
> Indeed, given $\varepsilon > 0$, choose $\delta > 0$ with $|f(p) - f(q)| < \varepsilon$ whenever $\|p - q\| < \delta$. If $h, k < \delta$, then for every $x \in [a, b]$, $\big|\sum_{j} f(x, \eta_j)\, k - F(x)\big| \leq \sum_j \int_{y_{j-1}}^{y_j} |f(x, \eta_j) - f(x, y)| \, dy \leq \varepsilon (d - c)$, uniformly in $x$; hence $\big|S_{N,M} - \sum_i F(\xi_i)\, h\big| \leq \varepsilon (d - c)(b - a)$. Likewise $|F(x) - F(x')| \leq \varepsilon (d - c)$ for $|x - x'| < \delta$, so $F$ is continuous and $\sum_i F(\xi_i)\, h \to \int_a^b F(x)\, dx$.
>
> Taking $N, M \to \infty$:
>
> $$
> \iint_{[a,b] \times [c,d]} f(x, y) \, dA = \lim_{N,M \to \infty} S_{N,M} = \int_a^b \left( \int_c^d f(x, y) \, dy \right) dx.
> $$

^pf-15-8

*Uses:* [[§15 Multivariable Integration#^def-15-11|Def. §15.11]], [[§15a The Definition of the Integral#^rem-15-6|§15a Rem. (Evaluating the Integral)]], [[§32 The Definition of the Riemann Integral#^def-32-new5|451 Def. §32.3]], [[§32 The Definition of the Riemann Integral#^thm-32-7|451 §32.7]], [[Heine–Borel Theorem|590 §15.12]], [[§15 Compact Spaces#^rem-15-1|590 §15 Rem. (uniform continuity on compact sets)]]

![[m452-15-2.svg]]
*Fubini's theorem geometrically: freeze $x$ and integrate over $y$ to get the cross-sectional area $A(x)$ (red slab); then integrate $A(x)$ over $x$ to stack the slabs into the volume. The iterated integral $\int\!\!\int f\,dy\,dx$ is this two-stage process; Fubini says it equals the double integral whenever $f$ is integrable.*

> [!remark]- Connections
> - Makes rigorous the simple-case computation ([[§15b Properties of the Integral#Iterated Integrals: The Simple Case|“Iterated Integrals: The Simple Case”]]) above; extended to curved regions in [[§15 Multivariable Integration#^thm-15-9|Theorem §15.9]].
> - Its Type I/II form plus the [[Fundamental Theorem of Calculus]] in the inner variable proves [[Green's Theorem|Green's Theorem]] (§16.1), and one dimension up the [[Divergence Theorem in ℝⁿ|Divergence Theorem in ℝⁿ]] (§17.1).
> - Lebesgue version, for every integrable $f$ on $\mathbb{R}^p \times \mathbb{R}^q$ with no continuity assumption: [[§17 Invariance Properties and Fubini's Theorem#^thm-17-6|551 Thm. §17.6]].
> - Used in Relativity: the total-derivative terms in the variation of a field action are integrated first over their own variable — [[§B4.1 The Klein–Gordon Equation#^thm-b4-1-2|REL Theorem §B4.1.2]].
> - Computational version: [[§98 Double Integrals Over Rectangles#^thm-98-3|Calc Thm. §98.3]] (with worked examples).

> [!remark] Remark: Why Continuity Matters
> The key point is that $F(x) = \int_c^d f(x, y) \, dy$ must be well-defined and integrable. Continuity of $f$ guarantees this.
>
> More generally, Fubini's theorem holds if $f$ is **integrable** and the iterated integrals exist. For a bounded integrable $f$ on a bounded domain, $\iint_D |f| \, dA < \infty$ holds automatically; the condition $\iint_D |f| \, dA < \infty$ (absolute integrability) matters when $f$ or $D$ is unbounded, so that the double integral is improper (or, in Lebesgue theory, MATH 551).

^rem-15-10

### Fubini's Theorem for General Regions

> [!definition] Definition §15.12: Type I Region
> A **Type I region** (vertically simple) is:
>
> $$
> D = \{(x, y) : a \leq x \leq b, \; g_1(x) \leq y \leq g_2(x)\}
> $$
>
> where $g_1, g_2: [a, b] \to \mathbb{R}$ are continuous with $g_1(x) \leq g_2(x)$.

^def-15-12

> [!definition] Definition §15.12: Type II Region
> A **Type II region** (horizontally simple) is:
>
> $$
> D = \{(x, y) : c \leq y \leq d, \; h_1(y) \leq x \leq h_2(y)\}
> $$
>
> where $h_1, h_2: [c, d] \to \mathbb{R}$ are continuous with $h_1(y) \leq h_2(y)$.

^def-15-new5


![[m452-15-6.svg]]
*Type I: $D$ lies between two graphs over $[a, b]$, so every vertical line meets it in one segment $g_1(x) \leq y \leq g_2(x)$ (red). Type II is the same with the axes swapped: every horizontal line meets it in one segment $h_1(y) \leq x \leq h_2(y)$. These segments are the domains of the inner integrals in Fubini's theorem.*

> [!remark]- Connections
> - Same regions in Stewart: [[§99 Double Integrals Over General Regions#^def-99-2|Calc Def. §99.2]] and [[§99 Double Integrals Over General Regions#^def-99-3|Calc Def. §99.3]], with iterated integrals over them in [[§99 Double Integrals Over General Regions#^thm-99-1|Calc Thm. §99.1]] and [[§99 Double Integrals Over General Regions#^thm-99-2|Calc Thm. §99.2]].

> [!theorem] Theorem §15.9: Fubini for Type I Regions
> If $D = \{(x, y) : a \leq x \leq b, \; g_1(x) \leq y \leq g_2(x)\}$ and $f$ is continuous on $D$, then:
>
> $$
> \iint_D f(x, y) \, dA = \int_a^b \left( \int_{g_1(x)}^{g_2(x)} f(x, y) \, dy \right) dx.
> $$

^thm-15-9

> [!proof]+ Proof
> We give a detailed proof that carefully controls the error from approximating the curved region with rectangles.
>
> **Setup and assumptions.**
>
> Let $D = \{(x, y) : a \leq x \leq b, \; \psi(x) \leq y \leq \varphi(x)\}$ where $\psi, \varphi: [a,b] \to \mathbb{R}$ are continuous with $\psi(x) \leq \varphi(x)$ for all $x \in [a, b]$.
>
> *Claim: $D$ is closed* ([[§2 Open and Closed Sets#^def-2-new3|Def. §2.4]]).
>
> Suppose $(x_k, y_k) \in D$ and $(x_k, y_k) \to (x_0, y_0)$ ([[§1 Sequences and Limits in ℝⁿ#^def-1-1|Def. §1.1]]). Then $x_k \to x_0$ and $y_k \to y_0$. Since $(x_k, y_k) \in D$:
>
> $$
> a \leq x_k \leq b \quad \text{and} \quad \psi(x_k) \leq y_k \leq \varphi(x_k).
> $$
>
> Taking $k \to \infty$: since $[a,b]$ is closed, $a \leq x_0 \leq b$. By continuity of $\psi$ and $\varphi$:
>
> $$
> \psi(x_0) = \lim_{k \to \infty} \psi(x_k) \leq \lim_{k \to \infty} y_k = y_0 \leq \lim_{k \to \infty} \varphi(x_k) = \varphi(x_0).
> $$
>
> Thus $(x_0, y_0) \in D$, so $D$ is closed.
>
> *Boundedness.* Since $D$ is closed and bounded (contained in $[a, b] \times [\min \psi, \max \varphi]$), $D$ is compact ([[Heine–Borel Theorem|Heine–Borel]]). Since $f$ is continuous on the compact set $D$, $f$ is bounded ([[Continuous Image of a Compact Space is Compact|continuous image of compact is compact]]): there exists $B > 0$ such that $|f(x, y)| \leq B$ for all $(x, y) \in D$.
>
> Without loss of generality, embed $D$ in a square $[0, M] \times [0, M]$ for some integer $M > 0$ (translate $D$ if necessary). Since the proof integrates $f$ over regions $D_k \supseteq D$, we extend $f$ outside $D$: set $f(x, y) := f(\bar{x}, \bar{y})$ with $\bar{x} = \min(\max(x, a), b)$ and $\bar{y} = \min(\max(y, \psi(\bar{x})), \varphi(\bar{x}))$. This extension is continuous on $[0, M]^2$ (a composition of continuous functions), agrees with $f$ on $D$, and still satisfies $|f| \leq B$. (Extending by $0$ would also keep $|f| \leq B$, but would break the continuity needed in Step 7.)
>
> **Step 1: Partition the square into a grid.**
>
> Fix $\varepsilon > 0$. We will show the difference between the double integral and the iterated integral is $< C\varepsilon$ for some constant $C$ depending only on $B$ and $M$.
>
> Choose $k \in \mathbb{N}$ large (to be determined). Partition $[0, M]$ into $M \cdot 2^k$ intervals of width $h = \frac{1}{2^k}$:
>
> $$
> 0 = t_0 < t_1 < t_2 < \cdots < t_{M \cdot 2^k} = M, \quad t_i = \frac{i}{2^k}.
> $$
>
> This creates a grid of $(M \cdot 2^k)^2$ small squares, each of side $h = \frac{1}{2^k}$ and area $h^2 = \frac{1}{4^k}$.
>
> **Step 2: Use uniform continuity to control oscillation of boundary curves.**
>
> Since $\psi$ and $\varphi$ are continuous on the compact interval $[a, b]$, they are **uniformly continuous** ([[§19 Uniform Continuity#^thm-19-1|451 §19.1]]).
>
> Thus, for our fixed $\varepsilon > 0$, there exists $\delta > 0$ such that:
>
> $$
> |x - x'| < \delta \implies |\varphi(x) - \varphi(x')| < \varepsilon \quad \text{and} \quad |\psi(x) - \psi(x')| < \varepsilon.
> $$
>
> Choose $k$ large enough that $\frac{1}{2^k} < \delta$. Then within any column of width $\frac{1}{2^k}$:
>
> $$
> \sup_{x \in [t_i, t_{i+1}]} \varphi(x) - \inf_{x \in [t_i, t_{i+1}]} \varphi(x) < \varepsilon.
> $$
>
> Similarly for $\psi$. This means: *within each column, the curves $\varphi$ and $\psi$ oscillate by less than $\varepsilon$*.
>
> **Step 3: Define approximating step functions.**
>
> For each column $[t_i, t_{i+1}]$ intersecting $[a, b]$, define:
>
> $$
> \begin{aligned}
> \varphi_k(x) &= \text{smallest grid value } \geq \sup_{x' \in [t_i, t_{i+1}]} \varphi(x') \quad \text{for } x \in [t_i, t_{i+1}] \\
> \psi_k(x) &= \text{largest grid value } \leq \inf_{x' \in [t_i, t_{i+1}]} \psi(x') \quad \text{for } x \in [t_i, t_{i+1}]
> \end{aligned}
> $$
>
> In other words:
> - $\varphi_k$ rounds $\varphi$ up to the nearest grid line (within each column, taking the sup first).
> - $\psi_k$ rounds $\psi$ down to the nearest grid line (within each column, taking the inf first).
>
> Then $\varphi_k$ and $\psi_k$ are step functions constant on each column, and:
>
> $$
> \psi_k(x) \leq \psi(x) \leq \varphi(x) \leq \varphi_k(x) \quad \text{for all } x \in [a, b].
> $$
>
> Also, define $a_k$ = largest grid point $\leq a$, and $b_k$ = smallest grid point $\geq b$.
>
> **Step 4: Define the rectangular approximation $D_k$.**
>
> Let:
>
> $$
> D_k = \{(x, y) : a_k \leq x \leq b_k, \; \psi_k(x) \leq y \leq \varphi_k(x)\}.
> $$
>
> This is a union of grid squares that contains $D$: specifically, $D \subseteq D_k$.
>
> The region $D_k$ is a “staircase” approximation to $D$, where each column consists of a stack of complete grid squares.
>
> **Step 5: Estimate the area of $D_k \setminus D$ (the error region).**
>
> The error region $D_k \setminus D$ consists of:
> 1. **Top boundary squares:** In each column $[t_i, t_{i+1}]$, the squares between $y = \varphi(x)$ and $y = \varphi_k(x)$.
>
>     Since $\sup \varphi - \inf \varphi < \varepsilon$ within the column (by uniform continuity), and $\varphi_k$ is the next grid line above $\sup \varphi$:
>
>     $$
>     \varphi_k(x) - \varphi(x) < \varepsilon + \frac{1}{2^k} < 2\varepsilon
>     $$
>
>     for $k$ large enough that $\frac{1}{2^k} < \varepsilon$.
> 2. **Bottom boundary squares:** Similarly, $\psi(x) - \psi_k(x) < 2\varepsilon$.
> 3. **Left boundary:** The strip from $x = a_k$ to $x = a$ has width $\leq \frac{1}{2^k} < \varepsilon$ and height $\leq M$.
> 4. **Right boundary:** The strip from $x = b$ to $x = b_k$ has width $\leq \frac{1}{2^k} < \varepsilon$ and height $\leq M$.
>
> Number of columns intersecting $[a, b]$: at most $(b - a) \cdot 2^k + 2 \leq M \cdot 2^k + 2$.
>
> Area contributed by top boundary squares in each column: $\leq 2\varepsilon \cdot \frac{1}{2^k}$.
>
> Total area from top boundary: $\leq 2\varepsilon \cdot \frac{1}{2^k} \cdot (M \cdot 2^k + 2) = 2\varepsilon(M + \frac{2}{2^k}) < 2\varepsilon(M + 1)$.
>
> Similarly for bottom boundary.
>
> Left/right boundary areas: each $\leq \varepsilon \cdot M$.
>
> Total:
>
> $$
> |D_k \setminus D| \leq 2\varepsilon(M+1) + 2\varepsilon(M+1) + 2\varepsilon M = \varepsilon(6M + 4).
> $$
>
> **Step 6: Compare integrals over $D$ and $D_k$.**
>
> Since $D \subseteq D_k$ ([[§15 Multivariable Integration#^thm-15-4|additivity over domains]], [[§15 Multivariable Integration#^cor-15-6|absolute value inequality]]):
>
> $$
> \left| \iint_D f \, dA - \iint_{D_k} f \, dA \right| = \left| \iint_{D_k \setminus D} f \, dA \right| \leq \iint_{D_k \setminus D} |f| \, dA \leq B \cdot |D_k \setminus D| \leq B\varepsilon(6M + 4).
> $$
>
> **Step 7: Apply Fubini for rectangles to $D_k$.**
>
> The key observation: $D_k$ is a union of grid squares, and within each column $[t_i, t_{i+1}]$, the region is a rectangle $[t_i, t_{i+1}] \times [\psi_k(x), \varphi_k(x)]$ (where $\psi_k, \varphi_k$ are constant on this column).
>
> By [[Fubini's Theorem|Fubini's theorem for rectangles]] (applied column by column):
>
> $$
> \iint_{D_k} f \, dA = \int_{a_k}^{b_k} \left( \int_{\psi_k(x)}^{\varphi_k(x)} f(x, y) \, dy \right) dx.
> $$
>
> **Step 8: Compare the iterated integrals.**
>
> We need to compare:
>
> $$
> \int_{a_k}^{b_k} \int_{\psi_k(x)}^{\varphi_k(x)} f \, dy \, dx \quad \text{vs.} \quad \int_a^b \int_{\psi(x)}^{\varphi(x)} f \, dy \, dx.
> $$
>
> For each fixed $x \in [a, b]$, since $\psi_k(x) \leq \psi(x) \leq \varphi(x) \leq \varphi_k(x)$ ([[§33 Properties of the Riemann Integral#^thm-33-5|451 §33.5]], [[§33 Properties of the Riemann Integral#^thm-33-4|451 §33.4]]):
>
> $$
> \begin{aligned}
> \left| \int_{\psi_k(x)}^{\varphi_k(x)} f \, dy - \int_{\psi(x)}^{\varphi(x)} f \, dy \right| &= \left| \int_{\psi_k(x)}^{\psi(x)} f \, dy + \int_{\varphi(x)}^{\varphi_k(x)} f \, dy \right| \\
> &\leq \int_{\psi_k(x)}^{\psi(x)} |f| \, dy + \int_{\varphi(x)}^{\varphi_k(x)} |f| \, dy \\
> &\leq B(\psi(x) - \psi_k(x)) + B(\varphi_k(x) - \varphi(x)) \\
> &\leq B \cdot 2\varepsilon + B \cdot 2\varepsilon = 4B\varepsilon.
> \end{aligned}
> $$
>
> Integrating over $x$:
>
> $$
> \left| \int_a^b \int_{\psi_k(x)}^{\varphi_k(x)} f \, dy \, dx - \int_a^b \int_{\psi(x)}^{\varphi(x)} f \, dy \, dx \right| \leq \int_a^b 4B\varepsilon \, dx = 4B\varepsilon(b - a) \leq 4BM\varepsilon.
> $$
>
> Also, the integrals over $[a_k, a]$ and $[b, b_k]$ contribute:
>
> $$
> \left| \int_{a_k}^{a} \int_{\psi_k}^{\varphi_k} f \, dy \, dx \right| \leq B \cdot M \cdot (a - a_k) \leq BM\varepsilon.
> $$
>
> Similarly for $[b, b_k]$. Total contribution from left/right strips: $\leq 2BM\varepsilon$.
>
> **Step 9: Combine all estimates.**
>
> $$
> \begin{aligned}
> &\left| \iint_D f \, dA - \int_a^b \int_{\psi(x)}^{\varphi(x)} f \, dy \, dx \right| \\
> &\leq \left| \iint_D f \, dA - \iint_{D_k} f \, dA \right| + \left| \iint_{D_k} f \, dA - \int_{a_k}^{b_k} \int_{\psi_k}^{\varphi_k} f \, dy \, dx \right| \\
> &\quad + \left| \int_{a_k}^{b_k} \int_{\psi_k}^{\varphi_k} f \, dy \, dx - \int_a^b \int_{\psi}^{\varphi} f \, dy \, dx \right| \\
> &\leq B\varepsilon(6M + 4) + 0 + (4BM\varepsilon + 2BM\varepsilon) \\
> &= B\varepsilon(6M + 4 + 6M) = B\varepsilon(12M + 4).
> \end{aligned}
> $$
>
> The middle term is $0$ because Fubini for rectangles gives exact equality for $D_k$.
>
> **Step 10: Conclusion.**
>
> Let $C = B(12M + 4)$. We have shown:
>
> $$
> \left| \iint_D f \, dA - \int_a^b \int_{\psi(x)}^{\varphi(x)} f \, dy \, dx \right| \leq C\varepsilon.
> $$
>
> Since $\varepsilon > 0$ was arbitrary and $C$ is independent of $\varepsilon$, the left side must equal $0$:
>
> $$
> \iint_D f(x, y) \, dA = \int_a^b \left( \int_{\psi(x)}^{\varphi(x)} f(x, y) \, dy \right) dx.
> $$

^pf-15-9

*Uses:* [[§2 Open and Closed Sets#^def-2-new3|Def. §2.4]], [[§1 Sequences and Limits in ℝⁿ#^def-1-1|Def. §1.1]], [[§15 Multivariable Integration#^thm-15-4|§15.4]], [[§15 Multivariable Integration#^thm-15-5|§15.5]], [[§15 Multivariable Integration#^cor-15-6|§15.6]], [[Fubini's Theorem|§15.8]], [[Heine–Borel Theorem|590 §15.12]], [[Continuous Image of a Compact Space is Compact|590 §15.3]], [[§19 Uniform Continuity#^thm-19-1|451 §19.1]], [[§33 Properties of the Riemann Integral#^thm-33-4|451 §33.4]], [[§33 Properties of the Riemann Integral#^thm-33-5|451 §33.5]]

![[m452-15-8.svg]]
*Steps 3–5 of the proof. On a grid of side $1/2^k$, each column is stretched to whole squares: from $\psi_k$ (the grid line just below $\inf \psi$ on the column) up to $\varphi_k$ (the grid line just above $\sup \varphi$), and from $a_k$ to $b_k$ horizontally. The resulting staircase $D_k$ (red outline) contains $D$ (blue). Fubini holds exactly on $D_k$, since each column is a rectangle. The error region $D_k \setminus D$ (red) is a thin skin along $\partial D$. By uniform continuity of $\varphi$ and $\psi$, its height in each column is $< 2\varepsilon$, so its total area is $O(\varepsilon)$.*

> [!remark]- Connections
> - Computational version: [[§99 Double Integrals Over General Regions#^thm-99-1|Calc Thm. §99.1]] (with worked examples); with f ≡ 1 it is the area between curves, [[§39 Areas Between Curves#^thm-39-1|Calc Thm. §39.1]].

> [!theorem] Theorem §15.10: Fubini for Type II Regions
> If $D = \{(x, y) : c \leq y \leq d, \; h_1(y) \leq x \leq h_2(y)\}$ and $f$ is continuous on $D$, then:
>
> $$
> \iint_D f(x, y) \, dA = \int_c^d \left( \int_{h_1(y)}^{h_2(y)} f(x, y) \, dx \right) dy.
> $$

^thm-15-10

> [!proof]+ Proof
> The proof is identical to the [[§15 Multivariable Integration#^thm-15-9|Type I case]], with the roles of $x$ and $y$ interchanged. The region is approximated by horizontal stacks of rectangles, and uniform continuity of $h_1, h_2$ controls the boundary oscillation.

^pf-15-10

*Uses:* [[§15 Multivariable Integration#^thm-15-9|§15.9]], [[§19 Uniform Continuity#^thm-19-1|451 §19.1]]

> [!remark]- Connections
> - Computational version: [[§99 Double Integrals Over General Regions#^thm-99-2|Calc Thm. §99.2]] (with worked examples).

### Changing the Order of Integration

> [!theorem] Corollary §15.11: Changing Order of Integration
> If $D$ is both Type I and Type II (i.e., can be described either way), and $f$ is continuous on $D$, then:
>
> $$
> \int_a^b \int_{g_1(x)}^{g_2(x)} f(x, y) \, dy \, dx = \int_c^d \int_{h_1(y)}^{h_2(y)} f(x, y) \, dx \, dy.
> $$

^cor-15-11

> [!proof]+ Proof
> Both iterated integrals equal $\iint_D f \, dA$ by the [[§15 Multivariable Integration#^thm-15-9|Type I]] and [[§15 Multivariable Integration#^thm-15-10|Type II]] versions of Fubini's theorem.

^pf-15-11

*Uses:* [[§15 Multivariable Integration#^thm-15-9|§15.9]], [[§15 Multivariable Integration#^thm-15-10|§15.10]]

> [!remark] Remark: When to Change Order
> Changing the order of integration is useful when:
> - One order leads to an integral that is difficult or impossible to evaluate in closed form.
> - The other order simplifies the computation.
>
> The key step is to carefully describe the region $D$ in both Type I and Type II forms.

^rem-15-11

> [!example] Example §15.1: Changing Order of Integration
> Evaluate $\displaystyle \int_0^1 \int_x^1 e^{y^2} \, dy \, dx$.
>
> **Problem:** The inner integral $\int_x^1 e^{y^2} \, dy$ has no elementary antiderivative.
>
> **Solution:** Change the order of integration ([[§15 Multivariable Integration#^cor-15-11|Corollary §15.11]]).
>
> The region is $D = \{(x, y) : 0 \leq x \leq 1, \; x \leq y \leq 1\}$.
>
> Rewrite as Type II: $D = \{(x, y) : 0 \leq y \leq 1, \; 0 \leq x \leq y\}$.
>
> Then:
>
> $$
> \int_0^1 \int_x^1 e^{y^2} \, dy \, dx = \int_0^1 \int_0^y e^{y^2} \, dx \, dy = \int_0^1 e^{y^2} \cdot y \, dy = \frac{1}{2} e^{y^2} \Big|_0^1 = \frac{e - 1}{2}.
> $$

^ex-15-1


![[m452-15-7.svg]]
*The triangle of Example §15.1 sliced both ways. Left, as a Type I region: the vertical slice at $x$ runs over $x \leq y \leq 1$, and the inner integral $\int_x^1 e^{y^2}\,dy$ cannot be done in closed form. Right, as a Type II region: the horizontal slice at $y$ runs over $0 \leq x \leq y$, and $e^{y^2}$ is constant along it, so the inner integral is just $y\,e^{y^2}$. Same region, same double integral ([[§15 Multivariable Integration#^cor-15-11|§15.11]]), but only one order is computable.*

### A Counterexample: When Fubini Fails

> [!example] Example §15.2: Failure without Absolute Integrability
> Consider $f(x, y) = \dfrac{x^2 - y^2}{(x^2 + y^2)^2}$ on $(0, 1] \times (0, 1]$.
>
> Compute the iterated integrals:
>
> $$
> \int_0^1 \left( \int_0^1 \frac{x^2 - y^2}{(x^2 + y^2)^2} \, dy \right) dx = \int_0^1 \frac{1}{x^2 + 1} \, dx = \frac{\pi}{4}.
> $$
>
> $$
> \int_0^1 \left( \int_0^1 \frac{x^2 - y^2}{(x^2 + y^2)^2} \, dx \right) dy = \int_0^1 \frac{-1}{y^2 + 1} \, dy = -\frac{\pi}{4}.
> $$
>
> The two iterated integrals give different values! This happens because $f$ is unbounded near the origin (so it is not Riemann integrable on the square), and even as an improper integral (over $[\delta, 1]^2$, $\delta \to 0$) it is not absolutely integrable:
>
> $$
> \iint_{(0,1] \times (0,1]} |f(x, y)| \, dA = +\infty.
> $$
>
> The function is not absolutely integrable, so Fubini's theorem does not apply.

^ex-15-2

> [!remark]- Connections
> - The integrals here are improper (the integrand is unbounded near the origin): [[§36 Improper Integrals|451 §36]].
> - Same counterexample in 551, excluded there by the hypothesis $f \in L(\mathbb{R}^n)$ of Fubini's theorem: [[§17 Invariance Properties and Fubini's Theorem#^rem-17-3|551 Rem. §17.3]].

> [!theorem] Theorem §15.12: Fubini-Tonelli: Non-negative Functions
> If $f \geq 0$ is measurable on $D$, then:
>
> $$
> \iint_D f \, dA = \int \left( \int f \, dy \right) dx = \int \left( \int f \, dx \right) dy
> $$
>
> where all three quantities are equal (possibly $+\infty$).
>
> This is useful for checking absolute integrability: compute $\iint_D |f| \, dA$ using iterated integrals. If finite, Fubini applies to $f$.

^thm-15-12

> [!remark]- Connections
> - Rigorous version, where measurability of the slices and of the inner integral is proved rather than assumed: [[§17 Invariance Properties and Fubini's Theorem#^thm-17-3|551 Thm. §17.3]] (Tonelli).
> - Used in PDEs: Tonelli's check of absolute integrability, followed by Fubini, justifies reversing the order of integration in the transform of $f(t)/t$, [[§51★ Definition and Elementary Properties#^thm-51-6|341 Thm. §51.6]], and in the heat-kernel form of the infinite-rod solution, [[§27 Infinite Rod#^thm-27-3|341 Thm. §27.3]].

> [!remark] Remark: Scope of Theorem §15.12
> The theorem is quoted without proof, and its hypothesis lies outside this course: "measurable" means Lebesgue measurable, which the Riemann–Jordan theory of this section does not define, and the integrals may be $+\infty$ (for unbounded $f$ or $D$ they are understood in the Lebesgue sense, or as improper integrals). Its precise statement and proof are in Measure Theory: [[§17 Invariance Properties and Fubini's Theorem#^thm-17-3|551 Thm. §17.3]] (Tonelli), followed by [[§17 Invariance Properties and Fubini's Theorem#^thm-17-6|551 Thm. §17.6]] (Fubini for absolutely integrable $f$). In this section it explains the failure in [[§15 Multivariable Integration#^ex-15-2|Example §15.2]] (there $\iint |f|\,dA = +\infty$) and is cited in Step 1 of [[§15 Multivariable Integration#^ex-15-7|Example §15.7]], where the exhaustion argument at the end of the example gives a proof that stays within the course.

^rem-15-15

*Continued in [[§15d The Change of Variables Formula]]: the general change of variables formula on rectangles, with three proofs.*
