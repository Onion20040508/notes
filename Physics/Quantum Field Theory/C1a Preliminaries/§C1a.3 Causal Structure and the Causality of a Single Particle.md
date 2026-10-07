---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C1a
section: C1a.3
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C1a.2 Natural Units and Dimensional Analysis]] · ↑ [[· C1a Preliminaries]] · [[§C1a.4 The Lorentz Group]] →

*Sources: the user's PHY 513 notes, Ch. 2 §§2.1–2.2 and Ch. 2 §2.4 ("The scale of causality violation") · PHY 513 Lecture 2 (Larsen, 2 Sep 2026), Part A · Peskin & Schroeder §2.1, pp. 13–14 · DLMF §10.17, §10.27 (cited in the user's notes).*

Can one relativistic particle propagate without leaving its light cone? The causal classes of spacetime and their invariance are Relativity's ([[§B1.3 Causal Structure and Proper Time#^def-b1-3-1|REL Def. §B1.3.1]], [[§B1.3 Causal Structure and Proper Time#^thm-b1-3-1|REL Theorem §B1.3.1]]), the nonrelativistic propagator is [[§C4.1 Propagators#^thm-c4-1-4|QM Theorem §C4.1.4]], and saddle points are [[§CA.5 Gaussian Integrals, Stationary Phase and Bessel Functions|§CA.5]]. This section (Lecture 2, Part A) states causality as a principle, defines the single-particle amplitude $U$, writes it as a boundary value and a radial integral, and shows with the lecture's saddle point that it leaks outside the light cone over a Compton wavelength. The exact amplitude needs the Wightman function: it is $2i\partial_t D_W$, and its closed forms are [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-7|Theorem §C2b.3.7]]–[[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-10|Theorem §C2b.3.10]]; that its leak is exactly the part field theory keeps as a correlation while the commutator vanishes is [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-7|Theorem §C2b.4.7]].

*Conventions* ([[Larsen PHY 513]]): $\hbar = c = 1$, $g = \operatorname{diag}(+, -, -, -)$, $x^2 = t^2 - \mathbf x^2$, $E_{\mathbf p} = \sqrt{\mathbf p^2 + m^2}$, $m > 0$ unless stated otherwise.

## Causal structure

