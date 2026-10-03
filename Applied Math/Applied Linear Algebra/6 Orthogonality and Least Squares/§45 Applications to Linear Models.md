---
type: section
subject: "[[Applied Linear Algebra]]"
chapter: 6
section: 45
lay: "6.6"
aliases: ["Lay 6.6"]
tags: [applied-linear-algebra, math235]
---
← [[§44 Least-Squares Problems]] · ↑ [[· 6 Orthogonality and Least Squares]] · [[§46 Inner Product Spaces]] →

*Lay, Section 6.6.*

Fitting a formula to experimental data is a least-squares problem in disguise. Fitting a line, a parabola, a cubic, a plane, or any combination $\beta_0 f_0 + \cdots + \beta_k f_k$ of known functions works the same way: the unknown coefficients enter linearly, so the conditions "the formula reproduces each data point" form a linear system $X\boldsymbol\beta = \mathbf{y}$, usually inconsistent. The best fit, in the sense of the smallest sum of squared residuals, is the least-squares solution of [[§44 Least-Squares Problems|§44]], found from the normal equations $X^TX\boldsymbol\beta = X^T\mathbf{y}$. The section uses statistics notation throughout.

> [!definition] Definition §45.1: Design Matrix, Parameter Vector, Observation Vector
> In the statistical analysis of data, the least-squares problem $A\mathbf{x} = \mathbf{b}$ is written
>
> $$
> X\boldsymbol\beta = \mathbf{y},
> $$
>
> where $X$ is the **design matrix**, $\boldsymbol\beta$ the **parameter vector**, and $\mathbf{y}$ the **observation vector**.
>
> *Lay: 6.6 (text)*

^def-45-1

## Least-Squares Lines

> [!definition] Definition §45.2: Residuals and the Least-Squares Line
> Let $(x_1, y_1), \ldots, (x_n, y_n)$ be data points and $y = \beta_0 + \beta_1x$ a line. For each $j$, $y_j$ is the **observed value** of $y$, and $\beta_0 + \beta_1x_j$ (the point of the line with the same $x$-coordinate) is the **predicted** $y$-value. Their difference $y_j - (\beta_0 + \beta_1x_j)$ is a **residual**.
>
> The **least-squares line** is the line $y = \beta_0 + \beta_1x$ that minimizes the sum of the squares of the residuals. It is also called the **line of regression of $y$ on $x$** (any errors in the data are assumed to be only in the $y$-coordinates), and $\beta_0$, $\beta_1$ are the (linear) **regression coefficients**. Lay writes $y = \beta_0 + \beta_1x$ instead of $y = mx + b$.
>
> *Lay: 6.6 (text)*

^def-45-2

> [!theorem] Proposition §45.1: The Least-Squares Line Is a Least-Squares Solution
> Let
>
> $$
> X = \begin{bmatrix} 1 & x_1 \\ 1 & x_2 \\ \vdots & \vdots \\ 1 & x_n \end{bmatrix}, \qquad \boldsymbol\beta = \begin{bmatrix} \beta_0 \\ \beta_1 \end{bmatrix}, \qquad \mathbf{y} = \begin{bmatrix} y_1 \\ y_2 \\ \vdots \\ y_n \end{bmatrix} . \tag{1}
> $$
>
> Then $\beta_0, \beta_1$ are the coefficients of the least-squares line if and only if $\boldsymbol\beta$ is a least-squares solution of $X\boldsymbol\beta = \mathbf{y}$, that is, a solution of the normal equations $X^TX\boldsymbol\beta = X^T\mathbf{y}$.
>
> *Lay: 6.6 (text)*

^prop-45-1

