---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: CA
section: CA.4
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§CA.3 Fourier Transforms and Fourier Tricks]] · ↑ [[· CA Mathematical Methods]] · [[§CA.5 Gaussian Integrals, Stationary Phase and Bessel Functions]] →

*Sources: the user's PHY 513 notes, App. A §A.5 and Ch. 6 §6.5 (the working rules, stated twice there) · PHY 513 Lecture 6 (Larsen, 21 Sep 2026), "Complex Analysis: a Survival Guide" · PHY 513, Problem Set 4, Problem 1 · Stein & Shakarchi, Complex Analysis, Ch. 1–3 (cited in the user's notes).*

Every propagator, every loop integral and the Wightman function of [[§C2.9 Explicit Forms of the Wightman Function|§C2.9]] are evaluated by moving contours in the complex plane. Lecture 6 compressed the subject into three facts: an integral needs a path; the one entry in the table, $\oint_{|z| = 1}\frac{dz}{2\pi iz} = 1$; and the integral does not change when the path is deformed without crossing a singularity. This section states them with proofs, adds what the course uses (residues, closing a real-line integral, poles on the path, branch cuts, the identity theorem), and ends with the sheet of working rules ([[§CA.4 Contour Integration#^thm-ca-4-9|Theorem §CA.4.9]]) that [[P2 Green's Functions by Contour Integration|P2]] and [[§C2.11 Green's Functions and Contours|§C2.11]]–[[§C2.13 Wick Rotation and the Two-Point Family|§C2.13]] cite. Line integrals in the plane and Green's theorem are [[§16 Line Integrals and Green's Theorem#^thm-16-1|452 Thm. §16.1]]; the vault has no complex-analysis subject yet, so this is the interim home.

## Contours and analytic functions

> [!definition] Definition §CA.4.1: Contour; Contour Integral
> A **contour** $\gamma$ is a piecewise-smooth oriented curve $z(s)$, $a \le s \le b$, in $\mathbb C$, and
>
> $$
> \int_\gamma f(z)\,dz \equiv \int_a^bf\bigl(z(s)\bigr)\,z'(s)\,ds .
> $$
>
> It does not depend on the parametrization, is linear in $f$, and changes sign when the orientation is reversed.
>
> *Source: the user's PHY 513 notes, App. A §A.5 (eq. (contourdef))*

^def-ca-4-1

> [!theorem] Theorem §CA.4.1: The ML Inequality and the Basic Integral
> 1. If $|f| \le M$ on $\gamma$ and $\gamma$ has length $L$, then $\bigl|\int_\gamma f\,dz\bigr| \le ML$.
> 2. On a counterclockwise circle around $z_0$, for every integer $n$ and every radius,
>
> $$
> \oint(z - z_0)^n\,dz = 2\pi i\,\delta_{n,-1} .
> $$
>
> *Source: the user's PHY 513 notes, App. A §A.5 (Derivation "The one integral in the table") · PHY 513 Lecture 6 · PHY 513, Problem Set 4, Problem 1(a)–(d)*

^thm-ca-4-1

> [!derivation]- Derivation
> **Step 1** (ML). $\bigl|\int_a^bf(z(s))z'(s)\,ds\bigr| \le \int_a^b|f(z(s))|\,|z'(s)|\,ds \le M\int_a^b|z'(s)|\,ds = ML$.
>
> **Step 2** (parametrize the circle). $z = z_0 + re^{i\varphi}$, $\varphi: 0 \to 2\pi$ (counterclockwise), $dz = ire^{i\varphi}d\varphi$, $(z - z_0)^n = r^ne^{in\varphi}$:
>
> $$
> \oint(z - z_0)^n\,dz = ir^{n+1}\int_0^{2\pi}e^{i(n+1)\varphi}\,d\varphi .
> $$
>
> **Step 3** (evaluate). For $n = -1$ the integrand is $1$ and the result is $2\pi i$, independent of $r$. For $n \ne -1$, $\int_0^{2\pi}e^{i(n+1)\varphi}d\varphi = \bigl[e^{i(n+1)\varphi}/i(n+1)\bigr]_0^{2\pi} = 0$.
>
> **What the derivation shows.**
> - For $n \ne -1$ the integrand has the single-valued antiderivative $(z - z_0)^{n+1}/(n + 1)$, which returns to its starting value; only $n = -1$ fails, because $\log(z - z_0)$ gains $2\pi i$ on the way round.
> - The lecture's table entry is $n = -1$, $z_0 = 0$, divided by $2\pi i$; the independence of $r$ is the first instance of contour deformation (Theorem §CA.4.2).

^der-ca-4-1

*Uses:* [[§CA.4 Contour Integration#^def-ca-4-1|Def. §CA.4.1]]

> [!definition] Definition §CA.4.2: Analytic Function
> $f$ is **analytic** (holomorphic) at $z$ if $f'(z) = \lim_{h\to0}[f(z + h) - f(z)]/h$ exists with the same limit from every direction of $h$. With $f = u + iv$, $z = x + iy$, this implies the **Cauchy–Riemann equations** $\partial_xu = \partial_yv$, $\partial_yu = -\partial_xv$. Polynomials, $e^z$, and rational functions away from the zeros of their denominators are analytic; $\bar z$ and $|z|^2$ are not.
>
> *Source: the user's PHY 513 notes, App. A §A.5 (eq. (CR))*

^def-ca-4-2

> [!theorem] Theorem §CA.4.2: Cauchy's Theorem; Deformation of Contours
> If $f$ is analytic on and inside a closed contour $\Gamma$, then $\oint_\Gamma f\,dz = 0$. Hence the integral between two points does not depend on the path, as long as one path can be deformed into the other without crossing a point where $f$ is not analytic. An analytic function is infinitely differentiable and equals its Taylor series in every disc of analyticity.
>
> *Source: the user's PHY 513 notes, App. A §A.5 (Principle "Cauchy's theorem") · Stein & Shakarchi, Ch. 2*

^thm-ca-4-2

> [!derivation]- Derivation
> **Step 1** (real form). With $f = u + iv$ and $dz = dx + i\,dy$: $\oint f\,dz = \oint(u\,dx - v\,dy) + i\oint(v\,dx + u\,dy)$.
>
> **Step 2** (Green's theorem). For $u$, $v$ with continuous partial derivatives, [[§16 Line Integrals and Green's Theorem#^thm-16-1|452 Thm. §16.1]], $\oint(P\,dx + Q\,dy) = \iint(\partial_xQ - \partial_yP)\,dx\,dy$, turns the two pieces into $\iint(-\partial_xv - \partial_yu)$ and $\iint(\partial_xu - \partial_yv)$.
>
> **Step 3** (Cauchy–Riemann). Both integrands vanish ([[§CA.4 Contour Integration#^def-ca-4-2|Def. §CA.4.2]]), so $\oint f\,dz = 0$. Goursat's proof removes the continuity assumption.
>
> **Step 4** (deformation). Two paths from $z_1$ to $z_2$ that can be deformed into each other through a region of analyticity form, with one reversed, a closed contour with $f$ analytic inside; by Step 3 its integral is zero, so the two path integrals are equal.
>
> **Step 5** (Taylor series). Follows from Cauchy's integral formula (Stein & Shakarchi, Ch. 2, Theorem 4.4), not reproduced here.
>
> **What the derivation shows.**
> - Cauchy–Riemann says that $u\,dx - v\,dy$ and $v\,dx + u\,dy$ are closed forms; Cauchy's theorem is Green's theorem for them.
> - Used everywhere a contour is moved: closing contours, moving poles by $i\varepsilon$, Wick rotation.

^der-ca-4-2

*Uses:* [[§16 Line Integrals and Green's Theorem#^thm-16-1|452 Thm. §16.1]]

> [!theorem] Theorem §CA.4.3: Identity Theorem
> If $f$ and $g$ are analytic on a connected open set $U$ and agree on a subset of $U$ with an accumulation point in $U$, then $f = g$ on all of $U$. In particular an analytic continuation, when it exists, is unique.
>
> *Source: the user's PHY 513 notes, Ch. 5 §5.4 (Principle "Tools used in this section and the next") · Stein & Shakarchi, Ch. 2*

^thm-ca-4-3

> [!derivation]- Derivation
> **Step 1** (local). Let $h = f - g$, zero on a set accumulating at $z_0 \in U$. Expand $h = \sum_na_n(z - z_0)^n$ in a disc around $z_0$ ([[§CA.4 Contour Integration#^thm-ca-4-2|Theorem §CA.4.2]]). If some $a_n \ne 0$, let $k$ be the first: $h = (z - z_0)^ku(z)$ with $u$ analytic and $u(z_0) = a_k \ne 0$, so by continuity $u \ne 0$ near $z_0$ and $h \ne 0$ on a punctured disc around $z_0$, contradicting the accumulation of zeros. So all $a_n = 0$: $h \equiv 0$ near $z_0$.
>
> **Step 2** (global). Let $A$ be the set of points of $U$ near which $h$ vanishes identically. $A$ is open by definition and nonempty by Step 1. If $w \in U$ is a limit of points of $A$, then $w$ is an accumulation point of zeros of $h$, and Step 1 at $w$ gives $w \in A$: $A$ is closed in $U$. $U$ is connected, so $A = U$.
>
> **What the derivation shows.**
> - Connectedness is essential: on two disjoint discs an analytic function can be $0$ on one and $1$ on the other.
> - Used to continue one Euclidean evaluation to the Wightman function everywhere ([[§C2.9 Explicit Forms of the Wightman Function#^thm-c2-9-2|Theorem §C2.9.2]]) and the Gaussian integral to complex variance ([[§C4.1 Propagators#^thm-c4-1-3|QM Theorem §C4.1.3]]).

^der-ca-4-3

*Uses:* [[§CA.4 Contour Integration#^thm-ca-4-2|Theorem §CA.4.2]]

## Residues

> [!definition] Definition §CA.4.3: Isolated Singularity; Laurent Expansion; Residue
> $z_0$ is an **isolated singularity** of $f$ if $f$ is analytic on a punctured disc $0 < |z - z_0| < \rho$ but not at $z_0$. There $f = \sum_{n=-\infty}^{\infty}a_n(z - z_0)^n$ (Laurent), and the singularity is **removable**, a **pole of order $k$** or **essential** as the negative powers are absent, stop at $n = -k$, or do not stop. The **residue** is
>
> $$
> \operatorname*{Res}_{z_0}f \equiv a_{-1} = \frac{1}{2\pi i}\oint_{|z - z_0| = r}f(z)\,dz \qquad (0 < r < \rho) .
> $$
>
> *Source: the user's PHY 513 notes, App. A §A.5 (Definitions "Isolated singularities and the Laurent expansion", "Definition of the residue")*

^def-ca-4-3

> [!remark] Remark: What a residue is
> The residue is a number attached to the function and the point together; it is not the value $f(z_0)$, which does not exist, but the coefficient of the $1/(z - z_0)$ part of how $f$ blows up. The two forms in the definition say the same thing from two sides: integrating the Laurent series term by term round a circle, [[§CA.4 Contour Integration#^thm-ca-4-1|Theorem §CA.4.1]], 2 kills every power but $n = -1$. A closed loop detects that one term and nothing else: the analytic part and the higher poles alike have single-valued antiderivatives.
>
> *Source: the user's PHY 513 notes, App. A §A.5*

^rem-ca-4-1

> [!theorem] Theorem §CA.4.4: Computing Residues
> 1. Simple pole: $\operatorname{Res}_{z_0}f = \lim_{z\to z_0}(z - z_0)f(z)$; for $f = g/h$ with $g$ analytic and $h$ having a simple zero, $\operatorname{Res}_{z_0}(g/h) = g(z_0)/h'(z_0)$.
> 2. Pole of order $k$: $\operatorname{Res}_{z_0}f = \dfrac{1}{(k - 1)!}\lim_{z\to z_0}\dfrac{d^{k-1}}{dz^{k-1}}\bigl[(z - z_0)^kf(z)\bigr]$.
> 3. For the propagator integrand, $\operatorname*{Res}_{p^0 = \pm E}\dfrac{e^{-ip^0t}}{(p^0)^2 - E^2} = \pm\dfrac{e^{\mp iEt}}{2E}$.
>
> *Source: the user's PHY 513 notes, App. A §A.5 (eqs. (residueformulas), (propresidues))*

^thm-ca-4-4

> [!derivation]- Derivation
> **Step 1** (simple pole). Near $z_0$, $f = \frac{a_{-1}}{z - z_0} + (\text{analytic})$, so $(z - z_0)f \to a_{-1}$. For $f = g/h$: $h(z) = h'(z_0)(z - z_0) + O\bigl((z - z_0)^2\bigr)$ with $h'(z_0) \ne 0$, so $(z - z_0)\frac{g}{h} \to \frac{g(z_0)}{h'(z_0)}$.
>
> **Step 2** (order $k$). $(z - z_0)^kf = a_{-k} + \cdots + a_{-1}(z - z_0)^{k-1} + \cdots$ is analytic, and $a_{-1}$ is its $(k - 1)$-th Taylor coefficient, $\frac{1}{(k - 1)!}\frac{d^{k-1}}{dz^{k-1}}$ at $z_0$. Example: $e^z/z^2 = z^{-2} + z^{-1} + \tfrac12 + \cdots$ has residue $1$, the coefficient of $z^{-1}$, not of $z^{-2}$.
>
> **Step 3** (the propagator). $g = e^{-ip^0t}$, $h = (p^0)^2 - E^2$, $h'(p^0) = 2p^0$: at $p^0 = E$, $\frac{e^{-iEt}}{2E}$; at $p^0 = -E$, $\frac{e^{iEt}}{-2E}$. Equivalently, the partial fractions $\frac{1}{(p^0)^2 - E^2} = \frac{1}{2E}\bigl(\frac{1}{p^0 - E} - \frac{1}{p^0 + E}\bigr)$ (check: the numerator is $(p^0 + E) - (p^0 - E) = 2E$) display both residues at once.
>
> **What the derivation shows.**
> - Same function, two poles, two different numbers: the residue at $+E$ carries the positive-energy wave, the one at $-E$ the negative-frequency wave that becomes the reversed Wightman function ([[§C2.11 Green's Functions and Contours#^thm-c2-11-5|Theorem §C2.11.5]]).

^der-ca-4-4

*Uses:* [[§CA.4 Contour Integration#^def-ca-4-3|Def. §CA.4.3]], [[§CA.4 Contour Integration#^thm-ca-4-2|Theorem §CA.4.2]] (Taylor series of $(z - z_0)^kf$)

> [!theorem] Theorem §CA.4.5: Residue Theorem
> If $f$ is analytic on a closed contour $\Gamma$ and inside it except at finitely many isolated singularities $z_1, \dots, z_N$, then
>
> $$
> \oint_\Gamma f\,dz = \pm2\pi i\sum_{k=1}^N\operatorname*{Res}_{z_k}f ,
> $$
>
> with $+$ for counterclockwise and $-$ for clockwise traversal. Singularities outside $\Gamma$ contribute nothing.
>
> *Source: the user's PHY 513 notes, App. A §A.5 (Principle "The residue theorem")*

^thm-ca-4-5

> [!derivation]- Derivation
> **Step 1** (deform). By Cauchy's theorem ([[§CA.4 Contour Integration#^thm-ca-4-2|Theorem §CA.4.2]]) deform $\Gamma$, without changing the integral, into small circles around each $z_k$ joined to the outer path by pairs of segments traversed in opposite directions.
>
> **Step 2** (cancel). The two traversals of each segment cancel.
>
> **Step 3** (circles). On a counterclockwise circle around $z_k$ the integral is $2\pi i\operatorname{Res}_{z_k}f$ ([[§CA.4 Contour Integration#^def-ca-4-3|Def. §CA.4.3]]); reversing the orientation reverses the sign.
>
> **What the derivation shows.**
> - Singularities outside $\Gamma$ never enter; those on $\Gamma$ are excluded by hypothesis and need Theorem §CA.4.7.

^der-ca-4-5

*Uses:* [[§CA.4 Contour Integration#^thm-ca-4-2|Theorem §CA.4.2]], [[§CA.4 Contour Integration#^def-ca-4-3|Def. §CA.4.3]]

## Integrals along the real line

> [!theorem] Theorem §CA.4.6: Closing the Contour: the ML Estimate and Jordan's Lemma
> Let $C_R$ be the upper semicircle of radius $R$.
> 1. *(Algebraic decay)* If $|f| \le C/R^{1+\delta}$ on $C_R$ for some $\delta > 0$, then $\int_{C_R}f\,dz \to 0$.
> 2. *(Jordan)* If $\max_{C_R}|g| \to 0$, at any rate, and $\lambda > 0$, then $\int_{C_R}g(z)\,e^{i\lambda z}\,dz \to 0$. For $e^{-i\lambda z}$ use the lower semicircle.
>
> So a real-line integral may be closed where the integrand decays: $e^{ikz}$ upward for $k > 0$, downward for $k < 0$; $e^{-ip^0t}$ upward for $t < 0$, downward for $t > 0$.
>
> *Source: the user's PHY 513 notes, App. A §A.5 ("Integrals along the real line: closing the contour"), Ch. 5 §5.4*

^thm-ca-4-6

> [!derivation]- Derivation
> **Step 1** (algebraic decay). The semicircle has length $\pi R$, so by ML ([[§CA.4 Contour Integration#^thm-ca-4-1|Theorem §CA.4.1]]) the arc is at most $\pi R\cdot C/R^{1+\delta} = \pi C/R^\delta \to 0$. A rational function whose denominator has degree at least two more than its numerator qualifies.
>
> **Step 2** (Jordan: the exponential on the arc). On $z = Re^{i\theta}$, $0 \le \theta \le \pi$: $|e^{i\lambda z}| = |e^{i\lambda R\cos\theta}|\,e^{-\lambda R\sin\theta} = e^{-\lambda R\sin\theta}$ and $|dz| = R\,d\theta$.
>
> **Step 3** (Jordan: the estimate). By symmetry about $\theta = \pi/2$ and $\sin\theta \ge 2\theta/\pi$ on $[0, \pi/2]$ (concavity),
>
> $$
> \int_0^\pi e^{-\lambda R\sin\theta}R\,d\theta = 2\int_0^{\pi/2}e^{-\lambda R\sin\theta}R\,d\theta \le 2\int_0^{\pi/2}e^{-2\lambda R\theta/\pi}R\,d\theta = \frac{\pi}{\lambda}\bigl(1 - e^{-\lambda R}\bigr) < \frac\pi\lambda .
> $$
>
> So $\bigl|\int_{C_R}g\,e^{i\lambda z}dz\bigr| \le \frac\pi\lambda\max_{C_R}|g| \to 0$.
>
> **Step 4** (which side). $|e^{ikz}| = e^{-k\operatorname{Im}z}$ decays in the upper half-plane for $k > 0$; $|e^{-ip^0t}| = e^{t\operatorname{Im}p^0}$ decays in the upper half-plane for $t < 0$ and the lower for $t > 0$.
>
> **What the derivation shows.**
> - The sign of the time difference, causal order, decides the contour.
> - Jordan needs no rate of decay of $g$ but needs $g \to 0$; for the propagator integrand the faster ML estimate suffices ([[§C2.11 Green's Functions and Contours#^thm-c2-11-5|Theorem §C2.11.5]], Step 2).

^der-ca-4-6

*Uses:* [[§CA.4 Contour Integration#^thm-ca-4-1|Theorem §CA.4.1]]

> [!caution] Caution: Jordan's lemma needs $g \to 0$
> No rate of decay is required, but $g$ must tend to zero. For the equal-time Wightman integrand $p\,e^{ipr}/\sqrt{p^2 + m^2}$ the kernel tends to $1$ and the lemma fails; the cure there is to write $p\,e^{ipr} = -i\partial_re^{ipr}$ first ([[§C2.9 Explicit Forms of the Wightman Function#^thm-c2-9-3|Theorem §C2.9.3]], second route). Nor may a regulator such as $e^{-\varepsilon p}$ be kept on the arc: near $\arg p = \pi$ it grows like $e^{\varepsilon R}$.
>
> *Source: the user's PHY 513 notes, Ch. 5 §5.4*

^cau-ca-4-1

> [!example] Example §CA.4.1: Two Lorentzian Integrals
> For $a > 0$, evaluate $\int_{-\infty}^\infty\frac{dx}{x^2 + a^2}$ and $I(k) = \int_{-\infty}^{\infty}\frac{e^{ikx}\,dx}{x^2 + a^2}$.
>
> *No exponential.* The integrand decays like $1/R^2$, so close either way. Upward, the enclosed pole $ia$ has residue $1/2ia$ ([[§CA.4 Contour Integration#^thm-ca-4-4|Theorem §CA.4.4]]), and the integral is $2\pi i/2ia = \pi/a$: the elementary $\arctan$ result (substitute $x = a\tan u$). Closing downward, clockwise, round $-ia$ (residue $-1/2ia$) gives the same.
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

^ex-ca-4-1

## Poles on the path and branch cuts

> [!theorem] Theorem §CA.4.7: Poles on the Contour: the Half-Residue Lemma
> Let $f = g/(z - x_0)$ with $g$ analytic near a real $x_0$. A small semicircle passing *above* $x_0$ (clockwise) contributes $-i\pi g(x_0)$, one passing *below* (counterclockwise) $+i\pi g(x_0)$, so
>
> $$
> \int_{\text{above}}f = \mathcal P\!\!\int f - i\pi\operatorname*{Res}_{x_0}f, \qquad \int_{\text{below}}f = \mathcal P\!\!\int f + i\pi\operatorname*{Res}_{x_0}f .
> $$
>
> Passing above a pole is the same as moving it down by $i\varepsilon$; the principal value is the average of the two.
>
> *Source: the user's PHY 513 notes, App. A §A.5 (Derivation "The half-residue lemma")*

^thm-ca-4-7

> [!derivation]- Derivation
> **Step 1** (above). On $z = x_0 + re^{i\varphi}$ with $\varphi$ from $\pi$ to $0$ (above the pole, clockwise), $dz = ire^{i\varphi}d\varphi$ and
>
> $$
> \int f\,dz = \int_\pi^0\frac{g(x_0 + re^{i\varphi})}{re^{i\varphi}}\,ire^{i\varphi}\,d\varphi = i\int_\pi^0g(x_0 + re^{i\varphi})\,d\varphi \;\xrightarrow{r\to0}\; -i\pi\,g(x_0),
> $$
>
> by continuity of $g$.
>
> **Step 2** (below). $\varphi$ runs from $\pi$ to $2\pi$ (counterclockwise): the same computation gives $+i\pi g(x_0)$.
>
> **Step 3** (the straight pieces). Outside $|x - x_0| < r$ they tend, as $r \to 0$, to the principal value ([[§CA.2 Generalized Functions#^def-ca-2-6|Def. §CA.2.6]]).
>
> **Step 4** (moving the pole instead). The real axis with the pole at $x_0 - i\varepsilon$ can be deformed, by Cauchy's theorem, into a path that passes above $x_0$ without crossing the pole; as $\varepsilon \to 0$ this is the contour of Step 1.
>
> **What the derivation shows.**
> - The two passings differ by a full loop, $2\pi i\operatorname{Res}$; the principal value is their average.
> - As an identity of generalized functions this is the Sokhotski–Plemelj formula ([[§CA.2 Generalized Functions#^thm-ca-2-11|Theorem §CA.2.11]]).

^der-ca-4-7

*Uses:* [[§CA.2 Generalized Functions#^def-ca-2-6|Def. §CA.2.6]], [[§CA.4 Contour Integration#^thm-ca-4-2|Theorem §CA.4.2]]

> [!example] Example §CA.4.2: A Step Function from a Pole
> Show that $\displaystyle\lim_{\varepsilon\to0^+}\int_{-\infty}^{\infty}\frac{dx}{2\pi i}\,\frac{e^{ikx}}{x - i\varepsilon} = \theta(k)$.
>
> The pole sits at $i\varepsilon$, just above the axis. For $k > 0$ close upward (Jordan): the pole is enclosed counterclockwise, and the result is $e^{-k\varepsilon} \to 1$. For $k < 0$ close downward: nothing is enclosed, and the result is $0$. A single pole infinitesimally off the axis produces a step function, and the side it sits on decides which sign of $k$ survives. With $k$ a time, this is causality in its most compact form, the mechanism of the retarded Green's function ([[§C2.11 Green's Functions and Contours#^thm-c2-11-5|Theorem §C2.11.5]]).
>
> *Source: the user's PHY 513 notes, App. A §A.5 (worked example (iii))*

^ex-ca-4-2

> [!theorem] Theorem §CA.4.8: Integrals around a Branch Cut
> A branch point (for example $\pm im$ of $\sqrt{p^2 + m^2}$) is not an isolated singularity: going once round it changes the function, so it has no Laurent series and no residue. The function is made single-valued by a **cut** from the branch point; a contour may be deformed onto the cut, and the integral becomes the integral of the discontinuity across it. An integrable branch point ($|f| = O(\delta^{-1/2})$ on a circle of radius $\delta$) contributes nothing as $\delta \to 0$.
>
> *Source: the user's PHY 513 notes, App. A §A.5 ("Not every singularity is isolated"), Ch. 5 §5.4 (keyhole contour) · PS §2.4, Fig. 2.3*

^thm-ca-4-8

> [!derivation]- Derivation
> **Step 1** (a closed contour avoiding the cut). On the plane cut along, say, $[ia, i\infty)$, the function is analytic. Take the real line, the large arc, the two lips of the cut (one traversed downward, the other upward) and a small circle round the branch point; Cauchy's theorem ([[§CA.4 Contour Integration#^thm-ca-4-2|Theorem §CA.4.2]]) gives total zero.
>
> **Step 2** (the lips). They carry the two boundary values $f_\pm$ of the function and are traversed in opposite directions, so together they give $\pm\int(f_+ - f_-)$, the integral of the discontinuity.
>
> **Step 3** (the small circle). If $|f| = O(\delta^{-1/2})$ on the circle of radius $\delta$, its contribution is at most $2\pi\delta\cdot O(\delta^{-1/2}) = O(\delta^{1/2}) \to 0$ (ML, [[§CA.4 Contour Integration#^thm-ca-4-1|Theorem §CA.4.1]]).
>
> **What the derivation shows.**
> - The values on the lips depend on the choice of branch; the total does not.
> - Worked case: the equal-time Wightman function, where the two lips *add* ([[§C2.9 Explicit Forms of the Wightman Function#^thm-c2-9-3|Theorem §C2.9.3]], second route).

^der-ca-4-8

*Uses:* [[§CA.4 Contour Integration#^thm-ca-4-1|Theorem §CA.4.1]], [[§CA.4 Contour Integration#^thm-ca-4-2|Theorem §CA.4.2]]

![[ph-qft-ca-2-1.svg]]
*The complex $p$-plane for the position-space two-point integrals with phase $pr - t\sqrt{p^2 + m^2}$. $\sqrt{p^2 + m^2}$ has branch points at $\pm im$, with cuts to $\pm i\infty$. For $r > |t|$ the large arc contributes nothing, and the real-line integral equals the integral around the upper cut, down its left lip and up its right lip (Theorem §CA.4.8); the closed contour drawn runs the other way round the cut and sums to zero. The saddle point of [[§CA.5 Gaussian Integrals, Stationary Phase and Bessel Functions#^ex-ca-5-1|Example §CA.5.1]] lies on this cut. Adapted from the user's PHY 513 notes, Fig. 2.2.*

## The working rules

> [!theorem] Theorem §CA.4.9: Working Rules for Contour Integrals
> 1. *Orientation:* counterclockwise $+2\pi i\sum\operatorname{Res}$, clockwise $-2\pi i\sum\operatorname{Res}$; closing a real-line integral upward is counterclockwise, downward clockwise.
> 2. *Where to close:* where the integrand decays; $e^{ikz}$ upward for $k > 0$, $e^{-ip^0t}$ upward for $t < 0$ and downward for $t > 0$.
> 3. *When the arc vanishes:* decay faster than $1/R$ (ML), or decay to zero at any rate times an exponential in its good half-plane (Jordan). Check it: it can fail.
> 4. *Deformation:* free through regions of analyticity; pushing the contour across a pole changes the answer by $\pm2\pi i\operatorname{Res}$.
> 5. *Residues:* $g(z_0)/h'(z_0)$ at a simple zero of the denominator, or split the poles by partial fractions first.
> 6. *Poles on the path:* undefined until told how to pass each pole; above and below differ by $2\pi i\operatorname{Res}$; passing above = moving the pole down by $i\varepsilon$; the principal value is the average.
> 7. *Branch points are not poles:* they need cuts, and the integral round a cut is the integral of the discontinuity.
>
> *Source: the user's PHY 513 notes, App. A §A.5 (Principle "Working rules"), Ch. 6 §6.5 (Principle "Recall: working rules", the same list)*

^thm-ca-4-9

> [!derivation]- Derivation
> Each rule is one of the theorems above. **Rule 1:** [[§CA.4 Contour Integration#^thm-ca-4-5|Theorem §CA.4.5]]. **Rules 2–3:** [[§CA.4 Contour Integration#^thm-ca-4-6|Theorem §CA.4.6]]. **Rule 4:** [[§CA.4 Contour Integration#^thm-ca-4-2|Theorem §CA.4.2]], with the residue theorem applied to the loop between the two contours. **Rule 5:** [[§CA.4 Contour Integration#^thm-ca-4-4|Theorem §CA.4.4]]. **Rule 6:** [[§CA.4 Contour Integration#^thm-ca-4-7|Theorem §CA.4.7]] and [[§CA.2 Generalized Functions#^thm-ca-2-11|Theorem §CA.2.11]]. **Rule 7:** [[§CA.4 Contour Integration#^thm-ca-4-8|Theorem §CA.4.8]].
>
> **What the derivation shows.**
> - The procedure that strings these rules together for Green's functions is [[P2 Green's Functions by Contour Integration|P2]].

^der-ca-4-9

*Uses:* [[§CA.4 Contour Integration#^thm-ca-4-2|Theorem §CA.4.2]], [[§CA.4 Contour Integration#^thm-ca-4-4|Theorem §CA.4.4]], [[§CA.4 Contour Integration#^thm-ca-4-5|Theorem §CA.4.5]], [[§CA.4 Contour Integration#^thm-ca-4-6|Theorem §CA.4.6]], [[§CA.4 Contour Integration#^thm-ca-4-7|Theorem §CA.4.7]], [[§CA.4 Contour Integration#^thm-ca-4-8|Theorem §CA.4.8]], [[§CA.2 Generalized Functions#^thm-ca-2-11|Theorem §CA.2.11]]

> [!remark] Remark: "Move the contour up to infinity"
> The lecture's phrasing for closing a contour is the same argument as the semicircle: the real-axis integral equals the integral along the line $\operatorname{Im}p^0 = L$ plus two vertical segments at $\operatorname{Re}p^0 = \pm X$; the segments vanish as $X \to \infty$, and on the shifted line the integrand carries $e^{-L|t|}$, which kills it as $L \to \infty$. Both descriptions are correct; the closed contour is the one that generalizes, and the procedure built on it is [[P2 Green's Functions by Contour Integration|P2]].
>
> *Source: the user's PHY 513 notes, Ch. 6 §6.5 (Derivation "Closing the contour for the Green's function", "The lecture's version")*

^rem-ca-4-2

> [!remark]- Connections
> - Example §CA.4.1 is the one-dimensional cousin of the Yukawa potential ([[§B4.1 The Klein–Gordon Equation#^rem-b4-1-4|REL Remark: Static solutions and the Yukawa potential]]) and of the free scattering Green's function $-e^{ik\rho}/4\pi\rho$, whose $k'$-plane integral closes the two exponentials on opposite sides exactly as here ([[§C10.1 The Lippmann–Schwinger Equation and the Born Approximation#^thm-c10-1-3|QM Theorem §C10.1.3]]).
> - Example §CA.4.2 is the transform behind every causal response: the energy transform of a retarded propagator is analytic in the upper half-plane ([[§C4.1 Propagators#^thm-c4-1-7|QM Theorem §C4.1.7]]), the impulse response of a damped oscillator vanishes before the kick ([[§B4.4 Fourier Transforms and the Delta Function#^thm-b4-4-6|WO Theorem §B4.4.6]], whose transform $\chi(\omega)$ has its poles in one half-plane), and the retarded Green's function of the Klein–Gordon field passes above both poles ([[§C2.11 Green's Functions and Contours#^thm-c2-11-5|Theorem §C2.11.5]]).
> - The half-residue lemma is what QM uses for the imaginary part of the resolvent in the optical theorem ([[§C10.2 The Eikonal Approximation and the Optical Theorem|QM §C10.2]]); its distribution form is [[§CA.2 Generalized Functions#^thm-ca-2-11|Theorem §CA.2.11]].
> - The identity theorem makes analytic continuation unique; it is what turns one Euclidean evaluation into the Wightman function everywhere ([[§C2.9 Explicit Forms of the Wightman Function#^thm-c2-9-2|Theorem §C2.9.2]]) and what extends the Gaussian integral to complex variance ([[§C4.1 Propagators#^thm-c4-1-3|QM Theorem §C4.1.3]]).
> - Green's theorem in the plane ([[§16 Line Integrals and Green's Theorem#^thm-16-1|452 Thm. §16.1]]) is the whole proof of Cauchy's theorem for smooth $u$, $v$; Cauchy–Riemann says that $u\,dx - v\,dy$ and $v\,dx + u\,dy$ are closed forms.
> - Loop integrals (QFT C7, planned) bring branch cuts back, and the spinor and vector propagators (spinor: [[§C5.9 The Dirac Propagator and Spin–Statistics#^thm-c5-9-8|Theorem §C5.9.8]], Step 4; vector: [[§C4.8 Vector-Field Propagators#^thm-c4-8-3|Theorem §C4.8.3]], [[§C4.8 Vector-Field Propagators#^thm-c4-8-6|Theorem §C4.8.6]]) have numerators that are analytic in $p^0$, so the same residues give them the same $i\varepsilon$ (Yu eq. (6.262)).
> - **Used in** (C1 places): Def. §CA.4.2 — the single-particle amplitude as a boundary value ([[§C1.3 Causal Structure and the Causality of a Single Particle#^thm-c1-3-4|Theorem §C1.3.4]]); Theorems §CA.4.2, §CA.4.6, §CA.4.8 and Caution: Jordan's lemma needs g → 0 — the single-particle amplitude at spacelike separation ([[§C1.3 Causal Structure and the Causality of a Single Particle#^thm-c1-3-6|Theorem §C1.3.6]]).
> - **Used in** (C5 places): Theorems §CA.4.4–§CA.4.6 and Caution: Jordan's lemma needs g → 0 — the Dirac Feynman propagator, whose numerator $\slashed{p} + m$ makes the arc decay only like $1/\lvert p^0\rvert$, so that Jordan's lemma replaces the ML estimate ([[§C5.9 The Dirac Propagator and Spin–Statistics#^thm-c5-9-8|Theorem §C5.9.8]], Step 4).
