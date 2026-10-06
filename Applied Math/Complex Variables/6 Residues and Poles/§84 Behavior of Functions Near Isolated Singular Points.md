---
type: section
subject: "[[Complex Variables]]"
chapter: 6
section: 84
bc: "84"
aliases: ["B&C 84"]
tags: [complex-variables, math342]
---
← [[§83 Zeros and Poles]] · ↑ [[· 6 Residues and Poles]] · [[§84a The Function e^(1∕z)]] →

*Brown–Churchill, Section 84 · MAT 342 HW 12, Practice Final (Spring 2012).*

The three types of isolated singular points, defined through Laurent series in [[§78 The Three Types of Isolated Singular Points|§78]], can also be told apart by how $f$ behaves near the point. Near a removable singular point $f$ is bounded, and conversely a bounded analytic function in a punctured disk has a removable singularity (**Riemann's theorem**). Near a pole $|f(z)| \to \infty$. Near an essential singular point $f$ comes arbitrarily close to every complex number in every punctured neighborhood (the **Casorati–Weierstrass theorem**), a weak form of Picard's theorem. B&C notes that these results are not used elsewhere in the book; they are the reason the classification matters, and they give the quickest way to classify a singularity from a limit.

## Removable Singular Points

> [!theorem] Theorem §84.1: Bounded Near a Removable Singular Point
> If $z_0$ is a removable singular point of a function $f$, then $f$ is bounded and analytic in some [[§12★ Regions in the Complex Plane#^def-12-new1|deleted neighborhood]] $0 < |z - z_0| < \varepsilon$ of $z_0$.
>
> *B&C: Sec. 84, Theorem 1*

^thm-84-1

> [!proof]+ Proof
> Since $z_0$ is removable, $f$ is analytic in a disk $|z - z_0| < R_2$ when $f(z_0)$ is properly defined ([[§78 The Three Types of Isolated Singular Points#^prop-78-1|Proposition §78.1]]). Then $f$ is continuous in any closed disk $|z - z_0| \le \varepsilon$ where $\varepsilon < R_2$. Consequently $f$ is bounded in that disk, by the theorem that a function continuous on a closed bounded region is bounded there ([[§18 Continuity#^thm-18-6|Theorem §18.6]]); and this means that, in addition to being analytic, $f$ is bounded in the deleted neighborhood $0 < |z - z_0| < \varepsilon$. (Changing the value at the single point $z_0$ does not affect the values in the deleted neighborhood.)

^pf-84-1

*Uses:* [[§78 The Three Types of Isolated Singular Points#^prop-78-1|§78.1]], [[§18 Continuity#^thm-18-6|§18.6]]

The next theorem is known as **Riemann's theorem** and is closely related to Theorem §84.1: it is its converse.

> [!theorem] Theorem §84.2: Riemann's Theorem
> Suppose that a function $f$ is bounded and analytic in some deleted neighborhood $0 < |z - z_0| < \varepsilon$ of $z_0$. If $f$ is not analytic at $z_0$, then it has a removable singularity there.
>
> *B&C: Sec. 84, Theorem 2*

^thm-84-2

> [!proof]+ Proof
> Assume that $f$ is not analytic at $z_0$. As a consequence, the point $z_0$ must be an isolated singularity of $f$ (it is a singular point, since $f$ is analytic at points of every neighborhood of $z_0$, and $f$ is analytic in a deleted neighborhood of it); and $f(z)$ is represented by a Laurent series
>
> $$
> f(z) = \sum_{n=0}^{\infty} a_n(z - z_0)^n + \sum_{n=1}^{\infty}\frac{b_n}{(z - z_0)^n} \qquad (1)
> $$
>
> throughout the deleted neighborhood $0 < |z - z_0| < \varepsilon$. If $C$ denotes a positively oriented circle $|z - z_0| = \rho$, where $\rho < \varepsilon$ (Fig. 97 in B&C), we know from Laurent's theorem ([[§67 Proof of Laurent's Theorem#^thm-67-1|Theorem §67.1]]) that the coefficients $b_n$ in expansion (1) can be written
>
> $$
> b_n = \frac{1}{2\pi i}\int_C \frac{f(z)\,dz}{(z - z_0)^{-n+1}} \qquad (n = 1, 2, \ldots) . \qquad (2)
> $$
>
> Now the boundedness condition on $f$ tells us that there is a positive constant $M$ such that $|f(z)| \le M$ whenever $0 < |z - z_0| < \varepsilon$. On $C$ the integrand of (2) is $f(z)(z - z_0)^{n-1}$, of modulus at most $M\rho^{n-1}$, and $C$ has length $2\pi\rho$. Hence it follows from expression (2) and the ML-inequality ([[§47 Upper Bounds for Moduli of Contour Integrals#^thm-47-2|Theorem §47.2]]) that
>
> $$
> |b_n| \le \frac{1}{2\pi}\cdot\frac{M}{\rho^{-n+1}}\cdot2\pi\rho = M\rho^n \qquad (n = 1, 2, \ldots) .
> $$
>
> Since the coefficients $b_n$ are constants (by (2) they do not depend on the choice of $\rho$) and since $\rho$ can be chosen arbitrarily small, we may conclude that $b_n = 0$ ($n = 1, 2, \ldots$) in the Laurent series (1): letting $\rho \to 0$ in $|b_n| \le M\rho^n$ with $n \ge 1$ gives $|b_n| \le 0$. This tells us that $z_0$ is a removable singularity of $f$, and the proof of Theorem §84.2 is complete.

^pf-84-2

*Uses:* [[§78 The Three Types of Isolated Singular Points#^def-78-2|Def. §78.2]], [[§74 Isolated Singular Points#^def-74-1|Def. §74.1]], [[§67 Proof of Laurent's Theorem#^thm-67-1|§67.1]] (Laurent's theorem), [[§47 Upper Bounds for Moduli of Contour Integrals#^thm-47-2|§47.2]] (ML-inequality)

> [!remark]- Connections
> - Riemann's theorem has no real counterpart: $\sin(1/x)$ is bounded and infinitely differentiable on $0 < |x| < 1$ but cannot be extended continuously to $0$, [[§17 Continuous Functions#^ex-17-5|451 Ex. §17.5]]. The proof works because the Laurent coefficients are integrals over circles, which a bound on $|f|$ controls (as in Cauchy's inequality, [[§57 Some Consequences of the Extension#^thm-57-4|Theorem §57.4]]).

## Essential Singular Points

We know from [[§79 Examples (The Three Types of Isolated Singular Points)#^ex-79-2|Example §79.2]] that the behavior of a function near an essential singular point can be quite irregular. The next theorem, regarding such behavior, is related to Picard's theorem ([[§79 Examples (The Three Types of Isolated Singular Points)#^thm-79-1|Theorem §79.1]]) and is usually referred to as the **Casorati–Weierstrass theorem**. It states that in each deleted neighborhood of an essential singular point, a function assumes values arbitrarily close to any given number.

> [!theorem] Theorem §84.3: Casorati–Weierstrass Theorem
> Suppose that $z_0$ is an essential singularity of a function $f$, and let $w_0$ be any complex number. Then, for any positive number $\varepsilon$, the inequality
>
> $$
> |f(z) - w_0| < \varepsilon \qquad (3)
> $$
>
> is satisfied at some point $z$ in each deleted neighborhood $0 < |z - z_0| < \delta$ of $z_0$ (Fig. 98 in B&C).
>
> *B&C: Sec. 84, Theorem 3*

^thm-84-3

> [!proof]+ Proof
> The proof is by contradiction. Since $z_0$ is an isolated singularity of $f$, there is a deleted neighborhood $0 < |z - z_0| < \delta$ throughout which $f$ is analytic; it suffices to treat deleted neighborhoods this small, since a larger one contains a smaller one. Assume that condition (3) is *not* satisfied for any point $z$ there. Thus $|f(z) - w_0| \ge \varepsilon$ when $0 < |z - z_0| < \delta$, and so the function
>
> $$
> g(z) = \frac{1}{f(z) - w_0} \qquad (0 < |z - z_0| < \delta) \qquad (4)
> $$
>
> is analytic (its denominator is analytic and never zero) and bounded, by $1/\varepsilon$, in its domain of definition. Hence, according to Theorem §84.2, $z_0$ is a removable singularity of $g$; we let $g$ be defined at $z_0$ so that it is analytic there. (If $g$ happens to be analytic at $z_0$ already, there is nothing to remove.)
>
> **If $g(z_0) \ne 0$**, the function $f(z)$, which can be written
>
> $$
> f(z) = \frac{1}{g(z)} + w_0 \qquad (5)
> $$
>
> when $0 < |z - z_0| < \delta$, becomes analytic at $z_0$ when it is defined there as
>
> $$
> f(z_0) = \frac{1}{g(z_0)} + w_0 ,
> $$
>
> since $1/g$ is analytic where $g$ is analytic and nonzero. But this means that $z_0$ is a removable singularity of $f$ (the Laurent series of $f$ in the punctured disk is then its Taylor series, with no negative powers), not an essential one, and we have a contradiction.
>
> **If $g(z_0) = 0$**, the function $g$ must have a zero of some finite order $m$ at $z_0$ ([[§82 Zeros of Analytic Functions#^def-82-1|Definition §82.1]]), because $g(z)$ is not identically equal to zero in the neighborhood $|z - z_0| < \delta$ (it is nonzero at every point other than $z_0$; compare the proof of [[§82 Zeros of Analytic Functions#^thm-82-2|Theorem §82.2]]). In view of equation (5), then, $f = \frac{1 + w_0g}{g}$ is a quotient whose numerator is analytic and equal to $1$ at $z_0$ and whose denominator has a zero of order $m$ there; so $f$ has a pole of order $m$ at $z_0$ ([[§83 Zeros and Poles#^thm-83-1|Theorem §83.1]]). So, once again, we have a contradiction, and Theorem §84.3 is proved.

^pf-84-3

*Uses:* [[§84 Behavior of Functions Near Isolated Singular Points#^thm-84-2|§84.2]], [[§82 Zeros of Analytic Functions#^def-82-1|Def. §82.1]], [[§82 Zeros of Analytic Functions#^thm-82-2|§82.2]], [[§83 Zeros and Poles#^thm-83-1|§83.1]], [[§78 The Three Types of Isolated Singular Points#^def-78-3|Def. §78.3]]

In the language of sets: the image under $f$ of every punctured neighborhood of an essential singular point is dense in $\mathbb{C}$. Picard's theorem says much more, that the image omits at most one point, and that every other value is taken infinitely often.

## Poles of Order m

The next theorem shows how the behavior of functions near poles is fundamentally different from their behavior near removable and essential singularities.

> [!theorem] Theorem §84.4: A Function Tends to Infinity at a Pole
> If $z_0$ is a pole of a function $f$, then
>
> $$
> \lim_{z\to z_0} f(z) = \infty . \qquad (6)
> $$
>
> *B&C: Sec. 84, Theorem 4*

^thm-84-4

> [!proof]+ Proof
> Assume that $f$ has a pole of order $m$ at $z_0$ and use the theorem in §80 ([[§80 Residues at Poles#^thm-80-1|Theorem §80.1]]). It tells us that
>
> $$
> f(z) = \frac{\phi(z)}{(z - z_0)^m} ,
> $$
>
> where $\phi$ is analytic and nonzero at $z_0$. Since $\phi$ is continuous at $z_0$ and $\phi(z_0) \ne 0$,
>
> $$
> \lim_{z\to z_0}\frac{1}{f(z)} = \lim_{z\to z_0}\frac{(z - z_0)^m}{\phi(z)} = \frac{\lim_{z\to z_0}(z - z_0)^m}{\lim_{z\to z_0}\phi(z)} = \frac{0}{\phi(z_0)} = 0 ,
> $$
>
> and limit (6) holds, according to the theorem in §17 regarding limits involving the point at infinity ([[§17 Limits Involving the Point at Infinity#^thm-17-1|Theorem §17.1]]: $\lim_{z\to z_0} f(z) = \infty$ if and only if $\lim_{z\to z_0} 1/f(z) = 0$).

^pf-84-4

*Uses:* [[§80 Residues at Poles#^thm-80-1|§80.1]], [[§17 Limits Involving the Point at Infinity#^thm-17-1|§17.1]]

As B&C remarks in a footnote, Theorem §84.4 says that the modulus $|f(z)|$ increases without bound as $z$ tends to $z_0$, and so suggests the existence of a pole in the nonmathematical sense: the graph of $|f|$ rises above $z_0$ like a pole.

> [!remark] Remark: Telling the Three Types Apart by Behavior
> Let $z_0$ be an isolated singular point of $f$. Then:
> - $z_0$ is **removable** if and only if $f$ is bounded in some deleted neighborhood of $z_0$ (Theorems §84.1 and §84.2);
> - $z_0$ is a **pole** if and only if $\lim_{z\to z_0} f(z) = \infty$;
> - $z_0$ is **essential** if and only if $f$ is neither bounded near $z_0$ nor tends to $\infty$; in that case $\lim_{z\to z_0} f(z)$ exists neither as a finite number nor as $\infty$.
>
> *Why.* The three types exclude each other and exhaust all cases ([[§78 The Three Types of Isolated Singular Points|§78]]). At a removable point $f$ is bounded (Theorem §84.1), so $f \not\to \infty$. At a pole $f \to \infty$ (Theorem §84.4), so $f$ is not bounded. At an essential point $f$ comes within $1$ of $0$ in every deleted neighborhood (Theorem §84.3 with $w_0 = 0$), so $f \not\to \infty$, and also within $1$ of every $w_0$ with $|w_0|$ as large as we like, so $f$ is unbounded. Reading the three implications backward gives the three "if" directions. The converse of Theorem §84.4 in particular: if $f \to \infty$ at an isolated singular point, it is neither removable nor essential, hence a pole.

^rem-84-1

## Examples

> [!example] Example §84.1: The Behavior of z⁵(1 − cos(1/z)) Near 0
> Consider
>
> $$
> f(z) = z^5\Big(1 - \cos\frac1z\Big) .
> $$
>
> Is $f$ bounded in a small disk $0 < |z| < \delta$? Does it have a finite or infinite limit at $0$? What else can be said about its behavior near $0$?
>
> **Classification.** With $\cos w = \sum_{n \ge 0}\frac{(-1)^n}{(2n)!}w^{2n}$ and $w = 1/z$,
>
> $$
> 1 - \cos\frac1z = \sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{(2n)!}\,\frac{1}{z^{2n}}, \qquad
> f(z) = \sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{(2n)!}\,z^{5-2n} = \frac{z^3}{2} - \frac{z}{24} + \frac{1}{720\,z} - \frac{1}{40320\,z^3} + \cdots \qquad (0 < |z| < \infty) .
> $$
>
> Every term with $n \ge 3$ is a negative power with nonzero coefficient, so $z = 0$ is an **essential singular point** (with residue $\frac{1}{720}$).
>
> **Not bounded; no limit, finite or infinite.** By the Remark above, $f$ is not bounded in any deleted neighborhood $0 < |z| < \delta$, and $\lim_{z\to0} f(z)$ is neither a number nor $\infty$. The two directions of approach make this concrete:
> - *Along the real axis*, $z = x$: $|1 - \cos(1/x)| \le 2$, so $|f(x)| \le 2|x|^5 \to 0$.
> - *Along the imaginary axis*, $z = iy$ with $y > 0$: $\cos\frac{1}{iy} = \cos\big(-\frac iy\big) = \cosh\frac1y$, so $|f(iy)| = y^5\big(\cosh\frac1y - 1\big) \ge y^5\cdot\frac{1}{720\,y^6} = \frac{1}{720\,y} \to \infty$ as $y \to 0^+$ (using $\cosh t - 1 \ge t^6/6!$ for real $t$). Numerically, $|f(0.1i)| \approx 0.11$ but $|f(0.05i)| \approx 75.8$.
>
> So $f$ tends to $0$ along one ray and to $\infty$ along another. More is true: by the Casorati–Weierstrass theorem (Theorem §84.3), in every deleted neighborhood of $0$, $f$ takes values arbitrarily close to *any* complex number; and by Picard's theorem it takes every complex value, with at most one exception, infinitely often.
>
> *Source: 342 HW 12, Problem 2*

^ex-84-1

> [!example] Example §84.2: Casorati–Weierstrass for e^(1/z)
> Show directly that $f(z) = e^{1/z}$ comes arbitrarily close to every complex number $w_0$ in every deleted neighborhood $0 < |z| < \delta$ of its essential singular point $0$ ([[§79 Examples (The Three Types of Isolated Singular Points)#^ex-79-2|Example §79.2]]).
>
> **$w_0 \ne 0$: the value is attained exactly.** Let $\operatorname{Log}w_0$ be the principal logarithm ([[§31 The Logarithmic Function#^def-31-2|Definition §31.2]]). For each integer $n$,
>
> $$
> z_n = \frac{1}{\operatorname{Log}w_0 + 2n\pi i} \qquad\text{satisfies}\qquad e^{1/z_n} = e^{\operatorname{Log}w_0 + 2n\pi i} = w_0 ,
> $$
>
> and $|z_n| \le \dfrac{1}{2|n|\pi - |\operatorname{Log}w_0|} \to 0$ as $|n| \to \infty$. So infinitely many points $z_n$ lie in $0 < |z| < \delta$, and at each of them $|f(z_n) - w_0| = 0 < \varepsilon$. For instance, with $w_0 = 2 + 3i$ the points $z_n$ for $n = 1, 5, 50$ have moduli about $0.136$, $0.031$, $0.0032$, and $e^{1/z_n} = 2 + 3i$ at each.
>
> **$w_0 = 0$: approached but never attained.** On the negative real axis, $z = -1/n$ ($n = 1, 2, \ldots$) gives $e^{1/z} = e^{-n}$, which is less than $\varepsilon$ for $n$ large, while $|z| = 1/n < \delta$. But $e^{1/z} \ne 0$ for every $z$. So $0$ is the one value omitted, the exception allowed by Picard's theorem, and Casorati–Weierstrass, which only promises values *close* to $w_0$, is sharp in this sense.
>
> *B&C: Sec. 79, Example 2; Sec. 84, Theorem 3*

^ex-84-2

> [!example] Example §84.3: Small Semicircles Around a Simple Pole
> Let $S_r$ be the upper half of the circle of radius $r$ centered at $0$, parametrized by $z(\theta) = re^{i\theta}$, $0 \le \theta \le \pi$. Let $f$ have a simple pole at $0$, and set $B = \operatorname{Res}_{z=0} f$. Prove that $\lim_{r\to0}\int_{S_r} f(z)\,dz = \pi iB$.
>
> **The first part of the problem.** If $g$ is analytic in some open disk centered at $0$, then $\lim_{r\to0}\int_{S_r} g(z)\,dz = 0$: $g$ is bounded, say by $M$, on a closed disk $|z| \le R'$ inside it ([[§18 Continuity#^thm-18-6|Theorem §18.6]]), so $\big|\int_{S_r} g\big| \le M\pi r \to 0$ by the ML-inequality. This is [[§47 Upper Bounds for Moduli of Contour Integrals#^ex-47-5|Example §47.5]](d).
>
> **Removing the principal part.** Since $0$ is a simple pole, the Laurent series of $f$ in a punctured disk $0 < |z| < R$ is $f(z) = \frac{B}{z} + \sum_{n \ge 0}a_nz^n$. So $g(z) = f(z) - \frac Bz$ has a zero principal part: $0$ is a removable singular point of $g$, and with $g(0) = a_0$ the function $g$ is analytic in $|z| < R$ ([[§78 The Three Types of Isolated Singular Points#^prop-78-1|Proposition §78.1]]; equivalently, $g$ is bounded near $0$, Theorem §84.1). Then
>
> $$
> \int_{S_r} f(z)\,dz = \int_{S_r} g(z)\,dz + B\int_{S_r}\frac{dz}{z} = \int_{S_r} g(z)\,dz + B\int_0^{\pi}\frac{ire^{i\theta}}{re^{i\theta}}\,d\theta = \int_{S_r} g(z)\,dz + \pi iB .
> $$
>
> By the first part the integral of $g$ tends to $0$, so $\lim_{r\to0}\int_{S_r} f(z)\,dz = \pi iB$: half of the $2\pi iB$ that a full circle would give. This is the limit behind the indented contours of [[§89★ An Indented Path#^thm-89-1|Theorem §89.1]], which treats the clockwise half circle.
>
> *Source: 342 practice final (Spring 2012), Q7(b)*

^ex-84-3

> [!example] Example §84.4: A Growth Bound That Forces Removability
> Let $f$ be analytic in a deleted neighborhood $0 < |z - z_0| < \varepsilon$, and suppose that $|f(z)| \le M|z - z_0|^{-1/2}$ there for some constant $M$. Show that $f$ is analytic at $z_0$ or has a removable singular point there. Show also that the exponent $-\frac12$ cannot be replaced by $-1$.
>
> **The function $g(z) = (z - z_0)f(z)$.** It is analytic in the deleted neighborhood, and there
>
> $$
> |g(z)| \le M|z - z_0|^{1/2} \le M\varepsilon^{1/2} ,
> $$
>
> so $g$ is bounded. By Riemann's theorem (Theorem §84.2), either $g$ is analytic at $z_0$ or $z_0$ is a removable singular point of $g$; in both cases $g$, given the value $\lim_{z\to z_0} g(z)$ at $z_0$, is analytic at $z_0$ ([[§78 The Three Types of Isolated Singular Points#^prop-78-1|Proposition §78.1]]). That limit is $0$, since $|g(z)| \le M|z - z_0|^{1/2} \to 0$. So $g$ is analytic at $z_0$ with $g(z_0) = 0$.
>
> **Back to $f$.** For $z \ne z_0$, $f(z) = g(z)/(z - z_0)$. By [[§80 Residues at Poles#^ex-80-1|Example §80.1]](b), applied to $g$, the quotient $g(z)/(z - z_0)$ has a removable singular point at $z_0$ (assigning it the value $g'(z_0)$ makes it analytic there). Hence $f$, which agrees with this quotient in the deleted neighborhood, is analytic at $z_0$ or has a removable singular point there.
>
> **Sharpness.** $f(z) = 1/(z - z_0)$ satisfies $|f(z)| = |z - z_0|^{-1}$, a bound of the form $M|z - z_0|^{-1}$ with $M = 1$, but $z_0$ is a simple pole. The same argument works for any bound $|f(z)| \le M|z - z_0|^{-\alpha}$ with $\alpha < 1$: an analytic function that blows up more slowly than $1/|z - z_0|$ cannot blow up at all.
>
> *Source: illustration added in these notes (not in B&C)*

^ex-84-4

