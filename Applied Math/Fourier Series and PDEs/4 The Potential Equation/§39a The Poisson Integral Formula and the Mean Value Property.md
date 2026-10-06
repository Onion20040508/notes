---
type: section
subject: "[[Fourier Series and PDEs]]"
chapter: 4
section: 39
powers: "4.5"
aliases: ["Powers 4.5 (cont.)"]
tags: [fourier-series-and-pdes, math341]
---
← [[§39 Potential in a Disk]] · ↑ [[· 4 The Potential Equation]] →

*Powers, Section 4.5 · MAT 341 lectures 11.21, 11.26, 12.3 · HW 13 · Practice Final.*

Summing the series solution of Dirichlet's problem in a disk ([[§39 Potential in a Disk|§39]]) gives the Poisson integral formula. Setting $r = 0$ gives the mean value property, from which follow the maximum principle and the uniqueness of the solution of Dirichlet's problem in any region. Physically: the electrostatic potential inside a long cylinder with prescribed voltage on its surface, or the steady temperature in a circular plate.

## The Poisson Integral Formula

> [!theorem] Theorem §39.3: Poisson Integral Formula
> The solution (10)–(11) of Dirichlet's problem (1)–(4) can be written as a single integral:
>
> $$
> v(r, \theta) = \frac{1}{2\pi}\int_{-\pi}^{\pi}f(\phi)\,\frac{c^2 - r^2}{c^2 + r^2 - 2rc\cos(\theta - \phi)}\,d\phi, \qquad 0 \le r < c .
> $$
>
> *Powers: Exercise 4.5.8*

^thm-39-3

