---
type: section
subject: "[[Complex Variables]]"
chapter: 4
section: 56
bc: "56"
aliases: ["B&C 56"]
tags: [complex-variables, math342, extension]
---
← [[§55 An Extension of the Cauchy Integral Formula]] · ↑ [[· 4 Integrals]] · [[§57 Some Consequences of the Extension]] →

*Brown–Churchill, Section 56 (with Exercises 3, 5, 6, 9 of Section 57).*
★ *Beyond MAT 342: the course skipped this section or left it optional; it is included from Brown–Churchill.*

This section proves the extended Cauchy integral formula of [[§55 An Extension of the Cauchy Integral Formula|§55]], $f^{(n)}(z) = \frac{n!}{2\pi i}\int_C f(s)\,ds/(s - z)^{n+1}$. B&C verifies the cases $n = 1$ and $n = 2$ by estimating a difference quotient, the same idea as in the proof of the Cauchy integral formula: since $s$ stays on $C$, at a fixed positive distance from $z$, the factor $1/(s - z)$ can be differentiated under the integral sign with a bound that is uniform on $C$. For general $n$, B&C refers to other texts; here the general case is reduced to $n = 1$ by integrating by parts around $C$, once the cases $n = 1, 2$ have shown that all derivatives of $f$ are analytic. This is the vault's proof that an analytic function has derivatives of all orders, given by integrals.

> [!theorem] Theorem §56.1: Extended Cauchy Integral Formula
> Let $f$ be analytic inside and on a simple closed contour $C$, taken in the positive sense. If $z$ is any point interior to $C$, then $f$ has derivatives of all orders at $z$, and
>
> $$
> f^{(n)}(z) = \frac{n!}{2\pi i}\int_C \frac{f(s)\,ds}{(s - z)^{n+1}} \qquad (n = 0, 1, 2, \ldots) , \qquad (5)
> $$
>
> where $f^{(0)}(z) = f(z)$ and $0! = 1$. Equivalently, if $z_0$ is interior to $C$, $\displaystyle f^{(n)}(z_0) = \frac{n!}{2\pi i}\int_C \frac{f(z)\,dz}{(z - z_0)^{n+1}}$.
>
> *B&C: Sec. 55, Theorem (verified in Sec. 56)*

^thm-56-1

