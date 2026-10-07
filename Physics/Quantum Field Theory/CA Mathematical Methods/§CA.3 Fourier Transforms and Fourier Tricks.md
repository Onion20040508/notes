---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: CA
section: CA.3
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§CA.2 Generalized Functions]] · ↑ [[· CA Mathematical Methods]] · [[§CA.4 Contour Integration]] →

*Sources: the user's PHY 513 notes, App. A §§A.2–A.3, Ch. 4 §4.3 (the six rules), Ch. 6 §6.3 (the four-dimensional transform) · standard results stated here, where marked: Stein & Shakarchi, Fourier Analysis (Princeton Lectures I), Ch. 5–6; Hörmander I, Ch. 7; Reed & Simon I, Ch. IX; DLMF §§10.9, 10.22.*

Every mode computation of [[· C2a The Quantum Scalar Field|C2a]] is a short sequence of Fourier moves: write a plane wave, exchange the $\mathbf x$- and $\mathbf p$-integrals, collect a $(2\pi)^3\delta^3$, relabel $\mathbf p \to -\mathbf p$, let a damping factor go to zero. This section states each move as a rule and says in what sense it holds: as an absolutely convergent integral for wave packets, as an identity in $\mathcal S'$ ([[§CA.2 Generalized Functions|§CA.2]]), or as a limit $\varepsilon \to 0^+$. It starts from the transform and the delta function of [[§B4.4 Fourier Transforms and the Delta Function#^def-b4-4-1|WO Def. §B4.4.1]] and [[§B4.4 Fourier Transforms and the Delta Function#^thm-b4-4-3|WO Theorem §B4.4.3]], in that subject's convention, and from Fubini's theorem ([[§25 Invariance Properties and Fubini's Theorem#^thm-25-6|551 Thm. §25.6]]). New here, beyond the user's six rules: inversion and Plancherel on $\mathcal S$, the transform of distributions, the plane-wave delta function with the reason it is not a convergent integral, the exchange of integrals as Fubini for wave packets, changes of variable, damping factors and the $i\varepsilon$ limits of the propagator denominators, and transforms of Lorentz-invariant functions.

## Conventions

> [!definition] Definition §CA.3.1: Fourier Transform in Space and Spacetime
> In space and in spacetime, with $p\cdot x = p^0t - \mathbf p\cdot\mathbf x$,
>
> $$
> f(\mathbf x) = \int\frac{d^3k}{(2\pi)^3}\,\tilde f(\mathbf k)\,e^{i\mathbf k\cdot\mathbf x}, \quad \tilde f(\mathbf k) = \int d^3x\,f(\mathbf x)\,e^{-i\mathbf k\cdot\mathbf x}; \qquad f(x) = \int\frac{d^4p}{(2\pi)^4}\,\tilde f(p)\,e^{-ip\cdot x}, \quad \tilde f(p) = \int d^4x\,f(x)\,e^{ip\cdot x} .
> $$
>
> All factors of $2\pi$ sit with the momentum integral. The phase $e^{-ip\cdot x} = e^{-ip^0t}\,e^{+i\mathbf p\cdot\mathbf x}$ has opposite signs on time and space.
>
> *Source: the user's PHY 513 notes, Ch. 6 §6.3 (Definition "Conventions") · PS §2.4, eq. (2.57) · Yu, same convention*

^def-ca-3-1

