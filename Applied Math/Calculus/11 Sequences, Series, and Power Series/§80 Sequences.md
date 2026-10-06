---
type: section
subject: "[[Calculus]]"
chapter: 11
section: 80
stewart: "11.1"
aliases: ["Stewart 11.1"]
tags: [calculus]
---
← [[§79 The Cycloid, the Cardioid and the Four-Leaved Rose]] · ↑ [[· 11 Sequences, Series, and Power Series]] · [[§81 Monotonic and Bounded Sequences]] →

*Stewart, Section 11.1.*

A sequence is an infinite list $a_1, a_2, a_3, \ldots$, that is, a function on the positive integers. This section defines what it means for $a_n$ to approach a limit $L$ and transfers the tools for limits of functions to sequences: the Limit Laws, the Squeeze Theorem, continuous functions, and l'Hospital's Rule applied to a function that agrees with $a_n$ at the integers. The one genuinely new tool is the Monotonic Sequence Theorem: a bounded monotonic sequence converges even when we cannot compute its limit. It rests on the Completeness Axiom, and it is what later makes series with positive terms tractable ([[§82 Series|§82]], [[§83 The Integral Test and Estimates of Sums|§83]]).

## Infinite Sequences

> [!definition] Definition §93.1: Sequence
> An **infinite sequence**, or just a **sequence**, is a list of numbers written in a definite order:
>
> $$
> a_1, \ a_2, \ a_3, \ a_4, \ \ldots, \ a_n, \ \ldots
> $$
>
> $a_1$ is the *first term*, $a_2$ the *second term*, and $a_n$ the *$n$th term*. Every term $a_n$ has a successor $a_{n+1}$. Equivalently, a sequence is a function $f$ whose domain is the set of positive integers, with $a_n = f(n)$.
>
> **Notation.** The sequence $\{a_1, a_2, a_3, \ldots\}$ is also written $\{a_n\}$ or $\{a_n\}_{n=1}^{\infty}$. Unless stated otherwise $n$ starts at $1$; a different starting index is shown in the notation, e.g. $\left\{ \frac{n}{n+1} \right\}_{n=2}^{\infty} = \left\{ \frac23, \frac34, \frac45, \ldots \right\}$.
>
> *Stewart: 11.1 (text)*

^def-80-1

