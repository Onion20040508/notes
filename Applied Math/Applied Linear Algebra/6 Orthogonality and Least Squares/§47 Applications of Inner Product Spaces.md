---
type: section
subject: "[[Applied Linear Algebra]]"
chapter: 6
section: 47
lay: "6.8"
aliases: ["Lay 6.8"]
tags: [applied-linear-algebra, math235]
---
← [[§46 Inner Product Spaces]] · ↑ [[· 6 Orthogonality and Least Squares]] · [[§48★ Diagonalization of Symmetric Matrices]] →

*Lay, Section 6.8.*

Three applications show what the inner products of [[§46 Inner Product Spaces|§46]] are for. *Weighted least squares* replaces the dot product of $\mathbb{R}^n$ by a weighted one, so that reliable measurements count more; it reduces to an ordinary least-squares problem after rescaling the rows. *Trend analysis* fits data with orthogonal polynomials for an evaluation inner product, so that the linear, quadratic and cubic trends come out as separate coefficients. *Fourier approximation* projects a function in $C[0, 2\pi]$ onto the span of $1, \cos t, \sin t, \ldots, \cos nt, \sin nt$, which are orthogonal for the integral inner product. In all three the answer is an orthogonal projection, computed with the formulas of Chapter 6.

## Weighted Least-Squares