> [!remark] Remark: Why It Works
> For $n = 1$ the difference quotient of $f$ at $z$ is an integral over $C$ of $f(s)$ times the difference quotient of $1/(s - z)$, which is $1/\big((s - z - \Delta z)(s - z)\big)$. This differs from $1/(s - z)^2$ by $\Delta z/\big((s - z - \Delta z)(s - z)^2\big)$, which is at most $|\Delta z|/\big((d - |\Delta z|)d^2\big)$ on all of $C$, where $d$ is the distance from $z$ to $C$. Multiplying by $\max|f|$ and the length of $C$ gives an error that tends to $0$ with $\Delta z$. Nothing about $f$ is used except that it is bounded on $C$ and represented by its Cauchy integral; this is why the same argument shows that any integral of Cauchy type is analytic ([[§56★ Verification of the Extension (An Extension of the Cauchy Integral Formula)#^ex-56-1|Example §56.1]]).

^rem-56-1

> [!proof]- Proof
> The case $n = 0$ is the Cauchy integral formula, [[§54 Cauchy Integral Formula#^thm-54-1|Theorem §54.1]]:
>
> $$
> f(z) = \frac{1}{2\pi i}\int_C \frac{f(s)\,ds}{s - z} . \qquad (1)
> $$
>
> Throughout, $d$ denotes the smallest distance from $z$ to points $s$ on $C$, which is positive since $z$ is not on $C$ and $C$ is closed and bounded; $M$ is the maximum value of $|f(s)|$ on $C$ (it exists because $f$ is continuous on the closed bounded set $C$); and $L$ is the length of $C$. If $0 < |\Delta z| < d$, the point $z + \Delta z$ is also interior to $C$, since the disk $|w - z| < d$ contains no point of $C$ and the segment from $z$ to any of its points cannot cross $C$.
>
> **Step 1: $n = 1$.** We verify that $f'(z)$ exists and that
>
> $$
> f'(z) = \frac{1}{2\pi i}\int_C \frac{f(s)\,ds}{(s - z)^2} . \qquad (2)
> $$
>
> Let $0 < |\Delta z| < d$. It follows from expression (1), applied at $z$ and at $z + \Delta z$, that
>
> $$
> \frac{f(z + \Delta z) - f(z)}{\Delta z} = \frac{1}{2\pi i}\int_C \Big(\frac{1}{s - z - \Delta z} - \frac{1}{s - z}\Big)\frac{f(s)}{\Delta z}\,ds = \frac{1}{2\pi i}\int_C \frac{f(s)\,ds}{(s - z - \Delta z)(s - z)} .
> $$
>
> But
>
> $$
> \frac{1}{(s - z - \Delta z)(s - z)} = \frac{1}{(s - z)^2} + \frac{\Delta z}{(s - z - \Delta z)(s - z)^2} ,
> $$
>
> and this means that
>
> $$
> \frac{f(z + \Delta z) - f(z)}{\Delta z} - \frac{1}{2\pi i}\int_C \frac{f(s)\,ds}{(s - z)^2} = \frac{1}{2\pi i}\int_C \frac{\Delta z\,f(s)\,ds}{(s - z - \Delta z)(s - z)^2} . \qquad (3)
> $$
>
> Since $|s - z| \ge d$ and $|\Delta z| < d$,
>
> $$
> |s - z - \Delta z| = |(s - z) - \Delta z| \ge \big||s - z| - |\Delta z|\big| \ge d - |\Delta z| > 0 .
> $$
>
> Thus, by the upper bound for moduli of contour integrals ([[§47 Upper Bounds for Moduli of Contour Integrals|§47]]),
>
> $$
> \left| \int_C \frac{\Delta z\,f(s)\,ds}{(s - z - \Delta z)(s - z)^2} \right| \le \frac{|\Delta z|\,M}{(d - |\Delta z|)\,d^2}\,L .
> $$
>
> Upon letting $\Delta z$ tend to zero, the right-hand side of equation (3) tends to zero. Consequently
>
> $$
> \lim_{\Delta z \to 0}\frac{f(z + \Delta z) - f(z)}{\Delta z} = \frac{1}{2\pi i}\int_C \frac{f(s)\,ds}{(s - z)^2} ,
> $$
>
> and the expression (2) for $f'(z)$ is established.
>
> **Step 2: $n = 2$** (B&C's Exercise 9, Sec. 57). We verify that
>
> $$
> f''(z) = \frac{1}{\pi i}\int_C \frac{f(s)\,ds}{(s - z)^3} . \qquad (4)
> $$
>
> *(a)* By Step 1, expression (2) holds at every point interior to $C$, in particular at $z$ and $z + \Delta z$. Since
>
> $$
> \frac{1}{(s - z - \Delta z)^2} - \frac{1}{(s - z)^2} = \frac{(s - z)^2 - (s - z - \Delta z)^2}{(s - z - \Delta z)^2(s - z)^2} = \frac{2(s - z)\Delta z - (\Delta z)^2}{(s - z - \Delta z)^2(s - z)^2} ,
> $$
>
> we get, writing $\frac{1}{\pi i} = \frac{2}{2\pi i}$,
>
> $$
> \frac{f'(z + \Delta z) - f'(z)}{\Delta z} - \frac{1}{\pi i}\int_C \frac{f(s)\,ds}{(s - z)^3} = \frac{1}{2\pi i}\int_C \Big[\frac{2(s - z) - \Delta z}{(s - z - \Delta z)^2(s - z)^2} - \frac{2}{(s - z)^3}\Big]f(s)\,ds .
> $$
>
> Over the common denominator $(s - z - \Delta z)^2(s - z)^3$ the bracket has numerator
>
> $$
> \big(2(s - z) - \Delta z\big)(s - z) - 2(s - z - \Delta z)^2 = 3(s - z)\Delta z - 2(\Delta z)^2 ,
> $$
>
> so
>
> $$
> \frac{f'(z + \Delta z) - f'(z)}{\Delta z} - \frac{1}{\pi i}\int_C \frac{f(s)\,ds}{(s - z)^3} = \frac{1}{2\pi i}\int_C \frac{3(s - z)\Delta z - 2(\Delta z)^2}{(s - z - \Delta z)^2(s - z)^3}f(s)\,ds .
> $$
>
> *(b)* Let $D$ be the largest distance from $z$ to points of $C$. For $s$ on $C$ and $0 < |\Delta z| < d$, the triangle inequality gives $|3(s - z)\Delta z - 2(\Delta z)^2| \le 3D|\Delta z| + 2|\Delta z|^2$, while as in Step 1 $|s - z - \Delta z|^2|s - z|^3 \ge (d - |\Delta z|)^2d^3$. So the integral on the right is bounded in modulus by
>
> $$
> \frac{\big(3D|\Delta z| + 2|\Delta z|^2\big)M}{(d - |\Delta z|)^2d^3}\,L .
> $$
>
> *(c)* This bound tends to $0$ as $\Delta z \to 0$. Hence $f''(z)$ exists and is given by (4).
>
> **Step 3: all derivatives are analytic.** *(B&C states that induction gives the general formula, that "the verification is considerably more involved", and refers to Markushevich, Vol. I, pp. 299–301; here is a proof.)* Since $f$ is analytic at each point inside and on $C$, it is analytic in an open set $U$ containing $C$ and its interior. Let $w$ be any point of $U$, and let $C_w$ be a positively oriented circle centered at $w$ whose closed disk lies in $U$. Then $f$ is analytic inside and on $C_w$, and by Step 2 (with $C_w$ in place of $C$), $f''$ exists at every point inside $C_w$. So $f'$ is differentiable in a neighborhood of $w$: $f'$ is analytic at every point of $U$. Applying the same argument to the analytic function $f'$ shows that $f''$ is analytic in $U$, and so on: every derivative $f^{(k)}$ is analytic in $U$.
>
> **Step 4: integration by parts around $C$.** Fix $z$ inside $C$. For integers $k \ge 1$ and $m \ge 1$,
>
> $$
> \int_C \frac{f^{(k)}(s)\,ds}{(s - z)^m} = m\int_C \frac{f^{(k-1)}(s)\,ds}{(s - z)^{m+1}} . \qquad (\ast)
> $$
>
> Indeed, $G(s) = f^{(k-1)}(s)(s - z)^{-m}$ is analytic in the open set $U$ with the point $z$ removed, which contains $C$, and there
>
> $$
> G'(s) = \frac{f^{(k)}(s)}{(s - z)^m} - m\,\frac{f^{(k-1)}(s)}{(s - z)^{m+1}} ,
> $$
>
> a continuous function. So $G'$ has the antiderivative $G$ on a domain containing $C$ (the part of $U$ minus $z$ that contains the connected set $C$), and its integral around the closed contour $C$ is $0$ by the theorem in [[§48 Antiderivatives|§48]]. That is $(\ast)$.
>
> **Step 5: the formula for every $n$.** Let $n \ge 2$. By Step 3, $f^{(n-1)}$ is analytic inside and on $C$, so Step 1 applied to $f^{(n-1)}$ gives
>
> $$
> f^{(n)}(z) = \frac{1}{2\pi i}\int_C \frac{f^{(n-1)}(s)\,ds}{(s - z)^2} .
> $$
>
> Apply $(\ast)$ repeatedly, with $(k, m) = (n - 1, 2), (n - 2, 3), \ldots, (1, n)$:
>
> $$
> \int_C \frac{f^{(n-1)}(s)\,ds}{(s - z)^2} = 2\int_C \frac{f^{(n-2)}(s)\,ds}{(s - z)^3} = 2 \cdot 3\int_C \frac{f^{(n-3)}(s)\,ds}{(s - z)^4} = \cdots = 2 \cdot 3 \cdots n\int_C \frac{f(s)\,ds}{(s - z)^{n+1}} .
> $$
>
> Since $2 \cdot 3 \cdots n = n!$, this is (5). Together with the cases $n = 0, 1$ (expressions (1) and (2)), the theorem is proved.

^pf-56-1

*Uses:* [[§54 Cauchy Integral Formula#^thm-54-1|§54.1]], [[§47 Upper Bounds for Moduli of Contour Integrals|§47]] (Theorem), [[§48 Antiderivatives|§48]] (Theorem), [[§25 Analytic Functions|§25]] (analytic at a point means differentiable in a neighborhood), [[§18 Continuity|§18]] (a continuous function on a closed bounded set is bounded)

> [!remark]- Connections
> - Step 1 is differentiation under the integral sign, justified by a bound that is uniform in $s$ on $C$; the general real-variable form (a parameter-dependent integral whose partial derivative is continuous may be differentiated under the integral sign) is the same mechanism. Steps 4–5 are integration by parts, with the fundamental theorem of calculus replaced by [[§48 Antiderivatives|§48]].

## Integrals of Cauchy Type

The proof of Step 1 used about $f$ on $C$ only that it is continuous there. So any continuous function on $C$ produces an analytic function inside $C$; it need not be the function one started with.

> [!example] Example §56.1: Integrals of Cauchy Type Are Analytic
> Let $f$ be a function that is continuous on a simple closed contour $C$. Following the procedure of Step 1, prove that the function
>
> $$
> g(z) = \frac{1}{2\pi i}\int_C \frac{f(s)\,ds}{s - z}
> $$
>
> is analytic at each point $z$ interior to $C$, and that
>
> $$
> g'(z) = \frac{1}{2\pi i}\int_C \frac{f(s)\,ds}{(s - z)^2}
> $$
>
> at such a point.
>
> Fix $z$ inside $C$ and let $d$, $M$, $L$ be as in the proof ($M$ exists since $f$ is continuous on the closed bounded set $C$). For $0 < |\Delta z| < d$, the point $z + \Delta z$ is inside $C$, and directly from the definition of $g$,
>
> $$
> \frac{g(z + \Delta z) - g(z)}{\Delta z} - \frac{1}{2\pi i}\int_C \frac{f(s)\,ds}{(s - z)^2} = \frac{1}{2\pi i}\int_C \frac{\Delta z\,f(s)\,ds}{(s - z - \Delta z)(s - z)^2} ,
> $$
>
> by the same algebra as in (3). The right side has modulus at most $\dfrac{1}{2\pi}\cdot\dfrac{|\Delta z|\,ML}{(d - |\Delta z|)d^2} \to 0$. So $g'(z)$ exists and is given by the stated integral. Since this holds at every point of the open set interior to $C$, $g$ is analytic there. (The same argument works at points exterior to $C$, with $d$ the distance from $z$ to $C$.)
>
> *B&C: Sec. 57, Exercise 6*

^ex-56-1

> [!example] Example §56.2: Different Functions Inside and Outside
> **(a)** Let $C$ be the circle $|z| = 3$, described in the positive sense. Show that if
>
> $$
> g(z) = \int_C \frac{2s^2 - s - 2}{s - z}\,ds \qquad (|z| \ne 3) ,
> $$
>
> then $g(2) = 8\pi i$. What is the value of $g(z)$ when $|z| > 3$?
>
> For $|z| < 3$, equation (6) of §55 with the entire function $f(s) = 2s^2 - s - 2$ gives $g(z) = 2\pi i\,(2z^2 - z - 2)$; in particular $g(2) = 2\pi i\,(8 - 2 - 2) = 8\pi i$. For $|z| > 3$, the integrand is analytic in $s$ inside and on $C$ (its only singular point $s = z$ is outside), so $g(z) = 0$ by the Cauchy–Goursat theorem. So the same integral defines the polynomial $2\pi i(2z^2 - z - 2)$ inside $C$ and the zero function outside; both are analytic, as Example §56.1 says they must be. (Quadrature: $g(2) = 25.1327\ldots i = 8\pi i$, $g(4 + i) = g(-3.5) = 0$.)
>
> **(b)** Let $C$ be the positively oriented unit circle and $f(s) = \bar s$ on $C$, a continuous function. Then the integral of Cauchy type of Example §56.1 is identically zero inside $C$. Indeed $\bar s = 1/s$ on $|s| = 1$, so for $|z| < 1$, $z \ne 0$, by partial fractions,
>
> $$
> g(z) = \frac{1}{2\pi i}\int_C \frac{ds}{s(s - z)} = \frac{1}{2\pi i}\cdot\frac1z\int_C\Big(\frac{1}{s - z} - \frac1s\Big)ds = \frac{1}{2\pi i}\cdot\frac{2\pi i - 2\pi i}{z} = 0 ,
> $$
>
> and $g(0) = \frac{1}{2\pi i}\int_C ds/s^2 = 0$. So $g$ is analytic inside $C$, but it does not take the values $\bar s$ (of modulus $1$) as $z$ approaches $C$. The Cauchy integral reproduces $f$ only when $f$ is itself analytic inside and on $C$.
>
> *B&C: Sec. 57, Exercise 3; part (b) illustrates Exercise 6*

^ex-56-2

> [!example] Example §56.3: Moving a Derivative Across the Integral Sign
> Show that if $f$ is analytic within and on a simple closed contour $C$ and $z_0$ is not on $C$, then
>
> $$
> \int_C \frac{f'(z)\,dz}{z - z_0} = \int_C \frac{f(z)\,dz}{(z - z_0)^2} .
> $$
>
> **By integration by parts.** This is $(\ast)$ of the proof with $k = m = 1$, and the argument there does not need $z_0$ to be inside $C$: the function $G(z) = f(z)/(z - z_0)$ is analytic on an open set containing $C$ (the open set $U$ of Step 3 with $z_0$ removed), with derivative
>
> $$
> G'(z) = \frac{f'(z)}{z - z_0} - \frac{f(z)}{(z - z_0)^2} ,
> $$
>
> which is continuous because $f'$ is analytic (Step 3). The integral of $G'$ around the closed contour $C$ is $0$ ([[§48 Antiderivatives|§48]]), which is the identity.
>
> **By the formulas.** If $z_0$ is inside $C$, the left side is $2\pi i\,f'(z_0)$ by the Cauchy integral formula applied to the analytic function $f'$, and the right side is $2\pi i\,f'(z_0)$ by (5) with $n = 1$. If $z_0$ is outside $C$, both integrands are analytic inside and on $C$, and both sides are $0$ by the Cauchy–Goursat theorem. (Quadrature for $f = e^z$ on the unit circle: both sides are $-0.766152 + 7.635960i = 2\pi i\,e^{0.2 + 0.1i}$ for $z_0 = 0.2 + 0.1i$, and $0$ for $z_0 = 3$.)
>
> *B&C: Sec. 57, Exercise 5*

^ex-56-3
