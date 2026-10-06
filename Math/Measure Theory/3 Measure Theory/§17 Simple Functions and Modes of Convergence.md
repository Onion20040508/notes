---
type: section
subject: "[[Measure Theory]]"
chapter: 3
section: 17
tags: [measure-theory, math551]
---
← [[§16 Limits and Positive Parts of Measurable Functions]] · ↑ [[· 3 Measure Theory]] · [[§18 Egorov's and Lusin's Theorems]] →

Every non-negative measurable function can be approximated from below by simple functions. This section introduces simple functions, proves the approximation theorems, and compares pointwise, almost everywhere and uniform convergence.

## Simple Functions

> [!definition] Definition §25.1: Simple Function
> A function $f: E \to \mathbb{R}$ is called **simple** if its range $R(f) = \{y \mid y = f(x) \text{ for some } x \in E\}$ has only finitely many elements.

^def-17-1

> [!theorem] Proposition §25.1: Canonical Representation of Simple Functions
> Let $f: E \to \mathbb{R}$ be a simple function with $R(f) = \{a_1, a_2, \ldots, a_n\} \subseteq \mathbb{R}$, where $a_i \neq a_j$ for $i \neq j$. Define
>
> $$
> E_j = \{x \in E \mid f(x) = a_j\}, \quad j = 1, \ldots, n.
> $$
>
> Then $E_i \cap E_j = \emptyset$ for $i \neq j$, $\bigcup_{j=1}^n E_j = E$, and
>
> $$
> f(x) = \sum_{j=1}^{n} a_j \chi_{E_j}(x).
> $$
>
> If $f$ is measurable, then each $E_j \in \mathcal{M}$.

^prop-17-1

