---
type: section
subject: "[[Fourier Series and PDEs]]"
chapter: 5
section: "55★"
powers: "5.5"
aliases: ["Powers 5.5"]
tags: [fourier-series-and-pdes, math341, extension]
---
← [[§54★ Problems in Polar Coordinates]] · ↑ [[· 5 Higher Dimensions and Other Coordinates]] · [[§56★ Properties of Bessel Functions]] →

*Powers, Section 5.5.*
★ *Beyond MAT 341: the course did not cover this section; it is included from Powers.*

Separating variables in polar coordinates left the radial equation $(rR')' - \mu^2R/r + \lambda^2rR = 0$ ([[§54★ Problems in Polar Coordinates#^thm-54-2|Theorem §54.2]]). It has a singular point at $r = 0$, so it cannot be solved by a power series alone; the method of Frobenius, a power series times $r^\alpha$, produces the Bessel function of the first kind $J_\mu(\lambda r)$, bounded at the origin. A second solution, from reduction of order, is the Bessel function of the second kind $Y_\mu(\lambda r)$, unbounded at the origin, so in a disk only $J_\mu$ survives. Both oscillate like damped cosines with infinitely many zeros, and the zeros of $J_\mu$ play the role that the multiples of $\pi$ play for $\sin x$: they give the eigenvalues, hence the cooling rates of a cylinder and the frequencies of a drum. The section also collects the derivative and integral formulas used in the next sections and introduces the modified Bessel functions, which arise when the sign of $\lambda^2$ is reversed.

## Bessel's Equation and the Method of Frobenius

> [!definition] Definition §55.1: Bessel's Equation
> **Bessel's equation** of order $\mu \ge 0$, with parameter $\lambda > 0$, is
>
> $$
> \frac{d}{dr}\Big(r\frac{dR}{dr}\Big) - \frac{\mu^2}{r}R + \lambda^2rR = 0, \qquad 0 < r , \qquad (1)
> $$
>
> or, multiplied by $r$, $r^2R'' + rR' + (\lambda^2r^2 - \mu^2)R = 0$. In the variable $x = \lambda r$ it becomes $x^2y'' + xy' + (x^2 - \mu^2)y = 0$ for $y(x) = R(x/\lambda)$, so $\lambda$ only rescales $r$.
>
> *Powers: 5.5, Equation (1); 5.4, Equation (12)*

^def-55-1

> [!remark]- Connections
> - In standard form, $R'' + \frac{1}{r}R' + \big(\lambda^2 - \frac{\mu^2}{r^2}\big)R = 0$, a second-order linear equation whose coefficients are continuous on $0 < r < \infty$ but not at $r = 0$. The existence and uniqueness theorem [[§18 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-18-1|331 Thm. §18.1]] applies on $(0, \infty)$, and the solution space there is two-dimensional; at $r = 0$, a [[§2★ Variable Coefficients and Higher-Order Equations#^def-2-4|regular singular point]], solutions may blow up.
> - The radial part of the two-dimensional Helmholtz equation $\nabla^2\phi + \lambda^2\phi = 0$ in polar coordinates ([[§44 Potential Equation#^thm-44-3|Theorem §44.3]]), which is how it arose in [[§54★ Problems in Polar Coordinates#^thm-54-2|Theorem §54.2]].

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

^rem-55-1

> [!theorem] Theorem §55.1: The Frobenius Coefficients for Bessel's Equation
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

^thm-55-1

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

^pf-55-1

*Uses:* [[§55★ Bessel's Equation#^def-55-1|Def. §55.1]]

> [!remark]- Remark: The Other Root α = −μ
> For $\alpha = -\mu$ the coefficient of $c_k$ is $(k - \mu)^2 - \mu^2 = k(k - 2\mu)$, which vanishes at $k = 2\mu$. When $2\mu$ is not an integer the recursion goes through and gives a second solution, $J_{-\mu}$. When $\mu$ is an integer, the case met in the disk problems, the recursion breaks down at $k = 2\mu$ (for $\mu = 0$ the two roots coincide), and the second solution is not of the form (2). That is why Powers finds it by a different method, Theorem §55.3.

^rem-55-2

> [!definition] Definition §55.2: Bessel Function of the First Kind
> For integer $\mu \ge 0$, choose by convention $c_0 = \Big(\dfrac{\lambda}{2}\Big)^\mu\cdot\dfrac{1}{\mu!}$ in (4). The solution of (1) so obtained is the **Bessel function of the first kind of order $\mu$**:
>
> $$
> J_\mu(\lambda r) = \Big(\frac{\lambda r}{2}\Big)^\mu\sum_{m=0}^{\infty} \frac{(-1)^m}{m!\,(\mu + m)!}\Big(\frac{\lambda r}{2}\Big)^{2m} . \qquad (5)
> $$
>
> As a function of one variable, $J_\mu(x) = \sum_{m \ge 0} \dfrac{(-1)^m}{m!\,(m + \mu)!}\Big(\dfrac{x}{2}\Big)^{2m + \mu}$, and (5) is $J_\mu$ evaluated at $x = \lambda r$.
>
> *Powers: 5.5, Equation (5)*

^def-55-2

The series serves for evaluating $J_\mu$ and for obtaining its properties. From now on, Powers says, *consider the Bessel functions of the first kind to be as well known as sines and cosines*, although less familiar.

> [!remark]- Connections
> - Stewart defines $J_0$ by the same series and finds its domain by the ratio test and its derivative term by term: [[§89 Representations of Functions as Power Series#^ex-89-5|Calc Ex. §89.5]].
> - The rigorous facts behind Theorem §55.2: radius of convergence, [[§23 Power Series#^thm-23-2|451 Thm. §23.2]]; a power series may be differentiated term by term inside its interval of convergence, [[§26 Differentiation and Integration of Power Series#^thm-26-4|451 Thm. §26.4]].
> - See also: [[§66 Laurent Series#^ex-66-2|342 Ex. §66.2]] (the $J_n$ as Laurent coefficients of $\exp\big[\frac z2\big(w - \frac1w\big)\big]$, with the integral formula $J_n(z) = \frac1\pi\int_0^\pi\cos(n\phi - z\sin\phi)\,d\phi$).
> - Used in Electromagnetism: the four kinds of Bessel function in cylindrical boundary-value problems — [[§C6.3 Separation in Cylindrical and Polar Coordinates#^def-c6-3-1|EM Def. §C6.3.1]], [[§C6.3 Separation in Cylindrical and Polar Coordinates#^thm-c6-3-1|EM Theorem §C6.3.1]].

> [!theorem] Theorem §55.2: J_μ Solves Bessel's Equation
> For integer $\mu \ge 0$ the series (5) converges for every $r$, and $R = J_\mu(\lambda r)$ is a solution of Bessel's equation (1) on $0 < r < \infty$. It is bounded near $r = 0$, with $J_0(0) = 1$ and $J_\mu(0) = 0$ for $\mu \ge 1$.
>
> *Powers: 5.5 (text)*

^thm-55-2

> [!proof]+ Proof
> (Powers asserts this; here is why.) Write $s = \lambda r/2$. The ratio of consecutive terms of the series in (5) is
>
> $$
> \left|\frac{(-1)^{m+1}s^{2m+2}}{(m+1)!\,(\mu + m + 1)!}\cdot\frac{m!\,(\mu + m)!}{(-1)^ms^{2m}}\right| = \frac{s^2}{(m + 1)(\mu + m + 1)} \to 0
> $$
>
> as $m \to \infty$, for every $s$. By the ratio test the series converges for all $r$: it is a power series with infinite radius of convergence. Such a series may be differentiated term by term any number of times, so the computation in the proof of Theorem §55.1 is legitimate for $R = J_\mu(\lambda r) = \sum c_kr^{\mu + k}$, and since its coefficients satisfy (3) and (4), all coefficients of $r^2R'' + rR' + (\lambda^2r^2 - \mu^2)R$ vanish: $R$ solves (1). Being a convergent power series times $r^\mu$, $J_\mu(\lambda r)$ is continuous, hence bounded near $0$; at $r = 0$ every term with a positive power of $r$ vanishes, so $J_\mu(0)$ is the $m = 0$ term $(\lambda r/2)^{\mu}/\mu!$ at $r = 0$, which is $1$ for $\mu = 0$ and $0$ for $\mu \ge 1$.

^pf-55-2

*Uses:* [[§55★ Bessel's Equation#^thm-55-1|§55.1]], [[§55★ Bessel's Equation#^def-55-2|Def. §55.2]], [[§14 Series#^thm-14-9|451 Thm. §14.9]] (ratio test), [[§26 Differentiation and Integration of Power Series#^thm-26-4|451 Thm. §26.4]] (term-by-term differentiation)

> [!example] Example §55.1: The Series for J₀ and J₁
> Write out the first terms of $J_0(x)$ and $J_1(x)$, evaluate $J_0(1)$, and use the series to check the first zero $2.405$ of $J_0$.
>
> **The series.** With $\mu = 0$ the denominators in (5) are $(m!)^2 2^{2m} = 1, 4, 64, 2304, 147456$; with $\mu = 1$ they are $m!\,(m + 1)!\,2^{2m+1} = 2, 16, 384, 18432$:
>
> $$
> J_0(x) = 1 - \frac{x^2}{4} + \frac{x^4}{64} - \frac{x^6}{2304} + \frac{x^8}{147456} - \cdots, \qquad J_1(x) = \frac{x}{2} - \frac{x^3}{16} + \frac{x^5}{384} - \frac{x^7}{18432} + \cdots .
> $$
>
> Differentiating the first series term by term gives $-\frac{x}{2} + \frac{x^3}{16} - \frac{x^5}{384} + \cdots = -J_1(x)$, a first instance of Theorem §56.2.
>
> **$J_0(1)$.** $1 - 0.25 + 0.015625 - 0.000434 + 0.000007 = 0.765198$; the terms alternate and decrease, so the error is less than the next term, about $10^{-7}$ (the true value is $0.7651977$).
>
> **The first zero.** At $x = 2.405$, $(x/2)^2 = 1.44601$, and the partial sums are
>
> $$
> 1, \quad -0.44601, \quad 0.07673, \quad -0.00726, \quad 0.00033, \quad -0.00011, \quad -0.0000900, \quad -0.0000906, \quad \ldots
> $$
>
> converging to $J_0(2.405) \approx -0.00009$. So $J_0$ changes sign just below $2.405$ (the zero is $2.40483$). For larger $x$ more terms are needed before the terms start to decrease, which is why tables, or the asymptotic form of [[§56★ Properties of Bessel Functions#^rem-56-1|Remark: Why J₀ Oscillates]], are used there.
>
> *Powers: 5.5, Equation (5); Table 1*

^ex-55-1

## The Second Solution

There must be a second, independent solution of Bessel's equation.

> [!theorem] Theorem §55.3: A Second Solution by Reduction of Order
> On any interval of $r > 0$ on which $J_\mu(\lambda r) \ne 0$, the function
>
> $$
> J_\mu(\lambda r)\cdot\int \frac{dr}{r\,J_\mu^2(\lambda r)} \qquad (6)
> $$
>
> is a solution of Bessel's equation (1), independent of $J_\mu(\lambda r)$.
>
> *Powers: 5.5, Equation (6)*

^thm-55-3

> [!proof]+ Proof
> Powers says that this follows by variation of parameters; the method is reduction of order. In standard form (1) is $R'' + p(r)R' + q(r)R = 0$ with $p(r) = 1/r$. Let $y_1(r) = J_\mu(\lambda r)$, a solution by Theorem §55.2. By reduction of order, $R = v(r)y_1(r)$ is a solution if and only if
>
> $$
> y_1v'' + \Big(2y_1' + \frac{1}{r}y_1\Big)v' = 0 , \qquad\text{that is,}\qquad \frac{(v')'}{v'} = -\frac{2y_1'}{y_1} - \frac{1}{r}
> $$
>
> where $y_1 \ne 0$ and $v' \ne 0$. Integrating, $\ln|v'| = -2\ln|y_1| - \ln r + \text{const}$, so $v' = C/(r\,y_1^2)$ and $v = C\int dr/(r\,y_1^2)$; with $C = 1$ this is (6). It is independent of $y_1$ because $v$ is not constant ($v' \ne 0$). Equivalently, the Wronskian of $y_1$ and $vy_1$ is $y_1(vy_1)' - y_1'vy_1 = y_1^2v' = 1/r \ne 0$, in agreement with Abel's formula $W = C\exp(-\int dr/r) = C/r$.

^pf-55-3

*Uses:* [[§55★ Bessel's Equation#^thm-55-2|§55.2]], [[§20 Repeated Roots; Reduction of Order#^prop-20-3|331 Prop. §20.3]] (reduction of order), [[§18 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-18-8|331 Thm. §18.8]] (Abel's theorem)

> [!definition] Definition §55.3: Bessel Function of the Second Kind
> In its standard form, normalized by convention, the second solution of Bessel's equation is called the **Bessel function of the second kind of order $\mu$** and is denoted $Y_\mu(\lambda r)$. It is a solution on all of $0 < r < \infty$, independent of $J_\mu(\lambda r)$.
>
> *Powers: 5.5 (text)*

^def-55-3

> [!remark]- Remark: The Series for Y₀
> Powers does not give the standard normalization. For $\mu = 0$ it is
>
> $$
> Y_0(x) = \frac{2}{\pi}\Big(\ln\frac{x}{2} + \gamma\Big)J_0(x) + \frac{2}{\pi}\sum_{m=1}^{\infty} \frac{(-1)^{m+1}H_m}{(m!)^2}\Big(\frac{x}{2}\Big)^{2m}, \qquad H_m = 1 + \frac12 + \cdots + \frac1m ,
> $$
>
> where $\gamma = 0.5772\ldots$ is Euler's constant. The logarithm is the behavior predicted by Theorem §55.4: $Y_0(x) \approx \frac{2}{\pi}\ln x$ as $x \to 0^+$. (Numerically $Y_0(1) = 0.0883$, and the first zero of $Y_0$ is at $0.894$.)
>
> *Source: the standard normalization (DLMF §10.8); not in Powers.*

^rem-55-3

> [!theorem] Theorem §55.4: The Second Solution Is Unbounded at the Origin
> $|Y_\mu(\lambda r)| \to \infty$ as $r \to 0^+$. More precisely, the solution (6) behaves like a constant times $\ln r$ if $\mu = 0$ and like a constant times $r^{-\mu}$ if $\mu > 0$.
>
> *Powers: 5.5 (text)*

^thm-55-4

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
> Take the antiderivative in (6) as $\int_r^{r_0}$ (another choice adds a multiple of $J_\mu$, which is bounded). If $\mu = 0$, $\int_r^{r_0} Ks^{-1}(1 + F)\,ds = K\ln(r_0/r) + O(1)$, and since $J_0(\lambda r) \to 1$, the solution (6) is $K\ln(1/r) + O(1) \to \infty$. If $\mu \ge 1$ (an integer, as in Definition §55.2; for non-integer $\mu > 0$ the same computation works with $\Gamma(\mu + 1)$ in place of $\mu!$), $\int_r^{r_0} Ks^{-1-2\mu}(1 + F)\,ds = \frac{K}{2\mu}r^{-2\mu} + O(r^{2-2\mu}) + O(\ln(1/r)) + O(1)$, whose leading term is $\frac{K}{2\mu}r^{-2\mu}$; multiplied by $J_\mu(\lambda r) \sim (\lambda r/2)^\mu/\mu!$ it gives (6) $\sim \frac{(\mu - 1)!}{2}\big(\frac{2}{\lambda}\big)^\mu r^{-\mu} \to \infty$.
>
> Finally $Y_\mu = AJ_\mu + B\cdot(6)$ for some constants with $B \ne 0$, since $Y_\mu$ is independent of $J_\mu$; as $J_\mu$ is bounded near $0$, $|Y_\mu(\lambda r)| \to \infty$.

^pf-55-4

*Uses:* [[§55★ Bessel's Equation#^def-55-2|Def. §55.2]], [[§55★ Bessel's Equation#^thm-55-3|§55.3]], [[§55★ Bessel's Equation#^def-55-3|Def. §55.3]]

> [!theorem] Theorem §55.5: General Solution of Bessel's Equation
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

^thm-55-5

> [!proof]+ Proof
> On $0 < r < \infty$ the equation in standard form has continuous coefficients. $J_\mu(\lambda r)$ and $Y_\mu(\lambda r)$ are solutions there, and they are linearly independent: $J_\mu(\lambda r)$ stays bounded as $r \to 0$ and $Y_\mu(\lambda r)$ does not (Theorem §55.4), so neither is a constant multiple of the other. For two solutions of a second-order linear equation, independence means that their Wronskian is not zero, so they form a fundamental set and $AJ_\mu + BY_\mu$ contains every solution. If $B \ne 0$, then $|AJ_\mu(\lambda r) + BY_\mu(\lambda r)| \ge |B|\,|Y_\mu(\lambda r)| - |A|\,|J_\mu(\lambda r)| \to \infty$ as $r \to 0$; so a bounded solution has $B = 0$.

^pf-55-5

*Uses:* [[§55★ Bessel's Equation#^thm-55-2|§55.2]], [[§55★ Bessel's Equation#^thm-55-4|§55.4]], [[§18 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-18-4|331 Thm. §18.4]] (general solution from a fundamental set)

> [!remark]- Connections
> - The general solution of a second-order linear equation from two independent solutions, and independence as a nonzero Wronskian: [[§18 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-18-4|331 Thm. §18.4]], with Abel's theorem [[§18 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-18-8|331 Thm. §18.8]] giving $W[J_\mu, Y_\mu] = C/r$ without computing either function.
> - The same pattern in the potential problem of [[§48 Potential in a Disk#^thm-48-2|Theorem §48.2]]: the radial equation $r^2R'' + rR' - m^2R = 0$ (Bessel's equation with $\lambda = 0$) has solutions $r^m$ and $r^{-m}$ (or $1$ and $\ln r$), and boundedness at the center discards the second, just as it discards $Y_\mu$ here.
> - Used in Electromagnetism: separated solutions of Laplace's equation in cylindrical coordinates, and the zeros, asymptotics and orthogonality boundary-value problems need — [[§C6.3 Separation in Cylindrical and Polar Coordinates#^thm-c6-3-1|EM Theorem §C6.3.1]], [[§C6.3 Separation in Cylindrical and Polar Coordinates#^thm-c6-3-2|EM Theorem §C6.3.2]].

![[m341-45-2.svg]]
*The Bessel functions of the second kind $Y_0$ (blue) and $Y_1$ (red), computed with SciPy. Both tend to $-\infty$ at the origin, $Y_0$ like $\frac{2}{\pi}\ln x$ and $Y_1$ like $-\frac{2}{\pi x}$, which is why they are excluded from problems in a full disk. For large $x$ they oscillate within the envelope $\pm\sqrt{2/(\pi x)}$ (dashed), like $J_0$ and $J_1$ shifted by a quarter period.*

*Continued in [[§56★ Properties of Bessel Functions]]: zeros, derivative and integral formulas, radial eigenvalue problems and modified Bessel functions.*
