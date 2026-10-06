---
type: section
subject: "[[Complex Variables]]"
chapter: 4
section: 51
bc: "51"
aliases: ["B&C 51"]
tags: [complex-variables, math342]
---
← [[§50 Cauchy–Goursat Theorem]] · ↑ [[· 4 Integrals]] · [[§52 Simply Connected Domains]] →

*Brown–Churchill, Section 51 (with Exercises 4, 7–9 of Section 53) · MAT 342 HW 6, Practice Final (Fall 1999).*

This section proves the Cauchy–Goursat theorem, which [[§50 Cauchy–Goursat Theorem|§50]] states: if $f$ is analytic at all points interior to and on a simple closed contour $C$, then $\int_C f(z)\,dz = 0$. Cauchy's own proof used Green's theorem and needed $f'$ to be continuous; Goursat's argument needs only that $f'$ exists. Cover the region inside $C$ by small squares, on each of which $f$ is within $\varepsilon$ of its linear approximation at a point; a linear function integrates to zero around any closed contour, the integrals along shared sides cancel, and what is left is at most a constant times $\varepsilon$. The one delicate step is a lemma that such a covering exists, proved by repeated subdivision; everything later in the course (the deformation of paths, the Cauchy integral formula, Taylor and Laurent series, residues) rests on this theorem.

## A Preliminary Lemma

