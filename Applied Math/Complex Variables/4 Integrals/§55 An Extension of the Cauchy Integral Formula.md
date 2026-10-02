---
type: section
subject: "[[Complex Variables]]"
chapter: 4
section: 55
bc: "55"
aliases: ["B&C 55"]
tags: [complex-variables, math342]
---
← [[§54 Cauchy Integral Formula]] · ↑ [[· 4 Integrals]] · [[§56★ Verification of the Extension (An Extension of the Cauchy Integral Formula)]] →

*Brown–Churchill, Section 55 (with Exercises 2, 4, 8 of Section 57) · MAT 342 HW 7 · Practice Finals (Spring 2012, Fall 2009).*

The Cauchy integral formula can be extended to give an integral representation of every derivative $f^{(n)}(z_0)$ of an analytic function: differentiating $1/(z - z_0)$ under the integral sign $n$ times produces $n!/(z - z_0)^{n+1}$. In particular an analytic function has derivatives of all orders, a fact proved in [[§57 Some Consequences of the Extension|§57]]. In computations the formula is used backwards: it evaluates $\int_C f(z)\,dz/(z - z_0)^{n+1}$ by differentiating $f$ instead of integrating. The verification of the formula is in [[§56★ Verification of the Extension (An Extension of the Cauchy Integral Formula)|§56★]], which the course left optional; this section states it and uses it.

## The Extended Formula

Let $f$ be analytic inside and on a simple closed contour $C$, taken in the positive sense. If $z_0$ is any point interior to $C$, then

$$
f^{(n)}(z_0) = \frac{n!}{2\pi i}\int_C \frac{f(z)\,dz}{(z - z_0)^{n+1}} \qquad (n = 0, 1, 2, \ldots) . \qquad (1)
$$

This is B&C's theorem in Section 55; it is boxed and proved as [[§56★ Verification of the Extension (An Extension of the Cauchy Integral Formula)#^thm-56-1|Theorem §56.1]]. With the agreement that

$$
f^{(0)}(z_0) = f(z_0) \qquad\text{and}\qquad 0! = 1 ,
$$

