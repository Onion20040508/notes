---
type: section
subject: "[[Ordinary Differential Equations]]"
chapter: 2
section: 14
bdp: "2.8"
aliases: ["BDP 2.8"]
tags: [ordinary-differential-equations, math331]
---
← [[§13 Numerical Approximations꞉ Euler's Method]] · ↑ [[· 2 First-Order Differential Equations]] · [[§15★ First-Order Difference Equations]] →

*Boyce–DiPrima, Section 2.8.*

This section proves Theorem 2.4.2: if $f$ and $\partial f/\partial y$ are continuous near $(t_0, y_0)$, the initial value problem $y' = f(t, y)$, $y(t_0) = y_0$ has exactly one solution on some interval around $t_0$. Since there is no formula for the solution, the proof constructs it as a limit: the problem is rewritten as an integral equation, and the method of successive approximations (Picard iteration) produces a sequence of functions that converges uniformly to a solution. BDP indicates the main steps and leaves the estimates to Problems 14–18; here the proof is written out in full, with those problems as lemmas. The tools are uniform convergence, the Weierstrass M-test and the exchange of limit and integral from Single Variable Analysis, and a Lipschitz bound from the mean value theorem. The same method, with absolute values replaced by vector norms, proves the existence and uniqueness theorems for first-order systems, [[§33 Introduction to Systems of First-Order Linear Equations#^thm-33-2|Theorem §33.2]] and [[§33 Introduction to Systems of First-Order Linear Equations#^thm-33-3|Theorem §33.3]], and hence for second-order linear equations, [[§18 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-18-1|Theorem §18.1]]; BDP proves none of these.

## Reduction to the Origin

It is enough to consider initial value problems whose initial point $(t_0, y_0)$ is the origin,

$$
y' = f(t, y), \qquad y(0) = 0 , \qquad (2)
$$

because a translation of the coordinate axes takes any initial point to the origin.

> [!theorem] Lemma §18.1: Translation to the Origin
> Let $g(s, w) = f(t_0 + s,\, y_0 + w)$. A function $y = \phi(t)$ solves $y' = f(t, y)$, $y(t_0) = y_0$ on an interval $|t - t_0| \le h$ if and only if $w = \psi(s) = \phi(t_0 + s) - y_0$ solves
>
> $$
> w' = g(s, w), \qquad w(0) = 0
> $$
>
> on $|s| \le h$. Moreover $f$ and $\partial f/\partial y$ are continuous on the rectangle $|t - t_0| \le a$, $|y - y_0| \le b$ if and only if $g$ and $\partial g/\partial w$ are continuous on $|s| \le a$, $|w| \le b$.
>
> *BDP: 2.8 (text)*

^lem-14-1

> [!proof]+ Proof
> The map $(s, w) \mapsto (t_0 + s, y_0 + w)$ is a translation, taking the second rectangle onto the first; composition with it preserves continuity, and $\partial g/\partial w(s, w) = \partial f/\partial y(t_0 + s, y_0 + w)$. By the chain rule, $\psi'(s) = \phi'(t_0 + s)$, so
>
> $$
> \psi'(s) = g(s, \psi(s)) \iff \phi'(t_0 + s) = f\big(t_0 + s,\, \phi(t_0 + s)\big) ,
> $$
>
> and $\psi(0) = 0 \iff \phi(t_0) = y_0$.

^pf-14-1

In this form, Theorem 2.4.2 becomes BDP's **Theorem 2.8.1**: *if $f$ and $\partial f/\partial y$ are continuous in a rectangle $R\colon |t| \le a$, $|y| \le b$, then there is some interval $|t| \le h \le a$ in which there exists a unique solution $y = \phi(t)$ of (2).* It is proved below as [[§14 The Existence and Uniqueness Theorem#^thm-14-7|Theorem §14.7]], after the steps of its proof.

## The Integral Equation

Suppose for the moment that $y = \phi(t)$ is a differentiable function satisfying (2). Then $f(t, \phi(t))$ is a continuous function of $t$ only, and integrating $y' = f(t, y)$ from the initial point $t = 0$ to an arbitrary $t$ (with $\phi(0) = 0$) gives the equation (3) below.

> [!definition] Definition §18.1: Integral Equation
> The equation
>
> $$
> \phi(t) = \int_0^t f(s, \phi(s))\,ds , \qquad (3)
> $$
>
> for an unknown continuous function $\phi$, is the **integral equation** associated with (2). It is called an integral equation because it contains an integral of the unknown function. It is not a formula for the solution, but another relation satisfied by any solution.
>
> *BDP: 2.8 (text)*

^def-14-1

> [!theorem] Lemma §18.2: The Initial Value Problem and the Integral Equation Are Equivalent
> Let $f$ be continuous on $R$, and let $\phi$ be a continuous function on an interval $|t| \le h$ whose graph lies in $R$. Then $\phi$ is a (differentiable) solution of the initial value problem (2) on $|t| \le h$ if and only if it satisfies the integral equation (3) there.
>
> *BDP: 2.8 (text)*

^lem-14-2

> [!proof]+ Proof
> **(2) $\Rightarrow$ (3).** If $\phi' = f(t, \phi(t))$, the right side is continuous, and by the fundamental theorem of calculus ([[§34 Fundamental Theorem of Calculus#^thm-34-1|451 Thm. §34.1]]) $\phi(t) - \phi(0) = \int_0^t \phi'(s)\,ds = \int_0^t f(s, \phi(s))\,ds$; with $\phi(0) = 0$ this is (3).
>
> **(3) $\Rightarrow$ (2).** Substituting $t = 0$ in (3) gives $\phi(0) = 0$: the initial condition holds. The integrand $s \mapsto f(s, \phi(s))$ is continuous, as the composition of continuous functions. So, by the fundamental theorem of calculus ([[§34 Fundamental Theorem of Calculus#^thm-34-4|451 Thm. §34.4]]), the right side of (3) is differentiable with derivative $f(t, \phi(t))$: $\phi$ is differentiable and $\phi'(t) = f(t, \phi(t))$.

^pf-14-2

*Uses:* [[§14 The Existence and Uniqueness Theorem#^def-14-1|Def. §14.1]], [[§34 Fundamental Theorem of Calculus#^thm-34-1|451 Thm. §34.1]], [[§34 Fundamental Theorem of Calculus#^thm-34-4|451 Thm. §34.4]] (the two halves of the FTC)

So it is enough to show that the integral equation (3) has a unique solution on some interval $|t| \le h$.

## The Method of Successive Approximations

> [!definition] Definition §18.2: Picard Iterates
> The **method of successive approximations**, or **Picard's iteration method**, starts from an initial function $\phi_0$, chosen arbitrarily or to approximate the solution in some way; the simplest choice is
>
> $$
> \phi_0(t) = 0 . \qquad (4)
> $$
>
> Substituting $\phi_0(s)$ for $\phi(s)$ in the right side of (3) gives the next approximation, and so on:
>
> $$
> \phi_1(t) = \int_0^t f(s, \phi_0(s))\,ds, \qquad \phi_2(t) = \int_0^t f(s, \phi_1(s))\,ds, \qquad\ldots, \qquad \phi_{n+1}(t) = \int_0^t f(s, \phi_n(s))\,ds . \qquad (5)\text{–}(7)
> $$
>
> The functions $\phi_0, \phi_1, \phi_2, \ldots$ are the **Picard iterates**, and $\{\phi_n\}$ the sequence of successive approximations.
>
> *BDP: 2.8, equations (4)–(7)*

^def-14-2

Each iterate satisfies the initial condition, but in general none satisfies the differential equation. If at some stage $\phi_{k+1}(t) = \phi_k(t)$, then $\phi_k$ is a solution of (3), hence of (2), and the sequence can be stopped; in general this does not happen, and the whole infinite sequence must be considered. Four questions must be answered:
1. Do all members of the sequence $\{\phi_n\}$ exist, or may the process break down at some stage?
2. Does the sequence converge?
3. What are the properties of the limit function? In particular, does it satisfy the integral equation (3), and hence the initial value problem (2)?
4. Is this the only solution, or may there be others?

The uniqueness argument rests on an inequality that BDP proves inside Example 1; here it is first, as a lemma, since it is used twice.

> [!theorem] Lemma §18.3: A Gronwall-Type Inequality
> Let $w$ be continuous and $w(t) \ge 0$ on $[0, c]$, and suppose that for some constant $A > 0$
>
> $$
> w(t) \le A \int_0^t w(s)\,ds \qquad\text{for } 0 \le t \le c .
> $$
>
> Then $w(t) = 0$ for $0 \le t \le c$.
>
> *BDP: Example 2.8.1, equations (17)–(22)*

^lem-14-3

> [!proof]+ Proof
> Let
>
> $$
> U(t) = \int_0^t w(s)\,ds . \qquad (18)
> $$
>
> Then $U(0) = 0$ (19) and $U(t) \ge 0$ for $t \ge 0$ (20), since $w \ge 0$. By the fundamental theorem of calculus $U$ is differentiable with $U'(t) = w(t)$, so the hypothesis says
>
> $$
> U'(t) - AU(t) \le 0 \qquad\text{for } 0 \le t \le c . \qquad (21)
> $$
>
> Multiplying by the positive quantity $e^{-At}$,
>
> $$
> \big(e^{-At}U(t)\big)' = e^{-At}\big(U'(t) - AU(t)\big) \le 0 . \qquad (22)
> $$
>
> So $e^{-At}U(t)$ is nonincreasing on $[0, c]$, and since it is $0$ at $t = 0$, $e^{-At}U(t) \le 0$. Hence $U(t) \le 0$, and with (20), $U(t) = 0$ on $[0, c]$. Then $w(t) = U'(t) = 0$.

^pf-14-3

*Uses:* [[§34 Fundamental Theorem of Calculus#^thm-34-4|451 Thm. §34.4]] (FTC), [[§29 The Mean Value Theorem#^cor-29-7|451 Cor. §29.7]] (a function with nonpositive derivative is nonincreasing)

> [!example] Example §18.1: Picard Iteration for y′ = 2t(1 + y)
> Solve the initial value problem
>
> $$
> y' = 2t(1 + y), \qquad y(0) = 0 \qquad (8)
> $$
>
> by the method of successive approximations.
>
> **The iterates.** If $y = \phi(t)$, the integral equation is
>
> $$
> \phi(t) = \int_0^t 2s\big(1 + \phi(s)\big)\,ds . \qquad (9)
> $$
>
> With $\phi_0(t) = 0$,
>
> $$
> \phi_1(t) = \int_0^t 2s\,ds = t^2, \qquad \phi_2(t) = \int_0^t 2s(1 + s^2)\,ds = t^2 + \frac{t^4}{2}, \qquad \phi_3(t) = \int_0^t 2s\Big(1 + s^2 + \frac{s^4}{2}\Big)ds = t^2 + \frac{t^4}{2} + \frac{t^6}{2 \cdot 3} . \qquad (10)\text{–}(12)
> $$
>
> These suggest
>
> $$
> \phi_n(t) = t^2 + \frac{t^4}{2!} + \frac{t^6}{3!} + \cdots + \frac{t^{2n}}{n!} \qquad (13)
> $$
>
> for each $n \ge 1$. By induction: (13) holds for $n = 1$ by (10), and if it holds for $n = k$, then
>
> $$
> \phi_{k+1}(t) = \int_0^t 2s\Big(1 + s^2 + \frac{s^4}{2!} + \cdots + \frac{s^{2k}}{k!}\Big)ds = \int_0^t \Big(2s + 2s^3 + \frac{2s^5}{2!} + \cdots + \frac{2s^{2k+1}}{k!}\Big)ds = t^2 + \frac{t^4}{2!} + \frac{t^6}{3!} + \cdots + \frac{t^{2k+2}}{(k+1)!} , \qquad (14)
> $$
>
> since $\int_0^t 2s^{2j+1}/j!\,ds = t^{2j+2}/(j+1)!$.
>
> **Convergence.** By (13), $\phi_n(t)$ is the $n$th partial sum of the series
>
> $$
> \sum_{k=1}^{\infty} \frac{t^{2k}}{k!} , \qquad (15)
> $$
>
> so $\lim_{n\to\infty} \phi_n(t)$ exists if and only if (15) converges. By the [[§86 The Ratio and Root Tests#^thm-86-1|ratio test]], for each $t \ne 0$,
>
> $$
> \left| \frac{t^{2k+2}}{(k+1)!} \cdot \frac{k!}{t^{2k}} \right| = \frac{t^2}{k + 1} \to 0 \quad\text{as } k \to \infty , \qquad (16)
> $$
>
> so (15) converges for every $t$: its sum $\phi(t)$ is the limit of $\{\phi_n(t)\}$ for every $t$. Since (15) is a power series converging on the whole line, it can be [[§89 Representations of Functions as Power Series#^thm-89-1|differentiated and integrated term by term]], and direct computation shows that $\phi(t) = \sum_{k \ge 1} t^{2k}/k!$ satisfies (9) (or, substituting into (8), the initial value problem). Here the series can even be identified: $\sum_{k \ge 0} u^k/k! = e^u$ with $u = t^2$ gives
>
> $$
> \phi(t) = e^{t^2} - 1 ,
> $$
>
> and indeed $\phi' = 2te^{t^2} = 2t(1 + \phi)$, $\phi(0) = 0$. (The same solution comes from (8) as a separable or as a linear equation, BDP Problem 2.8.13.) This identification is not needed for existence and uniqueness.
>
> **Uniqueness.** Suppose $\phi$ and $\psi$ both solve (8). Both satisfy (9), so by subtraction and the linearity of integration
>
> $$
> \phi(t) - \psi(t) = \int_0^t 2s\big(\phi(s) - \psi(s)\big)\,ds .
> $$
>
> For $t > 0$, taking absolute values,
>
> $$
> |\phi(t) - \psi(t)| \le \int_0^t 2s\,|\phi(s) - \psi(s)|\,ds .
> $$
>
> Restrict $t$ to $0 \le t \le A/2$, where $A > 0$ is arbitrary; then $2s \le A$ and
>
> $$
> |\phi(t) - \psi(t)| \le A\int_0^t |\phi(s) - \psi(s)|\,ds \qquad\text{for } 0 \le t \le A/2 . \qquad (17)
> $$
>
> By [[§14 The Existence and Uniqueness Theorem#^lem-14-3|Lemma §14.3]] (with $w = |\phi - \psi|$ and $c = A/2$), $\phi = \psi$ on $[0, A/2]$; since $A$ is arbitrary, $\phi(t) = \psi(t)$ for all $t \ge 0$. For $t \le 0$ the same argument applies to $\tilde\phi(\tau) = \phi(-\tau)$ and $\tilde\psi(\tau) = \psi(-\tau)$, $\tau \ge 0$: they satisfy $\tilde\phi(\tau) - \tilde\psi(\tau) = \int_0^\tau 2\sigma\big(\tilde\phi(\sigma) - \tilde\psi(\sigma)\big)d\sigma$ (substitute $s = -\sigma$). So (8) has only one solution.
>
> *BDP: Example 2.8.1*

^ex-14-1

![[m331-11-1.svg]]
*The first four Picard iterates of [[§14 The Existence and Uniqueness Theorem#^ex-14-1|Example §14.1]], $\phi_1 = t^2$, $\phi_2 = t^2 + t^4/2$, $\phi_3$, $\phi_4$, and the solution $\phi = e^{t^2} - 1$ (dashed). As $n$ increases the iterates stay close to $\phi$ over a gradually increasing interval: $\phi - \phi_n$ is the tail $\sum_{k > n} t^{2k}/k!$, which is tiny for $|t| < 1$ and grows quickly beyond.*

## The General Case

From now on $f$ and $\partial f/\partial y$ are continuous on the closed rectangle

$$
R\colon\ |t| \le a, \quad |y| \le b ,
$$

and $\phi_n$ are the Picard iterates (4)–(7). In [[§14 The Existence and Uniqueness Theorem#^ex-14-1|Example §14.1]], $f$ and $\partial f/\partial y$ were continuous in the whole $ty$-plane and every iterate could be computed explicitly. In general $f$ is known to be continuous only in $R$, and the iterates cannot be computed. The danger is that at some stage the graph of $\phi_k$ contains points outside $R$; then computing $\phi_{k+1}$ would require evaluating $f$ where it is not known to be continuous, or even to exist. To avoid this, $t$ may have to be restricted to a smaller interval than $|t| \le a$.

> [!theorem] Lemma §18.4: The Iterates Exist and Stay in a Bow Tie
> Since $f$ is continuous on the closed bounded set $R$, it is bounded there: there is $M \ge 0$ with
>
> $$
> |f(t, y)| \le M, \qquad (t, y) \text{ in } R . \qquad (23)
> $$
>
> Let $h = \min(a, b/M)$ (and $h = a$ if $M = 0$), and let $D$ be the rectangle $|t| \le h$, $|y| \le b$. Then every Picard iterate $\phi_n$ is defined and continuous on $|t| \le h$, and
>
> $$
> |\phi_n(t)| \le M|t| \le b \qquad\text{for } |t| \le h .
> $$
>
> So the graph of every $\phi_n$ lies in the bow tie $|y| \le M|t|$, $|t| \le h$, inside $D \subseteq R$.
>
> *BDP: 2.8 (text, question 1); Problem 2.8.16(a)*

^lem-14-4

> [!proof]+ Proof
> A continuous function on a closed, bounded set in the plane is bounded (the extreme value theorem, [[§113 Maximum and Minimum Values#^thm-113-3|Calc Thm. §113.3]]), which gives $M$. Now induct on $n$. The claim holds for $\phi_0 = 0$. Suppose $\phi_n$ is continuous on $|t| \le h$ with $|\phi_n(t)| \le M|t| \le Mh \le b$. Then $(s, \phi_n(s))$ lies in $D \subseteq R$ for $|s| \le h$, so $s \mapsto f(s, \phi_n(s))$ is defined and continuous there, being a composition of continuous functions. Hence $\phi_{n+1}(t) = \int_0^t f(s, \phi_n(s))\,ds$ is defined, and continuous (even differentiable) by the fundamental theorem of calculus ([[§34 Fundamental Theorem of Calculus#^thm-34-4|451 Thm. §34.4]]), and
>
> $$
> |\phi_{n+1}(t)| = \left| \int_0^t f(s, \phi_n(s))\,ds \right| \le \left| \int_0^t |f(s, \phi_n(s))|\,ds \right| \le M|t| \le Mh \le b ,
> $$
>
> because $|f| \le M$ on $D$. Geometrically: $\phi_n(0) = 0$ and the slope of $\phi_{n+1}$ is $\phi_{n+1}'(t) = f(t, \phi_n(t))$, at most $M$ in absolute value, so the graph of $\phi_{n+1}$ cannot leave the region between the lines $y = \pm Mt$; this region stays inside $R$ as long as $|t| \le b/M$.

^pf-14-4

*Uses:* [[§14 The Existence and Uniqueness Theorem#^def-14-2|Def. §14.2]], [[§113 Maximum and Minimum Values#^thm-113-3|Calc Thm. §113.3]] (extreme value theorem in the plane), [[§34 Fundamental Theorem of Calculus#^thm-34-4|451 Thm. §34.4]], [[§33 Properties of the Riemann Integral#^thm-33-4|451 Thm. §33.4]] ($|\int g| \le \int |g|$)

If $b/M < a$, a larger $h$ may be obtainable by finding a better (smaller) bound $M$ for $|f|$, if this is possible.

![[m331-11-2.svg]]
*The bow tie of [[§14 The Existence and Uniqueness Theorem#^lem-14-4|Lemma §14.4]] when $b/M < a$. Every iterate passes through the origin with slope at most $M$ in absolute value, so its graph (green) stays between the lines $y = \pm Mt$ (orange region). This region stays inside the rectangle $R$ only for $|t| \le b/M$, which is why the theorem gives a solution on $|t| \le h = \min(a, b/M)$ (red dashed lines) rather than on all of $|t| \le a$.*

For the convergence (question 2), write $\phi_n$ as a partial sum of a series:

$$
\phi_n(t) = \phi_1(t) + \big(\phi_2(t) - \phi_1(t)\big) + \cdots + \big(\phi_n(t) - \phi_{n-1}(t)\big) \qquad\text{is the $n$th partial sum of}\qquad \phi_1(t) + \sum_{k=1}^{\infty} \big(\phi_{k+1}(t) - \phi_k(t)\big) , \qquad (24)
$$

and estimate the general term $|\phi_{k+1}(t) - \phi_k(t)|$. This is where $\partial f/\partial y$ enters, through the following condition.

> [!definition] Definition §18.4: Lipschitz Condition
> A function $f(t, y)$ satisfies a **Lipschitz condition** (with respect to $y$) in a region $D$ if there is a constant $K$ such that
>
> $$
> |f(t, y_1) - f(t, y_2)| \le K\,|y_1 - y_2| \qquad (31)
> $$
>
> for any two points $(t, y_1)$ and $(t, y_2)$ in $D$ with the same $t$ coordinate. (Named after Rudolf Lipschitz, 1832–1903.)
>
> *BDP: Problem 2.8.14, equation (31)*

^def-14-3

> [!theorem] Lemma §18.5: A Continuous ∂f/∂y Gives a Lipschitz Condition
> If $\partial f/\partial y$ is continuous on the rectangle $R$, then $f$ satisfies the Lipschitz condition (31) in $R$, with $K$ the maximum value of $|\partial f/\partial y|$ on $R$.
>
> *BDP: Problem 2.8.14*

^lem-14-5

> [!proof]+ Proof
> $|\partial f/\partial y|$ is continuous on the closed bounded set $R$, so it attains a maximum value $K$ there. Let $(t, y_1)$ and $(t, y_2)$ be in $R$, say $y_1 < y_2$. The vertical segment between them lies in $R$, because $R$ is a rectangle. Hold $t$ fixed and apply the mean value theorem to $f$ as a function of $y$ alone on $[y_1, y_2]$: there is $\eta$ between $y_1$ and $y_2$ with
>
> $$
> f(t, y_2) - f(t, y_1) = \frac{\partial f}{\partial y}(t, \eta)\,(y_2 - y_1), \qquad\text{so}\qquad |f(t, y_1) - f(t, y_2)| \le K\,|y_1 - y_2| .
> $$

^pf-14-5

*Uses:* [[§14 The Existence and Uniqueness Theorem#^def-14-3|Def. §14.3]], [[§113 Maximum and Minimum Values#^thm-113-3|Calc Thm. §113.3]] (extreme value theorem), [[§29 The Mean Value Theorem#^thm-29-3|451 Thm. §29.3]] (mean value theorem)

> [!theorem] Lemma §18.6: Estimate of Successive Differences
> With $M$, $h$ as in [[§14 The Existence and Uniqueness Theorem#^lem-14-4|Lemma §14.4]] and $K$ as in [[§14 The Existence and Uniqueness Theorem#^lem-14-5|Lemma §14.5]], for every $n \ge 1$ and $|t| \le h$,
>
> $$
> |\phi_n(t) - \phi_{n-1}(t)| \le \frac{MK^{n-1}|t|^n}{n!} \le \frac{MK^{n-1}h^n}{n!} .
> $$
>
> *BDP: Problems 2.8.15 and 2.8.16*

^lem-14-6

> [!proof]+ Proof
> By [[§14 The Existence and Uniqueness Theorem#^lem-14-4|Lemma §14.4]] the graphs of all iterates lie in $D \subseteq R$, so for $|s| \le h$ the points $(s, \phi_n(s))$ and $(s, \phi_{n-1}(s))$ are in $R$ with the same $s$ coordinate, and by [[§14 The Existence and Uniqueness Theorem#^lem-14-5|Lemma §14.5]] (Problem 15)
>
> $$
> \big|f(s, \phi_n(s)) - f(s, \phi_{n-1}(s))\big| \le K\,|\phi_n(s) - \phi_{n-1}(s)| .
> $$
>
> **$n = 1$.** $|\phi_1(t) - \phi_0(t)| = |\phi_1(t)| \le M|t|$ by [[§14 The Existence and Uniqueness Theorem#^lem-14-4|Lemma §14.4]] (Problem 16(a)).
>
> **Induction.** Suppose the estimate holds for $n$. Then for $|t| \le h$,
>
> $$
> |\phi_{n+1}(t) - \phi_n(t)| = \left| \int_0^t \big[ f(s, \phi_n(s)) - f(s, \phi_{n-1}(s)) \big]\,ds \right| \le \left| \int_0^t K\,|\phi_n(s) - \phi_{n-1}(s)|\,ds \right| \le \left| \int_0^t K\,\frac{MK^{n-1}|s|^n}{n!}\,ds \right| = \frac{MK^n|t|^{n+1}}{(n + 1)!} ,
> $$
>
> which is the estimate for $n + 1$. (For $n = 1$ this is Problem 16(b), $|\phi_2(t) - \phi_1(t)| \le MK|t|^2/2$.) The second inequality in the statement follows from $|t| \le h$.

^pf-14-6

*Uses:* [[§14 The Existence and Uniqueness Theorem#^lem-14-4|§14.4]], [[§14 The Existence and Uniqueness Theorem#^lem-14-5|§14.5]], [[§33 Properties of the Riemann Integral#^thm-33-4|451 Thm. §33.4]], [[§33 Properties of the Riemann Integral#^thm-33-3|451 Thm. §33.3]] (monotonicity of the integral)

Now all four questions can be answered.

> [!theorem] Theorem §18.7: Existence and Uniqueness of Solutions of y′ = f(t, y), y(0) = 0
> If $f$ and $\partial f/\partial y$ are continuous in a rectangle $R\colon |t| \le a$, $|y| \le b$, then there is some interval $|t| \le h \le a$ in which there exists a unique solution $y = \phi(t)$ of the initial value problem (2),
>
> $$
> y' = f(t, y), \qquad y(0) = 0 .
> $$
>
> In fact one can take $h = \min(a, b/M)$, where $M$ bounds $|f|$ on $R$; the solution is the limit of the Picard iterates, which converge to it uniformly on $|t| \le h$; and any solution of (2) on an interval $|t| \le h'$ with $h' \le h$ coincides with $\phi$ there.
>
> *BDP: Theorem 2.8.1 (with $h$ and the uniform convergence from the text of 2.8)*

^thm-14-7

> [!proof]- Proof
> Let $M$, $h$ and $D$ be as in [[§14 The Existence and Uniqueness Theorem#^lem-14-4|Lemma §14.4]] and $K$ as in [[§14 The Existence and Uniqueness Theorem#^lem-14-5|Lemma §14.5]].
>
> **1. All iterates exist.** By [[§14 The Existence and Uniqueness Theorem#^lem-14-4|Lemma §14.4]] every $\phi_n$ is defined and continuous on $I = [-h, h]$, with graph in $D$.
>
> **2. The sequence converges uniformly.** By (24), $\phi_n$ is the $n$th partial sum of the series $\phi_1 + \sum_{k \ge 1}(\phi_{k+1} - \phi_k)$ of continuous functions on $I$. By [[§14 The Existence and Uniqueness Theorem#^lem-14-6|Lemma §14.6]], for every $t$ in $I$,
>
> $$
> |\phi_1(t)| \le Mh, \qquad |\phi_{k+1}(t) - \phi_k(t)| \le \frac{MK^k h^{k+1}}{(k + 1)!} =: M_k \quad (k \ge 1) .
> $$
>
> The constants $M_k$ do not depend on $t$, and their sum converges:
>
> $$
> Mh + \sum_{k=1}^{\infty} M_k = \sum_{n=1}^{\infty} \frac{MK^{n-1}h^n}{n!} = \frac{M}{K}\Big(Kh + \frac{(Kh)^2}{2!} + \cdots\Big) = \frac{M}{K}\big(e^{Kh} - 1\big) < \infty
> $$
>
> if $K > 0$ (the exponential series; if $K = 0$ all terms after the first vanish). This is BDP's Problem 17. By the Weierstrass M-test the series converges uniformly on $I$; that is, $\phi_n$ converges uniformly on $I$ to a function
>
> $$
> \phi(t) = \lim_{n\to\infty} \phi_n(t) . \qquad (25)
> $$
>
> **3. The limit is continuous and satisfies the integral equation.** A uniform limit of continuous functions is continuous ([[§24 Uniform Convergence#^thm-24-2|451 Thm. §24.2]]), so $\phi$ is continuous on $I$. (Continuity is not automatic for a pointwise limit of continuous functions; see [[§14 The Existence and Uniqueness Theorem#^rem-14-1|Remark: What Uniform Convergence Is For]].) Letting $n \to \infty$ in $|\phi_n(t)| \le M|t|$ gives $|\phi(t)| \le M|t| \le b$, so the graph of $\phi$ lies in $D$ too. Now let $n \to \infty$ in (7):
>
> $$
> \phi(t) = \lim_{n\to\infty} \phi_{n+1}(t) = \lim_{n\to\infty} \int_0^t f(s, \phi_n(s))\,ds . \qquad (26)
> $$
>
> We want to take the limit inside the integral and then inside $f$, to arrive at
>
> $$
> \phi(t) = \int_0^t \lim_{n\to\infty} f(s, \phi_n(s))\,ds = \int_0^t f\Big(s, \lim_{n\to\infty} \phi_n(s)\Big)\,ds = \int_0^t f(s, \phi(s))\,ds . \qquad (27)\text{–}(29)
> $$
>
> In general such an interchange is not permissible, but here the integrands converge uniformly. (BDP justifies the step inside $f$ by the continuity of $f$ in its second variable; here is the uniform version that the interchange needs.) By the Lipschitz condition, for all $s$ in $I$,
>
> $$
> \big| f(s, \phi_n(s)) - f(s, \phi(s)) \big| \le K\,|\phi_n(s) - \phi(s)| \le K \sup_{I} |\phi_n - \phi| \longrightarrow 0 ,
> $$
>
> so $f(s, \phi_n(s)) \to f(s, \phi(s))$ uniformly on $I$, and these are continuous functions of $s$. Uniform convergence allows exchanging limit and integral (on $[0, t]$, or on $[t, 0]$ if $t < 0$), which gives (29). So $\phi$ satisfies the integral equation (3) on $I$, and by [[§14 The Existence and Uniqueness Theorem#^lem-14-2|Lemma §14.2]] it is a solution of the initial value problem (2) on $|t| \le h$.
>
> **4. Uniqueness.** Let $\psi$ be any solution of (2) on an interval $|t| \le h'$ with $h' \le h$.
>
> *Its graph stays in $D$.* (BDP's Problem 18 assumes this; here is why it holds.) Let $\tau$ be the supremum of the $t \in [0, h']$ such that $|\psi(s)| \le b$ for all $0 \le s \le t$; the set contains $0$, and by continuity $|\psi| \le b$ on $[0, \tau]$. On $[0, \tau]$ the points $(s, \psi(s))$ lie in $R$, so $|\psi'(s)| = |f(s, \psi(s))| \le M$, and by the mean value inequality $|\psi(t)| \le Mt$. If $\tau < h'$, then $|\psi(\tau)| \le M\tau < b$ (if $M > 0$, because $M\tau < Mh \le b$; if $M = 0$, because $b > 0$), and by continuity $|\psi| < b$ on a slightly longer interval $[0, \tau + \varepsilon]$, contradicting the choice of $\tau$. So $|\psi(t)| \le b$ on $[0, h']$, and in the same way on $[-h', 0]$.
>
> *The estimate.* Both $\phi$ and $\psi$ satisfy the integral equation (3) on $|t| \le h'$ ([[§14 The Existence and Uniqueness Theorem#^lem-14-2|Lemma §14.2]]). Subtracting, for $0 \le t \le h'$ (Problem 18(a)–(c)),
>
> $$
> |\phi(t) - \psi(t)| = \left| \int_0^t \big[f(s, \phi(s)) - f(s, \psi(s))\big]\,ds \right| \le \int_0^t \big| f(s, \phi(s)) - f(s, \psi(s)) \big|\,ds \le K \int_0^t |\phi(s) - \psi(s)|\,ds , \qquad (30)
> $$
>
> using the Lipschitz condition, which applies because both graphs lie in $D$. This is the inequality (17) of [[§14 The Existence and Uniqueness Theorem#^ex-14-1|Example §14.1]] with $A = K$ (replace $K$ by $K + 1$ if $K = 0$, so that $A > 0$). By [[§14 The Existence and Uniqueness Theorem#^lem-14-3|Lemma §14.3]] with $w = |\phi - \psi|$, $\phi = \psi$ on $[0, h']$. For $-h' \le t \le 0$, apply the same argument to $\tilde\phi(\tau) = \phi(-\tau)$ and $\tilde\psi(\tau) = \psi(-\tau)$: the substitution $s = -\sigma$ gives $|\tilde\phi(\tau) - \tilde\psi(\tau)| \le K\int_0^\tau |\tilde\phi(\sigma) - \tilde\psi(\sigma)|\,d\sigma$ for $0 \le \tau \le h'$, and [[§14 The Existence and Uniqueness Theorem#^lem-14-3|Lemma §14.3]] again gives $\tilde\phi = \tilde\psi$. So there is no solution of (2) other than the one generated by the method of successive approximations.

^pf-14-7

*Uses:* [[§14 The Existence and Uniqueness Theorem#^lem-14-2|§14.2]], [[§14 The Existence and Uniqueness Theorem#^lem-14-3|§14.3]], [[§14 The Existence and Uniqueness Theorem#^lem-14-4|§14.4]], [[§14 The Existence and Uniqueness Theorem#^lem-14-5|§14.5]], [[§14 The Existence and Uniqueness Theorem#^lem-14-6|§14.6]], [[§25 More on Uniform Convergence#^thm-25-3|451 Thm. §25.3]] (Weierstrass M-test), [[§24 Uniform Convergence#^thm-24-2|451 Thm. §24.2]] (uniform limits of continuous functions are continuous), [[§25 More on Uniform Convergence#^thm-25-1|451 Thm. §25.1]] (exchanging limit and integral), [[§90 Taylor and Maclaurin Series#^thm-90-6|Calc Thm. §90.6]] (the exponential series), [[§29 The Mean Value Theorem#^prop-29-8|451 Prop. §29.8]] (mean value inequality)

> [!remark]- Connections
> - Rigorous tools, all from Single Variable Analysis: uniform convergence, [[§24 Uniform Convergence#^def-24-2|451 Def. §24.2]]; the Weierstrass M-test, [[§25 More on Uniform Convergence#^thm-25-3|451 Thm. §25.3]], applied to the series (24) with $M_k = MK^kh^{k+1}/(k+1)!$; continuity of the limit, [[§24 Uniform Convergence#^thm-24-2|451 Thm. §24.2]]; and the exchange of limit and integral, [[§25 More on Uniform Convergence#^thm-25-1|451 Thm. §25.1]] and [[§33 Properties of the Riemann Integral#^thm-33-12|451 Thm. §33.12]]. No other subject in the vault proves the existence and uniqueness theorem; this proof is its home.
> - In the language of Functional Analysis: the map $T\phi(t) = \int_0^t f(s, \phi(s))\,ds$ sends continuous functions on $[-h, h]$ with graph in $D$ to themselves ([[§14 The Existence and Uniqueness Theorem#^lem-14-4|Lemma §14.4]]), a solution is a fixed point $T\phi = \phi$, and [[§14 The Existence and Uniqueness Theorem#^lem-14-6|Lemma §14.6]] says $\|T^n\phi_0 - T^{n-1}\phi_0\|_\infty \le MK^{n-1}h^n/n!$. So the iterates form a Cauchy sequence ([[§10 Normed Linear Spaces#^def-10-5|556 Def. §10.5]]) in $\big(C[-h, h], \|\cdot\|_\infty\big)$, which is complete, [[§11 Completeness#^thm-11-1|556 Thm. §11.1]]: this is the abstract reason the iterates converge.

> [!remark]- Remark: What Uniform Convergence Is For
> Two of BDP's problems show why step 3 of the proof needs uniform convergence.
> - A sequence of continuous functions can converge pointwise to a discontinuous function: $\phi_n(x) = x^n$ on $0 \le x \le 1$ tends to $0$ for $x < 1$ and to $1$ at $x = 1$ (BDP Problem 2.8.11; [[§24 Uniform Convergence#^ex-24-2|451 Ex. §24.2]]).
> - Limit and integral cannot always be exchanged, even when the limit exists and is continuous: $\phi_n(x) = 2nxe^{-nx^2}$ tends to $0$ for every $0 \le x \le 1$, so $\int_0^1 \lim \phi_n\,dx = 0$, but $\int_0^1 2nxe^{-nx^2}\,dx = 1 - e^{-n} \to 1$ (BDP Problem 2.8.12; compare the escaping triangle of [[§25 More on Uniform Convergence#^ex-25-1|451 Ex. §25.1]]).
>
> In both cases the convergence is not uniform. The M-test estimate of step 2 guarantees uniform convergence of the Picard iterates, which rules out both failures.

^rem-14-1

> [!remark] Remark: A Lipschitz Condition Is Enough
> The proof used the continuity of $\partial f/\partial y$ only through the Lipschitz condition ([[§14 The Existence and Uniqueness Theorem#^lem-14-5|Lemma §14.5]]): steps 2–4 need just $|f(t, y_1) - f(t, y_2)| \le K|y_1 - y_2|$. So [[§14 The Existence and Uniqueness Theorem#^thm-14-7|Theorem §14.7]] remains true, with the same proof, if the hypothesis "$\partial f/\partial y$ is continuous" is replaced by "$f$ satisfies a Lipschitz condition in $R$", a slightly stronger theorem. For example, $f(t, y) = |y|$ is not differentiable in $y$ at $y = 0$, but $\big||y_1| - |y_2|\big| \le |y_1 - y_2|$, so $y' = |y|$, $y(0) = 0$ has the unique solution $y = 0$. By contrast $f(y) = y^{1/3}$ satisfies no Lipschitz condition near $y = 0$ (the quotient $y^{1/3}/y = y^{-2/3}$ is unbounded), and [[§8 Differences Between Linear and Nonlinear Differential Equations#^ex-8-3|Example §8.3]] shows that uniqueness then fails.

^rem-14-2

Translating back to an arbitrary initial point gives the theorem as stated in Section 2.4.

> [!theorem] Theorem §18.8: Existence and Uniqueness for First-Order Nonlinear Equations
> Let the functions $f$ and $\partial f/\partial y$ be continuous in some rectangle $\alpha < t < \beta$, $\gamma < y < \delta$ containing the point $(t_0, y_0)$. Then, in some interval $t_0 - h < t < t_0 + h$ contained in $\alpha < t < \beta$, there is a unique solution $y = \phi(t)$ of the initial value problem
>
> $$
> y' = f(t, y), \qquad y(t_0) = y_0 . \qquad (9)
> $$
>
> *BDP: Theorem 2.4.2*

^thm-14-8

> [!proof]+ Proof
> Since the rectangle is open, choose $a, b > 0$ so small that the closed rectangle $|t - t_0| \le a$, $|y - y_0| \le b$ lies inside it; $f$ and $\partial f/\partial y$ are continuous there. By [[§14 The Existence and Uniqueness Theorem#^lem-14-1|Lemma §14.1]], $g(s, w) = f(t_0 + s, y_0 + w)$ and $\partial g/\partial w$ are continuous on $|s| \le a$, $|w| \le b$. [[§14 The Existence and Uniqueness Theorem#^thm-14-7|Theorem §14.7]] gives $h$ with $0 < h \le a$ and a unique solution $\psi$ of $w' = g(s, w)$, $w(0) = 0$ on $|s| \le h$. By [[§14 The Existence and Uniqueness Theorem#^lem-14-1|Lemma §14.1]], $\phi(t) = y_0 + \psi(t - t_0)$ solves (9) on $|t - t_0| \le h$, in particular on $t_0 - h < t < t_0 + h$, which lies in $(\alpha, \beta)$ since $h \le a$.
>
> For uniqueness, let $\chi$ be another solution of (9) on $t_0 - h < t < t_0 + h$, and let $0 < h' < h$. On $|t - t_0| \le h'$, $\chi(t_0 + s) - y_0$ solves the translated problem on $|s| \le h'$ ([[§14 The Existence and Uniqueness Theorem#^lem-14-1|Lemma §14.1]]), so by the last statement of [[§14 The Existence and Uniqueness Theorem#^thm-14-7|Theorem §14.7]] it equals $\psi$ there; that is, $\chi = \phi$ on $|t - t_0| \le h'$. Since $h' < h$ was arbitrary, $\chi = \phi$ on the whole interval.

^pf-14-8

*Uses:* [[§14 The Existence and Uniqueness Theorem#^lem-14-1|§14.1]], [[§14 The Existence and Uniqueness Theorem#^thm-14-7|§14.7]]

[[§14 The Existence and Uniqueness Theorem#^thm-14-8|Theorem §14.8]] contains the linear theorem's hypotheses as a special case ([[§8 Differences Between Linear and Nonlinear Differential Equations#^rem-8-1|Remark: Reading Theorem 2.4.2]]) and gives the geometric consequence that solution curves do not cross ([[§8 Differences Between Linear and Nonlinear Differential Equations#^cor-8-3|Corollary §8.3]]). The value $h = \min(a, b/M)$ is usually far from the true interval of existence, as the next example shows.

> [!example] Example §18.2: The Interval Given by the Proof
> For $y' = y^2$, $y(0) = 1$ ([[§8 Differences Between Linear and Nonlinear Differential Equations#^ex-8-4|Example §8.4]]), compare the interval of existence guaranteed by the proof with the true one.
>
> **Translate.** With $w = y - 1$ ([[§14 The Existence and Uniqueness Theorem#^lem-14-1|Lemma §14.1]]), the problem is $w' = (1 + w)^2$, $w(0) = 0$. On the rectangle $|t| \le a$, $|w| \le b$,
>
> $$
> M = \max |g| = (1 + b)^2, \qquad K = \max \Big|\frac{\partial g}{\partial w}\Big| = \max |2(1 + w)| = 2(1 + b) ,
> $$
>
> so the proof gives a solution on $|t| \le h = \min\big(a,\ b/(1 + b)^2\big)$. Since $f$ is continuous everywhere, $a$ can be as large as we like, and the best choice of $b$ maximizes $b/(1 + b)^2$: its derivative $\big((1 + b)^2 - 2b(1 + b)\big)/(1 + b)^4 = (1 - b)/(1 + b)^3$ vanishes at $b = 1$, giving the value $\frac14$. So [[§14 The Existence and Uniqueness Theorem#^thm-14-7|Theorem §14.7]] guarantees the solution on $|t| \le \frac14$.
>
> **The truth.** The solution $y = 1/(1 - t)$ exists on $-\infty < t < 1$. The interval from the proof is correct but much too small, and it is symmetric about $t = 0$, whereas the true interval is not.
>
> **The iterates.** In the original variables ($\phi_0 = 1$, $\phi_{n+1}(t) = 1 + \int_0^t \phi_n(s)^2\,ds$, the translate of [[§14 The Existence and Uniqueness Theorem#^def-14-2|Definition §14.2]]),
>
> $$
> \phi_1 = 1 + t, \qquad \phi_2 = 1 + t + t^2 + \frac{t^3}{3}, \qquad \phi_3 = 1 + t + t^2 + t^3 + \frac23 t^4 + \frac13 t^5 + \frac19 t^6 + \frac{1}{63}t^7 ,
> $$
>
> which agree with the geometric series $\frac{1}{1 - t} = 1 + t + t^2 + \cdots$ in more and more terms (through $t^n$ for $\phi_n$).
>
> *BDP: Example 2.4.4 (the problem); the analysis by Theorem 2.8.1 is added*

^ex-14-2
