---
type: section
subject: "[[Multivariable Analysis]]"
chapter: 7
section: 36
tags: [multivariable-analysis, math452]
---
← [[§35 The Unit Sphere and Spherical Coordinates]] · ↑ [[· 7 Differential Forms and the Generalized Stokes' Theorem]] · [[§37 The Algebra of Differential Forms]] →

## Part III: Differential Forms

Chapter 7: [[· 7 Differential Forms and the Generalized Stokes' Theorem|Differential Forms and the Generalized Stokes' Theorem]].

## Motivation: What Are We Integrating?

All semester we have been computing integrals: $\int_a^b f\,dx$, $\int_\gamma \mathbf{F}\cdot d\mathbf{r}$, $\iint_D f\,dx\,dy$, $\iint_S \mathbf{F}\cdot d\mathbf{S}$, $\iiint_V f\,dV$. Each time, we had to choose a parametrization, compute Jacobians or cross products, keep track of signs, and verify the answer was independent of the parametrization. And we proved three “integral = boundary integral” theorems ([[Green's Theorem|Green's]], [[Divergence Theorem in ℝ³|Divergence]], [[Stokes' Theorem in ℝ³|Stokes']]) with three separate proofs, even though they all say the same thing.

Differential forms answer one question: **what is the object we are actually integrating, before we choose a parametrization?**

Look at all the integrals we have been writing:

| **Integral** | **Integrand** | **Domain** |
|---|---|---|
| *Over curves:* | | |
| $\int_a^b f(x) \, dx$ | $f \, dx$ | interval |
| $\int_\gamma P \, dx + Q \, dy + R\,dz$ | $P \, dx + Q \, dy + R\,dz$ | curve |
| $\int_\gamma f \, ds$ | $f \, ds = f\,\vert\boldsymbol{\gamma}'\vert\,dt$ | curve |
| *Over surfaces and flat regions:* | | |
| $\iint_D f \, dx \, dy$ | $f \, dx \, dy$ | 2D region |
| $\iint_S P \, dy \, dz + Q \, dz \, dx + R \, dx \, dy$ | $P \, dy\, dz + Q \, dz \, dx + R \, dx \, dy$ | surface |
| $\iint_S f \, dS$ | $f\,dS = f\,\vert\mathbf{X}_u \times \mathbf{X}_v\vert\,du\,dv$ | surface |
| *Over volumes:* | | |
| $\iiint_V f \, dx \, dy \, dz$ | $f \, dx \, dy \, dz$ | 3D region |

Some of these integrands — $P\,dx + Q\,dy$, $f\,dx\,dy$, $P\,dy\,dz + Q\,dz\,dx + R\,dx\,dy$ — are expressions involving $dx$, $dy$, $dz$ in various combinations. Others — $f\,ds$, $f\,dS$ — involve absolute values ($|\boldsymbol{\gamma}'|$, $|\mathbf{X}_u \times \mathbf{X}_v|$). We have been treating these symbols as shorthand. Differential forms take the first kind seriously as **algebraic objects** that can be added, multiplied, and differentiated. The second kind (with absolute values) are fundamentally different, and understanding why is the starting point.

## Signed, Unsigned, and Signed in Disguise

Not all integrals behave the same way under orientation reversal. We have encountered three fundamentally different kinds:

**Category 1: Genuinely signed.** The integral $\int_a^b f(x)\,dx$ satisfies $\int_a^b = -\int_b^a$ ([[§34 Fundamental Theorem of Calculus#^rem-34-1|451 orientation convention]]): it flips sign when you reverse direction. The $dx$ carries orientation. Similarly, $\int_\gamma \mathbf{F} \cdot d\mathbf{r}$ flips when you reverse $\gamma$, and $\iint_S \mathbf{F} \cdot d\mathbf{S}$ flips when you reverse the normal. These will turn out to be *differential form integrals*.

**Category 2: Genuinely unsigned.** The scalar line integral $\int_\gamma f\,ds$ ([[§27 Line Integrals and Green's Theorem#^def-27-1|Def. §27.1]]) does *not* change sign when you reverse $\gamma$, because $ds = |\boldsymbol{\gamma}'(t)|\,dt > 0$ always. Similarly, $\iint_S f\,dS$ ([[§31 Surface Integrals#^def-31-5|Def. §31.5]]) uses $dS = |\mathbf{X}_u \times \mathbf{X}_v|\,du\,dv > 0$. These have absolute values built into their definitions — no reinterpretation can make them signed. They compute physical quantities (mass, arc length, surface area) and do not appear in any integral theorem. These are *not* differential forms.

**Category 3: Signed in disguise.** The double integral $\iint_D f\,dx\,dy$ is formally a 2-form integral ($dx\,dy$ is $dx \wedge dy$). But in this course, we treat $D$ as an unoriented set and use $|J|$ in the change of variables ([[Change of Variables Formula (multiple integrals)|Theorem §25.3]]), discarding the sign of the Jacobian. If we parametrize $D$ by an orientation-*reversing* map $\Phi$ (one with $J < 0$), the $|J|$ formula doesn't notice — it gives the same positive answer. A true form integral would use the signed $J$ and produce a negative value, reflecting the reversed orientation. The volume integral $\iiint_V f\,dx\,dy\,dz$ is the same: formally a 3-form, but the course always uses $|J|$.

(A warning on notation: swapping $dx\,dy$ to $dy\,dx$ in a Riemann double integral means changing the *order of iterated integration*, which by [[§23 Fubini's Theorem#^cor-23-4|Fubini]] gives the same answer. This is *not* the same as $dx \wedge dy = -dy \wedge dx$, which is about the *orientation of the basis vectors* spanning the area element. The wedge product anti-commutativity is an algebraic property of forms, not a statement about Fubini's theorem.)

However, there *is* a 2D operation that genuinely reverses orientation: **reversing the bounds** of an iterated integral. In 1D, $\int_0^1 f\,dx = -\int_1^0 f\,dx$. In 2D, reversing the inner bounds does the same thing:

$$
\int_0^1\!\!\int_1^0 f\,dx\,dy = -\int_0^1\!\!\int_0^1 f\,dx\,dy,
$$

because the inner integral picks up a sign from the 1D rule. More generally:

| **Iterated integral** | **Sign** | **Why** |
|---|:-:|---|
| $\int_0^1\!\int_0^1 f\,dx\,dy$ | $+$ | standard orientation |
| $\int_0^1\!\int_1^0 f\,dx\,dy$ | $-$ | $x$-direction reversed |
| $\int_1^0\!\int_0^1 f\,dx\,dy$ | $-$ | $y$-direction reversed |
| $\int_1^0\!\int_1^0 f\,dx\,dy$ | $+$ | both reversed $= 180°$ rotation (preserves orientation) |

Each bound carries a direction of traversal, and reversing one is an orientation-reversing transformation (signed Jacobian $= -1$). Reversing both gives $(-1)(-1) = +1$ — orientation-preserving. This is *not* Fubini: Fubini swaps which variable is integrated first while keeping all bounds in the same direction. Bound reversal changes the *direction* of traversal within one variable.

![[m452-21-3.svg]]
*The four rows of the table as oriented frames on the unit square. Each bound pair sets the direction of traversal of one variable (black arrows start at the lower limit); the arc turns from the first direction ($x$, inner integral) to the second ($y$). Counterclockwise turn: sign $+$ (blue); clockwise: sign $-$ (red). Reversing one direction is a reflection and flips the turn; reversing both is a rotation by $180^\circ$ and restores it.*

The reason we do not see this in 452 is that we write $\iint_D f\,dA$, where $D$ is a *set* with no ordered bounds. The orientation information that iterated integrals with explicit bounds carry is erased. The $|J|$ formula works with unoriented sets, so it never encounters orientation reversal. In the forms language, $\int_0^1\!\int_0^1 f\,dx \wedge dy$ is the integral over the unit square *with the standard orientation*. Writing $\iint_D f\,dA$ strips this.

This creates an inconsistency across dimensions. In 1D, the change of variables uses the **signed** derivative $g'(t)$:

$$
\int_a^b f(x)\,dx = \int_{g^{-1}(a)}^{g^{-1}(b)} f(g(t)) \cdot g'(t)\,dt.
$$

If $g$ is decreasing ($g' < 0$), two things happen: the limits reverse, and $g'$ is negative. The two sign changes cancel. But in 2D/3D, the course uses $|J|$, stripping the sign entirely. The 1D integral keeps its orientation; the 2D/3D integrals discard theirs. Differential forms resolve this by making *all* dimensions consistently signed — but we need to define what a form is before we can see how.

## What Orientation Means

Before proceeding, we should clarify what “orientation of a domain” means, because the intuition is very different depending on the dimension.

For a **curve in $\mathbb{R}^2$ or $\mathbb{R}^3$**, orientation means “which direction are you traversing” — from $a$ to $b$, or from $b$ to $a$. You can see this: draw an arrow on the curve.

For a **surface in $\mathbb{R}^3$**, orientation means “which side is up” — which direction the normal vector $\hat{n}$ points. You can see this too: paint one side red, the other blue.

But for a **volume in $\mathbb{R}^3$**: what would orientation mean? The region fills space — there is no “other side” to point to, no direction to reverse. You cannot paint the inside of a solid ball a different color from… what?

The answer is purely algebraic: the orientation of a 3D region in $\mathbb{R}^3$ is the **choice of coordinate ordering**. The “standard orientation” is $(x, y, z)$ in the right-hand-rule order, corresponding to $dx \wedge dy \wedge dz > 0$. The “opposite orientation” would be the left-hand rule, corresponding to $dx \wedge dy \wedge dz < 0$. But unlike curves and surfaces, there is no geometric way to visualize this — it is a convention, not a visible feature.

In fact, coordinate ordering describes orientation *at every dimension* — it just happens to coincide with the geometric picture when the region is not top-dimensional:

**In 2D:** A flat region $D \subseteq \mathbb{R}^2$ with coordinates $(x,y)$ has $dx \wedge dy > 0$ (standard orientation). Switching to the ordering $(y,x)$ gives $dy \wedge dx = -dx \wedge dy < 0$ (reversed). The map $(x,y) \mapsto (y,x)$ has Jacobian $\det\left(\begin{smallmatrix} 0 & 1 \\ 1 & 0 \end{smallmatrix}\right) = -1$: a reflection, which reverses orientation ([[§37 Determinants#^ladr-9-61|LADR 9.61]]). Now embed $D$ as a surface in $\mathbb{R}^3$ (lying flat in the $xy$-plane). The two orderings correspond to the normal pointing in $+\hat{z}$ or $-\hat{z}$ — flipping the normal. So switching coordinate ordering (the algebraic description) produces the same effect as flipping the surface (the geometric description).

![[m452-21-2.svg]]
*Two descriptions of the same choice. Algebraic: an ordered pair of basis vectors — $(\hat{e}_x, \hat{e}_y)$ on the left, $(\hat{e}_y, \hat{e}_x)$ on the right; the green arc turns from the 1st vector to the 2nd, counterclockwise or clockwise as seen from above. Geometric: the normal $\pm\hat{z}$ (red) given by the right-hand rule from that turn. Swapping the order $\leftrightarrow$ flipping the normal $\leftrightarrow$ negating $dx \wedge dy$.*

**In 1D:** There is only one coordinate $x$ — nothing to swap it with. Instead, orientation is the **choice of direction**: does $x$ increase or decrease as you traverse? Writing $\int_a^b$ means “traverse in the direction of increasing $x$” (standard). Writing $\int_b^a$ means “traverse in the direction of decreasing $x$” (reversed). The sign flip $\int_a^b = -\int_b^a$ is the 1D version of switching the coordinate ordering. There is no second coordinate to swap, so the only freedom is the sign of the single basis vector: $+\hat{e}_x$ or $-\hat{e}_x$.

**The uniform description:** In all dimensions, orientation is determined by the **sign of the permutation** ([[§36 Alternating Multilinear Forms#^ladr-9-32|LADR 9.32]]) of basis vectors. Two ordered bases have the same orientation if and only if the permutation relating them is even (an even number of transpositions); they have opposite orientation if the permutation is odd. This is encoded by the Levi-Civita symbol $\varepsilon_{ij\ldots k}$ ([[§37 The Algebra of Differential Forms#^def-37-2|Def. §37.2]]), which equals $+1$ for even permutations, $-1$ for odd, and $0$ if any index is repeated.

In 1D, the only “permutation” is the sign of the single basis vector: $\{+\hat{e}_x\}$ vs $\{-\hat{e}_x\}$. In 2D, $\{\hat{e}_x, \hat{e}_y\}$ vs $\{\hat{e}_y, \hat{e}_x\}$ is a single transposition (odd, so orientation reverses). In 3D, even permutations of $\{\hat{e}_x, \hat{e}_y, \hat{e}_z\}$ — such as $(y,z,x)$ and $(z,x,y)$ — preserve orientation, while odd ones — such as $(y,x,z)$ — reverse it.

The wedge product $\wedge$ (defined formally in [[§37 The Algebra of Differential Forms#^def-37-1|§37]]; for now, the key property is $dx_i \wedge dx_j = -dx_j \wedge dx_i$, with $dx_i \wedge dx_i = 0$) is the realization of this same structure as an algebraic operation on differentials:

$$
dx_i \wedge dx_j \wedge dx_k = \varepsilon_{ijk}\,dx \wedge dy \wedge dz.
$$

The three defining properties match exactly: swapping two indices negates $\varepsilon_{ijk}$, and swapping two wedge factors negates the product; repeating an index gives $\varepsilon_{iik} = 0$, and $dx_i \wedge dx_i = 0$; the standard ordering gives $\varepsilon_{123} = +1$, and $dx \wedge dy \wedge dz > 0$. The determinant formula $\det(A) = \sum_\sigma \mathrm{sgn}(\sigma)\prod_i A_{i,\sigma(i)}$ ([[§37 Determinants#^ladr-9-46|LADR 9.46]]) is what you get when you expand the wedge product evaluated on a set of vectors — the wedge product computes determinants by tracking permutation signs automatically.

So the cross product, the determinant, the Jacobian, and the wedge product are all manifestations of the same algebraic structure: **alternating multilinear maps** ([[§36 Alternating Multilinear Forms#^ladr-9-27|LADR 9.27]]). The Levi-Civita symbol is the coordinate version; the wedge product is the coordinate-free version that works in any dimension and on any manifold. The geometric intuition (direction of traversal, normal vector) is available only when the region is embedded in a higher-dimensional space.

The pattern is: a $k$-dimensional region in $\mathbb{R}^n$ with $n > k$ has a **normal direction** in the ambient space, so orientation is geometric and visible. A $k$-dimensional region in $\mathbb{R}^k$ (top-dimensional) has no ambient space to point into, so orientation is purely algebraic.

| **Region** | **Top-dim?** | **Orientation means…** | **Visible?** |
|---|:-:|---|:-:|
| Curve in $\mathbb{R}^2$ or $\mathbb{R}^3$ | no | direction of traversal | yes |
| Surface in $\mathbb{R}^2$ | yes | $(x,y)$ vs $(y,x)$ ordering | no |
| Surface in $\mathbb{R}^3$ | no | normal points up or down | yes |
| Volume in $\mathbb{R}^3$ | yes | $(x,y,z)$ vs $(y,x,z)$ ordering | no |
| Volume in $\mathbb{R}^4$ | no | normal points in $+w$ or $-w$ | yes |

This is why surface orientation in $\mathbb{R}^3$ feels natural (you can point to the normal) but volume orientation in $\mathbb{R}^3$ feels abstract (there is no 4th dimension to point into). If you *did* embed $\mathbb{R}^3$ into $\mathbb{R}^4$, a 3D region would suddenly have a normal direction ($\pm\hat{e}_w$), and the two orientations would become “which side of the 3D hypersurface are you on” — exactly like the two sides of a surface in $\mathbb{R}^3$.

This also explains why the [[Divergence Theorem in ℝ³|Divergence Theorem]] needs the *boundary surface* to be oriented (the normal is visible — outward vs inward) but does not need the *volume itself* to be oriented (it is top-dimensional, so the standard orientation of $\mathbb{R}^3$ is automatic). And it is why $|J|$ suffices for volume integrals in this course: since everyone agrees on the standard coordinate ordering, the signed and unsigned versions always agree, and orientation is invisible.

## What a Differential Form Is

> [!definition] Definition §36.1: Coordinate 1-Forms
> Let $x_1, \ldots, x_n$ be the standard coordinates on $\mathbb{R}^n$. The **coordinate 1-forms** $dx_1, \ldots, dx_n$ are defined by:
>
> $$
> dx_i(\mathbf{v}) = v_i \qquad \text{(the $i$-th component of $\mathbf{v}$)}.
> $$

^def-36-1

> [!remark]- Connections
> - The coordinate 1-forms $dx_1, \ldots, dx_n$ are the dual basis of the standard basis: [[§12 Duality#^ladr-3-113|LADR 3.113]].
> - On a manifold the coordinate 1-forms at a point are the dual basis of the coordinate derivations, [[§32 The Cotangent Space#^lem-32-2|591 Lemma §32.2]], and the covectors at all points together form the cotangent bundle, [[§46 The Cotangent Bundle#^def-46-1|591 Def. §46.1]].

> [!definition] Definition §36.2: Differential Form
> A **$k$-form** on an open subset $U \subseteq \mathbb{R}^n$ is an expression:
>
> $$
> \omega = \sum_{i_1 < i_2 < \cdots < i_k} f_{i_1 \cdots i_k}(x_1, \ldots, x_n) \; dx_{i_1} \wedge dx_{i_2} \wedge \cdots \wedge dx_{i_k},
> $$
>
> where each $f_{i_1 \cdots i_k}: U \to \mathbb{R}$ is a smooth coefficient function, and the sum runs over all $\binom{n}{k}$ strictly increasing index sequences.
>
> The special cases are:
> - A **0-form** is a smooth function $f: U \to \mathbb{R}$.
> - In $\mathbb{R}^3$: a **1-form** is $f_1\,dx + f_2\,dy + f_3\,dz$ (3 coefficients); a **2-form** is $f_{23}\,dy \wedge dz + f_{31}\,dz \wedge dx + f_{12}\,dx \wedge dy$ (3 coefficients); a **3-form** is $f_{123}\,dx \wedge dy \wedge dz$ (1 coefficient).

^def-36-2

> [!remark]- Connections
> - At each point a $k$-form is an alternating $k$-linear form on $\mathbb{R}^n$ ([[§36 Alternating Multilinear Forms#^ladr-9-27|LADR 9.27]]); there are none for $k > n$ ([[§36 Alternating Multilinear Forms#^ladr-9-29|LADR 9.29]]) and the top-degree ones form a 1-dimensional space ([[§36 Alternating Multilinear Forms#^ladr-9-37|LADR 9.37]]).

**What this definition says, concretely:**

A $k$-form is a machine: at each point, you feed it $k$ tangent vectors and it outputs a number.

**0-form** (one coefficient). A smooth function $f(x,y,z)$. It eats zero tangent vectors — it just outputs a number at each point. “Integrating” a 0-form means evaluating it: $\int_{\{p\}} f = f(p)$.

A 0-form needs only one coefficient because there is no direction to choose.

**1-form** (three coefficients in $\mathbb{R}^3$). At each point, it eats one tangent vector $\mathbf{v}$ and outputs a number. To do this, it needs to assign a weight to each independent direction: “if you move in $dx$, the weight is $f_1$; in $dy$, it is $f_2$; in $dz$, it is $f_3$.” So a 1-form in $\mathbb{R}^3$ has $\binom{3}{1} = 3$ coefficient functions:

$$
\omega = f_1\,dx + f_2\,dy + f_3\,dz.
$$

The coefficients $f_1, f_2, f_3$ are smooth functions of $(x,y,z)$ — they vary from point to point. They are **coordinate-dependent**: in $(x,y,z)$ coordinates, $f_1(p) = \omega_p(\hat{e}_x)$ is “what the form outputs when fed the unit vector in the $x$-direction.” In spherical coordinates, the same form $\omega$ would have different coefficient functions, because the basis vectors $\hat{e}_r, \hat{e}_\theta, \hat{e}_\phi$ are different from $\hat{e}_x, \hat{e}_y, \hat{e}_z$. The form itself is coordinate-independent; the coefficients describe it in a particular coordinate system — just as a vector field $\mathbf{F}$ has different components in Cartesian vs. spherical, but points in the same direction.

When you feed $\omega$ a tangent vector $\mathbf{v} = (v_1, v_2, v_3)$, the output is $f_1 v_1 + f_2 v_2 + f_3 v_3$. To integrate $\omega$ over a curve $\gamma$, you feed it the tangent vector $\gamma'(t)\,dt$ at each point and sum:

$$
\int_\gamma \omega = \int_a^b (f_1\, x' + f_2\, y' + f_3\, z')\,dt.
$$

(In [[§27 Line Integrals and Green's Theorem|§27]]–[[§34 Stokes' Theorem in ℝ³|§34]], we wrote $P, Q, R$ for $f_1, f_2, f_3$.)

The simplest 1-form is $df = f_x\,dx + f_y\,dy + f_z\,dz$, where the coefficients come from a single function $f$. But not every 1-form arises this way: $\omega = y\,dx + x^2\,dy$ has no single antiderivative $f$ with $f_x = y$ and $f_y = x^2$ (since $f_{xy} = 1 \neq 2x = f_{yx}$). Such a form is called *not exact* ([[§39 Closed and Exact Forms#^def-39-3|Def. §39.3]]).

This $df$ is the same object as the differential from [[§10 The Differential#^def-10-1|§10]] — same formula, same notation. In §10, we introduced $df = f_x\,dx + f_y\,dy + f_z\,dz$ as the “best linear approximation”: $\Delta f \approx f_x\,\Delta x + f_y\,\Delta y + f_z\,\Delta z$ for small changes. But we never said precisely what $dx$, $dy$, $dz$ *are*. Now we can: $dx$ is the 1-form that eats a tangent vector $\mathbf{v} = (v_1, v_2, v_3)$ and outputs $v_1$ (the $x$-component). So $df$ eats $\mathbf{v}$ and outputs $f_x v_1 + f_y v_2 + f_z v_3 = \nabla f \cdot \mathbf{v}$, the [[Directional Derivative Formula|directional derivative]] of $f$ in direction $\mathbf{v}$. The “best linear approximation” and the “1-form that outputs directional derivatives” are the same thing — and this is where the name “differential forms” comes from: $df$ is the prototypical example, and all forms generalize it.

**2-form** (three coefficients in $\mathbb{R}^3$). At each point, it eats two tangent vectors (spanning a parallelogram) and outputs a signed area, weighted differently for each independent plane. In $\mathbb{R}^3$ there are $\binom{3}{2} = 3$ independent coordinate planes ($yz$, $zx$, $xy$), so a 2-form needs three coefficient functions:

$$
\eta = f_{23}\,dy \wedge dz + f_{31}\,dz \wedge dx + f_{12}\,dx \wedge dy.
$$

(In §31, the flux of a vector field $\mathbf{u} = (a, b, c)$ is the integral of this 2-form with $(f_{23}, f_{31}, f_{12}) = (a, b, c)$. The subscript notation makes the structure explicit: the subscripts name which basis element the coefficient multiplies.)

To integrate $\eta$ over a surface $S$ parametrized by $\mathbf{X}(u,v)$: at each point of $S$, the parametrization provides two tangent vectors $\mathbf{X}_u$ and $\mathbf{X}_v$ (from [[§31 Surface Integrals#^def-31-2|§31]]). These span a small parallelogram — the infinitesimal surface element. The 2-form eats this pair of vectors and outputs a number (the signed area, weighted by the coefficients at that point). Summing over all such parallelograms:

$$
\iint_S \eta = \iint_D \big[ f_{23}(y_u z_v - z_u y_v) + f_{31}(z_u x_v - x_u z_v) + f_{12}(x_u y_v - y_u x_v) \big] \, du \, dv.
$$

The three parenthesized terms are the components of $\mathbf{X}_u \times \mathbf{X}_v$, so this is $\iint_D (f_{23}, f_{31}, f_{12}) \cdot (\mathbf{X}_u \times \mathbf{X}_v) \, du\,dv$ — the flux integral from [[§32 Flux Integrals and the Divergence Theorem in ℝ³#^def-32-1|§32]].

**3-form** (one coefficient in $\mathbb{R}^3$). At each point, it eats three tangent vectors (spanning a parallelepiped) and outputs signed volume times a coefficient. There is only $\binom{3}{3} = 1$ way to choose 3 differentials from $\{dx, dy, dz\}$: you must take all three. Any other combination either repeats a differential ($dx \wedge dx \wedge dy = 0$) or is a permutation of $dx \wedge dy \wedge dz$ (giving $\pm dx \wedge dy \wedge dz$). So a 3-form has just one coefficient:

$$
\mu = f_{123}\,dx \wedge dy \wedge dz.
$$

To integrate: if $V$ is described directly in $(x,y,z)$ coordinates, $\iiint_V \mu = \iiint_V f_{123}\,dx\,dy\,dz$. (In $\mathbb{R}^4$, a 3-form would have $\binom{4}{3} = 4$ terms.)

**The count of coefficients** follows Pascal's triangle: $\binom{3}{0} = 1$, $\binom{3}{1} = 3$, $\binom{3}{2} = 3$, $\binom{3}{3} = 1$. It rises then falls because choosing which 2 of 3 directions to include is the same as choosing which 1 to exclude.

## Forms and Riemann Integration

Looking at the integration formulas above, you may notice: the right-hand side of every formula is an ordinary Riemann integral over a parameter domain. For instance:

$$
\int_\gamma \omega = \int_a^b (\underbrace{f_1\, x' + f_2\, y' + f_3\, z'}_{\text{a function of } t})\,dt, \qquad \iint_S \eta = \iint_D (\underbrace{(f_{23}, f_{31}, f_{12}) \cdot (\mathbf{X}_u \times \mathbf{X}_v)}_{\text{a function of } (u,v)})\,du\,dv.
$$

So what did the form actually *do*? It produced the correct integrand. The form $\omega = f_1\,dx + f_2\,dy + f_3\,dz$, combined with the parametrization $\gamma(t)$, automatically generated the function $f_1 x' + f_2 y' + f_3 z'$ that goes inside the Riemann integral. Without forms, you derive this by hand ([[Multivariable Chain Rule|chain rule]], cross products, Jacobians). With forms, the [[§37 The Algebra of Differential Forms#^def-37-3|pullback]] machinery does it for you.

The two layers do different jobs:
- **Forms** (this section) determine *what* to integrate: the correct integrand on the parameter domain, with all Jacobians and signs.
- **Riemann integration** ([[§21 The Definition of the Integral#^def-21-7|§21.7]]) determines the *number*: Riemann sums, Fubini, etc.

Forms do not replace Riemann integration. They sit on top of it. On flat domains in Cartesian coordinates, you can skip the forms layer entirely — the Riemann integral works directly. This is what we did for 90% of the course. The forms layer becomes essential when the domain is curved (curves, surfaces), the coordinates are non-Cartesian (polar, spherical), or you want to understand why three integral theorems are really one theorem.

**The 1D inconsistency resolved.**

We can now return to the inconsistency from the three categories above. In the forms framework, the change of variables in *every* dimension uses the signed Jacobian:

$$
\iint_D f\,dx \wedge dy = \iint_{D^*} f(\Phi) \cdot J\,du \wedge dv.
$$

Consider two parametrizations of the same region $D$: one with $\Phi(u,v)$ (where $J > 0$), and another $\tilde{\Phi}(u,v) = \Phi(v,u)$ that swaps the parameter roles (so $\tilde{J} = -J < 0$). These describe the same geometric region, but with opposite orientations. The forms formula gives:

$$
\iint_{D^*} f(\Phi) \cdot J\,du\,dv \quad \text{vs.} \quad \iint_{D^*} f(\tilde{\Phi}) \cdot (-J)\,du\,dv.
$$

The sign flip in the Jacobian reflects the orientation reversal — exactly as in 1D, where going from $a$ to $b$ vs. $b$ to $a$ produces opposite signs. The $|J|$ approach from [[Change of Variables Formula (multiple integrals)|§15]] gives $|J| = |-J|$, so both parametrizations yield the same positive number. This is correct for computing areas, but it means the integral cannot distinguish the two orientations — which is exactly the information the integral theorems need.

> [!remark] Remark: Riemann vs. Lebesgue
> The two-layer picture above shows that the forms layer (pullback, wedge products, Jacobians) is purely algebraic — it does not depend on which integration theory computes the number in step 2. Everything in these notes uses the Riemann integral, but the forms framework works identically with the Lebesgue integral of [[§22 The General Lebesgue Integral|551 §22]]. For continuous functions on compact domains, the two integrals agree (in one variable, every Riemann integrable function is Lebesgue integrable with the same integral, [[§23 The Dominated Convergence Theorem#^thm-23-5|551 Thm. §23.5]]), so every computation here gives the same answer either way. The Lebesgue integral becomes necessary when pushing beyond 452: forms with $L^p$ coefficients (not just smooth), limit theorems (DCT/MCT for swapping $\lim$ and $\int$), and Hodge theory (minimizing $L^2$ norms over spaces of forms). The forms framework is the same; the integration backend determines how far you can push it.

^rem-36-1

## Why the Algebra Must Be Anti-Commutative

We have said that a $k$-form “waits for a parametrization” to become a number. But what algebra governs the combination of differentials? The answer is not imposed by convention — it is *forced* by the requirement that coordinate substitution reproduces the Jacobian determinant.

### Discovering the Rules from a Computation

Consider a surface $\mathbf{X}(u,v) = (x(u,v), y(u,v))$ in $\mathbb{R}^2$. We want to express the area element $dx\,dy$ in terms of $du\,dv$.

**Step 1.** The chain rule gives:

$$
dx = x_u\,du + x_v\,dv, \qquad dy = y_u\,du + y_v\,dv.
$$

**Step 2.** Combine these into an area element. Expand formally, treating the product of differentials as an unknown operation:

$$
(x_u\,du + x_v\,dv)(y_u\,du + y_v\,dv) = x_u y_u\,du\,du + x_u y_v\,du\,dv + x_v y_u\,dv\,du + x_v y_v\,dv\,dv.
$$

**Step 3.** We know from [[§24 The Change of Variables Formula#^rem-24-14|§24]] that the correct answer is the *signed* Jacobian determinant:

$$
(x_u y_v - x_v y_u)\,du\,dv = \det \begin{pmatrix} x_u & x_v \\ y_u & y_v \end{pmatrix} du\,dv.
$$

For the expansion in Step 2 to equal this, we *need*:

$$
du\,du = 0, \qquad dv\,dv = 0, \qquad dv\,du = -du\,dv.
$$

These are not arbitrary conventions — they are forced by the determinant:
- $du\,du = 0$: If we tried to compute $dx \wedge dx$ by the same method, we would get $\det\begin{pmatrix} x_u & x_u \\ x_v & x_v \end{pmatrix} = 0$ — a determinant with two identical columns is always zero ([[§37 Determinants#^ladr-9-45|LADR 9.45]]). So the “product of $dx$ with itself” must vanish.
- $dv\,du = -du\,dv$: Swapping the two columns of a $2 \times 2$ determinant negates it ([[§36 Alternating Multilinear Forms#^ladr-9-30|LADR 9.30]]): $\det\begin{pmatrix} x_u & x_v \\ y_u & y_v \end{pmatrix} = -\det\begin{pmatrix} x_v & x_u \\ y_v & y_u \end{pmatrix}$. Swapping $u \leftrightarrow v$ in the parametrization reverses the orientation, so the product of differentials must be anti-commutative.

**Step 4.** These are exactly the rules of the wedge product: $du \wedge du = 0$, $dv \wedge dv = 0$, and $dv \wedge du = -du \wedge dv$. The anti-commutativity is not an abstract axiom — it is the *unique* multiplication rule on differentials that makes coordinate substitution produce the Jacobian determinant.

![[m452-21-1.svg]]
*Each 2-form pullback is a signed projected area: $dx \wedge dy$ measures the shadow of the tangent parallelogram on the $xy$-plane, with sign given by orientation. The three shadows (on the $yz$-, $zx$-, $xy$-planes) are the three components of $\mathbf{X}_u \times \mathbf{X}_v$; the Gram determinant $\det(G)$ is the sum of their squares.*

The computation above is informal: we have not yet defined the wedge product. In [[§37 The Algebra of Differential Forms#^def-37-1|Def. §37.1]], we axiomatize these rules, and then the computation becomes a formal proposition (the *[[§37 The Algebra of Differential Forms#^def-37-3|pullback formula]]*) that underlies all integration of forms.
