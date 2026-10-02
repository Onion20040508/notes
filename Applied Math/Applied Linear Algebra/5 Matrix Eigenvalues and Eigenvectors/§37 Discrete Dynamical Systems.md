---
type: section
subject: "[[Applied Linear Algebra]]"
chapter: 5
section: 37
lay: "5.6"
aliases: ["Lay 5.6"]
tags: [applied-linear-algebra, math235]
---
← [[§36 Complex Eigenvalues]] · ↑ [[· 5 Matrix Eigenvalues and Eigenvectors]] · [[§38 Applications to Differential Equations]] →

*Lay, Section 5.6.*

A discrete dynamical system $\mathbf{x}_{k+1} = A\mathbf{x}_k$ describes a state vector that changes in steps: populations by age class, owls and rats, the distribution of a Markov chain. Writing the initial vector in an eigenvector basis turns the system into independent scalar recursions, $\mathbf{x}_k = c_1\lambda_1^k\mathbf{v}_1 + \cdots + c_n\lambda_n^k\mathbf{v}_n$. The long-term behavior is then read off from the eigenvalues: the eigenvalue of largest absolute value sets the eventual growth rate, and its eigenvector the eventual proportions. In the plane the eigenvalues classify the pictures. The origin is an attractor when both eigenvalues are less than $1$ in absolute value, a repeller when both exceed $1$, and a saddle point otherwise. Complex eigenvalues produce spirals. The section ends with the spotted owl model of the chapter introduction.

Until Example §37.4 we assume that $A$ is diagonalizable, with $n$ linearly independent eigenvectors $\mathbf{v}_1, \ldots, \mathbf{v}_n$ and corresponding eigenvalues $\lambda_1, \ldots, \lambda_n$, arranged so that $|\lambda_1| \ge |\lambda_2| \ge \cdots \ge |\lambda_n|$.

> [!theorem] Theorem §37.1: The Eigenvector Decomposition of a Solution
> Let $A$ be as above. Since $\{\mathbf{v}_1, \ldots, \mathbf{v}_n\}$ is a basis for $\mathbb{R}^n$, any initial vector can be written uniquely as
>
> $$
> \mathbf{x}_0 = c_1\mathbf{v}_1 + \cdots + c_n\mathbf{v}_n , \qquad (1)
> $$
>
> and then the solution of $\mathbf{x}_{k+1} = A\mathbf{x}_k$ is
>
> $$
> \mathbf{x}_k = c_1(\lambda_1)^k\mathbf{v}_1 + \cdots + c_n(\lambda_n)^k\mathbf{v}_n \qquad (k = 0, 1, 2, \ldots) . \qquad (2)
> $$
>
> *Lay: 5.6, Equations (1) and (2)*

^thm-37-1

