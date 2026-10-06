---
type: section
subject: "[[Applied Linear Algebra]]"
chapter: 5
section: 47
lay: "5.8"
aliases: ["Lay 5.8"]
tags: [applied-linear-algebra, math235]
---
← [[§46 Applications to Differential Equations]] · ↑ [[· 5 Matrix Eigenvalues and Eigenvectors]] · [[§48 The Matrix with Rows (1, 2) and (4, 3)]] →

*Lay, Section 5.8.*

In scientific applications eigenvalues are seldom known exactly, and a close numerical approximation is usually enough; often only the largest eigenvalue is needed. The power method estimates a strictly dominant eigenvalue and an eigenvector for it, by repeatedly multiplying a vector by $A$ and rescaling. It works for the same reason as the long-term analysis of dynamical systems in [[§45 Discrete Dynamical Systems|§45]]: the component along the dominant eigenvector outgrows all the others. The inverse power method applies the same idea to $(A - \alpha I)^{-1}$. Given a rough estimate $\alpha$, it converges quickly to the eigenvalue nearest to $\alpha$.

## The Power Method

> [!definition] Definition §57.1: Strictly Dominant Eigenvalue
> An eigenvalue $\lambda_1$ of an $n \times n$ matrix $A$ is **strictly dominant** if it is larger in absolute value than all the other eigenvalues: $|\lambda_1| > |\lambda_j|$ for every eigenvalue $\lambda_j \ne \lambda_1$.
>
> *Lay: 5.8 (text)*

^def-47-1

Assume for simplicity that $A$ is diagonalizable, with a basis of eigenvectors $\mathbf{v}_1, \ldots, \mathbf{v}_n$ whose eigenvalues decrease in size, the strictly dominant one first:

$$
|\lambda_1| > |\lambda_2| \ge |\lambda_3| \ge \cdots \ge |\lambda_n| . \qquad (1)
$$

> [!theorem] Theorem §57.1: Powers Line Up with the Dominant Eigenvector
> Under assumption (1), let $\mathbf{x} = c_1\mathbf{v}_1 + \cdots + c_n\mathbf{v}_n$ with $c_1 \ne 0$. Then
>
> $$
> (\lambda_1)^{-k}A^k\mathbf{x} \to c_1\mathbf{v}_1 \qquad \text{as } k \to \infty . \qquad (3)
> $$
>
> So for large $k$ a scalar multiple of $A^k\mathbf{x}$ points almost in the direction of the eigenvector $c_1\mathbf{v}_1$, and $A^k\mathbf{x}$ itself points almost in the direction of $\mathbf{v}_1$ or $-\mathbf{v}_1$. More precisely, the angle between the line through $\mathbf{0}$ and $A^k\mathbf{x}$ and the eigenspace line through $\mathbf{v}_1$ goes to zero.
>
> *Lay: 5.8, Equations (2) and (3)*

^thm-47-1