> [!remark]- Connections
> - The canonical representation is the one used to define the integral of a simple function: [[§20 The Lebesgue Integral for Simple Functions#^def-20-1|Def. §20.1]].
> - Measurability of each $E_j$ is condition (5) of [[§15 Measurable Functions#^prop-15-2|Proposition §15.2]].

> [!definition] Definition §25.2: Support of a Function
> Let $f: E \to \overline{\mathbb{R}}$ be an extended real-valued function. The **support** of $f$ is
>
> $$
> \operatorname{supp} f = \overline{\{x \in E \mid f(x) \neq 0\}}.
> $$
>
> We say $f$ is **compactly supported** if $\operatorname{supp} f$ is compact (bounded and closed in $\mathbb{R}^n$, by [[§6 Open Covers and the Heine–Borel Theorem#^thm-6-4|Heine–Borel]]). Equivalently, $f(x) = 0$ outside some bounded closed set.

^def-17-2

> [!remark]- Connections
> - General-topology form of “compact = bounded and closed”: [[Heine–Borel Theorem]].
> - Compactly supported continuous functions are dense in $L^1$: [[Continuous Functions of Compact Support are Dense in L¹|Theorem §24.7]].

## Approximation by Simple Functions

The following theorem shows that every non-negative measurable function can be approximated from below by simple functions.

> [!theorem] Theorem §25.2: Approximation by Simple Functions: Non-negative Case
> Let $f: E \to \mathbb{R} \cup \{+\infty\}$ be a non-negative measurable function. Then there exists an **increasing** sequence of measurable simple functions $\{\varphi_k\}_{k \geq 1}$ such that:
> 1. $0 \leq \varphi_1(x) \leq \varphi_2(x) \leq \cdots \leq \varphi_k(x) \leq \cdots$ for all $x \in E$.
> 2. $\displaystyle\lim_{k \to \infty} \varphi_k(x) = f(x)$ for all $x \in E$.

^thm-17-2

> [!proof]+ Proof
> For each $k \in \mathbb{N}$, we partition the range $[0, k)$ into $k \cdot 2^{k-1}$ intervals of length $\frac{1}{2^{k-1}}$:
>
> $$
> \left[0, \frac{1}{2^{k-1}}\right), \left[\frac{1}{2^{k-1}}, \frac{2}{2^{k-1}}\right), \ldots, \left[\frac{k \cdot 2^{k-1} - 1}{2^{k-1}}, k\right).
> $$
>
> Define the level sets:
>
> $$
> \begin{aligned}
> E_{kj} &= \left\{x \in E \;\middle|\; \frac{j-1}{2^{k-1}} \leq f(x) < \frac{j}{2^{k-1}}\right\}, \quad j = 1, 2, \ldots, k \cdot 2^{k-1}, \\
> E_k &= \{x \in E \mid f(x) \geq k\}.
> \end{aligned}
> $$
>
> Since $f$ is measurable, each $E_{kj}$ and $E_k$ is [[§15 Measurable Functions#^prop-15-2|measurable]]. Define:
>
> $$
> \varphi_k(x) = \sum_{j=1}^{k \cdot 2^{k-1}} \frac{j-1}{2^{k-1}} \chi_{E_{kj}}(x) + k \cdot \chi_{E_k}(x).
> $$
>
> **Claim 1: $\varphi_k$ is simple and measurable.**
>
> This is clear since $\varphi_k$ is a [[§15 Measurable Functions#^thm-15-3|finite linear combination]] of [[§15 Measurable Functions#^prop-15-1|characteristic functions of measurable sets]].
>
> **Claim 2: $\varphi_k(x) \leq \varphi_{k+1}(x)$ for all $x \in E$.**
>
> When we pass from $k$ to $k+1$, each interval $\left[\frac{j-1}{2^{k-1}}, \frac{j}{2^{k-1}}\right)$ is subdivided into two intervals of half the length:
>
> $$
> E_{kj} = E_{k+1, 2j-1} \cup E_{k+1, 2j},
> $$
>
> where
>
> $$
> E_{k+1, 2j-1} = \left\{x \in E \;\middle|\; \frac{2j-2}{2^k} \leq f(x) < \frac{2j-1}{2^k}\right\}, \quad E_{k+1, 2j} = \left\{x \in E \;\middle|\; \frac{2j-1}{2^k} \leq f(x) < \frac{2j}{2^k}\right\}.
> $$
>
> On $E_{k+1, 2j-1}$: $\varphi_{k+1}(x) = \frac{2j-2}{2^k} = \frac{j-1}{2^{k-1}} = \varphi_k(x)$.
>
> On $E_{k+1, 2j}$: $\varphi_{k+1}(x) = \frac{2j-1}{2^k} > \frac{2j-2}{2^k} = \frac{j-1}{2^{k-1}} = \varphi_k(x)$.
>
> Similarly, $E_k \supseteq E_{k+1}$, and $\varphi_{k+1}(x) \geq \varphi_k(x)$ on $E_k \setminus E_{k+1}$.
>
> **Claim 3: $\varphi_k(x) \to f(x)$ as $k \to \infty$.**
>
> *Case 1: $0 \leq f(x_0) < \infty$.* For $k > f(x_0)$, we have $x_0 \in E_{kj}$ for some $j$, so
>
> $$
> 0 \leq f(x_0) - \varphi_k(x_0) < \frac{1}{2^{k-1}} \to 0 \text{ as } k \to \infty.
> $$
>
> *Case 2: $f(x_0) = +\infty$.* Then $x_0 \in E_k$ for all $k$, so $\varphi_k(x_0) = k \to \infty = f(x_0)$.

^pf-17-2

*Uses:* [[§15 Measurable Functions#^prop-15-2|§15.2]], [[§15 Measurable Functions#^def-15-3|Def. §15.3]], [[§15 Measurable Functions#^prop-15-1|§15.1]], [[§15 Measurable Functions#^thm-15-3|§15.3]], [[§17 Simple Functions and Modes of Convergence#^def-17-1|Def. §17.1]]

![[m551-12-3.svg]]
*The staircase of [[§17 Simple Functions and Modes of Convergence#^thm-17-2|Theorem §17.2]]. $\varphi_2$ (orange, shaded) rounds $f$ (blue) down to the grid of step $\tfrac12$ (gray lines) and is capped at $2$ on $E_2 = \{f \geq 2\}$; $\varphi_3$ (red) uses step $\tfrac14$ and cap $3$. Each step sits over a level set $E_{kj}$, so it is the range that gets partitioned. Halving the step can only raise a value, so $\varphi_2 \leq \varphi_3 \leq f$, and $f - \varphi_k < 2^{-(k-1)}$ wherever $f < k$.*

> [!remark]- Connections
> - Partitions the *range* of $f$, where Darboux sums partition the *domain*: [[§8 Motivation꞉ The Riemann Integral#^def-8-2|Def. §8.2]], [[§32 The Definition of the Riemann Integral|451 §32]].
> - With the [[Monotone Convergence Theorem (Lebesgue)|Monotone Convergence Theorem]] this gives $\int \varphi_k \to \int f$, used for [[§21 Consequences of the Monotone Convergence Theorem#^thm-21-1|linearity of the integral]].

> [!theorem] Theorem §25.3: Approximation by Simple Functions: General Case
> Let $f: E \to \overline{\mathbb{R}}$ be a measurable function. Then there exists a sequence of measurable simple functions $\{\psi_k\}_{k \geq 1}$ such that:
> 1. $|\psi_k(x)| \leq |f(x)|$ for all $x \in E$ and all $k$.
> 2. $\displaystyle\lim_{k \to \infty} \psi_k(x) = f(x)$ for all $x \in E$.

^thm-17-3

> [!proof]+ Proof
> Write $f = f^+ - f^-$, where $f^+, f^- \geq 0$ are [[§16 Limits and Positive Parts of Measurable Functions#^prop-16-6|measurable]].
>
> By [[Simple Function Approximation Theorem|the previous theorem]], there exist increasing sequences of non-negative simple functions $\{\varphi_k^{(1)}\}$ and $\{\varphi_k^{(2)}\}$ with
>
> $$
> \varphi_k^{(1)}(x) \to f^+(x), \qquad \varphi_k^{(2)}(x) \to f^-(x) \quad \text{for all } x \in E.
> $$
>
> Define $\psi_k(x) = \varphi_k^{(1)}(x) - \varphi_k^{(2)}(x)$. Then:
> - $\psi_k$ is simple ([[§17 Simple Functions and Modes of Convergence#^rem-17-6|the difference of two simple functions is simple]]).
> - $\psi_k(x) \to f^+(x) - f^-(x) = f(x)$ for all $x \in E$.
> - $|\psi_k(x)| \leq \varphi_k^{(1)}(x) + \varphi_k^{(2)}(x) \leq f^+(x) + f^-(x) = |f(x)|$.

^pf-17-3

*Uses:* [[§16 Limits and Positive Parts of Measurable Functions#^prop-16-6|§16.6]], [[Simple Function Approximation Theorem|§17.2]], [[§16 Limits and Positive Parts of Measurable Functions#^prop-16-5|§16.5]], [[§17 Simple Functions and Modes of Convergence#^rem-17-6|Rem. §12.6]]

> [!remark] Remark
> The difference of two simple functions is simple: if $\varphi = \sum a_i \chi_{A_i}$ and $\psi = \sum b_j \chi_{B_j}$, then $\varphi - \psi$ takes only finitely many values (at most $|\{a_i\}| \cdot |\{b_j\}|$ distinct values).

^rem-17-6

> [!remark]- Connections
> - Used for density of simple functions: [[§24 The L¹ Space and Density Theorems#^thm-24-5|in L¹ (Theorem §24.5)]] and [[§35 Lᵖ as a Banach Space#^thm-35-12|in Lᵖ (Theorem §35.12)]].

## Modes of Convergence

> [!definition] Definition §26.1: Pointwise Convergence
> Let $\{f_k\}_{k \in \mathbb{N}}$ be a sequence of functions on $E$.
> - We say $f_k \to f$ **pointwise** on $E$ if $\displaystyle\lim_{k \to \infty} f_k(x) = f(x)$ for all $x \in E$.

^def-17-3

> [!remark]- Connections
> - MATH 451 version of pointwise convergence: [[§24 Uniform Convergence#^def-24-1|451 Definition §24.1]].

> [!definition] Definition §26.2: Almost Everywhere Convergence
> Let $\{f_k\}_{k \in \mathbb{N}}$ be a sequence of functions on $E$.
> - We say $f_k \to f$ **almost everywhere** (a.e.) on $E$ if there exists a measure zero set $Z \subseteq E$ such that $\displaystyle\lim_{k \to \infty} f_k(x) = f(x)$ for all $x \in E \setminus Z$.
>
> We write $f_k \to f$ a.e. on $E$, or $f_k(x) \to f(x)$ for a.e. $x \in E$.

^def-17-4

> [!definition] Definition §17.5: Uniform Convergence
> We say $\{f_k\}$ converges **uniformly** to $f$ on $E$ if: for all $\epsilon > 0$, there exists $\ell \in \mathbb{N}$ such that for all $k \geq \ell$,
>
> $$
> \sup_{x \in E} |f_k(x) - f(x)| \leq \epsilon.
> $$

^def-17-5

> [!remark]- Connections
> - MATH 451: [[§24 Uniform Convergence#^def-24-2|451 Definition §24.2]]; the sup form used here is [[§24 Uniform Convergence#^thm-24-1|451 Theorem §24.1: Supremum Criterion]].

> [!example] Example §17.1: Pointwise but Not Uniform Convergence
> Let $f_k(x) = x^k$ for $x \in [0, 1]$. Then:
>
> $$
> f_k(x) \to f(x) = \begin{cases} 0 & \text{if } 0 \leq x < 1 \\ 1 & \text{if } x = 1 \end{cases}
> $$
>
> pointwise on $[0, 1]$.
>
> However, the convergence is **not uniform**. For $0 \leq x < 1$ and $\epsilon > 0$, we need $x^k < \epsilon$, i.e., $k \ln x < \ln \epsilon$, i.e., $k > \frac{\ln \epsilon}{\ln x}$. As $x \to 1^-$, $\ln x \to 0^-$, so $\frac{\ln \epsilon}{\ln x} \to +\infty$. No single $\ell$ works for all $x \in [0, 1)$.

^ex-17-1

> [!remark]- Connections
> - The same example in MATH 451: [[§24 Uniform Convergence#^ex-24-2|451 Example §24.2]].
> - Uniform after removing a small set near $1$: [[§18 Egorov's and Lusin's Theorems#^ex-18-1|Example §18.1]] ([[Egorov's Theorem|Egorov]]).

> [!theorem] Theorem §25.4: Uniform Limit of Continuous Functions
> Let $\{f_k\}_{k \in \mathbb{N}}$ be a sequence of continuous functions on $E$. If $f_k \to f$ uniformly on $E$, then $f$ is continuous on $E$.

^thm-17-4

> [!proof]+ Proof
> This is a [[§24 Uniform Convergence#^thm-24-2|standard result from MATH 451]] (Real Analysis). The key is that uniform convergence allows interchanging limits:
>
> $$
> \lim_{y \to x} f(y) = \lim_{y \to x} \lim_{k \to \infty} f_k(y) = \lim_{k \to \infty} \lim_{y \to x} f_k(y) = \lim_{k \to \infty} f_k(x) = f(x).
> $$

^pf-17-4

*Uses:* [[§24 Uniform Convergence#^thm-24-2|451 §24.2]]

> [!remark]- Connections
> - Used in Step 2 of [[Lusin's Theorem|Lusin's Theorem]].

> [!remark] Remark: A.e. Convergence Preserves Measurability
> If $\{f_k\}$ is a sequence of measurable functions on $E$ and $f_k \to f$ a.e. on $E$, then $f$ is measurable. (This follows from the fact that [[§16 Limits and Positive Parts of Measurable Functions#^cor-16-3|pointwise limits of measurable functions are measurable]], combined with the proposition that [[§16 Limits and Positive Parts of Measurable Functions#^prop-16-7|functions equal a.e. to measurable functions are measurable]].)

^rem-17-7

## Uniform Approximation of Bounded Measurable Functions

> [!theorem] Theorem §25.5: Uniform Approximation for Bounded Functions
> Let $f: E \to \mathbb{R}$ be a **bounded** measurable function. Then there exists a sequence of simple measurable functions $\{\psi_k\}$ such that:
> 1. $|\psi_k(x)| \leq |f(x)|$ for all $x \in E$ and all $k$.
> 2. $\psi_k \to f$ **uniformly** on $E$.

^thm-17-5

> [!proof]+ Proof
> Suppose $|f(x)| \leq M$ for all $x \in E$. Then $0 \leq f^+(x) \leq M$ and $0 \leq f^-(x) \leq M$.
>
> Let $\{\varphi_k^{(1)}\}$ and $\{\varphi_k^{(2)}\}$ be the approximating sequences for $f^+$ and $f^-$ from the [[Simple Function Approximation Theorem|approximation theorem]]. For $k > M$, every $x \in E$ satisfies $f^+(x) < k$, so $x \notin E_k$ (the set where $f^+ \geq k$). Thus:
>
> $$
> 0 \leq f^+(x) - \varphi_k^{(1)}(x) \leq \frac{1}{2^{k-1}} \quad \text{for all } x \in E.
> $$
>
> Similarly, $0 \leq f^-(x) - \varphi_k^{(2)}(x) \leq \frac{1}{2^{k-1}}$ for all $x \in E$.
>
> Let $\psi_k = \varphi_k^{(1)} - \varphi_k^{(2)}$. Then:
>
> $$
> \begin{aligned}
> |f(x) - \psi_k(x)| &= |f^+(x) - \varphi_k^{(1)}(x) - (f^-(x) - \varphi_k^{(2)}(x))| \\
> &\leq (f^+(x) - \varphi_k^{(1)}(x)) + (f^-(x) - \varphi_k^{(2)}(x)) \\
> &\leq \frac{1}{2^{k-1}} + \frac{1}{2^{k-1}} = \frac{2}{2^{k-1}} = \frac{1}{2^{k-2}}.
> \end{aligned}
> $$
>
> This bound is independent of $x$, so $\sup_{x \in E} |f(x) - \psi_k(x)| \leq \frac{1}{2^{k-2}} \to 0$ as $k \to \infty$.

^pf-17-5

*Uses:* [[Simple Function Approximation Theorem|§17.2]], [[§17 Simple Functions and Modes of Convergence#^thm-17-3|§17.3]], [[§16 Limits and Positive Parts of Measurable Functions#^prop-16-5|§16.5]], [[§16 Limits and Positive Parts of Measurable Functions#^prop-16-6|§16.6]], [[§17 Simple Functions and Modes of Convergence#^def-17-5|Def. §17.5]], [[§24 Uniform Convergence#^thm-24-1|451 §24.1]]

> [!remark]- Connections
> - Used in Step 2 of [[Lusin's Theorem|Lusin's Theorem]].

## Set-Theoretic Characterization of Convergence

The following characterization translates the $\epsilon$-$N$ definition of convergence into set-theoretic language, which is essential for proving measurability of limits and for [[Egorov's Theorem|Egorov's theorem]].

> [!theorem] Proposition §25.6: Convergence as Set Membership
> Let $f, f_1, f_2, \ldots$ be functions on $E$ with $f$ finite-valued. Then $f_k(x_0) \to f(x_0)$ as $k \to \infty$ if and only if
>
> $$
> x_0 \in \bigcap_{j=1}^{\infty} \bigcup_{\ell=1}^{\infty} \bigcap_{k=\ell}^{\infty} \left\{ x \in E : |f_k(x) - f(x)| < \frac{1}{j} \right\}.
> $$

^prop-17-6

> [!proof]+ Proof
> The statement $f_k(x_0) \to f(x_0)$ [[§7 Limits of Sequences#^def-7-2|means]]: for all $\epsilon > 0$, there exists $\ell \in \mathbb{N}$ such that for all $k \geq \ell$, $|f_k(x_0) - f(x_0)| < \epsilon$.
>
> Taking $\epsilon = \frac{1}{j}$ for $j \in \mathbb{N}$ [[Archimedean Property|captures all]] $\epsilon > 0$. Thus:
>
> $$
> \begin{aligned}
> f_k(x_0) \to f(x_0) &\Longleftrightarrow \forall j \in \mathbb{N}, \, \exists \ell \in \mathbb{N}, \, \forall k \geq \ell: \, |f_k(x_0) - f(x_0)| < \frac{1}{j} \\
> &\Longleftrightarrow x_0 \in \bigcap_{j=1}^{\infty} \bigcup_{\ell=1}^{\infty} \bigcap_{k=\ell}^{\infty} \left\{ x \in E : |f_k(x) - f(x)| < \frac{1}{j} \right\}.
> \end{aligned}
> $$

^pf-17-6

*Uses:* [[§7 Limits of Sequences#^def-7-2|451 Def. §7.2]], [[Archimedean Property|451 Archimedean Property]]

> [!definition] Definition §17.6: Set of Convergence
> Define the **set of convergence**:
>
> $$
> C = \bigcap_{j=1}^{\infty} \bigcup_{\ell=1}^{\infty} \bigcap_{k=\ell}^{\infty} \left\{ x \in E : |f_k(x) - f(x)| < \frac{1}{j} \right\}.
> $$

^def-17-6

> [!definition] Definition §17.7: Set of Divergence
> The **set of divergence** is $E \setminus C$. By De Morgan's laws:
>
> $$
> E \setminus C = \bigcup_{j=1}^{\infty} \bigcap_{\ell=1}^{\infty} \bigcup_{k=\ell}^{\infty} \left\{ x \in E : |f_k(x) - f(x)| \geq \frac{1}{j} \right\}.
> $$
>
> The statement “$f_k \to f$ [[§17 Simple Functions and Modes of Convergence#^def-17-4|a.e.]] on $E$” is equivalent to $m(E \setminus C) = 0$.

^def-17-7

> [!remark]- Connections
> - The inner unions $\bigcup_{k \geq \ell}\{|f_k - f| \geq 1/j\}$ are exactly the sets $E_\ell^{(j)}$ in the proof of [[Egorov's Theorem|Egorov's Theorem]].
