---
type: section
subject: "[[Complex Variables]]"
chapter: 4
section: 59
bc: "59"
aliases: ["B&C 59"]
tags: [complex-variables, math342]
---
← [[§58 Liouville's Theorem and the Fundamental Theorem of Algebra]] · ↑ [[· 4 Integrals]] · [[§60 Convergence of Sequences]] →

*Brown–Churchill, Section 59 · MAT 342 HW 8 · Practice Finals (Fall 2009, Spring 2005, Fall 1999).*

The Cauchy integral formula on a circle says that the value of an analytic function at the center is the average of its values on the circle (Gauss's mean value theorem). An average cannot exceed its terms unless all are equal, so $|f|$ cannot have a local maximum at a point unless $f$ is constant near it; a chain of overlapping disks spreads this over the whole domain. The result is the maximum modulus principle: a nonconstant analytic function on a closed bounded region takes its largest modulus only on the boundary, and the same holds for its real and imaginary parts, which are harmonic. This is the complex-variable proof of the maximum principle for potentials and steady temperatures.

## Gauss's Mean Value Theorem and a Lemma

> [!theorem] Theorem §59.1: Gauss's Mean Value Theorem
> If a function $f$ is analytic within and on a circle $|z - z_0| = \rho$, its value at the center is the arithmetic mean of its values on the circle:
>
> $$
> f(z_0) = \frac{1}{2\pi}\int_0^{2\pi} f(z_0 + \rho e^{i\theta})\,d\theta . \qquad (2)
> $$
>
> *B&C: Sec. 59 (text)*

^thm-59-1

> [!proof]+ Proof
> Let $C_\rho$ denote the positively oriented circle $|z - z_0| = \rho$. The Cauchy integral formula ([[§54 Cauchy Integral Formula#^thm-54-1|Theorem §54.1]]) tells us that
>
> $$
> f(z_0) = \frac{1}{2\pi i}\int_{C_\rho}\frac{f(z)\,dz}{z - z_0} ; \qquad (1)
> $$
>
> and the parametric representation $z = z_0 + \rho e^{i\theta}$ ($0 \le \theta \le 2\pi$) for $C_\rho$, with $dz = i\rho e^{i\theta}\,d\theta$ and $z - z_0 = \rho e^{i\theta}$, enables us to write equation (1) as
>
> $$
> f(z_0) = \frac{1}{2\pi i}\int_0^{2\pi}\frac{f(z_0 + \rho e^{i\theta})}{\rho e^{i\theta}}\,i\rho e^{i\theta}\,d\theta = \frac{1}{2\pi}\int_0^{2\pi} f(z_0 + \rho e^{i\theta})\,d\theta .
> $$

^pf-59-1

*Uses:* [[§54 Cauchy Integral Formula#^thm-54-1|§54.1]], [[§44 Contour Integrals#^def-44-1|Def. §44.1]]

> [!remark]- Connections
> - The real part of (2) is the mean value property of the harmonic function $u = \operatorname{Re} f$, [[§39 Potential in a Disk#^thm-39-4|341 Thm. §39.4]], proved there from the polar Laplacian instead of from the Cauchy integral formula.

> [!theorem] Lemma §59.2: Local Maximum of the Modulus
> Suppose that $|f(z)| \le |f(z_0)|$ at each point $z$ in some neighborhood $|z - z_0| < \varepsilon$ in which $f$ is analytic. Then $f(z)$ has the constant value $f(z_0)$ throughout that neighborhood.
>
> *B&C: Sec. 59, Lemma*

^lem-59-2

> [!proof]+ Proof
> Let $z_1$ be any point other than $z_0$ in the given neighborhood, and let $\rho$ be the distance between $z_1$ and $z_0$. If $C_\rho$ denotes the positively oriented circle $|z - z_0| = \rho$, centered at $z_0$ and passing through $z_1$, then $f$ is analytic within and on $C_\rho$ (since $\rho < \varepsilon$), and Gauss's mean value theorem (2) gives
>
> $$
> |f(z_0)| \le \frac{1}{2\pi}\int_0^{2\pi}|f(z_0 + \rho e^{i\theta})|\,d\theta . \qquad (3)
> $$
>
> On the other hand, since
>
> $$
> |f(z_0 + \rho e^{i\theta})| \le |f(z_0)| \qquad (0 \le \theta \le 2\pi) , \qquad (4)
> $$
>
> we find that
>
> $$
> \int_0^{2\pi}|f(z_0 + \rho e^{i\theta})|\,d\theta \le \int_0^{2\pi}|f(z_0)|\,d\theta = 2\pi|f(z_0)| .
> $$
>
> Thus
>
> $$
> |f(z_0)| \ge \frac{1}{2\pi}\int_0^{2\pi}|f(z_0 + \rho e^{i\theta})|\,d\theta . \qquad (5)
> $$
>
> It is now evident from inequalities (3) and (5) that
>
> $$
> |f(z_0)| = \frac{1}{2\pi}\int_0^{2\pi}|f(z_0 + \rho e^{i\theta})|\,d\theta, \qquad\text{or}\qquad \int_0^{2\pi}\big[|f(z_0)| - |f(z_0 + \rho e^{i\theta})|\big]\,d\theta = 0 .
> $$
>
> The integrand in this last integral is continuous in the variable $\theta$; and, in view of condition (4), it is greater than or equal to zero on the entire interval $0 \le \theta \le 2\pi$. Because the value of the integral is zero, the integrand must be identically equal to zero. That is,
>
> $$
> |f(z_0 + \rho e^{i\theta})| = |f(z_0)| \qquad (0 \le \theta \le 2\pi) . \qquad (6)
> $$
>
> This shows that $|f(z)| = |f(z_0)|$ for all points $z$ on the circle $|z - z_0| = \rho$.
>
> Finally, since $z_1$ is any point in the deleted neighborhood $0 < |z - z_0| < \varepsilon$, the equation $|f(z)| = |f(z_0)|$ is, in fact, satisfied by all points $z$ lying on any circle $|z - z_0| = \rho$, where $0 < \rho < \varepsilon$. Consequently, $|f(z)| = |f(z_0)|$ everywhere in the neighborhood $|z - z_0| < \varepsilon$. But when the modulus of an analytic function is constant in a domain, the function itself is constant there ([[§26 Further Examples (Analytic Functions)#^ex-26-4|Example §26.4]]). Thus $f(z) = f(z_0)$ for each point $z$ in the neighborhood.

^pf-59-2

*Uses:* [[§59 Maximum Modulus Principle#^thm-59-1|§59.1]], [[§33 Properties of the Riemann Integral#^thm-33-7|451 Thm. §33.7]] (a continuous nonnegative function with zero integral vanishes), [[§26 Further Examples (Analytic Functions)#^ex-26-4|Ex. §26.4]]

## The Maximum Modulus Principle

> [!theorem] Theorem §59.3: Maximum Modulus Principle
> If a function $f$ is analytic and not constant in a given domain $D$, then $|f(z)|$ has no maximum value in $D$. That is, there is no point $z_0$ in the domain such that $|f(z)| \le |f(z_0)|$ for all points $z$ in it.
>
> *B&C: Sec. 59, Theorem*

^thm-59-3

> [!proof]+ Proof
> Given that $f$ is analytic in $D$, assume that $|f(z)|$ *does* have a maximum value at some point $z_0$ in $D$; we show that $f(z)$ must then be constant throughout $D$. The approach is similar to that of [[§28★ Uniquely Determined Analytic Functions#^lem-28-1|Lemma §28.1]].
>
> **A chain of disks.** Let $P$ be any point of $D$ other than $z_0$. Since a domain is connected, there is a polygonal line $L$ lying in $D$ and extending from $z_0$ to $P$ ([[§12★ Regions in the Complex Plane#^def-12-4|Definition §12.4]]). Let $d$ be the shortest distance from points of $L$ to the boundary of $D$; it is positive, because $L$ is a closed bounded set inside the open set $D$. (When $D$ is the entire plane, $d$ may have any positive value.) Since $L$ has finite length, there is a finite sequence of points
>
> $$
> z_0, z_1, z_2, \ldots, z_{n-1}, z_n
> $$
>
> along $L$ such that $z_n$ coincides with the point $P$ and
>
> $$
> |z_k - z_{k-1}| < d \qquad (k = 1, 2, \ldots, n)
> $$
>
> (mark points along $L$ at arc-length spacing less than $d$). Form the finite sequence of neighborhoods
>
> $$
> N_0, N_1, N_2, \ldots, N_{n-1}, N_n ,
> $$
>
> where each $N_k$ has center $z_k$ and radius $d$. Then $f$ is analytic in each of these neighborhoods, which are all contained in $D$, and the center of each neighborhood $N_k$ ($k = 1, 2, \ldots, n$) lies in the neighborhood $N_{k-1}$.
>
> **Passing the constant along the chain.** Since $|f(z)|$ was assumed to have a maximum value in $D$ at $z_0$, it also has a maximum value in $N_0$ at that point. Hence, according to Lemma §59.2, $f(z)$ has the constant value $f(z_0)$ throughout $N_0$. In particular, $f(z_1) = f(z_0)$. This means that $|f(z)| \le |f(z_1)|$ for each point $z$ in $N_1$; and the lemma can be applied again, this time telling us that $f(z) = f(z_1) = f(z_0)$ when $z$ is in $N_1$. Since $z_2$ is in $N_1$, then, $f(z_2) = f(z_0)$. Hence $|f(z)| \le |f(z_2)|$ when $z$ is in $N_2$; and the lemma is once again applicable, showing that $f(z) = f(z_2) = f(z_0)$ when $z$ is in $N_2$. Continuing in this manner (by induction on $k$), we eventually reach the neighborhood $N_n$ and arrive at the fact that $f(z_n) = f(z_0)$.
>
> Recalling that $z_n$ coincides with the point $P$, which is any point other than $z_0$ in $D$, we may conclude that $f(z) = f(z_0)$ for *every* point $z$ in $D$. Inasmuch as $f(z)$ has now been shown to be constant throughout $D$, the theorem is proved.

^pf-59-3

*Uses:* [[§59 Maximum Modulus Principle#^lem-59-2|§59.2]], [[§12★ Regions in the Complex Plane#^def-12-4|Def. §12.4]]

![[m342-59-1.svg]]
*The chain of neighborhoods in the proof. Each disk $N_k$ has radius $d$, the distance from the polygonal line $L$ to the boundary of $D$, so it lies in $D$; and each center $z_k$ lies in the previous disk. The lemma makes $f$ constant on $N_0$, which fixes the value at $z_1$ and makes $|f|$ maximal there; so $f$ is constant on $N_1$, and so on until $N_n$, which contains $P$.*

> [!remark]- Connections
> - The same structure (local constancy from a mean value property, then a connectedness argument) proves the maximum principle for harmonic functions, [[§39 Potential in a Disk#^thm-39-5|341 Thm. §39.5]]. There the connectedness step is the open-and-closed argument of Topology ([[§13 Connected Spaces#^def-13-1|590 Def. §13.1]]): the set where the maximum is attained is open by the lemma and closed by continuity. B&C uses polygonal lines instead, which is the same thing for plane domains ([[§14 Connected Subspaces of ℝ#^thm-14-4|590 Thm. §14.4]] gives one direction).

If a function $f$ that is analytic at each point in the interior of a closed bounded region $R$ is also continuous throughout $R$, then the modulus $|f(z)|$ has a maximum value somewhere in $R$ ([[§18 Continuity#^thm-18-6|Theorem §18.6]]). That is, there exists a nonnegative constant $M$ such that $|f(z)| \le M$ for all points $z$ in $R$, and equality holds for at least one such point. If $f$ is a constant function, then $|f(z)| = M$ for all $z$ in $R$. If, however, $f(z)$ is not constant, then, according to the theorem just proved, $|f(z)| \ne M$ for any point $z$ in the interior of $R$. We thus arrive at an important corollary.

> [!theorem] Corollary §59.4: The Maximum Is on the Boundary
> Suppose that a function $f$ is continuous on a closed bounded region $R$ and that it is analytic and not constant in the interior of $R$. Then the maximum value of $|f(z)|$ in $R$, which is always reached, occurs somewhere on the boundary of $R$ and never in the interior.
>
> *B&C: Sec. 59, Corollary*

^cor-59-4

> [!proof]+ Proof
> The function $|f(z)|$ is continuous on the closed bounded set $R$, so it attains a maximum value $M$ at some point of $R$ ([[§18 Continuity#^thm-18-6|Theorem §18.6]]). The interior of $R$ is a domain on which $f$ is analytic and not constant, so by Theorem §59.3 there is no point $z_0$ of the interior at which $|f(z)| \le |f(z_0)|$ for all $z$ in the interior; in particular $|f(z_0)| \ne M$ for interior points $z_0$. Hence every point where the maximum $M$ is reached lies on the boundary of $R$.

^pf-59-4

*Uses:* [[§59 Maximum Modulus Principle#^thm-59-3|§59.3]], [[§18 Continuity#^thm-18-6|§18.6]]

> [!remark]- Connections
> - "Which is always reached" is compactness: a closed bounded subset of the plane is compact ([[§15 Compact Spaces#^thm-15-12|590 Thm. §15.12]]), the continuous image of a compact set is compact ([[§15 Compact Spaces#^thm-15-3|590 Thm. §15.3]]), and a compact set of reals has a largest element; in calculus language, [[§96 Maximum and Minimum Values#^thm-96-3|Calc Thm. §96.3]]. On an unbounded region the corollary can fail: $e^z$ on the closed half plane $x \ge 0$ has $|e^z| = 1$ on the boundary $x = 0$ but is unbounded inside.

When the function $f$ in the corollary is written $f(z) = u(x, y) + iv(x, y)$, the component function $u(x, y)$ also has a maximum value in $R$ which is assumed on the boundary of $R$ and never in the interior, where it is harmonic ([[§27★ Harmonic Functions#^thm-27-1|Theorem §27.1]]).

> [!theorem] Corollary §59.5: Maximum of the Real Part
> Let $f(z) = u(x, y) + iv(x, y)$ be continuous on a closed bounded region $R$ and analytic and not constant in the interior of $R$. Then $u(x, y)$ has a maximum value in $R$, which is assumed on the boundary of $R$ and never in the interior.
>
> *B&C: Sec. 59 (text)*

^cor-59-5

> [!proof]+ Proof
> The composite function $g(z) = \exp[f(z)]$ is continuous in $R$ and analytic in the interior. It is not constant in the interior: if it were, then $0 = g'(z) = f'(z)e^{f(z)}$ there, so $f' = 0$ and $f$ would be constant in the interior (a domain; [[§25 Analytic Functions#^thm-25-3|Theorem §25.3]]). Hence, by Corollary §59.4, its modulus $|g(z)| = \exp[u(x, y)]$, which is continuous in $R$, assumes its maximum value in $R$ on the boundary, and never in the interior. In view of the increasing nature of the exponential function, the maximum value of $u(x, y)$ in $R$ is attained exactly where that of $\exp[u(x, y)]$ is: on the boundary, and never in the interior.

^pf-59-5

*Uses:* [[§59 Maximum Modulus Principle#^cor-59-4|§59.4]], [[§25 Analytic Functions#^thm-25-3|§25.3]]

Properties of *minimum* values of $|f(z)|$ and $u(x, y)$ are similar; they are treated in Examples §59.2 and §59.3.

## Examples

> [!example] Example §59.1: The Modulus of (z + 1)² on a Triangle
> Consider the function $f(z) = (z + 1)^2$ defined on the closed triangular region $R$ with vertices at the points $z = 0$, $z = 2$ and $z = i$. Locate the points of $R$ at which $|f(z)|$ has its maximum and minimum values.
>
> A simple geometric argument works. Interpret $|f(z)|$ as the square of the distance $d$ between $-1$ and a point $z$ of $R$:
>
> $$
> d^2 = |f(z)| = |z - (-1)|^2 .
> $$
>
> *Maximum.* The distance from a fixed point to a point of a triangle is largest at a vertex (each point of the triangle is a weighted average of the vertices, and distance is a convex function). The distances from $-1$ to the vertices $0$, $2$, $i$ are $1$, $3$, $\sqrt2$; so the maximum of $|f|$ is $9$, at $z = 2$.
>
> *Minimum.* Every point of $R$ has $x \ge 0$, so $d = |z + 1| \ge x + 1 \ge 1$, with equality only at $z = 0$. So the minimum of $|f|$ is $1$, at $z = 0$.
>
> Both occur at boundary points, as Corollary §59.4 (and, for the minimum, Example §59.2, since $f$ has no zero in $R$) require.
>
> *B&C: Sec. 59, Example*

^ex-59-1

> [!example] Example §59.2: The Minimum Modulus
> **(a)** Let a function $f$ be continuous on a closed bounded region $R$, and let it be analytic and not constant throughout the interior of $R$. Assuming that $f(z) \ne 0$ anywhere in $R$, prove that $|f(z)|$ has a *minimum value* $m$ in $R$ which occurs on the boundary of $R$ and never in the interior.
>
> Apply Corollary §59.4 to $g(z) = 1/f(z)$. Since $f$ has no zeros in $R$, $g$ is continuous on $R$ and analytic in the interior; and $g$ is not constant in the interior, since otherwise $f = 1/g$ would be. So $|g|$ attains a maximum value $M$ in $R$, only at boundary points. Since $|g(z)| = 1/|f(z)|$, and $t \mapsto 1/t$ is decreasing for $t > 0$,
>
> $$
> |g(z)| \le |g(z_1)| \quad\text{for all } z \in R \qquad\Longleftrightarrow\qquad |f(z)| \ge |f(z_1)| \quad\text{for all } z \in R .
> $$
>
> So $|f|$ attains the minimum value $m = 1/M > 0$ exactly at the points where $|g|$ attains its maximum: on the boundary, and never in the interior.
>
> **(b)** Use the function $f(z) = z$ to show that the condition $f(z) \ne 0$ anywhere in $R$ is necessary. Take $R$ to be the closed disk $|z| \le 1$. Then $f$ is continuous on $R$, analytic and not constant in the interior, but $|f(z)| = |z|$ reaches its minimum value $0$ at the interior point $z = 0$.
>
> **(c) Practice Final.** The same statement for the closed unit disk: if $f$ is continuous on $R\colon |z| \le 1$, analytic in $|z| < 1$, and $f(z) \ne 0$ for all $z$ in $R$, then $|f(z)|$ has a minimum $m$ in $R$, equal to $|f(z_0)|$ for some $z_0$ with $|z_0| = 1$. If $f$ is not constant, this is part (a). If $f$ is constant, $|f|$ is constant and its minimum is attained everywhere, in particular on the circle $|z| = 1$.
>
> *B&C: Sec. 59, Exercises 2 and 3; Source: 342 HW 8; 342 practice final (Fall 2009), Q3*

^ex-59-2

> [!example] Example §59.3: Minimum and Maximum of the Components
> **(a)** Let $f(z) = u(x, y) + iv(x, y)$ be continuous on a closed bounded region $R$ and analytic and not constant throughout the interior of $R$. Prove that $u(x, y)$ has a minimum value in $R$ which occurs on the boundary of $R$ and never in the interior.
>
> Following the suggestion to use Example §59.2, let $g(z) = \exp[f(z)]$. It is continuous on $R$, analytic in the interior, never zero, and not constant in the interior (if it were, $f'e^f = 0$ would give $f' = 0$ and $f$ constant, as in the proof of Corollary §59.5). By Example §59.2(a), $|g(z)| = e^{u(x, y)}$ has a minimum value in $R$, attained on the boundary and never in the interior; since $e^t$ is increasing, the same holds for $u$. (Alternatively, apply Corollary §59.5 to $-f$, whose real part is $-u$: the maximum of $-u$ is the minimum of $u$.)
>
> **(b)** With the same hypotheses, the component $v(x, y)$ has maximum and minimum values in $R$ which are reached on the boundary of $R$ and never in the interior, where it is harmonic. Apply the results for $u$ to $g(z) = -if(z) = v(x, y) - iu(x, y)$, whose real part is $v$; $g$ is continuous on $R$, analytic and not constant in the interior.
>
> **(c) An illustration.** For $f(z) = e^z$ and the rectangle $R\colon 0 \le x \le 1$, $0 \le y \le \pi$, $u = e^x\cos y$. Since $\cos y$ decreases from $1$ to $-1$ on $[0, \pi]$, $u \le e^x \le e$ with equality only at $z = 1$, and $u \ge -e^x \ge -e$ with equality only at $z = 1 + \pi i$: the maximum $e$ and the minimum $-e$ are at the boundary points $z = 1$ and $z = 1 + \pi i$ (B&C's answer).
>
> *B&C: Sec. 59, Exercises 5, 6 and 7; Source: 342 HW 8 (Exercise 7 optional)*

^ex-59-3

> [!example] Example §59.4: Two True-or-False Questions
> **(a)** *If $f$ is a non-constant entire function and $|f(z)| \le 2$ for every $z$ on the unit circle $|z| = 1$, then $f$ must map the unit disk $|z| < 1$ into the disk $|w| < 2$.*
>
> **True.** Apply Corollary §59.4 on the closed unit disk $R$. The function $f$ is continuous on $R$ and analytic in the interior; it is not constant there, since an entire function that is constant on an open disk is constant in the whole plane ([[§28★ Uniquely Determined Analytic Functions#^lem-28-1|Lemma §28.1]]). So the maximum $M$ of $|f|$ on $R$ is attained only on the circle, where $|f| \le 2$; hence $M \le 2$, and every interior point has $|f(z)| < M \le 2$.
>
> **(b)** *There is a function $f(z)$, analytic in the disk $D = \{|z| < 1\}$, such that $|f(z)|^2 = 4 - |z|^2$ for all $z$ in $D$.*
>
> **False.** Such an $f$ would have $|f(z)| = \sqrt{4 - |z|^2} \le 2 = |f(0)|$ for all $z$ in $D$, so $|f|$ would have a maximum value in the domain $D$, at $z = 0$. By the maximum modulus principle $f$ would be constant, so $|f|$ would be constant; but $\sqrt{4 - |z|^2}$ is not. ([[§27★ Harmonic Functions#^ex-27-5|Example §27.5]] gives a second proof, comparing the Laplacians of $|f|^2$ and $4 - |z|^2$.)
>
> *Source: 342 practice final (Spring 2005), Q8(c); 342 practice final (Fall 1999), Q7(b)*

^ex-59-4
