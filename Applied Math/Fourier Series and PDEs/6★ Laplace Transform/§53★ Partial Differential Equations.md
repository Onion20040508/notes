---
type: section
subject: "[[Fourier Series and PDEs]]"
chapter: 6
section: 53
powers: "6.3"
aliases: ["Powers 6.3"]
tags: [fourier-series-and-pdes, math341, extension]
---
← [[§52★ Partial Fractions and Convolutions]] · ↑ [[· 6★ Laplace Transform]] · [[§54★ More Difficult Examples]] →

*Powers, Section 6.3.*
★ *Beyond MAT 341: the course did not cover this section; it is included from Powers.*

This section applies the Laplace transform in $t$ to a heat or wave problem on $0 < x < 1$, with $x$ held as a parameter. All time derivatives disappear: the partial differential equation becomes an ordinary differential equation in $x$ for $U(x, s)$, the boundary conditions are transformed with it, and the initial conditions enter through the derivative rule. Solving this boundary value problem is routine. Inverting the answer is not, because $U$ is usually a ratio of hyperbolic functions of $\sqrt s$ and is found in no table. Powers inverts it by an extension of Heaviside's formula: locate the values $r_n$ where $U$ becomes infinite and add up terms $A_n(x)e^{r_nt}$. For the heat equation the $r_n$ are the decay rates $-n^2\pi^2$, for the wave equation they are $\pm i\times$ the natural frequencies. The resulting series is the one separation of variables gives ([[§19 Example꞉ Fixed End Temperatures#^thm-19-5|Theorem §19.5]], [[§30 Solution of the Vibrating String Problem#^thm-30-2|Theorem §30.2]]), here produced without an eigenfunction expansion. [[§54★ More Difficult Examples|§54★]] shows the payoff when the boundary conditions depend on time.

## Transforming in t

