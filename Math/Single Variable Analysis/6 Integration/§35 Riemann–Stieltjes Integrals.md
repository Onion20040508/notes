---
type: section
subject: "[[Single Variable Analysis]]"
section: 35
chapter: 6
tags: [real-analysis, math451]
---
← [[§34 Fundamental Theorem of Calculus]] · ↑ [[· 6 Integration]] · [[§36 Improper Integrals]] →

A brief introduction, as in lecture. The Riemann integral is essentially a sum, and one application is taking *averages* — where *weights* matter. How to pass from $\int_a^b f\,dx$ to weighted sums and weighted integrals?

The key: in the Darboux sums, the factor $(t_k - t_{k-1})$ represents *uniform* weight. Take instead an increasing function $F: [a,b] \to \mathbb{R}$ — the cumulative weight — and replace the length of $[t_{k-1}, t_k]$ by the weight increment

$$
F(t_k^-) - F(t_{k-1}^+),
$$

where $F(t^-), F(t^+)$ denote left and right limits (which exist for monotone $F$). Since $F$ need not be continuous, its *jumps at the partition points* must be accounted for separately:

$$
J_F(f, P) = \sum_{k=0}^{n} f(t_k)\,\bigl[ F(t_k^+) - F(t_k^-) \bigr]
$$

(with the conventions $F(a^-) = F(a)$, $F(b^+) = F(b)$). Then define

$$
U_F(f, P) = J_F(f,P) + \sum_{k=1}^n M\bigl(f, (t_{k-1}, t_k)\bigr)\bigl( F(t_k^-) - F(t_{k-1}^+) \bigr),
$$

$$
L_F(f, P) = J_F(f,P) + \sum_{k=1}^n m\bigl(f, (t_{k-1}, t_k)\bigr)\bigl( F(t_k^-) - F(t_{k-1}^+) \bigr),
$$

and the **upper and lower Darboux–Stieltjes integrals**

$$
U_F(f) = \inf_P U_F(f, P), \qquad L_F(f) = \sup_P L_F(f, P).
$$

As before, $L_F(f) \leq U_F(f)$.

> [!definition] Definition §35.1: Darboux–Stieltjes Integrability
> $f$ is **Darboux–Stieltjes integrable** with respect to $F$ if $L_F(f) = U_F(f)$; the common value is denoted
>
> $$
> \int_a^b f(x)\,dF(x).
> $$

^def-35-1

![[m451-35-1.svg]]
*Weights read off the vertical axis: in a Darboux–Stieltjes sum the open subinterval $(t_{k-1}, t_k)$ carries the weight $F(t_k^-) - F(t_{k-1}^+)$ (blue bars, alternating shades), while a jump of $F$ at a partition point is a separate weight $F(t_k^+) - F(t_k^-)$ (red), charged to the single value $f(t_k)$ in $J_F(f,P)$. Together the bars fill $F(b) - F(a)$; for $F(x) = x$ they are just the lengths $t_k - t_{k-1}$.*

The theory parallels §32: $f$ is Darboux–Stieltjes integrable if and only if for every $\varepsilon > 0$ some partition has $U_F(f,P) - L_F(f,P) < \varepsilon$; every continuous $f$ is Darboux–Stieltjes integrable; and one can define Riemann–Stieltjes sums and integrability — all very similar to the special case $F(x) = x$, which recovers the ordinary Riemann integral. (Details: Ross §35.)
