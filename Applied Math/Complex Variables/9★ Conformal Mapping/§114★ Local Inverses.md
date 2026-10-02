---
type: section
subject: "[[Complex Variables]]"
chapter: 9
section: 114
bc: "114"
aliases: ["B&C 114"]
tags: [complex-variables, math342, extension]
---
← [[§113★ Further Examples (Preservation of Angles and Scale Factors)]] · ↑ [[· 9★ Conformal Mapping]] · [[§115★ Harmonic Conjugates]] →

*Brown–Churchill, Section 114.*
★ *Beyond MAT 342: the course skipped this section or left it optional; it is included from Brown–Churchill.*

A transformation that is conformal at $z_0$ can be undone near $f(z_0)$ by an analytic function, its local inverse, whose derivative is $1/f'$. The proof is the real inverse function theorem applied to $(x, y) \mapsto (u, v)$: by the Cauchy–Riemann equations the Jacobian of an analytic map is $|f'(z)|^2$, which is nonzero exactly where the map is conformal, and the same equations, applied to the formulas for the derivatives of the inverse, show that the inverse is again analytic. Local inverses are how one goes back from the simple $w$ region to the physical $z$ region in Chapter 10, and they are the general form of choosing a branch: $\log w$ undoes $e^z$, and a branch of $w^{1/2}$ undoes $z^2$.

## The Local Inverse

> [!definition] Definition §114.1: Local Inverse
> Let $w = f(z)$ and $w_0 = f(z_0)$. A **local inverse** of the transformation at $z_0$ is a transformation $z = g(w)$, defined and analytic in a neighborhood $N$ of $w_0$, such that
>
> $$
> g(w_0) = z_0 \qquad\text{and}\qquad f[g(w)] = w \quad\text{for all } w \text{ in } N .
> $$
>
> *B&C: Sec. 114 (text)*

^def-114-1

The proof uses the Jacobian of the pair of real functions $u$, $v$.

> [!definition] Definition §114.2: Jacobian
> For a transformation $u = u(x, y)$, $v = v(x, y)$ with first-order partial derivatives at $(x, y)$, the determinant
>
> $$
> J = \begin{vmatrix} u_x & u_y \\ v_x & v_y \end{vmatrix} = u_xv_y - v_xu_y
> $$
>
> is the **Jacobian** of the transformation at $(x, y)$.
>
> *B&C: Sec. 114 (text)*

^def-114-2

> [!theorem] Theorem §114.1: Conformal Maps Have Local Inverses
> If $w = f(z)$ is conformal at $z_0$ and $w_0 = f(z_0)$, then there is a unique transformation $z = g(w)$, defined and analytic in a neighborhood $N$ of $w_0$, such that $g(w_0) = z_0$ and $f[g(w)] = w$ for all $w$ in $N$. Moreover
>
> $$
> g'(w) = \frac{1}{f'(z)} \qquad (z = g(w),\ w \text{ in } N), \qquad (1)
> $$
>
> so $z = g(w)$ is itself conformal at $w_0$.
>
> *B&C: Sec. 114 (text) and Exercises 7, 8*

^thm-114-1

