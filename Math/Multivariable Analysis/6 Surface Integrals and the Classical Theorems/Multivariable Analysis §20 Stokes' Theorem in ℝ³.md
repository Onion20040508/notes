---
type: section
subject: "[[Multivariable Analysis]]"
chapter: 6
section: 20
tags: [multivariable-analysis, math452]
---
← [[Multivariable Analysis §19 The Laplacian in Spherical Coordinates]] · ↑ [[Multivariable Analysis — 6 Surface Integrals and the Classical Theorems]] · [[Multivariable Analysis §21 Introduction to Differential Forms]] →

Green's theorem ([[Multivariable Analysis §16 Line Integrals and Green's Theorem#^thm-16-1|Section 16]]) relates a line integral around a closed curve $\gamma$ to a double integral over the enclosed *flat* region $D \subseteq \mathbb{R}^2$. Stokes' theorem generalizes this: it relates a line integral around the boundary $\partial S$ of a *curved* surface $S \subseteq \mathbb{R}^3$ to a surface integral over $S$.

## Statement

> [!theorem] Theorem §20.1: Stokes' Theorem
> Let $S \subseteq \mathbb{R}^3$ be an oriented, piecewise smooth surface with piecewise smooth boundary curve $\partial S$. Orient $\partial S$ by the right-hand rule: if $\hat{n}$ is the chosen normal to $S$ and you walk along $\partial S$ with $\hat{n}$ pointing from your feet to your head, the surface is on your left.
>
> If $\mathbf{F} = (P, Q, R)$ is $C^1$ on an open set containing $S$, then:
>
> $$
> \boxed{\oint_{\partial S} \mathbf{F} \cdot d\mathbf{r} = \iint_S (\nabla \times \mathbf{F}) \cdot d\mathbf{S}}
> $$
>
> where $\nabla \times \mathbf{F} = \left(\frac{\partial R}{\partial y} - \frac{\partial Q}{\partial z}, \;\; \frac{\partial P}{\partial z} - \frac{\partial R}{\partial x}, \;\; \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}\right)$ ([[Multivariable Analysis §16 Line Integrals and Green's Theorem#^def-16-5|Def. §16.5]]) and $d\mathbf{S} = (\mathbf{X}_u \times \mathbf{X}_v) \, du \, dv$ ([[Multivariable Analysis §18 Surface Integrals#^def-18-6|Def. §18.6]]).

^thm-20-1

> [!remark]- Connections
> - The flat case is [[Multivariable Analysis §16 Line Integrals and Green's Theorem#^thm-16-3|Green's Theorem as 2D Stokes' Theorem]]; the proof below reduces to [[Multivariable Analysis §16 Line Integrals and Green's Theorem#^thm-16-1|Green's Theorem]] on the parameter domain.
> - In forms language: $d$ on 1-forms gives the curl ([[Multivariable Analysis §22 The Algebra of Differential Forms#^prop-22-3|Prop. §22.3]]), and the theorem is a case of the [[Multivariable Analysis §23 The Generalized Stokes' Theorem#^thm-23-1|Generalized Stokes' Theorem]].

> [!remark] Remark: Orientation Convention
> The boundary orientation is determined by the surface orientation:
> - If $\hat{n}$ points “upward,” then $\partial S$ is traversed counterclockwise when viewed from above.
> - If $\hat{n}$ is reversed, $\partial S$ reverses direction.
>
> This is the same right-hand rule as in electromagnetism: curl your right hand's fingers in the direction of $\partial S$, and your thumb points in the direction of $\hat{n}$.

^rem-20-1

![[m452-20-1.svg]]
*Stokes' theorem, both sides at once. Green: the field's circulation around the rim, $\oint_{\partial S}\mathbf{F}\cdot d\mathbf{r}$. Red: the curl of $\mathbf{F}$ distributed over the cap, each vector measuring the microscopic circulation of a tiny loop (drawn) in the tangent plane; its flux through the surface is $\iint_S (\nabla\times\mathbf{F})\cdot d\mathbf{S}$. The theorem is the cancellation argument of [[Multivariable Analysis §16 Line Integrals and Green's Theorem|§16]] made global: tile the cap with tiny loops, and every interior edge is traversed twice in opposite directions — all microscopic circulations telescope into the single circulation around the rim.*

## Proof for Graph Surfaces

We first prove Stokes' theorem for the special case where $S$ is the graph of a function $z = h(x,y)$ over a domain $D \subseteq \mathbb{R}^2$. This is not the full theorem (it only handles surfaces that project injectively onto the $xy$-plane), but it makes the geometric idea transparent: the boundary curve $\Gamma$ on $S$ projects down to a curve $\gamma$ in the $xy$-plane, and the line integral on $\Gamma$ can be computed by working entirely in $D$.

**Setup.** Let $S = \{(x, y, h(x,y)) : (x,y) \in D\}$ with $h \in C^2$, and let $\mathbf{F} = (P, Q, R)$ be $C^1$. The boundary curve $\Gamma = \partial S$ sits above $\gamma = \partial D$: if $\gamma$ is parametrized by $(x(t), y(t))$ for $t \in [a, b]$, then $\Gamma$ is parametrized by:

$$
\Gamma^*(t) = \big(x(t), \, y(t), \, h(x(t), y(t))\big).
$$

**Step 1: Pull back the line integral to $\gamma$.**

The velocity of $\Gamma^*$ is:

$$
\frac{d\Gamma^*}{dt} = (x', \, y', \, h_x x' + h_y y')
$$

by the [[Multivariable Analysis §10 Composition of Functions and the Chain Rule#^thm-10-2|chain rule]] (the third component uses $\frac{d}{dt}h(x(t), y(t)) = h_x x' + h_y y'$).

Now recall from [[Multivariable Analysis §16 Line Integrals and Green's Theorem#^def-16-2|Section 16]] the definition of the line integral: if a curve is parametrized by $\mathbf{r}(t)$, then $d\mathbf{r} = \mathbf{r}\,'(t) \, dt$, so

$$
\oint_\Gamma \mathbf{F} \cdot d\mathbf{r} = \int_a^b \mathbf{F}(\Gamma^*(t)) \cdot \frac{d\Gamma^*}{dt} \, dt.
$$

That is, the notation $\mathbf{F} \cdot d\mathbf{r}$ means: evaluate $\mathbf{F}$ at the point on the curve, dot with the velocity, and integrate over the parameter. Substituting $\mathbf{F} = (P, Q, R)$ and $\frac{d\Gamma^*}{dt} = (x', y', h_x x' + h_y y')$:

$$
\begin{aligned}
\oint_\Gamma \mathbf{F} \cdot d\mathbf{r} &= \int_a^b \big[ P \, x' + Q \, y' + R(h_x x' + h_y y') \big] \, dt \\
&= \int_a^b \big[ (P + Rh_x) x' + (Q + Rh_y) y' \big] \, dt \\
&= \oint_\gamma (P + Rh_x) \, dx + (Q + Rh_y) \, dy.
\end{aligned}
$$

The 3D line integral on $\Gamma$ has been reduced to a 2D line integral on $\gamma$, with modified integrands $\tilde{P} = P + Rh_x$ and $\tilde{Q} = Q + Rh_y$.

**Step 2: Apply Green's theorem on $D$.**

By [[Multivariable Analysis §16 Line Integrals and Green's Theorem#^thm-16-1|Green's theorem]]:

$$
\oint_\gamma \tilde{P} \, dx + \tilde{Q} \, dy = \iint_D \left(\frac{\partial \tilde{Q}}{\partial x} - \frac{\partial \tilde{P}}{\partial y}\right) dx \, dy.
$$

**Step 3: Compute $\tilde{Q}_x - \tilde{P}_y$.**

Using the [[Multivariable Analysis §6 Differentiability#^thm-6-4|product]] and [[Multivariable Analysis §10 Composition of Functions and the Chain Rule#^thm-10-2|chain]] rules (noting that $P, Q, R$ are evaluated at $(x, y, h(x,y))$, so e.g. $\frac{\partial P}{\partial x} = P_x + P_z h_x$):

$$
\begin{aligned}
\frac{\partial \tilde{Q}}{\partial x} &= \frac{\partial}{\partial x}(Q + Rh_y) = (Q_x + Q_z h_x) + (R_x + R_z h_x)h_y + R h_{yx}, \\
\frac{\partial \tilde{P}}{\partial y} &= \frac{\partial}{\partial y}(P + Rh_x) = (P_y + P_z h_y) + (R_y + R_z h_y)h_x + R h_{xy}.
\end{aligned}
$$

Subtracting: the $Rh_{xy}$ and $Rh_{yx}$ terms cancel (equality of mixed partials: $h_{xy} = h_{yx}$, hence $C^2$; [[Multivariable Analysis §5 Equality of Mixed Partials#^thm-5-1|Theorem §5.1]]). The $R_z h_x h_y$ terms also cancel. What remains:

$$
\begin{aligned}
\tilde{Q}_x - \tilde{P}_y &= (Q_x - P_y) + (Q_z h_x - P_z h_y) + (R_x h_y - R_y h_x).
\end{aligned}
$$

**Step 4: Recognize the result as $(\nabla \times \mathbf{F}) \cdot (\mathbf{X}_x \times \mathbf{X}_y)$.**

For the graph parametrization $\mathbf{X}(x,y) = (x, y, h(x,y))$, we computed in [[Multivariable Analysis §18 Surface Integrals#Graph Surfaces|Section 18]] that $\mathbf{X}_x \times \mathbf{X}_y = (-h_x, -h_y, 1)$. Now:

$$
\begin{aligned}
(\nabla \times \mathbf{F}) \cdot (-h_x, -h_y, 1) &= (R_y - Q_z)(-h_x) + (P_z - R_x)(-h_y) + (Q_x - P_y)(1) \\
&= (Q_x - P_y) + (Q_z h_x - P_z h_y) + (R_x h_y - R_y h_x) \\
&= \tilde{Q}_x - \tilde{P}_y.
\end{aligned}
$$

Therefore:

$$
\oint_\Gamma \mathbf{F} \cdot d\mathbf{r} = \iint_D (\tilde{Q}_x - \tilde{P}_y) \, dx \, dy = \iint_D (\nabla \times \mathbf{F}) \cdot (\mathbf{X}_x \times \mathbf{X}_y) \, dx \, dy = \iint_S (\nabla \times \mathbf{F}) \cdot d\mathbf{S}. \qquad \square
$$

*Uses:* [[Multivariable Analysis §10 Composition of Functions and the Chain Rule#^thm-10-2|§10.2]], [[Multivariable Analysis §16 Line Integrals and Green's Theorem#^def-16-2|Def. §16.2]], [[Multivariable Analysis §16 Line Integrals and Green's Theorem#^thm-16-1|§16.1]], [[Multivariable Analysis §6 Differentiability#^thm-6-4|§6.4]], [[Multivariable Analysis §5 Equality of Mixed Partials#^thm-5-1|§5.1]], [[Multivariable Analysis §16 Line Integrals and Green's Theorem#^def-16-5|Def. §16.5]], [[Multivariable Analysis §18 Surface Integrals#^def-18-6|Def. §18.6]]

> [!remark] Remark: Limitations and the General Case
> This proof works only for surfaces that are graphs over a domain in the $xy$-plane. For a general surface (e.g., a hemisphere, where the normal is not everywhere “upward”), we would need to decompose into graph patches and sum — just as the Divergence Theorem proof required decomposition into simple solid regions ([[Multivariable Analysis §18 Surface Integrals#^rem-18-8|Remark in §18]]).
>
> The general proof below avoids this decomposition entirely: by working with an abstract parametrization $(u,v)$ instead of $(x,y)$, the pullback to the parameter domain reduces *every* surface to a flat region, where Green's theorem applies directly.

^rem-20-2

## Proof for General Parametrized Surfaces

The strategy: parametrize $S$ by $\mathbf{X}: D \to \mathbb{R}^3$, pull both sides back to the flat parameter domain $D$, and show they are equal by Green's theorem on $D$.

**Step 1: Set up the parametrization.**

Let $\mathbf{X}: \overline{D} \to \mathbb{R}^3$ be a $C^2$ parametrization of $S$ ([[Multivariable Analysis §18 Surface Integrals#^def-18-1|Def. §18.1]]), where $D \subseteq \mathbb{R}^2$ is a bounded domain with piecewise smooth boundary $\partial D$.

The parametrization maps:
- the interior of $D$ onto $S$,
- the boundary $\partial D$ onto $\partial S$.

Write $\mathbf{X}(u,v) = (x(u,v), \, y(u,v), \, z(u,v))$.

**Step 2: Pull back the right side (surface integral).**

The surface integral is:

$$
\iint_S (\nabla \times \mathbf{F}) \cdot d\mathbf{S} = \iint_D (\nabla \times \mathbf{F})\big|_{\mathbf{X}(u,v)} \cdot (\mathbf{X}_u \times \mathbf{X}_v) \, du \, dv.
$$

Write $\nabla \times \mathbf{F} = (\alpha_1, \alpha_2, \alpha_3)$ where:

$$
\alpha_1 = R_y - Q_z, \qquad \alpha_2 = P_z - R_x, \qquad \alpha_3 = Q_x - P_y.
$$

Then:

$$
\begin{aligned}
(\nabla \times \mathbf{F}) \cdot (\mathbf{X}_u \times \mathbf{X}_v) &= \alpha_1(y_u z_v - z_u y_v) + \alpha_2(z_u x_v - x_u z_v) + \alpha_3(x_u y_v - y_u x_v) \\
&= (R_y - Q_z)(y_u z_v - z_u y_v) \\
&\quad + (P_z - R_x)(z_u x_v - x_u z_v) \\
&\quad + (Q_x - P_y)(x_u y_v - y_u x_v).
\end{aligned} \tag{RHS}
$$

**Step 3: Pull back the left side (line integral).**

The line integral is:

$$
\oint_{\partial S} \mathbf{F} \cdot d\mathbf{r} = \oint_{\partial S} P \, dx + Q \, dy + R \, dz.
$$

On the boundary $\partial S$, the curve is parametrized by $\mathbf{X}(u(t), v(t))$ where $(u(t), v(t))$ traces $\partial D$. By the [[Multivariable Analysis §10 Composition of Functions and the Chain Rule#^thm-10-2|chain rule]]:

$$
dx = x_u \, du + x_v \, dv, \qquad dy = y_u \, du + y_v \, dv, \qquad dz = z_u \, du + z_v \, dv.
$$

Substituting:

$$
\begin{aligned}
P \, dx + Q \, dy + R \, dz &= P(x_u \, du + x_v \, dv) + Q(y_u \, du + y_v \, dv) + R(z_u \, du + z_v \, dv) \\
&= \underbrace{(Px_u + Qy_u + Rz_u)}_{=: \, \mathcal{A}(u,v)} du + \underbrace{(Px_v + Qy_v + Rz_v)}_{=: \, \mathcal{B}(u,v)} dv.
\end{aligned}
$$

Therefore:

$$
\oint_{\partial S} P \, dx + Q \, dy + R \, dz = \oint_{\partial D} \mathcal{A} \, du + \mathcal{B} \, dv. \tag{LHS}
$$

**Step 4: Apply Green's theorem on $D$.**

By Green's theorem ([[Multivariable Analysis §16 Line Integrals and Green's Theorem#^thm-16-1|Theorem §16.1]]) applied to the flat domain $D$:

$$
\oint_{\partial D} \mathcal{A} \, du + \mathcal{B} \, dv = \iint_D \left(\frac{\partial \mathcal{B}}{\partial u} - \frac{\partial \mathcal{A}}{\partial v}\right) du \, dv. \tag{LHS$'$}
$$

**Step 5: Compute $\frac{\partial \mathcal{B}}{\partial u} - \frac{\partial \mathcal{A}}{\partial v}$ and show it equals (RHS).**

This is the most involved step. We compute each partial derivative using the [[Multivariable Analysis §6 Differentiability#^thm-6-4|product rule]].

*Computing $\frac{\partial \mathcal{B}}{\partial u}$:* Recall $\mathcal{B} = Px_v + Qy_v + Rz_v$. By the product rule:

$$
\begin{aligned}
\frac{\partial \mathcal{B}}{\partial u} &= \frac{\partial P}{\partial u}x_v + P x_{vu} + \frac{\partial Q}{\partial u}y_v + Q y_{vu} + \frac{\partial R}{\partial u}z_v + R z_{vu}.
\end{aligned}
$$

Now $\frac{\partial P}{\partial u}$ is computed by the [[Multivariable Analysis §10 Composition of Functions and the Chain Rule#^thm-10-2|chain rule]] (since $P = P(x(u,v), y(u,v), z(u,v))$):

$$
\frac{\partial P}{\partial u} = P_x x_u + P_y y_u + P_z z_u.
$$

Similarly for $Q$ and $R$. Therefore:

$$
\begin{aligned}
\frac{\partial \mathcal{B}}{\partial u} &= (P_x x_u + P_y y_u + P_z z_u) x_v + P x_{uv} \\
&\quad + (Q_x x_u + Q_y y_u + Q_z z_u) y_v + Q y_{uv} \\
&\quad + (R_x x_u + R_y y_u + R_z z_u) z_v + R z_{uv}.
\end{aligned}
$$

*Computing $\frac{\partial \mathcal{A}}{\partial v}$:* By the identical argument with $u \leftrightarrow v$:

$$
\begin{aligned}
\frac{\partial \mathcal{A}}{\partial v} &= (P_x x_v + P_y y_v + P_z z_v) x_u + P x_{uv} \\
&\quad + (Q_x x_v + Q_y y_v + Q_z z_v) y_u + Q y_{uv} \\
&\quad + (R_x x_v + R_y y_v + R_z z_v) z_u + R z_{uv}.
\end{aligned}
$$

*Subtracting:* The second-derivative terms $Px_{uv}$, $Qy_{uv}$, $Rz_{uv}$ appear in both and **cancel** (this uses $x_{uv} = x_{vu}$, i.e., equality of mixed partials ([[Multivariable Analysis §5 Equality of Mixed Partials#^thm-5-1|Theorem §5.1]]) — this is why we need $\mathbf{X} \in C^2$).

Collecting the remaining terms by which partial derivatives of $P$, $Q$, $R$ they involve:

$$
\begin{aligned}
\frac{\partial \mathcal{B}}{\partial u} - \frac{\partial \mathcal{A}}{\partial v} &= P_x(x_u x_v - x_v x_u) + P_y(y_u x_v - y_v x_u) + P_z(z_u x_v - z_v x_u) \\
&\quad + Q_x(x_u y_v - x_v y_u) + Q_y(y_u y_v - y_v y_u) + Q_z(z_u y_v - z_v y_u) \\
&\quad + R_x(x_u z_v - x_v z_u) + R_y(y_u z_v - y_v z_u) + R_z(z_u z_v - z_v z_u).
\end{aligned}
$$

The “diagonal” terms vanish: $x_u x_v - x_v x_u = 0$, $y_u y_v - y_v y_u = 0$, $z_u z_v - z_v z_u = 0$.

Six terms remain. Regrouping by the cross product components:

$$
\begin{aligned}
\frac{\partial \mathcal{B}}{\partial u} - \frac{\partial \mathcal{A}}{\partial v} &= (R_y - Q_z)(y_u z_v - z_u y_v) \\
&\quad + (P_z - R_x)(z_u x_v - x_u z_v) \\
&\quad + (Q_x - P_y)(x_u y_v - y_u x_v).
\end{aligned}
$$

*Verification by direct expansion.* Rather than tracing individual terms through the regrouping, we verify by expanding both sides independently and checking they match.

**Expand (RHS):**

$$
\begin{aligned}
\text{(RHS)} &= R_y(y_u z_v - z_u y_v) - Q_z(y_u z_v - z_u y_v) \\
&\quad + P_z(z_u x_v - x_u z_v) - R_x(z_u x_v - x_u z_v) \\
&\quad + Q_x(x_u y_v - y_u x_v) - P_y(x_u y_v - y_u x_v).
\end{aligned}
$$

This gives 12 terms: $R_y y_u z_v$, $-R_y z_u y_v$, $-Q_z y_u z_v$, $Q_z z_u y_v$, $P_z z_u x_v$, $-P_z x_u z_v$, $-R_x z_u x_v$, $R_x x_u z_v$, $Q_x x_u y_v$, $-Q_x y_u x_v$, $-P_y x_u y_v$, $P_y y_u x_v$.

**Expand $\frac{\partial \mathcal{B}}{\partial u} - \frac{\partial \mathcal{A}}{\partial v}$** (the 6 surviving non-diagonal terms):

$$
\begin{aligned}
&P_y(y_u x_v - y_v x_u) + P_z(z_u x_v - z_v x_u) \\
+\; &Q_x(x_u y_v - x_v y_u) + Q_z(z_u y_v - z_v y_u) \\
+\; &R_x(x_u z_v - x_v z_u) + R_y(y_u z_v - y_v z_u).
\end{aligned}
$$

This gives: $P_y y_u x_v$, $-P_y y_v x_u$, $P_z z_u x_v$, $-P_z z_v x_u$, $Q_x x_u y_v$, $-Q_x x_v y_u$, $Q_z z_u y_v$, $-Q_z z_v y_u$, $R_x x_u z_v$, $-R_x x_v z_u$, $R_y y_u z_v$, $-R_y y_v z_u$.

These are exactly the same 12 terms (reordering factors within each product). Therefore:

$$
\frac{\partial \mathcal{B}}{\partial u} - \frac{\partial \mathcal{A}}{\partial v} = (\nabla \times \mathbf{F}) \cdot (\mathbf{X}_u \times \mathbf{X}_v).
$$

**Step 6: Combine.**

Putting Steps 3, 4, and 5 together:

$$
\oint_{\partial S} \mathbf{F} \cdot d\mathbf{r} = \oint_{\partial D} \mathcal{A} \, du + \mathcal{B} \, dv = \iint_D \left(\frac{\partial \mathcal{B}}{\partial u} - \frac{\partial \mathcal{A}}{\partial v}\right) du \, dv = \iint_D (\nabla \times \mathbf{F}) \cdot (\mathbf{X}_u \times \mathbf{X}_v) \, du \, dv = \iint_S (\nabla \times \mathbf{F}) \cdot d\mathbf{S}.
$$

This completes the proof. $\blacksquare$

*Uses:* [[Multivariable Analysis §18 Surface Integrals#^def-18-1|Def. §18.1]], [[Multivariable Analysis §18 Surface Integrals#^def-18-6|Def. §18.6]], [[Multivariable Analysis §16 Line Integrals and Green's Theorem#^def-16-5|Def. §16.5]], [[Multivariable Analysis §10 Composition of Functions and the Chain Rule#^thm-10-2|§10.2]], [[Multivariable Analysis §16 Line Integrals and Green's Theorem#^thm-16-1|§16.1]], [[Multivariable Analysis §6 Differentiability#^thm-6-4|§6.4]], [[Multivariable Analysis §5 Equality of Mixed Partials#^thm-5-1|§5.1]]

> [!remark] Remark: Structure of the Proof
> The proof has a clean logical flow:
> 1. **Pull back** both sides from $\mathbb{R}^3$ to the parameter domain $D \subseteq \mathbb{R}^2$.
> 2. **Apply Green's theorem** on the flat domain $D$.
> 3. **Verify** that the integrand on the RHS of Green's theorem equals $(\nabla \times \mathbf{F}) \cdot (\mathbf{X}_u \times \mathbf{X}_v)$ by expanding and comparing 12 terms.
>
> The key cancellation in Step 5 — the second-derivative terms $Px_{uv}$, $Qy_{uv}$, $Rz_{uv}$ dropping out — relies on equality of mixed partials ($x_{uv} = x_{vu}$, [[Multivariable Analysis §5 Equality of Mixed Partials#^thm-5-1|Theorem §5.1]]). This is why Stokes' theorem requires $\mathbf{X} \in C^2$ (not just $C^1$).
>
> Compare with the Divergence Theorem proof ([[Multivariable Analysis §18 Surface Integrals#^pf-18-2|Section 18]]), which reduced to the [[Fundamental Theorem of Calculus]]. Stokes' theorem instead reduces to [[Multivariable Analysis §16 Line Integrals and Green's Theorem#^thm-16-1|Green's theorem]] — one dimension lower, but on the parameter domain rather than in physical space.

^rem-20-3

> [!remark] Remark: Special Cases
> **1. Flat surface in $\mathbb{R}^2$:** If $S$ is a region $D$ in the $xy$-plane with $\hat{n} = \hat{k}$, then $(\nabla \times \mathbf{F}) \cdot \hat{k} = Q_x - P_y$ and Stokes' theorem reduces to Green's theorem ([[Multivariable Analysis §16 Line Integrals and Green's Theorem#^thm-16-3|Theorem §16.3]]):
>
> $$
> \oint_{\partial D} P \, dx + Q \, dy = \iint_D (Q_x - P_y) \, dx \, dy.
> $$
>
> **2. Closed surface (no boundary):** If $S$ is a closed surface ($\partial S = \emptyset$), then:
>
> $$
> \iint_S (\nabla \times \mathbf{F}) \cdot d\mathbf{S} = 0.
> $$
>
> The curl of any vector field has zero total flux through a closed surface. This is a special case of $d^2 = 0$ ([[Multivariable Analysis §22 The Algebra of Differential Forms#^thm-22-5|Theorem §22.5]]) in the language of differential forms.
>
> **3. Same boundary, different surfaces:** If $S_1$ and $S_2$ are two surfaces with the same boundary $\partial S_1 = \partial S_2 = C$ (and compatible orientations), then:
>
> $$
> \iint_{S_1} (\nabla \times \mathbf{F}) \cdot d\mathbf{S} = \oint_C \mathbf{F} \cdot d\mathbf{r} = \iint_{S_2} (\nabla \times \mathbf{F}) \cdot d\mathbf{S}.
> $$
>
> The surface integral of a curl depends only on the boundary, not on which surface spans it.

^rem-20-4

> [!remark] Remark: The Complete Picture
> With Stokes' theorem, we have proved all three integral theorems on the syllabus:
>
> | **Theorem** | **Domain** | **Boundary** | **Reduces to** |
> |---|:---:|:---:|:---:|
> | Green's (2D) ([[Multivariable Analysis §16 Line Integrals and Green's Theorem#^thm-16-1\|§16.1]]) | flat region $D \subseteq \mathbb{R}^2$ | curve $\partial D$ | FTC in each variable |
> | Divergence (3D) ([[Multivariable Analysis §18 Surface Integrals#^thm-18-2\|§18.2]]) | volume $V \subseteq \mathbb{R}^3$ | closed surface $\partial V$ | FTC in each variable |
> | Stokes' (3D) ([[Multivariable Analysis §20 Stokes' Theorem in ℝ³#^thm-20-1\|§20.1]]) | surface $S \subseteq \mathbb{R}^3$ | curve $\partial S$ | Green's on parameter domain |
>
> All three are special cases of the [[Multivariable Analysis §23 The Generalized Stokes' Theorem#^thm-23-1|generalized Stokes' theorem]] $\int_{\partial \Omega} \omega = \int_\Omega d\omega$, where $\omega$ is a differential form ([[Multivariable Analysis §21 Introduction to Differential Forms#^def-21-1|Def. §21.1]]) and $d$ is the exterior derivative ([[Multivariable Analysis §22 The Algebra of Differential Forms#^def-22-4|Def. §22.4]]).

^rem-20-5
