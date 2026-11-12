---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: CA
section: CA.2
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§CA.1 Exchanging Limits, Derivatives and Integrals]] · ↑ [[· CA Mathematical Methods]] · [[§CA.3 Products of Distributions and Operator-Valued Distributions]] →

*Sources: the user's PHY 513 notes, App. A §A.4 and the principal value of §A.5, App. A §A.2 (rule 5, integration by parts), Ch. 4 §4.3 and §4.9, Ch. 6 §§6.2–6.3 · PHY 513, Problem Set 4, Problem 0 (generalized functions) and eq. (11) · standard results stated here, where marked: Hörmander, The Analysis of Linear Partial Differential Operators I, Ch. 2–4; Gel'fand & Shilov, Generalized Functions, Vol. 1, Ch. I; Reed & Simon, Methods of Modern Mathematical Physics I, Ch. V; Stein & Shakarchi, Functional Analysis (Princeton Lectures IV), Ch. 3.*

The delta function, the Wightman, commutator and Feynman functions, the overlap $\langle\mathbf p|\mathbf q\rangle$ and the field operators themselves are not functions: none of them has a value at every point, and several have none anywhere. This section says what they are, continuous linear maps on test functions, and which operations on them are defined: derivatives always, products with smooth functions, limits $\varepsilon \to 0^+$ whenever they converge on every test function. It starts from the working delta function of [[§B4.4 Fourier Transforms and the Delta Function#^def-b4-4-2|WO Def. §B4.4.2]] and [[§B1.2 The Dirac Delta Function and the Helmholtz Theorem#^thm-b1-2-1|EM Theorem §B1.2.1]], from the δ-normalized kets of [[§49 Position Eigenstates and Continuous Resolutions#^prop-49-3|556 Prop. §49.3]], and from the exchange theorems of [[§CA.1 Exchanging Limits, Derivatives and Integrals|§CA.1]]; the Fourier transform of a distribution is [[§CA.4 Fourier Transforms and Fourier Tricks|§CA.4]]. New here, beyond the user's App. A §A.4: the spaces $\mathcal D$ and $\mathcal S$, the principal value, support and singular support, changes of variables and composition with a function; integration by parts against a delta function is the derivative rule seen as a calculation. The products that exist and those that do not (among them $\delta^3(\mathbf 0)$) and operator-valued distributions follow in [[§CA.3 Products of Distributions and Operator-Valued Distributions|§CA.3]]. Boundary values of analytic functions (with the Sokhotski–Plemelj formula), the $i\varepsilon$ limits and fundamental solutions, which also need the Fourier transform and contour integration, are [[§CA.7 Boundary Values, iε Limits and Fundamental Solutions|§CA.7]]. Proofs rest on this chapter and on the Math vault only; each statement lists in Connections the places of [[· C2a The Quantum Scalar Field|C2a]] and [[· C2b Two-Point Functions, Causality and Propagators|C2b]] that use it.

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

> [!definition] Definition §CA.2.2: Generalized Function
> A **generalized function** (distribution) $T$ is a linear map $\varphi \mapsto T[\varphi] \in \mathbb C$ on the test functions $\varphi \in \mathcal D$ ([[§CA.2 Generalized Functions#^def-ca-2-1|Def. §CA.2.1]]), continuous: $T[\varphi_k] \to T[\varphi]$ whenever $\varphi_k \to \varphi$ in the sense of Def. §CA.2.1, which every map met here is. The space of these maps is written $\mathcal D'$. A locally integrable function $\psi$ defines the generalized function $T_\psi[\varphi] = \int\psi\varphi$.
>
> *Source: the user's PHY 513 notes, App. A §A.4, Ch. 6 §6.2 · PHY 513, Problem Set 4, Problem 0*

^def-ca-2-2

> [!definition] Definition §CA.2.3: Tempered Distribution
> With **Schwartz functions** (smooth, decaying with all derivatives faster than every power: the space $\mathcal S$ of [[§CA.2 Generalized Functions#^def-ca-2-1|Def. §CA.2.1]]) in place of test functions in [[§CA.2 Generalized Functions#^def-ca-2-2|Def. §CA.2.2]], the maps are **tempered distributions**: linear maps $T: \mathcal S \to \mathbb C$ with $T[\varphi_k] \to T[\varphi]$ whenever $\varphi_k \to \varphi$ in $\mathcal S$. The space of these maps is written $\mathcal S'$. Restricted to $\mathcal D \subset \mathcal S$ a tempered distribution is a generalized function, because a sequence that converges in $\mathcal D$ converges in $\mathcal S$ (with all supports in $|x| \le R$, $\|\varphi_k - \varphi\|_{\alpha,\beta} \le R^{|\alpha|}\sup|\partial^\beta(\varphi_k - \varphi)| \to 0$).
>
> *Source: the user's PHY 513 notes, App. A §A.4, Ch. 6 §6.2 · PHY 513, Problem Set 4, Problem 0*

^def-ca-2-3

> [!definition] Definition §CA.2.4: The Delta Function
> The **delta function** is the map $\delta[\varphi] = \varphi(0)$; the delta function at a point $a \in \mathbb R^n$ is the map $\varphi \mapsto \varphi(a)$, written $\delta(x - a)$, and $\delta^n$ when the dimension is to be shown. It is a generalized function ([[§CA.2 Generalized Functions#^def-ca-2-2|Def. §CA.2.2]]) and a tempered distribution ([[§CA.2 Generalized Functions#^def-ca-2-3|Def. §CA.2.3]]): it is linear, and $|\varphi_k(a) - \varphi(a)| \le \sup|\varphi_k - \varphi| \to 0$ in either sense of convergence. Under an integral sign, $\int d^nx\,\delta(x - a)\varphi(x)$ is notation for $\varphi(a)$.
>
> *Source: the user's PHY 513 notes, App. A §A.4, Ch. 6 §6.2 · PHY 513, Problem Set 4, Problem 0*

^def-ca-2-4

> [!remark] Remark: What changes from the working delta function
> [[§B4.4 Fourier Transforms and the Delta Function#^def-b4-4-2|WO Def. §B4.4.2]] and [[§B1.2 The Dirac Delta Function and the Helmholtz Theorem#^def-b1-2-1|EM Def. §B1.2.1]] define $\delta$ by what it does under an integral and realize it as a limit of narrow peaks; the rules were checked one by one with a nascent delta. Here the map *is* the object: $\int dx\,\delta(x)\varphi(x)$ is notation for $\varphi \mapsto \varphi(0)$, chosen so that the formula for $T_\psi$ can be used uniformly. Nothing is lost by the generalization: a test function sharply peaked at $x_0$ with unit integral gives $T_\psi[\varphi] \approx \psi(x_0)$, so $\psi$ is recovered from $T_\psi$; and the generalized functions reach beyond the test functions, since $\varphi \mapsto \int\varphi$ is $T_1$ for the constant $1$. The same move appears in [[§49 Position Eigenstates and Continuous Resolutions#^prop-49-3|556 Prop. §49.3]]: a position "eigenket" is not a vector of the Hilbert space but makes sense paired with one.
>
> *Source: the user's PHY 513 notes, App. A §A.4 (Derivation "Three examples, in order of generality") · PHY 513, Problem Set 4, Problem 0*

^rem-ca-2-1

> [!theorem] Lemma §CA.2.1: A Continuous Functional Is Bounded by Finitely Many Seminorms
> 1. If $T \in \mathcal S'$ ([[§CA.2 Generalized Functions#^def-ca-2-3|Def. §CA.2.3]]), there are an integer $M$ and a constant $C$ with $|T[\varphi]| \le C\sum_{|\alpha|, |\beta| \le M}\|\varphi\|_{\alpha,\beta}$ for every $\varphi \in \mathcal S$.
> 2. If $T \in \mathcal D'$ ([[§CA.2 Generalized Functions#^def-ca-2-2|Def. §CA.2.2]]) and $R > 0$, there are an integer $N$ and a constant $C$ with $|T[\varphi]| \le C\sum_{|\beta| \le N}\sup|\partial^\beta\varphi|$ for every $\varphi \in \mathcal D$ that vanishes outside the ball $|x| \le R$.
>
> Conversely, a linear map on $\mathcal S$ with a bound as in 1 is a tempered distribution.
>
> *Source: standard (Hörmander I, §2.1; Reed & Simon I, Ch. V); the proof is written here*

^lem-ca-2-1

> [!derivation]- Derivation
> **Step 1** (part 1, by contradiction). Suppose no pair $M$, $C$ works. Then for each $M = 1, 2, \dots$ the bound fails with $C = M$: there is $\varphi_M \in \mathcal S$ with
>
> $$
> |T[\varphi_M]| > M\sum_{|\alpha|, |\beta| \le M}\|\varphi_M\|_{\alpha,\beta} .
> $$
>
> In particular $T[\varphi_M] \ne 0$. Put $\psi_M = \varphi_M/T[\varphi_M]$; by linearity $T[\psi_M] = 1$ for every $M$.
>
> **Step 2** (the sequence tends to zero). Fix $\alpha$, $\beta$. For $M \ge \max(|\alpha|, |\beta|)$ the seminorm $\|\cdot\|_{\alpha,\beta}$ is one of the terms of the sum, so
>
> $$
> \|\psi_M\|_{\alpha,\beta} = \frac{\|\varphi_M\|_{\alpha,\beta}}{|T[\varphi_M]|} \le \frac{1}{|T[\varphi_M]|}\sum_{|\alpha'|, |\beta'| \le M}\|\varphi_M\|_{\alpha',\beta'} < \frac1M .
> $$
>
> Hence $\|\psi_M\|_{\alpha,\beta} \to 0$ for every $\alpha$, $\beta$: $\psi_M \to 0$ in $\mathcal S$ ([[§CA.2 Generalized Functions#^def-ca-2-1|Def. §CA.2.1]]).
>
> **Step 3** (contradiction). $T$ is continuous, so $T[\psi_M] \to T[0] = 0$; but $T[\psi_M] = 1$. So some pair $M$, $C$ works.
>
> **Step 4** (part 2). The same argument with $\varphi_M \in \mathcal D$ vanishing outside $|x| \le R$ and the sums $\sum_{|\beta| \le M}\sup|\partial^\beta\varphi_M|$: the functions $\psi_M = \varphi_M/T[\varphi_M]$ all vanish outside the one ball $|x| \le R$, and $\sup|\partial^\beta\psi_M| < 1/M$ for $M \ge |\beta|$, so $\psi_M \to 0$ in $\mathcal D$, while $T[\psi_M] = 1$.
>
> **Step 5** (converse). If $|T[\varphi]| \le C\sum_{|\alpha|, |\beta| \le M}\|\varphi\|_{\alpha,\beta}$ and $\varphi_k \to \varphi$ in $\mathcal S$, apply the bound to $\varphi_k - \varphi$: $|T[\varphi_k] - T[\varphi]| \le C\sum\|\varphi_k - \varphi\|_{\alpha,\beta} \to 0$, a finite sum of null sequences.
>
> **What the derivation shows.**
> - Continuity along sequences, as in the definitions, is the same as a bound by finitely many seminorms; the bound is what estimates use (Theorem §CA.2.1, Step 3, proves such a bound directly).
> - In part 2 the order $N$ may depend on the ball: a generalized function has finite order on bounded sets only.
> - Used next: the finite order in the point-support theorem (Theorem §CA.2.2, Step 1) and the last step of Theorem §CA.2.5, 1.

^der-lem-ca-2-1

*Uses:* [[§CA.2 Generalized Functions#^def-ca-2-1|Def. §CA.2.1]], [[§CA.2 Generalized Functions#^def-ca-2-2|Def. §CA.2.2]], [[§CA.2 Generalized Functions#^def-ca-2-3|Def. §CA.2.3]]

> [!theorem] Theorem §CA.2.1: Regular and Singular Tempered Distributions
> 1. $\mathcal D$ is dense in $\mathcal S$, so a tempered distribution ([[§CA.2 Generalized Functions#^def-ca-2-3|Def. §CA.2.3]]) is fixed by its action on $\mathcal D$.
> 2. If $\psi$ is locally integrable and $\int d^nx\,|\psi(x)|(1 + |x|)^{-N} < \infty$ for some $N$, then $T_\psi[\varphi] = \int\psi\varphi$ is a tempered distribution, and $\psi \mapsto T_\psi$ is injective (functions equal almost everywhere identified). Examples: $1$, $e^{i\mathbf k\cdot\mathbf x}$, $\theta(t)$, polynomials, $1/|\mathbf x|$ and $1/|\mathbf x|^2$ on $\mathbb R^3$. Not covered: $1/x$ on $\mathbb R$ (not locally integrable) and $e^x$ (too fast).
> 3. $\partial^\alpha\delta[\varphi] = (-1)^{|\alpha|}\partial^\alpha\varphi(0)$ (δ: [[§CA.2 Generalized Functions#^def-ca-2-4|Def. §CA.2.4]]) is a tempered distribution, and it is $T_\psi$ for no locally integrable $\psi$.
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
> **Step 4** (injectivity, on any open set). Let $U \subseteq \mathbb R^n$ be open and suppose $T_\psi[\varphi] = 0$ for every $\varphi \in \mathcal D$ supported in $U$; the claim is $\psi = 0$ almost everywhere on $U$ (injectivity is the case $U = \mathbb R^n$: if $T_\psi = T_{\psi'}$ then $T_{\psi - \psi'} = 0$). Fix a closed ball $B = \{|x - c| \le R\} \subset U$ and $0 < \varepsilon_0 < R$, and let $h = \psi$ on $B$, $h = 0$ elsewhere; $h \in L^1(\mathbb R^n)$ because $\psi$ is locally integrable. Let $\rho \in \mathcal D$ vanish outside $|x| \le 1$ with $\int\rho = 1$, and $\rho_\varepsilon(x) = \varepsilon^{-n}\rho(x/\varepsilon)$ (the family studied below as a nascent delta function, Theorem §CA.2.5, 3; only the notation is used here).
>
> *(a) The smoothed function vanishes.* For $|x_0 - c| \le R - \varepsilon_0$ and $\varepsilon \le \varepsilon_0$, $y \mapsto \rho_\varepsilon(x_0 - y)$ is a test function that vanishes outside $|y - x_0| \le \varepsilon$, a set inside $B \subset U$. So
>
> $$
> (h \ast \rho_\varepsilon)(x_0) \equiv \int d^ny\,h(y)\,\rho_\varepsilon(x_0 - y) = \int d^ny\,\psi(y)\,\rho_\varepsilon(x_0 - y) = T_\psi\bigl[\rho_\varepsilon(x_0 - \cdot)\bigr] = 0 .
> $$
>
> *(b) The smoothed function tends to $h$ in $L^1$.* Substitute $y = x - \varepsilon u$, $d^ny = \varepsilon^nd^nu$: $(h \ast \rho_\varepsilon)(x) = \int d^nu\,h(x - \varepsilon u)\rho(u)$, and $h(x) = \int d^nu\,h(x)\rho(u)$ since $\int\rho = 1$. Hence, exchanging the order of integration of a nonnegative integrand (Tonelli, [[§25 Invariance Properties and Fubini's Theorem#^thm-25-3|551 Thm. §25.3]]),
>
> $$
> \int d^nx\,\bigl|(h \ast \rho_\varepsilon)(x) - h(x)\bigr| \le \int d^nu\,|\rho(u)|\,\omega(\varepsilon u), \qquad \omega(a) \equiv \int d^nx\,|h(x - a) - h(x)| .
> $$
>
> $\omega(a) \le 2\|h\|_{L^1}$, and $\omega(a) \to 0$ as $a \to 0$ (continuity of translation in $L^1$, [[§25 Invariance Properties and Fubini's Theorem#^thm-25-2|551 Thm. §25.2]]). So the integrand on the right tends to $0$ for every $u$ and is bounded by the integrable $2\|h\|_{L^1}|\rho(u)|$; by dominated convergence ([[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|Theorem §CA.1.1]]) the right side tends to $0$ as $\varepsilon \to 0$.
>
> *(c) Conclusion.* By (a), on the ball $|x - c| \le R - \varepsilon_0$ one has $|\psi| = |h| = |h - h \ast \rho_\varepsilon|$, so $\int_{|x - c| \le R - \varepsilon_0}|\psi| \le \int d^nx\,|h \ast \rho_\varepsilon - h| \to 0$ by (b): the integral of $|\psi|$ over that ball is $0$, and $\psi = 0$ almost everywhere on it ([[§21 Consequences of the Monotone Convergence Theorem#^prop-21-4|551 Prop. §21.4]]). $U$ is a countable union of such balls (rational centres and radii), so $\psi = 0$ almost everywhere on $U$. That $\psi \ast \rho_\varepsilon \to \psi$ in $L^1$ on bounded sets is Lebesgue's approximation theorem (Stein & Shakarchi, Real Analysis, Ch. 3). For continuous $\psi$ this is the peaked-test-function argument of [[§CA.2 Generalized Functions#^rem-ca-2-1|Remark: What changes from the working delta function]].
>
> **Step 5** (derivatives of δ). $|\partial^\alpha\varphi(0)| \le \|\varphi\|_{0,\alpha}$: linear and continuous. Suppose $\partial^\alpha\delta = T_\psi$. On test functions supported away from $0$ both sides give $0$, so by Step 4 with $U = \mathbb R^n \setminus \{0\}$, $\psi = 0$ almost everywhere, and $T_\psi = 0$. But with $\chi$ of Step 1, $\partial^\alpha\delta[x^\alpha\chi] = (-1)^{|\alpha|}\partial^\alpha(x^\alpha\chi)(0) = (-1)^{|\alpha|}\alpha! \ne 0$. Contradiction.
>
> **Step 6** (the examples). $|e^{i\mathbf k\cdot\mathbf x}| = |\theta| = 1$: take $N = n + 1$. A polynomial of degree $d$: $N = d + n + 1$. On $\mathbb R^3$, $\int_{|\mathbf x| < 1}d^3x/|\mathbf x| = 4\pi\int_0^1r\,dr = 2\pi$ and $\int_{|\mathbf x| < 1}d^3x/|\mathbf x|^2 = 4\pi$, finite, and $N = 3$ handles $|\mathbf x| > 1$. On $\mathbb R$, $\int_{-1}^1dx/|x| = \infty$. For $e^x$, the Schwartz function $\varphi = e^{-\sqrt{1 + x^2}}$ gives $e^x\varphi = e^{x - \sqrt{1 + x^2}} \to 1$ as $x \to \infty$, so $\int e^x\varphi$ diverges.
>
> **What the derivation shows.**
> - Polynomial growth is exactly the price of being tempered; local integrability is where $1/x$ fails, which is why it needs the principal value ([[§CA.2 Generalized Functions#^def-ca-2-5|Def. §CA.2.5]]).
> - δ is the first distribution that is no function at all; its derivatives are the next.
> - Step 1 is why physics may test with compactly supported wave packets and still conclude statements in $\mathcal S'$.

^der-ca-2-1

*Uses:* [[§CA.2 Generalized Functions#^def-ca-2-1|Def. §CA.2.1]], [[§CA.2 Generalized Functions#^def-ca-2-2|Def. §CA.2.2]], [[§CA.2 Generalized Functions#^def-ca-2-3|Def. §CA.2.3]], [[§CA.2 Generalized Functions#^def-ca-2-4|Def. §CA.2.4]], [[§25 Invariance Properties and Fubini's Theorem#^thm-25-3|551 Thm. §25.3]], [[§25 Invariance Properties and Fubini's Theorem#^thm-25-2|551 Thm. §25.2]], [[§21 Consequences of the Monotone Convergence Theorem#^prop-21-4|551 Prop. §21.4]], [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|Theorem §CA.1.1]]

## The principal value

One singular generalized function besides δ is needed from the start: $1/x$ is not locally integrable on $\mathbb R$ (Theorem §CA.2.1, 2), and the principal value is the generalized function that replaces it.

> [!definition] Definition §CA.2.5: Principal Value
> For a test function $\varphi$ vanishing outside $[-L, L]$,
>
> $$
> \mathcal P\!\!\int\frac{\varphi(s)}{s}\,ds \equiv \lim_{\delta\to0^+}\Bigl(\int_{-\infty}^{-\delta} + \int_\delta^\infty\Bigr)\frac{\varphi(s)}{s}\,ds = \int_{-L}^{L}\frac{\varphi(s) - \varphi(0)}{s}\,ds .
> $$
>
> The generalized function $\mathcal P\frac1s$ so defined is real and odd and acts as $1/s$ away from $s = 0$.
>
> *Source: the user's PHY 513 notes, App. A §A.5 (Definition "The principal value")*

^def-ca-2-5

## Support and singular support

> [!definition] Definition §CA.2.6: Support and Singular Support
> A distribution $T$ **vanishes** on an open set $U$ if $T[\varphi] = 0$ for every $\varphi \in \mathcal D$ supported in $U$. Its **support** $\operatorname{supp}T$ is the complement of the largest open set on which $T$ vanishes; its **singular support** $\operatorname{sing\,supp}T$ is the complement of the largest open set on which $T$ equals a smooth function ($T[\varphi] = \int g\varphi$ with $g$ smooth there). Both largest sets exist (a distribution that vanishes, or is smooth, near every point of a union of open sets is so on the union: Hörmander I, §2.2).
>
> Examples: $\operatorname{supp}\delta = \operatorname{sing\,supp}\delta = \{0\}$; $\operatorname{supp}\theta = [0, \infty)$, $\operatorname{sing\,supp}\theta = \{0\}$; $\operatorname{supp}\mathcal P\frac1x = \mathbb R$, $\operatorname{sing\,supp}\mathcal P\frac1x = \{0\}$ (the principal value $\mathcal P\frac1x$: [[§CA.2 Generalized Functions#^def-ca-2-5|Def. §CA.2.5]]).
>
> *Source: standard; stated here (Hörmander I, §2.2; Gel'fand & Shilov 1, Ch. I)*

^def-ca-2-6

## Operations on distributions

Operations on generalized functions are defined by moving them onto the test function, one definition per operation.

> [!definition] Definition §CA.2.7: Derivative of a Generalized Function
> The **derivative** of a generalized function $T$ is moved onto the test function: $T'[\varphi] \equiv -T[\varphi']$, and $\partial_\mu T[\varphi] \equiv -T[\partial_\mu\varphi]$.
>
> *Source: the user's PHY 513 notes, App. A §A.4 (Derivation "Operations are defined by transferring them to the test function")*

^def-ca-2-7

> [!definition] Definition §CA.2.8: Product of a Generalized Function with a Smooth Function
> For a smooth function $g$, $(gT)[\varphi] \equiv T[g\varphi]$. Two generalized functions cannot in general be multiplied.
>
> *Source: the user's PHY 513 notes, App. A §A.4 (Derivation "Operations are defined by transferring them to the test function")*

^def-ca-2-8

> [!example] Example §CA.2.1: The Products x·δ = 0 and x·𝒫(1/x) = 1
> On $\mathbb R$, multiply by the smooth function $g(x) = x$ ([[§CA.2 Generalized Functions#^def-ca-2-8|Def. §CA.2.8]]).
> 1. $x\,\delta = 0$: $(x\,\delta)[\varphi] = \delta[x\varphi] = 0\cdot\varphi(0) = 0$ (δ: [[§CA.2 Generalized Functions#^def-ca-2-4|Def. §CA.2.4]]). In the same way $g\,\delta = g(0)\,\delta$ for every smooth $g$, since $\delta[g\varphi] = g(0)\varphi(0)$.
> 2. $x\,\mathcal P\frac1x = 1$: by the second form of [[§CA.2 Generalized Functions#^def-ca-2-5|Def. §CA.2.5]] applied to $x\varphi(x)$, which vanishes at $0$,
>
> $$
> \Bigl(x\,\mathcal P\frac1x\Bigr)[\varphi] = \mathcal P\frac1x[x\varphi] = \int_{-L}^{L}\frac{x\varphi(x) - 0}{x}\,dx = \int\varphi = T_1[\varphi] .
> $$
>
> So multiplication by $x$ removes the delta function and turns the principal value into the constant $1$. Used next: these are the two identities behind the impossibility of a general product ([[§CA.3 Products of Distributions and Operator-Valued Distributions#^thm-ca-3-1|Theorem §CA.3.1]], 3), and with the boundary values $\frac{1}{x \pm i0} = \mathcal P\frac1x \mp i\pi\delta$ ([[§CA.7 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-7-2|Theorem §CA.7.2]]) they give $x\cdot\frac{1}{x \pm i0} = 1$.
>
> *Source: standard; stated here (the two computations of L. Schwartz's impossibility argument, Hörmander I, §§2.2, 8.2)*

^ex-ca-2-1

> [!definition] Definition §CA.2.9: Distributional Limit
> $T_\varepsilon \to T$ (as $\varepsilon \to 0^+$, or along a sequence) means $T_\varepsilon[\varphi] \to T[\varphi]$ for every test function $\varphi$.
>
> *Source: the user's PHY 513 notes, App. A §A.4 (Derivation "Operations are defined by transferring them to the test function")*

^def-ca-2-9

> [!definition] Definition §CA.2.10: Fourier Transform of a Generalized Function
> For a tempered distribution $T$ ([[§CA.2 Generalized Functions#^def-ca-2-3|Def. §CA.2.3]]), $\tilde T[\varphi] \equiv T[\tilde\varphi]$.
>
> *Source: the user's PHY 513 notes, App. A §A.4 (Derivation "Operations are defined by transferring them to the test function")*

^def-ca-2-10

> [!definition] Definition §CA.2.11: Linear Change of Variables
> For an invertible real $n \times n$ matrix $A$ and $a \in \mathbb R^n$, the composition of $T$ with $x \mapsto Ax + a$ is the distribution
>
> $$
> T(Ax + a)[\varphi] \equiv |\det A|^{-1}\,T\bigl[\varphi\bigl(A^{-1}(\cdot - a)\bigr)\bigr] .
> $$
>
> *Source: standard; stated here (Hörmander I, §§3.1, 6.1) · the user's PHY 513 notes, Ch. 6 §6.3 (Derivation "The rules", 3: Lorentz covariance)*

^def-ca-2-11

> [!definition] Definition §CA.2.12: Invariant Distribution
> $T$ is **invariant** under a group of linear changes of variables ([[§CA.2 Generalized Functions#^def-ca-2-11|Def. §CA.2.11]]) if $T(gx) = T$ for every $g$ in the group; **Lorentz invariant** if $T[\varphi\circ\Lambda^{-1}] = T[\varphi]$ for every proper orthochronous $\Lambda$ (for which $|\det\Lambda| = 1$).
>
> *Source: standard; stated here (Hörmander I, §§3.1, 6.1) · the user's PHY 513 notes, Ch. 6 §6.3 (Derivation "The rules", 3: Lorentz covariance)*

^def-ca-2-12

## Distributions supported at a point

> [!theorem] Theorem §CA.2.2: Distributions Supported at a Point
> If $\operatorname{supp}T \subseteq \{a\}$, then $T = \sum_{|\alpha| \le N}c_\alpha\,\partial^\alpha\delta(x - a)$ for some $N$ and constants $c_\alpha$. A distribution known away from a point is therefore fixed up to finitely many derivatives of δ at that point.
>
> *Source: standard; stated here (Hörmander I, §2.3)*

^thm-ca-2-2

> [!derivation]- Derivation
> Take $a = 0$: otherwise replace $T$ by its translate $\varphi \mapsto T[\varphi(\cdot - a)]$, which is supported at $0$ and to which the formula for $a = 0$ applies (this is $T(x + a)$ in the notation of [[§CA.2 Generalized Functions#^def-ca-2-11|Def. §CA.2.11]], with $A = \mathbb 1$).
>
> **Step 1** (finite order). By [[§CA.2 Generalized Functions#^lem-ca-2-1|Lemma §CA.2.1]], 2 with $R = 1$, there are $N$ and $C$ with $|T[\varphi]| \le C\sum_{|\beta| \le N}\sup|\partial^\beta\varphi|$ for all test functions $\varphi$ supported in the ball $|x| \le 1$ (Hörmander I, §2.1).
>
> **Step 2** (split φ). Let $\chi \in \mathcal D$ equal $1$ near $0$, supported in $|x| \le 1$, and let $P_N(x) = \sum_{|\alpha| \le N}\partial^\alpha\varphi(0)\,x^\alpha/\alpha!$ be the Taylor polynomial of $\varphi$ at $0$, $r = \varphi - P_N$. Then $\varphi = \chi P_N + \chi r + (1 - \chi)\varphi$.
>
> **Step 3** (the far piece). $(1 - \chi)\varphi$ vanishes near $0$, hence is supported away from $\operatorname{supp}T$: $T[(1 - \chi)\varphi] = 0$.
>
> **Step 4** (the remainder). $r$ and its derivatives up to order $N$ vanish at $0$, so $|\partial^\beta r(x)| \le C|x|^{N + 1 - |\beta|}$ near $0$. With $\chi_\varepsilon(x) = \chi(x/\varepsilon)$, $\chi r - \chi_\varepsilon r$ vanishes near $0$, so $T[\chi r] = T[\chi_\varepsilon r]$. By Leibniz, every derivative $\partial^\beta(\chi_\varepsilon r)$ with $|\beta| \le N$ is a sum of terms $\varepsilon^{-|\gamma|}(\partial^\gamma\chi)(x/\varepsilon)\,\partial^{\beta - \gamma}r$ supported in $|x| \le \varepsilon$, each at most $C\varepsilon^{-|\gamma|}\varepsilon^{N + 1 - |\beta| + |\gamma|} = C\varepsilon^{N + 1 - |\beta|} \le C\varepsilon$. By Step 1, $|T[\chi r]| \le C'\varepsilon$ for every $\varepsilon$: $T[\chi r] = 0$.
>
> **Step 5** (the polynomial). $T[\chi P_N] = \sum_{|\alpha| \le N}\frac{\partial^\alpha\varphi(0)}{\alpha!}T[\chi x^\alpha]$. With $\partial^\alpha\delta[\varphi] = (-1)^{|\alpha|}\partial^\alpha\varphi(0)$ ([[§CA.2 Generalized Functions#^def-ca-2-7|Def. §CA.2.7]]), this is $\sum_\alpha c_\alpha\,\partial^\alpha\delta[\varphi]$ with $c_\alpha = (-1)^{|\alpha|}T[\chi x^\alpha]/\alpha!$.
>
> **What the derivation shows.**
> - The ambiguity of a distribution at one point is a finite sum of δ-derivatives, never anything spread out.
> - This is the freedom in extending $\theta(x^0)D(x)$ across $x = 0$ ([[§CA.3 Products of Distributions and Operator-Valued Distributions#^thm-ca-3-1|Theorem §CA.3.1]]) and in contact terms of time-ordered products; for a fundamental solution the equation itself removes it ([[§CA.7 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-7-7|Theorem §CA.7.7]], 3).

^der-ca-2-2

*Uses:* [[§CA.2 Generalized Functions#^def-ca-2-6|Def. §CA.2.6]], [[§CA.2 Generalized Functions#^lem-ca-2-1|Lemma §CA.2.1]], [[§CA.2 Generalized Functions#^def-ca-2-4|Def. §CA.2.4]], [[§CA.2 Generalized Functions#^def-ca-2-7|Def. §CA.2.7]], [[§CA.2 Generalized Functions#^def-ca-2-11|Def. §CA.2.11]]

## Derivatives and limits

> [!theorem] Theorem §CA.2.3: Integration by Parts; the Gradient of a Delta Function
> For functions on a region $V$ with outward normal $\hat n$,
>
> $$
> \int_Vd^3x\,(\partial_if)\,g = \oint_{\partial V}dS\,n_i\,f\,g - \int_Vd^3x\,f\,\partial_ig .
> $$
>
> For fields that fall off at infinity, $\int d^3x\,\nabla f\cdot\nabla g = -\int d^3x\,f\,\nabla^2g$, and $\int d^3y\,f(\mathbf y)\,\nabla_{\mathbf y}\delta^3(\mathbf x - \mathbf y) = -\nabla f(\mathbf x)$.
>
> *Source: the user's PHY 513 notes, App. A §A.2 (rule 5), Ch. 4 §4.3*

^thm-ca-2-3

> [!derivation]- Derivation
> **Step 1** (product rule). $\partial_i(fg) = (\partial_if)g + f\,\partial_ig$.
>
> **Step 2** (divergence theorem). Integrate over $V$ and apply [[§28 The Divergence Theorem in Higher Dimensions and Green's Identities#^thm-28-1|452 Thm. §28.1]] to the vector field $fg\,\hat e_i$: $\int_V\partial_i(fg) = \oint_{\partial V}n_ifg$. Rearranging gives the first formula.
>
> **Step 3** (gradients). Take $g \to \partial_ig$ and sum over $i$: $\int_V\nabla f\cdot\nabla g = \oint_{\partial V}f\,\hat n\cdot\nabla g - \int_Vf\nabla^2g$. With $V$ a ball of radius $L \to \infty$, the surface term is dropped when $f\,\partial_rg$ falls off faster than $1/L^2$.
>
> ⚑ By-product: "fields fall off at infinity" is an assumption about the states in which the operators are evaluated (wave packets, not plane waves); it is made every time a surface term is dropped → [[§C2b.1 Heisenberg Fields#^thm-c2b-1-2|§C2b.1, Theorem §C2b.1.2, Step 5]].
>
> **Step 4** (delta function). With $f = \delta^3(\mathbf x - \mathbf y)$ as a function of $\mathbf y$, the surface term vanishes because the delta function is zero on $\partial V$ (its support, the point $\mathbf x$, lies inside); so $\int d^3y\,\delta^3(\mathbf x - \mathbf y)\,\partial_ig(\mathbf y) = -\int d^3y\,\partial_{y^i}\delta^3(\mathbf x - \mathbf y)\,g(\mathbf y)$, i.e. $\int d^3y\,g\,\nabla_{\mathbf y}\delta^3 = -\nabla g(\mathbf x)$. This is also the *definition* of the derivative of $\delta$ ([[§CA.2 Generalized Functions#^def-ca-2-7|Def. §CA.2.7]]).
>
> **What the derivation shows.**
> - Two uses of one move, differing only in which factor kills the surface term: fall-off at infinity, or a delta function supported inside.
> - The four-dimensional version is the step in every Euler–Lagrange and Noether derivation (Euler–Lagrange: [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^der-c1b-2-4|Derivation §C1b.2.4]], step 4; Noether charges: [[§C1b.6 Conserved Charges and Internal Symmetries#^thm-c1b-6-1|Theorem §C1b.6.1]], [[§C1b.8 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^der-c1b-8-4|Derivation §C1b.8.4]], step 7).

^der-ca-2-3

*Uses:* [[§28 The Divergence Theorem in Higher Dimensions and Green's Identities#^thm-28-1|452 Thm. §28.1]], [[§CA.2 Generalized Functions#^def-ca-2-7|Def. §CA.2.7]]

> [!theorem] Theorem §CA.2.4: Every Generalized Function Is Differentiable
> 1. Every generalized function has derivatives of all orders, and for differentiable $\psi$, $(T_\psi)' = T_{\psi'}$.
> 2. $\theta' = \delta$ and $\delta'[\varphi] = -\varphi'(0)$.
>
> *Source: the user's PHY 513 notes, App. A §A.4*

^thm-ca-2-4

> [!derivation]- Derivation
> **Step 1** (part 1). $\varphi'$ is again a test function, so $T'[\varphi] = -T[\varphi']$ is defined, and so are all higher derivatives. For differentiable $\psi$, integration by parts gives $\int\psi'\varphi = [\psi\varphi] - \int\psi\varphi'$, and the boundary term vanishes because $\varphi$ is zero outside a bounded region.
>
> **Step 2** ($\theta' = \delta$). $\theta'[\varphi] = -\int_{-\infty}^\infty\theta\varphi' = -\int_0^\infty\varphi' = -[\varphi]_0^\infty = \varphi(0) = \delta[\varphi]$.
>
> ⚑ By-product: the jump of a step function is a delta function; this is the jump that makes the retarded function a Green's function ([[§C2b.6 Green's Functions and Contours#^thm-c2b-6-5|Theorem §C2b.6.5]], Step 6) and the contact term of time ordering ([[§C2b.7 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-7-1|Theorem §C2b.7.1]], 4).
>
> **Step 3** ($\delta'$). $\delta'[\varphi] = -\delta[\varphi'] = -\varphi'(0)$, which is the rule of [[§CA.2 Generalized Functions#^thm-ca-2-3|Theorem §CA.2.3]], Step 4, seen as a definition.
>
> **What the derivation shows.**
> - Rules that look like tricks ($\theta' = \delta$, $\int e^{ikx} = 2\pi\delta$) are definitions plus one integration by parts or one inversion; the second, the transform of the constant, is [[§CA.4 Fourier Transforms and Fourier Tricks#^thm-ca-4-3|Theorem §CA.4.3]].

^der-ca-2-4

*Uses:* [[§CA.2 Generalized Functions#^def-ca-2-7|Def. §CA.2.7]]

> [!theorem] Lemma §CA.2.2: The Space 𝒮 Is a Complete Metric Space
> Number the countably many seminorms of [[§CA.2 Generalized Functions#^def-ca-2-1|Def. §CA.2.1]] as $p_1, p_2, \dots$, with $p_1(\varphi) = \|\varphi\|_{0,0} = \sup|\varphi|$, and put
>
> $$
> d(\varphi, \psi) = \sum_{j=1}^\infty2^{-j}\min\{1, p_j(\varphi - \psi)\} .
> $$
>
> 1. $d$ is a metric on $\mathcal S$ that depends only on $\varphi - \psi$, and $d(\varphi_k, \varphi) \to 0$ if and only if $\varphi_k \to \varphi$ in $\mathcal S$. If $\sum_{j \le J}p_j(\psi) < r/2$ and $2^{-J} < r/2$, then $d(\psi, 0) < r$.
> 2. $(\mathcal S, d)$ is complete: every Cauchy sequence converges in $\mathcal S$.
>
> *Source: standard (Reed & Simon I, Ch. V; Hörmander I, §7.1); the proof is written here*

^lem-ca-2-2

> [!derivation]- Derivation
> **Step 1** (a metric). The series converges, $d \le \sum_j2^{-j} = 1$. $d$ is symmetric and depends only on $\varphi - \psi$. If $d(\varphi, \psi) = 0$ then $p_1(\varphi - \psi) = \sup|\varphi - \psi| = 0$, so $\varphi = \psi$. Triangle inequality: each $p_j$ satisfies $p_j(\varphi - \chi) \le p_j(\varphi - \psi) + p_j(\psi - \chi)$, and for $a, b \ge 0$, $\min\{1, a + b\} \le \min\{1, a\} + \min\{1, b\}$ (if $a \ge 1$ or $b \ge 1$ the right side is at least $1$; otherwise it is $a + b$); multiply by $2^{-j}$ and sum.
>
> **Step 2** (the same convergence). If $d(\varphi_k, \varphi) \to 0$, then $2^{-j}\min\{1, p_j(\varphi_k - \varphi)\} \le d(\varphi_k, \varphi) \to 0$, so $p_j(\varphi_k - \varphi) \to 0$ for each $j$. Conversely, for any $J$,
>
> $$
> d(\psi, 0) \le \sum_{j \le J}p_j(\psi) + \sum_{j > J}2^{-j} = \sum_{j \le J}p_j(\psi) + 2^{-J} ,
> $$
>
> which is the last claim of part 1; given $\eta > 0$ choose $J$ with $2^{-J} < \eta/2$, and then $d(\varphi_k, \varphi) < \eta$ as soon as $\sum_{j \le J}p_j(\varphi_k - \varphi) < \eta/2$, which holds for large $k$ when $\varphi_k \to \varphi$ in $\mathcal S$. The same two estimates applied to $\varphi_k - \varphi_l$ show that $(\varphi_k)$ is Cauchy for $d$ exactly when it is Cauchy in every seminorm.
>
> **Step 3** (limits exist). Let $(\varphi_k)$ be Cauchy for $d$. For each $\alpha$, $\beta$ the functions $x^\alpha\partial^\beta\varphi_k$ are then Cauchy in the supremum norm, so they converge uniformly on $\mathbb R^n$ to a bounded function $g_{\alpha,\beta}$, which is continuous as a uniform limit of continuous functions ([[§17 Simple Functions and Modes of Convergence#^thm-17-4|551 Thm. §17.4]]). Put $\varphi = g_{0,0}$.
>
> **Step 4** (the limit is smooth, with the right derivatives). Claim: $\partial^\beta\varphi$ exists and equals $g_{0,\beta}$, by induction on $|\beta|$; for $\beta = 0$ this is the definition of $\varphi$. Suppose it holds for $\beta$, and fix a point $x$ and a direction $e_i$. The functions $F_k(r) = \partial^\beta\varphi_k(x + re_i)$ of one variable converge at $r = 0$, and their derivatives $F_k'(r) = \partial_i\partial^\beta\varphi_k(x + re_i)$ converge uniformly in $r$ to $g_{0,\beta + e_i}(x + re_i)$. By [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-3|Theorem §CA.1.3]] the limit $F(r) = g_{0,\beta}(x + re_i) = \partial^\beta\varphi(x + re_i)$ is differentiable with $F' = g_{0,\beta + e_i}(x + re_i)$: $\partial_i\partial^\beta\varphi = g_{0,\beta + e_i}$, a continuous function. So $\varphi$ has continuous partial derivatives of all orders. Pointwise, $x^\alpha\partial^\beta\varphi = x^\alpha g_{0,\beta} = \lim_kx^\alpha\partial^\beta\varphi_k = g_{\alpha,\beta}$, a bounded function: $\|\varphi\|_{\alpha,\beta} < \infty$, so $\varphi \in \mathcal S$, and $\|\varphi_k - \varphi\|_{\alpha,\beta} = \sup|x^\alpha\partial^\beta\varphi_k - g_{\alpha,\beta}| \to 0$. By Step 2, $d(\varphi_k, \varphi) \to 0$.
>
> **What the derivation shows.**
> - Convergence in $\mathcal S$ is convergence in a metric, so continuity along sequences is continuity, and closed sets, balls and Baire's theorem are available.
> - Completeness is the exchange of a limit with derivatives, licensed by uniform convergence of the derivatives (Theorem §CA.1.3), once for each multi-index.

^der-lem-ca-2-2

*Uses:* [[§CA.2 Generalized Functions#^def-ca-2-1|Def. §CA.2.1]], [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-3|Theorem §CA.1.3]], [[§17 Simple Functions and Modes of Convergence#^thm-17-4|551 Thm. §17.4]]

> [!theorem] Theorem §CA.2.5: Distributional Limits
> Let $T_\varepsilon$, $\varepsilon > 0$, be tempered distributions.
> 1. If $T_\varepsilon[\varphi]$ converges as $\varepsilon \to 0^+$ for every $\varphi \in \mathcal S$, the limit $T[\varphi]$ is again a tempered distribution: continuity comes free.
> 2. If $T_\varepsilon \to T$, then $\partial^\alpha T_\varepsilon \to \partial^\alpha T$, and $gT_\varepsilon \to gT$ for every smooth $g$ whose derivatives grow at most polynomially. Limits and derivatives always commute for distributions.
> 3. *(Nascent delta functions)* If $\rho \in L^1(\mathbb R^n)$, $\int\rho = 1$, and $\rho_\varepsilon(x) = \varepsilon^{-n}\rho(x/\varepsilon)$, then $\rho_\varepsilon \to \delta$.
>
> *Source: 1 standard; proved here from the Baire category theorem (uniform boundedness on $\mathcal S$: Reed & Simon I, Ch. V; Hörmander I, §2.1) · 2–3 the user's PHY 513 notes, App. A §A.4 (Derivation "Operations are defined by transferring them to the test function", limits) and §A.5 (the Lorentzian)*

^thm-ca-2-5

> [!derivation]- Derivation
> **Step 1** (part 1: one bound for the whole family). Take any sequence $\varepsilon_k \to 0^+$ and write $T_k = T_{\varepsilon_k}$. By hypothesis $T[\varphi] = \lim_kT_k[\varphi]$ exists for every $\varphi \in \mathcal S$ and does not depend on the sequence; it is linear in $\varphi$ as a limit of linear maps. What has to be shown is continuity. The argument is that of the uniform boundedness principle ([[§42 Uniform Boundedness and Approximation#^thm-42-6|556 Thm. §42.6]], stated there for Banach spaces), run in the complete metric space $(\mathcal S, d)$ of [[§CA.2 Generalized Functions#^lem-ca-2-2|Lemma §CA.2.2]].
>
> *(a) Closed sets that cover $\mathcal S$.* For $M = 1, 2, \dots$ let $A_M = \{\varphi \in \mathcal S : |T_k[\varphi]| \le M \text{ for all } k\}$. Each $A_M$ is closed: if $\varphi_n \in A_M$ and $\varphi_n \to \varphi$, then $T_k[\varphi_n] \to T_k[\varphi]$ for each $k$ (continuity of $T_k$), so $|T_k[\varphi]| \le M$. A convergent sequence of numbers is bounded, so every $\varphi$ lies in some $A_M$: $\mathcal S = \bigcup_MA_M$.
>
> *(b) One of them contains a ball.* A complete metric space is not a countable union of nowhere dense sets (Baire, [[§40 The Baire Category Theorem#^thm-40-4|556 Thm. §40.4]]), so some $A_M$ is not nowhere dense: its closure, which is $A_M$ itself, has an interior point ([[§40 The Baire Category Theorem#^def-40-1|556 Def. §40.1]]). There are $\varphi_0$ and $r > 0$ with $\{\varphi : d(\varphi, \varphi_0) < r\} \subseteq A_M$.
>
> *(c) A bound near zero.* If $d(\psi, 0) < r$, then $d(\varphi_0 + \psi, \varphi_0) = d(\psi, 0) < r$, so $\varphi_0 + \psi \in A_M$ and $|T_k[\psi]| \le |T_k[\varphi_0 + \psi]| + |T_k[\varphi_0]| \le 2M$ for every $k$.
>
> *(d) A bound by seminorms.* Choose $J$ with $2^{-J} < r/2$. For $\varphi \ne 0$ put $s = \sum_{j \le J}p_j(\varphi) > 0$ (already $p_1(\varphi) = \sup|\varphi| > 0$) and $\psi = r\varphi/4s$; then $\sum_{j \le J}p_j(\psi) = r/4 < r/2$, so $d(\psi, 0) < r$ (Lemma §CA.2.2, 1) and by (c)
>
> $$
> |T_k[\varphi]| = \frac{4s}{r}\,|T_k[\psi]| \le \frac{8M}{r}\sum_{j \le J}p_j(\varphi) \qquad\text{for every } k .
> $$
>
> The bound does not depend on $k$, so it passes to the limit: $|T[\varphi]| \le \frac{8M}{r}\sum_{j \le J}p_j(\varphi)$, a finite sum of seminorms. A linear map with such a bound is a tempered distribution ([[§CA.2 Generalized Functions#^lem-ca-2-1|Lemma §CA.2.1]], converse). (Reed & Simon I, Ch. V, prove the same statement from the uniform boundedness principle for Fréchet spaces.)
>
> **Step 2** (part 2). For a fixed $\varphi \in \mathcal S$, $\partial^\alpha\varphi$ is one fixed test function, so by [[§CA.2 Generalized Functions#^def-ca-2-7|Def. §CA.2.7]]
>
> $$
> \partial^\alpha T_\varepsilon[\varphi] = (-1)^{|\alpha|}T_\varepsilon[\partial^\alpha\varphi] \longrightarrow (-1)^{|\alpha|}T[\partial^\alpha\varphi] = \partial^\alpha T[\varphi] .
> $$
>
> Likewise $g\varphi \in \mathcal S$ (Leibniz rule and the polynomial bounds), and by [[§CA.2 Generalized Functions#^def-ca-2-8|Def. §CA.2.8]] $gT_\varepsilon[\varphi] = T_\varepsilon[g\varphi] \to T[g\varphi] = gT[\varphi]$. Both arrows are the definition of the limit ([[§CA.2 Generalized Functions#^def-ca-2-9|Def. §CA.2.9]]) applied to one fixed test function.
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
> - The shape of a nascent delta function is irrelevant; only its integral and integrability matter. The Gaussian of [[§B4.4 Fourier Transforms and the Delta Function#^def-b4-4-2|WO Def. §B4.4.2]], the Lorentzian $\varepsilon/\pi(x^2 + \varepsilon^2)$ of Sokhotski–Plemelj ([[§CA.7 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-7-2|Theorem §CA.7.2]]) and the heat kernel of Fourier inversion ([[§CA.4 Fourier Transforms and Fourier Tricks#^thm-ca-4-1|Theorem §CA.4.1]]) are three choices of $\rho$.

^der-ca-2-5

*Uses:* [[§CA.2 Generalized Functions#^lem-ca-2-1|Lemma §CA.2.1]], [[§CA.2 Generalized Functions#^lem-ca-2-2|Lemma §CA.2.2]], [[§40 The Baire Category Theorem#^thm-40-4|556 Thm. §40.4]], [[§40 The Baire Category Theorem#^def-40-1|556 Def. §40.1]], [[§CA.2 Generalized Functions#^def-ca-2-7|Def. §CA.2.7]], [[§CA.2 Generalized Functions#^def-ca-2-8|Def. §CA.2.8]], [[§CA.2 Generalized Functions#^def-ca-2-9|Def. §CA.2.9]], [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|Theorem §CA.1.1]], [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-3|Theorem §CA.1.3]] (for contrast)

## Changes of variables and invariant distributions

> [!theorem] Theorem §CA.2.6: Composition of δ with a Function
> 1. *(Linear maps)* For $T = T_\psi$ the formula of [[§CA.2 Generalized Functions#^def-ca-2-11|Def. §CA.2.11]] is the substitution rule; in particular $\delta(Ax + a) = |\det A|^{-1}\delta(x + A^{-1}a)$ and $\delta(\lambda x) = |\lambda|^{-n}\delta(x)$.
> 2. *(One variable)* Let $f$ be smooth with simple zeros $x_i$ ($f'(x_i) \ne 0$), and $\rho \in \mathcal D$ with $\int\rho = 1$. Then $\delta(f(x)) \equiv \lim_{\varepsilon\to0^+}\rho_\varepsilon(f(x))$ exists and
>
> $$
> \delta\bigl(f(x)\bigr) = \sum_i\frac{\delta(x - x_i)}{|f'(x_i)|} .
> $$
>
> 3. *(Several variables)* If $f: \mathbb R^n \to \mathbb R$ is smooth and $\nabla f \ne 0$ on $\Sigma = \{f = 0\}$, then $\delta(f) \equiv \lim_{\varepsilon\to0^+}\rho_\varepsilon(f)$ exists and $\delta(f)[\varphi] = \int_\Sigma\varphi\,dS/|\nabla f|$, with $dS$ the area element of the hypersurface $\Sigma$. At a zero where $\nabla f = 0$ the limit need not exist.
>
> *Source: standard; stated here (Hörmander I, §6.1; Gel'fand & Shilov 1, Ch. III) · the working form is [[§B1.2 The Dirac Delta Function and the Helmholtz Theorem#^thm-b1-2-1|EM Theorem §B1.2.1]], 1 and [[§B4.4 Fourier Transforms and the Delta Function#^thm-b4-4-3|WO Theorem §B4.4.3]], 2*

^thm-ca-2-6

> [!derivation]- Derivation
> **Step 1** (part 1). For $T = T_\psi$ substitute $y = Ax + a$, so $x = A^{-1}(y - a)$ and $d^nx = |\det A|^{-1}d^ny$ ([[§25 Change of Variables on General Domains#^thm-25-6|452 Thm. §25.6]], on growing balls, then the limit by dominated convergence); the domain $\mathbb R^n$ is unchanged:
>
> $$
> \int d^nx\,\psi(Ax + a)\,\varphi(x) = |\det A|^{-1}\int d^ny\,\psi(y)\,\varphi\bigl(A^{-1}(y - a)\bigr) .
> $$
>
> This is Def. §CA.2.11 for $T_\psi$. For δ: $\delta(Ax + a)[\varphi] = |\det A|^{-1}\varphi(A^{-1}(0 - a)) = |\det A|^{-1}\varphi(-A^{-1}a)$, which is $|\det A|^{-1}\delta(x + A^{-1}a)[\varphi]$. With $A = \lambda\mathbb 1$, $|\det A| = |\lambda|^n$.
>
> **Step 2** (part 2: localize). Let $\varphi \in \mathcal D$ vanish outside $[-L, L]$ and let $\rho$ vanish outside $[-1, 1]$. Simple zeros are isolated, so $[-L, L]$ contains finitely many, $x_1, \dots, x_k$; choose disjoint open intervals $U_i \ni x_i$ on which $|f'| \ge \frac12|f'(x_i)|$. On the compact rest of $[-L, L]$, $|f| \ge c > 0$; for $\varepsilon < c$, $\rho_\varepsilon(f(x)) = \varepsilon^{-1}\rho(f(x)/\varepsilon) = 0$ there. Only the $U_i$ contribute.
>
> **Step 3** (part 2: substitute). On $U_i$, $f$ is strictly monotone, so $u = f(x)$ is a valid substitution with inverse $x(u)$ and $dx = du/|f'(x(u))|$: the absolute value appears because, for decreasing $f$, the limits of integration flip and absorb the sign of $f'$.
>
> $$
> \int_{U_i}dx\,\varepsilon^{-1}\rho\bigl(f(x)/\varepsilon\bigr)\varphi(x) = \int_{f(U_i)}du\,\varepsilon^{-1}\rho(u/\varepsilon)\,g_i(u), \qquad g_i(u) = \frac{\varphi(x(u))}{|f'(x(u))|} .
> $$
>
> **Step 4** (part 2: limit). $g_i$ is bounded and continuous at $u = 0$ with $g_i(0) = \varphi(x_i)/|f'(x_i)|$, and $f(U_i)$ contains a neighbourhood of $0$. By [[§CA.2 Generalized Functions#^thm-ca-2-5|Theorem §CA.2.5]], 3 (with its closing remark), the integral tends to $g_i(0)$. Summing over $i$ gives the formula; the result does not depend on $\rho$.
>
> ⚑ By-product: $\delta(f)$ depends on the function $f$, not only on its zero set: $\delta(2f) = \frac12\delta(f)$. That is why $\delta(p^2 - m^2)$ and $\delta(p^0 - E_{\mathbf p})$ differ by $2E_{\mathbf p}$, the Jacobian of the invariant measure → [[§CA.2 Generalized Functions#^thm-ca-2-7|Theorem §CA.2.7]].
>
> **Step 5** (part 3). Let $\varphi \in \mathcal D$ with support $K$, and let $\rho$ vanish outside $[-1, 1]$.
>
> *(a) Localize.* At each point $p \in K \cap \Sigma$ some $\partial_if(p) \ne 0$; by continuity there is an open box around $p$, a product $W' \times I$ of an open box $W'$ in the other $n - 1$ coordinates and an open interval $I$ in $x_i$, on which $|\partial_if| \ge c_p > 0$. $K \cap \Sigma$ is compact, so finitely many boxes $V_1, \dots, V_N$ cover it; with $V_0 = \mathbb R^n \setminus (K \cap \Sigma)$ they cover $\mathbb R^n$. Take a partition of unity $\chi_0 + \chi_1 + \cdots + \chi_N = 1$ with $\chi_j$ supported in $V_j$ ([[§65 Partitions of Unity#^thm-65-7|591 Thm. §65.7]]). The support of $\chi_0\varphi$ is a compact set on which $f \ne 0$, so $|f| \ge c > 0$ there and $\rho_\varepsilon(f)\,\chi_0\varphi = 0$ for $\varepsilon < c$. Only the boxes contribute.
>
> *(b) One box.* In $V_j = W' \times I$ name the coordinates so that $i = n$, $x = (x', x_n)$. By Fubini ([[§25 Invariance Properties and Fubini's Theorem#^thm-25-6|551 Thm. §25.6]]; the integrand is bounded with compact support)
>
> $$
> \int d^nx\,\rho_\varepsilon\bigl(f(x)\bigr)\,(\chi_j\varphi)(x) = \int_{W'}d^{n-1}x'\int_Idx_n\,\rho_\varepsilon\bigl(f(x', x_n)\bigr)\,(\chi_j\varphi)(x', x_n) .
> $$
>
> At fixed $x'$, $x_n \mapsto f(x', x_n)$ is strictly monotone on $I$ with $|\partial_nf| \ge c_j$, so $u = f(x', x_n)$ is a substitution as in Step 3, with inverse $x_n(x', u)$: the inner integral is $\int du\,\rho_\varepsilon(u)\,g_{x'}(u)$ with $g_{x'}(u) = (\chi_j\varphi)(x', x_n(x', u))/|\partial_nf(x', x_n(x', u))|$ on the interval $f(x', I)$ and $0$ elsewhere. As a function of $x_n$, $\chi_j\varphi$ vanishes outside a compact subset of $I$, so $g_{x'}$ is continuous on $\mathbb R$, and $|g_{x'}| \le \sup|\varphi|/c_j$. By [[§CA.2 Generalized Functions#^thm-ca-2-5|Theorem §CA.2.5]], 3 the inner integral tends to $g_{x'}(0)$, which is $(\chi_j\varphi)(x', Y(x'))/|\partial_nf(x', Y(x'))|$ if $f(x', \cdot)$ has a zero $Y(x')$ in $I$ and $0$ if it has none. The inner integral is bounded by $\|\rho\|_{L^1}\sup|\varphi|/c_j$ on the bounded set $W'$, so by dominated convergence ([[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|Theorem §CA.1.1]])
>
> $$
> \int d^nx\,\rho_\varepsilon(f)\,\chi_j\varphi \longrightarrow \int_{W'_j}d^{n-1}x'\,\frac{(\chi_j\varphi)(x', Y(x'))}{|\partial_nf(x', Y(x'))|} ,
> $$
>
> where $W'_j \subseteq W'$ is the set of $x'$ for which the zero exists. By the implicit function theorem ([[§15 The Implicit Function Theorem#^thm-15-2|452 Thm. §15.2]]) $W'_j$ is open and $Y$ is continuously differentiable on it, with $\partial_iY = -\partial_if/\partial_nf$.
>
> *(c) The surface element.* $\Sigma \cap V_j$ is the graph $x_n = Y(x')$, $x' \in W'_j$. The area element of a graph is $dS = \sqrt{1 + |\nabla'Y|^2}\,d^{n-1}x'$: for $n = 3$ this is $|\mathbf X_u \times \mathbf X_v|\,du\,dv$ of [[§31 Surface Integrals#^def-31-5|452 Def. §31.5]] with $\mathbf X(u, v) = (u, v, Y(u, v))$, $\mathbf X_u \times \mathbf X_v = (-Y_u, -Y_v, 1)$; for general $n$ it is the square root of the Gram determinant $\det(\mathbb 1 + \nabla'Y\,\nabla'Y^{\mathsf T}) = 1 + |\nabla'Y|^2$ (eigenvalue $1 + |\nabla'Y|^2$ on $\nabla'Y$, eigenvalue $1$ on its orthogonal complement), taken here as the definition of the element of a hypersurface. With $\partial_iY = -\partial_if/\partial_nf$, $1 + |\nabla'Y|^2 = |\nabla f|^2/(\partial_nf)^2$, so
>
> $$
> \frac{d^{n-1}x'}{|\partial_nf|} = \frac{dS}{|\nabla f|} .
> $$
>
> *(d) Sum.* $\chi_0$ vanishes on $K \cap \Sigma$, so $\sum_{j \ge 1}\chi_j = 1$ there, and
>
> $$
> \delta(f)[\varphi] = \sum_{j=1}^N\int_{\Sigma \cap V_j}\chi_j\varphi\,\frac{dS}{|\nabla f|} = \int_\Sigma\varphi\,\frac{dS}{|\nabla f|} ,
> $$
>
> the integral over $\Sigma$ being the sum over the graph patches. This is the coarea formula $d^nx = dS\,du/|\nabla f|$ in the form needed here.
>
> **Step 6** (a critical zero). For $f(x) = x^2$ on $\mathbb R$, $f'(0) = 0$. With $x = \sqrt{\varepsilon v}$ on $x > 0$, $dx = \sqrt\varepsilon\,dv/2\sqrt v$, and $\int_0^\infty\varepsilon^{-1}\rho(x^2/\varepsilon)\varphi(x)\,dx = \frac{1}{2\sqrt\varepsilon}\int_0^\infty\rho(v)\varphi(\sqrt{\varepsilon v})\frac{dv}{\sqrt v}$, which diverges like $\varepsilon^{-1/2}$ when $\varphi(0) \ne 0$ and $\int_0^\infty\rho(v)v^{-1/2}dv \ne 0$: $\delta(x^2)$ does not exist on $\mathbb R$.
>
> **What the derivation shows.**
> - Composition is a limit, and it needs only simple zeros; $1/|f'(x_i)|$ is the Jacobian of the substitution, which blows up at a critical zero.
> - In four dimensions $x^2 = (x^0)^2 - \mathbf x^2$ has its only critical point at the origin, where the singularity turns out to be integrable: $\delta(x^2)$ exists on $\mathbb R^4$ ([[§CA.2 Generalized Functions#^thm-ca-2-7|Theorem §CA.2.7]], 2).

^der-ca-2-6

*Uses:* [[§CA.2 Generalized Functions#^def-ca-2-11|Def. §CA.2.11]], [[§CA.2 Generalized Functions#^thm-ca-2-5|Theorem §CA.2.5]], [[§25 Change of Variables on General Domains#^thm-25-6|452 Thm. §25.6]], [[§CA.2 Generalized Functions#^def-ca-2-4|Def. §CA.2.4]], [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|Theorem §CA.1.1]], [[§25 Invariance Properties and Fubini's Theorem#^thm-25-6|551 Thm. §25.6]], [[§15 The Implicit Function Theorem#^thm-15-2|452 Thm. §15.2]], [[§31 Surface Integrals#^def-31-5|452 Def. §31.5]], [[§65 Partitions of Unity#^thm-65-7|591 Thm. §65.7]]

> [!theorem] Theorem §CA.2.7: Invariant Distributions on the Mass Shell and the Light Cone
> Let $m > 0$ and $E_{\mathbf p} = \sqrt{\mathbf p^2 + m^2}$.
> 1. $\theta(\pm p^0)\,\delta(p^2 - m^2)$ is a tempered distribution on $\mathbb R^4$, acting as $\varphi \mapsto \int d^3p\,\varphi(\pm E_{\mathbf p}, \mathbf p)/2E_{\mathbf p}$, and it is Lorentz invariant.
> 2. In position space, with $r = |\mathbf x|$, $\theta(\pm x^0)\,\delta(x^2)$ is a tempered distribution acting as $\varphi \mapsto \int d^3x\,\varphi(\pm r, \mathbf x)/2r$; it is the limit $\mu \to 0^+$ of $\theta(\pm x^0)\delta(x^2 - \mu^2)$, and it is Lorentz invariant; so is $\operatorname{sgn}(x^0)\,\delta(x^2)$.
> 3. $\theta(p^0)$ by itself is not Lorentz invariant.
>
> *Source: the user's PHY 513 notes, Ch. 4 §4.9 (the invariant measure), Ch. 6 §6.3 (Principle "Free fields live on the mass shell") · stated here as distributions (standard: Gel'fand & Shilov 1, Ch. III)*

^thm-ca-2-7

> [!derivation]- Derivation
> **Step 1** (the $p^0$ integral at fixed $\mathbf p$). $f(p^0) = (p^0)^2 - E_{\mathbf p}^2$ has the simple zeros $\pm E_{\mathbf p}$, with $|f'(\pm E_{\mathbf p})| = 2E_{\mathbf p} \ge 2m > 0$. By [[§CA.2 Generalized Functions#^thm-ca-2-6|Theorem §CA.2.6]], 2,
>
> $$
> \delta(p^2 - m^2) = \frac{\delta(p^0 - E_{\mathbf p}) + \delta(p^0 + E_{\mathbf p})}{2E_{\mathbf p}} .
> $$
>
> The product with $\theta(\pm p^0)$ is taken before the limit that defines the delta function. Let $\rho \in \mathcal D(\mathbb R)$ vanish outside $[-1, 1]$ with $\int\rho = 1$, and let $0 < \varepsilon \le m^2/2$. On the support of $\rho_\varepsilon(p^2 - m^2)$, $|p^2 - m^2| \le \varepsilon$, so $(p^0)^2 \ge E_{\mathbf p}^2 - \varepsilon \ge E_{\mathbf p}^2/2 > 0$: the support has two pieces, $p^0 \ge E_{\mathbf p}/\sqrt2$ and $p^0 \le -E_{\mathbf p}/\sqrt2$, and $\theta(\pm p^0)$ is constant near each. Hence
>
> $$
> \Delta^\pm_\varepsilon(p) \equiv \theta(\pm p^0)\,\rho_\varepsilon(p^2 - m^2)
> $$
>
> is a smooth function on $\mathbb R^4$, and $\theta(\pm p^0)\,\delta(p^2 - m^2) \equiv \lim_{\varepsilon\to0^+}\Delta^\pm_\varepsilon$. (The same product is the one of [[§CA.3 Products of Distributions and Operator-Valued Distributions#^thm-ca-3-1|Theorem §CA.3.1]], 2, in the next section, $\theta$ being smooth near the support of $\delta(p^2 - m^2)$; the direct definition keeps this derivation independent of it.) At fixed $\mathbf p$, on the piece $p^0 > 0$ substitute $u = (p^0)^2 - E_{\mathbf p}^2$, so $p^0 = \sqrt{E_{\mathbf p}^2 + u}$ and $dp^0 = du/2\sqrt{E_{\mathbf p}^2 + u}$:
>
> $$
> \int dp^0\,\Delta^+_\varepsilon(p)\,\varphi(p^0, \mathbf p) = \int du\,\rho_\varepsilon(u)\,g_{\mathbf p}(u), \qquad g_{\mathbf p}(u) = \frac{\varphi\bigl(\sqrt{E_{\mathbf p}^2 + u}, \mathbf p\bigr)}{2\sqrt{E_{\mathbf p}^2 + u}} .
> $$
>
> For $|u| \le \varepsilon$, $2\sqrt{E_{\mathbf p}^2 + u} \ge \sqrt2E_{\mathbf p}$, so $g_{\mathbf p}$ is continuous at $u = 0$ and bounded there by $\sup_{p^0}|\varphi(p^0, \mathbf p)|/\sqrt2E_{\mathbf p}$; the integral tends to $g_{\mathbf p}(0) = \varphi(E_{\mathbf p}, \mathbf p)/2E_{\mathbf p}$ ([[§CA.2 Generalized Functions#^thm-ca-2-5|Theorem §CA.2.5]], 3, with its closing remark). On the piece $p^0 < 0$ the substitution $p^0 = -\sqrt{E_{\mathbf p}^2 + u}$ gives in the same way $\int dp^0\,\Delta^-_\varepsilon\,\varphi \to \varphi(-E_{\mathbf p}, \mathbf p)/2E_{\mathbf p}$. So the product keeps one root: $\int dp^0\,\theta(\pm p^0)\delta(p^2 - m^2)\varphi(p^0, \mathbf p) = \varphi(\pm E_{\mathbf p}, \mathbf p)/2E_{\mathbf p}$. The same result follows from part 3 of Theorem §CA.2.6 in all four variables, since $\nabla(p^2 - m^2) = 2(p^0, -\mathbf p) \ne 0$ on the shell ($p^0 = \pm E_{\mathbf p} \ne 0$).
>
> **Step 2** (tempered). Write $T_\pm[\varphi] = \int d^3p\,\varphi(\pm E_{\mathbf p}, \mathbf p)/2E_{\mathbf p}$. With $|\varphi(p)| \le (1 + |p|)^{-4}\sup_q(1 + |q|)^4|\varphi(q)|$, $|p| \ge |\mathbf p|$ and $1/2E_{\mathbf p} \le 1/2m$,
>
> $$
> |T_\pm[\varphi]| \le \frac{1}{2m}\int\frac{d^3p}{(1 + |\mathbf p|)^4}\cdot\sup_q(1 + |q|)^4|\varphi(q)| ,
> $$
>
> and the integral is finite ($4\pi\int_0^\infty p^2dp/(1 + p)^4 < \infty$). As in [[§CA.2 Generalized Functions#^thm-ca-2-1|Theorem §CA.2.1]], Step 3, $T_\pm$ is continuous on $\mathcal S$. The same bound gives the limit on $\mathbb R^4$: by Step 1 the $p^0$-integral of $\Delta^\pm_\varepsilon\varphi$ is at most $\|\rho\|_{L^1}\sup_{p^0}|\varphi(p^0, \mathbf p)|/\sqrt2m \le C(1 + |\mathbf p|)^{-4}$, integrable over $d^3p$ and independent of $\varepsilon$, and it converges at each $\mathbf p$; by dominated convergence $\int d^4p\,\Delta^\pm_\varepsilon\,\varphi \to T_\pm[\varphi]$ for every $\varphi \in \mathcal S(\mathbb R^4)$. So $\theta(\pm p^0)\delta(p^2 - m^2) = T_\pm$ as a limit in $\mathcal S'(\mathbb R^4)$.
>
> **Step 3** (invariance, upper shell). Let $\Lambda$ be proper orthochronous: $\Lambda^{\mathsf T}g\Lambda = g$, $\det\Lambda = 1$, $\Lambda^0{}_0 \ge 1$. By [[§CA.2 Generalized Functions#^def-ca-2-11|Def. §CA.2.11]], $T_+(\Lambda p)[\varphi] = T_+[\varphi\circ\Lambda^{-1}]$ (since $|\det\Lambda| = 1$), and the claim is $T_+[\varphi\circ\Lambda^{-1}] = T_+[\varphi]$.
>
> *(a) The sign of $p^0$ on timelike vectors.* From $\Lambda^{\mathsf T}g\Lambda = g$, $\Lambda^{-1} = g\Lambda^{\mathsf T}g$, hence $\Lambda g\Lambda^{\mathsf T} = g$, whose $00$ component is $(\Lambda^0{}_0)^2 - \sum_i(\Lambda^0{}_i)^2 = 1$. Let $p^2 > 0$ and $p^0 > 0$, so $|\mathbf p| < p^0$. By the Cauchy–Schwarz inequality $\bigl|\sum_i\Lambda^0{}_ip^i\bigr| \le \sqrt{(\Lambda^0{}_0)^2 - 1}\,|\mathbf p| < \Lambda^0{}_0\,p^0$, so $(\Lambda p)^0 = \Lambda^0{}_0p^0 + \sum_i\Lambda^0{}_ip^i > 0$; applied to $-p$, $p^0 < 0$ gives $(\Lambda p)^0 < 0$. (The same fact: [[§B1.3 Causal Structure and Proper Time#^thm-b1-3-1|REL Theorem §B1.3.1]], 2.) Also $(\Lambda p)^2 = p^2$.
>
> *(b) The regularized functions are invariant.* Where $\rho_\varepsilon(p^2 - m^2) \ne 0$, $p^2 \ge m^2 - \varepsilon > 0$, so $p$ is timelike and by (a) $\theta((\Lambda p)^0) = \theta(p^0)$; and $\rho_\varepsilon((\Lambda p)^2 - m^2) = \rho_\varepsilon(p^2 - m^2)$ everywhere. Hence $\Delta^+_\varepsilon(\Lambda p) = \Delta^+_\varepsilon(p)$ for all $p$.
>
> *(c) Change variables.* Substitute $p = \Lambda q$ ($|\det\Lambda| = 1$, $\Lambda\mathbb R^4 = \mathbb R^4$; [[§25 Change of Variables on General Domains#^thm-25-6|452 Thm. §25.6]], as in Step 1 of Theorem §CA.2.6):
>
> $$
> \int d^4p\,\Delta^+_\varepsilon(p)\,\varphi(\Lambda^{-1}p) = \int d^4q\,\Delta^+_\varepsilon(\Lambda q)\,\varphi(q) = \int d^4q\,\Delta^+_\varepsilon(q)\,\varphi(q) .
> $$
>
> *(d) The limit.* $\varphi\circ\Lambda^{-1} \in \mathcal S$, so by Step 2 the left side tends to $T_+[\varphi\circ\Lambda^{-1}]$ and the right side to $T_+[\varphi]$.
>
> ⚑ By-product: written out, $T_+[\varphi\circ\Lambda^{-1}] = T_+[\varphi]$ is $\int\frac{d^3p}{2E_{\mathbf p}}\varphi\bigl(\Lambda^{-1}(E_{\mathbf p}, \mathbf p)\bigr) = \int\frac{d^3p}{2E_{\mathbf p}}\varphi(E_{\mathbf p}, \mathbf p)$: the measure $d^3p/2E_{\mathbf p}$ on the upper shell is invariant → the physics form, with the same argument in $\delta$-function notation, is [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-3|Theorem §C2a.4.3]], 2.
>
> **Step 4** (lower shell). Let $\psi(p) = \varphi(-p)$. Then $\varphi(-E_{\mathbf p}, \mathbf p) = \psi(E_{\mathbf p}, -\mathbf p)$, and the linear change of variables $\mathbf p \to -\mathbf p$ on $\mathbb R^3$ ($|\det(-\mathbb 1)| = 1$, [[§25 Change of Variables on General Domains#^thm-25-6|452 Thm. §25.6]]; $E_{-\mathbf p} = E_{\mathbf p}$) gives $T_-[\varphi] = T_+[\psi]$. Since $\Lambda$ is linear, $(\varphi\circ\Lambda^{-1})(-p) = \varphi(\Lambda^{-1}(-p)) = (\psi\circ\Lambda^{-1})(p)$, so $T_-[\varphi\circ\Lambda^{-1}] = T_+[\psi\circ\Lambda^{-1}] = T_+[\psi] = T_-[\varphi]$ by Step 3.
>
> **Step 5** (light cone: the limit). Steps 1–4 with $x$ in place of $p$ and $\mu$ in place of $m$ define the invariant distributions $T^\mu_\pm[\varphi] = \int d^3x\,\varphi(\pm\sqrt{r^2 + \mu^2}, \mathbf x)/2\sqrt{r^2 + \mu^2}$. As $\mu \to 0^+$ the integrand tends to $\varphi(\pm r, \mathbf x)/2r$ for $r > 0$ and is bounded by $\frac{1}{2r}(1 + r)^{-4}\sup(1 + |q|)^4|\varphi(q)|$, integrable on $\mathbb R^3$ because $\int_{r < 1}d^3x/2r = \pi$. By dominated convergence $T^\mu_\pm[\varphi] \to \int d^3x\,\varphi(\pm r, \mathbf x)/2r$; by [[§CA.2 Generalized Functions#^thm-ca-2-5|Theorem §CA.2.5]], 1 the limit is tempered.
>
> ⚑ By-product: at the origin $\nabla(x^2) = 0$ and Theorem §CA.2.6, 3 does not apply; $\delta(x^2)$ is *defined* there by this limit, and it exists only because $1/r$ is integrable in three dimensions (contrast Theorem §CA.2.6, Step 6, on $\mathbb R$).
>
> **Step 6** (light cone: invariance). Each $T^\mu_\pm$ is invariant (Steps 3–4), so $T^\mu_\pm[\varphi\circ\Lambda^{-1}] = T^\mu_\pm[\varphi]$; both sides converge as $\mu \to 0^+$ (Step 5, applied to $\varphi\circ\Lambda^{-1}$ and to $\varphi$), so the limits agree. $\operatorname{sgn}(x^0)\delta(x^2) = T^0_+ - T^0_-$ is invariant as a difference of invariant distributions.
>
> **Step 7** (part 3). For spacelike $p = (a, b, 0, 0)$ with $0 < a < b$, the boost with velocity $v$ along $x^1$, $a/b < v < 1$, gives $p'^0 = \gamma(a - vb) < 0$. So $\theta(p^0)$ changes value on an open set of spacelike $p$; only on timelike and null vectors is the sign of $p^0$ invariant, which is why the products with $\delta(p^2 - m^2)$ and $\delta(x^2)$ are.
>
> **What the derivation shows.**
> - The invariant measure $d^3p/2E_{\mathbf p}$ is the action of an invariant distribution; $1/2E_{\mathbf p}$ is the Jacobian of Theorem §CA.2.6.
> - Assumptions: $m > 0$ for the shell (so the zeros are simple and $1/2E_{\mathbf p}$ is bounded), proper orthochronous $\Lambda$.
> - The light-cone distribution $\operatorname{sgn}(x^0)\delta(x^2)$ is the massless commutator function ([[§C2b.5 Microcausality and the Commutator Function#^thm-c2b-5-8|Theorem §C2b.5.8]]).

^der-ca-2-7

*Uses:* [[§CA.2 Generalized Functions#^thm-ca-2-6|Theorem §CA.2.6]], [[§CA.2 Generalized Functions#^def-ca-2-11|Def. §CA.2.11]], [[§CA.2 Generalized Functions#^thm-ca-2-1|Theorem §CA.2.1]], [[§CA.2 Generalized Functions#^thm-ca-2-5|Theorem §CA.2.5]], [[§25 Change of Variables on General Domains#^thm-25-6|452 Thm. §25.6]]

> [!remark]- Connections
> - Distributions as linear maps on test functions are a dual space: the generalized functions sit in the dual of the test functions as kets sit in the dual of bras; the position "eigenket" that is not a vector is the same phenomenon ([[§49 Position Eigenstates and Continuous Resolutions#^prop-49-3|556 Prop. §49.3]]). Operator-valued distributions ([[§CA.3 Products of Distributions and Operator-Valued Distributions#^def-ca-3-1|Def. §CA.3.1]]) carry the same idea one level up: $\hat\phi(x)$ is no more an operator than $|x\rangle$ is a vector.
> - The composition rule $\delta(f(x)) = \sum_i\delta(x - x_i)/|f'(x_i)|$ ([[§B1.2 The Dirac Delta Function and the Helmholtz Theorem#^thm-b1-2-1|EM Theorem §B1.2.1]], justified as a limit in Theorem §CA.2.6) is what turns $\theta(p^0)\delta(p^2 - m^2)$ into the invariant measure $d^3p/2E_{\mathbf p}$ ([[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-2|Def. §C2a.4.2]]) and $\delta(t^2 - r^2)$ into the light-cone deltas of the massless commutator.
> - Limits commute with derivatives for distributions (Theorem §CA.2.5, 2) but not for functions ([[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-3|Theorem §CA.1.3]]); C2a–C2b need the function version only where it wants a pointwise formula, as in the real-variable evaluation of the Wightman function ([[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-3|Theorem §C2b.3.3]]).
> - The point-support theorem (Theorem §CA.2.2) is also why, in the renormalization of later chapters, products at a point are ambiguous only by local terms (the second semester, planned: PHY 513 Lecture 17, slide 26).
> - The spectrum of a matrix as the distribution $\frac1N\sum_i\delta(x - \lambda_i)$ ([[§CA.2 Generalized Functions#^def-ca-2-4|Def. §CA.2.4]]) and its limits (Theorem §CA.2.5) become, for random matrices, empirical spectral measures and their weak convergence ([[§R2.7 Weak Convergence, Characteristic Functions and Concentration#^def-r2-7-11|Thesis Def. §R2.7.11]], [[§R2.7 Weak Convergence, Characteristic Functions and Concentration#^def-r2-7-1|Thesis Def. §R2.7.1]]).
> - Integration by parts with a delta function is how $[\hat\pi, \hat H]$ acquires $\nabla^2\hat\phi$ ([[§C2b.1 Heisenberg Fields#^thm-c2b-1-2|Theorem §C2b.1.2]]); the divergence theorem behind it is [[§28 The Divergence Theorem in Higher Dimensions and Green's Identities#^thm-28-1|452 Thm. §28.1]], and the four-dimensional version is the step in every Euler–Lagrange and Noether derivation (Euler–Lagrange: [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^der-c1b-2-4|Derivation §C1b.2.4]], step 4; Noether charges: [[§C1b.6 Conserved Charges and Internal Symmetries#^thm-c1b-6-1|Theorem §C1b.6.1]], [[§C1b.8 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^der-c1b-8-4|Derivation §C1b.8.4]], step 7).
> - **Used in**, statement by statement (C2a–C2b items):
>   - Def. §CA.2.1–§CA.2.2 (test functions; distributions): wave packets and smeared fields — [[§C2a.1 Canonical Quantization of Fields#^def-c2a-1-1|Def. §C2a.1.1]], [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-4|Theorem §C2a.4.4]], [[§C2b.9 Particle Production by a Classical Source#^thm-c2b-9-1|Theorem §C2b.9.1]], [[§C2a.1 Canonical Quantization of Fields|§C2a.1]] (Mathematical background), [[§C2b.6 Green's Functions and Contours#^rem-c2b-6-1|§C2b.6, Remark: What a Green's "function" is, and why it is not unique]].
>   - Theorem §CA.2.1 (regular and singular distributions): δ, plane waves and $\langle\mathbf p|\mathbf q\rangle$ as tempered distributions — [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-5|Theorem §C2a.4.5]], [[§C2b.2 The Wightman Function#^thm-c2b-2-3|Theorem §C2b.2.3]], [[§C2b.5 Microcausality and the Commutator Function#^thm-c2b-5-9|Theorem §C2b.5.9]], [[§C2b.7 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-7-9|Theorem §C2b.7.9]], [[§C2b.8 Wick Rotation and the Two-Point Family#^thm-c2b-8-4|Theorem §C2b.8.4]], [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-1|Theorem §C2b.3.1]].
>   - Def. §CA.2.6 (support, singular support): the singular support of $D_W$ is the light cone; microcausality as the support of $D$ — [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-3|Theorem §C2b.3.3]], [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-6|Theorem §C2b.3.6]], [[§C2b.5 Microcausality and the Commutator Function#^thm-c2b-5-4|Theorem §C2b.5.4]], [[§C2b.5 Microcausality and the Commutator Function#^thm-c2b-5-6|Theorem §C2b.5.6]], [[§C2b.6 Green's Functions and Contours#^thm-c2b-6-6|Theorem §C2b.6.6]], [[§C2b.5 Microcausality and the Commutator Function#^thm-c2b-5-10|Theorem §C2b.5.10]].
>   - Theorem §CA.2.2 (point support): extending $\theta(x^0)D$ across the origin; contact terms — [[§C2b.1 Heisenberg Fields#^thm-c2b-1-3|Theorem §C2b.1.3]], [[§C2b.6 Green's Functions and Contours#^thm-c2b-6-6|Theorem §C2b.6.6]], [[§C2b.7 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-7-4|Theorem §C2b.7.4]].
>   - Defs. §CA.2.7–§CA.2.10 (operations: derivative, product with a smooth function, limit, transform): differentiating mode integrals of operator fields, "use the support of the delta" — [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-2|Theorem §C2a.2.2]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-3|Theorem §C2a.2.3]], [[§C2a.6 Coherent States and the Classical Field#^thm-c2a-6-4|Theorem §C2a.6.4]], [[§C2b.1 Heisenberg Fields#^thm-c2b-1-4|Theorem §C2b.1.4]], [[§C2b.1 Heisenberg Fields#^thm-c2b-1-6|Theorem §C2b.1.6]], [[§C2b.1 Heisenberg Fields#^thm-c2b-1-2|Theorem §C2b.1.2]], [[§C2b.2 The Wightman Function#^thm-c2b-2-2|Theorem §C2b.2.2]], [[§C2b.2 The Wightman Function#^thm-c2b-2-4|Theorem §C2b.2.4]], [[§C2b.5 Microcausality and the Commutator Function#^thm-c2b-5-11|Theorem §C2b.5.11]], [[§C2b.6 Green's Functions and Contours#^thm-c2b-6-3|Theorem §C2b.6.3]], [[§C2b.6 Green's Functions and Contours#^thm-c2b-6-5|Theorem §C2b.6.5]], [[§C2b.7 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-7-9|Theorem §C2b.7.9]], [[§C2b.9 Particle Production by a Classical Source#^thm-c2b-9-1|Theorem §C2b.9.1]], [[§C2b.7 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-7-8|Theorem §C2b.7.8]], [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-5|Theorem §C2a.3.5]], [[§C2b.2 The Wightman Function#^thm-c2b-2-5|Theorem §C2b.2.5]], [[§C2b.6 Green's Functions and Contours#^thm-c2b-6-4|Theorem §C2b.6.4]], [[§C2a.2 Mode Expansion and the Mode Algebra#^lem-c2a-2-1|Lemma §C2a.2.1]].
>   - Theorem §CA.2.4 (every distribution is differentiable; $\theta' = \delta$): contact terms of step functions in time — [[§C2b.6 Green's Functions and Contours#^thm-c2b-6-5|Theorem §C2b.6.5]], [[§C2b.7 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-7-1|Theorem §C2b.7.1]], [[§C2b.7 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-7-5|Theorem §C2b.7.5]], [[P2 Green's Functions by Contour Integration#^p2-7|P2, step 7]].
>   - Theorem §CA.2.5 (distributional limits): every $\varepsilon \to 0^+$ — [[§C2a.1 Canonical Quantization of Fields#^thm-c2a-1-3|Theorem §C2a.1.3]], [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-3|Theorem §C2a.3.3]], [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-5|Theorem §C2a.4.5]], [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-7|Theorem §C2a.4.7]], [[§C2b.2 The Wightman Function#^thm-c2b-2-5|Theorem §C2b.2.5]], [[§C2b.5 Microcausality and the Commutator Function#^thm-c2b-5-12|Theorem §C2b.5.12]], [[§C2b.7 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-7-2|Theorem §C2b.7.2]].
>   - Defs. §CA.2.11, §CA.2.12 and Theorem §CA.2.6 (changes of variables, composition): Lorentz invariance as a statement about distributions, $\delta(p^2 - m^2)$ — [[§C2a.1 Canonical Quantization of Fields#^thm-c2a-1-3|Theorem §C2a.1.3]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|Theorem §C2a.2.6]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-7|Theorem §C2a.2.7]], [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-3|Theorem §C2a.4.3]], [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-4|Theorem §C2a.4.4]], [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-5|Theorem §C2a.4.5]], [[§C2b.2 The Wightman Function#^thm-c2b-2-1|Theorem §C2b.2.1]], [[§C2b.2 The Wightman Function#^thm-c2b-2-2|Theorem §C2b.2.2]], [[§C2b.2 The Wightman Function#^thm-c2b-2-3|Theorem §C2b.2.3]], [[§C2b.2 The Wightman Function#^thm-c2b-2-4|Theorem §C2b.2.4]], [[§C2b.5 Microcausality and the Commutator Function#^thm-c2b-5-4|Theorem §C2b.5.4]], [[§C2b.5 Microcausality and the Commutator Function#^thm-c2b-5-6|Theorem §C2b.5.6]], [[§C2b.5 Microcausality and the Commutator Function#^thm-c2b-5-8|Theorem §C2b.5.8]], [[§C2b.1 Heisenberg Fields#^thm-c2b-1-3|Theorem §C2b.1.3]], [[§C2b.6 Green's Functions and Contours#^thm-c2b-6-6|Theorem §C2b.6.6]], [[§C2b.7 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-7-2|Theorem §C2b.7.2]], [[§C2b.7 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-7-10|Theorem §C2b.7.10]], [[§C2b.7 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-7-9|Theorem §C2b.7.9]], [[§C2b.6 Green's Functions and Contours#^thm-c2b-6-7|Theorem §C2b.6.7]].
>   - Theorem §CA.2.7 (invariant shell and cone distributions): the invariant measure, $D_W$ as the transform of the positive shell, the massless $\operatorname{sgn}(x^0)\delta(x^2)$ — [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-3|Theorem §C2a.4.3]], [[§C2b.2 The Wightman Function#^thm-c2b-2-1|Theorem §C2b.2.1]], [[§C2b.2 The Wightman Function#^thm-c2b-2-2|Theorem §C2b.2.2]], [[§C2b.2 The Wightman Function#^thm-c2b-2-3|Theorem §C2b.2.3]], [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-6|Theorem §C2b.3.6]], [[§C2b.5 Microcausality and the Commutator Function#^thm-c2b-5-4|Theorem §C2b.5.4]], [[§C2b.5 Microcausality and the Commutator Function#^thm-c2b-5-8|Theorem §C2b.5.8]], [[§C2b.1 Heisenberg Fields#^thm-c2b-1-3|Theorem §C2b.1.3]], [[§C2b.6 Green's Functions and Contours#^thm-c2b-6-6|Theorem §C2b.6.6]], [[§C2b.7 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-7-10|Theorem §C2b.7.10]].
>   - Def. §CA.2.5 (principal value): the principal function, dropping $i\varepsilon$ after a Wick rotation — [[§C2b.6 Green's Functions and Contours#^thm-c2b-6-4|Theorem §C2b.6.4]], [[§C2b.8 Wick Rotation and the Two-Point Family#^rem-c2b-8-2|§C2b.8, Remark: The two-point functions at a glance]].
>   - Theorem §CA.2.3 (integration by parts): the gradient term with fall-off — [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-4|Theorem §C2a.5.4]], [[§C2b.1 Heisenberg Fields#^thm-c2b-1-2|Theorem §C2b.1.2]].
>   - Def. §CA.2.4 (the delta function): [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-1|Theorem §C2a.2.1]], [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-4|Theorem §C2a.4.4]], [[§C2b.1 Heisenberg Fields#^thm-c2b-1-2|Theorem §C2b.1.2]], [[§C2b.1 Heisenberg Fields#^thm-c2b-1-4|Theorem §C2b.1.4]], [[§C2b.1 Heisenberg Fields#^thm-c2b-1-6|Theorem §C2b.1.6]], [[§C2b.2 The Wightman Function#^thm-c2b-2-1|Theorem §C2b.2.1]], [[§C2b.9 Particle Production by a Classical Source#^ex-c2b-9-1|Example §C2b.9.1]].
>   - Example §CA.2.1 (x·δ = 0 and x·𝒫(1/x) = 1): [[§C2b.6 Green's Functions and Contours#^thm-c2b-6-4|Theorem §C2b.6.4]].
> - **Used in**, statement by statement (C1a–C1b items):
>   - Def. §CA.2.1–§CA.2.2 (test functions; distributions): variations and the functional derivative — [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^def-c1b-2-3|Def. §C1b.2.3]], [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^rem-c1b-2-2|§C1b.2, Remark: The functional derivative is a distribution]].
>   - Theorem §CA.2.1 (regular and singular distributions): δ as a functional derivative — [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^rem-c1b-2-2|§C1b.2, Remark: The functional derivative is a distribution]], [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-4|Theorem §C1b.2.4]], [[§C1b.4 Hamiltonian Field Theory#^thm-c1b-4-1|Theorem §C1b.4.1]], [[§C1b.4 Hamiltonian Field Theory#^thm-c1b-4-4|Theorem §C1b.4.4]].
>   - Def. §CA.2.6 (support, singular support): [[§C2b.4 The Single-Particle Amplitude in Closed Form#^thm-c2b-4-3|Theorem §C2b.4.3]], [[§C2b.5 Microcausality and the Commutator Function#^thm-c2b-5-7|Theorem §C2b.5.7]].
>   - Defs. §CA.2.7–§CA.2.10 (operations: derivative, product with a smooth function, limit, transform): [[§C1a.3 Causal Structure and the Causality of a Single Particle#^thm-c1a-3-3|Theorem §C1a.3.3]], [[§C2b.5 Microcausality and the Commutator Function#^thm-c2b-5-7|Theorem §C2b.5.7]], [[§C1a.3 Causal Structure and the Causality of a Single Particle#^thm-c1a-3-5|Theorem §C1a.3.5]].
>   - Theorem §CA.2.5 (distributional limits): [[§C2b.4 The Single-Particle Amplitude in Closed Form#^thm-c2b-4-1|Theorem §C2b.4.1]], [[§C1a.3 Causal Structure and the Causality of a Single Particle|§C1a.3]] (Mathematical background).
>   - Defs. §CA.2.11, §CA.2.12 (changes of variables): invariance of distributions — [[§C2b.5 Microcausality and the Commutator Function#^thm-c2b-5-7|Theorem §C2b.5.7]], [[§C1a.4 The Lorentz Group#^thm-c1a-4-1|Theorem §C1a.4.1]], [[§C1b.1 Fields and Their Transformation Laws#^thm-c1b-1-3|Theorem §C1b.1.3]], [[§C1b.4 Hamiltonian Field Theory#^thm-c1b-4-5|Theorem §C1b.4.5]].
>   - Theorem §CA.2.7 (invariant shell and cone distributions): [[§C1a.4 The Lorentz Group#^thm-c1a-4-1|Theorem §C1a.4.1]], [[§C1b.1 Fields and Their Transformation Laws#^cau-c1b-1-1|§C1b.1, Caution: What "the scalar does not change" does not mean]].
>   - Theorem §CA.2.3 (integration by parts): [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-4|Theorem §C1b.2.4]], [[§C1b.4 Hamiltonian Field Theory#^thm-c1b-4-4|Theorem §C1b.4.4]], [[§C1b.8 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^thm-c1b-8-4|Theorem §C1b.8.4]], [[§C1b.7 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-7-9|Theorem §C1b.7.9]].
>   - Def. §CA.2.3 (tempered distribution): [[§C1a.3 Causal Structure and the Causality of a Single Particle#^thm-c1a-3-3|Theorem §C1a.3.3]].
> - **Used in**, statement by statement (C3 items):
>   - Def. §CA.2.2 (distributions): the equal-time commutators of the Noether charges — [[§C3.3 How Fields Transform under the Lorentz Group#^rem-c3-3-2|§C3.3, Remark: The laws for fields that are distributions]], [[§C3.5 Covariant Quantum Fields and the Free Scalar's Representation|§C3.5]] (Mathematical background).
>   - Defs. §CA.2.7–§CA.2.10 (operations: derivative, product with a smooth function, limit, transform): transformation laws and orbital generators on distributions — [[§C3.3 How Fields Transform under the Lorentz Group#^rem-c3-3-2|§C3.3, Remark: The laws for fields that are distributions]], [[§C3.5 Covariant Quantum Fields and the Free Scalar's Representation#^thm-c3-5-2|Theorem §C3.5.2]].
>   - Defs. §CA.2.11, §CA.2.12 (changes of variables): moving the argument of a field — [[§C3.3 How Fields Transform under the Lorentz Group#^rem-c3-3-2|§C3.3, Remark: The laws for fields that are distributions]], [[§C3.5 Covariant Quantum Fields and the Free Scalar's Representation#^thm-c3-5-5|Theorem §C3.5.5]].
>   - Theorem §CA.2.7 (invariant shell and cone distributions): Lorentz-invariant distributions as fixed points of the scalar law — [[§C3.3 How Fields Transform under the Lorentz Group#^rem-c3-3-2|§C3.3, Remark: The laws for fields that are distributions]].
>   - Def. §CA.2.4 (the delta function): [[§C3.5 Covariant Quantum Fields and the Free Scalar's Representation#^thm-c3-5-6|Theorem §C3.5.6]].
> - **Used in**, statement by statement (C5a–C5b items):
>   - Def. §CA.2.1 (test functions): smeared Dirac fields — [[§C5b.1 Canonical Quantization of the Dirac Field#^def-c5b-1-5|Def. §C5b.1.5]].
>   - Theorem §CA.2.1 (regular and singular distributions): plane-wave solutions and the propagator at finite $\varepsilon$ as tempered distributions — [[§C5a.7 The Dirac Equation and Its Lagrangian#^rem-c5a-7-5|§C5a.7, Remark: In what sense the equations hold]], [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-4|Theorem §C5b.8.4]].
>   - Theorem §CA.2.2 (distributions supported at a point): uniqueness of $S_F$ at the origin — [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-4|Theorem §C5b.8.4]].
>   - Def. §CA.2.6 (support, singular support): microcausality of the Dirac field — [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-3|Theorem §C5b.7.3]], [[§C5b.8 Green's Functions and the Dirac Feynman Propagator|§C5b.8]] (Mathematical background).
>   - Theorem §CA.2.4 (derivatives): Dirac solutions as Klein–Gordon solutions, $\partial_0\theta = \delta$ in the propagator — [[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-8|Theorem §C5a.7.8]], [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-3|Theorem §C5b.8.3]], [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-1|Theorem §C5b.8.1]], [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-5|Theorem §C5b.8.5]].
>   - Defs. §CA.2.7–§CA.2.10 (operations: derivative, product with a smooth function, limit, transform): the Dirac operator on distributions, derivatives of two-point functions, supports — [[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-1|Theorem §C5a.7.1]], [[§C5a.7 The Dirac Equation and Its Lagrangian#^rem-c5a-7-5|§C5a.7, Remark: In what sense the equations hold]], [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-1|Theorem §C5b.7.1]], [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-3|Theorem §C5b.7.3]], [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-4|Theorem §C5b.8.4]], [[§C5b.1 Canonical Quantization of the Dirac Field#^thm-c5b-1-9|Theorem §C5b.1.9]], [[§C5b.8 Green's Functions and the Dirac Feynman Propagator|§C5b.8]] (Mathematical background).
>   - Theorem §CA.2.5 (distributional limits): nascent deltas and the limit $\varepsilon \to 0^+$ — [[§C5b.1 Canonical Quantization of the Dirac Field#^thm-c5b-1-8|Theorem §C5b.1.8]], [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-3|Theorem §C5b.8.3]].
>   - Defs. §CA.2.11, §CA.2.12 (changes of variables): covariance of the Dirac equation in $\mathcal S'$, the smeared anticommutator — [[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-1|Theorem §C5a.7.1]], [[§C5a.7 The Dirac Equation and Its Lagrangian#^rem-c5a-7-5|§C5a.7, Remark: In what sense the equations hold]], [[§C5b.1 Canonical Quantization of the Dirac Field#^thm-c5b-1-8|Theorem §C5b.1.8]], [[§C5b.4 Fermions, Fock Space and the Pauli Principle#^thm-c5b-4-4|★ Theorem §C5b.4.4]].
>   - Theorem §CA.2.7 (invariant shell and cone distributions): solutions as transforms supported on the mass shell — [[§C5a.11 The Spinors u(p), v(p) and Their Dirac Conjugates#^rem-c5a-11-2|§C5a.11, Remark: In what sense a general solution is a superposition of these plane waves]].
>   - Theorem §CA.2.3 (integration by parts): the spin of the quanta at rest — [[§C5b.4 Fermions, Fock Space and the Pauli Principle#^thm-c5b-4-3|Theorem §C5b.4.3]], [[§C5a.9 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-9-7|Theorem §C5a.9.7]], [[§C5b.1 Canonical Quantization of the Dirac Field#^thm-c5b-1-3|Theorem §C5b.1.3]].
>   - Def. §CA.2.2 (generalized function): [[§C5b.1 Canonical Quantization of the Dirac Field|§C5b.1]] (Mathematical background).
>   - Def. §CA.2.4 (the delta function): [[§C5b.1 Canonical Quantization of the Dirac Field#^thm-c5b-1-9|Theorem §C5b.1.9]].
> - **Used in**, statement by statement (C9 items):
>   - Def. §CA.2.7 (derivative): the derivative of the parity-transformed field — [[§C9.4 Fermion Bilinears under Parity#^thm-c9-4-5|Theorem §C9.4.5]], [[§C9.2 Parity of the Scalar Field#^thm-c9-2-5|Theorem §C9.2.5]], [[§C9.4 Fermion Bilinears under Parity#^thm-c9-4-6|★ Theorem §C9.4.6]], [[§C9.12 C, T and CPT for the Complex Scalar Field#^thm-c9-12-3|Theorem §C9.12.3]].
>   - Def. §CA.2.11 (linear change of variables): the smeared parity law, test function $f \to f\circ \mathcal P$ — [[§C9.3 Parity on States, Spinors and the Dirac Field#^thm-c9-3-5|Theorem §C9.3.5]], [[§C9.2 Parity of the Scalar Field#^thm-c9-2-2|Theorem §C9.2.2]].
> - **Used in**, statement by statement (C4 items):
>   - Theorem §CA.2.1 (Regular and Singular Tempered Distributions): [[§C4.11 Vector-Field Propagators#^thm-c4-11-7|Theorem §C4.11.7]].
>   - Def. §CA.2.6 (Support and Singular Support): [[§C4.11 Vector-Field Propagators#^thm-c4-11-2|Theorem §C4.11.2]], [[§C4.11 Vector-Field Propagators|§C4.11]].
>   - Theorem §CA.2.4 (Every Generalized Function Is Differentiable): [[§C4.2★ The Proca Field#^thm-c4-2-4|Theorem §C4.2.4]], [[§C4.11 Vector-Field Propagators#^thm-c4-11-3|Theorem §C4.11.3]], [[§C4.11 Vector-Field Propagators|§C4.11]].
>   - Defs. §CA.2.7–§CA.2.10 (operations: derivative, product with a smooth function, limit, transform): [[§C4.4★ Quantizing the Proca Field꞉ Modes and the Mode Algebra#^thm-c4-4-3|Theorem §C4.4.3]], [[§C4.6 The Maxwell Field, Gauge Symmetry and Gauge Fixing#^thm-c4-6-3|Theorem §C4.6.3]], [[§C4.8 Covariant Quantization꞉ Modes and the Indefinite Mode Algebra#^thm-c4-8-6|Theorem §C4.8.6]], [[§C4.10 The Gupta–Bleuler Condition and Physical Photons#^thm-c4-10-3|Theorem §C4.10.3]], [[§C4.11 Vector-Field Propagators#^thm-c4-11-1|Theorem §C4.11.1]], [[§C4.11 Vector-Field Propagators#^thm-c4-11-2|Theorem §C4.11.2]], [[§C4.11 Vector-Field Propagators|§C4.11]], [[§C4.4★ Quantizing the Proca Field꞉ Modes and the Mode Algebra#^thm-c4-4-4|Theorem §C4.4.4]], [[§C4.8 Covariant Quantization꞉ Modes and the Indefinite Mode Algebra#^thm-c4-8-8|Theorem §C4.8.8]], [[§C4.2★ The Proca Field#^thm-c4-2-13|Theorem §C4.2.13]].
>   - Theorem §CA.2.7 (Invariant Distributions on the Mass Shell and the Light Cone): [[§C4.8 Covariant Quantization꞉ Modes and the Indefinite Mode Algebra#^thm-c4-8-9|Theorem §C4.8.9]], [[§C4.11 Vector-Field Propagators#^thm-c4-11-7|Theorem §C4.11.7]], [[§C4.11 Vector-Field Propagators|§C4.11]].
>   - Theorem §CA.2.3 (Integration by Parts; the Gradient of a Delta Function): [[§C4.2★ The Proca Field#^thm-c4-2-9|Theorem §C4.2.9]], [[§C4.2★ The Proca Field|§C4.2★]], [[§C4.4★ Quantizing the Proca Field꞉ Modes and the Mode Algebra#^thm-c4-4-3|Theorem §C4.4.3]], [[§C4.4★ Quantizing the Proca Field꞉ Modes and the Mode Algebra#^thm-c4-4-6|Theorem §C4.4.6]], [[§C4.6 The Maxwell Field, Gauge Symmetry and Gauge Fixing#^thm-c4-6-5|Theorem §C4.6.5]], [[§C4.8 Covariant Quantization꞉ Modes and the Indefinite Mode Algebra#^thm-c4-8-6|Theorem §C4.8.6]], [[§C4.4★ Quantizing the Proca Field꞉ Modes and the Mode Algebra#^thm-c4-4-4|Theorem §C4.4.4]], [[§C4.8 Covariant Quantization꞉ Modes and the Indefinite Mode Algebra#^thm-c4-8-8|Theorem §C4.8.8]], [[§C4.2★ The Proca Field#^thm-c4-2-13|Theorem §C4.2.13]], [[§C4.7 The Feynman-Gauge Field꞉ Canonical Structure and Angular Momentum#^thm-c4-7-5|Theorem §C4.7.5]], [[§C4.7 The Feynman-Gauge Field꞉ Canonical Structure and Angular Momentum#^thm-c4-7-6|Theorem §C4.7.6]], [[§C4.7 The Feynman-Gauge Field꞉ Canonical Structure and Angular Momentum#^thm-c4-7-7|Theorem §C4.7.7]].
> - **Used in**, statement by statement (Electromagnetism C items):
>   - Def. §CA.2.1 (test functions): variations of compact support, the polarization charge, a comb of line charges — [[§C2.1 The Static Limit and the Field of a Charge Distribution#^thm-c2-1-2|EM Theorem §C2.1.2]], [[§C5.1 Polarization Charge and the Polarization#^thm-c5-1-2|EM Theorem §C5.1.2]], [[§C6.2 Separation in Cartesian and Spherical Coordinates#^ex-c6-2-2|EM Example §C6.2.2]], [[§C3.1 Cartesian Multipole Moments and Dipole Layers#^mod-c3-1-2|EM Model §C3.1.2]].
>   - Def. §CA.2.2 (distributions): point charges, point dipoles, surface charge and polarization charge as distributions — [[§C4.1 Induced Charge, Screening and Thomson's Theorem#^rem-c4-1-1|EM Remark: What changes from levels A and B]], [[§C5.1 Polarization Charge and the Polarization#^thm-c5-1-2|EM Theorem §C5.1.2]], [[§C6.1 Potential Theory and Uniqueness#^rem-c6-1-1|EM Remark: What changes from level B]].
>   - Theorem §CA.2.1 (regular and singular distributions): the current of a point charge, the Coulomb field and the fields of surface layers as distributions — [[§C1.1 Building the Maxwell Action#^thm-c1-1-6|EM Theorem §C1.1.6]], [[§C2.1 The Static Limit and the Field of a Charge Distribution#^rem-c2-1-1|EM Remark: The Coulomb potential as a fundamental solution]], [[§C2.3 Electrostatic Energy and Self-Energy#^thm-c2-3-7|EM Theorem §C2.3.7]], [[§C4.1 Induced Charge, Screening and Thomson's Theorem#^rem-c4-1-1|EM Remark: What changes from levels A and B]], [[§C4.1 Induced Charge, Screening and Thomson's Theorem#^thm-c4-1-6|EM Theorem §C4.1.6]], [[§C5.2 The Field of Polarized Matter#^thm-c5-2-1|EM Theorem §C5.2.1]], [[§C5.2 The Field of Polarized Matter#^ex-c5-2-3|EM Example §C5.2.3]].
>   - Theorem §CA.2.2 (distributions supported at a point): the charge density as a series of point multipoles — [[§C3.1 Cartesian Multipole Moments and Dipole Layers#^thm-c3-1-6|EM Theorem §C3.1.6]].
>   - Theorem §CA.2.4 (every distribution is differentiable; $\theta' = \delta$): the Bianchi identity for distributional potentials, jumps at dipole layers and surfaces, the jump condition of a Green function — [[§C1.2 The Field Equations and the Bianchi Identity#^thm-c1-2-4|EM Theorem §C1.2.4]], [[§C3.1 Cartesian Multipole Moments and Dipole Layers#^thm-c3-1-10|EM Theorem §C3.1.10]], [[§C3.2 Spherical Multipole Expansions#^ex-c3-2-3|EM Example §C3.2.3]], [[§C5.1 Polarization Charge and the Polarization#^thm-c5-1-2|EM Theorem §C5.1.2]], [[§C7.4 Constructing Green Functions#^thm-c7-4-2|EM Theorem §C7.4.2]], [[§C7.5★ Logarithmic Potentials and the Poisson–Boltzmann Equation#^thm-c7-5-4|EM Theorem §C7.5.4]].
>   - Defs. §CA.2.7–§CA.2.10 (operations: derivative, product with a smooth function, limit, transform): field equations in weak form, Poisson's equation as an identity of distributions, multipole and polarization densities — [[§C1.2 The Field Equations and the Bianchi Identity#^thm-c1-2-2|EM Theorem §C1.2.2]], [[§C1.3 Gauge Symmetry and Charge Conservation#^thm-c1-3-1|EM Theorem §C1.3.1]], [[§C1.3 Gauge Symmetry and Charge Conservation#^ex-c1-3-1|EM Example §C1.3.1]], [[§C2.1 The Static Limit and the Field of a Charge Distribution#^thm-c2-1-2|EM Theorem §C2.1.2]], [[§C2.2 Gauss's Law and the Solid Angle#^thm-c2-2-4|EM Theorem §C2.2.4]], [[§C3.1 Cartesian Multipole Moments and Dipole Layers#^mod-c3-1-2|EM Model §C3.1.2]], [[§C3.1 Cartesian Multipole Moments and Dipole Layers#^thm-c3-1-3|EM Theorem §C3.1.3]], [[§C3.1 Cartesian Multipole Moments and Dipole Layers#^mod-c3-1-5|EM Model §C3.1.5]], [[§C3.1 Cartesian Multipole Moments and Dipole Layers#^thm-c3-1-6|EM Theorem §C3.1.6]], [[§C3.1 Cartesian Multipole Moments and Dipole Layers#^thm-c3-1-9|EM Theorem §C3.1.9]], [[§C4.3 The Capacitance Matrix#^thm-c4-3-3|EM Theorem §C4.3.3]], [[§C5.1 Polarization Charge and the Polarization#^thm-c5-1-2|EM Theorem §C5.1.2]], [[§C6.1 Potential Theory and Uniqueness#^thm-c6-1-2|EM Theorem §C6.1.2]], [[§C7.1 The Method of Images#^thm-c7-1-1|EM Theorem §C7.1.1]], [[§C7.3 Green Functions for Poisson’s Equation#^def-c7-3-1|EM Def. §C7.3.1]].
>   - Theorem §CA.2.5 (distributional limits): the point dipole as a limit, closure relations, the Poisson kernel as a nascent delta — [[§C3.1 Cartesian Multipole Moments and Dipole Layers#^mod-c3-1-2|EM Model §C3.1.2]], [[§C6.2 Separation in Cartesian and Spherical Coordinates#^thm-c6-2-1|EM Theorem §C6.2.1]], [[§C6.2 Separation in Cartesian and Spherical Coordinates#^thm-c6-2-3|EM Theorem §C6.2.3]], [[§C7.3 Green Functions for Poisson’s Equation#^thm-c7-3-5|EM Theorem §C7.3.5]], [[§C7.4 Constructing Green Functions#^thm-c7-4-1|EM Theorem §C7.4.1]].
>   - Defs. §CA.2.11, §CA.2.12 and Theorem §CA.2.6 (changes of variables, composition): the field of a point dipole, the current of a point charge, line sources — [[§C3.1 Cartesian Multipole Moments and Dipole Layers#^thm-c3-1-4|EM Theorem §C3.1.4]], [[§C1.1 Building the Maxwell Action#^thm-c1-1-6|EM Theorem §C1.1.6]], [[§C7.5★ Logarithmic Potentials and the Poisson–Boltzmann Equation#^thm-c7-5-1|EM Theorem §C7.5.1]].
>   - Theorem §CA.2.3 (integration by parts): the Coulomb force from the potential energy, the second derivatives of $1/r$, the dipole layer — [[§C2.3 Electrostatic Energy and Self-Energy#^thm-c2-3-1|EM Theorem §C2.3.1]], [[§C3.1 Cartesian Multipole Moments and Dipole Layers#^thm-c3-1-3|EM Theorem §C3.1.3]], [[§C3.1 Cartesian Multipole Moments and Dipole Layers#^thm-c3-1-9|EM Theorem §C3.1.9]].
>   - Def. §CA.2.4 (the delta function): [[§C1.1 Building the Maxwell Action#^thm-c1-1-6|EM Theorem §C1.1.6]], [[§C3.1 Cartesian Multipole Moments and Dipole Layers#^mod-c3-1-2|EM Model §C3.1.2]], [[§C7.1 The Method of Images#^thm-c7-1-1|EM Theorem §C7.1.1]].
> - **Used in** (C6b places, Lecture 15): Theorems §CA.2.2–§CA.2.3 — the $S$-matrix conserves four-momentum, only $\delta^4$ itself survives ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-4|Theorem §C6b.1.4]]); Theorem §CA.2.6 — the longitudinal Jacobian $1/\lvert\mathbf v_A - \mathbf v_B\rvert$, the invariance of $\delta^4$, two-body phase space ([[§C6b.9 Evaluating the Cross Section#^thm-c6b-9-1|Theorem §C6b.9.1]], [[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-6|Theorem §C6b.1.6]], [[§C6b.3 The Cross Section#^thm-c6b-3-8|Theorem §C6b.3.8]], [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-1|Theorem §C6b.4.1]]), [[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-4|Theorem §C6b.1.4]], [[§C6b.3 The Cross Section#^thm-c6b-3-5|Theorem §C6b.3.5]], [[§C6b.6 Decay Kinematics#^ex-c6b-6-1|Example §C6b.6.1]], [[§C6b.6 Decay Kinematics#^thm-c6b-6-5|★ Theorem §C6b.6.5]], [[§C6b.9 Evaluating the Cross Section#^cau-c6b-9-2|§C6b.9, Caution: 1/f′(0) on slide 14]]; Theorem §CA.2.5 — the Breit–Wigner shape as a nascent delta function ([[§C6b.7 The Width in the Propagator#^thm-c6b-7-4|Theorem §C6b.7.4]]); Def. §CA.2.1 — [[§C6b.1 The S-Matrix and the Invariant Amplitude#^cau-c6b-1-3|§C6b.1, Caution: Names for the S-matrix, the T-matrix and the amplitude]]; Def. §CA.2.7 — [[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-4|Theorem §C6b.1.4]]; Def. §CA.2.8 — [[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-4|Theorem §C6b.1.4]].
> - **Used in** (C6c places): Theorem §CA.2.6 — [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-2|Theorem §C6c.4.2]], [[§C6c.7 Particle Production by a Classical Source꞉ the Diagrammatic Route#^thm-c6c-7-2|Theorem §C6c.7.2]].
