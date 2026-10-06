---
type: section
subject: "[[Fourier Series and PDEs]]"
chapter: 4
section: 47
powers: "4.4"
aliases: ["Powers 4.4"]
tags: [fourier-series-and-pdes, math341]
---
← [[§46 Further Examples for a Rectangle]] · ↑ [[· 4 The Potential Equation]] · [[§48 Potential in a Disk]] →

*Powers, Section 4.4 · MAT 341 lecture 11.21 · HW 12.*

The potential equation can be solved in unbounded regions, just like the heat equation on a semi-infinite rod ([[§32 Semi-Infinite Rod|§32]]). In place of a boundary condition at a far side, the solution is required to stay bounded far away. The model region is a slot, a half of a vertical strip. When the homogeneous conditions are on the two parallel walls, the eigenvalues are discrete and the solution is a Fourier series whose terms decay exponentially up the slot. When they are on the bottom edge together with boundedness, every positive separation constant is allowed, and the product solutions are combined by a Fourier integral instead of a series. Physically: the potential in a long channel with a charged end, or the steady temperature in a long fin.

## Potential in a Slot

The problem is

$$
\begin{aligned}
&\frac{\partial^2u}{\partial x^2} + \frac{\partial^2u}{\partial y^2} = 0, && 0 < x < a, \quad 0 < y, && (1) \\
&u(x, 0) = f(x), && 0 < x < a, && (2) \\
&u(0, y) = g_1(y), \quad u(a, y) = g_2(y), && 0 < y, && (3), (4)
\end{aligned}
$$

