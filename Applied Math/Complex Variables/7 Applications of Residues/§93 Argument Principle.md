---
type: section
subject: "[[Complex Variables]]"
chapter: 7
section: 93
bc: "93"
aliases: ["B&C 93"]
tags: [complex-variables, math342]
---
← [[§92★ Definite Integrals Involving Sines and Cosines]] · ↑ [[· 7 Applications of Residues]] · [[§94 Rouché's Theorem]] →

*Brown–Churchill, Section 93 · MAT 342 HW 13, Practice Final (Spring 2012).*

The residue theorem also counts. If $f$ is analytic except for poles inside a simple closed contour $C$, and analytic and nonzero on $C$, then $f'/f$ has a simple pole with residue $m$ at each zero of order $m$ and residue $-m$ at each pole of order $m$, so $\frac{1}{2\pi i}\int_C f'/f\,dz$ is the number of zeros minus the number of poles inside $C$. The same integral measures how often the image curve $f(C)$ winds around the origin. The resulting **argument principle** locates zeros by looking only at the boundary: it is the basis of Rouché's theorem in §94, and of stability tests such as the Nyquist criterion in engineering.

## Winding Numbers

> [!definition] Definition §93.1: Meromorphic Function
> A function $f$ is **meromorphic** in a domain $D$ if it is analytic throughout $D$ except for poles.
>
> *B&C: Sec. 93 (text)*

^def-93-1

Suppose that $f$ is meromorphic in the domain interior to a positively oriented simple closed contour $C$, and analytic and nonzero on $C$ ("analytic on $C$" means analytic in an open set containing $C$). The image $\Gamma$ of $C$ under $w = f(z)$ is a closed contour, not necessarily simple, in the $w$ plane; as $z$ traverses $C$ in the positive direction, $w$ traverses $\Gamma$ in a direction that we take as the orientation of $\Gamma$. Since $f$ has no zeros on $C$, $\Gamma$ does not pass through $w = 0$.

> [!definition] Definition §93.2: Change of Argument; Winding Number
> Let $w_0$ and $w$ be points on $\Gamma$, $w_0$ fixed, and let $\phi_0$ be a value of $\arg w_0$. Let $\arg w$ vary continuously, starting with the value $\phi_0$, as $w$ begins at $w_0$ and traverses $\Gamma$ once in its direction of orientation. When $w$ returns to $w_0$, $\arg w$ has a particular value $\phi_1$ of $\arg w_0$. The number
>
> $$
> \Delta_C\arg f(z) = \phi_1 - \phi_0
> $$
>
> is the **change in argument** of $f(z)$ as $z$ describes $C$ once in the positive direction. It is an integral multiple of $2\pi$, and the integer
>
> $$
> \frac{1}{2\pi}\Delta_C\arg f(z)
> $$
>
> is the **winding number** of $\Gamma$ with respect to the origin $w = 0$: the number of times $w$ winds around the origin, positive for counterclockwise and negative for clockwise winding.
>
> *B&C: Sec. 93 (text)*

^def-93-2

B&C takes for granted that $\arg w$ can be made to vary continuously along $\Gamma$, and that the change does not depend on the choices made; the next lemma supplies both.

> [!theorem] Lemma §93.1: A Continuous Argument Along a Contour
> Let $w(t)$, $a \le t \le b$, be continuous and piecewise smooth (continuously differentiable except at finitely many points, with one-sided derivatives there), with $w(t) \ne 0$ for all $t$, and let $\phi_0$ be a value of $\arg w(a)$. Then
>
> $$
> \phi(t) = \phi_0 + \operatorname{Im}\int_a^t\frac{w'(\tau)}{w(\tau)}\,d\tau
> $$
>
> is continuous and piecewise smooth, $\phi(t)$ is a value of $\arg w(t)$ for every $t$, and $w(t) = \rho(t)e^{i\phi(t)}$ with $\rho(t) = |w(t)|$. Any other continuous function $\psi$ with $w(t) = \rho(t)e^{i\psi(t)}$ differs from $\phi$ by a constant multiple of $2\pi$. In particular, for $w(t) = f(z(t))$ with $z = z(t)$ a parametrization of $C$,
>
> $$
> \Delta_C\arg f(z) = \phi(b) - \phi(a) = \operatorname{Im}\int_C\frac{f'(z)}{f(z)}\,dz
> $$
>
> is well defined and does not depend on $\phi_0$ or on the starting point.
>
> *B&C: Sec. 93 (text), equations (2)–(3)*

^lem-93-1

> [!proof]+ Proof
> Let $h(t) = \int_a^t w'(\tau)/w(\tau)\,d\tau$. The integrand is piecewise continuous, so $h$ is continuous, and $h' = w'/w$ except at finitely many points. The function $g(t) = w(t)e^{-h(t)}$ is continuous, and away from those points
>
> $$
> g'(t) = w'(t)e^{-h(t)} - w(t)h'(t)e^{-h(t)} = 0 .
> $$
>
> So the real and imaginary parts of $g$ are constant on each subinterval (mean value theorem: [[§29 The Mean Value Theorem#^cor-29-4|451 Cor. §29.4]]), hence, by continuity, constant on $[a, b]$: $g(t) = g(a) = w(a)$. Therefore $w(t) = w(a)e^{h(t)}$. Writing $w(a) = \rho(a)e^{i\phi_0}$ and $h = \operatorname{Re}h + i\operatorname{Im}h$,
>
> $$
> w(t) = \rho(a)e^{\operatorname{Re}h(t)}\,e^{i(\phi_0 + \operatorname{Im}h(t))} = \rho(a)e^{\operatorname{Re}h(t)}\,e^{i\phi(t)} ,
> $$
>
> and taking moduli, $\rho(t) = \rho(a)e^{\operatorname{Re}h(t)}$; so $w(t) = \rho(t)e^{i\phi(t)}$, and $\phi$ is continuous and piecewise smooth.
>
> If also $w(t) = \rho(t)e^{i\psi(t)}$, then $e^{i(\phi(t) - \psi(t))} = 1$, so $\phi(t) - \psi(t)$ is a multiple of $2\pi$ for every $t$. A continuous function on an interval whose values lie in the discrete set $2\pi\mathbb{Z}$ is constant (by the intermediate value theorem, [[§18 Properties of Continuous Functions#^thm-18-3|451 Thm. §18.3]], it cannot jump between two of these values). So $\phi - \psi$ is constant, and $\phi(b) - \phi(a) = \psi(b) - \psi(a)$: the change of argument does not depend on the continuous choice.
>
> For $w(t) = f(z(t))$, the chain rule $\frac{d}{dt}f(z(t)) = f'(z(t))z'(t)$ ([[§43 Contours#^prop-43-5|Proposition §43.5]]) holds on each smooth arc, and $f'(z(t))z'(t)/f(z(t))$ is the integrand of $\int_C f'(z)/f(z)\,dz$ in the parametrization ([[§44 Contour Integrals#^def-44-1|Definition §44.1]]); so $\phi(b) - \phi(a) = \operatorname{Im}h(b) = \operatorname{Im}\int_C f'/f\,dz$. This contour integral does not depend on where the closed contour $C$ is started. Finally $w(b) = w(a)$, so $\phi(b)$ and $\phi(a)$ are two values of $\arg w(a)$, and the change is a multiple of $2\pi$.

^pf-93-1

*Uses:* [[§93 Argument Principle#^def-93-2|Def. §93.2]], [[§43 Contours#^prop-43-5|§43.5]], [[§44 Contour Integrals#^def-44-1|Def. §44.1]], [[§41 Derivatives of Functions w(t)#^prop-41-1|§41.1]], [[§42 Definite Integrals of Functions w(t)#^thm-42-2|§42.2]], [[§29 The Mean Value Theorem#^cor-29-4|451 Cor. §29.4]] (vanishing derivative), [[§18 Properties of Continuous Functions#^thm-18-3|451 Thm. §18.3]] (intermediate value theorem)

> [!remark]- Connections
> - In topology the continuous argument is a **lift** of the loop $w(t)/|w(t)|$ through the covering map $\mathbb{R} \to S^1$, $\phi \mapsto e^{i\phi}$: its existence and uniqueness up to $2\pi\mathbb{Z}$ is the path lifting lemma, [[§24 Covering Spaces#^lem-24-6|590 Lem. §24.6]], and the winding number is the class of the loop in $\pi_1(S^1) \cong \mathbb{Z}$, [[§24 Covering Spaces#^thm-24-10|590 Thm. §24.10]]. The formula of Lemma §93.1 constructs the lift explicitly for piecewise smooth loops.

> [!theorem] Proposition §93.2: Winding Number Zero Off a Ray
> In the notation above, suppose there is a ray from the origin $w = 0$ that does not intersect $\Gamma$. Then $\Delta_C\arg f(z) = 0$: the winding number of $\Gamma$ with respect to the origin is zero.
>
> *B&C: Sec. 94, Exercise 3; Source: 342 HW 13*

^prop-93-2

> [!proof]+ Proof
> Let the ray be $\arg w = \alpha$. Every $w$ on $\Gamma$ has exactly one argument $\Theta(w)$ in the open interval $\alpha < \Theta < \alpha + 2\pi$, and $\Theta$ is continuous on the plane cut along the ray: it is the imaginary part of the branch $\log w = \ln|w| + i\Theta$, $\alpha < \Theta < \alpha + 2\pi$, which is analytic there ([[§33 Branches and Derivatives of Logarithms#^thm-33-1|Theorem §33.1]]). So $\psi(t) = \Theta(w(t))$ is a continuous argument along $\Gamma$, and by Lemma §93.1
>
> $$
> \Delta_C\arg f(z) = \psi(b) - \psi(a) = \Theta(w(b)) - \Theta(w(a)) = 0 ,
> $$
>
> because $w(b) = w(a)$. (This is B&C's suggested argument in another form: a continuous argument confined to an interval of length $2\pi$ changes by less than $2\pi$ in absolute value, and a multiple of $2\pi$ smaller than $2\pi$ in absolute value is $0$.)

^pf-93-2

*Uses:* [[§93 Argument Principle#^lem-93-1|§93.1]], [[§93 Argument Principle#^def-93-2|Def. §93.2]], [[§33 Branches and Derivatives of Logarithms#^thm-33-1|§33.1]]

In particular, $\Delta_C\arg f(z) = 0$ when $\Gamma$ lies in an open half plane whose boundary passes through the origin, or in a disk not containing the origin.

## Counting Zeros and Poles

Count a zero of order $m_0$ as $m_0$ zeros and a pole of order $m_p$ as $m_p$ poles.

> [!theorem] Lemma §93.3: Finitely Many Zeros and Poles
> Let $f$ be meromorphic in the domain $D$ interior to a simple closed contour $C$, and analytic and nonzero on $C$. Then $f$ has only finitely many poles in $D$, and only finitely many zeros, each of finite order.
>
> *B&C: Sec. 83, Exercises 11 and 12; Sec. 94, Exercise 4*

^lem-93-3

> [!proof]+ Proof
> Let $\overline{D} = D \cup C$, a closed bounded set. Every point of $C$ has a disk around it in which $f$ is analytic and, by continuity, nonzero.
>
> **Poles.** Suppose there were infinitely many distinct poles. By the Bolzano–Weierstrass theorem, in the form of [[§82 Zeros of Analytic Functions#^ex-82-3|Example §82.3]], they have an accumulation point $z^{\ast}$ in $\overline{D}$. It is not on $C$, since near points of $C$ there are no poles. So $z^{\ast} \in D$, where $f$ is either analytic at $z^{\ast}$ (then analytic in a disk around it, which contains no pole) or has a pole at $z^{\ast}$ (an isolated singular point, so a punctured disk around it contains no pole). Either way some neighborhood of $z^{\ast}$ contains at most one pole, a contradiction.
>
> **$f$ is not identically zero.** Let $D_0$ be $D$ with the finitely many poles removed; it is open and connected (a polygonal path in $D$ can be rerouted around finitely many points). If $f \equiv 0$ in $D_0$, then by continuity $f = 0$ at the points of $C$, which are limits of points of $D_0$; but $f \ne 0$ on $C$.
>
> **Zeros have finite order.** If at a zero $z_0$ all derivatives of $f$ vanished, the Taylor series of $f$ at $z_0$ would be $0$, so $f \equiv 0$ in a disk around $z_0$, and then $f \equiv 0$ in the domain $D_0$ by [[§28★ Uniquely Determined Analytic Functions#^lem-28-1|Lemma §28.1]], which we have excluded.
>
> **Finitely many zeros.** Suppose there were infinitely many. They accumulate at some $z^{\ast} \in \overline{D}$. Not on $C$, since $f \ne 0$ near $C$. Not at a pole, since $|f(z)| \to \infty$ at a pole ([[§84 Behavior of Functions Near Isolated Singular Points#^thm-84-4|Theorem §84.4]]), so $f \ne 0$ near it. So $f$ is analytic at $z^{\ast}$, $f(z^{\ast}) = 0$ by continuity, and $z^{\ast}$ is a zero that is not isolated. But a zero of finite order is isolated ([[§82 Zeros of Analytic Functions#^thm-82-2|Theorem §82.2]]): a contradiction.

^pf-93-3

*Uses:* [[§93 Argument Principle#^def-93-1|Def. §93.1]], [[§82 Zeros of Analytic Functions#^thm-82-2|§82.2]], [[§84 Behavior of Functions Near Isolated Singular Points#^thm-84-4|§84.4]], [[§28★ Uniquely Determined Analytic Functions#^lem-28-1|§28.1]], [[§63 Proof of Taylor's Theorem#^thm-63-1|§63.1]], [[§82 Zeros of Analytic Functions#^ex-82-3|Ex. §82.3]] (Bolzano–Weierstrass)

> [!theorem] Theorem §93.4: Argument Principle
> Let $C$ denote a positively oriented simple closed contour, and suppose that
> - (a) a function $f(z)$ is meromorphic in the domain interior to $C$;
> - (b) $f(z)$ is analytic and nonzero on $C$;
> - (c) counting multiplicities, $Z$ is the number of zeros and $P$ the number of poles of $f(z)$ inside $C$.
>
> Then
>
> $$
> \int_C\frac{f'(z)}{f(z)}\,dz = 2\pi i(Z - P) \qquad\text{and}\qquad \frac{1}{2\pi}\Delta_C\arg f(z) = Z - P . \qquad (8)
> $$
>
> *B&C: Sec. 93, Theorem*

^thm-93-4

> [!proof]+ Proof
> The integral of $f'(z)/f(z)$ around $C$ is evaluated in two ways. ($Z$ and $P$ are finite by Lemma §93.3.)
>
> **By the change of argument.** Let $z = z(t)$ $(a \le t \le b)$ be a parametric representation of $C$, so that
>
> $$
> \int_C\frac{f'(z)}{f(z)}\,dz = \int_a^b\frac{f'[z(t)]z'(t)}{f[z(t)]}\,dt . \qquad (1)
> $$
>
> The image $\Gamma$ never passes through $w = 0$, so by Lemma §93.1 $f[z(t)] = \rho(t)e^{i\phi(t)}$ $(a \le t \le b)$ (2) with $\rho > 0$ and $\phi$ continuous and piecewise smooth, and along each smooth arc
>
> $$
> f'[z(t)]z'(t) = \frac{d}{dt}f[z(t)] = \frac{d}{dt}\big[\rho(t)e^{i\phi(t)}\big] = \rho'(t)e^{i\phi(t)} + i\rho(t)e^{i\phi(t)}\phi'(t) . \qquad (3)
> $$
>
> Since $\rho'$ and $\phi'$ are piecewise continuous, (2) and (3) give
>
> $$
> \int_C\frac{f'(z)}{f(z)}\,dz = \int_a^b\frac{\rho'(t)}{\rho(t)}\,dt + i\int_a^b\phi'(t)\,dt = \ln\rho(t)\Big|_a^b + i\phi(t)\Big|_a^b .
> $$
>
> But $\rho(b) = \rho(a)$ and $\phi(b) - \phi(a) = \Delta_C\arg f(z)$. Hence
>
> $$
> \int_C\frac{f'(z)}{f(z)}\,dz = i\Delta_C\arg f(z) . \qquad (4)
> $$
>
> **By residues.** $f'(z)/f(z)$ is analytic inside and on $C$ except at the points inside $C$ where the zeros and poles of $f$ occur. If $f$ has a zero of order $m_0$ at $z_0$, then ([[§82 Zeros of Analytic Functions#^thm-82-1|Theorem §82.1]])
>
> $$
> f(z) = (z - z_0)^{m_0}g(z), \qquad (5)
> $$
>
> where $g$ is analytic and nonzero at $z_0$. Hence $f'(z) = m_0(z - z_0)^{m_0 - 1}g(z) + (z - z_0)^{m_0}g'(z)$, or
>
> $$
> \frac{f'(z)}{f(z)} = \frac{m_0}{z - z_0} + \frac{g'(z)}{g(z)} . \qquad (6)
> $$
>
> Since $g'/g$ is analytic at $z_0$, it has a Taylor series representation about that point, and (6) shows that $f'/f$ has a simple pole at $z_0$ with residue $m_0$. If instead $f$ has a pole of order $m_p$ at $z_0$, then ([[§80 Residues at Poles#^thm-80-1|Theorem §80.1]])
>
> $$
> f(z) = (z - z_0)^{-m_p}\phi(z), \qquad (7)
> $$
>
> with $\phi$ analytic and nonzero at $z_0$. This has the form (5) with $m_0$ replaced by $-m_p$, so by (6) $f'/f$ has a simple pole at $z_0$ with residue $-m_p$. The residue theorem ([[§76 Cauchy's Residue Theorem#^thm-76-1|Theorem §76.1]]) now gives $\int_C f'/f\,dz = 2\pi i(Z - P)$, the first equation of (8).
>
> Equating the right sides of (4) and (8) gives $\frac{1}{2\pi}\Delta_C\arg f(z) = Z - P$.

^pf-93-4

*Uses:* [[§93 Argument Principle#^lem-93-1|§93.1]], [[§93 Argument Principle#^lem-93-3|§93.3]], [[§93 Argument Principle#^def-93-2|Def. §93.2]], [[§82 Zeros of Analytic Functions#^thm-82-1|§82.1]], [[§80 Residues at Poles#^thm-80-1|§80.1]], [[§76 Cauchy's Residue Theorem#^thm-76-1|§76.1]], [[§43 Contours#^prop-43-5|§43.5]]

> [!remark]- Connections
> - For polynomials, the argument principle is the analytic form of the winding-number proof of the fundamental theorem of algebra, [[§25 The Fundamental Theorem of Algebra#^thm-25-1|590 Thm. §25.1]], which counts how often the image of a large circle winds around $0$ by means of $\pi_1(S^1) \cong \mathbb{Z}$. B&C completes this route in [[§94 Rouché's Theorem#^ex-94-2|Example §94.2]].

> [!remark] Remark: Method — Using the Argument Principle
> - **Counting from the formula.** If the zeros and poles inside $C$ are known, $\Delta_C\arg f = 2\pi(Z - P)$ predicts how the image of $C$ winds around $0$ (Examples §93.1, §93.2).
> - **Counting from the picture.** If the image $\Gamma$ is known, count its signed crossings of a ray from the origin (counterclockwise crossings $+1$, clockwise $-1$); for $f$ analytic inside $C$ the result is the number of zeros (Example §93.3).
> - **Counting from the integral.** $\frac{1}{2\pi i}\int_C f'/f\,dz = Z - P$; weighted versions such as $\frac{1}{2\pi i}\int_C z^kf'/f\,dz$ return sums of powers of the zeros (Example §93.4).
> - In practice the winding is rarely visible directly; Rouché's theorem ([[§94 Rouché's Theorem#^thm-94-1|Theorem §94.1]]) compares $f$ with a simpler function instead.

^rem-93-1

## Examples

> [!example] Example §93.1: A Function with One Pole Inside
> Let $f(z) = \dfrac{z^3 + 2}{z} = z^2 + \dfrac2z$ and let $C$ be the circle $|z| = 1$, positively oriented. The zeros of $f$ are the cube roots of $-2$, of modulus $\sqrt[3]{2} > 1$, so all lie outside $C$; the only singularity in the finite plane is a simple pole at the origin. By the argument principle, $Z = 0$, $P = 1$, and
>
> $$
> \Delta_C\arg f(z) = 2\pi(0 - 1) = -2\pi :
> $$
>
> the image $\Gamma$ of $C$ winds around $w = 0$ once in the clockwise direction. Directly: on $C$, $w = e^{i2\theta} + 2e^{-i\theta}$, dominated by the term $2e^{-i\theta}$, which turns once clockwise. The curve $\Gamma$ is a deltoid with cusps at $w = 3$ and $w = 3e^{\pm i2\pi/3}$, the images of the three points $z^3 = 1$ where $f'(z) = 2z - 2/z^2 = 0$.
>
> *B&C: Sec. 93, Example*

^ex-93-1

![[m342-93-1.svg]]
*Example §93.1: the unit circle $C$ (left), with the pole of $f(z) = z^2 + 2/z$ inside and its three zeros outside, and its image $\Gamma$ (right), computed from $w = e^{i2\theta} + 2e^{-i\theta}$. As $z$ goes once counterclockwise around $C$, $w$ goes once clockwise around the origin: winding number $Z - P = -1$. The cusps are the images of the points of $C$ where $f' = 0$.*

> [!example] Example §93.2: Three Changes of Argument
> Let $C$ be the unit circle $|z| = 1$, described in the positive sense. Use the argument principle to determine $\Delta_C\arg f(z)$ when
>
> $$
> \text{(a)}\ f(z) = z^2, \qquad \text{(b)}\ f(z) = 1/z^2, \qquad \text{(c)}\ f(z) = (2z - 1)^7/z^3 .
> $$
>
> **(a)** A zero of order $2$ at $0$, no poles: $\Delta_C\arg f = 2\pi\cdot2 = 4\pi$. (Directly: $e^{i\theta} \mapsto e^{i2\theta}$ goes twice around.)
>
> **(b)** A pole of order $2$ at $0$, no zeros: $\Delta_C\arg f = 2\pi(0 - 2) = -4\pi$.
>
> **(c)** A zero of order $7$ at $z = \frac12$, inside $C$, and a pole of order $3$ at $0$: $\Delta_C\arg f = 2\pi(7 - 3) = 8\pi$.
>
> All three agree with B&C's answers.
>
> *B&C: Sec. 94, Exercise 1*

^ex-93-2

> [!example] Example §93.3: Reading the Winding Number from a Picture
> Let $f$ be analytic inside and on a positively oriented simple closed contour $C$, never zero on $C$, and let the image of $C$ under $w = f(z)$ be the closed contour $\Gamma$ of B&C's Figure 114 (p. 293): a curve made of three loops, a narrow one around the $v$ axis, a medium one and a large one, all traversed counterclockwise and all enclosing the origin. Determine $\Delta_C\arg f(z)$ and the number of zeros of $f$ inside $C$.
>
> Count the crossings of $\Gamma$ with the positive $u$ axis, a ray from the origin. In the figure $\Gamma$ crosses it three times, each time going upward, that is, counterclockwise about the origin. Each such crossing adds $2\pi$ to the continuous argument (between crossings the argument cannot pass through a multiple of $2\pi$ without crossing the ray). So
>
> $$
> \Delta_C\arg f(z) = 3\cdot2\pi = 6\pi .
> $$
>
> Since $f$ is analytic inside $C$, $P = 0$, and the argument principle gives $Z = \frac{6\pi}{2\pi} = 3$: $f$ has three zeros inside $C$, counting multiplicities. Both values are B&C's answers.
>
> *B&C: Sec. 94, Exercise 2; Source: 342 HW 13*

^ex-93-3

> [!example] Example §93.4: Sums of Powers of the Zeros
> **(a)** Let $k$ and $m$ be nonnegative integers, $\phi$ analytic at $z_0$ with $\phi(z_0) \ne 0$, and $g(z) = (z - z_0)^m\phi(z)$. Then
>
> $$
> \operatorname{Res}_{z=z_0}\Big(z^k\,\frac{g'(z)}{g(z)}\Big) = mz_0^k .
> $$
>
> Indeed, by (6), $z^kg'/g = \frac{mz^k}{z - z_0} + z^k\frac{\phi'}{\phi}$. The second term is analytic at $z_0$ and has residue $0$. The first is $m\frac{z^k - z_0^k}{z - z_0} + \frac{mz_0^k}{z - z_0}$, where the quotient $\frac{z^k - z_0^k}{z - z_0} = z^{k-1} + z^{k-2}z_0 + \cdots + z_0^{k-1}$ is a polynomial; so the residue is $mz_0^k$ (with $z_0^0 = 1$, also when $z_0 = 0$; for $m = 0$ both sides are $0$).
>
> **(b)** Let $f$ be analytic inside and on a positively oriented simple closed contour $C$, with no zeros on $C$ and zeros $z_1, \ldots, z_n$ inside of multiplicities $m_1, \ldots, m_n$. Then for every nonnegative integer $k$,
>
> $$
> \int_C\frac{z^kf'(z)}{f(z)}\,dz = 2\pi i\sum_{j=1}^{n}m_jz_j^k .
> $$
>
> For $k = 0$ this is the argument principle with $P = 0$, and for $k = 1$ it is B&C's Exercise 5 of §94. Proof: $z^kf'/f$ is analytic inside and on $C$ except at the $z_j$, where $f = (z - z_j)^{m_j}\phi_j$ with $\phi_j$ analytic and nonzero at $z_j$ ([[§82 Zeros of Analytic Functions#^thm-82-1|Theorem §82.1]]). By (a) the residue there is $m_jz_j^k$, and the residue theorem gives the formula.
>
> For instance, if $f$ is a polynomial with all its zeros inside $C$, then $\frac{1}{2\pi i}\int_C zf'/f\,dz$ is the sum of the zeros, which is $-a_{n-1}/a_n$ for $f = a_nz^n + a_{n-1}z^{n-1} + \cdots$.
>
> *The key's boxed answer to (a) is written as $\operatorname{Res}_{z_0}\big(z^k\phi'(z)/\phi(z)\big) = z_0^km$; the residue meant is that of $z^kg'(z)/g(z)$ (the key itself shows that $z^k\phi'/\phi$ has residue $0$). In (b) its final sum runs to $m$ where $n$ is meant.*
>
> *B&C: Sec. 94, Exercise 5; Source: 342 practice final (Spring 2012), Q2*

^ex-93-4
