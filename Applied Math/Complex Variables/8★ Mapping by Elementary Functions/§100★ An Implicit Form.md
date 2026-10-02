---
type: section
subject: "[[Complex Variables]]"
chapter: 8
section: 100
bc: "100"
aliases: ["B&C 100"]
tags: [complex-variables, math342, extension]
---
← [[§99★ Linear Fractional Transformations]] · ↑ [[· 8★ Mapping by Elementary Functions]] · [[§101★ Mappings of the Upper Half Plane]] →

*Brown–Churchill, Section 100.*
★ *Beyond MAT 342: the course skipped this section or left it optional; it is included from Brown–Churchill.*

Three point conditions determine a linear fractional transformation completely. This section writes the transformation that sends $z_1, z_2, z_3$ to $w_1, w_2, w_3$ in one line, as an equality of two **cross ratios**, and proves that it is the only one. A point at infinity among the six is handled by deleting the two factors that contain it. Since a circle is determined by three of its points, this is the practical tool for mapping a given circle or line onto another: choose three points on each and match them.

## The Cross-Ratio Equation

> [!theorem] Theorem §100.1: The Transformation Through Three Points
> Let $z_1, z_2, z_3$ be distinct points of the finite $z$ plane and $w_1, w_2, w_3$ distinct points of the finite $w$ plane. The equation
>
> $$
> \frac{(w - w_1)(w_2 - w_3)}{(w - w_3)(w_2 - w_1)} = \frac{(z - z_1)(z_2 - z_3)}{(z - z_3)(z_2 - z_1)} \qquad (1)
> $$
>
> defines (implicitly) a linear fractional transformation $w = T(z)$ with $T(z_k) = w_k$ for $k = 1, 2, 3$.
>
> *B&C: Sec. 100, Equation (1)*

^thm-100-1

