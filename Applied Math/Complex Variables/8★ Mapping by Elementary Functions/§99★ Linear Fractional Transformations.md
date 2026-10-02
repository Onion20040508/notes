---
type: section
subject: "[[Complex Variables]]"
chapter: 8
section: 99
bc: "99"
aliases: ["B&C 99"]
tags: [complex-variables, math342, extension]
---
← [[§98★ Mappings by 1∕z]] · ↑ [[· 8★ Mapping by Elementary Functions]] · [[§100★ An Implicit Form]] →

*Brown–Churchill, Section 99.*
★ *Beyond MAT 342: the course skipped this section or left it optional; it is included from Brown–Churchill.*

A linear fractional (Möbius) transformation $w = (az + b)/(cz + d)$ is a linear map, the reciprocal, and another linear map, one after the other. So it inherits the property proved for $1/z$ in [[§98★ Mappings by 1∕z|§98]]: **it maps circles and lines onto circles and lines.** Extended to the point at infinity it is a continuous bijection of the extended plane whose inverse is again linear fractional, and compositions of such maps are linear fractional too. These maps are the workhorses of conformal mapping: there is exactly one carrying any three points to any three points ([[§100★ An Implicit Form|§100]]), and they move half planes and disks into one another ([[§101★ Mappings of the Upper Half Plane|§101]]).

## Definition and Decomposition

> [!definition] Definition §99.1: Linear Fractional Transformation
> A **linear fractional transformation**, or **Möbius transformation**, is a mapping
>
> $$
> w = \frac{az + b}{cz + d} \qquad (ad - bc \ne 0) , \qquad (1)
> $$
>
> where $a$, $b$, $c$, $d$ are complex constants. Since it can be written in the form
>
> $$
> Azw + Bz + Cw + D = 0 \qquad (AD - BC \ne 0) , \qquad (2)
> $$
>
> which is linear in $z$ and linear in $w$, it is also called a **bilinear transformation**.
>
> *B&C: Sec. 99, Equations (1) and (2)*

^def-99-1

> [!theorem] Proposition §99.1: The Two Forms Agree
> Every transformation (1) can be written in the form (2), and every equation (2) can be put in the form (1).
>
> *B&C: Sec. 99 (text)*

^prop-99-1

> [!proof]+ Proof
> Clearing the denominator in (1) gives $czw + dw - az - b = 0$, which is (2) with $A = c$, $B = -a$, $C = d$, $D = -b$; then $AD - BC = -bc + ad \ne 0$. Conversely, solving (2) for $w$ gives $w = \dfrac{-Bz - D}{Az + C}$, which is (1) with $a = -B$, $b = -D$, $c = A$, $d = C$, and $ad - bc = -BC + AD \ne 0$.

^pf-99-1

