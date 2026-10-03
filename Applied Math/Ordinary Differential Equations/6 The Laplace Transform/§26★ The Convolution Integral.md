---
type: section
subject: "[[Ordinary Differential Equations]]"
chapter: 6
section: 26
bdp: "6.6"
aliases: ["BDP 6.6"]
tags: [ordinary-differential-equations, math331, extension]
---
← [[§25 Impulse Functions]] · ↑ [[· 6 The Laplace Transform]] · [[§27 Introduction to Systems of First-Order Linear Equations]] →

*Boyce–DiPrima, Section 6.6.*
★ *Beyond MATH 331: the course skipped this section; it is included from Boyce–DiPrima as part of the chapter.*

The Laplace transform turns derivatives into multiplication by $s$, but it does not turn products into products: $\mathcal{L}\{fg\} \ne \mathcal{L}\{f\}\,\mathcal{L}\{g\}$ in general. The product of two transforms is instead the transform of the convolution $f \ast  g$, an integral that mixes the values of $f$ and $g$ over the whole past. This gives inverse transforms of products without partial fractions. More importantly, it gives a formula for the solution of $ay'' + by' + cy = g(t)$ with *any* forcing $g$: the solution with zero initial values is the convolution of $g$ with the impulse response of [[§25 Impulse Functions|§25]], the response of the system to $\delta(t)$. The transfer function $H(s) = 1/(as^2 + bs + c)$ depends only on the system, not on the input.

## The Convolution Theorem

> [!definition] Definition §26.1: Convolution
> For functions $f$ and $g$ defined on $t \ge 0$, the **convolution of $f$ and $g$** is the function
>
> $$
> h(t) = (f * g)(t) = \int_0^t f(t - \tau)\,g(\tau)\,d\tau . \qquad (2), (3)
> $$
>
> The integral is a **convolution integral**. The substitution $\xi = t - \tau$ turns it into $\int_0^t f(\xi)\,g(t - \xi)\,d\xi$, so it also equals
>
> $$
> (g * f)(t) = \int_0^t f(\tau)\,g(t - \tau)\,d\tau .
> $$
>
> The value $(f \ast  g)(t)$ depends on $f$ and $g$ on the whole interval $[0, t]$. Convolution integrals describe **hereditary systems**, whose behavior at time $t$ depends on their past history as well as their present state (neutron transport, viscoelasticity, population dynamics).
>
> *BDP: Theorem 6.6.1 and 6.6 (text), Equations (2) and (3)*

^def-26-1

> [!theorem] Proposition §26.1: Algebraic Properties of Convolution
> For piecewise continuous $f$, $g$, $g_1$, $g_2$, $h$ on $t \ge 0$:
>
> $$
> \begin{aligned}
> f * g &= g * f && \text{(commutative law)} \qquad (4) \\
> f * (g_1 + g_2) &= f * g_1 + f * g_2 && \text{(distributive law)} \qquad (5) \\
> (f * g) * h &= f * (g * h) && \text{(associative law)} \qquad (6) \\
> f * 0 &= 0 * f = 0 && \text{(zero property)} \qquad (7)
> \end{aligned}
> $$
>
> In (7), $0$ is the function that is identically zero.
>
> *BDP: 6.6 (text), Equations (4)–(7)*

^prop-26-1

