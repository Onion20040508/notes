---
type: section
subject: "[[Complex Variables]]"
chapter: 2
section: 16
bc: "16"
aliases: ["B&C 16"]
tags: [complex-variables, math342]
---
← [[§15 Limits]] · ↑ [[· 2 Analytic Functions]] · [[§17 Limits Involving the Point at Infinity]] →

*Brown–Churchill, Section 16 · MAT 342 HW 2.*

Definition §15.1 tests whether a proposed number is a limit; it does not find limits. This section supplies the tools that do. Theorem §16.1 says that $f = u + iv$ has a limit exactly when its real and imaginary parts have limits, which reduces complex limits to the limits of real functions of two variables from calculus. With it, the familiar rules carry over: limits of sums, products and quotients are the sums, products and quotients of the limits, and so the limit of a polynomial or rational function at a point where it is defined is its value there. These rules are the basis of the continuity theorems of [[§18 Continuity|§18]] and of the differentiation rules of [[§20 Rules for Differentiation|§20]].

## Limits and Components

> [!theorem] Theorem §16.1: Limits of the Real and Imaginary Parts
> Suppose that
>
> $$
> f(z) = u(x, y) + iv(x, y) \quad (z = x + iy), \qquad z_0 = x_0 + iy_0, \qquad w_0 = u_0 + iv_0 .
> $$
>
> If
>
> $$
> \lim_{(x, y)\to(x_0, y_0)} u(x, y) = u_0 \qquad\text{and}\qquad \lim_{(x, y)\to(x_0, y_0)} v(x, y) = v_0 , \qquad (1)
> $$
>
> then
>
> $$
> \lim_{z\to z_0} f(z) = w_0 ; \qquad (2)
> $$
>
> and, conversely, if statement (2) is true, then so is statement (1).
>
> *B&C: Sec. 16, Theorem 1*

^thm-16-1

