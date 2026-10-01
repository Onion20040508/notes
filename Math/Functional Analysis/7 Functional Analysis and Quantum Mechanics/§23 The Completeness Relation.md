---
type: section
subject: "[[Functional Analysis]]"
chapter: 7
section: 23
tags: [functional-analysis, math556, companion]
---
← [[§22 Bras, Kets, and the Riesz Map]] · ↑ [[· 7 Functional Analysis and Quantum Mechanics]] · [[§24 Position Eigenstates and Continuous Resolutions]] →

*Companion — Threads: dimension, completeness. $\sum_n |e_n\rangle\langle e_n| = \mathbf{1}$ holds strongly, not in norm.*

The physicists' identity $\sum_n |e_n\rangle\langle e_n| = \mathbf{1}$ is Theorem [[§20 Orthonormal Sets and Bases#^thm-20-8|§20.8]] rewritten; the name “completeness relation” and Wu's “[[§20 Orthonormal Sets and Bases#^def-20-2|complete orthonormal set]]” refer to the same thing. What needs care is the sense in which an infinite sum of operators equals $\mathbf{1}$.

## Operators and Projections

> [!definition] Definition §23.1: Bounded Operator; Operator Norm; Strong Convergence
> Let $H$ be a Hilbert space. A linear map $T : H \to H$ is a **bounded operator** if there is $c \ge 0$ with $\|Tx\| \le c\,\|x\|$ for all $x$; its **operator norm** $\|T\|$ is the infimum of such $c$. A sequence of bounded operators $T_n$ converges **strongly** to $T$ if $T_n x \to T x$ for every $x \in H$, and **in norm** if $\|T_n - T\| \to 0$. The identity operator is written $\mathbf{1}$.

^def-23-1

> [!remark]- Connections
> - The general definition, for maps $X \to Y$: [[§21 Boundedness and Continuity#^def-21-2|Def. §21.2]]; the operator norm as a norm on $\mathcal{L}(X, Y)$: [[§21 Boundedness and Continuity#^thm-21-3|§21.3]].
> - Finite dimensions: [[§27 Consequences of Singular Value Decomposition#^ladr-7-86|LADR 7.86]].

As for functionals (Lemma [[§22 Bras, Kets, and the Riesz Map#^lem-22-1|§22.1]]), $\|Tx\| \le \|T\|\,\|x\|$. Norm convergence implies strong convergence, since $\|T_n x - Tx\| \le \|T_n - T\|\,\|x\|$.

> [!definition] Definition §23.2: Orthogonal Projection
> Let $Y$ be a closed subspace of a Hilbert space $H$. By Theorem [[§18 Projection and Orthogonal Decomposition#^thm-18-4|§18.4]] every $x \in H$ is uniquely $x = y + v$ with $y \in Y$, $v \in Y^\perp$. The **orthogonal projection** onto $Y$ is $P_Y x = y$.

^def-23-2

> [!remark]- Connections
> - Finite-dimensional $Y$ in LADR: [[§21 Orthogonal Complements and Minimization Problems#^ladr-6-55|LADR 6.55]].

> [!theorem] Proposition §23.1: Finite Sums of Outer Products are Projections
> Let $e_1, \ldots, e_N$ be orthonormal in a Hilbert space $H$, $Y = \operatorname{span}\{e_1, \ldots, e_N\}$, and
>
> $$
> P_N = \sum_{n=1}^N |e_n\rangle\langle e_n|, \qquad P_N x = \sum_{n=1}^N (x, e_n)\, e_n .
> $$
>
> Then $Y$ is closed and $P_N = P_Y$. Moreover $\|P_N x\|^2 + \|x - P_N x\|^2 = \|x\|^2$ for every $x$.

^prop-23-1

> [!proof]+ Proof
> $Y$ is finite-dimensional, hence closed (Corollary [[§10 New Normed Spaces from Old#^cor-10-5|§10.5]]). By Lemma [[§20 Orthonormal Sets and Bases#^lem-20-2|§20.2]], $x - P_N x \perp e_n$ for each $n$, hence $x - P_N x \in Y^\perp$; and $P_N x \in Y$. So $x = P_N x + (x - P_N x)$ is the decomposition of Theorem [[§18 Projection and Orthogonal Decomposition#^thm-18-4|§18.4]], and by its uniqueness $P_Y x = P_N x$. The identity is Pythagoras (Lemma [[§20 Orthonormal Sets and Bases#^lem-20-1|§20.1]](a)).

^pf-23-1

*Uses:* [[§10 New Normed Spaces from Old#^cor-10-5|§10.5]], [[§20 Orthonormal Sets and Bases#^lem-20-2|§20.2]], [[§18 Projection and Orthogonal Decomposition#^thm-18-4|§18.4]], [[§23 The Completeness Relation#^def-23-2|Def. §23.2]], [[§20 Orthonormal Sets and Bases#^lem-20-1|§20.1]], [[§22 Bras, Kets, and the Riesz Map#^def-22-2|Def. §22.2]]

> [!remark]- Connections
> - Finite-dimensional version, $P_U = \sum_k |e_k\rangle\langle e_k|$: [[§21 Orthogonal Complements and Minimization Problems#^ladr-6-55|LADR 6.55]], [[§21 Orthogonal Complements and Minimization Problems#^ladr-6-57|LADR 6.57]].

> [!example] Example §23.1: Parity
> For a particle in the symmetric box $[-1,1]$, the parity operator $(\Pi\psi)(x) = \psi(-x)$ has the even and odd states as its eigenspaces, with eigenvalues $+1$ and $-1$. By Proposition [[§18 Projection and Orthogonal Decomposition#^prop-18-7|§18.7]] these eigenspaces are closed and orthogonal, and $L^2[-1,1] = E \oplus O$. Writing $P_E$, $P_O$ for the orthogonal projections, $P_E + P_O = \mathbf{1}$ and $\Pi = P_E - P_O$: the simplest resolution of the identity, with two projections, and the simplest spectral decomposition. It is why energy eigenstates of a symmetric potential can be chosen even or odd.

^ex-23-1

## The Completeness Relation

> [!theorem] Theorem §23.2: The Completeness Relation
> Let $\{e_n\}_{n \ge 1}$ be a countable orthonormal set in a Hilbert space $H$, and $P_N = \sum_{n=1}^N |e_n\rangle\langle e_n|$. Then $\{e_n\}$ is complete if and only if $P_N \to \mathbf{1}$ strongly, i.e.
>
> $$
> \sum_{n=1}^\infty |e_n\rangle\langle e_n| = \mathbf{1} \qquad \text{in the sense that} \qquad \sum_{n=1}^\infty (x, e_n)\, e_n = x \quad \text{for every } x \in H .
> $$

^thm-23-2

> [!proof]+ Proof
> For fixed $x$, the partial sums $P_N x = \sum_{n \le N} (x, e_n) e_n$ differ from the partial sums $s_M$ of Proposition [[§20 Orthonormal Sets and Bases#^prop-20-6|§20.6]] (taken along the enumeration of $S_x$ in increasing order of $n$) only by the omitted zero terms: $P_N x = s_{M(N)}$ with $M(N) = \#(S_x \cap \{1, \ldots, N\})$, which is non-decreasing and tends to $\#S_x$. Hence $P_N x \to \sum_n (x, e_n) e_n$ for every $x$. So $P_N x \to x$ for all $x$ iff $\{e_n\}$ is an orthonormal basis, iff it is complete, by Theorem [[§20 Orthonormal Sets and Bases#^thm-20-8|§20.8]].

^pf-23-2

*Uses:* [[§20 Orthonormal Sets and Bases#^prop-20-6|§20.6]], [[§20 Orthonormal Sets and Bases#^thm-20-8|§20.8]], [[§20 Orthonormal Sets and Bases#^def-20-4|Def. §20.4]], [[§23 The Completeness Relation#^def-23-1|Def. §23.1]]

> [!remark]- Connections
> - The same theorem in the notation of Chapter 5: [[§20 Orthonormal Sets and Bases#^thm-20-8|§20.8]] ((1) ⇔ (2)).

> [!theorem] Proposition §23.3: The Completeness Relation Does Not Hold in Norm
> If $\{e_n\}_{n \ge 1}$ is an infinite orthonormal set, then $\|\mathbf{1} - P_N\| = 1$ for every $N$. In particular $P_N \not\to \mathbf{1}$ in operator norm, even when $\{e_n\}$ is complete.

^prop-23-3

> [!proof]+ Proof
> By Proposition [[§23 The Completeness Relation#^prop-23-1|§23.1]], $\|(\mathbf{1} - P_N)x\|^2 = \|x\|^2 - \|P_N x\|^2 \le \|x\|^2$, so $c = 1$ is admissible and $\|\mathbf{1} - P_N\| \le 1$. On the other hand $(\mathbf{1} - P_N)e_{N+1} = e_{N+1}$, a unit vector, so every admissible $c$ is at least $1$.

^pf-23-3

*Uses:* [[§23 The Completeness Relation#^prop-23-1|§23.1]], [[§23 The Completeness Relation#^def-23-1|Def. §23.1]]

> [!remark] Remark
> Each truncation $P_N$ misses the directions $e_{N+1}, e_{N+2}, \ldots$ entirely, and there is always a unit vector in those directions; so $P_N$ is never uniformly close to $\mathbf{1}$. What is true is that for each *fixed* state $x$ the missed part $\|x - P_N x\|^2 = \sum_{n > N} |(x, e_n)|^2$ tends to $0$. Physics computations only ever apply $\sum_n |e_n\rangle\langle e_n|$ to vectors, or sandwich it between vectors, so strong convergence is exactly what they need; it is also the first place where an identity of linear algebra holds in infinite dimensions only in a weakened sense.

^rem-23-1

> [!theorem] Corollary §23.4: Inserting a Complete Set of States
> Let $\{e_n\}_{n \ge 1}$ be a complete orthonormal set in $H$. For all $x, y \in H$,
>
> $$
> \langle y | x \rangle = \sum_{n=1}^\infty \langle y | e_n \rangle \langle e_n | x \rangle ,
> $$
>
> the series converging absolutely. With $y = x$ this is [[§20 Orthonormal Sets and Bases#^thm-20-8|Parseval's equality]], $\|x\|^2 = \sum_n |\langle e_n | x \rangle|^2$.

^cor-23-4

> [!proof]+ Proof
> In the notation of these notes the claim is $(x, y) = \sum_n (x, e_n)(e_n, y)$. By Theorem [[§23 The Completeness Relation#^thm-23-2|§23.2]], $P_N x \to x$, so by continuity of the inner product (Lemma [[§18 Projection and Orthogonal Decomposition#^lem-18-1|§18.1]]),
>
> $$
> (x, y) = \lim_{N \to \infty} (P_N x, y) = \lim_{N \to \infty} \sum_{n \le N} (x, e_n)(e_n, y).
> $$
>
> Absolute convergence: by the Cauchy–Schwarz inequality for sequences (Hölder with $p = q = 2$, Theorem [[§12 Hölder's Inequality for Sequences#^thm-12-1|§12.1]]) and Bessel's inequality (Theorem [[§20 Orthonormal Sets and Bases#^thm-20-5|§20.5]]), $\sum_n |(x, e_n)|\,|(e_n, y)| \le \|x\|\,\|y\|$.

^pf-23-4

*Uses:* [[§23 The Completeness Relation#^thm-23-2|§23.2]], [[§18 Projection and Orthogonal Decomposition#^lem-18-1|§18.1]], [[§12 Hölder's Inequality for Sequences#^thm-12-1|§12.1]], [[§20 Orthonormal Sets and Bases#^thm-20-5|§20.5]], [[§22 Bras, Kets, and the Riesz Map#^rem-22-1|Remark: Conventions]]

> [!remark]- Connections
> - Parseval's equality, the case $y = x$: [[§20 Orthonormal Sets and Bases#^thm-20-8|§20.8]](3); in finite dimensions [[§20 Orthonormal Bases#^ladr-6-30|LADR 6.30]].

> [!example] Example §23.2: A Particle on a Ring
> The Fourier basis $e_n(\theta) = e^{in\theta}/\sqrt{2\pi}$, $n \in \mathbb{Z}$, of $L^2[0,2\pi]$ (Theorem [[§20 Orthonormal Sets and Bases#^thm-20-11|§20.11]]) consists of the momentum eigenstates of a particle on a circle: $-i\,\frac{d}{d\theta} e_n = n\,e_n$, and $e_n$ is an eigenfunction of the free Hamiltonian $-\frac12 \frac{d^2}{d\theta^2}$ with energy $n^2/2$. Its completeness relation $\sum_{n \in \mathbb{Z}} |e_n\rangle\langle e_n| = \mathbf{1}$ is the $L^2$ convergence of Fourier series, and Corollary [[§23 The Completeness Relation#^cor-23-4|§23.4]] is Parseval's identity $\int_0^{2\pi} f\,\bar{g} = \sum_n c_n(f)\,\overline{c_n(g)}$. The spectrum is discrete because the configuration space is compact; compare [[§24 Position Eigenstates and Continuous Resolutions|§24]].

^ex-23-2
