---
type: section
subject: "[[Complex Variables]]"
chapter: 2
section: 18
bc: "18"
aliases: ["B&C 18"]
tags: [complex-variables, math342]
---
← [[§17 Limits Involving the Point at Infinity]] · ↑ [[· 2 Analytic Functions]] · [[§19 Derivatives]] →

*Brown–Churchill, Section 18 · MAT 342 HW 2.*

A function is continuous at $z_0$ when its limit there exists and equals its value. The limit theorems of [[§16 Theorems on Limits|§16]] make sums, products, quotients and polynomials continuous at once; this section adds the two properties that need an ε–δ argument (compositions are continuous, and a continuous function that is nonzero at a point stays nonzero nearby), reduces continuity of $f = u + iv$ to that of $u$ and $v$, and proves that a continuous function on a closed bounded region is bounded and attains its maximum modulus. That last theorem is used again and again: in the ML-inequality estimates of Chapter 4, in the proof of Liouville's theorem and the fundamental theorem of algebra ([[§58 Liouville's Theorem and the Fundamental Theorem of Algebra|§58]]), and in the maximum modulus principle ([[§59 Maximum Modulus Principle|§59]]).

## Continuity

> [!definition] Definition §18.1: Continuity
> A function $f$ is **continuous at a point $z_0$** if all three of the following conditions are satisfied:
>
> $$
> \lim_{z\to z_0} f(z) \ \text{exists}, \qquad (1)
> $$
>
> $$
> f(z_0) \ \text{exists}, \qquad (2)
> $$
>
> $$
> \lim_{z\to z_0} f(z) = f(z_0) . \qquad (3)
> $$
>
> Statement (3) actually contains (1) and (2), since the existence of the quantity on each side is needed. It says that for each positive number $\varepsilon$ there is a positive number $\delta$ such that
>
> $$
> |f(z) - f(z_0)| < \varepsilon \qquad\text{whenever}\qquad |z - z_0| < \delta . \qquad (4)
> $$
>
> A function is **continuous in a region $R$** if it is continuous at each point of $R$ (at boundary points of $R$ that belong to $R$, in the sense of [[§15 Limits#^def-15-2|Definition §15.2]]).
>
> *B&C: Sec. 18, definitions (1)–(4)*

^def-18-1

In (4) the restriction $z \ne z_0$ of the limit definition can be dropped, since at $z = z_0$ the inequality reads $0 < \varepsilon$.

> [!remark]- Connections
> - The same definition for maps between metric spaces, [[§21 More on Metric Spaces꞉ Continuity#^def-21-1|451 Def. §21.1]], with $X = Y = \mathbb{C}$ and $d(z, w) = |z - w|$; for real functions of two variables, [[§3 Continuity and Limits of Functions#^def-3-1|452 Def. §3.1]].

> [!theorem] Proposition §18.1: Sums, Products, Quotients and Polynomials
> If two functions are continuous at a point, their sum and product are also continuous at that point; their quotient is continuous at any such point where the denominator is not zero. A polynomial is continuous in the entire plane, and a rational function $P(z)/Q(z)$ is continuous at every point where $Q(z) \ne 0$.
>
> *B&C: Sec. 18 (text)*

^prop-18-1

> [!proof]+ Proof
> If $f$ and $F$ are continuous at $z_0$, then $f(z) \to f(z_0)$ and $F(z) \to F(z_0)$, so by [[§16 Theorems on Limits#^thm-16-2|Theorem §16.2]] $f + F \to f(z_0) + F(z_0)$, $fF \to f(z_0)F(z_0)$, and, when $F(z_0) \ne 0$, $f/F \to f(z_0)/F(z_0)$: each limit equals the value of the combined function at $z_0$. For polynomials and rational functions this is [[§16 Theorems on Limits#^cor-16-3|Corollary §16.3]].

^pf-18-1

*Uses:* [[§18 Continuity#^def-18-1|Def. §18.1]], [[§16 Theorems on Limits#^thm-16-2|§16.2]], [[§16 Theorems on Limits#^cor-16-3|§16.3]]

> [!example] Example §18.1: Three ε–δ Proofs
> Use the definition of limit ([[§15 Limits#^def-15-1|Definition §15.1]]) to prove
>
> $$
> \text{(a)}\ \lim_{z\to z_0}\operatorname{Re} z = \operatorname{Re} z_0; \qquad \text{(b)}\ \lim_{z\to z_0}\bar z = \bar z_0; \qquad \text{(c)}\ \lim_{z\to0}\frac{\bar z^{\,2}}{z} = 0 .
> $$
>
> **(a)** For any $z$, $|\operatorname{Re} z - \operatorname{Re} z_0| = |\operatorname{Re}(z - z_0)| \le |z - z_0|$ ([[§4 Vectors and Moduli#^prop-4-1|Proposition §4.1]]). Given $\varepsilon > 0$, let $\delta = \varepsilon$: then $|\operatorname{Re} z - \operatorname{Re} z_0| \le |z - z_0| < \varepsilon$ whenever $0 < |z - z_0| < \delta$.
>
> **(b)** $|\bar z - \bar z_0| = |\overline{z - z_0}| = |z - z_0|$ ([[§6 Complex Conjugates#^thm-6-1|Theorem §6.1]] and [[§6 Complex Conjugates#^def-6-1|Definition §6.1]]). So again $\delta = \varepsilon$ works: $|\bar z - \bar z_0| < \varepsilon$ whenever $0 < |z - z_0| < \varepsilon$.
>
> **(c)** For $z \ne 0$, $\big|\bar z^{\,2}/z - 0\big| = |\bar z|^2/|z| = |z|^2/|z| = |z|$. So $\delta = \varepsilon$ works: $\big|\bar z^{\,2}/z\big| < \varepsilon$ whenever $0 < |z| < \varepsilon$.
>
> **Consequences for continuity.** By (a) and (b), $\operatorname{Re} z$ and $\bar z$ are continuous everywhere, and so is $\operatorname{Im} z = \operatorname{Re}(-iz)$. By (c), the function equal to $\bar z^{\,2}/z$ for $z \ne 0$ and to $0$ at $z = 0$ is continuous at $0$; at every other point it is a quotient of continuous functions with nonzero denominator (Proposition §18.1). So it is continuous in the whole plane, although it has no derivative at $0$ ([[§22 Examples (Cauchy–Riemann Equations)#^ex-22-3|Example §22.3]]).
>
> *B&C: Sec. 18, Exercise 1; Source: 342 HW 2*

^ex-18-1

> [!example] Example §18.2: Linear and Quadratic Functions from the Definition
> Let $a$, $b$, $c$ be complex constants. Use the definition of limit to show
>
> $$
> \text{(a)}\ \lim_{z\to z_0}(az + b) = az_0 + b; \qquad \text{(b)}\ \lim_{z\to z_0}(z^2 + c) = z_0^2 + c .
> $$
>
> **(a)** $|(az + b) - (az_0 + b)| = |a|\,|z - z_0|$. If $a = 0$ this is $0$ and any $\delta$ works; otherwise $\delta = \varepsilon/|a|$ works.
>
> **(b)** $|(z^2 + c) - (z_0^2 + c)| = |z - z_0|\,|z + z_0|$, and $|z + z_0| \le |z - z_0| + 2|z_0|$. If $|z - z_0| < 1$, then $|z + z_0| < 1 + 2|z_0|$. So with
>
> $$
> \delta = \min\Big(1,\ \frac{\varepsilon}{1 + 2|z_0|}\Big) ,
> $$
>
> $0 < |z - z_0| < \delta$ gives $|(z^2 + c) - (z_0^2 + c)| < \delta(1 + 2|z_0|) \le \varepsilon$. The first restriction $\delta \le 1$ controls the factor $|z + z_0|$, the second makes the product small.
>
> *B&C: Sec. 18, Exercise 2(a), (b)*

^ex-18-2

## Two Properties Proved from the Definition

> [!theorem] Theorem §18.2: Composition of Continuous Functions
> Let $w = f(z)$ be defined for all $z$ in a neighborhood $|z - z_0| < \delta$ of $z_0$, and let $W = g(w)$ be defined on a set containing the image of that neighborhood under $f$, so that $W = g[f(z)]$ is defined for $|z - z_0| < \delta$. If $f$ is continuous at $z_0$ and $g$ is continuous at the point $f(z_0)$ of the $w$ plane, then $g[f(z)]$ is continuous at $z_0$.
>
> *B&C: Sec. 18, Theorem 1*

^thm-18-2

> [!proof]+ Proof
> Let $\varepsilon > 0$. Since $g$ is continuous at $f(z_0)$, there is a positive number $\gamma$ such that
>
> $$
> \big|g[f(z)] - g[f(z_0)]\big| < \varepsilon \qquad\text{whenever}\qquad |f(z) - f(z_0)| < \gamma .
> $$
>
> Since $f$ is continuous at $z_0$, applying (4) to $f$ with $\gamma$ in place of $\varepsilon$ gives a positive number $\delta'$, which may be taken $\le \delta$, such that $|f(z) - f(z_0)| < \gamma$ whenever $|z - z_0| < \delta'$. So the neighborhood $|z - z_0| < \delta$ can be made small enough that the second inequality holds, and then the first does: $\big|g[f(z)] - g[f(z_0)]\big| < \varepsilon$ whenever $|z - z_0| < \delta'$. This is the continuity of $g[f(z)]$ at $z_0$.

^pf-18-2

*Uses:* [[§18 Continuity#^def-18-1|Def. §18.1]]

> [!remark]- Connections
> - The same proof for real functions: [[§17 Continuous Functions#^thm-17-4|451 Thm. §17.4]]; for functions of two variables, [[§3 Continuity and Limits of Functions#^thm-3-4|452 Thm. §3.4]].

> [!theorem] Theorem §18.3: Nonzero Near a Point Where It Is Nonzero
> If a function $f(z)$ is continuous and nonzero at a point $z_0$, then $f(z) \ne 0$ throughout some neighborhood of that point.
>
> *B&C: Sec. 18, Theorem 2*

^thm-18-3

> [!proof]+ Proof
> Since $f(z_0) \ne 0$, the number $|f(z_0)|/2$ is positive; assign it to $\varepsilon$ in statement (4). This gives a positive number $\delta$ such that
>
> $$
> |f(z) - f(z_0)| < \frac{|f(z_0)|}{2} \qquad\text{whenever}\qquad |z - z_0| < \delta .
> $$
>
> If there were a point $z$ in the neighborhood $|z - z_0| < \delta$ at which $f(z) = 0$, this would read $|f(z_0)| < |f(z_0)|/2$, a contradiction. So $f(z) \ne 0$ for $|z - z_0| < \delta$; in fact $|f(z)| > |f(z_0)|/2$ there.

^pf-18-3

*Uses:* [[§18 Continuity#^def-18-1|Def. §18.1]]

## Continuity and the Components

The continuity of a function

$$
f(z) = u(x, y) + iv(x, y) \qquad (5)
$$

is closely related to the continuity of its component functions.

> [!theorem] Theorem §18.4: Continuity of the Components
> If the component functions $u$ and $v$ in (5) are continuous at a point $z_0 = (x_0, y_0)$, then so is $f$. Conversely, if $f$ is continuous at $z_0$, the same is true of $u$ and $v$ at that point.
>
> *B&C: Sec. 18, Theorem 3*

^thm-18-4

> [!proof]+ Proof
> By [[§16 Theorems on Limits#^thm-16-1|Theorem §16.1]] with $w_0 = f(z_0) = u(x_0, y_0) + iv(x_0, y_0)$,
>
> $$
> \lim_{z\to z_0} f(z) = f(z_0) \quad\Longleftrightarrow\quad \lim_{(x, y)\to(x_0, y_0)} u(x, y) = u(x_0, y_0) \ \text{ and } \lim_{(x, y)\to(x_0, y_0)} v(x, y) = v(x_0, y_0) .
> $$
>
> The left side is the continuity of $f$ at $z_0$, the right side the continuity of $u$ and $v$ at $(x_0, y_0)$.

^pf-18-4

*Uses:* [[§16 Theorems on Limits#^thm-16-1|§16.1]], [[§18 Continuity#^def-18-1|Def. §18.1]]

The modulus of a continuous function is continuous. B&C leaves this as an exercise and uses it in [[§112★ Preservation of Angles and Scale Factors|§112★]] and [[§113★ Further Examples (Preservation of Angles and Scale Factors)|§113★]].

> [!theorem] Proposition §18.5: Limits of the Modulus
> If $\displaystyle\lim_{z\to z_0} f(z) = w_0$, then $\displaystyle\lim_{z\to z_0}|f(z)| = |w_0|$. In particular, if $f$ is continuous at $z_0$, so is $|f|$.
>
> *B&C: Sec. 18, Exercise 7; Source: 342 HW 2 (optional)*

^prop-18-5

> [!proof]+ Proof
> By the reverse triangle inequality ([[§5 Triangle Inequality#^cor-5-2|Corollary §5.2]]),
>
> $$
> \big|\,|f(z)| - |w_0|\,\big| \le |f(z) - w_0| .
> $$
>
> Given $\varepsilon > 0$, choose $\delta$ for $f$ as in definition (2) of [[§15 Limits|§15]]; then $\big|\,|f(z)| - |w_0|\,\big| \le |f(z) - w_0| < \varepsilon$ whenever $0 < |z - z_0| < \delta$, and the same $\delta$ works for $|f|$. The second statement is the case $w_0 = f(z_0)$.

^pf-18-5

*Uses:* [[§15 Limits#^def-15-1|Def. §15.1]], [[§5 Triangle Inequality#^cor-5-2|§5.2]]

## Continuous Functions on Closed Bounded Regions

Recall from [[§12★ Regions in the Complex Plane|§12★]] that a region $R$ is **closed** if it contains all of its boundary points ([[§12★ Regions in the Complex Plane#^def-12-3|Definition §12.3]]), and **bounded** if it lies inside some circle centered at the origin ([[§12★ Regions in the Complex Plane#^def-12-5|Definition §12.5]]).

> [!definition] Definition §18.2: Bounded Function
> A function $f$ is **bounded on $R$** if there is a nonnegative real number $M$ such that $|f(z)| \le M$ for all points $z$ in $R$.
>
> *B&C: Sec. 18 (text)*

^def-18-2

> [!theorem] Theorem §18.6: Continuous Functions on Closed Bounded Regions Are Bounded
> If a function $f$ is continuous throughout a region $R$ that is both closed and bounded, there exists a nonnegative real number $M$ such that
>
> $$
> |f(z)| \le M \qquad\text{for all points } z \text{ in } R , \qquad (6)
> $$
>
> where equality holds for at least one such $z$.
>
> *B&C: Sec. 18, Theorem 4*

^thm-18-6

> [!proof]+ Proof
> Write $f(z) = u(x, y) + iv(x, y)$ as in (5). By Theorem §18.4, $u$ and $v$ are continuous throughout $R$, so the real-valued function
>
> $$
> |f(z)| = \sqrt{[u(x, y)]^2 + [v(x, y)]^2}
> $$
>
> is continuous throughout $R$: $u^2 + v^2$ is a sum of products of continuous functions, and the square root is continuous on $[0, \infty)$ (alternatively, Proposition §18.5). A continuous real-valued function on a closed bounded set in the plane reaches a maximum value $M$ somewhere in the set (B&C cites this from advanced calculus; it is the extreme value theorem in two variables). So there is $z_1 \in R$ with $|f(z)| \le |f(z_1)| = M$ for all $z \in R$, and $M \ge 0$ since it is a modulus. Inequality (6) thus holds, with equality at $z_1$, and $f$ is bounded on $R$.

^pf-18-6

*Uses:* [[§18 Continuity#^thm-18-4|§18.4]], [[§18 Continuity#^prop-18-5|§18.5]], [[§18 Continuity#^def-18-2|Def. §18.2]], [[§96 Maximum and Minimum Values#^thm-96-3|Calc Thm. §96.3]] (extreme value theorem in two variables)

> [!remark]- Connections
> - The extreme value theorem for a closed bounded set in $\mathbb{R}^2$ is [[§96 Maximum and Minimum Values#^thm-96-3|Calc Thm. §96.3]]; its rigorous proof combines Heine–Borel, [[§15 Compact Spaces#^thm-15-12|590 Thm. §15.12]] (closed and bounded in $\mathbb{R}^n$ means compact), with [[§15 Compact Spaces#^thm-15-3|590 Thm. §15.3]] (the continuous image of a compact set is compact). The one-variable case on $[a, b]$ is [[§18 Properties of Continuous Functions#^thm-18-1|451 Thm. §18.1]].

> [!example] Example §18.3: The Hypotheses of Theorem §18.6
> **Both hypotheses hold.** $f(z) = z^2 + 1$ is continuous on the closed disk $|z| \le 1$, which is closed and bounded. Here $|f(z)| \le |z|^2 + 1 \le 2$, with equality exactly when $|z| = 1$ and $z^2$ is a positive multiple of $1$, that is, at $z = \pm 1$. So $M = 2$, attained at $z = \pm1$.
>
> **Not closed.** $f(z) = 1/(1 - |z|^2)$ (the function of B&C's Exercise 1(d), Section 14) is continuous on the open disk $|z| < 1$, a quotient of continuous functions with nonzero denominator ($|z|^2 = z\bar z$ is continuous by Example §18.1). It is not bounded there: $f(r) = 1/(1 - r^2) \to \infty$ as $r \to 1^-$. Even a bounded function may fail to reach its bound: on $|z| < 1$, $|z| < 1$ everywhere, but the value $1$ is never attained.
>
> **Not bounded.** $f(z) = z$ is continuous on the closed half plane $\operatorname{Re} z \ge 0$, which contains all its boundary points but is not bounded, and $|f(z)| = |z|$ is unbounded there.
>
> *B&C: Sec. 18, Theorem 4 (text); Sec. 14, Exercise 1(d)*

^ex-18-3
