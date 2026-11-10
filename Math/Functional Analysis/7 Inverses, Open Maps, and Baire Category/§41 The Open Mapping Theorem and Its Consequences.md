---
type: section
subject: "[[Functional Analysis]]"
chapter: 7
section: 41
tags: [functional-analysis, math556]
---
← [[§40 The Baire Category Theorem]] · ↑ [[· 7 Inverses, Open Maps, and Baire Category]] · [[§42 Uniform Boundedness and Approximation]] →

*Stage: maps — Thread: completeness. Baire's theorem applied to $Y = \bigcup_n M(B(0,n))$: a bounded linear map onto a Banach space is open; bounded inverses, equivalent norms and closed graphs follow.*

Throughout this section $B(x_0, r)$ denotes the *open* ball with center $x_0$ and radius $r > 0$ (in whichever space $x_0$ lies; when the space must be named, $B_X$ or $B_Y$); a closed ball is written with a closure bar.

## The Open Mapping Theorem

The open mapping theorem (Theorem [[§41 The Open Mapping Theorem and Its Consequences#^thm-41-2|§41.2]]) reduces to the following theorem, and Banach's theorem (Theorem [[§39 Solving Mx = y#^thm-39-2|§39.2]]) follows from the open mapping theorem. The theorem comes first, so that each proof follows its statement. What matters in it is that the ball in $Y$ is centered at the origin, not at an arbitrary point: linearity then moves it anywhere and rescales it.

> [!theorem] Theorem §41.1: The Image of the Unit Ball Contains a Ball About $0$
> Let $X, Y$ be Banach spaces and $M \in \mathcal{L}(X, Y)$ with $R(M) = Y$. Then there is $\delta > 0$ such that
>
> $$
> B(0, \delta) \subset M\bigl( B(0, 1) \bigr) .
> $$
>
> *Lax: §15.5, Thm 9*

^thm-41-1

> [!proof]+ Proof of Theorem [[§41 The Open Mapping Theorem and Its Consequences#^thm-41-1|§41.1]]
> **Step 1: some $\overline{M(B(0,n))}$ has an interior point.** Every $x \in X$ has $\|x\| < n$ for some $n \in \mathbb{N}$, so $X = \bigcup_{n=1}^\infty B(0, n)$. Since $M$ is onto,
>
> $$
> Y = M(X) = \bigcup_{n=1}^\infty M\bigl( B(0, n) \bigr) .
> $$
>
> $Y$ is complete, so by the Baire category theorem (Theorem [[§40 The Baire Category Theorem#^thm-40-4|§40.4]]) it is of the second category (Definition [[§40 The Baire Category Theorem#^def-40-3|§40.3]]): not every $M(B(0,n))$ is nowhere dense. So there is $n \in \mathbb{N}$ such that $\overline{M(B(0,n))}$ has an interior point, i.e. there are $z_0 \in Y$ and $r > 0$ with
>
> $$
> B(z_0, r) \subset \overline{M\bigl( B(0, n) \bigr)} .
> $$
>
> (The center $z_0$ is a point of $Y$.)
>
> **Step 2: two properties of $\overline{M(B(0,n))}$.**
>
> 1. *Symmetry:* if $z \in \overline{M(B(0,n))}$, then $-z \in \overline{M(B(0,n))}$.
> 2. *Convexity:* $\overline{M(B(0,n))}$ is convex.
>
> Both hold first without the closure. If $z = Mx$ with $x \in B(0, n)$, then $-x \in B(0, n)$ and $-z = M(-x)$. If $y_1, y_2 \in M(B(0,n))$, there are $x_1, x_2 \in B(0, n)$ with $y_1 = Mx_1$, $y_2 = Mx_2$; for every $0 \le \alpha \le 1$, $\alpha x_1 + (1 - \alpha) x_2 \in B(0, n)$, because a ball is convex, and
>
> $$
> M\bigl( \alpha x_1 + (1-\alpha) x_2 \bigr) = \alpha M x_1 + (1 - \alpha) M x_2 = \alpha y_1 + (1 - \alpha) y_2 \in M\bigl( B(0, n) \bigr) .
> $$
>
> *With the closure:* if $z_k \in M(B(0,n))$ and $z_k \to z$, then $-z_k \in M(B(0,n))$ and $-z_k \to -z$, so $-z \in \overline{M(B(0,n))}$. If $y_{1,k} \to y_1$ and $y_{2,k} \to y_2$ with $y_{i,k} \in M(B(0,n))$, then $\alpha y_{1,k} + (1-\alpha) y_{2,k} \in M(B(0,n))$ converges to $\alpha y_1 + (1-\alpha) y_2$, which therefore lies in $\overline{M(B(0,n))}$.
>
> **Step 3: a ball about the origin.** By symmetry, $B(-z_0, r) \subset \overline{M(B(0,n))}$ as well. (If $y \in B(-z_0, r)$ then $-y \in B(z_0, r)$, so $-y$, and hence $y$, lies in $\overline{M(B(0,n))}$.) By convexity, everything between the two balls is in $\overline{M(B(0,n))}$, and in particular
>
> $$
> B(0, r) \subset \overline{M\bigl( B(0, n) \bigr)} :
> $$
>
> for every $y \in B(0, r)$,
>
> $$
> y = \tfrac12 (z_0 + y) + \tfrac12 (-z_0 + y), \qquad z_0 + y \in B(z_0, r), \quad -z_0 + y \in B(-z_0, r),
> $$
>
> and convexity with $\alpha = \frac12$ gives $y \in \overline{M(B(0,n))}$.
>
> ![[m556-41-1.svg]]
>
> By symmetry the ball $B(z_0, r)$ has a mirror image $B(-z_0, r)$; by convexity the set contains the “capsule” joining them (thin lines), and so the ball $B(0, r)$ about the origin.
>
> **Step 4: rescaling.** We have shown: there are $r > 0$ and $n \in \mathbb{N}$ with $B(0, r) \subset \overline{M(B(0,n))}$. By linearity,
>
> $$
> B\bigl( 0, \tfrac{r}{n} \bigr) \subset \overline{M\bigl( B(0, 1) \bigr)} .
> $$
>
> (For $c > 0$, $B(0, c\rho) = c\, B(0, \rho)$ in both spaces, $M(c\, S) = c\, M(S)$, and $\overline{c\, S} = c\, \overline{S}$ since $z \mapsto cz$ is a homeomorphism; take $c = \frac1n$.) Let $\delta = \frac{r}{3n}$. Then $B(0, 3\delta) \subset \overline{M(B(0,1))}$, and, again by linearity,
>
> $$
> B(0, 3\rho\delta) \subset \overline{M\bigl( B(0, \rho) \bigr)} \qquad \text{for all } \rho > 0 . \tag{$\dagger$}
> $$
>
> **Step 5: removing the closure.** We want $B(0, \delta) \subset M(B(0, 1))$, without the closure. Shrinking the ball does not remove the closure by itself. Let $y_0 \in B(0, \delta)$. By $(\dagger)$ with $\rho = \frac13$, $B(0, \delta) \subset \overline{M(B(0, \frac13))}$, so there is $x_0 \in B_X(0, \frac13)$ with
>
> $$
> \|y_0 - Mx_0\| < \frac{\delta}{3}, \qquad \text{i.e.} \qquad y_0 - Mx_0 \in B_Y\bigl( 0, \tfrac{\delta}{3} \bigr) \subset \overline{M\bigl( B_X(0, \tfrac{1}{3^2}) \bigr)} ,
> $$
>
> the last inclusion by $(\dagger)$ with $\rho = \frac{1}{3^2}$. So there is $x_1 \in B_X(0, \frac{1}{3^2})$ with
>
> $$
> \|y_0 - Mx_0 - Mx_1\| < \frac{\delta}{3^2}, \qquad \text{i.e.} \qquad y_0 - Mx_0 - Mx_1 \in B_Y\bigl( 0, \tfrac{\delta}{3^2} \bigr) \subset \overline{M\bigl( B_X(0, \tfrac{1}{3^3}) \bigr)} .
> $$
>
> Then take $x_2 \in B_X(0, \frac{1}{3^3})$ with $\|y_0 - Mx_0 - Mx_1 - Mx_2\| < \frac{\delta}{3^3}$, and so on: each step corrects the previous error, and the errors form a geometric sequence. Inductively, we take $x_j \in B_X(0, \frac{1}{3^{j+1}})$ with
>
> $$
> \Bigl\| y_0 - \sum_{j=0}^n M x_j \Bigr\| < \frac{\delta}{3^{n+1}} \qquad \text{for every } n . \tag{$\ddagger$}
> $$
>
> (Given $x_0, \ldots, x_n$ with $(\ddagger)$, the vector $y_0 - \sum_{j=0}^n Mx_j$ lies in $B_Y(0, \frac{\delta}{3^{n+1}}) \subset \overline{M(B_X(0, \frac{1}{3^{n+2}}))}$ by $(\dagger)$ with $\rho = 3^{-(n+2)}$, which gives $x_{n+1} \in B_X(0, \frac{1}{3^{n+2}})$ with $(\ddagger)$ for $n + 1$.)
>
> **Step 6: the series converges.** We want $\sum_j x_j$ to converge to some $x^0 \in X$ with $\|x^0\| \le \frac12$ and $y_0 = Mx^0$. Since $\|x_j\| < 3^{-(j+1)}$,
>
> $$
> \sum_{j=0}^\infty \|x_j\| \le \sum_{j=0}^\infty \frac{1}{3^{j+1}} = \frac13 \cdot \frac{1}{1 - \frac13} = \frac12 ;
> $$
>
> a sum of non-negative terms always makes sense, as the limit of an increasing sequence. Hence the partial sums are Cauchy in $X$: for $n > m$,
>
> $$
> \Bigl\| \sum_{j=m+1}^n x_j \Bigr\| \le \sum_{j=m+1}^n \|x_j\| \to 0 \qquad (n, m \to \infty) ,
> $$
>
> the tail of a convergent series. $X$ is a Banach space, so there is $x^0 \in X$ with $\lim_{n \to \infty} \sum_{j=0}^n x_j = x^0$, and $\|x^0\| = \lim_n \bigl\| \sum_{j=0}^n x_j \bigr\| \le \frac12$ (continuity of the norm, Proposition [[§11 Normed Linear Spaces#^prop-11-4|§11.4]]). In particular $x^0 \in B(0, 1)$. Finally, by $(\ddagger)$ and the linearity of $M$, $\|y_0 - M(\sum_{j=0}^n x_j)\| < \delta/3^{n+1} \to 0$, and $M$ is continuous, so
>
> $$
> y_0 = \lim_{n \to \infty} M\Bigl( \sum_{j=0}^n x_j \Bigr) = M x^0 .
> $$
>
> Hence $y_0 \in M(B(0, 1))$. As $y_0 \in B(0, \delta)$ was arbitrary, $B(0, \delta) \subset M(B(0, 1))$.

^pf-41-1

*Uses:* [[§40 The Baire Category Theorem#^thm-40-4|§40.4]], [[§40 The Baire Category Theorem#^def-40-3|Def. §40.3]], [[§11 Normed Linear Spaces#^prop-11-4|§11.4]]

![[m556-41-2.svg]]

The successive approximation of Steps 5–6: $Mx_0$ approximates $y_0$ to within $\delta/3$, adding $Mx_1$ to within $\delta/3^2$, and so on; the corrections $x_j$ have $\|x_j\| < 3^{-(j+1)}$, so their sum $x^0$ exists in the Banach space $X$, has $\|x^0\| \le \frac12$, and $Mx^0 = y_0$.

![[m556-41-a1.gif|480]]

*(Not from lecture; animation added, vault only.)* Steps 5–6 for an onto $M$ of the plane (chosen for the picture), with corrections $x_j$ that are only approximately right at each step (error $\sim 3^{-j}$). Right: $Mx_0 + \cdots + Mx_j$ approaches $y_0$, the residual shrinking by about $1/3$ each time (dashed circles of radius $\sim 3^{-(j+1)}$). Left: the corrections, a third of the size each time, so their sum converges.

> [!theorem] Theorem §41.2: Open Mapping Theorem
> Let $X, Y$ be Banach spaces and $M : X \to Y$ a bounded linear map that is onto (surjective, $R(M) = Y$). Then $M$ is an [[§39 Solving Mx = y#^def-39-3|open map]]: for every open $O \subset X$, $M(O)$ is open in $Y$.
>
> *Lax: §15.5, Thm 10*

^thm-41-2

> [!proof]+ Proof of the open mapping theorem
> Assume Theorem [[§41 The Open Mapping Theorem and Its Consequences#^thm-41-1|§41.1]]. Let $O \subset X$ be open. We want $M(O) = \{ Mx : x \in O \}$ to be open, that is, for every $x_0 \in O$ there is $\delta' > 0$ with $B(Mx_0, \delta') \subset M(O)$ (every point of $M(O)$ is of the form $Mx_0$, $x_0 \in O$). Since $O$ is open, there is $r > 0$ with $B(x_0, r) \subset O$. With $\delta$ from Theorem [[§41 The Open Mapping Theorem and Its Consequences#^thm-41-1|§41.1]], we show
>
> $$
> B(Mx_0, r\delta) \subset M\bigl( B(x_0, r) \bigr) \ \bigl( \subset M(O) \bigr) .
> $$
>
> Let $y \in B(Mx_0, r\delta)$; we want $x \in B(x_0, r)$ with $y = Mx$. Now
>
> $$
> y \in B(Mx_0, r\delta) \iff \|y - Mx_0\| < r\delta \iff \Bigl\| \frac{y}{r} - \frac{Mx_0}{r} \Bigr\| < \delta ,
> $$
>
> so $\frac{y - Mx_0}{r} \in B(0, \delta)$. By Theorem [[§41 The Open Mapping Theorem and Its Consequences#^thm-41-1|§41.1]] there is $x_1 \in B(0, 1)$ with $\frac{y - Mx_0}{r} = Mx_1$. Then
>
> $$
> y = Mx_0 + r\, Mx_1 = M(x_0 + r x_1), \qquad x = x_0 + r x_1 \in B(x_0, r),
> $$
>
> since $\|x - x_0\| = r\|x_1\| < r$. This is just shifting and shrinking: only the linearity of $M$ is used.

^pf-41-2

*Uses:* [[§41 The Open Mapping Theorem and Its Consequences#^thm-41-1|§41.1]]

![[m556-41-3.svg]]

The open mapping theorem from Theorem [[§41 The Open Mapping Theorem and Its Consequences#^thm-41-1|§41.1]]: the map $x \mapsto x_0 + rx$ carries $B(0,1)$ onto $B(x_0, r) \subset O$, and correspondingly $y \mapsto Mx_0 + ry$ carries $B(0, \delta) \subset M(B(0,1))$ onto $B(Mx_0, r\delta) \subset M(B(x_0, r))$. Only linearity is used.

Banach's theorem (Theorem [[§39 Solving Mx = y#^thm-39-2|§39.2]]) follows at once.

> [!proof]+ Proof of Banach's theorem from the open mapping theorem
> Let $M : X \to Y$ be bounded, linear, one-to-one and onto, so that $M^{-1} : Y \to X$ exists; it is linear ([[§39 Solving Mx = y|§39]]). A linear map is bounded if and only if it is continuous (Proposition [[§30 Boundedness and Continuity#^prop-30-2|§30.2]]), and continuous if and only if the inverse image of every open set is open (Lemma [[§39 Solving Mx = y#^lem-39-3|§39.3]]). For $O \subset X$ open, the inverse image of $O$ under $M^{-1}$ is
>
> $$
> (M^{-1})^{-1}(O) = M(O) ,
> $$
>
> which is open by Theorem [[§41 The Open Mapping Theorem and Its Consequences#^thm-41-2|§41.2]]. So $M^{-1}$ is continuous, hence bounded.

^pf-39-2

*Uses:* [[§39 Solving Mx = y#^lem-39-3|§39.3]], [[§41 The Open Mapping Theorem and Its Consequences#^thm-41-2|§41.2]], [[§30 Boundedness and Continuity#^prop-30-2|§30.2]]

> [!remark] Remark: Where Completeness is Used
> Completeness of $Y$ is used once, in Step 1, through Baire: what is needed is only that $Y = R(M)$ is of the second category, and the assumption can be weakened accordingly. Completeness of $X$ is used in Step 6, to sum the corrections. The proof has two halves of different nature: Baire gives a ball in the *closure* of the image (Steps 1–4), and successive approximation removes the closure (Steps 5–6).

^rem-41-1

## Equivalent Norms

> [!theorem] Theorem §41.3: Equivalent Norm Theorem
> Let $X$ be a linear space with two norms $\|\cdot\|_1$, $\|\cdot\|_2$ such that $(X, \|\cdot\|_1)$ and $(X, \|\cdot\|_2)$ are both Banach spaces. Assume there is $c > 0$ with
>
> $$
> \|x\|_1 \le c\, \|x\|_2 \qquad \text{for all } x \in X .
> $$
>
> Then $\|\cdot\|_1$ and $\|\cdot\|_2$ are equivalent (Definition [[§14 New Normed Spaces from Old#^def-14-1|§14.1]]).
>
> *Lax: §15.5, Thm 13 (for two compatible complete norms, proved there from the closed graph theorem)*

^thm-41-3

> [!proof]+ Proof
> Let $i : X \to X$, $i(x) = x$, be the identity. As a map $i : (X, \|\cdot\|_2) \to (X, \|\cdot\|_1)$ it is linear, and bounded by the assumption: $\|i(x)\|_1 \le c\, \|x\|_2$. It is one-to-one and onto, and both spaces are complete. By Banach's theorem (Theorem [[§39 Solving Mx = y#^thm-39-2|§39.2]]), $i^{-1} : (X, \|\cdot\|_1) \to (X, \|\cdot\|_2)$ is also bounded: there is $C$ with $\|x\|_2 \le C\, \|x\|_1$ for all $x$. With the assumption, the norms are equivalent.

^pf-41-3

*Uses:* [[§30 Boundedness and Continuity#^prop-30-2|§30.2]], [[§39 Solving Mx = y#^thm-39-2|§39.2]]

In other words, if both norms are complete and one of them is stronger than the other, then they are equivalent: two complete norms cannot be strictly comparable. (Compare Theorem [[§14 New Normed Spaces from Old#^thm-14-4|§14.4]]: in finite dimensions all norms are equivalent, with no assumption. Lax states the theorem for two complete norms that are *compatible*, that is, a sequence converging in both norms has the same limit in both; comparability implies compatibility. He proves it from the closed graph theorem, the reverse of the order here.)

> [!example] Example §41.1: $C^1[a,b]$ is Not Complete in the Maximum Norm
> $C^1[a,b]$ is complete in the norm $\|f\|_{C^1} = \max |f| + \max |f'|$ (Part 2 of the proof of Proposition [[§13 The Completion of a Normed Space#^prop-13-5|§13.5]]), and $\max |f| \le \|f\|_{C^1}$. If $C^1[a,b]$ were also complete in $\max|f|$, Theorem [[§41 The Open Mapping Theorem and Its Consequences#^thm-41-3|§41.3]] would make the two norms equivalent.
> They are not: $f_n(t) = \sin\bigl( n(t - a) \bigr)$ has $\max |f_n| \le 1$ but $\|f_n\|_{C^1} \ge |f_n'(a)| = n$. So $(C^1[a,b], \max|\cdot|)$ is not complete; its completion is $C[a,b]$ (Midterm Problem 1, [[§39 Solving Mx = y|§39]]).

^ex-41-1

> [!example] Example §41.2: $C[0,1]$ is Not Complete in the $L^1$ Norm
> $(C[0,1], \|\cdot\|_1)$, where $\|f\|_1 = \int_0^1 |f(x)|\, dx$, is not a Banach space.
>
> *Source: HW9, Problem 2*

^ex-41-2

> [!proof]+ Proof
> *(HW9, Problem 2. Not from lecture; filled in.)* Let $\|f\|_\infty = \max_{t \in [0,1]} |f(t)|$. We compare the two norms on $X = C[0,1]$ and apply the equivalent norm theorem (Theorem [[§41 The Open Mapping Theorem and Its Consequences#^thm-41-3|§41.3]]).
>
> **Step 1: the norms are comparable.** For $f \in C[0,1]$, $|f(x)| \le \|f\|_\infty$ for all $x$, so
>
> $$
> \|f\|_1 = \int_0^1 |f(x)|\, dx \le \|f\|_\infty .
> $$
>
> **Step 2: they are not equivalent.** Let $f_n(t) = t^n$. Then $\|f_n\|_\infty = 1$ and $\|f_n\|_1 = \int_0^1 t^n\, dt = \frac{1}{n+1}$. If there were $C$ with $\|f\|_\infty \le C \|f\|_1$ for all $f$, then $1 \le \frac{C}{n+1}$ for every $n$, which is impossible. So the two norms are not equivalent (Definition [[§14 New Normed Spaces from Old#^def-14-1|§14.1]]).
>
> **Step 3: conclusion.** $(C[0,1], \|\cdot\|_\infty)$ is a Banach space (Theorem [[§12 Completeness#^thm-12-1|§12.1]]). If $(C[0,1], \|\cdot\|_1)$ were also a Banach space, then by Step 1 the hypotheses of Theorem [[§41 The Open Mapping Theorem and Its Consequences#^thm-41-3|§41.3]] would hold with $c = 1$, and the two norms would be equivalent, contradicting Step 2. So $(C[0,1], \|\cdot\|_1)$ is not complete. (Its completion is $L^1[0,1]$, Proposition [[§19 The Function Spaces Lᵖ(Ω)#^prop-19-8|§19.8]].)

^pf-ex-41-2

*Uses:* [[§41 The Open Mapping Theorem and Its Consequences#^thm-41-3|§41.3]], [[§14 New Normed Spaces from Old#^def-14-1|Def. §14.1]], [[§12 Completeness#^thm-12-1|§12.1]], [[§19 The Function Spaces Lᵖ(Ω)#^prop-19-8|§19.8]]

## The Closed Graph Theorem

> [!theorem] Theorem §41.4: Closed Graph Theorem
> Let $X, Y$ be Banach spaces and $D(M) \subset X$. Assume $M : D(M) \to Y$ is a [[§39 Solving Mx = y#^def-39-5|closed (linear) map]]. If $D(M) = X$, then $M \in \mathcal{L}(X, Y)$.
>
> *Lax: §15.5, Thm 12*

^thm-41-4

> [!proof]+ Proof
> Let $X$ carry its norm $\|\cdot\|_X$. Recall (Definition [[§39 Solving Mx = y#^def-39-6|§39.6]]) that the graph norm of $M$ on $D(M) = X$ is
>
> $$
> \|x\|_G = \|x\|_X + \|Mx\|_Y , \qquad x \in X .
> $$
>
> *It is a norm.* Homogeneity: $\|ax\|_G = |a|\,\|x\|_X + \|aMx\|_Y = |a|\,\|x\|_G$, by linearity of $M$. Triangle inequality: $\|x + x'\|_X \le \|x\|_X + \|x'\|_X$ and $\|M(x + x')\|_Y = \|Mx + Mx'\|_Y \le \|Mx\|_Y + \|Mx'\|_Y$; add. Positivity: $\|x\|_G \ge \|x\|_X$, which is $> 0$ for $x \neq 0$. We also have
>
> $$
> \|x\|_X \le \|x\|_G \qquad \text{for all } x \in X .
> $$
>
> *$(X, \|\cdot\|_G)$ is complete.* Let $\{x_n\}_{n \in \mathbb{N}}$ be a Cauchy sequence in $(X, \|\cdot\|_G)$: for every $\varepsilon > 0$ there is $N$ such that
>
> $$
> \|x_n - x_m\|_X + \|Mx_n - Mx_m\|_Y < \varepsilon \qquad \text{for all } n, m > N .
> $$
>
> Ignoring one term at a time, $\{x_n\}$ is Cauchy in $(X, \|\cdot\|_X)$ and $\{Mx_n\}$ is Cauchy in $(Y, \|\cdot\|_Y)$. Both are Banach spaces, so there are $x_0 \in X$ and $y_0 \in Y$ with $x_n \to x_0$ in $X$ and $Mx_n \to y_0$ in $Y$; that is, $(x_n, Mx_n) \to (x_0, y_0)$ in $X \times Y$. Since $M$ is closed (and $x_0 \in X = D(M)$), $y_0 = Mx_0$. Now let $m \to \infty$ in the Cauchy inequality: by continuity of the norms,
>
> $$
> \|x_n - x_0\|_X + \|Mx_n - Mx_0\|_Y \le \varepsilon \qquad \text{for all } n > N ,
> $$
>
> i.e. $x_n \to x_0$ in $\|\cdot\|_G$. So $(X, \|\cdot\|_G)$ is a Banach space.
>
> *Conclusion.* Both $(X, \|\cdot\|_X)$ and $(X, \|\cdot\|_G)$ are complete and $\|x\|_X \le \|x\|_G$, so by the equivalent norm theorem (Theorem [[§41 The Open Mapping Theorem and Its Consequences#^thm-41-3|§41.3]]) there is $C > 0$ with $\|x\|_G \le C\, \|x\|_X$ for all $x \in X$. Hence
>
> $$
> \|Mx\|_Y = \|x\|_G - \|x\|_X \le (C - 1)\, \|x\|_X \qquad \text{for all } x \in X ,
> $$
>
> and $M \in \mathcal{L}(X, Y)$.

^pf-41-4

*Uses:* [[§39 Solving Mx = y#^def-39-6|Def. §39.6]], [[§41 The Open Mapping Theorem and Its Consequences#^thm-41-3|§41.3]]

The domain $D(M)$ is the domain of definition of $M$. In Example [[§39 Solving Mx = y#^ex-39-3|§39.3]], $M = \frac{d}{dt} : C^1[0,1] \to C[0,1]$, inside $X = Y = C[0,1]$, with $D(\frac{d}{dt}) = C^1[0,1]$, is closed but not bounded; this does not contradict the theorem, because its domain is not the whole space $C[0,1]$. So a closed map that is not bounded necessarily has a domain smaller than $X$.

The closed graph theorem and the open mapping principle together decide when a range is closed.

> [!theorem] Proposition §41.5: Closed Range Criterion
> Let $X, Y$ be Banach spaces and $M : X \to Y$ a closed linear map (defined on all of $X$). For $x \in X$ let
>
> $$
> d\bigl( x, N(M) \bigr) = \inf_{w \in N(M)} \|x - w\|
> $$
>
> be the distance from $x$ to the null space $N(M)$. Then the range $R(M)$ is closed in $Y$ if and only if there is a constant $a > 0$ such that
>
> $$
> d\bigl( x, N(M) \bigr) \le a\, \|Mx\| \qquad \text{for all } x \in X .
> $$
>
> *Source: HW9, Problem 3*

^prop-41-5

> [!proof]+ Proof
> *(HW9, Problem 3. Not from lecture; filled in.)* Write $N = N(M)$ and $R = R(M)$ (Definitions [[§39 Solving Mx = y#^def-39-2|§39.2]] and [[§39 Solving Mx = y#^def-39-1|§39.1]]). By the closed graph theorem (Theorem [[§41 The Open Mapping Theorem and Its Consequences#^thm-41-4|§41.4]]), $M \in \mathcal{L}(X, Y)$.
>
> **($\Rightarrow$)** Assume $R$ is closed in $Y$. We must produce $a$.
>
> *Step 1: $R$ is a Banach space.* $R$ is a linear subspace of $Y$. A Cauchy sequence in $R$ converges in $Y$, because $Y$ is complete, and its limit lies in $R$, because $R$ is closed. So $R$ is complete in the norm of $Y$.
>
> *Step 2: a ball in the image.* $M : X \to R$ is a bounded linear map between Banach spaces and it is onto $R$. By Theorem [[§41 The Open Mapping Theorem and Its Consequences#^thm-41-1|§41.1]], applied with $R$ in place of $Y$, there is $\delta > 0$ such that every $y \in R$ with $\|y\| < \delta$ is $y = Mz$ for some $z \in X$ with $\|z\| < 1$.
>
> *Step 3: the estimate.* Let $x \in X$. If $Mx = 0$, then $x \in N$ and $d(x, N) = 0$. If $Mx \neq 0$, put $y = \frac{\delta}{2} \frac{Mx}{\|Mx\|}$. Then $y \in R$ and $\|y\| = \frac{\delta}{2} < \delta$, so by Step 2 there is $z$ with $Mz = y$ and $\|z\| < 1$. Put $w = x - \frac{2\|Mx\|}{\delta}\, z$. By linearity,
>
> $$
> Mw = Mx - \frac{2\|Mx\|}{\delta}\, Mz = Mx - \frac{2\|Mx\|}{\delta} \cdot \frac{\delta}{2} \frac{Mx}{\|Mx\|} = 0 ,
> $$
>
> so $w \in N$, and
>
> $$
> d(x, N) \le \|x - w\| = \frac{2\|Mx\|}{\delta}\, \|z\| \le \frac{2}{\delta}\, \|Mx\| .
> $$
>
> So the inequality holds with $a = 2/\delta$.
>
> **($\Leftarrow$)** Assume $d(x, N) \le a \|Mx\|$ for all $x \in X$. Let $y \in Y$ be the limit of a sequence $Mx_n$ of points of $R$; we must show $y \in R$. The $x_n$ themselves need not converge, since they are determined only up to elements of $N$; we correct them by elements of $N$.
>
> *Step 1: a fast subsequence.* $\{Mx_n\}$ converges, so it is Cauchy, and there are $n_1 < n_2 < \cdots$ with $\|Mx_{n_{k+1}} - Mx_{n_k}\| < 2^{-k}$ for all $k \ge 1$.
>
> *Step 2: corrections.* By the assumption applied to $x_{n_{k+1}} - x_{n_k}$,
>
> $$
> d\bigl( x_{n_{k+1}} - x_{n_k}, N \bigr) \le a\, \|Mx_{n_{k+1}} - Mx_{n_k}\| < a\, 2^{-k} .
> $$
>
> The distance is an infimum, so there is $w_k \in N$ with $\|x_{n_{k+1}} - x_{n_k} - w_k\| < a\, 2^{-k}$. Define
>
> $$
> z_1 = x_{n_1}, \qquad z_{k+1} = x_{n_{k+1}} - (w_1 + \cdots + w_k) .
> $$
>
> Then $z_{k+1} - z_k = x_{n_{k+1}} - x_{n_k} - w_k$, so $\|z_{k+1} - z_k\| < a\, 2^{-k}$, and $Mz_k = Mx_{n_k}$ because $M$ vanishes on $N$.
>
> *Step 3: convergence.* For $l > k$, by the triangle inequality,
>
> $$
> \|z_l - z_k\| \le \sum_{j=k}^{l-1} \|z_{j+1} - z_j\| < \sum_{j=k}^{\infty} a\, 2^{-j} = a\, 2^{1-k} ,
> $$
>
> so $\{z_k\}$ is Cauchy in $X$. Since $X$ is complete, $z_k \to z$ for some $z \in X$. Also $Mz_k = Mx_{n_k} \to y$, as a subsequence of $Mx_n \to y$.
>
> *Step 4: $y \in R$.* $z_k \to z$ and $Mz_k \to y$, and $M$ is closed (Definition [[§39 Solving Mx = y#^def-39-5|§39.5]]), so $y = Mz \in R$. Hence $R$ contains the limit of every convergent sequence of its points: $R$ is closed.

^pf-41-5

*Uses:* [[§39 Solving Mx = y#^def-39-2|Def. §39.2]], [[§39 Solving Mx = y#^def-39-1|Def. §39.1]], [[§41 The Open Mapping Theorem and Its Consequences#^thm-41-4|§41.4]], [[§41 The Open Mapping Theorem and Its Consequences#^thm-41-1|§41.1]], [[§39 Solving Mx = y#^def-39-5|Def. §39.5]]

> [!remark] Remark: What Each Direction of the Closed Range Criterion Uses
> *(Not from lecture.)* The direction ($\Leftarrow$) uses only that $M$ is closed and $X$ is complete: $Y$ may be any normed linear space, and the same argument works for a closed map with domain $D(M) \subset X$, since then $z_k \in D(M)$ and closedness gives $z \in D(M)$. The direction ($\Rightarrow$) uses the completeness of both spaces, through the open mapping principle. In terms of the induced map of Theorem [[§39 Solving Mx = y#^thm-39-1|§39.1]], the inequality says $\|[x]\| \le a\, \|M_0 [x]\|$: the inverse of $M_0 : X/N \to R(M)$ is bounded.

^rem-41-2

> [!remark] Remark: How the Theorems Fit Together
> The chain of this section is: the Baire category theorem (Theorem [[§40 The Baire Category Theorem#^thm-40-4|§40.4]]) $\Rightarrow$ the image of the unit ball contains a ball (Theorem [[§41 The Open Mapping Theorem and Its Consequences#^thm-41-1|§41.1]]) $\Rightarrow$ the open mapping theorem (Theorem [[§41 The Open Mapping Theorem and Its Consequences#^thm-41-2|§41.2]]) $\Rightarrow$ Banach's inverse mapping theorem (Theorem [[§39 Solving Mx = y#^thm-39-2|§39.2]]) $\Rightarrow$ the equivalent norm theorem (Theorem [[§41 The Open Mapping Theorem and Its Consequences#^thm-41-3|§41.3]]) $\Rightarrow$ the closed graph theorem (Theorem [[§41 The Open Mapping Theorem and Its Consequences#^thm-41-4|§41.4]]).
> The closed graph theorem is used in the converse direction of the usual check: to show a linear map defined everywhere is bounded, it suffices to show that $x_n \to x$ and $Mx_n \to y$ imply $y = Mx$, which is often easier than estimating $\|Mx\|$ directly, because the convergence $Mx_n \to y$ comes for free. Completeness of both spaces is essential in every link.

^rem-41-3