> [!proof]+ Proof
> **(1) implies (2).** Limits (1) tell us that for each positive number $\varepsilon$ there exist positive numbers $\delta_1$ and $\delta_2$ such that
>
> $$
> |u - u_0| < \frac\varepsilon2 \quad\text{whenever}\quad 0 < \sqrt{(x - x_0)^2 + (y - y_0)^2} < \delta_1 \qquad (3)
> $$
>
> and
>
> $$
> |v - v_0| < \frac\varepsilon2 \quad\text{whenever}\quad 0 < \sqrt{(x - x_0)^2 + (y - y_0)^2} < \delta_2 . \qquad (4)
> $$
>
> Let $\delta$ be any positive number smaller than $\delta_1$ and $\delta_2$. Since
>
> $$
> |(u + iv) - (u_0 + iv_0)| = |(u - u_0) + i(v - v_0)| \le |u - u_0| + |v - v_0|
> $$
>
> and
>
> $$
> \sqrt{(x - x_0)^2 + (y - y_0)^2} = |(x - x_0) + i(y - y_0)| = |(x + iy) - (x_0 + iy_0)| ,
> $$
>
> statements (3) and (4) give
>
> $$
> |(u + iv) - (u_0 + iv_0)| < \frac\varepsilon2 + \frac\varepsilon2 = \varepsilon \qquad\text{whenever}\qquad 0 < |(x + iy) - (x_0 + iy_0)| < \delta .
> $$
>
> That is, limit (2) holds.
>
> **(2) implies (1).** Now assume (2): for each positive number $\varepsilon$ there is a positive number $\delta$ such that
>
> $$
> |(u + iv) - (u_0 + iv_0)| < \varepsilon \qquad (5)
> $$
>
> whenever
>
> $$
> 0 < |(x + iy) - (x_0 + iy_0)| < \delta . \qquad (6)
> $$
>
> But the real and imaginary parts of a complex number are at most its modulus ([[§4 Vectors and Moduli#^prop-4-1|Proposition §4.1]]):
>
> $$
> |u - u_0| \le |(u - u_0) + i(v - v_0)|, \qquad |v - v_0| \le |(u - u_0) + i(v - v_0)| ,
> $$
>
> and $|(x + iy) - (x_0 + iy_0)| = \sqrt{(x - x_0)^2 + (y - y_0)^2}$. Hence (5) and (6) give
>
> $$
> |u - u_0| < \varepsilon \quad\text{and}\quad |v - v_0| < \varepsilon \qquad\text{whenever}\qquad 0 < \sqrt{(x - x_0)^2 + (y - y_0)^2} < \delta .
> $$
>
> This establishes limits (1).

^pf-16-1

*Uses:* [[§15 Limits#^def-15-1|Def. §15.1]], [[§3 Continuity and Limits of Functions#^def-3-2|452 Def. §3.2]] (limits in two variables), [[§4 Vectors and Moduli#^prop-4-1|§4.1]] ($|\operatorname{Re} z|, |\operatorname{Im} z| \le |z|$), [[§5 Triangle Inequality#^thm-5-1|§5.1]]

## Limits of Sums, Products and Quotients

> [!theorem] Theorem §16.2: Limits of Sums, Products and Quotients
> Suppose that
>
> $$
> \lim_{z\to z_0} f(z) = w_0 \qquad\text{and}\qquad \lim_{z\to z_0} F(z) = W_0 . \qquad (7)
> $$
>
> Then
>
> $$
> \lim_{z\to z_0}\big[f(z) + F(z)\big] = w_0 + W_0 , \qquad (8)
> $$
>
> $$
> \lim_{z\to z_0}\big[f(z)F(z)\big] = w_0W_0 ; \qquad (9)
> $$
>
> and, if $W_0 \ne 0$,
>
> $$
> \lim_{z\to z_0}\frac{f(z)}{F(z)} = \frac{w_0}{W_0} . \qquad (10)
> $$
>
> *B&C: Sec. 16, Theorem 2*

^thm-16-2

> [!proof]+ Proof
> B&C proves (9) by reducing to real limits and says that (8) and (10) can be verified in the same way; here are all three. Write
>
> $$
> f(z) = u(x, y) + iv(x, y), \quad F(z) = U(x, y) + iV(x, y), \quad z_0 = x_0 + iy_0, \quad w_0 = u_0 + iv_0, \quad W_0 = U_0 + iV_0 .
> $$
>
> By hypotheses (7) and Theorem §16.1, the limits as $(x, y)$ approaches $(x_0, y_0)$ of $u$, $v$, $U$ and $V$ exist and equal $u_0$, $v_0$, $U_0$ and $V_0$. Limits of real functions of two variables obey the sum, product and quotient laws ([[§91 Limits and Continuity#^thm-91-2|Calc Thm. §91.2]]).
>
> **(8).** The components of $f + F$ are $u + U$ and $v + V$, with limits $u_0 + U_0$ and $v_0 + V_0$. By Theorem §16.1 again, $f(z) + F(z) \to (u_0 + U_0) + i(v_0 + V_0) = w_0 + W_0$. (Directly from the definition, B&C's Exercise 6(b): choose $\delta$ so that $|f(z) - w_0| < \varepsilon/2$ and $|F(z) - W_0| < \varepsilon/2$ for $0 < |z - z_0| < \delta$; then $|(f + F) - (w_0 + W_0)| < \varepsilon$ by the triangle inequality.)
>
> **(9).** The real and imaginary components of the product
>
> $$
> f(z)F(z) = (uU - vV) + i(vU + uV)
> $$
>
> have the limits $u_0U_0 - v_0V_0$ and $v_0U_0 + u_0V_0$ as $(x, y)$ approaches $(x_0, y_0)$. Hence, by Theorem §16.1, $f(z)F(z)$ has the limit
>
> $$
> (u_0U_0 - v_0V_0) + i(v_0U_0 + u_0V_0) = w_0W_0 .
> $$
>
> **(10).** First, $F(z) \ne 0$ near $z_0$, so the quotient is defined in a deleted neighborhood of $z_0$: taking $\varepsilon = |W_0|/2$ in (7) gives a $\delta$ with $|F(z) - W_0| < |W_0|/2$, hence $|F(z)| \ge |W_0| - |F(z) - W_0| > |W_0|/2 > 0$, for $0 < |z - z_0| < \delta$. Multiplying numerator and denominator by $\overline{F(z)}$,
>
> $$
> \frac{f(z)}{F(z)} = \frac{(u + iv)(U - iV)}{U^2 + V^2} = \frac{uU + vV}{U^2 + V^2} + i\,\frac{vU - uV}{U^2 + V^2} .
> $$
>
> The denominators tend to $U_0^2 + V_0^2 = |W_0|^2 \ne 0$, so by the real quotient law the two components tend to $(u_0U_0 + v_0V_0)/|W_0|^2$ and $(v_0U_0 - u_0V_0)/|W_0|^2$. By Theorem §16.1 the quotient tends to
>
> $$
> \frac{(u_0 + iv_0)(U_0 - iV_0)}{|W_0|^2} = \frac{w_0\overline{W_0}}{W_0\overline{W_0}} = \frac{w_0}{W_0} .
> $$

^pf-16-2

*Uses:* [[§16 Theorems on Limits#^thm-16-1|§16.1]], [[§91 Limits and Continuity#^thm-91-2|Calc Thm. §91.2]] (limit laws in two variables), [[§5 Triangle Inequality#^thm-5-1|§5.1]], [[§6 Complex Conjugates#^prop-6-3|§6.3]] ($W\bar W = |W|^2$)

> [!remark]- Connections
> - Theorem §16.1 is the statement that a function into $\mathbb{R}^2$ has a limit exactly when each coordinate does, because $\max(|a|, |b|) \le |a + ib| \le |a| + |b|$; the same comparison of norms is used for sequences in [[§60 Convergence of Sequences#^thm-60-2|Theorem §60.2]]. The rigorous home of the real limit laws used here is [[§3 Continuity and Limits of Functions|452 §3]] ([[§3 Continuity and Limits of Functions#^thm-3-2|452 Thm. §3.2]] for products, [[§3 Continuity and Limits of Functions#^thm-3-3|452 Thm. §3.3]] for quotients, stated there for continuity).

From definition (2) of [[§15 Limits|§15]] it is easy to compute the two basic limits from which all polynomial limits follow.

> [!theorem] Corollary §16.3: Limits of Polynomials and Rational Functions
> For any complex numbers $z_0$ and $c$,
>
> $$
> \lim_{z\to z_0} c = c, \qquad \lim_{z\to z_0} z = z_0, \qquad \lim_{z\to z_0} z^n = z_0^n \quad (n = 1, 2, \ldots) .
> $$
>
> Consequently the limit of a polynomial $P(z) = a_0 + a_1z + a_2z^2 + \cdots + a_nz^n$ as $z$ approaches a point $z_0$ is the value of the polynomial at that point:
>
> $$
> \lim_{z\to z_0} P(z) = P(z_0) ; \qquad (11)
> $$
>
> and if $P$ and $Q$ are polynomials with $Q(z_0) \ne 0$, then $\lim_{z\to z_0} P(z)/Q(z) = P(z_0)/Q(z_0)$.
>
> *B&C: Sec. 16 (text) and equation (11); Sec. 18, Exercises 3(c) and 4*

^cor-16-3

> [!proof]+ Proof
> **Constants.** $|c - c| = 0 < \varepsilon$ for every $z$, so any $\delta$ works.
>
> **The identity.** $|z - z_0| < \varepsilon$ whenever $0 < |z - z_0| < \varepsilon$, so $\delta = \varepsilon$ works.
>
> **Powers** (B&C's Exercise 4). By induction on $n$. The case $n = 1$ is the identity. If $\lim_{z\to z_0} z^n = z_0^n$, then by property (9) with $f(z) = z^n$ and $F(z) = z$,
>
> $$
> \lim_{z\to z_0} z^{n + 1} = \lim_{z\to z_0}\big(z^n \cdot z\big) = z_0^n \cdot z_0 = z_0^{n + 1} .
> $$
>
> **Polynomials.** By (9), $\lim a_kz^k = a_kz_0^k$ for each $k$ (a constant times $z^k$), and by (8), applied $n$ times, $\lim P(z) = a_0 + a_1z_0 + \cdots + a_nz_0^n = P(z_0)$.
>
> **Rational functions.** By (11), $P(z) \to P(z_0)$ and $Q(z) \to Q(z_0) \ne 0$, and (10) gives $P(z)/Q(z) \to P(z_0)/Q(z_0)$.

^pf-16-3

*Uses:* [[§15 Limits#^def-15-1|Def. §15.1]], [[§16 Theorems on Limits#^thm-16-2|§16.2]], [[§13 Functions and Mappings#^def-13-3|Def. §13.3]]

> [!example] Example §16.1: Cancel, Then Use the Quotient Law
> Determine whether
>
> $$
> \lim_{z\to-i}\frac{z^2 + 1}{(z + i)(\bar z + 2)}
> $$
>
> exists, and compute it.
>
> The function is defined except where $z = -i$ or $\bar z = -2$, that is, $z = -2$; so it is defined in a deleted neighborhood of $-i$. There $z \ne -i$, and since $z^2 + 1 = (z - i)(z + i)$,
>
> $$
> \frac{z^2 + 1}{(z + i)(\bar z + 2)} = \frac{z - i}{\bar z + 2} \qquad (z \ne -i,\ z \ne -2) .
> $$
>
> The limit involves only points $z \ne -i$, so it is the limit of the right side. As $z \to -i$: $z - i \to -2i$ (Corollary §16.3), and $\bar z = x - iy \to 0 - i(-1) = i$ by Theorem §16.1 (its components $x$ and $-y$ tend to $0$ and $1$), so $\bar z + 2 \to 2 + i \ne 0$. By the quotient law (10), the limit exists and
>
> $$
> \lim_{z\to-i}\frac{z^2 + 1}{(z + i)(\bar z + 2)} = \frac{-2i}{2 + i} = \frac{-2i(2 - i)}{(2 + i)(2 - i)} = \frac{-4i + 2i^2}{5} = -\frac25 - \frac45 i .
> $$
>
> Numerically, at $z = -i + 10^{-7}(1 + 2i)$ the function equals $-0.40000 - 0.80000i$ to five places.
>
> *Source: 342 HW 2, Problem 3(a)*

^ex-16-1

> [!example] Example §16.2: A Limit Through the Components
> Show that
>
> $$
> \lim_{z\to1 - i}\big[x + i(2x + y)\big] = 1 + i \qquad (z = x + iy) .
> $$
>
> **By Theorem §16.1.** Here $u(x, y) = x$ and $v(x, y) = 2x + y$ are polynomials in $x, y$, and as $(x, y) \to (1, -1)$, $u \to 1$ and $v \to 2 - 1 = 1$. So $f(z) \to 1 + i$.
>
> **From the definition**, as B&C asks. With $z_0 = 1 - i$,
>
> $$
> \big|x + i(2x + y) - (1 + i)\big| = \big|(x - 1) + i\big(2(x - 1) + (y + 1)\big)\big| \le |x - 1| + 2|x - 1| + |y + 1| \le 4|z - z_0| ,
> $$
>
> since $|x - 1| \le |z - z_0|$ and $|y + 1| \le |z - z_0|$. So $\delta = \varepsilon/4$ works: $|f(z) - (1 + i)| < \varepsilon$ whenever $0 < |z - z_0| < \varepsilon/4$.
>
> *B&C: Sec. 18, Exercise 2(c)*

^ex-16-2

> [!example] Example §16.3: Limits of Rational Functions
> **(a)** For a positive integer $n$ and $z_0 \ne 0$, $\lim_{z\to z_0} 1/z^n = 1/z_0^n$, by (10) with $f = 1$ and $F = z^n \to z_0^n \ne 0$.
>
> **(b)** $\displaystyle\lim_{z\to i}\frac{iz^3 - 1}{z + i} = \frac{i \cdot i^3 - 1}{i + i} = \frac{i^4 - 1}{2i} = 0$, by Corollary §16.3, since the denominator tends to $2i \ne 0$.
>
> *B&C: Sec. 18, Exercise 3(a), (b)*

^ex-16-3

The following product rule, in which only one factor has a limit, is often more convenient than (9).

> [!theorem] Proposition §16.4: A Null Function Times a Bounded Function
> If $\lim_{z\to z_0} f(z) = 0$ and there is a positive number $M$ such that $|g(z)| \le M$ for all $z$ in some neighborhood of $z_0$, then
>
> $$
> \lim_{z\to z_0} f(z)g(z) = 0 .
> $$
>
> *B&C: Sec. 18, Exercise 9; Source: 342 HW 2 (optional)*

^prop-16-4

> [!proof]+ Proof
> Let $|g(z)| \le M$ for $|z - z_0| < \rho$. Given $\varepsilon > 0$, choose $\delta_1 > 0$ with $|f(z)| < \varepsilon/M$ whenever $0 < |z - z_0| < \delta_1$, and let $\delta = \min(\delta_1, \rho)$. Then, whenever $0 < |z - z_0| < \delta$,
>
> $$
> |f(z)g(z) - 0| = |f(z)|\,|g(z)| < \frac{\varepsilon}{M}\cdot M = \varepsilon .
> $$
>
> Note that $g$ need not have a limit at $z_0$: for example $z \cdot (z/\bar z) \to 0$ as $z \to 0$, although $z/\bar z$ has no limit there ([[§15 Limits#^ex-15-2|Example §15.2]]).

^pf-16-4

*Uses:* [[§15 Limits#^def-15-1|Def. §15.1]]
