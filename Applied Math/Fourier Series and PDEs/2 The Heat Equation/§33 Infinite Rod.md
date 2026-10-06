---
type: section
subject: "[[Fourier Series and PDEs]]"
chapter: 2
section: 33
powers: "2.11"
aliases: ["Powers 2.11"]
tags: [fourier-series-and-pdes, math341]
---
← [[§32 Semi-Infinite Rod]] · ↑ [[· 2 The Heat Equation]] · [[§34★ The Error Function]] →

*Powers, Section 2.11 · MAT 341 lectures 10.22, 10.24 · HW 9 · Midterm 2, Practice Midterm 2.*

To study heat conduction in the middle of a very long rod, one may assume that it extends from $-\infty$ to $\infty$, so that there are no boundary conditions at all, only boundedness. Separation of variables then gives both $\cos(\lambda x)$ and $\sin(\lambda x)$ for every $\lambda \ge 0$, and the solution is a full Fourier integral ([[§18 Fourier Integral#^def-18-2|Definition §18.2]]) with time-dependent factors; this is how the course solved the infinite rod (lectures 10.22 and 10.24, HW 9, Midterm 2). Reversing the order of integration turns that integral into a single integral of the initial temperature against a Gaussian, the heat kernel. This form shows that heat spreads with infinite speed, so that a positive initial temperature on any interval makes the temperature positive everywhere at once, and it leads to the error function of [[§34★ The Error Function|§34★]].

## The Fourier Integral Solution

The problem to be solved is

$$
\begin{aligned}
\frac{\partial^2u}{\partial x^2} &= \frac1k\frac{\partial u}{\partial t}, && -\infty < x < \infty, \quad 0 < t, && (1) \\
u(x, 0) &= f(x), && -\infty < x < \infty, && (2) \\
|u(x, t)| &\ \text{bounded as } x \to \pm\infty . && && (3)
\end{aligned}
$$

With $u = \phi(x)T(t)$ the heat equation separates as before, $\phi''/\phi = T'/(kT) = \text{const}$.

> [!theorem] Proposition §33.1: Bounded Solutions on the Whole Line
> The equation $\phi'' = \mu\phi$, $-\infty < x < \infty$, has a nonzero solution bounded as $x \to \pm\infty$ only if $\mu \le 0$. For $\mu = -\lambda^2$, every solution
>
> $$
> \phi(x; \lambda) = A\cos(\lambda x) + B\sin(\lambda x)
> $$
>
> is bounded, and the accompanying factor is $T(t; \lambda) = \exp(-\lambda^2kt)$; $\lambda = 0$ gives the constants.
>
> *Powers: 2.11 (text)*

^prop-33-1

> [!proof]+ Proof
> If $\mu = \nu^2 > 0$, $\phi = Ae^{\nu x} + Be^{-\nu x}$; boundedness as $x \to \infty$ forces $A = 0$ and boundedness as $x \to -\infty$ forces $B = 0$. If $\mu = 0$, $\phi = A + Bx$, bounded only if $B = 0$, leaving the constants. If $\mu = -\lambda^2 < 0$, every solution $A\cos(\lambda x) + B\sin(\lambda x)$ is bounded by $|A| + |B|$. In every case $T'/(kT) = \mu$ gives $T = e^{\mu kt}$.

^pf-33-1

> [!theorem] Theorem §33.2: Fourier Integral Solution of the Infinite Rod Problem
> Let $f$ be sectionally smooth with $\int_{-\infty}^\infty |f(x)|\,dx$ finite, and let $A(\lambda)$, $B(\lambda)$ be its Fourier integral coefficient functions,
>
> $$
> A(\lambda) = \frac1\pi\int_{-\infty}^\infty f(x)\cos(\lambda x)\,dx, \qquad B(\lambda) = \frac1\pi\int_{-\infty}^\infty f(x)\sin(\lambda x)\,dx . \qquad (5)
> $$
>
> Then
>
> $$
> u(x, t) = \int_0^\infty \big(A(\lambda)\cos(\lambda x) + B(\lambda)\sin(\lambda x)\big)\exp(-\lambda^2kt)\,d\lambda \qquad (4)
> $$
>
> satisfies the partial differential equation (1) for $t > 0$ and the initial condition (2) (with the average $\frac12(f(x+) + f(x-))$ at jumps). For each $t > 0$, $u$ is bounded in $x$; if $f$ is bounded, $|u(x, t)| \le \sup|f|$ for all $x$ and $t$.
>
> *Powers: 2.11, Eqs. (4) and (5)*

^thm-33-2

> [!proof]+ Proof
> At $t = 0$ the exponential factor becomes $1$, and the initial condition reads
>
> $$
> \int_0^\infty \big(A(\lambda)\cos(\lambda x) + B(\lambda)\sin(\lambda x)\big)\,d\lambda = f(x), \qquad -\infty < x < \infty .
> $$
>
> This is a Fourier integral problem, so $A$ and $B$ must be the Fourier integral coefficient functions (5), and by the Fourier Integral Representation Theorem, [[§18 Fourier Integral#^thm-18-1|Theorem §18.1]], the left side equals $\frac12(f(x+) + f(x-))$.
>
> (Powers asserts that (4) then satisfies (1); here is why.) $|A(\lambda)|$, $|B(\lambda)| \le \frac1\pi\int|f| =: M$. For $t \ge t_1 > 0$, the integrand of (4) is bounded by $2Me^{-\lambda^2kt_1}$, and its derivatives $\partial^2/\partial x^2$ and $\frac1k\partial/\partial t$ by $2M\lambda^2e^{-\lambda^2kt_1}$, integrable over $0 < \lambda < \infty$. As in the proof of [[§32 Semi-Infinite Rod#^thm-32-2|Theorem §32.2]], differentiation under the integral sign is legitimate, and each $\big(A\cos(\lambda x) + B\sin(\lambda x)\big)e^{-\lambda^2kt}$ satisfies (1) by Proposition §33.1. The same bound gives $|u(x, t)| \le 2M\sqrt{\pi/(4kt)}$ for each $t > 0$. Powers adds that "it can be proved" that $u$ stays bounded if $f$ is; that follows from the kernel form, [[§33 Infinite Rod#^thm-33-3|Theorem §33.3]]: $|u| \le \sup|f|\cdot\frac{1}{\sqrt{4\pi kt}}\int e^{-(x' - x)^2/4kt}dx' = \sup|f|$.

^pf-33-2

*Uses:* [[§33 Infinite Rod#^prop-33-1|§33.1]], [[§18 Fourier Integral#^thm-18-1|§18.1]], [[§32 Semi-Infinite Rod#^thm-32-2|§32.2]], [[§33 Infinite Rod#^thm-33-3|§33.3]]

> [!example] Example §33.1: A Hot Center Section
> Solve (1)–(3) with
>
> $$
> f(x) = \begin{cases} 0, & x < -a, \\ T_0, & -a < x < a, \\ 0, & a < x . \end{cases}
> $$
>
> In words, the rod has a center section of length $2a$ whose temperature differs from that of the long sections to the left and right. Since $f$ is even, $B(\lambda) = 0$, and
>
> $$
> A(\lambda) = \frac1\pi\int_{-\infty}^\infty f(x)\cos(\lambda x)\,dx = \frac1\pi\int_{-a}^a T_0\cos(\lambda x)\,dx = \frac{2T_0}{\pi\lambda}\sin(\lambda a) .
> $$
>
> So the solution of the problem is
>
> $$
> u(x, t) = \frac{2T_0}{\pi}\int_0^\infty \frac{\sin(\lambda a)}{\lambda}\cos(\lambda x)\exp(-\lambda^2kt)\,d\lambda . \qquad (6)
> $$
>
> The figure suggests that $u(x, t)$ is positive for all $x$ when $t > 0$. This is indeed true (Remark below), and it illustrates an interesting property of the heat equation: the instantaneous transmission of information. The "hot" section $-a < x < a$ instantly raises the temperature everywhere else from its initial value $0$ to a positive value.
>
> *Powers: 2.11, Example*

^ex-33-1

![[m341-27-1.svg]]
*The solution (6) of Example §33.1 on $-3a < x < 3a$ at the dimensionless times $kt/a^2 = 0.01$, $1$ and $10$, with the initial block (dashed). The values were computed from the closed form $\frac{T_0}{2}\big[\operatorname{erf}\frac{a - x}{\sqrt{4kt}} + \operatorname{erf}\frac{a + x}{\sqrt{4kt}}\big]$ of [[§34★ The Error Function#^ex-34-1|Example §34.1]]. At every $t > 0$ the temperature is positive everywhere, however far from the hot section.*

## The Heat Kernel Form

Starting from the general form of the solution (4), Powers derives a second form.

> [!theorem] Theorem §33.3: The Heat Kernel Form of the Solution
> Under the hypotheses of Theorem §33.2, for $t > 0$,
>
> $$
> u(x, t) = \frac{1}{\sqrt{4k\pi t}}\int_{-\infty}^\infty f(x')\exp\Big[\frac{-(x' - x)^2}{4kt}\Big]dx' . \qquad (7)
> $$
>
> *Powers: 2.11, Eq. (7)*

^thm-33-3

> [!proof]+ Proof
> Change the variable of integration in (5) to $x'$ and substitute the formulas for $A(\lambda)$ and $B(\lambda)$ into (4):
>
> $$
> u(x, t) = \frac1\pi\int_0^\infty\Big[\int_{-\infty}^\infty f(x')\cos(\lambda x')\,dx'\cos(\lambda x) + \int_{-\infty}^\infty f(x')\sin(\lambda x')\,dx'\sin(\lambda x)\Big]\exp(-\lambda^2kt)\,d\lambda .
> $$
>
> Combining the terms with $\cos(\lambda x')\cos(\lambda x) + \sin(\lambda x')\sin(\lambda x) = \cos\big(\lambda(x' - x)\big)$,
>
> $$
> u(x, t) = \frac1\pi\int_0^\infty\int_{-\infty}^\infty f(x')\cos\big(\lambda(x' - x)\big)\,dx'\exp(-\lambda^2kt)\,d\lambda .
> $$
>
> **Reversing the order.** (Powers writes "if the order of integration may be reversed"; it may.) The integrand is bounded by $|f(x')|e^{-\lambda^2kt}$, whose double integral over $-\infty < x' < \infty$, $0 < \lambda < \infty$ is $\int|f|\,dx'\cdot\sqrt{\pi/(4kt)} < \infty$. By Fubini's theorem the order can be reversed:
>
> $$
> u(x, t) = \frac1\pi\int_{-\infty}^\infty f(x')\int_0^\infty \cos\big(\lambda(x' - x)\big)\exp(-\lambda^2kt)\,d\lambda\,dx' .
> $$
>
> **The inner integral.** Powers quotes it from his Miscellaneous Exercise 32 of Chapter 1 (complex integration); here is a real-variable derivation. For fixed $t > 0$ let
>
> $$
> J(y) = \int_0^\infty \cos(\lambda y)e^{-\lambda^2kt}\,d\lambda .
> $$
>
> With $\lambda = \sigma/\sqrt{kt}$ and $\int_0^\infty e^{-\sigma^2}d\sigma = \sqrt\pi/2$ ([[§34★ The Error Function#^prop-34-1|Proposition §34.1]](d)), $J(0) = \frac{1}{\sqrt{kt}}\cdot\frac{\sqrt\pi}{2} = \sqrt{\pi/(4kt)}$. Differentiating under the integral sign (the $y$-derivative of the integrand is dominated by $\lambda e^{-\lambda^2kt}$, which is integrable) and integrating by parts with $d\big(-e^{-\lambda^2kt}/(2kt)\big) = \lambda e^{-\lambda^2kt}d\lambda$,
>
> $$
> J'(y) = -\int_0^\infty \lambda\sin(\lambda y)e^{-\lambda^2kt}\,d\lambda = -\Big[-\frac{\sin(\lambda y)e^{-\lambda^2kt}}{2kt}\Big]_0^\infty - \frac{y}{2kt}\int_0^\infty \cos(\lambda y)e^{-\lambda^2kt}\,d\lambda = -\frac{y}{2kt}J(y) .
> $$
>
> This [[Integrating Factor Solution Formula|first-order linear equation]] with $J(0) = \sqrt{\pi/(4kt)}$ has the unique solution
>
> $$
> \int_0^\infty \cos\big(\lambda(x' - x)\big)\exp(-\lambda^2kt)\,d\lambda = J(x' - x) = \sqrt{\frac{\pi}{4kt}}\exp\Big[\frac{-(x' - x)^2}{4kt}\Big], \qquad t > 0 .
> $$
>
> Substituting, and using $\frac1\pi\sqrt{\pi/(4kt)} = 1/\sqrt{4k\pi t}$, gives (7).

^pf-33-3

*Uses:* [[§33 Infinite Rod#^thm-33-2|§33.2]], [[§34★ The Error Function#^prop-34-1|§34.1]], [[§25 Invariance Properties and Fubini's Theorem#^thm-25-6|551 Thm. §25.6]], [[§23 The Dominated Convergence Theorem#^thm-23-3|551 Thm. §23.3]], [[§5 Linear Differential Equations; Method of Integrating Factors#^thm-5-2|331 Thm. §5.2]] (first-order linear equations)

> [!remark]- Connections
> - The reversal of the order of integration is Fubini's theorem, [[§25 Invariance Properties and Fubini's Theorem#^thm-25-6|551 Thm. §25.6]], whose integrability hypothesis is checked with Tonelli's theorem, [[§25 Invariance Properties and Fubini's Theorem#^thm-25-3|551 Thm. §25.3]].
> - The normalization $\int_{-\infty}^\infty e^{-y^2}dy = \sqrt\pi$ behind the constant $1/\sqrt{4k\pi t}$: [[§25 Change of Variables on General Domains#^ex-25-4|452 Ex. §25.4]].

> [!remark] Remark: The Heat Kernel
> Formula (7) says $u(x, t) = \int_{-\infty}^\infty G(x - x', t)f(x')\,dx'$ with
>
> $$
> G(x, t) = \frac{1}{\sqrt{4k\pi t}}\exp\Big[-\frac{x^2}{4kt}\Big] ,
> $$
>
> the **heat kernel** (fundamental solution). It is itself a solution of the heat equation for $t > 0$ (differentiate, Powers' Exercise 2.11.5); it is positive; and $\int_{-\infty}^\infty G(x, t)\,dx = 1$ for every $t$ (Powers' Exercise 2.11.7 obtains this from (7) with $f \equiv 1$, whose solution is $u \equiv 1$). It is a Gaussian centered at $0$ whose width $\sqrt{2kt}$ grows like $\sqrt t$: as $t \to 0+$ it concentrates all its unit mass at $x = 0$, and as $t \to \infty$ it flattens out. Three consequences:
> - **Infinite speed of propagation.** If $f \ge 0$ and $f > 0$ on some interval, the integrand in (7) is positive there, so $u(x, t) > 0$ for every $x$ and every $t > 0$, as in Example §33.1.
> - **The initial condition.** Since $G$ has unit mass concentrating at $0$, $u(x, t) \to f(x)$ as $t \to 0+$ at each point where $f$ is continuous (and to the average at a jump).
> - **Maximum principle.** $\inf f \le u(x, t) \le \sup f$.
>
> Of the two forms, (4) and (7), each has its advantages. If $kt$ is large, the exponential in (4) is nearly zero except for small $\lambda$, and $\int_0^\Lambda$ with $\Lambda$ not large is accurate. If $kt$ is small, the exponential in (7) is nearly zero except for $x'$ near $x$, and $\frac{1}{\sqrt{4k\pi t}}\int_{x - h}^{x + h}$ with $h$ not large is accurate. Formula (7) requires no intermediate integrations, shows directly the influence of the initial condition, and does not need $\int|f| < \infty$ (for instance $f \equiv 1$ or $f = \operatorname{sgn} x$, [[§34★ The Error Function#^thm-34-2|Theorem §34.2]]). For Example §33.1 it gives
>
> $$
> u(x, t) = \frac{T_0}{\sqrt{4\pi kt}}\int_{-a}^a \exp\Big[\frac{-(x' - x)^2}{4kt}\Big]dx' , \qquad (8)
> $$
>
> which [[§34★ The Error Function#^ex-34-1|Example §34.1]] evaluates with the error function.

^rem-33-1

The semi-infinite rod of [[§32 Semi-Infinite Rod|§32]] can be treated the same way, by extending the initial temperature to an odd function.

> [!theorem] Proposition §33.4: The Semi-Infinite Rod in Heat Kernel Form
> The solution of $u_{xx} = \frac1ku_t$, $0 < x$, $0 < t$, $u(0, t) = 0$, $u(x, 0) = f(x)$ for $0 < x$ ([[§32 Semi-Infinite Rod#^thm-32-2|Theorem §32.2]]) can be expressed as
>
> $$
> u(x, t) = \frac{1}{\sqrt{4k\pi t}}\int_0^\infty f(x')\Big[\exp\Big(\frac{-(x' - x)^2}{4kt}\Big) - \exp\Big(\frac{-(x' + x)^2}{4kt}\Big)\Big]dx' .
> $$
>
> *Powers: Exercise 2.11.4*

^prop-33-4

> [!proof]+ Proof
> Following Powers' hint, solve the infinite-rod problem with initial condition $f_o$, the odd extension of $f$ ($f_o(x) = f(x)$ for $x > 0$, $f_o(x) = -f(-x)$ for $x < 0$). Its solution is odd in $x$: in (4), $f_o$ odd gives $A \equiv 0$, so $u$ is a sine integral, which vanishes at $x = 0$; restricted to $x > 0$ it therefore solves the semi-infinite problem, and its coefficient $B(\lambda) = \frac1\pi\int f_o\sin(\lambda x)\,dx = \frac2\pi\int_0^\infty f\sin(\lambda x)\,dx$ is that of [[§32 Semi-Infinite Rod#^thm-32-2|Theorem §32.2]]. Now use (7) and split the interval of integration at $0$:
>
> $$
> u = \frac{1}{\sqrt{4k\pi t}}\Big[\int_0^\infty f(x')e^{-(x' - x)^2/4kt}dx' + \int_{-\infty}^0 \big(-f(-x')\big)e^{-(x' - x)^2/4kt}dx'\Big] .
> $$
>
> In the second integral substitute $x' \to -x'$; it becomes $-\int_0^\infty f(x')e^{-(x' + x)^2/4kt}dx'$, which gives the stated formula. (The second exponential is the "image" of a source at $-x'$ of opposite sign, which keeps the end $x = 0$ at temperature $0$.)

^pf-33-4

*Uses:* [[§33 Infinite Rod#^thm-33-2|§33.2]], [[§33 Infinite Rod#^thm-33-3|§33.3]], [[§32 Semi-Infinite Rod#^thm-32-2|§32.2]]

## Examples

> [!example] Example §33.2: A Decaying Exponential on Half the Rod
> Solve
>
> $$
> u_t = u_{xx}, \quad -\infty < x < \infty, \ t > 0, \qquad u \ \text{bounded as } x \to \pm\infty, \qquad u(x, 0) = f(x) = \begin{cases} e^{-x}, & x > 0, \\ 0, & x < 0 . \end{cases}
> $$
>
> **(a)** With $u_\lambda = \phi(x)T(t)$: $T'/T = \phi''/\phi = \mu$, so $\phi'' = \mu\phi$, $T' = \mu T$, and $\phi$ is bounded as $x \to \pm\infty$.
>
> **(b)** By Proposition §33.1: $\mu = \nu^2 > 0$ gives $\phi = Ae^{\nu x} + Be^{-\nu x}$, and boundedness as $x \to \infty$ and $x \to -\infty$ forces $A = B = 0$; $\mu = 0$ gives the constants; $\mu = -\lambda^2$ gives $\phi = A\cos(\lambda x) + B\sin(\lambda x)$ for all $\lambda > 0$, with $T = e^{-\lambda^2t}$. The basic solutions are
>
> $$
> u_\lambda(x, t) = e^{-\lambda^2t}\big(A(\lambda)\cos(\lambda x) + B(\lambda)\sin(\lambda x)\big), \qquad \lambda \ge 0 .
> $$
>
> **(c)** By (5) and the integrals $\int_0^\infty e^{-x}\cos(\lambda x)\,dx = \frac{1}{1 + \lambda^2}$ and $\int_0^\infty e^{-x}\sin(\lambda x)\,dx = \lambda\int_0^\infty e^{-x}\cos(\lambda x)\,dx = \frac{\lambda}{1 + \lambda^2}$ ([[§32 Semi-Infinite Rod#^ex-32-3|Example §32.3]]),
>
> $$
> A(\lambda) = \frac{1}{\pi(1 + \lambda^2)}, \qquad B(\lambda) = \frac{\lambda}{\pi(1 + \lambda^2)}, \qquad u(x, t) = \frac1\pi\int_0^\infty \frac{\cos(\lambda x) + \lambda\sin(\lambda x)}{1 + \lambda^2}\,e^{-\lambda^2t}\,d\lambda .
> $$
>
> In closed form, $u = \frac12e^{t - x}\operatorname{erfc}\big((2t - x)/\sqrt{4t}\big)$ ([[§34★ The Error Function#^ex-34-3|Example §34.3]]).
>
> *The key restates the domain as $0 < x < \infty$, and in case $\mu > 0$ it uses $\phi(0) = 0$, a condition this problem does not have; boundedness as $x \to -\infty$ gives $B = 0$ instead, with the same conclusion.*
>
> *Source: 341 Midterm 2, Q2*

^ex-33-2

> [!example] Example §33.3: A Block and a Half Sine Wave
> **(a)** Solve $u_t = u_{xx}$ on $-\infty < x < \infty$ with $u$ bounded and $u(x, 0) = f(x)$, where $f = 1$ for $0 < x < \pi$ and $f = 0$ otherwise.
>
> The basic solutions are those of Example §33.2(b). The coefficients are
>
> $$
> A(\lambda) = \frac1\pi\int_0^\pi \cos(\lambda x)\,dx = \frac{\sin(\lambda\pi)}{\pi\lambda}, \qquad B(\lambda) = \frac1\pi\int_0^\pi \sin(\lambda x)\,dx = \frac{1 - \cos(\lambda\pi)}{\pi\lambda} ,
> $$
>
> so
>
> $$
> u(x, t) = \frac1\pi\int_0^\infty \frac{\sin(\lambda\pi)\cos(\lambda x) + (1 - \cos(\lambda\pi))\sin(\lambda x)}{\lambda}\,e^{-\lambda^2t}\,d\lambda = \frac1\pi\int_0^\infty \frac{\sin(\lambda x) + \sin\big(\lambda(\pi - x)\big)}{\lambda}\,e^{-\lambda^2t}\,d\lambda ,
> $$
>
> using $\sin(\lambda\pi)\cos(\lambda x) - \cos(\lambda\pi)\sin(\lambda x) = \sin(\lambda(\pi - x))$. The second form is visibly symmetric about $x = \pi/2$, the center of the block. In closed form, $u = \frac12\big[\operatorname{erf}\frac{x}{2\sqrt t} + \operatorname{erf}\frac{\pi - x}{2\sqrt t}\big]$ ([[§34★ The Error Function#^ex-34-2|Example §34.2]]).
>
> **(b)** The same with $u_t = 2u_{xx}$ and $f(x) = \sin x$ for $0 < x < \pi$, $0$ otherwise. Now $T = e^{-2\lambda^2t}$, and with $\sin x\cos(\lambda x) = \frac12\big(\sin((1 + \lambda)x) + \sin((1 - \lambda)x)\big)$ and $\cos((1 \pm \lambda)\pi) = -\cos(\lambda\pi)$,
>
> $$
> A(\lambda) = \frac1\pi\int_0^\pi \sin x\cos(\lambda x)\,dx = \frac{1}{2\pi}\Big(\frac{1 - \cos((\lambda + 1)\pi)}{\lambda + 1} + \frac{1 - \cos((1 - \lambda)\pi)}{1 - \lambda}\Big) = \frac{1 + \cos(\lambda\pi)}{\pi(1 - \lambda^2)} ,
> $$
>
> and, as in [[§32 Semi-Infinite Rod#^ex-32-2|Example §32.2]], $B(\lambda) = \frac1\pi\int_0^\pi \sin x\sin(\lambda x)\,dx = \frac{\sin(\lambda\pi)}{\pi(1 - \lambda^2)}$. Combining as in (a),
>
> $$
> u(x, t) = \frac1\pi\int_0^\infty \frac{\cos(\lambda x) + \cos\big(\lambda(\pi - x)\big)}{1 - \lambda^2}\,e^{-2\lambda^2t}\,d\lambda ,
> $$
>
> with a removable singularity at $\lambda = 1$ ($A(1) = 0$, $B(1) = \frac12$).
>
> *The Practice Midterm key ends its formula for $u$ with $dx$ in place of $d\lambda$.*
>
> *Source: 341 HW 9, Problem 3; 341 Practice Midterm 2, Q8*

^ex-33-3

> [!example] Example §33.4: A Gaussian Stays Gaussian
> The Gaussian distribution is $f_\sigma(x) = \frac{1}{\sqrt{2\pi\sigma^2}}e^{-x^2/2\sigma^2}$. Solve $u_t = u_{xx}$ on $-\infty < x < \infty$, $u$ bounded, with $u(x, 0) = f_2(x) = \frac{1}{\sqrt{8\pi}}e^{-x^2/8}$, using the Gaussian integral $\int_{-\infty}^\infty e^{-(x - ki)^2}dx = \sqrt\pi$ and $e^{ix} = \cos x + i\sin x$.
>
> **(a)** The basic solutions are $e^{-\lambda^2t}\big(A(\lambda)\cos(\lambda x) + B(\lambda)\sin(\lambda x)\big)$, as in Example §33.2.
>
> **(b)** $f_2$ is even, so $B = 0$. Since $\sin$ is odd, $A(\lambda) = \frac1\pi\int f_2(x)e^{i\lambda x}dx$, and completing the square, $-\frac{x^2}{8} + i\lambda x = -\frac18(x - 4i\lambda)^2 - 2\lambda^2$. With $x = \sqrt8\,y$ the hint gives $\int_{-\infty}^\infty e^{-(x - 4i\lambda)^2/8}dx = \sqrt{8\pi}$, so
>
> $$
> A(\lambda) = \frac1\pi\cdot\frac{1}{\sqrt{8\pi}}\cdot\sqrt{8\pi}\,e^{-2\lambda^2} = \frac1\pi e^{-2\lambda^2} .
> $$
>
> Then, by the inner integral of Theorem §33.3 (with $kt$ replaced by $t + 2$),
>
> $$
> u(x, t) = \frac1\pi\int_0^\infty e^{-(t + 2)\lambda^2}\cos(\lambda x)\,d\lambda = \frac1\pi\sqrt{\frac{\pi}{4(t + 2)}}\,e^{-x^2/4(t + 2)} = \frac{1}{\sqrt{2\pi(2t + 4)}}\,e^{-x^2/2(2t + 4)} = f_{\sqrt{2t + 4}}(x) .
> $$
>
> The solution is again a Gaussian, with variance $\sigma^2(t) = 4 + 2t$: the variance grows by $2kt$. (By (7), this is the statement that convolving Gaussians adds their variances.) The same computation in complex form, with the transform $C(\lambda)$, is [[§19★ Complex Methods#^ex-19-3|Example §19.3]].
>
> **(c)** At a fixed time $t_0$, $u(x, t_0) = \int_0^\infty A_{t_0}(\lambda)\cos(\lambda x)\,d\lambda$ with $A_{t_0}(\lambda) = \frac1\pi\int u(x, t_0)\cos(\lambda x)\,dx = \frac1\pi e^{-\lambda^2(t_0 + 2)}$.
>
> **(d)** Let $U_t(x) = u(x, t)$, with maxima at $x = 0$ and $\lambda = 0$ for $U_t$ and $A_t$. The half-widths $\Delta x$, $\Delta\lambda$ defined by $U_t(\Delta x)/U_t(0) = \frac12$ and $A_t(\Delta\lambda)/A_t(0) = \frac12$ satisfy $e^{-\Delta x^2/(4t + 8)} = \frac12$ and $e^{-\Delta\lambda^2(t + 2)} = \frac12$:
>
> $$
> \Delta x(t) = \sqrt{(4t + 8)\ln 2}, \qquad \Delta\lambda(t) = \sqrt{\frac{\ln 2}{t + 2}}, \qquad \Delta x\cdot\Delta\lambda = 2\ln 2 .
> $$
>
> As the heat spreads, the profile widens and its frequency content narrows in exact proportion: a Gaussian cannot be narrow in both $x$ and $\lambda$ (the uncertainty relation of Fourier analysis).
>
> *Source: 341 Midterm 2, Q3 (bonus)*

^ex-33-4