and, as usual, $u(x, y)$ must remain bounded as $y \to \infty$. Following [[§45 Potential in a Rectangle#^thm-45-2|Theorem §45.2]], set $u = u_1 + u_2$, where both parts are harmonic and bounded, and

$$
\begin{aligned}
&u_1(x, 0) = f(x), \quad u_1(0, y) = 0, \quad u_1(a, y) = 0; \\
&u_2(x, 0) = 0, \quad u_2(0, y) = g_1(y), \quad u_2(a, y) = g_2(y) .
\end{aligned}
$$

> [!theorem] Theorem §58.1: Slot with Data on the Bottom
> The bounded solution $u_1$ of the potential equation in the slot $0 < x < a$, $0 < y$, with $u_1(0, y) = u_1(a, y) = 0$ and $u_1(x, 0) = f(x)$, is
>
> $$
> u_1(x, y) = \sum_{n=1}^{\infty}a_n\sin\Big(\frac{n\pi x}{a}\Big)\exp\Big(-\frac{n\pi y}{a}\Big), \qquad a_n = \frac2a\int_0^a f(x)\sin\Big(\frac{n\pi x}{a}\Big)dx . \qquad (7)
> $$
>
> *Powers: 4.4, Equation (7); Exercise 4.4.1*

^thm-47-1

> [!proof]+ Proof
> **Separation.** Assume $u_1 = X(x)Y(y)$; then $X''/X = -Y''/Y = -\lambda^2$. The sign of the constant is determined by the conditions at $x = 0$ and $x = a$, which become homogeneous conditions on $X$:
>
> $$
> X(0) = 0, \qquad X(a) = 0 . \qquad (5)
> $$
>
> (One can also see it from the condition along $y = 0$, which demands functions of $x$ able to represent an arbitrary function.) Together with
>
> $$
> X'' + \lambda^2X = 0 \qquad (6)
> $$
>
> this is the eigenvalue problem of [[§25 Example꞉ Fixed End Temperatures#^thm-25-2|Theorem §25.2]], whose solution is $X_n(x) = \sin(n\pi x/a)$, $\lambda_n^2 = (n\pi/a)^2$, $n = 1, 2, 3, \ldots$
>
> **The factor $Y$.** It satisfies $Y'' - \lambda_n^2Y = 0$ for $0 < y$ and must remain bounded as $y \to \infty$. The solutions of the equation are combinations of $e^{\lambda_ny}$ and $e^{-\lambda_ny}$; the first is unbounded, so its coefficient must be $0$ and $Y_n(y) = \exp(-\lambda_ny)$. (This is why the exponential form is chosen here rather than $\cosh$ and $\sinh$, both of which are unbounded.)
>
> **Superposition.** Each $X_nY_n$ is harmonic, vanishes on the walls and is bounded, so the series (7) has the same properties when it converges (for $y \ge \delta > 0$ its terms are dominated by $|a_n|e^{-n\pi\delta/a}$). At $y = 0$ it becomes $\sum a_n\sin(n\pi x/a) = f(x)$, a Fourier sine series ([[§11 Even and Odd Functions; Half-Range Expansions#^def-11-4|Definition §11.4]]), which determines the $a_n$ as stated.

^pf-47-1

*Uses:* [[§25 Example꞉ Fixed End Temperatures#^thm-25-2|§25.2]] (the eigenvalue problem), [[§11 Even and Odd Functions; Half-Range Expansions#^def-11-4|Def. §11.4]] (sine series)

> [!remark]- Connections
> - See also: [[§27★ Harmonic Functions#^ex-27-1|342 Ex. §27.1]] (the case $a = \pi$, $f(x) = \sin x$, whose solution $e^{-y}\sin x$ is the real part of an entire function).

> [!theorem] Theorem §58.2: Slot with Data on the Walls
> Let $g_1$ and $g_2$ be sectionally smooth on $0 < y < \infty$ with $\int_0^\infty|g_i(y)|\,dy < \infty$. The bounded solution $u_2$ of the potential equation in the slot $0 < x < a$, $0 < y$, with $u_2(x, 0) = 0$, $u_2(0, y) = g_1(y)$, $u_2(a, y) = g_2(y)$, is
>
> $$
> u_2(x, y) = \int_0^\infty\left[A(\mu)\frac{\sinh(\mu x)}{\sinh(\mu a)} + B(\mu)\frac{\sinh\big(\mu(a - x)\big)}{\sinh(\mu a)}\right]\sin(\mu y)\,d\mu , \qquad (9)
> $$
>
> $$
> A(\mu) = \frac2\pi\int_0^\infty g_2(y)\sin(\mu y)\,dy, \qquad B(\mu) = \frac2\pi\int_0^\infty g_1(y)\sin(\mu y)\,dy .
> $$
>
> *Powers: 4.4, Equation (9); Exercise 4.4.3*

^thm-47-2

> [!proof]+ Proof
> **Separation.** Again $u_2 = X(x)Y(y)$, but now the homogeneous condition at $y = 0$ and the boundedness condition become conditions on $Y$:
>
> $$
> Y(0) = 0, \qquad Y(y) \ \text{bounded as } y \to \infty .
> $$
>
> The potential equation becomes
>
> $$
> \frac{X''(x)}{X(x)} + \frac{Y''(y)}{Y(y)} = 0 , \qquad (8)
> $$
>
> and both ratios must be constant.
>
> **The sign of $Y''/Y$.** (Powers says the auxiliary conditions force $Y \equiv 0$ unless $Y''/Y < 0$; here is why.) If $Y''/Y = \mu^2 > 0$, then $Y = Ae^{\mu y} + Be^{-\mu y}$, $Y(0) = A + B = 0$ gives $Y = 2A\sinh(\mu y)$, which is unbounded unless $A = 0$. If $Y''/Y = 0$, then $Y = A + By$, $Y(0) = 0$ gives $Y = By$, unbounded unless $B = 0$. So $Y''/Y = -\mu^2$, $Y'' + \mu^2Y = 0$, and the solution satisfying $Y(0) = 0$ is
>
> $$
> Y(y) = \sin(\mu y) ,
> $$
>
> which is bounded **for every** $\mu > 0$: no condition at a far end selects particular values of $\mu$.
>
> **The factor $X$.** It solves $X''/X = \mu^2$; as in [[§45 Potential in a Rectangle#^thm-45-2|Theorem §45.2]], write its general solution as
>
> $$
> X(x) = A\frac{\sinh(\mu x)}{\sinh(\mu a)} + B\frac{\sinh\big(\mu(a - x)\big)}{\sinh(\mu a)} ,
> $$
>
> a form chosen because the first term is $0$ at $x = 0$ and $1$ at $x = a$, and the second the reverse.
>
> **Superposition by an integral.** Since $\mu$ is a continuous parameter, the product solutions are combined by an integral over $\mu$ instead of a sum, with coefficients $A(\mu)$, $B(\mu)$: this is (9). At the walls,
>
> $$
> u_2(0, y) = \int_0^\infty B(\mu)\sin(\mu y)\,d\mu = g_1(y), \qquad u_2(a, y) = \int_0^\infty A(\mu)\sin(\mu y)\,d\mu = g_2(y), \qquad 0 < y .
> $$
>
> These are Fourier sine integral representations of $g_1$ and $g_2$ ([[§18 Fourier Integral#^def-18-4|Definition §18.4]]), so $B(\mu)$ and $A(\mu)$ are given by the sine-integral coefficient formula $\frac2\pi\int_0^\infty g(y)\sin(\mu y)\,dy$.

^pf-47-2

*Uses:* [[§45 Potential in a Rectangle#^thm-45-2|§45.2]] (the $\sinh$ basis), [[§18 Fourier Integral#^def-18-4|Def. §18.4]] (Fourier sine integral)

> [!remark] Remark: Method — Unbounded Regions
> 1. Impose boundedness ("$u$ remains bounded as $y \to \infty$", [[§6★ Singular Boundary Value Problems#^def-6-4|Definition §6.4]]) wherever the region is unbounded; it plays the role of a homogeneous boundary condition, because sums and integrals of bounded solutions are bounded.
> 2. Split the problem so that each part has homogeneous (or homogeneous-like) conditions on a pair of facing boundaries.
> 3. If the homogeneous pair is a pair of parallel walls a finite distance apart, the eigenvalues are discrete: use a Fourier **series**, and pick the decaying exponential $e^{-\lambda_n y}$ in the unbounded direction.
> 4. If one of the pair is "at infinity" (boundedness), every $\mu > 0$ is allowed: combine the product solutions by a Fourier **integral** and determine $A(\mu)$, $B(\mu)$ from the Fourier integral formulas.

^rem-47-1

> [!example] Example §58.1: A Slot with a Constant Bottom Value
> Solve the potential equation in the slot $0 < x < a$, $0 < y$ with $u(0, y) = u(a, y) = 0$, $u(x, 0) = 1$, $u$ bounded.
>
> **Series.** By Theorem §47.1 with $f = 1$, $a_n = \frac2a\int_0^a\sin(n\pi x/a)\,dx = \frac{2}{n\pi}\big(1 - (-1)^n\big)$, which is $\frac{4}{n\pi}$ for odd $n$ and $0$ for even $n$:
>
> $$
> u(x, y) = \frac4\pi\sum_{n \text{ odd}}\frac1n\sin\Big(\frac{n\pi x}{a}\Big)e^{-n\pi y/a} .
> $$
>
> **Closed form.** Put $\rho = e^{-\pi y/a}$ and $\theta = \pi x/a$, so the sum is the imaginary part of $\sum_{n \text{ odd}}z^n/n$ with $z = \rho e^{i\theta}$, $|z| < 1$. Subtracting the series $\ln(1 - z) = -\sum z^n/n$ from $\ln(1 + z) = \sum(-1)^{n+1}z^n/n$ gives $\sum_{n \text{ odd}}z^n/n = \frac12\ln\frac{1 + z}{1 - z}$ (the method of [[§19★ Complex Methods#^ex-19-1|Example §19.1]]). Since
>
> $$
> \frac{1 + z}{1 - z} = \frac{(1 + z)(1 - \bar z)}{|1 - z|^2} = \frac{1 - \rho^2 + 2i\rho\sin\theta}{|1 - z|^2}
> $$
>
> has positive real part, its argument is $\arctan\big(2\rho\sin\theta/(1 - \rho^2)\big)$, and the imaginary part of $\frac12\ln$ is half of it. With $2\rho/(1 - \rho^2) = 1/\sinh(\pi y/a)$,
>
> $$
> u(x, y) = \frac2\pi\arctan\left(\frac{\sin(\pi x/a)}{\sinh(\pi y/a)}\right) .
> $$
>
> **Check.** On the walls $\sin(\pi x/a) = 0$, so $u = 0$; as $y \to 0^+$ with $0 < x < a$, the argument tends to $+\infty$ and $u \to \frac2\pi\cdot\frac\pi2 = 1$; as $y \to \infty$, $u \approx \frac4\pi\sin(\pi x/a)e^{-\pi y/a} \to 0$. Far up the slot only the first term matters: the solution decays like $e^{-\pi y/a}$, at a rate set by the width of the slot. At the corners $(0, 0)$ and $(a, 0)$ the data jump from $1$ to $0$, and all level curves meet there (figure below).
>
> *Powers: Exercise 4.4.4(a)*

^ex-47-1

![[m341-38-1.svg]]
*Level curves $u = 0.1, \ldots, 0.9$ of the slot solution $u = \frac2\pi\arctan\big(\sin(\pi x/a)/\sinh(\pi y/a)\big)$ of Example §47.1. Every level curve runs from one bottom corner to the other, where the boundary value jumps from $1$ to $0$; the curves with $u \ge 0.5$ (red) hug the bottom, and the potential fades exponentially up the slot.*

> [!remark]- Connections
> - Complex-variables version: [[§120★ A Related Problem (Steady Temperatures in a Half Plane)#^ex-120-1|342 Ex. §120.1]] (the same slot, shifted to $-\pi/2 < x < \pi/2$, mapped onto a half plane by $\sin z$; it gives the same arctangent).

> [!example] Example §58.2: A Slot with Data on Both Walls
> Solve
>
> $$
> u_{xx} + u_{yy} = 0 \ \ (0 < x < a, \ y > 0); \qquad u(x, 0) = 0; \qquad u \ \text{bounded as } y \to \infty; \qquad u(0, y) = g_1(y), \ \ u(a, y) = g_2(y) .
> $$
>
> **(a) Separation.** With $u = X(x)Y(y)$, $-X''/X = Y''/Y = p$, so $X'' = -pX$, $Y'' = pY$, with $Y(0) = 0$ and $Y$ bounded as $y \to \infty$.
>
> **(b) Basic solutions.** For $p > 0$, $Y = Ae^{\sqrt p y} + Be^{-\sqrt p y}$ with $A + B = 0$ is $A(e^{\sqrt p y} - e^{-\sqrt p y})$, bounded only if $A = 0$. For $p = 0$, $Y = Ay$, bounded only if $A = 0$. For $p = -\lambda^2 < 0$, $Y = A\sin(\lambda y)$ (from $Y(0) = 0$), bounded for every $\lambda > 0$. Then $X'' = \lambda^2X$, and the basic solutions are
>
> $$
> u_\lambda(x, y) = \sin(\lambda y)\big(A(\lambda)\sinh(\lambda x) + B(\lambda)\cosh(\lambda x)\big), \qquad \lambda > 0 .
> $$
>
> **(c) The Fourier integral.** Superposing over all $\lambda > 0$,
>
> $$
> u(x, y) = \int_0^\infty\sin(\lambda y)\big(A(\lambda)\sinh(\lambda x) + B(\lambda)\cosh(\lambda x)\big)\,d\lambda .
> $$
>
> At $x = 0$: $g_1(y) = \int_0^\infty B(\lambda)\sin(\lambda y)\,d\lambda$, so $B(\lambda) = \frac2\pi\int_0^\infty g_1(y)\sin(\lambda y)\,dy$. At $x = a$: $g_2(y) = \int_0^\infty\big(A(\lambda)\sinh(\lambda a) + B(\lambda)\cosh(\lambda a)\big)\sin(\lambda y)\,d\lambda$, so
>
> $$
> A(\lambda)\sinh(\lambda a) + B(\lambda)\cosh(\lambda a) = \frac2\pi\int_0^\infty g_2(y)\sin(\lambda y)\,dy, \qquad A(\lambda) = \frac{2}{\pi\sinh(\lambda a)}\int_0^\infty g_2(y)\sin(\lambda y)\,dy - B(\lambda)\coth(\lambda a) .
> $$
>
> Rewriting $A\sinh(\lambda x) + B\cosh(\lambda x)$ with the identity of [[§45 Potential in a Rectangle#^thm-45-1|Theorem §45.1]]'s proof turns this into Powers' form (9).
>
> **(d) A concrete case.** If $g_1 = 0$ and $g_2(y) = e^{-y}$, then $B = 0$ and, since $\int_0^\infty e^{-y}\sin(\lambda y)\,dy = \lambda/(1 + \lambda^2)$ (two integrations by parts, or the Laplace transform of $\sin$),
>
> $$
> u(x, y) = \frac2\pi\int_0^\infty\frac{\lambda}{1 + \lambda^2}\,\frac{\sinh(\lambda x)}{\sinh(\lambda a)}\,\sin(\lambda y)\,d\lambda .
> $$
>
> As with most Fourier integrals ([[§18 Fourier Integral|§18]]), this one cannot be evaluated in closed form; it is the answer.
>
> *Source: 341 HW 12, Problem 3; 341 lecture 11.21; Powers: Exercise 4.4.4(b)*

^ex-47-2

> [!example] Example §58.3: A Solution the Method Cannot Find
> The function $u(x, y) = x$ is harmonic, bounded in the slot ($0 \le u \le a$), and satisfies the slot problem (1)–(4) with $f(x) = x$, $g_1(y) = 0$, $g_2(y) = a$.
>
> The method of this section splits it as $u_1 + u_2$. The part $u_1$ is fine: $a_n = \frac2a\int_0^a x\sin(n\pi x/a)\,dx = \frac{2a(-1)^{n+1}}{n\pi}$. But $u_2$ needs $A(\mu) = \frac2\pi\int_0^\infty a\sin(\mu y)\,dy$, and this integral does not converge: $g_2 = a$ is not absolutely integrable on $0 < y < \infty$, so it has no Fourier sine integral representation. The method breaks down although the solution is as simple as can be. The reason is visible in the split: $u_1 \to 0$ up the slot while $u = x$ does not, so $u_2 = x - u_1$ must tend to $x$ as $y \to \infty$; but wall data that do not die out at infinity are exactly what the Fourier integral of Theorem §47.2 cannot represent.
>
> *Powers: Exercise 4.4.19*

^ex-47-3

## Other Unbounded Regions

The potential equation can also be solved in a strip ($0 < x < a$, $-\infty < y < \infty$), a quarter-plane ($0 < x$, $0 < y$) or a half-plane ($0 < x$, $-\infty < y < \infty$). Along each boundary line a boundary condition is imposed, and the solution is required to remain bounded in remote portions of the region. In general a Fourier integral is employed, because the separation constant is a continuous parameter, as for $u_2$ above.

> [!remark] Remark: The Half-Plane and Its Poisson Formula
> For the upper half-plane $y > 0$ with $u(x, 0) = f(x)$ and $u$ bounded, the product solutions are $e^{-\lambda y}\cos(\lambda x)$ and $e^{-\lambda y}\sin(\lambda x)$, $\lambda \ge 0$, and the Fourier integral solution can be summed under the integral sign (as for the infinite rod, [[§33 Infinite Rod#^thm-33-3|Theorem §33.3]]). Powers' Exercises 4.4.15–16 lead to
>
> $$
> u(x, y) = \frac1\pi\int_{-\infty}^{\infty}f(x')\,\frac{y}{y^2 + (x - x')^2}\,dx' ,
> $$
>
> the half-plane counterpart of the Poisson integral formula for the disk, [[§49 The Poisson Integral Formula and the Mean Value Property#^thm-49-1|Theorem §49.1]]. For example, with $f = 1$ for $x > 0$ and $0$ for $x < 0$ it gives $u = \frac12 + \frac1\pi\arctan(x/y)$, the harmonic function that is constant on rays from the origin.

^rem-47-2

> [!remark]- Connections
> - Complex-variables version: [[§138★ Schwarz Integral Formula#^thm-138-2|342 Thm. §138.2]] (the half-plane formula derived from the Cauchy integral formula) and [[§139★ Dirichlet Problem for a Half Plane#^thm-139-1|342 Thm. §139.1]] (the proof that it solves the Dirichlet problem for bounded data with jumps); a worked case is [[§119★ Steady Temperatures in a Half Plane#^ex-119-1|342 Ex. §119.1]].
