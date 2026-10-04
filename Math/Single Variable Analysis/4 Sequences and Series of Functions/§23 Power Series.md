---
subject: "[[Single Variable Analysis]]"
section: 23
chapter: 4
tags: [real-analysis, math451]
---
← [[§22 More on Metric Spaces꞉ Connectedness]] · ↑ [[· 4 Sequences and Series of Functions]] · [[§24 Uniform Convergence]] →

The simplest functions are the constants $a$ and the variable $x$. Starting from them we get all polynomials $a_0 + a_1 x + \cdots + a_n x^n$. Letting $n \to +\infty$, we should get **power series**

$$
a_0 + a_1 x + a_2 x^2 + \cdots = \sum_{n=0}^{\infty} a_n x^n.
$$

We know the value of a polynomial at every $x$. How about a power series? Take $a_n = 1$: what is $\sum_{n=0}^\infty x^n$ at $x = 2$, i.e. $\sum 2^n$? Of course $+\infty$ — in $\mathbb{R}$. (In a strange number system called the $2$-adic numbers, the answer is $-1$; we will not get into $p$-adic numbers.) So to make sense of a power series *as a function*, we must first determine its **domain**: for which $x$ does the series converge? Then we must study its properties as a function.

> [!definition] Definition §23.1: Convergence of a Power Series at a Point
> For a power series $\sum_{n=0}^\infty a_n x^n$, the partial sums are now *functions*
>
> $$
> s_n(x) = \sum_{k=0}^n a_k x^k.
> $$
>
> We say the series **converges at $x$** if $\lim_{n\to+\infty} s_n(x)$ exists — i.e. if the numerical series $\sum a_n x^n$ converges in the sense of §14.

^def-23-1

