---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C6c
section: C6c.8
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C6c.7 Particle Production by a Classical Source꞉ the Diagrammatic Route]] · ↑ [[· C6c Feynman Rules for Amplitudes]] · [[§C6c.9 The Linear Sigma Model꞉ the Broken Phase]] →

*Sources: PHY 513, Problem Set 10 ("Scattering Processes"), Problem 1(a1)–(a3) (statement, Larsen; the user's solution, 2026-11-13) · Peskin & Schroeder, An Introduction to Quantum Field Theory, Problem 4.3(a), pp. 127–128 (page images checked); §4.5, eqs. (4.84)–(4.85) · the homes cited in each box.*

[[§C6c.6 Feynman Rules for Amplitudes|§C6c.6]] collected the rules for $i\mathcal M$ and applied them to one field ($\phi^4$, the cubic–quartic theory) and to three different fields with one vertex of distinct legs ([[§C6c.6 Feynman Rules for Amplitudes#^mod-c6c-6-5|Model §C6c.6.5]]). The linear sigma model of Problem Set 10 has $N$ real fields $\Phi^i$ of one mass, rotated into each other by a symmetry, and one quartic interaction $\frac\lambda4(\Phi^i\Phi^i)^2$. Three things are new:
1. **the fields carry an index**: propagators and vertices become functions of the indices of the lines that meet, $\delta^{ij}D_F$ and $V^{ijkl}$ ([[§C6c.8 The Linear Sigma Model꞉ Fields with an Internal Index#^thm-c6c-8-2|Theorem §C6c.8.2]], [[§C6c.8 The Linear Sigma Model꞉ Fields with an Internal Index#^thm-c6c-8-3|Theorem §C6c.8.3]]);
2. **the vertex is read off by differentiating the interaction potential**, the hint of the problem, which is the counting rule of [[§C6a.14 Feynman Rules for Polynomial Interactions#^thm-c6a-14-2|Theorem §C6a.14.2]] in index form ([[§C6c.8 The Linear Sigma Model꞉ Fields with an Internal Index#^thm-c6c-8-4|Theorem §C6c.8.4]]);
3. **identical and distinguishable final particles occur in one model**: the same vertex function gives three different total cross sections ([[§C6c.8 The Linear Sigma Model꞉ Fields with an Internal Index#^ex-c6c-8-2|Example §C6c.8.2]], [[§C6c.8 The Linear Sigma Model꞉ Fields with an Internal Index#^thm-c6c-8-5|Theorem §C6c.8.5]]).

This section takes $m^2 > 0$ (Problem 1(a)); $m^2 < 0$ is [[§C6c.9 The Linear Sigma Model꞉ the Broken Phase|§C6c.9]], and the model with the symmetry broken by a linear term is [[§C6c.10 The Linear Sigma Model꞉ Explicit Symmetry Breaking|§C6c.10]].

**Setup and scope.** An instance of [[§C6a.0 Setups and Observables#^mod-c6a-0-3|Model §C6a.0.3]]: a permanent interaction, free relativistic states $|p, i\rangle = \sqrt{2E_{\mathbf p}}\,\hat a^{i\dagger}_{\mathbf p}|0\rangle$ over the free vacuum $|0\rangle$ standing for the in and out states ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^pr-c6b-1-3|Principle §C6b.1.3]]), everything at the lowest order in $\lambda$, where the rules of [[§C6c.6 Feynman Rules for Amplitudes#^thm-c6c-6-2|Theorem §C6c.6.2]] are the amplitude. *Conventions* ([[Larsen PHY 513]]): $g = \operatorname{diag}(+,-,-,-)$, $\hbar = c = 1$; the index $i = 1, \dots, N$ is written upstairs, repeated indices are summed, and its position has no meaning (the metric of the index space is $\delta^{ij}$); a particle created by $\hat\Phi^i$ is "of type $i$"; $\hat S = \mathbb 1 + i\hat T$ and $\langle f|i\hat T|i\rangle = (2\pi)^4\delta^4(\sum p_{\rm in} - \sum p_{\rm out})\,i\mathcal M$ ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-3|Def. §C6b.1.3]]); the centre-of-mass energy is $E_{\rm cm}$ ([[§C6b.3 The Cross Section#^def-c6b-3-6|Def. §C6b.3.6]]; $E_{\rm cms}$ in the problem set).

## The model

> [!model] Model §C6c.8.1: The O(N) Linear Sigma Model
> $N$ real scalar fields $\Phi^i$, $i = 1, \dots, N$, with
>
> $$
> \mathcal L = \frac12\,\partial_\mu\Phi^i\,\partial^\mu\Phi^i - \frac12\,m^2\,\Phi^i\Phi^i - \frac\lambda4\bigl(\Phi^i\Phi^i\bigr)^2 , \qquad \lambda > 0 ,
> $$
>
> repeated indices summed; $\lambda$ is dimensionless, as the coupling of $\phi^4$ theory ([[§C6a.1 From Free to Interacting Fields#^thm-c6a-1-2|Theorem §C6a.1.2]]).
> 1. *Symmetry.* $\mathcal L$ is invariant under $\Phi^i \to R^{ij}\Phi^j$ for every constant $N \times N$ orthogonal matrix $R$, $R^{ij}R^{ik} = \delta^{jk}$, that is, under the group $O(N)$ ([[§11 Topological Groups and Classical Matrix Groups#^def-11-7|591 Def. §11.7]]): $\mathcal L$ contains the fields only in the dot products $\Phi^i\Phi^i$ and $\partial_\mu\Phi^i\,\partial^\mu\Phi^i$, and $R^{ij}\Phi^j\,R^{ik}\Phi^k = \delta^{jk}\Phi^j\Phi^k = \Phi^j\Phi^j$ (the same with $\partial_\mu\Phi$, since $R$ does not depend on $x$). The symmetry acts on the index, not on spacetime: an internal symmetry ([[§C1b.6 Conserved Charges and Internal Symmetries|§C1b.6]]; for $N = 2$ the rotation of [[§C1b.6 Conserved Charges and Internal Symmetries#^ex-c1b-6-2|Example §C1b.6.2]]).
> 2. *The free theory.* For $\lambda = 0$, $\mathcal L$ is a sum of $N$ independent real Klein–Gordon Lagrangians with the same mass $m$ ([[§C2a.1 Canonical Quantization of Fields#^mod-c2a-1-1|Model §C2a.1.1]] for each $i$); the state space is the product of $N$ scalar Fock spaces over one free vacuum $|0\rangle$.
> 3. *The interaction.* $\mathcal L_{\rm int} = -\frac\lambda4(\Phi^i\Phi^i)^2$ has no derivatives, so the conjugate momenta are those of the free theory and $\hat{\mathcal H}_I = -\mathcal L_{\rm int} = \frac\lambda4\bigl(\hat\Phi^m\hat\Phi^m\bigr)^2$, as for $\phi^4$ ([[§C6a.1 From Free to Interacting Fields#^thm-c6a-1-4|Theorem §C6a.1.4]], [[§C6a.1 From Free to Interacting Fields#^thm-c6a-1-5|Theorem §C6a.1.5]]). The **interaction potential** is $V_{\rm int}(\Phi) = \frac\lambda4(\Phi^i\Phi^i)^2$, $\mathcal L_{\rm int} = -V_{\rm int}$.
>
> *Assumptions:* in this section $m^2 > 0$, so that $\Phi = 0$ is the minimum of the potential and the quadratic term is a mass term; for $m^2 < 0$ see [[§C6c.9 The Linear Sigma Model꞉ the Broken Phase#^thm-c6c-9-1|Theorem §C6c.9.1]].
>
> *Model:* [[§C6a.0 Setups and Observables#^mod-c6a-0-3|Model §C6a.0.3]] with $N$ fields; *applies:* the theory itself; its $S$-matrix by the rules of [[§C6c.6 Feynman Rules for Amplitudes#^thm-c6c-6-3|Theorem §C6c.6.3]] with the lines and the vertex of this section, at lowest order exactly.
>
> *Source: PHY 513, Problem Set 10, Problem 1 (statement, Larsen: "The linear sigma model is a theory of $N$ real scalar fields $\Phi^i$ … The Lagrangian is invariant under $\Phi^i \to R^{ij}\Phi^j$ for any $N \times N$ orthogonal matrix $R$") · PS Problem 4.3, p. 127 (the Hamiltonian $H = \int d^3x\,\bigl(\frac12(\Pi^i)^2 + \frac12(\nabla\Phi^i)^2 + V(\Phi^2)\bigr)$ with $V(\Phi^2) = \frac12m^2(\Phi^i)^2 + \frac\lambda4((\Phi^i)^2)^2$, "a function symmetric under rotations of $\boldsymbol\Phi$") · items 1–3 written here*

^mod-c6c-8-1

> [!caution] Caution: The normalization of the quartic term
> For $N = 1$ the interaction of [[§C6c.8 The Linear Sigma Model꞉ Fields with an Internal Index#^mod-c6c-8-1|Model §C6c.8.1]] is $\frac\lambda4\Phi^4$, not the lecture's $\frac{\lambda}{4!}\phi^4$ ([[§C6a.1 From Free to Interacting Fields#^mod-c6a-1-1|Model §C6a.1.1]]). The $4!$ attachments of four lines to four equal legs are then not cancelled ([[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-4|Theorem §C6c.4.4]], 2): the one-field vertex is $-i\frac\lambda4\cdot4! = -6i\lambda$, not $-i\lambda$. The two normalizations are related by $\lambda_{\rm lecture} = 6\lambda$; every formula of $\phi^4$ theory carries over with this replacement (check: $\sigma = \lambda_{\rm lecture}^2/32\pi E_{\rm cm}^2$ of [[§C6c.11 From the Question to the Formula#^ex-c6c-11-3|Example §C6c.11.3]] becomes $36\lambda^2/32\pi E_{\rm cm}^2 = 9\lambda^2/8\pi E_{\rm cm}^2$, the last line of [[§C6c.8 The Linear Sigma Model꞉ Fields with an Internal Index#^ex-c6c-8-2|Example §C6c.8.2]]).
>
> *Source: PHY 513, Problem Set 10, Problem 1 (statement: "Note the normalization of the quartic term: for $N = 1$ it is $\frac\lambda4\Phi^4$, not the $\frac{\lambda}{4!}\phi^4$ used in lecture"; (a2): "Check that your result reduces to $-6i\lambda$ when all four indices are equal") · the comparison with Example §C6c.11.3 written here*

^cau-c6c-8-1

## The propagator

> [!theorem] Theorem §C6c.8.2: The Propagator Is Diagonal in the Index
> In the free theory of [[§C6c.8 The Linear Sigma Model꞉ Fields with an Internal Index#^mod-c6c-8-1|Model §C6c.8.1]] ($\lambda = 0$, $m^2 > 0$),
>
> $$
> \langle0|T\,\hat\Phi^i(x)\hat\Phi^j(y)|0\rangle = \delta^{ij}\,D_F(x - y) = \delta^{ij}\int\frac{d^4p}{(2\pi)^4}\,\frac{i}{p^2 - m^2 + i\varepsilon}\,e^{-ip\cdot(x - y)} ,
> $$
>
> $D_F$ the Feynman propagator of one real scalar field of mass $m$ ([[§C2b.7 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-7-2|Theorem §C2b.7.2]], [[§C2b.7 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-7-10|Theorem §C2b.7.10]]). So a line keeps its index from one end to the other: in momentum space an internal line with indices $i$, $j$ at its ends is $\delta^{ij}\dfrac{i}{p^2 - m^2 + i\varepsilon}$. This is [[§C6a.14 Feynman Rules for Polynomial Interactions#^lem-c6a-14-1|Lemma §C6a.14.1]], 1, for $N$ fields of equal mass.
>
> *Model:* [[§C6c.8 The Linear Sigma Model꞉ Fields with an Internal Index#^mod-c6c-8-1|Model §C6c.8.1]] at $\lambda = 0$ (the free fields, [[§C2a.1 Canonical Quantization of Fields#^mod-c2a-1-1|Model §C2a.1.1]] for each $i$); *applies:* free vacuum $|0\rangle$, exact; in the interacting theory it is the contraction of two interaction-picture fields, the line of every diagram.
>
> *Source: PHY 513, Problem Set 10, Problem 1(a1) (the user's solution) · PS Problem 4.3(a), p. 128 (the contraction of $\Phi^i(x)$ with $\Phi^j(y)$ is $\delta^{ij}D_F(x - y)$)*

^thm-c6c-8-2

> [!derivation]- Derivation
> **Step 1** (the free Lagrangian). For $\lambda = 0$ the Lagrangian is a sum of $N$ independent real Klein–Gordon Lagrangians with the same mass $m$,
>
> $$
> \mathcal L_0 = \sum_{i=1}^N\Bigl(\frac12\,\partial_\mu\hat\Phi^i\,\partial^\mu\hat\Phi^i - \frac12\,m^2\,\hat\Phi^i\hat\Phi^i\Bigr) .
> $$
>
> **Step 2** (mode expansions). So each $\hat\Phi^i$ has the mode expansion of a real scalar field ([[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-2|Theorem §C2a.2.2]]), with its own oscillators:
>
> $$
> \hat\Phi^i(x) = \int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}\Bigl(\hat a^i_{\mathbf p}\,e^{-ip\cdot x} + \hat a^{i\dagger}_{\mathbf p}\,e^{ip\cdot x}\Bigr) , \qquad E_{\mathbf p} = \sqrt{|\mathbf p|^2 + m^2} .
> $$
>
> **Step 3** (the mode algebra). The fields are independent, so the oscillators of different fields commute ([[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|Theorem §C2a.2.6]] for each field):
>
> $$
> [\hat a^i_{\mathbf p}, \hat a^{j\dagger}_{\mathbf q}] = (2\pi)^3\,\delta^3(\mathbf p - \mathbf q)\,\delta^{ij} .
> $$
>
> **Step 4** ($i \ne j$). The only term of $\langle0|\hat\Phi^i(x)\hat\Phi^j(y)|0\rangle$ not annihilated by the vacuum is $\langle0|\hat a^i_{\mathbf p}\,\hat a^{j\dagger}_{\mathbf q}|0\rangle$ (the other three contain $\hat a_{\mathbf q}|0\rangle = 0$ or $\langle0|\hat a^\dagger_{\mathbf p} = 0$). Since the two operators commute, $\hat a^{j\dagger}_{\mathbf q}$ can be moved to the left, where $\langle0|\hat a^{j\dagger}_{\mathbf q} = 0$:
>
> $$
> \langle0|\hat a^i_{\mathbf p}\,\hat a^{j\dagger}_{\mathbf q}|0\rangle = \langle0|\hat a^{j\dagger}_{\mathbf q}\,\hat a^i_{\mathbf p}|0\rangle = 0 \qquad (i \ne j) .
> $$
>
> The same holds for the other ordering, $\langle0|\hat\Phi^j(y)\hat\Phi^i(x)|0\rangle = 0$, so the time-ordered product vanishes.
>
> **Step 5** ($i = j$). It is the propagator of a single real scalar field of mass $m$ ([[§C2b.7 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-7-2|Theorem §C2b.7.2]]; Fourier form [[§C2b.7 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-7-10|Theorem §C2b.7.10]]). Steps 4 and 5 together are the statement.
>
> **What the derivation shows.**
> - The $\delta^{ij}$ is the $\delta^{ij}$ of the mode algebra: a particle of type $i$ is created and absorbed only by $\hat\Phi^i$. The same fact decides which external particle a field can contract with (Step 3 of [[§C6c.8 The Linear Sigma Model꞉ Fields with an Internal Index#^der-c6c-8-3|Derivation §C6c.8.3]]).
> - The equal masses were not used for the $\delta^{ij}$; they make the function multiplying it the same for every $i$, as the $O(N)$ symmetry requires.

^der-c6c-8-2

*Uses:* [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-2|Theorem §C2a.2.2]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|Theorem §C2a.2.6]], [[§C2b.7 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-7-2|Theorem §C2b.7.2]], [[§C2b.7 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-7-10|Theorem §C2b.7.10]], [[§C6a.14 Feynman Rules for Polynomial Interactions#^lem-c6a-14-1|Lemma §C6a.14.1]]

## The vertex

> [!theorem] Theorem §C6c.8.3: The Four-Point Vertex with Indices
> In [[§C6c.8 The Linear Sigma Model꞉ Fields with an Internal Index#^mod-c6c-8-1|Model §C6c.8.1]] there is one vertex, with four legs. For external lines with indices $i, j, k, l$ (incoming or outgoing alike) its factor is
>
> $$
> V^{ijkl} = -2i\lambda\,\bigl(\delta^{ij}\delta^{kl} + \delta^{ik}\delta^{jl} + \delta^{il}\delta^{jk}\bigr) ,
> $$
>
> one term for each of the three ways of splitting the four lines into two pairs of equal index. In cases:
> 1. four lines of the same field: all three terms are $1$, $V^{iiii} = -6i\lambda$ (no sum);
> 2. two lines of one field and two of another: exactly one term is $1$, $-2i\lambda$;
> 3. any other pattern (three lines of one field and one of another, or more than two fields): $0$, since no term of the interaction has that field content.
>
> In position space the vertex carries $\int d^4z$, in momentum space $(2\pi)^4\delta^4(\sum p)$, as every vertex ([[§C6a.14 Feynman Rules for Polynomial Interactions#^thm-c6a-14-2|Theorem §C6a.14.2]]).
>
> *Model:* [[§C6c.8 The Linear Sigma Model꞉ Fields with an Internal Index#^mod-c6c-8-1|Model §C6c.8.1]]; *applies:* every order (the factor of the vertex in any diagram, with $\frac1S$ for the diagram: [[§C6a.14 Feynman Rules for Polynomial Interactions#^thm-c6a-14-2|Theorem §C6a.14.2]], 2); derived here from the first-order term between free relativistic states.
>
> *Source: PHY 513, Problem Set 10, Problem 1(a2) (the user's solution) · PS Problem 4.3(a), p. 128 (the vertex $-2i\lambda(\delta^{ij}\delta^{kl} + \delta^{il}\delta^{jk} + \delta^{ik}\delta^{jl})$: "the vertex between two $\Phi^1$s and two $\Phi^2$s has the value $(-2i\lambda)$; that between four $\Phi^1$s has the value $(-6i\lambda)$")*

^thm-c6c-8-3

> [!derivation]- Derivation
> **Step 1** (the interaction as a double sum). The interaction is $\hat{\mathcal H}_I = \frac\lambda4\bigl(\hat\Phi^m\hat\Phi^m\bigr)^2$ ([[§C6c.8 The Linear Sigma Model꞉ Fields with an Internal Index#^mod-c6c-8-1|Model §C6c.8.1]], 3). The square of the sum is a double sum,
>
> $$
> \hat{\mathcal H}_I = \frac\lambda4\sum_{m,n}\hat\Phi^m\hat\Phi^m\,\hat\Phi^n\hat\Phi^n .
> $$
>
> **Step 2** (the first-order term). The first-order term of $T\exp\bigl(-i\int d^4z\,\hat{\mathcal H}_I\bigr)$ ([[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-7|Theorem §C6a.3.7]]) between the initial and final states is
>
> $$
> \langle f|\,(-i)\int d^4z\;\frac\lambda4\sum_{m,n}\hat\Phi^m(z)\,\hat\Phi^m(z)\,\hat\Phi^n(z)\,\hat\Phi^n(z)\,|i\rangle .
> $$
>
> **Step 3** (the contractions). Take four external particles, with momenta $p_1, p_2$ (incoming) and $p_3, p_4$ (outgoing) and types $i, j, k, l$. The vertex is the contribution in which each of the four fields contracts with one of the four external particles, so there is no propagator. A field $\hat\Phi^m(z)$ contracted with a particle of type $i$ and momentum $p$ gives (Step 3 of [[§C6c.8 The Linear Sigma Model꞉ Fields with an Internal Index#^der-c6c-8-2|Derivation §C6c.8.2]]; [[§C6a.14 Feynman Rules for Polynomial Interactions#^lem-c6a-14-1|Lemma §C6a.14.1]]; [[§C6c.2 Contractions with External Particles#^lem-c6c-2-2|Lemma §C6c.2.2]], 2; [[§C6c.2 Contractions with External Particles#^lem-c6c-2-1|Lemma §C6c.2.1]])
>
> $$
> \delta^{im}\,e^{-ip\cdot z} \quad\text{(incoming)} , \qquad \delta^{im}\,e^{ip\cdot z} \quad\text{(outgoing)} .
> $$
>
> All four fields are at the same point $z$, so every contraction gives the same phases, with ([[§CA.4 Fourier Transforms and Fourier Tricks#^thm-ca-4-3|Theorem §CA.4.3]])
>
> $$
> \int d^4z\;e^{-i(p_1 + p_2 - p_3 - p_4)\cdot z} = (2\pi)^4\,\delta^4(p_1 + p_2 - p_3 - p_4) .
> $$
>
> **Step 4** (what the vertex factor is). The vertex factor is the coefficient of this delta function: $-i$ times the coupling $\frac\lambda4$ times the sum over all contractions of their Kronecker deltas, summed over $m, n$ ([[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-1|Theorem §C6c.4.1]], the tree case).
>
> **Step 5** (counting the contractions). The four particles can be assigned to the four fields in $4! = 24$ ways ([[§C6c.2 Contractions with External Particles#^thm-c6c-2-4|Theorem §C6c.2.4]] at one point). The Kronecker deltas depend on which two particles contract with the pair $\hat\Phi^m\hat\Phi^m$, the other two contracting with $\hat\Phi^n\hat\Phi^n$.
>
> **Step 6** (the pair $i, j$ on one pair of fields). If the particles of types $i, j$ contract with $\hat\Phi^m\hat\Phi^m$ and those of types $k, l$ with $\hat\Phi^n\hat\Phi^n$, the deltas are $\delta^{im}\delta^{jm}\delta^{kn}\delta^{ln}$. The two particles can be contracted with the two $\hat\Phi^m$ in $2!$ ways, and likewise for the two $\hat\Phi^n$, which gives $2!\cdot2!$ contractions with these deltas. If instead the particles of types $k, l$ contract with $\hat\Phi^m\hat\Phi^m$ and those of types $i, j$ with $\hat\Phi^n\hat\Phi^n$, the deltas are $\delta^{km}\delta^{lm}\delta^{in}\delta^{jn}$, again for $2!\cdot2!$ contractions. Summed over $m, n$, both give the same result,
>
> $$
> \sum_{m,n}\delta^{im}\delta^{jm}\delta^{kn}\delta^{ln} = \delta^{ij}\delta^{kl} , \qquad \sum_{m,n}\delta^{km}\delta^{lm}\delta^{in}\delta^{jn} = \delta^{kl}\delta^{ij} ,
> $$
>
> so $2\cdot2!\cdot2! = 8$ contractions contribute $\delta^{ij}\delta^{kl}$.
>
> **Step 7** (the other pairs). The other ways of choosing the two particles on $\hat\Phi^m\hat\Phi^m$ work the same way:
>
> $$
> \begin{aligned}
> \sum_{m,n}\delta^{im}\delta^{km}\delta^{jn}\delta^{ln} &= \delta^{ik}\delta^{jl} , & \sum_{m,n}\delta^{jm}\delta^{lm}\delta^{in}\delta^{kn} &= \delta^{jl}\delta^{ik} , \\
> \sum_{m,n}\delta^{im}\delta^{lm}\delta^{jn}\delta^{kn} &= \delta^{il}\delta^{jk} , & \sum_{m,n}\delta^{jm}\delta^{km}\delta^{in}\delta^{ln} &= \delta^{jk}\delta^{il} ,
> \end{aligned}
> $$
>
> each for $2!\cdot2!$ contractions, so $8$ contractions contribute $\delta^{ik}\delta^{jl}$ and $8$ contribute $\delta^{il}\delta^{jk}$. This accounts for all $3\cdot8 = 24$ contractions.
>
> **Step 8** (the result). Hence
>
> $$
> V^{ijkl} = (-i)\cdot\frac\lambda4\cdot8\,\bigl(\delta^{ij}\delta^{kl} + \delta^{ik}\delta^{jl} + \delta^{il}\delta^{jk}\bigr) = -2i\lambda\,\bigl(\delta^{ij}\delta^{kl} + \delta^{ik}\delta^{jl} + \delta^{il}\delta^{jk}\bigr) .
> $$
>
> **Step 9** (check: equal indices). When all four indices are equal the three terms are all $1$, so all $24$ contractions contribute and $V^{iiii} = (-i)\cdot\frac\lambda4\cdot4! = -6i\lambda$.
>
> **What the derivation shows.**
> - The $24$ contractions fall into three groups of $8$, one group for each way of splitting the four lines into two pairs; a group is $2$ (which pair of fields takes which pair of particles) times $2!\cdot2!$. The three terms of $V^{ijkl}$ are these three groups.
> - The same count with the sum split by field content first → the second route below.
> - The same result by four derivatives of $V_{\rm int}$ → [[§C6c.8 The Linear Sigma Model꞉ Fields with an Internal Index#^thm-c6c-8-4|Theorem §C6c.8.4]], [[§C6c.8 The Linear Sigma Model꞉ Fields with an Internal Index#^ex-c6c-8-1|Example §C6c.8.1]].
> - At lowest order the amplitude of a $2 \to 2$ process is this vertex factor, $i\mathcal M = V^{ijkl}$ → [[§C6c.8 The Linear Sigma Model꞉ Fields with an Internal Index#^ex-c6c-8-2|Example §C6c.8.2]].

^der-c6c-8-3

> [!derivation]- Derivation (second route: the sum split by field content)
> *The first version of the solution to Problem Set 10, Problem 1(a2) (2026-11-13), kept as a second route: the interaction is first written as a sum of monomials, and each monomial is counted by itself.*
>
> **Step 1** (the interaction, split by field content). The interaction is $\hat{\mathcal H}_I = \frac\lambda4\bigl(\hat\Phi^m\hat\Phi^m\bigr)^2$ ([[§C6c.8 The Linear Sigma Model꞉ Fields with an Internal Index#^mod-c6c-8-1|Model §C6c.8.1]], 3). The square of the sum is a double sum, which splits into the terms with $m = n$ and those with $m \ne n$; each pair $m \ne n$ appears twice, as $(m, n)$ and $(n, m)$:
>
> $$
> \Bigl(\sum_m\hat\Phi^m\hat\Phi^m\Bigr)^2 = \sum_{m,n}\hat\Phi^m\hat\Phi^m\,\hat\Phi^n\hat\Phi^n = \sum_m\bigl(\hat\Phi^m\bigr)^4 + 2\sum_{m<n}\bigl(\hat\Phi^m\bigr)^2\bigl(\hat\Phi^n\bigr)^2 .
> $$
>
> Hence
>
> $$
> \hat{\mathcal H}_I = \frac\lambda4\sum_m\bigl(\hat\Phi^m\bigr)^4 + \frac\lambda2\sum_{m<n}\bigl(\hat\Phi^m\bigr)^2\bigl(\hat\Phi^n\bigr)^2 .
> $$
>
> **Step 2** (the legs). Every term has four fields, so every vertex has four legs, of two types: four legs of the same field, or two legs of one field and two of another (the vertex data of [[§C6a.14 Feynman Rules for Polynomial Interactions#^def-c6a-14-1|Def. §C6a.14.1]]: one monomial for each $m$ and one for each pair $m < n$).
>
> **Step 3** (the first-order term). The first-order term of $T\exp\bigl(-i\int d^4z\,\hat{\mathcal H}_I\bigr)$ ([[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-7|Theorem §C6a.3.7]]) between the initial and final states is
>
> $$
> \langle f|\,(-i)\int d^4z\,\biggl[\frac\lambda4\sum_m\bigl(\hat\Phi^m\bigr)^4 + \frac\lambda2\sum_{m<n}\bigl(\hat\Phi^m\bigr)^2\bigl(\hat\Phi^n\bigr)^2\biggr](z)\,|i\rangle .
> $$
>
> **Step 4** (the contractions). Take the external particles to have momenta $p_1, p_2$ (incoming) and $p_3, p_4$ (outgoing) and types $i, j, k, l$. A field $\hat\Phi^m(z)$ contracts only with a particle of type $m$ (Step 3 of [[§C6c.8 The Linear Sigma Model꞉ Fields with an Internal Index#^der-c6c-8-2|Derivation §C6c.8.2]]; [[§C6a.14 Feynman Rules for Polynomial Interactions#^lem-c6a-14-1|Lemma §C6a.14.1]]), giving $e^{-ip\cdot z}$ for an incoming and $e^{ip\cdot z}$ for an outgoing particle ([[§C6c.2 Contractions with External Particles#^lem-c6c-2-2|Lemma §C6c.2.2]], 2; [[§C6c.2 Contractions with External Particles#^lem-c6c-2-1|Lemma §C6c.2.1]]). With one vertex all four fields contract with the external particles, so there is no propagator, and every contraction gives the same phases, with ([[§CA.4 Fourier Transforms and Fourier Tricks#^thm-ca-4-3|Theorem §CA.4.3]])
>
> $$
> \int d^4z\;e^{-i(p_1 + p_2 - p_3 - p_4)\cdot z} = (2\pi)^4\,\delta^4(p_1 + p_2 - p_3 - p_4) .
> $$
>
> **Step 5** (what the vertex factor is). The vertex factor is the coefficient of this delta function: $-i$ times the coupling of the term times the number of contractions ([[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-1|Theorem §C6c.4.1]], the tree case).
>
> **Step 6** (four legs of the same field). If all four particles are of type $i$, only the term $\frac\lambda4\bigl(\hat\Phi^i\bigr)^4$ contributes (no sum). The four particles can be contracted with the four fields in $4\cdot3\cdot2\cdot1 = 4!$ ways (one for each $\sigma \in S_4$, all equal: [[§C6c.2 Contractions with External Particles#^thm-c6c-2-4|Theorem §C6c.2.4]] at one point), so the vertex factor is
>
> $$
> (-i)\cdot\frac\lambda4\cdot4! = -6i\lambda .
> $$
>
> **Step 7** (two legs of one field and two of another). If two particles are of type $m$ and two of type $n \ne m$, only the term $\frac\lambda2\bigl(\hat\Phi^m\bigr)^2\bigl(\hat\Phi^n\bigr)^2$ contributes. The two particles of type $m$ can be contracted with the two $\hat\Phi^m$ in $2!$ ways, and likewise for type $n$, so the vertex factor is
>
> $$
> (-i)\cdot\frac\lambda2\cdot2!\cdot2! = -2i\lambda .
> $$
>
> (Written out, with the legs $\hat\Phi^m_a\hat\Phi^m_b\hat\Phi^n_a\hat\Phi^n_b$ and particles $q, q'$ of type $m$, $r, r'$ of type $n$, the four contractions are $\{q a, q' b\}$ or $\{q b, q' a\}$, each with $\{r a, r' b\}$ or $\{r b, r' a\}$.)
>
> **Step 8** (general indices). The indices $i, j, k, l$ can be equal in pairs in three ways: $i = j$ and $k = l$, $i = k$ and $j = l$, or $i = l$ and $j = k$. Each gives $-2i\lambda$, and any other pattern gives zero, since no term of $\hat{\mathcal H}_I$ has that field content. Hence
>
> $$
> V^{ijkl} = -2i\lambda\,\bigl(\delta^{ij}\delta^{kl} + \delta^{ik}\delta^{jl} + \delta^{il}\delta^{jk}\bigr) .
> $$
>
> **Step 9** (check). When all four indices are equal the three terms are all $1$, and $V^{iiii} = -6i\lambda$, in agreement with Step 6.
>
> **What the derivation shows.**
> - The coefficient $\frac\lambda2$ of the mixed term, twice the $\frac\lambda4$ of the Lagrangian, comes from the two orders $(m, n)$, $(n, m)$ of the double sum; with $2!\cdot2!$ contractions against $4!$ it makes the two cases differ by the factor $3$, the number of pairings.
> - The two cases $-6i\lambda$ and $-2i\lambda$ are the cases 1 and 2 of the theorem; the first route obtains all index patterns at once.

^der-c6c-8-3b

*Uses:* [[§C6c.8 The Linear Sigma Model꞉ Fields with an Internal Index#^mod-c6c-8-1|Model §C6c.8.1]], [[§C6a.14 Feynman Rules for Polynomial Interactions#^def-c6a-14-1|Def. §C6a.14.1]], [[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-7|Theorem §C6a.3.7]], [[§C6a.14 Feynman Rules for Polynomial Interactions#^lem-c6a-14-1|Lemma §C6a.14.1]], [[§C6c.2 Contractions with External Particles#^lem-c6c-2-1|Lemma §C6c.2.1]], [[§C6c.2 Contractions with External Particles#^lem-c6c-2-2|Lemma §C6c.2.2]], [[§C6c.2 Contractions with External Particles#^thm-c6c-2-4|Theorem §C6c.2.4]], [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-1|Theorem §C6c.4.1]], [[§CA.4 Fourier Transforms and Fourier Tricks#^thm-ca-4-3|Theorem §CA.4.3]]

*Procedure:* [[P6 Tree Amplitude from a Lagrangian#^p6-2|P6, step 2]]

> [!theorem] Theorem §C6c.8.4: The Vertex Factor Is −i Times the Derivative of the Interaction Potential
> Let $\mathcal L_{\rm int} = -V_{\rm int}(\Phi)$, with $V_{\rm int}$ a polynomial without derivatives in real fields $\Phi^1, \dots, \Phi^N$ (the interactions of [[§C6a.14 Feynman Rules for Polynomial Interactions#^def-c6a-14-1|Def. §C6a.14.1]] with real fields, written with an index). Then the vertex at which $n$ lines with indices $i_1, \dots, i_n$ meet has the factor
>
> $$
> V^{i_1\cdots i_n} = -i\,\frac{\partial^nV_{\rm int}}{\partial\Phi^{i_1}\cdots\partial\Phi^{i_n}}\bigg|_{\Phi = 0} .
> $$
>
> 1. If $V_{\rm int}$ is homogeneous of degree $n$ (one kind of vertex, as in [[§C6c.8 The Linear Sigma Model꞉ Fields with an Internal Index#^mod-c6c-8-1|Model §C6c.8.1]]), the $n$-th derivative is a constant and nothing has to be set to zero. If $V_{\rm int}$ has terms of several degrees (cubic and quartic, as in [[§C6c.9 The Linear Sigma Model꞉ the Broken Phase#^thm-c6c-9-5|Theorem §C6c.9.5]]), the value at $\Phi = 0$ picks the terms of degree $n$.
> 2. It is the rule $-ic\prod_in_i!$ of [[§C6a.14 Feynman Rules for Polynomial Interactions#^thm-c6a-14-2|Theorem §C6a.14.2]] for all monomials at once: for a term $c\prod_i(\Phi^i)^{n_i}$ of $V_{\rm int}$, the derivative with respect to exactly its field content ($n_i$ times $\Phi^i$ for each $i$) is $c\prod_in_i!$, and the derivative with respect to any other content of the same degree is zero.
> 3. $V^{i_1\cdots i_n}$ is symmetric under every permutation of its indices ([[§6 Equality of Mixed Partials#^thm-6-1|452 Thm. §6.1]]), as a sum over all ways of attaching the $n$ lines to the legs of the vertex must be.
>
> *Equivalently,* in words: strip the fields from the term, multiply by $i$ and by the number of permutations of equal fields ([[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-4|Theorem §C6c.4.4]], 2–3; [[§C6c.6 Feynman Rules for Amplitudes#^thm-c6c-6-1|Theorem §C6c.6.1]], 4); the derivatives do the stripping and the counting in one step.
>
> *Model:* [[§C6a.0 Setups and Observables#^mod-c6a-0-3|Model §C6a.0.3]] with any polynomial interaction without derivatives of real scalar fields; *applies:* the vertex factors of the Feynman rules, every order ([[§C6a.14 Feynman Rules for Polynomial Interactions#^thm-c6a-14-4|Theorem §C6a.14.4]], [[§C6c.6 Feynman Rules for Amplitudes#^thm-c6c-6-3|Theorem §C6c.6.3]]); not for interactions with derivatives, where the vertex depends on the momenta.
>
> *Source: PHY 513, Problem Set 10, Problem 1(a2) (statement, the hint: "the vertex factor is $-i$ times the fourth derivative of the interaction potential with respect to $\Phi^i$, $\Phi^j$, $\Phi^k$, $\Phi^l$") · stated in general and derived here from [[§C6a.14 Feynman Rules for Polynomial Interactions#^thm-c6a-14-2|Theorem §C6a.14.2]]; checked with `qft-C/tools/hw10/verify.py`*

^thm-c6c-8-4

> [!derivation]- Derivation
> **Step 1** (monomials). Write $V_{\rm int} = \sum_tc_tM_t$ with distinct monomials $M_t = \prod_i(\Phi^i)^{n_{t,i}}$ of degree $r_t = \sum_in_{t,i}$. Differentiation is linear, so it is enough to differentiate one monomial $M = \prod_i(\Phi^i)^{n_i}$ of degree $r$.
>
> **Step 2** (the derivative of a monomial). Let the indices $i_1, \dots, i_n$ contain the value $i$ exactly $m_i$ times, $\sum_im_i = n$. Since $\frac{\partial}{\partial\Phi^i}$ acts only on the factor $(\Phi^i)^{n_i}$, and $\bigl(\frac{d}{dx}\bigr)^mx^k = k(k-1)\cdots(k-m+1)\,x^{k-m} = \frac{k!}{(k-m)!}x^{k-m}$ for $m \le k$ and $0$ for $m > k$,
>
> $$
> \frac{\partial^nM}{\partial\Phi^{i_1}\cdots\partial\Phi^{i_n}} = \prod_i\frac{n_i!}{(n_i - m_i)!}\,(\Phi^i)^{n_i - m_i} \quad\text{if every } m_i \le n_i , \qquad = 0 \quad\text{otherwise} .
> $$
>
> **Step 3** (the value at $\Phi = 0$). At $\Phi = 0$ a nonzero value needs $n_i - m_i = 0$ for every $i$: the indices are exactly the field content of $M$, in particular $n = r$, and the value is $\prod_in_i!$. In the other cases: if $n > r$, some $m_i > n_i$ and the derivative vanishes identically; if $n < r$, some power of a field is left and vanishes at $\Phi = 0$; if $n = r$ but the content differs, some $m_i > n_i$. Therefore
>
> $$
> -i\,\frac{\partial^nV_{\rm int}}{\partial\Phi^{i_1}\cdots\partial\Phi^{i_n}}\bigg|_{\Phi = 0} = -i\,c_t\prod_in_{t,i}! \quad\text{for the monomial } M_t \text{ with } n_{t,i} = m_i \text{ for all } i ,
> $$
>
> and $0$ if $V_{\rm int}$ has no such monomial.
>
> **Step 4** (the same count as the contractions). At a vertex of type $t$, $n$ distinct lines with $m_i$ of them of type $i$ attach only if $m_i = n_{t,i}$ for every $i$ (a line of type $i$ ends on a leg of type $i$: [[§C6a.14 Feynman Rules for Polynomial Interactions#^lem-c6a-14-1|Lemma §C6a.14.1]]), and then in $\prod_in_{t,i}!$ ways, all equal; the vertex factor is $-ic_t\prod_in_{t,i}!$ ([[§C6a.14 Feynman Rules for Polynomial Interactions#^thm-c6a-14-2|Theorem §C6a.14.2]], 1, with $g_t = c_t$). This is the right-hand side of Step 3: part 2, and with it the formula of the statement. Part 1 is Step 3 read for a homogeneous $V_{\rm int}$ (every monomial has degree $n$, so no field is left after $n$ derivatives).
>
> **Step 5** (part 3). Partial derivatives of a polynomial commute ([[§6 Equality of Mixed Partials#^thm-6-1|452 Thm. §6.1]]), so permuting $i_1, \dots, i_n$ does not change the derivative.
>
> **What the derivation shows.**
> - Each $\frac{\partial}{\partial\Phi^i}$ removes one field of type $i$ from the term in every possible way, by the product rule; a line of type $i$ is attached to one leg of type $i$ in every possible way. The product rule is the count of contractions.
> - For a potential with terms of several degrees the derivative must be taken at zero field; the cubic vertices of the broken phase are an instance → [[§C6c.9 The Linear Sigma Model꞉ the Broken Phase#^thm-c6c-9-5|Theorem §C6c.9.5]].

^der-c6c-8-4

*Uses:* [[§C6a.14 Feynman Rules for Polynomial Interactions#^thm-c6a-14-2|Theorem §C6a.14.2]], [[§C6a.14 Feynman Rules for Polynomial Interactions#^def-c6a-14-1|Def. §C6a.14.1]], [[§C6a.14 Feynman Rules for Polynomial Interactions#^lem-c6a-14-1|Lemma §C6a.14.1]], [[§6 Equality of Mixed Partials#^thm-6-1|452 Thm. §6.1]]

*Procedure:* [[P6 Tree Amplitude from a Lagrangian#^p6-2|P6, step 2]]

> [!example] Example §C6c.8.1: The Sigma-Model Vertex by Four Derivatives
> The vertex of [[§C6c.8 The Linear Sigma Model꞉ Fields with an Internal Index#^thm-c6c-8-3|Theorem §C6c.8.3]] once more, by [[§C6c.8 The Linear Sigma Model꞉ Fields with an Internal Index#^thm-c6c-8-4|Theorem §C6c.8.4]]: differentiate $V_{\rm int} = \frac\lambda4\bigl(\Phi^m\Phi^m\bigr)^2$ four times, using $\frac{\partial\Phi^m}{\partial\Phi^i} = \delta^{mi}$ and $\frac{\partial}{\partial\Phi^i}(\Phi^m\Phi^m) = 2\Phi^i$.
>
> **Step 1** (first derivative).
>
> $$
> \frac{\partial V_{\rm int}}{\partial\Phi^i} = \frac\lambda4\cdot2\bigl(\Phi^m\Phi^m\bigr)\cdot2\Phi^i = \lambda\bigl(\Phi^m\Phi^m\bigr)\Phi^i .
> $$
>
> **Step 2** (second derivative; product rule on $(\Phi^m\Phi^m)\,\Phi^i$).
>
> $$
> \frac{\partial^2V_{\rm int}}{\partial\Phi^j\partial\Phi^i} = \lambda\bigl[2\Phi^j\Phi^i + \bigl(\Phi^m\Phi^m\bigr)\delta^{ij}\bigr] .
> $$
>
> **Step 3** (third derivative).
>
> $$
> \frac{\partial^3V_{\rm int}}{\partial\Phi^k\partial\Phi^j\partial\Phi^i} = \lambda\bigl[2\delta^{jk}\Phi^i + 2\Phi^j\delta^{ik} + 2\Phi^k\delta^{ij}\bigr] .
> $$
>
> **Step 4** (fourth derivative). Every term is linear in the field, so the result is a constant ($V_{\rm int}$ is homogeneous of degree $4$):
>
> $$
> \frac{\partial^4V_{\rm int}}{\partial\Phi^l\partial\Phi^k\partial\Phi^j\partial\Phi^i} = \lambda\bigl[2\delta^{jk}\delta^{il} + 2\delta^{jl}\delta^{ik} + 2\delta^{kl}\delta^{ij}\bigr] = 2\lambda\,\bigl(\delta^{ij}\delta^{kl} + \delta^{ik}\delta^{jl} + \delta^{il}\delta^{jk}\bigr) .
> $$
>
> **Step 5** (the vertex). Times $-i$: $V^{ijkl} = -2i\lambda\,(\delta^{ij}\delta^{kl} + \delta^{ik}\delta^{jl} + \delta^{il}\delta^{jk})$, the result of the contraction count. For $N = 1$: $-i\frac{d^4}{d\Phi^4}\frac\lambda4\Phi^4 = -i\frac\lambda4\cdot4! = -6i\lambda$ ([[§C6c.8 The Linear Sigma Model꞉ Fields with an Internal Index#^cau-c6c-8-1|Caution: The normalization of the quartic term]]).
>
> *Source: derived here by the hint of PHY 513, Problem Set 10, Problem 1(a2) ([[§C6c.8 The Linear Sigma Model꞉ Fields with an Internal Index#^thm-c6c-8-4|Theorem §C6c.8.4]]); the result is the user's of Problem 1(a2), obtained there by counting contractions · checked for all index values with `qft-C/tools/hw10/verify.py`*

^ex-c6c-8-1

## Three processes, three total cross sections

> [!example] Example §C6c.8.2: Φ¹Φ² → Φ¹Φ², Φ¹Φ¹ → Φ²Φ² and Φ¹Φ¹ → Φ¹Φ¹ at Lowest Order
> ![[ph-qft-c6c-8-1.svg]]
> *The one diagram of each process at order $\lambda$: the vertex of [[§C6c.8 The Linear Sigma Model꞉ Fields with an Internal Index#^thm-c6c-8-3|Theorem §C6c.8.3]] with the types of the four external particles ($\Phi^1$ green, $\Phi^2$ blue; incoming left, outgoing right), the terms of $V^{ijkl}$ that survive, and $i\mathcal M$. Added figure.*
>
> In [[§C6c.8 The Linear Sigma Model꞉ Fields with an Internal Index#^mod-c6c-8-1|Model §C6c.8.1]], to lowest order in $\lambda$, in the centre-of-mass frame:
>
> | process | $(i, j, k, l)$ | $i\mathcal M$ | $\bigl(\frac{d\sigma}{d\Omega}\bigr)_{\rm cm}$ | final particles | $\sigma$ |
> |---|---|---|---|---|---|
> | $\Phi^1\Phi^2 \to \Phi^1\Phi^2$ | $(1, 2, 1, 2)$ | $-2i\lambda$ | $\dfrac{\lambda^2}{16\pi^2E_{\rm cm}^2}$ | different types | $\dfrac{\lambda^2}{4\pi E_{\rm cm}^2}$ |
> | $\Phi^1\Phi^1 \to \Phi^2\Phi^2$ | $(1, 1, 2, 2)$ | $-2i\lambda$ | $\dfrac{\lambda^2}{16\pi^2E_{\rm cm}^2}$ | identical | $\dfrac{\lambda^2}{8\pi E_{\rm cm}^2}$ |
> | $\Phi^1\Phi^1 \to \Phi^1\Phi^1$ | $(1, 1, 1, 1)$ | $-6i\lambda$ | $\dfrac{9\lambda^2}{16\pi^2E_{\rm cm}^2}$ | identical | $\dfrac{9\lambda^2}{8\pi E_{\rm cm}^2}$ |
>
> **Step 1** (states). With relativistic normalization, the initial state with particles of types $i, j$ and momenta $p_1, p_2$, and the final state with types $k, l$ and momenta $p_3, p_4$, are
>
> $$
> |p_1, i;\,p_2, j\rangle = \sqrt{2E_{\mathbf p_1}}\sqrt{2E_{\mathbf p_2}}\;\hat a^{i\dagger}_{\mathbf p_1}\hat a^{j\dagger}_{\mathbf p_2}|0\rangle , \qquad \langle p_3, k;\,p_4, l| = \sqrt{2E_{\mathbf p_3}}\sqrt{2E_{\mathbf p_4}}\;\langle0|\,\hat a^l_{\mathbf p_4}\hat a^k_{\mathbf p_3} .
> $$
>
> For the three processes, with the factors $\sqrt{2E_{\mathbf p}}$ as above,
>
> $$
> \begin{aligned}
> \Phi^1\Phi^2 \to \Phi^1\Phi^2:&\qquad |i\rangle \propto \hat a^{1\dagger}_{\mathbf p_1}\hat a^{2\dagger}_{\mathbf p_2}|0\rangle , &\langle f| &\propto \langle0|\,\hat a^2_{\mathbf p_4}\hat a^1_{\mathbf p_3} , \\
> \Phi^1\Phi^1 \to \Phi^2\Phi^2:&\qquad |i\rangle \propto \hat a^{1\dagger}_{\mathbf p_1}\hat a^{1\dagger}_{\mathbf p_2}|0\rangle , &\langle f| &\propto \langle0|\,\hat a^2_{\mathbf p_4}\hat a^2_{\mathbf p_3} , \\
> \Phi^1\Phi^1 \to \Phi^1\Phi^1:&\qquad |i\rangle \propto \hat a^{1\dagger}_{\mathbf p_1}\hat a^{1\dagger}_{\mathbf p_2}|0\rangle , &\langle f| &\propto \langle0|\,\hat a^1_{\mathbf p_4}\hat a^1_{\mathbf p_3} .
> \end{aligned}
> $$
>
> **Step 2** (amplitudes). At lowest order each process is given by the single vertex of [[§C6c.8 The Linear Sigma Model꞉ Fields with an Internal Index#^thm-c6c-8-3|Theorem §C6c.8.3]], so
>
> $$
> \langle p_3, k;\,p_4, l|\,i\hat T\,|p_1, i;\,p_2, j\rangle = (2\pi)^4\,\delta^4(p_1 + p_2 - p_3 - p_4)\,V^{ijkl} ,
> $$
>
> and comparing with $\langle f|i\hat T|i\rangle = (2\pi)^4\delta^4(p_1 + p_2 - p_3 - p_4)\,i\mathcal M$ ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-3|Def. §C6b.1.3]]) gives $i\mathcal M = V^{ijkl}$. With $(i, j)$ the incoming and $(k, l)$ the outgoing types,
>
> $$
> \begin{aligned}
> \Phi^1\Phi^2 \to \Phi^1\Phi^2:&\quad (i, j, k, l) = (1, 2, 1, 2) , &\text{only } \delta^{ik}\delta^{jl} = 1 , &\quad i\mathcal M = -2i\lambda , \\
> \Phi^1\Phi^1 \to \Phi^2\Phi^2:&\quad (i, j, k, l) = (1, 1, 2, 2) , &\text{only } \delta^{ij}\delta^{kl} = 1 , &\quad i\mathcal M = -2i\lambda , \\
> \Phi^1\Phi^1 \to \Phi^1\Phi^1:&\quad (i, j, k, l) = (1, 1, 1, 1) , &\text{all three} = 1 , &\quad i\mathcal M = -6i\lambda .
> \end{aligned}
> $$
>
> **Step 3** (differential cross sections). For $2 \to 2$ scattering in the centre-of-mass frame ([[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-4|Theorem §C6b.4.4]]),
>
> $$
> \Bigl(\frac{d\sigma}{d\Omega}\Bigr)_{\rm cm} = \frac{1}{2E_1\,2E_2\,|\mathbf v_1 - \mathbf v_2|}\,\frac{|\mathbf p_f|}{16\pi^2E_{\rm cm}}\,|\mathcal M|^2 ,
> $$
>
> where $|\mathbf p_i|$ and $|\mathbf p_f|$ are the magnitudes of the initial and final momenta. In this frame $\mathbf p_2 = -\mathbf p_1$, and with $\mathbf v = \mathbf p/E$ and $E_1 + E_2 = E_{\rm cm}$,
>
> $$
> 2E_1\,2E_2\,|\mathbf v_1 - \mathbf v_2| = 4E_1E_2\Bigl(\frac{|\mathbf p_i|}{E_1} + \frac{|\mathbf p_i|}{E_2}\Bigr) = 4|\mathbf p_i|\,(E_1 + E_2) = 4|\mathbf p_i|\,E_{\rm cm} ,
> $$
>
> so
>
> $$
> \Bigl(\frac{d\sigma}{d\Omega}\Bigr)_{\rm cm} = \frac{|\mathbf p_f|}{64\pi^2E_{\rm cm}^2\,|\mathbf p_i|}\,|\mathcal M|^2 .
> $$
>
> By four-momentum conservation in the centre-of-mass frame, $\mathbf p_2 = -\mathbf p_1$ and $\mathbf p_4 = -\mathbf p_3$, and the total energy is $E_{\rm cm}$ before and after. All particles have mass $m$, so each carries energy $E_{\rm cm}/2$:
>
> $$
> \sqrt{|\mathbf p_i|^2 + m^2} = \frac{E_{\rm cm}}{2} = \sqrt{|\mathbf p_f|^2 + m^2} \quad\Longrightarrow\quad |\mathbf p_f| = |\mathbf p_i| .
> $$
>
> Hence $\bigl(\frac{d\sigma}{d\Omega}\bigr)_{\rm cm} = \frac{|\mathcal M|^2}{64\pi^2E_{\rm cm}^2}$ (this is [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-9|Theorem §C6b.4.9]], all masses equal), and
>
> $$
> \begin{aligned}
> \Bigl(\frac{d\sigma}{d\Omega}\Bigr)_{\rm cm}(\Phi^1\Phi^2 \to \Phi^1\Phi^2) &= \frac{4\lambda^2}{64\pi^2E_{\rm cm}^2} = \frac{\lambda^2}{16\pi^2E_{\rm cm}^2} , \\
> \Bigl(\frac{d\sigma}{d\Omega}\Bigr)_{\rm cm}(\Phi^1\Phi^1 \to \Phi^2\Phi^2) &= \frac{4\lambda^2}{64\pi^2E_{\rm cm}^2} = \frac{\lambda^2}{16\pi^2E_{\rm cm}^2} , \\
> \Bigl(\frac{d\sigma}{d\Omega}\Bigr)_{\rm cm}(\Phi^1\Phi^1 \to \Phi^1\Phi^1) &= \frac{36\lambda^2}{64\pi^2E_{\rm cm}^2} = \frac{9\lambda^2}{16\pi^2E_{\rm cm}^2} .
> \end{aligned}
> $$
>
> **Step 4** (identical particles). The cross section is the scattering probability, summed over all final states, per unit incoming flux; the sum over final states is taken with the completeness relation on two-particle states. For two particles of the same type $\hat a^\dagger_{\mathbf p_3}\hat a^\dagger_{\mathbf p_4} = \hat a^\dagger_{\mathbf p_4}\hat a^\dagger_{\mathbf p_3}$, so $|p_3p_4\rangle = |p_4p_3\rangle$, and ([[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-2|Theorem §C2a.4.2]])
>
> $$
> \langle q_3q_4|p_3p_4\rangle = (2E_{\mathbf p_3})(2E_{\mathbf p_4})(2\pi)^6\Bigl[\delta^3(\mathbf q_3 - \mathbf p_3)\,\delta^3(\mathbf q_4 - \mathbf p_4) + \delta^3(\mathbf q_3 - \mathbf p_4)\,\delta^3(\mathbf q_4 - \mathbf p_3)\Bigr] .
> $$
>
> With $d\Pi = \frac{d^3p}{(2\pi)^3\,2E_{\mathbf p}}$,
>
> $$
> \int d\Pi_3\,d\Pi_4\;|p_3p_4\rangle\langle p_3p_4|q_3q_4\rangle = |q_3q_4\rangle + |q_4q_3\rangle = 2\,|q_3q_4\rangle :
> $$
>
> the integral over all $(\mathbf p_3, \mathbf p_4)$ reaches each final state twice, at $(\mathbf p_3, \mathbf p_4)$ and at $(\mathbf p_4, \mathbf p_3)$. The completeness relation is therefore
>
> $$
> \mathbb 1 = \frac{1}{2!}\int d\Pi_3\,d\Pi_4\;|p_3p_4\rangle\langle p_3p_4| ,
> $$
>
> and for identical final particles the phase-space integral carries a factor $\frac12$, $\sigma = \frac12\int d\Omega\,\frac{d\sigma}{d\Omega}$. For distinguishable final particles only the first product of delta functions appears, and there is no such factor. (This is the case $n = 2$ of [[§C6b.9 Evaluating the Cross Section#^thm-c6b-9-4|Theorem §C6b.9.4]], Step 2 of its derivation; as half the sphere: [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-6|Theorem §C6b.4.6]].)
>
> **Step 5** (total cross sections). Each $\frac{d\sigma}{d\Omega}$ is independent of angle, so $\int d\Omega$ gives $4\pi$ ([[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-5|Theorem §C6b.4.5]], 3). In $\Phi^1\Phi^2 \to \Phi^1\Phi^2$ the final particles are of different types; in the other two processes they are identical. Hence
>
> $$
> \begin{aligned}
> \sigma(\Phi^1\Phi^2 \to \Phi^1\Phi^2) &= 4\pi\cdot\frac{\lambda^2}{16\pi^2E_{\rm cm}^2} = \frac{\lambda^2}{4\pi E_{\rm cm}^2} , \\
> \sigma(\Phi^1\Phi^1 \to \Phi^2\Phi^2) &= \frac12\cdot4\pi\cdot\frac{\lambda^2}{16\pi^2E_{\rm cm}^2} = \frac{\lambda^2}{8\pi E_{\rm cm}^2} , \\
> \sigma(\Phi^1\Phi^1 \to \Phi^1\Phi^1) &= \frac12\cdot4\pi\cdot\frac{9\lambda^2}{16\pi^2E_{\rm cm}^2} = \frac{9\lambda^2}{8\pi E_{\rm cm}^2} .
> \end{aligned}
> $$
>
> *Model:* [[§C6c.8 The Linear Sigma Model꞉ Fields with an Internal Index#^mod-c6c-8-1|Model §C6c.8.1]], $m^2 > 0$; *applies:* lowest order in $\lambda$, free relativistic states for the in and out states, centre-of-mass frame, any $E_{\rm cm} \ge 2m$.
>
> *Source: PHY 513, Problem Set 10, Problem 1(a3) (the user's solution; the table collects its results) · PS Problem 4.3(a), p. 128 (the three processes)*

^ex-c6c-8-2

> [!theorem] Theorem §C6c.8.5: One Vertex Function, Three Total Cross Sections
> In [[§C6c.8 The Linear Sigma Model꞉ Fields with an Internal Index#^mod-c6c-8-1|Model §C6c.8.1]] at lowest order every $2 \to 2$ amplitude is the same function $i\mathcal M = V^{ijkl}$ ([[§C6c.8 The Linear Sigma Model꞉ Fields with an Internal Index#^thm-c6c-8-3|Theorem §C6c.8.3]]), and the processes differ in two places only:
> 1. **which $\delta$-terms survive**, decided by the types of the four particles: one term, $i\mathcal M = -2i\lambda$, when two types occur; all three, $i\mathcal M = -6i\lambda$, when all four particles are of one type; $|\mathcal M|^2$ then differs by the factor $9$;
> 2. **the factor $\frac12$ for identical final particles**, which belongs to the total cross section and not to the amplitude: at a given angle $d\sigma/d\Omega$ has no factor, in the total $\sigma = \frac12\int d\Omega\,\frac{d\sigma}{d\Omega}$ ([[§C6b.9 Evaluating the Cross Section#^thm-c6b-9-4|Theorem §C6b.9.4]]).
>
> So $\Phi^1\Phi^2 \to \Phi^1\Phi^2$ and $\Phi^1\Phi^1 \to \Phi^2\Phi^2$ have the same $\mathcal M$ and the same $d\sigma/d\Omega$ but total cross sections that differ by $2$, and
>
> $$
> \sigma(\Phi^1\Phi^2 \to \Phi^1\Phi^2) : \sigma(\Phi^1\Phi^1 \to \Phi^2\Phi^2) : \sigma(\Phi^1\Phi^1 \to \Phi^1\Phi^1) = 2 : 1 : 9 .
> $$
>
> The identical particles of the *initial* state give no factor.
>
> *Model:* [[§C6c.8 The Linear Sigma Model꞉ Fields with an Internal Index#^mod-c6c-8-1|Model §C6c.8.1]], $m^2 > 0$; *applies:* lowest order in $\lambda$, centre-of-mass frame, equal $E_{\rm cm}$ for the three processes.
>
> *Source: stated here from PHY 513, Problem Set 10, Problem 1(a3) (the user's solution; statement: "Take care with identical particles in the final state")*

^thm-c6c-8-5

> [!derivation]- Derivation
> **Step 1** (part 1). In $V^{ijkl} = -2i\lambda(\delta^{ij}\delta^{kl} + \delta^{ik}\delta^{jl} + \delta^{il}\delta^{jk})$ put the types: $(1, 2, 1, 2)$ gives $(0 + 1 + 0)$, $(1, 1, 2, 2)$ gives $(1 + 0 + 0)$, $(1, 1, 1, 1)$ gives $(1 + 1 + 1)$; so $|\mathcal M|^2 = 4\lambda^2$, $4\lambda^2$, $36\lambda^2$ (Step 2 of [[§C6c.8 The Linear Sigma Model꞉ Fields with an Internal Index#^ex-c6c-8-2|Example §C6c.8.2]]).
>
> **Step 2** (part 2). All masses are equal, so $\bigl(\frac{d\sigma}{d\Omega}\bigr)_{\rm cm} = \frac{|\mathcal M|^2}{64\pi^2E_{\rm cm}^2}$ for each process ([[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-9|Theorem §C6b.4.9]]), with no identical-particle factor at a given angle ([[§C6b.9 Evaluating the Cross Section#^thm-c6b-9-4|Theorem §C6b.9.4]], "no factor locally"). Integrated over all directions, the final states $\Phi^2\Phi^2$ and $\Phi^1\Phi^1$ are each counted twice, $S_{\rm id} = 2!$; the final state $\Phi^1\Phi^2$ is counted once.
>
> **Step 3** (the ratio).
>
> $$
> \sigma = \frac{1}{S_{\rm id}}\cdot4\pi\cdot\frac{|\mathcal M|^2}{64\pi^2E_{\rm cm}^2} : \qquad \frac{4\lambda^2}{1} : \frac{4\lambda^2}{2} : \frac{36\lambda^2}{2} = 4 : 2 : 18 = 2 : 1 : 9 .
> $$
>
> **Step 4** (the initial state). The flux factor $\frac{1}{2E_1\,2E_2\,|\mathbf v_1 - \mathbf v_2|}$ and the definition of the cross section refer to one beam particle and one target particle of given momenta ([[§C6b.3 The Cross Section#^def-c6b-3-2|Def. §C6b.3.2]]); nothing is summed over initial states, so two identical incoming particles bring no factor ($\Phi^1\Phi^1 \to \Phi^2\Phi^2$ has $\frac12$ from the final $\Phi^2\Phi^2$, not from the initial $\Phi^1\Phi^1$).

^der-c6c-8-5

*Uses:* [[§C6c.8 The Linear Sigma Model꞉ Fields with an Internal Index#^thm-c6c-8-3|Theorem §C6c.8.3]], [[§C6c.8 The Linear Sigma Model꞉ Fields with an Internal Index#^ex-c6c-8-2|Example §C6c.8.2]], [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-9|Theorem §C6b.4.9]], [[§C6b.9 Evaluating the Cross Section#^thm-c6b-9-4|Theorem §C6b.9.4]], [[§C6b.3 The Cross Section#^def-c6b-3-2|Def. §C6b.3.2]]

*Procedure:* [[P7 From ℳ to σ or Γ#^p7-7|P7, step 7]]

> [!abstract]- Mathematical background
> Proved in the Math vault and in CA; each line says what the physics above relies on.
>
> - [[§11 Topological Groups and Classical Matrix Groups#^def-11-7|591 Def. §11.7]] — the orthogonal group $O(N)$: the matrices that preserve the dot product, hence $\Phi^i\Phi^i$ and $\partial_\mu\Phi^i\,\partial^\mu\Phi^i$ (Model §C6c.8.1, 1); as a matrix Lie group, [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-3|Def. §CB.1.3]].
> - [[§6 Equality of Mixed Partials#^thm-6-1|452 Thm. §6.1]] — mixed partial derivatives commute: the vertex function $V^{i_1\cdots i_n}$ is symmetric in its indices (Theorem §C6c.8.4, 3).
> - [[§CA.4 Fourier Transforms and Fourier Tricks#^thm-ca-4-3|Theorem §CA.4.3]] — the vertex integral of the plane waves is the momentum delta whose coefficient is the vertex factor.
> - [[§CA.9 Splitting Pairings and the Exponential Formula#^thm-ca-9-4|Theorem §CA.9.4]] — the relabelling group of a vertex with several kinds of legs, order $\prod_in_i!$, behind the vertex factor $-ic\prod_in_i!$ (used through [[§C6a.14 Feynman Rules for Polynomial Interactions#^thm-c6a-14-2|Theorem §C6a.14.2]]).

> [!remark]- Connections
> - With one field the model is $\phi^4$ theory in another normalization, $\lambda_{\rm lecture} = 6\lambda$, and the third cross section is the lecture's first one — [[§C6c.8 The Linear Sigma Model꞉ Fields with an Internal Index#^cau-c6c-8-1|Caution: The normalization of the quartic term]], [[§C6c.11 From the Question to the Formula#^ex-c6c-11-3|Example §C6c.11.3]].
> - In the three-scalar theory the vertex content decides which channels exist; here it decides which $\delta$-terms of one vertex survive. Both are the statement that a line of one type ends only on a leg of that type — [[§C6c.6 Feynman Rules for Amplitudes#^thm-c6c-6-6|Theorem §C6c.6.6]], [[§C6a.14 Feynman Rules for Polynomial Interactions#^lem-c6a-14-1|Lemma §C6a.14.1]].
> - For $N = 2$ and $\phi = (\Phi^1 + i\Phi^2)/\sqrt2$, $\Phi^i\Phi^i = 2\phi^\dagger\phi$ and the interaction is $\lambda(\phi^\dagger\phi)^2$, the complex model of Problem Set 8 with coupling $4\lambda$ in place of its $\lambda$; its vertex $-i\cdot4\lambda$ is $V^{ijkl}u^iu^j\bar u^k\bar u^l$ with $u = (1, i)/\sqrt2$, since $\delta^{ij}u^iu^j = 0$ and $\delta^{ik}u^i\bar u^k = 1$: $-2i\lambda(0 + 1 + 1)$ — [[§C6a.9 Position-Space Feynman Rules#^mod-c6a-9-3|Model §C6a.9.3]], [[§C6a.14 Feynman Rules for Polynomial Interactions#^thm-c6a-14-2|Theorem §C6a.14.2]].
> - The $\frac12$ of the total cross section is the counting of final states, obtained in the box by ordered tuples and with wave packets by the resolution of the identity; the three processes show it acting on $\sigma$ and not on $d\sigma/d\Omega$ — [[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-8|Theorem §C6b.2.8]], [[§C6b.9 Evaluating the Cross Section#^thm-c6b-9-4|Theorem §C6b.9.4]], [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-6|Theorem §C6b.4.6]].
> - The same vertex function, with $N - 1$ fields, is the four-pion vertex of the broken phase, and the derivative rule gives its cubic vertices — [[§C6c.9 The Linear Sigma Model꞉ the Broken Phase#^thm-c6c-9-5|Theorem §C6c.9.5]].
> - The procedure that reads a vertex off a Lagrangian and the one that turns $\mathcal M$ into $\sigma$ — [[P6 Tree Amplitude from a Lagrangian|P6]], [[P7 From ℳ to σ or Γ|P7]].