> [!proof]+ Proof
> *BDP leaves the proofs to the reader (Problem 6.6.1).*
>
> **(4)** is the substitution $\xi = t - \tau$ of Definition §26.1: as $\tau$ runs from $0$ to $t$, $\xi$ runs from $t$ to $0$ and $d\tau = -d\xi$, so
>
> $$
> (f * g)(t) = \int_0^t f(t - \tau)g(\tau)\,d\tau = \int_t^0 f(\xi)g(t - \xi)\,(-d\xi) = \int_0^t g(t - \xi)f(\xi)\,d\xi = (g * f)(t) .
> $$
>
> **(5)** and **(7)** follow from linearity of the integral: $\int_0^t f(t - \tau)\big(g_1(\tau) + g_2(\tau)\big)d\tau$ splits into the two convolutions, and an integrand that is identically $0$ gives $0$ (use (4) for $0 \ast  f$).
>
> **(6)** Fix $t > 0$. By definition,
>
> $$
> \big((f * g) * h\big)(t) = \int_0^t (f * g)(t - \tau)\,h(\tau)\,d\tau = \int_0^t \Big(\int_0^{t - \tau} f(t - \tau - \sigma)\,g(\sigma)\,d\sigma\Big) h(\tau)\,d\tau .
> $$
>
> In the inner integral substitute $\sigma = u - \tau$ ($u$ from $\tau$ to $t$):
>
> $$
> = \int_0^t \Big(\int_\tau^t f(t - u)\,g(u - \tau)\,h(\tau)\,du\Big) d\tau .
> $$
>
> This is an iterated integral over the triangle $0 \le \tau \le u \le t$, of a bounded piecewise continuous function. Reversing the order of integration (Fubini's theorem on a bounded region, [[§17 Invariance Properties and Fubini's Theorem#^thm-17-6|551 Thm. §17.6]]), with $u$ from $0$ to $t$ outside and $\tau$ from $0$ to $u$ inside,
>
> $$
> = \int_0^t f(t - u)\Big(\int_0^u g(u - \tau)\,h(\tau)\,d\tau\Big) du = \int_0^t f(t - u)\,(g * h)(u)\,du = \big(f * (g * h)\big)(t) .
> $$

^pf-26-1

*Uses:* [[§26★ The Convolution Integral#^def-26-1|Def. §26.1]], [[§17 Invariance Properties and Fubini's Theorem#^thm-17-6|551 Thm. §17.6]] (Fubini's theorem)

Other properties of ordinary multiplication fail.

> [!example] Example §26.1: Convolution with 1
> In general $f * 1 \ne f$. Indeed
>
> $$
> (f * 1)(t) = \int_0^t f(t - \tau)\cdot 1\,d\tau = \int_0^t f(t - \tau)\,d\tau ,
> $$
>
> and for $f(t) = \cos t$
>
> $$
> (f * 1)(t) = \int_0^t \cos(t - \tau)\,d\tau = -\sin(t - \tau)\Big|_{\tau = 0}^{\tau = t} = -\sin 0 + \sin t = \sin t \ne \cos t .
> $$
>
> In fact $(f * 1)(t) = \int_0^t f(\xi)\,d\xi$ (substitute $\xi = t - \tau$): convolution with $1$ is integration from $0$, which matches $\mathcal{L}\{f * 1\} = F(s)\cdot\frac1s$ (Theorem §26.2). Similarly $f * f$ need not be nonnegative (BDP's Problem 6.6.3, with $f(t) = \sin t$).
>
> *BDP: 6.6 (text)*

^ex-26-1

> [!theorem] Theorem §26.2: The Convolution Theorem
> If $F(s) = \mathcal{L}\{f(t)\}$ and $G(s) = \mathcal{L}\{g(t)\}$ both exist for $s > a \ge 0$, then
>
> $$
> H(s) = F(s)\,G(s) = \mathcal{L}\{h(t)\}, \qquad s > a, \qquad (1)
> $$
>
> where $h = f * g$ is the convolution of Definition §26.1:
>
> $$
> h(t) = \int_0^t f(t - \tau)\,g(\tau)\,d\tau = \int_0^t f(\tau)\,g(t - \tau)\,d\tau . \qquad (2)
> $$
>
> Equivalently, $\mathcal{L}^{-1}\{F(s)G(s)\} = (f * g)(t)$: the transform of a convolution is the product of the transforms.
>
> *BDP: Theorem 6.6.1*

^thm-26-2

> [!proof]+ Proof
> Write both transforms with their own integration variables,
>
> $$
> F(s)G(s) = \int_0^\infty e^{-s\xi}f(\xi)\,d\xi \int_0^\infty e^{-s\tau}g(\tau)\,d\tau . \qquad (8)
> $$
>
> The integrand of the first integral does not depend on $\tau$, so $F(s)G(s)$ is an iterated integral:
>
> $$
> F(s)G(s) = \int_0^\infty e^{-s\tau}g(\tau)\Big(\int_0^\infty e^{-s\xi}f(\xi)\,d\xi\Big)d\tau = \int_0^\infty g(\tau)\Big(\int_0^\infty e^{-s(\xi + \tau)}f(\xi)\,d\xi\Big)d\tau . \qquad (9)
> $$
>
> For fixed $\tau$, substitute $\xi = t - \tau$ in the inner integral: $d\xi = dt$, $\xi = 0$ corresponds to $t = \tau$ and $\xi = \infty$ to $t = \infty$. So
>
> $$
> F(s)G(s) = \int_0^\infty g(\tau)\Big(\int_\tau^\infty e^{-st}f(t - \tau)\,dt\Big)d\tau . \qquad (10)
> $$
>
> This is an iterated integral over the wedge $0 \le \tau \le t < \infty$ of the $t\tau$-plane (figure below): for each $\tau$, $t$ runs from $\tau$ to $\infty$. Reverse the order of integration: for each $t \ge 0$, $\tau$ runs from $0$ to $t$. Then
>
> $$
> F(s)G(s) = \int_0^\infty e^{-st}\Big(\int_0^t f(t - \tau)\,g(\tau)\,d\tau\Big)dt = \int_0^\infty e^{-st}h(t)\,dt = \mathcal{L}\{h(t)\} . \qquad (11), (12)
> $$
>
> **The reversal of order.** (BDP assumes that the order of integration can be reversed; here is why, under the standing assumption of Chapter 6 that $f$ and $g$ are piecewise continuous and of exponential order $a$.) Exponential order gives $|f(t)| \le Ke^{at}$ only for $t \ge M$; but a piecewise continuous function is bounded on $[0, M]$, and $e^{at} \ge 1$ there because $a \ge 0$, so there are constants $K_1$, $K_2$ with $|f(t)| \le K_1e^{at}$ and $|g(t)| \le K_2e^{at}$ for *all* $t \ge 0$. On the wedge,
>
> $$
> \big|e^{-st}f(t - \tau)g(\tau)\big| \le K_1K_2\,e^{-st}e^{a(t - \tau)}e^{a\tau} = K_1K_2\,e^{-(s - a)t},
> \qquad
> \int_0^\infty\!\!\int_0^t K_1K_2\,e^{-(s - a)t}\,d\tau\,dt = K_1K_2\int_0^\infty t\,e^{-(s - a)t}\,dt = \frac{K_1K_2}{(s - a)^2} < \infty
> $$
>
> for $s > a$. So the integrand is absolutely integrable over the wedge, and by Tonelli's and Fubini's theorems ([[§17 Invariance Properties and Fubini's Theorem#^thm-17-3|551 Thm. §17.3]], [[§17 Invariance Properties and Fubini's Theorem#^thm-17-6|551 Thm. §17.6]]) both iterated integrals equal the double integral. (Each improper integral in (10) and (11) converges absolutely, so it agrees with the corresponding Lebesgue integral.) The same bound gives $|h(t)| \le K_1K_2\,te^{at}$ and $\int_0^\infty e^{-st}|h(t)|\,dt \le K_1K_2/(s - a)^2$, so $\mathcal{L}\{h\}$ exists (absolutely convergent) for $s > a$.

^pf-26-2

*Uses:* [[§26★ The Convolution Integral#^def-26-1|Def. §26.1]], [[§21 Definition of the Laplace Transform#^def-21-4|Def. §21.4]], [[§21 Definition of the Laplace Transform#^def-21-5|Def. §21.5]] (exponential order), [[§17 Invariance Properties and Fubini's Theorem#^thm-17-3|551 Thm. §17.3]], [[§17 Invariance Properties and Fubini's Theorem#^thm-17-6|551 Thm. §17.6]]

![[m331-26-1.svg]]
*The wedge $0 \le \tau \le t < \infty$ over which $F(s)G(s)$ is integrated. Equation (10) integrates along horizontal lines (red: fixed $\tau$, $t$ from $\tau$ to $\infty$); equation (11) along vertical segments (green: fixed $t$, $\tau$ from $0$ to $t$), and the inner integral along a vertical segment is exactly the convolution $h(t)$.*

> [!remark]- Connections
> - The interchange of order is Fubini's theorem for Lebesgue integrals, [[§17 Invariance Properties and Fubini's Theorem#^thm-17-6|551 Thm. §17.6]], made applicable by the absolute bound and Tonelli ([[§17 Invariance Properties and Fubini's Theorem#^thm-17-3|551 Thm. §17.3]]). Measure Theory has no item on convolution itself, so that is the only link.
> - See also: [[§52★ Partial Fractions and Convolutions#^thm-52-3|341 Thm. §52.3]] (the same theorem in Powers), with solution formulas for any forcing in [[§52★ Partial Fractions and Convolutions#^ex-52-5|341 Ex. §52.5]] and a forced vibrating wire inverted by convolution in [[§54★ More Difficult Examples#^ex-54-3|341 Ex. §54.3]].

> [!example] Example §26.2: An Inverse Transform by Convolution
> Find the inverse Laplace transform of $H(s) = \dfrac{a}{s^2(s^2 + a^2)}$.
>
> Think of $H$ as the product of $s^{-2} = \mathcal{L}\{t\}$ and $a/(s^2 + a^2) = \mathcal{L}\{\sin at\}$ ([[§22 Solution of Initial Value Problems#^thm-22-6|Theorem §22.6]], Table 6.2.1). By Theorem §26.2, integrating by parts with $u = t - \tau$, $dv = \sin(a\tau)\,d\tau$:
>
> $$
> h(t) = \int_0^t (t - \tau)\sin(a\tau)\,d\tau = \Big[-\frac{(t - \tau)\cos(a\tau)}{a}\Big]_{\tau = 0}^{\tau = t} - \int_0^t \frac{\cos(a\tau)}{a}\,d\tau = \frac{t}{a} - \frac{\sin(at)}{a^2} = \frac{at - \sin(at)}{a^2} . \qquad (14)
> $$
>
> The other form of (2), $h(t) = \int_0^t \tau\sin\big(a(t - \tau)\big)\,d\tau$, gives the same result. So does partial fractions: $\dfrac{a}{s^2(s^2 + a^2)} = \dfrac{1/a}{s^2} - \dfrac{1/a}{s^2 + a^2}$, with inverse $\dfrac{t}{a} - \dfrac{\sin at}{a^2}$.
>
> *BDP: Example 6.6.1*

^ex-26-2

## Input–Output Problems and the Transfer Function

Consider

$$
ay'' + by' + cy = g(t), \qquad y(0) = y_0, \quad y'(0) = y_0', \qquad (20), (21)
$$

with real constants $a$, $b$, $c$ and a given function $g$. Transforming and using the initial conditions,

$$
(as^2 + bs + c)Y(s) - (as + b)y_0 - ay_0' = G(s) .
$$

> [!definition] Definition §26.2: Transfer Function and Impulse Response
> The problem (20), (21) is an **input–output problem**: the coefficients $a$, $b$, $c$ describe a physical system, $g(t)$ is the **input** to the system, $y_0$ and $y_0'$ describe its initial state, and the solution $y(t)$ is the **output** at time $t$.
>
> The **transfer function** of the system is
>
> $$
> H(s) = \frac{1}{as^2 + bs + c} . \qquad (27)
> $$
>
> It depends only on the system ($a$, $b$, $c$), not on the input; with zero initial state it is the ratio of the transforms of the output and the input. Its inverse transform $h(t) = \mathcal{L}^{-1}\{H(s)\}$ is the **impulse response** of the system.
>
> *BDP: 6.6 (text), Equation (27)*

^def-26-2

> [!theorem] Theorem §26.3: Structure of the Solution of an Input–Output Problem
> The solution of (20), (21) is
>
> $$
> y(t) = \phi(t) + \psi(t), \qquad (24)
> $$
>
> where:
> - $\phi(t) = \mathcal{L}^{-1}\{\Phi(s)\}$, $\Phi(s) = \dfrac{(as + b)y_0 + ay_0'}{as^2 + bs + c}$, is the solution of $ay'' + by' + cy = 0$, $y(0) = y_0$, $y'(0) = y_0'$ (the free response to the initial state);
> - $\psi(t) = \mathcal{L}^{-1}\{\Psi(s)\}$, $\Psi(s) = H(s)G(s)$, is the solution of $ay'' + by' + cy = g(t)$, $y(0) = 0$, $y'(0) = 0$ (the response to the input), and
>
> $$
> \psi(t) = \int_0^t h(t - \tau)\,g(\tau)\,d\tau = (h * g)(t) ; \qquad (28)
> $$
>
> - the impulse response $h(t)$ is the solution of $ah'' + bh' + ch = \delta(t)$, $h(0) = 0$, $h'(0) = 0$. $\qquad (29)$
>
> So the response to an input is the convolution of the impulse response with the input.
>
> *BDP: 6.6 (text), Equations (22)–(29)*

^thm-26-3

> [!proof]+ Proof
> Solving the transformed equation for $Y(s)$,
>
> $$
> Y(s) = \frac{(as + b)y_0 + ay_0'}{as^2 + bs + c} + \frac{G(s)}{as^2 + bs + c} = \Phi(s) + \Psi(s), \qquad (22), (23)
> $$
>
> and inverting term by term gives (24). Setting $g = 0$ (so $G = 0$) in the same computation shows that $\Phi$ is the transform of the solution with data $y_0$, $y_0'$ and no forcing; setting $y_0 = y_0' = 0$ shows that $\Psi$ is the transform of the solution with forcing $g$ and zero data. By uniqueness of the inverse transform these are $\phi$ and $\psi$. Next, $\Psi(s) = H(s)G(s)$, and the Convolution Theorem §26.2 gives (28). Finally, if $g(t) = \delta(t)$ then $G(s) = 1$ ([[§25 Impulse Functions#^thm-25-2|Theorem §25.2]]) and $\Psi(s) = H(s)$, so $\psi = h$ solves (29).

^pf-26-3

*Uses:* [[§26★ The Convolution Integral#^def-26-2|Def. §26.2]], [[§26★ The Convolution Integral#^thm-26-2|§26.2]], [[§25 Impulse Functions#^thm-25-2|§25.2]], [[§22 Solution of Initial Value Problems#^prop-22-3|§22.3]] (the transformed equation), [[§22 Solution of Initial Value Problems#^thm-22-4|§22.4]] (uniqueness of the inverse transform)

> [!remark]- Connections
> - The same splitting $y = \phi + \psi$, for variable coefficients and without transforms: [[§18★ Variation of Parameters#^cor-18-2|Corollary §18.2]] (for the equation divided by $a$), where $\psi(t) = \int_{t_0}^t K(t, \tau)\,g(\tau)/a\,d\tau$ with the kernel $K(t, \tau) = \big(y_1(\tau)y_2(t) - y_1(t)y_2(\tau)\big)/W[y_1, y_2](\tau)$. For constant coefficients $K(t, \tau)/a = h(t - \tau)$ depends only on $t - \tau$, and the integral is the convolution (28).

Once $a$, $b$, $c$ are given, $\phi$ comes from the table, possibly after partial fractions or a translation. The input enters only through the convolution (28), which can be evaluated, numerically if necessary, for any $g$.

> [!example] Example §26.3: A Solution Formula for Any Input
> Find the solution of $y'' + 4y = g(t)$, $y(0) = 3$, $y'(0) = -1$.
>
> **Transform.** $s^2Y(s) - 3s + 1 + 4Y(s) = G(s)$, so
>
> $$
> Y(s) = \frac{3s - 1}{s^2 + 4} + \frac{G(s)}{s^2 + 4} = 3\,\frac{s}{s^2 + 4} - \frac12\,\frac{2}{s^2 + 4} + \frac12\,\frac{2}{s^2 + 4}\,G(s) .
> $$
>
> The first two terms carry the initial conditions, the last the forcing.
>
> **Invert.** With $\mathcal{L}\{\cos 2t\} = \frac{s}{s^2 + 4}$, $\mathcal{L}\{\sin 2t\} = \frac{2}{s^2 + 4}$ and Theorem §26.2,
>
> $$
> y = 3\cos 2t - \frac12\sin 2t + \frac12\int_0^t \sin\big(2(t - \tau)\big)\,g(\tau)\,d\tau .
> $$
>
> In the language of Theorem §26.3: the transfer function is $H(s) = 1/(s^2 + 4)$, the impulse response is $h(t) = \frac12\sin 2t$, $\phi(t) = 3\cos 2t - \frac12\sin 2t$ is the free response, and the integral is $\psi = h * g$. For a specific $g$ the integral can be evaluated, numerically if necessary. (This is the variation-of-parameters formula for this equation, [[§18★ Variation of Parameters#^cor-18-2|Corollary §18.2]] with $y_1 = \cos 2t$, $y_2 = \sin 2t$: its kernel $\frac{y_1(\tau)y_2(t) - y_1(t)y_2(\tau)}{W} = \frac12\sin 2(t - \tau)$ is $h(t - \tau)$.)
>
> *BDP: Example 6.6.2*

^ex-26-3

> [!remark] Remark: Step Response and Impulse Response
> Take $g = u_c$ in (28). Then $\psi(t) = \int_c^t h(t - \tau)\,d\tau = \int_0^{t - c} h(\sigma)\,d\sigma$ for $t \ge c$: the response to a unit step is the integral of the impulse response, delayed by $c$. In transforms: $\mathcal{L}\{u_c\}H(s) = e^{-cs}\,\frac{H(s)}{s}$. For the system $2y'' + y' + 2y$ of [[§24 Differential Equations with Discontinuous Forcing Functions#^ex-24-1|Example §24.1]] and [[§25 Impulse Functions#^ex-25-2|Example §25.2]], the impulse response is $h(t) = \frac{2}{\sqrt{15}}e^{-t/4}\sin\frac{\sqrt{15}}{4}t$ (Example §25.2 with the delay removed), and the function called $h$ in Example §24.1, $\mathcal{L}^{-1}\{1/(s(2s^2 + s + 2))\}$, is its integral $\int_0^t h$. The pulse response of Example §24.1 is the difference of two delayed step responses, and the responses to the pulses $d_\tau$ in the figure of §25 are $h * d_\tau(\cdot - 5)$.

^rem-26-1
