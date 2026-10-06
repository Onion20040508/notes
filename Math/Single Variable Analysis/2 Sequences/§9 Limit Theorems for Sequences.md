---
type: section
subject: "[[Single Variable Analysis]]"
section: 9
chapter: 2
tags: [real-analysis, math451]
---
← [[§8 A Discussion About Proofs]] · ↑ [[· 2 Sequences]] · [[§9a Divergence to ±∞ and the Ratio Test]] →

We want to simplify life — not using $(\varepsilon, N)$ every time. The theorems of this section let us compute limits by combining known ones.

## Convergent Implies Bounded

> [!theorem] Theorem §9.1: Convergent Sequences Are Bounded
> If a sequence $(s_n)_{n=1}^{\infty}$ is convergent, then it is **bounded**: there exists a number $M$ such that $|s_n| \leq M$ for all $n \geq 1$, i.e. the set $\{|s_n| \mid n \in \mathbb{N}\}$ is bounded.

^thm-9-1

> [!proof]+ Proof
> Let $s = \lim_{n\to\infty} s_n$. Take $\varepsilon = 1$ in the definition: there exists $N$ such that $|s_n - s| < 1$ for all $n \geq N$. By the [[§3 The Set ℝ of Real Numbers#^thm-3-3|triangle inequality]], for such $n$,
>
> $$
> |s_n| = |(s_n - s) + s| \leq |s_n - s| + |s| < |s| + 1.
> $$
>
> **Can we take $M = |s| + 1$? No** — don't forget the finitely many initial terms $s_1, \ldots, s_N$, which the bound above says nothing about. So take
>
> $$
> M = \max\{|s_1|, \ldots, |s_N|,\ |s| + 1\},
> $$
>
> a maximum of a *finite* set (which exists, §4). Now $|s_n| \leq M$ for all $n \geq 1$.

^pf-9-1

*Uses:* [[§7 Limits of Sequences#^def-7-2|Def. §7.2]], [[§3 The Set ℝ of Real Numbers#^thm-3-3|§3.3]], [[§4 The Completeness Axiom#^ex-4-1|Ex. §4.1]]

![[m451-9-1.svg]]
*Convergent implies bounded: from $N$ on (with $\varepsilon = 1$) the terms stay in the band $s \pm 1$ (blue), so $|s_n| < |s| + 1$; the finitely many early terms (gray) are handled by the maximum. Here the early term $|s_2|$ (red) is the largest, so it sets $M$, and every term lies between $-M$ and $M$.*

> [!remark]- Connections
> - Computational version: [[§60 Convergence of Sequences#^prop-60-4|342 Prop. §60.4]] (the same statement for complex sequences).

> [!example] Example §9.1: $\sqrt{n}$ Diverges
> The sequence $s_n = \sqrt{n}$ is not convergent. Why? It is unbounded: given any $M$, the [[Archimedean Property|Archimedean property]] provides $n > M^2$, and then $\sqrt{n} > M$. By the [[Contrapositive, Converse and Inverse|contrapositive]] of the theorem, an unbounded sequence cannot converge.

^ex-9-1

## Arithmetic of Limits

> [!theorem] Theorem §9.2: Scalar Multiples
> If $(s_n)$ is convergent, then for any $k \in \mathbb{R}$, $(k s_n)$ is also convergent, and
>
> $$
> \lim_{n\to\infty} k s_n = k \lim_{n\to\infty} s_n
> $$
>
> — the limit and the multiplication can be exchanged.

^thm-9-2

> [!proof]+ Proof
> Let $s = \lim s_n$. If $k = 0$ the sequence is constantly $0$. Otherwise, given $\varepsilon > 0$, choose $N$ with $|s_n - s| < \varepsilon / |k|$ for $n \geq N$; then $|k s_n - k s| = |k| \, |s_n - s| < \varepsilon$.

^pf-9-2

*Uses:* [[§7 Limits of Sequences#^def-7-2|Def. §7.2]]

> [!remark]- Connections
> - Computational version: limit laws for sequences, [[§80 Sequences#^thm-80-3|Calc Thm. §80.3]] (with worked examples).

> [!theorem] Theorem §9.3: Sums and Products
> If $s_n \to s$ and $t_n \to t$, then
>
> $$
> s_n + t_n \to s + t \qquad \text{and} \qquad s_n t_n \to s t.
> $$

^thm-9-3

> [!proof]+ Proof
> **Sum** (the easy one). Given $\varepsilon > 0$, we can require
>
> $$
> |s_n - s| < \frac\varepsilon2 \quad (n \geq N_1) \qquad \text{and} \qquad |t_n - t| < \frac\varepsilon2 \quad (n \geq N_2),
> $$
>
> by applying the definitions with tolerance $\varepsilon/2$. For $n \geq N = \max\{N_1, N_2\}$, the triangle inequality gives
>
> $$
> |s_n + t_n - (s + t)| \leq |s_n - s| + |t_n - t| < \frac\varepsilon2 + \frac\varepsilon2 = \varepsilon.
> $$
>
> **Product.** What is $|s_n t_n - st|$? Add and subtract the mixed term $s t_n$:
>
> $$
> |s_n t_n - s t| = |s_n t_n - s t_n + s t_n - s t|
> \leq |s_n t_n - s t_n| + |s t_n - s t|
> = |s_n - s|\,|t_n| + |t_n - t|\,|s|.
> $$
>
> If both summands are $< \varepsilon/2$, we are done. How? Since $(t_n)$ is convergent, it is *bounded* ([[§9 Limit Theorems for Sequences#^thm-9-1|Theorem §9.1]]): there exists $M > 0$ with $|t_n| \leq M$ for all $n$; enlarging $M$ if necessary, we may also assume $|s| \leq M$. Then
>
> $$
> |s_n - s|\,|t_n| \leq M |s_n - s|, \qquad |t_n - t|\,|s| \leq M |t_n - t|.
> $$
>
> Now, given $\varepsilon > 0$, require
>
> $$
> M |s_n - s| < \frac\varepsilon2 \quad (n \geq N_1) \qquad \text{and} \qquad M |t_n - t| < \frac\varepsilon2 \quad (n \geq N_2),
> $$
>
> i.e. apply the two convergence definitions with tolerance $\varepsilon / (2M)$. For $n \geq \max\{N_1, N_2\}$,
>
> $$
> |s_n t_n - st| \leq M|s_n - s| + M|t_n - t| < \varepsilon.
> $$

^pf-9-3

*Uses:* [[§7 Limits of Sequences#^def-7-2|Def. §7.2]], [[§3 The Set ℝ of Real Numbers#^thm-3-3|§3.3]], [[§9 Limit Theorems for Sequences#^thm-9-1|§9.1]]

> [!remark]- Connections
> - Computational version: limit laws for sequences, [[§80 Sequences#^thm-80-3|Calc Thm. §80.3]] (with worked examples).

**What is next? Division!**

> [!theorem] Theorem §9.4: Quotients
> Assume $s_n \to s$ and $t_n \to t$, with $t \neq 0$ (and $t_n \neq 0$ for all $n$, so the quotients are defined). Then
>
> $$
> \frac{s_n}{t_n} \longrightarrow \frac{s}{t}.
> $$

^thm-9-4

> [!proof]+ Proof
> The idea is the same. Combine over a common denominator and insert the mixed term $st$:
>
> $$
> \left| \frac{s_n}{t_n} - \frac{s}{t} \right|
> = \left| \frac{s_n t - s t_n}{t_n t} \right|
> = \left| \frac{s_n t - st + st - s t_n}{t_n t} \right|
> \leq \frac{|s_n - s|\,|t| + |s|\,|t - t_n|}{|t_n|\,|t|}.
> $$
>
> The new issue is the denominator: we need $|t_n|$ bounded away from $0$. Since $|t_n| \to |t| > \tfrac{|t|}{2}$, the “eventually above $a$” example of §8 (applied to the sequence $|t_n|$ with $a = |t|/2$) gives $N_0$ such that
>
> $$
> |t_n| > \frac{|t|}{2} \qquad \text{for } n \geq N_0.
> $$
>
> For such $n$,
>
> $$
> \left| \frac{s_n}{t_n} - \frac{s}{t} \right|
> \leq \frac{|s_n - s|\,|t| + |s|\,|t_n - t|}{\tfrac{|t|}{2}\,|t|}
> = \frac{2}{|t|} |s_n - s| + \frac{2|s|}{|t|^2} |t_n - t|.
> $$
>
> Both coefficients are fixed constants, so as in the product proof: given $\varepsilon > 0$, choose $N_1$ with $\tfrac{2}{|t|}|s_n - s| < \tfrac\varepsilon2$ for $n \geq N_1$, and $N_2$ with $\tfrac{2|s|}{|t|^2}|t_n - t| < \tfrac\varepsilon2$ for $n \geq N_2$ (if $s = 0$ the second term vanishes and any $N_2$ works). For $n \geq \max\{N_0, N_1, N_2\}$, the sum is $< \varepsilon$.

^pf-9-4

*Uses:* [[§7 Limits of Sequences#^def-7-2|Def. §7.2]], [[§8 A Discussion About Proofs#^ex-8-9|Ex. §8.9]], [[§3 The Set ℝ of Real Numbers#^thm-3-3|§3.3]]

> [!remark]- Connections
> - Computational version: limit laws for sequences, [[§80 Sequences#^thm-80-3|Calc Thm. §80.3]] (with worked examples).

An order-theoretic companion to the arithmetic rules — invoked constantly in these notes as “limits preserve $\leq$”:

> [!theorem] Proposition §9.5: Limits Preserve Weak Inequalities (HW)
> Suppose there exists $N_0$ such that $s_n \leq t_n$ for all $n > N_0$, and suppose $\lim s_n = s$ and $\lim t_n = t$ exist. Then
>
> $$
> s \leq t.
> $$

^prop-9-5

> [!proof]+ Proof
> Assume for contradiction $s > t$, and set $\varepsilon = \tfrac{s-t}{2} > 0$. By the difference rule ([[§9 Limit Theorems for Sequences#^thm-9-2|Theorem §9.2]] with $k = -1$, and [[§9 Limit Theorems for Sequences#^thm-9-3|Theorem §9.3]]), $t_n - s_n \to t - s$, so there is $N_1$ such that for $n > N_1$,
>
> $$
> |(t_n - s_n) - (t - s)| < \varepsilon, \qquad \text{in particular} \qquad t_n - s_n < (t - s) + \frac{s-t}{2} = \frac{t-s}{2} < 0.
> $$
>
> But for $n > \max\{N_0, N_1\}$ the hypothesis gives $t_n - s_n \geq 0$ — contradiction. Hence $s \leq t$.

^pf-9-5

*Uses:* [[§9 Limit Theorems for Sequences#^thm-9-2|§9.2]], [[§9 Limit Theorems for Sequences#^thm-9-3|§9.3]]

> [!remark]- Connections
> - Computational version for limits of functions: [[§10 Direct Substitution, One-Sided Limits and the Squeeze Theorem#^thm-10-4|Calc Thm. §10.4]].

> [!remark] Remark
> *Strict* inequalities are **not** preserved: $0 < \tfrac1n$ for every $n$, yet both limits equal $0$. Passing to the limit can only be trusted with $\leq$.

^rem-9-1

## Basic Sequences

To apply the theorems, we need a stock of basic limits.

> [!example] Example §9.2: $1/n^p \to 0$ for $p > 0$
> By the $(\varepsilon, N)$ definition: $\tfrac{1}{n^p} < \varepsilon$ if and only if $n^p > \tfrac1\varepsilon$, i.e. $n > (1/\varepsilon)^{1/p}$; take $N > (1/\varepsilon)^{1/p}$.

^ex-9-2

> [!example] Example §9.3: $a^n \to 0$ for $0 < a < 1$
> There are several proofs. *The lecture's proof, via logarithms:* we want $|a^n| = a^n < \varepsilon$. Taking $\log$ — legitimate for comparing since $\log$ is an increasing function — gives $n \log a < \log \varepsilon$. Since $\log a < 0$, dividing *flips* the inequality:
>
> $$
> n > \frac{\log \varepsilon}{\log a},
> $$
>
> so take $N > \tfrac{\log\varepsilon}{\log a}$.

^ex-9-3

> [!remark] Remark
> Strictly speaking, the logarithm has not yet been rigorously defined in this course — like the decimal expansion in §4, it is borrowed from the future. A proof from what we have: write $\tfrac1a = 1 + b$ with $b > 0$. By the binomial formula ([[Binomial Theorem|250 Thm. §12.10]], recalled in [[§9 Limit Theorems for Sequences#^ex-9-4|Example §9.4]]), $(1+b)^n \geq 1 + nb > nb$, so
>
> $$
> 0 < a^n = \frac{1}{(1+b)^n} < \frac{1}{nb} \longrightarrow 0,
> $$
>
> and $a^n \to 0$ by the [[Squeeze Theorem|Squeeze Theorem]].

^rem-9-2

> [!example] Example §9.4: $n^{1/n} \to 1$
> Define $s_n = n^{1/n} - 1$; the claim is equivalent to $s_n \to 0$. Note $s_n \geq 0$ for $n \geq 1$, and
>
> $$
> 1 + s_n = n^{1/n}, \qquad \text{so raising to the power } n: \qquad (1 + s_n)^n = n.
> $$
>
> Now recall the **binomial formula** ([[Binomial Theorem|250 Thm. §12.10]]):
>
> $$
> (a+b)^n = a^n + n a^{n-1} b + \frac12 n(n-1) a^{n-2} b^2 + \cdots + n a b^{n-1} + b^n.
> $$
>
> If $a > 0$ and $b \geq 0$, all terms are nonnegative, so keeping only one term,
>
> $$
> (a+b)^n \geq \frac12 n(n-1) a^{n-2} b^2.
> $$
>
> Applying this with $a = 1$, $b = s_n$:
>
> $$
> n = (1 + s_n)^n \geq \frac12 n(n-1) s_n^2,
> $$
>
> hence for $n \geq 2$,
>
> $$
> s_n^2 \leq \frac{2}{n-1}, \qquad \text{i.e.} \qquad 0 \leq s_n \leq \sqrt{\frac{2}{n-1}}.
> $$
>
> Is it clear now that $s_n \to 0$? Yes, by the [[Squeeze Theorem|Squeeze Theorem]]: $\tfrac{2}{n-1} \to 0$ (e.g. $\tfrac{2}{n-1} \leq \tfrac4n$ for $n \geq 2$), hence $\sqrt{2/(n-1)} \to 0$ by the square-root example of §8, and $s_n$ is squeezed between $0$ and a null sequence.

^ex-9-4

> [!theorem] Corollary §9.6: Linear Combinations
> If $s_n \to s$ and $t_n \to t$, then for any two constants $a, b$,
>
> $$
> a s_n + b t_n \longrightarrow a s + b t.
> $$
>
> (Combine the scalar-multiple and sum theorems.) So the limit commutes with *linear combinations* — a very important concept in linear algebra — and, with products and quotients, with all the basic arithmetic operations.

^cor-9-6

> [!example] Example §9.5: $a^{1/n} \to 1$ for Any $a > 0$
> Why is this true? First observe the pattern experimentally. If $a \geq 1$: $a^{1/2} \geq 1$ but smaller than $a$; $a^{1/3} \geq 1$ but smaller than $a^{1/2}$ — the sequence decreases toward $1$ from above. If $a \leq 1$, symmetrically, it increases toward $1$ from below.
>
> *Proof.* **Case (i): $a \geq 1$.** When $n > a$ (Archimedean), $a^{1/n} < n^{1/n}$; and clearly $1 \leq a^{1/n}$. So we have the squeezing
>
> $$
> 1 \leq a^{1/n} < n^{1/n}.
> $$
>
> Both outer sequences ($s_n = 1$ and $t_n = n^{1/n}$) converge to $1$, so $a^{1/n} \to 1$ by the [[Squeeze Theorem|Squeeze Theorem]].
>
> **Case (ii): $a < 1$.** Then $\tfrac1a > 1$, and by case (i) together with the quotient limit theorem,
>
> $$
> a^{1/n} = \frac{1}{(1/a)^{1/n}} \longrightarrow \frac11 = 1. \tag*{$\blacksquare$}
> $$

^ex-9-5

> [!example] Example §9.6: Finding the Limit of a Recursion
> Let $t_1 = 1$ and $t_{n+1} = \dfrac{t_n^2 + 2}{2 t_n}$. *Assuming* $(t_n)$ is convergent, find $t = \lim_{n\to\infty} t_n$.
>
> Rewrite the recursion as $t_{n+1} \cdot (2 t_n) = t_n^2 + 2$. Both sides are convergent sequences ($\lim t_{n+1} = \lim t_n = t$, as the shifted sequence has the same limit), so applying the product and sum limit theorems,
>
> $$
> 2 t^2 = t^2 + 2, \qquad \text{i.e.} \qquad t^2 = 2.
> $$
>
> Since $t_1 = 1 > 0$ and the recursion preserves positivity (by induction), $t \geq 0$; hence $t = \sqrt2$. (This recursion is exactly Newton's method for solving $x^2 = 2$.)

^ex-9-6

> [!remark]- Connections
> - Worked examples: this recursion is Newton's method, [[§35 Newton's Method#^def-35-1|Calc Def. §35.1]].

> [!example] Example §9.7: Limit Theorems Prove Non-Existence Too
> Let $x_1 = 1$ and $x_{n+1} = 3 x_n^2$ for $n \geq 1$.
>
> **(a)** If $a = \lim x_n$ exists, prove $a = \tfrac13$ or $a = 0$. Note $\lim x_{n+1} = \lim x_n = a$; taking limits in the recursion (product theorem) gives
>
> $$
> a = 3a^2, \qquad \text{i.e.} \qquad a(3a - 1) = 0.
> $$
>
> **(b)** Does $\lim x_n$ exist? **No!** Why: $x_1 = 1$ and $x_2 = 3 > 1$; by induction, if $x_n \geq 1$ then $x_{n+1} = 3x_n^2 \geq 3 > 1$, so $x_n \geq 1$ for all $n$. If the limit existed it would satisfy $a \geq 1$ (limits preserve $\geq$), contradicting (a). So the two candidate values rule each other out — the sequence diverges.

^ex-9-7

*Divergence to $\pm\infty$ and the ratio test continue in [[§9a Divergence to ±∞ and the Ratio Test]].*
