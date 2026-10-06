---
type: section
subject: "[[Complex Variables]]"
chapter: 7
section: 94
bc: "94"
aliases: ["B&C 94"]
tags: [complex-variables, math342]
---
← [[§93 Argument Principle]] · ↑ [[· 7 Applications of Residues]] · [[§95★ Inverse Laplace Transforms]] →

*Brown–Churchill, Section 94 · MAT 342 HW 13, Practice Final (Spring 2012).*

Rouché's theorem turns the argument principle into a practical tool for locating zeros. If on a closed contour one term $f$ of a function dominates the rest $g$, $|f| > |g|$, then $f + g$ has as many zeros inside as $f$ does. The reason is that $f + g = f\cdot(1 + g/f)$, and the factor $1 + g/f$ stays in the disk $|w - 1| < 1$, so it cannot wind around the origin: it changes the argument by nothing. For polynomials, comparing with the largest term on a circle counts the roots in a disk or an annulus without finding them, and comparing with the leading term on a large circle gives a second proof of the fundamental theorem of algebra.

> [!theorem] Theorem §94.1: Rouché's Theorem
> Let $C$ denote a simple closed contour, and suppose that
> - (a) two functions $f(z)$ and $g(z)$ are analytic inside and on $C$;
> - (b) $|f(z)| > |g(z)|$ at each point on $C$.
>
> Then $f(z)$ and $f(z) + g(z)$ have the same number of zeros, counting multiplicities, inside $C$.
>
> *B&C: Sec. 94, Theorem*

^thm-94-1

