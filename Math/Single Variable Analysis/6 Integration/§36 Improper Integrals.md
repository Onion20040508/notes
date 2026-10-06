---
type: section
subject: "[[Single Variable Analysis]]"
section: 36
chapter: 6
tags: [real-analysis, math451]
---
← [[§35 Riemann–Stieltjes Integrals]] · ↑ [[· 6 Integration]]

> [!remark] Remark: Provenance
> This section was only mentioned in the final lecture; it is written out here from Ross §36, because it settles two accounts: the symbol $\int_1^\infty \tfrac{dx}{x^p}$, used on credit by the integral test of §15, and the completion of the Stieltjes story of §35, which ends at the distribution functions of probability theory.

^rem-36-1

The Riemann integral of §32 requires a *bounded* function on a *bounded* closed interval. Both restrictions are lifted the same way: integrate on smaller good intervals, then take a limit.

## Improper Riemann Integrals

> [!definition] Definition §36.1: Improper Integrals on Half-Open Intervals
> Let $[a, b)$ be an interval, $b$ finite or $+\infty$, and let $f$ be integrable on each $[a, d]$ with $a < d < b$. If
>
> $$
> \lim_{d \to b^-} \int_a^d f(x)\,dx
> $$
>
> exists — as a finite number, $+\infty$, or $-\infty$ — we define $\int_a^b f\,dx$ to be that limit. The mirror definition applies on $(a, b]$ ($a$ finite or $-\infty$), via $\lim_{c \to a^+} \int_c^b f\,dx$. When the value is finite the integral **converges**; when it is $\pm\infty$ it **diverges to** $\pm\infty$; and when $b = +\infty$ (resp. $a = -\infty$) or $f$ is not integrable on the closed interval, the object so defined is called an **improper integral**.

^def-36-1

