---
type: section
subject: "[[Multivariable Analysis]]"
chapter: 2
section: 11
tags: [multivariable-analysis, math452]
---
← [[§10 The Differential]] · ↑ [[· 2 Differentiation]] · [[§12 Composition of Functions and the Chain Rule]] →

## Review: Single-Variable Taylor's Theorem

For a function $f: \mathbb{R} \to \mathbb{R}$ that is $(N+1)$-times differentiable, the Taylor expansion around $x = a$ is ([[§31 Taylor's Theorem#^thm-31-2|451 §31.2]]):

$$
f(x) = \sum_{k=0}^{N} \frac{f^{(k)}(a)}{k!}(x - a)^k + R_{N+1},
$$

where the remainder (Lagrange form) is:

$$
R_{N+1} = \frac{f^{(N+1)}(\xi)}{(N+1)!}(x - a)^{N+1}
$$

for some $\xi$ between $a$ and $x$.

## The Key Idea: Reduce to Single Variable

For $f(x, y)$, we want to expand $f(x + h, y + k)$ around $(x, y)$. The trick is to **parametrize the line segment** from $(x, y)$ to $(x + h, y + k)$.

Define the single-variable function:

$$
F(t) = f(x + th, y + tk), \quad 0 \leq t \leq 1.
$$

![[m452-9-1.svg]]
*Reducing to one variable. Left: the segment from $(x, y)$ to $(x+h, y+k)$, traced by $(x + th, y + tk)$ (blue point) as $t$ runs over $[0,1]$. Right: $f$ read along the segment is the one-variable function $F(t)$, with $F(0) = f(x,y)$ and $F(1) = f(x+h,y+k)$. The single-variable Lagrange remainder is evaluated at some $\theta \in (0,1)$ (red), which on the left is the point $(x+\theta h,\, y+\theta k)$ of the segment — where all the $(N+1)$-st partials in $R_{N+1}$ are evaluated.*

Key observations:
- $F(0) = f(x, y)$ — the starting point
- $F(1) = f(x + h, y + k)$ — the ending point (what we want to expand)

Now we apply single-variable Taylor to $F(t)$ around $t = 0$!

## Computing Derivatives of $F(t)$

> [!theorem] Theorem §11.1: Derivatives of $F(t)$
> If $f$ has continuous partial derivatives up to order $m$, then:
>
> $$
> F^{(m)}(t) = \sum_{\ell=0}^{m} \binom{m}{\ell} \frac{\partial^m f}{\partial x^\ell \, \partial y^{m-\ell}}(x + th, y + tk) \cdot h^\ell k^{m-\ell}.
> $$

^thm-11-1

> [!proof]+ Proof
> We prove by induction on $m$.
>
> **Base case ($m = 1$):** By the [[§8 Algebra of Differentiable Functions#^thm-8-7|chain rule]]:
>
> $$
> F'(t) = \frac{d}{dt} f(x + th, y + tk) = f_x(x + th, y + tk) \cdot h + f_y(x + th, y + tk) \cdot k.
> $$
>
> This matches the formula with $\binom{1}{0} = \binom{1}{1} = 1$.
>
> **Inductive step:** Assume the formula holds for $m$. Differentiating:
>
> $$
> \begin{aligned}
> F^{(m+1)}(t) &= \frac{d}{dt} F^{(m)}(t) = \frac{d}{dt} \sum_{\ell=0}^{m} \binom{m}{\ell} \frac{\partial^m f}{\partial x^\ell \, \partial y^{m-\ell}} \cdot h^\ell k^{m-\ell}.
> \end{aligned}
> $$
>
> Applying the chain rule to each term:
>
> $$
> \frac{d}{dt} \frac{\partial^m f}{\partial x^\ell \, \partial y^{m-\ell}} = \frac{\partial^{m+1} f}{\partial x^{\ell+1} \, \partial y^{m-\ell}} \cdot h + \frac{\partial^{m+1} f}{\partial x^\ell \, \partial y^{m+1-\ell}} \cdot k.
> $$
>
> After collecting terms and using the Pascal's triangle identity $\binom{m}{\ell-1} + \binom{m}{\ell} = \binom{m+1}{\ell}$ ([[§12★ Counting Functions and Subsets#^prop-12-8|250 Prop. §12.8]]), we obtain the formula for $m + 1$.

^pf-11-1

*Uses:* [[§8 Algebra of Differentiable Functions#^thm-8-7|§8.7]], [[Continuous Partials Imply Differentiability|§7.2]], [[Schwarz–Clairaut Theorem|§6.1]], [[§12★ Counting Functions and Subsets#^prop-12-8|250 Prop. §12.8]]

> [!remark] Remark: First Few Derivatives
> Explicitly:
>
> $$
> \begin{aligned}
> F'(t) &= f_x h + f_y k, \\[4pt]
> F''(t) &= f_{xx} h^2 + 2f_{xy} hk + f_{yy} k^2, \\[4pt]
> F'''(t) &= f_{xxx} h^3 + 3f_{xxy} h^2 k + 3f_{xyy} hk^2 + f_{yyy} k^3,
> \end{aligned}
> $$
>
> where all partial derivatives are evaluated at $(x + th, y + tk)$.
>
> Note the binomial coefficients! This is why we can write symbolically:
>
> $$
> F^{(m)}(t) = \left( h \frac{\partial}{\partial x} + k \frac{\partial}{\partial y} \right)^m f \bigg|_{(x+th, y+tk)}.
> $$

^rem-11-1

## Taylor's Theorem for Two Variables

> [!theorem] Theorem §11.2: Multivariable Taylor's Theorem
> Let $f : \mathbb{R}^2 \to \mathbb{R}$ have continuous partial derivatives up to order $N + 1$ in an open ball $B$ around $(x, y)$, and let $(x + h, y + k) \in B$. Then:
>
> $$
> f(x + h, y + k) = \sum_{m=0}^{N} \frac{1}{m!} \sum_{\ell=0}^{m} \binom{m}{\ell} \frac{\partial^m f}{\partial x^\ell \, \partial y^{m-\ell}}(x, y) \cdot h^\ell k^{m-\ell} + R_{N+1},
> $$
>
> where the remainder is:
>
> $$
> R_{N+1} = \frac{1}{(N+1)!} \sum_{\ell=0}^{N+1} \binom{N+1}{\ell} \frac{\partial^{N+1} f}{\partial x^\ell \, \partial y^{N+1-\ell}}(x + \theta h, y + \theta k) \cdot h^\ell k^{N+1-\ell}
> $$
>
> for some $\theta \in (0, 1)$.

^thm-11-2

> [!proof]+ Proof
> The segment from $(x, y)$ to $(x + h, y + k)$ lies in the ball $B$, so by [[§11 Taylor's Theorem for Multivariable Functions#^thm-11-1|Theorem §11.1]] the function $F(t) = f(x + th, y + tk)$ has continuous derivatives up to order $N + 1$ on $[0, 1]$. Apply single-variable [[§31 Taylor's Theorem#^thm-31-2|Taylor's theorem]] to $F$:
>
> $$
> F(1) = \sum_{m=0}^{N} \frac{F^{(m)}(0)}{m!} \cdot 1^m + \frac{F^{(N+1)}(\theta)}{(N+1)!} \cdot 1^{N+1}
> $$
>
> for some $\theta \in (0, 1)$.
>
> Since $F(1) = f(x + h, y + k)$ and $F^{(m)}(0)$ is the [[§11 Taylor's Theorem for Multivariable Functions#^thm-11-1|formula for derivatives]] evaluated at $t = 0$ (i.e., at $(x, y)$), we obtain the result.

^pf-11-2

*Uses:* [[§11 Taylor's Theorem for Multivariable Functions#^thm-11-1|§11.1]], [[§31 Taylor's Theorem#^thm-31-2|451 §31.2]]

> [!remark]- Connections
> - The 1D theorem it reduces to: [[§31 Taylor's Theorem#^thm-31-2|Taylor's Theorem with Lagrange Remainder]].
> - The second-order case drives the [[Second Derivative Test in Several Variables|second-order sufficient conditions (§18.1)]] via the [[§18 Second-Order Sufficient Conditions#^def-18-1|Hessian]].
> - The second-order expansion in $N$ variables, $f(p+h)=f(p)+\nabla f(p)\cdot h+\tfrac12h^{\mathsf T}H_f(p+\theta h)h$, is proved by the same restriction to a line, together with a Peano-form remainder, in the honors-thesis notes ([[§R2.1 The Hessian and the Second-Derivative Test in N Variables#^thm-r2-1-1|Thesis Thm. §R2.1.1]]).

> [!remark] Remark: Compact Notation Using Differentials
> The Taylor expansion can be written elegantly as:
>
> $$
> f(x + h, y + k) = \sum_{m=0}^{N} \frac{1}{m!} d^m f \big|_{(x,y)} + R_{N+1},
> $$
>
> where $d^m f = \left( h \partial_x + k \partial_y \right)^m f$ is the $m$-th [[§10 The Differential#^def-10-3|differential]].

^rem-11-2

> [!remark] Remark: Why the Linear Path?
> One might ask: why parametrize with the linear path $F(t) = f(x + th, y + tk)$ rather than a general path $(h(t), k(t))$ from $(0,0)$ to $(h,k)$?
>
> The answer is that the Taylor polynomial $T_N(h,k)$ is the **unique polynomial that matches all partial derivatives of $f$ at $(x,y)$** up to order $N$. The linear path is special because:
> - The “instantaneous direction” $(h'(t), k'(t)) = (h, k)$ is constant
> - No path curvature: $h^{(j)}(t) = k^{(j)}(t) = 0$ for $j \geq 2$
> - Therefore $F^{(m)}(0) = d^m f$ directly, with no correction terms
>
> A curved path would have a changing instantaneous direction, introducing terms involving $h''(0), k''(0), \ldots$ that mix the geometry of the path with the geometry of $f$. The final answer $f(x+h,y+k)$ is path-independent (it's just a number!), but only the linear path produces the **canonical** polynomial whose coefficients are the intrinsic partial derivatives of $f$.

^rem-11-3

## Explicit Low-Order Expansions

> [!example] Example §11.1: First-Order Taylor Expansion
> For $N = 0$:
>
> $$
> f(x + h, y + k) = f(x, y) + R_1,
> $$
>
> where $R_1 = f_x(x + \theta h, y + \theta k) \cdot h + f_y(x + \theta h, y + \theta k) \cdot k$.
>
> This is the **Mean Value Theorem** for two variables.

^ex-11-1

> [!remark]- Connections
> - The 1D version it generalizes: [[Mean Value Theorem]].

> [!example] Example §11.2: Second-Order Taylor Expansion
> For $N = 1$:
>
> $$
> f(x + h, y + k) = f(x, y) + f_x(x, y) h + f_y(x, y) k + R_2,
> $$
>
> where:
>
> $$
> R_2 = \frac{1}{2} \left[ f_{xx}(\xi, \eta) h^2 + 2f_{xy}(\xi, \eta) hk + f_{yy}(\xi, \eta) k^2 \right]
> $$
>
> for some $(\xi, \eta) = (x + \theta h, y + \theta k)$ with $\theta \in (0, 1)$.
>
> This shows that $f(x+h, y+k) = f(x,y) + df + O(\rho^2)$, confirming our [[§7 Differentiability#^def-7-1|definition of differentiability]].

^ex-11-2

> [!example] Example §11.3: Third-Order Taylor Expansion
> For $N = 2$:
>
> $$
> \begin{aligned}
> f(x + h, y + k) &= f(x, y) + \bigl[ f_x h + f_y k \bigr] \\
> &\quad + \frac{1}{2} \bigl[ f_{xx} h^2 + 2f_{xy} hk + f_{yy} k^2 \bigr] + R_3,
> \end{aligned}
> $$
>
> where $R_3 = O(\rho^3)$ involves third-order partial derivatives.

^ex-11-3

## Appendix: Rolle's Theorem and the Mean Value Theorem

The Taylor theorem relies on the single-variable MVT, which in turn follows from Rolle's theorem.

> [!theorem] Theorem §11.3: Rolle's Theorem
> If $f$ is continuous on $[a, b]$, differentiable on $(a, b)$, and $f(a) = f(b)$, then there exists $\xi \in (a, b)$ such that $f'(\xi) = 0$.

^thm-11-3

> [!proof]+ Proof Idea
> Since $f$ is continuous on $[a, b]$, it attains its maximum and minimum ([[Extreme Value Theorem]]). If $\max = \min$, then $f$ is constant and $f' \equiv 0$. Otherwise, at least one of max/min occurs at an interior point $\xi \in (a, b)$, where $f'(\xi) = 0$ ([[§29 The Mean Value Theorem#^thm-29-1|Fermat's theorem]]).

^pf-11-3

*Uses:* [[Extreme Value Theorem|451 §18.1]], [[§29 The Mean Value Theorem#^thm-29-1|451 §29.1]]

> [!remark]- Connections
> - MATH 451 home: [[§29 The Mean Value Theorem#^thm-29-2|Rolle's Theorem (451 §29.2)]].
> - Fermat's theorem in $\mathbb{R}^n$: [[§17 Optimization and Lagrange Multipliers#^thm-17-1|Theorem §17.1]].

> [!theorem] Theorem §11.4: Mean Value Theorem
> If $f$ is continuous on $[a, b]$ and differentiable on $(a, b)$, then there exists $\xi \in (a, b)$ such that:
>
> $$
> f'(\xi) = \frac{f(b) - f(a)}{b - a}.
> $$

^thm-11-4

> [!proof]+ Proof
> Define the secant line:
>
> $$
> g(x) = \frac{f(b) - f(a)}{b - a}(x - a) + f(a).
> $$
>
> Note that $g(a) = f(a)$ and $g(b) = f(b)$.
>
> Let $h(x) = f(x) - g(x)$. Then:
> - $h$ is continuous on $[a, b]$ and differentiable on $(a, b)$
> - $h(a) = f(a) - g(a) = 0$
> - $h(b) = f(b) - g(b) = 0$
>
> By [[§11 Taylor's Theorem for Multivariable Functions#^thm-11-3|Rolle's theorem]], there exists $\xi \in (a, b)$ with $h'(\xi) = 0$. Since $h'(x) = f'(x) - \frac{f(b) - f(a)}{b - a}$:
>
> $$
> f'(\xi) = \frac{f(b) - f(a)}{b - a}.
> $$

^pf-11-4

*Uses:* [[§11 Taylor's Theorem for Multivariable Functions#^thm-11-3|§11.3]]

> [!remark]- Connections
> - MATH 451 home: [[Mean Value Theorem]] (451 §29.3), with the same proof.
