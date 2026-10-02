---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: CA
section: CA.2
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§CA.1 Generalized Functions and Fourier Transforms]] · ↑ [[· CA Mathematical Methods]] · [[§CA.3 Gaussian Integrals, Stationary Phase and Bessel Functions]] →

*Sources: the user's PHY 513 notes, App. A §A.5 and Ch. 6 §6.5 (the working rules, stated twice there) · PHY 513 Lecture 6 (Larsen, 21 Sep 2026), "Complex Analysis: a Survival Guide" · PHY 513, Problem Set 4, Problem 1 · Stein & Shakarchi, Complex Analysis, Ch. 1–3 (cited in the user's notes).*

Every propagator, every loop integral and the Wightman function of [[§C2.5 Heisenberg Fields, Two-Point Functions and Causality|§C2.5]] are evaluated by moving contours in the complex plane. Lecture 6 compressed the subject into three facts: an integral needs a path; the one entry in the table, $\oint_{|z| = 1}\frac{dz}{2\pi iz} = 1$; and the integral does not change when the path is deformed without crossing a singularity. This section states them with proofs, adds what the course uses (residues, closing a real-line integral, poles on the path, branch cuts, the identity theorem), and ends with the sheet of working rules ([[§CA.2 Contour Integration#^thm-ca-2-9|Theorem §CA.2.9]]) that [[P2 Green's Functions by Contour Integration|P2]] and [[§C2.6 Green's Functions and the Feynman Propagator|§C2.6]] cite. Line integrals in the plane and Green's theorem are [[§16 Line Integrals and Green's Theorem#^thm-16-1|452 Thm. §16.1]]; the vault has no complex-analysis subject yet, so this is the interim home.

## Contours and analytic functions

> [!definition] Definition §CA.2.1: Contour; Contour Integral
> A **contour** $\gamma$ is a piecewise-smooth oriented curve $z(s)$, $a \le s \le b$, in $\mathbb C$, and
>
> $$
> \int_\gamma f(z)\,dz \equiv \int_a^bf\bigl(z(s)\bigr)\,z'(s)\,ds .
> $$
>
> It does not depend on the parametrization, is linear in $f$, and changes sign when the orientation is reversed.
>
> *Source: the user's PHY 513 notes, App. A §A.5 (eq. (contourdef))*

^def-ca-2-1

> [!theorem] Theorem §CA.2.1: The ML Inequality and the Basic Integral
> 1. If $|f| \le M$ on $\gamma$ and $\gamma$ has length $L$, then $\bigl|\int_\gamma f\,dz\bigr| \le ML$.
> 2. On a counterclockwise circle around $z_0$, for every integer $n$ and every radius,
>
> $$
> \oint(z - z_0)^n\,dz = 2\pi i\,\delta_{n,-1} .
> $$
>
> *Source: the user's PHY 513 notes, App. A §A.5 (Derivation "The one integral in the table") · PHY 513 Lecture 6 · PHY 513, Problem Set 4, Problem 1(a)–(d)*

^thm-ca-2-1

> [!derivation]- Derivation
> *1.* $\bigl|\int_a^bf(z(s))z'(s)\,ds\bigr| \le M\int_a^b|z'(s)|\,ds = ML$.
>
> *2.* With $z = z_0 + re^{i\varphi}$, $dz = ire^{i\varphi}d\varphi$, the integral is $ir^{n+1}\int_0^{2\pi}e^{i(n+1)\varphi}d\varphi$, which is $2\pi i$ for $n = -1$ and $0$ otherwise. For $n \ne -1$ the integrand has the single-valued antiderivative $(z - z_0)^{n+1}/(n + 1)$; only $n = -1$ fails, because $\log(z - z_0)$ gains $2\pi i$ on the way round. The lecture's table entry is $n = -1$, $z_0 = 0$, divided by $2\pi i$.

^der-ca-2-1

> [!definition] Definition §CA.2.2: Analytic Function
> $f$ is **analytic** (holomorphic) at $z$ if $f'(z) = \lim_{h\to0}[f(z + h) - f(z)]/h$ exists with the same limit from every direction of $h$. With $f = u + iv$, $z = x + iy$, this implies the **Cauchy–Riemann equations** $\partial_xu = \partial_yv$, $\partial_yu = -\partial_xv$. Polynomials, $e^z$, and rational functions away from the zeros of their denominators are analytic; $\bar z$ and $|z|^2$ are not.
>
> *Source: the user's PHY 513 notes, App. A §A.5 (eq. (CR))*

^def-ca-2-2

> [!theorem] Theorem §CA.2.2: Cauchy's Theorem; Deformation of Contours
> If $f$ is analytic on and inside a closed contour $\Gamma$, then $\oint_\Gamma f\,dz = 0$. Hence the integral between two points does not depend on the path, as long as one path can be deformed into the other without crossing a point where $f$ is not analytic. An analytic function is infinitely differentiable and equals its Taylor series in every disc of analyticity.
>
> *Source: the user's PHY 513 notes, App. A §A.5 (Principle "Cauchy's theorem") · Stein & Shakarchi, Ch. 2*

^thm-ca-2-2

> [!derivation]- Derivation
> For $u$, $v$ with continuous partial derivatives: $\oint f\,dz = \oint(u\,dx - v\,dy) + i\oint(v\,dx + u\,dy)$. Green's theorem ([[§16 Line Integrals and Green's Theorem#^thm-16-1|452 Thm. §16.1]]) turns the two pieces into $\iint(-\partial_xv - \partial_yu)$ and $\iint(\partial_xu - \partial_yv)$, both zero by Cauchy–Riemann. Goursat's proof removes the continuity assumption. The deformation statement follows by applying the theorem to the closed contour made of one path and the reverse of the other. The Taylor expansion follows from Cauchy's integral formula (Stein & Shakarchi, Ch. 2, Theorem 4.4), which is not reproduced here.

^der-ca-2-2

*Uses:* [[§16 Line Integrals and Green's Theorem#^thm-16-1|452 Thm. §16.1]]

> [!theorem] Theorem §CA.2.3: Identity Theorem
> If $f$ and $g$ are analytic on a connected open set $U$ and agree on a subset of $U$ with an accumulation point in $U$, then $f = g$ on all of $U$. In particular an analytic continuation, when it exists, is unique.
>
> *Source: the user's PHY 513 notes, Ch. 5 §5.4 (Principle "Tools used in this section and the next") · Stein & Shakarchi, Ch. 2*

^thm-ca-2-3

> [!derivation]- Derivation
> Let $h = f - g$, zero on a set accumulating at $z_0 \in U$. Expand $h$ in its Taylor series at $z_0$ ([[§CA.2 Contour Integration#^thm-ca-2-2|Theorem §CA.2.2]]). If some coefficient were nonzero, then $h = (z - z_0)^ku(z)$ with $u$ analytic and $u(z_0) \ne 0$, so $h \ne 0$ on a punctured disc around $z_0$, contradicting the accumulation. So $h \equiv 0$ near $z_0$. The set of points of $U$ near which $h$ vanishes identically is therefore nonempty and open, and by the same argument applied at its limit points it is closed in $U$; $U$ being connected, it is all of $U$.

^der-ca-2-3

*Uses:* [[§CA.2 Contour Integration#^thm-ca-2-2|Theorem §CA.2.2]]

## Residues

> [!definition] Definition §CA.2.3: Isolated Singularity; Laurent Expansion; Residue
> $z_0$ is an **isolated singularity** of $f$ if $f$ is analytic on a punctured disc $0 < |z - z_0| < \rho$ but not at $z_0$. There $f = \sum_{n=-\infty}^{\infty}a_n(z - z_0)^n$ (Laurent), and the singularity is **removable**, a **pole of order $k$** or **essential** as the negative powers are absent, stop at $n = -k$, or do not stop. The **residue** is
>
> $$
> \operatorname*{Res}_{z_0}f \equiv a_{-1} = \frac{1}{2\pi i}\oint_{|z - z_0| = r}f(z)\,dz \qquad (0 < r < \rho) .
> $$
>
> *Source: the user's PHY 513 notes, App. A §A.5 (Definitions "Isolated singularities and the Laurent expansion", "Definition of the residue")*

^def-ca-2-3

> [!remark] Remark: What a residue is
> The residue is a number attached to the function and the point together; it is not the value $f(z_0)$, which does not exist, but the coefficient of the $1/(z - z_0)$ part of how $f$ blows up. The two forms in the definition say the same thing from two sides: integrating the Laurent series term by term round a circle, [[§CA.2 Contour Integration#^thm-ca-2-1|Theorem §CA.2.1]], 2 kills every power but $n = -1$. A closed loop detects that one term and nothing else: the analytic part and the higher poles alike have single-valued antiderivatives.
>
> *Source: the user's PHY 513 notes, App. A §A.5*

^rem-ca-2-1

> [!theorem] Theorem §CA.2.4: Computing Residues
> 1. Simple pole: $\operatorname{Res}_{z_0}f = \lim_{z\to z_0}(z - z_0)f(z)$; for $f = g/h$ with $g$ analytic and $h$ having a simple zero, $\operatorname{Res}_{z_0}(g/h) = g(z_0)/h'(z_0)$.
> 2. Pole of order $k$: $\operatorname{Res}_{z_0}f = \dfrac{1}{(k - 1)!}\lim_{z\to z_0}\dfrac{d^{k-1}}{dz^{k-1}}\bigl[(z - z_0)^kf(z)\bigr]$.
> 3. For the propagator integrand, $\operatorname*{Res}_{p^0 = \pm E}\dfrac{e^{-ip^0t}}{(p^0)^2 - E^2} = \pm\dfrac{e^{\mp iEt}}{2E}$.
>
> *Source: the user's PHY 513 notes, App. A §A.5 (eqs. (residueformulas), (propresidues))*

^thm-ca-2-4

> [!derivation]- Derivation
> *1.* $f = a_{-1}/(z - z_0) + (\text{analytic})$; and $h(z) = h'(z_0)(z - z_0) + O\bigl((z - z_0)^2\bigr)$. *2.* $(z - z_0)^kf$ is analytic, and $a_{-1}$ is its $(k - 1)$-th Taylor coefficient. Example: $e^z/z^2 = z^{-2} + z^{-1} + \tfrac12 + \cdots$ has residue $1$, the coefficient of $z^{-1}$, not of $z^{-2}$. *3.* $g = e^{-ip^0t}$, $h = (p^0)^2 - E^2$, $h' = 2p^0$; equivalently the partial fractions $\frac{1}{(p^0)^2 - E^2} = \frac{1}{2E}\bigl(\frac{1}{p^0 - E} - \frac{1}{p^0 + E}\bigr)$.

^der-ca-2-4

> [!theorem] Theorem §CA.2.5: Residue Theorem
> If $f$ is analytic on a closed contour $\Gamma$ and inside it except at finitely many isolated singularities $z_1, \dots, z_N$, then
>
> $$
> \oint_\Gamma f\,dz = \pm2\pi i\sum_{k=1}^N\operatorname*{Res}_{z_k}f ,
> $$
>
> with $+$ for counterclockwise and $-$ for clockwise traversal. Singularities outside $\Gamma$ contribute nothing.
>
> *Source: the user's PHY 513 notes, App. A §A.5 (Principle "The residue theorem")*

^thm-ca-2-5

> [!derivation]- Derivation
> By Cauchy's theorem ([[§CA.2 Contour Integration#^thm-ca-2-2|Theorem §CA.2.2]]) deform $\Gamma$, without changing the integral, into small circles around each $z_k$ joined by pairs of segments traversed in both directions, which cancel. On each circle the integral is $2\pi i\operatorname{Res}_{z_k}f$ ([[§CA.2 Contour Integration#^def-ca-2-3|Def. §CA.2.3]]); reversing the orientation reverses the sign.

^der-ca-2-5

*Uses:* [[§CA.2 Contour Integration#^thm-ca-2-2|Theorem §CA.2.2]], [[§CA.2 Contour Integration#^def-ca-2-3|Def. §CA.2.3]]

## Integrals along the real line

> [!theorem] Theorem §CA.2.6: Closing the Contour: the ML Estimate and Jordan's Lemma
> Let $C_R$ be the upper semicircle of radius $R$.
> 1. *(Algebraic decay)* If $|f| \le C/R^{1+\delta}$ on $C_R$ for some $\delta > 0$, then $\int_{C_R}f\,dz \to 0$.
> 2. *(Jordan)* If $\max_{C_R}|g| \to 0$, at any rate, and $\lambda > 0$, then $\int_{C_R}g(z)\,e^{i\lambda z}\,dz \to 0$. For $e^{-i\lambda z}$ use the lower semicircle.
>
> So a real-line integral may be closed where the integrand decays: $e^{ikz}$ upward for $k > 0$, downward for $k < 0$; $e^{-ip^0t}$ upward for $t < 0$, downward for $t > 0$.
>
> *Source: the user's PHY 513 notes, App. A §A.5 ("Integrals along the real line: closing the contour"), Ch. 5 §5.4*

^thm-ca-2-6

> [!derivation]- Derivation
> *1.* ML: $\pi R\cdot C/R^{1+\delta} \to 0$. A rational function whose denominator has degree at least two more than its numerator qualifies.
>
> *2.* On $C_R$, $|e^{i\lambda z}| = e^{-\lambda R\sin\theta}$, and $\sin\theta \ge 2\theta/\pi$ on $[0, \pi/2]$, so $\int_0^\pi e^{-\lambda R\sin\theta}R\,d\theta \le 2\int_0^{\pi/2}e^{-2\lambda R\theta/\pi}R\,d\theta < \pi/\lambda$. The arc is at most $(\pi/\lambda)\max_{C_R}|g| \to 0$.
>
> *Which side.* $|e^{ikz}| = e^{-k\operatorname{Im}z}$ decays in the upper half-plane for $k > 0$; $|e^{-ip^0t}| = e^{t\operatorname{Im}p^0}$ decays in the upper half-plane for $t < 0$. The sign of the time difference, causal order, decides the contour.

^der-ca-2-6

> [!caution] Caution: Jordan's lemma needs $g \to 0$
> No rate of decay is required, but $g$ must tend to zero. For the equal-time Wightman integrand $p\,e^{ipr}/\sqrt{p^2 + m^2}$ the kernel tends to $1$ and the lemma fails; the cure there is to write $p\,e^{ipr} = -i\partial_re^{ipr}$ first ([[§C2.5 Heisenberg Fields, Two-Point Functions and Causality#^thm-c2-5-7|Theorem §C2.5.7]], second route). Nor may a regulator such as $e^{-\varepsilon p}$ be kept on the arc: near $\arg p = \pi$ it grows like $e^{\varepsilon R}$.
>
> *Source: the user's PHY 513 notes, Ch. 5 §5.4*

^cau-ca-2-1

> [!example] Example §CA.2.1: Two Lorentzian Integrals
> For $a > 0$, evaluate $\int_{-\infty}^\infty\frac{dx}{x^2 + a^2}$ and $I(k) = \int_{-\infty}^{\infty}\frac{e^{ikx}\,dx}{x^2 + a^2}$.
>
> *No exponential.* The integrand decays like $1/R^2$, so close either way. Upward, the enclosed pole $ia$ has residue $1/2ia$ ([[§CA.2 Contour Integration#^thm-ca-2-4|Theorem §CA.2.4]]), and the integral is $2\pi i/2ia = \pi/a$: the elementary $\arctan$ result (substitute $x = a\tan u$). Closing downward, clockwise, round $-ia$ (residue $-1/2ia$) gives the same.
>
> *With the exponential.* For $k > 0$ close upward (Jordan): $2\pi i\cdot e^{-ka}/2ia$. For $k < 0$ close downward, clockwise, round $-ia$ with residue $e^{ka}/(-2ia)$: $-2\pi i\cdot e^{ka}/(-2ia)$. Together,
>
> $$
> \int_{-\infty}^{\infty}\frac{e^{ikx}\,dx}{x^2 + a^2} = \frac\pi a\,e^{-a|k|} .
> $$
>
> The two signs of $k$ need two contours and pick up two different poles, and the answer has a kink at $k = 0$ where the choice switches: the pattern of every propagator computation. Physically it is the one-dimensional static Green's function of $-\partial_x^2 + a^2$, a Yukawa profile of range $1/a$.
>
> *Source: the user's PHY 513 notes, App. A §A.5 (worked examples (i), (ii)) · PHY 513, Problem Set 4, Problem 1(e)–(i) (the first integral)*

^ex-ca-2-1

## Poles on the path and branch cuts

> [!theorem] Theorem §CA.2.7: Poles on the Contour: the Half-Residue Lemma
> Let $f = g/(z - x_0)$ with $g$ analytic near a real $x_0$. A small semicircle passing *above* $x_0$ (clockwise) contributes $-i\pi g(x_0)$, one passing *below* (counterclockwise) $+i\pi g(x_0)$, so
>
> $$
> \int_{\text{above}}f = \mathcal P\!\!\int f - i\pi\operatorname*{Res}_{x_0}f, \qquad \int_{\text{below}}f = \mathcal P\!\!\int f + i\pi\operatorname*{Res}_{x_0}f .
> $$
>
> Passing above a pole is the same as moving it down by $i\varepsilon$; the principal value is the average of the two.
>
> *Source: the user's PHY 513 notes, App. A §A.5 (Derivation "The half-residue lemma")*

^thm-ca-2-7

> [!derivation]- Derivation
> On $z = x_0 + re^{i\varphi}$ with $\varphi$ from $\pi$ to $0$ (above, clockwise), $\int f\,dz = \int_\pi^0\frac{g(x_0 + re^{i\varphi})}{re^{i\varphi}}\,ire^{i\varphi}\,d\varphi \to -i\pi g(x_0)$ as $r \to 0$; below, $\varphi$ runs from $\pi$ to $2\pi$ and gives $+i\pi g(x_0)$. The straight pieces outside $|x - x_0| < r$ tend to the principal value ([[§CA.1 Generalized Functions and Fourier Transforms#^def-ca-1-4|Def. §CA.1.4]]). Moving the pole instead of the path: by Cauchy's theorem the real axis with the pole at $x_0 - i\varepsilon$ may be deformed to pass above $x_0$, and as $\varepsilon \to 0$ this is the contour above the pole. As an identity of generalized functions this is the Sokhotski–Plemelj formula ([[§CA.1 Generalized Functions and Fourier Transforms#^thm-ca-1-8|Theorem §CA.1.8]]).

^der-ca-2-7

*Uses:* [[§CA.1 Generalized Functions and Fourier Transforms#^def-ca-1-4|Def. §CA.1.4]], [[§CA.2 Contour Integration#^thm-ca-2-2|Theorem §CA.2.2]]

> [!example] Example §CA.2.2: A Step Function from a Pole
> Show that $\displaystyle\lim_{\varepsilon\to0^+}\int_{-\infty}^{\infty}\frac{dx}{2\pi i}\,\frac{e^{ikx}}{x - i\varepsilon} = \theta(k)$.
>
> The pole sits at $i\varepsilon$, just above the axis. For $k > 0$ close upward (Jordan): the pole is enclosed counterclockwise, and the result is $e^{-k\varepsilon} \to 1$. For $k < 0$ close downward: nothing is enclosed, and the result is $0$. A single pole infinitesimally off the axis produces a step function, and the side it sits on decides which sign of $k$ survives. With $k$ a time, this is causality in its most compact form, the mechanism of the retarded Green's function ([[§C2.6 Green's Functions and the Feynman Propagator#^thm-c2-6-4|Theorem §C2.6.4]]).
>
> *Source: the user's PHY 513 notes, App. A §A.5 (worked example (iii))*

^ex-ca-2-2

> [!theorem] Theorem §CA.2.8: Integrals around a Branch Cut
> A branch point (for example $\pm im$ of $\sqrt{p^2 + m^2}$) is not an isolated singularity: going once round it changes the function, so it has no Laurent series and no residue. The function is made single-valued by a **cut** from the branch point; a contour may be deformed onto the cut, and the integral becomes the integral of the discontinuity across it. An integrable branch point ($|f| = O(\delta^{-1/2})$ on a circle of radius $\delta$) contributes nothing as $\delta \to 0$.
>
> *Source: the user's PHY 513 notes, App. A §A.5 ("Not every singularity is isolated"), Ch. 5 §5.4 (keyhole contour) · PS §2.4, Fig. 2.3*

^thm-ca-2-8

> [!derivation]- Derivation
> On the cut-plane the function is analytic, so Cauchy's theorem applies to any closed contour that does not cross the cut: the real line, the large arc, the two lips of the cut traversed in opposite directions, and a small circle round the branch point. The lips carry the two boundary values of the function, so together they give $\int(f_{\text{one side}} - f_{\text{other side}})$, the discontinuity. The small circle contributes at most $2\pi\delta\cdot O(\delta^{-1/2}) = O(\delta^{1/2})$ (ML, [[§CA.2 Contour Integration#^thm-ca-2-1|Theorem §CA.2.1]]). The worked case is the equal-time Wightman function, where the two lips *add* ([[§C2.5 Heisenberg Fields, Two-Point Functions and Causality#^thm-c2-5-7|Theorem §C2.5.7]], second route).

^der-ca-2-8

*Uses:* [[§CA.2 Contour Integration#^thm-ca-2-1|Theorem §CA.2.1]], [[§CA.2 Contour Integration#^thm-ca-2-2|Theorem §CA.2.2]]

![[ph-qft-ca-2-1.svg]]
*The complex $p$-plane for the position-space two-point integrals with phase $pr - t\sqrt{p^2 + m^2}$. $\sqrt{p^2 + m^2}$ has branch points at $\pm im$, with cuts to $\pm i\infty$. For $r > |t|$ the large arc contributes nothing, and the real-line integral equals the integral around the upper cut, down its right lip and up its left lip (Theorem §CA.2.8). The saddle point of [[§CA.3 Gaussian Integrals, Stationary Phase and Bessel Functions#^ex-ca-3-1|Example §CA.3.1]] lies on this cut. Adapted from the user's PHY 513 notes, Fig. 2.2.*

## The working rules

> [!theorem] Theorem §CA.2.9: Working Rules for Contour Integrals
> 1. *Orientation:* counterclockwise $+2\pi i\sum\operatorname{Res}$, clockwise $-2\pi i\sum\operatorname{Res}$; closing a real-line integral upward is counterclockwise, downward clockwise.
> 2. *Where to close:* where the integrand decays; $e^{ikz}$ upward for $k > 0$, $e^{-ip^0t}$ upward for $t < 0$ and downward for $t > 0$.
> 3. *When the arc vanishes:* decay faster than $1/R$ (ML), or decay to zero at any rate times an exponential in its good half-plane (Jordan). Check it: it can fail.
> 4. *Deformation:* free through regions of analyticity; pushing the contour across a pole changes the answer by $\pm2\pi i\operatorname{Res}$.
> 5. *Residues:* $g(z_0)/h'(z_0)$ at a simple zero of the denominator, or split the poles by partial fractions first.
> 6. *Poles on the path:* undefined until told how to pass each pole; above and below differ by $2\pi i\operatorname{Res}$; passing above = moving the pole down by $i\varepsilon$; the principal value is the average.
> 7. *Branch points are not poles:* they need cuts, and the integral round a cut is the integral of the discontinuity.
>
> *Source: the user's PHY 513 notes, App. A §A.5 (Principle "Working rules"), Ch. 6 §6.5 (Principle "Recall: working rules", the same list)*

^thm-ca-2-9

> [!derivation]- Derivation
> Rule 1 is [[§CA.2 Contour Integration#^thm-ca-2-5|Theorem §CA.2.5]]; rules 2–3 are [[§CA.2 Contour Integration#^thm-ca-2-6|Theorem §CA.2.6]]; rule 4 is [[§CA.2 Contour Integration#^thm-ca-2-2|Theorem §CA.2.2]] with the residue theorem applied to the loop between the two contours; rule 5 is [[§CA.2 Contour Integration#^thm-ca-2-4|Theorem §CA.2.4]]; rule 6 is [[§CA.2 Contour Integration#^thm-ca-2-7|Theorem §CA.2.7]] and [[§CA.1 Generalized Functions and Fourier Transforms#^thm-ca-1-8|Theorem §CA.1.8]]; rule 7 is [[§CA.2 Contour Integration#^thm-ca-2-8|Theorem §CA.2.8]].

^der-ca-2-9

*Uses:* [[§CA.2 Contour Integration#^thm-ca-2-2|Theorem §CA.2.2]], [[§CA.2 Contour Integration#^thm-ca-2-4|Theorem §CA.2.4]], [[§CA.2 Contour Integration#^thm-ca-2-5|Theorem §CA.2.5]], [[§CA.2 Contour Integration#^thm-ca-2-6|Theorem §CA.2.6]], [[§CA.2 Contour Integration#^thm-ca-2-7|Theorem §CA.2.7]], [[§CA.2 Contour Integration#^thm-ca-2-8|Theorem §CA.2.8]], [[§CA.1 Generalized Functions and Fourier Transforms#^thm-ca-1-8|Theorem §CA.1.8]]

> [!remark] Remark: "Move the contour up to infinity"
> The lecture's phrasing for closing a contour is the same argument as the semicircle: the real-axis integral equals the integral along the line $\operatorname{Im}p^0 = L$ plus two vertical segments at $\operatorname{Re}p^0 = \pm X$; the segments vanish as $X \to \infty$, and on the shifted line the integrand carries $e^{-L|t|}$, which kills it as $L \to \infty$. Both descriptions are correct; the closed contour is the one that generalizes, and the procedure built on it is [[P2 Green's Functions by Contour Integration|P2]].
>
> *Source: the user's PHY 513 notes, Ch. 6 §6.5 (Derivation "Closing the contour for the Green's function", "The lecture's version")*

^rem-ca-2-2

> [!remark]- Connections
> - Example §CA.2.1 is the one-dimensional cousin of the Yukawa potential ([[§B4.1 The Klein–Gordon Equation#^rem-b4-1-4|REL Remark: Static solutions and the Yukawa potential]]) and of the free scattering Green's function $-e^{ik\rho}/4\pi\rho$, whose $k'$-plane integral closes the two exponentials on opposite sides exactly as here ([[§C10.1 The Lippmann–Schwinger Equation and the Born Approximation#^thm-c10-1-3|QM Theorem §C10.1.3]]).
> - Example §CA.2.2 is the transform behind every causal response: the energy transform of a retarded propagator is analytic in the upper half-plane ([[§C4.1 Propagators#^thm-c4-1-7|QM Theorem §C4.1.7]]), the impulse response of a damped oscillator vanishes before the kick ([[§B4.4 Fourier Transforms and the Delta Function#^thm-b4-4-6|WO Theorem §B4.4.6]], whose transform $\chi(\omega)$ has its poles in one half-plane), and the retarded Green's function of the Klein–Gordon field passes above both poles ([[§C2.6 Green's Functions and the Feynman Propagator#^thm-c2-6-4|Theorem §C2.6.4]]).
> - The half-residue lemma is what QM uses for the imaginary part of the resolvent in the optical theorem ([[§C10.2 The Eikonal Approximation and the Optical Theorem|QM §C10.2]]); its distribution form is [[§CA.1 Generalized Functions and Fourier Transforms#^thm-ca-1-8|Theorem §CA.1.8]].
> - The identity theorem makes analytic continuation unique; it is what turns one Euclidean evaluation into the Wightman function everywhere ([[§C2.5 Heisenberg Fields, Two-Point Functions and Causality#^thm-c2-5-7|Theorem §C2.5.7]]) and what extends the Gaussian integral to complex variance ([[§C4.1 Propagators#^thm-c4-1-3|QM Theorem §C4.1.3]]).
> - Green's theorem in the plane ([[§16 Line Integrals and Green's Theorem#^thm-16-1|452 Thm. §16.1]]) is the whole proof of Cauchy's theorem for smooth $u$, $v$; Cauchy–Riemann says that $u\,dx - v\,dy$ and $v\,dx + u\,dy$ are closed forms.
> - Loop integrals (QFT C7, planned) bring branch cuts back, and the spinor and vector propagators (QFT C4–C5, planned) have numerators that are analytic in $p^0$, so the same residues give them the same $i\varepsilon$ (Yu eq. (6.262)).
