---
type: section
subject: "[[Complex Variables]]"
chapter: 7
section: 95
bc: "95"
aliases: ["B&C 95"]
tags: [complex-variables, math342, extension]
---
← [[§94 Rouché's Theorem]] · ↑ [[· 7 Applications of Residues]] · [[§96★ Linear Transformations]] →

*Brown–Churchill, Section 95.*
★ *Beyond MAT 342: the course skipped this section or left it optional; it is included from Brown–Churchill.*

A Laplace transform $F(s) = \int_0^\infty e^{-st}f(t)\,dt$ can be inverted by an integral along a vertical line in the complex $s$ plane, the **Bromwich integral**. When $F$ is analytic except for isolated singular points to the left of the line, the line can be closed by a large semicircle on the left, and the residue theorem turns the inverse transform into the sum of the residues of $e^{st}F(s)$; with infinitely many poles, as in heat and wave problems, into a series of residues. B&C gives this only formally: "it can be shown" that the Bromwich integral is the inverse transform, and the vanishing of the semicircle integral is assumed. This note supplies the proofs: the semicircle estimate (Jordan's inequality again), the residue formulas (6) and (7) under stated conditions, the inversion theorem (from the Fourier integral theorem), uniqueness of the inverse transform, and, for rational $F$, a complete proof that the residue sum is the inverse transform. These are the results behind the inverse-transform tables of ODE and the extended Heaviside formula of Fourier Series and PDEs.

## The Bromwich Integral

Suppose a function $F$ of the complex variable $s$ is analytic throughout the finite $s$ plane except for a finite number of isolated singularities $s_1, \ldots, s_N$. Let $L_R$ be the vertical segment from $s = \gamma - iR$ to $s = \gamma + iR$, where the constant $\gamma$ is positive and large enough that the singularities all lie to the left of it, $\operatorname{Re}s_n < \gamma$; and let $C_R$ be the left semicircle $s = \gamma + Re^{i\theta}$ $(\pi/2 \le \theta \le 3\pi/2)$, from $\gamma + iR$ to $\gamma - iR$.

> [!definition] Definition §95.1: Bromwich Integral
> The function $f$ of the real variable $t$ defined for $t > 0$ by
>
> $$
> f(t) = \frac{1}{2\pi i}\lim_{R\to\infty}\int_{L_R} e^{st}F(s)\,ds \qquad (t > 0), \qquad (1)
> $$
>
> provided this limit exists, is usually written
>
> $$
> f(t) = \frac{1}{2\pi i}\,\text{P.V.}\int_{\gamma - i\infty}^{\gamma + i\infty} e^{st}F(s)\,ds \qquad (t > 0) \qquad (2)
> $$
>
> (a principal value as in [[§85 Evaluation of Improper Integrals#^def-85-2|Definition §85.2]]), and such an integral is called a **Bromwich integral**.
>
> *B&C: Sec. 95, equations (1)–(2)*

^def-95-1

The **Laplace transform** of a function $f(t)$, $t \ge 0$, is

$$
F(s) = \int_0^\infty e^{-st}f(t)\,dt , \qquad (3)
$$

now for complex $s$. If $f$ is piecewise continuous on every finite interval and $|f(t)| \le Ke^{at}$ for $t \ge 0$, the integral converges absolutely for $\operatorname{Re}s > a$, since $|e^{-st}f(t)| \le Ke^{-(\operatorname{Re}s - a)t}$; this is the proof of [[§21 Definition of the Laplace Transform#^thm-21-2|331 Thm. §21.2]] with $\operatorname{Re}s$ in place of $s$. B&C states that "when fairly general conditions are imposed", the Bromwich integral (2) of the transform $F$ returns $f$; Theorem §95.4 below is such a statement. The computation rests on the residue theorem on the closed contour $L_R + C_R$:

$$
\int_{L_R} e^{st}F(s)\,ds = 2\pi i\sum_{n=1}^{N}\operatorname{Res}_{s=s_n}\big[e^{st}F(s)\big] - \int_{C_R} e^{st}F(s)\,ds . \qquad (4)
$$

![[m342-95-1.svg]]
*The contour of B&C's Figure 115: the Bromwich segment $L_R$ on the line $\operatorname{Re}s = \gamma$, to the right of all singular points $s_n$ (green), closed on the left by the semicircle $C_R$ of radius $R$ about $\gamma$. For $t > 0$, $|e^{st}| = e^{t\operatorname{Re}s}$ is small far to the left, which is why the contour is closed on that side.*

## Closing the Contour to the Left

> [!theorem] Lemma §95.1: The Left Semicircle
> Let $C_R$ be the semicircle $s = \gamma + Re^{i\theta}$ $(\pi/2 \le \theta \le 3\pi/2)$, let $F$ be continuous on $C_R$ with $|F(s)| \le M_R$ there, and let $t > 0$. Then
>
> $$
> \Big|\int_{C_R} e^{st}F(s)\,ds\Big| < \frac{\pi M_Re^{\gamma t}}{t} .
> $$
>
> Consequently, if $M_R \to 0$ as $R \to \infty$, then for every $t > 0$
>
> $$
> \lim_{R\to\infty}\int_{C_R} e^{st}F(s)\,ds = 0 . \qquad (5)
> $$
>
> *B&C: Sec. 95, limit (5) (assumed there; the estimate is added here)*

^lem-95-1

> [!proof]+ Proof
> On $C_R$, $ds = iRe^{i\theta}\,d\theta$ and $|e^{st}| = e^{t\operatorname{Re}s} = e^{\gamma t}e^{tR\cos\theta}$. Hence
>
> $$
> \Big|\int_{C_R} e^{st}F(s)\,ds\Big| \le M_Re^{\gamma t}R\int_{\pi/2}^{3\pi/2} e^{tR\cos\theta}\,d\theta = M_Re^{\gamma t}R\int_0^{\pi} e^{-tR\sin\varphi}\,d\varphi ,
> $$
>
> by the substitution $\theta = \varphi + \pi/2$, $\cos\theta = -\sin\varphi$. By Jordan's inequality ([[§88★ Jordan's Lemma#^lem-88-1|Lemma §88.1]], with $tR > 0$ in place of $R$) the last integral is less than $\pi/(tR)$, which gives the bound. For fixed $t > 0$ it tends to $0$ when $M_R \to 0$.

^pf-95-1

*Uses:* [[§88★ Jordan's Lemma#^lem-88-1|§88.1]], [[§42 Definite Integrals of Functions w(t)|§42]], [[§44 Contour Integrals|§44]]

This is Jordan's lemma ([[§88★ Jordan's Lemma#^thm-88-2|Theorem §88.2]]) turned through a right angle: there $e^{iaz}$ decays in the upper half plane, here $e^{st}$ decays in the left half plane. As there, $M_R \to 0$ suffices; the length $\pi R$ of the semicircle does not enter.

> [!theorem] Theorem §95.2: Inverse Transform as a Sum of Residues
> Let $F$ be analytic in the finite plane except for isolated singular points $s_1, \ldots, s_N$, all with $\operatorname{Re}s_n < \gamma$, and suppose that $|F(s)| \le M_R$ on $C_R$ with $M_R \to 0$ as $R \to \infty$. Then for every $t > 0$ the limit (1) exists, and
>
> $$
> f(t) = \sum_{n=1}^{N}\operatorname{Res}_{s=s_n}\big[e^{st}F(s)\big] \qquad (t > 0) . \qquad (6)
> $$
>
> *B&C: Sec. 95, equations (4)–(6)*

^thm-95-2

> [!proof]+ Proof
> Let $R > \max_n|s_n - \gamma|$. Then every $s_n$ lies inside the closed contour formed by $L_R$ (upward) and $C_R$: it is in the disk $|s - \gamma| < R$ and to the left of the line $\operatorname{Re}s = \gamma$. The function $e^{st}F(s)$ is analytic inside and on this positively oriented contour except at the $s_n$ ($e^{st}$ is entire), and Cauchy's residue theorem ([[§76 Cauchy's Residue Theorem|§76]]) gives (4). By Lemma §95.1 the last term of (4) tends to $0$ as $R \to \infty$. Hence $\lim_{R\to\infty}\int_{L_R} e^{st}F(s)\,ds$ exists and equals $2\pi i\sum_n\operatorname{Res}_{s=s_n}[e^{st}F(s)]$; dividing by $2\pi i$ gives (6).

^pf-95-2

*Uses:* [[§95★ Inverse Laplace Transforms#^lem-95-1|§95.1]], [[§95★ Inverse Laplace Transforms#^def-95-1|Def. §95.1]], [[§76 Cauchy's Residue Theorem|§76]] (Theorem)

In heat conduction and vibration problems $F(s)$ typically has infinitely many isolated singular points $s_n$, all to the left of some line $\operatorname{Re}s = \gamma$, and the finite sum (6) is replaced by a series of residues (7). B&C states this without conditions; the following version makes the passage to the limit along a suitable sequence of semicircles precise.

> [!theorem] Theorem §95.3: Inverse Transform as a Series of Residues
> Let $F$ be analytic in the finite plane except for isolated singular points $s_1, s_2, \ldots$, all with $\operatorname{Re}s_n < \gamma$. Suppose there are radii $R_1 < R_2 < \cdots \to \infty$ such that no $s_n$ lies on the semicircles $C_{R_N}$ and $|F(s)| \le M_N$ on $C_{R_N}$, with $M_N \to 0$. Then for every $t > 0$
>
> $$
> \frac{1}{2\pi i}\lim_{N\to\infty}\int_{L_{R_N}} e^{st}F(s)\,ds = \lim_{N\to\infty}\sum_{|s_n - \gamma| < R_N}\operatorname{Res}_{s=s_n}\big[e^{st}F(s)\big] ,
> $$
>
> both limits existing. In this sense
>
> $$
> f(t) = \sum_{n=1}^{\infty}\operatorname{Res}_{s=s_n}\big[e^{st}F(s)\big] \qquad (t > 0), \qquad (7)
> $$
>
> with the terms grouped by the semicircles.
>
> *B&C: Sec. 95, equation (7)*

^thm-95-3

> [!proof]+ Proof
> **Finitely many $s_n$ in each disk.** If infinitely many $s_n$ lay in a bounded set, they would accumulate at some point $s^*$ (Bolzano–Weierstrass). $F$ is not analytic at $s^*$, since every neighborhood of $s^*$ contains singular points; so $s^*$ is one of the singular points, and it is not isolated, contrary to the hypothesis. So only finitely many $s_n$ satisfy $|s_n - \gamma| < R_N$.
>
> **The limit.** For each $N$ the singular points inside the closed contour $L_{R_N} + C_{R_N}$ are exactly those with $|s_n - \gamma| < R_N$ (all have $\operatorname{Re}s_n < \gamma$, and none lies on $C_{R_N}$). As in the proof of Theorem §95.2, the residue theorem gives
>
> $$
> \frac{1}{2\pi i}\int_{L_{R_N}} e^{st}F(s)\,ds = \sum_{|s_n - \gamma| < R_N}\operatorname{Res}_{s=s_n}\big[e^{st}F(s)\big] - \frac{1}{2\pi i}\int_{C_{R_N}} e^{st}F(s)\,ds ,
> $$
>
> and by Lemma §95.1 the last term is less than $M_Ne^{\gamma t}/(2t)$ in modulus, which tends to $0$. So the two limits exist together and are equal.

^pf-95-3

*Uses:* [[§95★ Inverse Laplace Transforms#^lem-95-1|§95.1]], [[§95★ Inverse Laplace Transforms#^thm-95-2|§95.2]], [[§76 Cauchy's Residue Theorem|§76]] (Theorem)

## The Bromwich Integral Inverts the Transform

Theorems §95.2 and §95.3 evaluate the Bromwich integral; that its value is the function whose transform is $F$ is a separate statement, which B&C leaves at "it can be shown". It is the Fourier integral theorem in disguise. Call $f$ **sectionally smooth** on $[0, \infty)$ if it is sectionally smooth on every finite interval ([[§8 Convergence of Fourier Series#^def-8-4|341 Def. §8.4]]).

> [!theorem] Theorem §95.4: Inversion by the Bromwich Integral
> Let $f$ be sectionally smooth on $[0, \infty)$ with $|f(t)| \le Ke^{at}$ for $t \ge 0$, and let $F$ be its Laplace transform (3), $\operatorname{Re}s > a$. Then for every $\gamma > a$ and every $t > 0$,
>
> $$
> \frac{1}{2\pi i}\lim_{R\to\infty}\int_{L_R} e^{st}F(s)\,ds = \frac12\big(f(t+) + f(t-)\big) .
> $$
>
> In particular the Bromwich integral (2) equals $f(t)$ at every $t > 0$ where $f$ is continuous.
>
> *B&C: Sec. 95 (text) ("it can be shown"); B&C omits the proof*

^thm-95-4

> [!proof]+ Proof
> Let $g(\tau) = e^{-\gamma\tau}f(\tau)$ for $\tau > 0$ and $g(\tau) = 0$ for $\tau < 0$. Then $g$ is sectionally smooth on every finite interval (the jump at $\tau = 0$ is allowed), and
>
> $$
> \int_{-\infty}^{\infty}|g(\tau)|\,d\tau \le K\int_0^\infty e^{-(\gamma - a)\tau}\,d\tau = \frac{K}{\gamma - a} < \infty .
> $$
>
> So $g$ satisfies the hypotheses of the Fourier integral theorem, and its complex coefficient function ([[§15★ Complex Methods#^def-15-2|341 Def. §15.2]]) is
>
> $$
> C(\lambda) = \frac{1}{2\pi}\int_{-\infty}^{\infty} g(\tau)e^{-i\lambda\tau}\,d\tau = \frac{1}{2\pi}\int_0^\infty e^{-(\gamma + i\lambda)\tau}f(\tau)\,d\tau = \frac{1}{2\pi}F(\gamma + i\lambda) .
> $$
>
> Parametrize $L_R$ by $s = \gamma + i\lambda$ $(-R \le \lambda \le R)$, $ds = i\,d\lambda$:
>
> $$
> \frac{1}{2\pi i}\int_{L_R} e^{st}F(s)\,ds = \frac{1}{2\pi}\int_{-R}^{R} e^{(\gamma + i\lambda)t}F(\gamma + i\lambda)\,d\lambda = e^{\gamma t}\int_{-R}^{R} C(\lambda)e^{i\lambda t}\,d\lambda .
> $$
>
> By the complex form of the Fourier integral theorem ([[§15★ Complex Methods#^thm-15-2|341 Thm. §15.2]]), as $R \to \infty$ the right side tends to $e^{\gamma t}\cdot\frac12\big(g(t+) + g(t-)\big)$, and for $t > 0$ this is $\frac12\big(f(t+) + f(t-)\big)$, because $e^{-\gamma\tau}$ is continuous.

^pf-95-4

*Uses:* [[§95★ Inverse Laplace Transforms#^def-95-1|Def. §95.1]], [[§15★ Complex Methods#^thm-15-2|341 Thm. §15.2]], [[§15★ Complex Methods#^def-15-2|341 Def. §15.2]], [[§14 Fourier Integral#^thm-14-1|341 Thm. §14.1]]

*The proof is complete relative to the Fourier integral theorem, [[§14 Fourier Integral#^thm-14-1|341 Thm. §14.1]], which the vault states without proof. For rational $F$, Theorem §95.6 below proves the inversion directly, without it.*

> [!remark]- Connections
> - BDP mentions this formula only as "a general formula for the inverse transform [that] requires functions of a complex variable", [[§22 Solution of Initial Value Problems#^def-22-1|331 Def. §22.1]]; Theorem §95.4 is that formula. At $t = 0$ the same computation gives $\frac12f(0+)$, and for $t < 0$ it gives $0$: the Bromwich integral reproduces $f$ extended by zero to negative times.

> [!theorem] Corollary §95.5: Uniqueness of the Inverse Transform
> Let $f_1$ and $f_2$ be sectionally smooth on $[0, \infty)$ with $|f_j(t)| \le Ke^{at}$, and suppose their Laplace transforms agree for all real $s > a$. Then $f_1(t) = f_2(t)$ at every $t > 0$ where both are continuous; more precisely, $f_1(t+) + f_1(t-) = f_2(t+) + f_2(t-)$ for all $t > 0$.
>
> *B&C: Sec. 95 (text) ("$f(t)$ is retrieved by means of equation (2)")*

^cor-95-5

> [!proof]+ Proof
> **$F_j$ is analytic in $\operatorname{Re}s > a$.** Fix $s$ with $\sigma = \operatorname{Re}s > a$, let $\delta = \frac12(\sigma - a)$ and $0 < |h| \le \delta$. From the power series of the exponential, $|e^w - 1 - w| \le \sum_{k\ge2}|w|^k/k! \le \frac12|w|^2e^{|w|}$ for complex $w$; with $w = -ht$,
>
> $$
> \Big|\frac{F_j(s + h) - F_j(s)}{h} + \int_0^\infty te^{-st}f_j(t)\,dt\Big| \le \int_0^\infty e^{-\sigma t}|f_j(t)|\,\frac{|h|t^2e^{\delta t}}{2}\,dt \le \frac{|h|K}{2}\int_0^\infty t^2e^{-\delta t}\,dt = \frac{|h|K}{\delta^3} ,
> $$
>
> which tends to $0$ with $h$. So $F_j'(s)$ exists for every $s$ in the half plane: $F_j$ is analytic there. (This is the argument of [[§22 Solution of Initial Value Problems#^thm-22-6|331 Thm. §22.6]], entry 19, with complex $h$.)
>
> **Conclusion.** $F_1 - F_2$ is analytic in the domain $\operatorname{Re}s > a$ and vanishes on the segment $a + 1 \le s \le a + 2$ of the real axis, so it vanishes identically ([[§28★ Uniquely Determined Analytic Functions|§28★]], Lemma). In particular $F_1 = F_2$ on the line $\operatorname{Re}s = a + 1$, and Theorem §95.4 with $\gamma = a + 1$ gives $\frac12\big(f_1(t+) + f_1(t-)\big) = \frac12\big(f_2(t+) + f_2(t-)\big)$ for $t > 0$.

^pf-95-5

*Uses:* [[§95★ Inverse Laplace Transforms#^thm-95-4|§95.4]], [[§28★ Uniquely Determined Analytic Functions|§28★]] (Lemma), [[§19 Derivatives|§19]]

> [!remark]- Connections
> - This is Lerch's theorem, [[§22 Solution of Initial Value Problems#^thm-22-4|331 Thm. §22.4]], which BDP states without proof ("it can be shown"), here proved for sectionally smooth functions of exponential order (relative to the Fourier integral theorem). It is what makes a table of transforms, read backwards, a table of inverse transforms.

## Rational Transforms

For rational $F$ everything can be proved from scratch: the residue sum is an explicit function whose transform is $F$.

> [!theorem] Theorem §95.6: Inverse Transform of a Rational Function
> Let $F = P/Q$ with polynomials $P$, $Q$ without common factors and $\deg P < \deg Q$, and let $s_1, \ldots, s_N$ be the distinct zeros of $Q$, of orders $m_1, \ldots, m_N$. Then:
>
> **(a)** $F$ has the partial fraction decomposition
>
> $$
> F(s) = \sum_{n=1}^{N}\sum_{k=1}^{m_n}\frac{c_{n,k}}{(s - s_n)^k} ,
> $$
>
> where $\sum_k c_{n,k}(s - s_n)^{-k}$ is the principal part of $F$ at $s_n$.
>
> **(b)** For all real $t$,
>
> $$
> f(t) := \sum_{n=1}^{N}\operatorname{Res}_{s=s_n}\big[e^{st}F(s)\big] = \sum_{n=1}^{N}\sum_{k=1}^{m_n} c_{n,k}\,\frac{t^{k-1}}{(k - 1)!}\,e^{s_nt} .
> $$
>
> **(c)** The function $f$ is continuous and of exponential order, and its Laplace transform is $F(s)$ for $\operatorname{Re}s > \max_n\operatorname{Re}s_n$.
>
> **(d)** For every $\gamma > \max_n\operatorname{Re}s_n$ and $t > 0$, the Bromwich integral (1) exists and equals $f(t)$.
>
> *B&C: Sec. 95, equation (6), for rational $F$ (B&C's Example and Exercises 1–3 are of this kind)*

^thm-95-6

> [!proof]+ Proof
> Each $s_n$ is a pole of order $m_n$ of $F$ ([[§83 Zeros and Poles|§83]], Theorem 1), and $F$ is analytic elsewhere.
>
> **(a)** Let $P_n(s) = \sum_{k=1}^{m_n} c_{n,k}(s - s_n)^{-k}$ be the principal part of the Laurent series of $F$ at $s_n$ ([[§66 Laurent Series|§66]]). Then $F - P_n$ is analytic at $s_n$ (its Laurent series there has no negative powers), and the other $P_j$ are analytic at $s_n$. So $G = F - \sum_n P_n$, once its removable singularities at the $s_n$ are filled in, is entire. As $|s| \to \infty$, $F(s) \to 0$ (since $\deg P < \deg Q$) and each $P_n(s) \to 0$; so $G(s) \to 0$. Hence $G$ is bounded (by $1$ outside some disk, and on that closed disk by continuity), so it is constant by Liouville's theorem ([[§58 Liouville's Theorem and the Fundamental Theorem of Algebra|§58]], Theorem 1), and the constant is its limit $0$.
>
> **(b)** Near $s_n$, $e^{st}F(s) = e^{st}P_n(s) + e^{st}\big(F(s) - P_n(s)\big)$, and the second term is analytic at $s_n$, so $\operatorname{Res}_{s_n}[e^{st}F] = \operatorname{Res}_{s_n}[e^{st}P_n]$. From $e^{st} = e^{s_nt}e^{(s - s_n)t} = e^{s_nt}\sum_{j\ge0}\frac{t^j}{j!}(s - s_n)^j$, the coefficient of $(s - s_n)^{-1}$ in $e^{st}(s - s_n)^{-k}$ is $e^{s_nt}t^{k-1}/(k - 1)!$. Summing over $k$ with the weights $c_{n,k}$ gives (b).
>
> **(c)** Each term $t^{k-1}e^{s_nt}$ is continuous and $|t^{k-1}e^{s_nt}| \le Ce^{(\operatorname{Re}s_n + 1)t}$ for $t \ge 0$. For $w$ with $\operatorname{Re}w > 0$ and $j = 0, 1, 2, \ldots$,
>
> $$
> \int_0^\infty t^je^{-wt}\,dt = \frac{j!}{w^{j+1}} :
> $$
>
> for $j = 0$ the integral is $\big[-e^{-wt}/w\big]_0^\infty = 1/w$, since $|e^{-wt}| = e^{-t\operatorname{Re}w} \to 0$; and integration by parts gives $\int_0^\infty t^je^{-wt}\,dt = \frac jw\int_0^\infty t^{j-1}e^{-wt}\,dt$, the boundary term $t^je^{-wt}$ vanishing at both ends. With $w = s - s_n$ and $j = k - 1$, the transform of $\frac{t^{k-1}}{(k-1)!}e^{s_nt}$ is $(s - s_n)^{-k}$ for $\operatorname{Re}s > \operatorname{Re}s_n$. By linearity and (a), the transform of $f$ is $F$.
>
> **(d)** Since $\deg Q \ge \deg P + 1$, there is $K$ with $|F(s)| \le K/|s|$ for $|s|$ large (as in [[§85 Evaluation of Improper Integrals#^prop-85-4|Proposition §85.4]]). On $C_R$, $|s| \ge R - \gamma$, so $|F| \le M_R = K/(R - \gamma) \to 0$, and Theorem §95.2 applies: the Bromwich integral exists and equals the residue sum $f(t)$.

^pf-95-6

*Uses:* [[§95★ Inverse Laplace Transforms#^thm-95-2|§95.2]], [[§83 Zeros and Poles|§83]] (Theorem 1), [[§66 Laurent Series|§66]], [[§58 Liouville's Theorem and the Fundamental Theorem of Algebra|§58]] (Theorem 1), [[§85 Evaluation of Improper Integrals#^prop-85-4|§85.4]], [[§22 Solution of Initial Value Problems#^thm-22-6|331 Thm. §22.6]] (entry 11)

> [!remark]- Connections
> - Part (c) is entry 11 of the table, $\mathcal{L}\{t^ne^{at}\} = n!/(s - a)^{n+1}$, [[§22 Solution of Initial Value Problems#^thm-22-6|331 Thm. §22.6]], extended to complex $a$; part (a) is the partial fraction decomposition used in [[§22 Solution of Initial Value Problems#^rem-22-4|331 Remark: Method — Inverting a Rational Transform]], proved here by Liouville's theorem (for real factors: [[§47 Integration of Rational Functions by Partial Fractions#^thm-47-3|Calc Thm. §47.3]]). At simple poles the residues are $P(s_n)/Q'(s_n)\,e^{s_nt}$, which is Heaviside's formula, [[§52★ Partial Fractions and Convolutions#^thm-52-2|341 Thm. §52.2]]; at a double pole, [[§54★ More Difficult Examples#^prop-54-2|341 Prop. §54.2]].

> [!remark] Remark: Why the Extended Heaviside Formula Works
> In [[§53★ Partial Differential Equations#^rem-53-3|341 Remark: Why It Works]], the solution $u(x, t)$ of a heat or wave problem is recovered from its transform $U(x, s)$ by summing the terms $A_n(x)e^{r_nt}$, the residues of $e^{st}U(x, s)$ at its poles $r_n$. The results above make this precise, for each fixed $x$:
> - If $u(x, \cdot)$ is sectionally smooth and of exponential order, Theorem §95.4 says that the Bromwich integral of $U(x, \cdot)$ returns $u(x, t)$.
> - If $U(x, \cdot)$ is a single-valued function of $s$ with only isolated singular points to the left of $\operatorname{Re}s = \gamma$, and is small on a sequence of semicircles $C_{R_N}$ passing between the poles, Theorem §95.3 evaluates that Bromwich integral as the series of residues, grouped by the semicircles.
>
> Together, $u(x, t) = \sum_n\operatorname{Res}_{s=r_n}[e^{st}U(x, s)]$, which is the extended Heaviside formula. Example §95.3 shows how the condition on the semicircles is checked for a denominator $\sinh s$; for $\sinh\sqrt s$, as in [[§53★ Partial Differential Equations#^ex-53-3|341 Ex. §53.3]], a similar estimate of $\sinh w$, $w = \sqrt s$, on curves passing between the poles $-n^2\pi^2$ is needed (it is not carried out here). When $U$ is not single-valued (a branch point at $s = 0$ from $e^{-\sqrt s\,x}$), the contour must avoid the branch cut, as in [[§91★ Integration Along a Branch Cut|§91★]], and the inverse transform contains an integral along the cut besides the residues.

^rem-95-1

> [!remark] Remark: Method — Inverse Laplace Transforms by Residues
> To find $f = \mathcal{L}^{-1}\{F\}$:
> 1. **Singular points.** Locate the poles $s_n$ of $F$ (zeros of the denominator not cancelled by the numerator; check that a candidate is not removable).
> 2. **Residues** of $e^{st}F(s)$: at a simple pole $\frac{p(s_n)}{q'(s_n)}e^{s_nt}$ for $F = p/q$; at a pole of order $m$, $\frac{1}{(m-1)!}\frac{d^{m-1}}{ds^{m-1}}\big[(s - s_n)^me^{st}F(s)\big]_{s=s_n}$, which produces the factors $t^{k}e^{s_nt}$.
> 3. **Conjugate pairs.** For real $F$ the residues at $s_n$ and $\bar s_n$ are conjugate: add them as $2\operatorname{Re}$ of one of them.
> 4. **Sum** (or, with infinitely many poles, sum in groups and examine convergence).
> 5. **Justify:** rational $F$ with $\deg P < \deg Q$ needs nothing more (Theorem §95.6); otherwise check $|F| \to 0$ on semicircles passing between the poles (Theorem §95.3), and that $F$ is the transform of a reasonable function (Theorem §95.4).
> 6. **Check** $f(0+) = \lim_{s\to\infty}sF(s)$ and, if possible, compare with a table.

^rem-95-2

## Examples

> [!example] Example §95.1: The Inverse Transform of s/(s² + 4)
> The function
>
> $$
> F(s) = \frac{s}{s^2 + 4} = \frac{s}{(s + 2i)(s - 2i)}
> $$
>
> has isolated singularities at $s = \pm2i$. By (6),
>
> $$
> f(t) = \operatorname{Res}_{s=2i}\Big[\frac{e^{st}s}{(s + 2i)(s - 2i)}\Big] + \operatorname{Res}_{s=-2i}\Big[\frac{e^{st}s}{(s + 2i)(s - 2i)}\Big] .
> $$
>
> Both singularities are simple poles: writing
>
> $$
> f(t) = \operatorname{Res}_{s=2i}\Big[\frac{\phi_1(s)}{s - 2i}\Big] + \operatorname{Res}_{s=-2i}\Big[\frac{\phi_2(s)}{s + 2i}\Big], \qquad \phi_1(s) = \frac{e^{st}s}{s + 2i}, \quad \phi_2(s) = \frac{e^{st}s}{s - 2i} ,
> $$
>
> we find
>
> $$
> f(t) = \phi_1(2i) + \phi_2(-2i) = \frac{e^{i2t}(2i)}{4i} + \frac{e^{-i2t}(-2i)}{-4i} = \frac{e^{i2t} + e^{-i2t}}{2} = \cos2t .
> $$
>
> B&C treats this formally; here Theorem §95.6 applies ($\deg P = 1 < 2 = \deg Q$), so $\cos2t$ is the inverse transform and the Bromwich integral with any $\gamma > 0$ converges to it. It agrees with the table entry $\mathcal{L}\{\cos at\} = s/(s^2 + a^2)$, [[§22 Solution of Initial Value Problems#^thm-22-6|331 Thm. §22.6]] (entry 6).
>
> *B&C: Sec. 95, Example*

^ex-95-1

> [!example] Example §95.2: A Real Pole and a Complex Pair
> Find the inverse Laplace transform of $F(s) = \dfrac{12}{s^3 + 8}$.
>
> **Poles.** The cube roots of $-8$ are $-2$ and $1 \pm \sqrt3\,i$ (moduli $2$, arguments $\pi$ and $\pm\pi/3$); all are simple zeros of $s^3 + 8$, whose derivative is $3s^2$.
>
> **Residues.** At $s = -2$: $\frac{12e^{-2t}}{3\cdot4} = e^{-2t}$. At $s_1 = 1 + \sqrt3\,i$, using $s_1^2 = -2 + 2\sqrt3\,i = 2(-1 + \sqrt3\,i)$:
>
> $$
> \operatorname{Res}_{s=s_1}\frac{12e^{st}}{s^3 + 8} = \frac{12e^{s_1t}}{3s_1^2} = \frac{2e^te^{i\sqrt3t}}{-1 + \sqrt3\,i} .
> $$
>
> The residue at $\bar s_1$ is its conjugate, and by B&C's suggestion ($z + \bar z = 2\operatorname{Re}z$), with $\frac{1}{-1 + \sqrt3\,i} = \frac{-1 - \sqrt3\,i}{4}$,
>
> $$
> 2\operatorname{Re}\Big(\frac{2e^te^{i\sqrt3t}}{-1 + \sqrt3\,i}\Big) = e^t\operatorname{Re}\Big[(-1 - \sqrt3\,i)\big(\cos\sqrt3t + i\sin\sqrt3t\big)\Big] = e^t\big(\sqrt3\sin\sqrt3t - \cos\sqrt3t\big) .
> $$
>
> **Answer.** By Theorem §95.6,
>
> $$
> f(t) = e^{-2t} + e^t\big(\sqrt3\sin\sqrt3t - \cos\sqrt3t\big) ,
> $$
>
> B&C's answer. **Checks.** $f(0) = 1 - 1 = 0$, $f'(0) = -2 + (-1 + 3) = 0$ and $f''(0) = 4 + 8 = 12$, matching $sF$, $s^2F \to 0$ and $s^3F \to 12$ as $s \to \infty$ (the transform of $f'''$ is $s^3F - s^2f(0) - sf'(0) - f''(0)$, which must tend to $0$); and a symbolic computation of $\mathcal{L}\{f\}$ returns $12/(s^3 + 8)$.
>
> *B&C: Sec. 95, Exercise 3*

^ex-95-2

> [!example] Example §95.3: Infinitely Many Poles
> Find $f(t)$ when
>
> $$
> F(s) = \frac{1}{s^2} - \frac{1}{s\sinh s} ,
> $$
>
> whose isolated singularities are $s_0 = 0$ and $s_n = n\pi i$, $\bar s_n = -n\pi i$ $(n = 1, 2, \ldots)$, the zeros of $s\sinh s$ ([[§39★ Hyperbolic Functions|§39★]]).
>
> **(a) $s_0 = 0$ is removable.** From the Laurent series $\frac{1}{\sinh s} = \frac1s - \frac s6 + \cdots$ $(0 < |s| < \pi)$ ([[§73★ Multiplication and Division of Power Series|§73★]], Exercise 5), $\frac{1}{s\sinh s} = \frac{1}{s^2} - \frac16 + \cdots$, so $F(s) = \frac16 + \cdots$ is analytic at $0$ once defined there, and so is $e^{st}F(s)$: its residue at $s_0$ is $0$.
>
> **(b) The poles $\pm n\pi i$.** $e^{st}/s^2$ is analytic there. For $-e^{st}/(s\sinh s)$ use [[§83 Zeros and Poles|§83]] (Theorem 2) with $p = -e^{st}/s$ and $q = \sinh s$, $q'(\pm n\pi i) = \cosh(n\pi i) = \cos n\pi = (-1)^n \ne 0$:
>
> $$
> \operatorname{Res}_{s=s_n}\big[e^{st}F(s)\big] = \frac{-e^{in\pi t}}{n\pi i\,(-1)^n} = \frac{(-1)^ni\exp(in\pi t)}{n\pi}, \qquad \operatorname{Res}_{s=\bar s_n}\big[e^{st}F(s)\big] = -\frac{(-1)^ni\exp(-in\pi t)}{n\pi} .
> $$
>
> Each pair adds up to $\frac{(-1)^ni}{n\pi}\big(e^{in\pi t} - e^{-in\pi t}\big) = \frac{(-1)^ni}{n\pi}\cdot2i\sin n\pi t = \frac2\pi\cdot\frac{(-1)^{n+1}}{n}\sin n\pi t$.
>
> **(c) The semicircles.** Take $\gamma = 1$ and $R_N^2 = 1 + (N + \frac12)^2\pi^2$, so that $C_{R_N}$ crosses the imaginary axis at $\pm(N + \frac12)\pi i$, midway between poles, and contains no pole. Write $s = x + iy$; $|\sinh s|^2 = \sinh^2x + \sin^2y$ ([[§39★ Hyperbolic Functions|§39★]]). Where $|x| \ge 1$ on $C_{R_N}$, $|\sinh s| \ge \sinh1 > 1$. Where $|x| < 1$, $y^2 = R_N^2 - (x - 1)^2 = (N + \frac12)^2\pi^2 + (2x - x^2)$ with $|2x - x^2| < 3$, so
>
> $$
> \Big||y| - \big(N + \tfrac12\big)\pi\Big| = \frac{|2x - x^2|}{|y| + (N + \frac12)\pi} < \frac{3}{(N + \frac12)\pi} \le \frac{3}{2.5\pi} < 0.4 \qquad (N \ge 2),
> $$
>
> and therefore $|\sin y| = |\cos(|y| - (N + \frac12)\pi)| > \cos0.4 > \frac12$. So $|\sinh s| > \frac12$ on $C_{R_N}$ for $N \ge 2$, and with $|s| \ge R_N - 1$ there,
>
> $$
> |F(s)| \le \frac{1}{(R_N - 1)^2} + \frac{2}{R_N - 1} = M_N \to 0 .
> $$
>
> **(d) The series.** The singular points inside $C_{R_N}$ are $0$ and $\pm n\pi i$ for $n \le N$. By Theorem §95.3,
>
> $$
> f(t) = \sum_{n=1}^{\infty}\Big\{\operatorname{Res}_{s=s_n}\big[e^{st}F(s)\big] + \operatorname{Res}_{s=\bar s_n}\big[e^{st}F(s)\big]\Big\} = \frac2\pi\sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{n}\sin n\pi t \qquad (t > 0),
> $$
>
> B&C's answer, where $f(t)$ is the Bromwich integral taken along the segments $L_{R_N}$.
>
> **(e) Which function is it?** The series is the Fourier series of the sawtooth: $x$ on $-1 < x < 1$, extended with period $2$ ([[§7 Arbitrary Period and Half-Range Expansions#^ex-7-3|341 Ex. §7.3]]); it converges to $t$ for $0 < t < 1$, to $t - 2$ for $1 < t < 3$, and so on, and to $0$ at the jumps $t = 1, 3, 5, \ldots$. Conversely, the sawtooth is $f(t) = t - 2\sum_{k\ge1}u_{2k-1}(t)$, with $u_c$ the unit step at $c$, and for $s > 0$, by [[§23 Step Functions#^thm-23-1|331 Thm. §23.1]],
>
> $$
> \mathcal{L}\{f\} = \frac{1}{s^2} - \frac2s\sum_{k\ge1}e^{-(2k-1)s} = \frac{1}{s^2} - \frac2s\cdot\frac{e^{-s}}{1 - e^{-2s}} = \frac{1}{s^2} - \frac{2}{s(e^s - e^{-s})} = \frac{1}{s^2} - \frac{1}{s\sinh s} .
> $$
>
> (The termwise transform is legitimate: the tail $\sum_{k>K}u_{2k-1}(t)$ vanishes for $t < 2K + 1$ and is at most $t$, so its transform is at most $\int_{2K+1}^\infty te^{-st}\,dt \to 0$.) So $F$ is indeed the transform of the sawtooth, a sectionally smooth function of exponential order, and Theorem §95.4 confirms that the Bromwich integral returns it, with the average value $0$ at the jumps: two independent routes to the same function.
>
> *B&C: Sec. 95, Exercise 4*

^ex-95-3
