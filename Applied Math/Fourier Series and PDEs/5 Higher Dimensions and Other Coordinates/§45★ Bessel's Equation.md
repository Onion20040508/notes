---
type: section
subject: "[[Fourier Series and PDEs]]"
chapter: 5
section: 45
powers: "5.5"
aliases: ["Powers 5.5"]
tags: [fourier-series-and-pdes, math341, extension]
---
← [[§44★ Problems in Polar Coordinates]] · ↑ [[· 5 Higher Dimensions and Other Coordinates]] · [[§46★ Temperature in a Cylinder]] →

*Powers, Section 5.5.*
★ *Beyond MAT 341: the course did not cover this section; it is included from Powers.*

Separating variables in polar coordinates left the radial equation $(rR')' - \mu^2R/r + \lambda^2rR = 0$ ([[§44★ Problems in Polar Coordinates#^thm-44-2|Theorem §44.2]]). It has a singular point at $r = 0$, so it cannot be solved by a power series alone; the method of Frobenius, a power series times $r^\alpha$, produces the Bessel function of the first kind $J_\mu(\lambda r)$, bounded at the origin. A second solution, from reduction of order, is the Bessel function of the second kind $Y_\mu(\lambda r)$, unbounded at the origin, so in a disk only $J_\mu$ survives. Both oscillate like damped cosines with infinitely many zeros, and the zeros of $J_\mu$ play the role that the multiples of $\pi$ play for $\sin x$: they give the eigenvalues, hence the cooling rates of a cylinder and the frequencies of a drum. The section also collects the derivative and integral formulas used in the next sections and introduces the modified Bessel functions, which arise when the sign of $\lambda^2$ is reversed.

## Bessel's Equation and the Method of Frobenius

> [!definition] Definition §45.1: Bessel's Equation
> **Bessel's equation** of order $\mu \ge 0$, with parameter $\lambda > 0$, is
>
> $$
> \frac{d}{dr}\Big(r\frac{dR}{dr}\Big) - \frac{\mu^2}{r}R + \lambda^2rR = 0, \qquad 0 < r , \qquad (1)
> $$
>
> or, multiplied by $r$, $r^2R'' + rR' + (\lambda^2r^2 - \mu^2)R = 0$. In the variable $x = \lambda r$ it becomes $x^2y'' + xy' + (x^2 - \mu^2)y = 0$ for $y(x) = R(x/\lambda)$, so $\lambda$ only rescales $r$.
>
> *Powers: 5.5, Equation (1); 5.4, Equation (12)*

^def-45-1

> [!remark]- Connections
> - In standard form, $R'' + \frac{1}{r}R' + \big(\lambda^2 - \frac{\mu^2}{r^2}\big)R = 0$, a second-order linear equation whose coefficients are continuous on $0 < r < \infty$ but not at $r = 0$. The existence and uniqueness theorem [[§14 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-14-1|331 Thm. §14.1]] applies on $(0, \infty)$, and the solution space there is two-dimensional; at $r = 0$, a [[§1★ Homogeneous Linear Equations#^def-1-6|regular singular point]], solutions may blow up.
> - The radial part of the two-dimensional Helmholtz equation $\nabla^2\phi + \lambda^2\phi = 0$ in polar coordinates ([[§35 Potential Equation#^thm-35-3|Theorem §35.3]]), which is how it arose in [[§44★ Problems in Polar Coordinates#^thm-44-2|Theorem §44.2]].

> [!remark] Remark: Method — The Method of Frobenius
> To solve an equation like (1) near the singular point $r = 0$:
> 1. Assume that $R$ is a power series multiplied by an unknown power of $r$:
>
>    $$
>    R(r) = r^\alpha\big(c_0 + c_1r + \cdots + c_kr^k + \cdots\big), \qquad c_0 \ne 0 . \qquad (2)
>    $$
>
> 2. Substitute into the equation (here multiplied by $r$), and line up like powers of $r$.
> 3. Set the coefficient of each power equal to zero. The lowest power gives the **indicial equation** for $\alpha$; the others give a recursion for the $c_k$.
> 4. For each admissible root $\alpha$, solve the recursion and check that the series converges.

^rem-45-1

> [!theorem] Theorem §45.1: The Frobenius Coefficients for Bessel's Equation
> A series (2) satisfies Bessel's equation (1) if and only if
>
> $$
> c_0(\alpha^2 - \mu^2) = 0, \qquad c_1\big((\alpha + 1)^2 - \mu^2\big) = 0, \qquad c_k\big((\alpha + k)^2 - \mu^2\big) + \lambda^2c_{k-2} = 0, \quad k \ge 2 .
> $$
>
> With $c_0 \ne 0$ this forces $\alpha = \pm\mu$. For $\alpha = \mu \ge 0$: $c_1 = 0$, all coefficients with odd index are zero,
>
> $$
> c_k = -\frac{\lambda^2c_{k-2}}{(\mu + k)^2 - \mu^2} = -\lambda^2\frac{c_{k-2}}{k(2\mu + k)}, \qquad k \ge 2 , \qquad (3)
> $$
>
> and for even index $k = 2m$
>
> $$
> c_{2m} = \frac{(-1)^m}{m!\,(\mu + 1)(\mu + 2)\cdots(\mu + m)}\Big(\frac{\lambda}{2}\Big)^{2m}c_0 . \qquad (4)
> $$
>
> *Powers: 5.5, Equations (2)–(4)*

^thm-45-1

> [!proof]+ Proof
> **The tableau.** Carrying out the differentiations in (1) and multiplying by $r$ gives $r^2R'' + rR' - \mu^2R + \lambda^2r^2R = 0$. For $R = \sum_{k \ge 0} c_kr^{\alpha + k}$,
>
> $$
> \begin{aligned}
> r^2R'' &= \textstyle\sum_{k \ge 0} (\alpha + k)(\alpha + k - 1)c_kr^{\alpha + k}, \\
> rR' &= \textstyle\sum_{k \ge 0} (\alpha + k)c_kr^{\alpha + k}, \\
> -\mu^2R &= \textstyle\sum_{k \ge 0} -\mu^2c_kr^{\alpha + k}, \\
> \lambda^2r^2R &= \textstyle\sum_{k \ge 2} \lambda^2c_{k-2}r^{\alpha + k} .
> \end{aligned}
> $$
>
> The expression for $\lambda^2r^2R$ is shifted so that like powers of $r$ line up; its lowest power is $r^{\alpha + 2}$. Since $(\alpha + k)(\alpha + k - 1) + (\alpha + k) = (\alpha + k)^2$, adding the four lines gives
>
> $$
> 0 = c_0(\alpha^2 - \mu^2)r^\alpha + c_1\big((\alpha + 1)^2 - \mu^2\big)r^{\alpha + 1} + \sum_{k \ge 2}\Big[c_k\big((\alpha + k)^2 - \mu^2\big) + \lambda^2c_{k-2}\Big]r^{\alpha + k} .
> $$
>
> After division by $r^\alpha$ this is a power series that vanishes for all small $r > 0$, so each coefficient must be zero, which gives the three conditions.
>
> **The case $\alpha = \mu \ge 0$.** As a bookkeeping agreement $c_0 \ne 0$, so $\alpha^2 = \mu^2$. With $\alpha = \mu$, $(\mu + k)^2 - \mu^2 = k(2\mu + k) > 0$ for every $k \ge 1$. The second condition becomes $c_1(2\mu + 1) = 0$, so $c_1 = 0$, and the third becomes (3), which finds $c_k$ from $c_{k-2}$. All $c$'s with odd index are multiples of $c_1$, hence zero. For even index, (3) with $k = 2m$ reads
>
> $$
> c_{2m} = -\frac{\lambda^2}{2m(2\mu + 2m)}c_{2m-2} = -\Big(\frac{\lambda}{2}\Big)^2\frac{1}{m(\mu + m)}c_{2m-2} ;
> $$
>
> for example $c_2 = -\frac{\lambda^2}{2(2\mu + 2)}c_0$ and $c_4 = -\frac{\lambda^2}{4(2\mu + 4)}c_2 = \frac{\lambda^4}{2\cdot4\cdot(2\mu + 2)(2\mu + 4)}c_0$. Applying this $m$ times collects the factor $(-1)^m(\lambda/2)^{2m}$ and the denominator $m!\,(\mu + 1)(\mu + 2)\cdots(\mu + m)$, which is (4).

^pf-45-1

*Uses:* [[§45★ Bessel's Equation#^def-45-1|Def. §45.1]]

> [!remark]- Remark: The Other Root α = −μ
> For $\alpha = -\mu$ the coefficient of $c_k$ is $(k - \mu)^2 - \mu^2 = k(k - 2\mu)$, which vanishes at $k = 2\mu$. When $2\mu$ is not an integer the recursion goes through and gives a second solution, $J_{-\mu}$. When $\mu$ is an integer, the case met in the disk problems, the recursion breaks down at $k = 2\mu$ (for $\mu = 0$ the two roots coincide), and the second solution is not of the form (2). That is why Powers finds it by a different method, Theorem §45.3.

^rem-45-2

> [!definition] Definition §45.2: Bessel Function of the First Kind
> For integer $\mu \ge 0$, choose by convention $c_0 = \Big(\dfrac{\lambda}{2}\Big)^\mu\cdot\dfrac{1}{\mu!}$ in (4). The solution of (1) so obtained is the **Bessel function of the first kind of order $\mu$**:
>
> $$
> J_\mu(\lambda r) = \Big(\frac{\lambda r}{2}\Big)^\mu\sum_{m=0}^{\infty} \frac{(-1)^m}{m!\,(\mu + m)!}\Big(\frac{\lambda r}{2}\Big)^{2m} . \qquad (5)
> $$
>
> As a function of one variable, $J_\mu(x) = \sum_{m \ge 0} \dfrac{(-1)^m}{m!\,(m + \mu)!}\Big(\dfrac{x}{2}\Big)^{2m + \mu}$, and (5) is $J_\mu$ evaluated at $x = \lambda r$.
>
> *Powers: 5.5, Equation (5)*

^def-45-2

The series serves for evaluating $J_\mu$ and for obtaining its properties. From now on, Powers says, *consider the Bessel functions of the first kind to be as well known as sines and cosines*, although less familiar.

> [!remark]- Connections
> - Stewart defines $J_0$ by the same series and finds its domain by the ratio test and its derivative term by term: [[§77 Representations of Functions as Power Series#^ex-77-5|Calc Ex. §77.5]].
> - The rigorous facts behind Theorem §45.2: radius of convergence, [[§23 Power Series#^thm-23-2|451 Thm. §23.2]]; a power series may be differentiated term by term inside its interval of convergence, [[§26 Differentiation and Integration of Power Series#^thm-26-4|451 Thm. §26.4]].
> - See also: [[§66 Laurent Series#^ex-66-2|342 Ex. §66.2]] (the $J_n$ as Laurent coefficients of $\exp\big[\frac z2\big(w - \frac1w\big)\big]$, with the integral formula $J_n(z) = \frac1\pi\int_0^\pi\cos(n\phi - z\sin\phi)\,d\phi$).
> - Used in Electromagnetism: the four kinds of Bessel function in cylindrical boundary-value problems — [[§C6.3 Separation in Cylindrical and Polar Coordinates#^def-c6-3-1|EM Def. §C6.3.1]], [[§C6.3 Separation in Cylindrical and Polar Coordinates#^thm-c6-3-1|EM Theorem §C6.3.1]].

> [!theorem] Theorem §45.2: J_μ Solves Bessel's Equation
> For integer $\mu \ge 0$ the series (5) converges for every $r$, and $R = J_\mu(\lambda r)$ is a solution of Bessel's equation (1) on $0 < r < \infty$. It is bounded near $r = 0$, with $J_0(0) = 1$ and $J_\mu(0) = 0$ for $\mu \ge 1$.
>
> *Powers: 5.5 (text)*

^thm-45-2

> [!proof]+ Proof
> (Powers asserts this; here is why.) Write $s = \lambda r/2$. The ratio of consecutive terms of the series in (5) is
>
> $$
> \left|\frac{(-1)^{m+1}s^{2m+2}}{(m+1)!\,(\mu + m + 1)!}\cdot\frac{m!\,(\mu + m)!}{(-1)^ms^{2m}}\right| = \frac{s^2}{(m + 1)(\mu + m + 1)} \to 0
> $$
>
> as $m \to \infty$, for every $s$. By the ratio test the series converges for all $r$: it is a power series with infinite radius of convergence. Such a series may be differentiated term by term any number of times, so the computation in the proof of Theorem §45.1 is legitimate for $R = J_\mu(\lambda r) = \sum c_kr^{\mu + k}$, and since its coefficients satisfy (3) and (4), all coefficients of $r^2R'' + rR' + (\lambda^2r^2 - \mu^2)R$ vanish: $R$ solves (1). Being a convergent power series times $r^\mu$, $J_\mu(\lambda r)$ is continuous, hence bounded near $0$; at $r = 0$ every term with a positive power of $r$ vanishes, so $J_\mu(0)$ is the $m = 0$ term $(\lambda r/2)^{\mu}/\mu!$ at $r = 0$, which is $1$ for $\mu = 0$ and $0$ for $\mu \ge 1$.

^pf-45-2

*Uses:* [[§45★ Bessel's Equation#^thm-45-1|§45.1]], [[§45★ Bessel's Equation#^def-45-2|Def. §45.2]], [[§14 Series#^thm-14-9|451 Thm. §14.9]] (ratio test), [[§26 Differentiation and Integration of Power Series#^thm-26-4|451 Thm. §26.4]] (term-by-term differentiation)

> [!example] Example §45.1: The Series for J₀ and J₁
> Write out the first terms of $J_0(x)$ and $J_1(x)$, evaluate $J_0(1)$, and use the series to check the first zero $2.405$ of $J_0$.
>
> **The series.** With $\mu = 0$ the denominators in (5) are $(m!)^2 2^{2m} = 1, 4, 64, 2304, 147456$; with $\mu = 1$ they are $m!\,(m + 1)!\,2^{2m+1} = 2, 16, 384, 18432$:
>
> $$
> J_0(x) = 1 - \frac{x^2}{4} + \frac{x^4}{64} - \frac{x^6}{2304} + \frac{x^8}{147456} - \cdots, \qquad J_1(x) = \frac{x}{2} - \frac{x^3}{16} + \frac{x^5}{384} - \frac{x^7}{18432} + \cdots .
> $$
>
> Differentiating the first series term by term gives $-\frac{x}{2} + \frac{x^3}{16} - \frac{x^5}{384} + \cdots = -J_1(x)$, a first instance of Theorem §45.7.
>
> **$J_0(1)$.** $1 - 0.25 + 0.015625 - 0.000434 + 0.000007 = 0.765198$; the terms alternate and decrease, so the error is less than the next term, about $10^{-7}$ (the true value is $0.7651977$).
>
> **The first zero.** At $x = 2.405$, $(x/2)^2 = 1.44601$, and the partial sums are
>
> $$
> 1, \quad -0.44601, \quad 0.07673, \quad -0.00726, \quad 0.00033, \quad -0.00011, \quad -0.0000900, \quad -0.0000906, \quad \ldots
> $$
>
> converging to $J_0(2.405) \approx -0.00009$. So $J_0$ changes sign just below $2.405$ (the zero is $2.40483$). For larger $x$ more terms are needed before the terms start to decrease, which is why tables, or the asymptotic form of [[§45★ Bessel's Equation#^rem-45-4|Remark: Why J₀ Oscillates]], are used there.
>
> *Powers: 5.5, Equation (5); Table 1*

^ex-45-1

## The Second Solution

There must be a second, independent solution of Bessel's equation.

> [!theorem] Theorem §45.3: A Second Solution by Reduction of Order
> On any interval of $r > 0$ on which $J_\mu(\lambda r) \ne 0$, the function
>
> $$
> J_\mu(\lambda r)\cdot\int \frac{dr}{r\,J_\mu^2(\lambda r)} \qquad (6)
> $$
>
> is a solution of Bessel's equation (1), independent of $J_\mu(\lambda r)$.
>
> *Powers: 5.5, Equation (6)*

^thm-45-3

> [!proof]+ Proof
> Powers says that this follows by variation of parameters; the method is reduction of order. In standard form (1) is $R'' + p(r)R' + q(r)R = 0$ with $p(r) = 1/r$. Let $y_1(r) = J_\mu(\lambda r)$, a solution by Theorem §45.2. By reduction of order, $R = v(r)y_1(r)$ is a solution if and only if
>
> $$
> y_1v'' + \Big(2y_1' + \frac{1}{r}y_1\Big)v' = 0 , \qquad\text{that is,}\qquad \frac{(v')'}{v'} = -\frac{2y_1'}{y_1} - \frac{1}{r}
> $$
>
> where $y_1 \ne 0$ and $v' \ne 0$. Integrating, $\ln|v'| = -2\ln|y_1| - \ln r + \text{const}$, so $v' = C/(r\,y_1^2)$ and $v = C\int dr/(r\,y_1^2)$; with $C = 1$ this is (6). It is independent of $y_1$ because $v$ is not constant ($v' \ne 0$). Equivalently, the Wronskian of $y_1$ and $vy_1$ is $y_1(vy_1)' - y_1'vy_1 = y_1^2v' = 1/r \ne 0$, in agreement with Abel's formula $W = C\exp(-\int dr/r) = C/r$.

^pf-45-3

*Uses:* [[§45★ Bessel's Equation#^thm-45-2|§45.2]], [[§16 Repeated Roots; Reduction of Order#^prop-16-3|331 Prop. §16.3]] (reduction of order), [[§14 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-14-8|331 Thm. §14.8]] (Abel's theorem)

> [!definition] Definition §45.3: Bessel Function of the Second Kind
> In its standard form, normalized by convention, the second solution of Bessel's equation is called the **Bessel function of the second kind of order $\mu$** and is denoted $Y_\mu(\lambda r)$. It is a solution on all of $0 < r < \infty$, independent of $J_\mu(\lambda r)$.
>
> *Powers: 5.5 (text)*

^def-45-3

> [!remark]- Remark: The Series for Y₀
> Powers does not give the standard normalization. For $\mu = 0$ it is
>
> $$
> Y_0(x) = \frac{2}{\pi}\Big(\ln\frac{x}{2} + \gamma\Big)J_0(x) + \frac{2}{\pi}\sum_{m=1}^{\infty} \frac{(-1)^{m+1}H_m}{(m!)^2}\Big(\frac{x}{2}\Big)^{2m}, \qquad H_m = 1 + \frac12 + \cdots + \frac1m ,
> $$
>
> where $\gamma = 0.5772\ldots$ is Euler's constant. The logarithm is the behavior predicted by Theorem §45.4: $Y_0(x) \approx \frac{2}{\pi}\ln x$ as $x \to 0^+$. (Numerically $Y_0(1) = 0.0883$, and the first zero of $Y_0$ is at $0.894$.)
>
> *Source: the standard normalization (DLMF §10.8); not in Powers.*

^rem-45-3

> [!theorem] Theorem §45.4: The Second Solution Is Unbounded at the Origin
> $|Y_\mu(\lambda r)| \to \infty$ as $r \to 0^+$. More precisely, the solution (6) behaves like a constant times $\ln r$ if $\mu = 0$ and like a constant times $r^{-\mu}$ if $\mu > 0$.
>
> *Powers: 5.5 (text)*

^thm-45-4

> [!proof]+ Proof
> *Powers gives this as a sketch:* when $r$ is very small, $J_\mu(\lambda r) \cong (\lambda/2)^\mu r^\mu/\mu!$, the first term of its series, and then (6) is approximately
>
> $$
> \text{constant}\times r^\mu\int \frac{dr}{r^{1+2\mu}} = \text{constant}\times\begin{cases} \ln r, & \mu = 0, \\ r^{-\mu}, & \mu > 0 . \end{cases}
> $$
>
> Here are the details. By (5), $J_\mu(\lambda r) = \frac{(\lambda r/2)^\mu}{\mu!}\big(1 + E(r)\big)$, where $E(r)$ is a power series in $r^2$ with $E(0) = 0$, so $|E(r)| \le Cr^2$ for small $r$. Choose $r_0 > 0$ with $|E| \le \frac12$ on $(0, r_0]$; then $J_\mu(\lambda r) \ne 0$ there, and
>
> $$
> \frac{1}{r\,J_\mu^2(\lambda r)} = K\,r^{-1-2\mu}\big(1 + F(r)\big), \qquad K = (\mu!)^2\Big(\frac{2}{\lambda}\Big)^{2\mu}, \qquad |F(r)| \le C'r^2 .
> $$
>
> Take the antiderivative in (6) as $\int_r^{r_0}$ (another choice adds a multiple of $J_\mu$, which is bounded). If $\mu = 0$, $\int_r^{r_0} Ks^{-1}(1 + F)\,ds = K\ln(r_0/r) + O(1)$, and since $J_0(\lambda r) \to 1$, the solution (6) is $K\ln(1/r) + O(1) \to \infty$. If $\mu \ge 1$ (an integer, as in Definition §45.2; for non-integer $\mu > 0$ the same computation works with $\Gamma(\mu + 1)$ in place of $\mu!$), $\int_r^{r_0} Ks^{-1-2\mu}(1 + F)\,ds = \frac{K}{2\mu}r^{-2\mu} + O(r^{2-2\mu}) + O(\ln(1/r)) + O(1)$, whose leading term is $\frac{K}{2\mu}r^{-2\mu}$; multiplied by $J_\mu(\lambda r) \sim (\lambda r/2)^\mu/\mu!$ it gives (6) $\sim \frac{(\mu - 1)!}{2}\big(\frac{2}{\lambda}\big)^\mu r^{-\mu} \to \infty$.
>
> Finally $Y_\mu = AJ_\mu + B\cdot(6)$ for some constants with $B \ne 0$, since $Y_\mu$ is independent of $J_\mu$; as $J_\mu$ is bounded near $0$, $|Y_\mu(\lambda r)| \to \infty$.

^pf-45-4

*Uses:* [[§45★ Bessel's Equation#^def-45-2|Def. §45.2]], [[§45★ Bessel's Equation#^thm-45-3|§45.3]], [[§45★ Bessel's Equation#^def-45-3|Def. §45.3]]

> [!theorem] Theorem §45.5: General Solution of Bessel's Equation
> The differential equation
>
> $$
> \frac{d}{dr}\Big(r\frac{dR}{dr}\Big) - \frac{\mu^2}{r}R + \lambda^2rR = 0
> $$
>
> is called Bessel's equation. Its general solution is
>
> $$
> R(r) = AJ_\mu(\lambda r) + BY_\mu(\lambda r)
> $$
>
> ($A$ and $B$ arbitrary constants). The functions $J_\mu$ and $Y_\mu$ are called Bessel functions of order $\mu$ of the first and second kinds, respectively. The Bessel function of the second kind is unbounded at the origin; hence the solutions bounded as $r \to 0$ are exactly the multiples $AJ_\mu(\lambda r)$.
>
> *Powers: 5.5, Summary*

^thm-45-5

> [!proof]+ Proof
> On $0 < r < \infty$ the equation in standard form has continuous coefficients. $J_\mu(\lambda r)$ and $Y_\mu(\lambda r)$ are solutions there, and they are linearly independent: $J_\mu(\lambda r)$ stays bounded as $r \to 0$ and $Y_\mu(\lambda r)$ does not (Theorem §45.4), so neither is a constant multiple of the other. For two solutions of a second-order linear equation, independence means that their Wronskian is not zero, so they form a fundamental set and $AJ_\mu + BY_\mu$ contains every solution. If $B \ne 0$, then $|AJ_\mu(\lambda r) + BY_\mu(\lambda r)| \ge |B|\,|Y_\mu(\lambda r)| - |A|\,|J_\mu(\lambda r)| \to \infty$ as $r \to 0$; so a bounded solution has $B = 0$.

^pf-45-5

*Uses:* [[§45★ Bessel's Equation#^thm-45-2|§45.2]], [[§45★ Bessel's Equation#^thm-45-4|§45.4]], [[§14 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-14-4|331 Thm. §14.4]] (general solution from a fundamental set)

> [!remark]- Connections
> - The general solution of a second-order linear equation from two independent solutions, and independence as a nonzero Wronskian: [[§14 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-14-4|331 Thm. §14.4]], with Abel's theorem [[§14 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-14-8|331 Thm. §14.8]] giving $W[J_\mu, Y_\mu] = C/r$ without computing either function.
> - The same pattern in the potential problem of [[§39 Potential in a Disk#^thm-39-2|Theorem §39.2]]: the radial equation $r^2R'' + rR' - m^2R = 0$ (Bessel's equation with $\lambda = 0$) has solutions $r^m$ and $r^{-m}$ (or $1$ and $\ln r$), and boundedness at the center discards the second, just as it discards $Y_\mu$ here.
> - Used in Electromagnetism: separated solutions of Laplace's equation in cylindrical coordinates, and the zeros, asymptotics and orthogonality boundary-value problems need — [[§C6.3 Separation in Cylindrical and Polar Coordinates#^thm-c6-3-1|EM Theorem §C6.3.1]], [[§C6.3 Separation in Cylindrical and Polar Coordinates#^thm-c6-3-2|EM Theorem §C6.3.2]].

![[m341-45-2.svg]]
*The Bessel functions of the second kind $Y_0$ (blue) and $Y_1$ (red), computed with SciPy. Both tend to $-\infty$ at the origin, $Y_0$ like $\frac{2}{\pi}\ln x$ and $Y_1$ like $-\frac{2}{\pi x}$, which is why they are excluded from problems in a full disk. For large $x$ they oscillate within the envelope $\pm\sqrt{2/(\pi x)}$ (dashed), like $J_0$ and $J_1$ shifted by a quarter period.*

## Zeros and Behavior at Infinity

> [!theorem] Theorem §45.6: Zeros of the Bessel Functions
> Both kinds of Bessel functions have an infinite number of zeros: there are infinitely many values of $\alpha$ (and $\beta$) for which
>
> $$
> J_\mu(\alpha) = 0, \qquad Y_\mu(\beta) = 0 .
> $$
>
> Also, as $r \to \infty$, both $J_\mu(\lambda r)$ and $Y_\mu(\lambda r)$ tend to zero. The first zeros $\alpha_{mn}$ of $J_m$, $J_m(\alpha_{mn}) = 0$, are
>
> | $m$ | $n = 1$ | $n = 2$ | $n = 3$ | $n = 4$ |
> |---|---|---|---|---|
> | $0$ | $2.405$ | $5.520$ | $8.654$ | $11.792$ |
> | $1$ | $3.832$ | $7.016$ | $10.173$ | $13.324$ |
> | $2$ | $5.136$ | $8.417$ | $11.620$ | $14.796$ |
> | $3$ | $6.380$ | $9.761$ | $13.015$ | $16.223$ |
>
> *Powers: 5.5 (text); Table 1*

^thm-45-6

*Powers omits the proof. (The table agrees with values recomputed with SciPy to all digits shown.)*

![[m341-45-1.svg]]
*$J_0$ (blue) and $J_1$ (red), computed with SciPy. $J_0(0) = 1$ and $J_1(0) = 0$; both oscillate with slowly decreasing amplitude, like damped cosines. The dots mark the zeros of $J_0$ (2.405, 5.520, 8.654, 11.792) and the circles those of $J_1$ (3.832, 7.016, 10.173, 13.324): they alternate (Corollary §45.9 puts a zero of $J_1$ between consecutive zeros of $J_0$; Rolle's theorem applied to $xJ_1(x)$, whose derivative is $xJ_0(x)$ by Theorem §45.7(d), puts a zero of $J_0$ between consecutive zeros of $J_1$), and consecutive zeros are about $\pi$ apart. $J_1$ has its maximum $0.582$ at $x = 1.841$, and $J_0$ its minimum $-0.403$ at the first zero of $J_1$, since $J_0' = -J_1$.*

> [!remark] Remark: Why J₀ Oscillates
> The substitution $y = \sqrt{x}\,J_0(x)$ turns Bessel's equation $x^2J_0'' + xJ_0' + x^2J_0 = 0$ into
>
> $$
> y'' + \Big(1 + \frac{1}{4x^2}\Big)y = 0 .
> $$
>
> For large $x$ this is nearly $y'' + y = 0$, so $y \approx A\cos(x - \delta)$, and $J_0(x) \approx A\cos(x - \delta)/\sqrt{x}$: an oscillation with infinitely many zeros, spaced by nearly $\pi$, and amplitude decaying like $1/\sqrt{x}$. The precise statement is $J_0(x) \approx \sqrt{2/(\pi x)}\cos(x - \pi/4)$ and $Y_0(x) \approx \sqrt{2/(\pi x)}\sin(x - \pi/4)$; for $J_\mu$ the phase is $x - \mu\pi/2 - \pi/4$. Already at $x = 10$ the approximation gives $J_0(10) \approx -0.2468$ against the true $-0.2459$. The spacings of the zeros in the table, $3.115$, $3.134$, $3.138$, approach $\pi = 3.1416$.
>
> *Source: Liouville's normal form and the standard asymptotic formulas (DLMF §10.7); not in Powers.*

^rem-45-4

## Derivative and Integral Formulas

The next formulas, Powers' Exercises 5.5.3–5.5.7, are used in [[§46★ Temperature in a Cylinder|§46]] and after to compute coefficients of Bessel series.

> [!theorem] Theorem §45.7: Derivatives of Bessel Functions
> With the prime denoting differentiation with respect to the argument:
> - (a) $\dfrac{d}{dr}J_\mu(\lambda r) = \lambda J_\mu'(\lambda r)$;
> - (b) $J_0'(x) = -J_1(x)$, so $\dfrac{d}{dr}J_0(\lambda r) = -\lambda J_1(\lambda r)$;
> - (c) $\dfrac{d}{dx}\big(x^{-\mu}J_\mu(x)\big) = -x^{-\mu}J_{\mu+1}(x)$;
> - (d) $\dfrac{d}{dx}\big(x^\mu J_\mu(x)\big) = x^\mu J_{\mu-1}(x)$, for $\mu \ge 1$.
>
> *Powers: Exercises 5.5.3, 5.5.4 and 5.5.6*

^thm-45-7

> [!proof]+ Proof
> (a) is the chain rule. For (c) and (d), differentiate the series of Definition §45.2 term by term (Theorem §45.2).
>
> **(c)** $x^{-\mu}J_\mu(x) = \sum_{m \ge 0} \dfrac{(-1)^mx^{2m}}{2^{2m+\mu}\,m!\,(m + \mu)!}$. The term $m = 0$ is constant; for $m \ge 1$, $\frac{d}{dx}x^{2m} = 2mx^{2m-1}$ and $2m/m! = 2/(m - 1)!$, so
>
> $$
> \frac{d}{dx}\big(x^{-\mu}J_\mu(x)\big) = \sum_{m \ge 1} \frac{(-1)^mx^{2m-1}}{2^{2m+\mu-1}(m - 1)!\,(m + \mu)!} = \sum_{j \ge 0} \frac{(-1)^{j+1}x^{2j+1}}{2^{2j+\mu+1}\,j!\,(j + \mu + 1)!} = -x^{-\mu}\sum_{j \ge 0} \frac{(-1)^j}{j!\,(j + \mu + 1)!}\Big(\frac{x}{2}\Big)^{2j+\mu+1} ,
> $$
>
> with $m = j + 1$; the last sum is $J_{\mu+1}(x)$.
>
> **(b)** is (c) with $\mu = 0$, combined with (a).
>
> **(d)** $x^\mu J_\mu(x) = \sum_{m \ge 0} \dfrac{(-1)^mx^{2m+2\mu}}{2^{2m+\mu}\,m!\,(m + \mu)!}$, and $\frac{d}{dx}x^{2m+2\mu} = 2(m + \mu)x^{2m+2\mu-1}$ with $(m + \mu)/(m + \mu)! = 1/(m + \mu - 1)!$ (here $\mu \ge 1$ is used), so
>
> $$
> \frac{d}{dx}\big(x^\mu J_\mu(x)\big) = \sum_{m \ge 0} \frac{(-1)^mx^{2m+2\mu-1}}{2^{2m+\mu-1}\,m!\,(m + \mu - 1)!} = x^\mu\sum_{m \ge 0} \frac{(-1)^m}{m!\,(m + \mu - 1)!}\Big(\frac{x}{2}\Big)^{2m+\mu-1} = x^\mu J_{\mu-1}(x) .
> $$

^pf-45-7

*Uses:* [[§45★ Bessel's Equation#^def-45-2|Def. §45.2]], [[§45★ Bessel's Equation#^thm-45-2|§45.2]], [[§26 Differentiation and Integration of Power Series#^thm-26-4|451 Thm. §26.4]]

> [!theorem] Corollary §45.8: An Integral Formula
> For integer $\mu \ge 0$,
>
> $$
> \int x^{\mu+1}J_\mu(x)\,dx = x^{\mu+1}J_{\mu+1}(x) + C ;
> $$
>
> in particular $\displaystyle\int xJ_0(x)\,dx = xJ_1(x) + C$.
>
> *Powers: Exercise 5.5.7*

^cor-45-8

> [!proof]+ Proof
> Theorem §45.7(d) with $\mu + 1$ in place of $\mu$ reads $\frac{d}{dx}\big(x^{\mu+1}J_{\mu+1}(x)\big) = x^{\mu+1}J_\mu(x)$, so $x^{\mu+1}J_{\mu+1}$ is an antiderivative of $x^{\mu+1}J_\mu$. (Powers writes the integrand as $x^\mu J_\mu(x)\,x$.)

^pf-45-8

*Uses:* [[§45★ Bessel's Equation#^thm-45-7|§45.7]]

> [!theorem] Corollary §45.9: J₁ Has Infinitely Many Zeros
> Between any two consecutive positive zeros of $J_0$ there is a zero of $J_1$. In particular $J_1(x) = 0$ has an infinite number of solutions.
>
> *Powers: Exercise 5.5.5*

^cor-45-9

> [!proof]+ Proof
> Let $\alpha < \alpha'$ be consecutive positive zeros of $J_0$. $J_0$ is differentiable, and $J_0(\alpha) = J_0(\alpha') = 0$, so by Rolle's theorem $J_0'(\xi) = 0$ for some $\xi$ in $(\alpha, \alpha')$. By Theorem §45.7(b), $J_1(\xi) = -J_0'(\xi) = 0$. Since $J_0$ has infinitely many zeros (Theorem §45.6), this gives infinitely many zeros of $J_1$, one in each gap. (In the table: $2.405 < 3.832 < 5.520 < 7.016 < 8.654 < \cdots$.)

^pf-45-9

*Uses:* [[§45★ Bessel's Equation#^thm-45-6|§45.6]], [[§45★ Bessel's Equation#^thm-45-7|§45.7]], [[§29 The Mean Value Theorem#^thm-29-2|451 Thm. §29.2]] (Rolle's theorem)

## Radial Eigenvalue Problems

> [!example] Example §45.2: The Radial Eigenvalue Problem with a Fixed Edge
> Find the values of $\lambda$ for which
>
> $$
> \frac{1}{r}\frac{d}{dr}\Big(r\frac{d\phi}{dr}\Big) + \lambda^2\phi = 0, \quad 0 < r < a, \qquad \phi(a) = 0, \quad \phi(0) \text{ bounded}
> $$
>
> has a nonzero solution, and describe the eigenfunctions.
>
> **Bessel's equation of order 0.** Multiplying by $r$ gives $(r\phi')' + \lambda^2r\phi = 0$, which is (1) with $\mu = 0$. By Theorem §45.5 its bounded solutions are $\phi = AJ_0(\lambda r)$.
>
> **The boundary condition.** $\phi(a) = AJ_0(\lambda a) = 0$ with $A \ne 0$ requires $\lambda a$ to be a zero of $J_0$: $\lambda a = \alpha_{0n}$, so
>
> $$
> \lambda_n = \frac{\alpha_{0n}}{a} = \frac{2.405}{a},\ \frac{5.520}{a},\ \frac{8.654}{a},\ \ldots, \qquad \phi_n(r) = J_0\Big(\frac{\alpha_{0n}r}{a}\Big) .
> $$
>
> **No other cases.** For $\lambda = 0$, $(r\phi')' = 0$ gives $\phi = A + B\ln r$; boundedness forces $B = 0$ and $\phi(a) = 0$ then forces $A = 0$. A negative $\lambda^2 = -\gamma^2$ gives the modified Bessel equation, whose bounded solutions $AI_0(\gamma r)$ never vanish for $r > 0$ ([[§45★ Bessel's Equation#^thm-45-10|Theorem §45.10]]), so $\phi(a) = 0$ forces $A = 0$. (Every other solution is unbounded: since $I_0 > 0$ on $(0, \infty)$, reduction of order as in [[§45★ Bessel's Equation#^thm-45-3|Theorem §45.3]] gives the second solution $I_0(\gamma r)\int dr/(r\,I_0^2(\gamma r))$, and the proof of [[§45★ Bessel's Equation#^thm-45-4|Theorem §45.4]] for $\mu = 0$ applies word for word, because $I_0(\gamma r) = 1 + O(r^2)$ just as $J_0(\lambda r)$ is: it behaves like $\ln(1/r)$.)
>
> **The eigenfunctions.** $\phi_n$ starts at $\phi_n(0) = 1$ and vanishes at $r = a$; inside, it vanishes where $\alpha_{0n}r/a$ is an earlier zero of $J_0$, so it has $n - 1$ zeros in $0 < r < a$ (the nodal circles of a drum). $\phi_1$ decreases from $1$ to $0$ without changing sign; $\phi_2$ changes sign at $r = (2.405/5.520)a = 0.436a$; $\phi_3$ at $r = 0.278a$ and $0.638a$. Their graphs are the piece of the blue curve in the figure above from $0$ to the $n$th zero, compressed to the interval $[0, a]$. This is the eigenvalue problem of the cylinder, [[§46★ Temperature in a Cylinder#^prop-46-1|Proposition §46.1]].
>
> *Powers: Exercises 5.5.1 and 5.5.2*

^ex-45-2

> [!example] Example §45.3: The Radial Eigenvalue Problem with an Insulated Edge
> Solve the eigenvalue problem
>
> $$
> \frac{1}{r}\frac{d}{dr}\Big(r\frac{d\phi}{dr}\Big) + \lambda^2\phi = 0, \quad 0 < r < a, \qquad \frac{d\phi}{dr}(a) = 0, \quad \phi(0) \text{ bounded} .
> $$
>
> As in Example §45.2, for $\lambda > 0$ the bounded solutions are $\phi = AJ_0(\lambda r)$. By Theorem §45.7(b), $\phi'(r) = -\lambda AJ_1(\lambda r)$, so the boundary condition is $\lambda AJ_1(\lambda a) = 0$: $\lambda a$ must be a positive zero of $J_1$. This time $\lambda = 0$ also works: $\phi = A + B\ln r$ is bounded only for $B = 0$, and the constant $\phi = 1$ satisfies $\phi'(a) = 0$. The eigenvalues and eigenfunctions are
>
> $$
> \lambda_0 = 0, \quad \phi_0 = 1; \qquad \lambda_n = \frac{\alpha_{1n}}{a} = \frac{3.832}{a},\ \frac{7.016}{a},\ \frac{10.173}{a},\ \ldots, \quad \phi_n(r) = J_0\Big(\frac{\alpha_{1n}r}{a}\Big) .
> $$
>
> The eigenfunctions are pieces of $J_0$ ending at its turning points rather than at its zeros: $\phi_1 = J_0(3.832r/a)$ ends at the minimum of $J_0$, with zero slope. This is the radial problem for the insulated plate of [[§44★ Problems in Polar Coordinates#^ex-44-3|Example §44.3]], and the constant eigenfunction is the mean temperature that the plate keeps forever.
>
> *Powers: Exercise 5.5.10*

^ex-45-3

## Modified Bessel Functions

> [!definition] Definition §45.4: Modified Bessel Equation and Function
> The **modified Bessel equation** differs from Bessel's equation only in the sign of one term:
>
> $$
> \frac{d}{dr}\Big(r\frac{dR}{dr}\Big) - \frac{\mu^2}{r}R - \lambda^2rR = 0 . \qquad (7)
> $$
>
> Its solution that is bounded at $r = 0$, in standard form, is the **modified Bessel function of the first kind of order $\mu$**,
>
> $$
> I_\mu(\lambda r) = \Big(\frac{\lambda r}{2}\Big)^\mu\sum_{m=0}^{\infty} \frac{1}{m!\,(\mu + m)!}\Big(\frac{\lambda r}{2}\Big)^{2m} .
> $$
>
> *Powers: 5.5, Equation (7) and text*

^def-45-4

> [!theorem] Theorem §45.10: I_μ Solves the Modified Bessel Equation
> For integer $\mu \ge 0$, $I_\mu(\lambda r)$ is a solution of (7), bounded at $r = 0$; its power-series coefficients are those of $J_\mu(\lambda r)$ except for signs. Every term of its series is positive, so $I_\mu(x) > 0$ for $x > 0$, and $I_0$ is increasing with $I_0(0) = 1$; in particular $I_\mu$ has no positive zeros.
>
> *Powers: Exercise 5.5.8*

^thm-45-10

> [!proof]+ Proof
> Apply the method of Frobenius exactly as in Theorem §45.1, with $-\lambda^2$ in place of $\lambda^2$. The conditions become $c_0(\alpha^2 - \mu^2) = 0$, $c_1((\alpha + 1)^2 - \mu^2) = 0$ and $c_k((\alpha + k)^2 - \mu^2) - \lambda^2c_{k-2} = 0$. With $\alpha = \mu$: $c_1 = 0$, odd coefficients vanish, and
>
> $$
> c_k = +\lambda^2\frac{c_{k-2}}{k(2\mu + k)}, \qquad c_{2m} = \frac{1}{m!\,(\mu + 1)\cdots(\mu + m)}\Big(\frac{\lambda}{2}\Big)^{2m}c_0 ,
> $$
>
> which is (4) without the factor $(-1)^m$. The same choice $c_0 = (\lambda/2)^\mu/\mu!$ gives the series of Definition §45.4. It converges for all $r$ by the ratio test, as in Theorem §45.2 (the ratio of terms has the same absolute value), and may be differentiated term by term, so it solves (7). All its terms are positive for $x > 0$; for $\mu = 0$ the derivative series $\sum_{m \ge 1} m\,(x/2)^{2m-1}/(m!)^2$ is positive too, so $I_0$ increases from $I_0(0) = 1$.

^pf-45-10

*Uses:* [[§45★ Bessel's Equation#^thm-45-1|§45.1]], [[§45★ Bessel's Equation#^thm-45-2|§45.2]], [[§45★ Bessel's Equation#^def-45-4|Def. §45.4]]

> [!example] Example §45.4: A Circular Plate Cooled by Convection
> Find the temperature in a circular plate whose faces are exposed to convection, if
>
> $$
> \frac{1}{r}\frac{d}{dr}\Big(r\frac{du}{dr}\Big) - \gamma^2(u - T) = 0, \quad 0 < r < a, \qquad u(a) = T_1 ,
> $$
>
> with $u$ bounded at the center; here $T$ is the temperature of the surrounding fluid, $T_1$ that of the rim, and $\gamma^2 > 0$ measures the heat loss through the faces (compare the thin plate of [[§42 Three-Dimensional Heat Equation#^ex-42-3|Example §42.3]]).
>
> **Reduce to the modified Bessel equation.** Put $w = u - T$. Then $\frac{1}{r}(rw')' - \gamma^2w = 0$, or $(rw')' - \gamma^2rw = 0$: equation (7) with $\mu = 0$ and $\lambda = \gamma$. Its bounded solutions are $w = AI_0(\gamma r)$: a second solution behaves like $\ln(1/r)$ at the center, as shown in [[§45★ Bessel's Equation#^ex-45-2|Example §45.2]], and is excluded just as $Y_0$ is (its standard form is called $K_0$).
>
> **Boundary condition.** $w(a) = T_1 - T = AI_0(\gamma a)$, and $I_0(\gamma a) \ne 0$ by Theorem §45.10, so
>
> $$
> u(r) = T + (T_1 - T)\,\frac{I_0(\gamma r)}{I_0(\gamma a)} .
> $$
>
> Check: $u(a) = T + (T_1 - T) = T_1$. Since $I_0$ is increasing, $u$ moves monotonically from $T_1$ at the rim toward $T$ at the center. For example, with $\gamma a = 2$, $I_0(2) = 2.2796$, so the center is at $T + 0.439(T_1 - T)$: less than half of the rim's excess temperature reaches the center. For large $\gamma a$ the center is nearly at the fluid temperature.
>
> *Powers: Exercise 5.5.9*

^ex-45-4
