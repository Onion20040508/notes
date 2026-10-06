---
type: section
subject: "[[Fourier Series and PDEs]]"
chapter: 3
section: 31
powers: "3.3"
aliases: ["Powers 3.3"]
tags: [fourier-series-and-pdes, math341]
---
← [[§30 Solution of the Vibrating String Problem]] · ↑ [[· 3 The Wave Equation]] · [[§32 One-Dimensional Wave Equation꞉ Generalities]] →

*Powers, Section 3.3 · MAT 341 lectures 10.31, 11.5 · HW 10 · Midterm 2 · Practice Midterm 2 · Practice Final.*

In the plucked-string example of §30 ([[§30 Solution of the Vibrating String Problem#^ex-30-1|Example §30.1]]) the solution turned out to depend on $x$ and $t$ only through $x - ct$ and $x + ct$. In these variables the wave equation becomes $v_{zw} = 0$, which can be integrated directly: every solution is $\psi(x + ct) + \phi(x - ct)$, the superposition of a wave travelling left and a wave travelling right, both with speed $c$. This is **d'Alembert's solution**. For the vibrating string the two waves are found from the initial data, and the boundary conditions decide how the data must be extended beyond $0 < x < a$: the initial displacement by its odd $2a$-periodic extension, the integrated initial velocity by its even one. The result expresses $u$ in closed form, shows how the initial data travel and reflect at the fixed ends, and agrees with the series solution term by term.

## The General Solution of the Wave Equation

> [!theorem] Theorem §31.1: The Wave Equation in Characteristic Coordinates
> Let $w = x + ct$, $z = x - ct$, and $u(x, t) = v(w, z)$, where $v$ has continuous second partial derivatives. Then
>
> $$
> \frac{\partial^2 u}{\partial x^2} - \frac{1}{c^2}\frac{\partial^2 u}{\partial t^2} = 4\frac{\partial^2 v}{\partial z\,\partial w} ,
> $$
>
> so $u$ satisfies the wave equation $u_{xx} = u_{tt}/c^2$ if and only if
>
> $$
> \frac{\partial^2 v}{\partial z\,\partial w} = 0 .
> $$
>
> *Powers: 3.3 (text); Exercise 3.3.11*

^thm-31-1

> [!proof]+ Proof
> *Powers states the result and leaves the computation to Exercise 11.* Since $\partial w/\partial x = 1$, $\partial z/\partial x = 1$, $\partial w/\partial t = c$, $\partial z/\partial t = -c$, the chain rule gives
>
> $$
> \frac{\partial u}{\partial x} = \frac{\partial v}{\partial w} + \frac{\partial v}{\partial z}, \qquad
> \frac{\partial u}{\partial t} = \frac{\partial v}{\partial w}\frac{\partial w}{\partial t} + \frac{\partial v}{\partial z}\frac{\partial z}{\partial t} = c\frac{\partial v}{\partial w} - c\frac{\partial v}{\partial z} .
> $$
>
> Applying the same rules to these first derivatives, and using $v_{wz} = v_{zw}$ (the mixed partials are continuous),
>
> $$
> \frac{\partial^2 u}{\partial x^2} = v_{ww} + 2v_{wz} + v_{zz}, \qquad
> \frac{\partial^2 u}{\partial t^2} = c\big(cv_{ww} - cv_{wz}\big) - c\big(cv_{zw} - cv_{zz}\big) = c^2\big(v_{ww} - 2v_{wz} + v_{zz}\big) .
> $$
>
> Subtracting, $u_{xx} - u_{tt}/c^2 = 4v_{wz}$. Since the change of variables $(x, t) \mapsto (w, z)$ is one-to-one (with inverse $x = (w + z)/2$, $t = (w - z)/(2c)$), $u_{xx} = u_{tt}/c^2$ at every point exactly when $v_{zw} = 0$ at every point.

^pf-31-1

*Uses:* [[§94 The Chain Rule#^thm-94-2|Calc Thm. §94.2]] (chain rule), [[§92 Partial Derivatives#^thm-92-2|Calc Thm. §92.2]] (Clairaut)

> [!remark]- Connections
> - The chain rule for a change of variables in the plane, rigorously: [[§10 Composition of Functions and the Chain Rule#^thm-10-2|452 Thm. §10.2]]; equality of mixed partials: [[§5 Equality of Mixed Partials#^thm-5-1|452 Thm. §5.1]].
> - The lecture's version of the same computation: the operator factors as $\partial_t^2 - c^2\partial_x^2 = (\partial_t - c\partial_x)(\partial_t + c\partial_x)$, and the new coordinates are chosen so that the two factors become (multiples of) $\partial/\partial w$ and $\partial/\partial z$. The lines $x \pm ct = \text{const}$ are the **characteristics** of the wave equation; the classification of second-order equations as hyperbolic, parabolic and elliptic is [[§40★ Classification and Limitations#^def-40-1|Definition §40.1]] (Powers 4.6).

> [!theorem] Theorem §31.2: d'Alembert's General Solution
> If $\psi$ and $\phi$ are any twice differentiable functions of one variable, then
>
> $$
> u(x, t) = \psi(x + ct) + \phi(x - ct) \qquad (1)
> $$
>
> satisfies the wave equation $u_{xx} = u_{tt}/c^2$ for all $x$ and $t$. Conversely, every solution with continuous second partial derivatives on the whole $(x, t)$-plane has the form (1).
>
> *Powers: 3.3, Equation (1); Exercise 3.3.10*

^thm-31-2

> [!proof]+ Proof
> **(1) is a solution** (Exercise 10). By the chain rule, $u_{xx} = \psi''(x + ct) + \phi''(x - ct)$ and $u_{tt} = c^2\psi''(x + ct) + (-c)^2\phi''(x - ct)$, so $u_{tt} = c^2u_{xx}$.
>
> **Every solution has the form (1).** Let $v(w, z) = u(x, t)$ as in [[§31 d'Alembert's Solution#^thm-31-1|Theorem §31.1]], so $v_{zw} = 0$ on the whole $(w, z)$-plane. Written as
>
> $$
> \frac{\partial}{\partial z}\Big(\frac{\partial v}{\partial w}\Big) = 0 ,
> $$
>
> this says that $\partial v/\partial w$ is independent of $z$ (for fixed $w$, a function of $z$ with zero derivative on the whole line is constant):
>
> $$
> \frac{\partial v}{\partial w} = \theta(w) .
> $$
>
> Integrating in $w$ (for fixed $z$),
>
> $$
> v = \int\theta(w)\,dw + \phi(z) ,
> $$
>
> where $\phi(z)$ plays the role of an integration "constant". The integral of $\theta$ is a function of $w$ alone; calling it $\psi(w)$, $v(w, z) = \psi(w) + \phi(z)$. Transforming back, $u(x, t) = \psi(x + ct) + \phi(x - ct)$. (Explicitly, $\psi(w) = v(w, 0) - v(0, 0)$ and $\phi(z) = v(0, z)$, and these are twice differentiable because $v$ is.)

^pf-31-2

*Uses:* [[§31 d'Alembert's Solution#^thm-31-1|§31.1]], [[§94 The Chain Rule#^thm-94-2|Calc Thm. §94.2]]

> [!definition] Definition §31.1: d'Alembert's Solution; Travelling Waves
> The form (1), $u(x, t) = \psi(x + ct) + \phi(x - ct)$, is called **d'Alembert's solution** or the **travelling wave solution** of the wave equation. It represents the solution as the superposition of two waves with propagation speed $c$: the graph of $\phi(x - ct)$ is the graph of $\phi$ shifted $ct$ units to the right (a wave moving **right**), and the graph of $\psi(x + ct)$ is the graph of $\psi$ shifted $ct$ units to the left (a wave moving **left**).
>
> *Powers: 3.3 (text)*

^def-31-1

> [!remark] Remark: Names in the Lecture
> The lecture writes d'Alembert's solution as $u = \phi(x + ct) + \psi(x - ct)$, with the names of the two functions exchanged; Midterm 2 and the practice problems follow the lecture. These notes keep Powers' names throughout: $\psi$ for the left-moving wave and $\phi$ for the right-moving one. The lecture also describes the result as a superposition of standing waves: each standing wave $\sin(\lambda x)\cos(\lambda ct) = \frac12[\sin\lambda(x + ct) + \sin\lambda(x - ct)]$ is itself the sum of two travelling waves of the same frequency moving in opposite directions.

^rem-31-1

## The Vibrating String by d'Alembert's Method

Now consider the vibrating string problem of [[§29 The Vibrating String#^def-29-3|Definition §29.3]]:

$$
\begin{aligned}
&\frac{\partial^2 u}{\partial x^2} = \frac{1}{c^2}\frac{\partial^2 u}{\partial t^2}, && 0 < x < a, \quad 0 < t, && (2) \\
&u(0, t) = 0, \quad u(a, t) = 0, && 0 < t, && (3) \\
&u(x, 0) = f(x), && 0 < x < a, && (4) \\
&\frac{\partial u}{\partial t}(x, 0) = g(x), && 0 < x < a . && (5)
\end{aligned}
$$

A form for $u$ is known; the problem is to choose $\psi$ and $\phi$ so that the initial and boundary conditions hold.

> [!definition] Definition §31.2: The Integrated Initial Velocity G
> For the initial velocity $g$, let
>
> $$
> G(x) = \frac1c\int_0^x g(y)\,dy . \qquad (8)
> $$
>
> Equivalently, $G$ is the solution of the initial value problem $dG/dx = \frac1cg(x)$, $0 < x$, $G(0) = 0$ (at points where $g$ is continuous, by the [[Fundamental Theorem of Calculus|fundamental theorem of calculus]]). $\bar f_o$ denotes the odd periodic extension of $f$ with period $2a$, and $\bar G_e$ the even periodic extension of $G$ with period $2a$.
>
> *Powers: 3.3, Equation (8); Exercise 3.3.6*

^def-31-2

> [!theorem] Theorem §31.3: d'Alembert's Solution of the Vibrating String Problem
> The solution of the vibrating string problem (2)–(5) is
>
> $$
> u(x, t) = \frac12\big[\bar f_o(x + ct) + \bar f_o(x - ct)\big] + \frac12\big[\bar G_e(x + ct) - \bar G_e(x - ct)\big] , \qquad (13)
> $$
>
> where $\bar f_o$ is the odd $2a$-periodic extension of $f$ and $\bar G_e$ the even $2a$-periodic extension of $G(x) = \frac1c\int_0^x g(y)\,dy$. In d'Alembert's form (1), $u = \psi(x + ct) + \phi(x - ct)$ with
>
> $$
> \psi(x) = \frac12\big(\bar f_o(x) + \bar G_e(x) + A\big), \qquad \phi(x) = \frac12\big(\bar f_o(x) - \bar G_e(x) - A\big)
> $$
>
> for an arbitrary constant $A$, which cancels in (13).
>
> *Powers: 3.3, Equations (6)–(13)*

^thm-31-3

> [!proof]+ Proof
> **Initial conditions.** Assume $u(x, t) = \psi(x + ct) + \phi(x - ct)$ ([[§31 d'Alembert's Solution#^thm-31-2|Theorem §31.2]]). At $t = 0$, and differentiating in $t$ first,
>
> $$
> \psi(x) + \phi(x) = f(x), \qquad c\psi'(x) - c\phi'(x) = g(x), \qquad 0 < x < a . \qquad (6)
> $$
>
> Divide the second equation by $c$ and integrate from $0$ to $x$:
>
> $$
> \psi(x) - \phi(x) = G(x) + A, \qquad 0 < x < a , \qquad (7)
> $$
>
> with $G$ as in (8) and $A = \psi(0) - \phi(0)$ an arbitrary constant. Solving (6) and (7) simultaneously,
>
> $$
> \psi(x) = \frac12\big(f(x) + G(x) + A\big), \qquad \phi(x) = \frac12\big(f(x) - G(x) - A\big), \qquad 0 < x < a .
> $$
>
> **Extensions.** These equations give $\psi$ and $\phi$ only for arguments between $0$ and $a$, but $x \pm ct$ takes every value, so the functions must be extended:
>
> $$
> \psi(x) = \frac12\big(\tilde f(x) + \tilde G(x) + A\big), \qquad \phi(x) = \frac12\big(\tilde f(x) - \tilde G(x) - A\big),
> $$
>
> where $\tilde f$, $\tilde G$ are some extensions of $f$, $G$ ($\tilde f = f$ and $\tilde G = G$ on $0 < x < a$). However they are chosen, the wave equation (by Theorem §31.2) and the initial conditions are satisfied. So the extensions must be determined by the boundary conditions,
>
> $$
> u(0, t) = \psi(ct) + \phi(-ct) = 0, \qquad (9) \qquad\qquad u(a, t) = \psi(a + ct) + \phi(a - ct) = 0, \qquad t > 0 . \qquad (10)
> $$
>
> The first says $\tilde f(ct) + \tilde G(ct) + A + \tilde f(-ct) - \tilde G(-ct) - A = 0$, that is,
>
> $$
> \tilde f(ct) + \tilde f(-ct) + \tilde G(ct) - \tilde G(-ct) = 0 .
> $$
>
> Since $f$ and $G$ are not interdependent, Powers requires the two parts to vanish individually:
>
> $$
> \tilde f(ct) = -\tilde f(-ct), \qquad \tilde G(ct) = \tilde G(-ct) : \qquad (11)
> $$
>
> $\tilde f$ is odd and $\tilde G$ is even. At the second endpoint the same calculation gives $\tilde f(a + ct) + \tilde f(a - ct) + \tilde G(a + ct) - \tilde G(a - ct) = 0$, and again individually
>
> $$
> \tilde f(a + ct) = -\tilde f(a - ct), \qquad \tilde G(a + ct) = \tilde G(a - ct) . \qquad (12)
> $$
>
> Using oddness and evenness on the right sides, $\tilde f(a + ct) = \tilde f(-a + ct)$ and $\tilde G(a + ct) = \tilde G(-a + ct)$: changing the argument by $2a$ does not change the value, so both are periodic with period $2a$. Hence $\tilde f = \bar f_o$, the odd periodic extension of $f$, and $\tilde G = \bar G_e$, the even periodic extension of $G$, and
>
> $$
> \psi(x + ct) = \frac12\big(\bar f_o(x + ct) + \bar G_e(x + ct) + A\big), \qquad \phi(x - ct) = \frac12\big(\bar f_o(x - ct) - \bar G_e(x - ct) - A\big) .
> $$
>
> Adding gives (13).
>
> **Check.** (Powers' "individually" is a choice, not a deduction; here is why the choice works.) With $\tilde f = \bar f_o$ and $\tilde G = \bar G_e$ each part of (9) vanishes, by oddness and evenness. For (10): $\bar f_o(a - ct) = -\bar f_o(ct - a) = -\bar f_o(ct + a)$ by oddness and $2a$-periodicity, and likewise $\bar G_e(a - ct) = \bar G_e(ct - a) = \bar G_e(ct + a)$, so both parts of (10) vanish. At $t = 0$, (13) gives $u(x, 0) = \bar f_o(x) = f(x)$, and $u_t(x, 0) = \frac c2\big[\bar G_e'(x) + \bar G_e'(x)\big] = cG'(x) = g(x)$ for $0 < x < a$ (the $\bar f_o'$ terms cancel). So (13) satisfies (2)–(5).

^pf-31-3

*Uses:* [[§31 d'Alembert's Solution#^thm-31-2|§31.2]], [[§31 d'Alembert's Solution#^def-31-2|Def. §31.2]], [[§7 Arbitrary Period and Half-Range Expansions#^def-7-3|Def. §7.3]] (odd and even periodic extensions)

![[m341-31-1.svg]]
*d'Alembert's construction for the plucked string of [[§30 Solution of the Vibrating String Problem#^ex-30-1|Example §30.1]] at $ct = 0.3a$. The odd $2a$-periodic extension $\bar f_o$ is shifted $ct$ to the left (blue) and $ct$ to the right (red, dashed); on $0 < x < a$ (shaded) their average is the string (black), a trapezoid. The two waves are point reflections of each other through the ends $(0, 0)$ and $(a, 0)$, which is how the fixed ends act: a wave arriving at an end comes back inverted.*

> [!remark] Remark: When Formula (13) Is a Classical Solution
> Formula (13) has continuous second derivatives exactly when $\bar f_o$ and $\bar G_e$ do: $f$ twice continuously differentiable with $f(0) = f(a) = 0$ and $f''(0) = f''(a) = 0$, and $g$ continuously differentiable with $g(0) = g(a) = 0$ (these make the odd and even extensions smooth across the ends). For a plucked string, $f$ has a corner; then (13) still satisfies the initial and boundary conditions and the wave equation away from the lines $x \pm ct =$ (corner position $+ 2ka$), along which the corners travel. It is the physically correct motion, and it equals the series (9), which converges uniformly. This is the precise sense in which the series solutions of [[§30 Solution of the Vibrating String Problem#^thm-30-2|Theorem §30.2]] are solutions.

^rem-31-2

> [!remark] Remark: Method — d'Alembert's Method for the Vibrating String
> To solve (2)–(5) by d'Alembert's method (the lecture's steps):
> 1. Write $u(x, t) = \psi(x + ct) + \phi(x - ct)$.
> 2. Compute $G(x) = \frac1c\int_0^x g(y)\,dy$ on $0 < x < a$; then $\psi = \frac12(f + G + A)$ and $\phi = \frac12(f - G - A)$ there.
> 3. Extend: $\bar f_o$ odd and $\bar G_e$ even, both with period $2a$ (state the extensions explicitly). The constant $A$ is arbitrary; it may be chosen to cancel the constant term of $\bar G_e$.
> 4. For a formula, expand $\bar f_o(x) = \sum a_n\sin(n\pi x/a)$ and $\bar G_e(x) = \gamma_0 + \sum\gamma_n\cos(n\pi x/a)$, and substitute $x + ct$ and $x - ct$; or leave $u$ in the form (13).
> 5. For a sketch of $u(\cdot, t^*)$ when $g \equiv 0$: sketch $\bar f_o(x)$; sketch $\bar f_o(x + ct^*)$ (shifted $ct^*$ to the left) and $\bar f_o(x - ct^*)$ (shifted $ct^*$ to the right) on the same axes; average them graphically; check the boundary conditions. If $f \equiv 0$, do the same with $\bar G_e(x + ct^*)$ and $-\bar G_e(x - ct^*)$ (shifted right and reflected in the horizontal axis).

^rem-31-3

> [!theorem] Proposition §31.4: d'Alembert's Solution Agrees with the Series Solution
> Let $a_n$ and $b_n$ be the coefficients (10), (11) of the series solution [[§30 Solution of the Vibrating String Problem#^thm-30-2|Theorem §30.2]]. Then
>
> $$
> \bar f_o(x) = \sum_{n=1}^\infty a_n\sin\frac{n\pi x}{a}, \qquad \bar G_e(x) = \gamma_0 - \sum_{n=1}^\infty b_n\cos\frac{n\pi x}{a}, \qquad \gamma_0 = \frac1a\int_0^a G(x)\,dx ,
> $$
>
> and, term by term,
>
> $$
> \frac12\big[\bar f_o(x + ct) + \bar f_o(x - ct)\big] = \sum_{n=1}^\infty a_n\sin(\lambda_nx)\cos(\lambda_nct), \qquad
> \frac12\big[\bar G_e(x + ct) - \bar G_e(x - ct)\big] = \sum_{n=1}^\infty b_n\sin(\lambda_nx)\sin(\lambda_nct) ,
> $$
>
> so (13) is the series (9).
>
> *(Powers' Exercise 3.2.6 writes $\sum b_n\cos(n\pi x/a) = \bar G_e(x)$; the cosine coefficients of $\bar G_e$ are $-b_n$, and $\bar G_e$ has the constant term $\gamma_0$, which cancels in (13).)*
>
> *Powers: Exercise 3.2.6 · Source: 341 lectures 10.31, 11.5*

^prop-31-4

> [!proof]+ Proof
> The first expansion is the definition of $a_n$ (sine coefficients of $f$, which are the Fourier coefficients of $\bar f_o$). For $\bar G_e$, the cosine coefficients are $\gamma_n = \frac2a\int_0^aG(x)\cos(n\pi x/a)\,dx$. Integrating by parts, with $G' = g/c$,
>
> $$
> \gamma_n = \frac2a\Big[G(x)\frac{a}{n\pi}\sin\frac{n\pi x}{a}\Big]_0^a - \frac{2}{n\pi}\int_0^a\frac{g(x)}{c}\sin\frac{n\pi x}{a}\,dx = 0 - \frac{2}{n\pi c}\int_0^a g(x)\sin\frac{n\pi x}{a}\,dx = -b_n ,
> $$
>
> since $\sin(0) = \sin(n\pi) = 0$. Now use
>
> $$
> \sin(A + B) + \sin(A - B) = 2\sin A\cos B, \qquad \cos(A - B) - \cos(A + B) = 2\sin A\sin B
> $$
>
> with $A = \lambda_nx$, $B = \lambda_nct$. The first gives $\frac12 a_n[\sin\lambda_n(x + ct) + \sin\lambda_n(x - ct)] = a_n\sin(\lambda_nx)\cos(\lambda_nct)$. In $\frac12[\bar G_e(x + ct) - \bar G_e(x - ct)]$ the constant $\gamma_0$ cancels, and each term is $\frac12(-b_n)[\cos\lambda_n(x + ct) - \cos\lambda_n(x - ct)] = \frac12 b_n[\cos\lambda_n(x - ct) - \cos\lambda_n(x + ct)] = b_n\sin(\lambda_nx)\sin(\lambda_nct)$.

^pf-31-4

*Uses:* [[§30 Solution of the Vibrating String Problem#^thm-30-2|§30.2]], [[§31 d'Alembert's Solution#^thm-31-3|§31.3]], [[§7 Arbitrary Period and Half-Range Expansions#^def-7-4|Def. §7.4]]

> [!example] Example §31.1: The Midterm Problem by d'Alembert's Method
> For the problem of [[§30 Solution of the Vibrating String Problem#^ex-30-2|Example §30.2]], $u_{tt} = 4u_{xx}$ on $0 < x < \pi$ with fixed ends, $u(x, 0) = x$ and $u_t(x, 0) = \sin(2x)$: **(d)** express $\psi$ and $\phi$ in terms of the initial conditions, **(e)** expand them in Fourier series and write $u$ as d'Alembert's solution, **(f)** check that the result agrees with the series solution. (The exam names the two functions the other way round.)
>
> **(d)** Here $c = 2$, $a = \pi$, and
>
> $$
> G(x) = \frac12\int_0^x\sin(2y)\,dy = \frac14\big(1 - \cos(2x)\big), \qquad 0 < x < \pi .
> $$
>
> Then $\psi(x) = \frac12(\bar f_o(x) + \bar G_e(x) + A)$ and $\phi(x) = \frac12(\bar f_o(x) - \bar G_e(x) - A)$, where $\bar f_o$ is the odd $2\pi$-periodic extension of $f(x) = x$ (a sawtooth) and $\bar G_e$ the even $2\pi$-periodic extension of $G$. Since $\frac14(1 - \cos 2x)$ is already even and $2\pi$-periodic, $\bar G_e(x) = \frac14(1 - \cos 2x)$ for all $x$.
>
> **(e)** By [[§30 Solution of the Vibrating String Problem#^ex-30-2|Example §30.2]], $\bar f_o(x) = \sum_{n\ge1}\frac{2(-1)^{n+1}}{n}\sin(nx)$. Choose $A = -\frac14$, so that $\bar G_e(x) + A = -\frac14\cos(2x)$ (its only cosine coefficient is $-\frac14$, at $n = 2$, which is $-b_2$ as Proposition §31.4 predicts). Then
>
> $$
> \psi(x) = \sum_{n=1}^\infty\frac{(-1)^{n+1}}{n}\sin(nx) - \frac18\cos(2x), \qquad \phi(x) = \sum_{n=1}^\infty\frac{(-1)^{n+1}}{n}\sin(nx) + \frac18\cos(2x),
> $$
>
> $$
> u(x, t) = \psi(x + 2t) + \phi(x - 2t) = \sum_{n=1}^\infty\frac{(-1)^{n+1}}{n}\big[\sin n(x + 2t) + \sin n(x - 2t)\big] + \frac18\big[\cos 2(x - 2t) - \cos 2(x + 2t)\big] .
> $$
>
> **(f)** By the identities in the proof of Proposition §31.4, $\frac{(-1)^{n+1}}{n}[\sin n(x + 2t) + \sin n(x - 2t)] = \frac{2(-1)^{n+1}}{n}\sin(nx)\cos(2nt)$ and $\frac18[\cos 2(x - 2t) - \cos 2(x + 2t)] = \frac14\sin(2x)\sin(4t)$. This is the solution of [[§30 Solution of the Vibrating String Problem#^ex-30-2|Example §30.2]].
>
> The form of (e) shows what the series hides: $\bar f_o$ jumps from $\pi$ to $-\pi$ at $x = \pi$ (because $f(\pi) = \pi \ne 0$), so $u$ has a jump of size $\pi$ that enters at the end $x = \pi$ and travels along the string with speed $2$.
>
> *The key's part (e) writes $\cos(n(x \mp 2t))$ in the last term, where $\cos(2(x \mp 2t))$ is meant; part (f) uses the correct form.*
>
> *Source: 341 Midterm 2, Q1(d)–(f)*

^ex-31-1

> [!example] Example §31.2: The Struck String by d'Alembert's Method
> For the piano string of [[§30 Solution of the Vibrating String Problem#^ex-30-3|Example §30.3]] ($f \equiv 0$, $g = 2x/a$ on $(0, a/2)$ and $2 - 2x/a$ on $(a/2, a)$): **(b)** find $\psi$ and $\phi$ and the solution by computing the Fourier expansions; **(c)** check that it agrees with the series solution.
>
> **(b)** With $f \equiv 0$, $\psi = \frac12(\bar G_e + A)$ and $\phi = -\frac12(\bar G_e + A)$, so $u = \frac12[\bar G_e(x + ct) - \bar G_e(x - ct)]$. Integrating $g/c$,
>
> $$
> G(x) = \begin{cases} \dfrac{x^2}{ca}, & 0 < x < \dfrac a2, \\[2mm] \dfrac1c\Big(-\dfrac{x^2}{a} + 2x - \dfrac a2\Big), & \dfrac a2 < x < a, \end{cases}
> $$
>
> (the second piece is $\frac1c\big[\frac a4 + \int_{a/2}^x(2 - 2y/a)\,dy\big]$, and both pieces equal $a/(4c)$ at $x = a/2$). $\bar G_e$ is its even $2a$-periodic extension. Its constant term is $\gamma_0 = \frac1a\int_0^aG = \frac1{ca}\big(\frac{a^2}{24} + \frac{5a^2}{24}\big) = \frac{a}{4c}$, and by Proposition §31.4 its cosine coefficients are $\gamma_n = -b_n = -\dfrac{8a}{n^3\pi^3c}\sin\dfrac{n\pi}{2}$, from [[§30 Solution of the Vibrating String Problem#^ex-30-3|Example §30.3]]. (Directly: $\gamma_n = \frac2a\int_0^aG\cos\frac{n\pi x}{a}\,dx = -\frac{2}{n\pi c}\int_0^ag\sin\frac{n\pi x}{a}\,dx$.) Hence
>
> $$
> \bar G_e(x) = \frac{a}{4c} - \sum_{n=1}^\infty\frac{8a\sin(n\pi/2)}{n^3\pi^3c}\cos\frac{n\pi x}{a},
> \qquad
> u(x, t) = \sum_{n=1}^\infty\frac{4a\sin(n\pi/2)}{n^3\pi^3c}\Big[\cos\frac{n\pi(x - ct)}{a} - \cos\frac{n\pi(x + ct)}{a}\Big] .
> $$
>
> **(c)** Since $\frac12[\cos(A - B) - \cos(A + B)] = \sin A\sin B$, this is $\sum\frac{8a\sin(n\pi/2)}{n^3\pi^3c}\sin\frac{n\pi x}{a}\sin\frac{n\pi ct}{a}$, the series of [[§30 Solution of the Vibrating String Problem#^ex-30-3|Example §30.3]].
>
> The largest displacement is $u(a/2, a/(2c)) = \frac12[\bar G_e(a) - \bar G_e(0)] = \frac12G(a) = \frac{a}{4c}$. At $t = a/c$ the string passes through its rest position, $u(x, a/c) = \frac12[\bar G_e(x + a) - \bar G_e(x - a)] = 0$ by periodicity, and then bulges the other way. On the Practice Final the multiple-choice part asks which extensions are needed: $\bar f_o$ odd and $\bar G_e$ even, both periodic; for its data ($a = c = 2$) the key's coefficients $-\frac{8}{n^3\pi^3}\sin\frac{n\pi}{2}$ of $\bar G_e$ are the case $a = c = 2$ above.
>
> *The key's part (b) drops the factor $a$: it gives the cosine coefficients as $-\frac{8}{n^3\pi^3c}\sin\frac{n\pi}{2}$ instead of $-\frac{8a}{n^3\pi^3c}\sin\frac{n\pi}{2}$, which does not agree with its own part (a).*
>
> *Source: 341 HW 10, Problem 1(b), (c); 341 Practice Final, Q7*

^ex-31-2

![[m341-31-2.svg]]
*The struck string of Example §31.2, $u = \frac12[\bar G_e(x + ct) - \bar G_e(x - ct)]$ at $ct = 0.15a, 0.3a, 0.5a, a, 1.5a$. The string rises smoothly (no corners: the velocity, not the displacement, had the corner), reaches its largest displacement $a/(4c)$ at $ct = a/2$, is flat again at $ct = a$, and is the mirror image at $ct = 1.5a$; the period is $2a/c$.*

> [!example] Example §31.3: Piecewise Initial Data
> Solve by d'Alembert's method
>
> $$
> u_{tt} = 4u_{xx}, \quad 0 < x < 2; \qquad u(0, t) = u(2, t) = 0; \qquad u(x, 0) = f(x) = \begin{cases} x, & 0 < x < 1, \\ 0, & 1 < x < 2, \end{cases} \qquad u_t(x, 0) = g(x) = \begin{cases} -1, & 0 < x < 1, \\ 0, & 1 < x < 2 . \end{cases}
> $$
>
> **(a) $\psi$ and $\phi$.** Here $c = 2$, $a = 2$, and $G(x) = \frac12\int_0^xg$ is $-x/2$ on $(0, 1)$ and $-\frac12$ on $(1, 2)$. Then $\psi = \frac12(\bar f_o + \bar G_e + A)$ and $\phi = \frac12(\bar f_o - \bar G_e - A)$, with $\bar f_o$ the odd and $\bar G_e$ the even extension, both of period $4$.
>
> **(b) Fourier expansions.** The sine coefficients of $f$ are, integrating by parts,
>
> $$
> a_n = \frac22\int_0^1x\sin\frac{n\pi x}{2}\,dx = \Big[-\frac{2x}{n\pi}\cos\frac{n\pi x}{2}\Big]_0^1 + \frac{2}{n\pi}\int_0^1\cos\frac{n\pi x}{2}\,dx = -\frac{2}{n\pi}\cos\frac{n\pi}{2} + \frac{4}{n^2\pi^2}\sin\frac{n\pi}{2} .
> $$
>
> For $\bar G_e$: $\gamma_0 = \frac12\int_0^2G = \frac12\big(-\frac14 - \frac12\big) = -\frac38$, and
>
> $$
> \gamma_n = \int_0^1\Big(-\frac x2\Big)\cos\frac{n\pi x}{2}\,dx + \int_1^2\Big(-\frac12\Big)\cos\frac{n\pi x}{2}\,dx = \frac{2}{n^2\pi^2}\Big(1 - \cos\frac{n\pi}{2}\Big) .
> $$
>
> (Check by Proposition §31.4: $b_n = \frac{2}{2n\pi}\int_0^1(-1)\sin\frac{n\pi x}{2}\,dx = -\frac{2}{n^2\pi^2}\big(1 - \cos\frac{n\pi}{2}\big) = -\gamma_n$.) Choosing $A = \frac38$ removes the constant, and
>
> $$
> \psi(x) = \frac12\sum_{n=1}^\infty\Big[a_n\sin\frac{n\pi x}{2} + \gamma_n\cos\frac{n\pi x}{2}\Big], \qquad \phi(x) = \frac12\sum_{n=1}^\infty\Big[a_n\sin\frac{n\pi x}{2} - \gamma_n\cos\frac{n\pi x}{2}\Big],
> $$
>
> $$
> u(x, t) = \psi(x + 2t) + \phi(x - 2t) = \sum_{n=1}^\infty\Big[a_n\cos(n\pi t) - \gamma_n\sin(n\pi t)\Big]\sin\frac{n\pi x}{2} .
> $$
>
> For instance $a_1 = 4/\pi^2$, $a_2 = 1/\pi$, $\gamma_1 = 2/\pi^2$, $\gamma_2 = 1/\pi^2$, $\gamma_4 = 0$.
>
> *The key gives $\gamma_n = \frac{2}{n^2\pi^2}\big(\cos\frac{n\pi}{2} - 1\big)$, with the opposite sign; its sine coefficients agree with the above.*
>
> *Source: 341 Practice Midterm 2, Q5*

^ex-31-3
