---
type: section
subject: "[[Complex Variables]]"
chapter: 4
section: 58
bc: "58"
aliases: ["B&C 58"]
tags: [complex-variables, math342]
---
← [[§57 Some Consequences of the Extension]] · ↑ [[· 4 Integrals]] · [[§59 Maximum Modulus Principle]] →

*Brown–Churchill, Section 58 (with Exercises 1 and 8 of Section 59) · MAT 342 HW 8 · Practice Finals (Fall 2009, Fall 2002).*

Cauchy's inequality bounds $|f'(z_0)|$ by $M_R/R$, where $M_R$ is the maximum of $|f|$ on a circle of radius $R$ about $z_0$. If $f$ is entire and bounded, $R$ can be taken as large as we please with $M_R$ staying bounded, so $f' = 0$: a bounded entire function is constant (Liouville's theorem). Applied to $1/P(z)$, this proves the fundamental theorem of algebra: a nonconstant polynomial has a zero, and therefore factors completely into linear factors. The vault has two other proofs of the fundamental theorem of algebra, one by a minimum argument (Linear Algebra) and one by the fundamental group of the circle (Topology); this one is the shortest, because the hard work was done in the Cauchy–Goursat theorem.

> [!theorem] Theorem §58.1: Liouville's Theorem
> If a function $f$ is entire and bounded in the complex plane, then $f(z)$ is constant throughout the plane.
>
> *B&C: Sec. 58, Theorem 1*

^thm-58-1

> [!proof]+ Proof
> Assume that $f$ is as stated. Since $f$ is entire, Cauchy's inequality ([[§57 Some Consequences of the Extension#^thm-57-4|Theorem §57.4]]) can be applied with any choice of $z_0$ and $R$. In particular, when $n = 1$ it tells us that
>
> $$
> |f'(z_0)| \le \frac{M_R}{R} . \qquad (1)
> $$
>
> Moreover, the boundedness condition on $f$ tells us that a nonnegative constant $M$ exists such that $|f(z)| \le M$ for all $z$; and, because the constant $M_R$ in inequality (1) is always less than or equal to $M$, it follows that
>
> $$
> |f'(z_0)| \le \frac{M}{R} , \qquad (2)
> $$
>
> where $R$ can be arbitrarily large. The number $M$ in inequality (2) is independent of the value of $R$ that is taken. Hence that inequality holds for arbitrarily large values of $R$ only if $f'(z_0) = 0$. Since the choice of $z_0$ was arbitrary, $f'(z) = 0$ everywhere in the complex plane. Consequently, $f$ is a constant function, according to the theorem in [[§25 Analytic Functions|§25]].

^pf-58-1

