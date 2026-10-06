---
type: section
subject: "[[Fourier Series and PDEs]]"
chapter: 3
section: 38
powers: "3.2"
aliases: ["Powers 3.2"]
tags: [fourier-series-and-pdes, math341]
---
← [[§37 The Vibrating String]] · ↑ [[· 3 The Wave Equation]] · [[§39 d'Alembert's Solution]] →

*Powers, Section 3.2 · MAT 341 lectures 10.29, 10.31, 11.5 · HW 10 · Midterm 2 · Practice Final.*

The vibrating string problem is solved by separation of variables, exactly as the heat problem of [[§25 Example꞉ Fixed End Temperatures|§25]]: the eigenvalue problem $\phi'' + \lambda^2\phi = 0$, $\phi(0) = \phi(a) = 0$ is the same, and only the time factor changes. Here it satisfies $T'' + \lambda^2c^2T = 0$ and oscillates instead of decaying. The product solutions are **standing waves**, each a fixed shape $\sin(n\pi x/a)$ whose amplitude oscillates with frequency $nc/(2a)$, and the solution is their superposition, with coefficients from the Fourier sine series of the initial displacement and the initial velocity. Because the frequencies are integer multiples of the lowest one, the motion is periodic in time, which is why a string sounds a musical note. Rewriting the series as an average of two shifted copies of the initial shape anticipates d'Alembert's solution ([[§39 d'Alembert's Solution|§39]]).

## Separation of Variables

