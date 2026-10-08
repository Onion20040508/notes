---
type: section
subject: "[[Functional Analysis]]"
chapter: 7
section: 40
tags: [functional-analysis, math556, companion]
---
← [[§39 Position Eigenstates and Continuous Resolutions]] · ↑ [[· 7 Functional Analysis and Quantum Mechanics]]

*Companion — Thread: dimension. Discrete and continuous spectrum.*

> [!theorem] Theorem §40.1: Spectrum of the Hydrogen Atom
> In atomic units, the hydrogen Hamiltonian $H_{\mathrm{hyd}} = -\tfrac12 \Delta - \tfrac{1}{|x|}$ on $L^2(\mathbb{R}^3)$ (spin ignored) is self-adjoint. Its eigenvalues are $E_n = -\tfrac{1}{2n^2}$, $n = 1, 2, \ldots$, with eigenspaces of dimension $n^2$, and its spectrum also contains the continuum $[0, \infty)$, which carries no eigenvectors. In particular the closed linear span $Y_{\mathrm{b}}$ of all eigenfunctions (the bound states) is a proper subspace of $L^2(\mathbb{R}^3)$.

^thm-40-1

> [!proof]+ Proof
> Not covered, and beyond the course: it requires the theory of unbounded self-adjoint operators. Recorded here as physics input; see for instance G. Teschl, *Mathematical Methods in Quantum Mechanics*, the chapter on the hydrogen atom.

^pf-40-1

![[m556-25-1.svg]]
*The hydrogen spectrum drawn in the Coulomb well $V = -1/|x|$ (grey). The eigenvalues $E_n = -\frac{1}{2n^2}$ (blue, each drawn over the region where $V < E_n$, with eigenspace dimension $n^2$) accumulate at $0$; above them lies the continuum $[0, \infty)$ (red), which carries no eigenvectors. Because $V \to 0$ at infinity, nothing confines an electron with $E \ge 0$, and the bound states alone span only the proper subspace $Y_{\mathrm{b}}$.*

> [!theorem] Corollary §40.2: Bound States are Not Complete
> Let $\{\psi_{nlm}\}$ be an orthonormal basis of eigenfunctions of $Y_{\mathrm{b}}$. Then $\{\psi_{nlm}\}$ is not a complete orthonormal set in $L^2(\mathbb{R}^3)$, and there are states $\psi$ with
>
> $$
> \sum_{n,l,m} |(\psi, \psi_{nlm})|^2 < \|\psi\|^2 .
> $$

^cor-40-2

