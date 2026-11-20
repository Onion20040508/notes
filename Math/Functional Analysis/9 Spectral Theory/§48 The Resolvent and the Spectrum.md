---
type: section
subject: "[[Functional Analysis]]"
chapter: 9
section: 48
tags: [functional-analysis, math556]
---
← [[§47 Weak and Strong Analyticity]] · ↑ [[· 9 Spectral Theory]] · [[§49 Elementary Spectral Theory]] →

*Stage: maps — Thread: invertibility. $\lambda I - M$ can fail to be invertible by not being one-to-one, by having a dense range that is not everything, or by having a range that is not dense: point, continuous and residual spectrum.*

*Lecture 21 (Tue Nov 17), second part. Source: the handwritten notes of the lecture; there is no recording. The steps that the notes leave out, and the items marked as such, are filled in. The definitions were checked against Lax §17.1, §20.1 and §32.1; the division of the spectrum into three parts and the two examples of [[§48 The Resolvent and the Spectrum|§48]] follow the lecture, and Lax does not use this division.*

## Eigenvalues of Matrices

Recall: let $A$ be an $n \times n$ matrix, acting as $A : \mathbb{R}^n \to \mathbb{R}^n$ by $A(x) = Ax$ for $x = (x_1, \ldots, x_n)^T$. A number $\lambda$ is an **eigenvalue** of $A$ ([[§14 Invariant Subspaces#^ladr-5-5|LADR 5.5]]) if there is $x_0 \in \mathbb{R}^n$, $x_0 \neq 0$, such that $A x_0 = \lambda x_0$. The following are equivalent:

1. $\lambda$ is an eigenvalue of $A$;
2. $\lambda I - A$ is not one-to-one;
3. $\lambda I - A$ is not onto.

(1) $\Leftrightarrow$ (2): $A x_0 = \lambda x_0$ means $(\lambda I - A) x_0 = 0$, and a linear map is one-to-one exactly when its null space is $\{0\}$. (2) $\Leftrightarrow$ (3): for a linear map of $\mathbb{R}^n$ to itself the dimensions of the null space and of the range add up to $n$ ([[§8 Null Spaces and Ranges#^ladr-3-21|LADR 3.21]]), so the null space is $\{0\}$ exactly when the range is all of $\mathbb{R}^n$. In infinite dimensions (2) and (3) are no longer equivalent: on $\ell^2$ the right shift is one-to-one and not onto, and the left shift is onto and not one-to-one (Examples [[§45 Convergence of Operators#^ex-45-2|§45.2]] and [[§45 Convergence of Operators#^ex-45-1|§45.1]]). This is why the eigenvalues have to be replaced by a larger set.

> [!example] Example §48.1: Eigenvalues and Stability
> Let $A = (\lambda_0)$ be a $1 \times 1$ matrix, $\lambda_0 \in \mathbb{R}$, and consider the differential equation
>
> $$
> \frac{dx}{dt} = \lambda_0\, x , \qquad \text{with solution} \qquad x(t) = x(0)\, e^{\lambda_0 t} .
> $$
>
> The constant function $x \equiv 0$ is a solution: $0$ is an **equilibrium state**.
> - If $\lambda_0 < 0$: $x(t) \to 0$ as $t \to \infty$. The equilibrium state $0$ is **stable**.
> - If $\lambda_0 > 0$: $|x(t)| \to \infty$ as $t \to \infty$ (for $x(0) \neq 0$). The equilibrium state $0$ is **unstable**.
> - If $\lambda_0 = 0$:     $x(t) = x(0)$ for all $t$. Solutions neither decay nor grow: a solution that starts near $0$ stays near $0$ but does not return to it, and every constant is an equilibrium state.
>
> So the sign of the eigenvalue decides the behaviour of the solutions for large times. For a system $\frac{dx}{dt} = Ax$ with an $n \times n$ matrix $A$ the eigenvalues of $A$ play the same role, and for equations in infinite-dimensional spaces the spectrum does.
>
> ![[m556-48-1.svg]]
>
> The solutions $x(0)\, e^{\lambda_0 t}$ for the three signs of $\lambda_0$. (Not from lecture; figure added.)

^ex-48-1

> [!remark]- Connections
> - Equilibrium solutions and their stability for $x' = Ax$: [[§37 Homogeneous Linear Systems with Constant Coefficients#^def-37-2|ODE Def. §37.2]]; the scalar equation $y' = ry$: [[§9 Autonomous Differential Equations and Population Dynamics#^def-9-2|ODE Def. §9.2]].

## Resolvent Set, Resolvent and Spectrum

Throughout this section $X$ is a Banach space over $\mathbb{C}$, and $M$ is one of the following:

- (a) a bounded linear map $M \in \mathcal{L}(X, X)$; then its domain is $D(M) = X$;
- (b) more generally, a closed linear map $M : D(M) \to X$ whose domain $D(M)$ is a linear subspace of $X$ (Definition [[§39 Solving Mx = y#^def-39-5|§39.5]]).

Case (a) is contained in case (b), since continuous maps are closed (Example [[§39 Solving Mx = y#^ex-39-1|§39.1]]). The lecture states the definitions for (a) and notes that they apply to (b) as well. For $\lambda \in \mathbb{C}$, $\lambda I - M$ denotes the linear map $D(M) \to X$, $x \mapsto \lambda x - Mx$, where $I$ is the identity.

> [!definition] Definition §48.1: Resolvent Set
> Let $X$ be a Banach space over $\mathbb{C}$ and $M \in \mathcal{L}(X, X)$ (or $M : D(M) \to X$ a closed linear map with $D(M) \subset X$). A number $\lambda \in \mathbb{C}$ belongs to $\rho(M)$ if $\lambda I - M$ is **invertible**, that is, if $\lambda I - M : X \to X$ (in the closed case, $\lambda I - M : D(M) \to X$) is one-to-one and onto:
>
> $$
> \rho(M) = \{ \lambda \in \mathbb{C} : \lambda I - M \text{ is invertible} \} .
> $$
>
> $\rho(M)$ is called the **resolvent set** of $M$.
>
> *Lax: §17.1, definition after Thm 2 (for an element of a Banach algebra); §20.1, opening paragraph; §32.1, definition before Thm 5 (unbounded operators in a Hilbert space)*

^def-48-1

> [!remark]- Connections
> - In finite dimensions: invertible means injective and surjective, [[§10 Invertibility and Isomorphisms#^ladr-3-63|LADR 3.63]], and there the two are equivalent, [[§10 Invertibility and Isomorphisms#^ladr-3-65|LADR 3.65]].
> - Closed maps and their domains: [[§39 Solving Mx = y#^def-39-5|Def. §39.5]].

For $\lambda \in \rho(M)$ the inverse map $(\lambda I - M)^{-1} : X \to X$ exists and is linear. The definition does not ask the inverse to be bounded. It is bounded automatically; for a closed map this is the check that the lecture asks for, and the next lemma prepares it.

> [!theorem] Lemma §48.1: Closed Maps: Shifts and Inverses
> *(Not from lecture; filled in.)* Let $X$ be a normed linear space over $\mathbb{C}$ and $T : D(T) \to X$ a closed linear map with $D(T) \subset X$.
>
> 1. For every $\lambda \in \mathbb{C}$ the map $\lambda I - T : D(T) \to X$ is closed.
> 2. If $T$ is one-to-one, then the inverse $T^{-1} : R(T) \to X$, with domain the range $R(T)$ of $T$, is a closed linear map.

^lem-48-1

> [!proof]+ Proof
> (1) Let $x_n \in D(T)$ with $x_n \to x$ in $X$ and $(\lambda I - T) x_n \to y$ in $X$. Then
>
> $$
> T x_n = \lambda x_n - (\lambda I - T) x_n \to \lambda x - y .
> $$
>
> Since $T$ is closed (Definition [[§39 Solving Mx = y#^def-39-5|§39.5]]), $x \in D(T)$ and $Tx = \lambda x - y$, that is, $(\lambda I - T) x = y$. So $\lambda I - T$ is closed.
>
> (2) $T^{-1}$ is linear: if $y_1 = Tx_1$ and $y_2 = Tx_2$, then $T(c_1 x_1 + c_2 x_2) = c_1 y_1 + c_2 y_2$, so $T^{-1}(c_1 y_1 + c_2 y_2) = c_1 x_1 + c_2 x_2$. Let $y_n \in R(T)$ with $y_n \to y$ in $X$ and $T^{-1} y_n \to x$ in $X$. Put $x_n = T^{-1} y_n \in D(T)$. Then $x_n \to x$ and $T x_n = y_n \to y$. Since $T$ is closed, $x \in D(T)$ and $Tx = y$. Hence $y \in R(T)$ and $T^{-1} y = x$, which is what Definition [[§39 Solving Mx = y#^def-39-5|§39.5]] asks of $T^{-1}$. (In terms of graphs: the graph of $T^{-1}$ is the graph of $T$ with the two components exchanged, and exchanging the components maps closed sets of $X \times X$ to closed sets.)

^pf-48-1

*Uses:* [[§39 Solving Mx = y#^def-39-5|Def. §39.5]]

> [!theorem] Proposition §48.2: The Inverse of $\lambda I - M$ is Bounded
> Let $X$ be a Banach space over $\mathbb{C}$, let $M \in \mathcal{L}(X, X)$ or $M : D(M) \to X$ a closed linear map with $D(M) \subset X$, and let $\lambda \in \rho(M)$. Then
>
> $$
> (\lambda I - M)^{-1} \in \mathcal{L}(X, X) .
> $$
>
> *Lax: §20.1, opening paragraph (for $M \in \mathcal{L}(X, X)$)*

^prop-48-2

> [!proof]+ Proof
> *$M \in \mathcal{L}(X, X)$.* Then $\lambda I - M \in \mathcal{L}(X, X)$, since $\mathcal{L}(X, X)$ is a linear space (Theorem [[§30 Boundedness and Continuity#^thm-30-8|§30.8]]). By assumption $\lambda I - M : X \to X$ is one-to-one and onto, and $X$ is a Banach space. By Banach's inverse mapping theorem (Theorem [[§39 Solving Mx = y#^thm-39-2|§39.2]]), which is a consequence of the open mapping theorem (Theorem [[§41 The Open Mapping Theorem and Its Consequences#^thm-41-2|§41.2]]), $(\lambda I - M)^{-1}$ is a bounded linear map.
>
> *$M$ closed.* By Lemma [[§48 The Resolvent and the Spectrum#^lem-48-1|§48.1]](1), $\lambda I - M : D(M) \to X$ is a closed linear map. It is one-to-one, so by Lemma [[§48 The Resolvent and the Spectrum#^lem-48-1|§48.1]](2) its inverse $(\lambda I - M)^{-1}$ is a closed linear map with domain $R(\lambda I - M)$, and $R(\lambda I - M) = X$ because $\lambda I - M$ is onto. A closed linear map that is defined on all of the Banach space $X$, with values in the Banach space $X$, is bounded by the closed graph theorem (Theorem [[§41 The Open Mapping Theorem and Its Consequences#^thm-41-4|§41.4]]). So $(\lambda I - M)^{-1} \in \mathcal{L}(X, X)$; its values lie in $D(M)$.

^pf-48-2

*Uses:* [[§30 Boundedness and Continuity#^thm-30-8|§30.8]], [[§39 Solving Mx = y#^thm-39-2|§39.2]], [[§41 The Open Mapping Theorem and Its Consequences#^thm-41-2|§41.2]], [[§48 The Resolvent and the Spectrum#^lem-48-1|§48.1]], [[§41 The Open Mapping Theorem and Its Consequences#^thm-41-4|§41.4]]

> [!remark]- Connections
> - Tools: [[Banach's Inverse Mapping Theorem]] (bounded $M$), [[Closed Graph Theorem]] (closed $M$).

> [!definition] Definition §48.2: Resolvent
> Let $X$ and $M$ be as in Definition [[§48 The Resolvent and the Spectrum#^def-48-1|§48.1]]. For $\lambda \in \rho(M)$ put
>
> $$
> R(\lambda; M) = (\lambda I - M)^{-1} \in \mathcal{L}(X, X) .
> $$
>
> The map $R(\,\cdot\,; M) : \rho(M) \to \mathcal{L}(X, X)$, $\lambda \mapsto (\lambda I - M)^{-1}$, is called the **resolvent** of $M$.
>
> *Lax: §17.1, Thm 3(ii)*

^def-48-2

> [!remark]- Connections
> - The resolvent is the function to which [[Dunford's Theorem]] and the analytic functions of [[§47 Weak and Strong Analyticity|§47]] are applied.

By Proposition [[§48 The Resolvent and the Spectrum#^prop-48-2|§48.2]] the resolvent indeed takes its values in $\mathcal{L}(X, X)$. (The letter $R$ also denotes ranges, as in $R(\lambda I - M)$; the resolvent is always written with the two arguments $\lambda; M$.)

> [!definition] Definition §48.3: Spectrum
> Let $X$ and $M$ be as in Definition [[§48 The Resolvent and the Spectrum#^def-48-1|§48.1]]. The **spectrum** of $M$ is the complement of the resolvent set,
>
> $$
> \sigma(M) = \mathbb{C} \setminus \rho(M) = \{ \lambda \in \mathbb{C} : \lambda I - M \text{ is not invertible} \} .
> $$
>
> *Lax: §17.1, definition after Thm 2; §32.3 (unbounded operators)*

^def-48-3

> [!remark] Remark: Invertible in $\mathcal{L}(X, X)$
> Lax defines the resolvent set and the spectrum in his Chapter 17 for an element $M$ of a Banach algebra, where “invertible” means that there is an element $N$ of the algebra with $NM = MN = I$. For the algebra $\mathcal{L}(X, X)$ this agrees with the definition above. If such an $N \in \mathcal{L}(X, X)$ exists for $\lambda I - M$, then $\lambda I - M$ is one-to-one (apply $N$ to $(\lambda I - M)x = 0$) and onto ($y = (\lambda I - M)(Ny)$). Conversely, if $\lambda I - M$ is one-to-one and onto, then $N = (\lambda I - M)^{-1}$ belongs to $\mathcal{L}(X, X)$ by Proposition [[§48 The Resolvent and the Spectrum#^prop-48-2|§48.2]]. Lax makes the same point at the beginning of his §20.1.

^rem-48-1

## Classifying the Spectrum

Let $\lambda \in \sigma(M)$, so that $\lambda I - M : D(M) \to X$ is not invertible. Either $\lambda I - M$ is not one-to-one; or it is one-to-one and not onto, and then its range may or may not be dense in $X$. The spectrum is divided accordingly.

> [!definition] Definition §48.4: Eigenvalue and Eigenvector
> Let $X$ and $M$ be as in Definition [[§48 The Resolvent and the Spectrum#^def-48-1|§48.1]], and $\lambda \in \mathbb{C}$. If there is $x_0 \in D(M)$, $x_0 \neq 0$, such that
>
> $$
> (\lambda I - M) x_0 = 0 , \qquad \text{that is,} \qquad M x_0 = \lambda x_0 ,
> $$
>
> then $\lambda$ is called an **eigenvalue** of $M$, and $x_0$ a corresponding **eigenvector**.
>
> *Lax: §20.1, after Corollary 1 of Thm 3*

^def-48-4

> [!remark]- Connections
> - In finite dimensions: eigenvalue [[§14 Invariant Subspaces#^ladr-5-5|LADR 5.5]], equivalent conditions [[§14 Invariant Subspaces#^ladr-5-7|LADR 5.7]], eigenvector [[§14 Invariant Subspaces#^ladr-5-8|LADR 5.8]].

> [!definition] Definition §48.5: Point Spectrum
> Let $X$ and $M$ be as in Definition [[§48 The Resolvent and the Spectrum#^def-48-1|§48.1]]. The **point spectrum** of $M$ is the set of its eigenvalues (Definition [[§48 The Resolvent and the Spectrum#^def-48-4|§48.4]]),
>
> $$
> \sigma_p(M) = \{ \text{eigenvalues of } M \} .
> $$
>
> Equivalently, $\lambda \in \sigma_p(M)$ if and only if $\lambda I - M$ is not one-to-one.

^def-48-5

(A linear map is one-to-one exactly when its null space is $\{0\}$, and the eigenvectors for $\lambda$ are the nonzero elements of the null space of $\lambda I - M$.)

> [!definition] Definition §48.6: Continuous Spectrum
> Let $X$ and $M$ be as in Definition [[§48 The Resolvent and the Spectrum#^def-48-1|§48.1]]. A number $\lambda \in \mathbb{C}$ belongs to the **continuous spectrum** $\sigma_c(M)$ of $M$ if $\lambda I - M$ is one-to-one but not onto, and its range is dense in $X$:
>
> $$
> R(\lambda I - M) \neq X \qquad \text{but} \qquad \overline{R(\lambda I - M)} = X .
> $$

^def-48-6

> [!definition] Definition §48.7: Residual Spectrum
> Let $X$ and $M$ be as in Definition [[§48 The Resolvent and the Spectrum#^def-48-1|§48.1]]. A number $\lambda \in \mathbb{C}$ belongs to the **residual spectrum** $\sigma_r(M)$ of $M$ if $\lambda I - M$ is one-to-one and its range is not dense in $X$:
>
> $$
> \overline{R(\lambda I - M)} \subsetneq X .
> $$

^def-48-7

> [!theorem] Proposition §48.3: The Three Parts of the Spectrum
> Let $X$ and $M$ be as in Definition [[§48 The Resolvent and the Spectrum#^def-48-1|§48.1]]. Then
>
> $$
> \sigma(M) = \sigma_p(M) \cup \sigma_c(M) \cup \sigma_r(M) ,
> $$
>
> and the three sets $\sigma_p(M)$, $\sigma_c(M)$, $\sigma_r(M)$ are pairwise disjoint.

^prop-48-3

> [!proof]+ Proof
> Let $\lambda \in \mathbb{C}$ and $T = \lambda I - M : D(M) \to X$. Exactly one of the following four cases holds:
>
> - (i) $T$ is not one-to-one;
> - (ii) $T$ is one-to-one and $R(T) = X$;
> - (iii) $T$ is one-to-one, $R(T) \neq X$ and $\overline{R(T)} = X$;
> - (iv) $T$ is one-to-one and $\overline{R(T)} \neq X$.
>
> Indeed, if $T$ is one-to-one, then either $\overline{R(T)} \neq X$, which is (iv), or $\overline{R(T)} = X$, and then either $R(T) = X$ or $R(T) \neq X$; in case (iv) also $R(T) \neq X$, because $R(T) \subset \overline{R(T)}$. By Definitions [[§48 The Resolvent and the Spectrum#^def-48-1|§48.1]], [[§48 The Resolvent and the Spectrum#^def-48-5|§48.5]], [[§48 The Resolvent and the Spectrum#^def-48-6|§48.6]] and [[§48 The Resolvent and the Spectrum#^def-48-7|§48.7]], the four cases are $\lambda \in \sigma_p(M)$, $\lambda \in \rho(M)$, $\lambda \in \sigma_c(M)$ and $\lambda \in \sigma_r(M)$, in this order. So $\mathbb{C}$ is the disjoint union of $\rho(M)$, $\sigma_p(M)$, $\sigma_c(M)$ and $\sigma_r(M)$, and $\sigma(M) = \mathbb{C} \setminus \rho(M)$ (Definition [[§48 The Resolvent and the Spectrum#^def-48-3|§48.3]]) is the disjoint union of the last three.

^pf-48-3

*Uses:* [[§48 The Resolvent and the Spectrum#^def-48-1|Def. §48.1]], [[§48 The Resolvent and the Spectrum#^def-48-5|Def. §48.5]], [[§48 The Resolvent and the Spectrum#^def-48-6|Def. §48.6]], [[§48 The Resolvent and the Spectrum#^def-48-7|Def. §48.7]], [[§48 The Resolvent and the Spectrum#^def-48-3|Def. §48.3]]

![[m556-48-2.svg]]

Where a number $\lambda \in \mathbb{C}$ falls: three questions about the map $\lambda I - M$ sort $\mathbb{C}$ into the resolvent set (blue) and the three parts of the spectrum (red). (Not from lecture; figure added.)

> [!example] Example §48.2: The Spectrum of a Matrix
> *(Not from lecture; filled in.)* Let $X = \mathbb{C}^n$ and let $A$ be an $n \times n$ matrix with complex entries, acting by $x \mapsto Ax$. A linear map of $\mathbb{C}^n$ to itself is one-to-one if and only if it is onto (as for $\mathbb{R}^n$ at the beginning of this section). So if $\lambda I - A$ is one-to-one, then $\lambda \in \rho(A)$: the cases of $\sigma_c$ and $\sigma_r$ do not occur, and
>
> $$
> \sigma(A) = \sigma_p(A) = \{ \text{eigenvalues of } A \} = \{ \lambda \in \mathbb{C} : \det(\lambda I - A) = 0 \} , \qquad \sigma_c(A) = \sigma_r(A) = \varnothing .
> $$
>
> The spectrum of a matrix is a set of at most $n$ points, and it is not empty, since the polynomial $\det(\lambda I - A)$ of degree $n$ has a root in $\mathbb{C}$ ([[Fundamental Theorem of Algebra (Liouville proof)|fundamental theorem of algebra]]). The scalars have to be complex for this: the rotation $A = \bigl( \begin{smallmatrix} 0 & -1 \\ 1 & 0 \end{smallmatrix} \bigr)$ has real entries and no real eigenvalue, and $\sigma(A) = \{ i, -i \}$.

^ex-48-2

> [!remark]- Connections
> - Every operator on a finite-dimensional complex space has an eigenvalue: [[§15 The Minimal Polynomial#^ladr-5-19|LADR 5.19]].

> [!remark] Remark: Other Uses of the Names
> Lax does not divide the spectrum in this way. At the beginning of §20.1 he only distinguishes the two ways in which a map can fail to be invertible, (a) not one-to-one and (b) not onto, and he remarks that in an infinite-dimensional space (b) can hold without (a), so that a point of the spectrum need not be an eigenvalue. The “absolutely continuous, singular and point spectra” of his §31.4 are a different division: there a symmetric operator on a Hilbert space is decomposed according to the Lebesgue decomposition of its spectral measures. The two uses of the words “point” and “continuous” should not be identified.

^rem-48-2

## Multiplication by $t$: Two Examples

In finite dimensions only the point spectrum occurs (Example [[§48 The Resolvent and the Spectrum#^ex-48-2|§48.2]]). The next two examples show that the other two parts occur for one of the simplest operators, multiplication by the variable: on $C[0,1]$ its spectrum is purely residual, and on $L^2[0,1]$ it is purely continuous. In both examples the functions are complex-valued, and

$$
(Mf)(t) = t f(t) , \qquad \bigl( (\lambda I - M) f \bigr)(t) = \lambda f(t) - t f(t) = (\lambda - t) f(t) \qquad (t \in [0,1],\ \lambda \in \mathbb{C}) .
$$

> [!example] Example §48.3: Multiplication by $t$ on $C[0,1]$
> Let $X = C[0,1]$ with the norm $\|f\| = \max_{t \in [0,1]} |f(t)|$, and let $M f(t) = t f(t)$. Then $M : C[0,1] \to C[0,1]$, $M \in \mathcal{L}(C[0,1], C[0,1])$ with $\|M\| \le 1$, and
>
> $$
> \rho(M) = \mathbb{C} \setminus [0,1] , \qquad \sigma(M) = [0,1] = \sigma_r(M) , \qquad \sigma_p(M) = \sigma_c(M) = \varnothing .
> $$

^ex-48-3

> [!proof]+ Proof
> **$M$ is bounded.** For $f \in C[0,1]$ the function $t f(t)$ is continuous, and $|t f(t)| \le |f(t)| \le \|f\|$ for $t \in [0,1]$. So $\|Mf\| \le \|f\|$, and $\|M\| \le 1$ (Proposition [[§30 Boundedness and Continuity#^prop-30-1|§30.1]](c)). (In fact $\|M\| = 1$: for $f \equiv 1$, $\|Mf\| = \max_t t = 1$.)
>
> **$\mathbb{C} \setminus [0,1] \subset \rho(M)$.** Let $\lambda \in \mathbb{C} \setminus [0,1]$. *One-to-one:* if $(\lambda I - M) f = 0$, then $(\lambda - t) f(t) = 0$ for all $t \in [0,1]$; since $\lambda - t \neq 0$ there, $f(t) \equiv 0$. *Onto:* for every $g \in C[0,1]$,
>
> $$
> (\lambda I - M) f = g \quad \Longleftrightarrow \quad (\lambda - t) f(t) = g(t) \quad \Longleftrightarrow \quad f(t) = \frac{g(t)}{\lambda - t} ,
> $$
>
> and this $f$ belongs to $C[0,1]$, as a quotient of continuous functions whose denominator has no zero on $[0,1]$. So $\lambda I - M$ is one-to-one and onto.
>
> **$[0,1] \subset \sigma_r(M)$.** Let $\lambda_0 \in [0,1]$.
>
> *$\lambda_0 I - M$ is one-to-one.* If $(\lambda_0 I - M) f(t) = (\lambda_0 - t) f(t) = 0$ for all $t$, then $f(t) = 0$ for all $t \neq \lambda_0$. Since $f$ is continuous, also $f(\lambda_0) = \lim_{t \to \lambda_0} f(t) = 0$. So $f(t) \equiv 0$ on $[0,1]$. In particular $\lambda_0 \notin \sigma_p(M)$.
>
> *Claim: $R(\lambda_0 I - M) \neq C[0,1]$, and the range is not dense.* Let $g \in R(\lambda_0 I - M)$. Then there is $f \in C[0,1]$ with $(\lambda_0 - t) f(t) = g(t)$ for all $t$; at $t = \lambda_0$ this gives $g(\lambda_0) = 0$. Hence
>
> $$
> R(\lambda_0 I - M) \subset Z := \{ g \in C[0,1] : g(\lambda_0) = 0 \} \subsetneq C[0,1] ,
> $$
>
> where $Z \neq C[0,1]$ because the constant function $1$ is not in $Z$. The set $Z$ is closed: if $g_n \in Z$ and $g_n \to g$ in the maximum norm, then $|g(\lambda_0)| = |g(\lambda_0) - g_n(\lambda_0)| \le \|g - g_n\| \to 0$, so $g \in Z$. A closed set that contains $R(\lambda_0 I - M)$ contains its closure (Definition [[§11 Normed Linear Spaces#^def-11-7|§11.7]]), so
>
> $$
> \overline{R(\lambda_0 I - M)} \subset \{ g \in C[0,1] : g(\lambda_0) = 0 \} \subsetneq C[0,1] .
> $$
>
> By Definition [[§48 The Resolvent and the Spectrum#^def-48-7|§48.7]], $\lambda_0 \in \sigma_r(M)$.
>
> **Conclusion.** $\mathbb{C} \setminus [0,1] \subset \rho(M)$ and $[0,1] \subset \sigma_r(M) \subset \sigma(M) = \mathbb{C} \setminus \rho(M)$. Hence $\rho(M) = \mathbb{C} \setminus [0,1]$ and $\sigma_r(M) = [0,1] = \sigma(M)$; by Proposition [[§48 The Resolvent and the Spectrum#^prop-48-3|§48.3]], $\sigma_p(M)$ and $\sigma_c(M)$ are empty.

^pf-ex-48-3

*Uses:* [[§30 Boundedness and Continuity#^prop-30-1|§30.1]], [[§11 Normed Linear Spaces#^def-11-7|Def. §11.7]], [[§48 The Resolvent and the Spectrum#^def-48-7|Def. §48.7]], [[§48 The Resolvent and the Spectrum#^prop-48-3|§48.3]]

![[m556-48-3.svg]]

Why the range is not dense in $C[0,1]$: every $g$ in the range vanishes at $\lambda_0$, so $\|1 - g\| \ge |1 - g(\lambda_0)| = 1$, however narrow the notch of $g$ at $\lambda_0$ is. In the maximum norm the constant $1$ stays at distance $1$ from the range. (Not from lecture; figure added.)

> [!example] Example §48.4: Multiplication by $t$ on $L^2[0,1]$
> Let $X = L^2[0,1]$ and $M f(t) = t f(t)$. Then $M : L^2[0,1] \to L^2[0,1]$, $M \in \mathcal{L}(L^2[0,1], L^2[0,1])$ with $\|M\| \le 1$, and
>
> $$
> \rho(M) = \mathbb{C} \setminus [0,1] , \qquad \sigma(M) = [0,1] = \sigma_c(M) , \qquad \sigma_p(M) = \sigma_r(M) = \varnothing .
> $$

^ex-48-4

> [!proof]+ Proof
> **$M$ is bounded.** If $f = \tilde f$ almost everywhere, then $t f(t) = t \tilde f(t)$ almost everywhere, so $M$ is defined on the elements of $L^2[0,1]$. Since $|t f(t)| \le |f(t)|$ on $[0,1]$, $\|Mf\|_{L^2} \le \|f\|_{L^2}$, so $M \in \mathcal{L}(L^2[0,1], L^2[0,1])$ with $\|M\| \le 1$.
>
> **$\mathbb{C} \setminus [0,1] \subset \rho(M)$.** Let $\lambda \in \mathbb{C}$, $\lambda \notin [0,1]$. Then $(\lambda I - M) f(t) = (\lambda - t) f(t)$, and
>
> $$
> d := \operatorname{dist}(\lambda, [0,1]) = \min_{t \in [0,1]} |\lambda - t| > 0 ,
> $$
>
> so $\lambda I - M : L^2[0,1] \to L^2[0,1]$ is invertible. *One-to-one:* if $(\lambda - t) f(t) = 0$ for almost every $t$, then $f(t) = 0$ for almost every $t$, because $\lambda - t \neq 0$. *Onto:* for $g \in L^2[0,1]$ the function $f(t) = \frac{g(t)}{\lambda - t}$ is measurable with $|f(t)| \le \frac{1}{d} |g(t)|$, so $f \in L^2[0,1]$, and $(\lambda I - M) f = g$. The same bound shows $\|R(\lambda; M) g\|_{L^2} \le \frac{1}{d} \|g\|_{L^2}$, that is, $\|R(\lambda; M)\| \le \frac{1}{\operatorname{dist}(\lambda, [0,1])}$.
>
> **$[0,1] \subset \sigma_c(M)$.** Let $\lambda_0 \in [0,1]$. Then $(\lambda_0 I - M) f(t) = (\lambda_0 - t) f(t)$.
>
> *$\lambda_0 I - M$ is one-to-one.* If $(\lambda_0 - t) f(t) = 0$ for almost every $t$, then $f(t) = 0$ for almost every $t \neq \lambda_0$; the single point $\lambda_0$ has measure zero, so $f = 0$ in $L^2[0,1]$. In particular $\lambda_0 \notin \sigma_p(M)$.
>
> *Claim: $\overline{R(\lambda_0 I - M)} = L^2[0,1]$.* Step 1. Let $g \in L^2[0,1]$, and for $\varepsilon > 0$ let
>
> $$
> g_\varepsilon(t) = \begin{cases} g(t), & |t - \lambda_0| > \varepsilon, \\ 0, & |t - \lambda_0| \le \varepsilon. \end{cases}
> $$
>
> Then
>
> $$
> \|g - g_\varepsilon\|_{L^2}^2 = \int_{[0,1] \cap [\lambda_0 - \varepsilon,\, \lambda_0 + \varepsilon]} |g(t)|^2\, dt \to 0 \qquad \text{as } \varepsilon \to 0 .
> $$
>
> (By the [[Dominated Convergence Theorem|dominated convergence theorem]]: the integrand $|g|^2 \chi_{\{ |t - \lambda_0| \le \varepsilon \}}$ tends to $0$ at every $t \neq \lambda_0$ as $\varepsilon \to 0$, and it is dominated by the integrable function $|g|^2$.)
>
> Step 2. $g_\varepsilon \in R(\lambda_0 I - M)$ for every $\varepsilon > 0$. Indeed,
>
> $$
> (\lambda_0 I - M) f = g_\varepsilon \quad \Longleftrightarrow \quad (\lambda_0 - t) f(t) = g_\varepsilon(t) \quad \Longleftrightarrow \quad f(t) = \frac{g_\varepsilon(t)}{\lambda_0 - t} = \begin{cases} \dfrac{g(t)}{\lambda_0 - t}, & |t - \lambda_0| > \varepsilon, \\[1ex] 0, & |t - \lambda_0| \le \varepsilon, \end{cases}
> $$
>
> (equalities for almost every $t$), and this $f$ belongs to $L^2[0,1]$: it is measurable, and $|f(t)| \le \frac{1}{\varepsilon} |g(t)|$, because $\frac{1}{|\lambda_0 - t|} < \frac{1}{\varepsilon}$ where $f(t) \neq 0$. So $g_\varepsilon \in R(\lambda_0 I - M)$. By Step 1 every $g \in L^2[0,1]$ is a limit of elements of the range, hence $\overline{R(\lambda_0 I - M)} = L^2[0,1]$.
>
> ![[m556-48-4.svg]]
>
> Top: the cut-off of a constant function. Bottom: $g_\varepsilon$ (red) equals $g$ outside $[\lambda_0 - \varepsilon, \lambda_0 + \varepsilon]$ and is $0$ inside. Cutting $g$ off near $\lambda_0$ changes it little in $L^2$, and the cut-off function is in the range.
>
> ![[m556-48-a1.gif|460]]
>
> *(Not from lecture; animation added, vault only.)* The cut-off for $\lambda_0 = 0.4$ and $\varepsilon$ from $0.3$ down to $0.003$. Top: $g$ (grey) and $g_\varepsilon$ (blue). Bottom: the solution $f_\varepsilon = g_\varepsilon / (\lambda_0 - t)$ of $(\lambda_0 I - M) f_\varepsilon = g_\varepsilon$ (red, clipped). Right: $\|g - g_\varepsilon\|_{L^2} \to 0$, so $g$ is a limit of elements of the range; $\|f_\varepsilon\|_{L^2}$ grows without bound, so the inverse is not bounded on the range; $\max |g - g_\varepsilon|$ stays near $|g(\lambda_0)|$, so in the maximum norm $g_\varepsilon$ does not approach $g$, which is why the same cut-off does not give a dense range in $C[0,1]$.
>
> *Claim: $R(\lambda_0 I - M) \neq L^2[0,1]$.* If $g \in R(\lambda_0 I - M)$, the solution $f$ of $(\lambda_0 I - M) f = g$ has to be $f(t) = \frac{g(t)}{\lambda_0 - t}$. Let $g \equiv 1$: then $f(t) = \frac{1}{\lambda_0 - t} \notin L^2[0,1]$. In detail: if $(\lambda_0 - t) f(t) = 1$ for almost every $t$, then $f(t) = \frac{1}{\lambda_0 - t}$ for almost every $t$. The interval $[0,1]$ contains $[\lambda_0, \lambda_0 + \frac12]$ or $[\lambda_0 - \frac12, \lambda_0]$, and over either of them
>
> $$
> \int \frac{dt}{|\lambda_0 - t|^2} = \int_0^{1/2} \frac{ds}{s^2} = \lim_{a \to 0^+} \Bigl( \frac1a - 2 \Bigr) = \infty .
> $$
>
> So no $f \in L^2[0,1]$ solves $(\lambda_0 I - M) f = 1$: the constant $1$ is not in $R(\lambda_0 I - M)$. By Definition [[§48 The Resolvent and the Spectrum#^def-48-6|§48.6]], $\lambda_0 \in \sigma_c(M)$.
>
> **Conclusion.** $\mathbb{C} \setminus [0,1] \subset \rho(M)$ and $[0,1] \subset \sigma_c(M) \subset \sigma(M)$. Hence $\rho(M) = \mathbb{C} \setminus [0,1]$ and $\sigma(M) = \sigma_c(M) = [0,1]$; by Proposition [[§48 The Resolvent and the Spectrum#^prop-48-3|§48.3]], $\sigma_p(M)$ and $\sigma_r(M)$ are empty.

^pf-ex-48-4

*Uses:* [[§48 The Resolvent and the Spectrum#^def-48-6|Def. §48.6]], [[§48 The Resolvent and the Spectrum#^prop-48-3|§48.3]]

> [!remark]- Connections
> - Method: [[Functional Analysis Problem-Solving Techniques#^rem-t34|Technique 34]] (cut off near the singularity).
> - The same operator on $L^2(\mathbb{R})$ has no eigenvectors: [[§52 Position Eigenstates and Continuous Resolutions#^prop-52-3|Prop. §52.3]].

![[m556-48-5.svg]]

The spectrum of multiplication by $t$ is the interval $[0,1]$ of the values of $t$, both on $C[0,1]$ and on $L^2[0,1]$. For $\lambda$ off the interval, $d = \operatorname{dist}(\lambda, [0,1])$ is the smallest value of $|\lambda - t|$, and the inverse is division by $\lambda - t$, of norm at most $\frac1d$. (Not from lecture; figure added.)

> [!theorem] Proposition §48.4: Approximate Eigenvectors of Multiplication by $t$
> *(Not from lecture; filled in.)* Let $M f(t) = t f(t)$ on $L^2[0,1]$ and $\lambda_0 \in [0,1]$. For $0 < \varepsilon \le \frac12$ let $J_\varepsilon = [0,1] \cap [\lambda_0 - \varepsilon, \lambda_0 + \varepsilon]$, an interval of length $|J_\varepsilon| \ge \varepsilon$, and
>
> $$
> \varphi_\varepsilon = \frac{1}{\sqrt{|J_\varepsilon|}}\, \chi_{J_\varepsilon} .
> $$
>
> Then $\|\varphi_\varepsilon\|_{L^2} = 1$ and $\|(\lambda_0 I - M) \varphi_\varepsilon\|_{L^2} \le \varepsilon$. Consequently there is no constant $c$ with $\|f\|_{L^2} \le c\, \|(\lambda_0 I - M) f\|_{L^2}$ for all $f \in L^2[0,1]$.

^prop-48-4

> [!proof]+ Proof
> $\|\varphi_\varepsilon\|_{L^2}^2 = \frac{1}{|J_\varepsilon|} \int_{J_\varepsilon} dt = 1$. On $J_\varepsilon$, $|\lambda_0 - t| \le \varepsilon$, so
>
> $$
> \|(\lambda_0 I - M) \varphi_\varepsilon\|_{L^2}^2 = \frac{1}{|J_\varepsilon|} \int_{J_\varepsilon} |\lambda_0 - t|^2\, dt \le \varepsilon^2 .
> $$
>
> If $\|f\|_{L^2} \le c\, \|(\lambda_0 I - M) f\|_{L^2}$ held for all $f$, then $f = \varphi_\varepsilon$ would give $1 \le c\, \varepsilon$ for every $\varepsilon \in (0, \frac12]$, which is false for $\varepsilon < \frac1c$.

^pf-48-4

> [!remark] Remark: Reading the Approximate Eigenvectors
> The functions $\varphi_\varepsilon$ are unit vectors with $M \varphi_\varepsilon - \lambda_0 \varphi_\varepsilon \to 0$: they satisfy the eigenvalue equation up to an error that tends to $0$, although no eigenvector exists. The proposition gives a second reason why $\lambda_0 \in \sigma(M)$, without looking at the range. If $\lambda_0$ were in $\rho(M)$, then $R(\lambda_0; M)$ would be bounded (Proposition [[§48 The Resolvent and the Spectrum#^prop-48-2|§48.2]]), and $\|f\| = \|R(\lambda_0; M)(\lambda_0 I - M) f\| \le \|R(\lambda_0; M)\|\, \|(\lambda_0 I - M) f\|$ would be a bound of the excluded kind.

^rem-48-3

> [!remark] Remark: What the Examples Show
> In both examples $\sigma_p(M) = \varnothing$: multiplication by $t$ has no eigenvectors, yet its spectrum is the whole interval of the values of $t$. The spectrum, not the set of eigenvalues, is the right generalization of the eigenvalues of a matrix. Which part of the spectrum the interval $[0,1]$ is depends on the space. In $C[0,1]$ every function in the range vanishes at $\lambda_0$; this is a closed condition, and the range is far from dense. In $L^2[0,1]$ a single point does not matter, and the range is dense. In both cases $\sigma(M)$ is a nonempty, closed and bounded set, as it is for every bounded operator on a Banach space $X \neq \{0\}$ over $\mathbb{C}$ (Theorem [[§49 Elementary Spectral Theory#^thm-49-8|§49.8]]). Lax's Chapter 20 computes the spectra of further operators: shifts (§20.2), Volterra integral operators (§20.3) and the Fourier transform (§20.4).

^rem-48-4

> [!remark] Remark: The Position Operator
> In quantum mechanics multiplication by the coordinate on $L^2$ is the position operator ([[§52 Position Eigenstates and Continuous Resolutions|§52]], there on $L^2(\mathbb{R})$). Proposition [[§52 Position Eigenstates and Continuous Resolutions#^prop-52-3|§52.3]] of that section is the statement $\sigma_p(M) = \varnothing$. Example [[§48 The Resolvent and the Spectrum#^ex-48-4|§48.4]] says where the “position eigenvalues” of physics are: every $\lambda_0$ in the interval belongs to the spectrum, as a point of the continuous spectrum and not as an eigenvalue. The “eigenfunction” $\delta(t - \lambda_0)$ of the physics texts is not an element of $L^2$; what exists in $L^2$ are the approximate eigenvectors $\varphi_\varepsilon$ of Proposition [[§48 The Resolvent and the Spectrum#^prop-48-4|§48.4]], wave packets concentrated within $\varepsilon$ of $\lambda_0$.

^rem-48-5

> [!remark]- Connections
> - Companion chapter: [[§52 Position Eigenstates and Continuous Resolutions|§52]] (position has no eigenvectors; the spectral projections of position).
> - Physics: position eigenkets and continuous spectra, [[§C2.1 Continuous Spectra and Position Eigenkets]].

