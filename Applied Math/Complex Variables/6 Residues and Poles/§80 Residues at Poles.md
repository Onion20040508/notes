---
type: section
subject: "[[Complex Variables]]"
chapter: 6
section: 80
bc: "80"
aliases: ["B&C 80"]
tags: [complex-variables, math342]
---
← [[§79 Examples (The Three Types of Isolated Singular Points)]] · ↑ [[· 6 Residues and Poles]] · [[§81 Examples (Residues at Poles)]] →

*Brown–Churchill, Section 80 · MAT 342 HW 11, Practice Final (Fall 2002).*

The basic way to recognize a pole and find its residue is to write out the Laurent series and look at the coefficient of $1/(z - z_0)$. This section replaces the series by a factorization: $z_0$ is a pole of order $m$ exactly when $f(z) = \phi(z)/(z - z_0)^m$ with $\phi$ analytic and nonzero at $z_0$, and then the residue is $\phi^{(m-1)}(z_0)/(m-1)!$, a single derivative of $\phi$. The proof is a translation between the Laurent series of $f$ and the Taylor series of $\phi$. In practice this is the most-used residue formula of the chapter.

## The Theorem

> [!theorem] Theorem §80.1: Poles and Their Residues
> Let $z_0$ be an isolated singular point of a function $f$. The following two statements are equivalent:
>
> **(a)** $z_0$ is a pole of order $m$ ($m = 1, 2, \ldots$) of $f$;
>
> **(b)** $f(z)$ can be written in the form
>
> $$
> f(z) = \frac{\phi(z)}{(z - z_0)^m} \qquad (m = 1, 2, \ldots),
> $$
>
> where $\phi(z)$ is analytic and nonzero at $z_0$.
>
> Moreover, if statements (a) and (b) are true, then
>
> $$
> \operatorname{Res}_{z=z_0} f(z) = \phi(z_0) \quad\text{when } m = 1 \qquad\text{and}\qquad \operatorname{Res}_{z=z_0} f(z) = \frac{\phi^{(m-1)}(z_0)}{(m - 1)!} \quad\text{when } m = 2, 3, \ldots .
> $$
>
> *B&C: Sec. 80, Theorem*

^thm-80-1

