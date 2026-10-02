---
subject: "[[Single Variable Analysis]]"
section: 17
chapter: 3
tags: [real-analysis, math451]
---
← [[§16 Decimal Expansions of Real Numbers (Not Covered)]] · ↑ [[· 3 Continuity]] · [[§18 Properties of Continuous Functions]] →

We now start a central chapter of this course: the notion of *continuity*. You have all used continuous functions in calculus; now we will be rigorous.

## Two Definitions of Continuity

Start with basics. Let $f: \Omega \to \mathbb{R}$ be a real-valued function defined on a subset $\Omega \subseteq \mathbb{R}$, called the **domain** of $f$, sometimes denoted $\operatorname{dom}(f)$. The domain can be any subset, but usually we take intervals — closed $[a,b]$, open $(a,b)$, half-open — and unions of them; this is related to the open and closed subsets of $\mathbb{R}$ discussed in §13. Determining the domain of a function is important, as we will see repeatedly.

> [!definition] Definition §17.1: Continuity at a Point — Sequential Definition
> $f: \Omega \to \mathbb{R}$ is said to be **continuous at $x_0 \in \Omega$** if for every sequence $(x_n)$ in $\Omega$ converging to $x_0$,
>
> $$
> f(x_n) \longrightarrow f(x_0).
> $$
>
> Intuitively: when $x \in \Omega$ is close to $x_0$, then $f(x)$ is close to $f(x_0)$.

^def-17-1