The problem of [[§37 The Vibrating String#^def-37-3|Definition §37.3]] is

$$
\begin{aligned}
&\frac{\partial^2 u}{\partial x^2} = \frac{1}{c^2}\frac{\partial^2 u}{\partial t^2}, && 0 < x < a, \quad 0 < t, && (1) \\
&u(0, t) = 0, \quad u(a, t) = 0, && 0 < t, && (2) \\
&u(x, 0) = f(x), && 0 < x < a, && (3) \\
&\frac{\partial u}{\partial t}(x, 0) = g(x), && 0 < x < a . && (4)
\end{aligned}
$$

The partial differential equation and the boundary conditions are linear and homogeneous, so separation of variables may succeed. Assume $u(x, t) = \phi(x)T(t)$ ($T$ no longer means tension). Then (1) becomes $\phi''(x)T(t) = \frac{1}{c^2}\phi(x)T''(t)$, and dividing by $\phi T$,

$$
\frac{\phi''(x)}{\phi(x)} = \frac{T''(t)}{c^2T(t)}, \qquad 0 < x < a, \quad 0 < t .
$$

The left side depends only on $x$ and the right side only on $t$, so both are equal to a constant, written $-\lambda^2$:

$$
T'' + \lambda^2c^2T = 0, \quad 0 < t, \qquad (5) \qquad\qquad \phi'' + \lambda^2\phi = 0, \quad 0 < x < a . \qquad (6)
$$

The boundary conditions become $\phi(0)T(t) = 0$, $\phi(a)T(t) = 0$, and since $T(t) \equiv 0$ gives only the trivial solution $u \equiv 0$,

$$
\phi(0) = 0, \qquad \phi(a) = 0 . \qquad (7)
$$

The eigenvalue problem (6)–(7) was solved in [[§25 Example꞉ Fixed End Temperatures#^thm-25-2|Theorem §25.2]] (Powers 2.3): a positive separation constant ($\phi''/\phi = p^2 > 0$) or zero gives only $\phi \equiv 0$ (Powers' Exercise 3.2.18; the cases are worked in [[§38 Solution of the Vibrating String Problem#^ex-38-2|Example §38.2]]), and the eigenvalues and eigenfunctions are

$$
\lambda_n^2 = \Big(\frac{n\pi}{a}\Big)^2, \qquad \phi_n(x) = \sin(\lambda_nx), \qquad n = 1, 2, 3, \ldots .
$$

For $\lambda = \lambda_n$, equation (5) is the equation of simple harmonic motion with angular frequency $\lambda_nc$ ([[§23 Mechanical and Electrical Vibrations#^prop-23-2|331 Prop. §23.2]]), with general solution

$$
T_n(t) = a_n\cos(\lambda_nct) + b_n\sin(\lambda_nct) ,
$$

where $a_n$ and $b_n$ are arbitrary: there are two independent solutions. This is the substantial difference from the heat problem: there $T(t) = e^{-\lambda^2kt}$ tends to $0$ as $t \to \infty$, whereas here $T(t)$ has no limit but oscillates periodically, in agreement with intuition.

> [!definition] Definition §38.1: Standing Waves
> For each $n = 1, 2, 3, \ldots$ the product solutions
>
> $$
> u_n(x, t) = \sin(\lambda_nx)\big[a_n\cos(\lambda_nct) + b_n\sin(\lambda_nct)\big], \qquad \lambda_n = \frac{n\pi}{a}, \qquad (8)
> $$
>
> are called **standing waves**. For fixed $a_n$ and $b_n$, $u_n(x, t)$ keeps the same shape $\sin(\lambda_nx)$ with a variable, periodic amplitude. The points $x = ka/n$, $k = 0, 1, \ldots, n$, where $\sin(\lambda_nx) = 0$, never move; they are the **nodes** of $u_n$.
>
> *Powers: 3.2, Equation (8) and text*

^def-38-1

> [!theorem] Proposition §38.1: Standing Waves Solve the Homogeneous Problem
> For any constants $a_n$ and $b_n$, the standing wave $u_n(x, t)$ of (8) satisfies the wave equation (1) and the boundary conditions (2).
>
> *Powers: 3.2 (text); Exercise 3.2.1*

^prop-38-1

> [!proof]+ Proof
> Write $u_n = \phi_n(x)T_n(t)$ with $\phi_n(x) = \sin(\lambda_nx)$ and $T_n(t) = a_n\cos(\lambda_nct) + b_n\sin(\lambda_nct)$. Then
>
> $$
> \frac{\partial^2 u_n}{\partial x^2} = -\lambda_n^2\sin(\lambda_nx)\,T_n(t), \qquad
> \frac{\partial^2 u_n}{\partial t^2} = \sin(\lambda_nx)\big[-\lambda_n^2c^2a_n\cos(\lambda_nct) - \lambda_n^2c^2b_n\sin(\lambda_nct)\big] = -\lambda_n^2c^2\sin(\lambda_nx)\,T_n(t),
> $$
>
> so $\frac{1}{c^2}\partial^2u_n/\partial t^2 = -\lambda_n^2\sin(\lambda_nx)T_n(t) = \partial^2u_n/\partial x^2$, which is (1). At the ends, $\sin(0) = 0$ and $\sin(\lambda_na) = \sin(n\pi) = 0$, so $u_n(0, t) = u_n(a, t) = 0$ for all $t$, which is (2).

^pf-38-1

*Uses:* [[§38 Solution of the Vibrating String Problem#^def-38-1|Def. §38.1]]

![[m341-30-1.svg]]
*The first three standing waves $\sin(n\pi x/a)\cos(n\pi ct/a)$ at the times when the amplitude factor $\cos(n\pi ct/a)$ is $1$ (blue), $\frac12$, $0$ (gray), $-\frac12$ and $-1$ (red). The shape never changes, only its amplitude; the $n + 1$ nodes (black dots) stay at rest. Mode $n$ completes its oscillation $n$ times as fast as mode $1$.*

## The Series Solution

By the principle of superposition ([[§25 Example꞉ Fixed End Temperatures#^thm-25-4|Theorem §25.4]]), every finite linear combination of the $u_n$ also satisfies (1) and (2); the combination needs no new constants because the $a_n$ and $b_n$ are arbitrary. Taking an infinite series and requiring the initial conditions leads to the solution.

> [!theorem] Theorem §38.2: Series Solution of the Vibrating String Problem
> Let $f$ and $g$ be sectionally smooth on $0 < x < a$. The solution of the vibrating string problem (1)–(4) is
>
> $$
> u(x, t) = \sum_{n=1}^\infty \sin(\lambda_nx)\big[a_n\cos(\lambda_nct) + b_n\sin(\lambda_nct)\big], \qquad \lambda_n = \frac{n\pi}{a}, \qquad (9)
> $$
>
> with the coefficients
>
> $$
> a_n = \frac{2}{a}\int_0^a f(x)\sin\Big(\frac{n\pi x}{a}\Big)dx, \qquad (10) \qquad\qquad
> b_n = \frac{2}{n\pi c}\int_0^a g(x)\sin\Big(\frac{n\pi x}{a}\Big)dx . \qquad (11)
> $$
>
> That is, $a_n$ is the $n$th Fourier sine coefficient of the initial displacement $f$, and $b_n\lambda_nc$ is the $n$th Fourier sine coefficient of the initial velocity $g$.
>
> *Powers: 3.2, Equations (9)–(11)*

^thm-38-2

> [!proof]+ Proof
> *Powers gives this as a derivation that assumes the series may be differentiated term by term.*
>
> By [[§38 Solution of the Vibrating String Problem#^prop-38-1|Proposition §38.1]] and superposition, the series (9) satisfies the wave equation (1) and the boundary conditions (2) for any choice of $a_n$, $b_n$ (to the extent that it may be differentiated term by term). It remains to satisfy the initial conditions. At $t = 0$, $\cos(0) = 1$ and $\sin(0) = 0$, so (3) requires
>
> $$
> u(x, 0) = \sum_{n=1}^\infty a_n\sin\Big(\frac{n\pi x}{a}\Big) = f(x), \qquad 0 < x < a .
> $$
>
> Differentiating (9) term by term in $t$,
>
> $$
> \frac{\partial u}{\partial t}(x, t) = \sum_{n=1}^\infty \sin(\lambda_nx)\big[-a_n\lambda_nc\sin(\lambda_nct) + b_n\lambda_nc\cos(\lambda_nct)\big] ,
> $$
>
> and at $t = 0$ condition (4) requires
>
> $$
> \frac{\partial u}{\partial t}(x, 0) = \sum_{n=1}^\infty b_n\frac{n\pi}{a}c\,\sin\Big(\frac{n\pi x}{a}\Big) = g(x), \qquad 0 < x < a .
> $$
>
> Both are Fourier sine series problems: a given function on $0 < x < a$ is to be expanded in a series of $\sin(n\pi x/a)$ ([[§11 Even and Odd Functions; Half-Range Expansions#^def-11-4|Definition §11.4]]). In each case the constant multiplying $\sin(n\pi x/a)$ must be the Fourier sine coefficient of the given function. So $a_n$ is given by (10), and
>
> $$
> b_n\frac{n\pi}{a}c = \frac{2}{a}\int_0^a g(x)\sin\Big(\frac{n\pi x}{a}\Big)dx, \qquad\text{that is,}\qquad b_n = \frac{2}{n\pi c}\int_0^a g(x)\sin\Big(\frac{n\pi x}{a}\Big)dx ,
> $$
>
> which is (11). Since $f$ and $g$ are sectionally smooth, their sine series converge to them at every point of $0 < x < a$ where they are continuous ([[§12 Convergence of Fourier Series#^thm-12-1|Theorem §12.1]], for the odd periodic extension): the initial conditions really are satisfied, except possibly at points of discontinuity of $f$ or $g$.

^pf-38-2

*Uses:* [[§38 Solution of the Vibrating String Problem#^prop-38-1|§38.1]], [[§11 Even and Odd Functions; Half-Range Expansions#^def-11-4|Def. §11.4]] (sine series), [[§12 Convergence of Fourier Series#^thm-12-1|§12.1]] (convergence theorem)

By the nature of the problem one expects $f$, at least, to be continuous, with $f(0) = f(a) = 0$ (the string is attached at the ends). Then the sine series of $f$ converges uniformly ([[§13 Uniform Convergence#^thm-13-5|Theorem §13.5]]). That the formal series (9) really is a solution is best seen from its d'Alembert form, [[§39 d'Alembert's Solution#^thm-39-3|Theorem §39.3]] (see [[§39 d'Alembert's Solution#^rem-39-2|Remark: When Formula (13) Is a Classical Solution]]).

> [!remark]- Connections
> - The coefficients $\lambda_n = n\pi/a$, $\phi_n = \sin(\lambda_nx)$ are the eigenvalues and eigenfunctions of the regular Sturm–Liouville problem (6)–(7), and the sine coefficients (10), (11) are orthogonal projections onto them: [[§29 Sturm–Liouville Problems#^thm-29-2|Theorem §29.2]], [[§30 Expansion in Series of Eigenfunctions#^thm-30-2|Theorem §30.2]]. The finite-dimensional picture is the expansion of a vector in an orthogonal basis of eigenvectors of a symmetric matrix, [[§58★ Diagonalization of Symmetric Matrices#^thm-58-3|235 Thm. §58.3]].
> - Uniform convergence of (9) when $\sum(|a_n| + |b_n|) < \infty$ (as for (12) below, where $|a_n| \le 8h/(\pi^2n^2)$) is the Weierstrass M-test, [[§25 More on Uniform Convergence#^thm-25-3|451 Thm. §25.3]].

> [!remark] Remark: Method — Separation of Variables for the Vibrating String
> To solve $u_{tt} = c^2u_{xx}$ on $0 < x < a$ with homogeneous boundary conditions and initial data $u(x, 0) = f(x)$, $u_t(x, 0) = g(x)$ (the course's "standard steps"):
> 1. Put $u_n(x, t) = \phi(x)T(t)$ into the equation and the boundary conditions, and separate: $\phi''/\phi = T''/(c^2T) = p$, giving $\phi'' = p\phi$ with the boundary conditions translated to $\phi$, and $T'' = c^2pT$.
> 2. Solve the eigenvalue problem for $\phi$ in the three cases $p > 0$, $p = 0$, $p < 0$ (write $p = -\lambda^2$), keeping only the cases with nonzero solutions.
> 3. For each eigenvalue, solve for $T$: $T_n = a_n\cos(\lambda_nct) + b_n\sin(\lambda_nct)$ for $p = -\lambda_n^2 < 0$, and $T_0 = a_0 + b_0t$ if $p = 0$ is an eigenvalue. Write down the basic solutions $u_n = \phi_nT_n$.
> 4. Superpose, $u = \sum_n u_n$, and impose $u(x, 0) = f$ and $u_t(x, 0) = g$: both are eigenfunction expansions. Compute $a_n$ from $f$ and $b_n$ from $g$, remembering the factor $\lambda_nc$ in the $b_n$.
> 5. If the boundary conditions are not homogeneous, first subtract an equilibrium solution ([[§40 One-Dimensional Wave Equation꞉ Generalities#^def-40-2|Definition §40.2]]).

^rem-38-1

> [!example] Example §38.1: The Plucked String
> The string is lifted at the middle to height $h$ and released ([[§37 The Vibrating String#^ex-37-3|Example §37.3(a)]]):
>
> $$
> f(x) = \begin{cases} h\cdot\dfrac{2x}{a}, & 0 < x < \dfrac a2, \\[2mm] h\Big(2 - \dfrac{2x}{a}\Big), & \dfrac a2 < x < a, \end{cases} \qquad g(x) \equiv 0 .
> $$
>
> **Coefficients.** Since $g \equiv 0$, $b_n = 0$ for all $n$. Write $k = n\pi/a$. Integration by parts gives
>
> $$
> \int_0^{a/2} x\sin(kx)\,dx = \Big[-\frac{x\cos(kx)}{k}\Big]_0^{a/2} + \Big[\frac{\sin(kx)}{k^2}\Big]_0^{a/2} = -\frac{a\cos(n\pi/2)}{2k} + \frac{\sin(n\pi/2)}{k^2},
> $$
>
> $$
> \int_{a/2}^a\Big(2 - \frac{2x}{a}\Big)\sin(kx)\,dx = \Big[-\Big(2 - \frac{2x}{a}\Big)\frac{\cos(kx)}{k}\Big]_{a/2}^a - \frac{2}{ak}\int_{a/2}^a\cos(kx)\,dx = \frac{\cos(n\pi/2)}{k} + \frac{2\sin(n\pi/2)}{ak^2},
> $$
>
> using $\sin(ka) = \sin(n\pi) = 0$. Hence, by (10),
>
> $$
> a_n = \frac{2h}{a}\Big[\frac{2}{a}\Big(-\frac{a\cos(n\pi/2)}{2k} + \frac{\sin(n\pi/2)}{k^2}\Big) + \frac{\cos(n\pi/2)}{k} + \frac{2\sin(n\pi/2)}{ak^2}\Big] = \frac{2h}{a}\cdot\frac{4\sin(n\pi/2)}{ak^2} = \frac{8h}{\pi^2}\,\frac{\sin(n\pi/2)}{n^2} .
> $$
>
> The cosine terms cancel. Since $\sin(n\pi/2)$ is $0$ for even $n$ and $(-1)^{(n-1)/2}$ for odd $n$, only odd modes are present. The complete solution is
>
> $$
> u(x, t) = \frac{8h}{\pi^2}\sum_{n=1}^\infty \frac{\sin(n\pi/2)}{n^2}\sin\Big(\frac{n\pi x}{a}\Big)\cos\Big(\frac{n\pi ct}{a}\Big) = \frac{8h}{\pi^2}\Big[\sin\frac{\pi x}{a}\cos\frac{\pi ct}{a} - \frac19\sin\frac{3\pi x}{a}\cos\frac{3\pi ct}{a} + \cdots\Big] . \qquad (12)
> $$
>
> Each term is at most $8h/(\pi^2n^2)$ in absolute value and $\sum 1/n^2$ converges, so by the M-test the series (12) converges uniformly in $x$ and $t$ (Powers' Exercise 3.2.17). In the lecture the same computation is done with $h = 1$.
>
> **Shape at a given time.** In the form (12) it is hard to see what shape the string takes. By [[§38 Solution of the Vibrating String Problem#^prop-38-3|Proposition §38.3]] below, $u(x, t) = \frac12\big[\bar f_o(x - ct) + \bar f_o(x + ct)\big]$, where $\bar f_o$ is the odd $2a$-periodic extension of $f$, and the values can be read off the graph of $f$. For instance, at $x = 0.2a$, $t = 0.9a/c$,
>
> $$
> u\Big(0.2a, 0.9\frac ac\Big) = \frac12\big[\bar f_o(-0.7a) + \bar f_o(1.1a)\big] = \frac12\big[(-0.6h) + (-0.2h)\big] = -0.4h ,
> $$
>
> since $\bar f_o(-0.7a) = -f(0.7a) = -h(2 - 1.4) = -0.6h$ and $\bar f_o(1.1a) = \bar f_o(-0.9a) = -f(0.9a) = -0.2h$. The figure shows $u$ for several times: the corner of the initial triangle splits into two corners that travel apart with speed $c$, leaving a flat top; the horizontal portions of the string have a nonzero velocity. The displacement is periodic in time with period $2a/c$, and during the second half-period the string returns to its initial position through the same shapes.
>
> *Powers: 3.2, Example · Source: 341 lecture 10.29*

^ex-38-1

![[m341-30-2.svg]]
*The plucked string of Example §38.1 at times $ct = 0, 0.15a, \ldots, a$ (blue to red), computed from $u = \frac12[\bar f_o(x - ct) + \bar f_o(x + ct)]$ (equal to the series (12): its partial sum with 2000 terms differs from it by about $10^{-4}h$). The string is a trapezoid whose flat top descends at constant speed; at $ct = a/2$ it is flat, at $ct = a$ it is the initial triangle turned upside down.*

> [!theorem] Proposition §38.3: Solution as an Average of Two Shifted Copies of f
> Let $f$ be continuous and sectionally smooth on $0 \le x \le a$ with $f(0) = f(a) = 0$, let $g \equiv 0$, and let $\bar f_o$ be the odd periodic extension of $f$ with period $2a$, defined for all real arguments. Then the series solution (9) of the vibrating string problem is
>
> $$
> u(x, t) = \frac12\big[\bar f_o(x - ct) + \bar f_o(x + ct)\big] . \qquad (13)
> $$
>
> The graph of $\bar f_o(x + ct)$ is the graph of $\bar f_o$ shifted $ct$ units to the left, that of $\bar f_o(x - ct)$ is shifted $ct$ units to the right, and $u(x, t)$ is their average.
>
> *Powers: 3.2, Equation (13) and text*

^prop-38-3

> [!proof]+ Proof
> Powers carries out the computation for Example §38.1 and observes that it works for any $f$; here it is for any $f$. With $g \equiv 0$ all $b_n = 0$, and (9) is $u = \sum a_n\sin(\lambda_nx)\cos(\lambda_nct)$. By the identity
>
> $$
> \sin(A)\cos(B) = \frac12\big[\sin(A - B) + \sin(A + B)\big]
> $$
>
> with $A = \lambda_nx$, $B = \lambda_nct$, each term is $\frac12 a_n\big[\sin\big(n\pi(x - ct)/a\big) + \sin\big(n\pi(x + ct)/a\big)\big]$, so
>
> $$
> u(x, t) = \frac12\Big[\sum_{n=1}^\infty a_n\sin\Big(\frac{n\pi(x - ct)}{a}\Big) + \sum_{n=1}^\infty a_n\sin\Big(\frac{n\pi(x + ct)}{a}\Big)\Big]
> $$
>
> (both series converge, so the sum may be split). The series $\sum a_n\sin(n\pi y/a)$, with $a_n$ the sine coefficients (10) of $f$, is the Fourier series of the odd $2a$-periodic extension $\bar f_o$ ([[§11 Even and Odd Functions; Half-Range Expansions#^def-11-2|Definition §11.2]]). Under the hypotheses $\bar f_o$ is continuous on the whole line (the conditions $f(0) = f(a) = 0$ prevent jumps at multiples of $a$) and sectionally smooth, so its Fourier series converges to $\bar f_o(y)$ at every $y$ ([[§12 Convergence of Fourier Series#^thm-12-1|Theorem §12.1]]). Putting $y = x - ct$ and $y = x + ct$ gives (13).

^pf-38-3

*Uses:* [[§38 Solution of the Vibrating String Problem#^thm-38-2|§38.2]], [[§11 Even and Odd Functions; Half-Range Expansions#^def-11-2|Def. §11.2]] (odd periodic extension), [[§12 Convergence of Fourier Series#^thm-12-1|§12.1]]

Formula (13) gives $u$ without summing a series, for any $f$, as long as $g \equiv 0$. [[§39 d'Alembert's Solution#^thm-39-3|Theorem §39.3]] generalizes it to any $g$.

> [!example] Example §38.2: The Midterm Problem by Separation of Variables
> Solve
>
> $$
> \frac{\partial^2u}{\partial t^2} = 4\frac{\partial^2u}{\partial x^2}, \quad 0 < x < \pi; \qquad u(0, t) = u(\pi, t) = 0; \qquad u(x, 0) = x, \quad \frac{\partial u}{\partial t}(x, 0) = \sin(2x) .
> $$
>
> Here $c = 2$ and $a = \pi$.
>
> **(a) Separation.** Put $u_n = \phi(x)T(t)$: $\phi T'' = 4\phi''T$, so $\dfrac{\phi''}{\phi} = \dfrac{T''}{4T} = p$, a constant. Hence
>
> $$
> \phi'' = p\phi, \quad \phi(0) = 0, \quad \phi(\pi) = 0; \qquad T'' = 4pT .
> $$
>
> **(b) The three cases.**
> - $p = \mu^2 > 0$: $\phi = Ae^{\mu x} + Be^{-\mu x}$. Then $\phi(0) = A + B = 0$ and $\phi(\pi) = Ae^{\mu\pi} + Be^{-\mu\pi} = A(e^{\mu\pi} - e^{-\mu\pi}) = 0$. Since $e^{\mu\pi} \ne e^{-\mu\pi}$, $A = B = 0$: no nonzero solutions.
> - $p = 0$: $\phi = A + Bx$; $\phi(0) = A = 0$ and $\phi(\pi) = B\pi = 0$: no nonzero solutions.
> - $p = -\lambda^2 < 0$: $\phi = A\cos(\lambda x) + B\sin(\lambda x)$; $\phi(0) = A = 0$ and $\phi(\pi) = B\sin(\lambda\pi) = 0$, which allows $B \ne 0$ exactly when $\lambda = n$, $n = 1, 2, \ldots$. So $p_n = -n^2$ and $\phi_n = \sin(nx)$.
>
> Then $T_n'' = -4n^2T_n$, so $T_n = a_n\cos(2nt) + b_n\sin(2nt)$, and the basic solutions are $u_n = \sin(nx)\big[a_n\cos(2nt) + b_n\sin(2nt)\big]$.
>
> **(c) Coefficients.** By (10), integrating by parts,
>
> $$
> a_n = \frac{2}{\pi}\int_0^\pi x\sin(nx)\,dx = \frac{2}{\pi}\Big[-\frac{x\cos(nx)}{n}\Big]_0^\pi + \frac{2}{\pi n}\int_0^\pi\cos(nx)\,dx = -\frac{2\cos(n\pi)}{n} = \frac{2(-1)^{n+1}}{n} .
> $$
>
> By (11) with $c = 2$, and orthogonality ($\int_0^\pi\sin(2x)\sin(nx)\,dx$ is $\pi/2$ for $n = 2$ and $0$ otherwise),
>
> $$
> b_n = \frac{2}{2n\pi}\int_0^\pi\sin(2x)\sin(nx)\,dx = \begin{cases} \dfrac{1}{2\pi}\cdot\dfrac{\pi}{2} = \dfrac14, & n = 2, \\ 0, & n \ne 2 . \end{cases}
> $$
>
> So
>
> $$
> u(x, t) = \sum_{n=1}^\infty\frac{2(-1)^{n+1}}{n}\sin(nx)\cos(2nt) + \frac14\sin(2x)\sin(4t) .
> $$
>
> Here $f(x) = x$ does not vanish at $x = \pi$: the odd $2\pi$-periodic extension of $f$ is a sawtooth with jumps at odd multiples of $\pi$, its sine series converges only like $1/n$, and not uniformly. The series is still the solution in the sense of Theorem §38.2; its d'Alembert form ([[§39 d'Alembert's Solution#^ex-39-1|Example §39.1]]) shows the jumps travelling along the string.
>
> *Source: 341 Midterm 2, Q1(a)–(c)*

^ex-38-2

> [!example] Example §38.3: The Struck Piano String
> A hammer strikes the middle of a piano string at rest ([[§37 The Vibrating String#^ex-37-3|Example §37.3(b)]]):
>
> $$
> w_{tt} = c^2w_{xx}, \quad w(0, t) = w(a, t) = 0, \quad w(x, 0) = 0, \quad w_t(x, 0) = g(x) = \begin{cases} 2x/a, & 0 < x < a/2, \\ 2 - 2x/a, & a/2 < x < a . \end{cases}
> $$
>
> Since $f \equiv 0$, all $a_n = 0$. The function $g$ is the plucked shape of [[§38 Solution of the Vibrating String Problem#^ex-38-1|Example §38.1]] with $h = 1$, so its sine coefficients are $\frac2a\int_0^a g(x)\sin(n\pi x/a)\,dx = 8\sin(n\pi/2)/(n^2\pi^2)$, that is, $\int_0^a g(x)\sin(n\pi x/a)\,dx = 4a\sin(n\pi/2)/(n^2\pi^2)$. By (11),
>
> $$
> b_n = \frac{2}{n\pi c}\cdot\frac{4a\sin(n\pi/2)}{n^2\pi^2} = \frac{8a}{n^3\pi^3c}\sin\Big(\frac{n\pi}{2}\Big),
> \qquad
> w(x, t) = \sum_{n=1}^\infty\frac{8a\sin(n\pi/2)}{n^3\pi^3c}\sin\Big(\frac{n\pi x}{a}\Big)\sin\Big(\frac{n\pi ct}{a}\Big) .
> $$
>
> The coefficients now decay like $1/n^3$: integrating the velocity smooths the motion, and the solution has no corners travelling along the string ([[§39 d'Alembert's Solution#^ex-39-2|Example §39.2]], with a figure).
>
> The Practice Final asks for $u_{tt} = 4u_{xx}$, $0 < x < 2$, $u(x, 0) = 0$ and $u_t(x, 0) = x$ on $(0, 1)$, $2 - x$ on $(1, 2)$: this is the case $a = 2$, $c = 2$, and the solution is $u(x, t) = \sum_n \frac{8\sin(n\pi/2)}{n^3\pi^3}\sin\big(\frac{n\pi x}{2}\big)\sin(n\pi t)$.
>
> *Source: 341 HW 10, Problem 1(a); 341 Practice Final, Q7*

^ex-38-3

> [!example] Example §38.4: Free Ends and the Zero Eigenvalue
> Solve $u_{tt} = u_{xx}$, $0 < x < a$, with $u_x(0, t) = 0$, $u_x(a, t) = 0$, $u(x, 0) = f(x)$, $u_t(x, 0) = g(x)$. (Zero slope at the ends: the ends are free to slide vertically. The same problem describes the air pressure in a pipe open at both ends.)
>
> **(a) Separation.** $u_n = \phi(x)T(t)$ gives $\phi''/\phi = T''/T = p$, so $\phi'' = p\phi$, $\phi'(0) = 0$, $\phi'(a) = 0$, and $T'' = pT$.
>
> **(b) The three cases.**
> - $p = \mu^2 > 0$: $\phi = A\cosh(\mu x) + B\sinh(\mu x)$; $\phi'(0) = B\mu = 0$ and $\phi'(a) = A\mu\sinh(\mu a) = 0$ force $A = B = 0$.
> - $p = 0$: $\phi = A + Bx$; $\phi' = B = 0$, so $\phi_0 = 1$ (any constant) is an eigenfunction. Then $T'' = 0$ and $T_0 = A_0 + B_0t$.
> - $p = -\lambda^2 < 0$: $\phi = A\cos(\lambda x) + B\sin(\lambda x)$; $\phi'(0) = B\lambda = 0$ and $\phi'(a) = -A\lambda\sin(\lambda a) = 0$, so $\lambda_n = n\pi/a$ and $\phi_n = \cos(n\pi x/a)$, with $T_n = A_n\cos(n\pi t/a) + B_n\sin(n\pi t/a)$.
>
> The basic solutions are $u_0 = A_0 + B_0t$ and $u_n = \cos(n\pi x/a)\big[A_n\cos(n\pi t/a) + B_n\sin(n\pi t/a)\big]$.
>
> **(c) Coefficients.** With $u = A_0 + B_0t + \sum_{n\ge1}u_n$,
>
> $$
> u(x, 0) = A_0 + \sum_{n=1}^\infty A_n\cos\frac{n\pi x}{a} = f(x), \qquad u_t(x, 0) = B_0 + \sum_{n=1}^\infty\frac{n\pi}{a}B_n\cos\frac{n\pi x}{a} = g(x),
> $$
>
> two Fourier cosine series, so
>
> $$
> A_0 = \frac1a\int_0^a f(x)\,dx, \quad A_n = \frac2a\int_0^a f(x)\cos\frac{n\pi x}{a}\,dx, \quad B_0 = \frac1a\int_0^a g(x)\,dx, \quad B_n = \frac{2}{n\pi}\int_0^a g(x)\cos\frac{n\pi x}{a}\,dx .
> $$
>
> The zero eigenvalue, absent for fixed ends, contributes the term $A_0 + B_0t$: the average displacement $\frac1a\int_0^a u\,dx = A_0 + B_0t$ moves with the average initial velocity $B_0$ forever, since no end holds the string in place. Unless $\int_0^a g = 0$, the motion is a drift plus vibrations and is not periodic.
>
> *Source: 341 HW 10, Problem 2*

^ex-38-4

## Frequencies of Vibration

> [!definition] Definition §38.2: Frequencies of Vibration
> The multipliers $\lambda_nc$ of $t$ in the standing waves (8) are the **frequencies of vibration** in radians per unit time; $\lambda_nc/2\pi$ are the frequencies in cycles per unit time (hertz, if the time unit is the second). For the vibrating string the possible frequencies are
>
> $$
> \frac{(n\pi/a)c}{2\pi} = n\frac{c}{2a}, \qquad n = 1, 2, 3, \ldots .
> $$
>
> *(Powers prints this as $n\pi c/2a$, a misprint: the factor $\pi$ cancels.)*
>
> *Powers: 3.2 (text)*

^def-38-2

> [!theorem] Proposition §38.4: The String Vibrates Periodically
> The frequencies $nc/(2a)$ form an arithmetic sequence, all multiples of the lowest one, $c/(2a)$. Consequently the standing waves $u_n(x, t)$ have the common period $2a/c$, and the solution $u(x, t)$ of (9) is periodic in time with period $2a/c$.
>
> *Powers: 3.2 (text)*

^prop-38-4

> [!proof]+ Proof
> The $n$th standing wave depends on $t$ through $\cos(n\pi ct/a)$ and $\sin(n\pi ct/a)$, which have period $2a/(nc)$. Since $2a/c = n\cdot 2a/(nc)$ is an integer multiple of this period, $u_n(x, t + 2a/c) = u_n(x, t)$ for every $n$. Adding the terms of the series (9), $u(x, t + 2a/c) = u(x, t)$.

^pf-38-4

*Uses:* [[§38 Solution of the Vibrating String Problem#^def-38-2|Def. §38.2]], [[§38 Solution of the Vibrating String Problem#^thm-38-2|§38.2]]

> [!remark] Remark: Why a String Sounds a Note
> The lowest frequency, the **fundamental**, is
>
> $$
> \nu_1 = \frac{c}{2a} = \frac{1}{2a}\sqrt{\frac{T}{\rho}} ,
> $$
>
> and the others, the **overtones**, are its integer multiples $2\nu_1, 3\nu_1, \ldots$ (harmonics). Tightening the string (larger $T$) raises the pitch; a longer or heavier string lowers it; pressing a guitar string against a fret shortens $a$. The ear hears a sum of harmonics of one fundamental as a single musical note, whose timbre depends on the coefficients: the plucked string (12) has only odd harmonics with amplitudes $1/n^2$, the struck string of Example §38.3 has amplitudes $1/n^3$. For a nonuniform string or a beam the frequencies are not multiples of one fundamental, and the sound is not musical ([[§40 One-Dimensional Wave Equation꞉ Generalities#^rem-40-1|§40]]).

^rem-38-2
