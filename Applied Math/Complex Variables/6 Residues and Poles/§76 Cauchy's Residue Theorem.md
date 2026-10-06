---
type: section
subject: "[[Complex Variables]]"
chapter: 6
section: 76
bc: "76"
aliases: ["B&C 76"]
tags: [complex-variables, math342]
---
← [[§75 Residues]] · ↑ [[· 6 Residues and Poles]] · [[§77★ Residue at Infinity]] →

*Brown–Churchill, Section 76 · MAT 342 HW 11, Practice Finals (Fall 1999, Fall 2002, Fall 2009).*

If $f$ is analytic inside and on a positively oriented simple closed contour $C$ except at finitely many points inside, then the integral of $f$ around $C$ is $2\pi i$ times the sum of the residues at those points. This is **Cauchy's residue theorem**, the central result of the chapter. Its proof combines two earlier facts: the Cauchy–Goursat theorem for multiply connected domains lets the contour shrink to small circles around the singular points, and around each circle the integral is $2\pi i$ times one residue ([[§75 Residues#^thm-75-1|Theorem §75.1]]). Evaluating a contour integral thereby becomes a local computation at finitely many points, which is how residues are used for real integrals in Chapter 7.

## The Theorem

If $f$ is analytic inside a simple closed contour $C$ except for a *finite* number of singular points, those points are isolated ([[§74 Isolated Singular Points#^prop-74-1|Proposition §74.1]]), and each has a residue.

> [!theorem] Theorem §76.1: Cauchy's Residue Theorem
> Let $C$ be a [[§43 Contours#^def-43-10|simple closed contour]], described in the positive sense. If a function $f$ is analytic inside and on $C$ except for a finite number of singular points $z_k$ ($k = 1, 2, \ldots, n$) inside $C$ (Fig. 93 in B&C), then
>
> $$
> \int_C f(z)\,dz = 2\pi i\sum_{k=1}^{n}\operatorname{Res}_{z=z_k} f(z) . \qquad (1)
> $$
>
> *B&C: Sec. 76, Theorem*

^thm-76-1

> [!proof]+ Proof
> By [[§74 Isolated Singular Points#^prop-74-1|Proposition §74.1]], each $z_k$ is isolated and has a deleted neighborhood $0 < |z - z_k| < \varepsilon_k$, lying inside $C$, in which $f$ is analytic, where (as in that proof) $\varepsilon_k$ is less than the distance from $z_k$ to every other $z_j$ and to $C$. Then the closed disks $|z - z_k| \le \varepsilon_k/2$ lie inside $C$ and are pairwise disjoint, since $\varepsilon_k/2 + \varepsilon_j/2 < |z_k - z_j|$. Let $C_k$ be the positively oriented circle $|z - z_k| = \varepsilon_k/2$. Then the circles $C_k$ are interior to $C$ and no two of them have points in common.
>
> The circles $C_k$, together with the simple closed contour $C$, form the boundary of a closed region throughout which $f$ is analytic: the points inside or on $C$ and on or exterior to every $C_k$. Its interior is a multiply connected domain. By the adaptation of the Cauchy–Goursat theorem to such domains ([[§53 Multiply Connected Domains#^thm-53-1|Theorem §53.1]]), with $C$ described in the positive sense and the $C_k$ in the negative sense,
>
> $$
> \int_C f(z)\,dz - \sum_{k=1}^{n}\int_{C_k} f(z)\,dz = 0 .
> $$
>
> Each $C_k$ is a positively oriented simple closed contour around $z_k$ lying in the punctured disk $0 < |z - z_k| < \varepsilon_k$ where $f$ is analytic, so by [[§75 Residues#^thm-75-1|Theorem §75.1]]
>
> $$
> \int_{C_k} f(z)\,dz = 2\pi i\operatorname{Res}_{z=z_k} f(z) \qquad (k = 1, 2, \ldots, n) .
> $$
>
> Substituting these values into the previous equation gives (1).

^pf-76-1

*Uses:* [[§74 Isolated Singular Points#^prop-74-1|§74.1]], [[§75 Residues#^thm-75-1|§75.1]], [[§53 Multiply Connected Domains#^thm-53-1|§53.1]] (Cauchy–Goursat for multiply connected domains)

![[m342-76-1.svg]]
*The proof of the residue theorem. The singular points $z_1, \ldots, z_n$ inside $C$ are enclosed in small disjoint circles $C_k$ (red). Between $C$ and the circles $f$ is analytic, so the integral over $C$ equals the sum of the integrals over the $C_k$, all taken counterclockwise; each of these is $2\pi i$ times one residue.*

> [!remark]- Connections
> - The Cauchy–Goursat theorem for multiply connected domains, which carries the proof, is the complex form of Green's theorem for a region with holes, [[§131 Extended Versions of Green's Theorem#^thm-131-2|Calc Thm. §131.2]] (the rigorous [[§27 Line Integrals and Green's Theorem#^thm-27-1|452 Thm. §27.1]] is stated for a region bounded by one simple closed curve and extends to holes by the same cutting into pieces), applied to $u$ and $v$ when their partial derivatives are continuous: the Cauchy–Riemann equations ([[§21 Cauchy–Riemann Equations#^thm-21-1|Theorem §21.1]]) make the double integrals vanish. The residue theorem says that all the circulation of $f$ around $C$ is concentrated at the singular points.
> - Fourier Series and PDEs inverts Laplace transforms by "closing the Bromwich line to the left" and summing residues of $e^{st}U(s)$ ([[§66★ Partial Differential Equations#^rem-66-2|341 Remark: The Extended Heaviside Formula]]): that step is Theorem §76.1 applied to large closed contours.

> [!remark] Remark: Method — Evaluating a Contour Integral by Residues
> 1. **Draw the contour** and find all singular points of $f$; decide which lie inside $C$. Singular points outside $C$ play no role.
> 2. **Compute the residue** at each singular point inside $C$: from a Laurent series ([[§75 Residues#^rem-75-1|Remark: Method — Computing a Residue from a Laurent Series]]), or, at a pole, by the formulas of [[§80 Residues at Poles#^thm-80-1|Theorem §80.1]] and [[§83 Zeros and Poles#^thm-83-2|Theorem §83.2]].
> 3. **Add and multiply by $2\pi i$**, checking that $C$ is positively oriented (for a clockwise contour the sign changes).
> 4. **Alternatives.** If $f = g(z)/(z - z_0)^{m}$ with $g$ analytic inside and on $C$ and $z_0$ the only singular point, the (extended) Cauchy integral formula ([[§54 Cauchy Integral Formula#^thm-54-1|Theorem §54.1]], [[§56★ Verification of the Extension (An Extension of the Cauchy Integral Formula)#^thm-56-1|Theorem §56.1]]) gives the same value; it is the residue theorem for a pole. If *all* the singular points of $f$ lie inside $C$ and there are many of them, the single residue of [[§77★ Residue at Infinity#^thm-77-2|Theorem §77.2]] may be quicker.

^rem-76-1

## Examples

> [!example] Example §76.1: Two Residues, by Series and by Partial Fractions
> Evaluate
>
> $$
> \int_C \frac{4z - 5}{z(z - 1)}\,dz , \qquad (2)
> $$
>
> where $C$ is the circle $|z| = 2$, described counterclockwise (Fig. 94 in B&C).
>
> The integrand has the two isolated singular points $z = 0$ and $z = 1$, both interior to $C$. Call the residues $B_1$ (at $0$) and $B_2$ (at $1$); both come from the Maclaurin series $\frac{1}{1 - z} = 1 + z + z^2 + \cdots$ ($|z| < 1$).
>
> **At $z = 0$.** When $0 < |z| < 1$,
>
> $$
> \frac{4z - 5}{z(z - 1)} = \frac{4z - 5}{z}\cdot\frac{-1}{1 - z} = \Big(4 - \frac5z\Big)\big(-1 - z - z^2 - \cdots\big) ,
> $$
>
> and the coefficient of $1/z$ in the product is $(-5)(-1)$:
>
> $$
> B_1 = 5 . \qquad (3)
> $$
>
> **At $z = 1$.** When $0 < |z - 1| < 1$,
>
> $$
> \frac{4z - 5}{z(z - 1)} = \frac{4(z - 1) - 1}{z - 1}\cdot\frac{1}{1 + (z - 1)} = \Big(4 - \frac{1}{z - 1}\Big)\big[1 - (z - 1) + (z - 1)^2 - \cdots\big] ,
> $$
>
> and the coefficient of $1/(z - 1)$ is $(-1)(1)$:
>
> $$
> B_2 = -1 . \qquad (4)
> $$
>
> **The integral.** By the residue theorem,
>
> $$
> \int_C \frac{4z - 5}{z(z - 1)}\,dz = 2\pi i(B_1 + B_2) = 2\pi i(5 - 1) = 8\pi i . \qquad (5)
> $$
>
> **Shortcut.** It is easier to start from the partial fractions
>
> $$
> \frac{4z - 5}{z(z - 1)} = \frac5z + \frac{-1}{z - 1}
> $$
>
> (check: $5(z - 1) - z = 4z - 5$). Since $5/z$ is already a Laurent series when $0 < |z| < 1$, and $-1/(z - 1)$ is one when $0 < |z - 1| < 1$, while the other fraction is analytic near each point, the residues $5$ and $-1$ can be read off directly.
>
> *B&C: Sec. 76, Example*

^ex-76-1

> [!example] Example §76.2: Residue Theorem Versus Cauchy's Integral Formula
> For each function, determine the type of the singular point, find the residue, and compute the integral over the circle $C\colon |z| = 2$, oriented counterclockwise. Can the Cauchy integral formula or its extension be used instead?
>
> $$
> \text{(a)}\ \frac{e^{-z^2}}{(z - 1)^2}; \qquad \text{(b)}\ z^3e^{1/z} .
> $$
>
> **(a) The singular point.** $e^{-z^2}$ is entire and $e^{-1} \ne 0$, so the only singular point is $z = 1$, inside $C$. Expanding $g(z) = e^{-z^2}$ in its Taylor series about $1$,
>
> $$
> \frac{e^{-z^2}}{(z - 1)^2} = \frac{g(1)}{(z - 1)^2} + \frac{g'(1)}{z - 1} + \frac{g''(1)}{2!} + \cdots \qquad (0 < |z - 1| < \infty) ,
> $$
>
> with $g(1) = e^{-1} \ne 0$: the principal part has exactly two terms, so $z = 1$ is a **pole of order 2** ([[§78 The Three Types of Isolated Singular Points#^def-78-4|Definition §78.4]]). The residue is
>
> $$
> \operatorname{Res}_{z=1}\frac{e^{-z^2}}{(z - 1)^2} = g'(1) = \big[-2ze^{-z^2}\big]_{z=1} = -\frac{2}{e} ,
> $$
>
> and the residue theorem gives
>
> $$
> \int_C \frac{e^{-z^2}}{(z - 1)^2}\,dz = 2\pi i\Big(-\frac2e\Big) = -\frac{4\pi i}{e} .
> $$
>
> *By Cauchy's formula.* Yes: $g(z) = e^{-z^2}$ is analytic inside and on $C$, and $z_0 = 1$ is interior to $C$, so the extended Cauchy integral formula $\int_C \frac{g(z)\,dz}{(z - z_0)^{n+1}} = \frac{2\pi i}{n!}g^{(n)}(z_0)$ ([[§56★ Verification of the Extension (An Extension of the Cauchy Integral Formula)#^thm-56-1|Theorem §56.1]]) with $n = 1$ gives $2\pi i\,g'(1) = -4\pi i/e$, the same value.
>
> **(b) The singular point.** $z^3e^{1/z}$ is analytic except at $z = 0$, inside $C$. Its Laurent series is
>
> $$
> z^3e^{1/z} = z^3\sum_{n=0}^{\infty}\frac{1}{n!\,z^n} = \sum_{n=0}^{\infty}\frac{z^{3-n}}{n!} = z^3 + z^2 + \frac{z}{2!} + \frac{1}{3!} + \frac{1}{4!\,z} + \frac{1}{5!\,z^2} + \cdots \qquad (0 < |z| < \infty) .
> $$
>
> Infinitely many negative powers occur, so $z = 0$ is an **essential singular point** ([[§78 The Three Types of Isolated Singular Points#^def-78-3|Definition §78.3]]). The term $z^{-1}$ has $3 - n = -1$, $n = 4$, so
>
> $$
> \operatorname{Res}_{z=0} z^3e^{1/z} = \frac{1}{4!} = \frac{1}{24}, \qquad \int_C z^3e^{1/z}\,dz = 2\pi i\cdot\frac{1}{24} = \frac{\pi i}{12} .
> $$
>
> *By Cauchy's formula.* No: the formula needs the integrand in the form $g(z)/(z - z_0)^{n+1}$ with $g$ analytic inside and on $C$. Here $z^3e^{1/z} = g(z)/z^{m}$ would require $g(z) = z^{m+3}e^{1/z}$, which still has an essential singular point at $0$ for every $m$ (its Laurent series still has infinitely many negative powers). At an essential singular point only the Laurent series gives the residue.
>
> *Source: 342 HW 11, Problem 1*

^ex-76-2

A simple and a double pole together occur in a final-exam integral, $\int_C \frac{e^z}{z^3 - 2z^2}\,dz$ over the counterclockwise circle $|z| = 3$, which is worked with the Cauchy integral formula in [[§55 An Extension of the Cauchy Integral Formula#^ex-55-5|Example §55.5]](b). In the language of residues the two pieces there are $\operatorname{Res}_{z=2} = \phi(2) = \frac{e^2}{4}$ with $\phi(z) = e^z/z^2$, and $\operatorname{Res}_{z=0} = h'(0) = -\frac34$ with $h(z) = e^z/(z - 2)$ (the residue formulas of [[§80 Residues at Poles#^thm-80-1|Theorem §80.1]] with $m = 1$ and $m = 2$), so the integral is $2\pi i\big(\frac{e^2}{4} - \frac34\big) = \frac{\pi i}{2}(e^2 - 3)$.

> [!example] Example §76.3: Exponential Denominators
> Evaluate, with all circles traversed counterclockwise,
>
> $$
> \text{(a)}\ \int_{|z| = 1}\frac{\sin z + 1}{e^{3z} - e^z}\,dz; \qquad \text{(b)}\ \int_{|z| = 1}\frac{\cos z + 1}{e^{2z} - e^z}\,dz; \qquad \text{(c)}\ \int_{|z| = 2}\frac{\cos z}{e^{iz} - 1}\,dz .
> $$
>
> **Where the denominators vanish.** $e^w = 1$ exactly when $w = 2k\pi i$, $k \in \mathbb{Z}$ ([[§31 The Logarithmic Function#^thm-31-1|Theorem §31.1]]). (a) $e^{3z} - e^z = e^z(e^{2z} - 1)$ vanishes when $2z = 2k\pi i$, $z = k\pi i$; inside $|z| = 1$ only $z = 0$. (b) $e^{2z} - e^z = e^z(e^z - 1)$ vanishes at $z = 2k\pi i$; inside $|z| = 1$ only $z = 0$. (c) $e^{iz} = 1$ when $iz = 2k\pi i$, $z = 2k\pi$; inside $|z| = 2$ only $z = 0$. In each case the numerator is entire, so the only singular point inside the contour is $z = 0$.
>
> **The residue at $0$.** Each integrand has the form $p(z)/q(z)$ with $p, q$ entire, $q(0) = 0$ and $q'(0) \ne 0$. Write $q(z) = q'(0)z + \frac{q''(0)}{2}z^2 + \cdots = z\,g(z)$ with $g$ entire and $g(0) = q'(0) \ne 0$; then $p/q = (p/g)/z$ with $p/g$ analytic at $0$, so the coefficient of $1/z$ is $p(0)/g(0) = p(0)/q'(0)$. (This is [[§83 Zeros and Poles#^thm-83-2|Theorem §83.2]].)
> - (a) $p(0) = \sin 0 + 1 = 1$, $q'(z) = 3e^{3z} - e^z$, $q'(0) = 2$: residue $\frac12$, integral $2\pi i\cdot\frac12 = \pi i$.
> - (b) $p(0) = \cos 0 + 1 = 2$, $q'(z) = 2e^{2z} - e^z$, $q'(0) = 1$: residue $2$, integral $4\pi i$.
> - (c) $p(0) = \cos 0 = 1$, $q'(z) = ie^{iz}$, $q'(0) = i$: residue $\frac1i = -i$, integral $2\pi i(-i) = 2\pi$.
>
> *Source: 342 practice final (Fall 2002), Q3; 342 practice final (Fall 2009), Q4(b); 342 practice final (Fall 1999), Q2*

^ex-76-3
