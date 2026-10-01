---
type: section
subject: "[[Calculus]]"
chapter: 11
section: 69
stewart: "11.1"
aliases: ["Stewart 11.1"]
tags: [calculus]
---
← [[§68 Conic Sections in Polar Coordinates]] · ↑ [[· 11 Sequences, Series, and Power Series]] · [[§70 Series]] →

*Stewart, Section 11.1.*

A sequence is an infinite list $a_1, a_2, a_3, \ldots$, that is, a function on the positive integers. This section defines what it means for $a_n$ to approach a limit $L$ and transfers the tools for limits of functions to sequences: the Limit Laws, the Squeeze Theorem, continuous functions, and l'Hospital's Rule applied to a function that agrees with $a_n$ at the integers. The one genuinely new tool is the Monotonic Sequence Theorem: a bounded monotonic sequence converges even when we cannot compute its limit. It rests on the Completeness Axiom, and it is what later makes series with positive terms tractable ([[§70 Series|§70]], [[§71 The Integral Test and Estimates of Sums|§71]]).

## Infinite Sequences

> [!definition] Definition §69.1: Sequence
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

^def-69-1

> [!remark] Remark: Ways to Describe a Sequence
> - **By a formula for the $n$th term**, e.g. $a_n = 1/2^n$ (the distances $\frac12, \frac14, \frac18, \ldots$ walked in Zeno's paradox). A factor $(-1)^n$ or $(-1)^{n-1}$ makes the signs alternate: $\left\{ (-1)^n \frac{n+1}{3^n} \right\}_{n=0}^{\infty} = \left\{ 1, -\frac23, \frac39, -\frac{4}{27}, \ldots \right\}$. To find a formula from the first few terms, read off the numerators, the denominators and the signs separately: $\frac35, -\frac{4}{25}, \frac{5}{125}, -\frac{6}{625}, \ldots$ has numerators $n + 2$, denominators $5^n$ and sign $+$ for $n = 1$, so $a_n = (-1)^{n-1} \dfrac{n+2}{5^n}$.
> - **Recursively**, each term from the preceding ones: the **Fibonacci sequence** $f_1 = 1$, $f_2 = 1$, $f_n = f_{n-1} + f_{n-2}$ ($n \ge 3$) gives $\{1, 1, 2, 3, 5, 8, 13, 21, \ldots\}$.
> - **With no defining equation at all**: the $n$th decimal digit of $e$, $\{7, 1, 8, 2, 8, 1, 8, 2, 8, 4, 5, \ldots\}$.
>
> A sequence can be pictured by plotting its terms on a number line or by plotting its graph, the isolated points $(n, a_n)$ (Stewart's Examples 11.1.1–11.1.3).

^rem-69-1

## The Limit of a Sequence

> [!definition] Definition §69.2: Limit of a Sequence
> A sequence $\{a_n\}$ has the **limit** $L$, and we write
>
> $$
> \lim_{n \to \infty} a_n = L \qquad\text{or}\qquad a_n \to L \text{ as } n \to \infty ,
> $$
>
> if we can make the terms $a_n$ as close to $L$ as we like by taking $n$ sufficiently large. If $\lim_{n \to \infty} a_n$ exists, the sequence **converges** (is **convergent**). Otherwise it **diverges** (is **divergent**).
>
> *Stewart: 11.1, Definition 1*

^def-69-2

For example, $1 - \dfrac{n}{n+1} = \dfrac{1}{n+1}$ can be made as small as we like by taking $n$ large, so $\dfrac{n}{n+1} \to 1$. The precise version mirrors the definition of $\lim_{x \to \infty} f(x) = L$ in [[§11 Limits at Infinity; Horizontal Asymptotes|§11]] (Definition 2.6.7).

> [!definition] Definition §69.3: Precise Definition of a Limit of a Sequence
> $\lim_{n \to \infty} a_n = L$ means: for every $\varepsilon > 0$ there is a corresponding integer $N$ such that
>
> $$
> \text{if} \quad n > N \quad \text{then} \quad |a_n - L| < \varepsilon .
> $$
>
> *Stewart: 11.1, Definition 2*

^def-69-3

![[m233-69-1.svg]]
*Definition §69.3 for one $\varepsilon$. The terms (dots) may wander in and out of the band $L - \varepsilon < y < L + \varepsilon$ (green) for a while, but from $a_{N+1}$ on (red) every term lies inside it. A smaller $\varepsilon$ usually needs a larger $N$.*

> [!remark]- Connections
> - Rigorous treatment: [[§7 Limits of Sequences#^def-7-2|451 Def. §7.2]] (the same definition, with $n > N$), where the limit is shown to be unique, [[§7 Limits of Sequences#^thm-7-1|451 Thm. §7.1]].

A sequence diverges if its terms do not approach a single number. It can oscillate between two values, like $(-1)^n$, or grow without bound.

> [!definition] Definition §69.4: Infinite Limit
> $\lim_{n \to \infty} a_n = \infty$ means: for every positive number $M$ there is an integer $N$ such that
>
> $$
> \text{if} \quad n > N \quad \text{then} \quad a_n > M .
> $$
>
> We then say that $\{a_n\}$ **diverges to $\infty$**. $\lim_{n \to \infty} a_n = -\infty$ is defined analogously (if $n > N$ then $a_n < M$, for every negative $M$).
>
> *Stewart: 11.1, Definition 3*

^def-69-4

## Properties of Convergent Sequences

The only difference between $\lim_{n \to \infty} a_n = L$ and $\lim_{x \to \infty} f(x) = L$ is that $n$ is required to be an integer.

> [!theorem] Theorem §69.1: Limits Through a Function
> If $\displaystyle\lim_{x \to \infty} f(x) = L$ and $f(n) = a_n$ when $n$ is an integer, then $\displaystyle\lim_{n \to \infty} a_n = L$.
>
> The same holds with $L = \infty$ or $L = -\infty$.
>
> *Stewart: 11.1, Theorem 4*

^thm-69-1

> [!proof]+ Proof
> *Stewart gives this as the observation above; here it is written out.* Let $\varepsilon > 0$. Since $\lim_{x \to \infty} f(x) = L$, there is a number $M$ such that $|f(x) - L| < \varepsilon$ whenever $x > M$. Let $N$ be an integer with $N \ge M$. If $n > N$, then $n > M$, so
>
> $$
> |a_n - L| = |f(n) - L| < \varepsilon .
> $$
>
> By Definition §69.3, $a_n \to L$. For $L = \infty$: given $M' > 0$ there is $M$ with $f(x) > M'$ for $x > M$, and the same choice of $N$ gives $a_n > M'$ for $n > N$.

^pf-69-1

*Uses:* [[§69 Sequences#^def-69-3|Def. §69.3]], [[§69 Sequences#^def-69-4|Def. §69.4]], [[§11 Limits at Infinity; Horizontal Asymptotes|§11]] (Definitions 2.6.7 and 2.6.9)

The converse is false: $f(x) = \sin(\pi x)$ has $f(n) = 0$ for every integer $n$, so $a_n = f(n) \to 0$, but $\lim_{x \to \infty} \sin(\pi x)$ does not exist.

> [!theorem] Corollary §69.2: Reciprocal Powers
> $$
> \lim_{n \to \infty} \frac{1}{n^r} = 0 \qquad \text{if } r > 0 .
> $$
>
> *Stewart: 11.1, Equation 5*

^cor-69-2

> [!proof]+ Proof
> $\lim_{x \to \infty} 1/x^r = 0$ for $r > 0$ (Theorem 2.6.5), so Theorem §69.1 with $f(x) = 1/x^r$ gives the result.

^pf-69-2

*Uses:* [[§69 Sequences#^thm-69-1|§69.1]], [[§11 Limits at Infinity; Horizontal Asymptotes|§11]] (Theorem 2.6.5)

> [!theorem] Theorem §69.3: Limit Laws for Sequences
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

^thm-69-3

*Stewart does not prove these separately ("their proofs are similar" to those of the Limit Laws for functions, [[§8 Calculating Limits Using the Limit Laws|§8]] and Appendix F). Proofs for sequences: [[§9 Limit Theorems for Sequences#^thm-9-3|451 Thm. §9.3]] (sums and products), [[§9 Limit Theorems for Sequences#^thm-9-2|451 Thm. §9.2]] (scalar multiples) and [[§9 Limit Theorems for Sequences#^thm-9-4|451 Thm. §9.4]] (quotients).*

> [!theorem] Theorem §69.4: Squeeze Theorem for Sequences
> If $a_n \le b_n \le c_n$ for $n \ge n_0$ and $\displaystyle\lim_{n \to \infty} a_n = \lim_{n \to \infty} c_n = L$, then $\displaystyle\lim_{n \to \infty} b_n = L$.
>
> *Stewart: 11.1 (text), Squeeze Theorem for Sequences*

^thm-69-4

> [!proof]+ Proof
> *Stewart states this without proof; the proof of the Squeeze Theorem for functions in Appendix F adapts as follows.* Let $\varepsilon > 0$. Since $a_n \to L$ there is $N_1$ with $|a_n - L| < \varepsilon$, in particular $L - \varepsilon < a_n$, for $n > N_1$. Since $c_n \to L$ there is $N_2$ with $c_n < L + \varepsilon$ for $n > N_2$. Let $N = \max\{n_0, N_1, N_2\}$. For $n > N$,
>
> $$
> L - \varepsilon < a_n \le b_n \le c_n < L + \varepsilon ,
> $$
>
> so $|b_n - L| < \varepsilon$. Hence $b_n \to L$.

^pf-69-4

*Uses:* [[§69 Sequences#^def-69-3|Def. §69.3]]

> [!theorem] Theorem §69.5: Absolute Value Tending to Zero
> If $\displaystyle\lim_{n \to \infty} |a_n| = 0$, then $\displaystyle\lim_{n \to \infty} a_n = 0$.
>
> *Stewart: 11.1, Theorem 6*

^thm-69-5

> [!proof]+ Proof
> (Stewart leaves this as Exercise 93.) For every $n$, $-|a_n| \le a_n \le |a_n|$. By the Constant Multiple Law, $\lim_{n \to \infty} (-|a_n|) = -\lim_{n \to \infty} |a_n| = 0$, and $\lim_{n \to \infty} |a_n| = 0$ by hypothesis. By the Squeeze Theorem, $a_n \to 0$.

^pf-69-5

*Uses:* [[§69 Sequences#^thm-69-3|§69.3]], [[§69 Sequences#^thm-69-4|§69.4]]

> [!example] Example §69.1: Dividing by the Highest Power
> **(a)** Find $\displaystyle\lim_{n \to \infty} \frac{n}{n+1}$.
>
> As for limits at infinity, divide numerator and denominator by the highest power of $n$ in the denominator, then use the Limit Laws and Corollary §69.2 with $r = 1$:
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

^ex-69-1

> [!example] Example §69.2: Passing to a Function of a Real Variable
> **(a)** Calculate $\displaystyle\lim_{n \to \infty} \frac{\ln n}{n}$.
>
> Numerator and denominator both tend to $\infty$. L'Hospital's Rule ([[§28 Indeterminate Forms and L'Hospital's Rule|§28]]) applies to functions of a real variable, not to sequences, so apply it to $f(x) = (\ln x)/x$:
>
> $$
> \lim_{x \to \infty} \frac{\ln x}{x} = \lim_{x \to \infty} \frac{1/x}{1} = 0 .
> $$
>
> Since $f(n) = (\ln n)/n$, Theorem §69.1 gives $\displaystyle\lim_{n \to \infty} \frac{\ln n}{n} = 0$.
>
> **(b)** Find $\displaystyle\lim_{n \to \infty} \sin\frac{\pi}{n}$.
>
> $\pi/n \to 0$ and sine is continuous at $0$, so by Theorem §69.6 below,
>
> $$
> \lim_{n \to \infty} \sin\frac{\pi}{n} = \sin\Big( \lim_{n \to \infty} \frac{\pi}{n} \Big) = \sin 0 = 0 .
> $$
>
> *Stewart: Examples 11.1.6 and 11.1.9*

^ex-69-2

> [!example] Example §69.3: Squeezing
> **(a)** Evaluate $\displaystyle\lim_{n \to \infty} \frac{(-1)^n}{n}$ if it exists.
>
> The terms alternate in sign, so look at absolute values first: $\displaystyle\lim_{n \to \infty} \left| \frac{(-1)^n}{n} \right| = \lim_{n \to \infty} \frac1n = 0$. By Theorem §69.5, $\displaystyle\lim_{n \to \infty} \frac{(-1)^n}{n} = 0$.
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

^ex-69-3

> [!theorem] Theorem §69.6: Continuous Functions Preserve Limits of Sequences
> If $\displaystyle\lim_{n \to \infty} a_n = L$ and the function $f$ is continuous at $L$, then
>
> $$
> \lim_{n \to \infty} f(a_n) = f(L) .
> $$
>
> *Stewart: 11.1, Theorem 7; proof in Appendix F*

^thm-69-6

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
> Combining (1) with $x = a_n$ and (2): if $n > N$ then $|f(a_n) - f(L)| < \varepsilon$. By Definition §69.3, $f(a_n) \to f(L)$.
>
> The same argument works if $f$ is only continuous from the right at $L$ and $a_n \ge L$ for all $n$ (or from the left and $a_n \le L$): (1) is then only needed for $L \le x < L + \delta$.

^pf-69-6

*Uses:* [[§69 Sequences#^def-69-3|Def. §69.3]], [[§10 Continuity#^def-10-1|Def. §10.1]], [[§9 The Precise Definition of a Limit|§9]] (precise definition of a limit)

> [!remark]- Connections
> - In 451 this is the *definition* of continuity ([[§17 Continuous Functions#^def-17-1|451 Def. §17.1]]: $f$ is continuous at $L$ if $f(a_n) \to f(L)$ for every sequence $a_n \to L$ in the domain), and its equivalence with the ε–δ form is [[§17 Continuous Functions#^thm-17-1|451 Thm. §17.1]]; the proof above is one half of that equivalence.

> [!theorem] Corollary §69.7: Power Law
> $$
> \lim_{n \to \infty} a_n^p = \Big[ \lim_{n \to \infty} a_n \Big]^p \qquad \text{if } p > 0 \text{ and } a_n > 0 ,
> $$
>
> provided $\lim_{n \to \infty} a_n$ exists.
>
> *Stewart: 11.1 (text), Power Law*

^cor-69-7

> [!proof]+ Proof
> (Stewart leaves this as Exercise 94.) Let $L = \lim a_n$; since $a_n > 0$, $L \ge 0$. The function $f(x) = x^p$ is continuous on $(0, \infty)$ ([[§10 Continuity|§10]]), so if $L > 0$, Theorem §69.6 gives $a_n^p = f(a_n) \to f(L) = L^p$. If $L = 0$, let $\varepsilon > 0$. There is $N$ with $0 < a_n < \varepsilon^{1/p}$ for $n > N$, and then $0 < a_n^p < \varepsilon$ because $x \mapsto x^p$ is increasing on $(0, \infty)$. So $a_n^p \to 0 = 0^p$.

^pf-69-7

*Uses:* [[§69 Sequences#^thm-69-6|§69.6]], [[§10 Continuity|§10]] (continuity of power functions)

Stewart's Example 11 classifies the geometric sequence $\{r^n\}$; the result is used throughout the chapter.

> [!theorem] Theorem §69.8: The Sequence of Powers
> The sequence $\{r^n\}$ is convergent if $-1 < r \le 1$ and divergent for all other values of $r$:
>
> $$
> \lim_{n \to \infty} r^n = \begin{cases} 0 & \text{if } -1 < r < 1 \\ 1 & \text{if } r = 1 . \end{cases}
> $$
>
> Moreover $r^n \to \infty$ if $r > 1$.
>
> *Stewart: 11.1, Equation 9 (from Example 11.1.11)*

^thm-69-8

> [!proof]+ Proof
> **$r > 1$ and $0 < r < 1$.** From [[§11 Limits at Infinity; Horizontal Asymptotes|§11]] and the graphs of exponential functions ([[§4 Exponential Functions|§4]]), $\lim_{x \to \infty} b^x = \infty$ for $b > 1$ and $\lim_{x \to \infty} b^x = 0$ for $0 < b < 1$. With $b = r$ and Theorem §69.1, $r^n \to \infty$ if $r > 1$ and $r^n \to 0$ if $0 < r < 1$.
>
> **$r = 1$ and $r = 0$.** $1^n = 1 \to 1$ and $0^n = 0 \to 0$ (constant sequences).
>
> **$-1 < r < 0$.** Then $0 < |r| < 1$, so $|r^n| = |r|^n \to 0$ by the first case, and $r^n \to 0$ by Theorem §69.5.
>
> **$r \le -1$.** Stewart says "$\{r^n\}$ diverges as in Example 7" (where $(-1)^n = -1, 1, -1, 1, \ldots$ oscillates between $1$ and $-1$ and so approaches no number). In general: consecutive terms $r^n$ and $r^{n+1}$ have opposite signs and absolute values $|r|^n \ge 1$, so $|r^{n+1} - r^n| = |r|^n + |r|^{n+1} \ge 2$ for every $n$. If $r^n \to L$, then with $\varepsilon = \frac12$ there would be $N$ with $|r^n - L| < \frac12$ for all $n > N$, and then $|r^{n+1} - r^n| \le |r^{n+1} - L| + |L - r^n| < 1$, a contradiction. So $\{r^n\}$ diverges.

^pf-69-8

*Uses:* [[§69 Sequences#^thm-69-1|§69.1]], [[§69 Sequences#^thm-69-5|§69.5]], [[§69 Sequences#^def-69-3|Def. §69.3]], [[§11 Limits at Infinity; Horizontal Asymptotes|§11]] (limits of exponentials)

> [!remark]- Connections
> - Rigorous treatment: [[§9 Limit Theorems for Sequences#^ex-9-10|451 Ex. §9.10]] (complete classification of the geometric sequence, without logarithms); collected in [[Geometric series]].

## Monotonic and Bounded Sequences

> [!definition] Definition §69.5: Increasing, Decreasing, Monotonic
> A sequence $\{a_n\}$ is **increasing** if $a_n < a_{n+1}$ for all $n \ge 1$, that is, $a_1 < a_2 < a_3 < \cdots$. It is **decreasing** if $a_n > a_{n+1}$ for all $n \ge 1$. It is **monotonic** if it is either increasing or decreasing.
>
> For instance, $\left\{ \frac{3}{n+5} \right\}$ is decreasing: $\dfrac{3}{n+5} > \dfrac{3}{n+6} = \dfrac{3}{(n+1)+5}$, since the second denominator is larger.
>
> *Stewart: 11.1, Definition 10; Example 11.1.12*

^def-69-5

> [!example] Example §69.4: Showing a Sequence Is Decreasing
> Show that $a_n = \dfrac{n}{n^2 + 1}$ is decreasing.
>
> **Solution 1 (compare $a_n$ and $a_{n+1}$).** We must show $a_n > a_{n+1}$, that is, $\dfrac{n}{n^2+1} > \dfrac{n+1}{(n+1)^2 + 1}$. The denominators are positive, so cross-multiplying gives an equivalent inequality:
>
> $$
> \begin{aligned}
> n\big[(n+1)^2 + 1\big] > (n+1)(n^2 + 1)
> &\iff n^3 + 2n^2 + 2n > n^3 + n^2 + n + 1 \\
> &\iff n^2 + n > 1 .
> \end{aligned}
> $$
>
> Since $n \ge 1$, $n^2 + n \ge 2 > 1$ is true. So $a_n > a_{n+1}$ for all $n$.
>
> **Solution 2 (the derivative of a related function).** Let $f(x) = \dfrac{x}{x^2+1}$. By the Quotient Rule,
>
> $$
> f'(x) = \frac{(x^2 + 1) - x \cdot 2x}{(x^2+1)^2} = \frac{1 - x^2}{(x^2+1)^2} < 0 \qquad \text{whenever } x^2 > 1 .
> $$
>
> So $f$ is decreasing on $(1, \infty)$, and, being continuous at $1$, on $[1, \infty)$ ([[§27 What Derivatives Tell Us About the Shape of a Graph|§27]]). Hence $a_n = f(n) > f(n+1) = a_{n+1}$ for all $n \ge 1$.
>
> *Stewart: Example 11.1.13*

^ex-69-4

> [!definition] Definition §69.6: Bounded Sequence
> A sequence $\{a_n\}$ is **bounded above** if there is a number $M$ such that $a_n \le M$ for all $n \ge 1$, and **bounded below** if there is a number $m$ such that $m \le a_n$ for all $n \ge 1$. If it is bounded above and below, it is a **bounded sequence**.
>
> For instance, $a_n = n$ is bounded below ($a_n > 0$) but not above, and $a_n = n/(n+1)$ is bounded since $0 < a_n < 1$.
>
> *Stewart: 11.1, Definition 11*

^def-69-6

Neither condition alone forces convergence: $(-1)^n$ is bounded but divergent, and $a_n = n$ is monotonic but $n \to \infty$. Together they do. If $\{a_n\}$ increases and $a_n \le M$ for all $n$, the terms are forced to crowd together below $M$ and approach some number $L \le M$. Making this precise needs a property of the real numbers.

> [!definition] Definition §69.7: Least Upper Bound; the Completeness Axiom
> A number $b$ is a **least upper bound** of a set $S$ of real numbers if $b$ is an upper bound for $S$ ($x \le b$ for all $x$ in $S$) and $b \le M$ for every other upper bound $M$ of $S$.
>
> **Completeness Axiom.** If $S$ is a nonempty set of real numbers that has an upper bound $M$ ($x \le M$ for all $x$ in $S$), then $S$ has a least upper bound $b$.
>
> The axiom expresses the fact that there is no gap or hole in the real number line. In the same way, a nonempty set with a lower bound has a **greatest lower bound**.
>
> *Stewart: 11.1 (text)*

^def-69-7

> [!remark]- Connections
> - Rigorous treatment: [[§4 The Completeness Axiom#^def-4-4|451 Def. §4.4]] (with the supremum, [[§4 The Completeness Axiom#^def-4-3|451 Def. §4.3]]); hub [[Completeness Axiom]].

> [!theorem] Theorem §69.9: Monotonic Sequence Theorem
> Every bounded, monotonic sequence is convergent.
>
> In particular, a sequence that is increasing and bounded above converges, and a sequence that is decreasing and bounded below converges.
>
> *Stewart: 11.1, Theorem 12*

^thm-69-9

> [!proof]+ Proof
> **Increasing.** Suppose $\{a_n\}$ is increasing and bounded above. The set $S = \{a_n \mid n \ge 1\}$ is nonempty and has an upper bound, so by the Completeness Axiom it has a least upper bound $L$. Let $\varepsilon > 0$. Then $L - \varepsilon$ is *not* an upper bound for $S$, since $L$ is the *least* upper bound. Therefore
>
> $$
> a_N > L - \varepsilon \qquad \text{for some integer } N .
> $$
>
> The sequence is increasing, so $a_n \ge a_N$ for every $n > N$. Thus if $n > N$, then $a_n > L - \varepsilon$, and $a_n \le L$ because $L$ is an upper bound, so
>
> $$
> 0 \le L - a_n < \varepsilon , \qquad\text{that is,}\qquad |L - a_n| < \varepsilon \quad \text{whenever } n > N .
> $$
>
> So $\lim_{n \to \infty} a_n = L$.
>
> **Decreasing.** Stewart says that a similar proof, using the greatest lower bound, works. Equivalently: if $\{a_n\}$ is decreasing and bounded below by $m$, then $\{-a_n\}$ is increasing and bounded above by $-m$, so $-a_n \to L'$ for some $L'$ by the first part, and $a_n \to -L'$ by the Constant Multiple Law.

^pf-69-9

*Uses:* [[§69 Sequences#^def-69-7|Def. §69.7]], [[§69 Sequences#^def-69-5|Def. §69.5]], [[§69 Sequences#^def-69-6|Def. §69.6]], [[§69 Sequences#^def-69-3|Def. §69.3]], [[§69 Sequences#^thm-69-3|§69.3]]

> [!remark]- Connections
> - Rigorous treatment: [[§10 Monotone Sequences and Cauchy Sequences#^thm-10-1|451 Thm. §10.1]] (Monotone Convergence Theorem, same proof); an unbounded monotone sequence tends to $\pm\infty$, [[§10 Monotone Sequences and Cauchy Sequences#^thm-10-3|451 Thm. §10.3]].

> [!example] Example §69.5: A Recursive Sequence
> Investigate the sequence defined by the *recurrence relation*
>
> $$
> a_1 = 2, \qquad a_{n+1} = \tfrac12 (a_n + 6) \qquad \text{for } n = 1, 2, 3, \ldots
> $$
>
> **First terms.** $a_1 = 2$, $a_2 = \frac12(2 + 6) = 4$, $a_3 = \frac12(4 + 6) = 5$, $a_4 = 5.5$, $a_5 = 5.75$, $a_6 = 5.875$, $a_7 = 5.9375$, $a_8 = 5.96875$, $a_9 = 5.984375$. They suggest that the sequence increases towards $6$.
>
> **Increasing, by induction.** $a_2 = 4 > 2 = a_1$. If $a_{k+1} > a_k$, then $a_{k+1} + 6 > a_k + 6$, so $\frac12(a_{k+1} + 6) > \frac12(a_k + 6)$, that is, $a_{k+2} > a_{k+1}$. So $a_{n+1} > a_n$ for all $n$.
>
> **Bounded, by induction.** Being increasing, the sequence is bounded below by $a_1 = 2$. Upper bound: $a_1 = 2 < 6$. If $a_k < 6$, then $a_k + 6 < 12$, so $a_{k+1} = \frac12(a_k + 6) < \frac12 (12) = 6$. So $a_n < 6$ for all $n$.
>
> **The limit.** By the Monotonic Sequence Theorem, $L = \lim_{n \to \infty} a_n$ exists. The theorem does not say what $L$ is, but now the recurrence relation does. As $n \to \infty$ also $n + 1 \to \infty$, so $a_{n+1} \to L$ too (if $|a_n - L| < \varepsilon$ for $n > N$, then also $|a_{n+1} - L| < \varepsilon$ for $n > N$). Taking limits on both sides of the recurrence, with the Limit Laws,
>
> $$
> L = \lim_{n \to \infty} a_{n+1} = \lim_{n \to \infty} \tfrac12 (a_n + 6) = \tfrac12 \Big( \lim_{n \to \infty} a_n + 6 \Big) = \tfrac12 (L + 6) .
> $$
>
> Solving $L = \frac12 (L + 6)$ gives $2L = L + 6$, so $L = 6$, as predicted.
>
> *Stewart: Example 11.1.14*

^ex-69-5

> [!remark] Remark: Method — Finding the Limit of a Sequence
> 1. **Rational expressions in $n$** (also with roots): divide numerator and denominator by the highest power of $n$ in the denominator and use the Limit Laws with $1/n^r \to 0$ ([[§69 Sequences#^ex-69-1|Example §69.1]]).
> 2. **Indeterminate forms with a real-variable formula** ($\ln n / n$, $n^{1/n}$, …): find $\lim_{x \to \infty} f(x)$ by l'Hospital's Rule and transfer it with [[§69 Sequences#^thm-69-1|Theorem §69.1]].
> 3. **Factorials, $(-1)^n$ and other integer-only expressions:** bound $a_n$ between simpler sequences and squeeze, or show $|a_n| \to 0$ ([[§69 Sequences#^ex-69-3|Example §69.3]]). Compare with $r^n$ ([[§69 Sequences#^thm-69-8|Theorem §69.8]]).
> 4. **A continuous function of a convergent sequence:** move the limit inside ([[§69 Sequences#^thm-69-6|Theorem §69.6]]).
> 5. **Recursive sequences:** show by induction that the sequence is monotonic and bounded, conclude that $L$ exists, then let $n \to \infty$ in the recurrence and solve for $L$ ([[§69 Sequences#^ex-69-5|Example §69.5]]). Solving for $L$ before knowing that the limit exists can give a wrong answer.
> 6. **Divergence:** exhibit two different values approached infinitely often, as for $(-1)^n$, or show $a_n \to \pm\infty$.

^rem-69-2
