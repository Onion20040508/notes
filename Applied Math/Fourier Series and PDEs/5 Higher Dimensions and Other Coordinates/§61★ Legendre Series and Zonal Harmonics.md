---
type: section
subject: "[[Fourier Series and PDEs]]"
chapter: 5
section: "61★"
powers: "5.9"
aliases: ["Powers 5.9 (cont.)"]
tags: [fourier-series-and-pdes, math341, extension]
---
← [[§60★ Spherical Coordinates; Legendre Polynomials]] · ↑ [[· 5 Higher Dimensions and Other Coordinates]] · [[§62★ Some Applications of Legendre Polynomials]] →

*Powers, Section 5.9.*
★ *Beyond MAT 341: the course did not cover this section; it is included from Powers.*

This section develops the Legendre series of a function on $-1 < x < 1$ and their convergence, so that the Legendre polynomials $P_n$ of [[§60★ Spherical Coordinates; Legendre Polynomials|§60★]] can be used like sines and cosines. Physically, $P_n(\cos\phi)$ are the zonal harmonics: the angular parts of axially symmetric potentials, temperatures and waves in and around spheres (electrostatics, gravitation, heat conduction, acoustics, and quantum mechanics in a central field).

## Legendre Series

To use Legendre polynomials in boundary value problems, a given function $f(x)$ must be expressed in the form $f(x) = \sum_{n=0}^{\infty} b_nP_n(x)$, $-1 < x < 1$. Multiplying by $P_m$ and integrating, orthogonality and the norm (6) leave $\int_{-1}^{1} fP_m\,dx = b_m\frac{2}{2m+1}$.

> [!definition] Definition §61.1: Legendre Series
> The **Legendre series** of a function $f$ on $-1 < x < 1$ is
>
> $$
> \sum_{n=0}^{\infty} b_nP_n(x), \qquad b_n = \frac{2n+1}{2}\int_{-1}^{1} f(x)P_n(x)\,dx . \qquad (10)
> $$
>
> *Powers: 5.9, Equation (10)*

^def-61-1

> [!theorem] Theorem §61.1: Convergence of Legendre Series
> If $f(x)$ is sectionally smooth on the interval $-1 < x < 1$, then at every point of that interval the Legendre series of $f$ converges, and
>
> $$
> \sum_{n=0}^{\infty} b_nP_n(x) = \frac{f(x+) + f(x-)}{2} .
> $$
>
> *Powers: 5.9, Theorem*

^thm-61-1

