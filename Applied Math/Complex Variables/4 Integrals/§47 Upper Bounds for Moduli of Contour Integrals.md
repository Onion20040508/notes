---
type: section
subject: "[[Complex Variables]]"
chapter: 4
section: 47
bc: "47"
aliases: ["B&C 47"]
tags: [complex-variables, math342]
---
← [[§46 Examples Involving Branch Cuts]] · ↑ [[· 4 Integrals]] · [[§48 Antiderivatives]] →

*Brown–Churchill, Section 47 · MAT 342 HW 5, HW 6, Practice Finals (Fall 1999, Fall 2002, Spring 2005, Fall 2009, Spring 2012).*

Most contour integrals are never evaluated exactly; what is needed is an estimate. The **ML-inequality** says that if $|f(z)| \le M$ on a contour $C$ of length $L$, then $\big|\int_C f(z)\,dz\big| \le ML$. It rests on the inequality $\big|\int_a^b w(t)\,dt\big| \le \int_a^b |w(t)|\,dt$, whose proof has to get around the fact that complex numbers cannot be compared: rotate the integral onto the positive real axis first. The ML-inequality is used to show that integrals over large semicircles tend to zero (evaluating improper integrals, [[§85 Evaluation of Improper Integrals#^thm-85-3|Theorem §85.3]]) and integrals over small circles too; it is also the analytic step in the proofs of [[§49 Proof of the Theorem (Antiderivatives)#^thm-49-1|§49]], of the Cauchy–Goursat theorem and of the Cauchy integral formula.

## The Lemma and the Theorem

> [!theorem] Lemma §47.1: Modulus of an Integral of w(t)
> If $w(t)$ is a piecewise continuous complex-valued function defined on an interval $a \le t \le b$, then
>
> $$
> \Big|\int_a^b w(t)\,dt\Big| \le \int_a^b |w(t)|\,dt . \qquad (1)
> $$
>
> *B&C: Sec. 47, Lemma*

^lem-47-1

> [!proof]+ Proof
> The function $|w(t)| = \sqrt{u^2 + v^2}$ is piecewise continuous, so the right side exists. The inequality clearly holds when the value of the integral on the left is zero. Otherwise write it in exponential form,
>
> $$
> \int_a^b w(t)\,dt = r_0e^{i\theta_0} \qquad (r_0 > 0) . \qquad (2)
> $$
>
> Solving for $r_0$ (multiply by the constant $e^{-i\theta_0}$, [[§42 Definite Integrals of Functions w(t)#^prop-42-1|Proposition §42.1]](b)),
>
> $$
> r_0 = \int_a^b e^{-i\theta_0}w(t)\,dt . \qquad (3)
> $$
>
> The left side is a real number, so the right side is too, and a real number equals its real part. By the first of properties (3) in [[§42 Definite Integrals of Functions w(t)#^def-42-1|§42]],
>
> $$
> r_0 = \operatorname{Re}\int_a^b e^{-i\theta_0}w(t)\,dt = \int_a^b \operatorname{Re}\big[e^{-i\theta_0}w(t)\big]\,dt . \qquad (4)
> $$
>
> But for each $t$,
>
> $$
> \operatorname{Re}\big[e^{-i\theta_0}w(t)\big] \le \big|e^{-i\theta_0}w(t)\big| = |e^{-i\theta_0}|\,|w(t)| = |w(t)| ,
> $$
>
> and integrating this inequality between real functions (monotonicity of the integral) gives, with (4), $r_0 \le \int_a^b |w(t)|\,dt$. By (2), $r_0$ is the left side of (1).

^pf-47-1

*Uses:* [[§42 Definite Integrals of Functions w(t)#^def-42-1|Def. §42.1]], [[§42 Definite Integrals of Functions w(t)#^prop-42-1|§42.1]], [[§33 Properties of the Riemann Integral#^thm-33-3|451 Thm. §33.3]] (monotonicity of the integral)

> [!remark]- Connections
> - For real $w$ this is [[§33 Properties of the Riemann Integral#^thm-33-4|451 Thm. §33.4]], proved from $-|w| \le w \le |w|$. That trick has no complex analogue, and the rotation by $e^{-i\theta_0}$ replaces it.

> [!theorem] Theorem §47.2: The ML-Inequality
> Let $C$ denote a contour of length $L$, and suppose that a function $f(z)$ is piecewise continuous on $C$. If $M$ is a nonnegative constant such that
>
> $$
> |f(z)| \le M \qquad (5)
> $$
>
> for all points $z$ on $C$ at which $f(z)$ is defined, then
>
> $$
> \Big|\int_C f(z)\,dz\Big| \le ML . \qquad (6)
> $$
>
> The inequality (6) is strict if inequality (5) is strict at all such points and $L > 0$.
>
> *B&C: Sec. 47, Theorem*

^thm-47-2

> [!proof]+ Proof
> Let $z = z(t)$ $(a \le t \le b)$ be a parametric representation of $C$. By [[§47 Upper Bounds for Moduli of Contour Integrals#^lem-47-1|Lemma §47.1]],
>
> $$
> \Big|\int_C f(z)\,dz\Big| = \Big|\int_a^b f[z(t)]\,z'(t)\,dt\Big| \le \int_a^b \big|f[z(t)]\,z'(t)\big|\,dt .
> $$
>
> Since $\big|f[z(t)]z'(t)\big| = |f[z(t)]|\,|z'(t)| \le M|z'(t)|$ when $a \le t \le b$, except possibly at finitely many points (which do not affect the integral),
>
> $$
> \Big|\int_C f(z)\,dz\Big| \le M\int_a^b |z'(t)|\,dt = ML ,
> $$
>
> the last integral being the length of $C$ ([[§43 Contours#^def-43-3|Definition §43.3]], summed over the smooth arcs of $C$).
>
> **Strictness** (B&C: "of course"; here is why). Suppose $|f(z)| < M$ wherever $f$ is defined on $C$, and $L > 0$. Some smooth arc of $C$, say on $[t_{k-1}, t_k]$, has positive length, so $t_{k-1} < t_k$. Inside $[t_{k-1}, t_k]$ choose a subinterval $[c, d]$, $c < d$, containing no point where $f[z(t)]$ is discontinuous (there are only finitely many). The function $g(t) = \big(M - |f[z(t)]|\big)|z'(t)|$ is nonnegative wherever $f[z(t)]$ is defined; on $[c, d]$, made continuous at $c$ and $d$ by one-sided limits, it is continuous, and it is positive on $(c, d)$, because $|f| < M$ there and $z'(t) \ne 0$ inside a smooth arc. A continuous nonnegative function that is positive somewhere has positive integral, so $\int_c^d g\,dt > 0$, while $\int g\,dt \ge 0$ over the rest of $[a, b]$. Hence $\int_a^b g\,dt > 0$, that is, $\int_a^b |f[z(t)]|\,|z'(t)|\,dt < M\int_a^b |z'(t)|\,dt = ML$.

^pf-47-2

*Uses:* [[§47 Upper Bounds for Moduli of Contour Integrals#^lem-47-1|§47.1]], [[§44 Contour Integrals#^def-44-1|Def. §44.1]], [[§43 Contours#^def-43-3|Def. §43.3]], [[§43 Contours#^def-43-4|Def. §43.4]], [[§33 Properties of the Riemann Integral#^thm-33-7|451 Thm. §33.7]] (a nonnegative continuous function with zero integral vanishes)

> [!remark] Remark: Such a Bound Always Exists
> Since $C$ is a contour and $f$ is piecewise continuous on $C$, a number $M$ as in (5) always exists. On each smooth arc of $C$, $|f[z(t)]|$ (redefined at the ends by its one-sided limits) is continuous on a closed bounded interval, so it reaches a maximum value there by the extreme value theorem; the largest of these finitely many maxima will do. In practice $M$ is found by the triangle inequalities, as in the examples, and need not be the maximum.

^rem-47-1

> [!remark]- Connections
> - The existence of $M$ is the extreme value theorem, [[§18 Properties of Continuous Functions#^thm-18-1|451 Thm. §18.1]] (and [[§18 Continuity#^thm-18-6|Theorem §18.6]] for continuous functions of $z$ on a closed bounded region).

> [!remark] Remark: Method — Bounding a Contour Integral
> 1. **$L$.** Find the length of $C$: $|z_2 - z_1|$ for a segment, $R\,\Delta\theta$ for an arc of a circle of radius $R$, $\pi R$ for a semicircle.
> 2. **$M$, numerator.** Bound $|$numerator$|$ from above with the triangle inequality $|z_1 + z_2| \le |z_1| + |z_2|$ ([[§5 Triangle Inequality#^thm-5-1|§5.1]]); for exponentials use $|e^{z}| = e^{x}$, so $|e^{iz}| = e^{-y}$; for logarithms $|\operatorname{Log} z| \le \ln|z| + \pi$ when $|z| \ge 1$.
> 3. **$M$, denominator.** Bound $|$denominator$|$ from *below* with the reverse triangle inequality $|z_1 + z_2| \ge \big||z_1| - |z_2|\big|$ ([[§5 Triangle Inequality#^cor-5-2|§5.2]]), checking that the bound is positive on $C$; or use the distance from the origin to $C$.
> 4. **Limits.** To show $\int_{C_R} \to 0$ as $R \to \infty$ (or $\rho \to 0$), write $M_RL$ as a function of $R$ and divide numerator and denominator by the highest power of $R$.

^rem-47-2

## B&C's Examples

> [!example] Example §47.1: An Arc of a Circle
> Let $C$ be the arc of the circle $|z| = 2$ from $z = 2$ to $z = 2i$ that lies in the first quadrant. Show that
>
> $$
> \Big|\int_C \frac{z - 2}{z^4 + 1}\,dz\Big| \le \frac{4\pi}{15} . \qquad (7)
> $$
>
> If $z$ is a point on $C$, then
>
> $$
> |z - 2| = |z + (-2)| \le |z| + |-2| = 2 + 2 = 4 \qquad\text{and}\qquad |z^4 + 1| \ge \big||z|^4 - 1\big| = 15 .
> $$
>
> Thus, when $z$ lies on $C$,
>
> $$
> \Big|\frac{z - 2}{z^4 + 1}\Big| = \frac{|z - 2|}{|z^4 + 1|} \le \frac{4}{15} .
> $$
>
> With $M = 4/15$ and $L = \pi$ (a quarter of the circumference $4\pi$), inequality (6) gives (7). (The actual modulus is about $0.183$, against the bound $0.838$.)
>
> *B&C: Sec. 47, Example 1*

^ex-47-1

> [!example] Example §47.2: A Large Semicircle
> Let $C_R$ be the semicircle $z = Re^{i\theta}$ $(0 \le \theta \le \pi)$ from $z = R$ to $z = -R$, where $R > 3$. Show that
>
> $$
> \lim_{R\to\infty}\int_{C_R}\frac{(z + 1)\,dz}{(z^2 + 4)(z^2 + 9)} = 0 \qquad (8)
> $$
>
> without evaluating the integral. If $z$ is a point on $C_R$,
>
> $$
> |z + 1| \le |z| + 1 = R + 1, \qquad |z^2 + 4| \ge \big||z|^2 - 4\big| = R^2 - 4, \qquad |z^2 + 9| \ge \big||z|^2 - 9\big| = R^2 - 9 .
> $$
>
> So if $f(z)$ is the integrand in (8),
>
> $$
> |f(z)| = \frac{|z + 1|}{|z^2 + 4|\,|z^2 + 9|} \le \frac{R + 1}{(R^2 - 4)(R^2 - 9)} = M_R ,
> $$
>
> where $M_R$ is an upper bound for $|f(z)|$ on $C_R$ ($R > 3$ makes both factors of the denominator positive). The length of $C_R$ is $L = \pi R$, so by Theorem §47.2
>
> $$
> \Big|\int_{C_R}\frac{(z + 1)\,dz}{(z^2 + 4)(z^2 + 9)}\Big| \le M_RL , \qquad (9)
> $$
>
> where
>
> $$
> M_RL = \frac{\pi(R^2 + R)}{(R^2 - 4)(R^2 - 9)}\cdot\frac{1/R^4}{1/R^4} = \frac{\pi\Big(\dfrac{1}{R^2} + \dfrac{1}{R^3}\Big)}{\Big(1 - \dfrac{4}{R^2}\Big)\Big(1 - \dfrac{9}{R^2}\Big)} .
> $$
>
> This shows that $M_RL \to 0$ as $R \to \infty$, and (8) follows from (9).
>
> *B&C: Sec. 47, Example 2*

^ex-47-2

## Course Examples

> [!example] Example §47.3: An Arc and a Segment
> **(a)** Let $C$ be the arc of Example §47.1. Show that $\Big|\displaystyle\int_C \frac{z + 4}{z^3 - 1}\,dz\Big| \le \dfrac{6\pi}{7}$.
>
> On $C$, $|z + 4| \le |z| + 4 = 6$ and $|z^3 - 1| \ge |z|^3 - 1 = 7$, so $M = 6/7$; with $L = \pi$ the bound is $6\pi/7$. (Actual modulus about $1.614$, against $2.693$.)
>
> **(b)** Let $C$ be the line segment from $z = i$ to $z = 1$. Show that $\Big|\displaystyle\int_C \frac{dz}{z^4}\Big| \le 4\sqrt2$ without evaluating the integral.
>
> Of all the points on the segment, the midpoint $\frac12(1 + i)$ is closest to the origin, at distance $d = \sqrt2/2$. (The foot of the perpendicular from $0$ to the line $x + y = 1$ is that midpoint.) So $|z| \ge \sqrt2/2$ on $C$ and
>
> $$
> \Big|\frac{1}{z^4}\Big| = \frac{1}{|z|^4} \le \frac{1}{(\sqrt2/2)^4} = 4 = M .
> $$
>
> The length of $C$ is $L = |1 - i| = \sqrt2$, so the integral is at most $4\sqrt2$ in modulus. (In fact, by an antiderivative, $\int_C z^{-4}\,dz = -\frac13\big[z^{-3}\big]_i^1 = -\frac13(1 - i)$, of modulus $0.471$.)
>
> *B&C: Sec. 47, Exercises 1(a) and 2; Source: 342 HW 5*

^ex-47-3

> [!example] Example §47.4: Log z / z² on a Large Circle
> Let $C_R$ be the circle $|z| = R$ $(R > 1)$, counterclockwise. Show that
>
> $$
> \Big|\int_{C_R}\frac{\operatorname{Log} z}{z^2}\,dz\Big| < 2\pi\Big(\frac{\pi + \ln R}{R}\Big) ,
> $$
>
> and that the integral tends to zero as $R \to \infty$.
>
> On $C_R$, $\operatorname{Log} z = \ln R + i\Theta$ with $-\pi < \Theta \le \pi$. Since $\ln R > 0$,
>
> $$
> |\operatorname{Log} z| = |\ln R + i\Theta| \le \ln R + |\Theta| \le \ln R + \pi ,
> $$
>
> with strict inequality everywhere on $C_R$: if $|\Theta| < \pi$ the second step is strict, and at $z = -R$, $|\ln R + i\pi| = \sqrt{\ln^2R + \pi^2} < \ln R + \pi$. Hence $|f(z)| < (\pi + \ln R)/R^2 = M$ on $C_R$, and with $L = 2\pi R$ the strict form of Theorem §47.2 gives the bound $2\pi(\pi + \ln R)/R$. ($\operatorname{Log} z$ is discontinuous at $z = -R$, but the integrand is piecewise continuous on $C_R$.) By l'Hôpital's rule,
>
> $$
> \lim_{R\to\infty}\frac{\pi + \ln R}{R} = \lim_{R\to\infty}\frac{1/R}{1} = 0 ,
> $$
>
> so the integral tends to zero. (Parametrizing shows that the integral is exactly $2\pi i/R$: modulus $2\pi/R$, against the bound $2\pi(\pi + \ln R)/R$.)
>
> *B&C: Sec. 47, Exercise 5; Source: 342 HW 6, Problem 2*

^ex-47-4

> [!example] Example §47.5: Bounds from Old Finals
> **(a)** Let $C_A$ be the straight line segment from $A + iA$ to $-A + iA$, where $A > 1$. Prove that
>
> $$
> \Big|\int_{C_A}\frac{e^{iz}}{z^2 + 1}\,dz\Big| \le \frac{2Ae^{-A}}{A^2 - 1} .
> $$
>
> On $C_A$, $z = x + iA$ with $|x| \le A$, so $|e^{iz}| = |e^{ix - A}| = e^{-A}$, and $|z|^2 = x^2 + A^2 \ge A^2$, so $|z^2 + 1| \ge |z|^2 - 1 \ge A^2 - 1 > 0$. Hence $M = e^{-A}/(A^2 - 1)$, and $L = 2A$. The bound tends to $0$ as $A \to \infty$: on a high horizontal line, $e^{iz}$ is exponentially small.
>
> **(b)** Let $S_R$ be the upper semicircle $z = Re^{i\theta}$ $(0 \le \theta \le \pi)$, $R > 1$. Prove that $\displaystyle\lim_{R\to\infty}\int_{S_R}\frac{z^2\,dz}{1 + z^4} = 0$.
>
> On $S_R$, $|z^2| = R^2$ and $|1 + z^4| \ge |z|^4 - 1 = R^4 - 1$, and $L = \pi R$, so the modulus of the integral is at most $\pi R^3/(R^4 - 1) = \pi\big(1/R\big)/\big(1 - 1/R^4\big) \to 0$.
>
> **(c)** Prove that $\Big|\displaystyle\int_C e^{iz^2}\,dz\Big| < 5$, where $C$ is the arc of the circle $|z| = 2$ from $2$ to $2i$, counterclockwise.
>
> On $C$, $z = 2e^{i\theta}$ $(0 \le \theta \le \frac\pi2)$, so $iz^2 = 4ie^{2i\theta}$ has real part $-4\sin 2\theta \le 0$, and $|e^{iz^2}| = e^{-4\sin 2\theta} \le 1$. With $M = 1$ and $L = \pi$, the modulus is at most $\pi < 5$. (Numerically it is $0.486$.)
>
> **(d)** Let $S_r$ be the upper half of the circle of radius $r$ centered at $0$, $z = re^{i\theta}$ $(0 \le \theta \le \pi)$, and let $g$ be analytic in some open disk $|z| < R_0$. Prove that $\displaystyle\lim_{r\to0}\int_{S_r} g(z)\,dz = 0$.
>
> Fix $R$ with $0 < R < R_0$. Since $g$ is analytic, it is continuous on the closed disk $|z| \le R$, which is closed and bounded, so $|g| \le M$ there for some $M$ ([[§18 Continuity#^thm-18-6|Theorem §18.6]]). For $r \le R$, Theorem §47.2 gives $\big|\int_{S_r} g\,dz\big| \le M\pi r \to 0$.
>
> The second part of that problem, $\int_{S_r} f\,dz \to \pi i\operatorname{Res}_{z=0} f$ for a simple pole, is B&C's indentation lemma, [[§89★ An Indented Path#^thm-89-1|Theorem §89.1]].
>
> These bounds are used in context later: (a) is the top side of a rectangle, an alternative to the semicircle for the Fourier-type integrals of [[§87 Improper Integrals from Fourier Analysis#^prop-87-1|Proposition §87.1]]; (b) is the arc estimate behind the degree condition, [[§85 Evaluation of Improper Integrals#^prop-85-4|Proposition §85.4]].
>
> *In (d) the Spring 2012 key writes the length of $S_r$ as $2\pi r$; it is $\pi r$. The conclusion is unaffected.*
>
> *Source: (a) 342 practice final (Fall 2002), Q7, and (Fall 2009), Q7; (b) 342 practice final (Spring 2005), Q7; (c) 342 practice final (Fall 1999), Q9; (d) 342 practice final (Spring 2012), Q7(a)*

^ex-47-5
