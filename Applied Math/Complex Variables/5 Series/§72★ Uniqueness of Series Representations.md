---
type: section
subject: "[[Complex Variables]]"
chapter: 5
section: 72
bc: "72"
aliases: ["B&C 72"]
tags: [complex-variables, math342, extension]
---
← [[§71★ Integration and Differentiation of Power Series]] · ↑ [[· 5 Series]] · [[§73★ Multiplication and Division of Power Series]] →

*Brown–Churchill, Section 72 · MAT 342 HW 10.*
★ *Beyond MAT 342: the course skipped this section or left it optional; it is included from Brown–Churchill.*

A function has only one series representation of each kind. If $\sum a_n(z - z_0)^n$ converges to $f(z)$ in some disk about $z_0$, it is the Taylor series of $f$. If a series in positive and negative powers converges to $f(z)$ in an annulus about $z_0$, it is the Laurent series of $f$ for that annulus. Both proofs integrate the series term by term against $(z - z_0)^{-n-1}$; the integral of $(z - z_0)^{m-n-1}$ around a circle kills every term except $m = n$. Uniqueness is what justifies every shortcut of [[§64 Examples (Proof of Taylor's Theorem)|§64]], [[§65 Negative Powers of (z − z₀)|§65]], [[§67 Proof of Laurent's Theorem|§67]] and [[§68 Examples (Proof of Laurent's Theorem)|§68]]: however a series was obtained, it is *the* series. The course used this throughout HW 9 and HW 10 without proof.

## Uniqueness of Taylor Series

> [!theorem] Theorem §72.1: Uniqueness of Taylor Series
> If a series
>
> $$
> \sum_{n=0}^{\infty}a_n(z - z_0)^n \qquad (1)
> $$
>
> converges to $f(z)$ at all points interior to some circle $|z - z_0| = R$, then it is the Taylor series expansion for $f$ in powers of $z - z_0$; that is, $a_n = f^{(n)}(z_0)/n!$ for $n = 0, 1, 2, \ldots$
>
> *B&C: Sec. 72, Theorem 1*

^thm-72-1

> [!proof]+ Proof
> Write the representation
>
> $$
> f(z) = \sum_{n=0}^{\infty}a_n(z - z_0)^n \qquad (|z - z_0| < R) \qquad (2)
> $$
>
> with the index of summation $m$: $f(z) = \sum_{m=0}^{\infty}a_m(z - z_0)^m$. The series converges at every point of $|z - z_0| < R$, so its circle of convergence has radius at least $R$, and $f$, its sum, is analytic in the disk ([[§71★ Integration and Differentiation of Power Series#^cor-71-2|Corollary §71.2]]). Let $C$ be a positively oriented circle centered at $z_0$ with radius less than $R$, and fix $n \ge 0$. By [[§71★ Integration and Differentiation of Power Series#^thm-71-1|Theorem §71.1]],
>
> $$
> \int_C g(z)f(z)\,dz = \sum_{m=0}^{\infty}a_m\int_C g(z)(z - z_0)^m\,dz , \qquad (3)
> $$
>
> where $g(z)$ is the function
>
> $$
> g(z) = \frac{1}{2\pi i}\cdot\frac{1}{(z - z_0)^{n+1}} , \qquad (4)
> $$
>
> continuous on $C$. By the extension of the Cauchy integral formula ([[§56★ Verification of the Extension (An Extension of the Cauchy Integral Formula)#^thm-56-1|Theorem §56.1]]),
>
> $$
> \int_C g(z)f(z)\,dz = \frac{1}{2\pi i}\int_C\frac{f(z)\,dz}{(z - z_0)^{n+1}} = \frac{f^{(n)}(z_0)}{n!} ; \qquad (5)
> $$
>
> and since ([[§45 Some Examples (Contour Integrals)#^ex-45-5|Example §45.5]])
>
> $$
> \int_C g(z)(z - z_0)^m\,dz = \frac{1}{2\pi i}\int_C\frac{dz}{(z - z_0)^{n-m+1}} = \begin{cases} 0 & \text{when } m \ne n, \\ 1 & \text{when } m = n, \end{cases} \qquad (6)
> $$
>
> every term of the series on the right of (3) vanishes except the one with $m = n$:
>
> $$
> \sum_{m=0}^{\infty}a_m\int_C g(z)(z - z_0)^m\,dz = a_n . \qquad (7)
> $$
>
> Because of (5) and (7), equation (3) reduces to $\dfrac{f^{(n)}(z_0)}{n!} = a_n$. So series (2) is the Taylor series of $f$ about $z_0$.

^pf-72-1

*Uses:* [[§71★ Integration and Differentiation of Power Series#^thm-71-1|§71.1]], [[§71★ Integration and Differentiation of Power Series#^cor-71-2|§71.2]], [[§56★ Verification of the Extension (An Extension of the Cauchy Integral Formula)#^thm-56-1|§56.1]], [[§45 Some Examples (Contour Integrals)#^ex-45-5|Ex. §45.5]] ($\int_C(z - z_0)^k\,dz$)

> [!theorem] Corollary §72.2: A Power Series That Vanishes Near z₀ Is Zero
> If the series (1) converges to zero throughout some neighborhood of $z_0$, then the coefficients $a_n$ are all zero. Consequently, two power series in $z - z_0$ that converge to the same function in a neighborhood of $z_0$ have the same coefficients.
>
> *B&C: Sec. 72 (text)*

^cor-72-2

> [!proof]+ Proof
> Apply [[§72★ Uniqueness of Series Representations#^thm-72-1|Theorem §72.1]] with $f \equiv 0$: then $a_n = f^{(n)}(z_0)/n! = 0$ for every $n$. For the second statement, the difference of the two series converges to zero near $z_0$ ([[§61 Convergence of Series#^prop-61-4|Proposition §61.4]]), so its coefficients, the differences of the coefficients, vanish.

^pf-72-2

*Uses:* [[§72★ Uniqueness of Series Representations#^thm-72-1|§72.1]], [[§61 Convergence of Series#^prop-61-4|§61.4]]

> [!remark]- Connections
> - The real version is [[§78 Taylor and Maclaurin Series#^thm-78-1|Calc Thm. §78.1]] with [[§78 Taylor and Maclaurin Series#^cor-78-2|Calc Cor. §78.2]], proved there by repeated term-by-term differentiation, the route of [[§72★ Uniqueness of Series Representations#^ex-72-3|Example §72.3]]; the rigorous term-by-term calculus is [[§26 Differentiation and Integration of Power Series#^thm-26-4|451 Thm. §26.4]].

## Uniqueness of Laurent Series

The proof for Laurent series needs Theorem §71.1 for series that also contain negative powers. B&C leaves this extension to an exercise.

> [!theorem] Lemma §72.3: Term-by-Term Integration of Laurent Series
> Consider two series
>
> $$
> S_1(z) = \sum_{n=0}^{\infty}a_n(z - z_0)^n \qquad\text{and}\qquad S_2(z) = \sum_{n=1}^{\infty}\frac{b_n}{(z - z_0)^n}
> $$
>
> which converge in some annular domain $R_1 < |z - z_0| < R_2$. Let $C$ be any contour lying in that annulus, and let $g(z)$ be continuous on $C$. Then
>
> $$
> \int_C g(z)S_1(z)\,dz = \sum_{n=0}^{\infty}a_n\int_C g(z)(z - z_0)^n\,dz , \qquad \int_C g(z)S_2(z)\,dz = \sum_{n=1}^{\infty}b_n\int_C\frac{g(z)}{(z - z_0)^n}\,dz ,
> $$
>
> and consequently, for $S(z) = \sum_{n=-\infty}^{\infty}c_n(z - z_0)^n = S_1(z) + S_2(z)$,
>
> $$
> \int_C g(z)S(z)\,dz = \sum_{n=-\infty}^{\infty}c_n\int_C g(z)(z - z_0)^n\,dz .
> $$
>
> *B&C: Sec. 72, Exercise 10*

^lem-72-3

> [!proof]+ Proof
> The contour $C$ is the image of a closed interval under a continuous map, so $|z - z_0|$ attains a minimum $r_1$ and a maximum $r_2$ on $C$, with $R_1 < r_1 \le r_2 < R_2$. By [[§70★ Continuity of Sums of Power Series#^cor-70-3|Corollary §70.3]] both series converge uniformly on the closed annulus $r_1 \le |z - z_0| \le r_2$, which contains $C$, and their sums are continuous there ([[§70★ Continuity of Sums of Power Series#^thm-70-1|Theorem §70.1]], [[§70★ Continuity of Sums of Power Series#^cor-70-2|Corollary §70.2]]).
>
> **$S_1$.** Its circle of convergence has radius at least $R_2$, and $C$ is interior to it; this is [[§71★ Integration and Differentiation of Power Series#^thm-71-1|Theorem §71.1]] itself.
>
> **$S_2$.** Repeat the proof of Theorem §71.1 with the remainder $\tau_N(z) = S_2(z) - \sum_{n=1}^{N}b_n(z - z_0)^{-n}$. As there,
>
> $$
> \int_C g(z)S_2(z)\,dz = \sum_{n=1}^{N}b_n\int_C\frac{g(z)}{(z - z_0)^n}\,dz + \int_C g(z)\tau_N(z)\,dz ,
> $$
>
> all integrands being continuous on $C$. If $M = \max_C|g|$ and $L$ is the length of $C$, uniform convergence gives, for each $\varepsilon > 0$, an $N_\varepsilon$ with $|\tau_N(z)| < \varepsilon$ for all $z$ on $C$ when $N > N_\varepsilon$, and so $\big|\int_C g\tau_N\,dz\big| \le M\varepsilon L$. Letting $N \to \infty$ gives the second formula.
>
> **$S$.** Add the two formulas. The right side is the sum of the two convergent series, which is what the doubly infinite series means ([[§66 Laurent Series#^def-66-1|Definition §66.1]]).

^pf-72-3

*Uses:* [[§71★ Integration and Differentiation of Power Series#^thm-71-1|§71.1]], [[§70★ Continuity of Sums of Power Series#^thm-70-1|§70.1]], [[§70★ Continuity of Sums of Power Series#^cor-70-2|§70.2]], [[§70★ Continuity of Sums of Power Series#^cor-70-3|§70.3]], [[§47 Upper Bounds for Moduli of Contour Integrals#^thm-47-2|§47.2]] (ML-inequality), [[§66 Laurent Series#^def-66-1|Def. §66.1]]

> [!theorem] Theorem §72.4: Uniqueness of Laurent Series
> If a series
>
> $$
> \sum_{n=-\infty}^{\infty}c_n(z - z_0)^n = \sum_{n=0}^{\infty}a_n(z - z_0)^n + \sum_{n=1}^{\infty}\frac{b_n}{(z - z_0)^n} \qquad (8)
> $$
>
> converges to $f(z)$ at all points in some annular domain about $z_0$, then it is the Laurent series expansion for $f$ in powers of $z - z_0$ for that domain.
>
> *B&C: Sec. 72, Theorem 2*

^thm-72-4

> [!proof]+ Proof
> Let the annular domain be $R_1 < |z - z_0| < R_2$, so that $f(z) = \sum_{n=-\infty}^{\infty}c_n(z - z_0)^n$ at each point of it. Let $g(z)$ be defined by (4), but now allow $n$ to be any integer, negative too. Let $C$ be any circle in the annulus centered at $z_0$, taken in the positive sense. Using the index of summation $m$ and [[§72★ Uniqueness of Series Representations#^lem-72-3|Lemma §72.3]],
>
> $$
> \frac{1}{2\pi i}\int_C\frac{f(z)\,dz}{(z - z_0)^{n+1}} = \int_C g(z)f(z)\,dz = \sum_{m=-\infty}^{\infty}c_m\int_C g(z)(z - z_0)^m\,dz . \qquad (9)
> $$
>
> Equations (6) remain valid when the integers $m$ and $n$ are allowed to be negative, since they only use that $\int_C(z - z_0)^k\,dz$ is $2\pi i$ for $k = -1$ and $0$ for every other integer $k$. So equation (9) reduces to
>
> $$
> \frac{1}{2\pi i}\int_C\frac{f(z)\,dz}{(z - z_0)^{n+1}} = c_n \qquad (n = 0, \pm1, \pm2, \ldots) ,
> $$
>
> which is expression (5) of [[§66 Laurent Series#^def-66-1|Definition §66.1]] for the coefficients of the Laurent series of $f$ in the annulus. (For this to be meaningful, $f$ must be analytic in the annulus, which B&C takes for granted. Here is why it is. The nonnegative part of (8) is a power series converging in $|z - z_0| < R_2$, so its sum is analytic there by [[§71★ Integration and Differentiation of Power Series#^cor-71-2|Corollary §71.2]]. The negative part is $T\big(1/(z - z_0)\big)$, where $T(w) = \sum b_nw^n$ is analytic in $|w| < 1/R_1$, again by Corollary §71.2, so it is analytic in $|z - z_0| > R_1$ by the chain rule.)

^pf-72-4

*Uses:* [[§72★ Uniqueness of Series Representations#^lem-72-3|§72.3]], [[§66 Laurent Series#^def-66-1|Def. §66.1]], [[§67 Proof of Laurent's Theorem#^thm-67-1|§67.1]], [[§71★ Integration and Differentiation of Power Series#^cor-71-2|§71.2]], [[§45 Some Examples (Contour Integrals)#^ex-45-5|Ex. §45.5]], [[§20 Rules for Differentiation#^thm-20-4|§20.4]] (chain rule)

## Examples

> [!example] Example §72.1: A Laurent Series by Substitution
> **Problem.** By substituting $1/(1 - z)$ for $z$ in the expansion $\frac{1}{(1 - z)^2} = \sum_{n=0}^{\infty}(n + 1)z^n$ $(|z| < 1)$ of [[§71★ Integration and Differentiation of Power Series#^ex-71-2|Example §71.2]], derive the Laurent series
>
> $$
> \frac{1}{z^2} = \sum_{n=2}^{\infty}\frac{(-1)^n(n - 1)}{(z - 1)^n} \qquad (1 < |z - 1| < \infty) .
> $$
>
> **Substitution.** Put $w = \frac{1}{1 - z}$; the condition $|w| < 1$ is $|z - 1| > 1$. Since $1 - w = \frac{(1 - z) - 1}{1 - z} = \frac{-z}{1 - z}$,
>
> $$
> \frac{1}{(1 - w)^2} = \frac{(1 - z)^2}{z^2} = \sum_{n=0}^{\infty}\frac{n + 1}{(1 - z)^n} \qquad (|z - 1| > 1) .
> $$
>
> **Divide by $(1 - z)^2$** (term by term, [[§61 Convergence of Series#^prop-61-4|Proposition §61.4]]):
>
> $$
> \frac{1}{z^2} = \sum_{n=0}^{\infty}\frac{n + 1}{(1 - z)^{n+2}} = \sum_{n=0}^{\infty}\frac{(-1)^n(n + 1)}{(z - 1)^{n+2}} = \sum_{n=2}^{\infty}\frac{(-1)^n(n - 1)}{(z - 1)^n} ,
> $$
>
> using $(1 - z)^{n+2} = (-1)^n(z - 1)^{n+2}$ and replacing $n$ by $n - 2$. By Theorem §72.4 this is the Laurent series of $1/z^2$ in $1 < |z - 1| < \infty$. Compare [[§71★ Integration and Differentiation of Power Series#^ex-71-2|Example §71.2]](a): inside the circle $|z - 1| = 1$ the same function has a Taylor series in nonnegative powers of $z - 1$, outside it a Laurent series in negative powers only, starting with $(z - 1)^{-2}$. (Check at $z = 3$: $\sum_{n \ge 2}(-1)^n(n - 1)/2^n = \frac19$.)
>
> *B&C: Sec. 72, Exercise 2; Source: 342 HW 10*

^ex-72-1

> [!example] Example §72.2: Dividing Out a Zero
> **Problem.** Prove that if $f$ is analytic at $z_0$ and $f(z_0) = f'(z_0) = \cdots = f^{(m)}(z_0) = 0$, then the function $g$ defined by
>
> $$
> g(z) = \begin{cases} \dfrac{f(z)}{(z - z_0)^{m+1}} & \text{when } z \ne z_0, \\[2mm] \dfrac{f^{(m+1)}(z_0)}{(m + 1)!} & \text{when } z = z_0 \end{cases}
> $$
>
> is analytic at $z_0$.
>
> **Proof.** By Taylor's theorem ([[§63 Proof of Taylor's Theorem#^thm-63-1|Theorem §63.1]]), $f(z) = \sum_{n=0}^{\infty}\frac{f^{(n)}(z_0)}{n!}(z - z_0)^n$ in some disk $|z - z_0| < \varepsilon$. The first $m + 1$ coefficients vanish, so
>
> $$
> f(z) = \sum_{n=m+1}^{\infty}\frac{f^{(n)}(z_0)}{n!}(z - z_0)^n, \qquad\text{and for } 0 < |z - z_0| < \varepsilon, \qquad g(z) = \sum_{k=0}^{\infty}\frac{f^{(m+1+k)}(z_0)}{(m + 1 + k)!}(z - z_0)^k .
> $$
>
> At $z = z_0$ the series on the right has the value $\frac{f^{(m+1)}(z_0)}{(m + 1)!} = g(z_0)$. So $g$ is the sum of a power series converging in $|z - z_0| < \varepsilon$, hence analytic at $z_0$ by [[§71★ Integration and Differentiation of Power Series#^cor-71-2|Corollary §71.2]]. This is the basic step in the study of zeros of analytic functions ([[§82 Zeros of Analytic Functions#^thm-82-1|Theorem §82.1]]): $f(z) = (z - z_0)^{m+1}g(z)$ with $g$ analytic.
>
> *B&C: Sec. 72, Exercise 8*

^ex-72-2

> [!example] Example §72.3: Uniqueness by Repeated Differentiation
> **Problem.** Suppose $f(z) = \sum_{n=0}^{\infty}a_n(z - z_0)^n$ inside some circle $|z - z_0| = R$. Use term-by-term differentiation and induction to show that
>
> $$
> f^{(n)}(z) = \sum_{k=0}^{\infty}\frac{(n + k)!}{k!}a_{n+k}(z - z_0)^k \qquad (n = 0, 1, 2, \ldots;\ |z - z_0| < R),
> $$
>
> and deduce Theorem §72.1 again.
>
> **Induction.** For $n = 0$ the formula is the hypothesis. If it holds for $n$, then by [[§71★ Integration and Differentiation of Power Series#^thm-71-4|Theorem §71.4]], applied to the power series on the right (it converges in $|z - z_0| < R$),
>
> $$
> f^{(n+1)}(z) = \sum_{k=1}^{\infty}k\frac{(n + k)!}{k!}a_{n+k}(z - z_0)^{k-1} = \sum_{j=0}^{\infty}\frac{(n + 1 + j)!}{j!}a_{n+1+j}(z - z_0)^j ,
> $$
>
> with $j = k - 1$, since $k\frac{(n + k)!}{k!} = \frac{(n + 1 + j)!}{j!}$. This is the formula for $n + 1$.
>
> **Uniqueness.** Setting $z = z_0$, only the $k = 0$ term survives: $f^{(n)}(z_0) = n!\,a_n$, that is, $a_n = f^{(n)}(z_0)/n!$. This proves Theorem §72.1 without integrals.
>
> *B&C: Sec. 72, Exercise 9*

^ex-72-3

> [!example] Example §72.4: Power Series and Analytic Continuation
> **(a)** The function $f_2(z) = \dfrac{1}{z^2 + 1}$ $(z \ne \pm i)$ is the analytic continuation ([[§28★ Uniquely Determined Analytic Functions#^def-28-1|Definition §28.1]]) of
>
> $$
> f_1(z) = \sum_{n=0}^{\infty}(-1)^nz^{2n} \qquad (|z| < 1)
> $$
>
> into the domain consisting of all points except $\pm i$. Indeed, $f_1$ is analytic in $|z| < 1$ (Corollary §71.2), and substituting $-z^2$ into the geometric series shows $f_1(z) = \frac{1}{1 + z^2} = f_2(z)$ there. The function $f_2$ is analytic in the connected domain $\mathbb{C} \setminus \{\pm i\}$, which contains the disk, and agrees with $f_1$ on it, so it is an analytic continuation of $f_1$; by the uniqueness of analytic continuation ([[§28★ Uniquely Determined Analytic Functions#^prop-28-4|Proposition §28.4]]) it is the only one.
>
> **(b)** Likewise $f_2(z) = 1/z^2$ $(z \ne 0)$ is the analytic continuation of
>
> $$
> f_1(z) = \sum_{n=0}^{\infty}(n + 1)(z + 1)^n \qquad (|z + 1| < 1)
> $$
>
> into $\mathbb{C} \setminus \{0\}$. Differentiating the geometric series $-\frac1z = \frac{1}{1 - (z + 1)} = \sum_{n=0}^{\infty}(z + 1)^n$ $(|z + 1| < 1)$ term by term ([[§71★ Integration and Differentiation of Power Series#^thm-71-4|Theorem §71.4]]) gives $\frac{1}{z^2} = \sum_{n=1}^{\infty}n(z + 1)^{n-1} = \sum_{n=0}^{\infty}(n + 1)(z + 1)^n = f_1(z)$ in the disk, and $1/z^2$ is analytic in the connected domain $z \ne 0$, which contains it.
>
> Both power series have radius $1$, the distance from the center to the nearest singular point of the continuation, as [[§71★ Integration and Differentiation of Power Series#^cor-71-3|Corollary §71.3]] requires.
>
> *B&C: Sec. 72, Exercises 11 and 12*

^ex-72-4
