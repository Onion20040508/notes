---
type: section
subject: "[[Fourier Series and PDEs]]"
chapter: 6
section: 52
powers: "6.2"
aliases: ["Powers 6.2"]
tags: [fourier-series-and-pdes, math341, extension]
---
← [[§51★ Definition and Elementary Properties]] · ↑ [[· 6★ Laplace Transform]] · [[§53★ Partial Differential Equations]] →

*Powers, Section 6.2 · MAT 341 Practice Midterm 1.*
★ *Beyond MAT 341: the course did not cover this section; it is included from Powers.*

Transforming a linear differential equation with constant coefficients removes the derivatives and builds in the initial conditions, so the transformed problem is solved by algebra. The real work is inverting the answer. This section gives Powers' two inversion tools. For a rational transform $q(s)/p(s)$ whose denominator has simple roots, **Heaviside's formula** $\mathcal{L}^{-1}(q/p) = \sum q(r_i)e^{r_it}/p'(r_i)$ needs no algebraic partial-fraction work; in [[§53★ Partial Differential Equations|§53★]] it is extended to transcendental $p$, and that extension is how heat and wave problems are solved by transform. The **convolution theorem** inverts a product of transforms and gives solution formulas valid for every forcing function. Both tools, and the IVP method itself, are developed in [[Ordinary Differential Equations]]: [[§22 Solution of Initial Value Problems|§22]] and [[§26★ The Convolution Integral|§26★]]. Here they are stated in Powers' form and linked there; Heaviside's formula is not in that subject and is proved here.

## Transforming a Differential Equation

