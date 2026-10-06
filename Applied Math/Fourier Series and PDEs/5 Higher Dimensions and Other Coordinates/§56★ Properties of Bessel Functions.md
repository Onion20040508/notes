---
type: section
subject: "[[Fourier Series and PDEs]]"
chapter: 5
section: "56★"
powers: "5.5"
aliases: ["Powers 5.5 (cont.)"]
tags: [fourier-series-and-pdes, math341, extension]
---
← [[§55★ Bessel's Equation]] · ↑ [[· 5 Higher Dimensions and Other Coordinates]] · [[§57★ Temperature in a Cylinder]] →

*Powers, Section 5.5.*
★ *Beyond MAT 341: the course did not cover this section; it is included from Powers.*

The Bessel functions $J_\mu$ and $Y_\mu$ of [[§55★ Bessel's Equation|§55★]] both oscillate like damped cosines with infinitely many zeros, and the zeros of $J_\mu$ play the role that the multiples of $\pi$ play for $\sin x$: they give the eigenvalues, hence the cooling rates of a cylinder and the frequencies of a drum. This section also collects the derivative and integral formulas used in the next sections and introduces the modified Bessel functions, which arise when the sign of $\lambda^2$ is reversed.

## Zeros and Behavior at Infinity

> [!theorem] Theorem §56.1: Zeros of the Bessel Functions
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

^thm-56-1

*Powers omits the proof. (The table agrees with values recomputed with SciPy to all digits shown.)*

![[m341-45-1.svg]]
*$J_0$ (blue) and $J_1$ (red), computed with SciPy. $J_0(0) = 1$ and $J_1(0) = 0$; both oscillate with slowly decreasing amplitude, like damped cosines. The dots mark the zeros of $J_0$ (2.405, 5.520, 8.654, 11.792) and the circles those of $J_1$ (3.832, 7.016, 10.173, 13.324): they alternate (Corollary §56.4 puts a zero of $J_1$ between consecutive zeros of $J_0$; Rolle's theorem applied to $xJ_1(x)$, whose derivative is $xJ_0(x)$ by Theorem §56.2(d), puts a zero of $J_0$ between consecutive zeros of $J_1$), and consecutive zeros are about $\pi$ apart. $J_1$ has its maximum $0.582$ at $x = 1.841$, and $J_0$ its minimum $-0.403$ at the first zero of $J_1$, since $J_0' = -J_1$.*

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

^rem-56-1
## Derivative and Integral Formulas

The next formulas, Powers' Exercises 5.5.3–5.5.7, are used in [[§57★ Temperature in a Cylinder|§46]] and after to compute coefficients of Bessel series.

> [!theorem] Theorem §56.2: Derivatives of Bessel Functions
> With the prime denoting differentiation with respect to the argument:
> - (a) $\dfrac{d}{dr}J_\mu(\lambda r) = \lambda J_\mu'(\lambda r)$;
> - (b) $J_0'(x) = -J_1(x)$, so $\dfrac{d}{dr}J_0(\lambda r) = -\lambda J_1(\lambda r)$;
> - (c) $\dfrac{d}{dx}\big(x^{-\mu}J_\mu(x)\big) = -x^{-\mu}J_{\mu+1}(x)$;
> - (d) $\dfrac{d}{dx}\big(x^\mu J_\mu(x)\big) = x^\mu J_{\mu-1}(x)$, for $\mu \ge 1$.
>
> *Powers: Exercises 5.5.3, 5.5.4 and 5.5.6*

^thm-56-2

> [!proof]+ Proof
> (a) is the chain rule. For (c) and (d), differentiate the series of Definition §55.2 term by term (Theorem §55.2).
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

^pf-56-2

*Uses:* [[§55★ Bessel's Equation#^def-55-2|Def. §55.2]], [[§55★ Bessel's Equation#^thm-55-2|§55.2]], [[§26 Differentiation and Integration of Power Series#^thm-26-4|451 Thm. §26.4]]

> [!theorem] Corollary §56.3: An Integral Formula
> For integer $\mu \ge 0$,
>
> $$
> \int x^{\mu+1}J_\mu(x)\,dx = x^{\mu+1}J_{\mu+1}(x) + C ;
> $$
>
> in particular $\displaystyle\int xJ_0(x)\,dx = xJ_1(x) + C$.
>
> *Powers: Exercise 5.5.7*

^cor-56-3

> [!proof]+ Proof
> Theorem §56.2(d) with $\mu + 1$ in place of $\mu$ reads $\frac{d}{dx}\big(x^{\mu+1}J_{\mu+1}(x)\big) = x^{\mu+1}J_\mu(x)$, so $x^{\mu+1}J_{\mu+1}$ is an antiderivative of $x^{\mu+1}J_\mu$. (Powers writes the integrand as $x^\mu J_\mu(x)\,x$.)

^pf-56-3

*Uses:* [[§56★ Properties of Bessel Functions#^thm-56-2|§56.2]]

> [!theorem] Corollary §56.4: J₁ Has Infinitely Many Zeros
> Between any two consecutive positive zeros of $J_0$ there is a zero of $J_1$. In particular $J_1(x) = 0$ has an infinite number of solutions.
>
> *Powers: Exercise 5.5.5*

^cor-56-4

> [!proof]+ Proof
> Let $\alpha < \alpha'$ be consecutive positive zeros of $J_0$. $J_0$ is differentiable, and $J_0(\alpha) = J_0(\alpha') = 0$, so by Rolle's theorem $J_0'(\xi) = 0$ for some $\xi$ in $(\alpha, \alpha')$. By Theorem §56.2(b), $J_1(\xi) = -J_0'(\xi) = 0$. Since $J_0$ has infinitely many zeros (Theorem §56.1), this gives infinitely many zeros of $J_1$, one in each gap. (In the table: $2.405 < 3.832 < 5.520 < 7.016 < 8.654 < \cdots$.)

^pf-56-4

*Uses:* [[§56★ Properties of Bessel Functions#^thm-56-1|§56.1]], [[§56★ Properties of Bessel Functions#^thm-56-2|§56.2]], [[§29 The Mean Value Theorem#^thm-29-2|451 Thm. §29.2]] (Rolle's theorem)

## Radial Eigenvalue Problems

> [!example] Example §56.1: The Radial Eigenvalue Problem with a Fixed Edge
> Find the values of $\lambda$ for which
>
> $$
> \frac{1}{r}\frac{d}{dr}\Big(r\frac{d\phi}{dr}\Big) + \lambda^2\phi = 0, \quad 0 < r < a, \qquad \phi(a) = 0, \quad \phi(0) \text{ bounded}
> $$
>
> has a nonzero solution, and describe the eigenfunctions.
>
> **Bessel's equation of order 0.** Multiplying by $r$ gives $(r\phi')' + \lambda^2r\phi = 0$, which is (1) with $\mu = 0$. By Theorem §55.5 its bounded solutions are $\phi = AJ_0(\lambda r)$.
>
> **The boundary condition.** $\phi(a) = AJ_0(\lambda a) = 0$ with $A \ne 0$ requires $\lambda a$ to be a zero of $J_0$: $\lambda a = \alpha_{0n}$, so
>
> $$
> \lambda_n = \frac{\alpha_{0n}}{a} = \frac{2.405}{a},\ \frac{5.520}{a},\ \frac{8.654}{a},\ \ldots, \qquad \phi_n(r) = J_0\Big(\frac{\alpha_{0n}r}{a}\Big) .
> $$
>
> **No other cases.** For $\lambda = 0$, $(r\phi')' = 0$ gives $\phi = A + B\ln r$; boundedness forces $B = 0$ and $\phi(a) = 0$ then forces $A = 0$. A negative $\lambda^2 = -\gamma^2$ gives the modified Bessel equation, whose bounded solutions $AI_0(\gamma r)$ never vanish for $r > 0$ ([[§56★ Properties of Bessel Functions#^thm-56-5|Theorem §56.5]]), so $\phi(a) = 0$ forces $A = 0$. (Every other solution is unbounded: since $I_0 > 0$ on $(0, \infty)$, reduction of order as in [[§55★ Bessel's Equation#^thm-55-3|Theorem §55.3]] gives the second solution $I_0(\gamma r)\int dr/(r\,I_0^2(\gamma r))$, and the proof of [[§55★ Bessel's Equation#^thm-55-4|Theorem §55.4]] for $\mu = 0$ applies word for word, because $I_0(\gamma r) = 1 + O(r^2)$ just as $J_0(\lambda r)$ is: it behaves like $\ln(1/r)$.)
>
> **The eigenfunctions.** $\phi_n$ starts at $\phi_n(0) = 1$ and vanishes at $r = a$; inside, it vanishes where $\alpha_{0n}r/a$ is an earlier zero of $J_0$, so it has $n - 1$ zeros in $0 < r < a$ (the nodal circles of a drum). $\phi_1$ decreases from $1$ to $0$ without changing sign; $\phi_2$ changes sign at $r = (2.405/5.520)a = 0.436a$; $\phi_3$ at $r = 0.278a$ and $0.638a$. Their graphs are the piece of the blue curve in the figure above from $0$ to the $n$th zero, compressed to the interval $[0, a]$. This is the eigenvalue problem of the cylinder, [[§57★ Temperature in a Cylinder#^prop-57-1|Proposition §57.1]].
>
> *Powers: Exercises 5.5.1 and 5.5.2*

^ex-56-1

> [!example] Example §56.2: The Radial Eigenvalue Problem with an Insulated Edge
> Solve the eigenvalue problem
>
> $$
> \frac{1}{r}\frac{d}{dr}\Big(r\frac{d\phi}{dr}\Big) + \lambda^2\phi = 0, \quad 0 < r < a, \qquad \frac{d\phi}{dr}(a) = 0, \quad \phi(0) \text{ bounded} .
> $$
>
> As in Example §56.1, for $\lambda > 0$ the bounded solutions are $\phi = AJ_0(\lambda r)$. By Theorem §56.2(b), $\phi'(r) = -\lambda AJ_1(\lambda r)$, so the boundary condition is $\lambda AJ_1(\lambda a) = 0$: $\lambda a$ must be a positive zero of $J_1$. This time $\lambda = 0$ also works: $\phi = A + B\ln r$ is bounded only for $B = 0$, and the constant $\phi = 1$ satisfies $\phi'(a) = 0$. The eigenvalues and eigenfunctions are
>
> $$
> \lambda_0 = 0, \quad \phi_0 = 1; \qquad \lambda_n = \frac{\alpha_{1n}}{a} = \frac{3.832}{a},\ \frac{7.016}{a},\ \frac{10.173}{a},\ \ldots, \quad \phi_n(r) = J_0\Big(\frac{\alpha_{1n}r}{a}\Big) .
> $$
>
> The eigenfunctions are pieces of $J_0$ ending at its turning points rather than at its zeros: $\phi_1 = J_0(3.832r/a)$ ends at the minimum of $J_0$, with zero slope. This is the radial problem for the insulated plate of [[§54★ Problems in Polar Coordinates#^ex-54-3|Example §54.3]], and the constant eigenfunction is the mean temperature that the plate keeps forever.
>
> *Powers: Exercise 5.5.10*

^ex-56-2

## Modified Bessel Functions

> [!definition] Definition §56.1: Modified Bessel Equation
> The **modified Bessel equation** differs from Bessel's equation only in the sign of one term:
>
> $$
> \frac{d}{dr}\Big(r\frac{dR}{dr}\Big) - \frac{\mu^2}{r}R - \lambda^2rR = 0 . \qquad (7)
> $$
>
> *Powers: 5.5, Equation (7) and text*

^def-56-1

> [!definition] Definition §56.2: Modified Bessel Function of the First Kind
> The solution of the modified Bessel equation (7) ([[§56★ Properties of Bessel Functions#^def-56-1|Definition §56.1]]) that is bounded at $r = 0$, in standard form, is the **modified Bessel function of the first kind of order $\mu$**,
>
> $$
> I_\mu(\lambda r) = \Big(\frac{\lambda r}{2}\Big)^\mu\sum_{m=0}^{\infty} \frac{1}{m!\,(\mu + m)!}\Big(\frac{\lambda r}{2}\Big)^{2m} .
> $$
>
> *Powers: 5.5, Equation (7) and text*

^def-56-2

> [!theorem] Theorem §56.5: I_μ Solves the Modified Bessel Equation
> For integer $\mu \ge 0$, $I_\mu(\lambda r)$ is a solution of (7), bounded at $r = 0$; its power-series coefficients are those of $J_\mu(\lambda r)$ except for signs. Every term of its series is positive, so $I_\mu(x) > 0$ for $x > 0$, and $I_0$ is increasing with $I_0(0) = 1$; in particular $I_\mu$ has no positive zeros.
>
> *Powers: Exercise 5.5.8*

^thm-56-5

> [!proof]+ Proof
> Apply the method of Frobenius exactly as in Theorem §55.1, with $-\lambda^2$ in place of $\lambda^2$. The conditions become $c_0(\alpha^2 - \mu^2) = 0$, $c_1((\alpha + 1)^2 - \mu^2) = 0$ and $c_k((\alpha + k)^2 - \mu^2) - \lambda^2c_{k-2} = 0$. With $\alpha = \mu$: $c_1 = 0$, odd coefficients vanish, and
>
> $$
> c_k = +\lambda^2\frac{c_{k-2}}{k(2\mu + k)}, \qquad c_{2m} = \frac{1}{m!\,(\mu + 1)\cdots(\mu + m)}\Big(\frac{\lambda}{2}\Big)^{2m}c_0 ,
> $$
>
> which is (4) without the factor $(-1)^m$. The same choice $c_0 = (\lambda/2)^\mu/\mu!$ gives the series of Definition §56.2. It converges for all $r$ by the ratio test, as in Theorem §55.2 (the ratio of terms has the same absolute value), and may be differentiated term by term, so it solves (7). All its terms are positive for $x > 0$; for $\mu = 0$ the derivative series $\sum_{m \ge 1} m\,(x/2)^{2m-1}/(m!)^2$ is positive too, so $I_0$ increases from $I_0(0) = 1$.

^pf-56-5

*Uses:* [[§55★ Bessel's Equation#^thm-55-1|§55.1]], [[§55★ Bessel's Equation#^thm-55-2|§55.2]], [[§56★ Properties of Bessel Functions#^def-56-1|Def. §56.1]], [[§56★ Properties of Bessel Functions#^def-56-2|Def. §56.2]]

> [!example] Example §56.3: A Circular Plate Cooled by Convection
> Find the temperature in a circular plate whose faces are exposed to convection, if
>
> $$
> \frac{1}{r}\frac{d}{dr}\Big(r\frac{du}{dr}\Big) - \gamma^2(u - T) = 0, \quad 0 < r < a, \qquad u(a) = T_1 ,
> $$
>
> with $u$ bounded at the center; here $T$ is the temperature of the surrounding fluid, $T_1$ that of the rim, and $\gamma^2 > 0$ measures the heat loss through the faces (compare the thin plate of [[§52 Three-Dimensional Heat Equation#^ex-52-3|Example §52.3]]).
>
> **Reduce to the modified Bessel equation.** Put $w = u - T$. Then $\frac{1}{r}(rw')' - \gamma^2w = 0$, or $(rw')' - \gamma^2rw = 0$: equation (7) with $\mu = 0$ and $\lambda = \gamma$. Its bounded solutions are $w = AI_0(\gamma r)$: a second solution behaves like $\ln(1/r)$ at the center, as shown in [[§56★ Properties of Bessel Functions#^ex-56-1|Example §56.1]], and is excluded just as $Y_0$ is (its standard form is called $K_0$).
>
> **Boundary condition.** $w(a) = T_1 - T = AI_0(\gamma a)$, and $I_0(\gamma a) \ne 0$ by Theorem §56.5, so
>
> $$
> u(r) = T + (T_1 - T)\,\frac{I_0(\gamma r)}{I_0(\gamma a)} .
> $$
>
> Check: $u(a) = T + (T_1 - T) = T_1$. Since $I_0$ is increasing, $u$ moves monotonically from $T_1$ at the rim toward $T$ at the center. For example, with $\gamma a = 2$, $I_0(2) = 2.2796$, so the center is at $T + 0.439(T_1 - T)$: less than half of the rim's excess temperature reaches the center. For large $\gamma a$ the center is nearly at the fluid temperature.
>
> *Powers: Exercise 5.5.9*

^ex-56-3