> [!proof]+ Proof
> Follow Powers' steps (a)–(e). Fix $r < c$ and $\theta$, and put $\rho = r/c < 1$.
>
> **(a)–(b)** Replace $\theta$ by $\phi$ in (11) and substitute the integrals for the coefficients in (10):
>
> $$
> v(r, \theta) = \frac{1}{2\pi}\int_{-\pi}^{\pi}f(\phi)\,d\phi + \sum_{n=1}^{\infty}\frac{r^n}{\pi c^n}\int_{-\pi}^{\pi}f(\phi)\big(\cos(n\phi)\cos(n\theta) + \sin(n\phi)\sin(n\theta)\big)\,d\phi .
> $$
>
> **(c)** By the identity $\cos(n\theta)\cos(n\phi) + \sin(n\theta)\sin(n\phi) = \cos\big(n(\theta - \phi)\big)$,
>
> $$
> v(r, \theta) = \frac{1}{2\pi}\int_{-\pi}^{\pi}f(\phi)\,d\phi + \sum_{n=1}^{\infty}\frac1\pi\int_{-\pi}^{\pi}f(\phi)\rho^n\cos\big(n(\theta - \phi)\big)\,d\phi .
> $$
>
> **(d)** Take the integral outside the series:
>
> $$
> v(r, \theta) = \frac{1}{2\pi}\int_{-\pi}^{\pi}f(\phi)\Big(1 + 2\sum_{n=1}^{\infty}\rho^n\cos\big(n(\theta - \phi)\big)\Big)\,d\phi .
> $$
>
> (Powers does not justify this; here is why it is allowed.) Let $K(\psi) = 1 + 2\sum_{n=1}^{\infty}\rho^n\cos(n\psi)$ and let $K_N$ be its $N$th partial sum. The terms satisfy $|2\rho^n\cos(n\psi)| \le 2\rho^n$ and $\sum 2\rho^n < \infty$, so by the Weierstrass M-test $K_N \to K$ uniformly in $\psi$. Hence
>
> $$
> \Big|\int_{-\pi}^{\pi}f(\phi)K(\theta - \phi)\,d\phi - \int_{-\pi}^{\pi}f(\phi)K_N(\theta - \phi)\,d\phi\Big| \le \sup_\psi|K(\psi) - K_N(\psi)|\int_{-\pi}^{\pi}|f(\phi)|\,d\phi \to 0 ,
> $$
>
> and the second integral is the $N$th partial sum of the series in (c). So the series in (c) converges to the integral in (d), for any $f$ with $\int|f| < \infty$ (bounded or not).
>
> **(e)** Sum the series ([[§15★ Complex Methods|§15★]], Powers' Exercise 1.10.5a). With $\psi = \theta - \phi$ and $w = \rho e^{i\psi}$, $|w| = \rho < 1$, the geometric series ([[§61 Convergence of Series#^ex-61-1|342 Ex. §61.1]]) gives
>
> $$
> 1 + \sum_{n=1}^{\infty}\rho^n\cos(n\psi) = \operatorname{Re}\sum_{n=0}^{\infty}w^n = \operatorname{Re}\frac{1}{1 - w} = \operatorname{Re}\frac{1 - \bar w}{|1 - w|^2} = \frac{1 - \rho\cos\psi}{1 - 2\rho\cos\psi + \rho^2} .
> $$
>
> Hence
>
> $$
> 1 + 2\sum_{n=1}^{\infty}\rho^n\cos(n\psi) = \frac{2(1 - \rho\cos\psi)}{1 - 2\rho\cos\psi + \rho^2} - 1 = \frac{1 - \rho^2}{1 - 2\rho\cos\psi + \rho^2} = \frac{c^2 - r^2}{c^2 + r^2 - 2rc\cos\psi} ,
> $$
>
> multiplying numerator and denominator by $c^2$. Substituting into (d) gives the formula.

^pf-39-3

*Uses:* [[§39 Potential in a Disk#^thm-39-2|§39.2]], [[§15★ Complex Methods|§15★]] (Exercise 1.10.5a), [[§25 More on Uniform Convergence#^thm-25-3|451 Thm. §25.3]] (M-test), [[§61 Convergence of Series#^ex-61-1|342 Ex. §61.1]] (geometric series)

> [!remark]- Connections
> - The kernel $\frac{c^2 - r^2}{c^2 + r^2 - 2rc\cos(\theta - \phi)}$ is, up to the factor $\frac{1}{2\pi c}$, the normal derivative on the circle of the Green's function of the disk. The general representation of a harmonic function by its boundary values comes from Green's second identity, [[§17 The Divergence Theorem in Higher Dimensions and Green's Identities#^thm-17-3|452 Thm. §17.3]], applied with the fundamental solution $\ln r$, [[§17 The Divergence Theorem in Higher Dimensions and Green's Identities#^thm-17-5|452 Thm. §17.5]]; 452 develops these tools but does not compute the kernel of the disk. The half-plane counterpart is [[§38 Potential in Unbounded Regions#^rem-38-2|Remark: The Half-Plane and Its Poisson Formula]].
> - Complex-variables version: [[§134★ Poisson Integral Formula#^thm-134-1|342 Thm. §134.1]] (the same formula, derived from the Cauchy integral formula; both proofs are kept), with the kernel's positivity and mean value $1$ in [[§134★ Poisson Integral Formula#^prop-134-2|342 Prop. §134.2]] and its series in [[§135★ Dirichlet Problem for a Disk#^prop-135-3|342 Prop. §135.3]].
> - Used in Electromagnetism: the three-dimensional analogue, Poisson's integral for the ball, with existence — [[§C6.2 Separation in Cartesian and Spherical Coordinates#^thm-c6-2-3|EM Theorem §C6.2.3]]; as the Poisson kernel of a Green function — [[§C7.3 Green Functions for Poisson’s Equation#^thm-c7-3-4|EM Theorem §C7.3.4]], [[§C7.4 Constructing Green Functions#^thm-c7-4-3|EM Theorem §C7.4.3]].

> [!remark] Remark: The Poisson Kernel Is a Weight
> The kernel is positive for $r < c$, since $c^2 + r^2 - 2rc\cos\psi \ge (c - r)^2 > 0$. Taking $f \equiv 1$, whose solution is $v \equiv 1$, shows $\frac{1}{2\pi}\int_{-\pi}^{\pi}\frac{c^2 - r^2}{c^2 + r^2 - 2rc\cos\psi}\,d\psi = 1$. So $v(r, \theta)$ is a weighted average of the boundary values, and $\min f \le v \le \max f$: the maximum principle for the disk, read off directly. At $r = 0$ the kernel is identically $1$ and the weighted average is the plain average: the mean value property. As $r \to c$ the weight concentrates near $\phi = \theta$, which is why $v(r, \theta) \to f(\theta)$ at points of continuity of $f$.

^rem-39-2

## Properties of the Solution

> [!theorem] Theorem §39.4: Mean Value Property
> **(a)** The solution of the potential equation at the center of a disk equals the average of its values around the edge: for the solution $v$ of (1)–(4),
>
> $$
> v(0, \theta) = a_0 = \frac{1}{2\pi}\int_{-\pi}^{\pi}f(\theta)\,d\theta = \frac{1}{2\pi}\int_{-\pi}^{\pi}v(c, \theta)\,d\theta ,
> $$
>
> and also
>
> $$
> v(0, \theta) = \frac{1}{2\pi}\int_{-\pi}^{\pi}v(r, \theta)\,d\theta \qquad (13)
> $$
>
> for any $r$ between $0$ and $c$.
>
> **(b)** More generally, if $u$ is harmonic in a region that contains a closed disk of radius $\rho$ centered at a point $P$, then $u(P)$ equals the average of $u$ over the circle of radius $\rho$ about $P$.
>
> *Powers: 4.5, Equation (13) and text*

^thm-39-4

> [!proof]+ Proof
> **(a)** Setting $r = 0$ in (10) leaves $v(0, \theta) = a_0$, and (11) gives the first formula. For (13), which Powers calls "easy to show": for fixed $r < c$ the series (10) converges uniformly in $\theta$ (its terms are bounded by a constant times $(r/c)^n$), so it may be integrated term by term over $-\pi < \theta < \pi$. Every $\cos(n\theta)$ and $\sin(n\theta)$ with $n \ge 1$ integrates to $0$, so $\frac{1}{2\pi}\int_{-\pi}^{\pi}v(r, \theta)\,d\theta = a_0 = v(0, \theta)$.
>
> **(b)** Part (a) concerns the function given by the series. The maximum principle needs the property for an arbitrary harmonic function, about an arbitrary point. (Powers takes this step for granted; here is a proof in the spirit of the section.) Put the origin of polar coordinates at $P$, write $u(r, \theta)$, and let
>
> $$
> A(r) = \frac{1}{2\pi}\int_{-\pi}^{\pi}u(r, \theta)\,d\theta, \qquad 0 < r \le \rho ,
> $$
>
> the constant term of the Fourier series of $u(r, \cdot)$. Since $u$ has continuous second derivatives on the closed disk, we may differentiate under the integral sign. By the polar form of $\nabla^2u = 0$ ([[§35 Potential Equation#^thm-35-3|Theorem §35.3]]), $\frac{\partial}{\partial r}(ru_r) = -\frac1ru_{\theta\theta}$, so
>
> $$
> \frac{d}{dr}\big(rA'(r)\big) = \frac{1}{2\pi}\int_{-\pi}^{\pi}\frac{\partial}{\partial r}\big(ru_r\big)\,d\theta = -\frac{1}{2\pi r}\int_{-\pi}^{\pi}u_{\theta\theta}\,d\theta = -\frac{1}{2\pi r}\Big[u_\theta\Big]_{\theta = -\pi}^{\theta = \pi} = 0 ,
> $$
>
> by periodicity. Hence $rA'(r) = \kappa$ is constant. As $r \to 0^+$, $rA'(r) = \frac{1}{2\pi}\int_{-\pi}^{\pi}r\,u_r\,d\theta \to 0$, because $u_r = u_x\cos\theta + u_y\sin\theta$ stays bounded near $P$; so $\kappa = 0$ and $A$ is constant. Finally $A(r) \to u(P)$ as $r \to 0^+$, by continuity of $u$ at $P$. So $A(\rho) = u(P)$, which is the claim. (This is the same computation as for the $n = 0$ term in Theorem §39.2: the average $A(r)$ solves $\frac1r(rA')' = 0$, so $A = \alpha + \beta\ln r$, and boundedness kills $\ln r$.)
>
> Multiplying the circle averages by $2\pi r$ and integrating from $0$ to $\rho$ gives the version in lecture 11.7: $u(P)$ is also the average of $u$ over the disk of radius $\rho$, $u(P) = \frac{1}{\pi\rho^2}\iint u\,dA$.

^pf-39-4

*Uses:* [[§39 Potential in a Disk#^thm-39-2|§39.2]], [[§35 Potential Equation#^thm-35-3|§35.3]], [[§25 More on Uniform Convergence#^thm-25-3|451 Thm. §25.3]], [[§25 More on Uniform Convergence#^thm-25-1|451 Thm. §25.1]]

> [!remark]- Connections
> - The mean value property in $\mathbb{R}^n$, from Green's second identity with the fundamental solution: [[§17 The Divergence Theorem in Higher Dimensions and Green's Identities#^ex-17-3|452 Ex. §17.3]] (given there as a sketch; the proof of (b) above is a complete two-dimensional version).
> - Complex-variables version: [[§59 Maximum Modulus Principle#^thm-59-1|342 Thm. §59.1]] (Gauss's mean value theorem for analytic functions; its real part is (b) for $u = \operatorname{Re} f$) and [[§135★ Dirichlet Problem for a Disk#^cor-135-2|342 Cor. §135.2]]; a worked case is [[§123★ Examples (Electrostatic Potential)#^ex-123-4|342 Ex. §123.4]] (the value $\frac34$ on the axis of a cylinder, as the mean of the boundary values).

This characteristic of solutions of the potential equation is called the **mean value property**. From it, it is just a step to the maximum principle stated in [[§35 Potential Equation|§35]]: the mean value of a function lies between its minimum and maximum, and cannot equal either unless the function is constant.

> [!theorem] Theorem §39.5: Maximum Principle
> Let $R$ be a bounded, connected open region, and let $u$ be harmonic in $R$ and continuous on $R$ together with its boundary. If $u$ attains its maximum (or its minimum) over $R$ and its boundary at a point inside $R$, then $u$ is constant. Consequently the maximum and the minimum of $u$ are attained on the boundary of $R$.
>
> *Powers: 4.1 (text) and 4.5 (text)*

^thm-39-5

> [!proof]+ Proof
> Powers says the maximum principle is "just a step" from the mean value property; here is the step. The closure of $R$ is closed and bounded and $u$ is continuous there, so $u$ attains a maximum value $M$. Suppose $u(P) = M$ at some $P$ inside $R$.
>
> **$u = M$ near $P$.** Let $\rho > 0$ be so small that the closed disk of radius $\rho$ about $P$ lies in $R$, and let $0 < s \le \rho$. By Theorem §39.4(b), $M = u(P)$ is the average of $u$ over the circle of radius $s$ about $P$. On that circle $u \le M$. If $u(Q) < M$ at some point $Q$ of the circle, then by continuity $u < M - \varepsilon$ on an arc of positive length around $Q$, and the average would be less than $M$. So $u = M$ on every such circle, that is, on the whole disk of radius $\rho$ about $P$.
>
> **$u = M$ everywhere.** Let $S = \{Q \in R : u(Q) = M\}$. The previous step, applied at each point of $S$, shows that $S$ is open. It is also closed in $R$, since $u$ is continuous. $S$ is not empty and $R$ is connected, so $S = R$: $u \equiv M$ in $R$.
>
> For the minimum, apply this to $-u$, which is also harmonic. If $u$ is not constant, neither extreme value is attained inside $R$, so both are attained on the boundary; if $u$ is constant, they are attained everywhere.

^pf-39-5

*Uses:* [[§39a The Poisson Integral Formula and the Mean Value Property#^thm-39-4|§39.4]], [[§96 Maximum and Minimum Values#^thm-96-3|Calc Thm. §96.3]] (extreme value theorem), [[§13 Connected Spaces#^def-13-new1|590 Def. §13.1]] (connectedness)

> [!remark]- Connections
> - Complex-variables version: [[§59 Maximum Modulus Principle#^thm-59-3|342 Thm. §59.3]] (the maximum modulus principle) and [[§59 Maximum Modulus Principle#^cor-59-5|342 Cor. §59.5]] (the real part of a nonconstant analytic function takes its maximum only on the boundary, the case $u = \operatorname{Re} f$ of this theorem).

> [!theorem] Corollary §39.6: Uniqueness for Dirichlet's Problem
> Suppose that $u$ and $v$ are two solutions of the potential equation in a bounded region $R$ (continuous up to the boundary) that have the same values on the boundary of $R$. Then $u$ and $v$ are identical.
>
> *Powers: 4.5 (text)*

^cor-39-6

> [!proof]+ Proof
> Their difference $w = u - v$ is also a solution of the potential equation in $R$ (the equation is linear and homogeneous), and it has value $0$ all along the boundary of $R$. By the maximum principle, the maximum and minimum values of $w$ are attained on the boundary, so both are $0$. Therefore $w$ is identically $0$ throughout $R$; in other words, $u$ and $v$ are identical. (The maximum principle was proved for connected $R$. If $R$ is not connected, apply it on each connected component $R_i$: $R_i$ is a bounded connected open set, and its boundary lies in the boundary of $R$, because a point of $R$ lies in some open component, which is either $R_i$ itself or disjoint from it; so $w = 0$ on the boundary of $R_i$ as well.)

^pf-39-6

*Uses:* [[§39a The Poisson Integral Formula and the Mean Value Property#^thm-39-5|§39.5]]

> [!remark]- Connections
> - A second proof, by the energy method: Green's first identity with $u = v = w$ gives $\iint|\nabla w|^2 = 0$, [[§17 The Divergence Theorem in Higher Dimensions and Green's Identities#^ex-17-1|452 Ex. §17.1]]. It needs $w$ to have continuous first derivatives up to the boundary, while the maximum principle needs only continuity.

So the series solutions of [[§36 Potential in a Rectangle|§36]]–[[§38 Potential in Unbounded Regions|§38]] and of [[§39 Potential in a Disk|§39]] are *the* solutions of their Dirichlet problems, and a solution found by any other means (a harmonic polynomial, a closed form) must agree with them.
