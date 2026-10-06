---
type: section
subject: "[[Complex Variables]]"
chapter: 2
section: 20
bc: "20"
aliases: ["B&C 20"]
tags: [complex-variables, math342]
---
← [[§19 Derivatives]] · ↑ [[· 2 Analytic Functions]] · [[§21 Cauchy–Riemann Equations]] →

*Brown–Churchill, Section 20 · MAT 342 HW 3.*

The definition of the derivative in [[§19 Derivatives#^def-19-1|Definition §19.1]] is formally the same as in calculus, with $z$ in place of $x$, so the basic differentiation rules carry over with the same proofs: constants, sums, products, quotients, integer powers and the chain rule. Only the limit theorems of [[§16 Theorems on Limits#^thm-16-2|Theorem §16.2]] and the fact that differentiable functions are continuous are needed. With these rules every polynomial is differentiable everywhere and every rational function wherever its denominator is not zero, which makes them the first examples of the analytic functions of [[§25 Analytic Functions#^def-25-1|Definition §25.1]]. The chain rule is proved by B&C's device of an auxiliary function $\Phi$, which avoids dividing by $f(z) - f(z_0)$.

## The Basic Rules

In stating the rules, either $\dfrac{d}{dz}f(z)$ or $f'(z)$ is used, whichever is more convenient.

> [!theorem] Theorem §20.1: Constants, the Identity and Constant Multiples
> Let $c$ be a complex constant, and let $f$ be a function whose derivative exists at a point $z$. Then
>
> $$
> \frac{d}{dz}c = 0, \qquad \frac{d}{dz}z = 1, \qquad \frac{d}{dz}\big[cf(z)\big] = cf'(z) . \qquad (1)
> $$
>
> *B&C: Sec. 20, rules (1)*

^thm-20-1

> [!proof]+ Proof
> B&C says these are easy to show; here they are, from definition (3) of §19. For $w = c$, $\Delta w/\Delta z = (c - c)/\Delta z = 0$ for every $\Delta z \ne 0$, so the limit is $0$. For $w = z$, $\Delta w/\Delta z = \Delta z/\Delta z = 1$. For $w = cf(z)$,
>
> $$
> \frac{\Delta w}{\Delta z} = c\,\frac{f(z + \Delta z) - f(z)}{\Delta z} \longrightarrow c f'(z)
> $$
>
> by the product rule for limits (a constant times a function).

^pf-20-1

*Uses:* [[§19 Derivatives#^def-19-1|Def. §19.1]], [[§16 Theorems on Limits#^thm-16-2|§16.2]], [[§16 Theorems on Limits#^cor-16-3|§16.3]]

> [!theorem] Theorem §20.2: Sum, Product and Quotient Rules
> If the derivatives of two functions $f$ and $g$ exist at a point $z$, then
>
> $$
> \frac{d}{dz}\big[f(z) + g(z)\big] = f'(z) + g'(z) , \qquad (3)
> $$
>
> $$
> \frac{d}{dz}\big[f(z)g(z)\big] = f(z)g'(z) + f'(z)g(z) ; \qquad (4)
> $$
>
> and, when $g(z) \ne 0$,
>
> $$
> \frac{d}{dz}\Big[\frac{f(z)}{g(z)}\Big] = \frac{g(z)f'(z) - f(z)g'(z)}{[g(z)]^2} . \qquad (5)
> $$
>
> *B&C: Sec. 20, rules (3)–(5)*

^thm-20-2

> [!proof]+ Proof
> **(3)** (B&C's Exercise 5). For $w = f(z) + g(z)$,
>
> $$
> \frac{\Delta w}{\Delta z} = \frac{f(z + \Delta z) - f(z)}{\Delta z} + \frac{g(z + \Delta z) - g(z)}{\Delta z} \longrightarrow f'(z) + g'(z)
> $$
>
> by the sum rule for limits.
>
> **(4).** Write the change in the product $w = f(z)g(z)$ as
>
> $$
> \Delta w = f(z + \Delta z)g(z + \Delta z) - f(z)g(z) = f(z)\big[g(z + \Delta z) - g(z)\big] + \big[f(z + \Delta z) - f(z)\big]g(z + \Delta z) .
> $$
>
> Thus
>
> $$
> \frac{\Delta w}{\Delta z} = f(z)\,\frac{g(z + \Delta z) - g(z)}{\Delta z} + \frac{f(z + \Delta z) - f(z)}{\Delta z}\,g(z + \Delta z) .
> $$
>
> Since $g'(z)$ exists, $g$ is continuous at $z$ ([[§19 Derivatives#^thm-19-1|Theorem §19.1]]), so $g(z + \Delta z) \to g(z)$ as $\Delta z \to 0$ ([[§15 Limits#^prop-15-3|Proposition §15.3]]). Letting $\Delta z$ tend to zero, the limit theorems give $f(z)g'(z) + f'(z)g(z)$.
>
> **(5).** (B&C does not derive the quotient rule; here it is in the same way.) Since $g$ is continuous and nonzero at $z$, $g(z + \Delta z) \ne 0$ for $|\Delta z|$ small ([[§18 Continuity#^thm-18-3|Theorem §18.3]]). For such $\Delta z \ne 0$, with $w = f/g$,
>
> $$
> \Delta w = \frac{f(z + \Delta z)}{g(z + \Delta z)} - \frac{f(z)}{g(z)} = \frac{\big[f(z + \Delta z) - f(z)\big]g(z) - f(z)\big[g(z + \Delta z) - g(z)\big]}{g(z + \Delta z)\,g(z)} ,
> $$
>
> so
>
> $$
> \frac{\Delta w}{\Delta z} = \frac{\dfrac{f(z + \Delta z) - f(z)}{\Delta z}\,g(z) - f(z)\,\dfrac{g(z + \Delta z) - g(z)}{\Delta z}}{g(z + \Delta z)\,g(z)} \longrightarrow \frac{f'(z)g(z) - f(z)g'(z)}{[g(z)]^2} ,
> $$
>
> using again $g(z + \Delta z) \to g(z)$ and the quotient rule for limits, the denominator tending to $[g(z)]^2 \ne 0$.

^pf-20-2

*Uses:* [[§19 Derivatives#^def-19-1|Def. §19.1]], [[§19 Derivatives#^thm-19-1|§19.1]], [[§16 Theorems on Limits#^thm-16-2|§16.2]], [[§15 Limits#^prop-15-3|§15.3]], [[§18 Continuity#^thm-18-3|§18.3]]

> [!remark]- Connections
> - The real versions, with the same proofs: [[§28 Basic Properties of the Derivative#^thm-28-2|451 Thm. §28.2]].

B&C states the power rule before the sum, product and quotient rules; its proof uses them, so it comes here.

> [!theorem] Theorem §20.3: Power Rule
> If $n$ is a positive integer,
>
> $$
> \frac{d}{dz}z^n = nz^{n - 1} . \qquad (2)
> $$
>
> This rule remains valid when $n$ is a negative integer, provided that $z \ne 0$.
>
> *B&C: Sec. 20, rule (2); Exercises 6 and 7*

^thm-20-3

> [!proof]+ Proof
> **Positive $n$** (B&C's Exercise 6(a)), by induction. For $n = 1$, (2) reads $\frac{d}{dz}z = 1$, which is (1). If $\frac{d}{dz}z^n = nz^{n - 1}$, then by the product rule (4)
>
> $$
> \frac{d}{dz}z^{n + 1} = \frac{d}{dz}\big(z^n \cdot z\big) = z^n \cdot 1 + nz^{n - 1}\cdot z = (n + 1)z^n .
> $$
>
> (Exercise 6(b) gives a direct proof: by the binomial formula ([[§3 Further Algebraic Properties#^thm-3-4|Theorem §3.4]]), $(z + \Delta z)^n - z^n = \sum_{k=1}^{n}\binom nk z^{n - k}(\Delta z)^k$, so $\Delta w/\Delta z = nz^{n - 1} + \sum_{k=2}^{n}\binom nk z^{n - k}(\Delta z)^{k - 1} \to nz^{n - 1}$.)
>
> **Negative $n$** (B&C's Exercise 7). Let $n = -m$ with $m$ a positive integer, and $z \ne 0$. Then $z^n = 1/z^m$, and by the quotient rule (5) with $f = 1$, $g = z^m$,
>
> $$
> \frac{d}{dz}z^{-m} = \frac{z^m \cdot 0 - 1\cdot mz^{m - 1}}{z^{2m}} = -mz^{-m - 1} = nz^{n - 1} .
> $$

^pf-20-3

*Uses:* [[§20 Rules for Differentiation#^thm-20-1|§20.1]], [[§20 Rules for Differentiation#^thm-20-2|§20.2]]

> [!example] Example §20.1: The Derivative of z² from the Definition
> Use definition (3) of [[§19 Derivatives#^def-19-1|Definition §19.1]] to show that $dw/dz = 2z$ when $w = z^2$.
>
> $$
> \frac{\Delta w}{\Delta z} = \frac{(z + \Delta z)^2 - z^2}{\Delta z} = \frac{2z\,\Delta z + (\Delta z)^2}{\Delta z} = 2z + \Delta z \longrightarrow 2z \qquad (\Delta z \to 0) .
> $$
>
> So $z^2$ is differentiable everywhere, with derivative $2z$, in agreement with (2). This is used in [[§22 Examples (Cauchy–Riemann Equations)#^ex-22-1|Example §22.1]] to test the Cauchy–Riemann equations.
>
> *B&C: Sec. 20, Exercise 1*

^ex-20-1

> [!example] Example §20.2: Polynomials and Their Coefficients
> **(a)** A polynomial $P(z) = a_0 + a_1z + a_2z^2 + \cdots + a_nz^n$ ($a_n \ne 0$, $n \ge 1$) is differentiable everywhere, with derivative
>
> $$
> P'(z) = a_1 + 2a_2z + \cdots + na_nz^{n - 1} .
> $$
>
> By (3) applied repeatedly, $P'$ is the sum of the derivatives of the terms; by (1) and (2), $\frac{d}{dz}a_0 = 0$ and $\frac{d}{dz}(a_kz^k) = ka_kz^{k - 1}$.
>
> **(b)** The coefficients can be written
>
> $$
> a_0 = P(0), \qquad a_1 = \frac{P'(0)}{1!}, \qquad a_2 = \frac{P''(0)}{2!}, \qquad \ldots, \qquad a_n = \frac{P^{(n)}(0)}{n!} .
> $$
>
> Differentiating $m$ times ($m \le n$), each term $a_kz^k$ with $k < m$ disappears and each with $k \ge m$ becomes $k(k - 1)\cdots(k - m + 1)a_kz^{k - m}$:
>
> $$
> P^{(m)}(z) = m!\,a_m + (m + 1)!\,a_{m + 1}z + \frac{(m + 2)!}{2!}a_{m + 2}z^2 + \cdots + \frac{n!}{(n - m)!}a_nz^{n - m} .
> $$
>
> At $z = 0$ every term containing $z$ vanishes, leaving $P^{(m)}(0) = m!\,a_m$. These are the Taylor coefficients of $P$ at $0$, a first case of [[§62 Taylor Series#^def-62-1|Definition §62.1]].
>
> *B&C: Sec. 20, Exercise 3; Source: 342 HW 3*

^ex-20-2

## The Chain Rule

> [!theorem] Theorem §20.4: Chain Rule
> Suppose that $f$ has a derivative at $z_0$ and that $g$ has a derivative at the point $f(z_0)$. Then the function $F(z) = g[f(z)]$ has a derivative at $z_0$, and
>
> $$
> F'(z_0) = g'[f(z_0)]\,f'(z_0) . \qquad (6)
> $$
>
> If $w = f(z)$ and $W = g(w)$, so that $W = F(z)$, the chain rule reads $\dfrac{dW}{dz} = \dfrac{dW}{dw}\,\dfrac{dw}{dz}$.
>
> *B&C: Sec. 20, rule (6)*

^thm-20-4

> [!remark] Remark: Why the Auxiliary Function
> The calculus argument multiplies and divides by $f(z) - f(z_0)$, which fails when $f(z) = f(z_0)$ at points $z$ arbitrarily close to $z_0$. B&C instead writes the difference quotient of $g$ as $g'(w_0) + \Phi(w)$ with $\Phi$ continuous at $w_0$, an identity that holds even when $w = w_0$, so nothing is ever divided by $f(z) - f(z_0)$.

^rem-20-1

> [!proof]+ Proof
> Choose a specific point $z_0$ at which $f'(z_0)$ exists, write $w_0 = f(z_0)$, and assume that $g'(w_0)$ exists. Then there is an $\varepsilon$ neighborhood $|w - w_0| < \varepsilon$ of $w_0$ on which $g$ is defined, and on it we can define a function $\Phi$ with $\Phi(w_0) = 0$ and
>
> $$
> \Phi(w) = \frac{g(w) - g(w_0)}{w - w_0} - g'(w_0) \qquad\text{when}\qquad w \ne w_0 . \qquad (7)
> $$
>
> By the definition of derivative,
>
> $$
> \lim_{w\to w_0}\Phi(w) = 0 ; \qquad (8)
> $$
>
> hence $\Phi$ is continuous at $w_0$. Expression (7) can be put in the form
>
> $$
> g(w) - g(w_0) = \big[g'(w_0) + \Phi(w)\big](w - w_0) \qquad (|w - w_0| < \varepsilon) , \qquad (9)
> $$
>
> which is valid even when $w = w_0$ (both sides are $0$). Since $f'(z_0)$ exists, $f$ is continuous at $z_0$ ([[§19 Derivatives#^thm-19-1|Theorem §19.1]]), so we can choose a positive number $\delta$ such that the point $f(z)$ lies in the neighborhood $|w - w_0| < \varepsilon$ whenever $|z - z_0| < \delta$. So it is legitimate to replace $w$ in (9) by $f(z)$ for any $z$ with $|z - z_0| < \delta$. With that substitution, and with $w_0 = f(z_0)$, dividing by $z - z_0$ gives
>
> $$
> \frac{g[f(z)] - g[f(z_0)]}{z - z_0} = \big\{g'[f(z_0)] + \Phi[f(z)]\big\}\,\frac{f(z) - f(z_0)}{z - z_0} \qquad (0 < |z - z_0| < \delta) , \qquad (10)
> $$
>
> where $z \ne z_0$ so that we are not dividing by zero. Now $f$ is continuous at $z_0$ and $\Phi$ is continuous at $w_0 = f(z_0)$, so the composition $\Phi[f(z)]$ is continuous at $z_0$ ([[§18 Continuity#^thm-18-2|Theorem §18.2]]); since $\Phi(w_0) = 0$,
>
> $$
> \lim_{z\to z_0}\Phi[f(z)] = 0 .
> $$
>
> So, by the limit theorems, the right side of (10) tends to $g'[f(z_0)]\,f'(z_0)$ as $z$ approaches $z_0$, and (10) becomes (6) in the limit.

^pf-20-4

*Uses:* [[§19 Derivatives#^def-19-1|Def. §19.1]], [[§19 Derivatives#^thm-19-1|§19.1]], [[§18 Continuity#^thm-18-2|§18.2]], [[§16 Theorems on Limits#^thm-16-2|§16.2]]

> [!remark]- Connections
> - The real chain rule, its naive proof, the gap, and the same repair: [[§28 Basic Properties of the Derivative#^thm-28-3|451 Thm. §28.3]] ([[§28 Basic Properties of the Derivative#^pf-28-3-2|second proof]], whose function $h$ is $g'(w_0) + \Phi$).

> [!example] Example §20.3: A Composite Function
> To find the derivative of $(1 - 4z^2)^3$, write $w = 1 - 4z^2$ and $W = w^3$. Then
>
> $$
> \frac{d}{dz}(1 - 4z^2)^3 = \frac{dW}{dw}\,\frac{dw}{dz} = 3w^2(-8z) = -24z(1 - 4z^2)^2 .
> $$
>
> *B&C: Sec. 20, Example*

^ex-20-3

> [!example] Example §20.4: Two Derivatives by the Rules
> Use the differentiation rules to find $f'(z)$.
>
> **(a)** $f(z) = \dfrac{(i - z^2)^5}{(1 + i)^2}$. The denominator is a constant, $(1 + i)^2 = 1 + 2i + i^2 = 2i$. By (1) and the chain rule with $w = i - z^2$, $W = w^5$,
>
> $$
> f'(z) = \frac{1}{2i}\cdot 5(i - z^2)^4\cdot(-2z) = \frac{-10z(i - z^2)^4}{2i} = 5iz\,(i - z^2)^4 ,
> $$
>
> using $-1/i = i$. Valid for all $z$.
>
> **(b)** $f(z) = \dfrac{(2 + iz)^3}{iz^2}$ ($z \ne 0$). By the chain rule, $\frac{d}{dz}(2 + iz)^3 = 3(2 + iz)^2\cdot i$, and $\frac{d}{dz}(iz^2) = 2iz$. The quotient rule (5) gives
>
> $$
> f'(z) = \frac{iz^2\cdot3i(2 + iz)^2 - (2 + iz)^3\cdot2iz}{(iz^2)^2} = \frac{-3z^2(2 + iz)^2 - 2iz(2 + iz)^3}{-z^4} = \frac{3z(2 + iz)^2 + 2i(2 + iz)^3}{z^3} .
> $$
>
> Factoring out $(2 + iz)^2$, and $3z + 2i(2 + iz) = 3z + 4i - 2z = z + 4i$:
>
> $$
> f'(z) = \frac{(2 + iz)^2(z + 4i)}{z^3} \qquad (z \ne 0) .
> $$
>
> Check, writing $f(z) = -i(2 + iz)^3z^{-2}$ and using the product rule and (2) with $n = -2$: $f'(z) = -i\big[3i(2 + iz)^2z^{-2} - 2(2 + iz)^3z^{-3}\big] = 3(2 + iz)^2z^{-2} + 2i(2 + iz)^3z^{-3}$, the same.
>
> *Source: 342 HW 3, Problem 1*

^ex-20-4

## A l'Hôpital Rule

> [!theorem] Proposition §20.5: A l'Hôpital Rule
> Suppose that $f(z_0) = g(z_0) = 0$ and that $f'(z_0)$ and $g'(z_0)$ exist, where $g'(z_0) \ne 0$. Then
>
> $$
> \lim_{z\to z_0}\frac{f(z)}{g(z)} = \frac{f'(z_0)}{g'(z_0)} .
> $$
>
> *B&C: Sec. 20, Exercise 4; Source: 342 HW 3 (optional)*

^prop-20-5

> [!proof]+ Proof
> Since $f(z_0) = g(z_0) = 0$, for $z \ne z_0$
>
> $$
> \frac{f(z)}{g(z)} = \frac{\dfrac{f(z) - f(z_0)}{z - z_0}}{\dfrac{g(z) - g(z_0)}{z - z_0}} ,
> $$
>
> whenever $g(z) \ne 0$. The function $q(z) = \big(g(z) - g(z_0)\big)/(z - z_0)$, extended by $q(z_0) = g'(z_0)$, is continuous at $z_0$ by definition (1) of [[§19 Derivatives#^def-19-1|Definition §19.1]], and $q(z_0) \ne 0$; so by [[§18 Continuity#^thm-18-3|Theorem §18.3]], $q(z) \ne 0$ for $|z - z_0| < \delta$, that is, $g(z) = (z - z_0)q(z) \ne 0$ for $0 < |z - z_0| < \delta$. So $f/g$ is defined in a deleted neighborhood of $z_0$ and equals the quotient above, whose numerator tends to $f'(z_0)$ and denominator to $g'(z_0) \ne 0$. The quotient rule for limits gives the result.
>
> For example, with $f(z) = z^4 - 1$ and $g(z) = z - i$, which both vanish at $i$,
>
> $$
> \lim_{z\to i}\frac{z^4 - 1}{z - i} = \frac{4i^3}{1} = -4i .
> $$
>
> Directly: $z^4 - 1 = (z - i)(z^3 + iz^2 - z - i)$, and the cofactor at $z = i$ is $-i - i - i - i = -4i$.

^pf-20-5

*Uses:* [[§19 Derivatives#^def-19-1|Def. §19.1]], [[§18 Continuity#^thm-18-3|§18.3]], [[§16 Theorems on Limits#^thm-16-2|§16.2]]

> [!remark]- Connections
> - The real l'Hôpital rule, which needs the mean value theorem and allows $f'$, $g'$ to be evaluated near $z_0$ rather than at it: [[§30 L'Hospital's Rule#^thm-30-1|451 Thm. §30.1]]. The complex version here is the simple case where $f'(z_0)$ and $g'(z_0)$ exist; there is no complex mean value theorem.
