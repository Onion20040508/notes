---
subject: "[[Single Variable Analysis]]"
section: 33
chapter: 6
tags: [real-analysis, math451]
---
← [[Single Variable Analysis §32 The Definition of the Riemann Integral]] · ↑ [[Single Variable Analysis — 6 Integration]] · [[Single Variable Analysis §34 Fundamental Theorem of Calculus]] →

It is often not easy to check integrability from the definitions — we need properties.

> [!theorem] Theorem §33.1: Monotonic Functions Are Integrable
> If $f: [a,b] \to \mathbb{R}$ is monotonic, then $f$ is integrable. (Note $f$ need not be continuous — though one can prove a monotonic function has at most countably many discontinuities, so it is not too bad.)

^thm-33-1

> [!proof]+ Proof
> Say $f$ is increasing (the decreasing case is symmetric). Take the equal partition $P$, so $t_k - t_{k-1} = \tfrac{b-a}{n}$. By monotonicity, the sup and inf on each subinterval are attained at the endpoints:
>
> $$
> M\bigl(f, [t_{k-1},t_k]\bigr) = f(t_k), \qquad m\bigl(f, [t_{k-1},t_k]\bigr) = f(t_{k-1}).
> $$
>
> So the difference of the sums *telescopes*:
>
> $$
> U(f,P) - L(f,P) = \sum_{k=1}^n \bigl( f(t_k) - f(t_{k-1}) \bigr)\, \frac{b-a}{n} = \bigl( f(b) - f(a) \bigr)\, \frac{b-a}{n}.
> $$
>
> For any $\varepsilon > 0$, take $n$ large enough that this is $< \varepsilon$: the Cauchy criterion applies. Done!

^pf-33-1

![[m451-33-1.svg]]
*Why monotone functions are integrable: on each subinterval of the equal partition, the gap between upper and lower rectangles is a box of width $\tfrac{b-a}{n}$ and height $f(t_k) - f(t_{k-1})$ (red). Slid sideways, the boxes stack into one column of height $f(b) - f(a)$ — the telescoping sum — so $U - L = \bigl(f(b) - f(a)\bigr)\tfrac{b-a}{n}$. A jump of $f$ (hollow and filled dots) changes nothing.*

> [!theorem] Theorem §33.2: Linearity
> If $f, g: [a,b] \to \mathbb{R}$ are integrable, then:
>
> 1. for any constant $c$, $cf$ is integrable and $\int_a^b cf = c\int_a^b f$;
>
> 2. $f + g$ is integrable and
>
>    $$
>    \int_a^b (f + g)\,dx = \int_a^b f\,dx + \int_a^b g\,dx.
>    $$

^thm-33-2

