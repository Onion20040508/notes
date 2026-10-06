---
type: section
subject: "[[Multivariable Analysis]]"
chapter: 7
section: 37
tags: [multivariable-analysis, math452]
---
← [[§36 Introduction to Differential Forms]] · ↑ [[· 7 Differential Forms and the Generalized Stokes' Theorem]] · [[§38 The Exterior Derivative]] →

## The Wedge Product

In [[§36 Introduction to Differential Forms#Why the Algebra Must Be Anti-Commutative|§36]], we discovered that coordinate substitution *forces* the multiplication of differentials to be anti-commutative. We now axiomatize these rules.

> [!remark] Note: Terminology: Properties of Operations
> An **operation** takes two inputs and produces one output (like $+$ or $\times$). We say an operation $\star$ is:
>
> **Linear in the first argument** if $(\alpha a + \beta b) \star c = \alpha (a \star c) + \beta (b \star c)$ for all scalars $\alpha, \beta$. That is, the operation distributes over addition and commutes with scalar multiplication — just like ordinary multiplication does.
>
> **Bilinear** ([[§38 Tensor Products#^ladr-9-77|LADR 9.77]]) if it is linear in each argument separately: linear in the first when the second is held fixed, and linear in the second when the first is held fixed. The dot product $\mathbf{u} \cdot \mathbf{v}$ and the cross product $\mathbf{u} \times \mathbf{v}$ are both bilinear. (You already use this implicitly every time you expand $(a\mathbf{u} + b\mathbf{v}) \times \mathbf{w} = a(\mathbf{u} \times \mathbf{w}) + b(\mathbf{v} \times \mathbf{w})$.)
>
> **Associative** if $(a \star b) \star c = a \star (b \star c)$, so parentheses don't matter. Addition and multiplication are associative; the cross product is *not* ($(\mathbf{u} \times \mathbf{v}) \times \mathbf{w} \neq \mathbf{u} \times (\mathbf{v} \times \mathbf{w})$ in general).
>
> **Commutative** if $a \star b = b \star a$. **Anti-commutative** if $a \star b = -(b \star a)$. The cross product is anti-commutative; the wedge product will be too.

^rem-37-1

> [!definition] Definition §37.1: Wedge Product
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

^def-37-1

> [!remark]- Connections
> - Linear-algebra model: for functionals $\varphi, \tau$, $\varphi \wedge \tau(u,w) = \varphi(u)\tau(w) - \varphi(w)\tau(u)$ is an alternating bilinear form ([[§35 Bilinear Forms and Quadratic Forms#^ladr-9-15|LADR 9.15]]); anti-commutativity is the swap rule for alternating forms ([[§36 Alternating Multilinear Forms#^ladr-9-30|LADR 9.30]]).
> - The wedge of $k$ covectors is the alternating part of their tensor product $\varphi_1 \otimes \cdots \otimes \varphi_k$ (an $m$-linear functional, [[§38 Tensor Products#^ladr-9-85|LADR 9.85]], [[§38 Tensor Products#^ladr-9-88b|LADR 9.88b]]).

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

> [!definition] Definition §37.2: Levi-Civita Symbol
> For indices $i_1, i_2, \ldots, i_k \in \{1, 2, \ldots, n\}$, the **Levi-Civita symbol** is:
>
> $$
> \varepsilon_{i_1 i_2 \cdots i_k} = \begin{cases} +1 & \text{if } (i_1, \ldots, i_k) \text{ is an even permutation of } (1, 2, \ldots, k), \\ -1 & \text{if } (i_1, \ldots, i_k) \text{ is an odd permutation of } (1, 2, \ldots, k), \\ 0 & \text{if any index is repeated.} \end{cases}
> $$

^def-37-2

> [!theorem] Proposition §37.1: Wedge Product Equals Levi-Civita Symbol
> For coordinate differentials $dx_i, dx_j$ in $\mathbb{R}^n$:
>
> $$
> dx_i \wedge dx_j = \varepsilon_{ij}\,dx \wedge dy \quad (\text{in } \mathbb{R}^2), \qquad dx_i \wedge dx_j \wedge dx_k = \varepsilon_{ijk}\,dx \wedge dy \wedge dz \quad (\text{in } \mathbb{R}^3).
> $$
>
> More generally, if $(i_1, \ldots, i_k)$ is a rearrangement of $(1, 2, \ldots, k)$ or has a repeated index, then $dx_{i_1} \wedge \cdots \wedge dx_{i_k} = \varepsilon_{i_1 \cdots i_k}\,dx_1 \wedge \cdots \wedge dx_k$. (For other index sets, sorting the indices gives $dx_{i_1} \wedge \cdots \wedge dx_{i_k} = \pm\, dx_{j_1} \wedge \cdots \wedge dx_{j_k}$ with $j_1 < \cdots < j_k$, the sign being that of the sorting permutation.)

^prop-37-1

> [!proof]+ Proof
> Both sides obey the same rules: (i) swapping two adjacent factors/indices negates the value (anti-commutativity of $\wedge$ and the sign rule for $\varepsilon$), and (ii) a repeated factor/index gives zero ($dx_i \wedge dx_i = 0$ and $\varepsilon_{\ldots i \ldots i \ldots} = 0$). Since both sides equal $+1$ on the identity permutation ($dx_1 \wedge \cdots \wedge dx_k$ and $\varepsilon_{12\ldots k} = 1$), they agree everywhere.

^pf-37-1

*Uses:* [[§37 The Algebra of Differential Forms#^def-37-1|Def. §37.1]], [[§37 The Algebra of Differential Forms#^def-37-2|Def. §37.2]], [[§36 Alternating Multilinear Forms#^ladr-9-34|LADR 9.34]]

> [!remark]- Connections
> - The same argument in linear algebra: an alternating form on permuted inputs picks up the sign of the permutation ([[§36 Alternating Multilinear Forms#^ladr-9-35|LADR 9.35]]), which yields the Leibniz formula for the determinant ([[§37 Determinants#^ladr-9-46|LADR 9.46]]).

The wedge product is the Levi-Civita symbol promoted from a numerical table to an algebraic operation.

> [!example] Example §37.1: Computing with Wedge Products
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

^ex-37-1

We can now formalize the computation from [[§36 Introduction to Differential Forms#Why the Algebra Must Be Anti-Commutative|§36]]. The key concept is the *pullback*: the operation that translates a form from ambient coordinates to parameter coordinates so that it can be integrated.

> [!definition] Definition §37.3: Pullback
> Let $\omega$ be a differential form on $\mathbb{R}^n$, expressed in the **ambient coordinates** $x_1, \ldots, x_n$.
>
> Let $\Phi: D \subseteq \mathbb{R}^k \to \mathbb{R}^n$ be a $C^1$ map (a **parametrization**), where $D$ has its own **parameter coordinates** $u_1, \ldots, u_k$. The map $\Phi$ relates the two coordinate systems:
>
> $$
> \Phi(u_1, \ldots, u_k) = \big(x_1(u_1, \ldots, u_k),\; \ldots,\; x_n(u_1, \ldots, u_k)\big).
> $$
>
> The **pullback** $\Phi^{\ast}\omega$ is the form on $D$ obtained by:
> 1. Replacing each ambient differential $dx_i$ with $\displaystyle\sum_{j=1}^k \frac{\partial x_i}{\partial u_j}\,du_j$ (the [[Multivariable Chain Rule|chain rule]]),
> 2. Expanding using the wedge product rules.

^def-37-3

> [!definition] Definition §37.4: Integral of a Form over a Parametrized Set
> Let $\omega$ be a differential form on $\mathbb{R}^n$ and $\Phi: D \subseteq \mathbb{R}^k \to \mathbb{R}^n$ a $C^1$ parametrization, with pullback $\Phi^{\ast}\omega$ ([[§37 The Algebra of Differential Forms#^def-37-3|Definition §37.3]]). The integral of $\omega$ over $\Phi(D)$ is then defined as:
>
> $$
> \int_{\Phi(D)} \omega \;=\; \int_D \Phi^*\omega.
> $$

^def-37-4

![[m452-22-1.svg]]
*The two directions of the pullback story. The parametrization $\Phi$ pushes points forward: $(u,v) \mapsto \mathbf{X}(u,v)$. The pullback $\Phi^{\ast}$ pulls forms backward: a form written in ambient differentials $dx_i$ becomes a form in parameter differentials $du_j$, via $dx_i = \sum_j (x_i)_{u_j}\,du_j$. Integration always happens at the parameter end — $\int_{\Phi(D)}\omega$ is defined as $\int_D \Phi^{\ast}\omega$.*

> [!remark]- Connections
> - The coefficients of $\Phi^*\omega$ are $k \times k$ minors of the Jacobian, i.e. determinants ([[§37 Determinants#^ladr-9-46|LADR 9.46]]); in the top-degree case $k = n$ this is the signed volume factor $\det J$, whose absolute value is the volume distortion ([[§37 Determinants#^ladr-9-61|LADR 9.61]], [[§25 Change of Variables on General Domains#^prop-25-5|Proposition §25.5]]).
> - Pulling back and then applying $d$ is how the classical theorems become one statement: [[Generalized Stokes' Theorem|Theorem §40.1]].
> - On a manifold the same substitution, $dx^i = \sum_j \frac{\partial x^i}{\partial y^j}\,dy^j$, is how covectors change between charts: [[§42 The Cotangent Bundle#^prop-42-2|591 Prop. §42.2]].

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

^rem-37-2

*Chain ([[Polar and spherical coordinates|polar and spherical coordinates]]):* ← [[§35 The Unit Sphere and Spherical Coordinates|Chapter 6]]

**Carrying out the pullback** produces determinants of minors of the Jacobian matrix $J = \big[\frac{\partial x_i}{\partial u_j}\big]$ (which is $n \times k$):

$$
\Phi^*(dx_{i_1} \wedge \cdots \wedge dx_{i_k}) = \det \begin{pmatrix} (x_{i_1})_{u_1} & \cdots & (x_{i_1})_{u_k} \\ \vdots & \ddots & \vdots \\ (x_{i_k})_{u_1} & \cdots & (x_{i_k})_{u_k} \end{pmatrix} du_1 \wedge \cdots \wedge du_k.
$$

That is, the pullback of a coordinate $k$-form extracts the $k \times k$ minor of $J$ corresponding to rows $i_1, \ldots, i_k$. This is not a new result — it is what happens when you carry out steps 1 and 2 of the definition. Each $dx_{i_\ell}$ becomes $\sum_j (x_{i_\ell})_{u_j}\,du_j$; wedging $k$ of these and using anti-commutativity kills all terms with repeated $du_j$; the surviving terms are the Leibniz formula for the determinant ([[§37 Determinants#^ladr-9-46|LADR 9.46]]) (compare the informal $2 \times 2$ computation in [[§36 Introduction to Differential Forms#Why the Algebra Must Be Anti-Commutative|§36]]).

> [!example] Example §37.2: Pullback Along a Curve (Line Integral, §27)
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
> This is the line integral $\int_{\boldsymbol{\gamma}} \mathbf{F} \cdot d\mathbf{r}$ from [[§27 Line Integrals and Green's Theorem#^def-27-2|§27]].

^ex-37-2

> [!example] Example §37.3: Pullback Along a Surface (Flux Integral, §31)
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
> The three parenthesized quantities are the components of $\mathbf{X}_u \times \mathbf{X}_v$, so this is $\iint_D \mathbf{F} \cdot (\mathbf{X}_u \times \mathbf{X}_v)\,du\,dv$ — the flux integral from [[§32 Flux Integrals and the Divergence Theorem in ℝ³#^def-32-1|§32]].

^ex-37-3

> [!example] Example §37.4: Pullback for Change of Variables (§20)
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
> This is the *signed* change of variables formula. The $|J|$ version from [[Change of Variables Formula (multiple integrals)|§15]] takes the absolute value, discarding the orientation ([[§36 Introduction to Differential Forms#Signed, Unsigned, and Signed in Disguise|Category 3]]).

^ex-37-4

> [!remark] Remark: The Cross Product Is the Pullback in Disguise
> In $\mathbb{R}^3$, the three $2 \times 2$ minors of the Jacobian are exactly the three components of the cross product:
>
> $$
> \mathbf{X}_u \times \mathbf{X}_v = \big(\underbrace{y_u z_v - z_u y_v}_{\mathbf{X}^*(dy \wedge dz)}, \;\; \underbrace{z_u x_v - x_u z_v}_{\mathbf{X}^*(dz \wedge dx)}, \;\; \underbrace{x_u y_v - y_u x_v}_{\mathbf{X}^*(dx \wedge dy)}\big).
> $$
>
> The cross product packages the pullbacks of all three coordinate 2-forms into a single vector. This packaging only works in $\mathbb{R}^3$, because $\binom{3}{2} = 3$: the number of independent 2-forms equals the dimension. In $\mathbb{R}^4$ there would be $\binom{4}{2} = 6$ minors — not packageable as a vector. The pullback works in any dimension; the cross product is its $\mathbb{R}^3$ shortcut.

^rem-37-3

> [!remark]- Connections
> - The cross product in components and as a determinant: [[§96 The Cross Product#^def-96-1|Calc Def. §96.1]], [[§96 The Cross Product#^prop-96-1|Calc Prop. §96.1]].

*Continued in [[§38 The Exterior Derivative]]: the exterior derivative, the identity d² = 0, and the known integrals in the language of forms.*
