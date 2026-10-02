---
type: section
subject: "[[Complex Variables]]"
chapter: 3
section: 33
bc: "33"
aliases: ["B&C 33"]
tags: [complex-variables, math342]
---
← [[§32 Examples (The Logarithmic Function)]] · ↑ [[· 3 Elementary Functions]] · [[§34 Some Identities Involving Logarithms]] →

*Brown–Churchill, Section 33 · MAT 342 HW 4.*

The multiple-valued $\log z = \ln r + i\theta$ becomes an honest analytic function once $\theta$ is confined to an open interval $\alpha < \theta < \alpha + 2\pi$. The price is a ray, the branch cut $\theta = \alpha$, which is removed from the domain: across it the imaginary part jumps by $2\pi$. On the cut plane the branch is analytic with $\frac{d}{dz}\log z = \frac1z$, exactly as in calculus. The section introduces the general vocabulary of branches, branch cuts and branch points, which returns with every multiple-valued function: powers $z^c$ ([[§35 The Power Function#^def-35-1|Definition §35.1]]), inverse trigonometric functions ([[§40★ Inverse Trigonometric and Hyperbolic Functions#^def-40-1|Definition §40.1]]), and contour integrals along branch cuts ([[§46 Examples Involving Branch Cuts|§46]], [[§91★ Integration Along a Branch Cut|§91★]]).

## Branches of log z

If $z = re^{i\theta}$ is nonzero, the argument $\theta$ has any one of the values $\theta = \Theta + 2n\pi$ $(n = 0, \pm1, \pm2, \ldots)$, where $\Theta = \operatorname{Arg} z$. Hence [[§31 The Logarithmic Function#^def-31-1|Definition §31.1]] can be written

$$
\log z = \ln r + i\theta . \qquad (1)
$$

> [!definition] Definition §33.1: A Branch of the Logarithm
> Let $\alpha$ be any real number. Restricting $\theta$ in (1) to $\alpha < \theta < \alpha + 2\pi$ gives the function
>
> $$
> \log z = \ln r + i\theta \qquad (r > 0,\ \alpha < \theta < \alpha + 2\pi) , \qquad (2)
> $$
>
> with components
>
> $$
> u(r, \theta) = \ln r \qquad\text{and}\qquad v(r, \theta) = \theta . \qquad (3)
> $$
>
> It is single-valued on the domain $r > 0$, $\alpha < \theta < \alpha + 2\pi$: the plane with the origin and the ray $\theta = \alpha$ removed. With $\alpha = -\pi$ it is the restriction of $\operatorname{Log} z$ to $|z| > 0$, $-\pi < \operatorname{Arg} z < \pi$.
>
> *B&C: Sec. 33, Equations (2) and (3)*

^def-33-1

> [!theorem] Theorem §33.1: Each Branch of log z Is Analytic, with Derivative 1/z
> The function (2) is continuous and analytic throughout its domain $r > 0$, $\alpha < \theta < \alpha + 2\pi$, and
>
> $$
> \frac{d}{dz}\log z = \frac1z \qquad (|z| > 0,\ \alpha < \arg z < \alpha + 2\pi) . \qquad (4)
> $$
>
> In particular
>
> $$
> \frac{d}{dz}\operatorname{Log} z = \frac1z \qquad (|z| > 0,\ -\pi < \operatorname{Arg} z < \pi) . \qquad (5)
> $$
>
> If (2) were defined on the ray $\theta = \alpha$ as well (by $\theta = \alpha$ or by $\theta = \alpha + 2\pi$), it would not be continuous there.
>
> *B&C: Sec. 33, Equations (4) and (5)*

^thm-33-1

> [!proof]+ Proof
> **Continuity.** $u = \ln r = \ln|z|$ is continuous for $z \ne 0$. For $v = \theta$ (B&C asserts this; here is why): let $w = ze^{-i(\alpha + \pi)}$. If $z = re^{i\theta}$ with $\alpha < \theta < \alpha + 2\pi$, then $w = re^{i(\theta - \alpha - \pi)}$ with $-\pi < \theta - \alpha - \pi < \pi$, so $w$ is off the ray $(-\infty, 0]$ and $\theta - \alpha - \pi = \operatorname{Arg} w$. Off that ray,
>
> $$
> \operatorname{Arg} w = 2\tan^{-1}\frac{\operatorname{Im} w}{|w| + \operatorname{Re} w} ,
> $$
>
> since for $w = \rho e^{i\varphi}$, $-\pi < \varphi < \pi$, the quotient is $\sin\varphi/(1 + \cos\varphi) = \tan\frac\varphi2$ with $\frac\varphi2 \in (-\frac\pi2, \frac\pi2)$, and the denominator $|w| + \operatorname{Re} w$ vanishes only for real $w \le 0$. The right side is a continuous function of $w$, and $w$ is a continuous function of $z$; so $\theta = \alpha + \pi + \operatorname{Arg} w$ is continuous on the domain.
>
> **Analyticity and the derivative.** In the polar coordinates $(r, \theta)$, $r > 0$, $\alpha < \theta < \alpha + 2\pi$, the components (3) have the first-order partial derivatives
>
> $$
> u_r = \frac1r, \qquad u_\theta = 0, \qquad v_r = 0, \qquad v_\theta = 1 ,
> $$
>
> which exist and are continuous throughout the domain and satisfy the polar form of the Cauchy–Riemann equations
>
> $$
> ru_r = v_\theta, \qquad u_\theta = -rv_r
> $$
>
> at every point. By [[§24★ Polar Coordinates#^thm-24-3|Theorem §24.3]], the derivative exists at every point of the domain (so the function is analytic there) and equals
>
> $$
> \frac{d}{dz}\log z = e^{-i\theta}(u_r + iv_r) = e^{-i\theta}\Big(\frac1r + i0\Big) = \frac{1}{re^{i\theta}} = \frac1z .
> $$
>
> With $\alpha = -\pi$ this is (5).
>
> **No continuous extension to the ray.** Let $z_0 = r_0e^{i\alpha}$ be a point of the ray $\theta = \alpha$, $r_0 > 0$. The points $r_0e^{i(\alpha + \epsilon)}$ and $r_0e^{i(\alpha + 2\pi - \epsilon)}$, $0 < \epsilon < \pi$, both tend to $z_0$ as $\epsilon \to 0$, while the values of $v$ there, $\alpha + \epsilon$ and $\alpha + 2\pi - \epsilon$, tend to $\alpha$ and to $\alpha + 2\pi$. So no value of $v$ at $z_0$ makes $v$ continuous at $z_0$.

^pf-33-1

*Uses:* [[§33 Branches and Derivatives of Logarithms#^def-33-1|Def. §33.1]], [[§24★ Polar Coordinates#^thm-24-3|§24.3]], [[§18 Continuity#^thm-18-2|§18.2]]

![[m342-33-1.svg]]
*The branch (2) of $\log z$ lives on the plane cut along the ray $\theta = \alpha$ (red, dashed; the origin is removed too). Going once around the origin counterclockwise from the cut, $v = \theta$ increases continuously from $\alpha$ to $\alpha + 2\pi$. At a point of the cut (red dot) two nearby points (green) on opposite sides have values of $v$ near $\alpha$ and near $\alpha + 2\pi$: this jump of $2\pi$ is why the cut must be removed.*

> [!remark]- Connections
> - The derivative $1/z$ restricts on the positive real axis to $\frac{d}{dx}\ln x = \frac1x$, [[§19 Derivatives of Logarithmic and Inverse Trigonometric Functions#^cor-19-3|Calc Cor. §19.3]]. The real proof differentiates an inverse function; the same route works here, [[§33 Branches and Derivatives of Logarithms#^ex-33-3|Example §33.3]].
> - Topologically, $z \mapsto e^z$ is a covering map of $\mathbb{C}$ onto $\mathbb{C} \setminus \{0\}$: in polar form it is $x \mapsto e^x$ times the covering $\mathbb{R} \to S^1$, $y \mapsto e^{iy}$ (up to the factor $2\pi$), of [[§24 Covering Spaces#^thm-24-2|590 Thm. §24.2]]. A branch of $\log z$ is a continuous inverse of this covering over the cut plane. No continuous logarithm exists on a circle around $0$: it would lift the generating loop of $\pi_1(S^1) \cong \mathbb{Z}$ to a closed loop, [[§24 Covering Spaces#^thm-24-10|590 Thm. §24.10]]. This is why a cut is unavoidable.

## Branches, Branch Cuts, Branch Points

> [!definition] Definition §33.2: Branch of a Multiple-Valued Function; Principal Branch
> A **branch** of a multiple-valued function $f$ is any single-valued function $F$ that is analytic in some domain at each point $z$ of which the value $F(z)$ is one of the values of $f$. (The requirement of analyticity prevents $F$ from taking a random selection of the values of $f$.)
>
> For each fixed $\alpha$, the function (2) is a branch of the multiple-valued function (1). The function
>
> $$
> \operatorname{Log} z = \ln r + i\Theta \qquad (r > 0,\ -\pi < \Theta < \pi) \qquad (6)
> $$
>
> is called the **principal branch**.
>
> *B&C: Sec. 33 (text), Equation (6)*

^def-33-2

> [!definition] Definition §33.3: Branch Cut; Branch Point
> A **branch cut** is a portion of a line or curve that is introduced in order to define a branch $F$ of a multiple-valued function $f$. Points on the branch cut for $F$ are singular points ([[§25 Analytic Functions#^def-25-3|Definition §25.3]]) of $F$. Any point that is common to all branch cuts of $f$ is called a **branch point**.
>
> For the branch (2) of the logarithm, the branch cut is the origin together with the ray $\theta = \alpha$; for the principal branch (6) it is the origin together with the ray $\Theta = \pi$, the nonpositive real axis. The origin is a branch point of $\log z$.
>
> *B&C: Sec. 33 (text)*

^def-33-3

> [!remark] Remark: Method — Choosing a Branch
> To make $\log z$, or a function built from it, single-valued and analytic on a given region:
> 1. **Locate the trouble.** For $\log(g(z))$ the branch point is where $g(z) = 0$; the cut must keep $g(z)$ off one ray from $0$.
> 2. **Choose the ray to avoid the region of interest.** A branch with cut $\theta = \alpha$ is analytic wherever $g(z)$ avoids the ray $\arg = \alpha$. For example, the principal branch $\operatorname{Log} g(z)$ is analytic wherever $g(z)$ is analytic and not a real number $\le 0$.
> 3. **Fix the interval for $\theta$** ($\alpha < \theta < \alpha + 2\pi$), and compute every value with $\theta$ in that interval, never with $\operatorname{Arg}$ unless the interval is $(-\pi, \pi)$.
> 4. **Identities depend on the branch.** An identity such as $\log(z^2) = 2\log z$ may hold for one branch and fail for another (Example §33.1), because the right side may produce an angle outside the chosen interval.

^rem-33-1

## Examples

> [!example] Example §33.1: log(i²) = 2 log i Depends on the Branch
> We saw in [[§32 Examples (The Logarithmic Function)#^ex-32-4|Example §32.4]] that the *set* of values of $\log(i^2)$ is not the set of values of $2\log i$. For a specific branch there is only one value of each side, and equality can occur.
>
> **(a)** With the branch $\log z = \ln r + i\theta$ $\big(r > 0,\ \frac\pi4 < \theta < \frac{9\pi}{4}\big)$: $i^2 = -1 = e^{i\pi}$ with $\pi$ in the interval, so
>
> $$
> \log(i^2) = \log(-1) = \ln 1 + i\pi = \pi i ,
> $$
>
> and $i = e^{i\pi/2}$ with $\pi/2$ in the interval, so
>
> $$
> 2\log i = 2\Big(\ln 1 + i\frac\pi2\Big) = \pi i .
> $$
>
> Hence $\log(i^2) = 2\log i$ for this branch. $\qquad (7)$
>
> **(b)** With the branch $\log z = \ln r + i\theta$ $\big(r > 0,\ \frac{3\pi}{4} < \theta < \frac{11\pi}{4}\big)$: again $\pi$ is in the interval, so $\log(i^2) = \log(-1) = \pi i$. But now $\frac\pi2 < \frac{3\pi}{4}$ is not in the interval; the argument of $i$ that is, is $\frac\pi2 + 2\pi = \frac{5\pi}{2}$. So
>
> $$
> 2\log i = 2\Big(\ln 1 + i\frac{5\pi}{2}\Big) = 5\pi i \ne \pi i ,
> $$
>
> and $\log(i^2) \ne 2\log i$ for this branch.
>
> *B&C: Sec. 33, Example and Exercise 4; Source: 342 HW 4 (optional problems)*

^ex-33-1

> [!example] Example §33.2: The Branch with Cut Along the Positive Real Axis
> Consider the branch
>
> $$
> \log z = \ln r + i\theta \qquad (r > 0,\ 0 < \theta < 2\pi) ,
> $$
>
> whose branch cut is the origin and the positive real axis. Find $\log(-1 - i)$ and $\log(-1)$ for this branch.
>
> $-1 - i$ has modulus $\sqrt2$, and of its arguments $-\frac{3\pi}{4} + 2n\pi$ exactly one lies in $(0, 2\pi)$, namely $\frac{5\pi}{4}$. So
>
> $$
> \log(-1 - i) = \ln\sqrt2 + i\frac{5\pi}{4} = \frac12\ln 2 + \frac{5\pi}{4}i .
> $$
>
> Similarly $-1 = e^{i\pi}$ with $\pi \in (0, 2\pi)$, so $\log(-1) = \ln 1 + i\pi = \pi i$. A branch takes a single value at each point: here the answer is one number, not the list $\frac12\ln 2 + i\big(\frac{5\pi}{4} + 2n\pi\big)$. Compare $\operatorname{Log}(-1 - i) = \frac12\ln 2 - \frac{3\pi}{4}i$ ([[§32 Examples (The Logarithmic Function)#^ex-32-1|Example §32.1]]): the two branches differ by $2\pi i$ in the lower half plane and agree in the upper half plane, where $0 < \theta < \pi$ for both.
>
> *Source: 342 HW 4, Problem 1(b), second part*

^ex-33-2

> [!example] Example §33.3: The Derivative from e^(log z) = z
> Given that the branch (2) is analytic at each point of its domain (Theorem §33.1), its derivative also follows from the identity
>
> $$
> e^{\log z} = z \qquad (|z| > 0,\ \alpha < \arg z < \alpha + 2\pi)
> $$
>
> of [[§31 The Logarithmic Function#^prop-31-2|Proposition §31.2]]. Differentiate both sides, using the chain rule ([[§20 Rules for Differentiation#^thm-20-4|Theorem §20.4]]) and $\frac{d}{dw}e^w = e^w$ ([[§30 The Exponential Function#^thm-30-3|Theorem §30.3]]):
>
> $$
> e^{\log z}\,\frac{d}{dz}\log z = 1 , \qquad\text{so}\qquad \frac{d}{dz}\log z = \frac{1}{e^{\log z}} = \frac1z .
> $$
>
> This route needs analyticity of $\log z$ as an input; Theorem §33.1 supplies it.
>
> *B&C: Sec. 33, Exercise 6; Source: 342 HW 4 (optional problems)*

^ex-33-3

> [!example] Example §33.4: Where Is a Principal Logarithm Analytic?
> **(a)** $f(z) = \operatorname{Log}(z - i)$ is analytic everywhere except on the portion $x \le 0$ of the line $y = 1$. Indeed $\operatorname{Log} w$ is analytic except where $w$ is real and $w \le 0$ (Theorem §33.1 and the Method), and $w = z - i = x + i(y - 1)$ is real and $\le 0$ exactly when $y = 1$ and $x \le 0$. Elsewhere $f$ is a composition of analytic functions, analytic by the chain rule.
>
> **(b)** $f(z) = \dfrac{\operatorname{Log}(z + 4)}{z^2 + i}$ is analytic everywhere except at $\pm(1 - i)/\sqrt2$ and on the portion $x \le -4$ of the real axis. The numerator is analytic except where $z + 4$ is real and $\le 0$, that is, $y = 0$ and $x \le -4$. The denominator is entire and vanishes where $z^2 = -i = e^{-i\pi/2}$, that is, at the square roots $z = \pm e^{-i\pi/4} = \pm\frac{1 - i}{\sqrt2}$ ([[§10 Roots of Complex Numbers#^thm-10-2|Theorem §10.2]]). A quotient of analytic functions is analytic where the denominator is nonzero ([[§25 Analytic Functions#^prop-25-1|Proposition §25.1]]).
>
> *B&C: Sec. 33, Exercise 10*

^ex-33-4