Throughout, $C$ is a positively oriented simple closed contour and $R$ is the closed region consisting of the points of $C$ together with the points interior to $C$. Saying that $f$ is analytic throughout $R$ means that $f$ is analytic at every point of $R$, hence in some open set containing $R$ ([[§25 Analytic Functions#^def-25-1|Definition §25.1]]).

Draw equally spaced lines parallel to the real and imaginary axes, with the same spacing in both directions. Since $R$ is bounded, only finitely many of the closed squares they form contain points of $R$.

> [!definition] Definition §51.1: Squares and Partial Squares
> In a covering of $R$ by a grid as above, a **square** is one of the closed square subregions (boundary together with interior) that contains points of $R$. If a square also contains points that are not in $R$, the set of its points that are in $R$ is a **partial square**. The finitely many squares and partial squares **cover** $R$: each point of $R$ lies in at least one of them, and each of them contains points of $R$.
>
> *B&C: Sec. 51 (text)*

^def-51-1

The proof of the lemma below subdivides squares again and again and needs the fact that a nested sequence of such squares has a common point. B&C leaves this to two exercises.

> [!theorem] Lemma §51.1: Nested Squares
> Let $\sigma_0\colon a_0 \le x \le b_0,\ c_0 \le y \le d_0$ be a closed square. Divide it into four equal closed squares by segments parallel to the axes and select one of them, $\sigma_1\colon a_1 \le x \le b_1,\ c_1 \le y \le d_1$; divide $\sigma_1$ into four and select one, $\sigma_2$; and so on. Then there is a point $(x_0, y_0)$ that belongs to every square of the sequence $\sigma_0, \sigma_1, \sigma_2, \ldots$
>
> *B&C: Sec. 53, Exercises 8 and 9*

^lem-51-1

> [!proof]+ Proof
> **Nested intervals (Exercise 8).** The intervals $a_n \le x \le b_n$ are each the left or the right half of the one before, so
>
> $$
> a_0 \le a_1 \le a_2 \le \cdots \le b_2 \le b_1 \le b_0, \qquad b_n - a_n = \frac{b_0 - a_0}{2^n} .
> $$
>
> The left endpoints $a_n$ form a nondecreasing sequence bounded above by $b_0$, so they have a limit $A$; the right endpoints form a nonincreasing sequence bounded below by $a_0$, so they have a limit $B$. Then $B - A = \lim (b_n - a_n) = 0$, so $A = B$; write $x_0 = A = B$. Since $a_n$ increases to $x_0$ and $b_n$ decreases to $x_0$, $a_n \le x_0 \le b_n$ for every $n$: the point $x_0$ belongs to every interval.
>
> **Nested squares (Exercise 9).** Each $\sigma_n$ is the product of the intervals $a_n \le x \le b_n$ and $c_n \le y \le d_n$, and both sequences of intervals are formed by halving, as in Exercise 8. So there are $x_0$ in every $[a_n, b_n]$ and $y_0$ in every $[c_n, d_n]$, and $(x_0, y_0)$ lies in every $\sigma_n$. (It is the only such point, since the diagonal of $\sigma_n$ tends to $0$.)

^pf-51-1

*Uses:* [[§10 Monotone Sequences and Cauchy Sequences#^thm-10-1|451 Thm. §10.1]] (monotone convergence)

> [!theorem] Lemma §51.2: Covering Lemma
> Let $f$ be analytic throughout a closed region $R$ consisting of the points interior to a positively oriented simple closed contour $C$ together with the points on $C$ itself. For any positive number $\varepsilon$, the region $R$ can be covered with a finite number of squares and partial squares, indexed by $j = 1, 2, \ldots, n$, such that in each one there is a fixed point $z_j$ for which the inequality
>
> $$
> \left| \frac{f(z) - f(z_j)}{z - z_j} - f'(z_j) \right| < \varepsilon \qquad (1)
> $$
>
> is satisfied by all points other than $z_j$ in that square or partial square.
>
> *B&C: Sec. 51, Lemma*

^lem-51-2

> [!proof]- Proof
> Fix $\varepsilon > 0$ and start from a covering of $R$ by squares and partial squares (Definition §51.1). Call a square or partial square **good** if it contains a point $z_j$ such that (1) holds for all its other points.
>
> **The subdivision process.** If one of the subregions of the covering is not good, divide its whole square into four smaller squares by the segments joining the midpoints of opposite sides; keep those of the four that contain points of $R$, and cut each down to its points in $R$ if it is a partial square. If any of the new subregions is not good, subdivide it in the same way, and so on. Good subregions are never subdivided. At every stage the subregions still cover $R$, because the four quarters of a square cover it. So if, for each of the original subregions, the process stops after a finite number of steps, then $R$ is covered by finitely many good squares and partial squares, which is the lemma.
>
> **The process stops.** Suppose not: for some original subregion the process never stops. Let $\sigma_0$ be its square (the whole square, if the subregion is a partial square). At least one of the four quarters of $\sigma_0$ must also have a process that never stops, for if each of them stopped after finitely many steps, then so would the process for $\sigma_0$, after the largest of these numbers plus one. (B&C says only that one of the quarters "must contain points of $R$ but no appropriate point $z_j$"; this is the precise form of that choice.) Let $\sigma_1$ be such a quarter, the lowest and then the furthest to the left if there are several. Repeating, we obtain a nested sequence
>
> $$
> \sigma_0, \sigma_1, \sigma_2, \ldots, \sigma_{k-1}, \sigma_k, \ldots \qquad (2)
> $$
>
> of squares, each a quarter of the one before, such that every $\sigma_k$ contains points of $R$ and its subregion is not good.
>
> **A common point in $R$.** By Lemma §51.1 there is a point $z_0$ common to every $\sigma_k$. If $s$ is the side of $\sigma_0$, the side of $\sigma_k$ is $s/2^k$ and its diagonal is $\sqrt2\,s/2^k$. Choose a point $w_k$ of $R$ in each $\sigma_k$; then $|w_k - z_0| \le \sqrt2\,s/2^k \to 0$. So every $\delta$ neighborhood $|z - z_0| < \delta$ contains points of $R$ (either $z_0$ itself or points of $R$ distinct from $z_0$, which makes $z_0$ an accumulation point of $R$). Since $R$ is a closed set, it contains its accumulation points ([[§12★ Regions in the Complex Plane#^thm-12-2|Theorem §12.2]]); so in either case $z_0$ is a point of $R$.
>
> **The contradiction.** Since $f$ is analytic throughout $R$, it is analytic at $z_0$, and $f'(z_0)$ exists. By the definition of derivative ([[§19 Derivatives#^def-19-1|Definition §19.1]]), for our $\varepsilon$ there is a $\delta$ neighborhood $|z - z_0| < \delta$ such that
>
> $$
> \left| \frac{f(z) - f(z_0)}{z - z_0} - f'(z_0) \right| < \varepsilon
> $$
>
> for all points $z \ne z_0$ in that neighborhood. Choose $K$ so large that the diagonal $\sqrt2\,s/2^K$ of $\sigma_K$ is less than $\delta$. Since $z_0$ lies in $\sigma_K$, every point of $\sigma_K$ is within $\sqrt2\,s/2^K < \delta$ of $z_0$; so the whole square $\sigma_K$ lies in the neighborhood. Hence $z_0$, which is a point of $R$ in $\sigma_K$, serves as the point $z_j$ in inequality (1) for the subregion consisting of $\sigma_K$ or a part of $\sigma_K$: that subregion is good. Contrary to the way in which the sequence (2) was formed, then, it is not necessary to subdivide $\sigma_K$. This contradiction proves the lemma.

^pf-51-2

*Uses:* [[§51 Proof of the Theorem (Cauchy–Goursat Theorem)#^def-51-1|Def. §51.1]], [[§51 Proof of the Theorem (Cauchy–Goursat Theorem)#^lem-51-1|§51.1]], [[§19 Derivatives#^def-19-1|Def. §19.1]], [[§12★ Regions in the Complex Plane#^thm-12-2|§12.2]]

![[m342-51-1.svg]]
*A covering of $R$ (shaded) by squares and partial squares. The partial squares are the parts inside $C$ of the squares that stick out (dashed). The square $\sigma_0$ (red) was not good and has been divided into four; one of its quarters, $\sigma_1$, was divided again. The lemma says that this process ends after finitely many steps.*

![[m342-51-2.svg]]
*(a) If the subdivision never stopped, it would produce nested squares $\sigma_0 \supset \sigma_1 \supset \sigma_2 \supset \cdots$ shrinking to a point $z_0$ of $R$. Inside the $\delta$ neighborhood where the difference quotient of $f$ at $z_0$ is within $\varepsilon$ of $f'(z_0)$ there is a whole square of the sequence (here $\sigma_4$), with $z_0$ as its point $z_j$; so that square is good, a contradiction. (b) Positively oriented boundaries of two adjacent subregions traverse their common side (red) in opposite directions, so the two integrals along it cancel.*

## Proof of the Cauchy–Goursat Theorem

> [!remark] Remark: Why It Works
> On each small subregion, $f(z)$ is a linear function $f(z_j) + f'(z_j)(z - z_j)$ plus an error $(z - z_j)\delta_j(z)$ with $|\delta_j| < \varepsilon$. The linear part has an antiderivative, so its integral around the closed boundary $C_j$ is $0$. The error is at most $\varepsilon$ times (diameter) times (length of $C_j$), which for a square of side $s_j$ is a multiple of $\varepsilon s_j^2$, the area; summed over all squares, this gives a multiple of $\varepsilon$ times the total area. The partial squares add a multiple of $\varepsilon$ times the length of $C$. Since the integrals along interior sides cancel, the sum of the integrals around the $C_j$ is $\int_C f(z)\,dz$, which is therefore smaller than any multiple of $\varepsilon$.

^rem-51-1

> [!theorem] Theorem §51.3: Cauchy–Goursat Theorem
> If a function $f$ is analytic at all points interior to and on a simple closed contour $C$, then
>
> $$
> \int_C f(z)\,dz = 0 . \qquad (3)
> $$
>
> This holds for either orientation of $C$.
>
> *B&C: Sec. 50, Theorem (proved in Sec. 51)*

^thm-51-3

> [!proof]- Proof
> If $C$ is negatively oriented, $\int_C f(z)\,dz = -\int_{-C} f(z)\,dz$, and $-C$ is positively oriented; so it suffices to treat a positively oriented $C$. Let $R$ be the closed region consisting of $C$ and the points interior to it.
>
> **An upper bound for the modulus of the integral.** Given an arbitrary positive number $\varepsilon$, consider the covering of $R$ in the statement of Lemma §51.2. On the $j$th square or partial square define a function $\delta_j(z)$ whose values are $\delta_j(z_j) = 0$, where $z_j$ is the fixed point in inequality (1), and
>
> $$
> \delta_j(z) = \frac{f(z) - f(z_j)}{z - z_j} - f'(z_j) \qquad\text{when } z \ne z_j . \qquad (4)
> $$
>
> According to inequality (1),
>
> $$
> |\delta_j(z)| < \varepsilon \qquad (5)
> $$
>
> at all points $z$ in the subregion on which $\delta_j(z)$ is defined. Also, $\delta_j(z)$ is continuous throughout the subregion: at $z \ne z_j$ it is built from the continuous function $f$, and at $z_j$
>
> $$
> \lim_{z \to z_j}\delta_j(z) = f'(z_j) - f'(z_j) = 0 = \delta_j(z_j) .
> $$
>
> Let $C_j$ ($j = 1, 2, \ldots, n$) denote the positively oriented boundaries of the squares or partial squares covering $R$. By the definition of $\delta_j(z)$, the value of $f$ at a point $z$ on any particular $C_j$ can be written
>
> $$
> f(z) = f(z_j) - z_jf'(z_j) + f'(z_j)z + (z - z_j)\delta_j(z)
> $$
>
> (for $z \ne z_j$ multiply (4) by $z - z_j$; for $z = z_j$ both sides are $f(z_j)$); and this means that
>
> $$
> \int_{C_j} f(z)\,dz = \big[f(z_j) - z_jf'(z_j)\big]\int_{C_j} dz + f'(z_j)\int_{C_j} z\,dz + \int_{C_j}(z - z_j)\delta_j(z)\,dz . \qquad (6)
> $$
>
> But
>
> $$
> \int_{C_j} dz = 0 \qquad\text{and}\qquad \int_{C_j} z\,dz = 0 ,
> $$
>
> since the functions $1$ and $z$ possess the antiderivatives $z$ and $z^2/2$ everywhere in the finite plane ([[§49 Proof of the Theorem (Antiderivatives)#^thm-49-1|Theorem §49.1]]). So equation (6) reduces to
>
> $$
> \int_{C_j} f(z)\,dz = \int_{C_j}(z - z_j)\delta_j(z)\,dz \qquad (j = 1, 2, \ldots, n) . \qquad (7)
> $$
>
> The sum of all $n$ integrals on the left in equations (7) can be written
>
> $$
> \sum_{j=1}^{n}\int_{C_j} f(z)\,dz = \int_C f(z)\,dz ,
> $$
>
> since the two integrals along the common boundary of every pair of adjacent subregions cancel each other, the integral being taken in one sense along that line segment in one subregion and in the opposite sense in the other (figure (b) above). Only the integrals along the arcs that are parts of $C$ remain, and these arcs make up $C$, each traversed once in the positive sense. Thus, in view of equations (7),
>
> $$
> \int_C f(z)\,dz = \sum_{j=1}^{n}\int_{C_j}(z - z_j)\delta_j(z)\,dz ;
> $$
>
> and so
>
> $$
> \left| \int_C f(z)\,dz \right| \le \sum_{j=1}^{n}\left| \int_{C_j}(z - z_j)\delta_j(z)\,dz \right| . \qquad (8)
> $$
>
> **Conclusion.** Bound each modulus on the right of (8) by the upper bound for moduli of contour integrals ([[§47 Upper Bounds for Moduli of Contour Integrals#^thm-47-2|Theorem §47.2]]). Each $C_j$ coincides either entirely or partially with the boundary of a square; in either case let $s_j$ denote the length of a side of that square. Since, in the $j$th integral, both the variable $z$ and the point $z_j$ lie in that square,
>
> $$
> |z - z_j| \le \sqrt2\,s_j .
> $$
>
> In view of inequality (5), then, each integrand on the right in (8) satisfies
>
> $$
> |(z - z_j)\delta_j(z)| = |z - z_j|\,|\delta_j(z)| < \sqrt2\,s_j\varepsilon . \qquad (9)
> $$
>
> If $C_j$ is the boundary of a square, its length is $4s_j$; letting $A_j = s_j^2$ denote the area of the square,
>
> $$
> \left| \int_{C_j}(z - z_j)\delta_j(z)\,dz \right| < \sqrt2\,s_j\varepsilon \cdot 4s_j = 4\sqrt2\,A_j\varepsilon . \qquad (10)
> $$
>
> If $C_j$ is the boundary of a partial square, it consists of pieces of the sides of the square, of total length at most $4s_j$, and of arcs of $C$, of total length $L_j$; so its length does not exceed $4s_j + L_j$. Again letting $A_j$ denote the area of the full square,
>
> $$
> \left| \int_{C_j}(z - z_j)\delta_j(z)\,dz \right| < \sqrt2\,s_j\varepsilon\,(4s_j + L_j) \le 4\sqrt2\,A_j\varepsilon + \sqrt2\,SL_j\varepsilon , \qquad (11)
> $$
>
> where $S$ is the length of a side of some square that encloses the entire contour $C$ as well as all of the squares originally used in covering $R$, so that $s_j \le S$. The squares of the covering do not overlap and lie in that enclosing square, so the sum of all the $A_j$'s does not exceed $S^2$; and the arcs of $C$ belonging to the various partial squares make up $C$, so the sum of the $L_j$'s is the length $L$ of $C$. It now follows from inequalities (8), (10) and (11) that
>
> $$
> \left| \int_C f(z)\,dz \right| < \big(4\sqrt2\,S^2 + \sqrt2\,SL\big)\varepsilon .
> $$
>
> The left-hand side does not depend on $\varepsilon$, while $S$ and $L$ are fixed by $C$ and the original grid; since $\varepsilon$ is arbitrary, the right-hand side can be made as small as we please. A nonnegative number smaller than every positive number is $0$, so $\int_C f(z)\,dz = 0$, which is statement (3).

^pf-51-3

*Uses:* [[§51 Proof of the Theorem (Cauchy–Goursat Theorem)#^lem-51-2|§51.2]], [[§51 Proof of the Theorem (Cauchy–Goursat Theorem)#^def-51-1|Def. §51.1]], [[§49 Proof of the Theorem (Antiderivatives)#^thm-49-1|§49.1]], [[§47 Upper Bounds for Moduli of Contour Integrals#^thm-47-2|§47.2]], [[§44 Contour Integrals#^thm-44-2|§44.2]]

> [!remark]- Connections
> - Cauchy's version, [[§50 Cauchy–Goursat Theorem#^thm-50-2|Theorem §50.2]], assumes $f'$ continuous and reduces $\int_C f(z)\,dz$ to two double integrals by Green's theorem, [[§27 Line Integrals and Green's Theorem#^thm-27-1|452 Thm. §27.1]] ([[§130 Green's Theorem#^thm-130-1|Calc Thm. §130.1]]), whose integrands vanish by the Cauchy–Riemann equations ([[§21 Cauchy–Riemann Equations#^thm-21-1|Theorem §21.1]]). Goursat's proof uses only the existence of $f'$, and so can later prove that $f'$ is continuous, indeed analytic ([[§57 Some Consequences of the Extension#^thm-57-1|§57.1]]).
> - The nested squares of Lemma §51.1 are a nested sequence of nonempty closed sets in a compact space, which always have a common point: [[§18 Compact Spaces#^cor-18-6|590 Cor. §18.6]]. The halving argument is the two-dimensional form of the bisection proofs in Single Variable Analysis.

> [!remark]- Remark: What the Proof Takes for Granted
> B&C treats two geometric points as evident. First, the positively oriented boundary of a partial square is a closed contour along which one can integrate, and its pieces on $C$ inherit the positive orientation of $C$. Second, the sides shared by adjacent subregions cancel and the remaining arcs make up $C$ exactly once. For the contours met in practice, which cross each grid line only finitely often, both are clear from a picture; in general they rest on the Jordan curve theorem ([[§43 Contours#^thm-43-4|Theorem §43.4]]), which B&C states without proof. For an arbitrary simple closed contour (one that wiggles across a grid line infinitely often, like the curve in [[§52 Simply Connected Domains#^ex-52-2|Example §52.2]]) a partial square may break into infinitely many pieces, and a complete proof needs more work: many texts first prove the theorem for triangles or rectangles, where no partial squares occur, and then pass to general contours. B&C's route, followed here, is the one used in the course.

^rem-51-2

## Applying the Theorem

The procedure for showing that an integral around a closed contour vanishes is [[§50 Cauchy–Goursat Theorem#^rem-50-2|Remark: Method — Showing That an Integral Around a Closed Contour Is Zero]]; with the Cauchy–Goursat theorem now proved, its step 2 needs no continuity of $f'$.

> [!example] Example §51.1: Three Integrals Around the Unit Circle
> Show that $\int_C f(z)\,dz = 0$ when $C$ is the unit circle $|z| = 1$, in either direction, for (b) $f(z) = ze^{-z}$; (c) $f(z) = \dfrac{1}{z^2 + 2z + 2}$; (f) $f(z) = \operatorname{Log}(z + 2)$.
>
> **(b)** $z$ and $e^{-z}$ are entire, so their product is entire; in particular it is analytic inside and on $C$, and $\int_C ze^{-z}\,dz = 0$.
>
> **(c)** A quotient of polynomials is analytic wherever its denominator is not zero. The zeros of $z^2 + 2z + 2$ are $z = -1 \pm \sqrt{1 - 2} = -1 \pm i$, of modulus $\sqrt2 > 1$. So $f$ is analytic in the disk $|z| < \sqrt2$, which contains $C$ and its interior, and $\int_C f(z)\,dz = 0$.
>
> **(f)** The principal branch $\operatorname{Log} w$ is analytic except on the ray $w \le 0$ of the real axis, so $\operatorname{Log}(z + 2)$ is analytic except where $z + 2$ is real and $\le 0$, that is, on the ray $x \le -2$, $y = 0$. That ray does not meet the disk $|z| < 2$, which contains $C$ and its interior. Hence $\int_C \operatorname{Log}(z + 2)\,dz = 0$.
>
> (Numerical quadrature over the parametrized circle gives $0$ to 20 digits in all three cases.)
>
> *B&C: Sec. 53, Exercise 1(b), (c), (f); Source: 342 HW 6*

^ex-51-1

> [!example] Example §51.2: The Integral of z̄ and the Area Inside C
> **(a)** Show that if $C$ is a positively oriented simple closed contour, then the area of the region enclosed by $C$ is
>
> $$
> \frac{1}{2i}\int_C \bar z\,dz .
> $$
>
> The function $\bar z$ is not analytic anywhere ([[§19 Derivatives#^ex-19-2|Example §19.2]]), so the Cauchy–Goursat theorem does not apply. But expression (4) in the proof of [[§50 Cauchy–Goursat Theorem#^thm-50-2|Theorem §50.2]],
>
> $$
> \int_C f(z)\,dz = \iint_R (-v_x - u_y)\,dA + i\iint_R (u_x - v_y)\,dA ,
> $$
>
> used only Green's theorem, not the Cauchy–Riemann equations, so it holds for any $f = u + iv$ whose components have continuous first partial derivatives on the region $R$ enclosed by $C$. For $f(z) = \bar z = x - iy$, $u = x$ and $v = -y$, so $-v_x - u_y = 0$ and $u_x - v_y = 1 + 1 = 2$:
>
> $$
> \int_C \bar z\,dz = 2i\iint_R dA = 2i \cdot (\text{area of } R) .
> $$
>
> Dividing by $2i$ gives the formula. (For the unit circle, numerical quadrature gives $\frac{1}{2i}\int_C \bar z\,dz = 3.14159\ldots = \pi$.)
>
> **(b) Practice Final.** Compute $I = \int_C \big(e^{\sin z} + \bar z\big)\,dz$, where $C$ is the circle $|z| = 2$ traversed counterclockwise.
>
> The function $e^{\sin z}$ is entire (a composition of entire functions), so its integral is $0$ by the Cauchy–Goursat theorem. By part (a), $\int_C \bar z\,dz = 2i \cdot \pi 2^2 = 8\pi i$. Check: on $|z| = 2$, $\bar z = 4/z$, and $\int_C 4\,dz/z = 4 \cdot 2\pi i$. Hence
>
> $$
> I = 0 + 8\pi i = 8\pi i .
> $$
>
> *B&C: Sec. 53, Exercise 7; Source: 342 HW 6 (optional); 342 practice final (Fall 1999), Q3*

^ex-51-2

> [!example] Example §51.3: A Gaussian Integral
> Use the Cauchy–Goursat theorem to derive the integration formula
>
> $$
> \int_0^\infty e^{-x^2}\cos 2bx\,dx = \frac{\sqrt\pi}{2}e^{-b^2} \qquad (b > 0) .
> $$
>
> **(a) The rectangle.** Integrate the entire function $e^{-z^2}$ around the positively oriented boundary of the rectangle with vertices $-a$, $a$, $a + bi$, $-a + bi$ ($a > 0$); by the theorem the four integrals add up to $0$.
> - *Lower leg*, $z = x$, $-a \le x \le a$: $\displaystyle\int_{-a}^{a}e^{-x^2}\,dx = 2\int_0^a e^{-x^2}\,dx$.
> - *Upper leg*, $z = x + bi$ from $x = a$ to $x = -a$: since $e^{-(x + bi)^2} = e^{b^2}e^{-x^2}e^{-2ibx}$ and the sine part of $e^{-2ibx}$ is odd,
>
> $$
> -e^{b^2}\int_{-a}^{a}e^{-x^2}e^{-2ibx}\,dx = -2e^{b^2}\int_0^a e^{-x^2}\cos 2bx\,dx .
> $$
>
> - *Right leg*, $z = a + iy$, $0 \le y \le b$, $dz = i\,dy$: $\displaystyle ie^{-a^2}\int_0^b e^{y^2}e^{-i2ay}\,dy$. *Left leg*, $z = -a + iy$ from $y = b$ to $y = 0$: $\displaystyle -ie^{-a^2}\int_0^b e^{y^2}e^{i2ay}\,dy$. Their sum is
>
> $$
> ie^{-a^2}\int_0^b e^{y^2}\big(e^{-i2ay} - e^{i2ay}\big)\,dy = 2e^{-a^2}\int_0^b e^{y^2}\sin 2ay\,dy .
> $$
>
> Setting the total equal to $0$ and dividing by $2e^{b^2}$:
>
> $$
> \int_0^a e^{-x^2}\cos 2bx\,dx = e^{-b^2}\int_0^a e^{-x^2}\,dx + e^{-(a^2 + b^2)}\int_0^b e^{y^2}\sin 2ay\,dy .
> $$
>
> **(b) The limit.** Accept $\int_0^\infty e^{-x^2}\,dx = \frac{\sqrt\pi}{2}$ (square it and change to polar coordinates). The last term is at most $e^{-(a^2 + b^2)}\int_0^b e^{y^2}\,dy$ in modulus, a constant times $e^{-a^2}$, which tends to $0$ as $a \to \infty$. Letting $a \to \infty$ gives the formula.
>
> (Check: for $a = 2$, $b = 0.7$ both sides of the identity in (a) equal $0.546917$; for $b = 0.5$ the integral is $0.690194 = \frac{\sqrt\pi}{2}e^{-1/4}$.)
>
> *B&C: Sec. 53, Exercise 4; Source: 342 HW 6 (optional)*

^ex-51-3