> [!proof]+ Proof
> B&C reduces the existence to the inverse function theorem of advanced calculus and leaves the analyticity of $g$ and formula (1) to Exercises 7 and 8; here is the whole argument.
>
> **Smoothness of $u$, $v$.** Since $w = f(z)$ is conformal at $z_0$, $f$ is analytic in some neighborhood of $z_0$ ([[§112★ Preservation of Angles and Scale Factors#^prop-112-2|Proposition §112.2]]). Write $z = x + iy$, $z_0 = x_0 + iy_0$, $f(z) = u(x, y) + iv(x, y)$. Then $u$ and $v$, with their partial derivatives of all orders, are continuous in a neighborhood of $(x_0, y_0)$ ([[§57 Some Consequences of the Extension#^cor-57-2|Corollary §57.2]]).
>
> **The Jacobian.** The pair of equations
>
> $$
> u = u(x, y), \qquad v = v(x, y) \qquad (2)
> $$
>
> is a transformation from that neighborhood into the $uv$ plane. By the Cauchy–Riemann equations $u_x = v_y$, $u_y = -v_x$ ([[§21 Cauchy–Riemann Equations#^thm-21-1|Theorem §21.1]]) and $f'(z) = u_x + iv_x$,
>
> $$
> J = u_xv_y - v_xu_y = (u_x)^2 + (v_x)^2 = |f'(z)|^2 ,
> $$
>
> and $J \ne 0$ at $(x_0, y_0)$ because $f'(z_0) \ne 0$.
>
> **The real inverse.** Continuous first partials and $J \ne 0$ at $(x_0, y_0)$ are the hypotheses of the inverse function theorem ([[§13 The Inverse Function Theorem#^thm-13-2|452 Thm. §13.2]]). With $u_0 = u(x_0, y_0)$, $v_0 = v(x_0, y_0)$ (3), it gives a continuous transformation
>
> $$
> x = x(u, v), \qquad y = y(u, v), \qquad (4)
> $$
>
> defined on a neighborhood $N$ of $(u_0, v_0)$ and taking $(u_0, v_0)$ to $(x_0, y_0)$, such that (2) holds when (4) holds; the functions (4) have continuous first-order partial derivatives, and the Jacobian matrix of (4) is the inverse of that of (2):
>
> $$
> x_u = \frac1Jv_y, \qquad x_v = -\frac1Ju_y, \qquad y_u = -\frac1Jv_x, \qquad y_v = \frac1Ju_x \qquad (5)
> $$
>
> throughout $N$, the right sides evaluated at $(x(u, v), y(u, v))$. Shrinking $N$ to a disk, we may take $N$ connected.
>
> **$g$ is analytic (Exercise 7).** With $w = u + iv$, $w_0 = u_0 + iv_0$, put
>
> $$
> g(w) = x(u, v) + iy(u, v) . \qquad (6)
> $$
>
> Then (2) and (4) read $w = f(z)$ and $z = g(w)$, so $g(w_0) = z_0$ and $f[g(w)] = w$ in $N$. By (5) and the Cauchy–Riemann equations for $u$, $v$,
>
> $$
> x_u = \frac{v_y}{J} = \frac{u_x}{J} = y_v, \qquad x_v = -\frac{u_y}{J} = \frac{v_x}{J} = -y_u ,
> $$
>
> so $x$ and $y$ satisfy the Cauchy–Riemann equations $x_u = y_v$, $x_v = -y_u$ in $N$, and their first partials are continuous there. By the sufficient conditions for differentiability ([[§23 Sufficient Conditions for Differentiability#^thm-23-1|Theorem §23.1]]), $g$ is differentiable at every point of the open set $N$, that is, analytic in $N$.
>
> **Formula (1) (Exercise 8).** Differentiate $f[g(w)] = w$ by the chain rule ([[§20 Rules for Differentiation#^thm-20-4|Theorem §20.4]]): $f'[g(w)]\,g'(w) = 1$. Hence $f'(z) \ne 0$ at $z = g(w)$ and $g'(w) = 1/f'(z)$. (Directly from (5): $g'(w) = x_u + iy_u = (u_x - iv_x)/J = \overline{f'(z)}/|f'(z)|^2 = 1/f'(z)$.) In particular $g'(w_0) = 1/f'(z_0) \ne 0$, so $g$ is conformal at $w_0$.
>
> **Uniqueness.** The inverse function theorem also provides a neighborhood $U$ of $z_0$ on which $f$ is one-to-one (B&C's "unique continuous transformation"). Let $g_1$ and $g_2$ be continuous near $w_0$ with $g_1(w_0) = g_2(w_0) = z_0$ and $f[g_1(w)] = f[g_2(w)] = w$. By continuity there is a disk $N'$ about $w_0$ with $g_1(N') \subset U$ and $g_2(N') \subset U$; for $w$ in $N'$ the points $g_1(w)$, $g_2(w)$ of $U$ have the same image $w$, so $g_1(w) = g_2(w)$. Thus two local inverses agree near $w_0$; if both are analytic on a common domain containing $w_0$, they agree on all of it ([[§28★ Uniquely Determined Analytic Functions#^thm-28-2|Theorem §28.2]]).

^pf-114-1

*Uses:* [[§114★ Local Inverses#^def-114-1|Def. §114.1]], [[§114★ Local Inverses#^def-114-2|Def. §114.2]], [[§112★ Preservation of Angles and Scale Factors#^prop-112-2|§112.2]], [[§57 Some Consequences of the Extension#^cor-57-2|§57.2]], [[§21 Cauchy–Riemann Equations#^thm-21-1|§21.1]], [[§23 Sufficient Conditions for Differentiability#^thm-23-1|§23.1]], [[§20 Rules for Differentiation#^thm-20-4|§20.4]] (chain rule), [[§28★ Uniquely Determined Analytic Functions#^thm-28-2|§28.2]], [[§13 The Inverse Function Theorem#^thm-13-2|452 Thm. §13.2]] (inverse function theorem)

> [!remark]- Connections
> - The real inverse function theorem in the plane, with the formula $J^{-1}$ for the Jacobian matrix of the inverse used in (5): [[§13 The Inverse Function Theorem#^thm-13-2|452 Thm. §13.2]], and the Jacobian, [[§13 The Inverse Function Theorem#^def-13-1|452 Def. §13.1]]. The complex theorem adds only that for an analytic $f$ the Jacobian is $|f'|^2$ and that the inverse again satisfies the Cauchy–Riemann equations.
> - The one-variable analogue, where the hypothesis is $f'(x_0) \ne 0$: [[§29 The Mean Value Theorem#^thm-29-10|451 Thm. §29.10]].

## Examples

> [!example] Example §114.1: Local Inverses of the Exponential Function
> By [[§112★ Preservation of Angles and Scale Factors#^ex-112-1|Example §112.1]], $w = e^z$ is conformal everywhere, in particular at $z_0 = 2\pi i$, whose image is $w_0 = e^{2\pi i} = 1$. Find the local inverse there.
>
> Write points of the $w$ plane as $w = \rho e^{i\phi}$. The local inverse is $g(w) = \log w$, the branch
>
> $$
> \log w = \ln\rho + i\phi \qquad (\rho > 0,\ \pi < \phi < 3\pi)
> $$
>
> of the logarithm ([[§33 Branches and Derivatives of Logarithms#^def-33-1|Definition §33.1]], [[§33 Branches and Derivatives of Logarithms#^thm-33-1|Theorem §33.1]]), restricted to any neighborhood of $w_0$ that does not contain the origin. Indeed $g(1) = \ln 1 + i2\pi = 2\pi i$, and for $w$ in the neighborhood $f[g(w)] = \exp(\log w) = w$. Also
>
> $$
> g'(w) = \frac{d}{dw}\log w = \frac1w = \frac{1}{\exp z} ,
> $$
>
> in accordance with (1), since $f'(z) = e^z$. If instead $z_0 = 0$ is chosen (again $w_0 = 1$), the principal branch $\operatorname{Log} w = \ln\rho + i\phi$ $(\rho > 0,\ -\pi < \phi < \pi)$ serves as $g$, and $g(1) = 0$. The same point $w_0$ has different local inverses at different preimages $z_0$.
>
> *B&C: Sec. 114, Example*

^ex-114-1

> [!example] Example §114.2: Local Inverses of z²
> Find the local inverse of $w = z^2$ at $z_0 = 2$, $z_0 = -2$ and $z_0 = -i$.
>
> In each case $f'(z_0) = 2z_0 \ne 0$, so Theorem §114.1 applies, and the local inverse is a branch of $w^{1/2} = \sqrt\rho\,e^{i\phi/2}$ ($w = \rho e^{i\phi}$, $\rho > 0$) whose value at $w_0 = z_0^2$ is $z_0$ ([[§108★ Mappings by Branches of z^(1∕2)#^def-108-2|Definition §108.2]]).
>
> **(a) $z_0 = 2$, $w_0 = 4$.** The principal branch, $-\pi < \phi < \pi$: at $w_0 = 4$, $\phi = 0$, and $\sqrt4\,e^{0} = 2$.
>
> **(b) $z_0 = -2$, $w_0 = 4$.** Take $\pi < \phi < 3\pi$: then $w_0 = 4$ has $\phi = 2\pi$, and $\sqrt4\,e^{i\pi} = -2$. (Equivalently, minus the principal branch.)
>
> **(c) $z_0 = -i$, $w_0 = -1$.** Take $2\pi < \phi < 4\pi$: then $w_0 = -1$ has $\phi = 3\pi$, and $\sqrt1\,e^{i3\pi/2} = -i$.
>
> In each case $g'(w) = \frac12\sqrt\rho^{\,-1}e^{-i\phi/2} = \dfrac{1}{2g(w)} = \dfrac{1}{f'(z)}$, as (1) says.
>
> *B&C: Sec. 114, Exercise 6*

^ex-114-2

> [!example] Example §114.3: No Local Inverse at a Critical Point
> The hypothesis $f'(z_0) \ne 0$ cannot be dropped. For $w = z^2$ at the critical point $z_0 = 0$ ($w_0 = 0$): every neighborhood of $0$ contains $\varepsilon$ and $-\varepsilon$ for small $\varepsilon > 0$, and both are mapped to $\varepsilon^2$. So $f$ is one-to-one on no neighborhood of $0$. Nor is there a local inverse in the sense of Definition §114.1: if $g$ were analytic near $0$ with $g(0) = 0$ and $f[g(w)] = w$, the chain rule at $w = 0$ would give $f'(0)\,g'(0) = 1$, impossible since $f'(0) = 0$. The real Jacobian is $J = |f'(0)|^2 = 0$, so the inverse function theorem does not apply. Geometrically, a neighborhood of $0$ is wrapped twice around a neighborhood of $0$, with angles doubled ([[§112★ Preservation of Angles and Scale Factors#^ex-112-4|Example §112.4]]).
>
> *B&C: Sec. 114 (text, the hypothesis f′(z₀) ≠ 0); the example is added*

^ex-114-3
