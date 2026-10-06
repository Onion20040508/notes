---
type: section
subject: "[[Complex Variables]]"
chapter: 5
section: 69
bc: "69"
aliases: ["B&C 69"]
tags: [complex-variables, math342, extension]
---
← [[§68 Examples (Proof of Laurent's Theorem)]] · ↑ [[· 5 Series]] · [[§70★ Continuity of Sums of Power Series]] →

*Brown–Churchill, Section 69.*
★ *Beyond MAT 342: the course skipped this section or left it optional; it is included from Brown–Churchill.*

Sections 69–72 develop the general theory of power series that the Taylor and Laurent sections used without proof: where a power series converges, that its sum is continuous and analytic, that it may be integrated and differentiated term by term, and that its coefficients are determined by its sum. This section supplies the two convergence facts everything else rests on. **Theorem §69.1:** convergence at one point $z_1$ forces absolute convergence at every point closer to the center, so the set of convergence is a disk, bounded by the *circle of convergence*. **Theorem §69.3:** inside that circle the convergence is uniform on every smaller closed disk. The proofs compare the series with a convergent geometric series or with a convergent series of constants, which is the Weierstrass M-test in disguise.

## Absolute Convergence

> [!theorem] Theorem §69.1: Convergence at a Point Implies Absolute Convergence Closer In
> If a power series
>
> $$
> \sum_{n=0}^{\infty}a_n(z - z_0)^n \qquad (1)
> $$
>
> converges when $z = z_1$ $(z_1 \ne z_0)$, then it is absolutely convergent at each point $z$ in the open disk $|z - z_0| < R_1$, where $R_1 = |z_1 - z_0|$.
>
> *B&C: Sec. 69, Theorem 1*

^thm-69-1

> [!proof]+ Proof
> Assume that $\sum_{n=0}^{\infty}a_n(z_1 - z_0)^n$ converges. Its terms tend to zero ([[§61 Convergence of Series#^cor-61-2|Corollary §61.2]]) and are therefore bounded ([[§60 Convergence of Sequences#^prop-60-4|Proposition §60.4]]): there is a positive constant $M$ with
>
> $$
> |a_n(z_1 - z_0)^n| \le M \qquad (n = 0, 1, 2, \ldots) .
> $$
>
> If $|z - z_0| < R_1$, write
>
> $$
> \rho = \frac{|z - z_0|}{|z_1 - z_0|} < 1 .
> $$
>
> Then
>
> $$
> |a_n(z - z_0)^n| = |a_n(z_1 - z_0)^n|\Big(\frac{|z - z_0|}{|z_1 - z_0|}\Big)^n \le M\rho^n \qquad (n = 0, 1, 2, \ldots) .
> $$
>
> The series $\sum_{n=0}^{\infty}M\rho^n$ is a geometric series, which converges since $\rho < 1$. By the comparison test for series of real numbers, $\sum_{n=0}^{\infty}|a_n(z - z_0)^n|$ converges.

^pf-69-1

*Uses:* [[§61 Convergence of Series#^cor-61-2|§61.2]], [[§60 Convergence of Sequences#^prop-60-4|§60.4]], [[§61 Convergence of Series#^def-61-2|Def. §61.2]], [[§14 Series#^thm-14-7|451 Thm. §14.7]] (comparison test)

So the set of points inside some circle centered at $z_0$ is a region of convergence of (1), provided the series converges at some point other than $z_0$.

> [!definition] Definition §69.1: Circle of Convergence
> The **circle of convergence** of the power series (1) is the greatest circle $|z - z_0| = R$ centered at $z_0$ such that the series converges at each point inside it. Explicitly, $R$ is the supremum of the distances $|z - z_0|$ over all points $z$ at which (1) converges. If (1) converges at every point, $R = \infty$ and the series converges in the whole plane; if it converges only at $z_0$, there is no circle of convergence ($R = 0$).
>
> *B&C: Sec. 69 (text)*

^def-69-1

(B&C speaks of "the greatest circle" without saying why one exists; the supremum is the precise version, and the next corollary shows that it is the greatest circle.)

> [!theorem] Corollary §69.2: Convergence Inside, Divergence Outside
> Let (1) have circle of convergence $|z - z_0| = R$. Then (1) converges absolutely at every point $z$ with $|z - z_0| < R$, and it diverges at every point $z_2$ with $|z_2 - z_0| > R$.
>
> *B&C: Sec. 69 (text)*

^cor-69-2

> [!proof]+ Proof
> **Inside.** Let $|z - z_0| < R$. Since $R$ is a supremum, there is a point $z_1$ at which (1) converges with $|z - z_0| < |z_1 - z_0| \le R$. By [[§69★ Absolute and Uniform Convergence of Power Series#^thm-69-1|Theorem §69.1]], (1) converges absolutely at $z$.
>
> **Outside.** If (1) converged at a point $z_2$ with $|z_2 - z_0| > R$, then $|z_2 - z_0|$ would be one of the distances whose supremum is $R$, which is impossible. (B&C phrases this as: by Theorem §69.1 the series would converge everywhere inside the circle through $z_2$, and the first circle could not be the circle of convergence.)

^pf-69-2

*Uses:* [[§69★ Absolute and Uniform Convergence of Power Series#^thm-69-1|§69.1]], [[§69★ Absolute and Uniform Convergence of Power Series#^def-69-1|Def. §69.1]]

On the circle of convergence itself the theorem says nothing; [[§69★ Absolute and Uniform Convergence of Power Series#^ex-69-2|Example §69.2]] shows that anything can happen there.

> [!remark]- Connections
> - The real version, for intervals instead of disks: [[§23 Power Series#^thm-23-1|451 Thm. §23.1]] (trichotomy) and [[§23 Power Series#^thm-23-2|451 Thm. §23.2]], which also gives a formula for the radius, $1/R = \limsup|a_n|^{1/n}$ (the Cauchy–Hadamard formula; B&C does not use it). Its proof applies to complex series without change, since the root test only involves $|a_n(z - z_0)^n|$. The calculus statement "convergence spreads inward, divergence outward" is [[§76 Power Series#^lem-76-1|Calc Lem. §76.1]].

## Uniform Convergence

Suppose that the power series (1) has circle of convergence $|z - z_0| = R$, and let

$$
S(z) = \sum_{n=0}^{\infty}a_n(z - z_0)^n, \qquad S_N(z) = \sum_{n=0}^{N-1}a_n(z - z_0)^n \qquad (|z - z_0| < R)
$$

be its sum and partial sums, with remainder

$$
\rho_N(z) = S(z) - S_N(z) \qquad (|z - z_0| < R) . \qquad (2)
$$

For each fixed $z$ in the disk, $\rho_N(z) \to 0$: for each $\varepsilon > 0$ there is a positive integer $N_\varepsilon$ such that

$$
|\rho_N(z)| < \varepsilon \qquad\text{whenever}\qquad N > N_\varepsilon . \qquad (3)
$$

In general $N_\varepsilon$ depends on $z$ as well as on $\varepsilon$.

> [!definition] Definition §69.2: Uniform Convergence
> The power series (1) **converges uniformly** in a region within its circle of convergence if, for each $\varepsilon > 0$, the integer $N_\varepsilon$ in (3) can be chosen depending only on $\varepsilon$ and not on the point $z$ of the region: $|\rho_N(z)| < \varepsilon$ for all $N > N_\varepsilon$ and all $z$ in the region.
>
> *B&C: Sec. 69 (text)*

^def-69-2

> [!theorem] Theorem §69.3: Uniform Convergence on Smaller Closed Disks
> If $z_1$ is a point inside the circle of convergence $|z - z_0| = R$ of a power series
>
> $$
> \sum_{n=0}^{\infty}a_n(z - z_0)^n , \qquad (4)
> $$
>
> then that series is uniformly convergent in the closed disk $|z - z_0| \le R_1$, where $R_1 = |z_1 - z_0|$.
>
> *B&C: Sec. 69, Theorem 2*

^thm-69-3

> [!proof]+ Proof
> Since $z_1$ lies inside the circle of convergence, there are points inside that circle and farther from $z_0$ than $z_1$ at which the series converges ([[§69★ Absolute and Uniform Convergence of Power Series#^cor-69-2|Corollary §69.2]]). So, by [[§69★ Absolute and Uniform Convergence of Power Series#^thm-69-1|Theorem §69.1]],
>
> $$
> \sum_{n=0}^{\infty}|a_n(z_1 - z_0)^n| \qquad (5)
> $$
>
> converges. Letting $m$ and $N$ denote positive integers with $m > N$, write the remainders of the series (4) and (5) as
>
> $$
> \rho_N(z) = \lim_{m\to\infty}\sum_{n=N}^{m}a_n(z - z_0)^n \qquad (6) \qquad\text{and}\qquad \sigma_N = \lim_{m\to\infty}\sum_{n=N}^{m}|a_n(z_1 - z_0)^n| , \qquad (7)
> $$
>
> respectively. (These are the remainders after $N$ terms: $\sum_{n=N}^{m} = S_{m+1} - S_N$, which tends to $S - S_N$.) By [[§60 Convergence of Sequences#^prop-60-3|Proposition §60.3]], the moduli converge to the modulus of the limit:
>
> $$
> |\rho_N(z)| = \lim_{m\to\infty}\Big|\sum_{n=N}^{m}a_n(z - z_0)^n\Big| ;
> $$
>
> and when $|z - z_0| \le |z_1 - z_0|$, the triangle inequality gives
>
> $$
> \Big|\sum_{n=N}^{m}a_n(z - z_0)^n\Big| \le \sum_{n=N}^{m}|a_n||z - z_0|^n \le \sum_{n=N}^{m}|a_n||z_1 - z_0|^n = \sum_{n=N}^{m}|a_n(z_1 - z_0)^n| .
> $$
>
> Letting $m \to \infty$ (limits preserve non-strict inequalities),
>
> $$
> |\rho_N(z)| \le \sigma_N \qquad\text{when}\qquad |z - z_0| \le R_1 . \qquad (8)
> $$
>
> Since the $\sigma_N$ are the remainders of a convergent series, they tend to zero as $N$ tends to infinity: for each $\varepsilon > 0$ an integer $N_\varepsilon$ exists such that
>
> $$
> \sigma_N < \varepsilon \qquad\text{whenever}\qquad N > N_\varepsilon . \qquad (9)
> $$
>
> Because of (8) and (9), condition (3) holds for all points $z$ in the disk $|z - z_0| \le R_1$, with a value of $N_\varepsilon$ that does not depend on $z$. Hence the convergence of (4) is uniform in that disk.

^pf-69-3

*Uses:* [[§69★ Absolute and Uniform Convergence of Power Series#^thm-69-1|§69.1]], [[§69★ Absolute and Uniform Convergence of Power Series#^cor-69-2|§69.2]], [[§69★ Absolute and Uniform Convergence of Power Series#^def-69-2|Def. §69.2]], [[§60 Convergence of Sequences#^prop-60-3|§60.3]], [[§61 Convergence of Series#^def-61-3|Def. §61.3]], [[§5 Triangle Inequality#^cor-5-3|§5.3]], [[§9 Limit Theorems for Sequences#^prop-9-5|451 Prop. §9.5]] (limits preserve weak inequalities)

![[m342-69-1.svg]]
*Theorems §69.1 and §69.3. The series converges absolutely at every point $z$ inside the circle of convergence $|z - z_0| = R$ (blue) and diverges at every point $z_2$ outside it. For any point $z_1$ inside, the convergence is uniform on the closed disk $|z - z_0| \le |z_1 - z_0|$ (green), because there every term is dominated by the corresponding term of the convergent series $\sum|a_n(z_1 - z_0)^n|$.*

> [!remark]- Connections
> - The proof is the Weierstrass M-test, [[§25 More on Uniform Convergence#^thm-25-3|451 Thm. §25.3]], with the constants $M_n = |a_n(z_1 - z_0)^n|$; Definition §69.2 is the remainder form of [[§24 Uniform Convergence#^def-24-2|451 Def. §24.2]] applied to the partial sums. The real counterpart of the theorem is [[§26 Differentiation and Integration of Power Series#^thm-26-1|451 Thm. §26.1]].

## Examples

> [!example] Example §69.1: The Geometric Series Is Uniform Only Away from the Circle
> For $\sum_{n=0}^{\infty}z^n$, [[§61 Convergence of Series#^ex-61-1|Example §61.1]] shows convergence for $|z| < 1$ and divergence for $|z| \ge 1$, so the circle of convergence is $|z| = 1$, and the remainder is $\rho_N(z) = z^N/(1 - z)$.
>
> **Uniform on $|z| \le R_1$ for each $R_1 < 1$.** There $|1 - z| \ge 1 - |z| \ge 1 - R_1$, so
>
> $$
> |\rho_N(z)| \le \frac{R_1^N}{1 - R_1} = \sigma_N ,
> $$
>
> which is exactly the remainder of $\sum|z_1|^n$ at $|z_1| = R_1$ used in the proof of Theorem §69.3. Given $\varepsilon$, one $N_\varepsilon$ serves for the whole closed disk.
>
> **Not uniform on the open disk $|z| < 1$.** Fix any $N$. For real $z = x$ with $0 < x < 1$, $\rho_N(x) = x^N/(1 - x) \to \infty$ as $x \to 1^-$. So for $\varepsilon = 1$ no single $N_\varepsilon$ works for all $z$ in $|z| < 1$. Theorem §69.3 cannot be improved to the whole open disk.
>
> *Source: illustration of B&C Sec. 69 added in these notes (not in B&C)*

^ex-69-1

> [!example] Example §69.2: Behavior on the Circle of Convergence
> Each of the following series has circle of convergence $|z| = 1$: each converges for $|z| < 1$ (compare with the geometric series), and for $|z| > 1$ its terms do not tend to zero (since $|z|^n/n^2 \to \infty$ when $|z| > 1$).
> - $\sum_{n=0}^{\infty}z^n$ **diverges at every point** of $|z| = 1$: the terms have modulus $1$.
> - $\sum_{n=1}^{\infty}\dfrac{z^n}{n^2}$ **converges absolutely at every point** of $|z| \le 1$, by comparison with $\sum 1/n^2$. It even converges uniformly on the closed disk $|z| \le 1$, since $|\rho_N(z)| \le \sum_{n \ge N}1/n^2$ there; this goes beyond Theorem §69.3, whose disks stay inside the circle.
> - $\sum_{n=1}^{\infty}\dfrac{z^n}{n}$ **converges at some points of the circle and diverges at others**: at $z = 1$ it is the harmonic series, which diverges; at $z = -1$ it is the alternating harmonic series, which converges (but not absolutely); at $z = i$ it is the series of [[§61 Convergence of Series#^ex-61-3|Example §61.3]], which converges to $-\frac12\ln 2 + i\frac\pi4$.
>
> So the circle of convergence separates convergence from divergence only off the circle; on it, each series must be examined separately.
>
> *Source: illustration of B&C Sec. 69 added in these notes (not in B&C)*

^ex-69-2

> [!example] Example §69.3: The Two Extreme Cases
> **$\sum_{n=0}^{\infty}n!\,z^n$ converges only at $z = 0$.** For $z \ne 0$ the ratio of consecutive terms is $(n + 1)|z| \to \infty$, so $|n!\,z^n| \to \infty$ and the series diverges by [[§61 Convergence of Series#^cor-61-2|Corollary §61.2]]. Theorem §69.1 never applies, and the series has no circle of convergence. Such a series represents no function at all; by [[§63 Proof of Taylor's Theorem#^thm-63-1|Taylor's theorem]] it is not the Taylor series of any function analytic at $0$.
>
> **$\sum_{n=0}^{\infty}z^n/n!$ converges at every point.** Here $R = \infty$ ([[§64 Examples (Proof of Taylor's Theorem)#^prop-64-1|Proposition §64.1]], the series of $e^z$), and Theorem §69.3, applied with $z_1$ of any modulus, gives uniform convergence on every closed disk $|z| \le R_1$. The convergence is not uniform on the whole plane: for real $z = x > 0$ the remainder $\rho_N(x) \ge x^N/N!$ is unbounded in $x$.
>
> *Source: illustration of B&C Sec. 69 added in these notes (not in B&C)*

^ex-69-3