> [!proof]+ Proof
> (1) For $c \geq 0$: $U(cf, P) = c\,U(f,P)$ and $L(cf,P) = c\,L(f,P)$, so the Cauchy criterion and the value transfer directly. For $c < 0$, multiplying by $c$ *swaps* sup and inf: $U(cf,P) = c\,L(f,P)$ and $L(cf,P) = c\,U(f,P)$; the criterion and value again follow.
>
> (2) Here the Darboux approach meets a difficulty: on a subinterval $I$,
>
> $$
> M(f+g, I) \ \neq\ M(f,I) + M(g,I) \quad \text{in general}
> $$
>
> (the two functions may peak at different points) — only the inequalities
>
> $$
> M(f+g, I) \leq M(f,I) + M(g,I), \qquad m(f+g, I) \geq m(f,I) + m(g,I)
> $$
>
> hold (for Riemann sums, by contrast, additivity is exact — which is why the lecture remarked that Riemann's definition handles (2) more easily). Summing the inequalities over any partition $P$:
>
> $$
> L(f,P) + L(g,P) \leq L(f+g, P) \leq U(f+g, P) \leq U(f,P) + U(g,P).
> $$
>
> Given $\varepsilon$, choose partitions with $U(f,\cdot) - L(f,\cdot) < \tfrac\varepsilon2$ and $U(g,\cdot) - L(g,\cdot) < \tfrac\varepsilon2$, and pass to their common refinement $P$; then the outer quantities above are within $\varepsilon$ of each other, so $U(f+g,P) - L(f+g,P) < \varepsilon$: $f+g$ is integrable. Moreover the display traps both $\int(f+g)$ and $\int f + \int g$ in the same interval of length $< \varepsilon$; as $\varepsilon$ is arbitrary, they are equal.

^pf-33-2

> [!theorem] Theorem §33.3: Monotonicity of the Integral
> If $f, g$ are integrable on $[a,b]$ and $f(x) \leq g(x)$ for all $x$, then
>
> $$
> \int_a^b f\,dx \leq \int_a^b g\,dx.
> $$

^thm-33-3

> [!proof]+ Proof
> First: if $h \leq 0$ is integrable, then $\int_a^b h \leq 0$, since already $U(h, P) \leq 0$ for every $P$ (each $M(h, \cdot) \leq 0$), and the integral is $\leq$ every upper sum. Now write $f = g + (f - g)$ with $f - g \leq 0$ integrable (linearity):
>
> $$
> \int_a^b f = \int_a^b g + \int_a^b (f - g) \leq \int_a^b g.
> $$

^pf-33-3

> [!theorem] Theorem §33.4: Absolute Values
> If $f: [a,b] \to \mathbb{R}$ is integrable, then $|f|$ is integrable, and
>
> $$
> \left| \int_a^b f\,dx \right| \leq \int_a^b |f|\,dx.
> $$

^thm-33-4

> [!proof]+ Proof
> Which definition to use? Riemann sums are awkward here; Darboux works. The key observation: on any subinterval $I$,
>
> $$
> M(|f|, I) - m(|f|, I) \ \leq\ M(f, I) - m(f, I)
> $$
>
> — *taking absolute values decreases the variation*. Indeed, for any $x, y \in I$, the reverse [[Triangle inequality|triangle inequality]] gives
>
> $$
> \bigl| |f(x)| - |f(y)| \bigr| \leq |f(x) - f(y)| \leq M(f,I) - m(f,I),
> $$
>
> and taking the supremum over pairs $x, y$ on the left yields exactly $M(|f|,I) - m(|f|,I)$. Consequently $U(|f|,P) - L(|f|,P) \leq U(f,P) - L(f,P)$ for every partition, and the Cauchy criterion transfers from $f$ to $|f|$.
>
> For the inequality: $\pm f \leq |f|$, so by monotonicity and linearity, $\pm \int_a^b f \leq \int_a^b |f|$, which is the claim.

^pf-33-4

> [!remark] Remark: Warning
> The converse fails: for $f = 1$ on $\mathbb{Q}$ and $f = -1$ off $\mathbb{Q}$, the function $|f| \equiv 1$ is integrable on $[0,1]$, but $f$ is not (the Dirichlet argument verbatim: $U(f,P) = 1$, $L(f,P) = -1$ always).

^rem-33-1

> [!theorem] Theorem §33.5: Additivity over Subintervals
> Let $a < c < b$. If $f$ is integrable on $[a,c]$ and on $[c,b]$, then $f$ is integrable on $[a,b]$, and
>
> $$
> \int_a^b f\,dx = \int_a^c f\,dx + \int_c^b f\,dx.
> $$

^thm-33-5

> [!proof]+ Proof
> Given $\varepsilon > 0$, take partitions $P_1$ of $[a,c]$ and $P_2$ of $[c,b]$ with $U - L < \tfrac\varepsilon2$ on each. Their concatenation $P = P_1 \cup P_2$ is a partition of $[a,b]$ (containing $c$ as a cut point), and upper/lower sums split along $c$:
>
> $$
> U(f, P) = U(f, P_1) + U(f, P_2), \qquad L(f,P) = L(f,P_1) + L(f,P_2),
> $$
>
> so $U(f,P) - L(f,P) < \varepsilon$: integrable on $[a,b]$. The same splitting traps $\int_a^b f$ and $\int_a^c f + \int_c^b f$ between the same bounds within $\varepsilon$, forcing equality.

^pf-33-5

The converse direction — that integrability passes *down* to subintervals — is what makes splitting a given integral legal in the first place:

> [!theorem] Proposition §33.6: Restriction to Subintervals (HW)
> If $f$ is integrable on $[a,b]$, then $f$ is integrable on every interval $[c,d] \subseteq [a,b]$.

^prop-33-6

> [!proof]+ Proof
> Given $\varepsilon > 0$, the Cauchy criterion (§32) provides a partition $P$ of $[a,b]$ with $U(f,P) - L(f,P) < \varepsilon$. Refine to $P^* = P \cup \{c, d\}$; by the Refinement Lemma the difference only shrinks:
>
> $$
> U(f, P^*) - L(f, P^*) < \varepsilon.
> $$
>
> The points of $P^*$ lying in $[c,d]$ form a partition $P_2$ of $[c,d]$ (with $c, d$ as its endpoints), and the total difference splits along $c$ and $d$ into three blocks — over $[a,c]$, $[c,d]$, $[d,b]$ — each of the form $\sum (M_k - m_k)(t_k - t_{k-1}) \geq 0$. Discarding the two outer blocks,
>
> $$
> U(f, [c,d], P_2) - L(f, [c,d], P_2) \leq U(f, P^*) - L(f, P^*) < \varepsilon,
> $$
>
> and the Cauchy criterion on $[c,d]$ concludes.

^pf-33-6

> [!remark] Remark
> Together the two results make integrability on $[a,b]$ *equivalent* to integrability on both halves, and they license every splitting used later: chopping an integral along a partition (as in the [[Fundamental Theorem of Calculus|FTC]]'s telescoping, §34) silently invokes this proposition to know each piece $\int_{t_{k-1}}^{t_k} f$ exists.

^rem-33-2

## Positivity

> [!theorem] Theorem §33.7: Vanishing Integral of a Nonnegative Function
> Suppose $f: [a,b] \to \mathbb{R}$ is continuous and $f(x) \geq 0$ for all $x \in [a,b]$. Then $\int_a^b f\,dx \geq 0$; and if
>
> $$
> \int_a^b f\,dx = 0,
> $$
>
> then $f(x) = 0$ for *all* $x \in [a,b]$.

^thm-33-7

> [!proof]+ Proof
> The first statement is a special case of monotonicity ($0 \leq f$). For the second — why is it true? Geometrically: a bump anywhere would contribute positive area. Prove it by contradiction: suppose $f(x_0) > 0$ for some $x_0 \in [a,b]$. We may assume $x_0 \in (a,b)$: if $x_0$ were an endpoint, continuity provides nearby *interior* points where $f$ is still close to $f(x_0)$, hence positive — replace $x_0$ by one of them.
>
> By continuity at $x_0$ (with tolerance $\tfrac{f(x_0)}{2}$), there is $\varepsilon > 0$ small enough that $[x_0 - \varepsilon, x_0 + \varepsilon] \subset [a,b]$ and, for all $x$ in this neighborhood,
>
> $$
> |f(x) - f(x_0)| < \frac{f(x_0)}{2}, \qquad \text{hence} \qquad f(x) > \frac{f(x_0)}{2}.
> $$
>
> Now split the integral (additivity over subintervals) and discard the two outer pieces, which are $\geq 0$ since $f \geq 0$:
>
> $$
> \int_a^b f\,dx = \int_a^{x_0-\varepsilon} f + \int_{x_0-\varepsilon}^{x_0+\varepsilon} f + \int_{x_0+\varepsilon}^b f
> \ \geq\ \int_{x_0-\varepsilon}^{x_0+\varepsilon} f
> \ \geq\ \int_{x_0-\varepsilon}^{x_0+\varepsilon} \frac{f(x_0)}{2}\,dx
> = \frac{f(x_0)}{2}\cdot 2\varepsilon = f(x_0)\,\varepsilon > 0,
> $$
>
> contradicting $\int_a^b f = 0$.

^pf-33-7

![[m451-33-2.svg]]
*Positivity of the integral: if $f(x_0) > 0$, continuity keeps $f > \tfrac12 f(x_0)$ on $[x_0 - \varepsilon, x_0 + \varepsilon]$, so the region under $f$ (blue) contains the red rectangle of area $\tfrac12 f(x_0) \cdot 2\varepsilon = f(x_0)\,\varepsilon > 0$ — hence $\int_a^b f \geq f(x_0)\,\varepsilon > 0$.*

> [!theorem] Corollary §33.8: Vanishing Integral of a Square
> If $f: [a,b] \to \mathbb{R}$ is continuous and $\int_a^b f^2\,dx = 0$, then $f \equiv 0$.

^cor-33-8

> [!proof]+ Proof
> $f^2$ is continuous and $f^2(x) \geq 0$; the theorem gives $f^2 \equiv 0$, hence $f \equiv 0$.

^pf-33-8

> [!example] Example §33.1: Orthogonal to everything means zero
> Let $f: [a,b] \to \mathbb{R}$ be continuous, and suppose that for *all* continuous $g: [a,b] \to \mathbb{R}$,
>
> $$
> \int_a^b f(x)g(x)\,dx = 0.
> $$
>
> Show $f \equiv 0$. How? Take $g = f$: then $\int_a^b f^2 = 0$, and the corollary finishes.

^ex-33-1

> [!remark] Remark: Inner products on function spaces
> In $\mathbb{R}^2$, $\mathbb{R}^3$ we have orthogonality of vectors, governed by the inner product $\langle x, y \rangle = \sum_i x_i y_i$. On the space of continuous functions on $[a,b]$ — an *infinite-dimensional* vector space — the integral supplies an inner product:
>
> $$
> \langle f, g \rangle = \int_a^b f(x)g(x)\,dx.
> $$
>
> In $\mathbb{R}^2$, a vector perpendicular to every vector must be zero; the example above is exactly the same statement for the vector space of functions, proved by the same idea (pair the vector with itself).

^rem-33-3

## Mean Value Theorems for Integrals

> [!theorem] Theorem §33.9: Intermediate Value Theorem for Integrals
> Let $f: [a,b] \to \mathbb{R}$ be continuous. Then there exists at least one point $x_0 \in [a,b]$ such that
>
> $$
> f(x_0) = \frac{1}{b-a} \int_a^b f\,dx.
> $$

^thm-33-9

What does it mean? The right side is the **mean value** of $f$ over $[a,b]$: the mean value is attained — it equals the value of $f$ at some point.

> [!remark] Remark
> The continuity assumption is important. Counterexample: $f: [-1,1] \to \mathbb{R}$ with $f = -1$ on $[-1, 0)$ and $f = 1$ on $[0,1]$ (a step function, integrable by §32). Its mean value is $0$ — a value $f$ never takes.

^rem-33-4

> [!proof]+ Proof
> Since $f$ is continuous on the closed bounded interval, the [[Extreme Value Theorem|Extreme Value Theorem]] provides a maximum point $x_1$ and a minimum point $x_2$:
>
> $$
> f(x_1) = M = \max f, \qquad f(x_2) = m = \min f.
> $$
>
> By monotonicity of the integral, $m \leq f \leq M$ gives
>
> $$
> m(b-a) \leq \int_a^b f\,dx \leq M(b-a), \qquad \text{i.e.} \qquad m \leq \frac{1}{b-a}\int_a^b f\,dx \leq M.
> $$
>
> So the average value lies between $f(x_2)$ and $f(x_1)$. By the [[Intermediate Value Theorem|Intermediate Value Theorem]] for continuous functions (§18, applied between the points $x_1$ and $x_2$), some $x_0$ between them satisfies
>
> $$
> f(x_0) = \frac{1}{b-a}\int_a^b f\,dx.
> $$

^pf-33-9

![[m451-33-3.svg]]
*Left: the rectangle over $[a,b]$ at the mean height $\tfrac{1}{b-a}\int_a^b f$ (red) has the same area as the region under $f$ (blue); a continuous $f$ must cross that height, at some $x_0$. Right: the step function of the remark jumps over its mean value $0$ — without continuity the mean need not be attained.*

> [!theorem] Theorem §33.10: Weighted Mean Value Theorem
> Let $f, g: [a,b] \to \mathbb{R}$ be continuous with $g(x) \geq 0$ for all $x$. Then there exists $x_0 \in [a,b]$ such that
>
> $$
> \int_a^b f(x)g(x)\,dx = f(x_0) \int_a^b g(x)\,dx.
> $$
>
> This generalizes the previous theorem ($g \equiv 1$); here $g$ plays the role of a *weight function*, and the left side divided by $\int g$ is the weighted average of $f$.

^thm-33-10

> [!proof]+ Proof
> The same proof. With $M = \max f$, $m = \min f$: since $g \geq 0$,
>
> $$
> m\,g(x) \leq f(x)g(x) \leq M\,g(x),
> $$
>
> and integrating (monotonicity),
>
> $$
> m \int_a^b g\,dx \leq \int_a^b fg\,dx \leq M \int_a^b g\,dx.
> $$
>
> If $\int_a^b g\,dx = 0$: then $g \equiv 0$ by the positivity theorem (continuous, nonnegative), so $fg \equiv 0$, both sides vanish, and any $x_0$ works. Otherwise divide:
>
> $$
> m \leq \frac{\int_a^b fg\,dx}{\int_a^b g\,dx} \leq M,
> $$
>
> and the Intermediate Value Theorem for $f$ (between its min and max points) supplies $x_0$. Done.

^pf-33-10

The theorem places $x_0$ only in the *closed* interval. That is genuinely weaker than it needs to be:

> [!theorem] Proposition §33.11: The Witness Can Be Taken Interior (HW)
> In the Weighted [[Mean Value Theorem|Mean Value Theorem]], the point can always be chosen with $x_0 \in (a,b)$, the *open* interval.

^prop-33-11

> [!proof]+ Proof
> If $\int_a^b g\,dx = 0$, then (as in the theorem's proof) both sides vanish for *every* $x_0$; pick any interior point. So assume $\int_a^b g\,dx > 0$ and set
>
> $$
> A = \frac{\int_a^b fg\,dx}{\int_a^b g\,dx} \in [m, M].
> $$
>
> If $f$ is constant, $A = f(x_0)$ for every interior $x_0$. So assume $m < M$, and split by where $A$ sits.
>
> *Interior value* ($m < A < M$): let $x_1, x_2 \in [a,b]$ attain $f(x_1) = M$, $f(x_2) = m$ (Extreme Value Theorem); these are distinct. The IVT on the interval between them gives $x_0$ with $f(x_0) = A$, and since $A$ differs from both endpoint values, $x_0$ lies *strictly* between $x_1$ and $x_2$ — hence strictly inside $[a,b]$.
>
> *Boundary value* ($A = m$; the case $A = M$ is symmetric): then
>
> $$
> \int_a^b (f - m)\,g\,dx = \int_a^b fg\,dx - m \int_a^b g\,dx = 0,
> $$
>
> with $(f-m)g$ continuous and $\geq 0$; by the vanishing-integral theorem above, $(f - m)\,g \equiv 0$ on $[a,b]$. Since $\int_a^b g\,dx > 0$, some $x^*$ has $g(x^*) > 0$, and by continuity $g > 0$ on a whole interval $(x^* - \delta, x^* + \delta) \cap [a,b]$ of positive length. On that interval the identity $(f-m)g \equiv 0$ forces $f \equiv m$; and an interval of positive length inside $[a,b]$ certainly contains a point $x_0$ of the open $(a,b)$. There, $f(x_0) = m = A$.

^pf-33-11

> [!remark] Remark
> All the work sits in the boundary cases $A \in \{m, M\}$, where the plain IVT route might hand back only an endpoint (if $f$ attains its extremum nowhere else). The rescue mechanism — vanishing integral of a nonnegative continuous function forces identical vanishing, then local positivity of $g$ converts one good point into a whole subinterval — is the same tool as “orthogonal to everything means zero” above. Taking $g \equiv 1$ shows the ordinary Intermediate Value Theorem for Integrals also admits an interior witness.

^rem-33-5

> [!example] Example §33.2: Equal integrals meet
> Suppose $f, g: [a,b] \to \mathbb{R}$ are continuous and $\int_a^b f = \int_a^b g$. Show that $f(x_0) = g(x_0)$ for some $x_0 \in [a,b]$.
>
> Consider $h = f - g$: continuous, with $\int_a^b h = 0$ by linearity — so the mean value of $h$ is $0$. By the Intermediate Value Theorem for integrals, some $x_0$ has
>
> $$
> h(x_0) = \frac{1}{b-a}\int_a^b h\,dx = 0, \qquad \text{i.e.} \qquad f(x_0) = g(x_0).
> $$
>
> *In fact $x_0$ can be found in the open interval $(a,b)$* (HW). Suppose not: $h$ has no zero in $(a,b)$. Being continuous and never zero there, $h$ keeps a constant sign on $(a,b)$ (otherwise the IVT would manufacture a zero); say $h > 0$ on $(a,b)$ (else replace $h$ by $-h$). By continuity, $h(a), h(b) \geq 0$ as limits of positive values, so $h \geq 0$ on all of $[a,b]$ — continuous, nonnegative, with $\int_a^b h = 0$. The vanishing-integral theorem forces $h \equiv 0$, contradicting $h > 0$ on the nonempty $(a,b)$.

^ex-33-2

## Uniform Convergence and Integration Revisited

> [!theorem] Theorem §33.12: Integration of Uniform Limits
> Suppose $f_n: [a,b] \to \mathbb{R}$ are continuous and converge uniformly to $f$. Then $f$ is integrable, and
>
> $$
> \int_a^b f_n\,dx \longrightarrow \int_a^b f\,dx.
> $$

^thm-33-12

> [!proof]+ Proof
> By the uniform-limit theorem of §24, $f$ is continuous — hence integrable, by §32. (This is the point that was taken on credit back in §25: there, integrability was part of the calculus toolkit; now it is proved.) For the convergence: given $\varepsilon > 0$, uniform convergence provides $N$ such that for $n \geq N$ and all $x \in [a,b]$,
>
> $$
> |f_n(x) - f(x)| < \frac{\varepsilon}{b-a}.
> $$
>
> Then, by linearity, the absolute-value inequality, and monotonicity,
>
> $$
> \left| \int_a^b f_n\,dx - \int_a^b f\,dx \right| = \left| \int_a^b (f_n - f)\,dx \right| \leq \int_a^b |f_n - f|\,dx \leq \int_a^b \frac{\varepsilon}{b-a}\,dx = \varepsilon.
> $$

^pf-33-12