> [!proof]+ Proof
> As in [[§45 Discrete Dynamical Systems#^thm-45-1|Theorem §45.1]], $A^k\mathbf{x} = c_1(\lambda_1)^k\mathbf{v}_1 + c_2(\lambda_2)^k\mathbf{v}_2 + \cdots + c_n(\lambda_n)^k\mathbf{v}_n$. Dividing by $(\lambda_1)^k$ (note $\lambda_1 \ne 0$, being strictly larger in absolute value than $|\lambda_2| \ge 0$),
>
> $$
> \frac{1}{(\lambda_1)^k}A^k\mathbf{x} = c_1\mathbf{v}_1 + c_2\Big(\frac{\lambda_2}{\lambda_1}\Big)^k\mathbf{v}_2 + \cdots + c_n\Big(\frac{\lambda_n}{\lambda_1}\Big)^k\mathbf{v}_n \qquad (k = 1, 2, \ldots) . \qquad (2)
> $$
>
> By (1), the fractions $\lambda_2/\lambda_1, \ldots, \lambda_n/\lambda_1$ are all less than $1$ in magnitude, so their powers go to zero, and (3) follows. Multiplying a vector by a nonzero scalar does not change the line it spans, so the line through $A^k\mathbf{x}$ is the line through $(\lambda_1)^{-k}A^k\mathbf{x}$, which tends to the line through $c_1\mathbf{v}_1 \ne \mathbf{0}$.

^pf-47-1

*Uses:* [[§45 Discrete Dynamical Systems#^thm-45-1|§45.1]], [[§47 Iterative Estimates for Eigenvalues#^def-47-1|Def. §47.1]]

> [!example] Example §57.1: Directions of the Powers
> Let $A = \begin{bmatrix} 1.8 & .8 \\ .2 & 1.2 \end{bmatrix}$, $\mathbf{v}_1 = \begin{bmatrix} 4 \\ 1 \end{bmatrix}$ and $\mathbf{x} = \begin{bmatrix} -.5 \\ 1 \end{bmatrix}$. The eigenvalues of $A$ are $2$ and $1$ ($\operatorname{tr} A = 3$, $\det A = 2.16 - .16 = 2$), and the eigenspace for $\lambda_1 = 2$ is the line through $\mathbf{0}$ and $\mathbf{v}_1$: $A\mathbf{v}_1 = (7.2 + .8,\ .8 + 1.2) = (8, 2) = 2\mathbf{v}_1$. Compute $A^k\mathbf{x}$ for $k = 0, \ldots, 8$:
>
> $$
> A\mathbf{x} = \begin{bmatrix} -.9 + .8 \\ -.1 + 1.2 \end{bmatrix} = \begin{bmatrix} -.1 \\ 1.1 \end{bmatrix}, \qquad
> A^2\mathbf{x} = A(A\mathbf{x}) = \begin{bmatrix} -.18 + .88 \\ -.02 + 1.32 \end{bmatrix} = \begin{bmatrix} .7 \\ 1.3 \end{bmatrix}, \qquad
> A^3\mathbf{x} = \begin{bmatrix} 1.26 + 1.04 \\ .14 + 1.56 \end{bmatrix} = \begin{bmatrix} 2.3 \\ 1.7 \end{bmatrix},
> $$
>
> and so on:
>
> | $k$ | $0$ | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ | $7$ | $8$ |
> |---|---|---|---|---|---|---|---|---|---|
> | $A^k\mathbf{x}$ | $(-.5,\ 1)$ | $(-.1,\ 1.1)$ | $(.7,\ 1.3)$ | $(2.3,\ 1.7)$ | $(5.5,\ 2.5)$ | $(11.9,\ 4.1)$ | $(24.7,\ 7.3)$ | $(50.3,\ 13.7)$ | $(101.5,\ 26.5)$ |
>
> The vectors grow, but their directions are what matters: the ratio of the entries, $101.5/26.5 \approx 3.83$ at $k = 8$, approaches $4$, the ratio for $\mathbf{v}_1 = (4, 1)$. The lines through $\mathbf{0}$ and $A^k\mathbf{x}$ approach the eigenspace line. Exactly: $A - I = \begin{bmatrix} .8 & .8 \\ .2 & .2 \end{bmatrix}$ gives the eigenvector $\mathbf{v}_2 = (1, -1)$ for $\lambda_2 = 1$, and $\mathbf{x} = \frac{1}{10}\mathbf{v}_1 - \frac{9}{10}\mathbf{v}_2$, so $A^k\mathbf{x} = \frac{2^k}{10}\mathbf{v}_1 - \frac{9}{10}\mathbf{v}_2$; at $k = 8$ this is $(102.4 - .9,\ 25.6 + .9) = (101.5, 26.5)$.
>
> *Lay: Example 5.8.1*

^ex-47-1

![[m235-39-1.svg]]
*[[§47 Iterative Estimates for Eigenvalues#^ex-47-1|Example §47.1]]: the vectors $\mathbf{x}, A\mathbf{x}, \ldots, A^4\mathbf{x}$ (dots) and the lines through $\mathbf{0}$ and $A^k\mathbf{x}$ for $k \le 7$ (gray), which close in on the eigenspace line through $\mathbf{v}_1 = (4, 1)$ (blue). The component $-\frac{9}{10}\mathbf{v}_2$ stays fixed while the $\mathbf{v}_1$-component doubles at each step.*

The vectors $(\lambda_1)^{-k}A^k\mathbf{x}$ in (3) converge, but we cannot form them, because $\lambda_1$ is unknown. Instead, scale each $A^k\mathbf{x}$ so that its largest entry is $1$. The resulting sequence $\{\mathbf{x}_k\}$ converges to a multiple of $\mathbf{v}_1$ whose largest entry is $1$. And when $\mathbf{x}_k$ is close to an eigenvector for $\lambda_1$, $A\mathbf{x}_k$ is close to $\lambda_1\mathbf{x}_k$, so its entry of largest absolute value is close to $\lambda_1 \cdot 1$. (Lay omits careful proofs of these two statements.)

> [!remark] Remark: Method — The Power Method for Estimating a Strictly Dominant Eigenvalue
> 1. Select an initial vector $\mathbf{x}_0$ whose largest entry is $1$.
> 2. For $k = 0, 1, \ldots$:
>    - a. Compute $A\mathbf{x}_k$.
>    - b. Let $\mu_k$ be an entry in $A\mathbf{x}_k$ whose absolute value is as large as possible.
>    - c. Compute $\mathbf{x}_{k+1} = (1/\mu_k)A\mathbf{x}_k$.
> 3. For almost all choices of $\mathbf{x}_0$, the sequence $\{\mu_k\}$ approaches the dominant eigenvalue, and the sequence $\{\mathbf{x}_k\}$ approaches a corresponding eigenvector.
>
> *Lay: 5.8, boxed algorithm*

^rem-47-1

> [!example] Example §57.2: The Power Method
> Apply the power method to $A = \begin{bmatrix} 6 & 5 \\ 1 & 2 \end{bmatrix}$ with $\mathbf{x}_0 = \begin{bmatrix} 0 \\ 1 \end{bmatrix}$. Stop when $k = 5$, and estimate the dominant eigenvalue and a corresponding eigenvector.
>
> Compute $A\mathbf{x}_0$ and its largest entry $\mu_0$, scale by $1/\mu_0$, and repeat:
>
> $$
> A\mathbf{x}_0 = \begin{bmatrix} 5 \\ 2 \end{bmatrix}, \ \mu_0 = 5; \qquad
> \mathbf{x}_1 = \frac15\begin{bmatrix} 5 \\ 2 \end{bmatrix} = \begin{bmatrix} 1 \\ .4 \end{bmatrix}, \ A\mathbf{x}_1 = \begin{bmatrix} 6 + 2 \\ 1 + .8 \end{bmatrix} = \begin{bmatrix} 8 \\ 1.8 \end{bmatrix}, \ \mu_1 = 8;
> $$
>
> $$
> \mathbf{x}_2 = \frac18\begin{bmatrix} 8 \\ 1.8 \end{bmatrix} = \begin{bmatrix} 1 \\ .225 \end{bmatrix}, \ A\mathbf{x}_2 = \begin{bmatrix} 6 + 1.125 \\ 1 + .45 \end{bmatrix} = \begin{bmatrix} 7.125 \\ 1.450 \end{bmatrix}, \ \mu_2 = 7.125 .
> $$
>
> Continuing (with a computer, 16-digit accuracy):
>
> | $k$ | $0$ | $1$ | $2$ | $3$ | $4$ | $5$ |
> |---|---|---|---|---|---|---|
> | $\mathbf{x}_k$ | $(0,\ 1)$ | $(1,\ .4)$ | $(1,\ .225)$ | $(1,\ .2035)$ | $(1,\ .2005)$ | $(1,\ .20007)$ |
> | $A\mathbf{x}_k$ | $(5,\ 2)$ | $(8,\ 1.8)$ | $(7.125,\ 1.450)$ | $(7.0175,\ 1.4070)$ | $(7.0025,\ 1.4010)$ | $(7.00036,\ 1.40014)$ |
> | $\mu_k$ | $5$ | $8$ | $7.125$ | $7.0175$ | $7.0025$ | $7.00036$ |
>
> The evidence strongly suggests that $\{\mathbf{x}_k\}$ approaches $(1, .2)$ and $\{\mu_k\}$ approaches $7$. This is easily verified:
>
> $$
> A\begin{bmatrix} 1 \\ .2 \end{bmatrix} = \begin{bmatrix} 6 + 1 \\ 1 + .4 \end{bmatrix} = \begin{bmatrix} 7 \\ 1.4 \end{bmatrix} = 7\begin{bmatrix} 1 \\ .2 \end{bmatrix} .
> $$
>
> The convergence is fast because the other eigenvalue is much smaller: $\lambda_2 = \operatorname{tr} A - 7 = 1$, so the error shrinks roughly like $(1/7)^k$.
>
> *Lay: Example 5.8.2*

^ex-47-2

> [!remark] Remark: Speed and Failure
> The rate of convergence depends on the ratio $|\lambda_2/\lambda_1|$: in (2) the vector $c_2(\lambda_2/\lambda_1)^k\mathbf{v}_2$ is the main source of error when a scaled $A^k\mathbf{x}$ is used to estimate $c_1\mathbf{v}_1$ (the other fractions $|\lambda_j/\lambda_1|$ are likely smaller). If $|\lambda_2/\lambda_1|$ is close to $1$, $\{\mu_k\}$ and $\{\mathbf{x}_k\}$ can converge very slowly, and other methods may be preferred.
>
> There is a slight chance that the initial vector has no component in the $\mathbf{v}_1$ direction ($c_1 = 0$). But rounding errors in the computation of the $\mathbf{x}_k$ are likely to create a small component in that direction, and then the $\mathbf{x}_k$ start to converge to a multiple of $\mathbf{v}_1$.
>
> *Lay: 5.8 (text)*

^rem-47-2

## The Inverse Power Method

This method approximates *any* eigenvalue, provided a good initial estimate $\alpha$ of it is known. The idea is to apply the power method to $B = (A - \alpha I)^{-1}$.

> [!theorem] Proposition §57.2: Eigenvalues of (A − αI)⁻¹
> Let $A$ be $n \times n$ and $\alpha$ a scalar that is not an eigenvalue of $A$. If the eigenvalues of $A$ are $\lambda_1, \ldots, \lambda_n$, then the eigenvalues of $B = (A - \alpha I)^{-1}$ are
>
> $$
> \frac{1}{\lambda_1 - \alpha}, \quad \frac{1}{\lambda_2 - \alpha}, \quad \ldots, \quad \frac{1}{\lambda_n - \alpha},
> $$
>
> and the corresponding eigenvectors are the same as those for $A$.
>
> *Lay: 5.8 (text) and Exercises 15–16*

^prop-47-2

> [!proof]+ Proof
> $A - \alpha I$ is invertible because $\alpha$ is not an eigenvalue ([[§41 The Characteristic Equation#^thm-41-2|Theorem §41.2]] applied to $A - \alpha I$: $0$ is not an eigenvalue of $A - \alpha I$). If $A\mathbf{v} = \lambda\mathbf{v}$ with $\mathbf{v} \ne \mathbf{0}$, then $(A - \alpha I)\mathbf{v} = (\lambda - \alpha)\mathbf{v}$ with $\lambda - \alpha \ne 0$. Apply $B = (A - \alpha I)^{-1}$ to both sides and divide by $\lambda - \alpha$:
>
> $$
> B\mathbf{v} = \frac{1}{\lambda - \alpha}\mathbf{v} .
> $$
>
> Conversely, if $B\mathbf{v} = \mu\mathbf{v}$ with $\mathbf{v} \ne \mathbf{0}$, then $\mu \ne 0$ ($B$ is invertible), and applying $A - \alpha I$ gives $\mathbf{v} = \mu(A - \alpha I)\mathbf{v}$, so $A\mathbf{v} = (\alpha + 1/\mu)\mathbf{v}$: every eigenvalue of $B$ arises this way, $\mu = 1/(\lambda - \alpha)$ with $\lambda = \alpha + 1/\mu$.

^pf-47-2

*Uses:* [[§41 The Characteristic Equation#^thm-41-2|§41.2]], [[§40 Eigenvectors and Eigenvalues#^def-40-1|Def. §40.1]]

Suppose, for example, that $\alpha$ is closer to $\lambda_2$ than to the other eigenvalues of $A$. Then $1/(\lambda_2 - \alpha)$ is a strictly dominant eigenvalue of $B$. If $\alpha$ is really close to $\lambda_2$, then $1/(\lambda_2 - \alpha)$ is much larger than the other eigenvalues of $B$, and the power method for $B$ converges very rapidly, for almost all choices of $\mathbf{x}_0$. If $\nu_k$ estimates $1/(\lambda - \alpha)$, then $\alpha + 1/\nu_k$ estimates $\lambda$.

> [!remark] Remark: Method — The Inverse Power Method for Estimating an Eigenvalue λ of A
> 1. Select an initial estimate $\alpha$ sufficiently close to $\lambda$.
> 2. Select an initial vector $\mathbf{x}_0$ whose largest entry is $1$.
> 3. For $k = 0, 1, \ldots$:
>    - a. Solve $(A - \alpha I)\mathbf{y}_k = \mathbf{x}_k$ for $\mathbf{y}_k$.
>    - b. Let $\mu_k$ be an entry in $\mathbf{y}_k$ whose absolute value is as large as possible.
>    - c. Compute $\nu_k = \alpha + (1/\mu_k)$.
>    - d. Compute $\mathbf{x}_{k+1} = (1/\mu_k)\mathbf{y}_k$.
> 4. For almost all choices of $\mathbf{x}_0$, the sequence $\{\nu_k\}$ approaches the eigenvalue $\lambda$ of $A$, and the sequence $\{\mathbf{x}_k\}$ approaches a corresponding eigenvector.
>
> The matrix $B = (A - \alpha I)^{-1}$ does not appear: instead of computing $(A - \alpha I)^{-1}\mathbf{x}_k$, it is better to solve $(A - \alpha I)\mathbf{y}_k = \mathbf{x}_k$. Since this system must be solved for each $k$ with the same coefficient matrix, an LU factorization of $A - \alpha I$ ([[§18 Matrix Factorizations#^def-18-2|Definition §18.2]]; [[§18 Matrix Factorizations#^rem-18-1|§18, Remark: Method — Solving Ax = b with an LU Factorization]]) speeds up the process. If no estimate is available for the smallest eigenvalue, take $\alpha = 0$; this works reasonably well if the smallest eigenvalue is much closer to zero than to the others.
>
> *Lay: 5.8, boxed algorithm and text*

^rem-47-3

> [!example] Example §57.3: The Smallest Eigenvalue by the Inverse Power Method
> Suppose $21$, $3.3$ and $1.9$ are estimates for the eigenvalues of
>
> $$
> A = \begin{bmatrix} 10 & -8 & -4 \\ -8 & 13 & 4 \\ -4 & 5 & 4 \end{bmatrix} .
> $$
>
> Find the smallest eigenvalue, accurate to six decimal places.
>
> The two smallest eigenvalues seem close together, so use the inverse power method with $\alpha = 1.9$: $\mathbf{y}_k = (A - 1.9I)^{-1}\mathbf{x}_k$, $\mu_k$ the largest entry of $\mathbf{y}_k$, $\nu_k = 1.9 + 1/\mu_k$, $\mathbf{x}_{k+1} = (1/\mu_k)\mathbf{y}_k$, starting from $\mathbf{x}_0 = (1, 1, 1)$. A computer gives:
>
> | $k$ | $0$ | $1$ | $2$ | $3$ | $4$ |
> |---|---|---|---|---|---|
> | $\mathbf{x}_k$ | $(1,\ 1,\ 1)$ | $(.5736,\ .0646,\ 1)$ | $(.5054,\ .0045,\ 1)$ | $(.5004,\ .0003,\ 1)$ | $(.50003,\ .00002,\ 1)$ |
> | $\mathbf{y}_k$ | $(4.45,\ .50,\ 7.76)$ | $(5.0131,\ .0442,\ 9.9197)$ | $(5.0012,\ .0031,\ 9.9949)$ | $(5.0001,\ .0002,\ 9.9996)$ | $(5.000006,\ .000015,\ 9.999975)$ |
> | $\mu_k$ | $7.76$ | $9.9197$ | $9.9949$ | $9.9996$ | $9.999975$ |
> | $\nu_k$ | $2.03$ | $2.0008$ | $2.00005$ | $2.000004$ | $2.0000002$ |
>
> The initial estimate was fairly good, and the sequence converged quickly: the smallest eigenvalue is $2$ (exactly, as one checks: $A\begin{bmatrix} .5 \\ 0 \\ 1 \end{bmatrix} = \begin{bmatrix} 5 - 4 \\ -4 + 4 \\ -2 + 4 \end{bmatrix} = \begin{bmatrix} 1 \\ 0 \\ 2 \end{bmatrix} = 2\begin{bmatrix} .5 \\ 0 \\ 1 \end{bmatrix}$), and $\mathbf{x}_k \to (.5, 0, 1)$ is an eigenvector. Here $1/(2 - 1.9) = 10$ is the dominant eigenvalue of $B$, and the next one is $1/(3.32 - 1.9) \approx .70$, a ratio of about $.07$, which explains the speed. (The other eigenvalues are $\approx 21.68$ and $\approx 3.32$.)
>
> *Lay: Example 5.8.3*

^ex-47-3

> [!remark] Remark: Beyond These Methods
> The power and inverse power methods are practical for many simple situations and introduce the problem of eigenvalue estimation. A more robust and widely used iterative method is the **QR algorithm**, the heart of MATLAB's `eig(A)`; it is built on similarity transformations ([[§41 The Characteristic Equation#^thm-41-6|Theorem §41.6]]). To judge whether a given $\mathbf{x}$ is a good approximate eigenvector, compute $A\mathbf{x}$ and compare it with multiples of $\mathbf{x}$: if the entrywise ratios $(A\mathbf{x})_i/x_i$ are nearly equal, their common value estimates the eigenvalue (Lay's Practice Problem).
>
> *Lay: 5.8 (text) and Practice Problem*

^rem-47-4