*Uses:* [[§99★ Linear Fractional Transformations#^def-99-1|Def. §99.1]]

> [!theorem] Proposition §99.2: Decomposition into Simpler Maps
> If $c = 0$, then $ad \ne 0$ and (1) is the nonconstant linear function $w = (a/d)z + b/d$. If $c \ne 0$, then
>
> $$
> w = \frac ac + \frac{bc - ad}{c}\cdot\frac{1}{cz + d} \qquad (ad - bc \ne 0) , \qquad (3)
> $$
>
> so (1) is the composition of the three mappings
>
> $$
> Z = cz + d, \qquad W = \frac1Z, \qquad w = \frac ac + \frac{bc - ad}{c}\,W .
> $$
>
> In either case the condition $ad - bc \ne 0$ ensures that (1) is not a constant function.
>
> *B&C: Sec. 99, Equation (3)*

^prop-99-2

> [!proof]+ Proof
> If $c = 0$, the condition reads $ad \ne 0$, and dividing by $d$ gives the linear function, nonconstant because $a/d \ne 0$. If $c \ne 0$, put the right side of (3) over the common denominator $c(cz + d)$:
>
> $$
> \frac{a(cz + d) + bc - ad}{c(cz + d)} = \frac{acz + bc}{c(cz + d)} = \frac{az + b}{cz + d} .
> $$
>
> The last of the three maps is linear with nonzero coefficient $(bc - ad)/c$, so the composition is not constant.

^pf-99-2

*Uses:* [[§96★ Linear Transformations#^def-96-1|Def. §96.1]]

> [!theorem] Corollary §99.3: Circles and Lines Go to Circles and Lines
> Every linear fractional transformation transforms circles and lines into circles and lines.
>
> *B&C: Sec. 99 (text)*

^cor-99-3

> [!proof]+ Proof
> By Proposition §99.2, the transformation is either a linear map, or a linear map, the reciprocal and a linear map in succession. A linear map takes circles to circles and lines to lines (it is a similarity, [[§96★ Linear Transformations#^prop-96-1|Proposition §96.1]]), and $1/z$ takes circles and lines to circles and lines ([[§98★ Mappings by 1∕z#^thm-98-3|Theorem §98.3]]). A composition of maps with this property has it.

^pf-99-3

*Uses:* [[§99★ Linear Fractional Transformations#^prop-99-2|§99.2]], [[§96★ Linear Transformations#^prop-96-1|§96.1]], [[§98★ Mappings by 1∕z#^thm-98-3|§98.3]]

## The Extended Plane and the Inverse

Solving (1) for $z$ gives

$$
z = \frac{-dw + b}{cw - a} \qquad (ad - bc \ne 0) , \qquad (4)
$$

which recovers $z$ from its image, except that when $c \ne 0$ the value $w = a/c$ makes the denominator vanish. The gap is filled at infinity.

> [!definition] Definition §99.2: Linear Fractional Transformation on the Extended Plane
> For $ad - bc \ne 0$ write
>
> $$
> T(z) = \frac{az + b}{cz + d} \qquad (5)
> $$
>
> at the finite points where $cz + d \ne 0$, and set
>
> $$
> T(\infty) = \infty \quad\text{if } c = 0 ; \qquad (6)
> $$
>
> $$
> T(\infty) = \frac ac \quad\text{and}\quad T\Big(-\frac dc\Big) = \infty \quad\text{if } c \ne 0 . \qquad (7)
> $$
>
> For $T(z) = 1/z$ this agrees with [[§97★ The Transformation w = 1∕z#^def-97-2|Definition §97.2]].
>
> *B&C: Sec. 99, Equations (5)–(7)*

^def-99-2

> [!theorem] Theorem §99.4: Continuity, Bijectivity and the Inverse
> With Definition §99.2, $T$ is continuous on the extended $z$ plane and is a one-to-one mapping of the extended $z$ plane onto the extended $w$ plane. Its inverse, defined by $T^{-1}(w) = z$ if and only if $T(z) = w$, is the linear fractional transformation
>
> $$
> T^{-1}(w) = \frac{-dw + b}{cw - a} \qquad (ad - bc \ne 0) , \qquad (8)
> $$
>
> with
>
> $$
> T^{-1}(\infty) = \infty \quad\text{if } c = 0 ; \qquad (9)
> $$
>
> $$
> T^{-1}\Big(\frac ac\Big) = \infty \quad\text{and}\quad T^{-1}(\infty) = -\frac dc \quad\text{if } c \ne 0 . \qquad (10)
> $$
>
> In particular $T^{-1}[T(z)] = z$ for each point of the extended plane.
>
> *B&C: Sec. 99 (text)*

^thm-99-4

> [!proof]+ Proof
> **Continuity.** (B&C refers this to Sec. 18, Exercise 11, which is [[§17 Limits Involving the Point at Infinity#^prop-17-2|Proposition §17.2]]; here are the cases.) Use [[§17 Limits Involving the Point at Infinity#^thm-17-1|Theorem §17.1]]: $\lim_{z\to z_0} f(z) = \infty$ if and only if $\lim_{z\to z_0} 1/f(z) = 0$, and $\lim_{z\to\infty} f(z) = w_0$ if and only if $\lim_{z\to0} f(1/z) = w_0$.
> - At a finite $z_0$ with $cz_0 + d \ne 0$, $T$ is a quotient of polynomials with nonzero denominator, hence continuous ([[§18 Continuity#^prop-18-1|Proposition §18.1]]).
> - If $c \ne 0$ and $z_0 = -d/c$, then $az_0 + b = (bc - ad)/c \ne 0$, so $1/T(z) = (cz + d)/(az + b) \to 0$; hence $T(z) \to \infty = T(-d/c)$.
> - At $z_0 = \infty$: for $z \ne 0$, $T(1/z) = \dfrac{a + bz}{c + dz}$. If $c \ne 0$ this tends to $a/c = T(\infty)$ as $z \to 0$. If $c = 0$, then $a \ne 0$ and $1/T(1/z) = dz/(a + bz) \to 0$, so $T(1/z) \to \infty = T(\infty)$.
>
> **One to one and onto.** Let $w$ be finite, and if $c \ne 0$ let also $w \ne a/c$. For a finite $z$ with $cz + d \ne 0$,
>
> $$
> w = \frac{az + b}{cz + d} \iff w(cz + d) = az + b \iff z(cw - a) = -dw + b ,
> $$
>
> and $cw - a \ne 0$ (if $c = 0$ this is $-a \ne 0$). So the only candidate is $z$ of (4), and it is admissible: $cz + d = \dfrac{c(-dw + b) + d(cw - a)}{cw - a} = \dfrac{bc - ad}{cw - a} \ne 0$. The remaining values: if $c = 0$, the point $w = \infty$ comes only from $z = \infty$ by (6), since $T$ is finite at every finite point. If $c \ne 0$, the point $w = \infty$ comes only from $z = -d/c$ by (7); and $w = a/c$ comes only from $z = \infty$, because a finite $z$ with $T(z) = a/c$ would give $0 = z(c\frac ac - a) = -\frac{ad}{c} + b = \frac{bc - ad}{c}$, which is false. So every point of the extended $w$ plane has exactly one preimage, and $T^{-1}$ is given by (4), that is by (8), together with (9) and (10).
>
> **$T^{-1}$ is linear fractional**, since $(-d)(-a) - bc = ad - bc \ne 0$; and (9), (10) are exactly the rules (6), (7) for its coefficients $-d$, $b$, $c$, $-a$.

^pf-99-4

*Uses:* [[§99★ Linear Fractional Transformations#^def-99-2|Def. §99.2]], [[§17 Limits Involving the Point at Infinity#^thm-17-1|§17.1]], [[§17 Limits Involving the Point at Infinity#^prop-17-2|§17.2]], [[§18 Continuity#^prop-18-1|§18.1]]

> [!theorem] Proposition §99.5: Compositions
> If $T(z) = \dfrac{a_1z + b_1}{c_1z + d_1}$ and $S(z) = \dfrac{a_2z + b_2}{c_2z + d_2}$ are linear fractional transformations, then so is $S[T(z)]$:
>
> $$
> S[T(z)] = \frac{a_3z + b_3}{c_3z + d_3}, \qquad \begin{bmatrix} a_3 & b_3 \\ c_3 & d_3 \end{bmatrix} = \begin{bmatrix} a_2 & b_2 \\ c_2 & d_2 \end{bmatrix}\begin{bmatrix} a_1 & b_1 \\ c_1 & d_1 \end{bmatrix} ,
> $$
>
> and $a_3d_3 - b_3c_3 = (a_1d_1 - b_1c_1)(a_2d_2 - b_2c_2) \ne 0$.
>
> *B&C: Sec. 99 (text); Sec. 100, Exercise 5*

^prop-99-5

> [!proof]+ Proof
> At a finite $z$ where $T(z)$ is finite and $S$ is finite at $T(z)$, multiply numerator and denominator of $S[T(z)] = \dfrac{a_2T(z) + b_2}{c_2T(z) + d_2}$ by $c_1z + d_1$:
>
> $$
> S[T(z)] = \frac{a_2(a_1z + b_1) + b_2(c_1z + d_1)}{c_2(a_1z + b_1) + d_2(c_1z + d_1)} = \frac{(a_2a_1 + b_2c_1)z + (a_2b_1 + b_2d_1)}{(c_2a_1 + d_2c_1)z + (c_2b_1 + d_2d_1)} ,
> $$
>
> and these coefficients are the entries of the matrix product. The determinant of a product is the product of the determinants, which gives $a_3d_3 - b_3c_3$. So $S \circ T$ agrees with the linear fractional transformation $R(z) = (a_3z + b_3)/(c_3z + d_3)$ at all but finitely many points of the extended plane. Both are continuous there (Theorem §99.4, applied to $T$, $S$ and $R$), and every one of the finitely many exceptional points is a limit of points where they agree, so they agree everywhere.

^pf-99-5

*Uses:* [[§99★ Linear Fractional Transformations#^thm-99-4|§99.4]]

> [!remark]- Connections
> - The correspondence $\begin{bmatrix} a & b \\ c & d\end{bmatrix} \mapsto T$ turns matrix multiplication in $GL_2(\mathbb{C})$, [[§3 Basic Examples of Groups#^def-3-6|493 Def. §3.6]], into composition of maps, and the inverse matrix gives $T^{-1}$ of (8) up to the factor $1/(ad - bc)$. So the linear fractional transformations form a group under composition, the image of $GL_2(\mathbb{C})$; two matrices give the same map exactly when they are proportional.

There is always a linear fractional transformation that maps three given distinct points $z_1, z_2, z_3$ onto three specified distinct points $w_1, w_2, w_3$, and only one; this is proved in [[§100★ An Implicit Form#^thm-100-1|Theorem §100.1]] and [[§100★ An Implicit Form#^thm-100-3|Theorem §100.3]]. The examples below find it directly.

> [!remark] Remark: Method — The Transformation Through Three Given Points, Directly
> 1. Write $w = (az + b)/(cz + d)$ and turn each requirement $T(z_k) = w_k$ into a linear equation in $a, b, c, d$: $az_k + b = w_k(cz_k + d)$.
> 2. A point at infinity gives a simpler condition: $T(z_k) = \infty$ means $cz_k + d = 0$; $T(\infty) = w_k$ means $c \ne 0$ and $a = w_kc$; $T(\infty) = \infty$ means $c = 0$.
> 3. Three conditions leave one free nonzero factor, which cancels. Check $ad - bc \ne 0$ and the three images.
>
> The cross-ratio formula of [[§100★ An Implicit Form|§100]] does the same job in one step.

^rem-99-1

## Examples

> [!example] Example §99.1: Mapping 2, i, −2 onto 1, i, −1
> Find the linear fractional transformation $w = (az + b)/(cz + d)$ that maps $z_1 = 2$, $z_2 = i$, $z_3 = -2$ onto $w_1 = 1$, $w_2 = i$, $w_3 = -1$.
>
> Since $1$ is the image of $2$ and $-1$ the image of $-2$,
>
> $$
> 2c + d = 2a + b \qquad\text{and}\qquad 2c - d = -2a + b .
> $$
>
> Adding gives $b = 2c$; then the first equation gives $d = 2a$, so
>
> $$
> w = \frac{az + 2c}{cz + 2a} \qquad [\,2(a^2 - c^2) \ne 0\,] . \qquad (11)
> $$
>
> Since $i$ is to go to $i$, $ai + 2c = i(ci + 2a) = -c + 2ai$, so $3c = ai$ and $c = ai/3$. Then
>
> $$
> w = \frac{az + \frac{2ai}{3}}{\frac{ai}{3}z + 2a} = \frac{z + \frac{2i}{3}}{\frac i3 z + 2} = \frac{3z + 2i}{iz + 6} , \qquad (12)
> $$
>
> after cancelling $a \ne 0$ and multiplying by $3$. Check: $ad - bc = 3 \cdot 6 - 2i \cdot i = 20 \ne 0$, and $\frac{6 + 2i}{2i + 6} = 1$, $\frac{3i + 2i}{-1 + 6} = i$, $\frac{-6 + 2i}{-2i + 6} = -1$.
>
> *B&C: Sec. 99, Example 1*

^ex-99-1

> [!example] Example §99.2: A Point Goes to Infinity
> Find the linear fractional transformation that maps $z_1 = 1$, $z_2 = 0$, $z_3 = -1$ onto $w_1 = i$, $w_2 = \infty$, $w_3 = 1$.
>
> Since $\infty$ is the image of $0$, (6) and (7) give $c \ne 0$ and $d = 0$ ($T(-d/c) = \infty$ with $-d/c = 0$), so
>
> $$
> w = \frac{az + b}{cz} \qquad (bc \ne 0) . \qquad (13)
> $$
>
> The conditions $1 \mapsto i$ and $-1 \mapsto 1$ read
>
> $$
> ic = a + b, \qquad -c = -a + b ,
> $$
>
> and adding and subtracting give $2b = (i - 1)c$, $2a = (1 + i)c$. Multiplying numerator and denominator of (13) by $2$ and cancelling $c$,
>
> $$
> w = \frac{(i + 1)z + (i - 1)}{2z} . \qquad (14)
> $$
>
> Check: $z = 1$ gives $\frac{2i}{2} = i$, $z = -1$ gives $\frac{-2}{-2} = 1$, and $z = 0$ gives $\infty$.
>
> *B&C: Sec. 99, Example 2*

^ex-99-2

> [!example] Example §99.3: When Is a Transformation Its Own Inverse?
> Let $T(z) = (az + b)/(cz + d)$, $ad - bc \ne 0$, be any linear fractional transformation other than $T(z) = z$. Show that $T^{-1} = T$ if and only if $d = -a$.
>
> By (8), $T^{-1}(z) = (-dz + b)/(cz - a)$. At the finite points where both are finite, $T^{-1}(z) = T(z)$ means $(az + b)(cz - a) = (-dz + b)(cz + d)$. Expanding,
>
> $$
> acz^2 + (bc - a^2)z - ab = -cdz^2 + (bc - d^2)z + bd ,
> $$
>
> that is,
>
> $$
> (a + d)\big[cz^2 + (d - a)z - b\big] = 0 .
> $$
>
> If $d = -a$, this holds at every such $z$, and by continuity (Theorem §99.4) $T^{-1} = T$ on the whole extended plane. Conversely, if $T^{-1} = T$ and $a + d \ne 0$, the polynomial $cz^2 + (d - a)z - b$ would vanish at infinitely many points, so $c = 0$, $d = a$, $b = 0$, and $T(z) = az/a = z$, which was excluded. Hence $d = -a$. For example $T(z) = \frac{z - 1}{z + 1}$ is not its own inverse ($d = 1 \ne -1 = -a$), but $\frac{z + 1}{z - 1}$ is.
>
> *B&C: Sec. 100, Exercise 12*

^ex-99-3
