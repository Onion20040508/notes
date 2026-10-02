---
type: section
subject: "[[Calculus]]"
chapter: 7
section: 47
stewart: "7.4"
aliases: ["Stewart 7.4"]
tags: [calculus]
---
← [[§46 Trigonometric Substitution]] · ↑ [[· 7 Techniques of Integration]] · [[§48 Strategy for Integration]] →

*Stewart, Section 7.4.*

Every rational function can be integrated. Taking $\frac{2}{x - 1} - \frac{1}{x + 2}$ to a common denominator gives $\frac{x + 5}{x^2 + x - 2}$; reversing this, $\int \frac{x + 5}{x^2 + x - 2}\,dx = 2\ln|x - 1| - \ln|x + 2| + C$. The method of **partial fractions** does this in general. Divide, so that the numerator has lower degree than the denominator. Factor the denominator into linear and irreducible quadratic factors. Write the quotient as a sum of simple fractions, one kind for each kind of factor. Each of these integrates to a rational function, a logarithm or an inverse tangent. Substitutions that turn other integrands into rational functions extend the reach of the method.

## The Method of Partial Fractions

> [!definition] Definition §47.1: Proper and Improper Rational Functions
> If $P(x) = a_n x^n + a_{n-1} x^{n-1} + \cdots + a_1 x + a_0$ with $a_n \ne 0$, then $P$ has **degree** $n$, written $\deg(P) = n$. A rational function $f(x) = P(x)/Q(x)$, with $P$ and $Q$ polynomials, is **proper** if $\deg(P) < \deg(Q)$ and **improper** if $\deg(P) \ge \deg(Q)$.
>
> *Stewart: 7.4 (text)*

^def-47-1

> [!theorem] Theorem §47.1: Division of Polynomials
> If $f = P/Q$ is improper, then long division of $P$ by $Q$ gives polynomials $S$ (the quotient) and $R$ (the remainder) with $\deg(R) < \deg(Q)$ and
>
> $$
> f(x) = \frac{P(x)}{Q(x)} = S(x) + \frac{R(x)}{Q(x)} . \qquad (1)
> $$
>
> *Stewart: 7.4, Equation 1*

^thm-47-1