> [!definition] Definition §47.1: Weighted Sum of Squares for Error
> Let $\mathbf{y} \in \mathbb{R}^n$ be a vector of observations $y_1, \ldots, y_n$, approximated by a vector $\hat{\mathbf{y}}$ (with entries $\hat y_1, \ldots, \hat y_n$) from a specified subspace of $\mathbb{R}^n$. The **sum of the squares for error** is
>
> $$
> \operatorname{SS(E)} = (y_1 - \hat y_1)^2 + \cdots + (y_n - \hat y_n)^2 = \|\mathbf{y} - \hat{\mathbf{y}}\|^2 .
> $$
>
> If the measurements are not equally reliable, assign **weights** $w_1^2, \ldots, w_n^2$ (positive, larger for more reliable measurements). The **weighted sum of the squares for error** is
>
> $$
> \text{weighted } \operatorname{SS(E)} = w_1^2(y_1 - \hat y_1)^2 + \cdots + w_n^2(y_n - \hat y_n)^2 .
> $$
>
> It is the square of the length of $\mathbf{y} - \hat{\mathbf{y}}$ for the weighted inner product $\langle \mathbf{x}, \mathbf{y}\rangle = w_1^2x_1y_1 + \cdots + w_n^2x_ny_n$, as in [[§46 Inner Product Spaces#^ex-46-1|Example §46.1]].
>
> *Lay: 6.8 (text), Equations (1) and (2)*

^def-47-1

> [!theorem] Proposition §47.1: Weighted Least Squares as Ordinary Least Squares
> Let $W$ be the $n \times n$ diagonal matrix with positive diagonal entries $w_1, \ldots, w_n$. For an $n \times k$ matrix $A$, a vector $\hat{\mathbf{x}}$ minimizes the weighted SS(E) of $A\mathbf{x}$ as an approximation to $\mathbf{y}$ if and only if $\hat{\mathbf{x}}$ is an (ordinary) least-squares solution of
>
> $$
> WA\mathbf{x} = W\mathbf{y}, \qquad\text{that is, a solution of}\qquad (WA)^TWA\mathbf{x} = (WA)^TW\mathbf{y} .
> $$
>
> *Lay: 6.8 (text)*

^prop-47-1

> [!proof]+ Proof
> Left multiplication by $W$ multiplies entry $j$ by $w_j$: $W\mathbf{y} = (w_1y_1, \ldots, w_ny_n)$, and likewise $W\hat{\mathbf{y}}$. The $j$th term of the weighted SS(E) is
>
> $$
> w_j^2(y_j - \hat y_j)^2 = (w_jy_j - w_j\hat y_j)^2,
> $$
>
> so the weighted SS(E) equals $\|W\mathbf{y} - W\hat{\mathbf{y}}\|^2$, an ordinary squared length in $\mathbb{R}^n$. With $\hat{\mathbf{y}} = A\mathbf{x}$ this is $\|W\mathbf{y} - WA\mathbf{x}\|^2$, and minimizing it over $\mathbf{x}$ is, by definition, finding a least-squares solution of $WA\mathbf{x} = W\mathbf{y}$. By [[§44 Least-Squares Problems#^thm-44-1|Theorem §44.1]] these are the solutions of the normal equations for this system.

^pf-47-1

*Uses:* [[§44 Least-Squares Problems#^def-44-1|Def. §44.1]], [[§44 Least-Squares Problems#^thm-44-1|§44.1]]

> [!remark]- Remark: Choosing the Weights
> The measurements for the North American Datum (the chapter's motivating least-squares problem) were made over 140 years and are far from equally reliable, so they were weighted. In statistical terms: if the errors in measuring the $y_i$ are independent random variables with mean $0$ and variances $\sigma_1^2, \ldots, \sigma_n^2$, the appropriate weights are $w_i^2 = 1/\sigma_i^2$. The larger the variance of the error, the smaller the weight. Weighting all points by a common factor does not change the solution, since it multiplies both sides of the normal equations by the square of that factor.

^rem-47-1

> [!example] Example §47.1: A Weighted Least-Squares Line
> Find the least-squares line $y = \beta_0 + \beta_1x$ for the data $(-2, 3)$, $(-1, 5)$, $(0, 5)$, $(1, 4)$, $(2, 3)$, if the errors in measuring the $y$-values of the last two points are greater than for the others, so that these two points are weighted half as much as the rest.
>
> **Set-up.** As in [[§45 Applications to Linear Models#^prop-45-1|Proposition §45.1]],
>
> $$
> X = \begin{bmatrix} 1 & -2 \\ 1 & -1 \\ 1 & 0 \\ 1 & 1 \\ 1 & 2 \end{bmatrix}, \qquad \boldsymbol\beta = \begin{bmatrix} \beta_0 \\ \beta_1 \end{bmatrix}, \qquad \mathbf{y} = \begin{bmatrix} 3 \\ 5 \\ 5 \\ 4 \\ 3 \end{bmatrix} .
> $$
>
> Take $W$ with diagonal entries $2, 2, 2, 1, 1$; left multiplication by $W$ scales the rows:
>
> $$
> WX = \begin{bmatrix} 2 & -4 \\ 2 & -2 \\ 2 & 0 \\ 1 & 1 \\ 1 & 2 \end{bmatrix}, \qquad W\mathbf{y} = \begin{bmatrix} 6 \\ 10 \\ 10 \\ 4 \\ 3 \end{bmatrix} .
> $$
>
> **Normal equations.** Each entry is an inner product of columns:
>
> $$
> (WX)^TWX = \begin{bmatrix} 4 + 4 + 4 + 1 + 1 & -8 - 4 + 0 + 1 + 2 \\ -9 & 16 + 4 + 0 + 1 + 4 \end{bmatrix} = \begin{bmatrix} 14 & -9 \\ -9 & 25 \end{bmatrix}, \qquad
> (WX)^TW\mathbf{y} = \begin{bmatrix} 12 + 20 + 20 + 4 + 3 \\ -24 - 20 + 0 + 4 + 6 \end{bmatrix} = \begin{bmatrix} 59 \\ -34 \end{bmatrix} .
> $$
>
> **Solution.** The determinant is $14 \cdot 25 - 81 = 269$, so
>
> $$
> \begin{bmatrix} \beta_0 \\ \beta_1 \end{bmatrix} = \frac{1}{269}\begin{bmatrix} 25 & 9 \\ 9 & 14 \end{bmatrix} \begin{bmatrix} 59 \\ -34 \end{bmatrix} = \frac{1}{269}\begin{bmatrix} 1475 - 306 \\ 531 - 476 \end{bmatrix} = \begin{bmatrix} 1169/269 \\ 55/269 \end{bmatrix} \approx \begin{bmatrix} 4.3 \\ 0.20 \end{bmatrix} .
> $$
>
> The weighted least-squares line is $y = 4.3 + 0.20x$ (two significant digits).
>
> **Comparison.** Without weights, $X^TX = \begin{bmatrix} 5 & 0 \\ 0 & 10 \end{bmatrix}$ (the $x$-data are already in mean-deviation form) and $X^T\mathbf{y} = (20, -1)$, so the ordinary least-squares line is $y = 4 - 0.1x$. Down-weighting the two right-hand points, which lie low, tilts the line up on the right.
>
> *Lay: Example 6.8.1*

^ex-47-1

![[m235-47-1.svg]]
*Example §47.1: the ordinary least-squares line $y = 4 - 0.1x$ (blue) and the weighted one $y = 4.3 + 0.2x$ (red). The weighted fit uses $w = 2$ for the three filled points and $w = 1$ for the two hollow, less reliable ones, so in the weighted SS(E) their squared residuals count $4$ times less.*

## Trend Analysis of Data

> [!definition] Definition §47.2: Trend Function and Trend Coefficients
> Let $f$ be an unknown function whose values are known (perhaps only approximately) at $t_0, \ldots, t_n$, and give $\mathbb{P}_n$ the evaluation inner product
>
> $$
> \langle p, q\rangle = p(t_0)q(t_0) + \cdots + p(t_n)q(t_n)
> $$
>
> of [[§46 Inner Product Spaces#^ex-46-2|Example §46.2]]. Let $p_0, p_1, p_2, p_3$ be the orthogonal basis of $\mathbb{P}_3$ obtained by Gram–Schmidt from $1, t, t^2, t^3$, and let $g \in \mathbb{P}_n$ be a polynomial whose values at $t_0, \ldots, t_n$ coincide with those of $f$ (one exists by Lay's Supplementary Exercise 11 of Chapter 2: the interpolation conditions form a linear system whose coefficient matrix is the transposed Vandermonde matrix of the distinct points $t_0, \ldots, t_n$, invertible by [[§21 Properties of Determinants#^prop-21-8|Proposition §21.8]]; compare the Lagrange interpolation of [[§22 Cramer’s Rule, Volume, and Linear Transformations#^ex-22-2|Example §22.2]]). The orthogonal projection of $g$ onto $\mathbb{P}_3$,
>
> $$
> \hat g = c_0p_0 + c_1p_1 + c_2p_2 + c_3p_3, \qquad c_i = \frac{\langle g, p_i\rangle}{\langle p_i, p_i\rangle},
> $$
>
> is the **cubic trend function** of the data, and $c_0, \ldots, c_3$ are the **trend coefficients**: $c_1$ measures the linear trend, $c_2$ the quadratic trend, $c_3$ the cubic trend. Projecting onto $\mathbb{P}_2$ instead gives the quadratic trend function. This procedure is a **trend analysis** of the data.
>
> *Lay: 6.8 (text)*

^def-47-2

> [!remark] Remark: Why Orthogonal Polynomials
> Fitting $y = \beta_0 + \beta_1t + \beta_2t^2$ directly, as in [[§45 Applications to Linear Models#^ex-45-2|Example §45.2]], gives a coefficient $\beta_2$ that need not carry the quadratic information alone: it is not "independent", in a statistical sense, of the other $\beta_i$. Engineers analyzing a car's position $f(t)$, for instance, may want to separate the quadratic and cubic components (acceleration) from the linear term (constant velocity). With an orthogonal basis $p_0, p_1, p_2, p_3$, each trend coefficient is computed on its own, $c_i = \langle g, p_i\rangle / \langle p_i, p_i\rangle$, and adding a higher trend later does not change the earlier coefficients: for the quartic trend one only needs a $p_4 \in \mathbb{P}_4$ orthogonal to $\mathbb{P}_3$ and $\langle g, p_4\rangle / \langle p_4, p_4\rangle$. Under certain conditions on the data the trend coefficients are statistically independent. In practice statisticians seldom need trends of degree higher than cubic or quartic.

^rem-47-2

> [!example] Example §47.2: A Quadratic Trend Function
> The simplest and most common case is when the points $t_0, \ldots, t_n$ can be adjusted to be evenly spaced and to sum to zero. Fit a quadratic trend function to the data $(-2, 3)$, $(-1, 5)$, $(0, 5)$, $(1, 4)$, $(2, 3)$.
>
> The $t$-values are $-2, \ldots, 2$, so the orthogonal polynomials of [[§46 Inner Product Spaces#^ex-46-3|Example §46.3]] apply. Only the vectors of values are needed:
>
> $$
> p_0: \begin{bmatrix} 1 \\ 1 \\ 1 \\ 1 \\ 1 \end{bmatrix}, \qquad p_1: \begin{bmatrix} -2 \\ -1 \\ 0 \\ 1 \\ 2 \end{bmatrix}, \qquad p_2: \begin{bmatrix} 2 \\ -1 \\ -2 \\ -1 \\ 2 \end{bmatrix}, \qquad \text{data } g: \begin{bmatrix} 3 \\ 5 \\ 5 \\ 4 \\ 3 \end{bmatrix} .
> $$
>
> Compute $\langle g, p_0\rangle = 20$, $\langle p_0, p_0\rangle = 5$; $\langle g, p_1\rangle = -6 - 5 + 0 + 4 + 6 = -1$, $\langle p_1, p_1\rangle = 10$; $\langle g, p_2\rangle = 6 - 5 - 10 - 4 + 6 = -7$, $\langle p_2, p_2\rangle = 14$. The best approximation by polynomials in $\mathbb{P}_2$ is
>
> $$
> \hat p = \frac{20}{5}p_0 - \frac{1}{10}p_1 - \frac{7}{14}p_2, \qquad \hat p(t) = 4 - 0.1t - 0.5(t^2 - 2) .
> $$
>
> The coefficient of $p_2$ is not small compared with the others, so it is reasonable to conclude that the trend is at least quadratic. (The first two coefficients, $4$ and $-0.1$, reproduce the ordinary least-squares line $y = 4 - 0.1t$ of Example §47.1: projecting onto $\mathbb{P}_1$ just drops the $p_2$ term.)
>
> *Lay: Example 6.8.2*

^ex-47-2

## Fourier Series (Calculus Required)

> [!definition] Definition §47.3: Trigonometric Polynomial
> A **trigonometric polynomial** is a function on $[0, 2\pi]$ of the form
>
> $$
> \frac{a_0}{2} + a_1\cos t + \cdots + a_n\cos nt + b_1\sin t + \cdots + b_n\sin nt . \tag{4}
> $$
>
> If $a_n$ and $b_n$ are not both zero, it has **order $n$**.
>
> *Lay: 6.8 (text)*

^def-47-3

Continuous functions, such as a sound wave, an electric signal or the motion of a vibrating mechanical system, are often approximated by trigonometric polynomials. Their use rests on the following orthogonality.

> [!theorem] Proposition §47.2: Orthogonality of the Trigonometric System
> For every $n \ge 1$, the set
>
> $$
> \{1, \cos t, \cos 2t, \ldots, \cos nt, \sin t, \sin 2t, \ldots, \sin nt\} \tag{5}
> $$
>
> is orthogonal in $C[0, 2\pi]$ with the inner product
>
> $$
> \langle f, g\rangle = \int_0^{2\pi} f(t)g(t)\,dt . \tag{6}
> $$
>
> Moreover $\langle 1, 1\rangle = 2\pi$ and $\langle \cos kt, \cos kt\rangle = \langle \sin kt, \sin kt\rangle = \pi$ for $k \ge 1$.
>
> *Lay: 6.8 (text); Example 6.8.3; Exercises 5–7*

^prop-47-2

> [!proof]+ Proof
> Lay works the first case (Example 3) and leaves the rest as Exercises 5–7. Let $m$, $n$ be positive integers. All cases follow from the product-to-sum identities
>
> $$
> \cos A\cos B = \tfrac12[\cos(A + B) + \cos(A - B)], \quad \sin A\sin B = \tfrac12[\cos(A - B) - \cos(A + B)], \quad \sin A\cos B = \tfrac12[\sin(A + B) + \sin(A - B)],
> $$
>
> and the facts that for an integer $k \ne 0$, $\int_0^{2\pi}\cos kt\,dt = \frac{\sin kt}{k}\Big|_0^{2\pi} = 0$ and $\int_0^{2\pi}\sin kt\,dt = -\frac{\cos kt}{k}\Big|_0^{2\pi} = 0$.
>
> **$\cos mt \perp \cos nt$ for $m \ne n$** (Lay's Example 3):
>
> $$
> \langle \cos mt, \cos nt\rangle = \int_0^{2\pi}\cos mt\cos nt\,dt = \frac12\int_0^{2\pi}[\cos(mt + nt) + \cos(mt - nt)]\,dt = \frac12\Big[\frac{\sin(mt + nt)}{m + n} + \frac{\sin(mt - nt)}{m - n}\Big]_0^{2\pi} = 0 .
> $$
>
> **$\sin mt \perp \sin nt$ for $m \ne n$**: in the same way, $\frac12\int_0^{2\pi}[\cos(m - n)t - \cos(m + n)t]\,dt = 0$, since $m - n \ne 0$ and $m + n \ne 0$.
>
> **$\sin mt \perp \cos nt$ for all $m, n \ge 1$**: $\frac12\int_0^{2\pi}[\sin(m + n)t + \sin(m - n)t]\,dt = 0$, because each term integrates to $0$ (and $\sin 0t = 0$ when $m = n$).
>
> **$1 \perp \cos kt$, $1 \perp \sin kt$** for $k \ge 1$: these are the integrals $\int_0^{2\pi}\cos kt\,dt = \int_0^{2\pi}\sin kt\,dt = 0$.
>
> **Norms.** $\langle 1, 1\rangle = \int_0^{2\pi}1\,dt = 2\pi$. For $k \ge 1$, $\cos^2 kt = \frac12(1 + \cos 2kt)$ and $\sin^2 kt = \frac12(1 - \cos 2kt)$, so $\int_0^{2\pi}\cos^2 kt\,dt = \int_0^{2\pi}\sin^2 kt\,dt = \frac12 \cdot 2\pi = \pi$.

^pf-47-2

*Uses:* [[§46 Inner Product Spaces#^ex-46-4|Ex. §46.4]] (the inner product (6))

> [!remark]- Connections
> - The same system normalized on $[-\pi, \pi]$ is Axler's orthonormal list [[§20 Orthonormal Bases#^ladr-6-23|LADR 6.23]](d); in complex form $e^{int}/\sqrt{2\pi}$ it is the Fourier basis of $L^2[0, 2\pi]$, [[§20 Orthonormal Sets and Bases#^thm-20-11|556 Thm. §20.11]].
> - See also: [[§6 Periodic Functions and Fourier Series#^prop-6-3|341 Prop. §6.3]] (the same relations on $(-\pi, \pi)$, the starting point of Fourier series).

> [!definition] Definition §47.4: Fourier Approximation; Fourier Coefficients
> Let $W$ be the subspace of $C[0, 2\pi]$ spanned by the functions (5). For $f \in C[0, 2\pi]$, the best approximation to $f$ by functions in $W$ (for the inner product (6)) is the **$n$th-order Fourier approximation** to $f$ on $[0, 2\pi]$. Since (5) is an orthogonal set, it is the orthogonal projection $\operatorname{proj}_W f$, and its coefficients $a_k$, $b_k$ in the form (4) are the **Fourier coefficients** of $f$.
>
> *Lay: 6.8 (text)*

^def-47-4

> [!theorem] Theorem §47.3: Formulas for the Fourier Coefficients
> The Fourier coefficients of $f \in C[0, 2\pi]$ are
>
> $$
> a_k = \frac1\pi\int_0^{2\pi}f(t)\cos kt\,dt, \qquad b_k = \frac1\pi\int_0^{2\pi}f(t)\sin kt\,dt \qquad (k \ge 0 \text{ for } a_k,\ k \ge 1 \text{ for } b_k), \tag{7}
> $$
>
> and the constant term of the $n$th-order Fourier approximation is $\frac{a_0}{2}$, with $a_0$ given by (7) for $k = 0$.
>
> *Lay: 6.8 (text), Equation (7)*

^thm-47-3

> [!proof]+ Proof
> By the projection formula of [[§46 Inner Product Spaces#^thm-46-2|Theorem §46.2]] for the orthogonal basis (5) of $W$, the coefficients of $\cos kt$ and $\sin kt$ ($k \ge 1$) are
>
> $$
> a_k = \frac{\langle f, \cos kt\rangle}{\langle \cos kt, \cos kt\rangle}, \qquad b_k = \frac{\langle f, \sin kt\rangle}{\langle \sin kt, \sin kt\rangle} .
> $$
>
> By Proposition §47.2 the denominators are $\pi$, which gives (7). The coefficient of the constant function $1$ is
>
> $$
> \frac{\langle f, 1\rangle}{\langle 1, 1\rangle} = \frac{1}{2\pi}\int_0^{2\pi}f(t) \cdot 1\,dt = \frac12\Big[\frac1\pi\int_0^{2\pi}f(t)\cos(0 \cdot t)\,dt\Big] = \frac{a_0}{2} .
> $$
>
> This is why the constant term in (4) is written as $a_0/2$: one formula (7) covers every $k \ge 0$.

^pf-47-3

*Uses:* [[§46 Inner Product Spaces#^thm-46-2|§46.2]], [[§47 Applications of Inner Product Spaces#^prop-47-2|§47.2]]

> [!remark]- Connections
> - See also: [[§6 Periodic Functions and Fourier Series#^prop-6-4|341 Prop. §6.4]] and [[§6 Periodic Functions and Fourier Series#^def-6-2|341 Def. §6.2]] (the same coefficients on $(-\pi, \pi)$; Powers' constant term $a_0$, the mean value of $f$, is Lay's $a_0/2$), followed by worked Fourier series.

> [!example] Example §47.3: Fourier Approximations of f(t) = t
> Find the $n$th-order Fourier approximation to $f(t) = t$ on $[0, 2\pi]$.
>
> **Constant term.**
>
> $$
> \frac{a_0}{2} = \frac12 \cdot \frac1\pi\int_0^{2\pi}t\,dt = \frac{1}{2\pi}\Big[\frac12t^2\Big]_0^{2\pi} = \frac{1}{2\pi} \cdot 2\pi^2 = \pi .
> $$
>
> **Cosine terms.** For $k \ge 1$, integrating by parts ($\int t\cos kt\,dt = \frac{t}{k}\sin kt + \frac{1}{k^2}\cos kt$),
>
> $$
> a_k = \frac1\pi\int_0^{2\pi}t\cos kt\,dt = \frac1\pi\Big[\frac{1}{k^2}\cos kt + \frac{t}{k}\sin kt\Big]_0^{2\pi} = \frac1\pi\Big[\frac{1}{k^2} - \frac{1}{k^2}\Big] = 0 .
> $$
>
> **Sine terms.** ($\int t\sin kt\,dt = \frac{1}{k^2}\sin kt - \frac{t}{k}\cos kt$.)
>
> $$
> b_k = \frac1\pi\int_0^{2\pi}t\sin kt\,dt = \frac1\pi\Big[\frac{1}{k^2}\sin kt - \frac{t}{k}\cos kt\Big]_0^{2\pi} = \frac1\pi\Big[-\frac{2\pi}{k}\Big] = -\frac2k .
> $$
>
> So the $n$th-order Fourier approximation of $f(t) = t$ is
>
> $$
> \pi - 2\sin t - \sin 2t - \frac23\sin 3t - \cdots - \frac2n\sin nt .
> $$
>
> *Lay: Example 6.8.4*

^ex-47-3

![[m235-47-2.svg]]
*Example §47.3: $f(t) = t$ (black) and its third-order (left) and fourth-order (right) Fourier approximations (blue). The approximations oscillate around the line and are pulled toward $\pi$ at both ends of $[0, 2\pi]$, where the periodic extension of $f$ jumps from $2\pi$ back to $0$; the error is small in the mean-square sense, not at every point.*

> [!definition] Definition §47.5: Mean Square Error
> The norm $\|f - \operatorname{proj}_W f\|$ of the difference between $f$ and a Fourier approximation is the **mean square error** of the approximation (*mean*, because the norm is defined by an integral).
>
> *Lay: 6.8 (text)*

^def-47-5

> [!theorem] Theorem §47.4: Fourier Approximations Converge in the Mean
> For every $f \in C[0, 2\pi]$, the mean square error of the $n$th-order Fourier approximation tends to $0$ as $n \to \infty$:
>
> $$
> \Big\| f - \Big(\frac{a_0}{2} + \sum_{m=1}^n (a_m\cos mt + b_m\sin mt)\Big) \Big\| \to 0 .
> $$
>
> In particular, every $f \in C[0, 2\pi]$ can be approximated as closely as desired, in this norm, by trigonometric polynomials.
>
> *Lay: 6.8 (text)*

^thm-47-4

*Lay omits the proof ("it can be shown"). It is the completeness of the trigonometric system in $L^2[0, 2\pi]$, [[§20 Orthonormal Sets and Bases#^thm-20-11|556 Thm. §20.11]], combined with [[§20 Orthonormal Sets and Bases#^thm-20-8|556 Thm. §20.8]] (the $n$th-order Fourier approximation of a real $f$ is the partial sum $\sum_{|k| \le n} (f, e_k)e_k$ of its expansion in the basis $e_k = e^{ikt}/\sqrt{2\pi}$, and these partial sums converge to $f$ in norm); the completeness itself is quoted there without proof as well (via Fejér's theorem).*

> [!remark]- Connections
> - Fourier series in $L^2$, with Parseval's equality $\int_0^{2\pi}|f|^2 = \sum |c_n|^2$: [[§20 Orthonormal Sets and Bases#^rem-20-9|556 Remark: Fourier Series]]; the finite Bessel inequality $\|\operatorname{proj}_W f\| \le \|f\|$ (Proposition §46.3 here) is [[§20 Orthonormal Sets and Bases#^lem-20-2|556 Lem. §20.2]].
> - Convergence in the mean does not give convergence at every point: in the figure after Example §47.3 the approximations of $t$ miss the endpoint values $0$ and $2\pi$.
> - See also: [[§11★ Mean Error and Convergence in Mean#^thm-11-6|341 Thm. §11.6]] (convergence in the mean for every $f$ with $\int f^2$ finite, from the minimum error in [[§11★ Mean Error and Convergence in Mean#^thm-11-2|341 Thm. §11.2]]), with Parseval's equality, [[§11★ Mean Error and Convergence in Mean#^thm-11-4|341 Thm. §11.4]].

> [!definition] Definition §47.6: Fourier Series
> Because of Theorem §47.4 one writes
>
> $$
> f(t) = \frac{a_0}{2} + \sum_{m=1}^\infty (a_m\cos mt + b_m\sin mt),
> $$
>
> the **Fourier series** of $f$ on $[0, 2\pi]$. The term $a_m\cos mt$, for example, is the projection of $f$ onto the one-dimensional subspace spanned by $\cos mt$.
>
> *Lay: 6.8 (text)*

^def-47-6

> [!example] Example §47.4: Fourier Approximations Without Integrals
> Find the first-order and third-order Fourier approximations to
>
> $$
> f(t) = 3 - 2\sin t + 5\sin 2t - 6\cos 2t .
> $$
>
> $f$ is already a trigonometric polynomial (of order $2$), so no integrals are needed. Its coefficients in the orthogonal set (5) are $\frac{a_0}{2} = 3$, $b_1 = -2$, $b_2 = 5$, $a_2 = -6$, and all others $0$; by the uniqueness of coordinates in an orthogonal basis ([[§41 Orthogonal Sets#^thm-41-2|Theorem §41.2]], in $C[0, 2\pi]$), these are its Fourier coefficients. The projection onto $\operatorname{Span}\{1, \cos t, \sin t\}$ keeps the terms of order $\le 1$, so the first-order Fourier approximation is
>
> $$
> 3 - 2\sin t .
> $$
>
> For the third order, $f$ lies in $W = \operatorname{Span}\{1, \cos t, \cos 2t, \cos 3t, \sin t, \sin 2t, \sin 3t\}$, so its projection onto $W$ is $f$ itself ([[§42 Orthogonal Projections#^prop-42-2|Proposition §42.2]]): the third-order Fourier approximation is $3 - 2\sin t + 5\sin 2t - 6\cos 2t$.
>
> *Lay: 6.8, Practice Problem 2*

^ex-47-4
