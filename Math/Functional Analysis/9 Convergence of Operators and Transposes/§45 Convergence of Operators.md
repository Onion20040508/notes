---
type: section
subject: "[[Functional Analysis]]"
chapter: 9
section: 45
tags: [functional-analysis, math556]
---
← [[§44 Weak Sequential Compactness]] · ↑ [[· 9 Convergence of Operators and Transposes]] · [[§46 The Transpose]] →

*Stage: maps — Thread: functionals. Sequences of bounded linear maps converge uniformly, strongly or weakly; each mode implies the next, and even the weakest forces a uniform bound on the norms when the domain is complete.*

*Lecture 19 (Tue Nov 10), last part, and the beginning of Lecture 20 (Thu Nov 12), which recalled the three modes of convergence and gave the second example. Sources: the handwritten notes of both lectures and, for Lecture 20, the Otter.ai transcript. The proofs of the proposition and of the theorem, which the notes only name, are filled in.*

## Three Modes of Convergence

The modes of convergence for vectors (Definition [[§43 Weak and Weak-Star Convergence#^def-43-1|§43.1]]) carry over to sequences of bounded linear maps. Throughout, $X$ and $Y$ are normed linear spaces, and $A_n \in \mathcal{L}(X, Y)$ for $n = 1, 2, \ldots$, $A_0 \in \mathcal{L}(X, Y)$.

> [!definition] Definition §45.1: Uniform Convergence of Operators
> The sequence $\{A_n\}_{n=1}^\infty$ **converges uniformly** to $A_0$, written $A_n \rightrightarrows A_0$ as $n \to \infty$, if
>
> $$
> \lim_{n \to \infty} \|A_n - A_0\| = 0 ,
> $$
>
> where $\|\cdot\|$ is the operator norm of $\mathcal{L}(X, Y)$ (Definition [[§30 Boundedness and Continuity#^def-30-3|§30.3]]). Uniform convergence is also called **convergence in norm**.
>
> *Lax: §15.2 (the uniform topology of $\mathcal{L}(X, U)$)*

^def-45-1

> [!definition] Definition §45.2: Strong Convergence of Operators
> The sequence $\{A_n\}_{n=1}^\infty$ **converges strongly** to $A_0$, written $A_n \to A_0$ as $n \to \infty$ or $\mathop{\text{s-lim}}_{n \to \infty} A_n = A_0$, if for every $x \in X$
>
> $$
> \lim_{n \to \infty} \|A_n x - A_0 x\|_Y = 0 .
> $$
>
> *Lax: §15.2, definition of strong sequential convergence*

^def-45-2

> [!remark]- Connections
> - Used in the companion chapter for the completeness relation: [[§48 The Completeness Relation#^thm-48-2|§48.2]] (strong) against [[§48 The Completeness Relation#^prop-48-3|§48.3]] (not in norm).

> [!definition] Definition §45.3: Weak Convergence of Operators
> The sequence $\{A_n\}_{n=1}^\infty$ **converges weakly** to $A_0$, written $A_n \rightharpoonup A_0$ as $n \to \infty$ or $\mathop{\text{w-lim}}_{n \to \infty} A_n = A_0$, if for every $x \in X$ and every $\ell \in Y'$
>
> $$
> \lim_{n \to \infty} \ell(A_n x) = \ell(A_0 x) ,
> $$
>
> that is, if $A_n x \rightharpoonup A_0 x$ in $Y$ for every $x \in X$.
>
> *Lax: §15.2, definition of weak sequential convergence, and (18) in §15.3*

^def-45-3

Uniform convergence is convergence in the normed linear space $\mathcal{L}(X, Y)$ (Theorem [[§30 Boundedness and Continuity#^thm-30-8|§30.8]]); strong convergence is strong convergence of the vectors $A_n x$ for each $x$ separately; weak convergence is weak convergence of the vectors $A_n x$ for each $x$ separately.

> [!theorem] Proposition §45.1: Uniform Implies Strong Implies Weak
> Let $X$, $Y$ be normed linear spaces and $A_n, A_0 \in \mathcal{L}(X, Y)$.
>
> 1. If $A_n \rightrightarrows A_0$, then $A_n \to A_0$ strongly.
> 2. If $A_n \to A_0$ strongly, then $A_n \rightharpoonup A_0$ weakly.

^prop-45-1

> [!proof]+ Proof
> *(Stated in lecture; the proof is filled in.)*
>
> (1) Let $x \in X$. Since $A_n - A_0 \in \mathcal{L}(X, Y)$, Proposition [[§30 Boundedness and Continuity#^prop-30-1|§30.1]](b) gives
>
> $$
> \|A_n x - A_0 x\|_Y = \|(A_n - A_0) x\|_Y \le \|A_n - A_0\|\, \|x\|_X \longrightarrow 0 \qquad \text{as } n \to \infty .
> $$
>
> (2) Let $x \in X$ and $\ell \in Y'$. By linearity and boundedness of $\ell$,
>
> $$
> |\ell(A_n x) - \ell(A_0 x)| = |\ell(A_n x - A_0 x)| \le \|\ell\|\, \|A_n x - A_0 x\|_Y \longrightarrow 0 \qquad \text{as } n \to \infty .
> $$
>
> This is Proposition [[§43 Weak and Weak-Star Convergence#^prop-43-1|§43.1]](1), applied to the vectors $A_n x$ in $Y$.

^pf-45-1

*Uses:* [[§30 Boundedness and Continuity#^prop-30-1|§30.1]], [[§43 Weak and Weak-Star Convergence#^prop-43-1|§43.1]]

> [!theorem] Theorem §45.2: Weakly Convergent Sequences of Operators are Bounded
> Let $X$ be a Banach space, $Y$ a normed linear space, and $\{A_n\}_{n=1}^\infty \subset \mathcal{L}(X, Y)$, $A_0 \in \mathcal{L}(X, Y)$. If $A_n \rightharpoonup A_0$ weakly, then
>
> $$
> \sup_n \|A_n\| < \infty .
> $$
>
> By Proposition [[§45 Convergence of Operators#^prop-45-1|§45.1]] the same holds if $A_n \to A_0$ strongly or $A_n \rightrightarrows A_0$.
>
> *Lax: §15.3, Cor 7$'$ (for Banach spaces $X$, $U$)*

^thm-45-2

> [!proof]+ Proof
> The notes say: by the uniform boundedness principle.
>
> **Step 1: pointwise bounded.** Fix $x \in X$. By hypothesis $A_n x \rightharpoonup A_0 x$ in $Y$. A weakly convergent sequence is bounded (Theorem [[§43 Weak and Weak-Star Convergence#^thm-43-4|§43.4]]), so
>
> $$
> \sup_n \|A_n x\|_Y < \infty \qquad \text{for every } x \in X .
> $$
>
> **Step 2: uniformly bounded.** $X$ is a Banach space and $\{A_n\}$ is a family of bounded linear maps from $X$ to the normed linear space $Y$ that is bounded at every point of $X$. By the uniform boundedness principle (Theorem [[§42 Uniform Boundedness and Approximation#^thm-42-6|§42.6]]), $\sup_n \|A_n\| < \infty$.

^pf-45-2

*Uses:* [[§43 Weak and Weak-Star Convergence#^thm-43-4|§43.4]], [[§42 Uniform Boundedness and Approximation#^thm-42-6|§42.6]]

> [!remark] Remark: Completeness of the Domain
> The notes state the theorem for normed linear spaces $X$ and $Y$. Step 2 uses the completeness of $X$, and without it the conclusion can fail: on $X = c_{00}$ the functionals $\ell_n(x) = n\, x_n$ converge to $0$ at every point, hence strongly and weakly as maps $c_{00} \to \mathbb{F}$, while $\|\ell_n\| = n$ (Example [[§43 Weak and Weak-Star Convergence#^ex-43-7|§43.7]]). Completeness of $Y$ is not needed: Step 1 uses the uniform boundedness principle on the dual $Y'$, which is always complete.

^rem-45-1

## The Shifts on $\ell^2$

Neither implication of Proposition [[§45 Convergence of Operators#^prop-45-1|§45.1]] can be reversed. Both examples live on $\ell^2$ (Definition [[§18 Minkowski's Inequality and the Spaces ℓᵖ#^def-18-1|§18.1]]), with $e_n = (0, \ldots, 0, 1, 0, \ldots)$, the $1$ in the $n$-th place.

> [!example] Example §45.1: Strong but Not Uniform Convergence: Powers of the Left Shift
> Let $T : \ell^2 \to \ell^2$ be the **left shift**,
>
> $$
> T(a_1, a_2, a_3, \ldots) = (a_2, a_3, a_4, \ldots) , \qquad \text{so} \qquad T^j(a_1, a_2, \ldots) = (a_{j+1}, a_{j+2}, \ldots) .
> $$
>
> Then $T \in \mathcal{L}(\ell^2, \ell^2)$, and for the powers $T^j$, $j = 1, 2, \ldots$:
>
> 1. $T^j \to 0$ strongly as $j \to \infty$;
> 2. $\|T^j\| = 1$ for every $j$, so $T^j \not\rightrightarrows 0$.
>
> Strong convergence does not imply uniform convergence.

^ex-45-1

> [!proof]+ Proof
> $T$ is linear, since it acts coordinate by coordinate. For $x = (x_1, x_2, \ldots) \in \ell^2$,
>
> $$
> \|T^j x\|^2 = \sum_{i=1}^\infty |x_{j+i}|^2 = \sum_{i=j+1}^\infty |x_i|^2 \le \sum_{i=1}^\infty |x_i|^2 = \|x\|^2 .
> $$
>
> So $T^j x \in \ell^2$ and $\|T^j x\| \le \|x\|$: each $T^j$ is bounded, with $\|T^j\| \le 1$.
>
> (1) Since $\sum_{i=1}^\infty |x_i|^2$ converges, its tails tend to $0$:
>
> $$
> \|T^j x - 0\| = \Bigl( \sum_{i=j+1}^\infty |x_i|^2 \Bigr)^{1/2} \longrightarrow 0 \qquad \text{as } j \to \infty, \text{ for every } x \in \ell^2 .
> $$
>
> (2) $T e_n = e_{n-1}$ for $n \ge 2$, so $T^j e_n = e_{n-j}$ for $n > j$; in particular $T^j e_{j+1} = e_1$. Since $\|e_{j+1}\| = 1$ and $\|T^j e_{j+1}\| = \|e_1\| = 1$, $\|T^j\| \ge 1$ (Proposition [[§30 Boundedness and Continuity#^prop-30-1|§30.1]](a)). With $\|T^j\| \le 1$, $\|T^j\| = 1$ for every $j$. So $\|T^j - 0\| = 1$ does not tend to $0$.

^pf-ex-45-1

*Uses:* [[§30 Boundedness and Continuity#^prop-30-1|§30.1]]

> [!remark]- Connections
> - On a finite-dimensional space a linear operator is injective if and only if it is surjective: [[§10 Invertibility and Isomorphisms#^ladr-3-65|LADR 3.65]]. The left shift is surjective but not injective, and the right shift injective but not surjective, so this fails on $\ell^2$.

> [!example] Example §45.2: Weak but Not Strong Convergence: Powers of the Right Shift
> *(Lecture 20.)* Let $S : \ell^2 \to \ell^2$ be the **right shift**,
>
> $$
> S(a_1, a_2, a_3, \ldots) = (0, a_1, a_2, \ldots) , \qquad \text{so} \qquad S^j(a_1, a_2, \ldots) = (\underbrace{0, \ldots, 0}_{j}, a_1, a_2, \ldots) .
> $$
>
> Then $S \in \mathcal{L}(\ell^2, \ell^2)$, and:
>
> 1. $S^j \rightharpoonup 0$ weakly as $j \to \infty$;
> 2. $\|S^j x\| = \|x\|$ for every $x \in \ell^2$ and every $j$, so $S^j \not\to 0$ strongly.
>
> Weak convergence does not imply strong convergence.

^ex-45-2

> [!proof]+ Proof
> $S$ is linear, and $\|S^j x\|^2 = \sum_{i=1}^\infty |x_i|^2 = \|x\|^2$, since $S^j x$ has the same nonzero entries as $x$. This is (2): for $x \neq 0$, $\|S^j x - 0\| = \|x\|$ does not tend to $0$. It also shows $S^j \in \mathcal{L}(\ell^2, \ell^2)$ with $\|S^j\| = 1$. Nor does $\{S^j\}$ converge strongly to any other $A \in \mathcal{L}(\ell^2, \ell^2)$: strong convergence would give $S^j x \rightharpoonup Ax$ (Proposition [[§45 Convergence of Operators#^prop-45-1|§45.1]](2)), while $S^j x \rightharpoonup 0$ by (1), and weak limits are unique (Proposition [[§43 Weak and Weak-Star Convergence#^prop-43-1|§43.1]](2)); so $A = 0$, which is excluded.
>
> (1) Every $\ell \in (\ell^2)'$ is $\ell(u) = (u, y) = \sum_i u_i\, \overline{y_i}$ for some $y \in \ell^2$ (Example [[§31 Dual Spaces#^ex-31-1|§31.1]]). The $i$-th entry of $S^j x$ is $x_{i-j}$ for $i > j$ and $0$ for $i \le j$, so by the Cauchy–Schwarz inequality
>
> $$
> |\ell(S^j x)| = \Bigl| \sum_{i=j+1}^\infty x_{i-j}\, \overline{y_i} \Bigr| \le \Bigl( \sum_{i=j+1}^\infty |x_{i-j}|^2 \Bigr)^{1/2} \Bigl( \sum_{i=j+1}^\infty |y_i|^2 \Bigr)^{1/2} = \|x\| \Bigl( \sum_{i=j+1}^\infty |y_i|^2 \Bigr)^{1/2} \longrightarrow 0
> $$
>
> as $j \to \infty$, a tail of the convergent series $\sum_i |y_i|^2$. So $\ell(S^j x) \to 0 = \ell(0\, x)$ for all $x \in \ell^2$ and $\ell \in (\ell^2)'$.

^pf-ex-45-2

*Uses:* [[§45 Convergence of Operators#^prop-45-1|§45.1]], [[§43 Weak and Weak-Star Convergence#^prop-43-1|§43.1]], [[§31 Dual Spaces#^ex-31-1|Ex. §31.1]]

![[m556-45-1.svg]]

The two shifts applied to $x = (1, 0.8, 0.8^2, \ldots)$, entries drawn as bars. The left shift $T^j$ (blue) discards the first $j$ entries, and what remains is a tail of $x$, whose norm tends to $0$ (Example [[§45 Convergence of Operators#^ex-45-1|§45.1]]). The right shift $S^j$ (red) moves all of $x$ out to the right without changing its norm; against a fixed $y \in \ell^2$ it meets only the tail of $y$, so the inner products tend to $0$ (Example [[§45 Convergence of Operators#^ex-45-2|§45.2]]).

![[m556-45-a1.gif|460]]

*(Not from lecture; animation added, vault only.)* The powers $T^j$ and $S^j$ for $j = 0, 1, \ldots, 16$, applied to $x_i = 0.82^{\,i-1}$. Top left: $T^j x$ (blue) over $x$ (grey); the bars that remain are the tail of $x$. Bottom left: $S^j x$ (red) moving to the right over a fixed $y \in \ell^2$ (grey). Right: $\|T^j x\|$ decreases to $0$, $\|S^j x\|$ stays equal to $\|x\|$, and $|(S^j x, y)|$ decreases to $0$.

A third instance is in the companion chapter: for a complete orthonormal set $\{e_n\}$ in a Hilbert space, the partial sums $P_N$ of the completeness relation converge to the identity strongly (Theorem [[§48 The Completeness Relation#^thm-48-2|§48.2]]) but not uniformly (Proposition [[§48 The Completeness Relation#^prop-48-3|§48.3]]).