> [!remark]- Connections
> - In topological spaces, continuity implies sequential continuity, with the converse for metrizable domains: [[§11 Metric Topology#^thm-11-9|590 Thm. §11.9]].
> - Computational version: Stewart's definition [[§10 Continuity#^def-10-1|Calc Def. §10.1]]; the sequential form, [[§69 Sequences#^thm-69-6|Calc Thm. §69.6]] (with worked examples).

> [!example] Example §17.1: Linear and polynomial functions
> $f(x) = 2x$ on $\Omega = \mathbb{R}$ is continuous at every $x_0$: if $x_n \to x_0$, then $f(x_n) = 2x_n \to 2x_0 = f(x_0)$ by the scalar-multiple limit theorem. More generally, every polynomial
>
> $$
> f(x) = a_n x^n + a_{n-1}x^{n-1} + \cdots + a_0
> $$
>
> is continuous at every point — by the limit theorems for sequences ($+$, $-$, $\times$) applied to $x_n \to x_0$.

^ex-17-1

For some functions the sequential definition is not so easy to check directly — e.g. $f(x) = \sqrt{x}$ on $[0, +\infty)$: if $x_n \to x_0$ with $x_n \geq 0$, does $\sqrt{x_n} \to \sqrt{x_0}$ follow? (We did prove this in §8, but it took work.) We need another formulation, involving $\varepsilon$ as in the case of sequences.

> [!theorem] Theorem §17.1: The Epsilon-Delta Characterization
> $f$ is continuous at $x_0 \in \Omega$ if and only if: for every $\varepsilon > 0$, there exists $\delta > 0$ such that for every $x \in \Omega$ with $|x - x_0| < \delta$,
>
> $$
> |f(x) - f(x_0)| < \varepsilon.
> $$
>
> This is the $(\varepsilon, \delta)$ definition — very basic and important; compare it with the $(\varepsilon, N)$ definition for sequences.

^thm-17-1

> [!proof]+ Proof
> ($\Leftarrow$) Suppose the $(\varepsilon,\delta)$ condition holds, and let $x_n \to x_0$ with $x_n \in \Omega$. Given $\varepsilon > 0$, get the corresponding $\delta > 0$. By the $(\varepsilon, N)$ definition applied to the tolerance $\delta$, there exists $N$ such that $|x_n - x_0| < \delta$ for all $n \geq N$. Therefore $|f(x_n) - f(x_0)| < \varepsilon$ for all $n \geq N$, which shows $f(x_n) \to f(x_0)$.
>
> ($\Rightarrow$) Conversely, assume $f$ is continuous at $x_0$ in the sequential sense; we prove the $(\varepsilon,\delta)$ condition by contradiction. If it fails, there exists some $\varepsilon > 0$ such that for *every* $\delta > 0$ there is a point $x_\delta \in \Omega$ with
>
> $$
> |x_\delta - x_0| < \delta \qquad \text{but} \qquad |f(x_\delta) - f(x_0)| \geq \varepsilon.
> $$
>
> For every $n \in \mathbb{N}$, apply this with $\delta = \tfrac1n$ to get $x_n \in \Omega$ with $|x_n - x_0| < \tfrac1n$ and $|f(x_n) - f(x_0)| \geq \varepsilon$. Then $x_n \to x_0$ but $f(x_n) \not\to f(x_0)$ — contradicting the sequential continuity at $x_0$.

^pf-17-1

![[m451-17-1.svg]]
*The $(\varepsilon, \delta)$ picture: the tolerance band $f(x_0) \pm \varepsilon$ (gray) is prescribed first; continuity provides a window $x_0 \pm \delta$ so narrow that over it the graph stays inside the band — it leaves the red box through the sides, never the top or bottom. Outside the window the graph is free to escape the band (and here it does, on both sides): $\delta$ genuinely depends on $\varepsilon$ and on $x_0$. This is the third member of a family: the $(\varepsilon, N)$ band for sequences (§9), this local window, one window-width for *all* points at once (uniform continuity, §19), and one band around a whole sequence of graphs (uniform convergence, §24).*

> [!remark] Remark: Solving for delta
> In the $(\varepsilon,\delta)$ definition, $\delta$ depends on $\varepsilon$: we need to *solve* $\delta$ in terms of $\varepsilon$. The idea, as with sequences: start with the target $|f(x) - f(x_0)| < \varepsilon$, *simplify first* — replace $|f(x)-f(x_0)|$ by a simpler upper bound if needed — and then solve for $|x - x_0| < \delta = \delta(\varepsilon)$.

^rem-17-1

> [!remark]- Connections
> - For maps between metric spaces, ε-δ continuity is equivalent to the open-set definition: [[§11 Metric Topology#^thm-11-7|590 Thm. §11.7]].

> [!example] Example §17.2: A first epsilon-delta proof
> $f(x) = 3x$ is continuous at every $x_0 \in \mathbb{R}$. How to get $\delta$? Start with
>
> $$
> |f(x) - f(x_0)| = |3x - 3x_0| = 3|x - x_0| < \varepsilon \quad \iff \quad |x - x_0| < \tfrac13\varepsilon.
> $$
>
> So take $\delta = \tfrac13 \varepsilon$. *Write-up:* for every $\varepsilon > 0$, let $\delta = \tfrac13\varepsilon$; when $|x - x_0| < \delta$, we get $|f(x) - f(x_0)| = 3|x-x_0| < 3 \cdot \tfrac13 \varepsilon = \varepsilon$.

^ex-17-2

> [!example] Example §17.3: The square root
> $f(x) = \sqrt{x}: [0,+\infty) \to \mathbb{R}$ is continuous at every $x_0 \geq 0$. Two cases.
>
> **Case $x_0 > 0$.** We want $|\sqrt x - \sqrt{x_0}| < \varepsilon$. By the conjugate,
>
> $$
> |\sqrt x - \sqrt{x_0}| = \left| \frac{x - x_0}{\sqrt x + \sqrt{x_0}} \right| \leq \frac{|x - x_0|}{\sqrt{x_0}},
> $$
>
> where the inequality replaces the denominator by the smaller $\sqrt{x_0}$ — solving the original inequality exactly would be awkward; the simplified bound is what we solve. Setting $\tfrac{|x-x_0|}{\sqrt{x_0}} < \varepsilon$ gives $|x - x_0| < \varepsilon \sqrt{x_0}$, so take
>
> $$
> \delta = \varepsilon \sqrt{x_0}.
> $$
>
> Going back: when $|x - x_0| < \delta$ (and $x \geq 0$), the computation above gives $|\sqrt x - \sqrt{x_0}| < \varepsilon$.
>
> **Case $x_0 = 0$.** The proof above fails — why? We divided by $\sqrt{x_0} = 0$. Handle it directly: $f(0) = 0$, and we want $|\sqrt x| < \varepsilon$, which simplifies to $|x| < \varepsilon^2$. So take $\delta = \varepsilon^2$, and go back to verify.
>
> It is important to note that $\delta$ depends on $\varepsilon$ *and also on $x_0$* — here $\delta = \varepsilon\sqrt{x_0}$ shrinks as $x_0$ approaches $0$. We will return to this point (uniform continuity).

^ex-17-3

> [!example] Example §17.4: Damped oscillation
> Define $f: \mathbb{R} \to \mathbb{R}$ by $f(0) = 0$ and $f(x) = x \sin \tfrac1x$ for $x \neq 0$. Then $f$ is continuous at $x = 0$. Two ways:
>
> (1) *Sequences:* if $x_n \to 0$, then $|f(x_n) - f(0)| = |x_n \sin\tfrac{1}{x_n}| \leq |x_n| \to 0$ (null times bounded, §8; for terms with $x_n=0$ the value is $0$ anyway).
>
> (2) *$(\varepsilon,\delta)$:* for $x \neq 0$, $|f(x) - f(0)| = |x \sin\tfrac1x| \leq |x|$, so take $\delta = \varepsilon$.
>
> In this case both are convenient; sometimes one is more convenient than the other. (About $\sin$: its rigorous definition comes later; here we use only the bound $|\sin t| \leq 1$.)

^ex-17-4

> [!example] Example §17.5: Undamped oscillation
> Define $g: \mathbb{R} \to \mathbb{R}$ by $g(0) = 0$ and $g(x) = \sin\tfrac1x$ for $x \neq 0$. Then $g$ is *not* continuous at $0$. How to prove it? Find a sequence $x_n \to 0$ with $g(x_n) \not\to 0 = g(0)$. As $x_n \to 0$, $\tfrac{1}{x_n} \to \infty$; choose the reciprocals to land where $\sin$ equals $1$:
>
> $$
> \frac{1}{x_n} = 2n\pi + \frac\pi2, \qquad \text{i.e.} \qquad x_n = \frac{1}{2n\pi + \tfrac\pi2} \longrightarrow 0,
> $$
>
> and $g(x_n) = \sin\left(2n\pi + \tfrac\pi2\right) = 1 \not\to 0$.

^ex-17-5

![[m451-17-3.svg]]
*Damped versus undamped oscillation at $0$. Left: $f(x) = x\sin\tfrac1x$ is trapped between $\pm|x|$ (dashed), so the square with $\delta = \varepsilon$ (red) contains the graph over $|x| < \delta$ — continuity at $0$. Right: $g(x) = \sin\tfrac1x$ oscillates between $\pm1$ ever faster (shaded: infinitely many oscillations); the points $x_n = \tfrac{1}{2n\pi + \pi/2} \to 0$ (red) keep $g(x_n) = 1$, far from $g(0) = 0$.*

> [!remark]- Connections
> - The graph of sin(1/x) on (0, 1] is the topologist's sine curve, [[§14 Connected Subspaces of ℝ#^ex-14-7|590 Ex. §14.7]], whose closure is connected but not path-connected because of this oscillation at 0.

> [!definition] Definition §17.2: Continuous Function
> A function $f: \Omega \to \mathbb{R}$ is called **continuous** if it is continuous at *every* point $x_0 \in \Omega$.

^def-17-2

> [!remark] Remark: Continuity depends on the domain
> Granting that $\sin x$ is continuous everywhere (proved later), the function $g$ above is continuous at every $x \neq 0$ but not at $0$ — so $g$ is not a continuous function. But if we define $G: \mathbb{R} \setminus \{0\} \to \mathbb{R}$, $G(x) = \sin\tfrac1x$, then $G$ *is* continuous. The difference between $g$ and $G$? Only the domain: $\operatorname{dom}(G)$ omits the bad point. Likewise $f(x) = \tfrac1x$ with $\operatorname{dom}(f) = (0,+\infty)$ is continuous, while extending it to $[0,+\infty)$ by $g(0) = 0$ produces a non-continuous function. So the continuity of a function depends on its domain — the domain is part of the definition of a function.

^rem-17-2

## Building Continuous Functions

> [!theorem] Theorem §17.2: Absolute Value of a Continuous Function
> If $f$ is continuous at $x_0$, then $|f|$ is continuous at $x_0$.

^thm-17-2

> [!proof]+ Proof
> By the reverse [[Triangle inequality|triangle inequality]],
>
> $$
> \bigl| |f(x)| - |f(x_0)| \bigr| \leq |f(x) - f(x_0)|,
> $$
>
> so any $\delta$ that works for $f$ (with tolerance $\varepsilon$) works for $|f|$.

^pf-17-2

> [!remark] Remark: The converse fails
> Define $f(x) = 1$ for $x \in \mathbb{Q}$ and $f(x) = -1$ for $x \in \mathbb{R}\setminus\mathbb{Q}$. Then $|f| \equiv 1$ is certainly continuous, but $f$ is continuous at *no* point: at any $x_0$, by the density of $\mathbb{Q}$ and of $\mathbb{R}\setminus\mathbb{Q}$ (§4, and below), there are sequences $x_n \to x_0$ along which $f \equiv 1$ and sequences along which $f \equiv -1$; both $1$ and $-1$ cannot equal $f(x_0)$.

^rem-17-3

> [!theorem] Theorem §17.3: Arithmetic of Continuous Functions
> If $f, g$ are continuous at $x_0 \in \operatorname{dom}(f) \cap \operatorname{dom}(g)$, then:
>
> 1. $f \pm g$ is continuous at $x_0$;
>
> 2. $fg$ is continuous at $x_0$;
>
> 3. if $g(x_0) \neq 0$, then $f/g$ is continuous at $x_0$ (on the domain where $g \neq 0$).

^thm-17-3

> [!proof]+ Proof
> It follows from the limit theorems for sequences (§9): if $x_n \to x_0$, then $f(x_n) \to f(x_0)$ and $g(x_n) \to g(x_0)$, so $f(x_n) \pm g(x_n) \to f(x_0) \pm g(x_0)$, $f(x_n)g(x_n) \to f(x_0)g(x_0)$, and (using $g(x_0) \neq 0$, quotient theorem) $f(x_n)/g(x_n) \to f(x_0)/g(x_0)$. One could also do it directly by the $(\varepsilon,\delta)$ definition.

^pf-17-3

> [!remark]- Connections
> - Same rules for functions of two variables: [[§3 Continuity and Limits of Functions#^thm-3-1|452 Thm. §3.1]], [[§3 Continuity and Limits of Functions#^thm-3-2|452 Thm. §3.2]], [[§3 Continuity and Limits of Functions#^thm-3-3|452 Thm. §3.3]] (sum, product, quotient).
> - Computational version: [[§10 Continuity#^thm-10-1|Calc Thm. §10.1]] (with worked examples).
> - Computational version: [[§18 Continuity#^prop-18-1|342 Prop. §18.1]] (sums, products, quotients and polynomials of continuous complex functions).

> [!example] Example §17.6: Polynomials and rational functions
> (1) All polynomial functions are continuous — we knew this already; it also follows from (1)–(2) starting with constants and $f(x)=x$. (2) Every rational function $\tfrac{P(x)}{Q(x)}$ is continuous at every point where the polynomial $Q$ does not vanish.

^ex-17-6

> [!remark]- Connections
> - Computational version: [[§10 Continuity#^thm-10-2|Calc Thm. §10.2]].

The most important and useful theorem in this section:

> [!theorem] Theorem §17.4: Composition of Continuous Functions
> Suppose $x_0 \in \operatorname{dom}(f)$ and $f(x_0) \in \operatorname{dom}(g)$ (with $f$ mapping into $\operatorname{dom}(g)$ near $x_0$, so the composition is defined). If $f$ is continuous at $x_0$ and $g$ is continuous at $f(x_0)$, then the composed function $g(f(x))$ is continuous at $x_0$.

^thm-17-4

> [!proof]+ Proof
> Suppose $x_n \to x_0$. Then $f(x_n) \to f(x_0)$ ($f$ continuous at $x_0$). Then $g(f(x_n)) \to g(f(x_0))$ ($g$ continuous at $f(x_0)$, applied to the sequence $f(x_n)$ in $\operatorname{dom}(g)$). Done! — The sequential definition makes this proof effortless.

^pf-17-4

> [!remark]- Connections
> - Several-variable versions: [[§3 Continuity and Limits of Functions#^thm-3-4|452 Thm. §3.4]] and [[§10 Composition of Functions and the Chain Rule#^thm-10-1|452 Thm. §10.1]].
> - Composition rule for continuous maps of topological spaces: [[§9 Continuous Functions#^thm-9-4|590 Thm. §9.4]].
> - Computational version: [[§10 Continuity#^thm-10-9|Calc Thm. §10.9]], with limits of composites in [[§10 Continuity#^thm-10-7|Calc Thm. §10.7]] (with worked examples).
> - Computational version: [[§18 Continuity#^thm-18-2|342 Thm. §18.2]] (composition of continuous complex functions, same proof).

> [!example] Example §17.7: Compositions and domains
> When applying the composition theorem, *check the domains*. (1) $f(x) = \tfrac1x$ is continuous at every $x \neq 0$, and $g(x) = \sin x$ is continuous (later); so $\sin\tfrac1x$ is continuous at every $x \neq 0$ — as claimed above. (2) $f(x) = \sqrt{|x|}: \mathbb{R} \to \mathbb{R}$ is continuous everywhere: it is the composition of $|x|: \mathbb{R} \to [0,\infty)$ and $\sqrt{x}: [0,\infty) \to \mathbb{R}$, and the domain condition is satisfied since $|x|$ takes values exactly in $\operatorname{dom}(\sqrt{\ })$.

^ex-17-7

> [!theorem] Theorem §17.5: Max and Min of Continuous Functions
> If $f, g: [a,b] \to \mathbb{R}$ are continuous, then $\max\{f,g\}$ and $\min\{f,g\}$ are continuous.

^thm-17-5

> [!proof]+ Proof
> This is more complicated than the arithmetic operations — until one finds the identity. *Claim:*
>
> $$
> \max\{f,g\}(x) = \frac12\bigl(f(x) + g(x)\bigr) + \frac12\bigl|f(x) - g(x)\bigr|.
> $$
>
> Check both cases: if $f(x) > g(x)$, the right side is $\tfrac12(f+g) + \tfrac12(f-g) = f(x) = \max\{f,g\}(x)$; if $f(x) \leq g(x)$, it is $\tfrac12(f+g) + \tfrac12(g-f) = g(x) = \max\{f,g\}(x)$. Now combine the theorems: $f - g$ is continuous, hence $|f-g|$ is continuous, hence the whole right side is continuous (sums and scalar multiples). Similarly
>
> $$
> \min\{f,g\}(x) = \frac12\bigl(f(x)+g(x)\bigr) - \frac12\bigl|f(x)-g(x)\bigr|
> $$
>
> (or use $\min\{f,g\} = -\max\{-f,-g\}$).

^pf-17-5

## Exotic Functions

We have seen many continuous functions — polynomials, rational functions, and later $\sin$, $\cos$, exponentials. How about some *non*-continuous functions? Making use of the structures of the rational and real numbers, we can construct functions far stranger than the ordinary ones.

> [!example] Example §17.8: Nowhere continuous
> The function $f = 1$ on $\mathbb{Q}$, $f = -1$ on $\mathbb{R}\setminus\mathbb{Q}$ above is continuous at no point — yet $|f|$ is continuous. Can we make *both* $g$ and $|g|$ discontinuous everywhere? Take
>
> $$
> g(x) = 1 \ (x \in \mathbb{Q}), \qquad g(x) = 0 \ (x \in \mathbb{R}\setminus\mathbb{Q}).
> $$
>
> Since $g \geq 0$, $|g| = g$, so it suffices that $g$ is nowhere continuous — which follows by the same two-sequence argument at every point.

^ex-17-8

> [!remark] Remark: Density of the irrationals
> These arguments use that $\mathbb{R} \setminus \mathbb{Q}$ is dense in $\mathbb{R}$: every interval $(a,b)$ contains irrational points. Why? The interval $(a,b)$ contains uncountably many points, but only countably many rationals (§2) — so it must contain (uncountably many) irrationals. One can also argue directly: if $x_0 \in \mathbb{Q}$, the points $x_0 + \tfrac{\pi}{n}$ are irrational and converge to $x_0$.

^rem-17-4

> [!example] Example §17.9: Continuous exactly at the irrationals
> Can we construct $f: \mathbb{R} \to \mathbb{R}$ that is continuous at every *irrational* point but discontinuous at every *rational* point? Not so easy — but yes. Define
>
> $$
> f(x) = 0 \quad (x \in \mathbb{R}\setminus\mathbb{Q}); \qquad f\left(\frac pq\right) = \frac1q \quad \left( \frac pq \in \mathbb{Q} \text{ in lowest terms},\ q > 0 \right).
> $$
>
> (The lowest-terms representation with positive denominator is unique, so $f$ is well defined.)
>
> **Discontinuity at rationals (the easy part).** Let $x_0 = \tfrac pq$, so $f(x_0) = \tfrac1q > 0$. Choose an irrational sequence $x_n \to x_0$ (density of irrationals above — e.g. $x_n = x_0 + \tfrac\pi n$). Then $f(x_n) = 0 \not\to \tfrac1q = f(x_0)$. Not continuous.
>
> **Continuity at irrationals (the harder part).** Let $x_0 \in \mathbb{R}\setminus\mathbb{Q}$, so $f(x_0) = 0$; take any $x_n \to x_0$; we must show $f(x_n) \to 0$. For irrational terms $f(x_n) = 0$ — no problem. Assume for the moment all $x_n \in \mathbb{Q}$, written in lowest terms $x_n = \tfrac{p_n}{q_n}$.
>
> *Claim (1): $(q_n)$ is not bounded.* Suppose $q_n \leq M$ for all $n$. Since $\tfrac{p_n}{q_n} \to x_0$, the sequence is bounded: $\left|\tfrac{p_n}{q_n}\right| \leq C$, hence $|p_n| \leq C q_n \leq CM$. So only finitely many pairs $(p_n, q_n)$ occur — the sequence $(x_n)$ takes only finitely many distinct values. A convergent sequence with finitely many values is eventually constant, so $x_0$ would equal that constant, a *rational* number — contradicting $x_0$ irrational.
>
> *Claim (2): in fact $q_n \to +\infty$.* If not, some subsequence $(q_{n_k})$ is bounded (negating $q_n \to +\infty$: there is $M$ such that for every $N$ some $n \geq N$ has $q_n \leq M$; extract inductively). But $\tfrac{p_{n_k}}{q_{n_k}} \to x_0$ still, so Claim (1) applied to the subsequence gives a contradiction.
>
> Now finish: $f(x_n) = \tfrac{1}{q_n} \to 0 = f(x_0)$.
>
> *The general (mixed) sequence:* split $(x_n)$ into its irrational terms, along which $f \equiv 0$, and its rational terms, along which $f \to 0$ by the argument above (if there are infinitely many of them; finitely many don't matter). Given $\varepsilon > 0$, beyond some index every term of either kind has $f(x_n) < \varepsilon$; hence $f(x_n) \to 0$. So $f$ is continuous at every irrational point.

^ex-17-9

![[m451-17-2.svg]]
*The Thomae function on $(0,1)$, drawn for $q \leq 14$. The proof is visible: above any fixed height $\varepsilon$ (dashed) lie only finitely many dots (red — those with $\tfrac1q > \varepsilon$), so an irrational $x_0$ has a window (blue strip) containing none of them, and there every value of $f$ is below $\varepsilon$ — continuity at every irrational. At a rational $\tfrac pq$, by contrast, the dot sits at height $\tfrac1q > 0$ while the irrationals arbitrarily close by give $0$ — discontinuity.*

A counterweight to all these constructions — continuity is *rigid* on dense sets:

> [!theorem] Proposition §17.6: Continuous Functions Are Determined on the Rationals (HW)
> Let $f, g: (a,b) \to \mathbb{R}$ be continuous with $f(r) = g(r)$ for every rational $r \in (a,b)$. Then $f(x) = g(x)$ for *all* $x \in (a,b)$. In particular, a continuous function vanishing at every rational point of $(a,b)$ vanishes identically.

^prop-17-6

> [!proof]+ Proof
> Let $h = f - g$, continuous on $(a,b)$ with $h(r) = 0$ for every rational $r \in (a,b)$; it suffices to show $h \equiv 0$. Fix $x_0 \in (a,b)$. For each $n$, the set
>
> $$
> \left( x_0 - \tfrac1n,\ x_0 + \tfrac1n \right) \cap (a,b)
> $$
>
> is a nonempty open interval ($x_0$ is an interior point of $(a,b)$), so the density of $\mathbb{Q}$ (§4) provides a rational $r_n$ inside it. Then $r_n \in (a,b)$, $r_n \to x_0$, and by the sequential definition of continuity,
>
> $$
> h(x_0) = \lim_{n\to\infty} h(r_n) = \lim_{n\to\infty} 0 = 0.
> $$

^pf-17-6

> [!remark]- Connections
> - Computational version: Stewart fills in $b^x$ at irrational $x$ from its rational values, [[§4 Exponential Functions#^def-4-3|Calc Def. §4.3]].

> [!remark] Remark
> Nothing about $\mathbb{Q}$ was special except its *density*: the same proof shows a continuous function is determined by its values on any dense subset (any $Y$ with $\overline{Y} \supseteq (a,b)$, in the closure language of §13). Read against the examples above, this is the price they pay: any function built to *distinguish* $\mathbb{Q}$ from $\mathbb{R}\setminus\mathbb{Q}$ — Dirichlet-type or Thomae-type — is forced to be discontinuous somewhere, for a continuous function cannot tell a dense set apart from the whole line.

^rem-17-5
