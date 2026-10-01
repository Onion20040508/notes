---
subject: "[[Single Variable Analysis]]"
section: 32
chapter: 6
tags: [real-analysis, math451]
---
← [[§31 Taylor's Theorem]] · ↑ [[· 6 Integration]] · [[§33 Properties of the Riemann Integral]] →

Let $f: [a,b] \to \mathbb{R}$ be a function — not necessarily continuous. We want to understand when $\int_a^b f(x)\,dx$ exists, and how to define it rigorously from what we have learned. Geometrically, it should be the area under the graph — so we have the notion of the integral, right? **No.** The problem: *what is area?* We only know how to compute areas of simple regions — rectangles, triangles, trapezoids. The idea, as always in this course: approximate the complicated by the simple, and take a limit. *The limit is the key.*

## Darboux Sums and the Darboux Integral

> [!definition] Definition §32.1: Sup and Inf over a Set; Partitions; Upper and Lower Sums
> Suppose $f$ is *bounded* on $[a,b]$. For any subset $S \subseteq [a,b]$, define
>
> $$
> M(f, S) = \sup\{ f(x) \mid x \in S \}, \qquad m(f, S) = \inf\{ f(x) \mid x \in S \}
> $$
>
> (finite, by boundedness; max and min values may not exist, which is why we use $\sup$ and $\inf$). A **partition** of $[a,b]$ is a division into $n$ subintervals,
>
> $$
> P: \quad a = t_0 < t_1 < \cdots < t_n = b.
> $$
>
> For each partition define the **upper sum** and **lower sum**
>
> $$
> U(f, P) = \sum_{k=1}^n M\bigl(f, [t_{k-1}, t_k]\bigr)\,(t_k - t_{k-1}), \qquad
> L(f, P) = \sum_{k=1}^n m\bigl(f, [t_{k-1}, t_k]\bigr)\,(t_k - t_{k-1})
> $$
>
> — geometrically, sums of areas of rectangles circumscribing and inscribed in the region under the graph. If the integral exists (whatever it is), it should clearly satisfy $L(f,P) \leq \int_a^b f \leq U(f,P)$.

^def-32-1

> [!remark]- Connections
> - Two-dimensional version, partitioning a Jordan measurable region into pieces of area |Dᵢ|: [[§15 Multivariable Integration#^def-15-7|452 Def. §15.7]] and [[§15 Multivariable Integration#^def-15-8|452 Def. §15.8]].

> [!definition] Definition §32.2: Darboux Integrals
> The **Darboux upper integral** and **lower integral** are
>
> $$
> U(f) = \inf\{ U(f,P) \mid P \text{ a partition of } [a,b] \}, \quad
> L(f) = \sup\{ L(f,P) \mid P \text{ a partition of } [a,b] \}.
> $$
>
> $f$ is called **Darboux integrable** if $L(f) = U(f)$, and then $\int_a^b f\,dx$ is defined to be this common value.

^def-32-2

![[m451-32-1.svg]]
*Left: an uneven partition $P$; the upper sum (red outline) and lower sum (blue fill) trap the curve. Right: a refinement of $P$ — four more points inserted (unlabeled ticks): the gap boxes of the refinement (blue) sit inside the gap boxes of $P$ (red outline), so $U - L$ shrinks subinterval by subinterval — the Refinement Lemma in one picture.*

> [!remark]- Connections
> - Double integral over a region, with integrability defined by upper minus lower sum tending to 0: [[§15 Multivariable Integration#^def-15-10|452 Def. §15.10]] and [[§15 Multivariable Integration#^def-15-11|452 Def. §15.11]].

> [!example] Example §32.1: The identity function
> Show $f(x) = x$ is Darboux integrable on $[0,1]$ and $\int_0^1 x\,dx = \tfrac12$. (We know the value from the Fundamental Theorem — but here we must prove it *from the definition*.)
>
> *Idea:* find partitions for which $U(f,P)$ and $L(f,P)$ come close to a common value $I$. Take the equal division $P_n: t_k = \tfrac kn$. On $[t_{k-1}, t_k]$, $f = x$ is increasing, so its sup is $\tfrac kn$ and inf is $\tfrac{k-1}{n}$:
>
> $$
> U(f, P_n) = \sum_{k=1}^n \frac kn \cdot \frac1n = \frac{1}{n^2}\, \frac{n(n+1)}{2} = \frac12\left(1 + \frac1n\right),
> \quad
> L(f, P_n) = \frac{1}{n^2}\, \frac{(n-1)n}{2} = \frac12\left(1 - \frac1n\right).
> $$
>
> Since $U(f)$ is an infimum over *all* partitions, $U(f) \leq U(f, P_n) = \tfrac12(1 + \tfrac1n)$ for every $n$; letting $n \to \infty$, $U(f) \leq \tfrac12$. Similarly $L(f) \geq \tfrac12$. Combined with the theorem below ($L(f) \leq U(f)$),
>
> $$
> \frac12 \leq L(f) \leq U(f) \leq \frac12,
> $$
>
> forcing equality: $f$ is integrable with $\int_0^1 x\,dx = \tfrac12$.

^ex-32-1

![[m451-32-3.svg]]
*The equal partition $P_n$ for $f(x) = x$ on $[0,1]$ (here $n = 5$): the lower sum is the blue staircase, and the upper sum adds the $n$ red squares along the diagonal, each of side $\tfrac1n$. So $U(f,P_n) - L(f,P_n) = n \cdot \tfrac{1}{n^2} = \tfrac1n \to 0$, squeezing both sums onto $\tfrac12$.*

> [!example] Example §32.2: A step function
> Show $g: [0,2] \to \mathbb{R}$, $g(x) = 1$ for $x \in [0,1)$ and $g(x) = 0$ for $x \in [1,2]$, is Darboux integrable. Given $\varepsilon > 0$, isolate the jump in a short subinterval: take
>
> $$
> P: \quad 0 < 1 - \tfrac\varepsilon2 < 1 < 2.
> $$
>
> On $[0, 1-\tfrac\varepsilon2]$: $M = m = 1$. On $[1-\tfrac\varepsilon2, 1]$: $M = 1$, $m = 0$ (the value at $1$). On $[1,2]$: $M = m = 0$. So
>
> $$
> U(g,P) = \left(1 - \tfrac\varepsilon2\right) + \tfrac\varepsilon2 = 1, \qquad L(g,P) = 1 - \tfrac\varepsilon2,
> $$
>
> and $U(g,P) - L(g,P) = \tfrac\varepsilon2 < \varepsilon$. By the Cauchy criterion below, $g$ is integrable; and since $L(g) \geq 1 - \tfrac\varepsilon2$ for every $\varepsilon$ while $U(g) \leq 1$, the integral is $\int_0^2 g = 1$. A jump discontinuity does not destroy integrability.

^ex-32-2

![[m451-32-4.svg]]
*The jump isolated: $g$ (blue; filled dot $g(1) = 0$, hollow dot at the value $1$ not taken at $x = 1$) with $P: 0 < 1 - \tfrac\varepsilon2 < 1 < 2$. Upper and lower sums agree except on the short subinterval $[1 - \tfrac\varepsilon2, 1]$, where $M = 1$ and $m = 0$: the red strip is the whole gap, $U(g,P) - L(g,P) = \tfrac\varepsilon2$.*

> [!example] Example §32.3: The Dirichlet function is not integrable
> Let $f(x) = 1$ for $x \in \mathbb{Q}$, $f(x) = 0$ for $x \notin \mathbb{Q}$. Then $f$ is *not* integrable on $[0,1]$: every subinterval $[t_{k-1}, t_k]$ of every partition contains both rationals and irrationals (density of both, §4 and §17), so
>
> $$
> M\bigl(f, [t_{k-1},t_k]\bigr) = 1, \qquad m\bigl(f, [t_{k-1},t_k]\bigr) = 0
> $$
>
> always. Hence $U(f,P) = 1$ and $L(f,P) = 0$ for *every* partition, giving $U(f) = 1 \neq 0 = L(f)$.

^ex-32-3

> [!remark]- Connections
> - Same example in 551 ([[§8 Motivation꞉ The Riemann Integral#^ex-8-2|551 Ex. §8.2]]): the Dirichlet function vanishes off the null set ℚ ([[§9 Lebesgue Outer Measure#^ex-9-2|551 Ex. §9.2]]), so it is Lebesgue integrable with integral 0.

## Lower Is at Most Upper

> [!theorem] Theorem §32.1: Lower Integral at Most Upper Integral
> For every bounded $f: [a,b] \to \mathbb{R}$:    $L(f) \leq U(f)$.

^thm-32-1

Is this obvious? Maybe not: $L(f)$ and $U(f)$ are a sup and an inf over *different* competitions. The proof goes through two lemmas.

> [!theorem] Lemma §32.2: Refinement Lemma
> Let $P, Q$ be partitions of $[a,b]$ with $Q$ a **refinement** of $P$ (every cut point of $P$ is a cut point of $Q$). Then
>
> $$
> L(f, P) \leq L(f, Q) \leq U(f, Q) \leq U(f, P).
> $$

^lem-32-2

> [!proof]+ Proof
> The middle inequality holds for any single partition, since $m \leq M$ on each subinterval. For the outer ones, it suffices (by induction on the number of added points) to add *one* cut point $c$ to one subinterval $[t_{k-1}, t_k]$. The sup over a subset is at most the sup over the whole:
>
> $$
> M\bigl(f, [t_{k-1}, c]\bigr),\ M\bigl(f, [c, t_k]\bigr) \ \leq\ M\bigl(f, [t_{k-1}, t_k]\bigr),
> $$
>
> so
>
> $$
> M(f,[t_{k-1},c])(c - t_{k-1}) + M(f,[c,t_k])(t_k - c) \leq M(f,[t_{k-1},t_k])(t_k - t_{k-1}),
> $$
>
> and summing over the (unchanged) other subintervals, $U(f,Q) \leq U(f,P)$. Dually, infima over subsets are $\geq$, giving $L(f,Q) \geq L(f,P)$.

^pf-32-2

> [!theorem] Lemma §32.3: Cross Lemma
> For *any* two partitions $P, Q$ (with no relation between them):
>
> $$
> L(f, P) \leq U(f, Q).
> $$

^lem-32-3

> [!proof]+ Proof
> The trick is a middle stepping-stone: combine $P$ and $Q$ into the common refinement $P \cup Q$ (all cut points of both). It refines both, so by the Refinement Lemma twice:
>
> $$
> L(f,P) \leq L(f, P\cup Q) \leq U(f, P \cup Q) \leq U(f, Q),
> $$
>
> the middle inequality being the single-partition fact $m \leq M$.

^pf-32-3

> [!proof]+ Proof
> Fix any partition $Q$. By the Cross Lemma, $U(f,Q)$ is an upper bound for *all* the lower sums, so
>
> $$
> L(f) = \sup_P L(f,P) \leq U(f, Q).
> $$
>
> Now $L(f)$ is a lower bound for all the upper sums, so
>
> $$
> L(f) \leq \inf_Q U(f,Q) = U(f).
> $$

^pf-32-1

## The Cauchy Criterion for Integrability

> [!theorem] Theorem §32.4: Cauchy Criterion
> A bounded $f: [a,b] \to \mathbb{R}$ is Darboux integrable if and only if for every $\varepsilon > 0$ there exists a partition $P$ such that
>
> $$
> U(f, P) - L(f, P) < \varepsilon.
> $$

^thm-32-4

This is convenient: we may pick a *special* partition, usually the equal division, as in the examples above.

> [!proof]+ Proof
> ($\Rightarrow$) Suppose $f$ is integrable. Given $\varepsilon$, by the characterizations of sup and inf there are partitions $P, Q$ with
>
> $$
> L(f, P) \geq L(f) - \frac\varepsilon2, \qquad U(f, Q) \leq U(f) + \frac\varepsilon2.
> $$
>
> Pass to the common refinement $P \cup Q$: by the Refinement Lemma the two estimates persist,
>
> $$
> L(f, P\cup Q) \geq L(f) - \frac\varepsilon2, \qquad U(f, P\cup Q) \leq U(f) + \frac\varepsilon2,
> $$
>
> and since $L(f) = U(f)$, subtracting gives $U(f, P\cup Q) - L(f, P\cup Q) \leq \varepsilon$.
>
> ($\Leftarrow$) For any such $P$,
>
> $$
> U(f) - L(f) \leq U(f,P) - L(f,P) < \varepsilon.
> $$
>
> Since $\varepsilon$ is arbitrary, $U(f) - L(f) \leq 0$; combined with $U(f) - L(f) \geq 0$ (previous theorem), $U(f) = L(f)$: integrable.

^pf-32-4

In computations one usually runs a whole *sequence* of partitions and takes limits — as in the identity-function example above. The following packages that pattern once and for all, value included:

> [!theorem] Proposition §32.5: Sequential Criterion with Value (HW)
> Let $f$ be bounded on $[a,b]$, and suppose there are sequences $(U_n)$, $(L_n)$ of upper and lower Darboux sums of $f$ with $U_n - L_n \to 0$. Then $f$ is integrable and
>
> $$
> \int_a^b f\,dx = \lim_{n\to\infty} U_n = \lim_{n\to\infty} L_n.
> $$

^prop-32-5

> [!proof]+ Proof
> Every upper sum bounds $U(f)$ from above and every lower sum bounds $L(f)$ from below, so for each $n$,
>
> $$
> L_n \leq L(f) \leq U(f) \leq U_n, \qquad \text{hence} \qquad 0 \leq U(f) - L(f) \leq U_n - L_n \to 0,
> $$
>
> forcing $U(f) = L(f)$: $f$ is integrable, with $\int_a^b f$ trapped in every $[L_n, U_n]$. Then
>
> $$
> 0 \leq U_n - \int_a^b f \leq U_n - L_n \to 0
> \qquad \text{and} \qquad
> 0 \leq \int_a^b f - L_n \leq U_n - L_n \to 0,
> $$
>
> so both sequences converge to the integral by squeezing.

^pf-32-5

For example, the equal partitions for $f(x) = x^3$ on $[0, b]$ give (via $\sum_{k=1}^n k^3 = \tfrac{n^2(n+1)^2}{4}$, proved by induction in §1)

$$
U_n = \frac{b^4 (n+1)^2}{4 n^2}, \qquad L_n = \frac{b^4 (n-1)^2}{4 n^2}, \qquad U_n - L_n = \frac{b^4}{n} \to 0,
$$

so $x^3$ is integrable on $[0,b]$ with $\int_0^b x^3\,dx = \lim U_n = \tfrac{b^4}{4}$ — no separate sup/inf bookkeeping needed.

## Riemann Sums and the Riemann Integral

> [!definition] Definition §32.3: Mesh; Riemann Sums; Riemann Integrability
> For a partition $P$, define its **mesh** by $\operatorname{mesh}(P) = \max\{ t_k - t_{k-1} \}$ (for the equal partition into $n$ pieces, $\operatorname{mesh} = \tfrac{b-a}{n}$). For bounded $f$, a **Riemann sum** associated with $P$ is
>
> $$
> S = \sum_{k=1}^n f(x_k)\,(t_k - t_{k-1}), \qquad x_k \in [t_{k-1}, t_k] \text{ arbitrary}
> $$
>
> — compare with $U(f,P)$ and $L(f,P)$, which bracket every such $S$. $f$ is called **Riemann integrable** if there exists a value $r$ such that: for every $\varepsilon > 0$ there is $\delta > 0$ such that for every partition $P$ with $\operatorname{mesh}(P) < \delta$ and every Riemann sum $S$ associated with $P$,
>
> $$
> |S - r| < \varepsilon.
> $$
>
> The value $r$ is the **Riemann integral** of $f$.

^def-32-3

![[m451-32-2.svg]]
*A Riemann sum: both choices are arbitrary — the partition points $t_k$ (unequal lengths; $\operatorname{mesh}(P)$ is the widest) and the tags $x_k$ inside each piece, with rectangle heights $f(x_k)$, neither sup nor inf. Dashed red and blue mark the sup $M$ and inf $m$ of $f$ on each subinterval: every Riemann sum is squeezed, $L(f,P) \leq S \leq U(f,P)$ — the mechanism behind the equivalence theorem below.*

One difficulty in *using* this definition: we need a candidate value $r$ before we can check anything — whereas the Darboux definition asks only for the sup and inf to meet. Fortunately:

> [!remark]- Connections
> - In the plane the mesh is the largest diameter of a piece: [[§15 Multivariable Integration#^def-15-9|452 Def. §15.9]].
> - Recapped in 551 as [[§8 Motivation꞉ The Riemann Integral#^def-8-3|551 Def. §8.3]]; every Riemann integrable function is Lebesgue integrable with the same integral, [[§15 The General Lebesgue Integral#^thm-15-10|551 Thm. §15.10]].

> [!theorem] Theorem §32.6: Equivalence of the Two Integrals
> 1. $f: [a,b] \to \mathbb{R}$ is Riemann integrable if and only if it is Darboux integrable (and the values agree).
>
> 2. (Mesh form of the Cauchy criterion) $f$ is Darboux integrable if and only if for every $\varepsilon > 0$ there is $\delta > 0$ such that *every* partition with $\operatorname{mesh}(P) < \delta$ satisfies $U(f,P) - L(f,P) < \varepsilon$.

^thm-32-6

These were stated without proof in lecture (the proofs take too much time; see the book for details). The essential difference between the two notions is that Riemann's requires a limit in the $\varepsilon$-$\delta$ sense over the mesh, which (2) supplies on the Darboux side. From now on, “integrable” means either.

> [!theorem] Theorem §32.7: Continuous Functions Are Integrable
> If $f: [a,b] \to \mathbb{R}$ is continuous ($a, b$ finite), then $f$ is integrable.

^thm-32-7

> [!proof]+ Proof
> We show $f$ is Darboux integrable via the Cauchy criterion. The key: since $f$ is continuous on the closed bounded $[a,b]$, it is *uniformly continuous* (§19 — this is exactly the application promised there). So for every $\varepsilon > 0$ there exists $\delta > 0$ such that
>
> $$
> |x - y| < \delta \implies |f(x) - f(y)| < \frac{\varepsilon}{b-a}.
> $$
>
> Choose $n$ so large that $\tfrac{b-a}{n} < \delta$, and let $P$ be the equal partition into $n$ subintervals. On each $[t_{k-1}, t_k]$, any two points are within $\delta$, so any two values of $f$ differ by less than $\tfrac{\varepsilon}{b-a}$; taking suprema over pairs,
>
> $$
> M\bigl(f,[t_{k-1},t_k]\bigr) - m\bigl(f,[t_{k-1},t_k]\bigr) \leq \frac{\varepsilon}{b-a}.
> $$
>
> Therefore
>
> $$
> U(f,P) - L(f,P) = \sum_{k=1}^n \bigl(M_k - m_k\bigr)\,\frac{b-a}{n} \leq \sum_{k=1}^n \frac{\varepsilon}{b-a}\cdot\frac{b-a}{n} = \varepsilon.
> $$

^pf-32-7
