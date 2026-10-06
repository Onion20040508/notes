---
type: section
subject: "[[Fourier Series and PDEs]]"
chapter: 3
section: "42★"
powers: "3.6"
aliases: ["Powers 3.6"]
tags: [fourier-series-and-pdes, math341, extension]
---
← [[§41★ Estimation of Eigenvalues]] · ↑ [[· 3 The Wave Equation]] · [[§43 Plucked, Struck, Midterm, Hanging and Nonuniform Strings]] →

*Powers, Section 3.6 · MAT 341 Practice Midterm 2.*
★ *Beyond MAT 341: the course did not cover this section; it is included from Powers.*

On a semi-infinite string $0 < x < \infty$ the wave equation can be solved as the heat equation was on the semi-infinite rod ([[§32 Semi-Infinite Rod#^thm-32-2|Theorem §32.2]]): separate variables and combine the product solutions in a Fourier integral instead of a series. The integral, however, gives no idea of what $u$ looks like, and d'Alembert's method again does better: the fixed end acts as a mirror, and a pulse travelling toward it comes back inverted. The same method solves the string driven by a moving end, where the disturbance travels into the string with speed $c$, and the infinite string, where it gives d'Alembert's formula $u = \frac12[f(x + ct) + f(x - ct)] + \frac{1}{2c}\int_{x-ct}^{x+ct}g$. In contrast with the heat equation, a disturbance needs time $|x - x_0|/c$ to reach the point $x$.

## The Semi-Infinite String

> [!definition] Definition §42.1: The Semi-Infinite String Problem
> The problem for a string occupying $0 < x < \infty$ with its end at $x = 0$ fixed is
>
> $$
> \begin{aligned}
> &\frac{\partial^2 u}{\partial x^2} = \frac{1}{c^2}\frac{\partial^2 u}{\partial t^2}, && 0 < t, \quad 0 < x, && (1) \\
> &u(x, 0) = f(x), && 0 < x, && (2) \\
> &\frac{\partial u}{\partial t}(x, 0) = g(x), && 0 < x, && (3) \\
> &u(0, t) = 0, && 0 < t, && (4)
> \end{aligned}
> $$
>
> together with the requirement that $u(x, t)$ be bounded as $x \to \infty$.
>
> *Powers: 3.6, Equations (1)–(4)*

^def-42-1

> [!theorem] Theorem §42.1: Fourier Integral Solution of the Semi-Infinite String
> If $\int_0^\infty|f(x)|\,dx$ and $\int_0^\infty|g(x)|\,dx$ are finite, the solution of (1)–(4) is
>
> $$
> u(x, t) = \int_0^\infty\big(A(\lambda)\cos(\lambda ct) + B(\lambda)\sin(\lambda ct)\big)\sin(\lambda x)\,d\lambda , \qquad (5)
> $$
>
> with
>
> $$
> A(\lambda) = \frac2\pi\int_0^\infty f(x)\sin(\lambda x)\,dx, \qquad B(\lambda) = \frac{2}{\pi\lambda c}\int_0^\infty g(x)\sin(\lambda x)\,dx .
> $$
>
> *Powers: 3.6, Equation (5) and text*

^thm-42-1

> [!proof]+ Proof
> *Powers gives this as a formal derivation, as for the semi-infinite rod.* Separating variables, $u(x, t) = \phi(x)T(t)$, the factors satisfy
>
> $$
> T'' + \lambda^2c^2T = 0, \quad 0 < t, \qquad \phi'' + \lambda^2\phi = 0, \quad 0 < x, \qquad \phi(0) = 0, \quad |\phi(x)| \text{ bounded} .
> $$
>
> (A positive separation constant gives $\phi = Be^{\mu x} + Ce^{-\mu x}$, and $\phi(0) = 0$ with boundedness force $\phi \equiv 0$; so does the constant $0$.) The solutions are
>
> $$
> \phi(x; \lambda) = \sin(\lambda x), \qquad T(t; \lambda) = A\cos(\lambda ct) + B\sin(\lambda ct),
> $$
>
> for every $\lambda > 0$: there is no condition at a second end to make $\lambda$ discrete. Combine the products $\phi(x; \lambda)T(t; \lambda)$ in a Fourier integral over $\lambda$, which is (5). The initial conditions become
>
> $$
> u(x, 0) = f(x) = \int_0^\infty A(\lambda)\sin(\lambda x)\,d\lambda, \qquad \frac{\partial u}{\partial t}(x, 0) = g(x) = \int_0^\infty\lambda cB(\lambda)\sin(\lambda x)\,d\lambda, \qquad 0 < x
> $$
>
> (differentiating under the integral sign). Both are Fourier sine integrals ([[§18 Fourier Integral#^def-18-4|Definition §18.4]]), so $A(\lambda)$ and $\lambda cB(\lambda)$ are the Fourier sine integral coefficients of $f$ and $g$, which gives the formulas. It is sufficient that $\int_0^\infty|f|$ and $\int_0^\infty|g|$ be finite to guarantee that $A$ and $B$ exist.

^pf-42-1

*Uses:* [[§18 Fourier Integral#^def-18-4|Def. §18.4]] (Fourier sine integral), [[§32 Semi-Infinite Rod#^thm-32-2|§32.2]] (the same method for heat)

The deficiency of the Fourier integral form (5) is that it gives no idea of what $u(x, t)$ looks like. The d'Alembert solution comes to the aid again.

> [!theorem] Theorem §42.2: d'Alembert's Solution of the Semi-Infinite String
> The solution of (1)–(4) is
>
> $$
> u(x, t) = \frac12\big[f_o(x + ct) + G_e(x + ct)\big] + \frac12\big[f_o(x - ct) - G_e(x - ct)\big] , \qquad (6)
> $$
>
> where $f_o$ is the odd extension of $f$ and $G_e$ the even extension of $G(x) = \frac1c\int_0^xg(y)\,dy$ to the whole line (no periodicity).
>
> *Powers: 3.6, Equation (6)*

^thm-42-2

> [!proof]+ Proof
> By [[§39 d'Alembert's Solution#^thm-39-2|Theorem §39.2]] the solution has the form $u(x, t) = \psi(x + ct) + \phi(x - ct)$. As in the finite case ([[§39 d'Alembert's Solution#^thm-39-3|Theorem §39.3]]), the initial conditions boil down to
>
> $$
> \psi(x) + \phi(x) = f(x), \qquad \psi(x) - \phi(x) = G(x) + A, \qquad 0 < x ,
> $$
>
> with $A$ any constant, so that
>
> $$
> \psi(x) = \frac12\big(f(x) + G(x) + A\big), \qquad \phi(x) = \frac12\big(f(x) - G(x) - A\big), \qquad x > 0 .
> $$
>
> Both $f$ and $G$ are known for $x > 0$. Thus $\psi(x + ct)$ is defined for all $x > 0$ and $t \ge 0$; but $\phi(x - ct)$ is not yet defined for $x - ct < 0$. So $f$ and $G$ must be extended to negative arguments, as $\tilde f$ and $\tilde G$, in such a way that the sole boundary condition (4) holds:
>
> $$
> u(0, t) = 0 = \psi(ct) + \phi(-ct) = \frac12\big[f(ct) + G(ct) + A + \tilde f(-ct) - \tilde G(-ct) - A\big] .
> $$
>
> Powers takes the two parts to vanish individually, $f(ct) + \tilde f(-ct) = 0$ and $G(ct) - \tilde G(-ct) = 0$ for $t > 0$: that is, $\tilde f = f_o$ is the odd extension of $f$ and $\tilde G = G_e$ is the even extension of $G$. With this choice the boundary condition holds for every $t$, and substituting into $u = \psi(x + ct) + \phi(x - ct)$ (the constant $A$ cancels) gives (6). The initial conditions hold as in the proof of [[§39 d'Alembert's Solution#^thm-39-3|Theorem §39.3]]: $u(x, 0) = f_o(x) = f(x)$ and $u_t(x, 0) = cG_e'(x) = g(x)$ for $x > 0$.

^pf-42-2

*Uses:* [[§39 d'Alembert's Solution#^thm-39-2|§39.2]], [[§39 d'Alembert's Solution#^thm-39-3|§39.3]], [[§39 d'Alembert's Solution#^def-39-2|Def. §39.2]]

Given $f$ and $g$, it is now a simple matter to construct $f_o$ and $G_e$, and so to graph $u(x, t)$ as a function of either variable or to evaluate it at given $x$ and $t$. For $x > ct$ the end has no influence yet, and $u = \frac12[f(x + ct) + f(x - ct)] + \frac12[G(x + ct) - G(x - ct)]$ involves only the given data.

> [!example] Example §42.1: Reflection of a Pulse at the Fixed End
> Take $c = 1$, $g \equiv 0$, and an initial triangular pulse $f(x) = 1 - |x - 3|$ for $2 < x < 4$, $f(x) = 0$ elsewhere on $x > 0$. Then $G \equiv 0$ and, by (6),
>
> $$
> u(x, t) = \frac12\big[f_o(x + t) + f_o(x - t)\big], \qquad f_o(y) = \begin{cases} f(y), & y > 0, \\ -f(-y), & y < 0 . \end{cases}
> $$
>
> - **$t = 1$.** $u = \frac12f(x + 1) + \frac12f(x - 1)$: the pulse has split into two pulses of half the height, centred at $x = 2$ (moving left) and $x = 4$ (moving right).
> - **$t = 2.5$.** The left pulse, $\frac12f(x + 2.5)$, is centred at $x = 0.5$ and overlaps the reflected wave $\frac12f_o(x - 2.5) = -\frac12f(2.5 - x)$, which is nonzero for $0 < x < 0.5$. There
>
> $$
> u = \frac12\big[(1 - |x - 0.5|) - (1 - |x + 0.5|)\big] = \frac12\big[(x + 0.5) - (0.5 - x)\big] = x ,
> $$
>
> and for $0.5 < x < 1.5$, $u = \frac12(1.5 - x)$. Near the end the string is a small triangle that vanishes at $x = 0$, as it must.
> - **$t = 3$.** For $0 < x < 1$ the incident wave $\frac12(1 - x)$ and the reflected wave $-\frac12(1 - x)$ cancel exactly: the string near the end is momentarily straight (but moving).
> - **$t = 5$.** $u = -\frac12f(5 - x) + \frac12f(x - 5)$: an inverted half pulse centred at $x = 2$ moving right, following the upright one centred at $x = 8$.
>
> The fixed end reflects the pulse upside down; the odd extension is precisely the "image" pulse, travelling toward the end from the other side, that makes $u(0, t) = 0$.
>
> *Powers: 3.6, Figure 5 (the construction); the pulse is chosen here*

^ex-42-1

![[m341-34-1.svg]]
*The pulse of Example §42.1 on the semi-infinite string ($c = 1$) at $t = 0, 1, 2.5, 3, 5$. It splits into two half pulses; the left one meets the fixed end at $t = 2$, is folded back ($t = 2.5$), cancels momentarily ($t = 3$), and returns inverted, following the right one at the same speed.*

## A Moving End

Another problem that can be treated by d'Alembert's method has a boundary condition that is a function of time. For simplicity take zero initial conditions:

$$
\begin{aligned}
&\frac{\partial^2 u}{\partial x^2} = \frac{1}{c^2}\frac{\partial^2 u}{\partial t^2}, \quad 0 < t, \quad 0 < x, && (7) \\
&u(x, 0) = 0, \quad \frac{\partial u}{\partial t}(x, 0) = 0, \quad 0 < x, && (8), (9) \\
&u(0, t) = h(t), \quad 0 < t . && (10)
\end{aligned}
$$

> [!theorem] Theorem §42.3: The String Driven at Its End
> The solution of (7)–(10) is $u(x, t) = \phi(x - ct)$ (12), where
>
> $$
> \phi(q) = \begin{cases} 0, & q > 0, \\ h\Big(-\dfrac qc\Big), & q < 0 ; \end{cases} \qquad (14)
> $$
>
> that is,
>
> $$
> u(x, t) = \begin{cases} h\Big(t - \dfrac xc\Big), & x < ct, \\ 0, & x > ct . \end{cases}
> $$
>
> *Powers: 3.6, Equations (11)–(14)*

^thm-42-3

> [!proof]+ Proof
> As a solution of the wave equation, $u(x, t) = \psi(x + ct) + \phi(x - ct)$ (11). The two initial conditions (8), (9) are treated exactly as in the first problem: $G \equiv 0$, and the arbitrary constant $A$ may be taken as $0$, so
>
> $$
> \psi(x) = 0, \qquad \phi(x) = 0, \qquad 0 < x .
> $$
>
> Since both $x$ and $t$ are positive, $x + ct > 0$ and $\psi(x + ct) = 0$ always; so (11) simplifies to $u(x, t) = \phi(x - ct)$ (12). The boundary condition (10) tells how to evaluate $\phi$ for negative arguments:
>
> $$
> u(0, t) = \phi(-ct) = h(t), \qquad 0 < t . \qquad (13)
> $$
>
> With $q = -ct < 0$, $t = -q/c$, this is $\phi(q) = h(-q/c)$. Together with $\phi(q) = 0$ for $q > 0$ this is (14). (The argument $q$ is a dummy, used to avoid association with either $x$ or $t$.) For $x < ct$, $\phi(x - ct) = h\big(-(x - ct)/c\big) = h(t - x/c)$.

^pf-42-3

*Uses:* [[§39 d'Alembert's Solution#^thm-39-2|§39.2]]

The graph of $\phi$ for negative arguments is that of $h$, reflected and rescaled: graph the even extension of $h$, replace its right half by $0$, and adjust the scale so that $q = -c$ where $t = 1$, and so on. A wave equation with nonzero initial conditions **and** a time-varying boundary condition is solved by breaking it into two problems, one like (1)–(4) with zero boundary condition and one like (7)–(10) with zero initial conditions, and adding the solutions.

> [!example] Example §42.2: A Pulse Sent in from the End
> Let the end be moved by $h(t) = \frac H2t$ for $0 < t < 2$, $h(t) = H(3 - t)$ for $2 < t < 3$, and $h(t) = 0$ for $t > 3$ (up slowly, down quickly, then held). By Theorem §42.3, $u(x, t) = h(t - x/c)$ for $x < ct$ and $0$ beyond.
>
> - $t = 1$: $u = \frac H2\big(1 - \frac xc\big)$ for $0 < x < c$, a ramp from $\frac H2$ down to $0$.
> - $t = 2$: $u = \frac H2\big(2 - \frac xc\big)$ for $0 < x < 2c$, from $H$ down to $0$.
> - $t = 3$: $u = H\frac xc$ for $0 < x < c$ and $\frac H2\big(3 - \frac xc\big)$ for $c < x < 3c$: the end is back at $0$, and the whole shape of $h$, reversed, is on the string.
> - $t = 4$: $u = 0$ for $x < c$, $H\big(\frac xc - 1\big)$ for $c < x < 2c$, $\frac H2\big(4 - \frac xc\big)$ for $2c < x < 4c$.
>
> The disturbance caused by the moving end arrives at a fixed point $x$ at time $x/c$, so it travels with the velocity $c$, the wave speed, and the shape seen at $t = 4$ continues to travel to the right unchanged.
>
> *Powers: 3.6, Example*

^ex-42-2

![[m341-34-2.svg]]
*The string of Example §42.2 at $t = 1, 2, 3, 4$. Points farther from the end start moving later: $u(x, t) = h(t - x/c)$ is the history of the end, delayed by the travel time $x/c$. The front, where $u$ first becomes nonzero, is at $x = ct$.*

## The Infinite String

> [!theorem] Theorem §42.4: d'Alembert's Formula for the Infinite String
> Let $f$ have two continuous derivatives and $g$ one, on $-\infty < x < \infty$. The solution of
>
> $$
> \frac{\partial^2 u}{\partial x^2} = \frac{1}{c^2}\frac{\partial^2 u}{\partial t^2}, \quad -\infty < x < \infty, \quad 0 < t; \qquad u(x, 0) = f(x), \quad \frac{\partial u}{\partial t}(x, 0) = g(x), \quad -\infty < x < \infty,
> $$
>
> is
>
> $$
> u(x, t) = \frac12\big(f(x + ct) + f(x - ct)\big) + \frac{1}{2c}\int_{x-ct}^{x+ct}g(z)\,dz .
> $$
>
> *Powers: Exercises 3.6.7 and 3.6.8*

^thm-42-4

> [!proof]+ Proof
> **Derivation** (Exercise 7). By [[§39 d'Alembert's Solution#^thm-39-2|Theorem §39.2]], $u = \psi(x + ct) + \phi(x - ct)$. The initial conditions give, now for all real $x$, $\psi + \phi = f$ and $c\psi' - c\phi' = g$; integrating the second, $\psi - \phi = G + A$ with $G(x) = \frac1c\int_0^xg(z)\,dz$. Hence $\psi = \frac12(f + G + A)$ and $\phi = \frac12(f - G - A)$ on the whole line, and no extension is needed:
>
> $$
> u(x, t) = \frac12\big[f(x + ct) + f(x - ct)\big] + \frac12\big[G(x + ct) - G(x - ct)\big] ,
> $$
>
> and $\frac12[G(x + ct) - G(x - ct)] = \frac{1}{2c}\int_{x-ct}^{x+ct}g(z)\,dz$.
>
> **Verification** (Exercise 8). By the fundamental theorem of calculus and the chain rule (Leibniz's rule for an integral with variable limits), $\frac{\partial}{\partial t}\int_{x-ct}^{x+ct}g = cg(x + ct) + cg(x - ct)$ and $\frac{\partial}{\partial x}\int_{x-ct}^{x+ct}g = g(x + ct) - g(x - ct)$. So
>
> $$
> u_t = \frac c2\big[f'(x + ct) - f'(x - ct)\big] + \frac12\big[g(x + ct) + g(x - ct)\big], \qquad
> u_{tt} = \frac{c^2}{2}\big[f''(x + ct) + f''(x - ct)\big] + \frac c2\big[g'(x + ct) - g'(x - ct)\big],
> $$
>
> $$
> u_{xx} = \frac12\big[f''(x + ct) + f''(x - ct)\big] + \frac{1}{2c}\big[g'(x + ct) - g'(x - ct)\big] ,
> $$
>
> and $u_{tt} = c^2u_{xx}$. At $t = 0$: $u(x, 0) = f(x) + \frac{1}{2c}\int_x^xg = f(x)$ and $u_t(x, 0) = 0 + \frac12[g(x) + g(x)] = g(x)$.

^pf-42-4

*Uses:* [[§39 d'Alembert's Solution#^thm-39-2|§39.2]], [[§34 Fundamental Theorem of Calculus#^thm-34-4|451 Thm. §34.4]] (FTC), [[§110 The Chain Rule#^thm-110-2|Calc Thm. §110.2]]

> [!remark] Remark: Finite Speed of Propagation
> By Theorem §42.4, $u(x, t)$ depends only on the initial data on the interval $[x - ct, x + ct]$: a disturbance at $x_0$ cannot be felt at $x$ before the time $|x - x_0|/c$. This is the opposite of the heat equation on the infinite rod ([[§33 Infinite Rod#^rem-33-1|§33]]), where an initial temperature concentrated near one point makes the temperature positive everywhere at every $t > 0$. The semi-infinite string of Theorem §42.2 is the infinite string with odd data: if $f$ and $g$ are extended as odd functions, $G$ is even, and d'Alembert's formula gives $u(0, t) = 0$ automatically.

^rem-42-1

> [!example] Example §42.3: A Gaussian Pulse with a Push
> Let $f_1(x) = \frac{1}{\sqrt{2\pi}}e^{-x^2/2}$ (the Gaussian distribution with $\sigma = 1$) and $-1 < \alpha < 1$. Solve
>
> $$
> w_{tt} = w_{xx}, \quad -\infty < x < \infty, \quad t > 0; \qquad w(x, 0) = f_1(x), \qquad w_t(x, 0) = \alpha f_1'(x) .
> $$
>
> By Theorem §42.4 with $c = 1$,
>
> $$
> w(x, t) = \frac12\big[f_1(x + t) + f_1(x - t)\big] + \frac12\int_{x-t}^{x+t}\alpha f_1'(z)\,dz = \frac12\big[f_1(x + t) + f_1(x - t)\big] + \frac\alpha2\big[f_1(x + t) - f_1(x - t)\big],
> $$
>
> that is,
>
> $$
> w(x, t) = \frac{1 + \alpha}{2}f_1(x + t) + \frac{1 - \alpha}{2}f_1(x - t) .
> $$
>
> The initial velocity decides how the bump divides: a fraction $\frac{1 + \alpha}{2}$ travels left and $\frac{1 - \alpha}{2}$ travels right; with $\alpha = 0$ (released from rest) it splits evenly, and in the limits $\alpha \to \pm1$ it travels entirely one way. The total $E(t) = \int_{-\infty}^\infty w\,dx = \frac{1 + \alpha}{2} + \frac{1 - \alpha}{2} = 1$ is conserved, while the shape does not spread, unlike the heat equation's solution $f_{\sqrt{2t + 1}}$ from the same initial data.
>
> *Source: 341 Practice Midterm 2, Q10(c)*

^ex-42-3

*Chain: the Gaussian earlier in [[§19★ Complex Methods#^ex-19-3|Chapter 1]] (its Fourier transform) · [[§36 Heated Section, Half Sine Wave, One-Sided Exponential and Gaussian#The Gaussian|Chapter 2]] (a heat solution).*

> [!example] Example §42.4: The Fourier Integral and d'Alembert's Form Agree
> Solve the semi-infinite string problem (1)–(4) with $f(x) = xe^{-x}$, $g(x) \equiv 0$, in both forms.
>
> **Fourier integral.** $B(\lambda) = 0$, and, since $\int_0^\infty xe^{-x}\sin(\lambda x)\,dx$ is the imaginary part of $\int_0^\infty xe^{-(1 - i\lambda)x}\,dx = \frac{1}{(1 - i\lambda)^2} = \frac{(1 + i\lambda)^2}{(1 + \lambda^2)^2}$,
>
> $$
> A(\lambda) = \frac2\pi\cdot\frac{2\lambda}{(1 + \lambda^2)^2}, \qquad u(x, t) = \frac4\pi\int_0^\infty\frac{\lambda}{(1 + \lambda^2)^2}\cos(\lambda ct)\sin(\lambda x)\,d\lambda .
> $$
>
> **d'Alembert.** $G \equiv 0$, and the odd extension of $f$ is $f_o(y) = ye^{-|y|}$. By (6),
>
> $$
> u(x, t) = \frac12\big[(x + ct)e^{-(x + ct)} + (x - ct)e^{-|x - ct|}\big] .
> $$
>
> For $x > ct$ both terms are the travelling halves of the initial bump; for $x < ct$ the second term $(x - ct)e^{x - ct}$ is negative, the reflection coming back from the end. The two forms agree (numerically, for instance, both give $u = 0.28493$ at $x = 0.5$, $ct = 0.2$ and $u = -0.10926$ at $x = 1$, $ct = 2$), as they must: by the product formula $\cos(\lambda ct)\sin(\lambda x) = \frac12[\sin\lambda(x + ct) + \sin\lambda(x - ct)]$, the integral is $\frac12$ times the sum of the Fourier sine integrals of $f$ evaluated at $x + ct$ and $x - ct$, and the sine integral represents the odd extension $f_o$ ([[§18 Fourier Integral#^cor-18-2|Corollary §18.2]]). This is Powers' Exercise 3.6.2 in a concrete case.
>
> *Powers: 3.6, Equations (5) and (6); Exercise 3.6.2*

^ex-42-4
