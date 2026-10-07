---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C2b
section: C2b.2
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C2b.1 Heisenberg Fields]] · ↑ [[· C2b Two-Point Functions, Causality and Propagators]] · [[§C2b.3 Explicit Forms of the Wightman Function]] →

*Sources: the user's PHY 513 notes, Ch. 5 §§5.4–5.5 and Ch. 6 §6.9 · PHY 513 Lecture 5 (Larsen, 16 Sep 2026; no slides, reconstructed in the user's notes) · Peskin & Schroeder §2.4, p. 27 · PHY 513, Problem Set 4, Problems 2(a) and 4(a)–(b).*

How are the values of the free field at two spacetime points correlated in the vacuum? The answer is a function, the vacuum two-point function $D_W$, built from the Heisenberg field of [[§C2b.1 Heisenberg Fields|§C2b.1]] ([[§C2b.1 Heisenberg Fields#^thm-c2b-1-4|Theorem §C2b.1.4]]); whether the theory is causal turns on it. This section defines it, writes it as a Lorentz-invariant mode integral that solves the Klein–Gordon equation, and shows that it is the boundary value of an analytic function. Its explicit forms are [[§C2b.3 Explicit Forms of the Wightman Function|§C2b.3]], and its antisymmetric part, the commutator function, is [[§C2b.4 Microcausality and the Commutator Function|§C2b.4]].

*Conventions* ([[Larsen PHY 513]]): $\hbar = c = 1$, $g = \operatorname{diag}(+, -, -, -)$, $E_{\mathbf p} = \sqrt{\mathbf p^2 + m^2}$, $p\cdot x = E_{\mathbf p}t - \mathbf p\cdot\mathbf x$ whenever $p$ is on shell, $[\hat a_{\mathbf p}, \hat a_{\mathbf q}^\dagger] = (2\pi)^3\delta^3(\mathbf p - \mathbf q)$, $|\mathbf p\rangle = \sqrt{2E_{\mathbf p}}\,\hat a_{\mathbf p}^\dagger|0\rangle$. Lecture 5 writes $\omega_{\mathbf p}$ for $E_{\mathbf p}$ ([[§C2a.1 Canonical Quantization of Fields#^cau-c2a-1-1|Caution: Eₚ, not ωₚ; π, not Π]]). Unless stated otherwise $m > 0$; the massless case is stated separately where it differs.

## The Wightman function

> [!definition] Definition §C2b.2.1: Wightman Function
> The **Wightman function** of the free field is the vacuum expectation value
>
> $$
> D_W(x - y) \equiv \langle0|\hat\phi(x)\hat\phi(y)|0\rangle ,
> $$
>
> the amplitude for a quantum created at $y$ to be found at $x$. Peskin & Schroeder call it $D(x - y)$.
>
> *Source: the user's PHY 513 notes, Ch. 5 §5.4 · PS §2.4, eq. (2.50) · PHY 513, Problem Set 4, eq. (8)*

^def-c2b-2-1

> [!theorem] Theorem §C2b.2.1: The Wightman Function as a Mode Integral
> With $\xi = x - y$ and $p^0 = E_{\mathbf p}$, the Wightman function depends on $x$ and $y$ only through $\xi$, and
>
> $$
> D_W(\xi) = \int\frac{d^3p}{(2\pi)^3\,2E_{\mathbf p}}\,e^{-ip\cdot\xi} = \int\frac{d^4p}{(2\pi)^4}\,2\pi\,\theta(p^0)\,\delta(p^2 - m^2)\,e^{-ip\cdot\xi} :
> $$
>
> the Fourier transform of the positive-energy mass shell. The integral converges absolutely for no real $\xi$; the formula is an identity of tempered distributions ([[§C2b.2 The Wightman Function#^thm-c2b-2-2|Theorem §C2b.2.2]]).
>
> *Source: the user's PHY 513 notes, Ch. 5 §5.4 (Derivation "Computing $D_W$"), Ch. 6 §6.9 · PS §2.4, eq. (2.50) · PHY 513, Problem Set 4, Problem 4(a)*

^thm-c2b-2-1

> [!derivation]- Derivation
> **Step 1** (two fields, two names). By [[§C2b.1 Heisenberg Fields#^thm-c2b-1-4|Theorem §C2b.1.4]] (a product of two operator-valued distributions at different points: read it smeared, $\hat\phi(f)\hat\phi(g)$, [[§C2b.1 Heisenberg Fields#^thm-c2b-1-6|Theorem §C2b.1.6]]),
>
> $$
> \hat\phi(x)\hat\phi(y) = \int\frac{d^3p}{(2\pi)^3}\frac{d^3q}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}\sqrt{2E_{\mathbf q}}}\Bigl(\hat a_{\mathbf p}e^{-ip\cdot x} + \hat a_{\mathbf p}^\dagger e^{ip\cdot x}\Bigr)\Bigl(\hat a_{\mathbf q}e^{-iq\cdot y} + \hat a_{\mathbf q}^\dagger e^{iq\cdot y}\Bigr).
> $$
>
> **Step 2** (all four terms). The product of the brackets is $\hat a_{\mathbf p}\hat a_{\mathbf q}\,e^{-ip\cdot x - iq\cdot y} + \hat a_{\mathbf p}\hat a_{\mathbf q}^\dagger\,e^{-ip\cdot x + iq\cdot y} + \hat a_{\mathbf p}^\dagger \hat a_{\mathbf q}\,e^{ip\cdot x - iq\cdot y} + \hat a_{\mathbf p}^\dagger \hat a_{\mathbf q}^\dagger\,e^{ip\cdot x + iq\cdot y}$.
>
> **Step 3** (vacuum expectation values). $\langle0|\hat a_{\mathbf p}\hat a_{\mathbf q}|0\rangle = 0$ and $\langle0|\hat a_{\mathbf p}^\dagger \hat a_{\mathbf q}|0\rangle = 0$ because $\hat a_{\mathbf q}|0\rangle = 0$; $\langle0|\hat a_{\mathbf p}^\dagger \hat a_{\mathbf q}^\dagger|0\rangle = 0$ because $\langle0|\hat a_{\mathbf p}^\dagger = 0$. The survivor is $\langle0|\hat a_{\mathbf p}\hat a_{\mathbf q}^\dagger|0\rangle = \langle0|[\hat a_{\mathbf p}, \hat a_{\mathbf q}^\dagger]|0\rangle = (2\pi)^3\delta^3(\mathbf p - \mathbf q)$ ([[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|Theorem §C2a.2.6]]).
>
> **Step 4** (integrate the delta). It eliminates $\mathbf q$ (sense: smeared in $y$, the $\mathbf q$-integrand carries the Schwartz factor $\tilde g(q)$, and $\delta^3$ acts on it as in [[§CA.2 Generalized Functions#^def-ca-2-2|Def. §CA.2.2]]; the pointwise formula below is the kernel of the result, Theorem §C2b.2.2): $\mathbf q = \mathbf p$, $q^0 = p^0$, $\frac{1}{\sqrt{2E_{\mathbf p}}\sqrt{2E_{\mathbf q}}} \to \frac{1}{2E_{\mathbf p}}$, and $e^{-ip\cdot x + iq\cdot y} \to e^{-ip\cdot(x - y)}$:
>
> $$
> D_W = \int\frac{d^3p}{(2\pi)^3\,2E_{\mathbf p}}\,e^{-ip\cdot(x - y)} .
> $$
>
> ⚑ By-product: $D_W$ depends on $x - y$ only (translation invariance of the vacuum), and the invariant measure of [[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-2|Def. §C2a.4.2]] appears by itself.
>
> **Step 5** (the four-dimensional form). For any $F$, $\int\frac{d^4p}{(2\pi)^4}2\pi\,\theta(p^0)\delta(p^2 - m^2)F(p) = \int\frac{d^3p}{(2\pi)^3}\int dp^0\,\theta(p^0)\,\frac{\delta(p^0 - E_{\mathbf p}) + \delta(p^0 + E_{\mathbf p})}{2E_{\mathbf p}}F(p)$ by the composition rule ([[§B1.2 The Dirac Delta Function and the Helmholtz Theorem#^thm-b1-2-1|EM Theorem §B1.2.1]], justified as a distributional limit in [[§CA.2 Generalized Functions#^thm-ca-2-6|Theorem §CA.2.6]], 2, and in four dimensions [[§CA.2 Generalized Functions#^thm-ca-2-7|Theorem §CA.2.7]], 1; roots $p^0 = \pm E_{\mathbf p}$, $|\partial_{p^0}(p^2 - m^2)| = 2E_{\mathbf p}$). The step function removes the root $-E_{\mathbf p}$, and the $p^0$ integral sets $p^0 = E_{\mathbf p}$. With $F = e^{-ip\cdot\xi}$ this is Step 4 ([[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-3|Theorem §C2a.4.3]]).
>
> ⚑ By-product: $\tilde D_W(p) = 2\pi\theta(p^0)\delta(p^2 - m^2)$, the momentum-space entry of the two-point family → [[§C2b.7 Wick Rotation and the Two-Point Family#^rem-c2b-7-2|§C2b.7, Remark: The two-point functions at a glance]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-11|Theorem §C2b.6.11]].
>
> **Step 6** (no convergence at real $\xi$). At real $\xi$ the integrand has modulus $1/2E_{\mathbf p}$, and $\int\frac{d^3p}{2E_{\mathbf p}} = 2\pi\int_0^\infty\frac{p^2\,dp}{\sqrt{p^2 + m^2}}$ diverges like $\int p\,dp$.
>
> ⚑ By-product: the formula needs a meaning beyond ordinary integration → [[§C2b.2 The Wightman Function#^thm-c2b-2-5|Theorem §C2b.2.5]] (boundary value).
>
> **What the derivation shows.**
> - Of the four orderings of ladder operators only $\hat a\hat a^\dagger$ survives in the vacuum: $D_W$ is "create at $y$, annihilate at $x$".
> - The measure $d^3p/2E_{\mathbf p}$, introduced for the states in §C2a.4, now does its job in an amplitude; it is what will make $D_W$ Lorentz invariant (Theorem §C2b.2.3).
> - Used next: invariance (Theorem §C2b.2.3), the homogeneous equation and conjugation (Theorem §C2b.2.4), the boundary value (Theorem §C2b.2.5).

^der-c2b-2-1

*Uses:* [[§C2b.1 Heisenberg Fields#^thm-c2b-1-4|Theorem §C2b.1.4]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|Theorem §C2a.2.6]], [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-3|Theorem §C2a.4.3]], [[§B1.2 The Dirac Delta Function and the Helmholtz Theorem#^thm-b1-2-1|EM Theorem §B1.2.1]], [[§CA.2 Generalized Functions#^thm-ca-2-6|Theorem §CA.2.6]], [[§CA.2 Generalized Functions#^thm-ca-2-7|Theorem §CA.2.7]]

> [!theorem] Theorem §C2b.2.2: The Wightman Function Is a Tempered Distribution
> With $\tilde f(p) = \int d^4x\,f(x)e^{ip\cdot x}$ and $p^0 = E_{\mathbf p}$:
> 1. For $f, g \in \mathcal S(\mathbb R^4)$, $\langle0|\hat\phi(f)\hat\phi(g)|0\rangle = \displaystyle\int\frac{d^3p}{(2\pi)^3\,2E_{\mathbf p}}\,\tilde f(-p)\,\tilde g(p)$, finite. This bilinear form has the kernel $D_W(x - y)$ with $D_W \in \mathcal S'(\mathbb R^4)$ the transform of $2\pi\theta(p^0)\delta(p^2 - m^2)$: that is what [[§C2b.2 The Wightman Function#^def-c2b-2-1|Def. §C2b.2.1]] means.
> 2. *How it acts:* $D_W[f] = \displaystyle\int d^4\xi\,f(\xi)\,D_W(\xi) = \int\frac{d^3p}{(2\pi)^3\,2E_{\mathbf p}}\,\tilde f(-p)$. The mode integral of [[§C2b.2 The Wightman Function#^thm-c2b-2-1|Theorem §C2b.2.1]] is this formula with the $\xi$-integral done first.
> 3. *At fixed time:* $D_W(t, \cdot)$ is a tempered distribution in $\boldsymbol\xi$ with spatial transform $e^{-iE_{\mathbf p}t}/2E_{\mathbf p}$, smooth in $t$, and $D_W[f] = \int dt\,D_W(t, \cdot)\bigl[f(t, \cdot)\bigr]$.
>
> *Source: the user's PHY 513 notes, App. A §A.4 (the Wightman function as a tempered distribution), Ch. 5 §5.4 · stated here with its action (standard: Streater & Wightman, Ch. 2–3; Reed & Simon II, §IX.8)*

^thm-c2b-2-2

> [!derivation]- Derivation
> **Step 1** (the bilinear form). By [[§C2b.1 Heisenberg Fields#^thm-c2b-1-6|Theorem §C2b.1.6]], 1, $\hat\phi(g)|0\rangle = \int\frac{d^3q}{(2\pi)^3}\frac{\tilde g(q)}{\sqrt{2E_{\mathbf q}}}\hat a_{\mathbf q}^\dagger|0\rangle$, and in $\langle0|\hat\phi(f)$ only the annihilation part of $\hat\phi(f)$ survives, with coefficient $\tilde f(-p)$. With $\langle0|\hat a_{\mathbf p}\hat a_{\mathbf q}^\dagger|0\rangle = (2\pi)^3\delta^3(\mathbf p - \mathbf q)$ ([[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|Theorem §C2a.2.6]]) acting on the Schwartz integrand,
>
> $$
> \langle0|\hat\phi(f)\hat\phi(g)|0\rangle = \int\frac{d^3p\,d^3q}{(2\pi)^6}\frac{\tilde f(-p)\,\tilde g(q)}{\sqrt{2E_{\mathbf p}2E_{\mathbf q}}}(2\pi)^3\delta^3(\mathbf p - \mathbf q) = \int\frac{d^3p}{(2\pi)^3\,2E_{\mathbf p}}\,\tilde f(-p)\,\tilde g(p) .
> $$
>
> **Step 2** (continuity, hence a kernel). On the shell $|\tilde f(\pm E_{\mathbf p}, \pm\mathbf p)| \le C(1 + |\mathbf p|)^{-4}\,\sup_k(1 + |k|)^4|\tilde f(k)|$, and the supremum is a Schwartz seminorm of $\tilde f$, controlled by finitely many seminorms of $f$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-1|Theorem §CA.3.1]], 1). So the form is bounded by seminorms of $f$ times seminorms of $g$: continuous in each argument. By the kernel theorem ([[§CA.2 Generalized Functions#^thm-ca-2-11|Theorem §CA.2.11]]) there is a unique $K \in \mathcal S'(\mathbb R^8)$ with $\langle0|\hat\phi(f)\hat\phi(g)|0\rangle = K[f \otimes g]$.
>
> **Step 3** (the candidate $D_W$). Define $D_W[h] \equiv \int\frac{d^3p}{(2\pi)^3\,2E_{\mathbf p}}\tilde h(-p)$ for $h \in \mathcal S(\mathbb R^4)$; by the bound of Step 2 it is a tempered distribution. It is the inverse transform of $2\pi\theta(p^0)\delta(p^2 - m^2)$: moving the transform onto the test function ([[§CA.2 Generalized Functions#^def-ca-2-4|Def. §CA.2.4]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-2|Theorem §CA.3.2]]), $\int d^4\xi\,h(\xi)\int\frac{d^4p}{(2\pi)^4}\tilde D_W(p)e^{-ip\cdot\xi}$ is $\tilde D_W$ applied to $\tilde h(-p)/(2\pi)^4$, and $\theta(p^0)\delta(p^2 - m^2)$ acts as $\varphi \mapsto \int d^3p\,\varphi(E_{\mathbf p}, \mathbf p)/2E_{\mathbf p}$ ([[§CA.2 Generalized Functions#^thm-ca-2-7|Theorem §CA.2.7]], 1), which gives $\int\frac{d^3p}{(2\pi)^3\,2E_{\mathbf p}}\tilde h(-p)$.
>
> **Step 4** (the kernel depends on $x - y$ only). Let $h(\xi) = \int d^4y\,f(\xi + y)\,g(y)$, a Schwartz function; then $\int d^4x\,d^4y\,f(x)g(y)D_W(x - y) \equiv D_W[h]$ ([[§CA.2 Generalized Functions#^def-ca-2-8|Def. §CA.2.8]]). Its transform, with the substitution $x = \xi + y$ (Jacobian 1; translation ↔ phase, [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-5|Theorem §CA.3.5]], 1), is
>
> $$
> \tilde h(-p) = \int d^4\xi\,d^4y\,f(\xi + y)\,g(y)\,e^{-ip\cdot\xi} = \int d^4x\,f(x)\,e^{-ip\cdot x}\int d^4y\,g(y)\,e^{ip\cdot y} = \tilde f(-p)\,\tilde g(p) .
> $$
>
> So $D_W[h]$ equals Step 1, and by uniqueness $K(x, y) = D_W(x - y)$. Parts 1 and 2.
>
> **Step 5** (why the mode integral needs the order). Read with the $\mathbf p$-integral inside, $\int d^4\xi\,f(\xi)\bigl[\int\frac{d^3p}{2E_{\mathbf p}}e^{-ip\cdot\xi}\bigr]$, the bracket diverges for every $\xi$ (Step 6 of Derivation §C2b.2.1). With the $\xi$-integral inside, the integrand is $\tilde f(-p)/2E_{\mathbf p}$, absolutely integrable; this order is the meaning of the formula ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-6|Theorem §CA.3.6]], "after smearing").
>
> ⚑ By-product: $D_W$ has values at points only where it is a smooth function, off the light cone → [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-6|Theorem §C2b.3.6]].
>
> **Step 6** (fixed time). For $g \in \mathcal S(\mathbb R^3)$ with spatial transform $\tilde g(\mathbf k) = \int d^3\xi\,g(\boldsymbol\xi)e^{-i\mathbf k\cdot\boldsymbol\xi}$, put $D_W(t, \cdot)[g] \equiv \int\frac{d^3p}{(2\pi)^3\,2E_{\mathbf p}}e^{-iE_{\mathbf p}t}\,\tilde g(-\mathbf p)$, the action of the spatial inverse transform of $e^{-iE_{\mathbf p}t}/2E_{\mathbf p}$. Each $t$-derivative brings down $-iE_{\mathbf p}$ and the integrand stays absolutely integrable, uniformly in $t$, so $t \mapsto D_W(t, \cdot)[g]$ is smooth ([[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|Theorem §CA.1.1]], 2). For $f \in \mathcal S(\mathbb R^4)$, Fubini in $(t, \mathbf p)$ and $\int dt\,e^{-iE_{\mathbf p}t}\int d^3\xi\,f(t, \boldsymbol\xi)e^{i\mathbf p\cdot\boldsymbol\xi} = \tilde f(-p)$ give $\int dt\,D_W(t, \cdot)[f(t, \cdot)] = D_W[f]$. Part 3.
>
> **What the derivation shows.**
> - "$\langle0|\hat\phi(x)\hat\phi(y)|0\rangle$" is the kernel of a continuous bilinear form; the vacuum is translation invariant, so the kernel depends on $x - y$.
> - $D_W$ is a function of time with values in spatial distributions: this is what lets step functions $\theta(\pm\xi^0)$ multiply it ([[§C2b.5 Green's Functions and Contours#^thm-c2b-5-6|Theorem §C2b.5.6]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-4|Theorem §C2b.6.4]]).
> - Used next: invariance as a distribution (Theorem §C2b.2.3), the boundary value (Theorem §C2b.2.5), $D$ and $D_1$ ([[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-4|Theorem §C2b.4.4]]).

^der-c2b-2-2

*Uses:* [[§C2b.1 Heisenberg Fields#^thm-c2b-1-6|Theorem §C2b.1.6]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|Theorem §C2a.2.6]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-1|Theorem §CA.3.1]], [[§CA.2 Generalized Functions#^thm-ca-2-11|Theorem §CA.2.11]], [[§CA.2 Generalized Functions#^def-ca-2-4|Def. §CA.2.4]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-2|Theorem §CA.3.2]], [[§CA.2 Generalized Functions#^thm-ca-2-7|Theorem §CA.2.7]], [[§CA.2 Generalized Functions#^def-ca-2-8|Def. §CA.2.8]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-5|Theorem §CA.3.5]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-6|Theorem §CA.3.6]], [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|Theorem §CA.1.1]]

> [!theorem] Theorem §C2b.2.3: Lorentz Invariance of the Wightman Function
> For every $\Lambda \in SO^+(1,3)$, $D_W$ is invariant as a distribution, $D_W[f\circ\Lambda^{-1}] = D_W[f]$ for every test function $f$ ([[§CA.2 Generalized Functions#^def-ca-2-8|Def. §CA.2.8]]); where $D_W$ is a function, off the light cone ([[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-6|Theorem §C2b.3.6]]), this reads $D_W(\Lambda\xi) = D_W(\xi)$. Hence $D_W$ is constant on the orbits of $SO^+(1,3)$: a function of $\xi^2$ alone at spacelike $\xi$, and of $\xi^2$ and $\operatorname{sgn}\xi^0$ at timelike $\xi$ (on the light cone, where $D_W$ is singular, the future and past halves are also distinct orbits).
>
> *Source: the user's PHY 513 notes, Ch. 5 §5.4 · PS §2.4, p. 27 ("we have already argued in (2.40) that integrals of this form are Lorentz invariant")*

^thm-c2b-2-3

> [!derivation]- Derivation
> **Step 1** (substitute). In the four-dimensional form of [[§C2b.2 The Wightman Function#^thm-c2b-2-1|Theorem §C2b.2.1]], substitute $p = \Lambda q$ (sense: in the pairing of Theorem §C2b.2.2, 2, $D_W[f\circ\Lambda^{-1}] = \int\frac{d^3p}{(2\pi)^3 2E_{\mathbf p}}\widetilde{f\circ\Lambda^{-1}}(-p)$ with $\widetilde{f\circ\Lambda^{-1}}(k) = \tilde f(\Lambda^{-1}k)$, and the substitution is [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|Theorem §CA.3.7]], 4 applied to the invariant shell distribution of [[§CA.2 Generalized Functions#^thm-ca-2-7|Theorem §CA.2.7]], 1). The Jacobian is $|\det\Lambda| = 1$; $p^2 = q^2$; and $p\cdot\Lambda\xi = \Lambda q\cdot\Lambda\xi = q\cdot\xi$ ([[§B1.2 Lorentz Transformations and the Lorentz Group#^thm-b1-2-2|REL Theorem §B1.2.2]]).
>
> **Step 2** (the step function). On the support of $\delta(q^2 - m^2)$ with $m > 0$, $q$ is timelike, and an orthochronous $\Lambda$ preserves the sign of the time component of a timelike vector ([[§B1.3 Causal Structure and Proper Time#^thm-b1-3-1|REL Theorem §B1.3.1]]; [[§C1a.4 The Lorentz Group#^thm-c1a-4-5|Theorem §C1a.4.5]], 3): $\theta((\Lambda q)^0) = \theta(q^0)$. (For $m = 0$ the support is the null cone without its tip, and part 2 of the same theorem applies.)
>
> ⚑ By-product: the assumption $m > 0$ (or the null-cone version for $m = 0$) is used here and only here.
>
> **Step 3** (conclude). Steps 1–2 give
>
> $$
> D_W(\Lambda\xi) = \int\frac{d^4q}{(2\pi)^4}\,2\pi\theta(q^0)\delta(q^2 - m^2)\,e^{-iq\cdot\xi} = D_W(\xi) .
> $$
>
> ⚑ By-product: the regulator of Theorem §C2b.2.5, $\xi^0 \to \xi^0 - i\varepsilon$, is not invariant, since $\Lambda$ moves $(\varepsilon, \mathbf 0)$ to another vector of the open forward cone; the boundary value does not depend on the direction of approach within that cone ([[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-1|Theorem §CA.6.1]], 2; Step 6 of Derivation §C2b.2.5), so the distribution is invariant although each regulated function is not → [[§C2b.2 The Wightman Function#^thm-c2b-2-5|Theorem §C2b.2.5]].
>
> **Step 4** (orbits). The orbits of $SO^+(1,3)$ are each one-sheeted hyperboloid $\xi^2 = -r^2$, each sheet of $\xi^2 = \tau^2 > 0$ separately, and the two halves of the null cone ([[§B1.3 Causal Structure and Proper Time#^rem-b1-3-1|REL Remark: Normal forms, and the orbits of the Lorentz group]]; [[§C1a.4 The Lorentz Group#^thm-c1a-4-4|Theorem §C1a.4.4]]). An invariant function is constant on each. (Off the cone $D_W$ is a continuous function, and two continuous functions equal as distributions are equal pointwise, [[§CA.2 Generalized Functions#^thm-ca-2-1|Theorem §CA.2.1]], 2; so the distributional invariance of Step 3 is pointwise invariance there.)
>
> ⚑ By-product: the spacelike orbit through $\xi$ contains $-\xi$; the future and past sheets do not → microcausality, [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-5|Theorem §C2b.4.5]].
>
> **What the derivation shows.**
> - Invariance needs the four-dimensional form; the three-dimensional integral hides it in $E_{\mathbf p}$ ([[§C2b.1 Heisenberg Fields#^rem-c2b-1-2|§C2b.1, Remark: What is covariant and what is not yet]]).
> - $\theta(p^0)$, positive energy, is an invariant statement only because the shell is timelike: the same fact that makes "past" and "future" invariant for spacetime intervals.
> - Used next: microcausality (Theorem §C2b.4.5), the frame choices in Theorems §C2b.3.3–§C2b.3.4.

^der-c2b-2-3

*Uses:* [[§C2b.2 The Wightman Function#^thm-c2b-2-1|Theorem §C2b.2.1]], [[§B1.2 Lorentz Transformations and the Lorentz Group#^thm-b1-2-2|REL Theorem §B1.2.2]], [[§B1.3 Causal Structure and Proper Time#^thm-b1-3-1|REL Theorem §B1.3.1]], [[§B1.3 Causal Structure and Proper Time#^rem-b1-3-1|REL Remark: Normal forms, and the orbits of the Lorentz group]]

> [!theorem] Theorem §C2b.2.4: The Wightman Function Is a Homogeneous Solution; Reversal Is Conjugation
> 1. $(\partial_x^2 + m^2)D_W(x - y) = 0$.
> 2. $D_W(-\xi) = \overline{D_W(\xi)}$.
>
> *Source: the user's PHY 513 notes, Ch. 5 §5.5 (Derivation "Both are parts of the Wightman function", Step 1) · PHY 513, Problem Set 4, Problem 4(b)*

^thm-c2b-2-4

> [!derivation]- Derivation
> **Step 1** (each mode is on shell). On a plane wave, $\partial_\mu e^{-ip\cdot\xi} = -ip_\mu e^{-ip\cdot\xi}$ ([[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-8|Theorem §C1a.5.8]]), so $(\partial^2 + m^2)e^{-ip\cdot\xi} = (m^2 - p^2)e^{-ip\cdot\xi}$, and $p^2 = E_{\mathbf p}^2 - \mathbf p^2 = m^2$. The operator passes through the integral in the sense of generalized functions ([[§CA.2 Generalized Functions#^def-ca-2-4|Def. §CA.2.4]]): with Theorem §C2b.2.2, 2, $\bigl((\partial^2 + m^2)D_W\bigr)[f] = D_W\bigl[(\partial^2 + m^2)f\bigr] = \int\frac{d^3p}{(2\pi)^3\,2E_{\mathbf p}}(m^2 - p^2)\tilde f(-p) = 0$, by the derivative rule in $\mathcal S$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-5|Theorem §CA.3.5]], 3) and $p^2 = m^2$ on the shell; or for the regulated function $W$ of Theorem §C2b.2.5 by [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|Theorem §CA.1.1]].
>
> **Step 2** (conjugation from the operators). For any state, $\overline{\langle0|\hat A|0\rangle} = \langle0|\hat A^\dagger|0\rangle$, and $(\hat\phi(x)\hat\phi(y))^\dagger = \hat\phi(y)^\dagger\hat\phi(x)^\dagger = \hat\phi(y)\hat\phi(x)$ because $\hat\phi$ is Hermitian. So $\overline{D_W(x - y)} = \langle0|\hat\phi(y)\hat\phi(x)|0\rangle = D_W(y - x)$. (As distributions, with $\overline T[f] \equiv \overline{T[\bar f]}$ and $T(-\cdot)[f] \equiv T[f(-\cdot)]$, [[§CA.2 Generalized Functions#^def-ca-2-8|Def. §CA.2.8]]: by Theorem §C2b.2.2, 2, $\overline{D_W[\bar f]} = \int\frac{d^3p}{(2\pi)^3 2E_{\mathbf p}}\tilde f(p) = D_W[f(-\cdot)]$.)
>
> **Step 3** (the same from the integral). Conjugating the integrand turns $e^{-ip\cdot\xi}$ into $e^{+ip\cdot\xi} = e^{-ip\cdot(-\xi)}$, the integrand of $D_W(-\xi)$; for the regulated function, $\overline{W(\xi^0 - i\varepsilon, \boldsymbol\xi)} = W(-\xi^0 - i\varepsilon, -\boldsymbol\xi)$, so the prescription maps correctly.
>
> **What the derivation shows.**
> - Part 1 uses the mass shell only; $D_W$ is a solution, not a Green's function. The sign $m^2 - p^2$ is the one that slips ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^cau-c2b-6-2|§C2b.6, Caution: Signs that slip]]).
> - Part 2 uses the Hermiticity of $\hat\phi$; for a complex field the corresponding statement relates $\langle\hat\phi\hat\phi^\dagger\rangle$ and $\langle\hat\phi^\dagger\hat\phi\rangle$.
> - Used next: the split into $D$ and $D_1$ (Theorem §C2b.4.3).

^der-c2b-2-4

*Uses:* [[§CA.2 Generalized Functions#^def-ca-2-4|Def. §CA.2.4]], [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|Theorem §CA.1.1]]

> [!theorem] Theorem §C2b.2.5: The Wightman Function Is a Boundary Value
> Because every energy is positive, the function
>
> $$
> W(z, \boldsymbol\xi) \equiv \int\frac{d^3p}{(2\pi)^3\,2E_{\mathbf p}}\,e^{-iE_{\mathbf p}z + i\mathbf p\cdot\boldsymbol\xi}, \qquad \operatorname{Im}z < 0,
> $$
>
> converges absolutely and is analytic in the lower half $z$-plane, and
>
> $$
> D_W(\xi) = \lim_{\varepsilon\to0^+}W(\xi^0 - i\varepsilon, \boldsymbol\xi)
> $$
>
> in $\mathcal S'(\mathbb R^4)$: for every test function $f$, $\int d^4\xi\,f(\xi)\,W(\xi^0 - i\varepsilon, \boldsymbol\xi) \to D_W[f]$ of [[§C2b.2 The Wightman Function#^thm-c2b-2-2|Theorem §C2b.2.2]], 2 ([[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-1|Theorem §CA.6.1]]). The limit is the same along $\xi - i\varepsilon\eta$ for every $\eta$ in the open forward light cone. This limit *is* the definition of the physicist's "$\xi^0 \to \xi^0 - i\varepsilon$".
>
> *Source: the user's PHY 513 notes, Ch. 5 §5.4 (Principle "The Wightman function is a boundary value") · PHY 513, Problem Set 4, Problem 2(a) (the prescription $t \to t - i\varepsilon$)*

^thm-c2b-2-5

> [!derivation]- Derivation
> **Step 1** (the modulus). Write $z = a - ib$ with $b > 0$. Then $|e^{-iE_{\mathbf p}z}| = |e^{-iE_{\mathbf p}a}|\,e^{-bE_{\mathbf p}} = e^{-bE_{\mathbf p}}$, so the integrand has modulus $e^{-bE_{\mathbf p}}/2E_{\mathbf p}$.
>
> **Step 2** (absolute convergence, uniformly). For $b \ge b_0 > 0$ the modulus is at most $e^{-b_0E_{\mathbf p}}/2E_{\mathbf p}$, and $\int d^3p\,e^{-b_0E_{\mathbf p}}/2E_{\mathbf p} \le 2\pi\int_0^\infty p\,e^{-b_0p}\,dp < \infty$ (using $E_{\mathbf p} \ge p$).
>
> **Step 3** (analyticity). The $z$-derivative of the integrand is $-iE_{\mathbf p}$ times it, bounded by $\frac12e^{-b_0E_{\mathbf p}}$, again integrable. By [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|Theorem §CA.1.1]], 2 the complex derivative exists and is the integral of the derivative ([[§CA.4 Contour Integration#^def-ca-4-2|Def. §CA.4.2]]): $W$ is analytic for $\operatorname{Im}z < 0$.
>
> ⚑ By-product: the lower half-plane is the right one only because $E_{\mathbf p} > 0$, the spectrum condition; for negative energies $e^{-iEz}$ would grow there → [[§C2b.2 The Wightman Function#^rem-c2b-2-1|★ Remark: Why "Wightman function"]].
>
> **Step 4** (the boundary value as a generalized function). Let $f(\xi)$ be a Schwartz function of the four coordinates, so that $\tilde f(-p) = \int d^4\xi\,f(\xi)e^{-ip\cdot\xi}$ (Def. §CA.3.1's transform at $-p$). Exchanging the absolutely convergent integrals (Fubini; for $\varepsilon > 0$ the integrand is bounded by $|f(\xi)|e^{-\varepsilon E_{\mathbf p}}/2E_{\mathbf p}$, integrable over $(\xi, \mathbf p)$),
>
> $$
> \int d^4\xi\,f(\xi)\,W(\xi^0 - i\varepsilon, \boldsymbol\xi) = \int\frac{d^3p}{(2\pi)^3\,2E_{\mathbf p}}\,e^{-\varepsilon E_{\mathbf p}}\,\tilde f(-E_{\mathbf p}, -\mathbf p) .
> $$
>
> $\tilde f$ decreases faster than any power, so $|e^{-\varepsilon E}\tilde f/2E| \le |\tilde f|/2E$ is integrable independently of $\varepsilon$, and by dominated convergence the right side tends to $\int\frac{d^3p}{(2\pi)^32E_{\mathbf p}}\tilde f(-E_{\mathbf p}, -\mathbf p)$. So the limit exists as a tempered distribution ([[§CA.2 Generalized Functions#^def-ca-2-4|Def. §CA.2.4]]), and it is the mode integral of [[§C2b.2 The Wightman Function#^thm-c2b-2-1|Theorem §C2b.2.1]] read against test functions.
>
> ⚑ By-product: "$\xi^0 \to \xi^0 - i\varepsilon$" is not a trick but the definition of $D_W$; the same prescription in momentum space becomes the $i\varepsilon$ of the Feynman propagator → [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-9|Theorem §C2b.6.9]].
>
> **Step 5** (equal times). At $\xi^0 = 0$ the regulated integral is $\int\frac{d^3p}{(2\pi)^32E_{\mathbf p}}e^{-\varepsilon E_{\mathbf p}}e^{i\mathbf p\cdot\boldsymbol\xi}$: the convergence factor $e^{-\varepsilon E_{\mathbf p}}$ is not an approximation but exactly $W(-i\varepsilon, \boldsymbol\xi)$.
>
> **Step 6** (the forward tube). For $\eta$ with $\eta^0 > |\boldsymbol\eta|$ and $p$ on the positive shell, $p\cdot\eta = E_{\mathbf p}\eta^0 - \mathbf p\cdot\boldsymbol\eta \ge E_{\mathbf p}(\eta^0 - |\boldsymbol\eta|) > 0$, so $\int\frac{d^3p}{(2\pi)^3 2E_{\mathbf p}}e^{-ip\cdot(\xi - i\varepsilon\eta)}$ has modulus of the integrand $e^{-\varepsilon p\cdot\eta}/2E_{\mathbf p}$: it converges and is analytic in the tube, and Step 4 with $e^{-\varepsilon p\cdot\eta} \le 1$ in place of $e^{-\varepsilon E_{\mathbf p}}$ gives the same limit $D_W[f]$. The direction $\eta = (1, \mathbf 0)$ is not special ([[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-1|Theorem §CA.6.1]], 2).
>
> **What the derivation shows.**
> - The spectrum condition $E_{\mathbf p} > 0$ is the only physics used; the rest is dominated convergence ([[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|Theorem §CA.1.1]]) applied to the pairing with a test function, the definition of a distributional limit ([[§CA.2 Generalized Functions#^thm-ca-2-5|Theorem §CA.2.5]]).
> - The distributional meaning of $D_W$ is now fixed; where the limit is a smooth function (outside the light cone) it is an ordinary function (Theorem §C2b.3.3).
> - Used next: the Euclidean evaluation on $z = -i\tau$ (Theorem §C2b.3.1) and the continuation to every $\xi$ (Theorem §C2b.3.2).

^der-c2b-2-5

*Uses:* [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|Theorem §CA.1.1]], [[§CA.4 Contour Integration#^def-ca-4-2|Def. §CA.4.2]], [[§CA.2 Generalized Functions#^def-ca-2-4|Def. §CA.2.4]], [[§C2b.2 The Wightman Function#^thm-c2b-2-1|Theorem §C2b.2.1]], [[§C2b.2 The Wightman Function#^thm-c2b-2-2|Theorem §C2b.2.2]], [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-1|Theorem §CA.6.1]], [[§CA.2 Generalized Functions#^thm-ca-2-5|Theorem §CA.2.5]]

> [!remark]- ★ Remark: Why "Wightman function": the axiomatic view
> The $n$-point functions $W_n = \langle0|\hat\phi(x_1)\cdots\hat\phi(x_n)|0\rangle$ are tempered distributions, and Wightman's axioms characterize a field theory by them. For $n = 2$ every axiom has been seen here: Poincaré invariance (Theorem §C2b.2.3), the spectrum condition as analyticity in the forward tube (Theorem §C2b.2.5), locality as the symmetry of $W_2$ at spacelike separation (Theorem §C2b.4.5), positivity from the Hilbert-space norm and clustering from the uniqueness of the vacuum. The reconstruction theorem runs the logic backwards: distributions with these properties determine a Hilbert space, a unique invariant vacuum and a field, so the Fock space of [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^pr-c2a-3-3|Principle §C2a.3.3]] is a consequence of the correlation functions. At imaginary times the $W_n$ become the Euclidean Schwinger functions (Theorem §C2b.3.1 is the $n = 2$ one), and the Osterwalder–Schrader theorem (reflection positivity) is the rigorous basis of the Euclidean path integral and of lattice field theory. For the free field every $W_n$ is fixed by $W_2 = D_W$ through Wick's theorem (QFT C6, planned).
>
> *Source: the user's PHY 513 notes, Ch. 5 §5.4 (Derivation "Why 'Wightman function': the axiomatic view")*

^rem-c2b-2-1

> [!remark]- Connections
> - The oscillator's ground-state correlation $\langle0|\hat x(t)\hat x(0)|0\rangle = \frac{\hbar}{2m\omega}e^{-i\omega t}$, with its imaginary part a state-independent commutator, is the one-mode version of $D_W = \frac12(D_1 + iD)$: [[§C3.4 The Harmonic Oscillator and Coherent States Revisited#^ex-c3-4-2|QM Example §C3.4.2]]; a field is one such oscillator per $\mathbf p$, and $D_W$ sums their correlations with the weight $1/2E_{\mathbf p}$.
> - The boundary-value definition $\xi^0 \to \xi^0 - i\varepsilon$ is the same device as $t \to t - i\varepsilon$ for the Fresnel integrals of the nonrelativistic propagator ([[§C4.1 Propagators#^thm-c4-1-3|QM Theorem §C4.1.3]]) and as $E \to E + i\varepsilon$ in [[§C4.1 Propagators#^thm-c4-1-7|QM Theorem §C4.1.7]]: positivity of the energy makes the lower half of the complex time plane harmless.
> - The Wightman function's antisymmetric part is the commutator function and its symmetric part the Hadamard function ([[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-3|Theorem §C2b.4.3]]); with time ordering it gives the Feynman propagator ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-2|Theorem §C2b.6.2]]).
> - [[§CA.2 Generalized Functions#^thm-ca-2-11|Theorem §CA.2.11]] (the kernel theorem) is why "$\langle0|\hat\phi(x)\hat\phi(y)|0\rangle$" means one distribution in $(x, y)$: the smeared form $\langle0|\hat\phi(f)\hat\phi(g)|0\rangle$ of Theorem §C2b.2.2 is continuous, so it has a kernel, and translation invariance makes it $D_W(x - y)$.
> - [[§CA.2 Generalized Functions#^thm-ca-2-7|Theorem §CA.2.7]] (the invariant shell distribution $\theta(p^0)\delta(p^2 - m^2)$) is $\tilde D_W/2\pi$; the composition rule behind it, [[§CA.2 Generalized Functions#^thm-ca-2-6|Theorem §CA.2.6]], is Step 5 of Derivation §C2b.2.1.
> - [[§CA.2 Generalized Functions#^def-ca-2-8|Def. §CA.2.8]] (linear changes of variables, invariant distributions) and [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|Theorem §CA.3.7]] (rotating and boosting the integration variable) make Lorentz invariance a statement about distributions (Theorem §C2b.2.3).
> - In operator language Theorem §C2b.2.3 follows from $U(\Lambda)\hat\phi(x)U(\Lambda)^{-1} = \hat\phi(\Lambda x)$ and $U(\Lambda)|0\rangle = |0\rangle$: $\langle0|\hat\phi(\Lambda x)\hat\phi(\Lambda y)|0\rangle = \langle0|\hat\phi(x)\hat\phi(y)|0\rangle$ — [[§C3.5 Quantum Poincaré Transformations#^thm-c3-5-12|Theorem §C3.5.12]], [[§C3.5 Quantum Poincaré Transformations#^thm-c3-5-11|Theorem §C3.5.11]].
> - [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-1|Theorem §CA.6.1]] (boundary values of analytic functions) is the general form of Theorem §C2b.2.5; its tube version is why the non-invariant regulator $\xi^0 - i\varepsilon$ still gives an invariant distribution.
> - [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|Theorem §CA.1.1]] (dominated convergence, differentiation under the integral) proves analyticity of $W$, the boundary limit, and smoothness in time.
> - [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-6|Theorem §CA.3.6]] (exchanging the space and momentum integrals) and [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-5|Theorem §CA.3.5]] (translation ↔ phase) turn the double mode integral into the action $D_W[f] = \int\frac{d^3p}{(2\pi)^3 2E_{\mathbf p}}\tilde f(-p)$.
