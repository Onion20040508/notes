---
type: section
subject: "[[Complex Variables]]"
chapter: 5
section: 70
bc: "70"
aliases: ["B&C 70"]
tags: [complex-variables, math342, extension]
---
← [[§69★ Absolute and Uniform Convergence of Power Series]] · ↑ [[· 5 Series]] · [[§71★ Integration and Differentiation of Power Series]] →

*Brown–Churchill, Section 70.*
★ *Beyond MAT 342: the course skipped this section or left it optional; it is included from Brown–Churchill.*

The first consequence of uniform convergence is that the sum of a power series is a continuous function inside its circle of convergence. Each partial sum is a polynomial, hence continuous, and a uniformly small remainder cannot destroy continuity; the proof is the "$\varepsilon/3$ argument". The substitution $w = 1/(z - z_0)$ carries the results of [[§69★ Absolute and Uniform Convergence of Power Series|§69]] and this section over to series in negative powers of $z - z_0$, and so to both halves of a Laurent series. Continuity is the hypothesis of Morera's theorem, which [[§71★ Integration and Differentiation of Power Series|§71]] uses to upgrade "continuous" to "analytic".

> [!theorem] Theorem §70.1: The Sum of a Power Series Is Continuous
> A power series
>
> $$
> \sum_{n=0}^{\infty}a_n(z - z_0)^n \qquad (1)
> $$
>
> represents a continuous function $S(z)$ at each point inside its circle of convergence $|z - z_0| = R$. That is, if $z_1$ is a point inside that circle, then for each positive number $\varepsilon$ there is a positive number $\delta$ such that
>
> $$
> |S(z) - S(z_1)| < \varepsilon \qquad\text{whenever}\qquad |z - z_1| < \delta , \qquad (2)
> $$
>
> where $\delta$ is small enough that $z$ lies in the domain of definition $|z - z_0| < R$ of $S(z)$.
>
> *B&C: Sec. 70, Theorem*

^thm-70-1

