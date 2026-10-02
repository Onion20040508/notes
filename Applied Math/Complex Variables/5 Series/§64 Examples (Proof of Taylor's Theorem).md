---
type: section
subject: "[[Complex Variables]]"
chapter: 5
section: 64
bc: "64"
aliases: ["B&C 64"]
tags: [complex-variables, math342]
---
← [[§63 Proof of Taylor's Theorem]] · ↑ [[· 5 Series]] · [[§65 Negative Powers of (z − z₀)]] →

*Brown–Churchill, Section 64 · MAT 342 HW 9 · Practice Final (Spring 2005).*

This section collects the six Maclaurin series that the rest of the course uses constantly: the geometric series, $e^z$, $\sin z$, $\cos z$, $\sinh z$ and $\cosh z$. It also shows how to obtain new Taylor series from them by substitution, multiplication by powers, shifting the center, and identities, without computing a single derivative. That these shortcuts produce *the* Taylor series is guaranteed by uniqueness ([[§72★ Uniqueness of Series Representations#^thm-72-1|Theorem §72.1]]): if $f(z) = \sum a_n(z - z_0)^n$ for all $z$ in some disk about $z_0$, then $a_n = f^{(n)}(z_0)/n!$, however the $a_n$ were found. Conversely, the coefficients of a known series give the derivatives of $f$ at $z_0$ without differentiating.

## Six Maclaurin Series

> [!theorem] Proposition §64.1: Six Maclaurin Series
>
> $$
> \begin{aligned}
> \frac{1}{1 - z} &= \sum_{n=0}^{\infty} z^n = 1 + z + z^2 + \cdots && (|z| < 1), && (1) \\
> e^z &= \sum_{n=0}^{\infty}\frac{z^n}{n!} = 1 + \frac{z}{1!} + \frac{z^2}{2!} + \cdots && (|z| < \infty), && (2) \\
> \sin z &= \sum_{n=0}^{\infty}(-1)^n\frac{z^{2n+1}}{(2n + 1)!} = z - \frac{z^3}{3!} + \frac{z^5}{5!} - \cdots && (|z| < \infty), && (3) \\
> \cos z &= \sum_{n=0}^{\infty}(-1)^n\frac{z^{2n}}{(2n)!} = 1 - \frac{z^2}{2!} + \frac{z^4}{4!} - \cdots && (|z| < \infty), && (4) \\
> \sinh z &= \sum_{n=0}^{\infty}\frac{z^{2n+1}}{(2n + 1)!} = z + \frac{z^3}{3!} + \frac{z^5}{5!} + \cdots && (|z| < \infty), && (5) \\
> \cosh z &= \sum_{n=0}^{\infty}\frac{z^{2n}}{(2n)!} = 1 + \frac{z^2}{2!} + \frac{z^4}{4!} + \cdots && (|z| < \infty). && (6)
> \end{aligned}
> $$
>
> *B&C: Sec. 64, expansions (1)–(6) and Examples 1–6*

^prop-64-1

> [!proof]+ Proof
> **(1)** (B&C's Example 1; the series was already summed directly in [[§61 Convergence of Series#^ex-61-1|Example §61.1]].) The only singular point of $f(z) = 1/(1 - z)$ in the finite plane is $z = 1$, so by Taylor's theorem ([[§63 Proof of Taylor's Theorem#^thm-63-1|Theorem §63.1]]) its Maclaurin series converges to $f(z)$ when $|z| < 1$. By induction, $f^{(n)}(z) = n!/(1 - z)^{n+1}$ (the step: $\frac{d}{dz}\,n!(1 - z)^{-n-1} = (n + 1)!(1 - z)^{-n-2}$), so $f^{(n)}(0) = n!$ for $n = 0, 1, 2, \ldots$, and $a_n = 1$.
>
> **(2)** (Example 2.) $f(z) = e^z$ is entire, $f^{(n)}(z) = e^z$, and $f^{(n)}(0) = 1$, so $a_n = 1/n!$ and the series converges to $e^z$ for every $z$.
>
> **(3)** (Example 3.) Use the definition $\sin z = (e^{iz} - e^{-iz})/(2i)$ ([[§37 The Trigonometric Functions sin z and cos z|§37]]) and expansion (2) with $z$ replaced by $iz$ and by $-iz$. By [[§61 Convergence of Series#^prop-61-4|Proposition §61.4]] the two series may be subtracted term by term:
>
> $$
> \sin z = \frac{1}{2i}\Big(\sum_{n=0}^{\infty}\frac{(iz)^n}{n!} - \sum_{n=0}^{\infty}\frac{(-iz)^n}{n!}\Big) = \frac{1}{2i}\sum_{n=0}^{\infty}\big(1 - (-1)^n\big)\frac{i^nz^n}{n!} \qquad (|z| < \infty) .
> $$
>
> But $1 - (-1)^n = 0$ when $n$ is even, and deleting zero terms from a convergent series does not change its sum (the new partial sums are a subsequence of the old ones). So we can replace $n$ by $2n + 1$:
>
> $$
> \sin z = \frac{1}{2i}\sum_{n=0}^{\infty}\big(1 - (-1)^{2n+1}\big)\frac{i^{2n+1}z^{2n+1}}{(2n + 1)!} .
> $$
>
> Inasmuch as $1 - (-1)^{2n+1} = 2$ and $i^{2n+1} = (i^2)^ni = (-1)^ni$, this reduces to (3). *(B&C writes "we refer to expansion (1)" here; the expansion used is (2).)*
>
> **(4)** (Example 4.) Differentiate (3) term by term, which is justified by [[§71★ Integration and Differentiation of Power Series#^thm-71-4|Theorem §71.4]], at every $z$ (the circle of convergence of (3) is infinite):
>
> $$
> \cos z = \sum_{n=0}^{\infty}\frac{(-1)^n}{(2n + 1)!}\frac{d}{dz}z^{2n+1} = \sum_{n=0}^{\infty}(-1)^n\frac{2n + 1}{(2n + 1)!}z^{2n} = \sum_{n=0}^{\infty}(-1)^n\frac{z^{2n}}{(2n)!} \qquad (|z| < \infty) .
> $$
>
> ([[§64 Examples (Proof of Taylor's Theorem)#^ex-64-4|Example §64.4]] obtains (4) from the exponential series instead, without term-by-term differentiation.)
>
> **(5)** (Example 5.) Since $\sinh z = -i\sin(iz)$ ([[§39★ Hyperbolic Functions|§39]]), replace $z$ by $iz$ in (3) and multiply by $-i$:
>
> $$
> \sinh z = -i\sum_{n=0}^{\infty}(-1)^n\frac{(iz)^{2n+1}}{(2n + 1)!} = \sum_{n=0}^{\infty}\frac{z^{2n+1}}{(2n + 1)!} \qquad (|z| < \infty) ,
> $$
>
> because $(iz)^{2n+1} = (-1)^niz^{2n+1}$ and $-i\cdot(-1)^n\cdot(-1)^ni = 1$.
>
> **(6)** (Example 6.) Since $\cosh z = \cos(iz)$ ([[§39★ Hyperbolic Functions|§39]]), replace $z$ by $iz$ in (4): $(iz)^{2n} = (-1)^nz^{2n}$, so
>
> $$
> \cosh z = \sum_{n=0}^{\infty}(-1)^n\frac{(iz)^{2n}}{(2n)!} = \sum_{n=0}^{\infty}\frac{z^{2n}}{(2n)!} \qquad (|z| < \infty) .
> $$

^pf-64-1

*Uses:* [[§63 Proof of Taylor's Theorem#^thm-63-1|§63.1]], [[§61 Convergence of Series#^ex-61-1|Ex. §61.1]], [[§61 Convergence of Series#^prop-61-4|§61.4]], [[§71★ Integration and Differentiation of Power Series#^thm-71-4|§71.4]], [[§37 The Trigonometric Functions sin z and cos z|§37]] (definitions of sin, cos), [[§39★ Hyperbolic Functions|§39]] (sinh, cosh), [[§30 The Exponential Function|§30]] ($\frac{d}{dz}e^z = e^z$)

> [!remark]- Connections
> - With $z = x$ real these are the calculus series [[§78 Taylor and Maclaurin Series#^thm-78-6|Calc Thm. §78.6]] ($e^x$), [[§78 Taylor and Maclaurin Series#^thm-78-7|Calc Thm. §78.7]] ($\sin x$) and [[§78 Taylor and Maclaurin Series#^thm-78-8|Calc Thm. §78.8]] ($\cos x$), proved there with Taylor's inequality; here analyticity makes the remainder estimate unnecessary. The rigorous real-variable construction of $\sin$ and $\cos$ from their series is [[§26 Differentiation and Integration of Power Series#^ex-26-8|451 Ex. §26.8]].

Two observations apply to every example below:
**(a)** the region of convergence can be determined before the series is found ([[§62 Taylor Series#^rem-62-1|Remark: Where the Taylor Series Converges to f]]);
**(b)** there are usually several reasonable ways to find the series.

> [!remark] Remark: Method — Taylor Series from Known Series
> To expand $f$ about $z_0$:
> 1. **Find the disk.** Locate the points where $f$ is not analytic; the series will converge to $f$ in $|z - z_0| < R$, where $R$ is the distance from $z_0$ to the nearest of them ($R = \infty$ for an entire function).
> 2. **Rewrite $f$ in terms of $z - z_0$.** Typical moves: $\dfrac{1}{a - z} = \dfrac{1}{(a - z_0) - (z - z_0)} = \dfrac{1}{a - z_0}\cdot\dfrac{1}{1 - \frac{z - z_0}{a - z_0}}$; $e^z = e^{z_0}e^{z - z_0}$; addition formulas and periodicity for trigonometric and hyperbolic functions.
> 3. **Substitute into one of (1)–(6)**, multiply by powers or constants, and add series term by term ([[§61 Convergence of Series#^prop-61-4|Proposition §61.4]]). Carry the condition of validity through each substitution; for the geometric series, $|w| < 1$ becomes $|z - z_0| < |a - z_0|$, which should reproduce the disk of step 1.
> 4. **Reindex** so that the general term is $c_n(z - z_0)^n$ if a standard form is wanted.
> 5. **Read off derivatives if needed:** $f^{(n)}(z_0) = n!\,a_n$ ([[§72★ Uniqueness of Series Representations#^thm-72-1|Theorem §72.1]]).

^rem-64-1

## Examples

> [!example] Example §64.1: Series Obtained from the Geometric Series
> **(a) $1/(1 + z)$.** Substitute $-z$ for $z$ in (1); since $|-z| < 1$ exactly when $|z| < 1$,
>
> $$
> \frac{1}{1 + z} = \sum_{n=0}^{\infty}(-1)^nz^n \qquad (|z| < 1) .
> $$
>
> **(b) $1/z$ about $z_0 = 1$.** Replace $z$ by $1 - z$ in (1); the condition $|1 - z| < 1$ is the same as $|z - 1| < 1$:
>
> $$
> \frac1z = \sum_{n=0}^{\infty}(-1)^n(z - 1)^n \qquad (|z - 1| < 1) .
> $$
>
> The disk reaches the singular point $0$, as it must.
>
> **(c) $1/(1 - z)$ about $z_0 = i$.** The distance from $z_0 = i$ to the singularity $z = 1$ is $|1 - i| = \sqrt2$, so the condition of validity will be $|z - i| < \sqrt2$. To get powers of $z - i$, write
>
> $$
> \frac{1}{1 - z} = \frac{1}{(1 - i) - (z - i)} = \frac{1}{1 - i}\cdot\frac{1}{1 - \frac{z - i}{1 - i}} .
> $$
>
> Because $\big|\frac{z - i}{1 - i}\big| = \frac{|z - i|}{\sqrt2} < 1$ when $|z - i| < \sqrt2$, expansion (1) gives
>
> $$
> \frac{1}{1 - z} = \frac{1}{1 - i}\sum_{n=0}^{\infty}\Big(\frac{z - i}{1 - i}\Big)^n = \sum_{n=0}^{\infty}\frac{(z - i)^n}{(1 - i)^{n+1}} \qquad (|z - i| < \sqrt2) .
> $$
>
> The first coefficients are $\frac{1}{1 - i} = \frac{1 + i}{2}$, $\frac{1}{(1 - i)^2} = \frac i2$, $\frac{1}{(1 - i)^3} = \frac{-1 + i}{4}$ (checked against $f^{(n)}(i)/n! = 1/(1 - i)^{n+1}$ with sympy).
>
> *B&C: Sec. 64, Example 1*

^ex-64-1

> [!example] Example §64.2: Substitution, Multiplication by a Power, and Periodicity
> **(a) $z^3e^{2z}$.** This entire function has a Maclaurin series valid for all $z$. Replace $z$ by $2z$ in (2) and multiply through by $z^3$:
>
> $$
> z^3e^{2z} = \sum_{n=0}^{\infty}\frac{2^n}{n!}z^{n+3} \qquad (|z| < \infty) ,
> $$
>
> and, replacing $n$ by $n - 3$,
>
> $$
> z^3e^{2z} = \sum_{n=3}^{\infty}\frac{2^{n-3}}{(n - 3)!}z^n = z^3 + 2z^4 + 2z^5 + \frac43z^6 + \cdots \qquad (|z| < \infty) .
> $$
>
> In particular $\frac{d^5}{dz^5}\big(z^3e^{2z}\big)\big|_{z=0} = 5!\cdot2 = 240$.
>
> **(b) $\cosh z$ about $z_0 = -2\pi i$.** Replace $z$ by $z + 2\pi i$ in (6) and recall that $\cosh z$ has period $2\pi i$ ([[§39★ Hyperbolic Functions|§39]]), so $\cosh(z + 2\pi i) = \cosh z$:
>
> $$
> \cosh z = \sum_{n=0}^{\infty}\frac{(z + 2\pi i)^{2n}}{(2n)!} \qquad (|z| < \infty) .
> $$
>
> *B&C: Sec. 64, Examples 2 and 6*

^ex-64-2

> [!example] Example §64.3: sin z About π/2, in Two Ways
> **Problem.** Find the Taylor series of $\sin z$ about $z_0 = \pi/2$ **(a)** by computing derivatives and **(b)** by using $\sin z = \cos(\frac\pi2 - z)$ and the series for $\cos z$. For what $z$ does it converge? **(c)** Similarly expand $\cos z$ about $\pi/2$, using $\cos z = -\sin(z - \frac\pi2)$.
>
> **(a)** By [[§62 Taylor Series#^ex-62-1|Example §62.1]], $\sin^{(2n)}z = (-1)^n\sin z$ and $\sin^{(2n+1)}z = (-1)^n\cos z$. At $\pi/2$, where $\sin = 1$ and $\cos = 0$:
>
> $$
> \sin^{(2n)}\big(\tfrac\pi2\big) = (-1)^n, \qquad \sin^{(2n+1)}\big(\tfrac\pi2\big) = 0, \qquad\text{so}\qquad \sin z = \sum_{n=0}^{\infty}\frac{(-1)^n}{(2n)!}\Big(z - \frac\pi2\Big)^{2n} .
> $$
>
> **(b)** Replace $z$ by $\frac\pi2 - z$ in (4). Since the exponent $2n$ is even, $\big(\frac\pi2 - z\big)^{2n} = \big(z - \frac\pi2\big)^{2n}$, and
>
> $$
> \sin z = \cos\Big(\frac\pi2 - z\Big) = \sum_{n=0}^{\infty}(-1)^n\frac{(z - \pi/2)^{2n}}{(2n)!} = 1 - \frac{(z - \pi/2)^2}{2!} + \frac{(z - \pi/2)^4}{4!} - \cdots ,
> $$
>
> the same series. **Convergence:** $\sin z$ is entire, so the series converges to $\sin z$ for all $z$ (and (4) converges for every value of its argument).
>
> **(c)** Replace $z$ by $z - \frac\pi2$ in (3):
>
> $$
> \cos z = -\sin\Big(z - \frac\pi2\Big) = -\sum_{n=0}^{\infty}(-1)^n\frac{(z - \pi/2)^{2n+1}}{(2n + 1)!} = \sum_{n=0}^{\infty}\frac{(-1)^{n+1}}{(2n + 1)!}\Big(z - \frac\pi2\Big)^{2n+1} \qquad (|z| < \infty) .
> $$
>
> *B&C: Sec. 65, Exercise 4 (part (c)); Source: 342 HW 9, Problem 1*

^ex-64-3

> [!example] Example §64.4: cos z from the Exponential Series
> **Problem.** Rederive the Maclaurin series (4) for $\cos z$ from the definition $\cos z = (e^{iz} + e^{-iz})/2$ and the series (2) for $e^z$.
>
> Replace $z$ by $iz$ and by $-iz$ in (2) and add term by term ([[§61 Convergence of Series#^prop-61-4|Proposition §61.4]]):
>
> $$
> \cos z = \frac12\sum_{n=0}^{\infty}\frac{(iz)^n + (-iz)^n}{n!} = \frac12\sum_{n=0}^{\infty}\big(1 + (-1)^n\big)\frac{i^nz^n}{n!} \qquad (|z| < \infty) .
> $$
>
> For odd $n$, $1 + (-1)^n = 0$; for $n = 2k$, $1 + (-1)^{2k} = 2$ and $i^{2k} = (i^2)^k = (-1)^k$. Deleting the zero terms,
>
> $$
> \cos z = \frac12\sum_{k=0}^{\infty}2(-1)^k\frac{z^{2k}}{(2k)!} = \sum_{k=0}^{\infty}(-1)^k\frac{z^{2k}}{(2k)!} \qquad (|z| < \infty) .
> $$
>
> *B&C: Sec. 65, Exercise 8(a); Source: 342 HW 9*

^ex-64-4

> [!example] Example §64.5: Reading Derivatives from the Coefficients
> **(a) $\sin(z^2)$.** Replace $z$ by $z^2$ in (3):
>
> $$
> \sin(z^2) = \sum_{n=0}^{\infty}(-1)^n\frac{z^{4n+2}}{(2n + 1)!} = z^2 - \frac{z^6}{3!} + \frac{z^{10}}{5!} - \cdots \qquad (|z| < \infty) .
> $$
>
> This series converges to $f(z) = \sin(z^2)$ for all $z$, so it is the Maclaurin series of $f$ ([[§72★ Uniqueness of Series Representations#^thm-72-1|Theorem §72.1]]), and $f^{(k)}(0) = k!\,a_k$. Only the powers $z^k$ with $k = 4n + 2$ occur. Since $4n$ is never of the form $4m + 2$, the coefficient of $z^{4n}$ is $0$, so $f^{(4n)}(0) = 0$; since every exponent $4n + 2$ is even, the coefficient of each odd power is $0$, so $f^{(2n+1)}(0) = 0$ $(n = 0, 1, 2, \ldots)$.
>
> **(b) $\tan^{(5)}(0)$ with as little calculation as possible**, given that the Taylor series of $\tan z$ centered at $0$ has the form
>
> $$
> \tan z = z + \frac13z^3 + \frac{2}{15}z^5 + \cdots \quad\text{(terms of order at least seven)} .
> $$
>
> The coefficient of $z^5$ is $\tan^{(5)}(0)/5!$, so
>
> $$
> \tan^{(5)}(0) = 5!\cdot\frac{2}{15} = \frac{240}{15} = 16 .
> $$
>
> (Direct differentiation confirms $16$. The series converges to $\tan z$ in $|z| < \pi/2$, the distance to the nearest zeros $\pm\pi/2$ of $\cos z$.)
>
> *B&C: Sec. 65, Exercise 9; Source: 342 HW 9 (part (a)); 342 practice final (Spring 2005), Q1(a) (part (b))*

^ex-64-5