> [!proof]+ Proof
> The $j$th entry of $X\boldsymbol\beta$ is $\beta_0 + \beta_1x_j$, the predicted value, so the $j$th entry of $\mathbf{y} - X\boldsymbol\beta$ is the $j$th residual and
>
> $$
> \|\mathbf{y} - X\boldsymbol\beta\|^2 = \sum_{j=1}^n \big(y_j - (\beta_0 + \beta_1x_j)\big)^2
> $$
>
> is precisely the sum of the squares of the residuals. Minimizing this sum is minimizing $\|\mathbf{y} - X\boldsymbol\beta\|$, which is the definition of a least-squares solution. If the data points were all on the line, $X\boldsymbol\beta = \mathbf{y}$ would hold exactly; usually it has no solution. The last statement is [[§44 Least-Squares Problems#^thm-44-1|Theorem §44.1]].

^pf-45-1

*Uses:* [[§44 Least-Squares Problems#^def-44-1|Def. §44.1]], [[§44 Least-Squares Problems#^thm-44-1|§44.1]]

> [!remark]- Connections
> - The regression lines and the quadratic model of Calculus are computed this way (there by calculator): [[§2 Mathematical Models꞉ A Catalog of Essential Functions#^def-2-3|Calc Def. §2.3]], [[§2 Mathematical Models꞉ A Catalog of Essential Functions#^ex-2-2|Calc Ex. §2.2]] (a regression line), [[§2 Mathematical Models꞉ A Catalog of Essential Functions#^ex-2-3|Calc Ex. §2.3]] (a quadratic fit to real data, the model of Example §45.2(a)).
> - Rigorous treatment of the minimization: [[§21 Orthogonal Complements and Minimization Problems#^ladr-6-61|LADR 6.61]] with $U = \operatorname{Col} X$.

> [!definition] Definition §45.3: Mean-Deviation Form
> Let $\bar{x} = \frac1n(x_1 + \cdots + x_n)$ be the average of the $x$-values. The new variable $x^{\ast} = x - \bar{x}$ has data $x_j^{\ast} = x_j - \bar{x}$, which are said to be in **mean-deviation form**.
>
> *Lay: 6.6 (text)*

^def-45-3

> [!theorem] Proposition §45.2: Fitting a Line in Mean-Deviation Form
> Let the $x_j$ not all be equal, and put the $x$-data in mean-deviation form, $x_j^* = x_j - \bar{x}$ (so $\sum x_j^* = 0$). Then the two columns of the design matrix $X = [\,\mathbf{1}\ \ \mathbf{x}^*\,]$ are orthogonal, $X^TX$ is diagonal, and the least-squares line $y = \beta_0^* + \beta_1^*x^*$ has
>
> $$
> \beta_0^* = \bar{y} = \frac1n\sum_j y_j, \qquad \beta_1^* = \frac{\sum_j x_j^*y_j}{\sum_j (x_j^*)^2} .
> $$
>
> In terms of the original variable, the least-squares line is $y = \bar{y} + \beta_1^*(x - \bar{x})$. In particular it passes through the point $(\bar{x}, \bar{y})$.
>
> *Lay: 6.6 (text); Exercises 14, 17 and 18*

^prop-45-2

> [!proof]+ Proof
> The columns of $X$ are $\mathbf{1} = (1, \ldots, 1)$ and $\mathbf{x}^* = (x_1^*, \ldots, x_n^*)$, and $\mathbf{1} \cdot \mathbf{x}^* = \sum_j (x_j - \bar{x}) = n\bar{x} - n\bar{x} = 0$. So
>
> $$
> X^TX = \begin{bmatrix} \mathbf{1} \cdot \mathbf{1} & \mathbf{1} \cdot \mathbf{x}^* \\ \mathbf{x}^* \cdot \mathbf{1} & \mathbf{x}^* \cdot \mathbf{x}^* \end{bmatrix} = \begin{bmatrix} n & 0 \\ 0 & \sum (x_j^*)^2 \end{bmatrix}, \qquad X^T\mathbf{y} = \begin{bmatrix} \sum y_j \\ \sum x_j^*y_j \end{bmatrix},
> $$
>
> and the normal equations decouple into $n\beta_0^* = \sum y_j$ and $\big(\sum (x_j^*)^2\big)\beta_1^* = \sum x_j^*y_j$. Since the $x_j$ are not all equal, some $x_j^* \ne 0$ and $\sum (x_j^*)^2 > 0$, so both equations can be solved. This gives the formulas, exactly as in [[§44 Least-Squares Problems#^ex-44-4|Example §44.4]].
>
> The lines $y = \beta_0 + \beta_1x$ are the same as the lines $y = \beta_0^* + \beta_1^*(x - \bar{x})$, with $\beta_1 = \beta_1^*$ and $\beta_0 = \beta_0^* - \beta_1^*\bar{x}$, and a line has the same residuals at the data points in either description. So the minimizing line is the same, and it is $y = \bar{y} + \beta_1^*(x - \bar{x})$, which takes the value $\bar{y}$ at $x = \bar{x}$.

^pf-45-2

*Uses:* [[§45 Applications to Linear Models#^prop-45-1|§45.1]], [[§44 Least-Squares Problems#^thm-44-1|§44.1]]

> [!example] Example §45.1: A Least-Squares Line
> Find the equation $y = \beta_0 + \beta_1x$ of the least-squares line that best fits the data points $(2, 1)$, $(5, 2)$, $(7, 3)$, $(8, 3)$.
>
> **Normal equations.** Build $X$ from the $x$-coordinates and $\mathbf{y}$ from the $y$-coordinates:
>
> $$
> X = \begin{bmatrix} 1 & 2 \\ 1 & 5 \\ 1 & 7 \\ 1 & 8 \end{bmatrix}, \qquad \mathbf{y} = \begin{bmatrix} 1 \\ 2 \\ 3 \\ 3 \end{bmatrix}, \qquad
> X^TX = \begin{bmatrix} 4 & 22 \\ 22 & 142 \end{bmatrix}, \qquad X^T\mathbf{y} = \begin{bmatrix} 9 \\ 57 \end{bmatrix},
> $$
>
> since $2 + 5 + 7 + 8 = 22$, $4 + 25 + 49 + 64 = 142$, $1 + 2 + 3 + 3 = 9$ and $2 + 10 + 21 + 24 = 57$. With $\det X^TX = 568 - 484 = 84$,
>
> $$
> \begin{bmatrix} \beta_0 \\ \beta_1 \end{bmatrix} = \begin{bmatrix} 4 & 22 \\ 22 & 142 \end{bmatrix}^{-1} \begin{bmatrix} 9 \\ 57 \end{bmatrix} = \frac{1}{84}\begin{bmatrix} 142 & -22 \\ -22 & 4 \end{bmatrix} \begin{bmatrix} 9 \\ 57 \end{bmatrix} = \frac{1}{84}\begin{bmatrix} 1278 - 1254 \\ -198 + 228 \end{bmatrix} = \frac{1}{84}\begin{bmatrix} 24 \\ 30 \end{bmatrix} = \begin{bmatrix} 2/7 \\ 5/14 \end{bmatrix} .
> $$
>
> The least-squares line is $y = \frac27 + \frac{5}{14}x$. Its predicted values at $x = 2, 5, 7, 8$ are $1, \frac{29}{14}, \frac{39}{14}, \frac{44}{14}$, so the residuals are $0, -\frac{1}{14}, \frac{3}{14}, -\frac{2}{14}$ (they sum to $0$), and the minimal sum of squared residuals is $\frac{0 + 1 + 9 + 4}{196} = \frac{1}{14}$.
>
> **The same line in mean-deviation form.** Here $\bar{x} = \frac{22}{4} = 5.5$, so $\mathbf{x}^{\ast} = (-3.5, -0.5, 1.5, 2.5)$, and $\bar{y} = \frac94$. By Proposition §45.2,
>
> $$
> \beta_1^* = \frac{-3.5 - 1 + 4.5 + 7.5}{12.25 + 0.25 + 2.25 + 6.25} = \frac{7.5}{21} = \frac{5}{14}, \qquad
> y = \frac94 + \frac{5}{14}\Big(x - \frac{11}{2}\Big) = \frac{63 - 55}{28} + \frac{5}{14}x = \frac27 + \frac{5}{14}x,
> $$
>
> the same line, with no matrix inversion.
>
> *Lay: Example 6.6.1; the second part is Exercise 6.6.17*

^ex-45-1

![[m235-45-1.svg]]
*Example §45.1: the least-squares line $y = \frac27 + \frac{5}{14}x$ and the four data points. The residuals are the vertical segments from each data point to the line (red, drawn to scale; at $x = 2$ the point lies on the line); the line minimizes the sum of their squares. It passes through $(\bar{x}, \bar{y}) = (5.5, 2.25)$ (Proposition §45.2).*

## The General Linear Model

> [!definition] Definition §45.4: Linear Model; Residual Vector
> Statisticians introduce the **residual vector** $\boldsymbol\epsilon = \mathbf{y} - X\boldsymbol\beta$ and write
>
> $$
> \mathbf{y} = X\boldsymbol\beta + \boldsymbol\epsilon .
> $$
>
> Any equation of this form is a **linear model**. Once $X$ and $\mathbf{y}$ are determined, the goal is to minimize the length of $\boldsymbol\epsilon$, that is, to find a least-squares solution $\hat{\boldsymbol\beta}$ of $X\boldsymbol\beta = \mathbf{y}$; it solves the normal equations $X^TX\boldsymbol\beta = X^T\mathbf{y}$.
>
> *Lay: 6.6 (text)*

^def-45-4

## Least-Squares Fitting of Other Curves

> [!remark] Remark: Linear in the Parameters
> When data points $(x_1, y_1), \ldots, (x_n, y_n)$ do not lie close to a line, one may postulate a relation
>
> $$
> y = \beta_0f_0(x) + \beta_1f_1(x) + \cdots + \beta_kf_k(x) \tag{2}
> $$
>
> with known functions $f_0, \ldots, f_k$ and unknown parameters $\beta_0, \ldots, \beta_k$. This is a linear model, because (2) is linear in the *parameters*, however nonlinear the $f_i$ are in $x$. Row $j$ of the design matrix is $(f_0(x_j), \ldots, f_k(x_j))$, the residual at $x_j$ is $y_j$ minus the fitted value, and the parameters are chosen to minimize the sum of the squared residuals.

^rem-45-1

> [!example] Example §45.2: Design Matrices for Curve Fitting
> Describe the linear model that gives a least-squares fit of data $(x_1, y_1), \ldots, (x_n, y_n)$ by each of the following curves.
>
> **(a) A parabola** $y = \beta_0 + \beta_1x + \beta_2x^2$. Typical sources: an average-cost curve as a function of the production level (opening upward), or the net primary production of nutrients in a plant as a function of the surface area of the foliage (opening downward). Each data point gives an equation with a residual $\epsilon_j$ between the observed and the predicted value:
>
> $$
> \begin{aligned}
> y_1 &= \beta_0 + \beta_1x_1 + \beta_2x_1^2 + \epsilon_1 \\
> &\ \ \vdots \\
> y_n &= \beta_0 + \beta_1x_n + \beta_2x_n^2 + \epsilon_n
> \end{aligned}
> \qquad\text{that is}\qquad
> \underbrace{\begin{bmatrix} y_1 \\ y_2 \\ \vdots \\ y_n \end{bmatrix}}_{\mathbf{y}} = \underbrace{\begin{bmatrix} 1 & x_1 & x_1^2 \\ 1 & x_2 & x_2^2 \\ \vdots & \vdots & \vdots \\ 1 & x_n & x_n^2 \end{bmatrix}}_{X} \underbrace{\begin{bmatrix} \beta_0 \\ \beta_1 \\ \beta_2 \end{bmatrix}}_{\boldsymbol\beta} + \underbrace{\begin{bmatrix} \epsilon_1 \\ \epsilon_2 \\ \vdots \\ \epsilon_n \end{bmatrix}}_{\boldsymbol\epsilon} .
> $$
>
> **(b) A cubic** $y = \beta_0 + \beta_1x + \beta_2x^2 + \beta_3x^3$ (for instance a company's total costs as a function of production). The same analysis gives
>
> $$
> X = \begin{bmatrix} 1 & x_1 & x_1^2 & x_1^3 \\ 1 & x_2 & x_2^2 & x_2^3 \\ \vdots & \vdots & \vdots & \vdots \\ 1 & x_n & x_n^2 & x_n^3 \end{bmatrix}, \qquad \boldsymbol\beta = \begin{bmatrix} \beta_0 \\ \beta_1 \\ \beta_2 \\ \beta_3 \end{bmatrix} .
> $$
>
> **(c) A trend with a seasonal term** $y = \beta_0 + \beta_1x + \beta_2\sin(2\pi x/12)$, for monthly sales ($x$ in months) with seasonal fluctuations: $\beta_0 + \beta_1x$ is the basic sales trend, and the sine term the seasonal change. Row $k$ of $X\boldsymbol\beta$ must be the predicted value $\beta_0 + \beta_1x_k + \beta_2\sin(2\pi x_k/12)$, so
>
> $$
> X = \begin{bmatrix} 1 & x_1 & \sin(2\pi x_1/12) \\ \vdots & \vdots & \vdots \\ 1 & x_n & \sin(2\pi x_n/12) \end{bmatrix}, \qquad \boldsymbol\beta = \begin{bmatrix} \beta_0 \\ \beta_1 \\ \beta_2 \end{bmatrix} .
> $$
>
> In each case, $\hat{\boldsymbol\beta}$ is found from $X^TX\boldsymbol\beta = X^T\mathbf{y}$.
>
> *Lay: Examples 6.6.2 and 6.6.3; Practice Problem*

^ex-45-2

## Multiple Regression

> [!definition] Definition §45.5: Multiple Regression; Trend Surface
> When an experiment has two independent variables $u$, $v$ and one dependent variable $y$, a prediction equation such as
>
> $$
> y = \beta_0 + \beta_1u + \beta_2v \quad (4)
> \qquad\text{or}\qquad
> y = \beta_0 + \beta_1u + \beta_2v + \beta_3u^2 + \beta_4uv + \beta_5v^2 \quad (5)
> $$
>
> is fitted by **multiple regression**. Both are linear models, being linear in the parameters (even though $u$ and $v$ are multiplied in (5)); in general any $y = \beta_0f_0(u, v) + \cdots + \beta_kf_k(u, v)$ with known $f_i$ is. In geology, a least-squares fit of this kind (erosion surfaces, glacial cirques, soil pH) is called a **trend surface**; the fit by (4) is the **least-squares plane**.
>
> *Lay: 6.6 (text)*

^def-45-5

> [!example] Example §45.3: A Least-Squares Plane
> Local models of terrain are built from data $(u_1, v_1, y_1), \ldots, (u_n, v_n, y_n)$, where $u_j$, $v_j$, $y_j$ are latitude, longitude and altitude. Describe the linear model based on (4) that gives a least-squares fit.
>
> The data should satisfy $y_j = \beta_0 + \beta_1u_j + \beta_2v_j + \epsilon_j$ for $j = 1, \ldots, n$, which is $\mathbf{y} = X\boldsymbol\beta + \boldsymbol\epsilon$ with
>
> $$
> \mathbf{y} = \begin{bmatrix} y_1 \\ y_2 \\ \vdots \\ y_n \end{bmatrix}, \qquad
> X = \begin{bmatrix} 1 & u_1 & v_1 \\ 1 & u_2 & v_2 \\ \vdots & \vdots & \vdots \\ 1 & u_n & v_n \end{bmatrix}, \qquad
> \boldsymbol\beta = \begin{bmatrix} \beta_0 \\ \beta_1 \\ \beta_2 \end{bmatrix}, \qquad
> \boldsymbol\epsilon = \begin{bmatrix} \epsilon_1 \\ \epsilon_2 \\ \vdots \\ \epsilon_n \end{bmatrix} .
> $$
>
> The least-squares solution $\hat{\boldsymbol\beta}$ gives the least-squares plane $y = \hat\beta_0 + \hat\beta_1u + \hat\beta_2v$, the plane minimizing the sum of the squared vertical distances to the data points.
>
> *Lay: Example 6.6.4*

^ex-45-3

> [!remark] Remark: One Principle for All Linear Models
> Multiple regression has the same abstract form as simple regression: once the design matrix $X$ is set up, the normal equations $X^TX\boldsymbol\beta = X^T\mathbf{y}$ have the same matrix form no matter how many variables are involved. Whenever $X^TX$ is invertible (equivalently, the columns of $X$ are linearly independent, [[§44 Least-Squares Problems#^thm-44-2|Theorem §44.2]]),
>
> $$
> \hat{\boldsymbol\beta} = (X^TX)^{-1}X^T\mathbf{y} .
> $$
>
> For a line, the columns $\mathbf{1}$ and $\mathbf{x}$ are independent exactly when the data contain at least two points with different $x$-coordinates (Lay's Exercise 5).

^rem-45-2