> [!remark] Remark: Ways to Describe a Sequence
> - **By a formula for the $n$th term**, e.g. $a_n = 1/2^n$ (the distances $\frac12, \frac14, \frac18, \ldots$ walked in Zeno's paradox). A factor $(-1)^n$ or $(-1)^{n-1}$ makes the signs alternate: $\left\{ (-1)^n \frac{n+1}{3^n} \right\}_{n=0}^{\infty} = \left\{ 1, -\frac23, \frac39, -\frac{4}{27}, \ldots \right\}$. To find a formula from the first few terms, read off the numerators, the denominators and the signs separately: $\frac35, -\frac{4}{25}, \frac{5}{125}, -\frac{6}{625}, \ldots$ has numerators $n + 2$, denominators $5^n$ and sign $+$ for $n = 1$, so $a_n = (-1)^{n-1} \dfrac{n+2}{5^n}$.
> - **Recursively**, each term from the preceding ones: the **Fibonacci sequence** $f_1 = 1$, $f_2 = 1$, $f_n = f_{n-1} + f_{n-2}$ ($n \ge 3$) gives $\{1, 1, 2, 3, 5, 8, 13, 21, \ldots\}$.
> - **With no defining equation at all**: the $n$th decimal digit of $e$, $\{7, 1, 8, 2, 8, 1, 8, 2, 8, 4, 5, \ldots\}$.
>
> A sequence can be pictured by plotting its terms on a number line or by plotting its graph, the isolated points $(n, a_n)$ (Stewart's Examples 11.1.1–11.1.3).

^rem-80-1

## The Limit of a Sequence

> [!definition] Definition §93.2: Limit of a Sequence
> A sequence $\{a_n\}$ has the **limit** $L$, and we write
>
> $$
> \lim_{n \to \infty} a_n = L \qquad\text{or}\qquad a_n \to L \text{ as } n \to \infty ,
> $$
>
> if we can make the terms $a_n$ as close to $L$ as we like by taking $n$ sufficiently large. If $\lim_{n \to \infty} a_n$ exists, the sequence **converges** (is **convergent**). Otherwise it **diverges** (is **divergent**).
>
> *Stewart: 11.1, Definition 1*

^def-80-2

For example, $1 - \dfrac{n}{n+1} = \dfrac{1}{n+1}$ can be made as small as we like by taking $n$ large, so $\dfrac{n}{n+1} \to 1$. The precise version mirrors the definition of $\lim_{x \to \infty} f(x) = L$ in [[§13 Limits at Infinity; Horizontal Asymptotes#^def-13-4|Definition §13.4]] (Stewart's Definition 2.6.7).

> [!definition] Definition §93.3: Precise Definition of a Limit of a Sequence
> $\lim_{n \to \infty} a_n = L$ means: for every $\varepsilon > 0$ there is a corresponding integer $N$ such that
>
> $$
> \text{if} \quad n > N \quad \text{then} \quad |a_n - L| < \varepsilon .
> $$
>
> *Stewart: 11.1, Definition 2*

^def-80-3

![[m233-69-1.svg]]
*[[§80 Sequences#^def-80-3|Definition §80.3]] for one $\varepsilon$. The terms (dots) may wander in and out of the band $L - \varepsilon < y < L + \varepsilon$ (green) for a while, but from $a_{N+1}$ on (red) every term lies inside it. A smaller $\varepsilon$ usually needs a larger $N$.*

> [!remark]- Connections
> - Rigorous treatment: [[§7 Limits of Sequences#^def-7-2|451 Def. §7.2]] (the same definition, with $n > N$), where the limit is shown to be unique, [[§7 Limits of Sequences#^thm-7-1|451 Thm. §7.1]].
> - See also: [[§37 Solution Sets of Linear Difference Equations#^ex-37-2|235 Ex. §37.2]] (the Fibonacci sequence of Remark: Ways to Describe a Sequence solved by linear algebra: $F_k = (\varphi^k - \psi^k)/\sqrt5$, and $F_{k+1}/F_k \to \varphi$).
> - See also: [[§38 Applications to Markov Chains#^def-38-6|235 Def. §38.6]] ([[§80 Sequences#^def-80-2|Definition §80.2]] for sequences of vectors: convergence entry by entry, used for Markov chains).

A sequence diverges if its terms do not approach a single number. It can oscillate between two values, like $(-1)^n$, or grow without bound.

> [!definition] Definition §80.4: Infinite Limit
> $\lim_{n \to \infty} a_n = \infty$ means: for every positive number $M$ there is an integer $N$ such that
>
> $$
> \text{if} \quad n > N \quad \text{then} \quad a_n > M .
> $$
>
> We then say that $\{a_n\}$ **diverges to $\infty$**. $\lim_{n \to \infty} a_n = -\infty$ is defined analogously (if $n > N$ then $a_n < M$, for every negative $M$).
>
> *Stewart: 11.1, Definition 3*

^def-80-4

## Properties of Convergent Sequences

The only difference between $\lim_{n \to \infty} a_n = L$ and $\lim_{x \to \infty} f(x) = L$ is that $n$ is required to be an integer.

> [!theorem] Theorem §93.1: Limits Through a Function
> If $\displaystyle\lim_{x \to \infty} f(x) = L$ and $f(n) = a_n$ when $n$ is an integer, then $\displaystyle\lim_{n \to \infty} a_n = L$.
>
> The same holds with $L = \infty$ or $L = -\infty$.
>
> *Stewart: 11.1, Theorem 4*

^thm-80-1

> [!proof]+ Proof
> *Stewart gives this as the observation above; here it is written out.* Let $\varepsilon > 0$. Since $\lim_{x \to \infty} f(x) = L$, there is a number $M$ such that $|f(x) - L| < \varepsilon$ whenever $x > M$. Let $N$ be an integer with $N \ge M$. If $n > N$, then $n > M$, so
>
> $$
> |a_n - L| = |f(n) - L| < \varepsilon .
> $$
>
> By [[§80 Sequences#^def-80-3|Definition §80.3]], $a_n \to L$. For $L = \infty$: given $M' > 0$ there is $M$ with $f(x) > M'$ for $x > M$, and the same choice of $N$ gives $a_n > M'$ for $n > N$.

^pf-80-1

*Uses:* [[§80 Sequences#^def-80-3|Def. §80.3]], [[§80 Sequences#^def-80-4|Def. §80.4]], [[§13 Limits at Infinity; Horizontal Asymptotes#^def-13-4|Def. §13.4]], [[§13 Limits at Infinity; Horizontal Asymptotes#^def-13-5|Def. §13.5]]

The converse is false: $f(x) = \sin(\pi x)$ has $f(n) = 0$ for every integer $n$, so $a_n = f(n) \to 0$, but $\lim_{x \to \infty} \sin(\pi x)$ does not exist.

> [!theorem] Corollary §93.2: Reciprocal Powers
> $$
> \lim_{n \to \infty} \frac{1}{n^r} = 0 \qquad \text{if } r > 0 .
> $$
>
> *Stewart: 11.1, Equation 5*

^cor-80-2

> [!proof]+ Proof
> $\lim_{x \to \infty} 1/x^r = 0$ for $r > 0$ ([[§13 Limits at Infinity; Horizontal Asymptotes#^thm-13-3|Theorem §13.3]]), so [[§80 Sequences#^thm-80-1|Theorem §80.1]] with $f(x) = 1/x^r$ gives the result.

^pf-80-2

*Uses:* [[§80 Sequences#^thm-80-1|§80.1]], [[§13 Limits at Infinity; Horizontal Asymptotes#^thm-13-3|§13.3]]

> [!theorem] Theorem §80.3: Limit Laws for Sequences
> Suppose that $\{a_n\}$ and $\{b_n\}$ are convergent sequences and $c$ is a constant. Then
>
> $$
> \begin{aligned}
> &1.\ \lim_{n \to \infty} (a_n + b_n) = \lim_{n \to \infty} a_n + \lim_{n \to \infty} b_n && \text{(Sum Law)} \\
> &2.\ \lim_{n \to \infty} (a_n - b_n) = \lim_{n \to \infty} a_n - \lim_{n \to \infty} b_n && \text{(Difference Law)} \\
> &3.\ \lim_{n \to \infty} c\,a_n = c \lim_{n \to \infty} a_n && \text{(Constant Multiple Law)} \\
> &4.\ \lim_{n \to \infty} (a_n b_n) = \lim_{n \to \infty} a_n \cdot \lim_{n \to \infty} b_n && \text{(Product Law)} \\
> &5.\ \lim_{n \to \infty} \frac{a_n}{b_n} = \frac{\lim_{n \to \infty} a_n}{\lim_{n \to \infty} b_n} \quad \text{if } \lim_{n \to \infty} b_n \ne 0 && \text{(Quotient Law)}
> \end{aligned}
> $$
>
> Also $\lim_{n \to \infty} c = c$ for any constant $c$.
>
> *Stewart: 11.1 (text), Limit Laws for Sequences*

^thm-80-3

*Stewart does not prove these separately ("their proofs are similar" to those of the Limit Laws for functions, [[§9 Calculating Limits Using the Limit Laws#^thm-9-1|Theorem §9.1]], proved in 2.4 and Appendix F). Proofs for sequences: [[§9 Limit Theorems for Sequences#^thm-9-3|451 Thm. §9.3]] (sums and products), [[§9 Limit Theorems for Sequences#^thm-9-2|451 Thm. §9.2]] (scalar multiples) and [[§9 Limit Theorems for Sequences#^thm-9-4|451 Thm. §9.4]] (quotients).*

> [!theorem] Theorem §80.4: Squeeze Theorem for Sequences
> If $a_n \le b_n \le c_n$ for $n \ge n_0$ and $\displaystyle\lim_{n \to \infty} a_n = \lim_{n \to \infty} c_n = L$, then $\displaystyle\lim_{n \to \infty} b_n = L$.
>
> *Stewart: 11.1 (text), Squeeze Theorem for Sequences*

^thm-80-4

> [!proof]+ Proof
> *Stewart states this without proof; the proof of the Squeeze Theorem for functions in Appendix F ([[§10 Direct Substitution, One-Sided Limits and the Squeeze Theorem#^thm-10-5|Theorem §10.5]]) adapts as follows.* Let $\varepsilon > 0$. Since $a_n \to L$ there is $N_1$ with $|a_n - L| < \varepsilon$, in particular $L - \varepsilon < a_n$, for $n > N_1$. Since $c_n \to L$ there is $N_2$ with $c_n < L + \varepsilon$ for $n > N_2$. Let $N = \max\{n_0, N_1, N_2\}$. For $n > N$,
>
> $$
> L - \varepsilon < a_n \le b_n \le c_n < L + \varepsilon ,
> $$
>
> so $|b_n - L| < \varepsilon$. Hence $b_n \to L$.

^pf-80-4

*Uses:* [[§80 Sequences#^def-80-3|Def. §80.3]]

> [!remark]- Connections
> - Rigorous treatment: [[§8 A Discussion About Proofs#^thm-8-1|451 Thm. §8.1]] (for $a_n \le b_n \le c_n$ for all $n$, with the same proof; hub [[Squeeze Theorem]]). The version for functions is [[§10 Direct Substitution, One-Sided Limits and the Squeeze Theorem#^thm-10-5|Theorem §10.5]].

> [!theorem] Theorem §80.5: Absolute Value Tending to Zero
> If $\displaystyle\lim_{n \to \infty} |a_n| = 0$, then $\displaystyle\lim_{n \to \infty} a_n = 0$.
>
> *Stewart: 11.1, Theorem 6*

^thm-80-5

> [!proof]+ Proof
> (Stewart leaves this as Exercise 93.) For every $n$, $-|a_n| \le a_n \le |a_n|$. By the Constant Multiple Law, $\lim_{n \to \infty} (-|a_n|) = -\lim_{n \to \infty} |a_n| = 0$, and $\lim_{n \to \infty} |a_n| = 0$ by hypothesis. By the Squeeze Theorem, $a_n \to 0$.

^pf-80-5

*Uses:* [[§80 Sequences#^thm-80-3|§80.3]], [[§80 Sequences#^thm-80-4|§80.4]]

> [!theorem] Theorem §80.6: Continuous Functions Preserve Limits of Sequences
> If $\displaystyle\lim_{n \to \infty} a_n = L$ and the function $f$ is continuous at $L$, then
>
> $$
> \lim_{n \to \infty} f(a_n) = f(L) .
> $$
>
> *Stewart: 11.1, Theorem 7; proof in Appendix F*

^thm-80-6

> [!proof]+ Proof
> Let $\varepsilon > 0$. Since $f$ is continuous at $L$, $\lim_{x \to L} f(x) = f(L)$, so there is $\delta > 0$ such that
>
> $$
> |x - L| < \delta \quad\Longrightarrow\quad |f(x) - f(L)| < \varepsilon . \qquad (1)
> $$
>
> (The limit definition gives this for $0 < |x - L| < \delta$, which is how Stewart writes it; for $x = L$ it holds trivially, and that case is needed because $a_n$ may equal $L$.) Since $a_n \to L$ and $\delta > 0$, there is an integer $N$ such that
>
> $$
> n > N \quad\Longrightarrow\quad |a_n - L| < \delta . \qquad (2)
> $$
>
> Combining (1) with $x = a_n$ and (2): if $n > N$ then $|f(a_n) - f(L)| < \varepsilon$. By [[§80 Sequences#^def-80-3|Definition §80.3]], $f(a_n) \to f(L)$.
>
> The same argument works if $f$ is only continuous from the right at $L$ and $a_n \ge L$ for all $n$ (or from the left and $a_n \le L$): (1) is then only needed for $L \le x < L + \delta$.

^pf-80-6

*Uses:* [[§80 Sequences#^def-80-3|Def. §80.3]], [[§12 Continuity#^def-12-1|Def. §12.1]], [[§11 The Precise Definition of a Limit#^def-11-1|Def. §11.1]]

> [!remark]- Connections
> - In 451 this is the *definition* of continuity ([[§17 Continuous Functions#^def-17-1|451 Def. §17.1]]: $f$ is continuous at $L$ if $f(a_n) \to f(L)$ for every sequence $a_n \to L$ in the domain), and its equivalence with the ε–δ form is [[§17 Continuous Functions#^thm-17-1|451 Thm. §17.1]]; the proof above is one half of that equivalence.

> [!theorem] Corollary §80.7: Power Law
> $$
> \lim_{n \to \infty} a_n^p = \Big[ \lim_{n \to \infty} a_n \Big]^p \qquad \text{if } p > 0 \text{ and } a_n > 0 ,
> $$
>
> provided $\lim_{n \to \infty} a_n$ exists.
>
> *Stewart: 11.1 (text), Power Law*

^cor-80-7

> [!proof]+ Proof
> (Stewart leaves this as Exercise 94.) Let $L = \lim a_n$. Then $L \ge 0$: if $L < 0$, [[§80 Sequences#^def-80-3|Definition §80.3]] with $\varepsilon = -L$ would give $a_n < L + \varepsilon = 0$ for large $n$. The function $f(x) = x^p = e^{p \ln x}$ is continuous on $(0, \infty)$ ([[§12 Continuity#^thm-12-6|Theorem §12.6]], [[§12 Continuity#^thm-12-9|Theorem §12.9]]), so if $L > 0$, [[§80 Sequences#^thm-80-6|Theorem §80.6]] gives $a_n^p = f(a_n) \to f(L) = L^p$. If $L = 0$, let $\varepsilon > 0$. There is $N$ with $0 < a_n < \varepsilon^{1/p}$ for $n > N$, and then $0 < a_n^p < \varepsilon$ because $x \mapsto x^p$ is increasing on $(0, \infty)$. So $a_n^p \to 0 = 0^p$.

^pf-80-7

*Uses:* [[§80 Sequences#^thm-80-6|§80.6]], [[§80 Sequences#^def-80-3|Def. §80.3]], [[§12 Continuity#^thm-12-6|§12.6]], [[§12 Continuity#^thm-12-9|§12.9]]

> [!example] Example §93.1: Dividing by the Highest Power
> **(a)** Find $\displaystyle\lim_{n \to \infty} \frac{n}{n+1}$.
>
> As for limits at infinity, divide numerator and denominator by the highest power of $n$ in the denominator, then use the Limit Laws and [[§80 Sequences#^cor-80-2|Corollary §80.2]] with $r = 1$:
>
> $$
> \lim_{n \to \infty} \frac{n}{n+1} = \lim_{n \to \infty} \frac{1}{1 + \dfrac1n} = \frac{\lim_{n \to \infty} 1}{\lim_{n \to \infty} 1 + \lim_{n \to \infty} \dfrac1n} = \frac{1}{1 + 0} = 1 .
> $$
>
> **(b)** Is $a_n = \dfrac{n}{\sqrt{10 + n}}$ convergent or divergent?
>
> Divide numerator and denominator by $n = \sqrt{n^2}$:
>
> $$
> \frac{n}{\sqrt{10 + n}} = \frac{1}{\sqrt{\dfrac{10}{n^2} + \dfrac1n}} .
> $$
>
> The numerator is the constant $1$, and the denominator is positive and tends to $\sqrt{0 + 0} = 0$. So $a_n \to \infty$: the sequence diverges.
>
> *Stewart: Examples 11.1.4 and 11.1.5*

^ex-80-1

> [!example] Example §93.2: Passing to a Function of a Real Variable
> **(a)** Calculate $\displaystyle\lim_{n \to \infty} \frac{\ln n}{n}$.
>
> Numerator and denominator both tend to $\infty$. L'Hospital's Rule ([[§31 Indeterminate Forms and L'Hospital's Rule#^thm-31-2|Theorem §31.2]]) applies to functions of a real variable, not to sequences, so apply it to $f(x) = (\ln x)/x$:
>
> $$
> \lim_{x \to \infty} \frac{\ln x}{x} = \lim_{x \to \infty} \frac{1/x}{1} = 0 .
> $$
>
> Since $f(n) = (\ln n)/n$, [[§80 Sequences#^thm-80-1|Theorem §80.1]] gives $\displaystyle\lim_{n \to \infty} \frac{\ln n}{n} = 0$.
>
> **(b)** Find $\displaystyle\lim_{n \to \infty} \sin\frac{\pi}{n}$.
>
> $\pi/n \to 0$ and sine is continuous at $0$, so by [[§80 Sequences#^thm-80-6|Theorem §80.6]],
>
> $$
> \lim_{n \to \infty} \sin\frac{\pi}{n} = \sin\Big( \lim_{n \to \infty} \frac{\pi}{n} \Big) = \sin 0 = 0 .
> $$
>
> *Stewart: Examples 11.1.6 and 11.1.9*

^ex-80-2

> [!example] Example §93.3: Squeezing
> **(a)** Evaluate $\displaystyle\lim_{n \to \infty} \frac{(-1)^n}{n}$ if it exists.
>
> The terms alternate in sign, so look at absolute values first: $\displaystyle\lim_{n \to \infty} \left| \frac{(-1)^n}{n} \right| = \lim_{n \to \infty} \frac1n = 0$. By [[§80 Sequences#^thm-80-5|Theorem §80.5]], $\displaystyle\lim_{n \to \infty} \frac{(-1)^n}{n} = 0$.
>
> **(b)** Discuss the convergence of $a_n = n!/n^n$, where $n! = 1 \cdot 2 \cdot 3 \cdots n$.
>
> Numerator and denominator tend to $\infty$, but there is no function to use with l'Hospital's Rule ($x!$ is not defined for non-integers). Write out the terms:
>
> $$
> a_1 = 1, \qquad a_2 = \frac{1 \cdot 2}{2 \cdot 2}, \qquad a_3 = \frac{1 \cdot 2 \cdot 3}{3 \cdot 3 \cdot 3}, \qquad a_n = \frac{1 \cdot 2 \cdot 3 \cdots n}{n \cdot n \cdot n \cdots n} . \qquad (8)
> $$
>
> They seem to decrease towards $0$. To confirm this, split off the first factor in (8):
>
> $$
> a_n = \frac1n \left( \frac{2 \cdot 3 \cdots n}{n \cdot n \cdots n} \right) .
> $$
>
> The bracket is a product of $n - 1$ factors $k/n$ with $2 \le k \le n$, each at most $1$, so it is at most $1$, and
>
> $$
> 0 < a_n \le \frac1n .
> $$
>
> Since $1/n \to 0$, the Squeeze Theorem gives $a_n \to 0$.
>
> *Stewart: Examples 11.1.8 and 11.1.10*

^ex-80-3

Stewart's Example 11 classifies the geometric sequence $\{r^n\}$; the result is used throughout the chapter.

> [!theorem] Theorem §80.8: The Sequence of Powers
> The sequence $\{r^n\}$ is convergent if $-1 < r \le 1$ and divergent for all other values of $r$:
>
> $$
> \lim_{n \to \infty} r^n = \begin{cases} 0 & \text{if } -1 < r < 1 \\ 1 & \text{if } r = 1 . \end{cases}
> $$
>
> Moreover $r^n \to \infty$ if $r > 1$.
>
> *Stewart: 11.1, Equation 9 (from Example 11.1.11)*

^thm-80-8

> [!proof]+ Proof
> **$r > 1$ and $0 < r < 1$.** From [[§13 Limits at Infinity; Horizontal Asymptotes#^thm-13-4|Theorem §13.4]] and the graphs of exponential functions ([[§4 Exponential Functions#^prop-4-2|Proposition §4.2]]), $\lim_{x \to \infty} b^x = \infty$ for $b > 1$ and $\lim_{x \to \infty} b^x = 0$ for $0 < b < 1$. With $b = r$ and [[§80 Sequences#^thm-80-1|Theorem §80.1]], $r^n \to \infty$ if $r > 1$ and $r^n \to 0$ if $0 < r < 1$.
>
> **$r = 1$ and $r = 0$.** $1^n = 1 \to 1$ and $0^n = 0 \to 0$ (constant sequences).
>
> **$-1 < r < 0$.** Then $0 < |r| < 1$, so $|r^n| = |r|^n \to 0$ by the first case, and $r^n \to 0$ by [[§80 Sequences#^thm-80-5|Theorem §80.5]].
>
> **$r \le -1$.** Stewart says "$\{r^n\}$ diverges as in Example 7" (where $(-1)^n = -1, 1, -1, 1, \ldots$ oscillates between $1$ and $-1$ and so approaches no number). In general: consecutive terms $r^n$ and $r^{n+1}$ have opposite signs and absolute values $|r|^n \ge 1$, so $|r^{n+1} - r^n| = |r|^n + |r|^{n+1} \ge 2$ for every $n$. If $r^n \to L$, then with $\varepsilon = \frac12$ there would be $N$ with $|r^n - L| < \frac12$ for all $n > N$, and then $|r^{n+1} - r^n| \le |r^{n+1} - L| + |L - r^n| < 1$, a contradiction. So $\{r^n\}$ diverges.

^pf-80-8

*Uses:* [[§80 Sequences#^thm-80-1|§80.1]], [[§80 Sequences#^thm-80-5|§80.5]], [[§80 Sequences#^def-80-3|Def. §80.3]], [[§13 Limits at Infinity; Horizontal Asymptotes#^thm-13-4|§13.4]], [[§4 Exponential Functions#^prop-4-2|§4.2]]

*The section continues in [[§81 Monotonic and Bounded Sequences]].*
