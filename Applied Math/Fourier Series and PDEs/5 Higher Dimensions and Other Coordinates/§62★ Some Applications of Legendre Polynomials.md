---
type: section
subject: "[[Fourier Series and PDEs]]"
chapter: 5
section: "62★"
powers: "5.10"
aliases: ["Powers 5.10"]
tags: [fourier-series-and-pdes, math341, extension]
---
← [[§61★ Legendre Series and Zonal Harmonics]] · ↑ [[· 5 Higher Dimensions and Other Coordinates]] · [[§63★ Insulated Disk, Cooled Plate and Step Function]] →

*Powers, Section 5.10.*
★ *Beyond MAT 341: the course did not cover this section; it is included from Powers.*

This section puts the Legendre polynomials of [[§60★ Spherical Coordinates; Legendre Polynomials|§49]] to work on three axially symmetric problems. Inside a sphere, the potential equation separates into Legendre's equation and a Cauchy–Euler equation, and the solution is a series $\sum b_n\rho^nP_n(\cos\phi)$ whose coefficients come from the Legendre series of the boundary values. On a thin spherical shell the heat equation becomes one-dimensional in the colatitude $\phi$, and each zonal harmonic decays like $e^{-n(n+1)kt/R^2}$. For waves in a sphere the radial factors are Bessel functions of order $n + \frac12$, the spherical Bessel functions, and the nodal surfaces are spheres and cones. Physically: the electrostatic potential (or steady temperature) inside a sphere with given surface values, heat diffusion over a spherical surface, and the acoustic modes of a spherical cavity.

## A. Potential in a Sphere

We consider the axially symmetric potential equation, with no variation in the longitudinal ($\theta$) direction. The unknown $u$ might be an electrostatic potential or a steady-state temperature.

$$
\frac{1}{\rho^2}\bigg\{\frac{\partial}{\partial\rho}\Big(\rho^2\frac{\partial u}{\partial\rho}\Big) + \frac{1}{\sin\phi}\frac{\partial}{\partial\phi}\Big(\sin\phi\,\frac{\partial u}{\partial\phi}\Big)\bigg\} = 0, \quad 0 < \rho < c, \quad 0 < \phi < \pi, \qquad (1) \qquad\qquad u(c, \phi) = f(\phi), \quad 0 < \phi < \pi . \qquad (2)
$$

Of course $u$ is to be bounded at the singular points $\phi = 0$, $\phi = \pi$ and $\rho = 0$. The product form $u(\rho, \phi) = \Phi(\phi)R(\rho)$ separates (1) into

