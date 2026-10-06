---
type: section
subject: "[[Complex Variables]]"
chapter: 5
section: 73
bc: "73"
aliases: ["B&C 73"]
tags: [complex-variables, math342, extension]
---
← [[§72★ Uniqueness of Series Representations]] · ↑ [[· 5 Series]] · [[§74 Isolated Singular Points]] →

*Brown–Churchill, Section 73 · MAT 342 Practice Final (Fall 2002).*
★ *Beyond MAT 342: the course skipped this section or left it optional; it is included from Brown–Churchill.*

Power series can be multiplied and divided like polynomials. If $\sum a_n(z - z_0)^n$ and $\sum b_n(z - z_0)^n$ converge in a disk, their product is the series obtained by multiplying term by term and collecting like powers, the **Cauchy product**, valid in the same disk. If the second sum has no zeros in the disk, their quotient is the series obtained by long division. The proofs are short because of what precedes: the sums are analytic ([[§71★ Integration and Differentiation of Power Series#^cor-71-2|Corollary §71.2]]), so the product and quotient have Taylor series ([[§63 Proof of Taylor's Theorem#^thm-63-1|Theorem §63.1]]), and those coefficients are computed from the given ones with Leibniz's rule and uniqueness ([[§72★ Uniqueness of Series Representations#^thm-72-1|Theorem §72.1]]). In practice only the first few terms are needed. They give the leading terms of Laurent series such as $1/\sin z$ and $1/\sinh z$, which the old finals use to find principal parts and residues ([[§74 Isolated Singular Points|Chapter 6]]).

## Products

> [!theorem] Lemma §73.1: Leibniz's Rule
> If $f(z)$ and $g(z)$ have derivatives up to order $n$ at a point, then there
>
> $$
> (fg)^{(n)} = \sum_{k=0}^{n}\binom nk f^{(k)}g^{(n-k)} \qquad (n = 1, 2, \ldots), \qquad (3)
> $$
>
> where $\binom nk = \dfrac{n!}{k!(n - k)!}$ $(k = 0, 1, 2, \ldots, n)$, $f^{(0)} = f$ and $0! = 1$.
>
> *B&C: Sec. 73, Exercise 7*

^lem-73-1

> [!proof]+ Proof
> By induction on $n$, for all pairs of functions at once. For $n = 1$ the rule is the product rule $(fg)' = fg' + f'g$ ([[§20 Rules for Differentiation#^thm-20-2|Theorem §20.2]]). Assume that it holds for $n = m$, where $m$ is any positive integer, and let $f$, $g$ have derivatives up to order $m + 1$. Applying the hypothesis to the pairs $(f, g')$ and $(f', g)$,
>
> $$
> (fg)^{(m+1)} = (fg' + f'g)^{(m)} = (fg')^{(m)} + (f'g)^{(m)} = \sum_{k=0}^{m}\binom mk f^{(k)}g^{(m+1-k)} + \sum_{k=0}^{m}\binom mk f^{(k+1)}g^{(m-k)} .
> $$
>
> Replace $k$ by $k - 1$ in the second sum, so that it runs over $k = 1, \ldots, m + 1$ with terms $\binom{m}{k-1}f^{(k)}g^{(m+1-k)}$, and separate the term $k = 0$ of the first sum and $k = m + 1$ of the second:
>
> $$
> (fg)^{(m+1)} = fg^{(m+1)} + \sum_{k=1}^{m}\Big[\binom mk + \binom{m}{k-1}\Big]f^{(k)}g^{(m+1-k)} + f^{(m+1)}g .
> $$
>
> With the identity $\binom mk + \binom{m}{k-1} = \binom{m+1}{k}$ (Pascal's rule, [[§12★ Counting Functions and Subsets#^prop-12-8|250 Prop. §12.8]], proved again in the proof of [[§3 Further Algebraic Properties#^thm-3-4|Theorem §3.4]]) and $\binom{m+1}{0} = \binom{m+1}{m+1} = 1$,
>
> $$
> (fg)^{(m+1)} = fg^{(m+1)} + \sum_{k=1}^{m}\binom{m+1}{k}f^{(k)}g^{(m+1-k)} + f^{(m+1)}g = \sum_{k=0}^{m+1}\binom{m+1}{k}f^{(k)}g^{(m+1-k)} ,
> $$
>
> which is the rule for $n = m + 1$.

^pf-73-1

*Uses:* [[§20 Rules for Differentiation#^thm-20-2|§20.2]] (product rule), [[§3 Further Algebraic Properties#^thm-3-4|§3.4]] (Pascal's identity, in its proof)

> [!definition] Definition §73.1: Cauchy Product
> The **Cauchy product** of the power series $\sum_{n=0}^{\infty}a_n(z - z_0)^n$ and $\sum_{n=0}^{\infty}b_n(z - z_0)^n$ is the power series $\sum_{n=0}^{\infty}c_n(z - z_0)^n$ with
>
> $$
> c_n = \sum_{k=0}^{n}a_kb_{n-k} = a_0b_n + a_1b_{n-1} + \cdots + a_nb_0 .
> $$
>
> It is the series obtained by formally multiplying the two series term by term and collecting the resulting terms in like powers of $z - z_0$.
>
> *B&C: Sec. 73 (text)*

^def-73-1

> [!theorem] Theorem §73.2: Multiplication of Power Series
> Suppose that each of the power series
>
> $$
> \sum_{n=0}^{\infty}a_n(z - z_0)^n \qquad\text{and}\qquad \sum_{n=0}^{\infty}b_n(z - z_0)^n \qquad (1)
> $$
>
> converges within some circle $|z - z_0| = R$, with sums $f(z)$ and $g(z)$. Then their Cauchy product converges to $f(z)g(z)$ there:
>
> $$
> f(z)g(z) = a_0b_0 + (a_0b_1 + a_1b_0)(z - z_0) + (a_0b_2 + a_1b_1 + a_2b_0)(z - z_0)^2 + \cdots + \Big(\sum_{k=0}^{n}a_kb_{n-k}\Big)(z - z_0)^n + \cdots \qquad (4)
> $$
>
> for $|z - z_0| < R$.
>
> *B&C: Sec. 73 (text), equation (4)*

^thm-73-2

> [!proof]+ Proof
> The sums $f$ and $g$ are analytic in the disk $|z - z_0| < R$ ([[§71★ Integration and Differentiation of Power Series#^cor-71-2|Corollary §71.2]]), so their product is analytic there and has a Taylor series expansion valid in the disk ([[§63 Proof of Taylor's Theorem#^thm-63-1|Theorem §63.1]]):
>
> $$
> f(z)g(z) = \sum_{n=0}^{\infty}c_n(z - z_0)^n \qquad (|z - z_0| < R), \qquad c_n = \frac{(fg)^{(n)}(z_0)}{n!} . \qquad (2)
> $$
>
> According to [[§72★ Uniqueness of Series Representations#^thm-72-1|Theorem §72.1]], the series (1) are themselves the Taylor series of $f$ and $g$: $a_k = f^{(k)}(z_0)/k!$ and $b_k = g^{(k)}(z_0)/k!$. For instance,
>
> $$
> c_0 = f(z_0)g(z_0) = a_0b_0, \qquad c_1 = \frac{f(z_0)g'(z_0) + f'(z_0)g(z_0)}{1!} = a_0b_1 + a_1b_0, \qquad c_2 = \frac{f(z_0)g''(z_0) + 2f'(z_0)g'(z_0) + f''(z_0)g(z_0)}{2!} = a_0b_2 + a_1b_1 + a_2b_0 .
> $$
>
> In general, by Leibniz's rule ([[§73★ Multiplication and Division of Power Series#^lem-73-1|Lemma §73.1]]),
>
> $$
> c_n = \frac{1}{n!}\sum_{k=0}^{n}\frac{n!}{k!(n - k)!}f^{(k)}(z_0)g^{(n-k)}(z_0) = \sum_{k=0}^{n}\frac{f^{(k)}(z_0)}{k!}\cdot\frac{g^{(n-k)}(z_0)}{(n - k)!} = \sum_{k=0}^{n}a_kb_{n-k} ,
> $$
>
> and (2) becomes (4).

^pf-73-2

*Uses:* [[§73★ Multiplication and Division of Power Series#^lem-73-1|§73.1]], [[§73★ Multiplication and Division of Power Series#^def-73-1|Def. §73.1]], [[§71★ Integration and Differentiation of Power Series#^cor-71-2|§71.2]], [[§63 Proof of Taylor's Theorem#^thm-63-1|§63.1]], [[§72★ Uniqueness of Series Representations#^thm-72-1|§72.1]]

> [!remark]- Connections
> - The calculus statement is [[§78 Taylor and Maclaurin Series#^thm-78-10|Calc Thm. §78.10]]. In real analysis the Cauchy product of two absolutely convergent series converges to the product of the sums (Mertens' theorem, not in the vault); here analyticity gives the result for power series in one line, with no rearrangement argument.

## Quotients

Continue to let $f(z)$ and $g(z)$ denote the sums of the series (1), and suppose that $g(z) \ne 0$ when $|z - z_0| < R$. Then the quotient $f(z)/g(z)$ is analytic throughout the disk, so it has a Taylor series there. Its coefficients could be found by differentiating $f/g$ repeatedly, but they are the same as those found by formally carrying out the division of the first series by the second. B&C states this without proof; here is the statement and the reason.

> [!theorem] Proposition §73.3: Division of Power Series
> Under the hypotheses of Theorem §73.2, suppose also that $g(z) \ne 0$ for $|z - z_0| < R$. Then
>
> $$
> \frac{f(z)}{g(z)} = \sum_{n=0}^{\infty}d_n(z - z_0)^n \qquad (|z - z_0| < R), \qquad (6)
> $$
>
> where the coefficients are determined recursively by
>
> $$
> d_0 = \frac{a_0}{b_0}, \qquad d_n = \frac{1}{b_0}\Big(a_n - \sum_{k=1}^{n}b_kd_{n-k}\Big) \qquad (n = 1, 2, \ldots) ,
> $$
>
> which are exactly the coefficients produced by formal long division of $\sum a_n(z - z_0)^n$ by $\sum b_n(z - z_0)^n$.
>
> *B&C: Sec. 73 (text), equation (6)*

^prop-73-3

> [!proof]+ Proof
> The quotient $q = f/g$ is analytic in $|z - z_0| < R$, since $f$ and $g$ are and $g$ has no zeros there. By Taylor's theorem $q(z) = \sum d_n(z - z_0)^n$ in the whole disk, which is (6). Now $f = g\cdot q$, and by Theorem §73.2 the Cauchy product of the series of $g$ and $q$ converges to $f$ in the disk. By uniqueness ([[§72★ Uniqueness of Series Representations#^cor-72-2|Corollary §72.2]]) its coefficients are those of $f$:
>
> $$
> a_n = \sum_{k=0}^{n}b_kd_{n-k} = b_0d_n + \sum_{k=1}^{n}b_kd_{n-k} \qquad (n = 0, 1, 2, \ldots) .
> $$
>
> Since $b_0 = g(z_0) \ne 0$, these equations can be solved for $d_0, d_1, d_2, \ldots$ in turn, and they give the stated recursion; in particular the $d_n$ are uniquely determined by the $a_n$ and $b_n$. Long division produces the same numbers: at step $n$ it chooses the next quotient coefficient $d_n$ so that the coefficient of $(z - z_0)^n$ in $f - g\cdot(d_0 + \cdots + d_n(z - z_0)^n)$ vanishes, which is the equation $a_n = \sum_{k=0}^{n}b_kd_{n-k}$.

^pf-73-3

*Uses:* [[§73★ Multiplication and Division of Power Series#^thm-73-2|§73.2]], [[§63 Proof of Taylor's Theorem#^thm-63-1|§63.1]], [[§71★ Integration and Differentiation of Power Series#^cor-71-2|§71.2]], [[§72★ Uniqueness of Series Representations#^cor-72-2|§72.2]]

## Examples

> [!example] Example §73.1: sinh z/(1 + z) by Multiplication
> The function $f(z) = \dfrac{\sinh z}{1 + z}$ has a singular point at $z = -1$, so its Maclaurin series is valid in the open disk $|z| < 1$. To find the first four nonzero terms, multiply
>
> $$
> (\sinh z)\Big(\frac{1}{1 + z}\Big) = \Big(z + \frac16z^3 + \frac{1}{120}z^5 + \cdots\Big)(1 - z + z^2 - z^3 + \cdots)
> $$
>
> term by term: each term of the first series times $1$, then times $-z$, then times $z^2$, and so on, with like powers assembled vertically:
>
> $$
> \begin{array}{rrrrrr}
> z & & +\tfrac16z^3 & & +\tfrac{1}{120}z^5 & + \cdots \\
>  & -z^2 & & -\tfrac16z^4 & & - \cdots \\
>  & & +z^3 & & +\tfrac16z^5 & + \cdots \\
>  & & & -z^4 & & - \cdots
> \end{array}
> $$
>
> Adding the columns,
>
> $$
> \frac{\sinh z}{1 + z} = z - z^2 + \frac76z^3 - \frac76z^4 + \cdots \qquad (|z| < 1) . \qquad (5)
> $$
>
> In the notation of Theorem §73.2, $c_3 = a_1b_2 + a_3b_0 = 1 + \frac16$ and $c_4 = a_1b_3 + a_3b_1 = -1 - \frac16$. (Sympy gives the same, with next term $\frac{47}{40}z^5$.)
>
> *B&C: Sec. 73, Example 1*

^ex-73-1

> [!example] Example §73.2: 1/sinh z by Division
> The zeros of the entire function $\sinh z$ are $z = n\pi i$ $(n = 0, \pm1, \pm2, \ldots)$ ([[§39★ Hyperbolic Functions#^thm-39-4|Theorem §39.4]]). So the reciprocal
>
> $$
> \frac{1}{\sinh z} = \frac{1}{z + \frac{z^3}{3!} + \frac{z^5}{5!} + \cdots} = \frac1z\left(\frac{1}{1 + \frac{z^2}{3!} + \frac{z^4}{5!} + \cdots}\right) \qquad (7)
> $$
>
> has a Laurent series representation in the punctured disk $0 < |z| < \pi$. The denominator in parentheses is the sum of a power series that converges everywhere and equals $(\sinh z)/z$ for $z \ne 0$ and $1$ at $0$; it has no zeros in $|z| < \pi$. By Proposition §73.3, the function in parentheses has a Maclaurin series valid in $|z| < \pi$, found by dividing the series in the denominator into $1$.
>
> **Long division.** The first quotient term is $1$; subtracting $1\cdot(1 + \frac{1}{3!}z^2 + \frac{1}{5!}z^4 + \cdots)$ from $1$ leaves $-\frac{1}{3!}z^2 - \frac{1}{5!}z^4 - \cdots$. The next quotient term is $-\frac{1}{3!}z^2$; subtracting $-\frac{1}{3!}z^2(1 + \frac{1}{3!}z^2 + \cdots) = -\frac{1}{3!}z^2 - \frac{1}{(3!)^2}z^4 - \cdots$ leaves $\big(\frac{1}{(3!)^2} - \frac{1}{5!}\big)z^4 + \cdots$, which is the next quotient term. So
>
> $$
> \frac{1}{1 + \frac{z^2}{3!} + \frac{z^4}{5!} + \cdots} = 1 - \frac{1}{3!}z^2 + \Big[\frac{1}{(3!)^2} - \frac{1}{5!}\Big]z^4 + \cdots = 1 - \frac16z^2 + \frac{7}{360}z^4 + \cdots \qquad (|z| < \pi), \qquad (8)
> $$
>
> since $\frac{1}{36} - \frac{1}{120} = \frac{10 - 3}{360} = \frac{7}{360}$.
>
> **Undetermined coefficients (the same computation).** Write the left side of (8) as $d_0 + d_1z + d_2z^2 + d_3z^3 + d_4z^4 + \cdots$ and multiply:
>
> $$
> 1 = \Big(1 + \frac{1}{3!}z^2 + \frac{1}{5!}z^4 + \cdots\Big)(d_0 + d_1z + d_2z^2 + d_3z^3 + d_4z^4 + \cdots) \qquad (|z| < \pi),
> $$
>
> that is,
>
> $$
> (d_0 - 1) + d_1z + \Big(d_2 + \frac{1}{3!}d_0\Big)z^2 + \Big(d_3 + \frac{1}{3!}d_1\Big)z^3 + \Big(d_4 + \frac{1}{3!}d_2 + \frac{1}{5!}d_0\Big)z^4 + \cdots = 0 .
> $$
>
> By [[§72★ Uniqueness of Series Representations#^cor-72-2|Corollary §72.2]] every coefficient is zero: $d_0 = 1$, $d_1 = 0$, $d_2 = -\frac16$, $d_3 = 0$, $d_4 = \frac{1}{36} - \frac{1}{120} = \frac{7}{360}$, which is (8).
>
> **The Laurent series.** In view of (7),
>
> $$
> \frac{1}{\sinh z} = \frac1z - \frac16z + \frac{7}{360}z^3 + \cdots \qquad (0 < |z| < \pi) , \qquad (9)
> $$
>
> and any number of further terms can be found by continuing the division (the next is $-\frac{31}{15120}z^5$).
>
> *B&C: Sec. 73, Example 2 and Exercise 6*

^ex-73-2

> [!example] Example §73.3: The Laurent Series of 1/sin z
> **Problem (Fall 2002).** Show that the Laurent series of $1/\sin z$ centered at $0$ has the form
>
> $$
> \frac{1}{\sin z} = \frac1z + \frac16z + \frac{7}{360}z^3 + \cdots \quad\text{(terms of order at least five)} .
> $$
>
> **Division.** The zeros of $\sin z$ are $z = n\pi$ ([[§38 Zeros and Singularities of Trigonometric Functions#^thm-38-1|Theorem §38.1]]), so $1/\sin z$ has a Laurent series in $0 < |z| < \pi$. As in Example §73.2,
>
> $$
> \csc z = \frac{1}{\sin z} = \frac1z\cdot\frac{1}{1 - \frac{z^2}{3!} + \frac{z^4}{5!} - \cdots} ,
> $$
>
> and the recursion of Proposition §73.3 with $b_0 = 1$, $b_2 = -\frac16$, $b_4 = \frac{1}{120}$ (odd $b_k = 0$) gives $d_0 = 1$, $d_2 = \frac16$, $d_4 = -\big(b_2d_2 + b_4d_0\big) = \frac{1}{36} - \frac{1}{120} = \frac{7}{360}$. Hence
>
> $$
> \csc z = \frac1z + \frac{1}{3!}z + \Big[\frac{1}{(3!)^2} - \frac{1}{5!}\Big]z^3 + \cdots = \frac1z + \frac16z + \frac{7}{360}z^3 + \cdots \qquad (0 < |z| < \pi) .
> $$
>
> **Check by multiplication:** $\big(\frac1z + \frac16z + \frac{7}{360}z^3\big)\big(z - \frac{z^3}{6} + \frac{z^5}{120}\big) = 1 + \big(\frac16 - \frac16\big)z^2 + \big(\frac{1}{120} - \frac{1}{36} + \frac{7}{360}\big)z^4 + \cdots = 1 + 0\cdot z^2 + 0\cdot z^4 + \cdots$, since $\frac{3 - 10 + 7}{360} = 0$.
>
> **One more term.** The next coefficient is $\frac{31}{15120}$ (the Fall 2009 final quotes the series to this term and then uses it as in [[§81 Examples (Residues at Poles)#^ex-81-5|Example §81.5]]). With $b_6 = -\frac{1}{5040}$, the recursion gives
>
> $$
> d_6 = -\big(b_2d_4 + b_4d_2 + b_6d_0\big) = \frac{7}{2160} - \frac{1}{720} + \frac{1}{5040} = \frac{49 - 21 + 3}{15120} = \frac{31}{15120} ,
> $$
>
> as sympy confirms.
>
> The rest of the Fall 2002 problem, the principal part and residues of $(1 - z)/(z^5\sin z)$, is [[§81 Examples (Residues at Poles)#^ex-81-5|Example §81.5]].
>
> *B&C: Sec. 73, Exercise 3; Source: 342 practice final (Fall 2002), Q1(a)*

^ex-73-3

> [!example] Example §73.4: An Integral from a Divided Series
> **Problem.** Show that $\dfrac{1}{z^2\sinh z} = \dfrac{1}{z^3} - \dfrac16\cdot\dfrac1z + \dfrac{7}{360}z + \cdots$ $(0 < |z| < \pi)$, and use it to show that
>
> $$
> \int_C\frac{dz}{z^2\sinh z} = -\frac{\pi i}{3}
> $$
>
> when $C$ is the positively oriented unit circle $|z| = 1$.
>
> **Series.** Multiply the Laurent series (9) of $1/\sinh z$ by $1/z^2$ term by term ([[§61 Convergence of Series#^prop-61-4|Proposition §61.4]]); by uniqueness ([[§72★ Uniqueness of Series Representations#^thm-72-4|Theorem §72.4]]) the result is the Laurent series of $1/(z^2\sinh z)$ in $0 < |z| < \pi$.
>
> **Integral.** The unit circle lies in that punctured disk and goes once around $0$, so by the method of [[§68 Examples (Proof of Laurent's Theorem)#^ex-68-4|Example §68.4]] the integral is $2\pi i$ times the coefficient of $1/z$:
>
> $$
> \int_C\frac{dz}{z^2\sinh z} = 2\pi i\Big(-\frac16\Big) = -\frac{\pi i}{3} \approx -1.0471976\,i ,
> $$
>
> which numerical quadrature on the unit circle confirms.
>
> *B&C: Sec. 73, Exercise 5*

^ex-73-4
