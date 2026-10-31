---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C6b
section: C6b.7
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C6b.6 Amplitudes from Correlation Functions]] · ↑ [[· C6b The S-Matrix, Amplitudes and Observables]] · [[§C9.1 Discrete Lorentz Transformations]] →

*Sources: PHY 513, Problem Set 8, Problem 3 (based on PS Problem 4.1; the user's solution, parts (a)–(f), submitted 2026-10-30) · Peskin & Schroeder, An Introduction to Quantum Field Theory, Problem 4.1; §2.4, pp. 32–33, eqs. (2.61)–(2.66) · the course's time-ordered exponential and Wick's theorem ([[§C6a.3 The Time-Evolution Operator and Time Ordering|§C6a.3]], [[§C6a.6 Wick's Theorem|§C6a.6]]).*

A classical source switched on for a finite time leaves the vacuum in a state with some particles. [[§C2b.8 Particle Production by a Classical Source|§C2b.8]] answered this with the retarded function: the late-time field has shifted annihilation operators and the final state is a coherent state, with Poisson-distributed particle number. This section reaches the same answer the way Problem Set 8 asks, through the interaction picture: the probabilities are squares of matrix elements of the time-ordered exponential ([[§C6a.3 The Time-Evolution Operator and Time Ordering#^def-c6a-3-1|Def. §C6a.3.1]]), Wick's theorem turns them into diagrams with one-legged **source vertices**, and the vacuum diagrams exponentiate. Two tools appear that the earlier sections lacked, written here in the general form so that they can move: the contraction of a field with an outgoing particle ([[§C6b.7 Particle Production by a Classical Source꞉ the Diagrammatic Route#^lem-c6b-7-4|Lemma §C6b.7.4]]) and the measure on $n$-particle states ([[§C6b.7 Particle Production by a Classical Source꞉ the Diagrammatic Route#^thm-c6b-7-6|Theorem §C6b.7.6]]). Everything below is the user's solution, tagged by part.

*Conventions* ([[Larsen PHY 513]]): the source model is [[§C2b.5 Green's Functions and Contours#^mod-c2b-5-1|Model §C2b.5.1]], $j$ real, smooth, nonzero only for a finite time, $\hat H_{\rm int}(t) = -\int d^3x\,j(t, \mathbf x)\,\hat\phi(\mathbf x)$; $\tilde j(k) = \int d^4x\,e^{ik\cdot x}j(x)$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^def-ca-3-1|Def. §CA.3.1]]) with $k^0 = E_{\mathbf k}$ where stated; **one-particle states $|\mathbf k\rangle = \hat a^\dagger_{\mathbf k}|0\rangle$, not relativistically normalized** ([[§C6b.7 Particle Production by a Classical Source꞉ the Diagrammatic Route#^cau-c6b-7-1|Caution: Two normalizations of one-particle states]]); $\lambda$ is the mean number of particles produced (PS's letter; there is no $\phi^4$ coupling in this section); $\hat\phi^\pm$ the positive- and negative-frequency parts ([[§C2b.1 Heisenberg Fields#^thm-c2b-1-5|Theorem §C2b.1.5]]).

## The mathematics used here

A vacuum sum over diagrams weighted by $1/S$ is the exponential of its connected part:

![[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-3]]

and the counting of [[§CA.7 Pairings, Diagrams and Symmetry Factors|§CA.7]] holds for vertices with one leg, $|G_n| = n!$ ([[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-4|Theorem §CA.8.4]], 1 and 4).

## No particles

> [!theorem] Theorem §C6b.7.1: The Vacuum-Persistence Amplitude of a Source
> The probability that the source creates no particles is
>
> $$
> P(0) = |\mathcal A(0)|^2, \qquad \mathcal A(0) = \langle0|\,T\Bigl\{\exp\Bigl[i\int d^4x\,j(x)\,\hat\phi_I(x)\Bigr]\Bigr\}|0\rangle ,
> $$
>
> and the amplitude to end in a free state $|f\rangle$ is $\langle f|T\{\exp[i\int d^4x\,j\hat\phi_I]\}|0\rangle$.
>
> *Source: PHY 513, Problem Set 8, Problem 3(a) (the user's solution) · PS Problem 4.1(a)*

^thm-c6b-7-1

> [!derivation]- Derivation
> **Step 1** (interaction picture). $\hat H_0|0\rangle = 0$, and since $j = 0$ outside a finite time interval, before and after it the Hamiltonian is $\hat H_0$: the in and out states with no particles are $|0\rangle$. With the interaction-picture field $\hat\phi_I(t, \mathbf x) = e^{i\hat H_0t}\hat\phi(\mathbf x)e^{-i\hat H_0t}$ ([[§C6a.2 The Interaction Picture#^def-c6a-2-1|Def. §C6a.2.1]]),
>
> $$
> \hat H_I(t) = e^{i\hat H_0t}\hat H_{\rm int}(t)e^{-i\hat H_0t} = -\int d^3x\,j(t, \mathbf x)\,\hat\phi_I(t, \mathbf x) ,
> $$
>
> $j$ being a number. The evolution operator is the time-ordered exponential ([[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-8|Theorem §C6a.3.8]]; its derivation uses only $i\partial_tU = \hat H_I(t)U$, so an explicitly time-dependent $\hat H_I(t)$ is allowed):
>
> $$
> \hat U(t, t') = T\Bigl\{\exp\Bigl[-i\int_{t'}^tdt''\,\hat H_I(t'')\Bigr]\Bigr\} .
> $$
>
> **Step 2** (the amplitude). ${}_{\rm out}\langle0|0\rangle_{\rm in} = \lim_{T\to\infty}\langle0|\hat U(T, -T)|0\rangle$, and the exponent is
>
> $$
> -i\int_{-T}^Tdt\Bigl(-\int d^3x\,j(t, \mathbf x)\,\hat\phi_I(t, \mathbf x)\Bigr) = i\int_{-T}^Tdt\int d^3x\,j(x)\,\hat\phi_I(x) \;\xrightarrow{T\to\infty}\; i\int d^4x\,j(x)\,\hat\phi_I(x) ,
> $$
>
> the limit trivial because $j$ has compact support in time. So $\mathcal A(0)$ is as stated, $P(0) = |\mathcal A(0)|^2$; for any free final state the same steps give $\langle f|\hat U(\infty, -\infty)|0\rangle$.
>
> **What the derivation shows.**
> - Unlike $\phi^4$ theory ([[§C6a.4 The Interacting Vacuum and the Two-Point Function|§C6a.4]]) no $T(1 - i\varepsilon)$ projection is needed: the interaction is switched off, and the free vacuum is the in- and out-vacuum.

^der-c6b-7-1

*Uses:* [[§C6a.2 The Interaction Picture#^def-c6a-2-1|Def. §C6a.2.1]], [[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-8|Theorem §C6a.3.8]], [[§C2b.5 Green's Functions and Contours#^mod-c2b-5-1|Model §C2b.5.1]]

> [!theorem] Theorem §C6b.7.2: The No-Particle Probability to Order j²
> $$
> P(0) = 1 - \lambda + O(j^4), \qquad \lambda = \int\frac{d^3k}{(2\pi)^3}\,\frac{1}{2E_{\mathbf k}}\,\bigl|\tilde j(k)\bigr|^2\Big|_{k^0 = E_{\mathbf k}} ,
> $$
>
> with $\mathcal A(0) = 1 + \mathcal A_2 + O(j^4)$, $\mathcal A_2 = -\frac{i}{2}\int\frac{d^4p}{(2\pi)^4}\frac{|\tilde j(p)|^2}{p^2 - m^2 + i\varepsilon}$ and $2\operatorname{Re}\mathcal A_2 = -\lambda$. $\lambda$ is the mean number $\bar N$ of [[§C2b.8 Particle Production by a Classical Source#^thm-c2b-8-3|Theorem §C2b.8.3]].
>
> *Source: PHY 513, Problem Set 8, Problem 3(b) (the user's solution; the problem's comment: "Extracting that real part from the Feynman propagator is where the $i\epsilon$ prescription does its work") · PS Problem 4.1(b)*

^thm-c6b-7-2

> [!derivation]- Derivation
> **Step 1** (expand). $j$ is a number, so it and the integrals come out of the time ordering ([[§C6a.3 The Time-Evolution Operator and Time Ordering#^def-c6a-3-1|Def. §C6a.3.1]]):
>
> $$
> T\exp\Bigl(i\int d^4x\,j\hat\phi_I\Bigr) = \sum_{n\ge0}\frac{i^n}{n!}\int d^4x_1\cdots d^4x_n\,j(x_1)\cdots j(x_n)\,T\{\hat\phi_I(x_1)\cdots\hat\phi_I(x_n)\} ,
> $$
>
> the $n$-th term of order $j^n$. $P(0)$ to order $j^2$ with remainder $O(j^4)$ needs $\mathcal A(0) = 1 + \mathcal A_1 + \mathcal A_2 + \mathcal A_3 + O(j^4)$, $\mathcal A_n = \frac{i^n}{n!}\int\prod d^4x_i\,j(x_i)\,\langle0|T\{\hat\phi_I(x_1)\cdots\hat\phi_I(x_n)\}|0\rangle$.
>
> **Step 2** (the probability). $\mathcal A_n^{\ast}$ is of order $j^n$ like $\mathcal A_n$, so
>
> $$
> P(0) = (1 + \mathcal A_1 + \mathcal A_2 + \mathcal A_3)(1 + \mathcal A_1^{\ast} + \mathcal A_2^{\ast} + \mathcal A_3^{\ast}) + O(j^4) = 1 + 2\operatorname{Re}\mathcal A_1 + \bigl(2\operatorname{Re}\mathcal A_2 + |\mathcal A_1|^2\bigr) + \bigl(2\operatorname{Re}\mathcal A_3 + 2\operatorname{Re}(\mathcal A_1\mathcal A_2^{\ast})\bigr) + O(j^4) .
> $$
>
> **Step 3** (odd orders). Every term of the mode expansion of $\hat\phi_I$ has one $\hat a$ or one $\hat a^\dagger$, so $\langle0|\hat\phi_I(x)|0\rangle = 0$ and $\mathcal A_1 = 0$. By Wick's theorem ([[§C6a.6 Wick's Theorem#^thm-c6a-6-2|Theorem §C6a.6.2]]), with $\hat\phi_i \equiv \hat\phi_I(x_i)$, $D_{ij} = D_F(x_i - x_j)$,
>
> $$
> T\{\hat\phi_1\hat\phi_2\hat\phi_3\} = \,:\!\hat\phi_1\hat\phi_2\hat\phi_3\!: + \overbracket{\hat\phi_1\hat\phi_2}\,\hat\phi_3 + \overbracket{\hat\phi_1\hat\phi_3}\,\hat\phi_2 + \overbracket{\hat\phi_2\hat\phi_3}\,\hat\phi_1 = \,:\!\hat\phi_1\hat\phi_2\hat\phi_3\!: + D_{12}\hat\phi_3 + D_{13}\hat\phi_2 + D_{23}\hat\phi_1 ;
> $$
>
> every term keeps an uncontracted field, and $\langle0|{:}\cdots{:}|0\rangle = 0$ ([[§C6a.5 Normal Ordering and Contractions#^thm-c6a-5-1|Theorem §C6a.5.1]], 2), $\langle0|\hat\phi_i|0\rangle = 0$: $\mathcal A_3 = 0$. So $P(0) = 1 + 2\operatorname{Re}\mathcal A_2 + O(j^4)$.
>
> **Step 4** ($\mathcal A_2$). $\langle0|T\{\hat\phi_1\hat\phi_2\}|0\rangle = \langle0|{:}\hat\phi_1\hat\phi_2{:}|0\rangle + D_{12} = D_F(x_1 - x_2) = \int\frac{d^4p}{(2\pi)^4}\frac{i\,e^{-ip\cdot(x_1 - x_2)}}{p^2 - m^2 + i\varepsilon}$ ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-9|Theorem §C2b.6.9]]). With $e^{-ip\cdot(x_1 - x_2)} = e^{-ip\cdot x_1}e^{ip\cdot x_2}$ and the $p$-integral outside,
>
> $$
> \mathcal A_2 = -\frac12\int\frac{d^4p}{(2\pi)^4}\frac{i}{p^2 - m^2 + i\varepsilon}\underbrace{\int d^4x_1\,j(x_1)e^{-ip\cdot x_1}}_{\tilde j(-p)}\;\underbrace{\int d^4x_2\,j(x_2)e^{ip\cdot x_2}}_{\tilde j(p)} = -\frac i2\int\frac{d^4p}{(2\pi)^4}\frac{|\tilde j(p)|^2}{p^2 - m^2 + i\varepsilon} ,
> $$
>
> using $\tilde j(-p) = \tilde j(p)^{\ast}$ for real $j$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-4|Theorem §CA.3.4]], 4).
>
> **Step 5** (real part, the user's route). For real $A$, $B$, $C$: $\frac{A}{B + iC} = \frac{AB}{B^2 + C^2} - i\frac{AC}{B^2 + C^2}$. With $A = |\tilde j(p)|^2$, $B = p^2 - m^2$, $C = \varepsilon$, the first part times $-\frac i2$ is imaginary, so
>
> $$
> \operatorname{Re}\mathcal A_2 = -\frac12\int\frac{d^4p}{(2\pi)^4}\,|\tilde j(p)|^2\,\frac{\varepsilon}{(p^2 - m^2)^2 + \varepsilon^2} .
> $$
>
> $\frac{\varepsilon}{x^2 + \varepsilon^2}$ has area $\pi$ and tends to $\pi\delta(x)$ as $\varepsilon \to 0^+$ (after the integration); this is the $-i\pi\delta(p^2 - m^2)$ of [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-6|Theorem §CA.6.6]], 1, the home of the step. $p^2 - m^2 = (p^0)^2 - E_{\mathbf p}^2$ has simple zeros $p^0 = \pm E_{\mathbf p}$ with $|\partial_{p^0}(p^2 - m^2)| = 2E_{\mathbf p}$ ([[§CA.2 Generalized Functions#^thm-ca-2-6|Theorem §CA.2.6]], 2):
>
> $$
> \delta(p^2 - m^2) = \frac{\delta(p^0 - E_{\mathbf p})}{2E_{\mathbf p}} + \frac{\delta(p^0 + E_{\mathbf p})}{2E_{\mathbf p}}, \qquad \int dp^0\,\pi|\tilde j(p)|^2\delta(p^2 - m^2) = \frac{\pi}{2E_{\mathbf p}}\bigl(|\tilde j(E_{\mathbf p}, \mathbf p)|^2 + |\tilde j(-E_{\mathbf p}, \mathbf p)|^2\bigr) .
> $$
>
> **Step 6** (the two terms are equal). $\tilde j(-E_{\mathbf p}, \mathbf p) = \tilde j(E_{\mathbf p}, -\mathbf p)^{\ast}$ (reality), and $\mathbf p \to -\mathbf p$ in $\int d^3p$ (Jacobian 1, $E_{-\mathbf p} = E_{\mathbf p}$, [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|Theorem §CA.3.7]], 1) turns the second into the first. With $\frac{d^4p}{(2\pi)^4} = \frac{d^3p}{(2\pi)^3}\frac{dp^0}{2\pi}$:
>
> $$
> 2\operatorname{Re}\mathcal A_2 = -\int\frac{d^3p}{(2\pi)^3}\,\frac{1}{2\pi}\,\frac{\pi}{2E_{\mathbf p}}\,2\,|\tilde j(E_{\mathbf p}, \mathbf p)|^2 = -\int\frac{d^3p}{(2\pi)^3}\frac{|\tilde j(E_{\mathbf p}, \mathbf p)|^2}{2E_{\mathbf p}} = -\lambda .
> $$
>
> ⚑ By-product: only the on-shell values $\tilde j(E_{\mathbf p}, \mathbf p)$ enter: the $i\varepsilon$ selects the mass shell, and $\lambda = \bar N$ of [[§C2b.8 Particle Production by a Classical Source#^thm-c2b-8-3|Theorem §C2b.8.3]] (same integral): the source radiates only its on-shell components ([[§C2b.8 Particle Production by a Classical Source#^rem-c2b-8-1|§C2b.8, Remark: Only the on-shell part of the source radiates]]).
>
> **What the derivation shows.**
> - The imaginary part of $\mathcal A_2$ (a phase) does not enter $P(0)$; the real part is the $\delta$-function part of the Feynman propagator.

^der-c6b-7-2

*Uses:* [[§C6a.3 The Time-Evolution Operator and Time Ordering#^def-c6a-3-1|Def. §C6a.3.1]], [[§C6a.6 Wick's Theorem#^thm-c6a-6-2|Theorem §C6a.6.2]], [[§C6a.5 Normal Ordering and Contractions#^thm-c6a-5-1|Theorem §C6a.5.1]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-9|Theorem §C2b.6.9]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-4|Theorem §CA.3.4]], [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-6|Theorem §CA.6.6]], [[§CA.2 Generalized Functions#^thm-ca-2-6|Theorem §CA.2.6]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|Theorem §CA.3.7]]

## Diagrams with source vertices

> [!definition] Definition §C6b.7.1: Source Vertex
> In the expansion of [[§C6b.7 Particle Production by a Classical Source꞉ the Diagrammatic Route#^thm-c6b-7-1|Theorem §C6b.7.1]], each factor $i\int d^4x\,j(x)\,\hat\phi_I(x)$ is a **source vertex**, drawn as a cross: one leg, weight $i\int d^4x\,j(x)$. Lines are contractions $D_F$; a line joining two source vertices is
>
> $$
> L = \int d^4x\,d^4y\,\bigl(ij(x)\bigr)\bigl(ij(y)\bigr)\,D_F(x - y) = 2\mathcal A_2 .
> $$
>
> The order-$j^n$ term has prefactor $\frac{1}{n!} = \frac{1}{|G_n|}$, $G_n = S_n$ the permutations of the one-legged vertices ([[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-4|Theorem §CA.8.4]], 1).
>
> *Source: PHY 513, Problem Set 8, Problem 3(c) (the user's "Feynman rules": "a source vertex, drawn as a cross, with a single leg and weight $i\int d^4x\,j(x)$")*

^def-c6b-7-1

> [!theorem] Theorem §C6b.7.3: The Vacuum Series of a Source Exponentiates
> The order-$j^{2m}$ term of $\mathcal A(0)$ is one diagram, $m$ disjoint lines, with symmetry factor $S_m = 2^m\,m!$; odd orders vanish; and, to all orders in $j$,
>
> $$
> \mathcal A(0) = \sum_{m\ge0}\frac{L^m}{2^m\,m!} = \sum_{m\ge0}\frac{(\mathcal A_2)^m}{m!} = e^{\mathcal A_2}, \qquad P(0) = e^{2\operatorname{Re}\mathcal A_2} = e^{-\lambda} .
> $$
>
> *Source: PHY 513, Problem Set 8, Problem 3(c) (the user's solution) · PS Problem 4.1(c)*

^thm-c6b-7-3

> [!derivation]- Derivation
> **Step 1** (the term of (b) as a diagram). $\mathcal A_2 = \frac{1}{2!}\int d^4x_1\,d^4x_2\,(ij(x_1))(ij(x_2))\,D_F(x_1 - x_2) = \frac12L$: one line between two source vertices. $G_2 = \{e, (x_1\,x_2)\}$, $|G_2| = 2!\,(1!)^2 = 2$; the single pairing $\{x_1, x_2\}$ is mapped to itself by the exchange, so its orbit has one element and $S_1 = |G_2|/1 = 2$.
>
> **Step 2** (odd orders). $n$ one-legged vertices and no external points: for odd $n$ one leg is left over, every Wick term keeps a field and vanishes ([[§C6a.8 Position-Space Feynman Rules#^thm-c6a-8-3|Theorem §C6a.8.3]], Step 1, with source vertices).
>
> **Step 3** ($S_m$ by counting). At order $2m$, $|G| = (2m)!$. The complete pairings of $2m$ vertices: choose a first pair, a second from the rest, …,
>
> $$
> \binom{2m}{2}\binom{2m - 2}{2}\cdots\binom22 = \frac{(2m)!}{2!\,(2m - 2)!}\cdot\frac{(2m - 2)!}{2!\,(2m - 4)!}\cdots\frac{2!}{2!\,0!} = \frac{(2m)!}{2^m} ,
> $$
>
> ordered lists of $m$ pairs; each pairing (a set of pairs) is listed $m!$ times: $N = \frac{(2m)!}{2^m\,m!}$. All pairings have the same shape ($m$ disjoint lines), one orbit, so $S_m = \frac{(2m)!}{N} = 2^m\,m!$. As a stabilizer: flip each line ($2^m$) and permute the $m$ identical lines ($m!$) — part 2 of [[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-3|Theorem §CA.8.3]] with $S(\text{line}) = 2$.
>
> **Step 4** (sum). $\mathcal A_{2m} = \frac{1}{(2m)!}\int\prod d^4x_i\,(ij(x_i))\,\langle0|T\{\hat\phi_I(x_1)\cdots\hat\phi_I(x_{2m})\}|0\rangle$; by [[§C6a.6 Wick's Theorem#^thm-c6a-6-3|Theorem §C6a.6.3]] the vacuum value is the sum over the $N$ pairings of products of $m$ propagators, and after renaming the variables each gives $L^m$:
>
> $$
> \mathcal A_{2m} = \frac{N}{(2m)!}L^m = \frac{L^m}{2^m\,m!} = \frac{1}{S_m}L^m = \frac{(L/2)^m}{m!} = \frac{(\mathcal A_2)^m}{m!}, \qquad \mathcal A(0) = \sum_{m\ge0}\frac{(\mathcal A_2)^m}{m!} = e^{\mathcal A_2} .
> $$
>
> $\mathcal A_2$ is exact (the only diagram with two vertices), so this holds to all orders in $j$; it is [[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-3|Theorem §CA.8.3]] (with [[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-4|Theorem §CA.8.4]], 4, $r = 1$) for a theory whose only connected vacuum diagram is the line.
>
> **Step 5** (probability). $P(0) = |e^{\mathcal A_2}|^2 = e^{\mathcal A_2 + \mathcal A_2^{\ast}} = e^{2\operatorname{Re}\mathcal A_2} = e^{-\lambda}$ ([[§C6b.7 Particle Production by a Classical Source꞉ the Diagrammatic Route#^thm-c6b-7-2|Theorem §C6b.7.2]]); to order $j^2$, $1 - \lambda$.

^der-c6b-7-3

*Uses:* [[§C6b.7 Particle Production by a Classical Source꞉ the Diagrammatic Route#^def-c6b-7-1|Def. §C6b.7.1]], [[§C6a.6 Wick's Theorem#^thm-c6a-6-3|Theorem §C6a.6.3]], [[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-3|Theorem §CA.8.3]], [[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-4|Theorem §CA.8.4]], [[§C6b.7 Particle Production by a Classical Source꞉ the Diagrammatic Route#^thm-c6b-7-2|Theorem §C6b.7.2]]

## Outgoing particles

> [!theorem] Lemma §C6b.7.4: Contraction of Fields with Outgoing Particles
> Let $|\mathbf k_1\cdots\mathbf k_n\rangle = \hat a^\dagger_{\mathbf k_1}\cdots\hat a^\dagger_{\mathbf k_n}|0\rangle$ and $k_i^0 = E_{\mathbf k_i}$. For a normal-ordered product of $r$ free fields ([[§C6a.5 Normal Ordering and Contractions#^thm-c6a-5-1|Theorem §C6a.5.1]]),
>
> $$
> \langle\mathbf k_1\cdots\mathbf k_n|\,{:}\hat\phi_I(y_1)\cdots\hat\phi_I(y_r){:}\,|0\rangle = \delta_{rn}\sum_{\sigma\in S_n}\prod_{i=1}^n\frac{e^{ik_i\cdot y_{\sigma(i)}}}{\sqrt{2E_{\mathbf k_i}}} :
> $$
>
> each outgoing particle contracts with exactly one field, $\overbracket{\langle\mathbf k|\,\hat\phi_I(y)} \equiv [\hat a_{\mathbf k}, \hat\phi_I^-(y)] = e^{ik\cdot y}/\sqrt{2E_{\mathbf k}}$. Hence in $\langle\mathbf k_1\cdots\mathbf k_n|T\{\hat\phi_I(x_1)\cdots\hat\phi_I(x_\ell)\}|0\rangle$ only the Wick terms with exactly $n$ uncontracted fields survive. For relativistically normalized states $|\mathbf k\rangle_{\rm rel} = \sqrt{2E_{\mathbf k}}\,\hat a^\dagger_{\mathbf k}|0\rangle$ ([[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-1|Def. §C2a.4.1]]) the factors $\frac{1}{\sqrt{2E}}$ drop out: ${}_{\rm rel}\langle\mathbf k_1\cdots\mathbf k_n|{:}\hat\phi_I(y_1)\cdots\hat\phi_I(y_n){:}|0\rangle = \sum_\sigma\prod_ie^{ik_i\cdot y_{\sigma(i)}}$; for $n = 1$, $\langle\mathbf p|\hat\phi_I(x)|0\rangle = e^{ip\cdot x}$ ([[§C2b.1 Heisenberg Fields#^thm-c2b-1-5|Theorem §C2b.1.5]]).
>
> *Source: PHY 513, Problem Set 8, Problem 3(d)–(e) (the user's solution: "Only one uncontracted field survives"; "Exactly $n$ uncontracted fields survive"; the sum over $\sigma \in S_n$) and Problem 4 (relativistic form) · stated in general here, so that it can move to a section on external states*

^lem-c6b-7-4

> [!derivation]- Derivation
> **Step 1** (only $\hat\phi^-$ acts). Normal ordering puts every $\hat\phi_I^-$ ($\propto \hat a^\dagger$) left of every $\hat\phi_I^+$ ($\propto \hat a$), and $\hat\phi_I^+|0\rangle = 0$ ([[§C2b.1 Heisenberg Fields#^thm-c2b-1-5|Theorem §C2b.1.5]]): of the $2^r$ terms of ${:}\prod(\hat\phi^+ + \hat\phi^-){:}$ only one survives on $|0\rangle$,
>
> $$
> \langle0|\hat a_{\mathbf k_n}\cdots\hat a_{\mathbf k_1}\,{:}\hat\phi_I(y_1)\cdots\hat\phi_I(y_r){:}\,|0\rangle = \langle0|\hat a_{\mathbf k_n}\cdots\hat a_{\mathbf k_1}\,\hat\phi_I^-(y_1)\cdots\hat\phi_I^-(y_r)|0\rangle
> $$
>
> (the order of the $\hat a$'s is irrelevant, they commute).
>
> **Step 2** (the elementary contraction). With $[\hat a_{\mathbf k}, \hat a^\dagger_{\mathbf p}] = (2\pi)^3\delta^3(\mathbf k - \mathbf p)$,
>
> $$
> [\hat a_{\mathbf k}, \hat\phi_I^-(y)] = \int\frac{d^3p}{(2\pi)^3}\frac{e^{ip\cdot y}}{\sqrt{2E_{\mathbf p}}}(2\pi)^3\delta^3(\mathbf k - \mathbf p) = \frac{e^{ik\cdot y}}{\sqrt{2E_{\mathbf k}}}, \qquad k^0 = E_{\mathbf k},
> $$
>
> a number.
>
> **Step 3** (move one $\hat a$ through). With $X = \hat\phi_I^-(y_2)\cdots\hat\phi_I^-(y_r)$ and $\hat aB = B\hat a + [\hat a, B]$,
>
> $$
> \hat a_{\mathbf k}\,\hat\phi_I^-(y_1)X|0\rangle = \hat\phi_I^-(y_1)\,\hat a_{\mathbf k}X|0\rangle + \frac{e^{ik\cdot y_1}}{\sqrt{2E_{\mathbf k}}}\,X|0\rangle ,
> $$
>
> and repeating through $X$, $\hat a_{\mathbf k}\hat\phi_I^-(y_1)\cdots\hat\phi_I^-(y_r)|0\rangle = \sum_{l=1}^r\frac{e^{ik\cdot y_l}}{\sqrt{2E_{\mathbf k}}}\prod_{l'\ne l}\hat\phi_I^-(y_{l'})|0\rangle$ (the term with $\hat a_{\mathbf k}$ at the right end vanishes): each $\hat a$ removes one $\hat\phi^-$ in all possible ways.
>
> **Step 4** (count). Apply $\hat a_{\mathbf k_1}, \dots, \hat a_{\mathbf k_n}$ in turn. If $r < n$, an $\hat a$ meets $|0\rangle$ with no $\hat\phi^-$ left: $0$. If $r > n$, after all $\hat a$'s a $\hat\phi^- \propto \hat a^\dagger$ stands next to $\langle0|$: $0$. If $r = n$, $\hat a_{\mathbf k_1}$ picks $y_{\sigma(1)}$ ($n$ choices), $\hat a_{\mathbf k_2}$ one of the remaining ($n - 1$), …: one term per bijection $\sigma$, $n!$ terms, the stated sum. For $n = 1$: $\langle\mathbf k|\hat\phi_I^-(y)|0\rangle = e^{ik\cdot y}/\sqrt{2E_{\mathbf k}}$.
>
> **Step 5** (in Wick's theorem). $T\{\hat\phi_I(x_1)\cdots\hat\phi_I(x_\ell)\} = \sum(\text{products of }D_F)\cdot{:}\text{remaining }r\text{ fields}{:}$ ([[§C6a.6 Wick's Theorem#^thm-c6a-6-2|Theorem §C6a.6.2]]), $r = \ell, \ell - 2, \dots$; by Step 4 only $r = n$ survives between $\langle\mathbf k_1\cdots\mathbf k_n|$ and $|0\rangle$. Relativistic normalization multiplies by $\prod_i\sqrt{2E_{\mathbf k_i}}$.

^der-c6b-7-4

*Uses:* [[§C2b.1 Heisenberg Fields#^thm-c2b-1-5|Theorem §C2b.1.5]], [[§C6a.5 Normal Ordering and Contractions#^thm-c6a-5-1|Theorem §C6a.5.1]], [[§C6a.6 Wick's Theorem#^thm-c6a-6-2|Theorem §C6a.6.2]], [[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-1|Def. §C2a.4.1]]

> [!caution] Caution: Two normalizations of one-particle states
> Problem Set 8 uses both. Problem 3 (PS 4.1) takes $|\mathbf k\rangle = \hat a^\dagger_{\mathbf k}|0\rangle$, with
>
> $$
> \langle\mathbf p|\mathbf k\rangle = (2\pi)^3\delta^3(\mathbf p - \mathbf k), \qquad \mathbb 1_1 = \int\frac{d^3k}{(2\pi)^3}|\mathbf k\rangle\langle\mathbf k|, \qquad \langle\mathbf k|\hat\phi_I(x)|0\rangle = \frac{e^{ik\cdot x}}{\sqrt{2E_{\mathbf k}}} ;
> $$
>
> Problem 4 and the decay and cross-section formulas take $|\mathbf k\rangle = \sqrt{2E_{\mathbf k}}\,\hat a^\dagger_{\mathbf k}|0\rangle$ ([[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-1|Def. §C2a.4.1]]), with $\langle\mathbf p|\mathbf k\rangle = 2E_{\mathbf k}(2\pi)^3\delta^3(\mathbf p - \mathbf k)$, $\mathbb 1_1 = \int\frac{d^3k}{(2\pi)^32E_{\mathbf k}}|\mathbf k\rangle\langle\mathbf k|$ ([[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-2|Def. §C2a.4.2]]) and $\langle\mathbf k|\hat\phi_I(x)|0\rangle = e^{ik\cdot x}$. The amplitudes differ by $\sqrt{2E}$ per particle and the measures by $\frac{1}{2E}$ per particle; probabilities, integrated with the matching measure, agree. Mixing the two (a relativistic amplitude with $\frac{d^3k}{(2\pi)^3}$) gives a wrong factor $2E$ per particle.
>
> *Source: PHY 513, Problem Set 8, Problems 3(d) and 4 (the user's solution: "To use the decay rate of Lecture 15, the states are taken relativistically normalized") · [[Larsen PHY 513]] (register row)*

^cau-c6b-7-1

> [!theorem] Theorem §C6b.7.5: The One-Particle Amplitude
> For one particle of momentum $\mathbf k$, $k^0 = E_{\mathbf k}$,
>
> $$
> \mathcal A(\mathbf k) = \langle\mathbf k|\,T\Bigl\{\exp\Bigl[i\int d^4x\,j\hat\phi_I\Bigr]\Bigr\}|0\rangle = \frac{i\,\tilde j(k)}{\sqrt{2E_{\mathbf k}}}\,e^{\mathcal A_2}, \qquad dP(1) = \frac{d^3k}{(2\pi)^3}\,\frac{|\tilde j(k)|^2}{2E_{\mathbf k}}\,e^{-\lambda}, \qquad P(1) = \lambda\,e^{-\lambda} ;
> $$
>
> to leading order $\mathcal A(\mathbf k) = i\tilde j(k)/\sqrt{2E_{\mathbf k}} + O(j^3)$ and $|\mathcal A(\mathbf k)|^2 = |\tilde j(k)|^2/2E_{\mathbf k} + O(j^4)$.
>
> *Source: PHY 513, Problem Set 8, Problem 3(d) (the user's solution) · PS Problem 4.1(d)*

^thm-c6b-7-5

> [!derivation]- Derivation
> **Step 1** (only one uncontracted field). By [[§C6b.7 Particle Production by a Classical Source꞉ the Diagrammatic Route#^thm-c6b-7-1|Theorem §C6b.7.1]] the amplitude is the stated matrix element; its order-$j^\ell$ term is $\frac{1}{\ell!}\int\prod d^4x_i\,(ij(x_i))\,\langle\mathbf k|T\{\hat\phi_I(x_1)\cdots\hat\phi_I(x_\ell)\}|0\rangle$, and by [[§C6b.7 Particle Production by a Classical Source꞉ the Diagrammatic Route#^lem-c6b-7-4|Lemma §C6b.7.4]] ($n = 1$) only the Wick terms with one uncontracted field survive, that field giving $e^{ik\cdot x_i}/\sqrt{2E_{\mathbf k}}$. Even $\ell$: no such term, $\mathcal A_{2m}(\mathbf k) = 0$ (in particular $\langle\mathbf k|0\rangle = 0$).
>
> **Step 2** (leading order). $\ell = 1$: $\mathcal A_1(\mathbf k) = i\int d^4x\,j(x)\frac{e^{ik\cdot x}}{\sqrt{2E_{\mathbf k}}} = \frac{i\tilde j(k)}{\sqrt{2E_{\mathbf k}}}$; the cross term with the $O(j^3)$ correction is $O(j^4)$, so $|\mathcal A(\mathbf k)|^2 = \frac{|\tilde j(k)|^2}{2E_{\mathbf k}} + O(j^4)$.
>
> **Step 3** (all orders, count). At $\ell = 2m + 1$ the uncontracted field is one of $2m + 1$, the rest are paired in $\frac{(2m)!}{2^m\,m!}$ ways ([[§C6b.7 Particle Production by a Classical Source꞉ the Diagrammatic Route#^der-c6b-7-3|Derivation §C6b.7.3]], Step 3): $(2m + 1)\frac{(2m)!}{2^m\,m!} = \frac{(2m + 1)!}{2^m\,m!}$ terms; after renaming the variables each is the external line times $m$ vacuum lines, $\frac{i\tilde j(k)}{\sqrt{2E_{\mathbf k}}}\,L^m$ (Def §C6b.7.1). So
>
> $$
> \mathcal A_{2m+1}(\mathbf k) = \frac{1}{(2m + 1)!}\cdot\frac{(2m + 1)!}{2^m\,m!}\cdot\frac{i\tilde j(k)}{\sqrt{2E_{\mathbf k}}}L^m = \frac{i\tilde j(k)}{\sqrt{2E_{\mathbf k}}}\,\frac{(\mathcal A_2)^m}{m!}, \qquad \mathcal A(\mathbf k) = \frac{i\tilde j(k)}{\sqrt{2E_{\mathbf k}}}\,e^{\mathcal A_2} :
> $$
>
> the external line times the vacuum series of [[§C6b.7 Particle Production by a Classical Source꞉ the Diagrammatic Route#^thm-c6b-7-3|Theorem §C6b.7.3]], with symmetry factor $2^m\,m!$ (the external line, its momentum labelled, can be neither flipped nor exchanged).
>
> **Step 4** (probability). $|e^{\mathcal A_2}|^2 = e^{-\lambda}$, and the one-particle measure is $\frac{d^3k}{(2\pi)^3}$ (applying $\int\mu\,d^3k\,|\mathbf k\rangle\langle\mathbf k|$ to $|\mathbf p\rangle$ gives $\mu(2\pi)^3|\mathbf p\rangle$, so $\mu = (2\pi)^{-3}$; [[§C6b.7 Particle Production by a Classical Source꞉ the Diagrammatic Route#^thm-c6b-7-6|Theorem §C6b.7.6]], $n = 1$). Integrating, $P(1) = e^{-\lambda}\int\frac{d^3k}{(2\pi)^3}\frac{|\tilde j(k)|^2}{2E_{\mathbf k}} = \lambda e^{-\lambda}$.

^der-c6b-7-5

*Uses:* [[§C6b.7 Particle Production by a Classical Source꞉ the Diagrammatic Route#^thm-c6b-7-1|Theorem §C6b.7.1]], [[§C6b.7 Particle Production by a Classical Source꞉ the Diagrammatic Route#^lem-c6b-7-4|Lemma §C6b.7.4]], [[§C6b.7 Particle Production by a Classical Source꞉ the Diagrammatic Route#^thm-c6b-7-3|Theorem §C6b.7.3]], [[§C6b.7 Particle Production by a Classical Source꞉ the Diagrammatic Route#^thm-c6b-7-6|Theorem §C6b.7.6]]

> [!theorem] Theorem §C6b.7.6: The Measure on n-Particle States
> On the $n$-particle states $|\mathbf k_1\cdots\mathbf k_n\rangle = \hat a^\dagger_{\mathbf k_1}\cdots\hat a^\dagger_{\mathbf k_n}|0\rangle$,
>
> $$
> \langle\mathbf k_1\cdots\mathbf k_n|\mathbf p_1\cdots\mathbf p_n\rangle = \sum_{\sigma\in S_n}\prod_{i=1}^n(2\pi)^3\delta^3(\mathbf k_i - \mathbf p_{\sigma(i)}), \qquad \mathbb 1_n = \frac{1}{n!}\int\prod_{i=1}^n\frac{d^3k_i}{(2\pi)^3}\,|\mathbf k_1\cdots\mathbf k_n\rangle\langle\mathbf k_1\cdots\mathbf k_n| :
> $$
>
> integrating each momentum independently counts each state $n!$ times. With relativistic normalization the same holds with $\frac{d^3k_i}{(2\pi)^32E_{\mathbf k_i}}$; this is the $\frac{1}{S_{\rm id}}$ of identical particles ([[§C6b.3 Evaluating the Cross Section#^thm-c6b-3-4|Theorem §C6b.3.4]], whose derivation, Step 2, is the same computation).
>
> *Source: PHY 513, Problem Set 8, Problem 3(e) (the user's solution, paragraph "Measure") and Problem 4 ("as for the $\frac{1}{n!}$ in Problem 3(e), the total rate carries a factor $\frac{1}{2!}$")*

^thm-c6b-7-6

> [!derivation]- Derivation
> **Step 1** (overlap). The $\hat a^\dagger$'s commute, so $|\mathbf k_1\cdots\mathbf k_n\rangle$ is symmetric. $\langle\mathbf k_1\cdots\mathbf k_n|\mathbf p_1\cdots\mathbf p_n\rangle = \langle0|\hat a_{\mathbf k_1}\cdots\hat a_{\mathbf k_n}\hat a^\dagger_{\mathbf p_1}\cdots\hat a^\dagger_{\mathbf p_n}|0\rangle$ is Step 4 of [[§C6b.7 Particle Production by a Classical Source꞉ the Diagrammatic Route#^der-c6b-7-4|Derivation §C6b.7.4]] with $\hat a^\dagger_{\mathbf p}$ for $\hat\phi^-$ and $[\hat a_{\mathbf k}, \hat a^\dagger_{\mathbf p}] = (2\pi)^3\delta^3(\mathbf k - \mathbf p)$: the stated sum.
>
> **Step 2** (resolution of the identity). Let $\mu_n\int\prod d^3k_i\,|\mathbf k_1\cdots\rangle\langle\mathbf k_1\cdots|$ act on $|\mathbf p_1\cdots\mathbf p_n\rangle$; each delta does one integral, and every permuted state equals $|\mathbf p_1\cdots\mathbf p_n\rangle$:
>
> $$
> \mu_n(2\pi)^{3n}\sum_{\sigma\in S_n}|\mathbf p_{\sigma(1)}\cdots\mathbf p_{\sigma(n)}\rangle = \mu_n(2\pi)^{3n}\,n!\,|\mathbf p_1\cdots\mathbf p_n\rangle ,
> $$
>
> the identity iff $\mu_n = \frac{1}{n!\,(2\pi)^{3n}}$. With relativistic normalization every delta carries $2E$, cancelled by $\frac{1}{2E}$ in the measure.

^der-c6b-7-6

*Uses:* [[§C6b.7 Particle Production by a Classical Source꞉ the Diagrammatic Route#^der-c6b-7-4|Derivation §C6b.7.4]], [[§C6b.3 Evaluating the Cross Section#^thm-c6b-3-4|Theorem §C6b.3.4]]

> [!theorem] Theorem §C6b.7.7: The Number of Particles Is Poisson Distributed
> $$
> \mathcal A(\mathbf k_1, \dots, \mathbf k_n) = \prod_{i=1}^n\frac{i\,\tilde j(k_i)}{\sqrt{2E_{\mathbf k_i}}}\;e^{\mathcal A_2}, \qquad P(n) = \frac{1}{n!}\int\prod_i\frac{d^3k_i}{(2\pi)^3}\,|\mathcal A(\mathbf k_1, \dots, \mathbf k_n)|^2 = \frac{\lambda^n}{n!}\,e^{-\lambda} .
> $$
>
> *Source: PHY 513, Problem Set 8, Problem 3(e) (the user's solution) · PS Problem 4.1(e)*

^thm-c6b-7-7

> [!derivation]- Derivation
> **Step 1** (surviving terms). At order $\ell$, by [[§C6b.7 Particle Production by a Classical Source꞉ the Diagrammatic Route#^lem-c6b-7-4|Lemma §C6b.7.4]] exactly $n$ fields are uncontracted, so $\ell = n + 2m$ (other orders vanish). Choose them ($\binom\ell n$), match them to the particles ($n!$, the sum over $\sigma$), pair the rest ($\frac{(2m)!}{2^m\,m!}$):
>
> $$
> \binom{\ell}{n}\,n!\,\frac{(2m)!}{2^m\,m!} = \frac{\ell!}{(2m)!}\cdot\frac{(2m)!}{2^m\,m!} = \frac{\ell!}{2^m\,m!}
> $$
>
> terms, each, after renaming, $\prod_i\frac{i\tilde j(k_i)}{\sqrt{2E_{\mathbf k_i}}}\cdot L^m$.
>
> **Step 2** (sum). With the $\frac{1}{\ell!}$ of the expansion, $\mathcal A_{n+2m} = \prod_i\frac{i\tilde j(k_i)}{\sqrt{2E_{\mathbf k_i}}}\frac{(\mathcal A_2)^m}{m!}$, and $\sum_m$ gives the amplitude; $n = 0, 1$ are Theorems §C6b.7.3 and §C6b.7.5. In diagrams: $n$ external lines and $m$ vacuum lines, $S = 2^m\,m!$ (labelled outgoing momenta are never relabelled).
>
> **Step 3** (probability). $|\mathcal A|^2 = \prod_i\frac{|\tilde j(k_i)|^2}{2E_{\mathbf k_i}}e^{-\lambda}$, and with the measure of [[§C6b.7 Particle Production by a Classical Source꞉ the Diagrammatic Route#^thm-c6b-7-6|Theorem §C6b.7.6]] each factor integrates to $\lambda$: $P(n) = \frac{e^{-\lambda}}{n!}\lambda^n$.

^der-c6b-7-7

*Uses:* [[§C6b.7 Particle Production by a Classical Source꞉ the Diagrammatic Route#^lem-c6b-7-4|Lemma §C6b.7.4]], [[§C6b.7 Particle Production by a Classical Source꞉ the Diagrammatic Route#^thm-c6b-7-3|Theorem §C6b.7.3]], [[§C6b.7 Particle Production by a Classical Source꞉ the Diagrammatic Route#^thm-c6b-7-5|Theorem §C6b.7.5]], [[§C6b.7 Particle Production by a Classical Source꞉ the Diagrammatic Route#^thm-c6b-7-6|Theorem §C6b.7.6]]

> [!theorem] Theorem §C6b.7.8: Normalization, Mean and Variance
> $$
> \sum_{n\ge0}P(n) = 1, \qquad \bar N = \sum_nn\,P(n) = \lambda, \qquad \langle(N - \bar N)^2\rangle = \lambda .
> $$
>
> *Source: PHY 513, Problem Set 8, Problem 3(f) (the user's solution) · PS Problem 4.1(f)*

^thm-c6b-7-8

> [!derivation]- Derivation
> **Step 1** (normalization). $\sum_nP(n) = e^{-\lambda}\sum_n\frac{\lambda^n}{n!} = e^{-\lambda}e^\lambda = 1$.
>
> **Step 2** (mean). The $n = 0$ term vanishes and $\frac{n}{n!} = \frac{1}{(n-1)!}$; shifting $n \to n + 1$: $\bar N = e^{-\lambda}\sum_{n\ge1}\frac{\lambda^n}{(n-1)!} = \lambda e^{-\lambda}\sum_{n\ge0}\frac{\lambda^n}{n!} = \lambda$.
>
> **Step 3** (second moment). With $n = (n - 1) + 1$ and shifts by 2 and 1 (the $n = 1$ term of the first sum vanishes):
>
> $$
> \sum_{n\ge0}\frac{n^2\lambda^n}{n!} = \sum_{n\ge1}\frac{(n - 1)\lambda^n}{(n - 1)!} + \sum_{n\ge1}\frac{\lambda^n}{(n - 1)!} = \sum_{n\ge0}\frac{\lambda^{n+2}}{n!} + \sum_{n\ge0}\frac{\lambda^{n+1}}{n!} = (\lambda^2 + \lambda)e^\lambda ,
> $$
>
> so $\langle N^2\rangle = \lambda^2 + \lambda$ and $\langle(N - \bar N)^2\rangle = \langle N^2\rangle - 2\bar N\langle N\rangle + \bar N^2 = \langle N^2\rangle - \bar N^2 = \lambda$.

^der-c6b-7-8

> [!remark] Remark: Two routes, one answer
> The coherent-state route of [[§C2b.8 Particle Production by a Classical Source|§C2b.8]] (Heisenberg picture, retarded function) gives the final state $\prod_{\mathbf p}$-coherent with $\eta_{\mathbf p} = i\tilde j(E_{\mathbf p}, \mathbf p)$ ([[§C2b.8 Particle Production by a Classical Source#^thm-c2b-8-2|Theorem §C2b.8.2]]) and Poisson statistics with mean $\bar N$ ([[§C2b.8 Particle Production by a Classical Source#^thm-c2b-8-3|Theorem §C2b.8.3]], [[§C2a.6 Coherent States and the Classical Field#^thm-c2a-6-6|Theorem §C2a.6.6]]); the diagrammatic route here gives $\mathcal A(\mathbf k_1, \dots) = \prod_i\frac{i\tilde j(k_i)}{\sqrt{2E_{\mathbf k_i}}}e^{\mathcal A_2}$, which is the expansion of that coherent state in $\hat a^\dagger|0\rangle$ states up to the phase $e^{i\operatorname{Im}\mathcal A_2}$, with $\lambda = \bar N$. The diagrammatic route is the one that generalizes to interactions that are not linear in the field.
>
> *Source: PS §2.4 and Problem 4.1 · [[§C6a.2 The Interaction Picture|§C6a.2]], Connections*

^rem-c6b-7-1

> [!remark]- Connections
> - The vacuum series exponentiates by the same exponential formula as the vacuum bubbles of $\phi^4$ theory; here the only connected vacuum diagram is the line, so the whole series is $e^{L/2}$ — [[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-3|Theorem §CA.8.3]], [[§C6a.11 The iε Limit and Vacuum Bubbles#^thm-c6a-11-6|Theorem §C6a.11.6]].
> - $P(0) = e^{-\lambda}$ is the vacuum-persistence probability; at order $j^2$, $1 - P(0) = \lambda = P(1)$: the probability lost from the vacuum is the probability of emitting one particle, carried by the $\delta(p^2 - m^2)$ part of $D_F$ — [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-6|Theorem §CA.6.6]] (the $\delta(p^2 - m^2)$ part of $D_F$).
> - The contraction of a field with an outgoing particle is the external-line rule of amplitudes: in relativistic normalization each external scalar line gives $e^{ip\cdot x}$, i.e. factor 1 after the vertex integral, as in the decay $\Phi \to \phi\phi$ — [[§C6b.5 Decay Rates and Widths#^ex-c6b-5-1|Example §C6b.5.1]], [[§C6b.6 Amplitudes from Correlation Functions#^thm-c6b-6-1|Theorem §C6b.6.1]].
> - The $n!$ of the $n$-particle measure and the identical-particle factor $S_{\rm id}$ are one fact, the symmetry of bosonic states — [[§C6b.3 Evaluating the Cross Section#^thm-c6b-3-4|Theorem §C6b.3.4]], [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-2|Theorem §C2a.4.2]].
> - The same computation with $j$ a classical current and $\hat\phi$ the photon field gives the Poisson distribution of soft photons emitted by a classical charge (PS Problem 4.1's remark; bremsstrahlung, QFT C8, planned) — [[§C2b.8 Particle Production by a Classical Source|§C2b.8]], Connections.
