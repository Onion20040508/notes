---
type: section
subject: "[[Fourier Series and PDEs]]"
chapter: 1
section: 12
powers: "1.7"
aliases: ["Powers 1.7"]
tags: [fourier-series-and-pdes, math341, extension]
---
← [[§11★ Mean Error and Convergence in Mean]] · ↑ [[· 1 Fourier Series and Integrals]] · [[§13★ Numerical Determination of Fourier Coefficients]] →

*Powers, Section 1.7.*
★ *Beyond MAT 341: the course did not cover this section; it is included from Powers.*

This section proves the Fourier convergence theorem that [[§8 Convergence of Fourier Series#^thm-8-1|Theorem §8.1]] states without proof: the Fourier series of a sectionally smooth periodic function converges at every point, to the average of the one-sided limits. The partial sum $S_N(x)$ is rewritten as an integral of $f$ against the Dirichlet kernel, the difference $S_N(x) - f(x)$ then turns out to be a Fourier coefficient of an auxiliary function, and the fact that Fourier coefficients tend to zero (the Riemann–Lebesgue lemma) finishes the proof. The one delicate point is that the auxiliary function has no bad discontinuity at $y = 0$, and this is exactly where sectional smoothness is used. No other subject in the vault proves pointwise convergence of Fourier series, so the proof is written out completely here, including the jump case that Powers leaves as an exercise; every later "$f$ equals its Fourier series" in the heat, wave and potential problems rests on it.

## Three Lemmas

Throughout, the period is $2\pi$; any other period follows by a change of variables ([[§12★ Proof of Convergence#^cor-12-5|Corollary §12.5]]). The finite cosine sum that appears in every step gets a name.

> [!definition] Definition §12.1: The Dirichlet Kernel
> For $N = 1, 2, \dots$ the **Dirichlet kernel** is the trigonometric polynomial
>
> $$
> D_N(y) = \frac12 + \sum_{n=1}^{N} \cos(ny) .
> $$
>
> It is continuous, even and periodic with period $2\pi$, and $D_N(0) = N + \frac12$.
>
> *Powers: 1.7, Lemmas 1 and 2 (Powers does not name the kernel)*

^def-12-1

> [!theorem] Lemma §12.1: The Kernel Has Integral One
> For all $N = 1, 2, \dots$,
>
> $$
> \frac1\pi\int_{-\pi}^{\pi}\Big(\frac12 + \sum_{n=1}^{N}\cos(ny)\Big)\,dy = 1 , \qquad\text{and}\qquad \frac1\pi\int_{0}^{\pi} D_N(y)\,dy = \frac1\pi\int_{-\pi}^{0} D_N(y)\,dy = \frac12 . \qquad (21)
> $$
>
> *Powers: 1.7, Lemma 1 and Equation (21)*

^lem-12-1

> [!proof]+ Proof
> (Powers' Exercise 1.7.2: integrate term by term.) The sum is finite, so the integral of $D_N$ is the sum of the integrals of its terms. Here $\int_{-\pi}^{\pi}\frac12\,dy = \pi$ and, for $n \ge 1$,
>
> $$
> \int_{-\pi}^{\pi}\cos(ny)\,dy = \Big[\frac{\sin(ny)}{n}\Big]_{-\pi}^{\pi} = 0 ,
> $$
>
> so $\frac1\pi\int_{-\pi}^{\pi} D_N = \frac1\pi \cdot \pi = 1$. Since $D_N$ is even, the substitution $y \mapsto -y$ shows $\int_{-\pi}^{0} D_N = \int_0^{\pi} D_N$, and the two halves add up to $\pi$; so each is $\frac\pi2$.

^pf-12-1

*Uses:* [[§12★ Proof of Convergence#^def-12-1|Def. §12.1]], [[§33 Properties of the Riemann Integral#^thm-33-2|451 Thm. §33.2]] (linearity), [[§33 Properties of the Riemann Integral#^thm-33-5|451 Thm. §33.5]] (additivity)

> [!theorem] Lemma §12.2: Closed Form of the Kernel
> For all $N = 1, 2, \dots$ and all $y$ that are not multiples of $2\pi$,
>
> $$
> D_N(y) = \frac12 + \sum_{n=1}^{N}\cos(ny) = \frac{\sin\big((N + \frac12)y\big)}{2\sin(\frac12 y)} .
> $$
>
> At the multiples of $2\pi$ the right side has the limit $N + \frac12 = D_N(0)$.
>
> *Powers: 1.7, Lemma 2*

^lem-12-2

> [!proof]+ Proof
> (Powers' Exercise 1.7.1: multiply through by $2\sin(\frac12 y)$.) The product formula $\sin\alpha\cos\beta = \frac12\big(\sin(\alpha + \beta) + \sin(\alpha - \beta)\big)$ with $\alpha = \frac12 y$, $\beta = ny$ gives
>
> $$
> 2\sin\big(\tfrac12 y\big)\cos(ny) = \sin\big((n + \tfrac12)y\big) - \sin\big((n - \tfrac12)y\big) .
> $$
>
> Hence the sum telescopes:
>
> $$
> 2\sin\big(\tfrac12 y\big)D_N(y) = \sin\big(\tfrac12 y\big) + \sum_{n=1}^{N}\Big[\sin\big((n + \tfrac12)y\big) - \sin\big((n - \tfrac12)y\big)\Big] = \sin\big(\tfrac12 y\big) + \sin\big((N + \tfrac12)y\big) - \sin\big(\tfrac12 y\big) = \sin\big((N + \tfrac12)y\big) .
> $$
>
> (For $N = 3$: $\sin\frac12 y + [\sin\frac32 y - \sin\frac12 y] + [\sin\frac52 y - \sin\frac32 y] + [\sin\frac72 y - \sin\frac52 y] = \sin\frac72 y$.) If $y$ is not a multiple of $2\pi$, then $\sin(\frac12 y) \ne 0$ and we may divide. At $y = 0$, $\sin(ay)/\sin(by) \to a/b$, so the quotient tends to $(N + \frac12)/(2 \cdot \frac12) = N + \frac12$; by periodicity the same holds at every multiple of $2\pi$.

^pf-12-2

*Uses:* [[§12★ Proof of Convergence#^def-12-1|Def. §12.1]]

![[m341-12-1.svg]]
*The Dirichlet kernel $D_N(y) = \sin((N + \frac12)y)/(2\sin\frac12 y)$ for $N = 2, 5, 10$. The central peak has height $N + \frac12$ and width about $2\pi/(N + \frac12)$, and the area under the whole curve is always $\pi$ (Lemma §12.1). Away from $y = 0$ the kernel does not become small: it oscillates ever faster between the envelopes $\pm 1/(2|\sin\frac12 y|)$. The convergence proof works because these fast oscillations cancel against any fixed decent function (Lemma §12.3), not because the kernel decays.*

> [!theorem] Lemma §12.3: Fourier Coefficients Tend to Zero
> If $\phi(y)$ is sectionally continuous, $-\pi < y < \pi$, then its Fourier coefficients tend to $0$ with $n$:
>
> $$
> \lim_{n\to\infty}\frac1\pi\int_{-\pi}^{\pi}\phi(y)\cos(ny)\,dy = 0, \qquad \lim_{n\to\infty}\frac1\pi\int_{-\pi}^{\pi}\phi(y)\sin(ny)\,dy = 0 .
> $$
>
> *Powers: 1.7, Lemma 3 (proved in 1.6)*

^lem-12-3

> [!proof]+ Proof
> Powers proved this in Section 1.6 ([[§11★ Mean Error and Convergence in Mean#^cor-11-5|Corollary §11.5]], with $a = \pi$) as a consequence of Bessel's inequality; here is the argument. Let $a_n$, $b_n$ be the two integrals in the statement and $a_0 = \frac{1}{2\pi}\int_{-\pi}^{\pi}\phi$; these are the Fourier coefficients of $\phi$ (period $2\pi$). Since $\phi$ is sectionally continuous, so is $\phi^2$, and $\int_{-\pi}^{\pi}\phi^2$ is finite. Bessel's inequality (with $a = \pi$) says
>
> $$
> 2a_0^2 + \sum_{n=1}^{N}\big(a_n^2 + b_n^2\big) \le \frac1\pi\int_{-\pi}^{\pi}\phi^2(y)\,dy \qquad\text{for every } N .
> $$
>
> So the series $\sum (a_n^2 + b_n^2)$ of nonnegative terms has bounded partial sums and converges. The terms of a convergent series tend to $0$; hence $a_n^2 \to 0$ and $b_n^2 \to 0$, that is, $a_n \to 0$ and $b_n \to 0$.

^pf-12-3

*Uses:* [[§11★ Mean Error and Convergence in Mean#^thm-11-3|§11.3]] (Bessel's inequality), [[§11★ Mean Error and Convergence in Mean#^cor-11-5|§11.5]]

> [!remark]- Connections
> - Bessel's inequality in any inner product space: [[§20 Orthonormal Sets and Bases#^thm-20-5|556 Thm. §20.5]]. The proof above is that inequality for the orthonormal functions $\frac{1}{\sqrt{2\pi}}, \frac{\cos ny}{\sqrt\pi}, \frac{\sin ny}{\sqrt\pi}$ in $L^2(-\pi, \pi)$, together with the fact that the terms of a convergent series tend to $0$.
> - Lemma §12.3 is the simplest case of the **Riemann–Lebesgue lemma**: the same conclusion holds for every absolutely integrable $\phi$, on an interval or on the whole line. The standard proof checks it for step functions by direct integration and passes to the limit using the density of step functions in $L^1$, [[§16 The L¹ Space and Density Theorems#^thm-16-6|551 Thm. §16.6]]. The vault has no separate proof of this general form; [[§12★ Proof of Convergence#^ex-12-3|Example §12.3]] carries out the limiting argument by hand in one case.

## The Convergence Theorem

The theorem is [[§8 Convergence of Fourier Series#^thm-8-1|Theorem §8.1]] (Powers 1.3), restated for period $2\pi$; [[§12★ Proof of Convergence#^cor-12-5|Corollary §12.5]] returns to period $2a$. Recall ([[§8 Convergence of Fourier Series#^def-8-4|Definition §8.4]]) that $f$ is **sectionally smooth** if $f$ is sectionally continuous, $f'$ exists except at finitely many points of each finite interval, and $f'$ is sectionally continuous. In particular the one-sided limits $f(x\pm)$ and $f'(x\pm) = \lim_{t \to x\pm} f'(t)$ exist at every $x$.

> [!theorem] Theorem §12.4: Fourier Convergence Theorem
> If $f(x)$ is sectionally smooth and periodic with period $2\pi$, then the Fourier series corresponding to $f$ converges at every $x$, and the sum of the series is
>
> $$
> a_0 + \sum_{n=1}^{\infty} a_n\cos(nx) + b_n\sin(nx) = \frac12\big(f(x+) + f(x-)\big) . \qquad (1)
> $$
>
> In particular the sum is $f(x)$ at every point where $f$ is continuous.
>
> *Powers: 1.7, Theorem (stated in 1.3)*

^thm-12-4

> [!remark] Remark: The Idea of the Proof
> The partial sum $S_N(x)$ is an average of the values $f(x + y)$ weighted by $\frac1\pi D_N(y)$, a weight of total mass $1$ (Lemma §12.1) with a tall peak at $y = 0$. So $S_N(x) - f(x)$ is the average of $f(x + y) - f(x)$ with the same weight. By Lemma §12.2 the weight is $\sin((N + \frac12)y)$ divided by $2\sin(\frac12 y)$, and the quotient
>
> $$
> \frac{f(x + y) - f(x)}{2\sin(\frac12 y)}
> $$
>
> is a fixed function of $y$, independent of $N$. Then $S_N(x) - f(x)$ is essentially a Fourier sine coefficient of that function, which tends to $0$ by Lemma §12.3, provided the function is sectionally continuous. Away from $y = 0$ it obviously is. At $y = 0$ numerator and denominator both vanish, and the quotient stays bounded exactly when $f$ has one-sided derivatives at $x$; this is where sectional smoothness enters.

^rem-12-1

> [!proof]- Proof
> Let the point $x$ be chosen; it remains fixed. Let $S_N$ be the partial sum of the Fourier series of $f$,
>
> $$
> S_N(x) = a_0 + \sum_{n=1}^{N} a_n\cos(nx) + b_n\sin(nx) , \qquad (2)
> $$
>
> where the Fourier coefficients are
>
> $$
> a_0 = \frac{1}{2\pi}\int_{-\pi}^{\pi} f(z)\,dz, \qquad a_n = \frac1\pi\int_{-\pi}^{\pi} f(z)\cos(nz)\,dz, \qquad b_n = \frac1\pi\int_{-\pi}^{\pi} f(z)\sin(nz)\,dz . \qquad (3)
> $$
>
> *(Powers prints the factor in front of $b_n$ in (3) as $\frac{1}{2\pi}$, p. 96; the correct factor, used throughout the proof, is $\frac1\pi$.)* The variable of integration is called $z$, which does not affect the values.
>
> **Part 1. Transformation of $S_N(x)$.** Replace the coefficients in (2) by the integrals (3). The sum is finite, so it can be taken inside one integral, and $\cos(nz)\cos(nx) + \sin(nz)\sin(nx) = \cos(n(z - x))$:
>
> $$
> \begin{aligned}
> S_N(x) &= \frac{1}{2\pi}\int_{-\pi}^{\pi} f(z)\,dz + \sum_{n=1}^{N}\Big[\frac1\pi\int_{-\pi}^{\pi} f(z)\cos(nz)\,dz\,\cos(nx) + \frac1\pi\int_{-\pi}^{\pi} f(z)\sin(nz)\,dz\,\sin(nx)\Big] \\
> &= \frac1\pi\int_{-\pi}^{\pi} f(z)\Big(\frac12 + \sum_{n=1}^{N}\big[\cos(nz)\cos(nx) + \sin(nz)\sin(nx)\big]\Big)\,dz
> = \frac1\pi\int_{-\pi}^{\pi} f(z)\Big(\frac12 + \sum_{n=1}^{N}\cos\big(n(z - x)\big)\Big)\,dz . \qquad (4)\text{–}(8)
> \end{aligned}
> $$
>
> Change the variable of integration from $z$ to $y = z - x$:
>
> $$
> S_N(x) = \frac1\pi\int_{-\pi - x}^{\pi - x} f(x + y)\,D_N(y)\,dy . \qquad (9)
> $$
>
> Both factors of the integrand $g(y) = f(x + y)D_N(y)$ are periodic in $y$ with period $2\pi$, and the integral of a $2\pi$-periodic function over any interval $[c, c + 2\pi]$ is the same (Powers' Exercise 1.1.5, [[§6 Periodic Functions and Fourier Series#^prop-6-2|Proposition §6.2]]). (Here is why: let $m = \pi + 2k\pi$ be the point of $[c, c + 2\pi]$ congruent to $\pi$; then $c - 2k\pi \in [-\pi, \pi]$, and shifting $\int_c^m g$ by $-2k\pi$ and $\int_m^{c + 2\pi} g$ by $-2k\pi - 2\pi$ turns them into $\int_{c - 2k\pi}^{\pi} g$ and $\int_{-\pi}^{c - 2k\pi} g$, which add up to $\int_{-\pi}^{\pi} g$.) Therefore
>
> $$
> S_N(x) = \frac1\pi\int_{-\pi}^{\pi} f(x + y)\Big(\frac12 + \sum_{n=1}^{N}\cos(ny)\Big)\,dy = \frac1\pi\int_{-\pi}^{\pi} f(x + y)\,D_N(y)\,dy . \qquad (10)
> $$
>
> **Part 2. Expression for $S_N(x) - f(x)$, when $f$ is continuous at $x$.** Here the sum should be $f(x)$, so we must show $S_N(x) - f(x) \to 0$. Since $x$ is fixed, $f(x)$ is a number, and by Lemma §12.1
>
> $$
> f(x) = f(x) \cdot \frac1\pi\int_{-\pi}^{\pi} D_N(y)\,dy = \frac1\pi\int_{-\pi}^{\pi} f(x)\,D_N(y)\,dy . \qquad (11)
> $$
>
> Subtracting (11) from (10),
>
> $$
> S_N(x) - f(x) = \frac1\pi\int_{-\pi}^{\pi}\big(f(x + y) - f(x)\big)D_N(y)\,dy . \qquad (12)
> $$
>
> **Part 3. The limit, when $f$ is continuous at $x$.** By Lemma §12.2 (the integrand at the single point $y = 0$ does not affect the integral),
>
> $$
> S_N(x) - f(x) = \frac1\pi\int_{-\pi}^{\pi}\big(f(x + y) - f(x)\big)\frac{\sin\big((N + \frac12)y\big)}{2\sin(\frac12 y)}\,dy . \qquad (13)
> $$
>
> The addition formula $\sin\big((N + \frac12)y\big) = \cos(Ny)\sin(\frac12 y) + \sin(Ny)\cos(\frac12 y)$ splits this into
>
> $$
> S_N(x) - f(x) = \frac1\pi\int_{-\pi}^{\pi}\big(f(x + y) - f(x)\big)\frac12\cos(Ny)\,dy + \frac1\pi\int_{-\pi}^{\pi}\big(f(x + y) - f(x)\big)\frac{\cos(\frac12 y)}{2\sin(\frac12 y)}\sin(Ny)\,dy . \qquad (14)
> $$
>
> *The first integral* is the Fourier cosine coefficient (with index $N$) of
>
> $$
> \psi(y) = \frac12\big(f(x + y) - f(x)\big) . \qquad (15)
> $$
>
> Since $f$ is sectionally continuous, so is its translate $\psi$, and the first integral tends to $0$ as $N \to \infty$ by Lemma §12.3.
>
> *The second integral* is the Fourier sine coefficient of
>
> $$
> \phi(y) = \frac{f(x + y) - f(x)}{2\sin(\frac12 y)}\cos\big(\tfrac12 y\big) . \qquad (16)
> $$
>
> We show that $\phi$ is sectionally continuous on $-\pi \le y \le \pi$. On $\delta \le |y| \le \pi$, for any $\delta > 0$, we have $|\sin(\frac12 y)| \ge \sin(\frac12\delta) > 0$, so $\phi$ is a sectionally continuous function times continuous functions there: bounded, with at most finitely many jumps. The only difficulty is the apparent division by $0$ at $y = 0$. Numerator and denominator of $\big(f(x + y) - f(x)\big)/\big(2\sin(\frac12 y)\big)$ both tend to $0$ as $y \to 0$, the numerator because $f$ is continuous at $x$. Choose $\delta > 0$ so small that $f$ is differentiable at every point of $(x - \delta, x)$ and $(x, x + \delta)$ (there are only finitely many exceptional points nearby); the derivative of the denominator, $\cos(\frac12 y)$, is nonzero there. By l'Hôpital's rule, applied to each one-sided limit,
>
> $$
> \lim_{y\to0+}\frac{f(x + y) - f(x)}{2\sin(\frac12 y)} = \lim_{y\to0+}\frac{f'(x + y)}{\cos(\frac12 y)} = f'(x+), \qquad
> \lim_{y\to0-}\frac{f(x + y) - f(x)}{2\sin(\frac12 y)} = f'(x-) . \qquad (17)\text{–}(19)
> $$
>
> Both limits exist because $f'$ is sectionally continuous. (Powers treats two cases: if $f$ is differentiable near $x$ with $f'$ continuous at $x$, the two limits are equal to $f'(x)$ and $\phi$ has a removable discontinuity at $y = 0$; if $f$ has a corner at $x$, they differ and $\phi$ has a jump. The computation is the same.) In either case $\phi$ is sectionally continuous, its Fourier sine coefficient tends to $0$ by Lemma §12.3, and with (14) $S_N(x) - f(x) \to 0$. The proof is complete for every $x$ where $f$ is continuous.
>
> **Part 4. $f$ is not continuous at $x$.** Now let $f$ have a jump at $x$. Return to Part 2 and express the proposed sum of the series with the halves of Lemma §12.1, equation (21):
>
> $$
> \frac12\big(f(x+) + f(x-)\big) = \frac1\pi\int_0^{\pi} f(x+)\,D_N(y)\,dy + \frac1\pi\int_{-\pi}^{0} f(x-)\,D_N(y)\,dy . \qquad (20)
> $$
>
> Splitting the interval of integration in (10) in half to match and subtracting (20),
>
> $$
> S_N(x) - \frac12\big(f(x+) + f(x-)\big) = \underbrace{\frac1\pi\int_0^{\pi}\big(f(x + y) - f(x+)\big)D_N(y)\,dy}_{I_N^+} + \underbrace{\frac1\pi\int_{-\pi}^{0}\big(f(x + y) - f(x-)\big)D_N(y)\,dy}_{I_N^-} . \qquad (22)
> $$
>
> (Powers leaves the rest as an exercise, "the technique is the same as in Part 3"; here it is.) For $I_N^+$, use Lemma §12.2 and the addition formula exactly as in (13)–(14):
>
> $$
> I_N^+ = \frac1\pi\int_0^{\pi}\frac12\big(f(x + y) - f(x+)\big)\cos(Ny)\,dy + \frac1\pi\int_0^{\pi}\frac{f(x + y) - f(x+)}{2\sin(\frac12 y)}\cos\big(\tfrac12 y\big)\sin(Ny)\,dy .
> $$
>
> Define, on $-\pi < y < \pi$,
>
> $$
> \psi_R(y) = \begin{cases} \frac12\big(f(x + y) - f(x+)\big), & 0 < y < \pi, \\ 0, & -\pi < y < 0, \end{cases}
> \qquad
> \phi_R(y) = \begin{cases} \dfrac{f(x + y) - f(x+)}{2\sin(\frac12 y)}\cos\big(\tfrac12 y\big), & 0 < y < \pi, \\ 0, & -\pi < y < 0, \end{cases}
> $$
>
> so that $I_N^+ = \frac1\pi\int_{-\pi}^{\pi}\psi_R(y)\cos(Ny)\,dy + \frac1\pi\int_{-\pi}^{\pi}\phi_R(y)\sin(Ny)\,dy$. Clearly $\psi_R$ is sectionally continuous. For $\phi_R$, only $y = 0$ needs attention, as in Part 3. From the left, $\phi_R = 0$. From the right, $f(x + y) - f(x+) \to 0$ as $y \to 0+$ by definition of $f(x+)$, and l'Hôpital's rule as in (18) gives
>
> $$
> \lim_{y\to0+}\phi_R(y) = \lim_{y\to0+}\frac{f'(x + y)}{\cos(\frac12 y)}\cos\big(\tfrac12 y\big) = f'(x+) .
> $$
>
> (For l'Hôpital's rule on $0 < y < \delta$, give $f$ the value $f(x+)$ at $x$; then $f(x + y) - f(x+)$ is continuous on $[0, \delta)$, differentiable on $(0, \delta)$, and vanishes at $y = 0$.) So $\phi_R$ has at most a jump at $0$ and is sectionally continuous, and Lemma §12.3 shows $I_N^+ \to 0$. In the same way, with
>
> $$
> \phi_L(y) = \frac{f(x + y) - f(x-)}{2\sin(\frac12 y)}\cos\big(\tfrac12 y\big) \quad (-\pi < y < 0), \qquad \lim_{y\to0-}\phi_L(y) = f'(x-) ,
> $$
>
> extended by $0$ to $0 < y < \pi$, and the corresponding $\psi_L$, $I_N^- \to 0$. By (22), $S_N(x) \to \frac12\big(f(x+) + f(x-)\big)$.
>
> The crux of the proof is that the function $\phi$ of (16), or $\phi_R$ and $\phi_L$ arising from (22), does not have a bad discontinuity at $y = 0$.

^pf-12-4

*Uses:* [[§12★ Proof of Convergence#^def-12-1|Def. §12.1]], [[§12★ Proof of Convergence#^lem-12-1|§12.1]], [[§12★ Proof of Convergence#^lem-12-2|§12.2]], [[§12★ Proof of Convergence#^lem-12-3|§12.3]], [[§6 Periodic Functions and Fourier Series#^def-6-2|Def. §6.2]], [[§6 Periodic Functions and Fourier Series#^prop-6-2|§6.2]], [[§8 Convergence of Fourier Series#^def-8-4|Def. §8.4]], [[§30 L'Hospital's Rule#^thm-30-1|451 Thm. §30.1]] (one-sided l'Hôpital's rule), [[§33 Properties of the Riemann Integral#^thm-33-2|451 Thm. §33.2]], [[§33 Properties of the Riemann Integral#^thm-33-5|451 Thm. §33.5]]

> [!remark]- Connections
> - Convergence of Fourier series in the mean-square sense holds for every $f \in L^2$, with no smoothness at all: [[§20 Orthonormal Sets and Bases#^rem-20-9|556 Rem. §20.9]] (the Fourier basis, [[§20 Orthonormal Sets and Bases#^thm-20-11|556 Thm. §20.11]]); Powers' version is [[§11★ Mean Error and Convergence in Mean#^thm-11-6|Theorem §11.6]], and the computational one [[§47 Applications of Inner Product Spaces#^thm-47-4|235 Thm. §47.4]]. Pointwise convergence, proved here, needs a local condition at the point $x$, which sectional smoothness provides.
> - The tools are those of Single Variable Analysis: the Riemann integral of sectionally continuous functions and one-sided l'Hôpital's rule, [[§30 L'Hospital's Rule#^thm-30-1|451 Thm. §30.1]]. For uniform convergence (continuous $f$ with sectionally continuous $f'$) see [[§9 Uniform Convergence#^thm-9-3|Theorem §9.3]].
> - See also: [[§66 Laurent Series#^ex-66-3|342 Ex. §66.3]] (for boundary values of a function analytic in an annulus, the Fourier series converges as a Laurent series) and [[§135★ Dirichlet Problem for a Disk#^thm-135-1|342 Thm. §135.1]] (for piecewise continuous $f$, the series with its terms damped by $(r/r_0)^n$ converges to $f$ at every point of continuity).

Section 1.3 states the theorem for period $2a$; it follows by stretching the variable.

> [!theorem] Corollary §12.5: Convergence for Period 2a
> If $f(x)$ is sectionally smooth and periodic with period $2a$, then at each point $x$ the Fourier series corresponding to $f$ converges, and its sum is
>
> $$
> a_0 + \sum_{n=1}^{\infty} a_n\cos\Big(\frac{n\pi x}{a}\Big) + b_n\sin\Big(\frac{n\pi x}{a}\Big) = \frac{f(x+) + f(x-)}{2} ,
> $$
>
> where $a_0 = \frac{1}{2a}\int_{-a}^{a} f(x)\,dx$, $a_n = \frac1a\int_{-a}^{a} f(x)\cos\big(\frac{n\pi x}{a}\big)dx$, $b_n = \frac1a\int_{-a}^{a} f(x)\sin\big(\frac{n\pi x}{a}\big)dx$.
>
> *Powers: 1.3, Theorem (proved in 1.7)*

^cor-12-5

> [!proof]+ Proof
> Let $g(s) = f(as/\pi)$. Then $g$ has period $2\pi$, and it is sectionally smooth: its discontinuities and the points where it is not differentiable are the images of those of $f$, finitely many per period, and $g'(s) = \frac a\pi f'(as/\pi)$ is sectionally continuous. The substitution $x = as/\pi$, $ds = \frac\pi a\,dx$, turns the coefficients of $g$ into those of $f$:
>
> $$
> \frac1\pi\int_{-\pi}^{\pi} g(s)\cos(ns)\,ds = \frac1\pi\int_{-a}^{a} f(x)\cos\Big(\frac{n\pi x}{a}\Big)\frac\pi a\,dx = a_n ,
> $$
>
> and likewise for $a_0$ and $b_n$. So the Fourier series of $g$ at $s = \pi x/a$ is, term by term, the Fourier series of $f$ at $x$. By [[§12★ Proof of Convergence#^thm-12-4|Theorem §12.4]] it converges to $\frac12\big(g(s+) + g(s-)\big) = \frac12\big(f(x+) + f(x-)\big)$.

^pf-12-5

*Uses:* [[§12★ Proof of Convergence#^thm-12-4|§12.4]], [[§7 Arbitrary Period and Half-Range Expansions#^prop-7-1|§7.1]]

> [!remark] Remark: What the Hypothesis Does
> Sectional smoothness was used only in Part 3 and Part 4, and only near $y = 0$, to keep the quotient $\big(f(x + y) - f(x\pm)\big)/y$ bounded. So the proof gives convergence at a point $x$ whenever $f$ is sectionally continuous and has finite one-sided difference-quotient limits at $x$, whatever $f$ does elsewhere. The hypothesis is sufficient but not necessary: in [[§12★ Proof of Convergence#^ex-12-3|Example §12.3]] the quotient is unbounded and the series still converges. Some local condition is needed, though: there are continuous periodic functions whose Fourier series diverge at a point (a classical construction of du Bois-Reymond, not given in the vault).

^rem-12-2

## The Crux: No Bad Discontinuity at y = 0

The three examples look at the auxiliary function $\phi$ of (16) at $x = 0$ in a corner case, a jump case, and a case where the theorem's hypothesis fails.

> [!example] Example §12.1: A Corner
> Let $f(x) = |x|$ for $-\pi < x < \pi$ and $f(x + 2\pi) = f(x)$. Then $f$ is continuous and has a corner at $x = 0$. Sketch $\phi(y)$ of (16) for $x = 0$ and find $\phi(0+)$ and $\phi(0-)$.
>
> With $x = 0$ and $f(0) = 0$,
>
> $$
> \phi(y) = \frac{|y|}{2\sin(\frac12 y)}\cos\big(\tfrac12 y\big) = \frac{|y|}{2}\cot\big(\tfrac12 y\big), \qquad -\pi < y < \pi .
> $$
>
> It is odd, falls from $1$ to $0$ on $0 < y \le \pi$ (with $\phi(\pi) = 0$), and since $\frac{y/2}{\sin(y/2)} \to 1$,
>
> $$
> \phi(0+) = \lim_{y\to0+}\frac{y}{2\sin(\frac12 y)}\cos\big(\tfrac12 y\big) = 1 = f'(0+), \qquad \phi(0-) = -1 = f'(0-) .
> $$
>
> So $\phi$ has a jump at $0$ and is sectionally continuous, as Part 3 of the proof requires, and the series converges to $f(0) = 0$. Check: the Fourier series of $f$ (even, so only cosines) has $a_0 = \frac1\pi\int_0^{\pi} x\,dx = \frac\pi2$ and $a_n = \frac2\pi\int_0^{\pi} x\cos(nx)\,dx = \frac{2}{\pi}\cdot\frac{(-1)^n - 1}{n^2}$, so
>
> $$
> |x| = \frac\pi2 - \frac4\pi\Big(\cos x + \frac{\cos 3x}{9} + \frac{\cos 5x}{25} + \cdots\Big) ,
> $$
>
> and at $x = 0$ the right side is $\frac\pi2 - \frac4\pi\cdot\frac{\pi^2}{8} = 0$, using $1 + \frac19 + \frac1{25} + \cdots = \frac{\pi^2}{8}$.
>
> *Powers: Exercise 1.7.3*

^ex-12-1

> [!example] Example §12.2: A Jump
> Let $f$ be the odd periodic extension (period $2\pi$) of $\pi - x$, $0 < x < \pi$. Then $f$ has a jump at $x = 0$: $f(0+) = \pi$, $f(0-) = -\pi$. Sketch the functions $\phi_R$, $\phi_L$ of Part 4 at $x = 0$.
>
> For $0 < y < \pi$, $f(y) - f(0+) = (\pi - y) - \pi = -y$; for $-\pi < y < 0$, $f(y) = -(\pi - (-y)) = -\pi - y$, so $f(y) - f(0-) = -y$ as well. Hence
>
> $$
> \phi_R(y) = \frac{-y}{2\sin(\frac12 y)}\cos\big(\tfrac12 y\big) \ (y > 0), \qquad \phi_L(y) = \frac{-y}{2\sin(\frac12 y)}\cos\big(\tfrac12 y\big) \ (y < 0) .
> $$
>
> Both are $-\frac y2\cot(\frac12 y)$, which rises from $-1$ near $0$ to $0$ at $y = \pm\pi$, and $\phi_R(0+) = \phi_L(0-) = -1 = f'(0\pm)$. No bad discontinuity, so the series converges at $0$ to $\frac12(\pi + (-\pi)) = 0$. Check: $b_n = \frac2\pi\int_0^{\pi}(\pi - x)\sin(nx)\,dx = \frac2n$, so the series is $2\sum_{n\ge1}\frac{\sin(nx)}{n}$, and every term vanishes at $x = 0$.
>
> *Powers: Exercise 1.7.4*

^ex-12-2

> [!example] Example §12.3: Convergence Without Sectional Smoothness
> Let $f$ be periodic with period $2\pi$ and $f(x) = |x|^{3/4}$ for $-\pi < x < \pi$.
>
> **(a) $f$ is continuous at $0$ but not sectionally smooth.** $f(x) \to 0 = f(0)$ as $x \to 0$. For $x \ne 0$, $f'(x) = \frac34|x|^{-1/4}\operatorname{sgn}x$, which is unbounded near $0$: $f'$ has a bad discontinuity there, so $f'$ is not sectionally continuous.
>
> **(b) $\phi$ has a bad discontinuity.** With $x = 0$, $\phi(y) = \dfrac{|y|^{3/4}}{2\sin(\frac12 y)}\cos\big(\tfrac12 y\big)$. Away from $0$ it is continuous. Since $2\sin(\frac12 y)/y \to 1$, $\phi(y)$ behaves like $|y|^{3/4}/y = \operatorname{sgn}(y)\,|y|^{-1/4}$, which tends to $\pm\infty$ as $y \to 0\pm$. So Part 3 of the proof does not apply.
>
> **(c) The Fourier coefficients of $\phi$ still tend to $0$.** Since $\sin u \ge \frac{2u}{\pi}$ for $0 \le u \le \frac\pi2$, we have $|2\sin(\frac12 y)| \ge \frac{2|y|}{\pi}$ for $|y| \le \pi$, and so $|\phi(y)| \le \frac\pi2|y|^{-1/4}$. Fix $0 < \delta < \pi$ and split the sine coefficient:
>
> $$
> \frac1\pi\int_{-\pi}^{\pi}\phi(y)\sin(ny)\,dy = \frac1\pi\int_{|y| < \delta}\phi(y)\sin(ny)\,dy + \frac1\pi\int_{-\pi}^{\pi}\phi_\delta(y)\sin(ny)\,dy ,
> $$
>
> where $\phi_\delta = \phi$ on $\delta \le |y| \le \pi$ and $\phi_\delta = 0$ on $|y| < \delta$. The first integral is bounded, for every $n$, by the convergent improper integral
>
> $$
> \frac1\pi\int_{-\delta}^{\delta}\frac\pi2|y|^{-1/4}\,dy = \int_0^{\delta} y^{-1/4}\,dy = \frac43\,\delta^{3/4} .
> $$
>
> The function $\phi_\delta$ is sectionally continuous (it is bounded, with jumps at $\pm\delta$ only), so the second integral tends to $0$ by Lemma §12.3. Hence
>
> $$
> \limsup_{n\to\infty}\Big|\frac1\pi\int_{-\pi}^{\pi}\phi(y)\sin(ny)\,dy\Big| \le \frac43\,\delta^{3/4}
> $$
>
> for every $\delta > 0$, and the limit is $0$. The cosine coefficients of $\psi(y) = \frac12|y|^{3/4}$ tend to $0$ by Lemma §12.3 directly. By (14) the Fourier series of $f$ converges at $0$ to $f(0) = 0$, although $f$ is not sectionally smooth: the hypothesis of Theorem §12.4 is sufficient, not necessary. What matters is that $\phi$ is absolutely integrable near $0$.
>
> *Powers: Exercise 1.7.5*

^ex-12-3
