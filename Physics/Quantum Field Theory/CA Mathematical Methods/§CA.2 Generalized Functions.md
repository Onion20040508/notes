---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: CA
section: CA.2
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§CA.1 Exchanging Limits, Derivatives and Integrals]] · ↑ [[· CA Mathematical Methods]] · [[§CA.3 Fourier Transforms and Fourier Tricks]] →

*Sources: the user's PHY 513 notes, App. A §A.4 and the Sokhotski–Plemelj part of §A.5, Ch. 6 §6.2 · PHY 513, Problem Set 4, Problem 0 (generalized functions) and eq. (11) · standard results stated here, where marked: Hörmander, The Analysis of Linear Partial Differential Operators I, Ch. 2–4; Gel'fand & Shilov, Generalized Functions, Vol. 1, Ch. I; Reed & Simon, Methods of Modern Mathematical Physics I, Ch. V; Stein & Shakarchi, Functional Analysis (Princeton Lectures IV), Ch. 3; Streater & Wightman, PCT, Spin and Statistics, and All That, Ch. 3.*

The delta function, the Wightman, commutator and Feynman functions, the overlap $\langle\mathbf p|\mathbf q\rangle$ and the field operators themselves are not functions: none of them has a value at every point, and several have none anywhere. This section says what they are, continuous linear maps on test functions, and which operations on them are defined: derivatives always, products only sometimes, limits $\varepsilon \to 0^+$ whenever they converge on every test function. It starts from the working delta function of [[§B4.4 Fourier Transforms and the Delta Function#^def-b4-4-2|WO Def. §B4.4.2]] and [[§B1.2 The Dirac Delta Function and the Helmholtz Theorem#^thm-b1-2-1|EM Theorem §B1.2.1]], from the δ-normalized kets of [[§37 Position Eigenstates and Continuous Resolutions#^prop-37-3|556 Prop. §37.3]], and from the exchange theorems of [[§CA.1 Exchanging Limits, Derivatives and Integrals|§CA.1]]; the Fourier transform of a distribution is [[§CA.3 Fourier Transforms and Fourier Tricks|§CA.3]]. New here, beyond the user's App. A §A.4: the spaces $\mathcal D$ and $\mathcal S$, support and singular support, changes of variables and composition with a function, the products that exist and those that do not (among them $\delta^3(\mathbf 0)$), boundary values of analytic functions (with the Sokhotski–Plemelj formula, which is how every $i\varepsilon$ of [[§C2b.5 Green's Functions and Contours|§C2b.5]]–[[§C2b.7 Wick Rotation and the Two-Point Family|§C2b.7]] is read), fundamental solutions and operator-valued distributions. Each statement lists in Connections the places of [[· C2a The Quantum Scalar Field|C2a]] and [[· C2b Two-Point Functions, Causality and Propagators|C2b]] that use it.

## Test functions and distributions

> [!definition] Definition §CA.2.1: Test Functions: the Spaces 𝒟 and 𝒮
> On $\mathbb R^n$, with multi-indices $\alpha$, $\beta$ and the seminorms $\|\varphi\|_{\alpha,\beta} = \sup_x|x^\alpha\partial^\beta\varphi(x)|$:
> - $\mathcal D(\mathbb R^n)$ is the space of smooth $\varphi$ that vanish outside a bounded set; $\varphi_k \to \varphi$ in $\mathcal D$ if all supports lie in one bounded set and $\partial^\beta\varphi_k \to \partial^\beta\varphi$ uniformly for every $\beta$.
> - $\mathcal S(\mathbb R^n)$, the **Schwartz functions**, is the space of smooth $\varphi$ with every $\|\varphi\|_{\alpha,\beta} < \infty$; $\varphi_k \to \varphi$ in $\mathcal S$ if $\|\varphi_k - \varphi\|_{\alpha,\beta} \to 0$ for every $\alpha$, $\beta$.
>
> Examples: the bump $e^{-1/(1 - x^2)}$ for $|x| < 1$ (zero elsewhere) is in $\mathcal D(\mathbb R)$; $e^{-x^2}$ is in $\mathcal S$ but not in $\mathcal D$.
>
> *Source: standard; stated here (Hörmander I, §§1.3, 2.1, 7.1; Stein & Shakarchi, Fourier Analysis, Ch. 5–6) · the user's PHY 513 notes, App. A §A.4 (test functions), Ch. 6 §6.2 (Schwartz functions for Fourier transforms)*

^def-ca-2-1

> [!definition] Definition §CA.2.2: Generalized Function; Tempered Distribution
> A **test function** $\varphi$ is smooth and vanishes outside a bounded region (the space $\mathcal D$ of [[§CA.2 Generalized Functions#^def-ca-2-1|Def. §CA.2.1]]). A **generalized function** (distribution) $T$ is a linear map $\varphi \mapsto T[\varphi] \in \mathbb C$ on test functions (continuous: $T[\varphi_k] \to T[\varphi]$ whenever $\varphi_k \to \varphi$ in the sense of Def. §CA.2.1, which every map met here is). A locally integrable function $\psi$ defines $T_\psi[\varphi] = \int\psi\varphi$; the **delta function** is the map $\delta[\varphi] = \varphi(0)$. With **Schwartz functions** (smooth, decaying with all derivatives faster than every power) in place of test functions, the maps are **tempered distributions**. The two spaces of maps are written $\mathcal D'$ and $\mathcal S'$.
>
> *Source: the user's PHY 513 notes, App. A §A.4, Ch. 6 §6.2 · PHY 513, Problem Set 4, Problem 0*

^def-ca-2-2

> [!remark] Remark: What changes from the working delta function
> [[§B4.4 Fourier Transforms and the Delta Function#^def-b4-4-2|WO Def. §B4.4.2]] and [[§B1.2 The Dirac Delta Function and the Helmholtz Theorem#^def-b1-2-1|EM Def. §B1.2.1]] define $\delta$ by what it does under an integral and realize it as a limit of narrow peaks; the rules were checked one by one with a nascent delta. Here the map *is* the object: $\int dx\,\delta(x)\varphi(x)$ is notation for $\varphi \mapsto \varphi(0)$, chosen so that the formula for $T_\psi$ can be used uniformly. Nothing is lost by the generalization: a test function sharply peaked at $x_0$ with unit integral gives $T_\psi[\varphi] \approx \psi(x_0)$, so $\psi$ is recovered from $T_\psi$; and the generalized functions reach beyond the test functions, since $\varphi \mapsto \int\varphi$ is $T_1$ for the constant $1$. The same move appears in [[§37 Position Eigenstates and Continuous Resolutions#^prop-37-3|556 Prop. §37.3]]: a position "eigenket" is not a vector of the Hilbert space but makes sense paired with one.
>
> *Source: the user's PHY 513 notes, App. A §A.4 (Derivation "Three examples, in order of generality") · PHY 513, Problem Set 4, Problem 0*

^rem-ca-2-1

> [!theorem] Theorem §CA.2.1: Regular and Singular Tempered Distributions
> 1. $\mathcal D$ is dense in $\mathcal S$, so a tempered distribution is fixed by its action on $\mathcal D$.
> 2. If $\psi$ is locally integrable and $\int d^nx\,|\psi(x)|(1 + |x|)^{-N} < \infty$ for some $N$, then $T_\psi[\varphi] = \int\psi\varphi$ is a tempered distribution, and $\psi \mapsto T_\psi$ is injective (functions equal almost everywhere identified). Examples: $1$, $e^{i\mathbf k\cdot\mathbf x}$, $\theta(t)$, polynomials, $1/|\mathbf x|$ and $1/|\mathbf x|^2$ on $\mathbb R^3$. Not covered: $1/x$ on $\mathbb R$ (not locally integrable) and $e^x$ (too fast).
> 3. $\partial^\alpha\delta[\varphi] = (-1)^{|\alpha|}\partial^\alpha\varphi(0)$ is a tempered distribution, and it is $T_\psi$ for no locally integrable $\psi$.
>
> *Source: standard; stated here (Hörmander I, §§1.3, 2.1, 7.1; Reed & Simon I, §V.3) · the user's PHY 513 notes, App. A §A.4 (Derivation "Three examples, in order of generality")*

^thm-ca-2-1

> [!derivation]- Derivation
> **Step 1** (density). Let $\chi \in \mathcal D$ with $\chi = 1$ on $|x| \le 1$, and $\chi_R(x) = \chi(x/R)$. By the Leibniz rule,
>
> $$
> \partial^\beta\bigl[(1 - \chi_R)\varphi\bigr] = (1 - \chi_R)\,\partial^\beta\varphi - \sum_{0 < \gamma \le \beta}\binom\beta\gamma R^{-|\gamma|}(\partial^\gamma\chi)(x/R)\,\partial^{\beta - \gamma}\varphi .
> $$
>
> Every term vanishes for $|x| \le R$. For $|x| \ge R$, the first term times $x^\alpha$ is at most $\sup|1 - \chi|\cdot\sup_{|x| \ge R}|x^\alpha\partial^\beta\varphi| \le \sup|1 - \chi|\cdot R^{-1}\sup|x|\,|x^\alpha\partial^\beta\varphi|$, and $|x| \le \sum_i|x_i|$ makes the last supremum a finite sum of seminorms of $\varphi$. Each remaining term carries $R^{-|\gamma|} \le R^{-1}$ times $\sup|\partial^\gamma\chi|$ times the seminorm $\|\varphi\|_{\alpha,\beta - \gamma}$. So $\|\varphi - \chi_R\varphi\|_{\alpha,\beta} \le C_{\alpha\beta}/R \to 0$, with $\chi_R\varphi \in \mathcal D$.
>
> **Step 2** (fixed by $\mathcal D$). If $T, T' \in \mathcal S'$ agree on $\mathcal D$, then by continuity $T[\varphi] = \lim_RT[\chi_R\varphi] = \lim_RT'[\chi_R\varphi] = T'[\varphi]$.
>
> **Step 3** (regular distributions are tempered). $(1 + |x|)^N \le C_N\sum_{|\alpha| \le N}|x^\alpha|$, so
>
> $$
> |T_\psi[\varphi]| \le \int d^nx\,|\psi|(1 + |x|)^{-N}\cdot\sup_x(1 + |x|)^N|\varphi(x)| \le C\sum_{|\alpha| \le N}\|\varphi\|_{\alpha,0} .
> $$
>
> $T_\psi$ is linear, and the bound applied to $\varphi_k - \varphi$ shows that $\varphi_k \to \varphi$ in $\mathcal S$ implies $T_\psi[\varphi_k] \to T_\psi[\varphi]$.
>
> **Step 4** (injectivity; sketch). If $T_\psi = 0$, pair it with the test functions $\rho_\varepsilon(x_0 - \cdot)$ of a nascent delta function ([[§CA.2 Generalized Functions#^thm-ca-2-4|Theorem §CA.2.4]], 3, with $\rho \in \mathcal D$): $(\psi \ast  \rho_\varepsilon)(x_0) = 0$ for every $x_0$. As $\varepsilon \to 0$, $\psi \ast  \rho_\varepsilon \to \psi$ in $L^1$ on every bounded set (Lebesgue's approximation theorem; Stein & Shakarchi, Real Analysis, Ch. 3), so $\psi = 0$ almost everywhere. For continuous $\psi$ this is the peaked-test-function argument of [[§CA.2 Generalized Functions#^rem-ca-2-1|Remark: What changes from the working delta function]].
>
> **Step 5** (derivatives of δ). $|\partial^\alpha\varphi(0)| \le \|\varphi\|_{0,\alpha}$: linear and continuous. Suppose $\partial^\alpha\delta = T_\psi$. On test functions supported away from $0$ both sides give $0$, so by Step 4 (applied on $\mathbb R^n \setminus \{0\}$) $\psi = 0$ almost everywhere, and $T_\psi = 0$. But with $\chi$ of Step 1, $\partial^\alpha\delta[x^\alpha\chi] = (-1)^{|\alpha|}\partial^\alpha(x^\alpha\chi)(0) = (-1)^{|\alpha|}\alpha! \ne 0$. Contradiction.
>
> **Step 6** (the examples). $|e^{i\mathbf k\cdot\mathbf x}| = |\theta| = 1$: take $N = n + 1$. A polynomial of degree $d$: $N = d + n + 1$. On $\mathbb R^3$, $\int_{|\mathbf x| < 1}d^3x/|\mathbf x| = 4\pi\int_0^1r\,dr = 2\pi$ and $\int_{|\mathbf x| < 1}d^3x/|\mathbf x|^2 = 4\pi$, finite, and $N = 3$ handles $|\mathbf x| > 1$. On $\mathbb R$, $\int_{-1}^1dx/|x| = \infty$. For $e^x$, the Schwartz function $\varphi = e^{-\sqrt{1 + x^2}}$ gives $e^x\varphi = e^{x - \sqrt{1 + x^2}} \to 1$ as $x \to \infty$, so $\int e^x\varphi$ diverges.
>
> **What the derivation shows.**
> - Polynomial growth is exactly the price of being tempered; local integrability is where $1/x$ fails, which is why it needs the principal value ([[§CA.2 Generalized Functions#^def-ca-2-6|Def. §CA.2.6]]).
> - δ is the first distribution that is no function at all; its derivatives are the next.
> - Step 1 is why physics may test with compactly supported wave packets and still conclude statements in $\mathcal S'$.

^der-ca-2-1

*Uses:* [[§CA.2 Generalized Functions#^def-ca-2-1|Def. §CA.2.1]], [[§CA.2 Generalized Functions#^def-ca-2-2|Def. §CA.2.2]], [[§CA.2 Generalized Functions#^thm-ca-2-4|Theorem §CA.2.4]]

> [!definition] Definition §CA.2.3: Support and Singular Support
> A distribution $T$ **vanishes** on an open set $U$ if $T[\varphi] = 0$ for every $\varphi \in \mathcal D$ supported in $U$. Its **support** $\operatorname{supp}T$ is the complement of the largest open set on which $T$ vanishes; its **singular support** $\operatorname{sing\,supp}T$ is the complement of the largest open set on which $T$ equals a smooth function ($T[\varphi] = \int g\varphi$ with $g$ smooth there). Both largest sets exist (a distribution that vanishes, or is smooth, near every point of a union of open sets is so on the union: Hörmander I, §2.2).
>
> Examples: $\operatorname{supp}\delta = \operatorname{sing\,supp}\delta = \{0\}$; $\operatorname{supp}\theta = [0, \infty)$, $\operatorname{sing\,supp}\theta = \{0\}$; $\operatorname{supp}\mathcal P\frac1x = \mathbb R$, $\operatorname{sing\,supp}\mathcal P\frac1x = \{0\}$.
>
> *Source: standard; stated here (Hörmander I, §2.2; Gel'fand & Shilov 1, Ch. I)*

^def-ca-2-3

> [!theorem] Theorem §CA.2.2: Distributions Supported at a Point
> If $\operatorname{supp}T \subseteq \{a\}$, then $T = \sum_{|\alpha| \le N}c_\alpha\,\partial^\alpha\delta(x - a)$ for some $N$ and constants $c_\alpha$. A distribution known away from a point is therefore fixed up to finitely many derivatives of δ at that point.
>
> *Source: standard; stated here (Hörmander I, §2.3)*

^thm-ca-2-2

> [!derivation]- Derivation (proof sketch)
> Take $a = 0$ (translate by [[§CA.2 Generalized Functions#^def-ca-2-5|Def. §CA.2.5]]).
>
> **Step 1** (finite order; quoted). Continuity of $T$ on test functions supported in the ball $|x| \le 1$ gives $N$ and $C$ with $|T[\varphi]| \le C\sum_{|\beta| \le N}\sup|\partial^\beta\varphi|$ for all such $\varphi$ (Hörmander I, §2.1).
>
> **Step 2** (split φ). Let $\chi \in \mathcal D$ equal $1$ near $0$, supported in $|x| \le 1$, and let $P_N(x) = \sum_{|\alpha| \le N}\partial^\alpha\varphi(0)\,x^\alpha/\alpha!$ be the Taylor polynomial of $\varphi$ at $0$, $r = \varphi - P_N$. Then $\varphi = \chi P_N + \chi r + (1 - \chi)\varphi$.
>
> **Step 3** (the far piece). $(1 - \chi)\varphi$ vanishes near $0$, hence is supported away from $\operatorname{supp}T$: $T[(1 - \chi)\varphi] = 0$.
>
> **Step 4** (the remainder). $r$ and its derivatives up to order $N$ vanish at $0$, so $|\partial^\beta r(x)| \le C|x|^{N + 1 - |\beta|}$ near $0$. With $\chi_\varepsilon(x) = \chi(x/\varepsilon)$, $\chi r - \chi_\varepsilon r$ vanishes near $0$, so $T[\chi r] = T[\chi_\varepsilon r]$. By Leibniz, every derivative $\partial^\beta(\chi_\varepsilon r)$ with $|\beta| \le N$ is a sum of terms $\varepsilon^{-|\gamma|}(\partial^\gamma\chi)(x/\varepsilon)\,\partial^{\beta - \gamma}r$ supported in $|x| \le \varepsilon$, each at most $C\varepsilon^{-|\gamma|}\varepsilon^{N + 1 - |\beta| + |\gamma|} = C\varepsilon^{N + 1 - |\beta|} \le C\varepsilon$. By Step 1, $|T[\chi r]| \le C'\varepsilon$ for every $\varepsilon$: $T[\chi r] = 0$.
>
> **Step 5** (the polynomial). $T[\chi P_N] = \sum_{|\alpha| \le N}\frac{\partial^\alpha\varphi(0)}{\alpha!}T[\chi x^\alpha]$. With $\partial^\alpha\delta[\varphi] = (-1)^{|\alpha|}\partial^\alpha\varphi(0)$, this is $\sum_\alpha c_\alpha\,\partial^\alpha\delta[\varphi]$ with $c_\alpha = (-1)^{|\alpha|}T[\chi x^\alpha]/\alpha!$.
>
> **What the derivation shows.**
> - The ambiguity of a distribution at one point is a finite sum of δ-derivatives, never anything spread out.
> - This is the freedom in extending $\theta(x^0)D(x)$ across $x = 0$ ([[§CA.2 Generalized Functions#^thm-ca-2-7|Theorem §CA.2.7]]) and in contact terms of time-ordered products; for a fundamental solution the equation itself removes it ([[§CA.2 Generalized Functions#^thm-ca-2-14|Theorem §CA.2.14]], 3).

^der-ca-2-2

*Uses:* [[§CA.2 Generalized Functions#^def-ca-2-3|Def. §CA.2.3]], [[§CA.2 Generalized Functions#^def-ca-2-5|Def. §CA.2.5]]

## Operations on distributions

> [!definition] Definition §CA.2.4: Derivative, Limit and Fourier Transform of a Generalized Function
> Operations are moved onto the test function:
> - *derivative:* $T'[\varphi] \equiv -T[\varphi']$, and $\partial_\mu T[\varphi] \equiv -T[\partial_\mu\varphi]$;
> - *product with a smooth function $g$:* $(gT)[\varphi] \equiv T[g\varphi]$ (two generalized functions cannot in general be multiplied);
> - *limit:* $T_\varepsilon \to T$ means $T_\varepsilon[\varphi] \to T[\varphi]$ for every test function;
> - *Fourier transform* (tempered $T$): $\tilde T[\varphi] \equiv T[\tilde\varphi]$.
>
> *Source: the user's PHY 513 notes, App. A §A.4 (Derivation "Operations are defined by transferring them to the test function")*

^def-ca-2-4

> [!theorem] Theorem §CA.2.3: Every Generalized Function Is Differentiable
> 1. Every generalized function has derivatives of all orders, and for differentiable $\psi$, $(T_\psi)' = T_{\psi'}$.
> 2. $\theta' = \delta$ and $\delta'[\varphi] = -\varphi'(0)$.
>
> *Source: the user's PHY 513 notes, App. A §A.4*

^thm-ca-2-3

> [!derivation]- Derivation
> **Step 1** (part 1). $\varphi'$ is again a test function, so $T'[\varphi] = -T[\varphi']$ is defined, and so are all higher derivatives. For differentiable $\psi$, integration by parts gives $\int\psi'\varphi = [\psi\varphi] - \int\psi\varphi'$, and the boundary term vanishes because $\varphi$ is zero outside a bounded region.
>
> **Step 2** ($\theta' = \delta$). $\theta'[\varphi] = -\int_{-\infty}^\infty\theta\varphi' = -\int_0^\infty\varphi' = -[\varphi]_0^\infty = \varphi(0) = \delta[\varphi]$.
>
> ⚑ By-product: the jump of a step function is a delta function; this is the jump that makes the retarded function a Green's function ([[§C2b.5 Green's Functions and Contours#^thm-c2b-5-5|Theorem §C2b.5.5]], Step 6) and the contact term of time ordering ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-1|Theorem §C2b.6.1]], 4).
>
> **Step 3** ($\delta'$). $\delta'[\varphi] = -\delta[\varphi'] = -\varphi'(0)$, which is the rule of [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-8|Theorem §CA.3.8]], Step 4, seen as a definition.
>
> **What the derivation shows.**
> - Rules that look like tricks ($\theta' = \delta$, $\int e^{ikx} = 2\pi\delta$) are definitions plus one integration by parts or one inversion; the second, the transform of the constant, is [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]].

^der-ca-2-3

*Uses:* [[§CA.2 Generalized Functions#^def-ca-2-4|Def. §CA.2.4]]

> [!theorem] Theorem §CA.2.4: Distributional Limits
> Let $T_\varepsilon$, $\varepsilon > 0$, be tempered distributions.
> 1. If $T_\varepsilon[\varphi]$ converges as $\varepsilon \to 0^+$ for every $\varphi \in \mathcal S$, the limit $T[\varphi]$ is again a tempered distribution: continuity comes free.
> 2. If $T_\varepsilon \to T$, then $\partial^\alpha T_\varepsilon \to \partial^\alpha T$, and $gT_\varepsilon \to gT$ for every smooth $g$ whose derivatives grow at most polynomially. Limits and derivatives always commute for distributions.
> 3. *(Nascent delta functions)* If $\rho \in L^1(\mathbb R^n)$, $\int\rho = 1$, and $\rho_\varepsilon(x) = \varepsilon^{-n}\rho(x/\varepsilon)$, then $\rho_\varepsilon \to \delta$.
>
> *Source: 1 standard; stated here (uniform boundedness on $\mathcal S$: Reed & Simon I, Ch. V; Hörmander I, §2.1) · 2–3 the user's PHY 513 notes, App. A §A.4 (Derivation "Operations are defined by transferring them to the test function", limits) and §A.5 (the Lorentzian)*

^thm-ca-2-4

> [!derivation]- Derivation
> **Step 1** (part 1; quoted). Apply the uniform boundedness principle to a sequence $\varepsilon_k \to 0^+$: a family of continuous linear functionals on $\mathcal S$ that is bounded at every $\varphi$ is bounded by one finite sum of seminorms, $|T_{\varepsilon_k}[\varphi]| \le C\sum_{|\alpha|, |\beta| \le M}\|\varphi\|_{\alpha,\beta}$, and the bound passes to the limit. Not proved here (it uses the completeness of $\mathcal S$; Reed & Simon I, Ch. V).
>
> **Step 2** (part 2). For a fixed $\varphi \in \mathcal S$, $\partial^\alpha\varphi$ is one fixed test function, so by [[§CA.2 Generalized Functions#^def-ca-2-4|Def. §CA.2.4]]
>
> $$
> \partial^\alpha T_\varepsilon[\varphi] = (-1)^{|\alpha|}T_\varepsilon[\partial^\alpha\varphi] \longrightarrow (-1)^{|\alpha|}T[\partial^\alpha\varphi] = \partial^\alpha T[\varphi] .
> $$
>
> Likewise $g\varphi \in \mathcal S$ (Leibniz rule and the polynomial bounds), and $gT_\varepsilon[\varphi] = T_\varepsilon[g\varphi] \to T[g\varphi]$.
>
> ⚑ By-product: the exchange of a limit and a derivative, which for functions needs uniform convergence of the derivatives ([[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-3|Theorem §CA.1.3]]), is automatic here; the price is that the result is only a distribution. Example: $F_n = \sin(nr)/\sqrt n \to 0$, and $F_n' = \sqrt n\cos(nr)$ has no pointwise limit, but $\int\sqrt n\cos(nr)\varphi(r)\,dr = -\frac{1}{\sqrt n}\int\sin(nr)\varphi'(r)\,dr \to 0$ (one integration by parts, boundary terms zero): $F_n' \to 0$ as distributions.
>
> **Step 3** (part 3: substitute). For $\varphi \in \mathcal S$, put $x = \varepsilon u$, $d^nx = \varepsilon^nd^nu$:
>
> $$
> \int d^nx\,\varepsilon^{-n}\rho(x/\varepsilon)\,\varphi(x) = \int d^nu\,\rho(u)\,\varphi(\varepsilon u) .
> $$
>
> **Step 4** (part 3: limit). $\rho(u)\varphi(\varepsilon u) \to \rho(u)\varphi(0)$ for every $u$, and $|\rho(u)\varphi(\varepsilon u)| \le |\rho(u)|\sup|\varphi|$, integrable and independent of $\varepsilon$. By dominated convergence ([[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|Theorem §CA.1.1]]) the integral tends to $\varphi(0)\int\rho = \varphi(0) = \delta[\varphi]$. Only continuity of $\varphi$ at $0$ and boundedness were used, so the same holds for any bounded function continuous at $0$.
>
> **What the derivation shows.**
> - Every "$\varepsilon \to 0^+$" of C2a–C2b is a limit in the sense of part 1: a family of honest integrals that converges on each test function.
> - The shape of a nascent delta function is irrelevant; only its integral and integrability matter. The Gaussian of [[§B4.4 Fourier Transforms and the Delta Function#^def-b4-4-2|WO Def. §B4.4.2]], the Lorentzian $\varepsilon/\pi(x^2 + \varepsilon^2)$ of Sokhotski–Plemelj ([[§CA.2 Generalized Functions#^thm-ca-2-11|Theorem §CA.2.11]]) and the heat kernel of Fourier inversion ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-1|Theorem §CA.3.1]]) are three choices of $\rho$.

^der-ca-2-4

*Uses:* [[§CA.2 Generalized Functions#^def-ca-2-4|Def. §CA.2.4]], [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|Theorem §CA.1.1]], [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-3|Theorem §CA.1.3]] (for contrast)

> [!definition] Definition §CA.2.5: Linear Change of Variables; Invariant Distribution
> For an invertible real $n \times n$ matrix $A$ and $a \in \mathbb R^n$, the composition of $T$ with $x \mapsto Ax + a$ is the distribution
>
> $$
> T(Ax + a)[\varphi] \equiv |\det A|^{-1}\,T\bigl[\varphi\bigl(A^{-1}(\cdot - a)\bigr)\bigr] .
> $$
>
> $T$ is **invariant** under a group of such maps if $T(gx) = T$ for every $g$ in the group; **Lorentz invariant** if $T[\varphi\circ\Lambda^{-1}] = T[\varphi]$ for every proper orthochronous $\Lambda$ (for which $|\det\Lambda| = 1$).
>
> *Source: standard; stated here (Hörmander I, §§3.1, 6.1) · the user's PHY 513 notes, Ch. 6 §6.3 (Derivation "The rules", 3: Lorentz covariance)*

^def-ca-2-5

> [!theorem] Theorem §CA.2.5: Composition of δ with a Function
> 1. *(Linear maps)* For $T = T_\psi$ the formula of [[§CA.2 Generalized Functions#^def-ca-2-5|Def. §CA.2.5]] is the substitution rule; in particular $\delta(Ax + a) = |\det A|^{-1}\delta(x + A^{-1}a)$ and $\delta(\lambda x) = |\lambda|^{-n}\delta(x)$.
> 2. *(One variable)* Let $f$ be smooth with simple zeros $x_i$ ($f'(x_i) \ne 0$), and $\rho \in \mathcal D$ with $\int\rho = 1$. Then $\delta(f(x)) \equiv \lim_{\varepsilon\to0^+}\rho_\varepsilon(f(x))$ exists and
>
> $$
> \delta\bigl(f(x)\bigr) = \sum_i\frac{\delta(x - x_i)}{|f'(x_i)|} .
> $$
>
> 3. *(Several variables)* If $f: \mathbb R^n \to \mathbb R$ is smooth and $\nabla f \ne 0$ on $\Sigma = \{f = 0\}$, then $\delta(f)[\varphi] = \int_\Sigma\varphi\,dS/|\nabla f|$. At a zero where $\nabla f = 0$ the limit need not exist.
>
> *Source: standard; stated here (Hörmander I, §6.1; Gel'fand & Shilov 1, Ch. III) · the working form is [[§B1.2 The Dirac Delta Function and the Helmholtz Theorem#^thm-b1-2-1|EM Theorem §B1.2.1]], 1 and [[§B4.4 Fourier Transforms and the Delta Function#^thm-b4-4-3|WO Theorem §B4.4.3]], 2*

^thm-ca-2-5

> [!derivation]- Derivation
> **Step 1** (part 1). For $T = T_\psi$ substitute $y = Ax + a$, so $x = A^{-1}(y - a)$ and $d^nx = |\det A|^{-1}d^ny$ ([[§25 Change of Variables on General Domains#^thm-25-6|452 Thm. §25.6]], on growing balls, then the limit by dominated convergence); the domain $\mathbb R^n$ is unchanged:
>
> $$
> \int d^nx\,\psi(Ax + a)\,\varphi(x) = |\det A|^{-1}\int d^ny\,\psi(y)\,\varphi\bigl(A^{-1}(y - a)\bigr) .
> $$
>
> This is Def. §CA.2.5 for $T_\psi$. For δ: $\delta(Ax + a)[\varphi] = |\det A|^{-1}\varphi(A^{-1}(0 - a)) = |\det A|^{-1}\varphi(-A^{-1}a)$, which is $|\det A|^{-1}\delta(x + A^{-1}a)[\varphi]$. With $A = \lambda\mathbb 1$, $|\det A| = |\lambda|^n$.
>
> **Step 2** (part 2: localize). Let $\varphi \in \mathcal D$ vanish outside $[-L, L]$ and let $\rho$ vanish outside $[-1, 1]$. Simple zeros are isolated, so $[-L, L]$ contains finitely many, $x_1, \dots, x_k$; choose disjoint open intervals $U_i \ni x_i$ on which $|f'| \ge \frac12|f'(x_i)|$. On the compact rest of $[-L, L]$, $|f| \ge c > 0$; for $\varepsilon < c$, $\rho_\varepsilon(f(x)) = \varepsilon^{-1}\rho(f(x)/\varepsilon) = 0$ there. Only the $U_i$ contribute.
>
> **Step 3** (part 2: substitute). On $U_i$, $f$ is strictly monotone, so $u = f(x)$ is a valid substitution with inverse $x(u)$ and $dx = du/|f'(x(u))|$: the absolute value appears because, for decreasing $f$, the limits of integration flip and absorb the sign of $f'$.
>
> $$
> \int_{U_i}dx\,\varepsilon^{-1}\rho\bigl(f(x)/\varepsilon\bigr)\varphi(x) = \int_{f(U_i)}du\,\varepsilon^{-1}\rho(u/\varepsilon)\,g_i(u), \qquad g_i(u) = \frac{\varphi(x(u))}{|f'(x(u))|} .
> $$
>
> **Step 4** (part 2: limit). $g_i$ is bounded and continuous at $u = 0$ with $g_i(0) = \varphi(x_i)/|f'(x_i)|$, and $f(U_i)$ contains a neighbourhood of $0$. By [[§CA.2 Generalized Functions#^thm-ca-2-4|Theorem §CA.2.4]], 3 (with its closing remark), the integral tends to $g_i(0)$. Summing over $i$ gives the formula; the result does not depend on $\rho$.
>
> ⚑ By-product: $\delta(f)$ depends on the function $f$, not only on its zero set: $\delta(2f) = \frac12\delta(f)$. That is why $\delta(p^2 - m^2)$ and $\delta(p^0 - E_{\mathbf p})$ differ by $2E_{\mathbf p}$, the Jacobian of the invariant measure → [[§CA.2 Generalized Functions#^thm-ca-2-6|Theorem §CA.2.6]].
>
> **Step 5** (part 3; sketch). Near a point of $\Sigma$ where $\partial_nf \ne 0$, the implicit function theorem gives coordinates $(y', u)$ with $u = f(x)$, in which $d^nx = dS\,du/|\nabla f|$ (the coarea formula). Steps 2–4 then run in the variable $u$ with $y'$ as a parameter, and give $\int_\Sigma\varphi\,dS/|\nabla f|$.
>
> **Step 6** (a critical zero). For $f(x) = x^2$ on $\mathbb R$, $f'(0) = 0$. With $x = \sqrt{\varepsilon v}$ on $x > 0$, $dx = \sqrt\varepsilon\,dv/2\sqrt v$, and $\int_0^\infty\varepsilon^{-1}\rho(x^2/\varepsilon)\varphi(x)\,dx = \frac{1}{2\sqrt\varepsilon}\int_0^\infty\rho(v)\varphi(\sqrt{\varepsilon v})\frac{dv}{\sqrt v}$, which diverges like $\varepsilon^{-1/2}$ when $\varphi(0) \ne 0$ and $\int_0^\infty\rho(v)v^{-1/2}dv \ne 0$: $\delta(x^2)$ does not exist on $\mathbb R$.
>
> **What the derivation shows.**
> - Composition is a limit, and it needs only simple zeros; $1/|f'(x_i)|$ is the Jacobian of the substitution, which blows up at a critical zero.
> - In four dimensions $x^2 = (x^0)^2 - \mathbf x^2$ has its only critical point at the origin, where the singularity turns out to be integrable: $\delta(x^2)$ exists on $\mathbb R^4$ ([[§CA.2 Generalized Functions#^thm-ca-2-6|Theorem §CA.2.6]], 2).

^der-ca-2-5

*Uses:* [[§CA.2 Generalized Functions#^def-ca-2-5|Def. §CA.2.5]], [[§CA.2 Generalized Functions#^thm-ca-2-4|Theorem §CA.2.4]], [[§25 Change of Variables on General Domains#^thm-25-6|452 Thm. §25.6]]

> [!theorem] Theorem §CA.2.6: Invariant Distributions on the Mass Shell and the Light Cone
> Let $m > 0$ and $E_{\mathbf p} = \sqrt{\mathbf p^2 + m^2}$.
> 1. $\theta(\pm p^0)\,\delta(p^2 - m^2)$ is a tempered distribution on $\mathbb R^4$, acting as $\varphi \mapsto \int d^3p\,\varphi(\pm E_{\mathbf p}, \mathbf p)/2E_{\mathbf p}$, and it is Lorentz invariant.
> 2. In position space, with $r = |\mathbf x|$, $\theta(\pm x^0)\,\delta(x^2)$ is a tempered distribution acting as $\varphi \mapsto \int d^3x\,\varphi(\pm r, \mathbf x)/2r$; it is the limit $\mu \to 0^+$ of $\theta(\pm x^0)\delta(x^2 - \mu^2)$, and it is Lorentz invariant; so is $\operatorname{sgn}(x^0)\,\delta(x^2)$.
> 3. $\theta(p^0)$ by itself is not Lorentz invariant.
>
> *Source: the user's PHY 513 notes, Ch. 4 §4.9 (the invariant measure), Ch. 6 §6.3 (Principle "Free fields live on the mass shell") · stated here as distributions (standard: Gel'fand & Shilov 1, Ch. III)*

^thm-ca-2-6

> [!derivation]- Derivation
> **Step 1** (the $p^0$ integral at fixed $\mathbf p$). $f(p^0) = (p^0)^2 - E_{\mathbf p}^2$ has the simple zeros $\pm E_{\mathbf p}$, with $|f'(\pm E_{\mathbf p})| = 2E_{\mathbf p} \ge 2m > 0$. By [[§CA.2 Generalized Functions#^thm-ca-2-5|Theorem §CA.2.5]], 2,
>
> $$
> \delta(p^2 - m^2) = \frac{\delta(p^0 - E_{\mathbf p}) + \delta(p^0 + E_{\mathbf p})}{2E_{\mathbf p}} .
> $$
>
> The product with $\theta(\pm p^0)$ is defined because $\theta$ is constant near $\pm E_{\mathbf p} \ne 0$ ([[§CA.2 Generalized Functions#^thm-ca-2-7|Theorem §CA.2.7]], 2); it keeps one root: $\int dp^0\,\theta(\pm p^0)\delta(p^2 - m^2)\varphi(p^0, \mathbf p) = \varphi(\pm E_{\mathbf p}, \mathbf p)/2E_{\mathbf p}$. The same result follows from part 3 of Theorem §CA.2.5 in all four variables, since $\nabla(p^2 - m^2) = 2(p^0, -\mathbf p) \ne 0$ on the shell ($p^0 = \pm E_{\mathbf p} \ne 0$).
>
> **Step 2** (tempered). Write $T_\pm[\varphi] = \int d^3p\,\varphi(\pm E_{\mathbf p}, \mathbf p)/2E_{\mathbf p}$. With $|\varphi(p)| \le (1 + |p|)^{-4}\sup_q(1 + |q|)^4|\varphi(q)|$, $|p| \ge |\mathbf p|$ and $1/2E_{\mathbf p} \le 1/2m$,
>
> $$
> |T_\pm[\varphi]| \le \frac{1}{2m}\int\frac{d^3p}{(1 + |\mathbf p|)^4}\cdot\sup_q(1 + |q|)^4|\varphi(q)| ,
> $$
>
> and the integral is finite ($4\pi\int_0^\infty p^2dp/(1 + p)^4 < \infty$). As in [[§CA.2 Generalized Functions#^thm-ca-2-1|Theorem §CA.2.1]], Step 3, $T_\pm$ is continuous on $\mathcal S$.
>
> **Step 3** (invariance, upper shell). For proper orthochronous $\Lambda$, [[§CA.2 Generalized Functions#^def-ca-2-5|Def. §CA.2.5]] gives $T_+(\Lambda p)[\varphi] = T_+[\varphi\circ\Lambda^{-1}] = \int\frac{d^3p}{2E_{\mathbf p}}\,\varphi\bigl(\Lambda^{-1}(E_{\mathbf p}, \mathbf p)\bigr)$. The measure $d^3p/2E_{\mathbf p}$ on the upper shell is invariant ([[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-4|Theorem §C2a.4.4]], 2, applied to the function $F = \varphi\circ\Lambda^{-1}$), so this equals $\int\frac{d^3p}{2E_{\mathbf p}}\varphi(E_{\mathbf p}, \mathbf p) = T_+[\varphi]$.
>
> **Step 4** (lower shell). Let $\psi(p) = \varphi(-p)$. Then $\varphi(-E_{\mathbf p}, \mathbf p) = \psi(E_{\mathbf p}, -\mathbf p)$, and relabelling $\mathbf p \to -\mathbf p$ (Jacobian $1$, $E_{-\mathbf p} = E_{\mathbf p}$; [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|Theorem §CA.3.7]]) gives $T_-[\varphi] = T_+[\psi]$. Since $\Lambda$ is linear, $(\varphi\circ\Lambda^{-1})(-p) = \varphi(\Lambda^{-1}(-p)) = (\psi\circ\Lambda^{-1})(p)$, so $T_-[\varphi\circ\Lambda^{-1}] = T_+[\psi\circ\Lambda^{-1}] = T_+[\psi] = T_-[\varphi]$ by Step 3.
>
> **Step 5** (light cone: the limit). Steps 1–4 with $x$ in place of $p$ and $\mu$ in place of $m$ define the invariant distributions $T^\mu_\pm[\varphi] = \int d^3x\,\varphi(\pm\sqrt{r^2 + \mu^2}, \mathbf x)/2\sqrt{r^2 + \mu^2}$. As $\mu \to 0^+$ the integrand tends to $\varphi(\pm r, \mathbf x)/2r$ for $r > 0$ and is bounded by $\frac{1}{2r}(1 + r)^{-4}\sup(1 + |q|)^4|\varphi(q)|$, integrable on $\mathbb R^3$ because $\int_{r < 1}d^3x/2r = \pi$. By dominated convergence $T^\mu_\pm[\varphi] \to \int d^3x\,\varphi(\pm r, \mathbf x)/2r$; by [[§CA.2 Generalized Functions#^thm-ca-2-4|Theorem §CA.2.4]], 1 the limit is tempered.
>
> ⚑ By-product: at the origin $\nabla(x^2) = 0$ and Theorem §CA.2.5, 3 does not apply; $\delta(x^2)$ is *defined* there by this limit, and it exists only because $1/r$ is integrable in three dimensions (contrast Theorem §CA.2.5, Step 6, on $\mathbb R$).
>
> **Step 6** (light cone: invariance). Each $T^\mu_\pm$ is invariant (Steps 3–4), so $T^\mu_\pm[\varphi\circ\Lambda^{-1}] = T^\mu_\pm[\varphi]$; both sides converge as $\mu \to 0^+$ (Step 5, applied to $\varphi\circ\Lambda^{-1}$ and to $\varphi$), so the limits agree. $\operatorname{sgn}(x^0)\delta(x^2) = T^0_+ - T^0_-$ is invariant as a difference of invariant distributions.
>
> **Step 7** (part 3). For spacelike $p = (a, b, 0, 0)$ with $0 < a < b$, the boost with velocity $v$ along $x^1$, $a/b < v < 1$, gives $p'^0 = \gamma(a - vb) < 0$. So $\theta(p^0)$ changes value on an open set of spacelike $p$; only on timelike and null vectors is the sign of $p^0$ invariant, which is why the products with $\delta(p^2 - m^2)$ and $\delta(x^2)$ are.
>
> **What the derivation shows.**
> - The invariant measure $d^3p/2E_{\mathbf p}$ is the action of an invariant distribution; $1/2E_{\mathbf p}$ is the Jacobian of Theorem §CA.2.5.
> - Assumptions: $m > 0$ for the shell (so the zeros are simple and $1/2E_{\mathbf p}$ is bounded), proper orthochronous $\Lambda$.
> - The light-cone distribution $\operatorname{sgn}(x^0)\delta(x^2)$ is the massless commutator function ([[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-8|Theorem §C2b.4.8]]).

^der-ca-2-6

*Uses:* [[§CA.2 Generalized Functions#^thm-ca-2-5|Theorem §CA.2.5]], [[§CA.2 Generalized Functions#^def-ca-2-5|Def. §CA.2.5]], [[§CA.2 Generalized Functions#^thm-ca-2-1|Theorem §CA.2.1]], [[§CA.2 Generalized Functions#^thm-ca-2-4|Theorem §CA.2.4]], [[§CA.2 Generalized Functions#^thm-ca-2-7|Theorem §CA.2.7]], [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-4|Theorem §C2a.4.4]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|Theorem §CA.3.7]]

## Products

> [!theorem] Theorem §CA.2.7: Products with Disjoint Singular Supports
> 1. If $g$ is smooth, $gT$ is defined for every $T \in \mathcal D'$; if moreover every derivative of $g$ grows at most polynomially, $gT \in \mathcal S'$ for every $T \in \mathcal S'$ ([[§CA.2 Generalized Functions#^def-ca-2-4|Def. §CA.2.4]]).
> 2. If $\operatorname{sing\,supp}S \cap \operatorname{sing\,supp}T = \emptyset$, the product $ST$ is defined, uniquely, by being $gT$ near every point where $S = g$ is smooth and $hS$ near every point where $T = h$ is smooth.
> 3. In general there is no product: no associative product of distributions extends multiplication by smooth functions and contains δ and $\mathcal P\frac1x$, because $(x\,\delta)\,\mathcal P\frac1x = 0$ while $\delta\,(x\,\mathcal P\frac1x) = \delta$.
>
> *Source: standard; stated here (Hörmander I, §§2.2, 8.2; L. Schwartz's impossibility theorem in its elementary form) · the user's PHY 513 notes, Ch. 6 §6.2 ("Why this matters beyond tidiness": products)*

^thm-ca-2-7

> [!derivation]- Derivation
> **Step 1** (part 1). For $\varphi \in \mathcal D$, $g\varphi \in \mathcal D$; for $\varphi \in \mathcal S$ and polynomially bounded derivatives of $g$, the Leibniz rule bounds each $\|g\varphi\|_{\alpha,\beta}$ by finitely many seminorms of $\varphi$, so $g\varphi \in \mathcal S$ and $\varphi \mapsto T[g\varphi]$ is continuous.
>
> **Step 2** (part 2: cover). Every point has an open neighbourhood on which $S$ or $T$ is smooth, because no point lies in both singular supports.
>
> **Step 3** (part 2: patch). Take a locally finite cover by such neighbourhoods $U_j$ and a partition of unity $\sum_j\chi_j = 1$ with $\chi_j \in \mathcal D$ supported in $U_j$. Define $(ST)[\varphi] = \sum_jP_j[\chi_j\varphi]$, with $P_j = g_jT$ if $S = g_j$ on $U_j$ and $P_j = h_jS$ if $T = h_j$ there. Each term is defined by Step 1, and for $\varphi \in \mathcal D$ only finitely many terms are nonzero.
>
> **Step 4** (part 2: consistency; sketch). Where both are smooth, $S = g$ and $T = h$, the two prescriptions agree: $gT[\psi] = \int hg\psi = hS[\psi]$. Hence the result does not depend on the cover or the partition (the full bookkeeping is Hörmander I, §2.2).
>
> **Step 5** (part 3: $x\,\mathcal P\frac1x = 1$). By Def. §CA.2.4 and the second form of [[§CA.2 Generalized Functions#^def-ca-2-6|Def. §CA.2.6]] applied to $x\varphi(x)$, which vanishes at $0$: $(x\,\mathcal P\frac1x)[\varphi] = \mathcal P\frac1x[x\varphi] = \int_{-L}^{L}\frac{x\varphi(x) - 0}{x}\,dx = \int\varphi = T_1[\varphi]$.
>
> **Step 6** (part 3: $x\,\delta = 0$). $(x\,\delta)[\varphi] = \delta[x\varphi] = 0\cdot\varphi(0) = 0$.
>
> **Step 7** (part 3: the contradiction). An associative product would give $\delta = \delta\cdot1 = \delta\,(x\,\mathcal P\frac1x) = (\delta\,x)\,\mathcal P\frac1x = 0\cdot\mathcal P\frac1x = 0$, which is false. Here δ and $\mathcal P\frac1x$ share the singular point $0$, which part 2 excludes.
>
> **What the derivation shows.**
> - A product is defined exactly when at each point at least one factor is smooth; at a common singular point no value is canonical and a regularization must choose one ([[§CA.2 Generalized Functions#^thm-ca-2-8|Theorem §CA.2.8]]).
> - $\theta(x^0)D(x)$: $\operatorname{sing\,supp}\theta(x^0)$ is the hyperplane $x^0 = 0$ and $\operatorname{sing\,supp}D$ is the light cone; they meet only at $x = 0$. So the product is defined on $\mathbb R^4 \setminus \{0\}$; an extension across $0$ exists (the slice-by-slice definition, [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-6|Theorem §C2b.5.6]]), any two extensions differ by $\sum c_\alpha\partial^\alpha\delta^4$ ([[§CA.2 Generalized Functions#^thm-ca-2-2|Theorem §CA.2.2]]), and the Green's-function equation removes even that freedom ([[§CA.2 Generalized Functions#^thm-ca-2-14|Theorem §CA.2.14]], 3). Equivalently, by power counting: $D$ scales like $|x|^{-2}$ at the origin, every $\partial^\alpha\delta^4$ at least like $|x|^{-4}$, so exactly one extension is no more singular than $D$ itself (scaling degree $2 < 4$; Brunetti–Fredenhagen, Commun. Math. Phys. 208 (2000), Thm. 5.2; quoted).

^der-ca-2-7

*Uses:* [[§CA.2 Generalized Functions#^def-ca-2-3|Def. §CA.2.3]], [[§CA.2 Generalized Functions#^def-ca-2-4|Def. §CA.2.4]], [[§CA.2 Generalized Functions#^def-ca-2-6|Def. §CA.2.6]]

> [!theorem] Theorem §CA.2.8: Products Without a Value: θ·δ, δ² and δ(0)
> Let $\rho, \sigma \in \mathcal D(\mathbb R)$ be nonnegative with unit integral, $\delta_\varepsilon = \rho_\varepsilon$ and $\theta_\varepsilon(x) = \int_{-\infty}^x\sigma_\varepsilon$.
> 1. $\theta_\varepsilon\delta_\varepsilon \to c\,\delta$ with $c = \int\rho(u)\Sigma(u)\,du$, $\Sigma(u) = \int_{-\infty}^u\sigma$. For $\sigma = \rho$, $c = \frac12$; as $\rho$ and $\sigma$ vary, $c$ takes every value in $[0, 1]$. So "$\theta(0)$", and with it $\theta\cdot\delta$, has no value.
> 2. $\delta_\varepsilon^2[\varphi] = \varepsilon^{-1}\varphi(0)\int\rho^2 + o(\varepsilon^{-1}) \to \infty$ whenever $\varphi(0) \ne 0$: $\delta^2$ does not exist.
> 3. $\delta^n_\varepsilon(0) = \varepsilon^{-n}\rho(0)$ in $n$ dimensions: δ evaluated at its singular point has no value. The $\delta^3(\mathbf 0)$ of a mode sum is this evaluation; it acquires a meaning only through a regularization ([[§CA.2 Generalized Functions#^thm-ca-2-9|Theorem §CA.2.9]]).
>
> *Source: standard; stated here · the user's PHY 513 notes, Ch. 6 §6.2 ("Why this matters beyond tidiness"), Ch. 4 §4.6 (the $\delta^3(0)$ of the zero-point energy)*

^thm-ca-2-8

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
> ⚑ By-product: the convention $\theta(0) = \frac12$ is the choice of one and the same smoothing for both factors (Step 2), not a fact → [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^cau-c2b-6-1|§C2b.6, Caution: The step function at zero]].
>
> **Step 4** (part 2). $\int dx\,\varepsilon^{-2}\rho(x/\varepsilon)^2\varphi(x) = \varepsilon^{-1}\int du\,\rho(u)^2\varphi(\varepsilon u)$ (substitute $x = \varepsilon u$), and the last integral tends to $\varphi(0)\int\rho^2 > 0$ by dominated convergence. So the pairing grows like $\varepsilon^{-1}$.
>
> **Step 5** (part 3). $\rho_\varepsilon(0) = \varepsilon^{-n}\rho(0/\varepsilon) = \varepsilon^{-n}\rho(0)$, divergent and dependent on $\rho$. In the plane-wave representation, $(2\pi)^3\delta^3(\mathbf k) = \int d^3x\,e^{i\mathbf k\cdot\mathbf x}$ at $\mathbf k = \mathbf 0$ is $\int d^3x\,1$, the volume of space: the regularization of Theorem §CA.2.9.
>
> **What the derivation shows.**
> - At a common singular point the answer depends on how the factors were smoothed: the hallmark of an undefined product.
> - Where C2a–C2b meet each case: $\theta\cdot\delta$ in the time derivative of a time-ordered product, where it multiplies an equal-time commutator ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-1|Theorem §C2b.6.1]]); $\delta^3(\mathbf 0)$ in the zero-point energy ([[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-3|Theorem §C2a.3.3]]); $\phi(x)^2$ at one point, whose vacuum part is the Wightman function at coincident points ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^rem-c2b-6-3|Remark: The zero-point energy is the Wightman function at coincident points]]).

^der-ca-2-8

*Uses:* [[§CA.2 Generalized Functions#^thm-ca-2-4|Theorem §CA.2.4]], [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|Theorem §CA.1.1]]

> [!theorem] Theorem §CA.2.9: Box Regularization of δ³(0)
> In a cube of side $L$ and volume $V = L^3$ with periodic boundary conditions, the momenta are $\mathbf k \in (2\pi/L)\mathbb Z^3$ and
>
> $$
> \int_Vd^3x\,e^{i(\mathbf k - \mathbf k')\cdot\mathbf x} = V\,\delta_{\mathbf k\mathbf k'} .
> $$
>
> As $L \to \infty$, $\sum_{\mathbf k} \leftrightarrow V\int\frac{d^3k}{(2\pi)^3}$ and $V\delta_{\mathbf k\mathbf k'} \leftrightarrow (2\pi)^3\delta^3(\mathbf k - \mathbf k')$. The coincident value is then $(2\pi)^3\delta^3(\mathbf 0) \leftrightarrow V$: a quantity proportional to $\delta^3(\mathbf 0)$ is proportional to the volume, and its density is finite or not according to the remaining integral.
>
> *Source: the user's PHY 513 notes, Ch. 4 §4.6 ("$(2\pi)^3\delta^3(0) = \int d^3x = V$ is the volume of space"), Ch. 4 §4.5 (discrete modes) · standard*

^thm-ca-2-9

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
> **Step 5** (the coincident value). At $\mathbf k = \mathbf k'$ the box gives $V\delta_{\mathbf k\mathbf k} = V$, where $(2\pi)^3\delta^3(\mathbf 0)$ itself has no value ([[§CA.2 Generalized Functions#^thm-ca-2-8|Theorem §CA.2.8]], 3). Equivalently, $\int_Vd^3x\,e^{i\mathbf 0\cdot\mathbf x} = V$.
>
> ⚑ By-product: the zero-point energy $\frac12(2\pi)^3\delta^3(\mathbf 0)\int\frac{d^3k}{(2\pi)^3}E_{\mathbf k}$ becomes $V\int\frac{d^3k}{(2\pi)^3}\frac{E_{\mathbf k}}2$, a volume times an energy density, and the density is still divergent at large $\mathbf k$ → [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-3|Theorem §C2a.3.3]].
>
> **What the derivation shows.**
> - $\delta^3(\mathbf 0)$ is an infrared divergence, the volume of space; it is a different divergence from the ultraviolet one of $\int d^3k\,E_{\mathbf k}$.
> - In a box only densities and differences have a limit as $L \to \infty$; the box is a regularization, removed at the end.

^der-ca-2-9

*Uses:* [[§CA.2 Generalized Functions#^thm-ca-2-8|Theorem §CA.2.8]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]]

> [!remark] Remark: Point splitting: how a product at one point is regularized
> For $x \ne y$, $\phi(x)\phi(y)$ is a well-defined operator-valued distribution in the pair $(x, y)$; its vacuum expectation value is $D_W(x - y)$ ([[§C2b.2 The Wightman Function#^def-c2b-2-1|Def. §C2b.2.1]]). The product at one point is the limit $y \to x$, which does not exist: $D_W(x - y)$ grows like $1/4\pi^2|(x - y)^2|$ as the points approach ([[§C2b.3 Explicit Forms of the Wightman Function|§C2b.3]]). Subtracting the vacuum part first, $:\!\phi(x)^2\!: = \lim_{y\to x}\bigl[\phi(x)\phi(y) - D_W(x - y)\bigr]$, leaves a finite operator-valued distribution: this is normal ordering ([[§C2a.3 Energy, Momentum and the Zero-Point Energy#^def-c2a-3-1|Def. §C2a.3.1]]), and the subtracted $c$-number, differentiated in $x$ and $y$ before the points meet, gives the zero-point energy density ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^rem-c2b-6-3|Remark: The zero-point energy is the Wightman function at coincident points]]). The box ([[§CA.2 Generalized Functions#^thm-ca-2-9|Theorem §CA.2.9]]) regularizes the volume; point splitting regularizes the coincident point.
>
> *Source: standard; stated here · the user's PHY 513 notes, Ch. 6 §6.2 ("Why this matters beyond tidiness"), Ch. 6 §6.7 (the zero-point energy as the Wightman function at coincident points)*

^rem-ca-2-2

## Boundary values of analytic functions

> [!definition] Definition §CA.2.6: Principal Value
> For a test function $\varphi$ vanishing outside $[-L, L]$,
>
> $$
> \mathcal P\!\!\int\frac{\varphi(s)}{s}\,ds \equiv \lim_{\delta\to0^+}\Bigl(\int_{-\infty}^{-\delta} + \int_\delta^\infty\Bigr)\frac{\varphi(s)}{s}\,ds = \int_{-L}^{L}\frac{\varphi(s) - \varphi(0)}{s}\,ds .
> $$
>
> The generalized function $\mathcal P\frac1s$ so defined is real and odd and acts as $1/s$ away from $s = 0$.
>
> *Source: the user's PHY 513 notes, App. A §A.5 (Definition "The principal value")*

^def-ca-2-6

> [!theorem] Theorem §CA.2.10: Boundary Values of Analytic Functions Are Distributions
> 1. Let $F$ be analytic on the strip $0 < \operatorname{Im}z < y_0$ with $|F(x + iy)| \le C(1 + |x|)^Ny^{-k}$ there. Then $F(x + i0) \equiv \lim_{y\to0^+}F(\cdot + iy)$ exists in $\mathcal S'(\mathbb R)$, and it is the $(k + 1)$-th derivative of a continuous, polynomially bounded function. The same holds from below.
> 2. In $n$ variables: if $F$ is analytic on the tube $\mathbb R^n + i\Gamma$ over an open convex cone $\Gamma$, with a bound polynomial in $x$ and in the inverse distance to the boundary, then $\lim_{\eta\to0,\ \eta\in\Gamma}F(\cdot + i\eta)$ exists in $\mathcal S'(\mathbb R^n)$ and does not depend on the direction of approach within $\Gamma$.
>
> *Source: standard; stated here (Hörmander I, §3.1; Streater & Wightman, Ch. 2) · the user's PHY 513 notes, App. A §A.4 (limits; the boundary value defining the Wightman function), Ch. 5 §5.4*

^thm-ca-2-10

> [!derivation]- Derivation
> Part 1; take $y_0 = 2$ and the upper side.
>
> **Step 1** (primitives). The strip is simply connected, so $F$ has analytic primitives ([[§CA.4 Contour Integration#^thm-ca-4-2|Theorem §CA.4.2]]: integrals between two points do not depend on the path). Put $z_{\ast} = i$ and define $G_0 = F$, $G_{j+1}(z) = \int_{z_{\ast}}^zG_j(w)\,dw$; then $G_{k+1}^{(k+1)} = F$.
>
> **Step 2** (each integration lowers the blow-up by one). Integrate along the path $z_{\ast} \to x + i \to x + iy$, horizontal, then vertical. If $|G_j(x + it)| \le C_j(1 + |x|)^{M_j}t^{-k_j}$ for $0 < t \le 1$, the horizontal piece is at most $C_j(1 + |x|)^{M_j + 1}$ and the vertical piece is $\int_y^1C_j(1 + |x|)^{M_j}t^{-k_j}dt$, which is $\le C(1 + |x|)^{M_j}y^{-(k_j - 1)}$ if $k_j \ge 2$, $\le C(1 + |x|)^{M_j}(1 + \ln\frac1y)$ if $k_j = 1$, and bounded if $k_j = 0$. After $k$ integrations $|G_k| \le C(1 + |x|)^{M}(1 + \ln\frac1y)$.
>
> **Step 3** (continuity up to the axis). $G_{k+1}(x + iy) = G_{k+1}(x + i) - i\int_y^1G_k(x + it)\,dt$, and $|G_k(x + it)| \le C(1 + |x|)^M(1 + \ln\frac1t)$ is integrable at $t = 0$. By dominated convergence $G_{k+1}(x + iy) \to G(x)$ as $y \to 0^+$, $G$ is continuous, and $|G_{k+1}(x + iy)| \le C'(1 + |x|)^{M + 1}$ uniformly in $0 < y \le 1$.
>
> **Step 4** (pair with a test function). On a horizontal line the complex derivative is $\partial_x$, so for $\varphi \in \mathcal S$, with $k + 1$ integrations by parts (the boundary terms vanish: $G_j$ grow polynomially, $\varphi^{(i)}$ decay faster than any power),
>
> $$
> \int dx\,F(x + iy)\,\varphi(x) = \int dx\,\partial_x^{k+1}G_{k+1}(x + iy)\,\varphi(x) = (-1)^{k+1}\int dx\,G_{k+1}(x + iy)\,\varphi^{(k+1)}(x) .
> $$
>
> **Step 5** (the limit). The integrand converges pointwise to $G(x)\varphi^{(k+1)}(x)$ and is bounded by $C'(1 + |x|)^{M+1}|\varphi^{(k+1)}(x)|$, integrable and independent of $y$. By dominated convergence the pairing tends to $(-1)^{k+1}\int G\varphi^{(k+1)} = \partial^{k+1}T_G[\varphi]$ ([[§CA.2 Generalized Functions#^def-ca-2-4|Def. §CA.2.4]]), a tempered distribution by [[§CA.2 Generalized Functions#^thm-ca-2-1|Theorem §CA.2.1]], 2.
>
> ⚑ By-product: every boundary value is a finite-order derivative of a continuous function, the order fixed by how fast $F$ blows up at the real axis. Example: $|1/(x + iy)| \le y^{-1}$, $k = 1$, and $1/(x + i0)$ is the derivative of $\log(x + i0)$ ([[§CA.2 Generalized Functions#^thm-ca-2-12|Theorem §CA.2.12]]).
>
> **Step 6** (part 2; sketch). Fix $\eta \in \Gamma$ and run Steps 1–5 in the single complex variable $\tau$ of $F(x + \tau\eta)$, uniformly in $x$; independence of the direction follows because $F$ is analytic between any two directions of $\Gamma$ (Hörmander I, §3.1).
>
> **What the derivation shows.**
> - The "$+i0$" of a boundary value is a limit in $\mathcal S'$; nothing is assigned a value at $\varepsilon = 0$. Analyticity and a polynomial bound are all that is needed.
> - Instances in C2a–C2b: the Wightman function from the lower half $\xi^0$-plane ([[§C2b.2 The Wightman Function#^thm-c2b-2-5|Theorem §C2b.2.5]]), $1/(x \pm i0)$, and the Feynman propagator, analytic in $p^0$ off the two shifted poles.

^der-ca-2-10

*Uses:* [[§CA.4 Contour Integration#^thm-ca-4-2|Theorem §CA.4.2]], [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|Theorem §CA.1.1]], [[§CA.2 Generalized Functions#^def-ca-2-4|Def. §CA.2.4]], [[§CA.2 Generalized Functions#^thm-ca-2-1|Theorem §CA.2.1]]

> [!theorem] Theorem §CA.2.11: Sokhotski–Plemelj Formula
> As generalized functions, for $\varepsilon \to 0^+$,
>
> $$
> \frac{1}{x - x_0 \pm i\varepsilon} \longrightarrow \mathcal P\frac{1}{x - x_0} \mp i\pi\,\delta(x - x_0) .
> $$
>
> Mnemonic: the pole of $1/(x - x_0 - i\varepsilon)$ lies *above* the real path and gives $+i\pi$; a pole below gives $-i\pi$.
>
> *Source: the user's PHY 513 notes, App. A §A.5, eq. (SP) and Derivation "The Sokhotski–Plemelj formula, derived directly" · PHY 513, Problem Set 4, eq. (11)*

^thm-ca-2-11

> [!derivation]- Derivation
> Take the lower sign with $s = x - x_0$; the upper sign is the complex conjugate. Let $\varphi$ be a test function vanishing outside $[-L, L]$.
>
> **Step 1** (split at finite $\varepsilon$). Multiply numerator and denominator by $s + i\varepsilon$:
>
> $$
> \frac{1}{s - i\varepsilon} = \frac{s + i\varepsilon}{s^2 + \varepsilon^2} = \underbrace{\frac{s}{s^2 + \varepsilon^2}}_{\text{real, odd}} + i\,\underbrace{\frac{\varepsilon}{s^2 + \varepsilon^2}}_{\text{real, even}} .
> $$
>
> Both pieces are bounded for $\varepsilon > 0$, but neither has a pointwise limit at $s = 0$, where both are of order $1/\varepsilon$.
>
> **Step 2** (imaginary part: substitute). With $s = \varepsilon u$, $ds = \varepsilon\,du$: $\int\varphi(s)\frac{\varepsilon\,ds}{s^2 + \varepsilon^2} = \int\varphi(\varepsilon u)\frac{du}{1 + u^2}$.
>
> **Step 3** (imaginary part: limit). $\varphi(\varepsilon u) \to \varphi(0)$ for every $u$, and $|\varphi(\varepsilon u)|/(1 + u^2) \le \sup|\varphi|/(1 + u^2)$, integrable and independent of $\varepsilon$. By dominated convergence ([[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|Theorem §CA.1.1]]) the integral tends to $\varphi(0)\int\frac{du}{1 + u^2} = \pi\varphi(0)$ ([[§CA.4 Contour Integration#^ex-ca-4-1|Example §CA.4.1]]). So $\frac{\varepsilon}{s^2 + \varepsilon^2} \to \pi\delta(s)$: the Lorentzian is a nascent delta function of area $\pi$.
>
> **Step 4** (real part: subtract $\varphi(0)$). On $[-L, L]$, $\int_{-L}^L\varphi(0)\frac{s\,ds}{s^2 + \varepsilon^2} = 0$ by oddness, so
>
> $$
> \int_{-L}^{L}\varphi(s)\frac{s\,ds}{s^2 + \varepsilon^2} = \int_{-L}^{L}\frac{\varphi(s) - \varphi(0)}{s}\cdot\frac{s^2}{s^2 + \varepsilon^2}\,ds .
> $$
>
> **Step 5** (real part: limit). The difference quotient $[\varphi(s) - \varphi(0)]/s$ is bounded (by $\sup|\varphi'|$), and $0 \le s^2/(s^2 + \varepsilon^2) \le 1$ tends to $1$ for every $s \ne 0$. By dominated convergence the integral tends to $\int_{-L}^L\frac{\varphi(s) - \varphi(0)}{s}ds = \mathcal P\!\int\frac{\varphi}{s}$ ([[§CA.2 Generalized Functions#^def-ca-2-6|Def. §CA.2.6]]).
>
> ⚑ By-product: the subtraction of $\varphi(0)$ must be done on a bounded symmetric interval. The user's notes write these integrals over all of $\mathbb R$, where the subtracted $\varphi(0)/s$ is not integrable at infinity and would need a symmetric limit there as well; the bounded interval is the safe form.
>
> **Step 6** (assemble). $\frac{1}{s - i\varepsilon} \to \mathcal P\frac1s + i\pi\delta(s)$, the lower sign of the formula; conjugating gives the upper.
>
> **What the derivation shows.**
> - The real part is the principal value and the imaginary part the delta function, and nothing else enters; a smooth symmetric cutoff gives the same answer as the sharp one in the definition.
> - The factor $\pi$ is the area of the Lorentzian, the same $\pi$ that $\int du/(1 + u^2)$ gives by residues.
> - Used in: the massless commutator ([[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-8|Theorem §C2b.4.8]]), the differences of Green's functions on the shell ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-9|Theorem §C2b.6.9]]), the principal function ([[§C2b.7 Wick Rotation and the Two-Point Family#^thm-c2b-7-6|Theorem §C2b.7.6]]).

^der-ca-2-11

*Uses:* [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|Theorem §CA.1.1]], [[§CA.2 Generalized Functions#^def-ca-2-6|Def. §CA.2.6]], [[§CA.4 Contour Integration#^ex-ca-4-1|Example §CA.4.1]]

> [!derivation]- Derivation (second route: the half-residue lemma)
> **Step 1.** For integrands $f = g/(x - x_0)$ with $g$ analytic near $x_0$ (every propagator integrand is of this kind), a small semicircle passing above the pole gives $\mathcal P\!\int f - i\pi g(x_0)$ and one passing below gives $\mathcal P\!\int f + i\pi g(x_0)$ ([[§CA.4 Contour Integration#^thm-ca-4-7|Theorem §CA.4.7]]).
>
> **Step 2.** By Cauchy's theorem ([[§CA.4 Contour Integration#^thm-ca-4-2|Theorem §CA.4.2]]), keeping the path on the real axis with the pole moved down to $x_0 - i\varepsilon$, i.e. the denominator $x - x_0 + i\varepsilon$, equals passing above the pole: the upper sign, $\mathcal P - i\pi\delta$. Moving the pole up gives the lower sign.
>
> **What the derivation shows.**
> - The two prescriptions differ by a full loop, $2\pi i\,g(x_0)$, and the principal value is their average. This route needs analyticity of $g$; the direct route works for every test function.
>
> *Source: the user's PHY 513 notes, App. A §A.5 (Derivation "The half-residue lemma")*

*Uses:* [[§CA.4 Contour Integration#^thm-ca-4-7|Theorem §CA.4.7]], [[§CA.4 Contour Integration#^thm-ca-4-2|Theorem §CA.4.2]]

> [!caution] Caution: What the formula does and does not say
> Pointwise it is empty: at $x \ne x_0$, $\delta = 0$ and $\mathcal P\frac{1}{x - x_0}$ acts as $\frac{1}{x - x_0}$, so it reads $\frac{1}{x - x_0} = \frac{1}{x - x_0}$. Its whole content sits at $x = x_0$, where $\frac{1}{s \mp i\varepsilon} \sim \pm\frac{i}{\varepsilon}$ has no value; what it specifies is what that divergence does under an integral. So an $i\varepsilon$ expression may be evaluated at $\varepsilon = 0$ wherever its denominator does not vanish, and the formula is needed only where it does.
>
> *Source: the user's PHY 513 notes, App. A §A.5 (Caution "What the formula does and does not say")*

^cau-ca-2-1

> [!theorem] Theorem §CA.2.12: Logarithm and Powers at the Real Axis
> With the principal branch of $\log$ (cut along the negative real axis), as distributions on $\mathbb R$:
> 1. $\log(x \pm i0) = \ln|x| \pm i\pi\,\theta(-x)$;
> 2. $\dfrac{d}{dx}\log(x \pm i0) = \dfrac{1}{x \pm i0} = \mathcal P\dfrac1x \mp i\pi\,\delta(x)$;
> 3. $\dfrac{1}{(x \pm i0)^2} \equiv -\dfrac{d}{dx}\dfrac{1}{x \pm i0} = -\dfrac{d}{dx}\mathcal P\dfrac1x \pm i\pi\,\delta'(x)$.
>
> *Source: standard; stated here (Gel'fand & Shilov 1, Ch. I)*

^thm-ca-2-12

> [!derivation]- Derivation
> **Step 1** (pointwise limit). For $x > 0$, $\log(x \pm iy) \to \ln x$. For $x < 0$, $\log(x \pm iy) = \ln|x \pm iy| + i\arg(x \pm iy)$, and $\arg(x + iy) \to \pi$, $\arg(x - iy) \to -\pi$ as $y \to 0^+$ (the points approach the cut from above and from below). So the limit is $\ln|x| \pm i\pi\theta(-x)$ for $x \ne 0$.
>
> **Step 2** (domination). For $0 < y < 1$: $|x| \le |x \pm iy| \le |x| + 1$, so $\ln|x| \le \ln|x \pm iy| \le \ln(1 + |x|)$ and $|\log(x \pm iy)| \le |\ln|x|| + \ln(1 + |x|) + \pi$. This bound times $|\varphi|$ is integrable ($\ln|x|$ is integrable at $0$). By dominated convergence the pairing converges to that of $\ln|x| \pm i\pi\theta(-x)$: part 1, the case $k = 0$ of [[§CA.2 Generalized Functions#^thm-ca-2-10|Theorem §CA.2.10]].
>
> **Step 3** (part 2: differentiate the limit). For $y > 0$, $\frac{d}{dx}\log(x \pm iy) = \frac{1}{x \pm iy}$. Derivatives commute with distributional limits ([[§CA.2 Generalized Functions#^thm-ca-2-4|Theorem §CA.2.4]], 2), so $\frac{d}{dx}\log(x \pm i0) = \lim\frac{1}{x \pm iy} = \frac{1}{x \pm i0}$.
>
> **Step 4** (part 2: differentiate the right side). $\frac{d}{dx}\theta(-x) = -\delta(x)$ ([[§CA.2 Generalized Functions#^thm-ca-2-3|Theorem §CA.2.3]], 2, with the substitution $x \to -x$ of [[§CA.2 Generalized Functions#^thm-ca-2-5|Theorem §CA.2.5]], 1). For $\ln|x|$, by Def. §CA.2.4 and two integrations by parts on $(-\infty, -\delta]$ and $[\delta, \infty)$:
>
> $$
> -\int\ln|x|\,\varphi'(x)\,dx = \lim_{\delta\to0^+}\Bigl[\ln\delta\,\bigl(\varphi(\delta) - \varphi(-\delta)\bigr) + \int_{|x| > \delta}\frac{\varphi(x)}{x}\,dx\Bigr] = \mathcal P\!\!\int\frac{\varphi(x)}{x}\,dx ,
> $$
>
> since $|\varphi(\delta) - \varphi(-\delta)| \le 2\delta\sup|\varphi'|$ and $\delta\ln\delta \to 0$. So $\frac{d}{dx}\ln|x| = \mathcal P\frac1x$, and $\frac{1}{x \pm i0} = \mathcal P\frac1x \mp i\pi\delta(x)$.
>
> ⚑ By-product: this is the Sokhotski–Plemelj formula by a third route ([[§CA.2 Generalized Functions#^thm-ca-2-11|Theorem §CA.2.11]]): differentiate the logarithm's jump.
>
> **Step 5** (part 3). For $y > 0$, $\frac{d}{dx}\frac{1}{x \pm iy} = -\frac{1}{(x \pm iy)^2}$; take the limit with Theorem §CA.2.4, 2, and differentiate part 2: $-\frac{d}{dx}\bigl[\mathcal P\frac1x \mp i\pi\delta\bigr] = -\frac{d}{dx}\mathcal P\frac1x \pm i\pi\delta'$.
>
> **What the derivation shows.**
> - The logarithm is the mildest boundary value (a function, $k = 0$); every negative power follows from it by differentiation, and the $\pm i\pi$ is the jump of the argument across the cut.
> - The logarithms in the Wightman function near the light cone ([[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-5|Theorem §C2b.3.5]]) are of this kind.

^der-ca-2-12

*Uses:* [[§CA.2 Generalized Functions#^thm-ca-2-10|Theorem §CA.2.10]], [[§CA.2 Generalized Functions#^thm-ca-2-4|Theorem §CA.2.4]], [[§CA.2 Generalized Functions#^thm-ca-2-3|Theorem §CA.2.3]], [[§CA.2 Generalized Functions#^thm-ca-2-5|Theorem §CA.2.5]], [[§CA.2 Generalized Functions#^def-ca-2-6|Def. §CA.2.6]]

> [!theorem] Theorem §CA.2.13: The Light-Cone Boundary Value
> On $\mathbb R^4$, with $t = x^0$, $r = |\mathbf x|$ and $F_\varepsilon(x) = 1/\bigl(-(t - i\varepsilon)^2 + r^2\bigr)$:
> 1. $F_\varepsilon$ converges as $\varepsilon \to 0^+$ in $\mathcal S'(\mathbb R^4)$; the limit is written $1/(-x^2 + i0\,x^0)$, since $-(t - i\varepsilon)^2 + r^2 = -x^2 + 2i\varepsilon t + \varepsilon^2$.
> 2. Its imaginary part is $-\pi\operatorname{sgn}(x^0)\,\delta(x^2)$ (with $\delta(x^2)$ as in [[§CA.2 Generalized Functions#^thm-ca-2-6|Theorem §CA.2.6]], 2); its real part is $-\mathcal P\frac{1}{x^2} \equiv -\frac{1}{2r}\bigl[\mathcal P\frac{1}{t - r} - \mathcal P\frac{1}{t + r}\bigr]$, which is the function $-1/x^2$ off the cone.
> 3. Its singular support is the light cone $x^2 = 0$, and it is Lorentz invariant.
>
> *Source: standard; stated here (Gel'fand & Shilov 1, Ch. III; Streater & Wightman, Ch. 2) · the user's PHY 513 notes, Ch. 5 §§5.4, 5.7 (the massless Wightman and commutator functions)*

^thm-ca-2-13

> [!derivation]- Derivation
> **Step 1** (analytic, with a bound). Write $z = t - iy$, $y > 0$. Then $z^2 - r^2 = (z - r)(z + r)$, and each factor has imaginary part $-y$, so $|z^2 - r^2| \ge y^2$: $F$ is analytic in the lower half $t$-plane at each $\mathbf x$, with $|F| \le y^{-2}$ ($k = 2$, $N = 0$ in [[§CA.2 Generalized Functions#^thm-ca-2-10|Theorem §CA.2.10]]).
>
> **Step 2** (a second primitive, uniform in $\mathbf x$). For $r > 0$ define $G(z, r) = \frac{1}{2r}\int_{-r}^{r}\log(z - s)\,ds$, the average of $\log(z - s)$ over $s \in [-r, r]$. Differentiating under the integral,
>
> $$
> \partial_zG = \frac{1}{2r}\int_{-r}^{r}\frac{ds}{z - s} = \frac{1}{2r}\bigl[\log(z + r) - \log(z - r)\bigr], \qquad \partial_z^2G = \frac{1}{2r}\Bigl[\frac{1}{z + r} - \frac{1}{z - r}\Bigr] = \frac{-1}{z^2 - r^2} = F .
> $$
>
> **Step 3** (the bound on $G$; sketch — the full estimate is standard and not written out here). By Step 2 of [[§CA.2 Generalized Functions#^thm-ca-2-12|Theorem §CA.2.12]], for $0 < y < 1$, $|\log(t - s - iy)| \le |\ln|t - s|| + \ln(1 + |t| + r) + \pi$. Averaging over $s \in [-r, r]$: $|G(t - iy, r)| \le \frac{1}{2r}\int_{-r}^{r}|\ln|t - s||\,ds + \ln(1 + |t| + r) + \pi \le C\bigl(1 + |\ln r| + \ln(1 + |t| + r)\bigr)$, because the average of $|\ln|u||$ over an interval of length $2r$ is at most $1 + |\ln r|$ up to a constant. This bound is independent of $y$ and locally integrable on $\mathbb R^4$ ($|\ln r|$ is integrable against $d^3x$).
>
> **Step 4** (pair and take the limit). For $\varphi \in \mathcal S(\mathbb R^4)$, integrate by parts twice in $t$ at fixed $\mathbf x$ (boundary terms vanish: $G$ grows logarithmically):
>
> $$
> \int d^4x\,F_\varepsilon\,\varphi = \int d^3x\int dt\,G(t - i\varepsilon, r)\,\partial_t^2\varphi(t, \mathbf x) .
> $$
>
> As $\varepsilon \to 0^+$, $G(t - i\varepsilon, r) \to G(t - i0, r)$ for almost every $(t, \mathbf x)$ (part 1 of Theorem §CA.2.12 inside the average), dominated by Step 3 times $|\partial_t^2\varphi|$. By dominated convergence the limit exists and equals $\partial_t^2$ of the locally integrable, polynomially bounded function $G(t - i0, r)$: a tempered distribution. This is part 1.
>
> **Step 5** (part 2: partial fractions at fixed $r > 0$). $F_\varepsilon = -\frac{1}{2r}\Bigl[\frac{1}{t - r - i\varepsilon} - \frac{1}{t + r - i\varepsilon}\Bigr]$. By Sokhotski–Plemelj in $t$ ([[§CA.2 Generalized Functions#^thm-ca-2-11|Theorem §CA.2.11]], lower sign: $\frac{1}{s - i0} = \mathcal P\frac1s + i\pi\delta(s)$),
>
> $$
> F_0 = -\frac{1}{2r}\Bigl[\mathcal P\frac{1}{t - r} - \mathcal P\frac{1}{t + r}\Bigr] - \frac{i\pi}{2r}\bigl[\delta(t - r) - \delta(t + r)\bigr] .
> $$
>
> **Step 6** (part 2: identify the delta terms). By [[§CA.2 Generalized Functions#^thm-ca-2-5|Theorem §CA.2.5]], 2, $\delta(t^2 - r^2) = [\delta(t - r) + \delta(t + r)]/2r$; multiplying by $\operatorname{sgn}t$, which is $+1$ at $t = r$ and $-1$ at $t = -r$, gives $\operatorname{sgn}(t)\delta(t^2 - r^2) = [\delta(t - r) - \delta(t + r)]/2r$. So the imaginary part is $-\pi\operatorname{sgn}(x^0)\delta(x^2)$. The $\mathbf x$-integral near $r = 0$ converges: the delta terms give $\int d^3x\,\varphi(\pm r, \mathbf x)/2r$ as in [[§CA.2 Generalized Functions#^thm-ca-2-6|Theorem §CA.2.6]], 2, and the bracket of principal values is $h(r) - h(-r)$ with $h(s) = \mathcal P\!\int dt\,\varphi(t, \mathbf x)/(t - s)$ smooth in $s$, so it is $O(r)$ and the $\frac{1}{2r}$ is harmless.
>
> **Step 7** (part 3; invariance sketch). Off the cone, $F_\varepsilon \to -1/x^2$ uniformly with all derivatives on compact sets, so the limit is smooth there; on the cone the delta term of part 2 is not smooth. For invariance: $1/(-z\cdot z)$, $z = x - i\eta$, is analytic on the tube $\eta \in V_+$ (the open forward cone), because $\operatorname{Im}(z\cdot z) = -2x\cdot\eta$ and $\operatorname{Re}(z\cdot z) = x^2 - \eta^2$ cannot both vanish there: $x\cdot\eta = 0$ with $\eta$ timelike forces $x^2 \le 0$, so $\operatorname{Re} < 0$. A proper orthochronous $\Lambda$ maps the tube to itself and leaves $z\cdot z$ unchanged; the boundary value does not depend on the direction of approach within $V_+$ ([[§CA.2 Generalized Functions#^thm-ca-2-10|Theorem §CA.2.10]], 2), so approaching along $(\varepsilon, \mathbf 0)$ or along $\Lambda(\varepsilon, \mathbf 0)$ gives the same distribution.
>
> **What the derivation shows.**
> - $\frac{1}{4\pi^2}\cdot\frac{1}{-x^2 + i0\,x^0}$ is the massless Wightman function; its imaginary part, $-\frac{1}{4\pi}\operatorname{sgn}(x^0)\delta(x^2)$, is half the massless commutator function, and its real part gives the Hadamard function ([[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-8|Theorem §C2b.4.8]]).
> - The "$-i\varepsilon x^0$" prescription is a boundary value from the forward tube, which is why it is Lorentz invariant although it singles out $x^0$.

^der-ca-2-13

*Uses:* [[§CA.2 Generalized Functions#^thm-ca-2-10|Theorem §CA.2.10]], [[§CA.2 Generalized Functions#^thm-ca-2-11|Theorem §CA.2.11]], [[§CA.2 Generalized Functions#^thm-ca-2-12|Theorem §CA.2.12]], [[§CA.2 Generalized Functions#^thm-ca-2-5|Theorem §CA.2.5]], [[§CA.2 Generalized Functions#^thm-ca-2-6|Theorem §CA.2.6]], [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|Theorem §CA.1.1]]

## Fundamental solutions

> [!definition] Definition §CA.2.7: Fundamental Solution
> For a linear differential operator $P(\partial)$ with constant coefficients on $\mathbb R^n$, a **fundamental solution** is a distribution $G$ with $P(\partial)G = -i\,\delta^n$ in the sense of [[§CA.2 Generalized Functions#^def-ca-2-4|Def. §CA.2.4]], i.e. $G[P(-\partial)\varphi] = -i\varphi(0)$ for every $\varphi \in \mathcal D$. For the Klein–Gordon operator, $(\partial^2 + m^2)G = -i\delta^4$; the factor $-i$ is the Peskin–Schroeder normalization, $G = -i\times$ the mathematicians' fundamental solution.
>
> *Source: the user's PHY 513 notes, Ch. 6 §6.2 (Principle "The Green's function is a linear map, and there is one per boundary condition") · standard (Hörmander I, §§3.3, 7.3)*

^def-ca-2-7

> [!theorem] Theorem §CA.2.14: Fundamental Solutions Differ by Homogeneous Solutions
> 1. If $G_1$, $G_2$ are fundamental solutions of $P(\partial)$, then $H = G_1 - G_2$ solves $P(\partial)H = 0$ as a distribution; conversely $G_1 + H$ is a fundamental solution for every distributional solution $H$ of the homogeneous equation.
> 2. For tempered $G$, $H$ and the Klein–Gordon operator, $(m^2 - p^2)\tilde G = -i$ and $(m^2 - p^2)\tilde H = 0$, so $\operatorname{supp}\tilde H$ lies on the mass shell $p^2 = m^2$.
> 3. A homogeneous solution of the Klein–Gordon equation supported at one point is zero: two fundamental solutions that agree away from a point agree everywhere.
>
> *Source: the user's PHY 513 notes, Ch. 6 §6.2 (one Green's function per boundary condition), §6.3 (Principle "Free fields live on the mass shell") · standard*

^thm-ca-2-14

> [!derivation]- Derivation
> **Step 1** (part 1). Derivatives of distributions are linear (Def. §CA.2.4), so $P(\partial)H = P(\partial)G_1 - P(\partial)G_2 = -i\delta + i\delta = 0$; and $P(\partial)(G_1 + H) = -i\delta + 0$.
>
> **Step 2** (part 2: Fourier side). By the derivative rule in $\mathcal S'$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-5|Theorem §CA.3.5]], 3), $\partial^2 + m^2 \to m^2 - p^2$; and $\tilde\delta^4 = 1$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-2|Theorem §CA.3.2]], 3). So the equations become $(m^2 - p^2)\tilde G = -i$ and $(m^2 - p^2)\tilde H = 0$.
>
> **Step 3** (part 2: support). Let $\varphi \in \mathcal D(\mathbb R^4)$ vanish near the shell. Then $\psi = \varphi/(m^2 - p^2)$ is again in $\mathcal D$ (the denominator does not vanish on the support of $\varphi$), and
>
> $$
> \tilde H[\varphi] = \tilde H\bigl[(m^2 - p^2)\psi\bigr] = \bigl((m^2 - p^2)\tilde H\bigr)[\psi] = 0 .
> $$
>
> So $\tilde H$ vanishes on the open set off the shell ([[§CA.2 Generalized Functions#^def-ca-2-3|Def. §CA.2.3]]).
>
> ⚑ By-product: a solution of the free equation has no Fourier components off the mass shell, as a statement about distributions → [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-2|Theorem §C2b.5.2]].
>
> **Step 4** (part 3). If $\operatorname{supp}H \subseteq \{a\}$, then $H = \sum_{|\alpha| \le N}c_\alpha\partial^\alpha\delta(x - a)$ ([[§CA.2 Generalized Functions#^thm-ca-2-2|Theorem §CA.2.2]]). Its transform is $e^{ip\cdot a}Q(p)$ with $Q$ a polynomial: each $\partial^\alpha\delta$ transforms into a monomial in the components of $p$ times a constant, and the translation gives the phase ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-5|Theorem §CA.3.5]], 1). The equation $(m^2 - p^2)e^{ip\cdot a}Q(p) = 0$ for all $p$ forces $(m^2 - p^2)Q(p) = 0$ as a polynomial, and since $m^2 - p^2$ is not the zero polynomial, $Q = 0$: all $c_\alpha = 0$.
>
> **What the derivation shows.**
> - Choosing a Green's function is choosing which homogeneous solution, built on the mass shell, to add; contours are this choice in momentum space ([[§C2b.5 Green's Functions and Contours#^thm-c2b-5-3|Theorem §C2b.5.3]]).
> - The differences $\tilde D_F - \tilde D_{\bar F}$ and $\tilde D_R - \tilde D_A$ are supported on the shell for this reason ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-9|Theorem §C2b.6.9]]).
> - Part 3 removes the δ-ambiguity in extending $\theta(x^0)D(x)$ across $x = 0$ ([[§CA.2 Generalized Functions#^thm-ca-2-7|Theorem §CA.2.7]]).

^der-ca-2-14

*Uses:* [[§CA.2 Generalized Functions#^def-ca-2-7|Def. §CA.2.7]], [[§CA.2 Generalized Functions#^def-ca-2-4|Def. §CA.2.4]], [[§CA.2 Generalized Functions#^def-ca-2-3|Def. §CA.2.3]], [[§CA.2 Generalized Functions#^thm-ca-2-2|Theorem §CA.2.2]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-2|Theorem §CA.3.2]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-5|Theorem §CA.3.5]]

> [!theorem] Theorem §CA.2.15: Convolution with a Fundamental Solution Solves the Sourced Equation
> If $G$ is a fundamental solution of $P(\partial)$ and $j \in \mathcal D(\mathbb R^n)$, then $\phi(x) \equiv i\,G\bigl[j(x - \cdot)\bigr]$ is smooth and $P(\partial)\phi = j$. In the physicists' notation, $\phi(x) = i\int d^ny\,G(x - y)\,j(y)$.
>
> *Source: the user's PHY 513 notes, Ch. 6 §§6.1–6.2 (eq. (greensolution); the Green's function as the map $j \mapsto \phi$) · standard (Hörmander I, §4.2)*

^thm-ca-2-15

> [!derivation]- Derivation
> **Step 1** (the definition is the familiar integral). For $G = T_g$, $G[j(x - \cdot)] = \int d^ny\,g(y)\,j(x - y)$, and the substitution $y \to x - y$ (Jacobian $1$) turns it into $\int d^ny\,g(x - y)\,j(y)$. For general $G$, $y \mapsto j(x - y)$ is a test function for each $x$, so $G[j(x - \cdot)]$ is defined.
>
> **Step 2** (smoothness). The difference quotient $[j(x + he_k - y) - j(x - y)]/h$ converges to $(\partial_kj)(x - y)$ in $\mathcal D$ as $h \to 0$ (all supports in one bounded set; Taylor's theorem with a remainder uniform in $y$ for every derivative). By continuity of $G$, $\partial_k\,G[j(x - \cdot)] = G[(\partial_kj)(x - \cdot)]$. Repeating, $\phi$ is smooth.
>
> **Step 3** (move the derivative onto $G$). $(\partial_kj)(x - y) = -\partial_{y_k}[j(x - y)]$, so by [[§CA.2 Generalized Functions#^def-ca-2-4|Def. §CA.2.4]]
>
> $$
> G\bigl[(\partial_kj)(x - \cdot)\bigr] = -G\bigl[\partial_{y_k}j(x - \cdot)\bigr] = (\partial_kG)\bigl[j(x - \cdot)\bigr] .
> $$
>
> Applying this to each derivative in $P(\partial)$: $P(\partial)\,G[j(x - \cdot)] = (P(\partial)G)[j(x - \cdot)]$.
>
> **Step 4** (use the equation). $(P(\partial)G)[j(x - \cdot)] = -i\,\delta[j(x - \cdot)] = -i\,j(x - 0) = -i\,j(x)$. Multiplying by $i$: $P(\partial)\phi = j$.
>
> **What the derivation shows.**
> - The Green's function is the linear map $j \mapsto \phi$, and "$G(x - y)$" its kernel ([[§CA.2 Generalized Functions#^rem-ca-2-3|Remark: What the language buys in field theory]]); the $i$ in the solution formula undoes the $-i$ of the normalization.
> - Sources that are test functions, smooth and switched on and off, give smooth fields; this is the hypothesis on $j$ in [[§C2b.5 Green's Functions and Contours#^mod-c2b-5-1|Model §C2b.5.1]] and [[§C2b.8 Particle Production by a Classical Source|§C2b.8]].

^der-ca-2-15

*Uses:* [[§CA.2 Generalized Functions#^def-ca-2-7|Def. §CA.2.7]], [[§CA.2 Generalized Functions#^def-ca-2-4|Def. §CA.2.4]]

## Operator-valued distributions

> [!definition] Definition §CA.2.8: Operator-Valued Distribution
> Let $\mathcal H$ be a Hilbert space and $\mathcal D_0 \subset \mathcal H$ a dense subspace. An **operator-valued (tempered) distribution** on $\mathbb R^n$ is a map $f \mapsto \Phi(f)$ from $\mathcal S(\mathbb R^n)$ to linear operators defined on $\mathcal D_0$, with $\Phi(f)\mathcal D_0 \subseteq \mathcal D_0$, linear in $f$, such that for all $\Psi_1, \Psi_2 \in \mathcal D_0$ the matrix element $f \mapsto \langle\Psi_1|\Phi(f)|\Psi_2\rangle$ is a tempered distribution. One writes $\Phi(f) = \int d^nx\,f(x)\,\Phi(x)$; the symbol $\Phi(x)$ is the kernel of this notation, not an operator.
>
> *Source: standard; stated here (Streater & Wightman, Ch. 3) · the user's PHY 513 notes, App. A §A.4 and Ch. 6 §6.2 ("operator-valued distribution", $\phi[\varphi] = \int d^4x\,\varphi(x)\phi(x)$)*

^def-ca-2-8

> [!theorem] Theorem §CA.2.16: The Kernel Theorem
> If $B(f, g)$ is bilinear on $\mathcal S(\mathbb R^n) \times \mathcal S(\mathbb R^m)$ and continuous in each argument separately, there is a unique $K \in \mathcal S'(\mathbb R^{n+m})$ with $B(f, g) = K[f \otimes g]$, $(f \otimes g)(x, y) = f(x)g(y)$. So a smeared two-point quantity, such as $\langle0|\phi(f)\phi(g)|0\rangle$ or $[a(f), a^\dagger(g)]$, is one distribution $K(x, y)$ in both variables together.
>
> *Source: standard; stated here (L. Schwartz's kernel theorem; Reed & Simon I, Ch. V; Hörmander I, §5.2)*

^thm-ca-2-16

> [!derivation]- Derivation (stated; an example worked)
> **Step 1** (the theorem). Not proved here: it rests on the nuclearity of $\mathcal S$ (Reed & Simon I, Ch. V).
>
> **Step 2** (example: the mode algebra, smeared). With $a(f) = \int\frac{d^3p}{(2\pi)^3}\overline{f(\mathbf p)}\,a_{\mathbf p}$ and $a^\dagger(g) = \int\frac{d^3q}{(2\pi)^3}g(\mathbf q)\,a^\dagger_{\mathbf q}$ for $f, g \in \mathcal S(\mathbb R^3)$, the commutator of [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|Theorem §C2a.2.6]] gives
>
> $$
> [a(f), a^\dagger(g)] = \int\frac{d^3p}{(2\pi)^3}\overline{f(\mathbf p)}\,g(\mathbf p) ,
> $$
>
> a number bounded by $\|f\|_{L^2}\|g\|_{L^2}/(2\pi)^3$ and hence continuous in each argument. (It is antilinear in $f$; the theorem applies to the bilinear form $(f, g) \mapsto [a(\bar f), a^\dagger(g)]$.) Its kernel, with respect to the measure $\frac{d^3p}{(2\pi)^3}\frac{d^3q}{(2\pi)^3}$, is $(2\pi)^3\delta^3(\mathbf p - \mathbf q)$: the unsmeared relation $[a_{\mathbf p}, a^\dagger_{\mathbf q}] = (2\pi)^3\delta^3(\mathbf p - \mathbf q)$ is the statement of the theorem for this $B$.
>
> **What the derivation shows.**
> - Every two-point formula with $\delta$'s, or with $D_W(x - y)$, is an identity between kernels in the sense of this theorem: it means what it says after both points are smeared.

^der-ca-2-16

*Uses:* [[§CA.2 Generalized Functions#^def-ca-2-8|Def. §CA.2.8]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|Theorem §C2a.2.6]]

> [!remark] Remark: What the language buys in field theory
> - *A Green's function is a linear map.* The sources of physics, smooth and of finite duration, are test functions, and $\phi = i\int D_C\,j$ defines the map $j \mapsto \phi$; "$D_C(x - y)$" is the kernel through which it is written, not a function with values. There is one such map per boundary condition ([[§C2b.5 Green's Functions and Contours#^def-c2b-5-1|Def. §C2b.5.1]]).
> - *Integrals that converge nowhere still define objects.* $\int d^3p\,e^{-ip\cdot\xi}/2E_{\mathbf p}$ converges for no real $\xi$, yet it is a tempered distribution, the boundary value of an analytic function ([[§C2b.2 The Wightman Function#^thm-c2b-2-5|Theorem §C2b.2.5]]).
> - *Products at a point are undefined.* The field is an operator-valued distribution, $\phi[f] = \int d^4x\,f(x)\phi(x)$, and $\phi(x)^2$ is a product of distributions at one point. That is the origin of the $\delta^3(0)$ in the zero-point energy and of normal ordering ([[§C2a.3 Energy, Momentum and the Zero-Point Energy#^def-c2a-3-1|Def. §C2a.3.1]]), and later of every ultraviolet divergence.
>
> *Source: the user's PHY 513 notes, Ch. 6 §6.2, App. A §A.4 · PHY 513, Problem Set 4, Problem 0*

^rem-ca-2-3

> [!remark]- Connections
> - The imaginary part of Sokhotski–Plemelj is the Lorentzian nascent delta function of [[§B4.4 Fourier Transforms and the Delta Function#^def-b4-4-2|WO Def. §B4.4.2]]; the same Lorentzian is the line shape of a ringing oscillator ([[§B4.4 Fourier Transforms and the Delta Function#^ex-b4-4-1|WO Example §B4.4.1]]), whose width is the $\varepsilon$ that a damped mode carries ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-10|Theorem §CA.3.10]]).
> - Sokhotski–Plemelj was used inline before it had a home: the level shift (principal value) and decay rate ($-i\pi\delta$, Fermi's golden rule) of [[§C9.6 The Interaction Picture and the Atom–Field Interaction|QM §C9.6]], and the imaginary part of the resolvent behind the optical theorem in [[§C10.2 The Eikonal Approximation and the Optical Theorem|QM §C10.2]]. In field theory it gives the differences of Green's functions on the mass shell ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-9|Theorem §C2b.6.9]]) and the massless commutator function ([[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-8|Theorem §C2b.4.8]]).
> - Distributions as linear maps on test functions are a dual space: the generalized functions sit in the dual of the test functions as kets sit in the dual of bras; the position "eigenket" that is not a vector is the same phenomenon ([[§37 Position Eigenstates and Continuous Resolutions#^prop-37-3|556 Prop. §37.3]]). Operator-valued distributions (Def. §CA.2.8) carry the same idea one level up: $\phi(x)$ is no more an operator than $|x\rangle$ is a vector.
> - The composition rule $\delta(f(x)) = \sum_i\delta(x - x_i)/|f'(x_i)|$ ([[§B1.2 The Dirac Delta Function and the Helmholtz Theorem#^thm-b1-2-1|EM Theorem §B1.2.1]], justified as a limit in Theorem §CA.2.5) is what turns $\theta(p^0)\delta(p^2 - m^2)$ into the invariant measure $d^3p/2E_{\mathbf p}$ ([[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-2|Def. §C2a.4.2]]) and $\delta(t^2 - r^2)$ into the light-cone deltas of the massless commutator.
> - Limits commute with derivatives for distributions (Theorem §CA.2.4, 2) but not for functions ([[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-3|Theorem §CA.1.3]]); C2a–C2b need the function version only where it wants a pointwise formula, as in the real-variable evaluation of the Wightman function ([[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-3|Theorem §C2b.3.3]]).
> - The point-support theorem (Theorem §CA.2.2) is also why, in the renormalization of later chapters, products at a point are ambiguous only by local terms (QFT C7, planned).
> - Theorem §CA.2.11 applied to a spectrum is Stieltjes inversion: the imaginary part of the resolvent trace at $x + i\varepsilon$ is the eigenvalue density smoothed by a Lorentzian, the tool of the semicircle law ([[§R3.4 The Semicircle Law II꞉ Stieltjes Transform and Coulomb Gas#^thm-r3-4-3|Thesis Thm. §R3.4.3]]); its δ part gives the golden-rule width of a level coupled to many others ([[§R4.2 Nearly Diagonal Matrices꞉ Gershgorin and Perturbation Theory#^thm-r4-2-8|Thesis Thm. §R4.2.8]]).
> - The spectrum of a matrix as the distribution $\frac1N\sum_i\delta(x - \lambda_i)$ (Def. §CA.2.2) and its limits (Theorem §CA.2.4) become, for random matrices, empirical spectral measures and their weak convergence ([[§R2.7 Weak Convergence, Characteristic Functions and Concentration#^def-r2-7-11|Thesis Def. §R2.7.11]], [[§R2.7 Weak Convergence, Characteristic Functions and Concentration#^def-r2-7-1|Thesis Def. §R2.7.1]]).
> - **Used in**, statement by statement (C2a–C2b items):
>   - Def. §CA.2.1–§CA.2.2 (test functions; distributions): wave packets and smeared fields — [[§C2a.1 Canonical Quantization of Fields#^def-c2a-1-1|Def. §C2a.1.1]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-1|Theorem §C2a.2.1]], [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-5|Theorem §C2a.4.5]], [[§C2b.1 Heisenberg Fields#^thm-c2b-1-1|Theorem §C2b.1.1]], [[§C2b.1 Heisenberg Fields#^thm-c2b-1-2|Theorem §C2b.1.2]], [[§C2b.1 Heisenberg Fields#^thm-c2b-1-3|Theorem §C2b.1.3]], [[§C2b.1 Heisenberg Fields#^thm-c2b-1-4|Theorem §C2b.1.4]], [[§C2b.2 The Wightman Function#^thm-c2b-2-1|Theorem §C2b.2.1]], [[§C2b.8 Particle Production by a Classical Source#^thm-c2b-8-4|Theorem §C2b.8.4]], [[§C2b.8 Particle Production by a Classical Source#^ex-c2b-8-1|Example §C2b.8.1]].
>   - Theorem §CA.2.1 (regular and singular distributions): δ, plane waves and $\langle\mathbf p|\mathbf q\rangle$ as tempered distributions — [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-6|Theorem §C2a.4.6]], [[§C2b.2 The Wightman Function#^thm-c2b-2-3|Theorem §C2b.2.3]], [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-9|Theorem §C2b.4.9]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-8|Theorem §C2b.6.8]], [[§C2b.7 Wick Rotation and the Two-Point Family#^thm-c2b-7-4|Theorem §C2b.7.4]].
>   - Def. §CA.2.3 (support, singular support): the singular support of $D_W$ is the light cone; microcausality as the support of $D$ — [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-3|Theorem §C2b.3.3]], [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-6|Theorem §C2b.3.6]], [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-4|Theorem §C2b.4.4]], [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-6|Theorem §C2b.4.6]], [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-6|Theorem §C2b.5.6]].
>   - Theorem §CA.2.2 (point support): extending $\theta(x^0)D$ across the origin; contact terms — [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-2|Theorem §C2b.5.2]], [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-6|Theorem §C2b.5.6]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-3|Theorem §C2b.6.3]].
>   - Def. §CA.2.4 (operations: derivative, product with a smooth function, limit, transform): differentiating mode integrals of operator fields, "use the support of the delta" — [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-2|Theorem §C2a.2.2]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-3|Theorem §C2a.2.3]], [[§C2a.6 Coherent States and the Classical Field#^thm-c2a-6-4|Theorem §C2a.6.4]], [[§C2b.1 Heisenberg Fields#^thm-c2b-1-1|Theorem §C2b.1.1]], [[§C2b.1 Heisenberg Fields#^thm-c2b-1-2|Theorem §C2b.1.2]], [[§C2b.1 Heisenberg Fields#^thm-c2b-1-3|Theorem §C2b.1.3]], [[§C2b.2 The Wightman Function#^thm-c2b-2-2|Theorem §C2b.2.2]], [[§C2b.2 The Wightman Function#^thm-c2b-2-4|Theorem §C2b.2.4]], [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-10|Theorem §C2b.4.10]], [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-3|Theorem §C2b.5.3]], [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-5|Theorem §C2b.5.5]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-8|Theorem §C2b.6.8]], [[§C2b.8 Particle Production by a Classical Source#^thm-c2b-8-4|Theorem §C2b.8.4]].
>   - Theorem §CA.2.3 (every distribution is differentiable; $\theta' = \delta$): contact terms of step functions in time — [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-5|Theorem §C2b.5.5]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-1|Theorem §C2b.6.1]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-4|Theorem §C2b.6.4]], [[P2 Green's Functions by Contour Integration#^p2-7|P2, step 7]].
>   - Theorem §CA.2.4 (distributional limits): every $\varepsilon \to 0^+$ — [[§C2a.1 Canonical Quantization of Fields#^thm-c2a-1-3|Theorem §C2a.1.3]], [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-2|Theorem §C2a.3.2]], [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-6|Theorem §C2a.4.6]], [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-8|Theorem §C2a.4.8]], [[§C2b.2 The Wightman Function#^thm-c2b-2-5|Theorem §C2b.2.5]], [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-11|Theorem §C2b.4.11]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-2|Theorem §C2b.6.2]].
>   - Def. §CA.2.5 and Theorem §CA.2.5 (changes of variables, composition): Lorentz invariance as a statement about distributions, $\delta(p^2 - m^2)$ — [[§C2a.1 Canonical Quantization of Fields#^thm-c2a-1-3|Theorem §C2a.1.3]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|Theorem §C2a.2.6]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-7|Theorem §C2a.2.7]], [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-4|Theorem §C2a.4.4]], [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-5|Theorem §C2a.4.5]], [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-6|Theorem §C2a.4.6]], [[§C2b.2 The Wightman Function#^thm-c2b-2-1|Theorem §C2b.2.1]], [[§C2b.2 The Wightman Function#^thm-c2b-2-2|Theorem §C2b.2.2]], [[§C2b.2 The Wightman Function#^thm-c2b-2-3|Theorem §C2b.2.3]], [[§C2b.2 The Wightman Function#^thm-c2b-2-4|Theorem §C2b.2.4]], [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-4|Theorem §C2b.4.4]], [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-6|Theorem §C2b.4.6]], [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-8|Theorem §C2b.4.8]], [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-2|Theorem §C2b.5.2]], [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-6|Theorem §C2b.5.6]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-2|Theorem §C2b.6.2]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-7|Theorem §C2b.6.7]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-8|Theorem §C2b.6.8]].
>   - Theorem §CA.2.6 (invariant shell and cone distributions): the invariant measure, $D_W$ as the transform of the positive shell, the massless $\operatorname{sgn}(x^0)\delta(x^2)$ — [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-4|Theorem §C2a.4.4]], [[§C2b.2 The Wightman Function#^thm-c2b-2-1|Theorem §C2b.2.1]], [[§C2b.2 The Wightman Function#^thm-c2b-2-2|Theorem §C2b.2.2]], [[§C2b.2 The Wightman Function#^thm-c2b-2-3|Theorem §C2b.2.3]], [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-6|Theorem §C2b.3.6]], [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-4|Theorem §C2b.4.4]], [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-8|Theorem §C2b.4.8]], [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-2|Theorem §C2b.5.2]], [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-6|Theorem §C2b.5.6]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-7|Theorem §C2b.6.7]].
>   - Theorem §CA.2.7 (products): $D_R = \theta(x^0)D$, $T$-products — [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-3|Theorem §C2a.2.3]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|Theorem §C2a.2.6]], [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-1|Theorem §C2a.3.1]], [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-5|Theorem §C2a.3.5]], [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-2|Theorem §C2a.4.2]], [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-4|Theorem §C2a.4.4]], [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-5|Theorem §C2a.4.5]], [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-6|Theorem §C2a.4.6]], [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-3|Theorem §C2a.5.3]], [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-4|Theorem §C2a.5.4]], [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-4|Theorem §C2b.4.4]], [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-12|Theorem §C2b.4.12]], [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-2|Theorem §C2b.5.2]], [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-4|Theorem §C2b.5.4]], [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-5|Theorem §C2b.5.5]], [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-6|Theorem §C2b.5.6]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-3|Theorem §C2b.6.3]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-6|Theorem §C2b.6.6]].
>   - Theorem §CA.2.8 (θ·δ, δ², δ(0)): the zero-point energy, time-ordering contact terms — [[§C2a.1 Canonical Quantization of Fields#^thm-c2a-1-3|Theorem §C2a.1.3]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-7|Theorem §C2a.2.7]], [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-2|Theorem §C2a.3.2]], [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-3|Theorem §C2a.3.3]], [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-6|Theorem §C2a.4.6]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-3|Theorem §C2b.6.3]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-6|Theorem §C2b.6.6]].
>   - Theorem §CA.2.9 (box) and Remark: Point splitting: $(2\pi)^3\delta^3(\mathbf 0) \to V$, normal ordering — [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-1|Theorem §C2a.3.1]], [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-2|Theorem §C2a.3.2]], [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-3|Theorem §C2a.3.3]], [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-5|Theorem §C2a.3.5]], [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-4|Theorem §C2a.5.4]], [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-6|Theorem §C2a.5.6]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^rem-c2b-6-3|§C2b.6, Remark: The zero-point energy is the Wightman function at coincident points]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-6|Theorem §C2b.6.6]].
>   - Def. §CA.2.6 and Caution: What the formula does and does not say (principal value; $i\varepsilon$ only matters at zeros): the principal function, dropping $i\varepsilon$ after a Wick rotation — [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-4|Theorem §C2b.5.4]], [[§C2b.7 Wick Rotation and the Two-Point Family#^thm-c2b-7-1|Theorem §C2b.7.1]], [[§C2b.7 Wick Rotation and the Two-Point Family#^thm-c2b-7-4|Theorem §C2b.7.4]], [[§C2b.7 Wick Rotation and the Two-Point Family#^def-c2b-7-2|Def. §C2b.7.2]].
>   - Theorem §CA.2.10 (boundary values): $D_W$ from the lower half-plane — [[§C2b.2 The Wightman Function#^thm-c2b-2-3|Theorem §C2b.2.3]], [[§C2b.2 The Wightman Function#^thm-c2b-2-5|Theorem §C2b.2.5]], [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-4|Theorem §C2b.3.4]].
>   - Theorem §CA.2.11 (Sokhotski–Plemelj): [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-8|Theorem §C2b.4.8]], [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-4|Theorem §C2b.5.4]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-8|Theorem §C2b.6.8]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-9|Theorem §C2b.6.9]], [[§C2b.7 Wick Rotation and the Two-Point Family#^thm-c2b-7-6|Theorem §C2b.7.6]].
>   - Theorem §CA.2.12 (logarithms and powers): the light-cone singularity — [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-5|Theorem §C2b.3.5]], [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-6|Theorem §C2b.3.6]].
>   - Theorem §CA.2.13 (light-cone boundary value): massless $D_W$, $D$, $D_1$ — [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-5|Theorem §C2b.3.5]], [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-6|Theorem §C2b.3.6]], [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-8|Theorem §C2b.4.8]], [[§C2b.7 Wick Rotation and the Two-Point Family#^thm-c2b-7-4|Theorem §C2b.7.4]].
>   - Def. §CA.2.7, Theorems §CA.2.14–§CA.2.15 (fundamental solutions): Green's functions, contours as boundary conditions, the sourced field — [[§C2b.5 Green's Functions and Contours#^rem-c2b-5-1|§C2b.5, Remark: What a Green's "function" is]], [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-2|Theorem §C2b.5.2]], [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-4|Theorem §C2b.5.4]], [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-6|Theorem §C2b.5.6]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-3|Theorem §C2b.6.3]], [[§C2b.8 Particle Production by a Classical Source#^thm-c2b-8-1|Theorem §C2b.8.1]], [[§C2b.8 Particle Production by a Classical Source#^thm-c2b-8-4|Theorem §C2b.8.4]].
>   - Def. §CA.2.8, Theorem §CA.2.16 (operator-valued distributions, kernels): $\phi(f)$, $[\phi, \pi] = i\delta^3$, $[a, a^\dagger] = (2\pi)^3\delta^3$, $\langle0|\phi(x)\phi(y)|0\rangle$ — [[§C2a.1 Canonical Quantization of Fields#^def-c2a-1-1|Def. §C2a.1.1]], [[§C2a.1 Canonical Quantization of Fields#^thm-c2a-1-3|Theorem §C2a.1.3]], [[§C2a.2 Mode Expansion and the Mode Algebra#^def-c2a-2-2|Def. §C2a.2.2]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-4|Theorem §C2a.2.4]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-7|Theorem §C2a.2.7]], [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-6|Theorem §C2a.4.6]], [[§C2a.6 Coherent States and the Classical Field#^thm-c2a-6-8|Theorem §C2a.6.8]], [[§C2b.1 Heisenberg Fields#^thm-c2b-1-2|Theorem §C2b.1.2]], [[§C2b.2 The Wightman Function#^thm-c2b-2-2|Theorem §C2b.2.2]].
> - **Used in**, statement by statement (C1a–C1b items):
>   - Def. §CA.2.1–§CA.2.2 (test functions; distributions): variations and the functional derivative — [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^def-c1b-2-3|Def. §C1b.2.3]], [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^rem-c1b-2-2|§C1b.2, Remark: The functional derivative is a distribution]].
>   - Theorem §CA.2.1 (regular and singular distributions): δ as a functional derivative — [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^rem-c1b-2-2|§C1b.2, Remark: The functional derivative is a distribution]], [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-4|Theorem §C1b.2.4]], [[§C1b.4 Hamiltonian Field Theory#^thm-c1b-4-1|Theorem §C1b.4.1]], [[§C1b.4 Hamiltonian Field Theory#^thm-c1b-4-4|Theorem §C1b.4.4]].
>   - Def. §CA.2.3 (support, singular support): [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-8|Theorem §C2b.3.8]], [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-7|Theorem §C2b.4.7]].
>   - Def. §CA.2.4 (operations): [[§C1a.3 Causal Structure and the Causality of a Single Particle#^thm-c1a-3-2|Theorem §C1a.3.2]], [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-7|Theorem §C2b.4.7]].
>   - Theorem §CA.2.4 (distributional limits): [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-7|Theorem §C2b.3.7]].
>   - Def. §CA.2.5 (changes of variables): invariance of distributions — [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-7|Theorem §C2b.4.7]], [[§C1a.4 The Lorentz Group#^thm-c1a-4-1|Theorem §C1a.4.1]], [[§C1b.1 Fields and Their Transformation Laws#^thm-c1b-1-3|Theorem §C1b.1.3]], [[§C1b.4 Hamiltonian Field Theory#^thm-c1b-4-5|Theorem §C1b.4.5]].
>   - Theorem §CA.2.6 (invariant shell and cone distributions): [[§C1a.4 The Lorentz Group#^thm-c1a-4-1|Theorem §C1a.4.1]], [[§C1b.1 Fields and Their Transformation Laws#^cau-c1b-1-1|§C1b.1, Caution: What "the scalar does not change" does not mean]].
>   - Theorem §CA.2.8 (θ·δ, δ², δ(0)): [[§C1b.4 Hamiltonian Field Theory#^thm-c1b-4-5|Theorem §C1b.4.5]].
>   - Theorem §CA.2.10 (boundary values): [[§C1a.5 Vectors, Tensors and Index Notation#^rem-c1a-5-3|§C1a.5, Remark: In what sense 1/x² is harmonic, and where the source sits]].
>   - Theorem §CA.2.13 (light-cone boundary value): [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-9|Theorem §C1a.5.9]], [[§C1a.5 Vectors, Tensors and Index Notation#^rem-c1a-5-3|§C1a.5, Remark: In what sense 1/x² is harmonic, and where the source sits]].
>   - Def. §CA.2.8, Theorem §CA.2.16 (operator-valued distributions, kernels): [[§C1a.5 Vectors, Tensors and Index Notation#^rem-c1a-5-4|§C1a.5, Remark: Three expansions, not one]], [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^rem-c1b-2-8|§C1b.2, Remark: The second variation is the operator whose inverse is the propagator]], [[§C1b.4 Hamiltonian Field Theory#^thm-c1b-4-5|Theorem §C1b.4.5]], [[§C1b.5 Noether's Theorem#^rem-c1b-5-6|§C1b.5, Remark: In what sense these identities hold]].
> - **Used in**, statement by statement (C3 items):
>   - Def. §CA.2.2 (distributions): the equal-time commutators of the Noether charges — [[§C3.5 Quantum Poincaré Transformations#^thm-c3-5-13|Theorem §C3.5.13]].
>   - Def. §CA.2.4 (operations): transformation laws and orbital generators on distributions — [[§C3.4 How Fields Transform under the Lorentz Group#^rem-c3-4-2|§C3.4, Remark: The laws for fields that are distributions]], [[§C3.5 Quantum Poincaré Transformations#^thm-c3-5-9|Theorem §C3.5.9]].
>   - Def. §CA.2.5 (changes of variables): moving the argument of a field — [[§C3.4 How Fields Transform under the Lorentz Group#^rem-c3-4-2|§C3.4, Remark: The laws for fields that are distributions]], [[§C3.5 Quantum Poincaré Transformations#^thm-c3-5-12|Theorem §C3.5.12]].
>   - Theorem §CA.2.6 (invariant shell and cone distributions): Lorentz-invariant distributions as fixed points of the scalar law — [[§C3.4 How Fields Transform under the Lorentz Group#^rem-c3-4-2|§C3.4, Remark: The laws for fields that are distributions]].
>   - Theorem §CA.2.7 (products): the normalization of the induced states — [[§C3.6★ Particle States and the Little Group#^thm-c3-6-4|Theorem §C3.6.4]], [[§C3.6★ Particle States and the Little Group#^thm-c3-6-5|Theorem §C3.6.5]].
>   - Def. §CA.2.8 (operator-valued distributions): covariance of quantum fields — [[§C3.4 How Fields Transform under the Lorentz Group#^rem-c3-4-2|§C3.4, Remark: The laws for fields that are distributions]], [[§C3.5 Quantum Poincaré Transformations#^pr-c3-5-8|Principle §C3.5.8]].
> - **Used in**, statement by statement (C5a–C5b items):
>   - Def. §CA.2.1 (test functions): smeared Dirac fields — [[§C5b.1 Canonical Quantization of the Dirac Field#^def-c5b-1-6|Def. §C5b.1.6]].
>   - Theorem §CA.2.1 (regular and singular distributions): plane-wave solutions and the propagator at finite $\varepsilon$ as tempered distributions — [[§C5a.3 The Dirac Equation and Its Lagrangian#^rem-c5a-3-6|§C5a.3, Remark: In what sense the equations hold]], [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-4|Theorem §C5b.8.4]].
>   - Theorem §CA.2.2 (distributions supported at a point): uniqueness of $S_F$ at the origin — [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-4|Theorem §C5b.8.4]].
>   - Def. §CA.2.3 (support, singular support): microcausality of the Dirac field — [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-3|Theorem §C5b.7.3]].
>   - Theorem §CA.2.3 (derivatives): Dirac solutions as Klein–Gordon solutions, $\partial_0\theta = \delta$ in the propagator — [[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-10|Theorem §C5a.3.10]], [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-3|Theorem §C5b.8.3]].
>   - Def. §CA.2.4 (operations): the Dirac operator on distributions, derivatives of two-point functions, supports — [[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-1|Theorem §C5a.3.1]], [[§C5a.3 The Dirac Equation and Its Lagrangian#^rem-c5a-3-6|§C5a.3, Remark: In what sense the equations hold]], [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-1|Theorem §C5b.7.1]], [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-3|Theorem §C5b.7.3]], [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-4|Theorem §C5b.8.4]].
>   - Theorem §CA.2.4 (distributional limits): nascent deltas and the limit $\varepsilon \to 0^+$ — [[§C5b.1 Canonical Quantization of the Dirac Field#^thm-c5b-1-8|Theorem §C5b.1.8]], [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-3|Theorem §C5b.8.3]].
>   - Def. §CA.2.5 (changes of variables): covariance of the Dirac equation in $\mathcal S'$, the smeared anticommutator — [[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-1|Theorem §C5a.3.1]], [[§C5a.3 The Dirac Equation and Its Lagrangian#^rem-c5a-3-6|§C5a.3, Remark: In what sense the equations hold]], [[§C5b.1 Canonical Quantization of the Dirac Field#^thm-c5b-1-8|Theorem §C5b.1.8]].
>   - Theorem §CA.2.6 (invariant shell and cone distributions): solutions as transforms supported on the mass shell — [[§C5a.5 Plane-Wave Solutions#^rem-c5a-5-6|§C5a.5, Remark: In what sense a general solution is a superposition of these plane waves]].
>   - Theorem §CA.2.7 (products): smooth prefactors on the support of δ, multiplication by polynomials, slice products — [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-3|Theorem §C5b.2.3]], [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-2|Theorem §C5b.3.2]], [[§C5b.4 Fermions, Fock Space and the Pauli Principle#^thm-c5b-4-2|Theorem §C5b.4.2]], [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-1|Theorem §C5b.7.1]], [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-4|Theorem §C5b.7.4]], [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-4|Theorem §C5b.8.4]].
>   - Theorem §CA.2.8 (θ·δ, δ², δ(0)): the coincident anticommutator $\delta^3(\mathbf 0)$ — [[§C5b.1 Canonical Quantization of the Dirac Field#^thm-c5b-1-8|Theorem §C5b.1.8]].
>   - Theorem §CA.2.9 (box regularization of $\delta^3(\mathbf 0)$): the fermionic zero-point energy and vacuum charge — [[§C5b.1 Canonical Quantization of the Dirac Field|§C5b.1]] (Connections), [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-5|Theorem §C5b.3.5]].
>   - Def. §CA.2.8 (operator-valued distributions): the quantized Dirac field — [[§C5a.3 The Dirac Equation and Its Lagrangian#^rem-c5a-3-6|§C5a.3, Remark: In what sense the equations hold]], [[§C5a.5 Plane-Wave Solutions#^rem-c5a-5-6|§C5a.5, Remark: In what sense a general solution is a superposition of these plane waves]], [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-1|Theorem §C5b.2.1]], [[§C5b.1 Canonical Quantization of the Dirac Field#^def-c5b-1-6|Def. §C5b.1.6]].
> - **Used in**, statement by statement (C4 items):
>   - Theorem §CA.2.1 (Regular and Singular Tempered Distributions): [[§C4.8 Vector-Field Propagators#^rem-c4-8-2|§C4.8, Remark: The sign of the photon propagator and negative norm]], [[§C4.8 Vector-Field Propagators#^thm-c4-8-7|Theorem §C4.8.7]].
>   - Remark (Point splitting: how a product at one point is regularized): [[§C4.4★ Quantizing the Massive Vector Field|§C4.4★]].
>   - Def. §CA.2.3 (Support and Singular Support): [[§C4.8 Vector-Field Propagators#^thm-c4-8-2|Theorem §C4.8.2]], [[§C4.8 Vector-Field Propagators#^thm-c4-8-3|Theorem §C4.8.3]], [[§C4.8 Vector-Field Propagators|§C4.8]].
>   - Theorem §CA.2.3 (Every Generalized Function Is Differentiable): [[§C4.2★ The Proca Field#^thm-c4-2-4|Theorem §C4.2.4]], [[§C4.2★ The Proca Field#^thm-c4-2-5|Theorem §C4.2.5]], [[§C4.8 Vector-Field Propagators#^thm-c4-8-3|Theorem §C4.8.3]], [[§C4.8 Vector-Field Propagators#^thm-c4-8-4|Theorem §C4.8.4]], [[§C4.8 Vector-Field Propagators|§C4.8]].
>   - Def. §CA.2.4 (Derivative, Limit and Fourier Transform of a Generalized Function): [[§C4.4★ Quantizing the Massive Vector Field#^thm-c4-4-2|Theorem §C4.4.2]], [[§C4.4★ Quantizing the Massive Vector Field#^thm-c4-4-3|Theorem §C4.4.3]], [[§C4.5 The Maxwell Field, Gauge Symmetry and Gauge Fixing#^thm-c4-5-3|Theorem §C4.5.3]], [[§C4.6 Covariant Quantization and the Indefinite Metric#^thm-c4-6-4|Theorem §C4.6.4]], [[§C4.6 Covariant Quantization and the Indefinite Metric#^thm-c4-6-5|Theorem §C4.6.5]], [[§C4.7 The Gupta–Bleuler Condition and Physical Photons#^thm-c4-7-3|Theorem §C4.7.3]], [[§C4.7 The Gupta–Bleuler Condition and Physical Photons#^thm-c4-7-4|Theorem §C4.7.4]], [[§C4.8 Vector-Field Propagators#^thm-c4-8-1|Theorem §C4.8.1]], [[§C4.8 Vector-Field Propagators#^thm-c4-8-2|Theorem §C4.8.2]], [[§C4.8 Vector-Field Propagators#^thm-c4-8-3|Theorem §C4.8.3]], [[§C4.8 Vector-Field Propagators|§C4.8]].
>   - Theorem §CA.2.6 (Invariant Distributions on the Mass Shell and the Light Cone): [[§C4.6 Covariant Quantization and the Indefinite Metric#^thm-c4-6-6|Theorem §C4.6.6]], [[§C4.6 Covariant Quantization and the Indefinite Metric#^thm-c4-6-7|Theorem §C4.6.7]], [[§C4.8 Vector-Field Propagators#^rem-c4-8-2|§C4.8, Remark: The sign of the photon propagator and negative norm]], [[§C4.8 Vector-Field Propagators#^thm-c4-8-7|Theorem §C4.8.7]], [[§C4.8 Vector-Field Propagators|§C4.8]].
>   - Def. §CA.2.7 (Fundamental Solution): [[§C4.2★ The Proca Field#^thm-c4-2-7|Theorem §C4.2.7]], [[§C4.2★ The Proca Field#^thm-c4-2-8|Theorem §C4.2.8]], [[§C4.2★ The Proca Field|§C4.2★]].
>   - Theorem §CA.2.7 (Products with Disjoint Singular Supports): [[§C4.4★ Quantizing the Massive Vector Field#^thm-c4-4-4|Theorem §C4.4.4]], [[§C4.4★ Quantizing the Massive Vector Field#^thm-c4-4-6|Theorem §C4.4.6]], [[§C4.4★ Quantizing the Massive Vector Field#^thm-c4-4-9|Theorem §C4.4.9]], [[§C4.4★ Quantizing the Massive Vector Field#^thm-c4-4-10|Theorem §C4.4.10]], [[§C4.6 Covariant Quantization and the Indefinite Metric#^thm-c4-6-8|Theorem §C4.6.8]], [[§C4.6 Covariant Quantization and the Indefinite Metric#^thm-c4-6-9|Theorem §C4.6.9]], [[§C4.6 Covariant Quantization and the Indefinite Metric#^thm-c4-6-10|Theorem §C4.6.10]].
>   - Def. §CA.2.8 (Operator-Valued Distribution): [[§C4.3★ Massive Polarization Vectors and the Plane-Wave Expansion#^rem-c4-3-1|§C4.3★, Remark: In what sense the Proca field is a distribution]].
>   - Theorem §CA.2.9 (Box Regularization of δ³(0)): [[§C4.4★ Quantizing the Massive Vector Field|§C4.4★]].
>   - Theorem §CA.2.11 (Sokhotski–Plemelj Formula): [[§C4.8 Vector-Field Propagators#^rem-c4-8-2|§C4.8, Remark: The sign of the photon propagator and negative norm]], [[§C4.8 Vector-Field Propagators#^thm-c4-8-7|Theorem §C4.8.7]], [[§C4.8 Vector-Field Propagators|§C4.8]].
>   - Theorem §CA.2.12 (Logarithm and Powers at the Real Axis): [[§C4.8 Vector-Field Propagators#^rem-c4-8-3|§C4.8, Remark: Why the ξ-term is allowed: Faddeev–Popov]], [[§C4.8 Vector-Field Propagators#^thm-c4-8-8|Theorem §C4.8.8]], [[§C4.8 Vector-Field Propagators|§C4.8]].
>   - Theorem §CA.2.13 (The Light-Cone Boundary Value): [[§C4.8 Vector-Field Propagators#^thm-c4-8-5|Theorem §C4.8.5]], [[§C4.8 Vector-Field Propagators|§C4.8]].
>   - Theorem §CA.2.15 (Convolution with a Fundamental Solution Solves the Sourced Equation): [[§C4.2★ The Proca Field#^thm-c4-2-7|Theorem §C4.2.7]], [[§C4.2★ The Proca Field#^thm-c4-2-8|Theorem §C4.2.8]].
> - **Used in**, statement by statement (Electromagnetism C items):
>   - Def. §CA.2.1 (test functions): variations of compact support, the polarization charge, a comb of line charges — [[§C2.1 The Static Limit and the Field of a Charge Distribution#^thm-c2-1-2|EM Theorem §C2.1.2]], [[§C5.1 Polarization Charge and the Polarization#^thm-c5-1-2|EM Theorem §C5.1.2]], [[§C6.2 Separation in Cartesian and Spherical Coordinates#^ex-c6-2-2|EM Example §C6.2.2]].
>   - Def. §CA.2.2 (distributions): point charges, point dipoles, surface charge and polarization charge as distributions — [[§C1.1 Building the Maxwell Action#^thm-c1-1-6|EM Theorem §C1.1.6]], [[§C3.1 Cartesian Multipole Moments and Dipole Layers#^mod-c3-1-2|EM Model §C3.1.2]], [[§C4.1 Induced Charge, Screening and Thomson's Theorem#^rem-c4-1-1|EM Remark: What changes from levels A and B]], [[§C5.1 Polarization Charge and the Polarization#^thm-c5-1-2|EM Theorem §C5.1.2]], [[§C6.1 Potential Theory and Uniqueness#^rem-c6-1-1|EM Remark: What changes from level B]], [[§C7.1 The Method of Images#^thm-c7-1-1|EM Theorem §C7.1.1]].
>   - Theorem §CA.2.1 (regular and singular distributions): the current of a point charge, the Coulomb field and the fields of surface layers as distributions — [[§C1.1 Building the Maxwell Action#^thm-c1-1-6|EM Theorem §C1.1.6]], [[§C2.1 The Static Limit and the Field of a Charge Distribution#^rem-c2-1-1|EM Remark: The Coulomb potential as a fundamental solution]], [[§C2.3 Electrostatic Energy and Self-Energy#^thm-c2-3-7|EM Theorem §C2.3.7]], [[§C4.1 Induced Charge, Screening and Thomson's Theorem#^rem-c4-1-1|EM Remark: What changes from levels A and B]], [[§C4.1 Induced Charge, Screening and Thomson's Theorem#^thm-c4-1-6|EM Theorem §C4.1.6]], [[§C5.2 The Field of Polarized Matter#^thm-c5-2-1|EM Theorem §C5.2.1]], [[§C5.2 The Field of Polarized Matter#^ex-c5-2-3|EM Example §C5.2.3]].
>   - Theorem §CA.2.2 (distributions supported at a point): the charge density as a series of point multipoles — [[§C3.1 Cartesian Multipole Moments and Dipole Layers#^thm-c3-1-6|EM Theorem §C3.1.6]].
>   - Theorem §CA.2.3 (every distribution is differentiable; $\theta' = \delta$): the Bianchi identity for distributional potentials, jumps at dipole layers and surfaces, the jump condition of a Green function — [[§C1.2 The Field Equations and the Bianchi Identity#^thm-c1-2-4|EM Theorem §C1.2.4]], [[§C3.1 Cartesian Multipole Moments and Dipole Layers#^thm-c3-1-10|EM Theorem §C3.1.10]], [[§C3.2 Spherical Multipole Expansions#^ex-c3-2-3|EM Example §C3.2.3]], [[§C5.1 Polarization Charge and the Polarization#^thm-c5-1-2|EM Theorem §C5.1.2]], [[§C7.4 Constructing Green Functions#^thm-c7-4-2|EM Theorem §C7.4.2]], [[§C7.5★ Logarithmic Potentials and the Poisson–Boltzmann Equation#^thm-c7-5-4|EM Theorem §C7.5.4]].
>   - Def. §CA.2.4 (operations): field equations in weak form, Poisson's equation as an identity of distributions, multipole and polarization densities — [[§C1.2 The Field Equations and the Bianchi Identity#^thm-c1-2-2|EM Theorem §C1.2.2]], [[§C1.3 Gauge Symmetry and Charge Conservation#^thm-c1-3-1|EM Theorem §C1.3.1]], [[§C1.3 Gauge Symmetry and Charge Conservation#^ex-c1-3-1|EM Example §C1.3.1]], [[§C2.1 The Static Limit and the Field of a Charge Distribution#^thm-c2-1-2|EM Theorem §C2.1.2]], [[§C2.2 Gauss's Law and the Solid Angle#^thm-c2-2-4|EM Theorem §C2.2.4]], [[§C3.1 Cartesian Multipole Moments and Dipole Layers#^mod-c3-1-2|EM Model §C3.1.2]], [[§C3.1 Cartesian Multipole Moments and Dipole Layers#^thm-c3-1-3|EM Theorem §C3.1.3]], [[§C3.1 Cartesian Multipole Moments and Dipole Layers#^mod-c3-1-5|EM Model §C3.1.5]], [[§C3.1 Cartesian Multipole Moments and Dipole Layers#^thm-c3-1-6|EM Theorem §C3.1.6]], [[§C3.1 Cartesian Multipole Moments and Dipole Layers#^thm-c3-1-9|EM Theorem §C3.1.9]], [[§C4.3 The Capacitance Matrix#^thm-c4-3-3|EM Theorem §C4.3.3]], [[§C5.1 Polarization Charge and the Polarization#^thm-c5-1-2|EM Theorem §C5.1.2]], [[§C6.1 Potential Theory and Uniqueness#^thm-c6-1-2|EM Theorem §C6.1.2]], [[§C7.1 The Method of Images#^thm-c7-1-1|EM Theorem §C7.1.1]], [[§C7.3 Green Functions for Poisson’s Equation#^def-c7-3-1|EM Def. §C7.3.1]].
>   - Theorem §CA.2.4 (distributional limits): the point dipole as a limit, closure relations, the Poisson kernel as a nascent delta — [[§C3.1 Cartesian Multipole Moments and Dipole Layers#^mod-c3-1-2|EM Model §C3.1.2]], [[§C6.2 Separation in Cartesian and Spherical Coordinates#^thm-c6-2-1|EM Theorem §C6.2.1]], [[§C6.2 Separation in Cartesian and Spherical Coordinates#^thm-c6-2-3|EM Theorem §C6.2.3]], [[§C7.3 Green Functions for Poisson’s Equation#^thm-c7-3-5|EM Theorem §C7.3.5]], [[§C7.4 Constructing Green Functions#^thm-c7-4-1|EM Theorem §C7.4.1]].
>   - Def. §CA.2.5 and Theorem §CA.2.5 (changes of variables, composition): the field of a point dipole, the current of a point charge, line sources — [[§C3.1 Cartesian Multipole Moments and Dipole Layers#^thm-c3-1-4|EM Theorem §C3.1.4]], [[§C1.1 Building the Maxwell Action#^thm-c1-1-6|EM Theorem §C1.1.6]], [[§C7.5★ Logarithmic Potentials and the Poisson–Boltzmann Equation#^thm-c7-5-1|EM Theorem §C7.5.1]].
>   - Theorem §CA.2.7 (products): the Helmholtz form of D, the force on a dielectric interface — [[§C5.2 The Field of Polarized Matter#^thm-c5-2-5|EM Theorem §C5.2.5]], [[§C5.6 Forces in Dielectrics#^ex-c5-6-2|EM Example §C5.6.2]].
>   - Theorem §CA.2.8 (θ·δ, δ², δ(0)): the self-energy of a point charge, no self-force, the average field on a surface charge — [[§C1.5 The Electromagnetic Energy–Momentum Tensor#^rem-c1-5-1|EM Remark: Point charges, and where the electrostatic energy sits]], [[§C2.1 The Static Limit and the Field of a Charge Distribution#^thm-c2-1-4|EM Theorem §C2.1.4]], [[§C2.2 Gauss's Law and the Solid Angle#^ex-c2-2-3|EM Example §C2.2.3]], [[§C2.3 Electrostatic Energy and Self-Energy#^thm-c2-3-7|EM Theorem §C2.3.7]], [[§C2.4 The Electric Stress Tensor#^thm-c2-4-3|EM Theorem §C2.4.3]], [[§C5.6 Forces in Dielectrics#^thm-c5-6-1|EM Theorem §C5.6.1]], [[§C5.6 Forces in Dielectrics#^ex-c5-6-2|EM Example §C5.6.2]].
>   - Def. §CA.2.7, Theorems §CA.2.14–§CA.2.15 (fundamental solutions): the Coulomb potential, the Green functions of Poisson's equation, the Lorenz-gauge and Proca solutions — [[§C1.3 Gauge Symmetry and Charge Conservation#^ex-c1-3-2|EM ★ Example §C1.3.2]], [[§C1.4 Gauge Fixing and the Two Polarizations#^thm-c1-4-1|EM Theorem §C1.4.1]], [[§C2.1 The Static Limit and the Field of a Charge Distribution#^rem-c2-1-1|EM Remark: The Coulomb potential as a fundamental solution]], [[§C7.3 Green Functions for Poisson’s Equation#^def-c7-3-1|EM Def. §C7.3.1]], [[§C7.3 Green Functions for Poisson’s Equation#^thm-c7-3-1|EM Theorem §C7.3.1]], [[§C7.3 Green Functions for Poisson’s Equation#^thm-c7-3-4|EM Theorem §C7.3.4]].