> [!caution] Caution: Two conventions in the vault
> Oscillations and waves ([[§B4.4 Fourier Transforms and the Delta Function#^def-b4-4-1|WO Def. §B4.4.1]]) puts $1/2\pi$ in the forward transform and synthesizes from $e^{+i\omega t}$, the engineering time dependence of that subject. Here the time factor is the positive-frequency $e^{-iEt}$ of quantum mechanics and the space factor is the $e^{+i\mathbf p\cdot\mathbf x}$ of the mode expansions; the opposite signs are the Minkowski metric, not an inconsistency. PS, Yu and the user's notes use the convention of Def. §CA.3.1; some books put $e^{+ip\cdot x}$ in the synthesis, which flips every sign below. Convert before combining formulas.

^cau-ca-3-1

## The transform on 𝒮 and on 𝒮′

> [!theorem] Theorem §CA.3.1: Fourier Inversion and Plancherel on 𝒮
> In the spatial convention of [[§CA.3 Fourier Transforms and Fourier Tricks#^def-ca-3-1|Def. §CA.3.1]] (the spacetime case is the same with four variables):
> 1. $f \mapsto \tilde f$ maps $\mathcal S(\mathbb R^3)$ onto $\mathcal S(\mathbb R^3)$, continuously, and $f(\mathbf x) = \int\frac{d^3k}{(2\pi)^3}\tilde f(\mathbf k)e^{i\mathbf k\cdot\mathbf x}$, both integrals absolutely convergent.
> 2. *(Multiplication formula)* $\int d^3k\,\tilde f(\mathbf k)\,g(\mathbf k) = \int d^3x\,f(\mathbf x)\,\tilde g(\mathbf x)$ for $f, g \in \mathcal S$.
> 3. *(Parseval–Plancherel)* $\int d^3x\,\overline{f}g = \int\frac{d^3k}{(2\pi)^3}\overline{\tilde f}\,\tilde g$; the transform extends to $L^2$, with $\int d^3x\,|f|^2 = \int\frac{d^3k}{(2\pi)^3}|\tilde f|^2$.
>
> *Source: standard; stated here in the field-theory convention (Stein & Shakarchi, Fourier Analysis, Ch. 5–6) · the same theorems in the WO convention: [[§B4.4 Fourier Transforms and the Delta Function#^thm-b4-4-1|WO Theorem §B4.4.1]], [[§B4.4 Fourier Transforms and the Delta Function#^thm-b4-4-4|WO Theorem §B4.4.4]]*

^thm-ca-3-1

> [!derivation]- Derivation
> **Step 1** ($\mathcal S \to \mathcal S$). Integration by parts (no boundary terms for $f \in \mathcal S$) gives $\int d^3x\,(\partial_jf)e^{-i\mathbf k\cdot\mathbf x} = ik_j\tilde f$, and differentiation under the integral ([[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|Theorem §CA.1.1]], 2) gives $\partial_{k_j}\tilde f = \int d^3x\,(-ix_j)f\,e^{-i\mathbf k\cdot\mathbf x}$. So $k^\alpha\partial_k^\beta\tilde f$ is the transform of a finite combination of $x^\gamma\partial^\delta f$, each in $\mathcal S \subset L^1$, hence bounded: $\|\tilde f\|_{\alpha,\beta} \le C\sum\|f\|_{\gamma,\delta}$ with $|\gamma| \le |\beta| + 4$ (four extra powers of $|\mathbf x|$ make $\int d^3x$ converge). So $\tilde f \in \mathcal S$, continuously.
>
> **Step 2** (regulate the synthesis). For $f \in \mathcal S$ and $\varepsilon > 0$ put $I_\varepsilon(\mathbf x) = \int\frac{d^3k}{(2\pi)^3}\tilde f(\mathbf k)e^{i\mathbf k\cdot\mathbf x}e^{-\varepsilon\mathbf k^2}$. Insert $\tilde f(\mathbf k) = \int d^3y\,f(\mathbf y)e^{-i\mathbf k\cdot\mathbf y}$; the double integral of $|f(\mathbf y)|e^{-\varepsilon\mathbf k^2}$ is finite, so Fubini ([[§25 Invariance Properties and Fubini's Theorem#^thm-25-6|551 Thm. §25.6]]) allows the exchange:
>
> $$
> I_\varepsilon(\mathbf x) = \int d^3y\,f(\mathbf y)\int\frac{d^3k}{(2\pi)^3}e^{-\varepsilon\mathbf k^2 + i\mathbf k\cdot(\mathbf x - \mathbf y)} = \int d^3y\,f(\mathbf y)\,\frac{e^{-(\mathbf x - \mathbf y)^2/4\varepsilon}}{(4\pi\varepsilon)^{3/2}} ,
> $$
>
> by the Gaussian integral [[§CA.5 Gaussian Integrals, Stationary Phase and Bessel Functions#^thm-ca-5-1|Theorem §CA.5.1]], 1 ($n = 3$, $s = \varepsilon$).
>
> **Step 3** (two limits of one quantity). The heat kernel $h_\varepsilon(\mathbf u) = (4\pi\varepsilon)^{-3/2}e^{-\mathbf u^2/4\varepsilon}$ is a nascent delta function ([[§CA.2 Generalized Functions#^thm-ca-2-4|Theorem §CA.2.4]], 3, with $\rho(\mathbf u) = (4\pi)^{-3/2}e^{-\mathbf u^2/4}$ and scale $\sqrt\varepsilon$), so with $\mathbf y = \mathbf x - \mathbf u$, $I_\varepsilon(\mathbf x) = \int d^3u\,h_\varepsilon(\mathbf u)f(\mathbf x - \mathbf u) \to f(\mathbf x)$. On the other hand $\tilde f \in L^1$ (Step 1) and $e^{-\varepsilon\mathbf k^2} \to 1$ under the bound $|\tilde f|$, so by dominated convergence $I_\varepsilon(\mathbf x) \to \int\frac{d^3k}{(2\pi)^3}\tilde f e^{i\mathbf k\cdot\mathbf x}$. The two limits are equal: inversion. Onto: every $g \in \mathcal S$ is the transform of $\check g(\mathbf x) = \int\frac{d^3k}{(2\pi)^3}g(\mathbf k)e^{i\mathbf k\cdot\mathbf x}$, which is in $\mathcal S$ by Step 1.
>
> **Step 4** (part 2). $\int d^3k\,g(\mathbf k)\int d^3x\,f(\mathbf x)e^{-i\mathbf k\cdot\mathbf x} = \int d^3x\,f(\mathbf x)\int d^3k\,g(\mathbf k)e^{-i\mathbf k\cdot\mathbf x}$, by Fubini ($\int\!\!\int|f||g| < \infty$).
>
> **Step 5** (part 3). Write $g$ by inversion and exchange (Fubini): $\int d^3x\,\overline{f(\mathbf x)}\int\frac{d^3k}{(2\pi)^3}\tilde g(\mathbf k)e^{i\mathbf k\cdot\mathbf x} = \int\frac{d^3k}{(2\pi)^3}\tilde g(\mathbf k)\,\overline{\int d^3x\,f(\mathbf x)e^{-i\mathbf k\cdot\mathbf x}} = \int\frac{d^3k}{(2\pi)^3}\tilde g\,\overline{\tilde f}$. The extension to $L^2$ uses density of $\mathcal S$ in $L^2$ and is quoted (Stein & Shakarchi, Real Analysis, Ch. 5).
>
> ⚑ By-product: no delta function appears; inversion is proved with a nascent one, the heat kernel. "$\int d^3x\,e^{i\mathbf k\cdot\mathbf x} = (2\pi)^3\delta^3(\mathbf k)$" is the shorthand for this proof → [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]].
>
> **What the derivation shows.**
> - All factors of $2\pi$ sit in the $\mathbf k$ measure, so Plancherel carries $(2\pi)^{-3}$ on the momentum side; this is the normalization of every $\int d^3p/(2\pi)^3$ in C2.
> - Assumption used: $f \in \mathcal S$ (or $L^1$ with $\tilde f \in L^1$); plane waves are not covered and need [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-2|Theorem §CA.3.2]].

^der-ca-3-1

*Uses:* [[§25 Invariance Properties and Fubini's Theorem#^thm-25-6|551 Thm. §25.6]], [[§CA.5 Gaussian Integrals, Stationary Phase and Bessel Functions#^thm-ca-5-1|Theorem §CA.5.1]], [[§CA.2 Generalized Functions#^thm-ca-2-4|Theorem §CA.2.4]], [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|Theorem §CA.1.1]]

> [!theorem] Theorem §CA.3.2: The Fourier Transform of Tempered Distributions
> For $T \in \mathcal S'$ the transform is $\tilde T[\varphi] \equiv T[\tilde\varphi]$ ([[§CA.2 Generalized Functions#^def-ca-2-4|Def. §CA.2.4]]). Then:
> 1. $\tilde T \in \mathcal S'$, and for $T = T_\psi$ with $\psi \in L^1$ it is the function transform: $\widetilde{T_\psi} = T_{\tilde\psi}$.
> 2. $T \mapsto \tilde T$ is a bijection of $\mathcal S'$, and $T_\varepsilon \to T$ implies $\tilde T_\varepsilon \to \tilde T$: a limit may be taken before or after transforming.
> 3. $\tilde\delta = 1$, and the transform of $1$ is $(2\pi)^n\delta^n$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]]).
>
> *Source: the user's PHY 513 notes, App. A §A.4 (tempered distributions, $\tilde T[\varphi] = T[\tilde\varphi]$) · standard (Hörmander I, §7.1; Reed & Simon I, Ch. IX)*

^thm-ca-3-2

> [!derivation]- Derivation
> **Step 1** (part 1: tempered). Write $\mathcal F\varphi = \tilde\varphi$ and $\mathcal F^{-1}\varphi = \check\varphi$ for the transform and its inverse. $\varphi \mapsto \tilde\varphi$ is linear and continuous on $\mathcal S$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-1|Theorem §CA.3.1]], 1), so $\tilde T = T\circ\mathcal F$ is a continuous linear map on $\mathcal S$.
>
> **Step 2** (part 1: consistent). For $\psi \in L^1$ and $\varphi \in \mathcal S$, Fubini gives the multiplication formula of Theorem §CA.3.1, 2: $T_{\tilde\psi}[\varphi] = \int\tilde\psi\,\varphi = \int\psi\,\tilde\varphi = T_\psi[\tilde\varphi] = \widetilde{T_\psi}[\varphi]$. The definition is the only one consistent with functions.
>
> **Step 3** (part 2: inverse). With $\check\varphi$ the inverse transform, Theorem §CA.3.1 gives $\mathcal F\check\varphi = \varphi = \mathcal F^{-1}\tilde\varphi$. Define $\check T[\varphi] = T[\check\varphi]$. Then $\mathcal F^{-1}\tilde T[\varphi] = \tilde T[\check\varphi] = T[\mathcal F\check\varphi] = T[\varphi]$, and likewise in the other order.
>
> **Step 4** (part 2: limits). $\tilde T_\varepsilon[\varphi] = T_\varepsilon[\tilde\varphi] \to T[\tilde\varphi] = \tilde T[\varphi]$, because $\tilde\varphi$ is one fixed test function.
>
> **Step 5** (part 3). $\tilde\delta[\varphi] = \delta[\tilde\varphi] = \tilde\varphi(0) = \int d^nx\,\varphi(x)e^{-i0\cdot x} = T_1[\varphi]$.
>
> **What the derivation shows.**
> - The transform of a distribution is defined, like every operation, by moving it onto the test function; continuity in $\varepsilon$ costs nothing (Step 4). This is why an $i\varepsilon$ expression may be transformed first and $\varepsilon \to 0$ taken afterwards ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-10|Theorem §CA.3.10]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-11|Theorem §CA.3.11]]).

^der-ca-3-2

*Uses:* [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-1|Theorem §CA.3.1]], [[§CA.2 Generalized Functions#^def-ca-2-4|Def. §CA.2.4]], [[§CA.2 Generalized Functions#^def-ca-2-2|Def. §CA.2.2]]

> [!theorem] Theorem §CA.3.3: Plane Waves Integrate to a Delta Function
> As tempered distributions in $\mathbf k$ (respectively $p$),
>
> $$
> \int d^nx\,e^{i\mathbf k\cdot\mathbf x} = (2\pi)^n\delta^n(\mathbf k), \qquad \int d^4x\,e^{ip\cdot x} = (2\pi)^4\delta^4(p) .
> $$
>
> Meaning: for every $\varphi \in \mathcal S$, $\int d^nx\bigl[\int d^nk\,\varphi(\mathbf k)e^{i\mathbf k\cdot\mathbf x}\bigr] = (2\pi)^n\varphi(\mathbf 0)$, with the $\mathbf k$-integral done first. The $\mathbf x$-integral by itself converges for no $\mathbf k$; the identity is the limit of the box integrals $\int_{[-L, L]^n}$ as $L \to \infty$, and of $\int d^nx\,e^{i\mathbf k\cdot\mathbf x - \varepsilon\mathbf x^2}$ as $\varepsilon \to 0^+$.
>
> *Source: the user's PHY 513 notes, App. A §A.2 (Rule 1), §A.4 (Derivation "Three examples, in order of generality"), Ch. 4 §4.3 (rule 1) · standard*

^thm-ca-3-3

> [!derivation]- Derivation
> **Step 1** (not a convergent integral). $|e^{i\mathbf k\cdot\mathbf x}| = 1$ is not integrable over $\mathbb R^n$. In one dimension the box integral is $\int_{-L}^{L}e^{ikx}dx = 2\sin(kL)/k$ for $k \ne 0$, which oscillates between $\pm2/|k|$ without a limit as $L \to \infty$, and $2L \to \infty$ for $k = 0$. So the left side is not a function of $\mathbf k$.
>
> **Step 2** (the meaning). For a Schwartz function $\varphi(\mathbf k)$, the pairing is $\int d^nk\,\varphi(\mathbf k)\int d^nx\,e^{i\mathbf k\cdot\mathbf x} \equiv \int d^nx\,\hat\varphi(\mathbf x)$ with $\hat\varphi(\mathbf x) = \int d^nk\,\varphi(\mathbf k)e^{i\mathbf k\cdot\mathbf x}$, the order that converges. By Fourier inversion ([[§B4.4 Fourier Transforms and the Delta Function#^thm-b4-4-1|WO Theorem §B4.4.1]], rewritten in the convention of [[§CA.3 Fourier Transforms and Fourier Tricks#^def-ca-3-1|Def. §CA.3.1]]; or [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-1|Theorem §CA.3.1]]: $\hat\varphi = (2\pi)^n\check\varphi$ and $\int d^nx\,\check\varphi(\mathbf x) = \tilde{\check\varphi}(\mathbf 0) = \varphi(\mathbf 0)$), $\int d^nx\,\hat\varphi(\mathbf x) = (2\pi)^n\varphi(\mathbf 0)$, which is $(2\pi)^n\delta^n[\varphi]$. A Gaussian convergence factor makes the same statement concrete ([[§B4.4 Fourier Transforms and the Delta Function#^thm-b4-4-3|WO Theorem §B4.4.3]], 4).
>
> **Step 3** (the Gaussian regulator). $\int d^nx\,e^{-\varepsilon\mathbf x^2 + i\mathbf k\cdot\mathbf x} = (\pi/\varepsilon)^{n/2}e^{-\mathbf k^2/4\varepsilon} = (2\pi)^nh_\varepsilon(\mathbf k)$, with $h_\varepsilon$ the heat kernel of Theorem §CA.3.1, Step 3 ([[§CA.5 Gaussian Integrals, Stationary Phase and Bessel Functions#^thm-ca-5-1|Theorem §CA.5.1]], 1, multiplied by $(2\pi)^n$, with $\mathbf x$ and $\mathbf k$ exchanged). $h_\varepsilon \to \delta^n$ ([[§CA.2 Generalized Functions#^thm-ca-2-4|Theorem §CA.2.4]], 3); and $e^{-\varepsilon\mathbf x^2} \to 1$ in $\mathcal S'$ by dominated convergence, so by [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-2|Theorem §CA.3.2]], 2 the regulated transforms converge to the transform of $1$. Both limits are $(2\pi)^n\delta^n$.
>
> **Step 4** (four dimensions). $e^{ip\cdot x} = e^{ip^0t}e^{-i\mathbf p\cdot\mathbf x}$ factorizes into four one-dimensional exponentials; the minus sign on the spatial part is the change of variables $\mathbf p \to -\mathbf p$, under which $\delta^3$ is even ([[§CA.2 Generalized Functions#^thm-ca-2-5|Theorem §CA.2.5]], 1, $|\det| = 1$). So $\int d^4x\,e^{ip\cdot x} = (2\pi)^4\delta(p^0)\delta^3(\mathbf p)$.
>
> **What the derivation shows.**
> - The plane-wave delta function is Fourier inversion, and "do the $\mathbf x$-integral first" is shorthand for "pair with a test function in $\mathbf k$ and integrate $\mathbf x$ last".
> - Different regulators (Gaussian, box) give the same distribution; they differ only in what they assign to the meaningless $\delta^n(\mathbf 0)$: the box gives the volume ([[§CA.2 Generalized Functions#^thm-ca-2-9|Theorem §CA.2.9]]).

^der-ca-3-3

*Uses:* [[§B4.4 Fourier Transforms and the Delta Function#^thm-b4-4-1|WO Theorem §B4.4.1]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-1|Theorem §CA.3.1]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-2|Theorem §CA.3.2]], [[§CA.5 Gaussian Integrals, Stationary Phase and Bessel Functions#^thm-ca-5-1|Theorem §CA.5.1]], [[§CA.2 Generalized Functions#^thm-ca-2-4|Theorem §CA.2.4]], [[§CA.2 Generalized Functions#^thm-ca-2-5|Theorem §CA.2.5]]

> [!derivation]- Derivation (second route: the box)
> **Step 1** (split off a Gaussian). In one dimension, for $\varphi \in \mathcal S$ write $\varphi(k) = \varphi(0)e^{-k^2} + k\,\psi(k)$; $\psi(k) = [\varphi(k) - \varphi(0)e^{-k^2}]/k$ is smooth (the bracket vanishes at $k = 0$) and decays with its derivative.
>
> **Step 2** (the remainder vanishes: Riemann–Lebesgue). $\int dk\,k\psi(k)\frac{2\sin kL}{k} = 2\int dk\,\psi(k)\sin kL = \Bigl[-\frac{2\psi\cos kL}{L}\Bigr]_{-\infty}^{\infty} + \frac2L\int dk\,\psi'(k)\cos kL$, bounded by $\frac2L\int|\psi'| \to 0$.
>
> **Step 3** (the Gaussian term). $J(L) = \int dk\,e^{-k^2}\frac{2\sin kL}{k}$ has $J(0) = 0$ and, differentiating under the integral (bound $2e^{-k^2}$; [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|Theorem §CA.1.1]], 2), $J'(L) = \int dk\,e^{-k^2}2\cos kL = 2\sqrt\pi\,e^{-L^2/4}$ (the Gaussian integral with $b = iL$). So $J(L) = 2\sqrt\pi\int_0^Le^{-s^2/4}ds \to 2\sqrt\pi\cdot\sqrt\pi = 2\pi$.
>
> **Step 4** (assemble). $\int dk\,\varphi(k)\int_{-L}^{L}dx\,e^{ikx} \to 2\pi\varphi(0)$. In $n$ dimensions the box is a product of one-dimensional boxes; for $\varphi = \varphi_1(k_1)\cdots\varphi_n(k_n)$ the statement factorizes, and finite sums of such products approximate every Schwartz function (sketch).
>
> **What the derivation shows.**
> - The box regulator converges to the same distribution; at $\mathbf k = \mathbf 0$ it equals $(2L)^n$, the volume of the box, which is the $\delta^n(\mathbf 0) \to V$ of [[§CA.2 Generalized Functions#^thm-ca-2-9|Theorem §CA.2.9]].
> - Step 2 is the Riemann–Lebesgue lemma: rapidly oscillating phases integrate to zero against smooth functions.
>
> *Source: standard; stated here*

*Uses:* [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|Theorem §CA.1.1]], [[§CA.5 Gaussian Integrals, Stationary Phase and Bessel Functions#^thm-ca-5-1|Theorem §CA.5.1]]

> [!theorem] Theorem §CA.3.4: Rules of the Fourier Transform
> 1. *Plane-wave delta functions:* $\int d^3x\,e^{i\mathbf k\cdot\mathbf x} = (2\pi)^3\delta^3(\mathbf k)$ and $\int d^4x\,e^{ip\cdot x} = (2\pi)^4\delta^4(p)$; the pairs of Def. §CA.3.1 are inverse to each other.
> 2. *Derivatives:* $\partial_\mu \leftrightarrow -ip_\mu$, so $\partial^2 \leftrightarrow -p^2$ and $\partial^2 + m^2 \leftrightarrow m^2 - p^2$.
> 3. *Convolution:* if $h(x) = \int d^4y\,D(x - y)\,j(y)$, then $\tilde h(p) = \tilde D(p)\,\tilde j(p)$.
> 4. *Reality and invariance:* $f$ real $\Rightarrow$ $\tilde f(-p) = \overline{\tilde f(p)}$; $f$ a Lorentz scalar $\Rightarrow$ $\tilde f$ a Lorentz scalar.
>
> All hold in the sense of generalized functions ([[§CA.2 Generalized Functions#^def-ca-2-4|Def. §CA.2.4]]); the precise conditions are Theorem §CA.3.5.
>
> *Source: the user's PHY 513 notes, Ch. 6 §6.3 (Derivation "The rules"), Ch. 4 §4.3 (rules 1 and 4), App. A §A.2*

^thm-ca-3-4

> [!derivation]- Derivation
> **Step 1** (rule 1). In one dimension $\int ds\,e^{iks} = 2\pi\delta(k)$ ([[§B4.4 Fourier Transforms and the Delta Function#^thm-b4-4-3|WO Theorem §B4.4.3]], 4, with $\omega \to k$, $t \to s$; the sign in the exponent is irrelevant since $\delta$ is even). The integral over $d^3x$ or $d^4x$ factorizes into three or four such integrals: $\int d^4x\,e^{ip\cdot x} = \int dt\,e^{ip^0t}\prod_{i=1}^3\int dx^i\,e^{-ip^ix^i} = (2\pi)^4\delta(p^0)\delta^3(\mathbf p)$. As a statement against test functions this is [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]].
>
> **Step 2** (inversion). Insert the synthesis into the analysis formula: $\int d^4x\,e^{ip\cdot x}\int\frac{d^4q}{(2\pi)^4}\tilde f(q)e^{-iq\cdot x} = \int\frac{d^4q}{(2\pi)^4}\tilde f(q)\,(2\pi)^4\delta^4(p - q) = \tilde f(p)$, the $x$ integral done first by Step 1.
>
> **Step 3** (rule 2). $\partial_0e^{-ip\cdot x} = -ip^0e^{-ip\cdot x} = -ip_0e^{-ip\cdot x}$; $\partial_ie^{+i\mathbf p\cdot\mathbf x} = +ip^ie^{i\mathbf p\cdot\mathbf x} = -ip_ie^{i\mathbf p\cdot\mathbf x}$ (lowering a spatial index changes its sign). So $\partial_\mu \to -ip_\mu$ for all four components, and $\partial^2 = \partial_\mu\partial^\mu \to (-ip_\mu)(-ip^\mu) = -p^2$.
>
> ⚑ By-product: the opposite signs in the phase are what let one formula cover all four components; with $\partial^2 + m^2 \to m^2 - p^2$, the Klein–Gordon operator is multiplication by a function that vanishes exactly on the mass shell → [[§CA.3 Fourier Transforms and Fourier Tricks#^rem-ca-3-1|Remark: A linear equation becomes algebra]].
>
> **Step 4** (rule 3). $\tilde h(p) = \int d^4x\,e^{ip\cdot x}\int d^4y\,D(x - y)j(y)$. Substitute $x = u + y$ at fixed $y$ (Jacobian 1), so $e^{ip\cdot x} = e^{ip\cdot u}e^{ip\cdot y}$: $\tilde h(p) = \int d^4y\,e^{ip\cdot y}j(y)\int d^4u\,e^{ip\cdot u}D(u) = \tilde j(p)\tilde D(p)$.
>
> **Step 5** (reality). Conjugate $\tilde f(p) = \int d^4x\,f(x)e^{ip\cdot x}$ with $f$ real: $\overline{\tilde f(p)} = \int d^4x\,f(x)e^{-ip\cdot x} = \tilde f(-p)$.
>
> **Step 6** (invariance). A scalar satisfies $f(\Lambda^{-1}x) = f(x)$. In $\tilde f(\Lambda p) = \int d^4x\,f(x)e^{i(\Lambda p)\cdot x}$ substitute $x = \Lambda y$: $|\det\Lambda| = 1$, $(\Lambda p)\cdot(\Lambda y) = p\cdot y$ ([[§B1.2 Lorentz Transformations and the Lorentz Group#^thm-b1-2-2|REL Theorem §B1.2.2]]), $f(\Lambda y) = f(y)$; so $\tilde f(\Lambda p) = \tilde f(p)$.
>
> **What the derivation shows.**
> - Every rule is a substitution or a factorization; the only analysis is in rule 1, which is a statement about generalized functions.
> - Used in: the Green's function as division by $m^2 - p^2$ ([[§C2b.1 Heisenberg Fields#^thm-c2b-1-3|Theorem §C2b.1.3]]), the canonical relations recovered from mode integrals ([[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-10|Theorem §C2b.4.10]]), the source transform $\tilde j$ ([[§C2b.8 Particle Production by a Classical Source#^thm-c2b-8-1|Theorem §C2b.8.1]]).

^der-ca-3-4

*Uses:* [[§B4.4 Fourier Transforms and the Delta Function#^thm-b4-4-3|WO Theorem §B4.4.3]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]], [[§B1.2 Lorentz Transformations and the Lorentz Group#^thm-b1-2-2|REL Theorem §B1.2.2]]

> [!remark] Remark: A linear equation becomes algebra
> By rule 2 a linear differential equation with constant coefficients becomes multiplication: the Klein–Gordon operator is multiplication by $m^2 - p^2$, which vanishes exactly on the mass shell. By rule 3 the Green's-function solution of a sourced equation is division by that factor. Both facts, and the trouble that the factor has zeros, are the subject of [[§C2b.5 Green's Functions and Contours|§C2b.5]]; a free field is a transform supported on the shell ([[§C2b.1 Heisenberg Fields#^thm-c2b-1-3|Theorem §C2b.1.3]]).
>
> *Source: the user's PHY 513 notes, Ch. 6 §6.3*

^rem-ca-3-1

> [!theorem] Theorem §CA.3.5: Translation, Phase, and the Rules in 𝒮′
> In the spacetime convention of [[§CA.3 Fourier Transforms and Fourier Tricks#^def-ca-3-1|Def. §CA.3.1]]:
> 1. *(Translation ↔ phase)* $f(x - a)$ has the transform $e^{ip\cdot a}\tilde f(p)$.
> 2. *(Phase ↔ translation)* $e^{-iq\cdot x}f(x)$ has the transform $\tilde f(p - q)$.
> 3. *(The rules in $\mathcal S'$)* The derivative rule $\widetilde{\partial_\mu T} = -ip_\mu\tilde T$ holds for every $T \in \mathcal S'$; the convolution rule $\widetilde{D \ast  j} = \tilde D\,\tilde j$ holds for $D \in \mathcal S'$ and $j \in \mathcal S$, where $\tilde D\,\tilde j$ is the product of a distribution with a Schwartz function. Parts 1–2 hold for $T \in \mathcal S'$ with $T(x - a)$ as in [[§CA.2 Generalized Functions#^def-ca-2-5|Def. §CA.2.5]].
>
> *Source: the user's PHY 513 notes, Ch. 6 §6.3 (Derivation "The rules", 2 and 4) · standard (Hörmander I, §7.1)*

^thm-ca-3-5

> [!derivation]- Derivation
> **Step 1** (part 1). $\int d^4x\,f(x - a)e^{ip\cdot x}$; substitute $x = u + a$ (Jacobian $1$, domain $\mathbb R^4$ unchanged), so $e^{ip\cdot x} = e^{ip\cdot u}e^{ip\cdot a}$: the integral is $e^{ip\cdot a}\int d^4u\,f(u)e^{ip\cdot u} = e^{ip\cdot a}\tilde f(p)$.
>
> **Step 2** (part 2). $\int d^4x\,e^{-iq\cdot x}f(x)e^{ip\cdot x} = \int d^4x\,f(x)e^{i(p - q)\cdot x} = \tilde f(p - q)$.
>
> **Step 3** (derivative rule in $\mathcal S'$). Here the transform of a test function $\varphi(p)$ is $\tilde\varphi(x) = \int d^4p\,\varphi(p)e^{ip\cdot x}$, so $\partial_\mu\tilde\varphi(x) = \int d^4p\,\varphi(p)\,ip_\mu e^{ip\cdot x} = \mathcal F(ip_\mu\varphi)(x)$. Then, by [[§CA.2 Generalized Functions#^def-ca-2-4|Def. §CA.2.4]],
>
> $$
> \widetilde{\partial_\mu T}[\varphi] = (\partial_\mu T)[\tilde\varphi] = -T[\partial_\mu\tilde\varphi] = -T\bigl[\mathcal F(ip_\mu\varphi)\,\bigr] = -\tilde T[ip_\mu\varphi] = (-ip_\mu\tilde T)[\varphi] .
> $$
>
> **Step 4** (convolution rule in $\mathcal S'$). With $(D \ast  j)(x) = D[j(x - \cdot)]$, a smooth polynomially bounded function,
>
> $$
> \widetilde{D * j}[\varphi] = \int d^4x\,D\bigl[j(x - \cdot)\bigr]\tilde\varphi(x) = D\Bigl[\int d^4x\,j(x - \cdot)\,\tilde\varphi(x)\Bigr] ,
> $$
>
> the exchange of $D$ with the $x$-integral holding because the Riemann sums of the $x$-integral converge in $\mathcal S$ (sketch). The function in brackets is, at the point $y$, $\int d^4x\,j(x - y)\int d^4p\,\varphi(p)e^{ip\cdot x} = \int d^4p\,\varphi(p)e^{ip\cdot y}\int d^4u\,j(u)e^{ip\cdot u} = \mathcal F(\tilde j\varphi)(y)$, with $x = u + y$ and Fubini. So $\widetilde{D * j}[\varphi] = D[\mathcal F(\tilde j\varphi)\,] = \tilde D[\tilde j\varphi] = (\tilde j\tilde D)[\varphi]$.
>
> **What the derivation shows.**
> - These are the precise conditions behind the rules of [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-4|Theorem §CA.3.4]]: the derivative rule always holds, the convolution rule whenever one factor is a test function, as every physical source is.
> - Translation invariance of a two-point function, $D(x - y)$, is part 1 in the form "a function of $x - y$ has a transform carrying $e^{ip\cdot(x - y)}$".

^der-ca-3-5

*Uses:* [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-2|Theorem §CA.3.2]], [[§CA.2 Generalized Functions#^def-ca-2-4|Def. §CA.2.4]], [[§CA.2 Generalized Functions#^def-ca-2-5|Def. §CA.2.5]], [[§25 Invariance Properties and Fubini's Theorem#^thm-25-6|551 Thm. §25.6]]

## Tricks in mode computations

> [!theorem] Theorem §CA.3.6: Exchanging the Space and Momentum Integrals
> Let $A, B \in \mathcal S(\mathbb R^3)$ (wave packets), $a(\mathbf x) = \int\frac{d^3p}{(2\pi)^3}A(\mathbf p)e^{i\mathbf p\cdot\mathbf x}$ and $b(\mathbf x) = \int\frac{d^3q}{(2\pi)^3}B(\mathbf q)e^{i\mathbf q\cdot\mathbf x}$. Then, every integral converging absolutely,
>
> $$
> \int d^3x\,a(\mathbf x)\,b(\mathbf x) = \int\frac{d^3p}{(2\pi)^3}\,A(\mathbf p)\,B(-\mathbf p) .
> $$
>
> The physicists' route (exchange the order, do $\int d^3x$ first to get $(2\pi)^3\delta^3(\mathbf p + \mathbf q)$, then set $\mathbf q = -\mathbf p$) computes the same number. Phases $e^{\mp iE_{\mathbf p}t}$ ride along inside $A$, $B$ (the split-exponential rule). For coefficients that are not wave packets, such as $a_{\mathbf p}$, the identity holds after smearing them with test functions.
>
> *Source: the user's PHY 513 notes, Ch. 4 §4.3 (rules 1–3 of "The six rules"; Caution "Where the errors live") · justified here (standard: Fubini)*

^thm-ca-3-6

> [!derivation]- Derivation
> **Step 1** (wave packets in space). $a$ and $b$ are inverse transforms of Schwartz functions, hence Schwartz ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-1|Theorem §CA.3.1]], 1); $ab \in \mathcal S \subset L^1$, so the left side converges absolutely.
>
> **Step 2** (insert $b$, exchange). $\int d^3x\,a(\mathbf x)\,b(\mathbf x) = \int d^3x\,a(\mathbf x)\int\frac{d^3q}{(2\pi)^3}B(\mathbf q)e^{i\mathbf q\cdot\mathbf x}$. Since $\int\!\!\int d^3x\,d^3q\,|a(\mathbf x)||B(\mathbf q)| = \|a\|_{L^1}\|B\|_{L^1} < \infty$, Fubini ([[§25 Invariance Properties and Fubini's Theorem#^thm-25-6|551 Thm. §25.6]]) gives
>
> $$
> = \int\frac{d^3q}{(2\pi)^3}B(\mathbf q)\int d^3x\,a(\mathbf x)\,e^{i\mathbf q\cdot\mathbf x} .
> $$
>
> **Step 3** (the $\mathbf x$-integral is a transform). $\int d^3x\,a(\mathbf x)e^{i\mathbf q\cdot\mathbf x} = \int d^3x\,a(\mathbf x)e^{-i(-\mathbf q)\cdot\mathbf x} = \tilde a(-\mathbf q) = A(-\mathbf q)$, by inversion ($a = \check A$, so $\tilde a = A$).
>
> **Step 4** (relabel). $\int\frac{d^3q}{(2\pi)^3}B(\mathbf q)A(-\mathbf q)$; substitute $\mathbf q = -\mathbf p$ (Jacobian $|\det(-\mathbb 1)| = 1$, $\mathbb R^3 \to \mathbb R^3$; [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|Theorem §CA.3.7]], 1): $\int\frac{d^3p}{(2\pi)^3}A(\mathbf p)B(-\mathbf p)$.
>
> **Step 5** (the physicists' route). Formally $\int d^3x\int\frac{d^3p}{(2\pi)^3}\frac{d^3q}{(2\pi)^3}A(\mathbf p)B(\mathbf q)e^{i(\mathbf p + \mathbf q)\cdot\mathbf x}$; the $\mathbf x$-integral is $(2\pi)^3\delta^3(\mathbf p + \mathbf q)$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]], a distribution in $\mathbf p + \mathbf q$ paired with the test function $A(\mathbf p)B(\mathbf q)$ at fixed $\mathbf p$), and the $\mathbf q$-integral sets $\mathbf q = -\mathbf p$: $\int\frac{d^3p}{(2\pi)^3}A(\mathbf p)B(-\mathbf p)$, the same result. Steps 2–4 are the proof that this bookkeeping is right.
>
> **Step 6** (with time; the split-exponential rule). At fixed $t$, put $A(\mathbf p) = \alpha(\mathbf p)e^{\mp iE_{\mathbf p}t}$ and $B(\mathbf q) = \beta(\mathbf q)e^{\mp iE_{\mathbf q}t}$; these are still Schwartz in $\mathbf p$ (for $m > 0$, $E_{\mathbf p}$ is smooth and its derivatives grow at most polynomially). After Step 4, $B(-\mathbf p)$ carries $E_{-\mathbf p} = E_{\mathbf p}$, since $E$ depends on $|\mathbf p|$ only, so the phases combine to $e^{\mp2iE_{\mathbf p}t}$, or to $1$ when one phase is conjugated: "the delta equates the frequencies".
>
> ⚑ By-product: when $A$ or $B$ is an unsmeared operator coefficient such as $a_{\mathbf p}$, the identity holds as an identity of operator-valued distributions ([[§CA.2 Generalized Functions#^def-ca-2-8|Def. §CA.2.8]]); a product of two such coefficients at the same momentum, left unsmeared, is where a $\delta^3(\mathbf 0)$ appears → [[§CA.2 Generalized Functions#^thm-ca-2-8|Theorem §CA.2.8]], 3.
>
> **What the derivation shows.**
> - The exchange of integrals is Fubini for wave packets; the delta function is bookkeeping for one Fourier inversion.
> - Time phases ride along, and $E_{-\mathbf p} = E_{\mathbf p}$ is what makes the surviving phase $e^{\mp2iE_{\mathbf p}t}$ or $1$.
> - Assumption used: absolute integrability, i.e. wave packets; for plane-wave coefficients the identity is read after smearing.

^der-ca-3-6

*Uses:* [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-1|Theorem §CA.3.1]], [[§25 Invariance Properties and Fubini's Theorem#^thm-25-6|551 Thm. §25.6]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|Theorem §CA.3.7]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]]

> [!theorem] Theorem §CA.3.7: Changes of Integration Variable: Relabelling, Shifting, Rescaling, Rotating
> For an integral over all of $\mathbb R^n$ that converges absolutely, or for the pairing of a tempered distribution with a test function ([[§CA.2 Generalized Functions#^def-ca-2-5|Def. §CA.2.5]]):
> 1. *(Relabel)* $\int d^np\,F(\mathbf p) = \int d^np\,F(-\mathbf p)$;
> 2. *(Shift)* $\int d^np\,F(\mathbf p) = \int d^np\,F(\mathbf p + \mathbf a)$;
> 3. *(Rescale)* $\int d^np\,F(\mathbf p) = |\lambda|^n\int d^np\,F(\lambda\mathbf p)$ for $\lambda \ne 0$;
> 4. *(Rotate, boost)* $\int d^3p\,F(\mathbf p) = \int d^3p\,F(R\mathbf p)$ for a rotation $R$, and $\int d^4p\,F(p) = \int d^4p\,F(\Lambda p)$ for a Lorentz transformation $\Lambda$.
>
> The domain is unchanged; what changes is the integrand's argument: phases $\mathbf p\cdot\mathbf x \to -\mathbf p\cdot\mathbf x$, operator labels $\mathbf p \to -\mathbf p$, while $E_{-\mathbf p} = E_{R\mathbf p} = E_{\mathbf p}$.
>
> *Source: the user's PHY 513 notes, Ch. 4 §4.3 (rule 3: relabelling), App. A §A.3 ("Why the axis may be chosen") · [[§25 Change of Variables on General Domains#^thm-25-6|452 Thm. §25.6]]*

^thm-ca-3-7

> [!derivation]- Derivation
> **Step 1** (the formula). For an invertible affine map $\mathbf p = L\mathbf q + \mathbf a$, the change of variables theorem ([[§25 Change of Variables on General Domains#^thm-25-6|452 Thm. §25.6]], on balls of growing radius, then dominated convergence) gives $\int d^np\,F(\mathbf p) = |\det L|\int d^nq\,F(L\mathbf q + \mathbf a)$, and $L\mathbb R^n + \mathbf a = \mathbb R^n$: the domain is unchanged.
>
> **Step 2** (the Jacobians). $L = -\mathbb 1$: $|\det L| = |(-1)^n| = 1$. Shift: $L = \mathbb 1$. Rescale: $L = \lambda\mathbb 1$, $|\det L| = |\lambda|^n$. Rotation: $\det R = 1$. Lorentz: $\Lambda^{\mathsf T}g\Lambda = g$ gives $(\det\Lambda)^2 = 1$.
>
> **Step 3** (orientation, in one dimension). Substituting $p = -q$ turns $\int_{-\infty}^{\infty}dp$ into $\int_{\infty}^{-\infty}(-dq)$, and the sign of $dp = -dq$ and the reversed limits cancel: $\int_{-\infty}^{\infty}dq$. This cancellation is the absolute value in $|\det L|$.
>
> **Step 4** (what changes). $E_{\mathbf p} = \sqrt{\mathbf p^2 + m^2}$ depends on $|\mathbf p|$, and $|-\mathbf p| = |R\mathbf p| = |\mathbf p|$. Everything else that depends on $\mathbf p$, an exponent or an operator label, is evaluated at the new argument, and must be carried along.
>
> **Step 5** (distributions). For a pairing $T[\varphi]$, the same substitution is [[§CA.2 Generalized Functions#^def-ca-2-5|Def. §CA.2.5]] with $A = L$.
>
> **What the derivation shows.**
> - Any measure- and domain-preserving map of a dummy variable is allowed; "choose the polar axis along $\mathbf r$" ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-9|Theorem §CA.3.9]]) and "choose the frame" ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-12|Theorem §CA.3.12]]) are instances.
> - The one thing to track is the label: a dropped sign turns $[a_{\mathbf p}, a^\dagger_{-\mathbf p}]$ into $[a_{\mathbf p}, a^\dagger_{\mathbf p}]$ and creates a spurious $\delta^3(\mathbf 0)$ ([[§C2a.2 Mode Expansion and the Mode Algebra#^rem-c2a-2-2|Remark: Two bookkeeping rules for mode integrals]]).
> - A box of side $L$ is not shift invariant unless the functions are periodic, which is why [[§CA.2 Generalized Functions#^thm-ca-2-9|Theorem §CA.2.9]] uses periodic boundary conditions.

^der-ca-3-7

*Uses:* [[§25 Change of Variables on General Domains#^thm-25-6|452 Thm. §25.6]], [[§CA.2 Generalized Functions#^def-ca-2-5|Def. §CA.2.5]]

> [!theorem] Theorem §CA.3.8: Integration by Parts; the Gradient of a Delta Function
> For functions on a region $V$ with outward normal $\hat n$,
>
> $$
> \int_Vd^3x\,(\partial_if)\,g = \oint_{\partial V}dS\,n_i\,f\,g - \int_Vd^3x\,f\,\partial_ig .
> $$
>
> For fields that fall off at infinity, $\int d^3x\,\nabla f\cdot\nabla g = -\int d^3x\,f\,\nabla^2g$, and $\int d^3y\,f(\mathbf y)\,\nabla_{\mathbf y}\delta^3(\mathbf x - \mathbf y) = -\nabla f(\mathbf x)$.
>
> *Source: the user's PHY 513 notes, App. A §A.2 (rule 5), Ch. 4 §4.3*

^thm-ca-3-8

> [!derivation]- Derivation
> **Step 1** (product rule). $\partial_i(fg) = (\partial_if)g + f\,\partial_ig$.
>
> **Step 2** (divergence theorem). Integrate over $V$ and apply [[§28 The Divergence Theorem in Higher Dimensions and Green's Identities#^thm-28-1|452 Thm. §28.1]] to the vector field $fg\,\hat e_i$: $\int_V\partial_i(fg) = \oint_{\partial V}n_ifg$. Rearranging gives the first formula.
>
> **Step 3** (gradients). Take $g \to \partial_ig$ and sum over $i$: $\int_V\nabla f\cdot\nabla g = \oint_{\partial V}f\,\hat n\cdot\nabla g - \int_Vf\nabla^2g$. With $V$ a ball of radius $L \to \infty$, the surface term is dropped when $f\,\partial_rg$ falls off faster than $1/L^2$.
>
> ⚑ By-product: "fields fall off at infinity" is an assumption about the states in which the operators are evaluated (wave packets, not plane waves); it is made every time a surface term is dropped → [[§C2b.1 Heisenberg Fields#^thm-c2b-1-2|§C2b.1, Theorem §C2b.1.2, Step 5]].
>
> **Step 4** (delta function). With $f = \delta^3(\mathbf x - \mathbf y)$ as a function of $\mathbf y$, the surface term vanishes because the delta function is zero on $\partial V$ (its support, the point $\mathbf x$, lies inside); so $\int d^3y\,\delta^3(\mathbf x - \mathbf y)\,\partial_ig(\mathbf y) = -\int d^3y\,\partial_{y^i}\delta^3(\mathbf x - \mathbf y)\,g(\mathbf y)$, i.e. $\int d^3y\,g\,\nabla_{\mathbf y}\delta^3 = -\nabla g(\mathbf x)$. This is also the *definition* of the derivative of $\delta$ ([[§CA.2 Generalized Functions#^def-ca-2-4|Def. §CA.2.4]]).
>
> **What the derivation shows.**
> - Two uses of one move, differing only in which factor kills the surface term: fall-off at infinity, or a delta function supported inside.
> - The four-dimensional version is the step in every Euler–Lagrange and Noether derivation (Euler–Lagrange: [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^der-c1b-2-4|Derivation §C1b.2.4]], step 4; Noether charges: [[§C1b.5 Noether's Theorem#^thm-c1b-5-3|Theorem §C1b.5.3]], [[§C1b.7 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^der-c1b-7-4|Derivation §C1b.7.4]], step 7).

^der-ca-3-8

*Uses:* [[§28 The Divergence Theorem in Higher Dimensions and Green's Identities#^thm-28-1|452 Thm. §28.1]], [[§CA.2 Generalized Functions#^def-ca-2-4|Def. §CA.2.4]]

> [!theorem] Theorem §CA.3.9: Angular Integrals
> 1. For a radial $f$ and $r = |\mathbf r|$: $\displaystyle\int d^3p\,f(|\mathbf p|)\,e^{i\mathbf p\cdot\mathbf r} = \frac{4\pi}{r}\int_0^\infty dp\,p\,f(p)\sin(pr)$.
> 2. Without an exponential: $\int d^3p\,p^if(|\mathbf p|) = 0$ and $\int d^3p\,p^ip^jf(|\mathbf p|) = \tfrac13\delta^{ij}\int d^3p\,\mathbf p^2f(|\mathbf p|)$.
> 3. A component under the exponential is a derivative: $p^ie^{i\mathbf p\cdot\mathbf r} = -i\partial_{r^i}e^{i\mathbf p\cdot\mathbf r}$.
>
> *Source: the user's PHY 513 notes, App. A §A.3 (rule 6, Derivation "Angular integrals, from the ground up")*

^thm-ca-3-9

> [!derivation]- Derivation
> **Step 1** (rotate the integration variable). Let $R$ be a rotation with $R\hat z = \hat r$ and substitute $\mathbf p = R\mathbf q$: $|\det R| = 1$, the domain $\mathbb R^3$ is unchanged, $|\mathbf p| = |\mathbf q|$, and $\mathbf p\cdot\mathbf r = \mathbf q\cdot R^{\mathsf T}\mathbf r = rq_z$. The dummy variable is rotated; nothing is done to $\mathbf r$. This is "choose the polar axis along $\mathbf r$".
>
> **Step 2** (spherical coordinates). $\mathbf q = q(\sin\theta\cos\varphi, \sin\theta\sin\varphi, \cos\theta)$ has Jacobian $q^2\sin\theta$, so $d^3q = q^2\sin\theta\,dq\,d\theta\,d\varphi$ ([[§21 The Definition of the Integral#^rem-21-5|452 Rem. §15.5]]), and $q_z = q\cos\theta$. The integrand does not depend on $\varphi$: that integral gives $2\pi$.
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
> **Step 6** (part 3). $\partial_{r^i}e^{i\mathbf p\cdot\mathbf r} = ip^ie^{i\mathbf p\cdot\mathbf r}$; multiply by $-i$. Under the integral the derivative is moved outside by [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|Theorem §CA.1.1]], 2 (regulated) or by definition (generalized functions).
>
> **What the derivation shows.**
> - A three-dimensional transform of a radial function is a one-dimensional sine transform; the result depends on $\mathbf r$ only through $r$, as rotation invariance requires.
> - The four-dimensional version of the idea is a choice of frame: $\mathbf x = \mathbf y$ for timelike separation, $x^0 = y^0$ for spacelike ([[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-3|Theorem §C2b.3.3]], second route; [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-4|Theorem §C2b.3.4]], Step 5).

^der-ca-3-9

*Uses:* [[§21 The Definition of the Integral#^rem-21-5|452 Rem. §15.5]], [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|Theorem §CA.1.1]]

## Damping factors and iε

> [!theorem] Theorem §CA.3.10: Damping Factors: the Transform of the Step Function
> For real $\omega$ and $\varepsilon > 0$, $\int_0^\infty dt\,e^{i\omega t - \varepsilon t} = \dfrac{i}{\omega + i\varepsilon}$. As $\varepsilon \to 0^+$, in $\mathcal S'(\mathbb R)$,
>
> $$
> \tilde\theta(\omega) = \int dt\,\theta(t)\,e^{i\omega t} = \frac{i}{\omega + i0} = i\,\mathcal P\frac1\omega + \pi\,\delta(\omega) .
> $$
>
> Conversely $\int\frac{d\omega}{2\pi}e^{-i\omega t}\frac{i}{\omega + i\varepsilon} = \theta(t)\,e^{-\varepsilon t}$: a damping factor on $t > 0$ puts the pole below the real axis.
>
> *Source: standard; stated here · the user's PHY 513 notes, App. A §A.5 (worked example (iii)), Ch. 6 §6.9 (poles moved off the axis)*

^thm-ca-3-10

> [!derivation]- Derivation
> **Step 1** (finite ε). $\int_0^\infty e^{(i\omega - \varepsilon)t}dt = \Bigl[\frac{e^{(i\omega - \varepsilon)t}}{i\omega - \varepsilon}\Bigr]_0^\infty = 0 - \frac{1}{i\omega - \varepsilon} = \frac{1}{\varepsilon - i\omega}$; the upper limit vanishes because $|e^{(i\omega - \varepsilon)t}| = e^{-\varepsilon t}$. Multiplying numerator and denominator by $i$: $\frac{i}{i\varepsilon + \omega} = \frac{i}{\omega + i\varepsilon}$.
>
> **Step 2** (regulated step function). $\theta_\varepsilon(t) = \theta(t)e^{-\varepsilon t} \to \theta$ in $\mathcal S'$ (dominated convergence, $|\theta_\varepsilon\varphi| \le |\varphi|$). Its transform is the function of Step 1, so by [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-2|Theorem §CA.3.2]], 2, $\tilde\theta = \lim_{\varepsilon\to0^+}\frac{i}{\omega + i\varepsilon}$.
>
> **Step 3** (Sokhotski–Plemelj). $\frac{1}{\omega + i\varepsilon} \to \mathcal P\frac1\omega - i\pi\delta(\omega)$ ([[§CA.2 Generalized Functions#^thm-ca-2-11|Theorem §CA.2.11]], upper sign), so $\frac{i}{\omega + i\varepsilon} \to i\mathcal P\frac1\omega + \pi\delta(\omega)$.
>
> **Step 4** (check). $\theta = \frac12 + \frac12\operatorname{sgn}$. The transform of $\frac12$ is $\frac12\cdot2\pi\delta(\omega) = \pi\delta(\omega)$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]], $n = 1$), the even part. The odd part, $\frac12\widetilde{\operatorname{sgn}} = i\mathcal P\frac1\omega$, is the transform of $\frac12\operatorname{sgn}$: Steps 1–3 applied to $\theta(-t)$ give $-\frac{i}{\omega - i0}$, and $\widetilde{\operatorname{sgn}} = \frac{i}{\omega + i0} + \frac{i}{\omega - i0} = 2i\mathcal P\frac1\omega$.
>
> **Step 5** (converse). $\frac{1}{2\pi}\int d\omega\,e^{-i\omega t}\frac{i}{\omega + i\varepsilon}$ has its pole at $\omega = -i\varepsilon$. For $t > 0$, $|e^{-i\omega t}| = e^{t\operatorname{Im}\omega}$ decays in the lower half-plane: close downward, clockwise ([[§CA.4 Contour Integration#^thm-ca-4-6|Theorem §CA.4.6]], Jordan, since $\frac{i}{2\pi(\omega + i\varepsilon)} \to 0$), enclosing the pole with residue $\frac{i}{2\pi}e^{-i(-i\varepsilon)t} = \frac{i}{2\pi}e^{-\varepsilon t}$; the integral is $-2\pi i\cdot\frac{i}{2\pi}e^{-\varepsilon t} = e^{-\varepsilon t}$. For $t < 0$ close upward: no pole, $0$. Together $\theta(t)e^{-\varepsilon t}$ ([[§CA.4 Contour Integration#^ex-ca-4-2|Example §CA.4.2]] is the same computation).
>
> **What the derivation shows.**
> - "$i\varepsilon$ from damping": a factor $e^{-\varepsilon t}$ that makes $\int_0^\infty$ converge moves the pole to $\omega = -i\varepsilon$, below the axis; the side of the pole encodes the direction of time.
> - The real part $\pi\delta(\omega)$ is the mean value $\frac12$ of the step; the principal value is its jump.
> - Used next: the iε of every propagator denominator ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-11|Theorem §CA.3.11]]).

^der-ca-3-10

*Uses:* [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-2|Theorem §CA.3.2]], [[§CA.2 Generalized Functions#^thm-ca-2-11|Theorem §CA.2.11]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]], [[§CA.4 Contour Integration#^thm-ca-4-6|Theorem §CA.4.6]]

> [!theorem] Theorem §CA.3.11: The iε Limits of the Propagator Denominators
> For $m > 0$, as $\varepsilon \to 0^+$, in $\mathcal S'(\mathbb R^4)$:
> 1. $\dfrac{1}{p^2 - m^2 + i\varepsilon} \to \mathcal P\dfrac{1}{p^2 - m^2} - i\pi\,\delta(p^2 - m^2)$, so $\dfrac{i}{p^2 - m^2 + i\varepsilon} \to i\,\mathcal P\dfrac{1}{p^2 - m^2} + \pi\,\delta(p^2 - m^2)$; complex conjugate for $-i\varepsilon$.
> 2. $\dfrac{1}{(p^0 + i\varepsilon)^2 - \mathbf p^2 - m^2} \to \mathcal P\dfrac{1}{p^2 - m^2} - i\pi\operatorname{sgn}(p^0)\,\delta(p^2 - m^2)$; complex conjugate for $p^0 - i\varepsilon$.
> 3. Replacing $\varepsilon$ by $\varepsilon\,c(\mathbf p)$ with $c$ smooth and positive (for example $2E_{\mathbf p}\varepsilon \to \varepsilon$) does not change the limits.
>
> Here $\mathcal P\frac{1}{p^2 - m^2} \equiv \frac{1}{2E_{\mathbf p}}\bigl[\mathcal P\frac{1}{p^0 - E_{\mathbf p}} - \mathcal P\frac{1}{p^0 + E_{\mathbf p}}\bigr]$, applied in $p^0$ at fixed $\mathbf p$.
>
> *Source: the user's PHY 513 notes, Ch. 6 §6.9 (Derivation "The distributional version: Sokhotski–Plemelj"; "only the sign of the infinitesimal matters") · justified here*

^thm-ca-3-11

> [!derivation]- Derivation
> **Step 1** (factor at fixed $\mathbf p$). $p^2 - m^2 + i\varepsilon = (p^0)^2 - (E_{\mathbf p}^2 - i\varepsilon) = (p^0 - E_\varepsilon)(p^0 + E_\varepsilon)$ with $E_\varepsilon = \sqrt{E_{\mathbf p}^2 - i\varepsilon}$ (principal root). Writing $E_\varepsilon = a - ib$: $a^2 - b^2 = E_{\mathbf p}^2$ and $2ab = \varepsilon$, so $b = \varepsilon/2a > 0$ and $a = E_{\mathbf p} + O(\varepsilon^2)$.
>
> **Step 2** (partial fractions). $\frac{1}{(p^0)^2 - E_\varepsilon^2} = \frac{1}{2E_\varepsilon}\Bigl[\frac{1}{p^0 - E_\varepsilon} - \frac{1}{p^0 + E_\varepsilon}\Bigr]$; check: the numerator is $(p^0 + E_\varepsilon) - (p^0 - E_\varepsilon) = 2E_\varepsilon$.
>
> **Step 3** (Sokhotski–Plemelj in $p^0$). $p^0 - E_\varepsilon = p^0 - a + ib$, so $\frac{1}{p^0 - E_\varepsilon} \to \mathcal P\frac{1}{p^0 - E_{\mathbf p}} - i\pi\delta(p^0 - E_{\mathbf p})$; $p^0 + E_\varepsilon = p^0 + a - ib$, so $\frac{1}{p^0 + E_\varepsilon} \to \mathcal P\frac{1}{p^0 + E_{\mathbf p}} + i\pi\delta(p^0 + E_{\mathbf p})$ ([[§CA.2 Generalized Functions#^thm-ca-2-11|Theorem §CA.2.11]]). The shift of the real part, $a - E_{\mathbf p} = O(\varepsilon^2)$, is harmless: $\int dp^0\frac{\varphi(p^0)}{p^0 - a + ib} = \int ds\frac{\varphi(s + a - E_{\mathbf p})}{s - E_{\mathbf p} + ib}$ with $s = p^0 - a + E_{\mathbf p}$, and $\varphi(\cdot + a - E_{\mathbf p}) \to \varphi$ in $\mathcal S$.
>
> **Step 4** (combine). $\frac{1}{2E_\varepsilon} \to \frac{1}{2E_{\mathbf p}}$, and
>
> $$
> \frac{1}{2E_{\mathbf p}}\Bigl[\mathcal P\frac{1}{p^0 - E_{\mathbf p}} - \mathcal P\frac{1}{p^0 + E_{\mathbf p}}\Bigr] - i\pi\,\frac{\delta(p^0 - E_{\mathbf p}) + \delta(p^0 + E_{\mathbf p})}{2E_{\mathbf p}} = \mathcal P\frac{1}{p^2 - m^2} - i\pi\,\delta(p^2 - m^2) ,
> $$
>
> the last by [[§CA.2 Generalized Functions#^thm-ca-2-5|Theorem §CA.2.5]], 2. Multiplying by $i$ gives the second form of part 1.
>
> **Step 5** (from $p^0$ to $\mathbb R^4$; sketch). Steps 1–4 hold at each $\mathbf p$. To integrate over $\mathbf p$ against $\varphi \in \mathcal S(\mathbb R^4)$ one needs a bound uniform in $\varepsilon$: the derivation of Sokhotski–Plemelj bounds the $p^0$-pairing by $C\sup_{p^0}(1 + |p^0|)^2(|\varphi| + |\partial_0\varphi|)$, and since $E_{\mathbf p} \ge m$ the constant is uniform in $\mathbf p$; for Schwartz $\varphi$ this decays faster than any power of $|\mathbf p|$, and dominated convergence in $\mathbf p$ finishes.
>
> **Step 6** (part 2). $(p^0 + i\varepsilon)^2 - E_{\mathbf p}^2 = (p^0 - E_{\mathbf p} + i\varepsilon)(p^0 + E_{\mathbf p} + i\varepsilon)$: both poles, $\pm E_{\mathbf p} - i\varepsilon$, are below the axis, and the partial fractions are exact with $2E_{\mathbf p}$: $\frac{1}{2E_{\mathbf p}}\Bigl[\frac{1}{p^0 - E_{\mathbf p} + i\varepsilon} - \frac{1}{p^0 + E_{\mathbf p} + i\varepsilon}\Bigr]$. Each term has the upper sign of Sokhotski–Plemelj, so the limit is
>
> $$
> \frac{1}{2E_{\mathbf p}}\Bigl[\mathcal P\frac{1}{p^0 - E_{\mathbf p}} - \mathcal P\frac{1}{p^0 + E_{\mathbf p}}\Bigr] - i\pi\,\frac{\delta(p^0 - E_{\mathbf p}) - \delta(p^0 + E_{\mathbf p})}{2E_{\mathbf p}} = \mathcal P\frac{1}{p^2 - m^2} - i\pi\operatorname{sgn}(p^0)\,\delta(p^2 - m^2) .
> $$
>
> **Step 7** (part 3). At fixed $\mathbf p$, $c(\mathbf p)$ is a positive constant, and Steps 1–3 only use $b > 0$ and $b \to 0$; the uniformity of Step 5 holds if $c$ is bounded above and below on bounded sets of $\mathbf p$ and grows at most polynomially.
>
> **What the derivation shows.**
> - The $i\varepsilon$ denominators are limits in $\mathcal S'$; they agree with $1/(p^2 - m^2)$ off the mass shell and differ only on it, by $\delta(p^2 - m^2)$ or $\operatorname{sgn}(p^0)\delta(p^2 - m^2)$: so $\varepsilon = 0$ may be set wherever $p^2 \ne m^2$ ([[§CA.2 Generalized Functions#^cau-ca-2-1|§CA.2, Caution: What the formula does and does not say]]).
> - Both shell terms are Lorentz invariant ([[§CA.2 Generalized Functions#^thm-ca-2-6|Theorem §CA.2.6]]): the Feynman prescription is manifestly so, the retarded one under orthochronous transformations only.
> - Used in: the Feynman propagator and the differences on the shell ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-9|Theorem §C2b.6.9]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-11|Theorem §C2b.6.11]]), the family relations ([[§C2b.7 Wick Rotation and the Two-Point Family#^thm-c2b-7-5|Theorem §C2b.7.5]]).

^der-ca-3-11

*Uses:* [[§CA.2 Generalized Functions#^thm-ca-2-11|Theorem §CA.2.11]], [[§CA.2 Generalized Functions#^thm-ca-2-5|Theorem §CA.2.5]], [[§CA.2 Generalized Functions#^thm-ca-2-6|Theorem §CA.2.6]], [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|Theorem §CA.1.1]]

## Fourier transforms of Lorentz-invariant functions

> [!theorem] Theorem §CA.3.12: Fourier Transforms of Lorentz-Invariant Functions
> 1. If $\tilde f \in \mathcal S'(\mathbb R^4)$ is Lorentz invariant, so is $f$. A continuous invariant function on the open set $x^2 \ne 0$ depends only on $x^2$ and, inside the cone, on $\operatorname{sgn}x^0$.
> 2. *(Euclidean radial transform)* If $\int_0^\infty p^3|F(p)|\,dp < \infty$, then with $R = |x_E|$,
>
> $$
> \int d^4p_E\,F(|p_E|)\,e^{ip_E\cdot x_E} = \frac{4\pi^2}{R}\int_0^\infty dp\,p^2F(p)\,J_1(pR) .
> $$
>
> 3. *(Minkowski: choose the frame)* At spacelike $x$ the transform may be computed at $x = (0, \mathbf x)$, at timelike $x$ at $x = (x^0, \mathbf 0)$; the $d^3p$ integral then reduces to one dimension, by [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-9|Theorem §CA.3.9]] in the first case and by $d^3p = 4\pi p^2dp$ in the second.
>
> *Source: the user's PHY 513 notes, App. A §A.3 ("The four-dimensional version"), Ch. 6 §6.3 (rule 3) · standard (Stein & Weiss's radial formula in four dimensions; Poisson's integral, DLMF §10.9)*

^thm-ca-3-12

> [!derivation]- Derivation
> **Step 1** (part 1: invariance passes to the transform). With $\check\varphi(p) = \int\frac{d^4x}{(2\pi)^4}\varphi(x)e^{-ip\cdot x}$, the test function whose transform $\int d^4p\,\check\varphi(p)e^{ip\cdot x}$ (the transform on test functions of [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-5|Theorem §CA.3.5]], Step 3) is $\varphi$, so that $f[\varphi] = \tilde f[\check\varphi]$, the substitution $x = \Lambda y$ ($|\det\Lambda| = 1$, $p\cdot\Lambda y = \Lambda^{-1}p\cdot y$) gives $\mathcal F^{-1}(\varphi\circ\Lambda^{-1}) = \check\varphi\circ\Lambda^{-1}$. Then $f[\varphi\circ\Lambda^{-1}] = \tilde f[\check\varphi\circ\Lambda^{-1}] = \tilde f[\check\varphi] = f[\varphi]$ (Theorem §CA.3.2 and [[§CA.2 Generalized Functions#^def-ca-2-5|Def. §CA.2.5]]). This is rule 4 of [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-4|Theorem §CA.3.4]] for distributions.
>
> **Step 2** (part 1: the orbits). Rotate $\mathbf x$ onto the $x^1$-axis: $x = (t, r, 0, 0)$. If $t^2 - r^2 = c > 0$ and $t > 0$, boost along $x^1$ with $v = r/t$: $\gamma = t/\sqrt c$, $t' = \gamma(t - vr) = \frac{t}{\sqrt c}\cdot\frac{c}{t} = \sqrt c$, $x'^1 = \gamma(r - vt) = 0$. If $c < 0$, boost with $v = t/r$: $t' = 0$, $x'^1 = \frac{r}{\sqrt{-c}}\cdot\frac{r^2 - t^2}{r} = \sqrt{-c}$. So every point with $x^2 = c$ is carried to $(\pm\sqrt c, \mathbf 0)$ ($c > 0$, sign of $x^0$ kept) or $(0, \sqrt{-c}, 0, 0)$ ($c < 0$), and an invariant function is constant on each such set.
>
> **Step 3** (part 2: hyperspherical coordinates). $p_E = p(\cos\chi, \sin\chi\cos\theta, \sin\chi\sin\theta\cos\varphi, \sin\chi\sin\theta\sin\varphi)$ with $\chi, \theta \in [0, \pi]$, $\varphi \in [0, 2\pi)$ has $d^4p_E = p^3\sin^2\chi\sin\theta\,dp\,d\chi\,d\theta\,d\varphi$ (check: $\int\sin^2\chi\,d\chi\int\sin\theta\,d\theta\int d\varphi = \frac\pi2\cdot2\cdot2\pi = 2\pi^2$, the area of the unit 3-sphere). Rotate the dummy variable so that $x_E$ lies along $\chi = 0$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|Theorem §CA.3.7]], 4): $p_E\cdot x_E = pR\cos\chi$. The $\theta$ and $\varphi$ integrals give $4\pi$.
>
> **Step 4** (part 2: the $\chi$ integral). Poisson's integral, $J_\nu(z) = \frac{(z/2)^\nu}{\Gamma(\nu + \frac12)\Gamma(\frac12)}\int_0^\pi\cos(z\cos\chi)\sin^{2\nu}\chi\,d\chi$ (DLMF §10.9; the $\sin(z\cos\chi)$ part of $e^{iz\cos\chi}$ integrates to zero, being odd under $\chi \to \pi - \chi$), with $\nu = 1$ and $\Gamma(\frac32)\Gamma(\frac12) = \frac\pi2$, gives $\int_0^\pi\sin^2\chi\,e^{ipR\cos\chi}d\chi = \pi\frac{J_1(pR)}{pR}$.
>
> **Step 5** (part 2: assemble). $\int_0^\infty p^3dp\,F(p)\cdot4\pi\cdot\pi\frac{J_1(pR)}{pR} = \frac{4\pi^2}{R}\int_0^\infty p^2F(p)J_1(pR)\,dp$. Absolute convergence: $|J_1(z)/z| \le \frac12$, so the integrand is bounded by $\frac12p^3|F|$.
>
> **Step 6** (check: the Euclidean propagator). $F = 1/(p^2 + m^2)$ violates the hypothesis ($\int p\,dp$ diverges): the formula then holds with a conditionally convergent radial integral, and the table integral $\int_0^\infty\frac{p^2J_1(pR)}{p^2 + m^2}dp = mK_1(mR)$ (DLMF §10.22; quoted) gives $\int\frac{d^4p_E}{(2\pi)^4}\frac{e^{ip_E\cdot x_E}}{p_E^2 + m^2} = \frac{1}{(2\pi)^4}\cdot\frac{4\pi^2}{R}mK_1(mR) = \frac{mK_1(mR)}{4\pi^2R}$, the Euclidean propagator found by Schwinger's route ([[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-1|Theorem §C2b.3.1]]).
>
> **Step 7** (part 3). By part 1 the transform at $x$ equals its value at the representative of Step 2. At $x = (0, \mathbf x)$ the phase $e^{-ip\cdot x}$ is $e^{i\mathbf p\cdot\mathbf x}$, and the angular integral applies; at $x = (t, \mathbf 0)$ it is $e^{-ip^0t}$, independent of the direction of $\mathbf p$, and $d^3p = 4\pi p^2dp$.
>
> **What the derivation shows.**
> - Lorentz invariance reduces a four-dimensional transform to a one-dimensional integral: $J_1$ (and then $K_1$) in Euclidean signature, a sine transform or a radial integral in Minkowski signature after a choice of frame.
> - Used in: Lorentz invariance of $D_W$ as a distribution ([[§C2b.2 The Wightman Function#^thm-c2b-2-3|Theorem §C2b.2.3]]), the frame choices of [[§C2b.3 Explicit Forms of the Wightman Function|§C2b.3]], and $D_E$ in position space ([[§C2b.7 Wick Rotation and the Two-Point Family|§C2b.7]]).

^der-ca-3-12

*Uses:* [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-2|Theorem §CA.3.2]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|Theorem §CA.3.7]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-9|Theorem §CA.3.9]], [[§CA.2 Generalized Functions#^def-ca-2-5|Def. §CA.2.5]], [[§CA.5 Gaussian Integrals, Stationary Phase and Bessel Functions#^thm-ca-5-3|Theorem §CA.5.3]]

> [!remark]- Connections
> - The angular integral is the first step of every position-space propagator: the Wightman function ([[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-3|Theorem §C2b.3.3]]), the scattering Green's function $-e^{ik\rho}/4\pi\rho$ ([[§C10.1 The Lippmann–Schwinger Equation and the Born Approximation#^thm-c10-1-3|QM Theorem §C10.1.3]]) and the Yukawa potential ([[§B4.1 The Klein–Gordon Equation#^rem-b4-1-4|REL Remark: Static solutions and the Yukawa potential]]).
> - Integration by parts with a delta function is how $[\pi, H]$ acquires $\nabla^2\phi$ ([[§C2b.1 Heisenberg Fields#^thm-c2b-1-2|Theorem §C2b.1.2]]); the divergence theorem behind it is [[§28 The Divergence Theorem in Higher Dimensions and Green's Identities#^thm-28-1|452 Thm. §28.1]], and the four-dimensional version is the step in every Euler–Lagrange and Noether derivation (Euler–Lagrange: [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^der-c1b-2-4|Derivation §C1b.2.4]], step 4; Noether charges: [[§C1b.5 Noether's Theorem#^thm-c1b-5-3|Theorem §C1b.5.3]], [[§C1b.7 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^der-c1b-7-4|Derivation §C1b.7.4]], step 7).
> - Plancherel with $(2\pi)^{-3}$ on the momentum side is why the norm of a one-particle wave packet is $\int\frac{d^3p}{(2\pi)^32E_{\mathbf p}}|g|^2$, and why the number of particles radiated by a source is finite when $\tilde j$ is a Schwartz function ([[§C2b.8 Particle Production by a Classical Source|§C2b.8]]).
> - The damping factor of Theorem §CA.3.10 is the impulse response of a damped oscillator seen from the frequency side ([[§B4.4 Fourier Transforms and the Delta Function#^thm-b4-4-6|WO Theorem §B4.4.6]]) and the adiabatic switching $e^{\eta t}$, $\eta \to 0^+$, of time-dependent perturbation theory ([[§C9.6 The Interaction Picture and the Atom–Field Interaction|QM §C9.6]]).
> - Inversion for functions that are only piecewise smooth and integrable, with the midpoint value at jumps, is the Fourier integral theorem of [[§18 Fourier Integral#^thm-18-1|341 Thm. §18.1]]; Theorem §CA.3.1 trades that generality for Schwartz functions, the class on which the transform extends to distributions.
> - The Euclidean radial formula with $J_1$ is the four-dimensional analogue of the sine transform of Theorem §CA.3.9: in $n$ dimensions the kernel is $J_{n/2 - 1}(pR)/(pR)^{n/2 - 1}$, which for $n = 3$ is proportional to $\sin(pR)/pR$.
> - Theorem §CA.3.1 on a periodic lattice block (inversion and Parseval) is the step that turns a lattice energy into a sum over wavevectors and bounds it by the lowest eigenvalue of the transformed interaction, the Luttinger–Tisza method ([[§M3.3 The Luttinger–Tisza Method#^thm-m3-3-3|Thesis Thm. §M3.3.3]], [[§M3.3 The Luttinger–Tisza Method#^thm-m3-3-5|Thesis Thm. §M3.3.5]]).
> - **Used in**, statement by statement (C2a–C2b items):
>   - Def. §CA.3.1 (conventions): the transform $\tilde f$ of a smearing function — [[§C2a.1 Canonical Quantization of Fields|§C2a.1]] (conventions), [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-7|Theorem §C2a.2.7]], [[§C2b.1 Heisenberg Fields#^thm-c2b-1-6|Theorem §C2b.1.6]].
>   - Theorem §CA.3.1 (inversion, Plancherel): mode extraction and wave-packet norms — [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-4|Theorem §C2a.2.4]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|Theorem §C2a.2.6]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-7|Theorem §C2a.2.7]], [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-7|Theorem §C2a.4.7]], [[§C2b.1 Heisenberg Fields#^thm-c2b-1-6|Theorem §C2b.1.6]], [[§C2b.2 The Wightman Function#^thm-c2b-2-2|Theorem §C2b.2.2]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-7|Theorem §C2b.6.7]], [[§C2b.8 Particle Production by a Classical Source#^thm-c2b-8-4|Theorem §C2b.8.4]].
>   - Theorem §CA.3.2 (transform in $\mathcal S'$): transforms of two-point functions and of $i\varepsilon$ expressions — [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-1|Theorem §C2a.2.1]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-2|Theorem §C2a.2.2]], [[§C2a.6 Coherent States and the Classical Field#^thm-c2a-6-4|Theorem §C2a.6.4]], [[§C2b.2 The Wightman Function#^thm-c2b-2-2|Theorem §C2b.2.2]], [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-1|Theorem §C2b.3.1]], [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-4|Theorem §C2b.3.4]], [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-11|Theorem §C2b.4.11]], [[§C2b.1 Heisenberg Fields#^thm-c2b-1-3|Theorem §C2b.1.3]], [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-4|Theorem §C2b.5.4]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-10|Theorem §C2b.6.10]], [[§C2b.7 Wick Rotation and the Two-Point Family#^thm-c2b-7-4|Theorem §C2b.7.4]], [[§C2b.8 Particle Production by a Classical Source#^thm-c2b-8-4|Theorem §C2b.8.4]].
>   - Theorem §CA.3.3 (plane-wave delta): orthonormality of modes, $(f_{\mathbf p}, f_{\mathbf q}) = (2\pi)^3\delta^3$ — [[§C2a.1 Canonical Quantization of Fields|§C2a.1]] (conventions), [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-1|Theorem §C2a.2.1]], [[§C2a.2 Mode Expansion and the Mode Algebra#^rem-c2a-2-2|Remark: Two bookkeeping rules]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-3|Theorem §C2a.2.3]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-5|Theorem §C2a.2.5]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|Theorem §C2a.2.6]], [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-1|Theorem §C2a.3.1]], [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-4|Theorem §C2a.3.4]], [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-5|Theorem §C2a.3.5]], [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-4|Theorem §C2a.5.4]], [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-5|Theorem §C2a.5.5]], [[P1 Canonical Quantization#^p1-5|P1, step 5]], [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-10|Theorem §C2b.4.10]], [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-11|Theorem §C2b.4.11]], [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-3|Theorem §C2b.5.3]], [[P2 Green's Functions by Contour Integration#^p2-1|P2, step 1]].
>   - Theorem §CA.3.4 (rules): plane-wave deltas in mode computations, reality $\tilde f(-\mathbf p) = \overline{\tilde f(\mathbf p)}$ — [[§C2a.1 Canonical Quantization of Fields|§C2a.1]] (conventions), [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-1|Theorem §C2a.2.1]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-3|Theorem §C2a.2.3]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|Theorem §C2a.2.6]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-7|Theorem §C2a.2.7]], [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-1|Theorem §C2a.3.1]], [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-4|Theorem §C2a.3.4]], [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-5|Theorem §C2a.3.5]], [[§C2b.1 Heisenberg Fields#^thm-c2b-1-6|Theorem §C2b.1.6]], [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-10|Theorem §C2b.4.10]], [[§C2b.1 Heisenberg Fields#^thm-c2b-1-3|Theorem §C2b.1.3]], [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-3|Theorem §C2b.5.3]], [[§C2b.8 Particle Production by a Classical Source#^thm-c2b-8-1|Theorem §C2b.8.1]].
>   - Theorem §CA.3.5 (translation, phase; rules in $\mathcal S'$): Green's function as division, $\tilde j$ — [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-1|Theorem §C2a.2.1]], [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-7|Theorem §C2a.4.7]], [[§C2b.1 Heisenberg Fields#^thm-c2b-1-6|Theorem §C2b.1.6]], [[§C2b.2 The Wightman Function#^thm-c2b-2-2|Theorem §C2b.2.2]], [[§C2b.2 The Wightman Function#^thm-c2b-2-4|Theorem §C2b.2.4]], [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-4|Theorem §C2b.4.4]], [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-11|Theorem §C2b.4.11]], [[§C2b.1 Heisenberg Fields#^thm-c2b-1-3|Theorem §C2b.1.3]], [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-4|Theorem §C2b.5.4]], [[P2 Green's Functions by Contour Integration#^p2-1|P2, step 1]].
>   - Theorem §CA.3.6 (exchanging integrals; split exponentials): every mode computation — [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-1|Theorem §C2a.2.1]], [[§C2a.2 Mode Expansion and the Mode Algebra#^rem-c2a-2-2|Remark: Two bookkeeping rules]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-3|Theorem §C2a.2.3]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-4|Theorem §C2a.2.4]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-5|Theorem §C2a.2.5]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|Theorem §C2a.2.6]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-7|Theorem §C2a.2.7]], [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-1|Theorem §C2a.3.1]], [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-4|Theorem §C2a.5.4]], [[P1 Canonical Quantization#^p1-5|P1, step 5]], [[§C2b.1 Heisenberg Fields#^thm-c2b-1-6|Theorem §C2b.1.6]], [[§C2b.2 The Wightman Function#^thm-c2b-2-2|Theorem §C2b.2.2]], [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-4|Theorem §C2b.5.4]], [[§C2b.8 Particle Production by a Classical Source#^thm-c2b-8-1|Theorem §C2b.8.1]].
>   - Theorem §CA.3.7 (changes of variable): relabelling in mode sums, frames — [[§C2a.2 Mode Expansion and the Mode Algebra#^rem-c2a-2-2|Remark: Two bookkeeping rules]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-2|Theorem §C2a.2.2]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-4|Theorem §C2a.2.4]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-5|Theorem §C2a.2.5]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-7|Theorem §C2a.2.7]], [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-1|Theorem §C2a.3.1]], [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-5|Theorem §C2a.3.5]], [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-7|Theorem §C2a.4.7]], [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-2|Theorem §C2a.5.2]], [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-4|Theorem §C2a.5.4]], [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-5|Theorem §C2a.5.5]], [[§C2b.1 Heisenberg Fields#^thm-c2b-1-4|Theorem §C2b.1.4]], [[§C2b.2 The Wightman Function#^thm-c2b-2-3|Theorem §C2b.2.3]], [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-3|Theorem §C2b.3.3]], [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-4|Theorem §C2b.4.4]], [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-10|Theorem §C2b.4.10]], [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-11|Theorem §C2b.4.11]], [[§C2b.1 Heisenberg Fields#^thm-c2b-1-3|Theorem §C2b.1.3]], [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-5|Theorem §C2b.5.5]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-2|Theorem §C2b.6.2]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-4|Theorem §C2b.6.4]], [[§C2b.7 Wick Rotation and the Two-Point Family#^thm-c2b-7-2|Theorem §C2b.7.2]], [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-7|Theorem §C2b.5.7]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-3|Theorem §C2b.6.3]], [[P2 Green's Functions by Contour Integration#^p2-6|P2, step 6]].
>   - Theorems §CA.3.8–§CA.3.9 (integration by parts; angular integrals): the gradient term with fall-off, the zero-point energy density — [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-4|Theorem §C2a.5.4]], [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-4|Theorem §C2a.3.4]], [[§C2b.1 Heisenberg Fields#^thm-c2b-1-2|Theorem §C2b.1.2]], [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-3|Theorem §C2b.3.3]].
>   - Theorem §CA.3.10 (damping, $\tilde\theta$): the retarded function, the $i\varepsilon$ from switching — [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-3|Theorem §C2b.3.3]].
>   - Theorem §CA.3.11 ($i\varepsilon$ limits): $D_F$ and $D_R$ in momentum space as limits in $\mathcal S'$ — [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-2|Theorem §C2b.6.2]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-9|Theorem §C2b.6.9]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-10|Theorem §C2b.6.10]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-11|Theorem §C2b.6.11]], [[§C2b.7 Wick Rotation and the Two-Point Family#^thm-c2b-7-4|Theorem §C2b.7.4]], [[§C2b.7 Wick Rotation and the Two-Point Family#^thm-c2b-7-5|Theorem §C2b.7.5]], [[P2 Green's Functions by Contour Integration#^p2-3|P2, step 3]].
>   - Theorem §CA.3.12 (invariant transforms): [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-3|Theorem §C2b.3.3]].
> - **Used in**, statement by statement (C1a–C1b items):
>   - Def. §CA.3.1 (conventions): [[§C1a.3 Causal Structure and the Causality of a Single Particle#^thm-c1a-3-2|Theorem §C1a.3.2]], [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-8|Theorem §C1a.5.8]].
>   - Theorems §CA.3.1–§CA.3.3 (inversion, transform in $\mathcal S'$, plane-wave delta): the single-particle amplitude as a Fourier transform — [[§C1a.3 Causal Structure and the Causality of a Single Particle#^thm-c1a-3-2|Theorem §C1a.3.2]].
>   - Theorem §CA.3.4 (rules): derivatives of plane waves — [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-8|Theorem §C1a.5.8]], [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-11|Theorem §C1a.5.11]].
>   - Theorem §CA.3.5 (translation, phase; rules in $\mathcal S'$): [[§C1a.3 Causal Structure and the Causality of a Single Particle#^thm-c1a-3-2|Theorem §C1a.3.2]], [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-8|Theorem §C1a.5.8]].
>   - Theorem §CA.3.7 (changes of variable): [[§C1a.3 Causal Structure and the Causality of a Single Particle#^thm-c1a-3-5|Theorem §C1a.3.5]], [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-10|Theorem §C2b.3.10]].
>   - Theorems §CA.3.8–§CA.3.9 (integration by parts; angular integrals): [[§C1a.3 Causal Structure and the Causality of a Single Particle#^thm-c1a-3-5|Theorem §C1a.3.5]], [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-4|Theorem §C1b.2.4]], [[§C1b.4 Hamiltonian Field Theory#^thm-c1b-4-4|Theorem §C1b.4.4]], [[§C1b.7 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^thm-c1b-7-4|Theorem §C1b.7.4]].
> - **Used in**, statement by statement (C5a–C5b items):
>   - Def. §CA.3.1 (conventions): [[§C5b.1 Canonical Quantization of the Dirac Field|§C5b.1]], [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality|§C5b.7]] (conventions).
>   - Theorem §CA.3.1 (inversion, Plancherel): the classical Dirac charge is positive — [[§C5b.5 The U(1) Charge, Particles and Antiparticles#^thm-c5b-5-2|Theorem §C5b.5.2]].
>   - Theorem §CA.3.2 (transform in $\mathcal S'$): solutions as transforms, the mode expansion, the propagator limit — [[§C5a.6 Plane-Wave Solutions#^rem-c5a-6-6|§C5a.6, Remark: In what sense a general solution is a superposition of these plane waves]], [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-1|Theorem §C5b.2.1]], [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-4|Theorem §C5b.8.4]].
>   - Theorem §CA.3.3 (plane-wave delta): mode extraction, $H$ and $Q$ in modes, the mode algebra, spin at rest — [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-3|Theorem §C5b.2.3]], [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-2|Theorem §C5b.3.2]], [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-5|Theorem §C5b.2.5]], [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-4|Theorem §C5b.2.4]], [[§C5b.4 Fermions, Fock Space and the Pauli Principle#^thm-c5b-4-3|Theorem §C5b.4.3]].
>   - Theorem §CA.3.4 (rules): derivatives of plane waves in the mode expansion — [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-1|Theorem §C5b.2.1]].
>   - Theorem §CA.3.5 (translation, phase; rules in $\mathcal S'$): Dirac two-point functions as $i\slashed{\partial} + m$ applied to scalar ones — [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-1|Theorem §C5b.7.1]], [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-2|Theorem §C5b.7.2]], [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-3|Theorem §C5b.8.3]], [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-4|Theorem §C5b.8.4]].
>   - Theorem §CA.3.6 (exchanging integrals; split exponentials): [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-3|Theorem §C5b.2.3]], [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-2|Theorem §C5b.3.2]].
>   - Theorem §CA.3.7 (changes of variable): relabelling $\mathbf p \to -\mathbf p$ — [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-1|Theorem §C5b.2.1]], [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-4|Theorem §C5b.2.4]], [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-3|Theorem §C5b.8.3]].
>   - Theorem §CA.3.8 (integration by parts): the spin of the quanta at rest — [[§C5b.4 Fermions, Fock Space and the Pauli Principle#^thm-c5b-4-3|Theorem §C5b.4.3]].
>   - Theorem §CA.3.11 ($i\varepsilon$ limits): $S_F$ as a limit in $\mathcal S'$ — [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-3|Theorem §C5b.8.3]], [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-4|Theorem §C5b.8.4]], [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-5|Theorem §C5b.8.5]].
>   - Remark: A linear equation becomes algebra: the Dirac equation for plane waves — [[§C5a.6 Plane-Wave Solutions#^thm-c5a-6-1|Theorem §C5a.6.1]].
> - **Used in**, statement by statement (C4 items):
>   - Def. §CA.3.1 (Fourier Transform in Space and Spacetime): [[§C4.6 The Maxwell Field, Gauge Symmetry and Gauge Fixing#^cau-c4-6-1|§C4.6, Caution: Names of polarization vectors and mode operators across the sources]], [[§C4.9 Vector-Field Propagators#^cau-c4-9-1|§C4.9, Caution: Names and signs of the vector propagator]].
>   - Theorem §CA.3.2 (The Fourier Transform of Tempered Distributions): [[§C4.4★ Quantizing the Proca Field꞉ Modes and the Mode Algebra#^rem-c4-4-1|§C4.4★, Remark: In what sense the Proca field is a distribution]], [[§C4.4★ Quantizing the Proca Field꞉ Modes and the Mode Algebra#^thm-c4-4-5|Theorem §C4.4.5]], [[§C4.3★ Massive Polarization Vectors and Plane Waves|§C4.3★]], [[§C4.5★ Energy, Momentum and the Spin-One Quanta of the Proca Field#^thm-c4-5-7|Theorem §C4.5.7]], [[§C4.5★ Energy, Momentum and the Spin-One Quanta of the Proca Field#^thm-c4-5-8|Theorem §C4.5.8]], [[§C4.4★ Quantizing the Proca Field꞉ Modes and the Mode Algebra|§C4.4★]], [[§C4.5★ Energy, Momentum and the Spin-One Quanta of the Proca Field|§C4.5★]], [[§C4.8 The Gupta–Bleuler Condition and Physical Photons#^thm-c4-8-3|Theorem §C4.8.3]], [[§C4.8 The Gupta–Bleuler Condition and Physical Photons#^thm-c4-8-4|Theorem §C4.8.4]], [[§C4.8 The Gupta–Bleuler Condition and Physical Photons#^thm-c4-8-8|Theorem §C4.8.8]], [[§C4.8 The Gupta–Bleuler Condition and Physical Photons#^thm-c4-8-9|Theorem §C4.8.9]], [[§C4.9 Vector-Field Propagators#^rem-c4-9-2|§C4.9, Remark: The sign of the photon propagator and negative norm]], [[§C4.9 Vector-Field Propagators#^thm-c4-9-7|Theorem §C4.9.7]].
>   - Theorem §CA.3.3 (Plane Waves Integrate to a Delta Function): [[§C4.4★ Quantizing the Proca Field꞉ Modes and the Mode Algebra#^rem-c4-4-2|§C4.4★, Remark: Why A⁰ drops out]], [[§C4.4★ Quantizing the Proca Field꞉ Modes and the Mode Algebra#^thm-c4-4-6|Theorem §C4.4.6]], [[§C4.4★ Quantizing the Proca Field꞉ Modes and the Mode Algebra#^thm-c4-4-7|Theorem §C4.4.7]], [[§C4.5★ Energy, Momentum and the Spin-One Quanta of the Proca Field#^thm-c4-5-2|Theorem §C4.5.2]], [[§C4.5★ Energy, Momentum and the Spin-One Quanta of the Proca Field#^thm-c4-5-3|Theorem §C4.5.3]], [[§C4.4★ Quantizing the Proca Field꞉ Modes and the Mode Algebra|§C4.4★]], [[§C4.5★ Energy, Momentum and the Spin-One Quanta of the Proca Field|§C4.5★]], [[§C4.6 The Maxwell Field, Gauge Symmetry and Gauge Fixing#^thm-c4-6-4|Theorem §C4.6.4]], [[§C4.6 The Maxwell Field, Gauge Symmetry and Gauge Fixing#^thm-c4-6-5|Theorem §C4.6.5]], [[§C4.7 Covariant Quantization and the Indefinite Metric#^mod-c4-7-4|Model §C4.7.4]], [[§C4.7 Covariant Quantization and the Indefinite Metric#^thm-c4-7-10|Theorem §C4.7.10]], [[§C4.7 Covariant Quantization and the Indefinite Metric#^thm-c4-7-11|Theorem §C4.7.11]], [[§C4.7 Covariant Quantization and the Indefinite Metric#^thm-c4-7-12|Theorem §C4.7.12]], [[§C4.7 Covariant Quantization and the Indefinite Metric#^thm-c4-7-13|Theorem §C4.7.13]].
>   - Theorem §CA.3.4 (Rules of the Fourier Transform): [[§C4.4★ Quantizing the Proca Field꞉ Modes and the Mode Algebra#^rem-c4-4-1|§C4.4★, Remark: In what sense the Proca field is a distribution]], [[§C4.4★ Quantizing the Proca Field꞉ Modes and the Mode Algebra#^thm-c4-4-7|Theorem §C4.4.7]], [[§C4.5★ Energy, Momentum and the Spin-One Quanta of the Proca Field#^thm-c4-5-2|Theorem §C4.5.2]], [[§C4.6 The Maxwell Field, Gauge Symmetry and Gauge Fixing#^rem-c4-6-1|§C4.6, Remark: The longitudinal mode decouples from conserved currents]], [[§C4.9 Vector-Field Propagators#^thm-c4-9-9|Theorem §C4.9.9]], [[§C4.9 Vector-Field Propagators#^thm-c4-9-10|Theorem §C4.9.10]].
>   - Theorem §CA.3.5 (Translation, Phase, and the Rules in 𝒮′): [[§C4.6 The Maxwell Field, Gauge Symmetry and Gauge Fixing#^thm-c4-6-4|Theorem §C4.6.4]], [[§C4.6 The Maxwell Field, Gauge Symmetry and Gauge Fixing#^thm-c4-6-5|Theorem §C4.6.5]], [[§C4.9 Vector-Field Propagators#^rem-c4-9-1|§C4.9, Remark: The covariant replacement rule]], [[§C4.9 Vector-Field Propagators#^thm-c4-9-1|Theorem §C4.9.1]], [[§C4.9 Vector-Field Propagators#^thm-c4-9-2|Theorem §C4.9.2]], [[§C4.9 Vector-Field Propagators#^thm-c4-9-3|Theorem §C4.9.3]], [[§C4.9 Vector-Field Propagators#^thm-c4-9-4|Theorem §C4.9.4]], [[§C4.9 Vector-Field Propagators|§C4.9]].
>   - Theorem §CA.3.6 (Exchanging the Space and Momentum Integrals): [[§C4.4★ Quantizing the Proca Field꞉ Modes and the Mode Algebra#^rem-c4-4-1|§C4.4★, Remark: In what sense the Proca field is a distribution]], [[§C4.3★ Massive Polarization Vectors and Plane Waves|§C4.3★]], [[§C4.4★ Quantizing the Proca Field꞉ Modes and the Mode Algebra#^rem-c4-4-2|§C4.4★, Remark: Why A⁰ drops out]], [[§C4.4★ Quantizing the Proca Field꞉ Modes and the Mode Algebra#^thm-c4-4-6|Theorem §C4.4.6]], [[§C4.4★ Quantizing the Proca Field꞉ Modes and the Mode Algebra#^thm-c4-4-7|Theorem §C4.4.7]], [[§C4.5★ Energy, Momentum and the Spin-One Quanta of the Proca Field#^thm-c4-5-3|Theorem §C4.5.3]], [[§C4.6 The Maxwell Field, Gauge Symmetry and Gauge Fixing#^thm-c4-6-4|Theorem §C4.6.4]], [[§C4.6 The Maxwell Field, Gauge Symmetry and Gauge Fixing#^thm-c4-6-5|Theorem §C4.6.5]], [[§C4.7 Covariant Quantization and the Indefinite Metric#^thm-c4-7-10|Theorem §C4.7.10]], [[§C4.7 Covariant Quantization and the Indefinite Metric#^thm-c4-7-11|Theorem §C4.7.11]].
>   - Theorem §CA.3.7 (Changes of Integration Variable: Relabelling, Shifting, Rescaling, Rotating): [[§C4.4★ Quantizing the Proca Field꞉ Modes and the Mode Algebra#^rem-c4-4-1|§C4.4★, Remark: In what sense the Proca field is a distribution]], [[§C4.4★ Quantizing the Proca Field꞉ Modes and the Mode Algebra#^thm-c4-4-5|Theorem §C4.4.5]], [[§C4.3★ Massive Polarization Vectors and Plane Waves|§C4.3★]], [[§C4.4★ Quantizing the Proca Field꞉ Modes and the Mode Algebra#^thm-c4-4-7|Theorem §C4.4.7]], [[§C4.5★ Energy, Momentum and the Spin-One Quanta of the Proca Field#^thm-c4-5-2|Theorem §C4.5.2]], [[§C4.5★ Energy, Momentum and the Spin-One Quanta of the Proca Field#^thm-c4-5-4|Theorem §C4.5.4]], [[§C4.5★ Energy, Momentum and the Spin-One Quanta of the Proca Field#^thm-c4-5-5|Theorem §C4.5.5]], [[§C4.5★ Energy, Momentum and the Spin-One Quanta of the Proca Field#^thm-c4-5-7|Theorem §C4.5.7]], [[§C4.5★ Energy, Momentum and the Spin-One Quanta of the Proca Field#^thm-c4-5-8|Theorem §C4.5.8]], [[§C4.7 Covariant Quantization and the Indefinite Metric#^thm-c4-7-14|Theorem §C4.7.14]], [[§C4.7 Covariant Quantization and the Indefinite Metric#^thm-c4-7-15|Theorem §C4.7.15]].
>   - Theorem §CA.3.8 (Integration by Parts; the Gradient of a Delta Function): [[§C4.2★ The Proca Field#^thm-c4-2-9|Theorem §C4.2.9]], [[§C4.2★ The Proca Field#^thm-c4-2-10|Theorem §C4.2.10]], [[§C4.2★ The Proca Field|§C4.2★]], [[§C4.4★ Quantizing the Proca Field꞉ Modes and the Mode Algebra#^rem-c4-4-2|§C4.4★, Remark: Why A⁰ drops out]], [[§C4.4★ Quantizing the Proca Field꞉ Modes and the Mode Algebra#^thm-c4-4-3|Theorem §C4.4.3]], [[§C4.4★ Quantizing the Proca Field꞉ Modes and the Mode Algebra#^thm-c4-4-6|Theorem §C4.4.6]], [[§C4.6 The Maxwell Field, Gauge Symmetry and Gauge Fixing#^thm-c4-6-4|Theorem §C4.6.4]], [[§C4.6 The Maxwell Field, Gauge Symmetry and Gauge Fixing#^thm-c4-6-5|Theorem §C4.6.5]], [[§C4.7 Covariant Quantization and the Indefinite Metric#^thm-c4-7-6|Theorem §C4.7.6]], [[§C4.7 Covariant Quantization and the Indefinite Metric#^thm-c4-7-7|Theorem §C4.7.7]].
>   - Derivation (Derivation): [[§C4.9 Vector-Field Propagators#^thm-c4-9-7|Theorem §C4.9.7]].
>   - Theorem §CA.3.11 (The iε Limits of the Propagator Denominators): [[§C4.9 Vector-Field Propagators#^rem-c4-9-2|§C4.9, Remark: The sign of the photon propagator and negative norm]], [[§C4.9 Vector-Field Propagators#^thm-c4-9-7|Theorem §C4.9.7]], [[§C4.9 Vector-Field Propagators|§C4.9]].
> - **Used in**, statement by statement (Electromagnetism C items):
>   - Def. §CA.3.1 (conventions): plane-wave solutions, the free field in Fourier space — [[§C1.1 Building the Maxwell Action#^ex-c1-1-1|EM Example §C1.1.1]], [[§C1.4 Gauge Fixing and the Two Polarizations#^thm-c1-4-4|EM Theorem §C1.4.4]].
>   - Theorem §CA.3.1 (inversion, Plancherel): Klein–Gordon solutions as superpositions of plane waves — [[§C1.1 Building the Maxwell Action#^ex-c1-1-1|EM Example §C1.1.1]].
>   - Theorem §CA.3.3 (plane-wave delta): the cylindrical form of the free Green function — [[§C7.4 Constructing Green Functions#^thm-c7-4-2|EM Theorem §C7.4.2]].
>   - Theorem §CA.3.4 (rules): derivatives of plane waves, the transverse current, two degrees of freedom per point — [[§C1.1 Building the Maxwell Action#^ex-c1-1-1|EM Example §C1.1.1]], [[§C1.4 Gauge Fixing and the Two Polarizations#^thm-c1-4-2|EM Theorem §C1.4.2]], [[§C1.4 Gauge Fixing and the Two Polarizations#^thm-c1-4-4|EM Theorem §C1.4.4]].
>   - Theorem §CA.3.5 (translation, phase; rules in $\mathcal S'$): conservation of the point-charge current in Fourier space — [[§C1.3 Gauge Symmetry and Charge Conservation#^ex-c1-3-1|EM Example §C1.3.1]].
>   - Theorem §CA.3.8 (integration by parts): the Coulomb force from the potential energy, the second derivatives of $1/r$, the dipole layer — [[§C2.3 Electrostatic Energy and Self-Energy#^thm-c2-3-1|EM Theorem §C2.3.1]], [[§C3.1 Cartesian Multipole Moments and Dipole Layers#^thm-c3-1-3|EM Theorem §C3.1.3]], [[§C3.1 Cartesian Multipole Moments and Dipole Layers#^thm-c3-1-9|EM Theorem §C3.1.9]].
>   - Theorem §CA.3.10 (damping): the two-tube electron lens by a Fourier integral — [[§C6.3 Separation in Cylindrical and Polar Coordinates#^ex-c6-3-1|EM Example §C6.3.1]].
