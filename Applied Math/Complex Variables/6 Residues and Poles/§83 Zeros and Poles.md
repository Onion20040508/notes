---
type: section
subject: "[[Complex Variables]]"
chapter: 6
section: 83
bc: "83"
aliases: ["B&C 83"]
tags: [complex-variables, math342]
---
← [[§82 Zeros of Analytic Functions]] · ↑ [[· 6 Residues and Poles]] · [[§84 Behavior of Functions Near Isolated Singular Points]] →

*Brown–Churchill, Section 83 · MAT 342 HW 12.*

Most poles met in practice come from zeros of a denominator. If $p$ and $q$ are analytic at $z_0$, $p(z_0) \ne 0$ and $q$ has a zero of order $m$ at $z_0$, then $p/q$ has a pole of order $m$ there (Theorem 1), and conversely. For a simple zero of $q$ this gives the most convenient residue formula of all, $\operatorname{Res}_{z=z_0} p/q = p(z_0)/q'(z_0)$ (Theorem 2), which needs no factorization of $q$. It handles $\cot z$, $\tan z$, $1/\sin z$ and the roots of polynomials at once, and with the residue theorem it evaluates integrals such as the one that sums $\sum(-1)^{n+1}/n^2 = \pi^2/12$.

## Zeros of the Denominator

> [!theorem] Theorem §83.1: A Zero of Order m in the Denominator Is a Pole of Order m
> Suppose that
>
> **(a)** two functions $p$ and $q$ are analytic at a point $z_0$;
>
> **(b)** $p(z_0) \ne 0$ and $q$ has a zero of order $m$ at $z_0$.
>
> Then the quotient $p(z)/q(z)$ has a pole of order $m$ at $z_0$.
>
> *B&C: Sec. 83, Theorem 1*

^thm-83-1

