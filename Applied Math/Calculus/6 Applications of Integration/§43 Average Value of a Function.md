---
type: section
subject: "[[Calculus]]"
chapter: 6
section: 43
stewart: "6.5"
aliases: ["Stewart 6.5"]
tags: [calculus]
---
← [[§42 Work]] · ↑ [[· 6 Applications of Integration]] · [[§44 Integration by Parts]] →

*Stewart, Section 6.5.*

The average of finitely many numbers is their sum divided by how many there are. To average a function over an interval, for example a temperature over a day, average $n$ equally spaced values and let $n \to \infty$. The averages become Riemann sums divided by $b - a$, so the average value of $f$ is $\frac{1}{b - a} \int_a^b f(x)\,dx$. The Mean Value Theorem for Integrals says that a continuous function actually takes its average value somewhere. It follows from the Mean Value Theorem for derivatives applied to $\int_a^x f(t)\,dt$.

## Average Value

The average of $y_1, \ldots, y_n$ is $y_{\rm avg} = \dfrac{y_1 + y_2 + \cdots + y_n}{n}$. For a function $y = f(x)$, $a \le x \le b$, divide $[a, b]$ into $n$ equal subintervals of length $\Delta x = (b - a)/n$, choose $x_1^*, \ldots, x_n^*$ in successive subintervals, and average the values $f(x_1^*), \ldots, f(x_n^*)$. (For a temperature with $n = 24$: readings every hour, averaged.) Since $n = (b - a)/\Delta x$,

$$
\frac{f(x_1^*) + \cdots + f(x_n^*)}{n} = \frac{f(x_1^*) + \cdots + f(x_n^*)}{\dfrac{b - a}{\Delta x}} = \frac{1}{b - a} \big[ f(x_1^*)\,\Delta x + \cdots + f(x_n^*)\,\Delta x \big] = \frac{1}{b - a} \sum_{i=1}^{n} f(x_i^*)\,\Delta x .
$$

As $n$ increases we average more and more closely spaced values (readings every minute, every second), and by the definition of the integral the limit is

$$
\lim_{n \to \infty} \frac{1}{b - a} \sum_{i=1}^{n} f(x_i^*)\,\Delta x = \frac{1}{b - a} \int_a^b f(x)\,dx .
$$

> [!definition] Definition §43.1: Average Value of a Function
> The **average value of $f$** on the interval $[a, b]$ is
>
> $$
> f_{\rm avg} = \frac{1}{b - a} \int_a^b f(x)\,dx .
> $$
>
> For a positive function this says $\dfrac{\text{area}}{\text{width}} = \text{average height}$.
>
> *Stewart: 6.5 (text)*

^def-43-1

> [!example] Example §43.1: An Average Value
> Find the average value of $f(x) = 1 + x^2$ on the interval $[-1, 2]$.
>
> With $a = -1$ and $b = 2$,
>
> $$
> f_{\rm avg} = \frac{1}{b - a} \int_a^b f(x)\,dx = \frac{1}{2 - (-1)} \int_{-1}^{2} (1 + x^2)\,dx = \frac13 \Big[x + \frac{x^3}{3}\Big]_{-1}^{2} = \frac13 \Big[\Big(2 + \frac83\Big) - \Big(-1 - \frac13\Big)\Big] = \frac13 \cdot 6 = 2 .
> $$
>
> *Stewart: Example 6.5.1*

^ex-43-1

## The Mean Value Theorem for Integrals

