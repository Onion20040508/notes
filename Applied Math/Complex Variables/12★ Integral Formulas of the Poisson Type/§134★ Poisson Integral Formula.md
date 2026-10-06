---
type: section
subject: "[[Complex Variables]]"
chapter: 12
section: "134★"
bc: "134"
aliases: ["B&C 134"]
tags: [complex-variables, math342, extension]
---
← [[§133a The Square, the Equilateral Triangle and the Step]] · ↑ [[· 12★ Integral Formulas of the Poisson Type]] · [[§135★ Dirichlet Problem for a Disk]] →

*Brown–Churchill, Section 134.*
★ *Beyond MAT 342: the course skipped this section or left it optional; it is included from Brown–Churchill.*

Chapter 12 develops integral formulas that solve boundary value problems for harmonic functions. The Cauchy integral formula gives the values of an analytic function inside a circle from its values on the circle; subtracting the (zero) Cauchy integral at the inverse point turns the kernel into a real one, the Poisson kernel, and taking real parts gives the Poisson integral formula for a harmonic function in a disk. The kernel is positive, harmonic and has mean value one, which is what makes the formula solve the Dirichlet problem in [[§135★ Dirichlet Problem for a Disk|§135★]]. The same formula is derived in Fourier Series and PDEs by summing the series solution of separation of variables (the two derivations are linked below); physically, it gives the potential inside a long cylinder with prescribed surface voltage, and the steady temperatures in a disk.

## The Formula

