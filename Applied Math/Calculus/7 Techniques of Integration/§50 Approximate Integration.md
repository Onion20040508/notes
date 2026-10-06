---
type: section
subject: "[[Calculus]]"
chapter: 7
section: 50
stewart: "7.7"
aliases: ["Stewart 7.7"]
tags: [calculus]
---
← [[§49 Integration Using Tables and Technology]] · ↑ [[· 7 Techniques of Integration]] · [[§51 Improper Integrals]] →

*Stewart, Section 7.7.*

The exact value of a definite integral is out of reach in two situations: when no antiderivative can be found, as for $\int_0^1 e^{x^2}\,dx$ or $\int_{-1}^1 \sqrt{1 + x^3}\,dx$ ([[§48 Strategy for Integration#^thm-48-2|Theorem §48.2]]), and when the integrand is known only from measured data. Then one approximates. Any Riemann sum is an approximation. Better ones replace the graph on each subinterval by a horizontal segment at the midpoint (Midpoint Rule), by a chord (Trapezoidal Rule), or by a parabola through three points (Simpson's Rule). Error bounds in terms of $f''$ or $f^{(4)}$ say how large $n$ must be for a given accuracy. Simpson's Rule, whose error decreases like $1/n^4$, is by far the most accurate of the three.

Throughout, $[a, b]$ is divided into $n$ subintervals of equal length $\Delta x = (b - a)/n$, with endpoints $x_i = a + i\,\Delta x$ ($i = 0, 1, \ldots, n$).

## Endpoint, Midpoint and Trapezoidal Approximations

> [!definition] Definition §50.1: Left and Right Endpoint Approximations
> Taking $x_i^{\ast}$ in $\int_a^b f(x)\,dx \approx \sum_{i=1}^n f(x_i^{\ast})\,\Delta x$ to be the left or right endpoint of $[x_{i-1}, x_i]$ gives the **left endpoint approximation** $L_n$ and the **right endpoint approximation** $R_n$:
>
> $$
> \int_a^b f(x)\,dx \approx L_n = \sum_{i=1}^n f(x_{i-1})\,\Delta x \qquad (1) \qquad\qquad \int_a^b f(x)\,dx \approx R_n = \sum_{i=1}^n f(x_i)\,\Delta x \qquad (2)
> $$
>
> *Stewart: 7.7, Equations 1 and 2*

^def-50-1

> [!remark]- Connections
> - These are Riemann sums ([[§35 The Definite Integral#^def-35-new1|Def. §35.2]]); in 451 the integral is the limit of such sums as the mesh tends to $0$, [[§32 The Definition of the Riemann Integral#^def-32-3|451 Def. §32.3]], so for an integrable $f$ every rule of this section converges to $\int_a^b f$ as $n \to \infty$. The error bounds below add a *rate*.

> [!definition] Definition §50.2: The Midpoint Rule
> $$
> \int_a^b f(x)\,dx \approx M_n = \Delta x\,\big[f(\bar x_1) + f(\bar x_2) + \cdots + f(\bar x_n)\big] ,
> $$
>
> where $\bar x_i = \frac12 (x_{i-1} + x_i)$ is the midpoint of $[x_{i-1}, x_i]$.
>
> *Stewart: 7.7, Midpoint Rule*

^def-50-2

> [!definition] Definition §50.3: The Trapezoidal Rule
> $$
> \int_a^b f(x)\,dx \approx T_n = \frac{\Delta x}{2}\big[f(x_0) + 2f(x_1) + 2f(x_2) + \cdots + 2f(x_{n-1}) + f(x_n)\big] .
> $$
>
> *Stewart: 7.7, Trapezoidal Rule*

^def-50-3

> [!remark]- Connections
> - See also: [[§13★ Numerical Determination of Fourier Coefficients#^def-13-1|341 Def. §13.1]] (the trapezoidal rule applied to the Fourier coefficients of a periodic function; over a full period it is far more accurate than the general error bound suggests).

> [!remark] Remark: Where the Trapezoidal Rule Comes From
> $T_n$ is the average of $L_n$ and $R_n$:
>
> $$
> \frac12\Big[\sum_{i=1}^n f(x_{i-1})\,\Delta x + \sum_{i=1}^n f(x_i)\,\Delta x\Big] = \frac{\Delta x}{2}\sum_{i=1}^n \big(f(x_{i-1}) + f(x_i)\big) = \frac{\Delta x}{2}\big[f(x_0) + 2f(x_1) + \cdots + 2f(x_{n-1}) + f(x_n)\big] ,
> $$
>
> since every interior point $x_1, \ldots, x_{n-1}$ is the right end of one subinterval and the left end of the next. When $f \ge 0$, the term $\frac{\Delta x}{2}\big(f(x_{i-1}) + f(x_i)\big)$ is the area of the trapezoid above $[x_{i-1}, x_i]$ under the chord joining $(x_{i-1}, f(x_{i-1}))$ and $(x_i, f(x_i))$: the graph is replaced by a broken line.

^rem-50-1

> [!example] Example §50.1: Trapezoidal and Midpoint Rules for ln 2
> Use (a) the Trapezoidal Rule and (b) the Midpoint Rule with $n = 5$ to approximate $\displaystyle\int_1^2 \frac1x\,dx$.
>
> Here $\Delta x = (2 - 1)/5 = 0.2$.
>
> **(a)**
>
> $$
> T_5 = \frac{0.2}{2}\big[f(1) + 2f(1.2) + 2f(1.4) + 2f(1.6) + 2f(1.8) + f(2)\big] = 0.1\Big(\frac11 + \frac{2}{1.2} + \frac{2}{1.4} + \frac{2}{1.6} + \frac{2}{1.8} + \frac12\Big) \approx 0.695635 .
> $$
>
> **(b)** The midpoints are $1.1, 1.3, 1.5, 1.7, 1.9$:
>
> $$
> M_5 = 0.2\big[f(1.1) + f(1.3) + f(1.5) + f(1.7) + f(1.9)\big] = \frac15\Big(\frac{1}{1.1} + \frac{1}{1.3} + \frac{1}{1.5} + \frac{1}{1.7} + \frac{1}{1.9}\Big) \approx 0.691908 .
> $$
>
> The exact value is $\int_1^2 \frac{dx}{x} = \ln x\Big]_1^2 = \ln 2 = 0.693147\ldots$
>
> *Stewart: Example 7.7.1*

^ex-50-1

## Error Bounds for the Midpoint and Trapezoidal Rules

> [!definition] Definition §50.4: Error of an Approximation
> The **error** of an approximation is the amount that must be added to it to make it exact:
>
> $$
> E_T = \int_a^b f(x)\,dx - T_n \qquad\text{and}\qquad E_M = \int_a^b f(x)\,dx - M_n ,
> $$
>
> and similarly $E_L$, $E_R$ and, below, $E_S$.
>
> *Stewart: 7.7 (text)*

^def-50-4

In Example §50.1, $E_T \approx -0.002488$ and $E_M \approx 0.001239$. Repeating the computation for more values of $n$:

| $n$ | $L_n$ | $R_n$ | $T_n$ | $M_n$ | $E_L$ | $E_R$ | $E_T$ | $E_M$ |
|---|---|---|---|---|---|---|---|---|
| 5 | 0.745635 | 0.645635 | 0.695635 | 0.691908 | $-0.052488$ | $0.047512$ | $-0.002488$ | $0.001239$ |
| 10 | 0.718771 | 0.668771 | 0.693771 | 0.692835 | $-0.025624$ | $0.024376$ | $-0.000624$ | $0.000312$ |
| 20 | 0.705803 | 0.680803 | 0.693303 | 0.693069 | $-0.012656$ | $0.012344$ | $-0.000156$ | $0.000078$ |

> [!remark] Remark: What the Tables Show
> These observations hold in most cases.
> 1. Every method becomes more accurate as $n$ increases. (But very large $n$ means so many arithmetic operations that accumulated round-off error becomes a concern.)
> 2. The errors of $L_n$ and $R_n$ have opposite signs and are roughly halved when $n$ is doubled.
> 3. The Trapezoidal and Midpoint Rules are much more accurate than the endpoint approximations.
> 4. The errors of $T_n$ and $M_n$ have opposite signs and are divided by about $4$ when $n$ is doubled.
> 5. The error of the Midpoint Rule is about half that of the Trapezoidal Rule.
>
> **Why the midpoint wins** (figure below). On $[x_{i-1}, x_i]$ the midpoint rectangle has the same area as the trapezoid $ABCD$ whose top side is tangent to the graph at $P = (\bar x_i, f(\bar x_i))$: tilting the top about $P$ adds as much area on one side as it removes on the other. The tangent stays closer to the graph than the chord $QR$ of the trapezoid $AQRD$ used by the Trapezoidal Rule. For a graph that bends one way, the tangent lies on one side of the graph and the chord on the other, which is why $E_T$ and $E_M$ have opposite signs.

^rem-50-2

![[m233-50-1.svg]]
*One subinterval of a concave-down graph. The Midpoint Rule's rectangle has the same area as the tangent trapezoid $ABCD$, which overestimates by the red area. The Trapezoidal Rule's trapezoid $AQRD$ underestimates by the blue area, which is larger. Both errors are governed by how much the graph bends, that is, by $f''$.*

> [!theorem] Theorem §50.1: Error Bounds for the Trapezoidal and Midpoint Rules
> Suppose $|f''(x)| \le K$ for $a \le x \le b$. If $E_T$ and $E_M$ are the errors in the Trapezoidal and Midpoint Rules, then
>
> $$
> |E_T| \le \frac{K(b - a)^3}{12n^2} \qquad\text{and}\qquad |E_M| \le \frac{K(b - a)^3}{24n^2} .
> $$
>
> *Stewart: 7.7, Theorem 3*

^thm-50-1

*Stewart omits the proof ("proved in books on numerical analysis"); no note in the vault proves it. The $n^2$ in the denominator explains observation 4 ($(2n)^2 = 4n^2$), and the factor $f''$ measures how much the graph bends.*

$K$ can be any number at least as large as all the values of $|f''(x)|$, but smaller $K$ gives better bounds. The bound is a worst case: the actual error can be much smaller.

> [!example] Example §50.2: Choosing n for a Given Accuracy
> **(a)** Bound the error of $T_5$ in Example §50.1. **(b)** How large should $n$ be to guarantee that $T_n$ and $M_n$ approximate $\int_1^2 \frac1x\,dx$ to within $0.0001$?
>
> **(a)** For $f(x) = 1/x$, $f'(x) = -1/x^2$ and $f''(x) = 2/x^3$. On $1 \le x \le 2$, $1/x \le 1$, so $|f''(x)| = 2/x^3 \le 2/1^3 = 2$. With $K = 2$, $a = 1$, $b = 2$, $n = 5$,
>
> $$
> |E_T| \le \frac{2(2 - 1)^3}{12(5)^2} = \frac{1}{150} \approx 0.006667 ,
> $$
>
> substantially more than the actual error $0.002488$.
>
> **(b)** For the Trapezoidal Rule we need $\dfrac{2(1)^3}{12n^2} < 0.0001$, that is, $n^2 > \dfrac{2}{12(0.0001)}$, so
>
> $$
> n > \frac{1}{\sqrt{0.0006}} \approx 40.8 .
> $$
>
> So $n = 41$ guarantees the accuracy. (A smaller $n$ may well suffice, but $41$ is the smallest that the error bound can *guarantee*.) For the Midpoint Rule, $\dfrac{2(1)^3}{24n^2} < 0.0001$ gives $n > \dfrac{1}{\sqrt{0.0012}} \approx 28.9$, so $n = 29$.
>
> *Stewart: Example 7.7.2 and the text before it*

^ex-50-2

## Simpson's Rule

Simpson's Rule approximates the graph by parabolas instead of line segments. Now $n$ must be **even**, and on each pair of consecutive subintervals $[x_{i}, x_{i+2}]$ the curve is replaced by the parabola through the three points $P_i$, $P_{i+1}$, $P_{i+2}$ on the graph, where $P_i = (x_i, y_i)$ with $y_i = f(x_i)$. Write $h = \Delta x$.

> [!theorem] Lemma §50.2: Area Under a Parabola Through Three Points
> If the parabola $y = Ax^2 + Bx + C$ passes through $(-h, y_0)$, $(0, y_1)$ and $(h, y_2)$, then
>
> $$
> \int_{-h}^{h} (Ax^2 + Bx + C)\,dx = \frac{h}{3}(y_0 + 4y_1 + y_2) .
> $$
>
> The same holds for the parabola through three points with equally spaced $x$-coordinates $x_0$, $x_0 + h$, $x_0 + 2h$, integrated from $x_0$ to $x_0 + 2h$.
>
> *Stewart: 7.7 (text)*

^lem-50-2

> [!proof]+ Proof
> $Ax^2 + C$ is even and $Bx$ is odd, so by the symmetry rule for integrals ([[§38 The Substitution Rule#^thm-38-4|Theorem §38.4]], Stewart 5.5.7),
>
> $$
> \int_{-h}^{h} (Ax^2 + Bx + C)\,dx = 2\int_0^h (Ax^2 + C)\,dx = 2\Big[A\frac{x^3}{3} + Cx\Big]_0^h = 2\Big(A\frac{h^3}{3} + Ch\Big) = \frac{h}{3}(2Ah^2 + 6C) .
> $$
>
> Since the parabola passes through the three points,
>
> $$
> y_0 = A(-h)^2 + B(-h) + C = Ah^2 - Bh + C, \qquad y_1 = C, \qquad y_2 = Ah^2 + Bh + C ,
> $$
>
> so $y_0 + 4y_1 + y_2 = 2Ah^2 + 6C$, and the area is $\frac{h}{3}(y_0 + 4y_1 + y_2)$. Shifting a parabola horizontally does not change the area under it, which gives the second statement.

^pf-50-2

*Uses:* [[§38 The Substitution Rule#^thm-38-4|§38.4]] (integrals of even and odd functions)

> [!definition] Definition §50.5: Simpson's Rule
> For $n$ even,
>
> $$
> \int_a^b f(x)\,dx \approx S_n = \frac{\Delta x}{3}\big[f(x_0) + 4f(x_1) + 2f(x_2) + 4f(x_3) + \cdots + 2f(x_{n-2}) + 4f(x_{n-1}) + f(x_n)\big] .
> $$
>
> The coefficients follow the pattern $1, 4, 2, 4, 2, 4, \ldots, 4, 2, 4, 1$.
>
> *Stewart: 7.7, Simpson's Rule*

^def-50-5

> [!remark] Remark: Where Simpson's Rule Comes From
> By Lemma §50.2, the area under the parabola through $P_0, P_1, P_2$ from $x_0$ to $x_2$ is $\frac{h}{3}(y_0 + 4y_1 + y_2)$, the one through $P_2, P_3, P_4$ gives $\frac{h}{3}(y_2 + 4y_3 + y_4)$, and so on. Adding the $n/2$ pieces,
>
> $$
> \frac{h}{3}(y_0 + 4y_1 + y_2) + \frac{h}{3}(y_2 + 4y_3 + y_4) + \cdots + \frac{h}{3}(y_{n-2} + 4y_{n-1} + y_n) = \frac{h}{3}(y_0 + 4y_1 + 2y_2 + 4y_3 + 2y_4 + \cdots + 2y_{n-2} + 4y_{n-1} + y_n) :
> $$
>
> each even-indexed interior point is shared by two parabolas. The derivation pictures $f \ge 0$, but $S_n$ is a reasonable approximation for any continuous $f$. The rule is named after Thomas Simpson (1710–1761), a weaver who taught himself mathematics and popularized it in *Mathematical Dissertations* (1743); Cavalieri and Gregory knew it in the 17th century.

^rem-50-3

![[m233-50-2.svg]]
*Simpson's Rule with $n = 4$: on $[x_0, x_2]$ and on $[x_2, x_4]$ the graph (blue) is replaced by the parabola (red) through the three points above $x_0, x_1, x_2$ and $x_2, x_3, x_4$. The shaded area under the parabolas is $S_4$. Even for this wavy graph the parabolas follow it closely; for a smooth, slowly varying $f$ they are practically indistinguishable from it.*

> [!theorem] Proposition §50.3: Simpson's Rule as a Weighted Average
> $$
> S_{2n} = \tfrac13 T_n + \tfrac23 M_n .
> $$
>
> *Stewart: 7.7 (text; Exercise 50)*

^prop-50-3

> [!proof]+ Proof
> (Stewart leaves this as an exercise.) Let $\Delta x = (b - a)/n$, with endpoints $x_i$ and midpoints $\bar x_i$. The $2n$ subintervals of length $h = \Delta x/2$ have endpoints $x_0, \bar x_1, x_1, \bar x_2, x_2, \ldots, \bar x_n, x_n$, in which the midpoints $\bar x_i$ have odd index and the $x_i$ even index. So
>
> $$
> S_{2n} = \frac{h}{3}\Big[f(x_0) + 2\sum_{i=1}^{n-1} f(x_i) + f(x_n)\Big] + \frac{4h}{3}\sum_{i=1}^n f(\bar x_i) = \frac{\Delta x}{6}\Big[f(x_0) + 2\sum_{i=1}^{n-1} f(x_i) + f(x_n)\Big] + \frac{2\Delta x}{3}\sum_{i=1}^n f(\bar x_i) .
> $$
>
> The first term is $\frac13 \cdot \frac{\Delta x}{2}[\cdots] = \frac13 T_n$ and the second is $\frac23 \cdot \Delta x \sum f(\bar x_i) = \frac23 M_n$.

^pf-50-3

*Uses:* [[§50 Approximate Integration#^def-50-2|Def. §50.2]], [[§50 Approximate Integration#^def-50-3|Def. §50.3]], [[§50 Approximate Integration#^def-50-5|Def. §50.5]]

Since $E_T$ and $E_M$ usually have opposite signs and $|E_M| \approx \frac12 |E_T|$, this weighting nearly cancels the two errors. In Example §50.1 with $n = 5$: $\frac13(0.695635) + \frac23(0.691908) \approx 0.693150 = S_{10}$.

## Error Bound for Simpson's Rule

> [!theorem] Theorem §50.4: Error Bound for Simpson's Rule
> Suppose $|f^{(4)}(x)| \le K$ for $a \le x \le b$. If $E_S$ is the error in Simpson's Rule, then
>
> $$
> |E_S| \le \frac{K(b - a)^5}{180n^4} .
> $$
>
> *Stewart: 7.7, Theorem 4*

^thm-50-4

*Stewart omits the proof; no note in the vault proves it. The $n^4$ means that doubling $n$ divides the error by about $16$. Since $f^{(4)} = 0$ for a cubic, Simpson's Rule is exact for polynomials of degree at most $3$ (Exercise 48).*

> [!example] Example §50.3: Simpson's Rule for ln 2
> **(a)** Use Simpson's Rule with $n = 10$ to approximate $\displaystyle\int_1^2 \frac1x\,dx$. **(b)** How large should $n$ be to guarantee accuracy within $0.0001$?
>
> **(a)** $f(x) = 1/x$, $n = 10$, $\Delta x = 0.1$:
>
> $$
> \begin{aligned}
> S_{10} &= \frac{0.1}{3}\big[f(1) + 4f(1.1) + 2f(1.2) + 4f(1.3) + \cdots + 2f(1.8) + 4f(1.9) + f(2)\big] \\
> &= \frac{0.1}{3}\Big(\frac11 + \frac{4}{1.1} + \frac{2}{1.2} + \frac{4}{1.3} + \frac{2}{1.4} + \frac{4}{1.5} + \frac{2}{1.6} + \frac{4}{1.7} + \frac{2}{1.8} + \frac{4}{1.9} + \frac12\Big) \approx 0.693150 ,
> \end{aligned}
> $$
>
> much closer to $\ln 2 \approx 0.693147$ than $T_{10} \approx 0.693771$ or $M_{10} \approx 0.692835$; the error is about $-0.000003$.
>
> **(b)** $f^{(4)}(x) = 24/x^5$, and $x \ge 1$ gives $1/x \le 1$, so $|f^{(4)}(x)| \le 24$. With $K = 24$, we need
>
> $$
> \frac{24(1)^5}{180n^4} < 0.0001, \qquad\text{that is,}\qquad n^4 > \frac{24}{180(0.0001)}, \qquad n > \frac{1}{\sqrt[4]{0.00075}} \approx 6.04 .
> $$
>
> Since $n$ must be even, $n = 8$ suffices, against $n = 41$ for the Trapezoidal Rule and $n = 29$ for the Midpoint Rule (Example §50.2).
>
> | $n$ | $M_n$ | $S_n$ | $E_M$ | $E_S$ |
> |---|---|---|---|---|
> | 4 | 0.69121989 | 0.69325397 | $0.00192729$ | $-0.00010679$ |
> | 8 | 0.69266055 | 0.69315453 | $0.00048663$ | $-0.00000735$ |
> | 16 | 0.69302521 | 0.69314765 | $0.00012197$ | $-0.00000047$ |
>
> $E_S$ shrinks by a factor of roughly $15$ each time $n$ doubles, and $E_M$ by about $4$.
>
> *Stewart's margin table lists $0.69315453$, $0.69314765$, $0.69314721$ as $S_4$, $S_8$, $S_{16}$ (with errors $-0.00000735$, $-0.00000047$, $-0.00000003$); these are in fact $S_8$, $S_{16}$, $S_{32}$, i.e. $S_{2n} = \frac13 T_n + \frac23 M_n$ in each row. The values above are recomputed.*
>
> *Stewart: Examples 7.7.4 and 7.7.6*

^ex-50-3

> [!example] Example §50.4: An Integral with No Elementary Antiderivative
> Approximate $\displaystyle\int_0^1 e^{x^2}\,dx$ (a) by the Midpoint Rule and (b) by Simpson's Rule, with $n = 10$, and bound the error in each case.
>
> **(a)** $\Delta x = 0.1$ and the midpoints are $0.05, 0.15, \ldots, 0.95$:
>
> $$
> M_{10} = 0.1\big[e^{0.0025} + e^{0.0225} + e^{0.0625} + e^{0.1225} + e^{0.2025} + e^{0.3025} + e^{0.4225} + e^{0.5625} + e^{0.7225} + e^{0.9025}\big] \approx 1.460393 .
> $$
>
> For $f(x) = e^{x^2}$: $f'(x) = 2xe^{x^2}$ and $f''(x) = (2 + 4x^2)e^{x^2}$. For $0 \le x \le 1$, $x^2 \le 1$, so $0 \le f''(x) \le 6e$. With $K = 6e$, Theorem §50.1 gives
>
> $$
> |E_M| \le \frac{6e(1)^3}{24(10)^2} = \frac{e}{400} \approx 0.007 .
> $$
>
> (The actual error is about $0.0023$: error bounds are worst cases.)
>
> **(b)**
>
> $$
> \begin{aligned}
> S_{10} &= \frac{0.1}{3}\big[f(0) + 4f(0.1) + 2f(0.2) + \cdots + 2f(0.8) + 4f(0.9) + f(1)\big] \\
> &= \frac{0.1}{3}\big[e^0 + 4e^{0.01} + 2e^{0.04} + 4e^{0.09} + 2e^{0.16} + 4e^{0.25} + 2e^{0.36} + 4e^{0.49} + 2e^{0.64} + 4e^{0.81} + e^1\big] \approx 1.462681 .
> \end{aligned}
> $$
>
> Differentiating twice more, $f^{(4)}(x) = (12 + 48x^2 + 16x^4)e^{x^2}$, so $0 \le f^{(4)}(x) \le (12 + 48 + 16)e = 76e$ on $[0, 1]$. With $K = 76e$, Theorem §50.4 gives
>
> $$
> |E_S| \le \frac{76e(1)^5}{180(10)^4} \approx 0.000115 .
> $$
>
> So, correct to three decimal places, $\displaystyle\int_0^1 e^{x^2}\,dx \approx 1.463$.
>
> *Stewart: Examples 7.7.3 and 7.7.7*

^ex-50-4

> [!example] Example §50.5: Integrating Measured Data
> A graph of the data traffic $D(t)$ (megabits per second) on the link from the United States to the Swiss academic network SWITCH over one day gives the following hourly readings from midnight to noon:
>
> | $t$ (hours) | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
> |---|---|---|---|---|---|---|---|---|---|---|---|---|---|
> | $D(t)$ | 3.2 | 2.7 | 1.9 | 1.7 | 1.3 | 1.0 | 1.1 | 1.3 | 2.8 | 5.7 | 7.1 | 7.7 | 7.9 |
>
> Estimate the total amount of data transmitted from midnight to noon.
>
> With $t$ in seconds, the amount $A(t)$ transmitted by time $t$ satisfies $A'(t) = D(t)$, so by the Net Change Theorem ([[§37 Indefinite Integrals and the Net Change Theorem#^thm-37-2|Theorem §37.2]]) the total by noon ($t = 12 \times 60^2 = 43{,}200$) is $\int_0^{43{,}200} D(t)\,dt$. No formula for $D$ is available, but Simpson's Rule needs only the values. With $n = 12$ and $\Delta t = 3600$,
>
> $$
> \begin{aligned}
> \int_0^{43{,}200} D(t)\,dt &\approx \frac{3600}{3}\big[3.2 + 4(2.7) + 2(1.9) + 4(1.7) + 2(1.3) + 4(1.0) + 2(1.1) \\
> &\qquad\qquad + 4(1.3) + 2(2.8) + 4(5.7) + 2(7.1) + 4(7.7) + 7.9\big] = 1200 \times 119.9 = 143{,}880 .
> \end{aligned}
> $$
>
> About $144{,}000$ megabits ($144$ gigabits, or $18$ gigabytes) were transmitted. Using such a rule on data is reasonable when the values do not change rapidly between readings.
>
> *Stewart: Example 7.7.5*

^ex-50-5