*Powers omits the proof.* It is the analogue of the Fourier convergence theorem, [[§12 Convergence of Fourier Series#^thm-12-1|Theorem §12.1]].

> [!remark]- Connections
> - [[§15★ Mean Error and Convergence in Mean#^def-15-2|Convergence in the mean]] (in $L^2[-1, 1]$) has a short proof from results in the vault. The normalized polynomials $\sqrt{(2n+1)/2}\,P_n$ are an orthonormal set (Propositions §60.5 and §49.8) whose span is all polynomials. Polynomials are dense in $C[-1, 1]$ for the maximum norm by Weierstrass's approximation theorem ([[§27 Weierstrass's Approximation Theorem (Not Covered)|451 §27]], a heading only: the theorem was not covered), and continuous functions are dense in $L^2[-1, 1]$ ([[§35 Lᵖ as a Banach Space#^thm-35-12|551 Thm. §35.12]](iii)). So the set is complete, hence an orthonormal basis with Parseval's equality: [[§24 Orthonormal Sets and Bases#^thm-24-8|556 Thm. §24.8]]. The pointwise statement of the theorem needs more.

> [!theorem] Proposition §61.2: Legendre Series of Odd, Even and Half-Range Functions
> If $f$ is odd on $-1 < x < 1$, only the odd-indexed coefficients $b_n$ can be nonzero; if $f$ is even, only the even-indexed ones. Consequently a function $f$ given on $0 < x < 1$ is represented there both by
>
> $$
> f(x) = \sum_{n\ \mathrm{even}} b_nP_n(x), \qquad b_n = (2n+1)\int_0^1 f(x)P_n(x)\,dx \quad (n \text{ even}), \qquad (11)
> $$
>
> $$
> f(x) = \sum_{n\ \mathrm{odd}} b_nP_n(x), \qquad b_n = (2n+1)\int_0^1 f(x)P_n(x)\,dx \quad (n \text{ odd}), \qquad (12)
> $$
>
> the series of its even and of its odd extension.
>
> *Powers: 5.9, Equations (11)–(12)*

^prop-61-2

> [!proof]+ Proof
> $P_n$ is even or odd with $n$ ([[§60★ Spherical Coordinates; Legendre Polynomials#^def-60-3|Definition §60.3]]). If $f$ is odd and $n$ is even, $fP_n$ is odd and its integral over $-1 < x < 1$ is $0$; similarly if $f$ is even and $n$ is odd. If $f$ and $P_n$ have the same parity, $fP_n$ is even, and $\int_{-1}^{1} fP_n = 2\int_0^1 fP_n$, which turns (10) into (11) or (12). Applied to the even or odd extension of $f$, [[§61★ Legendre Series and Zonal Harmonics#^thm-61-1|Theorem §61.1]] shows that each series represents $f$ on $0 < x < 1$.

^pf-61-2

*Uses:* [[§60★ Spherical Coordinates; Legendre Polynomials#^def-60-3|Def. §60.3]], [[§61★ Legendre Series and Zonal Harmonics#^def-61-1|Def. §61.1]], [[§61★ Legendre Series and Zonal Harmonics#^thm-61-1|§61.1]]

Because the $P_n$ are polynomials, the integral (10) for any specific coefficient can be done in closed form for many functions $f$. Getting $b_n$ as a function of $n$ is not so easy, but some elementary integrals follow from the differential equation $\big((1 - x^2)P_n'\big)' + n(n+1)P_n = 0$.

> [!theorem] Proposition §61.3: Integrals of Pₙ and xPₙ
> For $n \ne 0$, respectively $n \ne 1$,
>
> $$
> \int P_n(x)\,dx = \frac{-(1 - x^2)}{n(n+1)}P_n'(x), \qquad (13) \qquad\qquad \int xP_n(x)\,dx = \frac{1 - x^2}{(n+2)(n-1)}\big(P_n(x) - xP_n'(x)\big) . \qquad (14)
> $$
>
> *Powers: 5.9, Summary box, Equations (13)–(14)*

^prop-61-3

> [!proof]+ Proof
> **(13).** Separate the two terms of the differential equation and integrate:
>
> $$
> n(n+1)\int P_n\,dx = \int -\big((1 - x^2)P_n'\big)'\,dx = -(1 - x^2)P_n'(x) ,
> $$
>
> and divide by $n(n+1) \ne 0$.
>
> **(14).** Multiply the differential equation by $x$, separate terms and integrate by parts twice:
>
> $$
> \begin{aligned}
> n(n+1)\int xP_n\,dx &= \int -x\big((1 - x^2)P_n'\big)'\,dx = -x(1 - x^2)P_n' + \int (1 - x^2)P_n'\,dx \\
> &= -x(1 - x^2)P_n' + (1 - x^2)P_n - \int (-2x)P_n\,dx .
> \end{aligned}
> $$
>
> Move the last term to the left: $\big(n(n+1) - 2\big)\int xP_n\,dx = (1 - x^2)\big(P_n - xP_n'\big)$, and $n(n+1) - 2 = (n+2)(n-1)$, which is not $0$ for $n \ne 1$. (For $n = 1$ the integration is done directly.)

^pf-61-3

These formulas are useful if $P_n(x)$ and $P_n'(x)$ can be evaluated easily, and the recurrence relations do this, in particular at $x = 0$.

> [!theorem] Proposition §61.4: Values at the Origin
> $$
> P_n(0) = (-1)^{n/2}\frac{1 \cdot 3 \cdots (n-1)}{2 \cdot 4 \cdots n}, \quad n = 2, 4, 6, \ldots; \qquad P_n(0) = 0, \quad n = 1, 3, 5, \ldots ; \qquad (15)
> $$
>
> and $P_n'(0) = nP_{n-1}(0)$ (16). So $P_2(0) = -\frac12$, $P_4(0) = \frac{1 \cdot 3}{2 \cdot 4} = \frac38$, $P_6(0) = -\frac{1 \cdot 3 \cdot 5}{2 \cdot 4 \cdot 6} = -\frac{5}{16}$.
>
> *Powers: 5.9, Equations (15)–(16)*

^prop-61-4

> [!proof]+ Proof
> $P_n(0) = 0$ for odd $n$ because the odd-indexed Legendre polynomials are odd functions. For odd $n$, (9) at $x = 0$ gives $(n+1)P_{n+1}(0) + nP_{n-1}(0) = 0$, that is,
>
> $$
> P_{n+1}(0) = -\frac{n}{n+1}P_{n-1}(0) .
> $$
>
> Starting from $P_0(0) = 1$, successively $P_2(0) = -\frac12$, $P_4(0) = -\frac34P_2(0) = \frac{1 \cdot 3}{2 \cdot 4}$, $P_6(0) = -\frac56P_4(0) = -\frac{1 \cdot 3 \cdot 5}{2 \cdot 4 \cdot 6}$, and by induction (15): each step multiplies by $-\frac{n}{n+1}$ with $n$ odd. Formula (16) is part of [[§60★ Spherical Coordinates; Legendre Polynomials#^prop-60-7|Proposition §60.7]].

^pf-61-4

*Uses:* [[§60★ Spherical Coordinates; Legendre Polynomials#^prop-60-7|§60.7]]

> [!example] Example §61.1: The Legendre Series of a Step Function
> Find the Legendre series of
>
> $$
> f(x) = \begin{cases} -1, & -1 < x < 0, \\ \phantom{-}1, & 0 < x < 1. \end{cases}
> $$
>
> $f$ is odd, so only odd-indexed polynomials appear, and by (12), (13) and (16), for odd $n$,
>
> $$
> \begin{aligned}
> b_n &= (2n+1)\int_0^1 P_n(x)\,dx = -\frac{2n+1}{n(n+1)}\Big[(1 - x^2)P_n'(x)\Big]_0^1 = \frac{2n+1}{n(n+1)}P_n'(0) = \frac{2n+1}{n+1}P_{n-1}(0) \\
> &= (-1)^{(n-1)/2}\,\frac{1 \cdot 3 \cdot 5 \cdots (n-2)}{2 \cdot 4 \cdot 6 \cdots (n-1)}\cdot\frac{2n+1}{n+1} \qquad (n = 3, 5, 7, \ldots),
> \end{aligned}
> $$
>
> using (15) for the even index $n - 1$. Separately, $b_1 = 3\int_0^1 x\,dx = \frac32$ (the general formula also gives this, with $P_0(0) = 1$). So $b_3 = \frac74\cdot\big(-\frac12\big) = -\frac78$, $b_5 = \frac{11}{6}\cdot\frac38 = \frac{11}{16}$, $b_7 = -\frac{75}{128}$, $b_9 = \frac{133}{256}$, and because $f$ is sectionally smooth, by [[§61★ Legendre Series and Zonal Harmonics#^thm-61-1|Theorem §61.1]]
>
> $$
> f(x) = \frac32P_1(x) - \frac78P_3(x) + \frac{11}{16}P_5(x) - \cdots, \qquad -1 < x < 1,\ x \ne 0 ,
> $$
>
> and the series is $0$ at $x = 0$.
>
> *Powers: 5.9, Example*

^ex-61-1

> [!example] Example §61.2: The Legendre Series of |x|
> Find the Legendre series of $f(x) = |x|$, $-1 < x < 1$.
>
> $f$ is even, so by (11) $b_n = (2n+1)\int_0^1 xP_n(x)\,dx$ for even $n$. For $n = 0$, $b_0 = \int_0^1 x\,dx = \frac12$. For even $n \ge 2$, (14) gives
>
> $$
> \int_0^1 xP_n(x)\,dx = \bigg[\frac{(1 - x^2)\big(P_n - xP_n'\big)}{(n+2)(n-1)}\bigg]_0^1 = -\frac{P_n(0)}{(n+2)(n-1)}, \qquad b_n = -\frac{(2n+1)P_n(0)}{(n+2)(n-1)} .
> $$
>
> With (15): $b_2 = -\frac{5 \cdot (-1/2)}{4 \cdot 1} = \frac58$, $b_4 = -\frac{9 \cdot (3/8)}{6 \cdot 3} = -\frac{3}{16}$, $b_6 = -\frac{13 \cdot (-5/16)}{8 \cdot 5} = \frac{13}{128}$. So
>
> $$
> |x| = \frac12 + \frac58P_2(x) - \frac{3}{16}P_4(x) + \frac{13}{128}P_6(x) - \cdots, \qquad -1 < x < 1 .
> $$
>
> $|x|$ is continuous, with a corner at $0$, and the convergence is much faster than for the step function: the partial sum through $P_6$ is within $0.086$ of $|x|$ everywhere on $-1 \le x \le 1$, the worst place being the corner $x = 0$.
>
> *Powers: 5.9, Figure 13(b) (Exercise 5.9.11)*

^ex-61-2

![[m341-49-2.svg]]
*Partial sums of Legendre series, computed from Examples §61.1 and §49.3. (a) The step function and its partial sum through $P_9$: it oscillates about $\pm1$, with the largest errors near the jump and near the endpoints, as a Fourier series does. (b) $|x|$ and its partial sum through $P_6$, already close except near the corner at $x = 0$.*

*Chain: the triangle wave earlier in [[§21 Sawtooth, Triangle Wave, Parabola, Rectified Sine, Sinc Function and Rectangular Pulse#The Triangle Wave|Chapter 1]] (its Fourier series).*

## Zonal Harmonics

> [!theorem] Theorem §61.5: The Legendre Eigenvalue Problems
> The solutions of the eigenvalue problem
>
> $$
> \big((1 - x^2)y'\big)' + \mu^2y = 0, \quad -1 < x < 1, \qquad y(x) \text{ bounded at } x = -1 \text{ and at } x = 1 ,
> $$
>
> are $y(x) = P_n(x)$, $\mu_n^2 = n(n+1)$, $n = 0, 1, 2, \ldots$. The solutions of the eigenvalue problem
>
> $$
> \big(\sin\phi\,\Phi'\big)' + \mu^2\sin\phi\,\Phi = 0, \quad 0 < \phi < \pi, \qquad \Phi(\phi) \text{ bounded at } \phi = 0 \text{ and at } \phi = \pi ,
> $$
>
> are $\Phi(\phi) = P_n(\cos\phi)$, $\mu_n^2 = n(n+1)$, $n = 0, 1, 2, \ldots$. The eigenfunctions $\Phi_n$ are orthogonal with weight $\sin\phi$: $\int_0^{\pi}\Phi_n(\phi)\Phi_m(\phi)\sin\phi\,d\phi = 0$ for $n \ne m$.
>
> *Powers: 5.9, Summary box; Exercise 5.9.6*

^thm-61-5

> [!proof]+ Proof
> The first statement is [[§60★ Spherical Coordinates; Legendre Polynomials#^thm-60-4|Theorem §60.4]] with the normalization of [[§60★ Spherical Coordinates; Legendre Polynomials#^def-60-3|Definition §60.3]]; it rests on the unboundedness assumed in part (b) of that theorem, which Powers does not prove. The second follows by the change of variables $x = \cos\phi$ of [[§60★ Spherical Coordinates; Legendre Polynomials#^prop-60-2|Proposition §60.2]]. For the orthogonality, the same substitution, with $dx = -\sin\phi\,d\phi$, gives
>
> $$
> \int_0^{\pi} P_n(\cos\phi)P_m(\cos\phi)\sin\phi\,d\phi = \int_{-1}^{1} P_n(x)P_m(x)\,dx = 0 \qquad (n \ne m)
> $$
>
> by [[§60★ Spherical Coordinates; Legendre Polynomials#^prop-60-5|Proposition §60.5]].

^pf-61-5

*Uses:* [[§60★ Spherical Coordinates; Legendre Polynomials#^thm-60-4|§60.4]], [[§60★ Spherical Coordinates; Legendre Polynomials#^def-60-3|Def. §60.3]], [[§60★ Spherical Coordinates; Legendre Polynomials#^prop-60-2|§60.2]], [[§60★ Spherical Coordinates; Legendre Polynomials#^prop-60-5|§60.5]]

> [!definition] Definition §61.2: Zonal Harmonics
> The functions $P_n(\cos\phi)$ on the sphere are called **zonal harmonics**, because their nodal lines, the loci of $P_n(\cos\phi) = 0$, are parallels $\phi =$ const that divide the sphere into zones. $P_n(\cos\phi)$ has $n$ nodal parallels, at the colatitudes $\phi = \arccos x_k$ of the $n$ zeros $x_k$ of $P_n$, and the zones between them are alternately positive and negative.
>
> *Powers: 5.9 (text), Figure 14*

^def-61-2

For example, $P_1(\cos\phi) = \cos\phi$ has the equator as its only nodal line; $P_2(\cos\phi) = \frac12(3\cos^2\phi - 1)$ vanishes on the two parallels $\cos\phi = \pm1/\sqrt3$, $\phi \approx 54.7°$ and $125.3°$, so it is positive on two polar caps and negative on the equatorial belt.
