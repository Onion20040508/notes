---
type: section
subject: "[[Fourier Series and PDEs]]"
chapter: 5
section: "59★"
powers: "5.8"
aliases: ["Powers 5.8"]
tags: [fourier-series-and-pdes, math341, extension]
---
← [[§58★ Vibrations of a Circular Membrane]] · ↑ [[· 5 Higher Dimensions and Other Coordinates]] · [[§60★ Spherical Coordinates; Legendre Polynomials]] →

*Powers, Section 5.8.*
★ *Beyond MAT 341: the course did not cover this section; it is included from Powers.*

After the elementary functions, the Bessel functions are among the most useful in engineering and physics, partly because a whole family of differential equations reduces to Bessel's equation by a change of variables. This section states that family and works three problems with the separation details kept short: the steady-state temperature (or potential) in a cylinder with insulated side, where the radial condition $R'(a) = 0$ brings in the zeros of $J_1$ and the eigenvalue $0$; radial waves in a sphere, where Bessel functions of order $\frac12$ turn out to be elementary; and the pressure in a lubricated bearing, a regular Sturm–Liouville problem whose eigenvalues come from a determinant of Bessel functions. Physically: steady heat flow in a cylinder, the radial acoustic modes of a spherical cavity, and lubrication.

## A Family of Bessel Equations

> [!theorem] Theorem §59.1: Equations Solved by Bessel Functions
> The general solution of
>
> $$
> \phi'' + \frac{1 - 2\alpha}{x}\phi' + \bigg[\big(\lambda\gamma x^{\gamma-1}\big)^2 - \frac{p^2\gamma^2 - \alpha^2}{x^2}\bigg]\phi = 0 \qquad (1)
> $$
>
> is
>
> $$
> \phi(x) = x^{\alpha}\big[AJ_p(\lambda x^{\gamma}) + BY_p(\lambda x^{\gamma})\big] .
> $$
>
> *Powers: 5.8, Equation (1)*

^thm-59-1

*Powers omits the proof.* The remark below shows where the formula comes from.

