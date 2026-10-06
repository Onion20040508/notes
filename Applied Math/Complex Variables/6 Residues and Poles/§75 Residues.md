---
type: section
subject: "[[Complex Variables]]"
chapter: 6
section: 75
bc: "75"
aliases: ["B&C 75"]
tags: [complex-variables, math342]
---
← [[§74 Isolated Singular Points]] · ↑ [[· 6 Residues and Poles]] · [[§76 Cauchy's Residue Theorem]] →

*Brown–Churchill, Section 75 · MAT 342 HW 11, Practice Final (Spring 2005).*

Near an isolated singular point $z_0$ a function has a Laurent series, and of all its coefficients one controls contour integrals: the coefficient $b_1$ of $1/(z - z_0)$, called the **residue**. By Laurent's coefficient formula, the integral of $f$ around any positively oriented simple closed contour that encloses $z_0$ and no other singular point is $2\pi i$ times the residue. So an integral is reduced to reading off one coefficient of a series, which is usually built from known Maclaurin series. This is the basic step of the residue theorem of [[§76 Cauchy's Residue Theorem|§76]] and of all the applications in Chapter 7.

## The Residue

When $z_0$ is an isolated singular point of $f$ ([[§74 Isolated Singular Points#^def-74-1|Definition §74.1]]), there is a positive number $R_2$ such that $f$ is analytic at each point $z$ with $0 < |z - z_0| < R_2$. Consequently (Laurent's theorem, [[§67 Proof of Laurent's Theorem#^thm-67-1|Theorem §67.1]], stated in [[§66 Laurent Series|§66]]) $f$ has a Laurent series representation

$$
f(z) = \sum_{n=0}^{\infty} a_n(z - z_0)^n + \frac{b_1}{z - z_0} + \frac{b_2}{(z - z_0)^2} + \cdots + \frac{b_n}{(z - z_0)^n} + \cdots \qquad (0 < |z - z_0| < R_2), \qquad (1)
$$

where in particular

$$
b_n = \frac{1}{2\pi i}\int_C \frac{f(z)\,dz}{(z - z_0)^{-n+1}} \qquad (n = 1, 2, \ldots)
$$

for any positively oriented simple closed contour $C$ around $z_0$ that lies in the punctured disk $0 < |z - z_0| < R_2$ (Fig. 90 in B&C).

> [!definition] Definition §75.1: Residue
> Let $z_0$ be an isolated singular point of $f$, with Laurent series (1) in $0 < |z - z_0| < R_2$. The coefficient $b_1$ of $1/(z - z_0)$ is called the **residue** of $f$ at $z_0$, written
>
> $$
> b_1 = \operatorname{Res}_{z=z_0} f(z) .
> $$
>
> When the function and the point are clearly indicated, the residue is sometimes denoted simply by $B$.
>
> *B&C: Sec. 75 (text)*

^def-75-1

> [!theorem] Theorem §75.1: An Integral Is 2πi Times a Residue
> Let $z_0$ be an isolated singular point of $f$, with $f$ analytic in $0 < |z - z_0| < R_2$, and let $C$ be a positively oriented [[§43 Contours#^def-43-new5|simple closed contour]] around $z_0$ lying in that punctured disk. Then
>
> $$
> \int_C f(z)\,dz = 2\pi i\operatorname{Res}_{z=z_0} f(z) . \qquad (3)
> $$
>
> *B&C: Sec. 75, Equations (2)–(3)*

^thm-75-1

> [!proof]+ Proof
> Put $n = 1$ in the coefficient formula of Laurent's theorem. Since $(z - z_0)^{-1+1} = 1$, it reads
>
> $$
> b_1 = \frac{1}{2\pi i}\int_C f(z)\,dz , \qquad\text{that is,}\qquad \int_C f(z)\,dz = 2\pi i\,b_1 , \qquad (2)
> $$
>
> and $b_1 = \operatorname{Res}_{z=z_0} f(z)$ by definition.

^pf-75-1

*Uses:* [[§75 Residues#^def-75-1|Def. §75.1]], [[§67 Proof of Laurent's Theorem#^thm-67-1|§67.1]] (Laurent's theorem, coefficient formula)

Equation (3) is a powerful method for evaluating integrals around simple closed contours: the whole integral is determined by a single coefficient.

> [!remark] Remark: Method — Computing a Residue from a Laurent Series
> 1. **Locate the singular point** $z_0$ and check that it is isolated; let $R_2$ be its distance to the nearest other singular point ($R_2 = \infty$ if there is none).
> 2. **Build the Laurent series** in $0 < |z - z_0| < R_2$ from known expansions ([[§64 Examples (Proof of Taylor's Theorem)|§64]]): $e^w$, $\sin w$, $\cos w$, $\cosh w$, $\sinh w$ and the geometric series ([[§61 Convergence of Series#^ex-61-1|Example §61.1]]) $\frac{1}{1 - w} = \sum w^n$ ($|w| < 1$), substituting $w = 1/z$, $w = z - z_0$, $w = -(z - z_0)/2$ and so on, and multiplying by powers of $z - z_0$. Any series in powers of $z - z_0$ that converges to $f$ in the punctured disk *is* its Laurent series ([[§72★ Uniqueness of Series Representations#^thm-72-4|Theorem §72.4]]), however it was found.
> 3. **Read off** the coefficient of $1/(z - z_0)$. Only the terms that can produce $(z - z_0)^{-1}$ need to be computed: if $f(z) = (z - z_0)^{-k}g(z)$, it is the coefficient of $(z - z_0)^{k-1}$ in $g$.
> 4. **Integrate.** If $C$ is positively oriented and encloses $z_0$ and no other singular point, $\int_C f(z)\,dz = 2\pi i\operatorname{Res}_{z=z_0} f(z)$ (Theorem §75.1). Several singular points inside $C$: [[§76 Cauchy's Residue Theorem#^thm-76-1|Theorem §76.1]].
>
> Faster rules at poles come in [[§80 Residues at Poles#^thm-80-1|Theorem §80.1]] and [[§83 Zeros and Poles#^thm-83-2|Theorem §83.2]]; the Laurent series is the method of last resort and the only one at [[§78 The Three Types of Isolated Singular Points#^def-78-3|essential singular points]].

^rem-75-1

## Examples

> [!example] Example §75.1: The Integral of (eᶻ − 1)/z⁵ Around the Unit Circle
> Evaluate
>
> $$
> \int_C \frac{e^z - 1}{z^5}\,dz , \qquad (4)
> $$
>
> where $C$ is the positively oriented unit circle $|z| = 1$ (Fig. 91 in B&C).
>
> The integrand is analytic everywhere in the finite plane except at $z = 0$, so it has a Laurent series valid in $0 < |z| < \infty$, and by (3) the integral is $2\pi i$ times its residue at $0$. From the Maclaurin series $e^z = \sum_{n=0}^{\infty} z^n/n!$ ($|z| < \infty$),
>
> $$
> \frac{e^z - 1}{z^5} = \frac{1}{z^5}\sum_{n=1}^{\infty}\frac{z^n}{n!} = \sum_{n=1}^{\infty}\frac{z^{n-5}}{n!} = \frac{1}{z^4} + \frac{1}{2!\,z^3} + \frac{1}{3!\,z^2} + \frac{1}{4!\,z} + \frac{1}{5!} + \cdots \qquad (0 < |z| < \infty) .
> $$
>
> The coefficient of $1/z$ occurs when $n - 5 = -1$, that is, $n = 4$. Hence
>
> $$
> \operatorname{Res}_{z=0}\frac{e^z - 1}{z^5} = \frac{1}{4!} = \frac{1}{24}, \qquad \int_C \frac{e^z - 1}{z^5}\,dz = 2\pi i\Big(\frac{1}{24}\Big) = \frac{\pi i}{12} .
> $$
>
> *B&C prints the integrand of (4) and of the final line as $(e^z - 1)/z^4$, but computes with $z^5$; for $(e^z - 1)/z^4$ the residue is $1/3! = 1/6$ and the integral is $\pi i/3$.*
>
> *B&C: Sec. 75, Example 1*

^ex-75-1

> [!example] Example §75.2: A Zero Integral Without Analyticity
> Show that
>
> $$
> \int_C \cosh\Big(\frac{1}{z^2}\Big)\,dz = 0 , \qquad (5)
> $$
>
> where $C$ is the positively oriented unit circle $|z| = 1$.
>
> The composite function $\cosh(1/z^2)$ is analytic everywhere except at the origin, since $1/z^2$ is and $\cosh z$ is entire; the isolated singular point $z = 0$ is interior to $C$. Substituting $1/z^2$ into the Maclaurin series $\cosh w = 1 + \frac{w^2}{2!} + \frac{w^4}{4!} + \frac{w^6}{6!} + \cdots$ ($|w| < \infty$) gives the Laurent series
>
> $$
> \cosh\Big(\frac{1}{z^2}\Big) = 1 + \frac{1}{2!}\cdot\frac{1}{z^4} + \frac{1}{4!}\cdot\frac{1}{z^8} + \frac{1}{6!}\cdot\frac{1}{z^{12}} + \cdots \qquad (0 < |z| < \infty) .
> $$
>
> It contains no term in $1/z$, so the residue at $z = 0$ is zero ($b_1 = 0$), and (5) follows from (3).
>
> The example is a reminder that analyticity of a function within and on a simple closed contour is a *sufficient* condition for its integral around the contour to be zero ([[§51 Proof of the Theorem (Cauchy–Goursat Theorem)#^thm-51-3|Theorem §51.3]]), not a *necessary* one.
>
> *B&C: Sec. 75, Example 2*

^ex-75-2

> [!example] Example §75.3: A Residue from the Geometric Series
> Evaluate
>
> $$
> \int_C \frac{dz}{z(z - 2)^5} , \qquad (6)
> $$
>
> where $C$ is the positively oriented circle $|z - 2| = 1$ (Fig. 92 in B&C).
>
> The integrand is analytic everywhere in the finite plane except at $z = 0$ and $z = 2$. Only $z = 2$ lies inside $C$, and the integrand has a Laurent series in the punctured disk $0 < |z - 2| < 2$, which contains $C$. So by (3) the integral is $2\pi i$ times the residue at $z = 2$. To find it, write the factor $1/z$ in powers of $z - 2$ and use the geometric series:
>
> $$
> \frac{1}{z(z - 2)^5} = \frac{1}{(z - 2)^5}\cdot\frac{1}{2 + (z - 2)} = \frac{1}{2(z - 2)^5}\cdot\frac{1}{1 - \big(-\frac{z - 2}{2}\big)} = \frac{1}{2(z - 2)^5}\sum_{n=0}^{\infty}\Big(-\frac{z - 2}{2}\Big)^n = \sum_{n=0}^{\infty}\frac{(-1)^n}{2^{n+1}}(z - 2)^{n-5} ,
> $$
>
> valid for $0 < |z - 2| < 2$ (where $|(z - 2)/2| < 1$). The coefficient of $1/(z - 2)$ comes from $n = 4$: it is $\frac{(-1)^4}{2^5} = \frac{1}{32}$. Consequently
>
> $$
> \int_C \frac{dz}{z(z - 2)^5} = 2\pi i\Big(\frac{1}{32}\Big) = \frac{\pi i}{16} .
> $$
>
> *B&C: Sec. 75, Example 3*

^ex-75-3

*Chain (the geometric series): earlier in [[§73a The Geometric Series|Chapter 5]] · later in [[§135★ Dirichlet Problem for a Disk|Chapter 12]]*

> [!example] Example §75.4: Three Residues at the Origin
> Find the residue at $z = 0$ of
>
> $$
> \text{(a)}\ \frac{1}{z + z^2}; \qquad \text{(b)}\ z\cos\Big(\frac1z\Big); \qquad \text{(c)}\ \frac{z - \sin z}{z} .
> $$
>
> **(a)** The singular points are $0$ and $-1$, so the Laurent series about $0$ is valid in $0 < |z| < 1$. By the geometric series,
>
> $$
> \frac{1}{z + z^2} = \frac1z\cdot\frac{1}{1 + z} = \frac1z\sum_{n=0}^{\infty}(-1)^nz^n = \sum_{n=0}^{\infty}(-1)^nz^{n-1} = \frac1z - 1 + z - z^2 + \cdots ,
> $$
>
> and the coefficient of $1/z$ ($n = 0$) is $\operatorname{Res}_{z=0}\frac{1}{z + z^2} = 1$.
>
> **(b)** With $\cos w = \sum_{n=0}^{\infty}\frac{(-1)^n}{(2n)!}w^{2n}$ and $w = 1/z$,
>
> $$
> z\cos\Big(\frac1z\Big) = \sum_{n=0}^{\infty}\frac{(-1)^n}{(2n)!}z^{1-2n} = z - \frac{1}{2!}\cdot\frac1z + \frac{1}{4!}\cdot\frac{1}{z^3} - \cdots \qquad (0 < |z| < \infty) .
> $$
>
> The term $z^{-1}$ comes from $1 - 2n = -1$, that is, $n = 1$, so $\operatorname{Res}_{z=0} z\cos(1/z) = -\frac{1}{2}$.
>
> **(c)** With $\sin z = \sum_{n=0}^{\infty}\frac{(-1)^n}{(2n+1)!}z^{2n+1}$,
>
> $$
> \frac{z - \sin z}{z} = 1 - \frac{\sin z}{z} = 1 - \sum_{n=0}^{\infty}\frac{(-1)^n}{(2n+1)!}z^{2n} = \frac{z^2}{3!} - \frac{z^4}{5!} + \cdots \qquad (0 < |z| < \infty) .
> $$
>
> There is no term in $z^{-1}$ (in fact no negative power at all), so $\operatorname{Res}_{z=0}\frac{z - \sin z}{z} = 0$.
>
> *B&C: Sec. 77, Exercise 1(a)–(c); Source: 342 HW 11*

^ex-75-4

The same reading-off of one coefficient settles a final-exam integral, $\frac{1}{2\pi i}\int_C\big(\frac{1}{z^2} + z + z^3\big)e^{1/z}\,dz = \frac{1}{2!} + \frac{1}{4!} = \frac{13}{24}$ over the unit circle, worked in [[§68 Examples (Proof of Laurent's Theorem)#^ex-68-4|Example §68.4]](b).

> [!remark] Remark: Derivatives Have Zero Residue
> If $F$ is analytic in a punctured disk $0 < |z - z_0| < R$, then $f = F'$ has residue $0$ at $z_0$. Indeed, let $C$ be the circle $|z - z_0| = r$ with $0 < r < R$. Since $F$ is an antiderivative of $f$ in a domain containing $C$, the integral of $f$ around the closed contour $C$ is zero ([[§49 Proof of the Theorem (Antiderivatives)#^thm-49-1|Theorem §49.1]]), so $\operatorname{Res}_{z=z_0} f(z) = \frac{1}{2\pi i}\int_C f(z)\,dz = 0$ by (3). (In terms of series: differentiating the Laurent series of $F$ term by term, $\frac{d}{dz}(z - z_0)^n = n(z - z_0)^{n-1}$, and the power $-1$ would come only from $n = 0$, whose coefficient $n$ is $0$.) For instance, there is **no** function $F$ analytic in $0 < |z| < 1$ with $\operatorname{Res}_{z=0} F'(z) = 1$: $1/z$ has no antiderivative in the punctured disk, which is why $\log z$ needs a branch cut ([[§33 Branches and Derivatives of Logarithms#^def-33-3|Definition §33.3]]).
>
> *Source: 342 practice final (Spring 2005), Q8(b)*

^rem-75-2
