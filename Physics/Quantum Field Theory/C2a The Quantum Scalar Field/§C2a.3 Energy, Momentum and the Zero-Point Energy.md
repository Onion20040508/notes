---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C2a
section: C2a.3
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C2a.2 Mode Expansion and the Mode Algebra]] · ↑ [[· C2a The Quantum Scalar Field]] · [[§C2a.4 Particles and Relativistic Normalization]] →

*Sources: the user's PHY 513 notes, Ch. 4 §§4.6–4.8 · PHY 513 Lecture 4 (Larsen), Part C; Problem Set 3, Problem 2(b), with the course solution · Peskin & Schroeder, An Introduction to Quantum Field Theory, §2.3 · Yu Zhao-Huan, 量子场论讲义, §2.3.3 · the user's pre-course notes, §3.3.*

What are the energy and momentum of the free real field? With the mode expansion and the mode algebra of [[§C2a.2 Mode Expansion and the Mode Algebra|§C2a.2]] ([[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-2|Theorem §C2a.2.2]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|Theorem §C2a.2.6]]), this section reduces $H$ and $\mathbf P$, the charges of time and space translations in their field form ([[§C1b.4 Hamiltonian Field Theory#^thm-c1b-4-2|Theorem §C1b.4.2]], [[§C1b.6 Spacetime Symmetries꞉ Energy–Momentum and Angular Momentum#^thm-c1b-6-6|Theorem §C1b.6.6]], recalled in [[§C2a.1 Canonical Quantization of Fields|§C2a.1]] and collected in [[§C2a.1 Canonical Quantization of Fields#^mod-c2a-1-1|Model §C2a.1.1]]), to one oscillator per momentum, isolates the zero-point energy, and removes it by normal ordering. The ladder relations it ends with are what [[§C2a.4 Particles and Relativistic Normalization|§C2a.4]] reads off as particles; the steps are [[P1 Canonical Quantization#^p1-5|P1, step 5]].

## The Hamiltonian, the zero-point energy and the momentum

> [!theorem] Theorem §C2a.3.1: Hamiltonian in Mode Form
> The Hamiltonian of [[§C2a.1 Canonical Quantization of Fields#^mod-c2a-1-1|Model §C2a.1.1]], $H = \int d^3x\,\bigl[\frac12\pi^2 + \frac12(\nabla\phi)^2 + \frac12m^2\phi^2\bigr]$ (the field form of [[§C1b.4 Hamiltonian Field Theory#^thm-c1b-4-2|Theorem §C1b.4.2]], recalled in [[§C2a.1 Canonical Quantization of Fields|§C2a.1]]), read as an operator in the order written, is in modes
>
> $$
> H = \int\frac{d^3p}{(2\pi)^3}\,\frac{E_{\mathbf p}}{2}\bigl(a_{\mathbf p}a^\dagger_{\mathbf p} + a^\dagger_{\mathbf p}a_{\mathbf p}\bigr) = \int\frac{d^3p}{(2\pi)^3}\,E_{\mathbf p}\,a^\dagger_{\mathbf p}a_{\mathbf p} + E_0 ,
> $$
>
> one oscillator of frequency $E_{\mathbf p}$ per momentum, plus the constant $E_0$ of [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-3|Theorem §C2a.3.3]]. Computed on any time slice it is the same operator.
>
> *Source: the user's PHY 513 notes, Ch. 4 §4.6, eq. (Hfinal) · PHY 513 Lecture 4, Part C · PS §2.3, eq. (2.31) · Yu §2.3.3, eqs. (2.130)–(2.132)*

^thm-c2a-3-1

> [!derivation]- Derivation
> **1. Substitute, keeping distinct variables.** Insert the $t = 0$ forms of [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-2|Theorem §C2a.2.2]], variable $\mathbf p$ in the first factor and $\mathbf p'$ in the second. With $\nabla e^{i\mathbf p\cdot\mathbf x} = i\mathbf p\,e^{i\mathbf p\cdot\mathbf x}$ and $(-i)^2 = -1$, the three terms of $H$ are (each a product of two operator-valued distributions at the same point $\mathbf x$; ⚑ By-product: this coincident product is what produces the $\delta^3(\mathbf 0)$ of step 8 → [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-2|Theorem §C2a.3.2]], [[§CA.2 Generalized Functions#^rem-ca-2-2|Remark: Point splitting]])
>
> $$
> \int d^3x\,\tfrac12\pi^2 = \int d^3x\int\frac{d^3p\,d^3p'}{(2\pi)^6}\Bigl(-\frac{\sqrt{E_{\mathbf p}E_{\mathbf p'}}}{4}\Bigr)\bigl(a_{\mathbf p} - a^\dagger_{-\mathbf p}\bigr)\bigl(a_{\mathbf p'} - a^\dagger_{-\mathbf p'}\bigr)\,e^{i(\mathbf p + \mathbf p')\cdot\mathbf x} ,
> $$
>
> $$
> \int d^3x\,\tfrac12(\nabla\phi)^2 = \int d^3x\int\frac{d^3p\,d^3p'}{(2\pi)^6}\,\frac{(i\mathbf p)\cdot(i\mathbf p')}{4\sqrt{E_{\mathbf p}E_{\mathbf p'}}}\bigl(a_{\mathbf p} + a^\dagger_{-\mathbf p}\bigr)\bigl(a_{\mathbf p'} + a^\dagger_{-\mathbf p'}\bigr)\,e^{i(\mathbf p + \mathbf p')\cdot\mathbf x} ,
> $$
>
> $$
> \int d^3x\,\tfrac12m^2\phi^2 = \int d^3x\int\frac{d^3p\,d^3p'}{(2\pi)^6}\,\frac{m^2}{4\sqrt{E_{\mathbf p}E_{\mathbf p'}}}\bigl(a_{\mathbf p} + a^\dagger_{-\mathbf p}\bigr)\bigl(a_{\mathbf p'} + a^\dagger_{-\mathbf p'}\bigr)\,e^{i(\mathbf p + \mathbf p')\cdot\mathbf x} .
> $$
>
> **2. Do the $d^3x$ integral first.** Exchanging the order of integration ([[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|Theorem §CA.1.1]], in the distributional sense), $\int d^3x\,e^{i(\mathbf p + \mathbf p')\cdot\mathbf x} = (2\pi)^3\delta^3(\mathbf p + \mathbf p')$ in all three terms. *Sense:* the delta is an identity in $\mathcal S'$ in $\mathbf p + \mathbf p'$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]]); the exchange is Fubini for wave packets ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-6|Theorem §CA.3.6]]), applied here to matrix elements between wave-packet states, where the operator coefficients become Schwartz functions of $\mathbf p$, $\mathbf p'$ ([[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-7|Theorem §C2a.2.7]], 2).
>
> **3. Integrate the delta.** The $\mathbf p'$ integral sets $\mathbf p' = -\mathbf p$, eliminating $\mathbf p'$ and one $(2\pi)^3$ (δ acting in $\mathbf p'$; the result is an identity of quadratic forms between wave-packet states, as in step 2). What changes: $E_{\mathbf p'} \to E_{-\mathbf p} = E_{\mathbf p}$, so $\sqrt{E_{\mathbf p}E_{\mathbf p'}} \to E_{\mathbf p}$; $a_{\mathbf p'} \to a_{-\mathbf p}$; $a^\dagger_{-\mathbf p'} \to a^\dagger_{\mathbf p}$; $(i\mathbf p)\cdot(i\mathbf p') \to (i\mathbf p)\cdot(-i\mathbf p) = \mathbf p^2$:
>
> $$
> H = \int\frac{d^3p}{(2\pi)^3}\Bigl[-\frac{E_{\mathbf p}}{4}\bigl(a_{\mathbf p} - a^\dagger_{-\mathbf p}\bigr)\bigl(a_{-\mathbf p} - a^\dagger_{\mathbf p}\bigr) + \frac{\mathbf p^2 + m^2}{4E_{\mathbf p}}\bigl(a_{\mathbf p} + a^\dagger_{-\mathbf p}\bigr)\bigl(a_{-\mathbf p} + a^\dagger_{\mathbf p}\bigr)\Bigr] .
> $$
>
> **4. Mass shell.** $\mathbf p^2 + m^2 = E_{\mathbf p}^2$, so the second coefficient is $E_{\mathbf p}/4$, the same as the first. ⚑ By-product: this equality of coefficients is the mass-shell relation, and it is what makes the cancellation of step 6 possible → [[§C2a.2 Mode Expansion and the Mode Algebra#^rem-c2a-2-1|Remark: Why the frequency is the energy]].
>
> **5. Expand both products into all four terms.** Keeping the order of operators:
>
> $$
> \bigl(a_{\mathbf p} - a^\dagger_{-\mathbf p}\bigr)\bigl(a_{-\mathbf p} - a^\dagger_{\mathbf p}\bigr) = a_{\mathbf p}a_{-\mathbf p} - a_{\mathbf p}a^\dagger_{\mathbf p} - a^\dagger_{-\mathbf p}a_{-\mathbf p} + a^\dagger_{-\mathbf p}a^\dagger_{\mathbf p} ,
> $$
>
> $$
> \bigl(a_{\mathbf p} + a^\dagger_{-\mathbf p}\bigr)\bigl(a_{-\mathbf p} + a^\dagger_{\mathbf p}\bigr) = a_{\mathbf p}a_{-\mathbf p} + a_{\mathbf p}a^\dagger_{\mathbf p} + a^\dagger_{-\mathbf p}a_{-\mathbf p} + a^\dagger_{-\mathbf p}a^\dagger_{\mathbf p} .
> $$
>
> **6. Combine with coefficients $-E_{\mathbf p}/4$ and $+E_{\mathbf p}/4$.** The $a_{\mathbf p}a_{-\mathbf p}$ terms: $-1 + 1 = 0$. The $a^\dagger_{-\mathbf p}a^\dagger_{\mathbf p}$ terms: $-1 + 1 = 0$. The $a_{\mathbf p}a^\dagger_{\mathbf p}$ terms: $+1 + 1 = 2$. The $a^\dagger_{-\mathbf p}a_{-\mathbf p}$ terms: $+1 + 1 = 2$. Hence
>
> $$
> H = \int\frac{d^3p}{(2\pi)^3}\,\frac{E_{\mathbf p}}{2}\Bigl(a_{\mathbf p}a^\dagger_{\mathbf p} + a^\dagger_{-\mathbf p}a_{-\mathbf p}\Bigr) .
> $$
>
> The dropped terms would create or destroy two quanta of opposite momenta; they cancel between the kinetic and the gradient-plus-mass terms.
>
> **7. Relabel.** In the second term substitute $\mathbf p \to -\mathbf p$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|Theorem §CA.3.7]], 1): Jacobian 1, $E_{-\mathbf p} = E_{\mathbf p}$, $a^\dagger_{-\mathbf p}a_{-\mathbf p} \to a^\dagger_{\mathbf p}a_{\mathbf p}$. This gives the first form in the statement. ⚑ By-product: the ordering that comes out is the symmetric one, $\frac12(aa^\dagger + a^\dagger a)$, inherited from writing $H$ in $\phi$ and $\pi$ before quantizing; it is a choice → [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^rem-c2a-3-2|Remark: Normal ordering is a choice of quantization]].
>
> **8. Reorder.** By [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|Theorem §C2a.2.6]], $a_{\mathbf p}a^\dagger_{\mathbf p} = a^\dagger_{\mathbf p}a_{\mathbf p} + [a_{\mathbf p}, a^\dagger_{\mathbf p}] = a^\dagger_{\mathbf p}a_{\mathbf p} + (2\pi)^3\delta^3(\mathbf 0)$. So
>
> $$
> H = \int\frac{d^3p}{(2\pi)^3}\,E_{\mathbf p}\,a^\dagger_{\mathbf p}a_{\mathbf p} + \int\frac{d^3p}{(2\pi)^3}\,\frac{E_{\mathbf p}}{2}\,(2\pi)^3\delta^3(\mathbf 0) .
> $$
>
> ⚑ By-product: the second term is an infinite c-number, the zero-point energy $E_0$ → [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-3|Theorem §C2a.3.3]]. As written it has no value at all: $\delta^3(\mathbf 0)$ is δ at its singular point, and only a box and a cutoff make it a number → [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-2|Theorem §C2a.3.2]].
>
> **9. Any time slice: the four kinds of term.** Use the time-dependent expansion $\phi = \int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}\sum_{s = \pm}c^s_{\mathbf p}\,e^{is\,p\cdot x}$, with $c^-_{\mathbf p} = a_{\mathbf p}$, $c^+_{\mathbf p} = a^\dagger_{\mathbf p}$, $p^0 = E_{\mathbf p}$. Since $p\cdot x = E_{\mathbf p}t - \mathbf p\cdot\mathbf x$, $\partial_te^{is\,p\cdot x} = isE_{\mathbf p}\,e^{is\,p\cdot x}$ and $\nabla e^{is\,p\cdot x} = -is\,\mathbf p\,e^{is\,p\cdot x}$. Each of $\frac12\pi^2$, $\frac12(\nabla\phi)^2$, $\frac12m^2\phi^2$ is then a double integral over $\mathbf p$, $\mathbf q$ of $c^s_{\mathbf p}c^{s'}_{\mathbf q}\,e^{i(s\,p + s'q)\cdot x}/(2\cdot2\sqrt{E_{\mathbf p}E_{\mathbf q}})$ times, respectively, $(isE_{\mathbf p})(is'E_{\mathbf q})$, $(-is\mathbf p)\cdot(-is'\mathbf q)$ and $m^2$; together
>
> $$
> \mathcal H = \int\frac{d^3p\,d^3q}{(2\pi)^6}\sum_{s, s'}\frac{-ss'(E_{\mathbf p}E_{\mathbf q} + \mathbf p\cdot\mathbf q) + m^2}{4\sqrt{E_{\mathbf p}E_{\mathbf q}}}\;c^s_{\mathbf p}c^{s'}_{\mathbf q}\,e^{i(s\,p + s'q)\cdot x} .
> $$
>
> **10. The $d^3x$ integral at time $t$.** $\int d^3x\,e^{i(s\,p + s'q)\cdot x} = e^{i(sE_{\mathbf p} + s'E_{\mathbf q})t}(2\pi)^3\delta^3(s\mathbf p + s'\mathbf q)$ ([[§C2a.2 Mode Expansion and the Mode Algebra#^rem-c2a-2-2|Remark: Two bookkeeping rules]]; an identity in $\mathcal S'$, [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]], with the phase moved out by [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-6|Theorem §CA.3.6]]; the prefactors are smooth, so each delta acts through its support, [[§CA.2 Generalized Functions#^thm-ca-2-7|Theorem §CA.2.7]], 1). For $s' = s$ the delta sets $\mathbf q = -\mathbf p$: $ss' = 1$, $\mathbf p\cdot\mathbf q = -\mathbf p^2$, numerator $-E_{\mathbf p}^2 + \mathbf p^2 + m^2$, phase $e^{2isE_{\mathbf p}t}$, operators $a_{\mathbf p}a_{-\mathbf p}$ ($s = -$) or $a^\dagger_{\mathbf p}a^\dagger_{-\mathbf p}$ ($s = +$). For $s' = -s$ it sets $\mathbf q = \mathbf p$: $ss' = -1$, $\mathbf p\cdot\mathbf q = \mathbf p^2$, numerator $E_{\mathbf p}^2 + \mathbf p^2 + m^2$, phase $1$, operators $a_{\mathbf p}a^\dagger_{\mathbf p}$ and $a^\dagger_{\mathbf p}a_{\mathbf p}$. In both cases $\sqrt{E_{\mathbf p}E_{\mathbf q}} = E_{\mathbf p}$, and (Yu eq. (2.130))
>
> $$
> H = \frac12\int\frac{d^3p}{(2\pi)^3\,2E_{\mathbf p}}\Bigl[(E_{\mathbf p}^2 + \mathbf p^2 + m^2)\bigl(a_{\mathbf p}a^\dagger_{\mathbf p} + a^\dagger_{\mathbf p}a_{\mathbf p}\bigr) + (-E_{\mathbf p}^2 + \mathbf p^2 + m^2)\bigl(a_{\mathbf p}a_{-\mathbf p}e^{-2iE_{\mathbf p}t} + a^\dagger_{\mathbf p}a^\dagger_{-\mathbf p}e^{2iE_{\mathbf p}t}\bigr)\Bigr] .
> $$
>
> **11. Mass shell again.** The mass shell makes the second coefficient $0$ and the first $2E_{\mathbf p}^2$: all $t$-dependence sits in terms whose coefficient vanishes, and the result equals step 6. ⚑ By-product: $H$ is the same operator on every slice (energy conservation of the free field), and it is the mass shell at work → [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-1|Theorem §C2a.3.1]] (last sentence of the statement).
>
> **What the derivation shows**
> - Each $\mathbf p$ is one oscillator of frequency $E_{\mathbf p}$; the cancellation of the number-changing terms needs the mass shell (steps 4, 6, 11).
> - The symmetric ordering of step 7 is inherited, not forced; reordering it produced the zero-point energy ([[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-3|Theorem §C2a.3.3]]), which normal ordering removes ([[§C2a.3 Energy, Momentum and the Zero-Point Energy#^def-c2a-3-1|Def. §C2a.3.1]]).
> - Assumptions actually used: the equal-time algebra, exchange of the $\mathbf x$ and momentum integrals, $E_{-\mathbf p} = E_{\mathbf p}$.
> - Used next: the ladder relations ([[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-6|Theorem §C2a.3.6]]) and the spectrum ([[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-2|Theorem §C2a.4.2]]).

^der-c2a-3-1

*Uses:* [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-2|Theorem §C2a.2.2]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|Theorem §C2a.2.6]], [[§C2a.2 Mode Expansion and the Mode Algebra#^rem-c2a-2-2|Remark: Two bookkeeping rules]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-4|Theorem §CA.3.4]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-6|Theorem §CA.3.6]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|Theorem §CA.3.7]], [[§CA.2 Generalized Functions#^thm-ca-2-7|Theorem §CA.2.7]], [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|Theorem §CA.1.1]]

*Procedure:* [[P1 Canonical Quantization#^p1-5|P1, step 5]]

> [!theorem] Theorem §C2a.3.2: δ³(0) Has No Value; in a Box It Is the Volume
> 1. The constant $[a_{\mathbf p}, a^\dagger_{\mathbf p}] = (2\pi)^3\delta^3(\mathbf 0)$ left by the reordering in [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-1|Theorem §C2a.3.1]] is δ evaluated at its singular point. It has no value, and $H$ in the order written is not an operator on the Fock space: $\langle0|H|0\rangle$ is not a number.
> 2. In a periodic box of volume $V = L^3$, with momenta $\mathbf k \in (2\pi/L)\mathbb Z^3$, $[a_{\mathbf k}, a^\dagger_{\mathbf k'}] = V\delta_{\mathbf k\mathbf k'}$ and a cutoff $|\mathbf k| < \Lambda$, the same reordering leaves the number
>
> $$
> E_0(V, \Lambda) = \langle0|H_V|0\rangle = \frac12\sum_{|\mathbf k| < \Lambda}E_{\mathbf k}, \qquad \frac{E_0(V, \Lambda)}{V} \xrightarrow{V\to\infty} \int_{|\mathbf p| < \Lambda}\frac{d^3p}{(2\pi)^3}\,\frac{E_{\mathbf p}}{2} .
> $$
>
> "$(2\pi)^3\delta^3(\mathbf 0) = V$" is the dictionary entry $V\delta_{\mathbf k\mathbf k} = V \leftrightarrow (2\pi)^3\delta^3(\mathbf 0)$, and "$E_0 = \langle0|H|0\rangle$" means $E_0(V, \Lambda)$.
>
> *Source: the user's PHY 513 notes, Ch. 4 §4.6 ("$(2\pi)^3\delta^3(0) = \int d^3x = V$ is the volume of space"), §4.5 (discrete modes), Ch. 6 §6.2 ("Why this matters beyond tidiness") · the box version written here*

^thm-c2a-3-2

> [!derivation]- Derivation
> **1. Why there is no value.** Replace $\delta^3$ by a nascent delta $\rho_\varepsilon(\mathbf u) = \varepsilon^{-3}\rho(\mathbf u/\varepsilon)$, $\int\rho = 1$ ([[§CA.2 Generalized Functions#^thm-ca-2-4|Theorem §CA.2.4]], 3). At the coincident label $\mathbf u = \mathbf p - \mathbf p = \mathbf 0$ the would-be value is $\varepsilon^{-3}\rho(\mathbf 0)$: it diverges as $\varepsilon \to 0^+$, and its size depends on the shape $\rho$ chosen ([[§CA.2 Generalized Functions#^thm-ca-2-8|Theorem §CA.2.8]], 3). A distribution has values only through test functions, and evaluation at a point of its singular support is not one of them. So $E_0 = \int\frac{d^3p}{(2\pi)^3}\frac{E_{\mathbf p}}2(2\pi)^3\delta^3(\mathbf 0)$ is not a number, and since $a_{\mathbf p}|0\rangle = 0$ it is all of $\langle0|H|0\rangle$.
>
> **2. Put the field in a box.** Take periodic boundary conditions on a cube of side $L$. The modes $e^{i\mathbf k\cdot\mathbf x}$ with $\mathbf k \in (2\pi/L)\mathbb Z^3$ satisfy
>
> $$
> \int_Vd^3x\,e^{i(\mathbf k - \mathbf k')\cdot\mathbf x} = V\,\delta_{\mathbf k\mathbf k'}
> $$
>
> ([[§CA.2 Generalized Functions#^thm-ca-2-9|Theorem §CA.2.9]]): an honest integral, with an honest value at $\mathbf k = \mathbf k'$. The mode expansion of [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-2|Theorem §C2a.2.2]] becomes $\phi(\mathbf x) = \frac1V\sum_{\mathbf k}\frac{a_{\mathbf k} + a^\dagger_{-\mathbf k}}{\sqrt{2E_{\mathbf k}}}e^{i\mathbf k\cdot\mathbf x}$, i.e. $\int\frac{d^3p}{(2\pi)^3} \to \frac1V\sum_{\mathbf k}$.
>
> **3. The box algebra and Hamiltonian.** Repeating [[§C2a.2 Mode Expansion and the Mode Algebra#^der-c2a-2-6|Derivation §C2a.2.6]] with $V\delta_{\mathbf k\mathbf k'}$ in place of $(2\pi)^3\delta^3(\mathbf k - \mathbf k')$ gives $[a_{\mathbf k}, a^\dagger_{\mathbf k'}] = V\delta_{\mathbf k\mathbf k'}$; repeating [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^der-c2a-3-1|Derivation §C2a.3.1]], steps 1–7, with the same replacement gives
>
> $$
> H_V = \frac1V\sum_{\mathbf k}\frac{E_{\mathbf k}}{2}\bigl(a_{\mathbf k}a^\dagger_{\mathbf k} + a^\dagger_{\mathbf k}a_{\mathbf k}\bigr) .
> $$
>
> **4. Reorder.** $a_{\mathbf k}a^\dagger_{\mathbf k} = a^\dagger_{\mathbf k}a_{\mathbf k} + V$, so
>
> $$
> H_V = \frac1V\sum_{\mathbf k}E_{\mathbf k}\,a^\dagger_{\mathbf k}a_{\mathbf k} + \frac12\sum_{\mathbf k}E_{\mathbf k} .
> $$
>
> The constant is the sum of the ground-state energies $\frac12E_{\mathbf k}$, one per mode. With the cutoff $|\mathbf k| < \Lambda$ the sum has finitely many terms, so $E_0(V, \Lambda)$ is a number, and $\langle0|H_V|0\rangle = E_0(V, \Lambda)$ because $a_{\mathbf k}|0\rangle = 0$.
>
> **5. The infinite-volume limit.** Each lattice point owns a cell of volume $(2\pi/L)^3 = (2\pi)^3/V$ in momentum space, so $\frac1V\sum_{|\mathbf k|<\Lambda}F(\mathbf k) = \sum_{|\mathbf k|<\Lambda}\frac{(2\pi/L)^3}{(2\pi)^3}F(\mathbf k)$ is a Riemann sum of $\int_{|\mathbf p|<\Lambda}\frac{d^3p}{(2\pi)^3}F$ and converges to it as $L \to \infty$ for continuous $F$. With $F = E_{\mathbf k}/2$ this is the limit of the statement. ⚑ By-product: $E_0$ needs two regulators; at fixed $\Lambda$ the density $E_0/V$ is finite, and as $\Lambda \to \infty$ it diverges like $\Lambda^4$ → [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-3|Theorem §C2a.3.3]].
>
> **6. The dictionary.** Comparing step 4 with [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^der-c2a-3-1|Derivation §C2a.3.1]], step 8: $\frac1V\sum_{\mathbf k}$ stands for $\int\frac{d^3p}{(2\pi)^3}$ and $V\delta_{\mathbf k\mathbf k'}$ for $(2\pi)^3\delta^3(\mathbf k - \mathbf k')$, so the continuum constant $\int\frac{d^3p}{(2\pi)^3}\frac{E_{\mathbf p}}2(2\pi)^3\delta^3(\mathbf 0)$ is the image of $\frac1V\sum_{\mathbf k}\frac{E_{\mathbf k}}2V$: the coincident value $(2\pi)^3\delta^3(\mathbf 0)$ corresponds to $V\delta_{\mathbf k\mathbf k} = V$ ([[§CA.2 Generalized Functions#^thm-ca-2-9|Theorem §CA.2.9]]).
>
> **What the derivation shows**
> - $\delta^3(\mathbf 0)$ is not a large number but an undefined one; the box replaces it by the volume, the cutoff makes the mode sum finite, and only then is $E_0 = \langle0|H|0\rangle$ a number.
> - The physical content is the density $E_0/V$ at fixed cutoff; the volume factor says the zero-point energy is extensive.
> - Normal ordering removes exactly this constant, and what is left is a genuine operator ([[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-5|Theorem §C2a.3.5]]); for the charge the analogous constant counts modes ([[§C2a.5 The Complex Scalar Field and Its Charge#^der-c2a-5-6|Derivation §C2a.5.6]], step 6).

^der-c2a-3-2

*Uses:* [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-1|Theorem §C2a.3.1]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-2|Theorem §C2a.2.2]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|Theorem §C2a.2.6]], [[§CA.2 Generalized Functions#^thm-ca-2-4|Theorem §CA.2.4]], [[§CA.2 Generalized Functions#^thm-ca-2-8|Theorem §CA.2.8]], [[§CA.2 Generalized Functions#^thm-ca-2-9|Theorem §CA.2.9]]

*Procedure:* [[P1 Canonical Quantization#^p1-5|P1, step 5]]

> [!theorem] Theorem §C2a.3.3: The Zero-Point Energy
> The constant in [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-1|Theorem §C2a.3.1]] is the vacuum energy $E_0 = \langle0|H|0\rangle$ of the unordered Hamiltonian, a sum of $\frac12E_{\mathbf p}$ over all modes:
>
> $$
> E_0 = V\int\frac{d^3p}{(2\pi)^3}\,\frac{E_{\mathbf p}}{2}, \qquad V = (2\pi)^3\delta^3(\mathbf 0) = \int d^3x .
> $$
>
> It diverges twice: in the infrared, in proportion to the volume $V$ of space; in the ultraviolet, through the energy density $\varepsilon_0 = E_0/V$, which with a momentum cutoff $\Lambda \gg m$ is $\varepsilon_0 \approx \Lambda^4/16\pi^2$. It is a c-number: it commutes with every operator. (Names in other sources, and the zero-point energies of the other fields: [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^cau-c2a-3-1|Caution: Names for the zero-point energy]].)
>
> *Source: the user's PHY 513 notes, Ch. 4 §4.6 (Caution "The zero-point energy") · PS §2.3, after eq. (2.31) · Yu §2.3.3, eqs. (2.132), (2.134); the cutoff estimate computed here*

^thm-c2a-3-3

> [!derivation]- Derivation
> **1. Where it comes from.** Step 8 of [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^der-c2a-3-1|Derivation §C2a.3.1]]: the reordering $a_{\mathbf p}a^\dagger_{\mathbf p} = a^\dagger_{\mathbf p}a_{\mathbf p} + [a_{\mathbf p}, a^\dagger_{\mathbf p}]$ leaves
>
> $$
> E_0 = \int\frac{d^3p}{(2\pi)^3}\,\frac{E_{\mathbf p}}{2}\,[a_{\mathbf p}, a^\dagger_{\mathbf p}] = \int\frac{d^3p}{(2\pi)^3}\,\frac{E_{\mathbf p}}{2}\,(2\pi)^3\delta^3(\mathbf 0) .
> $$
>
> **2. It is the vacuum energy.** $a_{\mathbf p}|0\rangle = 0$, so $\langle0|\int E_{\mathbf p}a^\dagger_{\mathbf p}a_{\mathbf p}|0\rangle = 0$ and $\langle0|H|0\rangle = E_0\langle0|0\rangle = E_0$. Each mode contributes the oscillator's ground-state energy $\frac12E_{\mathbf p}$ ([[§C2a.1 Canonical Quantization of Fields#^rem-c2a-1-1|Remark: The oscillator, recalled]]), times the density of modes $V\,d^3p/(2\pi)^3$.
>
> **3. $\delta^3(\mathbf 0)$ is a volume.** $(2\pi)^3\delta^3(\mathbf k) = \int d^3x\,e^{i\mathbf k\cdot\mathbf x}$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-4|Theorem §CA.3.4]]); at $\mathbf k = \mathbf 0$ the integrand is $1$, so $(2\pi)^3\delta^3(\mathbf 0) = \int d^3x = V$, infinite for all of space. *Sense:* not an evaluation, since δ has no value at $\mathbf 0$ ([[§CA.2 Generalized Functions#^thm-ca-2-8|Theorem §CA.2.8]], 3) and the plane-wave delta is not a convergent integral ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]]); what holds is the box identity $\int_Vd^3x\,e^{i(\mathbf k - \mathbf k')\cdot\mathbf x} = V\delta_{\mathbf k\mathbf k'}$ at $\mathbf k = \mathbf k'$ ([[§CA.2 Generalized Functions#^thm-ca-2-9|Theorem §CA.2.9]]), worked out in [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-2|Theorem §C2a.3.2]]. In a box of side $L$ the same computation gives $L^3$: the dictionary $(2\pi)^3\delta^3(\mathbf p - \mathbf q) \leftrightarrow V\delta_{\mathbf p\mathbf q}$ of box normalization. ⚑ By-product: the infrared divergence is extensive, an energy density times the volume → [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-3|Theorem §C2a.3.3]] (statement).
>
> **4. The energy density.** With $d^3p = 4\pi p^2\,dp$ for the rotation-invariant integrand,
>
> $$
> \varepsilon_0 = \int\frac{d^3p}{(2\pi)^3}\,\frac{E_{\mathbf p}}{2} = \frac{4\pi}{2(2\pi)^3}\int_0^\infty dp\,p^2\sqrt{p^2 + m^2} = \frac{1}{4\pi^2}\int_0^\infty dp\,p^2\sqrt{p^2 + m^2} ,
> $$
>
> whose integrand grows like $p^3$.
>
> **5. Cut off.** Stop the integral at $p = \Lambda \gg m$. The integral is elementary (computed here; checked numerically),
>
> $$
> \int_0^\Lambda dp\,p^2\sqrt{p^2 + m^2} = \frac{\Lambda(2\Lambda^2 + m^2)\sqrt{\Lambda^2 + m^2}}{8} - \frac{m^4}{8}\ln\frac{\Lambda + \sqrt{\Lambda^2 + m^2}}{m} = \frac{\Lambda^4}{4} + \frac{m^2\Lambda^2}{4} - \frac{m^4}{8}\ln\frac{2\Lambda}{m} + \frac{m^4}{32} + O\Bigl(\frac{m^6}{\Lambda^2}\Bigr) ,
> $$
>
> the expansion following from $\sqrt{\Lambda^2 + m^2} = \Lambda + m^2/2\Lambda - m^4/8\Lambda^3 + \dots$ Equivalently, expanding the integrand, $\sqrt{p^2 + m^2} = p + m^2/2p + O(m^4/p^3)$, gives the two leading terms directly:
>
> $$
> \int_0^\Lambda dp\,p^2\sqrt{p^2 + m^2} = \frac{\Lambda^4}{4} + \frac{m^2\Lambda^2}{4} + O\bigl(m^4\ln(\Lambda/m)\bigr), \qquad \varepsilon_0 = \frac{\Lambda^4}{16\pi^2} + \frac{m^2\Lambda^2}{16\pi^2} + \dots
> $$
>
> ⚑ By-product: the ultraviolet divergence is quartic, dominated by short wavelengths, and does not depend on $m$ at leading order → [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^rem-c2a-3-1|Remark: Why the zero-point energy is dropped]].
>
> **6. A c-number.** $E_0$ multiplies the identity operator, so $[E_0, X] = 0$ for every $X$: it shifts all energies equally and drops out of every commutator, in particular out of the Heisenberg equations ([[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-6|Theorem §C2a.3.6]]).
>
> **What the derivation shows**
> - The zero-point energy is $\frac12E_{\mathbf p}$ per mode; its two divergences are the infinite volume ($\delta^3(\mathbf 0)$) and the unbounded momenta.
> - It is invisible to energy differences and dynamics; only gravity couples to it (the cosmological-constant problem), and boundaries that change the mode sum make differences of it observable (Casimir).
> - Normal ordering is the prescription that sets it to zero ([[§C2a.3 Energy, Momentum and the Zero-Point Energy#^def-c2a-3-1|Def. §C2a.3.1]]); for the charge the analogous constant is not harmless ([[§C2a.5 The Complex Scalar Field and Its Charge#^rem-c2a-5-2|Remark: Why the vacuum must be neutral]]).

^der-c2a-3-3

*Uses:* [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-1|Theorem §C2a.3.1]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|Theorem §C2a.2.6]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-4|Theorem §CA.3.4]], [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-2|Theorem §C2a.3.2]], [[§CA.2 Generalized Functions#^thm-ca-2-8|Theorem §CA.2.8]], [[§CA.2 Generalized Functions#^thm-ca-2-9|Theorem §CA.2.9]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-9|Theorem §CA.3.9]]

> [!caution] Caution: Names for the zero-point energy
> One kind of constant, one letter. These notes write $E_0$ for the zero-point (vacuum) energy of the real scalar field and mark the other fields with a superscript: $2E_0$ for the complex scalar ([[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-4|Theorem §C2a.5.4]]), $E_0^{(\rm P)} = 3E_0$ for the Proca field ([[§C4.4★ Quantizing the Massive Vector Field#^thm-c4-4-6|Theorem §C4.4.6]]), $E_0^{(\gamma)}$ for the covariantly quantized photon, four polarizations at $m = 0$ ([[§C4.6 Covariant Quantization and the Indefinite Metric#^thm-c4-6-10|Theorem §C4.6.10]]), and $E_0^{(\rm D)} = -4E_0$ for the Dirac field ([[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-5|Theorem §C5b.3.5]]). Yu and the user's pre-course notes write $E_{\rm vac}$ for every field (Yu eqs. (2.150), (4.242), (5.269)), Yu keeping $E_0$ for one oscillator; Peskin–Schroeder ("this infinite constant term", after eq. (2.31)), Lecture 4 and the user's PHY 513 notes (Ch. 4 §4.6, Caution "The zero-point energy") leave it unnamed; earlier drafts of this vault wrote $E_{\rm vac}$ for the photon and $E^D_{\rm vac}$ for the Dirac field. Quantum Mechanics uses $E_0 = \frac12\hbar\omega$ for the ground-state energy of one oscillator ([[§B4.1 Ladder Operators and the Spectrum|QM §B4.1]]): the same letter, one mode instead of all of them.
>
> *Source: Yu, eqs. (2.150), (4.242), (5.269) · PS §2.3, p. 22 · the user's PHY 513 notes, Ch. 4 §4.6 · the user's pre-course notes, §3*

^cau-c2a-3-1

> [!theorem] Theorem §C2a.3.4: Momentum in Mode Form
> The field momentum of [[§C2a.1 Canonical Quantization of Fields#^mod-c2a-1-1|Model §C2a.1.1]], $\mathbf P = -\int d^3x\,\pi\nabla\phi$, the Noether charge of spatial translations ([[§C1b.6 Spacetime Symmetries꞉ Energy–Momentum and Angular Momentum#^thm-c1b-6-6|Theorem §C1b.6.6]]; for this field [[§C1b.6 Spacetime Symmetries꞉ Energy–Momentum and Angular Momentum#^ex-c1b-6-1|Example §C1b.6.1]], both recalled in [[§C2a.1 Canonical Quantization of Fields|§C2a.1]]), is in modes
>
> $$
> \mathbf P = \int\frac{d^3p}{(2\pi)^3}\,\mathbf p\;a^\dagger_{\mathbf p}a_{\mathbf p} ,
> $$
>
> with no constant term and no ordering choice needed: the would-be constant $\frac V2\int\frac{d^3p}{(2\pi)^3}\,\mathbf p$ vanishes by reflection symmetry for any rotation-invariant cutoff, and the vacuum carries no momentum.
>
> *Source: the user's PHY 513 notes, Ch. 4 §4.7, eq. (Pfinal) · PHY 513 Lecture 4, Part C ("Comments") · PS §2.3, eq. (2.33) · Yu §2.3.3, eqs. (2.141)–(2.144)*

^thm-c2a-3-4

> [!derivation]- Derivation
> **1. Substitute.** With the $t = 0$ forms, variable $\mathbf p$ in $\pi$ and $\mathbf p'$ in $\nabla\phi$, where $\nabla$ brings down $i\mathbf p'$:
>
> $$
> \mathbf P = -\int d^3x\int\frac{d^3p\,d^3p'}{(2\pi)^6}\,(-i)\sqrt{\frac{E_{\mathbf p}}{2}}\;\frac{i\mathbf p'}{\sqrt{2E_{\mathbf p'}}}\;\bigl(a_{\mathbf p} - a^\dagger_{-\mathbf p}\bigr)\bigl(a_{\mathbf p'} + a^\dagger_{-\mathbf p'}\bigr)\,e^{i(\mathbf p + \mathbf p')\cdot\mathbf x} ,
> $$
>
> with $(-i)(i) = 1$ and the numerical factor $\mathbf p'\sqrt{E_{\mathbf p}}/2\sqrt{E_{\mathbf p'}}$.
>
> **2. The $d^3x$ integral** gives $(2\pi)^3\delta^3(\mathbf p + \mathbf p')$ (an identity in $\mathcal S'$, [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]]; the exchange of integrals as in [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^der-c2a-3-1|Derivation §C2a.3.1]], step 2).
>
> **3. Integrate the delta.** $\mathbf p' = -\mathbf p$ is eliminated; $E_{\mathbf p'} = E_{\mathbf p}$, so the factor becomes $-\mathbf p/2$; $a_{\mathbf p'} \to a_{-\mathbf p}$, $a^\dagger_{-\mathbf p'} \to a^\dagger_{\mathbf p}$:
>
> $$
> \mathbf P = \int\frac{d^3p}{(2\pi)^3}\,\frac{\mathbf p}{2}\,\bigl(a_{\mathbf p} - a^\dagger_{-\mathbf p}\bigr)\bigl(a_{-\mathbf p} + a^\dagger_{\mathbf p}\bigr) .
> $$
>
> **4. Expand into all four terms.**
>
> $$
> \mathbf P = \int\frac{d^3p}{(2\pi)^3}\,\frac{\mathbf p}{2}\,\Bigl(a_{\mathbf p}a_{-\mathbf p} + a_{\mathbf p}a^\dagger_{\mathbf p} - a^\dagger_{-\mathbf p}a_{-\mathbf p} - a^\dagger_{-\mathbf p}a^\dagger_{\mathbf p}\Bigr) .
> $$
>
> **5. The number-changing terms are odd.** Let $I = \int d^3p\;\mathbf p\,a_{\mathbf p}a_{-\mathbf p}$. Substitute $\mathbf p \to -\mathbf p$ (Jacobian 1; [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|Theorem §CA.3.7]], 1, applied to matrix elements between wave packets, where the integrand is a Schwartz function): $I = \int d^3p\,(-\mathbf p)\,a_{-\mathbf p}a_{\mathbf p} = -\int d^3p\;\mathbf p\,a_{\mathbf p}a_{-\mathbf p} = -I$, using $[a_{-\mathbf p}, a_{\mathbf p}] = 0$. So $I = 0$; likewise for $\mathbf p\,a^\dagger_{-\mathbf p}a^\dagger_{\mathbf p}$, using $[a^\dagger, a^\dagger] = 0$. Dropped: odd integrand, by the commutation of the two annihilators (resp. creators). (Contrast [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^der-c2a-3-1|Derivation §C2a.3.1]], step 6, where the mass shell removed them.)
>
> **6. Relabel the third term.** $\mathbf p \to -\mathbf p$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|Theorem §CA.3.7]], 1): $-\mathbf p\,a^\dagger_{-\mathbf p}a_{-\mathbf p} \to +\mathbf p\,a^\dagger_{\mathbf p}a_{\mathbf p}$. Hence
>
> $$
> \mathbf P = \int\frac{d^3p}{(2\pi)^3}\,\frac{\mathbf p}{2}\bigl(a_{\mathbf p}a^\dagger_{\mathbf p} + a^\dagger_{\mathbf p}a_{\mathbf p}\bigr) .
> $$
>
> **7. Reorder.** $a_{\mathbf p}a^\dagger_{\mathbf p} = a^\dagger_{\mathbf p}a_{\mathbf p} + (2\pi)^3\delta^3(\mathbf 0)$ gives $\mathbf P = \int\frac{d^3p}{(2\pi)^3}\mathbf p\,a^\dagger_{\mathbf p}a_{\mathbf p} + \frac V2\int\frac{d^3p}{(2\pi)^3}\,\mathbf p$. The constant is the integral of an odd function over all of $\mathbb R^3$. In the box of [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-2|Theorem §C2a.3.2]] it is $\frac12\sum_{|\mathbf k|<\Lambda}\mathbf k$, which vanishes term by term, $\mathbf k$ cancelling $-\mathbf k$: the lattice and the cutoff ball are symmetric under $\mathbf k \to -\mathbf k$. ⚑ By-product: it vanishes only for a rotation-invariant (in particular, reflection-symmetric) regularization of the divergent integral; with it, the vacuum has $\mathbf P|0\rangle = 0$ → [[§C2a.4 Particles and Relativistic Normalization#^rem-c2a-4-2|Remark: Why the vacuum is the vacuum]].
>
> **What the derivation shows**
> - The Fourier label $\mathbf p$ is the eigenvalue of the momentum operator: it *is* momentum.
> - The number-changing terms die by oddness, not by the mass shell; no ordering prescription is needed.
> - Used next: the ladder relations and the spectrum; the generator property $[\phi(\mathbf x), \mathbf P] = -i\nabla\phi(\mathbf x)$, which follows in one line from the field form $\mathbf P = -\int d^3y\,\pi\nabla\phi$ and Principle §C2a.1.2: $-\int d^3y\,[\phi(\mathbf x), \pi(\mathbf y)]\,\nabla\phi(\mathbf y) = -i\nabla\phi(\mathbf x)$ (with all the Poincaré charges: [[§C3.5 Quantum Poincaré Transformations#^thm-c3-5-13|Theorem §C3.5.13]]), an identity of operator-valued distributions in $\mathbf x$: smeared with $f(\mathbf x)$ it is the pairing of [[§C2a.1 Canonical Quantization of Fields#^thm-c2a-1-3|Theorem §C2a.1.3]], $[\phi(f), \mathbf P] = -i\int d^3x\,f\,\nabla\phi = i\,\phi(\nabla f)$.

^der-c2a-3-4

*Uses:* [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-2|Theorem §C2a.2.2]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|Theorem §C2a.2.6]], [[§C2a.2 Mode Expansion and the Mode Algebra#^rem-c2a-2-2|Remark: Two bookkeeping rules]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-4|Theorem §CA.3.4]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|Theorem §CA.3.7]], [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-2|Theorem §C2a.3.2]], [[§C2a.1 Canonical Quantization of Fields#^thm-c2a-1-3|Theorem §C2a.1.3]]

*Procedure:* [[P1 Canonical Quantization#^p1-5|P1, step 5]]

> [!definition] Definition §C2a.3.1: Normal Ordering
> The **normal-ordered** product $:\!X\!:$ of creation and annihilation operators is the product rearranged with all creation operators to the left of all annihilation operators, as if they commuted, e.g. $:\!a_{\mathbf p}a^\dagger_{\mathbf q}\!: = a^\dagger_{\mathbf q}a_{\mathbf p}$; it is extended linearly to products of fields, $:\!\phi(x)\phi(y)\!:$. For the free field, the Hamiltonian is taken normal ordered, which removes the zero-point energy $E_0$ of [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-3|Theorem §C2a.3.3]]:
>
> $$
> :\!H\!: = \int\frac{d^3p}{(2\pi)^3}\,E_{\mathbf p}\,a^\dagger_{\mathbf p}a_{\mathbf p}, \qquad :\!H\!:|0\rangle = 0 .
> $$
>
> *Notation:* the colons $:\!X\!:$ are those of the user's PHY 513 notes (Ch. 6, $\hat\phi(x)\hat\phi(y) = \,:\!\hat\phi(x)\hat\phi(y)\!:\, + D_W(x - y)$); PS (§4.3) and Yu (§6.3.1, "normal product") write $N(X)$, and the operation is also called Wick ordering. These notes use the colons only.
>
> *Source: the user's PHY 513 notes, Ch. 4 §4.6 (Caution "The zero-point energy") · PHY 513 Lecture 4, Part C · PS §2.3, after eq. (2.31)*

^def-c2a-3-1

> [!remark] Remark: Why the zero-point energy is dropped
> $E_0$ ([[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-3|Theorem §C2a.3.3]]) is infinite twice over, extensive in the volume and quartic in the momentum cutoff. Only energy differences are measured, and $|0\rangle$ is the lowest state whatever the constant, with excitations spaced by $E_{\mathbf p}$; so the lecture "sweeps it under the rug" and defines $H|0\rangle = 0$. The one interaction that sees absolute energy is gravity, and there the discrepancy is the cosmological-constant problem, outside the course. Lorentz invariance gives a second reason: an invariant vacuum has zero four-momentum, so the generators of the Poincaré group are the normal-ordered $H$ and $\mathbf P$ ([[§C3.5 Quantum Poincaré Transformations#^thm-c3-5-7|Theorem §C3.5.7]]). (Boundaries change the mode sum, and differences of zero-point energies are physical: the Casimir force, mentioned in [[§C13.1★ Relativistic Wave Equations and the Klein–Gordon Field#^rem-c13-1-3|QM Remark: What the field repairs, and what it costs]].)
>
> *Source: the user's PHY 513 notes, Ch. 4 §4.6 · PHY 513 Lecture 4, Part C · PS §2.3, pp. 21–22*

^rem-c2a-3-1

> [!remark] Remark: Normal ordering is a choice of quantization
> Classically $a_{\mathbf p}a^{\ast}_{\mathbf p} = a^{\ast}_{\mathbf p}a_{\mathbf p}$, and $\int E_{\mathbf p}\,a^{\ast}_{\mathbf p}a_{\mathbf p}$ has no zero-point term. Writing $H$ in $\phi$ and $\pi$ and *then* promoting to operators produces the symmetric ordering $\frac12(aa^\dagger + a^\dagger a)$; reordering the classical expression first quantizes the same classical theory with no constant (Problem Set 3's prescription "without taking the commutator into account"; its course solution computed the commutator and showed the two routes agree). [[§C2a.1 Canonical Quantization of Fields#^pr-c2a-1-2|Principle §C2a.1.2]] does not fix the order, and normal ordering is a choice made at quantization, not a subtraction afterwards. For the energy the choice is harmless; for the U(1) charge it is forced by physics ([[§C2a.5 The Complex Scalar Field and Its Charge#^rem-c2a-5-2|Remark: Why the vacuum must be neutral]]). The constant itself is $\langle0|H|0\rangle$, built from products of fields at one point: the vacuum two-point function at coincident points ([[§C2b.2 The Wightman Function#^def-c2b-2-1|Def. §C2b.2.1]]); applied to time-ordered products, the same reordering produces the Feynman propagator ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-5|Theorem §C2b.6.5]]).
>
> *Source: the user's PHY 513 notes, Ch. 4 §4.6 · PHY 513 Problem Set 3, Problem 2(b), course solution*

^rem-c2a-3-2

> [!theorem] Theorem §C2a.3.5: The Normal-Ordered Hamiltonian Acts on Wave Packets
> 1. $:\!H\!:|0\rangle = 0$, and for wave packets $g_1, \dots, g_n \in \mathcal S(\mathbb R^3)$
>
> $$
> :\!H\!:\,a^\dagger(g_1)\cdots a^\dagger(g_n)|0\rangle = \sum_{j=1}^n a^\dagger(g_1)\cdots a^\dagger(E\,g_j)\cdots a^\dagger(g_n)|0\rangle, \qquad (E\,g)(\mathbf p) = E_{\mathbf p}\,g(\mathbf p) \in \mathcal S :
> $$
>
> $:\!H\!:$ is an operator on the wave-packet states (a dense set) and maps them to wave-packet states.
> 2. In the box, $H_V = \,:\!H_V\!: + E_0(V, \Lambda)$ exactly. As $V, \Lambda \to \infty$ the matrix elements of $:\!H_V\!:$ between wave packets converge to those of part 1, while $E_0(V, \Lambda)$ diverges: normal ordering removes exactly the part of $H$ that has no limit, the vacuum value of the coincident product.
>
> *Source: the user's PHY 513 notes, Ch. 4 §4.6 (Caution "The zero-point energy"), §4.8 (Caution "Two honesty points": products at a point need normal ordering) · stated and derived here for wave packets*

^thm-c2a-3-5

> [!derivation]- Derivation
> **1. The vacuum.** Every term of $:\!H\!: = \int\frac{d^3p}{(2\pi)^3}E_{\mathbf p}a^\dagger_{\mathbf p}a_{\mathbf p}$ ends in $a_{\mathbf p}$, and $a_{\mathbf p}|0\rangle = 0$.
>
> **2. One particle.** By [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-7|Theorem §C2a.2.7]], 2, $a_{\mathbf p}a^\dagger(g)|0\rangle = g(\mathbf p)|0\rangle$, a Schwartz function of $\mathbf p$ times the vacuum. So
>
> $$
> :\!H\!:\,a^\dagger(g)|0\rangle = \int\frac{d^3p}{(2\pi)^3}E_{\mathbf p}\,g(\mathbf p)\,a^\dagger_{\mathbf p}|0\rangle = a^\dagger(E\,g)|0\rangle
> $$
>
> by [[§C2a.2 Mode Expansion and the Mode Algebra#^def-c2a-2-2|Def. §C2a.2.2]]. For $m > 0$, $E_{\mathbf p}$ is smooth with polynomially bounded derivatives, so $E\,g \in \mathcal S$ ([[§CA.2 Generalized Functions#^thm-ca-2-7|Theorem §CA.2.7]], 1) and the result is again a wave packet, of norm $\int\frac{d^3p}{(2\pi)^3}E_{\mathbf p}^2|g|^2 < \infty$.
>
> **3. $n$ particles.** Move $a_{\mathbf p}$ to the right through $a^\dagger(g_1)\cdots a^\dagger(g_n)$ with $[a_{\mathbf p}, a^\dagger(g_j)] = g_j(\mathbf p)$ (step 2's computation without the vacuum): $a_{\mathbf p}a^\dagger(g_1)\cdots a^\dagger(g_n)|0\rangle = \sum_jg_j(\mathbf p)\prod_{i\ne j}a^\dagger(g_i)|0\rangle$, the last term $a^\dagger(g_1)\cdots a^\dagger(g_n)a_{\mathbf p}|0\rangle$ being $0$. Multiply by $E_{\mathbf p}a^\dagger_{\mathbf p}$ and integrate; $a^\dagger_{\mathbf p}$ commutes with every $a^\dagger(g_i)$ ([[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|Theorem §C2a.2.6]]), so it can be put in the $j$-th place, giving the statement.
>
> **4. The unordered Hamiltonian.** $H = \,:\!H\!: + E_0$ ([[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-1|Theorem §C2a.3.1]]), and $E_0 = \langle0|H|0\rangle$ has no value ([[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-2|Theorem §C2a.3.2]], 1): $H$ does not map $|0\rangle$, or any wave packet, to a vector of the Fock space.
>
> **5. In the box.** By [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^der-c2a-3-2|Derivation §C2a.3.2]], step 4, $H_V - \,:\!H_V\!: = E_0(V, \Lambda)$, a finite number for each $V$, $\Lambda$. The matrix elements of $:\!H_V\!:$ between box wave packets are Riemann sums of the integrals of steps 2–3 and converge to them ([[§C2a.3 Energy, Momentum and the Zero-Point Energy#^der-c2a-3-2|Derivation §C2a.3.2]], step 5); $E_0(V, \Lambda) \approx V\varepsilon_0(\Lambda)$ grows without bound. ⚑ By-product: normal ordering is subtraction of the vacuum expectation value, $:\!H\!: = H - \langle0|H|0\rangle$; in field form it is the point-splitting subtraction $:\!\phi(x)^2\!: = \lim_{y\to x}\bigl[\phi(x)\phi(y) - \langle0|\phi(x)\phi(y)|0\rangle\bigr]$, the subtracted term being the Wightman function at coincident points → [[§CA.2 Generalized Functions#^rem-ca-2-2|Remark: Point splitting]], [[§C2b.2 The Wightman Function#^def-c2b-2-1|Def. §C2b.2.1]].
>
> **What the derivation shows**
> - $:\!H\!:$ is a genuine (unbounded) operator on wave-packet states; $H$ differs from it by a constant that is not a number.
> - The ill-defined product in $H$ is the coincident product of fields; its divergent part is a c-number, the vacuum value, and normal ordering is the prescription that drops it.
> - Used next: the spectrum and the Fock space ([[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-2|Theorem §C2a.4.2]]), and the energy of a one-particle wave packet, $\langle g|:\!H\!:|g\rangle/\langle g|g\rangle$.

^der-c2a-3-5

*Uses:* [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^def-c2a-3-1|Def. §C2a.3.1]], [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-1|Theorem §C2a.3.1]], [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-2|Theorem §C2a.3.2]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|Theorem §C2a.2.6]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-7|Theorem §C2a.2.7]], [[§C2a.2 Mode Expansion and the Mode Algebra#^def-c2a-2-2|Def. §C2a.2.2]], [[§CA.2 Generalized Functions#^thm-ca-2-7|Theorem §CA.2.7]]

> [!theorem] Theorem §C2a.3.6: Ladder Relations
>
> $$
> [H, a^\dagger_{\mathbf p}] = E_{\mathbf p}\,a^\dagger_{\mathbf p}, \quad [H, a_{\mathbf p}] = -E_{\mathbf p}\,a_{\mathbf p}, \qquad [\mathbf P, a^\dagger_{\mathbf p}] = \mathbf p\,a^\dagger_{\mathbf p}, \quad [\mathbf P, a_{\mathbf p}] = -\mathbf p\,a_{\mathbf p} .
> $$
>
> So if $|\psi\rangle$ has energy $E$ and momentum $\mathbf P$, then $a^\dagger_{\mathbf p}|\psi\rangle$ has $E + E_{\mathbf p}$ and $\mathbf P + \mathbf p$, and $a_{\mathbf p}|\psi\rangle$ has $E - E_{\mathbf p}$ and $\mathbf P - \mathbf p$, unless zero.
>
> *Source: the user's PHY 513 notes, Ch. 4 §4.8 · PS §2.3, eq. (2.32) · Yu §2.3.3, eqs. (2.135)–(2.147)*

^thm-c2a-3-6

> [!derivation]- Derivation
> **1. Drop the constant.** $E_0$ is a c-number ([[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-3|Theorem §C2a.3.3]]), so $[H, X] = \bigl[\int\frac{d^3q}{(2\pi)^3}E_{\mathbf q}a^\dagger_{\mathbf q}a_{\mathbf q}, X\bigr]$; the integration variable is renamed $\mathbf q$ to keep it distinct from the label $\mathbf p$.
>
> **2. One number density with a creator.** $[a^\dagger_{\mathbf q}a_{\mathbf q}, a^\dagger_{\mathbf p}] = a^\dagger_{\mathbf q}[a_{\mathbf q}, a^\dagger_{\mathbf p}] + [a^\dagger_{\mathbf q}, a^\dagger_{\mathbf p}]a_{\mathbf q} = a^\dagger_{\mathbf q}(2\pi)^3\delta^3(\mathbf q - \mathbf p) + 0$.
>
> **3. Integrate.** $[H, a^\dagger_{\mathbf p}] = \int\frac{d^3q}{(2\pi)^3}E_{\mathbf q}\,a^\dagger_{\mathbf q}(2\pi)^3\delta^3(\mathbf q - \mathbf p) = E_{\mathbf p}a^\dagger_{\mathbf p}$, the delta eliminating $\mathbf q$. *Sense:* an identity of operator-valued distributions in $\mathbf p$; smeared with $g(\mathbf p)$ it reads $[H, a^\dagger(g)] = a^\dagger(E\,g)$, an identity between operators on wave packets ([[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-7|Theorem §C2a.2.7]], [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-5|Theorem §C2a.3.5]]).
>
> **4. With an annihilator.** $[a^\dagger_{\mathbf q}a_{\mathbf q}, a_{\mathbf p}] = a^\dagger_{\mathbf q}[a_{\mathbf q}, a_{\mathbf p}] + [a^\dagger_{\mathbf q}, a_{\mathbf p}]a_{\mathbf q} = -(2\pi)^3\delta^3(\mathbf q - \mathbf p)\,a_{\mathbf q}$, so $[H, a_{\mathbf p}] = -E_{\mathbf p}a_{\mathbf p}$.
>
> **5. Momentum.** Steps 2–4 with $\mathbf q$ in place of $E_{\mathbf q}$ ([[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-4|Theorem §C2a.3.4]]) give $[\mathbf P, a^\dagger_{\mathbf p}] = \mathbf p\,a^\dagger_{\mathbf p}$ and $[\mathbf P, a_{\mathbf p}] = -\mathbf p\,a_{\mathbf p}$.
>
> **6. Action on eigenstates.** $Ha^\dagger_{\mathbf p}|\psi\rangle = \bigl([H, a^\dagger_{\mathbf p}] + a^\dagger_{\mathbf p}H\bigr)|\psi\rangle = (E + E_{\mathbf p})\,a^\dagger_{\mathbf p}|\psi\rangle$; the other three cases are the same with the corresponding sign.
>
> **What the derivation shows**
> - $a^\dagger_{\mathbf p}$ adds a fixed energy $E_{\mathbf p}$ and momentum $\mathbf p$, whatever the state: the names "creation" and "annihilation" are justified.
> - The zero-point constant plays no role in any commutator.
> - Used next: the spectrum ([[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-2|Theorem §C2a.4.2]]); the time dependence $a_{\mathbf p}(t) = a_{\mathbf p}e^{-iE_{\mathbf p}t}$ ([[§C2b.1 Heisenberg Fields#^thm-c2b-1-1|Theorem §C2b.1.1]]).

^der-c2a-3-6

*Uses:* [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|Theorem §C2a.2.6]], [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-1|Theorem §C2a.3.1]], [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-4|Theorem §C2a.3.4]], [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-3|Theorem §C2a.3.3]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-7|Theorem §C2a.2.7]], [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-5|Theorem §C2a.3.5]]

> [!remark]- Connections
> - The Dirac field has the same constant with the opposite sign, $-\frac12E_{\mathbf p}$ for each of its four fermionic oscillators per momentum, and Lecture 10 removed it by the same normal ordering, returning to the scalar case ("I told you not to worry … it's the same word"); the user's PHY 513 notes cite this section's caution from Ch. 10 — [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-5|Theorem §C5b.3.5]], [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^rem-c5b-3-2|§C5b.3, Remark: Energies are measured from the vacuum]].
> - Quantum Mechanics' box quantization of the same field reaches the same spectrum with $\sum_{\mathbf k}$ and $\delta_{\mathbf k\mathbf k'}$; the continuum version replaces them by $\int d^3p/(2\pi)^3$ and $(2\pi)^3\delta^3$, with $(2\pi)^3\delta^3(\mathbf 0) = V$ the dictionary between them — [[§C13.1★ Relativistic Wave Equations and the Klein–Gordon Field#^thm-c13-1-6|QM Theorem §C13.1.6]].
> - Momentum as the eigenvalue label: the mode-form $\mathbf P$ generates translations of the field, $[\phi, \mathbf P] = -i\nabla\phi$ at equal times (equivalently $[\mathbf P, \phi] = i\nabla\phi$; Quantum Mechanics' box version has the same sign), the field version of momentum as the generator of translations — [[§C2.2 Translation and Momentum as Its Generator#^pr-c2-2-4|QM Principle §C2.2.4]], [[§C13.1★ Relativistic Wave Equations and the Klein–Gordon Field#^thm-c13-1-6|QM Theorem §C13.1.6]], 4. Covariantly, $[\phi, P^\mu] = i\partial^\mu\phi$, with the normal-ordered Noether $P^\mu$ as the generator of quantum translations — [[§C3.5 Quantum Poincaré Transformations#^thm-c3-5-9|Theorem §C3.5.9]], [[§C3.5 Quantum Poincaré Transformations#^thm-c3-5-13|Theorem §C3.5.13]].
> - $\delta^3(\mathbf 0)$ is δ evaluated at its singular point, which has no value; the box identity $\int_Vd^3x\,e^{i(\mathbf k - \mathbf k')\cdot\mathbf x} = V\delta_{\mathbf k\mathbf k'}$ is what gives "$(2\pi)^3\delta^3(\mathbf 0) = V$" a meaning ([[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-2|Theorem §C2a.3.2]]) — [[§CA.2 Generalized Functions#^thm-ca-2-8|Theorem §CA.2.8]], [[§CA.2 Generalized Functions#^thm-ca-2-9|Theorem §CA.2.9]]; nascent deltas show that the would-be value depends on the regulator — [[§CA.2 Generalized Functions#^thm-ca-2-4|Theorem §CA.2.4]].
> - Normal ordering is point splitting seen in modes: both subtract the vacuum value of a product of fields at one point ([[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-5|Theorem §C2a.3.5]]) — [[§CA.2 Generalized Functions#^rem-ca-2-2|Remark: Point splitting]]; products of distributions at a common singular point are undefined in general — [[§CA.2 Generalized Functions#^thm-ca-2-7|Theorem §CA.2.7]].
> - Every "$d^3x$ integral" in the mode computations is the plane-wave delta, an identity in $\mathcal S'$, and Fubini for wave packets — [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-6|Theorem §CA.3.6]]; the relabellings that combine terms are changes of variables with Jacobian 1 — [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|Theorem §CA.3.7]]; "on the support of the delta" is multiplication by a smooth function — [[§CA.2 Generalized Functions#^thm-ca-2-7|Theorem §CA.2.7]].
> - The zero-point energy is the Wightman function at coincident points, the same divergence as the light-cone singularity of $D_W$ — [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^rem-c2b-6-3|Remark: The zero-point energy is the Wightman function at coincident points]], [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-5|Theorem §C2b.3.5]].
> - The zero-point energy density of Theorem §C2a.3.3, of order $\Lambda^4$ with a momentum cutoff, is the most relevant coupling of all; its cutoff sensitivity is the cosmological-constant problem, the extreme case of the naturalness problem that the honors-thesis notes pose for a scalar mass, whose one-loop shift grows like $\Lambda^2$ ([[§R1.5★ Radiative Corrections, Naturalness and the Hierarchy Problem#^thm-r1-5-1|Thesis Thm. §R1.5.1]], [[§R1.5★ Radiative Corrections, Naturalness and the Hierarchy Problem#^def-r1-5-3|Thesis Def. §R1.5.3]]).
