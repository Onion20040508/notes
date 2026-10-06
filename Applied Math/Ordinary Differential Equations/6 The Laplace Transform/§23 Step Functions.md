---
type: section
subject: "[[Ordinary Differential Equations]]"
chapter: 6
section: 23
bdp: "6.3"
aliases: ["BDP 6.3"]
tags: [ordinary-differential-equations, math331]
---
← [[§22 Solution of Initial Value Problems]] · ↑ [[· 6 The Laplace Transform]] · [[§24 Differential Equations with Discontinuous Forcing Functions]] →

*Boyce–DiPrima, Section 6.3 · MATH 331 Written HW 5 (Problems 1–3); Final (Fall 2021), Q3–Q4; Final (Fall 2022, alternate), Q4.*

The Laplace transform is at its best with forcing terms that switch on and off. The unit step function $u_c(t)$ writes any piecewise continuous function as one formula, a sum of shifted pieces $u_c(t)\,f(t-c)$. Two shift theorems make the transform work with these pieces: a delay by $c$ in $t$ multiplies the transform by $e^{-cs}$ (Theorem 6.3.1), and multiplication by $e^{ct}$ shifts the transform by $c$ in $s$ (Theorem 6.3.2). Reading them backwards gives most inverse transforms in Chapter 6: an exponential $e^{-cs}$ in $F(s)$ means a delayed function, and a denominator that is completed to $(s-a)^2 + b^2$ means a factor $e^{at}$.

