---
type: section
subject: "[[Complex Variables]]"
chapter: 5
section: 60
bc: "60"
aliases: ["B&C 60"]
tags: [complex-variables, math342]
---
← [[§59b The Function z̄]] · ↑ [[· 5 Series]] · [[§61 Convergence of Series]] →

*Brown–Churchill, Section 60 · MAT 342 HW 9 (optional reading).*

Chapter 5 is about representing analytic functions by series, and every statement about a series is a statement about the limit of its partial sums. This section sets up limits of sequences of complex numbers. The definition is the $\varepsilon$–$n_0$ definition from calculus with $|\cdot|$ the modulus, and the main theorem says that a complex sequence converges exactly when its real and imaginary parts do, so the theory of real sequences carries over. Polar coordinates are different: the moduli of a convergent sequence converge, but its principal arguments need not ([[§60 Convergence of Sequences#^ex-60-2|Example §60.2]]).

## Limits of Sequences

> [!definition] Definition §60.1: Limit of a Sequence
> An infinite sequence $z_1, z_2, \ldots, z_n, \ldots$ of complex numbers **has a limit** $z$ if, for each positive number $\varepsilon$, there exists a positive integer $n_0$ such that
>
> $$
> |z_n - z| < \varepsilon \qquad\text{whenever}\qquad n > n_0 . \qquad (1)
> $$
>
> The sequence then **converges** to $z$, and we write
>
> $$
> \lim_{n\to\infty} z_n = z . \qquad (2)
> $$
>
> A sequence that has no limit **diverges**.
>
> *B&C: Sec. 60 (text)*

^def-60-1

Geometrically, (1) says that for large $n$ the points $z_n$ lie in any prescribed $\varepsilon$ neighborhood of $z$; since $\varepsilon$ may be as small as we please, the points $z_n$ become arbitrarily close to $z$ as $n$ increases. The value of $n_0$ depends, in general, on $\varepsilon$. The notation (2) presupposes that a sequence has at most one limit, which B&C leaves as an exercise.

> [!theorem] Proposition §60.1: Uniqueness of Limits
> A sequence of complex numbers has at most one limit: if $\lim_{n\to\infty} z_n = z$ and $\lim_{n\to\infty} z_n = w$, then $z = w$.
>
> *B&C: Sec. 61, Exercise 5*

^prop-60-1

> [!proof]+ Proof
> Let $\varepsilon > 0$. By (1) there are $n_1$ and $n_2$ with $|z_n - z| < \varepsilon/2$ for $n > n_1$ and $|z_n - w| < \varepsilon/2$ for $n > n_2$. Take any $n$ larger than both. By the triangle inequality,
>
> $$
> |z - w| \le |z - z_n| + |z_n - w| < \frac\varepsilon2 + \frac\varepsilon2 = \varepsilon .
> $$
>
> So the nonnegative number $|z - w|$ is less than every positive $\varepsilon$; hence $|z - w| = 0$ and $z = w$. (The exercise suggests a second route: by [[§60 Convergence of Sequences#^thm-60-2|Theorem §60.2]] below, $\operatorname{Re} z_n$ tends to both $\operatorname{Re} z$ and $\operatorname{Re} w$, so these are equal by uniqueness of real limits, and likewise for the imaginary parts. The direct argument avoids using the theorem before it is proved.)

^pf-60-1

*Uses:* [[§60 Convergence of Sequences#^def-60-1|Def. §60.1]], [[§5 Triangle Inequality#^thm-5-1|§5.1]] (triangle inequality)

> [!theorem] Theorem §60.2: Convergence by Real and Imaginary Parts
> Suppose that $z_n = x_n + iy_n$ $(n = 1, 2, \ldots)$ and $z = x + iy$. Then
>
> $$
> \lim_{n\to\infty} z_n = z \qquad (3)
> $$
>
> if and only if
>
> $$
> \lim_{n\to\infty} x_n = x \qquad\text{and}\qquad \lim_{n\to\infty} y_n = y . \qquad (4)
> $$
>
> *B&C: Sec. 60, Theorem*

^thm-60-2

> [!proof]+ Proof
> **(4) $\Rightarrow$ (3).** Let $\varepsilon > 0$. By (4) there are positive integers $n_1$ and $n_2$ such that
>
> $$
> |x_n - x| < \frac\varepsilon2 \quad\text{whenever } n > n_1, \qquad |y_n - y| < \frac\varepsilon2 \quad\text{whenever } n > n_2 .
> $$
>
> Let $n_0$ be the larger of $n_1$ and $n_2$. Since
>
> $$
> |(x_n + iy_n) - (x + iy)| = |(x_n - x) + i(y_n - y)| \le |x_n - x| + |y_n - y| ,
> $$
>
> we get $|z_n - z| < \frac\varepsilon2 + \frac\varepsilon2 = \varepsilon$ whenever $n > n_0$. So (3) holds.
>
> **(3) $\Rightarrow$ (4).** Let $\varepsilon > 0$, and let $n_0$ be such that $|(x_n + iy_n) - (x + iy)| < \varepsilon$ whenever $n > n_0$. The real and imaginary parts of a complex number are at most its modulus in absolute value, so
>
> $$
> |x_n - x| \le |(x_n - x) + i(y_n - y)| = |z_n - z| , \qquad |y_n - y| \le |(x_n - x) + i(y_n - y)| = |z_n - z| ,
> $$
>
> and therefore $|x_n - x| < \varepsilon$ and $|y_n - y| < \varepsilon$ whenever $n > n_0$. That is, (4) holds.

^pf-60-2

*Uses:* [[§60 Convergence of Sequences#^def-60-1|Def. §60.1]], [[§5 Triangle Inequality#^thm-5-1|§5.1]] (triangle inequality), [[§4 Vectors and Moduli#^prop-4-1|§4.1]] ($|\operatorname{Re} z|, |\operatorname{Im} z| \le |z|$)

> [!remark]- Connections
> - The real-variable definitions and facts that this theorem imports: [[§7 Limits of Sequences#^def-7-2|451 Def. §7.2]] (convergence), [[§7 Limits of Sequences#^thm-7-1|451 Thm. §7.1]] (uniqueness).
> - In metric-space language, $\mathbb{C}$ with $d(z, w) = |z - w|$ is $\mathbb{R}^2$ with the Euclidean distance ([[§13 Some Topological Concepts in Metric Spaces#^ex-13-2|451 Ex. §13.2]]), and the theorem is the case $n = 2$ of [[§13 Some Topological Concepts in Metric Spaces#^prop-13-1|451 Prop. §13.1]]: the Euclidean distance and the max distance $\max(|x_n - x|, |y_n - y|)$ have the same convergent sequences. Completeness of $\mathbb{C}$ follows the same way from [[§13 Some Topological Concepts in Metric Spaces#^thm-13-2|451 Thm. §13.2]].

The theorem lets us write

$$
\lim_{n\to\infty}(x_n + iy_n) = \lim_{n\to\infty} x_n + i\lim_{n\to\infty} y_n
$$

whenever both limits on the right exist or the one on the left exists. Two further facts about limits are left as exercises by B&C and used later in the chapter: the moduli of a convergent sequence converge (in the proof of [[§69★ Absolute and Uniform Convergence of Power Series#^thm-69-3|Theorem §69.3]]), and a convergent sequence is bounded (for the terms of a convergent series, [[§61 Convergence of Series|§61]], and in [[§69★ Absolute and Uniform Convergence of Power Series#^thm-69-1|Theorem §69.1]]).

> [!theorem] Proposition §60.3: Moduli of a Convergent Sequence Converge
> If $\lim_{n\to\infty} z_n = z$, then $\lim_{n\to\infty} |z_n| = |z|$.
>
> *B&C: Sec. 61, Exercise 3*

^prop-60-3

> [!proof]+ Proof
> By the reverse triangle inequality ([[§5 Triangle Inequality#^cor-5-2|Corollary §5.2]]), $\big||z_n| - |z|\big| \le |z_n - z|$. Given $\varepsilon > 0$, choose $n_0$ with $|z_n - z| < \varepsilon$ for $n > n_0$; then $\big||z_n| - |z|\big| < \varepsilon$ for $n > n_0$, which is the statement for the real sequence $|z_n|$.

^pf-60-3

*Uses:* [[§60 Convergence of Sequences#^def-60-1|Def. §60.1]], [[§5 Triangle Inequality#^cor-5-2|§5.2]]

The converse fails: $z_n = (-1)^n$ has $|z_n| = 1$ for all $n$ but does not converge.

> [!theorem] Proposition §60.4: Convergent Sequences Are Bounded
> If a sequence $z_n$ $(n = 1, 2, \ldots)$ converges to a number $z$, then there exists a positive number $M$ such that $|z_n| \le M$ for all $n$.
>
> *B&C: Sec. 61, Exercise 9*

^prop-60-4

> [!proof]+ Proof
> **(a)** Take $\varepsilon = 1$ in (1): there is a positive integer $n_0$ such that $|z_n - z| < 1$ whenever $n > n_0$, and then
>
> $$
> |z_n| = |z + (z_n - z)| \le |z| + |z_n - z| < |z| + 1 \qquad (n > n_0) .
> $$
>
> The finitely many remaining terms $z_1, \ldots, z_{n_0}$ are bounded by the largest of their moduli. So $M = \max\big(|z_1|, \ldots, |z_{n_0}|,\ |z| + 1\big)$ works.
>
> **(b)** Alternatively, write $z_n = x_n + iy_n$. By [[§60 Convergence of Sequences#^thm-60-2|Theorem §60.2]] the real sequences $x_n$ and $y_n$ converge, so they are bounded: $|x_n| \le M_1$ and $|y_n| \le M_2$ for all $n$ ([[§9 Limit Theorems for Sequences#^thm-9-1|451 Thm. §9.1]]). Then $|z_n| \le |x_n| + |y_n| \le M_1 + M_2$.

^pf-60-4

*Uses:* [[§60 Convergence of Sequences#^def-60-1|Def. §60.1]], [[§60 Convergence of Sequences#^thm-60-2|§60.2]], [[§5 Triangle Inequality#^thm-5-1|§5.1]], [[§9 Limit Theorems for Sequences#^thm-9-1|451 Thm. §9.1]]

## Examples

> [!example] Example §60.1: Two Limits by Components and by the Definition
> **(a)** The sequence
>
> $$
> z_n = -1 + i\,\frac{(-1)^n}{n^2} \qquad (n = 1, 2, \ldots)
> $$
>
> converges to $-1$. *By Theorem §60.2:* $x_n = -1 \to -1$ and $y_n = (-1)^n/n^2 \to 0$ (since $|y_n| = 1/n^2 \to 0$), so
>
> $$
> \lim_{n\to\infty}\Big(-1 + i\,\frac{(-1)^n}{n^2}\Big) = \lim_{n\to\infty}(-1) + i\lim_{n\to\infty}\frac{(-1)^n}{n^2} = -1 + i \cdot 0 = -1 .
> $$
>
> *By Definition §60.1:* given $\varepsilon > 0$,
>
> $$
> |z_n - (-1)| = \Big|i\,\frac{(-1)^n}{n^2}\Big| = \frac{1}{n^2} < \varepsilon \qquad\text{whenever}\qquad n > \frac{1}{\sqrt\varepsilon} ,
> $$
>
> so any integer $n_0 \ge 1/\sqrt\varepsilon$ serves.
>
> **(b)** $\lim_{n\to\infty}\big(\frac{1}{n^2} + i\big) = i$ from the definition: $\big|\big(\frac{1}{n^2} + i\big) - i\big| = \frac{1}{n^2} < \varepsilon$ whenever $n > 1/\sqrt\varepsilon$. For instance, $\varepsilon = 10^{-4}$ needs $n > 100$, so $n_0 = 100$.
>
> *B&C: Sec. 60, Example 1; Sec. 61, Exercise 1*

^ex-60-1

> [!example] Example §60.2: Principal Arguments Need Not Converge
> Take the sequence of Example §60.1(a), $z_n = -1 + i(-1)^n/n^2$, which converges to $-1$, and write it in polar coordinates with $r_n = |z_n|$ and $\Theta_n = \operatorname{Arg} z_n$ $(-\pi < \Theta_n \le \pi)$.
>
> **The moduli converge**, as Proposition §60.3 guarantees:
>
> $$
> r_n = \sqrt{1 + \frac{1}{n^4}} \to 1 = |-1| .
> $$
>
> **The arguments do not.** For even $n$ the point $z_n$ lies just above the negative real axis (imaginary part $1/n^2 > 0$), and for odd $n$ just below it. So
>
> $$
> \Theta_{2n} = \pi - \arctan\frac{1}{(2n)^2} \to \pi, \qquad \Theta_{2n-1} = -\pi + \arctan\frac{1}{(2n-1)^2} \to -\pi ,
> $$
>
> and the sequence $\Theta_n$ has two different limit points: $\lim_{n\to\infty}\Theta_n$ does not exist. The reason is that $\operatorname{Arg} z$ jumps by $2\pi$ across the negative real axis, and the limit $-1$ lies on that axis. Theorem §60.2 is a statement about Cartesian coordinates; it has no analogue for $(r, \Theta)$ near the negative real axis.
>
> *B&C: Sec. 60, Example 2*

^ex-60-2

> [!example] Example §60.3: Principal Arguments That Do Converge
> Let $\Theta_n = \operatorname{Arg} z_n$ for
>
> $$
> z_n = 1 + i\,\frac{(-1)^n}{n^2} \qquad (n = 1, 2, \ldots) .
> $$
>
> Here $\operatorname{Re} z_n = 1 > 0$, so $z_n$ lies in the right half plane, where the principal argument is $\operatorname{Arg}(x + iy) = \arctan(y/x)$, a continuous function. Hence
>
> $$
> \Theta_n = \arctan\frac{(-1)^n}{n^2} \to \arctan 0 = 0 .
> $$
>
> The sequence again alternates between the upper and lower half planes, as in Example §60.2, but now its limit $1$ lies on the positive real axis, away from the jump of $\operatorname{Arg}$, and so $\lim_{n\to\infty}\Theta_n = 0 = \operatorname{Arg} 1$. In general: if $z_n \to z$ and $z$ is not on the ray $x \le 0$, $y = 0$, then $\operatorname{Arg} z_n \to \operatorname{Arg} z$, because $\operatorname{Arg}$ is continuous off that ray.
>
> *B&C: Sec. 61, Exercise 2*

^ex-60-3