> [!proof]+ Proof
> Clear fractions in (1):
>
> $$
> (z - z_3)(w - w_1)(z_2 - z_1)(w_2 - w_3) = (z - z_1)(w - w_3)(z_2 - z_3)(w_2 - w_1) . \qquad (2)
> $$
>
> **The three points.** If $z = z_1$, the right side of (2) is zero, so the left side is too; since $z_1 \ne z_3$, $z_2 \ne z_1$ and $w_2 \ne w_3$, this forces $w = w_1$. Likewise, if $z = z_3$ the left side is zero, and $w = w_3$. If $z = z_2$, cancel the nonzero factor $(z_2 - z_1)(z_2 - z_3)$ to get the linear equation
>
> $$
> (w - w_1)(w_2 - w_3) = (w - w_3)(w_2 - w_1), \qquad\text{that is}\qquad w(w_1 - w_3) = w_2(w_1 - w_3) ,
> $$
>
> whose unique solution is $w = w_2$.
>
> **It is linear fractional.** Write $P = (z_2 - z_1)(w_2 - w_3)$ and $Q = (z_2 - z_3)(w_2 - w_1)$, both nonzero. Expanding the products in (2) puts it in the form
>
> $$
> Azw + Bz + Cw + D = 0 \qquad (3)
> $$
>
> with
>
> $$
> A = P - Q, \quad B = Qw_3 - Pw_1, \quad C = Qz_1 - Pz_3, \quad D = Pz_3w_1 - Qz_1w_3 .
> $$
>
> B&C argues that $AD - BC \ne 0$ because (2) does not define a constant function, as just shown. Here is the condition directly: multiplying out (checked symbolically),
>
> $$
> AD - BC = (z_1 - z_2)(z_1 - z_3)(z_2 - z_3)(w_1 - w_2)(w_1 - w_3)(w_2 - w_3) \ne 0 .
> $$
>
> So (3) has the form (2) of [[§99★ Linear Fractional Transformations#^def-99-1|Definition §99.1]], and by [[§99★ Linear Fractional Transformations#^prop-99-1|Proposition §99.1]] it can be solved as $w = T(z)$ with $T$ linear fractional.

^pf-100-1

*Uses:* [[§99★ Linear Fractional Transformations#^def-99-1|Def. §99.1]], [[§99★ Linear Fractional Transformations#^prop-99-1|§99.1]]

The two sides of (1) are **cross ratios**, which play a large role in fuller treatments of linear fractional transformations. The right side, as a function of $z$, is itself the linear fractional transformation that sends $z_1, z_2, z_3$ to $0, 1, \infty$ (B&C, Sec. 100, Exercise 4); so (1) says: send the $z$ points to $0, 1, \infty$, then bring $0, 1, \infty$ back to the $w$ points.

## Uniqueness

B&C leaves the uniqueness to the exercises; it rests on counting fixed points.

> [!theorem] Lemma §100.2: At Most Two Fixed Points
> A **fixed point** of a transformation $w = f(z)$ is a point $z_0$ with $f(z_0) = z_0$. Every linear fractional transformation other than the identity $w = z$ has at most two fixed points in the extended plane.
>
> *B&C: Sec. 100, Exercise 6*

^lem-100-2

> [!proof]+ Proof
> Let $T(z) = (az + b)/(cz + d)$, $ad - bc \ne 0$. At a finite $z$ with $cz + d \ne 0$,
>
> $$
> T(z) = z \iff az + b = z(cz + d) \iff cz^2 + (d - a)z - b = 0 .
> $$
>
> The excluded point $z = -d/c$ (when $c \ne 0$) is not fixed, since $T(-d/c) = \infty$.
>
> **$c \ne 0$.** The quadratic has at most two roots, and $\infty$ is not fixed because $T(\infty) = a/c$ is finite. At most two fixed points.
>
> **$c = 0$.** Then $T(\infty) = \infty$: one fixed point. The finite fixed points solve $(d - a)z = b$. If $d \ne a$ there is exactly one, for a total of two. If $d = a$, then $b \ne 0$ (otherwise $T(z) = az/a = z$ is the identity), and there is none, for a total of one.

^pf-100-2

*Uses:* [[§99★ Linear Fractional Transformations#^def-99-2|Def. §99.2]]

> [!theorem] Theorem §100.3: Uniqueness
> There is only one linear fractional transformation that maps three given distinct points $z_1, z_2, z_3$ of the extended $z$ plane onto three specified distinct points $w_1, w_2, w_3$ of the extended $w$ plane.
>
> *B&C: Sec. 100, Exercise 10*

^thm-100-3

> [!proof]+ Proof
> Let $T$ and $S$ be two such transformations. By [[§99★ Linear Fractional Transformations#^thm-99-4|Theorem §99.4]], $S^{-1}$ is linear fractional, and by [[§99★ Linear Fractional Transformations#^prop-99-5|Proposition §99.5]] so is $S^{-1} \circ T$. It has three fixed points:
>
> $$
> S^{-1}[T(z_k)] = S^{-1}(w_k) = z_k \qquad (k = 1, 2, 3) .
> $$
>
> By Lemma §100.2 it is the identity: $S^{-1}[T(z)] = z$ for all $z$. Applying $S$ to both sides, $T(z) = S(z)$ for all $z$.

^pf-100-3

*Uses:* [[§100★ An Implicit Form#^lem-100-2|§100.2]], [[§99★ Linear Fractional Transformations#^thm-99-4|§99.4]], [[§99★ Linear Fractional Transformations#^prop-99-5|§99.5]]

## A Point at Infinity

> [!theorem] Proposition §100.4: Deleting the Factors at Infinity
> If one of the prescribed points in the $z$ plane, or one in the $w$ plane, or one in each, is the point at infinity, the transformation is given by (1) with the two factors that contain that point deleted. For instance, when $z_1 = \infty$:
>
> $$
> \frac{(w - w_1)(w_2 - w_3)}{(w - w_3)(w_2 - w_1)} = \frac{z_2 - z_3}{z - z_3} ,
> $$
>
> and when $w_2 = \infty$:
>
> $$
> \frac{w - w_1}{w - w_3} = \frac{(z - z_1)(z_2 - z_3)}{(z - z_3)(z_2 - z_1)} .
> $$
>
> *B&C: Sec. 100 (text)*

^prop-100-4

> [!remark] Remark: Why Deleting Works
> B&C motivates the rule by continuity: replace $z_1$ by $1/z_1$ on the right of (1), clear fractions, and let $z_1 \to 0$:
>
> $$
> \lim_{z_1\to0}\frac{(z - 1/z_1)(z_2 - z_3)}{(z - z_3)(z_2 - 1/z_1)}\cdot\frac{z_1}{z_1} = \lim_{z_1\to0}\frac{(z_1z - 1)(z_2 - z_3)}{(z - z_3)(z_1z_2 - 1)} = \frac{z_2 - z_3}{z - z_3} .
> $$
>
> Each prescribed point occurs once in a numerator and once in a denominator of its side of (1), so the two factors containing it have ratio tending to $1$. The proof below checks the result directly.

^rem-100-1

> [!proof]+ Proof
> Let $R(z)$ be the right side of (1) and $L(w)$ the left side. As noted after Theorem §100.1, $R$ is the linear fractional transformation with $R(z_1) = 0$, $R(z_2) = 1$, $R(z_3) = \infty$. Delete the two factors containing a point at infinity:
> - $z_1 = \infty$: $R(z) = \dfrac{z_2 - z_3}{z - z_3}$ has $R(\infty) = 0$, $R(z_2) = 1$, $R(z_3) = \infty$;
> - $z_2 = \infty$: $R(z) = \dfrac{z - z_1}{z - z_3}$ has $R(z_1) = 0$, $R(\infty) = 1$, $R(z_3) = \infty$;
> - $z_3 = \infty$: $R(z) = \dfrac{z - z_1}{z_2 - z_1}$ has $R(z_1) = 0$, $R(z_2) = 1$, $R(\infty) = \infty$.
>
> In each case $R$ is still linear fractional and still sends the three points to $0, 1, \infty$; the same holds for $L$ and the $w$ points. Then the equation $L(w) = R(z)$ says $w = L^{-1}[R(z)]$, which is linear fractional ([[§99★ Linear Fractional Transformations#^thm-99-4|Theorem §99.4]], [[§99★ Linear Fractional Transformations#^prop-99-5|Proposition §99.5]]) and sends $z_k \mapsto 0, 1, \infty \mapsto w_k$. By Theorem §100.3 it is the required transformation.

^pf-100-4

*Uses:* [[§100★ An Implicit Form#^thm-100-1|§100.1]], [[§100★ An Implicit Form#^thm-100-3|§100.3]], [[§99★ Linear Fractional Transformations#^thm-99-4|§99.4]], [[§99★ Linear Fractional Transformations#^prop-99-5|§99.5]]

> [!remark] Remark: Method — Linear Fractional Transformation by Cross Ratios
> 1. Write (1) with the prescribed points; if one of them is $\infty$, delete the two factors containing it (Proposition §100.4).
> 2. Simplify the constants, clear fractions, and solve the resulting equation (linear in $w$) for $w$.
> 3. Check the three images. To map a circle or line onto another, choose three points on each, keeping the orientation in mind: the region to the left of $z_1 \to z_2 \to z_3$ goes to the region to the left of $w_1 \to w_2 \to w_3$.

^rem-100-2

## Examples

> [!example] Example §100.1: Mapping 2, i, −2 onto 1, i, −1 Again
> For $z_1 = 2$, $z_2 = i$, $z_3 = -2$ and $w_1 = 1$, $w_2 = i$, $w_3 = -1$, equation (1) reads
>
> $$
> \frac{(w - 1)(i + 1)}{(w + 1)(i - 1)} = \frac{(z - 2)(i + 2)}{(z + 2)(i - 2)} .
> $$
>
> Since $\frac{i + 1}{i - 1} = -i$ and $\frac{i + 2}{i - 2} = \frac{(i + 2)(-i - 2)}{(i - 2)(-i - 2)} = \frac{-3 - 4i}{5}$, this is $-5i(w - 1)(z + 2) = (-3 - 4i)(z - 2)(w + 1)$. Collecting the terms in $w$ on the left,
>
> $$
> w\big[-5i(z + 2) + (3 + 4i)(z - 2)\big] = (-3 - 4i)(z - 2) - 5i(z + 2) ,
> $$
>
> that is, $w\big[(3 - i)z - 6 - 18i\big] = (-3 - 9i)z + 6 - 2i$. Divide numerator and denominator by $-3 - 9i$, using $\frac{3 - i}{-3 - 9i} = \frac{i}{3}$, $\frac{-6 - 18i}{-3 - 9i} = 2$ and $\frac{6 - 2i}{-3 - 9i} = \frac{2i}{3}$:
>
> $$
> w = \frac{z + \frac{2i}{3}}{\frac i3 z + 2} = \frac{3z + 2i}{iz + 6} ,
> $$
>
> the transformation found in [[§99★ Linear Fractional Transformations#^ex-99-1|Example §99.1]], as uniqueness (Theorem §100.3) requires.
>
> *B&C: Sec. 100, Example 1*

^ex-100-1

> [!example] Example §100.2: A Point at Infinity in the w Plane
> For $z_1 = 1$, $z_2 = 0$, $z_3 = -1$ and $w_1 = i$, $w_2 = \infty$, $w_3 = 1$, delete the factors containing $w_2$ (Proposition §100.4):
>
> $$
> \frac{w - i}{w - 1} = \frac{(z - 1)(0 + 1)}{(z + 1)(0 - 1)} = -\frac{z - 1}{z + 1} .
> $$
>
> Clearing fractions, $(w - i)(z + 1) = -(z - 1)(w - 1)$, so $w(z + 1) + w(z - 1) = i(z + 1) + (z - 1)$, that is $2zw = (i + 1)z + (i - 1)$:
>
> $$
> w = \frac{(i + 1)z + (i - 1)}{2z} ,
> $$
>
> as in [[§99★ Linear Fractional Transformations#^ex-99-2|Example §99.2]].
>
> *B&C: Sec. 100, Example 2*

^ex-100-2

> [!example] Example §100.3: Mapping −1, 0, 1 onto −i, 1, i
> Equation (1) with $z_1 = -1$, $z_2 = 0$, $z_3 = 1$ and $w_1 = -i$, $w_2 = 1$, $w_3 = i$:
>
> $$
> \frac{(w + i)(1 - i)}{(w - i)(1 + i)} = \frac{(z + 1)(0 - 1)}{(z - 1)(0 + 1)} .
> $$
>
> Since $\frac{1 - i}{1 + i} = -i$, this is $\dfrac{w + i}{w - i} = \dfrac{z + 1}{i(z - 1)}$, so $i(w + i)(z - 1) = (w - i)(z + 1)$. Collecting the terms in $w$: $w\big[i(z - 1) - (z + 1)\big] = -i(z + 1) + (z - 1)$, that is $w\,(i - 1)(z + i) = (1 - i)(z - i)$ (expand to check: $(i - 1)(z + i) = (i - 1)z - 1 - i$ and $(1 - i)(z - i) = (1 - i)z - 1 - i$). Hence
>
> $$
> w = -\frac{z - i}{z + i} = \frac{i - z}{i + z} .
> $$
>
> Check: $z = -1 \mapsto \frac{i + 1}{i - 1} = -i$, $z = 0 \mapsto 1$, $z = 1 \mapsto \frac{i - 1}{i + 1} = i$. This map reappears in [[§102★ Examples (Mappings of the Upper Half Plane)#^ex-102-1|Example §102.1]]: it sends the real axis onto the unit circle and the upper half plane onto the unit disk.
>
> *B&C: Sec. 100, Exercise 1*

^ex-100-3

> [!example] Example §100.4: Infinity on Both Sides
> Find the transformation that maps $z_1 = \infty$, $z_2 = i$, $z_3 = 0$ onto $w_1 = 0$, $w_2 = i$, $w_3 = \infty$.
>
> Delete the factors containing $z_1$ on the right of (1) and those containing $w_3$ on the left:
>
> $$
> \frac{w - w_1}{w_2 - w_1} = \frac{z_2 - z_3}{z - z_3}, \qquad\text{that is}\qquad \frac{w}{i} = \frac{i}{z} .
> $$
>
> So $w = i^2/z = -1/z$. Check: $\infty \mapsto 0$, $i \mapsto -1/i = i$, $0 \mapsto \infty$.
>
> *B&C: Sec. 100, Exercise 3*

^ex-100-4

> [!example] Example §100.5: Fixed Points
> Find the fixed points (Lemma §100.2) of (a) $w = \dfrac{z - 1}{z + 1}$ and (b) $w = \dfrac{6z - 9}{z}$.
>
> **(a)** $\dfrac{z - 1}{z + 1} = z \iff z^2 + z = z - 1 \iff z^2 = -1$, so $z = \pm i$. Here $c = 1 \ne 0$, so $\infty$ is not fixed ($T(\infty) = 1$), and neither is $z = -1$ ($T(-1) = \infty$). The fixed points are $z = \pm i$.
>
> **(b)** $\dfrac{6z - 9}{z} = z \iff z^2 - 6z + 9 = 0 \iff (z - 3)^2 = 0$, so $z = 3$; again $T(\infty) = 6 \ne \infty$. There is just one fixed point, $z = 3$: the bound of Lemma §100.2 need not be attained.
>
> *B&C: Sec. 100, Exercise 7*

^ex-100-5