> [!proof]+ Proof
> The orientation of $C$ is immaterial to the statement, so we may assume it is positive. Neither $f$ nor $f + g$ has a zero on $C$, since there
>
> $$
> |f(z)| > |g(z)| \ge 0 \qquad\text{and}\qquad |f(z) + g(z)| \ge \big||f(z)| - |g(z)|\big| > 0 .
> $$
>
> Let $Z_f$ and $Z_{f+g}$ be the numbers of zeros of $f$ and $f + g$ inside $C$, counting multiplicities. Both functions are analytic inside and on $C$ and nonzero on $C$, so the argument principle ([[§93 Argument Principle#^thm-93-4|Theorem §93.4]], with $P = 0$) gives
>
> $$
> Z_f = \frac{1}{2\pi}\Delta_C\arg f(z) \qquad\text{and}\qquad Z_{f+g} = \frac{1}{2\pi}\Delta_C\arg\big[f(z) + g(z)\big] .
> $$
>
> On $C$, $f + g = f\cdot F$ with
>
> $$
> F(z) = 1 + \frac{g(z)}{f(z)} ,
> $$
>
> which is continuous and nonzero on $C$ (indeed analytic in a neighborhood of $C$, where $f \ne 0$). If $\phi_f$ and $\phi_F$ are continuous arguments of $f(z(t))$ and $F(z(t))$ along a parametrization of $C$ ([[§93 Argument Principle#^lem-93-1|Lemma §93.1]]), then $\phi_f + \phi_F$ is a continuous argument of their product; so
>
> $$
> \Delta_C\arg\big[f(z) + g(z)\big] = \Delta_C\arg\Big\{f(z)\Big[1 + \frac{g(z)}{f(z)}\Big]\Big\} = \Delta_C\arg f(z) + \Delta_C\arg F(z),
> $$
>
> and therefore
>
> $$
> Z_{f+g} = Z_f + \frac{1}{2\pi}\Delta_C\arg F(z) . \qquad (1)
> $$
>
> But on $C$
>
> $$
> |F(z) - 1| = \frac{|g(z)|}{|f(z)|} < 1 ,
> $$
>
> so under $w = F(z)$ the image of $C$ lies in the open disk $|w - 1| < 1$, which is contained in the half plane $\operatorname{Re} w > 0$. That image does not meet the ray $\arg w = \pi$ from the origin, so $\Delta_C\arg F(z) = 0$ by [[§93 Argument Principle#^prop-93-2|Proposition §93.2]] (whose proof uses only that $F(z(t))$ is a continuous, piecewise smooth, nonvanishing closed curve). Equation (1) reduces to $Z_{f+g} = Z_f$.

^pf-94-1

*Uses:* [[§93 Argument Principle#^thm-93-4|§93.4]], [[§93 Argument Principle#^lem-93-1|§93.1]], [[§93 Argument Principle#^prop-93-2|§93.2]], [[§5 Triangle Inequality#^cor-5-2|§5.2]]

> [!remark]- Connections
> - Topologically, Rouché's theorem is the homotopy invariance of the winding number. Since $|g| < |f|$ on $C$, the loops $(f + tg)(C)$, $0 \le t \le 1$, never pass through $0$, so they form a homotopy in $\mathbb{C} \setminus \{0\}$ from the image loop of $f$ to that of $f + g$, and homotopic loops wind equally often around $0$. Step 3 of the topological proof of the fundamental theorem of algebra, [[§25 The Fundamental Theorem of Algebra#^thm-25-1|590 Thm. §25.1]], is exactly this homotopy with $f = z^n$ on the unit circle; there the winding number is the class of the loop in $\pi_1(\mathbb{R}^2 \setminus \{0\}) \cong \pi_1(S^1) \cong \mathbb{Z}$ ([[Fundamental Group of the Circle]]).

![[m342-94-1.svg]]
*Rouché's theorem for Example §94.1, $f = 3z^3$, $g = z^4 + 6$ on $|z| = 2$. Left: the image of the circle under $f + g = z^4 + 3z^3 + 6$, computed from $z = 2e^{i\theta}$, winds three times counterclockwise around the origin, so $f + g$ has three zeros in $|z| < 2$. Right: the factor $F = 1 + g/f = 1 + z/3 + 2/z^3$ keeps the image inside the disk $|w - 1| < 1$ (dashed), since $|g/f| \le 22/24$ there; it never winds around $0$, so $f + g$ inherits the winding number $3$ of $3z^3$.*

> [!remark] Remark: Method — Counting Zeros with Rouché's Theorem
> To count the zeros of $h(z)$ in $|z| < r$:
> 1. **Split** $h = f + g$, with $f$ a single dominant term on $|z| = r$, usually the term $a_kz^k$ with the largest modulus $|a_k|r^k$. Then $f$ has $k$ zeros in $|z| < r$ (all at $0$).
> 2. **Bound** $|g|$ on $|z| = r$ by the triangle inequality, $|g(z)| \le \sum_{j\ne k}|a_j|r^j$, and check $|f| > |g|$ strictly. If the bound fails, try another split or another radius.
> 3. **Conclude** that $h$ has $k$ zeros in $|z| < r$, and none on $|z| = r$.
> 4. **Annulus** $r_1 < |z| < r_2$: count in $|z| < r_2$ and in $|z| < r_1$ and subtract; Rouché on $|z| = r_1$ also shows that there are no zeros on that circle, so the count is the same for $r_1 \le |z| < r_2$.
>
> The same works for non-polynomials; only analyticity inside and on the circle and the strict inequality are needed.

^rem-94-1

## Examples

> [!example] Example §94.1: The Roots of z⁴ + 3z³ + 6 in |z| < 2
> Determine the number of roots, counting multiplicities, of
>
> $$
> z^4 + 3z^3 + 6 = 0 \qquad (2)
> $$
>
> inside the circle $|z| = 2$. Write $f(z) = 3z^3$ and $g(z) = z^4 + 6$. When $|z| = 2$,
>
> $$
> |f(z)| = 3|z|^3 = 24 \qquad\text{and}\qquad |g(z)| \le |z|^4 + 6 = 22 .
> $$
>
> The conditions of Rouché's theorem are satisfied, and $f$ has three zeros (a triple zero at $0$) inside $|z| = 2$; so does $f + g$. Equation (2) has three roots there. (Numerically, the moduli of the four roots are $1.166$, $1.166$, $1.640$ and $2.693$.)
>
> *B&C: Sec. 94, Example 1*

^ex-94-1

> [!example] Example §94.2: The Fundamental Theorem of Algebra
> Rouché's theorem gives another proof of the fundamental theorem of algebra ([[§58 Liouville's Theorem and the Fundamental Theorem of Algebra#^thm-58-2|Theorem §58.2]]), in a stronger form: a polynomial
>
> $$
> P(z) = a_0 + a_1z + a_2z^2 + \cdots + a_nz^n \qquad (a_n \ne 0) \qquad (3)
> $$
>
> of degree $n \ge 1$ has exactly $n$ zeros, counting multiplicities.
>
> Write $f(z) = a_nz^n$ and $g(z) = a_0 + a_1z + \cdots + a_{n-1}z^{n-1}$, and let $|z| = R$ with $R > 1$. Then $|f(z)| = |a_n|R^n$ and
>
> $$
> |g(z)| \le |a_0| + |a_1|R + \cdots + |a_{n-1}|R^{n-1} \le \big(|a_0| + |a_1| + \cdots + |a_{n-1}|\big)R^{n-1} ,
> $$
>
> since $R > 1$. Hence
>
> $$
> \frac{|g(z)|}{|f(z)|} \le \frac{|a_0| + |a_1| + \cdots + |a_{n-1}|}{|a_n|R} < 1
> $$
>
> if, in addition to being greater than $1$,
>
> $$
> R > \frac{|a_0| + |a_1| + \cdots + |a_{n-1}|}{|a_n|} . \qquad (4)
> $$
>
> For such $R$, Rouché's theorem says that $f$ and $f + g = P$ have the same number of zeros in $|z| < R$, namely $n$ (the zero of order $n$ of $a_nz^n$ at the origin). This holds for every $R > R^* = \max\big(1, (|a_0| + \cdots + |a_{n-1}|)/|a_n|\big)$. (B&C leaves the last step implicit; here it is.) Fix $R_1 > R^*$; $P$ has $n$ zeros in $|z| < R_1$. If $z_1$ is any zero of $P$, choose $R > \max(R_1, |z_1|)$: the disk $|z| < R$ also contains exactly $n$ zeros, and these include the $n$ zeros in $|z| < R_1$, so they are the same zeros and $z_1$ is one of them. Hence $P$ has precisely $n$ zeros in the plane, all in $|z| \le R^*$.
>
> Liouville's theorem ([[§58 Liouville's Theorem and the Fundamental Theorem of Algebra#^thm-58-1|Theorem §58.1]]) only ensured at least one zero; Rouché's theorem gives $n$ directly, and also the bound (4) for their location.
>
> *B&C: Sec. 94, Example 2*

^ex-94-2

> [!remark]- Connections
> - Other proofs of the fundamental theorem of algebra in the vault: the topological one by winding numbers, [[§25 The Fundamental Theorem of Algebra#^thm-25-1|590 Thm. §25.1]] (hub: [[Fundamental Theorem of Algebra (topological proof)]]), which is the same idea as Example §94.2 with $\pi_1(S^1)$ in place of the argument principle; and the statement used in linear algebra, [[§13 Polynomials#^ladr-4-12|LADR 4.12]].

> [!example] Example §94.3: Counting Zeros in |z| < 2
> Determine the number of zeros, counting multiplicities, inside the circle $|z| = 2$ of
>
> $$
> \text{(a)}\ z^4 - 2z^3 + 9z^2 + z - 1, \qquad \text{(b)}\ z^5 + 3z^3 + z^2 + 1 .
> $$
>
> **(a)** On $|z| = 2$ the terms have moduli $16$, $16$, $36$, $2$, $1$; the dominant one is $9z^2$. With $f = 9z^2$, $g = z^4 - 2z^3 + z - 1$: $|f| = 36$ and $|g| \le 16 + 16 + 2 + 1 = 35 < 36$. So there are **2** zeros in $|z| < 2$.
>
> **(b)** With $f = z^5$, $g = 3z^3 + z^2 + 1$: $|f| = 32$ and $|g| \le 24 + 4 + 1 = 29 < 32$. So all **5** zeros lie in $|z| < 2$.
>
> Both agree with B&C's answers and with the computed roots (moduli $0.289$, $0.373$, $3.047$, $3.047$ in (a); all five of modulus less than $1.74$ in (b)).
>
> *B&C: Sec. 94, Exercise 7; Source: 342 HW 13*

^ex-94-3

> [!example] Example §94.4: Counting Zeros in an Annulus
> **(a)** Determine the number of roots, counting multiplicities, of $2z^5 - 6z^2 + z + 1 = 0$ in the annulus $1 \le |z| < 2$.
>
> *In $|z| < 2$:* $f = 2z^5$, $|f| = 64$; $g = -6z^2 + z + 1$, $|g| \le 24 + 2 + 1 = 27 < 64$. So $5$ roots.
>
> *In $|z| < 1$:* $f = -6z^2$, $|f| = 6$; $g = 2z^5 + z + 1$, $|g| \le 2 + 1 + 1 = 4 < 6$. So $2$ roots in $|z| < 1$, and, since $|f| > |g|$ on $|z| = 1$, none on that circle.
>
> Hence $5 - 2 = 3$ roots in $1 \le |z| < 2$ (B&C's answer; the computed moduli are $0.332$, $0.514$, $1.328$, $1.486$, $1.486$).
>
> **(b)** State Rouché's theorem and determine the number of zeros of $z^7 - 4z^3 + z - 1$ in the annulus $1 < |z| < 2$.
>
> *In $|z| < 1$:* $f = -4z^3$, $|f| = 4$; $g = z^7 + z - 1$, $|g| \le 3 < 4$. So $3$ zeros, none on $|z| = 1$ (B&C's Exercise 6(c)).
>
> *In $|z| < 2$:* $f = z^7$, $|f| = 128$; $g = -4z^3 + z - 1$, $|g| \le 32 + 2 + 1 = 35 < 128$. So $7$ zeros.
>
> Hence $7 - 3 = 4$ zeros in $1 < |z| < 2$. The key reaches the same count by the same comparisons, using the form $|f - h| < |f|$ of the hypothesis for $h = f + g$ (computed moduli: $0.569$, $0.569$, $0.792$ inside the unit disk and $1.314$, $1.401$, $1.456$, $1.456$ in the annulus).
>
> *B&C: Sec. 94, Exercise 8; Sec. 94, Exercise 6(c); Source: 342 HW 13, 342 practice final (Spring 2012), Q1*

^ex-94-4

> [!example] Example §94.5: The Equation czⁿ = eᶻ
> Show that if $c$ is a complex number with $|c| > e$, then the equation $cz^n = e^z$ has $n$ roots, counting multiplicities, inside the circle $|z| = 1$.
>
> Let $f(z) = cz^n$ and $g(z) = -e^z$, both entire. On $|z| = 1$, $z = x + iy$ with $x \le 1$, so
>
> $$
> |f(z)| = |c| > e \ge e^x = |e^z| = |g(z)| .
> $$
>
> By Rouché's theorem $f + g = cz^n - e^z$ has as many zeros in $|z| < 1$ as $cz^n$, namely $n$ (a zero of order $n$ at $0$; note $c \ne 0$). So $cz^n = e^z$ has $n$ roots there. (For instance, $3z^3 = e^z$ has the three roots $0.952$ and $-0.384 \pm 0.474i$ in the unit disk.)
>
> *B&C: Sec. 94, Exercise 9; Source: 342 HW 13*

^ex-94-5