> [!definition] Definition §53.1: Transform of a Function of x and t
> For a function $u(x, t)$, variables other than $t$ are treated as parameters, and the Laplace transform is taken in $t$:
>
> $$
> \mathcal{L}\big(u(x, t)\big) = \int_0^\infty e^{-st}u(x, t)\,dt = U(x, s) .
> $$
>
> $U$ is a function of $s$ and of the untransformed variable $x$. For instance, by the table ([[§51★ Definition and Elementary Properties#^thm-51-8|Theorem §51.8]]),
>
> $$
> \mathcal{L}\big(e^{-at}\sin(\pi x)\big) = \frac{1}{s + a}\sin(\pi x), \qquad
> \mathcal{L}\big(\sin(x + t)\big) = \mathcal{L}\big(\sin x\cos t + \cos x\sin t\big) = \frac{s\sin(x) + \cos(x)}{s^2 + 1} .
> $$
>
> *Powers: 6.3 (text)*

^def-53-1

> [!theorem] Theorem §53.1: Transforms of Partial Derivatives
> Derivatives with respect to the untransformed variable pass through the transform:
>
> $$
> \mathcal{L}\Big(\frac{\partial u}{\partial x}\Big) = \frac{\partial}{\partial x}U(x, s) = \frac{dU}{dx}, \qquad \mathcal{L}\Big(\frac{\partial^2 u}{\partial x^2}\Big) = \frac{d^2U}{dx^2} ,
> $$
>
> the ordinary-derivative notation keeping $s$ in the background as a parameter. Derivatives with respect to $t$ follow the rule of [[§51★ Definition and Elementary Properties#^thm-51-4|Theorem §51.4]]:
>
> $$
> \mathcal{L}\Big(\frac{\partial u}{\partial t}\Big) = s\mathcal{L}\big(u(x, t)\big) - u(x, 0), \qquad \mathcal{L}\Big(\frac{\partial^2 u}{\partial t^2}\Big) = s^2U(x, s) - su(x, 0) - \frac{\partial u}{\partial t}(x, 0) .
> $$
>
> *Powers: 6.3 (text)*

^thm-53-1

> [!proof]+ Proof
> **Time derivatives.** Fix $x$ and apply [[§51★ Definition and Elementary Properties#^thm-51-4|Theorem §51.4]] to $f(t) = u(x, t)$, by integration by parts as there. This assumes that $u$ and $u_t$ are continuous in $t$ (for the second formula), that the next derivative is sectionally continuous, and that all are of exponential order.
>
> **Space derivatives.** Powers assumes that $\partial/\partial x$ can be taken outside the integral:
>
> $$
> \mathcal{L}\Big(\frac{\partial u}{\partial x}\Big) = \int_0^\infty \frac{\partial u(x, t)}{\partial x}e^{-st}\,dt = \frac{\partial}{\partial x}\int_0^\infty u(x, t)e^{-st}\,dt = \frac{\partial}{\partial x}U(x, s) .
> $$
>
> Here is a sufficient condition. Suppose $u_x$ is continuous and $|u_x(x, t)| \le Me^{kt}$ for all $x$ in the interval and all $t \ge 0$, and let $\operatorname{Re}(s) > k$. By the mean value theorem in $x$,
>
> $$
> \frac{U(x + h, s) - U(x, s)}{h} = \int_0^\infty e^{-st}\,\frac{u(x + h, t) - u(x, t)}{h}\,dt = \int_0^\infty e^{-st}u_x(x + \theta h, t)\,dt
> $$
>
> for some $\theta = \theta(t, h) \in (0, 1)$. The integrand tends to $e^{-st}u_x(x, t)$ as $h \to 0$ and is bounded by $Me^{-(\operatorname{Re}(s) - k)t}$, which is integrable on $(0, \infty)$. By dominated convergence the limit may be taken inside the integral, which is the claim. Applying this to $u_x$ gives the formula for $u_{xx}$.

^pf-53-1

*Uses:* [[§51★ Definition and Elementary Properties#^thm-51-4|§51.4]], [[§29 The Mean Value Theorem#^thm-29-3|451 Thm. §29.3]] (mean value theorem), [[§15 The General Lebesgue Integral#^thm-15-8|551 Thm. §15.8]] (dominated convergence)

> [!remark]- Connections
> - Differentiation under the integral sign is a standard application of the dominated convergence theorem, [[§15 The General Lebesgue Integral#^thm-15-8|551 Thm. §15.8]]. The same argument in the transform variable, with $s$ in place of $x$, proves $\mathcal{L}(tf) = -F'(s)$ in [[§22 Solution of Initial Value Problems#^thm-22-6|331 Thm. §22.6]] (entry 19).

> [!remark] Remark: Method — Laplace Transform in t for a Heat or Wave Problem
> Given a boundary value–initial value problem in $x$ and $t$ (prepared, for example by dimensional analysis, so that as few parameters as possible remain):
> 1. **Transform** the partial differential equation *and the boundary conditions*, that is, everything valid for $t > 0$, by Theorem §53.1. The initial conditions are not transformed; they enter through $\mathcal{L}(u_t) = sU - u(x, 0)$ and $\mathcal{L}(u_{tt}) = s^2U - su(x, 0) - u_t(x, 0)$. A boundary value $u(0, t) = f(t)$ becomes $U(0, s) = F(s)$.
> 2. **Solve** the resulting ordinary boundary value problem in $x$ for $U(x, s)$, treating $s$ as a constant: a particular solution plus a combination of $\cosh(\sqrt s\,x)$, $\sinh(\sqrt s\,x)$ for the heat equation, or of $\cosh(sx)$, $\sinh(sx)$ for the wave equation.
> 3. **Invert.**
>    - If $U$ depends on $s$ only through elementary factors (the $x$-dependence riding along as constants), use the table ([[§51★ Definition and Elementary Properties#^thm-51-8|Theorem §51.8]]).
>    - Otherwise use the extended Heaviside formula (Remark: The Extended Heaviside Formula, below). Write $U = q(s)/p(s)$ and find the values $r_n$ where $U$ becomes infinite; $\cosh$, $\sinh$, $\cos$, $\sin$ and $\exp$ are never infinite, so these are the zeros of $p$ ([[§53★ Partial Differential Equations#^lem-53-2|Lemma §53.2]]). Compute $A_n(x) = \lim_{s\to r_n}(s - r_n)U(x, s)$, which is $q(r_n)/p'(r_n)$ at a simple zero. A point where this limit is $0$ contributes nothing. Combine conjugate roots into real terms.
> 4. **Assemble** $u(x, t) = \sum A_n(x)e^{r_nt}$, and check that the series converges and satisfies the problem. Compare with separation of variables when possible.

^rem-53-1

## Examples Inverted by the Table

> [!example] Example §53.1: A Heat Problem with a Single Mode
> Solve
>
> $$
> \frac{\partial^2u}{\partial x^2} = \frac{\partial u}{\partial t}, \quad 0 < x < 1,\ 0 < t; \qquad u(0, t) = 1,\quad u(1, t) = 1,\quad 0 < t; \qquad u(x, 0) = 1 + \sin(\pi x),\quad 0 < x < 1 .
> $$
>
> **Transform.** The partial differential equation and the boundary conditions are transformed, and the initial condition enters through $\mathcal{L}(u_t) = sU - u(x, 0)$:
>
> $$
> \frac{d^2U}{dx^2} = sU - \big(1 + \sin(\pi x)\big), \quad 0 < x < 1; \qquad U(0, s) = \frac1s, \quad U(1, s) = \frac1s .
> $$
>
> **Solve.** Try $U = \frac1s + c\sin(\pi x)$, which meets the boundary conditions. Then $U'' = -\pi^2c\sin(\pi x)$, while $sU - 1 - \sin(\pi x) = (sc - 1)\sin(\pi x)$. So $-\pi^2c = sc - 1$, $c = 1/(s + \pi^2)$, and
>
> $$
> U(x, s) = \frac1s + \frac{\sin(\pi x)}{s + \pi^2} .
> $$
>
> (For $s > 0$ this is the only solution: the difference of two solutions solves $U'' = sU$, $U(0) = U(1) = 0$, whose solutions $A\sinh(\sqrt s\,x)$ vanish at $x = 1$ only if $A = 0$.)
>
> **Invert.** As a function of $s$, $\sin(\pi x)$ is a constant, so the table gives
>
> $$
> u(x, t) = 1 + \sin(\pi x)\exp\big(-\pi^2t\big) :
> $$
>
> the steady state $1$ plus one decaying mode.
>
> *Powers: 6.3, Example 1*

^ex-53-1

> [!example] Example §53.2: A Wave Problem with a Single Mode
> Solve
>
> $$
> \frac{\partial^2u}{\partial x^2} = \frac{\partial^2u}{\partial t^2}, \quad 0 < x < 1,\ 0 < t; \qquad u(0, t) = 0,\quad u(1, t) = 0; \qquad u(x, 0) = \sin(\pi x),\quad \frac{\partial u}{\partial t}(x, 0) = -\sin(\pi x) .
> $$
>
> **Transform.** By $\mathcal{L}(u_{tt}) = s^2U - su(x, 0) - u_t(x, 0)$,
>
> $$
> \frac{d^2U}{dx^2} = s^2U - s\sin(\pi x) + \sin(\pi x), \quad 0 < x < 1; \qquad U(0, s) = 0, \quad U(1, s) = 0 .
> $$
>
> **Solve.** With $U = c\sin(\pi x)$: $-\pi^2c = s^2c - (s - 1)$, so
>
> $$
> U(x, s) = \frac{s - 1}{s^2 + \pi^2}\sin(\pi x) .
> $$
>
> **Invert.** $s/(s^2 + \pi^2)$ and $1/(s^2 + \pi^2)$ are the transforms of $\cos(\pi t)$ and $\sin(\pi t)/\pi$, so
>
> $$
> u(x, t) = \Big(\cos(\pi t) - \frac1\pi\sin(\pi t)\Big)\sin(\pi x) .
> $$
>
> Check: $u(x, 0) = \sin(\pi x)$ and $u_t(x, 0) = -\sin(\pi x)$. It is a single standing wave in the fundamental mode.
>
> *Powers: 6.3, Example 2*

^ex-53-2

## The Extended Heaviside Formula

When the initial condition is not a single eigenfunction, $U$ is no longer elementary. In Example §53.3 below (zero initial temperature, ends held at $1$) it is

$$
U(x, s) = \frac{\sinh(\sqrt s\,x) + \sinh\big(\sqrt s(1 - x)\big)}{s\sinh(\sqrt s)} ,
$$

a function that rarely appears in a table of transforms. Powers inverts it by extending Heaviside's formula ([[§52★ Partial Fractions and Convolutions#^thm-52-2|Theorem §52.2]]) from polynomials to transcendental functions.

> [!remark] Remark: The Extended Heaviside Formula
> When $U$ is the ratio of two transcendental functions (not polynomials) of $s$, write
>
> $$
> U(x, s) = \sum_n A_n(x)\frac{1}{s - r_n} .
> $$
>
> The numbers $r_n$ are the values of $s$ where the "denominator" of $U$ is zero, or rather where $|U(x, s)|$ becomes infinite; the $A_n$ are functions of $x$ but not of $s$. They are found as in [[§52★ Partial Fractions and Convolutions#^thm-52-2|Theorem §52.2]]: $A_n = \lim_{s\to r_n}(s - r_n)U(x, s)$, which equals $q(r_n)/p'(r_n)$ when $U = q/p$ and $r_n$ is a simple zero of $p$. From this form one expects
>
> $$
> u(x, t) = \sum_n A_n(x)\exp(r_nt) .
> $$
>
> This is not a theorem, and the solution should be checked for convergence.

^rem-53-2

> [!remark]- Remark: Why It Works
> Powers gives no justification; the standard one uses complex analysis, which the vault does not develop. The Laplace transform has an inversion formula, the **Bromwich integral**
>
> $$
> u(x, t) = \frac{1}{2\pi i}\int_{\sigma - i\infty}^{\sigma + i\infty} e^{st}\,U(x, s)\,ds ,
> $$
>
> taken along a vertical line $\operatorname{Re}(s) = \sigma$ to the right of all singularities of $U$. Suppose $U$ is a single-valued function of $s$ whose only singularities are poles $r_n$, and that it is small enough on a suitable sequence of large arcs in the left half-plane that pass between the poles. Then the line can be closed to the left, and the residue theorem turns the integral into the sum of the residues of $e^{st}U$. At a simple pole that residue is $A_n(x)e^{r_nt}$ with $A_n$ as above (compare the Connections of [[§52★ Partial Fractions and Convolutions#^thm-52-2|Theorem §52.2]]); at a double pole it is the expression of [[§54★ More Difficult Examples#^prop-54-2|Proposition §54.2]]. Two cautions follow.
> - **$U$ must be single-valued.** In Example §53.3, $U$ is an even function of $\sqrt s$, hence a function of $s$ alone (in Example §53.4, $\sqrt s$ does not occur); that is why "only the value of $s$, not the value of $\sqrt s$, is significant". When $\sqrt s$ enters otherwise, as $e^{-\sqrt s\,x}$ in [[§54★ More Difficult Examples#^ex-54-2|Example §54.2]], $s = 0$ is a branch point, and the method can only be used with care.
> - **The series must be checked.** The arcs condition can fail, and the formal series may then diverge or converge to the wrong function; Powers' instruction to check convergence (and the problem itself) is the practical safeguard.

^rem-53-3

> [!theorem] Lemma §53.2: Zeros of sinh and cosh
> For complex arguments the addition formulas hold, and $\cosh(iA) = \cos(A)$, $\sinh(iA) = i\sin(A)$. Hence, for real $\xi$, $\eta$,
>
> $$
> \sinh(\xi + i\eta) = \sinh(\xi)\cos(\eta) + i\cosh(\xi)\sin(\eta), \qquad \cosh(\xi + i\eta) = \cosh(\xi)\cos(\eta) + i\sinh(\xi)\sin(\eta) .
> $$
>
> Consequently:
> - (a) $\sinh(z) = 0$ if and only if $z = in\pi$, $n = 0, \pm1, \pm2, \ldots$; so $\sinh(\sqrt s) = 0$ exactly when $s = -n^2\pi^2$, $n = 0, 1, 2, \ldots$
> - (b) $\cosh(z) = 0$ if and only if $z = \pm i(2n - 1)\pi/2$, $n = 1, 2, \ldots$; so $\cosh(\sqrt s) = 0$ exactly when $s = -(2n - 1)^2\pi^2/4$.
>
> *Powers: 6.3 (text)*

^lem-53-2

> [!proof]+ Proof
> With $\cosh z = \frac12(e^z + e^{-z})$ and $\sinh z = \frac12(e^z - e^{-z})$ for complex $z$, the addition formulas follow from $e^{z + w} = e^ze^w$ exactly as for real arguments, and $\cosh(iA) = \frac12(e^{iA} + e^{-iA}) = \cos A$, $\sinh(iA) = \frac12(e^{iA} - e^{-iA}) = i\sin A$ by Euler's formula. So
>
> $$
> \sinh(\xi + i\eta) = \sinh\xi\cosh(i\eta) + \cosh\xi\sinh(i\eta) = \sinh\xi\cos\eta + i\cosh\xi\sin\eta ,
> $$
>
> and similarly for $\cosh$.
>
> **(a)** $\sinh(\xi + i\eta)$ is zero only if both its real and imaginary parts are zero:
>
> $$
> \sinh(\xi)\cos(\eta) = 0, \qquad \cosh(\xi)\sin(\eta) = 0 .
> $$
>
> Of the four possible combinations, only $\sinh\xi = 0$ and $\sin\eta = 0$ produce solutions (Powers asserts this; here is why). $\cosh\xi \ge 1$ is never zero, so the second equation forces $\sin\eta = 0$. Then $\cos\eta = \pm1 \ne 0$, and the first equation forces $\sinh\xi = 0$, that is, $\xi = 0$. Therefore $\xi = 0$ and $\eta = n\pi$. For $\sqrt s = \pm in\pi$ this gives $s = -n^2\pi^2$; both signs of the square root give the same $s$.
>
> **(b)** Now $\cosh\xi\cos\eta = 0$ and $\sinh\xi\sin\eta = 0$. Since $\cosh\xi \ne 0$, $\cos\eta = 0$, so $\sin\eta = \pm1$ and then $\sinh\xi = 0$, $\xi = 0$. Thus $z = i\eta$ with $\cos\eta = 0$, $\eta = \pm(2n - 1)\pi/2$.

^pf-53-2

> [!example] Example §53.3: Heating a Rod from Zero Temperature
> Solve
>
> $$
> \frac{\partial^2u}{\partial x^2} = \frac{\partial u}{\partial t}, \quad 0 < x < 1,\ 0 < t; \qquad u(0, t) = 1,\quad u(1, t) = 1; \qquad u(x, 0) = 0 ,
> $$
>
> a problem known to have a more complicated solution.
>
> **Transform and solve.** The transformed problem is
>
> $$
> \frac{d^2U}{dx^2} = sU, \quad 0 < x < 1; \qquad U(0, s) = \frac1s, \quad U(1, s) = \frac1s .
> $$
>
> The general solution is $U = A\cosh(\sqrt s\,x) + B\sinh(\sqrt s\,x)$. $U(0) = 1/s$ gives $A = 1/s$, and $U(1) = 1/s$ gives $B = (1 - \cosh\sqrt s)/(s\sinh\sqrt s)$. By the subtraction formula $\sinh\sqrt s\cosh(\sqrt s\,x) - \cosh\sqrt s\sinh(\sqrt s\,x) = \sinh(\sqrt s(1 - x))$,
>
> $$
> U(x, s) = \frac1s\cosh\big(\sqrt s\,x\big) + \frac{\big(1 - \cosh(\sqrt s)\big)\sinh(\sqrt s\,x)}{s\sinh(\sqrt s)} = \frac{\sinh(\sqrt s\,x) + \sinh\big(\sqrt s(1 - x)\big)}{s\sinh(\sqrt s)} .
> $$
>
> Numerator and denominator are both odd functions of $\sqrt s$, so $U$ depends only on $s$.
>
> **Singular points.** $\sinh$ is never infinite, so $U$ can become infinite only where $s = 0$ or $\sinh(\sqrt s) = 0$. By Lemma §53.2(a) these are $r_0 = 0$ and $r_n = -n^2\pi^2$, $n = 1, 2, \ldots$. The $A_n$ are computed piecemeal and the solution assembled at the end.
>
> **Part a ($r_0 = 0$).** Multiply the proposed development $U = \sum_{n\ge0} A_n(x)/(s - r_n)$ by $s - r_0 = s$ and let $s \to 0$. The right side tends to $A_0$. On the left, since $\sinh(z)/z \to 1$,
>
> $$
> \lim_{s\to0} s\,\frac{\sinh(\sqrt s\,x) + \sinh\big(\sqrt s(1 - x)\big)}{s\sinh(\sqrt s)} = x + (1 - x) = 1 = A_0(x) .
> $$
>
> So $s = 0$ contributes $1\cdot e^{0t} = 1$, the steady-state solution.
>
> **Part b ($r_n = -n^2\pi^2$).** With $q(s) = \sinh(\sqrt s\,x) + \sinh(\sqrt s(1 - x))$ and $p(s) = s\sinh(\sqrt s)$, $A_n = q(r_n)/p'(r_n)$. Take $\sqrt{r_n} = +in\pi$ in all calculations (the other choice changes the sign of both $q$ and $p'$, which are odd in $\sqrt s$, and leaves $A_n$ unchanged):
>
> $$
> p'(s) = \sinh\big(\sqrt s\big) + s\,\frac{1}{2\sqrt s}\cosh\big(\sqrt s\big), \qquad
> p'(r_n) = \tfrac12 in\pi\cosh(in\pi) = \tfrac12 in\pi\cos(n\pi) ,
> $$
>
> $$
> q(r_n) = \sinh(in\pi x) + \sinh\big(in\pi(1 - x)\big) = i\big[\sin(n\pi x) + \sin\big(n\pi(1 - x)\big)\big] .
> $$
>
> Hence the part of $u(x, t)$ that arises from $r_n$ is
>
> $$
> A_n(x)\exp(r_nt) = 2\,\frac{\sin(n\pi x) + \sin\big(n\pi(1 - x)\big)}{n\pi\cos(n\pi)}\exp\big(-n^2\pi^2t\big) .
> $$
>
> **Part c (assembly).**
>
> $$
> u(x, t) = 1 + \frac2\pi\sum_{n=1}^\infty \frac{\sin(n\pi x) + \sin\big(n\pi(1 - x)\big)}{n\cos(n\pi)}\exp\big(-n^2\pi^2t\big) .
> $$
>
> **Comparison with separation of variables.** Since $\sin(n\pi(1 - x)) = -\cos(n\pi)\sin(n\pi x)$, the numerator is $(1 - (-1)^n)\sin(n\pi x)$, and dividing by $\cos(n\pi) = (-1)^n$ gives $-2\sin(n\pi x)$ for odd $n$ and $0$ for even $n$:
>
> $$
> u(x, t) = 1 - \frac4\pi\sum_{n\ \text{odd}} \frac{\sin(n\pi x)}{n}\exp\big(-n^2\pi^2t\big) .
> $$
>
> This is the separation-of-variables solution in the form of [[§19 Example꞉ Fixed End Temperatures#^rem-19-1|§19]] (Method — The Steady-State/Transient Split): the steady state $1$ plus a transient $v$ with $v(x, 0) = -1$, whose sine coefficients are $-2\int_0^1\sin(n\pi x)\,dx = -2(1 - (-1)^n)/(n\pi)$. For $t \ge t_0 > 0$ the terms are bounded by $\frac4\pi e^{-n^2\pi^2t_0}$, so the series converges uniformly, together with its derivatives, and $u$ satisfies the heat equation and the boundary conditions. At $t = 0$ it is the sine series of $1 - 1 = 0$ on $0 < x < 1$.
>
> *Powers: 6.3, Example 3*

^ex-53-3

![[m341-53-1.svg]]
*The solution of Example §53.3, $u = 1 - \frac4\pi\sum_{n\ \text{odd}}\frac{\sin(n\pi x)}{n}e^{-n^2\pi^2t}$ (200 terms), at five times. Heat enters through both ends and the profile rises to the steady state $u = 1$ (dashed). By $t = 0.3$ only the $n = 1$ term, from the pole $s = -\pi^2$, is still visible: the pole closest to $s = 0$ sets the slowest rate of approach.*

> [!example] Example §53.4: A Wave Problem with a Free End
> Solve the wave problem
>
> $$
> \frac{\partial^2u}{\partial x^2} = \frac{\partial^2u}{\partial t^2}, \quad 0 < x < 1,\ 0 < t; \qquad u(0, t) = 0,\quad \frac{\partial u}{\partial x}(1, t) = 0; \qquad u(x, 0) = 0,\quad \frac{\partial u}{\partial t}(x, 0) = x .
> $$
>
> **Transform and solve.** The transformed problem is
>
> $$
> \frac{d^2U}{dx^2} = s^2U - x, \quad 0 < x < 1; \qquad U(0, s) = 0, \quad U'(1, s) = 0 .
> $$
>
> By undetermined coefficients, $x/s^2$ is a particular solution, so $U = x/s^2 + A\sinh(sx) + B\cosh(sx)$. $U(0) = 0$ gives $B = 0$, and $U'(1) = 1/s^2 + As\cosh(s) = 0$ gives $A = -1/(s^3\cosh s)$:
>
> $$
> U(x, s) = \frac{sx\cosh(s) - \sinh(sx)}{s^3\cosh(s)} .
> $$
>
> **Singular points.** The numerator is never infinite. The denominator is zero at $s = 0$ and, by Lemma §53.2(b), at $s = \pm i(2n - 1)\pi/2$, $n = 1, 2, \ldots$
>
> **Part a ($r_0 = 0$).** By the Taylor series of $\sinh$ and $\cosh$,
>
> $$
> sU(x, s) = \frac{sx\big(1 + \frac{s^2}{2} + \cdots\big) - \big(sx + \frac{s^3x^3}{6} + \cdots\big)}{s^2\big(1 + \frac{s^2}{2} + \cdots\big)} = \frac{s^3\big(\frac x2 - \frac{x^3}{6} + \cdots\big)}{s^2\big(1 + \frac{s^2}{2} + \cdots\big)} \to 0 .
> $$
>
> In spite of the formidable $s^3$ in the denominator, $s = 0$ is not really a singular point ($U$ tends to $\frac x2 - \frac{x^3}{6}$ there) and contributes nothing to $u(x, t)$.
>
> **Part b (the pairs $\pm i\rho_n$).** Label $\pm i(2n - 1)\pi/2 = \pm i\rho_n$, and take the roots in pairs. With $p(s) = s^3\cosh(s)$ and $q(s) = sx\cosh(s) - \sinh(sx)$, using $\cos\rho_n = 0$, $\sinh(i\rho) = i\sin(\rho)$ and $(\pm i)^4 = 1$:
>
> $$
> p'(s) = 3s^2\cosh(s) + s^3\sinh(s), \qquad p'(\pm i\rho_n) = (\pm i\rho_n)^3\sinh(\pm i\rho_n) = \rho_n^3\sin(\rho_n) ,
> $$
>
> $$
> q(\pm i\rho_n) = \pm i\rho_nx\cos(\rho_n) - \sinh(\pm i\rho_nx) = \mp i\sin(\rho_nx) .
> $$
>
> The two contributions together, by the exponential form of the sine:
>
> $$
> \frac{q(i\rho_n)}{p'(i\rho_n)}e^{i\rho_nt} + \frac{q(-i\rho_n)}{p'(-i\rho_n)}e^{-i\rho_nt} = \frac{\sin(\rho_nx)}{\rho_n^3\sin(\rho_n)}\,i\big(-e^{i\rho_nt} + e^{-i\rho_nt}\big) = \frac{2\sin(\rho_nx)\sin(\rho_nt)}{\rho_n^3\sin(\rho_n)} .
> $$
>
> **Part c.** Adding all the contributions,
>
> $$
> u(x, t) = 2\sum_{n=1}^\infty \frac{\sin(\rho_nx)\sin(\rho_nt)}{\rho_n^3\sin(\rho_n)}, \qquad \rho_n = \frac{(2n - 1)\pi}{2} .
> $$
>
> Since $\sin\rho_n = (-1)^{n+1}$, this is $u = 2\sum(-1)^{n+1}\sin(\rho_nx)\sin(\rho_nt)/\rho_n^3$. Separation of variables gives the same: the eigenfunctions for $X(0) = 0$, $X'(1) = 0$ are $\sin(\rho_nx)$ ([[§21 Example꞉ Different Boundary Conditions#^thm-21-1|Theorem §21.1]]), and $u = \sum b_n\sin(\rho_nx)\sin(\rho_nt)$ with $\rho_nb_n = 2\int_0^1 x\sin(\rho_nx)\,dx = 2\sin(\rho_n)/\rho_n^2$. The terms are bounded by $2/\rho_n^3$, so the series converges uniformly.
>
> *Powers: 6.3, Example 4*

^ex-53-4
