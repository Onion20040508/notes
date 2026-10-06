---
type: section
subject: "[[Functional Analysis]]"
chapter: 7
section: 32
tags: [functional-analysis, math556, companion]
---
← [[§31 The Completeness Relation]] · ↑ [[· 7 Functional Analysis and Quantum Mechanics]] · [[§33 Bound States Need Not Be Complete꞉ Hydrogen]] →

*Companion — Thread: dimension. Why $|x\rangle$ is not a vector, and what $\int |x\rangle\langle x|\,dx$ means.*

Physics also writes $\int |x\rangle\langle x|\,dx = \mathbf{1}$, with an uncountable family $\{|x\rangle\}_{x \in \mathbb{R}^n}$, while the energy eigenstates of a confined system form a countable basis. This section shows that there is no conflict in dimension, because the $|x\rangle$ are not vectors of the Hilbert space, and says what the continuous identity means.

## Every Orthonormal Set in L² is Countable

> [!theorem] Proposition §32.1: Orthonormal Sets in Separable Spaces are Countable
> Let $X$ be a separable inner product space (Definition [[§24 Orthonormal Sets and Bases#^def-24-5|§24.5]]). Then every orthonormal set in $X$ is countable.

^prop-32-1

> [!proof]+ Proof
> Let $\{e_\alpha\}_{\alpha \in \Lambda}$ be orthonormal and $D \subset X$ a countable dense set. For $\alpha \neq \beta$, Pythagoras gives $\|e_\alpha - e_\beta\|^2 = \|e_\alpha\|^2 + \|e_\beta\|^2 = 2$. Let $r = \sqrt{2}/2$. The open balls $B_r(e_\alpha)$ are pairwise disjoint: a common point $z$ of $B_r(e_\alpha)$ and $B_r(e_\beta)$ would give $\sqrt{2} = \|e_\alpha - e_\beta\| \le \|e_\alpha - z\| + \|z - e_\beta\| < 2r = \sqrt{2}$. Each ball contains a point of $D$, since $e_\alpha$ is a limit of a sequence in $D$. Choosing one such point $d_\alpha \in D \cap B_r(e_\alpha)$ for each $\alpha$ defines a map $\alpha \mapsto d_\alpha$, which is one-to-one because the balls are disjoint. So $\Lambda$ injects into the countable set $D$.

^pf-32-1

*Uses:* [[§24 Orthonormal Sets and Bases#^def-24-5|Def. §24.5]], [[§24 Orthonormal Sets and Bases#^def-24-1|Def. §24.1]], [[§24 Orthonormal Sets and Bases#^lem-24-1|§24.1]], [[§21 Cauchy–Schwarz and the Induced Norm#^thm-21-2|§21.2]], [[§10 Normed Linear Spaces#^def-10-7|Def. §10.7]]

![[m556-24-1.svg]]
*Two orthonormal vectors $e_\alpha$, $e_\beta$ at distance $\sqrt{2}$ (red), the disjoint balls of radius $\sqrt{2}/2$ around them (dashed), and a point $d_\alpha$, $d_\beta$ of the dense set (blue) in each.*

> [!remark]- Connections
> - The countable-basis half of the separability theorem of Chapter 5: [[§24 Orthonormal Sets and Bases#^thm-24-13|§24.13]].
> - The same count in topology: a space with a countable basis has no uncountable discrete subspace ([[§22 Countability Axioms#^lem-22-2|590 Lemma §22.2]]), and a separable metric space has a countable basis ([[§22 Countability Axioms#^prop-22-4|590 Prop. §22.4]]).

Orthonormal vectors are all at distance $\sqrt{2}$ from one another, so balls of radius $\sqrt{2}/2$ around them are disjoint, and each must catch its own point of the dense set. The same argument shows that $L^\infty$ is not separable (MATH 551 notes, Chapter *$L^p$ Spaces*, subsection [[§35 Lᵖ as a Banach Space#Density and Separability|Density and Separability]]).

> [!theorem] Theorem §32.2: $L^2(\mathbb{R}^n)$ is Separable
> $L^2(\mathbb{R}^n)$ is separable, and every orthonormal basis of it is countably infinite.

^thm-32-2

> [!proof]+ Proof
> Separability is now also the case $p = 2$, $E = \mathbb{R}^n$ of Proposition [[§25 Sequence and Function Spaces#^prop-25-4|§25.4]] (Lecture 9). It is proved in the MATH 551 notes (Chapter *$L^p$ Spaces*, subsection [[§35 Lᵖ as a Banach Space#^cor-35-13|Density and Separability]]): finite linear combinations of indicator functions of boxes with rational endpoints, with rational coefficients (with coefficients in $\mathbb{Q} + i\mathbb{Q}$ in the complex case), form a countable dense set. By Proposition [[§32 Position Eigenstates and Continuous Resolutions#^prop-32-1|§32.1]] every orthonormal basis is countable. It is not finite: the normalized indicators of disjoint unit cubes form an infinite orthonormal set, and a finite orthonormal basis $\{e_1, \ldots, e_N\}$ would make every $x$ a finite combination $\sum_{j \le N} (x, e_j) e_j$, so $L^2(\mathbb{R}^n)$ would have dimension at most $N$ and could not contain $N+1$ orthonormal (hence linearly independent) vectors.

^pf-32-2

*Uses:* [[§25 Sequence and Function Spaces#^prop-25-4|§25.4]], [[§35 Lᵖ as a Banach Space#^cor-35-13|551 §35.13]], [[§32 Position Eigenstates and Continuous Resolutions#^prop-32-1|§32.1]], [[§24 Orthonormal Sets and Bases#^def-24-4|Def. §24.4]], [[§24 Orthonormal Sets and Bases#^thm-24-8|§24.8]], [[§4 Span and Linear Independence#^ladr-2-22|LADR 2.22]]

> [!remark]- Connections
> - Separability of $L^p(E)$, proved in Chapter 5: [[§25 Sequence and Function Spaces#^prop-25-4|§25.4]]; its home in measure theory: [[§35 Lᵖ as a Banach Space#^cor-35-13|551 §35.13]].

> [!remark] Remark: There is No Dimension Mismatch
> The *Hilbert dimension* of $H$ is the cardinality of an orthonormal basis; in $L^2(\mathbb{R}^n)$ it is countable, and by [[§32 Position Eigenstates and Continuous Resolutions#^prop-32-1|the theorem]] every orthonormal set, let alone basis, in $L^2(\mathbb{R}^n)$ is countable. So the uncountable family $\{|x\rangle\}$ cannot be an orthonormal set of $L^2$ — and indeed its elements are not in $L^2$ at all, as the next two propositions show. The correct comparison is not “countable basis versus uncountable basis” but “orthonormal basis versus a different kind of object.”

^rem-32-1

## Position Has No Eigenvectors

> [!theorem] Proposition §32.3: Position Has No Eigenvectors
> Let $\psi \in L^2(\mathbb{R})$ and $\lambda \in \mathbb{R}$ satisfy $x\,\psi(x) = \lambda\,\psi(x)$ for almost every $x$. Then $\psi = 0$ in $L^2$.

^prop-32-3

> [!proof]+ Proof
> $(x - \lambda)\psi(x) = 0$ for almost every $x$, so $\psi(x) = 0$ for almost every $x \neq \lambda$. Since $\{\lambda\}$ has measure zero, $\psi = 0$ almost everywhere.

^pf-32-3

> [!remark]- Connections
> - Contrast with finite dimensions, where every self-adjoint operator has an eigenvalue: [[§24 Spectral Theorem#^ladr-7-27|LADR 7.27]].
> - Used in Quantum Field Theory: what $\delta(x - x_0)$ is instead, a generalized function acting on test functions, and one level up, field operators at a point as operator-valued distributions — [[§CA.2 Generalized Functions#^def-ca-2-2|QFT Def. §CA.2.2]], [[§CA.2 Generalized Functions#^rem-ca-2-1|QFT Remark: What changes from the working delta function]], [[§CA.2 Generalized Functions#^def-ca-2-8|QFT Def. §CA.2.8]].

> [!theorem] Proposition §32.4: Point Evaluation is Not Bounded
> Let $x_0 \in \mathbb{R}$. There is no $\psi \in L^2(\mathbb{R})$ with
>
> $$
> (\varphi, \psi) = \varphi(x_0) \qquad \text{for all } \varphi \in C_c(\mathbb{R}) .
> $$

^prop-32-4

> [!proof]+ Proof
> Suppose such $\psi$ exists. By [[§21 Cauchy–Schwarz and the Induced Norm#^thm-21-1|Cauchy–Schwarz]], $|\varphi(x_0)| = |(\varphi, \psi)| \le \|\psi\|_2\,\|\varphi\|_2$ for all $\varphi \in C_c(\mathbb{R})$. Let $\varphi_n$ be the tent function with $\varphi_n(x_0) = 1$, vanishing outside $[x_0 - \frac1n, x_0 + \frac1n]$ and linear in between. Then $0 \le \varphi_n \le 1$, so $\|\varphi_n\|_2^2 \le \frac{2}{n}$, and $1 = |\varphi_n(x_0)| \le \|\psi\|_2 \sqrt{2/n} \to 0$, a contradiction.

^pf-32-4

*Uses:* [[§21 Cauchy–Schwarz and the Induced Norm#^thm-21-1|§21.1]]

![[m556-24-3.svg]]
*The tent functions $\varphi_1, \varphi_2, \varphi_4$ (blue) of the proof. All have $\varphi_n(x_0) = 1$ (red), but $\varphi_n$ lives on $[x_0 - \frac1n, x_0 + \frac1n]$ with $0 \le \varphi_n \le 1$, so $\|\varphi_n\|_2^2$ (for $n = 4$ the shaded area under $\varphi_4^2$) is at most the area $\frac2n$ of the dashed box. A bound $|\varphi(x_0)| \le C\|\varphi\|_2$ would force $\varphi_n(x_0) \to 0$.*

> [!remark]- Connections
> - The idealization this rules out is the delta function of ODEs, [[§30 Impulse Functions#^def-30-3|331 Def. §30.3]], defined there as a limit of unit pulses (with worked examples).
> - Used in Quantum Field Theory: the same obstruction for a one-particle state of sharp momentum, which is not normalizable, and the wave packets and smeared fields that replace it — [[§C2a.4 Particles and Relativistic Normalization#^cau-c2a-4-1|QFT Caution: Plane-wave states are not normalizable]], [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-6|QFT Theorem §C2a.4.6]], [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-8|QFT Theorem §C2a.4.8]].

> [!remark] Remark: What $|x_0\rangle$ Would Have to Be
> In Dirac notation a position eigenstate is characterized by $\langle x_0 | \varphi \rangle = \varphi(x_0)$, i.e. $(\varphi, |x_0\rangle) = \varphi(x_0)$. Proposition [[§32 Position Eigenstates and Continuous Resolutions#^prop-32-4|§32.4]] says no element of $L^2$ does this: the functional $\varphi \mapsto \varphi(x_0)$ is unbounded in the $L^2$ norm, so by the [[§23 Bounded Linear Functionals and the Riesz Representation Theorem#^thm-23-2|Riesz theorem]] it is not a bra, and $|x_0\rangle$ is not a ket. (Point evaluation is not even well defined on $L^2$, whose elements are functions up to sets of measure zero.) The “wavefunction” of $|x_0\rangle$ would be $\delta(x - x_0)$, and the physicists' normalization $\langle x | x' \rangle = \delta(x - x')$ in place of $1$ is the symptom. Proposition [[§32 Position Eigenstates and Continuous Resolutions#^prop-32-3|§32.3]] says the same thing from the operator side: multiplication by $x$ has no eigenvalues at all.

^rem-32-2

## The Position Resolution of the Identity

The object that does exist is the family of projections “$\int_B |x\rangle\langle x|\,dx$”, one for each region $B$.

> [!theorem] Proposition §32.5: The Spectral Projections of Position
> For a measurable set $B \subset \mathbb{R}^n$ define $E(B) : L^2(\mathbb{R}^n) \to L^2(\mathbb{R}^n)$ by $E(B)\psi = \chi_B\,\psi$. Then:
> - (a) $E(B)$ is the orthogonal projection onto the closed subspace $\{ \psi : \psi = 0 \text{ a.e. outside } B \}$;
> - (b) $E(\varnothing) = 0$ and $E(\mathbb{R}^n) = \mathbf{1}$;
> - (c) if $B_1, B_2, \ldots$ are pairwise disjoint with union $B$, then $\sum_k E(B_k) = E(B)$ strongly;
> - (d) $(E(B)\psi, \psi) = \int_B |\psi(x)|^2\,dx$.

^prop-32-5

> [!proof]+ Proof
> Let $Y_B = \{ \psi : \psi = 0 \text{ a.e. outside } B \}$, a linear subspace. It is closed: an $L^2$-convergent sequence has an a.e. convergent subsequence (MATH 551 notes, [[§35 Lᵖ as a Banach Space#^cor-35-10|551 Cor. §35.10]]), so a limit of functions vanishing a.e. outside $B$ vanishes a.e. outside $B$. Its orthogonal complement contains every $\phi$ vanishing a.e. on $B$, since then $(\psi, \phi) = \int \psi\bar{\phi} = 0$ for $\psi \in Y_B$. Now $\psi = \chi_B\psi + \chi_{B^c}\psi$ with $\chi_B\psi \in Y_B$ and $\chi_{B^c}\psi \in Y_B^\perp$, so by uniqueness in Theorem [[§22 Projection and Orthogonal Decomposition#^thm-22-4|§22.4]], $P_{Y_B}\psi = \chi_B\psi$, proving (a). (b) is clear. For (c), $\sum_{k \le N} E(B_k)\psi = \chi_{B_1 \cup \cdots \cup B_N}\psi$, and
>
> $$
> \Bigl\| E(B)\psi - \sum_{k \le N} E(B_k)\psi \Bigr\|^2 = \int_{\bigcup_{k > N} B_k} |\psi|^2 \to 0
> $$
>
> by the [[Dominated Convergence Theorem|dominated convergence theorem]] (the integrand $\chi_{\bigcup_{k>N}B_k}|\psi|^2$ tends to $0$ pointwise and is dominated by $|\psi|^2$). (d) $(\chi_B\psi, \psi) = \int \chi_B |\psi|^2$.

^pf-32-5

*Uses:* [[§35 Lᵖ as a Banach Space#^cor-35-10|551 §35.10]], [[§22 Projection and Orthogonal Decomposition#^def-22-1|Def. §22.1]], [[§22 Projection and Orthogonal Decomposition#^thm-22-4|§22.4]], [[§31 The Completeness Relation#^def-31-2|Def. §31.2]], [[§31 The Completeness Relation#^def-31-1|Def. §31.1]], [[Dominated Convergence Theorem]]

![[m556-24-2.svg]]
*The Born rule, (d): $(E(B)\psi, \psi) = \int_B |\psi(x)|^2\,dx$ is the shaded red area under $|\psi(x)|^2$ over the region $B$ — the probability of finding the particle in $B$.*

> [!remark] Remark: Reading $\int |x\rangle\langle x|\,dx = \mathbf{1}$
> The proposition is the rigorous form of the continuous completeness relation. The symbol $\int_B |x\rangle\langle x|\,dx$ means $E(B)$, a genuine bounded operator even though no $|x\rangle$ is a vector; (b) is “$\int_{\mathbb{R}^n} |x\rangle\langle x|\,dx = \mathbf{1}$”; (c) replaces “summing over basis states” by countable additivity over disjoint regions, again in the strong sense; and (d) is the Born rule — the probability of finding the particle in $B$. A map $B \mapsto E(B)$ with these properties is a *projection-valued measure*. The spectral theorem, later in the course, will attach one to every self-adjoint operator: for an operator with a basis of eigenvectors it is $E(B) = \sum_{\lambda_n \in B} |e_n\rangle\langle e_n|$, for position it is the one above, and in general it mixes both. The kets $|x\rangle$ themselves can be given a rigorous meaning as elements of a larger space of distributions, via a rigged Hilbert space $\mathcal{S} \subset L^2 \subset \mathcal{S}'$; that construction is not needed for anything above.

^rem-32-3

> [!remark] Remark: How the Discrete and Continuous Relations Fit Together
> If $\{e_n\}$ is an orthonormal basis of $L^2(\mathbb{R}^n)$, physics writes $\sum_n e_n(x)\,\overline{e_n(x')} = \delta(x - x')$. Taken literally the left side need not converge anywhere. Integrated against $\varphi(x)$ and $\overline{\chi(x')}$ with $\varphi, \chi \in L^2$, it becomes $\sum_n (\varphi, e_n)(e_n, \chi) = (\varphi, \chi)$, which is Corollary [[§31 The Completeness Relation#^cor-31-4|§31.4]]. So the distributional identity is exactly “inserting a complete set of states”, and countably many $L^2$ functions can “sum to a delta” because the delta is not in $L^2$.

^rem-32-4

> [!remark]- Connections
> - Used in Quantum Mechanics: the eigenfunctions of momentum and of position, with Dirac orthonormality, and the continuous resolution of the identity — [[§B2.2 Observables and Hermitian Operators#^thm-b2-2-6|QM Theorem §B2.2.6]], [[§B2.2 Observables and Hermitian Operators#^thm-b2-2-7|QM Theorem §B2.2.7]]; position eigenkets and position measurements, with what is postulated and what is new, rest on Propositions [[§32 Position Eigenstates and Continuous Resolutions#^prop-32-3|§32.3]]–[[§32 Position Eigenstates and Continuous Resolutions#^prop-32-5|§32.5]] — [[§C2.1 Continuous Spectra and Position Eigenkets#^pr-c2-1-2|QM Principle §C2.1.2]], [[§C2.1 Continuous Spectra and Position Eigenkets#^rem-c2-1-2|QM Remark: What is postulated, and what is new]]; direction eigenkets, modelled on the position eigenstates of Proposition [[§32 Position Eigenstates and Continuous Resolutions#^prop-32-3|§32.3]] — [[§C5.4 Orbital Angular Momentum and Spherical Harmonics as Rotation Matrices#^def-c5-4-1|QM Def. §C5.4.1]]; the propagator, which evolves every wave function through the continuous resolution of Proposition [[§32 Position Eigenstates and Continuous Resolutions#^prop-32-5|§32.5]] — [[§C4.1 Propagators#^thm-c4-1-1|QM Theorem §C4.1.1]].
