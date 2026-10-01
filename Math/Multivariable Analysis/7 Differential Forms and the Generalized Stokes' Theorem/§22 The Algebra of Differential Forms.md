---
type: section
subject: "[[Multivariable Analysis]]"
chapter: 7
section: 22
tags: [multivariable-analysis, math452]
---
← [[§21 Introduction to Differential Forms]] · ↑ [[· 7 Differential Forms and the Generalized Stokes' Theorem]] · [[§23 The Generalized Stokes' Theorem]] →

## The Wedge Product

In [[§21 Introduction to Differential Forms#Why the Algebra Must Be Anti-Commutative|§21.6]], we discovered that coordinate substitution *forces* the multiplication of differentials to be anti-commutative. We now axiomatize these rules.

> [!remark] Note: Terminology: Properties of Operations
> An **operation** takes two inputs and produces one output (like $+$ or $\times$). We say an operation $\star$ is:
>
> **Linear in the first argument** if $(\alpha a + \beta b) \star c = \alpha (a \star c) + \beta (b \star c)$ for all scalars $\alpha, \beta$. That is, the operation distributes over addition and commutes with scalar multiplication — just like ordinary multiplication does.
>
> **Bilinear** ([[§35 Tensor Products#^ladr-9-77|LADR 9.77]]) if it is linear in each argument separately: linear in the first when the second is held fixed, and linear in the second when the first is held fixed. The dot product $\mathbf{u} \cdot \mathbf{v}$ and the cross product $\mathbf{u} \times \mathbf{v}$ are both bilinear. (You already use this implicitly every time you expand $(a\mathbf{u} + b\mathbf{v}) \times \mathbf{w} = a(\mathbf{u} \times \mathbf{w}) + b(\mathbf{v} \times \mathbf{w})$.)
>
> **Associative** if $(a \star b) \star c = a \star (b \star c)$, so parentheses don't matter. Addition and multiplication are associative; the cross product is *not* ($(\mathbf{u} \times \mathbf{v}) \times \mathbf{w} \neq \mathbf{u} \times (\mathbf{v} \times \mathbf{w})$ in general).
>
> **Commutative** if $a \star b = b \star a$. **Anti-commutative** if $a \star b = -(b \star a)$. The cross product is anti-commutative; the wedge product will be too.

^rem-22-1

> [!definition] Definition §22.1: Wedge Product
> The wedge product is an operation on forms satisfying three rules:
>
> 1. **Anti-commutativity:** $dx_i \wedge dx_j = -dx_j \wedge dx_i$ for any coordinate differentials.
> 2. **Linearity in each factor:** $(a\,\omega_1 + b\,\omega_2) \wedge \eta = a\,(\omega_1 \wedge \eta) + b\,(\omega_2 \wedge \eta)$, and similarly in the second factor. (This means you can expand wedge products using the distributive law, just like ordinary multiplication.)
> 3. **Associativity:** $(\omega \wedge \eta) \wedge \mu = \omega \wedge (\eta \wedge \mu)$.
>
> The key rule is:
>
> $$
> \boxed{dx_i \wedge dx_j = -dx_j \wedge dx_i}
> $$
>
> In particular, setting $i = j$: $dx_i \wedge dx_i = -dx_i \wedge dx_i$, which forces $dx_i \wedge dx_i = 0$.

^def-22-1

> [!remark]- Connections
> - Linear-algebra model: for functionals $\varphi, \tau$, $\varphi \wedge \tau(u,w) = \varphi(u)\tau(w) - \varphi(w)\tau(u)$ is an alternating bilinear form ([[§32 Bilinear Forms and Quadratic Forms#^ladr-9-15|LADR 9.15]]); anti-commutativity is the swap rule for alternating forms ([[§33 Alternating Multilinear Forms#^ladr-9-30|LADR 9.30]]).
> - The wedge of $k$ covectors is the alternating part of their tensor product $\varphi_1 \otimes \cdots \otimes \varphi_k$ (an $m$-linear functional, [[§35 Tensor Products#^ladr-9-85|LADR 9.85]], [[§35 Tensor Products#^ladr-9-88|LADR 9.88]]).

**Why anti-commutativity?** This encodes **orientation**. Recall:
- Swapping the order of parameters in a cross product flips the sign: $\mathbf{X}_u \times \mathbf{X}_v = -\mathbf{X}_v \times \mathbf{X}_u$.
- Changing the order of integration in a signed integral flips the sign: $\int_a^b = -\int_b^a$.
- The Jacobian determinant changes sign when two rows (or columns) are swapped.

All of these are manifestations of the same algebraic fact: $dx \wedge dy = -dy \wedge dx$. The wedge product is the single operation that captures orientation.

**Consequences:**

*1. Any repeated factor kills the product:* $dx \wedge dx = -dx \wedge dx = 0$.

*2. In $\mathbb{R}^3$, there are exactly 3 independent 2-forms:* $dy \wedge dz$, $dz \wedge dx$, $dx \wedge dy$. All others are either zero ($dx \wedge dx = 0$) or related by anti-commutativity ($dz \wedge dy = -dy \wedge dz$).

*3. There is exactly one independent 3-form:* $dx \wedge dy \wedge dz$. Any permutation of the factors gives $\pm dx \wedge dy \wedge dz$ (the sign is the sign of the permutation).

*4. In $\mathbb{R}^n$, there are $\binom{n}{k}$ independent $k$-forms:* choose which $k$ of the $n$ coordinate differentials appear. In $\mathbb{R}^3$: $\binom{3}{0} = 1$ function, $\binom{3}{1} = 3$ one-forms, $\binom{3}{2} = 3$ two-forms, $\binom{3}{3} = 1$ three-form.

> [!definition] Definition §22.2: Levi-Civita Symbol
> For indices $i_1, i_2, \ldots, i_k \in \{1, 2, \ldots, n\}$, the **Levi-Civita symbol** is:
>
> $$
> \varepsilon_{i_1 i_2 \cdots i_k} = \begin{cases} +1 & \text{if } (i_1, \ldots, i_k) \text{ is an even permutation of } (1, 2, \ldots, k), \\ -1 & \text{if } (i_1, \ldots, i_k) \text{ is an odd permutation of } (1, 2, \ldots, k), \\ 0 & \text{if any index is repeated.} \end{cases}
> $$

^def-22-2

> [!theorem] Proposition §22.1: Wedge Product Equals Levi-Civita Symbol
> For coordinate differentials $dx_i, dx_j$ in $\mathbb{R}^n$:
>
> $$
> dx_i \wedge dx_j = \varepsilon_{ij}\,dx \wedge dy \quad (\text{in } \mathbb{R}^2), \qquad dx_i \wedge dx_j \wedge dx_k = \varepsilon_{ijk}\,dx \wedge dy \wedge dz \quad (\text{in } \mathbb{R}^3).
> $$
>
> More generally, if $(i_1, \ldots, i_k)$ is a rearrangement of $(1, 2, \ldots, k)$ or has a repeated index, then $dx_{i_1} \wedge \cdots \wedge dx_{i_k} = \varepsilon_{i_1 \cdots i_k}\,dx_1 \wedge \cdots \wedge dx_k$. (For other index sets, sorting the indices gives $dx_{i_1} \wedge \cdots \wedge dx_{i_k} = \pm\, dx_{j_1} \wedge \cdots \wedge dx_{j_k}$ with $j_1 < \cdots < j_k$, the sign being that of the sorting permutation.)

^prop-22-1

> [!proof]+ Proof
> Both sides obey the same rules: (i) swapping two adjacent factors/indices negates the value (anti-commutativity of $\wedge$ and the sign rule for $\varepsilon$), and (ii) a repeated factor/index gives zero ($dx_i \wedge dx_i = 0$ and $\varepsilon_{\ldots i \ldots i \ldots} = 0$). Since both sides equal $+1$ on the identity permutation ($dx_1 \wedge \cdots \wedge dx_k$ and $\varepsilon_{12\ldots k} = 1$), they agree everywhere.

^pf-22-1

*Uses:* [[§22 The Algebra of Differential Forms#^def-22-1|Def. §22.1]], [[§22 The Algebra of Differential Forms#^def-22-2|Def. §22.2]], [[§33 Alternating Multilinear Forms#^ladr-9-34|LADR 9.34]]

> [!remark]- Connections
> - The same argument in linear algebra: an alternating form on permuted inputs picks up the sign of the permutation ([[§33 Alternating Multilinear Forms#^ladr-9-35|LADR 9.35]]), which yields the Leibniz formula for the determinant ([[§34 Determinants#^ladr-9-46|LADR 9.46]]).

The wedge product is the Levi-Civita symbol promoted from a numerical table to an algebraic operation.

> [!example] Example §22.1: Computing with Wedge Products
> Let $\omega = x \, dy + y \, dz$ (a 1-form) and $\eta = z \, dx + x \, dy$ (a 1-form). Their wedge product is a 2-form:
>
> $$
> \begin{aligned}
> \omega \wedge \eta &= (x \, dy + y \, dz) \wedge (z \, dx + x \, dy) \\
> &= xz \, dy \wedge dx + x^2 \, dy \wedge dy + yz \, dz \wedge dx + xy \, dz \wedge dy \\
> &= -xz \, dx \wedge dy + 0 + yz \, dz \wedge dx - xy \, dy \wedge dz \\
> &= -xy \, dy \wedge dz + yz \, dz \wedge dx - xz \, dx \wedge dy.
> \end{aligned}
> $$

^ex-22-1

We can now formalize the computation from [[§21 Introduction to Differential Forms#Why the Algebra Must Be Anti-Commutative|§21.6]]. The key concept is the *pullback*: the operation that translates a form from ambient coordinates to parameter coordinates so that it can be integrated.

> [!definition] Definition §22.3: Pullback
> Let $\omega$ be a differential form on $\mathbb{R}^n$, expressed in the **ambient coordinates** $x_1, \ldots, x_n$.
>
> Let $\Phi: D \subseteq \mathbb{R}^k \to \mathbb{R}^n$ be a $C^1$ map (a **parametrization**), where $D$ has its own **parameter coordinates** $u_1, \ldots, u_k$. The map $\Phi$ relates the two coordinate systems:
>
> $$
> \Phi(u_1, \ldots, u_k) = \big(x_1(u_1, \ldots, u_k),\; \ldots,\; x_n(u_1, \ldots, u_k)\big).
> $$
>
> The **pullback** $\Phi^*\omega$ is the form on $D$ obtained by:
> 1. Replacing each ambient differential $dx_i$ with $\displaystyle\sum_{j=1}^k \frac{\partial x_i}{\partial u_j}\,du_j$ (the [[Multivariable Chain Rule|chain rule]]),
> 2. Expanding using the wedge product rules.
>
> The integral of $\omega$ over $\Phi(D)$ is then defined as:
>
> $$
> \int_{\Phi(D)} \omega \;=\; \int_D \Phi^*\omega.
> $$

^def-22-3

![[m452-22-1.svg]]
*The two directions of the pullback story. The parametrization $\Phi$ pushes points forward: $(u,v) \mapsto \mathbf{X}(u,v)$. The pullback $\Phi^*$ pulls forms backward: a form written in ambient differentials $dx_i$ becomes a form in parameter differentials $du_j$, via $dx_i = \sum_j (x_i)_{u_j}\,du_j$. Integration always happens at the parameter end — $\int_{\Phi(D)}\omega$ is defined as $\int_D \Phi^*\omega$.*

> [!remark]- Connections
> - The coefficients of $\Phi^*\omega$ are $k \times k$ minors of the Jacobian, i.e. determinants ([[§34 Determinants#^ladr-9-46|LADR 9.46]]); in the top-degree case $k = n$ this is the signed volume factor $\det J$, whose absolute value is the volume distortion ([[§34 Determinants#^ladr-9-61|LADR 9.61]], [[§15 Multivariable Integration#^prop-15-19|Proposition §15.19]]).
> - Pulling back and then applying $d$ is how the classical theorems become one statement: [[Generalized Stokes' Theorem|Theorem §23.1]].
> - On a manifold the same substitution, $dx^i = \sum_j \frac{\partial x^i}{\partial y^j}\,dy^j$, is how covectors change between charts: [[§17 The Tangent Bundle#^prop-17-5|591 Prop. §17.5]].

> [!remark] Remark: Clarification of Terms
> The ambient coordinates $(x_1, \ldots, x_n)$ are the standard coordinates on $\mathbb{R}^n$ — the space the form lives in. The parameter coordinates $(u_1, \ldots, u_k)$ are the coordinates on $D$ — the space we integrate over. The parametrization $\Phi$ is the bridge: it tells us, for each point in $D$, where it sits in $\mathbb{R}^n$. You have been using parametrizations all semester:
>
> | **Object** | **$\Phi$** | $k$ | $n$ | **Parameter coords** | **Ambient coords** |
> |---|---|:-:|:-:|---|---|
> | Curve in $\mathbb{R}^3$ | $\boldsymbol{\gamma}(t)$ | 1 | 3 | $t$ | $(x,y,z)$ |
> | Surface in $\mathbb{R}^3$ | $\mathbf{X}(u,v)$ | 2 | 3 | $(u,v)$ | $(x,y,z)$ |
> | Polar coords | $(r\cos\theta, r\sin\theta)$ | 2 | 2 | $(r,\theta)$ | $(x,y)$ |
> | Spherical coords | $(r\sin\phi\cos\theta, \ldots)$ | 3 | 3 | $(r,\theta,\phi)$ | $(x,y,z)$ |
>
> The pullback is what you compute every time you “substitute the parametrization into the integral” — now given a name and a systematic procedure.

^rem-22-2

**Carrying out the pullback** produces determinants of minors of the Jacobian matrix $J = \big[\frac{\partial x_i}{\partial u_j}\big]$ (which is $n \times k$):

$$
\Phi^*(dx_{i_1} \wedge \cdots \wedge dx_{i_k}) = \det \begin{pmatrix} (x_{i_1})_{u_1} & \cdots & (x_{i_1})_{u_k} \\ \vdots & \ddots & \vdots \\ (x_{i_k})_{u_1} & \cdots & (x_{i_k})_{u_k} \end{pmatrix} du_1 \wedge \cdots \wedge du_k.
$$

That is, the pullback of a coordinate $k$-form extracts the $k \times k$ minor of $J$ corresponding to rows $i_1, \ldots, i_k$. This is not a new result — it is what happens when you carry out steps 1 and 2 of the definition. Each $dx_{i_\ell}$ becomes $\sum_j (x_{i_\ell})_{u_j}\,du_j$; wedging $k$ of these and using anti-commutativity kills all terms with repeated $du_j$; the surviving terms are the Leibniz formula for the determinant ([[§34 Determinants#^ladr-9-46|LADR 9.46]]) (compare the informal $2 \times 2$ computation in [[§21 Introduction to Differential Forms#Why the Algebra Must Be Anti-Commutative|§21.6]]).

> [!example] Example §22.2: Pullback Along a Curve (Line Integral, §16)
> Let $\omega = f_1\,dx + f_2\,dy + f_3\,dz$ be a 1-form on $\mathbb{R}^3$, and $\boldsymbol{\gamma}: [a,b] \to \mathbb{R}^3$ a curve with $\boldsymbol{\gamma}(t) = (x(t), y(t), z(t))$.
>
> The Jacobian is $3 \times 1$: $J = \begin{pmatrix} x' \\ y' \\ z' \end{pmatrix}$. Pull back:
>
> $$
> \boldsymbol{\gamma}^*\omega = f_1\,x'\,dt + f_2\,y'\,dt + f_3\,z'\,dt = (f_1 x' + f_2 y' + f_3 z')\,dt.
> $$
>
> So:
>
> $$
> \int_{\boldsymbol{\gamma}} \omega = \int_a^b (f_1 x' + f_2 y' + f_3 z')\,dt.
> $$
>
> This is the line integral $\int_{\boldsymbol{\gamma}} \mathbf{F} \cdot d\mathbf{r}$ from [[§16 Line Integrals and Green's Theorem#^def-16-2|§16]].

^ex-22-2

> [!example] Example §22.3: Pullback Along a Surface (Flux Integral, §18)
> Let $\eta = f_{23}\,dy \wedge dz + f_{31}\,dz \wedge dx + f_{12}\,dx \wedge dy$ be a 2-form on $\mathbb{R}^3$, and $\mathbf{X}: D \to \mathbb{R}^3$ a surface with $\mathbf{X}(u,v) = (x(u,v), y(u,v), z(u,v))$.
>
> The Jacobian is $3 \times 2$: $J = \begin{pmatrix} x_u & x_v \\ y_u & y_v \\ z_u & z_v \end{pmatrix}$. The three $2 \times 2$ minors give:
>
> $$
> \begin{aligned}
> \mathbf{X}^*(dy \wedge dz) &= (y_u z_v - z_u y_v)\,du\,dv, \\
> \mathbf{X}^*(dz \wedge dx) &= (z_u x_v - x_u z_v)\,du\,dv, \\
> \mathbf{X}^*(dx \wedge dy) &= (x_u y_v - y_u x_v)\,du\,dv.
> \end{aligned}
> $$
>
> So:
>
> $$
> \iint_S \eta = \iint_D \big[f_{23}(y_u z_v - z_u y_v) + f_{31}(z_u x_v - x_u z_v) + f_{12}(x_u y_v - y_u x_v)\big]\,du\,dv.
> $$
>
> The three parenthesized quantities are the components of $\mathbf{X}_u \times \mathbf{X}_v$, so this is $\iint_D \mathbf{F} \cdot (\mathbf{X}_u \times \mathbf{X}_v)\,du\,dv$ — the flux integral from [[§18 Surface Integrals#^def-18-6|§18]].

^ex-22-3

> [!example] Example §22.4: Pullback for Change of Variables (§15)
> Let $\mu = f\,dx \wedge dy$ be a 2-form on $\mathbb{R}^2$, and $\Phi: D^* \to \mathbb{R}^2$ a coordinate change with $\Phi(u,v) = (x(u,v), y(u,v))$.
>
> The Jacobian is $2 \times 2$: $J = \begin{pmatrix} x_u & x_v \\ y_u & y_v \end{pmatrix}$. There is $\binom{2}{2} = 1$ minor — the full determinant:
>
> $$
> \Phi^*(dx \wedge dy) = (x_u y_v - x_v y_u)\,du \wedge dv = (\det J)\,du\,dv.
> $$
>
> So:
>
> $$
> \iint_D f\,dx\,dy = \iint_{D^*} f(\Phi(u,v)) \cdot (\det J)\,du\,dv.
> $$
>
> This is the *signed* change of variables formula. The $|J|$ version from [[Change of Variables Formula (multiple integrals)|§15]] takes the absolute value, discarding the orientation ([[§21 Introduction to Differential Forms#Signed, Unsigned, and Signed in Disguise|Category 3]]).

^ex-22-4

> [!remark] Remark: The Cross Product Is the Pullback in Disguise
> In $\mathbb{R}^3$, the three $2 \times 2$ minors of the Jacobian are exactly the three components of the cross product:
>
> $$
> \mathbf{X}_u \times \mathbf{X}_v = \big(\underbrace{y_u z_v - z_u y_v}_{\mathbf{X}^*(dy \wedge dz)}, \;\; \underbrace{z_u x_v - x_u z_v}_{\mathbf{X}^*(dz \wedge dx)}, \;\; \underbrace{x_u y_v - y_u x_v}_{\mathbf{X}^*(dx \wedge dy)}\big).
> $$
>
> The cross product packages the pullbacks of all three coordinate 2-forms into a single vector. This packaging only works in $\mathbb{R}^3$, because $\binom{3}{2} = 3$: the number of independent 2-forms equals the dimension. In $\mathbb{R}^4$ there would be $\binom{4}{2} = 6$ minors — not packageable as a vector. The pullback works in any dimension; the cross product is its $\mathbb{R}^3$ shortcut.

^rem-22-3

> [!remark]- Connections
> - The cross product in components and as a determinant: [[§83 The Cross Product#^def-83-1|Calc Def. §83.1]], [[§83 The Cross Product#^prop-83-1|Calc Prop. §83.1]].

## The Exterior Derivative

The exterior derivative $d$ takes a $k$-form to a $(k+1)$-form. It is defined by a simple recipe and turns out to unify the gradient, curl, and divergence.

> [!definition] Definition §22.4: Exterior Derivative
> **On 0-forms** (functions $f$):
>
> $$
> df = \frac{\partial f}{\partial x} dx + \frac{\partial f}{\partial y} dy + \frac{\partial f}{\partial z} dz.
> $$
>
> This is the total differential from [[§8 The Differential#^def-8-1|Section 8]] — the same $df$ we have been writing all semester.
>
> **On 1-forms** ($\omega = f_1 \, dx + f_2 \, dy + f_3 \, dz$): apply $d$ to each coefficient and wedge with the existing differential:
>
> $$
> d\omega = df_1 \wedge dx + df_2 \wedge dy + df_3 \wedge dz
> $$
>
> where $df_1 = (f_1)_x \, dx + (f_1)_y \, dy + (f_1)_z \, dz$, etc.
>
> **On 2-forms** ($\eta = f_{23} \, dy \wedge dz + f_{31} \, dz \wedge dx + f_{12} \, dx \wedge dy$): same rule:
>
> $$
> d\eta = df_{23} \wedge dy \wedge dz + df_{31} \wedge dz \wedge dx + df_{12} \wedge dx \wedge dy.
> $$

^def-22-4

The recipe is always the same: differentiate each coefficient, wedge the result with the existing differentials, and simplify using anti-commutativity.

> [!theorem] Proposition §22.2: $d$ on 0-Forms Gives the Gradient
> For a smooth function $f$ on $\mathbb{R}^3$:
>
> $$
> df = f_x \, dx + f_y \, dy + f_z \, dz.
> $$
>
> That is, the coefficients of the 1-form $df$ are the components of $\nabla f = (f_x, f_y, f_z)$. The differential from [[§8 The Differential#^def-8-1|§8]] and the gradient from [[Directional Derivative Formula|§7]] are the same object: one is a 1-form, the other is the corresponding vector field.

^prop-22-2

> [!theorem] Proposition §22.3: $d$ on 1-Forms Gives the Curl
> For a smooth 1-form $\omega = f_1 \, dx + f_2 \, dy + f_3 \, dz$ on $\mathbb{R}^3$:
>
> $$
> d\omega = \big((f_3)_y - (f_2)_z\big) \, dy \wedge dz + \big((f_1)_z - (f_3)_x\big) \, dz \wedge dx + \big((f_2)_x - (f_1)_y\big) \, dx \wedge dy.
> $$
>
> That is, the coefficients of the 2-form $d\omega$ are the components of $\nabla \times \mathbf{F}$ where $\mathbf{F} = (f_1, f_2, f_3)$ (written $P, Q, R$ in §16–§20). The curl, first introduced in [[§11 The Three Differential Operators꞉ Gradient, Curl, Divergence|§11]] and [[§16 Line Integrals and Green's Theorem#^def-16-5|§16]], is $d$ applied to a 1-form.

^prop-22-3

> [!proof]+ Proof
> Compute:
>
> $$
> \begin{aligned}
> d\omega &= df_1 \wedge dx + df_2 \wedge dy + df_3 \wedge dz \\
> &= ((f_1)_x \, dx + (f_1)_y \, dy + (f_1)_z \, dz) \wedge dx + ((f_2)_x \, dx + (f_2)_y \, dy + (f_2)_z \, dz) \wedge dy \\
> &\quad + ((f_3)_x \, dx + (f_3)_y \, dy + (f_3)_z \, dz) \wedge dz.
> \end{aligned}
> $$
>
> Expanding, using $dx \wedge dx = dy \wedge dy = dz \wedge dz = 0$:
>
> $$
> \begin{aligned}
> d\omega &= (f_1)_y \, dy \wedge dx + (f_1)_z \, dz \wedge dx \\
> &\quad + (f_2)_x \, dx \wedge dy + (f_2)_z \, dz \wedge dy \\
> &\quad + (f_3)_x \, dx \wedge dz + (f_3)_y \, dy \wedge dz.
> \end{aligned}
> $$
>
> Using anti-commutativity to put each term in standard order ($dy \wedge dz$, $dz \wedge dx$, $dx \wedge dy$):
>
> $$
> d\omega = \big((f_3)_y - (f_2)_z\big) \, dy \wedge dz + \big((f_1)_z - (f_3)_x\big) \, dz \wedge dx + \big((f_2)_x - (f_1)_y\big) \, dx \wedge dy.
> $$
>
> The three coefficients are exactly the components of $\nabla \times \mathbf{F}$.

^pf-22-3

*Uses:* [[§22 The Algebra of Differential Forms#^def-22-4|Def. §22.4]], [[§22 The Algebra of Differential Forms#^def-22-1|Def. §22.1]], [[§16 Line Integrals and Green's Theorem#^def-16-5|Def. §16.5]]

> [!theorem] Proposition §22.4: $d$ on 2-Forms Gives the Divergence
> For a smooth 2-form $\eta = f_{23} \, dy \wedge dz + f_{31} \, dz \wedge dx + f_{12} \, dx \wedge dy$ on $\mathbb{R}^3$:
>
> $$
> d\eta = \big((f_{23})_x + (f_{31})_y + (f_{12})_z\big) \, dx \wedge dy \wedge dz.
> $$
>
> That is, the coefficient of the 3-form $d\eta$ is $\nabla \cdot \mathbf{F}$ where $\mathbf{F} = (f_{23}, f_{31}, f_{12})$ (written $\mathbf{u} = (a, b, c)$ in §18). The divergence, first introduced in [[§11 The Three Differential Operators꞉ Gradient, Curl, Divergence|§11]] and [[§16 Line Integrals and Green's Theorem#^def-16-4|§16]], is $d$ applied to a 2-form.

^prop-22-4

> [!proof]+ Proof
> Compute:
>
> $$
> \begin{aligned}
> d\eta &= df_{23} \wedge dy \wedge dz + df_{31} \wedge dz \wedge dx + df_{12} \wedge dx \wedge dy \\
> &= ((f_{23})_x \, dx + (f_{23})_y \, dy + (f_{23})_z \, dz) \wedge dy \wedge dz \\
> &\quad + ((f_{31})_x \, dx + (f_{31})_y \, dy + (f_{31})_z \, dz) \wedge dz \wedge dx \\
> &\quad + ((f_{12})_x \, dx + (f_{12})_y \, dy + (f_{12})_z \, dz) \wedge dx \wedge dy.
> \end{aligned}
> $$
>
> In each line, only the term with the “missing” differential survives (all others have a repeated factor):
>
> $$
> \begin{aligned}
> d\eta &= (f_{23})_x \, dx \wedge dy \wedge dz + (f_{31})_y \, dy \wedge dz \wedge dx + (f_{12})_z \, dz \wedge dx \wedge dy.
> \end{aligned}
> $$
>
> Reorder each to the standard $dx \wedge dy \wedge dz$ (each is an even permutation):
>
> $$
> d\eta = \big((f_{23})_x + (f_{31})_y + (f_{12})_z\big) \, dx \wedge dy \wedge dz.
> $$
>
> The coefficient is $\nabla \cdot \mathbf{F}$.

^pf-22-4

*Uses:* [[§22 The Algebra of Differential Forms#^def-22-4|Def. §22.4]], [[§22 The Algebra of Differential Forms#^def-22-1|Def. §22.1]], [[§22 The Algebra of Differential Forms#^prop-22-1|§22.1]], [[§16 Line Integrals and Green's Theorem#^def-16-4|Def. §16.4]]

These three propositions are summarized in the following table:

| **Input** | **Output** | **$d$ computes** | **Vector calculus name** |
|:-:|:-:|:-:|:-:|
| 0-form $f$ | 1-form $df$ | $\nabla f$ | gradient |
| 1-form $\omega$ | 2-form $d\omega$ | $\nabla \times \mathbf{F}$ | curl |
| 2-form $\eta$ | 3-form $d\eta$ | $\nabla \cdot \mathbf{F}$ | divergence |

### The Ladder: Gradient, Curl, and Divergence Are Not at the Same Level

In vector calculus, gradient, curl, and divergence all appear to be “differential operators on vector fields”:

$$
f \xrightarrow{\nabla} \mathbf{F} \xrightarrow{\nabla\times} \mathbf{G} \xrightarrow{\nabla\cdot} h.
$$

It seems like curl and divergence sit at the same level — both take vector fields and produce something. The identities $\nabla \times (\nabla f) = \mathbf{0}$ and $\nabla \cdot (\nabla \times \mathbf{F}) = 0$ look like two separate facts.

In the forms picture, they form a **ladder**:

$$
\underbrace{f}_{\text{0-form}} \xrightarrow{\;d\;} \underbrace{P\,dx + Q\,dy + R\,dz}_{\text{1-form}} \xrightarrow{\;d\;} \underbrace{A\,dy \wedge dz + B\,dz \wedge dx + C\,dx \wedge dy}_{\text{2-form}} \xrightarrow{\;d\;} \underbrace{h\,dx \wedge dy \wedge dz}_{\text{3-form}}
$$

Each arrow is the *same* operator $d$, but applied at a different rung:
- $d$ on a 0-form (degree $0 \to 1$) = gradient
- $d$ on a 1-form (degree $1 \to 2$) = curl
- $d$ on a 2-form (degree $2 \to 3$) = divergence

Curl and divergence are **not** at the same level: curl goes from degree 1 to degree 2, divergence goes from degree 2 to degree 3. The two “separate” identities $\nabla \times (\nabla f) = 0$ and $\nabla \cdot (\nabla \times \mathbf{F}) = 0$ are the single identity $d \circ d = 0$ applied at consecutive rungs.

> [!remark] Remark: The $\mathbb{R}^3$ Accident
> Why do curl and divergence *look* like they are at the same level in vector calculus? Because of a coincidence specific to $\mathbb{R}^3$.
>
> In $\mathbb{R}^n$, the number of independent $k$-forms is $\binom{n}{k}$. In $\mathbb{R}^3$:
>
> $$
> \binom{3}{0} = 1, \qquad \binom{3}{1} = 3, \qquad \binom{3}{2} = 3, \qquad \binom{3}{3} = 1.
> $$
>
> Both 1-forms and 2-forms have **3 components**. Since a vector field in $\mathbb{R}^3$ also has 3 components, we can represent *both* as vector fields. This lets us write both curl and divergence as operations on “vector fields,” hiding the fact that they act on forms of different degrees.
>
> **This coincidence fails in every other dimension:**
> - In $\mathbb{R}^2$: $\binom{2}{1} = 2$ components for 1-forms, $\binom{2}{2} = 1$ component for 2-forms. The “curl” of a 1-form $P\,dx + Q\,dy$ is the 2-form $(Q_x - P_y)\,dx \wedge dy$ — a single scalar, not a vector. This is why the 2D curl in [[§16 Line Integrals and Green's Theorem#^thm-16-3|Green's theorem]] is a number, not a vector field.
> - In $\mathbb{R}^4$: $\binom{4}{1} = 4$ components for 1-forms, $\binom{4}{2} = 6$ components for 2-forms. The “curl” of a 1-form is a 6-component object — it cannot be represented as a vector field. The cross product does not exist in $\mathbb{R}^4$ for the same reason.
>
> The exterior derivative $d$ works in *any* dimension. The vector calculus operators grad, curl, div are dimension-3 translations of $d$ that rely on the coincidence $\binom{3}{1} = \binom{3}{2}$.
>
> This also explains a fact from physics: the electromagnetic field in 4D spacetime is naturally a 2-form $F$ (with 6 independent components: 3 for $\mathbf{E}$, 3 for $\mathbf{B}$). Maxwell's equations become $dF = 0$ and $d{*}F = J$. The fact that $\mathbf{E}$ and $\mathbf{B}$ combine into a single object is invisible in 3D vector calculus but natural in the language of forms.

^rem-22-4

## $d^2 = 0$: The Unifying Identity

> [!theorem] Theorem §22.5: $d^2 = 0$
> For any smooth $k$-form $\omega$: $d(d\omega) = 0$.

^thm-22-5

> [!proof]+ Proof
> It suffices to check on a 0-form $f$ (the general case follows by linearity and the product rule).
>
> Compute $d(df)$: we have $df = f_x \, dx + f_y \, dy + f_z \, dz$, so:
>
> $$
> \begin{aligned}
> d(df) &= (f_{xy} \, dy + f_{xz} \, dz) \wedge dx + (f_{yx} \, dx + f_{yz} \, dz) \wedge dy + (f_{zx} \, dx + f_{zy} \, dy) \wedge dz \\
> &= f_{xy} \, dy \wedge dx + f_{xz} \, dz \wedge dx + f_{yx} \, dx \wedge dy + f_{yz} \, dz \wedge dy \\
> &\quad + f_{zx} \, dx \wedge dz + f_{zy} \, dy \wedge dz.
> \end{aligned}
> $$
>
> Using $dy \wedge dx = -dx \wedge dy$, etc.:
>
> $$
> d(df) = (f_{yx} - f_{xy}) \, dx \wedge dy + (f_{xz} - f_{zx}) \, dz \wedge dx + (f_{zy} - f_{yz}) \, dy \wedge dz = 0
> $$
>
> by equality of mixed partials ([[Schwarz–Clairaut Theorem|Schwarz–Clairaut]]) ($f_{xy} = f_{yx}$, etc.).

^pf-22-5

*Uses:* [[§22 The Algebra of Differential Forms#^def-22-4|Def. §22.4]], [[§22 The Algebra of Differential Forms#^def-22-1|Def. §22.1]], [[Schwarz–Clairaut Theorem|§5.1]]

> [!remark]- Connections
> - Why it works: the second derivative is a symmetric bilinear form and $d$ keeps only the alternating part ([[§22 The Algebra of Differential Forms#^prop-22-9|Proposition §22.9]]; linear algebra: [[§32 Bilinear Forms and Quadratic Forms#^ladr-9-17|LADR 9.17]]).
> - Used in Relativity: $d^2 = 0$ makes a gauge transformation leave the coupling of a charge and the field tensor unchanged — [[§B3.2 The Charged Particle#^thm-b3-2-3|REL Theorem §B3.2.3]]; and makes the homogeneous Maxwell pair an identity for any field tensor built from a potential — [[§B4.2 The Electromagnetic Field Tensor#^thm-b4-2-7|REL Theorem §B4.2.7]].
> - Vector-field form: $\operatorname{curl}\nabla f = \mathbf 0$, [[§111 Curl and Divergence#^thm-111-1|Calc Thm. §111.1]], and $\operatorname{div}\operatorname{curl}\mathbf F = 0$, [[§111 Curl and Divergence#^thm-111-3|Calc Thm. §111.3]].

> [!remark] Remark: Classical Consequences of $d^2 = 0$
> The identity $d^2 = 0$ applied at consecutive rungs of the ladder gives:
> - Rung $0 \to 1 \to 2$: $d(df) = 0$, i.e., $\nabla \times (\nabla f) = \mathbf{0}$. The curl of a gradient is zero.
> - Rung $1 \to 2 \to 3$: $d(d\omega) = 0$ for a 1-form, i.e., $\nabla \cdot (\nabla \times \mathbf{F}) = 0$. The divergence of a curl is zero.
>
> These are not two separate computational accidents — they are the *same* identity $d \circ d = 0$ applied at different points on the ladder. This also explains why the flux of a curl through a closed surface $S$ vanishes: by [[Stokes' Theorem in ℝ³|Stokes']], $\iint_S (\nabla \times \mathbf{F}) \cdot d\mathbf{S} = \int_S d\omega = \int_{\partial S} \omega = 0$ since $\partial S = \emptyset$ (equivalently, by the Divergence Theorem, since $\nabla \cdot (\nabla \times \mathbf{F}) = 0$).

^rem-22-5

## Translating the Known Integrals into Forms

With the wedge product, exterior derivative, and $d^2 = 0$ in hand, we can define what it means to integrate a differential form. The key idea is **pullback**: substitute the parametrization into the form to obtain a function on the parameter domain, then integrate that function.

> [!definition] Definition §22.5: Integration of a 1-Form over a Curve
> Let $\omega = f_1\,dx + f_2\,dy + f_3\,dz$ be a $C^0$ 1-form on an open set $U \subseteq \mathbb{R}^3$, and let $\boldsymbol{\gamma}: [a,b] \to U$ be a $C^1$ curve. The integral of $\omega$ over $\boldsymbol{\gamma}$ is defined by pulling back: substitute $dx = x'(t)\,dt$, $dy = y'(t)\,dt$, $dz = z'(t)\,dt$:
>
> $$
> \int_{\boldsymbol{\gamma}} \omega \;=\; \int_a^b \big(f_1\,x' + f_2\,y' + f_3\,z'\big)\,dt.
> $$

^def-22-5

> [!remark] Remark: 1-Form Integration Recovers the Line Integral
> The integral $\int_{\boldsymbol{\gamma}} \omega$ is the same as the line integral $\int_{\boldsymbol{\gamma}} \mathbf{F} \cdot d\mathbf{r}$ from [[§16 Line Integrals and Green's Theorem#^def-16-2|§16]], where $\mathbf{F} = (f_1, f_2, f_3)$: expanding $\mathbf{F} \cdot d\mathbf{r} = (f_1, f_2, f_3) \cdot (x', y', z')\,dt$ gives the same integrand.

^rem-22-6

> [!definition] Definition §22.6: Integration of a 2-Form over a Surface
> Let $\eta = f_{23}\,dy \wedge dz + f_{31}\,dz \wedge dx + f_{12}\,dx \wedge dy$ be a $C^0$ 2-form, and let $\mathbf{X}: D \to \mathbb{R}^3$ be a $C^1$ parametrized surface. The integral of $\eta$ over $S = \mathbf{X}(D)$ is defined by pulling back: substitute $dy \wedge dz = (y_u z_v - z_u y_v)\,du\,dv$, etc.:
>
> $$
> \iint_S \eta \;=\; \iint_D (f_{23}, f_{31}, f_{12}) \cdot (\mathbf{X}_u \times \mathbf{X}_v)\,du\,dv.
> $$

^def-22-6

> [!remark] Remark: 2-Form Integration Recovers the Flux Integral
> The integral $\iint_S \eta$ is the same as the flux integral $\iint_S \mathbf{F} \cdot d\mathbf{S}$ from [[§18 Surface Integrals#^def-18-6|§18]], where $\mathbf{F} = (f_{23}, f_{31}, f_{12})$: the cross product $\mathbf{X}_u \times \mathbf{X}_v$ produces the oriented area element, and the dot product selects the normal component of $\mathbf{F}$.

^rem-22-7

> [!remark] Remark: Scalar Integrals Are Not Form Integrals
> The scalar line integral $\int_{\boldsymbol{\gamma}} f\,ds$ and the scalar surface integral $\iint_S f\,dS$ cannot be expressed as integrals of differential forms. Their elements $ds = |\boldsymbol{\gamma}'(t)|\,dt$ and $dS = |\mathbf{X}_u \times \mathbf{X}_v|\,du\,dv$ involve absolute values, making them orientation-independent ([[§21 Introduction to Differential Forms#Signed, Unsigned, and Signed in Disguise|Category 2]]). Since they carry no sign, they do not participate in any integral theorem.

^rem-22-8

> [!example] Example §22.5: Flux Through the Unit Sphere via Pullback
> Compute $\iint_S \eta$ where $\eta = z\,dx \wedge dy$ (a 2-form) and $S$ is the unit sphere with outward orientation.
>
> **Step 1: Parametrize.** Use spherical coordinates:
>
> $$
> \mathbf{X}(\phi, \theta) = (\cos\phi\sin\theta, \;\sin\phi\sin\theta, \;\cos\theta), \qquad \phi \in [0, 2\pi], \;\; \theta \in [0, \pi].
> $$
>
> **Step 2: Pull back.** On the sphere, $z = \cos\theta$, and we need $\mathbf{X}^*(dx \wedge dy)$. Compute:
>
> $$
> \begin{aligned}
> dx &= -\sin\phi\sin\theta\,d\phi + \cos\phi\cos\theta\,d\theta, \\
> dy &= \cos\phi\sin\theta\,d\phi + \sin\phi\cos\theta\,d\theta.
> \end{aligned}
> $$
>
> By the pullback definition:
>
> $$
> \begin{aligned}
> \mathbf{X}^*(dx \wedge dy) &= \det \begin{pmatrix} x_\phi & x_\theta \\ y_\phi & y_\theta \end{pmatrix} d\phi\,d\theta \\
> &= \det \begin{pmatrix} -\sin\phi\sin\theta & \cos\phi\cos\theta \\ \cos\phi\sin\theta & \sin\phi\cos\theta \end{pmatrix} d\phi\,d\theta \\
> &= (-\sin^2\phi\sin\theta\cos\theta - \cos^2\phi\sin\theta\cos\theta)\,d\phi\,d\theta \\
> &= -\sin\theta\cos\theta\,d\phi\,d\theta.
> \end{aligned}
> $$
>
> **Step 3: Integrate.** Pull back the full 2-form:
>
> $$
> \mathbf{X}^*\eta = \mathbf{X}^*(z\,dx \wedge dy) = \cos\theta \cdot (-\sin\theta\cos\theta)\,d\phi\,d\theta = -\cos^2\theta\sin\theta\,d\phi\,d\theta.
> $$
>
> So:
>
> $$
> \begin{aligned}
> \iint_S \eta &= \int_0^{2\pi}\int_0^{\pi} (-\cos^2\theta\sin\theta)\,d\theta\,d\phi = -2\pi \int_0^{\pi} \cos^2\theta\sin\theta\,d\theta \\
> &= -2\pi \left[-\frac{\cos^3\theta}{3}\right]_0^{\pi} = -2\pi\left(\frac{1}{3} + \frac{1}{3}\right) = -\frac{4\pi}{3}.
> \end{aligned}
> $$
>
> **Verification.** The 2-form $\eta = z\,dx \wedge dy$ corresponds to the flux of $\mathbf{F} = (0, 0, z)$ through $S$. By the [[Divergence Theorem in ℝ³|Divergence Theorem]]: $\iint_S \mathbf{F} \cdot d\mathbf{S} = \iiint_V \nabla \cdot \mathbf{F}\,dV = \iiint_V 1\,dV = \frac{4\pi}{3}$. The sign discrepancy is because our parametrization gives the *inward* normal (check: at $\theta = \pi/2$, $\phi = 0$, i.e., at $(1, 0, 0)$, the cross product $\mathbf{X}_\phi \times \mathbf{X}_\theta = (0, 1, 0) \times (0, 0, -1) = (-1, 0, 0)$ points inward). Reversing the parameter order gives $+\frac{4\pi}{3}$. $\checkmark$

^ex-22-5

The following tables summarize the translation at each dimension.

**Dimension 0.** A 0-form is a function $f$. “Integrating” it means evaluating: $\int_{\{p\}} f = f(p)$. Its exterior derivative is the 1-form $df = f_x\,dx + f_y\,dy + f_z\,dz$.

**Dimension 1.** The integrals over curves:

| **Vector calculus** | **Forms expression** | **Form?** |
|---|---|---|
| $\int_a^b f'(x)\,dx$ | $\int_{[a,b]} df$ | yes: 1-form $df$ |
| $\int_\gamma f_1\,dx + f_2\,dy + f_3\,dz$ | $\int_\gamma \omega$, $\omega = f_1\,dx + f_2\,dy + f_3\,dz$ | yes: 1-form $\omega$ |
| $\int_\gamma f\,ds$ | no form expression | no (uses $\vert\boldsymbol{\gamma}'\vert$) |

The scalar line integral $\int_\gamma f\,ds$ has no form expression because $ds = |\boldsymbol{\gamma}'|\,dt$ involves an absolute value — it is intrinsically unsigned (Category 2).

**Dimension 2.** The integrals over flat regions and surfaces:

| **Vector calculus** | **Forms expression** | **Form?** |
|---|---|---|
| $\oint_{\partial D} f_1\,dx + f_2\,dy$<br>$= \iint_D \big((f_2)_x - (f_1)_y\big)\,dA$ | $\int_{\partial D} \omega = \int_D d\omega$ | Green's thm |
| $\iint_S \mathbf{F} \cdot d\mathbf{S}$ | $\iint_S \eta$, $\eta = f_{23}\,dy \wedge dz$<br>$+ \, f_{31}\,dz \wedge dx + f_{12}\,dx \wedge dy$ | yes: 2-form $\eta$ |
| $\iint_{D^*} f(\Phi)\,\vert J\vert\,du\,dv$ | no form expression (uses $\vert J\vert$) | no (Cat. 3) |
| $\iint_S f\,dS$ | no form expression (uses $\vert\mathbf{X}_u \times \mathbf{X}_v\vert$) | no (Cat. 2) |

[[Green's Theorem|Green's theorem]] is now visibly a special case of $\int_{\partial \Omega} \omega = \int_\Omega d\omega$ with $\omega$ a 1-form on $\mathbb{R}^2$ and $d\omega = \big((f_2)_x - (f_1)_y\big)\,dx \wedge dy$.

The change-of-variables integral from [[Change of Variables Formula (multiple integrals)|§15]] and the scalar surface integral both lack form expressions: the first suppresses orientation via $|J|$ (Category 3), the second is intrinsically unsigned (Category 2).

**Dimension 3.** The integral over volumes:

| **Vector calculus** | **Forms expression** | **Form?** |
|---|---|---|
| $\iint_{\partial V} \mathbf{F} \cdot \hat{n}\,dS = \iiint_V \nabla \cdot \mathbf{F}\,dV$ | $\int_{\partial V} \eta = \int_V d\eta$ | Div. thm |
| $\iiint_V f\,dx\,dy\,dz$ | $\int_V f\,dx \wedge dy \wedge dz$ | yes: 3-form |

The Divergence Theorem is $\int_{\partial V} \eta = \int_V d\eta$ with $\eta$ a 2-form and $d\eta = \big((f_{23})_x + (f_{31})_y + (f_{12})_z\big)\,dx \wedge dy \wedge dz$.

**Summary: the chain of form integrals.**

| **Dim** | **Form integral** | **$d$ connects to…** | **Theorem** |
|:-:|:-:|:-:|:-:|
| 0 | $f(p)$ | $\int_\Omega df$ (dim 1) | FTC |
| 1 | $\int_\gamma \omega$ | $\int_\Omega d\omega$ (dim 2) | Green's / Stokes' |
| 2 | $\iint_S \eta$ | $\int_\Omega d\eta$ (dim 3) | Divergence |
| 3 | $\iiint_V \mu$ | — | (top dimension) |

Each row is related to the next by the exterior derivative $d$. The integral theorems are the statement that moving down one row (applying $d$ and integrating over the region) equals staying in the current row and integrating over the boundary. This is the content of the generalized Stokes' theorem in [[Generalized Stokes' Theorem|§23]].

## What the Exterior Derivative Really Measures

### What “Derivative” Means, Revisited

To understand what $d$ can and cannot do, we need to revisit what “derivative” actually means — not as a computational recipe, but as a mathematical object.

Recall from [[§6 Differentiability#^def-6-1|§6]]: $f$ is differentiable at $\mathbf{p} \in \mathbb{R}^n$ if there exists a linear map $Df_{\mathbf{p}}: \mathbb{R}^n \to \mathbb{R}$ satisfying $f(\mathbf{p} + \mathbf{h}) = f(\mathbf{p}) + Df_{\mathbf{p}}(\mathbf{h}) + o(|\mathbf{h}|)$, where $\mathbf{p} = (x_0, y_0, \ldots)$ and $\mathbf{h} = (h, k, \ldots)$ are vectors in $\mathbb{R}^n$.

> [!theorem] Proposition §22.6: Gradient = Differential = 1-Form
> The total derivative $Df_{\mathbf{p}}$ from [[§6 Differentiability#^def-6-2|§6]], the differential $df$ from [[§8 The Differential#^def-8-1|§8]], and the gradient $\nabla f$ from [[Directional Derivative Formula|§7]] are three notations for the same linear map on tangent vectors:
>
> $$
> Df_{\mathbf{p}}(\mathbf{v}) = df(\mathbf{v}) = \nabla f \cdot \mathbf{v} = f_x v_1 + f_y v_2 + f_z v_3.
> $$
>
> Its components are the partial derivatives: $Df_{\mathbf{p}}(\hat{e}_i) = f_{x_i}(\mathbf{p})$.

^prop-22-6

> [!remark]- Connections
> - $Df_{\mathbf{p}}$ is a linear functional on $\mathbb{R}^n$ ([[§12 Duality#^ladr-3-108|LADR 3.108]]); the gradient is the vector that represents it via the dot product, by the [[Riesz representation theorem|Riesz representation theorem (LADR 6.42)]].
> - On a manifold with no inner product only the differential survives, not the gradient vector: [[§13 Tangent Spaces III꞉ The Cotangent Space#^rem-13-2|591 §13, Differential — Not Gradient]].

> [!definition] Definition §22.7: Second Total Derivative
> For $f: \mathbb{R}^n \to \mathbb{R}$ of class $C^2$ at $\mathbf{p}$, the **second total derivative** $D^2f_{\mathbf{p}}: \mathbb{R}^n \times \mathbb{R}^n \to \mathbb{R}$ is the bilinear form ([[§32 Bilinear Forms and Quadratic Forms#^ladr-9-1|LADR 9.1]]):
>
> $$
> D^2f_{\mathbf{p}}(\mathbf{u}, \mathbf{v}) = \lim_{t \to 0} \frac{Df_{\mathbf{p}+t\mathbf{u}}(\mathbf{v}) - Df_{\mathbf{p}}(\mathbf{v})}{t}.
> $$
>
> It measures how the directional derivative $Df(\mathbf{v})$ changes as you move in direction $\mathbf{u}$.

^def-22-7

> [!theorem] Proposition §22.7: The Second Total Derivative Is the Hessian
> In coordinates:
>
> $$
> D^2f_{\mathbf{p}}(\mathbf{u}, \mathbf{v}) = \sum_{i,j} f_{x_i x_j}(\mathbf{p})\, u_i\, v_j.
> $$
>
> The matrix of $D^2f_{\mathbf{p}}$ in the standard basis ([[§32 Bilinear Forms and Quadratic Forms#^ladr-9-4|LADR 9.4]]) is the Hessian from [[§14 Optimization and Lagrange Multipliers#^def-14-2|§14]]: $[D^2f_{\mathbf{p}}]_{ij} = f_{x_i x_j}(\mathbf{p})$.

^prop-22-7

Two directions appear because we are asking two separate questions: $\mathbf{v}$ asks “which directional derivative are we looking at?” and $\mathbf{u}$ asks “in which direction are we watching it change?” The Taylor expansion from [[Multivariable Taylor's Theorem|§9]] says exactly:

$$
f(\mathbf{p}+\mathbf{h}) = f(\mathbf{p}) + \underbrace{Df_{\mathbf{p}}(\mathbf{h})}_{\text{linear: gradient}} + \frac{1}{2}\underbrace{D^2f_{\mathbf{p}}(\mathbf{h}, \mathbf{h})}_{\text{bilinear: Hessian}} + o(|\mathbf{h}|^2).
$$

The second derivative test in [[Second Derivative Test in Several Variables|§14]] (checking whether $\mathbf{h}^T H_f \mathbf{h} > 0$ for all $\mathbf{h}$) was asking: is this bilinear form positive definite?

### Why $d^2 = 0$: Symmetry Kills Antisymmetry

> [!theorem] Proposition §22.8: Decomposition of Bilinear Forms
> Any bilinear form $B: \mathbb{R}^n \times \mathbb{R}^n \to \mathbb{R}$ decomposes uniquely as $B = B^{\mathrm{sym}} + B^{\mathrm{anti}}$, where:
>
> $$
> B^{\mathrm{sym}}(\mathbf{u}, \mathbf{v}) = \tfrac{1}{2}\big(B(\mathbf{u}, \mathbf{v}) + B(\mathbf{v}, \mathbf{u})\big), \qquad B^{\mathrm{anti}}(\mathbf{u}, \mathbf{v}) = \tfrac{1}{2}\big(B(\mathbf{u}, \mathbf{v}) - B(\mathbf{v}, \mathbf{u})\big).
> $$
>
> The symmetric part satisfies $B^{\mathrm{sym}}(\mathbf{u}, \mathbf{v}) = B^{\mathrm{sym}}(\mathbf{v}, \mathbf{u})$; the antisymmetric part satisfies $B^{\mathrm{anti}}(\mathbf{u}, \mathbf{v}) = -B^{\mathrm{anti}}(\mathbf{v}, \mathbf{u})$.

^prop-22-8

> [!remark]- Connections
> - This is $V^{(2)} = V^{(2)}_{\mathrm{sym}} \oplus V^{(2)}_{\mathrm{alt}}$ in LADR ([[§32 Bilinear Forms and Quadratic Forms#^ladr-9-17|LADR 9.17]]), with antisymmetric = alternating by [[§32 Bilinear Forms and Quadratic Forms#^ladr-9-16|LADR 9.16]].

> [!theorem] Proposition §22.9: $d^2 = 0$ Is Clairaut's Theorem in Forms Language
> For $C^2$ functions, the following three statements are the same fact in three languages (all three hold, by Clairaut's theorem):
> 1. Equality of mixed partials: $f_{x_i x_j} = f_{x_j x_i}$ (Clairaut's theorem, [[Schwarz–Clairaut Theorem|§5]]).
> 2. The Hessian is symmetric: $D^2f(\mathbf{u}, \mathbf{v}) = D^2f(\mathbf{v}, \mathbf{u})$.
> 3. $d^2 = 0$: the exterior derivative applied twice gives zero.

^prop-22-9

> [!proof]+ Proof
> (1) $\Leftrightarrow$ (2): The Hessian matrix $[D^2f]_{ij} = f_{x_ix_j}$ is symmetric if and only if $f_{x_ix_j} = f_{x_jx_i}$.
>
> (2) $\Leftrightarrow$ (3): The exterior derivative $d$ produces antisymmetric outputs. Applied to $df$, it extracts the antisymmetric part of the second derivative:
>
> $$
> d(df) = \sum_{i < j} (f_{x_j x_i} - f_{x_i x_j})\,dx_i \wedge dx_j.
> $$
>
> This vanishes for all $f$ if and only if the antisymmetric part $\frac{1}{2}(f_{x_ix_j} - f_{x_jx_i})$ is zero, which is exactly the symmetry of the Hessian.

^pf-22-9

*Uses:* [[§22 The Algebra of Differential Forms#^prop-22-7|§22.7]], [[§22 The Algebra of Differential Forms#^def-22-4|Def. §22.4]], [[§22 The Algebra of Differential Forms#^prop-22-8|§22.8]], [[§32 Bilinear Forms and Quadratic Forms#^ladr-9-17|LADR 9.17]]

The circle of ideas is:

[[§5 Equality of Mixed Partials|§5]] (mixed partials commute: $f_{xy} = f_{yx}$) $\;\longleftrightarrow\;$ [[§14 Optimization and Lagrange Multipliers|§14]] (Hessian is symmetric) $\;\longleftrightarrow\;$ §22 ($d^2 = 0$).

**The two branches of bilinear algebra.** From “bilinear maps on tangent vectors,” two independent theories branch off:
- **Symmetric** ([[§32 Bilinear Forms and Quadratic Forms#^ladr-9-9|LADR 9.9]]): inner products, metrics, Hessians, the second derivative test. This is the world of Riemannian geometry (Chapter 13 of Lee).
- **Antisymmetric** ([[§32 Bilinear Forms and Quadratic Forms#^ladr-9-14|LADR 9.14]]): forms, wedge products, determinants, orientation. This is the world of differential forms (Chapter 14 of Lee).

Both arise from bilinear algebra; neither contains the other. The Hessian lives in the symmetric branch; forms live in the antisymmetric branch. The identity $d^2 = 0$ is the statement that the second derivative is entirely symmetric — so the antisymmetric branch sees nothing there.

## Closed and Exact Forms

### What $d$ Actually Measures: Obstructions to Exactness

If $d$ does not give higher derivatives of functions, what *does* it do on higher forms?

At each level, $d$ measures the **obstruction to solving an equation**:

**On 0-forms:** $df$ measures how $f$ changes. The equation $df = 0$ means $f$ is constant.

**On 1-forms:** $d\omega$ measures how far $\omega$ is from being the differential of some function. The equation $d\omega = 0$ means $\omega$ is *closed* — it satisfies the integrability condition. But closed does not mean *exact*: $\omega = df$ for some $f$. The question “is every closed 1-form exact?” depends on the *topology* of the domain.

**On 2-forms:** $d\eta$ measures how far $\eta$ is from being $d\omega$ for some 1-form $\omega$. The equation $d\eta = 0$ means $\eta$ is closed; the question “is $\eta = d\omega$?” again depends on the topology.

> [!definition] Definition §22.8: Closed and Exact Forms
> A differential form $\omega$ is **closed** if $d\omega = 0$. It is **exact** if $\omega = d\eta$ for some form $\eta$ of one degree lower.

^def-22-8

> [!theorem] Proposition §22.10: Exact $\Rightarrow$ Closed
> Every exact form is closed.

^prop-22-10

> [!proof]+ Proof
> If $\omega = d\eta$, then $d\omega = d(d\eta) = d^2\eta = 0$ by [[Exterior Derivative Squares to Zero|Theorem §22.5]].

^pf-22-10

*Uses:* [[§22 The Algebra of Differential Forms#^def-22-8|Def. §22.8]], [[Exterior Derivative Squares to Zero|§22.5]]

> [!remark]- Connections
> - Vector-field form: a conservative field satisfies $P_y = Q_x$, [[§109 The Fundamental Theorem for Line Integrals#^thm-109-4|Calc Thm. §109.4]], and $\operatorname{curl}\nabla f = \mathbf 0$, [[§111 Curl and Divergence#^thm-111-1|Calc Thm. §111.1]] (with worked examples).

The forms terminology and the vector calculus terminology from [[§11 The Three Differential Operators꞉ Gradient, Curl, Divergence#^def-11-1|§11]] describe the same concepts:

| **Forms (§22)** | **Vector calculus (§11)** | **Condition** |
|---|---|---|
| exact 1-form: $\omega = df$ | conservative (gradient) field: $\mathbf{F} = \nabla f$ | has a potential |
| closed 1-form: $d\omega = 0$ | irrotational (curl-free) field: $\nabla \times \mathbf{F} = \mathbf{0}$ | no local rotation |
| exact 2-form: $\eta = d\omega$ | $\mathbf{F} = \nabla \times \mathbf{G}$ for some $\mathbf{G}$ | is a curl |
| closed 2-form: $d\eta = 0$ | solenoidal (divergence-free): $\nabla \cdot \mathbf{F} = 0$ | no net flux |
| exact $\Rightarrow$ closed | conservative $\Rightarrow$ irrotational; curl $\Rightarrow$ solenoidal | $d^2 = 0$ |

The converse — is every closed form exact? — is the central question. Equivalently:
- *Is every curl-free vector field a gradient?* (Is every closed 1-form exact?)
- *Is every divergence-free vector field a curl?* (Is every closed 2-form exact?)

> [!theorem] Proposition §22.11: A Closed Form That Is Not Exact
> On $\mathbb{R}^2 \setminus \{0\}$ (the plane with the origin removed), the 1-form
>
> $$
> \omega = \frac{-y\,dx + x\,dy}{x^2 + y^2}
> $$
>
> is closed ($d\omega = 0$) but not exact (there is no function $f$ on $\mathbb{R}^2 \setminus \{0\}$ with $df = \omega$).

^prop-22-11

> [!proof]+ Proof
> *Closed:* Write $\omega = f_1\,dx + f_2\,dy$ with $f_1 = \frac{-y}{x^2+y^2}$ and $f_2 = \frac{x}{x^2+y^2}$. Compute:
>
> $$
> (f_2)_x - (f_1)_y = \frac{(x^2+y^2) - x \cdot 2x}{(x^2+y^2)^2} - \frac{-(x^2+y^2) + y \cdot 2y}{(x^2+y^2)^2} = \frac{y^2 - x^2 + x^2 - y^2}{(x^2+y^2)^2} = 0.
> $$
>
> *Not exact:* Integrate $\omega$ around the unit circle $\boldsymbol{\gamma}(t) = (\cos t, \sin t)$ for $t \in [0, 2\pi]$:
>
> $$
> \int_{\boldsymbol{\gamma}} \omega = \int_0^{2\pi} \frac{-\sin t \cdot (-\sin t) + \cos t \cdot \cos t}{1}\,dt = \int_0^{2\pi} 1\,dt = 2\pi \neq 0.
> $$
>
> If $\omega = df$ for some $f$, the integral around any closed curve would be $f(\text{end}) - f(\text{start}) = 0$ ([[Fundamental Theorem of Calculus|FTC]]). The nonzero integral is a contradiction.

^pf-22-11

*Uses:* [[§22 The Algebra of Differential Forms#^def-22-8|Def. §22.8]], [[§22 The Algebra of Differential Forms#^def-22-4|Def. §22.4]], [[§22 The Algebra of Differential Forms#^def-22-5|Def. §22.5]], [[Multivariable Chain Rule|§10.2]], [[Fundamental Theorem of Calculus|451 §34.1]]

What went wrong? The domain $\mathbb{R}^2 \setminus \{0\}$ has a *hole* — the removed origin. The closed curve $\boldsymbol{\gamma}$ wraps around this hole, and the form $\omega$ detects it. On domains without holes, this failure does not occur:

![[m452-22-2.svg]]
*The vector field $\frac{(-y,\,x)}{x^2+y^2}$ of $\omega = \frac{-y\,dx + x\,dy}{x^2+y^2}$ (blue; arrow lengths shrink like $1/r$) circulates around the removed origin (hollow dot). Locally the field is a gradient (the curl vanishes), but no global potential exists: the counterclockwise unit circle $\boldsymbol{\gamma}$ (red) picks up $\int_{\boldsymbol{\gamma}}\omega = 2\pi$ per loop around the hole. The form measures the winding — an analytic object detecting a topological feature.*

> [!remark]- Connections
> - The topological side of the same hole: $\pi_1(\mathbb{R}^2 \setminus \{0\}) \cong \pi_1(S^1)$ ([[§26 Deformation Retracts and Homotopy Type#^thm-26-2|590 §26.2]]) $\cong \mathbb{Z}$ ([[Fundamental Group of the Circle]]); $\frac{1}{2\pi}\int_{\boldsymbol{\gamma}}\omega$ counts the winding.
> - Used in Electromagnetism: $\omega$ is the field $\hat\varphi/s$ of a line current, curl-free off the axis with circulation $2\pi$ around it, so its curl is a delta function on the axis — [[§B1.2 The Dirac Delta Function and the Helmholtz Theorem#^ex-b1-2-2|EM Example §B1.2.2]]; the warning that curl-free is not enough on a region with a hole — [[§B1.2 The Dirac Delta Function and the Helmholtz Theorem#^cau-b1-2-1|EM Caution: Curl-free is not enough on a region with a hole]].

> [!theorem] Proposition §22.12: Poincaré Lemma
> On a star-shaped domain $D \subseteq \mathbb{R}^n$ (i.e., there exists a point $\mathbf{p}_0 \in D$ such that the line segment from $\mathbf{p}_0$ to any $\mathbf{p} \in D$ lies entirely in $D$), every closed form is exact: $d\omega = 0 \;\Rightarrow\; \omega = d\eta$ for some $\eta$.
>
> In particular, since $\mathbb{R}^n$ itself is star-shaped, every closed form on $\mathbb{R}^n$ is exact.

^prop-22-12

![[m452-22-3.svg]]
*Why star-shaped is the right hypothesis. Left: from $\mathbf{p}_0$ every segment stays in the domain, so a potential can be built by integrating along these segments (the homotopy operator) — closed forms are exact. Right: in $\mathbb{R}^2\setminus\{\mathbf{0}\}$ no point works as $\mathbf{p}_0$: the segment to the point $\mathbf{p}$ opposite the hole runs through the removed origin, and indeed the closed form of Proposition §22.11 is not exact there.*

> [!remark]- Connections
> - A star-shaped domain contracts to $\mathbf{p}_0$ along the segments — a [[§22 Homotopy of Paths#^thm-22-1|straight-line homotopy (590 §22.1)]] — so it is [[§23 The Fundamental Group#^def-23-3|simply connected (590 Def. §23.3)]]; the homotopy operator in the proof integrates along exactly these segments.
> - Used in Electromagnetism: on a star-shaped region a curl-free field is a gradient and a divergence-free field is a curl, which gives the scalar and vector potentials — [[§B1.2 The Dirac Delta Function and the Helmholtz Theorem#^thm-b1-2-3|EM Theorem §B1.2.3]], with the hole case in [[§B1.2 The Dirac Delta Function and the Helmholtz Theorem#^cau-b1-2-1|EM Caution: Curl-free is not enough on a region with a hole]].
> - Used in Relativity: on a region without holes every field tensor obeying the homogeneous Maxwell pair comes from a four-potential — [[§B4.2 The Electromagnetic Field Tensor#^thm-b4-2-7|REL Theorem §B4.2.7]], [[§B4.2 The Electromagnetic Field Tensor#^rem-b4-2-4|REL Remark: Layers, and what comes later]].
> - Vector-field form: curl-free fields on ℝ³ are conservative, [[§114 Stokes' Theorem#^thm-114-4|Calc Thm. §114.4]], and the plane test on simply-connected regions, [[§110 Green's Theorem#^thm-110-5|Calc Thm. §110.5]] (with worked examples).

The proof (constructing $\eta$ explicitly via a homotopy operator) is beyond the scope of this course; see Lee, Chapter 17. The key point is that the failure of exactness is a *topological* property of the domain — it detects holes.

### From Obstructions to Topology

The space of closed forms modulo exact forms:

$$
H^k = \frac{\{\text{closed } k\text{-forms}\}}{\{\text{exact } k\text{-forms}\}}
$$

is called the **$k$-th de Rham cohomology group**. It measures the “$k$-dimensional holes” in the domain:
- $H^0$ counts the connected components: no 0-form is exact (there are no $(-1)$-forms), so $H^0$ is the space of closed 0-forms, i.e., locally constant functions, with one dimension per [[§13 Connected Spaces#^def-13-1|connected]] component.
- $H^1$ detects 1-dimensional holes: loops that cannot be contracted to a point. The example above ([[§22 The Algebra of Differential Forms#^prop-22-11|Proposition §22.11]]) shows $H^1(\mathbb{R}^2 \setminus \{0\}) \neq 0$.
- $H^2$ detects 2-dimensional holes: closed surfaces that do not bound a volume.

This is the bridge from calculus to topology: the exterior derivative $d$, defined purely by differentiation, detects the *shape* of the domain. This is the content of Chapters 17–18 of Lee's textbook (the 591 syllabus), and connects directly to the [[§23 The Fundamental Group#^def-23-2|fundamental group]] $\pi_1$ from 590.

## Applications to Physics

In physics, the exterior derivative on higher forms is not abstract at all — it describes the fundamental forces.

The electromagnetic potential $A$ is a 1-form. Its exterior derivative $F = dA$ is a 2-form — the electromagnetic field tensor (with 6 independent components: 3 for $\mathbf{E}$, 3 for $\mathbf{B}$, as discussed in [[§22 The Algebra of Differential Forms#^rem-22-4|Remark: The ℝ³ Accident]]). Two of Maxwell's equations become:

$$
dF = 0 \qquad \text{(no magnetic monopoles; Faraday's law)}.
$$

This is just $d^2A = 0$ — the identity $d^2 = 0$ is the reason magnetic monopoles do not exist (in classical electromagnetism). The other two Maxwell equations are $d{*}F = J$, where $*$ is the Hodge star and $J$ is the current 3-form.

More generally, in gauge theory and general relativity, the curvature of a connection is a 2-form, and the equations of motion (Yang–Mills, Einstein) are expressed as conditions on this curvature 2-form and its exterior derivative. The machinery of forms and $d$ is not a reformulation of known physics — it is the *native language* in which modern theoretical physics is written.