Is there a number $c$ at which $f$ takes exactly its average value, $f(c) = f_{\rm avg}$? For a temperature over a day there are typically such times (Stewart's graph has two, just before noon and just before midnight). For continuous functions the answer is always yes.

> [!theorem] Theorem §43.1: The Mean Value Theorem for Integrals
> If $f$ is continuous on $[a, b]$, then there exists a number $c$ in $[a, b]$ such that
>
> $$
> f(c) = f_{\rm avg} = \frac{1}{b - a} \int_a^b f(x)\,dx ,
> \qquad\text{that is,}\qquad
> \int_a^b f(x)\,dx = f(c)(b - a) .
> $$
>
> *Stewart: 6.5, The Mean Value Theorem for Integrals*

^thm-43-1

> [!remark] Remark: Why It Works
> For a positive $f$: there is a number $c$ such that the rectangle with base $[a, b]$ and height $f(c)$ has the same area as the region under the graph of $f$ from $a$ to $b$. Picturesquely, one can always chop off the top of a (two-dimensional) mountain at a certain height, namely $f_{\rm avg}$, and use it to fill in the valleys so that the mountain becomes completely flat. Since the graph of a continuous function is unbroken, it must cross that height.

^rem-43-1

> [!proof]+ Proof
> *Stewart outlines this proof in Exercise 28: the theorem is a consequence of the Mean Value Theorem for derivatives and the Fundamental Theorem of Calculus.* Let
>
> $$
> F(x) = \int_a^x f(t)\,dt , \qquad a \le x \le b .
> $$
>
> Since $f$ is continuous on $[a, b]$, FTC1 ([[§36 The Fundamental Theorem of Calculus#^thm-36-1|Theorem §36.1]]) shows that $F$ is continuous on $[a, b]$ and differentiable on $(a, b)$ with $F'(x) = f(x)$. By the Mean Value Theorem ([[§26 The Mean Value Theorem#^thm-26-2|Theorem §26.2]]) there is a number $c$ in $(a, b)$ with
>
> $$
> F(b) - F(a) = F'(c)(b - a) .
> $$
>
> Here $F(b) - F(a) = \int_a^b f(t)\,dt - 0$ ([[§35 The Definite Integral#^def-35-4|Definition §35.4]]) and $F'(c) = f(c)$, so $\int_a^b f(x)\,dx = f(c)(b - a)$. Dividing by $b - a > 0$ gives $f(c) = f_{\rm avg}$. (The argument even gives $c$ in the open interval $(a, b)$.)

^pf-43-1

*Uses:* [[§36 The Fundamental Theorem of Calculus#^thm-36-1|§36.1]], [[§26 The Mean Value Theorem#^thm-26-2|§26.2]] (Mean Value Theorem), [[§35 The Definite Integral#^def-35-4|Def. §35.4]], [[§43 Average Value of a Function#^def-43-1|Def. §43.1]]

> [!remark]- Connections
> - Rigorous treatment: [[§33 Properties of the Riemann Integral#^thm-33-9|451 Thm. §33.9]] proves it with the [[§10 Continuity#^thm-10-10|Intermediate Value Theorem]] instead (the average lies between the minimum and maximum of $f$), [[§33 Properties of the Riemann Integral#^prop-33-11|451 Prop. §33.11]] shows that $c$ can be taken in $(a, b)$, and [[§33 Properties of the Riemann Integral#^thm-33-10|451 Thm. §33.10]] is the weighted version.

> [!example] Example §43.2: Where f Equals Its Average
> $f(x) = 1 + x^2$ is continuous on $[-1, 2]$, so by Theorem §43.1 there is a number $c$ in $[-1, 2]$ such that
>
> $$
> \int_{-1}^{2} (1 + x^2)\,dx = f(c)\,[2 - (-1)] .
> $$
>
> Here $c$ can be found explicitly. By Example §43.1, $f_{\rm avg} = 2$, so $c$ satisfies $f(c) = 1 + c^2 = 2$, that is $c^2 = 1$. In this case there happen to be two such numbers in $[-1, 2]$, namely $c = \pm 1$.
>
> *Stewart: Example 6.5.2*

^ex-43-2

![[m233-43-1.svg]]
*Examples §43.1 and §43.2. The rectangle over $[-1, 2]$ of height $f_{\rm avg} = 2$ has the same area, $6$, as the region under $y = 1 + x^2$: the part of the graph above the red line (blue, area $\frac43$) exactly fills the valley below it (orange, area $\frac43$). The graph meets the line at $c = -1$ and $c = 1$, both numbers given by the Mean Value Theorem for Integrals.*

> [!example] Example §43.3: Average Velocity
> Show that the average velocity of a car over a time interval $[t_1, t_2]$ is the same as the average of its velocities during the trip.
>
> If $s(t)$ is the displacement of the car at time $t$, its average velocity over the interval is by definition
>
> $$
> \frac{\Delta s}{\Delta t} = \frac{s(t_2) - s(t_1)}{t_2 - t_1} .
> $$
>
> On the other hand, the average value of the velocity function $v = s'$ on the interval is, by the Net Change Theorem ([[§37 Indefinite Integrals and the Net Change Theorem#^thm-37-2|Theorem §37.2]]),
>
> $$
> v_{\rm avg} = \frac{1}{t_2 - t_1} \int_{t_1}^{t_2} v(t)\,dt = \frac{1}{t_2 - t_1} \int_{t_1}^{t_2} s'(t)\,dt = \frac{1}{t_2 - t_1} \big[s(t_2) - s(t_1)\big] = \frac{s(t_2) - s(t_1)}{t_2 - t_1} ,
> $$
>
> which is the average velocity.
>
> *Stewart: Example 6.5.3*

^ex-43-3
