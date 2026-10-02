---
type: section
subject: "[[Complex Variables]]"
chapter: 5
section: 63
bc: "63"
aliases: ["B&C 63"]
tags: [complex-variables, math342]
---
← [[§62 Taylor Series]] · ↑ [[· 5 Series]] · [[§64 Examples (Proof of Taylor's Theorem)]] →

*Brown–Churchill, Section 63 · MAT 342 HW 9.*

This section proves Taylor's theorem, stated in [[§62 Taylor Series|§62]]. The proof needs no information about the derivatives of $f$ beyond what the Cauchy integral formula already gives. For $s$ on a circle around $z_0$, the Cauchy kernel $1/(s - z)$ is the sum of a geometric series in $z$, and this series converges uniformly in $s$ because $|z/s|$ stays below a fixed ratio $r/r_0 < 1$. Integrating term by term against $f(s)$ produces the Taylor coefficients by the extended Cauchy formula. The remainder is controlled by the ML-inequality. The case of a disk centered at the origin is done first, and the general case follows by a translation. Every later representation of an analytic function by a power series rests on this theorem: the residue theory of Chapter 6 and the zeros of analytic functions ([[§82 Zeros of Analytic Functions|§82]]) both start from it.

## Taylor's Theorem

> [!theorem] Theorem §63.1: Taylor's Theorem
> Suppose that a function $f$ is analytic throughout a disk $|z - z_0| < R_0$, centered at $z_0$ and with radius $R_0$. Then $f(z)$ has the power series representation
>
> $$
> f(z) = \sum_{n=0}^{\infty} a_n(z - z_0)^n \qquad (|z - z_0| < R_0), \qquad\text{where}\qquad a_n = \frac{f^{(n)}(z_0)}{n!} \quad (n = 0, 1, 2, \ldots) .
> $$
>
> That is, the Taylor series of $f$ about $z_0$ ([[§62 Taylor Series#^def-62-1|Definition §62.1]]) converges to $f(z)$ at every point of the open disk.
>
> *B&C: Sec. 62, Theorem (proved in Sec. 63)*

^thm-63-1

> [!remark] Remark: Why It Works
> Fix $z$ inside a circle $C_0$ centered at $0$ that lies in the disk. For $s$ on $C_0$,
>
> $$
> \frac{1}{s - z} = \frac1s\cdot\frac{1}{1 - z/s} = \sum_{n=0}^{\infty}\frac{z^n}{s^{n+1}} ,
> $$
>
> a geometric series with ratio $|z/s| = r/r_0 < 1$ that is the same for every $s$ on $C_0$. Feeding this into the Cauchy integral formula $f(z) = \frac{1}{2\pi i}\int_{C_0}\frac{f(s)}{s - z}\,ds$ and integrating term by term gives $\sum z^n\cdot\frac{1}{2\pi i}\int_{C_0}\frac{f(s)}{s^{n+1}}\,ds = \sum\frac{f^{(n)}(0)}{n!}z^n$. To avoid justifying the interchange of sum and integral, the proof stops the geometric series after $N$ terms, keeps the exact remainder, and shows that its integral tends to zero.

^rem-63-1

> [!proof]- Proof
> **The case $z_0 = 0$.** Here $f$ is analytic throughout $|z| < R_0$, and we must show
>
> $$
> f(z) = \sum_{n=0}^{\infty}\frac{f^{(n)}(0)}{n!}z^n \qquad (|z| < R_0) .
> $$
>
> Fix $z$ with $|z| = r < R_0$, choose $r_0$ with $r < r_0 < R_0$, and let $C_0$ be the positively oriented circle $|s| = r_0$. Since $f$ is analytic inside and on $C_0$ (the closed disk $|s| \le r_0$ lies in $|s| < R_0$) and $z$ is interior to $C_0$, the Cauchy integral formula ([[§54 Cauchy Integral Formula#^thm-54-1|Theorem §54.1]]) applies:
>
> $$
> f(z) = \frac{1}{2\pi i}\int_{C_0}\frac{f(s)\,ds}{s - z} . \qquad (1)
> $$
>
> *Expanding the kernel.* For $s$ on $C_0$,
>
> $$
> \frac{1}{s - z} = \frac1s\cdot\frac{1}{1 - (z/s)} . \qquad (2)
> $$
>
> By the finite geometric identity ([[§61 Convergence of Series#^ex-61-1|Example §61.1]], equation (11))
>
> $$
> \frac{1}{1 - w} = \sum_{n=0}^{N-1} w^n + \frac{w^N}{1 - w} \qquad (w \ne 1), \qquad (3)
> $$
>
> applied with $w = z/s$ (which is not $1$, since $|z/s| = r/r_0 < 1$), and after multiplication by $1/s$,
>
> $$
> \frac{1}{s - z} = \sum_{n=0}^{N-1}\frac{1}{s^{n+1}}z^n + z^N\frac{1}{(s - z)s^N} \qquad (N = 1, 2, \ldots) . \qquad (4)
> $$
>
> (The last term is $\frac1s\cdot\frac{(z/s)^N}{1 - z/s} = \frac{z^N}{s^N(s - z)}$.)
>
> *Integrating.* Multiply (4) by $f(s)$ and integrate each side around $C_0$. All the integrands are continuous on $C_0$, and the sum is finite, so the integral of the sum is the sum of the integrals ([[§44 Contour Integrals#^thm-44-2|Theorem §44.2]]):
>
> $$
> \int_{C_0}\frac{f(s)\,ds}{s - z} = \sum_{n=0}^{N-1}\Big(\int_{C_0}\frac{f(s)\,ds}{s^{n+1}}\Big)z^n + z^N\int_{C_0}\frac{f(s)\,ds}{(s - z)s^N} .
> $$
>
> By the extension of the Cauchy integral formula ([[§56★ Verification of the Extension (An Extension of the Cauchy Integral Formula)#^thm-56-1|Theorem §56.1]]), applied at the point $0$ interior to $C_0$,
>
> $$
> \frac{1}{2\pi i}\int_{C_0}\frac{f(s)\,ds}{s^{n+1}} = \frac{f^{(n)}(0)}{n!} \qquad (n = 0, 1, 2, \ldots) .
> $$
>
> Multiplying through by $1/(2\pi i)$ and using (1), we arrive at
>
> $$
> f(z) = \sum_{n=0}^{N-1}\frac{f^{(n)}(0)}{n!}z^n + \rho_N(z), \qquad (5)
> $$
>
> where
>
> $$
> \rho_N(z) = \frac{z^N}{2\pi i}\int_{C_0}\frac{f(s)\,ds}{(s - z)s^N} . \qquad (6)
> $$
>
> The sum in (5) is the partial sum $S_N(z)$ of the Maclaurin series (the first $N$ terms), so $\rho_N(z) = f(z) - S_N(z)$ is its remainder, and by [[§61 Convergence of Series#^def-61-3|Definition §61.3]] the series converges to $f(z)$ once we show
>
> $$
> \lim_{N\to\infty}\rho_N(z) = 0 . \qquad (7)
> $$
>
> *Estimating the remainder.* If $s$ is on $C_0$, then by the reverse triangle inequality
>
> $$
> |s - z| \ge \big||s| - |z|\big| = r_0 - r > 0 .
> $$
>
> The function $f$ is continuous on the circle $C_0$, a closed and bounded set, so $|f(s)|$ has a maximum value $M$ there ([[§18 Continuity#^thm-18-6|Theorem §18.6]]). On $C_0$ the integrand of (6) therefore satisfies
>
> $$
> \Big|\frac{f(s)}{(s - z)s^N}\Big| \le \frac{M}{(r_0 - r)r_0^N} ,
> $$
>
> and $C_0$ has length $2\pi r_0$. By the ML-inequality ([[§47 Upper Bounds for Moduli of Contour Integrals#^thm-47-2|Theorem §47.2]]),
>
> $$
> |\rho_N(z)| \le \frac{r^N}{2\pi}\cdot\frac{M}{(r_0 - r)r_0^N}\cdot 2\pi r_0 = \frac{Mr_0}{r_0 - r}\Big(\frac{r}{r_0}\Big)^N .
> $$
>
> The factor $Mr_0/(r_0 - r)$ does not depend on $N$, and $(r/r_0)^N \to 0$ because $0 \le r/r_0 < 1$. So limit (7) holds, and the case $z_0 = 0$ is proved.
>
> **The case $z_0 \ne 0$.** Suppose that $f$ is analytic when $|z - z_0| < R_0$, and let $g(z) = f(z + z_0)$. If $|z| < R_0$, then $|(z + z_0) - z_0| < R_0$, so $g$ is defined there, and it is analytic there as the composition of $f$ with the entire function $z + z_0$; by the chain rule ([[§20 Rules for Differentiation#^thm-20-4|Theorem §20.4]]) $g'(z) = f'(z + z_0)$, and by induction $g^{(n)}(z) = f^{(n)}(z + z_0)$, so
>
> $$
> g^{(n)}(0) = f^{(n)}(z_0) \qquad (n = 0, 1, 2, \ldots) .
> $$
>
> The analyticity of $g$ in the disk $|z| < R_0$ ensures, by the first case, a Maclaurin series representation
>
> $$
> g(z) = \sum_{n=0}^{\infty}\frac{g^{(n)}(0)}{n!}z^n \qquad (|z| < R_0), \qquad\text{that is,}\qquad f(z + z_0) = \sum_{n=0}^{\infty}\frac{f^{(n)}(z_0)}{n!}z^n \qquad (|z| < R_0) .
> $$
>
> Replacing $z$ by $z - z_0$ in this equation and in its condition of validity gives
>
> $$
> f(z) = \sum_{n=0}^{\infty}\frac{f^{(n)}(z_0)}{n!}(z - z_0)^n \qquad (|z - z_0| < R_0) ,
> $$
>
> which is the theorem.

^pf-63-1

*Uses:* [[§62 Taylor Series#^def-62-1|Def. §62.1]], [[§61 Convergence of Series#^ex-61-1|Ex. §61.1]], [[§61 Convergence of Series#^def-61-3|Def. §61.3]], [[§54 Cauchy Integral Formula#^thm-54-1|§54.1]] (Cauchy integral formula), [[§56★ Verification of the Extension (An Extension of the Cauchy Integral Formula)#^thm-56-1|§56.1]] (extended formula), [[§47 Upper Bounds for Moduli of Contour Integrals#^thm-47-2|§47.2]] (ML-inequality), [[§44 Contour Integrals#^thm-44-2|§44.2]] (linearity of contour integrals), [[§5 Triangle Inequality#^cor-5-2|§5.2]], [[§20 Rules for Differentiation#^thm-20-4|§20.4]] (chain rule), [[§18 Continuity#^thm-18-6|§18.6]] (maximum of a continuous function)

![[m342-63-1.svg]]
*The proof for $z_0 = 0$. The point $z$ ($|z| = r$) lies inside the circle $C_0$ of radius $r_0$, which lies inside the disk of analyticity $|z| < R_0$ (dashed). For every $s$ on $C_0$ the ratio $|z/s| = r/r_0$ is the same number less than $1$, which is why the geometric series for $1/(s - z)$ converges at the same rate everywhere on $C_0$.*

> [!remark]- Connections
> - In real analysis, convergence of a Taylor series to $f$ is proved from a remainder estimate that needs bounds on all derivatives ([[§31 Taylor's Theorem#^thm-31-2|451 Thm. §31.2]]), and it can fail for a function with derivatives of all orders ([[§31 Taylor's Theorem#^ex-31-3|451 Ex. §31.3]]). Here the Cauchy integral formula supplies the bounds automatically: Cauchy's inequality $|f^{(n)}(0)| \le n!M/r_0^n$ ([[§57 Some Consequences of the Extension#^thm-57-4|Theorem §57.4]]) gives $|a_nz^n| \le M(r/r_0)^n$, and summing the tail of this geometric bound from $n = N$ reproduces exactly the estimate $\frac{Mr_0}{r_0 - r}(r/r_0)^N$ of the proof.
> - The calculus statement "a power series equals the Taylor series of its sum" ([[§78 Taylor and Maclaurin Series#^thm-78-1|Calc Thm. §78.1]]) is the converse direction; in this subject it is [[§72★ Uniqueness of Series Representations#^thm-72-1|Theorem §72.1]].

## Examples

> [!example] Example §63.1: e^z About z = 1, by Derivatives and by Translation
> **Problem.** Obtain the Taylor series
>
> $$
> e^z = e\sum_{n=0}^{\infty}\frac{(z - 1)^n}{n!} \qquad (|z - 1| < \infty)
> $$
>
> **(a)** by using $f^{(n)}(1)$ $(n = 0, 1, 2, \ldots)$; **(b)** by writing $e^z = e^{z - 1}e$.
>
> **(a)** Since $\frac{d}{dz}e^z = e^z$, every derivative of $f(z) = e^z$ is $e^z$, so $f^{(n)}(1) = e$ and $a_n = e/n!$. The function is entire, so by Theorem §63.1 the series converges to $e^z$ for every $z$.
>
> **(b)** This is the second case of the proof. Let $g(w) = f(w + 1) = e^{w+1} = e\cdot e^w$. The Maclaurin series of $e^w$ ([[§64 Examples (Proof of Taylor's Theorem)#^prop-64-1|Proposition §64.1]]) gives $g(w) = e\sum_{n=0}^{\infty}w^n/n!$ for all $w$; putting $w = z - 1$,
>
> $$
> e^z = e\cdot e^{z - 1} = e\sum_{n=0}^{\infty}\frac{(z - 1)^n}{n!} \qquad (|z - 1| < \infty) .
> $$
>
> *B&C: Sec. 65, Exercise 2; Source: 342 HW 9*

^ex-63-1

> [!example] Example §63.2: The Disk Is Known Before the Series
> **Problem.** Find the Maclaurin series of $f(z) = \dfrac{z}{z^4 + 4}$ and the disk in which it represents $f$.
>
> **The disk first.** $f$ fails to be analytic only where $z^4 = -4 = 4e^{i\pi}$, that is, at the four fourth roots ([[§10 Roots of Complex Numbers|§10]])
>
> $$
> z = \sqrt2\,e^{i(\pi/4 + k\pi/2)} = \pm1 \pm i \qquad (k = 0, 1, 2, 3) ,
> $$
>
> all at distance $\sqrt2$ from the origin. By Theorem §63.1 the Maclaurin series converges to $f(z)$ in $|z| < \sqrt2$, whatever its coefficients turn out to be.
>
> **The series.** Write $f(z) = \dfrac z4\cdot\dfrac{1}{1 + (z^4/4)}$ and use the geometric series with $w = -z^4/4$, valid when $|z^4/4| < 1$, that is, $|z| < \sqrt2$:
>
> $$
> f(z) = \frac z4\sum_{n=0}^{\infty}\Big(-\frac{z^4}{4}\Big)^n = \sum_{n=0}^{\infty}\frac{(-1)^n}{2^{2n+2}}z^{4n+1} = \frac z4 - \frac{z^5}{16} + \frac{z^9}{64} - \cdots \qquad (|z| < \sqrt2) .
> $$
>
> The geometric series converges exactly in the disk predicted by Taylor's theorem. That this series is the Maclaurin series of $f$, and not merely some series converging to $f$, is [[§72★ Uniqueness of Series Representations#^thm-72-1|Theorem §72.1]]. (Checked with sympy.)
>
> *B&C: Sec. 65, Exercise 3*

^ex-63-2

> [!example] Example §63.3: The Remainder Estimate in Numbers
> Apply the estimate of the proof,
>
> $$
> |\rho_N(z)| \le \frac{Mr_0}{r_0 - r}\Big(\frac{r}{r_0}\Big)^N, \qquad M = \max_{|s| = r_0}|f(s)| ,
> $$
>
> to $f(z) = e^z$ at $z = 1$ ($r = 1$). Since $|e^s| = e^{\operatorname{Re}s} \le e^{r_0}$ on $|s| = r_0$, with equality at $s = r_0$, we have $M = e^{r_0}$, and $f$ is entire, so any $r_0 > 1$ is allowed:
>
> $$
> \Big|e - \sum_{n=0}^{N-1}\frac{1}{n!}\Big| \le \frac{r_0e^{r_0}}{r_0 - 1}\,r_0^{-N} .
> $$
>
> | $N$ | true remainder | bound, $r_0 = 2$ | bound, $r_0 = N$ |
> |---|---|---|---|
> | $5$ | $9.95\times10^{-3}$ | $0.462$ | $5.94\times10^{-2}$ |
> | $10$ | $3.03\times10^{-7}$ | $1.44\times10^{-2}$ | $2.45\times10^{-6}$ |
> | $15$ | $8.15\times10^{-13}$ | $4.51\times10^{-4}$ | $8.0\times10^{-12}$ |
>
> With a fixed $r_0$ the bound decays only geometrically, like $2^{-N}$, while the true remainder decays like $1/N!$. Because $f$ is entire, $r_0$ may grow with $N$; the choice $r_0 = N$ gives $\frac{N}{N - 1}e^NN^{-N}$, which by Stirling's formula is within a factor of order $\sqrt N$ of $1/N!$. For a function analytic only in $|z| < R_0$, the estimate gives the geometric rate $(r/r_0)^N$ for every $r_0 < R_0$, and no better.
>
> *B&C: Sec. 63 (text), remainder estimate; numerical illustration added in these notes*

^ex-63-3