Let $C_0$ be the positively oriented circle $|z| = r_0$, and suppose that $f$ is analytic inside and on $C_0$. The Cauchy integral formula ([[§54 Cauchy Integral Formula#^thm-54-1|Theorem §54.1]])

$$
f(z) = \frac{1}{2\pi i}\int_{C_0}\frac{f(s)\,ds}{s - z} \qquad (1)
$$

expresses the value of $f$ at any point $z$ interior to $C_0$ in terms of its values at points $s$ on $C_0$. We obtain from it a corresponding formula for the real component of $f$.

> [!definition] Definition §134.1: Inverse Point with Respect to a Circle
> Let $z \ne 0$. The **inverse** of $z$ with respect to the circle $|z| = r_0$ is the point $z_1$ lying on the same ray from the origin as $z$ and satisfying $|z_1||z| = r_0^2$. If $z = re^{i\theta}$, then
>
> $$
> z_1 = \frac{r_0^2}{r}e^{i\theta} = \frac{r_0^2}{\overline z} .
> $$
>
> If $0 < r < r_0$, then $|z_1| = \frac{r_0}{r}r_0 > r_0$: the inverse of an interior point is exterior. (For $r_0 = 1$, inverse points were used in [[§97★ The Transformation w = 1∕z#^def-97-1|Definition §97.1]].)
>
> *B&C: Sec. 134 (text)*

^def-134-1

> [!theorem] Theorem §134.1: Poisson Integral Formula
> Let $f$ be analytic inside and on the circle $C_0\colon |z| = r_0$, and write $s = r_0e^{i\phi}$, $z = re^{i\theta}$. For $0 \le r < r_0$,
>
> $$
> f(re^{i\theta}) = \frac{r_0^2 - r^2}{2\pi}\int_0^{2\pi}\frac{f(r_0e^{i\phi})}{|s - z|^2}\,d\phi , \qquad (4)
> $$
>
> where, by the law of cosines ([[§142 Trigonometry#^thm-142-6|Calc Thm. §142.6]]),
>
> $$
> |s - z|^2 = r_0^2 - 2r_0r\cos(\phi - \theta) + r^2 . \qquad (5)
> $$
>
> Hence, if $u$ is the real component of $f$,
>
> $$
> u(r, \theta) = \frac{1}{2\pi}\int_0^{2\pi}\frac{(r_0^2 - r^2)\,u(r_0, \phi)}{r_0^2 - 2r_0r\cos(\phi - \theta) + r^2}\,d\phi \qquad (r < r_0) . \qquad (6)
> $$
>
> This is the **Poisson integral formula** for the harmonic function $u$ in the open disk bounded by the circle $r = r_0$.
>
> *B&C: Sec. 134, equations (4)–(6)*

^thm-134-1

> [!proof]+ Proof
> **$0 < r < r_0$.** Let $z_1 = r_0^2/\overline z$ be the inverse point (Definition §134.1). It is exterior to $C_0$, so $f(s)/(s - z_1)$ is analytic inside and on $C_0$, and by the Cauchy–Goursat theorem ([[§51 Proof of the Theorem (Cauchy–Goursat Theorem)#^thm-51-3|Theorem §51.3]])
>
> $$
> \int_{C_0}\frac{f(s)\,ds}{s - z_1} = 0 .
> $$
>
> Subtracting this from (1),
>
> $$
> f(z) = \frac{1}{2\pi i}\int_{C_0}\Big(\frac{1}{s - z} - \frac{1}{s - z_1}\Big)f(s)\,ds .
> $$
>
> With the parametric representation $s = r_0e^{i\phi}$ ($0 \le \phi \le 2\pi$), $ds = is\,d\phi$, so
>
> $$
> f(z) = \frac{1}{2\pi}\int_0^{2\pi}\Big(\frac{s}{s - z} - \frac{s}{s - z_1}\Big)f(s)\,d\phi , \qquad (2)
> $$
>
> where for convenience $s$ still denotes $r_0e^{i\phi}$. Now $s\overline s = r_0^2$, so
>
> $$
> z_1 = \frac{r_0^2}{r}e^{i\theta} = \frac{r_0^2}{re^{-i\theta}} = \frac{s\overline s}{\overline z} ,
> $$
>
> and the quantity in parentheses in (2) is
>
> $$
> \frac{s}{s - z} - \frac{s}{s - s\overline s/\overline z} = \frac{s}{s - z} - \frac{\overline z}{\overline z - \overline s} = \frac{s}{s - z} + \frac{\overline z}{\overline s - \overline z} = \frac{s(\overline s - \overline z) + \overline z(s - z)}{|s - z|^2} = \frac{r_0^2 - r^2}{|s - z|^2} . \qquad (3)
> $$
>
> Substituting (3) into (2) gives (4).
>
> **$r = 0$.** Then (4) reads $f(0) = \frac{1}{2\pi}\int_0^{2\pi}f(r_0e^{i\phi})\,d\phi$, which is just the parametric form of (1) at $z = 0$ (the inverse point does not exist, and none is needed).
>
> **The real part.** The triangle with vertices $0$, $z$, $s$ has sides $r$, $r_0$ and angle $\phi - \theta$ at the origin, so the law of cosines gives (5). The factor $\frac{r_0^2 - r^2}{|s - z|^2}$ is real, so taking real parts of (4) gives (6).

^pf-134-1

*Uses:* [[§54 Cauchy Integral Formula#^thm-54-1|§54.1]] (Cauchy integral formula), [[§51 Proof of the Theorem (Cauchy–Goursat Theorem)#^thm-51-3|§51.3]] (Cauchy–Goursat), [[§134★ Poisson Integral Formula#^def-134-1|Def. §134.1]]

> [!remark]- Connections
> - The same formula is [[§49 The Poisson Integral Formula and the Mean Value Property#^thm-49-1|341 Thm. §49.1]], proved there from the other end: solve Dirichlet's problem in the disk by separation of variables ([[§48 Potential in a Disk#^thm-48-2|341 Thm. §48.2]]), substitute the Fourier coefficients into the series, and sum the kernel $1 + 2\sum\rho^n\cos n\psi$ as a geometric series. Here the kernel comes from the Cauchy integral formula and the inverse point, with no series at all; [[§135★ Dirichlet Problem for a Disk#^prop-135-3|Proposition §135.3]] recovers the series form, closing the circle between the two proofs.
> - The kernel is, up to the factor $\frac{1}{2\pi r_0}$, the normal derivative of the Green's function of the disk; the general representation of a harmonic function by its boundary values comes from Green's second identity with the fundamental solution $\ln r$, [[§28 The Divergence Theorem in Higher Dimensions and Green's Identities#^thm-28-3|452 Thm. §28.3]] and [[§29 Conservation of Mass and Laplace's Equation#^thm-29-2|452 Thm. §29.2]].

Formula (6) holds for every function $u$ harmonic in a domain containing the closed disk $|z| \le r_0$, not only for the real part of a given $f$: such a $u$ is harmonic in a slightly larger open disk, which is simply connected, so it has a harmonic conjugate $v$ there ([[§115★ Harmonic Conjugates#^thm-115-4|Theorem §115.4]]), and $f = u + iv$ is analytic inside and on $C_0$.

## The Poisson Kernel

Formula (6) defines a linear integral transformation of $u(r_0, \phi)$ into $u(r, \theta)$.

> [!definition] Definition §134.2: Poisson Kernel
> The **Poisson kernel** is the real-valued function
>
> $$
> P(r_0, r, \phi - \theta) = \frac{r_0^2 - r^2}{r_0^2 - 2r_0r\cos(\phi - \theta) + r^2} , \qquad (7)
> $$
>
> which is, except for the factor $1/(2\pi)$, the kernel of the transformation (6). By (5) it can also be written
>
> $$
> P(r_0, r, \phi - \theta) = \frac{r_0^2 - r^2}{|s - z|^2} . \qquad (8)
> $$
>
> *B&C: Sec. 134, equations (7)–(8)*

^def-134-2

![[m342-134-1.svg]]
*The Poisson kernel $P(1, r, \phi - \theta)$ for $r = 0, 0.5, 0.8$. Each curve has mean value $1$ over a period (property (f)); its peak $(1 + r)/(1 - r)$ at $\phi = \theta$ grows and narrows as $z = re^{i\theta}$ approaches the boundary, so that the average (9) is dominated more and more by the boundary values near $\phi = \theta$.*

> [!theorem] Proposition §134.2: Properties of the Poisson Kernel
> For $r < r_0$:
>
> **(a)** $P$ is a positive function;
>
> **(b)** $P(r_0, r, \phi - \theta) = \operatorname{Re}\dfrac{s + z}{s - z}$;
>
> **(c)** $P(r_0, r, \phi - \theta)$ is a harmonic function of $r$ and $\theta$ interior to the circle $C_0$, for each fixed $s$ on $C_0$;
>
> **(d)** $P(r_0, r, \phi - \theta)$ is an even periodic function of $\phi - \theta$, with period $2\pi$;
>
> **(e)** $P(r_0, 0, \phi - \theta) = 1$;
>
> **(f)** $\displaystyle\frac{1}{2\pi}\int_0^{2\pi}P(r_0, r, \phi - \theta)\,d\phi = 1$.
>
> *B&C: Sec. 134 (text), properties (a)–(f)*

^prop-134-2

> [!proof]+ Proof
> **(a)** By (8), since $r < r_0$ makes the numerator positive and $s \ne z$.
>
> **(b)** Since $\overline z/(\overline s - \overline z)$ is the complex conjugate of $z/(s - z)$, the two have the same real part. By (8) and the second expression in (3),
>
> $$
> P = \operatorname{Re}\Big(\frac{s}{s - z} + \frac{\overline z}{\overline s - \overline z}\Big) = \operatorname{Re}\Big(\frac{s}{s - z} + \frac{z}{s - z}\Big) = \operatorname{Re}\frac{s + z}{s - z} .
> $$
>
> **(c)** For fixed $s$, $(s + z)/(s - z)$ is an analytic function of $z$ in $|z| < r_0$, and the real part of an analytic function is harmonic ([[§27★ Harmonic Functions#^thm-27-1|Theorem §27.1]]).
>
> **(d), (e)** Read off from (7): $\cos$ is even with period $2\pi$, and at $r = 0$ the fraction is $r_0^2/r_0^2$.
>
> **(f)** Apply (6) to $u \equiv 1$, the real part of $f \equiv 1$: the left side is $1$, and the right side is the mean of $P$ by (7).

^pf-134-2

*Uses:* [[§134★ Poisson Integral Formula#^thm-134-1|§134.1]], [[§134★ Poisson Integral Formula#^def-134-2|Def. §134.2]], [[§27★ Harmonic Functions#^thm-27-1|§27.1]]

> [!remark]- Connections
> - Properties (a), (e), (f) are [[§49 The Poisson Integral Formula and the Mean Value Property#^rem-49-2|341 Remark: The Poisson Kernel Is a Weight]]: the solution is a weighted average of the boundary values, which gives the maximum principle for the disk and, at $r = 0$, the mean value property [[§49 The Poisson Integral Formula and the Mean Value Property#^thm-49-2|341 Thm. §49.2]].

Formula (6) can now be written

$$
u(r, \theta) = \frac{1}{2\pi}\int_0^{2\pi}P(r_0, r, \phi - \theta)\,u(r_0, \phi)\,d\phi \qquad (r < r_0) . \qquad (9)
$$

So far $f$ has been assumed analytic on $C_0$ as well as inside, so that $u$ is harmonic in a domain including the circle and in particular continuous on it. These conditions are relaxed in [[§135★ Dirichlet Problem for a Disk|§135★]].

## Examples

> [!example] Example §134.1: The Mean Value at the Center
> Show that $\dfrac{1}{2\pi}\displaystyle\int_0^{2\pi}e^{\cos\phi}\cos(\sin\phi)\,d\phi = 1$.
>
> The function $u = e^x\cos y$ is the real part of the entire function $f(z) = e^z$. By (6) with $r = 0$ (where $P \equiv 1$ by property (e)) and $r_0 = 1$, $u(0, 0)$ is the mean of $u(1, \phi) = e^{\cos\phi}\cos(\sin\phi)$; and $u(0, 0) = e^0\cos0 = 1$. The value of a harmonic function at the center of a circle is the average of its values on the circle.
>
> *B&C: Sec. 134 (text), the case r = 0*

^ex-134-1

> [!example] Example §134.2: A Family of Trigonometric Integrals
> For $0 \le r < 1$ and $n = 0, 1, 2, \ldots$, show that
>
> $$
> \int_0^{2\pi}\frac{\cos n\phi}{1 - 2r\cos\phi + r^2}\,d\phi = \frac{2\pi r^n}{1 - r^2} .
> $$
>
> Apply (6) with $r_0 = 1$ to $u = \operatorname{Re} z^n = r^n\cos n\theta$, at the point $\theta = 0$:
>
> $$
> r^n = \frac{1}{2\pi}\int_0^{2\pi}\frac{(1 - r^2)\cos n\phi}{1 - 2r\cos\phi + r^2}\,d\phi ,
> $$
>
> which rearranges to the claim. For $n = 0$ this is property (f). Numerically, with $r = 0.6$, $n = 3$: both sides equal $2.1205750$ (quadrature and $2\pi(0.216)/0.64$).
>
> *B&C: Sec. 134, equation (6)*

^ex-134-2

> [!example] Example §134.3: Property (f) by Residues
> Check property (f) independently: for $0 \le r < r_0$,
>
> $$
> \int_0^{2\pi}\frac{d\phi}{r_0^2 - 2r_0r\cos\phi + r^2} = \frac{2\pi}{r_0^2 - r^2} .
> $$
>
> Use the method of [[§92★ Definite Integrals Involving Sines and Cosines#^prop-92-1|Proposition §92.1]]: put $z = e^{i\phi}$, $d\phi = dz/(iz)$, on the positively oriented unit circle $C$. The denominator factors as $r_0^2 - 2r_0r\cos\phi + r^2 = (r_0 - re^{i\phi})(r_0 - re^{-i\phi}) = (r_0 - rz)(r_0 - r/z)$, so
>
> $$
> \int_0^{2\pi}\frac{d\phi}{r_0^2 - 2r_0r\cos\phi + r^2} = \int_C\frac{dz}{i(r_0 - rz)(r_0z - r)} .
> $$
>
> The only singular point inside $C$ is the simple pole $z = r/r_0$, with residue $\dfrac{1}{i(r_0 - r^2/r_0)r_0} = \dfrac{1}{i(r_0^2 - r^2)}$ (the other pole, $z = r_0/r$, is outside). By the [[§76 Cauchy's Residue Theorem#^thm-76-1|residue theorem]] the integral is $2\pi i\cdot\frac{1}{i(r_0^2 - r^2)} = \frac{2\pi}{r_0^2 - r^2}$, and multiplying by $(r_0^2 - r^2)/(2\pi)$ gives property (f). The Poisson formula contains this residue computation: it is (6) for $u \equiv 1$.
>
> *B&C: Sec. 134, property (f)*

^ex-134-3
