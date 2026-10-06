---
type: section
subject: "[[Complex Variables]]"
chapter: 6
section: 81
bc: "81"
aliases: ["B&C 81"]
tags: [complex-variables, math342]
---
← [[§80 Residues at Poles]] · ↑ [[· 6 Residues and Poles]] · [[§82 Zeros of Analytic Functions]] →

*Brown–Churchill, Section 81 · MAT 342 HW 11, Practice Finals (Fall 2002, Fall 2009).*

The examples show the theorem of [[§80 Residues at Poles#^thm-80-1|§80]] at work: write $f = \phi/(z - z_0)^m$ with $\phi$ analytic and nonzero at $z_0$, and the residue is $\phi(z_0)$ or $\phi^{(m-1)}(z_0)/(m-1)!$. The method applies equally to branches of multiple-valued functions, as long as $z_0$ is off the branch cut. Two cautionary examples show when it must not be used: if $\phi(z_0) = 0$ the pole has lower order than it seems, and if $\phi$ is not defined at $z_0$ there is no such factorization; in both cases a few terms of the Laurent series settle the matter. The last two examples, from the course, combine the method with the residue theorem.

## The Theorem at Work

> [!example] Example §81.1: Simple Poles and a Pole of Order Three
> **(a)** The function
>
> $$
> f(z) = \frac{z + 4}{z^2 + 1}
> $$
>
> has an isolated singular point at $z = i$ and can be written
>
> $$
> f(z) = \frac{\phi(z)}{z - i} \qquad\text{where}\qquad \phi(z) = \frac{z + 4}{z + i} .
> $$
>
> Since $\phi$ is analytic at $z = i$ and $\phi(i) \ne 0$, that point is a simple pole of $f$, and the residue there is
>
> $$
> B_1 = \phi(i) = \frac{i + 4}{2i}\cdot\frac ii = \frac{-1 + 4i}{-2} = \frac12 - 2i .
> $$
>
> The point $z = -i$ is also a simple pole of $f$: with $\phi(z) = \frac{z + 4}{z - i}$ there, the residue is
>
> $$
> B_2 = \frac{-i + 4}{-2i}\cdot\frac ii = \frac{1 + 4i}{2} = \frac12 + 2i .
> $$
>
> **(b)** If
>
> $$
> f(z) = \frac{z^3 + 2z}{(z - i)^3} ,
> $$
>
> then $f(z) = \phi(z)/(z - i)^3$ where $\phi(z) = z^3 + 2z$. The function $\phi$ is entire, and $\phi(i) = -i + 2i = i \ne 0$. Hence $f$ has a pole of order $3$ at $z = i$, with residue
>
> $$
> B = \frac{\phi''(i)}{2!} = \frac{6i}{2!} = 3i .
> $$
>
> *B&C: Sec. 81, Examples 1 and 2*

^ex-81-1

The theorem can, of course, be used when branches of multiple-valued functions are involved.

> [!example] Example §81.2: A Residue Involving a Branch of log z
> Suppose that
>
> $$
> f(z) = \frac{(\log z)^3}{z^2 + 1} ,
> $$
>
> where the branch
>
> $$
> \log z = \ln r + i\theta \qquad (r > 0,\ 0 < \theta < 2\pi)
> $$
>
> of the logarithmic function is to be used ([[§33 Branches and Derivatives of Logarithms#^def-33-1|Definition §33.1]]). This branch is analytic off the nonnegative real axis, so $f$ is analytic there except at $\pm i$. To find the residue of $f$ at the singularity $z = i$, write
>
> $$
> f(z) = \frac{\phi(z)}{z - i} \qquad\text{where}\qquad \phi(z) = \frac{(\log z)^3}{z + i} .
> $$
>
> The function $\phi$ is clearly analytic at $z = i$, which lies off the branch cut ([[§33 Branches and Derivatives of Logarithms#^def-33-3|Definition §33.3]]; here $\theta = \pi/2$). Since $\log i = \ln 1 + i\frac\pi2 = \frac{i\pi}{2}$,
>
> $$
> \phi(i) = \frac{(\log i)^3}{2i} = \frac{(i\pi/2)^3}{2i} = \frac{-i\pi^3/8}{2i} = -\frac{\pi^3}{16} \ne 0 ,
> $$
>
> so $f$ has a simple pole at $i$, and the residue is $B = \phi(i) = -\dfrac{\pi^3}{16}$.
>
> *B&C: Sec. 81, Example 3*

^ex-81-2

## When the Factorization Fails

While the theorem of §80 ([[§80 Residues at Poles#^thm-80-1|Theorem §80.1]]) can be extremely useful, the identification of an isolated singular point as a pole of a certain order is sometimes done most efficiently by appealing directly to a Laurent series.

> [!example] Example §81.3: Two Cautions
> **(a) $\phi(z_0) = 0$.** If the residue of
>
> $$
> f(z) = \frac{1 - \cos z}{z^3}
> $$
>
> is needed at the singularity $z = 0$, it would be incorrect to write $f = \phi(z)/z^3$ with $\phi(z) = 1 - \cos z$ and to apply [[§80 Residues at Poles#^thm-80-1|Theorem §80.1]] with $m = 3$: the theorem requires $\phi(0) \ne 0$, and here $\phi(0) = 0$. The simplest way is to write out a few terms of the Laurent series:
>
> $$
> f(z) = \frac{1}{z^3}\Big[1 - \Big(1 - \frac{z^2}{2!} + \frac{z^4}{4!} - \frac{z^6}{6!} + \cdots\Big)\Big] = \frac{1}{z^3}\Big(\frac{z^2}{2!} - \frac{z^4}{4!} + \frac{z^6}{6!} - \cdots\Big) = \frac{1}{2!}\cdot\frac1z - \frac{z}{4!} + \frac{z^3}{6!} - \cdots \qquad (0 < |z| < \infty) .
> $$
>
> This shows that $f$ has a *simple pole* at $z = 0$, not a pole of order $3$, with residue $B = \frac12$.
>
> **(b) $\phi$ not defined at $z_0$.** Since $z^2\sinh z$ is entire and its zeros are $z = n\pi i$ ($n = 0, \pm1, \pm2, \ldots$) ([[§39★ Hyperbolic Functions#^thm-39-4|Theorem §39.4]]), the point $z = 0$ is an isolated singularity of
>
> $$
> f(z) = \frac{1}{z^2\sinh z} .
> $$
>
> Here it would be a mistake to write $f = \phi(z)/z^2$ with $\phi(z) = 1/\sinh z$ and to use [[§80 Residues at Poles#^thm-80-1|Theorem §80.1]] with $m = 2$, because $\phi$ is not even defined at $z = 0$. The residue $B = -\frac16$ follows at once from the Laurent series
>
> $$
> \frac{1}{z^2\sinh z} = \frac{1}{z^3} - \frac16\cdot\frac1z + \frac{7}{360}z + \cdots \qquad (0 < |z| < \pi)
> $$
>
> found in [[§73★ Multiplication and Division of Power Series#^ex-73-4|Example §73.4]]. The singularity is a pole of the *third* order, not the second. (Correctly factored: $f = \phi/z^3$ with $\phi(z) = z/\sinh z$, which is analytic at $0$ once $\phi(0) = 1$ is assigned.)
>
> *B&C: Sec. 81, Examples 4 and 5*

^ex-81-3

## Exercises from the Course

> [!example] Example §81.4: Poles Inside the Circle |z − 1| = 3
> For each function, show that each singular point is a pole, determine its order and residue, and compute the integral over the circle $C\colon |z - 1| = 3$, oriented counterclockwise:
>
> $$
> \text{(a)}\ \frac{z + 1}{z^2 - 9}; \qquad \text{(b)}\ \Big(\frac{z}{1 - 3z}\Big)^3; \qquad \text{(c)}\ \frac{\cos z}{z^2 - \pi^2} .
> $$
>
> **The contour.** $C$ is the circle of radius $3$ about $1$, so it meets the real axis at $-2$ and $4$. A point $z_0$ is inside $C$ when $|z_0 - 1| < 3$ (figure below).
>
> **(a)** $z^2 - 9 = (z - 3)(z + 3)$. At $z = 3$: $f = \phi/(z - 3)$ with $\phi = \frac{z + 1}{z + 3}$ analytic at $3$ and $\phi(3) = \frac46 = \frac23 \ne 0$: a simple pole with residue $\frac23$. At $z = -3$: $\phi = \frac{z + 1}{z - 3}$, $\phi(-3) = \frac{-2}{-6} = \frac13 \ne 0$: a simple pole with residue $\frac13$. Only $3$ is inside $C$ ($|3 - 1| = 2$, $|-3 - 1| = 4$), so
>
> $$
> \int_C \frac{z + 1}{z^2 - 9}\,dz = 2\pi i\cdot\frac23 = \frac{4\pi i}{3} .
> $$
>
> **(b)** $1 - 3z = -3(z - \frac13)$, so
>
> $$
> \Big(\frac{z}{1 - 3z}\Big)^3 = \frac{z^3}{-27(z - \frac13)^3} = \frac{\phi(z)}{(z - \frac13)^3}, \qquad \phi(z) = -\frac{z^3}{27} ,
> $$
>
> with $\phi$ entire and $\phi(\frac13) = -\frac{1}{729} \ne 0$: a pole of order $3$ at $\frac13$, with residue
>
> $$
> \frac{\phi''(\frac13)}{2!} = \frac12\Big(-\frac{6z}{27}\Big)\Big|_{z=1/3} = \frac12\cdot\Big(-\frac{2}{27}\Big) = -\frac{1}{27} .
> $$
>
> The pole is inside $C$, so $\displaystyle\int_C\Big(\frac{z}{1 - 3z}\Big)^3dz = 2\pi i\Big(-\frac{1}{27}\Big) = -\frac{2\pi i}{27}$.
>
> **(c)** $z^2 - \pi^2 = (z - \pi)(z + \pi)$, and $\cos(\pm\pi) = -1 \ne 0$. At $z = \pi$: $\phi = \frac{\cos z}{z + \pi}$, residue $\phi(\pi) = \frac{-1}{2\pi}$. At $z = -\pi$: $\phi = \frac{\cos z}{z - \pi}$, residue $\phi(-\pi) = \frac{-1}{-2\pi} = \frac{1}{2\pi}$. Both are simple poles. Only $\pi$ is inside $C$ ($|\pi - 1| \approx 2.14$, $|-\pi - 1| \approx 4.14$), so
>
> $$
> \int_C \frac{\cos z}{z^2 - \pi^2}\,dz = 2\pi i\Big(-\frac{1}{2\pi}\Big) = -i .
> $$
>
> *Source: 342 HW 11, Problem 2*

^ex-81-4

![[m342-81-1.svg]]
*The contour $|z - 1| = 3$ of Example §81.4 with the singular points of the three functions: (a) $\pm3$ (red), (b) $\frac13$ (green), (c) $\pm\pi$ (orange). The circle crosses the real axis at $-2$ and $4$, so $3$, $\frac13$ and $\pi$ are inside while $-3$ and $-\pi$ are outside and contribute nothing to the integrals.*

> [!example] Example §81.5: The Singularities of (1 − z)/(z⁵ sin z)
> The Laurent series of $1/\sin z$ centered at $0$ has the form
>
> $$
> \frac{1}{\sin z} = \frac1z + \frac16z + \frac{7}{360}z^3 + \cdots \quad\text{(terms of order at least five)} \qquad (0 < |z| < \pi) \qquad (\ast)
> $$
>
> (part (a) of the problem, derived in [[§73★ Multiplication and Division of Power Series#^ex-73-3|Example §73.3]]). **(b)** Find the principal part at $z = 0$ of $f(z) = \dfrac{1 - z}{z^5\sin z}$. **(c)** Find all the singularities of $f$ in the disk $D = \{|z| < 4\}$ and determine their type. **(d)** Find the residue at each of them.
>
> **(b)** By $(\ast)$,
>
> $$
> f(z) = (1 - z)\Big(\frac{1}{z^6} + \frac16\cdot\frac{1}{z^4} + \frac{7}{360}\cdot\frac{1}{z^2} + \frac{31}{15120} + \cdots\Big) ,
> $$
>
> whose principal part is
>
> $$
> \frac{1}{z^6} - \frac{1}{z^5} + \frac16\Big(\frac{1}{z^4} - \frac{1}{z^3}\Big) + \frac{7}{360}\Big(\frac{1}{z^2} - \frac1z\Big) .
> $$
>
> **(c)** $f$ is analytic except at the zeros of $z^5\sin z$, that is, at $z = n\pi$. In $|z| < 4$ these are $0$ and $\pm\pi$ ($2\pi > 4$). By (b), $z = 0$ is a **pole of order $6$**. At $\pm\pi$, $\sin z$ has a simple zero ($\cos(\pm\pi) = -1 \ne 0$) and $(1 - z)/z^5 \ne 0$, so $\pm\pi$ are **simple poles** ([[§83 Zeros and Poles#^thm-83-1|Theorem §83.1]]).
>
> **(d)** At $0$ the residue is the coefficient of $1/z$ in (b): $\operatorname{Res}_{z=0} f = -\frac{7}{360}$. At the simple poles, with $p(z) = (1 - z)/z^5$ and $q(z) = \sin z$, $\operatorname{Res} = p(z_0)/q'(z_0)$ ([[§83 Zeros and Poles#^thm-83-2|Theorem §83.2]]):
>
> $$
> \operatorname{Res}_{z=\pi} f = \frac{1 - \pi}{\pi^5\cos\pi} = \frac{\pi - 1}{\pi^5}, \qquad \operatorname{Res}_{z=-\pi} f = \frac{1 + \pi}{(-\pi)^5\cos(-\pi)} = \frac{1 + \pi}{\pi^5} .
> $$
>
> **Variant.** For $f(z) = \dfrac{1 + z}{z^5\sin z}$ the same steps give the principal part $\frac{1}{z^6} + \frac{1}{z^5} + \frac16\big(\frac{1}{z^4} + \frac{1}{z^3}\big) + \frac{7}{360}\big(\frac{1}{z^2} + \frac1z\big)$, again a pole of order $6$ at $0$ and simple poles at $\pm\pi$, with residues $\frac{7}{360}$ at $0$, $-\frac{1 + \pi}{\pi^5}$ at $\pi$ and $\frac{1 - \pi}{\pi^5}$ at $-\pi$.
>
> *The Fall 2002 key's first line for (b) carries an extra factor $1/z^5$ in front of a bracket that already contains it, and its last pair of terms is written $\frac{7}{360}(z^{-6} - \cdots)$ in place of $\frac{7}{360}(z^{-2} - z^{-1})$; its orders and residues are correct.*
>
> *Source: 342 practice final (Fall 2002), Q1(b)–(d); 342 practice final (Fall 2009), Q2*

^ex-81-5