Throughout, functions are piecewise continuous and of exponential order, so their transforms exist for $s$ large ([[§21 Definition of the Laplace Transform#^thm-21-2|Theorem §21.2]], BDP Theorem 6.1.2).

## The Unit Step Function

> [!definition] Definition §23.1: Unit Step Function
> For $c \ge 0$, the **unit step function** or **Heaviside function** is
>
> $$
> u_c(t) = \begin{cases} 0, & t < c, \\ 1, & t \ge c. \end{cases} \qquad (1)
> $$
>
> Only $t \ge 0$ matters for the Laplace transform. The value $1$ at $t = c$ is a convention: for a piecewise continuous function the value at a jump is irrelevant (it does not change any integral). Reading $1$ as "on" and $0$ as "off", $u_c(t)$ is a switch turned on at time $c$, and $1 - u_c(t)$ is a switch turned off at time $c$.
>
> *BDP: 6.3 (text), Equation (1)*

^def-23-1

> [!remark]- Connections
> - $u_c$ has a jump discontinuity at $c$ in the sense of [[§10 Continuity#^def-10-3|Calc Def. §10.3]]: the one-sided limits $0$ and $1$ exist and differ; it is continuous from the right there ([[§10 Continuity#^def-10-4|Calc Def. §10.4]]).

> [!example] Example §23.1: Piecewise Functions as Sums of Steps
> **(a) A rectangular pulse.** Let $h(t) = u_\pi(t) - u_{2\pi}(t)$, $t \ge 0$. From (1),
>
> $$
> h(t) = \begin{cases} 0 - 0, & 0 \le t < \pi, \\ 1 - 0, & \pi \le t < 2\pi, \\ 1 - 1, & 2\pi \le t < \infty \end{cases}
> \;=\; \begin{cases} 0, & 0 \le t < \pi, \\ 1, & \pi \le t < 2\pi, \\ 0, & 2\pi \le t . \end{cases}
> $$
>
> This is a switch turned on at $t = \pi$ and off at $t = 2\pi$, a **rectangular pulse**. In general $u_a(t) - u_b(t)$ ($a < b$) is $1$ on $[a, b)$ and $0$ elsewhere.
>
> **(b) A staircase.** Express in terms of $u_c(t)$:
>
> $$
> f(t) = \begin{cases} 2, & 0 \le t < 4, \\ 5, & 4 \le t < 7, \\ -1, & 7 \le t < 9, \\ 1, & t \ge 9. \end{cases} \qquad (2)
> $$
>
> Start with $f_1(t) = 2$, which agrees with $f$ on $[0, 4)$. At $t = 4$ the function jumps up by $3$, so add $3u_4(t)$: $f_2(t) = 2 + 3u_4(t)$ agrees with $f$ on $[0, 7)$. At $t = 7$ it jumps down by $6$, so add $-6u_7(t)$, and at $t = 9$ it jumps up by $2$. Hence
>
> $$
> f(t) = 2 + 3u_4(t) - 6u_7(t) + 2u_9(t) . \qquad (3)
> $$
>
> Each coefficient is the size of the jump at that point (panel (a) of the figure).
>
> *BDP: Examples 6.3.1 and 6.3.2*

^ex-23-1

![[m331-23-1.svg]]
*(a) The staircase (2) is built from left to right: each jump of $f$ at $t = c$ contributes the term (jump)$\cdot u_c(t)$, giving (3). (b) Translation ([[§23 Step Functions#^def-23-2|Definition §23.2]]): $u_c(t)f(t-c)$ is the graph of $f$ (dashed) moved $c$ units to the right, with $0$ filled in on $[0, c)$. Its transform is $e^{-cs}F(s)$ ([[§23 Step Functions#^thm-23-2|Theorem §23.2]]).*

> [!remark] Remark: Method — Writing a Piecewise Function with Step Functions
> Let $f(t) = f_k(t)$ on $c_k \le t < c_{k+1}$, $k = 0, 1, \ldots, m$, with $0 = c_0 < c_1 < \cdots < c_m$ and $c_{m+1} = \infty$.
> 1. Start with the first formula, $f_0(t)$.
> 2. At each break point $c_k$, add $u_{c_k}(t)\,\big(f_k(t) - f_{k-1}(t)\big)$: it switches off the old formula and switches on the new one. So
>
> $$
> f(t) = f_0(t) + \sum_{k=1}^{m} u_{c_k}(t)\big(f_k(t) - f_{k-1}(t)\big) .
> $$
>
> 3. To take the transform, rewrite each $f_k(t) - f_{k-1}(t)$ as a function of $t - c_k$, so that every term has the form $u_{c}(t)\,g(t - c)$ of Theorem §23.2. For constant pieces the differences are the jumps, as in (3).

^rem-23-1

> [!theorem] Theorem §23.1: Transform of the Unit Step
> For $c \ge 0$,
>
> $$
> \mathcal{L}\{u_c(t)\} = \frac{e^{-cs}}{s}, \qquad s > 0 . \qquad (4)
> $$
>
> In particular $\mathcal{L}\{u_0(t)\} = 1/s = \mathcal{L}\{1\}$, since $u_0(t) = 1$ for all $t \ge 0$.
>
> *BDP: 6.3 (text), Equation (4)*

^thm-23-1

> [!proof]+ Proof
> Since $u_c(t) = 0$ for $t < c$ and $u_c(t) = 1$ for $t \ge c$,
>
> $$
> \mathcal{L}\{u_c(t)\} = \int_0^\infty e^{-st} u_c(t)\,dt = \int_c^\infty e^{-st}\,dt = \lim_{A \to \infty} \Big[-\frac{e^{-st}}{s}\Big]_{t=c}^{t=A} = \lim_{A \to \infty} \frac{e^{-cs} - e^{-As}}{s} = \frac{e^{-cs}}{s}
> $$
>
> for $s > 0$, because then $e^{-As} \to 0$.

^pf-23-1

*Uses:* [[§23 Step Functions#^def-23-1|Def. §23.1]], [[§21 Definition of the Laplace Transform#^def-21-4|Def. §21.4]]

## Translations: the Shift in t

> [!definition] Definition §23.2: Translation of a Function
> For $f$ defined on $t \ge 0$ and $c \ge 0$, the function
>
> $$
> g(t) = \begin{cases} 0, & t < c, \\ f(t - c), & t \ge c, \end{cases} \qquad\text{that is,}\qquad g(t) = u_c(t)\,f(t - c),
> $$
>
> is the **translation** of $f$ a distance $c$ in the positive $t$ direction. Its graph is the graph of $f$ moved $c$ units to the right, with $g = 0$ on $[0, c)$.
>
> *BDP: 6.3 (text)*

^def-23-2

> [!theorem] Theorem §23.2: Laplace Transform of a Translation
> If $F(s) = \mathcal{L}\{f(t)\}$ exists for $s > a \ge 0$, and if $c$ is a positive constant, then
>
> $$
> \mathcal{L}\{u_c(t)\,f(t - c)\} = e^{-cs}\mathcal{L}\{f(t)\} = e^{-cs}F(s), \qquad s > a . \qquad (5)
> $$
>
> Conversely, if $f(t) = \mathcal{L}^{-1}\{F(s)\}$, then
>
> $$
> u_c(t)\,f(t - c) = \mathcal{L}^{-1}\{e^{-cs}F(s)\} . \qquad (6)
> $$
>
> A translation by $c$ in $t$ corresponds to multiplication of the transform by $e^{-cs}$.
>
> *BDP: Theorem 6.3.1*

^thm-23-2

> [!proof]+ Proof
> Since $u_c(t) = 0$ for $t < c$,
>
> $$
> \mathcal{L}\{u_c(t)\,f(t - c)\} = \int_0^\infty e^{-st} u_c(t)\,f(t - c)\,dt = \int_c^\infty e^{-st} f(t - c)\,dt .
> $$
>
> Substitute $\sigma = t - c$: then $d\sigma = dt$, $\sigma = 0$ when $t = c$, $\sigma \to \infty$ as $t \to \infty$, and $e^{-st} = e^{-s(\sigma + c)}$. So
>
> $$
> \mathcal{L}\{u_c(t)\,f(t - c)\} = \int_0^\infty e^{-(\sigma + c)s} f(\sigma)\,d\sigma = e^{-cs}\int_0^\infty e^{-s\sigma} f(\sigma)\,d\sigma = e^{-cs}F(s) .
> $$
>
> The last integral converges for $s > a$ by hypothesis, so the first one does too; this is (5). (The substitution is made in the integral over $[c, A]$, and then $A \to \infty$.) Taking the inverse transform of both sides of (5) gives (6).

^pf-23-2

*Uses:* [[§23 Step Functions#^def-23-1|Def. §23.1]], [[§23 Step Functions#^def-23-2|Def. §23.2]], [[§21 Definition of the Laplace Transform#^def-21-4|Def. §21.4]], [[§22 Solution of Initial Value Problems#^def-22-1|Def. §22.1]] (the inverse transform)

With $f(t) = 1$, $\mathcal{L}\{1\} = 1/s$, (5) gives $\mathcal{L}\{u_c(t)\} = e^{-cs}/s$ again, in agreement with Theorem §23.1.

> [!example] Example §23.2: Transforms of Piecewise Functions
> **(a)** Find $\mathcal{L}\{f(t)\}$ for
>
> $$
> f(t) = \begin{cases} \sin t, & 0 \le t < \frac{\pi}{4}, \\[2pt] \sin t + \cos\big(t - \frac{\pi}{4}\big), & t \ge \frac{\pi}{4}. \end{cases}
> $$
>
> Here $f(t) = \sin t + u_{\pi/4}(t)\cos\big(t - \frac{\pi}{4}\big)$, and the second term is the translation of $\cos t$ by $\pi/4$. By [[§23 Step Functions#^thm-23-2|Theorem §23.2]] and the table ([[§22 Solution of Initial Value Problems#^thm-22-6|Theorem §22.6]], Table 6.2.1),
>
> $$
> \mathcal{L}\{f(t)\} = \mathcal{L}\{\sin t\} + e^{-\pi s/4}\mathcal{L}\{\cos t\} = \frac{1}{s^2 + 1} + e^{-\pi s/4}\frac{s}{s^2 + 1} = \frac{1 + s e^{-\pi s/4}}{s^2 + 1} .
> $$
>
> This avoids splitting the defining integral at $\pi/4$.
>
> **(b)** Let $f(t) = \sin(2t) + u_\pi(t)\Big(\dfrac{t}{\pi} - \sin(2t)\Big) + u_{2\pi}(t)\,\dfrac{2\pi - t}{\pi}$. (i) Write $f$ piecewise. (ii) Write $f$ as a sum of terms $u_a(t)\,k(t - a)$. (iii) Compute $\mathcal{L}\{f(t)\}$.
>
> **(i)** On $[0, \pi)$ both steps are off: $f(t) = \sin 2t$. On $[\pi, 2\pi)$ the first is on: $f(t) = \sin 2t + \frac{t}{\pi} - \sin 2t = \frac{t}{\pi}$. For $t \ge 2\pi$ both are on: $f(t) = \frac{t}{\pi} + \frac{2\pi - t}{\pi} = 2$. So
>
> $$
> f(t) = \begin{cases} \sin 2t, & 0 \le t < \pi, \\ t/\pi, & \pi \le t < 2\pi, \\ 2, & t \ge 2\pi. \end{cases}
> $$
>
> The graph is one full period of $\sin 2t$, then a jump from $0$ to $1$ at $t = \pi$, a line rising to $2$ at $t = 2\pi$, and the constant $2$ (continuous at $2\pi$).
>
> **(ii)** Rewrite each bracket in terms of $t - a$. Since $\sin 2t$ has period $\pi$, $\sin 2t = \sin\big(2(t - \pi)\big)$; also $\frac{t}{\pi} = \frac{t - \pi}{\pi} + 1$ and $\frac{2\pi - t}{\pi} = -\frac{t - 2\pi}{\pi}$. Hence
>
> $$
> f(t) = \sin 2t - u_\pi(t)\sin\big(2(t - \pi)\big) + u_\pi(t)\Big(\frac{t - \pi}{\pi} + 1\Big) - u_{2\pi}(t)\,\frac{t - 2\pi}{\pi} .
> $$
>
> **(iii)** With $\mathcal{L}\{\sin 2t\} = \frac{2}{s^2 + 4}$, $\mathcal{L}\{\frac{t}{\pi} + 1\} = \frac{1}{\pi s^2} + \frac1s$, $\mathcal{L}\{\frac{t}{\pi}\} = \frac{1}{\pi s^2}$ and Theorem §23.2,
>
> $$
> \mathcal{L}\{f(t)\} = \frac{2}{s^2 + 4}\big(1 - e^{-\pi s}\big) + e^{-\pi s}\Big(\frac{1}{\pi s^2} + \frac{1}{s}\Big) - \frac{e^{-2\pi s}}{\pi s^2} .
> $$
>
> (A numerical check of the defining integral at $s = 0.7$ gives $0.61852$ on both sides.)
>
> *BDP: Example 6.3.3*
> *Source: 331 Written HW 5, Problem 1*

^ex-23-2

> [!remark] Remark: Method — Inverse Transforms Containing $e^{-cs}$
> To find $\mathcal{L}^{-1}\{e^{-cs}G(s)\}$:
> 1. Group the terms of $F(s)$ by their exponential factor, and handle each group separately (linearity).
> 2. Ignore $e^{-cs}$ and find $g(t) = \mathcal{L}^{-1}\{G(s)\}$: partial fractions ([[§22 Solution of Initial Value Problems#^rem-22-4|Method of §22]]), or completing the square ([[§23 Step Functions#^thm-23-3|Theorem §23.3]]).
> 3. Replace $t$ by $t - c$ *everywhere* in $g$, including inside exponentials, and multiply by $u_c(t)$: $\mathcal{L}^{-1}\{e^{-cs}G(s)\} = u_c(t)\,g(t - c)$ ([[§23 Step Functions#^thm-23-2|Theorem §23.2]]).
> 4. If a graph or a formula on each interval is wanted, write the answer piecewise.

^rem-23-2

> [!example] Example §23.3: Inverse Transforms of Delayed Functions
> **(a)** Find $\mathcal{L}^{-1}\Big\{\dfrac{1 - e^{-2s}}{s^2}\Big\}$ and graph it. By linearity and [[§23 Step Functions#^thm-23-2|Theorem §23.2]] with $g(t) = \mathcal{L}^{-1}\{1/s^2\} = t$,
>
> $$
> f(t) = \mathcal{L}^{-1}\Big\{\frac{1}{s^2}\Big\} - \mathcal{L}^{-1}\Big\{\frac{e^{-2s}}{s^2}\Big\} = t - u_2(t)(t - 2) = \begin{cases} t, & 0 \le t < 2, \\ 2, & t \ge 2. \end{cases}
> $$
>
> The graph is a ramp that rises to $2$ at $t = 2$ and stays there.
>
> **(b)** Compute $\mathcal{L}^{-1}\Big\{\dfrac{6e^{-5s}}{s^2 - 3s + 2}\Big\}$. Factor $s^2 - 3s + 2 = (s - 1)(s - 2)$. Partial fractions: $\dfrac{6}{(s - 1)(s - 2)} = \dfrac{A}{s - 2} + \dfrac{B}{s - 1}$ with $6 = A(s - 1) + B(s - 2)$; $s = 2$ gives $A = 6$ and $s = 1$ gives $B = -6$. So
>
> $$
> g(t) = \mathcal{L}^{-1}\Big\{\frac{6}{s - 2} - \frac{6}{s - 1}\Big\} = 6e^{2t} - 6e^{t},
> \qquad
> \mathcal{L}^{-1}\Big\{\frac{6e^{-5s}}{s^2 - 3s + 2}\Big\} = u_5(t)\big(6e^{2(t - 5)} - 6e^{t - 5}\big) .
> $$
>
> **(c)** Compute $\mathcal{L}^{-1}\Big\{\dfrac{e^{-2s}}{(s - 1)(s^2 + 4s + 5)}\Big\}$. The quadratic has no real roots ($16 - 20 < 0$), so
>
> $$
> \frac{1}{(s - 1)(s^2 + 4s + 5)} = \frac{A}{s - 1} + \frac{Bs + C}{s^2 + 4s + 5}, \qquad 1 = A(s^2 + 4s + 5) + (Bs + C)(s - 1) .
> $$
>
> At $s = 1$: $10A = 1$, $A = \frac{1}{10}$. Coefficient of $s^2$: $A + B = 0$, $B = -\frac{1}{10}$. Constant term: $5A - C = 1$, $C = -\frac12$. So $Bs + C = -\frac{1}{10}(s + 5) = -\frac{1}{10}\big[(s + 2) + 3\big]$, and with $s^2 + 4s + 5 = (s + 2)^2 + 1$ and [[§23 Step Functions#^thm-23-3|Theorem §23.3]],
>
> $$
> g(t) = \frac{1}{10}e^{t} - \frac{1}{10}\mathcal{L}^{-1}\Big\{\frac{(s + 2) + 3}{(s + 2)^2 + 1}\Big\} = \frac{1}{10}\Big[e^{t} - e^{-2t}(\cos t + 3\sin t)\Big] .
> $$
>
> Therefore
>
> $$
> \mathcal{L}^{-1}\Big\{\frac{e^{-2s}}{(s - 1)(s^2 + 4s + 5)}\Big\} = \frac{u_2(t)}{10}\Big[e^{t - 2} - e^{-2(t - 2)}\big(\cos(t - 2) + 3\sin(t - 2)\big)\Big] .
> $$
>
> *BDP: Example 6.3.4*
> *Source: 331 Final (Fall 2021), Q4; 331 Written HW 5, Problem 3(b)*

^ex-23-3

## Exponential Multipliers: the Shift in s

> [!theorem] Theorem §23.3: Multiplication by an Exponential
> If $F(s) = \mathcal{L}\{f(t)\}$ exists for $s > a \ge 0$, and if $c$ is a constant, then
>
> $$
> \mathcal{L}\{e^{ct}f(t)\} = F(s - c), \qquad s > a + c . \qquad (7)
> $$
>
> Conversely, if $f(t) = \mathcal{L}^{-1}\{F(s)\}$, then
>
> $$
> e^{ct}f(t) = \mathcal{L}^{-1}\{F(s - c)\} . \qquad (8)
> $$
>
> Multiplication of $f(t)$ by $e^{ct}$ translates the transform a distance $c$ in the positive $s$ direction, and conversely.
>
> *BDP: Theorem 6.3.2*

^thm-23-3

> [!proof]+ Proof
> By definition,
>
> $$
> \mathcal{L}\{e^{ct}f(t)\} = \int_0^\infty e^{-st}e^{ct}f(t)\,dt = \int_0^\infty e^{-(s - c)t}f(t)\,dt = F(s - c),
> $$
>
> since the last integral is the defining integral of $F$ evaluated at $s - c$. It converges when $s - c > a$, that is, $s > a + c$. (BDP justifies the range through the hypothesis $|f(t)| \le Ke^{at}$ of [[§21 Definition of the Laplace Transform#^thm-21-2|Theorem §21.2]] (BDP Theorem 6.1.2), which gives $|e^{ct}f(t)| \le Ke^{(a + c)t}$, so $e^{ct}f$ is of exponential order $a + c$.) Taking the inverse transform of (7) gives (8).

^pf-23-3

*Uses:* [[§21 Definition of the Laplace Transform#^def-21-4|Def. §21.4]], [[§21 Definition of the Laplace Transform#^thm-21-2|§21.2]] (Theorem 6.1.2)

> [!remark] Remark: Method — Completing the Square
> For $\mathcal{L}^{-1}\Big\{\dfrac{ps + q}{s^2 + Bs + C}\Big\}$ with $B^2 - 4C < 0$:
> 1. Complete the square: $s^2 + Bs + C = (s - a)^2 + b^2$, where $a = -B/2$ and $b^2 = C - B^2/4$.
> 2. Rewrite the numerator in powers of $s - a$: $ps + q = p(s - a) + (pa + q)$.
> 3. Read off, by [[§23 Step Functions#^thm-23-3|Theorem §23.3]] and the transforms of $\cos bt$ and $\sin bt$:
>
> $$
> \mathcal{L}^{-1}\Big\{\frac{p(s - a) + (pa + q)}{(s - a)^2 + b^2}\Big\} = e^{at}\Big(p\cos bt + \frac{pa + q}{b}\sin bt\Big) .
> $$
>
> This avoids complex roots in partial fractions.

^rem-23-3

> [!example] Example §23.4: Completing the Square
> **(a)** $G(s) = \dfrac{1}{s^2 - 4s + 5} = \dfrac{1}{(s - 2)^2 + 1} = F(s - 2)$ with $F(s) = \dfrac{1}{s^2 + 1} = \mathcal{L}\{\sin t\}$. By [[§23 Step Functions#^thm-23-3|Theorem §23.3]], $\mathcal{L}^{-1}\{G(s)\} = e^{2t}\sin t$.
>
> **(b)** $\mathcal{L}^{-1}\Big\{\dfrac{s + 11}{s^2 + 6s + 13}\Big\}$. Here $s^2 + 6s + 13 = (s + 3)^2 + 2^2$ and $s + 11 = (s + 3) + 8$, so
>
> $$
> \mathcal{L}^{-1}\Big\{\frac{(s + 3) + 4 \cdot 2}{(s + 3)^2 + 2^2}\Big\} = e^{-3t}\,\mathcal{L}^{-1}\Big\{\frac{s}{s^2 + 2^2} + 4\,\frac{2}{s^2 + 2^2}\Big\} = e^{-3t}\big(\cos 2t + 4\sin 2t\big) .
> $$
>
> **(c)** $\mathcal{L}^{-1}\Big\{\dfrac{5s - \alpha}{s^2 + 4s + 13}\Big\}$ for a constant $\alpha$. Here $s^2 + 4s + 13 = (s + 2)^2 + 3^2$ and $5s - \alpha = 5(s + 2) - (10 + \alpha)$, so
>
> $$
> \mathcal{L}^{-1}\Big\{5\,\frac{s + 2}{(s + 2)^2 + 3^2} - \frac{10 + \alpha}{3}\cdot\frac{3}{(s + 2)^2 + 3^2}\Big\} = e^{-2t}\Big(5\cos 3t - \frac{10 + \alpha}{3}\sin 3t\Big) .
> $$
>
> In the same way $\dfrac{1}{s^2 + 2s + 2} = \dfrac{1}{(s + 1)^2 + 1}$ has inverse $e^{-t}\sin t$ (HW 5, Problem 2(a)).
>
> *BDP: Example 6.3.5*
> *Source: 331 Final (Fall 2021), Q3; 331 Written HW 5, Problem 2(a), (c)*

^ex-23-4

> [!example] Example §23.5: Both Shifts at Once
> **(a)** Compute $\mathcal{L}^{-1}\Big\{\dfrac{s + 1 + e^{-7s}}{s^2 - 4s + 13}\Big\}$.
>
> Split by exponential factor (step 1 of the method): $\dfrac{s + 1}{s^2 - 4s + 13} + e^{-7s}\dfrac{1}{s^2 - 4s + 13}$, with $s^2 - 4s + 13 = (s - 2)^2 + 3^2$.
>
> *First term.* $s + 1 = (s - 2) + 3$, so by [[§23 Step Functions#^thm-23-3|Theorem §23.3]]
>
> $$
> \mathcal{L}^{-1}\Big\{\frac{(s - 2) + 3}{(s - 2)^2 + 3^2}\Big\} = e^{2t}(\cos 3t + \sin 3t) .
> $$
>
> *Second term.* $g(t) = \mathcal{L}^{-1}\Big\{\dfrac{1}{(s - 2)^2 + 3^2}\Big\} = \dfrac13 e^{2t}\sin 3t$, and by [[§23 Step Functions#^thm-23-2|Theorem §23.2]] the factor $e^{-7s}$ delays it by $7$. Altogether
>
> $$
> \mathcal{L}^{-1}\Big\{\frac{s + 1 + e^{-7s}}{s^2 - 4s + 13}\Big\} = e^{2t}(\cos 3t + \sin 3t) + \frac13\,u_7(t)\,e^{2(t - 7)}\sin\big(3(t - 7)\big) .
> $$
>
> **(b)** In the same way, $\dfrac{e^{-4s}}{s^2 + 4s + 13} = e^{-4s}\dfrac{1}{(s + 2)^2 + 3^2}$, $g(t) = \frac13 e^{-2t}\sin 3t$, and
>
> $$
> \mathcal{L}^{-1}\Big\{\frac{e^{-4s}}{s^2 + 4s + 13}\Big\} = \frac13\,u_4(t)\,e^{-2(t - 4)}\sin\big(3(t - 4)\big) .
> $$
>
> The $e^{-2t}$ is shifted too: it becomes $e^{-2(t - 4)} = e^{8 - 2t}$, not $e^{-2t}$.
>
> *Source: 331 Final (Fall 2022, alternate), Q4; 331 Written HW 5, Problem 2(b)*

^ex-23-5

> [!remark]- Remark: The Two Shift Rules Side by Side
> | | time domain | transform |
> |---|---|---|
> | shift in $t$ ([[§23 Step Functions#^thm-23-2\|Theorem §23.2]]) | $u_c(t)\,f(t - c)$ | $e^{-cs}F(s)$ |
> | shift in $s$ ([[§23 Step Functions#^thm-23-3\|Theorem §23.3]]) | $e^{ct}f(t)$ | $F(s - c)$ |
>
> An exponential in one variable is a shift in the other. The signs differ: a delay $c > 0$ gives $e^{-cs}$, while the factor $e^{ct}$ gives $s - c$. These are the two "shift" lines of the course's table of transforms.
>
> *Source: 331 Course Review (Laplace), table*

^rem-23-4
