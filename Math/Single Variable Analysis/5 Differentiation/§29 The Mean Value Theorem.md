---
type: section
subject: "[[Single Variable Analysis]]"
section: 29
chapter: 5
tags: [real-analysis, math451]
---
← [[§28 Basic Properties of the Derivative]] · ↑ [[· 5 Differentiation]] · [[§30 L'Hospital's Rule]] →

We come to an important section — the first of the three main results of this chapter.

## Interior Extrema and Rolle's Theorem

> [!theorem] Theorem §29.1: Interior Extremum Theorem
> Suppose $f: (a,b) \to \mathbb{R}$ has a maximum or minimum value at $x_0$. If $f$ is differentiable at $x_0$, then
>
> $$
> f'(x_0) = 0.
> $$

^thm-29-1

Note the interval is *open*: it has no boundary points, so $x_0$ is automatically an interior point. This is well known from calculus: a maximum or minimum point inside an interval is a **critical point** ($f'(x_0) = 0$).

> [!proof]+ Proof
> By definition! Assume $f$ has a maximum at $x_0$ (the minimum case is symmetric). The limit
>
> $$
> f'(x_0) = \lim_{x\to x_0} \frac{f(x) - f(x_0)}{x - x_0}
> $$
>
> exists, so both one-sided limits exist and equal it (§20). Now read the signs: for $x > x_0$, the numerator $f(x) - f(x_0) \leq 0$ (maximum!) while $x - x_0 > 0$, so the quotient is $\leq 0$, and limits preserve $\leq$:
>
> $$
> \lim_{x \to x_0^+} \frac{f(x) - f(x_0)}{x - x_0} \leq 0.
> $$
>
> For $x < x_0$ the quotient is $\geq 0$, so the left-hand limit is $\geq 0$. Both equal $f'(x_0)$, forcing $f'(x_0) = 0$.

^pf-29-1

*Uses:* [[§28 Basic Properties of the Derivative#^def-28-1|Def. §28.1]], [[§20 Limits of Functions#^thm-20-2|§20.2]], [[§9 Limit Theorems for Sequences#^prop-9-5|§9.5]]

> [!remark]- Connections
> - Fermat's condition in several variables (all partials vanish at an interior extremum): [[§14 Optimization and Lagrange Multipliers#^thm-14-1|452 Thm. §14.1]].
> - Computational version: [[§25 Maximum and Minimum Values#^thm-25-2|Calc Thm. §25.2]] (with worked examples).

> [!theorem] Theorem §29.2: Rolle's Theorem
> Let $f: [a,b] \to \mathbb{R}$ be continuous, and differentiable at every point of $(a,b)$ (briefly: differentiable on $(a,b)$). If $f(a) = f(b)$, then there exists $x_0 \in (a,b)$ with
>
> $$
> f'(x_0) = 0.
> $$

^thm-29-2

> [!proof]+ Proof
> By the [[Extreme Value Theorem|Extreme Value Theorem]] (§18), $f$ attains a maximum at some $x_1 \in [a,b]$ and a minimum at some $x_2 \in [a,b]$. Since $x_1, x_2$ could be endpoints, we cannot apply the previous theorem yet — two cases.
>
> *Case $f(x_1) = f(x_2)$:* the maximum equals the minimum, so every value of $f$ is squeezed between equal bounds — $f$ is constant. Then $f'(x_0) = 0$ for *every* $x_0 \in (a,b)$.
>
> *Case $f(x_1) > f(x_2)$:* since $f(a) = f(b)$, the two extreme values cannot both equal the common endpoint value; say $f(x_1) \neq f(a) = f(b)$ (otherwise argue with $x_2$). Then $x_1 \neq a, b$, so $x_1 \in (a,b)$: an interior maximum. By the previous theorem, $f'(x_1) = 0$.

^pf-29-2

*Uses:* [[Extreme Value Theorem|§18.1]], [[§29 The Mean Value Theorem#^thm-29-1|§29.1]]

> [!remark]- Connections
> - Computational version: [[§26 The Mean Value Theorem#^thm-26-1|Calc Thm. §26.1]] (with worked examples).
> - Used in PDEs: between consecutive zeros of $J_0$ lies a zero of $J_1=-J_0'$, [[§45★ Bessel's Equation#^cor-45-9|341 Cor. §45.9]].

## The Mean Value Theorem and Its Corollaries

> [!theorem] Theorem §29.3: Mean Value Theorem
> Let $f: [a,b] \to \mathbb{R}$ be continuous and differentiable on $(a,b)$. Then there exists $x_0 \in (a,b)$ such that
>
> $$
> f'(x_0) = \frac{f(b) - f(a)}{b - a}, \qquad \text{i.e.} \qquad f(b) - f(a) = f'(x_0)(b-a).
> $$

^thm-29-3

Two interpretations: (1) *slopes* — some tangent line is parallel to the chord through the endpoints; (2) *the average rate of change equals the rate of change at some one point*.

> [!proof]+ Proof
> Reduce to Rolle by subtracting the chord. Let $L$ be the linear function agreeing with $f$ at the endpoints:
>
> $$
> L(x) = f(a) + \frac{f(b) - f(a)}{b-a}\,(x - a), \qquad L(a) = f(a),\ L(b) = f(b), \qquad L'(x) = \frac{f(b)-f(a)}{b-a}.
> $$
>
> Set $g(x) = f(x) - L(x)$: continuous on $[a,b]$, differentiable on $(a,b)$, with $g(a) = g(b) = 0$. Rolle's theorem gives $x_0 \in (a,b)$ with $g'(x_0) = 0$, i.e.
>
> $$
> f'(x_0) - \frac{f(b)-f(a)}{b-a} = 0.
> $$

^pf-29-3

*Uses:* [[§29 The Mean Value Theorem#^thm-29-2|§29.2]]

![[m451-29-1.svg]]
*The [[Mean Value Theorem|Mean Value Theorem]]: somewhere in $(a,b)$ the tangent (red) is parallel to the secant (dashed). Rolle is the horizontal special case; the proof above is literally this picture — subtract the secant, and the extremum of what remains is $c$.*

> [!remark]- Connections
> - Computational version: [[§26 The Mean Value Theorem#^thm-26-2|Calc Thm. §26.2]] (with worked examples).
> - Fails for complex-valued functions: [[§41 Derivatives of Functions w(t)#^ex-41-3|342 Ex. §41.3]] (w(t) = eⁱᵗ on [0, 2π] has w′ never zero although w(2π) = w(0)).

> [!theorem] Corollary §29.4: Vanishing Derivative Means Constant
> If $f: (a,b) \to \mathbb{R}$ is differentiable and $f'(x) = 0$ for all $x \in (a,b)$, then $f$ is constant.

^cor-29-4

> [!proof]+ Proof
> Seems well known — but how to prove it? (The book has a proof by contradiction; here is a direct one.) For any two points $x_1 < x_2$ in $(a,b)$, the MVT on $[x_1, x_2]$ gives $x_0 \in (x_1, x_2)$ with
>
> $$
> f(x_2) - f(x_1) = f'(x_0)(x_2 - x_1) = 0 \cdot (x_2 - x_1) = 0.
> $$
>
> So $f$ takes the same value at any two points. Done.

^pf-29-4

*Uses:* [[Mean Value Theorem|§29.3]]

> [!remark]- Connections
> - If $f' = 0$ only almost everywhere, the conclusion needs absolute continuity: [[§18 Differentiation Theory#^thm-18-27|551 Thm. §18.27]], with the Cantor function as counterexample ([[§18 Differentiation Theory#^ex-18-4|551 Ex. §18.4]]).
> - Computational version: [[§26 The Mean Value Theorem#^thm-26-3|Calc Thm. §26.3]]; used for the uniqueness of solutions of $y' = ky$ in [[§21 Exponential Growth and Decay#^thm-21-1|Calc Thm. §21.1]].
> - Used in ODEs: every solution of $y' = ay - b$ has the form $b/a + ce^{at}$, [[§2 Solutions of Some Differential Equations#^thm-2-1|331 Thm. §2.1]], and the solutions of a separable equation are given implicitly by $H_1(x) + H_2(y) = c$, [[§5 Separable Differential Equations#^thm-5-1|331 Thm. §5.1]]; both proofs show that some function has zero derivative.
> - Computational version: [[§25 Analytic Functions#^thm-25-3|342 Thm. §25.3]] (f′ = 0 on a domain of ℂ forces f constant, reduced to this corollary along segments).

> [!theorem] Corollary §29.5: Equal Derivatives Differ by a Constant
> If $f, g: (a,b) \to \mathbb{R}$ are differentiable with $f'(x) = g'(x)$ for all $x$, then $f = g + c$ for some constant $c$.

^cor-29-5

> [!proof]+ Proof
> Apply the previous corollary to $f - g$, whose derivative vanishes identically.

^pf-29-5

*Uses:* [[§29 The Mean Value Theorem#^cor-29-4|§29.4]]

> [!remark]- Connections
> - Computational version: [[§26 The Mean Value Theorem#^cor-26-4|Calc Cor. §26.4]]; the most general antiderivative, [[§33 Antiderivatives#^thm-33-1|Calc Thm. §33.1]] (with worked examples).
> - Used in ODEs: the solutions of $y' + p(t)y = g(t)$ are exactly $\frac{1}{\mu}\big(\int_{t_0}^t \mu g\,ds + c\big)$, because $\mu y$ and $\int_{t_0}^t \mu g\,ds$ have the same derivative: [[§4 Linear Differential Equations; Method of Integrating Factors#^thm-4-1|331 Thm. §4.1]], [[§4 Linear Differential Equations; Method of Integrating Factors#^thm-4-2|331 Thm. §4.2]].

> [!theorem] Proposition §29.6: Vanishing k-th Derivative Means Polynomial (HW)
> Let $k \geq 1$ and let $f$ be $k$ times differentiable on an open interval $I$ with $f^{(k)} \equiv 0$ on $I$. Then $f$ is a polynomial of degree less than $k$; conversely, every such polynomial has vanishing $k$-th derivative.

^prop-29-6

> [!proof]+ Proof
> The converse is a direct computation. Forward, by induction on $k$. The case $k = 1$ is the constant corollary. Suppose the claim holds for $k$, and let $f^{(k+1)} \equiv 0$. Then $(f')^{(k)} = f^{(k+1)} \equiv 0$, so by the induction hypothesis $f'$ is a polynomial of degree less than $k$, say $f'(x) = \sum_{j=0}^{k-1} c_j x^j$. The polynomial $g(x) = \sum_{j=0}^{k-1} \tfrac{c_j}{j+1}\, x^{j+1}$ satisfies $g' = f'$ on $I$, so by the previous corollary $f = g + c$: a polynomial of degree at most $k$, i.e. less than $k + 1$.

^pf-29-6

*Uses:* [[§29 The Mean Value Theorem#^cor-29-4|§29.4]], [[§29 The Mean Value Theorem#^cor-29-5|§29.5]]

> [!remark] Remark
> This identifies the *kernel* of the $k$-th derivative operator: exactly the polynomials of degree $< k$ — a $k$-dimensional space, matching the $k$ constants of integration. It is also the uniqueness half of Taylor's theory (§31): once the remainder is shown to vanish, this proposition is what forces $f$ to *be* its Taylor polynomial.

^rem-29-1

> [!theorem] Corollary §29.7: Sign of the Derivative and Monotonicity
> Let $f: (a,b) \to \mathbb{R}$ be differentiable. If $f'(x) \geq 0$ for all $x$, then $f$ is increasing; if $f'(x) \leq 0$ for all $x$, then $f$ is decreasing.

^cor-29-7

> [!proof]+ Proof
> For $x_1 < x_2$ in $(a,b)$, the MVT gives $x_0$ with $f(x_2) - f(x_1) = f'(x_0)(x_2 - x_1)$, whose sign is the sign of $f'(x_0)$. (With strict inequalities $f' > 0$ throughout, the same display gives *strictly* increasing.)

^pf-29-7

*Uses:* [[Mean Value Theorem|§29.3]]

> [!remark]- Connections
> - Computational version: [[§27 What Derivatives Tell Us About the Shape of a Graph#^thm-27-1|Calc Thm. §27.1]] (with worked examples).

## Applications

> [!example] Example §29.1: Squared-Distance Contraction
> Suppose $f: \mathbb{R} \to \mathbb{R}$ satisfies $|f(x) - f(y)| \leq |x - y|^2$ for all $x, y$. Then $f$ is constant.
>
> *Proof.* For $x \neq y$,
>
> $$
> \left| \frac{f(x) - f(y)}{x - y} \right| \leq |x - y| \longrightarrow 0 \quad \text{as } x \to y,
> $$
>
> so $f$ is differentiable at every $y$ with $f'(y) = 0$ (squeeze). By the corollary, $f$ is constant.

^ex-29-1

> [!example] Example §29.2: The Tangent Line Inequality for the Exponential
> Prove: $e^x \geq ex$ for all $x \in \mathbb{R}$ (with equality at $x = 1$: the graph of $e^x$ lies above its tangent line at $(1, e)$).
>
> Let $f(x) = ex - e^x$; we want $f(x) \leq 0$. Note $f(1) = e - e = 0$. Check the derivative:
>
> $$
> f'(x) = e - e^x: \qquad f'(x) > 0 \text{ for } x < 1, \qquad f'(x) < 0 \text{ for } x > 1.
> $$
>
> So $f$ is increasing on $(-\infty, 1)$ and decreasing on $(1, \infty)$ (previous corollary): $x = 1$ is a global maximum with value $0$. Hence $f(x) \leq 0$ everywhere.

^ex-29-2

> [!example] Example §29.3: Sine below Its Argument
> Show $\sin x \leq x$ for all $x \geq 0$. Let $f(x) = x - \sin x$; then $f(0) = 0$ and
>
> $$
> f'(x) = 1 - \cos x \geq 0,
> $$
>
> so $f$ is increasing on $[0,\infty)$, giving $f(x) \geq f(0) = 0$, i.e. $\sin x \leq x$ for $x \geq 0$. Similarly (or by oddness: replace $x$ by $-x$), $\sin x \geq x$ for all $x \leq 0$.

^ex-29-3

The three examples above are one-sided instances of a two-sided principle:

> [!theorem] Proposition §29.8: Mean Value Inequality (HW)
> Suppose $f$ is continuous on $[a,b]$, differentiable on $(a,b)$, and $m \leq f'(x) \leq M$ for all $x \in (a,b)$. Then
>
> $$
> m\,(b-a) \;\leq\; f(b) - f(a) \;\leq\; M\,(b-a).
> $$
>
> Bounds on the derivative become bounds on every increment.

^prop-29-8

> [!proof]+ Proof
> The MVT gives $c \in (a,b)$ with $f(b) - f(a) = f'(c)(b-a)$; squeeze $f'(c)$ between $m$ and $M$ and multiply by $b - a > 0$.

^pf-29-8

*Uses:* [[Mean Value Theorem|§29.3]]

For instance: if $f$ is differentiable on $\mathbb{R}$ with $1 \leq f' \leq 2$ everywhere and $f(0) = 0$, then applying the proposition on $[0, x]$ gives $x \leq f(x) \leq 2x$ for every $x \geq 0$ — the graph is trapped between two lines through the origin.

![[m451-29-4.svg]]
*The mean value inequality as a wedge: with $f(0) = 0$ and $1 \leq f' \leq 2$, the graph of $f$ (blue) can never leave the region between the lines $x$ and $2x$ (dashed) for $x \geq 0$ — a bound on the slope becomes a bound on every increment.*

> [!example] Example §29.4: An Integrating Factor for Rolle (HW)
> Let $f, g$ be differentiable on an open interval $I$, and let $a < b$ in $I$ with $f(a) = f(b) = 0$. Show that
>
> $$
> f'(x) + f(x)\,g'(x) = 0 \qquad \text{for some } x \in (a,b).
> $$
>
> The expression is not the derivative of anything obvious — so *make* it one. Multiply by the always-positive factor $e^{g}$: the function $h = f\, e^{g}$ is differentiable on $I$ with
>
> $$
> h'(x) = e^{g(x)} \left[ f'(x) + f(x)\, g'(x) \right],
> $$
>
> and $h(a) = h(b) = 0$ since $f$ vanishes there. Rolle's theorem hands us $x_0 \in (a,b)$ with $h'(x_0) = 0$; dividing by $e^{g(x_0)} \neq 0$ leaves $f'(x_0) + f(x_0)g'(x_0) = 0$.

^ex-29-4

> [!remark] Remark
> The multiplier $e^{g}$ is the *integrating factor* of differential equations in embryo: the equation $y' + y\,g' = 0$ is exactly $(y e^{g})' = 0$, i.e. $y = C e^{-g}$. The general pattern is worth remembering: to prove some expression $E(x)$ vanishes somewhere, hunt for an auxiliary $h$ with equal endpoint values whose derivative is (positive function) $\times\, E$ — then Rolle does the rest. The MVT's own proof (tilting by a linear function) and the Generalized MVT of §30 are the same trick with different auxiliaries.

^rem-29-2

> [!remark]- Connections
> - Worked examples: the integrating factor for linear equations, [[§61 Linear Equations#^thm-61-1|Calc Thm. §61.1]]; $y' = x^2 y$ solved in [[§59 Separable Equations#^ex-59-3|Calc Ex. §59.3]].
> - The integrating factor in full: [[§4 Linear Differential Equations; Method of Integrating Factors#^def-4-2|331 Def. §4.2]] and the solution of $y' + p(t)y = g(t)$, [[§4 Linear Differential Equations; Method of Integrating Factors#^thm-4-2|331 Thm. §4.2]] (with worked examples).

## The Intermediate Value Theorem for Derivatives

Recall the [[Intermediate Value Theorem|Intermediate Value Theorem]] for continuous functions (§18). Derivatives satisfy their own version — remarkably, *without* assuming $f'$ continuous:

> [!theorem] Theorem §29.9: Darboux's Theorem
> Let $f: [a,b] \to \mathbb{R}$ be continuous and differentiable on $(a,b)$. Let $a < x_1 < x_2 < b$ and let $c$ lie between $f'(x_1)$ and $f'(x_2)$. Then there exists $x_0 \in (x_1, x_2)$ with
>
> $$
> f'(x_0) = c.
> $$

^thm-29-9

> [!proof]+ Proof
> Assume $f'(x_1) < c < f'(x_2)$ (for the reversed case, consider the maximum instead of the minimum below, or apply the result to $-f$). Following the general pattern — introduce a new function and find a critical point — let
>
> $$
> g(x) = f(x) - cx, \qquad g'(x_1) = f'(x_1) - c < 0, \quad g'(x_2) = f'(x_2) - c > 0.
> $$
>
> $g$ is continuous on $[x_1, x_2]$, so it attains a minimum at some $x_0 \in [x_1, x_2]$ ([[Extreme Value Theorem|EVT]]).
>
> *Claim: $x_0 \neq x_1, x_2$.* Since $g'(x_1) < 0$, the difference quotient $\tfrac{g(x) - g(x_1)}{x - x_1}$ is negative for $x$ slightly to the right of $x_1$ (its limit is negative); for such $x$, $x - x_1 > 0$ forces $g(x) < g(x_1)$ — nearby points in $(x_1, x_2)$ have *smaller* values, so $x_1$ is not the minimum. Symmetrically, $g'(x_2) > 0$ means points slightly to the *left* of $x_2$ have smaller values, so $x_2$ is not the minimum either.
>
> Hence $x_0 \in (x_1, x_2)$ is an interior minimum, and the Interior Extremum Theorem gives $g'(x_0) = 0$, i.e. $f'(x_0) = c$.

^pf-29-9

*Uses:* [[Extreme Value Theorem|§18.1]], [[§29 The Mean Value Theorem#^thm-29-1|§29.1]]

![[m451-29-2.svg]]
*The proof of Darboux's theorem: tilting by $cx$ makes $g = f - cx$ start downhill at $x_1$ ($g'(x_1) < 0$) and end uphill at $x_2$ ($g'(x_2) > 0$), so points just inside the interval lie below the endpoint values (dotted). The minimum given by the EVT is therefore interior, at $x_0$, where $g'(x_0) = 0$, i.e. $f'(x_0) = c$ — no continuity of $f'$ needed.*

> [!remark] Remark
> The point of the theorem: $f'$ may fail to be continuous (standard example: $f(x) = x^2 \sin\tfrac1x$, $f(0)=0$, whose derivative exists everywhere but is discontinuous at $0$), so we *cannot* simply apply the [[Intermediate Value Theorem|IVT]] of §18 to $f'$. Yet derivatives still take intermediate values.

^rem-29-3

> [!example] Example §29.5: Prescribed Derivative Values
> Let $f: \mathbb{R} \to \mathbb{R}$ be differentiable with $f(0) = 0$, $f(1) = 1$, $f(2) = 1$.
>
> **(a)** Some $x_0 \in (0,2)$ has $f'(x_0) = \tfrac12$: by the MVT on $[0,2]$,
>
> $$
> f'(x_0) = \frac{f(2) - f(0)}{2 - 0} = \frac12.
> $$
>
> **(b)** Some $x_0 \in (0,2)$ has $f'(x_0) = \tfrac17$: the MVT on $[0,1]$ gives $x_1 \in (0,1)$ with $f'(x_1) = \tfrac{1-0}{1-0} = 1$, and on $[1,2]$ gives $x_2 \in (1,2)$ with $f'(x_2) = \tfrac{1-1}{2-1} = 0$. Since $0 < \tfrac17 < 1$, Darboux's theorem applied between $x_1 < x_2$ produces $x_0 \in (x_1, x_2) \subset (0,2)$ with $f'(x_0) = \tfrac17$. (This second method also reproves (a).)

^ex-29-5

## The Derivative of the Inverse Function

Suppose $y = f(x)$ has an inverse $x = f^{-1}(y)$. *If we already knew* $f^{-1}$ were differentiable at $y_0 = f(x_0)$, the chain rule applied to $f^{-1}(f(x)) = x$ would give

$$
(f^{-1})'(y_0)\, f'(x_0) = 1, \qquad \text{i.e.} \qquad (f^{-1})'(y_0) = \frac{1}{f'(x_0)}.
$$

This computation finds the *formula* but presupposes the differentiability of $f^{-1}$ — which is exactly what the theorem must supply:

> [!theorem] Theorem §29.10: Inverse Function Theorem
> Let $I$ be an open interval and $f: I \to J = f(I)$ a continuous one-to-one map onto an open interval $J$, so that $f^{-1}: J \to I$ exists. If $f$ is differentiable at $x_0 \in I$ with $f'(x_0) \neq 0$, then $f^{-1}$ is differentiable at $y_0 = f(x_0)$, and
>
> $$
> (f^{-1})'(y_0) = \frac{1}{f'(x_0)}.
> $$

^thm-29-10

> [!proof]+ Proof
> Since $f$ is injective, $f(x) \neq f(x_0)$ for all $x \neq x_0$, so the reciprocal difference quotient is defined, and since $f'(x_0) \neq 0$, the reciprocal limit theorem gives
>
> $$
> \lim_{x \to x_0} \frac{x - x_0}{f(x) - f(x_0)} = \frac{1}{f'(x_0)}.
> $$
>
> Now translate into the $y$-variable. Write $g = f^{-1}$; a continuous injective function on an interval is strictly monotone (if not, three points would violate the [[Intermediate Value Theorem|IVT]]), so by the Continuous Inverse Theorem of §18 (extended to open intervals), $g$ is continuous. Let $y_n \to y_0$ in $J$ with $y_n \neq y_0$, and set $x_n = g(y_n)$. By continuity of $g$, $x_n \to x_0$, and by injectivity $x_n \neq x_0$. Then, by the sequential characterization of the limit above,
>
> $$
> \frac{g(y_n) - g(y_0)}{y_n - y_0} = \frac{x_n - x_0}{f(x_n) - f(x_0)} \longrightarrow \frac{1}{f'(x_0)}.
> $$
>
> Since the sequence $(y_n)$ was arbitrary, $g'(y_0)$ exists and equals $\tfrac{1}{f'(x_0)}$.

^pf-29-10

*Uses:* [[§18 Properties of Continuous Functions#^thm-18-9|§18.9]], [[Intermediate Value Theorem|§18.3]], [[§9 Limit Theorems for Sequences#^thm-9-4|§9.4]], [[§20 Limits of Functions#^def-20-1|Def. §20.1]]

> [!remark]- Connections
> - Complex counterpart: [[§114★ Local Inverses#^thm-114-1|342 Thm. §114.1]] (an analytic f with f′(z₀) ≠ 0 has an analytic local inverse with g′ = 1/f′).

> [!remark] Remark
> The assumption $f'(x_0) \neq 0$ is important: think of $f(x) = x^3$ at $x_0 = 0$ — the inverse $y \mapsto y^{1/3}$ exists but is not differentiable at $0$ (vertical tangent). Behind the theorem: $f'(x_0) \neq 0$ makes $f$ strictly monotone near $x_0$, so an inverse exists locally — a principle that generalizes far beyond calculus (the *inverse function theorem* of advanced analysis).

^rem-29-4

![[m451-29-3.svg]]
*Left: the graph of $f^{-1}$ (red) is the mirror image of the graph of $f$ (blue) in the line $y = x$; the mirror swaps rise and run, so the tangent at $(y_0, x_0)$ has slope $\tfrac{1}{f'(x_0)}$. Right: for $f(x) = x^3$ at $x_0 = 0$, the horizontal tangent ($f'(0) = 0$) mirrors into a vertical one — $y^{1/3}$ is not differentiable at $0$.*

> [!remark]- Connections
> - Several-variable version, with an invertible Jacobian in place of a nonzero derivative: [[§13 The Inverse Function Theorem#^thm-13-2|452 Thm. §13.2]].
> - Computational version: [[§19 Derivatives of Logarithmic and Inverse Trigonometric Functions#^thm-19-1|Calc Thm. §19.1]] (with worked examples).

> [!example] Example §29.6: Arcsine
> $f(x) = \sin x$ restricted to $\left[-\tfrac\pi2, \tfrac\pi2\right]$ (needed for $\arcsin$ to be well defined — draw the graph of $\sin$), with inverse $f^{-1}(y) = \arcsin y$:
>
> $$
> (\arcsin y)' = \frac{1}{\cos x} = \frac{1}{\sqrt{1 - \sin^2 x}} = \frac{1}{\sqrt{1 - y^2}},
> $$
>
> valid for $|y| < 1$: the Inverse Function Theorem needs $f'(x) = \cos x \neq 0$, i.e. $x \in \left(-\tfrac\pi2, \tfrac\pi2\right)$, and there $\cos x = +\sqrt{1 - \sin^2 x}$ because $\cos x > 0$. At $y = \pm1$ the arcsine has vertical tangents and no derivative.

^ex-29-6

> [!example] Example §29.7: Arctangent (HW)
> The same machine, one branch simpler. On $I = \left( -\tfrac\pi2, \tfrac\pi2 \right)$, $f(x) = \tan x$ has (quotient rule, Pythagoras)
>
> $$
> f'(x) = \frac{\cos^2 x + \sin^2 x}{\cos^2 x} = \frac{1}{\cos^2 x} > 0,
> $$
>
> so $f$ is strictly increasing with never-vanishing derivative, mapping $I$ onto $\mathbb{R}$. The Inverse Function Theorem applies at every point — no endpoint or sign caveats this time, unlike arcsine — and for $y_0 = \tan x_0$,
>
> $$
> \arctan'(y_0) = \frac{1}{f'(x_0)} = \cos^2 x_0 = \frac{1}{1 + \tan^2 x_0} = \frac{1}{1 + y_0^2},
> $$
>
> converting to the $y$-variable by dividing $\sin^2 + \cos^2 = 1$ through by $\cos^2$. So
>
> $$
> \arctan'(x) = \frac{1}{1+x^2} \qquad \text{on all of } \mathbb{R}
> $$
>
> — the derivative on which the arctangent series of §26 stands.

^ex-29-7
