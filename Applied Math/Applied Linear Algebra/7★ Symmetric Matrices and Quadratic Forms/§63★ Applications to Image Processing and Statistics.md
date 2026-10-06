---
type: section
subject: "[[Applied Linear Algebra]]"
chapter: 7
section: "63★"
lay: "7.5"
aliases: ["Lay 7.5"]
tags: [applied-linear-algebra, math235, extension]
---
← [[§62★ The Singular Value Decomposition in Applications]] · ↑ [[· 7★ Symmetric Matrices and Quadratic Forms]] · [[§64 Complex Numbers]] →

*Lay, Section 7.5.*
★ *Beyond MATH 235: the course ended with inner products (Ch. 6); Chapter 7 is included from Lay as the continuation.*

Multivariate data (lists of $p$ measurements on each of $N$ objects) form a $p \times N$ matrix whose columns are points in $\mathbb{R}^p$. Principal component analysis looks for an orthogonal change of variable that makes the new variables uncorrelated and orders them by decreasing variance. This is exactly the orthogonal diagonalization of the covariance matrix $S$, a symmetric positive semidefinite matrix. The eigenvectors of $S$ are the principal components, and the eigenvalues are the variances of the new variables. Total variance is preserved, so when a few eigenvalues dominate, the data are essentially low-dimensional and can be described by a few variables. The constrained optimization theorems of [[§60★ Constrained Optimization|§60★]] show that the first principal component is the direction of maximal variance. In practice the computation is done with the SVD of [[§61★ The Singular Value Decomposition|§61★]].

## Multivariate Data

> [!definition] Definition §63.1: Observation Vectors; Matrix of Observations
> When $p$ measurements are made on each of $N$ objects or individuals, the list of measurements for the $j$th one is an **observation vector** $\mathbf{X}_j$ in $\mathbb{R}^p$, and the $p \times N$ matrix $[\,\mathbf{X}_1\ \cdots\ \mathbf{X}_N\,]$ is the **matrix of observations**. Such data are called **multivariate**: each datum is identified with a point in $\mathbb{R}^p$.
>
> Examples:
> - Weights $w_j$ and heights $h_j$ of $N$ college students give observation vectors $\mathbf{X}_j = (w_j, h_j)$ in $\mathbb{R}^2$ and a $2 \times N$ matrix of observations $\begin{bmatrix} w_1 & \cdots & w_N \\ h_1 & \cdots & h_N \end{bmatrix}$; the observation vectors can be pictured as a two-dimensional scatter plot.
> - 300 samples of a plastic, each subjected to eight tests (melting point, density, ductility, tensile strength, …), give an $8 \times 300$ matrix of observations.
> - A multispectral satellite image of a region, taken at three wavelengths and $2000 \times 2000$ pixels, gives one observation vector in $\mathbb{R}^3$ per pixel (the three signal intensities), so a $3 \times 4{,}000{,}000$ matrix: a cloud of 4 million points in $\mathbb{R}^3$. The "multidimensional" character refers to the three *spectral* dimensions, not the two spatial ones.
>
> *Lay: 7.5 (text); Examples 7.5.1 and 7.5.2*

^def-63-1

## Mean and Covariance

> [!definition] Definition §63.2: Sample Mean
> Let $[\,\mathbf{X}_1\ \cdots\ \mathbf{X}_N\,]$ be a $p \times N$ matrix of observations. The **sample mean** of the observation vectors is
>
> $$
> \mathbf{M} = \frac1N (\mathbf{X}_1 + \cdots + \mathbf{X}_N) ,
> $$
>
> the "center" of the scatter plot.
>
> *Lay: 7.5 (text)*

^def-63-2

> [!definition] Definition §63.3: Mean-Deviation Form
> For $k = 1, \dots, N$ let $\hat{\mathbf{X}}_k = \mathbf{X}_k - \mathbf{M}$. The columns of the $p \times N$ matrix
>
> $$
> B = [\,\hat{\mathbf{X}}_1\ \ \hat{\mathbf{X}}_2\ \cdots\ \hat{\mathbf{X}}_N\,]
> $$
>
> have a zero sample mean, and $B$ is said to be in **mean-deviation form**.
>
> *Lay: 7.5 (text)*

^def-63-3

> [!definition] Definition §63.4: Covariance Matrix
> The (sample) **covariance matrix** of the observations is the $p \times p$ matrix
>
> $$
> S = \frac{1}{N - 1} BB^T ,
> $$
>
> where $B$ is the matrix of observations in mean-deviation form.
>
> *Lay: 7.5 (text)*

