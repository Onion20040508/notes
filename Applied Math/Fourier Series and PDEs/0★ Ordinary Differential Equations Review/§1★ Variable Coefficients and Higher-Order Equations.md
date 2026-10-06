---
type: section
subject: "[[Fourier Series and PDEs]]"
chapter: 0
section: 1
powers: "0.1"
aliases: ["Powers 0.1 (cont.)"]
tags: [fourier-series-and-pdes, math341, extension]
---
← [[§1★ Homogeneous Linear Equations]] · ↑ [[· 0★ Ordinary Differential Equations Review]] →

*Powers, Section 0.1 · MAT 341 lecture 8.27 · HW 1.*
★ *Beyond MAT 341: the course only reviewed parts of this section (lecture 8.27, HW 1 Q1); it is included in full from Powers.*

This section continues [[§1★ Homogeneous Linear Equations|§1★]] with the Cauchy–Euler equation $t^2u'' + ktu' + pu = 0$, which reappears in polar and spherical coordinates, singular points, reduction of order, and equations of order higher than two. The Cauchy–Euler equation and equations of order higher than two are not treated in [[Ordinary Differential Equations]] and are worked out here.

## The Cauchy–Euler Equation

One of the few equations with variable coefficients that can be solved in complete generality is the Cauchy–Euler equation. Its distinguishing feature is that the coefficient of the $n$th derivative is the $n$th power of $t$ times a constant. It is not treated in [[Ordinary Differential Equations]], so its solution is proved here.

> [!definition] Definition §1.5: Cauchy–Euler Equation
> The **Cauchy–Euler equation** is
>
> $$
> t^2\frac{d^2u}{dt^2} + kt\frac{du}{dt} + pu = 0 \qquad (k, p \text{ constants}) . \qquad (17)
> $$
>
> *Powers: 0.1, Equations (17)–(18)*

^def-1-5

> [!definition] Definition §1.5: Characteristic Equation of the Cauchy–Euler Equation
> The **characteristic equation** of the Cauchy–Euler equation (17) is
>
> $$
> m(m - 1) + km + p = 0 . \qquad (18)
> $$
>
> *Powers: 0.1, Equations (17)–(18)*

^def-1-new2

> [!theorem] Theorem §1.5: Solutions of the Cauchy–Euler Equation
> For $t > 0$, the general solution of (17) is determined by the roots $m_1$, $m_2$ of (18):
>
> | Roots of the characteristic equation | General solution |
> |---|---|
> | real, distinct: $m_1 \ne m_2$ | $u(t) = c_1t^{m_1} + c_2t^{m_2}$ |
> | real, double: $m_1 = m_2$ | $u(t) = c_1t^{m_1} + c_2(\ln t)t^{m_1}$ |
> | conjugate complex: $m_{1,2} = \alpha \pm i\beta$ | $u(t) = c_1t^\alpha\cos(\beta\ln t) + c_2t^\alpha\sin(\beta\ln t)$ |
>
> *Powers: 0.1, Table 2*

^thm-1-5

