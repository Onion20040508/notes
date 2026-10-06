---
type: section
subject: "[[Functional Analysis]]"
chapter: 5
section: 24
tags: [functional-analysis, math556]
---
← [[§23 Cauchy–Schwarz and the Induced Norm]] · ↑ [[· 5 Inner Product Spaces]] · [[§25 Projection and Orthogonal Decomposition]] →

*Stage: inner products — Thread: convexity. The parallelogram law says which norms arise.*

## Which Norms Come from an Inner Product

> [!theorem] Proposition §24.1: Parallelogram Law and Polarization
> Let $(X, (\cdot,\cdot))$ be an inner product space and $\|x\| = (x,x)^{1/2}$. For all $x, y \in X$:
> - (a) (parallelogram law) $\|x + y\|^2 + \|x - y\|^2 = 2\|x\|^2 + 2\|y\|^2$;
> - (b) (polarization) if $\mathbb{F} = \mathbb{R}$, $(x,y) = \frac14\bigl( \|x+y\|^2 - \|x-y\|^2 \bigr)$; if $\mathbb{F} = \mathbb{C}$,
>
> $$
> (x,y) = \frac14 \bigl( \|x+y\|^2 - \|x-y\|^2 \bigr) + \frac{i}{4} \bigl( \|x+iy\|^2 - \|x-iy\|^2 \bigr) = \frac14 \sum_{k=0}^{3} i^k\, \|x + i^k y\|^2 .
> $$
>
> In particular an inner product is determined by the norm it induces.
>
> *Lax: §6.1, (6)*

^prop-24-1