> [!proof]+ Proof
> **(a) implies (b).** Assume (a). Then $f(z)$ has a Laurent series representation
>
> $$
> f(z) = \sum_{n=0}^{\infty} a_n(z - z_0)^n + \frac{b_1}{z - z_0} + \frac{b_2}{(z - z_0)^2} + \cdots + \frac{b_{m-1}}{(z - z_0)^{m-1}} + \frac{b_m}{(z - z_0)^m} \qquad (b_m \ne 0),
> $$
>
> valid in a punctured disk $0 < |z - z_0| < R_2$ ([[§78 The Three Types of Isolated Singular Points#^def-78-4|Definition §78.4]]). Define $\phi$ by
>
> $$
> \phi(z) = \begin{cases} (z - z_0)^mf(z) & \text{when } z \ne z_0, \\ b_m & \text{when } z = z_0 . \end{cases}
> $$
>
> Multiplying the Laurent series by $(z - z_0)^m$ term by term shows that $\phi$ has the power series representation
>
> $$
> \phi(z) = b_m + b_{m-1}(z - z_0) + \cdots + b_2(z - z_0)^{m-2} + b_1(z - z_0)^{m-1} + \sum_{n=0}^{\infty} a_n(z - z_0)^{m+n}
> $$
>
> throughout the entire disk $|z - z_0| < R_2$. (For $z \ne z_0$ this is the Laurent series times $(z - z_0)^m$; the series $\sum a_n(z - z_0)^n$ converges in the whole disk, being a power series that converges in the punctured disk, so the right side converges there too; at $z = z_0$ both sides equal $b_m$.) Consequently $\phi$ is analytic in that disk ([[§71★ Integration and Differentiation of Power Series#^cor-71-2|Corollary §71.2]]), and in particular at $z_0$. Since $\phi(z_0) = b_m \ne 0$, and $f(z) = \phi(z)/(z - z_0)^m$ for $0 < |z - z_0| < R_2$, statement (b) follows.
>
> **(b) implies (a), and the residue.** Suppose now that we know only that $f$ has the form in (b). Since $\phi$ is analytic at $z_0$, it has a Taylor series representation ([[§63 Proof of Taylor's Theorem#^thm-63-1|Theorem §63.1]], Taylor's theorem)
>
> $$
> \phi(z) = \phi(z_0) + \frac{\phi'(z_0)}{1!}(z - z_0) + \frac{\phi''(z_0)}{2!}(z - z_0)^2 + \cdots + \frac{\phi^{(m-1)}(z_0)}{(m - 1)!}(z - z_0)^{m-1} + \sum_{n=m}^{\infty}\frac{\phi^{(n)}(z_0)}{n!}(z - z_0)^n
> $$
>
> in some neighborhood $|z - z_0| < \varepsilon$ of $z_0$. Dividing by $(z - z_0)^m$, the quotient in (b) becomes
>
> $$
> f(z) = \frac{\phi(z_0)}{(z - z_0)^m} + \frac{\phi'(z_0)/1!}{(z - z_0)^{m-1}} + \frac{\phi''(z_0)/2!}{(z - z_0)^{m-2}} + \cdots + \frac{\phi^{(m-1)}(z_0)/(m - 1)!}{z - z_0} + \sum_{n=m}^{\infty}\frac{\phi^{(n)}(z_0)}{n!}(z - z_0)^{n-m}
> $$
>
> when $0 < |z - z_0| < \varepsilon$. This is a series in powers of $z - z_0$ converging to $f$ in the punctured disk, so it is the Laurent series of $f$ there ([[§72★ Uniqueness of Series Representations#^thm-72-4|Theorem §72.4]]). Its principal part has the last term $\phi(z_0)/(z - z_0)^m$, and $\phi(z_0) \ne 0$: so $z_0$ is a pole of order $m$ of $f$. The coefficient of $1/(z - z_0)$ is $\phi^{(m-1)}(z_0)/(m - 1)!$, and this is the residue ([[§75 Residues#^def-75-1|Definition §75.1]]). The proof is complete.

^pf-80-1

*Uses:* [[§78 The Three Types of Isolated Singular Points#^def-78-4|Def. §78.4]], [[§75 Residues#^def-75-1|Def. §75.1]], [[§63 Proof of Taylor's Theorem#^thm-63-1|§63.1]] (Taylor's theorem), [[§71★ Integration and Differentiation of Power Series#^cor-71-2|§71.2]] (power series are analytic), [[§72★ Uniqueness of Series Representations#^thm-72-4|§72.4]] (uniqueness of Laurent series)

The two expressions for residues need not have been written separately: with the conventions $\phi^{(0)}(z_0) = \phi(z_0)$ and $0! = 1$, the second reduces to the first when $m = 1$. The representation in (b) is required to hold in some deleted neighborhood of $z_0$.

> [!remark]- Connections
> - In Fourier Series and PDEs, the coefficients of $\frac{A}{s - r} + \frac{B}{(s - r)^2}$ at a double root are $B = \lim_{s\to r}(s - r)^2U(s)$ and $A = \lim_{s\to r}(s - r)\big[U(s) - \frac{B}{(s - r)^2}\big]$, [[§54★ More Difficult Examples#^prop-54-2|341 Prop. §54.2]]. In the notation of Theorem §80.1 with $m = 2$ and $\phi(s) = (s - r)^2U(s)$, these are $B = \phi(r)$ and $A = \phi'(r)$, the residue. At a simple root the formula $\operatorname{Res} = \phi(z_0)$ is Heaviside's $q(r)/p'(r)$, [[§52★ Partial Fractions and Convolutions#^thm-52-2|341 Thm. §52.2]] (see [[§83 Zeros and Poles#^thm-83-2|Theorem §83.2]]).

> [!remark] Remark: Method — Computing the Residue at a Pole
> 1. **Factor out the singular factor.** Write $f(z) = \phi(z)/(z - z_0)^m$, with $m$ the power of $z - z_0$ that the formula of $f$ visibly divides by.
> 2. **Check $\phi$.** It must be analytic at $z_0$ (no other singular factor at $z_0$, no branch cut through $z_0$) and $\phi(z_0) \ne 0$. If $\phi(z_0) = 0$ the order is lower than $m$; if $\phi$ is not even defined at $z_0$ the factorization is wrong. In either case return to a Laurent series or to [[§83 Zeros and Poles#^thm-83-1|Theorem §83.1]] ([[§81 Examples (Residues at Poles)#^ex-81-3|Example §81.3]]).
> 3. **Read off the residue:** $\phi(z_0)$ for a simple pole, equivalently $\lim_{z\to z_0}(z - z_0)f(z)$; $\phi'(z_0)$ for $m = 2$; in general $\phi^{(m-1)}(z_0)/(m - 1)!$.
> 4. **If the principal part is wanted**, the Taylor coefficients $\phi^{(k)}(z_0)/k!$, $k = 0, \ldots, m - 1$, are its coefficients, read from $(z - z_0)^{-m}$ up to $(z - z_0)^{-1}$ ([[§80 Residues at Poles#^ex-80-2|Example §80.2]]).

^rem-80-1

## Examples

> [!example] Example §80.1: Dividing an Analytic Function by z − z₀
> Suppose that $f$ is analytic at $z_0$, and write $g(z) = f(z)/(z - z_0)$. Show that
>
> **(a)** if $f(z_0) \ne 0$, then $z_0$ is a simple pole of $g$, with residue $f(z_0)$;
>
> **(b)** if $f(z_0) = 0$, then $z_0$ is a removable singular point of $g$.
>
> Since $f$ is analytic at $z_0$, it has a Taylor series about $z_0$ valid in some neighborhood $|z - z_0| < \varepsilon$ ([[§63 Proof of Taylor's Theorem#^thm-63-1|Theorem §63.1]]); dividing by $z - z_0$,
>
> $$
> g(z) = \frac{f(z_0)}{z - z_0} + f'(z_0) + \frac{f''(z_0)}{2!}(z - z_0) + \frac{f'''(z_0)}{3!}(z - z_0)^2 + \cdots \qquad (0 < |z - z_0| < \varepsilon) .
> $$
>
> So $g$ is analytic in the punctured disk, and by uniqueness ([[§72★ Uniqueness of Series Representations#^thm-72-4|Theorem §72.4]]) this is its Laurent series there, with principal part $f(z_0)/(z - z_0)$.
>
> **(a)** If $f(z_0) \ne 0$, the principal part consists of the single nonzero term $f(z_0)/(z - z_0)$: a simple pole with residue $f(z_0)$. (This is also Theorem §80.1 with $m = 1$ and $\phi = f$.)
>
> **(b)** If $f(z_0) = 0$, the principal part is zero: a removable singular point; assigning $g(z_0) = f'(z_0)$ makes $g$ analytic at $z_0$.
>
> *B&C: Sec. 79, Exercise 3*

^ex-80-1

> [!example] Example §80.2: A Principal Part from the Taylor Series of φ
> Write the function
>
> $$
> f(z) = \frac{8a^3z^2}{(z^2 + a^2)^3} \qquad (a > 0)
> $$
>
> as
>
> $$
> f(z) = \frac{\phi(z)}{(z - ai)^3}, \qquad\text{where}\qquad \phi(z) = \frac{8a^3z^2}{(z + ai)^3} .
> $$
>
> Point out why $\phi$ has a Taylor series representation about $z = ai$, and use it to show that the principal part of $f$ at that point is
>
> $$
> \frac{\phi''(ai)/2}{z - ai} + \frac{\phi'(ai)}{(z - ai)^2} + \frac{\phi(ai)}{(z - ai)^3} = -\frac{i/2}{z - ai} - \frac{a/2}{(z - ai)^2} - \frac{a^2i}{(z - ai)^3} .
> $$
>
> **The Taylor series.** Since $z^2 + a^2 = (z - ai)(z + ai)$, indeed $f = \phi/(z - ai)^3$. The function $\phi$ is a quotient of polynomials whose denominator vanishes only at $-ai$, so it is analytic in the disk $|z - ai| < 2a$ and has a Taylor series there:
>
> $$
> \phi(z) = \phi(ai) + \phi'(ai)(z - ai) + \frac{\phi''(ai)}{2!}(z - ai)^2 + \sum_{n=3}^{\infty}\frac{\phi^{(n)}(ai)}{n!}(z - ai)^n .
> $$
>
> Dividing by $(z - ai)^3$, the terms with $n \le 2$ give the principal part displayed above (as in the proof of Theorem §80.1).
>
> **The values.** With $(2ai)^3 = -8a^3i$,
>
> $$
> \phi(ai) = \frac{8a^3(ai)^2}{(2ai)^3} = \frac{-8a^5}{-8a^3i} = \frac{a^2}{i} = -a^2i .
> $$
>
> By the quotient rule, $\phi'(z) = 8a^3\dfrac{2z(z + ai) - 3z^2}{(z + ai)^4} = \dfrac{8a^3z(2ai - z)}{(z + ai)^4}$, so
>
> $$
> \phi'(ai) = \frac{8a^3(ai)(ai)}{(2ai)^4} = \frac{-8a^5}{16a^4} = -\frac a2 .
> $$
>
> Differentiating once more, $\phi''(z) = 8a^3\dfrac{(2ai - 2z)(z + ai) - 4z(2ai - z)}{(z + ai)^5} = \dfrac{16a^3(z^2 - 4aiz - a^2)}{(z + ai)^5}$, so
>
> $$
> \phi''(ai) = \frac{16a^3(-a^2 + 4a^2 - a^2)}{(2ai)^5} = \frac{32a^5}{32a^5i} = -i, \qquad \frac{\phi''(ai)}{2} = -\frac i2 .
> $$
>
> This gives the stated principal part. Since $\phi(ai) = -a^2i \ne 0$, $ai$ is a pole of order $3$, with residue $-\frac{i}{2}$.
>
> *B&C: Sec. 79, Exercise 4; Source: 342 HW 11*

^ex-80-2

> [!example] Example §80.3: The Residue Formula from Cauchy's Integral Formula
> Let $z_0$ be an isolated singular point of $f$ and suppose that $f(z) = \phi(z)/(z - z_0)^m$, where $m$ is a positive integer and $\phi$ is analytic and nonzero at $z_0$. Use the extended Cauchy integral formula to show that $\operatorname{Res}_{z=z_0} f(z) = \phi^{(m-1)}(z_0)/(m - 1)!$.
>
> Since $\phi$ is analytic at $z_0$, there is a neighborhood $|z - z_0| < \varepsilon$ throughout which $\phi$ is analytic ([[§25 Analytic Functions#^def-25-1|Definition §25.1]]); then $f = \phi/(z - z_0)^m$ is analytic in $0 < |z - z_0| < \varepsilon$. Let $C$ be the positively oriented circle $|z - z_0| = \varepsilon/2$. It lies in that punctured disk and encloses $z_0$, so by [[§75 Residues#^thm-75-1|Theorem §75.1]]
>
> $$
> \operatorname{Res}_{z=z_0} f(z) = \frac{1}{2\pi i}\int_C \frac{\phi(z)\,dz}{(z - z_0)^m} .
> $$
>
> Now $\phi$ is analytic inside and on $C$, and the extended Cauchy integral formula ([[§56★ Verification of the Extension (An Extension of the Cauchy Integral Formula)#^thm-56-1|Theorem §56.1]]), $\int_C \frac{\phi(z)\,dz}{(z - z_0)^{n+1}} = \frac{2\pi i}{n!}\phi^{(n)}(z_0)$, applies with $n = m - 1$:
>
> $$
> \operatorname{Res}_{z=z_0} f(z) = \frac{1}{2\pi i}\cdot\frac{2\pi i}{(m - 1)!}\phi^{(m-1)}(z_0) = \frac{\phi^{(m-1)}(z_0)}{(m - 1)!} .
> $$
>
> This is a second proof of the residue formula of Theorem §80.1, without series. (It does not need $\phi(z_0) \ne 0$; that hypothesis only fixes the order of the pole.)
>
> *B&C: Sec. 81, Exercise 8; Source: 342 HW 11 (optional)*

^ex-80-3

> [!example] Example §80.4: The Residue at a Double Zero of the Denominator
> True or false: if $f$ and $g$ are analytic at $z_0$, $g(z_0) = g'(z_0) = 0$, and both $f(z_0)$ and $g''(z_0)$ are nonzero, then $\operatorname{Res}_{z=z_0}(f/g) = 0$.
>
> **False.** Take $f(z) = e^z$, $g(z) = z^2$, $z_0 = 0$: $g(0) = g'(0) = 0$, $g''(0) = 2 \ne 0$, $f(0) = 1 \ne 0$. Then $f/g = e^z/z^2$ has the form of Theorem §80.1 with $m = 2$ and $\phi(z) = e^z$, analytic and nonzero at $0$, so
>
> $$
> \operatorname{Res}_{z=0}\frac{e^z}{z^2} = \frac{\phi'(0)}{1!} = 1 \ne 0 .
> $$
>
> **In general.** By Taylor's theorem $g(z) = (z - z_0)^2h(z)$ with $h(z) = \frac{g''(z_0)}{2!} + \frac{g'''(z_0)}{3!}(z - z_0) + \cdots$ analytic and $h(z_0) = \frac12 g''(z_0) \ne 0$. Hence $f/g = \phi/(z - z_0)^2$ with $\phi = f/h$ analytic and nonzero at $z_0$: a pole of order $2$, with residue
>
> $$
> \phi'(z_0) = \frac{f'(z_0)h(z_0) - f(z_0)h'(z_0)}{h(z_0)^2} = \frac{2f'(z_0)}{g''(z_0)} - \frac{2f(z_0)g'''(z_0)}{3\,g''(z_0)^2} ,
> $$
>
> using $h'(z_0) = g'''(z_0)/6$. This vanishes only when $3f'(z_0)g''(z_0) = f(z_0)g'''(z_0)$; for $e^z/z^2$ it is $\frac{2\cdot1}{2} - 0 = 1$.
>
> *Source: 342 practice final (Fall 2002), Q8a*

^ex-80-4
