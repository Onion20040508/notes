---
type: section
subject: "[[Multivariable Analysis]]"
chapter: 3
section: 16
tags: [multivariable-analysis, math452]
---
← [[§15 The Implicit Function Theorem]] · ↑ [[· 3 Existence Theorems and Applications]] · [[§17 Optimization and Lagrange Multipliers]] →

## Motivation: Inverting Functions

**One dimension:** If $y = h(x)$ and $h'(x_0) \neq 0$, then $h$ is locally invertible near $x_0$, and ([[§29 The Mean Value Theorem#^thm-29-10|451 §29.10]]):

$$
(h^{-1})'(y_0) = \frac{1}{h'(x_0)} = \frac{1}{h'(h^{-1}(y_0))}.
$$

**Two dimensions:** Given a mapping $(x, y) \mapsto (u, v)$ where $u = \varphi(x, y)$ and $v = \psi(x, y)$, when can we invert to get $x = f(u, v)$ and $y = g(u, v)$?

## The Key Question: What Do We Want?

**What we have:** A mapping $(x, y) \mapsto (u, v)$ where $u = \varphi(x,y)$ and $v = \psi(x,y)$.

**What we want:**
1. Does an inverse mapping $(u, v) \mapsto (x, y)$ exist locally?
2. If so, what are the partial derivatives $f_u, f_v, g_u, g_v$ of the inverse?

**The problem:** We generally **cannot write down explicit formulas** for $f$ and $g$!

> [!example] Example §16.1: Why Explicit Inversion is Hard
> Given $u = x^2 - y^2$ and $v = 2xy$, try solving for $x$ and $y$ in terms of $u$ and $v$.
>
> You would need to solve a system of nonlinear equations — very difficult in general!

^ex-16-1

**What the Inverse Function Theorem gives us:**

Even though we can't find $f$ and $g$ explicitly, we get:
1. **Existence:** If $\det(J) \neq 0$, then $f$ and $g$ **exist** locally (even if we can't write them down).
2. **Derivatives:** We can compute the partial derivatives of $f$ and $g$ **without knowing the explicit formulas**:

$$
\begin{pmatrix} f_u & f_v \\ g_u & g_v \end{pmatrix} = \begin{pmatrix} \varphi_x & \varphi_y \\ \psi_x & \psi_y \end{pmatrix}^{-1}.
$$

**Why is this useful?** In many applications, we only need the derivatives, not the explicit inverse:
- In change of variables for integration, we need $|\det(J)|$
- In differential equations, we need how variables transform locally
- In optimization, we need to understand local behavior

## The Jacobian Matrix

> [!definition] Definition §16.1: Jacobian Matrix
> For a mapping $(x, y) \mapsto (\varphi(x,y), \psi(x,y))$, the **Jacobian matrix** is:
>
> $$
> J = \frac{\partial(\varphi, \psi)}{\partial(x, y)} = \begin{pmatrix} \varphi_x & \varphi_y \\ \psi_x & \psi_y \end{pmatrix}.
> $$

^def-16-1

> [!remark]- Connections
> - The same matrix as the total derivative of §7: [[§7 Differentiability#^def-7-3|Def. §7.3]]; Jacobians multiply under composition: [[§12 Composition of Functions and the Chain Rule#^rem-12-4|Chain Rule for Jacobians]].
> - Linear-algebra view: the matrix of the linear map $Df$ in the standard bases, [[§9 Matrices#^ladr-3-31|LADR 3.31]].
> - For an analytic map the Cauchy–Riemann equations make the Jacobian matrix a rotation–scaling matrix with determinant |f′|²: [[§21 Cauchy–Riemann Equations#^thm-21-1|342 Thm. §21.1]] and [[§114★ Local Inverses#^thm-114-1|342 Thm. §114.1]].

**What does the Jacobian do?** It describes how the mapping behaves **locally** near a point. If we make a small displacement $(dx, dy)$ in the input, the output changes by approximately:

$$
\begin{pmatrix} du \\ dv \end{pmatrix} \approx \begin{pmatrix} \varphi_x & \varphi_y \\ \psi_x & \psi_y \end{pmatrix} \begin{pmatrix} dx \\ dy \end{pmatrix} = J \begin{pmatrix} dx \\ dy \end{pmatrix}.
$$

In other words: **the Jacobian is the linear approximation to the mapping near a point**.

![[m452-13-2.svg]]
*The Jacobian as the linear approximation, for $u = x^2 - y^2$, $v = 2xy$ (Example §16.2) at $(x_0, y_0) = (1, \tfrac12)$. The small cell with sides $dx, dy$ (left) is carried to a slightly curved image cell (blue). The columns of $J$, scaled by $dx$ and $dy$ (red arrows), span the parallelogram $J$ makes of the cell (dashed), which hugs the true image better and better as the cell shrinks. Its area is $|\det J|\,dx\,dy$, here $\det J = 4(x_0^2 + y_0^2) = 5$. When $\det J \neq 0$ the parallelogram is not flattened, and $(du, dv)$ determines $(dx, dy)$.*

**When is the mapping invertible?** For the inverse to exist locally, we need to recover $(dx, dy)$ from $(du, dv)$:

$$
\begin{pmatrix} dx \\ dy \end{pmatrix} = J^{-1} \begin{pmatrix} du \\ dv \end{pmatrix}.
$$

This requires $J$ to be an **invertible matrix**, i.e., $\det(J) \neq 0$ ([[Invertible ⟺ nonzero determinant|LADR 9.50]]).

## How to Invert a $2 \times 2$ Matrix

> [!theorem] Proposition §16.1: Inverse of a $2 \times 2$ Matrix
> If $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$ and $\det(A) = ad - bc \neq 0$, then:
>
> $$
> A^{-1} = \frac{1}{ad - bc} \begin{pmatrix} d & -b \\ -c & a \end{pmatrix}.
> $$

^prop-16-1

> [!proof]+ Proof
> Direct verification:
>
> $$
> \begin{pmatrix} a & b \\ c & d \end{pmatrix} \cdot \frac{1}{ad-bc} \begin{pmatrix} d & -b \\ -c & a \end{pmatrix} = \frac{1}{ad-bc} \begin{pmatrix} ad - bc & 0 \\ 0 & ad - bc \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}.
> $$
>
> and in the other order
>
> $$
> \frac{1}{ad-bc} \begin{pmatrix} d & -b \\ -c & a \end{pmatrix} \cdot \begin{pmatrix} a & b \\ c & d \end{pmatrix} = \frac{1}{ad-bc} \begin{pmatrix} da - bc & db - bd \\ -ca + ac & -cb + ad \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}.
> $$

^pf-16-1

*Uses:* [[§9 Matrices#^ladr-3-41|LADR 3.41]], [[§10 Invertibility and Isomorphisms#^ladr-3-80|LADR 3.80]]

> [!remark]- Connections
> - The general statement behind it: a square matrix is invertible exactly when its determinant is nonzero, [[Invertible ⟺ nonzero determinant|LADR 9.50]].

> [!remark] Remark: Recipe for $2 \times 2$ Inverse
> To invert $\begin{pmatrix} a & b \\ c & d \end{pmatrix}$:
> 1. Swap the diagonal entries: $a \leftrightarrow d$
> 2. Negate the off-diagonal entries: $b \to -b$, $c \to -c$
> 3. Divide by the determinant $ad - bc$

^rem-16-1

**Applying to the Jacobian:**

$$
\begin{pmatrix} \varphi_x & \varphi_y \\ \psi_x & \psi_y \end{pmatrix}^{-1} = \frac{1}{\varphi_x \psi_y - \varphi_y \psi_x} \begin{pmatrix} \psi_y & -\varphi_y \\ -\psi_x & \varphi_x \end{pmatrix}.
$$

## Statement of the Theorem

> [!theorem] Theorem §16.2: Inverse Function Theorem
> Let $\varphi, \psi : \mathbb{R}^2 \to \mathbb{R}$ have continuous partial derivatives in a neighborhood of $(x_0, y_0)$. Define the Jacobian:
>
> $$
> J = \begin{pmatrix} \varphi_x & \varphi_y \\ \psi_x & \psi_y \end{pmatrix}.
> $$
>
> If $\det(J) \neq 0$ at $(x_0, y_0)$, then the mapping $(x, y) \mapsto (\varphi(x,y), \psi(x,y))$ is locally invertible near $(x_0, y_0)$.
>
> That is, there exist functions $f, g$ such that locally:
>
> $$
> x = f(\varphi(x,y), \psi(x,y)), \qquad y = g(\varphi(x,y), \psi(x,y)),
> $$
>
> and the Jacobian of the inverse is:
>
> $$
> \begin{pmatrix} f_u & f_v \\ g_u & g_v \end{pmatrix} = J^{-1} = \frac{1}{\det(J)} \begin{pmatrix} \psi_y & -\varphi_y \\ -\psi_x & \varphi_x \end{pmatrix}.
> $$

^thm-16-2

> [!proof]+ Proof via the Implicit Function Theorem
> The strategy is to apply the [[§15 The Implicit Function Theorem#^thm-15-2|Implicit Function Theorem]] **twice** to “peel off” the variables one at a time: first solve for $x$, then solve for $y$.
>
> **Setup and notation.** We have $u = \varphi(x,y)$ and $v = \psi(x,y)$, and we want to solve for $x$ and $y$ in terms of $u$ and $v$.
>
> The key difficulty: in the equation $\varphi(x,y) = u$, the variable $u$ **depends on** $(x,y)$. We cannot directly apply IFT because we need the “target” to be an independent parameter. To fix this, introduce **free parameters** $\tilde{u}, \tilde{v}$ that are independent of everything, and solve:
>
> $$
> F(x, y, \tilde{u}) \equiv \varphi(x, y) - \tilde{u} = 0, \qquad G(x, y, \tilde{v}) \equiv \psi(x, y) - \tilde{v} = 0.
> $$
>
> Define $u_0 = \varphi(x_0, y_0)$ and $v_0 = \psi(x_0, y_0)$. Then $F(x_0, y_0, u_0) = 0$ and $G(x_0, y_0, v_0) = 0$.
>
> **Variable dependence at start:** $x, y, \tilde{u}, \tilde{v}$ are all independent.
>
> **Step 1: Solve $F = 0$ for $x$.**
>
> WLOG assume $\varphi_x(x_0, y_0) \neq 0$. (Since $\det(J) = \varphi_x \psi_y - \varphi_y \psi_x \neq 0$, at least one of $\varphi_x, \psi_x$ is nonzero; if $\varphi_x = 0$, relabel.)
>
> We have:
>
> $$
> F(x, y, \tilde{u}) = \varphi(x, y) - \tilde{u} = 0, \qquad F_x = \varphi_x \neq 0.
> $$
>
> By the [[§15 The Implicit Function Theorem#^thm-15-2|Implicit Function Theorem]] (applied to $F = 0$, solving for $x$ in terms of $y, \tilde{u}$):
>
> There exists a function $x = X(y, \tilde{u})$ defined near $(y_0, u_0)$ such that:
> - (i) $X(y_0, u_0) = x_0$
> - (ii) $F(X(y, \tilde{u}), y, \tilde{u}) = 0$, i.e., $\varphi(X(y, \tilde{u}), y) = \tilde{u}$
> - (iii) $X_y = -\dfrac{F_y}{F_x} = -\dfrac{\varphi_y(X(y,\tilde{u}), y)}{\varphi_x(X(y,\tilde{u}), y)}$
>
> **Variable dependence after Step 1:** $y, \tilde{u}, \tilde{v}$ are independent; $x = X(y, \tilde{u})$ depends on $y, \tilde{u}$.
>
> **Step 2: Substitute into $G = 0$ and solve for $y$.**
>
> Plug $x = X(y, \tilde{u})$ into the second equation:
>
> $$
> H(y, \tilde{u}, \tilde{v}) \equiv G(X(y, \tilde{u}), y, \tilde{v}) = \psi(X(y, \tilde{u}), y) - \tilde{v} = 0.
> $$
>
> We need $H_y \neq 0$ to apply IFT. Compute using the [[Multivariable Chain Rule|chain rule]]:
>
> $$
> \begin{aligned}
> H_y &= \psi_x(X(y,\tilde{u}), y) \cdot X_y(y, \tilde{u}) + \psi_y(X(y,\tilde{u}), y) \\[4pt]
> &= \psi_x \cdot \left( -\frac{\varphi_y}{\varphi_x} \right) + \psi_y \\[4pt]
> &= \frac{-\psi_x \varphi_y + \psi_y \varphi_x}{\varphi_x} \\[4pt]
> &= \frac{1}{\varphi_x} \begin{vmatrix} \varphi_x & \varphi_y \\ \psi_x & \psi_y \end{vmatrix} = \frac{\det(J)}{\varphi_x}.
> \end{aligned}
> $$
>
> Since $\det(J) \neq 0$ and $\varphi_x \neq 0$, we have $H_y \neq 0$. Also $H(y_0, u_0, v_0) = G(x_0, y_0, v_0) = 0$.
>
> By the Implicit Function Theorem (applied to $H = 0$, solving for $y$ in terms of $\tilde{u}, \tilde{v}$):
>
> There exists a function $y = Y(\tilde{u}, \tilde{v})$ defined near $(u_0, v_0)$ such that:
> - (i) $Y(u_0, v_0) = y_0$
> - (ii) $H(Y(\tilde{u}, \tilde{v}), \tilde{u}, \tilde{v}) = 0$, i.e., $\psi(X(Y(\tilde{u},\tilde{v}), \tilde{u}), Y(\tilde{u}, \tilde{v})) = \tilde{v}$
>
> **Variable dependence after Step 2:** $\tilde{u}, \tilde{v}$ are independent; $y = Y(\tilde{u}, \tilde{v})$ and $x = X(Y(\tilde{u}, \tilde{v}), \tilde{u})$ both depend on $\tilde{u}, \tilde{v}$.
>
> **Step 3: Define the inverse functions.**
>
> Set:
>
> $$
> f(\tilde{u}, \tilde{v}) \equiv X(Y(\tilde{u}, \tilde{v}), \tilde{u}), \qquad g(\tilde{u}, \tilde{v}) \equiv Y(\tilde{u}, \tilde{v}).
> $$
>
> **Variable dependence at end:** $\tilde{u}, \tilde{v}$ are independent; $x = f(\tilde{u}, \tilde{v})$ and $y = g(\tilde{u}, \tilde{v})$ depend on them. The roles of $(x,y)$ and $(u,v)$ are now **reversed**.
>
> **Step 4: Verify the inverse property.**
>
> From Step 1: $\varphi(X(y, \tilde{u}), y) = \tilde{u}$ for all $(y, \tilde{u})$ near $(y_0, u_0)$.
>
> Setting $y = Y(\tilde{u}, \tilde{v}) = g(\tilde{u}, \tilde{v})$ and $X(Y(\tilde{u}, \tilde{v}), \tilde{u}) = f(\tilde{u}, \tilde{v})$:
>
> $$
> \varphi(f(\tilde{u}, \tilde{v}), g(\tilde{u}, \tilde{v})) = \tilde{u}. \quad \checkmark
> $$
>
> From Step 2: $\psi(X(Y(\tilde{u}, \tilde{v}), \tilde{u}), Y(\tilde{u}, \tilde{v})) = \tilde{v}$, i.e.:
>
> $$
> \psi(f(\tilde{u}, \tilde{v}), g(\tilde{u}, \tilde{v})) = \tilde{v}. \quad \checkmark
> $$
>
> Since $\tilde{u}, \tilde{v}$ were free parameters playing the role of $u, v$, we drop the tildes: $(\varphi, \psi) \circ (f, g)$ is the identity near $(u_0, v_0)$.
>
> **Step 5: The inverse on the other side.** The theorem asserts $x = f(\varphi(x,y), \psi(x,y))$ and $y = g(\varphi(x,y), \psi(x,y))$, which needs the uniqueness part of [[§15 The Implicit Function Theorem#^thm-15-2|Theorem §15.2]] (a). By it there are $\eta_1, \eta_2 > 0$ such that $X(y, \tilde{u})$ is the only solution $x$ of $\varphi(x, y) = \tilde{u}$ with $|x - x_0| < \eta_1$ (for $(y, \tilde{u})$ near $(y_0, u_0)$), and $Y(\tilde{u}, \tilde{v})$ is the only solution $y$ of $H(y, \tilde{u}, \tilde{v}) = 0$ with $|y - y_0| < \eta_2$ (for $(\tilde{u}, \tilde{v})$ near $(u_0, v_0)$). Let $(x, y)$ be close to $(x_0, y_0)$ and put $u = \varphi(x, y)$, $v = \psi(x, y)$; since $\varphi$ and $\psi$ are continuous, $(u, v)$ is close to $(u_0, v_0)$. Since $\varphi(x, y) = u$ and $|x - x_0| < \eta_1$, uniqueness in Step 1 gives $x = X(y, u)$. Then $H(y, u, v) = \psi(X(y, u), y) - v = \psi(x, y) - v = 0$ with $|y - y_0| < \eta_2$, so uniqueness in Step 2 gives $y = Y(u, v) = g(u, v)$, and then $x = X(g(u, v), u) = f(u, v)$. So $(f, g) \circ (\varphi, \psi)$ is the identity near $(x_0, y_0)$, and $f, g$ are the desired inverse functions. They are continuously differentiable because $X$ and $Y$ are ([[§15 The Implicit Function Theorem#^thm-15-2|Theorem §15.2]] (b)) and by the [[Multivariable Chain Rule|chain rule]]; the formula for their Jacobian then follows from $(f, g) \circ (\varphi, \psi) = \mathrm{id}$ as in the [[§16 The Inverse Function Theorem#Derivation via Chain Rule|derivation below]].

^pf-16-2

*Uses:* [[§15 The Implicit Function Theorem#^thm-15-2|§15.2]], [[Multivariable Chain Rule|§12.2]], [[§16 The Inverse Function Theorem#^def-16-1|Def. §16.1]]

> [!remark]- Connections
> - The 1D version in MATH 451: [[§29 The Mean Value Theorem#^thm-29-10|Inverse Function Theorem]] (451 §29.10), where the condition is $f'(x_0) \neq 0$.
> - The linear-algebra fact behind the hypothesis: [[Invertible ⟺ nonzero determinant|LADR 9.50]], and [[§10 Invertibility and Isomorphisms#^ladr-3-86|matrix of inverse equals inverse of matrix]] (LADR 3.86) behind the formula for the inverse's Jacobian.
> - The Jacobian determinant returns as the area factor in the [[§24 The Change of Variables Formula#^thm-24-2|change of variables formula]] (§15.14, §15.20).
> - The n-variable theorem, of which this is the case n = 2, is quoted in 591 as [[§33 Local Diffeomorphisms#^thm-33-1|591 Thm. §33.1]]; on manifolds it becomes the criterion that a map is a local diffeomorphism exactly where its differential is bijective, [[§33 Local Diffeomorphisms#^thm-33-2|591 Thm. §33.2]].
> - Complex counterpart: [[§114★ Local Inverses#^thm-114-1|342 Thm. §114.1]] (an analytic f with f′(z₀) ≠ 0 has an analytic local inverse; the Jacobian is |f′|²).

> [!remark] Remark: Tracking Variable Dependencies
> The proof works by progressively “solving away” the original variables:
>
> | **Stage** | **Independent variables** | **Dependent variables** |
> |:---:|---|---|
> | Start | $x, y, \tilde{u}, \tilde{v}$ | — |
> | After Step 1 | $y, \tilde{u}, \tilde{v}$ | $x = X(y, \tilde{u})$ |
> | After Step 2 | $\tilde{u}, \tilde{v}$ | $y = Y(\tilde{u}, \tilde{v})$, $x = X(Y(\tilde{u},\tilde{v}), \tilde{u})$ |

^rem-16-2

> [!remark] Remark: Why $\tilde{u}, \tilde{v}$ Are Needed
> In the original setup, $u = \varphi(x,y)$ depends on $(x,y)$. The Implicit Function Theorem requires solving an equation like $\varphi(x,y) = c$ where $c$ is a **free parameter** independent of the variables being solved for. By introducing $\tilde{u}$ as an independent copy of $u$, we create a legitimate IFT setup. At the end, the inverse satisfies $\varphi(f(u,v), g(u,v)) = u$, so setting $\tilde{u} = u$ is justified.

^rem-16-3

> [!remark] Remark: Tracking IFT Hypotheses
> | **Step** | **Equation** | **Solve for** | **IFT condition** | **Why satisfied** |
> |:---:|---|---|---|---|
> | 1 | $\varphi(x,y) - \tilde{u} = 0$ | $x = X(y, \tilde{u})$ | $F_x = \varphi_x \neq 0$ | WLOG |
> | 2 | $\psi(X(y,\tilde{u}),y) - \tilde{v} = 0$ | $y = Y(\tilde{u}, \tilde{v})$ | $H_y = \dfrac{\det J}{\varphi_x} \neq 0$ | $\det J \neq 0$, $\varphi_x \neq 0$ |

^rem-16-4

> [!remark] Remark: Comparison: 1D vs 2D
> | | **1D** | **2D** |
> |:---:|:---:|:---:|
> | Forward | $u = \varphi(x)$ | $(u, v) = (\varphi(x,y), \psi(x,y))$ |
> | Inverse | $x = \varphi^{-1}(u)$ | $(x, y) = (f(u, v), g(u, v))$ |
> | Condition | $\varphi'(x) \neq 0$ | $\det(J) \neq 0$ |
> | Derivative of inverse | $(\varphi^{-1})' = \dfrac{1}{\varphi'}$ | $D(f, g) = J^{-1}$ |

^rem-16-5

## Derivation via Chain Rule

We now derive the formula $D(f, g) = J^{-1}$ using the [[Multivariable Chain Rule|chain rule]].

Suppose the inverse exists: $x = f(u, v)$, $y = g(u, v)$.

Then the composition gives the identity:

$$
(x, y) = (f(\varphi(x,y), \psi(x,y)), \, g(\varphi(x,y), \psi(x,y))).
$$

**Using the chain rule:** For $f(u, v)$ where $u = \varphi(x,y)$ and $v = \psi(x,y)$:

$$
\begin{pmatrix} \partial_x f \\ \partial_y f \end{pmatrix} = \begin{pmatrix} f_u u_x + f_v v_x \\ f_u u_y + f_v v_y \end{pmatrix} = \begin{pmatrix} u_x & v_x \\ u_y & v_y \end{pmatrix} \begin{pmatrix} f_u \\ f_v \end{pmatrix}.
$$

Similarly for $g(u, v)$:

$$
\begin{pmatrix} \partial_x g \\ \partial_y g \end{pmatrix} = \begin{pmatrix} u_x & v_x \\ u_y & v_y \end{pmatrix} \begin{pmatrix} g_u \\ g_v \end{pmatrix}.
$$

**Combining into matrix form:**

$$
\begin{pmatrix} \partial_x f & \partial_x g \\ \partial_y f & \partial_y g \end{pmatrix} = \begin{pmatrix} \varphi_x & \psi_x \\ \varphi_y & \psi_y \end{pmatrix} \begin{pmatrix} f_u & g_u \\ f_v & g_v \end{pmatrix}.
$$

**Applying to the identity:** Since $f(\varphi(x,y), \psi(x,y)) = x$ and $g(\varphi(x,y), \psi(x,y)) = y$:

$$
\begin{pmatrix} \partial_x f & \partial_x g \\ \partial_y f & \partial_y g \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}.
$$

Substituting:

$$
\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} \varphi_x & \psi_x \\ \varphi_y & \psi_y \end{pmatrix} \begin{pmatrix} f_u & g_u \\ f_v & g_v \end{pmatrix}.
$$

**Solving for the inverse Jacobian:**

$$
\begin{pmatrix} f_u & g_u \\ f_v & g_v \end{pmatrix} = \begin{pmatrix} \varphi_x & \psi_x \\ \varphi_y & \psi_y \end{pmatrix}^{-1}.
$$

Taking the transpose ([[§9 Matrices#^ladr-3-54|LADR 3.54]]):

$$
\boxed{\begin{pmatrix} f_u & f_v \\ g_u & g_v \end{pmatrix} = \begin{pmatrix} \varphi_x & \varphi_y \\ \psi_x & \psi_y \end{pmatrix}^{-1} = J^{-1}}
$$

## Example: Finding Derivatives of the Inverse

> [!example] Example §16.2
> Consider the mapping:
>
> $$
> u = \varphi(x, y) = x^2 - y^2, \qquad v = \psi(x, y) = 2xy.
> $$
>
> Suppose the inverse exists: $x = f(u, v)$, $y = g(u, v)$. Find $f_u, f_v, g_u, g_v$.
>
> **Step 1: Compute the Jacobian.**
>
> $$
> J = \begin{pmatrix} \varphi_x & \varphi_y \\ \psi_x & \psi_y \end{pmatrix} = \begin{pmatrix} 2x & -2y \\ 2y & 2x \end{pmatrix}.
> $$
>
> **Step 2: Check invertibility.**
>
> $$
> \det(J) = 4x^2 + 4y^2 = 4(x^2 + y^2) \neq 0 \quad \text{for } (x, y) \neq (0, 0).
> $$
>
> **Step 3: Compute $J^{-1}$.**
>
> $$
> J^{-1} = \frac{1}{4(x^2 + y^2)} \begin{pmatrix} 2x & 2y \\ -2y & 2x \end{pmatrix} = \frac{1}{2(x^2 + y^2)} \begin{pmatrix} x & y \\ -y & x \end{pmatrix}.
> $$
>
> **Step 4: Read off the partial derivatives.**
>
> $$
> f_u = \frac{x}{2(x^2 + y^2)}, \quad f_v = \frac{y}{2(x^2 + y^2)}, \quad g_u = \frac{-y}{2(x^2 + y^2)}, \quad g_v = \frac{x}{2(x^2 + y^2)}.
> $$
>
> **Note:** The formulas are in terms of $(x, y)$, but $f, g$ are functions of $(u, v)$. To express purely in $(u, v)$, we would substitute $x = f(u, v)$, $y = g(u, v)$ — but we don't know those explicitly!
>
> **The power of the theorem:** We found the derivatives without explicit formulas for $f$ and $g$.

^ex-16-2

![[m452-13-1.svg]]
*Local but not global inversion for $u = x^2 - y^2$, $v = 2xy$. Near $(x_0, y_0) = (1, \tfrac12)$, where $\det J = 4(x^2 + y^2) = 5 \neq 0$, the small square $Q$ (blue) is carried one-to-one onto a curvilinear patch around $(u_0, v_0) = (\tfrac34, 1)$: the grid lines stay transversal, and on the patch the local inverse $(f, g)$ (green) exists. The map cannot be inverted globally, though. The antipodal square $-Q$ (red, dashed) lands on exactly the same patch, because $(-x, -y)$ and $(x, y)$ have the same image. The theorem only promises an inverse near one preimage at a time. At the origin (hollow dot), $\det J = 0$ and even the local statement fails.*

## Example: Polar Coordinates

> [!example] Example §16.3: Cartesian to Polar
> Define $r = r(x, y) = \sqrt{x^2 + y^2}$ and $\theta = \theta(x, y) = \arctan(y/x)$.
>
> The partial derivatives are:
>
> $$
> r_x = \frac{x}{r}, \quad r_y = \frac{y}{r}, \quad \theta_x = -\frac{y}{r^2}, \quad \theta_y = \frac{x}{r^2}.
> $$
>
> The Jacobian matrix and determinant:
>
> $$
> J = \begin{pmatrix} x/r & y/r \\ -y/r^2 & x/r^2 \end{pmatrix}, \qquad |J| = \frac{x^2 + y^2}{r^3} = \frac{1}{r}.
> $$

^ex-16-3

*Chain ([[Angle form on the punctured plane|angle form]]):* [[§39 Closed and Exact Forms#^prop-39-6|Chapter 7]] →

> [!remark]- Connections
> - The conversion formulas with worked examples: [[§75 Polar Coordinates#^thm-75-2|Calc Thm. §75.2]].

> [!example] Example §16.4: Polar to Cartesian
> Define $x = r\cos\theta$ and $y = r\sin\theta$.
>
> The Jacobian matrix and determinant:
>
> $$
> J = \begin{pmatrix} \cos\theta & -r\sin\theta \\ \sin\theta & r\cos\theta \end{pmatrix}, \qquad |J| = r.
> $$

^ex-16-4

> [!remark]- Connections
> - This $|J| = r$ is the factor in $dx\,dy = r\,dr\,d\theta$: [[§22 Properties of the Integral#^thm-22-6|Change of Variables to Polar Coordinates]] (§15.7), [[§25 Change of Variables on General Domains#^ex-25-1|Example §25.1]].
> - The conversion formulas with worked examples: [[§75 Polar Coordinates#^thm-75-2|Calc Thm. §75.2]].

> [!remark] Remark: Reciprocal Jacobians
> The Jacobian determinants are reciprocals: $\dfrac{1}{r} \cdot r = 1$.
>
> This is a general fact: if two mappings are inverses, their Jacobian determinants are reciprocals.

^rem-16-6

> [!remark]- Connections
> - Why: the [[§12 Composition of Functions and the Chain Rule#^rem-12-4|chain rule for Jacobians]] gives $J_{\Phi^{-1}} J_\Phi = I$, and the determinant is multiplicative ([[§37 Determinants#^ladr-9-49|LADR 9.49]]).
