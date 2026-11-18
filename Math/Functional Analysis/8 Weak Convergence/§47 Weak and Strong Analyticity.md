---
type: section
subject: "[[Functional Analysis]]"
chapter: 8
section: 47
tags: [functional-analysis, math556]
---
← [[§46 The Transpose]] · ↑ [[· 8 Weak Convergence]] · [[§48 The Resolvent and the Spectrum]] →

*Stage: maps — Thread: functionals. A Banach-space-valued function of a complex variable is analytic as soon as every bounded linear functional of it is (Dunford): Cauchy's integral formula for each functional, then the uniform boundedness principle.*

*Lecture 21 (Tue Nov 17), first part. Source: the handwritten notes of the lecture; there is no recording. The steps that the notes leave out, and the items marked as such, are filled in. The section was checked against Lax §11.4.*

The next section studies $(\lambda I - M)^{-1}$ as a function of the complex number $\lambda$; its values are bounded linear maps, elements of the Banach space $\mathcal{L}(X, X)$. To use complex analysis for such a function one has to say what “analytic” means when the values lie in a Banach space. As for convergence ([[§43 Weak and Weak-Star Convergence|§43]]), there are two candidates: one uses the norm, the other tests with bounded linear functionals. For convergence the two notions differ. For analyticity they agree, and this is the theorem of this section.

## Analytic Functions with Values in a Banach Space

Let $D \subset \mathbb{C}$ be an open set. Recall that a function $f : D \to \mathbb{C}$ is **analytic** on $D$ if the limit

$$
\lim_{z \to z_0} \frac{f(z) - f(z_0)}{z - z_0}
$$

exists at every $z_0 \in D$.

> [!definition] Definition §47.1: Strongly Analytic Function
> Let $D \subset \mathbb{C}$ be open, let $X$ be a Banach space over $\mathbb{C}$, and let $f : D \to X$ be a Banach-space-valued function. $f$ is **analytic** on $D$, or **strongly analytic** on $D$, if for every fixed $z_0 \in D$ the limit
>
> $$
> \lim_{h \to 0} \frac{f(z_0 + h) - f(z_0)}{h} \qquad (h \in \mathbb{C},\ h \neq 0)
> $$
>
> exists in $X$; that is, there is $g(z_0) \in X$ such that
>
> $$
> \lim_{h \to 0} \Bigl\| \frac{f(z_0 + h) - f(z_0)}{h} - g(z_0) \Bigr\| = 0 .
> $$
>
> The vector $g(z_0)$ is the **derivative** of $f$ at $z_0$, also written $f'(z_0)$.
>
> *Lax: §11.4, first definition*

^def-47-1