*Recall* ([[§B1.3 Causal Structure and Proper Time#^def-b1-3-1|REL Def. §B1.3.1]], [[§B1.3 Causal Structure and Proper Time#^thm-b1-3-1|REL Theorem §B1.3.1]]): relative to the origin a point $x$ is timelike ($x^2 > 0$), null ($x^2 = 0$) or spacelike ($x^2 < 0$); every Lorentz transformation preserves the class, and an orthochronous one preserves the sign of $x^0$ on timelike and null vectors, by the same Cauchy–Schwarz estimate on the first row of $\Lambda$ that the user's notes give. For spacelike $x$ the sign of $x^0$ is frame dependent. Same result, same argument: the home stays in Relativity. The orbits of the proper orthochronous group are [[§C1a.4 The Lorentz Group#^thm-c1a-4-4|Theorem §C1a.4.4]].

> [!caution] Caution: sgn x⁰, not ε(x⁰)
> The lecture writes $\varepsilon(x^0)$ for the sign of the time component, $+1$ in the future and $-1$ in the past. These notes write $\operatorname{sgn}x^0$, because $\varepsilon$ already names the Levi-Civita symbol and the infinitesimal of $i\varepsilon$ prescriptions. It is a second Lorentz invariant (under orthochronous transformations), independent of $x^2$, on timelike and null vectors, and is not defined (frame dependent) on spacelike ones.
>
> *Source: the user's PHY 513 notes, Ch. 2 §2.1 (eq. for $\operatorname{sgn}x^0$ and the note after it) · PHY 513 Lecture 2, Part A ("Future vs. Past")*

^cau-c1a-3-1

> [!remark] Remark: Why the future cannot be boosted into the past
> A second reading of the invariance of $\operatorname{sgn}x^0$: $SO^+(1,3)$ is connected ([[§C1a.4 The Lorentz Group#^thm-c1a-4-3|Theorem §C1a.4.3]]) and acts continuously, and it preserves $x^2$. Along a path $\Lambda(s)$ from $1$ to $\Lambda$, the point $\Lambda(s)x$ of a timelike $x$ moves continuously inside the timelike set, which has two components, $x^0 > 0$ and $x^0 < 0$; so it cannot change component. A spacelike hyperboloid is connected in $3+1$ dimensions and is a single orbit containing points with both signs of $x^0$, which is why $\operatorname{sgn}x^0$ is undefined there ([[§C1a.4 The Lorentz Group#^cau-c1a-4-4|§C1a.4, Caution: The orbit picture depends on the dimension]]). The same orbit fact gives a $\Lambda \in SO^+(1,3)$ with $\Lambda\xi = -\xi$ for every spacelike $\xi$, the step on which the microcausality of the free field rests ([[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-5|Theorem §C2b.4.5]]).
>
> *Source: the user's PHY 513 notes, Ch. 2 §2.1 ("A topological way to see it")*

^rem-c1a-3-1

> [!principle] Principle §C1a.3.1: Causality
> The entire response to a disturbance at a spacetime point lies in its causal future: at future timelike or null separation from it. Points at spacelike separation can neither affect it nor be affected by it.
>
> *Domain:* all of relativistic physics, as a kinematic statement prior to any dynamical law. For quantum fields its operator form is microcausality ([[§C2b.4 Microcausality and the Commutator Function#^pr-c2b-4-1|Principle §C2b.4.1]]).
>
> *Source: PHY 513 Lecture 2, Part A ("Definition: Causality") · the user's PHY 513 notes, Ch. 2 §2.1 (Principle "Causality")*

^pr-c1a-3-1

Relativity B states the same as an axiom inside a remark ([[§B1.3 Causal Structure and Proper Time#^rem-b1-3-2|REL Remark: Causality as a statement about cones]]); here it becomes one of the three principles of quantum field theory ([[§C1b.3 Mass Dimension, Locality and Power Counting#^rem-c1b-3-1|Remark: The three principles of quantum field theory]]). For a classical field with a source it is a theorem about the retarded Green's function, whose support is the closed forward cone ([[§C2b.5 Green's Functions and Contours#^thm-c2b-5-6|Theorem §C2b.5.6]]).

> [!remark] Remark: Causality and time-reversal symmetry
> Many equations of motion are symmetric under $t \to -t$: whoever can predict the future can postdict the past. That is a statement about the equations relating the two cones. Causality is the prior statement that the two cones are different, and that the region outside both is unaffected; the relation between the cones is a separate matter, treated with the discrete symmetries (QFT C9, planned).
>
> *Source: the user's PHY 513 notes, Ch. 2 §2.1 (Discussion)*

^rem-c1a-3-2

## The amplitude of a single particle

> [!caution] Caution: One symbol, two meanings
> In this section $p \equiv |\mathbf p|$ and $r \equiv |\mathbf x|$, so $p^2 = \mathbf p^2 \ge 0$. Elsewhere $p^2$ is the four-vector square $p_\mu p^\mu = E^2 - \mathbf p^2$. A three-dimensional integral contains no four-vectors, which decides the reading.
>
> *Source: the user's PHY 513 notes, Ch. 2 §2.2 (Caution "One symbol, two meanings") · PHY 513 Lecture 2, Part A ("Beware")*

^cau-c1a-3-2

> [!definition] Definition §C1a.3.1: Single-Particle Propagation Amplitude
> For one particle with Hamiltonian $\hat H = E(\hat{\mathbf P})$, a function of the momentum operator, the amplitude to propagate from the origin to $\mathbf x$ in time $t$ is
>
> $$
> U(t, \mathbf x) \equiv \langle\mathbf x|e^{-i\hat Ht}|\mathbf 0\rangle ,
> $$
>
> with $\langle\mathbf x|\mathbf p\rangle = e^{i\mathbf p\cdot\mathbf x}$ and $\langle\mathbf p|\mathbf p'\rangle = (2\pi)^3\delta^3(\mathbf p - \mathbf p')$. Since $|\mathbf x\rangle$ is not a normalizable state ([[§37 Position Eigenstates and Continuous Resolutions#^prop-37-3|556 Prop. §37.3]]), $U(t, \cdot)$ is defined as the kernel of $e^{-i\hat Ht}$: $(e^{-i\hat Ht}\psi)(\mathbf x) = \int d^3y\,U(t, \mathbf x - \mathbf y)\,\psi(\mathbf y)$. Causality ([[§C1a.3 Causal Structure and the Causality of a Single Particle#^pr-c1a-3-1|Principle §C1a.3.1]]) would require $U(t, \mathbf x) = 0$ for $|\mathbf x| > |t|$.
>
> *Source: PHY 513 Lecture 2, Part A ("Quantum Causality of Free Particle I") · the user's PHY 513 notes, Ch. 2 §2.2 (eqs. for $U$ and the completeness relation) · PS §2.1, p. 13*

^def-c1a-3-1

> [!theorem] Theorem §C1a.3.2: The Amplitude Is the Fourier Transform of the Phase
> For each real $t$, $U(t, \cdot)$ is the tempered distribution on $\mathbb R^3$
>
> $$
> U(t, \mathbf x) = \int\frac{d^3p}{(2\pi)^3}\,e^{-iE(\mathbf p)t + i\mathbf p\cdot\mathbf x},
> $$
>
> the inverse Fourier transform of the bounded function $e^{-iE(\mathbf p)t}$, acting on test functions $f$ by $U(t, \cdot)[f] = \int\frac{d^3p}{(2\pi)^3}e^{-iE(\mathbf p)t}\tilde f(-\mathbf p)$, $\tilde f(\mathbf k) = \int d^3x\,f(\mathbf x)e^{-i\mathbf k\cdot\mathbf x}$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^def-ca-3-1|Def. §CA.3.1]]). As $t \to 0$, $U(t, \cdot) \to \delta^3$ in $\mathcal S'(\mathbb R^3)$.
>
> *Source: the user's PHY 513 notes, Ch. 2 §2.2 (insertion of momentum states; check $U \to \delta^3$) · stated here as distributions*

^thm-c1a-3-2

> [!derivation]- Derivation
> **Step 1** (the operator on a wave packet). For $\psi \in \mathcal S(\mathbb R^3)$ write $\psi(\mathbf y) = \int\frac{d^3p}{(2\pi)^3}\tilde\psi(\mathbf p)e^{i\mathbf p\cdot\mathbf y}$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^def-ca-3-1|Def. §CA.3.1]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-1|Theorem §CA.3.1]]). $\hat H = E(\hat{\mathbf P})$ acts on the plane wave $e^{i\mathbf p\cdot\mathbf y}$ as multiplication by $E(\mathbf p)$ (this is what a function of $\hat{\mathbf P}$ means), so
>
> $$
> (e^{-i\hat Ht}\psi)(\mathbf x) = \int\frac{d^3p}{(2\pi)^3}\,e^{-iE(\mathbf p)t}\,\tilde\psi(\mathbf p)\,e^{i\mathbf p\cdot\mathbf x} .
> $$
>
> In bra-ket form this is the insertion of $\int\frac{d^3p}{(2\pi)^3}|\mathbf p\rangle\langle\mathbf p| = 1$ between $e^{-i\hat Ht}$ and $|\psi\rangle$, with $\langle\mathbf x|\mathbf p\rangle = e^{i\mathbf p\cdot\mathbf x}$.
>
> **Step 2** (convolution). $e^{-iE(\mathbf p)t}$ is smooth and bounded, so its inverse transform $U(t, \cdot)$ exists in $\mathcal S'(\mathbb R^3)$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-2|Theorem §CA.3.2]]), and a product of transforms is the transform of the convolution ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-5|Theorem §CA.3.5]], 3, in $\mathcal S'$ with one factor in $\mathcal S$; the same rule in three dimensions). So Step 1 is $\int d^3y\,U(t, \mathbf x - \mathbf y)\psi(\mathbf y)$: $U(t, \cdot)$ is the kernel of [[§C1a.3 Causal Structure and the Causality of a Single Particle#^def-c1a-3-1|Def. §C1a.3.1]]. Taking $\psi \to \delta^3$ formally gives $\langle\mathbf x|e^{-iHt}|\mathbf 0\rangle$, the definition; the action on a test function $f$ is the transform moved onto $f$ ([[§CA.2 Generalized Functions#^def-ca-2-4|Def. §CA.2.4]]): $\int d^3x\,f(\mathbf x)e^{i\mathbf p\cdot\mathbf x} = \tilde f(-\mathbf p)$.
>
> **Step 3** ($t \to 0$). $|e^{-iE(\mathbf p)t}\tilde f(-\mathbf p)| \le |\tilde f(-\mathbf p)|$, integrable, and the integrand tends to $\tilde f(-\mathbf p)$; by dominated convergence ([[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|Theorem §CA.1.1]]) $U(t, \cdot)[f] \to \int\frac{d^3p}{(2\pi)^3}\tilde f(-\mathbf p) = f(\mathbf 0)$ by Fourier inversion, which is $\delta^3[f]$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]]).
>
> **What the derivation shows.**
> - $U$ is a distribution in $\mathbf x$ for every $t$, whatever $E(\mathbf p)$; whether it is a function, and where it vanishes, is decided by the form of $E$.
> - Its time derivative is $-i$ times the transform of $E(\mathbf p)e^{-iE(\mathbf p)t}$: $i\partial_tU = \hat HU$, the Schrödinger equation for the kernel.
> - Used next: the nonrelativistic case (Theorem §C1a.3.3) and the relativistic one (Theorems §C1a.3.4–§C1a.3.6; exactly, [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-7|Theorem §C2b.3.7]]–[[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-7|Theorem §C2b.4.7]]).

^der-c1a-3-2

*Uses:* [[§CA.3 Fourier Transforms and Fourier Tricks#^def-ca-3-1|Def. §CA.3.1]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-1|Theorem §CA.3.1]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-2|Theorem §CA.3.2]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-5|Theorem §CA.3.5]], [[§CA.2 Generalized Functions#^def-ca-2-4|Def. §CA.2.4]], [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|Theorem §CA.1.1]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]]

> [!theorem] Theorem §C1a.3.3: The Nonrelativistic Amplitude Is Nonzero Everywhere
> For $E = \mathbf p^2/2m$ and $t \neq 0$,
>
> $$
> U(t, \mathbf x) = \Bigl(\frac{m}{2\pi it}\Bigr)^{3/2}e^{imr^2/2t}, \qquad |U(t, \mathbf x)| = \Bigl(\frac{m}{2\pi|t|}\Bigr)^{3/2}\ \text{ for every }\mathbf x :
> $$
>
> the amplitude is nonzero at every point after any time, and at fixed $\mathbf x \neq 0$ its modulus grows as $t \to 0$, although $U(t, \cdot) \to \delta^3$ as a distribution.
>
> *Source: PHY 513 Lecture 2, Part A ("Quantum Causality of Free Particle I–II") · the user's PHY 513 notes, Ch. 2 §2.2 (eq. for $U_{\text{NR}}$ and Derivation "The Gaussian integral behind the nonrelativistic amplitude") · PS §2.1, p. 14*

^thm-c1a-3-3

> [!derivation]- Derivation
> **Step 1** (the formula). $U(t, \mathbf x)$ for $\hat H = \hat{\mathbf P}^2/2m$ is the free propagator $K(\mathbf x, t; \mathbf 0, 0)$ of [[§C4.1 Propagators#^thm-c4-1-4|QM Theorem §C4.1.4]] with $\hbar = 1$, $T = t$, $\mathbf x' = \mathbf 0$. The computation there, a three-dimensional Gaussian with complex variance completed to a square ([[§CA.5 Gaussian Integrals, Stationary Phase and Bessel Functions#^thm-ca-5-1|Theorem §CA.5.1]], 1 with $s = it/2m$, continued to the imaginary axis as the Fresnel limit $t \to t - i0$, which also fixes the branch of the root), is the one in the user's notes and is not repeated.
>
> **Step 2** (the modulus). For real $t$, $|e^{imr^2/2t}| = 1$ and $|(m/2\pi it)^{3/2}| = (m/2\pi|t|)^{3/2}$, independent of $\mathbf x$.
>
> **Step 3** (growth and the delta limit). At fixed $\mathbf x \ne 0$ the modulus $\propto |t|^{-3/2}$ grows as $t \to 0$, while by [[§C1a.3 Causal Structure and the Causality of a Single Particle#^thm-c1a-3-2|Theorem §C1a.3.2]] the distribution tends to $\delta^3$. The two are compatible: the phase $mr^2/2t$ oscillates ever faster in $r$, and against a test function the oscillation wins (Step 3 of Derivation §C1a.3.2 is the proof).
>
> **What the derivation shows.**
> - The support of $U(t, \cdot)$ is all of $\mathbb R^3$ for every $t \neq 0$: propagation is instantaneous, which violates [[§C1a.3 Causal Structure and the Causality of a Single Particle#^pr-c1a-3-1|Principle §C1a.3.1]].
> - The obvious objection, that $\mathbf p^2/2m$ is not relativistic, is answered by Theorem §C1a.3.6 (and exactly by [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-8|Theorem §C2b.3.8]]).

^der-c1a-3-3

*Uses:* [[§C4.1 Propagators#^thm-c4-1-4|QM Theorem §C4.1.4]], [[§CA.5 Gaussian Integrals, Stationary Phase and Bessel Functions#^thm-ca-5-1|Theorem §CA.5.1]], [[§C1a.3 Causal Structure and the Causality of a Single Particle#^thm-c1a-3-2|Theorem §C1a.3.2]]

> [!theorem] Theorem §C1a.3.4: The Relativistic Amplitude Is a Boundary Value
> Let $E = E_{\mathbf p}$. The integral
>
> $$
> U(z, \mathbf x) \equiv \int\frac{d^3p}{(2\pi)^3}\,e^{-iE_{\mathbf p}z + i\mathbf p\cdot\mathbf x}
> $$
>
> converges absolutely and is analytic for $\operatorname{Im}z < 0$, and $U(t, \cdot) = \lim_{\varepsilon\to0^+}U(t - i\varepsilon, \cdot)$ in $\mathcal S'(\mathbb R^3)$ and, read as a distribution in $(t, \mathbf x)$, in $\mathcal S'(\mathbb R^4)$.
>
> *Source: derived here, from the user's PHY 513 notes, Ch. 2 §2.2 (Step 1 of Derivation "The relativistic amplitude in closed form": $t \to t - i\varepsilon$)*

^thm-c1a-3-4

> [!derivation]- Derivation
> **Step 1** (the modulus). Write $z = a - ib$, $b > 0$. Then $|e^{-iE_{\mathbf p}z}| = e^{-bE_{\mathbf p}}$, and since $E_{\mathbf p} \ge p$, $\int d^3p\,e^{-bE_{\mathbf p}} \le 4\pi\int_0^\infty p^2e^{-bp}\,dp = 8\pi/b^3 < \infty$.
>
> **Step 2** (analyticity). The $z$-derivative of the integrand is $-iE_{\mathbf p}$ times it, of modulus $E_{\mathbf p}e^{-bE_{\mathbf p}} \le (p + m)e^{-b_0p}$ for $b \ge b_0 > 0$, integrable uniformly in $z$. By [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|Theorem §CA.1.1]], 2, applied to $\partial/\partial a$ and $\partial/\partial b$ separately, $U$ has continuous partial derivatives obtained under the integral; since the integrand satisfies $\partial_b = -i\partial_a$ (the Cauchy–Riemann equations for $z = a - ib$), so does $U$, and the complex derivative exists ([[§CA.4 Contour Integration#^def-ca-4-2|Def. §CA.4.2]]). (The same estimate with the weight $1/2E_{\mathbf p}$ is Steps 1–3 of [[§C2b.2 The Wightman Function#^der-c2b-2-5|Derivation §C2b.2.5]], for the Wightman function.)
>
> **Step 3** (the boundary value). For $f \in \mathcal S(\mathbb R^3)$ and $\varepsilon > 0$ the double integral over $(\mathbf x, \mathbf p)$ converges absolutely, so (Fubini) $\int d^3x\,f(\mathbf x)\,U(t - i\varepsilon, \mathbf x) = \int\frac{d^3p}{(2\pi)^3}e^{-iE_{\mathbf p}t}e^{-\varepsilon E_{\mathbf p}}\tilde f(-\mathbf p)$. The integrand is bounded by $|\tilde f(-\mathbf p)|$, independently of $\varepsilon$; by dominated convergence the limit is $\int\frac{d^3p}{(2\pi)^3}e^{-iE_{\mathbf p}t}\tilde f(-\mathbf p) = U(t, \cdot)[f]$ ([[§C1a.3 Causal Structure and the Causality of a Single Particle#^thm-c1a-3-2|Theorem §C1a.3.2]]).
>
> ⚑ By-product: "$t \to t - i\varepsilon$" is not a regulator added by hand but the definition of $U$ at real $t$, and it works because every $E_{\mathbf p} > 0$; the Wightman function will be defined by the same prescription ([[§C2b.2 The Wightman Function#^thm-c2b-2-5|Theorem §C2b.2.5]]) → stated in [[§C1a.3 Causal Structure and the Causality of a Single Particle#^thm-c1a-3-4|Theorem §C1a.3.4]].
>
> **Step 4** (on $\mathbb R^4$). Read $U$ as a distribution on $\mathbb R^4$ by $U[f] = \int dt\,U(t, \cdot)[f(t, \cdot)]$; Step 3 with $f \in \mathcal S(\mathbb R^4)$ and dominated convergence in $(t, \mathbf p)$ gives $U = \lim U(t - i\varepsilon, \mathbf x)$ in $\mathcal S'(\mathbb R^4)$.
>
> **What the derivation shows.**
> - The amplitude is a boundary value of an analytic function, because every $E_{\mathbf p} > 0$; the analytic continuation is what makes the radial integral below absolutely convergent.
> - $U$ is the same mode integral as the Wightman function with the weight $1/2E_{\mathbf p}$ replaced by $1$; the relation $U = 2i\partial_tD_W$ and every closed form of $U$ follow once $D_W$ is known ([[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-7|Theorem §C2b.3.7]]).
> - Used next: the radial integral (Theorem §C1a.3.5) and the saddle point (Theorem §C1a.3.6).

^der-c1a-3-4

*Uses:* [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|Theorem §CA.1.1]], [[§CA.4 Contour Integration#^def-ca-4-2|Def. §CA.4.2]], [[§C1a.3 Causal Structure and the Causality of a Single Particle#^thm-c1a-3-2|Theorem §C1a.3.2]]

> [!theorem] Theorem §C1a.3.5: The Relativistic Amplitude as a Radial Integral
> For $\operatorname{Im}z < 0$ and $r > 0$,
>
> $$
> U(z, r) = \frac{1}{2\pi^2r}\int_0^\infty dp\;p\sin(pr)\,e^{-iE_pz} = \frac{1}{4\pi^2ir}\int_{-\infty}^{\infty}dp\;p\,e^{i(pr - E_pz)},
> $$
>
> both absolutely convergent. At real $t$ these are the lecture's and PS's formulas, which do not converge as integrals (the integrand grows like $p$) and mean the limit $z = t - i\varepsilon$, $\varepsilon \to 0^+$, of [[§C1a.3 Causal Structure and the Causality of a Single Particle#^thm-c1a-3-4|Theorem §C1a.3.4]].
>
> *Source: PHY 513 Lecture 2, Part A ("Relativistic Quantum Causality") · the user's PHY 513 notes, Ch. 2 §2.2 (Derivation "Reduction to a radial integral", eqs. for the radial and folded forms) · PS §2.1, p. 14*

^thm-c1a-3-5

> [!derivation]- Derivation
> **Step 1** (spherical coordinates). The integrand of [[§C1a.3 Causal Structure and the Causality of a Single Particle#^thm-c1a-3-4|Theorem §C1a.3.4]], 1 depends on the direction of $\mathbf p$ only through $\mathbf p\cdot\mathbf x = pr\cos\theta$, $\theta$ the angle between $\mathbf p$ and $\mathbf x$. Choose the polar axis along $\mathbf x$ (a rotation of the integration variable, Jacobian $1$: [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|Theorem §CA.3.7]]); $d^3p = p^2\,dp\,\sin\theta\,d\theta\,d\varphi$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-8|Theorem §CA.3.8]]). All integrals converge absolutely for $\operatorname{Im}z < 0$ (Step 1 of Derivation §C1a.3.4), so they may be done in any order.
>
> **Step 2** (the angles). The $\varphi$ integral gives $2\pi$. With $u = \cos\theta$, $du = -\sin\theta\,d\theta$, $\theta: 0 \to \pi$ becomes $u: 1 \to -1$, and the sign of $du$ restores the order: $\int_0^\pi\sin\theta\,e^{ipr\cos\theta}d\theta = \int_{-1}^1e^{ipru}du = \frac{e^{ipr} - e^{-ipr}}{ipr} = \frac{2\sin pr}{pr}$. So
>
> $$
> U = \frac{2\pi}{(2\pi)^3}\int_0^\infty p^2\,dp\,\frac{2\sin pr}{pr}\,e^{-iE_pz} = \frac{1}{2\pi^2r}\int_0^\infty dp\;p\sin(pr)\,e^{-iE_pz} .
> $$
>
> **Step 3** (fold onto the line). $E_{-p} = E_p$, so $p\sin(pr)e^{-iE_pz}$ is even in $p$ and $\int_0^\infty = \frac12\int_{-\infty}^\infty$. Write $\sin pr = (e^{ipr} - e^{-ipr})/2i$. In the $e^{-ipr}$ term substitute $p \to -p$ (Jacobian $1$, limits $\pm\infty$ exchanged and restored by the sign of $dp$, prefactor $p \to -p$, $E_p$ unchanged; [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|Theorem §CA.3.7]], 1): $-\int p\,e^{-ipr}e^{-iE_pz}dp = +\int p\,e^{ipr}e^{-iE_pz}dp$. The two terms are equal, and
>
> $$
> U = \frac{1}{2\pi^2r}\cdot\frac12\cdot\frac{2}{2i}\int_{-\infty}^{\infty}dp\;p\,e^{ipr}e^{-iE_pz} = \frac{1}{4\pi^2ir}\int_{-\infty}^{\infty}dp\;p\,e^{i(pr - E_pz)} .
> $$
>
> **What the derivation shows.**
> - The lecture's remark that "subtleties about convergence are OK for spatial separation" is made precise in two places: at $\operatorname{Im}z < 0$ there are no subtleties, and the limit to real $t$ is an ordinary function exactly off the light cone ([[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-8|Theorem §C2b.3.8]], [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-10|Theorem §C2b.3.10]]).
> - The same reduction with the weight $1/2E_p$ is the equal-time Wightman function ([[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-3|Theorem §C2b.3.3]], second route, Steps 2–3).
> - Used next: the saddle point of Theorem §C1a.3.6, and the second route of [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-8|Theorem §C2b.3.8]].

^der-c1a-3-5

*Uses:* [[§C1a.3 Causal Structure and the Causality of a Single Particle#^thm-c1a-3-4|Theorem §C1a.3.4]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|Theorem §CA.3.7]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-8|Theorem §CA.3.8]]

> [!theorem] Theorem §C1a.3.6: The Leak Is Exponentially Small but Not Zero
> For $r > |t|$ and $m\rho \gg 1$, $\rho = \sqrt{r^2 - t^2}$, to leading order,
>
> $$
> U(t, \mathbf x) \simeq \frac{i\,m^{3/2}\,t}{(2\pi\rho)^{3/2}\,\rho}\,e^{-m\rho} :
> $$
>
> not zero at spacelike points with $t \neq 0$, and damped over the Compton wavelength $1/m$. In particular $U \propto e^{-m\sqrt{\mathbf x^2 - t^2}}$ (PS §2.1). The exact amplitude, which vanishes at no spacelike point with $t \ne 0$, and the next term $1 + 15/8m\rho$ are [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-8|Theorem §C2b.3.8]] and [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-9|Theorem §C2b.3.9]].
>
> *Source: PHY 513 Lecture 2, Part A ("Saddle Point Approximation", "Quantum Causality is Violated") · the user's PHY 513 notes, Ch. 2 §2.2 (check (iii); Derivation "Saddle point of the relativistic amplitude") · PS §2.1, p. 14*

^thm-c1a-3-6

> [!derivation]- Derivation (the saddle point, as in the lecture)
> The lecture needs only the exponent, and a saddle point produces it without the closed form. Take $0 < t < r$ (for $t < 0$ use $U(-t, \mathbf x) = \overline{U(t, \mathbf x)}$: conjugating the mode integral of [[§C1a.3 Causal Structure and the Causality of a Single Particle#^thm-c1a-3-2|Theorem §C1a.3.2]] gives $U(-t, -\mathbf x)$, and the substitution $\mathbf p \to -\mathbf p$ (Jacobian $1$, $E_{-\mathbf p} = E_{\mathbf p}$) shows that $U(-t, \cdot)$ is even in $\mathbf x$; at $t = 0$, $U = 0$ off the origin).
>
> **Step 1** (the phase). By [[§C1a.3 Causal Structure and the Causality of a Single Particle#^thm-c1a-3-5|Theorem §C1a.3.5]], $U = \frac{1}{4\pi^2ir}\int dp\;p\,e^{iS(p)}$ with $S(p) = pr - t\sqrt{p^2 + m^2}$ (the limit $z = t - i\varepsilon$ understood). This is the phase of the Wightman function's [[§CA.5 Gaussian Integrals, Stationary Phase and Bessel Functions#^ex-ca-5-1|Example §CA.5.1]]; only the prefactor differs, $p$ here against $p/\sqrt{p^2 + m^2}$ there.
>
> **Step 2** (stationary points). $S'(p) = r - \frac{pt}{\sqrt{p^2 + m^2}} = 0$ gives $r^2(p^2 + m^2) = p^2t^2$, i.e. $p^2(r^2 - t^2) = -m^2r^2$. Inside the cone ($r < t$) the root is real and $r/t = p/E_p$, the velocity of a classical particle of momentum $p$: stationary phase on the real axis ([[§C4.2 The Feynman Path Integral#^thm-c4-2-5|QM Theorem §C4.2.5]]) gives an oscillating amplitude dominated by the classical path. Outside, no real momentum has velocity $r/t > 1$, and the saddle moves to $p_0 = imr/\rho$ (Example §CA.5.1, Step 2).
>
> **Step 3** (the branch at the saddle). $S'(p_0) = 0$ forces $\sqrt{p_0^2 + m^2} = p_0t/r = imt/\rho$ (Example §CA.5.1, Step 3); indeed $p_0^2 + m^2 = m^2(1 - r^2/\rho^2) = -m^2t^2/\rho^2$.
>
> **Step 4** (the exponent). $S(p_0) = \frac{imr}{\rho}r - t\,\frac{imt}{\rho} = \frac{im(r^2 - t^2)}{\rho} = im\rho$, so $e^{iS(p_0)} = e^{-m\rho} = e^{-m\sqrt{r^2 - t^2}}$: the lecture's result. The approximation needs a large exponent, $m\rho \gg 1$ (the lecture's "$\mathbf x^2 - t^2 \gg 1$" in units $m = 1$).
>
> **Step 5** (the Gaussian factor). $S''(p) = -tm^2/(p^2 + m^2)^{3/2}$, so $S''(p_0) = -tm^2/(imt/\rho)^3 = -i\rho^3/mt^2$ and $\Phi = iS$ has $\Phi''(p_0) = \rho^3/mt^2 > 0$. The steepest-descent direction is vertical, $p = p_0 + iq$, and the Gaussian factor is $i\sqrt{2\pi/\Phi''(p_0)} = it\sqrt{2\pi m/\rho^3}$ ([[§CA.5 Gaussian Integrals, Stationary Phase and Bessel Functions#^thm-ca-5-2|Theorem §CA.5.2]], 2; Example §CA.5.1, Steps 5–6).
>
> **Step 6** (assemble, with the prefactor $p_0$). The difference from Example §CA.5.1 is $f(p_0) = p_0 = imr/\rho$:
>
> $$
> U \simeq \frac{1}{4\pi^2ir}\cdot\frac{imr}{\rho}\cdot e^{-m\rho}\cdot it\sqrt{\frac{2\pi m}{\rho^3}} = \frac{i\,m\,t\sqrt{2\pi m}}{4\pi^2\rho^{5/2}}\,e^{-m\rho} = \frac{i\,m^{3/2}\,t}{2^{3/2}\pi^{3/2}\rho^{5/2}}\,e^{-m\rho},
> $$
>
> the leading term of the theorem, phase included.
>
> **Step 7** (why the steepest descent is legitimate). $|p_0| = mr/\rho > m$, so the saddle lies on the cut of $\sqrt{p^2 + m^2}$, where the integrand is not analytic; PS's "we may freely push the contour upward" passes over this. On the cut representation of [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-8|Theorem §C2b.3.8]] (Step 5 of its second route, which uses only the radial integral of Theorem §C1a.3.5) the exponent $h(\varrho) = -\varrho r + t\sqrt{\varrho^2 - m^2}$ of the dominant term $\frac12e^{ts}$ is real: $h'(\varrho) = -r + t\varrho/s = 0$ gives $\varrho_0 = mr/\rho$, $s_0 = mt/\rho$, $h(\varrho_0) = -mr^2/\rho + mt^2/\rho = -m\rho$, and $h''(\varrho_0) = -tm^2/s_0^3 = -\rho^3/mt^2$. Laplace's method ([[§CA.5 Gaussian Integrals, Stationary Phase and Bessel Functions#^thm-ca-5-2|Theorem §CA.5.2]], 1; [[§CA.5 Gaussian Integrals, Stationary Phase and Bessel Functions#^rem-ca-5-2|Remark: When the saddle sits on a branch cut]]) gives $\int\varrho\,e^{-\varrho r}\sinh(ts)\,d\varrho \simeq \frac12\varrho_0\,e^{-m\rho}\sqrt{2\pi/|h''(\varrho_0)|} = \frac{mr}{2\rho}\,e^{-m\rho}\,t\sqrt{\frac{2\pi m}{\rho^3}}$, and multiplying by $\frac{i}{2\pi^2r}$ reproduces Step 6.
>
> **What the derivation shows.**
> - The saddle alone fixes the exponent $e^{-m\rho}$; the prefactor needs the Gaussian width and agrees with the closed form.
> - The complex saddle is the point $\varrho_0 = mr/\rho$ of the real cut integral seen from the other representation.
>
> *Source: PHY 513 Lecture 2, Part A ("Saddle Point Approximation") · the user's PHY 513 notes, Ch. 2 §2.2 (Derivation "Saddle point of the relativistic amplitude", including "The prefactor") · PS §2.1, p. 14*

^der-c1a-3-6

*Uses:* [[§C1a.3 Causal Structure and the Causality of a Single Particle#^thm-c1a-3-5|Theorem §C1a.3.5]], [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-8|Theorem §C2b.3.8]] (cut representation, Step 7), [[§CA.5 Gaussian Integrals, Stationary Phase and Bessel Functions#^ex-ca-5-1|Example §CA.5.1]], [[§CA.5 Gaussian Integrals, Stationary Phase and Bessel Functions#^thm-ca-5-2|Theorem §CA.5.2]], [[§CA.5 Gaussian Integrals, Stationary Phase and Bessel Functions#^rem-ca-5-2|Remark: When the saddle sits on a branch cut]], [[§C4.2 The Feynman Path Integral#^thm-c4-2-5|QM Theorem §C4.2.5]]

> [!remark] Remark: How field theory repairs causality
> The calculation assumed one particle at the origin and one at $\mathbf x$, with single-particle mechanics in between. With any number of particles ([[§C1a.1 Why Quantum Field Theory#^law-c1a-1-1|Law §C1a.1.1]]) the net process "one in, one out" happens in two ways: annihilate at one point and create at the other, in either order. For spacelike points there is no invariant order: some observers see the origin evolve into $\mathbf x$, others $\mathbf x$ into the origin, and a theory that answered which would be wrong even classically. Quantum field theory adds both amplitudes, and the criterion for influence becomes the commutator of fields, which vanishes at spacelike separation ([[§C2b.4 Microcausality and the Commutator Function#^pr-c2b-4-1|Principle §C2b.4.1]], [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-5|Theorem §C2b.4.5]]); for a charged field the second ordering is the antiparticle ([[§C2b.4 Microcausality and the Commutator Function#^rem-c2b-4-2|Remark: Two orderings that cancel; why antiparticles must exist]]). [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-7|Theorem §C2b.4.7]] is this bookkeeping done on $U$ itself.
>
> *Source: PHY 513 Lecture 2, Part A ("Resolution in Quantum Field Theory") · the user's PHY 513 notes, Ch. 2 §2.2 ("Causality is violated, and how field theory repairs it") · PS §2.1, p. 14*

^rem-c1a-3-3

> [!remark] Remark: Backward in time, then and now
> The relativistic quantum mechanics of the 1950s and 60s handled the leak by averaging forward and backward propagation, since one cannot know which is right. That is not entirely wrong: part 1 of [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-7|Theorem §C2b.4.7]] says the average is causal, and this is how the cancellation was first found. But it stretches single-particle quantum mechanics past what it can describe. Quantum field theory follows a principled line, and the spacelike commutator simply comes out zero.
>
> *Source: the user's PHY 513 notes, Ch. 2 §2.2 (Caution "Particles moving backward in time")*

^rem-c1a-3-4

> [!remark]- ★ Remark: No positive-energy amplitude can be strictly causal
> The leak is not an accident of $E_{\mathbf p} = \sqrt{\mathbf p^2 + m^2}$. If $U(t, \cdot)$ were supported in the ball $|\mathbf x| \le |t|$, it would be a distribution of compact support, and by the Paley–Wiener–Schwartz theorem (Hörmander, *The Analysis of Linear Partial Differential Operators I*, Thm. 7.3.1) its Fourier transform $e^{-iE(\mathbf p)t}$ would extend to an entire function of $\mathbf p \in \mathbb C^3$. For $E = \sqrt{\mathbf p^2 + m^2}$ it does not: going once around the branch point $\mathbf p^2 = -m^2$ changes the sign of the root and turns $e^{-iEt}$ into $e^{+iEt}$; for $m = 0$, $|\mathbf p|$ is not even smooth at $0$. Hegerfeldt's theorem (1974) generalizes this: positivity of the energy alone forbids a localized single-particle state from staying inside its light cone. Field theory does not localize particles; it localizes observables.
>
> *Source: stated here (standard: Hörmander, Thm. 7.3.1; G. C. Hegerfeldt, Phys. Rev. D 10, 3320 (1974)); beyond the course*

^rem-c1a-3-5

> [!remark]- Connections
> - The amplitude is the propagator of [[§C4.1 Propagators#^def-c4-1-1|QM Def. §C4.1.1]] for the Hamiltonian $\sqrt{\hat{\mathbf P}^2 + m^2}$; at imaginary time $U(-i\tau, \cdot)$ is the kernel of $e^{-\hat H\tau}$, the relativistic analogue of the heat kernel ([[§B4.2 Random Walks, the Central Limit Theorem and Diffusion#^thm-b4-2-6|TH Theorem §B4.2.6]]) that the nonrelativistic propagator becomes at imaginary time.
> - Sakurai's argument against the square-root Hamiltonian, that it is nonlocal and must eventually violate causality for a localized wave function ([[§C13.1★ Relativistic Wave Equations and the Klein–Gordon Field#^rem-c13-1-1|QM Remark: Why square]]), is made quantitative by [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-8|Theorem §C2b.3.8]]: the nonlocality has range $\hbar/mc$.
> - $U = 2i\partial_tD_W$ ([[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-7|Theorem §C2b.3.7]]) is the relativistic normalization at work: the one-particle states $|\mathbf p\rangle$ of field theory carry $\sqrt{2E_{\mathbf p}}$ ([[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-1|Def. §C2a.4.1]]), and $\hat\phi(x)|0\rangle$ creates a particle at $x$ with the weight $1/2E_{\mathbf p}$ ([[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-6|Theorem §C2a.4.6]]); the single-particle position states $|\mathbf x\rangle$ used here have weight $1$, which is why $U$ and $D_W$ differ by a time derivative.
> - The phase $pr - t\sqrt{p^2 + m^2}$ and its complex saddle are shared with the Wightman function ([[§CA.5 Gaussian Integrals, Stationary Phase and Bessel Functions#^ex-ca-5-1|Example §CA.5.1]]); the cut, the saddle on it and the arc condition $r > |t|$ are drawn in the figure of [[§CA.4 Contour Integration|§CA.4]]. A complex saddle giving an exponentially small amplitude is the field-theory cousin of tunnelling, whose WKB exponent is likewise a saddle value ([[§B9.4 Tunnelling and the Connection Formulas|QM §B9.4]]).
> - For $m = 0$ the single-particle amplitude leaks as a power law, $t/(r^2 - t^2)^2$ ([[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-8|Theorem §C2b.3.8]]), while the massless commutator function lives on the cone alone ([[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-8|Theorem §C2b.4.8]]): field theory propagates massless signals sharply, single-particle mechanics does not.
> - The decay length $1/m$ of the leak is the Compton wavelength of [[§B4.1 The Klein–Gordon Equation#^def-b4-1-2|REL Def. §B4.1.2]] and the range of the Yukawa potential ([[§B4.1 The Klein–Gordon Equation#^rem-b4-1-4|REL Remark: Static solutions and the Yukawa potential]]); the same $e^{-m\rho}$ governs the vacuum correlations $D_1$ outside the cone ([[§C2b.4 Microcausality and the Commutator Function#^rem-c2b-4-3|Remark: Influence and correlation]]), and by [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-7|Theorem §C2b.4.7]] that is no coincidence.
> - [[§C1a.3 Causal Structure and the Causality of a Single Particle#^pr-c1a-3-1|Principle §C1a.3.1]] for a classical field with a source is the support of the retarded Green's function in the forward cone ([[§C2b.5 Green's Functions and Contours#^thm-c2b-5-6|Theorem §C2b.5.6]]) and, for the quantum field, the domain-of-dependence statement ([[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-13|Theorem §C2b.4.13]]); in electromagnetism it is the retarded potential ([[§B11.1★ Potentials, Gauges and Retarded Potentials|EM §B11.1★]]).
> - Relativity is tested to extraordinary precision; the photon mass, for instance, is bounded below $10^{-18}$ eV (PDG, from solar-wind magnetohydrodynamics, quoted in the lecture's discussion). Nothing in the course assumes a violation of local Lorentz invariance.
> - The distributional statements used here are the CA tools: the Fourier transform on $\mathcal S'$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-2|Theorem §CA.3.2]]) makes $U(t, \cdot)$ a distribution for every $E$; boundary values of analytic functions ([[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-1|Theorem §CA.6.1]]) give it a meaning on the cone; distributional limits ([[§CA.2 Generalized Functions#^thm-ca-2-5|Theorem §CA.2.5]]) carry $U = 2i\partial_tD_W$ from the analytic functions to the boundary values.
