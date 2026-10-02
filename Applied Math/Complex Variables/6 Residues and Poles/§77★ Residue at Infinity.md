---
type: section
subject: "[[Complex Variables]]"
chapter: 6
section: 77
bc: "77"
aliases: ["B&C 77"]
tags: [complex-variables, math342, extension]
---
← [[§76 Cauchy's Residue Theorem]] · ↑ [[· 6 Residues and Poles]] · [[§78 The Three Types of Isolated Singular Points]] →

*Brown–Churchill, Section 77 · MAT 342 HW 11 (optional part), Practice Final (Spring 2005).*
★ *Beyond MAT 342: the course skipped this section or left it optional; it is included from Brown–Churchill.*

When all the singular points of $f$ lie inside a contour $C$, the integral of $f$ around $C$ can also be read off from the behavior of $f$ far away: it is determined by the **residue at infinity**, defined through a large circle traversed clockwise, which keeps the point at infinity on its left. Replacing $z$ by $1/z$ turns that residue into an ordinary residue at the origin, and so $\int_C f(z)\,dz = 2\pi i\operatorname{Res}_{z=0}\big[\frac{1}{z^2}f\big(\frac1z\big)\big]$. One residue then replaces the sum of many in Cauchy's residue theorem, which is often quicker; as a by-product, the residues of $f$ at all its singular points, $\infty$ included, add up to zero.

## The Residue at Infinity

Suppose that $f$ is analytic throughout the finite plane except for a finite number of singular points interior to a positively oriented simple closed contour $C$. Let $R_1$ be a positive number large enough that $C$ lies inside the circle $|z| = R_1$ (Fig. 95 in B&C). Then $f$ is analytic throughout the domain $R_1 < |z| < \infty$, and the point at infinity is an isolated singular point of $f$ ([[§74 Isolated Singular Points#^def-74-2|Definition §74.2]]).

> [!definition] Definition §77.1: Residue at Infinity
> Let $f$ be analytic in $R_1 < |z| < \infty$, and let $C_0$ be a circle $|z| = R_0$ with $R_0 > R_1$, oriented in the **clockwise** direction. The **residue of $f$ at infinity** is defined by the equation
>
> $$
> \int_{C_0} f(z)\,dz = 2\pi i\operatorname{Res}_{z=\infty} f(z) . \qquad (1)
> $$
>
> The circle $C_0$ keeps the point at infinity on its left, just as the singular point in the finite plane is on the left in [[§75 Residues#^thm-75-1|Theorem §75.1]].
>
> *B&C: Sec. 77, Equation (1)*

^def-77-1

The value does not depend on the choice of $R_0 > R_1$: two such circles bound an annulus in which $f$ is analytic, so the integrals over them agree by the principle of deformation of paths ([[§53 Multiply Connected Domains#^cor-53-2|Corollary §53.2]]).

> [!theorem] Proposition §77.1: Computing the Residue at Infinity
> Let $f$ be analytic throughout the finite plane except for a finite number of singular points interior to a positively oriented simple closed contour $C$. Then
>
> $$
> \int_C f(z)\,dz = -2\pi i\operatorname{Res}_{z=\infty} f(z) \qquad (2)
> $$
>
> and
>
> $$
> \operatorname{Res}_{z=\infty} f(z) = -\operatorname{Res}_{z=0}\Big[\frac{1}{z^2}f\Big(\frac1z\Big)\Big] . \qquad (6)
> $$
>
> *B&C: Sec. 77, Equations (2) and (6)*

^prop-77-1

> [!proof]+ Proof
> Let $R_1$ and $C_0$ be as above.
>
> **(2).** Since $f$ is analytic throughout the closed region bounded by $C$ and $C_0$, the principle of deformation of paths ([[§53 Multiply Connected Domains#^cor-53-2|Corollary §53.2]]) gives
>
> $$
> \int_C f(z)\,dz = \int_{-C_0} f(z)\,dz = -\int_{C_0} f(z)\,dz ,
> $$
>
> where $-C_0$ is the circle $|z| = R_0$ taken counterclockwise. By definition (1) the right side is $-2\pi i\operatorname{Res}_{z=\infty} f(z)$.
>
> **(6).** Since $f$ is analytic in the annulus $R_1 < |z| < \infty$, it has a Laurent series there (Laurent's theorem, [[§67 Proof of Laurent's Theorem#^thm-67-1|Theorem §67.1]]):
>
> $$
> f(z) = \sum_{n=-\infty}^{\infty} c_nz^n \qquad (R_1 < |z| < \infty), \qquad (3)
> $$
>
> $$
> c_n = \frac{1}{2\pi i}\int_{-C_0}\frac{f(z)\,dz}{z^{n+1}} \qquad (n = 0, \pm1, \pm2, \ldots) , \qquad (4)
> $$
>
> the circle $-C_0$ being positively oriented and lying in the annulus. If $0 < |z| < 1/R_1$, then $|1/z| > R_1$, so $z$ may be replaced by $1/z$ in (3); multiplying the result by $1/z^2$,
>
> $$
> \frac{1}{z^2}f\Big(\frac1z\Big) = \sum_{n=-\infty}^{\infty}\frac{c_n}{z^{n+2}} = \sum_{n=-\infty}^{\infty}\frac{c_{n-2}}{z^n} \qquad \Big(0 < |z| < \frac{1}{R_1}\Big) .
> $$
>
> This series converges to $\frac{1}{z^2}f(\frac1z)$ in the punctured disk, so it is the Laurent series of that function about $0$ ([[§72★ Uniqueness of Series Representations|§72★]], Theorem 2; B&C uses this tacitly). Its coefficient of $1/z$ is the one with $n = 1$, namely $c_{-1}$:
>
> $$
> c_{-1} = \operatorname{Res}_{z=0}\Big[\frac{1}{z^2}f\Big(\frac1z\Big)\Big] .
> $$
>
> On the other hand, putting $n = -1$ in (4) gives $c_{-1} = \frac{1}{2\pi i}\int_{-C_0} f(z)\,dz$, that is,
>
> $$
> \int_{C_0} f(z)\,dz = -2\pi i\operatorname{Res}_{z=0}\Big[\frac{1}{z^2}f\Big(\frac1z\Big)\Big] . \qquad (5)
> $$
>
> Comparing (5) with definition (1) gives (6).

^pf-77-1

*Uses:* [[§77★ Residue at Infinity#^def-77-1|Def. §77.1]], [[§53 Multiply Connected Domains#^cor-53-2|§53.2]] (deformation of paths), [[§67 Proof of Laurent's Theorem#^thm-67-1|§67.1]] (Laurent's theorem), [[§72★ Uniqueness of Series Representations|§72★]] (Theorem 2), [[§75 Residues#^def-75-1|Def. §75.1]]

![[m342-77-1.svg]]
*The residue at infinity. All singular points of $f$ (black dots) lie inside $C$ (blue), which lies inside the circle $|z| = R_1$ (dashed). The circle $C_0$, $|z| = R_0 > R_1$ (red), is traversed clockwise, so that the region "outside", which contains $\infty$, is on its left. Between $C$ and $C_0$ the function is analytic, which is why $\int_C f\,dz = -\int_{C_0} f\,dz$.*

> [!remark]- Connections
> - Adding a point $\infty$ to $\mathbb{C}$, with the complements of compact sets as its neighborhoods, is the one-point compactification, [[§17 Local Compactness#^def-17-2|590 Def. §17.2]]: the Riemann sphere. The substitution $z \mapsto 1/z$ is the chart at $\infty$, and the factor $1/z^2$ is $-\frac{d}{dz}(1/z)$, the change of variable for $dz$; this is why the residue at infinity is not simply the residue of $f(1/z)$ at $0$.

With equations (2) and (6), the following theorem is established. It is sometimes more efficient to use than Cauchy's residue theorem, since it involves only one residue.

> [!theorem] Theorem §77.2: The Integral as a Single Residue
> If a function $f$ is analytic everywhere in the finite plane except for a finite number of singular points interior to a positively oriented simple closed contour $C$, then
>
> $$
> \int_C f(z)\,dz = 2\pi i\operatorname{Res}_{z=0}\Big[\frac{1}{z^2}f\Big(\frac1z\Big)\Big] . \qquad (7)
> $$
>
> *B&C: Sec. 77, Theorem*

^thm-77-2

> [!proof]+ Proof
> By (2) and (6) of [[§77★ Residue at Infinity#^prop-77-1|Proposition §77.1]],
>
> $$
> \int_C f(z)\,dz = -2\pi i\operatorname{Res}_{z=\infty} f(z) = -2\pi i\Big(-\operatorname{Res}_{z=0}\Big[\frac{1}{z^2}f\Big(\frac1z\Big)\Big]\Big) = 2\pi i\operatorname{Res}_{z=0}\Big[\frac{1}{z^2}f\Big(\frac1z\Big)\Big] .
> $$

^pf-77-2

*Uses:* [[§77★ Residue at Infinity#^prop-77-1|§77.1]]

> [!theorem] Corollary §77.3: The Residues Add Up to Zero
> Suppose that $f$ is analytic throughout the finite plane except for a finite number of singular points $z_1, z_2, \ldots, z_n$. Then
>
> $$
> \operatorname{Res}_{z=z_1} f(z) + \operatorname{Res}_{z=z_2} f(z) + \cdots + \operatorname{Res}_{z=z_n} f(z) + \operatorname{Res}_{z=\infty} f(z) = 0 .
> $$
>
> *B&C: Sec. 77, Exercise 6; Source: 342 HW 11 (optional)*

^cor-77-3

> [!proof]+ Proof
> Let $C$ be a positively oriented circle $|z| = R$ with $R > |z_k|$ for every $k$. Then $f$ is analytic inside and on $C$ except at $z_1, \ldots, z_n$, all inside $C$, so by Cauchy's residue theorem $\int_C f(z)\,dz = 2\pi i\sum_{k=1}^{n}\operatorname{Res}_{z=z_k} f(z)$. By (2) of Proposition §77.1, also $\int_C f(z)\,dz = -2\pi i\operatorname{Res}_{z=\infty} f(z)$. Equating the two expressions and dividing by $2\pi i$ gives the claim.

^pf-77-3

*Uses:* [[§76 Cauchy's Residue Theorem#^thm-76-1|§76.1]], [[§77★ Residue at Infinity#^prop-77-1|§77.1]]

> [!theorem] Corollary §77.4: Rational Functions With a High-Degree Denominator
> Let
>
> $$
> P(z) = a_0 + a_1z + a_2z^2 + \cdots + a_nz^n \quad (a_n \ne 0), \qquad Q(z) = b_0 + b_1z + b_2z^2 + \cdots + b_mz^m \quad (b_m \ne 0)
> $$
>
> be polynomials with $m \ge n + 2$. If all the zeros of $Q(z)$ are interior to a simple closed contour $C$, then
>
> $$
> \int_C \frac{P(z)}{Q(z)}\,dz = 0 .
> $$
>
> *B&C: Sec. 77, Exercise 7; Source: 342 HW 11 (optional)*

^cor-77-4

> [!proof]+ Proof
> We may take $C$ positively oriented (reversing the orientation only changes the sign of $0$). The function $f = P/Q$ is analytic in the finite plane except at the zeros of $Q$, which are finitely many and interior to $C$, so Theorem §77.2 applies. For $z \ne 0$,
>
> $$
> P\Big(\frac1z\Big) = \frac{a_n + a_{n-1}z + \cdots + a_0z^n}{z^n}, \qquad Q\Big(\frac1z\Big) = \frac{b_m + b_{m-1}z + \cdots + b_0z^m}{z^m} ,
> $$
>
> so
>
> $$
> \frac{1}{z^2}f\Big(\frac1z\Big) = z^{m-n-2}\,\frac{a_n + a_{n-1}z + \cdots + a_0z^n}{b_m + b_{m-1}z + \cdots + b_0z^m} .
> $$
>
> Since $m - n - 2 \ge 0$ and the denominator tends to $b_m \ne 0$ as $z \to 0$, the right side is analytic at $z = 0$ (once the value at $0$ is assigned by continuity): its Laurent series about $0$ is a Taylor series, with no term in $1/z$. Hence $\operatorname{Res}_{z=0}\big[\frac{1}{z^2}f(\frac1z)\big] = 0$, and by (7) the integral is $0$.

^pf-77-4

*Uses:* [[§77★ Residue at Infinity#^thm-77-2|§77.2]], [[§75 Residues#^def-75-1|Def. §75.1]]

> [!remark] Remark: Method — One Residue Instead of Many
> 1. **Check the hypothesis:** every singular point of $f$ in the finite plane lies inside the positively oriented contour $C$.
> 2. **Substitute** $z \mapsto 1/z$ and form $g(z) = \frac{1}{z^2}f\big(\frac1z\big)$; simplify by multiplying numerator and denominator by a power of $z$.
> 3. **Find $\operatorname{Res}_{z=0} g$**: if $g = \frac1z\,h(z)$ with $h$ analytic at $0$, the residue is $h(0)$; if $g$ is analytic at $0$, it is $0$.
> 4. $\int_C f(z)\,dz = 2\pi i\operatorname{Res}_{z=0} g(z)$ (Theorem §77.2).
>
> The method pays off when $f$ has many singular points inside $C$ (roots of $z^n = c$, say) and is useless when some singular point lies outside $C$.

^rem-77-1

## Examples

> [!example] Example §77.1: Five Singular Points, One Residue
> The singularities of
>
> $$
> f(z) = \frac{z^3(1 - 3z)}{(1 + z)(1 + 2z^4)}
> $$
>
> all lie inside the positively oriented circle $C\colon |z| = 3$: they are $z = -1$ and the four roots of $z^4 = -\frac12$, of modulus $2^{-1/4} < 1$. To use Theorem §77.2, write
>
> $$
> \frac{1}{z^2}f\Big(\frac1z\Big) = \frac{1}{z^2}\cdot\frac{z^{-3}(1 - 3z^{-1})}{(1 + z^{-1})(1 + 2z^{-4})} = \frac{1}{z^2}\cdot\frac{z^{-4}(z - 3)}{z^{-5}(z + 1)(z^4 + 2)} = \frac1z\cdot\frac{z - 3}{(z + 1)(z^4 + 2)} . \qquad (8)
> $$
>
> The quotient $\dfrac{z - 3}{(z + 1)(z^4 + 2)}$ is analytic at the origin, so it has a Maclaurin series whose first term is its value at $0$, the nonzero number $\frac{-3}{1 \cdot 2} = -\frac32$. Hence, by (8),
>
> $$
> \frac{1}{z^2}f\Big(\frac1z\Big) = \frac1z\Big(-\frac32 + a_1z + a_2z^2 + a_3z^3 + \cdots\Big) = -\frac32\cdot\frac1z + a_1 + a_2z + a_3z^2 + \cdots
> $$
>
> in some punctured disk $0 < |z| < R_0$. It is now clear that
>
> $$
> \operatorname{Res}_{z=0}\Big[\frac{1}{z^2}f\Big(\frac1z\Big)\Big] = -\frac32, \qquad\text{and so}\qquad \int_C \frac{z^3(1 - 3z)}{(1 + z)(1 + 2z^4)}\,dz = 2\pi i\Big(-\frac32\Big) = -3\pi i . \qquad (9)
> $$
>
> *B&C: Sec. 77, Example*

^ex-77-1

> [!example] Example §77.2: Roots of Unity Inside a Circle
> Evaluate the integral of each function around the positively oriented circle $C\colon |z| = 2$:
>
> $$
> \text{(a)}\ \frac{z^5}{1 - z^3}; \qquad \text{(b)}\ \frac{1}{1 + z^2} .
> $$
>
> **(a)** The singular points are the three cube roots of unity $1, e^{2\pi i/3}, e^{4\pi i/3}$, all of modulus $1$ and inside $C$. Then
>
> $$
> \frac{1}{z^2}f\Big(\frac1z\Big) = \frac{1}{z^2}\cdot\frac{z^{-5}}{1 - z^{-3}} = \frac{1}{z^2}\cdot\frac{z^{-2}}{z^3 - 1} = -\frac{1}{z^4}\cdot\frac{1}{1 - z^3} = -\frac{1}{z^4}\big(1 + z^3 + z^6 + \cdots\big) = -\frac{1}{z^4} - \frac1z - z^2 - \cdots
> $$
>
> for $0 < |z| < 1$. The residue at $0$ is $-1$, so $\displaystyle\int_C \frac{z^5}{1 - z^3}\,dz = -2\pi i$.
>
> *Check by Cauchy's residue theorem.* Each cube root $\omega$ of unity is a simple zero of $1 - z^3$ (the derivative $-3z^2$ is nonzero there), and by the quotient rule [[§83 Zeros and Poles#^thm-83-2|Theorem §83.2]] the residue is $\dfrac{\omega^5}{-3\omega^2} = -\dfrac{\omega^3}{3} = -\dfrac13$. Three residues of $-\frac13$ give $2\pi i(-1) = -2\pi i$ again.
>
> **(b)** The singular points $\pm i$ lie inside $C$, and
>
> $$
> \frac{1}{z^2}f\Big(\frac1z\Big) = \frac{1}{z^2}\cdot\frac{1}{1 + z^{-2}} = \frac{1}{z^2 + 1} ,
> $$
>
> which is analytic at $0$. The residue is $0$ and $\displaystyle\int_C \frac{dz}{1 + z^2} = 0$, as [[§77★ Residue at Infinity#^cor-77-4|Corollary §77.4]] predicts ($m = 2 \ge 0 + 2$).
>
> *B&C: Sec. 77, Exercise 4(a)–(b); Source: 342 HW 11 (optional); 342 practice final (Spring 2005), Q3*

^ex-77-2

> [!example] Example §77.3: The Example of §76 With One Residue
> Evaluate $\displaystyle\int_C \frac{4z - 5}{z(z - 1)}\,dz$ over the positively oriented circle $|z| = 2$ ([[§76 Cauchy's Residue Theorem#^ex-76-1|Example §76.1]]) by finding only one residue.
>
> Both singular points $0$ and $1$ lie inside $C$. With $f(z) = \dfrac{4z - 5}{z(z - 1)}$,
>
> $$
> \frac{1}{z^2}f\Big(\frac1z\Big) = \frac{1}{z^2}\cdot\frac{4z^{-1} - 5}{z^{-1}(z^{-1} - 1)} = \frac{1}{z^2}\cdot\frac{z(4 - 5z)}{1 - z} = \frac1z\cdot\frac{4 - 5z}{1 - z} .
> $$
>
> The factor $\frac{4 - 5z}{1 - z}$ is analytic at $0$ with value $4$ there, so the residue at $0$ is $4$ and
>
> $$
> \int_C \frac{4z - 5}{z(z - 1)}\,dz = 2\pi i\cdot 4 = 8\pi i ,
> $$
>
> in agreement with §76, where the two residues $5$ and $-1$ were found. Consistently with [[§77★ Residue at Infinity#^cor-77-3|Corollary §77.3]], $\operatorname{Res}_{z=\infty} f = -4 = -(5 + (-1))$.
>
> *B&C: Sec. 77, Exercise 3*

^ex-77-3