> [!proof]+ Proof
> **Powers' argument: $t^m$ is a solution exactly when $m$ solves (18).** Assume $u(t) = t^m$. Then $u' = mt^{m-1}$, $u'' = m(m - 1)t^{m-2}$, and substituting into (17),
>
> $$
> t^2m(m - 1)t^{m-2} + ktmt^{m-1} + pt^m = \big(m(m - 1) + km + p\big)t^m = 0 .
> $$
>
> Since $t^m \ne 0$ for $t > 0$, this holds if and only if $m$ is a root of (18). For distinct real roots this gives the two solutions $t^{m_1}$, $t^{m_2}$, with Wronskian
>
> $$
> W(t^{m_1}, t^{m_2}) = t^{m_1}\,m_2t^{m_2 - 1} - t^{m_2}\,m_1t^{m_1 - 1} = (m_2 - m_1)\,t^{m_1 + m_2 - 1} \ne 0 ,
> $$
>
> so the first row of the table follows from Theorem §1.3.
>
> **All three rows, by the substitution $x = \ln t$.** (Powers states the other two rows without argument; the substitution is his Exercise 0.1.21.) For $t > 0$ put $x = \ln t$ and $u(t) = v(x)$, that is, $v(x) = u(e^x)$. By the chain rule, with $dx/dt = 1/t$,
>
> $$
> \frac{du}{dt} = \frac1t\,v'(x), \qquad \frac{d^2u}{dt^2} = \frac{d}{dt}\Big(\frac1t\,v'(x)\Big) = -\frac{1}{t^2}\,v'(x) + \frac{1}{t^2}\,v''(x) ,
> $$
>
> so $t\,u' = v'$ and $t^2u'' = v'' - v'$. Equation (17) becomes the constant-coefficient equation
>
> $$
> v'' + (k - 1)v' + pv = 0, \qquad -\infty < x < \infty ,
> $$
>
> whose characteristic equation $m^2 + (k - 1)m + p = 0$ is exactly (18), since $m(m - 1) + km = m^2 + (k - 1)m$. Because $t \mapsto \ln t$ is a one-to-one map of $(0, \infty)$ onto $(-\infty, \infty)$, $u$ solves (17) on $t > 0$ if and only if $v$ solves this equation on the whole line. By Theorem §1.4 its general solution is
>
> $$
> v = c_1e^{m_1x} + c_2e^{m_2x}, \qquad v = c_1e^{m_1x} + c_2xe^{m_1x}, \qquad v = c_1e^{\alpha x}\cos(\beta x) + c_2e^{\alpha x}\sin(\beta x)
> $$
>
> in the three cases. Substituting back $x = \ln t$ and $e^{mx} = t^m$ gives exactly the three rows of the table.

^pf-1-5

