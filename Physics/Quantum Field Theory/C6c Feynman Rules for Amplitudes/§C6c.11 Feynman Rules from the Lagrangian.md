---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C6c
section: C6c.11
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C6c.10 The Linear Sigma Model꞉ Explicit Symmetry Breaking]] · ↑ [[· C6c Feynman Rules for Amplitudes]] · [[§C6c.12 From the Question to the Formula]] →

*Sources: the user's PHY 513 notes, Appendix B "Feynman Rules from the Lagrangian" (2026-11-14; reference material, not from a lecture), sections "The rule", "Why it works", "Complex fields, fermions and vector fields", "Propagators from the quadratic part", "What the rule does not give", paragraph "Correspondence with Yu" · PHY 513, Problem Set 10, Problem 1(a2) (statement: the hint) · Yu Zhao-Huan, 量子场论讲义, §7.2 (after rules 1–12), §7.3, eq. (7.120) and the remark after it, §8.1 (after rule 9) · Peskin & Schroeder, An Introduction to Quantum Field Theory, §4.4, p. 93; §9.4, eqs. (9.51)–(9.58) · the homes cited in each box.*

The lectures derived each set of Feynman rules from contractions: $\phi^4$ theory ([[· C6a Interactions and Correlation Functions|C6a]], [[§C6c.4 First Order꞉ Enumerate, then Filter|§C6c.4]]–[[§C6c.6 Feynman Rules for Amplitudes|§C6c.6]]), Yukawa theory ([[· C6d Feynman Rules for Fermions|C6d]]), QED ([[§C8.4 Feynman Rules for QED|§C8.4]]). Each time the vertex factor came out as $i$ times the coupling in front of the fields, after counting the ways the lines can attach to identical fields. This section states that outcome once, as a rule that applies to any polynomial interaction ([[§C6c.11 Feynman Rules from the Lagrangian#^thm-c6c-11-1|Theorem §C6c.11.1]]), explains why it works ([[§C6c.11 Feynman Rules from the Lagrangian#^thm-c6c-11-2|Theorem §C6c.11.2]]), extends it to complex fields, fermions and vector fields ([[§C6c.11 Feynman Rules from the Lagrangian#^thm-c6c-11-3|Theorem §C6c.11.3]]), reads the propagators off the quadratic part of the Lagrangian in the same way ([[§C6c.11 Feynman Rules from the Lagrangian#^pr-c6c-11-4|Principle §C6c.11.4]]), and lists what the rule does not give ([[§C6c.11 Feynman Rules from the Lagrangian#^cau-c6c-11-2|Caution: What the rule does not give]]). Nothing here is new physics; it is bookkeeping that saves redoing the contractions for every new Lagrangian.

*Provenance.* The source is an appendix of the user's PHY 513 notes, reference material written on 2026-11-14 and not taken from a lecture. For real scalar fields the rule was the hint of Problem Set 10, Problem 1(a2), and is [[§C6c.8 The Linear Sigma Model꞉ Fields with an Internal Index#^thm-c6c-8-4|Theorem §C6c.8.4]], derived there from the counting rule of [[§C6a.14 Feynman Rules for Polynomial Interactions#^thm-c6a-14-2|Theorem §C6a.14.2]]; that theorem stays the home of "the vertex is the derivative" for real scalar fields. This section adds the form of the appendix, a second proof by assignments of lines to field factors, and the extensions. Interactions that contain derivatives of the fields, where the vertex depends on the momenta, are [[§C8.21★ Derivative Couplings and Scalar QED|§C8.21★]].

**Setup and conventions.** An instance of [[§C6a.0 Setups and Observables#^mod-c6a-0-3|Model §C6a.0.3]]: a permanent interaction $\mathcal L = \mathcal L_0 + \mathcal L_{\rm int}$ with $\mathcal L_{\rm int}$ a polynomial in the fields without derivatives, so that $\hat{\mathcal H}_I = -\mathcal L_{\rm int}$ and the Dyson series is $T\exp\bigl(i\int d^4z\,\mathcal L_{\rm int}\bigr)$ in the interaction-picture fields ([[§C6a.1 From Free to Interacting Fields#^thm-c6a-1-5|Theorem §C6a.1.5]], [[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-7|Theorem §C6a.3.7]]); the vertex factor is exact at every order, and the scope of the amplitudes built with it is that of [[§C6c.6 Feynman Rules for Amplitudes#^thm-c6c-6-3|Theorem §C6c.6.3]]. *Conventions* ([[Larsen PHY 513]]): $g = \operatorname{diag}(+,-,-,-)$, $\hbar = c = 1$; real bosonic fields are $\Phi_a$, the index $a$ labelling the species or the components of a multiplet, written downstairs as in the appendix ([[§C6c.8 The Linear Sigma Model꞉ Fields with an Internal Index|§C6c.8]] writes $\Phi^i$; the position has no meaning) and summed when repeated; in $\mathcal L_{\rm int}$ the fields are classical symbols, unhatted, with $\phi^\ast$ the conjugate of a complex field (the operator is $\hat\phi^\dagger$, [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^mod-c1b-2-7|Model §C1b.2.7]], [[§C2a.5 The Complex Scalar Field and Its Charge#^mod-c2a-5-1|Model §C2a.5.1]]); a **vertex factor** is the factor of a vertex in the momentum-space rules, what multiplies $(2\pi)^4\delta^4(\sum p)$ when $n$ distinct lines meet at the vertex ([[§C6a.14 Feynman Rules for Polynomial Interactions#^thm-c6a-14-2|Theorem §C6a.14.2]]); Fourier transforms as in [[§CA.4 Fourier Transforms and Fourier Tricks#^def-ca-4-1|Def. §CA.4.1]].

## The rule

> [!theorem] Theorem §C6c.11.1: The Vertex Factor from the Interaction Lagrangian
> Let $\mathcal L_{\rm int}$ be a polynomial in real bosonic fields $\Phi_a$ with no derivatives. The vertex at which lines of types $a_1, \dots, a_n$ meet has the factor
>
> $$
> V_{a_1\cdots a_n} = i\,\frac{\partial^n\mathcal L_{\rm int}}{\partial\Phi_{a_1}\cdots\partial\Phi_{a_n}}\bigg|_{\Phi = 0} .
> $$
>
> 1. Because the derivative is evaluated at $\Phi = 0$, only the monomials of degree exactly $n$ contribute.
> 2. The order of the derivatives does not matter ([[§6 Equality of Mixed Partials#^thm-6-1|452 Thm. §6.1]]): $V_{a_1\cdots a_n}$ is symmetric in its indices.
> 3. If no term of $\mathcal L_{\rm int}$ contains exactly these fields, the vertex is zero.
>
> *Equivalently,* this is [[§C6c.8 The Linear Sigma Model꞉ Fields with an Internal Index#^thm-c6c-8-4|Theorem §C6c.8.4]] with $\mathcal L_{\rm int} = -V_{\rm int}$: $i\,\partial^n\mathcal L_{\rm int} = -i\,\partial^nV_{\rm int}$. Two checks: $-\frac{\lambda}{4!}\phi^4$ gives $i\,\partial_\phi^4\bigl(-\frac{\lambda}{4!}\phi^4\bigr) = -i\lambda$, and $-\frac{\lambda}{3!}\phi^3$ gives $i\,\partial_\phi^3\bigl(-\frac{\lambda}{3!}\phi^3\bigr) = -i\lambda$. This is why couplings are written with $\frac{1}{n!}$ for $n$ identical fields: the derivative produces $n!$ and cancels it ([[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-4|Theorem §C6c.4.4]], 2).
>
> *Proof:* [[§C6c.8 The Linear Sigma Model꞉ Fields with an Internal Index#^thm-c6c-8-4|Theorem §C6c.8.4]], which derives the formula monomial by monomial from the counting rule $-ic\prod_in_i!$ of [[§C6a.14 Feynman Rules for Polynomial Interactions#^thm-c6a-14-2|Theorem §C6a.14.2]]; a second proof, by the assignments of lines to field factors, is [[§C6c.11 Feynman Rules from the Lagrangian#^thm-c6c-11-2|Theorem §C6c.11.2]].
>
> *Model:* [[§C6a.0 Setups and Observables#^mod-c6a-0-3|Model §C6a.0.3]] with any polynomial interaction without derivatives of real bosonic fields; *applies:* the vertex factors of the Feynman rules, every order; with labelled legs, the symmetry factor of the diagram being separate ([[§C6c.11 Feynman Rules from the Lagrangian#^cau-c6c-11-1|Caution: Labelled legs, not the symmetry factor of the diagram]]); complex fields, fermions, vector fields: [[§C6c.11 Feynman Rules from the Lagrangian#^thm-c6c-11-3|Theorem §C6c.11.3]]; not for interactions with derivatives ([[§C8.21★ Derivative Couplings and Scalar QED#^pr-c8-21-1|Principle §C8.21.1]]). In path-integral language the formula is $i$ times the $n$-th functional derivative of $S_{\rm int}$ with the momentum-conserving delta function stripped; this is a pointer to Lectures 23–26, not yet given, and is not developed here.
>
> *Source: the user's PHY 513 notes, Appendix B, section "The rule", Principle "Vertex factor from the interaction Lagrangian" and the paragraph after it (a principle there, a theorem here because it is derived) · PHY 513, Problem Set 10, Problem 1(a2) (statement, the hint) · checked with `qft-C/tools/rulesL/verify.py`*

^thm-c6c-11-1

*Procedure:* [[P6 Tree Amplitude from a Lagrangian#^p6-2|P6, step 2]]

## Why it works

> [!theorem] Theorem §C6c.11.2: The Vertex Is −i Times the Symmetrized Coefficient
> ![[ph-qft-c6c-11-1.svg]]
> *The case $n = 3$. (a) Three labelled lines of types $a_1, a_2, a_3$ and the three field factors of one term: a complete set of contractions is an assignment of lines to factors. (b) The $3! = 6$ assignments, which are also the six terms that three derivatives produce by the product rule. Added figure.*
>
> Write the part of $\mathcal L_{\rm int}$ of degree $n$ as
>
> $$
> \mathcal L_{\rm int} \supset -\frac{1}{n!}\,c_{b_1\cdots b_n}\,\Phi_{b_1}\cdots\Phi_{b_n} \qquad(\text{summed over } b_1, \dots, b_n) ,
> $$
>
> with any real coefficients $c_{b_1\cdots b_n}$, and let $\bar c_{b_1\cdots b_n} = \frac{1}{n!}\sum_{\sigma\in S_n}c_{b_{\sigma(1)}\cdots b_{\sigma(n)}}$ be the average of $c$ over the $n!$ orderings of its indices. Then:
> 1. the sum is unchanged when $c$ is replaced by $\bar c$: the coefficient may be taken totally symmetric, because the non-symmetric part of $c$ drops out of the sum (the product of commuting fields is symmetric);
> 2. if $c$ is totally symmetric, $V_{a_1\cdots a_n} = -i\,c_{a_1\cdots a_n}$;
> 3. for any $c$, $V_{a_1\cdots a_n} = -i\,\bar c_{a_1\cdots a_n}$: minus $i$ times the average of the coefficient over the $n!$ orderings.
>
> Both sides of the rule of [[§C6c.11 Feynman Rules from the Lagrangian#^thm-c6c-11-1|Theorem §C6c.11.1]] are sums over the same $n!$ assignments of the $n$ lines to the $n$ field factors: a complete set of contractions assigns each line to one factor, and $n$ derivatives pick the factors one after another. The algebraic part of the statement is [[§CA.9 Splitting Pairings and the Exponential Formula#^lem-ca-9-5|Lemma §CA.9.5]].
>
> *Model:* [[§C6a.0 Setups and Observables#^mod-c6a-0-3|Model §C6a.0.3]], real bosonic fields, no derivatives; *applies:* $n$ distinct lines at the vertex (external particles, or lines to other vertices that no symmetry of the diagram exchanges), every order; lines that close on the vertex or run in parallel leave a symmetry factor ([[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-5|Theorem §C6c.4.5]]).
>
> *Source: the user's PHY 513 notes, Appendix B, section "Why it works", Derivation "The derivative counts the contractions" and the sentence after it ("So the vertex is the symmetrized coefficient") · part 3 with its sign written here: the appendix's closing parenthesis says the fourth derivative of a quartic with a non-symmetric coefficient "equals the average of that coefficient over the $4!$ orderings"; with the $-\frac{1}{n!}$ of the term it is minus that average · checked with `qft-C/tools/rulesL/verify.py` (random non-symmetric arrays, $n = 3, 4$)*

^thm-c6c-11-2

> [!derivation]- Derivation
> **Step 1** (part 1: the coefficient may be taken symmetric). For a permutation $\sigma \in S_n$ rename the summation indices, $b_k \to b_{\sigma(k)}$, and then reorder the commuting fields:
>
> $$
> c_{b_1\cdots b_n}\,\Phi_{b_1}\cdots\Phi_{b_n} = c_{b_{\sigma(1)}\cdots b_{\sigma(n)}}\,\Phi_{b_{\sigma(1)}}\cdots\Phi_{b_{\sigma(n)}} = c_{b_{\sigma(1)}\cdots b_{\sigma(n)}}\,\Phi_{b_1}\cdots\Phi_{b_n} \qquad(\text{summed}) .
> $$
>
> The left side does not depend on $\sigma$; averaging the right side over the $n!$ permutations gives $\bar c_{b_1\cdots b_n}\Phi_{b_1}\cdots\Phi_{b_n}$ ([[§CA.9 Splitting Pairings and the Exponential Formula#^lem-ca-9-5|Lemma §CA.9.5]], 1). Example, $n = 2$: $c_{12}\Phi_1\Phi_2 + c_{21}\Phi_2\Phi_1 = (c_{12} + c_{21})\Phi_1\Phi_2$, and only the sum $c_{12} + c_{21} = 2\bar c_{12}$ appears.
>
> **Step 2** (the first-order term). The interaction has no derivatives, so $\hat{\mathcal H}_I = -\mathcal L_{\rm int}$ and the first-order term of the Dyson series is $i\int d^4z\,\mathcal L_{\rm int}$ ([[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-7|Theorem §C6a.3.7]]); its part of degree $n$ is
>
> $$
> -\frac{i}{n!}\int d^4z\;c_{b_1\cdots b_n}\,\hat\Phi_{b_1}(z)\cdots\hat\Phi_{b_n}(z) .
> $$
>
> **Step 3** (the lines). Attach $n$ lines to this vertex, line $k$ of type $a_k$. The lines are distinguishable, by their momenta or by where they lead, even when they are of the same type. Line $k$ brings a function $w_k(z)$: the plane wave $e^{-ip_k\cdot z}$ or $e^{+ip_k\cdot z}$ of an incoming or outgoing particle ([[§C6c.2 Contractions with External Particles#^lem-c6c-2-2|Lemma §C6c.2.2]], [[§C6c.2 Contractions with External Particles#^lem-c6c-2-1|Lemma §C6c.2.1]]), or a propagator $D_F(z - z')$ to another vertex.
>
> **Step 4** (a complete set of contractions is a permutation). Each line contracts with exactly one of the $n$ field factors, and each factor with exactly one line ([[§C6c.3 Wick's Theorem between Particle States#^thm-c6c-3-1|Theorem §C6c.3.1]]). A complete set of contractions is therefore a bijection from the lines to the factors, a permutation $\sigma$ of $n$ objects: line $k$ sits on factor $\sigma(k)$. There are $n!$ of them ([[§C6c.2 Contractions with External Particles#^thm-c6c-2-4|Theorem §C6c.2.4]]); for $n = 3$, written as $(\sigma(1)\,\sigma(2)\,\sigma(3))$,
>
> $$
> (1\,2\,3) , \quad (1\,3\,2) , \quad (2\,1\,3) , \quad (2\,3\,1) , \quad (3\,1\,2) , \quad (3\,2\,1) .
> $$
>
> **Step 5** (a contraction of different species vanishes). The contraction of $\hat\Phi_b(z)$ with a line of type $a$ is $\delta_{ab}\,w(z)$ ([[§C6a.14 Feynman Rules for Polynomial Interactions#^lem-c6a-14-1|Lemma §C6a.14.1]]). The assignment $\sigma$ therefore contributes
>
> $$
> \prod_{k=1}^n\delta_{a_k\,b_{\sigma(k)}}\,w_k(z) :
> $$
>
> it forces $b_{\sigma(k)} = a_k$ for every $k$.
>
> **Step 6** (the sum over the indices). With the deltas of Step 5 the sum over $b_1, \dots, b_n$ leaves one term, the coefficient with the index $a_k$ in slot $\sigma(k)$:
>
> $$
> \sum_{b_1, \dots, b_n}c_{b_1\cdots b_n}\prod_{k=1}^n\delta_{a_k\,b_{\sigma(k)}} = c_{a_{\sigma^{-1}(1)}\cdots a_{\sigma^{-1}(n)}} .
> $$
>
> For $n = 3$ and $\sigma = (2\,3\,1)$ of the figure: $b_2 = a_1$, $b_3 = a_2$, $b_1 = a_3$, and the term is $c_{a_3a_1a_2}$.
>
> **Step 7** (the sum over the assignments). As $\sigma$ runs over $S_n$ so does $\sigma^{-1}$, hence
>
> $$
> \sum_{\sigma\in S_n}c_{a_{\sigma^{-1}(1)}\cdots a_{\sigma^{-1}(n)}} = n!\;\bar c_{a_1\cdots a_n} ,
> $$
>
> and for a symmetric $c$ every one of the $n!$ assignments contributes the same $c_{a_1\cdots a_n}$.
>
> **Step 8** (the vertex factor from the contractions). Steps 2–7 give
>
> $$
> -\frac{i}{n!}\cdot n!\;\bar c_{a_1\cdots a_n}\int d^4z\,\prod_{k=1}^nw_k(z) = -i\,\bar c_{a_1\cdots a_n}\int d^4z\,\prod_{k=1}^nw_k(z) .
> $$
>
> In momentum space the integral of the plane waves is $(2\pi)^4\delta^4(\sum p)$ ([[§CA.4 Fourier Transforms and Fourier Tricks#^thm-ca-4-3|Theorem §CA.4.3]]), and its coefficient, the vertex factor, is $i\cdot\bigl(-\frac{1}{n!}\bigr)\cdot n!\,\bar c_{a_1\cdots a_n} = -i\,\bar c_{a_1\cdots a_n}$: parts 2 and 3.
>
> **Step 9** (the derivatives run over the same assignments). By the product rule $\frac{\partial}{\partial\Phi_{a_1}}$ picks one factor and sets its index to $a_1$, summed over which factor:
>
> $$
> \frac{\partial}{\partial\Phi_{a_1}}\bigl(\Phi_{b_1}\cdots\Phi_{b_n}\bigr) = \sum_{j=1}^n\delta_{a_1b_j}\prod_{l\ne j}\Phi_{b_l} .
> $$
>
> Then $\frac{\partial}{\partial\Phi_{a_2}}$ picks one of the remaining $n - 1$ factors, and so on; after $n$ derivatives no field is left and
>
> $$
> \frac{\partial^n}{\partial\Phi_{a_1}\cdots\partial\Phi_{a_n}}\bigl(\Phi_{b_1}\cdots\Phi_{b_n}\bigr) = \sum_{\sigma\in S_n}\prod_{k=1}^n\delta_{a_k\,b_{\sigma(k)}} ,
> $$
>
> $\sigma(k)$ the factor picked by the $k$-th derivative ([[§CA.9 Splitting Pairings and the Exponential Formula#^lem-ca-9-5|Lemma §CA.9.5]], 2). This is the sum of Step 5 without the functions $w_k$. With Steps 6–7,
>
> $$
> i\,\frac{\partial^n}{\partial\Phi_{a_1}\cdots\partial\Phi_{a_n}}\Bigl(-\frac{1}{n!}\,c_{b_1\cdots b_n}\Phi_{b_1}\cdots\Phi_{b_n}\Bigr) = i\cdot\Bigl(-\frac{1}{n!}\Bigr)\cdot n!\;\bar c_{a_1\cdots a_n} = -i\,\bar c_{a_1\cdots a_n} ,
> $$
>
> the factor of Step 8.
>
> **Step 10** (terms of other degrees). A term of degree $m \ne n$ does not contribute to the derivative at $\Phi = 0$: for $m < n$ the derivative vanishes identically, for $m > n$ fields are left over and vanish at $\Phi = 0$ ([[§CA.9 Splitting Pairings and the Exponential Formula#^lem-ca-9-5|Lemma §CA.9.5]], 4). It does not contribute to the vertex with $n$ distinct lines either: for $m < n$ there are not enough factors, and for $m > n$ the $m - n$ factors left over must contract among themselves, which is another diagram, with a loop at the vertex ([[§C6c.4 First Order꞉ Enumerate, then Filter#^ex-c6c-4-2|Example §C6c.4.2]]).
>
> **What the derivation shows.**
> - The derivative is a bookkeeping device for the contractions: "which factor is this line attached to" is "which factor did this derivative hit".
> - The $\frac{1}{n!}$ in front of a symmetric coefficient is cancelled by the $n!$ assignments, the general form of [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-4|Theorem §C6c.4.4]].
> - With several species the Kronecker deltas of Step 5 select the terms a given set of lines can use → [[§C6c.11 Feynman Rules from the Lagrangian#^ex-c6c-11-1|Example §C6c.11.1]], [[§C6c.11 Feynman Rules from the Lagrangian#^ex-c6c-11-2|Example §C6c.11.2]].
> - The lines were distinct. When they are not, fewer than $n!$ contractions are distinct and a symmetry factor remains → [[§C6c.11 Feynman Rules from the Lagrangian#^cau-c6c-11-1|Caution: Labelled legs, not the symmetry factor of the diagram]].

^der-c6c-11-2

*Uses:* [[§CA.9 Splitting Pairings and the Exponential Formula#^lem-ca-9-5|Lemma §CA.9.5]], [[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-7|Theorem §C6a.3.7]], [[§C6a.1 From Free to Interacting Fields#^thm-c6a-1-5|Theorem §C6a.1.5]], [[§C6c.2 Contractions with External Particles#^lem-c6c-2-1|Lemma §C6c.2.1]], [[§C6c.2 Contractions with External Particles#^lem-c6c-2-2|Lemma §C6c.2.2]], [[§C6c.2 Contractions with External Particles#^thm-c6c-2-4|Theorem §C6c.2.4]], [[§C6c.3 Wick's Theorem between Particle States#^thm-c6c-3-1|Theorem §C6c.3.1]], [[§C6a.14 Feynman Rules for Polynomial Interactions#^lem-c6a-14-1|Lemma §C6a.14.1]], [[§CA.4 Fourier Transforms and Fourier Tricks#^thm-ca-4-3|Theorem §CA.4.3]]

*Procedure:* [[P6 Tree Amplitude from a Lagrangian#^p6-2|P6, step 2]]

> [!example] Example §C6c.11.1: Two Fields: One Lagrangian, Several Vertices
> ![[ph-qft-c6c-11-2.svg]]
> *The vertices of $\mathcal L_{\rm int} = -\frac{\lambda}{4!}\phi^4 - \frac g4\phi^2\chi^2$: (a) four $\phi$ lines, (b) two $\phi$ and two $\chi$ lines, (c) three $\phi$ lines and one $\chi$ line, which no term supplies. Added figure.*
>
> With several fields the derivatives sort out which term feeds which vertex. For two real fields $\phi$, $\chi$ and
>
> $$
> \mathcal L_{\rm int} = -\frac{\lambda}{4!}\,\phi^4 - \frac g4\,\phi^2\chi^2 :
> $$
>
> **Step 1** (four $\phi$ lines). $\partial_\phi^4\phi^4 = 4!$ and $\partial_\phi^4(\phi^2\chi^2) = 0$, so
>
> $$
> V_{\phi\phi\phi\phi} = i\,\partial_\phi^4\,\mathcal L_{\rm int} = i\cdot\Bigl(-\frac{\lambda}{4!}\Bigr)\cdot4! = -i\lambda .
> $$
>
> **Step 2** (two $\phi$ and two $\chi$ lines). $\partial_\phi^2\partial_\chi^2\phi^4 = 0$ and $\partial_\phi^2\partial_\chi^2(\phi^2\chi^2) = 2!\cdot2!$, so
>
> $$
> V_{\phi\phi\chi\chi} = i\,\partial_\phi^2\partial_\chi^2\Bigl(-\frac g4\,\phi^2\chi^2\Bigr) = i\cdot\Bigl(-\frac g4\Bigr)\cdot2!\cdot2! = -ig .
> $$
>
> **Step 3** (three $\phi$ lines and one $\chi$ line). $\partial_\phi^3\partial_\chi\phi^4 = 0$ and $\partial_\phi^3\partial_\chi(\phi^2\chi^2) = 0$, so $V_{\phi\phi\phi\chi} = 0$; likewise $V_{\phi\chi\chi\chi} = V_{\chi\chi\chi\chi} = 0$.
>
> **Step 4** (the normalization). The $\frac14 = \frac{1}{2!\,2!}$ is the natural normalization for a term with two pairs of identical fields. In the form of [[§C6c.11 Feynman Rules from the Lagrangian#^thm-c6c-11-2|Theorem §C6c.11.2]], with $\Phi_1 = \phi$, $\Phi_2 = \chi$: the symmetric coefficient has $c_{1111} = \lambda$ and $c_{1122} = g$ in each of the $\frac{4!}{2!\,2!} = 6$ orderings of the indices $1, 1, 2, 2$, and $-\frac{1}{4!}\cdot6\,g\,\phi^2\chi^2 = -\frac g4\phi^2\chi^2$.
>
> *Model:* [[§C6a.0 Setups and Observables#^mod-c6a-0-3|Model §C6a.0.3]] with two real scalar fields; *applies:* the vertex factors, every order.
>
> *Source: the user's PHY 513 notes, Appendix B, section "Why it works" (first consequence) · Step 4, second half, written here · checked with `qft-C/tools/rulesL/verify.py`*

^ex-c6c-11-1

> [!example] Example §C6c.11.2: A Multiplet: the Coefficient Array of the Linear Sigma Model
> For a multiplet with $\mathcal L_{\rm int} = -\frac{1}{4!}\lambda_{abcd}\Phi_a\Phi_b\Phi_c\Phi_d$ and symmetric $\lambda_{abcd}$, [[§C6c.11 Feynman Rules from the Lagrangian#^thm-c6c-11-2|Theorem §C6c.11.2]], 2, gives $V_{abcd} = -i\lambda_{abcd}$. A Lagrangian written in another form, as a function of invariants like $\Phi_a\Phi_a$, is put into this form by the derivatives; the result is a sum of products of Kronecker deltas that records which legs must carry equal labels.
>
> **Step 1** (the sigma model). For $\mathcal L_{\rm int} = -\frac\lambda4(\Phi_a\Phi_a)^2$ ([[§C6c.8 The Linear Sigma Model꞉ Fields with an Internal Index#^mod-c6c-8-1|Model §C6c.8.1]]) the four derivatives were carried out in [[§C6c.8 The Linear Sigma Model꞉ Fields with an Internal Index#^ex-c6c-8-1|Example §C6c.8.1]]:
>
> $$
> \lambda_{abcd} = -\frac{\partial^4\mathcal L_{\rm int}}{\partial\Phi_a\,\partial\Phi_b\,\partial\Phi_c\,\partial\Phi_d} = 2\lambda\,\bigl(\delta_{ab}\delta_{cd} + \delta_{ac}\delta_{bd} + \delta_{ad}\delta_{bc}\bigr) , \qquad V_{abcd} = -i\lambda_{abcd} ,
> $$
>
> the vertex of [[§C6c.8 The Linear Sigma Model꞉ Fields with an Internal Index#^thm-c6c-8-3|Theorem §C6c.8.3]].
>
> **Step 2** (check: the array reproduces the Lagrangian). Each of the three terms contracts the four fields into $(\Phi_a\Phi_a)^2$:
>
> $$
> -\frac{1}{4!}\,\lambda_{abcd}\,\Phi_a\Phi_b\Phi_c\Phi_d = -\frac{1}{4!}\cdot2\lambda\cdot3\,(\Phi_a\Phi_a)^2 = -\frac\lambda4\,(\Phi_a\Phi_a)^2 .
> $$
>
> **Step 3** (a non-symmetric array for the same Lagrangian). The array $c_{abcd} = 6\lambda\,\delta_{ab}\delta_{cd}$ gives the same term, $-\frac{1}{4!}\cdot6\lambda\,(\Phi_a\Phi_a)^2$, but is not symmetric. Its average over the $24$ orderings sends $\delta_{ab}\delta_{cd}$ to each of the three pairings equally often:
>
> $$
> \bar c_{abcd} = 6\lambda\cdot\frac13\,\bigl(\delta_{ab}\delta_{cd} + \delta_{ac}\delta_{bd} + \delta_{ad}\delta_{bc}\bigr) = \lambda_{abcd} ,
> $$
>
> as [[§C6c.11 Feynman Rules from the Lagrangian#^thm-c6c-11-2|Theorem §C6c.11.2]], 3, requires: the vertex is $-i\bar c_{abcd}$, not $-ic_{abcd}$.
>
> *Model:* [[§C6c.8 The Linear Sigma Model꞉ Fields with an Internal Index#^mod-c6c-8-1|Model §C6c.8.1]]; *applies:* the vertex factor, every order.
>
> *Source: the user's PHY 513 notes, Appendix B, section "Why it works" (second consequence) · the sigma-model array from [[§C6c.8 The Linear Sigma Model꞉ Fields with an Internal Index#^ex-c6c-8-1|Example §C6c.8.1]] (PHY 513, Problem Set 10, Problem 1(a2)) · Steps 2–3 written here · checked with `qft-C/tools/rulesL/verify.py`*

^ex-c6c-11-2

> [!caution] Caution: Labelled legs, not the symmetry factor of the diagram
> The rule gives the vertex with *labelled* legs: $n$ distinct lines, each attached to one field factor. The symmetry factor of a whole diagram, for lines that close on one vertex or several lines that join the same two vertices, is a separate matter and still has to be divided out: $\frac1S$ per diagram ([[§C6a.9 Position-Space Feynman Rules#^thm-c6a-9-1|Theorem §C6a.9.1]], [[§C6a.10 Symmetry Factors in Practice#^thm-c6a-10-1|Theorem §C6a.10.1]], [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-5|Theorem §C6c.4.5]]; [[P5 Symmetry Factor of a Diagram|P5]]). Example: the tadpole of $\phi^4$ theory uses the vertex $-i\lambda$ and carries $\frac12$ ([[§C6c.4 First Order꞉ Enumerate, then Filter#^ex-c6c-4-2|Example §C6c.4.2]]). Tree diagrams of a process have $S = 1$ ([[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^thm-c6c-5-6|Theorem §C6c.5.6]]).
>
> *Source: the user's PHY 513 notes, Appendix B, section "Why it works" (last paragraph)*

^cau-c6c-11-1

## Complex fields, fermions and vector fields

> [!theorem] Theorem §C6c.11.3: The Rule for Complex Fields, Fermions and Vector Fields
> The rule of [[§C6c.11 Feynman Rules from the Lagrangian#^thm-c6c-11-1|Theorem §C6c.11.1]] extends to the other fields of the course:
> 1. **Complex fields.** Treat $\phi$ and $\phi^\ast$ as independent ([[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-9|Theorem §C1b.2.9]]) and differentiate with respect to each. A $\partial/\partial\phi$ is a line whose charge arrow points into the vertex, a $\partial/\partial\phi^\ast$ one whose arrow points out: the factor $\phi$ of the term is the $\hat\phi$ end of its line, and a complex line points from its $\hat\phi^\dagger$ end to its $\hat\phi$ end ([[§C6a.14 Feynman Rules for Polynomial Interactions#^lem-c6a-14-1|Lemma §C6a.14.1]]).
> 2. **Fermions.** Differentiate with respect to $\bar\psi_a$ from the left and $\psi_b$ from the right:
>
> $$
> V_{ab} = i\,\frac{\partial}{\partial\bar\psi_a}\,\mathcal L_{\rm int}\,\frac{\overleftarrow\partial}{\partial\psi_b} .
> $$
>
> The result is a $4\times4$ matrix in spinor space, row index from $\bar\psi$ and column index from $\psi$, which sits in the spinor chain read against the arrow ([[§C6d.2 Contractions with External Fermions#^thm-c6d-2-4|Theorem §C6d.2.4]]). With the derivatives taken this way a bilinear $\bar\psi\,\Gamma\,\psi$ gives $\Gamma$ with no extra sign.
> 3. **Vector fields.** $\partial/\partial A_\mu$ leaves a free index $\mu$, carried by the vector line; it is contracted with the propagator or with the polarization vector ([[§C8.3 Photon Lines꞉ the Quantized Photon Field, Polarizations and the Propagator#^thm-c8-3-5|Theorem §C8.3.5]], [[§C8.4 Feynman Rules for QED#^thm-c8-4-1|Theorem §C8.4.1]]).
>
> *Model:* [[§C6a.0 Setups and Observables#^mod-c6a-0-3|Model §C6a.0.3]] with complex scalar, Dirac and vector fields, interactions without derivatives; *applies:* the vertex factors, every order; part 2 for terms with one $\bar\psi$ and one $\psi$, which is every fermion interaction of the course (Yukawa theory, the pseudoscalar coupling, QED); terms with four or more fermion fields need the signs of the Grassmann derivatives and are not treated; external factors and fermion signs are not part of the rule ([[§C6c.11 Feynman Rules from the Lagrangian#^cau-c6c-11-2|Caution: What the rule does not give]]).
>
> *Source: the user's PHY 513 notes, Appendix B, section "Complex fields, fermions and vector fields", Principle "Extensions" (a principle there, a theorem here: each part is derived, within the scope stated, from the theorems cited in the derivation) · the scope of part 2 written here*

^thm-c6c-11-3

> [!derivation]- Derivation
> **Step 1** (part 1: the derivative of a monomial). A term $-c\,(\phi^\ast)^{\bar m}\phi^m$ differentiated $\bar m$ times with respect to $\phi^\ast$ and $m$ times with respect to $\phi$ gives
>
> $$
> i\,\partial_{\phi^\ast}^{\bar m}\,\partial_\phi^m\bigl(-c\,(\phi^\ast)^{\bar m}\phi^m\bigr) = -ic\;\bar m!\;m! ,
> $$
>
> and any other set of $\bar m + m$ derivatives gives zero at zero field. This is the vertex factor $-ic\prod_km_k!$ of [[§C6a.14 Feynman Rules for Polynomial Interactions#^thm-c6a-14-2|Theorem §C6a.14.2]] with the two kinds $\phi \smile \phi^\dagger$ ([[§C6a.14 Feynman Rules for Polynomial Interactions#^def-c6a-14-1|Def. §C6a.14.1]]): a line attaches only to a leg of the matching kind, the $m$ lines on the $\phi$ legs in $m!$ ways and the $\bar m$ lines on the $\phi^\ast$ legs in $\bar m!$ ways. Example: $-\frac\lambda4(\phi^\ast\phi)^2$ gives $-i\frac\lambda4\cdot2!\cdot2! = -i\lambda$.
>
> **Step 2** (part 1: the arrows). A factor $\hat\phi(z)$ of the vertex contracts with a $\hat\phi^\dagger$ elsewhere, and the line points from its $\hat\phi^\dagger$ end to its $\hat\phi$ end ([[§C6a.14 Feynman Rules for Polynomial Interactions#^lem-c6a-14-1|Lemma §C6a.14.1]]): into the vertex. A factor $\hat\phi^\dagger(z)$ contracts with a $\hat\phi$ elsewhere: the line points out of the vertex. For external lines, $\hat\phi$ absorbs an incoming particle or emits an outgoing antiparticle ([[§C6c.2 Contractions with External Particles#^lem-c6c-2-2|Lemma §C6c.2.2]], 3).
>
> **Step 3** (part 2: no counting). A term $\bar\psi_c\,\Gamma_{cd}\,\psi_d\,X$, with $X$ a product of bosonic fields, has one factor $\bar\psi$ and one factor $\psi$. The line that leaves the vertex can attach only to $\bar\psi$ and the line that arrives only to $\psi$ ([[§C6d.1 Yukawa Theory#^def-c6d-1-1|Def. §C6d.1.1]]): there is one assignment and nothing to count.
>
> **Step 4** (part 2: the derivatives and the sign). The left derivative removes a field standing at the left end of a product, the right derivative one standing at the right end ([[§CB.23 Grassmann Algebras#^def-cb-23-5|Def. §CB.23.5]], [[§CB.23 Grassmann Algebras#^def-cb-23-6|Def. §CB.23.6]]; in the course's use, [[§C5b.1 Canonical Quantization of the Dirac Field#^cau-c5b-1-3|§C5b.1, ★ Caution: Which side a Grassmann derivative acts from]]); neither field has to be moved past another anticommuting symbol, so no sign appears:
>
> $$
> \frac{\partial}{\partial\bar\psi_a}\,\bigl(\bar\psi_c\,\Gamma_{cd}\,\psi_d\bigr)\,\frac{\overleftarrow\partial}{\partial\psi_b} = \delta_{ac}\,\Gamma_{cd}\,\delta_{db} = \Gamma_{ab} .
> $$
>
> The bosonic factor $X$ is differentiated as in [[§C6c.11 Feynman Rules from the Lagrangian#^thm-c6c-11-1|Theorem §C6c.11.1]]. That $i$ times this matrix is the vertex, standing between the wave functions or propagators of its line with the $\bar\psi$ index on the left, is the content of the vertex derivations of Yukawa theory and QED ([[§C6d.1 Yukawa Theory#^thm-c6d-1-3|Theorem §C6d.1.3]], [[§C6d.1 Yukawa Theory#^thm-c6d-1-4|Theorem §C6d.1.4]], [[§C8.4 Feynman Rules for QED#^thm-c8-4-3|Theorem §C8.4.3]]); the reading of the line against its arrow is [[§C6d.2 Contractions with External Fermions#^thm-c6d-2-4|Theorem §C6d.2.4]].
>
> **Step 5** (part 3). The components $A_\mu$, $\mu = 0, \dots, 3$, are real bosonic fields labelled by $\mu$; they contract in pairs or with external photons, without signs ([[§C8.4 Feynman Rules for QED#^thm-c8-4-2|Theorem §C8.4.2]]). So [[§C6c.11 Feynman Rules from the Lagrangian#^thm-c6c-11-1|Theorem §C6c.11.1]] applies with $a = \mu$, and $\frac{\partial A_\nu}{\partial A_\mu} = \delta^\mu{}_\nu$ leaves the index of the line: $\frac{\partial}{\partial A_\mu}\bigl(\bar\psi\gamma^\nu\psi\,A_\nu\bigr) = \bar\psi\gamma^\mu\psi$.
>
> **What the derivation shows.**
> - Part 1 is the counting theorem in the notation of derivatives; parts 2 and 3 restate vertices the course derived by contractions. The derivative form adds nothing to those derivations except a uniform way to write the result.
> - What the fermion derivative leaves out, the signs between diagrams and the external spinors, comes from the order of the operators in the contractions → [[§C6c.11 Feynman Rules from the Lagrangian#^cau-c6c-11-2|Caution: What the rule does not give]].

^der-c6c-11-3

*Uses:* [[§C6c.11 Feynman Rules from the Lagrangian#^thm-c6c-11-1|Theorem §C6c.11.1]], [[§C6a.14 Feynman Rules for Polynomial Interactions#^thm-c6a-14-2|Theorem §C6a.14.2]], [[§C6a.14 Feynman Rules for Polynomial Interactions#^def-c6a-14-1|Def. §C6a.14.1]], [[§C6a.14 Feynman Rules for Polynomial Interactions#^lem-c6a-14-1|Lemma §C6a.14.1]], [[§C6c.2 Contractions with External Particles#^lem-c6c-2-2|Lemma §C6c.2.2]], [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-9|Theorem §C1b.2.9]], [[§C6d.1 Yukawa Theory#^def-c6d-1-1|Def. §C6d.1.1]], [[§C6d.1 Yukawa Theory#^thm-c6d-1-3|Theorem §C6d.1.3]], [[§C6d.1 Yukawa Theory#^thm-c6d-1-4|Theorem §C6d.1.4]], [[§C6d.2 Contractions with External Fermions#^thm-c6d-2-4|Theorem §C6d.2.4]], [[§C8.4 Feynman Rules for QED#^thm-c8-4-2|Theorem §C8.4.2]], [[§C8.4 Feynman Rules for QED#^thm-c8-4-3|Theorem §C8.4.3]], [[§CB.23 Grassmann Algebras#^def-cb-23-5|Def. §CB.23.5]], [[§CB.23 Grassmann Algebras#^def-cb-23-6|Def. §CB.23.6]]

*Procedure:* [[P6 Tree Amplitude from a Lagrangian#^p6-2|P6, step 2]]

> [!example] Example §C6c.11.3: Six Theories
> ![[ph-qft-c6c-11-3.svg]]
> *The six vertices of the table: (a) $\phi^4$, (b) $\phi^3$, (c) the complex scalar, with the arrows of $\partial_\phi$ (into the vertex) and $\partial_{\phi^\ast}$ (out); (d) Yukawa, (e) pseudoscalar Yukawa, (f) QED, with the row index $a$ of $\bar\psi$ on the outgoing arrow and the column index $b$ of $\psi$ on the incoming one. Added figure.*
>
> | theory | $\mathcal L_{\rm int}$ | derivatives | vertex | home |
> |---|---|---|---|---|
> | $\phi^4$ | $-\frac{\lambda}{4!}\phi^4$ | $i\,\partial_\phi^4$ | $-i\lambda$ | [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-4\|Theorem §C6c.4.4]] |
> | $\phi^3$ | $-\frac{\lambda}{3!}\phi^3$ | $i\,\partial_\phi^3$ | $-i\lambda$ | [[§C6a.14 Feynman Rules for Polynomial Interactions#^thm-c6a-14-2\|Theorem §C6a.14.2]] (there with $g$ for $\lambda$) |
> | complex $\lvert\phi\rvert^4$ | $-\frac\lambda4(\phi^\ast\phi)^2$ | $i\,\partial_{\phi^\ast}^2\partial_\phi^2$ | $-i\lambda$ | [[§C6a.14 Feynman Rules for Polynomial Interactions#^thm-c6a-14-2\|Theorem §C6a.14.2]], [[§C6a.9 Position-Space Feynman Rules#^mod-c6a-9-3\|Model §C6a.9.3]] |
> | Yukawa | $-g\,\bar\psi\psi\,\phi$ | $i\,\partial_{\bar\psi_a}\,(\cdot)\,\overleftarrow\partial_{\psi_b}\,\partial_\phi$ | $-ig\,\mathbb 1$ | [[§C6d.1 Yukawa Theory#^thm-c6d-1-3\|Theorem §C6d.1.3]] |
> | pseudoscalar Yukawa | $-ig\,\bar\psi\gamma^5\psi\,\phi$ | the same | $g\,\gamma^5$ | the coupling: [[§C6d.1 Yukawa Theory#^thm-c6d-1-6\|Theorem §C6d.1.6]] |
> | QED | $-e\,\bar\psi\gamma^\mu\psi\,A_\mu$ | $i\,\partial_{\bar\psi_a}\,(\cdot)\,\overleftarrow\partial_{\psi_b}\,\partial_{A_\mu}$ | $-ie\gamma^\mu$ | [[§C8.4 Feynman Rules for QED#^thm-c8-4-3\|Theorem §C8.4.3]] |
>
> The Yukawa and QED rows reproduce the vertices of the rules [[§C6d.6 Momentum-Space Feynman Rules#^thm-c6d-6-2|Theorem §C6d.6.2]] and [[§C8.4 Feynman Rules for QED#^thm-c8-4-4|Theorem §C8.4.4]]. In the pseudoscalar row $i\cdot(-ig)\,\gamma^5 = g\gamma^5$: the $i$ of the coupling, which makes $\bar\psi i\gamma^5\psi$ Hermitian ([[§C5a.6 The Dirac Conjugate and the Bilinears#^def-c5a-6-3|Def. §C5a.6.3]]), meets the $i$ of the rule.
>
> *Model:* the theories named ([[§C6a.1 From Free to Interacting Fields#^mod-c6a-1-1|Model §C6a.1.1]], [[§C6a.9 Position-Space Feynman Rules#^mod-c6a-9-2|Model §C6a.9.2]], [[§C6a.9 Position-Space Feynman Rules#^mod-c6a-9-3|Model §C6a.9.3]], [[§C6d.1 Yukawa Theory#^mod-c6d-1-1|Model §C6d.1.1]], [[§C8.1 The QED Lagrangian and the Covariant Derivative#^mod-c8-1-1|Model §C8.1.1]]); *applies:* the vertex factors, every order.
>
> *Source: the user's PHY 513 notes, Appendix B, section "Complex fields, fermions and vector fields" (the table and the sentence after it) · the columns "derivatives" and "home" written here · every row checked with `qft-C/tools/rulesL/verify.py`*

^ex-c6c-11-3

## Propagators from the quadratic part

The same idea applies to the free part: the vertices are derivatives of $\mathcal L_{\rm int}$, and the propagators are the inverse of the second derivative of the free action.

> [!principle] Principle §C6c.11.4: The Propagator from the Quadratic Part
> Write the free action $S_0 = \int d^4x\,\mathcal L_0$ in momentum space, with $\Phi(x) = \int\frac{d^4p}{(2\pi)^4}\tilde\Phi(p)\,e^{-ip\cdot x}$ ([[§CA.4 Fourier Transforms and Fourier Tricks#^def-ca-4-1|Def. §CA.4.1]]), so that $\partial_\mu \to -ip_\mu$ on $\tilde\Phi(p)$ ([[§CA.4 Fourier Transforms and Fourier Tricks#^thm-ca-4-4|Theorem §CA.4.4]], 2):
>
> $$
> \begin{aligned}
> S_0 &= \int\frac{d^4p}{(2\pi)^4}\;\tfrac12\,\tilde\Phi_a(-p)\,K_{ab}(p)\,\tilde\Phi_b(p) && \text{(real fields)} , \\
> S_0 &= \int\frac{d^4p}{(2\pi)^4}\;\tilde\Phi^\ast_a(p)\,K_{ab}(p)\,\tilde\Phi_b(p) && \text{(complex fields)} , \\
> S_0 &= \int\frac{d^4p}{(2\pi)^4}\;\tilde{\bar\psi}(p)\,K(p)\,\tilde\psi(p) , \qquad \tilde{\bar\psi}(p) \equiv \tilde\psi(p)^\dagger\gamma^0 && \text{(Dirac fields)} .
> \end{aligned}
> $$
>
> The **kernel** $K(p)$ is the second derivative of the quadratic action, taken with the same conventions as the vertices. Then
>
> $$
> \text{propagator} = i\,K^{-1}(p) , \qquad\text{with } p^2 \to p^2 + i\varepsilon :
> $$
>
> it is $i$ times the momentum-space Green's function of the free field equation $K(p)\tilde\Phi(p) = 0$, that is, $K(p)\cdot(\text{propagator}) = i\,\mathbb 1$.
>
> *Model:* a free theory with a quadratic Lagrangian ([[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^mod-c1b-2-6|Model §C1b.2.6]], [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^mod-c1b-2-7|Model §C1b.2.7]], [[§C5a.7 The Dirac Equation and Its Lagrangian#^mod-c5a-7-3|Model §C5a.7.3]], [[§C4.6 The Maxwell Field, Gauge Symmetry and Gauge Fixing#^mod-c4-6-7|Model §C4.6.7]]); *applies:* a principle that organizes cases proved one by one, not a theorem proved here in general: the real scalar ([[§C2b.7 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-7-5|Theorem §C2b.7.5]], [[§C2b.7 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-7-10|Theorem §C2b.7.10]]), the Dirac field ([[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-1|Theorem §C5b.8.1]], [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-8|Theorem §C5b.8.8]]), the photon in the Feynman gauge ([[§C4.11 Vector-Field Propagators#^thm-c4-11-6|Theorem §C4.11.6]]). In each the contraction of two free fields is shown to be a Green's function of the field equation, and the $i\varepsilon$ selects the Feynman one among the fundamental solutions, which differ by homogeneous solutions ([[§CA.7 Boundary Values, iε Limits and Fundamental Solutions#^def-ca-7-1|Def. §CA.7.1]], [[§CA.7 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-7-7|Theorem §CA.7.7]], [[§CA.7 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-7-6|Theorem §CA.7.6]]). It needs $K(p)$ to be invertible: [[§C6c.11 Feynman Rules from the Lagrangian#^ex-c6c-11-6|Example §C6c.11.6]].
>
> *Source: the user's PHY 513 notes, Appendix B, section "Propagators from the quadratic part", Principle "The propagator" and the display before it · the Dirac line written with $\tilde{\bar\psi}$: the appendix writes one line $\tilde\Phi^\ast_a K_{ab}\tilde\Phi_b$ for "complex or Dirac fields"; for a Dirac field the left factor is $\bar\psi = \psi^\dagger\gamma^0$, which is what gives $K = \slashed p - m$ · the condition $K\cdot(\text{propagator}) = i\,\mathbb 1$ and the applies line written here*

^pr-c6c-11-4

> [!example] Example §C6c.11.4: The Real Scalar Field
> **Step 1** (integration by parts). For $\mathcal L_0 = \frac12\partial_\mu\phi\,\partial^\mu\phi - \frac12m^2\phi^2$ ([[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^mod-c1b-2-6|Model §C1b.2.6]]), $\partial_\mu\phi\,\partial^\mu\phi = \partial_\mu(\phi\,\partial^\mu\phi) - \phi\,\partial^2\phi$, and the total divergence integrates to zero for fields that decay at infinity ([[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-5|Theorem §C1b.2.5]]):
>
> $$
> S_0 = \int d^4x\;\tfrac12\,\phi\,\bigl(-\partial^2 - m^2\bigr)\phi .
> $$
>
> **Step 2** (momentum space). Insert the Fourier form of both fields, with momenta $q$ and $p$; $-\partial^2 \to p^2$ on $\tilde\phi(p)$, and $\int d^4x\,e^{-i(q + p)\cdot x} = (2\pi)^4\delta^4(q + p)$ ([[§CA.4 Fourier Transforms and Fourier Tricks#^thm-ca-4-3|Theorem §CA.4.3]]) sets $q = -p$:
>
> $$
> S_0 = \int\frac{d^4q}{(2\pi)^4}\frac{d^4p}{(2\pi)^4}\;\tfrac12\,\tilde\phi(q)\,(p^2 - m^2)\,\tilde\phi(p)\,(2\pi)^4\delta^4(q + p) = \int\frac{d^4p}{(2\pi)^4}\;\tfrac12\,\tilde\phi(-p)\,(p^2 - m^2)\,\tilde\phi(p) .
> $$
>
> **Step 3** (the propagator). $K = p^2 - m^2$, and
>
> $$
> i\,K^{-1} = \frac{i}{p^2 - m^2 + i\varepsilon} = \tilde D_F(p)
> $$
>
> ([[§C2b.7 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-7-10|Theorem §C2b.7.10]]). Check: $(\partial^2 + m^2)D_F = -i\delta^4$ ([[§C2b.7 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-7-5|Theorem §C2b.7.5]]) reads $(-p^2 + m^2)\tilde D_F = -i$ in momentum space, that is, $K\tilde D_F = i$.
>
> *Model:* [[§C2a.1 Canonical Quantization of Fields#^mod-c2a-1-1|Model §C2a.1.1]]; *applies:* the free real scalar field, exact.
>
> *Source: the user's PHY 513 notes, Appendix B, section "Propagators from the quadratic part" (first item) · the steps written out here*

^ex-c6c-11-4

> [!example] Example §C6c.11.5: The Dirac Field
> **Step 1** (the kernel). $\mathcal L_0 = \bar\psi(i\slashed\partial - m)\psi$ ([[§C5a.7 The Dirac Equation and Its Lagrangian#^mod-c5a-7-3|Model §C5a.7.3]]) needs no integration by parts. With $\psi(x) = \int\frac{d^4p}{(2\pi)^4}\tilde\psi(p)e^{-ip\cdot x}$ and $\bar\psi(x) = \int\frac{d^4q}{(2\pi)^4}\tilde{\bar\psi}(q)e^{+iq\cdot x}$, $i\partial_\mu \to p_\mu$ and the $x$ integral sets $q = p$:
>
> $$
> S_0 = \int\frac{d^4p}{(2\pi)^4}\;\tilde{\bar\psi}(p)\,(\slashed p - m)\,\tilde\psi(p) , \qquad K = \slashed p - m .
> $$
>
> **Step 2** (the inverse). $(\slashed p - m)(\slashed p + m) = \slashed p\slashed p - m^2 = p^2 - m^2$, since $\slashed p\slashed p = p^2$ ([[§C5a.7 The Dirac Equation and Its Lagrangian#^def-c5a-7-3|Def. §C5a.7.3]]), so
>
> $$
> i\,K^{-1} = i\,(\slashed p - m)^{-1} = \frac{i\,(\slashed p + m)}{p^2 - m^2 + i\varepsilon} = \tilde S_F(p)
> $$
>
> ([[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-3|Theorem §C5b.8.3]]; the matrix inverse with $i\varepsilon$: [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-8|Theorem §C5b.8.8]]). Check: $(\slashed p - m)\tilde S_F(p) = i\,\mathbb 1$ ([[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-1|Theorem §C5b.8.1]]).
>
> *Model:* [[§C5b.1 Canonical Quantization of the Dirac Field#^mod-c5b-1-2|Model §C5b.1.2]]; *applies:* the free Dirac field, exact.
>
> *Source: the user's PHY 513 notes, Appendix B, section "Propagators from the quadratic part" (second item) · the steps written out here*

^ex-c6c-11-5

> [!example] Example §C6c.11.6: The Maxwell Field: No Inverse without Gauge Fixing
> **Step 1** (integration by parts). $-\frac14F_{\mu\nu}F^{\mu\nu} = -\frac12\bigl(\partial_\mu A_\nu\,\partial^\mu A^\nu - \partial_\mu A_\nu\,\partial^\nu A^\mu\bigr)$. Moving one derivative in each term and dropping the total divergences (fields that decay at infinity),
>
> $$
> \int d^4x\,\Bigl(-\tfrac14F_{\mu\nu}F^{\mu\nu}\Bigr) = \int d^4x\;\tfrac12\bigl(A_\nu\,\partial^2A^\nu - A_\nu\,\partial^\nu\partial_\mu A^\mu\bigr) = \int d^4x\;\tfrac12\,A_\mu\bigl(g^{\mu\nu}\partial^2 - \partial^\mu\partial^\nu\bigr)A_\nu .
> $$
>
> **Step 2** (the kernel). With $\partial_\mu \to -ip_\mu$: $\partial^2 \to -p^2$ and $\partial^\mu\partial^\nu \to -p^\mu p^\nu$, so
>
> $$
> K^{\mu\nu}(p) = -p^2g^{\mu\nu} + p^\mu p^\nu .
> $$
>
> **Step 3** (no inverse). $K^{\mu\nu}p_\nu = -p^2p^\mu + p^\mu p^2 = 0$: the matrix $K$ has the null vector $p_\nu$ and no inverse. This is [[§C4.6 The Maxwell Field, Gauge Symmetry and Gauge Fixing#^thm-c4-6-5|Theorem §C4.6.5]] (the Maxwell kinetic operator is singular; the Maxwell Lagrangian has no propagator). It is the gauge redundancy in another guise: a pure-gauge configuration $A_\mu = \partial_\mu\alpha$, $\tilde A_\mu(p) \propto p_\mu$, has $F_{\mu\nu} = 0$ and costs no action ([[§C4.6 The Maxwell Field, Gauge Symmetry and Gauge Fixing#^def-c4-6-1|Def. §C4.6.1]], [[§C8.2 Gauge Invariance#^thm-c8-2-3|Theorem §C8.2.3]]), so the quadratic form has a zero mode.
>
> **Step 4** (the Feynman gauge). Adding the gauge-fixing term $-\frac12(\partial_\mu A^\mu)^2$ ([[§C4.6 The Maxwell Field, Gauge Symmetry and Gauge Fixing#^def-c4-6-3|Def. §C4.6.3]]) adds $\frac12A_\mu\,\partial^\mu\partial^\nu A_\nu$ after one integration by parts, that is, $-p^\mu p^\nu$ to the kernel:
>
> $$
> K^{\mu\nu} = -p^2g^{\mu\nu} , \qquad i\,(K^{-1})_{\mu\nu} = \frac{-i\,g_{\mu\nu}}{p^2 + i\varepsilon} ,
> $$
>
> since $(-p^2g^{\mu\nu})\bigl(-\frac{g_{\nu\rho}}{p^2}\bigr) = \delta^\mu{}_\rho$. This is the photon propagator of the course ([[§C8.3 Photon Lines꞉ the Quantized Photon Field, Polarizations and the Propagator#^thm-c8-3-5|Theorem §C8.3.5]], [[§C4.11 Vector-Field Propagators#^thm-c4-11-6|Theorem §C4.11.6]]); for a general gauge parameter the kernel and its inverse are [[§C4.11 Vector-Field Propagators#^thm-c4-11-8|Theorem §C4.11.8]] ([[§C4.6 The Maxwell Field, Gauge Symmetry and Gauge Fixing#^mod-c4-6-7|Model §C4.6.7]]). The appendix marks this step as filled in, a preview of Lecture 25; the quantization of the gauge-fixed field with its four polarizations is [[§C4.8 Covariant Quantization꞉ Modes and the Indefinite Mode Algebra|§C4.8]] and [[§C8.3 Photon Lines꞉ the Quantized Photon Field, Polarizations and the Propagator#^thm-c8-3-4|Theorem §C8.3.4]].
>
> *Model:* [[§C4.6 The Maxwell Field, Gauge Symmetry and Gauge Fixing#^mod-c4-6-2|Model §C4.6.2]] (Steps 1–3), [[§C4.6 The Maxwell Field, Gauge Symmetry and Gauge Fixing#^mod-c4-6-7|Model §C4.6.7]] at $\xi = 1$ (Step 4); *applies:* classical kernels, exact; the propagator as a vacuum value in the Feynman gauge is [[§C4.11 Vector-Field Propagators#^thm-c4-11-6|Theorem §C4.11.6]].
>
> *Source: the user's PHY 513 notes, Appendix B, section "Propagators from the quadratic part" (third item) · PS §9.4, eqs. (9.51)–(9.52), (9.58) · the integrations by parts written out here · kernels checked numerically with `qft-C/tools/rulesL/verify.py`*

^ex-c6c-11-6

## What the rule does not give

> [!caution] Caution: What the rule does not give
> The rule supplies the vertices, and its analogue the propagators. Still to be supplied by hand:
> 1. **External-line factors**: $1$ for scalars ([[§C6c.6 Feynman Rules for Amplitudes#^thm-c6c-6-1|Theorem §C6c.6.1]], 1), $u$, $\bar u$, $\bar v$, $v$ for fermions ([[§C6d.2 Contractions with External Fermions#^thm-c6d-2-1|Theorem §C6d.2.1]]), $\epsilon_\mu$, $\epsilon^\ast_\mu$ for photons ([[§C8.4 Feynman Rules for QED#^thm-c8-4-1|Theorem §C8.4.1]]). They come from the free fields, not from $\mathcal L_{\rm int}$.
> 2. **Fermion signs**: the relative minus sign between diagrams that differ by exchanging identical fermions ([[§C6d.5 Second Order#^thm-c6d-5-3|Theorem §C6d.5.3]], [[§C6d.5 Second Order#^thm-c6d-5-4|Theorem §C6d.5.4]]), the overall sign relative to the $\mathbb 1$ of $\hat S = \mathbb 1 + i\hat T$ ([[§C8.5 The Coulomb Potential, and Why Like Charges Repel#^thm-c8-5-5|Theorem §C8.5.5]], [[§C8.5 The Coulomb Potential, and Why Like Charges Repel#^thm-c8-5-6|Theorem §C8.5.6]]), and the $-1$ for each closed fermion loop ([[§C6d.4 First Order#^thm-c6d-4-6|Theorem §C6d.4.6]]). They come from the order of the operators in the contractions ([[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-4|Theorem §C6d.3.4]]), not from any single vertex.
> 3. **Symmetry factors** of whole diagrams ([[§C6c.11 Feynman Rules from the Lagrangian#^cau-c6c-11-1|Caution: Labelled legs, not the symmetry factor of the diagram]]; [[P5 Symmetry Factor of a Diagram|P5]]).
> 4. **Momentum conservation and loops**: a delta function at each vertex, and $\int\frac{d^4\ell}{(2\pi)^4}$ for each loop momentum that conservation leaves undetermined ([[§C6c.6 Feynman Rules for Amplitudes#^thm-c6c-6-3|Theorem §C6c.6.3]], [[§C6a.14 Feynman Rules for Polynomial Interactions#^thm-c6a-14-3|Theorem §C6a.14.3]]).
> 5. **Which external state attaches where**: for complex fields and fermions, which of $\hat\phi$, $\hat\phi^\dagger$ (or $\hat\psi$, $\hat{\bar\psi}$) contains the operator that matches the state ([[§C6c.2 Contractions with External Particles#^lem-c6c-2-2|Lemma §C6c.2.2]], 3; [[§C6d.2 Contractions with External Fermions#^thm-c6d-2-1|Theorem §C6d.2.1]]; [[§C8.4 Feynman Rules for QED#^rem-c8-4-2|§C8.4, Remark: The external fermions are those of Yukawa theory]]), as for the arrows of [[§C6d.1 Yukawa Theory#^thm-c6d-1-5|Theorem §C6d.1.5]].
>
> *Source: the user's PHY 513 notes, Appendix B, section "What the rule does not give", Caution "Still to be supplied by hand"*

^cau-c6c-11-2

*Procedure:* [[P6 Tree Amplitude from a Lagrangian#^p6-4|P6, step 4]]

> [!remark] Remark: Correspondence with Yu
> Yu states the rule in words each time a theory is introduced: strip the field operators from the interaction term and multiply by $i$. He does so for Yukawa theory after the rules of §7.2 ($\mathcal L_{\rm Y} = -\kappa\phi\bar\psi\psi$ gives $-i\kappa$), for QED in §8.1 ($-Q_feA_\mu\bar\psi_f\gamma^\mu\psi_f$ gives $-iQ_fe\gamma^\mu$), and for $\phi^4$ in §7.3, where he adds that one must also multiply by the $4!$ permutations of the identical fields (eq. (7.120) and the remark after it). In these notes: [[§C6d.1 Yukawa Theory#^thm-c6d-1-4|Theorem §C6d.1.4]], [[§C8.4 Feynman Rules for QED#^thm-c8-4-3|Theorem §C8.4.3]], [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-4|Theorem §C6c.4.4]] ([[§C6a.14 Feynman Rules for Polynomial Interactions#^rem-c6a-14-1|§C6a.14, Remark: Yu's route]]). The derivative form of this section does the stripping and the counting in one step. For derivative couplings his §11.4.3 gives the momentum rule and the vertices of scalar QED: [[§C8.21★ Derivative Couplings and Scalar QED|§C8.21★]].
>
> *Source: the user's PHY 513 notes, Appendix B, paragraph "Correspondence with Yu" · Yu §7.2, the paragraph after rules 1–12; §7.3, eq. (7.120) and the remark on the vertex after the rules; §8.1, the paragraph after rule 9 (wording checked in the text of the current PDF)*

^rem-c6c-11-1

> [!abstract]- Mathematical background
> Proved in the Math vault, in CA and in CB; each line says what the physics above relies on.
>
> - [[§CA.9 Splitting Pairings and the Exponential Formula#^lem-ca-9-5|Lemma §CA.9.5]] — a homogeneous polynomial of degree $n$ in commuting variables has one symmetric coefficient array, equal to its $n$-th derivatives and to the average of any coefficient array over the $n!$ orderings: the algebra of [[§C6c.11 Feynman Rules from the Lagrangian#^thm-c6c-11-2|Theorem §C6c.11.2]].
> - [[§6 Equality of Mixed Partials#^thm-6-1|452 Thm. §6.1]] — mixed partial derivatives commute: the vertex factor is symmetric in its indices (Theorem §C6c.11.1, 2).
> - [[§CA.9 Splitting Pairings and the Exponential Formula#^thm-ca-9-4|Theorem §CA.9.4]] — the relabelling group of a vertex with several kinds of legs, of order $\prod_km_k!$: the count behind part 1 of Theorem §C6c.11.3, through [[§C6a.14 Feynman Rules for Polynomial Interactions#^thm-c6a-14-2|Theorem §C6a.14.2]].
> - [[§CA.4 Fourier Transforms and Fourier Tricks#^def-ca-4-1|Def. §CA.4.1]], [[§CA.4 Fourier Transforms and Fourier Tricks#^thm-ca-4-4|Theorem §CA.4.4]], [[§CA.4 Fourier Transforms and Fourier Tricks#^thm-ca-4-3|Theorem §CA.4.3]] — the Fourier convention, $\partial_\mu \leftrightarrow -ip_\mu$, and the plane-wave delta function: the kernel $K(p)$ and the momentum delta of a vertex.
> - [[§CA.7 Boundary Values, iε Limits and Fundamental Solutions#^def-ca-7-1|Def. §CA.7.1]], [[§CA.7 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-7-7|Theorem §CA.7.7]], [[§CA.7 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-7-6|Theorem §CA.7.6]] — fundamental solutions, their non-uniqueness, and the $i\varepsilon$ limits of the propagator denominators: in which sense $iK^{-1}$ with $p^2 \to p^2 + i\varepsilon$ is one Green's function among several.
> - [[§CB.23 Grassmann Algebras#^def-cb-23-5|Def. §CB.23.5]], [[§CB.23 Grassmann Algebras#^def-cb-23-6|Def. §CB.23.6]] — left and right derivatives with respect to anticommuting symbols: the fermion derivatives of Theorem §C6c.11.3, 2.

> [!remark]- Connections
> - The rule for real scalar fields, derived from the counting rule, with the sigma-model vertex as its first use; this section is its general form and second proof — [[§C6c.8 The Linear Sigma Model꞉ Fields with an Internal Index#^thm-c6c-8-4|Theorem §C6c.8.4]], [[§C6c.8 The Linear Sigma Model꞉ Fields with an Internal Index#^thm-c6c-8-3|Theorem §C6c.8.3]], [[§C6a.14 Feynman Rules for Polynomial Interactions#^thm-c6a-14-2|Theorem §C6a.14.2]].
> - "Strip the fields, multiply by $i$ and by the permutations of equal fields" is the same rule in words; the derivative does the stripping and the counting at once — [[§C6d.1 Yukawa Theory#^thm-c6d-1-4|Theorem §C6d.1.4]], [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-4|Theorem §C6c.4.4]], [[§C6c.6 Feynman Rules for Amplitudes#^thm-c6c-6-1|Theorem §C6c.6.1]].
> - Only the vertex depends on the interaction; the lines come from the free fields. The propagator principle says the same from the side of the quadratic part — [[§C6c.6 Feynman Rules for Amplitudes#^thm-c6c-6-1|Theorem §C6c.6.1]], [[§C6d.6 Momentum-Space Feynman Rules#^thm-c6d-6-1|Theorem §C6d.6.1]].
> - The propagator as the inverse of the second variation of the action, and as the covariance of a Gaussian in the path integral (Lectures 23–26) — [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^rem-c1b-2-8|§C1b.2, Remark: The second variation is the operator whose inverse is the propagator]], [[§C2b.7 Time Ordering, the Feynman Propagator and the iε Prescription#^rem-c2b-7-4|§C2b.7, Remark: The propagator as a Gaussian covariance (preview)]].
> - The zero mode of the Maxwell kernel is the reason the photon needs gauge fixing before it has a propagator — [[§C4.6 The Maxwell Field, Gauge Symmetry and Gauge Fixing#^thm-c4-6-5|Theorem §C4.6.5]], [[§C4.11 Vector-Field Propagators#^thm-c4-11-8|Theorem §C4.11.8]].
> - With derivatives in $\mathcal L_{\rm int}$ the vertex depends on the momenta, and $\hat{\mathcal H}_I = -\mathcal L_{\rm int}$ fails; scalar QED is the example — [[§C8.21★ Derivative Couplings and Scalar QED|§C8.21★]], [[§C6a.1 From Free to Interacting Fields#^thm-c6a-1-4|Theorem §C6a.1.4]].
> - The procedure that uses the rule, and the worked translations of questions into formulas — [[P6 Tree Amplitude from a Lagrangian|P6]], [[§C6c.12 From the Question to the Formula|§C6c.12]].
