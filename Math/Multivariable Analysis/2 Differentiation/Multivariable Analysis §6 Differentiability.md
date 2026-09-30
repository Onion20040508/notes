---
type: section
subject: "[[Multivariable Analysis]]"
chapter: 2
section: 6
tags: [multivariable-analysis, math452]
---
← [[Multivariable Analysis §5 Equality of Mixed Partials]] · ↑ [[Multivariable Analysis — 2 Differentiation]] · [[Multivariable Analysis §7 Directional Derivatives]] →

## Motivation: What Should Differentiability Mean?

In single-variable calculus, $f: \mathbb{R} \to \mathbb{R}$ is [[Single Variable Analysis §28 Basic Properties of the Derivative#^def-28-1|differentiable]] at $x_0$ if there exists a **[[Linear Algebra 3A Vector Space of Linear Maps#^ladr-3-1|linear map]]** $L: \mathbb{R} \to \mathbb{R}$ such that

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
> The problem is that partial derivatives only measure change along the coordinate axes. Consider $f(x,y) = \frac{2xy}{x^2 + y^2}$ for $(x,y) \neq (0,0)$ and $f(0,0) = 0$. We have $f_x(0,0) = f_y(0,0) = 0$ ([[Multivariable Analysis §4 Partial Derivatives#^ex-4-1|Ex. §4.1]]), so the “linear approximation” would be $L(h,k) = 0$.
>
> But along $y = x$: $f(h, h) = 1 \neq 0$. The linear approximation is terrible in this direction!
>
> The issue: partials exist, but they don't fit together into a coherent linear approximation for all directions.

^rem-6-1

> [!remark] Remark: The $o(\rho)$ Condition
> The condition $E(h,k) = o(\rho)$ ([[Multivariable Analysis §3 Continuity and Limits of Functions#^def-3-3|Def. §3.3]]) means:
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
> By [[Multivariable Analysis §4 Partial Derivatives#^def-4-1|definition of partial derivative]], this limit equals $f_x(x_0, y_0)$. Hence $A = f_x(x_0, y_0)$.
>
> Similarly, setting $h = 0$ shows $B = f_y(x_0, y_0)$.

^pf-def-6-1

*Uses:* [[Multivariable Analysis §4 Partial Derivatives#^def-4-1|Def. §4.1]], [[Multivariable Analysis §3 Continuity and Limits of Functions#^def-3-3|Def. §3.3]]

> [!remark]- Connections
> - MATH 451 version: [[Single Variable Analysis §28 Basic Properties of the Derivative#^def-28-1|The Derivative]]; for maps $\mathbb{R}^n \to \mathbb{R}^m$ the derivative becomes the [[Multivariable Analysis §13 The Inverse Function Theorem#^def-13-1|Jacobian matrix]] of §13, and in §22 it is the 1-form $df$ ([[Multivariable Analysis §22 The Algebra of Differential Forms#^prop-22-6|§22.6]]).

> [!definition] Definition §6.2: The Total Derivative and the Jacobian Matrix
> Let $f: \mathbb{R}^2 \to \mathbb{R}$ be differentiable at $(x_0, y_0)$. The **(total) derivative** of $f$ at $(x_0, y_0)$ is not a number — it is the [[Linear Algebra 3A Vector Space of Linear Maps#^ladr-3-1|linear map]]
>
> $$
> Df_{(x_0, y_0)}: \mathbb{R}^2 \to \mathbb{R}, \quad (h, k) \mapsto f_x(x_0, y_0) \cdot h + f_y(x_0, y_0) \cdot k.
> $$
>
> Its [[Linear Algebra 3C Matrices#^ladr-3-31|matrix in the standard basis]] is the **Jacobian matrix**:
>
> $$
> Df_{(x_0, y_0)} = \begin{pmatrix} f_x & f_y \end{pmatrix}, \quad Df_{(x_0,y_0)} \begin{pmatrix} h \\ k \end{pmatrix} = f_x \cdot h + f_y \cdot k.
> $$

^def-6-2

> [!remark]- Connections
> - A linear map $\mathbb{R}^2 \to \mathbb{R}$ is a [[Linear Algebra 3F Duality#^ladr-3-108|linear functional]] (LADR 3.108), so $Df$ lives in the dual space; this is the viewpoint of the 1-form $df$ in [[Multivariable Analysis §22 The Algebra of Differential Forms#^prop-22-6|Gradient = Differential = 1-Form]].
> - Jacobians of compositions multiply: [[Multivariable Analysis §10 Composition of Functions and the Chain Rule#^rem-10-4|Chain Rule for Jacobians]], i.e. [[Linear Algebra 3C Matrices#^ladr-3-43|Matrix of product of linear maps]] (LADR 3.43).

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

> [!theorem] Theorem §6.1: Differentiability Implies All Directional Derivatives
> If $f$ is differentiable at $(x_0, y_0)$ with derivative $L = Df_{(x_0,y_0)}$, then for every unit direction $\mathbf{u} = (a, b)$ the [[Multivariable Analysis §7 Directional Derivatives#^def-7-1|directional derivative]] exists and
>
> $$
> D_{\mathbf{u}} f(x_0, y_0) = L(a, b) = f_x(x_0,y_0) \cdot a + f_y(x_0,y_0) \cdot b.
> $$

^thm-6-1

> [!proof]+ Proof
> Apply the [[Multivariable Analysis §6 Differentiability#^def-6-1|definition of differentiability]] with the increment $(h, k) = (ta, tb)$:
>
> $$
> f(x_0 + ta,\, y_0 + tb) - f(x_0, y_0) = L(ta, tb) + E(ta, tb) = t \cdot L(a, b) + E(ta, tb),
> $$
>
> using [[Linear Algebra 3A Vector Space of Linear Maps#^ladr-3-1|linearity]] of $L$. Here $\rho = \sqrt{(ta)^2 + (tb)^2} = |t|\sqrt{a^2 + b^2} = |t|$, since $\mathbf{u}$ is a unit vector. Dividing by $t \neq 0$:
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

*Uses:* [[Multivariable Analysis §6 Differentiability#^def-6-1|Def. §6.1]], [[Multivariable Analysis §6 Differentiability#^def-6-2|Def. §6.2]], [[Multivariable Analysis §3 Continuity and Limits of Functions#^def-3-3|Def. §3.3]], [[Multivariable Analysis §7 Directional Derivatives#^def-7-1|Def. §7.1]], [[Linear Algebra 3A Vector Space of Linear Maps#^ladr-3-1|LADR 3.1]]

> [!remark]- Connections
> - Restated with the gradient in §7: [[Directional Derivative Formula|Directional Derivative Formula]].

> [!remark] Remark: Warning: The Converse Is False
> All directional derivatives can exist without $f$ being differentiable — they might not “fit together” into a single linear map. The function $f(x,y) = \frac{2xy}{x^2+y^2}$ from [[Multivariable Analysis §6 Differentiability#^rem-6-1|the motivation]] is one witness: both partials exist at the origin, yet no linear approximation works along $y = x$.

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

> [!theorem] Theorem §6.2: Continuous Partials Imply Differentiability
> Let $R$ be an open set. If $f_x$ and $f_y$ exist and are continuous on $R$, then $f$ is differentiable at every point of $R$.

^thm-6-2

> [!proof]+ Proof
> Let $(x_0, y_0) \in R$. Since $R$ is [[Multivariable Analysis §2 Open and Closed Sets#^def-2-4|open]], there exists $r > 0$ such that $B((x_0, y_0), r) \subseteq R$.
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
> By [[Multivariable Analysis §3 Continuity and Limits of Functions#^def-3-1|continuity]] of $f_x$ at $(x_0, y_0)$:
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
> Hence $f$ is [[Multivariable Analysis §6 Differentiability#^def-6-1|differentiable]] at $(x_0, y_0)$.

^pf-6-2

*Uses:* [[Multivariable Analysis §2 Open and Closed Sets#^def-2-4|Def. §2.4]], [[Multivariable Analysis §4 Partial Derivatives#^def-4-1|Def. §4.1]], [[Multivariable Analysis §3 Continuity and Limits of Functions#^def-3-1|Def. §3.1]], [[Multivariable Analysis §3 Continuity and Limits of Functions#^def-3-3|Def. §3.3]], [[Multivariable Analysis §6 Differentiability#^def-6-1|Def. §6.1]], [[Single Variable Analysis §3 The Set ℝ of Real Numbers#^thm-3-3|451 §3.3]], [[Mean Value Theorem|451 §29.3]]

![[m452-6-2.svg]]
*The same L-shaped path as in [[Multivariable Analysis §4 Partial Derivatives#^thm-4-1|§4.1]]: the two MVTs trade the increments of $f$ along the legs $h$ and $k$ (blue) for $h \cdot f_x(x_0+\alpha(h)h,\,y_0)$ and $k \cdot f_y(x_0+h,\,y_0+\theta(h,k)k)$, evaluated at the red points. Now the point is where those red points go: as $(h,k) \to (0,0)$ the path shrinks (faded copy) and drags them to $(x_0,y_0)$, so continuity of $f_x$ and $f_y$ makes both brackets in $E(h,k)/\rho$ tend to $0$.*

## Algebra of Partial Derivatives

> [!theorem] Theorem §6.3: Partial Derivatives of Sum and Difference
> If $f_x, f_y, g_x, g_y$ exist at $(x_0, y_0)$, then $(f \pm g)_x$ and $(f \pm g)_y$ exist at $(x_0, y_0)$ and:
>
> $$
> (f \pm g)_x = f_x \pm g_x, \qquad (f \pm g)_y = f_y \pm g_y.
> $$

^thm-6-3

> [!proof]+ Proof
> By [[Multivariable Analysis §4 Partial Derivatives#^def-4-1|definition]]:
>
> $$
> \begin{aligned}
> (f + g)_x(x_0, y_0) &= \lim_{h \to 0} \frac{(f + g)(x_0 + h, y_0) - (f + g)(x_0, y_0)}{h} \\
> &= \lim_{h \to 0} \frac{f(x_0 + h, y_0) - f(x_0, y_0)}{h} + \lim_{h \to 0} \frac{g(x_0 + h, y_0) - g(x_0, y_0)}{h} \\
> &= f_x(x_0, y_0) + g_x(x_0, y_0).
> \end{aligned}
> $$
>
> The proofs for $(f + g)_y$, $(f - g)_x$, and $(f - g)_y$ are identical.

^pf-6-3

*Uses:* [[Multivariable Analysis §4 Partial Derivatives#^def-4-1|Def. §4.1]], [[Single Variable Analysis §20 Limits of Functions#^rem-20-2|451 §20 (limit laws)]]

> [!theorem] Theorem §6.4: Product Rule for Partial Derivatives
> If $f_x, f_y, g_x, g_y$ exist at $(x_0, y_0)$, then $(fg)_x$ and $(fg)_y$ exist at $(x_0, y_0)$ and:
>
> $$
> (fg)_x = f_x g + f g_x, \qquad (fg)_y = f_y g + f g_y.
> $$

^thm-6-4

> [!proof]+ Proof
> We compute:
>
> $$
> (fg)_x(x_0, y_0) = \lim_{h \to 0} \frac{f(x_0 + h, y_0) g(x_0 + h, y_0) - f(x_0, y_0) g(x_0, y_0)}{h}.
> $$
>
> Add and subtract $f(x_0 + h, y_0) g(x_0, y_0)$:
>
> $$
> \begin{aligned}
> &= \lim_{h \to 0} \frac{f(x_0 + h, y_0) [g(x_0 + h, y_0) - g(x_0, y_0)] + g(x_0, y_0) [f(x_0 + h, y_0) - f(x_0, y_0)]}{h} \\
> &= \lim_{h \to 0} f(x_0 + h, y_0) \cdot \frac{g(x_0 + h, y_0) - g(x_0, y_0)}{h} + g(x_0, y_0) \cdot \lim_{h \to 0} \frac{f(x_0 + h, y_0) - f(x_0, y_0)}{h}.
> \end{aligned}
> $$
>
> Since $f_x$ exists, $f$ is continuous in $x$ at $(x_0, y_0)$ ([[Single Variable Analysis §28 Basic Properties of the Derivative#^thm-28-1|451 §28.1]]), so $\lim_{h \to 0} f(x_0 + h, y_0) = f(x_0, y_0)$. Thus:
>
> $$
> (fg)_x(x_0, y_0) = f(x_0, y_0) \cdot g_x(x_0, y_0) + g(x_0, y_0) \cdot f_x(x_0, y_0).
> $$
>
> The proof for $(fg)_y$ is identical.

^pf-6-4

*Uses:* [[Multivariable Analysis §4 Partial Derivatives#^def-4-1|Def. §4.1]], [[Single Variable Analysis §28 Basic Properties of the Derivative#^thm-28-1|451 §28.1]], [[Single Variable Analysis §20 Limits of Functions#^rem-20-2|451 §20 (limit laws)]]

> [!theorem] Theorem §6.5: Quotient Rule for Partial Derivatives
> If $f_x, f_y, g_x, g_y$ exist at $(x_0, y_0)$ and $g(x_0, y_0) \neq 0$, then $(f/g)_x$ and $(f/g)_y$ exist at $(x_0, y_0)$ and:
>
> $$
> \left(\frac{f}{g}\right)_x = \frac{f_x g - f g_x}{g^2}, \qquad \left(\frac{f}{g}\right)_y = \frac{f_y g - f g_y}{g^2}.
> $$

^thm-6-5

> [!proof]+ Proof
> First, we show $(1/g)_x = -g_x / g^2$. We have:
>
> $$
> \begin{aligned}
> \left(\frac{1}{g}\right)_x(x_0, y_0) &= \lim_{h \to 0} \frac{\frac{1}{g(x_0 + h, y_0)} - \frac{1}{g(x_0, y_0)}}{h} \\
> &= \lim_{h \to 0} \frac{g(x_0, y_0) - g(x_0 + h, y_0)}{h \cdot g(x_0 + h, y_0) \cdot g(x_0, y_0)} \\
> &= \frac{-g_x(x_0, y_0)}{g(x_0, y_0)^2}.
> \end{aligned}
> $$
>
> (We used continuity of $g$ in $x$, which follows from existence of $g_x$ ([[Single Variable Analysis §28 Basic Properties of the Derivative#^thm-28-1|451 §28.1]]).)
>
> Now apply the [[Multivariable Analysis §6 Differentiability#^thm-6-4|product rule]] to $f \cdot (1/g)$:
>
> $$
> \left(\frac{f}{g}\right)_x = f_x \cdot \frac{1}{g} + f \cdot \left(-\frac{g_x}{g^2}\right) = \frac{f_x}{g} - \frac{f g_x}{g^2} = \frac{f_x g - f g_x}{g^2}.
> $$
>
> The proof for $(f/g)_y$ is identical.

^pf-6-5

*Uses:* [[Multivariable Analysis §4 Partial Derivatives#^def-4-1|Def. §4.1]], [[Multivariable Analysis §6 Differentiability#^thm-6-4|§6.4]], [[Single Variable Analysis §28 Basic Properties of the Derivative#^thm-28-1|451 §28.1]], [[Single Variable Analysis §20 Limits of Functions#^rem-20-2|451 §20 (limit laws)]]

> [!remark]- Connections
> - Each partial is a one-variable derivative, so §6.3–§6.5 are the MATH 451 [[Single Variable Analysis §28 Basic Properties of the Derivative#^thm-28-2|Arithmetic of Derivatives]] applied to slices.

## Algebra of Differentiable Functions

> [!theorem] Theorem §6.6: Sum and Difference of Differentiable Functions
> If $f$ and $g$ are differentiable at $(x_0, y_0)$, then $f + g$ and $f - g$ are differentiable at $(x_0, y_0)$.

^thm-6-6

> [!proof]+ Proof
> Since $f$ is differentiable at $(x_0, y_0)$:
>
> $$
> f(x_0 + h, y_0 + k) - f(x_0, y_0) = f_x(x_0, y_0) h + f_y(x_0, y_0) k + o(\rho).
> $$
>
> Since $g$ is differentiable at $(x_0, y_0)$:
>
> $$
> g(x_0 + h, y_0 + k) - g(x_0, y_0) = g_x(x_0, y_0) h + g_y(x_0, y_0) k + o(\rho).
> $$
>
> Adding these:
>
> $$
> (f + g)(x_0 + h, y_0 + k) - (f + g)(x_0, y_0) = (f_x + g_x) h + (f_y + g_y) k + o(\rho).
> $$
>
> This is exactly the [[Multivariable Analysis §6 Differentiability#^def-6-1|definition of differentiability]] for $f + g$, with partial derivatives $f_x + g_x$ and $f_y + g_y$.

^pf-6-6

*Uses:* [[Multivariable Analysis §6 Differentiability#^def-6-1|Def. §6.1]], [[Multivariable Analysis §3 Continuity and Limits of Functions#^def-3-3|Def. §3.3]]

> [!theorem] Theorem §6.7: Product of Differentiable Functions
> If $f$ and $g$ are differentiable at $(x_0, y_0)$, then $fg$ is differentiable at $(x_0, y_0)$.

^thm-6-7

> [!proof]+ Proof
> Let $f_0 = f(x_0, y_0)$, $g_0 = g(x_0, y_0)$, and write:
>
> $$
> \begin{aligned}
> f(x_0 + h, y_0 + k) &= f_0 + f_x h + f_y k + o(\rho) =: f_0 + \Delta f, \\
> g(x_0 + h, y_0 + k) &= g_0 + g_x h + g_y k + o(\rho) =: g_0 + \Delta g.
> \end{aligned}
> $$
>
> where $\Delta f = f_x h + f_y k + o(\rho)$ and $\Delta g = g_x h + g_y k + o(\rho)$.
>
> Then:
>
> $$
> \begin{aligned}
> (fg)(x_0 + h, y_0 + k) - (fg)(x_0, y_0) &= (f_0 + \Delta f)(g_0 + \Delta g) - f_0 g_0 \\
> &= f_0 \Delta g + g_0 \Delta f + \Delta f \cdot \Delta g.
> \end{aligned}
> $$
>
> Now:
>
> $$
> \begin{aligned}
> f_0 \Delta g + g_0 \Delta f &= f_0 (g_x h + g_y k) + g_0 (f_x h + f_y k) + o(\rho) \\
> &= (f_0 g_x + g_0 f_x) h + (f_0 g_y + g_0 f_y) k + o(\rho) \\
> &= (fg)_x h + (fg)_y k + o(\rho).
> \end{aligned}
> $$
>
> For the remaining term, note that $|\Delta f| \leq C\rho$ and $|\Delta g| \leq C\rho$ for some constant $C$ (since linear terms plus $o(\rho)$ are $O(\rho)$). Thus:
>
> $$
> |\Delta f \cdot \Delta g| \leq C^2 \rho^2 = o(\rho).
> $$
>
> Therefore:
>
> $$
> (fg)(x_0 + h, y_0 + k) - (fg)(x_0, y_0) = (fg)_x h + (fg)_y k + o(\rho).
> $$
>
> Hence $fg$ is differentiable at $(x_0, y_0)$.

^pf-6-7

*Uses:* [[Multivariable Analysis §6 Differentiability#^def-6-1|Def. §6.1]], [[Multivariable Analysis §3 Continuity and Limits of Functions#^def-3-3|Def. §3.3]], [[Multivariable Analysis §6 Differentiability#^thm-6-4|§6.4]]

> [!theorem] Theorem §6.8: Quotient of Differentiable Functions
> If $f$ and $g$ are differentiable at $(x_0, y_0)$ and $g(x_0, y_0) \neq 0$, then $f/g$ is differentiable at $(x_0, y_0)$.

^thm-6-8

> [!proof]+ Proof
> It suffices to show $1/g$ is differentiable (then apply the [[Multivariable Analysis §6 Differentiability#^thm-6-7|product rule]] to $f \cdot (1/g)$).
>
> Let $g_0 = g(x_0, y_0) \neq 0$. Since $g$ is differentiable:
>
> $$
> g(x_0 + h, y_0 + k) = g_0 + g_x h + g_y k + o(\rho) = g_0(1 + \epsilon),
> $$
>
> where $\epsilon = \frac{g_x h + g_y k + o(\rho)}{g_0} = O(\rho)/g_0$.
>
> For small $\rho$, $|\epsilon| < 1$, so we can use $\frac{1}{1 + \epsilon} = 1 - \epsilon + O(\epsilon^2)$:
>
> $$
> \begin{aligned}
> \frac{1}{g(x_0 + h, y_0 + k)} &= \frac{1}{g_0(1 + \epsilon)} = \frac{1}{g_0}(1 - \epsilon + O(\epsilon^2)) \\
> &= \frac{1}{g_0} - \frac{1}{g_0} \cdot \frac{g_x h + g_y k + o(\rho)}{g_0} + O(\rho^2) \\
> &= \frac{1}{g_0} - \frac{g_x}{g_0^2} h - \frac{g_y}{g_0^2} k + o(\rho).
> \end{aligned}
> $$
>
> Thus:
>
> $$
> \frac{1}{g(x_0 + h, y_0 + k)} - \frac{1}{g(x_0, y_0)} = -\frac{g_x}{g^2} h - \frac{g_y}{g^2} k + o(\rho).
> $$
>
> This shows $1/g$ is differentiable with $(1/g)_x = -g_x/g^2$ and $(1/g)_y = -g_y/g^2$.

^pf-6-8

*Uses:* [[Multivariable Analysis §6 Differentiability#^def-6-1|Def. §6.1]], [[Multivariable Analysis §3 Continuity and Limits of Functions#^def-3-3|Def. §3.3]], [[Multivariable Analysis §6 Differentiability#^thm-6-7|§6.7]], [[Single Variable Analysis §14 Series#^ex-14-4|451 Ex. §14.4]]

> [!theorem] Theorem §6.9: Chain Rule: Composition of Differentiable Functions
> Let $g(x,y) = f(\varphi(x,y), \psi(x,y))$. If $\varphi, \psi$ are differentiable at $(x_0, y_0)$ and $f$ is differentiable at $(\varphi(x_0, y_0), \psi(x_0, y_0))$, then $g$ is differentiable at $(x_0, y_0)$ with:
>
> $$
> g_x = f_\xi \varphi_x + f_\eta \psi_x, \qquad g_y = f_\xi \varphi_y + f_\eta \psi_y.
> $$

^thm-6-9

> [!proof]+ Proof
> Let $(\xi_0, \eta_0) = (\varphi(x_0, y_0), \psi(x_0, y_0))$. Since $\varphi, \psi$ are differentiable at $(x_0, y_0)$:
>
> $$
> \begin{aligned}
> \varphi(x_0 + h, y_0 + k) - \varphi(x_0, y_0) &= \varphi_x h + \varphi_y k + o(\rho) =: \Delta\xi, \\
> \psi(x_0 + h, y_0 + k) - \psi(x_0, y_0) &= \psi_x h + \psi_y k + o(\rho) =: \Delta\eta.
> \end{aligned}
> $$
>
> Note that $|\Delta\xi|, |\Delta\eta| = O(\rho)$, so $\sigma := \sqrt{(\Delta\xi)^2 + (\Delta\eta)^2} = O(\rho)$.
>
> Since $f$ is differentiable at $(\xi_0, \eta_0)$:
>
> $$
> f(\xi_0 + \Delta\xi, \eta_0 + \Delta\eta) - f(\xi_0, \eta_0) = f_\xi \Delta\xi + f_\eta \Delta\eta + o(\sigma).
> $$
>
> Since $\sigma = O(\rho)$, we have $o(\sigma) = o(\rho)$. Substituting:
>
> $$
> \begin{aligned}
> g(x_0 + h, y_0 + k) - g(x_0, y_0) &= f_\xi (\varphi_x h + \varphi_y k + o(\rho)) + f_\eta (\psi_x h + \psi_y k + o(\rho)) + o(\rho) \\
> &= (f_\xi \varphi_x + f_\eta \psi_x) h + (f_\xi \varphi_y + f_\eta \psi_y) k + o(\rho).
> \end{aligned}
> $$
>
> Hence $g$ is differentiable with the stated partial derivatives.

^pf-6-9

*Uses:* [[Multivariable Analysis §6 Differentiability#^def-6-1|Def. §6.1]], [[Multivariable Analysis §3 Continuity and Limits of Functions#^def-3-3|Def. §3.3]]

> [!remark]- Connections
> - MATH 451 version: [[Single Variable Analysis §28 Basic Properties of the Derivative#^thm-28-3|Chain Rule]]; the continuity analogue is [[Multivariable Analysis §3 Continuity and Limits of Functions#^thm-3-4|§3.4]].
> - General form in §10: [[Multivariable Chain Rule|Multivariable Chain Rule]] and its [[Multivariable Analysis §10 Composition of Functions and the Chain Rule#^rem-10-2|matrix form]] (Jacobians multiply, [[Linear Algebra 3C Matrices#^ladr-3-43|LADR 3.43]]).

> [!remark] Remark: Summary: Algebra of Differentiable Functions
> If $f$ and $g$ are differentiable at $(x_0, y_0)$:
>
> | **Function** | **Differentiable?** | **Partial Derivatives** |
> |:---:|:---:|:---:|
> | $f + g$ | Yes | $(f+g)_x = f_x + g_x$, $(f+g)_y = f_y + g_y$ |
> | $f - g$ | Yes | $(f-g)_x = f_x - g_x$, $(f-g)_y = f_y - g_y$ |
> | $fg$ | Yes | $(fg)_x = f_x g + f g_x$, $(fg)_y = f_y g + f g_y$ |
> | $f/g$ | Yes (if $g \neq 0$) | $(f/g)_x = \dfrac{f_x g - f g_x}{g^2}$, $(f/g)_y = \dfrac{f_y g - f g_y}{g^2}$ |
> | $h(f, g)$ | Yes (if $h$ diff.) | [[Multivariable Analysis §6 Differentiability#^thm-6-9\|Chain rule]] |

^rem-6-5
