---
type: section
subject: "[[Ordinary Differential Equations]]"
chapter: 7
section: 30
bdp: "7.4"
aliases: ["BDP 7.4"]
tags: [ordinary-differential-equations, math331]
---
← [[§29 Systems of Linear Algebraic Equations; Linear Independence, Eigenvalues, Eigenvectors]] · ↑ [[· 7 Systems of First-Order Linear Equations]] · [[§31 Homogeneous Linear Systems with Constant Coefficients]] →

*Boyce–DiPrima, Section 7.4.*

The theory of a system of $n$ first-order linear equations $\mathbf{x}' = \mathbf{P}(t)\mathbf{x}$ runs parallel to that of a single second-order linear equation in [[§14 Solutions of Linear Homogeneous Equations; the Wronskian|§14]]. Linear combinations of solutions are solutions. Any $n$ solutions that are linearly independent at each point give every solution, each in exactly one way. Their independence is tested by one determinant, the Wronskian, and Abel's formula shows that it is either never zero or identically zero, so it suffices to check a single point. Such fundamental sets always exist, and for a real system, real and imaginary parts of complex solutions are again solutions. Everything in Sections 7.5–7.9 rests on these five theorems.

## Systems and Their Solutions

> [!definition] Definition §30.1: Linear System of First-Order Equations
> The system
>
> $$
> x_1' = p_{11}(t)x_1 + \cdots + p_{1n}(t)x_n + g_1(t), \quad \ldots, \quad x_n' = p_{n1}(t)x_1 + \cdots + p_{nn}(t)x_n + g_n(t) \qquad (1)
> $$
>
> is written, with $\mathbf{x} = (x_1, \ldots, x_n)^T$, $\mathbf{g} = (g_1, \ldots, g_n)^T$ and the $n \times n$ matrix $\mathbf{P}(t) = (p_{ij}(t))$, as
>
> $$
> \mathbf{x}' = \mathbf{P}(t)\mathbf{x} + \mathbf{g}(t) . \qquad (2)
> $$
>
> A vector function $\mathbf{x} = \mathbf{x}(t)$ is a **solution** of (2) if its components satisfy (1). Throughout, $\mathbf{P}$ and $\mathbf{g}$ are continuous on an interval $\alpha < t < \beta$ (each $p_{ij}$ and $g_i$ is continuous there); by [[§27 Introduction to Systems of First-Order Linear Equations#^thm-27-3|Theorem §27.3]] (BDP Theorem 7.1.2) this guarantees solutions on that interval. Setting $\mathbf{g}(t) = \mathbf{0}$ gives the **homogeneous** system
>
> $$
> \mathbf{x}' = \mathbf{P}(t)\mathbf{x} . \qquad (3)
> $$
>
> Specific solutions of (3) are written $\mathbf{x}^{(1)}(t), \ldots, \mathbf{x}^{(k)}(t)$, and $x_{ij}(t) = x_i^{(j)}(t)$ is the $i$th component of the $j$th solution.
>
> *BDP: 7.4 (text), Equations (1)–(4)*

^def-30-1

> [!theorem] Theorem §30.1: Principle of Superposition
> If $\mathbf{x}^{(1)}$ and $\mathbf{x}^{(2)}$ are solutions of the system (3), then $c_1\mathbf{x}^{(1)} + c_2\mathbf{x}^{(2)}$ is also a solution for any constants $c_1$ and $c_2$. More generally, if $\mathbf{x}^{(1)}, \ldots, \mathbf{x}^{(k)}$ are solutions of (3), so is
>
> $$
> \mathbf{x} = c_1\mathbf{x}^{(1)}(t) + \cdots + c_k\mathbf{x}^{(k)}(t) \qquad (8)
> $$
>
> for any constants $c_1, \ldots, c_k$.
>
> *BDP: Theorem 7.4.1; 7.4 (text), Equation (8)*

^thm-30-1

> [!proof]+ Proof
> Differentiation is linear and matrix multiplication distributes over sums, so
>
> $$
> (c_1\mathbf{x}^{(1)} + c_2\mathbf{x}^{(2)})' = c_1\mathbf{x}^{(1)\prime} + c_2\mathbf{x}^{(2)\prime} = c_1\mathbf{P}(t)\mathbf{x}^{(1)} + c_2\mathbf{P}(t)\mathbf{x}^{(2)} = \mathbf{P}(t)\big(c_1\mathbf{x}^{(1)} + c_2\mathbf{x}^{(2)}\big) .
> $$
>
> For $k$ solutions (BDP's Problem 7), induct on $k$: $c_1\mathbf{x}^{(1)} + \cdots + c_k\mathbf{x}^{(k)} = \big(c_1\mathbf{x}^{(1)} + \cdots + c_{k-1}\mathbf{x}^{(k-1)}\big) + c_k\mathbf{x}^{(k)}$ is $1$ times a solution (by the induction hypothesis) plus $c_k$ times a solution.

^pf-30-1

*Uses:* [[§30 Basic Theory of Systems of First-Order Linear Equations#^def-30-1|Def. §30.1]]

> [!remark]- Connections
> - See also: [[§38 Applications to Differential Equations#^prop-38-1|235 Prop. §38.1]], Lay's superposition for constant $A$, phrased as "the solution set is a subspace" of the vector-valued functions.

> [!example] Example §30.1: Two Solutions, Their Wronskian, and Abel's Formula
> Show that $\mathbf{x}^{(1)}(t) = \begin{pmatrix} 1 \\ 2 \end{pmatrix}e^{3t}$ and $\mathbf{x}^{(2)}(t) = \begin{pmatrix} 1 \\ -2 \end{pmatrix}e^{-t}$ are solutions of
>
> $$
> \mathbf{x}' = \begin{pmatrix} 1 & 1 \\ 4 & 1 \end{pmatrix}\mathbf{x}, \qquad (6)
> $$
>
> and that they form a fundamental set of solutions on $-\infty < t < \infty$.
>
> **Solutions.** $\mathbf{x}^{(1)\prime} = (3e^{3t}, 6e^{3t})^T$, and $\mathbf{P}\mathbf{x}^{(1)} = (e^{3t} + 2e^{3t},\ 4e^{3t} + 2e^{3t})^T = (3e^{3t}, 6e^{3t})^T$. Likewise $\mathbf{x}^{(2)\prime} = (-e^{-t}, 2e^{-t})^T$ and $\mathbf{P}\mathbf{x}^{(2)} = (e^{-t} - 2e^{-t},\ 4e^{-t} - 2e^{-t})^T = (-e^{-t}, 2e^{-t})^T$. By Theorem §30.1,
>
> $$
> \mathbf{x} = c_1\begin{pmatrix} 1 \\ 2 \end{pmatrix}e^{3t} + c_2\begin{pmatrix} 1 \\ -2 \end{pmatrix}e^{-t} = \begin{pmatrix} c_1e^{3t} + c_2e^{-t} \\ 2c_1e^{3t} - 2c_2e^{-t} \end{pmatrix} \qquad (7)
> $$
>
> is a solution for all $c_1$, $c_2$.
>
> **Wronskian.**
>
> $$
> W[\mathbf{x}^{(1)}, \mathbf{x}^{(2)}](t) = \begin{vmatrix} e^{3t} & e^{-t} \\ 2e^{3t} & -2e^{-t} \end{vmatrix} = -2e^{2t} - 2e^{2t} = -4e^{2t} ,
> $$
>
> which is never zero. So the two solutions are independent at every $t$ ([[§29 Systems of Linear Algebraic Equations; Linear Independence, Eigenvalues, Eigenvectors#^thm-29-2|Theorem §29.2]]), they form a fundamental set (Definition §30.3), and by Theorem §30.2 every solution of (6) is of the form (7).
>
> **Abel's formula.** Here $p_{11} + p_{22} = 1 + 1 = 2$, and indeed $W = c\,e^{\int 2\,dt} = c\,e^{2t}$ with $c = -4$, as Theorem §30.3 predicts.
>
> *BDP: 7.4 (text), Equations (5)–(7); 7.5, Equation (16)*

^ex-30-1

The nonhomogeneous system (2) is tied to (3) as for a single equation: the difference of two solutions of (2) solves (3) ([[§27 Introduction to Systems of First-Order Linear Equations#^ex-27-3|Example §27.3]], Written HW 6, Problem 1). In vector form, if $\mathbf{x}_1' = \mathbf{P}\mathbf{x}_1 + \mathbf{g}$ and $\mathbf{x}_2' = \mathbf{P}\mathbf{x}_2 + \mathbf{g}$, then $(\mathbf{x}_1 - \mathbf{x}_2)' = \mathbf{P}(\mathbf{x}_1 - \mathbf{x}_2)$. Consequently every solution of (2) is one particular solution plus a solution of (3), the structure of [[§35★ Nonhomogeneous Linear Systems|§35★]] (BDP's Problem 7.4.11), just as for $\mathbf{A}\mathbf{x} = \mathbf{b}$ in [[§29 Systems of Linear Algebraic Equations; Linear Independence, Eigenvalues, Eigenvectors#^thm-29-1|Theorem §29.1]].

## Fundamental Sets of Solutions

> [!definition] Definition §30.2: Wronskian of n Solutions
> Let $\mathbf{x}^{(1)}, \ldots, \mathbf{x}^{(n)}$ be $n$ solutions of (3), and let $\mathbf{X}(t)$ be the matrix whose columns are $\mathbf{x}^{(1)}(t), \ldots, \mathbf{x}^{(n)}(t)$:
>
> $$
> \mathbf{X}(t) = \begin{pmatrix} x_{11}(t) & \cdots & x_{1n}(t) \\ \vdots & & \vdots \\ x_{n1}(t) & \cdots & x_{nn}(t) \end{pmatrix} . \qquad (9)
> $$
>
> Its determinant is the **Wronskian** of the $n$ solutions:
>
> $$
> W[\mathbf{x}^{(1)}, \ldots, \mathbf{x}^{(n)}](t) = \det\mathbf{X}(t) . \qquad (10)
> $$
>
> By [[§29 Systems of Linear Algebraic Equations; Linear Independence, Eigenvalues, Eigenvectors#^thm-29-2|Theorem §29.2]], the solutions are linearly independent at a point $t$ if and only if $W[\mathbf{x}^{(1)}, \ldots, \mathbf{x}^{(n)}](t) \ne 0$.
>
> *BDP: 7.4 (text), Equations (9)–(10)*

^def-30-2

> [!theorem] Theorem §30.2: Every Solution Is a Combination of n Independent Solutions
> If the vector functions $\mathbf{x}^{(1)}, \ldots, \mathbf{x}^{(n)}$ are linearly independent solutions of the system (3) for each point in the interval $\alpha < t < \beta$, then each solution $\mathbf{x} = \mathbf{x}(t)$ of (3) can be expressed as a linear combination of $\mathbf{x}^{(1)}, \ldots, \mathbf{x}^{(n)}$,
>
> $$
> \mathbf{x}(t) = c_1\mathbf{x}^{(1)}(t) + \cdots + c_n\mathbf{x}^{(n)}(t), \qquad (11)
> $$
>
> in exactly one way.
>
> *BDP: Theorem 7.4.2*

^thm-30-2

> [!proof]+ Proof
> Let $\mathbf{x}(t)$ be a solution of (3), fix a point $t_0$ in $\alpha < t < \beta$, and let $\mathbf{y} = \mathbf{x}(t_0)$. We look for a solution of the form $c_1\mathbf{x}^{(1)}(t) + \cdots + c_n\mathbf{x}^{(n)}(t)$ that has the same initial value at $t_0$, that is, for constants with
>
> $$
> c_1\mathbf{x}^{(1)}(t_0) + \cdots + c_n\mathbf{x}^{(n)}(t_0) = \mathbf{y}, \qquad (12)
> $$
>
> or, in scalar form,
>
> $$
> c_1x_{11}(t_0) + \cdots + c_nx_{1n}(t_0) = y_1, \quad \ldots, \quad c_1x_{n1}(t_0) + \cdots + c_nx_{nn}(t_0) = y_n . \qquad (13)
> $$
>
> This is the linear system $\mathbf{X}(t_0)\mathbf{c} = \mathbf{y}$. Its determinant of coefficients is $W[\mathbf{x}^{(1)}, \ldots, \mathbf{x}^{(n)}](t_0)$, which is nonzero because the solutions are independent at $t_0$ (Definition §30.2). So (13) has a unique solution $c_1, \ldots, c_n$ ([[§29 Systems of Linear Algebraic Equations; Linear Independence, Eigenvalues, Eigenvectors#^thm-29-1|Theorem §29.1]](a)).
>
> With these constants, $\mathbf{z}(t) = c_1\mathbf{x}^{(1)}(t) + \cdots + c_n\mathbf{x}^{(n)}(t)$ is a solution of (3) (Theorem §30.1) with $\mathbf{z}(t_0) = \mathbf{y} = \mathbf{x}(t_0)$. Both $\mathbf{z}$ and $\mathbf{x}$ solve the initial value problem $\mathbf{x}' = \mathbf{P}(t)\mathbf{x}$, $\mathbf{x}(t_0) = \mathbf{y}$, so by the uniqueness part of [[§27 Introduction to Systems of First-Order Linear Equations#^thm-27-3|Theorem §27.3]] (BDP Theorem 7.1.2), $\mathbf{x}(t) = \mathbf{z}(t)$ on $\alpha < t < \beta$. This is (11).
>
> **Exactly one way.** (BDP asserts this; here is why, as in Problem 15b.) If also $\mathbf{x}(t) = k_1\mathbf{x}^{(1)}(t) + \cdots + k_n\mathbf{x}^{(n)}(t)$, then evaluating at $t_0$ shows that $k_1, \ldots, k_n$ also solve (13), whose solution is unique; so $k_j = c_j$ for all $j$.

^pf-30-2

*Uses:* [[§30 Basic Theory of Systems of First-Order Linear Equations#^thm-30-1|§30.1]], [[§30 Basic Theory of Systems of First-Order Linear Equations#^def-30-2|Def. §30.2]], [[§29 Systems of Linear Algebraic Equations; Linear Independence, Eigenvalues, Eigenvectors#^thm-29-1|§29.1]], [[§29 Systems of Linear Algebraic Equations; Linear Independence, Eigenvalues, Eigenvectors#^thm-29-2|§29.2]], [[§27 Introduction to Systems of First-Order Linear Equations#^thm-27-3|§27.3]] (existence and uniqueness)

> [!definition] Definition §30.3: Fundamental Set of Solutions; General Solution
> Any set of solutions $\{\mathbf{x}^{(1)}, \ldots, \mathbf{x}^{(n)}\}$ of (3) that is linearly independent at each point of $\alpha < t < \beta$ is a **fundamental set of solutions** on that interval. For a fundamental set, the expression (11) with arbitrary constants $c_1, \ldots, c_n$ contains every solution of (3) (Theorem §30.2), and only solutions (Theorem §30.1); it is called the **general solution** of (3).
>
> *BDP: 7.4 (text)*

^def-30-3

> [!remark]- Connections
> - Theorems §30.1 and §30.2 say that the solutions of (3) form an $n$-dimensional vector space, with a fundamental set as a basis: the map $\mathbf{x} \mapsto \mathbf{x}(t_0)$ is a linear bijection onto $\mathbb{R}^n$ (or $\mathbb{C}^n$), an isomorphism in the sense of [[§10 Invertibility and Isomorphisms#^ladr-3-69|LADR 3.69]], so the dimension is $n$ by [[§10 Invertibility and Isomorphisms#^ladr-3-70|LADR 3.70]]. Lay states this without proof for constant $A$ ([[§38 Applications to Differential Equations|235 §38]], after Prop. §38.1); this section is its proof.

> [!theorem] Theorem §30.3: Abel's Theorem
> If $\mathbf{x}^{(1)}, \ldots, \mathbf{x}^{(n)}$ are solutions of (3) on the interval $\alpha < t < \beta$, then in this interval $W[\mathbf{x}^{(1)}, \ldots, \mathbf{x}^{(n)}]$ either is identically zero or else never vanishes. More precisely, $W$ satisfies
>
> $$
> \frac{dW}{dt} = \big(p_{11}(t) + p_{22}(t) + \cdots + p_{nn}(t)\big)W, \qquad (14)
> $$
>
> and hence
>
> $$
> W(t) = c\exp\Big(\int \big[p_{11}(t) + \cdots + p_{nn}(t)\big]\,dt\Big), \qquad (15)
> $$
>
> where $c$ is a constant. Formula (15) is **Abel's formula** (for systems it is also called Liouville's formula). With a fixed lower limit, $W(t) = W(t_0)\exp\big(\int_{t_0}^t \operatorname{tr}\mathbf{P}(s)\,ds\big)$, where $\operatorname{tr}\mathbf{P} = p_{11} + \cdots + p_{nn}$ is the trace.
>
> *BDP: Theorem 7.4.3; 7.4 (text), Equations (14)–(15)*

^thm-30-3

> [!proof]+ Proof
> *BDP proves (14) in outline (Problem 8, case $n = 2$, with the general case left as part d); here is the general case.*
>
> **Step 1: the derivative of a determinant.** By the formula for the determinant of a matrix ([[§34 Determinants#^ladr-9-46|LADR 9.46]]), $W = \det\mathbf{X} = \sum_\sigma \operatorname{sgn}(\sigma)\,x_{1\sigma(1)}x_{2\sigma(2)}\cdots x_{n\sigma(n)}$, a sum over the permutations $\sigma$ of $\{1, \ldots, n\}$. Each term is a product of $n$ differentiable functions, one from each row. By the product rule,
>
> $$
> \frac{dW}{dt} = \sum_{k=1}^n \sum_\sigma \operatorname{sgn}(\sigma)\,x_{1\sigma(1)}\cdots x_{k\sigma(k)}'\cdots x_{n\sigma(n)} = \sum_{k=1}^n \det\mathbf{X}_k ,
> $$
>
> where $\mathbf{X}_k$ is $\mathbf{X}$ with its $k$th row replaced by the derivative of that row. (For $n = 2$ this is BDP's Problem 8a: $W' = \begin{vmatrix} x_{11}' & x_{12}' \\ x_{21} & x_{22} \end{vmatrix} + \begin{vmatrix} x_{11} & x_{12} \\ x_{21}' & x_{22}' \end{vmatrix}$.)
>
> **Step 2: use the equation.** Each column $\mathbf{x}^{(j)}$ solves (3), so its $k$th component satisfies $x_{kj}' = \sum_{m=1}^n p_{km}x_{mj}$. Hence the $k$th row of $\mathbf{X}'$ is
>
> $$
> \text{row}_k(\mathbf{X}') = \sum_{m=1}^n p_{km}\,\text{row}_m(\mathbf{X}) .
> $$
>
> The determinant is linear in each row ([[§21 Properties of Determinants#^thm-21-11|235 Thm. §21.11]], for columns, with [[§21 Properties of Determinants#^thm-21-6|235 Thm. §21.6]]), so
>
> $$
> \det\mathbf{X}_k = \sum_{m=1}^n p_{km}\det\big(\mathbf{X} \text{ with row } k \text{ replaced by row } m\big) .
> $$
>
> For $m \ne k$, the matrix in the $m$th term has two equal rows, so its determinant is $0$ ([[§21 Properties of Determinants#^cor-21-5|235 Cor. §21.5]]). Only $m = k$ survives, and $\det\mathbf{X}_k = p_{kk}\det\mathbf{X} = p_{kk}W$. Summing over $k$ gives (14).
>
> **Step 3: solve (14).** Equation (14) is the first-order linear equation $W' - \operatorname{tr}\mathbf{P}(t)\,W = 0$ with continuous coefficient. With the integrating factor $\mu(t) = \exp\big(-\int_{t_0}^t \operatorname{tr}\mathbf{P}(s)\,ds\big)$ ([[§4 Linear Differential Equations; Method of Integrating Factors#^thm-4-2|Theorem §4.2]]), $(\mu W)' = \mu(W' - \operatorname{tr}\mathbf{P}\,W) = 0$, so $\mu W$ is constant (if the solutions are complex-valued, apply this to the real and imaginary parts of $\mu W$), equal to its value $W(t_0)$ at $t_0$:
>
> $$
> W(t) = W(t_0)\exp\Big(\int_{t_0}^t \operatorname{tr}\mathbf{P}(s)\,ds\Big) .
> $$
>
> This is (15). The exponential is never zero, so $W(t) = 0$ for all $t$ if $W(t_0) = 0$, and $W(t) \ne 0$ for all $t$ if $W(t_0) \ne 0$.
>
> **Second proof** (BDP's alternative, Problem 14). Suppose the solutions are linearly dependent at one point $t_0$: there are constants $c_1, \ldots, c_n$, not all zero, with $c_1\mathbf{x}^{(1)}(t_0) + \cdots + c_n\mathbf{x}^{(n)}(t_0) = \mathbf{0}$. Then $\mathbf{z}(t) = c_1\mathbf{x}^{(1)}(t) + \cdots + c_n\mathbf{x}^{(n)}(t)$ solves (3) with $\mathbf{z}(t_0) = \mathbf{0}$. So does the zero function, and by the uniqueness part of [[§27 Introduction to Systems of First-Order Linear Equations#^thm-27-3|Theorem §27.3]], $\mathbf{z}(t) = \mathbf{0}$ for every $t$ in $\alpha < t < \beta$: the same constants make the solutions dependent at every point. So if $W$ vanishes at one point, it vanishes everywhere.

^pf-30-3

*Uses:* [[§30 Basic Theory of Systems of First-Order Linear Equations#^def-30-1|Def. §30.1]], [[§30 Basic Theory of Systems of First-Order Linear Equations#^def-30-2|Def. §30.2]], [[§30 Basic Theory of Systems of First-Order Linear Equations#^thm-30-1|§30.1]], [[§4 Linear Differential Equations; Method of Integrating Factors#^thm-4-2|§4.2]] (integrating factor), [[§27 Introduction to Systems of First-Order Linear Equations#^thm-27-3|§27.3]] (uniqueness), [[§34 Determinants#^ladr-9-46|LADR 9.46]] (Leibniz formula), [[§21 Properties of Determinants#^thm-21-11|235 Thm. §21.11]], [[§21 Properties of Determinants#^thm-21-6|235 Thm. §21.6]], [[§21 Properties of Determinants#^cor-21-5|235 Cor. §21.5]]

> [!remark]- Connections
> - Steps 1–2 are Jacobi's formula for the derivative of the determinant, [[§11 The Classical Groups Are Topological Manifolds#^prop-11-1|591 Prop. §11.1]] ([[Jacobi's Formula]]), applied along the curve $t \mapsto \mathbf{X}(t)$: where $\mathbf{X}$ is invertible, $\frac{d}{dt}\det\mathbf{X} = \det\mathbf{X}\,\operatorname{tr}(\mathbf{X}^{-1}\mathbf{X}') = \det\mathbf{X}\,\operatorname{tr}(\mathbf{X}^{-1}\mathbf{P}\mathbf{X}) = \operatorname{tr}\mathbf{P}\,\det\mathbf{X}$, by [[§31 Trace꞉ A Connection Between Matrices and Operators#^ladr-8-49|LADR 8.49]] ($\operatorname{tr}AB = \operatorname{tr}BA$).

The theorem means that to decide whether $n$ solutions form a fundamental set, it suffices to evaluate their Wronskian at one convenient point. Compare Abel's theorem for second-order equations, [[§14 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-14-8|Theorem §14.8]] (BDP Theorem 3.2.7); it is the case $n = 2$, $\mathbf{P} = \begin{pmatrix} 0 & 1 \\ -q & -p \end{pmatrix}$, where $\operatorname{tr}\mathbf{P} = -p$.

> [!theorem] Theorem §30.4: Existence of a Fundamental Set
> Let $\mathbf{e}^{(1)} = (1, 0, \ldots, 0)^T$, $\mathbf{e}^{(2)} = (0, 1, 0, \ldots, 0)^T$, …, $\mathbf{e}^{(n)} = (0, \ldots, 0, 1)^T$, and let $\mathbf{x}^{(1)}, \ldots, \mathbf{x}^{(n)}$ be the solutions of the system (3) that satisfy the initial conditions
>
> $$
> \mathbf{x}^{(1)}(t_0) = \mathbf{e}^{(1)}, \quad \ldots, \quad \mathbf{x}^{(n)}(t_0) = \mathbf{e}^{(n)}, \qquad (16)
> $$
>
> where $t_0$ is any point in $\alpha < t < \beta$. Then $\mathbf{x}^{(1)}, \ldots, \mathbf{x}^{(n)}$ form a fundamental set of solutions of (3).
>
> *BDP: Theorem 7.4.4*

^thm-30-4

> [!proof]+ Proof
> [[§27 Introduction to Systems of First-Order Linear Equations#^thm-27-3|Theorem §27.3]] (BDP Theorem 7.1.2) guarantees that each initial value problem in (16) has a unique solution on $\alpha < t < \beta$. At $t_0$ the matrix $\mathbf{X}(t_0)$ has columns $\mathbf{e}^{(1)}, \ldots, \mathbf{e}^{(n)}$, so it is the identity matrix and $W(t_0) = \det\mathbf{I} = 1 \ne 0$. By Abel's theorem (Theorem §30.3), $W(t) \ne 0$ for every $t$ in the interval, so the solutions are linearly independent at each point (Definition §30.2): they form a fundamental set (Definition §30.3).

^pf-30-4

*Uses:* [[§27 Introduction to Systems of First-Order Linear Equations#^thm-27-3|§27.3]], [[§30 Basic Theory of Systems of First-Order Linear Equations#^def-30-2|Def. §30.2]], [[§30 Basic Theory of Systems of First-Order Linear Equations#^thm-30-3|§30.3]], [[§30 Basic Theory of Systems of First-Order Linear Equations#^def-30-3|Def. §30.3]]

Once one fundamental set is known, others are obtained as independent linear combinations of it. For theoretical purposes the set of Theorem §30.4 is usually the simplest; as a matrix it reappears as the fundamental matrix $\mathbf{\Phi}(t)$ with $\mathbf{\Phi}(t_0) = \mathbf{I}$ in [[§33★ Fundamental Matrices#^def-33-2|Definition §33.2]].

> [!example] Example §30.2: The Fundamental Set Normalized at t = 0
> For the system (6) of Example §30.1, find the fundamental set of Theorem §30.4 with $t_0 = 0$.
>
> Every solution has the form (7), so we choose $c_1, c_2$ to match the initial values. For $\mathbf{x}(0) = \mathbf{e}^{(1)}$: $c_1 + c_2 = 1$ and $2c_1 - 2c_2 = 0$, so $c_1 = c_2 = \frac12$. For $\mathbf{x}(0) = \mathbf{e}^{(2)}$: $c_1 + c_2 = 0$ and $2c_1 - 2c_2 = 1$, so $c_1 = \frac14$, $c_2 = -\frac14$. Thus
>
> $$
> \hat{\mathbf{x}}^{(1)}(t) = \begin{pmatrix} \frac12(e^{3t} + e^{-t}) \\ e^{3t} - e^{-t} \end{pmatrix}, \qquad
> \hat{\mathbf{x}}^{(2)}(t) = \begin{pmatrix} \frac14(e^{3t} - e^{-t}) \\ \frac12(e^{3t} + e^{-t}) \end{pmatrix} .
> $$
>
> Their Wronskian is $1$ at $t = 0$, so by Abel's formula, with $\operatorname{tr}\mathbf{P} = 2$, it must be $e^{2t}$. Directly:
>
> $$
> \frac12(e^{3t} + e^{-t}) \cdot \frac12(e^{3t} + e^{-t}) - \frac14(e^{3t} - e^{-t})(e^{3t} - e^{-t}) = \frac14\big[(e^{3t} + e^{-t})^2 - (e^{3t} - e^{-t})^2\big] = \frac14 \cdot 4e^{2t} = e^{2t} .
> $$
>
> *BDP: 7.4 (text), applied to Equation (7)*

^ex-30-2

## Real-Valued Solutions

Just as for second-order linear equations ([[§14 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-14-6|Theorem §14.6]], BDP Theorem 3.2.6), a system with real coefficients may have complex-valued solutions, and then real solutions can be extracted from them.

> [!theorem] Theorem §30.5: Real and Imaginary Parts of a Complex Solution
> Consider the system (3), $\mathbf{x}' = \mathbf{P}(t)\mathbf{x}$, where each element of $\mathbf{P}$ is a real-valued continuous function. If $\mathbf{x} = \mathbf{u}(t) + i\mathbf{v}(t)$ is a complex-valued solution of (3), with $\mathbf{u}$ and $\mathbf{v}$ real, then its real part $\mathbf{u}(t)$ and its imaginary part $\mathbf{v}(t)$ are also solutions of this equation.
>
> *BDP: Theorem 7.4.5*

^thm-30-5

> [!proof]+ Proof
> Substitute $\mathbf{u}(t) + i\mathbf{v}(t)$ for $\mathbf{x}$ in (3):
>
> $$
> \mathbf{x}' - \mathbf{P}(t)\mathbf{x} = \mathbf{u}'(t) - \mathbf{P}(t)\mathbf{u}(t) + i\big(\mathbf{v}'(t) - \mathbf{P}(t)\mathbf{v}(t)\big) = \mathbf{0} . \qquad (17)
> $$
>
> Because $\mathbf{P}(t)$ is real, $\mathbf{u}' - \mathbf{P}\mathbf{u}$ and $\mathbf{v}' - \mathbf{P}\mathbf{v}$ are real vectors, so (17) is the splitting of $\mathbf{x}' - \mathbf{P}\mathbf{x}$ into real and imaginary parts. A complex vector is zero if and only if its real and imaginary parts are both zero. Hence $\mathbf{u}' - \mathbf{P}\mathbf{u} = \mathbf{0}$ and $\mathbf{v}' - \mathbf{P}\mathbf{v} = \mathbf{0}$: $\mathbf{u}$ and $\mathbf{v}$ are solutions of (3).

^pf-30-5

*Uses:* [[§30 Basic Theory of Systems of First-Order Linear Equations#^def-30-1|Def. §30.1]]

> [!remark] Remark: Summary
> 1. Any set of $n$ linearly independent solutions of $\mathbf{x}' = \mathbf{P}(t)\mathbf{x}$ is a fundamental set of solutions (Theorem §30.3 makes "independent at one point" enough).
> 2. Under the conditions of this section, fundamental sets always exist (Theorem §30.4).
> 3. Every solution of $\mathbf{x}' = \mathbf{P}(t)\mathbf{x}$ is a linear combination of any fundamental set of solutions (Theorem §30.2).

^rem-30-1