> [!proof]+ Proof
> Let $p$ and $q$ be as in the statement. Since $q$ has a zero of order $m$ at $z_0$, Theorem 1 of §82 ([[§82 Zeros of Analytic Functions#^thm-82-1|Theorem §82.1]]) tells us that
>
> $$
> q(z) = (z - z_0)^mg(z) ,
> $$
>
> where $g$ is analytic and nonzero at $z_0$. In particular $q$ is not identically zero near $z_0$, so by [[§82 Zeros of Analytic Functions#^thm-82-2|Theorem §82.2]] there is a deleted neighborhood of $z_0$ throughout which $q(z) \ne 0$; there $p/q$ is analytic, while at $z_0$ it is not even defined. So $z_0$ is an isolated singular point of the quotient $p(z)/q(z)$. Consequently
>
> $$
> \frac{p(z)}{q(z)} = \frac{\phi(z)}{(z - z_0)^m} \qquad\text{where}\qquad \phi(z) = \frac{p(z)}{g(z)} . \qquad (1)
> $$
>
> Since $g$ is continuous and nonzero at $z_0$, it is nonzero in a neighborhood of $z_0$ ([[§18 Continuity#^thm-18-3|Theorem §18.3]]), so $\phi$ is analytic at $z_0$; and $\phi(z_0) = p(z_0)/g(z_0) \ne 0$. It now follows from the theorem in §80 ([[§80 Residues at Poles#^thm-80-1|Theorem §80.1]]) that $z_0$ is a pole of order $m$ of $p(z)/q(z)$.

^pf-83-1

*Uses:* [[§82 Zeros of Analytic Functions#^thm-82-1|§82.1]], [[§82 Zeros of Analytic Functions#^thm-82-2|§82.2]], [[§80 Residues at Poles#^thm-80-1|§80.1]], [[§18 Continuity#^thm-18-3|§18.3]] (nonzero near a point where continuous and nonzero)

> [!example] Example §83.1: A Double Pole of 1/(1 − cos z)
> The two functions
>
> $$
> p(z) = 1 \qquad\text{and}\qquad q(z) = 1 - \cos z
> $$
>
> are entire, and $q$ has a zero of order $m = 2$ at the point $z_0 = 0$ ([[§82 Zeros of Analytic Functions#^ex-82-2|Example §82.2]]). Since $p(0) = 1 \ne 0$, it follows from Theorem §83.1 that the quotient
>
> $$
> \frac{p(z)}{q(z)} = \frac{1}{1 - \cos z}
> $$
>
> has a pole of order $m = 2$ at that point. (Its Laurent series begins $\frac{2}{z^2} + \frac16 + \cdots$, so the residue there is $0$.)
>
> *B&C: Sec. 83, Example 1*

^ex-83-1

## Residues at Simple Poles of Quotients

Theorem §83.1 leads to another method for identifying *simple* poles and finding the corresponding residues. It is sometimes easier to use than the theorem in §80.

> [!theorem] Theorem §83.2: Residue of p/q at a Simple Zero of q
> Let two functions $p$ and $q$ be analytic at a point $z_0$. If
>
> $$
> p(z_0) \ne 0, \qquad q(z_0) = 0, \qquad\text{and}\qquad q'(z_0) \ne 0,
> $$
>
> then $z_0$ is a simple pole of the quotient $p(z)/q(z)$ and
>
> $$
> \operatorname{Res}_{z=z_0}\frac{p(z)}{q(z)} = \frac{p(z_0)}{q'(z_0)} . \qquad (2)
> $$
>
> *B&C: Sec. 83, Theorem 2*

^thm-83-2

> [!proof]+ Proof
> Assume that $p$ and $q$ are as stated, and observe that because of the conditions on $q$, the point $z_0$ is a zero of order $m = 1$ of that function ([[§82 Zeros of Analytic Functions#^def-82-1|Definition §82.1]]). According to Theorem 1 in §82, then,
>
> $$
> q(z) = (z - z_0)g(z) , \qquad (3)
> $$
>
> where $g$ is analytic and nonzero at $z_0$. Furthermore, Theorem §83.1 tells us that $z_0$ is a simple pole of $p/q$, and expression (1) in its proof becomes
>
> $$
> \frac{p(z)}{q(z)} = \frac{\phi(z)}{z - z_0} \qquad\text{where}\qquad \phi(z) = \frac{p(z)}{g(z)} .
> $$
>
> Since this $\phi$ is analytic and nonzero at $z_0$, the theorem in §80 gives
>
> $$
> \operatorname{Res}_{z=z_0}\frac{p(z)}{q(z)} = \frac{p(z_0)}{g(z_0)} . \qquad (4)
> $$
>
> But $g(z_0) = q'(z_0)$, as is seen by differentiating each side of equation (3), $q'(z) = g(z) + (z - z_0)g'(z)$, and then setting $z = z_0$. Expression (4) thus takes the form (2).

^pf-83-2

*Uses:* [[§82 Zeros of Analytic Functions#^def-82-1|Def. §82.1]], [[§82 Zeros of Analytic Functions#^thm-82-1|§82.1]], [[§83 Zeros and Poles#^thm-83-1|§83.1]], [[§80 Residues at Poles#^thm-80-1|§80.1]]

> [!remark]- Connections
> - For polynomials this is Heaviside's formula of Fourier Series and PDEs, [[§52★ Partial Fractions and Convolutions#^thm-52-2|341 Thm. §52.2]]: the coefficient of $1/(s - r_k)$ in the partial-fraction expansion of $q/p$ is $q(r_k)/p'(r_k)$, the residue at the simple pole $r_k$. The partial-fraction decomposition itself, [[§47 Integration of Rational Functions by Partial Fractions#^thm-47-3|Calc Thm. §47.3]], follows from principal parts and Liouville's theorem (Connections of [[§78 The Three Types of Isolated Singular Points#^def-78-1|Definition §78.1]]).

There are expressions similar to (2) for residues at poles of higher order, but they are lengthier and, in general, not practical. (For a double pole of $1/q^2$, where $q$ has a simple zero, B&C's Exercise 8 gives $\operatorname{Res} = -q''(z_0)/[q'(z_0)]^3$.)

> [!remark] Remark: Method — Residues of Quotients
> 1. **Write $f = p/q$** with $p$, $q$ analytic at $z_0$ (often entire), and find the zeros of $q$.
> 2. **Check the conditions** $p(z_0) \ne 0$, $q(z_0) = 0$, $q'(z_0) \ne 0$. Then $z_0$ is a simple pole and $\operatorname{Res}_{z=z_0} f = p(z_0)/q'(z_0)$ (Theorem §83.2). No factoring of $q$ is needed, which is the point for $\sin z$, $\cosh z$, $z^n - c$.
> 3. **Higher-order zeros.** If $q$ has a zero of order $m \ge 2$ and $p(z_0) \ne 0$, the pole has order $m$ (Theorem §83.1); find the residue by [[§80 Residues at Poles#^thm-80-1|Theorem §80.1]] or a Laurent series.
> 4. **Common zeros.** If $p(z_0) = 0$ too, compare orders: with $p$ of order $k$ and $q$ of order $m$, $p/q = (z - z_0)^{k-m}\cdot(\text{analytic, nonzero})$, so the point is removable if $k \ge m$ and a pole of order $m - k$ if $k < m$ (Theorem §82.1).

^rem-83-1

The converse of Theorem §83.1 also holds: a pole of the quotient comes from a zero of the same order.

> [!theorem] Proposition §83.3: A Pole of Order m Comes From a Zero of Order m
> Let $p$ and $q$ be analytic at a point $z_0$, with $p(z_0) \ne 0$ and $q(z_0) = 0$. If the quotient $p(z)/q(z)$ has a pole of order $m$ at $z_0$, then $z_0$ is a zero of order $m$ of $q$.
>
> *B&C: Sec. 83, Exercise 10; Source: 342 HW 12*

^prop-83-3

> [!proof]+ Proof
> By [[§80 Residues at Poles#^thm-80-1|Theorem §80.1]] we can write
>
> $$
> \frac{p(z)}{q(z)} = \frac{\phi(z)}{(z - z_0)^m}
> $$
>
> in some deleted neighborhood $0 < |z - z_0| < \varepsilon$, where $\phi$ is analytic and nonzero at $z_0$. Shrinking $\varepsilon$, we may assume that $p$ and $\phi$ are analytic and nonzero in the whole disk $|z - z_0| < \varepsilon$ (they are continuous and nonzero at $z_0$). Solving for $q$,
>
> $$
> q(z) = (z - z_0)^m\,g(z), \qquad g(z) = \frac{p(z)}{\phi(z)} \qquad (0 < |z - z_0| < \varepsilon) .
> $$
>
> The function $g$ is analytic in the disk and $g(z_0) = p(z_0)/\phi(z_0) \ne 0$. At $z = z_0$ both sides of the equation are $0$, since $q(z_0) = 0$ and $m \ge 1$; so $q(z) = (z - z_0)^mg(z)$ throughout $|z - z_0| < \varepsilon$. By [[§82 Zeros of Analytic Functions#^thm-82-1|Theorem §82.1]], $q$ has a zero of order $m$ at $z_0$.

^pf-83-3

*Uses:* [[§80 Residues at Poles#^thm-80-1|§80.1]], [[§82 Zeros of Analytic Functions#^thm-82-1|§82.1]], [[§18 Continuity#^thm-18-3|§18.3]]

## Examples

> [!example] Example §83.2: Residues of cot z, a Hyperbolic Quotient, and z/(z⁴ + 4)
> **(a)** Consider
>
> $$
> f(z) = \cot z = \frac{\cos z}{\sin z} ,
> $$
>
> a quotient of the entire functions $p(z) = \cos z$ and $q(z) = \sin z$. Its singularities occur at the zeros of $q$, the points $z = n\pi$ ($n = 0, \pm1, \pm2, \ldots$) ([[§38 Zeros and Singularities of Trigonometric Functions#^thm-38-1|Theorem §38.1]]). Since
>
> $$
> p(n\pi) = (-1)^n \ne 0, \qquad q(n\pi) = 0, \qquad q'(n\pi) = \cos n\pi = (-1)^n \ne 0,
> $$
>
> Theorem §83.2 tells us that each singular point $z = n\pi$ of $f$ is a simple pole, with residue
>
> $$
> B_n = \frac{p(n\pi)}{q'(n\pi)} = \frac{(-1)^n}{(-1)^n} = 1 .
> $$
>
> **(b)** The residue of
>
> $$
> f(z) = \frac{z - \sinh z}{z^2\sinh z}
> $$
>
> at the zero $z = \pi i$ of $\sinh z$ ([[§39★ Hyperbolic Functions#^thm-39-4|Theorem §39.4]]) is found by writing $p(z) = z - \sinh z$ and $q(z) = z^2\sinh z$. Since $\sinh(\pi i) = i\sin\pi = 0$ and $\cosh(\pi i) = \cos\pi = -1$,
>
> $$
> p(\pi i) = \pi i \ne 0, \qquad q(\pi i) = 0, \qquad q'(\pi i) = \big[2z\sinh z + z^2\cosh z\big]_{z=\pi i} = (\pi i)^2(-1) = \pi^2 \ne 0 .
> $$
>
> So $z = \pi i$ is a simple pole of $f$, and the residue there is
>
> $$
> B = \frac{p(\pi i)}{q'(\pi i)} = \frac{\pi i}{\pi^2} = \frac i\pi .
> $$
>
> **(c)** The point $z_0 = \sqrt2e^{i\pi/4} = 1 + i$ is a zero of the polynomial $z^4 + 4$ ([[§11 Examples (Roots of Complex Numbers)#^ex-11-5|Example §11.5]]), hence an isolated singularity of
>
> $$
> f(z) = \frac{z}{z^4 + 4} .
> $$
>
> Writing $p(z) = z$ and $q(z) = z^4 + 4$: $p(z_0) = z_0 \ne 0$, $q(z_0) = 0$ and $q'(z_0) = 4z_0^3 \ne 0$. Theorem §83.2 shows that $z_0$ is a simple pole of $f$, and since $z_0^2 = (1 + i)^2 = 2i$,
>
> $$
> B_0 = \frac{p(z_0)}{q'(z_0)} = \frac{z_0}{4z_0^3} = \frac{1}{4z_0^2} = \frac{1}{8i} = -\frac i8 .
> $$
>
> This residue can also be found by the method of §80 (factoring $z^4 + 4$ into four linear factors), but the computation is somewhat more involved.
>
> *B&C: Sec. 83, Examples 2, 3 and 4*

^ex-83-2

> [!example] Example §83.3: Poles, Residues and Zeros of z/sin z and z²/(z⁴ + 9)
> For each function, find all the poles and the residue at each pole, and all the zeros with their orders.
>
> **(a) $f(z) = \dfrac{z}{\sin z}$.** The zeros of $\sin z$ are $z = n\pi$ ($n \in \mathbb{Z}$).
> - *At $z = 0$* the numerator vanishes too: $\frac{z}{\sin z} = \frac{1}{1 - z^2/3! + z^4/5! - \cdots}$, which tends to $1$; equivalently, by the Laurent series of $1/\sin z$ in [[§73★ Multiplication and Division of Power Series#^ex-73-3|Example §73.3]], $\frac{z}{\sin z} = 1 + \frac{z^2}{6} + \frac{7z^4}{360} + \cdots$. So $0$ is a **removable** singular point, not a pole; with $f(0) = 1$ the function is analytic there.
> - *At $z = n\pi$, $n \ne 0$*: $p(z) = z$ has $p(n\pi) = n\pi \ne 0$, and $q(z) = \sin z$ has $q'(n\pi) = \cos n\pi = (-1)^n \ne 0$. By Theorem §83.2 these are **simple poles**, with
>
> $$
> \operatorname{Res}_{z=n\pi}\frac{z}{\sin z} = \frac{n\pi}{\cos n\pi} = (-1)^nn\pi \qquad (n = \pm1, \pm2, \ldots) .
> $$
>
> - *Zeros.* $f(z) = 0$ would need $z = 0$, but there $f(0) = 1$ (after the removal). So $f$ has **no zeros**.
>
> **(b) $g(z) = \dfrac{z^2}{z^4 + 9}$.** The zeros of $z^4 + 9$ are the fourth roots of $-9 = 9e^{i\pi}$ ([[§10 Roots of Complex Numbers#^thm-10-2|Theorem §10.2]]):
>
> $$
> z_k = \sqrt3\,e^{i(\pi/4 + k\pi/2)} \qquad (k = 0, 1, 2, 3), \qquad\text{that is,}\qquad z_k = \sqrt{\tfrac32}\,(\pm1 \pm i) .
> $$
>
> - *Poles.* With $p(z) = z^2$ and $q(z) = z^4 + 9$: $p(z_k) \ne 0$ and $q'(z_k) = 4z_k^3 \ne 0$, so each $z_k$ is a **simple pole**, with
>
> $$
> \operatorname{Res}_{z=z_k} g = \frac{z_k^2}{4z_k^3} = \frac{1}{4z_k} = \frac{\bar z_k}{4|z_k|^2} = \frac{\bar z_k}{12} = \frac{e^{-i(\pi/4 + k\pi/2)}}{4\sqrt3} .
> $$
>
> Explicitly, at $\sqrt{3/2}(1 + i)$, $\sqrt{3/2}(-1 + i)$, $\sqrt{3/2}(-1 - i)$, $\sqrt{3/2}(1 - i)$ the residues are $\frac{1 - i}{4\sqrt6}$, $\frac{-1 - i}{4\sqrt6}$, $\frac{-1 + i}{4\sqrt6}$, $\frac{1 + i}{4\sqrt6}$ (using $\sqrt{3/2}/12 = 1/(4\sqrt6)$).
> - *Zeros.* $g(z) = z^2\cdot\frac{1}{z^4 + 9}$, where $\frac{1}{z^4 + 9}$ is analytic at $0$ with value $\frac19 \ne 0$. By Theorem §82.1, $z = 0$ is a **zero of order $2$**, and it is the only zero.
>
> *Source: 342 HW 12, Problem 1*

^ex-83-3

> [!example] Example §83.4: An Integral Around a Rectangle
> Show that
>
> $$
> \int_C \frac{dz}{(z^2 - 1)^2 + 3} = \frac{\pi}{2\sqrt2} ,
> $$
>
> where $C$ is the positively oriented boundary of the rectangle whose sides lie along the lines $x = \pm2$, $y = 0$ and $y = 1$.
>
> **The singular points.** The four zeros of $q(z) = (z^2 - 1)^2 + 3$ satisfy $z^2 - 1 = \pm\sqrt3\,i$, that is, they are the square roots of $1 \pm \sqrt3\,i = 2e^{\pm i\pi/3}$:
>
> $$
> \pm\sqrt2\,e^{i\pi/6} = \pm\frac{\sqrt3 + i}{\sqrt2}, \qquad \pm\sqrt2\,e^{-i\pi/6} = \pm\frac{\sqrt3 - i}{\sqrt2} .
> $$
>
> Of these, $z_0 = \frac{\sqrt3 + i}{\sqrt2} \approx 1.22 + 0.71i$ and $-\bar z_0 = \frac{-\sqrt3 + i}{\sqrt2}$ lie inside $C$ ($|x| < 2$, $0 < y < 1$); the other two have $y < 0$. So $1/q$ is analytic inside and on $C$ except at $z_0$ and $-\bar z_0$ (figure below).
>
> **The residues.** With $p = 1$ and $q'(z) = 4z(z^2 - 1)$: at $z_0$, $z_0^2 - 1 = \sqrt3\,i$, so $q'(z_0) = 4\sqrt3\,i\,z_0 \ne 0$; at $-\bar z_0$, $(-\bar z_0)^2 - 1 = \bar z_0^2 - 1 = -\sqrt3\,i$, so $q'(-\bar z_0) = 4\sqrt3\,i\,\bar z_0 \ne 0$. Both are simple poles, and by Theorem §83.2
>
> $$
> \operatorname{Res}_{z=z_0}\frac1q + \operatorname{Res}_{z=-\bar z_0}\frac1q = \frac{1}{4\sqrt3\,i}\Big(\frac{1}{z_0} + \frac{1}{\bar z_0}\Big) = \frac{1}{4\sqrt3\,i}\cdot\frac{2\operatorname{Re}z_0}{|z_0|^2} = \frac{1}{4\sqrt3\,i}\cdot\frac{2\sqrt3/\sqrt2}{2} = \frac{1}{4\sqrt2\,i} .
> $$
>
> **The integral.** By the residue theorem,
>
> $$
> \int_C \frac{dz}{(z^2 - 1)^2 + 3} = 2\pi i\cdot\frac{1}{4\sqrt2\,i} = \frac{\pi}{2\sqrt2} \approx 1.1107 ,
> $$
>
> which agrees with direct numerical integration along the four sides.
>
> *B&C: Sec. 83, Exercise 7; Source: 342 HW 12*

^ex-83-4

![[m342-83-2.svg]]
*The rectangle of Example §83.4 and the four zeros of $(z^2 - 1)^2 + 3$, which lie on the circle $|z| = \sqrt2$ at angles $\pm\frac\pi6$ and $\pi \pm \frac\pi6$. Only the two in the upper half plane, $z_0$ and $-\bar z_0$ (filled), are inside the contour; their residues are reflections of each other, and their sum is purely imaginary.*

> [!example] Example §83.5: The Sum of (−1)ⁿ⁺¹/n² by Residues
> Let $C_N$ denote the positively oriented boundary of the square whose edges lie along the lines
>
> $$
> x = \pm\Big(N + \frac12\Big)\pi \qquad\text{and}\qquad y = \pm\Big(N + \frac12\Big)\pi ,
> $$
>
> where $N$ is a positive integer. Show that
>
> $$
> \int_{C_N}\frac{dz}{z^2\sin z} = 2\pi i\Big[\frac16 + 2\sum_{n=1}^{N}\frac{(-1)^n}{n^2\pi^2}\Big] ,
> $$
>
> and deduce from the fact that the integral tends to zero as $N \to \infty$ that $\displaystyle\sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{n^2} = \frac{\pi^2}{12}$.
>
> **The poles inside $C_N$.** The singular points of $f(z) = \frac{1}{z^2\sin z}$ are the zeros $z = n\pi$ of $z^2\sin z$; those inside $C_N$ are $n = 0, \pm1, \ldots, \pm N$, since $(N + 1)\pi > (N + \frac12)\pi$.
>
> **At $z = n\pi$, $n \ne 0$.** With $p = 1$ and $q(z) = z^2\sin z$, $q'(z) = 2z\sin z + z^2\cos z$ and $q'(n\pi) = n^2\pi^2(-1)^n \ne 0$. By Theorem §83.2 these are simple poles, with
>
> $$
> \operatorname{Res}_{z=n\pi}\frac{1}{z^2\sin z} = \frac{1}{n^2\pi^2(-1)^n} = \frac{(-1)^n}{n^2\pi^2} ,
> $$
>
> the same value for $n$ and $-n$.
>
> **At $z = 0$** $q$ has a zero of order $3$, and the residue comes from the Laurent series of $1/\sin z$ in [[§73★ Multiplication and Division of Power Series#^ex-73-3|Example §73.3]],
>
> $$
> \frac{1}{z^2\sin z} = \frac{1}{z^2}\Big(\frac1z + \frac z6 + \frac{7z^3}{360} + \cdots\Big) = \frac{1}{z^3} + \frac16\cdot\frac1z + \frac{7z}{360} + \cdots ,
> $$
>
> so $\operatorname{Res}_{z=0} f = \frac16$ (a pole of order $3$).
>
> **The integral.** By the residue theorem,
>
> $$
> \int_{C_N}\frac{dz}{z^2\sin z} = 2\pi i\Big[\frac16 + \sum_{\substack{n=-N\\ n\ne0}}^{N}\frac{(-1)^n}{n^2\pi^2}\Big] = 2\pi i\Big[\frac16 + 2\sum_{n=1}^{N}\frac{(-1)^n}{n^2\pi^2}\Big] .
> $$
>
> (For $N = 3$ both sides equal $-0.04920\ldots\,i$; the left side was checked by numerical integration around the square.)
>
> **The integral tends to $0$.** (B&C refers to Exercise 8 of [[§47 Upper Bounds for Moduli of Contour Integrals|§47]]; here is the estimate.) Since $|\sin z|^2 = \sin^2x + \sinh^2y$ ([[§37 The Trigonometric Functions sin z and cos z#^prop-37-6|Proposition §37.6]]), on the vertical sides $x = \pm(N + \frac12)\pi$ we have $|\sin z| \ge |\sin x| = 1$, and on the horizontal sides $|\sin z| \ge |\sinh y| = \sinh\big((N + \frac12)\pi\big) > 1$. Also $|z| \ge (N + \frac12)\pi$ on $C_N$. Hence $|f(z)| \le \frac{1}{(N + \frac12)^2\pi^2}$ on $C_N$, whose length is $8(N + \frac12)\pi$, and by the ML-inequality ([[§47 Upper Bounds for Moduli of Contour Integrals#^thm-47-2|Theorem §47.2]])
>
> $$
> \Big|\int_{C_N}\frac{dz}{z^2\sin z}\Big| \le \frac{8(N + \frac12)\pi}{(N + \frac12)^2\pi^2} = \frac{8}{(N + \frac12)\pi} \longrightarrow 0 \qquad (N \to \infty) .
> $$
>
> **The sum.** Letting $N \to \infty$, the bracket tends to $0$:
>
> $$
> \frac16 + \frac{2}{\pi^2}\sum_{n=1}^{\infty}\frac{(-1)^n}{n^2} = 0, \qquad\text{so}\qquad \sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{n^2} = \frac{\pi^2}{12} .
> $$
>
> *B&C: Sec. 83, Exercise 6; Source: 342 HW 12*

^ex-83-5

![[m342-83-1.svg]]
*The square $C_N$ of Example §83.5 for $N = 2$. Its sides pass midway between consecutive poles $n\pi$ of $1/(z^2\sin z)$, so it encloses exactly the poles $n = 0, \pm1, \ldots, \pm N$ (filled) and stays away from all of them, which keeps $|\sin z| \ge 1$ on the contour. As $N$ grows the integral tends to $0$, while the enclosed residues build up the alternating series.*