> [!proof]+ Proof
> The weights in (1) exist and are unique because the $\mathbf{v}_i$ form a basis ([[§26 Coordinate Systems#^thm-26-1|Theorem §26.1]], the Unique Representation Theorem). Since the $\mathbf{v}_i$ are eigenvectors,
>
> $$
> \mathbf{x}_1 = A\mathbf{x}_0 = c_1A\mathbf{v}_1 + \cdots + c_nA\mathbf{v}_n = c_1\lambda_1\mathbf{v}_1 + \cdots + c_n\lambda_n\mathbf{v}_n ,
> $$
>
> and in general, if (2) holds for $k$, then $\mathbf{x}_{k+1} = A\mathbf{x}_k = c_1\lambda_1^k A\mathbf{v}_1 + \cdots + c_n\lambda_n^k A\mathbf{v}_n = c_1\lambda_1^{k+1}\mathbf{v}_1 + \cdots + c_n\lambda_n^{k+1}\mathbf{v}_n$. By induction (2) holds for all $k$ (this is [[§32 Eigenvectors and Eigenvalues#^thm-32-5|Theorem §32.5]] with $n$ terms).

^pf-37-1

*Uses:* [[§32 Eigenvectors and Eigenvalues#^thm-32-5|§32.5]], [[§26 Coordinate Systems#^thm-26-1|§26.1]] (the Unique Representation Theorem)

## A Predator–Prey System

> [!example] Example §37.1: Owls and Wood Rats
> Deep in the redwood forests of California, dusky-footed wood rats provide up to $80\%$ of the diet of the spotted owl, their main predator. Let $\mathbf{x}_k = \begin{bmatrix} O_k \\ R_k \end{bmatrix}$, where $k$ is the time in months, $O_k$ is the number of owls in the region and $R_k$ the number of rats (in thousands). Suppose
>
> $$
> O_{k+1} = (.5)O_k + (.4)R_k, \qquad R_{k+1} = -p \cdot O_k + (1.1)R_k , \qquad (3)
> $$
>
> where $p$ is a positive parameter. With no rats only half of the owls survive each month; with no owls the rats grow by $10\%$ per month; plentiful rats make the owl population rise ($.4R_k$), and $-p \cdot O_k$ counts the rats eaten ($1000p$ is the average number eaten by one owl in one month). Determine the evolution of the system when the predation parameter is $p = .104$. (The model is unrealistic in several respects, but it is a starting point for the nonlinear models of environmental science.)
>
> **Eigenvalues.** The coefficient matrix is $A = \begin{bmatrix} .5 & .4 \\ -.104 & 1.1 \end{bmatrix}$, with $\operatorname{tr} A = 1.6$ and $\det A = .55 + .0416 = .5916$, so $\det(A - \lambda I) = \lambda^2 - 1.6\lambda + .5916 = (\lambda - 1.02)(\lambda - .58)$ (check: $1.02 + .58 = 1.6$, $1.02 \cdot .58 = .5916$). The eigenvalues are $\lambda_1 = 1.02$ and $\lambda_2 = .58$.
>
> **Eigenvectors.** $A\begin{bmatrix} 10 \\ 13 \end{bmatrix} = \begin{bmatrix} 5 + 5.2 \\ -1.04 + 14.3 \end{bmatrix} = \begin{bmatrix} 10.2 \\ 13.26 \end{bmatrix} = 1.02\begin{bmatrix} 10 \\ 13 \end{bmatrix}$ and $A\begin{bmatrix} 5 \\ 1 \end{bmatrix} = \begin{bmatrix} 2.9 \\ .58 \end{bmatrix} = .58\begin{bmatrix} 5 \\ 1 \end{bmatrix}$, so $\mathbf{v}_1 = (10, 13)$ and $\mathbf{v}_2 = (5, 1)$.
>
> **Solution.** Writing $\mathbf{x}_0 = c_1\mathbf{v}_1 + c_2\mathbf{v}_2$, Theorem §37.1 gives, for $k \ge 0$,
>
> $$
> \mathbf{x}_k = c_1(1.02)^k\begin{bmatrix} 10 \\ 13 \end{bmatrix} + c_2(.58)^k\begin{bmatrix} 5 \\ 1 \end{bmatrix} .
> $$
>
> **Long-term behavior.** As $k \to \infty$, $(.58)^k$ rapidly approaches $0$. Assume $c_1 > 0$. Then for all sufficiently large $k$,
>
> $$
> \mathbf{x}_k \approx c_1(1.02)^k\begin{bmatrix} 10 \\ 13 \end{bmatrix}, \qquad (4) \qquad\qquad
> \mathbf{x}_{k+1} \approx c_1(1.02)^{k+1}\begin{bmatrix} 10 \\ 13 \end{bmatrix} = 1.02\,\mathbf{x}_k , \qquad (5)
> $$
>
> with the approximations improving as $k$ increases. By (5), both populations eventually grow by a factor of almost $1.02$ each month, a $2\%$ monthly growth rate. By (4), the entries of $\mathbf{x}_k$ are nearly in the ratio $10$ to $13$: for every $10$ owls there are about $13$ thousand rats.
>
> *Lay: Example 5.6.1*

^ex-37-1

> [!theorem] Proposition §37.2: The Dominant Eigenvalue Determines the Long-Term Behavior
> Let $A$ be diagonalizable as above, with $|\lambda_1| > |\lambda_j|$ for $j = 2, \ldots, n$, and let $\mathbf{x}_0$ be given by (1) with $c_1 \ne 0$. Then, as $k \to \infty$,
>
> $$
> \frac{1}{\lambda_1^k}\,\mathbf{x}_k \to c_1\mathbf{v}_1 \qquad\text{and}\qquad \frac{1}{\lambda_1^k}\big(\mathbf{x}_{k+1} - \lambda_1\mathbf{x}_k\big) \to \mathbf{0} .
> $$
>
> Under Lay's hypotheses, $|\lambda_1| \ge 1$ and $|\lambda_j| < 1$ for $j = 2, \ldots, n$, even the errors themselves tend to zero:
>
> $$
> \mathbf{x}_k - c_1(\lambda_1)^k\mathbf{v}_1 \to \mathbf{0} \qquad\text{and}\qquad \mathbf{x}_{k+1} - \lambda_1\mathbf{x}_k \to \mathbf{0} .
> $$
>
> These limits are the precise meaning of the approximations
>
> $$
> \mathbf{x}_{k+1} \approx \lambda_1\mathbf{x}_k \qquad (6) \qquad\qquad \text{and} \qquad\qquad \mathbf{x}_k \approx c_1(\lambda_1)^k\mathbf{v}_1 \qquad (7)
> $$
>
> for all sufficiently large $k$. By (6), the $\mathbf{x}_k$ eventually grow almost by a factor $\lambda_1$ each step, so $\lambda_1$ determines the eventual growth rate. By (7), for large $k$ the ratio of any two entries of $\mathbf{x}_k$ is nearly the ratio of the corresponding entries of $\mathbf{v}_1$.
>
> *Lay: 5.6 (text after Example 1)*

^prop-37-2

> [!proof]+ Proof
> Dividing (2) by $\lambda_1^k$ (note $\lambda_1 \ne 0$),
>
> $$
> \frac{1}{\lambda_1^k}\,\mathbf{x}_k = c_1\mathbf{v}_1 + c_2\Big(\frac{\lambda_2}{\lambda_1}\Big)^k\mathbf{v}_2 + \cdots + c_n\Big(\frac{\lambda_n}{\lambda_1}\Big)^k\mathbf{v}_n .
> $$
>
> Each ratio satisfies $|\lambda_j/\lambda_1| < 1$, so $(\lambda_j/\lambda_1)^k \to 0$, and the right side tends to $c_1\mathbf{v}_1$. In the same way $\lambda_1^{-k}\mathbf{x}_{k+1} = \lambda_1 \cdot \lambda_1^{-(k+1)}\mathbf{x}_{k+1} \to \lambda_1c_1\mathbf{v}_1$, so $\lambda_1^{-k}(\mathbf{x}_{k+1} - \lambda_1\mathbf{x}_k) \to \lambda_1c_1\mathbf{v}_1 - \lambda_1c_1\mathbf{v}_1 = \mathbf{0}$: the error in (6) is small compared with the size $|\lambda_1|^k$ of $\mathbf{x}_k$.
>
> Under Lay's hypotheses, subtract the first term of (2) instead of dividing:
>
> $$
> \mathbf{x}_k - c_1\lambda_1^k\mathbf{v}_1 = \sum_{j=2}^n c_j\lambda_j^k\mathbf{v}_j \to \mathbf{0}, \qquad \mathbf{x}_{k+1} - \lambda_1\mathbf{x}_k = \sum_{j=2}^n c_j(\lambda_j - \lambda_1)\lambda_j^k\mathbf{v}_j \to \mathbf{0},
> $$
>
> because $|\lambda_j| < 1$ gives $\lambda_j^k \to 0$. (Lay states (6) and (7) as approximations that "can be made as close as desired"; these limits are what that means. The hypothesis $|\lambda_1| \ge 1$ only matters for the interpretation as growth.)

^pf-37-2

*Uses:* [[§37 Discrete Dynamical Systems#^thm-37-1|§37.1]]

The case $\lambda_1 = 1$ is [[§33 The Characteristic Equation#^ex-33-4|Example §33.4]]: there $\mathbf{x}_k$ converges to the steady-state vector $c_1\mathbf{v}_1$. The same estimate, with the scaling done numerically, is the power method of [[§39 Iterative Estimates for Eigenvalues#^thm-39-1|Theorem §39.1]].

## Graphical Description of Solutions

When $A$ is $2 \times 2$, the algebra can be supplemented by a picture of what happens to an initial point $\mathbf{x}_0$ in $\mathbb{R}^2$ as it is transformed repeatedly by $\mathbf{x} \mapsto A\mathbf{x}$.

> [!definition] Definition §37.1: Trajectory; Attractor, Repeller, Saddle Point
> The graph of $\mathbf{x}_0, \mathbf{x}_1, \mathbf{x}_2, \ldots$ is called a **trajectory** of the dynamical system $\mathbf{x}_{k+1} = A\mathbf{x}_k$. The origin is
> - an **attractor** of the system if all trajectories tend toward $\mathbf{0}$;
> - a **repeller** if all solutions except the (constant) zero solution are unbounded and tend away from the origin;
> - a **saddle point** if the origin attracts solutions from some directions and repels them in other directions.
>
> The origin is the only possible attractor or repeller of a *linear* dynamical system; a nonlinear system can have several, and they are classified by the eigenvalues of its Jacobian matrix.
>
> *Lay: 5.6 (text)*

^def-37-1

> [!remark]- Connections
> - ODE version: trajectories and phase portraits of $\mathbf{x}' = A\mathbf{x}$, [[§31 Homogeneous Linear Systems with Constant Coefficients#^def-31-2|331 Def. §31.2]], and asymptotic stability of the equilibrium $\mathbf{0}$, [[§31 Homogeneous Linear Systems with Constant Coefficients#^def-31-1|331 Def. §31.1]]. The last sentence in dimension one: an equilibrium $u^*$ of $u_{n+1} = g(u_n)$ is asymptotically stable if $|g'(u^*)| < 1$ and unstable if $|g'(u^*)| > 1$, [[§12★ First-Order Difference Equations#^lem-12-5|331 Lemma §12.5]].

> [!theorem] Proposition §37.3: The Eigenvalues Classify the Origin
> Let $A$ be a $2 \times 2$ matrix with eigenvalues $\lambda_1$, $\lambda_2$ and linearly independent eigenvectors $\mathbf{v}_1$, $\mathbf{v}_2$, with $|\lambda_1| \ge |\lambda_2|$.
> 1. If $|\lambda_1| < 1$ (both eigenvalues less than $1$ in magnitude), the origin is an attractor. The direction of greatest attraction is the line through $\mathbf{0}$ and $\mathbf{v}_2$, the eigenvector for the eigenvalue of smaller magnitude.
> 2. If $|\lambda_2| > 1$ (both eigenvalues greater than $1$ in magnitude), the origin is a repeller. The direction of greatest repulsion is the line through $\mathbf{0}$ and $\mathbf{v}_1$, the eigenvector for the eigenvalue of larger magnitude.
> 3. If $|\lambda_1| > 1 > |\lambda_2|$, the origin is a saddle point. Trajectories starting on the line through $\mathbf{v}_2$ tend to $\mathbf{0}$; all others are unbounded. The direction of greatest attraction is the line through $\mathbf{v}_2$, and the direction of greatest repulsion is the line through $\mathbf{v}_1$.
>
> *Lay: 5.6 (text with Examples 2–5)*

^prop-37-3

> [!proof]+ Proof
> By Theorem §37.1, $\mathbf{x}_k = c_1\lambda_1^k\mathbf{v}_1 + c_2\lambda_2^k\mathbf{v}_2$, where $(c_1, c_2)$ is the coordinate vector of $\mathbf{x}_0$ in the eigenvector basis; $\mathbf{x}_k$ is unbounded exactly when one of the coefficients $c_i\lambda_i^k$ is unbounded (the coordinates of a vector are bounded exactly when the vector is, since $[\mathbf{x}]_{\mathcal{B}} = P^{-1}\mathbf{x}$ and $\mathbf{x} = P[\mathbf{x}]_{\mathcal{B}}$).
> 1. $|\lambda_i| < 1$ gives $\lambda_i^k \to 0$ for both $i$, so $\mathbf{x}_k \to \mathbf{0}$. The $\mathbf{v}_2$-component decays fastest, since $|\lambda_2|^k \le |\lambda_1|^k$.
> 2. If $\mathbf{x}_0 \ne \mathbf{0}$, some $c_i \ne 0$, and $|c_i\lambda_i^k| = |c_i||\lambda_i|^k \to \infty$. The $\mathbf{v}_1$-component grows fastest.
> 3. If $c_1 = 0$ ($\mathbf{x}_0$ on the line through $\mathbf{v}_2$), then $\mathbf{x}_k = c_2\lambda_2^k\mathbf{v}_2 \to \mathbf{0}$. If $c_1 \ne 0$, then $|c_1\lambda_1^k| \to \infty$ and $\{\mathbf{x}_k\}$ is unbounded.

^pf-37-3

*Uses:* [[§37 Discrete Dynamical Systems#^thm-37-1|§37.1]], [[§37 Discrete Dynamical Systems#^def-37-1|Def. §37.1]]

> [!remark]- Connections
> - ODE version: [[§32 Complex-Valued Eigenvalues#^thm-32-3|331 Thm. §32.3]], the classification of the origin for $\mathbf{x}' = A\mathbf{x}$ (saddle point, node, spiral point, center), where the sign of the real part of each eigenvalue plays the role of $|\lambda|$ compared with $1$. The $1 \times 1$ case $y_{k+1} = \rho y_k$: the solution $\rho^ky_0$ tends to $0$ for every $y_0$ exactly when $|\rho| < 1$, [[§12★ First-Order Difference Equations#^prop-12-1|331 Prop. §12.1]].

> [!example] Example §37.2: Attractor, Repeller and Saddle Point for Diagonal Matrices
> **(a) Attractor.** $A = \begin{bmatrix} .80 & 0 \\ 0 & .64 \end{bmatrix}$ has eigenvalues $.8$ and $.64$ with eigenvectors $\mathbf{v}_1 = (1, 0)$, $\mathbf{v}_2 = (0, 1)$. If $\mathbf{x}_0 = c_1\mathbf{v}_1 + c_2\mathbf{v}_2$, then
>
> $$
> \mathbf{x}_k = c_1(.8)^k\begin{bmatrix} 1 \\ 0 \end{bmatrix} + c_2(.64)^k\begin{bmatrix} 0 \\ 1 \end{bmatrix} .
> $$
>
> Both terms tend to $\mathbf{0}$, but the second faster: trajectories starting on the boundary of the square with corners $(\pm 3, \pm 3)$ approach $\mathbf{0}$ while flattening toward the $x_1$-axis. The direction of greatest attraction is the $x_2$-axis.
>
> **(b) Repeller.** $A = \begin{bmatrix} 1.44 & 0 \\ 0 & 1.2 \end{bmatrix}$ has eigenvalues $1.44$ and $1.2$. If $\mathbf{x}_0 = (c_1, c_2)$, then $\mathbf{x}_k = c_1(1.44)^k\begin{bmatrix} 1 \\ 0 \end{bmatrix} + c_2(1.2)^k\begin{bmatrix} 0 \\ 1 \end{bmatrix}$. Both terms grow, the first faster, so the direction of greatest repulsion is the $x_1$-axis; trajectories starting near $\mathbf{0}$ run away and bend toward the $x_1$-direction.
>
> **(c) Saddle point.** $D = \begin{bmatrix} 2.0 & 0 \\ 0 & 0.5 \end{bmatrix}$ has eigenvalues $2$ and $.5$. If $\mathbf{y}_0 = (c_1, c_2)$, then
>
> $$
> \mathbf{y}_k = c_12^k\begin{bmatrix} 1 \\ 0 \end{bmatrix} + c_2(.5)^k\begin{bmatrix} 0 \\ 1 \end{bmatrix} . \qquad (8)
> $$
>
> If $\mathbf{y}_0$ is on the $x_2$-axis, then $c_1 = 0$ and $\mathbf{y}_k \to \mathbf{0}$. If $\mathbf{y}_0$ is not on the $x_2$-axis, then $c_1 \ne 0$, the first term becomes arbitrarily large, and $\{\mathbf{y}_k\}$ is unbounded. Trajectories starting near the $x_2$-axis first approach the origin and then turn away along the $x_1$-axis.
>
> *Lay: Examples 5.6.2, 5.6.3 and 5.6.4*

^ex-37-2

## Change of Variable

The diagonal case is the general one in disguise. Let $A = PDP^{-1}$ with $P = [\,\mathbf{v}_1 \; \cdots \; \mathbf{v}_n\,]$ and $D$ the diagonal matrix of the corresponding eigenvalues.

> [!theorem] Theorem §37.4: Decoupling by a Change of Variable
> If $\{\mathbf{x}_k\}$ satisfies $\mathbf{x}_{k+1} = A\mathbf{x}_k$ with $A = PDP^{-1}$, then the sequence $\{\mathbf{y}_k\}$ defined by
>
> $$
> \mathbf{y}_k = P^{-1}\mathbf{x}_k, \qquad \text{or equivalently} \qquad \mathbf{x}_k = P\mathbf{y}_k ,
> $$
>
> satisfies $\mathbf{y}_{k+1} = D\mathbf{y}_k$. Writing $y_1(k), \ldots, y_n(k)$ for the entries of $\mathbf{y}_k$,
>
> $$
> \begin{bmatrix} y_1(k+1) \\ y_2(k+1) \\ \vdots \\ y_n(k+1) \end{bmatrix} = \begin{bmatrix} \lambda_1 & 0 & \cdots & 0 \\ 0 & \lambda_2 & & \vdots \\ \vdots & & \ddots & 0 \\ 0 & \cdots & 0 & \lambda_n \end{bmatrix}\begin{bmatrix} y_1(k) \\ y_2(k) \\ \vdots \\ y_n(k) \end{bmatrix},
> $$
>
> that is, $y_i(k + 1) = \lambda_i\,y_i(k)$ for each $i$: the change of variable has **decoupled** the system. The vector $\mathbf{y}_k$ is the coordinate vector of $\mathbf{x}_k$ relative to the eigenvector basis.
>
> *Lay: 5.6 (text, "Change of Variable")*

^thm-37-4

> [!proof]+ Proof
> Substitute $\mathbf{x}_k = P\mathbf{y}_k$ and $A = PDP^{-1}$ into $\mathbf{x}_{k+1} = A\mathbf{x}_k$:
>
> $$
> P\mathbf{y}_{k+1} = AP\mathbf{y}_k = (PDP^{-1})P\mathbf{y}_k = PD\mathbf{y}_k .
> $$
>
> Left-multiplying by $P^{-1}$ gives $\mathbf{y}_{k+1} = D\mathbf{y}_k$. Since $P = P_{\mathcal{B}}$ for the basis $\mathcal{B}$ of columns of $P$, $\mathbf{y}_k = P^{-1}\mathbf{x}_k = [\mathbf{x}_k]_{\mathcal{B}}$.

^pf-37-4

*Uses:* [[§34 Diagonalization#^thm-34-1|§34.1]], [[§26 Coordinate Systems#^prop-26-2|§26.2]] (the change-of-coordinates equation)

The evolution of $y_1(k)$, for example, is unaffected by what happens to $y_2(k), \ldots, y_n(k)$. We can decouple $\mathbf{x}_{k+1} = A\mathbf{x}_k$ by computing in the eigenvector coordinate system; when $n = 2$, this amounts to using graph paper with axes in the directions of the two eigenvectors.

> [!example] Example §37.3: A Saddle Point in Eigenvector Coordinates
> Show that the origin is a saddle point for solutions of $\mathbf{x}_{k+1} = A\mathbf{x}_k$, where $A = \begin{bmatrix} 1.25 & -.75 \\ -.75 & 1.25 \end{bmatrix}$, and find the directions of greatest attraction and greatest repulsion.
>
> $\det(A - \lambda I) = (1.25 - \lambda)^2 - .5625$, which is $0$ when $1.25 - \lambda = \pm .75$: the eigenvalues are $2$ and $.5$. Eigenvectors: $A\begin{bmatrix} 1 \\ -1 \end{bmatrix} = \begin{bmatrix} 2 \\ -2 \end{bmatrix}$ and $A\begin{bmatrix} 1 \\ 1 \end{bmatrix} = \begin{bmatrix} .5 \\ .5 \end{bmatrix}$, so $\mathbf{v}_1 = (1, -1)$ for $\lambda = 2$ and $\mathbf{v}_2 = (1, 1)$ for $\lambda = .5$. Since $|2| > 1$ and $|.5| < 1$, the origin is a saddle point (Proposition §37.3). If $\mathbf{x}_0 = c_1\mathbf{v}_1 + c_2\mathbf{v}_2$, then
>
> $$
> \mathbf{x}_k = c_12^k\mathbf{v}_1 + c_2(.5)^k\mathbf{v}_2 . \qquad (9)
> $$
>
> This looks just like (8) of Example §37.2(c), with $\mathbf{v}_1$ and $\mathbf{v}_2$ in place of the standard basis: by Theorem §37.4, in the coordinates $\mathbf{y} = P^{-1}\mathbf{x}$ the system *is* Example §37.2(c). The direction of greatest repulsion is the line through $\mathbf{0}$ and $\mathbf{v}_1$; if $\mathbf{x}_0$ is on it, $c_2 = 0$ and $\mathbf{x}_k$ moves quickly away from $\mathbf{0}$. The direction of greatest attraction is the line through $\mathbf{v}_2$. The trajectories are the hyperbola-like curves of Example §37.2(c), turned by $45°$ so that their axes are the eigenvector lines $x_2 = -x_1$ and $x_2 = x_1$.
>
> *Lay: Example 5.6.5*

^ex-37-3

![[m235-37-1.svg]]
*Trajectories in the three main cases. (a) Attractor, Example §37.2(a): starting on the square with corners $(\pm 3, \pm 3)$, the points approach $\mathbf{0}$ and flatten toward the $x_1$-axis, because the $x_2$-component decays faster ($.64 < .8$). (b) Saddle point, Example §37.3: points drift toward $\mathbf{0}$ along the attracting eigenvector line through $\mathbf{v}_2 = (1, 1)$ (green) and are then pushed out along the repelling line through $\mathbf{v}_1 = (1, -1)$ (red). (c) Spiral attractor, Example §37.4: complex eigenvalues $.9 \pm .2i$ of modulus $\approx .92 < 1$ make the points turn and spiral inward.*

## Complex Eigenvalues

When a real $2 \times 2$ matrix $A$ has complex eigenvalues, it is not diagonalizable (acting on $\mathbb{R}^2$), but the dynamical system $\mathbf{x}_{k+1} = A\mathbf{x}_k$ is still easy to describe, by [[§36 Complex Eigenvalues#^thm-36-4|Theorem §36.4]]: $A^k = PC^kP^{-1}$ with $C^k = |\lambda|^k R_{k\varphi}$ ([[§36 Complex Eigenvalues#^ex-36-5|Example §36.5]]). If the complex eigenvalues have absolute value $1$, the iterates of $\mathbf{x}_0$ go around the origin on an ellipse ([[§36 Complex Eigenvalues#^ex-36-3|Example §36.3]]). If their absolute value is greater than $1$, the origin is a repeller and the iterates spiral outward; if it is less than $1$, the origin is an attractor and the iterates spiral inward.

> [!example] Example §37.4: A Spiral Attractor
> $A = \begin{bmatrix} .8 & .5 \\ -.1 & 1.0 \end{bmatrix}$ has $\operatorname{tr} A = 1.8$ and $\det A = .8 + .05 = .85$, so its characteristic polynomial is $\lambda^2 - 1.8\lambda + .85$, with roots
>
> $$
> \lambda = \frac{1.8 \pm \sqrt{3.24 - 3.4}}{2} = .9 \pm \frac{\sqrt{-.16}}{2} = .9 \pm .2i .
> $$
>
> For $\lambda = .9 + .2i$, the first row of $A - \lambda I$ is $(-.1 - .2i,\ .5)$, and $(1 - 2i, 1)$ satisfies it: $(-.1 - .2i)(1 - 2i) + .5 = (-.1 + .2i - .2i - .4) + .5 = 0$. So the eigenvectors are $\begin{bmatrix} 1 \mp 2i \\ 1 \end{bmatrix}$ for $.9 \pm .2i$. Since $|\lambda|^2 = .81 + .04 = .85 < 1$, $|\lambda| \approx .92$: every trajectory spirals inward to the origin, turning by $\arg\lambda = \tan^{-1}(.2/.9) \approx 12.5°$ per step in the coordinates of $\operatorname{Re}\mathbf{v}$, $\operatorname{Im}\mathbf{v}$ and shrinking by the factor $.92$. Lay plots the trajectories from $(0, 2.5)$, $(3, 0)$ and $(0, -2.5)$.
>
> *Lay: Example 5.6.6*

^ex-37-4

> [!remark]- Connections
> - ODE version: for $\mathbf{x}' = A\mathbf{x}$, complex eigenvalues $\lambda \pm i\mu$ make the origin a spiral point, attracting when $\lambda < 0$, or a center when $\lambda = 0$, [[§32 Complex-Valued Eigenvalues#^def-32-1|331 Def. §32.1]]; a worked spiral sink, [[§32 Complex-Valued Eigenvalues#^ex-32-1|331 Ex. §32.1]].

## Survival of the Spotted Owls

> [!example] Example §37.5: The Spotted Owl Model
> In the chapter introduction, the spotted owl population of the Willow Creek area of California was modeled by $\mathbf{x}_{k+1} = A\mathbf{x}_k$, where $\mathbf{x}_k = (j_k, s_k, a_k)$ lists the numbers of females at time $k$ (years) in the juvenile, subadult and adult stages, and
>
> $$
> A = \begin{bmatrix} 0 & 0 & .33 \\ .18 & 0 & 0 \\ 0 & .71 & .94 \end{bmatrix} . \qquad (10)
> $$
>
> (Each year: adults produce $.33$ juvenile females each; $18\%$ of juveniles become subadults; $71\%$ of subadults and $94\%$ of adults survive as adults.)
>
> **(a) The model predicts extinction.** A computer gives the eigenvalues $\lambda_1 \approx .98$, $\lambda_2 \approx -.02 + .21i$ and $\lambda_3 \approx -.02 - .21i$. All three are less than $1$ in magnitude, since $|\lambda_2|^2 = |\lambda_3|^2 \approx (-.02)^2 + (.21)^2 = .0445$. Let $A$ act on $\mathbb{C}^3$. The three eigenvalues are distinct, so the corresponding eigenvectors $\mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3$ are linearly independent ([[§32 Eigenvectors and Eigenvalues#^thm-32-3|Theorem §32.3]], valid in $\mathbb{C}^3$) and form a basis for $\mathbb{C}^3$. So the general solution, with vectors in $\mathbb{C}^3$, is
>
> $$
> \mathbf{x}_k = c_1(\lambda_1)^k\mathbf{v}_1 + c_2(\lambda_2)^k\mathbf{v}_2 + c_3(\lambda_3)^k\mathbf{v}_3 . \qquad (11)
> $$
>
> If $\mathbf{x}_0$ is real, then so is every $\mathbf{x}_k = A^k\mathbf{x}_0$, because $A$ is real, even though it is written in (11) as a sum of complex vectors. Each term on the right of (11) tends to $\mathbf{0}$, because $|\lambda_i| < 1$. Therefore $\mathbf{x}_k \to \mathbf{0}$: the model predicts that the spotted owls will eventually all perish.
>
> **(b) A better search survival rate.** The entry $.18$ comes from: $60\%$ of juveniles live to leave the nest, but only $30\%$ of those survive the search for a new home range ($.6 \times .3 = .18$); search survival is lowered by clear-cut areas. Suppose instead the search survival rate is $50\%$, so the $(2, 1)$-entry of $A$ is $.6 \times .5 = .3$. Now the eigenvalues are approximately $\lambda_1 = 1.01$, $\lambda_2 = -.03 + .26i$, $\lambda_3 = -.03 - .26i$, and an eigenvector for $\lambda_1$ is approximately $\mathbf{v}_1 = (10, 3, 31)$. Equation (11) becomes
>
> $$
> \mathbf{x}_k = c_1(1.01)^k\mathbf{v}_1 + c_2(-.03 + .26i)^k\mathbf{v}_2 + c_3(-.03 - .26i)^k\mathbf{v}_3 .
> $$
>
> The last two terms tend to $\mathbf{0}$, so $\mathbf{x}_k$ becomes more and more like the real vector $c_1(1.01)^k\mathbf{v}_1$, and Proposition §37.2 applies. It can be shown that $c_1 > 0$ when the entries of $\mathbf{x}_0$ are nonnegative (and $\mathbf{x}_0 \ne \mathbf{0}$; compare [[§32 Eigenvectors and Eigenvalues#^rem-32-2|Remark: The Perron–Frobenius Theorem]]). So the owl population grows slowly, with long-term growth rate $1.01$ per year, and by (7) its eventual distribution by life stages is given by $\mathbf{v}_1$: for every $31$ adults, about $10$ juveniles and $3$ subadults.
>
> *(Numerical check: the eigenvalues of (10) are $.9836$ and $-.0218 \pm .2059i$; with the entry $.3$ they are $1.0090$ and $-.0345 \pm .2617i$, and $\mathbf{v}_1 \approx (10, 2.97, 30.58)$.)*
>
> *Lay: 5.6 (text, "Survival of the Spotted Owls"); Example 5.6.7*

^ex-37-5
