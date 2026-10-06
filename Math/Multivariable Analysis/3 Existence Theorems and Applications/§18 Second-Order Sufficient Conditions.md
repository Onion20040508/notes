---
type: section
subject: "[[Multivariable Analysis]]"
chapter: 3
section: 18
tags: [multivariable-analysis, math452]
---
← [[§17 Optimization and Lagrange Multipliers]] · ↑ [[· 3 Existence Theorems and Applications]] · [[§19 The Unit Circle and Polar Coordinates]] →

## Second-Order Sufficient Conditions: The Hessian Test

The Lagrange conditions $\nabla f = \mathbf{0}$ (unconstrained) or $\nabla f = \lambda \nabla g$ (constrained) are **necessary** for an extremum, but not sufficient. A critical point could be a max, min, or saddle point. The Hessian test provides **sufficient** conditions.

> [!definition] Definition §31.1: Hessian Matrix
> For $f \in C^2$ near $(x_0, y_0)$, the **Hessian matrix** is:
>
> $$
> H = \begin{pmatrix} f_{xx} & f_{xy} \\ f_{yx} & f_{yy} \end{pmatrix}
> $$
>
> evaluated at $(x_0, y_0)$. By [[Schwarz–Clairaut Theorem|Schwarz–Clairaut]], $H$ is [[§35 Bilinear Forms and Quadratic Forms#^ladr-9-11|symmetric]]: $f_{xy} = f_{yx}$.

^def-18-1

> [!remark]- Connections
> - $H$ is the matrix of a symmetric bilinear form ([[§35 Bilinear Forms and Quadratic Forms#^ladr-9-4|LADR 9.4]], [[§35 Bilinear Forms and Quadratic Forms#^ladr-9-9|LADR 9.9]]); made precise in [[§39 Closed and Exact Forms#^prop-39-2|The Second Total Derivative Is the Hessian]] (§22.7).

> [!remark] Remark: The Hessian as the Second Total Derivative
> Just as the gradient $\nabla f$ is the first total derivative — a linear map $Df_{\mathbf{p}}: \mathbf{v} \mapsto \nabla f \cdot \mathbf{v}$ that captures the first-order behavior of $f$ ([[§7 Differentiability|§7]]–[[§10 The Differential|§10]]) — the Hessian is the *second* total derivative: a [[§35 Bilinear Forms and Quadratic Forms#^ladr-9-1|bilinear form]] $D^2f_{\mathbf{p}}: (\mathbf{u}, \mathbf{v}) \mapsto \mathbf{u}^T H_f \mathbf{v}$ that captures the second-order behavior. The Taylor expansion from [[Multivariable Taylor's Theorem|§9]] says exactly this (where $\mathbf{p} \in \mathbb{R}^n$ is the base point and $\mathbf{h} \in \mathbb{R}^n$ is the increment):
>
> $$
> f(\mathbf{p} + \mathbf{h}) = f(\mathbf{p}) + \underbrace{Df_{\mathbf{p}}(\mathbf{h})}_{\text{linear: gradient}} + \frac{1}{2}\underbrace{D^2f_{\mathbf{p}}(\mathbf{h}, \mathbf{h})}_{\text{bilinear: Hessian}} + o(|\mathbf{h}|^2).
> $$
>
> The positive/negative definiteness test below asks: is this bilinear form positive for all directions $\mathbf{h}$? The symmetry of $H$ ($f_{xy} = f_{yx}$) will reappear in a deeper role when we study differential forms ([[§37 The Algebra of Differential Forms|§37]]).

^rem-18-8

> [!definition] Definition §31.2: Positive Definite
> A symmetric matrix $A = \begin{pmatrix} a & b \\ b & c \end{pmatrix}$ is:
> - **Positive definite** if $\mathbf{x}^T A \mathbf{x} > 0$ for all $\mathbf{x} \neq \mathbf{0}$.
>
> Explicitly, for $\mathbf{x} = (h, k)^T$:
>
> $$
> \mathbf{x}^T A \mathbf{x} = (h, k) \begin{pmatrix} a & b \\ b & c \end{pmatrix} \begin{pmatrix} h \\ k \end{pmatrix} = (h, k) \begin{pmatrix} ah + bk \\ bh + ck \end{pmatrix} = ah^2 + 2bhk + ck^2.
> $$

^def-18-2

> [!definition] Definition §31.3: Negative Definite
> A symmetric matrix $A = \begin{pmatrix} a & b \\ b & c \end{pmatrix}$ is:
> - **Negative definite** if $\mathbf{x}^T A \mathbf{x} < 0$ for all $\mathbf{x} \neq \mathbf{0}$.

^def-18-3

> [!definition] Definition §31.4: Indefinite
> A symmetric matrix $A = \begin{pmatrix} a & b \\ b & c \end{pmatrix}$ is:
> - **Indefinite** if $\mathbf{x}^T A \mathbf{x}$ takes both positive and negative values.

^def-18-4

> [!remark]- Connections
> - $\mathbf{x}^T A \mathbf{x}$ is the quadratic form of $A$ ([[§35 Bilinear Forms and Quadratic Forms#^ladr-9-18|LADR 9.18]], [[§35 Bilinear Forms and Quadratic Forms#^ladr-9-20|LADR 9.20]]); positive definite is the strict version of a positive operator ([[§25 Positive Operators#^ladr-7-34|LADR 7.34]]).
> - By the [[Real spectral theorem|real spectral theorem]] (LADR 7.29), definiteness is read off from the signs of the eigenvalues of $A$.
> - Computational version for n × n matrices: [[§59★ Quadratic Forms#^def-59-4|235 Def. §59.4]], with definiteness read off from eigenvalues in [[§59★ Quadratic Forms#^thm-59-4|235 Thm. §59.4]] (worked classifications).

> [!theorem] Theorem §31.1: Second-Order Sufficient Conditions — Unconstrained
> Let $f \in C^2(B_\varepsilon(x_0, y_0))$ with $f_x(x_0, y_0) = f_y(x_0, y_0) = 0$ (critical point).
>
> Let $H = \begin{pmatrix} f_{xx} & f_{xy} \\ f_{xy} & f_{yy} \end{pmatrix}$ be the Hessian at $(x_0, y_0)$.
> 1. If $H$ is positive definite, then $f$ has a **local minimum** at $(x_0, y_0)$.
> 2. If $H$ is negative definite, then $f$ has a **local maximum** at $(x_0, y_0)$.
> 3. If $H$ is indefinite, then $(x_0, y_0)$ is a **saddle point**.

^thm-18-1

![[m452-14-1.svg]]
*The three nondegenerate critical point types, classified by the Hessian: both eigenvalues positive (bowl, local min), both negative (dome, local max), mixed signs (saddle). The second derivative test of §17 reads these signs from $f_{xx}$ and $\det H = f_{xx}f_{yy} - f_{xy}^2$.*

> [!proof]+ Proof Sketch
> By Taylor's theorem (single-variable version applied to $F(t) = f(x_0 + th, y_0 + tk)$; [[§31 Taylor's Theorem#^thm-31-2|451 §31.2]], as in [[Multivariable Taylor's Theorem|Theorem §11.2]]):
>
> $$
> f(x_0 + h, y_0 + k) = f(x_0, y_0) + \underbrace{f_x h + f_y k}_{= 0} + \frac{1}{2}\left( f_{xx} h^2 + 2f_{xy} hk + f_{yy} k^2 \right)\Big|_{(x_0 + \theta h, y_0 + \theta k)}
> $$
>
> for some $\theta \in (0, 1)$.
>
> Using matrix notation:
>
> $$
> f(x_0 + h, y_0 + k) - f(x_0, y_0) = \frac{1}{2} (h, k) \begin{pmatrix} f_{xx} & f_{xy} \\ f_{xy} & f_{yy} \end{pmatrix}_{(x_0 + \theta h, y_0 + \theta k)} \begin{pmatrix} h \\ k \end{pmatrix}
> $$
>
> If $H$ is positive definite at $(x_0, y_0)$, then by continuity of second partials, $H$ remains positive definite in a neighborhood. Thus:
>
> $$
> (h, k) H \begin{pmatrix} h \\ k \end{pmatrix} > 0 \quad \text{for } (h, k) \neq (0, 0).
> $$
>
> This means $f(x_0 + h, y_0 + k) > f(x_0, y_0)$ for all small $(h, k) \neq (0, 0)$, so $(x_0, y_0)$ is a local minimum.
>
> Similarly, negative definite $\Rightarrow$ local maximum.
>
> If $H$ is indefinite, it has eigenvalues $\lambda_+ > 0 > \lambda_-$ with unit eigenvectors $\mathbf{v}_+, \mathbf{v}_-$ ([[Real spectral theorem|LADR 7.29]]). Restrict $f$ to the line through $(x_0, y_0)$ in direction $\mathbf{v}_\pm$, i.e., take $(h, k) = t\mathbf{v}_\pm$ above: the difference $f(x_0 + h, y_0 + k) - f(x_0, y_0)$ equals $\frac{t^2}{2}\,\mathbf{v}_\pm^{T} H_{(x_0 + \theta h, y_0 + \theta k)} \mathbf{v}_\pm$, and by continuity of the second partials $\mathbf{v}_\pm^{T} H_{(x_0 + \theta h, y_0 + \theta k)} \mathbf{v}_\pm \to \mathbf{v}_\pm^{T} H \mathbf{v}_\pm = \lambda_\pm$ as $t \to 0$. So for small $t \neq 0$ the difference is $> 0$ along $\mathbf{v}_+$ and $< 0$ along $\mathbf{v}_-$: $f$ takes values above and below $f(x_0, y_0)$ arbitrarily close to $(x_0, y_0)$, which is a saddle point.

^pf-18-1

*Uses:* [[§31 Taylor's Theorem#^thm-31-2|451 §31.2]], [[§11 Taylor's Theorem for Multivariable Functions#^thm-11-1|§11.1]], [[Multivariable Taylor's Theorem|§11.2]], [[Schwarz–Clairaut Theorem|§6.1]], [[§18 Second-Order Sufficient Conditions#^def-18-2|Def. §18.2]], [[§18 Second-Order Sufficient Conditions#^def-18-3|Def. §18.3]], [[§18 Second-Order Sufficient Conditions#^def-18-4|Def. §18.4]], [[§17 Optimization and Lagrange Multipliers#^def-17-1|Def. §17.1]], [[§17 Optimization and Lagrange Multipliers#^def-17-2|Def. §17.2]], [[Real spectral theorem|LADR 7.29]]

> [!remark]- Connections
> - MATH 451 relative: the one-variable Taylor expansion with Lagrange remainder ([[§31 Taylor's Theorem#^thm-31-2|451 §31.2]]) is the whole engine; in 1D the Hessian is just $f''(x_0)$.
> - The eigenvalue picture in the figure is the [[Real spectral theorem|real spectral theorem]] (LADR 7.29) applied to the symmetric matrix $H$.
> - Computational version: the test with $D = f_{xx}f_{yy} - f_{xy}^2$, [[§113 Maximum and Minimum Values#^thm-113-2|Calc Thm. §113.2]] (with worked examples).
> - Classifying the Hessian by its eigenvalues, with worked examples: [[§59★ Quadratic Forms#^thm-59-4|235 Thm. §59.4]].

## Testing Definiteness: Principal Minors

For a $2 \times 2$ symmetric matrix $A = \begin{pmatrix} a & b \\ b & c \end{pmatrix}$:

- **Positive definite** $\iff$ $a > 0$ and $\det(A) = ac - b^2 > 0$.
- **Negative definite** $\iff$ $a < 0$ and $\det(A) = ac - b^2 > 0$.
- **Indefinite** $\iff$ $\det(A) < 0$.

For the Hessian $H = \begin{pmatrix} f_{xx} & f_{xy} \\ f_{xy} & f_{yy} \end{pmatrix}$:

- **Local min** if $f_{xx} > 0$ and $f_{xx} f_{yy} - f_{xy}^2 > 0$.
- **Local max** if $f_{xx} < 0$ and $f_{xx} f_{yy} - f_{xy}^2 > 0$.
- **Saddle point** if $f_{xx} f_{yy} - f_{xy}^2 < 0$.
- **Test inconclusive** if $f_{xx} f_{yy} - f_{xy}^2 = 0$.

> [!remark] Remark: General $n \times n$ Case: Sylvester's Criterion
> For an $n \times n$ symmetric matrix $A$, check the **leading principal minors** (determinants of upper-left $k \times k$ submatrices for $k = 1, 2, \ldots, n$):
>
> $$
> \Delta_1 = a_{11}, \quad \Delta_2 = \det \begin{pmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{pmatrix}, \quad \Delta_3 = \det \begin{pmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \end{pmatrix}, \quad \ldots
> $$
>
> - **Positive definite** $\iff$ $\Delta_1 > 0, \Delta_2 > 0, \ldots, \Delta_n > 0$ (all positive).
> - **Negative definite** $\iff$ $\Delta_1 < 0, \Delta_2 > 0, \Delta_3 < 0, \ldots$ (alternating signs, starting negative).
>
> The pattern for negative definite: $(-1)^k \Delta_k > 0$ for all $k$.

^rem-18-9

> [!remark]- Connections
> - Other characterizations of (semi)definiteness — nonnegative eigenvalues, $A = R^*R$ — are in [[§25 Positive Operators#^ladr-7-38|Characterization of positive operators]] (LADR 7.38).

> [!remark] Remark: The Logical Flow: Necessary $\to$ Sufficient
> Now that we have both the Lagrange conditions (necessary) and the Hessian test (sufficient), we can summarize the complete optimization workflow:
>
> **Stage 1: Find candidates (Necessary Conditions).**
>
> The Lagrange condition $\nabla f = \lambda \nabla g$ (constrained, [[Method of Lagrange Multipliers|§17.2]]) or $\nabla f = \mathbf{0}$ (unconstrained, [[§17 Optimization and Lagrange Multipliers#^thm-17-1|§17.1]]) is a **necessary** condition for extrema:
>
> $$
> \text{If } (x_0, y_0) \text{ is an extremum} \quad \Longrightarrow \quad (x_0, y_0) \text{ satisfies the necessary condition.}
> $$
>
> The [[Contrapositive, Converse and Inverse|contrapositive]]: if a point does *not* satisfy the necessary condition, it *cannot* be an extremum. So solving these equations gives us all possible candidates.
>
> **Stage 2: Classify candidates (Sufficient Conditions).**
>
> Among the candidates, we determine which are actually maxima, minima, or neither using **sufficient** conditions:
> - **Comparison method:** If the domain is compact and $f$ is continuous, EVT guarantees a max and min exist ([[Extreme Value Theorem]]; [[Continuous Image of a Compact Space is Compact|590 §18.3]], [[Heine–Borel Theorem|Heine–Borel]]). Evaluate $f$ at all candidates; the largest value is the max, smallest is the min.
> - **Second-order test (Hessian):** Check definiteness of the Hessian (unconstrained, [[Second Derivative Test in Several Variables|§18.1]]) or bordered Hessian (constrained) to classify each candidate.
>
> **Summary:**
>
> $$
> \boxed{\text{Necessary conditions} \xrightarrow{\text{find}} \text{Candidates} \xrightarrow{\text{classify via}} \text{Sufficient conditions} \xrightarrow{\text{determine}} \text{Actual extrema}}
> $$
>
> This two-stage approach is fundamental: necessary conditions cast a wide net (no extremum escapes), then sufficient conditions filter out the true extrema.

^rem-18-10
