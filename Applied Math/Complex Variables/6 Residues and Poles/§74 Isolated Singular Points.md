---
type: section
subject: "[[Complex Variables]]"
chapter: 6
section: 74
bc: "74"
aliases: ["B&C 74"]
tags: [complex-variables, math342]
---
← [[§73★ Multiplication and Division of Power Series]] · ↑ [[· 6 Residues and Poles]] · [[§75 Residues]] →

*Brown–Churchill, Section 74.*

The Cauchy–Goursat theorem ([[§51 Proof of the Theorem (Cauchy–Goursat Theorem)#^thm-51-3|Theorem §51.3]]) says that the integral of a function analytic inside and on a simple closed contour $C$ is zero. This chapter treats the case where the function fails to be analytic at finitely many points inside $C$: each such point contributes a specific number, its residue, to the integral. The theory needs singular points that have a whole punctured disk of analyticity around them, so that a Laurent series is available there; this section defines these **isolated** singular points and shows, with the logarithm and with $1/\sin(\pi/z)$, that not every singular point is isolated.

## Isolated Singular Points

Recall ([[§25 Analytic Functions#^def-25-1|Definition §25.1]], [[§25 Analytic Functions#^def-25-3|Definition §25.3]]) that $f$ is analytic at $z_0$ if it has a derivative at each point of some neighborhood of $z_0$, and that $z_0$ is a **singular point** of $f$ if $f$ fails to be analytic at $z_0$ but is analytic at some point of every neighborhood of $z_0$.

> [!definition] Definition §74.1: Isolated Singular Point
> A singular point $z_0$ of $f$ is **isolated** if there is a deleted $\varepsilon$ neighborhood
>
> $$
> 0 < |z - z_0| < \varepsilon
> $$
>
> of $z_0$ throughout which $f$ is analytic.
>
> *B&C: Sec. 74 (text)*

^def-74-1

> [!remark]- Connections
> - "Isolated" is meant in the topological sense: an isolated singular point is not a limit point (accumulation point) of the other singular points, [[§7 Interior and Closure#^def-7-3|590 Def. §7.3]]. In [[§74 Isolated Singular Points#^ex-74-3|Example §74.3]] the origin is a limit point of the singular points $1/n$, and that is exactly why it is not isolated.

> [!example] Example §74.1: A Rational Function
> The function
>
> $$
> f(z) = \frac{z - 1}{z^5(z^2 + 9)}
> $$
>
> has the three isolated singular points $z = 0$ and $z = \pm 3i$.
>
> **Why.** $f$ is a quotient of polynomials, so it is analytic wherever the denominator $z^5(z^2 + 9)$ is nonzero, that is, everywhere except at $0$ and $\pm 3i$ ([[§25 Analytic Functions#^prop-25-1|Proposition §25.1]]). At those three points $f$ is not even defined, and every neighborhood of each of them contains points where $f$ is analytic; so they are singular points. Around $z = 0$ the deleted disk $0 < |z| < 3$ contains no other zero of the denominator, so $f$ is analytic there; around $\pm 3i$ the deleted disks of radius $3$ work in the same way (the distance from $3i$ to $0$ is $3$, to $-3i$ it is $6$).
>
> **In general**, the singular points of a rational function are always isolated, because the zeros of the polynomial in the denominator are finite in number ([[§58 Liouville's Theorem and the Fundamental Theorem of Algebra#^cor-58-4|Corollary §58.4]]: a polynomial of degree $n \ge 1$ has exactly $n$ zeros counted with multiplicity). Around each zero, take $\varepsilon$ smaller than its distance to the nearest other zero.
>
> *B&C: Sec. 74, Example 1*

^ex-74-1

> [!example] Example §74.2: The Origin Is Not an Isolated Singular Point of Log z
> The origin is a singular point of the principal branch ([[§33 Branches and Derivatives of Logarithms#^def-33-2|Definition §33.2]])
>
> $$
> F(z) = \operatorname{Log} z = \ln r + i\Theta \qquad (r > 0,\ -\pi < \Theta < \pi)
> $$
>
> of the logarithm: $F$ is not defined at $0$, but it is analytic at the points of the positive real axis, and every neighborhood of $0$ contains such points. It is **not** an isolated singular point, since every deleted $\varepsilon$ neighborhood of it contains points of the negative real axis, where the branch is not even defined (Fig. 88 in B&C). The same holds for any branch
>
> $$
> f(z) = \log z = \ln r + i\theta \qquad (r > 0,\ \alpha < \theta < \alpha + 2\pi) ,
> $$
>
> whose branch cut, the ray $\theta = \alpha$, meets every deleted neighborhood of the origin.
>
> *B&C: Sec. 74, Example 2*

^ex-74-2

> [!example] Example §74.3: Singular Points Accumulating at the Origin
> Consider
>
> $$
> f(z) = \frac{1}{\sin(\pi/z)} .
> $$
>
> **The singular points.** $f$ has no derivative at $z = 0$, where it is not defined. Since the zeros of $\sin w$ are $w = n\pi$ ($n = 0, \pm1, \pm2, \ldots$) ([[§38 Zeros and Singularities of Trigonometric Functions#^thm-38-1|Theorem §38.1]]), $\sin(\pi/z) = 0$ exactly when $\pi/z = n\pi$ with $n \ne 0$, that is, at $z = 1/n$; at these points $f$ is not defined either. At every other point $f$ is a quotient of analytic functions with nonzero denominator, hence analytic; in particular $f$ is analytic at every point off the real axis. So every neighborhood of each of the points
>
> $$
> z = 0 \qquad\text{and}\qquad z = \frac1n \quad (n = \pm1, \pm2, \ldots) \qquad (1)
> $$
>
> contains points where $f$ is analytic, and each of the points (1) is a singular point of $f$.
>
> **$z = 0$ is not isolated.** Every deleted $\varepsilon$ neighborhood of $0$ contains other singular points: given $\varepsilon > 0$, let $m$ be any positive integer with $m > 1/\varepsilon$. Then $0 < 1/m < \varepsilon$, so the singular point $1/m$ lies in $0 < |z| < \varepsilon$, and $f$ is not analytic throughout that deleted neighborhood.
>
> **The points $1/n$ are isolated.** Let $m$ be a fixed positive integer. The singular points nearest to $1/m$ are $1/(m+1)$ on the left and (if $m \ge 2$) $1/(m-1)$ on the right, at distances
>
> $$
> \frac1m - \frac{1}{m+1} = \frac{1}{m(m+1)} \qquad\text{and}\qquad \frac{1}{m-1} - \frac1m = \frac{1}{m(m-1)} > \frac{1}{m(m+1)} ;
> $$
>
> all other singular points, including $0$, are farther away. So $f$ is analytic in the deleted neighborhood of $1/m$ of radius $\varepsilon = \dfrac{1}{m(m+1)}$ (Fig. 89 in B&C). For negative $m$ the same argument works with $\varepsilon = \dfrac{1}{|m|(|m|+1)}$, by symmetry.
>
> *B&C: Sec. 74, Example 3*

^ex-74-3

![[m342-74-1.svg]]
*The singular points $z = 1/n$ of $f(z) = 1/\sin(\pi/z)$ (blue) crowd toward the origin from both sides. Every deleted disk about $0$, however small (red, radius $\varepsilon$), contains infinitely many of them, so $0$ is a singular point that is not isolated. Each $1/m$ is isolated: the deleted disk of radius $\frac{1}{m(m+1)}$ about it (green, $m = 2$, radius $\frac16$) reaches only to the next point $\frac{1}{m+1}$ and contains no singular point.*

## Finitely Many Singular Points Inside a Contour

In this chapter the singular points will usually be finitely many points inside a simple closed contour, and then they are automatically isolated.

> [!theorem] Proposition §74.1: Finitely Many Singular Points Inside a Contour Are Isolated
> Let $C$ be a simple closed contour, and let $f$ be analytic everywhere inside $C$ except for a finite number of singular points $z_1, z_2, \ldots, z_n$. Then each $z_k$ is an isolated singular point of $f$, and its deleted neighborhood $0 < |z - z_k| < \varepsilon$ can be chosen so small that it lies entirely inside $C$.
>
> *B&C: Sec. 74 (text)*

^prop-74-1

> [!proof]+ Proof
> Fix $k$. Let $d_1$ be the smallest of the distances $|z_k - z_j|$, $j \ne k$ (a minimum of finitely many positive numbers, so $d_1 > 0$; put $d_1 = \infty$ if $n = 1$). Let $d_2$ be the distance from $z_k$ to the closest point of $C$. (B&C takes its existence for granted; here is why it is positive.) If $z = z(t)$, $a \le t \le b$, parametrizes $C$, then $t \mapsto |z(t) - z_k|$ is continuous on $[a, b]$ and never zero, because $z_k$ lies inside $C$ and not on it; so it attains a positive minimum $d_2$ ([[Extreme Value Theorem]]).
>
> Choose any $\varepsilon$ with $0 < \varepsilon < \min(d_1, d_2)$. The disk $|z - z_k| < \varepsilon$ does not meet $C$; it is connected and contains the interior point $z_k$, so it lies entirely inside $C$ (the interior of $C$ is one of the two connected pieces into which $C$ divides the plane, by the Jordan curve theorem, [[§43 Contours#^thm-43-4|Theorem §43.4]]). Each point $z$ with $0 < |z - z_k| < \varepsilon$ is therefore inside $C$ and different from every $z_j$, so $f$ is analytic at $z$. Hence $f$ is analytic throughout the deleted neighborhood $0 < |z - z_k| < \varepsilon$, which lies inside $C$: $z_k$ is isolated.

^pf-74-1

*Uses:* [[§74 Isolated Singular Points#^def-74-1|Def. §74.1]], [[§43 Contours#^thm-43-4|§43.4]] (Jordan curve theorem), [[Extreme Value Theorem]]

## The Point at Infinity

It is sometimes convenient to treat the point at infinity ([[§17 Limits Involving the Point at Infinity#^def-17-1|Definition §17.1]]) as a singular point as well.

> [!definition] Definition §74.2: Isolated Singular Point at Infinity
> If there is a positive number $R_1$ such that $f$ is analytic for
>
> $$
> R_1 < |z| < \infty ,
> $$
>
> then $f$ is said to have an **isolated singular point at $z_0 = \infty$**.
>
> *B&C: Sec. 74 (text)*

^def-74-2

For example, a function that is analytic in the finite plane except at finitely many points has an isolated singular point at $\infty$: take $R_1$ larger than the moduli of all the singular points. This kind of singular point is used to define the residue at infinity ([[§77★ Residue at Infinity#^def-77-1|Definition §77.1]]).
