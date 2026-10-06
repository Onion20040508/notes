---
type: section
subject: "[[Complex Variables]]"
chapter: 4
section: 50
bc: "50"
aliases: ["B&C 50"]
tags: [complex-variables, math342]
---
← [[§49 Proof of the Theorem (Antiderivatives)]] · ↑ [[· 4 Integrals]] · [[§51 Proof of the Theorem (Cauchy–Goursat Theorem)]] →

*Brown–Churchill, Section 50.*

By [[§49 Proof of the Theorem (Antiderivatives)#^thm-49-1|Theorem §49.1]], a function with an antiderivative on a domain $D$ integrates to zero around every closed contour in $D$. This section gives a condition of a different kind, analyticity inside and on a simple closed contour $C$, that forces $\int_C f(z)\,dz = 0$; it is the central theorem of the theory, and the course singled it out as a very important theorem. Writing $f = u + iv$ and $dz = dx + i\,dy$ turns the contour integral into two real line integrals, and if $f'$ is continuous, Green's theorem turns these into double integrals whose integrands are exactly the two Cauchy–Riemann expressions, hence zero. This is Cauchy's original argument. Goursat showed that the continuity of $f'$ can be dropped; the resulting **Cauchy–Goursat theorem** is stated here and proved in [[§51 Proof of the Theorem (Cauchy–Goursat Theorem)#^thm-51-3|§51]]. Physically, it says that a two-dimensional flow that is both irrotational and source-free has zero circulation and zero flux around every closed curve enclosing no singularity.

## Contour Integrals as Real Line Integrals

We let $C$ denote a simple closed contour $z = z(t)$ $(a \le t \le b)$, described in the **positive sense** (counterclockwise), and assume that $f$ is analytic at each point interior to and on $C$. By definition (2) of [[§44 Contour Integrals#^def-44-1|§44]],
$$
\int_C f(z)\,dz = \int_a^b f[z(t)]\,z'(t)\,dt ; \qquad (1)
$$
and if $f(z) = u(x, y) + iv(x, y)$ and $z(t) = x(t) + iy(t)$, the integrand $f[z(t)]z'(t)$ is the product of $u[x(t), y(t)] + iv[x(t), y(t)]$ and $x'(t) + iy'(t)$.

> [!theorem] Proposition §50.1: Contour Integrals in Terms of Real Line Integrals
> Let $C$ be a contour $z(t) = x(t) + iy(t)$ $(a \le t \le b)$ and let $f(z) = u(x, y) + iv(x, y)$ be piecewise continuous on $C$. Then
>
> $$
> \int_C f(z)\,dz = \int_a^b (ux' - vy')\,dt + i\int_a^b (vx' + uy')\,dt , \qquad (2)
> $$
>
> that is, in terms of line integrals of real-valued functions of two real variables,
>
> $$
> \int_C f(z)\,dz = \int_C u\,dx - v\,dy + i\int_C v\,dx + u\,dy . \qquad (3)
> $$
>
> Formally, (3) is obtained by replacing $f(z)$ and $dz$ on the left by the binomials $u + iv$ and $dx + i\,dy$ and expanding their product.
>
> *B&C: Sec. 50 (text)*

^prop-50-1

> [!proof]+ Proof
> Multiply out: $(u + iv)(x' + iy') = (ux' - vy') + i(vx' + uy')$, where $u$, $v$ are evaluated at $(x(t), y(t))$. By definition (1) and [[§42 Definite Integrals of Functions w(t)#^def-42-1|Definition §42.1]], the integral of this function of $t$ is (2). The real line integrals in (3) are defined by $\int_C P\,dx + Q\,dy = \int_a^b \big(P[x(t), y(t)]\,x'(t) + Q[x(t), y(t)]\,y'(t)\big)\,dt$, so (2) and (3) say the same thing.

^pf-50-1

*Uses:* [[§44 Contour Integrals#^def-44-1|Def. §44.1]], [[§42 Definite Integrals of Functions w(t)#^def-42-1|Def. §42.1]], [[§108 Line Integrals#^def-108-4|Calc Def. §108.4]] (line integrals with respect to $x$ and $y$)

> [!remark] Remark: Circulation and Flux
> If $f = u + iv$, the vector field $\mathbf{V} = (u, -v)$, the conjugate $\overline{f}$ read as a vector, satisfies $\mathbf{V}\cdot d\mathbf{r} = u\,dx - v\,dy$ and $\mathbf{V}\cdot\mathbf{n}\,ds = u\,dy + v\,dx$ for the outward normal of a positively oriented curve. So (3) reads
>
> $$
> \int_C f(z)\,dz = \int_C \mathbf{V}\cdot d\mathbf{r} + i\int_C \mathbf{V}\cdot\mathbf{n}\,ds = \text{circulation} + i\,\text{flux}
> $$
>
> of $\mathbf{V}$ around $C$. In fluid flow, $f$ is the derivative of the complex potential and $\mathbf{V}$ the velocity; the Cauchy–Riemann equations for $f$ say that $\mathbf{V}$ is irrotational ([[§111 Curl and Divergence#^def-111-2|Calc Def. §111.2]]) and divergence-free ([[§111 Curl and Divergence#^def-111-3|Calc Def. §111.3]]).

^rem-50-1

## Cauchy's Theorem (with f′ Continuous)

Expression (3) is valid for any contour and any piecewise continuous $f$. For a simple closed contour, the line integrals in (3) can be converted to double integrals by Green's theorem from calculus: if two real-valued functions $P(x, y)$ and $Q(x, y)$, together with their first-order partial derivatives, are continuous throughout the closed region $R$ consisting of all points interior to and on the simple closed contour $C$, then
$$
\int_C P\,dx + Q\,dy = \iint_R (Q_x - P_y)\,dA .
$$

> [!theorem] Theorem §50.2: Cauchy's Theorem (f′ Continuous)
> Let $C$ be a simple closed contour, and let $R$ be the closed region consisting of the points interior to and on $C$. If a function $f$ is analytic in $R$ and $f'$ is continuous there, then
>
> $$
> \int_C f(z)\,dz = 0 . \qquad (5)
> $$
>
> This holds for either orientation of $C$.
>
> *B&C: Sec. 50 (text)*

^thm-50-2

> [!proof]+ Proof
> First let $C$ be positively oriented. Since $f$ is analytic in $R$, it is continuous there, and so are $u$ and $v$. Since $f'$ is continuous on $R$, so are the first-order partial derivatives of $u$ and $v$: by the Cauchy–Riemann equations ([[§21 Cauchy–Riemann Equations#^thm-21-1|Theorem §21.1]]),
>
> $$
> f' = u_x + iv_x = v_y - iu_y ,
> $$
>
> so $u_x = \operatorname{Re} f'$, $v_x = \operatorname{Im} f'$, $v_y = \operatorname{Re} f'$ and $u_y = -\operatorname{Im} f'$ are continuous. Green's theorem applies to both line integrals in (3), with $P = u$, $Q = -v$ and with $P = v$, $Q = u$:
>
> $$
> \int_C f(z)\,dz = \iint_R (-v_x - u_y)\,dA + i\iint_R (u_x - v_y)\,dA . \qquad (4)
> $$
>
> In view of the Cauchy–Riemann equations $u_x = v_y$, $u_y = -v_x$, the integrands of these two double integrals are zero throughout $R$. This proves (5).
>
> If $C$ is taken in the clockwise direction, then $-C$ is positively oriented, and by property (6) of [[§44 Contour Integrals#^thm-44-2|Theorem §44.2]]
>
> $$
> \int_C f(z)\,dz = -\int_{-C} f(z)\,dz = 0 .
> $$
>
> (On the hypothesis: B&C's form of Green's theorem asks for continuity of $P$, $Q$ and their partials on $R$. The rigorous version in the vault asks for continuity on an open set containing $R$; that holds whenever $f'$ is continuous on an open set containing $R$, as in all the applications below. The Cauchy–Goursat theorem removes the hypothesis on $f'$ altogether.)

^pf-50-2

*Uses:* [[§50 Cauchy–Goursat Theorem#^prop-50-1|§50.1]], [[§21 Cauchy–Riemann Equations#^thm-21-1|§21.1]] (Cauchy–Riemann equations and $f' = u_x + iv_x$), [[§110 Green's Theorem#^thm-110-1|Calc Thm. §110.1]] (Green's theorem), [[§44 Contour Integrals#^thm-44-2|§44.2]], [[§43 Contours#^thm-43-4|§43.4]] (the interior of $C$)

> [!remark]- Connections
> - Green's theorem: [[§110 Green's Theorem#^thm-110-1|Calc Thm. §110.1]], proved rigorously in [[§16 Line Integrals and Green's Theorem#^thm-16-1|452 Thm. §16.1]] (for $C^1$ functions on an open set containing the closed region). The two integrands $Q_x - P_y$ in (4) are the curl and the divergence of the field $\mathbf{V} = (u, -v)$ of the remark on circulation and flux above, so Theorem §50.2 is "curl-free and divergence-free fields have zero circulation and zero flux".
> - Cauchy's theorem says that the real 1-forms $u\,dx - v\,dy$ and $v\,dx + u\,dy$ are closed (that is the Cauchy–Riemann equations); on a region without holes closed forms are exact, which is the antiderivative of [[§52 Simply Connected Domains#^cor-52-2|Corollary §52.2]].

This result was obtained by Cauchy in the early part of the nineteenth century.

> [!example] Example §50.1: An Entire Function
> If $C$ is any simple closed contour, in either direction, then
>
> $$
> \int_C \sin(z^2)\,dz = 0 .
> $$
>
> The composite function $f(z) = \sin(z^2)$ is analytic everywhere, and its derivative $f'(z) = 2z\cos(z^2)$ is continuous everywhere ([[§37 The Trigonometric Functions sin z and cos z#^thm-37-1|Theorem §37.1]], chain rule [[§20 Rules for Differentiation#^thm-20-4|Theorem §20.4]]). Theorem §50.2 applies to every simple closed contour.
>
> *B&C: Sec. 50, Example*

^ex-50-1

## The Cauchy–Goursat Theorem

Goursat was the first to prove that *the condition of continuity on $f'$ can be omitted*. Its removal is important: it will allow us to show, for example, that the derivative $f'$ of an analytic function $f$ is analytic without having to assume the continuity of $f'$ ([[§57 Some Consequences of the Extension#^thm-57-1|Theorem §57.1]]), which follows as a consequence. (Assuming continuity of $f'$ here and then deducing it later would be circular.) The revised form of Cauchy's result is the **Cauchy–Goursat theorem**, proved in the next section as [[§51 Proof of the Theorem (Cauchy–Goursat Theorem)#^thm-51-3|Theorem §51.3]]:

**Theorem (Cauchy–Goursat).** *If a function $f$ is analytic at all points interior to and on a simple closed contour $C$, then*
$$
\int_C f(z)\,dz = 0 .
$$

The proof in [[§51 Proof of the Theorem (Cauchy–Goursat Theorem)|§51]] takes $C$ positively oriented; the other orientation follows as in the proof of Theorem §50.2. B&C remarks that a reader who wishes to accept the theorem without proof may pass directly to §52. Extensions to closed contours that cross themselves and to domains without holes are in [[§52 Simply Connected Domains#^thm-52-1|Theorem §52.1]], and to regions with holes in [[§53 Multiply Connected Domains#^thm-53-1|Theorem §53.1]].

> [!remark] Remark: Method — Showing That an Integral Around a Closed Contour Is Zero
> 1. **Locate the trouble.** Find where $f$ fails to be analytic: zeros of denominators, branch cuts ([[§33 Branches and Derivatives of Logarithms#^def-33-3|Definition §33.3]]) of logarithms and powers, points where $f$ involves $\bar z$, $|z|$, $\operatorname{Re} z$.
> 2. **Check the region.** If none of these points lies inside or on the simple closed contour $C$, then $\int_C f(z)\,dz = 0$ by the Cauchy–Goursat theorem (and, if $f'$ is visibly continuous there, already by Theorem §50.2). The orientation of $C$ does not matter.
> 3. **Alternatively**, if $f$ has an antiderivative on a domain containing $C$, the integral is zero by [[§49 Proof of the Theorem (Antiderivatives)#^thm-49-1|Theorem §49.1]]; this works for closed contours that are not simple.
> 4. **If a trouble point lies inside $C$**, the integral need not vanish ($\int_{|z|=1} dz/z = 2\pi i$); it is computed by deforming $C$ ([[§53 Multiply Connected Domains#^cor-53-2|Corollary §53.2]]), by the Cauchy integral formula ([[§54 Cauchy Integral Formula#^thm-54-1|Theorem §54.1]]) or by residues ([[§76 Cauchy's Residue Theorem#^thm-76-1|Theorem §76.1]]). The hypothesis is sufficient, not necessary: $\int_{|z|=1} dz/z^2 = 0$ although $1/z^2$ is not analytic at $0$ ([[§48 Antiderivatives#^ex-48-2|Example §48.2]]).

^rem-50-2

## Examples

> [!example] Example §50.2: Checking Analyticity Inside the Unit Circle
> Show that $\int_C f(z)\,dz = 0$ when $C$ is the unit circle $|z| = 1$, in either direction, and
>
> $$
> \text{(a)}\ f(z) = \frac{z^2}{z - 3}, \qquad \text{(d)}\ f(z) = \operatorname{sech} z, \qquad \text{(e)}\ f(z) = \tan z .
> $$
>
> **(a)** $f$ is analytic except at $z = 3$, which lies outside $C$; its derivative $\frac{2z(z - 3) - z^2}{(z - 3)^2} = \frac{z^2 - 6z}{(z - 3)^2}$ is continuous on $|z| \le 1$.
>
> **(d)** $\operatorname{sech} z = 1/\cosh z$ fails to be analytic only at the zeros of $\cosh z$, which are $z = \big(\frac\pi2 + n\pi\big)i$ $(n = 0, \pm1, \ldots)$ ([[§39★ Hyperbolic Functions#^thm-39-4|Theorem §39.4]]); all have modulus at least $\frac\pi2 > 1$. Its derivative $-\operatorname{sech} z\tanh z$ is continuous on $|z| \le 1$.
>
> **(e)** $\tan z = \sin z/\cos z$ fails to be analytic only at the zeros of $\cos z$, which are $z = \frac\pi2 + n\pi$ ([[§38 Zeros and Singularities of Trigonometric Functions#^thm-38-1|Theorem §38.1]]), again of modulus at least $\frac\pi2 > 1$; its derivative $\sec^2 z$ is continuous on $|z| \le 1$.
>
> In each case $f$ is analytic at all points interior to and on $C$, with $f'$ continuous there, so Theorem §50.2 (and a fortiori the Cauchy–Goursat theorem) gives $\int_C f(z)\,dz = 0$. Numerical quadrature around the circle gives $0$ to working precision in all three cases.
>
> *B&C: Sec. 53, Exercise 1(a), (d), (e)*

^ex-50-2

> [!example] Example §50.3: A Non-Analytic Integrand Through Green's Theorem
> Recompute the integral of $f(z) = y - x - i3x^2$ around the closed contour $OABO$ of [[§45 Some Examples (Contour Integrals)#^ex-45-3|Example §45.3]] (from $0$ up to $i$, across to $1 + i$, back along $y = x$) with formula (4), and see where the Cauchy–Riemann equations fail.
>
> Here $u = y - x$ and $v = -3x^2$, so $u_x = -1$, $u_y = 1$, $v_x = -6x$, $v_y = 0$; the Cauchy–Riemann equations fail everywhere, and the integrands of (4) are
>
> $$
> -v_x - u_y = 6x - 1, \qquad u_x - v_y = -1 .
> $$
>
> The contour bounds the triangle $T$: $0 \le x \le y \le 1$, but it is traversed *clockwise* (up the $y$ axis first, with $T$ on the right), so Green's theorem applies to $-OABO$, and
>
> $$
> \int_{OABO} f(z)\,dz = -\Big[\iint_T (6x - 1)\,dA + i\iint_T (-1)\,dA\Big] .
> $$
>
> With $\iint_T 1\,dA = \frac12$ and $\iint_T x\,dA = \int_0^1\int_0^y x\,dx\,dy = \int_0^1 \frac{y^2}{2}\,dy = \frac16$,
>
> $$
> \int_{OABO} f(z)\,dz = -\Big[\Big(1 - \frac12\Big) - \frac i2\Big] = \frac{-1 + i}{2} ,
> $$
>
> which is $I_1 - I_2$ of [[§45 Some Examples (Contour Integrals)#^ex-45-3|Example §45.3]]. The nonzero value measures, through (4), how far $f$ is from satisfying the Cauchy–Riemann equations inside $C$.
>
> *B&C: Sec. 45, Example 3*

^ex-50-3
