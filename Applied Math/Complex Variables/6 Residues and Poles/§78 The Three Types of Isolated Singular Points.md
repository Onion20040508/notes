---
type: section
subject: "[[Complex Variables]]"
chapter: 6
section: 78
bc: "78"
aliases: ["B&C 78"]
tags: [complex-variables, math342]
---
← [[§77★ Residue at Infinity]] · ↑ [[· 6 Residues and Poles]] · [[§79 Examples (The Three Types of Isolated Singular Points)]] →

*Brown–Churchill, Section 78 · MAT 342 Practice Finals (Spring 2005, Fall 1999).*

The negative powers in the Laurent series of $f$ at an isolated singular point form its **principal part**, and the principal part sorts isolated singular points into three types. If it is zero, the singular point is **removable**: redefining $f$ at one point makes it analytic there. If it has infinitely many nonzero terms, the point is an **essential singular point**. In between, a principal part with finitely many terms, the last of them $b_m/(z - z_0)^m$, makes $z_0$ a **pole of order $m$**. The classification organizes the rest of the chapter: residues at poles have convenient formulas ([[§80 Residues at Poles#^thm-80-1|Theorem §80.1]]), and the three types behave very differently near the point ([[§84 Behavior of Functions Near Isolated Singular Points|§84]]).

## The Principal Part

Recall ([[§75 Residues|§75]]) that if $f$ has an isolated singular point at $z_0$, then $f(z)$ has a Laurent series representation

$$
f(z) = \sum_{n=0}^{\infty} a_n(z - z_0)^n + \frac{b_1}{z - z_0} + \frac{b_2}{(z - z_0)^2} + \cdots + \frac{b_n}{(z - z_0)^n} + \cdots \qquad (1)
$$

in a punctured disk $0 < |z - z_0| < R_2$.

> [!definition] Definition §78.1: Principal Part
> The portion
>
> $$
> \frac{b_1}{z - z_0} + \frac{b_2}{(z - z_0)^2} + \cdots + \frac{b_n}{(z - z_0)^n} + \cdots \qquad (2)
> $$
>
> of the Laurent series (1), involving the negative powers of $z - z_0$, is called the **principal part** of $f$ at $z_0$.
>
> *B&C: Sec. 78 (text)*

^def-78-1

> [!remark]- Connections
> - For a rational function $f = P/Q$ with $\deg P < \deg Q$, the principal part at each zero of $Q$ is a finite sum $\sum_{k \le m} b_k/(z - z_0)^k$. Subtracting the principal parts at all the zeros of $Q$ leaves an entire function that tends to $0$ as $z \to \infty$, hence is bounded and so identically $0$ ([[§58 Liouville's Theorem and the Fundamental Theorem of Algebra#^thm-58-1|Theorem §58.1]], Liouville's theorem): $f$ is the sum of its principal parts. This is the partial-fraction decomposition, which [[§47 Integration of Rational Functions by Partial Fractions#^thm-47-3|Calc Thm. §47.3]] states without proof. The coefficients $b_k$ are the partial-fraction coefficients, and $b_1$ is the residue; compare [[§52★ Partial Fractions and Convolutions#^thm-52-2|341 Thm. §52.2]] (Heaviside's formula).

There are two extremes: the case in which every coefficient in the principal part (2) is zero, and the case in which infinitely many of them are nonzero.

## The Three Types

> [!definition] Definition §78.2: Removable Singular Point
> If every $b_n$ in (1) is zero, so that
>
> $$
> f(z) = \sum_{n=0}^{\infty} a_n(z - z_0)^n = a_0 + a_1(z - z_0) + a_2(z - z_0)^2 + \cdots \qquad (0 < |z - z_0| < R_2), \qquad (3)
> $$
>
> then $z_0$ is called a **removable singular point** of $f$.
>
> *B&C: Sec. 78 (a)*

^def-78-2

> [!theorem] Proposition §78.1: A Removable Singular Point Can Be Removed
> Let $z_0$ be a removable singular point of $f$, with expansion (3). Then:
>
> **(a)** the residue of $f$ at $z_0$ is zero;
>
> **(b)** if $f$ is defined, or redefined, at $z_0$ so that $f(z_0) = a_0$, then expansion (3) becomes valid throughout the entire disk $|z - z_0| < R_2$, and $f$ is analytic at $z_0$. The singularity $z_0$ is then *removed*.
>
> *B&C: Sec. 78 (a) (text)*

^prop-78-1

> [!proof]+ Proof
> **(a)** The residue is the coefficient $b_1$, which is $0$.
>
> **(b)** At $z = z_0$ the power series $\sum a_n(z - z_0)^n$ has the sum $a_0$, which is now also the value of $f$; for $0 < |z - z_0| < R_2$ the series equals $f(z)$ by (3). So (3) holds for $|z - z_0| < R_2$, and the power series converges throughout this disk; its circle of convergence therefore has radius at least $R_2$. Since a power series represents an analytic function at each point interior to its circle of convergence ([[§71★ Integration and Differentiation of Power Series#^cor-71-2|Corollary §71.2]]), $f$ is analytic at every point of $|z - z_0| < R_2$, in particular at $z_0$.

^pf-78-1

*Uses:* [[§78 The Three Types of Isolated Singular Points#^def-78-2|Def. §78.2]], [[§75 Residues#^def-75-1|Def. §75.1]], [[§71★ Integration and Differentiation of Power Series#^cor-71-2|§71.2]] (power series are analytic)

> [!definition] Definition §78.3: Essential Singular Point
> If an infinite number of the coefficients $b_n$ in the principal part (2) are nonzero, $z_0$ is said to be an **essential singular point** of $f$.
>
> *B&C: Sec. 78 (b)*

^def-78-3

> [!definition] Definition §78.4: Pole of Order m
> If the principal part of $f$ at $z_0$ contains at least one nonzero term but the number of such terms is only finite, then there is a positive integer $m$ ($m \ge 1$) such that
>
> $$
> b_m \ne 0 \qquad\text{and}\qquad b_{m+1} = b_{m+2} = \cdots = 0 .
> $$
>
> That is, expansion (1) takes the form
>
> $$
> f(z) = \sum_{n=0}^{\infty} a_n(z - z_0)^n + \frac{b_1}{z - z_0} + \frac{b_2}{(z - z_0)^2} + \cdots + \frac{b_m}{(z - z_0)^m} \qquad (0 < |z - z_0| < R_2), \qquad (4)
> $$
>
> where $b_m \ne 0$. In this case the [[§74 Isolated Singular Points#^def-74-1|isolated singular point]] $z_0$ is called a **pole of order $m$**. A pole of order $m = 1$ is usually referred to as a **simple pole**.
>
> *B&C: Sec. 78 (c)*

^def-78-4

Every isolated singular point is of exactly one of the three types: the number of nonzero $b_n$ is either zero, finite and positive, or infinite. The type is well defined because the Laurent series in a punctured disk is unique ([[§72★ Uniqueness of Series Representations#^thm-72-4|Theorem §72.4]]). (On the name *pole*: B&C refers to books by Wunsch and by Boas. The reason is [[§84 Behavior of Functions Near Isolated Singular Points#^thm-84-4|Theorem §84.4]]: near a pole $|f(z)|$ increases without bound, so the graph of $|f|$ over the plane rises above $z_0$ like a pole in the everyday sense.)

> [!remark] Remark: Method — Classifying an Isolated Singular Point
> 1. **Laurent series.** Write the principal part at $z_0$ and count its nonzero terms: none, removable; finitely many with the last one $b_m/(z - z_0)^m$, pole of order $m$; infinitely many, essential. This always works, and is the only method that recognizes an essential singular point directly ([[§79 Examples (The Three Types of Isolated Singular Points)|§79]]).
> 2. **Factor out a power.** If $f(z) = \phi(z)/(z - z_0)^m$ with $\phi$ analytic and nonzero at $z_0$, then $z_0$ is a pole of order $m$ ([[§80 Residues at Poles#^thm-80-1|Theorem §80.1]]). Beware: $\phi(z_0) = 0$ or $\phi$ not analytic at $z_0$ invalidates the conclusion ([[§81 Examples (Residues at Poles)#^ex-81-3|Example §81.3]]).
> 3. **Zeros of a denominator.** If $f = p/q$ with $p(z_0) \ne 0$ and $q$ having a zero of order $m$ at $z_0$, the pole has order $m$ ([[§83 Zeros and Poles#^thm-83-1|Theorem §83.1]]). If $p$ also vanishes at $z_0$, compare the orders of the two zeros.
> 4. **Behavior.** Bounded near $z_0$: removable. $|f(z)| \to \infty$: pole. Neither: essential ([[§84 Behavior of Functions Near Isolated Singular Points#^rem-84-1|Remark: Telling the Three Types Apart by Behavior]]).
>
> A residue of $0$ does not mean the point is removable ([[§78 The Three Types of Isolated Singular Points#^ex-78-1|Example §78.1]]).

^rem-78-1

## Examples

The essential singular point of $\sin(1/z)$ at the origin, with residue $1$, is the key to a final-exam integral: on the unit circle $\bar z = 1/z$, so $\int_{|z|=1}\sin(\bar z)\,dz = \int_{|z|=1}\sin(1/z)\,dz = 2\pi i$, although $\sin(\bar z)$ is analytic nowhere. It is worked in [[§68 Examples (Proof of Laurent's Theorem)#^ex-68-4|Example §68.4]](c).

> [!example] Example §78.1: A Zero Residue Does Not Make a Point Removable
> True or false: if $f$ has an isolated singularity at $z_0$ and $\operatorname{Res}_{z=z_0} f = 0$, then $z_0$ is a removable singularity.
>
> **False.** The residue is only the coefficient $b_1$; removability requires *all* $b_n$ to vanish. Counterexamples:
> - $f(z) = 1/z^2$: its Laurent series about $0$ is the single term $1/z^2$, so $b_1 = 0$ but $b_2 = 1$: a pole of order $2$ with residue $0$.
> - $f(z) = \cosh(1/z^2) = 1 + \frac{1}{2!\,z^4} + \frac{1}{4!\,z^8} + \cdots$ ([[§75 Residues#^ex-75-2|Example §75.2]]): residue $0$, but infinitely many nonzero $b_n$, so an essential singular point.
>
> (The converse is true: at a removable singular point the residue is $0$, [[§78 The Three Types of Isolated Singular Points#^prop-78-1|Proposition §78.1]](a).)
>
> *Source: 342 practice final (Fall 1999), Q7(c)*

^ex-78-1

> [!example] Example §78.2: Vanishing Moments Make a Singularity Removable
> Let $C$ be the circle $|z| = 1$, oriented counterclockwise. Assume that $f$ is analytic in the punctured disk $0 < |z| < 2$ and that $\int_C z^nf(z)\,dz = 0$ for all integers $n \ge 0$. True or false: $0$ is a removable singularity of $f$.
>
> **True.** $f$ has a Laurent series $\sum_{k=-\infty}^{\infty} c_kz^k$ in $0 < |z| < 2$, and $C$ is a positively oriented simple closed contour around $0$ in that annulus, so by Laurent's theorem ([[§67 Proof of Laurent's Theorem#^thm-67-1|Theorem §67.1]])
>
> $$
> c_k = \frac{1}{2\pi i}\int_C\frac{f(z)}{z^{k+1}}\,dz \qquad (k \in \mathbb{Z}) .
> $$
>
> For $k = -n - 1$ with $n \ge 0$, that is, for every $k \le -1$, this is $c_{-n-1} = \frac{1}{2\pi i}\int_C z^nf(z)\,dz = 0$. So every coefficient of a negative power vanishes: the principal part is zero and $0$ is a removable singular point. Conversely, at a removable singular point all these integrals are $0$ by the Cauchy–Goursat theorem ([[§51 Proof of the Theorem (Cauchy–Goursat Theorem)#^thm-51-3|Theorem §51.3]]), once $f$ is made analytic at $0$ ([[§78 The Three Types of Isolated Singular Points#^prop-78-1|Proposition §78.1]]).
>
> *Source: 342 practice final (Spring 2005), Q8(a)*

^ex-78-2

> [!example] Example §78.3: One Singular Point of Each Kind of Principal Part
> Write the principal part of each function at its isolated singular point, and classify the point:
>
> $$
> \text{(a)}\ \frac{\sin z}{z}; \qquad \text{(b)}\ \frac{1}{(2 - z)^3}; \qquad \text{(c)}\ \frac{1 - \cosh z}{z^3} .
> $$
>
> **(a)** The singular point is $0$. From the Maclaurin series of $\sin z$,
>
> $$
> \frac{\sin z}{z} = \frac1z\Big(z - \frac{z^3}{3!} + \frac{z^5}{5!} - \cdots\Big) = 1 - \frac{z^2}{3!} + \frac{z^4}{5!} - \cdots \qquad (0 < |z| < \infty) .
> $$
>
> The principal part is zero: a **removable singular point**; with the value $1$ at $0$ the function is entire ([[§78 The Three Types of Isolated Singular Points#^prop-78-1|Proposition §78.1]]).
>
> **(b)** The singular point is $2$, and $(2 - z)^3 = -(z - 2)^3$, so
>
> $$
> \frac{1}{(2 - z)^3} = \frac{-1}{(z - 2)^3} \qquad (0 < |z - 2| < \infty)
> $$
>
> is already its own Laurent series. The principal part is $-1/(z - 2)^3$, with $b_3 = -1 \ne 0$ and every other $b_n = 0$: a **pole of order $3$**, with residue $b_1 = 0$.
>
> **(c)** The singular point is $0$. From the Maclaurin series of $\cosh z$,
>
> $$
> \frac{1 - \cosh z}{z^3} = -\frac{1}{z^3}\Big(\frac{z^2}{2!} + \frac{z^4}{4!} + \frac{z^6}{6!} + \cdots\Big) = -\frac{1}{2}\cdot\frac1z - \frac{z}{4!} - \frac{z^3}{6!} - \cdots \qquad (0 < |z| < \infty) .
> $$
>
> The principal part is $-\frac{1}{2z}$: a **simple pole**, with residue $-\frac12$, although the denominator is $z^3$. (The numerator vanishes to order $2$ at $0$ and cancels two powers of $z$.)
>
> *B&C: Sec. 79, Exercises 1(c), 1(e) and 2(a)*

^ex-78-3
