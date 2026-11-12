---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C6a
section: C6a.12
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C6a.11 Feynman Rules in Momentum Space]] · ↑ [[· C6a Interactions and Correlation Functions]] · [[§C6a.13 Exponentiation of the Vacuum Bubbles and the Vacuum Energy Density]] →

*Sources: the user's PHY 513 notes, Ch. 14 §14.7 (Derivation "Fine point 1: the $T \to \infty(1 - i\epsilon)$ limit is the Feynman prescription", Figure "tilt", paragraph "What the denominator is", Principle "Vacuum bubbles cancel", Derivation "The factorization at second order (filled in)", paragraph "Why the bubbles had to go", Caution "'Connected' means attached to an external point"), §14.8 (Principle "From the master formula to Feynman diagrams") · PHY 513 Lecture 14 (Larsen, 26 Oct 2026), Part C, slides 23–26, and transcript · Peskin & Schroeder, An Introduction to Quantum Field Theory, §4.4, pp. 95–99, eqs. (4.48)–(4.57) · Yu Zhao-Huan, 量子场论讲义, §10.4, eqs. (10.176)–(10.181); §10.5.1, eqs. (10.192)–(10.197), (10.209).*

The rules of [[§C6a.9 Position-Space Feynman Rules|§C6a.9]] and [[§C6a.11 Feynman Rules in Momentum Space|§C6a.11]] were derived for the numerator of the master formula ([[§C6a.5 The Interacting Vacuum and the Two-Point Function#^thm-c6a-5-6|Theorem §C6a.5.6]]) as if its time integrals ran over the real line and as if there were no denominator. What happened to the limit and to the denominator? These are the two fine points of Part C. The limit $T \to \infty(1 - i\varepsilon)$ tilts every vertex time slightly below the real axis; keeping the vertex integrals well defined forces every energy to be integrated slightly above it, which is the Feynman prescription already built into $D_F$. The denominator is the sum of the diagrams with no external points, the vacuum bubbles, each proportional to the volume of spacetime; the numerator factorizes into the diagrams attached to the external points times the same sum, so the bubbles cancel: the interacting correlator is the sum of the diagrams attached to the external points. What the cancelled bubbles are, the exponential of the connected ones and the energy density of the interacting vacuum, is [[§C6a.13 Exponentiation of the Vacuum Bubbles and the Vacuum Energy Density|§C6a.13]]. Yu has no $T(1 - i\varepsilon)$ limit: his correlation functions are built from asymptotic in-fields with a phase normalization $\mathcal N$ (eqs. (10.177)–(10.181)). His cancellation of the bubbles, eqs. (10.193)–(10.197), splits the contractions binomially, and that is the proof written here. **Setup** ([[§C6a.1 From Free to Interacting Fields#^mod-c6a-1-1|Model §C6a.1.1]], an instance of [[§C6a.0 Setups and Observables#^mod-c6a-0-3|Model §C6a.0.3]]): as in [[§C6a.8 Feynman Diagrams for Correlation Functions|§C6a.8]], the expansion in $\lambda$ of the numerator of the master formula ([[§C6a.5 The Interacting Vacuum and the Two-Point Function#^thm-c6a-5-6|Theorem §C6a.5.6]]), free-vacuum values $\langle0|T\{\cdots\}|0\rangle$; the correlator in $|\Omega\rangle$ is numerator over denominator ([[§C6a.12 The iε Limit and Vacuum Bubbles#^thm-c6a-12-5|Theorem §C6a.12.5]]); identities hold order by order, as formal power series.

*Conventions* ([[Larsen PHY 513]]): as in [[§C6a.9 Position-Space Feynman Rules|§C6a.9]]; numerator and denominator are formal power series in $\lambda$; $V$ is the volume of space and $2T$ the length of the time interval, both taken finite and then large (a box, [[§CA.3 Products of Distributions and Operator-Valued Distributions#^thm-ca-3-3|Theorem §CA.3.3]]); $E_0$ is the ground-state energy of $\hat H$ measured from $\hat H_0|0\rangle = 0$ ([[§C6a.5 The Interacting Vacuum and the Two-Point Function#^def-c6a-5-1|Def. §C6a.5.1]]; not the zero-point energy, [[§C6a.5 The Interacting Vacuum and the Two-Point Function#^cau-c6a-5-1|§C6a.5, Caution: Two E₀'s]]).

A delta function at zero momentum in a finite box is the volume, $(2\pi)^3\delta^3(\mathbf 0) \leftrightarrow V$ ([[§CA.3 Products of Distributions and Operator-Valued Distributions#^thm-ca-3-3|Theorem §CA.3.3]]). The splitting of a pairing into its attached and vacuum parts, and the factorization of sums over pairings it implies, are proved in [[§CA.9 Splitting Pairings and the Exponential Formula|§CA.9]] and linked in the derivations; these three and the other CA results used (the exponential formula, the $i\varepsilon$ limits, the Fourier rules) are listed at the end.

## Fine point 1: the limit

> [!theorem] Theorem §C6a.12.1: The T(1 − iε) Limit Is the Feynman Prescription
> In the master formula the time of each vertex runs along $z^0 = \tau(1 - i\varepsilon)$, $-T \le \tau \le T$.
> 1. With real energies the vertex integral $\int dz^0\,e^{iP^0z^0}$, $P^0$ the energy flowing into the vertex, grows like $e^{\varepsilon|P^0|T}$ at one end and has no limit as $T \to \infty$.
> 2. If every energy is integrated along the tilted line $p^0 = s/(1 - i\varepsilon) \simeq s(1 + i\varepsilon)$, $s$ real, then $p^0z^0 = s\tau$ is real and the vertex integrals give $(2\pi)^4\delta^4$ as before ([[§C6a.11 Feynman Rules in Momentum Space#^thm-c6a-11-1|Theorem §C6a.11.1]]).
> 3. On that line $p^2 - m^2 = s^2 - \mathbf p^2 - m^2 + 2i\varepsilon s^2 + O(\varepsilon^2)$: the $+i\varepsilon$ of the Feynman propagator. Equivalently, the tilted line passes above the pole at $+E_{\mathbf p}$ and below the pole at $-E_{\mathbf p}$: it is the Feynman contour ([[§C2b.7 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-7-2|Theorem §C2b.7.2]], [[§C2b.7 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-7-10|Theorem §C2b.7.10]]), rotated by an infinitesimal angle in the direction of the Wick rotation ([[§C2b.8 Wick Rotation and the Two-Point Family#^thm-c2b-8-1|Theorem §C2b.8.1]]).
>
> So the limit prescription of the master formula and the $i\varepsilon$ of $D_F$ are one and the same: "Impose Feynman boundary conditions on propagators ⇒ precisely what we do already."
>
> *Model:* [[§C6a.1 From Free to Interacting Fields#^mod-c6a-1-1|Model §C6a.1.1]]; *applies:* as in the opening.
>
> *Source: PHY 513 Lecture 14, slide 24 ("Fine Point: Limiting Procedure") · the user's PHY 513 notes, Ch. 14 §14.7 (Derivation "Fine point 1") · PS §4.4, p. 95 and figure*

^thm-c6a-12-1

> [!derivation]- Derivation
> **Step 1** (where the vertex time comes from). The vertex integral is not really $\int d^4z$: $\int d^3z$ comes from $\hat H_I = \int d^3z\,\hat{\mathcal H}_I$ and is harmless, while $\int dz^0$ comes from $\int_{-T}^Tdt\,\hat H_I(t)$ with $T \to \infty(1 - i\varepsilon)$ ([[§C6a.5 The Interacting Vacuum and the Two-Point Function#^thm-c6a-5-6|Theorem §C6a.5.6]]; slide 24: "$d^3z$ from $H_I$ (simple), $dz^0$ from $\int H_I\,dt$ (subtle)"). With $T$ replaced by $T(1 - i\varepsilon)$ the time variable runs along
>
> $$
> z^0 = \tau(1 - i\varepsilon), \qquad \tau \in [-T, T], \qquad dz^0 = (1 - i\varepsilon)\,d\tau .
> $$
>
> **Step 2** (the growth, part 1). For real $P^0$,
>
> $$
> e^{iP^0z^0} = e^{iP^0\tau}\,e^{\varepsilon P^0\tau}, \qquad |e^{iP^0z^0}| = e^{\varepsilon P^0\tau},
> $$
>
> growing as $\tau \to +\infty$ for $P^0 > 0$ and as $\tau \to -\infty$ for $P^0 < 0$. The integral is
>
> $$
> \int_{-T(1-i\varepsilon)}^{T(1-i\varepsilon)}dz^0\,e^{iP^0z^0} = \Bigl[\frac{e^{iP^0z^0}}{iP^0}\Bigr]_{z^0 = -T(1-i\varepsilon)}^{T(1-i\varepsilon)} = \frac{e^{iP^0T}e^{\varepsilon P^0T} - e^{-iP^0T}e^{-\varepsilon P^0T}}{iP^0} ,
> $$
>
> of size $e^{\varepsilon|P^0|T}/|P^0|$ for large $T$: it diverges as $T \to \infty$ instead of producing a delta function.
>
> **Step 3** (the compensating tilt, part 2). Integrate every energy along $p^0 = s/(1 - i\varepsilon)$, $s \in \mathbb R$ (slide 24: "$p^0 \to \frac{p^0}{1 - i\epsilon} \simeq p^0(1 + i\epsilon)$"), so $dp^0 = ds/(1 - i\varepsilon)$. Then
>
> $$
> p^0z^0 = \frac{s}{1 - i\varepsilon}\cdot\tau(1 - i\varepsilon) = s\tau ,
> $$
>
> exactly real. With $s_{\rm in} = \sum_js_j$ the energy into the vertex,
>
> $$
> \int dz^0\,e^{i\sum_jp_j^0z^0} = (1 - i\varepsilon)\int_{-T}^Td\tau\,e^{is_{\rm in}\tau} = (1 - i\varepsilon)\,\frac{2\sin(s_{\rm in}T)}{s_{\rm in}} \;\xrightarrow{T\to\infty}\; (1 - i\varepsilon)\,2\pi\,\delta(s_{\rm in})
> $$
>
> ([[§CA.4 Fourier Transforms and Fourier Tricks#^thm-ca-4-3|Theorem §CA.4.3]], as the limit of box integrals). Using this delta to do one energy integral, say $s_4$,
>
> $$
> \int\frac{dp_4^0}{2\pi}\,(1 - i\varepsilon)\,2\pi\,\delta(s_1 + \dots + s_4)\,g(s_4) = \int\frac{ds_4}{2\pi(1 - i\varepsilon)}\,(1 - i\varepsilon)\,2\pi\,\delta(s_1 + \dots + s_4)\,g(s_4) = g(-s_1 - s_2 - s_3) :
> $$
>
> the factor $(1 - i\varepsilon)$ cancels; the remaining energy integrals carry $\frac{1}{1 - i\varepsilon} \to 1$ as $\varepsilon \to 0^+$. The spatial integrals give $(2\pi)^3\delta^3$ unchanged.
>
> **Step 4** (the propagator on the tilted line, part 3).
>
> $$
> (p^0)^2 = \frac{s^2}{(1 - i\varepsilon)^2} = s^2\bigl(1 + 2i\varepsilon + O(\varepsilon^2)\bigr), \qquad p^2 - m^2 = s^2 - \mathbf p^2 - m^2 + 2i\varepsilon s^2 + O(\varepsilon^2) .
> $$
>
> The coefficient $2s^2$ of $i\varepsilon$ is positive, and only the sign of the infinitesimal near the mass shell matters ([[§CA.7 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-7-6|Theorem §CA.7.6]], 3): this is $p^2 - m^2 + i\varepsilon$.
>
> **Step 5** (as a contour). The tilted line is the real axis rotated counterclockwise by $\arg\frac{1}{1 - i\varepsilon} = \arctan\varepsilon$:
>
> $$
> p^0 = \frac{s}{1 - i\varepsilon} = \frac{s(1 + i\varepsilon)}{1 + \varepsilon^2}, \qquad \operatorname{Im}p^0 = \frac{\varepsilon s}{1 + \varepsilon^2} \;\begin{cases} > 0, & s > 0,\\ < 0, & s < 0 .\end{cases}
> $$
>
> At $s = E_{\mathbf p}$ it lies above the real axis, so it passes *above* the pole at $+E_{\mathbf p}$ (or at $E_{\mathbf p} - i\varepsilon$); at $s = -E_{\mathbf p}$ it passes *below* $-E_{\mathbf p}$ (or $-E_{\mathbf p} + i\varepsilon$). That is the Feynman contour $C_F$ ([[§C2b.7 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-7-2|Theorem §C2b.7.2]]). Rotating the real axis to the tilted line sweeps only the first and third quadrants, which contain no Feynman poles, so the two integrals agree (Cauchy, as for the Wick rotation, [[§C2b.8 Wick Rotation and the Two-Point Family#^thm-c2b-8-1|Theorem §C2b.8.1]], through an infinitesimal angle; in position space, [[§C2b.8 Wick Rotation and the Two-Point Family#^thm-c2b-8-3|Theorem §C2b.8.3]]: "the Feynman prescription is the infinitesimal Wick rotation $t \to t(1 - i\varepsilon)$").
>
> ⚑ By-product: the limit has content, but the content is consistency: projecting onto the vacuum at early and late times ([[§C6a.5 The Interacting Vacuum and the Two-Point Function#^thm-c6a-5-1|Theorem §C6a.5.1]]) and the time ordering inside $D_F$ are the same $i\varepsilon$ → [[§C6a.12 The iε Limit and Vacuum Bubbles#^rem-c6a-12-1|Remark: Why "precisely what we do already"]].
>
> **What the derivation shows.**
> - Time and energy are tilted in opposite directions so that $p^0z^0$ stays real; the energy tilt is the Feynman $i\varepsilon$.
> - The rules of §C6a.9 and §C6a.11 stand as stated, with $\tilde D_F = i/(p^2 - m^2 + i\varepsilon)$ and $\varepsilon \to 0^+$ at the end.

^der-c6a-12-1

*Uses:* [[§C6a.5 The Interacting Vacuum and the Two-Point Function#^thm-c6a-5-6|Theorem §C6a.5.6]], [[§CA.4 Fourier Transforms and Fourier Tricks#^thm-ca-4-3|Theorem §CA.4.3]], [[§CA.7 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-7-6|Theorem §CA.7.6]], [[§C2b.7 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-7-2|Theorem §C2b.7.2]], [[§C2b.8 Wick Rotation and the Two-Point Family#^thm-c2b-8-1|Theorem §C2b.8.1]], [[§C2b.8 Wick Rotation and the Two-Point Family#^thm-c2b-8-3|Theorem §C2b.8.3]]

![[ph-qft-c6-11-1.svg]]
*Fine point 1. (a) In the master formula every vertex time $z^0$ runs from $-T(1 - i\varepsilon)$ to $T(1 - i\varepsilon)$, tilted below the real axis. (b) To keep $p^0z^0$ real, every energy is integrated along a line tilted the other way, $p^0 = s(1 + i\varepsilon)$; it passes above the pole at $E_{\mathbf p} - i\varepsilon$ and below the one at $-E_{\mathbf p} + i\varepsilon$: the Feynman contour, rotated infinitesimally in the direction of the Wick rotation. Adapted from the user's PHY 513 notes, Figure "tilt"; PS p. 95.*

> [!remark] Remark: Why "precisely what we do already"
> Slide 24 ends: "This means: impose Feynman boundary conditions on propagators ⇒ precisely what we do already." The extra limit has content, but the content is consistency: the computation makes sense only if the Feynman prescription was what was meant, and it was already built in. The tilt $T(1 - i\varepsilon)$ was introduced to project $|0\rangle$ onto $|\Omega\rangle$ ([[§C6a.5 The Interacting Vacuum and the Two-Point Function#^thm-c6a-5-1|Theorem §C6a.5.1]]): a damping factor on long times. A damping factor on $t > 0$ puts a pole below the real axis ([[§CA.7 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-7-5|Theorem §CA.7.5]]),
>
> $$
> \int_0^\infty dt\,e^{i\omega t}e^{-\varepsilon t} = \frac{1}{\varepsilon - i\omega} = \frac{i}{\omega + i\varepsilon}, \qquad \text{pole at } \omega = -i\varepsilon ,
> $$
>
> which is how the positive-energy pole of $D_F$ is displaced. The vacuum projection of Lecture 13 and the Feynman prescription of Lecture 6 are one mechanism.
>
> *Source: PHY 513 Lecture 14, slide 24, and transcript · PS §4.4, p. 95 ("But this is precisely what we do in following the Feynman boundary conditions for computing $D_F$")*

^rem-c6a-12-1

## Fine point 2: the denominator and vacuum bubbles

> [!definition] Definition §C6a.12.1: Vacuum Bubble
> A **vacuum bubble** (vacuum diagram) is a diagram with no external points; in a larger diagram, a connected piece that contains no external point. Its value follows from the rules of [[§C6a.9 Position-Space Feynman Rules#^thm-c6a-9-4|Theorem §C6a.9.4]]: every point of it is a vertex, integrated over all of spacetime.
>
> *Model:* [[§C6a.1 From Free to Interacting Fields#^mod-c6a-1-1|Model §C6a.1.1]]; *applies:* as in the opening.
>
> *Source: PHY 513 Lecture 14, slide 25 ("Denominator = diagrams with no external lines = vacuum bubbles") · PS §4.4, pp. 96–99 ("disconnected pieces", "vacuum bubbles" or "vacuum to vacuum transitions") · Yu §10.5.1, after eq. (10.192) (气泡图)*

^def-c6a-12-1

> [!definition] Definition §C6a.12.2: Diagram Attached to the External Points
> A diagram with external points is **attached to the external points** if every connected piece of it contains at least one external point, i.e. it has no vacuum bubble ([[§C6a.12 The iε Limit and Vacuum Bubbles#^def-c6a-12-1|Def. §C6a.12.1]]). For the labelled diagrams this is [[§CA.9 Splitting Pairings and the Exponential Formula#^def-ca-9-1|Def. §CA.9.1]]. PS and the slides call these diagrams "connected" ([[§C6a.12 The iε Limit and Vacuum Bubbles#^cau-c6a-12-1|Caution: "Connected" means attached to an external point]]).
>
> *Model:* [[§C6a.1 From Free to Interacting Fields#^mod-c6a-1-1|Model §C6a.1.1]]; *applies:* as in the opening.
>
> *Source: PS §4.4, p. 98 ("By 'disconnected' we mean 'disconnected from all external points'") · PHY 513 Lecture 14, slide 25 ("diagrams connected to external lines") · the user's PHY 513 notes, Ch. 14 §14.7*

^def-c6a-12-2

> [!theorem] Theorem §C6a.12.2: The Denominator Is the Sum of the Vacuum Diagrams
> $$
> \langle0|T\Bigl\{\exp\Bigl[-i\int_{-T}^Tdt\,\hat H_I(t)\Bigr]\Bigr\}|0\rangle = 1 + \sum(\text{diagrams with no external points}) ,
> $$
>
> each diagram, connected or not, built by the rules of [[§C6a.9 Position-Space Feynman Rules#^thm-c6a-9-4|Theorem §C6a.9.4]] with its symmetry factor; the term 1 is the empty diagram (order $\lambda^0$).
>
> *Model:* [[§C6a.1 From Free to Interacting Fields#^mod-c6a-1-1|Model §C6a.1.1]]; *applies:* as in the opening; in $|0\rangle$.
>
> *Source: PHY 513 Lecture 14, slide 25 · the user's PHY 513 notes, Ch. 14 §14.7 (paragraph "What the denominator is") · PS §4.4, p. 98 · Yu §10.5.1, eq. (10.193)*

^thm-c6a-12-2

> [!derivation]- Derivation
> **Step 1** (no external points). Steps 1–8 of [[§C6a.9 Position-Space Feynman Rules#^der-c6a-9-1|Derivation §C6a.9.1]] used nothing about $n_{\rm ext}$; with $E = \varnothing$ they give
>
> $$
> \langle0|T\Bigl\{e^{-i\int_{-T}^Tdt\,\hat H_I}\Bigr\}|0\rangle = \sum_{n\ge0}\frac{1}{n!}\Bigl(\frac{-i\lambda}{4!}\Bigr)^n\int d^4z_1\cdots d^4z_n\,\langle0|T\{\hat\phi_I(z_1)^4\cdots\hat\phi_I(z_n)^4\}|0\rangle = \sum_{n\ge0}\;\sum_{D:\,E=\varnothing,\ n\text{ vertices}}\frac{(-i\lambda)^n}{S(D)}\int d^4z_1\cdots d^4z_n\prod_{\text{lines of }D}D_F ,
> $$
>
> the rules of [[§C6a.9 Position-Space Feynman Rules#^thm-c6a-9-4|Theorem §C6a.9.4]] with $n_{\rm ext} = 0$.
>
> **Step 2** (order zero). The $n = 0$ term of the time-ordered exponential is $\mathbf 1$, and $\langle0|\mathbf 1|0\rangle = \langle0|0\rangle = 1$: the empty diagram.
>
> **What the derivation shows.**
> - The denominator is computed by the same rules as the numerator; it is not a separate object.

^der-c6a-12-2

*Uses:* [[§C6a.9 Position-Space Feynman Rules#^thm-c6a-9-4|Theorem §C6a.9.4]], [[§C6a.9 Position-Space Feynman Rules#^der-c6a-9-1|Derivation §C6a.9.1]]

> [!example] Example §C6a.12.1: The Denominator Through Second Order
> ![[ph-qft-c6a-11-1.svg]]
>
> Write $D_{vw} = D_F(z_v - z_w)$, so $D_{vv} = D_F(0)$.
>
> **Step 1** (first order). Wick's theorem for the four factors of $\hat\phi_I(z_1)^4$: the $1 + 6$ terms with a normal-ordered remainder vanish in the vacuum and the $3!! = 3$ complete contractions survive ([[§C6a.8 Feynman Diagrams for Correlation Functions#^cau-c6a-8-3|§C6a.8, Caution: Numerator, not yet the interacting correlator]]):
>
> $$
> \langle0|T\{\hat\phi_{(1,1)}\hat\phi_{(1,2)}\hat\phi_{(1,3)}\hat\phi_{(1,4)}\}|0\rangle = \underbrace{D_{11}^2}_{\{(1,1), (1,2)\}\,\{(1,3), (1,4)\}} + \underbrace{D_{11}^2}_{\{(1,1), (1,3)\}\,\{(1,2), (1,4)\}} + \underbrace{D_{11}^2}_{\{(1,1), (1,4)\}\,\{(1,2), (1,3)\}} = 3\,D_{11}^2 ,
> $$
>
> $$
> \frac{-i\lambda}{4!}\int d^4z_1\,3\,D_{11}^2 = \frac{-i\lambda}{8}\int d^4z_1\,D_F(0)^2 = \frac18(\text{figure-eight}) .
> $$
>
> **Step 2** (second order). Wick's theorem for the eight fields has $1 + 28 + 210 + 420$ terms with a remainder, all zero in the vacuum, and $7!! = 105$ complete contractions ([[§C6a.10 Symmetry Factors in Practice#^ex-c6a-10-2|Example §C6a.10.2]], Steps 2–3), which are $24$ melons, $72$ dumbbells and $9$ pairs of figure-eights ([[§C6a.10 Symmetry Factors in Practice#^ex-c6a-10-3|Example §C6a.10.3]]):
>
> $$
> \langle0|T\{\hat\phi_I(z_1)^4\hat\phi_I(z_2)^4\}|0\rangle = 24\,D_{12}^4 + 72\,D_{11}D_{22}D_{12}^2 + 9\,D_{11}^2D_{22}^2 .
> $$
>
> With the prefactor $\frac{1}{2!}\bigl(\frac{-i\lambda}{4!}\bigr)^2 = \frac{(-i\lambda)^2}{1152}$,
>
> $$
> \frac{(-i\lambda)^2}{1152}\int d^4z_1\,d^4z_2\bigl[24\,D_{12}^4 + 72\,D_{11}D_{22}D_{12}^2 + 9\,D_{11}^2D_{22}^2\bigr] = (-i\lambda)^2\int d^4z_1\,d^4z_2\Bigl[\frac{1}{48}D_{12}^4 + \frac{1}{16}D_F(0)^2D_{12}^2 + \frac{1}{128}D_F(0)^4\Bigr] .
> $$
>
> **Step 3** (collect). With $-i\lambda\int d^4z$ at every vertex and the symmetry factors of [[§C6a.10 Symmetry Factors in Practice#^ex-c6a-10-1|Example §C6a.10.1]] and [[§C6a.10 Symmetry Factors in Practice#^ex-c6a-10-3|Example §C6a.10.3]],
>
> $$
> \langle0|T\{e^{-i\int\hat H_I}\}|0\rangle = 1 + \tfrac18\,(\text{figure-eight}) + \Bigl[\tfrac{1}{16}\,(\text{dumbbell}) + \tfrac{1}{48}\,(\text{melon}) + \tfrac{1}{128}\,(\text{two figure-eights})\Bigr] + O(\lambda^3) .
> $$
>
> Slide 25 writes the series as "1 + (figure-eight) + ⋯", with the factors understood. Where a bubble sits is not fixed: its vertex positions are integrated over all of spacetime.
>
> *Source: the user's PHY 513 notes, Ch. 14 §14.7 (paragraph "What the denominator is") · PHY 513 Lecture 14, slide 25, and transcript · coefficients checked by enumeration (3 of 24; 72, 24, 9 of 1152)*

^ex-c6a-12-1

> [!theorem] Theorem §C6a.12.3: Every Vacuum Bubble Is Proportional to the Volume of Spacetime
> For a connected vacuum diagram $B$ with vertices $z_1, \dots, z_n$, in a box of volume $V$ and time interval $[-T, T]$,
>
> $$
> B = (2T\cdot V)\;b_B ,
> $$
>
> where $b_B$ is the value with one vertex held at the origin, independent of $T$ and $V$ up to effects of the boundary. In momentum space the factor is $(2\pi)^4\delta^{(4)}(0) = 2T\cdot V$, the delta of the last vertex, where conservation is automatic.
>
> *Model:* [[§C6a.1 From Free to Interacting Fields#^mod-c6a-1-1|Model §C6a.1.1]]; *applies:* as in the opening; finite $V$ and $2T$.
>
> *Source: PS §4.4, eqs. (4.48)–(4.49), p. 96 ("Every disconnected piece of a diagram … will have one such $(2\pi)^4\delta^{(4)}(0) = 2T\cdot V$ factor") · the user's PHY 513 notes, Ch. 14 §14.7 ("Each one is in fact proportional to the total spacetime volume") · PHY 513 Lecture 14, transcript*

^thm-c6a-12-3

> [!derivation]- Derivation
> **Step 1** (translation invariance). The value of $B$ is
>
> $$
> B = \frac{(-i\lambda)^n}{S}\int d^4z_1\cdots d^4z_n\,F(z_1, \dots, z_n), \qquad F = \prod_{\text{lines}}D_F(z_i - z_j),
> $$
>
> and $F(z_1 + c, \dots, z_n + c) = F(z_1, \dots, z_n)$ for every $c$: each factor depends only on a difference.
>
> **Step 2** (change variables). Put $w_1 = z_1$, $w_v = z_v - z_1$ for $v = 2, \dots, n$. The map is linear with block-triangular matrix (identity blocks on the diagonal), so its Jacobian is $1$ ([[§CA.4 Fourier Transforms and Fourier Tricks#^thm-ca-4-6|Theorem §CA.4.6]], 2, shift), and with $w_1 \equiv 0$ in the differences,
>
> $$
> F(z_1, \dots, z_n) = F(0, w_2, \dots, w_n), \qquad z_i - z_j = w_i - w_j .
> $$
>
> **Step 3** (the $z_1$-integral).
>
> $$
> B = \frac{(-i\lambda)^n}{S}\int d^4z_1\int d^4w_2\cdots d^4w_n\,F(0, w_2, \dots, w_n) = (2T\cdot V)\;b_B, \qquad b_B = \frac{(-i\lambda)^n}{S}\int d^4w_2\cdots d^4w_n\,F(0, w_2, \dots, w_n),
> $$
>
> with $\int d^4z_1 = 2T\cdot V$, the volume of the spacetime box ($b_B$ formal where it contains $D_F(0)$). Replacing the $w$-region (the box shifted by $-z_1$) by a fixed large region changes $B$ only by terms from $z_1$ near the boundary, negligible against $2T\cdot V$. Examples: the figure-eight, $n = 1$, has nothing to change, $-\frac{i\lambda}{8}\int d^4z\,D_F(0)^2 = 2TV\cdot\bigl(-\frac{i\lambda}{8}D_F(0)^2\bigr)$; the melon gives $\frac{(-i\lambda)^2}{48}\int d^4z_1\,d^4z_2\,D_F(z_1 - z_2)^4 = 2TV\cdot\frac{(-i\lambda)^2}{48}\int d^4w\,D_F(-w)^4$.
>
> **Step 4** (momentum space). By [[§C6a.11 Feynman Rules in Momentum Space#^thm-c6a-11-2|Theorem §C6a.11.2]] the deltas of $n - 1$ vertices fix all but the loop momenta; the delta of the last vertex then has argument zero, and
>
> $$
> (2\pi)^4\delta^4(0) = \int d^4z\,e^{i0\cdot z} = 2T\cdot V
> $$
>
> in the box ([[§CA.3 Products of Distributions and Operator-Valued Distributions#^thm-ca-3-3|Theorem §CA.3.3]] for the spatial part; for the time part $2\pi\delta(0) = \int_{-T}^Tdt = 2T$, i.e. $\delta(0) = 2T/2\pi$). For the melon, with momenta $k_1, \dots, k_4$ from $z_1$ to $z_2$:
>
> $$
> \int d^4z_1\,e^{-i(k_1 + \dots + k_4)\cdot z_1}\int d^4z_2\,e^{+i(k_1 + \dots + k_4)\cdot z_2} = (2\pi)^4\delta^4(k_1 + \dots + k_4)\;(2\pi)^4\delta^4(k_1 + \dots + k_4) ;
> $$
>
> doing the $k_4$-integral with the first delta sets $k_4 = -k_1 - k_2 - k_3$ and turns the second into $(2\pi)^4\delta^4(0) = 2T\cdot V$.
>
> ⚑ By-product: a vacuum bubble is infinite, proportional to the spacetime volume, like the zero-point energy is proportional to the volume of space ([[§C2b.7 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-7-8|Theorem §C2b.7.8]]); its density $b_B$ is the physical quantity → [[§C6a.12 The iε Limit and Vacuum Bubbles#^ex-c6a-12-2|Example §C6a.12.2]].
>
> **What the derivation shows.**
> - "This just tells us that the spacetime process can happen at any place in space, and at any time between $-T$ and $T$" (PS p. 96).

^der-c6a-12-3

*Uses:* [[§CA.4 Fourier Transforms and Fourier Tricks#^thm-ca-4-6|Theorem §CA.4.6]], [[§C6a.11 Feynman Rules in Momentum Space#^thm-c6a-11-2|Theorem §C6a.11.2]], [[§CA.3 Products of Distributions and Operator-Valued Distributions#^thm-ca-3-3|Theorem §CA.3.3]]

> [!example] Example §C6a.12.2: The Figure-Eight Is the First-Order Vacuum Energy
> ![[ph-qft-c6a-11-2.svg]]
>
> At first order the denominator is ([[§C6a.12 The iε Limit and Vacuum Bubbles#^ex-c6a-12-1|Example §C6a.12.1]], [[§C6a.12 The iε Limit and Vacuum Bubbles#^thm-c6a-12-3|Theorem §C6a.12.3]])
>
> $$
> 1 + \tfrac18(\text{figure-eight}) = 1 - \frac{i\lambda}{8}\int d^4z\,D_F(0)^2 = 1 - \frac{i\lambda}{8}D_F(0)^2\cdot2T\cdot V .
> $$
>
> The denominator is also $\langle0|U(T, -T)|0\rangle \to e^{-2iE_0T}|\langle0|\Omega\rangle|^2$ ([[§C6a.5 The Interacting Vacuum and the Two-Point Function#^thm-c6a-5-4|Theorem §C6a.5.4]]).
>
> **Step 1** (expand the right side). $E_0 = \lambda E_0^{(1)} + O(\lambda^2)$ vanishes with $\lambda$ ([[§C6a.5 The Interacting Vacuum and the Two-Point Function#^ex-c6a-5-1|Example §C6a.5.1]]). The first-order correction to the ground state is orthogonal to $|0\rangle$ ([[§B8.1 Nondegenerate Perturbation Theory#^thm-b8-1-2|QM Theorem §B8.1.2]]): with $|\Omega\rangle = \bigl(|0\rangle + \lambda|\psi^{(1)}\rangle + O(\lambda^2)\bigr)/\mathcal Z^{1/2}$, $\langle0|\psi^{(1)}\rangle = 0$ and $\mathcal Z = 1 + O(\lambda^2)$,
>
> $$
> |\langle0|\Omega\rangle|^2 = \frac{|1 + O(\lambda^2)|^2}{\mathcal Z} = 1 + O(\lambda^2), \qquad e^{-2iE_0T} = 1 - 2i\,\lambda E_0^{(1)}\,T + O(\lambda^2),
> $$
>
> $$
> e^{-2iE_0T}|\langle0|\Omega\rangle|^2 = 1 - 2i\,\lambda E_0^{(1)}\,T + O(\lambda^2) .
> $$
>
> **Step 2** (compare the coefficients of $\lambda T$).
>
> $$
> -2i\,\lambda E_0^{(1)}\,T = -\frac{i\lambda}{8}D_F(0)^2\cdot2T\cdot V \quad\Longrightarrow\quad \lambda E_0^{(1)} = \frac{\lambda}{8}\,D_F(0)^2\,V .
> $$
>
> **Step 3** (the same from quantum mechanics). First-order perturbation theory gives $\langle0|\hat H_{\rm int}|0\rangle$ ([[§B8.1 Nondegenerate Perturbation Theory#^thm-b8-1-1|QM Theorem §B8.1.1]]), with $\hat H_{\rm int} = \int d^3x\,\frac{\lambda}{4!}\hat\phi(\mathbf x)^4$ at one time. For the plain product of four fields Wick's theorem holds with $D_W$ in place of $D_F$ ([[§C6a.7 Wick's Theorem#^thm-c6a-7-4|★ Theorem §C6a.7.4]]):
>
> $$
> \hat\phi_1\hat\phi_2\hat\phi_3\hat\phi_4 = \,:\!\hat\phi_1\hat\phi_2\hat\phi_3\hat\phi_4\!: + \sum_{i<j}D_W(x_i - x_j):\!\hat\phi_k\hat\phi_l\!: + D_W(x_1 - x_2)D_W(x_3 - x_4) + D_W(x_1 - x_3)D_W(x_2 - x_4) + D_W(x_1 - x_4)D_W(x_2 - x_3) ;
> $$
>
> the normal-ordered terms vanish in the vacuum, and at coincident points each of the three products is $D_W(0)^2$:
>
> $$
> \langle0|\hat H_{\rm int}|0\rangle = \int d^3x\,\frac{\lambda}{4!}\cdot3\,D_W(0)^2 = \frac{\lambda}{8}\,D_W(0)^2\,V .
> $$
>
> $D_W(0)$ and $D_F(0)$ are the same formal quantity, $\langle0|\hat\phi(x)^2|0\rangle$.
>
> Both are infinite twice over, through $V$ and through $D_F(0)$ ([[§C6a.11 Feynman Rules in Momentum Space#^thm-c6a-11-3|Theorem §C6a.11.3]]); the computation shows what the bubbles are: the energy of the interacting vacuum relative to $|0\rangle$, the quantity the denominator was introduced to divide out.
>
> The term $\frac18(\text{figure-eight}) = V_1$ is the start of $e^{V_1}$; to all orders the denominator is $\exp(\sum_iV_i)$ and $E_0/V = i\sum_ib_{V_i}$ ([[§C6a.13 Exponentiation of the Vacuum Bubbles and the Vacuum Energy Density#^thm-c6a-13-1|Theorem §C6a.13.1]], [[§C6a.13 Exponentiation of the Vacuum Bubbles and the Vacuum Energy Density#^thm-c6a-13-2|Theorem §C6a.13.2]]).
>
> *Source: written here, from [[§C6a.5 The Interacting Vacuum and the Two-Point Function#^thm-c6a-5-4|Theorem §C6a.5.4]] and PS §4.4, eq. (4.49) · the identification at all orders, PS eqs. (4.55)–(4.56), is Theorem §C6a.13.2*

^ex-c6a-12-2

> [!theorem] Theorem §C6a.12.4: The Numerator Factorizes
> As formal power series in $\lambda$,
>
> $$
> \langle0|T\Bigl\{\hat\phi_I(x_1)\cdots\hat\phi_I(x_{n_{\rm ext}})\,e^{-i\int_{-T}^Tdt\,\hat H_I}\Bigr\}|0\rangle = \Bigl(\sum\text{diagrams attached to } x_1, \dots, x_{n_{\rm ext}}\Bigr)\times\langle0|T\Bigl\{e^{-i\int_{-T}^Tdt\,\hat H_I}\Bigr\}|0\rangle ,
> $$
>
> the first factor the sum, by the rules of [[§C6a.9 Position-Space Feynman Rules#^thm-c6a-9-4|Theorem §C6a.9.4]], of the diagrams attached to the external points ([[§C6a.12 The iε Limit and Vacuum Bubbles#^def-c6a-12-2|Def. §C6a.12.2]]), the second the sum of the vacuum diagrams ([[§C6a.12 The iε Limit and Vacuum Bubbles#^thm-c6a-12-2|Theorem §C6a.12.2]]).
>
> *Model:* [[§C6a.1 From Free to Interacting Fields#^mod-c6a-1-1|Model §C6a.1.1]]; *applies:* as in the opening.
>
> *Source: PHY 513 Lecture 14, slide 25 ("$\frac{\text{numerator}}{\text{denominator}} = \frac{(\text{diagrams connected to ext. lines})\times(\text{vacuum bubbles})}{\text{vacuum bubbles}}$") · the user's PHY 513 notes, Ch. 14 §14.7 (Principle "Vacuum bubbles cancel") · Yu §10.5.1, eqs. (10.194)–(10.196) (the proof followed here) · PS §4.4, pp. 96–98*

^thm-c6a-12-4

> [!derivation]- Derivation
> **Step 1** (the numerator as a sum over pairings). By Steps 1–4 of [[§C6a.9 Position-Space Feynman Rules#^der-c6a-9-1|Derivation §C6a.9.1]] (Wick's theorem; every term with a normal-ordered remainder vanishes in the vacuum), with $t = -\frac{i\lambda}{4!}$ and $E = \{x_1, \dots, x_{n_{\rm ext}}\}$,
>
> $$
> \mathcal N_E = \sum_{k\ge0}\frac{t^k}{k!}\sum_{P\in\mathcal P(X_{E,k})}f_k(P), \qquad f_k(P) = \int d^4z_1\cdots d^4z_k\,w(P), \qquad w(P) = \prod_{\{h,h'\}\in P}D_F\bigl(\mathrm{pt}(h) - \mathrm{pt}(h')\bigr) .
> $$
>
> **Step 2** (the integrand splits). Split $P = P_{\rm att}\sqcup P_{\rm vac}$ with $A = A(P)$ ([[§CA.9 Splitting Pairings and the Exponential Formula#^thm-ca-9-1|Theorem §CA.9.1]]). No block joins a vertex of $A$ to a vertex outside $A$ or to an external point, so
>
> $$
> w(P) = \underbrace{\prod_{\{h,h'\}\in P_{\rm att}}D_F}_{w(P_{\rm att}):\ z_v,\ v\notin A}\;\cdot\;\underbrace{\prod_{\{h,h'\}\in P_{\rm vac}}D_F}_{w(P_{\rm vac}):\ z_v,\ v\in A} .
> $$
>
> **Step 3** (the integrals separate). By Fubini (formally: the integrals are those of the regularized theory),
>
> $$
> f_k(P) = \int\prod_{v\notin A}d^4z_v\,w(P_{\rm att})\;\cdot\;\int\prod_{v\in A}d^4z_v\,w(P_{\rm vac}) = a_{k-j}(\rho_AP_{\rm att})\;b_j(\rho'_AP_{\rm vac}), \qquad j = |A|,
> $$
>
> after renaming the integration variables order-preservingly ($z_v \to z_{\rho_A(v)}$, unit Jacobian, [[§CA.4 Fourier Transforms and Fourier Tricks#^thm-ca-4-6|Theorem §CA.4.6]]), where
>
> $$
> a_i(Q) = \int\prod_{v=1}^id^4z_v\,w(Q)\quad (Q\in\mathcal P_{\rm att}(X_{E,i})), \qquad b_j(R) = \int\prod_{v=1}^jd^4z_v\,w(R)\quad (R\in\mathcal P(X_{\varnothing,j})) .
> $$
>
> This is the hypothesis of [[§CA.9 Splitting Pairings and the Exponential Formula#^thm-ca-9-2|Theorem §CA.9.2]].
>
> **Step 4** (factorize). [[§CA.9 Splitting Pairings and the Exponential Formula#^thm-ca-9-2|Theorem §CA.9.2]] gives
>
> $$
> \mathcal N_E = \Bigl(\sum_{i\ge0}\frac{t^i}{i!}\sum_{Q\in\mathcal P_{\rm att}(X_{E,i})}a_i(Q)\Bigr)\Bigl(\sum_{j\ge0}\frac{t^j}{j!}\sum_{R\in\mathcal P(X_{\varnothing,j})}b_j(R)\Bigr) .
> $$
>
> Yu's words for the step: of the $k$ interaction vertices, $j$ are placed in the vacuum part in $C_k^j = \frac{k!}{j!(k-j)!}$ ways, and the $\frac{1}{k!}$ becomes $\frac{1}{(k-j)!}\frac{1}{j!}$ (eqs. (10.194)–(10.195)).
>
> **Step 5** (identify the factors). The second factor is Step 1 with $E = \varnothing$, the denominator $\mathcal N_\varnothing$ ([[§C6a.12 The iε Limit and Vacuum Bubbles#^thm-c6a-12-2|Theorem §C6a.12.2]]; Yu eq. (10.196)). In the first, attachment is a property of the drawing ([[§CA.8 Pairings, Diagrams and Symmetry Factors#^thm-ca-8-8|Theorem §CA.8.8]]), so the attached pairings are a union of orbits, and Steps 5–8 of [[§C6a.9 Position-Space Feynman Rules#^der-c6a-9-1|Derivation §C6a.9.1]] turn $\frac{t^i}{i!}\sum_Qa_i(Q)$ into the sum of the attached diagrams with $i$ vertices, each with $(-i\lambda)^i/S$.
>
> **Step 6** (check at first order, $E = \{x, y\}$). The 15 pairings of [[§C6a.8 Feynman Diagrams for Correlation Functions#^der-c6a-8-1|Derivation §C6a.8.1]], Step 4, split by $A$:
> - $A = \varnothing$: the 12 of class (b), $\{x, z_a\}\,\{y, z_b\}\,\{z_c, z_d\}$, attached, $f_1 = a_1 = \int d^4z\,D_F(x - z)D_F(y - z)D_F(0)$;
> - $A = \{1\}$: the 3 of class (a), $P_{\rm att} = \{\{x, y\}\}$ and $P_{\rm vac}$ one of the three pairings of the legs, $f_1 = a_0\,b_1 = D_F(x - y)\cdot\int d^4z\,D_F(0)^2$.
>
> With $\alpha_0 = D_F(x - y)$, $\alpha_1 = 12\,a_1$, $\beta_0 = 1$, $\beta_1 = 3\,b_1$,
>
> $$
> t\bigl[12\,a_1 + 3\,D_F(x - y)\,b_1\bigr] = t\,(\alpha_1\beta_0 + \alpha_0\beta_1) = \bigl[(\alpha_0 + t\alpha_1)(\beta_0 + t\beta_1)\bigr]_{t^1} .
> $$
>
> **What the derivation shows.**
> - The factorization needs no knowledge of the bubbles themselves: only that a contraction splits uniquely and that the integrand does not care which vertices are called what.
> - At second order the cross term "tadpole times figure-eight" has the binomial factor $C_2^1 = 2$, the two ways of deciding which vertex carries which piece, which cancels the $\frac{1}{2!}$ of the second order ([[§C6a.12 The iε Limit and Vacuum Bubbles#^ex-c6a-12-3|Example §C6a.12.3]]).

^der-c6a-12-4

> [!derivation]- Derivation (second route: PS's exponentiation of the disconnected pieces)
> **Step 1** (a typical diagram, PS (4.50)–(4.51)). A diagram of the numerator is one piece attached to the external points times vacuum pieces; label the connected vacuum diagrams $V_1, V_2, \dots$ (figure-eight, dumbbell, melon, …) and write $V_i$ also for the value of $V_i$ with its own $\frac{1}{S(V_i)}$. If a diagram has $n_i$ copies of $V_i$, its symmetry factor is $S(\text{attached piece})\prod_in_i!\,S(V_i)^{n_i}$ ([[§CA.9 Splitting Pairings and the Exponential Formula#^thm-ca-9-2|Theorem §CA.9.2]] for the split, [[§CA.9 Splitting Pairings and the Exponential Formula#^thm-ca-9-3|Theorem §CA.9.3]], 2, for the vacuum part), and its value is
>
> $$
> (\text{value of attached piece})\cdot\prod_i\frac{1}{n_i!}(V_i)^{n_i} :
> $$
>
> "The $1/n_i!$ is the symmetry factor coming from interchanging the $n_i$ copies of $V_i$" (PS p. 96).
>
> **Step 2** (sum, PS (4.52)). Summing over all attached pieces and all $\{n_i\}$ (finitely many nonzero),
>
> $$
> \sum_{\text{attached}}\;\sum_{\{n_i\}}(\text{value})\prod_i\frac{V_i^{n_i}}{n_i!} = \Bigl(\sum\text{attached}\Bigr)\times\prod_i\Bigl(\sum_{n_i\ge0}\frac{V_i^{n_i}}{n_i!}\Bigr) = \Bigl(\sum\text{attached}\Bigr)\times\exp\Bigl(\sum_iV_i\Bigr) ,
> $$
>
> an identity of formal power series in $\lambda$ (each $V_i$ is $O(\lambda)$, so each order receives finitely many terms).
>
> **Step 3** (the denominator, PS p. 98). With no external points the attached piece is empty (value 1), and Step 2 reads $\langle0|T\{e^{-i\int\hat H_I}\}|0\rangle = \exp(\sum_iV_i)$ ([[§C6a.13 Exponentiation of the Vacuum Bubbles and the Vacuum Energy Density#^thm-c6a-13-1|Theorem §C6a.13.1]]). Dividing Step 2 by it gives [[§C6a.12 The iε Limit and Vacuum Bubbles#^thm-c6a-12-4|Theorem §C6a.12.4]] and [[§C6a.12 The iε Limit and Vacuum Bubbles#^thm-c6a-12-5|Theorem §C6a.12.5]].
>
> **Step 4** (check at second order, $E = \{x, y\}$). The terms of order $\lambda^2$ of $(D_F(x - y) + C_1 + C_2)(1 + V_1 + V_2^{\rm conn} + \frac12V_1^2)$, with $V_2^{\rm conn} = \frac1{16}(\text{dumbbell}) + \frac1{48}(\text{melon})$, are $C_2 + C_1V_1 + D_F(x - y)\bigl(V_2^{\rm conn} + \frac12V_1^2\bigr)$, and $\frac12\bigl(\frac18\bigr)^2 = \frac1{128}$ is the coefficient of two figure-eights ([[§C6a.12 The iε Limit and Vacuum Bubbles#^ex-c6a-12-3|Example §C6a.12.3]]).
>
> **What the derivation shows.**
> - The bubbles do not merely factor out, they exponentiate; the binomial route of the first derivation never needs this, PS's route needs the exponential formula.

^der-c6a-12-4b

*Uses:* [[§C6a.9 Position-Space Feynman Rules#^der-c6a-9-1|Derivation §C6a.9.1]], [[§CA.9 Splitting Pairings and the Exponential Formula#^thm-ca-9-1|Theorem §CA.9.1]], [[§CA.9 Splitting Pairings and the Exponential Formula#^thm-ca-9-2|Theorem §CA.9.2]], [[§CA.9 Splitting Pairings and the Exponential Formula#^thm-ca-9-3|Theorem §CA.9.3]], [[§CA.4 Fourier Transforms and Fourier Tricks#^thm-ca-4-6|Theorem §CA.4.6]], [[§CA.8 Pairings, Diagrams and Symmetry Factors#^thm-ca-8-8|Theorem §CA.8.8]], [[§C6a.12 The iε Limit and Vacuum Bubbles#^thm-c6a-12-2|Theorem §C6a.12.2]]

![[ph-qft-ca-7-6.svg]]
*The split of [[§CA.9 Splitting Pairings and the Exponential Formula#^thm-ca-9-1|Theorem §CA.9.1]]. The vertex $z_2$ has no path to an external point ([[§CA.9 Splitting Pairings and the Exponential Formula#^def-ca-9-1|Def. §CA.9.1]]), so $A(P) = \{2\}$; no block joins it to the rest, and $P$ is the disjoint union of an attached pairing and a vacuum pairing. In the numerator, this is the factorization into attached diagrams times vacuum bubbles (Theorem §C6a.12.4).*

> [!theorem] Theorem §C6a.12.5: Vacuum Bubbles Cancel
> In $\phi^4$ theory, to every order in $\lambda$,
>
> $$
> \langle\Omega|T\{\hat\phi_H(x_1)\cdots\hat\phi_H(x_{n_{\rm ext}})\}|\Omega\rangle = \sum\bigl(\text{diagrams attached to } x_1, \dots, x_{n_{\rm ext}}\bigr) ,
> $$
>
> by the rules of [[§C6a.9 Position-Space Feynman Rules#^thm-c6a-9-4|Theorem §C6a.9.4]] (or [[§C6a.11 Feynman Rules in Momentum Space#^thm-c6a-11-2|Theorem §C6a.11.2]]): only the diagrams in which every piece is attached to an external point are drawn. "Simplify: only draw diagrams connected to external lines."
>
> *Model:* [[§C6a.1 From Free to Interacting Fields#^mod-c6a-1-1|Model §C6a.1.1]]; *applies:* as in the opening; the result is the correlator in $|\Omega\rangle$.
>
> *Source: PHY 513 Lecture 14, slide 25 · the user's PHY 513 notes, Ch. 14 §14.7 (Principle "Vacuum bubbles cancel", eq. (nobubbles)) · PS §4.4, eqs. (4.54), (4.57) · Yu §10.5.1, box before eq. (10.194) and eq. (10.197)*

^thm-c6a-12-5

> [!derivation]- Derivation
> **Step 1** (the master formula). By [[§C6a.5 The Interacting Vacuum and the Two-Point Function#^thm-c6a-5-7|Theorem §C6a.5.7]], with the limit understood as in [[§C6a.12 The iε Limit and Vacuum Bubbles#^thm-c6a-12-1|Theorem §C6a.12.1]],
>
> $$
> \langle\Omega|T\{\hat\phi_H(x_1)\cdots\hat\phi_H(x_{n_{\rm ext}})\}|\Omega\rangle = \lim\frac{\mathcal N_E}{\mathcal N_\varnothing} .
> $$
>
> **Step 2** (divide). By [[§C6a.12 The iε Limit and Vacuum Bubbles#^thm-c6a-12-4|Theorem §C6a.12.4]], $\mathcal N_E = C_E\,\mathcal N_\varnothing$ with $C_E$ the sum of the attached diagrams. The denominator has constant term 1 ([[§C6a.12 The iε Limit and Vacuum Bubbles#^thm-c6a-12-2|Theorem §C6a.12.2]]), $\mathcal N_\varnothing = 1 + u$ with $u = O(\lambda)$, so it is invertible as a formal power series, $\mathcal N_\varnothing^{-1} = \sum_{k\ge0}(-u)^k$, and
>
> $$
> \frac{\mathcal N_E}{\mathcal N_\varnothing} = C_E\,\mathcal N_\varnothing\,\mathcal N_\varnothing^{-1} = C_E = \sum\bigl(\text{diagrams attached to } x_1, \dots, x_{n_{\rm ext}}\bigr) .
> $$
>
> ⚑ By-product: every vacuum bubble contains $2T\cdot V$ ([[§C6a.12 The iε Limit and Vacuum Bubbles#^thm-c6a-12-3|Theorem §C6a.12.3]]); the attached diagrams contain no such factor (each vertex is tied by propagators to fixed points). The infinities of numerator and denominator cancel exactly.
>
> **What the derivation shows.**
> - The denominator of the master formula has a single job: to remove the vacuum bubbles.
> - What remains is finite in $T$ and $V$; its ultraviolet divergences ($D_F(0)$ and loops) are a separate matter.

^der-c6a-12-5

*Uses:* [[§C6a.5 The Interacting Vacuum and the Two-Point Function#^thm-c6a-5-7|Theorem §C6a.5.7]], [[§C6a.12 The iε Limit and Vacuum Bubbles#^thm-c6a-12-4|Theorem §C6a.12.4]], [[§C6a.12 The iε Limit and Vacuum Bubbles#^thm-c6a-12-2|Theorem §C6a.12.2]], [[§C6a.12 The iε Limit and Vacuum Bubbles#^thm-c6a-12-3|Theorem §C6a.12.3]]

![[ph-qft-c6-11-2.svg]]
*The numerator factorizes: (the diagrams attached to $x$ and $y$, here the line, $\frac12$ tadpole and the shaded sum of higher orders) × (1 + the vacuum bubbles $\frac18$ figure-eight, $\frac{1}{16}$ dumbbell, $\frac{1}{48}$ melon, $\frac{1}{128}$ two figure-eights, …). The second factor is the denominator and cancels. Added figure.*

> [!example] Example §C6a.12.3: The Factorization at Second Order
> ![[ph-qft-c6a-11-3.svg]]
>
> Write $C_1 = \frac12(\text{tadpole})$ and $V_1 = \frac18(\text{figure-eight})$, each with its $-i\lambda\int d^4z$:
>
> $$
> C_1 = -\frac{i\lambda}{2}\int d^4z\,D_F(x - z)D_F(0)D_F(z - y), \qquad V_1 = -\frac{i\lambda}{8}\int d^4z\,D_F(0)^2 .
> $$
>
> [[§C6a.12 The iε Limit and Vacuum Bubbles#^thm-c6a-12-4|Theorem §C6a.12.4]] says that the second-order numerator is $C_2 + C_1V_1 + D_F(x - y)\,V_2$, with $C_2$ the attached second-order diagrams (the snowman, the chain and the sunset of [[§C6a.10 Symmetry Factors in Practice#^ex-c6a-10-4|Example §C6a.10.4]]) and $V_2$ the second-order bracket of [[§C6a.12 The iε Limit and Vacuum Bubbles#^ex-c6a-12-1|Example §C6a.12.1]]. The two cross terms check by listing complete contractions of $\hat\phi_x$, $\hat\phi_y$ and the legs $\hat\phi_{(v,a)}$ (every term of Wick's theorem with a normal-ordered remainder vanishes, Steps 3–4 of [[§C6a.9 Position-Space Feynman Rules#^der-c6a-9-1|Derivation §C6a.9.1]]), with the prefactor $\frac{1}{2!}\bigl(\frac{-i\lambda}{4!}\bigr)^2 = \frac{(-i\lambda)^2}{1152}$.
>
> *Tadpole and figure-eight* (a tadpole at one vertex $z_v$, a figure-eight at the other, $z_w$). The contractions are
>
> $$
> \{x, (v,a)\}\,\{y, (v,b)\}\,\{(v,c), (v,d)\}\,\{(w,e), (w,f)\}\,\{(w,g), (w,h)\} \;\longmapsto\; D_F(x - z_v)D_F(y - z_v)D_F(0)\cdot D_F(0)^2,
> $$
>
> with $v \in \{1, 2\}$ (2), $(a, b)$ ordered distinct legs of $v$ (12), $\{c, d\}$ the rest, and $\{\{e,f\},\{g,h\}\}$ one of the 3 pairings of the legs of $w$: $2\cdot12\cdot3 = 72$. The 36 with $v = 1$ and the 36 with $v = 2$ give the same integral after $z_1 \leftrightarrow z_2$, so
>
> $$
> \frac{(-i\lambda)^2}{1152}\cdot72\int d^4z_1\,d^4z_2\,D_F(x - z_1)D_F(0)D_F(z_1 - y)\,D_F(0)^2 = \Bigl(-\frac{i\lambda}{2}\int d^4z_1\,D_F(x - z_1)D_F(0)D_F(z_1 - y)\Bigr)\Bigl(-\frac{i\lambda}{8}\int d^4z_2\,D_F(0)^2\Bigr) = C_1V_1,
> $$
>
> since $\frac{72}{1152} = \frac{1}{16} = \frac12\cdot\frac18$. The $\frac{1}{2!}$ of the second-order expansion is compensated by the two choices $v \in \{1, 2\}$ (the binomial factor $C_2^1 = 2$ of Step 4 of [[§C6a.12 The iε Limit and Vacuum Bubbles#^der-c6a-12-4|Derivation §C6a.12.4]]); the symmetry factor $16 = 2\cdot8$ is the product of the two pieces'.
>
> *A free line times a second-order bubble.* The contractions are the pair $\{x, y\}$, a factor $D_F(x - y)$, times a complete contraction of the eight legs: $24 + 72 + 9 = 105$ ([[§C6a.10 Symmetry Factors in Practice#^ex-c6a-10-3|Example §C6a.10.3]]), and with $D_{vw} = D_F(z_v - z_w)$
>
> $$
> \frac{(-i\lambda)^2}{1152}\,D_F(x - y)\int d^4z_1\,d^4z_2\bigl[24\,D_{12}^4 + 72\,D_{11}D_{22}D_{12}^2 + 9\,D_{11}^2D_{22}^2\bigr] = D_F(x - y)\,V_2
> $$
>
> (Step 2 of [[§C6a.12 The iε Limit and Vacuum Bubbles#^ex-c6a-12-1|Example §C6a.12.1]]): coefficients $\frac{1}{48}$, $\frac{1}{16}$, $\frac{1}{128}$.
>
> Two identical figure-eights come with $\frac{9}{1152} = \frac{1}{128} = \frac12\bigl(\frac18\bigr)^2$: the $\frac{1}{2!}$ of $\frac{1}{2!}V_1^2$, the start of $e^{V_1}$. In general the bubbles exponentiate ([[§C6a.13 Exponentiation of the Vacuum Bubbles and the Vacuum Energy Density#^thm-c6a-13-1|Theorem §C6a.13.1]]).
>
> "The symmetry factors are what make the factorization work."
>
> *Source: the user's PHY 513 notes, Ch. 14 §14.7 (Derivation "The factorization at second order (filled in)", including "the start of $e^{V_1}$") · counts checked by enumeration (`qft-C/tools/l14/enumerate_pairings.py`)*

^ex-c6a-12-3

> [!caution] Caution: "Connected" means attached to an external point
> Slide 25 and PS (eqs. (4.54), (4.57)) say that the correlator is the sum of the "connected" diagrams. The precise statement is [[§C6a.12 The iε Limit and Vacuum Bubbles#^thm-c6a-12-5|Theorem §C6a.12.5]]: every piece of a diagram must be attached to at least one external point ([[§C6a.12 The iε Limit and Vacuum Bubbles#^def-c6a-12-2|Def. §C6a.12.2]]). A diagram can still be disconnected. In the free four-point function every diagram is two separate lines ([[§C6a.8 Feynman Diagrams for Correlation Functions#^ex-c6a-8-1|Example §C6a.8.1]]), and all three survive; PS: "Such diagrams do not exponentiate or factor; they contribute to the amplitude just as do the fully connected diagrams" (p. 99). What is removed are pieces attached to nothing. For the two-point function the two notions coincide.
>
> *Source: the user's PHY 513 notes, Ch. 14 §14.7 (Caution "'Connected' means attached to an external point") · PS §4.4, pp. 98–99*

^cau-c6a-12-1

> [!example] Example §C6a.12.4: The Physical Two-Point Function Through First Order, in Momentum Space
> ![[ph-qft-c6a-11-4.svg]]
>
> **Step 1** (position space). By [[§C6a.12 The iε Limit and Vacuum Bubbles#^thm-c6a-12-5|Theorem §C6a.12.5]] the figure-eight term of [[§C6a.8 Feynman Diagrams for Correlation Functions#^thm-c6a-8-1|Theorem §C6a.8.1]] is gone (done by hand at this order in [[§C6a.8 Feynman Diagrams for Correlation Functions#^cau-c6a-8-3|§C6a.8, Caution: Numerator, not yet the interacting correlator]]):
>
> $$
> \langle\Omega|T\{\hat\phi_H(x)\hat\phi_H(y)\}|\Omega\rangle = D_F(x - y) - \frac{i\lambda}{2}\int d^4z\,D_F(x - z)D_F(0)D_F(z - y) + O(\lambda^2) .
> $$
>
> **Step 2** (each term in momentum space). $D_F(x - y) = \int\frac{d^4p}{(2\pi)^4}e^{-ip\cdot(x-y)}\tilde D_F(p)$ ([[§C2b.7 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-7-10|Theorem §C2b.7.10]]), and the tadpole term is [[§C6a.11 Feynman Rules in Momentum Space#^ex-c6a-11-1|Example §C6a.11.1]]. Under one $p$-integral,
>
> $$
> \langle\Omega|T\{\hat\phi_H(x)\hat\phi_H(y)\}|\Omega\rangle = \int\frac{d^4p}{(2\pi)^4}\,e^{-ip\cdot(x-y)}\Bigl[\tilde D_F(p) + \tilde D_F(p)\Bigl(-\frac{i\lambda}{2}\int\frac{d^4k}{(2\pi)^4}\tilde D_F(k)\Bigr)\tilde D_F(p) + O(\lambda^2)\Bigr] :
> $$
>
> the line with momentum $p$, plus $\frac12$ the tadpole with $p$ entering, $p$ leaving and $k$ in the loop. "Physical two point function has no figure-8 vacuum bubble" (slide 25).
>
> *Source: PHY 513 Lecture 14, slide 25 (bottom) · the user's PHY 513 notes, Ch. 14 §14.6 (paragraph "The momentum-space two-point function") · Yu §10.5.1, eq. (10.209) (first two diagrams)*

^ex-c6a-12-4

> [!remark] Remark: Why the bubbles had to go
> The denominator was there because $|0\rangle$ is the wrong vacuum: it fixes the normalization against the true one, $|\Omega\rangle$ ([[§C6a.5 The Interacting Vacuum and the Two-Point Function#^thm-c6a-5-4|Theorem §C6a.5.4]]). The bubbles are diagrams that know about the vacuum and nothing else, processes unrelated to the quantity being computed. To understand the true vacuum wave function one would have to analyse these diagrams ([[§C6a.12 The iε Limit and Vacuum Bubbles#^ex-c6a-12-2|Example §C6a.12.2]] does it at first order), but that is not the question: the question concerns particles coming in and going out, not what the vacuum does on its own. The interacting vacuum is taken into account by not drawing them.
>
> *Source: PHY 513 Lecture 14, transcript · the user's PHY 513 notes, Ch. 14 §14.7 (paragraph "Why the bubbles had to go")*

^rem-c6a-12-2

> [!remark] Remark: From the master formula to Feynman diagrams (summary)
> - Wick's theorem: $T\{\hat\phi_1\cdots\hat\phi_n\} = \,:\!\hat\phi_1\cdots\hat\phi_n\!: +$ all contractions, a contraction being $D_F$ ([[§C6a.7 Wick's Theorem#^thm-c6a-7-2|Theorem §C6a.7.2]]); in the vacuum, $\sum_{\text{pairings}}\prod D_F$ ([[§C6a.7 Wick's Theorem#^thm-c6a-7-3|Theorem §C6a.7.3]]).
> - Each pairing is a diagram; the pairings of one diagram are an orbit, and the coefficient is $1/S$ ([[§C6a.9 Position-Space Feynman Rules#^thm-c6a-9-1|Theorem §C6a.9.1]]).
> - In $\phi^4$ theory the interacting correlator is the sum of all diagrams attached to the external points ([[§C6a.12 The iε Limit and Vacuum Bubbles#^thm-c6a-12-5|Theorem §C6a.12.5]]), with a line $D_F$ or $\frac{i}{p^2 - m^2 + i\varepsilon}$; a vertex $-i\lambda\int d^4z$, or $-i\lambda$ with momentum conservation; integration over undetermined momenta; a factor $1/S$ ([[§C6a.9 Position-Space Feynman Rules#^thm-c6a-9-4|Theorem §C6a.9.4]], [[§C6a.11 Feynman Rules in Momentum Space#^thm-c6a-11-2|Theorem §C6a.11.2]]).
> - The $T \to \infty(1 - i\varepsilon)$ limit is the Feynman $i\varepsilon$ ([[§C6a.12 The iε Limit and Vacuum Bubbles#^thm-c6a-12-1|Theorem §C6a.12.1]]), and the denominator cancels the vacuum bubbles.
>
> *Source: the user's PHY 513 notes, Ch. 14 §14.8 (Principle "From the master formula to Feynman diagrams")*

^rem-c6a-12-3

> [!remark] Remark: Yu's route
> Yu builds correlation functions from the asymptotic in-fields, $G^{(n)} = \frac{1}{\mathcal N}\langle0|T\{\phi_{\rm in}(x_1)\cdots\phi_{\rm in}(x_n)\exp[-i\int dt\,\tilde H_1]\}|0\rangle$ (eq. (10.177)), where the normalization $\mathcal N$ is a pure phase, the vacuum-to-vacuum amplitude (eq. (10.178)), and expands both (eqs. (10.180)–(10.181)). There is no tilted time: the in-field construction (LSZ, QFT C10, planned) replaces the $i\varepsilon$ projection of [[§C6a.5 The Interacting Vacuum and the Two-Point Function|§C6a.5]]. He notices the factorization in the first-order terms (eq. (10.192)), expands $\mathcal N$ in bubbles including the $\delta m^2$ crosses (eq. (10.193)), states the cancellation in a box, and proves it by the binomial split (eqs. (10.194)–(10.196)), arriving at "all connected diagrams with the $n$ external points" (eq. (10.197)). PS reach the same factorization by exponentiating the disconnected pieces (pp. 96–98; [[§C6a.12 The iε Limit and Vacuum Bubbles#^der-c6a-12-4b|Derivation §C6a.12.4, second route]]).
>
> *Source: Yu §10.4–§10.5.1, pp. 463–468*

^rem-c6a-12-4

> [!remark] Remark: From correlation functions to cross sections (preview)
> Slide 26: the next lecture relates correlation functions to more conventional observables (cross sections, decay widths); then come the Feynman rules for physical amplitudes in $\phi^4$ theory ([[§C6c.6 Feynman Rules for Amplitudes|§C6c.6]]), and after that in QED (PS §4.5–§4.8). The course went through Yukawa theory first, the rules with fermions (Lecture 17, [[· C6d Feynman Rules for Fermions|C6d]]), and then to QED (Lecture 18, [[· C8 Quantum Electrodynamics|C8]]). The answer is built from the same pieces as here: products of the same propagators and vertices. Lecture 15 (Oct 28) did the first step: the $S$-matrix and the amplitude $\mathcal M$ ([[§C6b.1 The S-Matrix and the Invariant Amplitude|§C6b.1]]), cross sections ([[§C6b.8 Wave Packets and the Cross Section|§C6b.8]], [[§C6b.9 Evaluating the Cross Section|§C6b.9]], [[§C6b.4 Two-Body Scattering Kinematics|§C6b.4]]), decay rates ([[§C6b.5 Decay Widths|§C6b.5]]), and the rule that amplitudes are these correlation functions with the external propagators stripped off ([[§C6c.1 Amplitudes from Correlation Functions#^thm-c6c-1-1|Theorem §C6c.1.1]]).
>
> *Source: PHY 513 Lecture 14, slide 26, and transcript*

^rem-c6a-12-5

> [!abstract]- Mathematical background
> Proved in CA; each line says what the physics above relies on.
>
> - [[§CA.9 Splitting Pairings and the Exponential Formula#^thm-ca-9-1|Theorem §CA.9.1]] — a pairing splits uniquely into the part attached to the external points and a vacuum part,
> - [[§CA.9 Splitting Pairings and the Exponential Formula#^thm-ca-9-2|Theorem §CA.9.2]] — and a sum over pairings with an exponential weight $\frac{t^k}{k!}$ factorizes accordingly.
> - [[§CA.3 Products of Distributions and Operator-Valued Distributions#^thm-ca-3-3|Theorem §CA.3.3]] — a delta function at zero momentum in a finite box is the volume.
> - [[§CA.9 Splitting Pairings and the Exponential Formula#^def-ca-9-1|Def. §CA.9.1]] — "attached" for labelled diagrams: every vertex joined by a path to an external point (Definition §C6a.12.2).
> - [[§CA.9 Splitting Pairings and the Exponential Formula#^thm-ca-9-3|Theorem §CA.9.3]] — the exponential formula: the sum over all vacuum diagrams is the exponential of the sum over connected ones, and $n_i$ copies of a connected piece contribute $n_i!\,S(V_i)^{n_i}$ to the symmetry factor (the second route of Derivation §C6a.12.4).
> - [[§CA.8 Pairings, Diagrams and Symmetry Factors#^thm-ca-8-8|Theorem §CA.8.8]] — a diagram is its drawing, so being attached is a property of the diagram and the attached pairings are a union of orbits (Derivation §C6a.12.4, Step 5).
> - [[§CA.4 Fourier Transforms and Fourier Tricks#^thm-ca-4-3|Theorem §CA.4.3]], [[§CA.4 Fourier Transforms and Fourier Tricks#^thm-ca-4-6|Theorem §CA.4.6]] — the time integral of the plane waves at a vertex is an energy delta function, as the limit of box integrals (Derivation §C6a.12.1); shifting and renaming the vertex positions has unit Jacobian (Derivations §C6a.12.3 and §C6a.12.4).
> - [[§CA.7 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-7-6|Theorem §CA.7.6]] — part 3, only the sign of the infinitesimal near the mass shell matters: the tilted energies give $p^2 - m^2 + i\varepsilon$ (Theorem §C6a.12.1).
> - [[§CA.7 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-7-5|Theorem §CA.7.5]] — a damping factor on $t > 0$ puts the pole below the real axis: why the tilt that projects onto the vacuum is the Feynman prescription (Remark: Why "precisely what we do already").

> [!remark]- Connections
> - The tilt of the times that projects onto the true vacuum is the same infinitesimal rotation that, finite, is the Wick rotation to Euclidean time; Euclidean correlators have no $i\varepsilon$ at all — [[§C2b.8 Wick Rotation and the Two-Point Family#^thm-c2b-8-1|Theorem §C2b.8.1]], [[§C6a.5 The Interacting Vacuum and the Two-Point Function#^thm-c6a-5-1|Theorem §C6a.5.1]].
> - Quantum mechanics switches perturbations on adiabatically with $e^{\varepsilon t}$; the same damping, in field theory, both selects the vacuum and fixes the propagator — [[§C10.1 The Lippmann–Schwinger Equation and the Born Approximation|QM §C10.1]], [[§CA.7 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-7-5|Theorem §CA.7.5]].
> - The factorization is a statement about sums over pairings with an exponential weight, proved in CA without physics — [[§CA.9 Splitting Pairings and the Exponential Formula#^thm-ca-9-2|Theorem §CA.9.2]].
> - Correlation functions become scattering amplitudes through the LSZ reduction formula, which is also Yu's route to this section's results; at lowest order the rule is "strip off the external lines" — [[§C6c.1 Amplitudes from Correlation Functions#^thm-c6c-1-1|Theorem §C6c.1.1]], QFT C10 (planned), [[§C6a.5 The Interacting Vacuum and the Two-Point Function#^rem-c6a-5-5|§C6a.5, Remark: Correspondence with Yu]].