> [!remark]- Connections
> - Computational version: [[§76 Power Series#^def-76-2|Calc Def. §76.2]] (with worked examples).

> [!example] Example §23.1: Three domains of convergence
> **(1)** $\sum_{n=0}^\infty x^n$: converges at $x$ iff $|x| < 1$, with
>
> $$
> \sum_{n=0}^\infty x^n = \frac{1}{1-x},
> $$
>
> computed directly from $s_n(x) = \tfrac{1-x^{n+1}}{1-x}$ (§14). Set of convergence: $(-1,1)$.
>
> **(2)** $\sum_{n=1}^\infty \dfrac{x^n}{n^2}$: no simple formula for $s_n(x)$, but the ratio (or root) test gives convergence for $|x| < 1$ and divergence for $|x| > 1$. At $|x| = 1$ the series is dominated by $\sum \tfrac{1}{n^2}$, so it converges (absolutely) at both $x = 1$ and $x = -1$. Set of convergence: $[-1, 1]$.
>
> **(3)** $\sum_{n=1}^\infty \dfrac{x^n}{n}$: converges for $|x| < 1$, diverges for $|x| > 1$; at $x = -1$ it is the alternating harmonic series (converges, §15), at $x = 1$ the harmonic series (diverges). Set of convergence: $[-1, 1)$.

^ex-23-1

These examples display the general pattern:

> [!theorem] Theorem §23.1: Trichotomy for the Set of Convergence
> For any power series $\sum_{n=0}^\infty a_n x^n$, exactly one of the following holds:
>
> 1. it converges for all $x \in \mathbb{R}$;
>
> 2. it converges only for $x = 0$;
>
> 3. it converges for all $x$ in a bounded interval centered at $0$ — which can be closed, open, or half-open, as the examples show — and diverges outside that interval.

^thm-23-1

> [!remark]- Connections
> - Computational version: [[§76 Power Series#^thm-76-3|Calc Thm. §76.3]] (with worked examples).
> - Computational version: [[§69★ Absolute and Uniform Convergence of Power Series#^thm-69-1|342 Thm. §69.1]] and [[§69★ Absolute and Uniform Convergence of Power Series#^cor-69-2|342 Cor. §69.2]] (complex power series converge inside a circle of convergence and diverge outside it).

> [!example] Example §23.2: The extreme cases
> $\sum_{n=0}^\infty \dfrac{x^n}{n!}$ converges for *all* $x$: by the ratio test at fixed $x$, $\left|\tfrac{a_{n+1}x^{n+1}}{a_n x^n}\right| = \tfrac{|x|}{n+1} \to 0 < 1$ (this is $\sum \tfrac{|x|^n}{n!}$-type convergence from §9). $\sum_{n=0}^\infty n!\, x^n$ converges *only* for $x = 0$: for $x \neq 0$, $(n!)^{1/n} \to +\infty$, so $\limsup |n! x^n|^{1/n} = +\infty > 1$ and the root test gives divergence.

^ex-23-2

The precise version of the trichotomy:

> [!theorem] Theorem §23.2: Radius of Convergence
> For a power series $\sum_{n=0}^\infty a_n x^n$, let
>
> $$
> \beta = \limsup_{n\to+\infty} |a_n|^{1/n}, \qquad R = \frac{1}{\beta}
> $$
>
> (with the conventions $R = +\infty$ if $\beta = 0$, and $R = 0$ if $\beta = +\infty$). Then:
>
> 1. the series converges (absolutely) for all $|x| < R$;
>
> 2. it diverges for all $|x| > R$.
>
> If $R = 0$, it converges only at $x = 0$; if $R = +\infty$, for all $x$. At $|x| = R$ (when $0 < R < \infty$), extra work is needed case by case. $R$ is called the **radius of convergence**.

^thm-23-2

> [!proof]+ Proof
> Apply the root test (§14) to the series $\sum a_n x^n$ at fixed $x$:
>
> $$
> \limsup_{n\to+\infty} |a_n x^n|^{1/n} = |x| \limsup_{n\to+\infty} |a_n|^{1/n} = |x| \beta,
> $$
>
> using that a nonnegative constant factor passes through the $\limsup$ ($\limsup (c\, b_n) = c \limsup b_n$ for $c \geq 0$ — from the corresponding fact for tail-sups). The root test gives absolute convergence when $|x|\beta < 1$, i.e. $|x| < R$, and divergence when $|x|\beta > 1$, i.e. $|x| > R$; the conventions handle $\beta = 0, +\infty$.

^pf-23-2

![[m451-23-1.svg]]
*Top: the radius theorem — absolute convergence on $(-R, R)$, divergence for $|x| > R$, and no verdict at $\pm R$ (red). Below: the three series of Example §23.1, all with $R = 1$, whose sets of convergence differ only at the endpoints (filled: included, hollow: excluded).*

> [!remark]- Connections
> - Computational version: radius of convergence in [[§76 Power Series#^thm-76-3|Calc Thm. §76.3]] (with worked examples).
> - Computational version: [[§69★ Absolute and Uniform Convergence of Power Series#^cor-69-2|342 Cor. §69.2]] (convergence inside, divergence outside the circle of convergence of a complex power series).

> [!remark] Remark
> The nice thing: a simple pattern. The domain of convergence of a power series is always an interval, determined by the single number $R$ — only the endpoint behavior needs individual attention.

^rem-23-1

## Worked Examples on the Radius

> [!example] Example §23.3: Integer coefficients
> Assume all $a_n$ are integers and infinitely many are nonzero. Prove $R \leq 1$.
>
> The nonzero coefficients form a subsequence $a_{n_k} \neq 0$ with $|a_{n_k}| \geq 1$ (nonzero integers). *Claim: if the series converges at $x$, then $|x| < 1$.* Indeed, convergence forces $a_n x^n \to 0$ (§14), hence along the subsequence $a_{n_k} x^{n_k} \to 0$; but
>
> $$
> |a_{n_k} x^{n_k}| \geq |x|^{n_k},
> $$
>
> so $|x|^{n_k} \to 0$, which requires $|x| < 1$ (for $|x| \geq 1$, $|x|^{n_k} \geq 1$).
>
> Therefore $R \leq 1$: otherwise $R > 1$ would put $x = 1$ inside $(-R, R)$, forcing convergence at $x = 1$ — contradicting the claim. (More directly: convergence at $x = 1$ would give $a_n \to 0$, impossible for integers with infinitely many nonzero terms, since $|a_{n_k}| \geq 1$.)

^ex-23-3

> [!example] Example §23.4: Coefficients not tending to zero
> If $\limsup_{n\to+\infty} |a_n| > 0$, prove $R \leq 1$. By contradiction: if $R > 1$, the series converges at $x = 1$, so $a_n = a_n \cdot 1^n \to 0$, hence $|a_n| \to 0$ and $\limsup |a_n| = 0$ — contradiction.

^ex-23-4

> [!example] Example §23.5: Nonnegative coefficients and endpoints
> Suppose $\sum a_n x^n$ has finite radius $R$ and $a_n \geq 0$ for all $n$. Prove: if the series converges at $x = R$, then it also converges at $x = -R$ — so the interval of convergence is all of $[-R, R]$.
>
> *Proof.* Convergence at $x = R$ with $a_n \geq 0$ means $\sum a_n R^n$ converges — and this is exactly $\sum |a_n(-R)^n|$. So the series at $x = -R$ converges *absolutely*, hence converges.
>
> Consequently, an interval of convergence like $(-1, 1]$ requires coefficients of mixed sign. Example:
>
> $$
> \sum_{n=1}^\infty (-1)^n \frac{x^n}{n}: \qquad R = 1; \quad \text{at } x = 1: \ \textstyle\sum(-1)^n\frac1n \text{ converges}; \quad \text{at } x = -1: \ \textstyle\sum \frac1n \text{ diverges}.
> $$

^ex-23-5

## Power Series Centered at a Point

More generally, consider

$$
\sum_{n=0}^{\infty} a_n (x - x_0)^n.
$$

The interval of convergence is now centered at $x_0$: it is $(x_0 - R,\, x_0 + R)$ (with the endpoint questions as before), where $R = 1/\beta$, $\beta = \limsup |a_n|^{1/n}$, exactly as before. The proof is the same root-test computation:

$$
\limsup_{n\to\infty} |a_n (x-x_0)^n|^{1/n} = \beta\, |x - x_0|,
$$

compared with $1$.

> [!example] Example §23.6: Two centered examples
> **(1)** $\sum_{n=0}^\infty n^2 (x-1)^n$: here $\beta = \lim (n^2)^{1/n} = \left(n^{1/n}\right)^2 \to 1$, so $R = 1$ and the interval is $(0, 2)$. The endpoints $0, 2$ are *not* included: there the terms are $\pm n^2$, which do not tend to $0$, so $\sum n^2(\pm1)^n$ diverges.
>
> **(2)** $\sum_{n=1}^\infty \left( \dfrac{x-2}{n} \right)^n$: here $a_n = \tfrac{1}{n^n}$, $\beta = \lim \tfrac1n = 0$, $R = +\infty$ — the series converges for all $x \in \mathbb{R}$.

^ex-23-6

> [!remark] Remark: Why centered series? Taylor series
> The main source of centered power series is the **Taylor series** of a function $f$ at a point $x_0$:
>
> $$
> \sum_{n=0}^\infty \frac{f^{(n)}(x_0)}{n!} (x - x_0)^n,
> $$
>
> which for $x_0 = 0$ specializes to $\sum \tfrac{f^{(n)}(0)}{n!} x^n$ — e.g., for $f(x) = e^x$, the series $\sum_{n=0}^\infty \tfrac{x^n}{n!}$, whose radius we computed to be $+\infty$. (This is a preview: derivatives, and the sense in which $e^x$ *equals* its Taylor series, belong to Part II.)

^rem-23-2

> [!example] Example §23.7: Root test beats ratio test
> Let $a_n = \left( \dfrac{3 + 2(-1)^n}{4} \right)^n$ — that is, $a_n = \left(\tfrac54\right)^n$ for even $n$ and $\left(\tfrac14\right)^n$ for odd $n$. Determine the intervals of convergence of (1) $\sum a_n x^n$ and (2) $\sum a_n (x-2)^n$.
>
> Here $|a_n|^{1/n} = \tfrac{3+2(-1)^n}{4}$ oscillates between $\tfrac54$ and $\tfrac14$, so
>
> $$
> \beta = \limsup_{n\to\infty} |a_n|^{1/n} = \frac54, \qquad R = \frac45.
> $$
>
> (The *ratio* test is useless here: consecutive ratios swing between roughly $\left(\tfrac14\right)^{n+1}/\left(\tfrac54\right)^n \to 0$ and $\left(\tfrac54\right)^{n+1}/\left(\tfrac14\right)^n \to \infty$, so $\liminf < 1 < \limsup$ — no information. This example shows the difference in power between the two tests.)
>
> So (1) has interval $\left(-\tfrac45, \tfrac45\right)$ and (2) has $\left(2 - \tfrac45,\ 2 + \tfrac45\right)$, endpoints excluded in both cases: at the endpoints, $|a_n(x - x_0)^n| = |a_n| \left(\tfrac45\right)^n$ equals $1$ along the even indices, so the terms do not tend to $0$.

^ex-23-7

> [!remark] Remark: Mind the absolute values (HW)
> The coefficients above were positive; with *signed* coefficients the radius formula must read $\limsup |a_n|^{1/n}$, absolute values included. Take $a_n = \left( \tfrac{1 + 2(-1)^n}{5} \right)^n$, which is $\left(\tfrac35\right)^n$ for even $n$ but $\left(-\tfrac15\right)^n$ — *negative* — for odd $n$. The signed root sequence $a_n^{1/n} = \tfrac{1+2(-1)^n}{5}$ oscillates between $\tfrac35$ and $-\tfrac15$, whereas the sequence the formula wants, $|a_n|^{1/n}$, oscillates between $\tfrac35$ and $\tfrac15$: here the two limsups happen to agree ($\tfrac35$, so $R = \tfrac53$), but the signed liminf $-\tfrac15$ is meaningless for convergence questions — only the moduli $|a_n(x-x_0)^n|$ enter the comparison with a geometric series in the radius theorem's proof.

^rem-23-3

> [!remark] Remark: Gap series (HW)
> A second situation where the coefficient-ratio recipe breaks: series with *gaps*, like
>
> $$
> \sum_{n=0}^\infty 2^{-n} x^{3n} \qquad \text{or} \qquad \sum_{n=1}^\infty \frac{3^n}{\sqrt n}\, x^{2n+1}.
> $$
>
> As power series $\sum a_m x^m$, most coefficients are *zero* ($a_m = 0$ unless $3 \mid m$, resp. $m$ odd), so consecutive ratios $a_{m+1}/a_m$ are undefined or useless. Two correct routes. **(1) Test the whole terms:** fix $x$ and apply the ratio test to the numerical series — for the second series,
>
> $$
> \left| \frac{3^{n+1} x^{2n+3} / \sqrt{n+1}}{3^{n} x^{2n+1} / \sqrt{n}} \right| = 3|x|^2 \sqrt{\tfrac{n}{n+1}} \longrightarrow 3|x|^2,
> $$
>
> giving convergence for $3|x|^2 < 1$, divergence for $3|x|^2 > 1$: so $R = \tfrac{1}{\sqrt3}$ (equivalently, substitute $y = x^2$). **(2) The root formula survives:** $\limsup |a_m|^{1/m}$ ignores the zero terms — for the first series, $|a_m|^{1/m} = (2^{-n})^{1/3n} = 2^{-1/3}$ along $m = 3n$ and $0$ elsewhere, so $\beta = 2^{-1/3}$ and $R = 2^{1/3}$. Both intervals turn out open, for different reasons: for the first series the endpoint terms have modulus $|2^{-n} x^{3n}| = 1$ at $x = \pm 2^{1/3}$ (no decay at all); for the second, since $x^{2n+1}$ carries the sign of $x$ uniformly, at $x = \pm\tfrac{1}{\sqrt3}$ every term equals $\pm\tfrac{1}{\sqrt3\,\sqrt n}$ — a single-signed multiple of the divergent p-series with $p = \tfrac12$, so no alternation comes to the rescue. The limsup formula's indifference to gaps is one more point for the root test.

^rem-23-4

## Do Limits Preserve Good Properties? A Gallery of Failures

A power series defines a function $f(x) = \sum a_n x^n$ on its interval of convergence — the limit of the polynomial partial sums $s_n(x)$, each certainly continuous. **Question: are limits of sequences of continuous functions continuous?** At the beginning of calculus, people did not ask such questions — they assumed yes automatically. The general answer is **no**, and the counterexamples below motivate the next section.

> [!example] Example §23.8: Continuity lost in the limit
> Let $f_n(x) = x^n$ on $[0,1]$. For every $x \in [0,1]$, $f_n(x)$ converges: for $x \in [0,1)$, $|x| < 1$ gives $x^n \to 0$; and $f_n(1) = 1$. So the limit function is
>
> $$
> f(x) = 0 \ (0 \leq x < 1), \qquad f(1) = 1
> $$
>
> — *not* continuous, though every $f_n$ is.

^ex-23-8

![[m451-23-2.svg]]
*$f_n(x) = x^n$ for $n = 1, 2, 4, 8, 16, 32$ (blue, darker as $n$ grows): each is continuous and passes through $(1,1)$, but for every fixed $x < 1$ the values sink to $0$. The pointwise limit (red) is $0$ on $[0,1)$ with an isolated value $f(1) = 1$ — a jump that none of the $f_n$ has.*

> [!example] Example §23.9: Powers of sine
> $f_n(x) = (\sin x)^n$, $x \in \mathbb{R}$: find all $x$ where $\lim_n f_n(x)$ exists. If $x \neq k\pi + \tfrac\pi2$ ($k \in \mathbb{Z}$), then $|\sin x| < 1$ and $f_n(x) \to 0$. If $\sin x = 1$ (i.e. $x = 2k\pi + \tfrac\pi2$), $f_n(x) \to 1$. If $\sin x = -1$ (i.e. $x = (2k+1)\pi + \tfrac\pi2$), $f_n(x) = (-1)^n$ diverges. So the limit function has domain $\mathbb{R} \setminus \{(2k+1)\pi + \tfrac\pi2\}$, equals $0$ except at the points $2k\pi + \tfrac\pi2$ where it equals $1$ — and is not continuous.

^ex-23-9

> [!example] Example §23.10: Derivatives escape the limit
> Since a limit of continuous functions can fail to be continuous, it certainly can fail to be differentiable. Subtler question: suppose $f_n \to f$ pointwise, all $f_n$ differentiable, *and* $f$ differentiable — must $f_n' \to f'$? **Still no.** The idea: even if $f_n$ converges, its rate of change can be wild. Let
>
> $$
> f_n(x) = \frac1n \sin nx: \qquad f_n(x) \to 0 \text{ for all } x, \quad \text{so } f \equiv 0, \ f' \equiv 0.
> $$
>
> But $f_n'(x) = \cos nx$, whose graph oscillates faster and faster as $n$ grows; e.g. at $x = \pi$, $f_n'(\pi) = (-1)^n$ diverges — certainly not converging to $f'(\pi) = 0$. (One can show $\cos nx$ converges only at the points $x = 2k\pi$.)

^ex-23-10

> [!example] Example §23.11: Integrals escape the limit
> Suppose $f_n(x) \to f(x)$ for all $x \in [a,b]$. Does $\int_a^b f_n \to \int_a^b f$? **No.** Let
>
> $$
> f_n(x) = (n+1)x^n \ \ (0 \leq x < 1), \qquad f_n(1) = 0.
> $$
>
> Then $f(x) = 0$ for all $x \in [0,1]$ (for $x < 1$, $(n+1)x^n \to 0$ by the growth scale of §9). But
>
> $$
> \int_0^1 f_n(x)\,dx = x^{n+1}\Big|_0^1 = 1 \not\longrightarrow 0 = \int_0^1 f(x)\,dx.
> $$
>
> The mass of the integral escapes to the endpoint. (Integrals here are used in the familiar calculus sense, on credit as usual.)

^ex-23-11

All these examples show: things are subtle and tricky, and we should be careful. The good news: for the partial sums of power series, most of the difficulties disappear — but to see why, we need a stronger notion of convergence.