> [!proof]+ Proof
> (Part (b) not covered in lecture.) By [[§23 Cauchy–Schwarz and the Induced Norm#^pf-23-1|(5.1)]] with $t = \pm 1$, and since $(x,y)$ and $(y,x)$ are conjugate and so have the same real part,
>
> $$
> \|x \pm y\|^2 = \|x\|^2 \pm 2\operatorname{Re}(x,y) + \|y\|^2 .
> $$
>
> Adding the two gives (a): in Wu's words, “$t$ positive cancels with $t$ negative.” Subtracting gives $\|x+y\|^2 - \|x-y\|^2 = 4\operatorname{Re}(x,y)$, which is (b) when $\mathbb{F} = \mathbb{R}$. When $\mathbb{F} = \mathbb{C}$, apply the same identity to $x$ and $iy$: since $(x, iy) = \bar{i}\,(x,y) = -i(x,y)$,
>
> $$
> \|x+iy\|^2 - \|x-iy\|^2 = 4\operatorname{Re}\bigl( -i(x,y) \bigr) = 4\operatorname{Im}(x,y),
> $$
>
> and $(x,y) = \operatorname{Re}(x,y) + i\operatorname{Im}(x,y)$ is the formula in (b).

^pf-24-1

*Uses:* [[§23 Cauchy–Schwarz and the Induced Norm#^pf-23-1|§23.1 (5.1)]], [[§22 Definition and Examples#^def-22-1|Def. §22.1]]

> [!remark]- Connections
> - The finite-dimensional home: [[§20 Inner Products and Norms#^ladr-6-21|LADR 6.21]] (parallelogram equality).
> - Used in Relativity: polarization recovers the Minkowski scalar product from the interval, without positivity — [[§B1.1 The Metric and Index Notation#^thm-b1-1-1|REL Theorem §B1.1.1]].

The parallelogram law is a statement of plane geometry: in the parallelogram spanned by $x$ and $y$, the diagonals are $x + y$ and $x - y$, and the squares of the two diagonals sum to the squares of the four sides.

![[m556-17-1.svg]]
*The parallelogram spanned by $x$ and $y$, with its two diagonals $x + y$ (red) and $x - y$ (blue). The law says the two diagonals' squares add up to the four sides' squares; polarization reads it the other way: the difference of the diagonals' squares is $4\operatorname{Re}(x,y)$, so the norm alone determines the inner product.*

The next theorem says it is the *only* obstruction.

> [!theorem] Theorem §24.2: Jordan–von Neumann
> Let $(X, \|\cdot\|)$ be a normed linear space. There is an inner product $(\cdot,\cdot)$ on $X$ with $(x,x) = \|x\|^2$ for all $x \in X$ if and only if $\|\cdot\|$ satisfies the parallelogram law. The inner product is then unique, given by the polarization formula of Proposition [[§24 The Parallelogram Law and Jordan–von Neumann#^prop-24-1|§24.1]](b).
>
> *Source: HW3, Problem 3*
>
> *Lax: §6.1, Exercise 1*

^thm-24-2

> [!proof]+ Proof
> Necessity and uniqueness are Proposition [[§24 The Parallelogram Law and Jordan–von Neumann#^prop-24-1|§24.1]]. (HW3, Problem 3.)
> For sufficiency, assume the parallelogram law
>
> $$
> \|x + y\|^2 + \|x - y\|^2 = 2\bigl( \|x\|^2 + \|y\|^2 \bigr) \qquad \text{for all } x, y \in X. \tag{P}
> $$
>
> We treat $\mathbb{F} = \mathbb{R}$ first and then reduce $\mathbb{F} = \mathbb{C}$ to it. Two properties of the norm are used repeatedly: $\|\lambda w\| = |\lambda|\,\|w\|$, in particular $\|{-w}\| = \|w\|$; and the norm is continuous, since $\bigl|\,\|u\| - \|v\|\,\bigr| \leq \|u - v\|$.
>
> **Part 1: the real case.** Let $\mathbb{F} = \mathbb{R}$ and define
>
> $$
> (x, y) := \frac14 \bigl( \|x + y\|^2 - \|x - y\|^2 \bigr), \qquad x, y \in X.
> $$
>
> *Step 1: symmetry and positivity.* Since $y + x = x + y$ and $\|y - x\| = \|{-(x - y)}\| = \|x - y\|$, we have $(y, x) = (x, y)$. Also
>
> $$
> (x, x) = \frac14 \bigl( \|2x\|^2 - \|0\|^2 \bigr) = \frac14 \cdot 4\|x\|^2 = \|x\|^2,
> $$
>
> so $(x,x) \geq 0$, with $(x,x) = 0$ if and only if $x = 0$, and $\|x\|^2 = (x,x)$.
>
> *Step 2: a midpoint identity.* We claim that
>
> $$
> (x, z) + (y, z) = 2\Bigl( \frac{x + y}{2},\, z \Bigr) \qquad \text{for all } x, y, z \in X. \tag{1}
> $$
>
> Put $u = \frac{x + y}{2}$ and $v = \frac{x - y}{2}$, so that $u + v = x$ and $u - v = y$. Applying (P) to the pair $u + z$, $v$ and to the pair $u - z$, $v$,
>
> $$
> \begin{aligned}
> \|x + z\|^2 + \|y + z\|^2 &= \|(u + z) + v\|^2 + \|(u + z) - v\|^2 = 2\|u + z\|^2 + 2\|v\|^2, \\
> \|x - z\|^2 + \|y - z\|^2 &= \|(u - z) + v\|^2 + \|(u - z) - v\|^2 = 2\|u - z\|^2 + 2\|v\|^2.
> \end{aligned}
> $$
>
> Subtracting the second line from the first,
>
> $$
> \bigl( \|x + z\|^2 - \|x - z\|^2 \bigr) + \bigl( \|y + z\|^2 - \|y - z\|^2 \bigr) = 2\bigl( \|u + z\|^2 - \|u - z\|^2 \bigr),
> $$
>
> that is, $4(x,z) + 4(y,z) = 8(u,z)$, which is (1).
>
> *Step 3: additivity in the first argument.* First, $(0, z) = \frac14 \bigl( \|z\|^2 - \|{-z}\|^2 \bigr) = 0$. Taking $y = 0$ in (1) gives $(x, z) = 2\bigl( \frac{x}{2}, z \bigr)$ for every $x \in X$. Applying this with $x + y$ in place of $x$, and then (1),
>
> $$
> (x + y, z) = 2\Bigl( \frac{x + y}{2}, z \Bigr) = (x, z) + (y, z).
> $$
>
> *Step 4: rational homogeneity.* We show $(ax, z) = a(x, z)$ for all $a \in \mathbb{Q}$. For $n \in \mathbb{N}$, induction on $n$ using Step 3 gives $(nx, z) = n(x, z)$, the case $n = 0$ being $(0, z) = 0$. Next,
>
> $$
> (-x, z) = \frac14 \bigl( \|{-x} + z\|^2 - \|{-x} - z\|^2 \bigr) = \frac14 \bigl( \|x - z\|^2 - \|x + z\|^2 \bigr) = -(x, z),
> $$
>
> so $(-nx, z) = -(nx, z) = -n(x, z)$, and the claim holds for all $a \in \mathbb{Z}$. Finally, for $m \in \mathbb{Z}$ and $n \in \mathbb{N}$ with $n \geq 1$,
>
> $$
> n\Bigl( \frac{m}{n}x,\, z \Bigr) = \Bigl( n \cdot \frac{m}{n}x,\, z \Bigr) = (mx, z) = m(x, z),
> $$
>
> and dividing by $n$ gives $\bigl( \frac{m}{n}x, z \bigr) = \frac{m}{n}(x, z)$.
>
> *Step 5: real homogeneity.* Fix $x, z \in X$ and define $\phi, \psi : \mathbb{R} \to \mathbb{R}$ by
>
> $$
> \phi(a) = (ax, z) = \frac14 \bigl( \|ax + z\|^2 - \|ax - z\|^2 \bigr), \qquad \psi(a) = a\,(x, z).
> $$
>
> The maps $a \mapsto ax \pm z$ are continuous from $\mathbb{R}$ to $X$, since $\|(ax \pm z) - (a'x \pm z)\| = |a - a'|\,\|x\|$; the norm is continuous; and $t \mapsto t^2$ is continuous. So $\phi$ is continuous, and so is $\psi$. By Step 4, $\phi = \psi$ on $\mathbb{Q}$. Given $a \in \mathbb{R}$, choose rationals $a_k \to a$; then
>
> $$
> \phi(a) = \lim_{k} \phi(a_k) = \lim_{k} \psi(a_k) = \psi(a).
> $$
>
> Hence $(ax, z) = a(x, z)$ for all $a \in \mathbb{R}$.
>
> *Step 6: conclusion.* By Steps 3 and 5, $(ax + by, z) = (ax, z) + (by, z) = a(x, z) + b(y, z)$ for all $a, b \in \mathbb{R}$, and by the symmetry of Step 1 the same holds in the second argument. Together with Step 1, $(\cdot,\cdot)$ is bilinear, symmetric and positive, i.e. a scalar product on $X$, and $(x, x) = \|x\|^2$ for all $x \in X$.
>
> **Part 2: the complex case.** Let $\mathbb{F} = \mathbb{C}$ and define
>
> $$
> (x, y) := \frac14 \bigl( \|x + y\|^2 - \|x - y\|^2 \bigr) + \frac{i}{4} \bigl( \|x + iy\|^2 - \|x - iy\|^2 \bigr), \qquad x, y \in X.
> $$
>
> Writing $R(x, y) := \frac14 \bigl( \|x + y\|^2 - \|x - y\|^2 \bigr) \in \mathbb{R}$, this reads
>
> $$
> (x, y) = R(x, y) + i\,R(x, iy). \tag{2}
> $$
>
> *Step 1: $R$ is a real scalar product.* Restricting scalar multiplication to $\mathbb{R}$ makes $X$ a linear space over $\mathbb{R}$; $\|\cdot\|$ is still a norm on it, and (P) still holds. By Part 1, $R$ is real-bilinear and symmetric, with $R(x, x) = \|x\|^2$.
>
> *Step 2: two identities.* For all $x, y \in X$,
>
> $$
> \text{(i)}\ \ R(ix, iy) = R(x, y), \qquad \text{(ii)}\ \ R(ix, y) = -R(x, iy).
> $$
>
> For (i): $\|ix \pm iy\| = \|i(x \pm y)\| = |i|\,\|x \pm y\| = \|x \pm y\|$. For (ii): since $i \cdot (-iy) = y$, identity (i) gives $R(ix, y) = R\bigl( ix, i(-iy) \bigr) = R(x, -iy)$, and $R(x, -iy) = -R(x, iy)$ by the real linearity of $R$ in its second argument.
>
> *Step 3: complex linearity in the first argument.* Additivity and real homogeneity, $(x + x', y) = (x, y) + (x', y)$ and $(ax, y) = a(x, y)$ for $a \in \mathbb{R}$, follow from (2) and the real bilinearity of $R$. For multiplication by $i$, by (2), (ii) and (i),
>
> $$
> (ix, y) = R(ix, y) + i\,R(ix, iy) = -R(x, iy) + i\,R(x, y) = i\bigl( R(x, y) + i\,R(x, iy) \bigr) = i\,(x, y).
> $$
>
> Hence, for $c = c_1 + ic_2$ with $c_1, c_2 \in \mathbb{R}$,
>
> $$
> (cx, y) = \bigl( c_1 x + c_2\,(ix),\, y \bigr) = c_1 (x, y) + c_2 (ix, y) = c_1 (x, y) + i c_2 (x, y) = c\,(x, y),
> $$
>
> and together with additivity, $(ax + by, z) = a(x, z) + b(y, z)$ for all $a, b \in \mathbb{C}$.
>
> *Step 4: skew-symmetry.* Since $R$ is real-valued, $\overline{(x, y)} = R(x, y) - i\,R(x, iy)$. On the other hand, by (2), the symmetry of $R$, and (ii),
>
> $$
> (y, x) = R(y, x) + i\,R(y, ix) = R(x, y) + i\,R(ix, y) = R(x, y) - i\,R(x, iy).
> $$
>
> So $(x, y) = \overline{(y, x)}$.
>
> *Step 5: conjugate linearity in the second argument.* By Steps 4 and 3,
>
> $$
> (x, ay + bz) = \overline{(ay + bz, x)} = \overline{a(y, x) + b(z, x)} = \bar{a}\,\overline{(y, x)} + \bar{b}\,\overline{(z, x)} = \bar{a}\,(x, y) + \bar{b}\,(x, z).
> $$
>
> *Step 6: positivity.* By (2), $(x, x) = R(x, x) + i\,R(x, ix)$, where $R(x, x) = \|x\|^2$ and
>
> $$
> R(x, ix) = \frac14 \bigl( \|(1 + i)x\|^2 - \|(1 - i)x\|^2 \bigr) = \frac14 \bigl( |1 + i|^2 - |1 - i|^2 \bigr) \|x\|^2 = 0.
> $$
>
> Hence $(x, x) = \|x\|^2 \geq 0$, with equality if and only if $x = 0$.
>
> By Steps 3–6, $(\cdot,\cdot)$ is sesquilinear, skew-symmetric and positive, i.e. a scalar product on $X$, and $(x, x) = \|x\|^2$ for all $x \in X$.

^pf-24-2

*Uses:* [[§24 The Parallelogram Law and Jordan–von Neumann#^prop-24-1|§24.1]], [[§22 Definition and Examples#^def-22-1|Def. §22.1]], [[§11 Normed Linear Spaces#^def-11-1|Def. §11.1]], [[§11 Normed Linear Spaces#^lem-11-3|§11.3]], [[§11 Normed Linear Spaces#^prop-11-4|§11.4]], [[§4 The Completeness Axiom#^thm-4-7|451 §4.7]]

> [!remark]- Connections
> - The finite-dimensional parallelogram equality, whose remark names Jordan–von Neumann: [[§20 Inner Products and Norms#^ladr-6-21|LADR 6.21]].
> - Used to rule out $p \neq 2$: [[§24 The Parallelogram Law and Jordan–von Neumann#^cor-24-3|§24.3]]; and as an application of [[Functional Analysis Problem-Solving Techniques#^ex-t10|Technique 10]].

> [!remark] Remark
> Two points about the proof. First, the only genuinely analytic step is real homogeneity: additivity yields it for rational scalars by pure algebra, and continuity of the norm extends it to the reals. Additivity alone would not suffice — there exist additive functions $\mathbb{R} \to \mathbb{R}$ that are not linear, constructed from a Hamel basis — which is why continuity must be invoked. Second, the complex case is reduced to the real one exactly as in the [[§9 The Complex Hahn–Banach Theorem#^thm-9-2|complex Hahn–Banach theorem]]: the real part determines everything, because $\operatorname{Im}(x,y) = \operatorname{Re}(x, iy)$, just as $\operatorname{Im}\ell(x) = -\operatorname{Re}\ell(ix)$ there.

^rem-24-1

> [!theorem] Corollary §24.3: Only $p = 2$ Gives an Inner Product
> Let $1 \le p \le \infty$ with $p \neq 2$. The norm $\|\cdot\|_p$ on $\mathbb{F}^n$ ($n \ge 2$), on $\ell^p$, and on $L^p(\Omega)$ does not come from an inner product.

^cor-24-3

> [!proof]+ Proof
> By Theorem [[§24 The Parallelogram Law and Jordan–von Neumann#^thm-24-2|§24.2]] it suffices to exhibit $x, y$ violating the parallelogram law. In $\mathbb{F}^n$ and $\ell^p$ take $x = e_1$, $y = e_2$. In $L^p(\Omega)$ take disjoint $A, B \subset \Omega$ of positive measure (two disjoint small balls) and $x = \chi_A / m(A)^{1/p}$, $y = \chi_B / m(B)^{1/p}$, or $x = \chi_A$, $y = \chi_B$ if $p = \infty$. In each case $\|x\|_p = \|y\|_p = 1$ and $x, y$ have disjoint supports, so $|x \pm y|^p = |x|^p + |y|^p$ pointwise and $\|x \pm y\|_p = 2^{1/p}$ for $p < \infty$, while $\|x \pm y\|_\infty = 1$. The parallelogram law would require $\|x+y\|_p^2 + \|x-y\|_p^2 = 2 \cdot 2^{2/p}$ to equal $2(\|x\|_p^2 + \|y\|_p^2) = 4$, i.e. $2^{2/p} = 2$, i.e. $p = 2$; for $p = \infty$ it would require $2 = 4$. (Not covered in lecture.)

^pf-24-3

*Uses:* [[§24 The Parallelogram Law and Jordan–von Neumann#^thm-24-2|§24.2]], [[§18 Minkowski's Inequality and the Spaces ℓᵖ#^def-18-1|Def. §18.1]], [[§19 The Function Spaces Lᵖ(Ω)#^def-19-1|Def. §19.1]]

![[m556-17-2.svg]]
*The proof in $\mathbb{R}^2$: the unit spheres of $\|\cdot\|_1$ (red), $\|\cdot\|_2$ (blue) and $\|\cdot\|_\infty$ (black). The sides $e_1$, $e_2$ of the square have norm $1$ in all three, but the diagonals $e_1 \pm e_2$ (dashed) cross the three spheres at $\tfrac12$, $\tfrac{1}{\sqrt2}$ and $1$ of their length, so their norms are $2$, $\sqrt2$ and $1$. The parallelogram law needs $\|e_1 + e_2\|^2 + \|e_1 - e_2\|^2 = 4$, which only the round sphere delivers.*