$$
(\rho^2R')' - \mu^2R = 0, \quad 0 < \rho < c, \qquad (3) \qquad\qquad (\sin\phi\,\Phi')' + \mu^2\sin\phi\,\Phi = 0, \quad 0 < \phi < \pi . \qquad (4)
$$

> [!theorem] Proposition §62.1: Potential in a Sphere
> If $f$ is sectionally smooth on $0 < \phi < \pi$, the solution of (1), (2) that is bounded in $0 \le \rho < c$, $0 \le \phi \le \pi$ is
>
> $$
> u(\rho, \phi) = \sum_{n=0}^{\infty} b_n\rho^nP_n(\cos\phi), \qquad (5)
> $$
>
> with
>
> $$
> b_n = \frac{2n+1}{2c^n}\int_0^{\pi} f(\phi)P_n(\cos\phi)\sin\phi\,d\phi . \qquad (7)
> $$
>
> *Powers: 5.10, Part A, Equations (5)–(7)*

^prop-62-1

> [!proof]+ Proof
> **Angular factor.** By [[§61★ Legendre Series and Zonal Harmonics#^thm-61-5|Theorem §61.5]], (4) with boundedness at $\phi = 0$ and $\pi$ has the eigenfunctions $\Phi_n(\phi) = P_n(\cos\phi)$ with $\mu_n^2 = n(n+1)$.
>
> **Radial factor.** With $\mu^2 = n(n+1)$, (3) becomes
>
> $$
> \rho^2R_n'' + 2\rho R_n' - n(n+1)R_n = 0, \quad 0 < \rho < c, \qquad R_n \text{ bounded at } \rho = 0 .
> $$
>
> This is a Cauchy–Euler equation ([[§2★ Variable Coefficients and Higher-Order Equations#^thm-2-1|Theorem §2.1]]). Trying $R = \rho^{\alpha}$ gives $\alpha(\alpha - 1) + 2\alpha - n(n+1) = (\alpha - n)(\alpha + n + 1) = 0$, so the solutions are $\rho^n$ and $\rho^{-(n+1)}$. The second is unbounded at $\rho = 0$. Hence $R_n = \rho^n$, and the product solutions are $u_n(\rho, \phi) = \rho^nP_n(\cos\phi)$.
>
> **The boundary condition.** The general bounded solution is the combination (5). At $\rho = c$ it must satisfy
>
> $$
> u(c, \phi) = \sum_{n=0}^{\infty} b_nc^nP_n(\cos\phi) = f(\phi), \qquad 0 < \phi < \pi . \qquad (6)
> $$
>
> With $x = \cos\phi$ this is the Legendre series of $F(x) = f(\arccos x)$ on $-1 < x < 1$ ([[§61★ Legendre Series and Zonal Harmonics#^def-61-1|Definition §61.1]]), so $b_nc^n = \frac{2n+1}{2}\int_{-1}^{1} F(x)P_n(x)\,dx$. Changing back to $\phi$, with $dx = -\sin\phi\,d\phi$, gives (7). By [[§61★ Legendre Series and Zonal Harmonics#^thm-61-1|Theorem §61.1]] the series (6) converges to $f$ at its points of continuity.

^pf-62-1

*Uses:* [[§61★ Legendre Series and Zonal Harmonics#^thm-61-5|§61.5]], [[§2★ Variable Coefficients and Higher-Order Equations#^thm-2-1|§2.1]], [[§61★ Legendre Series and Zonal Harmonics#^def-61-1|Def. §61.1]], [[§61★ Legendre Series and Zonal Harmonics#^thm-61-1|§61.1]]

> [!remark]- Connections
> - The weight $\sin\phi$ in (7) comes from the area element of the sphere $\rho = c$, $dA = c^2\sin\phi\,d\phi\,d\theta$, the boundary part of $dV = \rho^2\sin\phi\,d\rho\,d\theta\,d\phi$ in [[§123 Triple Integrals in Spherical Coordinates#^thm-123-2|Calc Thm. §123.2]]. In particular $b_0 = \frac12\int_0^{\pi} f\sin\phi\,d\phi$, the value of $u$ at the center, is the average of the boundary values over the sphere.
> - The Laplacian in these coordinates: [[§33 The Laplacian in Spherical Coordinates#^thm-33-1|452 Thm. §33.1]].

> [!example] Example §62.1: Two Hemispheres at Opposite Potentials
> The upper half of a sphere of radius $c$ is held at potential $V$ and the lower half at $-V$:
>
> $$
> f(\phi) = \begin{cases} \phantom{-}V, & 0 < \phi < \pi/2, \\ -V, & \pi/2 < \phi < \pi. \end{cases}
> $$
>
> Find the potential inside.
>
> With $x = \cos\phi$, the northern hemisphere $0 < \phi < \pi/2$ is $0 < x < 1$, so $F(x) = f(\arccos x)$ is $V$ times the step function of [[§61★ Legendre Series and Zonal Harmonics#^ex-61-1|Example §61.1]]. Its Legendre coefficients, as computed there and in Part B below, are $0$ for even $n$ and $V\frac{2n+1}{n+1}P_{n-1}(0)$ for odd $n$; these are $b_nc^n$. So
>
> $$
> u(\rho, \phi) = V\bigg[\frac32\Big(\frac{\rho}{c}\Big)P_1(\cos\phi) - \frac78\Big(\frac{\rho}{c}\Big)^3P_3(\cos\phi) + \frac{11}{16}\Big(\frac{\rho}{c}\Big)^5P_5(\cos\phi) - \cdots\bigg] .
> $$
>
> Only odd powers of $\rho\cos\phi$ appear, so $u$ is odd in $z$ and vanishes on the equatorial plane. Near the center the first term dominates: $u \approx \frac{3V}{2c}\rho\cos\phi = \frac{3V}{2c}z$, so the field $-\nabla u$ there is uniform, of magnitude $3V/(2c)$, pointing from the positive toward the negative hemisphere. On the positive $z$-axis ($\phi = 0$, $P_n(1) = 1$) the series gives $u = 0.362V$, $0.658V$, $0.867V$ at $z = c/4$, $c/2$, $3c/4$.
>
> *Powers: 5.10, Part A, with the boundary data and coefficients of the Part B example*

^ex-62-1

![[m341-50-2.svg]]
*Equipotentials $u = \pm0.2V, \ldots, \pm0.8V$ of Example §62.1 in a plane through the axis (300 terms). The potential is $V$ on the upper hemisphere and $-V$ on the lower; the equatorial plane is the equipotential $u = 0$, and all equipotentials end at the equator, where the boundary values jump. Near the center they are nearly parallel and equally spaced, the uniform field of the first term.*

## B. Heat Equation on a Spherical Shell

The temperature on a spherical shell satisfies the three-dimensional heat equation. If initially there is no dependence on $\theta$, there never will be. If, moreover, the shell is thin (thickness much less than the average radius $R$), we may assume that the temperature does not vary in the radial direction. The heat equation then becomes one-dimensional:

$$
\frac{1}{\sin\phi}\frac{\partial}{\partial\phi}\Big(\sin\phi\,\frac{\partial u}{\partial\phi}\Big) = \frac{R^2}{k}\frac{\partial u}{\partial t}, \quad 0 < \phi < \pi, \quad 0 < t, \qquad (8) \qquad\qquad u(\phi, 0) = f(\phi), \quad 0 < \phi < \pi , \qquad (9)
$$

and naturally we require $u$ to be bounded at $\phi = 0$ and $\phi = \pi$. The product form $u(\phi, t) = \Phi(\phi)T(t)$ leads to

$$
\frac{(\sin\phi\,\Phi'(\phi))'}{\sin\phi\,\Phi(\phi)} = \frac{R^2T'(t)}{kT(t)} = -\mu^2 ,
$$

and thus to the eigenvalue problem of [[§61★ Legendre Series and Zonal Harmonics#^thm-61-5|Theorem §61.5]]: $\mu_n^2 = n(n+1)$, $\Phi_n(\phi) = P_n(\cos\phi)$, $n = 0, 1, 2, \ldots$. The other factor of a product solution must be $T_n(t) = \exp\big(-n(n+1)kt/R^2\big)$.

> [!theorem] Proposition §62.2: Heat Conduction on a Thin Spherical Shell
> If $f$ is sectionally smooth on $0 < \phi < \pi$, the solution of (8), (9) bounded at $\phi = 0$ and $\pi$ is
>
> $$
> u(\phi, t) = \sum_{n=0}^{\infty} b_nP_n(\cos\phi)\,e^{-n(n+1)kt/R^2}, \qquad b_n = \frac{2n+1}{2}\int_0^{\pi} P_n(\cos\phi)f(\phi)\sin\phi\,d\phi . \qquad (10)
> $$
>
> *Powers: 5.10, Part B, Equations (10)–(11)*

^prop-62-2

> [!proof]+ Proof
> Each product $P_n(\cos\phi)e^{-n(n+1)kt/R^2}$ satisfies (8) and the boundedness conditions, by the separation above, and so does a series of constant multiples of them. At $t = 0$ the initial condition takes the form of a Legendre series,
>
> $$
> \sum_{n=0}^{\infty} b_nP_n(\cos\phi) = f(\phi), \qquad 0 < \phi < \pi , \qquad (11)
> $$
>
> whose coefficients are found as in the proof of [[§62★ Some Applications of Legendre Polynomials#^prop-62-1|Proposition §62.1]] (with $c = 1$). If $f$ is sectionally smooth, the series (11) equals $f(\phi)$ (at points of continuity) by [[§61★ Legendre Series and Zonal Harmonics#^thm-61-1|Theorem §61.1]], and so $u$ satisfies the problem as posed.

^pf-62-2

*Uses:* [[§61★ Legendre Series and Zonal Harmonics#^thm-61-5|§61.5]], [[§62★ Some Applications of Legendre Polynomials#^prop-62-1|§62.1]], [[§61★ Legendre Series and Zonal Harmonics#^thm-61-1|§61.1]]

The term with $n = 0$ does not decay: $b_0 = \frac12\int_0^{\pi} f\sin\phi\,d\phi$ is the average initial temperature over the sphere, and $u \to b_0$ as $t \to \infty$. Nothing in (8) lets heat in or out of the shell, so the average stays constant while the variations die out, the slowest being $P_1(\cos\phi) = \cos\phi$ with rate $2k/R^2$.

> [!example] Example §62.2: Northern Hemisphere Warm, Southern Hemisphere Cold
> Solve (8), (9) when $f(\phi) = T_0$ in the northern hemisphere ($0 < \phi < \pi/2$) and $f(\phi) = -T_0$ in the southern ($\pi/2 < \phi < \pi$).
>
> With $x = \cos\phi$,
>
> $$
> b_n = \frac{2n+1}{2}\int_0^{\pi} f(\phi)P_n(\cos\phi)\sin\phi\,d\phi = \frac{2n+1}{2}\bigg[\int_{-1}^{1} f(\cos^{-1}(x))P_n(x)\,dx\bigg] = T_0\frac{2n+1}{n+1}P_{n-1}(0)
> $$
>
> for odd $n$, and $b_n = 0$ for even $n$: $f(\cos^{-1}(x))$ is $T_0$ times the step function of [[§61★ Legendre Series and Zonal Harmonics#^ex-61-1|Example §61.1]]. So
>
> $$
> u(\phi, t) = T_0\bigg[\frac32\cos\phi\,e^{-2kt/R^2} - \frac78P_3(\cos\phi)\,e^{-12kt/R^2} + \frac{11}{16}P_5(\cos\phi)\,e^{-30kt/R^2} - \cdots\bigg] .
> $$
>
> The average temperature is $b_0 = 0$ for all time. The higher terms die out quickly: already at $kt/R^2 = 1$ the exponential factor of the second term is $e^{-10} \approx 4.5 \times 10^{-5}$ times that of the first, and $u \approx \frac32T_0\cos\phi\,e^{-2kt/R^2}$; at the north pole this is $0.203T_0$ (the full series gives $0.2030T_0$ too).
>
> *Powers: 5.10, Part B, Example, Figure 15*

^ex-62-2

![[m341-50-1.svg]]
*The temperature $u(\phi, t)$ of Example §62.2 as a function of the colatitude $\phi$, at $kt/R^2 = 0.01$, $0.1$, $0.3$ and $1$, with the initial temperature (dashed). The jump at the equator is smoothed out at once; as time goes on the profile approaches $\frac32T_0e^{-2kt/R^2}\cos\phi$ and decays to the average temperature $0$.*

## C. Spherical Waves

In [[§59★ Some Applications of Bessel Functions#^prop-59-4|Proposition §59.4]] the wave equation in a sphere was solved when the initial conditions depend only on $\rho$. Now the variable $\phi$ is also present:

$$
\begin{aligned}
\frac{1}{\rho^2}\frac{\partial}{\partial\rho}\Big(\rho^2\frac{\partial u}{\partial\rho}\Big) + \frac{1}{\rho^2\sin\phi}\frac{\partial}{\partial\phi}\Big(\sin\phi\,\frac{\partial u}{\partial\phi}\Big) &= \frac{1}{c^2}\frac{\partial^2u}{\partial t^2}, && 0 < \rho < a, \quad 0 < \phi < \pi, \quad 0 < t, \\
u(a, \phi, t) &= 0, && 0 < \phi < \pi, \quad 0 < t, \\
u(\rho, \phi, 0) = f(\rho, \phi), \quad \frac{\partial u}{\partial t}(\rho, \phi, 0) &= g(\rho, \phi), && 0 < \rho < a, \quad 0 < \phi < \pi, && (12)
\end{aligned}
$$

and in addition $u$ must be bounded as $\rho \to 0$ and as $\phi \to 0$ and $\phi \to \pi$. Product solutions $u = R(\rho)\Phi(\phi)T(t)$ give

$$
\frac{1}{\rho^2}\bigg(\frac{(\rho^2R')'}{R} + \frac{(\sin\phi\,\Phi')'}{\sin\phi\,\Phi}\bigg) = \frac{T''}{c^2T} = -\lambda^2 , \qquad (13)
$$

so that $\frac{(\rho^2R')'}{R} + \frac{(\sin\phi\,\Phi')'}{\sin\phi\,\Phi} = -\lambda^2\rho^2$, and again the ratio containing $\Phi$ must be a constant, $-\mu^2$. The two problems are

$$
\big(\sin\phi\,\Phi'\big)' + \mu^2\sin\phi\,\Phi = 0, \quad 0 < \phi < \pi, \qquad \Phi \text{ bounded at } \phi = 0, \pi ;
$$

$$
(\rho^2R')' - \mu^2R + \lambda^2\rho^2R = 0, \quad 0 < \rho < a, \qquad R(a) = 0, \qquad R \text{ bounded at } 0 .
$$

The first is solved by [[§61★ Legendre Series and Zonal Harmonics#^thm-61-5|Theorem §61.5]]: $\mu_n^2 = n(n+1)$, $\Phi_n(\phi) = P_n(\cos\phi)$.

> [!theorem] Proposition §62.3: Standing Waves in a Sphere
> For $n = 0, 1, 2, \ldots$, the bounded solutions of the radial equation with $\mu^2 = n(n+1)$ are the multiples of
>
> $$
> R_n(\rho) = \rho^{-1/2}J_{n+1/2}(\lambda\rho) ,
> $$
>
> and $R_n(a) = 0$ exactly when $\lambda = \lambda_{nm}$, where $\lambda_{nm}a$ is the $m$th positive solution of $J_{n+1/2}(\lambda a) = 0$. The product solutions of (12) without the initial conditions are
>
> $$
> \rho^{-1/2}J_{n+1/2}(\lambda_{nm}\rho)P_n(\cos\phi)\sin(\lambda_{nm}ct), \qquad \rho^{-1/2}J_{n+1/2}(\lambda_{nm}\rho)P_n(\cos\phi)\cos(\lambda_{nm}ct) .
> $$
>
> The frequencies of vibration of the sphere are $\lambda_{nm}c$ (radians per unit time).
>
> *Powers: 5.10, Part C*

^prop-62-3

> [!proof]+ Proof
> In standard form the radial equation is $R'' + \frac{2}{\rho}R' - \frac{\mu^2}{\rho^2}R + \lambda^2R = 0$, and by [[§59★ Some Applications of Bessel Functions#^ex-59-1|Example §59.1]](c), $\alpha = -\frac12$, $\gamma = 1$, $p = n + \frac12$ in [[§59★ Some Applications of Bessel Functions#^thm-59-1|Theorem §59.1]]. So the general solution is
>
> $$
> R_n(\rho) = \rho^{-1/2}\big[AJ_{n+1/2}(\lambda\rho) + BY_{n+1/2}(\lambda\rho)\big] .
> $$
>
> The Bessel functions of the second kind $Y_p(\lambda\rho)$ are unbounded at $\rho = 0$, so $B = 0$ and $R_n = \rho^{-1/2}J_{n+1/2}(\lambda\rho)$, which behaves like $\rho^n$ near $0$. (Powers asserts the unboundedness for every order; here is why it holds for $p = n + \frac12$. [[§55★ Bessel's Equation#^thm-55-4|Theorem §55.4]] proves it for integer order, and its argument for $\mu > 0$ goes through unchanged for $\mu = n + \frac12$ once $\mu!$ in the series for $J_\mu$ is replaced by $\Gamma(\mu + 1)$. Then, as in the proof of [[§55★ Bessel's Equation#^thm-55-5|Theorem §55.5]], a solution with $B \ne 0$ is unbounded.) (For $n = 0$ this is $\sqrt{2/(\pi\lambda)}\sin(\lambda\rho)/\rho$, the solution of [[§59★ Some Applications of Bessel Functions#^prop-59-4|Proposition §59.4]].) The boundary condition $R_n(a) = 0$ requires $J_{n+1/2}(\lambda a) = 0$. Finally $T'' + \lambda_{nm}^2c^2T = 0$ gives the sine and cosine of $\lambda_{nm}ct$.

^pf-62-3

*Uses:* [[§59★ Some Applications of Bessel Functions#^ex-59-1|Ex. §59.1]], [[§59★ Some Applications of Bessel Functions#^thm-59-1|§59.1]], [[§61★ Legendre Series and Zonal Harmonics#^thm-61-5|§61.5]], [[§55★ Bessel's Equation#^thm-55-4|§55.4]], [[§55★ Bessel's Equation#^thm-55-5|§55.5]]

The solution $u(\rho, \phi, t)$ is an infinite series of constant multiples of these functions; Powers does not write it out. The radial functions occur so often that they have their own name.

> [!definition] Definition §62.1: Spherical Bessel Functions
> The **spherical Bessel functions of the first kind** of order $n$ are
>
> $$
> j_n(z) = \sqrt{\frac{\pi}{2z}}\,J_{n+1/2}(z), \qquad n = 0, 1, 2, \ldots .
> $$
>
> Like $J_{1/2}$ ([[§59★ Some Applications of Bessel Functions|§48]], Part B), they are elementary:
>
> $$
> j_0(z) = \frac{\sin z}{z}, \qquad j_1(z) = \frac{\sin z - z\cos z}{z^2}, \qquad j_2(z) = \frac{(3 - z^2)\sin z - 3z\cos z}{z^3} .
> $$
>
> So the radial factor of Proposition §62.3 is a constant multiple of $j_n(\lambda\rho)$, and $R_n(a) = 0$ means $j_n(\lambda a) = 0$.
>
> *Powers: 5.10, Part C (text)*

^def-62-1

Powers lists $j_0$, $j_1$, $j_2$ without derivation. Each can be checked by substituting $R = j_n(\lambda\rho)$ into $R'' + \frac{2}{\rho}R' + \big(\lambda^2 - \frac{n(n+1)}{\rho^2}\big)R = 0$; for $j_0$ this is the computation of [[§59★ Some Applications of Bessel Functions#^prop-59-4|Proposition §59.4]].

> [!example] Example §62.3: The Lowest Frequencies of a Sphere
> Find the eigenvalues $\lambda_{nm}$ for $n = 0$ and $n = 1$.
>
> **$n = 0$.** $R_0(a) = 0$ comes down to $\sin(\lambda a)/(\lambda a) = 0$, so $\lambda_{0m} = m\pi/a$, $m = 1, 2, \ldots$, as in [[§59★ Some Applications of Bessel Functions#^prop-59-4|Proposition §59.4]]. Since $P_0(\cos\phi) = 1$, the product solutions with $n = 0$ are exactly the radial waves of [[§59★ Some Applications of Bessel Functions#^prop-59-4|Proposition §59.4]].
>
> **$n = 1$.** For other $n$ the solutions of $J_{n+1/2}(\lambda a) = 0$ must be found numerically. For $n = 1$, $j_1(\lambda a) = 0$ is the equation
>
> $$
> \sin(\lambda a) - \lambda a\cos(\lambda a) = 0, \qquad\text{that is,}\qquad \tan(\lambda a) = \lambda a ,
> $$
>
> with solutions $\lambda a = 4.493$, $7.725$, $10.904, \ldots$ (recomputed numerically). The corresponding modes $j_1(\lambda_{1m}\rho)\cos\phi$ change sign across the equatorial plane.
>
> In order, the lowest frequencies are $\lambda_{01}c = 3.142c/a$ ($n = 0$), $\lambda_{11}c = 4.493c/a$ ($n = 1$), $\lambda_{21}c = 5.763c/a$ ($n = 2$, the first zero of $j_2$), and $\lambda_{02}c = 6.283c/a$ ($n = 0$).
>
> *Powers: 5.10, Part C (text)*

^ex-62-3

> [!definition] Definition §62.2: Nodal Surfaces
> The **nodal surfaces** of a product solution, the points where it is $0$ for all time, are the solutions of
>
> $$
> J_{n+1/2}(\lambda_{nm}\rho)\,P_n(\cos\phi) = 0 .
> $$
>
> One or the other factor must be $0$, so these surfaces are either concentric spheres $\rho =$ const, determined by $J_{n+1/2}(\lambda_{nm}\rho) = 0$ (there are $m - 1$ of them inside the sphere), or cones $\phi =$ const, determined by $P_n(\cos\phi) = 0$ (the $n$ nodal parallels of the zonal harmonic, [[§61★ Legendre Series and Zonal Harmonics#^def-61-2|Definition §61.2]]; for $P_1$ the "cone" is the plane $z = 0$). This is the three-dimensional analogue of the nodal circles and diameters of a drum, [[§58★ Vibrations of a Circular Membrane#^def-58-3|Definition §58.3]].
>
> *Powers: 5.10, Part C (text)*

^def-62-2