*Stewart takes long division for granted. It is the division algorithm for polynomials, proved in [[§13 Polynomials#^ladr-4-9|LADR 4.9]].*

> [!theorem] Theorem §47.2: Factorization over the Reals
> Every polynomial $Q$ with real coefficients can be factored as a constant times a product of linear factors $ax + b$ and irreducible quadratic factors $ax^2 + bx + c$ with $b^2 - 4ac < 0$.
>
> *Stewart: 7.4 (text)*

^thm-47-2

*Stewart omits the proof ("it can be shown"). It rests on the Fundamental Theorem of Algebra and is proved in [[§13 Polynomials#^ladr-4-16|LADR 4.16]].*

For instance, $x^4 - 16 = (x^2 - 4)(x^2 + 4) = (x - 2)(x + 2)(x^2 + 4)$.

> [!remark]- Connections
> - Both theorems are proved in Linear Algebra: [[§13 Polynomials#^ladr-4-9|LADR 4.9]] (division with a basis of $\mathcal{P}_n$ instead of long division) and [[§13 Polynomials#^ladr-4-16|LADR 4.16]] (existence and uniqueness of the real factorization, from the complex one, since nonreal roots come in conjugate pairs).

> [!theorem] Theorem §47.3: Partial Fraction Decomposition
> Let $R/Q$ be a proper rational function, with $Q$ factored as in Theorem §47.2. Then $R(x)/Q(x)$ is a sum of **partial fractions**
>
> $$
> \frac{A}{(ax + b)^i} \qquad\text{and}\qquad \frac{Ax + B}{(ax^2 + bx + c)^j} ,
> $$
>
> with constants $A$, $B$, as follows.
> - **Case I: $Q$ is a product of distinct linear factors**, $Q(x) = (a_1x + b_1)(a_2x + b_2)\cdots(a_kx + b_k)$ (no factor repeated, and none a constant multiple of another). Then there are constants $A_1, \ldots, A_k$ with
>
>   $$
>   \frac{R(x)}{Q(x)} = \frac{A_1}{a_1x + b_1} + \frac{A_2}{a_2x + b_2} + \cdots + \frac{A_k}{a_kx + b_k} . \qquad (2)
>   $$
>
> - **Case II: some linear factors are repeated.** If $(a_1x + b_1)^r$ occurs in $Q$, then in place of the single term $A_1/(a_1x + b_1)$ one uses
>
>   $$
>   \frac{A_1}{a_1x + b_1} + \frac{A_2}{(a_1x + b_1)^2} + \cdots + \frac{A_r}{(a_1x + b_1)^r} . \qquad (7)
>   $$
>
> - **Case III: $Q$ has an irreducible quadratic factor, not repeated.** For each factor $ax^2 + bx + c$ ($b^2 - 4ac < 0$) there is a term
>
>   $$
>   \frac{Ax + B}{ax^2 + bx + c} . \qquad (9)
>   $$
>
> - **Case IV: $Q$ has a repeated irreducible quadratic factor** $(ax^2 + bx + c)^r$. In place of the single term (9) one uses
>
>   $$
>   \frac{A_1x + B_1}{ax^2 + bx + c} + \frac{A_2x + B_2}{(ax^2 + bx + c)^2} + \cdots + \frac{A_rx + B_r}{(ax^2 + bx + c)^r} . \qquad (11)
>   $$
>
> In general all four kinds of terms occur together, one group for each factor of $Q$.
>
> *Stewart: 7.4, Equations 2, 7, 9 and 11*

^thm-47-3

*Stewart omits the proof ("a theorem in algebra guarantees that it is always possible"); it can be proved by induction on the number of factors of $Q$. There is no rigorous home for it in the vault.*

For example,

$$
\frac{x^3 - x + 1}{x^2(x - 1)^3} = \frac{A}{x} + \frac{B}{x^2} + \frac{C}{x - 1} + \frac{D}{(x - 1)^2} + \frac{E}{(x - 1)^3},
\qquad
\frac{x}{(x - 2)(x^2 + 1)(x^2 + 4)} = \frac{A}{x - 2} + \frac{Bx + C}{x^2 + 1} + \frac{Dx + E}{x^2 + 4} .
$$

> [!remark]- Connections
> - See also: [[§22 Solution of Initial Value Problems#^rem-22-4|331 Remark: Method — Inverting a Rational Transform]] (the same decomposition in the variable $s$, used to invert Laplace transforms), worked in [[§22 Solution of Initial Value Problems#^ex-22-2|331 Ex. §22.2]].
> - See also: [[§52★ Partial Fractions and Convolutions#^thm-52-2|341 Thm. §52.2]] (Heaviside's formula: for distinct linear factors, real or complex, the coefficient of $1/(s - r_k)$ is $q(r_k)/p'(r_k)$, and the decomposition is proved to exist in that case).

> [!remark] Remark: Method — Partial Fractions
> To find $\int P(x)/Q(x)\,dx$:
> 1. **Divide** if $\deg P \ge \deg Q$, to get $S(x) + R(x)/Q(x)$ (Theorem §47.1). Integrate the polynomial $S$ term by term.
> 2. **Factor** $Q$ into linear and irreducible quadratic factors (Theorem §47.2). A root $r$ of $Q$ gives the factor $x - r$; a quadratic is irreducible when $b^2 - 4ac < 0$.
> 3. **Write the form** of the decomposition of $R/Q$ (Theorem §47.3), one group of terms per factor.
> 4. **Find the constants.** Multiply by the least common denominator $Q(x)$ to get a polynomial identity. Either expand and equate coefficients of like powers of $x$, which gives a linear system, or substitute convenient values of $x$ (the roots of the linear factors make all but one term vanish), or combine the two.
> 5. **Integrate each term.** $\int \frac{A}{ax + b}\,dx = \frac{A}{a}\ln|ax + b| + C$, and $\int \frac{A}{(ax + b)^i}\,dx$ for $i \ge 2$ is a power. For $\frac{Ax + B}{ax^2 + bx + c}$, complete the square in the denominator and substitute to reach
>
>    $$
>    \int \frac{Cu + D}{u^2 + a^2}\,du = C \int \frac{u}{u^2 + a^2}\,du + D \int \frac{du}{u^2 + a^2} = \frac{C}{2}\ln(u^2 + a^2) + \frac{D}{a}\tan^{-1}\frac{u}{a} + K ,
>    $$
>
>    using Theorem §47.4. Terms of Case IV need a substitution such as $x = \tan\theta$ ([[§46 Trigonometric Substitution#^rem-46-1|Remark: Method — Trigonometric Substitution]]) or a reduction formula.
> 6. **Look for a shortcut first.** If the numerator is (a multiple of) the derivative of the denominator, substitute: with $u = x(x^2 + 3) = x^3 + 3x$, $du = (3x^2 + 3)\,dx$ and $\int \frac{x^2 + 1}{x(x^2 + 3)}\,dx = \frac13 \ln|x^3 + 3x| + C$, with no partial fractions at all.
>
> *Stewart: 7.4 (text)*

^rem-47-1

> [!remark] Remark: Why Substituting Values Works
> In Example §47.1 below, Equation 4 is obtained by multiplying Equation 3 by $x(2x - 1)(x + 2)$, so a priori it holds only for $x \ne 0, \frac12, -2$, the very values one wants to substitute. But both sides of Equation 4 are polynomials, and they agree at infinitely many $x$. Their difference is a polynomial with infinitely many roots, so it is the zero polynomial, and Equation 4 holds for *all* $x$. (Equivalently: both sides are continuous and agree except at three points, so they agree there too, by taking limits.) This is Stewart's Exercise 75.

^rem-47-2

> [!theorem] Theorem §47.4: The Inverse Tangent Integral
> For $a \ne 0$,
>
> $$
> \int \frac{dx}{x^2 + a^2} = \frac1a \tan^{-1}\Big(\frac{x}{a}\Big) + C . \qquad (10)
> $$
>
> *Stewart: 7.4, Formula 10*

^thm-47-4

> [!proof]+ Proof
> Differentiate the right side with the Chain Rule, using $\frac{d}{du}\tan^{-1} u = \frac{1}{1 + u^2}$ ([[§19 Derivatives of Logarithmic and Inverse Trigonometric Functions#^thm-19-8|Theorem §19.8]]):
>
> $$
> \frac{d}{dx}\Big[\frac1a \tan^{-1}\frac{x}{a}\Big] = \frac1a \cdot \frac{1}{1 + x^2/a^2} \cdot \frac1a = \frac{1}{a^2 + x^2} .
> $$

^pf-47-4

*Uses:* [[§19 Derivatives of Logarithmic and Inverse Trigonometric Functions#^thm-19-8|§19.8]], [[§17 The Chain Rule#^thm-17-2|§17.2]]

> [!theorem] Proposition §47.5: The Integral of $1/(x^2 - a^2)$
> For $a \ne 0$,
>
> $$
> \int \frac{dx}{x^2 - a^2} = \frac{1}{2a} \ln\left|\frac{x - a}{x + a}\right| + C . \qquad (6)
> $$
>
> *Stewart: 7.4, Formula 6 (Example 7.4.3)*

^prop-47-5

> [!proof]+ Proof
> Case I of Theorem §47.3: $\dfrac{1}{x^2 - a^2} = \dfrac{1}{(x - a)(x + a)} = \dfrac{A}{x - a} + \dfrac{B}{x + a}$, so $A(x + a) + B(x - a) = 1$ for all $x$ (Remark above). Putting $x = a$ gives $2aA = 1$, $A = \frac{1}{2a}$; putting $x = -a$ gives $-2aB = 1$, $B = -\frac{1}{2a}$. Therefore
>
> $$
> \int \frac{dx}{x^2 - a^2} = \frac{1}{2a} \int \Big(\frac{1}{x - a} - \frac{1}{x + a}\Big)\,dx = \frac{1}{2a}\big(\ln|x - a| - \ln|x + a|\big) + C ,
> $$
>
> and $\ln|x - a| - \ln|x + a| = \ln\left|\frac{x - a}{x + a}\right|$.

^pf-47-5

*Uses:* [[§47 Integration of Rational Functions by Partial Fractions#^thm-47-3|§47.3]]

## Examples

> [!example] Example §47.1: Distinct Linear Factors
> Evaluate $\displaystyle\int \frac{x^2 + 2x - 1}{2x^3 + 3x^2 - 2x}\,dx$.
>
> The integrand is proper, so no division is needed. Factor: $2x^3 + 3x^2 - 2x = x(2x^2 + 3x - 2) = x(2x - 1)(x + 2)$, three distinct linear factors. So
>
> $$
> \frac{x^2 + 2x - 1}{x(2x - 1)(x + 2)} = \frac{A}{x} + \frac{B}{2x - 1} + \frac{C}{x + 2} . \qquad (3)
> $$
>
> Multiply by $x(2x - 1)(x + 2)$:
>
> $$
> x^2 + 2x - 1 = A(2x - 1)(x + 2) + Bx(x + 2) + Cx(2x - 1) = (2A + B + 2C)x^2 + (3A + 2B - C)x - 2A . \qquad (4, 5)
> $$
>
> **Equating coefficients:** $2A + B + 2C = 1$, $3A + 2B - C = 2$, $-2A = -1$. So $A = \frac12$; then $B + 2C = 0$ and $2B - C = \frac12$, which give $B = \frac15$, $C = -\frac{1}{10}$.
>
> **Or substitute values** in (4): $x = 0$ gives $-2A = -1$, $A = \frac12$; $x = \frac12$ gives $\frac54 B = \frac14$, $B = \frac15$; $x = -2$ gives $10C = -1$, $C = -\frac{1}{10}$.
>
> Then, with the mental substitution $u = 2x - 1$ in the middle term,
>
> $$
> \int \frac{x^2 + 2x - 1}{2x^3 + 3x^2 - 2x}\,dx = \int \Big(\frac12 \cdot \frac1x + \frac15 \cdot \frac{1}{2x - 1} - \frac{1}{10} \cdot \frac{1}{x + 2}\Big)\,dx = \frac12 \ln|x| + \frac{1}{10}\ln|2x - 1| - \frac{1}{10}\ln|x + 2| + K .
> $$
>
> *Stewart: Example 7.4.2*

^ex-47-1

> [!example] Example §47.2: Division and a Repeated Linear Factor
> Find $\displaystyle\int \frac{x^4 - 2x^2 + 4x + 1}{x^3 - x^2 - x + 1}\,dx$.
>
> **Divide.** $x^4 - 2x^2 + 4x + 1 = (x + 1)(x^3 - x^2 - x + 1) + 4x$, so the integrand is $x + 1 + \dfrac{4x}{x^3 - x^2 - x + 1}$.
>
> **Factor.** $Q(1) = 0$, so $x - 1$ is a factor: $x^3 - x^2 - x + 1 = (x - 1)(x^2 - 1) = (x - 1)^2(x + 1)$. The factor $x - 1$ is repeated (Case II):
>
> $$
> \frac{4x}{(x - 1)^2(x + 1)} = \frac{A}{x - 1} + \frac{B}{(x - 1)^2} + \frac{C}{x + 1} .
> $$
>
> **Constants.** Multiplying out,
>
> $$
> 4x = A(x - 1)(x + 1) + B(x + 1) + C(x - 1)^2 = (A + C)x^2 + (B - 2C)x + (-A + B + C) . \qquad (8)
> $$
>
> Equating coefficients: $A + C = 0$, $B - 2C = 4$, $-A + B + C = 0$, with solution $A = 1$, $B = 2$, $C = -1$. (By substitution: $x = 1$ gives $4 = 2B$; $x = -1$ gives $-4 = 4C$; no value of $x$ isolates $A$, but $x = 0$ gives $0 = -A + B + C$, so $A = 1$.)
>
> **Integrate.**
>
> $$
> \begin{aligned}
> \int \frac{x^4 - 2x^2 + 4x + 1}{x^3 - x^2 - x + 1}\,dx &= \int \Big[x + 1 + \frac{1}{x - 1} + \frac{2}{(x - 1)^2} - \frac{1}{x + 1}\Big]\,dx \\
> &= \frac{x^2}{2} + x + \ln|x - 1| - \frac{2}{x - 1} - \ln|x + 1| + K = \frac{x^2}{2} + x - \frac{2}{x - 1} + \ln\left|\frac{x - 1}{x + 1}\right| + K .
> \end{aligned}
> $$
>
> *Stewart: Example 7.4.4*

^ex-47-2

> [!example] Example §47.3: Irreducible Quadratic Factors
> Evaluate **(a)** $\displaystyle\int \frac{2x^2 - x + 4}{x^3 + 4x}\,dx$ and **(b)** $\displaystyle\int \frac{4x^2 - 3x + 2}{4x^2 - 4x + 3}\,dx$.
>
> **(a)** $x^3 + 4x = x(x^2 + 4)$, and $x^2 + 4$ is irreducible (Case III):
>
> $$
> \frac{2x^2 - x + 4}{x(x^2 + 4)} = \frac{A}{x} + \frac{Bx + C}{x^2 + 4}, \qquad 2x^2 - x + 4 = A(x^2 + 4) + (Bx + C)x = (A + B)x^2 + Cx + 4A .
> $$
>
> So $A + B = 2$, $C = -1$, $4A = 4$: $A = 1$, $B = 1$, $C = -1$. Split the second term, substituting $u = x^2 + 4$ in the first part and using Theorem §47.4 with $a = 2$ in the second:
>
> $$
> \int \frac{2x^2 - x + 4}{x^3 + 4x}\,dx = \int \frac{dx}{x} + \int \frac{x}{x^2 + 4}\,dx - \int \frac{dx}{x^2 + 4} = \ln|x| + \tfrac12 \ln(x^2 + 4) - \tfrac12 \tan^{-1}(x/2) + K .
> $$
>
> **(b)** The degrees are equal, so divide: $\dfrac{4x^2 - 3x + 2}{4x^2 - 4x + 3} = 1 + \dfrac{x - 1}{4x^2 - 4x + 3}$. The denominator is irreducible (discriminant $16 - 48 = -32 < 0$), so there is nothing to decompose. Complete the square: $4x^2 - 4x + 3 = (2x - 1)^2 + 2$. Substitute $u = 2x - 1$, so $du = 2\,dx$ and $x = \frac12(u + 1)$:
>
> $$
> \begin{aligned}
> \int \frac{4x^2 - 3x + 2}{4x^2 - 4x + 3}\,dx &= x + \frac12 \int \frac{\frac12(u + 1) - 1}{u^2 + 2}\,du = x + \frac14 \int \frac{u - 1}{u^2 + 2}\,du = x + \frac14 \int \frac{u}{u^2 + 2}\,du - \frac14 \int \frac{du}{u^2 + 2} \\
> &= x + \frac18 \ln(u^2 + 2) - \frac14 \cdot \frac{1}{\sqrt2}\tan^{-1}\Big(\frac{u}{\sqrt2}\Big) + C = x + \frac18 \ln(4x^2 - 4x + 3) - \frac{1}{4\sqrt2}\tan^{-1}\Big(\frac{2x - 1}{\sqrt2}\Big) + C .
> \end{aligned}
> $$
>
> This is step 5 of the method for a general term $\frac{Ax + B}{ax^2 + bx + c}$.
>
> *Stewart: Examples 7.4.5 and 7.4.6*

^ex-47-3

> [!example] Example §47.4: A Repeated Irreducible Quadratic Factor
> **(a)** Write out the form of the partial fraction decomposition of $\dfrac{x^3 + x^2 + 1}{x(x - 1)(x^2 + x + 1)(x^2 + 1)^3}$. **(b)** Evaluate $\displaystyle\int \frac{1 - x + 2x^2 - x^3}{x(x^2 + 1)^2}\,dx$.
>
> **(a)** One term for each linear factor, one for $x^2 + x + 1$ (irreducible: discriminant $-3$), and three for $(x^2 + 1)^3$ (Case IV):
>
> $$
> \frac{A}{x} + \frac{B}{x - 1} + \frac{Cx + D}{x^2 + x + 1} + \frac{Ex + F}{x^2 + 1} + \frac{Gx + H}{(x^2 + 1)^2} + \frac{Ix + J}{(x^2 + 1)^3} .
> $$
>
> Finding the ten constants by hand is tedious; a computer algebra system gives $A = -1$, $B = \frac18$, $C = D = -1$, $E = \frac{15}{8}$, $F = -\frac18$, $G = H = \frac34$, $I = -\frac12$, $J = \frac12$.
>
> **(b)** The form is $\dfrac{A}{x} + \dfrac{Bx + C}{x^2 + 1} + \dfrac{Dx + E}{(x^2 + 1)^2}$. Multiplying by $x(x^2 + 1)^2$,
>
> $$
> \begin{aligned}
> -x^3 + 2x^2 - x + 1 &= A(x^2 + 1)^2 + (Bx + C)x(x^2 + 1) + (Dx + E)x \\
> &= (A + B)x^4 + Cx^3 + (2A + B + D)x^2 + (C + E)x + A .
> \end{aligned}
> $$
>
> Equating coefficients: $A + B = 0$, $C = -1$, $2A + B + D = 2$, $C + E = -1$, $A = 1$. So $A = 1$, $B = -1$, $C = -1$, $D = 1$, $E = 0$, and (with $u = x^2 + 1$ in the second and fourth integrals)
>
> $$
> \begin{aligned}
> \int \frac{1 - x + 2x^2 - x^3}{x(x^2 + 1)^2}\,dx &= \int \Big(\frac1x - \frac{x + 1}{x^2 + 1} + \frac{x}{(x^2 + 1)^2}\Big)\,dx = \int \frac{dx}{x} - \int \frac{x\,dx}{x^2 + 1} - \int \frac{dx}{x^2 + 1} + \int \frac{x\,dx}{(x^2 + 1)^2} \\
> &= \ln|x| - \tfrac12 \ln(x^2 + 1) - \tan^{-1} x - \frac{1}{2(x^2 + 1)} + K .
> \end{aligned}
> $$
>
> It worked out nicely because $E = 0$. A term $1/(x^2 + 1)^2$ would need $x = \tan\theta$ or a reduction formula.
>
> *Stewart: Examples 7.4.7 and 7.4.8*

^ex-47-4

## Rationalizing Substitutions

Some integrands that are not rational become rational after a suitable substitution. In particular, if the integrand contains $\sqrt[n]{g(x)}$, the substitution $u = \sqrt[n]{g(x)}$ may work.

> [!example] Example §47.5: A Rationalizing Substitution
> Evaluate $\displaystyle\int \frac{\sqrt{x + 4}}{x}\,dx$.
>
> Let $u = \sqrt{x + 4}$. Then $u^2 = x + 4$, so $x = u^2 - 4$ and $dx = 2u\,du$:
>
> $$
> \int \frac{\sqrt{x + 4}}{x}\,dx = \int \frac{u}{u^2 - 4}\,2u\,du = 2 \int \frac{u^2}{u^2 - 4}\,du = 2 \int \Big(1 + \frac{4}{u^2 - 4}\Big)\,du .
> $$
>
> By Proposition §47.5 with $a = 2$ (or by factoring $u^2 - 4 = (u - 2)(u + 2)$),
>
> $$
> \int \frac{\sqrt{x + 4}}{x}\,dx = 2u + 8 \cdot \frac{1}{2 \cdot 2}\ln\left|\frac{u - 2}{u + 2}\right| + C = 2\sqrt{x + 4} + 2\ln\left|\frac{\sqrt{x + 4} - 2}{\sqrt{x + 4} + 2}\right| + C .
> $$
>
> *Stewart: Example 7.4.9*

^ex-47-5
