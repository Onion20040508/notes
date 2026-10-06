---
type: section
subject: "[[Calculus]]"
chapter: 11
section: 76
stewart: "11.8"
aliases: ["Stewart 11.8"]
tags: [calculus]
---
← [[§75 Strategy for Testing Series]] · ↑ [[· 11 Sequences, Series, and Power Series]] · [[§77 Representations of Functions as Power Series]] →

*Stewart, Section 11.8.*

A power series $\sum c_n (x - a)^n$ is a "polynomial with infinitely many terms": for each $x$ it is a series of numbers, which may converge or diverge, and where it converges it defines a function of $x$. The set where it converges is always an interval centered at $a$: a single point, the whole line, or an interval of radius $R$ whose endpoints must be checked one at a time. The radius is found with the Ratio (or Root) Test ([[§74 The Ratio and Root Tests#^thm-74-1|Theorem §74.1]], [[§74 The Ratio and Root Tests#^thm-74-2|Theorem §74.2]]), and the endpoints with the tests of [[§71 The Integral Test and Estimates of Sums|§71]]–[[§73 Alternating Series and Absolute Convergence|§73]]. The next three sections use power series to represent functions.

## Power Series

> [!definition] Definition §76.1: Power Series
> A **power series** is a series of the form
>
> $$
> \sum_{n=0}^{\infty} c_n x^n = c_0 + c_1 x + c_2 x^2 + c_3 x^3 + \cdots \qquad (1)
> $$
>
> where $x$ is a variable and the $c_n$ are constants, the **coefficients** of the series. For each number substituted for $x$, (1) is a series of constants that may converge or diverge. The sum of the series is the function
>
> $$
> f(x) = c_0 + c_1 x + c_2 x^2 + \cdots + c_n x^n + \cdots
> $$
>
> whose domain is the set of all $x$ for which the series converges.
>
> *Stewart: 11.8, Equation 1*

^def-76-1

For instance, with $c_n = 1$ for all $n$ we get the geometric series $\sum_{n=0}^{\infty} x^n = 1 + x + x^2 + \cdots$, which converges when $-1 < x < 1$ and diverges when $|x| \ge 1$ ([[§70 Series#^cor-70-2|Corollary §70.2]]): $x = \frac12$ gives the convergent series $1 + \frac12 + \frac14 + \cdots$, and $x = 2$ gives the divergent series $1 + 2 + 4 + \cdots$.

> [!definition] Definition §76.2: Power Series Centered at a
> A series of the form
>
> $$
> \sum_{n=0}^{\infty} c_n (x - a)^n = c_0 + c_1 (x - a) + c_2 (x - a)^2 + \cdots \qquad (3)
> $$
>
> is a **power series in $(x - a)$**, or a **power series centered at $a$**, or a **power series about $a$**.
>
> In the term for $n = 0$ in (1) and (3) we use the convention $(x - a)^0 = 1$ even when $x = a$. With it, all terms with $n \ge 1$ vanish at $x = a$, so a power series (3) always converges when $x = a$, with sum $c_0$.
>
> *Stewart: 11.8, Equation 3*

^def-76-2

> [!remark]- Connections
> - Rigorous treatment: [[§23 Power Series#^def-23-1|451 Def. §23.1]] (centered at $0$; the general center is the substitution $u = x - a$ used below).

To determine the values of $x$ for which a power series converges, we normally use the Ratio (or Root) Test.

> [!example] Example §76.1: A Finite Interval with One Endpoint
> For what values of $x$ does $\displaystyle\sum_{n=1}^{\infty} \frac{(x - 3)^n}{n}$ converge?
>
> **Ratio Test.** With $a_n = (x - 3)^n / n$,
>
> $$
> \left| \frac{a_{n+1}}{a_n} \right| = \left| \frac{(x - 3)^{n+1}}{n + 1} \cdot \frac{n}{(x - 3)^n} \right| = \frac{1}{1 + \dfrac1n} |x - 3| \to |x - 3| \qquad \text{as } n \to \infty .
> $$
>
> So the series is absolutely convergent, hence convergent, when $|x - 3| < 1$, and divergent when $|x - 3| > 1$. Now $|x - 3| < 1 \iff -1 < x - 3 < 1 \iff 2 < x < 4$: the series converges when $2 < x < 4$ and diverges when $x < 2$ or $x > 4$.
>
> **Endpoints.** The Ratio Test gives no information when $|x - 3| = 1$, so test $x = 2$ and $x = 4$ separately. At $x = 4$ the series is $\sum 1/n$, the harmonic series, which diverges. At $x = 2$ it is $\sum (-1)^n / n$, which converges by the Alternating Series Test.
>
> So the power series converges for $2 \le x < 4$.
>
> *Stewart: Example 11.8.1*

^ex-76-1

> [!example] Example §76.2: Converging Only at the Center, or Everywhere
> **(a)** For what values of $x$ is $\displaystyle\sum_{n=0}^{\infty} n!\,x^n$ convergent?
>
> Let $a_n = n!\,x^n$. If $x \ne 0$, then, since $(n+1)! = (n+1)\,n!$,
>
> $$
> \lim_{n \to \infty} \left| \frac{a_{n+1}}{a_n} \right| = \lim_{n \to \infty} \left| \frac{(n+1)!\,x^{n+1}}{n!\,x^n} \right| = \lim_{n \to \infty} (n + 1)|x| = \infty .
> $$
>
> By the Ratio Test the series diverges when $x \ne 0$. It converges only when $x = 0$.
>
> **(b)** For what values of $x$ does $\displaystyle\sum_{n=0}^{\infty} \frac{x^n}{(2n)!}$ converge?
>
> Here $a_n = x^n / (2n)!$, and $[2(n+1)]! = (2n+2)! = (2n)!\,(2n+1)(2n+2)$, so
>
> $$
> \left| \frac{a_{n+1}}{a_n} \right| = \left| \frac{x^{n+1}}{[2(n+1)]!} \cdot \frac{(2n)!}{x^n} \right| = \frac{(2n)!}{(2n)!\,(2n+1)(2n+2)} |x| = \frac{|x|}{(2n+1)(2n+2)} \to 0 < 1
> $$
>
> for all $x$. By the Ratio Test the series converges for all values of $x$.
>
> *Stewart: Examples 11.8.2 and 11.8.3*

^ex-76-2

## Interval of Convergence

In these examples the set where the series converges is an interval: finite for the geometric series and Example §76.1, the infinite interval $(-\infty, \infty)$ in Example §76.2(b), and the collapsed interval $[0, 0] = \{0\}$ in Example §76.2(a). This is true in general. Stewart's proof in Appendix F rests on two preliminary results about series centered at $0$.

> [!theorem] Lemma §76.1: Convergence Spreads Inward, Divergence Outward
> 1. If a power series $\sum c_n x^n$ converges when $x = b$ (where $b \ne 0$), then it converges whenever $|x| < |b|$.
> 2. If a power series $\sum c_n x^n$ diverges when $x = d$ (where $d \ne 0$), then it diverges whenever $|x| > |d|$.
>
> *Stewart: Appendix F (Section 11.8, Theorem)*

^lem-76-1

> [!proof]+ Proof
> **1.** Suppose $\sum c_n b^n$ converges. Then $\lim_{n \to \infty} c_n b^n = 0$ ([[§70 Series#^thm-70-4|Theorem §70.4]]). By [[§69 Sequences#^def-69-3|Definition §69.3]] with $\varepsilon = 1$, there is a positive integer $N$ such that $|c_n b^n| < 1$ whenever $n \ge N$. Thus, for $n \ge N$,
>
> $$
> |c_n x^n| = \left| \frac{c_n b^n x^n}{b^n} \right| = |c_n b^n| \left| \frac{x}{b} \right|^n < \left| \frac{x}{b} \right|^n .
> $$
>
> If $|x| < |b|$, then $|x/b| < 1$, so $\sum |x/b|^n$ is a convergent geometric series. By the Direct Comparison Test, $\sum_{n=N}^{\infty} |c_n x^n|$ is convergent. Thus $\sum c_n x^n$ is absolutely convergent and therefore convergent.
>
> **2.** Suppose $\sum c_n d^n$ diverges. If $x$ is any number with $|x| > |d|$, then $\sum c_n x^n$ cannot converge, because by part 1 the convergence of $\sum c_n x^n$ would imply the convergence of $\sum c_n d^n$. Therefore $\sum c_n x^n$ diverges whenever $|x| > |d|$.

^pf-76-1

*Uses:* [[§70 Series#^thm-70-4|§70.4]], [[§69 Sequences#^def-69-3|Def. §69.3]], [[§70 Series#^thm-70-1|§70.1]], [[§72 The Comparison Tests#^thm-72-1|§72.1]], [[§73 Alternating Series and Absolute Convergence#^thm-73-3|§73.3]]

> [!remark]- Connections
> - Complex-variables version: [[§69★ Absolute and Uniform Convergence of Power Series#^thm-69-1|342 Thm. §69.1]] (convergence at $z_1$ gives absolute convergence in the disk $|z - z_0| < |z_1 - z_0|$).

> [!theorem] Lemma §76.2: Three Possibilities at Center 0
> For a power series $\sum c_n x^n$ there are only three possibilities:
>
> (i) The series converges only when $x = 0$.
>
> (ii) The series converges for all $x$.
>
> (iii) There is a positive number $R$ such that the series converges if $|x| < R$ and diverges if $|x| > R$.
>
> *Stewart: Appendix F (Section 11.8, Theorem)*

^lem-76-2

> [!proof]+ Proof
> Suppose that neither (i) nor (ii) is true. Then there are nonzero numbers $b$ and $d$ such that $\sum c_n x^n$ converges for $x = b$ and diverges for $x = d$. Therefore the set
>
> $$
> S = \Big\{ x \ \Big|\ \sum c_n x^n \text{ converges} \Big\}
> $$
>
> is not empty. By Lemma §76.1(2) the series diverges if $|x| > |d|$, so $|x| \le |d|$ for all $x \in S$: $|d|$ is an upper bound for $S$. By the Completeness Axiom ([[§69 Sequences#^def-69-7|Definition §69.7]]), $S$ has a least upper bound $R$. Also $R > 0$: by Lemma §76.1(1) the series converges at $|b|/2$, so $R \ge |b|/2 > 0$.
>
> **$|x| > R$.** Then $x \notin S$, so $\sum c_n x^n$ diverges. (Stewart states this directly; here is why: if $x \in S$, pick $y$ with $R < y < |x|$. By Lemma §76.1(1) the series converges at $y$, so $y \in S$ and $y > R$, contradicting that $R$ is an upper bound.)
>
> **$|x| < R$.** Then $|x|$ is not an upper bound for $S$, so there is $b \in S$ with $b > |x|$. Since $b \in S$, $\sum c_n b^n$ converges, so by Lemma §76.1(1) $\sum c_n x^n$ converges.

^pf-76-2

*Uses:* [[§76 Power Series#^lem-76-1|§76.1]], [[§69 Sequences#^def-69-7|Def. §69.7]]

> [!theorem] Theorem §76.3: Three Possibilities for a Power Series
> For a power series $\sum_{n=0}^{\infty} c_n (x - a)^n$, there are only three possibilities:
>
> (i) The series converges only when $x = a$.
>
> (ii) The series converges for all $x$.
>
> (iii) There is a positive number $R$ such that the series converges if $|x - a| < R$ and diverges if $|x - a| > R$.
>
> *Stewart: 11.8, Theorem 4; proof in Appendix F*

^thm-76-3

> [!proof]+ Proof
> Make the change of variable $u = x - a$. The power series becomes $\sum c_n u^n$, and Lemma §76.2 applies to it. In case (iii) we have convergence for $|u| < R$ and divergence for $|u| > R$, that is, convergence for $|x - a| < R$ and divergence for $|x - a| > R$. Cases (i) and (ii) translate in the same way ($u = 0$ means $x = a$).

^pf-76-3

*Uses:* [[§76 Power Series#^lem-76-2|§76.2]]

> [!remark]- Connections
> - Rigorous treatment: [[§23 Power Series#^thm-23-1|451 Thm. §23.1]] (the same trichotomy) and [[§23 Power Series#^thm-23-2|451 Thm. §23.2]], which also gives a formula for $R$: $R = 1/\limsup |c_n|^{1/n}$ (Cauchy–Hadamard), proved with the Root Test.
> - Complex-variables version: [[§69★ Absolute and Uniform Convergence of Power Series#^cor-69-2|342 Cor. §69.2]] (the interval of convergence becomes a disk, inside the circle of convergence).

> [!definition] Definition §76.3: Radius and Interval of Convergence
> The number $R$ in case (iii) of Theorem §76.3 is the **radius of convergence** of the power series. By convention, $R = 0$ in case (i) and $R = \infty$ in case (ii).
>
> The **interval of convergence** is the interval of all $x$ for which the series converges. In case (i) it is the single point $a$; in case (ii) it is $(-\infty, \infty)$. In case (iii), $|x - a| < R$ reads $a - R < x < a + R$; at an *endpoint* $x = a \pm R$ anything can happen (convergence at one, both or neither endpoint), so there are four possibilities:
>
> $$
> (a - R, a + R) \qquad (a - R, a + R] \qquad [a - R, a + R) \qquad [a - R, a + R]
> $$
>
> *Stewart: 11.8 (text)*

^def-76-3

![[m233-76-1.svg]]
*Case (iii) of Theorem §76.3. Inside the interval $|x - a| < R$ (blue) the series converges, and in fact converges absolutely (proof of Lemma §76.1). Outside it (red) the series diverges. At the two endpoints $a \pm R$ (orange) the theorem says nothing, and each endpoint must be tested separately.*

> [!remark] Remark: Method — Finding the Interval of Convergence
> 1. Apply the Ratio Test (sometimes the Root Test) to $\sum |a_n|$, where $a_n = c_n (x - a)^n$ is the full term. The limit has the form $K |x - a|$ (or $0$, or $\infty$ for $x \ne a$).
> 2. Solve $K |x - a| < 1$: $R = 1/K$ (with $R = \infty$ if the limit is $0$, and $R = 0$ if it is $\infty$).
> 3. The Ratio and Root Tests always fail at the endpoints $x = a \pm R$ (the limit is $1$ there). Substitute each endpoint into the series and test the resulting numerical series with another test: $p$-series, comparison, alternating series, or the Test for Divergence.
> 4. Assemble the interval, including exactly the endpoints where the series converges.
>
> | Series | Radius of convergence | Interval of convergence |
> |---|---|---|
> | $\sum_{n=0}^{\infty} x^n$ (geometric) | $R = 1$ | $(-1, 1)$ |
> | $\sum_{n=1}^{\infty} (x - 3)^n / n$ (Example §76.1) | $R = 1$ | $[2, 4)$ |
> | $\sum_{n=0}^{\infty} n!\,x^n$ (Example §76.2(a)) | $R = 0$ | $\{0\}$ |
> | $\sum_{n=0}^{\infty} x^n / (2n)!$ (Example §76.2(b)) | $R = \infty$ | $(-\infty, \infty)$ |
>
> *Stewart: 11.8 (text, Note and table)*

^rem-76-1

> [!example] Example §76.3: Convergent at One Endpoint Only
> Find the radius of convergence and interval of convergence of $\displaystyle\sum_{n=0}^{\infty} \frac{(-3)^n x^n}{\sqrt{n+1}}$.
>
> Let $a_n = (-3)^n x^n / \sqrt{n+1}$. Then
>
> $$
> \left| \frac{a_{n+1}}{a_n} \right| = \left| \frac{(-3)^{n+1} x^{n+1}}{\sqrt{n+2}} \cdot \frac{\sqrt{n+1}}{(-3)^n x^n} \right| = \left| -3x \sqrt{\frac{n+1}{n+2}} \right| = 3 \sqrt{\frac{1 + (1/n)}{1 + (2/n)}}\, |x| \to 3|x| \qquad \text{as } n \to \infty .
> $$
>
> By the Ratio Test the series converges if $3|x| < 1$ and diverges if $3|x| > 1$, that is, it converges if $|x| < \frac13$ and diverges if $|x| > \frac13$. The radius of convergence is $R = \frac13$.
>
> **Endpoints.** If $x = -\frac13$, then $(-3)^n (-\frac13)^n = 1$ and the series is
>
> $$
> \sum_{n=0}^{\infty} \frac{1}{\sqrt{n+1}} = \frac{1}{\sqrt1} + \frac{1}{\sqrt2} + \frac{1}{\sqrt3} + \cdots ,
> $$
>
> a $p$-series with $p = \frac12 < 1$, which diverges. If $x = \frac13$, then $(-3)^n (\frac13)^n = (-1)^n$ and the series is $\displaystyle\sum_{n=0}^{\infty} \frac{(-1)^n}{\sqrt{n+1}}$, which converges by the Alternating Series Test ($1/\sqrt{n+1}$ decreases to $0$).
>
> So the series converges when $-\frac13 < x \le \frac13$: the interval of convergence is $\left( -\frac13, \frac13 \right]$.
>
> *Stewart: Example 11.8.4*

^ex-76-3

> [!example] Example §76.4: A Series Centered at −2
> Find the radius of convergence and interval of convergence of $\displaystyle\sum_{n=0}^{\infty} \frac{n (x + 2)^n}{3^{n+1}}$.
>
> With $a_n = n(x + 2)^n / 3^{n+1}$,
>
> $$
> \left| \frac{a_{n+1}}{a_n} \right| = \left| \frac{(n+1)(x+2)^{n+1}}{3^{n+2}} \cdot \frac{3^{n+1}}{n (x+2)^n} \right| = \left( 1 + \frac1n \right) \frac{|x + 2|}{3} \to \frac{|x + 2|}{3} \qquad \text{as } n \to \infty .
> $$
>
> By the Ratio Test the series converges if $|x + 2|/3 < 1$ and diverges if $|x + 2|/3 > 1$: it converges if $|x + 2| < 3$ and diverges if $|x + 2| > 3$. The radius of convergence is $R = 3$, and the center is $a = -2$.
>
> **Endpoints.** $|x + 2| < 3$ means $-5 < x < 1$. At $x = -5$ the series is
>
> $$
> \sum_{n=0}^{\infty} \frac{n(-3)^n}{3^{n+1}} = \frac13 \sum_{n=0}^{\infty} (-1)^n n ,
> $$
>
> which diverges by the Test for Divergence ($(-1)^n n$ does not converge to $0$). At $x = 1$ the series is $\displaystyle\sum_{n=0}^{\infty} \frac{n\,3^n}{3^{n+1}} = \frac13 \sum_{n=0}^{\infty} n$, which also diverges by the Test for Divergence.
>
> So the series converges only when $-5 < x < 1$: the interval of convergence is $(-5, 1)$.
>
> *Stewart: Example 11.8.5*

^ex-76-4