> [!proof]+ Proof
> Let $S_N(z)$ denote the sum of the first $N$ terms of (1) and $\rho_N(z) = S(z) - S_N(z)$ $(|z - z_0| < R)$ the remainder. Since $S(z) = S_N(z) + \rho_N(z)$,
>
> $$
> |S(z) - S(z_1)| = |S_N(z) - S_N(z_1) + \rho_N(z) - \rho_N(z_1)| \le |S_N(z) - S_N(z_1)| + |\rho_N(z)| + |\rho_N(z_1)| . \qquad (3)
> $$
>
> Choose $R_0$ with $|z_1 - z_0| < R_0 < R$, and let $\varepsilon > 0$. The circle $|z - z_0| = R_0$ contains points inside the circle of convergence at distance $R_0$ from $z_0$, so by [[§69★ Absolute and Uniform Convergence of Power Series#^thm-69-3|Theorem §69.3]] the series converges uniformly in the closed disk $|z - z_0| \le R_0$: there is a positive integer $N_\varepsilon$ such that
>
> $$
> |\rho_N(z)| < \frac\varepsilon3 \qquad\text{whenever}\qquad N > N_\varepsilon \qquad (4)
> $$
>
> for every $z$ in that disk, in particular for $z = z_1$ and for every $z$ in a neighborhood $|z - z_1| < \delta_1$ small enough to be contained in the disk (any $\delta_1 \le R_0 - |z_1 - z_0|$ will do).
>
> Now fix $N = N_\varepsilon + 1$. The partial sum $S_N(z)$ is a polynomial and is therefore continuous at $z_1$ ([[§18 Continuity|§18]]), so there is $\delta$ with $0 < \delta \le \delta_1$ such that
>
> $$
> |S_N(z) - S_N(z_1)| < \frac\varepsilon3 \qquad\text{whenever}\qquad |z - z_1| < \delta . \qquad (5)
> $$
>
> With $N = N_\varepsilon + 1$, both (4) (at $z$ and at $z_1$) and (5) hold, and (3) gives
>
> $$
> |S(z) - S(z_1)| < \frac\varepsilon3 + \frac\varepsilon3 + \frac\varepsilon3 = \varepsilon \qquad\text{whenever}\qquad |z - z_1| < \delta .
> $$
>
> This is statement (2).

^pf-70-1

*Uses:* [[§69★ Absolute and Uniform Convergence of Power Series#^thm-69-3|§69.3]], [[§61 Convergence of Series#^def-61-3|Def. §61.3]], [[§18 Continuity|§18]] (polynomials are continuous)

> [!remark]- Connections
> - This is the special case for power series of "a uniform limit of continuous functions is continuous", [[§24 Uniform Convergence#^thm-24-2|451 Thm. §24.2]] and [[§25 More on Uniform Convergence#^thm-25-2|451 Thm. §25.2]]; the real power-series version is [[§26 Differentiation and Integration of Power Series#^cor-26-2|451 Cor. §26.2]]. The $\varepsilon/3$ argument above is the same proof, with the uniformity supplied by Theorem §69.3 on a slightly larger closed disk.

## Series in Negative Powers

By writing $w = 1/(z - z_0)$, one can modify the two theorems of §69 and the theorem here so that they apply to series of the type

$$
\sum_{n=1}^{\infty}\frac{b_n}{(z - z_0)^n} . \qquad (6)
$$

> [!theorem] Corollary §70.2: Series in Negative Powers
> If series (6) converges at a point $z_1$ $(z_1 \ne z_0)$, then it converges absolutely, to a continuous function, in the domain exterior to the circle $|z - z_0| = R_1$, where $R_1 = |z_1 - z_0|$.
>
> *B&C: Sec. 70 (text)*

^cor-70-2

> [!proof]+ Proof
> Put $w = 1/(z - z_0)$, so that (6) becomes the power series $\sum_{n=1}^{\infty}b_nw^n$ in $w$ (with constant term $0$). It converges at $w_1 = 1/(z_1 - z_0)$, so by [[§69★ Absolute and Uniform Convergence of Power Series#^thm-69-1|Theorem §69.1]] it converges absolutely when
>
> $$
> |w| < \frac{1}{|z_1 - z_0|} , \qquad (7)
> $$
>
> and its circle of convergence has radius at least $1/R_1$, so by [[§70★ Continuity of Sums of Power Series#^thm-70-1|Theorem §70.1]] its sum $T(w)$ is continuous in the disk (7). Inequality (7) is the same as $|z - z_0| > |z_1 - z_0|$. In that domain the sum of (6) is $T\big(1/(z - z_0)\big)$, the composition of $T$ with the continuous function $1/(z - z_0)$, hence continuous ([[§18 Continuity|§18]]).

^pf-70-2

*Uses:* [[§69★ Absolute and Uniform Convergence of Power Series#^thm-69-1|§69.1]], [[§70★ Continuity of Sums of Power Series#^thm-70-1|§70.1]], [[§18 Continuity|§18]] (composition of continuous functions)

B&C goes on to state, without separate proof, that both halves of a Laurent series converge uniformly away from the edges of their annulus. Here is the statement and why it holds.

> [!theorem] Corollary §70.3: Uniform Convergence of Laurent Series
> If a Laurent series representation
>
> $$
> f(z) = \sum_{n=0}^{\infty}a_n(z - z_0)^n + \sum_{n=1}^{\infty}\frac{b_n}{(z - z_0)^n}
> $$
>
> is valid in an annulus $R_1 < |z - z_0| < R_2$, then both of the series on the right converge uniformly in any closed annulus $r_1 \le |z - z_0| \le r_2$ with $R_1 < r_1 \le r_2 < R_2$.
>
> *B&C: Sec. 70 (text)*

^cor-70-3

> [!proof]+ Proof
> **The nonnegative powers.** The power series $\sum a_n(z - z_0)^n$ converges at every point of the annulus, so at points at distance arbitrarily close to $R_2$ from $z_0$; hence its circle of convergence has radius at least $R_2$ ([[§69★ Absolute and Uniform Convergence of Power Series#^def-69-1|Definition §69.1]]). A point $z_1$ with $|z_1 - z_0| = r_2 < R_2$ is inside it, so by [[§69★ Absolute and Uniform Convergence of Power Series#^thm-69-3|Theorem §69.3]] the series converges uniformly on the closed disk $|z - z_0| \le r_2$, which contains the closed annulus.
>
> **The negative powers.** With $w = 1/(z - z_0)$, the series $\sum b_nw^n$ converges whenever $1/R_2 < |w| < 1/R_1$, so its circle of convergence has radius at least $1/R_1$. By Theorem §69.3 it converges uniformly on $|w| \le 1/r_1$: for each $\varepsilon$ there is $N_\varepsilon$ such that its remainders satisfy $|\tau_N(w)| < \varepsilon$ for $N > N_\varepsilon$ and all $|w| \le 1/r_1$. The remainders of $\sum b_n/(z - z_0)^n$ are $\tau_N\big(1/(z - z_0)\big)$, and $|z - z_0| \ge r_1$ exactly when $|1/(z - z_0)| \le 1/r_1$. So the same $N_\varepsilon$ works for all $z$ with $|z - z_0| \ge r_1$, in particular on the closed annulus.

^pf-70-3

*Uses:* [[§69★ Absolute and Uniform Convergence of Power Series#^def-69-1|Def. §69.1]], [[§69★ Absolute and Uniform Convergence of Power Series#^thm-69-3|§69.3]], [[§69★ Absolute and Uniform Convergence of Power Series#^def-69-2|Def. §69.2]]

This uniformity is what allows a Laurent series to be integrated term by term along a contour in its annulus ([[§72★ Uniqueness of Series Representations#^lem-72-3|Lemma §72.3]]).

## Examples

> [!example] Example §70.1: A Limit from Continuity of a Sum
> **Claim.** $\displaystyle\lim_{z\to0}\frac{e^z - 1}{z} = 1$.
>
> By the Maclaurin series of $e^z$ ([[§64 Examples (Proof of Taylor's Theorem)#^prop-64-1|Proposition §64.1]]), for $z \ne 0$
>
> $$
> \frac{e^z - 1}{z} = \frac1z\sum_{n=1}^{\infty}\frac{z^n}{n!} = \sum_{n=1}^{\infty}\frac{z^{n-1}}{n!} = \sum_{n=0}^{\infty}\frac{z^n}{(n + 1)!} .
> $$
>
> The last series converges for every $z$ (it is dominated by the series of $e^{|z|}$), so its circle of convergence is infinite, and by Theorem §70.1 its sum $S(z)$ is continuous everywhere. Since $S(z) = (e^z - 1)/z$ for $z \ne 0$ and $S(0) = 1$,
>
> $$
> \lim_{z\to0}\frac{e^z - 1}{z} = \lim_{z\to0}S(z) = S(0) = 1 .
> $$
>
> (This is also the derivative of $e^z$ at $0$; the point is that continuity of a power series gives such limits without differentiating. [[§71★ Integration and Differentiation of Power Series#^ex-71-1|Example §71.1]] goes further and shows that such a function is entire.)
>
> *Source: illustration of B&C Sec. 70 added in these notes (not in B&C)*

^ex-70-1

> [!example] Example §70.2: Negative Powers Converge Outside a Circle
> **(a)** $\sum_{n=1}^{\infty}z^{-n}$ converges at $z_1 = 2$ (a geometric series with ratio $\frac12$), so by Corollary §70.2 it converges absolutely, to a continuous function, in $|z| > 2$. In fact it converges in $|z| > 1$, to $\frac{1/z}{1 - 1/z} = \frac{1}{z - 1}$: the corollary gives the exterior of the circle through any point of convergence, and the best such circle is $|z| = 1$.
>
> **(b)** $e^{1/z} - 1 = \sum_{n=1}^{\infty}\frac{1}{n!\,z^n}$ converges at every $z_1 \ne 0$ ([[§68 Examples (Proof of Laurent's Theorem)#^ex-68-4|Example §68.4]]), so it converges absolutely in $|z| > |z_1|$ for every such $z_1$, that is, in the whole punctured plane $0 < |z| < \infty$, and its sum is continuous there, as it must be.
>
> *Source: illustration of B&C Sec. 70 added in these notes (not in B&C)*

^ex-70-2

> [!example] Example §70.3: Uniform on Closed Sub-Annuli, Not on the Annulus
> In $1 < |z| < 2$ the Laurent series of [[§67 Proof of Laurent's Theorem#^ex-67-1|Example §67.1]] is
>
> $$
> \frac{-1}{(z - 1)(z - 2)} = \sum_{n=0}^{\infty}\frac{z^n}{2^{n+1}} + \sum_{n=1}^{\infty}\frac{1}{z^n} .
> $$
>
> On the closed annulus $1.1 \le |z| \le 1.9$ the remainders after $N$ terms satisfy
>
> $$
> \Big|\sum_{n=N}^{\infty}\frac{z^n}{2^{n+1}}\Big| \le \frac12\sum_{n=N}^{\infty}(0.95)^n = 10\,(0.95)^N, \qquad \Big|\sum_{n=N+1}^{\infty}\frac{1}{z^n}\Big| \le \sum_{n=N+1}^{\infty}\Big(\frac{1}{1.1}\Big)^n = 10\,\Big(\frac{1}{1.1}\Big)^N ,
> $$
>
> bounds independent of $z$ that tend to $0$: the convergence is uniform there, as Corollary §70.3 asserts. On the whole open annulus it is not: for real $z = x$ with $1 < x < 2$, the second remainder is $\sum_{n > N}x^{-n} = \frac{x^{-N}}{x - 1}$, which tends to $\infty$ as $x \to 1^+$ for each fixed $N$.
>
> *Source: illustration of B&C Sec. 70 added in these notes (not in B&C)*

^ex-70-3
