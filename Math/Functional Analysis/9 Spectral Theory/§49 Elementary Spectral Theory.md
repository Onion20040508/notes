---
type: section
subject: "[[Functional Analysis]]"
chapter: 9
section: 49
tags: [functional-analysis, math556]
---
← [[§48 The Resolvent and the Spectrum]] · ↑ [[· 9 Spectral Theory]] · [[§50 Bras, Kets, and the Riesz Map]] →

*Stage: maps — Thread: invertibility. Operators near an invertible operator are invertible (geometric series); hence $\rho(M)$ is open, the resolvent is analytic on it, and Liouville's theorem shows that $\sigma(M)$ is not empty.*

*Lecture 22 (Thu Nov 19). Source: the handwritten notes of the lecture; there is no recording. The steps that the notes leave out, and the items marked as such, are filled in. The section was checked against Lax §17.1, §17.2 and §20.2. In the lecture the two lemmas of [[§49 Elementary Spectral Theory|§49]] are one lemma, proved in two cases.*

Throughout this section $X \neq \{0\}$ is a Banach space over $\mathbb{C}$ and $M \in \mathcal{L}(X, X)$. Recall (Definitions [[§48 The Resolvent and the Spectrum#^def-48-1|§48.1]] and [[§48 The Resolvent and the Spectrum#^def-48-3|§48.3]]): a number $\lambda \in \mathbb{C}$ belongs to $\rho(M)$ if $\lambda I - M : X \to X$ is invertible, and

$$
\rho(M) = \{ \lambda \in \mathbb{C} : \lambda I - M \text{ is invertible} \} , \qquad \sigma(M) = \mathbb{C} \setminus \rho(M) .
$$

Here $A \in \mathcal{L}(X, X)$ is invertible if it is one-to-one and onto. Its inverse $A^{-1}$ then belongs to $\mathcal{L}(X, X)$ (Theorem [[§39 Solving Mx = y#^thm-39-2|§39.2]]), and $A^{-1}A = AA^{-1} = I$. For $\lambda \in \rho(M)$ the resolvent is $R(\lambda; M) = (\lambda I - M)^{-1}$ (Definition [[§48 The Resolvent and the Spectrum#^def-48-2|§48.2]]).

## Left and Right Inverses

> [!definition] Definition §49.1: Left Inverse
> Let $A \in \mathcal{L}(X, X)$. $A$ has a **left inverse** if there is $B \in \mathcal{L}(X, X)$ such that $BA = I$.
>
> *Lax: §17.1, (4)*

^def-49-1

> [!remark]- Connections
> - In finite dimensions a one-sided inverse is an inverse: [[§10 Invertibility and Isomorphisms#^ladr-3-65|LADR 3.65]]; inverse of a linear map, [[§10 Invertibility and Isomorphisms#^ladr-3-59|LADR 3.59]].

> [!definition] Definition §49.2: Right Inverse
> Let $A \in \mathcal{L}(X, X)$. $A$ has a **right inverse** if there is $C \in \mathcal{L}(X, X)$ such that $AC = I$.
>
> *Lax: §17.1, (4)*

^def-49-2

> [!theorem] Lemma §49.1: One-Sided Inverses
> Let $A \in \mathcal{L}(X, X)$.
>
> 1. If $A$ has a left inverse, then $A : X \to X$ is one-to-one.
> 2. If $A$ has a right inverse, then $A : X \to X$ is onto.

^lem-49-1

> [!proof]+ Proof
> (1) Let $BA = I$. If $Ax = 0$, then $x = BAx = B0 = 0$. So the null space of $A$ is $\{0\}$, and $A$ is one-to-one.
>
> (2) Let $AC = I$. For every $x \in X$, $A(Cx) = x$, so $x \in R(A)$. So $A$ is onto.

^pf-49-1

> [!theorem] Lemma §49.2: Inverses, Products and Commuting Factors
> Let $X$ be a Banach space.
>
> 1. If $A \in \mathcal{L}(X, X)$ has both a left and a right inverse, then $A$ is invertible, and the left and the right inverse coincide; both are equal to $A^{-1}$.
> 2. If $M, N \in \mathcal{L}(X, X)$ and $M, N$ are invertible, then $MN$ is invertible and $(MN)^{-1} = N^{-1}M^{-1}$.
> 3. If $M, N \in \mathcal{L}(X, X)$ and $MN = NM$, and if $MN$ is invertible, then $M$ and $N$ are both invertible.
>
> *Lax: §17.1, (5) and Thm 1*

^lem-49-2

> [!proof]+ Proof
> (1) Assume there are $B, C \in \mathcal{L}(X, X)$ with $BA = I$ and $AC = I$. Then
>
> $$
> BAC = (BA)C = C \qquad \text{and} \qquad BAC = B(AC) = B ,
> $$
>
> so $B = C$. By Lemma [[§49 Elementary Spectral Theory#^lem-49-1|§49.1]], $A$ is one-to-one (it has a left inverse) and onto (it has a right inverse), so $A$ is invertible. Finally $B = B(AA^{-1}) = (BA)A^{-1} = A^{-1}$.
>
> (2) By associativity,
>
> $$
> \begin{aligned}(N^{-1}M^{-1})(MN) &= N^{-1}(M^{-1}M)N = N^{-1}N = I , \\
> (MN)(N^{-1}M^{-1}) &= M(NN^{-1})M^{-1} = MM^{-1} = I .\end{aligned}
> $$
>
> So $N^{-1}M^{-1} \in \mathcal{L}(X, X)$ is a left and a right inverse of $MN$. By (1), $MN$ is invertible and $(MN)^{-1} = N^{-1}M^{-1}$.
>
> (3) *$M$ is invertible.* Assume $MN = NM$ and $MN$ is invertible. Then $(MN)^{-1} \in \mathcal{L}(X, X)$ exists, and
>
> $$
> (MN)^{-1}MN = MN(MN)^{-1} = I .
> $$
>
> The second equality reads $M\bigl( N(MN)^{-1} \bigr) = I$: $M$ has the right inverse $N(MN)^{-1}$. In the first equality use $MN = NM$:
>
> $$
> (MN)^{-1}MN = (MN)^{-1}NM = \bigl( (MN)^{-1}N \bigr) M = I ,
> $$
>
> so $M$ has the left inverse $(MN)^{-1}N$. Thus $M$ has a left and a right inverse, and by (1) $M$ is invertible.
>
> *$N$ is invertible.* The first equality reads $\bigl( (MN)^{-1}M \bigr) N = I$, a left inverse of $N$. In the second, $MN(MN)^{-1} = NM(MN)^{-1} = N\bigl( M(MN)^{-1} \bigr) = I$, a right inverse of $N$. By (1) $N$ is invertible.

^pf-49-2

*Uses:* [[§49 Elementary Spectral Theory#^lem-49-1|§49.1]]

> [!example] Example §49.1: The Shifts on $\ell^2$ Have Only One-Sided Inverses
> On $\ell^2$ let $S(a_1, a_2, \ldots) = (0, a_1, a_2, \ldots)$ be the right shift (Example [[§45 Convergence of Operators#^ex-45-2|§45.2]]) and $T(a_1, a_2, \ldots) = (a_2, a_3, \ldots)$ the left shift (Example [[§45 Convergence of Operators#^ex-45-1|§45.1]]). Then
>
> $$
> \begin{aligned}TS(a_1, a_2, \ldots) &= T(0, a_1, a_2, \ldots) = (a_1, a_2, \ldots) , \\
> ST(a_1, a_2, \ldots) &= S(a_2, a_3, \ldots) = (0, a_2, a_3, \ldots) ,\end{aligned}
> $$
>
> so $TS = I$ and $ST \neq I$.
>
> 1. $S$ has the left inverse $T$ and is one-to-one, but $S$ is not onto: $(1, 0, 0, \ldots) \notin R(S)$. So $S$ has no right inverse (Lemma [[§49 Elementary Spectral Theory#^lem-49-1|§49.1]](2)) and is not invertible.
> 2. $T$ has the right inverse $S$ and is onto, but $T$ is not one-to-one: $T(1, 0, 0, \ldots) = 0$. So $T$ has no left inverse (Lemma [[§49 Elementary Spectral Theory#^lem-49-1|§49.1]](1)) and is not invertible.
> 3. The product $TS = I$ is invertible although neither factor is. This does not contradict Lemma [[§49 Elementary Spectral Theory#^lem-49-2|§49.2]](3), because $TS \neq ST$: the hypothesis $MN = NM$ cannot be dropped there.
>
> For a linear map of $\mathbb{C}^n$ to itself this cannot happen: there one-to-one and onto are equivalent (Example [[§48 The Resolvent and the Spectrum#^ex-48-2|§48.2]]), so a one-sided inverse is a two-sided inverse.
>
> *Source: not from lecture · filled in*
>
> *Lax: §20.2, (11) and the lines after it*

^ex-49-1

> [!remark]- Connections
> - The shifts as operators on $\ell^2$: [[§45 Convergence of Operators#^ex-45-1|Ex. §45.1]] (left shift), [[§45 Convergence of Operators#^ex-45-2|Ex. §45.2]] (right shift).
> - The same pair shows that one-to-one and onto are not equivalent in infinite dimensions: [[§48 The Resolvent and the Spectrum|§48]], opening.

## The Geometric Series for Operators

The model is the geometric series of numbers, $\frac{1}{1 - x} = \sum_{n=0}^\infty x^n$ for $|x| < 1$.

> [!theorem] Lemma §49.3: The Neumann Series
> Let $X$ be a Banach space and $A \in \mathcal{L}(X, X)$ with $\|A\| < 1$. Then the series $\sum_{n=0}^\infty A^n$ converges in $\mathcal{L}(X, X)$, $I - A$ is invertible, and
>
> $$
> (I - A)^{-1} = \sum_{n=0}^\infty A^n , \qquad \|(I - A)^{-1}\| \le \frac{1}{1 - \|A\|} .
> $$
>
> *Lax: §17.1, (9)–(9$'$), in the proof of Thm 2*

^lem-49-3

> [!proof]+ Proof
> **Step 1: $\lim_{m \to \infty} \sum_{n=0}^m A^n$ exists.** Put $S_m = \sum_{n=0}^m A^n \in \mathcal{L}(X, X)$, where $A^0 = I$. Since $X$ is complete, $\mathcal{L}(X, X)$ is a Banach space (Theorem [[§30 Boundedness and Continuity#^thm-30-8|§30.8]](2)), so it suffices to show that $\{S_m\}_m$ is a Cauchy sequence. For $k > m$,
>
> $$
> \Bigl\| \sum_{n=0}^k A^n - \sum_{n=0}^m A^n \Bigr\| = \Bigl\| \sum_{n=m+1}^k A^n \Bigr\| \le \sum_{n=m+1}^k \|A^n\| \le \sum_{n=m+1}^k \|A\|^n \to 0 \qquad \text{as } m, k \to \infty .
> $$
>
> Here $\|A^n\| \le \|A\|^n$ follows from $\|NM\| \le \|N\|\, \|M\|$ (Proposition [[§46 The Transpose#^prop-46-9|§46.9]](1)) by induction on $n$, and the last sum is a piece of the convergent geometric series $\sum_n \|A\|^n$, $\|A\| < 1$. So $\{S_m\}$ is Cauchy, and
>
> $$
> S := \lim_{m \to \infty} \sum_{n=0}^m A^n = \sum_{n=0}^\infty A^n \qquad \text{exists in } \mathcal{L}(X, X) .
> $$
>
> **Step 2: $S\,(I - A) = (I - A)\, S = I$.** For the partial sums the products telescope:
>
> $$
> (I - A)\, S_m = S_m\, (I - A) = \sum_{n=0}^m A^n - \sum_{n=0}^m A^{n+1} = I - A^{m+1} ,
> $$
>
> and $\|A^{m+1}\| \le \|A\|^{m+1} \to 0$ as $m \to \infty$. Multiplication by the fixed operator $I - A$ is continuous on $\mathcal{L}(X, X)$, since $\|(I - A)(S_m - S)\| \le \|I - A\|\, \|S_m - S\|$ and likewise on the other side. Letting $m \to \infty$ gives $(I - A) S = S (I - A) = I$.
>
> **Step 3: conclusion.** $S$ is a left and a right inverse of $I - A$. By Lemma [[§49 Elementary Spectral Theory#^lem-49-2|§49.2]](1), $I - A$ is invertible and $(I - A)^{-1} = S = \sum_{n=0}^\infty A^n$. For the norm, $\|S_m\| \le \sum_{n=0}^m \|A\|^n \le \frac{1}{1 - \|A\|}$ for every $m$, and $\|S\| = \lim_m \|S_m\|$, so $\|(I - A)^{-1}\| \le \frac{1}{1 - \|A\|}$.

^pf-49-3

*Uses:* [[§30 Boundedness and Continuity#^thm-30-8|§30.8]], [[§46 The Transpose#^prop-46-9|§46.9]], [[§49 Elementary Spectral Theory#^lem-49-2|§49.2]]

> [!remark]- Connections
> - The scalar model: [[§73a The Geometric Series]] (Complex Variables).
> - Completeness of the space of operators: [[Bounded Linear Maps into a Banach Space Form a Banach Space]].
> - Method: [[Functional Analysis Problem-Solving Techniques#^rem-t35|Technique 35]].

> [!theorem] Lemma §49.4: Perturbation of an Invertible Operator
> Let $X$ be a Banach space and let $K \in \mathcal{L}(X, X)$ be invertible. Assume $A \in \mathcal{L}(X, X)$ satisfies
>
> $$
> \|A\| < \frac{1}{\|K^{-1}\|} .
> $$
>
> Then $K - A : X \to X$ is invertible, with
>
> $$
> (K - A)^{-1} = (I - K^{-1}A)^{-1} K^{-1} = \sum_{n=0}^\infty (K^{-1}A)^n K^{-1} , \qquad \|(K - A)^{-1}\| \le \frac{\|K^{-1}\|}{1 - \|K^{-1}\|\, \|A\|} .
> $$
>
> *Lax: §17.1, Thm 2*

^lem-49-4

> [!proof]+ Proof
> Since
>
> $$
> \|K^{-1}A\| \le \|K^{-1}\|\, \|A\| < 1 ,
> $$
>
> $I - K^{-1}A$ is invertible by Lemma [[§49 Elementary Spectral Theory#^lem-49-3|§49.3]]. Then, by Lemma [[§49 Elementary Spectral Theory#^lem-49-2|§49.2]](2), the product
>
> $$
> K\, (I - K^{-1}A) = K - A
> $$
>
> is invertible, and
>
> $$
> (K - A)^{-1} = (I - K^{-1}A)^{-1} K^{-1} .
> $$
>
> *The bound.* By Lemma [[§49 Elementary Spectral Theory#^lem-49-3|§49.3]] for $K^{-1}A$ in place of $A$,
>
> $$
> \begin{aligned}\|(K - A)^{-1}\| \le \|K^{-1}\|\, \|(I - K^{-1}A)^{-1}\| &= \|K^{-1}\|\, \Bigl\| \sum_{n=0}^\infty (K^{-1}A)^n \Bigr\| \\
> &\le \|K^{-1}\| \sum_{n=0}^\infty \|K^{-1}\|^n\, \|A\|^n = \frac{\|K^{-1}\|}{1 - \|K^{-1}\|\, \|A\|} .\end{aligned}
> $$

^pf-49-4

*Uses:* [[§49 Elementary Spectral Theory#^lem-49-3|§49.3]], [[§49 Elementary Spectral Theory#^lem-49-2|§49.2]]

> [!remark] Remark: Invertible Operators Form an Open Set
> Lemma [[§49 Elementary Spectral Theory#^lem-49-4|§49.4]] says that the ball of radius $\frac{1}{\|K^{-1}\|}$ about an invertible $K$ in $\mathcal{L}(X, X)$ consists of invertible operators: the invertible operators form an open subset of $\mathcal{L}(X, X)$. The smaller $\|K^{-1}\|$ is, the larger the perturbation that $K$ tolerates. Only the completeness of $\mathcal{L}(X, X)$, the inequality $\|NM\| \le \|N\|\, \|M\|$ and the algebra of Lemma [[§49 Elementary Spectral Theory#^lem-49-2|§49.2]] are used; this is why Lax proves these results for the elements of a Banach algebra.

^rem-49-1

## The Resolvent Set is Open

> [!theorem] Proposition §49.5: The Resolvent Set is Open and Contains $|\lambda| > \|M\|$
> Let $X \neq \{0\}$ be a Banach space over $\mathbb{C}$ and $M \in \mathcal{L}(X, X)$.
>
> 1. Every $\lambda \in \mathbb{C}$ with $|\lambda| > \|M\|$ belongs to $\rho(M)$, and for these $\lambda$
>
> $$
> \|(\lambda I - M)^{-1}\| \le \frac{1}{|\lambda| - \|M\|} .
> $$
>
> 2. $\rho(M)$ is an open set in $\mathbb{C}$. More precisely, if $\lambda_0 \in \rho(M)$, then every $\lambda \in \mathbb{C}$ with $|\lambda - \lambda_0| < \frac{1}{\|(\lambda_0 I - M)^{-1}\|}$ belongs to $\rho(M)$, and
>
> $$
> \|(\lambda I - M)^{-1}\| \le \frac{\|(\lambda_0 I - M)^{-1}\|}{1 - \|(\lambda_0 I - M)^{-1}\|\, |\lambda - \lambda_0|} .
> $$
>
> 3. If $\lambda_0 \in \rho(M)$ and $\mu \in \sigma(M)$, then $|\mu - \lambda_0| \ge \frac{1}{\|(\lambda_0 I - M)^{-1}\|}$. Hence, if $\sigma(M) \neq \varnothing$,
>
> $$
> \|(\lambda_0 I - M)^{-1}\| \ge \frac{1}{\operatorname{dist}(\lambda_0, \sigma(M))} \qquad \text{for every } \lambda_0 \in \rho(M) .
> $$
>
> *Lax: §17.1, Thm 3(i) and Cor 3$'$; part (1) is in the proof of Thm 4*

^prop-49-5

> [!proof]+ Proof
> (1) Let $\lambda \in \mathbb{C}$ with $|\lambda| > \|M\|$. Then $\lambda \neq 0$, and
>
> $$
> \lambda I - M = \lambda \Bigl( I - \frac{1}{\lambda} M \Bigr) , \qquad \Bigl\| \frac{1}{\lambda} M \Bigr\| = \frac{1}{|\lambda|}\, \|M\| < 1 .
> $$
>
> By Lemma [[§49 Elementary Spectral Theory#^lem-49-3|§49.3]], $I - \frac1\lambda M$ is invertible; multiplying by the nonzero number $\lambda$ keeps it invertible, so $\lambda I - M$ is invertible, with $(\lambda I - M)^{-1} = \frac{1}{\lambda} \bigl( I - \frac{1}{\lambda} M \bigr)^{-1}$. By the bound of Lemma [[§49 Elementary Spectral Theory#^lem-49-3|§49.3]],
>
> $$
> \|(\lambda I - M)^{-1}\| = \frac{1}{|\lambda|}\, \Bigl\| \Bigl( I - \frac{1}{\lambda} M \Bigr)^{-1} \Bigr\| \le \frac{1}{|\lambda|} \cdot \frac{1}{1 - \|M\| / |\lambda|} = \frac{1}{|\lambda| - \|M\|} .
> $$
>
> (2) Let $\lambda_0 \in \rho(M)$, so that $\lambda_0 I - M$ is invertible. Let $\lambda \in \mathbb{C}$ with
>
> $$
> |\lambda - \lambda_0| < \frac{1}{\|(\lambda_0 I - M)^{-1}\|} .
> $$
>
> Write $\lambda I - M = (\lambda_0 I - M) - (\lambda_0 - \lambda) I = K - A$ with $K = \lambda_0 I - M$ and $A = (\lambda_0 - \lambda) I$, so that $\|A\| = |\lambda - \lambda_0| < \frac{1}{\|K^{-1}\|}$. By Lemma [[§49 Elementary Spectral Theory#^lem-49-4|§49.4]], $\lambda I - M$ is invertible, that is, $\lambda \in \rho(M)$, and the bound of that lemma is the stated one. So an open disk about each $\lambda_0 \in \rho(M)$ lies in $\rho(M)$: $\rho(M)$ is open.
>
> (3) By (2) the open disk of radius $\frac{1}{\|(\lambda_0 I - M)^{-1}\|}$ about $\lambda_0$ contains no point of $\sigma(M)$. So every $\mu \in \sigma(M)$ satisfies $|\mu - \lambda_0| \ge \frac{1}{\|(\lambda_0 I - M)^{-1}\|}$, and taking the infimum over $\mu \in \sigma(M)$,
>
> $$
> \operatorname{dist}(\lambda_0, \sigma(M)) \ge \frac{1}{\|(\lambda_0 I - M)^{-1}\|} ,
> $$
>
> which is the stated inequality.

^pf-49-5

*Uses:* [[§49 Elementary Spectral Theory#^lem-49-3|§49.3]], [[§49 Elementary Spectral Theory#^lem-49-4|§49.4]]

> [!remark]- Connections
> - Used for: the resolvent is analytic, [[§49 Elementary Spectral Theory#^prop-49-7|Prop. §49.7]]; the spectrum is closed and bounded, [[§49 Elementary Spectral Theory#^thm-49-8|Thm. §49.8]].
> - A case of equality in (3): multiplication by $t$ on $L^2[0,1]$, [[§48 The Resolvent and the Spectrum#^ex-48-4|Ex. §48.4]].

![[m556-49-1.svg]]

The spectrum $\sigma(M)$ and, around a point $\lambda_0$ of the resolvent set, a disk that stays in the resolvent set.

> [!remark] Remark: The Sign in the Distance Bound
> In the notes of the lecture the inequality of part (3) is stated with “$>$”, $\|(\lambda I - M)^{-1}\| > \bigl( \operatorname{dist}(\lambda, \sigma(M)) \bigr)^{-1}$, and derived with “$\ge$”, with the question whether a point outside the resolvent set must be at distance greater than or equal to the radius. The derivation is the correct one: a point of $\sigma(M)$ may lie on the boundary circle of the disk, and equality occurs (Example [[§49 Elementary Spectral Theory#^ex-49-2|§49.2]](1), (2)). The sketch in the notes also carries the word “convex” at $\sigma(M)$. The spectrum is closed and bounded (Theorem [[§49 Elementary Spectral Theory#^thm-49-8|§49.8]]) but need not be convex: for the diagonal matrix with entries $0$ and $1$ on $\mathbb{C}^2$ it is the two-point set $\{0, 1\}$ (Example [[§48 The Resolvent and the Spectrum#^ex-48-2|§48.2]]).

^rem-49-2

> [!example] Example §49.2: Equality and Strict Inequality in the Distance Bound
>
> 1. *$M = 0$.* Here $\lambda I - M = \lambda I$ is invertible exactly for $\lambda \neq 0$, so $\sigma(M) = \{0\}$, and $\|(\lambda I)^{-1}\| = \frac{1}{|\lambda|} = \frac{1}{\operatorname{dist}(\lambda, \sigma(M))}$: equality for every $\lambda \in \rho(M)$.
> 2. *Multiplication by $t$ on $L^2[0,1]$.* By Example [[§48 The Resolvent and the Spectrum#^ex-48-4|§48.4]], $\sigma(M) = [0,1]$ and $\|R(\lambda; M)\| \le \frac{1}{\operatorname{dist}(\lambda, [0,1])}$ for $\lambda \notin [0,1]$. With Proposition [[§49 Elementary Spectral Theory#^prop-49-5|§49.5]](3), $\|R(\lambda; M)\| = \frac{1}{\operatorname{dist}(\lambda, [0,1])}$: equality again.
> 3. *A nilpotent matrix.* Let $X = \mathbb{C}^2$ with the Euclidean norm and $M = \bigl( \begin{smallmatrix} 0 & a \\ 0 & 0 \end{smallmatrix} \bigr)$ with $a > 0$. Then $M^2 = 0$, $\sigma(M) = \{0\}$ (the only eigenvalue, Example [[§48 The Resolvent and the Spectrum#^ex-48-2|§48.2]]), and for $\lambda \neq 0$
>
> $$
> (\lambda I - M)^{-1} = \frac{1}{\lambda} I + \frac{1}{\lambda^2} M = \begin{pmatrix} \frac{1}{\lambda} & \frac{a}{\lambda^2} \\ 0 & \frac{1}{\lambda} \end{pmatrix} ,
> $$
>
> as one checks by multiplying with $\lambda I - M$ and using $M^2 = 0$. Applying this matrix to the unit vector $(0, 1)^T$ gives a vector of norm at least $\frac{a}{|\lambda|^2}$, so
>
> $$
> \|(\lambda I - M)^{-1}\| \ge \frac{a}{|\lambda|^2} > \frac{1}{|\lambda|} = \frac{1}{\operatorname{dist}(\lambda, \sigma(M))} \qquad \text{for } 0 < |\lambda| < a .
> $$
>
> The inequality is strict: the resolvent is much larger than the distance to the spectrum suggests, and the disk of Proposition [[§49 Elementary Spectral Theory#^prop-49-5|§49.5]](2) is smaller than the largest disk about $\lambda$ free of spectrum.
>
> *Source: not from lecture · filled in*

^ex-49-2

![[m556-49-a1.gif|460]]

*(Not from lecture; animation added, vault only.)* A matrix with strict inequality, as in part (3) of the example: $M = \bigl( \begin{smallmatrix} 0 & 1.6 \\ 0 & 1 \end{smallmatrix} \bigr)$ on $\mathbb{C}^2$ with the Euclidean norm, $\sigma(M) = \{0, 1\}$. The point $\lambda_0$ runs once around the spectrum. The red disk has the radius $1/\|(\lambda_0 I - M)^{-1}\|$ of Proposition [[§49 Elementary Spectral Theory#^prop-49-5|§49.5]](2); it lies in $\rho(M)$ and never reaches an eigenvalue. The dashed circle has radius $\operatorname{dist}(\lambda_0, \sigma(M))$ and passes through the nearest eigenvalue. Right: the two radii; the red one is the smaller throughout, by a factor of up to $2.2$.

![[m556-49-2.svg]]

The two uses of the geometric series in Proposition [[§49 Elementary Spectral Theory#^prop-49-5|§49.5]]. Outside the circle $|\lambda| = \|M\|$ every point is in $\rho(M)$, so the spectrum lies in the closed disk of radius $\|M\|$; and around each point $\lambda_0$ of $\rho(M)$, also inside that circle, a disk lies in $\rho(M)$. (Not from lecture; figure added.)

![[m556-49-3.svg]]

The norm of the resolvent of multiplication by $t$ on $L^2[0,1]$ along the real axis (Example [[§49 Elementary Spectral Theory#^ex-49-2|§49.2]](2)): it is finite on the resolvent set, tends to infinity as $\lambda$ approaches the spectrum, and for $\lambda > 1 = \|M\|$ it equals the bound $\frac{1}{|\lambda| - \|M\|}$ of Proposition [[§49 Elementary Spectral Theory#^prop-49-5|§49.5]](1). (Not from lecture; figure added.)

## The Resolvent is Analytic

> [!theorem] Lemma §49.6: The First Resolvent Identity
> Let $\lambda \in \rho(M)$ and $\mu \in \rho(M)$. Then
>
> 1. $(\lambda I - M)^{-1} - (\mu I - M)^{-1} = (\mu - \lambda)\, (\lambda I - M)^{-1} (\mu I - M)^{-1}$;
> 2. $(\lambda I - M)^{-1} (\mu I - M)^{-1} = (\mu I - M)^{-1} (\lambda I - M)^{-1}$: the resolvents commute.
>
> *Lax: §17.2, (24)*

^lem-49-6

> [!proof]+ Proof
> (1) Multiply the difference by $\lambda I - M$ on the left and by $\mu I - M$ on the right:
>
> $$
> (\lambda I - M) \Bigl( (\lambda I - M)^{-1} - (\mu I - M)^{-1} \Bigr) (\mu I - M) = (\mu I - M) - (\lambda I - M) = (\mu - \lambda) I .
> $$
>
> Now multiply this equation by $(\lambda I - M)^{-1}$ on the left and by $(\mu I - M)^{-1}$ on the right; the left side becomes the difference of the resolvents, and the right side becomes $(\mu - \lambda) (\lambda I - M)^{-1} (\mu I - M)^{-1}$.
>
> (2) The operators $\lambda I - M$ and $\mu I - M$ commute, $(\lambda I - M)(\mu I - M) = (\mu I - M)(\lambda I - M)$, since both products equal $\lambda\mu I - (\lambda + \mu) M + M^2$. Both products are invertible, by Lemma [[§49 Elementary Spectral Theory#^lem-49-2|§49.2]](2), and taking inverses of the two sides with the formula $(MN)^{-1} = N^{-1}M^{-1}$ of that lemma gives $(\mu I - M)^{-1}(\lambda I - M)^{-1} = (\lambda I - M)^{-1}(\mu I - M)^{-1}$.

^pf-49-6

*Uses:* [[§49 Elementary Spectral Theory#^lem-49-2|§49.2]]

> [!theorem] Proposition §49.7: The Resolvent is Analytic
> Let $X \neq \{0\}$ be a Banach space over $\mathbb{C}$ and $M \in \mathcal{L}(X, X)$. The resolvent $R(z; M) = (zI - M)^{-1}$, $z \in \rho(M)$, is an analytic function on $\rho(M)$ with values in the Banach space $\mathcal{L}(X, X)$ (Definition [[§47 Weak and Strong Analyticity#^def-47-1|§47.1]]), and its derivative is
>
> $$
> \frac{d}{dz} R(z; M) = -(zI - M)^{-2} = -R(z; M)^2 .
> $$
>
> *Lax: §17.1, Thm 3(ii)*

^prop-49-7

> [!proof]+ Proof
> The set $\rho(M)$ is open (Proposition [[§49 Elementary Spectral Theory#^prop-49-5|§49.5]](2)), and $\mathcal{L}(X, X)$ is a Banach space over $\mathbb{C}$ (Theorem [[§30 Boundedness and Continuity#^thm-30-8|§30.8]](2)), so Definition [[§47 Weak and Strong Analyticity#^def-47-1|§47.1]] applies. Let $\lambda_0 \in \rho(M)$. *What has to be shown:* $R(z; M)$ is continuous at $\lambda_0$ and differentiable at $\lambda_0$. For $z \in \rho(M)$, by the first resolvent identity (Lemma [[§49 Elementary Spectral Theory#^lem-49-6|§49.6]](1)),
>
> $$
> R(z; M) - R(\lambda_0; M) = (zI - M)^{-1} - (\lambda_0 I - M)^{-1} = (\lambda_0 - z)\, (zI - M)^{-1} (\lambda_0 I - M)^{-1} .
> $$
>
> **A bound for $\|(zI - M)^{-1}\|$ near $\lambda_0$.** Write $zI - M = (z - \lambda_0) I + \lambda_0 I - M$. Take $z$ with
>
> $$
> |z - \lambda_0| < \frac{1}{2\, \|(\lambda_0 I - M)^{-1}\|} .
> $$
>
> By Proposition [[§49 Elementary Spectral Theory#^prop-49-5|§49.5]](2), $z \in \rho(M)$ and
>
> $$
> \|(zI - M)^{-1}\| \le \|(\lambda_0 I - M)^{-1}\|\, \frac{1}{1 - \|(\lambda_0 I - M)^{-1}\|\, |z - \lambda_0|} < 2\, \|(\lambda_0 I - M)^{-1}\| ,
> $$
>
> because the denominator is larger than $\frac12$. (In the lecture the bound of Lemma [[§49 Elementary Spectral Theory#^lem-49-4|§49.4]] is derived at this point, with $K = \lambda_0 I - M$ and $A = (\lambda_0 - z) I$: $K - A = K(I - K^{-1}A)$, $(K - A)^{-1} = (I - K^{-1}A)^{-1}K^{-1}$, hence $\|(K - A)^{-1}\| \le \|K^{-1}\| \sum_{n=0}^\infty \|K^{-1}\|^n \|A\|^n$.)
>
> **Continuous at $\lambda_0$.** Let $|z - \lambda_0| < \frac{1}{2 \|(\lambda_0 I - M)^{-1}\|}$. By the identity and the bound,
>
> $$
> \begin{aligned}\|R(z; M) - R(\lambda_0; M)\| &\le |z - \lambda_0|\, \|(zI - M)^{-1}\|\, \|(\lambda_0 I - M)^{-1}\| \\
> &\le 2\, |z - \lambda_0|\, \|(\lambda_0 I - M)^{-1}\|^2 \to 0 \qquad \text{as } z \to \lambda_0 .\end{aligned}
> $$
>
> **Differentiable at $\lambda_0$.** Dividing the identity by $z - \lambda_0$, for $z \neq \lambda_0$,
>
> $$
> \frac{R(z; M) - R(\lambda_0; M)}{z - \lambda_0} = -(zI - M)^{-1} (\lambda_0 I - M)^{-1} \longrightarrow -(\lambda_0 I - M)^{-2} \qquad \text{as } z \to \lambda_0 .
> $$
>
> The limit holds in the norm of $\mathcal{L}(X, X)$ by the continuity just proved:
>
> $$
> \bigl\| (zI - M)^{-1} (\lambda_0 I - M)^{-1} - (\lambda_0 I - M)^{-2} \bigr\| \le \|R(z; M) - R(\lambda_0; M)\|\, \|(\lambda_0 I - M)^{-1}\| \to 0 .
> $$
>
> So the difference quotients converge in $\mathcal{L}(X, X)$ to $-(\lambda_0 I - M)^{-2}$, for every $\lambda_0 \in \rho(M)$.

^pf-49-7

*Uses:* [[§49 Elementary Spectral Theory#^prop-49-5|§49.5]], [[§30 Boundedness and Continuity#^thm-30-8|§30.8]], [[§47 Weak and Strong Analyticity#^def-47-1|Def. §47.1]], [[§49 Elementary Spectral Theory#^lem-49-6|§49.6]], [[§49 Elementary Spectral Theory#^lem-49-4|§49.4]]

> [!remark]- Connections
> - The notion of analyticity used: [[§47 Weak and Strong Analyticity#^def-47-1|Def. §47.1]]; the resolvent, [[§48 The Resolvent and the Spectrum#^def-48-2|Def. §48.2]].

## The Spectrum is Not Empty

> [!theorem] Theorem §49.8: The Spectrum is Nonempty, Closed and Bounded
> Let $X \neq \{0\}$ be a Banach space over $\mathbb{C}$ and $M \in \mathcal{L}(X, X)$. Then $\sigma(M)$ is not empty, and $\sigma(M)$ is a bounded and closed subset of $\mathbb{C}$, with
>
> $$
> \sigma(M) \subset \{ \lambda \in \mathbb{C} : |\lambda| \le \|M\| \} .
> $$
>
> *Lax: §17.1, Thm 4(i) (there by the Laurent series of the resolvent at $\infty$ and the Cauchy integral theorem)*

^thm-49-8

> [!proof]+ Proof
> **Bounded and closed.** By Proposition [[§49 Elementary Spectral Theory#^prop-49-5|§49.5]](1), every $\lambda$ with $|\lambda| > \|M\|$ is in $\rho(M)$, so $\sigma(M) \subset \{ |\lambda| \le \|M\| \}$ and $\sigma(M)$ is bounded. By Proposition [[§49 Elementary Spectral Theory#^prop-49-5|§49.5]](2), $\rho(M)$ is open, so its complement $\sigma(M)$ is closed in $\mathbb{C}$.
>
> **Not empty.** If not, $\sigma(M) = \varnothing$. Then $\rho(M) = \mathbb{C}$, and $(zI - M)^{-1}$ is analytic in all of $\mathbb{C}$ (Proposition [[§49 Elementary Spectral Theory#^prop-49-7|§49.7]]). Hence for every $\ell \in \bigl( \mathcal{L}(X, X) \bigr)'$ the scalar function
>
> $$
> f(z) = \ell\bigl( (zI - M)^{-1} \bigr)
> $$
>
> is holomorphic on $\mathbb{C}$, since a strongly analytic function is weakly analytic (Proposition [[§47 Weak and Strong Analyticity#^prop-47-1|§47.1]], applied in the Banach space $\mathcal{L}(X, X)$).
>
> *$f$ is bounded.* Let $|z| > \|M\| + 1$. By Proposition [[§49 Elementary Spectral Theory#^prop-49-5|§49.5]](1),
>
> $$
> \|(zI - M)^{-1}\| = |z|^{-1}\, \Bigl\| \Bigl( I - \frac{1}{z} M \Bigr)^{-1} \Bigr\| \le \frac{1}{|z| - \|M\|} ,
> $$
>
> and therefore
>
> $$
> \bigl| \ell\bigl( (zI - M)^{-1} \bigr) \bigr| \le \|\ell\|\, \frac{1}{|z| - \|M\|} < \|\ell\| \qquad \text{for all } |z| > \|M\| + 1 .
> $$
>
> On the closed disk $|z| \le \|M\| + 1$, which is compact, $f$ is bounded because it is continuous. So $f$ is a bounded holomorphic function on $\mathbb{C}$ (holomorphic means analytic, [[§25 Analytic Functions#^def-25-1|Complex Variables Def. §25.1]]). By [[Liouville's Theorem|Liouville's theorem]], $f$ is a constant.
>
> *The resolvent is constant.* Hence for all $z, \mu \in \mathbb{C}$
>
> $$
> f(z) - f(\mu) = \ell\bigl( (zI - M)^{-1} - (\mu I - M)^{-1} \bigr) = 0 \qquad \text{for all } \ell \in \bigl( \mathcal{L}(X, X) \bigr)' .
> $$
>
> In a normed linear space, an element on which every bounded linear functional vanishes is $0$ (Corollary [[§36 Duality in Normed Spaces#^cor-36-3|§36.3]], applied in the normed space $\mathcal{L}(X, X)$). So
>
> $$
> (zI - M)^{-1} = (\mu I - M)^{-1} \qquad \text{for all } z, \mu \in \rho(M) = \mathbb{C} .
> $$
>
> *The contradiction.* By the first resolvent identity (Lemma [[§49 Elementary Spectral Theory#^lem-49-6|§49.6]](1)),
>
> $$
> 0 = (zI - M)^{-1} - (\mu I - M)^{-1} = (\mu - z)\, (zI - M)^{-1} (\mu I - M)^{-1} .
> $$
>
> Take $z \neq \mu$. Then the product $(zI - M)^{-1} (\mu I - M)^{-1}$ is the zero operator. But it is a product of two invertible operators, hence invertible (Lemma [[§49 Elementary Spectral Theory#^lem-49-2|§49.2]](2)), and the zero operator is not one-to-one on $X \neq \{0\}$. This contradiction shows that $\sigma(M) \neq \varnothing$.

^pf-49-8

*Uses:* [[§49 Elementary Spectral Theory#^prop-49-5|§49.5]], [[§49 Elementary Spectral Theory#^prop-49-7|§49.7]], [[§47 Weak and Strong Analyticity#^prop-47-1|§47.1]], [[§36 Duality in Normed Spaces#^cor-36-3|§36.3]], [[§49 Elementary Spectral Theory#^lem-49-6|§49.6]], [[§49 Elementary Spectral Theory#^lem-49-2|§49.2]]

> [!remark]- Connections
> - Tools from complex analysis: [[Liouville's Theorem]].
> - Tools from this course: strongly analytic implies weakly analytic, [[§47 Weak and Strong Analyticity#^prop-47-1|Prop. §47.1]]; functionals separate points, [[§36 Duality in Normed Spaces#^cor-36-3|Cor. §36.3]] ([[Hahn–Banach Theorem for Normed Spaces]]).
> - Method: [[Functional Analysis Problem-Solving Techniques#^rem-t36|Technique 36]]; the same pattern proves [[Dunford's Theorem]].
> - In finite dimensions: every operator on a complex vector space has an eigenvalue, [[§15 The Minimal Polynomial#^ladr-5-19|LADR 5.19]]; the scalar analogue of the proof is the [[Fundamental Theorem of Algebra (Liouville proof)]].

![[m556-49-4.svg]]

The results of this section and how they depend on one another. Everything rests on the geometric series; complex analysis enters only at the arrow marked Liouville, which also uses the bound from the top row. (Not from lecture; figure added.)

> [!remark] Remark: Where Each Hypothesis Enters
> *Complex scalars* are essential: the proof rests on Liouville's theorem, and over $\mathbb{R}$ the statement is false. The rotation of $\mathbb{R}^2$ by a right angle has no real $\lambda$ for which $\lambda I - M$ fails to be invertible (Example [[§48 The Resolvent and the Spectrum#^ex-48-2|§48.2]]). *$X \neq \{0\}$* is needed in the last step: on $X = \{0\}$ every $\lambda I - M$ is invertible, and the spectrum is empty. *Completeness* enters through the geometric series, which converges because $\mathcal{L}(X, X)$ is complete. The theorem is the infinite-dimensional form of “every complex square matrix has an eigenvalue”, with the difference that a point of the spectrum need not be an eigenvalue (Examples [[§48 The Resolvent and the Spectrum#^ex-48-3|§48.3]] and [[§48 The Resolvent and the Spectrum#^ex-48-4|§48.4]]). In those two examples $\|M\| = 1$ and $\sigma(M) = [0,1]$, in agreement with $\sigma(M) \subset \{ |\lambda| \le \|M\| \}$.

^rem-49-3

> [!remark] Remark: The Pattern of the Proof
> The proof that $\sigma(M) \neq \varnothing$ applies a theorem of scalar complex analysis to a function with values in a Banach space, in three moves: apply an arbitrary functional $\ell$; use the scalar theorem, here Liouville's, for $\ell\bigl( (zI - M)^{-1} \bigr)$; return to the operators with the Hahn–Banach theorem, in the form that functionals separate points. Dunford's theorem (Theorem [[§47 Weak and Strong Analyticity#^thm-47-3|§47.3]]) was proved in the same way, with Cauchy's integral formula as the scalar theorem. Lax argues differently: he expands the resolvent in the series $\sum_n M^n \zeta^{-n-1}$ for $|\zeta| > \|M\|$ and integrates it around a large circle; if the spectrum were empty, the integral would vanish by the Cauchy integral theorem for analytic functions with values in a Banach space, while the series gives the value $I$. He attributes the nonemptiness of the spectrum to A. E. Taylor, and the theorem as a whole to Gelfand.

^rem-49-4