*Uses:* [[§1★ Homogeneous Linear Equations#^thm-1-3|§1.3]], [[§1★ Homogeneous Linear Equations#^thm-1-4|§1.4]], [[§1★ Variable Coefficients and Higher-Order Equations#^def-1-5|Def. §1.5]], [[§1★ Variable Coefficients and Higher-Order Equations#^def-1-new2|Def. §1.5]]

For $t < 0$ the same formulas hold with $t$ replaced by $|t|$: the substitution $t = -s$ leaves (17) unchanged in form. In this subject the variable is a radius $r > 0$, so this never matters.

> [!example] Example §1.3: Cauchy–Euler Equations in Polar Coordinates
> Separating variables in polar coordinates ([[§39 Potential in a Disk#^thm-39-2|Theorem §39.2]], Powers 4.5) produces Cauchy–Euler equations in the radius $r$. Solve, for $r > 0$ and a constant $\lambda > 0$:
>
> **(a) $r^2u'' + ru' - \lambda^2u = 0$ (19).** Here $k = 1$, $p = -\lambda^2$, and the characteristic equation is $m(m - 1) + m - \lambda^2 = m^2 - \lambda^2 = 0$, with roots $m = \pm\lambda$. The first row of Theorem §1.5 gives
>
> $$
> u(r) = c_1r^\lambda + c_2r^{-\lambda} . \qquad (20)
> $$
>
> **(b) $r^2u'' + ru' + \lambda^2u = 0$.** Now $m^2 + \lambda^2 = 0$, $m = \pm i\lambda$ ($\alpha = 0$, $\beta = \lambda$), and the third row gives
>
> $$
> u(r) = c_1\cos(\lambda\ln r) + c_2\sin(\lambda\ln r) .
> $$
>
> **(c) $\dfrac1r\dfrac{d}{dr}\Big(r\dfrac{du}{dr}\Big) = 0$.** Multiplying out, $u'' + \frac1ru' = 0$, that is $r^2u'' + ru' = 0$: the case $\lambda = 0$ of (a). The characteristic equation $m^2 = 0$ has the double root $0$, and the second row gives
>
> $$
> u(r) = c_1 + c_2\ln r .
> $$
>
> (Directly: $ru' = c_2$, so $u' = c_2/r$.) The solutions $r^{-\lambda}$ and $\ln r$ are unbounded as $r \to 0$; in a disk they are excluded by a boundedness condition ([[§4★ Singular Boundary Value Problems#^def-4-2|Definition §4.2]]).
>
> *Powers: 0.1, Equations (19)–(20); Exercises 0.1.10 and 0.1.11*

^ex-1-3

## Singular Points

> [!definition] Definition §1.6: Singular Point
> For the general linear equation
>
> $$
> \frac{d^2u}{dt^2} + k(t)\frac{du}{dt} + p(t)u = 0 ,
> $$
>
> any point where $k(t)$ or $p(t)$ fails to be continuous is a **singular point** of the differential equation. At such a point solutions may break down in various ways.
>
> *Powers: 0.1 (text), Equation (21)*

^def-1-6

> [!definition] Definition §1.6: Regular Singular Point
> If $t_0$ is a singular point ([[§1★ Variable Coefficients and Higher-Order Equations#^def-1-6|Definition §1.6]]) of the general linear equation at which both functions
>
> $$
> (t - t_0)k(t) \qquad\text{and}\qquad (t - t_0)^2p(t) \qquad (21)
> $$
>
> have Taylor series expansions about $t_0$, then $t_0$ is a **regular singular point**.
>
> *Powers: 0.1 (text), Equation (21)*

^def-1-new3

The Cauchy–Euler equation is the model: in standard form, $u'' + \frac ktu' + \frac p{t^2}u = 0$, so $tk(t) = k$ and $t^2p(t) = p$ are constants, and $t_0 = 0$ is a regular singular point. Its solutions $t^m$, $(\ln t)t^m$ show the typical behavior near such a point, which provides a model for more general equations (Bessel's equation, [[§45★ Bessel's Equation#^def-45-1|Definition §45.1]]; Legendre's equation, [[§49★ Spherical Coordinates; Legendre Polynomials#^def-49-2|Definition §49.2]]). Singular points at the ends of an interval are the subject of [[§4★ Singular Boundary Value Problems|§4★]].

> [!remark]- Remark: Solving by a Change of Variables
> Other second-order equations may be solved by power series, by a change of variables to a kind already solved, or by sheer luck. Powers' example is the equation
>
> $$
> t^4\frac{d^2u}{dt^2} + \lambda^2u = 0 , \qquad (22)
> $$
>
> from the theory of beams, with the change of variables $t = 1/z$, $u(t) = \frac1z\,v(z)$. Since $z = 1/t$, $dz/dt = -1/t^2 = -z^2$, and by the chain rule
>
> $$
> \frac{du}{dt} = \frac{d}{dz}\Big(\frac vz\Big)\frac{dz}{dt} = -z^2\,\frac{zv' - v}{z^2} = -zv' + v, \qquad
> \frac{d^2u}{dt^2} = \frac{d}{dz}(-zv' + v)\,(-z^2) = -z^2(-zv'' - v' + v') = z^3v'' .
> $$
>
> Substituting, $\big(\frac1z\big)^4z^3v'' + \lambda^2\frac vz = 0$, that is $\frac1z(v'' + \lambda^2v) = 0$, so $v'' + \lambda^2v = 0$ and $v = c_1\cos(\lambda z) + c_2\sin(\lambda z)$. Reversing the change of variables,
>
> $$
> u(t) = t\big(c_1\cos(\lambda/t) + c_2\sin(\lambda/t)\big) . \qquad (23)
> $$

^rem-1-1

## A Second Independent Solution

It is not generally possible to solve a second-order linear homogeneous equation with variable coefficients, but a second independent solution can always be found if one solution is known.

> [!theorem] Theorem §1.6: Reduction of Order
> Suppose $u_1(t)$ is a solution of
>
> $$
> \frac{d^2u}{dt^2} + k(t)\frac{du}{dt} + p(t)u = 0 . \qquad (24)
> $$
>
> Then $u_2(t) = v(t)u_1(t)$ is a solution if and only if
>
> $$
> u_1v'' + \big(2u_1' + k(t)u_1\big)v' = 0 , \qquad (25)
> $$
>
> a first-order linear equation for $v'$. A nonconstant solution $v$ (needed for $u_2$ to be independent of $u_1$) can therefore be found, at least in terms of integrals.
>
> *Powers: 0.1 (text), Equation (25)*

^thm-1-6

*Powers substitutes $u_2 = vu_1$: $v''u_1 + 2v'u_1' + vu_1'' + k(v'u_1 + vu_1') + pvu_1 = 0$, and the coefficient $u_1'' + ku_1' + pu_1$ of $v$ is zero. Proved in ODE: [[§16 Repeated Roots; Reduction of Order#^prop-16-3|331 Prop. §16.3]].*

> [!example] Example §1.4: Reduction of Order for a Legendre Equation
> The equation
>
> $$
> (1 - t^2)u'' - 2tu' + 2u = 0, \qquad -1 < t < 1 ,
> $$
>
> has the solution $u_1(t) = t$ (check: $0 - 2t + 2t = 0$). Find a second.
>
> **Substitute** $u_2 = v\cdot t$, so $u_2' = v't + v$, $u_2'' = v''t + 2v'$:
>
> $$
> (1 - t^2)(v''t + 2v') - 2t(v't + v) + 2vt = 0 , \qquad\text{that is}\qquad (1 - t^2)tv'' + (2 - 4t^2)v' = 0 .
> $$
>
> **Solve for $v'$.** Separating, with partial fractions,
>
> $$
> \frac{v''}{v'} = \frac{4t^2 - 2}{t(1 - t^2)} = -\frac2t + \frac{1}{1 - t} - \frac{1}{1 + t} ,
> $$
>
> so $\ln v' = -2\ln t - \ln(1 - t) - \ln(1 + t)$ (on $0 < t < 1$; any constant can be dropped), and
>
> $$
> v' = \frac{1}{t^2(1 - t^2)} = \frac{1}{t^2} + \frac{1/2}{1 - t} + \frac{1/2}{1 + t}, \qquad v = -\frac1t + \frac12\ln\Big|\frac{1 + t}{1 - t}\Big| .
> $$
>
> **The second solution** is
>
> $$
> u_2(t) = t\,v(t) = -1 + \frac t2\ln\frac{1 + t}{1 - t}, \qquad -1 < t < 1 ,
> $$
>
> which is defined and solves the equation on the whole interval (direct substitution checks it). Its Wronskian with $u_1$ is $W(t, u_2) = tu_2' - u_2 = \frac{1}{1 - t^2} \ne 0$, so $u_1$, $u_2$ are independent.
>
> The equation is Legendre's equation $(1 - t^2)u'' - 2tu' + n(n + 1)u = 0$ with $n = 1$ ([[§49★ Spherical Coordinates; Legendre Polynomials#^def-49-2|Definition §49.2]] with $\mu^2 = 2$, Powers 5.9). The polynomial solution $u_1 = t$ is bounded on $[-1, 1]$, while $u_2$ is unbounded as $t \to \pm1$, the regular singular points of the equation.
>
> *Powers: 0.1, Example (reduction of order)*

^ex-1-4

## Higher-Order Equations

Linear homogeneous equations of order higher than two, especially order four, occur frequently in elasticity and fluid mechanics. They are not treated in [[Ordinary Differential Equations]] (which covered only the second-order case and first-order systems).

> [!definition] Definition §1.7: nth-Order Linear Homogeneous Equation
> A general $n$th-order homogeneous linear equation is
>
> $$
> u^{(n)} + k_1(t)u^{(n-1)} + \cdots + k_{n-1}(t)u^{(1)} + k_n(t)u = 0 , \qquad (26)
> $$
>
> with given coefficient functions $k_1(t), \ldots, k_n(t)$. With constant coefficients it reads
>
> $$
> u^{(n)} + k_1u^{(n-1)} + \cdots + k_{n-1}u^{(1)} + k_nu = 0 . \qquad (27)
> $$
>
> *Powers: 0.1, Equations (26)–(28)*

^def-1-7

> [!definition] Definition §1.7: Characteristic Equation of the nth-Order Equation
> For the constant-coefficient equation (27) of [[§1★ Variable Coefficients and Higher-Order Equations#^def-1-7|Definition §1.7]], substituting $u = e^{mt}$ and dividing by $e^{mt}$ gives its **characteristic equation**
>
> $$
> m^n + k_1m^{n-1} + \cdots + k_{n-1}m + k_n = 0 . \qquad (28)
> $$
>
> *Powers: 0.1, Equations (26)–(28)*

^def-1-new4

> [!theorem] Theorem §1.7: General Solution of the nth-Order Equation
> The Principle of Superposition holds for (26), and its general solution is a linear combination of $n$ independent solutions $u_1(t), \ldots, u_n(t)$ with arbitrary constant coefficients:
>
> $$
> u(t) = c_1u_1(t) + c_2u_2(t) + \cdots + c_nu_n(t) .
> $$
>
> *Powers: 0.1 (text)*

^thm-1-7

*Powers omits the proof. Writing $x_1 = u, x_2 = u', \ldots, x_n = u^{(n-1)}$ turns (26) into a first-order linear system ([[§27 Introduction to Systems of First-Order Linear Equations#^prop-27-1|331 Prop. §27.1]]), for which superposition and the statement are [[§30 Basic Theory of Systems of First-Order Linear Equations#^thm-30-1|331 Thm. §30.1]] and [[§30 Basic Theory of Systems of First-Order Linear Equations#^thm-30-2|331 Thm. §30.2]].*

> [!theorem] Theorem §1.8: Solutions of the Constant-Coefficient nth-Order Equation
> Each distinct root of the characteristic equation (28) contributes as many independent solutions of (27) as its multiplicity; complex roots occur in conjugate pairs (the coefficients being real) and are written with real functions:
>
> | Root | Multiplicity | Contribution |
> |---|---|---|
> | $m$ real | $1$ | $ce^{mt}$ |
> | $m$ real | $k$ | $(c_1 + c_2t + \cdots + c_kt^{k-1})e^{mt}$ |
> | $m, \bar m = \alpha \pm i\beta$ | $1$ | $\big(a\cos(\beta t) + b\sin(\beta t)\big)e^{\alpha t}$ |
> | $m, \bar m = \alpha \pm i\beta$ | $k$ | $(a_1 + a_2t + \cdots + a_kt^{k-1})\cos(\beta t)e^{\alpha t} + (b_1 + b_2t + \cdots + b_kt^{k-1})\sin(\beta t)e^{\alpha t}$ |
>
> Since the multiplicities add up to $n$, the contributions together contain $n$ terms, and their sum is the general solution of (27).
>
> *Powers: 0.1, Table 3*

^thm-1-8

*Powers omits the proof ("can be shown to be the general solution"). The case $n = 2$ is [[§16 Repeated Roots; Reduction of Order#^thm-16-2|331 Thm. §16.2]]; the remark below shows why the listed functions are solutions.*

> [!remark]- Remark: Why It Works
> Let $L[u] = u^{(n)} + k_1u^{(n-1)} + \cdots + k_nu$ and let $P(m) = m^n + k_1m^{n-1} + \cdots + k_n$ be the characteristic polynomial. Since $\frac{d^j}{dt^j}e^{mt} = m^je^{mt}$,
>
> $$
> L[e^{mt}] = P(m)\,e^{mt} \qquad\text{for every (complex) } m .
> $$
>
> Differentiate this identity $j$ times with respect to $m$. On the left, $\partial^j_m e^{mt} = t^je^{mt}$, and $\partial_m$ commutes with the $t$-derivatives in $L$ (the function $e^{mt}$ is smooth in both variables). On the right, the Leibniz product rule gives
>
> $$
> L[t^je^{mt}] = \sum_{i=0}^{j}\binom ji P^{(i)}(m)\,t^{j-i}e^{mt} .
> $$
>
> If $m$ is a root of multiplicity $k$, then $P(m) = P'(m) = \cdots = P^{(k-1)}(m) = 0$, so for $j = 0, 1, \ldots, k - 1$ every term vanishes: $e^{mt}, te^{mt}, \ldots, t^{k-1}e^{mt}$ are solutions. For a complex root, the real and imaginary parts of $t^je^{(\alpha + i\beta)t}$ are solutions because the coefficients are real ([[§30 Basic Theory of Systems of First-Order Linear Equations#^thm-30-5|331 Thm. §30.5]]). That the $n$ functions so obtained are independent is the part that needs more work.

^rem-1-2

> [!example] Example §1.5: Two Fourth-Order Equations
> **(a)** Find the general solution of $u^{(4)} + 3u^{(2)} - 4u = 0$.
>
> The characteristic equation $m^4 + 3m^2 - 4 = 0$ is a quadratic in $m^2$: $(m^2 + 4)(m^2 - 1) = 0$, so $m^2 = -4$ or $1$, and the roots are $m = \pm2i, \pm1$, all simple. By Theorem §1.8 the pair $\pm2i$ ($\alpha = 0$, $\beta = 2$) contributes $a\cos(2t) + b\sin(2t)$, and $m = 1$, $m = -1$ contribute $e^t$, $e^{-t}$:
>
> $$
> u(t) = a\cos(2t) + b\sin(2t) + c_1e^t + c_2e^{-t} .
> $$
>
> **(b)** Find the general solution of $u^{(4)} - 2u^{(2)} + u = 0$.
>
> The characteristic equation $m^4 - 2m^2 + 1 = (m^2 - 1)^2 = (m - 1)^2(m + 1)^2 = 0$ has the roots $\pm1$, each of multiplicity $2$. Each contributes a first-degree polynomial times an exponential:
>
> $$
> u(t) = (c_1 + c_2t)e^t + (c_3 + c_4t)e^{-t} .
> $$
>
> With $e^{\pm t} = \cosh t \pm \sinh t$ the terms can be regrouped into the equivalent form
>
> $$
> u(t) = (C_1 + C_2t)\cosh(t) + (C_3 + C_4t)\sinh(t) ,
> $$
>
> where $C_1 = c_1 + c_3$, $C_2 = c_2 + c_4$, $C_3 = c_1 - c_3$, $C_4 = c_2 - c_4$.
>
> *Powers: 0.1, Examples (fourth-order equations)*

^ex-1-5

> [!remark] Remark: Some Important Equations and Their Solutions
> Powers boxes the four equations that recur throughout the book:
> 1. $\dfrac{du}{dt} = ku$ ($k$ constant): $u(t) = ce^{kt}$ (Theorem §1.1).
> 2. $\dfrac{d^2u}{dt^2} + \lambda^2u = 0$: $u(t) = a\cos(\lambda t) + b\sin(\lambda t)$ (Example §1.1).
> 3. $\dfrac{d^2u}{dt^2} - \lambda^2u = 0$: $u(t) = a\cosh(\lambda t) + b\sinh(\lambda t)$, or $u(t) = c_1e^{\lambda t} + c_2e^{-\lambda t}$ (Example §1.1).
> 4. $t^2u'' + tu' - \lambda^2u = 0$: $u(t) = c_1t^\lambda + c_2t^{-\lambda}$ (Example §1.3).

^rem-1-3