> [!remark]- Connections
> - Used in PDEs: the Fourier integral, [[§14 Fourier Integral#^def-14-new1|341 Def. §14.1]], and the solution of the semi-infinite rod, [[§26 Semi-Infinite Rod#^thm-26-2|341 Thm. §26.2]], are improper integrals in this sense.
> - The Lebesgue integral is absolute ([[§15 The General Lebesgue Integral#^rem-15-1|551 Rem. §15.1]]), so a conditionally convergent improper integral such as that of $\sin x / x$ on $[1, \infty)$ is not a Lebesgue integral; for integrable $f$ the tails vanish by [[§16 The L¹ Space and Density Theorems#^thm-16-3|551 Thm. §16.3]].
> - Computational version: [[§51 Improper Integrals#^def-51-1|Calc Def. §51.1]], [[§51 Improper Integrals#^def-51-2|Calc Def. §51.2]] (with worked examples).
> - Used in ODEs: the improper integral over $[a, \infty)$ that defines the Laplace transform, [[§21 Definition of the Laplace Transform#^def-21-1|331 Def. §21.1]] (with worked examples).

> [!remark] Remark: The New Definition Extends the Old One
> If $b$ is finite and $f$ *is* integrable on $[a,b]$, no conflict arises [Ross Ex. 36.1]: the function $d \mapsto \int_a^d f\,dx$ is Lipschitz, hence continuous, on $[a,b]$ (the continuity clause of [[Fundamental Theorem of Calculus|FTC]] II, §34), so its limit as $d \to b^-$ is its value at $b$ — the ordinary integral. The limit definition extends the old one; it never overwrites it.

^rem-36-2

> [!definition] Definition §36.2: Doubly Improper Integrals
> If $f$ is defined on $(a, b)$ (each end finite or infinite) and integrable on every closed $[c, d] \subseteq (a,b)$, fix any $\alpha \in (a,b)$ and define
>
> $$
> \int_a^b f\,dx = \int_a^\alpha f\,dx + \int_\alpha^b f\,dx,
> $$
>
> provided both one-sided improper integrals exist and the sum is not of the form $+\infty + (-\infty)$. (Extended arithmetic: $\infty + L = \infty$ for $L \neq -\infty$, and $-\infty + L = -\infty$ for $L \neq \infty$.)

^def-36-2

> [!remark]- Connections
> - Computational version: [[§51 Improper Integrals#^def-51-1|Calc Def. §51.1]] (with worked examples).
> - Computational version: [[§85 Evaluation of Improper Integrals#^def-85-2|342 Def. §85.2]] (the Cauchy principal value, the symmetric limit used in residue calculations).

The definition does not depend on the choice of $\alpha$ [Ross Ex. 36.2]: replacing $\alpha$ by $\alpha' \in (a,b)$ changes the two summands by $\mp \int_\alpha^{\alpha'} f\,dx$ — a *finite* proper integral, since additivity over subintervals passes through the defining limits — and the two changes cancel in the sum, also in the extended arithmetic above.

> [!example] Example §36.1: The Reciprocal at Both Ends
> $f(x) = \tfrac1x$ on $(0, \infty)$. At the far end, for $d > 1$, $\int_1^d \tfrac{dx}{x} = \log d$ [by [[Fundamental Theorem of Calculus|FTC]] I, logarithm on the usual credit], so
>
> $$
> \int_1^\infty \frac{dx}{x} = \lim_{d\to\infty} \log d = +\infty;
> $$
>
> at the near end, $\int_c^1 \tfrac{dx}{x} = -\log c$ for $0 < c < 1$, so $\int_0^1 \tfrac{dx}{x} = \lim_{c\to0^+}(-\log c) = +\infty$. Hence, in the extended arithmetic, $\int_0^\infty \tfrac{dx}{x} = +\infty$: the reciprocal diverges at *both* ends.

^ex-36-1

> [!example] Example §36.2: The p-Integrals and the Loan of §15
> For fixed $p \neq 1$ and $d > 1$, [[Fundamental Theorem of Calculus|FTC]] I gives $\int_1^d x^{-p}\,dx = \tfrac{1}{1-p}\bigl( d^{1-p} - 1 \bigr)$, so
>
> $$
> \int_1^\infty x^{-p}\,dx =
> \begin{cases}
> \dfrac{1}{p-1}, & p > 1 \quad (d^{1-p} \to 0), \\[2mm]
> +\infty, & 0 < p < 1 \quad (d^{1-p} \to \infty),
> \end{cases}
> $$
>
> and $p = 1$ is the previous example: $+\infty$. *Convergence exactly when $p > 1$* — this dichotomy, fed through the integral test, is precisely the p-series theorem of §15; the symbol $\int_1^\infty$ used there is now a defined object, and that loan is repaid.

^ex-36-2

![[m451-36-2.svg]]
*The p-integrals on $[1, \infty)$: the three graphs look alike, but only for $p = 2$ (blue) is the area under the whole tail finite, $\int_1^\infty x^{-2}\,dx = \tfrac{1}{p-1} = 1$; for $p = 1$ (dashed) and $p = \tfrac12$ (red), $\int_1^d$ grows without bound as $d \to \infty$.*

> [!remark]- Connections
> - Computational version: [[§51 Improper Integrals#^thm-51-1|Calc Thm. §51.1]]; the p-series, [[§71 The Integral Test and Estimates of Sums#^thm-71-2|Calc Thm. §71.2]].

> [!example] Example §36.3: A Symbol with No Meaning
> $\int_0^d \sin x\,dx = 1 - \cos d$ [by [[Fundamental Theorem of Calculus|FTC]] I] oscillates between $0$ and $2$ forever: as $d \to \infty$ the limit does not exist, *not even in* $[-\infty, +\infty]$. So $\int_0^\infty \sin x\,dx$ is not a convergent integral, not a divergent one — the symbol simply has **no meaning**. (Divergence to $\pm\infty$ is a defined outcome; this is worse.) The same holds for $\int_{-\infty}^0 \sin x\,dx$ and $\int_{-\infty}^\infty \sin x\,dx$.
>
> Yet the *symmetric* limit certainly exists:
>
> $$
> \lim_{a \to \infty} \int_{-a}^{a} \sin x\,dx = \lim_{a\to\infty} 0 = 0,
> $$
>
> the odd integrand cancelling itself exactly. Such a value — the symmetric limit existing where the improper integral does not — is called the **Cauchy principal value**. The doubly-improper definition deliberately sends the two endpoints to infinity *independently*, precisely to forbid this kind of miraculous cancellation: a principal value is not an improper integral.

^ex-36-3

![[m451-36-3.svg]]
*The running integral $\int_0^d \sin x\,dx = 1 - \cos d$ (blue) swings between $0$ and $2$ forever, driven by the alternating lobes of $\sin x$ (gray): no limit as $d \to \infty$, not even $\pm\infty$ — the symbol $\int_0^\infty \sin x\,dx$ has no meaning.*

> [!remark]- Connections
> - Computational version: [[§85 Evaluation of Improper Integrals#^ex-85-1|342 Ex. §85.1]] (a principal value that exists although the improper integral does not).

## Improper Stieltjes Integrals and Distribution Functions

To integrate against a weight over the whole line, first extend the weight. If $F$ is a bounded increasing function on an interval $I$, extend it to all of $\mathbb{R}$ by the constant device

$$
F(t) = \inf\{ F(u) : u \in I \} \ \text{ for } t \leq \inf I, \qquad
F(t) = \sup\{ F(u) : u \in I \} \ \text{ for } t \geq \sup I,
$$

which keeps $F$ increasing. So assume henceforth that $F$ is increasing on all of $\mathbb{R}$, and write

$$
F(-\infty) = \lim_{t \to -\infty} F(t), \qquad F(\infty) = \lim_{t \to \infty} F(t)
$$

(monotone limits, existing in $[-\infty, +\infty]$).

> [!definition] Definition §36.3: F-Integrability on the Line
> Suppose $f$ is $F$-integrable (§35) on every interval $[a,b]$. Define, whenever the limits exist,
>
> $$
> \int_0^\infty f\,dF = \lim_{b\to\infty} \int_0^b f\,dF, \qquad
> \int_{-\infty}^0 f\,dF = \lim_{a\to-\infty} \int_a^0 f\,dF,
> $$
>
> and, when the sum is not of the form $\infty + (-\infty)$,
>
> $$
> \int_{-\infty}^\infty f\,dF = \int_{-\infty}^0 f\,dF + \int_0^\infty f\,dF.
> $$
>
> If this is finite, $f$ is **$F$-integrable on $\mathbb{R}$**. For $F(t) = t$ this recovers the improper Riemann integral.

^def-36-3

> [!theorem] Theorem §36.1: Dichotomy for Nonnegative Integrands
> If $f$ is $F$-integrable on every $[a,b]$ and $f(x) \geq 0$ for all $x$, then either $f$ is $F$-integrable on $\mathbb{R}$ or $\int_{-\infty}^\infty f\,dF = +\infty$. No third possibility — in particular, the symbol always has a meaning.

^thm-36-1

> [!proof]+ Proof
> Ross omits “the simple argument”; here it is. Let $h(b) = \int_0^b f\,dF$ for $b \geq 0$. For $0 \leq b < b'$, additivity gives $h(b') - h(b) = \int_b^{b'} f\,dF \geq 0$, since $f \geq 0$ and $F$ is increasing make every lower Darboux–Stieltjes sum nonnegative. So $h$ is increasing, and its limit as $b \to \infty$ exists in $[0, +\infty]$ and equals $S = \sup_b h(b)$: for any $M < S$, some $b_0$ has $h(b_0) > M$, and then $h(b) \geq h(b_0) > M$ for all $b \geq b_0$ — which is the definition of $h(b) \to S$, whether $S$ is finite or $+\infty$. The mirror argument at $-\infty$ gives $\int_{-\infty}^0 f\,dF \in [0, +\infty]$. Both pieces lie in $[0, +\infty]$, so their sum is never $\infty + (-\infty)$: it is finite ($f$ is $F$-integrable on $\mathbb{R}$) or $+\infty$.

^pf-36-1

*Uses:* [[§36 Improper Integrals#^def-36-3|Def. §36.3]]

> [!remark]- Connections
> - Computational version: the Comparison Theorem resting on this dichotomy, [[§51 Improper Integrals#^thm-51-2|Calc Thm. §51.2]] (with worked examples).
> - ODE version: the comparison test for piecewise continuous integrands, [[§21 Definition of the Laplace Transform#^thm-21-1|331 Thm. §21.1]], used for the existence of the Laplace transform.

> [!theorem] Theorem §36.2: Bounded Integrand against a Finite Total Weight
> Suppose $-\infty < F(-\infty) \leq F(\infty) < \infty$ (finite total weight), and let $f$ be bounded on $\mathbb{R}$ and $F$-integrable on every $[a,b]$. Then $f$ is $F$-integrable on $\mathbb{R}$.

^thm-36-2

> [!proof]+ Proof
> Let $|f| \leq B$. First, constants: on any $[a,b]$, every Darboux–Stieltjes sum of the constant $c$ equals $c\,(F(b) - F(a))$, so $\int_a^b c\,dF = c\,(F(b)-F(a))$, and letting the endpoints run off, $\int_{-\infty}^\infty c\,dF = c\,(F(\infty) - F(-\infty))$ — finite by hypothesis.
>
> Now shift: $0 \leq f + B \leq 2B$. By the dichotomy, $f + B$ is $F$-integrable on $\mathbb{R}$ unless its integral is $+\infty$; but monotonicity on each interval bounds every piece,
>
> $$
> \int_a^b (f + B)\,dF \leq \int_a^b 2B\,dF \leq 2B\,\bigl( F(\infty) - F(-\infty) \bigr) < \infty,
> $$
>
> so the $+\infty$ branch is excluded. Finally $f = (f + B) + (-B)$: linearity of the Stieltjes integral on each interval passes through the defining limits [Ross Ex. 36.10], so $f$ is $F$-integrable on $\mathbb{R}$.

^pf-36-2

*Uses:* [[§36 Improper Integrals#^thm-36-1|§36.1]], [[§36 Improper Integrals#^def-36-3|Def. §36.3]]

> [!remark]- Connections
> - Used in PDEs: the coefficient integrals of the Fourier integral converge absolutely, since $|f(x)\cos\lambda x|\le|f(x)|$, [[§14 Fourier Integral#^thm-14-1|341 Thm. §14.1]].

> [!remark] Remark: Distribution Functions
> An increasing $F: \mathbb{R} \to \mathbb{R}$ with $F(-\infty) = 0$ and $F(\infty) = 1$ is called a **distribution function**: in probability, $F(t)$ is the probability that a numerical outcome is $\leq t$. (The Riemann weight $F(t) = t$ is *not* one — infinite total weight.) The theorem above then says: every bounded, interval-wise $F$-integrable $f$ — every bounded continuous $f$, in particular — can be averaged against a distribution, total weight $1$. Frequently $F$ has a **density**: a function $g \geq 0$ with
>
> $$
> F(t) = \int_{-\infty}^t g(x)\,dx, \qquad \text{forcing} \qquad \int_{-\infty}^\infty g(x)\,dx = F(\infty) = 1;
> $$
>
> and if $g$ is continuous, then $F'(t) = g(t)$ for all $t$ — this is exactly the global form of [[Fundamental Theorem of Calculus|FTC]] II established in §34.

^rem-36-3

> [!remark]- Connections
> - Computational version: probability density functions, [[§56 Probability#^def-56-2|Calc Def. §56.2]] (with worked examples).

> [!example] Example §36.4: The Normal Distribution
> It turns out that
>
> $$
> \int_{-\infty}^\infty e^{-x^2}\,dx = \sqrt\pi
> $$
>
> [on credit: Ross Ex. 36.7; the standard proof squares the integral and passes to polar coordinates, outside one-variable theory]. Substituting $x = u/\sqrt2$ gives $\int_{-\infty}^\infty e^{-u^2/2}\,du = \sqrt{2\pi}$, so
>
> $$
> g(x) = \frac{1}{\sqrt{2\pi}}\, e^{-x^2/2}
> $$
>
> is a density — the *normal density*, the most important in probability — and its distribution function
>
> $$
> F(t) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^t e^{-x^2/2}\,dx
> $$
>
> is the *normal distribution*. It has no elementary closed form; but that is an old acquaintance: §26 computed the explicit power series of $\int_0^x e^{-t^2}\,dt$, which (after the same $\sqrt2$ substitution and the additive constant $\tfrac12 = F(0)$) is precisely the explicit handle on $F$. The section that began by extending the integral ends where the notes' power series began.

^ex-36-4

![[m451-36-1.svg]]
*The normal density $g$ (left; total area $1$) and its distribution function $F$ (right): the accumulated area climbs from $0$ to $1$, with $F(0) = \tfrac12$ by symmetry. By the remark above, $F' = g$ everywhere — the sigmoid's slope at $t$ is the bell's height at $t$.*

> [!remark]- Connections
> - The value √π taken on credit here is computed in 452 via polar coordinates: [[§15 Multivariable Integration#^ex-15-7|452 Ex. §15.7]].
> - Computational version: [[§56 Probability#^prop-56-3|Calc Prop. §56.3]].