> [!remark] Remark: Method — Solving a Linear Initial Value Problem by Laplace Transform
> Powers' outline of the procedure:
>
> $$
> \begin{array}{ccc}
> \text{original problem} & \xrightarrow{\ \mathcal{L}\ } & \text{transformed problem} \\
> & & \big\downarrow \\
> \text{solution of original problem} & \xleftarrow{\ \mathcal{L}^{-1}\ } & \text{solution of transformed problem}
> \end{array}
> $$
>
> 1. Transform the whole equation, using [[§51★ Definition and Elementary Properties#^thm-51-4|Theorem §51.4]] for the derivatives; the initial conditions enter here.
> 2. Solve the resulting algebraic equation for $U(s) = \mathcal{L}(u)$.
> 3. Find $u(t) = \mathcal{L}^{-1}(U(s))$: break $U$ into simple pieces (linearity, Theorem §52.1) and invert each by the table ([[§51★ Definition and Elementary Properties#^thm-51-8|Theorem §51.8]]), by Heaviside's formula (Theorem §52.2) or by convolution (Theorem §52.3). This step is the difficult part.
>
> The same steps, with Boyce–DiPrima's table: [[§22 Solution of Initial Value Problems#^rem-22-3|331 §22]] (Method — Solving an Initial Value Problem by Laplace Transform).

^rem-52-1

> [!example] Example §52.1: Two Homogeneous Problems
> **First order.** To solve $u' + au = 0$, $u(0) = 1$, transform the entire equation:
>
> $$
> \mathcal{L}(u') + a\mathcal{L}(u) = 0 \quad\Longrightarrow\quad sU - 1 + aU = 0 \quad\Longrightarrow\quad U(s) = \frac{1}{s + a} .
> $$
>
> The derivative has been "transformed out", and the table gives $u(t) = e^{-at}$.
>
> **Second order.** For $u'' + \omega^2u = 0$, $u(0) = 1$, $u'(0) = 0$, the transformed equation is
>
> $$
> s^2U - s\cdot 1 - 0 + \omega^2U = 0 ,
> $$
>
> in which both initial conditions have been incorporated. So $U(s) = s/(s^2 + \omega^2)$, the transform of $u(t) = \cos(\omega t)$.
>
> *Powers: 6.2 (text)*

^ex-52-1

> [!theorem] Theorem §52.1: Linearity of the Inverse Transform
> For constants $c_1$, $c_2$,
>
> $$
> \mathcal{L}^{-1}\big[c_1F_1(s) + c_2F_2(s)\big] = c_1\mathcal{L}^{-1}\big[F_1(s)\big] + c_2\mathcal{L}^{-1}\big[F_2(s)\big] .
> $$
>
> This lets a complicated transform be broken into a sum of simple ones.
>
> *Powers: 6.2 (text)*

^thm-52-1

*Powers states this without proof. It follows from the linearity of $\mathcal{L}$ ([[§51★ Definition and Elementary Properties#^thm-51-2|Theorem §51.2]]) together with the uniqueness of the inverse transform; see [[§22 Solution of Initial Value Problems#^cor-22-5|331 Cor. §22.5]] and [[§22 Solution of Initial Value Problems#^thm-22-4|331 Thm. §22.4]] (Lerch's theorem, unproved there).*

## Partial Fractions and Heaviside's Formula

For the damped mass–spring system $u'' + au' + \omega^2u = 0$, $u(0) = u_0$, $u'(0) = u_1$, the transformed equation $s^2U - su_0 - u_1 + a(sU - u_0) + \omega^2U = 0$ gives $U$ as a ratio of two polynomials,

$$
U(s) = \frac{su_0 + (u_1 + au_0)}{s^2 + as + \omega^2} .
$$

This is not in the table. One could complete the square and use the shifting theorem ([[§23 Step Functions#^rem-23-3|331 §23]], Method — Completing the Square), but partial fractions are a better way. For $U(s) = (cs + d)/(s^2 + as + b)$ with distinct roots $r_1$, $r_2$ of the denominator, one looks for constants with

$$
\frac{cs + d}{(s - r_1)(s - r_2)} = \frac{A_1}{s - r_1} + \frac{A_2}{s - r_2} , \qquad (1)
$$

found by matching numerators: $c = A_1 + A_2$, $d = -A_1r_2 - A_2r_1$. Then $\mathcal{L}^{-1}(U) = A_1e^{r_1t} + A_2e^{r_2t}$. With more roots, this algebra becomes very tedious; a little calculus avoids it.

> [!theorem] Theorem §52.2: Heaviside's Formula
> Let $p$ and $q$ be polynomials, $q$ of lower degree than $p$, and let $p$ have only simple roots $r_1, r_2, \ldots, r_k$ (real or complex). Then
>
> $$
> \frac{q(s)}{p(s)} = \frac{q(r_1)}{p'(r_1)}\,\frac{1}{s - r_1} + \cdots + \frac{q(r_k)}{p'(r_k)}\,\frac{1}{s - r_k} ,
> $$
>
> and
>
> $$
> \mathcal{L}^{-1}\Big(\frac{q(s)}{p(s)}\Big) = \frac{q(r_1)}{p'(r_1)}\exp(r_1t) + \cdots + \frac{q(r_k)}{p'(r_k)}\exp(r_kt) . \qquad (2)
> $$
>
> *Powers: 6.2, Theorem 1*

^thm-52-2

> [!proof]+ Proof
> **The coefficients.** Write $p(s) = c(s - r_1)(s - r_2)\cdots(s - r_k)$ and try to write
>
> $$
> \frac{q(s)}{p(s)} = \frac{A_1}{s - r_1} + \frac{A_2}{s - r_2} + \cdots + \frac{A_k}{s - r_k} . \qquad (\ast)
> $$
>
> Multiplying $(\ast)$ by $s - r_1$ gives
>
> $$
> \frac{(s - r_1)q(s)}{p(s)} = A_1 + A_2\frac{s - r_1}{s - r_2} + \cdots + A_k\frac{s - r_1}{s - r_k} .
> $$
>
> As $s \to r_1$ the right side tends to $A_1$. The left side has the form $0/0$ at $r_1$, and Powers evaluates its limit by L'Hôpital's rule:
>
> $$
> \lim_{s\to r_1}\frac{(s - r_1)q(s)}{p(s)} = \lim_{s\to r_1}\frac{(s - r_1)q'(s) + q(s)}{p'(s)} = \frac{q(r_1)}{p'(r_1)} .
> $$
>
> (For a complex root, L'Hôpital's rule for real functions does not apply directly. Here is the same computation without it: $p(s) = (s - r_1)p_1(s)$ with $p_1(r_1) \ne 0$, because $r_1$ is a simple root, and $p'(r_1) = p_1(r_1)$ by the product rule. So $(s - r_1)q(s)/p(s) = q(s)/p_1(s) \to q(r_1)/p'(r_1)$.) The same argument at each root gives
>
> $$
> A_i = \frac{q(r_i)}{p'(r_i)} , \qquad i = 1, \ldots, k .
> $$
>
> **The decomposition exists.** Powers assumes that $q/p$ can be written in the form $(\ast)$; here is why it can. For each $i$ let $p_i(s) = p(s)/(s - r_i)$, a polynomial of degree $k - 1$, with $p_i(r_i) = p'(r_i) \ne 0$ and $p_i(r_j) = 0$ for $j \ne i$. The polynomial
>
> $$
> P(s) = \sum_{i=1}^{k}\frac{q(r_i)}{p'(r_i)}\,p_i(s)
> $$
>
> has degree at most $k - 1$ and satisfies $P(r_j) = q(r_j)$ for every $j$. So $P - q$, of degree at most $k - 1$ (since $\deg q < k$), has the $k$ distinct roots $r_1, \ldots, r_k$, and therefore $P = q$. Dividing $P = q$ by $p$ gives $(\ast)$ with $A_i = q(r_i)/p'(r_i)$.
>
> **The inverse transform.** By [[§51★ Definition and Elementary Properties#^ex-51-1|Example §51.1]], $\frac{1}{s - r_i} = \mathcal{L}(e^{r_it})$ for $\operatorname{Re}(s) > \operatorname{Re}(r_i)$, also for complex $r_i$. By linearity, [[§52★ Partial Fractions and Convolutions#^thm-52-1|Theorem §52.1]], the inverse transform of $(\ast)$ is (2).

^pf-52-2

*Uses:* [[§51★ Definition and Elementary Properties#^ex-51-1|Ex. §51.1]], [[§52★ Partial Fractions and Convolutions#^thm-52-1|§52.1]], [[§30 L'Hospital's Rule#^thm-30-1|451 Thm. §30.1]] (real roots)

> [!remark]- Connections
> - The existence of partial fraction decompositions of a real rational function, including repeated and quadratic factors: [[§47 Integration of Rational Functions by Partial Fractions#^thm-47-3|Calc Thm. §47.3]] (Case I is the situation here). Inverting a rational transform with repeated roots or irreducible quadratics by completing the square: [[§22 Solution of Initial Value Problems#^rem-22-4|331 §22]] (Method — Inverting a Rational Transform).
> - In complex-variable language, $q(r_i)/p'(r_i)$ is the residue of $q/p$ at the simple pole $r_i$, and (2) is the sum of the residues of $e^{st}q(s)/p(s)$. This is the form in which the formula is extended in [[§53★ Partial Differential Equations|§53★]].
> - Complex-variables version: [[§83 Zeros and Poles#^thm-83-2|342 Thm. §83.2]] ($q(r)/p'(r)$ as the residue at a simple pole) and [[§95★ Inverse Laplace Transforms#^thm-95-6|342 Thm. §95.6]] (for every proper rational transform, repeated roots included, the inverse transform is the sum of the residues of $e^{st}q(s)/p(s)$).

> [!remark] Remark: Repeated Roots
> Heaviside's formula needs simple roots. If $p$ has a double root $r$, the decomposition must contain $\frac{A}{s - r} + \frac{B}{(s - r)^2}$, whose inverse transform is $Ae^{rt} + Bte^{rt}$; the coefficients are found by limits as in [[§54★ More Difficult Examples#^prop-54-2|Proposition §54.2]]. A term $te^{rt}$ with $\operatorname{Re}(r) = 0$ grows linearly in time: this is resonance.

^rem-52-2

> [!example] Example §52.2: Partial Fractions Two Ways
> Invert $U(s) = \dfrac{s + 4}{s^2 + 3s + 2}$.
>
> **By matching numerators.** The roots of the denominator are $r_1 = -1$, $r_2 = -2$, and
>
> $$
> \frac{s + 4}{s^2 + 3s + 2} = \frac{A_1}{s + 1} + \frac{A_2}{s + 2} = \frac{(A_1 + A_2)s + (2A_1 + A_2)}{(s + 1)(s + 2)} .
> $$
>
> So $A_1 + A_2 = 1$ and $2A_1 + A_2 = 4$, giving $A_1 = 3$, $A_2 = -2$, and
>
> $$
> \mathcal{L}^{-1}\Big(\frac{s + 4}{s^2 + 3s + 2}\Big) = \mathcal{L}^{-1}\Big(\frac{3}{s + 1} - \frac{2}{s + 2}\Big) = 3e^{-t} - 2e^{-2t} .
> $$
>
> **By Heaviside's formula.** With $q(s) = s + 4$, $p(s) = s^2 + 3s + 2$, $p'(s) = 2s + 3$, Theorem §52.2 gives directly
>
> $$
> \mathcal{L}^{-1}\Big(\frac{s + 4}{s^2 + 3s + 2}\Big) = \frac{-1 + 4}{2(-1) + 3}e^{-t} + \frac{-2 + 4}{2(-2) + 3}e^{-2t} = 3e^{-t} - 2e^{-2t} .
> $$
>
> *Powers: 6.2 (text)*

^ex-52-2

> [!example] Example §52.3: The Damped Oscillator by Heaviside's Formula
> Invert $U(s) = \dfrac{su_0 + (u_1 + au_0)}{s^2 + as + \omega^2}$, the transform of the solution of $u'' + au' + \omega^2u = 0$, $u(0) = u_0$, $u'(0) = u_1$, in the underdamped case $a^2 < 4\omega^2$.
>
> **Roots.** $p(s) = s^2 + as + \omega^2$ has the simple complex roots $r_\pm = -\frac a2 \pm i\beta$, with $\beta = \sqrt{\omega^2 - a^2/4} > 0$, and $p'(r_\pm) = 2r_\pm + a = \pm 2i\beta$.
>
> **Coefficients.** With $q(s) = su_0 + u_1 + au_0$,
>
> $$
> q(r_+) = u_1 + \tfrac a2 u_0 + i\beta u_0, \qquad \frac{q(r_+)}{p'(r_+)} = \frac{u_0}{2} - \frac{i}{2\beta}\Big(u_1 + \frac a2 u_0\Big) .
> $$
>
> Since $p$ and $q$ have real coefficients, the coefficient at $r_- = \bar r_+$ is the complex conjugate, and so is its exponential. The two terms of (2) are conjugates, and their sum is twice the real part:
>
> $$
> u(t) = 2\operatorname{Re}\Big[\frac{q(r_+)}{p'(r_+)}e^{r_+t}\Big] = 2e^{-at/2}\operatorname{Re}\Big[\Big(\frac{u_0}{2} - \frac{i}{2\beta}\Big(u_1 + \frac a2 u_0\Big)\Big)\big(\cos\beta t + i\sin\beta t\big)\Big] ,
> $$
>
> $$
> u(t) = e^{-at/2}\Big[u_0\cos(\beta t) + \frac{u_1 + au_0/2}{\beta}\sin(\beta t)\Big] .
> $$
>
> Check: $u(0) = u_0$, and $u'(0) = -\frac a2 u_0 + \beta\cdot\frac{u_1 + au_0/2}{\beta} = u_1$. Pairing conjugate roots this way is how the method produces real sines and cosines; [[§53★ Partial Differential Equations|§53★]] uses it again.
>
> *Powers: 6.2 (text)*

^ex-52-3

## Convolutions

> [!example] Example §52.4: A First-Order Equation Two Ways
> Solve $u' + au = f(t)$, $u(0) = u_0$.
>
> **By transform.** Transforming the entire equation gives $sU - u_0 + aU = F(s)$, so
>
> $$
> U(s) = \frac{u_0}{s + a} + \frac{1}{s + a}F(s) .
> $$
>
> The first term is the transform of $u_0e^{-at}$. If $F$ is rational, partial fractions invert the second.
>
> **By an integrating factor** ([[Integrating Factor Solution Formula|331 Thm. §4.2]]). Multiply by $e^{at}$:
>
> $$
> e^{at}(u' + au) = e^{at}f(t), \qquad \big(ue^{at}\big)' = e^{at}f(t), \qquad ue^{at} = \int_0^t e^{at'}f(t')\,dt' + c ,
> $$
>
> $$
> u(t) = \int_0^t e^{-a(t - t')}f(t')\,dt' + ce^{-at} ,
> $$
>
> and the initial condition requires $c = u_0$.
>
> **Comparison.** The two answers must agree, so
>
> $$
> \mathcal{L}\Big[\int_0^t e^{-a(t - t')}f(t')\,dt'\Big] = \frac{1}{s + a}F(s) .
> $$
>
> The transform of this combination of $e^{-at}$ and $f(t)$ is the product of their transforms. The convolution theorem says this always happens.
>
> *Powers: 6.2 (text)*

^ex-52-4

> [!definition] Definition §52.1: Convolution
> The **convolution** of $g$ and $f$ is
>
> $$
> g(t) * f(t) = \int_0^t g(t - t')f(t')\,dt' .
> $$
>
> *Powers: 6.2 (text)*

^def-52-1

*This is [[§26★ The Convolution Integral#^def-26-1|331 Def. §26.1]].*

> [!theorem] Theorem §52.3: The Convolution Theorem
> If $g(t)$ and $f(t)$ have Laplace transforms $G(s)$ and $F(s)$, respectively, then
>
> $$
> \mathcal{L}\Big[\int_0^t g(t - t')f(t')\,dt'\Big] = G(s)F(s) . \qquad (3)
> $$
>
> *Powers: 6.2, Theorem 2*

^thm-52-3

*Powers omits the proof; see [[§26★ The Convolution Integral#^thm-26-2|331 Thm. §26.2]].*

> [!remark]- Connections
> - In Boyce–DiPrima's language, $1/p(s)$ is the transfer function of the system and its inverse transform is the impulse response; the response to any input $f$ is the impulse response convolved with $f$: [[§26★ The Convolution Integral#^thm-26-3|331 Thm. §26.3]]. Example §52.5 is this structure.
> - The [[§15★ Complex Methods#^def-15-2|Fourier transform]] turns the convolution $\int_{-\infty}^{\infty} g(x - x')f(x')\,dx'$ on the whole line into a product in the same way. [[§27 Infinite Rod#^thm-27-3|Theorem §27.3]] (Powers 2.11) obtains the temperature in an infinite rod as such a convolution of the initial temperature with the heat kernel $e^{-x^2/4kt}/\sqrt{4\pi kt}$.

> [!theorem] Proposition §52.4: Rules of Convolution
> $$
> g * f = f * g, \qquad (4a)
> $$
>
> $$
> f * (g * h) = (f * g) * h, \qquad (4b)
> $$
>
> $$
> f * (g + h) = f * g + f * h . \qquad (4c)
> $$
>
> *Powers: 6.2, Equations (4a)–(4c)*

^prop-52-4

*Powers omits the proof ("it can be shown"); see [[§26★ The Convolution Integral#^prop-26-1|331 Prop. §26.1]].*

> [!example] Example §52.5: Solution Formulas by Convolution
> **(a) A general formula.** Solve $u'' - au = f(t)$, $u(0) = u_0$, $u'(0) = u_1$, with $a > 0$. The transformed equation $s^2U - su_0 - u_1 - aU = F(s)$ gives
>
> $$
> U(s) = \frac{su_0 + u_1}{s^2 - a} + \frac{1}{s^2 - a}F(s) .
> $$
>
> By the table ([[§51★ Definition and Elementary Properties#^thm-51-8|Theorem §51.8]], with $\sqrt a$ in place of $a$), $s/(s^2 - a)$ is the transform of $\cosh(\sqrt a\,t)$ and $1/(s^2 - a)$ the transform of $\sinh(\sqrt a\,t)/\sqrt a$. By the convolution theorem, for every $f$,
>
> $$
> u(t) = u_0\cosh\big(\sqrt a\,t\big) + \frac{u_1}{\sqrt a}\sinh\big(\sqrt a\,t\big) + \int_0^t \frac{\sinh\big(\sqrt a(t - t')\big)}{\sqrt a}f(t')\,dt' . \qquad (5)
> $$
>
> **(b) A mass struck while in motion.** The model $u'' + \omega^2u = f(t)$, $u(0) = u_0$, $u'(0) = u_1$, with $f(t) = F_0$ for $t_0 < t < t_1$ and $f(t) = 0$ otherwise, has
>
> $$
> U(s) = \frac{su_0 + u_1}{s^2 + \omega^2} + \frac{1}{s^2 + \omega^2}F(s), \qquad
> u(t) = u_0\cos(\omega t) + u_1\frac{\sin(\omega t)}{\omega} + \int_0^t \frac{\sin\big(\omega(t - t')\big)}{\omega}f(t')\,dt' .
> $$
>
> The convolution is easy to calculate, because $f$ vanishes outside $(t_0, t_1)$. For $t < t_0$ the integrand is $0$. For $t_0 < t < t_1$,
>
> $$
> \int_{t_0}^{t}\frac{\sin\big(\omega(t - t')\big)}{\omega}F_0\,dt' = F_0\Big[\frac{\cos\big(\omega(t - t')\big)}{\omega^2}\Big]_{t'=t_0}^{t'=t} = F_0\,\frac{1 - \cos\big(\omega(t - t_0)\big)}{\omega^2} ,
> $$
>
> and for $t > t_1$ the same antiderivative between $t_0$ and $t_1$ gives
>
> $$
> \int_0^t \frac{\sin\big(\omega(t - t')\big)}{\omega}f(t')\,dt' =
> \begin{cases}
> 0, & t < t_0, \\[4pt]
> F_0\,\dfrac{1 - \cos\big(\omega(t - t_0)\big)}{\omega^2}, & t_0 < t < t_1, \\[10pt]
> F_0\,\dfrac{\cos\big(\omega(t - t_1)\big) - \cos\big(\omega(t - t_0)\big)}{\omega^2}, & t_1 < t .
> \end{cases}
> $$
>
> After the force stops, $\cos(\omega(t - t_1)) - \cos(\omega(t - t_0)) = 2\sin\big(\tfrac12\omega(t_1 - t_0)\big)\sin\big(\omega(t - \tfrac12(t_0 + t_1))\big)$. The blow adds a free oscillation of amplitude $\frac{2F_0}{\omega^2}\big|\sin\big(\tfrac12\omega(t_1 - t_0)\big)\big|$, which vanishes when the force acts for a whole number of periods $2\pi/\omega$.
>
> **(c) The course version.** With $\omega = 1$ and $u_0 = u_1 = 0$, part (b) is the bonus problem of the 341 Practice Midterm 1: solve $u'' + u = f$, $u(0) = u'(0) = 0$, for a bounded $f$. Integrating by parts twice, the boundary terms vanish because $u(0) = u'(0) = 0$, so $\mathcal{L}(u'') = s^2U$ ([[§51★ Definition and Elementary Properties#^thm-51-4|Theorem §51.4]]). The transformed equation is $(s^2 + 1)U = F$, that is,
>
> $$
> U(s) = F(s)\cdot\frac{1}{s^2 + 1} = \mathcal{L}(f)\,\mathcal{L}(\sin t) ,
> $$
>
> and the convolution theorem gives
>
> $$
> u(t) = \int_0^t f(t - t')\sin(t')\,dt' ,
> $$
>
> which is the formula of (b) with $\omega = 1$, by the rule $g * f = f * g$ (4a).
>
> *Powers: 6.2 (text); Source: 341 Practice Midterm 1, Q9*

^ex-52-5
