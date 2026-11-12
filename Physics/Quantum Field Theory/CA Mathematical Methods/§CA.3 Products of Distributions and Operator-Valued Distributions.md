---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: CA
section: CA.3
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§CA.2 Generalized Functions]] · ↑ [[· CA Mathematical Methods]] · [[§CA.3 Fourier Transforms and Fourier Tricks]] →

*Sources: the user's PHY 513 notes, Ch. 6 §6.2 ("Why this matters beyond tidiness"), Ch. 6 §6.7, Ch. 4 §§4.5–4.6, App. A §A.4 · PHY 513, Problem Set 4, Problem 0 · standard results stated here, where marked: Hörmander, The Analysis of Linear Partial Differential Operators I, §§2.2, 5.2, 8.2; Reed & Simon, Methods of Modern Mathematical Physics I, Ch. V; Streater & Wightman, PCT, Spin and Statistics, and All That, Ch. 3; Brunetti & Fredenhagen, Commun. Math. Phys. 208 (2000).*

Two generalized functions cannot in general be multiplied ([[§CA.2 Generalized Functions#^def-ca-2-5|Def. §CA.2.5]]). This section continues [[§CA.2 Generalized Functions|§CA.2]], which defines generalized functions, their supports and the operations on them. It says when a product exists (at each point at least one factor is smooth), shows on $\theta\cdot\delta$, $\delta^2$ and $\delta(0)$ what happens when it does not, gives the box regularization that turns $\delta^3(\mathbf 0)$ into a volume, and defines operator-valued distributions, the kind of object a quantum field is, with the kernel theorem that makes a smeared two-point quantity one distribution in both variables. It uses from §CA.2 the singular support ([[§CA.2 Generalized Functions#^def-ca-2-3|Def. §CA.2.3]]), the product with a smooth function, distributional limits ([[§CA.2 Generalized Functions#^thm-ca-2-5|Theorem §CA.2.5]]), the principal value ([[§CA.2 Generalized Functions#^def-ca-2-10|Def. §CA.2.10]]) and the two products of [[§CA.2 Generalized Functions#^ex-ca-2-1|Example §CA.2.1]]. The plane-wave delta function, of which the box is the discrete form, is [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]] of the next section. Each statement lists in Connections the places that use it.

## Products

> [!theorem] Theorem §CA.2.8: Products with Disjoint Singular Supports
> 1. If $g$ is smooth, $gT$ is defined for every $T \in \mathcal D'$; if moreover every derivative of $g$ grows at most polynomially, $gT \in \mathcal S'$ for every $T \in \mathcal S'$ ([[§CA.2 Generalized Functions#^def-ca-2-5|Def. §CA.2.5]]).
> 2. If $\operatorname{sing\,supp}S \cap \operatorname{sing\,supp}T = \emptyset$, the product $ST$ is defined, uniquely, by being $gT$ near every point where $S = g$ is smooth and $hS$ near every point where $T = h$ is smooth.
> 3. In general there is no product: no associative product of distributions extends multiplication by smooth functions and contains δ and the principal value $\mathcal P\frac1x$ ([[§CA.2 Generalized Functions#^def-ca-2-10|Def. §CA.2.10]]), because $(x\,\delta)\,\mathcal P\frac1x = 0$ while $\delta\,(x\,\mathcal P\frac1x) = \delta$ ([[§CA.2 Generalized Functions#^ex-ca-2-1|Example §CA.2.1]]).
>
> *Source: standard; stated here (Hörmander I, §§2.2, 8.2; L. Schwartz's impossibility theorem in its elementary form) · the user's PHY 513 notes, Ch. 6 §6.2 ("Why this matters beyond tidiness": products)*

^thm-ca-2-8

> [!derivation]- Derivation
> **Step 1** (part 1). For $\varphi \in \mathcal D$, $g\varphi \in \mathcal D$; for $\varphi \in \mathcal S$ and polynomially bounded derivatives of $g$, the Leibniz rule bounds each $\|g\varphi\|_{\alpha,\beta}$ by finitely many seminorms of $\varphi$, so $g\varphi \in \mathcal S$ and $\varphi \mapsto T[g\varphi]$ is continuous.
>
> **Step 2** (part 2: cover). Every point has an open neighbourhood on which $S$ or $T$ is smooth, because no point lies in both singular supports.
>
> **Step 3** (part 2: patch). Take a locally finite cover by such neighbourhoods $U_j$ and a partition of unity $\sum_j\chi_j = 1$ with $\chi_j \in \mathcal D$ supported in $U_j$. Define $(ST)[\varphi] = \sum_jP_j[\chi_j\varphi]$, with $P_j = g_jT$ if $S = g_j$ on $U_j$ and $P_j = h_jS$ if $T = h_j$ there. Each term is defined by Step 1, and for $\varphi \in \mathcal D$ only finitely many terms are nonzero.
>
> **Step 4** (part 2: consistency). *(a) On an overlap the prescriptions agree.* Let $U$, $U'$ be two of the neighbourhoods, with prescriptions $P$, $P'$, and let $\psi \in \mathcal D$ be supported in $U \cap U'$. If $P = gT$ and $P' = g'T$ (both with $S$ smooth: $S[\chi] = \int g\chi$ for $\chi$ supported in $U$, $S[\chi] = \int g'\chi$ for $\chi$ supported in $U'$), then $\int(g - g')\chi = 0$ for every $\chi \in \mathcal D$ supported in $U \cap U'$, so the continuous function $g - g'$ vanishes there ([[§CA.2 Generalized Functions#^thm-ca-2-1|Theorem §CA.2.1]], Step 4), and $gT[\psi] = T[g\psi] = T[g'\psi] = g'T[\psi]$; likewise for $P = hS$, $P' = h'S$. If $P = gT$ and $P' = hS$ (on $U$, $S = g$; on $U'$, $T = h$), then $g\psi$ is supported in $U'$ and $h\psi$ in $U$, so $gT[\psi] = T[g\psi] = \int h\,g\psi = S[h\psi] = hS[\psi]$. In every case $P[\psi] = P'[\psi]$.
>
> *(b) Independence of the cover and the partition.* Let $\{U_j, \chi_j, P_j\}$ and $\{U'_k, \chi'_k, P'_k\}$ be two choices. For $\varphi \in \mathcal D$ only finitely many $\chi_j\varphi$ and $\chi'_k\varphi$ are nonzero, and $\chi_j\varphi = \sum_k\chi'_k\chi_j\varphi$, $\chi'_k\varphi = \sum_j\chi_j\chi'_k\varphi$, finite sums. Each $\chi_j\chi'_k\varphi$ is supported in $U_j \cap U'_k$, so by (a) and linearity
>
> $$
> \sum_jP_j[\chi_j\varphi] = \sum_{j,k}P_j[\chi_j\chi'_k\varphi] = \sum_{j,k}P'_k[\chi_j\chi'_k\varphi] = \sum_kP'_k[\chi'_k\varphi] .
> $$
>
> *(c) A generalized function with the stated property, and the only one.* If $\varphi_n \to \varphi$ in $\mathcal D$, all supports lie in one bounded closed set, which meets the supports of only finitely many $\chi_j$ (the family of supports is locally finite and the set is compact); $\chi_j\varphi_n \to \chi_j\varphi$ in $\mathcal D$ by the Leibniz rule, so each of the finitely many terms $P_j[\chi_j\varphi_n]$ converges: $ST$ is continuous. For $\varphi$ supported in one $U_i$, each $\chi_j\varphi$ is supported in $U_j \cap U_i$, so by (a) $\sum_jP_j[\chi_j\varphi] = \sum_jP_i[\chi_j\varphi] = P_i[\varphi]$: on $U_i$ the product is the prescription $P_i$, that is $gT$ or $hS$. Uniqueness: a generalized function $Q$ that equals a prescription $P'_k$ on each set of some cover $\{U'_k\}$ of this kind satisfies $Q[\varphi] = \sum_kQ[\chi'_k\varphi] = \sum_kP'_k[\chi'_k\varphi]$, which by (b) is $(ST)[\varphi]$. (A partition of unity subordinate to a cover of $\mathbb R^n$ by bounded neighbourhoods, with locally finite supports, exists by [[§65 Partitions of Unity#^thm-65-7|591 Thm. §65.7]]; its functions then have compact support. The same bookkeeping is Hörmander I, §2.2.)
>
> **Step 5** (part 3: $x\,\mathcal P\frac1x = 1$). [[§CA.2 Generalized Functions#^ex-ca-2-1|Example §CA.2.1]], 2: $(x\,\mathcal P\frac1x)[\varphi] = \mathcal P\frac1x[x\varphi] = \int\varphi = T_1[\varphi]$.
>
> **Step 6** (part 3: $x\,\delta = 0$). [[§CA.2 Generalized Functions#^ex-ca-2-1|Example §CA.2.1]], 1: $(x\,\delta)[\varphi] = \delta[x\varphi] = 0$.
>
> **Step 7** (part 3: the contradiction). An associative product would give $\delta = \delta\cdot1 = \delta\,(x\,\mathcal P\frac1x) = (\delta\,x)\,\mathcal P\frac1x = 0\cdot\mathcal P\frac1x = 0$, which is false. Here δ and $\mathcal P\frac1x$ share the singular point $0$, which part 2 excludes.
>
> **What the derivation shows.**
> - A product is defined exactly when at each point at least one factor is smooth; at a common singular point no value is canonical and a regularization must choose one ([[§CA.2 Generalized Functions#^thm-ca-2-9|Theorem §CA.2.9]]).
> - $\theta(x^0)D(x)$: $\operatorname{sing\,supp}\theta(x^0)$ is the hyperplane $x^0 = 0$ and $\operatorname{sing\,supp}D$ is the light cone; they meet only at $x = 0$. So the product is defined on $\mathbb R^4 \setminus \{0\}$; an extension across $0$ exists (the slice-by-slice definition, [[§C2b.6 Green's Functions and Contours#^thm-c2b-6-6|Theorem §C2b.6.6]]), any two extensions differ by $\sum c_\alpha\partial^\alpha\delta^4$ ([[§CA.2 Generalized Functions#^thm-ca-2-2|Theorem §CA.2.2]]), and the Green's-function equation removes even that freedom ([[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-7|Theorem §CA.6.7]], 3). Equivalently, by power counting: $D$ scales like $|x|^{-2}$ at the origin, every $\partial^\alpha\delta^4$ at least like $|x|^{-4}$, so exactly one extension is no more singular than $D$ itself (scaling degree $2 < 4$; Brunetti–Fredenhagen, Commun. Math. Phys. 208 (2000), Thm. 5.2; quoted).

^der-ca-2-8

*Uses:* [[§CA.2 Generalized Functions#^def-ca-2-3|Def. §CA.2.3]], [[§CA.2 Generalized Functions#^def-ca-2-5|Def. §CA.2.5]], [[§CA.2 Generalized Functions#^def-ca-2-10|Def. §CA.2.10]], [[§CA.2 Generalized Functions#^ex-ca-2-1|Example §CA.2.1]], [[§CA.2 Generalized Functions#^thm-ca-2-1|Theorem §CA.2.1]], [[§65 Partitions of Unity#^thm-65-7|591 Thm. §65.7]]

> [!theorem] Theorem §CA.2.9: Products Without a Value: θ·δ, δ² and δ(0)
> Let $\rho, \sigma \in \mathcal D(\mathbb R)$ be nonnegative with unit integral, $\delta_\varepsilon = \rho_\varepsilon$ and $\theta_\varepsilon(x) = \int_{-\infty}^x\sigma_\varepsilon$.
> 1. $\theta_\varepsilon\delta_\varepsilon \to c\,\delta$ with $c = \int\rho(u)\Sigma(u)\,du$, $\Sigma(u) = \int_{-\infty}^u\sigma$. For $\sigma = \rho$, $c = \frac12$; as $\rho$ and $\sigma$ vary, $c$ takes every value in $[0, 1]$. So "$\theta(0)$", and with it $\theta\cdot\delta$, has no value.
> 2. $\delta_\varepsilon^2[\varphi] = \varepsilon^{-1}\varphi(0)\int\rho^2 + o(\varepsilon^{-1}) \to \infty$ whenever $\varphi(0) \ne 0$: $\delta^2$ does not exist.
> 3. $\delta^n_\varepsilon(0) = \varepsilon^{-n}\rho(0)$ in $n$ dimensions: δ evaluated at its singular point has no value. The $\delta^3(\mathbf 0)$ of a mode sum is this evaluation; it acquires a meaning only through a regularization ([[§CA.2 Generalized Functions#^thm-ca-2-10|Theorem §CA.2.10]]).
>
> *Source: standard; stated here · the user's PHY 513 notes, Ch. 6 §6.2 ("Why this matters beyond tidiness"), Ch. 4 §4.6 (the $\delta^3(0)$ of the zero-point energy)*

^thm-ca-2-9

> [!derivation]- Derivation
> **Step 1** (part 1: substitute). $\theta_\varepsilon(x) = \int_{-\infty}^x\varepsilon^{-1}\sigma(y/\varepsilon)\,dy = \Sigma(x/\varepsilon)$ (substitute $y = \varepsilon v$). Then, with $x = \varepsilon u$,
>
> $$
> \int dx\,\theta_\varepsilon(x)\,\delta_\varepsilon(x)\,\varphi(x) = \int du\,\Sigma(u)\,\rho(u)\,\varphi(\varepsilon u) \longrightarrow \varphi(0)\int du\,\Sigma(u)\rho(u),
> $$
>
> by dominated convergence ($0 \le \Sigma \le 1$, so the integrand is bounded by $\rho(u)\sup|\varphi|$).
>
> **Step 2** (part 1: one kernel). For $\sigma = \rho$, $\Sigma' = \rho$, so $\int\Sigma\rho\,du = \int\Sigma\Sigma'\,du = \bigl[\tfrac12\Sigma^2\bigr]_{-\infty}^{\infty} = \tfrac12(1 - 0) = \tfrac12$, whatever $\rho$ is.
>
> **Step 3** (part 1: two kernels). Let $\sigma$ vanish outside $[-1, 1]$ and $\rho(u) = \rho_0(u - b)$ with $\rho_0$ vanishing outside $[-1, 1]$. For $b \ge 2$, $\Sigma = 1$ on the support of $\rho$ and $c = 1$; for $b \le -2$, $\Sigma = 0$ there and $c = 0$; $c$ depends continuously on $b$, so it takes every value in $[0, 1]$.
>
> ⚑ By-product: the convention $\theta(0) = \frac12$ is the choice of one and the same smoothing for both factors (Step 2), not a fact → [[§C2b.7 Time Ordering, the Feynman Propagator and the iε Prescription#^cau-c2b-7-1|§C2b.7, Caution: The step function at zero]].
>
> **Step 4** (part 2). $\int dx\,\varepsilon^{-2}\rho(x/\varepsilon)^2\varphi(x) = \varepsilon^{-1}\int du\,\rho(u)^2\varphi(\varepsilon u)$ (substitute $x = \varepsilon u$), and the last integral tends to $\varphi(0)\int\rho^2 > 0$ by dominated convergence. So the pairing grows like $\varepsilon^{-1}$.
>
> **Step 5** (part 3). $\rho_\varepsilon(0) = \varepsilon^{-n}\rho(0/\varepsilon) = \varepsilon^{-n}\rho(0)$, divergent and dependent on $\rho$. In the plane-wave representation, $(2\pi)^3\delta^3(\mathbf k) = \int d^3x\,e^{i\mathbf k\cdot\mathbf x}$ at $\mathbf k = \mathbf 0$ is $\int d^3x\,1$, the volume of space: the regularization of Theorem §CA.2.10.
>
> **What the derivation shows.**
> - At a common singular point the answer depends on how the factors were smoothed: the hallmark of an undefined product.
> - Where C2a–C2b meet each case: $\theta\cdot\delta$ in the time derivative of a time-ordered product, where it multiplies an equal-time commutator ([[§C2b.7 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-7-1|Theorem §C2b.7.1]]); $\delta^3(\mathbf 0)$ in the zero-point energy ([[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-4|Theorem §C2a.3.4]]); $\hat\phi(x)^2$ at one point, whose vacuum part is the Wightman function at coincident points ([[§C2b.7 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-7-8|Theorem §C2b.7.8]]).

^der-ca-2-9

*Uses:* [[§CA.2 Generalized Functions#^thm-ca-2-5|Theorem §CA.2.5]], [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|Theorem §CA.1.1]]

> [!theorem] Theorem §CA.2.10: Box Regularization of δ³(0)
> In a cube of side $L$ and volume $V = L^3$ with periodic boundary conditions, the momenta are $\mathbf k \in (2\pi/L)\mathbb Z^3$ and
>
> $$
> \int_Vd^3x\,e^{i(\mathbf k - \mathbf k')\cdot\mathbf x} = V\,\delta_{\mathbf k\mathbf k'} .
> $$
>
> As $L \to \infty$, $\sum_{\mathbf k} \leftrightarrow V\int\frac{d^3k}{(2\pi)^3}$ and $V\delta_{\mathbf k\mathbf k'} \leftrightarrow (2\pi)^3\delta^3(\mathbf k - \mathbf k')$. The coincident value is then $(2\pi)^3\delta^3(\mathbf 0) \leftrightarrow V$: a quantity proportional to $\delta^3(\mathbf 0)$ is proportional to the volume, and its density is finite or not according to the remaining integral.
>
> *Source: the user's PHY 513 notes, Ch. 4 §4.6 ("$(2\pi)^3\delta^3(0) = \int d^3x = V$ is the volume of space"), Ch. 4 §4.5 (discrete modes) · standard*

^thm-ca-2-10

> [!derivation]- Derivation
> **Step 1** (one dimension). For $k = 2\pi n/L$, $k' = 2\pi n'/L$ with integers $n$, $n'$: if $n = n'$ the integrand of $\int_0^Ldx\,e^{i(k - k')x}$ is $1$ and the integral is $L$; if $n \ne n'$,
>
> $$
> \int_0^Ldx\,e^{i(k - k')x} = \frac{e^{i(k - k')L} - 1}{i(k - k')} = \frac{e^{2\pi i(n - n')} - 1}{i(k - k')} = 0 .
> $$
>
> So the integral is $L\,\delta_{nn'}$.
>
> **Step 2** (three dimensions). The exponential factorizes over the three axes; the product of three Step-1 integrals is $L^3\delta_{\mathbf k\mathbf k'} = V\delta_{\mathbf k\mathbf k'}$.
>
> **Step 3** (sums become integrals). The allowed $\mathbf k$ form a cubic lattice of spacing $2\pi/L$, one point per cell of volume $(2\pi)^3/V$. For a continuous, rapidly decreasing $F$, $\sum_{\mathbf k}F(\mathbf k)\frac{(2\pi)^3}{V}$ is a Riemann sum and tends to $\int d^3k\,F(\mathbf k)$. Hence $\sum_{\mathbf k} \leftrightarrow V\int\frac{d^3k}{(2\pi)^3}$.
>
> **Step 4** (the delta). The Kronecker delta satisfies $\sum_{\mathbf k'}\delta_{\mathbf k\mathbf k'}F(\mathbf k') = F(\mathbf k)$. By Step 3 the left side is $V\int\frac{d^3k'}{(2\pi)^3}\,\delta_{\mathbf k\mathbf k'}F(\mathbf k')$, and this equals $F(\mathbf k)$ for every $F$ only if $\delta_{\mathbf k\mathbf k'}$ stands for $(2\pi)^3\delta^3(\mathbf k - \mathbf k')/V$. So $V\delta_{\mathbf k\mathbf k'} \leftrightarrow (2\pi)^3\delta^3(\mathbf k - \mathbf k')$, and Step 2 is the box form of [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]].
>
> **Step 5** (the coincident value). At $\mathbf k = \mathbf k'$ the box gives $V\delta_{\mathbf k\mathbf k} = V$, where $(2\pi)^3\delta^3(\mathbf 0)$ itself has no value ([[§CA.2 Generalized Functions#^thm-ca-2-9|Theorem §CA.2.9]], 3). Equivalently, $\int_Vd^3x\,e^{i\mathbf 0\cdot\mathbf x} = V$.
>
> ⚑ By-product: the zero-point energy $\frac12(2\pi)^3\delta^3(\mathbf 0)\int\frac{d^3k}{(2\pi)^3}E_{\mathbf k}$ becomes $V\int\frac{d^3k}{(2\pi)^3}\frac{E_{\mathbf k}}2$, a volume times an energy density, and the density is still divergent at large $\mathbf k$ → [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-4|Theorem §C2a.3.4]].
>
> **What the derivation shows.**
> - $\delta^3(\mathbf 0)$ is an infrared divergence, the volume of space; it is a different divergence from the ultraviolet one of $\int d^3k\,E_{\mathbf k}$.
> - In a box only densities and differences have a limit as $L \to \infty$; the box is a regularization, removed at the end.

^der-ca-2-10

*Uses:* [[§CA.2 Generalized Functions#^thm-ca-2-9|Theorem §CA.2.9]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]]

> [!remark] Remark: Point splitting: how a product at one point is regularized
> For $x \ne y$, $\hat\phi(x)\hat\phi(y)$ is a well-defined operator-valued distribution in the pair $(x, y)$; its vacuum expectation value is $D_W(x - y)$ ([[§C2b.2 The Wightman Function#^def-c2b-2-1|Def. §C2b.2.1]]). The product at one point is the limit $y \to x$, which does not exist: $D_W(x - y)$ grows like $1/4\pi^2|(x - y)^2|$ as the points approach ([[§C2b.3 Explicit Forms of the Wightman Function|§C2b.3]]). Subtracting the vacuum part first, $:\!\hat\phi(x)^2\!: = \lim_{y\to x}\bigl[\hat\phi(x)\hat\phi(y) - D_W(x - y)\bigr]$, leaves a finite operator-valued distribution: this is normal ordering ([[§C2a.3 Energy, Momentum and the Zero-Point Energy#^def-c2a-3-1|Def. §C2a.3.1]]), and the subtracted $c$-number, differentiated in $x$ and $y$ before the points meet, gives the zero-point energy density ([[§C2b.7 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-7-8|Theorem §C2b.7.8]]). The box ([[§CA.2 Generalized Functions#^thm-ca-2-10|Theorem §CA.2.10]]) regularizes the volume; point splitting regularizes the coincident point.
>
> *Source: standard; stated here · the user's PHY 513 notes, Ch. 6 §6.2 ("Why this matters beyond tidiness"), Ch. 6 §6.7 (the zero-point energy as the Wightman function at coincident points)*

^rem-ca-2-2

## Operator-valued distributions

> [!definition] Definition §CA.2.11: Operator-Valued Distribution
> Let $\mathcal H$ be a Hilbert space and $\mathcal D_0 \subset \mathcal H$ a dense subspace. An **operator-valued (tempered) distribution** on $\mathbb R^n$ is a map $f \mapsto \Phi(f)$ from $\mathcal S(\mathbb R^n)$ to linear operators defined on $\mathcal D_0$, with $\Phi(f)\mathcal D_0 \subseteq \mathcal D_0$, linear in $f$, such that for all $\Psi_1, \Psi_2 \in \mathcal D_0$ the matrix element $f \mapsto \langle\Psi_1|\Phi(f)|\Psi_2\rangle$ is a tempered distribution. One writes $\Phi(f) = \int d^nx\,f(x)\,\Phi(x)$; the symbol $\Phi(x)$ is the kernel of this notation, not an operator.
>
> *Source: standard; stated here (Streater & Wightman, Ch. 3) · the user's PHY 513 notes, App. A §A.4 and Ch. 6 §6.2 ("operator-valued distribution", $\phi[\varphi] = \int d^4x\,\varphi(x)\phi(x)$)*

^def-ca-2-11

> [!theorem] Theorem §CA.2.11: The Kernel Theorem
> If $B(f, g)$ is bilinear on $\mathcal S(\mathbb R^n) \times \mathcal S(\mathbb R^m)$ and continuous in each argument separately, there is a unique $K \in \mathcal S'(\mathbb R^{n+m})$ with $B(f, g) = K[f \otimes g]$, $(f \otimes g)(x, y) = f(x)g(y)$. So a smeared two-point quantity, such as $\langle0|\hat\phi(f)\hat\phi(g)|0\rangle$ or $[\hat a(f), \hat a^\dagger(g)]$, is one distribution $K(x, y)$ in both variables together.
>
> *Source: standard; stated here (L. Schwartz's kernel theorem; Reed & Simon I, Ch. V; Hörmander I, §5.2)*

^thm-ca-2-11

> [!derivation]- Derivation (stated; an example worked)
> **Step 1** (the theorem). Not proved here: it rests on the nuclearity of $\mathcal S$ (Reed & Simon I, Ch. V).
> <!-- S6 (2026-11-12): searched ~/Notes/Math (Functional Analysis 556, Measure Theory 551, Multivariable Analysis 452, Topology, Differentiable Manifolds 591) and Applied Math for "kernel theorem", "nuclear", "tensor product of distributions", "Schwartz": no statement or proof in the vault; Reed & Simon and Hörmander not opened. The theorem stays stated, not proved. -->
>
> **Step 2** (example: the mode algebra, smeared). With $\hat a(f) = \int\frac{d^3p}{(2\pi)^3}\overline{f(\mathbf p)}\,\hat a_{\mathbf p}$ and $\hat a^\dagger(g) = \int\frac{d^3q}{(2\pi)^3}g(\mathbf q)\,\hat a^\dagger_{\mathbf q}$ for $f, g \in \mathcal S(\mathbb R^3)$, the commutator of [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|Theorem §C2a.2.6]] gives
>
> $$
> [\hat a(f), \hat a^\dagger(g)] = \int\frac{d^3p}{(2\pi)^3}\overline{f(\mathbf p)}\,g(\mathbf p) ,
> $$
>
> a number bounded by $\|f\|_{L^2}\|g\|_{L^2}/(2\pi)^3$ and hence continuous in each argument. (It is antilinear in $f$; the theorem applies to the bilinear form $(f, g) \mapsto [\hat a(\bar f), \hat a^\dagger(g)]$.) Its kernel, with respect to the measure $\frac{d^3p}{(2\pi)^3}\frac{d^3q}{(2\pi)^3}$, is $(2\pi)^3\delta^3(\mathbf p - \mathbf q)$: the unsmeared relation $[\hat a_{\mathbf p}, \hat a^\dagger_{\mathbf q}] = (2\pi)^3\delta^3(\mathbf p - \mathbf q)$ is the statement of the theorem for this $B$.
>
> **What the derivation shows.**
> - Every two-point formula with $\delta$'s, or with $D_W(x - y)$, is an identity between kernels in the sense of this theorem: it means what it says after both points are smeared.

^der-ca-2-11

*Uses:* [[§CA.2 Generalized Functions#^def-ca-2-11|Def. §CA.2.11]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|Theorem §C2a.2.6]]

> [!remark] Remark: What the language buys in field theory
> - *A Green's function is a linear map.* The sources of physics, smooth and of finite duration, are test functions, and $\phi = i\int D_C\,j$ defines the map $j \mapsto \phi$; "$D_C(x - y)$" is the kernel through which it is written, not a function with values. There is one such map per boundary condition ([[§C2b.6 Green's Functions and Contours#^def-c2b-6-1|Def. §C2b.6.1]]).
> - *Integrals that converge nowhere still define objects.* $\int d^3p\,e^{-ip\cdot\xi}/2E_{\mathbf p}$ converges for no real $\xi$, yet it is a tempered distribution, the boundary value of an analytic function ([[§C2b.2 The Wightman Function#^thm-c2b-2-5|Theorem §C2b.2.5]]).
> - *Products at a point are undefined.* The field is an operator-valued distribution, $\hat\phi[f] = \int d^4x\,f(x)\hat\phi(x)$, and $\hat\phi(x)^2$ is a product of distributions at one point. That is the origin of the $\delta^3(0)$ in the zero-point energy and of normal ordering ([[§C2a.3 Energy, Momentum and the Zero-Point Energy#^def-c2a-3-1|Def. §C2a.3.1]]), and later of every ultraviolet divergence.
>
> *Source: the user's PHY 513 notes, Ch. 6 §6.2, App. A §A.4 · PHY 513, Problem Set 4, Problem 0*

^rem-ca-2-3

> [!remark]- Connections
> - Operator-valued distributions ([[§CA.2 Generalized Functions#^def-ca-2-11|Def. §CA.2.11]]) carry the idea of [[§CA.2 Generalized Functions|§CA.2]], a generalized function as an element of a dual space, one level up: $\hat\phi(x)$ is no more an operator than a position "eigenket" is a vector ([[§48 Position Eigenstates and Continuous Resolutions#^prop-48-3|556 Prop. §48.3]]).
> - Where a product is not defined, the freedom that remains is measured by the point-support theorem ([[§CA.2 Generalized Functions#^thm-ca-2-2|Theorem §CA.2.2]]): two extensions of a product across a point differ by finitely many derivatives of δ there (Theorem §CA.2.8, What the derivation shows).
> - The box of Theorem §CA.2.10 and the plane-wave delta function of [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]] are one identity in two normalizations, $V\delta_{\mathbf k\mathbf k'} \leftrightarrow (2\pi)^3\delta^3(\mathbf k - \mathbf k')$; the box in space and time is [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-10|Theorem §CA.3.10]].
> - **Used in**, statement by statement (C2a–C2b items):
>   - Theorem §CA.2.8 (products): $D_R = \theta(x^0)D$, $T$-products — [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-3|Theorem §C2a.2.3]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|Theorem §C2a.2.6]], [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-1|Theorem §C2a.3.1]], [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-6|Theorem §C2a.3.6]], [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-1|Theorem §C2a.4.1]], [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-3|Theorem §C2a.4.3]], [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-4|Theorem §C2a.4.4]], [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-5|Theorem §C2a.4.5]], [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-3|Theorem §C2a.5.3]], [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-4|Theorem §C2a.5.4]], [[§C2b.5 Microcausality and the Commutator Function#^thm-c2b-5-4|Theorem §C2b.5.4]], [[§C2b.5 Microcausality and the Commutator Function#^thm-c2b-5-13|Theorem §C2b.5.13]], [[§C2b.1 Heisenberg Fields#^thm-c2b-1-3|Theorem §C2b.1.3]], [[§C2b.6 Green's Functions and Contours#^thm-c2b-6-4|Theorem §C2b.6.4]], [[§C2b.6 Green's Functions and Contours#^thm-c2b-6-5|Theorem §C2b.6.5]], [[§C2b.6 Green's Functions and Contours#^thm-c2b-6-6|Theorem §C2b.6.6]], [[§C2b.7 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-7-4|Theorem §C2b.7.4]], [[§C2b.7 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-7-7|Theorem §C2b.7.7]], [[§C2b.6 Green's Functions and Contours#^thm-c2b-6-2|Theorem §C2b.6.2]].
>   - Theorem §CA.2.9 (θ·δ, δ², δ(0)): the zero-point energy, time-ordering contact terms — [[§C2a.1 Canonical Quantization of Fields#^thm-c2a-1-3|Theorem §C2a.1.3]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-7|Theorem §C2a.2.7]], [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-3|Theorem §C2a.3.3]], [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-4|Theorem §C2a.3.4]], [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-5|Theorem §C2a.4.5]], [[§C2b.7 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-7-4|Theorem §C2b.7.4]], [[§C2b.7 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-7-7|Theorem §C2b.7.7]], [[§C2a.5 The Complex Scalar Field and Its Charge|§C2a.5]] (Mathematical background).
>   - Theorem §CA.2.10 (box) and Remark: Point splitting: $(2\pi)^3\delta^3(\mathbf 0) \to V$, normal ordering — [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-1|Theorem §C2a.3.1]], [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-3|Theorem §C2a.3.3]], [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-4|Theorem §C2a.3.4]], [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-6|Theorem §C2a.3.6]], [[§C2b.7 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-7-8|Theorem §C2b.7.8]], [[§C2b.7 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-7-7|Theorem §C2b.7.7]], [[§C2a.5 The Complex Scalar Field and Its Charge|§C2a.5]] (Mathematical background).
>   - Def. §CA.2.11, Theorem §CA.2.11 (operator-valued distributions, kernels): $\hat\phi(f)$, $[\hat\phi, \hat\pi] = i\delta^3$, $[\hat a, \hat a^\dagger] = (2\pi)^3\delta^3$, $\langle0|\hat\phi(x)\hat\phi(y)|0\rangle$ — [[§C2a.1 Canonical Quantization of Fields#^def-c2a-1-1|Def. §C2a.1.1]], [[§C2a.1 Canonical Quantization of Fields#^thm-c2a-1-3|Theorem §C2a.1.3]], [[§C2a.2 Mode Expansion and the Mode Algebra#^def-c2a-2-2|Def. §C2a.2.2]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-4|Theorem §C2a.2.4]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-7|Theorem §C2a.2.7]], [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-5|Theorem §C2a.4.5]], [[§C2a.6 Coherent States and the Classical Field#^thm-c2a-6-8|Theorem §C2a.6.8]], [[§C2b.1 Heisenberg Fields#^thm-c2b-1-6|Theorem §C2b.1.6]], [[§C2b.2 The Wightman Function#^thm-c2b-2-2|Theorem §C2b.2.2]], [[§C2a.5 The Complex Scalar Field and Its Charge|§C2a.5]] (Mathematical background), [[§C2a.6 Coherent States and the Classical Field|§C2a.6]] (Mathematical background).
>   - Remark: What the language buys in field theory: [[§C2b.6 Green's Functions and Contours#^rem-c2b-6-1|§C2b.6, Remark: What a Green's "function" is, and why it is not unique]].
> - **Used in**, statement by statement (C1a–C1b items):
>   - Theorem §CA.2.9 (θ·δ, δ², δ(0)): [[§C1b.4 Hamiltonian Field Theory#^thm-c1b-4-5|Theorem §C1b.4.5]].
>   - Def. §CA.2.11, Theorem §CA.2.11 (operator-valued distributions, kernels): [[§C1a.6 Calculus with Indices#^rem-c1a-6-2|§C1a.6, Remark: Three expansions, not one]], [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^rem-c1b-2-8|§C1b.2, Remark: The second variation is the operator whose inverse is the propagator]], [[§C1b.4 Hamiltonian Field Theory#^thm-c1b-4-5|Theorem §C1b.4.5]], [[§C1b.5 Noether's Theorem#^rem-c1b-5-9|§C1b.5, Remark: In what sense these identities hold]].
> - **Used in**, statement by statement (C3 items):
>   - Theorem §CA.2.8 (products): the normalization of the induced states — [[§C3.6★ Particle States and the Little Group#^thm-c3-6-5|Theorem §C3.6.5]], [[§C3.6★ Particle States and the Little Group#^thm-c3-6-6|Theorem §C3.6.6]].
>   - Def. §CA.2.11 (operator-valued distributions): covariance of quantum fields — [[§C3.3 How Fields Transform under the Lorentz Group#^rem-c3-3-2|§C3.3, Remark: The laws for fields that are distributions]], [[§C3.5 Covariant Quantum Fields and the Free Scalar's Representation#^pr-c3-5-1|Principle §C3.5.1]], [[§C3.5 Covariant Quantum Fields and the Free Scalar's Representation#^thm-c3-5-6|Theorem §C3.5.6]].
> - **Used in**, statement by statement (C5a–C5b items):
>   - Theorem §CA.2.8 (products): smooth prefactors on the support of δ, multiplication by polynomials, slice products — [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-3|Theorem §C5b.2.3]], [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-2|Theorem §C5b.3.2]], [[§C5b.4 Fermions, Fock Space and the Pauli Principle#^thm-c5b-4-1|Theorem §C5b.4.1]], [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-1|Theorem §C5b.7.1]], [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-4|Theorem §C5b.7.4]], [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-4|Theorem §C5b.8.4]], [[§C5b.1 Canonical Quantization of the Dirac Field|§C5b.1]] (Mathematical background), [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-4|Theorem §C5b.2.4]], [[§C5b.6 The Heisenberg Dirac Field#^thm-c5b-6-3|Theorem §C5b.6.3]].
>   - Theorem §CA.2.9 (θ·δ, δ², δ(0)): the coincident anticommutator $\delta^3(\mathbf 0)$ — [[§C5b.1 Canonical Quantization of the Dirac Field#^thm-c5b-1-8|Theorem §C5b.1.8]].
>   - Theorem §CA.2.10 (box regularization of $\delta^3(\mathbf 0)$): the fermionic zero-point energy and vacuum charge — [[§C5b.1 Canonical Quantization of the Dirac Field|§C5b.1]] (Connections).
>   - Def. §CA.2.11 (operator-valued distributions): the quantized Dirac field — [[§C5a.7 The Dirac Equation and Its Lagrangian#^rem-c5a-7-5|§C5a.7, Remark: In what sense the equations hold]], [[§C5a.11 The Spinors u(p), v(p) and Their Dirac Conjugates#^rem-c5a-11-2|§C5a.11, Remark: In what sense a general solution is a superposition of these plane waves]], [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-1|Theorem §C5b.2.1]], [[§C5b.1 Canonical Quantization of the Dirac Field#^def-c5b-1-5|Def. §C5b.1.5]], [[§C5a.6 The Dirac Conjugate and the Bilinears#^rem-c5a-6-2|§C5a.6, Remark: The quantized bilinears are Hermitian]], [[§C5b.1 Canonical Quantization of the Dirac Field#^thm-c5b-1-1|Theorem §C5b.1.1]], [[§C5b.6 The Heisenberg Dirac Field#^thm-c5b-6-2|Theorem §C5b.6.2]].
> - **Used in**, statement by statement (C9 items):
>   - Def. §CA.2.11 (operator-valued distribution): the parity law of $\hat\psi$ as an identity after smearing — [[§C9.3 Parity on States, Spinors and the Dirac Field#^thm-c9-3-5|Theorem §C9.3.5]], [[§C9.2 Parity of the Scalar Field#^thm-c9-2-2|Theorem §C9.2.2]], [[§C9.7 Charge Conjugation on the Field and Bilinears#^thm-c9-7-1|Theorem §C9.7.1]], [[§C9.7 Charge Conjugation on the Field and Bilinears#^thm-c9-7-2|Theorem §C9.7.2]], [[§C9.9 Time Reversal on States, Spinors and the Dirac Field#^thm-c9-9-7|Theorem §C9.9.7]].
> - **Used in**, statement by statement (C4 items):
>   - Remark (Point splitting: how a product at one point is regularized): [[§C4.5★ Energy, Momentum and the Spin-One Quanta of the Proca Field|§C4.5★]], [[§C4.5★ Energy, Momentum and the Spin-One Quanta of the Proca Field#^thm-c4-5-3|Theorem §C4.5.3]].
>   - Theorem §CA.2.8 (Products with Disjoint Singular Supports): [[§C4.4★ Quantizing the Proca Field꞉ Modes and the Mode Algebra#^thm-c4-4-7|Theorem §C4.4.7]], [[§C4.5★ Energy, Momentum and the Spin-One Quanta of the Proca Field#^thm-c4-5-6|Theorem §C4.5.6]], [[§C4.8 Covariant Quantization꞉ Modes and the Indefinite Mode Algebra#^thm-c4-8-11|Theorem §C4.8.11]], [[§C4.9 Energy, Momentum and the Indefinite Fock Space#^thm-c4-9-1|Theorem §C4.9.1]], [[§C4.5★ Energy, Momentum and the Spin-One Quanta of the Proca Field#^thm-c4-5-2|Theorem §C4.5.2]].
>   - Def. §CA.2.11 (Operator-Valued Distribution): [[§C4.4★ Quantizing the Proca Field꞉ Modes and the Mode Algebra#^rem-c4-4-1|§C4.4★, Remark: In what sense the Proca field is a distribution]].
>   - Theorem §CA.2.10 (Box Regularization of δ³(0)): [[§C4.5★ Energy, Momentum and the Spin-One Quanta of the Proca Field|§C4.5★]], [[§C4.5★ Energy, Momentum and the Spin-One Quanta of the Proca Field#^thm-c4-5-3|Theorem §C4.5.3]], [[§C4.5★ Energy, Momentum and the Spin-One Quanta of the Proca Field#^thm-c4-5-10|Theorem §C4.5.10]].
> - **Used in**, statement by statement (Electromagnetism C items):
>   - Theorem §CA.2.8 (products): the Helmholtz form of D, the force on a dielectric interface — [[§C5.2 The Field of Polarized Matter#^thm-c5-2-5|EM Theorem §C5.2.5]], [[§C5.6 Forces in Dielectrics#^ex-c5-6-2|EM Example §C5.6.2]].
>   - Theorem §CA.2.9 (θ·δ, δ², δ(0)): the self-energy of a point charge, no self-force, the average field on a surface charge — [[§C1.5 The Electromagnetic Energy–Momentum Tensor#^rem-c1-5-1|EM Remark: Point charges, and where the electrostatic energy sits]], [[§C2.1 The Static Limit and the Field of a Charge Distribution#^thm-c2-1-4|EM Theorem §C2.1.4]], [[§C2.2 Gauss's Law and the Solid Angle#^ex-c2-2-3|EM Example §C2.2.3]], [[§C2.3 Electrostatic Energy and Self-Energy#^thm-c2-3-7|EM Theorem §C2.3.7]], [[§C2.4 The Electric Stress Tensor#^thm-c2-4-3|EM Theorem §C2.4.3]], [[§C5.6 Forces in Dielectrics#^thm-c5-6-1|EM Theorem §C5.6.1]], [[§C5.6 Forces in Dielectrics#^ex-c5-6-2|EM Example §C5.6.2]].
> - **Used in** (C6a places, Lecture 14): Theorem §CA.2.9 — the contraction at coincident points and the first ultraviolet divergence ([[§C6a.5 Normal Ordering and Contractions#^cau-c6a-5-3|§C6a.5, Caution: In what sense these identities hold]], [[§C6a.10 Feynman Rules in Momentum Space#^rem-c6a-10-1|§C6a.10, Remark: The first ultraviolet divergence]]), [[§C6a.1 From Free to Interacting Fields#^rem-c6a-1-4|§C6a.1, ★ Remark: In what sense φ̂⁴(x) is defined]]; Theorem §CA.2.10 — vacuum bubbles proportional to the spacetime volume ([[§C6a.11 The iε Limit and Vacuum Bubbles#^thm-c6a-11-3|Theorem §C6a.11.3]]), [[§C6a.11 The iε Limit and Vacuum Bubbles|§C6a.11]]; Def. §CA.2.11 — [[§C6a.1 From Free to Interacting Fields#^rem-c6a-1-4|§C6a.1, ★ Remark: In what sense φ̂⁴(x) is defined]].
> - **Used in** (C6b places, Lecture 15): Theorems §CA.2.9–§CA.2.10 — Yu's box route, $(2\pi)^4\delta^4(0) = \tilde V\tilde T$, [[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-2|Theorem §C6b.2.2]], [[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-3|Theorem §C6b.2.3]], [[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-4|Theorem §C6b.2.4]], [[§C6b.5 Decay Widths#^thm-c6b-5-4|Theorem §C6b.5.4]].
> - **Used in** (C8 items, Lecture 18): Theorem §CA.2.8 — the $\delta^3$ of the photon commutator evaluates $\sqrt{2E_{\mathbf p}}/\sqrt{2E_{\mathbf q}}$ on its support in the contraction with an external photon ([[§C8.4 Feynman Rules for QED#^thm-c8-4-1|Theorem §C8.4.1]]).
> - **Used in** (C6d places): Theorem §CA.2.8 — [[§C6d.2 Contractions with External Fermions#^thm-c6d-2-1|Theorem §C6d.2.1]], [[§C6d.4 First Order#^thm-c6d-4-4|Theorem §C6d.4.4]].