it includes the Cauchy integral formula ([[§54 Cauchy Integral Formula#^thm-54-1|Theorem §54.1]])

$$
f(z_0) = \frac{1}{2\pi i}\int_C \frac{f(z)\,dz}{z - z_0} . \qquad (2)
$$

When written in the form

$$
\int_C \frac{f(z)\,dz}{(z - z_0)^{n+1}} = \frac{2\pi i}{n!}f^{(n)}(z_0) \qquad (n = 0, 1, 2, \ldots) , \qquad (3)
$$

expression (1) evaluates certain integrals when $f$ is analytic inside and on a simple closed contour $C$, taken in the positive sense, and $z_0$ is any point interior to $C$. Expression (1) is also useful in slightly different notation: if $s$ denotes points on $C$ and $z$ is a point interior to $C$, then

$$
f^{(n)}(z) = \frac{n!}{2\pi i}\int_C \frac{f(s)\,ds}{(s - z)^{n+1}} \qquad (n = 0, 1, 2, \ldots) , \qquad (4)
$$

that is,

$$
\int_C \frac{f(s)\,ds}{(s - z)^{n+1}} = \frac{2\pi i}{n!}f^{(n)}(z) \qquad (n = 0, 1, 2, \ldots) , \qquad (5)
$$

which includes the special case

$$
\int_C \frac{f(s)\,ds}{s - z} = 2\pi i\,f(z) . \qquad (6)
$$

> [!remark] Remark: Where the Formula Comes From
> If $s$ denotes points on $C$ and $z$ is a point interior to $C$, the Cauchy integral formula is
>
> $$
> f(z) = \frac{1}{2\pi i}\int_C \frac{f(s)\,ds}{s - z} . \qquad (10)
> $$
>
> Differentiating formally under this integral sign with respect to $z$, without rigorous justification, gives
>
> $$
> f'(z) = \frac{1}{2\pi i}\int_C f(s)\frac{\partial}{\partial z}(s - z)^{-1}\,ds = \frac{1}{2\pi i}\int_C \frac{f(s)\,ds}{(s - z)^2} ,
> $$
>
> and likewise
>
> $$
> f''(z) = \frac{(2)(1)}{2\pi i}\int_C \frac{f(s)\,ds}{(s - z)^{2+1}}, \qquad f'''(z) = \frac{(3)(2)(1)}{2\pi i}\int_C \frac{f(s)\,ds}{(s - z)^{3+1}} .
> $$
>
> These special cases suggest that (4) may be valid. The derivative falls only on the factor $(s - z)^{-1}$, which is as smooth in $z$ as one could wish while $s$ stays on $C$, away from $z$; the verification in [[§56★ Verification of the Extension (An Extension of the Cauchy Integral Formula)|§56★]] makes this precise with the same kind of estimate as in the proof of the Cauchy integral formula.

^rem-55-1

## Examples

The procedure is the one of [[§54 Cauchy Integral Formula#^rem-54-1|Remark: Method — Evaluating Contour Integrals by Cauchy's Formula]], step 3: write the integrand as $f(z)/(z - z_0)^{n+1}$ with $f$ analytic inside and on $C$, and differentiate $f$ $n$ times.

> [!example] Example §55.1: Powers of 1/z
> **(a)** If $C$ is the positively oriented unit circle $|z| = 1$ and $f(z) = \exp(2z)$, then $f'''(z) = 8\exp(2z)$ and
>
> $$
> \int_C \frac{\exp(2z)\,dz}{z^4} = \int_C \frac{f(z)\,dz}{(z - 0)^{3+1}} = \frac{2\pi i}{3!}f'''(0) = \frac{2\pi i}{6} \cdot 8 = \frac{8\pi i}{3} .
> $$
>
> **(b)** Let $z_0$ be any point interior to a positively oriented simple closed contour $C$. When $f(z) = 1$, all derivatives of $f$ vanish, and expression (3) shows that
>
> $$
> \int_C \frac{dz}{z - z_0} = 2\pi i \qquad\text{and}\qquad \int_C \frac{dz}{(z - z_0)^{n+1}} = 0 \quad (n = 1, 2, \ldots) .
> $$
>
> Compare [[§45 Some Examples (Contour Integrals)#^ex-45-5|Example §45.5]], where $C$ had to be a circle centered at $z_0$. (Quadrature: (a) $8.37758\ldots i = 8\pi i/3$; (b) $2\pi i$, $0$, $0$, $0$ for $n = 0, 1, 2, 3$ around the unit circle with $z_0 = 0.3 + 0.2i$.)
>
> *B&C: Sec. 55, Examples 1 and 2*

^ex-55-1

> [!example] Example §55.2: The Values of Legendre Polynomials at ±1
> If $n$ is a nonnegative integer and $f(z) = (z^2 - 1)^n$, expression (4) becomes
>
> $$
> \frac{d^n}{dz^n}(z^2 - 1)^n = \frac{n!}{2\pi i}\int_C \frac{(s^2 - 1)^n\,ds}{(s - z)^{n+1}} \qquad (n = 0, 1, 2, \ldots) , \qquad (7)
> $$
>
> where $C$ is any simple closed contour surrounding $z$. In view of (7), the Legendre polynomial
>
> $$
> P_n(z) = \frac{1}{n!\,2^n}\frac{d^n}{dz^n}(z^2 - 1)^n \qquad (n = 0, 1, 2, \ldots) \qquad (8)
> $$
>
> can be written as
>
> $$
> P_n(z) = \frac{1}{2^{n+1}\pi i}\int_C \frac{(s^2 - 1)^n\,ds}{(s - z)^{n+1}} \qquad (n = 0, 1, 2, \ldots) . \qquad (9)
> $$
>
> **$P_n(1)$.** Because
>
> $$
> \frac{(s^2 - 1)^n}{(s - 1)^{n+1}} = \frac{(s - 1)^n(s + 1)^n}{(s - 1)^{n+1}} = \frac{(s + 1)^n}{s - 1} ,
> $$
>
> expression (9) with $z = 1$ reveals that
>
> $$
> P_n(1) = \frac{1}{2^{n+1}\pi i}\int_C \frac{(s + 1)^n\,ds}{s - 1} ;
> $$
>
> and by writing $f(s) = (s + 1)^n$ and $z = 1$ in equation (6), we arrive at the values
>
> $$
> P_n(1) = \frac{1}{2^{n+1}\pi i}\,2\pi i\,(1 + 1)^n = 1 \qquad (n = 0, 1, 2, \ldots) .
> $$
>
> **$P_n(-1)$.** In the same way, $\dfrac{(s^2 - 1)^n}{(s + 1)^{n+1}} = \dfrac{(s - 1)^n}{s + 1}$, and equation (6) with $f(s) = (s - 1)^n$ and $z = -1$ gives
>
> $$
> P_n(-1) = \frac{1}{2^{n+1}\pi i}\,2\pi i\,(-1 - 1)^n = \frac{(-2)^n}{2^n} = (-1)^n \qquad (n = 0, 1, 2, \ldots) .
> $$
>
> (Check: $P_2(z) = \frac18\frac{d^2}{dz^2}(z^4 - 2z^2 + 1) = \frac12(3z^2 - 1)$ has $P_2(\pm1) = 1$; quadrature of (9) for $n \le 4$ gives $1$ and $(-1)^n$.)
>
> *B&C: Sec. 55, Example 3, and Sec. 57, Exercise 8*

^ex-55-2

> [!example] Example §55.3: A Double Pole Inside a Circle
> Find the value of the integral of $g(z) = \dfrac{1}{(z^2 + 4)^2}$ around the circle $|z - i| = 2$ in the positive sense.
>
> As in [[§54 Cauchy Integral Formula#^ex-54-3|Example §54.3]], of the zeros $\pm 2i$ of $z^2 + 4$ only $2i$ lies inside the circle. Write
>
> $$
> g(z) = \frac{f(z)}{(z - 2i)^2}, \qquad f(z) = \frac{1}{(z + 2i)^2}, \qquad f'(z) = \frac{-2}{(z + 2i)^3} ,
> $$
>
> with $f$ analytic inside and on the circle. By (3) with $n = 1$,
>
> $$
> \int_C \frac{dz}{(z^2 + 4)^2} = \frac{2\pi i}{1!}f'(2i) = 2\pi i\,\frac{-2}{(4i)^3} = 2\pi i\,\frac{-2}{-64i} = \frac{\pi}{16} .
> $$
>
> (B&C's answer: $\pi/16$; quadrature gives $0.19634954\ldots = \pi/16$.)
>
> *B&C: Sec. 57, Exercise 2(b); Source: 342 HW 7*

^ex-55-3

> [!example] Example §55.4: A Function Defined by a Contour Integral
> Let $C$ be any simple closed contour, described in the positive sense in the $z$ plane, and write
>
> $$
> g(z) = \int_C \frac{s^3 + 2s}{(s - z)^3}\,ds .
> $$
>
> Show that $g(z) = 6\pi iz$ when $z$ is inside $C$ and that $g(z) = 0$ when $z$ is outside.
>
> **$z$ inside $C$.** The function $f(s) = s^3 + 2s$ is entire, with $f''(s) = 6s$. By (5) with $n = 2$,
>
> $$
> g(z) = \frac{2\pi i}{2!}f''(z) = \pi i \cdot 6z = 6\pi iz .
> $$
>
> **$z$ outside $C$.** As a function of $s$, the integrand is analytic except at $s = z$, which is exterior to $C$; so it is analytic at all points interior to and on $C$, and $g(z) = 0$ by the Cauchy–Goursat theorem. (For $z$ on $C$ the integral is not defined.)
>
> (Check with $C$ the circle $|s| = 1.5$: quadrature gives $g(0.3 + 0.4i) = -7.5398 + 5.6549i = 6\pi i(0.3 + 0.4i)$ and $g(2 + i) = 0$.)
>
> *B&C: Sec. 57, Exercise 4; Source: 342 HW 7*

^ex-55-4

> [!example] Example §55.5: Two Final Exam Integrals
> **(a)** Let $C$ be the circle of radius $2$ centered at the origin, oriented counterclockwise. Evaluate
>
> $$
> I_n = \frac{1}{2\pi i}\int_C \frac{\operatorname{Log}(z + 3)}{(z - 1)^{n+1}}\,dz \qquad\text{for all integers } n \ge 0 .
> $$
>
> The principal logarithm $\operatorname{Log}(z + 3)$ is analytic except on the ray $x \le -3$, $y = 0$, which does not meet the disk $|z| < 3$; so $f(z) = \operatorname{Log}(z + 3)$ is analytic inside and on $C$, and $z_0 = 1$ is inside $C$. By (1), $I_n = f^{(n)}(1)/n!$.
> - $n = 0$: $I_0 = \operatorname{Log} 4 = \ln 4$.
> - $n \ge 1$: $f'(z) = (z + 3)^{-1}$, and by induction $f^{(n)}(z) = (-1)^{n-1}(n - 1)!\,(z + 3)^{-n}$. So
>
> $$
> I_n = \frac{1}{n!}\cdot\frac{(-1)^{n-1}(n - 1)!}{4^n} = \frac{(-1)^{n-1}}{n\,4^n} \qquad (n \ge 1) .
> $$
>
> (These are the Taylor coefficients of $\operatorname{Log}(z + 3)$ about $z = 1$: $\ln 4 + \frac{(z - 1)}{4} - \frac{(z - 1)^2}{32} + \cdots$. Quadrature: $I_0 = 1.3862944$, $I_1 = 0.25$, $I_2 = -0.03125$, $I_3 = 0.0052083$.)
>
> **(b)** Compute $\displaystyle\int_C \frac{e^z}{z^3 - 2z^2}\,dz$, where $C$ is the circle $|z| = 3$ traversed counterclockwise.
>
> Here $z^3 - 2z^2 = z^2(z - 2)$, and both singular points $0$ and $2$ lie inside $C$. Surround them by small disjoint positively oriented circles $C_0$ and $C_2$; by [[§53 Multiply Connected Domains#^thm-53-1|Theorem §53.1]], $\int_C = \int_{C_0} + \int_{C_2}$.
> - On $C_0$: the integrand is $f_0(z)/z^2$ with $f_0(z) = e^z/(z - 2)$ analytic inside and on $C_0$, and $f_0'(z) = \dfrac{e^z(z - 2) - e^z}{(z - 2)^2} = \dfrac{e^z(z - 3)}{(z - 2)^2}$, so $f_0'(0) = -\frac34$ and $\int_{C_0} = 2\pi i\,(-\frac34)$.
> - On $C_2$: the integrand is $f_2(z)/(z - 2)$ with $f_2(z) = e^z/z^2$, so $\int_{C_2} = 2\pi i\,f_2(2) = 2\pi i\,\frac{e^2}{4}$.
>
> $$
> \int_C \frac{e^z}{z^3 - 2z^2}\,dz = 2\pi i\Big(\frac{e^2}{4} - \frac34\Big) = \frac{\pi i}{2}\big(e^2 - 3\big) .
> $$
>
> (Quadrature over $|z| = 3$: $6.8943132\,i = \frac{\pi i}{2}(e^2 - 3)$.)
>
> *Source: 342 practice final (Spring 2012), Q8; 342 practice final (Fall 2009), Q4(a)*

^ex-55-5
