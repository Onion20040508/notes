---
type: section
subject: "[[Complex Variables]]"
chapter: 1
section: 5
bc: "5"
aliases: ["B&C 5"]
tags: [complex-variables, math342]
---
← [[§4 Vectors and Moduli]] · ↑ [[· 1 Complex Numbers]] · [[§6 Complex Conjugates]] →

*Brown–Churchill, Section 5 · MAT 342 HW 1.*

The triangle inequality $|z_1 + z_2| \le |z_1| + |z_2|$ is the basic tool for estimating complex quantities: it bounds the modulus of a sum by the sum of the moduli. Together with its reverse form $|z_1 + z_2| \ge \big||z_1| - |z_2|\big|$ and the rule $|z_1z_2| = |z_1||z_2|$, it gives upper and lower bounds for polynomials and quotients on circles and disks. Such estimates run through the whole subject: the ML-inequality for contour integrals ([[§47 Upper Bounds for Moduli of Contour Integrals#^thm-47-2|Theorem §47.2]]), Liouville's theorem and the fundamental theorem of algebra ([[§58 Liouville's Theorem and the Fundamental Theorem of Algebra#^thm-58-1|Theorems §58.1]] and [[§58 Liouville's Theorem and the Fundamental Theorem of Algebra#^thm-58-2|§58.2]]), which uses Example §5.3 below, and every estimate that makes an integral over a large arc tend to zero.

## The Triangle Inequality

> [!theorem] Theorem §5.1: Triangle Inequality
> For all complex numbers $z_1$ and $z_2$,
>
> $$
> |z_1 + z_2| \le |z_1| + |z_2| . \qquad (1)
> $$
>
> *B&C: Sec. 5, Equation (1)*

^thm-5-1

> [!proof]+ Proof
> B&C read (1) off the parallelogram of [[§4 Vectors and Moduli|§4]], Fig. 3: the length of one side of a triangle is at most the sum of the lengths of the other two. They leave an algebraic derivation to Exercise 15, Sec. 6, which uses conjugates ([[§6 Complex Conjugates#^rem-6-1|§6, Remark: The Triangle Inequality Through Conjugates]]). Here is the same derivation in coordinates, so that it needs nothing beyond §4.
>
> Let $z_1 = x_1 + iy_1$ and $z_2 = x_2 + iy_2$. Then
>
> $$
> |z_1 + z_2|^2 = (x_1 + x_2)^2 + (y_1 + y_2)^2 = |z_1|^2 + |z_2|^2 + 2(x_1x_2 + y_1y_2) .
> $$
>
> Expanding both sides shows the identity
>
> $$
> (x_1x_2 + y_1y_2)^2 + (x_1y_2 - x_2y_1)^2 = (x_1^2 + y_1^2)(x_2^2 + y_2^2) = |z_1|^2|z_2|^2
> $$
>
> (the cross terms $\pm 2x_1x_2y_1y_2$ cancel on the left). Hence $(x_1x_2 + y_1y_2)^2 \le |z_1|^2|z_2|^2$, so $x_1x_2 + y_1y_2 \le |x_1x_2 + y_1y_2| \le |z_1||z_2|$, and
>
> $$
> |z_1 + z_2|^2 \le |z_1|^2 + |z_2|^2 + 2|z_1||z_2| = \big(|z_1| + |z_2|\big)^2 .
> $$
>
> Both $|z_1 + z_2|$ and $|z_1| + |z_2|$ are nonnegative, so taking square roots gives (1).

^pf-5-1

*Uses:* [[§4 Vectors and Moduli#^def-4-1|Def. §4.1]], [[§1 Sums and Products#^def-1-3|Def. §1.3]]

> [!remark]- Connections
> - The same inequality, proved with conjugates: [[§13 Polynomials#^ladr-4-4|LADR 4.4]]; for norms in any inner product space it follows from Cauchy–Schwarz, [[Triangle inequality]]. The inequality $x_1x_2 + y_1y_2 \le |z_1||z_2|$ in the proof is Cauchy–Schwarz for the dot product in $\mathbb{R}^2$.
> - Stated without proof in [[§53 Complex Numbers#^thm-53-3|235 Thm. §53.3]] (property 6).

> [!remark] Remark: When Equality Holds
> The proof shows exactly when (1) is an equality: when $x_1x_2 + y_1y_2 = |z_1||z_2|$, that is, when $x_1y_2 - x_2y_1 = 0$ and $x_1x_2 + y_1y_2 \ge 0$. If $z_2 \ne 0$, the first condition says that the vectors $(x_1, y_1)$ and $(x_2, y_2)$ are parallel, $z_1 = tz_2$ with $t$ real, and then the second says $t|z_2|^2 \ge 0$, so $t \ge 0$. Thus $|z_1 + z_2| = |z_1| + |z_2|$ **if and only if one of the numbers is a nonnegative real multiple of the other**: $0$, $z_1$, $z_2$ lie on one ray from the origin.
>
> *B&C say that (1) is an equality when $0$, $z_1$ and $z_2$ are collinear. Collinearity is not enough; $z_1$ and $z_2$ must lie on the same side of $0$: for $z_1 = 1$, $z_2 = -1$, $|z_1 + z_2| = 0 < 2 = |z_1| + |z_2|$.*

^rem-5-1

> [!theorem] Corollary §5.2: Reverse Triangle Inequality
> For all complex numbers $z_1$ and $z_2$,
>
> $$
> |z_1 + z_2| \ge \big||z_1| - |z_2|\big| . \qquad (2)
> $$
>
> Replacing $z_2$ by $-z_2$ in (1) and (2),
>
> $$
> |z_1 - z_2| \le |z_1| + |z_2| \qquad\text{and}\qquad |z_1 - z_2| \ge \big||z_1| - |z_2|\big| .
> $$
>
> *B&C: Sec. 5, Equation (2) and text*

^cor-5-2

> [!proof]+ Proof
> Note first that $|-z| = |z|$, since $(-x)^2 + (-y)^2 = x^2 + y^2$. By (1),
>
> $$
> |z_1| = \big|(z_1 + z_2) + (-z_2)\big| \le |z_1 + z_2| + |-z_2| = |z_1 + z_2| + |z_2| ,
> $$
>
> which means that
>
> $$
> |z_1 + z_2| \ge |z_1| - |z_2| . \qquad (3)
> $$
>
> This is (2) when $|z_1| \ge |z_2|$. If $|z_1| < |z_2|$, interchange $z_1$ and $z_2$ in (3) to get $|z_1 + z_2| \ge |z_2| - |z_1| = -\big(|z_1| - |z_2|\big)$, which is (2) in this case. The last two inequalities are (1) and (2) applied to $z_1$ and $-z_2$, with $|-z_2| = |z_2|$.

^pf-5-2

*Uses:* [[§5 Triangle Inequality#^thm-5-1|§5.1]], [[§4 Vectors and Moduli#^def-4-1|Def. §4.1]]

Geometrically, (2) says that the length of one side of a triangle is at least the difference of the lengths of the other two sides. In practice one needs only (1) and (2): to bound $|z_1 - z_2|$, write it as $|z_1 + (-z_2)|$.

> [!theorem] Corollary §5.3: Triangle Inequality for Finite Sums
> For any complex numbers $z_1, \ldots, z_n$,
>
> $$
> |z_1 + z_2 + \cdots + z_n| \le |z_1| + |z_2| + \cdots + |z_n| \qquad (n = 2, 3, \ldots) . \qquad (4)
> $$
>
> *B&C: Sec. 5, Equation (4)*

^cor-5-3

> [!proof]+ Proof
> By induction on $n$. When $n = 2$, (4) is (1). If (4) holds for $n = m$, then by (1) and the induction hypothesis
>
> $$
> \big|(z_1 + \cdots + z_m) + z_{m+1}\big| \le |z_1 + \cdots + z_m| + |z_{m+1}| \le \big(|z_1| + \cdots + |z_m|\big) + |z_{m+1}| ,
> $$
>
> which is (4) for $n = m + 1$.

^pf-5-3

*Uses:* [[§5 Triangle Inequality#^thm-5-1|§5.1]]

The examples use one more pair of identities, which B&C leave to the exercises here and prove again in [[§6 Complex Conjugates#^thm-6-4|Theorem §6.4]].

> [!theorem] Proposition §5.4: Moduli of Products and Powers
> For all complex numbers $z_1, z_2, z$,
>
> $$
> |z_1z_2| = |z_1||z_2| \qquad\text{and}\qquad |z^n| = |z|^n \quad (n = 1, 2, \ldots) .
> $$
>
> *B&C: Sec. 5, Exercises 8 and 9*

^prop-5-4

> [!proof]+ Proof
> **Products** (Exercise 8). With $z_1 = x_1 + iy_1$, $z_2 = x_2 + iy_2$, the product is $z_1z_2 = (x_1x_2 - y_1y_2) + i(y_1x_2 + x_1y_2)$, so
>
> $$
> |z_1z_2|^2 = (x_1x_2 - y_1y_2)^2 + (y_1x_2 + x_1y_2)^2 = x_1^2x_2^2 + y_1^2y_2^2 + y_1^2x_2^2 + x_1^2y_2^2 = (x_1^2 + y_1^2)(x_2^2 + y_2^2) ,
> $$
>
> since the cross terms $-2x_1x_2y_1y_2$ and $+2x_1x_2y_1y_2$ cancel. So $|(x_1 + iy_1)(x_2 + iy_2)| = \sqrt{(x_1^2 + y_1^2)(x_2^2 + y_2^2)} = |z_1||z_2|$.
>
> **Powers** (Exercise 9). The identity is obvious for $n = 1$. If $|z^m| = |z|^m$, then $|z^{m+1}| = |z^mz| = |z^m||z| = |z|^m|z| = |z|^{m+1}$.

^pf-5-4

*Uses:* [[§4 Vectors and Moduli#^def-4-1|Def. §4.1]], [[§1 Sums and Products#^prop-1-2|§1.2]]

## Examples

> [!example] Example §5.1: Bounds on the Unit Circle
> If $z$ lies on the unit circle $|z| = 1$, then (1) and (2) give
>
> $$
> |z - 2| = |z + (-2)| \le |z| + |-2| = 1 + 2 = 3 \qquad\text{and}\qquad |z - 2| = |z + (-2)| \ge \big||z| - |-2|\big| = |1 - 2| = 1 .
> $$
>
> Both bounds are attained: at $z = -1$, $|z - 2| = 3$, and at $z = 1$, $|z - 2| = 1$ (the points of the circle farthest from and nearest to $2$).
>
> *B&C: Sec. 5, Example 1*

^ex-5-1

> [!example] Example §5.2: A Polynomial on a Circle
> Let $z$ be any point of the circle $|z| = 2$. By (4) and Proposition §5.4 ($|z^2| = |z|^2$),
>
> $$
> |3 + z + z^2| \le 3 + |z| + |z^2| = 3 + 2 + 4 = 9 .
> $$
>
> The bound is sharp: at $z = 2$ all three terms are positive and $3 + z + z^2 = 9$.
>
> *B&C: Sec. 5, Example 2*

^ex-5-2

> [!example] Example §5.3: Polynomials Are Large Far From the Origin
> Let $P(z) = a_0 + a_1z + a_2z^2 + \cdots + a_nz^n$ be a **polynomial** of degree $n \ge 1$, with complex constants $a_k$ and $a_n \ne 0$ (5). Show that there is a positive number $R$ such that
>
> $$
> \Big|\frac{1}{P(z)}\Big| < \frac{2}{|a_n|R^n} \qquad\text{whenever } |z| > R , \qquad (6)
> $$
>
> and that for $R$ sufficiently large, $|P(z)| < 2|a_n||z|^n$ whenever $|z| > R$.
>
> So the modulus of $1/P(z)$ is bounded from above outside a large circle; this is the property of polynomials used in [[§58 Liouville's Theorem and the Fundamental Theorem of Algebra#^thm-58-2|Theorem §58.2]] to prove the fundamental theorem of algebra.
>
> **Factor out $z^n$.** For $z \ne 0$ put
>
> $$
> w = \frac{a_0}{z^n} + \frac{a_1}{z^{n-1}} + \frac{a_2}{z^{n-2}} + \cdots + \frac{a_{n-1}}{z} , \qquad (7)
> $$
>
> so that
>
> $$
> P(z) = (a_n + w)z^n . \qquad (8)
> $$
>
> **Bound $w$.** Multiplying (7) by $z^n$ gives $wz^n = a_0 + a_1z + \cdots + a_{n-1}z^{n-1}$, so by (4) and Proposition §5.4, $|w||z|^n \le |a_0| + |a_1||z| + \cdots + |a_{n-1}||z|^{n-1}$, or
>
> $$
> |w| \le \frac{|a_0|}{|z|^n} + \frac{|a_1|}{|z|^{n-1}} + \frac{|a_2|}{|z|^{n-2}} + \cdots + \frac{|a_{n-1}|}{|z|} . \qquad (9)
> $$
>
> **Choose $R$.** A sufficiently large $R$ makes each of the $n$ quotients on the right of (9) less than $|a_n|/(2n)$ when $|z| > R$. (B&C assert this; here is a choice.) Take
>
> $$
> R = \max\Big(1,\ \frac{2n|a_0|}{|a_n|},\ \ldots,\ \frac{2n|a_{n-1}|}{|a_n|}\Big) .
> $$
>
> If $|z| > R \ge 1$, then $|z|^{n-k} \ge |z| > R$ for $k = 0, \ldots, n - 1$, so $|a_k|/|z|^{n-k} < |a_k|/R \le |a_n|/(2n)$ when $a_k \ne 0$ (and the quotient is $0$ when $a_k = 0$). Hence
>
> $$
> |w| < n\,\frac{|a_n|}{2n} = \frac{|a_n|}{2} \qquad\text{whenever } |z| > R .
> $$
>
> **Conclude.** By (2), $|a_n + w| \ge \big||a_n| - |w|\big| > \frac{|a_n|}{2}$ whenever $|z| > R$, and by (8),
>
> $$
> |P(z)| = |a_n + w||z|^n > \frac{|a_n|}{2}|z|^n > \frac{|a_n|}{2}R^n \qquad\text{whenever } |z| > R . \qquad (10)
> $$
>
> In particular $P(z) \ne 0$ there, and taking reciprocals gives (6).
>
> **The upper bound** (Exercise 7). Choose instead $R = \max\big(1, n|a_0|/|a_n|, \ldots, n|a_{n-1}|/|a_n|\big)$, so that each quotient in (9) is less than $|a_n|/n$ and $|w| < |a_n|$ for $|z| > R$. Then by (1), $|a_n + w| \le |a_n| + |w| < 2|a_n|$, and $|P(z)| = |a_n + w||z|^n < 2|a_n||z|^n$.
>
> *B&C: Sec. 5, Example 3 and Exercise 7*

^ex-5-3

> [!example] Example §5.4: A Circle Containing the Unit Circle
> **(a)** Sketch the curve $|z + 3 - 2i| = 6$. **(b)** It cuts the plane into the region it encloses and the unbounded region outside it; describe each by an inequality. **(c)** Show that the circle $|z| = 1$ lies entirely in the region enclosed by the curve.
>
> **(a)** The equation is $|z - (-3 + 2i)| = 6$: the points at distance $6$ from $-3 + 2i$, that is, the circle with center $(-3, 2)$ and radius $6$ ([[§4 Vectors and Moduli#^def-4-2|Definition §4.2]]).
>
> **(b)** A point is enclosed by the circle exactly when its distance from the center is less than the radius, and outside when it is greater:
>
> $$
> \text{inside: } |z + 3 - 2i| < 6, \qquad\qquad \text{outside: } |z + 3 - 2i| > 6 .
> $$
>
> The points of the circle itself, $|z + 3 - 2i| = 6$, belong to neither region.
>
> **(c)** We must show $|z + 3 - 2i| < 6$ whenever $|z| = 1$. By the triangle inequality (1),
>
> $$
> |z + (3 - 2i)| \le |z| + |3 - 2i| = 1 + \sqrt{13} < 1 + 4 = 5 < 6 ,
> $$
>
> since $\sqrt{13} < \sqrt{16} = 4$. (The bound $1 + \sqrt{13} \approx 4.61$ is attained at the point $z = (3 - 2i)/\sqrt{13}$ of the unit circle, where $z$ and $3 - 2i$ point the same way; see [[§5 Triangle Inequality#^rem-5-1|Remark: When Equality Holds]].)
>
> *Source: 342 HW 1, Problem 2*

^ex-5-4

![[m342-5-1.svg]]
*Example §5.4: the circle $|z + 3 - 2i| = 6$ (blue) with center $-3 + 2i$, and the unit circle (red) inside it. Every point of the unit circle is within $1 + \sqrt{13} \approx 4.61$ of the center (dashed: the farthest point), less than the radius $6$.*