> [!remark]- Remark: Why It Works
> Two substitutions turn (1) into Bessel's equation of order $p$.
> 1. **Remove the power $x^{\alpha}$.** Put $\phi = x^{\alpha}\psi$. Then $\phi' = x^{\alpha}\big(\psi' + \frac{\alpha}{x}\psi\big)$ and $\phi'' = x^{\alpha}\big(\psi'' + \frac{2\alpha}{x}\psi' + \frac{\alpha(\alpha-1)}{x^2}\psi\big)$, so
>
>    $$
>    \phi'' + \frac{1 - 2\alpha}{x}\phi' = x^{\alpha}\Big(\psi'' + \frac{1}{x}\psi' - \frac{\alpha^2}{x^2}\psi\Big) .
>    $$
>
>    The $-\alpha^2/x^2$ cancels the $+\alpha^2/x^2$ in the bracket of (1), and (1) becomes $\psi'' + \frac{1}{x}\psi' + \big[(\lambda\gamma x^{\gamma-1})^2 - \frac{p^2\gamma^2}{x^2}\big]\psi = 0$, or, multiplied by $x^2$,
>
>    $$
>    \Big(x\frac{d}{dx}\Big)^2\psi + \gamma^2\big(\lambda^2x^{2\gamma} - p^2\big)\psi = 0 ,
>    $$
>
>    since $x^2\psi'' + x\psi' = x\frac{d}{dx}\big(x\frac{d\psi}{dx}\big)$.
> 2. **Change the independent variable** to $s = \lambda x^{\gamma}$. Then $x\frac{d}{dx} = \gamma s\frac{d}{ds}$, and the equation becomes $\gamma^2\big[(s\frac{d}{ds})^2\psi + (s^2 - p^2)\psi\big] = 0$, that is, $s^2\psi'' + s\psi' + (s^2 - p^2)\psi = 0$: Bessel's equation of order $p$ in the variable $s$ ([[§55★ Bessel's Equation#^def-55-1|Definition §55.1]], with $\lambda = 1$). Its general solution is $AJ_p(s) + BY_p(s)$ ([[§55★ Bessel's Equation#^thm-55-5|Theorem §55.5]]).
>
> Hence $\phi = x^{\alpha}\psi = x^{\alpha}\big[AJ_p(\lambda x^{\gamma}) + BY_p(\lambda x^{\gamma})\big]$. Bessel's equation itself is the case $\alpha = 0$, $\gamma = 1$, $p = \mu$.

^rem-59-1

> [!example] Example §59.1: Recognizing Bessel's Equation in Disguise
> Identify $\alpha$, $\gamma$, $p$ in (1) for the radial equations met below and in [[§62★ Some Applications of Legendre Polynomials|§50]].
>
> **(a)** $R'' + \frac{2}{\rho}R' + \lambda^2R = 0$ (radial waves in a sphere, Part B). Matching $\frac{1 - 2\alpha}{x} = \frac{2}{x}$ gives $\alpha = -\frac12$. The coefficient of $R$ is the constant $\lambda^2$, so $\gamma - 1 = 0$, $\gamma = 1$, and $p^2\gamma^2 - \alpha^2 = 0$ gives $p = \frac12$. So $R = \rho^{-1/2}\big[AJ_{1/2}(\lambda\rho) + BY_{1/2}(\lambda\rho)\big]$.
>
> **(b)** $X'' + \frac{3}{x}X' + \lambda^2X = 0$ (the bearing, Part C). Now $1 - 2\alpha = 3$, so $\alpha = -1$, again $\gamma = 1$, and $p^2 - 1 = 0$ gives $p = 1$: $X = x^{-1}\big[AJ_1(\lambda x) + BY_1(\lambda x)\big]$.
>
> **(c)** $R'' + \frac{2}{\rho}R' - \frac{\mu^2}{\rho^2}R + \lambda^2R = 0$ (spherical waves with angular dependence, [[§62★ Some Applications of Legendre Polynomials#^prop-62-3|Proposition §62.3]]). As in (a), $\alpha = -\frac12$, $\gamma = 1$, and now $p^2 - \frac14 = \mu^2$; with $\mu^2 = n(n+1)$ this is $p^2 = n^2 + n + \frac14 = \big(n + \frac12\big)^2$, so $p = n + \frac12$.
>
> *Powers: 5.8, Parts B and C; 5.10, Part C*

^ex-59-1

## A. Potential Equation in a Cylinder

The steady-state temperature in a circular cylinder with insulated side surface, when the boundary data do not depend on $\theta$, satisfies

$$
\begin{aligned}
\frac{1}{r}\frac{\partial}{\partial r}\Big(r\frac{\partial u}{\partial r}\Big) + \frac{\partial^2u}{\partial z^2} &= 0, && 0 < r < a, \quad 0 < z < b, && (2)\\
\frac{\partial u}{\partial r}(a, z) &= 0, && 0 < z < b, && (3)\\
u(r, 0) &= f(r), && 0 < r < a, && (4)\\
u(r, b) &= g(r), && 0 < r < a. && (5)
\end{aligned}
$$

Here $u$ is independent of $\theta$, like the data. Assuming $u = R(r)Z(z)$ leads to

$$
(rR')' + \lambda^2rR = 0, \quad 0 < r < a, \quad (6) \qquad R'(a) = 0, \quad (7) \qquad |R(0)| \text{ bounded}, \quad (8) \qquad Z'' - \lambda^2Z = 0 . \quad (9)
$$

Condition (8) is added because $r = 0$ is a singular point.

> [!theorem] Proposition §59.2: The Radial Problem with Insulated Side
> Let $0 < \beta_1 < \beta_2 < \cdots$ be the positive zeros of $J_1$ ($\beta_1 = 3.832$, $\beta_2 = 7.016$, $\beta_3 = 10.173, \ldots$). The eigenvalue problem (6)–(8) has the eigenvalue $\lambda_0^2 = 0$ with eigenfunction $R_0 = 1$, and the eigenvalues
>
> $$
> \lambda_n^2 = \Big(\frac{\beta_n}{a}\Big)^2, \qquad R_n(r) = J_0(\lambda_n r), \qquad n = 1, 2, \ldots \qquad (10)
> $$
>
> The eigenfunctions are orthogonal with weight $r$ on $0 < r < a$, and
>
> $$
> \int_0^a J_0^2(\lambda_n r)\,r\,dr = \frac{a^2}{2}J_0^2(\beta_n), \qquad \int_0^a 1^2\,r\,dr = \frac{a^2}{2} .
> $$
>
> *Powers: 5.8, Equations (6)–(11) and the orthogonality relation after (12)*

^prop-59-2

> [!proof]+ Proof
> **Eigenvalues.** For $\lambda > 0$ the bounded solution of (6) is $R = J_0(\lambda r)$, as in [[§57★ Temperature in a Cylinder#^prop-57-1|Proposition §57.1]]. By [[§57★ Temperature in a Cylinder#^lem-57-5|Lemma §57.5]], $R'(a) = \lambda J_0'(\lambda a) = -\lambda J_1(\lambda a)$, so (7) holds exactly when $J_1(\lambda a) = 0$ (11): $\lambda a = \beta_n$. (Powers lists $0$ as the first eigenvalue; here is why.) For $\lambda = 0$, (6) is $(rR')' = 0$, with bounded solutions $R =$ constant, and these satisfy (7). Note $R_0(0) = J_0(0) = 1$, so $R_0 = 1$ is also "$J_0(0 \cdot r)$". A positive separation constant $+\mu^2$ gives the modified Bessel function $I_0(\mu r) = \sum_m (\mu r/2)^{2m}/(m!)^2$, a series of positive terms that is strictly increasing for $r > 0$ ([[§56★ Properties of Bessel Functions#^thm-56-5|Theorem §56.5]]); its derivative at $r = a$ is positive, so there are no other eigenvalues. (The same eigenvalue problem, Powers' Exercise 5.5.10, is [[§56★ Properties of Bessel Functions#^ex-56-2|Example §56.2]].)
>
> **Orthogonality.** The argument of [[§57★ Temperature in a Cylinder#^prop-57-2|Proposition §57.2]] applies verbatim: the boundary term $r(R_n'R_m - R_m'R_n)$ vanishes at $r = a$ because now $R_n'(a) = R_m'(a) = 0$, and at $r = 0$ because of the factor $r$. This includes $R_0 = 1$, so $\int_0^a J_0(\lambda_n r)\,r\,dr = 0$ for $n \ge 1$; directly, it equals $\frac{a}{\lambda_n}J_1(\beta_n) = 0$.
>
> **Norms.** (Powers leaves the coefficient formulas to Exercise 5.8.6; they need these norms.) Integrating $\frac{d}{dr}\big[(rR')^2\big] + \lambda^2r^2\frac{d}{dr}\big[R^2\big] = 0$ from $0$ to $a$ as in the proof of [[§57★ Temperature in a Cylinder#^prop-57-6|Proposition §57.6]] gives, in general,
>
> $$
> \int_0^a R^2\,r\,dr = \frac{a^2}{2}\Big(R^2(a) + \frac{R'^2(a)}{\lambda^2}\Big) ;
> $$
>
> with $R'(a) = 0$ and $R(a) = J_0(\beta_n)$ this is $\frac{a^2}{2}J_0^2(\beta_n)$.

^pf-59-2

*Uses:* [[§57★ Temperature in a Cylinder#^prop-57-1|§57.1]], [[§57★ Temperature in a Cylinder#^lem-57-5|§57.5]], [[§57★ Temperature in a Cylinder#^prop-57-2|§57.2]], [[§57★ Temperature in a Cylinder#^prop-57-6|§57.6]], [[§56★ Properties of Bessel Functions#^thm-56-5|§56.5]]

> [!theorem] Proposition §59.3: Potential in a Cylinder with Insulated Side
> The solution of (2)–(5) is
>
> $$
> u(r, z) = a_0 + b_0z + \sum_{n=1}^{\infty} J_0(\lambda_n r)\bigg[a_n\frac{\sinh(\lambda_n z)}{\sinh(\lambda_n b)} + b_n\frac{\sinh(\lambda_n(b - z))}{\sinh(\lambda_n b)}\bigg], \qquad \lambda_n = \frac{\beta_n}{a} , \qquad (12)
> $$
>
> with
>
> $$
> a_0 = \frac{2}{a^2}\int_0^a f(r)\,r\,dr, \qquad a_0 + b_0b = \frac{2}{a^2}\int_0^a g(r)\,r\,dr ,
> $$
>
> $$
> b_n = \frac{2}{a^2J_0^2(\beta_n)}\int_0^a f(r)J_0(\lambda_n r)\,r\,dr, \qquad a_n = \frac{2}{a^2J_0^2(\beta_n)}\int_0^a g(r)J_0(\lambda_n r)\,r\,dr .
> $$
>
> *Powers: 5.8, Equation (12); coefficients from Exercise 5.8.6*

^prop-59-3

> [!proof]+ Proof
> For $\lambda = 0$, (9) gives $Z = a_0 + b_0z$; for $\lambda = \lambda_n$, the solutions of $Z'' - \lambda_n^2Z = 0$ can be written as combinations of $\sinh(\lambda_n z)$ and $\sinh(\lambda_n(b - z))$, normalized to be $1$ at $z = b$, respectively $z = 0$. So each term of (12) satisfies (2), (3) and boundedness. At $z = 0$ and $z = b$ the series become
>
> $$
> u(r, 0) = a_0 + \sum_{n=1}^{\infty} b_nJ_0(\lambda_n r) = f(r), \qquad u(r, b) = (a_0 + b_0b) + \sum_{n=1}^{\infty} a_nJ_0(\lambda_n r) = g(r) .
> $$
>
> These are expansions in the orthogonal eigenfunctions $1, J_0(\lambda_1 r), J_0(\lambda_2 r), \ldots$ of [[§59★ Some Applications of Bessel Functions#^prop-59-2|Proposition §59.2]]. Multiplying by an eigenfunction times $r$ and integrating over $0 < r < a$ isolates one coefficient, and dividing by the norms of Proposition §59.2 gives the formulas.

^pf-59-3

*Uses:* [[§59★ Some Applications of Bessel Functions#^prop-59-2|§59.2]]

> [!remark]- Connections
> - Cylindrical coordinates $(r, \theta, z)$ and volume integrals in them: [[§122 Triple Integrals in Cylindrical Coordinates#^def-122-1|Calc Def. §122.1]]. The weight $r$ in the orthogonality relation is the factor $r$ in $dV = r\,dz\,dr\,d\theta$.

The constant term $a_0$ is the mean value of $f$ over the disk (the integral $\frac{2}{a^2}\int_0^a f\,r\,dr = \frac{1}{\pi a^2}\iint f\,dA$), and $b_0$ is the difference of the mean values on the two ends divided by $b$: with an insulated side, the net heat flux through every cross-section is the same, and it is carried by the term $b_0z$.

## B. Spherical Waves

In spherical coordinates $(\rho, \theta, \phi)$ ([[§60★ Spherical Coordinates; Legendre Polynomials#^def-60-1|Definition §60.1]]) the Laplacian is, by [[§60★ Spherical Coordinates; Legendre Polynomials#^prop-60-1|Proposition §60.1]],

$$
\nabla^2u = \frac{1}{\rho^2}\frac{\partial}{\partial\rho}\Big(\rho^2\frac{\partial u}{\partial\rho}\Big) + \frac{1}{\rho^2\sin\phi}\frac{\partial}{\partial\phi}\Big(\sin\phi\,\frac{\partial u}{\partial\phi}\Big) + \frac{1}{\rho^2\sin^2\phi}\frac{\partial^2u}{\partial\theta^2} .
$$

Consider a wave problem in a sphere when the initial conditions depend only on $\rho$:

$$
\begin{aligned}
\frac{1}{\rho^2}\frac{\partial}{\partial\rho}\Big(\rho^2\frac{\partial u}{\partial\rho}\Big) &= \frac{1}{c^2}\frac{\partial^2u}{\partial t^2}, && 0 < \rho < a, \quad 0 < t, && (13)\\
u(a, t) &= 0, && 0 < t, && (14)\\
u(\rho, 0) &= f(\rho), && 0 < \rho < a, && (15)\\
\frac{\partial u}{\partial t}(\rho, 0) &= g(\rho), && 0 < \rho < a. && (16)
\end{aligned}
$$

Separating $u(\rho, t) = R(\rho)T(t)$ gives

$$
T'' + \lambda^2c^2T = 0, \quad (17) \qquad (\rho^2R')' + \lambda^2\rho^2R = 0, \quad 0 < \rho < a, \quad (18) \qquad R(a) = 0, \quad (19) \qquad |R(0)| \text{ bounded}. \quad (20)
$$

Equation (18) is $R'' + \frac{2}{\rho}R' + \lambda^2R = 0$, and by [[§59★ Some Applications of Bessel Functions#^ex-59-1|Example §59.1]](a) its general solution is $R(\rho) = \rho^{-1/2}\big[AJ_{1/2}(\lambda\rho) + BY_{1/2}(\lambda\rho)\big]$. Near $\rho = 0$, $J_{1/2}(\lambda\rho) \sim \text{const} \times \rho^{1/2}$ and $Y_{1/2}(\lambda\rho) \sim \text{const} \times \rho^{-1/2}$, so (20) forces $B = 0$. The Bessel functions of order $\frac12$ are elementary:

$$
J_{1/2}(x) = \sqrt{\frac{2}{\pi}}\,\frac{\sin x}{\sqrt{x}}, \qquad Y_{1/2}(x) = -\sqrt{\frac{2}{\pi}}\,\frac{\cos x}{\sqrt{x}} .
$$

*Powers prints the constant factor in both formulas as $2/\pi$; it is $\sqrt{2/\pi}$. Only the shape $\sin(\lambda\rho)/\rho$ matters below.*

> [!theorem] Proposition §59.4: Radial Waves in a Sphere
> The eigenvalue problem (18)–(20) has the eigenvalues $\lambda_n^2 = (n\pi/a)^2$ and eigenfunctions
>
> $$
> R_n(\rho) = \frac{\sin(\lambda_n\rho)}{\rho}, \qquad n = 1, 2, \ldots , \qquad (21)
> $$
>
> which are orthogonal with weight $\rho^2$ on $0 < \rho < a$. The solution of (13)–(16) is
>
> $$
> u(\rho, t) = \sum_{n=1}^{\infty} \frac{\sin(\lambda_n\rho)}{\rho}\big[a_n\cos(\lambda_nct) + b_n\sin(\lambda_nct)\big] , \qquad (22)
> $$
>
> with
>
> $$
> a_n = \frac{2}{a}\int_0^a \rho f(\rho)\sin(\lambda_n\rho)\,d\rho, \qquad b_n = \frac{2}{\lambda_nca}\int_0^a \rho g(\rho)\sin(\lambda_n\rho)\,d\rho .
> $$
>
> *Powers: 5.8, Equations (21)–(22); coefficients from Exercise 5.8.7*

^prop-59-4

> [!proof]+ Proof
> **Eigenfunctions.** By the formula for $J_{1/2}$, the bounded solutions are multiples of $\rho^{-1/2}J_{1/2}(\lambda\rho) = \sqrt{2/(\pi\lambda)}\,\sin(\lambda\rho)/\rho$. (Powers asserts the formulas for $J_{1/2}$ and $Y_{1/2}$; here is a direct check that avoids them. By [[§6★ Singular Boundary Value Problems#^lem-6-2|Lemma §6.2]], $R = w/\rho$ satisfies (18) if and only if $w'' + \lambda^2w = 0$, so the general solution of (18) is $(A\sin\lambda\rho + B\cos\lambda\rho)/\rho$. The second term is unbounded at $\rho = 0$, while $\sin(\lambda\rho)/\rho \to \lambda$.) The condition (19), $\sin(\lambda a)/a = 0$, holds exactly when $\lambda a = n\pi$.
>
> **Orthogonality and coefficients.** With weight $\rho^2$,
>
> $$
> \int_0^a R_nR_m\,\rho^2\,d\rho = \int_0^a \sin(\lambda_n\rho)\sin(\lambda_m\rho)\,d\rho = \begin{cases} 0, & n \ne m, \\ a/2, & n = m, \end{cases}
> $$
>
> the orthogonality of the sine functions on $0 < \rho < a$. The initial conditions read $\sum a_n\sin(\lambda_n\rho)/\rho = f(\rho)$ and $\sum b_n\lambda_nc\sin(\lambda_n\rho)/\rho = g(\rho)$, that is, $\sum a_n\sin(n\pi\rho/a) = \rho f(\rho)$ and $\sum b_n\lambda_nc\sin(n\pi\rho/a) = \rho g(\rho)$. These are Fourier sine series ([[§11 Even and Odd Functions; Half-Range Expansions#^def-11-4|Definition §11.4]]), whose coefficients are the formulas stated. (Powers says only that the coefficients are chosen "as usual"; the details are Exercise 5.8.7.) Each term of (22) satisfies (13), (14) and boundedness by construction.

^pf-59-4

*Uses:* [[§59★ Some Applications of Bessel Functions#^ex-59-1|Ex. §59.1]], [[§6★ Singular Boundary Value Problems#^lem-6-2|§6.2]], [[§11 Even and Odd Functions; Half-Range Expansions#^def-11-4|Def. §11.4]] (Fourier sine series)

> [!remark] Remark: Spherical Waves Are Strings in Disguise
> The substitution in the proof says more: if $u(\rho, t)$ solves (13), then $w = \rho u$ solves the one-dimensional wave equation $w_{\rho\rho} = w_{tt}/c^2$, with $w(0, t) = 0$ and $w(a, t) = 0$, a vibrating string on $0 < \rho < a$ ([[§38 Solution of the Vibrating String Problem#^thm-38-2|Theorem §38.2]]). Hence every solution of (13) has the form $u = \frac{1}{\rho}\big(\psi_1(\rho + ct) + \psi_2(\rho - ct)\big)$, d'Alembert's form ([[§39 d'Alembert's Solution#^thm-39-2|Theorem §39.2]]) divided by $\rho$: spherical waves travel outward and inward with speed $c$ and amplitude decreasing like $1/\rho$ (Exercise 5.8.4). In particular the radial frequencies $n\pi c/a$ are harmonic, unlike those of the drum in [[§58★ Vibrations of a Circular Membrane#^ex-58-1|Example §58.1]].

^rem-59-2

## C. Pressure in a Bearing

The pressure in the lubricant inside a plane-pad bearing satisfies

$$
\begin{aligned}
\frac{\partial}{\partial x}\Big(x^3\frac{\partial p}{\partial x}\Big) + x^3\frac{\partial^2p}{\partial y^2} &= -1, && a < x < b, \quad -c < y < c, && (23)\\
p(a, y) = 0, \quad p(b, y) &= 0, && -c < y < c, && (24)\\
p(x, -c) = 0, \quad p(x, c) &= 0, && a < x < b, && (25)
\end{aligned}
$$

where $a$ and $c$ are positive constants and $b = a + 1$. Equation (23) is elliptic and nonhomogeneous.

> [!example] Example §59.2: Pressure in a Plane-Pad Bearing
> Solve (23)–(25), and find the first eigenvalues when $b/a = 2.5$.
>
> **Remove the source.** Let $p(x, y) = v(x) + u(x, y)$, where $v$ satisfies
>
> $$
> (x^3v')' = -1, \quad a < x < b, \qquad v(a) = 0, \quad v(b) = 0 . \qquad (26), (27)
> $$
>
> (Powers leaves $v$ to Exercise 5.8.9; here it is.) Integrating, $x^3v' = -x + C_1$, so $v' = -x^{-2} + C_1x^{-3}$ and $v = x^{-1} - \frac{C_1}{2}x^{-2} + C_2$. The two boundary conditions give $\frac{1}{a} - \frac{1}{b} = \frac{C_1}{2}\big(\frac{1}{a^2} - \frac{1}{b^2}\big)$, so $\frac{C_1}{2} = \frac{ab}{a + b}$, and then $C_2 = -\frac{1}{a + b}$. Hence
>
> $$
> v(x) = \frac{1}{x} - \frac{ab}{(a + b)x^2} - \frac{1}{a + b} = \frac{(x - a)(b - x)}{(a + b)x^2} .
> $$
>
> Then $u$ must solve the homogeneous problem
>
> $$
> \frac{\partial}{\partial x}\Big(x^3\frac{\partial u}{\partial x}\Big) + x^3\frac{\partial^2u}{\partial y^2} = 0, \qquad u(a, y) = 0, \quad u(b, y) = 0, \qquad u(x, \pm c) = -v(x) . \qquad (28)\text{–}(30)
> $$
>
> **Separate.** With $u = X(x)Y(y)$, $(x^3X')'/(x^3X) = -Y''/Y = -\lambda^2$, and
>
> $$
> (x^3X')' + \lambda^2x^3X = 0, \quad a < x < b, \qquad X(a) = 0, \quad X(b) = 0, \qquad Y'' - \lambda^2Y = 0 . \qquad (31)\text{–}(33)
> $$
>
> This is a regular Sturm–Liouville problem ([[§29 Sturm–Liouville Problems#^def-29-1|Definition §29.1]]) with $s(x) = p(x) = x^3 > 0$ on $a \le x \le b$; there is no singular point, so no boundedness condition is needed.
>
> **Solve the eigenvalue problem.** Equation (31) is $X'' + \frac{3}{x}X' + \lambda^2X = 0$, so by [[§59★ Some Applications of Bessel Functions#^ex-59-1|Example §59.1]](b), $X = \frac{1}{x}\big(AJ_1(\lambda x) + BY_1(\lambda x)\big)$. The boundary conditions (32) become
>
> $$
> AJ_1(\lambda a) + BY_1(\lambda a) = 0, \qquad AJ_1(\lambda b) + BY_1(\lambda b) = 0 .
> $$
>
> Not both $A$ and $B$ may be zero, so the determinant must vanish:
>
> $$
> J_1(\lambda a)Y_1(\lambda b) - J_1(\lambda b)Y_1(\lambda a) = 0 .
> $$
>
> For $b/a = 2.5$ (so $a = \frac23$, $b = \frac53$) the first three roots are $\lambda a = 2.156$, $4.223$, $6.307$ (recomputed numerically), so the first eigenvalues are
>
> $$
> \lambda_1^2 = \Big(\frac{2.156}{a}\Big)^2, \qquad \lambda_2^2 = \Big(\frac{4.223}{a}\Big)^2, \qquad \lambda_3^2 = \Big(\frac{6.307}{a}\Big)^2 .
> $$
>
> The eigenfunctions can be taken as
>
> $$
> X_n(x) = \frac{1}{x}\big(Y_1(\lambda_n a)J_1(\lambda_n x) - J_1(\lambda_n a)Y_1(\lambda_n x)\big) , \qquad (34)
> $$
>
> which vanish at $x = a$ by construction and at $x = b$ by the determinant condition.
>
> **Assemble.** The $y$-factor must be even in $y$, because the data at $y = \pm c$ are the same; so $Y_n = \cosh(\lambda_n y)$, and
>
> $$
> u(x, y) = \sum_{n=1}^{\infty} a_nX_n(x)\frac{\cosh(\lambda_n y)}{\cosh(\lambda_n c)} . \qquad (35)
> $$
>
> At $y = \pm c$ this is $\sum a_nX_n(x) = -v(x)$. By the orthogonality of the eigenfunctions of a regular Sturm–Liouville problem with weight $x^3$ ([[§29 Sturm–Liouville Problems#^thm-29-2|Theorem §29.2]]),
>
> $$
> \int_a^b X_n(x)X_m(x)\,x^3\,dx = 0, \quad n \ne m, \qquad\text{so}\qquad a_n = -\frac{\int_a^b v(x)X_n(x)\,x^3\,dx}{\int_a^b X_n^2(x)\,x^3\,dx} ,
> $$
>
> and the pressure is $p(x, y) = v(x) + u(x, y)$.
>
> *Powers: 5.8, Part C, Equations (23)–(35)*

^ex-59-2

> [!example] Example §59.3: Spherical Waves by d'Alembert's Method
> Find functions $\psi_1$, $\psi_2$ such that $u(\rho, t) = \frac{1}{\rho}\big(\psi_1(\rho + ct) + \psi_2(\rho - ct)\big)$ satisfies (13)–(16) and is bounded at $\rho = 0$. (Powers calls the two functions $\phi$ and $\psi$; here $\phi$ is the polar angle.)
>
> **Reduce to a string.** By [[§59★ Some Applications of Bessel Functions#^rem-59-2|Remark: Spherical Waves Are Strings in Disguise]], $w = \rho u = \psi_1(\rho + ct) + \psi_2(\rho - ct)$ solves $w_{\rho\rho} = w_{tt}/c^2$, and every such $u$ solves (13). The conditions on $u$ become conditions on $w$: $w(a, t) = 0$ by (14); $w(0, t) = 0$, because $u$ is bounded at $\rho = 0$; and, for $0 < \rho < a$,
>
> $$
> w(\rho, 0) = F(\rho) := \rho f(\rho), \qquad w_t(\rho, 0) = G(\rho) := \rho g(\rho) .
> $$
>
> **Initial conditions.** They read $\psi_1(\rho) + \psi_2(\rho) = F(\rho)$ and $c\big(\psi_1'(\rho) - \psi_2'(\rho)\big) = G(\rho)$ on $0 < \rho < a$. Integrating the second, $\psi_1 - \psi_2 = \frac{1}{c}H$ with $H(\rho) = \int_0^{\rho} G(s)\,ds$; a constant of integration may be dropped, because adding $K$ to $\psi_1$ and subtracting it from $\psi_2$ does not change $u$. Hence, on $0 < \rho < a$,
>
> $$
> \psi_1 = \tfrac12F + \tfrac{1}{2c}H, \qquad \psi_2 = \tfrac12F - \tfrac{1}{2c}H .
> $$
>
> **Boundary conditions.** For $t > 0$ the arguments $\rho \pm ct$ leave $(0, a)$, so $\psi_1$ and $\psi_2$ are needed on the whole line. The conditions $w(0, t) = 0$ and $w(a, t) = 0$ say that, for all $s > 0$,
>
> $$
> \psi_2(-s) = -\psi_1(s), \qquad \psi_1(a + s) = -\psi_2(a - s) .
> $$
>
> Both hold if $F$ and $G$ are replaced in the formulas above by their odd periodic extensions $\tilde F$, $\tilde G$ of period $2a$ ([[§11 Even and Odd Functions; Half-Range Expansions#^def-11-2|Definition §11.2]]) and $H(s) = \int_0^s \tilde G$. Indeed, $H$ is even because $\tilde G$ is odd, and $H$ has period $2a$ because the integral of the odd function $\tilde G$ over a period is $0$. Hence
>
> $$
> \psi_2(-s) = -\tfrac12\tilde F(s) - \tfrac{1}{2c}H(s) = -\psi_1(s), \qquad \psi_1(a + s) = -\tfrac12\tilde F(a - s) + \tfrac{1}{2c}H(a - s) = -\psi_2(a - s) ,
> $$
>
> using $\tilde F(a + s) = \tilde F(s - a) = -\tilde F(a - s)$ and $H(a + s) = H(s - a) = H(a - s)$.
>
> **The solution.**
>
> $$
> u(\rho, t) = \frac{1}{2\rho}\Big[\tilde F(\rho + ct) + \tilde F(\rho - ct)\Big] + \frac{1}{2c\rho}\int_{\rho - ct}^{\rho + ct} \tilde G(s)\,ds ,
> $$
>
> which is d'Alembert's solution of the string problem for $w$ ([[§39 d'Alembert's Solution#^thm-39-3|Theorem §39.3]]) divided by $\rho$. It is bounded at the center: since $\tilde F$ is odd and $H$ even, as $\rho \to 0$,
>
> $$
> \frac{\tilde F(ct + \rho) - \tilde F(ct - \rho)}{2\rho} \to \tilde F'(ct), \qquad \frac{H(ct + \rho) - H(ct - \rho)}{2c\rho} \to \frac{1}{c}\tilde G(ct) ,
> $$
>
> so $u(0, t) = \tilde F'(ct) + \tilde G(ct)/c$ wherever $\tilde F$ is differentiable and $\tilde G$ continuous.
>
> **What it says.** With $g = 0$, half of $w$ travels inward and half outward. The inward half is focused: $u = w/\rho$ grows as it approaches the center, and after passing through the center it travels outward with its sign reversed (the odd extension). At the wall both halves are reflected with a change of sign, as for the string.
>
> **A check.** Take $a = c = 1$, $f(\rho) = 1 - \rho^2$, $g = 0$. Then $F(s) = s - s^3$ is already odd, $\tilde F$ is its $2$-periodic continuation, and $u(\rho, t) = \frac{1}{2\rho}\big[\tilde F(\rho + t) + \tilde F(\rho - t)\big]$. For example, $u(0.5, 0.3) = F(0.8) + F(0.2) = 0.288 + 0.192 = 0.48$, $u(0, 0.3) = F'(0.3) = 1 - 3(0.3)^2 = 0.73$, and $u(0.2, 0.9) = \frac{1}{0.4}\big[F(1.1) + F(-0.7)\big] = \frac{1}{0.4}\big[{-0.171} - 0.357\big] = -1.32$, where $F(1.1) = F(-0.9) = -0.171$. The series of [[§59★ Some Applications of Bessel Functions#^prop-59-4|Proposition §59.4]], with $a_n = 2\int_0^1 \rho(1 - \rho^2)\sin(n\pi\rho)\,d\rho = \dfrac{12(-1)^{n+1}}{n^3\pi^3}$ and $b_n = 0$, gives the same three values.
>
> *Powers: Exercise 5.8.5*

^ex-59-3
