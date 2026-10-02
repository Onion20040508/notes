---
type: section
subject: "[[Complex Variables]]"
chapter: 7
section: 85
bc: "85"
aliases: ["B&C 85"]
tags: [complex-variables, math342]
---
← [[§84 Behavior of Functions Near Isolated Singular Points]] · ↑ [[· 7 Applications of Residues]] · [[§86 Example (Evaluation of Improper Integrals)]] →

*Brown–Churchill, Section 85.*

Chapter 7 turns the residue theorem into a tool of real analysis. This section first fixes what an improper integral over the whole line means and separates it from its Cauchy principal value, a symmetric limit that can exist when the integral itself diverges. It then describes the basic method: integrate a rational function $p/q$ around a large semicircle in the upper half plane, so that the integral along the real axis equals $2\pi i$ times the sum of the residues at the zeros of $q$ above the axis, minus an arc integral that disappears as the radius grows. The method evaluates integrals for which no elementary antiderivative is in sight, and it is the model for every contour argument in the chapter.

## Improper Integrals and Principal Values

> [!definition] Definition §85.1: Improper Integrals over Infinite Intervals
> If $f(x)$ is continuous for $0 \le x < \infty$, its **improper integral** over that interval is
>
> $$
> \int_0^\infty f(x)\,dx = \lim_{R\to\infty}\int_0^R f(x)\,dx ; \qquad (1)
> $$
>
> when the limit exists, the integral **converges** to it. If $f(x)$ is continuous for all $x$, its improper integral over $-\infty < x < \infty$ is
>
> $$
> \int_{-\infty}^{\infty} f(x)\,dx = \lim_{R_1\to\infty}\int_{-R_1}^{0} f(x)\,dx + \lim_{R_2\to\infty}\int_0^{R_2} f(x)\,dx , \qquad (2)
> $$
>
> and it converges to the sum when **both** limits exist; $R_1$ and $R_2$ tend to infinity independently.
>
> *B&C: Sec. 85 (text)*

^def-85-1