*Uses:* [[§57 Some Consequences of the Extension#^thm-57-4|§57.4]], [[§25 Analytic Functions|§25]] ($f' = 0$ on a domain implies $f$ constant)

In other words, no entire function except a constant is bounded in the complex plane.

> [!theorem] Theorem §58.2: Fundamental Theorem of Algebra
> Any polynomial
>
> $$
> P(z) = a_0 + a_1z + a_2z^2 + \cdots + a_nz^n \qquad (a_n \ne 0)
> $$
>
> of degree $n$ ($n \ge 1$) has at least one zero. That is, there exists at least one point $z_0$ such that $P(z_0) = 0$.
>
> *B&C: Sec. 58, Theorem 2*

^thm-58-2

> [!proof]+ Proof
> The proof is by contradiction. Suppose that $P(z)$ is *not* zero for any value of $z$. Then the quotient $1/P(z)$ is entire, as a quotient of entire functions with nonvanishing denominator. It is also bounded in the complex plane. To see this, recall statement (6) in [[§5 Triangle Inequality|§5]]: there is a positive number $R$ such that
>
> $$
> \left| \frac{1}{P(z)} \right| < \frac{2}{|a_n|R^n} \qquad\text{whenever } |z| > R .
> $$
>
> So $1/P(z)$ is bounded in the region exterior to the disk $|z| \le R$. But $1/P(z)$ is continuous on that closed disk, and this means that $1/P(z)$ is bounded there too ([[§18 Continuity|§18]]). Hence $1/P(z)$ is bounded in the entire plane.
>
> It now follows from Liouville's theorem that $1/P(z)$, and consequently $P(z)$, is constant. But $P(z)$ is not constant: its $n$th derivative is the nonzero number $n!\,a_n$. We have reached a contradiction.

^pf-58-2

*Uses:* [[§58 Liouville's Theorem and the Fundamental Theorem of Algebra#^thm-58-1|§58.1]], [[§5 Triangle Inequality|§5]] (statement (6)), [[§18 Continuity|§18]] (continuous on a closed bounded set implies bounded)

> [!remark]- Connections
> - The other proofs in the vault: [[Fundamental theorem of algebra, first version]] ([[§13 Polynomials#^ladr-4-12|LADR 4.12]]) shows that $|P|$ attains a minimum on a large closed disk (the extreme value theorem) and that the minimum cannot be positive, by moving in a direction where the lowest-order term of $P$ about the minimum point decreases $|P|$; [[Fundamental Theorem of Algebra (topological proof)]] ([[§25 The Fundamental Theorem of Algebra#^thm-25-1|590 Thm. §25.1]]) shows that a root-free $P$ would make the loop $z^n$ on a large circle nullhomotopic in $\mathbb{R}^2 \setminus \{0\}$, contradicting $\pi_1(S^1) \cong \mathbb{Z}$. The proof here hides the analysis in Liouville's theorem, that is, in the Cauchy integral formula. (B&C also cites a proof by R. P. Boas, *Amer. Math. Monthly* 71 (1964), p. 180, that uses the Cauchy–Goursat theorem directly.)
> - The minimum argument of LADR 4.12 is a minimum modulus principle for polynomials; its general form for analytic functions is [[§59 Maximum Modulus Principle#^ex-59-2|Example §59.2]].

The fundamental theorem tells us that any polynomial $P(z)$ of degree $n$ ($n \ge 1$) can be expressed as a product of linear factors. This uses the following fact, which B&C leaves as an exercise.

> [!theorem] Lemma §58.3: Factor Theorem
> Let $z_0$ be a zero of the polynomial
>
> $$
> P(z) = a_0 + a_1z + a_2z^2 + \cdots + a_nz^n \qquad (a_n \ne 0)
> $$
>
> of degree $n$ ($n \ge 1$). Then
>
> $$
> P(z) = (z - z_0)\,Q(z) ,
> $$
>
> where $Q(z)$ is a polynomial of degree $n - 1$.
>
> *B&C: Sec. 59, Exercise 8*

^lem-58-3

> [!proof]+ Proof
> **(a)** For $k = 2, 3, \ldots$,
>
> $$
> z^k - z_0^k = (z - z_0)\big(z^{k-1} + z^{k-2}z_0 + \cdots + zz_0^{k-2} + z_0^{k-1}\big) .
> $$
>
> Indeed, multiplying out, $z$ times the sum is $z^k + z^{k-1}z_0 + \cdots + zz_0^{k-1}$ and $z_0$ times the sum is $z^{k-1}z_0 + \cdots + zz_0^{k-1} + z_0^k$; their difference telescopes to $z^k - z_0^k$. For $k = 1$ the identity $z - z_0 = (z - z_0) \cdot 1$ is trivial.
>
> **(b)** Hence
>
> $$
> P(z) - P(z_0) = \sum_{k=1}^{n}a_k\big(z^k - z_0^k\big) = (z - z_0)\,Q(z), \qquad Q(z) = \sum_{k=1}^{n}a_k\sum_{j=0}^{k-1}z^{k-1-j}z_0^{\,j} .
> $$
>
> $Q$ is a polynomial, and only the term $k = n$, $j = 0$ contains $z^{n-1}$, with coefficient $a_n \ne 0$; so $Q$ has degree $n - 1$. Since $P(z_0) = 0$, $P(z) = (z - z_0)\,Q(z)$.

^pf-58-3

> [!remark]- Connections
> - The same statement and proof over any field: [[§13 Polynomials#^ladr-4-6|LADR 4.6]]; the resulting factorization is [[§13 Polynomials#^ladr-4-13|LADR 4.13]], with a uniqueness statement that B&C does not include.

> [!theorem] Corollary §58.4: Factorization into Linear Factors
> Any polynomial $P(z) = a_0 + a_1z + \cdots + a_nz^n$ ($a_n \ne 0$) of degree $n$ ($n \ge 1$) can be expressed as a product of linear factors:
>
> $$
> P(z) = c(z - z_1)(z - z_2)\cdots(z - z_n) , \qquad (3)
> $$
>
> where $c$ and $z_k$ ($k = 1, 2, \ldots, n$) are complex constants (in fact $c = a_n$). Some of the constants $z_k$ may appear more than once, but $P(z)$ has no more than $n$ distinct zeros.
>
> *B&C: Sec. 58 (text)*

^cor-58-4

> [!proof]+ Proof
> By induction on $n$. For $n = 1$, $P(z) = a_1\big(z - (-a_0/a_1)\big)$. Let $n \ge 2$. The fundamental theorem ensures that $P(z)$ has a zero $z_1$. Then, according to Lemma §58.3,
>
> $$
> P(z) = (z - z_1)\,Q_1(z) ,
> $$
>
> where $Q_1(z)$ is a polynomial of degree $n - 1$, with leading coefficient $a_n$. The same argument, applied to $Q_1(z)$, reveals that there is a number $z_2$ such that $P(z) = (z - z_1)(z - z_2)\,Q_2(z)$, where $Q_2(z)$ is a polynomial of degree $n - 2$. Continuing in this way (formally, by the induction hypothesis for $Q_1$), we arrive at expression (3), with $c = a_n$ since the leading coefficient is preserved at each step. Finally, if $P(w) = 0$, then $c(w - z_1)\cdots(w - z_n) = 0$ with $c \ne 0$, so one of the factors vanishes and $w$ is one of $z_1, \ldots, z_n$: $P(z)$ can have no more than $n$ distinct zeros.

^pf-58-4

*Uses:* [[§58 Liouville's Theorem and the Fundamental Theorem of Algebra#^thm-58-2|§58.2]], [[§58 Liouville's Theorem and the Fundamental Theorem of Algebra#^lem-58-3|§58.3]]

## Examples

> [!example] Example §58.1: A Harmonic Function Bounded Above
> Suppose that $f(z)$ is entire and that the harmonic function $u(x, y) = \operatorname{Re}[f(z)]$ has an upper bound $u_0$; that is, $u(x, y) \le u_0$ for all points $(x, y)$ in the $xy$ plane. Show that $u(x, y)$ must be constant throughout the plane.
>
> Apply Liouville's theorem to $g(z) = \exp[f(z)]$, which is entire as a composition of entire functions. Since $|e^w| = e^{\operatorname{Re} w}$,
>
> $$
> |g(z)| = e^{u(x, y)} \le e^{u_0} \qquad\text{for all } z ,
> $$
>
> so $g$ is bounded and therefore constant. Then $0 = g'(z) = f'(z)e^{f(z)}$, and since $e^{f(z)} \ne 0$, $f'(z) = 0$ for all $z$. By the theorem in [[§25 Analytic Functions|§25]], $f$ is constant, and so is its real part $u$. (The step from "$e^f$ is constant" to "$f$ is constant" needs an argument: $e^w$ takes each nonzero value at infinitely many points $w$, so constancy of $e^f$ alone says only that $f$ takes values in such a set; the derivative settles it.)
>
> *B&C: Sec. 59, Exercise 1; Source: 342 HW 8*

^ex-58-1

> [!example] Example §58.2: sin z Is Unbounded
> Is there a positive number $M$ such that the inequality $|\sin z| \le M$ holds for all complex numbers $z$?
>
> **No.** The function $\sin z$ is entire and not constant ($\sin 0 = 0$, $\sin\frac\pi2 = 1$). By Liouville's theorem a bounded entire function is constant, so $\sin z$ is not bounded. Directly: on the imaginary axis $\sin(iy) = i\sinh y$, and $|\sin(iy)| = |\sinh y| \to \infty$ as $y \to \infty$. (Compare the real sine, which is bounded by $1$ on the real line: boundedness on a line says nothing.)
>
> *Source: 342 practice final (Fall 2009), Q1(b)*

^ex-58-2

> [!example] Example §58.3: An Entire Function Bounded by |z|e^{−|z|}
> **True or false:** there exists an entire non-constant function $f(z)$ satisfying the inequality $|f(z)| \le |z|e^{-|z|}$.
>
> **False.** The function $r \mapsto re^{-r}$ ($r \ge 0$) has derivative $(1 - r)e^{-r}$, so its maximum is $e^{-1}$, at $r = 1$. Hence $|f(z)| \le 1/e$ for all $z$: $f$ is a bounded entire function, and by Liouville's theorem it is constant. (In fact $f \equiv 0$, since $|f(z)| \le |z|e^{-|z|} \to 0$ as $|z| \to \infty$, or simply since $|f(0)| \le 0$.)
>
> *Source: 342 practice final (Fall 2002), Q8(b)*

^ex-58-3
