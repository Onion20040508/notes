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
> 1 is [[§15 The General Lebesgue Integral#^thm-15-8|551 Thm. §15.8]]. For 2, the mean value theorem ([[§29 The Mean Value Theorem#^thm-29-3|451 Thm. §29.3]]) writes the difference quotient $[f(p, r + h) - f(p, r)]/h$ as $\partial_rf(p, r^*)$ at an intermediate point, bounded by $g(p)$ independently of $h$; apply 1 to a sequence $h_n \to 0$. The dominating function must not depend on $n$ (or $h$): that is the whole content.

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
> *1* (for $g$ continuously differentiable, which covers every use here; the general case uses the second mean value theorem). With $H(P) = \int_0^Ph$, integration by parts gives $\int_0^Pg\,h = g(P)H(P) - \int_0^Pg'(p)H(p)\,dp$. The first term tends to $0$ since $|H| \le M$ and $g \to 0$. In the second, $|g'H| \le -Mg'$ and $\int_0^\infty(-g') = g(0)$, so it converges absolutely.
>
> *2.* Let $R(p) = \int_p^\infty f$; it is bounded and tends to $0$, and $f = -R'$. Integrating by parts, $\int_0^\infty e^{-\varepsilon p}f\,dp = R(0) - \varepsilon\int_0^\infty e^{-\varepsilon p}R(p)\,dp$. Split the last integral at $P$: the piece $[0, P]$ is at most $\varepsilon P\sup|R|$, the piece $[P, \infty)$ at most $\sup_{p > P}|R|$. Choose $P$ large, then $\varepsilon$ small.

^der-ca-1-2

> [!theorem] Theorem §CA.1.3: Limits of Derivatives
> Let $F_n$ be differentiable on an interval, let $F_n(r_0)$ converge at one point, and let $F_n' \to G$ *uniformly* on the interval. Then $F_n \to F$ uniformly and $F' = G$. Pointwise convergence of the derivatives is not enough.
>
> *Source: the user's PHY 513 notes, App. A §A.1 (theorem 5), citing Rudin, Theorem 7.17*

^thm-ca-1-3

> [!derivation]- Derivation
> For continuous $F_n'$ (the case used here; Rudin's proof removes it): $F_n(r) = F_n(r_0) + \int_{r_0}^rF_n'$ ([[§34 Fundamental Theorem of Calculus#^thm-34-1|451 Thm. §34.1]]) converges uniformly on bounded intervals to $F(r) = F(r_0) + \int_{r_0}^rG$, and $G$ is continuous as a uniform limit of continuous functions, so $F' = G$ ([[§34 Fundamental Theorem of Calculus#^thm-34-4|451 Thm. §34.4]]). Counterexample to the pointwise version: $F_n = \sin(nr)/\sqrt n$ tends to $0$ uniformly while $F_n'(0) = \sqrt n$ diverges.

^der-ca-1-3

*Uses:* [[§34 Fundamental Theorem of Calculus#^thm-34-1|451 Thm. §34.1]], [[§34 Fundamental Theorem of Calculus#^thm-34-4|451 Thm. §34.4]]

> [!remark] Remark: Where each exchange is used, and where none applies
> Leibniz whenever $\partial_r$ or $\partial_t$ is taken inside a regulated integral; Dirichlet and Abel when a regulator is removed from a conditionally convergent integral; uniform convergence of derivatives in the real-variable evaluation of the Wightman function ([[§C2.5 Heisenberg Fields, Two-Point Functions and Causality#^thm-c2-5-7|Theorem §C2.5.7]], third route), where a limit and a derivative must be exchanged; dominated convergence in the Sokhotski–Plemelj formula below. Integrals that do not converge even conditionally, such as $\int d^3p/E_{\mathbf p}$, are covered by none of these. They are defined as generalized functions (Def. §CA.1.2 below), and there the exchanges hold by definition.
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
> *1.* The product of three or four one-dimensional identities $\int ds\,e^{iks} = 2\pi\delta(k)$ ([[§B4.4 Fourier Transforms and the Delta Function#^thm-b4-4-3|WO Theorem §B4.4.3]], 4); the sign in the exponent is irrelevant for a delta function. Inserting the synthesis into the analysis formula and using the identity returns $\tilde f$, which is inversion; as a statement about integrals against test functions it is [[§CA.1 Generalized Functions and Fourier Transforms#^thm-ca-1-7|Theorem §CA.1.7]], 3.
>
> *2.* $\partial_0e^{-ip\cdot x} = -ip^0e^{-ip\cdot x} = -ip_0e^{-ip\cdot x}$, and $\partial_ie^{+i\mathbf p\cdot\mathbf x} = ip^ie^{i\mathbf p\cdot\mathbf x} = -ip_ie^{i\mathbf p\cdot\mathbf x}$: the opposite signs in the phase are what let one formula cover all four components. Then $\partial^2 = \partial_\mu\partial^\mu \to (-ip_\mu)(-ip^\mu) = -p^2$.
>
> *3.* $\tilde h(p) = \int d^4x\,e^{ip\cdot x}\int d^4y\,D(x - y)j(y) = \int d^4y\,e^{ip\cdot y}j(y)\int d^4u\,e^{ip\cdot u}D(u)$ with $u = x - y$.
>
> *4.* Conjugate $\tilde f(p) = \int d^4x\,f\,e^{ip\cdot x}$. For a scalar, $f(\Lambda^{-1}x) = f(x)$; substitute $x \to \Lambda x$, using $|\det\Lambda| = 1$ and $(\Lambda x)\cdot(\Lambda p) = x\cdot p$ ([[§B1.2 Lorentz Transformations and the Lorentz Group#^thm-b1-2-2|REL Theorem §B1.2.2]]), to get $\tilde f(\Lambda p) = \tilde f(p)$.

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
> Integrate the product rule $\partial_i(fg) = (\partial_if)g + f\partial_ig$ over $V$ and apply the divergence theorem ([[§17 The Divergence Theorem in Higher Dimensions and Green's Identities#^thm-17-1|452 Thm. §17.1]]) to the vector field $fg\,\hat e_i$. The surface term vanishes for fields that fall off at infinity, or when one factor is a delta function whose support lies inside $V$. Contracting the index with $\partial_ig$ gives the second form; with $f = \delta^3(\mathbf x - \mathbf y)$ as a function of $\mathbf y$ it gives the third, which is also the *definition* of the derivative of $\delta$ ([[§CA.1 Generalized Functions and Fourier Transforms#^def-ca-1-3|Def. §CA.1.3]]). The strategy in practice: move the derivative to the factor where it is wanted, then argue the surface term away.

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
> *1.* Substitute $\mathbf p = R\mathbf q$ with $R$ a rotation taking $\hat z$ to $\hat r$: the measure, the domain and $|\mathbf p|$ are unchanged, and $\mathbf p\cdot\mathbf r = rq_z$. The dummy variable is rotated; nothing is done to $\mathbf r$. In spherical coordinates $d^3q = q^2\sin\theta\,dq\,d\theta\,d\varphi$ ([[§15 Multivariable Integration#^rem-15-5|452 Rem. §15.5]]); the $\varphi$ integral gives $2\pi$, and $u = \cos\theta$ absorbs the $\sin\theta$ of the Jacobian:
>
> $$
> \int_0^\pi\sin\theta\,e^{iqr\cos\theta}\,d\theta = \int_{-1}^1e^{iqru}\,du = \frac{2\sin qr}{qr} .
> $$
>
> Checks: at $r \to 0$ the result is $4\pi\int p^2f\,dp$, the full solid angle; with $f \equiv 1$ it must be $(2\pi)^3\delta^3(\mathbf r)$, and $\frac{4\pi}{r}\int_0^\infty p\sin pr\,dp$ vanishes for $r \ne 0$ by oscillation.
>
> *2.* $\mathbf p \to -\mathbf p$ shows the first vanishes. The second is a rotation-invariant symmetric tensor, hence $c\,\delta^{ij}$, and the trace fixes $3c = \int\mathbf p^2f$.
>
> *3.* Differentiate under the integral; this is how a non-decaying factor $p$ is moved outside an integral ([[§C2.5 Heisenberg Fields, Two-Point Functions and Causality#^thm-c2-5-7|Theorem §C2.5.7]], second route). The four-dimensional version of the idea is to choose the frame that simplifies $p\cdot x$: $\mathbf x = \mathbf y$ for timelike separation, $x^0 = y^0$ for spacelike.

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
> *1.* $\varphi'$ is again a test function, so $T'$ is defined, and so are its derivatives. For differentiable $\psi$, integration by parts with no boundary term (the test function vanishes outside a bounded region) gives $\int\psi'\varphi = -\int\psi\varphi'$.
>
> *2.* $\theta'[\varphi] = -\int_0^\infty\varphi'\,dx = \varphi(0)$, the jump that makes the retarded function a Green's function ([[§C2.6 Green's Functions and the Feynman Propagator#^thm-c2-6-4|Theorem §C2.6.4]]). $\delta'[\varphi] = -\delta[\varphi'] = -\varphi'(0)$, which is the rule of [[§CA.1 Generalized Functions and Fourier Transforms#^thm-ca-1-5|Theorem §CA.1.5]] seen as a definition.
>
> *3.* For a Schwartz function $\varphi$, $\tilde 1[\varphi] = \int d^nk\,\varphi(\mathbf k)\int d^nx\,e^{i\mathbf k\cdot\mathbf x}$ means $\int d^nx\,\hat\varphi(\mathbf x)$ with $\hat\varphi$ the transform of $\varphi$, which by Fourier inversion ([[§B4.4 Fourier Transforms and the Delta Function#^thm-b4-4-1|WO Theorem §B4.4.1]], rewritten in the convention of Def. §CA.1.1) equals $(2\pi)^n\varphi(\mathbf 0)$. A Gaussian convergence factor makes the same statement concrete ([[§B4.4 Fourier Transforms and the Delta Function#^thm-b4-4-3|WO Theorem §B4.4.3]], 4).

^der-ca-1-7

*Uses:* [[§CA.1 Generalized Functions and Fourier Transforms#^def-ca-1-3|Def. §CA.1.3]], [[§B4.4 Fourier Transforms and the Delta Function#^thm-b4-4-1|WO Theorem §B4.4.1]], [[§B4.4 Fourier Transforms and the Delta Function#^thm-b4-4-3|WO Theorem §B4.4.3]]

> [!remark] Remark: What the language buys in field theory
> - *A Green's function is a linear map.* The sources of physics, smooth and of finite duration, are test functions, and $\phi = i\int D_C\,j$ defines the map $j \mapsto \phi$; "$D_C(x - y)$" is the kernel through which it is written, not a function with values. There is one such map per boundary condition ([[§C2.6 Green's Functions and the Feynman Propagator#^def-c2-6-1|Def. §C2.6.1]]).
> - *Integrals that converge nowhere still define objects.* $\int d^3p\,e^{-ip\cdot\xi}/2E_{\mathbf p}$ converges for no real $\xi$, yet it is a tempered distribution, the boundary value of an analytic function ([[§C2.5 Heisenberg Fields, Two-Point Functions and Causality#^thm-c2-5-5|Theorem §C2.5.5]]).
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
> Take the lower sign, with $s = x - x_0$; the other is the complex conjugate. At finite $\varepsilon$,
>
> $$
> \frac{1}{s - i\varepsilon} = \underbrace{\frac{s}{s^2 + \varepsilon^2}}_{\text{real, odd}} + i\,\underbrace{\frac{\varepsilon}{s^2 + \varepsilon^2}}_{\text{real, even}} ,
> $$
>
> and neither piece has a pointwise limit at $s = 0$. Test against $\varphi$.
>
> *Imaginary part.* Substituting $s = \varepsilon x$, $\int\varphi(s)\frac{\varepsilon\,ds}{s^2 + \varepsilon^2} = \int\varphi(\varepsilon x)\frac{dx}{1 + x^2} \to \pi\varphi(0)$ by dominated convergence ([[§CA.1 Generalized Functions and Fourier Transforms#^thm-ca-1-1|Theorem §CA.1.1]]; $\varphi$ is bounded and $1/(1 + x^2)$ integrable), with $\int dx/(1 + x^2) = \pi$ ([[§CA.2 Contour Integration#^ex-ca-2-1|Example §CA.2.1]]). The Lorentzian is a nascent delta function of area $\pi$.
>
> *Real part.* On $[-L, L] \supset \operatorname{supp}\varphi$, oddness lets $\varphi(0)$ be subtracted for free:
>
> $$
> \int_{-L}^{L}\varphi(s)\frac{s\,ds}{s^2 + \varepsilon^2} = \int_{-L}^{L}\frac{\varphi(s) - \varphi(0)}{s}\cdot\frac{s^2}{s^2 + \varepsilon^2}\,ds \longrightarrow \int_{-L}^{L}\frac{\varphi(s) - \varphi(0)}{s}\,ds ,
> $$
>
> by dominated convergence, since the difference quotient is bounded and $0 \le s^2/(s^2 + \varepsilon^2) \le 1$ tends to $1$ except at one point. This is [[§CA.1 Generalized Functions and Fourier Transforms#^def-ca-1-4|Def. §CA.1.4]]: a smooth symmetric cutoff gives the same answer as the sharp one. (The user's notes write these integrals over all of $\mathbb R$; the subtracted $\varphi(0)/s$ then needs a symmetric limit at infinity as well, so the bounded interval is the safe form.)

^der-ca-1-8

*Uses:* [[§CA.1 Generalized Functions and Fourier Transforms#^thm-ca-1-1|Theorem §CA.1.1]], [[§CA.1 Generalized Functions and Fourier Transforms#^def-ca-1-4|Def. §CA.1.4]], [[§CA.2 Contour Integration#^ex-ca-2-1|Example §CA.2.1]]

> [!derivation]- Derivation (second route: the half-residue lemma)
> For integrands $f = g/(x - x_0)$ with $g$ analytic near $x_0$ (every propagator integrand is of this kind), passing above the pole along a small semicircle gives $\mathcal P\!\int f - i\pi g(x_0)$ and passing below gives $\mathcal P\!\int f + i\pi g(x_0)$ ([[§CA.2 Contour Integration#^thm-ca-2-7|Theorem §CA.2.7]]). By Cauchy's theorem, passing above a pole at $x_0$ is the same as keeping the path on the real axis and moving the pole down to $x_0 - i\varepsilon$, i.e. using the denominator $x - x_0 + i\varepsilon$; this gives the upper sign, and passing below gives the lower. The two prescriptions differ by a full loop, $2\pi i\,g(x_0)$, and the principal value is their average.
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
> - Sokhotski–Plemelj was used inline before it had a home: the level shift (principal value) and decay rate ($-i\pi\delta$, Fermi's golden rule) of [[§C9.6 The Interaction Picture and the Atom–Field Interaction|QM §C9.6]], and the imaginary part of the resolvent behind the optical theorem in [[§C10.2 The Eikonal Approximation and the Optical Theorem|QM §C10.2]]. In field theory it gives the differences of Green's functions on the mass shell ([[§C2.6 Green's Functions and the Feynman Propagator#^thm-c2-6-10|Theorem §C2.6.10]]) and the massless commutator function ([[§C2.5 Heisenberg Fields, Two-Point Functions and Causality#^thm-c2-5-11|Theorem §C2.5.11]]).
> - Distributions as linear maps on test functions are a dual space: the generalized functions sit in the dual of the test functions as kets sit in the dual of bras; the position "eigenket" that is not a vector is the same phenomenon ([[§26 Position Eigenstates and Continuous Resolutions#^prop-26-3|556 Prop. §26.3]]).
> - The composition rule $\delta(f(x)) = \sum_i\delta(x - x_i)/|f'(x_i)|$ ([[§B1.2 The Dirac Delta Function and the Helmholtz Theorem#^thm-b1-2-1|EM Theorem §B1.2.1]]) is what turns $\theta(p^0)\delta(p^2 - m^2)$ into the invariant measure $d^3p/2E_{\mathbf p}$ ([[§C2.2 The Real Scalar Field#^def-c2-2-3|Def. §C2.2.3]]) and $\delta(t^2 - r^2)$ into the light-cone deltas of the massless commutator.
> - The angular integral is the first step of every position-space propagator: the Wightman function ([[§C2.5 Heisenberg Fields, Two-Point Functions and Causality#^thm-c2-5-7|Theorem §C2.5.7]]), the scattering Green's function $-e^{ik\rho}/4\pi\rho$ ([[§C10.1 The Lippmann–Schwinger Equation and the Born Approximation#^thm-c10-1-3|QM Theorem §C10.1.3]]) and the Yukawa potential ([[§B4.1 The Klein–Gordon Equation#^rem-b4-1-4|REL Remark: Static solutions and the Yukawa potential]]).
> - Integration by parts with a delta function is how $[\pi, H]$ acquires $\nabla^2\phi$ ([[§C2.5 Heisenberg Fields, Two-Point Functions and Causality#^thm-c2-5-2|Theorem §C2.5.2]]); the divergence theorem behind it is [[§17 The Divergence Theorem in Higher Dimensions and Green's Identities#^thm-17-1|452 Thm. §17.1]], and the four-dimensional version is the step in every Euler–Lagrange and Noether derivation (QFT C1, planned).
