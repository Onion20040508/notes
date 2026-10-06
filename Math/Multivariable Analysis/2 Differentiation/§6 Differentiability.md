---
type: section
subject: "[[Multivariable Analysis]]"
chapter: 2
section: 6
tags: [multivariable-analysis, math452]
---
← [[§5 Equality of Mixed Partials]] · ↑ [[· 2 Differentiation]] · [[§6a Algebra of Differentiable Functions]] →

## Motivation: What Should Differentiability Mean?

In single-variable calculus, $f: \mathbb{R} \to \mathbb{R}$ is [[§28 Basic Properties of the Derivative#^def-28-1|differentiable]] at $x_0$ if there exists a **[[§7 Vector Space of Linear Maps#^ladr-3-1|linear map]]** $L: \mathbb{R} \to \mathbb{R}$ such that

$$
f(x_0 + h) - f(x_0) = L(h) + o(h).
$$

Since every linear map $\mathbb{R} \to \mathbb{R}$ has the form $L(h) = c \cdot h$ for some constant $c$, this becomes:

$$
f(x_0 + h) - f(x_0) = f'(x_0) \cdot h + o(h).
$$

For multivariable functions $f: \mathbb{R}^2 \to \mathbb{R}$, we use the same idea: $f$ is differentiable at $(x_0, y_0)$ if there exists a **linear map** $L: \mathbb{R}^2 \to \mathbb{R}$ such that

$$
f(x_0 + h, y_0 + k) - f(x_0, y_0) = L(h, k) + o(\rho), \quad \text{where } \rho = \sqrt{h^2 + k^2}.
$$

Every linear map $\mathbb{R}^2 \to \mathbb{R}$ has the form $L(h, k) = A \cdot h + B \cdot k$ for constants $A, B$.

![[m452-6-1.svg]]
*Differentiability means the surface $z = f(x,y)$ has a tangent plane at the point: the graph of the linear map $L(h,k) = f_x h + f_y k$, shifted to the point of tangency. The error between surface and plane is $o(\rho)$ — it vanishes faster than the distance.*

> [!remark] Remark: Why Not Just Require Partials to Exist?
> You might ask: why not define differentiability as “$f_x$ and $f_y$ exist”?
>
> The problem is that partial derivatives only measure change along the coordinate axes. Consider $f(x,y) = \frac{2xy}{x^2 + y^2}$ for $(x,y) \neq (0,0)$ and $f(0,0) = 0$. We have $f_x(0,0) = f_y(0,0) = 0$ ([[§4 Partial Derivatives#^ex-4-1|Ex. §4.1]]), so the “linear approximation” would be $L(h,k) = 0$.
>
> But along $y = x$: $f(h, h) = 1 \neq 0$. The linear approximation is terrible in this direction!
>
> The issue: partials exist, but they don't fit together into a coherent linear approximation for all directions.

^rem-6-1

> [!remark] Remark: The $o(\rho)$ Condition
> The condition $E(h,k) = o(\rho)$ ([[§3 Continuity and Limits of Functions#^def-3-new1|Def. §3.3]]) means:
>
> $$
> \lim_{(h,k) \to (0,0)} \frac{|E(h,k)|}{\sqrt{h^2 + k^2}} = 0.
> $$
>
> Equivalently, the definition of differentiability can be written as:
>
> $$
> \lim_{(h,k) \to (0,0)} \frac{f(x_0 + h, y_0 + k) - f(x_0, y_0) - f_x \cdot h - f_y \cdot k}{\sqrt{h^2 + k^2}} = 0.
> $$
>
> Compare with the single-variable case:
>
> $$
> \lim_{h \to 0} \frac{f(x_0 + h) - f(x_0) - f'(x_0) \cdot h}{h} = 0.
> $$
>
> The structure is identical: (actual change) $-$ (linear approximation), divided by distance.
>
> Dividing by $\rho = \sqrt{h^2 + k^2}$ (rather than $h$ or $k$ alone) ensures the approximation is good **uniformly in all directions**.

^rem-6-2

## Formal Definition

> [!definition] Definition §6.1: Differentiability
> $f : \mathbb{R}^2 \to \mathbb{R}$ is **differentiable** at $(x_0, y_0)$ if there exist constants $A, B$ such that
>
> $$
> f(x_0 + h, y_0 + k) - f(x_0, y_0) = A \cdot h + B \cdot k + o(\sqrt{h^2 + k^2}).
> $$
>
> If $f$ is differentiable, then necessarily $A = f_x(x_0, y_0)$ and $B = f_y(x_0, y_0)$.

^def-6-1

> [!proof]+ Proof that $A = f_x(x_0, y_0)$
> Setting $k = 0$: $f(x_0 + h, y_0) - f(x_0, y_0) = A \cdot h + o(|h|)$, so
>
> $$
> \frac{f(x_0 + h, y_0) - f(x_0, y_0)}{h} = A + \frac{o(|h|)}{h} \to A \quad \text{as } h \to 0.
> $$
>
> By [[§4 Partial Derivatives#^def-4-1|definition of partial derivative]], this limit equals $f_x(x_0, y_0)$. Hence $A = f_x(x_0, y_0)$.
>
> Similarly, setting $h = 0$ shows $B = f_y(x_0, y_0)$.

^pf-def-6-1

*Uses:* [[§4 Partial Derivatives#^def-4-1|Def. §4.1]], [[§3 Continuity and Limits of Functions#^def-3-new1|Def. §3.3]]

> [!remark]- Connections
> - MATH 451 version: [[§28 Basic Properties of the Derivative#^def-28-1|The Derivative]]; for a mapping $(x, y) \mapsto (\varphi, \psi)$ the derivative becomes the [[§13 The Inverse Function Theorem#^def-13-1|Jacobian matrix]] of §13, and in §22 it is the 1-form $df$ ([[§22 The Algebra of Differential Forms#^prop-22-6|§22.6]]).
> - Computational version: [[§93 Tangent Planes and Linear Approximations#^def-93-new1|Calc Def. §93.4]] (increment form, with worked examples).
> - Complex differentiability is this differentiability for (u, v) plus the Cauchy–Riemann equations: [[§21 Cauchy–Riemann Equations#^thm-21-1|342 Thm. §21.1]] (the equations are necessary) and [[§23 Sufficient Conditions for Differentiability#^cor-23-2|342 Cor. §23.2]] (real differentiability plus Cauchy–Riemann gives f′).

> [!definition] Definition §6.2: The Total Derivative
> Let $f: \mathbb{R}^2 \to \mathbb{R}$ be differentiable at $(x_0, y_0)$. The **(total) derivative** of $f$ at $(x_0, y_0)$ is not a number — it is the [[§7 Vector Space of Linear Maps#^ladr-3-1|linear map]]
>
> $$
> Df_{(x_0, y_0)}: \mathbb{R}^2 \to \mathbb{R}, \quad (h, k) \mapsto f_x(x_0, y_0) \cdot h + f_y(x_0, y_0) \cdot k.
> $$

^def-6-2

> [!remark]- Connections
> - A linear map $\mathbb{R}^2 \to \mathbb{R}$ is a [[§12 Duality#^ladr-3-108|linear functional]] (LADR 3.108), so $Df$ lives in the dual space; this is the viewpoint of the 1-form $df$ in [[§22 The Algebra of Differential Forms#^prop-22-6|Gradient = Differential = 1-Form]].
> - Computational version: the linearization $L(x,y) = f(a,b) + f_x(a,b)(x-a) + f_y(a,b)(y-b)$, [[§93 Tangent Planes and Linear Approximations#^def-93-2|Calc Def. §93.2]] (with worked examples).

> [!definition] Definition §6.2: The Jacobian Matrix
> Let $f: \mathbb{R}^2 \to \mathbb{R}$ be differentiable at $(x_0, y_0)$, with total derivative $Df_{(x_0, y_0)}$ ([[§6 Differentiability#^def-6-2|Definition §6.2]]). Its [[§9 Matrices#^ladr-3-31|matrix in the standard basis]] is the **Jacobian matrix**:
>
> $$
> Df_{(x_0, y_0)} = \begin{pmatrix} f_x & f_y \end{pmatrix}, \quad Df_{(x_0,y_0)} \begin{pmatrix} h \\ k \end{pmatrix} = f_x \cdot h + f_y \cdot k.
> $$

^def-6-new1

> [!remark]- Connections
> - Jacobians of compositions multiply: [[§10 Composition of Functions and the Chain Rule#^rem-10-4|Chain Rule for Jacobians]], i.e. [[§9 Matrices#^ladr-3-43|Matrix of product of linear maps]] (LADR 3.43).
> - In 591 the total derivative becomes the coordinate-free differential of a map between vector spaces, [[§21 The Differential of a Map Between Vector Spaces#^def-21-4|591 Def. §21.4]], and the Jacobian is the matrix of the differential of a smooth map between manifolds in coordinate bases, [[§28 The Differential in Coordinates#^thm-28-2|591 Thm. §28.2]].
> - The Jacobian is the standard matrix of the linear map Df: [[§9 The Matrix of a Linear Transformation#^thm-9-1|235 Thm. §9.1]] (its columns are the images of e₁, …, eₙ, with worked examples).

> [!definition] Definition §6.3: Tangent Plane
> Let $f$ be differentiable at $(x_0, y_0)$. The **tangent plane** to the graph of $f$ at $(x_0, y_0, f(x_0, y_0))$ is the plane
>
> $$
> z = f(x_0, y_0) + f_x(x_0, y_0)(x - x_0) + f_y(x_0, y_0)(y - y_0),
> $$
>
> i.e., the graph of the affine map $z = f(x_0, y_0) + L(x - x_0, y - y_0)$, where $L = Df_{(x_0,y_0)}$.

^def-6-3

> [!remark] Remark
> Differentiability means: the tangent plane approximates $f$ well *in all directions* — the error is $o(\rho)$ uniformly, not merely along the axes.

^rem-6-3

> [!remark]- Connections
> - The general statement in 591: the tangent space to the graph of a smooth $G : \mathbb{R}^n \to \mathbb{R}^k$ is the graph of $G'(x_0)$, [[§23 The Geometric Tangent Space#^lem-23-2|591 Lemma §23.2]].

> [!theorem] Theorem §6.1: Differentiability Implies All Directional Derivatives
> If $f$ is differentiable at $(x_0, y_0)$ with derivative $L = Df_{(x_0,y_0)}$, then for every unit direction $\mathbf{u} = (a, b)$ the [[§7 Directional Derivatives#^def-7-1|directional derivative]] (defined in §7, ahead) exists and
>
> $$
> D_{\mathbf{u}} f(x_0, y_0) = L(a, b) = f_x(x_0,y_0) \cdot a + f_y(x_0,y_0) \cdot b.
> $$

^thm-6-1

> [!proof]+ Proof
> Apply the [[§6 Differentiability#^def-6-1|definition of differentiability]] with the increment $(h, k) = (ta, tb)$:
>
> $$
> f(x_0 + ta,\, y_0 + tb) - f(x_0, y_0) = L(ta, tb) + E(ta, tb) = t \cdot L(a, b) + E(ta, tb),
> $$
>
> using [[§7 Vector Space of Linear Maps#^ladr-3-1|linearity]] of $L$. Here $\rho = \sqrt{(ta)^2 + (tb)^2} = |t|\sqrt{a^2 + b^2} = |t|$, since $\mathbf{u}$ is a unit vector. Dividing by $t \neq 0$:
>
> $$
> \frac{f(x_0 + ta, y_0 + tb) - f(x_0, y_0)}{t} = L(a, b) + \frac{E(ta, tb)}{t},
> $$
>
> and
>
> $$
> \left| \frac{E(ta, tb)}{t} \right| = \frac{|E(ta, tb)|}{\rho} \to 0 \quad \text{as } t \to 0,
> $$
>
> by the $o(\rho)$ condition. Hence the limit exists and equals $L(a, b)$.

^pf-6-1

*Uses:* [[§6 Differentiability#^def-6-1|Def. §6.1]], [[§6 Differentiability#^def-6-2|Def. §6.2]], [[§3 Continuity and Limits of Functions#^def-3-new1|Def. §3.3]], [[§7 Directional Derivatives#^def-7-1|Def. §7.1]], [[§7 Vector Space of Linear Maps#^ladr-3-1|LADR 3.1]]

> [!remark]- Connections
> - Restated with the gradient in §7: [[Directional Derivative Formula|Directional Derivative Formula]].
> - The coordinate-free form for smooth maps between vector spaces, $dF_p(v) = \frac{d}{dt}\big|_{t=0} F(p + tv)$: [[§21 The Differential of a Map Between Vector Spaces#^thm-21-3|591 Thm. §21.3]].
> - Computational version: [[§95 Directional Derivatives and the Gradient Vector#^thm-95-1|Calc Thm. §95.1]] and [[§95 Directional Derivatives and the Gradient Vector#^cor-95-2|Calc Cor. §95.2]] (with worked examples).

> [!remark] Remark: Warning: The Converse Is False
> All directional derivatives can exist without $f$ being differentiable — they might not “fit together” into a single linear map. A witness is $f(x,y) = \frac{x^2y}{x^4+y^2}$ for $(x,y) \neq (0,0)$, $f(0,0) = 0$. For a unit vector $\mathbf{u} = (a,b)$ with $b \neq 0$,
>
> $$
> \frac{f(ta,tb) - f(0,0)}{t} = \frac{a^2 b}{t^2a^4 + b^2} \to \frac{a^2}{b} \quad \text{as } t \to 0,
> $$
>
> and for $b = 0$ we have $f(ta, 0) = 0$; so every directional derivative exists at the origin. But along the parabola $y = x^2$, $f(x, x^2) = \tfrac12$ for $x \neq 0$, so $f$ is not continuous at $(0,0)$ — hence not differentiable there, since [[§6 Differentiability#^def-6-1|differentiability]] gives $f(x_0+h, y_0+k) - f(x_0,y_0) = Ah + Bk + o(\rho) \to 0$. (The function $\frac{2xy}{x^2+y^2}$ from [[§6 Differentiability#^rem-6-1|the motivation]] is not a witness: its directional derivatives off the axes do not exist at the origin.)

^rem-6-4

## Summary

| **Concept** | **Meaning** |
|:---|:---|
| $f$ is differentiable at $(x_0, y_0)$ | $\exists$ linear map $L$ s.t. $f(x_0+h, y_0+k) - f(x_0, y_0) = L(h,k) + o(\rho)$ |
| The derivative $Df$ | The linear map $L$ itself (not a number!) |
| Tangent plane | The graph of $f(x_0, y_0) + L(h, k)$ |
| Directional derivative $D_{\mathbf{u}} f$ | $L(\mathbf{u})$ — the derivative evaluated in direction $\mathbf{u}$ |

**Differentiability = existence of a good linear approximation in ALL directions at once.**

> [!example] Example §6.1: Partials Exist but Not Differentiable
> Let $f(x, y) = \dfrac{2xy}{x^2 + y^2}$ for $(x, y) \neq (0, 0)$ and $f(0, 0) = 0$.
>
> We have $f_x(0, 0) = f_y(0, 0) = 0$. If $f$ were differentiable at $(0, 0)$:
>
> $$
> f(h, k) - f(0, 0) = 0 \cdot h + 0 \cdot k + o(\sqrt{h^2 + k^2}).
> $$
>
> But with $h = k$: $f(h, h) = 1 \neq o(\sqrt{2}|h|)$. So $f$ is **not differentiable** at $(0, 0)$.

^ex-6-1

> [!remark]- Connections
> - Same example (xy/(x² + y²)) in Stewart: [[§93 Tangent Planes and Linear Approximations#^rem-93-1|Calc Remark §93.1]].
> - The complex analogue: [[§22 Examples (Cauchy–Riemann Equations)#^ex-22-3|342 Ex. §22.3]] (the Cauchy–Riemann equations hold at 0, yet f′(0) does not exist).

> [!theorem] Theorem §6.2: Continuous Partials Imply Differentiability
> Let $R$ be an open set. If $f_x$ and $f_y$ exist and are continuous on $R$, then $f$ is differentiable at every point of $R$.

^thm-6-2

> [!proof]+ Proof
> Let $(x_0, y_0) \in R$. Since $R$ is [[§2 Open and Closed Sets#^def-2-4|open]], there exists $r > 0$ such that $B((x_0, y_0), r) \subseteq R$.
>
> **Goal:** Show that
>
> $$
> f(x_0 + h, y_0 + k) - f(x_0, y_0) - f_x(x_0, y_0) \cdot h - f_y(x_0, y_0) \cdot k = o(\sqrt{h^2 + k^2})
> $$
>
> as $(h, k) \to (0, 0)$.
>
> For $(h, k)$ with $|(h, k)| < r$, define:
>
> $$
> E(h, k) = f(x_0 + h, y_0 + k) - f(x_0, y_0) - f_x(x_0, y_0) \cdot h - f_y(x_0, y_0) \cdot k.
> $$
>
> We rewrite $E(h, k)$ by adding and subtracting $f(x_0 + h, y_0)$:
>
> $$
> \begin{aligned}
> E(h, k) &= \bigl[f(x_0 + h, y_0 + k) - f(x_0 + h, y_0)\bigr] + \bigl[f(x_0 + h, y_0) - f(x_0, y_0)\bigr] \\
> &\qquad - f_x(x_0, y_0) \cdot h - f_y(x_0, y_0) \cdot k.
> \end{aligned}
> $$
>
> **Second bracket:** Define $g(x) = f(x, y_0)$ for $x \in [x_0, x_0 + h]$. Since $f_x$ exists on $R$, the function $g$ is differentiable with $g'(x) = f_x(x, y_0)$. By [[Mean Value Theorem|MVT]], there exists $\alpha(h) \in [0, 1]$ such that
>
> $$
> f(x_0 + h, y_0) - f(x_0, y_0) = h \cdot f_x(x_0 + \alpha(h) \cdot h, y_0).
> $$
>
> **First bracket:** Define $\psi(y) = f(x_0 + h, y)$ for $y \in [y_0, y_0 + k]$. Since $f_y$ exists on $R$, the function $\psi$ is differentiable with $\psi'(y) = f_y(x_0 + h, y)$. By MVT, there exists $\theta(h, k) \in [0, 1]$ such that
>
> $$
> f(x_0 + h, y_0 + k) - f(x_0 + h, y_0) = k \cdot f_y(x_0 + h, y_0 + \theta(h, k) \cdot k).
> $$
>
> Substituting into $E(h, k)$:
>
> $$
> \begin{aligned}
> E(h, k) &= k \cdot f_y(x_0 + h, y_0 + \theta(h, k) \cdot k) + h \cdot f_x(x_0 + \alpha(h) \cdot h, y_0) - f_x(x_0, y_0) \cdot h - f_y(x_0, y_0) \cdot k \\
> &= \bigl[f_x(x_0 + \alpha(h) \cdot h, y_0) - f_x(x_0, y_0)\bigr] \cdot h + \bigl[f_y(x_0 + h, y_0 + \theta(h, k) \cdot k) - f_y(x_0, y_0)\bigr] \cdot k.
> \end{aligned}
> $$
>
> **Bounding $|E(h, k)|$:** Let $\rho = \sqrt{h^2 + k^2}$. Since $|h| \leq \rho$ and $|k| \leq \rho$:
>
> $$
> |E(h, k)| \leq \bigl|f_x(x_0 + \alpha(h) \cdot h, y_0) - f_x(x_0, y_0)\bigr| \cdot \rho + \bigl|f_y(x_0 + h, y_0 + \theta(h, k) \cdot k) - f_y(x_0, y_0)\bigr| \cdot \rho.
> $$
>
> Thus:
>
> $$
> \frac{|E(h, k)|}{\rho} \leq \bigl|f_x(x_0 + \alpha(h) \cdot h, y_0) - f_x(x_0, y_0)\bigr| + \bigl|f_y(x_0 + h, y_0 + \theta(h, k) \cdot k) - f_y(x_0, y_0)\bigr|.
> $$
>
> **Taking the limit:** As $(h, k) \to (0, 0)$:
> - $(x_0 + \alpha(h) \cdot h, y_0) \to (x_0, y_0)$ since $\alpha(h) \in [0, 1]$ and $h \to 0$
> - $(x_0 + h, y_0 + \theta(h, k) \cdot k) \to (x_0, y_0)$ since $h \to 0$, $\theta(h,k) \in [0, 1]$, and $k \to 0$
>
> By [[§3 Continuity and Limits of Functions#^def-3-1|continuity]] of $f_x$ at $(x_0, y_0)$:
>
> $$
> \bigl|f_x(x_0 + \alpha(h) \cdot h, y_0) - f_x(x_0, y_0)\bigr| \to 0.
> $$
>
> By continuity of $f_y$ at $(x_0, y_0)$:
>
> $$
> \bigl|f_y(x_0 + h, y_0 + \theta(h, k) \cdot k) - f_y(x_0, y_0)\bigr| \to 0.
> $$
>
> Therefore $\dfrac{|E(h, k)|}{\rho} \to 0$ as $(h, k) \to (0, 0)$, which means $E(h, k) = o(\rho)$.
>
> Hence $f$ is [[§6 Differentiability#^def-6-1|differentiable]] at $(x_0, y_0)$.

^pf-6-2

*Uses:* [[§2 Open and Closed Sets#^def-2-4|Def. §2.4]], [[§4 Partial Derivatives#^def-4-1|Def. §4.1]], [[§3 Continuity and Limits of Functions#^def-3-1|Def. §3.1]], [[§3 Continuity and Limits of Functions#^def-3-new1|Def. §3.3]], [[§6 Differentiability#^def-6-1|Def. §6.1]], [[§3 The Set ℝ of Real Numbers#^thm-3-3|451 §3.3]], [[Mean Value Theorem|451 §29.3]]

![[m452-6-2.svg]]
*The same L-shaped path as in [[§4 Partial Derivatives#^thm-4-1|§4.1]]: the two MVTs trade the increments of $f$ along the legs $h$ and $k$ (blue) for $h \cdot f_x(x_0+\alpha(h)h,\,y_0)$ and $k \cdot f_y(x_0+h,\,y_0+\theta(h,k)k)$, evaluated at the red points. Now the point is where those red points go: as $(h,k) \to (0,0)$ the path shrinks (faded copy) and drags them to $(x_0,y_0)$, so continuity of $f_x$ and $f_y$ makes both brackets in $E(h,k)/\rho$ tend to $0$.*

> [!remark]- Connections
> - Computational version: [[§93 Tangent Planes and Linear Approximations#^thm-93-2|Calc Thm. §93.2]] (with worked examples).
> - Computational version: [[§23 Sufficient Conditions for Differentiability#^thm-23-1|342 Thm. §23.1]] (continuous first partials of u and v plus the Cauchy–Riemann equations give complex differentiability, with worked examples).

*Continued in [[§6a Algebra of Differentiable Functions]]: the algebra of partial derivatives and of differentiable functions (sums, products, quotients, compositions).*