> [!proof]+ Proof
> $Y_{\mathrm{b}}$ is a closed proper subspace, so by Theorem [[§25 Projection and Orthogonal Decomposition#^thm-25-4|§25.4]] its orthogonal complement is nonzero; any $0 \neq \psi \in Y_{\mathrm{b}}^\perp$ is orthogonal to every $\psi_{nlm}$, so the set is not complete. By Theorem [[§27 Orthonormal Sets and Bases#^thm-27-8|§27.8]] it is then not an orthonormal basis and Parseval's equality fails for some $\psi$; with Bessel's inequality (Theorem [[§27 Orthonormal Sets and Bases#^thm-27-5|§27.5]]) the inequality is strict for that $\psi$.

^pf-40-2

*Uses:* [[§40 Bound States Need Not Be Complete꞉ Hydrogen#^thm-40-1|§40.1]], [[§25 Projection and Orthogonal Decomposition#^thm-25-4|§25.4]], [[§27 Orthonormal Sets and Bases#^def-27-2|Def. §27.2]], [[§27 Orthonormal Sets and Bases#^thm-27-8|§27.8]], [[§27 Orthonormal Sets and Bases#^thm-27-5|§27.5]]

> [!remark]- Connections
> - Used in Quantum Mechanics: the bound states of hydrogen (Theorem [[§40 Bound States Need Not Be Complete꞉ Hydrogen#^thm-40-1|§40.1]]) — [[§B5.4 The Hydrogen Atom#^thm-b5-4-2|QM Theorem §B5.4.2]]; why they are not complete (Corollary [[§40 Bound States Need Not Be Complete꞉ Hydrogen#^cor-40-2|§40.2]]) — [[§B5.4 The Hydrogen Atom#^rem-b5-4-6|QM Remark: The bound states are not complete]]; the bound states rederived at level C, with the normalization for all $n$ and $\ell$, beside which the incompleteness is recalled — [[§C6.2 The Coulomb Problem#^thm-c6-2-2|QM Theorem §C6.2.2]], [[§C6.2 The Coulomb Problem#^rem-c6-2-2|QM Remark: What this closes at level B]].

> [!remark] Remark: Physical Reading
> For a normalized state $\psi$, $\sum_{n,l,m} |(\psi, \psi_{nlm})|^2$ is the probability of finding the electron in *some* bound state, and [[§27 Orthonormal Sets and Bases#^thm-27-5|Bessel's inequality]] says it is at most $1$. The deficit $1 - \sum |(\psi, \psi_{nlm})|^2 = \|P_{Y_{\mathrm{b}}^\perp}\psi\|^2$ is the ionization probability. The completeness relation for hydrogen must therefore include the scattering states,
>
> $$
> \sum_{n,l,m} |nlm\rangle\langle nlm| + \int_0^\infty dE\, \sum_{l,m} |E\,l\,m\rangle\langle E\,l\,m| = \mathbf{1},
> $$
>
> where, as with $|x\rangle$, the continuum “states” are not in $L^2$ and the integral stands for a projection-valued measure on $[0,\infty)$. By contrast, a system confined to a compact region (the ring of the example in [[§38 The Completeness Relation#^ex-38-2|§36]], a particle in a box) or by a potential growing at infinity (the harmonic oscillator) has purely discrete spectrum, and its eigenstates alone form an orthonormal basis — as the ring example shows, compactness forces discreteness. Hydrogen's potential decays at infinity, which is what lets the electron escape and creates the continuum.

^rem-40-1

> [!remark] Remark: To Be Continued
> Planned additions as the course proceeds: bounded operators and their adjoints (observables and the dagger, $\langle y | A x \rangle = \langle A^\dagger y | x \rangle$); self-adjoint and unitary operators (observables and time evolution); compact self-adjoint operators and the spectral theorem (the rigorous version of “diagonalize the Hamiltonian”); and the precise relation between the spectrum of an operator and the measurement outcomes of the corresponding observable.
>
> The physicist's versions are in Quantum Mechanics, [[§B2.2 Observables and Hermitian Operators|QM §B2.2]]: Hermitian conjugates and Hermitian operators, [[§B2.2 Observables and Hermitian Operators#^def-b2-2-1|QM Def. §B2.2.1]], and how far Hermitian is from self-adjoint, [[§B2.2 Observables and Hermitian Operators#^cau-b2-2-1|QM Caution: Hermitian is not quite self-adjoint]]; completeness of the eigenfunctions of an observable and when it is a theorem, [[§B2.2 Observables and Hermitian Operators#^pr-b2-2-5|QM Principle §B2.2.5]], [[§B2.2 Observables and Hermitian Operators#^rem-b2-2-1|QM Remark: When completeness is a theorem, and what it requires]]; unitary time evolution, [[§B2.3 The Postulates and the Generalized Statistical Interpretation#^rem-b2-3-2|QM Remark: Time evolution is unitary]]; spectrum and measurement outcomes, [[§B2.3 The Postulates and the Generalized Statistical Interpretation#^pr-b2-3-3|QM Principle §B2.3.3]].

^rem-40-2

> [!remark]- Connections
> - The finite-dimensional versions in LADR: adjoint [[§23 Self-Adjoint and Normal Operators#^ladr-7-1|LADR 7.1]], self-adjoint [[§23 Self-Adjoint and Normal Operators#^ladr-7-10|LADR 7.10]], unitary [[§26 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-51|LADR 7.51]]; spectral theorem: [[Real spectral theorem]], [[Complex spectral theorem]].
