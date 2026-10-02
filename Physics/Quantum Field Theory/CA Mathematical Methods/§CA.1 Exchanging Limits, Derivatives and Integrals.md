---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: CA
section: CA.1
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
↑ [[· CA Mathematical Methods]] · [[§CA.2 Generalized Functions]] →

*Sources: the user's PHY 513 notes, App. A §A.1 (Principle "Interchanging limits, derivatives and integrals"), citing Rudin, Principles of Mathematical Analysis, Ch. 6, 7 and 11.*

Quantum field theory differentiates under integrals, lets regulators $e^{-\varepsilon p}$ go to zero, and exchanges limits with derivatives, usually without comment. None of these exchanges is automatic. This section collects the three theorems that license them for ordinary integrals, starting from dominated convergence ([[§15 The General Lebesgue Integral#^thm-15-8|551 Thm. §15.8]]), the mean value theorem ([[§29 The Mean Value Theorem#^thm-29-3|451 Thm. §29.3]]) and the fundamental theorem of calculus ([[§34 Fundamental Theorem of Calculus#^thm-34-1|451 Thm. §34.1]]), and says where each is used and where none applies. Integrals that do not converge even conditionally are generalized functions, the subject of [[§CA.2 Generalized Functions|§CA.2]]; there the exchanges hold by definition ([[§CA.2 Generalized Functions#^thm-ca-2-4|Theorem §CA.2.4]]). This chapter is the interim home of these tools until a math-side Mathematical Methods subject exists (planned).

> [!theorem] Theorem §CA.1.1: Dominated Convergence and Differentiation under the Integral
> 1. *(Dominated convergence)* If $f_n(p) \to f(p)$ for almost every $p$ and $|f_n| \le g$ with $\int g < \infty$, then $\int f_n \to \int f$.
> 2. *(Leibniz)* If $F(r) = \int f(p, r)\,dp$, $\partial_rf$ exists, and $|\partial_rf(p, r)| \le g(p)$ with $\int g < \infty$ for all $r$ in an interval, then $F'(r) = \int\partial_rf(p, r)\,dp$ there.
>
> A limit $\varepsilon \to 0^+$ is covered by applying each statement to every sequence $\varepsilon_n \to 0^+$.
>
> *Source: the user's PHY 513 notes, App. A §A.1 (theorems 1–2), citing Rudin, Principles of Mathematical Analysis, Ch. 11*

^thm-ca-1-1

> [!derivation]- Derivation
> **Step 1** (part 1). This is [[§15 The General Lebesgue Integral#^thm-15-8|551 Thm. §15.8]].
>
> **Step 2** (difference quotient). For $h \ne 0$, $\frac{F(r + h) - F(r)}{h} = \int\frac{f(p, r + h) - f(p, r)}{h}\,dp$, and by the mean value theorem ([[§29 The Mean Value Theorem#^thm-29-3|451 Thm. §29.3]]), applied separately to the real and imaginary parts of $f$ (the integrands here are complex exponentials), each part of the integrand equals the same part of $\partial_rf(p, r^*)$ for some $r^*$ between $r$ and $r + h$ (a different $r^*$ for each part), so the integrand is bounded by $2g(p)$ independently of $h$.
>
> **Step 3** (limit). For any sequence $h_n \to 0$ the integrands converge to $\partial_rf(p, r)$, dominated by $2g$; by Step 1 the integrals converge to $\int\partial_rf\,dp$.
>
> **What the derivation shows.**
> - The whole content is that the dominating function does not depend on $n$ (or $h$); a bound that worsens as $\varepsilon \to 0$ is not enough.
> - Used in: analyticity of the Wightman function in the lower half-plane ([[§C2.8 The Wightman Function#^thm-c2-8-5|Theorem §C2.8.5]]), its third evaluation ([[§C2.9 Explicit Forms of the Wightman Function#^thm-c2-9-3|Theorem §C2.9.3]]), and Sokhotski–Plemelj ([[§CA.2 Generalized Functions#^thm-ca-2-11|Theorem §CA.2.11]]).

^der-ca-1-1

*Uses:* [[§15 The General Lebesgue Integral#^thm-15-8|551 Thm. §15.8]], [[§29 The Mean Value Theorem#^thm-29-3|451 Thm. §29.3]]

> [!theorem] Theorem §CA.1.2: Conditionally Convergent Integrals: Dirichlet's Test and Abel's Theorem
> 1. *(Dirichlet)* If $g$ decreases monotonically to $0$ on $[0, \infty)$ and $\bigl|\int_0^Ph\bigr| \le M$ for all $P$, then $\int_0^\infty g\,h$ converges (in general only conditionally). Example: $\int_0^\infty\frac{\cos pr}{\sqrt{p^2 + m^2}}\,dp$, $r > 0$.
> 2. *(Abel)* If $\int_0^\infty f$ converges, possibly only conditionally, then $\lim_{\varepsilon\to0^+}\int_0^\infty e^{-\varepsilon p}f(p)\,dp = \int_0^\infty f$.
>
> So a regulator $e^{-\varepsilon p}$ is harmless whenever the unregulated integral exists.
>
> *Source: the user's PHY 513 notes, App. A §A.1 (theorems 3–4)*

^thm-ca-1-2

> [!derivation]- Derivation
> *Part 1*, for $g$ continuously differentiable (every use here; the general case uses the second mean value theorem).
>
> **Step 1** (integrate by parts). With $H(P) = \int_0^Ph$, $\int_0^Pg\,h = g(P)H(P) - \int_0^Pg'(p)H(p)\,dp$ (boundary term at $0$: $H(0) = 0$).
>
> **Step 2** (the boundary term). $|g(P)H(P)| \le Mg(P) \to 0$.
>
> **Step 3** (the integral). $g' \le 0$, so $|g'H| \le -Mg'$, and $\int_0^\infty(-g') = g(0) - \lim g = g(0)$: the integral converges absolutely. Example: $g = 1/\sqrt{p^2 + m^2}$, $h = \cos pr$, $|\int_0^P\cos pr\,dp| \le 1/r$.
>
> *Part 2.*
>
> **Step 4** (the tail). Let $R(p) = \int_p^\infty f$; it is continuous, bounded by some $B$, tends to $0$, and $f = -R'$.
>
> **Step 5** (integrate by parts). $\int_0^\infty e^{-\varepsilon p}f\,dp = -\bigl[e^{-\varepsilon p}R\bigr]_0^\infty - \varepsilon\int_0^\infty e^{-\varepsilon p}R\,dp = R(0) - \varepsilon\int_0^\infty e^{-\varepsilon p}R(p)\,dp$; the boundary term at $\infty$ vanishes because $R \to 0$.
>
> **Step 6** (the remainder vanishes). Split at $P$: $\bigl|\varepsilon\int_0^Pe^{-\varepsilon p}R\bigr| \le \varepsilon PB$ and $\bigl|\varepsilon\int_P^\infty e^{-\varepsilon p}R\bigr| \le \sup_{p > P}|R(p)|\cdot\varepsilon\int_0^\infty e^{-\varepsilon p}dp = \sup_{p > P}|R|$. Given $\eta > 0$, choose $P$ with $\sup_{p > P}|R| < \eta$, then $\varepsilon < \eta/PB$.
>
> **What the derivation shows.**
> - Abel's theorem needs the *unregulated* integral to exist; it says nothing about integrals that diverge (those are generalized functions, [[§CA.2 Generalized Functions#^def-ca-2-2|Def. §CA.2.2]]).
> - It does not license exchanging the limit with a derivative: that needs Theorem §CA.1.3.

^der-ca-1-2

*Uses:* [[§34 Fundamental Theorem of Calculus#^thm-34-1|451 Thm. §34.1]] (for $H' = h$ and $R' = -f$ in the integrations by parts)

> [!theorem] Theorem §CA.1.3: Limits of Derivatives
> Let $F_n$ be differentiable on an interval, let $F_n(r_0)$ converge at one point, and let $F_n' \to G$ *uniformly* on the interval. Then $F_n \to F$ uniformly on bounded subintervals and $F' = G$. Pointwise convergence of the derivatives is not enough.
>
> *Source: the user's PHY 513 notes, App. A §A.1 (theorem 5), citing Rudin, Theorem 7.17*

^thm-ca-1-3

> [!derivation]- Derivation
> For continuous $F_n'$ (the case used here; Rudin's proof removes it).
>
> **Step 1** (integral form). $F_n(r) = F_n(r_0) + \int_{r_0}^rF_n'(s)\,ds$ ([[§34 Fundamental Theorem of Calculus#^thm-34-1|451 Thm. §34.1]]).
>
> **Step 2** (limit). $|\int_{r_0}^r(F_n' - G)| \le |r - r_0|\sup|F_n' - G| \to 0$, uniformly for $r$ in a bounded subinterval; so $F_n(r) \to F(r) \equiv \lim F_n(r_0) + \int_{r_0}^rG$ uniformly.
>
> **Step 3** (derivative). $G$ is continuous, as a uniform limit of continuous functions, so $F' = G$ ([[§34 Fundamental Theorem of Calculus#^thm-34-4|451 Thm. §34.4]]).
>
> **Step 4** (why uniformity matters). $F_n = \sin(nr)/\sqrt n$ tends to $0$ uniformly, yet $F_n'(0) = \sqrt n$ diverges: convergence of functions says nothing about convergence of derivatives.
>
> **What the derivation shows.**
> - This is the step that needs care in the real-variable evaluation of the Wightman function ([[§C2.9 Explicit Forms of the Wightman Function#^thm-c2-9-3|Theorem §C2.9.3]], third route, Step 4).

^der-ca-1-3

*Uses:* [[§34 Fundamental Theorem of Calculus#^thm-34-1|451 Thm. §34.1]], [[§34 Fundamental Theorem of Calculus#^thm-34-4|451 Thm. §34.4]]

> [!remark] Remark: Where each exchange is used, and where none applies
> Leibniz whenever $\partial_r$ or $\partial_t$ is taken inside a regulated integral; Dirichlet and Abel when a regulator is removed from a conditionally convergent integral; uniform convergence of derivatives in the real-variable evaluation of the Wightman function, where a limit and a derivative must be exchanged; dominated convergence in the Sokhotski–Plemelj formula ([[§CA.2 Generalized Functions#^thm-ca-2-11|Theorem §CA.2.11]]). Integrals that do not converge even conditionally, such as $\int d^3p/E_{\mathbf p}$, are covered by none of these. They are defined as generalized functions ([[§CA.2 Generalized Functions#^def-ca-2-2|Def. §CA.2.2]]), and there the exchanges hold by definition.
>
> *Source: the user's PHY 513 notes, App. A §A.1*

^rem-ca-1-1

> [!remark]- Connections
> - Dominated convergence is [[§15 The General Lebesgue Integral#^thm-15-8|551 Thm. §15.8]]; the whole content of Theorem §CA.1.1 is that the dominating function does not depend on the parameter, and the same check recurs in Sokhotski–Plemelj ([[§CA.2 Generalized Functions#^thm-ca-2-11|Theorem §CA.2.11]]), in nascent delta functions ([[§CA.2 Generalized Functions#^thm-ca-2-4|Theorem §CA.2.4]], 3) and in every boundary value ([[§CA.2 Generalized Functions#^thm-ca-2-10|Theorem §CA.2.10]]).
> - Abel's theorem says that a regulator $e^{-\varepsilon p}$ is harmless when the integral exists; the equal-time Wightman function shows the other case, where $e^{-\varepsilon E_{\mathbf p}}$ is not a regulator to be removed but the definition of a boundary value ([[§C2.8 The Wightman Function#^thm-c2-8-5|Theorem §C2.8.5]], Step 5).
> - Theorem §CA.1.3 fails for distributions in the most useful way: there, limits and derivatives always commute ([[§CA.2 Generalized Functions#^thm-ca-2-4|Theorem §CA.2.4]], 2); C2 needs the function version only for pointwise formulas such as the real-variable evaluation of the Wightman function ([[§C2.9 Explicit Forms of the Wightman Function#^thm-c2-9-3|Theorem §C2.9.3]]).
> - **Used in** (C2 places): Theorem §CA.1.1 — analyticity of the Wightman function and its Euclidean and real-variable evaluations ([[§C2.8 The Wightman Function#^thm-c2-8-2|Theorem §C2.8.2]], [[§C2.8 The Wightman Function#^thm-c2-8-4|Theorem §C2.8.4]], [[§C2.8 The Wightman Function#^thm-c2-8-5|Theorem §C2.8.5]], [[§C2.9 Explicit Forms of the Wightman Function#^thm-c2-9-1|Theorem §C2.9.1]], [[§C2.9 Explicit Forms of the Wightman Function#^thm-c2-9-3|Theorem §C2.9.3]], [[§C2.9 Explicit Forms of the Wightman Function#^thm-c2-9-6|Theorem §C2.9.6]]), exchanges of integrals in the source problem ([[§C2.14 Particle Production by a Classical Source#^thm-c2-14-1|Theorem §C2.14.1]]), differentiation under smeared mode integrals ([[§C2.7 Heisenberg Fields#^thm-c2-7-1|Theorem §C2.7.1]], [[§C2.10 Microcausality and the Commutator Function#^thm-c2-10-10|Theorem §C2.10.10]], [[§C2.12 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2-12-6|Theorem §C2.12.6]]), the $\varepsilon \to 0^+$ limit of a contour ([[§C2.11 Green's Functions and Contours#^thm-c2-11-4|Theorem §C2.11.4]]), differentiation under mode integrals for wave packets and the norm bound for a narrowing smeared field ([[§C2.1 Canonical Quantization of Fields#^thm-c2-1-3|Theorem §C2.1.3]], [[§C2.2 Mode Expansion and the Mode Algebra#^thm-c2-2-2|Theorem §C2.2.2]], [[§C2.3 Energy, Momentum and the Zero-Point Energy#^thm-c2-3-1|Theorem §C2.3.1]], [[§C2.4 Particles and Relativistic Normalization#^thm-c2-4-8|Theorem §C2.4.8]], [[§C2.6 Coherent States and the Classical Field#^thm-c2-6-4|Theorem §C2.6.4]]); Theorem §CA.1.2 — the spacelike Wightman function ([[§C2.9 Explicit Forms of the Wightman Function#^thm-c2-9-3|Theorem §C2.9.3]], second and third routes); Theorem §CA.1.3 — the third route to it ([[§C2.9 Explicit Forms of the Wightman Function#^thm-c2-9-3|Theorem §C2.9.3]]).
> - **Used in** (C1 places): Theorem §CA.1.1 — the single-particle amplitude as a boundary value and in closed form ([[§C1.3 Causal Structure and the Causality of a Single Particle#^thm-c1-3-2|Theorem §C1.3.2]], [[§C1.3 Causal Structure and the Causality of a Single Particle#^thm-c1-3-4|Theorem §C1.3.4]], [[§C1.3 Causal Structure and the Causality of a Single Particle#^thm-c1-3-6|Theorem §C1.3.6]]), the Euler–Lagrange and Hamilton equations ([[§C1.9 The Action Principle and the Euler–Lagrange Equations#^thm-c1-9-4|Theorem §C1.9.4]], [[§C1.10 Hamiltonian Field Theory#^thm-c1-10-1|Theorem §C1.10.1]], [[§C1.10 Hamiltonian Field Theory#^thm-c1-10-4|Theorem §C1.10.4]]), conservation of a Noether charge ([[§C1.11 Noether's Theorem#^thm-c1-11-3|Theorem §C1.11.3]], [[§C1.11 Noether's Theorem#^rem-c1-11-6|§C1.11, Remark: In what sense these identities hold]]).
> - **Used in** (C5 places): Theorem §CA.1.1 — a solution of the Dirac equation as a wave packet of plane-wave spinors, differentiated under the integral ([[§C5.5 Plane-Wave Solutions#^rem-c5-5-6|§C5.5, Remark: In what sense a general solution is a superposition of these plane waves]]).