^def-63-4

> [!theorem] Proposition §63.1: The Covariance Matrix Is Positive Semidefinite
> Any matrix of the form $BB^T$ is symmetric and positive semidefinite; hence so is the covariance matrix $S$. Its eigenvalues are real and nonnegative.
>
> *Lay: 7.5 (text; Exercise 25 of Section 7.2)*

^prop-63-1

> [!proof]+ Proof
> $(BB^T)^T = B^{TT}B^T = BB^T$, so $BB^T$ is symmetric. For every $\mathbf{x}$ in $\mathbb{R}^p$,
>
> $$
> \mathbf{x}^T(BB^T)\mathbf{x} = (B^T\mathbf{x})^T(B^T\mathbf{x}) = \|B^T\mathbf{x}\|^2 \ge 0 ,
> $$
>
> so the quadratic form of $BB^T$ is positive semidefinite ([[§59★ Quadratic Forms#^def-59-4|Definition §59.4]]). Multiplying by $\frac{1}{N-1} > 0$ (for $N \ge 2$) preserves both properties. The eigenvalues of $S$ are real ([[§58★ Diagonalization of Symmetric Matrices#^thm-58-3|Theorem §58.3]]) and nonnegative ([[§59★ Quadratic Forms#^prop-59-5|Proposition §59.5]]).

^pf-63-1

*Uses:* [[§59★ Quadratic Forms#^def-59-4|Def. §59.4]], [[§59★ Quadratic Forms#^prop-59-5|§59.5]], [[§58★ Diagonalization of Symmetric Matrices#^thm-58-3|§58.3]]

> [!remark]- Connections
> - Rigorous treatment: $T^*T$ (here $T = B^T$) is a positive operator, [[§27 Singular Value Decomposition#^ladr-7-64|LADR 7.64]](a); and conversely every positive operator has this form, [[§25 Positive Operators#^ladr-7-38|LADR 7.38]](f).
> - A Wishart matrix is the sample covariance matrix of $M$ independent mean-zero Gaussian observations, so by this proposition a random mass matrix of Wishart form has no tachyon; the population version, that every covariance matrix is positive semidefinite, is proved the same way ([[§R3.6 Wishart Matrices and the Marchenko–Pastur Law#^thm-r3-6-2|Thesis Thm. §R3.6.2]], [[§R2.5 Multivariate Gaussian Vectors#^thm-r2-5-7|Thesis Thm. §R2.5.7]]).

> [!definition] Definition §63.5: Variance
> Let $S = [s_{ij}]$ be the covariance matrix, and let $\mathbf{X}$ represent a vector that varies over the set of observation vectors, with coordinates $x_1, \dots, x_p$ (so $x_1$, for example, is a scalar that varies over the set of first coordinates of $\mathbf{X}_1, \dots, \mathbf{X}_N$).
>
> For $j = 1, \dots, p$, the diagonal entry $s_{jj}$ is the **variance** of $x_j$. It measures the spread of the values of $x_j$: if $m_j$ is the $j$th entry of $\mathbf{M}$, then $s_{jj} = \frac{1}{N-1}\sum_{k=1}^N (x_{j,k} - m_j)^2$ is the usual sample variance of the $N$ numbers $x_{j,1}, \dots, x_{j,N}$ (row $j$ of $B$ dotted with itself, divided by $N - 1$; Exercise 13).
>
> *Lay: 7.5 (text)*

^def-63-5

> [!definition] Definition §63.6: Total Variance
> The **total variance** of the data is the sum of the variances on the diagonal of $S$.
>
> *Lay: 7.5 (text)*

^def-63-6

> [!definition] Definition §63.7: Trace
> The sum of the diagonal entries of a square matrix $S$ is the **trace** of $S$, written $\operatorname{tr}(S)$. Thus $\{\text{total variance}\} = \operatorname{tr}(S)$.
>
> *Lay: 7.5 (text)*

^def-63-7

> [!definition] Definition §63.8: Covariance
> For $i \ne j$, the entry $s_{ij}$ is the **covariance** of $x_i$ and $x_j$. If $s_{ij} = 0$, then $x_i$ and $x_j$ are **uncorrelated**.
>
> Analysis of the multivariate data is greatly simplified when most or all of the variables $x_1, \dots, x_p$ are uncorrelated, that is, when the covariance matrix is diagonal or nearly diagonal.
>
> *Lay: 7.5 (text)*

^def-63-8

> [!example] Example §63.1: Sample Mean and Covariance Matrix
> Three measurements are made on each of four individuals in a random sample from a population. The observation vectors are
>
> $$
> \mathbf{X}_1 = \begin{bmatrix} 1 \\ 2 \\ 1 \end{bmatrix}, \quad \mathbf{X}_2 = \begin{bmatrix} 4 \\ 2 \\ 13 \end{bmatrix}, \quad \mathbf{X}_3 = \begin{bmatrix} 7 \\ 8 \\ 1 \end{bmatrix}, \quad \mathbf{X}_4 = \begin{bmatrix} 8 \\ 4 \\ 5 \end{bmatrix}.
> $$
>
> Compute the sample mean and the covariance matrix.
>
> **Mean.**
>
> $$
> \mathbf{M} = \frac14 \left( \begin{bmatrix} 1 \\ 2 \\ 1 \end{bmatrix} + \begin{bmatrix} 4 \\ 2 \\ 13 \end{bmatrix} + \begin{bmatrix} 7 \\ 8 \\ 1 \end{bmatrix} + \begin{bmatrix} 8 \\ 4 \\ 5 \end{bmatrix} \right) = \frac14 \begin{bmatrix} 20 \\ 16 \\ 20 \end{bmatrix} = \begin{bmatrix} 5 \\ 4 \\ 5 \end{bmatrix}.
> $$
>
> **Mean-deviation form.** Subtracting $\mathbf{M}$ from each $\mathbf{X}_k$,
>
> $$
> \hat{\mathbf{X}}_1 = \begin{bmatrix} -4 \\ -2 \\ -4 \end{bmatrix}, \quad \hat{\mathbf{X}}_2 = \begin{bmatrix} -1 \\ -2 \\ 8 \end{bmatrix}, \quad \hat{\mathbf{X}}_3 = \begin{bmatrix} 2 \\ 4 \\ -4 \end{bmatrix}, \quad \hat{\mathbf{X}}_4 = \begin{bmatrix} 3 \\ 0 \\ 0 \end{bmatrix},
> \qquad
> B = \begin{bmatrix} -4 & -1 & 2 & 3 \\ -2 & -2 & 4 & 0 \\ -4 & 8 & -4 & 0 \end{bmatrix}.
> $$
>
> (Each row of $B$ sums to $0$.)
>
> **Covariance matrix.** With $N - 1 = 3$,
>
> $$
> S = \frac13 \begin{bmatrix} -4 & -1 & 2 & 3 \\ -2 & -2 & 4 & 0 \\ -4 & 8 & -4 & 0 \end{bmatrix} \begin{bmatrix} -4 & -2 & -4 \\ -1 & -2 & 8 \\ 2 & 4 & -4 \\ 3 & 0 & 0 \end{bmatrix}
> = \frac13 \begin{bmatrix} 30 & 18 & 0 \\ 18 & 24 & -24 \\ 0 & -24 & 96 \end{bmatrix} = \begin{bmatrix} 10 & 6 & 0 \\ 6 & 8 & -8 \\ 0 & -8 & 32 \end{bmatrix}.
> $$
>
> (For instance, the $(1,1)$-entry is $\frac13(16 + 1 + 4 + 9) = 10$ and the $(2,3)$-entry is $\frac13(8 - 16 - 16 + 0) = -8$.)
>
> **Reading $S$.** The variance of $x_1$ is $10$ and the variance of $x_3$ is $32$: the third entries of the observation vectors are more spread out than the first entries. The total variance is $\operatorname{tr}(S) = 10 + 8 + 32 = 50$. The covariance of $x_1$ and $x_3$ is $0$ (the $(1,3)$-entry), so $x_1$ and $x_3$ are uncorrelated.
>
> *Lay: Example 7.5.3 and text*

^ex-63-1

## Principal Component Analysis

For simplicity, assume that the matrix of observations $[\,\mathbf{X}_1\ \cdots\ \mathbf{X}_N\,]$ is already in mean-deviation form. The goal of principal component analysis is to find an orthogonal $p \times p$ matrix $P = [\,\mathbf{u}_1\ \cdots\ \mathbf{u}_p\,]$ that determines a change of variable $\mathbf{X} = P\mathbf{Y}$,

$$
\begin{bmatrix} x_1 \\ x_2 \\ \vdots \\ x_p \end{bmatrix} = [\,\mathbf{u}_1\ \ \mathbf{u}_2\ \cdots\ \mathbf{u}_p\,] \begin{bmatrix} y_1 \\ y_2 \\ \vdots \\ y_p \end{bmatrix},
$$

with the property that the new variables $y_1, \dots, y_p$ are uncorrelated and are arranged in order of decreasing variance. Each observation vector $\mathbf{X}_k$ receives a "new name" $\mathbf{Y}_k$ with $\mathbf{X}_k = P\mathbf{Y}_k$: $\mathbf{Y}_k$ is the coordinate vector of $\mathbf{X}_k$ relative to the columns of $P$, and $\mathbf{Y}_k = P^{-1}\mathbf{X}_k = P^T\mathbf{X}_k$.

> [!theorem] Proposition §63.2: Covariance After a Change of Variable
> Let $\mathbf{X}_1, \dots, \mathbf{X}_N$ in $\mathbb{R}^p$ be in mean-deviation form with covariance matrix $S$, let $P$ be a $p \times p$ matrix, and let $\mathbf{Y}_k = P^T\mathbf{X}_k$ for $k = 1, \dots, N$. Then $\mathbf{Y}_1, \dots, \mathbf{Y}_N$ are in mean-deviation form, and their covariance matrix is $P^TSP$.
>
> *Lay: 7.5 (text; Exercise 11)*

^prop-63-2

> [!proof]+ Proof
> Let $X = [\,\mathbf{X}_1\ \cdots\ \mathbf{X}_N\,]$ and $Y = [\,\mathbf{Y}_1\ \cdots\ \mathbf{Y}_N\,] = P^TX$. Let $\mathbf{w}$ be the vector in $\mathbb{R}^N$ with every entry $1$. Mean-deviation form of the $\mathbf{X}_k$ means $X\mathbf{w} = \mathbf{X}_1 + \cdots + \mathbf{X}_N = \mathbf{0}$. Then $Y\mathbf{w} = P^TX\mathbf{w} = \mathbf{0}$, so the $\mathbf{Y}_k$ are in mean-deviation form too, and their covariance matrix is
>
> $$
> \frac{1}{N-1} YY^T = \frac{1}{N-1} P^TX (P^TX)^T = \frac{1}{N-1} P^T XX^T P = P^T \Big( \frac{1}{N-1} XX^T \Big) P = P^TSP .
> $$

^pf-63-2

*Uses:* [[§63★ Applications to Image Processing and Statistics#^def-63-3|Def. §63.3]], [[§63★ Applications to Image Processing and Statistics#^def-63-4|Def. §63.4]]

So the desired orthogonal matrix $P$ is one that makes $P^TSP$ diagonal. Let $D$ be a diagonal matrix with the eigenvalues $\lambda_1, \dots, \lambda_p$ of $S$ on the diagonal, arranged so that $\lambda_1 \ge \lambda_2 \ge \cdots \ge \lambda_p \ge 0$, and let $P$ be an orthogonal matrix whose columns are corresponding unit eigenvectors $\mathbf{u}_1, \dots, \mathbf{u}_p$ (Spectral Theorem, [[§58★ Diagonalization of Symmetric Matrices#^thm-58-3|Theorem §58.3]]). Then $S = PDP^T$ and $P^TSP = D$: the new variables are uncorrelated, with variances $\lambda_1 \ge \cdots \ge \lambda_p$.

> [!definition] Definition §63.9: Principal Components
> The unit eigenvectors $\mathbf{u}_1, \dots, \mathbf{u}_p$ of the covariance matrix $S$, ordered by decreasing eigenvalue, are called the **principal components** of the data (in the matrix of observations). The **first principal component** is the eigenvector corresponding to the largest eigenvalue of $S$, the **second principal component** is the eigenvector corresponding to the second largest eigenvalue, and so on.
>
> The first principal component determines the new variable $y_1$: if $c_1, \dots, c_p$ are the entries of $\mathbf{u}_1$, then, since $\mathbf{u}_1^T$ is the first row of $P^T$, the equation $\mathbf{Y} = P^T\mathbf{X}$ gives
>
> $$
> y_1 = \mathbf{u}_1^T\mathbf{X} = c_1x_1 + c_2x_2 + \cdots + c_px_p ,
> $$
>
> a linear combination of the original variables with the entries of $\mathbf{u}_1$ as weights. In the same way $\mathbf{u}_2$ determines $y_2$, and so on.
>
> *Lay: 7.5, Definition and text*

^def-63-9

> [!remark] Remark: Method — Principal Component Analysis
> 1. Arrange the data as a $p \times N$ matrix of observations and compute the sample mean $\mathbf{M}$.
> 2. Subtract $\mathbf{M}$ from every column to get $B$ in mean-deviation form, and compute $S = \frac{1}{N-1}BB^T$.
> 3. Find the eigenvalues $\lambda_1 \ge \cdots \ge \lambda_p \ge 0$ of $S$ and corresponding unit eigenvectors $\mathbf{u}_1, \dots, \mathbf{u}_p$: the principal components.
> 4. The new variables are $y_j = \mathbf{u}_j^T\mathbf{X}$ (with $\mathbf{X}$ in mean-deviation form); $y_j$ has variance $\lambda_j$, and $y_j$ explains the fraction $\lambda_j/\operatorname{tr}(S)$ of the total variance ([[§63★ Applications to Image Processing and Statistics#^prop-63-3|Proposition §63.3]]).
> 5. Keep the first few $y_j$ that together explain most of the variance; the data are essentially that many-dimensional.
>
> For large data sets, steps 2–3 are carried out with the SVD instead ([[§63★ Applications to Image Processing and Statistics#^prop-63-5|Proposition §63.5]]).

^rem-63-1

> [!example] Example §63.2: Principal Components of a Satellite Image
> The initial data for the multispectral image of Railroad Valley, Nevada (three spectral bands, [[§63★ Applications to Image Processing and Statistics#^def-63-1|Definition §63.1]]) consisted of 4 million vectors in $\mathbb{R}^3$, with covariance matrix
>
> $$
> S = \begin{bmatrix} 2382.78 & 2611.84 & 2136.20 \\ 2611.84 & 3106.47 & 2553.90 \\ 2136.20 & 2553.90 & 2650.71 \end{bmatrix}.
> $$
>
> Find the principal components of the data, list the new variable determined by the first principal component, and compute the percentages of the total variance explained by the three components.
>
> **Principal components.** The eigenvalues of $S$ (computed numerically) and the associated unit eigenvectors are
>
> $$
> \lambda_1 = 7614.23, \quad \lambda_2 = 427.63, \quad \lambda_3 = 98.10; \qquad
> \mathbf{u}_1 = \begin{bmatrix} .5417 \\ .6295 \\ .5570 \end{bmatrix}, \quad
> \mathbf{u}_2 = \begin{bmatrix} -.4894 \\ -.3026 \\ .8179 \end{bmatrix}, \quad
> \mathbf{u}_3 = \begin{bmatrix} .6834 \\ -.7157 \\ .1441 \end{bmatrix}.
> $$
>
> (Each $\mathbf{u}_j$ is determined only up to sign.) Using two decimal places, the variable for the first principal component is
>
> $$
> y_1 = .54x_1 + .63x_2 + .56x_3 .
> $$
>
> The values of $x_1$, $x_2$, $x_3$, converted to a gray scale, give the photographs of the region in the three spectral bands; at each pixel, the gray value of $y_1$, a weighted combination of the three intensities, gives a fourth photograph that "displays" the first principal component. In the variables $y_1, y_2, y_3$ the covariance matrix is $D = \operatorname{diag}(7614.23,\ 427.63,\ 98.10)$.
>
> **Percentages of variance.** The total variance is
>
> $$
> \operatorname{tr}(D) = 7614.23 + 427.63 + 98.10 = 8139.96 ,
> $$
>
> which equals $\operatorname{tr}(S) = 2382.78 + 3106.47 + 2650.71 = 8139.96$, as [[§63★ Applications to Image Processing and Statistics#^prop-63-3|Proposition §63.3]] predicts. The components explain
>
> $$
> \frac{7614.23}{8139.96} = 93.5\%, \qquad \frac{427.63}{8139.96} = 5.3\%, \qquad \frac{98.10}{8139.96} = 1.2\%
> $$
>
> of the total variance. In a sense, $93.5\%$ of the information collected by Landsat for the region is displayed in the photograph of $y_1$, with $5.3\%$ in that of $y_2$ and only $1.2\%$ left for $y_3$.
>
> **Interpretation.** The values of $y_3$ are all close to zero, so geometrically the data points lie nearly in the plane $y_3 = 0$; and $y_2$ also has relatively small variance, so the points lie approximately along a line. The data are essentially one-dimensional, a cloud shaped like a popsicle stick.
>
> *Lay: Examples 7.5.4 and 7.5.5*

^ex-63-2

## Reducing the Dimension of Multivariate Data

Principal component analysis is valuable when most of the variation, or dynamic range, in the data is due to variations in only a few of the new variables $y_1, \dots, y_p$.

> [!theorem] Proposition §63.3: Total Variance Is Unchanged
> An orthogonal change of variable $\mathbf{X} = P\mathbf{Y}$ does not change the total variance of the data. In particular, if $S = PDP^T$ as above, then
>
> $$
> \left\{ \begin{matrix} \text{total variance} \\ \text{of } x_1, \dots, x_p \end{matrix} \right\} = \left\{ \begin{matrix} \text{total variance} \\ \text{of } y_1, \dots, y_p \end{matrix} \right\} = \operatorname{tr}(D) = \lambda_1 + \cdots + \lambda_p .
> $$
>
> The variance of $y_j$ is $\lambda_j$, and the quotient $\lambda_j/\operatorname{tr}(S)$ measures the fraction of the total variance that is "explained" or "captured" by $y_j$.
>
> *Lay: 7.5 (text; Exercise 12)*

^prop-63-3

> [!proof]+ Proof
> (Lay: "roughly speaking, this is true because left-multiplication by $P$ does not change the lengths of vectors or the angles between them"; the proof is Exercise 12.) By [[§63★ Applications to Image Processing and Statistics#^prop-63-2|Proposition §63.2]], the covariance matrix of the $\mathbf{Y}_k = P^T\mathbf{X}_k$ is $P^TSP$, so it suffices to show $\operatorname{tr}(P^TSP) = \operatorname{tr}(S)$. The trace satisfies $\operatorname{tr}(FG) = \operatorname{tr}(GF)$ whenever both products are defined (Lay's Exercise 25 of Section 5.4), since both equal $\sum_{i,j} f_{ij}g_{ji}$. With $F = P^T$ and $G = SP$:
>
> $$
> \operatorname{tr}(P^TSP) = \operatorname{tr}(SPP^T) = \operatorname{tr}(S) ,
> $$
>
> because $PP^T = I$ for an orthogonal $P$. When $P$ diagonalizes $S$, $P^TSP = D$ and the common value is $\operatorname{tr}(D) = \lambda_1 + \cdots + \lambda_p$, while the variance of $y_j$ is the $j$th diagonal entry $\lambda_j$ of $D$.

^pf-63-3

*Uses:* [[§63★ Applications to Image Processing and Statistics#^prop-63-2|§63.2]], [[§63★ Applications to Image Processing and Statistics#^def-63-6|Def. §63.6]], [[§63★ Applications to Image Processing and Statistics#^def-63-7|Def. §63.7]], [[§51 Orthogonal Sets#^def-51-5|Def. §51.5]] (orthogonal matrices: $PP^T = I$)

## Characterizations of Principal Component Variables

> [!theorem] Theorem §63.4: Principal Components Maximize Variance
> Let $y_1, \dots, y_p$ arise from a principal component analysis of a $p \times N$ matrix of observations with covariance matrix $S$, eigenvalues $\lambda_1 \ge \cdots \ge \lambda_p$ and principal components $\mathbf{u}_1, \dots, \mathbf{u}_p$.
> - (a) If $\mathbf{u}$ is any unit vector and $y = \mathbf{u}^T\mathbf{X}$, then the variance of the values of $y$ as $\mathbf{X}$ varies over the original data $\mathbf{X}_1, \dots, \mathbf{X}_N$ is $\mathbf{u}^TS\mathbf{u}$.
> - (b) The variance of $y_1$ is as large as possible: the maximum of $\mathbf{u}^TS\mathbf{u}$ over all unit vectors $\mathbf{u}$ is $\lambda_1$, attained at $\mathbf{u} = \mathbf{u}_1$.
> - (c) $y_2$ has the maximum possible variance among all variables $y = \mathbf{u}^T\mathbf{X}$ ($\|\mathbf{u}\| = 1$) that are uncorrelated with $y_1$; $y_3$ has the maximum possible variance among all such variables uncorrelated with both $y_1$ and $y_2$; and so on.
>
> *Lay: 7.5 (text)*

^thm-63-4

> [!proof]+ Proof
> (Lay states (a), "turns out to be", and deduces (b)–(c) from Theorem 8 of Section 7.3; for (b), Theorem 6 is the relevant one. Here are the details.) Work with the data in mean-deviation form, $B = [\,\hat{\mathbf{X}}_1\ \cdots\ \hat{\mathbf{X}}_N\,]$; subtracting the mean of the $\mathbf{X}_k$ from $\mathbf{u}^T\mathbf{X}_k$ gives $\mathbf{u}^T\hat{\mathbf{X}}_k$.
>
> **(a)** The values of $y$ in mean-deviation form are the entries of the row vector $\mathbf{u}^TB$, so their variance is $\frac{1}{N-1}(\mathbf{u}^TB)(\mathbf{u}^TB)^T = \mathbf{u}^T\big(\frac{1}{N-1}BB^T\big)\mathbf{u} = \mathbf{u}^TS\mathbf{u}$. More generally, the covariance of $y = \mathbf{u}^T\mathbf{X}$ and $y' = \mathbf{u}'^T\mathbf{X}$ is $\frac{1}{N-1}(\mathbf{u}^TB)(\mathbf{u}'^TB)^T = \mathbf{u}^TS\mathbf{u}'$.
>
> **(b)** By [[§60★ Constrained Optimization#^thm-60-1|Theorem §60.1]] applied to the quadratic form $\mathbf{u}^TS\mathbf{u}$, its maximum over unit vectors is the largest eigenvalue $\lambda_1$, attained at $\mathbf{u}_1$.
>
> **(c)** By (a), the covariance of $y = \mathbf{u}^T\mathbf{X}$ with $y_i = \mathbf{u}_i^T\mathbf{X}$ is $\mathbf{u}^TS\mathbf{u}_i = \lambda_i\,\mathbf{u}^T\mathbf{u}_i$. If $\lambda_i > 0$, then $y$ is uncorrelated with $y_i$ exactly when $\mathbf{u}^T\mathbf{u}_i = 0$. So if $\lambda_1, \dots, \lambda_{k-1} > 0$, the variables uncorrelated with $y_1, \dots, y_{k-1}$ are those with $\mathbf{u}$ orthogonal to $\mathbf{u}_1, \dots, \mathbf{u}_{k-1}$, and by [[§60★ Constrained Optimization#^thm-60-3|Theorem §60.3]] the maximum of $\mathbf{u}^TS\mathbf{u}$ over them is $\lambda_k$, attained at $\mathbf{u}_k$, that is, by $y_k$. (If some of $\lambda_1, \dots, \lambda_{k-1}$ are $0$, let $j$ be the first index with $\lambda_j = 0$. Being uncorrelated with $y_1, \dots, y_{j-1}$ forces $\mathbf{u} \perp \mathbf{u}_1, \dots, \mathbf{u}_{j-1}$, and then $\mathbf{u}^TS\mathbf{u} \le \lambda_j = 0$ by [[§60★ Constrained Optimization#^thm-60-3|Theorem §60.3]] (by [[§60★ Constrained Optimization#^thm-60-1|Theorem §60.1]] if $j = 1$). So the maximum is $0 = \lambda_k$, and it is attained by $y_k$, which is uncorrelated with every $y_i$ because $\mathbf{u}_k^TS\mathbf{u}_i = \lambda_i\,\mathbf{u}_k^T\mathbf{u}_i = 0$ for $i \ne k$.)

^pf-63-4

*Uses:* [[§60★ Constrained Optimization#^thm-60-1|§60.1]], [[§60★ Constrained Optimization#^thm-60-3|§60.3]], [[§63★ Applications to Image Processing and Statistics#^def-63-4|Def. §63.4]], [[§63★ Applications to Image Processing and Statistics#^def-63-5|Def. §63.5]], [[§63★ Applications to Image Processing and Statistics#^def-63-8|Def. §63.8]], [[§63★ Applications to Image Processing and Statistics#^prop-63-1|§63.1]]

> [!remark]- Connections
> - Keeping the first $k$ principal components is the best rank-$k$ approximation of the data matrix $B^T/\sqrt{N-1}$: truncate its SVD after $k$ terms, [[§28 Consequences of Singular Value Decomposition#^ladr-7-92|LADR 7.92]] (Eckart–Young; there in the operator norm, with error $\sigma_{k+1}$).

> [!theorem] Proposition §63.5: Principal Component Analysis by the SVD
> Let $B$ be a $p \times N$ matrix of observations in mean-deviation form, and let $A = \frac{1}{\sqrt{N-1}}B^T$. Then $A^TA$ is the covariance matrix $S$. The squares of the singular values of $A$ are the $p$ eigenvalues of $S$, and the right singular vectors of $A$ are the principal components of the data.
>
> *Lay: 7.5, Numerical Note*

^prop-63-5

> [!proof]+ Proof
> $A^TA = \frac{1}{N-1}(B^T)^TB^T = \frac{1}{N-1}BB^T = S$. By [[§61★ The Singular Value Decomposition#^def-61-1|Definition §61.1]], the singular values of the $N \times p$ matrix $A$ are the square roots of the $p$ eigenvalues of $A^TA = S$, in decreasing order. In an SVD $A = U\Sigma V^T$, the right singular vectors (the columns of $V$) are orthonormal eigenvectors of $A^TA = S$ for those eigenvalues, in the same order ([[§61★ The Singular Value Decomposition#^def-61-2|Definition §61.2]]): they are principal components.

^pf-63-5

*Uses:* [[§61★ The Singular Value Decomposition#^def-61-1|Def. §61.1]], [[§61★ The Singular Value Decomposition#^def-61-2|Def. §61.2]], [[§63★ Applications to Image Processing and Statistics#^def-63-4|Def. §63.4]]

The SVD is the main tool for principal component analysis in practice: iterative calculation of the SVD of $A$ is faster and more accurate than an eigenvalue decomposition of $S$ (forming $BB^T$ squares the errors, as noted in [[§62★ The Singular Value Decomposition in Applications#^rem-62-1|§51, Remark: Numerical Note]]). This matters especially in hyperspectral image processing, with $p = 224$ spectral bands; principal component analysis is then completed in seconds on specialized workstations.

> [!example] Example §63.3: A Size Index for Weights and Heights
> The weights and heights of five boys are:
>
> | Boy | #1 | #2 | #3 | #4 | #5 |
> |---|---|---|---|---|---|
> | Weight (lb) | 120 | 125 | 125 | 135 | 145 |
> | Height (in.) | 61 | 60 | 64 | 68 | 72 |
>
> Find the covariance matrix, and make a principal component analysis of the data to find a single *size index* that explains most of the variation.
>
> **Covariance matrix.** The sample mean is $\mathbf{M} = \frac15(650, 325) = (130, 65)$. Subtracting it from the columns of the table,
>
> $$
> B = \begin{bmatrix} -10 & -5 & -5 & 5 & 15 \\ -4 & -5 & -1 & 3 & 7 \end{bmatrix},
> \qquad
> S = \frac{1}{5 - 1} BB^T = \frac14 \begin{bmatrix} 400 & 190 \\ 190 & 100 \end{bmatrix} = \begin{bmatrix} 100.0 & 47.5 \\ 47.5 & 25.0 \end{bmatrix}.
> $$
>
> (Entries of $BB^T$: $100 + 25 + 25 + 25 + 225 = 400$; $40 + 25 + 5 + 15 + 105 = 190$; $16 + 25 + 1 + 9 + 49 = 100$.)
>
> **Principal components.** Since $S$ is $2 \times 2$, this can be done by hand. The characteristic equation is $\lambda^2 - 125\lambda + (2500 - 2256.25) = \lambda^2 - 125\lambda + 243.75 = 0$, so
>
> $$
> \lambda = \frac{125 \pm \sqrt{125^2 - 4(243.75)}}{2} = \frac{125 \pm \sqrt{14650}}{2}, \qquad \lambda_1 \approx 123.02, \quad \lambda_2 \approx 1.98 .
> $$
>
> For $\lambda_1$, the first row of $S - \lambda_1 I$ is $(-23.02,\ 47.5)$, so $(47.5,\ 23.02)$ is an eigenvector; dividing by its length $\approx 52.78$ gives the first principal component
>
> $$
> \mathbf{u} = \begin{bmatrix} .900 \\ .436 \end{bmatrix}.
> $$
>
> **Size index.** Set
>
> $$
> y = .900\,\hat w + .436\,\hat h ,
> $$
>
> where $\hat w$ and $\hat h$ are weight and height in mean-deviation form. The variance of this index over the data set is $\lambda_1 \approx 123.02$. Since the total variance is $\operatorname{tr}(S) = 100 + 25 = 125$, the size index accounts for practically all ($123.02/125 \approx 98.4\%$) of the variance of the data.
>
> **The line of the first principal component.** In parametric vector form, $\mathbf{x} = \mathbf{M} + t\mathbf{u}$. It is the best approximation to the data in the sense that the sum of the squares of the *orthogonal* distances from the data points to the line is minimized: principal component analysis is equivalent to **orthogonal regression**. (Compare the least-squares line of [[§55 Applications to Linear Models#^def-55-3|Definition §55.3]], which minimizes *vertical* distances.)
>
> *Lay: 7.5, Practice Problems 1–2*

^ex-63-3

![[m235-52-1.svg]]
*[[§63★ Applications to Image Processing and Statistics#^ex-63-3|Example §63.3]]: the five boys (black, with axes starting at $w = 112$, $h = 54$), their mean $\mathbf{M}$ and the first principal component $\mathbf{u}$ (green). The blue line $\mathbf{M} + t\mathbf{u}$ minimizes the sum of the squared perpendicular distances (red). Both axes use the same scale, so perpendicular looks perpendicular; the second principal component, with variance only $1.98$, measures the small spread across the line.*