> [!remark]- Connections
> - The rigorous definitions: [[§36 Improper Integrals#^def-36-1|451 Def. §36.1]] (half-open intervals) and [[§36 Improper Integrals#^def-36-2|451 Def. §36.2]] (doubly improper integrals, with the same independent limits as in (2)); computational version [[§51 Improper Integrals#^def-51-1|Calc Def. §51.1]].

> [!definition] Definition §85.2: Cauchy Principal Value
> The **Cauchy principal value** (P.V.) of the integral (2) is the number
>
> $$
> \text{P.V.}\int_{-\infty}^{\infty} f(x)\,dx = \lim_{R\to\infty}\int_{-R}^{R} f(x)\,dx , \qquad (3)
> $$
>
> provided this single limit exists.
>
> *B&C: Sec. 85 (text)*

^def-85-2

> [!theorem] Proposition §85.1: A Convergent Integral Equals Its Principal Value
> If the improper integral (2) converges, then its Cauchy principal value (3) exists, and the two are equal.
>
> *B&C: Sec. 85 (text)*

^prop-85-1

> [!proof]+ Proof
> For every $R > 0$, $\int_{-R}^{R} f = \int_{-R}^{0} f + \int_0^{R} f$. As $R \to \infty$ each of the two terms on the right has a limit, namely the limits in (2) (a limit along $R_1 = R$, $R_2 = R$ is a special case of letting $R_1$ and $R_2$ tend to infinity separately). So
>
> $$
> \lim_{R\to\infty}\int_{-R}^{R} f(x)\,dx = \lim_{R\to\infty}\int_{-R}^{0} f(x)\,dx + \lim_{R\to\infty}\int_0^{R} f(x)\,dx ,
> $$
>
> and the right side is the value of (2).

^pf-85-1

*Uses:* [[§85 Evaluation of Improper Integrals#^def-85-1|Def. §85.1]], [[§85 Evaluation of Improper Integrals#^def-85-2|Def. §85.2]]

The converse fails.

> [!example] Example §85.1: A Principal Value Without an Integral
> For $f(x) = x$,
>
> $$
> \text{P.V.}\int_{-\infty}^{\infty} x\,dx = \lim_{R\to\infty}\int_{-R}^{R} x\,dx = \lim_{R\to\infty}\Big[\frac{x^2}{2}\Big]_{-R}^{R} = \lim_{R\to\infty} 0 = 0 . \qquad (4)
> $$
>
> On the other hand,
>
> $$
> \lim_{R_1\to\infty}\int_{-R_1}^{0} x\,dx + \lim_{R_2\to\infty}\int_0^{R_2} x\,dx = -\lim_{R_1\to\infty}\frac{R_1^2}{2} + \lim_{R_2\to\infty}\frac{R_2^2}{2} , \qquad (5)
> $$
>
> and neither limit exists, so the improper integral (5) diverges. The principal value $0$ comes only from the exact cancellation of the odd integrand over symmetric intervals.
>
> *B&C: Sec. 85, Example*

^ex-85-1

> [!remark]- Connections
> - The same phenomenon for $\sin x$: [[§36 Improper Integrals#^ex-36-3|451 Ex. §36.3]], which explains why the doubly improper integral is defined with independent endpoints.

For even functions the two notions agree.

> [!theorem] Proposition §85.2: Even Integrands
> Let $f(x)$ be continuous for all $x$ and **even**, $f(-x) = f(x)$, and suppose that the principal value (3) exists. Then the integral (2) converges, and
>
> $$
> \int_{-\infty}^{\infty} f(x)\,dx = \text{P.V.}\int_{-\infty}^{\infty} f(x)\,dx , \qquad (6)
> $$
>
> $$
> \int_0^{\infty} f(x)\,dx = \frac12\Big[\text{P.V.}\int_{-\infty}^{\infty} f(x)\,dx\Big] . \qquad (7)
> $$
>
> *B&C: Sec. 85, equations (6)–(7)*

^prop-85-2

> [!proof]+ Proof
> The substitution $x \mapsto -x$ and $f(-x) = f(x)$ give $\int_{-R}^{0} f(x)\,dx = \int_0^{R} f(x)\,dx$ for every $R > 0$; hence (the symmetry of the graph about the $y$ axis)
>
> $$
> \int_{-R_1}^{0} f(x)\,dx = \frac12\int_{-R_1}^{R_1} f(x)\,dx \qquad\text{and}\qquad \int_0^{R_2} f(x)\,dx = \frac12\int_{-R_2}^{R_2} f(x)\,dx .
> $$
>
> As $R_1 \to \infty$ and $R_2 \to \infty$, independently, each right side tends to $\frac12\,\text{P.V.}\int_{-\infty}^{\infty} f$, because the principal value exists. So both limits in (2) exist, and their sum is the principal value: this is (6). The second identity, read with $R_2 = R$, says $\int_0^{R} f = \frac12\int_{-R}^{R} f$; letting $R \to \infty$ gives (7).

^pf-85-2

*Uses:* [[§85 Evaluation of Improper Integrals#^def-85-1|Def. §85.1]], [[§85 Evaluation of Improper Integrals#^def-85-2|Def. §85.2]]

## The Method of Residues

The method applies to **rational functions** $f(x) = p(x)/q(x)$, where $p$ and $q$ are polynomials with real coefficients and no factors in common, and $q$ has no real zeros but at least one zero above the real axis. The distinct zeros of $q$ above the axis are finite in number (a nonzero polynomial has at most $\deg q$ zeros, [[§58 Liouville's Theorem and the Fundamental Theorem of Algebra#^cor-58-4|Corollary §58.4]]); label them $z_1, z_2, \ldots, z_n$. Integrate

$$
f(z) = \frac{p(z)}{q(z)} \qquad (8)
$$

around the positively oriented boundary of the half disk $|z| \le R$, $\operatorname{Im} z \ge 0$: the segment from $z = -R$ to $z = R$ followed by the upper half $C_R$ of the circle $|z| = R$, described counterclockwise, with $R$ so large that all the $z_k$ lie inside.

> [!theorem] Theorem §85.3: Improper Integrals of Rational Functions by Residues
> Let $f = p/q$ be as just described, and let $R > |z_k|$ for $k = 1, \ldots, n$. Then
>
> $$
> \int_{-R}^{R} f(x)\,dx = 2\pi i\sum_{k=1}^{n}\operatorname{Res}_{z=z_k} f(z) - \int_{C_R} f(z)\,dz . \qquad (9)
> $$
>
> If $\lim_{R\to\infty}\int_{C_R} f(z)\,dz = 0$, then
>
> $$
> \text{P.V.}\int_{-\infty}^{\infty} f(x)\,dx = 2\pi i\sum_{k=1}^{n}\operatorname{Res}_{z=z_k} f(z) ; \qquad (10)
> $$
>
> and if in addition $f$ is even,
>
> $$
> \int_{-\infty}^{\infty} f(x)\,dx = 2\pi i\sum_{k=1}^{n}\operatorname{Res}_{z=z_k} f(z) \qquad (11)
> $$
>
> and
>
> $$
> \int_0^{\infty} f(x)\,dx = \pi i\sum_{k=1}^{n}\operatorname{Res}_{z=z_k} f(z) . \qquad (12)
> $$
>
> *B&C: Sec. 85, equations (9)–(12)*

^thm-85-3

> [!proof]+ Proof
> As a quotient of polynomials, $f$ is analytic except at the zeros of $q$, which are isolated singular points. None lies on the closed contour $C$ formed by the segment and $C_R$: the segment is real and $q$ has no real zeros, and every zero of $q$ in the upper half plane has modulus less than $R$. Inside $C$ lie exactly $z_1, \ldots, z_n$ (the zeros of $q$ below the axis are outside). Cauchy's residue theorem ([[§76 Cauchy's Residue Theorem#^thm-76-1|Theorem §76.1]]) gives
>
> $$
> \int_{\text{segment}} f(z)\,dz + \int_{C_R} f(z)\,dz = 2\pi i\sum_{k=1}^{n}\operatorname{Res}_{z=z_k} f(z) .
> $$
>
> With the parametrization $z = x$ $(-R \le x \le R)$ of the segment, $z'(x) = 1$, the first integral is $\int_{-R}^{R} f(x)\,dx$ ([[§44 Contour Integrals#^def-44-1|Definition §44.1]]), and (9) follows.
>
> The right side of (9) is a constant minus $\int_{C_R} f$. If the arc integral tends to $0$, the right side tends to $2\pi i\sum\operatorname{Res}$, so $\lim_{R\to\infty}\int_{-R}^{R} f(x)\,dx$ exists and equals it: this is (10). If $f$ is even, Proposition §85.2 turns (10) into (11) and (12).

^pf-85-3

*Uses:* [[§85 Evaluation of Improper Integrals#^def-85-2|Def. §85.2]], [[§85 Evaluation of Improper Integrals#^prop-85-2|§85.2]], [[§76 Cauchy's Residue Theorem#^thm-76-1|§76.1]], [[§44 Contour Integrals#^def-44-1|Def. §44.1]], [[§58 Liouville's Theorem and the Fundamental Theorem of Algebra#^cor-58-4|§58.4]]

![[m342-85-1.svg]]
*The closed contour of Theorem §85.3: the segment $[-R, R]$ and the semicircle $C_R$. Since $q$ has real coefficients, its zeros come in conjugate pairs $z_k$, $\bar z_k$; the contour encloses the ones above the axis (red) once $R$ exceeds their moduli, and none of the ones below (gray).*

Whether the arc integral tends to zero depends only on the degrees. B&C checks it case by case with the bound of [[§47 Upper Bounds for Moduli of Contour Integrals#^thm-47-2|Theorem §47.2]]; here is the general statement, the criterion "$\deg q \ge \deg p + 2$" that the old-final keys quote ([[§86 Example (Evaluation of Improper Integrals)#^ex-86-4|Example §86.4]]).

> [!theorem] Proposition §85.4: The Degree Condition
> Let $f = p/q$ be as above, and suppose $\deg q \ge \deg p + 2$. Then there are constants $K$ and $R_1 \ge 1$ such that
>
> $$
> |f(z)| \le \frac{K}{|z|^2} \qquad\text{whenever } |z| \ge R_1 .
> $$
>
> Consequently $\lim_{R\to\infty}\int_{C_R} f(z)\,dz = 0$, the improper integral (2) converges (absolutely), and
>
> $$
> \int_{-\infty}^{\infty} f(x)\,dx = 2\pi i\sum_{k=1}^{n}\operatorname{Res}_{z=z_k} f(z) ,
> $$
>
> whether or not $f$ is even.
>
> *B&C: Sec. 86 (text), stated in general*

^prop-85-4

> [!proof]+ Proof
> Write $p(z) = \sum_{j=0}^{m} a_jz^j$ and $q(z) = \sum_{j=0}^{N} b_jz^j$ with $b_N \ne 0$ and $N \ge m + 2$. Let $A = \sum_j|a_j|$ and $B = \sum_{j<N}|b_j|$. For $|z| = r \ge 1$, the triangle inequality gives
>
> $$
> |p(z)| \le Ar^m, \qquad |q(z)| \ge |b_N|r^N - \sum_{j<N}|b_j|r^j \ge |b_N|r^N - Br^{N-1} .
> $$
>
> If also $r \ge 2B/|b_N|$, then $Br^{N-1} \le \frac12|b_N|r^N$ and $|q(z)| \ge \frac12|b_N|r^N$. So for $r \ge R_1 = \max(1, 2B/|b_N|)$,
>
> $$
> |f(z)| \le \frac{2A}{|b_N|}\,r^{m-N} \le \frac{K}{r^2}, \qquad K = \frac{2A}{|b_N|},
> $$
>
> since $m - N \le -2$ and $r \ge 1$.
>
> **The arc.** For $R \ge R_1$, $|f| \le K/R^2$ on $C_R$, whose length is $\pi R$; by [[§47 Upper Bounds for Moduli of Contour Integrals#^thm-47-2|Theorem §47.2]], $\big|\int_{C_R} f(z)\,dz\big| \le \pi K/R \to 0$.
>
> **Convergence.** On the real axis $f$ is real and continuous ($q$ has no real zeros), and $|f(x)| \le K/x^2$ for $|x| \ge R_1$. Since $\int_{R_1}^{\infty} K\,x^{-2}\,dx$ converges, the comparison theorem shows that $\int_{R_1}^{\infty}|f|$ converges, and then so does $\int_{R_1}^{\infty} f$ (apply comparison to $0 \le f + |f| \le 2|f|$ and subtract $|f|$). With the proper integral over $[0, R_1]$, $\int_0^{\infty} f$ converges; likewise $\int_{-\infty}^{0} f$. So (2) converges, by Proposition §85.1 its value is the principal value, and Theorem §85.3, (10), gives the residue sum.

^pf-85-4

*Uses:* [[§85 Evaluation of Improper Integrals#^prop-85-1|§85.1]], [[§85 Evaluation of Improper Integrals#^thm-85-3|§85.3]], [[§47 Upper Bounds for Moduli of Contour Integrals#^thm-47-2|§47.2]], [[§5 Triangle Inequality#^cor-5-2|§5.2]], [[§5 Triangle Inequality#^cor-5-3|§5.3]], [[§51 Improper Integrals#^thm-51-2|Calc Thm. §51.2]] (comparison)

> [!remark] Remark: Method — Improper Integrals of Rational Functions
> To evaluate $\int_{-\infty}^{\infty} p(x)/q(x)\,dx$ (or $\int_0^\infty$ of an even one):
> 1. **Check the hypotheses.** $q$ has no real zeros and $\deg q \ge \deg p + 2$; then the integral converges and the arc integral vanishes in the limit (Proposition §85.4). Otherwise bound $\int_{C_R}$ directly with $|q(z)| \ge \big||z|^N - \cdots\big|$ and the length $\pi R$.
> 2. **Find the zeros of $q$ in the upper half plane**, by the roots of complex numbers ([[§10 Roots of Complex Numbers#^thm-10-2|Theorem §10.2]]) or the quadratic formula.
> 3. **Compute the residues** of $p/q$ there: at a simple zero, $p(z_k)/q'(z_k)$ ([[§83 Zeros and Poles#^thm-83-2|Theorem §83.2]]); at a pole of order $m$, $\phi^{(m-1)}(z_k)/(m-1)!$ with $\phi = (z - z_k)^mf$ ([[§80 Residues at Poles#^thm-80-1|Theorem §80.1]]).
> 4. **Assemble** $2\pi i\sum\operatorname{Res}$; for an even integrand over $0 < x < \infty$ take half, $\pi i\sum\operatorname{Res}$.
> 5. **Check:** the answer must be real (and positive for a positive integrand).

^rem-85-1

## Examples

> [!example] Example §85.2: A Double Pole
> Show that $\displaystyle\int_0^\infty\frac{x^2\,dx}{(x^2 + 9)(x^2 + 4)^2} = \frac{\pi}{200}$.
>
> **Zeros.** $q(z) = (z^2 + 9)(z^2 + 4)^2$ has no real zeros; above the axis it has the simple zero $3i$ and the zero $2i$ of order $2$. Since $\deg q = 6 \ge 2 + 2$, Proposition §85.4 applies, and the integrand is even, so (12) holds.
>
> **The simple pole $3i$.** With $\phi(z) = z^2/\big((z + 3i)(z^2 + 4)^2\big)$,
>
> $$
> \operatorname{Res}_{z=3i} f(z) = \phi(3i) = \frac{-9}{6i\cdot(-5)^2} = -\frac{3}{50i} = \frac{3i}{50} .
> $$
>
> **The double pole $2i$.** Here $f(z) = \phi(z)/(z - 2i)^2$ with $\phi(z) = \dfrac{z^2}{(z^2 + 9)(z + 2i)^2}$, analytic and nonzero at $2i$, so the residue is $\phi'(2i)$ ([[§80 Residues at Poles#^thm-80-1|Theorem §80.1]]). The logarithmic derivative is the quickest route:
>
> $$
> \frac{\phi'(z)}{\phi(z)} = \frac2z - \frac{2z}{z^2 + 9} - \frac{2}{z + 2i}, \qquad \phi(2i) = \frac{-4}{5\cdot(4i)^2} = \frac{1}{20}, \qquad \frac{\phi'(2i)}{\phi(2i)} = \frac{2}{2i} - \frac{4i}{5} - \frac{2}{4i} = -i - \frac{4i}{5} + \frac i2 = -\frac{13i}{10} ,
> $$
>
> so $\operatorname{Res}_{z=2i} f(z) = \phi'(2i) = -\dfrac{13i}{200}$.
>
> **Conclusion.** The sum of the residues is $\frac{12i}{200} - \frac{13i}{200} = -\frac{i}{200}$, and by (12)
>
> $$
> \int_0^\infty\frac{x^2\,dx}{(x^2 + 9)(x^2 + 4)^2} = \pi i\Big(-\frac{i}{200}\Big) = \frac{\pi}{200} \approx 0.0157080 ,
> $$
>
> as quadrature confirms. (Directly, the arc bound is $\pi R^3/\big((R^2 - 9)(R^2 - 4)^2\big) \to 0$ for $R > 3$.) The same arc estimate for $z^2/(1 + z^4)$, an old-final problem, is [[§47 Upper Bounds for Moduli of Contour Integrals#^ex-47-5|Example §47.5]](b).
>
> *B&C: Sec. 86, Exercise 6*

^ex-85-2

> [!example] Example §85.3: Principal Values Without Symmetry
> Use residues to find the Cauchy principal values of
>
> $$
> \text{(a)}\ \int_{-\infty}^{\infty}\frac{dx}{x^2 + 2x + 2}, \qquad \text{(b)}\ \int_{-\infty}^{\infty}\frac{x\,dx}{(x^2 + 1)(x^2 + 2x + 2)} .
> $$
>
> Neither integrand is even, so formula (10) is the one to use; in both cases $\deg q \ge \deg p + 2$, so by Proposition §85.4 the integrals converge and the principal values are their values.
>
> **(a)** $z^2 + 2z + 2 = (z + 1)^2 + 1$ has the zeros $-1 \pm i$; only $z_1 = -1 + i$ is above the axis, and it is a simple zero. By [[§83 Zeros and Poles#^thm-83-2|Theorem §83.2]],
>
> $$
> \operatorname{Res}_{z=-1+i}\frac{1}{z^2 + 2z + 2} = \frac{1}{2z + 2}\Big|_{z=-1+i} = \frac{1}{2i}, \qquad \text{P.V.}\int_{-\infty}^{\infty}\frac{dx}{x^2 + 2x + 2} = 2\pi i\cdot\frac{1}{2i} = \pi .
> $$
>
> (Check: $\int\frac{dx}{(x + 1)^2 + 1} = \tan^{-1}(x + 1)$, which increases by $\pi$ over the line.)
>
> **(b)** Now $q(z) = (z^2 + 1)(z^2 + 2z + 2)$ has the simple zeros $i$ and $-1 + i$ above the axis. With $f(z) = z/q(z)$:
>
> $$
> \operatorname{Res}_{z=i} f(z) = \frac{i}{2i\,(i^2 + 2i + 2)} = \frac{1}{2(1 + 2i)} = \frac{1 - 2i}{10} ,
> $$
>
> and, using $(-1 + i)^2 = -2i$,
>
> $$
> \operatorname{Res}_{z=-1+i} f(z) = \frac{z}{(z^2 + 1)(2z + 2)}\Big|_{z=-1+i} = \frac{-1 + i}{(1 - 2i)(2i)} = \frac{-1 + i}{4 + 2i} = \frac{-1 + 3i}{10} .
> $$
>
> The sum is $\frac{i}{10}$, so
>
> $$
> \text{P.V.}\int_{-\infty}^{\infty}\frac{x\,dx}{(x^2 + 1)(x^2 + 2x + 2)} = 2\pi i\cdot\frac{i}{10} = -\frac\pi5 ,
> $$
>
> B&C's answer. Numerical quadrature confirms both values ($3.14159\ldots$ and $-0.62832\ldots$).
>
> *B&C: Sec. 86, Exercises 7 and 8*

^ex-85-3
