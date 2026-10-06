---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C5a
section: C5a.7
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C5a.6 Normalization, Spin Sums and Helicity]] · ↑ [[· C5a Spinors and the Dirac Equation]] · [[§C5b.1 Canonical Quantization of the Dirac Field]] →

*Sources: the user's PHY 513 notes, Ch. 9 §9.6 (Supplement: $\gamma$-matrix technology (Problem Set 5)) · PHY 513, Problem Set 5, Problems 2, 3 and 5 (as the user wrote them) · Peskin & Schroeder, §3.4, pp. 49–52, eqs. (3.68)–(3.81) · Yu Zhao-Huan, 量子场论讲义, §7.1, eqs. (7.48)–(7.54), §8.2.2, eqs. (8.44)–(8.77).*

How are long products of $\gamma$ matrices shortened, traced and reduced, as every amplitude with spin-½ particles requires? Everything follows from the Clifford algebra ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-1|Def. §C5a.2.1]]), the algebra of $\gamma^5$ ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-5|Def. §C5a.2.5]], [[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-13|Theorem §C5a.2.13]]), the basis property of the sixteen products ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-4|Theorem §C5a.2.4]]) and the slash of [[§C5a.3 The Dirac Equation and Its Lagrangian#^def-c5a-3-2|Def. §C5a.3.2]]. This section adds the working identities: slash algebra, contractions, traces, the $\varepsilon$-forms of $\gamma^5$ and its duality on $\sigma^{\mu\nu}$, the reduction of any product to the standard basis, and the Gordon identity. Problem Set 5 (submitted) proves several of them; its proofs appear as the user wrote them, and no other problem-set material is used.

*Conventions:* $\varepsilon^{0123} = +1$, $\varepsilon_{0123} = -1$ ([[§C1.5 Vectors, Tensors and Index Notation#^cau-c1-5-5|§C1.5, Caution: The sign of ε⁰¹²³]]); $\sigma^{\mu\nu} = \frac i2[\gamma^\mu, \gamma^\nu]$ ([[§C5a.4 Bilinears, Chirality and the Weyl Equations#^def-c5a-4-2|Def. §C5a.4.2]]; other normalizations: [[§C5a.4 Bilinears, Chirality and the Weyl Equations#^cau-c5a-4-1|§C5a.4, Caution: Three normalizations of σ^μν]]); components of four-vectors are numbers and commute with the $\gamma$'s; the identity matrix is often not written. Every identity here was checked numerically in the chiral basis in the user's notes.

## Products and slashes

> [!definition] Definition §C5a.7.1: Antisymmetrized Products of γ Matrices
> For indices $\mu_1, \dots, \mu_n$,
>
> $$
> \gamma^{[\mu_1}\gamma^{\mu_2}\cdots\gamma^{\mu_n]} \equiv \gamma^{[\mu_1\cdots\mu_n]} \equiv \frac1{n!}\sum_{\pi\in S_n}\operatorname{sgn}(\pi)\,\gamma^{\mu_{\pi(1)}}\cdots\gamma^{\mu_{\pi(n)}} ,
> $$
>
> of the Dirac matrices ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-1|Def. §C5a.2.1]]): the totally antisymmetric part, with weight $1/n!$. Thus $\gamma^{[\mu\nu]} = \frac12[\gamma^\mu, \gamma^\nu] = -i\sigma^{\mu\nu}$, with $\sigma^{\mu\nu}$ of [[§C5a.4 Bilinears, Chirality and the Weyl Equations#^def-c5a-4-2|Def. §C5a.4.2]].
>
> *Source: PHY 513, Problem Set 5, Problem 5(c) statement (notation) · PS §3.4, p. 49 · the user's PHY 513 notes, Ch. 9 §9.6 (Principle "Properties of $\gamma^5$")*

^def-c5a-7-1

The antisymmetrized product vanishes when two indices coincide (the terms cancel in pairs), and equals the plain product when all indices are distinct (each term, reordered by anticommuting distinct $\gamma$'s, carries the sign of its permutation twice). So $\gamma^{[\mu_1\cdots\mu_n]} = 0$ for $n \ge 5$: only four distinct $\gamma$'s exist.

> [!theorem] Theorem §C5a.7.1: Slash Algebra
> For four-vectors $a$, $b$, with slashes as in [[§C5a.3 The Dirac Equation and Its Lagrangian#^def-c5a-3-2|Def. §C5a.3.2]] and $\sigma^{\mu\nu} = \frac i2[\gamma^\mu, \gamma^\nu]$ ([[§C5a.4 Bilinears, Chirality and the Weyl Equations#^def-c5a-4-2|Def. §C5a.4.2]]):
>
> $$
> \gamma_\mu\gamma^\nu + \gamma^\nu\gamma_\mu = 2\delta_\mu{}^\nu, \qquad \gamma^\mu\slashed{a} = 2a^\mu - \slashed{a}\gamma^\mu, \qquad \slashed{a}\slashed{b} + \slashed{b}\slashed{a} = 2\,a\cdot b, \qquad \slashed{a}\slashed{b} = a\cdot b - i\sigma^{\mu\nu}a_\mu b_\nu .
> $$
>
> In particular $\slashed{a}\slashed{a} = a^2$.
>
> *Source: the user's PHY 513 notes, Ch. 9 §9.6 (opening paragraph), Ch. 8 §8.1 ("Square to ±1, or square root?") · PHY 513, Problem Set 5, Problems 2(c)–(d) and 3 (as the user wrote them) · Yu §8.2.2, eqs. (8.68)–(8.70)*

^thm-c5a-7-1

> [!derivation]- Derivation
> **1. Lower one index.** Multiply $\{\gamma^\rho, \gamma^\nu\} = 2g^{\rho\nu}$ by the constant $g_{\mu\rho}$ and sum: $\gamma_\mu\gamma^\nu + \gamma^\nu\gamma_\mu = 2g_{\mu\rho}g^{\rho\nu} = 2\delta_\mu{}^\nu$.
>
> **2. Move $\gamma^\mu$ past a slash.** $\gamma^\mu\slashed{a} = \gamma^\mu\gamma^\nu a_\nu = (2g^{\mu\nu} - \gamma^\nu\gamma^\mu)a_\nu = 2a^\mu - \slashed{a}\gamma^\mu$.
>
> **3. Two slashes.** Contract step 2 with $b_\mu$: $\slashed{b}\slashed{a} = 2a\cdot b - \slashed{a}\slashed{b}$.
>
> **4. Symmetric and antisymmetric parts.** $\gamma^\mu\gamma^\nu = \frac12\{\gamma^\mu, \gamma^\nu\} + \frac12[\gamma^\mu, \gamma^\nu] = g^{\mu\nu} - i\sigma^{\mu\nu}$ (the split of [[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-1|Theorem §C5a.2.1]], 3, with $\frac12[\gamma^\mu, \gamma^\nu] = -i\cdot\frac i2[\gamma^\mu, \gamma^\nu]$). Contract with $a_\mu b_\nu$.
>
> **5. Equal vectors.** $\sigma^{\mu\nu}a_\mu a_\nu = 0$ (antisymmetric against symmetric), so $\slashed{a}\slashed{a} = a^2$, as in [[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-1|Theorem §C5a.2.1]].
>
> **What the derivation shows**
> - Every rule is the Clifford algebra with indices moved by $g$; no representation is used.
> - Used next: each step of the contraction identities (Theorem §C5a.7.2) and of the Gordon identity (Theorem §C5a.7.9) is one application of step 2.

^der-c5a-7-1

*Uses:* [[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-1|Def. §C5a.2.1]], [[§C5a.3 The Dirac Equation and Its Lagrangian#^def-c5a-3-2|Def. §C5a.3.2]], [[§C5a.4 Bilinears, Chirality and the Weyl Equations#^def-c5a-4-2|Def. §C5a.4.2]]

## Contractions

> [!theorem] Theorem §C5a.7.2: Contraction Identities
> For any four-vectors $k$, $p$, $q$, in four spacetime dimensions, with slashes as in [[§C5a.3 The Dirac Equation and Its Lagrangian#^def-c5a-3-2|Def. §C5a.3.2]],
>
> $$
> \gamma_\mu\gamma^\mu = 4, \qquad \gamma_\mu\slashed{k}\gamma^\mu = -2\slashed{k}, \qquad \gamma_\mu\slashed{p}\slashed{q}\gamma^\mu = 4\,p\cdot q, \qquad \gamma_\mu\slashed{k}\slashed{p}\slashed{q}\gamma^\mu = -2\slashed{q}\slashed{p}\slashed{k} .
> $$
>
> Equivalently, with free indices: $\gamma_\mu\gamma^\nu\gamma^\mu = -2\gamma^\nu$, $\gamma_\mu\gamma^\nu\gamma^\rho\gamma^\mu = 4g^{\nu\rho}$, $\gamma_\mu\gamma^\nu\gamma^\rho\gamma^\sigma\gamma^\mu = -2\gamma^\sigma\gamma^\rho\gamma^\nu$.
>
> *Source: PHY 513, Problem Set 5, Problem 2 (as the user wrote it) · the user's PHY 513 notes, Ch. 9 §9.6 (Principle "Contraction identities", eq. (contractions)) · PS eqs. (5.8)–(5.9) (cited in Problem Set 5) · Yu §8.2.2, eqs. (8.56)–(8.63), (8.71)–(8.73)*

^thm-c5a-7-2

> [!derivation]- Derivation (the covariant route of the user's notes)
> Each step moves the rightmost $\gamma^\mu$ one place to the left with $\slashed{a}\gamma^\mu = 2a^\mu - \gamma^\mu\slashed{a}$ ([[§C5a.7 Gamma-Matrix Technology#^thm-c5a-7-1|Theorem §C5a.7.1]], step 2 rearranged) and then uses the previous identity.
>
> **1. No $\gamma$ inside.** $\gamma_\mu\gamma^\mu = g_{\mu\nu}\gamma^\nu\gamma^\mu$. $g_{\mu\nu}$ is symmetric, so only the symmetric part of $\gamma^\nu\gamma^\mu$ survives: $= \frac12g_{\mu\nu}\{\gamma^\nu, \gamma^\mu\} = g_{\mu\nu}g^{\nu\mu}\mathbb 1 = \delta^\mu{}_\mu\mathbb 1 = 4\cdot\mathbb 1$. ⚑ By-product: the $4$ is the spacetime dimension $d$, not the size of the matrices; in $d$ dimensions $\gamma_\mu\gamma^\mu = d$ and the identities below change (Yu §8.2.2, used in dimensional regularization, QFT C7, planned).
>
> **2. One slash.** $\gamma_\mu\slashed{k}\gamma^\mu = \gamma_\mu(2k^\mu - \gamma^\mu\slashed{k}) = 2\slashed{k} - (\gamma_\mu\gamma^\mu)\slashed{k} = 2\slashed{k} - 4\slashed{k} = -2\slashed{k}$, using $\gamma_\mu k^\mu = \slashed{k}$ and step 1.
>
> **3. Two slashes.** $\gamma_\mu\slashed{p}\slashed{q}\gamma^\mu = \gamma_\mu\slashed{p}(2q^\mu - \gamma^\mu\slashed{q}) = 2\slashed{q}\slashed{p} - (\gamma_\mu\slashed{p}\gamma^\mu)\slashed{q} = 2\slashed{q}\slashed{p} + 2\slashed{p}\slashed{q} = 2(\slashed{q}\slashed{p} + \slashed{p}\slashed{q}) = 4\,p\cdot q$, by step 2 and Theorem §C5a.7.1, step 3.
>
> **4. Three slashes.** $\gamma_\mu\slashed{k}\slashed{p}\slashed{q}\gamma^\mu = \gamma_\mu\slashed{k}\slashed{p}(2q^\mu - \gamma^\mu\slashed{q}) = 2\slashed{q}\slashed{k}\slashed{p} - (\gamma_\mu\slashed{k}\slashed{p}\gamma^\mu)\slashed{q} = 2\slashed{q}\slashed{k}\slashed{p} - 4(k\cdot p)\slashed{q}$ (step 3). Now $\slashed{k}\slashed{p} = 2k\cdot p - \slashed{p}\slashed{k}$, so $2\slashed{q}\slashed{k}\slashed{p} = 4(k\cdot p)\slashed{q} - 2\slashed{q}\slashed{p}\slashed{k}$. The $4(k\cdot p)\slashed{q}$ terms cancel: $-2\slashed{q}\slashed{p}\slashed{k}$.
>
> **5. Free-index forms.** Each identity is linear in each vector; take $k$, $p$, $q$ to be unit vectors along the coordinate axes (or differentiate with respect to $k_\nu$, $p_\rho$, $q_\sigma$).
>
> **What the derivation shows**
> - One rule, applied $n$ times, shortens a string of $n$ $\gamma$'s sandwiched by a contracted pair; the pattern continues to longer strings.
> - Assumption: four spacetime dimensions (step 1).

^der-c5a-7-2

*Uses:* [[§C5a.7 Gamma-Matrix Technology#^thm-c5a-7-1|Theorem §C5a.7.1]], [[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-1|Def. §C5a.2.1]]

> [!derivation]- Derivation (second route: Problem Set 5, Problem 2, as the user wrote it)
> **(a) Components.** With $g_{00} = 1$, $g_{ii} = -1$: $\gamma_0 = \gamma^0$, $\gamma_i = -\gamma^i$. For each fixed $\mu$ (no sum) $\gamma^\mu\gamma^\mu = \frac12\{\gamma^\mu, \gamma^\mu\} = g^{\mu\mu}$. Hence $\gamma_\mu\gamma^\mu = \gamma^0\gamma^0 - \sum_{i=1}^3\gamma^i\gamma^i = g^{00} - \sum_ig^{ii} = 1 - (-3) = 4$.
>
> **(b) Components, time and space separately.** From $\gamma^\mu\gamma^\nu = 2g^{\mu\nu} - \gamma^\nu\gamma^\mu$: $\gamma^j\gamma^0 = -\gamma^0\gamma^j$, $\gamma^i\gamma^j = -2\delta^{ij} - \gamma^j\gamma^i$, $(\gamma^0)^2 = 1$, $(\gamma^i)^2 = -1$. Write $\slashed{k} = k_0\gamma^0 - \sum_jk_j\gamma^j$ in the user's index form ($k_\nu\gamma_\nu$ with the metric written out) and $\gamma_\mu\slashed{k}\gamma^\mu = \gamma^0\slashed{k}\gamma^0 - \sum_i\gamma^i\slashed{k}\gamma^i$.
> - Time component: $\gamma^0k_0\gamma^0\gamma^0 - \sum_j\gamma^0k_j\gamma^j\gamma^0 = k_0\gamma^0 + \sum_jk_j\gamma^j$ (one anticommutation, then $(\gamma^0)^2 = 1$).
> - Space component, fixed $i$: $\gamma^ik_0\gamma^0\gamma^i - \sum_j\gamma^ik_j\gamma^j\gamma^i = -k_0\gamma^0(\gamma^i)^2 - \sum_jk_j(-2\delta_{ij} - \gamma^j\gamma^i)\gamma^i = k_0\gamma^0 + 2k_i\gamma^i - \sum_jk_j\gamma^j$.
> - Sum over $i = 1, 2, 3$ (the $i$-independent terms triple): $3k_0\gamma^0 + 2\sum_ik_i\gamma^i - 3\sum_jk_j\gamma^j = 3k_0\gamma^0 - \sum_jk_j\gamma^j$.
> - Subtract from the time component: $k_0\gamma^0 + \sum_jk_j\gamma^j - 3k_0\gamma^0 + \sum_jk_j\gamma^j = -2\bigl(k_0\gamma^0 - \sum_jk_j\gamma^j\bigr) = -2\slashed{k}$.
>
> **(c) Lowering indices.** With $\slashed{p} = p_\nu\gamma^\nu$, $\slashed{q} = q_\sigma\gamma^\sigma$ and $\gamma^\nu\gamma^\mu$-reorderings $\gamma_\mu\gamma^\nu = 2\delta_\mu{}^\nu - \gamma^\nu\gamma_\mu$:
>
> $$
> \gamma_\mu\slashed{p}\slashed{q}\gamma^\mu = p_\nu q_\sigma\bigl(2\delta_\mu{}^\nu - \gamma^\nu\gamma_\mu\bigr)\gamma^\sigma\gamma^\mu = 2\slashed{q}\slashed{p} - p_\nu q_\sigma\gamma^\nu\bigl(2\delta_\mu{}^\sigma - \gamma^\sigma\gamma_\mu\bigr)\gamma^\mu = 2\slashed{q}\slashed{p} - 2\slashed{p}\slashed{q} + 4\slashed{p}\slashed{q} ,
> $$
>
> using $\gamma_\mu\gamma^\mu = 4$ from (a); then $2\slashed{q}\slashed{p} = 2(2p\cdot q - \slashed{p}\slashed{q})$ gives $4p\cdot q - 2\slashed{p}\slashed{q} - 2\slashed{p}\slashed{q} + 4\slashed{p}\slashed{q} = 4p\cdot q$.
>
> **(d) From (c).** $\gamma_\mu\slashed{k}\slashed{p}\slashed{q}\gamma^\mu = \gamma_\mu\slashed{k}\slashed{p}\,q_\sigma(2\delta^{\sigma\mu} - \gamma^\mu\gamma^\sigma) = 2\gamma_\mu\slashed{k}\slashed{p}\,q^\mu - (\gamma_\mu\slashed{k}\slashed{p}\gamma^\mu)\slashed{q}$. The second term is $4(k\cdot p)\slashed{q}$ by (c). In the first, $\slashed{k}\slashed{p} = k_\nu p_\rho(2g^{\nu\rho} - \gamma^\rho\gamma^\nu)$, so $2\gamma_\mu\slashed{k}\slashed{p}\,q^\mu = 4(k\cdot p)\slashed{q} - 2\slashed{q}\slashed{p}\slashed{k}$. Total: $4(k\cdot p)\slashed{q} - 2\slashed{q}\slashed{p}\slashed{k} - 4(k\cdot p)\slashed{q} = -2\slashed{q}\slashed{p}\slashed{k}$.
>
> **What the derivation shows**
> - The component route of (a)–(b) needs only $(\gamma^0)^2 = 1$, $(\gamma^i)^2 = -1$ and anticommutation; the covariant route needs only the anticommutator and handles longer strings with the same pattern (the user's notes' comparison).

^der-c5a-7-2b

*Uses:* [[§C5a.7 Gamma-Matrix Technology#^thm-c5a-7-1|Theorem §C5a.7.1]], [[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-1|Def. §C5a.2.1]]

These identities shorten strings in which an index is contracted across other $\gamma$'s, as happens in every amplitude with a photon exchanged between fermion lines (QFT C8, planned).

## Traces

> [!theorem] Theorem §C5a.7.3: Traces of γ Matrices
> $$
> \operatorname{tr}\mathbb 1 = 4, \qquad \operatorname{tr}(\text{odd number of }\gamma\text{'s}) = 0, \qquad \operatorname{tr}(\gamma^\mu\gamma^\nu) = 4g^{\mu\nu}, \qquad \operatorname{tr}(\gamma^\mu\gamma^\nu\gamma^\rho\gamma^\sigma) = 4\bigl(g^{\mu\nu}g^{\rho\sigma} - g^{\mu\rho}g^{\nu\sigma} + g^{\mu\sigma}g^{\nu\rho}\bigr) .
> $$
>
> for the $4\times4$ Dirac matrices ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-1|Def. §C5a.2.1]]). With slashes ([[§C5a.3 The Dirac Equation and Its Lagrangian#^def-c5a-3-2|Def. §C5a.3.2]]): $\operatorname{tr}(\slashed{a}\slashed{b}) = 4a\cdot b$, $\operatorname{tr}(\slashed{a}\slashed{b}\slashed{c}\slashed{d}) = 4\bigl[(a\cdot b)(c\cdot d) - (a\cdot c)(b\cdot d) + (a\cdot d)(b\cdot c)\bigr]$.
>
> *Source: Yu §7.1, eqs. (7.48)–(7.54), §8.2.2, eqs. (8.44)–(8.45), (8.49)–(8.52), (8.74)–(8.75) · PS §5.1 (trace theorems, as statements) · the user's PHY 513 notes, Ch. 9 §9.1 (Derivation "Step 2": $\operatorname{tr}\gamma^\mu = 0$)*

^thm-c5a-7-3

> [!derivation]- Derivation
> The trace is cyclic, $\operatorname{tr}(AB) = \operatorname{tr}(BA)$ ([[§33 Trace꞉ A Connection Between Matrices and Operators#^ladr-8-49|LADR Thm. 8.49]]), and linear.
>
> **1. $\operatorname{tr}\mathbb 1 = 4$**: the Dirac matrices are $4\times4$ ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-5|Theorem §C5a.2.5]]: four is the dimension of every irreducible realization).
>
> **2. Odd number.** Let $M = \gamma^{\mu_1}\cdots\gamma^{\mu_n}$ with $n$ odd. Insert $(\gamma^5)^2 = \mathbb 1$ ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-13|Theorem §C5a.2.13]]): $\operatorname{tr}M = \operatorname{tr}(M\gamma^5\gamma^5)$. Move the first $\gamma^5$ to the left through the $n$ factors of $M$, each anticommuting with it: $M\gamma^5 = (-1)^n\gamma^5M = -\gamma^5M$. So $\operatorname{tr}M = -\operatorname{tr}(\gamma^5M\gamma^5)$. By cyclicity $\operatorname{tr}(\gamma^5M\gamma^5) = \operatorname{tr}(M\gamma^5\gamma^5) = \operatorname{tr}M$. Hence $\operatorname{tr}M = -\operatorname{tr}M = 0$.
>
> **3. Two.** $\operatorname{tr}(\gamma^\mu\gamma^\nu) = \operatorname{tr}(2g^{\mu\nu}\mathbb 1 - \gamma^\nu\gamma^\mu) = 8g^{\mu\nu} - \operatorname{tr}(\gamma^\nu\gamma^\mu) = 8g^{\mu\nu} - \operatorname{tr}(\gamma^\mu\gamma^\nu)$ (cyclicity in the last step). So $2\operatorname{tr}(\gamma^\mu\gamma^\nu) = 8g^{\mu\nu}$.
>
> **4. Four: move $\gamma^\mu$ to the right through the other three.** Each move uses $\gamma^\mu\gamma^\alpha = 2g^{\mu\alpha} - \gamma^\alpha\gamma^\mu$:
>
> $$
> \gamma^\mu\gamma^\nu\gamma^\rho\gamma^\sigma = 2g^{\mu\nu}\gamma^\rho\gamma^\sigma - \gamma^\nu\gamma^\mu\gamma^\rho\gamma^\sigma = 2g^{\mu\nu}\gamma^\rho\gamma^\sigma - 2g^{\mu\rho}\gamma^\nu\gamma^\sigma + \gamma^\nu\gamma^\rho\gamma^\mu\gamma^\sigma = 2g^{\mu\nu}\gamma^\rho\gamma^\sigma - 2g^{\mu\rho}\gamma^\nu\gamma^\sigma + 2g^{\mu\sigma}\gamma^\nu\gamma^\rho - \gamma^\nu\gamma^\rho\gamma^\sigma\gamma^\mu .
> $$
>
> **5. Take the trace.** By step 3 the first three terms give $8g^{\mu\nu}g^{\rho\sigma} - 8g^{\mu\rho}g^{\nu\sigma} + 8g^{\mu\sigma}g^{\nu\rho}$; by cyclicity $\operatorname{tr}(\gamma^\nu\gamma^\rho\gamma^\sigma\gamma^\mu) = \operatorname{tr}(\gamma^\mu\gamma^\nu\gamma^\rho\gamma^\sigma)$. So $2\operatorname{tr}(\gamma^\mu\gamma^\nu\gamma^\rho\gamma^\sigma) = 8(g^{\mu\nu}g^{\rho\sigma} - g^{\mu\rho}g^{\nu\sigma} + g^{\mu\sigma}g^{\nu\rho})$.
>
> **6. Slashes.** Contract with $a_\mu b_\nu$ (and $c_\rho d_\sigma$): the components are numbers and come out of the trace.
>
> **What the derivation shows**
> - Only the Clifford algebra, $\gamma^5$ and cyclicity are used: the traces are basis independent. Tracelessness of $\gamma^\mu$ alone is also [[§C13.2★ The Dirac Equation#^thm-c13-2-2|QM Theorem §C13.2.2]], part 2 (with $\gamma^\nu$ in place of $\gamma^5$).
> - ⚑ By-product: $\operatorname{tr}(\Gamma_A\Gamma_B) = 0$ for distinct elements of the sixteen-element basis and $\ne 0$ for equal ones: the trace is an inner product in which the basis is orthogonal; this is how the basis property is proved ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-4|Theorem §C5a.2.4]]) and how a matrix is expanded in it, $M = \frac14\sum_A\operatorname{tr}(\Gamma_A^{-1}M)\,\Gamma_A$.
> - Used next: spin sums turn squared amplitudes into traces ([[§C5a.7 Gamma-Matrix Technology#^rem-c5a-7-1|Remark: Why traces]]).

^der-c5a-7-3

*Uses:* [[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-1|Def. §C5a.2.1]], [[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-13|Theorem §C5a.2.13]], [[§33 Trace꞉ A Connection Between Matrices and Operators#^ladr-8-49|LADR Thm. 8.49]]

> [!theorem] Theorem §C5a.7.4: Traces with γ⁵
> $$
> \operatorname{tr}\gamma^5 = 0\ \text{(recalled)}, \qquad \operatorname{tr}(\gamma^\mu\gamma^\nu\gamma^5) = 0, \qquad \operatorname{tr}(\gamma^\mu\gamma^\nu\gamma^\rho\gamma^\sigma\gamma^5) = -4i\,\varepsilon^{\mu\nu\rho\sigma} \quad (\varepsilon^{0123} = +1),
> $$
>
> with $\gamma^5 = i\gamma^0\gamma^1\gamma^2\gamma^3$ ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-5|Def. §C5a.2.5]]; $\operatorname{tr}\gamma^5 = 0$ is [[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-13|Theorem §C5a.2.13]]) and $\varepsilon$ in the convention of [[§C1.5 Vectors, Tensors and Index Notation#^cau-c1-5-5|§C1.5, Caution: The sign of ε⁰¹²³]]; the trace of $\gamma^5$ times an odd number of $\gamma$'s vanishes. The convention-free form of the last identity is $\operatorname{tr}(\gamma^0\gamma^1\gamma^2\gamma^3\gamma^5) = -4i$.
>
> *Source: Yu §8.2.2, eqs. (8.46)–(8.48), (8.53)–(8.55) (with $\varepsilon^{0123} = +1$, Yu (1.104)) · PS §5.1 (as statements)*

^thm-c5a-7-4

> [!derivation]- Derivation
> **1. Odd number with $\gamma^5$.** $\gamma^5 = i\gamma^0\gamma^1\gamma^2\gamma^3$ is a product of four $\gamma$'s, so $\gamma^5$ times an odd number of $\gamma$'s is an odd product: trace zero by [[§C5a.7 Gamma-Matrix Technology#^thm-c5a-7-3|Theorem §C5a.7.3]].
>
> **2. $\operatorname{tr}\gamma^5$.** Recalled from its home, [[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-13|Theorem §C5a.2.13]], where it is derived (insert $(\gamma^0)^2 = \mathbb 1$, anticommute, use cyclicity).
>
> **3. Two $\gamma$'s and $\gamma^5$.** If $\mu = \nu$: $\gamma^\mu\gamma^\mu = g^{\mu\mu}$ (no sum), and the trace is $g^{\mu\mu}\operatorname{tr}\gamma^5 = 0$. If $\mu \ne \nu$: pick $\alpha \ne \mu, \nu$, so $(\gamma^\alpha)^2 = g^{\alpha\alpha} = \pm1$ and $\gamma^\alpha$ anticommutes with $\gamma^\mu$, $\gamma^\nu$, $\gamma^5$. Then $\operatorname{tr}(\gamma^\mu\gamma^\nu\gamma^5) = g^{\alpha\alpha}\operatorname{tr}(\gamma^\mu\gamma^\nu\gamma^5\gamma^\alpha\gamma^\alpha)$. Move the first $\gamma^\alpha$ to the front past three anticommuting factors: $= -g^{\alpha\alpha}\operatorname{tr}(\gamma^\alpha\gamma^\mu\gamma^\nu\gamma^5\gamma^\alpha) = -g^{\alpha\alpha}\operatorname{tr}(\gamma^\alpha\gamma^\alpha\gamma^\mu\gamma^\nu\gamma^5)$ (cyclicity) $= -\operatorname{tr}(\gamma^\mu\gamma^\nu\gamma^5)$. So it is $0$.
>
> **4. Four $\gamma$'s and $\gamma^5$, a repeated index.** If two of $\mu\nu\rho\sigma$ coincide, anticommute them next to each other (distinct ones anticommute, costing only signs), replace the pair by $g^{\alpha\alpha}$, and step 3 gives zero; so does $\varepsilon^{\mu\nu\rho\sigma}$.
>
> **5. Distinct indices.** Then $\mu\nu\rho\sigma$ is a permutation of $0123$, and reordering $\gamma^\mu\gamma^\nu\gamma^\rho\gamma^\sigma$ to $\gamma^0\gamma^1\gamma^2\gamma^3$ costs the sign of the permutation, which is $\varepsilon^{\mu\nu\rho\sigma}$ for $\varepsilon^{0123} = +1$. So $\operatorname{tr}(\gamma^\mu\gamma^\nu\gamma^\rho\gamma^\sigma\gamma^5) = \varepsilon^{\mu\nu\rho\sigma}\operatorname{tr}(\gamma^0\gamma^1\gamma^2\gamma^3\gamma^5)$.
>
> **6. The one number.** From the definition, $\gamma^0\gamma^1\gamma^2\gamma^3 = -i\gamma^5$, so $\operatorname{tr}(\gamma^0\gamma^1\gamma^2\gamma^3\gamma^5) = -i\operatorname{tr}((\gamma^5)^2) = -i\operatorname{tr}\mathbb 1 = -4i$.
>
> **What the derivation shows**
> - ⚑ By-product: the sign of the $\varepsilon$ trace depends on the $\varepsilon$ convention, the number $-4i$ in step 6 does not → [[§C5a.7 Gamma-Matrix Technology#^cau-c5a-7-1|Caution: The sign of the ε trace across sources]].
> - $\gamma^5$ traces produce one $\varepsilon$, hence pseudoscalar structures such as $\varepsilon^{\mu\nu\rho\sigma}p_\mu k_\nu p'_\rho k'_\sigma$ in parity-violating amplitudes.

^der-c5a-7-4

*Uses:* [[§C5a.7 Gamma-Matrix Technology#^thm-c5a-7-3|Theorem §C5a.7.3]], [[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-5|Def. §C5a.2.5]], [[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-13|Theorem §C5a.2.13]]

> [!caution] Caution: The sign of the ε trace across sources
> The convention-free statements are $\gamma^0\gamma^1\gamma^2\gamma^3 = -i\gamma^5$ and $\operatorname{tr}(\gamma^0\gamma^1\gamma^2\gamma^3\gamma^5) = -4i$. With $\varepsilon^{0123} = +1$ (these notes, the course, Yu) they give $\operatorname{tr}(\gamma^\mu\gamma^\nu\gamma^\rho\gamma^\sigma\gamma^5) = -4i\varepsilon^{\mu\nu\rho\sigma}$, $\gamma^{[\mu\nu\rho\sigma]} = -i\varepsilon^{\mu\nu\rho\sigma}\gamma^5$ and $\gamma^5 = -\frac i{4!}\varepsilon^{\mu\nu\rho\sigma}\gamma_\mu\gamma_\nu\gamma_\rho\gamma_\sigma$. Peskin–Schroeder state $\varepsilon^{0123} = -1$, and their p. 50 is not uniform: (3.68) and $\gamma^{\mu\nu\rho\sigma} = -i\varepsilon^{\mu\nu\rho\sigma}\gamma^5$ hold as printed only for $\varepsilon^{0123} = +1$, while $\gamma^{\mu\nu\rho} = -i\varepsilon^{\mu\nu\rho\sigma}\gamma_\sigma\gamma^5$ holds for their $\varepsilon^{0123} = -1$ (it is Theorem §C5a.7.6 with the sign of $\varepsilon$ flipped). Check: $\gamma^0\gamma^1\gamma^2 = -i\gamma^3\gamma^5$ from the definition of $\gamma^5$. Compare sources through the convention-free forms.
>
> *Source: PS §3.4, p. 50, eq. (3.68) · Yu §8.2.2, eq. (8.48) · checked against Derivation §C5a.7.4, step 6*

^cau-c5a-7-1

> [!remark] Remark: Why traces
> An unpolarized squared amplitude sums over spins: $\sum_{s,s'}\lvert\bar u^{s'}(p')\Gamma u^s(p)\rvert^2 = \sum\bar u^{s'}\Gamma u^s\,\bar u^s\bar\Gamma u^{s'}$, and the spin sums $\sum_su^s\bar u^s = \slashed{p} + m$, $\sum_sv^s\bar v^s = \slashed{p} - m$ ([[§C5a.6 Normalization, Spin Sums and Helicity#^thm-c5a-6-7|Theorem §C5a.6.7]], [[§C5a.6 Normalization, Spin Sums and Helicity#^thm-c5a-6-8|Theorem §C5a.6.8]]) close the chain of matrices into a loop: $\operatorname{tr}[\Gamma(\slashed{p} + m)\bar\Gamma(\slashed{p}' + m)]$ (Casimir's trick, Yu (7.47)). Every fermion line of an unpolarized cross section becomes a trace, and Theorems §C5a.7.2–§C5a.7.4 evaluate it without ever writing a spinor (QFT C7–C8, planned). Closed fermion loops give traces for the same reason.
>
> *Source: Yu §7.1, eq. (7.47) and the paragraph after it; §8.2.1, eq. (8.43)*

^rem-c5a-7-1

## γ⁵ and the ε symbol

> [!theorem] Theorem §C5a.7.5: γ⁵ as a Totally Antisymmetric Product
> $$
> \gamma^5 = -\frac i{24}\,\varepsilon_{\kappa\lambda\mu\nu}\,\gamma^\kappa\gamma^\lambda\gamma^\mu\gamma^\nu, \qquad \gamma^{[\kappa}\gamma^\lambda\gamma^\mu\gamma^{\nu]} = -i\,\varepsilon^{\kappa\lambda\mu\nu}\gamma^5 ,
> $$
>
> with $\gamma^5$ of [[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-5|Def. §C5a.2.5]], the antisymmetrization of [[§C5a.7 Gamma-Matrix Technology#^def-c5a-7-1|Def. §C5a.7.1]], and $\varepsilon^{0123} = +1 = -\varepsilon_{0123}$ ([[§C5a.7 Gamma-Matrix Technology#^cau-c5a-7-1|Caution: The sign of the ε trace across sources]]).
>
> *Source: PHY 513, Problem Set 5, Problem 5(c) (as the user wrote it) · the user's PHY 513 notes, Ch. 9 §9.6 (Principle "Properties of $\gamma^5$") · PS §3.4, p. 50, eq. (3.68)*

^thm-c5a-7-5

> [!derivation]- Derivation (as the user wrote it for Problem Set 5, Problem 5(c))
> **1. Swapping neighbours.** For $\kappa \ne \lambda$, $\gamma^\kappa\gamma^\lambda = 2g^{\kappa\lambda} - \gamma^\lambda\gamma^\kappa = -\gamma^\lambda\gamma^\kappa$ ($g$ is diagonal). So in a product of $\gamma$'s with distinct indices each neighbour swap gives $-1$. If $(\kappa, \lambda, \mu, \nu)$ is a permutation of $(0, 1, 2, 3)$, reordering the $\gamma$'s to $\gamma^0\gamma^1\gamma^2\gamma^3$ gives the same sign as reordering the indices of $\varepsilon$ to $0123$:
>
> $$
> \varepsilon_{\kappa\lambda\mu\nu}\gamma^\kappa\gamma^\lambda\gamma^\mu\gamma^\nu\ \text{(no sum)} = \varepsilon_{0123}\,\gamma^0\gamma^1\gamma^2\gamma^3 = -\gamma^0\gamma^1\gamma^2\gamma^3 .
> $$
>
> **2. First identity: count.** In the sum over $\kappa\lambda\mu\nu$, a term vanishes unless all four are distinct ($\varepsilon = 0$ otherwise). Fix $\kappa$ (4 options), $\lambda \ne \kappa$ (3), $\mu \ne \kappa, \lambda$ (2); then $\nu$ is the remaining index. Each of the $4\cdot3\cdot2 = 24$ terms equals $-\gamma^0\gamma^1\gamma^2\gamma^3$ by step 1. With $\gamma^0\gamma^1\gamma^2\gamma^3 = \gamma^5/i = -i\gamma^5$:
>
> $$
> \varepsilon_{\kappa\lambda\mu\nu}\gamma^\kappa\gamma^\lambda\gamma^\mu\gamma^\nu = -24\,\gamma^0\gamma^1\gamma^2\gamma^3 = 24i\,\gamma^5, \qquad \gamma^5 = \frac1{24i}\varepsilon_{\kappa\lambda\mu\nu}\gamma^\kappa\gamma^\lambda\gamma^\mu\gamma^\nu = -\frac i{24}\varepsilon_{\kappa\lambda\mu\nu}\gamma^\kappa\gamma^\lambda\gamma^\mu\gamma^\nu .
> $$
>
> **3. Second identity, distinct indices.** Each of the 24 terms of the antisymmetrization (Def. §C5a.7.1) is $\gamma^{\kappa'}\gamma^{\lambda'}\gamma^{\mu'}\gamma^{\nu'}$ for a permutation of $(\kappa, \lambda, \mu, \nu)$, weighted by its sign; reordering it back by neighbour swaps gives the same sign again, so every term equals $+\gamma^\kappa\gamma^\lambda\gamma^\mu\gamma^\nu$ and $\gamma^{[\kappa\lambda\mu\nu]} = \frac1{24}\cdot24\,\gamma^\kappa\gamma^\lambda\gamma^\mu\gamma^\nu$. By the neighbour swaps relative to $0123$, this is $\varepsilon^{\kappa\lambda\mu\nu}\gamma^0\gamma^1\gamma^2\gamma^3$ (with $\varepsilon^{0123} = +1$) $= -i\varepsilon^{\kappa\lambda\mu\nu}\gamma^5$.
>
> **4. Repeated indices.** If two indices coincide, $\varepsilon^{\kappa\lambda\mu\nu} = 0$, and the antisymmetrization vanishes: pair each term with the one in which the positions of the two equal indices are exchanged; the products are identical and the signs opposite.
>
> **What the derivation shows**
> - The lower-index $\varepsilon_{0123} = -1$ in step 2 and the upper-index $\varepsilon^{0123} = +1$ in step 3 are the two places where the convention enters ([[§C5a.7 Gamma-Matrix Technology#^cau-c5a-7-1|Caution: The sign of the ε trace across sources]]).
> - ⚑ By-product: $\gamma^5 \propto \varepsilon$ is why bilinears with $\gamma^5$ are "pseudo" ([[§C5a.4 Bilinears, Chirality and the Weyl Equations#^thm-c5a-4-2|Theorem §C5a.4.2]]).

^der-c5a-7-5

*Uses:* [[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-5|Def. §C5a.2.5]], [[§C5a.7 Gamma-Matrix Technology#^def-c5a-7-1|Def. §C5a.7.1]], [[§C1.5 Vectors, Tensors and Index Notation#^cau-c1-5-5|§C1.5, Caution: The sign of ε⁰¹²³]]

> [!theorem] Theorem §C5a.7.6: The Antisymmetric Product of Three γ's
> $$
> \gamma^{[\lambda}\gamma^\mu\gamma^{\nu]} = i\,\varepsilon^{\lambda\mu\nu\kappa}\,\gamma_\kappa\gamma^5 ,
> $$
>
> in the notation and $\varepsilon$ convention of [[§C5a.7 Gamma-Matrix Technology#^thm-c5a-7-5|Theorem §C5a.7.5]].
>
> *Source: PHY 513, Problem Set 5, Problem 5(d), first identity (as the user wrote it) · the user's PHY 513 notes, Ch. 9 §9.6 · PS §3.4, p. 50 ($\gamma^{\mu\nu\rho} = -i\varepsilon^{\mu\nu\rho\sigma}\gamma_\sigma\gamma^5$, with PS's $\varepsilon^{0123} = -1$)*

^thm-c5a-7-6

> [!derivation]- Derivation (as the user wrote it for Problem Set 5, Problem 5(d))
> **1. Only distinct indices matter.** If two of $\lambda, \mu, \nu$ coincide, both sides vanish (the antisymmetrization cancels in pairs; $\varepsilon = 0$). Let them be distinct: then each of the $3! = 6$ terms of $\gamma^{[\lambda\mu\nu]}$, reordered by neighbour swaps, gives the same sign twice, and $\gamma^{[\lambda\mu\nu]} = \gamma^\lambda\gamma^\mu\gamma^\nu$.
>
> **2. Multiply Theorem §C5a.7.5 by $\gamma_\kappa$ and sum over $\kappa$.** $\sum_\kappa\gamma_\kappa\gamma^{[\kappa\lambda\mu\nu]} = -i\varepsilon^{\kappa\lambda\mu\nu}\gamma_\kappa\gamma^5$.
>
> **3. Left side.** Only the one $\kappa$ distinct from $\lambda, \mu, \nu$ contributes (the other three terms vanish by step 4 of Derivation §C5a.7.5). For it, $\gamma^{[\kappa\lambda\mu\nu]} = \gamma^\kappa\gamma^\lambda\gamma^\mu\gamma^\nu = \gamma^\kappa\gamma^{[\lambda\mu\nu]}$, and $\gamma_\kappa\gamma^\kappa = g_{\kappa\kappa}g^{\kappa\kappa} = 1$ (no sum). The left side is $\gamma^{[\lambda\mu\nu]}$.
>
> **4. Right side.** Moving $\kappa$ to the last slot of $\varepsilon$ takes three neighbour swaps: $\varepsilon^{\kappa\lambda\mu\nu} = -\varepsilon^{\lambda\mu\nu\kappa}$. So $\gamma^{[\lambda\mu\nu]} = -i\varepsilon^{\kappa\lambda\mu\nu}\gamma_\kappa\gamma^5 = i\varepsilon^{\lambda\mu\nu\kappa}\gamma_\kappa\gamma^5$.
>
> **What the derivation shows**
> - The four antisymmetric products of three $\gamma$'s are the four $\gamma_\kappa\gamma^5$: nothing new beyond the axial-vector matrices.

^der-c5a-7-6

*Uses:* [[§C5a.7 Gamma-Matrix Technology#^thm-c5a-7-5|Theorem §C5a.7.5]], [[§C5a.7 Gamma-Matrix Technology#^def-c5a-7-1|Def. §C5a.7.1]]

> [!theorem] Theorem §C5a.7.7: γ⁵ Dualizes σ^μν
> $$
> \gamma^5\sigma_{\mu\nu} = \frac i2\,\varepsilon_{\mu\nu\lambda\kappa}\,\sigma^{\lambda\kappa} ,
> $$
>
> for any normalization $\sigma^{\mu\nu} = c\,[\gamma^\mu, \gamma^\nu]$ (the identity is homogeneous; [[§C5a.4 Bilinears, Chirality and the Weyl Equations#^cau-c5a-4-1|§C5a.4, Caution: Three normalizations of σ^μν]]), with $\varepsilon^{0123} = +1$ ([[§C5a.7 Gamma-Matrix Technology#^cau-c5a-7-1|Caution: The sign of the ε trace across sources]]). $\gamma^5\sigma^{\mu\nu}$ is therefore not a new matrix.
>
> *Source: PHY 513, Problem Set 5, Problem 5(d), second identity (as the user wrote it, with $\sigma^{\mu\nu} = \frac1{4i}[\gamma^\mu, \gamma^\nu]$) · the user's PHY 513 notes, Ch. 9 §9.6 (Derivation "Proof of the properties of $\gamma^5$", "Duality")*

^thm-c5a-7-7

> [!derivation]- Derivation
> Write $\gamma^{[\mu\nu]} = \frac12[\gamma^\mu, \gamma^\nu]$; every normalization of $\sigma$ is a constant times it.
>
> **1. Both sides vanish for $\mu = \nu$.** Assume $\mu \ne \nu$.
>
> **2. Contract Theorem §C5a.7.6 with $\gamma_\lambda$.** Left: $\sum_\lambda\gamma_\lambda\gamma^{[\lambda\mu\nu]}$; the terms with $\lambda = \mu$ or $\nu$ vanish; for each of the two $\lambda$ distinct from $\mu, \nu$, $\gamma_\lambda\gamma^{[\lambda\mu\nu]} = \gamma_\lambda\gamma^\lambda\gamma^\mu\gamma^\nu = \gamma^\mu\gamma^\nu = \gamma^{[\mu\nu]}$ (no sum; distinct indices). The left side is $2\gamma^{[\mu\nu]}$.
>
> **3. Right side.** $i\varepsilon^{\lambda\mu\nu\kappa}\gamma_\lambda\gamma_\kappa\gamma^5 = i\varepsilon^{\mu\nu\lambda\kappa}\gamma_\lambda\gamma_\kappa\gamma^5$ (moving $\lambda$ past $\mu\nu$: two swaps). By antisymmetry of $\varepsilon$ in $\lambda\kappa$ (rename $\lambda \leftrightarrow \kappa$ and average), $\varepsilon^{\mu\nu\lambda\kappa}\gamma_\lambda\gamma_\kappa = \varepsilon^{\mu\nu\lambda\kappa}\gamma_{[\lambda\kappa]}$. So $2\gamma^{[\mu\nu]} = i\varepsilon^{\mu\nu\lambda\kappa}\gamma_{[\lambda\kappa]}\gamma^5$.
>
> **4. Move indices.** Both sides are tensors; lower $\mu\nu$ and raise $\lambda\kappa$ by contracting with $g_{\mu\alpha}g_{\nu\beta}$ and inserting $g^{\lambda\rho}g_{\rho\lambda'}$ pairs (the dummy pair $\lambda\kappa$ may be moved up and down together). The $\varepsilon$ with indices $\mu\nu$ down and $\lambda\kappa$ up is the same tensor with indices moved by $g$; with all four lowered, $\varepsilon_{0123} = g_{00}g_{11}g_{22}g_{33}\varepsilon^{0123} = -1$, consistently. Result: $\gamma_{[\mu\nu]} = \frac i2\varepsilon_{\mu\nu\lambda\kappa}\gamma^{[\lambda\kappa]}\gamma^5$.
>
> **5. Move $\gamma^5$ to the left.** $\gamma^5$ commutes with a product of two $\gamma$'s ($\gamma^5\gamma^\lambda\gamma^\kappa = (-1)^2\gamma^\lambda\gamma^\kappa\gamma^5$, [[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-13|Theorem §C5a.2.13]]). Multiply on the left by $\gamma^5$ and use $(\gamma^5)^2 = \mathbb 1$: $\gamma^5\gamma_{[\mu\nu]} = \frac i2\varepsilon_{\mu\nu\lambda\kappa}\gamma^{[\lambda\kappa]}$.
>
> **6. Normalization.** Multiply both sides by the same constant $2c$: $\gamma^5\sigma_{\mu\nu} = \frac i2\varepsilon_{\mu\nu\lambda\kappa}\sigma^{\lambda\kappa}$ for $\sigma = c[\gamma, \gamma]$. (The user's write-up, with $\sigma = \frac1{4i}[\gamma, \gamma]$, runs steps 2–5 with $4i\sigma^{\mu\nu} = 2\gamma^{[\mu\nu]}$ in place of $\gamma^{[\mu\nu]}$.)
>
> **What the derivation shows**
> - $\gamma^5$ acts on the six $\sigma^{\mu\nu}$ as the Hodge dual: it exchanges the "electric" $\sigma^{0i}$ with the "magnetic" $\sigma^{jk}$, the matrix version of $\mathbf E \leftrightarrow \mathbf B$ duality ([[§C1.5 Vectors, Tensors and Index Notation#^thm-c1-5-7|Theorem §C1.5.7]]). Its eigenspaces $\gamma^5 = \mp1$ are the self-dual and anti-self-dual halves, $(1, 0)$ and $(0, 1)$: $\sigma^{\mu\nu}P_{L,R}$ is the tensor bilinear of a single chirality.

^der-c5a-7-7

*Uses:* [[§C5a.7 Gamma-Matrix Technology#^thm-c5a-7-6|Theorem §C5a.7.6]], [[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-13|Theorem §C5a.2.13]]

## Reduction

> [!theorem] Theorem §C5a.7.8: Every Product of γ's Reduces to the Standard Basis
> For any indices, a product of Dirac matrices ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-1|Def. §C5a.2.1]]) $\gamma^{\mu_1}\gamma^{\mu_2}\cdots\gamma^{\mu_n}$ is a linear combination, with coefficients built from $g^{\mu\nu}$ and $\varepsilon^{\mu\nu\rho\sigma}$, of the sixteen matrices
>
> $$
> \mathbb 1, \quad \gamma^\mu, \quad \sigma^{\mu\nu}\ (\mu < \nu), \quad \gamma^\mu\gamma^5, \quad \gamma^5 ,
> $$
>
> ($\sigma^{\mu\nu}$ of [[§C5a.4 Bilinears, Chirality and the Weyl Equations#^def-c5a-4-2|Def. §C5a.4.2]], $\gamma^5$ of [[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-5|Def. §C5a.2.5]]), with only the terms of the parity of $n$ (even $n$: $\mathbb 1$, $\sigma^{\mu\nu}$, $\gamma^5$; odd $n$: $\gamma^\mu$, $\gamma^\mu\gamma^5$). The combination is unique.
>
> *Source: PHY 513, Problem Set 5, Problem 5 (closing paragraph of the problem statement) · the user's PHY 513 notes, Ch. 9 §9.6 (Principle "Reducing any product of $\gamma$'s") · PS §3.4, p. 49*

^thm-c5a-7-8

> [!derivation]- Derivation
> **1. One component at a time.** Fix numerical values of $\mu_1, \dots, \mu_n \in \{0, 1, 2, 3\}$. If some value occurs twice, anticommute one copy next to the other (each passage over a $\gamma$ with a different index costs $-1$; passing an equal one is not needed, take the nearest copy) and replace the pair by $\gamma^\alpha\gamma^\alpha = g^{\alpha\alpha} = \pm1$. Repeat. The result is $\pm\gamma^{\alpha_1}\cdots\gamma^{\alpha_k}$ with distinct $\alpha$'s, the values occurring an odd number of times; $k \le 4$ and $k \equiv n \pmod 2$ (each step removes two factors).
>
> **2. Distinct products are basis elements.** Order the $\alpha$'s increasingly (anticommuting, signs only). For $k = 0$: $\mathbb 1$. $k = 1$: $\gamma^\alpha$. $k = 2$: $\gamma^\alpha\gamma^\beta = \gamma^{[\alpha\beta]} = -i\sigma^{\alpha\beta}$ ($\alpha \ne \beta$; Def. §C5a.7.1). $k = 3$: $\gamma^{[\alpha\beta\gamma]} = i\varepsilon^{\alpha\beta\gamma\kappa}\gamma_\kappa\gamma^5$ (Theorem §C5a.7.6), a single term. $k = 4$: $\gamma^0\gamma^1\gamma^2\gamma^3 = -i\gamma^5$.
>
> **3. Covariant form.** Steps 1–2 hold for every choice of index values, so the tensor $\gamma^{\mu_1}\cdots\gamma^{\mu_n}$ equals a sum of antisymmetrized products times products of $g$'s; the user's procedure does this covariantly: split each adjacent pair into its symmetric part, $g^{\mu\nu}\mathbb 1$ by the Clifford algebra, and its antisymmetric part, and repeat until every term is fully antisymmetric or a multiple of $\mathbb 1$. For three factors the result is $\gamma^\lambda\gamma^\mu\gamma^\nu = \gamma^{[\lambda\mu\nu]} + g^{\lambda\mu}\gamma^\nu - g^{\lambda\nu}\gamma^\mu + g^{\mu\nu}\gamma^\lambda$ (case check in [[§C5a.4 Bilinears, Chirality and the Weyl Equations#^der-c5a-4-14|Derivation §C5a.4.14]], step 1). Antisymmetrized products of five or more vanish; those of four and three are $\gamma^5$ and $\gamma_\kappa\gamma^5$ (Theorems §C5a.7.5–§C5a.7.6); $\gamma^5\sigma^{\mu\nu}$ is a combination of $\sigma$'s (Theorem §C5a.7.7).
>
> **4. Uniqueness.** The sixteen matrices are linearly independent ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-4|Theorem §C5a.2.4]]; the standard ones differ from the products $\gamma^I$ by nonzero factors $\pm1, \pm i$), so the coefficients are unique, and can be read off with traces ([[§C5a.7 Gamma-Matrix Technology#^thm-c5a-7-3|Theorem §C5a.7.3]], by-product).
>
> **What the derivation shows**
> - "Nothing beyond the sixteen is ever needed": the classification of bilinears ([[§C5a.4 Bilinears, Chirality and the Weyl Equations#^def-c5a-4-2|Def. §C5a.4.2]]) is complete.
> - ⚑ By-product: the parity of the number of $\gamma$'s is preserved by every step, which is why odd products are traceless and why $\gamma^5$ (even) commutes with $\sigma^{\mu\nu}$ and anticommutes with $\gamma^\mu$.

^der-c5a-7-8

*Uses:* [[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-1|Def. §C5a.2.1]], [[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-4|Theorem §C5a.2.4]], [[§C5a.7 Gamma-Matrix Technology#^thm-c5a-7-5|Theorem §C5a.7.5]], [[§C5a.7 Gamma-Matrix Technology#^thm-c5a-7-6|Theorem §C5a.7.6]], [[§C5a.7 Gamma-Matrix Technology#^thm-c5a-7-7|Theorem §C5a.7.7]]

## The Gordon identity

> [!theorem] Theorem §C5a.7.9: The Gordon Identity
> Let $p^2 = p'^2 = m^2 > 0$, $q = p' - p$, and let $u(p)$, $u(p')$ be positive-frequency spinors ([[§C5a.5 Plane-Wave Solutions#^def-c5a-5-1|Def. §C5a.5.1]]), $\bar u = u^\dagger\gamma^0$ ([[§C5a.3 The Dirac Equation and Its Lagrangian#^def-c5a-3-3|Def. §C5a.3.3]]), $(\slashed{p} - m)u(p) = 0$ and $(\slashed{p}' - m)u(p') = 0$ ([[§C5a.5 Plane-Wave Solutions#^thm-c5a-5-1|Theorem §C5a.5.1]]). Then
>
> $$
> \bar u(p')\gamma^\mu u(p) = \bar u(p')\Bigl[\frac{p^\mu + p'^\mu}{2m} + \frac{i\sigma^{\mu\nu}q_\nu}{2m}\Bigr]u(p), \qquad \sigma^{\mu\nu} = \frac i2[\gamma^\mu, \gamma^\nu] .
> $$
>
> Here $\sigma^{\mu\nu}$ is Peskin–Schroeder's ([[§C5a.4 Bilinears, Chirality and the Weyl Equations#^def-c5a-4-2|Def. §C5a.4.2]]); with another normalization the coefficient of the second term changes ([[§C5a.4 Bilinears, Chirality and the Weyl Equations#^cau-c5a-4-1|§C5a.4, Caution: Three normalizations of σ^μν]]). It is not a matrix identity: it holds only between on-shell spinors.
>
> *Source: PHY 513, Problem Set 5, Problem 3 (as the user wrote it; based on PS Problem 3.2) · the user's PHY 513 notes, Ch. 9 §9.6 (Principle "The Gordon identity", eq. (gordon))*

^thm-c5a-7-9

> [!derivation]- Derivation (the user's notes: split γ^μ in half)
> **1. The Dirac equation from both sides.** $\slashed{p}\,u(p) = m\,u(p)$ by hypothesis. For $u(p')$: take the adjoint of $(\slashed{p}' - m)u(p') = 0$ with $p'_\mu$ real, $u^\dagger(p')(\gamma^{\mu\dagger}p'_\mu - m) = 0$; insert $\gamma^0\gamma^0 = \mathbb 1$ on the left of the bracket and multiply by $\gamma^0$ on the right: $\bar u(p')(\gamma^0\gamma^{\mu\dagger}\gamma^0p'_\mu - m) = 0$, and $\gamma^0\gamma^{\mu\dagger}\gamma^0 = \gamma^\mu$ ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-3|Theorem §C5a.2.3]]): $\bar u(p')\slashed{p}' = m\,\bar u(p')$. Each acts only when the slashed momentum stands next to its own spinor.
>
> **2. Split $\gamma^\mu$ in half.** Using step 1 once on each side (with $m \ne 0$):
>
> $$
> \bar u(p')\gamma^\mu u(p) = \tfrac12\bar u(p')\gamma^\mu\tfrac{\slashed{p}}{m}u(p) + \tfrac12\bar u(p')\tfrac{\slashed{p}'}{m}\gamma^\mu u(p) = \frac1{2m}\bar u(p')\bigl(\gamma^\mu\slashed{p} + \slashed{p}'\gamma^\mu\bigr)u(p) .
> $$
>
> **3. Symmetric and antisymmetric parts.** $\gamma^\mu\gamma^\nu = g^{\mu\nu} - i\sigma^{\mu\nu}$ ([[§C5a.7 Gamma-Matrix Technology#^thm-c5a-7-1|Theorem §C5a.7.1]], step 4). Contracting with $p_\nu$: $\gamma^\mu\slashed{p} = p^\mu - i\sigma^{\mu\nu}p_\nu$. For the other order, $\slashed{p}'\gamma^\mu = p'_\nu\gamma^\nu\gamma^\mu = p'^\mu - i\sigma^{\nu\mu}p'_\nu = p'^\mu + i\sigma^{\mu\nu}p'_\nu$ ($\sigma$ antisymmetric).
>
> **4. Add.** $\gamma^\mu\slashed{p} + \slashed{p}'\gamma^\mu = p^\mu + p'^\mu + i\sigma^{\mu\nu}(p' - p)_\nu$. Insert into step 2.
>
> **What the derivation shows**
> - Only the two on-shell conditions and the Clifford algebra are used; $p^2 = m^2$ enters through the existence of $u$.
> - ⚑ By-product: the identity requires $m \ne 0$; for massless spinors the vector current cannot be split this way.

^der-c5a-7-9

*Uses:* [[§C5a.5 Plane-Wave Solutions#^thm-c5a-5-1|Theorem §C5a.5.1]], [[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-3|Theorem §C5a.2.3]], [[§C5a.7 Gamma-Matrix Technology#^thm-c5a-7-1|Theorem §C5a.7.1]]

> [!derivation]- Derivation (second route: Problem Set 5, Problem 3, as the user wrote it)
> **1. Expand the right side.** With $\sigma^{\mu\nu} = \frac i2[\gamma^\mu, \gamma^\nu]$ and $q = p' - p$, $i\sigma^{\mu\nu}q_\nu = i\cdot\frac i2(\gamma^\mu\gamma^\nu - \gamma^\nu\gamma^\mu)(p' - p)_\nu = -\frac12(\gamma^\mu\slashed{p}' - \slashed{p}'\gamma^\mu - \gamma^\mu\slashed{p} + \slashed{p}\gamma^\mu)$. So the bracket is $\frac1{2m}\bigl[p^\mu + p'^\mu - \frac12(\gamma^\mu\slashed{p}' - \slashed{p}'\gamma^\mu - \gamma^\mu\slashed{p} + \slashed{p}\gamma^\mu)\bigr]$.
>
> **2. Move $\slashed{p}'$ to the left and $\slashed{p}$ to the right**, where the Dirac equations act:
>
> $$
> \gamma^\mu\slashed{p}' - \slashed{p}'\gamma^\mu = (2p'^\mu - \slashed{p}'\gamma^\mu) - \slashed{p}'\gamma^\mu = 2p'^\mu - 2\slashed{p}'\gamma^\mu, \qquad -\gamma^\mu\slashed{p} + \slashed{p}\gamma^\mu = -\gamma^\mu\slashed{p} + (2p^\mu - \gamma^\mu\slashed{p}) = 2p^\mu - 2\gamma^\mu\slashed{p} .
> $$
>
> **3. Collect.** The bracket becomes $\frac1{2m}\bigl[p^\mu + p'^\mu - p'^\mu + \slashed{p}'\gamma^\mu - p^\mu + \gamma^\mu\slashed{p}\bigr] = \frac1{2m}(\slashed{p}'\gamma^\mu + \gamma^\mu\slashed{p})$: the $p^\mu + p'^\mu$ cancel.
>
> **4. The Dirac equation in momentum space.** The plane wave $\psi = u(p)e^{-ip\cdot x}$ obeys $(i\gamma^\mu\partial_\mu - m)\psi = 0$; $i\gamma^\mu\partial_\mu\psi = i\gamma^\mu(-ip_\mu)u\,e^{-ip\cdot x} = \slashed{p}\,u\,e^{-ip\cdot x}$, so $\slashed{p}\,u(p) = mu(p)$; at $p'$, its adjoint as in step 1 of the first route gives $\bar u(p')\slashed{p}' = m\bar u(p')$.
>
> **5. Conclude.** $\bar u(p')\bigl[\frac{\slashed{p}'}{2m}\gamma^\mu + \gamma^\mu\frac{\slashed{p}}{2m}\bigr]u(p) = \frac12\bar u(p')\gamma^\mu u(p) + \frac12\bar u(p')\gamma^\mu u(p) = \bar u(p')\gamma^\mu u(p)$.
>
> **What the derivation shows**
> - The same two ingredients as the first route, run from the right side to the left.

^der-c5a-7-9b

*Uses:* [[§C5a.5 Plane-Wave Solutions#^thm-c5a-5-1|Theorem §C5a.5.1]], [[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-3|Theorem §C5a.2.3]], [[§C5a.7 Gamma-Matrix Technology#^thm-c5a-7-1|Theorem §C5a.7.1]], [[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-6|Theorem §C5a.3.6]]

> [!remark] Remark: What the Gordon identity says
> The left side is the matrix element of the Dirac current $\bar\psi\gamma^\mu\psi$ ([[§C5a.4 Bilinears, Chirality and the Weyl Equations#^thm-c5a-4-9|Theorem §C5a.4.9]]), the current a photon couples to. The identity splits it in two. The term $(p + p')^\mu/2m$ has the momentum structure of the current of a charged scalar, $i(\phi^*\partial^\mu\phi - \phi\partial^\mu\phi^*)$ ([[§C1.11 Noether's Theorem#^thm-c1-11-5|Theorem §C1.11.5]], sign aside): pure convection. The term with $\sigma^{\mu\nu}q_\nu$ involves the spin ($\sigma^{ij} = 2S^{ij}$, twice the spin operator); coupled to $q_\nu A_\mu$, i.e. to $F_{\mu\nu}$, it is a magnetic-moment interaction $\propto\sigma^{\mu\nu}F_{\mu\nu}$, and its size relative to convection is what gives the Dirac electron $g = 2$ — the field-theoretic form of [[§C13.2★ The Dirac Equation#^thm-c13-2-5|QM Theorem §C13.2.5]]. With interactions the vertex becomes $\gamma^\mu F_1(q^2) + \frac{i\sigma^{\mu\nu}q_\nu}{2m}F_2(q^2)$, and the Gordon identity identifies $F_2(0)$ as the anomalous magnetic moment (PS §6.2; QFT C8, planned).
>
> *Source: the user's PHY 513 notes, Ch. 9 §9.6 (paragraph "What the Gordon identity says")*

^rem-c5a-7-2

> [!remark]- ★ Remark: The simplest Fierz identity
> Products of two bilinears can be rearranged by **Fierz identities**. The simplest rests on the $2\times2$ identity
>
> $$
> (\sigma^\mu)_{\alpha\beta}(\sigma_\mu)_{\gamma\delta} = 2\,\varepsilon_{\alpha\gamma}\varepsilon_{\beta\delta}
> $$
>
> (and the same for $\bar\sigma^\mu$; PS (3.77)). *Check.* $\{\mathbb 1, \sigma^i\}$ is a basis of $2\times2$ matrices orthogonal under $\operatorname{tr}(AB)$ with norm $2$, so for every $M$, $M = \frac12\operatorname{tr}(M)\mathbb 1 + \frac12\sum_i\operatorname{tr}(M\sigma^i)\sigma^i$; taking $M$ to be the matrix unit $E_{\delta\gamma}$ gives the completeness relation $\sum_i(\sigma^i)_{\alpha\beta}(\sigma^i)_{\gamma\delta} = 2\delta_{\alpha\delta}\delta_{\gamma\beta} - \delta_{\alpha\beta}\delta_{\gamma\delta}$. With $\sigma_\mu = (\mathbb 1, -\boldsymbol\sigma)$, the left side is $\delta_{\alpha\beta}\delta_{\gamma\delta} - \sum_i(\sigma^i)_{\alpha\beta}(\sigma^i)_{\gamma\delta} = 2(\delta_{\alpha\beta}\delta_{\gamma\delta} - \delta_{\alpha\delta}\delta_{\gamma\beta})$, and in two dimensions $\varepsilon_{\alpha\gamma}\varepsilon_{\beta\delta} = \delta_{\alpha\beta}\delta_{\gamma\delta} - \delta_{\alpha\delta}\delta_{\gamma\beta}$ (check the four index patterns; the sign convention of $\varepsilon$ cancels in the product). Sandwiched between commuting right-handed spinors it gives $(\bar u_{1R}\sigma^\mu u_{2R})(\bar u_{3R}\sigma_\mu u_{4R}) = -(\bar u_{1R}\sigma^\mu u_{4R})(\bar u_{3R}\sigma_\mu u_{2R})$ (PS (3.78)), antisymmetric under $2 \leftrightarrow 4$ because $\varepsilon_{\beta\delta}$ is; for anticommuting fields the reordering adds a sign. General four-component Fierz identities: PS Problem 3.6 (not used in the course).
>
> *Source: PS §3.4, pp. 51–52, eqs. (3.77)–(3.82)*

^rem-c5a-7-3

> [!remark]- Connections
> - The trace is the inner product that makes the sixteen $\Gamma$'s an orthogonal basis; the same idea expands any $2\times2$ matrix in Pauli matrices (the Fierz check above) and underlies the basis theorem — [[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-4|Theorem §C5a.2.4]], [[§B6.1 Spin One-Half and the Pauli Matrices#^thm-b6-1-4|QM Theorem §B6.1.4]].
> - Casimir's trick turns spin sums into traces: the spin sums of [[§C5a.6 Normalization, Spin Sums and Helicity|§C5a.6]] are what the trace theorems are for; the Dirac propagator's numerator $\slashed{p} + m$ is the same spin sum, so loop traces use the same identities — [[§C5a.6 Normalization, Spin Sums and Helicity#^thm-c5a-6-7|Theorem §C5a.6.7]], [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-3|Theorem §C5b.8.3]].
> - The duality $\gamma^5\sigma_{\mu\nu} = \frac i2\varepsilon_{\mu\nu\lambda\kappa}\sigma^{\lambda\kappa}$ is the Hodge star of antisymmetric tensors in matrix form; its eigenspaces are the $(1, 0)$ and $(0, 1)$ halves, the same split as $\mathbf E \mp i\mathbf B$ — [[§C1.5 Vectors, Tensors and Index Notation#^thm-c1-5-7|Theorem §C1.5.7]], [[§C3.3 How Fields Transform under the Lorentz Group#^thm-c3-3-7|Theorem §C3.3.7]].
> - The Gordon split of the current into convection and spin magnetization is the relativistic version of the Pauli equation's $\frac{e}{2m}(\mathbf L + 2\mathbf S)\cdot\mathbf B$, with $g = 2$ — [[§C13.2★ The Dirac Equation#^thm-c13-2-5|QM Theorem §C13.2.5]], [[§C5a.4 Bilinears, Chirality and the Weyl Equations#^thm-c5a-4-13|Theorem §C5a.4.13]].
> - $\gamma_\mu\gamma^\mu = d$ makes the contraction identities dimension dependent, the starting point of $\gamma$ algebra in dimensional regularization — QFT C7 (planned).
> - The $\varepsilon$ in $\gamma^5$ and its traces is the same pseudotensor whose sign convention separates these notes from Peskin–Schroeder — [[§C1.5 Vectors, Tensors and Index Notation#^cau-c1-5-5|§C1.5, Caution: The sign of ε⁰¹²³]], [[Larsen PHY 513]].
