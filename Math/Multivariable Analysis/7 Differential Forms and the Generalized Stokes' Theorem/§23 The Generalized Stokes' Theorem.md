---
type: section
subject: "[[Multivariable Analysis]]"
chapter: 7
section: 23
tags: [multivariable-analysis, math452]
---
← [[§22 The Algebra of Differential Forms]] · ↑ [[· 7 Differential Forms and the Generalized Stokes' Theorem]]

## The Classical Theorems in Forms Language

We now translate each of the four integral theorems from Parts I–II into the language of forms, showing explicitly that both sides become form integrals. The pattern that emerges will lead to the generalized theorem.

### The Fundamental Theorem of Calculus

Classical statement ([[Fundamental Theorem of Calculus|FTC]]): $\int_a^b f'(x)\,dx = f(b) - f(a)$.

**Right-hand side.** Let $\omega = f$ be a 0-form. Its exterior derivative ([[§22 The Algebra of Differential Forms#^def-22-4|Def. §22.4]]) is $d\omega = df = f'(x)\,dx$ (a 1-form). So:

$$
\int_a^b f'(x)\,dx = \int_{[a,b]} d\omega.
$$

**Left-hand side.** The boundary of $[a,b]$ is the two-point set $\partial[a,b] = \{a, b\}$, with the induced orientation: $b$ gets $+$ (outward-pointing = rightward) and $a$ gets $-$ (outward-pointing = leftward). “Integrating” the 0-form $\omega = f$ over this oriented boundary means:

$$
\int_{\partial[a,b]} \omega = f(b) - f(a).
$$

**Result:**

$$
\int_{\partial[a,b]} \omega = \int_{[a,b]} d\omega. \quad \checkmark
$$

### Green's Theorem

Classical statement ([[Green's Theorem|Theorem §16.1]]): $\oint_{\partial D} P\,dx + Q\,dy = \iint_D (Q_x - P_y)\,dx\,dy$.

**Right-hand side.** Let $\omega = f_1\,dx + f_2\,dy$ be a 1-form on $\mathbb{R}^2$ (with $f_1 = P$, $f_2 = Q$). Its exterior derivative is:

$$
d\omega = \big((f_2)_x - (f_1)_y\big)\,dx \wedge dy.
$$

This is a 2-form, and integrating it over $D$ gives:

$$
\iint_D d\omega = \iint_D \big((f_2)_x - (f_1)_y\big)\,dx\,dy.
$$

**Left-hand side.** Parametrize the boundary $\partial D = \boldsymbol{\gamma}(t) = (x(t), y(t))$ counterclockwise. Pull back the 1-form ([[§22 The Algebra of Differential Forms#^def-22-5|Def. §22.5]]):

$$
\omega = f_1\,dx + f_2\,dy \quad \xrightarrow{\text{pullback}} \quad (f_1\,x' + f_2\,y')\,dt.
$$

So $\int_{\partial D} \omega = \int_a^b (f_1\,x' + f_2\,y')\,dt = \oint_{\partial D} f_1\,dx + f_2\,dy$.

**Result:**

$$
\int_{\partial D} \omega = \iint_D d\omega. \quad \checkmark
$$

### Stokes' Theorem in $\mathbb{R}^3$

Classical statement ([[Stokes' Theorem in ℝ³|Theorem §20.1]]): $\iint_S (\nabla \times \mathbf{F}) \cdot \hat{n}\,dS = \oint_{\partial S} \mathbf{F} \cdot d\mathbf{r}$.

**Right-hand side.** Let $\omega = f_1\,dx + f_2\,dy + f_3\,dz$ be a 1-form (with $\mathbf{F} = (f_1, f_2, f_3)$). By the curl proposition ([[§22 The Algebra of Differential Forms#^prop-22-3|Proposition §22.3]]):

$$
d\omega = \big((f_3)_y - (f_2)_z\big)\,dy \wedge dz + \big((f_1)_z - (f_3)_x\big)\,dz \wedge dx + \big((f_2)_x - (f_1)_y\big)\,dx \wedge dy.
$$

Now integrate over the surface $S$ parametrized by $\mathbf{X}(u,v)$. Each 2-form pulls back by the pullback of [[§22 The Algebra of Differential Forms#^def-22-3|Def. §22.3]] (the three $2 \times 2$ minors, [[§22 The Algebra of Differential Forms#^ex-22-3|Ex. §22.3]]):

$$
\begin{aligned}
\iint_S d\omega &= \iint_D \big[(f_3)_y - (f_2)_z\big](y_u z_v - z_u y_v) + \big[(f_1)_z - (f_3)_x\big](z_u x_v - x_u z_v) \\
&\qquad + \big[(f_2)_x - (f_1)_y\big](x_u y_v - y_u x_v) \; du\,dv \\
&= \iint_D (\nabla \times \mathbf{F}) \cdot (\mathbf{X}_u \times \mathbf{X}_v)\,du\,dv.
\end{aligned}
$$

Now compare with the classical form: $\iint_S (\nabla \times \mathbf{F}) \cdot \hat{n}\,dS$. Since $\hat{n}\,dS = \frac{\mathbf{X}_u \times \mathbf{X}_v}{|\mathbf{X}_u \times \mathbf{X}_v|} \cdot |\mathbf{X}_u \times \mathbf{X}_v|\,du\,dv$, the norms **cancel**:

$$
\iint_S (\nabla \times \mathbf{F}) \cdot \hat{n}\,dS = \iint_D (\nabla \times \mathbf{F}) \cdot (\mathbf{X}_u \times \mathbf{X}_v)\,du\,dv = \iint_S d\omega.
$$

This cancellation is the key simplification: the forms framework never introduces $|\mathbf{X}_u \times \mathbf{X}_v|$ in the first place — it works directly with the signed cross product components, which are the 2-form pullbacks.

**Left-hand side.** Parametrize the boundary $\partial S = \boldsymbol{\gamma}(t) = (x(t), y(t), z(t))$. Pull back:

$$
\omega = f_1\,dx + f_2\,dy + f_3\,dz \quad \xrightarrow{\text{pullback}} \quad (f_1\,x' + f_2\,y' + f_3\,z')\,dt = \mathbf{F} \cdot \boldsymbol{\gamma}'(t)\,dt.
$$

So $\int_{\partial S} \omega = \oint_{\partial S} \mathbf{F} \cdot d\mathbf{r}$.

**Result:**

$$
\int_{\partial S} \omega = \iint_S d\omega. \quad \checkmark
$$

### The Divergence Theorem

Classical statement ([[Divergence Theorem in ℝ³|Theorem §18.2]]): $\iint_{\partial V} \mathbf{F} \cdot \hat{n}\,dS = \iiint_V \nabla \cdot \mathbf{F}\,dV$.

**Right-hand side.** Let $\eta = f_{23}\,dy \wedge dz + f_{31}\,dz \wedge dx + f_{12}\,dx \wedge dy$ be a 2-form (with $\mathbf{F} = (f_{23}, f_{31}, f_{12})$). By the divergence proposition ([[§22 The Algebra of Differential Forms#^prop-22-4|Proposition §22.4]]):

$$
d\eta = \big((f_{23})_x + (f_{31})_y + (f_{12})_z\big)\,dx \wedge dy \wedge dz = (\nabla \cdot \mathbf{F})\,dx \wedge dy \wedge dz.
$$

Integrating over $V$:

$$
\iiint_V d\eta = \iiint_V \nabla \cdot \mathbf{F}\,dV.
$$

**Left-hand side.** The boundary $\partial V$ is a closed surface. Parametrize each piece by $\mathbf{X}(u,v)$. The 2-form $\eta$ pulls back via [[§22 The Algebra of Differential Forms#^def-22-3|Def. §22.3]]:

$$
\begin{aligned}
\iint_{\partial V} \eta &= \iint_D \big[f_{23}(y_u z_v - z_u y_v) + f_{31}(z_u x_v - x_u z_v) + f_{12}(x_u y_v - y_u x_v)\big]\,du\,dv \\
&= \iint_D \mathbf{F} \cdot (\mathbf{X}_u \times \mathbf{X}_v)\,du\,dv.
\end{aligned}
$$

Again the norm cancellation: since $\hat{n}\,dS = (\mathbf{X}_u \times \mathbf{X}_v)\,du\,dv$:

$$
\iint_{\partial V} \mathbf{F} \cdot \hat{n}\,dS = \iint_{\partial V} \eta.
$$

**Result:**

$$
\iint_{\partial V} \eta = \iiint_V d\eta. \quad \checkmark
$$

## Statement

All four classical theorems have the same form: $\int_{\partial \Omega} \omega = \int_\Omega d\omega$, where $\omega$ is a form of one degree lower than the dimension of $\Omega$. This is the generalized Stokes' theorem.

> [!theorem] Theorem §23.1: Generalized Stokes' Theorem
> Let $\Omega$ be an oriented, compact, piecewise smooth $k$-dimensional region with piecewise smooth boundary $\partial \Omega$ (with the induced orientation). If $\omega$ is a $(k-1)$-form that is $C^1$ on a neighborhood of $\Omega$, then:
>
> $$
> \boxed{\int_{\partial \Omega} \omega = \int_\Omega d\omega}
> $$

^thm-23-1

![[m452-23-2.svg]]
*The induced orientation of $\partial\Omega$ (red) in each case of the theorem. $k=1$: the boundary of $[a,b]$ is $b$ with sign $+$ and $a$ with sign $-$ (outward directions), giving $f(b)-f(a)$. $k=2$, flat: $\partial D$ runs counterclockwise, $D$ on the left. $k=2$, curved: $\partial S$ follows the right-hand rule around $\hat{n}$. $k=3$: $\partial V$ carries the outward normal. One rule covers all four — outward direction first, then the orientation of the boundary — and it is the rule that makes $\int_{\partial\Omega}\omega = \int_\Omega d\omega$ come out with no stray signs.*

> [!remark]- Connections
> - $k = 1$: [[Fundamental Theorem of Calculus]]; $k = 2$: [[Green's Theorem|Green's theorem (Theorem §16.1)]] and [[Stokes' Theorem in ℝ³|Stokes' theorem in ℝ³ (Theorem §20.1)]]; $k = 3$: [[Divergence Theorem in ℝ³|Divergence theorem in ℝ³ (Theorem §18.2)]].
> - Top degree in any dimension ($k = n$, $\Omega \subseteq \mathbb{R}^n$) is the [[Divergence Theorem in ℝⁿ|Divergence Theorem in ℝⁿ (Theorem §17.1)]].
> - Proof: the course states the theorem without proof, after checking the four classical cases above. A proof for compact oriented manifolds with boundary is in Lee, *Introduction to Smooth Manifolds*, Ch. 16, the textbook of [[Differentiable Manifolds]].
> - The orientation bookkeeping is carried by the sign of the pullback determinant ([[§22 The Algebra of Differential Forms#^def-22-3|Def. §22.3]]; [[§34 Determinants#^ladr-9-61|LADR 9.61]]).
> - Computational versions: [[§109 The Fundamental Theorem for Line Integrals#^thm-109-1|Calc Thm. §109.1]] (k = 1), [[§110 Green's Theorem#^thm-110-1|Calc Thm. §110.1]], [[§114 Stokes' Theorem#^thm-114-1|Calc Thm. §114.1]] and [[§115 The Divergence Theorem#^thm-115-1|Calc Thm. §115.1]] (with worked examples).

**Reading the formula:** $\omega$ is one degree lower than the dimension of $\Omega$, so $\omega$ can be integrated over $\partial \Omega$ (which has dimension $k-1$), and $d\omega$ can be integrated over $\Omega$ (which has dimension $k$). The four classical theorems are this single identity applied at $k = 1, 2, 2, 3$:

| **$k$** | **$\Omega$** | **$\omega$** | **$d\omega$** | **Classical name** |
|:-:|:-:|:-:|:-:|:-:|
| 1 | interval $[a,b]$ | 0-form $f$ | $f'\,dx$ | FTC |
| 2 | region $D \subseteq \mathbb{R}^2$ | 1-form on $\mathbb{R}^2$ | curl $\cdot\,dx \wedge dy$ | Green's |
| 2 | surface $S \subseteq \mathbb{R}^3$ | 1-form on $\mathbb{R}^3$ | curl $\cdot$ 2-form | Stokes' |
| 3 | volume $V \subseteq \mathbb{R}^3$ | 2-form | div $\cdot\,dx \wedge dy \wedge dz$ | Divergence |

![[m452-23-1.svg]]
*The ladder of forms in $\mathbb{R}^3$. Each rung of $d$ (red) is one classical differential operator, and under it (green) the integral theorem that trades that $d$ for a boundary $\partial$. The dashed arcs skip two rungs: the two vanishing identities, both instances of $d^2 = 0$.*

> [!remark] Remark: The Punchline
> All four theorems are the same theorem:
>
> $$
> \int_{\partial \Omega} \omega = \int_\Omega d\omega.
> $$
>
> The apparent differences — gradient vs curl vs divergence, line integrals vs surface integrals vs volume integrals — arise from the same operation $d$ applied to forms of different degrees, integrated over regions of different dimensions.
>
> The two identities $\text{curl}(\text{grad}) = 0$ and $\text{div}(\text{curl}) = 0$ are also a single identity, $d^2 = 0$ ([[Exterior Derivative Squares to Zero|Theorem §22.5]]). And the orientation signs that caused so much bookkeeping (the [[§18 Surface Integrals#^rem-18-7|bottom surface normal]], the boundary curve direction, the $f(b) - f(a)$ sign) are all automatically handled by the wedge product's anti-commutativity.
>
> This is why differential forms are the natural language for integration on manifolds: a single theorem, a single derivative, a single product rule for signs.

^rem-23-1
