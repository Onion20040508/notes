---
type: section
subject: "[[Complex Variables]]"
chapter: 6
section: 82
bc: "82"
aliases: ["B&C 82"]
tags: [complex-variables, math342]
---
← [[§81 Examples (Residues at Poles)]] · ↑ [[· 6 Residues and Poles]] · [[§83 Zeros and Poles]] →

*Brown–Churchill, Section 82.*

Zeros and poles are closely related: a zero of order $m$ in a denominator produces a pole of order $m$ ([[§83 Zeros and Poles|§83]]). This section prepares that link with three facts about zeros of analytic functions, all read off from Taylor series. A zero of order $m$ can be factored out as $(z - z_0)^m$, leaving a function that is analytic and nonzero at $z_0$ ([[§82 Zeros of Analytic Functions#^thm-82-1|Theorem §82.1]]); zeros are isolated unless the function vanishes identically near the point ([[§82 Zeros of Analytic Functions#^thm-82-2|Theorem §82.2]]); and a function analytic in a disk that vanishes on a small domain or segment through the center vanishes in the whole disk ([[§82 Zeros of Analytic Functions#^thm-82-3|Theorem §82.3]]). The last fact is the local form of the uniqueness of analytic continuation used in [[§28★ Uniquely Determined Analytic Functions#^lem-28-1|Lemma §28.1]].

## Zeros of Order m

Suppose that $f$ is analytic at a point $z_0$. Then all of the derivatives $f^{(n)}(z)$ ($n = 1, 2, \ldots$) exist at $z_0$ ([[§57 Some Consequences of the Extension#^thm-57-1|Theorem §57.1]]).

> [!definition] Definition §82.1: Zero of Order m
> Let $f$ be analytic at $z_0$. If $f(z_0) = 0$ and there is a positive integer $m$ such that
>
> $$
> f(z_0) = f'(z_0) = f''(z_0) = \cdots = f^{(m-1)}(z_0) = 0 \qquad\text{and}\qquad f^{(m)}(z_0) \ne 0, \qquad (1)
> $$
>
> then $f$ is said to have a **zero of order $m$** at $z_0$. (When $m = 1$, condition (1) reads $f(z_0) = 0$, $f'(z_0) \ne 0$, with the convention $f^{(0)}(z_0) = f(z_0)$; a zero of order $1$ is a **simple zero**.)
>
> *B&C: Sec. 82, Equation (1)*

^def-82-1

The first theorem provides a useful alternative definition. Both parts of its proof use the fact ([[§63 Proof of Taylor's Theorem#^thm-63-1|Theorem §63.1]], Taylor's theorem) that a function analytic at $z_0$ has a Taylor series in powers of $z - z_0$ valid throughout some neighborhood $|z - z_0| < \varepsilon$ of $z_0$.

> [!theorem] Theorem §82.1: Factoring Out a Zero
> Let $f$ be a function that is analytic at a point $z_0$. The following two statements are equivalent:
>
> **(a)** $f$ has a zero of order $m$ at $z_0$;
>
> **(b)** there is a function $g$, which is analytic and nonzero at $z_0$, such that
>
> $$
> f(z) = (z - z_0)^mg(z) .
> $$
>
> *B&C: Sec. 82, Theorem 1*

^thm-82-1

> [!proof]+ Proof
> **(a) implies (b).** Assume that $f$ has a zero of order $m$ at $z_0$. The analyticity of $f$ at $z_0$ and conditions (1) tell us that in some neighborhood $|z - z_0| < \varepsilon$ there is a Taylor series representation whose first $m$ coefficients vanish:
>
> $$
> f(z) = \frac{f^{(m)}(z_0)}{m!}(z - z_0)^m + \frac{f^{(m+1)}(z_0)}{(m + 1)!}(z - z_0)^{m+1} + \frac{f^{(m+2)}(z_0)}{(m + 2)!}(z - z_0)^{m+2} + \cdots
> = (z - z_0)^m\Big[\frac{f^{(m)}(z_0)}{m!} + \frac{f^{(m+1)}(z_0)}{(m + 1)!}(z - z_0) + \frac{f^{(m+2)}(z_0)}{(m + 2)!}(z - z_0)^2 + \cdots\Big] .
> $$
>
> Consequently $f$ has the form in statement (b), where
>
> $$
> g(z) = \frac{f^{(m)}(z_0)}{m!} + \frac{f^{(m+1)}(z_0)}{(m + 1)!}(z - z_0) + \frac{f^{(m+2)}(z_0)}{(m + 2)!}(z - z_0)^2 + \cdots \qquad (|z - z_0| < \varepsilon) .
> $$
>
> (The bracketed series converges for $|z - z_0| < \varepsilon$: for $z \ne z_0$ it is the convergent Taylor series divided by $(z - z_0)^m$, and at $z_0$ trivially.) The convergence of this power series when $|z - z_0| < \varepsilon$ ensures that $g$ is analytic in that neighborhood, and in particular at $z_0$ ([[§71★ Integration and Differentiation of Power Series#^cor-71-2|Corollary §71.2]]). Moreover,
>
> $$
> g(z_0) = \frac{f^{(m)}(z_0)}{m!} \ne 0 .
> $$
>
> This completes the proof of the first part.
>
> **(b) implies (a).** Assume that $f(z) = (z - z_0)^mg(z)$ with $g$ analytic and nonzero at $z_0$. Since $g$ is analytic at $z_0$, it has a Taylor series representation
>
> $$
> g(z) = g(z_0) + \frac{g'(z_0)}{1!}(z - z_0) + \frac{g''(z_0)}{2!}(z - z_0)^2 + \cdots
> $$
>
> in some neighborhood $|z - z_0| < \varepsilon$. The expression for $f$ thus takes the form
>
> $$
> f(z) = g(z_0)(z - z_0)^m + \frac{g'(z_0)}{1!}(z - z_0)^{m+1} + \frac{g''(z_0)}{2!}(z - z_0)^{m+2} + \cdots
> $$
>
> when $|z - z_0| < \varepsilon$. Since this is a power series in $z - z_0$ that converges to $f$ in a neighborhood of $z_0$, it is the Taylor series of $f$ about $z_0$ ([[§72★ Uniqueness of Series Representations#^thm-72-1|Theorem §72.1]]). Comparing coefficients with $f^{(n)}(z_0)/n!$, conditions (1) hold; in particular
>
> $$
> f^{(m)}(z_0) = m!\,g(z_0) \ne 0 .
> $$
>
> Hence $z_0$ is a zero of order $m$ of $f$. The proof is complete.

^pf-82-1

*Uses:* [[§82 Zeros of Analytic Functions#^def-82-1|Def. §82.1]], [[§63 Proof of Taylor's Theorem#^thm-63-1|§63.1]] (Taylor's theorem), [[§71★ Integration and Differentiation of Power Series#^cor-71-2|§71.2]] (power series are analytic), [[§72★ Uniqueness of Series Representations#^thm-72-1|§72.1]] (uniqueness of Taylor series)

> [!remark] Remark: Method — Finding the Order of a Zero
> 1. **Derivatives.** Evaluate $f(z_0), f'(z_0), f''(z_0), \ldots$ until the first nonzero one; its index is the order (Definition §82.1).
> 2. **Factorization.** If $f(z) = (z - z_0)^mg(z)$ with $g$ analytic at $z_0$ and $g(z_0) \ne 0$, the order is $m$ (Theorem §82.1). Products add orders: if $f_1, f_2$ have zeros of orders $m_1, m_2$ at $z_0$, then $f_1f_2 = (z - z_0)^{m_1 + m_2}g_1g_2$ has a zero of order $m_1 + m_2$.
> 3. **Series.** Write the Taylor series of $f$ about $z_0$; the order is the lowest power of $z - z_0$ that occurs. For $1 - \cos z$ at $0$ the series starts with $z^2/2$ (order $2$); for $z - \sin z$ with $z^3/6$ (order $3$).

^rem-82-1

> [!example] Example §82.1: A Simple Zero of z³ − 1
> The polynomial $f(z) = z^3 - 1$ has a zero of order $m = 1$ at $z_0 = 1$, since
>
> $$
> f(z) = (z - 1)g(z), \qquad g(z) = z^2 + z + 1 ,
> $$
>
> where $f$ and $g$ are entire and $g(1) = 3 \ne 0$ (Theorem §82.1). The same conclusion follows from the observations that $f(1) = 0$ and $f'(1) = 3 \cdot 1^2 = 3 \ne 0$ (Definition §82.1).
>
> *B&C: Sec. 82, Example*

^ex-82-1

> [!example] Example §82.2: 1 − cos z Has a Zero of Order 2 at the Origin
> Use conditions (1) to show that $q(z) = 1 - \cos z$ has a zero of order $m = 2$ at $z_0 = 0$.
>
> $q$ is entire, and
>
> $$
> q(0) = 1 - \cos 0 = 0, \qquad q'(z) = \sin z,\ q'(0) = 0, \qquad q''(z) = \cos z,\ q''(0) = 1 \ne 0 .
> $$
>
> So conditions (1) hold with $m = 2$. Equivalently, $1 - \cos z = \frac{z^2}{2!} - \frac{z^4}{4!} + \cdots = z^2\big(\frac12 - \frac{z^2}{24} + \cdots\big)$, with the bracket analytic and equal to $\frac12$ at $0$. This fact is used in [[§83 Zeros and Poles#^ex-83-1|Example §83.1]] to show that $1/(1 - \cos z)$ has a pole of order $2$ at $0$.
>
> *B&C: Sec. 83, Exercise 2*

^ex-82-2

## Isolated Zeros

> [!definition] Definition §82.2: Isolated Zero
> A zero $z_0$ of a function $f$ is **isolated** if there is a [[§12★ Regions in the Complex Plane#^def-12-new1|deleted neighborhood]] $0 < |z - z_0| < \varepsilon$ of $z_0$ in which $f(z)$ is nonzero. A function **has only isolated zeros** if each of its zeros is isolated. (Compare the definition of an isolated singular point, [[§74 Isolated Singular Points#^def-74-1|Definition §74.1]].)
>
> *B&C: Sec. 82 (text)*

^def-82-2

The next theorem is a precise statement of the fact that an analytic function has only isolated zeros when it is not identically equal to zero.

> [!theorem] Theorem §82.2: Zeros Are Isolated
> Given a function $f$ and a point $z_0$, suppose that
>
> **(a)** $f$ is analytic at $z_0$;
>
> **(b)** $f(z_0) = 0$ but $f(z)$ is not identically equal to zero in any neighborhood of $z_0$.
>
> Then $f(z) \ne 0$ throughout some deleted neighborhood $0 < |z - z_0| < \varepsilon$ of $z_0$.
>
> *B&C: Sec. 82, Theorem 2*

^thm-82-2

> [!proof]+ Proof
> Let $f$ be as stated, and observe that not all of the derivatives of $f$ at $z_0$ are zero. If they were, all of the coefficients $f^{(n)}(z_0)/n!$ in the Taylor series for $f$ about $z_0$ would be zero; and since that series represents $f$ in some neighborhood of $z_0$ ([[§63 Proof of Taylor's Theorem#^thm-63-1|Theorem §63.1]]), $f(z)$ would be identically equal to zero in that neighborhood, contrary to (b). So, by the definition of zeros of order $m$, $f$ must have a zero of some finite order $m$ at $z_0$: $m$ is the first index with $f^{(m)}(z_0) \ne 0$, and $m \ge 1$ since $f(z_0) = 0$. According to Theorem §82.1, then,
>
> $$
> f(z) = (z - z_0)^mg(z) \qquad (2)
> $$
>
> in some neighborhood of $z_0$, where $g$ is analytic and nonzero at $z_0$.
>
> Now $g$ is continuous, in addition to being nonzero, at $z_0$, because it is analytic there. Hence there is some neighborhood $|z - z_0| < \varepsilon$ in which equation (2) holds and in which $g(z) \ne 0$ ([[§18 Continuity#^thm-18-3|Theorem §18.3]]). Since $(z - z_0)^m \ne 0$ when $z \ne z_0$, consequently $f(z) \ne 0$ in the *deleted* neighborhood $0 < |z - z_0| < \varepsilon$, and the proof is complete.

^pf-82-2

*Uses:* [[§82 Zeros of Analytic Functions#^def-82-1|Def. §82.1]], [[§82 Zeros of Analytic Functions#^thm-82-1|§82.1]], [[§63 Proof of Taylor's Theorem#^thm-63-1|§63.1]] (Taylor's theorem), [[§18 Continuity#^thm-18-3|§18.3]] (nonzero near a point where continuous and nonzero)

The final theorem concerns functions with zeros that are not all isolated. It was referred to in [[§28★ Uniquely Determined Analytic Functions|§28★]], where it drives the proof of [[§28★ Uniquely Determined Analytic Functions#^lem-28-1|Lemma §28.1]], and makes an interesting contrast to Theorem §82.2.

> [!theorem] Theorem §82.3: Vanishing on a Domain or Segment Through z₀
> Given a function $f$ and a point $z_0$, suppose that
>
> **(a)** $f$ is analytic throughout a neighborhood $N_0$ of $z_0$;
>
> **(b)** $f(z) = 0$ at each point $z$ of a domain $D$ or line segment $L$ containing $z_0$ (Fig. 96 in B&C).
>
> Then $f(z) \equiv 0$ in $N_0$; that is, $f(z)$ is identically equal to zero throughout $N_0$.
>
> *B&C: Sec. 82, Theorem 3*

^thm-82-3

> [!proof]+ Proof
> We begin with the observation that, under the stated conditions, $f(z) \equiv 0$ in some neighborhood $N$ of $z_0$. For otherwise $f$ would satisfy the hypotheses of Theorem §82.2 ($f$ is analytic at $z_0$, $f(z_0) = 0$ since $z_0$ lies in $D$ or on $L$, and $f$ is not identically zero in any neighborhood of $z_0$), and there would be a deleted neighborhood of $z_0$ throughout which $f(z) \ne 0$. That would be inconsistent with the condition that $f(z) = 0$ everywhere in a domain $D$ or on a line segment $L$ containing $z_0$: every deleted neighborhood of $z_0$ contains points of $D$ (which is open) and points of $L$ (a segment of positive length through $z_0$).
>
> Since $f(z) \equiv 0$ in the neighborhood $N$, all derivatives of $f$ vanish at $z_0$, and so all of the coefficients
>
> $$
> a_n = \frac{f^{(n)}(z_0)}{n!} \qquad (n = 0, 1, 2, \ldots)
> $$
>
> in the Taylor series for $f$ about $z_0$ are zero. Thus $f(z) \equiv 0$ in the neighborhood $N_0$, since the Taylor series also represents $f(z)$ in $N_0$ ([[§63 Proof of Taylor's Theorem#^thm-63-1|Theorem §63.1]]: $f$ is analytic throughout the disk $N_0$ centered at $z_0$). This completes the proof.

^pf-82-3

*Uses:* [[§82 Zeros of Analytic Functions#^thm-82-2|§82.2]], [[§63 Proof of Taylor's Theorem#^thm-63-1|§63.1]] (Taylor's theorem)

> [!remark]- Connections
> - Theorem §82.3 is local: it reaches only the disk $N_0$. The global statement, that two functions analytic in a domain $D$ which agree on a subdomain or segment agree throughout $D$ ([[§28★ Uniquely Determined Analytic Functions#^thm-28-2|Theorem §28.2]]), is obtained by chaining such disks along a polygonal path, and rests on $D$ being connected, [[§13 Connected Spaces#^def-13-new1|590 Def. §13.1]]: the set of points near which $f$ vanishes identically is open, and so is the set of points near which it does not (by Theorem §82.2), so one of them is empty.
> - Nothing like this holds for infinitely differentiable real functions: $e^{-1/x^2}$ (extended by $0$) vanishes with all its derivatives at $0$ without being identically zero near $0$, [[§31 Taylor's Theorem#^ex-31-3|451 Ex. §31.3]]; for an analytic function that would force $f \equiv 0$ near the point (proof of Theorem §82.2). Complex analyticity makes the Taylor series converge to the function, which is what the proofs of Theorems §82.2 and §82.3 use.

> [!example] Example §82.3: Finitely Many Zeros and Poles in a Closed Region
> Let $R$ be the region consisting of all points inside and on a simple closed contour $C$. Use the Bolzano–Weierstrass theorem, in the form *an infinite set of points lying in a closed bounded region $R$ has at least one [[§12★ Regions in the Complex Plane#^def-12-6|accumulation point]] in $R$*, to show:
>
> **(a)** if $f$ is analytic in $R$ except possibly for poles inside $C$, and all the zeros of $f$ in $R$ are interior to $C$ and of finite order, then those zeros are finite in number;
>
> **(b)** if $f$ is analytic in $R$ except for poles interior to $C$, then those poles are finite in number.
>
> **The Bolzano–Weierstrass theorem in this form.** Given an infinite subset $S$ of $R$, choose a sequence of distinct points of $S$. It is bounded, so it has a convergent subsequence ([[§13 Some Topological Concepts in Metric Spaces#^thm-13-3|451 Thm. §13.3]], in $\mathbb{R}^2$); the limit $z_0$ lies in $R$ since $R$ is closed, and every neighborhood of $z_0$ contains infinitely many points of $S$, so $z_0$ is an accumulation point of $S$.
>
> **(a)** Suppose the zeros were infinite in number, and let $z_0 \in R$ be an accumulation point of them. Every point of $R$ is either a pole or a point where $f$ is analytic.
> - *$z_0$ is not a pole.* Near a pole of order $m$, $f = \phi/(z - z_0)^m$ with $\phi$ analytic and nonzero at $z_0$ ([[§80 Residues at Poles#^thm-80-1|Theorem §80.1]]); by continuity $\phi \ne 0$ in a neighborhood, so $f \ne 0$ in a deleted neighborhood of the pole, and zeros cannot accumulate there.
> - *So $f$ is analytic at $z_0$*, hence continuous, and $f(z_0) = \lim f(z_k) = 0$ along a sequence of zeros $z_k \to z_0$: $z_0$ is itself a zero of $f$ in $R$, of finite order $m$ by hypothesis. By Theorem §82.1, $f = (z - z_0)^mg$ with $g(z_0) \ne 0$, and as in the proof of Theorem §82.2, $f \ne 0$ in a deleted neighborhood of $z_0$. This contradicts $z_0$ being an accumulation point of zeros.
>
> Hence the zeros are finite in number.
>
> **(b)** Suppose the poles were infinite in number, with an accumulation point $z_0 \in R$. If $f$ were analytic at $z_0$, it would be analytic in a whole neighborhood of $z_0$, which then could contain no pole. If $z_0$ were a pole, it would be an isolated singular point, with a deleted neighborhood containing no other singular point. Either way some neighborhood of $z_0$ contains no pole other than $z_0$, a contradiction. Hence the poles are finite in number.
>
> (These finiteness statements are what make the residue theorem ([[§76 Cauchy's Residue Theorem#^thm-76-1|Theorem §76.1]]) and the argument principle ([[§93 Argument Principle#^thm-93-4|Theorem §93.4]]) applicable to such functions.)
>
> *B&C: Sec. 83, Exercises 11 and 12*

^ex-82-3
