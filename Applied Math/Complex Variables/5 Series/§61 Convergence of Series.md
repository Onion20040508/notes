---
type: section
subject: "[[Complex Variables]]"
chapter: 5
section: 61
bc: "61"
aliases: ["B&C 61"]
tags: [complex-variables, math342]
---
← [[§60 Convergence of Sequences]] · ↑ [[· 5 Series]] · [[§62 Taylor Series]] →

*Brown–Churchill, Section 61 · MAT 342 HW 9 (optional reading).*

A series of complex numbers converges when its sequence of partial sums does, and by [[§60 Convergence of Sequences#^thm-60-2|Theorem §60.2]] this happens exactly when the real and imaginary parts converge separately. Familiar facts from calculus therefore carry over: the terms of a convergent series tend to zero, and absolute convergence implies convergence. The section also introduces the remainder $\rho_N = S - S_N$, the tool for every convergence proof in the chapter, and power series. Its one example, the geometric series $\sum z^n = 1/(1 - z)$ for $|z| < 1$, is the series from which the proofs of Taylor's and Laurent's theorems ([[§63 Proof of Taylor's Theorem#^thm-63-1|Theorem §63.1]], [[§67 Proof of Laurent's Theorem#^thm-67-1|Theorem §67.1]]) and most of the expansions in this chapter are built.

## Series and Their Sums

> [!definition] Definition §61.1: Convergent Series
> An infinite series
>
> $$
> \sum_{n=1}^{\infty} z_n = z_1 + z_2 + \cdots + z_n + \cdots \qquad (1)
> $$
>
> of complex numbers **converges to the sum** $S$ if the sequence of **partial sums**
>
> $$
> S_N = \sum_{n=1}^{N} z_n = z_1 + z_2 + \cdots + z_N \qquad (N = 1, 2, \ldots) \qquad (2)
> $$
>
> converges to $S$; we then write $\sum_{n=1}^{\infty} z_n = S$. A series that does not converge **diverges**.
>
> *B&C: Sec. 61 (text)*

^def-61-1

Since a sequence has at most one limit ([[§60 Convergence of Sequences#^prop-60-1|Proposition §60.1]]), a series has at most one sum.

> [!theorem] Theorem §61.1: Series by Real and Imaginary Parts
> Suppose that $z_n = x_n + iy_n$ $(n = 1, 2, \ldots)$ and $S = X + iY$. Then
>
> $$
> \sum_{n=1}^{\infty} z_n = S \qquad (3)
> $$
>
> if and only if
>
> $$
> \sum_{n=1}^{\infty} x_n = X \qquad\text{and}\qquad \sum_{n=1}^{\infty} y_n = Y . \qquad (4)
> $$
>
> *B&C: Sec. 61, Theorem*

^thm-61-1

> [!proof]+ Proof
> Write the partial sums (2) as
>
> $$
> S_N = X_N + iY_N, \qquad X_N = \sum_{n=1}^{N} x_n, \quad Y_N = \sum_{n=1}^{N} y_n . \qquad (5)
> $$
>
> Statement (3) is true if and only if $\lim_{N\to\infty} S_N = S$ (6). By (5) and [[§60 Convergence of Sequences#^thm-60-2|Theorem §60.2]], limit (6) holds if and only if
>
> $$
> \lim_{N\to\infty} X_N = X \qquad\text{and}\qquad \lim_{N\to\infty} Y_N = Y . \qquad (7)
> $$
>
> Since $X_N$ and $Y_N$ are the partial sums of the two series (4), the limits (7) say exactly that (4) holds.

^pf-61-1

*Uses:* [[§61 Convergence of Series#^def-61-1|Def. §61.1]], [[§60 Convergence of Sequences#^thm-60-2|§60.2]]

So one can write

$$
\sum_{n=1}^{\infty}(x_n + iy_n) = \sum_{n=1}^{\infty} x_n + i\sum_{n=1}^{\infty} y_n
$$

whenever the two series on the right converge or the one on the left does. The theorem is the bridge by which properties of real series carry over; here are the two that B&C needs.

> [!theorem] Corollary §61.2: The Terms of a Convergent Series Tend to Zero
> If a series of complex numbers converges, the $n$th term converges to zero as $n$ tends to infinity.
>
> *B&C: Sec. 61, Corollary 1*

^cor-61-2

> [!proof]+ Proof
> Let $\sum z_n$ converge, with $z_n = x_n + iy_n$. By [[§61 Convergence of Series#^thm-61-1|Theorem §61.1]] each of the real series
>
> $$
> \sum_{n=1}^{\infty} x_n \qquad\text{and}\qquad \sum_{n=1}^{\infty} y_n \qquad (8)
> $$
>
> converges. The $n$th term of a convergent series of real numbers tends to zero ([[§14 Series#^cor-14-2|451 Cor. §14.2]]), so by [[§60 Convergence of Sequences#^thm-60-2|Theorem §60.2]]
>
> $$
> \lim_{n\to\infty} z_n = \lim_{n\to\infty} x_n + i\lim_{n\to\infty} y_n = 0 + 0 \cdot i = 0 .
> $$

^pf-61-2

*Uses:* [[§61 Convergence of Series#^thm-61-1|§61.1]], [[§60 Convergence of Sequences#^thm-60-2|§60.2]], [[§14 Series#^cor-14-2|451 Cor. §14.2]]

It follows that the terms of a convergent series are bounded: a sequence converging to $0$ is bounded ([[§60 Convergence of Sequences#^prop-60-4|Proposition §60.4]]), so there is a positive constant $M$ with $|z_n| \le M$ for every $n$. This is the first step in the proof of [[§69★ Absolute and Uniform Convergence of Power Series#^thm-69-1|Theorem §69.1]].

> [!definition] Definition §61.2: Absolute Convergence
> The series (1) is **absolutely convergent** if the series
>
> $$
> \sum_{n=1}^{\infty}|z_n| = \sum_{n=1}^{\infty}\sqrt{x_n^2 + y_n^2} \qquad (z_n = x_n + iy_n)
> $$
>
> of real numbers converges.
>
> *B&C: Sec. 61 (text)*

^def-61-2

> [!theorem] Corollary §61.3: Absolute Convergence Implies Convergence
> The absolute convergence of a series of complex numbers implies the convergence of that series.
>
> *B&C: Sec. 61, Corollary 2*

^cor-61-3

> [!proof]+ Proof
> Assume that $\sum |z_n|$ converges. Since
>
> $$
> |x_n| \le \sqrt{x_n^2 + y_n^2} \qquad\text{and}\qquad |y_n| \le \sqrt{x_n^2 + y_n^2} ,
> $$
>
> the comparison test ([[§14 Series#^thm-14-7|451 Thm. §14.7]]) shows that $\sum |x_n|$ and $\sum |y_n|$ converge. An absolutely convergent series of real numbers converges ([[§14 Series#^prop-14-6|451 Prop. §14.6]]), so both series (8) converge, and by [[§61 Convergence of Series#^thm-61-1|Theorem §61.1]] the series (1) converges.

^pf-61-3

*Uses:* [[§61 Convergence of Series#^def-61-2|Def. §61.2]], [[§61 Convergence of Series#^thm-61-1|§61.1]], [[§14 Series#^thm-14-7|451 Thm. §14.7]], [[§14 Series#^prop-14-6|451 Prop. §14.6]]

> [!remark]- Connections
> - The real versions: [[§14 Series#^def-14-2|451 Def. §14.2]] (convergence of a series), [[§14 Series#^cor-14-2|451 Cor. §14.2]], [[§14 Series#^def-14-4|451 Def. §14.4]] and [[§14 Series#^prop-14-6|451 Prop. §14.6]]. In 451 the last is proved with the Cauchy criterion, [[§14 Series#^thm-14-1|451 Thm. §14.1]]; that proof works verbatim in $\mathbb{C}$, because $\mathbb{C}$ is complete and $\big|\sum_{n=N}^{m} z_n\big| \le \sum_{n=N}^{m}|z_n|$.

The algebra of convergent series is inherited the same way; B&C leaves it to the exercises, and it is used whenever two expansions are added, as in [[§64 Examples (Proof of Taylor's Theorem)|§64]] and [[§68 Examples (Proof of Laurent's Theorem)|§68]].

> [!theorem] Proposition §61.4: Sums, Constant Multiples and Conjugates of Series
> If $\sum_{n=1}^{\infty} z_n = S$ and $\sum_{n=1}^{\infty} w_n = T$, and $c$ is any complex number, then
>
> $$
> \sum_{n=1}^{\infty}(z_n + w_n) = S + T, \qquad \sum_{n=1}^{\infty} c\,z_n = cS, \qquad \sum_{n=1}^{\infty}\bar z_n = \bar S .
> $$
>
> *B&C: Sec. 61, Exercises 6, 7 and 8*

^prop-61-4

> [!proof]+ Proof
> Let $S_N$ and $T_N$ be the partial sums. The partial sums of the three new series are $S_N + T_N$, $cS_N$ and $\bar S_N$.
>
> **Sum.** (Exercise 8, by real series.) Write $z_n = x_n + iy_n$, $w_n = u_n + iv_n$, $S = X + iY$, $T = U + iV$. By Theorem §61.1, $\sum x_n = X$, $\sum y_n = Y$, $\sum u_n = U$, $\sum v_n = V$; the sum of two convergent real series converges to the sum of the sums ([[§14 Series#^prop-14-3|451 Prop. §14.3]]), so $\sum(x_n + u_n) = X + U$ and $\sum(y_n + v_n) = Y + V$, and Theorem §61.1 again gives $\sum(z_n + w_n) = (X + U) + i(Y + V) = S + T$.
>
> **Constant multiple.** $|cS_N - cS| = |c|\,|S_N - S|$. If $c = 0$ there is nothing to prove; otherwise, given $\varepsilon > 0$, choose $N_0$ with $|S_N - S| < \varepsilon/|c|$ for $N > N_0$.
>
> **Conjugate.** $|\bar S_N - \bar S| = |\overline{S_N - S}| = |S_N - S|$, so $\bar S_N \to \bar S$ with the same $N_0$ for each $\varepsilon$.

^pf-61-4

*Uses:* [[§61 Convergence of Series#^thm-61-1|§61.1]], [[§14 Series#^prop-14-3|451 Prop. §14.3]], [[§6 Complex Conjugates#^def-6-1|Def. §6.1]] ($|\bar z| = |z|$)

## Remainders and Power Series

> [!definition] Definition §61.3: Remainder; Power Series
> **(a)** If a series converges to $S$ and $S_N$ are its partial sums (2), the **remainder after $N$ terms** is
>
> $$
> \rho_N = S - S_N . \qquad (9)
> $$
>
> Thus $S = S_N + \rho_N$, and since $|S_N - S| = |\rho_N - 0|$, **a series converges to $S$ if and only if its sequence of remainders tends to zero.**
>
> **(b)** A **power series** is a series of the form
>
> $$
> \sum_{n=0}^{\infty} a_n(z - z_0)^n = a_0 + a_1(z - z_0) + a_2(z - z_0)^2 + \cdots + a_n(z - z_0)^n + \cdots ,
> $$
>
> where $z_0$ and the coefficients $a_n$ are complex constants and $z$ may be any point in a stated region containing $z_0$. For series involving a variable $z$, the sum, partial sums and remainders are written $S(z)$, $S_N(z)$ and $\rho_N(z)$.
>
> *B&C: Sec. 61 (text)*

^def-61-3

For a power series indexed from $n = 0$, B&C takes $S_N(z)$ to be the sum of the first $N$ terms, $S_N(z) = \sum_{n=0}^{N-1} a_n(z - z_0)^n$; this keeps $\rho_N(z) = S(z) - S_N(z)$ the tail starting with the term of degree $N$.

> [!example] Example §61.1: The Geometric Series
> **Claim.**
>
> $$
> \sum_{n=0}^{\infty} z^n = \frac{1}{1 - z} \qquad\text{whenever}\qquad |z| < 1 , \qquad (10)
> $$
>
> and the series diverges when $|z| \ge 1$.
>
> **Partial sums.** Recall the identity
>
> $$
> 1 + z + z^2 + \cdots + z^n = \frac{1 - z^{n+1}}{1 - z} \qquad (z \ne 1) ,
> $$
>
> which follows by multiplying the left side by $1 - z$ and telescoping. So the partial sums are
>
> $$
> S_N(z) = \sum_{n=0}^{N-1} z^n = 1 + z + \cdots + z^{N-1} = \frac{1 - z^N}{1 - z} \qquad (z \ne 1) .
> $$
>
> **Remainders.** With $S(z) = 1/(1 - z)$,
>
> $$
> \rho_N(z) = S(z) - S_N(z) = \frac{z^N}{1 - z}, \qquad |\rho_N(z)| = \frac{|z|^N}{|1 - z|} \qquad (z \ne 1) .
> $$
>
> If $|z| < 1$, then $|z|^N \to 0$, so $\rho_N(z) \to 0$, and (10) holds by Definition §61.3(a).
>
> **Divergence for $|z| \ge 1$.** Then $|z^n| = |z|^n \ge 1$, so the terms do not tend to zero and the series diverges by Corollary §61.2. (B&C reads this off from $|\rho_N(z)| = |z|^N/|1 - z| \not\to 0$; that shows that the series does not converge *to* $1/(1 - z)$, and the term test shows that it converges to nothing else either, including at $z = 1$, where $S_N = N$.)
>
> Two by-products are used constantly: the finite identity
>
> $$
> \frac{1}{1 - z} = \sum_{n=0}^{N-1} z^n + \frac{z^N}{1 - z} \qquad (z \ne 1) , \qquad (11)
> $$
>
> which is the starting point of the proofs of [[§63 Proof of Taylor's Theorem#^pf-63-1|Theorem §63.1]] and [[§67 Proof of Laurent's Theorem#^pf-67-1|Theorem §67.1]], and the fact that the convergence in (10) is absolute ($\sum|z|^n$ is a real geometric series).
>
> *B&C: Sec. 61, Example*

^ex-61-1

> [!remark]- Connections
> - The real geometric series and its uses in 451: [[Geometric series]]; the convergence statement is [[§14 Series#^ex-14-4|451 Ex. §14.4]], and [[§70 Series#^thm-70-1|Calc Thm. §70.1]] is the calculus version.

> [!example] Example §61.2: Two Real Series from the Geometric Series
> **Claim.** For $0 \le r < 1$ and all real $\theta$,
>
> $$
> \sum_{n=1}^{\infty} r^n\cos n\theta = \frac{r\cos\theta - r^2}{1 - 2r\cos\theta + r^2}, \qquad \sum_{n=1}^{\infty} r^n\sin n\theta = \frac{r\sin\theta}{1 - 2r\cos\theta + r^2} .
> $$
>
> **Proof.** Put $z = re^{i\theta}$ in (10); then $|z| = r < 1$ and, by de Moivre ([[§8 Products and Powers in Exponential Form#^cor-8-3|Corollary §8.3]]), $z^n = r^ne^{in\theta}$. Subtracting the $n = 0$ term,
>
> $$
> \sum_{n=1}^{\infty} r^ne^{in\theta} = \frac{1}{1 - z} - 1 = \frac{z}{1 - z} = \frac{z(1 - \bar z)}{|1 - z|^2} = \frac{re^{i\theta} - r^2}{1 - 2r\cos\theta + r^2} ,
> $$
>
> using $z\bar z = r^2$ and $|1 - z|^2 = (1 - r\cos\theta)^2 + r^2\sin^2\theta = 1 - 2r\cos\theta + r^2$ (which is positive, since $z \ne 1$). The left side is $\sum r^n\cos n\theta + i\sum r^n\sin n\theta$, so by Theorem §61.1 the two real series converge to the real and imaginary parts of the right side, which are the two formulas. At $r = 0$ both sides are $0$.
>
> **Check.** $r = 0.6$, $\theta = 1.1$: the cosine sum is $-0.107692$ and the sine sum $0.655553$, by direct summation and by the formulas.
>
> Doubling the first formula and adding $1$ gives $1 + 2\sum_{n \ge 1} r^n\cos n\theta = \dfrac{1 - r^2}{1 - 2r\cos\theta + r^2}$, the [[§134★ Poisson Integral Formula#^def-134-2|Poisson kernel]] of the unit disk ([[§39 Potential in a Disk#^thm-39-3|341 Thm. §39.3]], step (e) of the proof).
>
> *B&C: Sec. 61, Exercise 4; Source: 342 HW 9 (optional exercises, p. 185)*

^ex-61-2

> [!example] Example §61.3: Convergent but Not Absolutely Convergent
> The converse of Corollary §61.3 is false. Consider
>
> $$
> \sum_{n=1}^{\infty}\frac{i^n}{n} = i - \frac12 - \frac i3 + \frac14 + \frac i5 - \frac16 - \cdots .
> $$
>
> **Not absolutely convergent:** $\sum |i^n/n| = \sum 1/n$ is the harmonic series, which diverges.
>
> **Convergent:** the terms with even $n = 2k$ are real, $(-1)^k/(2k)$, and those with odd $n = 2k + 1$ are imaginary, $i(-1)^k/(2k + 1)$. So $x_n$ and $y_n$ are the alternating series
>
> $$
> \sum_{n=1}^{\infty} x_n = \sum_{k=1}^{\infty}\frac{(-1)^k}{2k} = -\frac12\ln 2, \qquad \sum_{n=1}^{\infty} y_n = \sum_{k=0}^{\infty}\frac{(-1)^k}{2k + 1} = \frac\pi4 ,
> $$
>
> each convergent by the alternating series test ([[§15 Alternating Series and Integral Tests#^thm-15-1|451 Thm. §15.1]]; the values are $-\frac12$ times the alternating harmonic series and Leibniz's series). By Theorem §61.1 the series converges, to $-\frac12\ln 2 + i\frac\pi4 \approx -0.346574 + 0.785398\,i$ (confirmed by direct summation). This value is $-\operatorname{Log}(1 - i) = -\big(\ln\sqrt2 - i\frac\pi4\big)$: the point $z = 1 - i$ lies on the circle of convergence of the logarithm series of [[§71★ Integration and Differentiation of Power Series#^ex-71-4|Example §71.4]], so that example does not prove it, but the numbers agree.
>
> *Source: illustration of B&C Sec. 61 added in these notes (not in B&C)*

^ex-61-3
