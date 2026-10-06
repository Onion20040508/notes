---
type: section
subject: "[[Complex Variables]]"
chapter: 5
section: 67
bc: "67"
aliases: ["B&C 67"]
tags: [complex-variables, math342]
---
← [[§66 Laurent Series]] · ↑ [[· 5 Series]] · [[§68 Examples (Proof of Laurent's Theorem)]] →

*Brown–Churchill, Section 67 · MAT 342 HW 10 · Practice Finals (Fall 1999, Spring 2005, Fall 2009, Spring 2012).*

This section proves Laurent's theorem, stated in [[§66 Laurent Series|§66]]. The proof follows the proof of Taylor's theorem ([[§63 Proof of Taylor's Theorem|§63]]) with one new ingredient. By the Cauchy–Goursat theorem for multiply connected domains, $f(z)$ is the difference of two Cauchy integrals, one over an outer circle $C_2$ and one over an inner circle $C_1$. On $C_2$ the kernel $1/(s - z)$ expands in positive powers of $z$, exactly as for Taylor's theorem. On $C_1$, where $|s| < |z|$, it expands in negative powers of $z$. The first integral therefore gives the series in nonnegative powers, and the second gives the series in negative powers. The examples show the same split in practice: singular points outside the annulus contribute positive powers, singular points inside it contribute negative powers.

## Laurent's Theorem

> [!theorem] Theorem §67.1: Laurent's Theorem
> Suppose that a function $f$ is analytic throughout an annular domain $R_1 < |z - z_0| < R_2$ ($0 \le R_1 < R_2 \le \infty$), centered at $z_0$, and let $C$ denote any positively oriented simple closed contour around $z_0$ and lying in that domain. Then, at each point in the domain, $f(z)$ has the series representation
>
> $$
> f(z) = \sum_{n=0}^{\infty} a_n(z - z_0)^n + \sum_{n=1}^{\infty}\frac{b_n}{(z - z_0)^n} \qquad (R_1 < |z - z_0| < R_2),
> $$
>
> where both series converge, and
>
> $$
> a_n = \frac{1}{2\pi i}\int_C\frac{f(z)\,dz}{(z - z_0)^{n+1}} \quad (n = 0, 1, 2, \ldots), \qquad b_n = \frac{1}{2\pi i}\int_C\frac{f(z)\,dz}{(z - z_0)^{-n+1}} \quad (n = 1, 2, \ldots) .
> $$
>
> Equivalently, $f(z) = \sum_{n=-\infty}^{\infty} c_n(z - z_0)^n$ with $c_n = \frac{1}{2\pi i}\int_C\frac{f(z)\,dz}{(z - z_0)^{n+1}}$ ([[§66 Laurent Series#^def-66-1|Definition §66.1]]).
>
> *B&C: Sec. 66, Theorem (proved in Sec. 67)*

^thm-67-1

> [!proof]- Proof
> **The case $z_0 = 0$.** Fix a point $z$ of the annulus $R_1 < |z| < R_2$ and write $|z| = r$.
>
> *Choosing the circles.* The contour $C$ is the image of a closed interval under a continuous map, so $|s|$ attains a minimum $m$ and a maximum $m'$ on $C$, and $R_1 < m \le m' < R_2$ because $C$ lies in the annulus. Choose $r_1$ and $r_2$ with
>
> $$
> R_1 < r_1 < \min(r, m), \qquad \max(r, m') < r_2 < R_2 .
> $$
>
> Then the closed annular region $r_1 \le |s| \le r_2$ is contained in the domain $R_1 < |s| < R_2$, and its interior contains both the point $z$ and the contour $C$ (Figure). Let $C_1$ and $C_2$ denote the circles $|s| = r_1$ and $|s| = r_2$, both positively oriented. The function $f$ is analytic on $C_1$ and $C_2$ and in the annular domain between them. Next, let $\gamma$ be the positively oriented circle with center $z$ and radius $\delta$, where $0 < \delta < \min(r - r_1, r_2 - r)$. For $|s - z| \le \delta$ we have $r_1 < r - \delta \le |s| \le r + \delta < r_2$, so $\gamma$ and its interior lie in the open region $r_1 < |s| < r_2$; in particular the interiors of $C_1$ and $\gamma$ are disjoint.
>
> *Two Cauchy integrals.* The function $f(s)/(s - z)$ is analytic on $C_2$, $C_1$, $\gamma$ and throughout the region inside $C_2$ and outside both $C_1$ and $\gamma$. By the Cauchy–Goursat theorem for the oriented boundary of a multiply connected domain ([[§53 Multiply Connected Domains#^thm-53-1|Theorem §53.1]]),
>
> $$
> \int_{C_2}\frac{f(s)\,ds}{s - z} - \int_{C_1}\frac{f(s)\,ds}{s - z} - \int_\gamma\frac{f(s)\,ds}{s - z} = 0 .
> $$
>
> By the Cauchy integral formula ([[§54 Cauchy Integral Formula#^thm-54-1|Theorem §54.1]]) the third integral is $2\pi i f(z)$. Hence
>
> $$
> f(z) = \frac{1}{2\pi i}\int_{C_2}\frac{f(s)\,ds}{s - z} + \frac{1}{2\pi i}\int_{C_1}\frac{f(s)\,ds}{z - s} . \qquad (1)
> $$
>
> *Expanding the two kernels.* For $s$ on $C_2$ we have $|z/s| = r/r_2 < 1$, and the expansion from the proof of Taylor's theorem ([[§63 Proof of Taylor's Theorem#^pf-63-1|proof of §63.1]], equation (4)) applies:
>
> $$
> \frac{1}{s - z} = \sum_{n=0}^{N-1}\frac{1}{s^{n+1}}z^n + z^N\frac{1}{(s - z)s^N} . \qquad (2)
> $$
>
> For $s$ on $C_1$ we have $|s/z| = r_1/r < 1$, so the same identity with the roles of $s$ and $z$ interchanged holds:
>
> $$
> \frac{1}{z - s} = \sum_{n=0}^{N-1}\frac{1}{s^{-n}}\cdot\frac{1}{z^{n+1}} + \frac{1}{z^N}\cdot\frac{s^N}{z - s} .
> $$
>
> Replacing the index of summation $n$ by $n - 1$, this takes the form
>
> $$
> \frac{1}{z - s} = \sum_{n=1}^{N}\frac{1}{s^{-n+1}}\cdot\frac{1}{z^n} + \frac{1}{z^N}\cdot\frac{s^N}{z - s} . \qquad (3)
> $$
>
> *Integrating.* Multiply (2) and (3) by $f(s)/(2\pi i)$ and integrate with respect to $s$ around $C_2$ and $C_1$, respectively (finite sums of continuous integrands, so the integrals may be taken term by term):
>
> $$
> \frac{1}{2\pi i}\int_{C_2}\frac{f(s)\,ds}{s - z} = \sum_{n=0}^{N-1}a_nz^n + \rho_N(z), \qquad \frac{1}{2\pi i}\int_{C_1}\frac{f(s)\,ds}{z - s} = \sum_{n=1}^{N}\frac{b_n}{z^n} + \sigma_N(z), \qquad (4)
> $$
>
> where
>
> $$
> a_n = \frac{1}{2\pi i}\int_{C_2}\frac{f(s)\,ds}{s^{n+1}}, \qquad b_n = \frac{1}{2\pi i}\int_{C_1}\frac{f(s)\,ds}{s^{-n+1}} \qquad (5)
> $$
>
> and
>
> $$
> \rho_N(z) = \frac{z^N}{2\pi i}\int_{C_2}\frac{f(s)\,ds}{(s - z)s^N}, \qquad \sigma_N(z) = \frac{1}{2\pi i\,z^N}\int_{C_1}\frac{s^Nf(s)\,ds}{z - s} .
> $$
>
> *The remainders tend to zero.* Let $M$ denote the maximum value of $|f(s)|$ on $C_1$ and $C_2$ (a continuous function on closed bounded sets, [[§18 Continuity#^thm-18-6|Theorem §18.6]]). If $s$ is on $C_2$, then $|s - z| \ge r_2 - r$; if $s$ is on $C_1$, then $|z - s| \ge r - r_1$. The circles have lengths $2\pi r_2$ and $2\pi r_1$. By the ML-inequality ([[§47 Upper Bounds for Moduli of Contour Integrals#^thm-47-2|Theorem §47.2]]),
>
> $$
> |\rho_N(z)| \le \frac{r^N}{2\pi}\cdot\frac{M}{(r_2 - r)r_2^N}\cdot2\pi r_2 = \frac{Mr_2}{r_2 - r}\Big(\frac{r}{r_2}\Big)^N, \qquad |\sigma_N(z)| \le \frac{1}{2\pi r^N}\cdot\frac{r_1^NM}{r - r_1}\cdot2\pi r_1 = \frac{Mr_1}{r - r_1}\Big(\frac{r_1}{r}\Big)^N .
> $$
>
> Since $r/r_2 < 1$ and $r_1/r < 1$, both $\rho_N(z)$ and $\sigma_N(z)$ tend to zero as $N \to \infty$:
>
> $$
> \lim_{N\to\infty}\rho_N(z) = 0 \qquad\text{and}\qquad \lim_{N\to\infty}\sigma_N(z) = 0 . \qquad (6)
> $$
>
> By (4), the series $\sum_{n \ge 0}a_nz^n$ therefore converges to $\frac{1}{2\pi i}\int_{C_2}\frac{f(s)\,ds}{s - z}$, and the series $\sum_{n \ge 1}b_n/z^n$ converges to $\frac{1}{2\pi i}\int_{C_1}\frac{f(s)\,ds}{z - s}$. (B&C adds the two expansions into one equation; keeping them apart shows that each series converges separately, as [[§66 Laurent Series#^def-66-1|Definition §66.1]] requires.) By (1), their sum is $f(z)$:
>
> $$
> f(z) = \sum_{n=0}^{\infty}a_nz^n + \sum_{n=1}^{\infty}\frac{b_n}{z^n} .
> $$
>
> *The coefficients do not depend on $z$.* The circles $C_1$ and $C_2$ were chosen with $z$ in mind, so it remains to show that the integrals (5) may be taken over $C$; then the coefficients are those of the theorem, the same for every $z$ (after renaming the variable of integration $s$ as $z$). Here is why [[§53 Multiply Connected Domains#^cor-53-2|Corollary §53.2]] (two positively oriented simple closed contours, one interior to the other, with the integrand analytic on both and between them, give equal integrals) applies; B&C cites it without detail.
> - The disk $|s| < m$ is connected, contains the point $0$, which is interior to $C$, and does not meet $C$; so it lies inside $C$ (the interior of $C$ is one of the two domains of the Jordan curve theorem, [[§43 Contours#^thm-43-4|Theorem §43.4]]). Likewise the set $|s| > m'$ is connected, unbounded and does not meet $C$, so it lies outside $C$. Hence the region inside $C$ is contained in $|s| \le m'$, and the region outside $C$ is contained in $|s| \ge m$.
> - For $a_n$: the integrand $f(s)/s^{n+1}$ is analytic in the annulus $R_1 < |s| < R_2$. The contour $C$ is interior to $C_2$ (since $m' < r_2$), and the points between them, inside $C_2$ and outside $C$, satisfy $R_1 < m \le |s| \le r_2 < R_2$. So $\int_{C_2} = \int_C$.
> - For $b_n$: the integrand $f(s)s^{n-1}$ is analytic in the same annulus. The circle $C_1$ is interior to $C$ (since $r_1 < m$), and the points between them satisfy $R_1 < r_1 \le |s| \le m' < R_2$. So $\int_{C_1} = \int_C$.
>
> This completes the proof when $z_0 = 0$.
>
> **The case $z_0 \ne 0$.** Let $f$ satisfy the conditions of the theorem and write $g(z) = f(z + z_0)$. Since $f$ is analytic in the annulus $R_1 < |z - z_0| < R_2$, the function $g$ is analytic when $R_1 < |(z + z_0) - z_0| < R_2$, that is, in the annulus $R_1 < |z| < R_2$ centered at the origin. The contour $C$ has a parametric representation $z = z(t)$ $(a \le t \le b)$ with
>
> $$
> R_1 < |z(t) - z_0| < R_2 \qquad (a \le t \le b) . \qquad (7)
> $$
>
> Let $\Gamma$ denote the path
>
> $$
> z = z(t) - z_0 \qquad (a \le t \le b) . \qquad (8)
> $$
>
> It is the translate of $C$ by $-z_0$, so it is a simple closed contour; by (7) it lies in the domain $R_1 < |z| < R_2$; and since a translation carries the interior of $C$, which contains $z_0$, onto the interior of $\Gamma$ without changing the sense of traversal, $\Gamma$ is positively oriented around the origin. By the first case, $g$ has the Laurent series representation
>
> $$
> g(z) = \sum_{n=0}^{\infty}a_nz^n + \sum_{n=1}^{\infty}\frac{b_n}{z^n} \qquad (R_1 < |z| < R_2), \qquad (9)
> $$
>
> where
>
> $$
> a_n = \frac{1}{2\pi i}\int_\Gamma\frac{g(z)\,dz}{z^{n+1}} \quad (n = 0, 1, 2, \ldots), \qquad (10) \qquad\qquad b_n = \frac{1}{2\pi i}\int_\Gamma\frac{g(z)\,dz}{z^{-n+1}} \quad (n = 1, 2, \ldots) . \qquad (11)
> $$
>
> Writing $f(z + z_0)$ for $g(z)$ in (9), then replacing $z$ by $z - z_0$ in the resulting equation and in the condition of validity, gives representation (1) of §66 in $R_1 < |z - z_0| < R_2$. The coefficients agree with (2) and (3) of §66, since by the definition of contour integrals ([[§44 Contour Integrals#^def-44-1|Definition §44.1]]), with $\Gamma'(t) = z'(t)$ and $g(\Gamma(t)) = f[z(t)]$,
>
> $$
> \int_\Gamma\frac{g(z)\,dz}{z^{n+1}} = \int_a^b\frac{f[z(t)]\,z'(t)}{[z(t) - z_0]^{n+1}}\,dt = \int_C\frac{f(z)\,dz}{(z - z_0)^{n+1}} ,
> $$
>
> and the same computation with $-n$ in place of $n$ handles $b_n$.

^pf-67-1

*Uses:* [[§66 Laurent Series#^def-66-1|Def. §66.1]], [[§63 Proof of Taylor's Theorem#^thm-63-1|§63.1]] (its proof, expansion (4)), [[§61 Convergence of Series#^ex-61-1|Ex. §61.1]], [[§53 Multiply Connected Domains#^thm-53-1|§53.1]] (Cauchy–Goursat for multiply connected domains), [[§53 Multiply Connected Domains#^cor-53-2|§53.2]] (deformation), [[§54 Cauchy Integral Formula#^thm-54-1|§54.1]], [[§47 Upper Bounds for Moduli of Contour Integrals#^thm-47-2|§47.2]] (ML-inequality), [[§44 Contour Integrals#^def-44-1|Def. §44.1]], [[§43 Contours#^thm-43-4|§43.4]] (Jordan curve theorem), [[§18 Continuity#^thm-18-6|§18.6]], [[§96 Maximum and Minimum Values#^thm-96-3|Calc Thm. §96.3]] (extreme value theorem)

![[m342-67-1.svg]]
*The proof for $z_0 = 0$. The function is analytic between the dashed circles $|z| = R_1$ and $|z| = R_2$. The circles $C_1$ and $C_2$ (blue) are chosen so that the closed ring between them contains both the point $z$ and the contour $C$ (green); the small circle $\gamma$ (red) about $z$ is cut out of the ring. The integral over $C_2$ produces the nonnegative powers of $z$, the integral over $C_1$ the negative powers, and at the end both are moved to $C$.*

> [!remark]- Connections
> - The multiply connected Cauchy–Goursat theorem used in the first step is, for $f$ with continuous derivative, the complex form of Green's theorem for a region with holes, [[§110 Green's Theorem#^thm-110-4|Calc Thm. §110.4]]; the rigorous Green's theorem is [[§16 Line Integrals and Green's Theorem#^thm-16-1|452 Thm. §16.1]].
> - The bounds $|\rho_N| \le \frac{Mr_2}{r_2 - r}(r/r_2)^N$ and $|\sigma_N| \le \frac{Mr_1}{r - r_1}(r_1/r)^N$ do not depend on $z$ as long as $z$ stays in a smaller closed ring $r_1' \le |z| \le r_2'$ with $r_1 < r_1'$, $r_2' < r_2$. So the convergence is uniform on such rings: the Weierstrass M-test situation of [[§25 More on Uniform Convergence#^thm-25-3|451 Thm. §25.3]]. B&C records this in [[§70★ Continuity of Sums of Power Series#^cor-70-3|Corollary §70.3]].

## Laurent Series by Partial Fractions

The proof shows where the two halves of a Laurent series come from, and this suggests a practical method for rational functions.

> [!remark] Remark: Method — Laurent Series in an Annulus
> To expand $f$ in powers of $z - z_0$ in an annulus $R_1 < |z - z_0| < R_2$:
> 1. **Find the annuli.** Mark the singular points of $f$. The circles centered at $z_0$ through them divide the plane into a disk, annuli, and an exterior domain; $f$ has a different Laurent series in each ([[§72★ Uniqueness of Series Representations#^thm-72-4|Theorem §72.4]] makes each one unique).
> 2. **Partial fractions.** Write a rational $f$ as a polynomial plus terms $A/(z - p)^k$.
> 3. **Expand each term according to where its pole lies.** If $|p - z_0| \ge R_2$ (pole outside the annulus), expand in nonnegative powers:
>
>    $$
>    \frac{1}{z - p} = -\frac{1}{p - z_0}\cdot\frac{1}{1 - \frac{z - z_0}{p - z_0}} = -\sum_{n=0}^{\infty}\frac{(z - z_0)^n}{(p - z_0)^{n+1}} \qquad (|z - z_0| < |p - z_0|) .
>    $$
>
>    If $|p - z_0| \le R_1$ (pole inside the inner circle), expand in negative powers:
>
>    $$
>    \frac{1}{z - p} = \frac{1}{z - z_0}\cdot\frac{1}{1 - \frac{p - z_0}{z - z_0}} = \sum_{n=1}^{\infty}\frac{(p - z_0)^{n-1}}{(z - z_0)^n} \qquad (|z - z_0| > |p - z_0|) .
>    $$
>
>    A pole at $p = z_0$ itself is already a single negative power. Higher powers $1/(z - p)^k$ follow by differentiating these series term by term ([[§71★ Integration and Differentiation of Power Series#^thm-71-4|Theorem §71.4]]).
> 4. **Add** the expansions ([[§61 Convergence of Series#^prop-61-4|Proposition §61.4]]). Poles outside the annulus contribute only to the nonnegative powers, poles inside it only to the negative powers, mirroring the integrals over $C_2$ and $C_1$ in the proof.

^rem-67-1

> [!example] Example §67.1: One Function, Three Domains
> **Problem.** The function
>
> $$
> f(z) = \frac{-1}{(z - 1)(z - 2)} = \frac{1}{z - 1} - \frac{1}{z - 2}
> $$
>
> has the singular points $z = 1$ and $z = 2$, and is analytic in $D_1\colon |z| < 1$, $D_2\colon 1 < |z| < 2$, $D_3\colon 2 < |z| < \infty$. Find its series in powers of $z$ in each domain.
>
> **$D_1$ (both poles outside).** $\frac{1}{z - 1} = -\sum_{n \ge 0}z^n$ and $-\frac{1}{z - 2} = \frac12\cdot\frac{1}{1 - z/2} = \sum_{n \ge 0}\frac{z^n}{2^{n+1}}$, so
>
> $$
> f(z) = \sum_{n=0}^{\infty}\big(2^{-n-1} - 1\big)z^n \qquad (|z| < 1) .
> $$
>
> **$D_2$ (pole $1$ inside, pole $2$ outside).** Now $\frac{1}{z - 1} = \frac1z\cdot\frac{1}{1 - 1/z} = \sum_{n \ge 1}\frac{1}{z^n}$, since $|1/z| < 1$:
>
> $$
> f(z) = \sum_{n=0}^{\infty}\frac{z^n}{2^{n+1}} + \sum_{n=1}^{\infty}\frac{1}{z^n} \qquad (1 < |z| < 2) .
> $$
>
> **The proof at work in $D_2$.** Compute the coefficients from (5), with $1 < r_1 < r_2 < 2$. For $b_n$, integrate $f(s)s^{n-1} = \frac{s^{n-1}}{s - 1} - \frac{s^{n-1}}{s - 2}$ over $C_1$: the second term is analytic inside and on $C_1$ (the point $2$ is outside), so its integral is $0$ by Cauchy–Goursat, and the Cauchy integral formula gives $\frac{1}{2\pi i}\int_{C_1}\frac{s^{n-1}\,ds}{s - 1} = 1^{n-1} = 1$. So $b_n = 1$, and only the inner pole contributes. For $a_n$, integrate $f(s)/s^{n+1}$ over $C_2$. The term $\frac{1}{(s - 1)s^{n+1}}$ contributes nothing: its integral over $|s| = R$ is the same for all $R > 1$ ([[§53 Multiply Connected Domains#^cor-53-2|Corollary §53.2]]) and is at most $2\pi R/\big((R - 1)R^{n+1}\big) \to 0$ as $R \to \infty$. The term $-\frac{1}{(s - 2)s^{n+1}}$ gives, by the extended Cauchy formula at $0$,
>
> $$
> a_n = -\frac{1}{n!}\frac{d^n}{ds^n}\Big(\frac{1}{s - 2}\Big)\Big|_{s=0} = -\frac{(-1)^nn!\,(0 - 2)^{-n-1}}{n!} = \frac{1}{2^{n+1}} .
> $$
>
> So only the outer pole contributes to the $a_n$, in agreement with the series above.
>
> **$D_3$ (both poles inside).** Also $-\frac{1}{z - 2} = -\frac1z\cdot\frac{1}{1 - 2/z} = -\sum_{n \ge 1}\frac{2^{n-1}}{z^n}$, so
>
> $$
> f(z) = \sum_{n=1}^{\infty}\frac{1 - 2^{n-1}}{z^n} \qquad (2 < |z| < \infty) .
> $$
>
> (The $n = 1$ term vanishes: $f(z) \approx -1/z^2$ for large $z$.) All three answers agree with numerical evaluation of the coefficient integrals (5) of §66 on circles of radius $0.5$, $1.5$ and $3$.
>
> **The Taylor case.** $\dfrac{1}{z^2 - 3z + 2} = -f(z)$, so its Taylor series about $0$ is $\sum_{n=0}^{\infty}\big(1 - 2^{-n-1}\big)z^n$, valid for $|z| < 1$, the distance to the nearer pole.
>
> *B&C: Sec. 68, Exercise 5; Source: 342 practice final (Fall 1999), Q6(b)*

^ex-67-1

> [!example] Example §67.2: Taylor and Laurent Series on Old Finals
> **(a) Spring 2012.** Let $f(z) = \dfrac{3}{(z - 1)(z + 2)} = \dfrac{1}{z - 1} - \dfrac{1}{z + 2}$. Find **(i)** the Taylor series centered at the origin, and where $f$ equals its sum; **(ii)** the Laurent series in $1 < |z| < 2$; **(iii)** the Laurent series in $|z| > 2$.
>
> **(i)** $\frac{1}{z - 1} = -\sum_{n \ge 0}z^n$ $(|z| < 1)$ and $-\frac{1}{z + 2} = -\frac12\cdot\frac{1}{1 + z/2} = \sum_{n \ge 0}\big(-\frac12\big)^{n+1}z^n$ $(|z| < 2)$, so
>
> $$
> f(z) = \sum_{n=0}^{\infty}\Big[-1 + \Big(-\frac12\Big)^{n+1}\Big]z^n \qquad (|z| < 1) .
> $$
>
> By Taylor's theorem the series converges to $f$ in $|z| < 1$, the largest open disk about $0$ in which $f$ is analytic. For $|z| \ge 1$ it diverges: for $n \ge 1$ the coefficient has modulus at least $1 - \frac14$, so the terms do not tend to $0$ ([[§61 Convergence of Series#^cor-61-2|Corollary §61.2]]). So $f$ equals its Taylor sum exactly on $|z| < 1$.
>
> **(ii)** With $\frac{1}{z - 1} = \sum_{n \ge 1}z^{-n}$ for $|z| > 1$:
>
> $$
> f(z) = \sum_{n=0}^{\infty}\Big(-\frac12\Big)^{n+1}z^n + \sum_{n=1}^{\infty}\frac{1}{z^n} \qquad (1 < |z| < 2) .
> $$
>
> **(iii)** With $-\frac{1}{z + 2} = -\frac1z\cdot\frac{1}{1 + 2/z} = -\sum_{n \ge 1}\frac{(-2)^{n-1}}{z^n}$ for $|z| > 2$:
>
> $$
> f(z) = \sum_{n=1}^{\infty}\frac{1 - (-2)^{n-1}}{z^n} = \frac{3}{z^2} - \frac{3}{z^3} + \frac{9}{z^4} - \cdots \qquad (|z| > 2) .
> $$
>
> **(b) Spring 2005.** For $f(z) = \dfrac{2z + 1}{z^2 + z - 2} = \dfrac{1}{z - 1} + \dfrac{1}{z + 2}$, the same expansions with the sign of the second term changed give the Taylor series
>
> $$
> f(z) = \sum_{n=0}^{\infty}\Big[-1 + \frac{(-1)^n}{2^{n+1}}\Big]z^n ,
> $$
>
> with radius of convergence $1$: by Taylor's theorem it converges in the largest disk about $0$ that avoids the singular points $1$ and $-2$, and it diverges for $|z| > 1$ because its terms do not tend to zero. In $1 < |z| < 2$, $f(z) = \sum_{n=1}^{\infty}z^{-n} + \sum_{n=0}^{\infty}\frac{(-1)^n}{2^{n+1}}z^n$.
>
> **(c) Fall 2009.** For $f(z) = \dfrac{2}{z^2 + 4z + 3} = \dfrac{1}{z + 1} - \dfrac{1}{z + 3}$: $\frac{1}{z + 1} = \sum_{n \ge 0}(-1)^nz^n$ $(|z| < 1)$ and $-\frac{1}{z + 3} = -\frac13\cdot\frac{1}{1 + z/3} = \sum_{n \ge 0}\frac{(-1)^{n+1}}{3^{n+1}}z^n$ $(|z| < 3)$, so
>
> $$
> f(z) = \sum_{n=0}^{\infty}(-1)^n\Big(1 - \frac{1}{3^{n+1}}\Big)z^n \qquad (|z| < 1),
> $$
>
> and $f$ equals the sum of its Taylor series exactly in $|z| < 1$ (the singular point $-1$ is on the circle, and the terms do not tend to zero for $|z| \ge 1$). In $1 < |z| < 3$, using $\frac{1}{z + 1} = \frac1z\cdot\frac{1}{1 + 1/z} = \sum_{n \ge 1}\frac{(-1)^{n-1}}{z^n}$,
>
> $$
> f(z) = \sum_{n=1}^{\infty}\frac{(-1)^{n-1}}{z^n} + \sum_{n=0}^{\infty}\frac{(-1)^{n+1}}{3^{n+1}}z^n \qquad (1 < |z| < 3) .
> $$
>
> All coefficients were confirmed by numerical contour integration.
>
> *Source: 342 practice final (Spring 2012), Q6; 342 practice final (Spring 2005), Q4; 342 practice final (Fall 2009), Q5*

^ex-67-2

> [!example] Example §67.3: A Laurent Series About z₀ = 1
> **Problem.** Show that when $0 < |z - 1| < 2$,
>
> $$
> \frac{z}{(z - 1)(z - 3)} = -3\sum_{n=0}^{\infty}\frac{(z - 1)^n}{2^{n+2}} - \frac{1}{2(z - 1)} ,
> $$
>
> and find the series in powers of $z - 1$ in the other domain, $2 < |z - 1| < \infty$.
>
> **Partial fractions.** $\dfrac{z}{(z - 1)(z - 3)} = \dfrac{A}{z - 1} + \dfrac{B}{z - 3}$ with $A = \frac{1}{1 - 3} = -\frac12$ and $B = \frac{3}{3 - 1} = \frac32$ (cover-up rule), so
>
> $$
> f(z) = -\frac{1}{2(z - 1)} + \frac{3}{2(z - 3)} .
> $$
>
> The first term is already a power of $z - 1$. The center is $z_0 = 1$, and the other pole $3$ is at distance $2$ from it.
>
> **$0 < |z - 1| < 2$ (pole $3$ outside).** Since $\big|\frac{z - 1}{2}\big| < 1$,
>
> $$
> \frac{3}{2(z - 3)} = \frac{3}{2\big((z - 1) - 2\big)} = -\frac34\cdot\frac{1}{1 - \frac{z - 1}{2}} = -\frac34\sum_{n=0}^{\infty}\frac{(z - 1)^n}{2^n} = -3\sum_{n=0}^{\infty}\frac{(z - 1)^n}{2^{n+2}} ,
> $$
>
> which gives the stated series.
>
> **$2 < |z - 1| < \infty$ (pole $3$ inside).** Now $\big|\frac{2}{z - 1}\big| < 1$, and
>
> $$
> \frac{3}{2(z - 3)} = \frac{3}{2(z - 1)}\cdot\frac{1}{1 - \frac{2}{z - 1}} = \frac32\sum_{n=0}^{\infty}\frac{2^n}{(z - 1)^{n+1}} = \sum_{n=1}^{\infty}\frac{3\cdot2^{n-2}}{(z - 1)^n} ,
> $$
>
> so, adding $-\frac{1}{2(z - 1)}$ to the $n = 1$ term $\frac{3}{2(z - 1)}$,
>
> $$
> \frac{z}{(z - 1)(z - 3)} = \frac{1}{z - 1} + \sum_{n=2}^{\infty}\frac{3\cdot2^{n-2}}{(z - 1)^n} = \frac{1}{z - 1} + \frac{3}{(z - 1)^2} + \frac{6}{(z - 1)^3} + \cdots \qquad (2 < |z - 1| < \infty) .
> $$
>
> *B&C: Sec. 68, Exercise 6; Source: 342 HW 10*

^ex-67-3
