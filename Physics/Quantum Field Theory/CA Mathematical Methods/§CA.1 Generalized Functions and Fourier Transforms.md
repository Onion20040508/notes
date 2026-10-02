---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: CA
section: CA.1
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
↑ [[· CA Mathematical Methods]] · [[§CA.2 Contour Integration]] →

*Sources: the user's PHY 513 notes, App. A §§A.1–A.4 and the Sokhotski–Plemelj part of §A.5, Ch. 4 §4.4 (the six rules), Ch. 6 §§6.2–6.3 · PHY 513, Problem Set 4, Problem 0 (generalized functions) and eq. (11).*

Quantum field theory writes integrals that converge for no real value of their arguments, delta functions of four-vectors, and infinitesimals $i\varepsilon$, and it exchanges limits, derivatives and integrals freely. This section says what each of these means and when each exchange is allowed. It starts from the working delta function and Fourier transform of [[§B4.4 Fourier Transforms and the Delta Function#^def-b4-4-2|WO Def. §B4.4.2]] and [[§B1.2 The Dirac Delta Function and the Helmholtz Theorem#^thm-b1-2-1|EM Theorem §B1.2.1]], from dominated convergence ([[§15 The General Lebesgue Integral#^thm-15-8|551 Thm. §15.8]]) and from the δ-normalized kets of [[§26 Position Eigenstates and Continuous Resolutions#^prop-26-3|556 Prop. §26.3]]. New here: the field-theory conventions for the transform in space and spacetime with their rules, the angular integral, generalized functions as linear maps on test functions, and the Sokhotski–Plemelj formula, which is how every $i\varepsilon$ of [[§C2.6 Green's Functions and the Feynman Propagator|§C2.6]] is read. This chapter is the interim home of these tools until a math-side Mathematical Methods subject exists (planned).

## Exchanging limits, derivatives and integrals

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
> **Step 2** (difference quotient). For $h \ne 0$, $\frac{F(r + h) - F(r)}{h} = \int\frac{f(p, r + h) - f(p, r)}{h}\,dp$, and by the mean value theorem ([[§29 The Mean Value Theorem#^thm-29-3|451 Thm. §29.3]]) the integrand equals $\partial_rf(p, r^*)$ for some $r^*$ between $r$ and $r + h$, so it is bounded by $g(p)$ independently of $h$.
>
> **Step 3** (limit). For any sequence $h_n \to 0$ the integrands converge to $\partial_rf(p, r)$, dominated by $g$; by Step 1 the integrals converge to $\int\partial_rf\,dp$.
>
> **What the derivation shows.**
> - The whole content is that the dominating function does not depend on $n$ (or $h$); a bound that worsens as $\varepsilon \to 0$ is not enough.
> - Used in: analyticity of the Wightman function in the lower half-plane ([[§C2.5 Heisenberg Fields, Two-Point Functions and Causality#^thm-c2-5-7|Theorem §C2.5.7]]), its third evaluation ([[§C2.5 Heisenberg Fields, Two-Point Functions and Causality#^thm-c2-5-10|Theorem §C2.5.10]]), and Sokhotski–Plemelj (Theorem §CA.1.8).

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
> - Abel's theorem needs the *unregulated* integral to exist; it says nothing about integrals that diverge (those are generalized functions, Def. §CA.1.2).
> - It does not license exchanging the limit with a derivative: that needs Theorem §CA.1.3.

^der-ca-1-2

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
> - This is the step that needs care in the real-variable evaluation of the Wightman function ([[§C2.5 Heisenberg Fields, Two-Point Functions and Causality#^thm-c2-5-10|Theorem §C2.5.10]], third route, Step 4).

^der-ca-1-3

*Uses:* [[§34 Fundamental Theorem of Calculus#^thm-34-1|451 Thm. §34.1]], [[§34 Fundamental Theorem of Calculus#^thm-34-4|451 Thm. §34.4]]

> [!remark] Remark: Where each exchange is used, and where none applies
> Leibniz whenever $\partial_r$ or $\partial_t$ is taken inside a regulated integral; Dirichlet and Abel when a regulator is removed from a conditionally convergent integral; uniform convergence of derivatives in the real-variable evaluation of the Wightman function, where a limit and a derivative must be exchanged; dominated convergence in the Sokhotski–Plemelj formula below. Integrals that do not converge even conditionally, such as $\int d^3p/E_{\mathbf p}$, are covered by none of these. They are defined as generalized functions (Def. §CA.1.2 below), and there the exchanges hold by definition.
>
> *Source: the user's PHY 513 notes, App. A §A.1*

^rem-ca-1-1

## Fourier transforms in space and spacetime

> [!definition] Definition §CA.1.1: Fourier Transform in Space and Spacetime
> In space and in spacetime, with $p\cdot x = p^0t - \mathbf p\cdot\mathbf x$,
>
> $$
> f(\mathbf x) = \int\frac{d^3k}{(2\pi)^3}\,\tilde f(\mathbf k)\,e^{i\mathbf k\cdot\mathbf x}, \quad \tilde f(\mathbf k) = \int d^3x\,f(\mathbf x)\,e^{-i\mathbf k\cdot\mathbf x}; \qquad f(x) = \int\frac{d^4p}{(2\pi)^4}\,\tilde f(p)\,e^{-ip\cdot x}, \quad \tilde f(p) = \int d^4x\,f(x)\,e^{ip\cdot x} .
> $$
>
> All factors of $2\pi$ sit with the momentum integral. The phase $e^{-ip\cdot x} = e^{-ip^0t}\,e^{+i\mathbf p\cdot\mathbf x}$ has opposite signs on time and space.
>
> *Source: the user's PHY 513 notes, Ch. 6 §6.3 (Definition "Conventions") · PS §2.4, eq. (2.57) · Yu, same convention*

^def-ca-1-1

> [!caution] Caution: Two conventions in the vault
> Oscillations and waves ([[§B4.4 Fourier Transforms and the Delta Function#^def-b4-4-1|WO Def. §B4.4.1]]) puts $1/2\pi$ in the forward transform and synthesizes from $e^{+i\omega t}$, the engineering time dependence of that subject. Here the time factor is the positive-frequency $e^{-iEt}$ of quantum mechanics and the space factor is the $e^{+i\mathbf p\cdot\mathbf x}$ of the mode expansions; the opposite signs are the Minkowski metric, not an inconsistency. PS, Yu and the user's notes use the convention of Def. §CA.1.1; some books put $e^{+ip\cdot x}$ in the synthesis, which flips every sign below. Convert before combining formulas.

^cau-ca-1-1

> [!theorem] Theorem §CA.1.4: Rules of the Fourier Transform
> 1. *Plane-wave delta functions:* $\int d^3x\,e^{i\mathbf k\cdot\mathbf x} = (2\pi)^3\delta^3(\mathbf k)$ and $\int d^4x\,e^{ip\cdot x} = (2\pi)^4\delta^4(p)$; the pairs of Def. §CA.1.1 are inverse to each other.
> 2. *Derivatives:* $\partial_\mu \leftrightarrow -ip_\mu$, so $\partial^2 \leftrightarrow -p^2$ and $\partial^2 + m^2 \leftrightarrow m^2 - p^2$.
> 3. *Convolution:* if $h(x) = \int d^4y\,D(x - y)\,j(y)$, then $\tilde h(p) = \tilde D(p)\,\tilde j(p)$.
> 4. *Reality and invariance:* $f$ real $\Rightarrow$ $\tilde f(-p) = \overline{\tilde f(p)}$; $f$ a Lorentz scalar $\Rightarrow$ $\tilde f$ a Lorentz scalar.
>
> All hold in the sense of generalized functions (Def. §CA.1.3).
>
> *Source: the user's PHY 513 notes, Ch. 6 §6.3 (Derivation "The rules"), Ch. 4 §4.4 (rules 1 and 4), App. A §A.2*

^thm-ca-1-4

> [!derivation]- Derivation
> **Step 1** (rule 1). In one dimension $\int ds\,e^{iks} = 2\pi\delta(k)$ ([[§B4.4 Fourier Transforms and the Delta Function#^thm-b4-4-3|WO Theorem §B4.4.3]], 4, with $\omega \to k$, $t \to s$; the sign in the exponent is irrelevant since $\delta$ is even). The integral over $d^3x$ or $d^4x$ factorizes into three or four such integrals: $\int d^4x\,e^{ip\cdot x} = \int dt\,e^{ip^0t}\prod_{i=1}^3\int dx^i\,e^{-ip^ix^i} = (2\pi)^4\delta(p^0)\delta^3(\mathbf p)$. As a statement against test functions this is [[§CA.1 Generalized Functions and Fourier Transforms#^thm-ca-1-7|Theorem §CA.1.7]], 3.
>
> **Step 2** (inversion). Insert the synthesis into the analysis formula: $\int d^4x\,e^{ip\cdot x}\int\frac{d^4q}{(2\pi)^4}\tilde f(q)e^{-iq\cdot x} = \int\frac{d^4q}{(2\pi)^4}\tilde f(q)\,(2\pi)^4\delta^4(p - q) = \tilde f(p)$, the $x$ integral done first by Step 1.
>
> **Step 3** (rule 2). $\partial_0e^{-ip\cdot x} = -ip^0e^{-ip\cdot x} = -ip_0e^{-ip\cdot x}$; $\partial_ie^{+i\mathbf p\cdot\mathbf x} = +ip^ie^{i\mathbf p\cdot\mathbf x} = -ip_ie^{i\mathbf p\cdot\mathbf x}$ (lowering a spatial index changes its sign). So $\partial_\mu \to -ip_\mu$ for all four components, and $\partial^2 = \partial_\mu\partial^\mu \to (-ip_\mu)(-ip^\mu) = -p^2$.
>
> ⚑ By-product: the opposite signs in the phase are what let one formula cover all four components; with $\partial^2 + m^2 \to m^2 - p^2$, the Klein–Gordon operator is multiplication by a function that vanishes exactly on the mass shell → [[§CA.1 Generalized Functions and Fourier Transforms#^rem-ca-1-2|Remark: A linear equation becomes algebra]].
>
> **Step 4** (rule 3). $\tilde h(p) = \int d^4x\,e^{ip\cdot x}\int d^4y\,D(x - y)j(y)$. Substitute $x = u + y$ at fixed $y$ (Jacobian 1), so $e^{ip\cdot x} = e^{ip\cdot u}e^{ip\cdot y}$: $\tilde h(p) = \int d^4y\,e^{ip\cdot y}j(y)\int d^4u\,e^{ip\cdot u}D(u) = \tilde j(p)\tilde D(p)$.
>
> **Step 5** (reality). Conjugate $\tilde f(p) = \int d^4x\,f(x)e^{ip\cdot x}$ with $f$ real: $\overline{\tilde f(p)} = \int d^4x\,f(x)e^{-ip\cdot x} = \tilde f(-p)$.
>
> **Step 6** (invariance). A scalar satisfies $f(\Lambda^{-1}x) = f(x)$. In $\tilde f(\Lambda p) = \int d^4x\,f(x)e^{i(\Lambda p)\cdot x}$ substitute $x = \Lambda y$: $|\det\Lambda| = 1$, $(\Lambda p)\cdot(\Lambda y) = p\cdot y$ ([[§B1.2 Lorentz Transformations and the Lorentz Group#^thm-b1-2-2|REL Theorem §B1.2.2]]), $f(\Lambda y) = f(y)$; so $\tilde f(\Lambda p) = \tilde f(p)$.
>
> **What the derivation shows.**
> - Every rule is a substitution or a factorization; the only analysis is in rule 1, which is a statement about generalized functions.
> - Used in: the Green's function as division by $m^2 - p^2$ ([[§C2.6 Green's Functions and the Feynman Propagator#^thm-c2-6-2|Theorem §C2.6.2]]), the canonical relations recovered from mode integrals ([[§C2.5 Heisenberg Fields, Two-Point Functions and Causality#^thm-c2-5-19|Theorem §C2.5.19]]), the source transform $\tilde j$ ([[§C2.7 Particle Production by a Classical Source#^thm-c2-7-1|Theorem §C2.7.1]]).

^der-ca-1-4

*Uses:* [[§B4.4 Fourier Transforms and the Delta Function#^thm-b4-4-3|WO Theorem §B4.4.3]], [[§CA.1 Generalized Functions and Fourier Transforms#^thm-ca-1-7|Theorem §CA.1.7]], [[§B1.2 Lorentz Transformations and the Lorentz Group#^thm-b1-2-2|REL Theorem §B1.2.2]]

> [!remark] Remark: A linear equation becomes algebra
> By rule 2 a linear differential equation with constant coefficients becomes multiplication: the Klein–Gordon operator is multiplication by $m^2 - p^2$, which vanishes exactly on the mass shell. By rule 3 the Green's-function solution of a sourced equation is division by that factor. Both facts, and the trouble that the factor has zeros, are the subject of [[§C2.6 Green's Functions and the Feynman Propagator|§C2.6]]; a free field is a transform supported on the shell ([[§C2.6 Green's Functions and the Feynman Propagator#^thm-c2-6-2|Theorem §C2.6.2]]).
>
> *Source: the user's PHY 513 notes, Ch. 6 §6.3*

^rem-ca-1-2

> [!theorem] Theorem §CA.1.5: Integration by Parts; the Gradient of a Delta Function
> For functions on a region $V$ with outward normal $\hat n$,
>
> $$
> \int_Vd^3x\,(\partial_if)\,g = \oint_{\partial V}dS\,n_i\,f\,g - \int_Vd^3x\,f\,\partial_ig .
> $$
>
> For fields that fall off at infinity, $\int d^3x\,\nabla f\cdot\nabla g = -\int d^3x\,f\,\nabla^2g$, and $\int d^3y\,f(\mathbf y)\,\nabla_{\mathbf y}\delta^3(\mathbf x - \mathbf y) = -\nabla f(\mathbf x)$.
>
> *Source: the user's PHY 513 notes, App. A §A.2 (rule 5), Ch. 4 §4.4*

^thm-ca-1-5

> [!derivation]- Derivation
> **Step 1** (product rule). $\partial_i(fg) = (\partial_if)g + f\,\partial_ig$.
>
> **Step 2** (divergence theorem). Integrate over $V$ and apply [[§17 The Divergence Theorem in Higher Dimensions and Green's Identities#^thm-17-1|452 Thm. §17.1]] to the vector field $fg\,\hat e_i$: $\int_V\partial_i(fg) = \oint_{\partial V}n_ifg$. Rearranging gives the first formula.
>
> **Step 3** (gradients). Take $g \to \partial_ig$ and sum over $i$: $\int_V\nabla f\cdot\nabla g = \oint_{\partial V}f\,\hat n\cdot\nabla g - \int_Vf\nabla^2g$. With $V$ a ball of radius $L \to \infty$, the surface term is dropped when $f\,\partial_rg$ falls off faster than $1/L^2$.
>
> ⚑ By-product: "fields fall off at infinity" is an assumption about the states in which the operators are evaluated (wave packets, not plane waves); it is made every time a surface term is dropped → [[§C2.5 Heisenberg Fields, Two-Point Functions and Causality#^thm-c2-5-2|§C2.5, Theorem §C2.5.2, Step 5]].
>
> **Step 4** (delta function). With $f = \delta^3(\mathbf x - \mathbf y)$ as a function of $\mathbf y$, the surface term vanishes because the delta function is zero on $\partial V$ (its support, the point $\mathbf x$, lies inside); so $\int d^3y\,\delta^3(\mathbf x - \mathbf y)\,\partial_ig(\mathbf y) = -\int d^3y\,\partial_{y^i}\delta^3(\mathbf x - \mathbf y)\,g(\mathbf y)$, i.e. $\int d^3y\,g\,\nabla_{\mathbf y}\delta^3 = -\nabla g(\mathbf x)$. This is also the *definition* of the derivative of $\delta$ ([[§CA.1 Generalized Functions and Fourier Transforms#^def-ca-1-3|Def. §CA.1.3]]).
>
> **What the derivation shows.**
> - Two uses of one move, differing only in which factor kills the surface term: fall-off at infinity, or a delta function supported inside.
> - The four-dimensional version is the step in every Euler–Lagrange and Noether derivation (QFT C1, planned).

^der-ca-1-5

*Uses:* [[§17 The Divergence Theorem in Higher Dimensions and Green's Identities#^thm-17-1|452 Thm. §17.1]], [[§CA.1 Generalized Functions and Fourier Transforms#^def-ca-1-3|Def. §CA.1.3]]

> [!theorem] Theorem §CA.1.6: Angular Integrals
> 1. For a radial $f$ and $r = |\mathbf r|$: $\displaystyle\int d^3p\,f(|\mathbf p|)\,e^{i\mathbf p\cdot\mathbf r} = \frac{4\pi}{r}\int_0^\infty dp\,p\,f(p)\sin(pr)$.
> 2. Without an exponential: $\int d^3p\,p^if(|\mathbf p|) = 0$ and $\int d^3p\,p^ip^jf(|\mathbf p|) = \tfrac13\delta^{ij}\int d^3p\,\mathbf p^2f(|\mathbf p|)$.
> 3. A component under the exponential is a derivative: $p^ie^{i\mathbf p\cdot\mathbf r} = -i\partial_{r^i}e^{i\mathbf p\cdot\mathbf r}$.
>
> *Source: the user's PHY 513 notes, App. A §A.3 (rule 6, Derivation "Angular integrals, from the ground up")*

^thm-ca-1-6

> [!derivation]- Derivation
> **Step 1** (rotate the integration variable). Let $R$ be a rotation with $R\hat z = \hat r$ and substitute $\mathbf p = R\mathbf q$: $|\det R| = 1$, the domain $\mathbb R^3$ is unchanged, $|\mathbf p| = |\mathbf q|$, and $\mathbf p\cdot\mathbf r = \mathbf q\cdot R^{\mathsf T}\mathbf r = rq_z$. The dummy variable is rotated; nothing is done to $\mathbf r$. This is "choose the polar axis along $\mathbf r$".
>
> **Step 2** (spherical coordinates). $\mathbf q = q(\sin\theta\cos\varphi, \sin\theta\sin\varphi, \cos\theta)$ has Jacobian $q^2\sin\theta$, so $d^3q = q^2\sin\theta\,dq\,d\theta\,d\varphi$ ([[§15 Multivariable Integration#^rem-15-5|452 Rem. §15.5]]), and $q_z = q\cos\theta$. The integrand does not depend on $\varphi$: that integral gives $2\pi$.
>
> **Step 3** (the polar angle). Substitute $u = \cos\theta$, $du = -\sin\theta\,d\theta$, which absorbs the $\sin\theta$ of the Jacobian; $\theta: 0 \to \pi$ becomes $u: 1 \to -1$, and the minus sign flips the limits back:
>
> $$
> \int_0^\pi\sin\theta\,e^{iqr\cos\theta}d\theta = \int_{-1}^1e^{iqru}du = \frac{e^{iqr} - e^{-iqr}}{iqr} = \frac{2\sin qr}{qr} .
> $$
>
> **Step 4** (assemble). $\int d^3p\,f\,e^{i\mathbf p\cdot\mathbf r} = 2\pi\int_0^\infty q^2f(q)\frac{2\sin qr}{qr}dq = \frac{4\pi}{r}\int_0^\infty q\,f(q)\sin qr\,dq$. Checks: as $r \to 0$, $\sin(qr)/r \to q$ and the result is $4\pi\int q^2f\,dq$, the full solid angle; with $f \equiv 1$ it must be $(2\pi)^3\delta^3(\mathbf r)$, and $\frac{4\pi}{r}\int_0^\infty q\sin qr\,dq$ indeed vanishes for $r \ne 0$ as a generalized function.
>
> **Step 5** (part 2). $\mathbf p \to -\mathbf p$ (Jacobian 1) maps $\int p^if$ to its negative, so it is $0$. $T^{ij} = \int p^ip^jf$ is symmetric and invariant under every rotation (substitute $\mathbf p = R\mathbf q$: $T = RTR^{\mathsf T}$), hence $T^{ij} = c\,\delta^{ij}$; the trace gives $3c = \int\mathbf p^2f$.
>
> **Step 6** (part 3). $\partial_{r^i}e^{i\mathbf p\cdot\mathbf r} = ip^ie^{i\mathbf p\cdot\mathbf r}$; multiply by $-i$. Under the integral the derivative is moved outside by [[§CA.1 Generalized Functions and Fourier Transforms#^thm-ca-1-1|Theorem §CA.1.1]], 2 (regulated) or by definition (generalized functions).
>
> **What the derivation shows.**
> - A three-dimensional transform of a radial function is a one-dimensional sine transform; the result depends on $\mathbf r$ only through $r$, as rotation invariance requires.
> - The four-dimensional version of the idea is a choice of frame: $\mathbf x = \mathbf y$ for timelike separation, $x^0 = y^0$ for spacelike ([[§C2.5 Heisenberg Fields, Two-Point Functions and Causality#^thm-c2-5-10|Theorem §C2.5.10]], second route; [[§C2.5 Heisenberg Fields, Two-Point Functions and Causality#^thm-c2-5-11|Theorem §C2.5.11]], Step 5).

^der-ca-1-6

*Uses:* [[§15 Multivariable Integration#^rem-15-5|452 Rem. §15.5]], [[§CA.1 Generalized Functions and Fourier Transforms#^thm-ca-1-1|Theorem §CA.1.1]]

## Generalized functions

> [!definition] Definition §CA.1.2: Test Function; Generalized Function; Tempered Distribution
> A **test function** $\varphi$ is smooth and vanishes outside a bounded region. A **generalized function** (distribution) $T$ is a linear map $\varphi \mapsto T[\varphi] \in \mathbb C$ on test functions (continuous in the standard sense, which every map met here is). A locally integrable function $\psi$ defines $T_\psi[\varphi] = \int\psi\varphi$; the **delta function** is the map $\delta[\varphi] = \varphi(0)$. With **Schwartz functions** (smooth, decaying with all derivatives faster than every power) in place of test functions, the maps are **tempered distributions**.
>
> *Source: the user's PHY 513 notes, App. A §A.4, Ch. 6 §6.2 · PHY 513, Problem Set 4, Problem 0*

^def-ca-1-2

> [!remark] Remark: What changes from the working delta function
> [[§B4.4 Fourier Transforms and the Delta Function#^def-b4-4-2|WO Def. §B4.4.2]] and [[§B1.2 The Dirac Delta Function and the Helmholtz Theorem#^def-b1-2-1|EM Def. §B1.2.1]] define $\delta$ by what it does under an integral and realize it as a limit of narrow peaks; the rules were checked one by one with a nascent delta. Here the map *is* the object: $\int dx\,\delta(x)\varphi(x)$ is notation for $\varphi \mapsto \varphi(0)$, chosen so that the formula for $T_\psi$ can be used uniformly. Nothing is lost by the generalization: a test function sharply peaked at $x_0$ with unit integral gives $T_\psi[\varphi] \approx \psi(x_0)$, so $\psi$ is recovered from $T_\psi$; and the generalized functions reach beyond the test functions, since $\varphi \mapsto \int\varphi$ is $T_1$ for the constant $1$. The same move appears in [[§26 Position Eigenstates and Continuous Resolutions#^prop-26-3|556 Prop. §26.3]]: a position "eigenket" is not a vector of the Hilbert space but makes sense paired with one.
>
> *Source: the user's PHY 513 notes, App. A §A.4 (Derivation "Three examples, in order of generality") · PHY 513, Problem Set 4, Problem 0*

^rem-ca-1-3

> [!definition] Definition §CA.1.3: Derivative, Limit and Fourier Transform of a Generalized Function
> Operations are moved onto the test function:
> - *derivative:* $T'[\varphi] \equiv -T[\varphi']$, and $\partial_\mu T[\varphi] \equiv -T[\partial_\mu\varphi]$;
> - *product with a smooth function $g$:* $(gT)[\varphi] \equiv T[g\varphi]$ (two generalized functions cannot in general be multiplied);
> - *limit:* $T_\varepsilon \to T$ means $T_\varepsilon[\varphi] \to T[\varphi]$ for every test function;
> - *Fourier transform* (tempered $T$): $\tilde T[\varphi] \equiv T[\tilde\varphi]$.
>
> *Source: the user's PHY 513 notes, App. A §A.4 (Derivation "Operations are defined by transferring them to the test function")*

^def-ca-1-3

> [!theorem] Theorem §CA.1.7: Every Generalized Function Is Differentiable
> 1. Every generalized function has derivatives of all orders, and for differentiable $\psi$, $(T_\psi)' = T_{\psi'}$.
> 2. $\theta' = \delta$ and $\delta'[\varphi] = -\varphi'(0)$.
> 3. The transform of the constant is a delta function: $\int d^nx\,e^{i\mathbf k\cdot\mathbf x} = (2\pi)^n\delta^n(\mathbf k)$ as tempered distributions.
>
> *Source: the user's PHY 513 notes, App. A §A.4*

^thm-ca-1-7

> [!derivation]- Derivation
> **Step 1** (part 1). $\varphi'$ is again a test function, so $T'[\varphi] = -T[\varphi']$ is defined, and so are all higher derivatives. For differentiable $\psi$, integration by parts gives $\int\psi'\varphi = [\psi\varphi] - \int\psi\varphi'$, and the boundary term vanishes because $\varphi$ is zero outside a bounded region.
>
> **Step 2** ($\theta' = \delta$). $\theta'[\varphi] = -\int_{-\infty}^\infty\theta\varphi' = -\int_0^\infty\varphi' = -[\varphi]_0^\infty = \varphi(0) = \delta[\varphi]$.
>
> ⚑ By-product: the jump of a step function is a delta function; this is the jump that makes the retarded function a Green's function ([[§C2.6 Green's Functions and the Feynman Propagator#^thm-c2-6-4|Theorem §C2.6.4]], Step 6) and the contact term of time ordering ([[§C2.6 Green's Functions and the Feynman Propagator#^thm-c2-6-5|Theorem §C2.6.5]], 4).
>
> **Step 3** ($\delta'$). $\delta'[\varphi] = -\delta[\varphi'] = -\varphi'(0)$, which is the rule of [[§CA.1 Generalized Functions and Fourier Transforms#^thm-ca-1-5|Theorem §CA.1.5]], Step 4, seen as a definition.
>
> **Step 4** (part 3). For a Schwartz function $\varphi(\mathbf k)$, the pairing is $\int d^nk\,\varphi(\mathbf k)\int d^nx\,e^{i\mathbf k\cdot\mathbf x} \equiv \int d^nx\,\hat\varphi(\mathbf x)$ with $\hat\varphi(\mathbf x) = \int d^nk\,\varphi(\mathbf k)e^{i\mathbf k\cdot\mathbf x}$, the order that converges. By Fourier inversion ([[§B4.4 Fourier Transforms and the Delta Function#^thm-b4-4-1|WO Theorem §B4.4.1]], rewritten in the convention of Def. §CA.1.1), $\int d^nx\,\hat\varphi(\mathbf x) = (2\pi)^n\varphi(\mathbf 0)$, which is $(2\pi)^n\delta^n[\varphi]$. A Gaussian convergence factor makes the same statement concrete ([[§B4.4 Fourier Transforms and the Delta Function#^thm-b4-4-3|WO Theorem §B4.4.3]], 4).
>
> **What the derivation shows.**
> - Rules that look like tricks ($\theta' = \delta$, $\int e^{ikx} = 2\pi\delta$) are definitions plus one integration by parts or one inversion.

^der-ca-1-7

*Uses:* [[§CA.1 Generalized Functions and Fourier Transforms#^def-ca-1-3|Def. §CA.1.3]], [[§B4.4 Fourier Transforms and the Delta Function#^thm-b4-4-1|WO Theorem §B4.4.1]], [[§B4.4 Fourier Transforms and the Delta Function#^thm-b4-4-3|WO Theorem §B4.4.3]]

> [!remark] Remark: What the language buys in field theory
> - *A Green's function is a linear map.* The sources of physics, smooth and of finite duration, are test functions, and $\phi = i\int D_C\,j$ defines the map $j \mapsto \phi$; "$D_C(x - y)$" is the kernel through which it is written, not a function with values. There is one such map per boundary condition ([[§C2.6 Green's Functions and the Feynman Propagator#^def-c2-6-1|Def. §C2.6.1]]).
> - *Integrals that converge nowhere still define objects.* $\int d^3p\,e^{-ip\cdot\xi}/2E_{\mathbf p}$ converges for no real $\xi$, yet it is a tempered distribution, the boundary value of an analytic function ([[§C2.5 Heisenberg Fields, Two-Point Functions and Causality#^thm-c2-5-7|Theorem §C2.5.7]]).
> - *Products at a point are undefined.* The field is an operator-valued distribution, $\phi[f] = \int d^4x\,f(x)\phi(x)$, and $\phi(x)^2$ is a product of distributions at one point. That is the origin of the $\delta^3(0)$ in the zero-point energy and of normal ordering ([[§C2.2 The Real Scalar Field#^def-c2-2-2|Def. §C2.2.2]]), and later of every ultraviolet divergence.
>
> *Source: the user's PHY 513 notes, Ch. 6 §6.2, App. A §A.4 · PHY 513, Problem Set 4, Problem 0*

^rem-ca-1-4

## The principal value and the Sokhotski–Plemelj formula

> [!definition] Definition §CA.1.4: Principal Value
> For a test function $\varphi$ vanishing outside $[-L, L]$,
>
> $$
> \mathcal P\!\!\int\frac{\varphi(s)}{s}\,ds \equiv \lim_{\delta\to0^+}\Bigl(\int_{-\infty}^{-\delta} + \int_\delta^\infty\Bigr)\frac{\varphi(s)}{s}\,ds = \int_{-L}^{L}\frac{\varphi(s) - \varphi(0)}{s}\,ds .
> $$
>
> The generalized function $\mathcal P\frac1s$ so defined is real and odd and acts as $1/s$ away from $s = 0$.
>
> *Source: the user's PHY 513 notes, App. A §A.5 (Definition "The principal value")*

^def-ca-1-4

> [!theorem] Theorem §CA.1.8: Sokhotski–Plemelj Formula
> As generalized functions, for $\varepsilon \to 0^+$,
>
> $$
> \frac{1}{x - x_0 \pm i\varepsilon} \longrightarrow \mathcal P\frac{1}{x - x_0} \mp i\pi\,\delta(x - x_0) .
> $$
>
> Mnemonic: the pole of $1/(x - x_0 - i\varepsilon)$ lies *above* the real path and gives $+i\pi$; a pole below gives $-i\pi$.
>
> *Source: the user's PHY 513 notes, App. A §A.5, eq. (SP) and Derivation "The Sokhotski–Plemelj formula, derived directly" · PHY 513, Problem Set 4, eq. (11)*

^thm-ca-1-8

> [!derivation]- Derivation
> Take the lower sign with $s = x - x_0$; the upper sign is the complex conjugate. Let $\varphi$ be a test function vanishing outside $[-L, L]$.
>
> **Step 1** (split at finite $\varepsilon$). Multiply numerator and denominator by $s + i\varepsilon$:
>
> $$
> \frac{1}{s - i\varepsilon} = \frac{s + i\varepsilon}{s^2 + \varepsilon^2} = \underbrace{\frac{s}{s^2 + \varepsilon^2}}_{\text{real, odd}} + i\,\underbrace{\frac{\varepsilon}{s^2 + \varepsilon^2}}_{\text{real, even}} .
> $$
>
> Both pieces are bounded for $\varepsilon > 0$, but neither has a pointwise limit at $s = 0$, where both are of order $1/\varepsilon$.
>
> **Step 2** (imaginary part: substitute). With $s = \varepsilon u$, $ds = \varepsilon\,du$: $\int\varphi(s)\frac{\varepsilon\,ds}{s^2 + \varepsilon^2} = \int\varphi(\varepsilon u)\frac{du}{1 + u^2}$.
>
> **Step 3** (imaginary part: limit). $\varphi(\varepsilon u) \to \varphi(0)$ for every $u$, and $|\varphi(\varepsilon u)|/(1 + u^2) \le \sup|\varphi|/(1 + u^2)$, integrable and independent of $\varepsilon$. By dominated convergence ([[§CA.1 Generalized Functions and Fourier Transforms#^thm-ca-1-1|Theorem §CA.1.1]]) the integral tends to $\varphi(0)\int\frac{du}{1 + u^2} = \pi\varphi(0)$ ([[§CA.2 Contour Integration#^ex-ca-2-1|Example §CA.2.1]]). So $\frac{\varepsilon}{s^2 + \varepsilon^2} \to \pi\delta(s)$: the Lorentzian is a nascent delta function of area $\pi$.
>
> **Step 4** (real part: subtract $\varphi(0)$). On $[-L, L]$, $\int_{-L}^L\varphi(0)\frac{s\,ds}{s^2 + \varepsilon^2} = 0$ by oddness, so
>
> $$
> \int_{-L}^{L}\varphi(s)\frac{s\,ds}{s^2 + \varepsilon^2} = \int_{-L}^{L}\frac{\varphi(s) - \varphi(0)}{s}\cdot\frac{s^2}{s^2 + \varepsilon^2}\,ds .
> $$
>
> **Step 5** (real part: limit). The difference quotient $[\varphi(s) - \varphi(0)]/s$ is bounded (by $\sup|\varphi'|$), and $0 \le s^2/(s^2 + \varepsilon^2) \le 1$ tends to $1$ for every $s \ne 0$. By dominated convergence the integral tends to $\int_{-L}^L\frac{\varphi(s) - \varphi(0)}{s}ds = \mathcal P\!\int\frac{\varphi}{s}$ ([[§CA.1 Generalized Functions and Fourier Transforms#^def-ca-1-4|Def. §CA.1.4]]).
>
> ⚑ By-product: the subtraction of $\varphi(0)$ must be done on a bounded symmetric interval. The user's notes write these integrals over all of $\mathbb R$, where the subtracted $\varphi(0)/s$ is not integrable at infinity and would need a symmetric limit there as well; the bounded interval is the safe form.
>
> **Step 6** (assemble). $\frac{1}{s - i\varepsilon} \to \mathcal P\frac1s + i\pi\delta(s)$, the lower sign of the formula; conjugating gives the upper.
>
> **What the derivation shows.**
> - The real part is the principal value and the imaginary part the delta function, and nothing else enters; a smooth symmetric cutoff gives the same answer as the sharp one in the definition.
> - The factor $\pi$ is the area of the Lorentzian, the same $\pi$ that $\int du/(1 + u^2)$ gives by residues.
> - Used in: the massless commutator ([[§C2.5 Heisenberg Fields, Two-Point Functions and Causality#^thm-c2-5-17|Theorem §C2.5.17]]), the differences of Green's functions on the shell ([[§C2.6 Green's Functions and the Feynman Propagator#^thm-c2-6-10|Theorem §C2.6.10]]), the principal function ([[§C2.6 Green's Functions and the Feynman Propagator#^thm-c2-6-15|Theorem §C2.6.15]]).

^der-ca-1-8

*Uses:* [[§CA.1 Generalized Functions and Fourier Transforms#^thm-ca-1-1|Theorem §CA.1.1]], [[§CA.1 Generalized Functions and Fourier Transforms#^def-ca-1-4|Def. §CA.1.4]], [[§CA.2 Contour Integration#^ex-ca-2-1|Example §CA.2.1]]

> [!derivation]- Derivation (second route: the half-residue lemma)
> **Step 1.** For integrands $f = g/(x - x_0)$ with $g$ analytic near $x_0$ (every propagator integrand is of this kind), a small semicircle passing above the pole gives $\mathcal P\!\int f - i\pi g(x_0)$ and one passing below gives $\mathcal P\!\int f + i\pi g(x_0)$ ([[§CA.2 Contour Integration#^thm-ca-2-7|Theorem §CA.2.7]]).
>
> **Step 2.** By Cauchy's theorem ([[§CA.2 Contour Integration#^thm-ca-2-2|Theorem §CA.2.2]]), keeping the path on the real axis with the pole moved down to $x_0 - i\varepsilon$, i.e. the denominator $x - x_0 + i\varepsilon$, equals passing above the pole: the upper sign, $\mathcal P - i\pi\delta$. Moving the pole up gives the lower sign.
>
> **What the derivation shows.**
> - The two prescriptions differ by a full loop, $2\pi i\,g(x_0)$, and the principal value is their average. This route needs analyticity of $g$; the direct route works for every test function.
>
> *Source: the user's PHY 513 notes, App. A §A.5 (Derivation "The half-residue lemma")*

*Uses:* [[§CA.2 Contour Integration#^thm-ca-2-7|Theorem §CA.2.7]], [[§CA.2 Contour Integration#^thm-ca-2-2|Theorem §CA.2.2]]

> [!caution] Caution: What the formula does and does not say
> Pointwise it is empty: at $x \ne x_0$, $\delta = 0$ and $\mathcal P\frac{1}{x - x_0}$ acts as $\frac{1}{x - x_0}$, so it reads $\frac{1}{x - x_0} = \frac{1}{x - x_0}$. Its whole content sits at $x = x_0$, where $\frac{1}{s \mp i\varepsilon} \sim \pm\frac{i}{\varepsilon}$ has no value; what it specifies is what that divergence does under an integral. So an $i\varepsilon$ expression may be evaluated at $\varepsilon = 0$ wherever its denominator does not vanish, and the formula is needed only where it does.
>
> *Source: the user's PHY 513 notes, App. A §A.5 (Caution "What the formula does and does not say")*

^cau-ca-1-2

> [!remark]- Connections
> - The imaginary part of Sokhotski–Plemelj is the Lorentzian nascent delta function of [[§B4.4 Fourier Transforms and the Delta Function#^def-b4-4-2|WO Def. §B4.4.2]]; the same Lorentzian is the line shape of a ringing oscillator ([[§B4.4 Fourier Transforms and the Delta Function#^ex-b4-4-1|WO Example §B4.4.1]]), whose width is the $\varepsilon$ that a damped mode carries.
> - Sokhotski–Plemelj was used inline before it had a home: the level shift (principal value) and decay rate ($-i\pi\delta$, Fermi's golden rule) of [[§C9.6 The Interaction Picture and the Atom–Field Interaction|QM §C9.6]], and the imaginary part of the resolvent behind the optical theorem in [[§C10.2 The Eikonal Approximation and the Optical Theorem|QM §C10.2]]. In field theory it gives the differences of Green's functions on the mass shell ([[§C2.6 Green's Functions and the Feynman Propagator#^thm-c2-6-10|Theorem §C2.6.10]]) and the massless commutator function ([[§C2.5 Heisenberg Fields, Two-Point Functions and Causality#^thm-c2-5-17|Theorem §C2.5.17]]).
> - Distributions as linear maps on test functions are a dual space: the generalized functions sit in the dual of the test functions as kets sit in the dual of bras; the position "eigenket" that is not a vector is the same phenomenon ([[§26 Position Eigenstates and Continuous Resolutions#^prop-26-3|556 Prop. §26.3]]).
> - The composition rule $\delta(f(x)) = \sum_i\delta(x - x_i)/|f'(x_i)|$ ([[§B1.2 The Dirac Delta Function and the Helmholtz Theorem#^thm-b1-2-1|EM Theorem §B1.2.1]]) is what turns $\theta(p^0)\delta(p^2 - m^2)$ into the invariant measure $d^3p/2E_{\mathbf p}$ ([[§C2.2 The Real Scalar Field#^def-c2-2-3|Def. §C2.2.3]]) and $\delta(t^2 - r^2)$ into the light-cone deltas of the massless commutator.
> - The angular integral is the first step of every position-space propagator: the Wightman function ([[§C2.5 Heisenberg Fields, Two-Point Functions and Causality#^thm-c2-5-10|Theorem §C2.5.10]]), the scattering Green's function $-e^{ik\rho}/4\pi\rho$ ([[§C10.1 The Lippmann–Schwinger Equation and the Born Approximation#^thm-c10-1-3|QM Theorem §C10.1.3]]) and the Yukawa potential ([[§B4.1 The Klein–Gordon Equation#^rem-b4-1-4|REL Remark: Static solutions and the Yukawa potential]]).
> - Integration by parts with a delta function is how $[\pi, H]$ acquires $\nabla^2\phi$ ([[§C2.5 Heisenberg Fields, Two-Point Functions and Causality#^thm-c2-5-2|Theorem §C2.5.2]]); the divergence theorem behind it is [[§17 The Divergence Theorem in Higher Dimensions and Green's Identities#^thm-17-1|452 Thm. §17.1]], and the four-dimensional version is the step in every Euler–Lagrange and Noether derivation (QFT C1, planned).