> [!remark]- Connections
> - The scalar case: [[§25 Analytic Functions#^def-25-1|analytic function]], [[§19 Derivatives#^def-19-1|derivative]] (Complex Variables).
> - The same two-way test for sequences: strong and weak convergence, [[§43 Weak and Weak-Star Convergence#^def-43-1|Def. §43.1]].

> [!definition] Definition §47.2: Weakly Analytic Function
> Let $D \subset \mathbb{C}$ be open, let $X$ be a Banach space over $\mathbb{C}$, and let $f : D \to X$ be given. For every $\ell \in X' = \mathcal{L}(X, \mathbb{C})$ the composition $z \mapsto \ell(f(z))$ is a function from $D$ to $\mathbb{C}$. $f$ is **weakly analytic** on $D$ if for every $\ell \in X'$ the function $\ell(f(z))$ is analytic on $D$.
>
> *Lax: §11.4, second definition*

^def-47-2

> [!remark] Remark: Strong and Weak as for Convergence
> The two definitions stand to each other as strong and weak convergence do (Definition [[§43 Weak and Weak-Star Convergence#^def-43-1|§43.1]]): the strong notion asks the difference quotients to converge in the norm of $X$, the weak notion only asks the numbers $\ell\bigl( \frac{f(z_0 + h) - f(z_0)}{h} \bigr)$ to converge, for each $\ell$ separately, and it does not ask the limits to come from one vector of $X$. For sequences the weak notion is strictly weaker in infinite dimensions (Example [[§43 Weak and Weak-Star Convergence#^ex-43-1|§43.1]]). For analyticity there is no gap (Theorem [[§47 Weak and Strong Analyticity#^thm-47-3|§47.3]]); Lax calls this a surprising result.

^rem-47-1

> [!example] Example §47.1: A Power Series with Values in $\ell^2$
> *(Not from lecture; filled in.)* Let $D = \{ z \in \mathbb{C} : |z| < 1 \}$, $X = \ell^2$ over $\mathbb{C}$ with entries numbered from $0$, and
>
> $$
> f(z) = (1, z, z^2, z^3, \ldots) , \qquad \text{that is,} \quad f(z)_n = z^n \quad (n = 0, 1, 2, \ldots) .
> $$
>
> 1. *$f(z) \in \ell^2$ for $|z| < 1$:* $\sum_{n=0}^\infty |z^n|^2 = \frac{1}{1 - |z|^2} < \infty$ (geometric series).
> 2. *$f$ is weakly analytic on $D$.* By the Riesz representation theorem (Theorem [[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^thm-26-5|§26.5]](2)), every $\ell \in (\ell^2)'$ is $\ell(x) = (x, b) = \sum_{n=0}^\infty x_n \overline{b_n}$ for some $b \in \ell^2$. Hence
>
> $$
> \ell(f(z)) = \sum_{n=0}^\infty \overline{b_n}\, z^n .
> $$
>
> Since $|b_n| \le \|b\|$ for all $n$, this power series converges for $|z| < 1$ (comparison with the geometric series), and [[§71★ Integration and Differentiation of Power Series#^cor-71-2|a power series is analytic inside its circle of convergence]]. So $\ell(f(z))$ is analytic on $D$ for every $\ell$.
> 3. *$f$ is strongly analytic on $D$, with $f'(z) = g(z) = (0, 1, 2z, 3z^2, \ldots)$, $g(z)_n = n z^{n-1}$.* Fix $z \in D$ and choose $r$ with $|z| < r < 1$. First, $g(z) \in \ell^2$, since $\sum_n n^2 |z|^{2(n-1)} < \infty$ by the ratio test. Let $0 < |h| < r - |z|$. For $n = 0$ and $n = 1$ the $n$-th entry of $\frac{f(z + h) - f(z)}{h} - g(z)$ is $0$. For $n \ge 2$, by the binomial theorem,
>
> $$
> (z + h)^n - z^n - n z^{n-1} h = \sum_{j=2}^n \binom{n}{j} z^{n-j} h^j ,
> $$
>
> and for $2 \le j \le n$ the binomial coefficients satisfy
>
> $$
> \binom{n}{j} = \frac{n(n-1)}{j(j-1)} \binom{n-2}{j-2} \le \frac{n(n-1)}{2} \binom{n-2}{j-2} .
> $$
>
> Dividing by $h$ and using the binomial theorem again, now for $(|z| + |h|)^{n-2}$,
>
> $$
> \begin{aligned}\Bigl| \frac{(z + h)^n - z^n}{h} - n z^{n-1} \Bigr| &\le \frac{n(n-1)}{2}\, |h| \sum_{j=2}^n \binom{n-2}{j-2} |z|^{n-j} |h|^{j-2} \\
> &= \frac{n(n-1)}{2}\, |h|\, (|z| + |h|)^{n-2} \le \frac{n(n-1)}{2}\, r^{n-2}\, |h| .\end{aligned}
> $$
>
> Squaring and summing over $n$,
>
> $$
> \Bigl\| \frac{f(z + h) - f(z)}{h} - g(z) \Bigr\|^2 \le |h|^2 \sum_{n=2}^\infty \frac{n^2 (n-1)^2}{4}\, r^{2(n-2)} = C_r^2\, |h|^2 ,
> $$
>
> where the series converges by the ratio test, since $r < 1$. Hence the difference quotients converge to $g(z)$ in the norm of $\ell^2$ as $h \to 0$.
>
> The weak check (2) takes two lines, because it only uses the theory of scalar power series; the strong check (3) needs an estimate that is uniform in the entries. Dunford's theorem (Theorem [[§47 Weak and Strong Analyticity#^thm-47-3|§47.3]]) says that (2) alone already gives (3).

^ex-47-1

> [!remark]- Connections
> - Weak and strong convergence do differ in $\ell^2$: [[§43 Weak and Weak-Star Convergence#^ex-43-1|Ex. §43.1]] ($e_n \rightharpoonup 0$).
> - Scalar power series: [[§71★ Integration and Differentiation of Power Series]] (Complex Variables).

## Strong Analyticity Implies Weak Analyticity

> [!theorem] Proposition §47.1: Strongly Analytic Functions are Weakly Analytic
> Let $D \subset \mathbb{C}$ be open, $X$ a Banach space over $\mathbb{C}$, and $f : D \to X$ strongly analytic on $D$ (Definition [[§47 Weak and Strong Analyticity#^def-47-1|§47.1]]). Then $f$ is weakly analytic on $D$ (Definition [[§47 Weak and Strong Analyticity#^def-47-2|§47.2]]), and for every $\ell \in X'$ and every $z_0 \in D$ the derivative of the scalar function $\ell(f(z))$ at $z_0$ is $\ell(f'(z_0))$.

^prop-47-1

> [!proof]+ Proof
> Let $\ell \in X'$ and $z_0 \in D$, and let $g(z_0) = f'(z_0)$ be the limit in Definition [[§47 Weak and Strong Analyticity#^def-47-1|§47.1]]. Since $\ell$ is linear,
>
> $$
> \frac{\ell(f(z_0 + h)) - \ell(f(z_0))}{h} = \ell\Bigl( \frac{f(z_0 + h) - f(z_0)}{h} \Bigr) .
> $$
>
> Since $\ell \in X'$ is continuous (Proposition [[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^prop-26-2|§26.2]]) and the argument on the right converges to $g(z_0)$ in $X$ as $h \to 0$, the right side converges to $\ell(g(z_0))$. Explicitly, $\bigl| \ell\bigl( \frac{f(z_0 + h) - f(z_0)}{h} \bigr) - \ell(g(z_0)) \bigr| \le \|\ell\|\, \bigl\| \frac{f(z_0 + h) - f(z_0)}{h} - g(z_0) \bigr\| \to 0$. So the limit defining the derivative of $\ell(f(z))$ at $z_0$ exists and equals $\ell(g(z_0))$. As $z_0 \in D$ and $\ell \in X'$ were arbitrary, $f$ is weakly analytic.

^pf-47-1

*Uses:* [[§47 Weak and Strong Analyticity#^def-47-1|Def. §47.1]], [[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^prop-26-2|§26.2]]

## Dunford's Theorem

The proof of the converse uses three facts about an analytic function $\varphi : D \to \mathbb{C}$ on an open set $D \subset \mathbb{C}$; they are theorems of complex analysis and are not proved in this course.

1. *Continuity.* $\varphi$ is continuous on $D$ ([[§19 Derivatives#^thm-19-1|differentiable implies continuous]]).
2. *[[Cauchy Integral Formula|Cauchy's integral formula]].* If the closed disk $\overline{B(z_0, r_0)} = \{ z : |z - z_0| \le r_0 \}$ lies in $D$ and $C = \{ \zeta : |\zeta - z_0| = r_0 \}$ is its boundary circle, traversed counterclockwise, then

$$
\varphi(z) = \frac{1}{2\pi i} \oint_C \frac{\varphi(\zeta)}{\zeta - z}\, d\zeta \qquad \text{for every } z \text{ with } |z - z_0| < r_0 .
$$

3. *The bound for a contour integral* (the [[ML-Inequality|ML-inequality]]). If $F$ is continuous on $C$ and $L$ is the length of $C$, then $\bigl| \oint_C F(\zeta)\, d\zeta \bigr| \le L\, \max_{\zeta \in C} |F(\zeta)|$. The circle $C$ of radius $r_0$ has length $L = 2\pi r_0$.

The proof also uses that a family of vectors whose mutual distances become small has a limit, in the following form.

> [!theorem] Lemma §47.2: A Cauchy Criterion for Limits as $h \to 0$
> *(Not from lecture; filled in.)* Let $X$ be a Banach space, $r > 0$, and let $q_h \in X$ be given for every $h \in \mathbb{C}$ with $0 < |h| < r$. Assume that for every $\varepsilon > 0$ there is $\delta \in (0, r]$ such that
>
> $$
> \|q_h - q_k\| < \varepsilon \qquad \text{whenever } 0 < |h| < \delta \text{ and } 0 < |k| < \delta .
> $$
>
> Then there is $g \in X$ with $\lim_{h \to 0} q_h = g$, that is, $\|q_h - g\| \to 0$ as $h \to 0$.

^lem-47-2

> [!proof]+ Proof
> Let $h_n = \frac{r}{n+1}$, so that $0 < h_n < r$ and $h_n \to 0$. *The sequence $\{q_{h_n}\}$ is Cauchy:* given $\varepsilon > 0$, take $\delta$ as in the assumption and $N$ with $h_n < \delta$ for all $n > N$; then $\|q_{h_n} - q_{h_m}\| < \varepsilon$ for all $n, m > N$. Since $X$ is complete, there is $g \in X$ with $q_{h_n} \to g$.
>
> *The whole family converges to $g$:* let $\varepsilon > 0$ and take $\delta$ as in the assumption. Choose $n$ so large that $h_n < \delta$ and $\|q_{h_n} - g\| < \varepsilon$. Then for every $h$ with $0 < |h| < \delta$,
>
> $$
> \|q_h - g\| \le \|q_h - q_{h_n}\| + \|q_{h_n} - g\| < 2\varepsilon .
> $$

^pf-47-2

> [!theorem] Theorem §47.3: Dunford's Theorem
> Let $D \subset \mathbb{C}$ be open and $X$ a Banach space over $\mathbb{C}$. If $f : D \to X$ is weakly analytic on $D$, then $f$ is strongly analytic on $D$. Together with Proposition [[§47 Weak and Strong Analyticity#^prop-47-1|§47.1]]: weak and strong analyticity are equivalent.
>
> *Lax: §11.4, Thm 4*

^thm-47-3

> [!proof]+ Proof
> Assume $f : D \to X$ is weakly analytic on $D$, and fix $z_0 \in D$. Since $D$ is open, there is $r_0 > 0$ such that $\overline{B(z_0, r_0)} \subset D$. For $h \in \mathbb{C}$ with $0 < |h| < r_0$ write
>
> $$
> q_h = \frac{f(z_0 + h) - f(z_0)}{h} \in X
> $$
>
> for the difference quotient. *What has to be shown:* the family $\{q_h\}$ is Cauchy as $h \to 0$, that is, for every $\varepsilon > 0$ there is $\delta > 0$ such that for all $h, k$ with $0 < |h| < \delta$ and $0 < |k| < \delta$,
>
> $$
> \|q_h - q_k\| = \Bigl\| \frac{f(z_0 + h) - f(z_0)}{h} - \frac{f(z_0 + k) - f(z_0)}{k} \Bigr\| < \varepsilon .
> $$
>
> Then Lemma [[§47 Weak and Strong Analyticity#^lem-47-2|§47.2]] gives the limit $\lim_{h \to 0} q_h$ in $X$, which is what Definition [[§47 Weak and Strong Analyticity#^def-47-1|§47.1]] asks for at $z_0$.
>
> **Step 1: Cauchy's integral formula for $\ell(f)$.** Let $\ell \in X' = \mathcal{L}(X, \mathbb{C})$ be given. By assumption $\ell(f(z))$ is analytic on $D$. Let $C = \{ \zeta : |\zeta - z_0| = r_0 \}$, traversed counterclockwise. By Cauchy's integral formula (fact (2) above), for every $z \in B(z_0, r_0) = \{ |z - z_0| < r_0 \}$,
>
> $$
> \ell(f(z)) = \frac{1}{2\pi i} \oint_C \frac{\ell(f(\zeta))}{\zeta - z}\, d\zeta .
> $$
>
> Let $|h| < \frac{r_0}{2}$ and $|k| < \frac{r_0}{2}$. Then $z_0 + h$, $z_0 + k$ and $z_0$ all lie in $B(z_0, r_0)$, so
>
> $$
> \ell(f(z_0 + h)) = \frac{1}{2\pi i} \oint_C \frac{\ell(f(\zeta))}{\zeta - (z_0 + h)}\, d\zeta , \qquad \ell(f(z_0)) = \frac{1}{2\pi i} \oint_C \frac{\ell(f(\zeta))}{\zeta - z_0}\, d\zeta ,
> $$
>
> and likewise with $k$ in place of $h$.
>
> ![[m556-47-1.svg]]
>
> The circle $C$ of radius $r_0$ around $z_0$, with its inside, lies in $D$.
>
> **Step 2: the difference quotients.** Let $0 < |h| < \frac{r_0}{2}$. By the linearity of $\ell$ and Step 1,
>
> $$
> \begin{aligned}\ell(q_h) = \frac1h \bigl( \ell(f(z_0 + h)) - \ell(f(z_0)) \bigr) &= \frac{1}{2\pi i} \oint_C \frac{\ell(f(\zeta))}{h} \Bigl( \frac{1}{\zeta - z_0 - h} - \frac{1}{\zeta - z_0} \Bigr) d\zeta \\
> &= \frac{1}{2\pi i} \oint_C \frac{\ell(f(\zeta))}{h} \cdot \frac{h}{(\zeta - z_0 - h)(\zeta - z_0)}\, d\zeta \\
> &= \frac{1}{2\pi i} \oint_C \frac{\ell(f(\zeta))}{(\zeta - z_0 - h)(\zeta - z_0)}\, d\zeta .\end{aligned}
> $$
>
> The same holds with $k$ in place of $h$, for $0 < |k| < \frac{r_0}{2}$. Subtracting,
>
> $$
> \begin{aligned}\ell(q_h - q_k) &= \frac{1}{2\pi i} \oint_C \ell(f(\zeta)) \Bigl( \frac{1}{(\zeta - z_0 - h)(\zeta - z_0)} - \frac{1}{(\zeta - z_0 - k)(\zeta - z_0)} \Bigr) d\zeta \\
> &= \frac{1}{2\pi i} \oint_C \ell(f(\zeta))\, \frac{h - k}{(\zeta - z_0 - h)(\zeta - z_0)(\zeta - z_0 - k)}\, d\zeta .\end{aligned}
> $$
>
> (With $a = \zeta - z_0$: $\frac{1}{a - h} - \frac{1}{a - k} = \frac{(a - k) - (a - h)}{(a - h)(a - k)} = \frac{h - k}{(a - h)(a - k)}$.)
>
> **Step 3: a bound for each $\ell$.** For $0 < |h| < \frac{r_0}{2}$, $0 < |k| < \frac{r_0}{2}$ and $h \neq k$ put
>
> $$
> x_{h,k} = \frac{1}{h - k}\, (q_h - q_k) = \frac{1}{h - k} \Bigl( \frac{f(z_0 + h) - f(z_0)}{h} - \frac{f(z_0 + k) - f(z_0)}{k} \Bigr) \in X .
> $$
>
> Dividing the last formula of Step 2 by $h - k$,
>
> $$
> \ell(x_{h,k}) = \frac{1}{2\pi i} \oint_C \frac{\ell(f(\zeta))}{(\zeta - z_0 - h)(\zeta - z_0)(\zeta - z_0 - k)}\, d\zeta .
> $$
>
> For $\zeta \in C$, that is $|\zeta - z_0| = r_0$, and $|h| < \frac{r_0}{2}$, $|k| < \frac{r_0}{2}$,
>
> $$
> |\zeta - z_0 - h| \ge |\zeta - z_0| - |h| > \frac{r_0}{2} , \qquad |\zeta - z_0| = r_0 \ge \frac{r_0}{2} , \qquad |\zeta - z_0 - k| > \frac{r_0}{2} ,
> $$
>
> so each of the three factors in the denominator has absolute value at least $\frac{r_0}{2}$. The function $\ell(f(\zeta))$ is analytic on $D$, hence continuous (fact (1)), so on the compact circle $C$ its absolute value has a finite supremum. By the bound for contour integrals (fact (3)), with the length $2\pi r_0$ of $C$,
>
> $$
> |\ell(x_{h,k})| \le \frac{1}{2\pi} \Bigl( \frac{2}{r_0} \Bigr)^3 \sup_{\zeta \in C} |\ell(f(\zeta))| \cdot 2\pi r_0 = \frac{8}{r_0^2}\, \sup_{\zeta \in C} |\ell(f(\zeta))| =: M(\ell) < \infty .
> $$
>
> The bound $M(\ell)$ depends on $\ell$ but not on $h$ and $k$:
>
> $$
> \sup \bigl\{ |\ell(x_{h,k})| : 0 < |h| < \tfrac{r_0}{2},\ 0 < |k| < \tfrac{r_0}{2},\ h \neq k \bigr\} \le M(\ell) < \infty \qquad \text{for every } \ell \in X' .
> $$
>
> ![[m556-47-2.svg]]
>
> The estimate of Step 3: $z_0 + h$ and $z_0 + k$ stay in the disk of radius $\frac{r_0}{2}$ (shaded), so every point $\zeta$ of $C$ is at distance more than $\frac{r_0}{2}$ from each of them, and at distance $r_0$ from $z_0$. (Not from lecture; figure added.)
>
> **Step 4: uniform boundedness.** Recall the uniform boundedness principle (Theorem [[§42 Uniform Boundedness and Approximation#^thm-42-6|§42.6]]): if $\{A_\alpha\}$ is a family of bounded linear maps on a Banach space with $\sup_\alpha \|A_\alpha x\| < \infty$ for every $x$, then $\sup_\alpha \|A_\alpha\| < \infty$. It is applied on the space $X'$, which is a Banach space (Corollary [[§31 Dual Spaces#^cor-31-1|§31.1]]). Each vector $x_{h,k} \in X$ defines the bounded linear functional $i(x_{h,k}) \in X'' = \mathcal{L}(X', \mathbb{C})$, $i(x_{h,k})(\ell) = \ell(x_{h,k})$, with $\|i(x_{h,k})\| = \|x_{h,k}\|$ (Proposition [[§37 Separable Duals and Reflexive Spaces#^prop-37-5|§37.5]]). By Step 3 the family $\{ i(x_{h,k}) \}$ is pointwise bounded on $X'$: for every $\ell \in X'$, $\sup_{h,k} |i(x_{h,k})(\ell)| \le M(\ell) < \infty$. Hence it is uniformly bounded:
>
> $$
> M := \sup \bigl\{ \|x_{h,k}\| : 0 < |h| < \tfrac{r_0}{2},\ 0 < |k| < \tfrac{r_0}{2},\ h \neq k \bigr\} < \infty ,
> $$
>
> where, as in Step 3,
>
> $$
> x_{h,k} = \frac{1}{h - k} \Bigl( \frac{f(z_0 + h) - f(z_0)}{h} - \frac{f(z_0 + k) - f(z_0)}{k} \Bigr) .
> $$
>
> **Step 5: the difference quotients are Cauchy.** By Step 4, for all $h, k$ with $0 < |h| < \frac{r_0}{2}$ and $0 < |k| < \frac{r_0}{2}$,
>
> $$
> \Bigl\| \frac{f(z_0 + h) - f(z_0)}{h} - \frac{f(z_0 + k) - f(z_0)}{k} \Bigr\| \le M\, |h - k| \le M\, (|h| + |k|)
> $$
>
> (for $h = k$ the left side is $0$). Let $\varepsilon > 0$. Enlarging $M$ if necessary, assume $M > 0$, and put
>
> $$
> \delta = \min\Bigl( \frac{r_0}{2},\ \frac{\varepsilon}{2M} \Bigr) .
> $$
>
> Then for all $h, k$ with $0 < |h| < \delta$ and $0 < |k| < \delta$: $|h| + |k| < \frac{\varepsilon}{M}$, so $\|q_h - q_k\| < \varepsilon$. This is the Cauchy property stated at the beginning, and Lemma [[§47 Weak and Strong Analyticity#^lem-47-2|§47.2]] (with $r = \frac{r_0}{2}$) gives $g(z_0) \in X$ with $\lim_{h \to 0} q_h = g(z_0)$. Since $z_0 \in D$ was arbitrary, $f$ is strongly analytic on $D$.

^pf-47-3

*Uses:* [[§47 Weak and Strong Analyticity#^lem-47-2|§47.2]], [[§47 Weak and Strong Analyticity#^def-47-1|Def. §47.1]], [[§42 Uniform Boundedness and Approximation#^thm-42-6|§42.6]], [[§31 Dual Spaces#^cor-31-1|§31.1]], [[§37 Separable Duals and Reflexive Spaces#^prop-37-5|§37.5]]

> [!remark]- Connections
> - Tools from complex analysis: [[Cauchy Integral Formula]], [[ML-Inequality]].
> - Tools from this course: [[Uniform Boundedness Principle]] on $X'$; the canonical embedding $X \to X''$, [[§37 Separable Duals and Reflexive Spaces#^prop-37-5|Prop. §37.5]].
> - Same method (vectors as functionals on the dual): [[Functional Analysis Problem-Solving Techniques#^rem-t29|Technique 29]]; weakly convergent sequences are bounded, [[§43 Weak and Weak-Star Convergence#^thm-43-6|Thm. §43.6]].
> - Used for the resolvent: [[§48 The Resolvent and the Spectrum#^def-48-2|Def. §48.2]].

> [!remark] Remark: The Length of the Circle
> In the notes of the lecture the bound of Step 3 is written with the factor $2\pi$ for the length of $C$, which gives $M(\ell) = \frac{8}{r_0^3} \sup_C |\ell(f)|$. The circle of radius $r_0$ has length $2\pi r_0$, which gives the value $\frac{8}{r_0^2} \sup_C |\ell(f)|$ used above. The proof only uses that $M(\ell)$ is finite and does not depend on $h$ and $k$, so nothing else changes.

^rem-47-2

![[m556-47-3.svg]]

The proof of Dunford's theorem at a glance, with $q_h$ the difference quotient and $x_{h,k} = (q_h - q_k)/(h - k)$. Complex analysis is used only for the scalar functions $\ell(f(z))$; the uniform boundedness principle turns the bounds $M(\ell)$, one for each functional, into a single bound in the norm of $X$. (Not from lecture; figure added.)

> [!remark] Remark: Where Completeness Enters
> The uniform boundedness principle is applied on $X'$, which is complete for every normed space $X$; so Steps 1–4 and the Lipschitz estimate $\|q_h - q_k\| \le M |h - k|$ of Step 5 hold for a weakly analytic function with values in any normed linear space. The completeness of $X$ is used only at the very end, in Lemma [[§47 Weak and Strong Analyticity#^lem-47-2|§47.2]], to turn the Cauchy property into a limit. This is the method “view vectors as functionals on the dual” (Technique 29 in the Problem-Solving Techniques), as in the proof that weakly convergent sequences are bounded (Theorem [[§43 Weak and Weak-Star Convergence#^thm-43-6|§43.6]]).

^rem-47-3

> [!remark] Remark: Where the Theorem is Used
> Dunford's theorem says that the analyticity of a vector-valued function can be checked one functional at a time, where all of scalar complex analysis is available. The main example is the resolvent $\lambda \mapsto (\lambda I - M)^{-1}$ of [[§48 The Resolvent and the Spectrum|§48]], a function with values in the Banach space $\mathcal{L}(X, X)$. Lax returns to the notion in his Chapter 17: there the resolvent is shown to be an analytic function on the resolvent set (§17.1, Thm 3), and the Cauchy integral theorem for analytic functions with values in a Banach space is used to show that the spectrum is not empty (§17.1, Thm 4).

^rem-47-4

> [!remark]- Connections
> - The scalar theorems that carry over once a function is known to be analytic: [[Cauchy–Goursat Theorem]], [[Liouville's Theorem]] (Complex Variables).

