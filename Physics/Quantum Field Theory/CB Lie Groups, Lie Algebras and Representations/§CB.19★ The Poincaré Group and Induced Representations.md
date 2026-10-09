---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: CB
section: CB.19
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§CB.18 Projective Representations, Wigner's Theorem and Antiunitary Symmetries]] · ↑ [[· CB Lie Groups, Lie Algebras and Representations]] · [[§CB.20 Grassmann Algebras]] →

*Sources: P. Woit, Quantum Theory, Groups and Representations, §18.1–§18.3 (semi-direct products, the Euclidean group, semi-direct product Lie algebras), §20.4 (representations of N ⋊ K, N commutative), §42.1–§42.3 (the Poincaré group, its orbits and little groups) (https://www.math.columbia.edu/~woit/QM/qmbook.pdf) · H. Osborn, Group Theory Lecture Notes (DAMTP, 2023), §4.5 (induced representations of the Poincaré group), §4.5.5 (the little group in SL(2,ℂ)) (https://www.damtp.cam.ac.uk/user/ho10/GNotes.pdf) · L. M. Borasi, Review and concrete description of the irreducible unitary representations of the universal cover of the complexified Poincaré group, arXiv:2108.10726, §3 (Wigner–Mackey theory; the realization on L² of an orbit) · the user's PHY 513 notes, Ch. 7 §7.6–§7.7 · Yu Zhao-Huan, 量子场论讲义, §3.3 (through §C3.6★–§C3.7★) · Group Theory (493) §§1–41 · the rest written here.*

★ Beyond the course's mathematics: PHY 513 uses the results (Wigner's classification, [[§C3.6★ Particle States and the Little Group|§C3.6★]]–[[§C3.7★ Massless Particles and Helicity|§C3.7★]]) but not the general theory of induced representations (decision SPEC-CB 4).

What is the Poincaré group as a group, and how are all its irreducible unitary representations built from the orbits of momenta and the little groups? The Poincaré group is a semidirect product of translations and Lorentz transformations; its unitary representations restrict on translations to momenta, the Lorentz group moves the momenta along orbits ([[§C1a.4 The Lorentz Group#^thm-c1a-4-2|Theorem §C1a.4.2]]), and a representation of the stabilizer of one momentum — the little group — induces a representation of the whole group. This section states the general construction (Wigner–Mackey) of which the course's induced representation ([[§C3.6★ Particle States and the Little Group#^thm-c3-6-4|Theorem §C3.6.4]]) is the case $\mathbb R^{1,3}\rtimes SL(2, \mathbb C)$, and computes the little groups inside $SL(2, \mathbb C)$. It builds on [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover|§CB.15]] and [[§CB.18 Projective Representations, Wigner's Theorem and Antiunitary Symmetries|§CB.18]] (Bargmann: why genuine representations of the cover suffice).

## Semidirect products and the Poincaré group

> [!definition] Definition §CB.19.1: Semidirect Product
> Let $N$ and $H$ be groups and $\varphi : H \to \operatorname{Aut}(N)$ a homomorphism. The **semidirect product** $N\rtimes_\varphi H$ is the set $N\times H$ with the product $(n, h)(n', h') = (n\,\varphi_h(n'), hh')$.
>
> *Source: P. Woit, Quantum Theory, Groups and Representations, §18.2, Definition "Semi-direct product group" (https://www.math.columbia.edu/~woit/QM/qmbook.pdf)*

^def-cb-19-1

> [!theorem] Theorem §CB.19.2: The Semidirect Product Is a Group with N Normal
> $N\rtimes_\varphi H$ ([[§CB.19★ The Poincaré Group and Induced Representations#^def-cb-19-1|Def. §CB.19.1]]) is a group with identity $(1, 1)$ and $(n, h)^{-1} = (\varphi_{h^{-1}}(n^{-1}), h^{-1})$; $N\times\{1\}$ is a normal subgroup ([[§38 Normal Subgroups#^def-38-1|493 Def. §38.1]]), $\{1\}\times H$ a subgroup, and the quotient ([[§40 Quotient Groups#^def-40-1|493 Def. §40.1]]) is isomorphic to $H$. Conjugation of $N$ by $H$ is $\varphi$: $(1, h)(n, 1)(1, h)^{-1} = (\varphi_h(n), 1)$.
>
> *Source: P. Woit, Quantum Theory, Groups and Representations, §18.2 (definition, the inverse, the associativity computation; normality as a digression) (https://www.math.columbia.edu/~woit/QM/qmbook.pdf) · identity, inverse on both sides, normality via a kernel and the quotient written here*

^thm-cb-19-2

> [!proof]- Proof
> Two facts about $\varphi$ are used throughout: each $\varphi_h$ is an automorphism of $N$, so $\varphi_h(1) = 1$, $\varphi_h(nn') = \varphi_h(n)\varphi_h(n')$, $\varphi_h(n^{-1}) = \varphi_h(n)^{-1}$; and $\varphi$ is a homomorphism, so $\varphi_{hh'} = \varphi_h\circ\varphi_{h'}$ and $\varphi_1 = \mathrm{id}_N$.
>
> **1. Associativity** (Woit §18.2). For $(n_i, h_i) \in N\rtimes_\varphi H$, by Def. §CB.19.1 twice,
>
> $$
> \bigl((n_1, h_1)(n_2, h_2)\bigr)(n_3, h_3) = \bigl(n_1\varphi_{h_1}(n_2), h_1h_2\bigr)(n_3, h_3) = \bigl(n_1\varphi_{h_1}(n_2)\,\varphi_{h_1h_2}(n_3),\ h_1h_2h_3\bigr) .
> $$
>
> Write $\varphi_{h_1h_2}(n_3) = \varphi_{h_1}(\varphi_{h_2}(n_3))$ (homomorphism) and $\varphi_{h_1}(n_2)\varphi_{h_1}(\varphi_{h_2}(n_3)) = \varphi_{h_1}(n_2\varphi_{h_2}(n_3))$ (automorphism). The result is $\bigl(n_1\varphi_{h_1}(n_2\varphi_{h_2}(n_3)),\ h_1(h_2h_3)\bigr) = (n_1, h_1)\bigl(n_2\varphi_{h_2}(n_3), h_2h_3\bigr) = (n_1, h_1)\bigl((n_2, h_2)(n_3, h_3)\bigr)$.
>
> **2. Identity.** $(1, 1)(n, h) = (1\cdot\varphi_1(n), h) = (n, h)$ since $\varphi_1 = \mathrm{id}$; $(n, h)(1, 1) = (n\varphi_h(1), h) = (n, h)$ since $\varphi_h(1) = 1$.
>
> **3. Inverse.** With $x = (\varphi_{h^{-1}}(n^{-1}), h^{-1})$: $(n, h)\,x = \bigl(n\,\varphi_h(\varphi_{h^{-1}}(n^{-1})), hh^{-1}\bigr) = (n\,\varphi_1(n^{-1}), 1) = (1, 1)$, and $x\,(n, h) = \bigl(\varphi_{h^{-1}}(n^{-1})\varphi_{h^{-1}}(n), 1\bigr) = (\varphi_{h^{-1}}(n^{-1}n), 1) = (1, 1)$. With Steps 1–2, $N\rtimes_\varphi H$ is a group ([[§1 The Definition of a Group#^def-1-1|493 Def. §1.1]]).
>
> **4. The two subgroups.** $(n, 1)(n', 1) = (n\varphi_1(n'), 1) = (nn', 1)$ and $(1, h)(1, h') = (\varphi_h(1), hh') = (1, hh')$; by Step 3, $(n, 1)^{-1} = (n^{-1}, 1)$ and $(1, h)^{-1} = (1, h^{-1})$. So $N\times\{1\}$ and $\{1\}\times H$ are subgroups ([[§4 Subgroups#^def-4-1|493 Def. §4.1]]), isomorphic to $N$ and $H$ by $n \mapsto (n, 1)$, $h \mapsto (1, h)$.
>
> **5. $N$ is normal, and the quotient is $H$.** The projection $\mathrm{pr}(n, h) = h$ is a homomorphism ([[§15 Homomorphisms#^def-15-1|493 Def. §15.1]]): $\mathrm{pr}\bigl((n, h)(n', h')\bigr) = hh'$. It is onto, and its kernel is $\{(n, h) : h = 1\} = N\times\{1\}$. Kernels are normal ([[§39 Sources of Normal Subgroups#^prop-39-2|493 Prop. §39.2]]), and the first isomorphism theorem ([[§41 The First and Second Isomorphism Theorems#^thm-41-1|493 Thm. §41.1]]) gives $(N\rtimes_\varphi H)/(N\times\{1\}) \cong H$ ([[§40 Quotient Groups#^def-40-1|493 Def. §40.1]]).
>
> **6. Conjugation is $\varphi$.** By Step 4, $(1, h)^{-1} = (1, h^{-1})$. Then $(1, h)(n, 1) = (\varphi_h(n), h)$ and $(\varphi_h(n), h)(1, h^{-1}) = (\varphi_h(n)\varphi_h(1), 1) = (\varphi_h(n), 1)$.
>
> **What the proof shows.**
> - ⚑ By-product: every element factors uniquely as $(n, h) = (n, 1)(1, h)$ (check: $(n, 1)(1, h) = (n\varphi_1(1), h)$): "first $H$, then $N$", the order of [[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra#^thm-c3-4-3|Theorem §C3.4.3]], 2, $U(\Lambda, a) = U(\mathbb 1, a)U(\Lambda)$. (Moved here from the end of the proof, CB ordering pass.)
> - The group law needs exactly that $\varphi$ is a homomorphism into the *automorphisms* of $N$; with $\varphi$ trivial it is the direct product.
> - $N$ is normal but $H$ in general is not: $(n, 1)(1, h)(n, 1)^{-1} = (n\,\varphi_h(n)^{-1}, h)$, which lies in $\{1\}\times H$ only if $\varphi_h(n) = n$.
> - Used next: the Poincaré group (Def. §CB.19.3) and its double cover (Def. §CB.19.4), with $N$ the translations.

^pf-cb-19-2

*Uses:* [[§CB.19★ The Poincaré Group and Induced Representations#^def-cb-19-1|Def. §CB.19.1]], [[§1 The Definition of a Group#^def-1-1|493 Def. §1.1]], [[§4 Subgroups#^def-4-1|493 Def. §4.1]], [[§15 Homomorphisms#^def-15-1|493 Def. §15.1]], [[§39 Sources of Normal Subgroups#^prop-39-2|493 Prop. §39.2]], [[§41 The First and Second Isomorphism Theorems#^thm-41-1|493 Thm. §41.1]]

> [!definition] Definition §CB.19.3: The Poincaré Group
> The **(proper orthochronous) Poincaré group** is $\mathbb R^{1,3}\rtimes SO^+(1,3)$ ([[§CB.19★ The Poincaré Group and Induced Representations#^def-cb-19-1|Def. §CB.19.1]]), with $\varphi_\Lambda(a) = \Lambda a$: the transformations $x \mapsto \Lambda x + a$, composed as $(a, \Lambda)(a', \Lambda') = (a + \Lambda a', \Lambda\Lambda')$.
>
> *Source: P. Woit, Quantum Theory, Groups and Representations, §42.1, Definition "Poincaré group" and the group law $(a_1, \Lambda_1)(a_2, \Lambda_2) = (a_1 + \Lambda_1a_2, \Lambda_1\Lambda_2)$ (https://www.math.columbia.edu/~woit/QM/qmbook.pdf) · the user's PHY 513 notes, Ch. 7 §7.6 (Definition "Quantum Poincaré transformations": the composition law)*

^def-cb-19-3

> [!definition] Definition §CB.19.4: The Double Cover of the Poincaré Group
> $\mathbb R^{1,3}\rtimes SL(2, \mathbb C)$ with $\varphi_\lambda(a) = \pi(\lambda)a$, $\pi$ the covering of [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-9|Theorem §CB.15.9]] (equivalently $\rho$ of [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-12|Theorem §CB.15.12]]). The map $(a, \lambda) \mapsto (a, \pi(\lambda))$ is a two-to-one covering homomorphism onto the Poincaré group ([[§CB.19★ The Poincaré Group and Induced Representations#^def-cb-19-3|Def. §CB.19.3]]); the source is simply connected, the universal covering group ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^def-cb-2-18|Def. §CB.2.18]]).
>
> *Source: P. Woit, Quantum Theory, Groups and Representations, §42.1 (the double cover $\mathbb R^4\rtimes SL(2, \mathbb C)$) (https://www.math.columbia.edu/~woit/QM/qmbook.pdf) · covering and simple connectivity from [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-9|Theorem §CB.15.9]] and [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-9|Theorem §CB.9.9]] · written here*

^def-cb-19-4

> [!theorem] Theorem §CB.19.5: The Poincaré Group as a Matrix Lie Group, and Its Lie Algebra
> $(a, \Lambda) \mapsto \begin{pmatrix}\Lambda & a\\ 0 & 1\end{pmatrix} \in GL(5, \mathbb R)$ is an isomorphism of the Poincaré group onto a closed subgroup of $GL(5, \mathbb R)$. Its Lie algebra ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-11|Def. §CB.1.11]]) is $\{\begin{pmatrix}\omega & b\\ 0 & 0\end{pmatrix} : \omega \in \mathfrak{so}(1,3), b \in \mathbb R^4\}$, ten-dimensional, whose brackets in the physicists' generators are the Poincaré algebra.
>
> *Source: P. Woit, Quantum Theory, Groups and Representations, §18.1 (the Euclidean group as $(d + 1)\times(d + 1)$ matrices), §18.3 (its Lie algebra and the bracket, eq. (18.2)), §42.1 (the Poincaré group as $5\times5$ matrices, eq. (42.1), Lie algebra of dimension 10) (https://www.math.columbia.edu/~woit/QM/qmbook.pdf) · the $5\times5$ generators in the course's convention: [[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra#^der-c3-4-5|Derivation §C3.4.5]], "What the derivation shows" · closedness and the identification of the Lie algebra written here · the course's Poincaré algebra, the same relations for the Hilbert-space generators: [[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra#^thm-c3-4-5|Theorem §C3.4.5]] (moved here from the statement, CB ordering pass)*

^thm-cb-19-5

> [!proof]- Proof
> Write $\iota(a, \Lambda) = \begin{pmatrix}\Lambda & a\\ 0 & 1\end{pmatrix}$ (block sizes $4 + 1$) and $G = \iota(\text{Poincaré group})$.
>
> **1. $\iota$ is an injective homomorphism** (Woit §18.1 for $E(d)$). Block multiplication gives
>
> $$
> \begin{pmatrix}\Lambda & a\\ 0 & 1\end{pmatrix}\begin{pmatrix}\Lambda' & a'\\ 0 & 1\end{pmatrix} = \begin{pmatrix}\Lambda\Lambda' & \Lambda a' + a\\ 0 & 1\end{pmatrix} ,
> $$
>
> which is $\iota$ of the product $(a + \Lambda a', \Lambda\Lambda')$ of Def. §CB.19.3. $\iota(a, \Lambda)$ is invertible ($\det = \det\Lambda = 1$), and $(a, \Lambda)$ is read off from the matrix, so $\iota$ is injective; it is an isomorphism onto its image $G$.
>
> **2. $G$ is closed.** $G = \{M \in GL(5, \mathbb R) : \text{last row of } M = (0, 0, 0, 0, 1),\ \text{upper-left block} \in SO^+(1,3)\}$. $SO^+(1,3)$ is cut out of $M_4(\mathbb R)$ by the closed conditions $\Lambda^{\mathsf T}g\Lambda = g$, $\det\Lambda = 1$, $\Lambda^0{}_0 \ge 1$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-1|Def. §CB.1.1]]), all preserved under limits. If $M_k \in G$ converge to $M \in GL(5, \mathbb C)$, then $M$ is real, its last row is the limit of the constant row $(0, 0, 0, 0, 1)$, and its block is a limit of elements of $SO^+(1,3)$, hence in $SO^+(1,3)$. So $G$ is a closed subgroup of $GL(5, \mathbb C)$, a matrix Lie group ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-3|Def. §CB.1.3]]).
>
> **3. Powers of a block matrix.** For $X = \begin{pmatrix}\omega & b\\ 0 & 0\end{pmatrix}$, induction on $n \ge 1$: $X^1 = X$, and if $X^n = \begin{pmatrix}\omega^n & \omega^{n-1}b\\ 0 & 0\end{pmatrix}$ then $X^{n+1} = X^nX = \begin{pmatrix}\omega^{n+1} & \omega^nb\\ 0 & 0\end{pmatrix}$. Summing the exponential series term by term ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-5|Theorem §CB.1.5]], absolute convergence):
>
> $$
> e^{sX} = \begin{pmatrix} e^{s\omega} & F(s)\,b\\ 0 & 1\end{pmatrix}, \qquad F(s) = \sum_{n \ge 1}\frac{s^n\omega^{n-1}}{n!} .
> $$
>
> **4. These matrices lie in the Lie algebra.** If $\omega \in \mathfrak{so}(1,3)$ and $b \in \mathbb R^4$, then $e^{s\omega} \in SO^+(1,3)$ for every $s$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-17|Theorem §CB.1.17]]) and $F(s)b$ is real, so by Step 3 $e^{sX} = \iota(F(s)b, e^{s\omega}) \in G$ for all $s$: $X$ is in the Lie algebra ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-11|Def. §CB.1.11]]).
>
> **5. And nothing else does.** Let $e^{sX} \in G$ for all $s$, and write $X = \begin{pmatrix}\omega & b\\ c & d\end{pmatrix}$ with $c$ a row and $d$ a number. $\frac{d}{ds}e^{sX}|_{s=0} = X$ (Theorem §CB.1.5). Every $e^{sX}$ is real with last row $(0, 0, 0, 0, 1)$, independent of $s$, so $X$ is real and its last row, the derivative of a constant, is zero: $c = 0$, $d = 0$. Now Step 3 applies, and the block $e^{s\omega}$ lies in $SO^+(1,3)$ for all $s$, so $\omega \in \mathfrak{so}(1,3)$ (Theorem §CB.1.17). With Step 4, the Lie algebra is exactly the stated set; its dimension is $\dim\mathfrak{so}(1,3) + \dim\mathbb R^4 = 6 + 4 = 10$.
>
> **6. The bracket** (Woit (18.2)). $X_1X_2 = \begin{pmatrix}\omega_1\omega_2 & \omega_1b_2\\ 0 & 0\end{pmatrix}$ and $X_2X_1 = \begin{pmatrix}\omega_2\omega_1 & \omega_2b_1\\ 0 & 0\end{pmatrix}$, so
>
> $$
> \Bigl[\begin{pmatrix}\omega_1 & b_1\\ 0 & 0\end{pmatrix}, \begin{pmatrix}\omega_2 & b_2\\ 0 & 0\end{pmatrix}\Bigr] = \begin{pmatrix}[\omega_1, \omega_2] & \omega_1b_2 - \omega_2b_1\\ 0 & 0\end{pmatrix} .
> $$
>
> **7. The physicists' generators.** Put $\tilde{\mathcal J}^{\mu\nu} = \begin{pmatrix}\mathcal J^{\mu\nu} & 0\\ 0 & 0\end{pmatrix}$ with the matrices $\mathcal J^{\mu\nu}$ of [[§CB.4 The Lorentz Algebra꞉ Generators and Commutation Relations#^def-cb-4-2|Def. §CB.4.2]], and $\tilde P^\mu = \begin{pmatrix}0 & p^\mu\\ 0 & 0\end{pmatrix}$ with $(p^\mu)^\alpha = -i\,g^{\mu\alpha}$. Then $-\frac i2\omega_{\mu\nu}\tilde{\mathcal J}^{\mu\nu} + i\varepsilon_\mu\tilde P^\mu$ has block $-\frac i2\omega_{\mu\nu}\mathcal J^{\mu\nu} = \frac12\omega_{\mu\nu}M^{\mu\nu}$, whose $(\mu, \nu)$ entry is $g^{\mu\alpha}\omega_{\alpha\nu}$ (Def. §CB.4.2 and $\omega_{\nu\alpha} = -\omega_{\alpha\nu}$), the general element of $\mathfrak{so}(1,3)$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-17|Theorem §CB.1.17]]), and last column $i\varepsilon_\mu(-ig^{\mu\alpha}) = \varepsilon^\alpha$, an arbitrary vector: the ten matrices span the Lie algebra.
>
> **8. Their brackets.** By Step 6:
> - $[\tilde{\mathcal J}^{\mu\nu}, \tilde{\mathcal J}^{\rho\sigma}]$ has block $[\mathcal J^{\mu\nu}, \mathcal J^{\rho\sigma}]$ and zero column: the Lorentz algebra of [[§CB.4 The Lorentz Algebra꞉ Generators and Commutation Relations#^thm-cb-4-6|Theorem §CB.4.6]] (stated there for these $4\times4$ matrices).
> - $[\tilde{\mathcal J}^{\mu\nu}, \tilde P^\rho]$ has zero block and column $\mathcal J^{\mu\nu}p^\rho$, with entries $(\mathcal J^{\mu\nu}p^\rho)^\alpha = i(g^{\mu\alpha}\delta^\nu{}_\beta - g^{\nu\alpha}\delta^\mu{}_\beta)(-ig^{\rho\beta}) = g^{\mu\alpha}g^{\nu\rho} - g^{\nu\alpha}g^{\mu\rho}$. The column of $i(g^{\nu\rho}\tilde P^\mu - g^{\mu\rho}\tilde P^\nu)$ is $i\bigl(g^{\nu\rho}(-ig^{\mu\alpha}) - g^{\mu\rho}(-ig^{\nu\alpha})\bigr) = g^{\nu\rho}g^{\mu\alpha} - g^{\mu\rho}g^{\nu\alpha}$, the same. So $[\tilde{\mathcal J}^{\mu\nu}, \tilde P^\rho] = i(g^{\nu\rho}\tilde P^\mu - g^{\mu\rho}\tilde P^\nu)$.
> - $[\tilde P^\mu, \tilde P^\nu]$ has block $[0, 0] = 0$ and column $0\cdot p^\nu - 0\cdot p^\mu = 0$.
>
> **What the proof shows.**
> - Step 7: the ten matrices span the Lie algebra with the parametrization of [[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra#^def-c3-4-1|Def. §C3.4.1]] (moved here from Step 7, CB ordering pass).
> - Step 8: These are the relations of [[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra#^thm-c3-4-5|Theorem §C3.4.5]], with the $5\times5$ matrices in place of the Hilbert-space generators. (Moved here from Step 8, CB ordering pass.)
> - ⚑ By-product: $(i\varepsilon_\mu\tilde P^\mu)^2 = 0$, so $e^{i\varepsilon_\mu\tilde P^\mu} = \mathbb 1 + i\varepsilon_\mu\tilde P^\mu = \iota(\varepsilon, \mathbb 1)$ exactly: translation by $\varepsilon$, the matrix counterpart of the translation operator $U(\mathbb 1, a)$ as an exponential of the momentum generators ([[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra#^thm-c3-4-3|Theorem §C3.4.3]], 3). The factor $-i$ in $p^\mu$ is fixed by the course's sign $+i\varepsilon_\mu$ in front of the momentum generators ([[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra#^cau-c3-4-1|§C3.4, Caution: Signs and names across the sources]]); Woit's real basis $t_\mu$ differs by such factors. (Moved here from the end of the proof, CB ordering pass.)
> - The semidirect structure is visible in the Lie algebra: translations form an abelian ideal ($[\cdot, \tilde P] \subset \operatorname{span}\tilde P$), the Lorentz algebra a subalgebra acting on it by $\omega \cdot b = \omega b$.
> - The $5\times5$ representation is finite-dimensional and not unitary ($\tilde P^\mu$ is nilpotent), in contrast to the unitary representations on Hilbert space built below; the commutation relations are the same in both.
> - Used next: the Casimir of the momentum generators ([[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra#^thm-c3-4-6|Theorem §C3.4.6]]) and the little-group algebras.

^pf-cb-19-5

*Uses:* [[§CB.19★ The Poincaré Group and Induced Representations#^def-cb-19-3|Def. §CB.19.3]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-1|Def. §CB.1.1]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-3|Def. §CB.1.3]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-11|Def. §CB.1.11]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-5|Theorem §CB.1.5]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-17|Theorem §CB.1.17]], [[§CB.4 The Lorentz Algebra꞉ Generators and Commutation Relations#^def-cb-4-2|Def. §CB.4.2]], [[§CB.4 The Lorentz Algebra꞉ Generators and Commutation Relations#^thm-cb-4-6|Theorem §CB.4.6]]

The course's Poincaré algebra of the ten generators on the Hilbert space of states is physics: [[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra#^thm-c3-4-5|Theorem §C3.4.5]].

## Orbits, stabilizers and little groups

Orbits and stabilizers, defined in Group Theory; the orbits of $SO^+(1,3)$ on momenta, proved in [[§C1a.4 The Lorentz Group|§C1a.4]]:

![[§27 Orbits#^def-27-1]]

![[§26 Stabilizers and Fixed Points#^def-26-1]]

![[§C1a.4 The Lorentz Group#^thm-c1a-4-2]]

The orbit theorem is the physical input of this ★ section and stays embedded as a physics box (CB ordering pass, 2026-10-08); everything else below rests on CB and Math.

The course's little group of a standard momentum, with its Wigner element, is physics: [[§C3.6★ Particle States and the Little Group#^def-c3-6-2|Def. §C3.6.2]].

> [!definition] Definition §CB.19.6: Characters of the Translations and the Dual Action
> For $p \in \mathbb R^{1,3}$ the **character** $\chi_p(a) = e^{ip\cdot a}$ is a continuous homomorphism $\mathbb R^{1,3} \to U(1)$, and every continuous homomorphism $\mathbb R^{1,3} \to U(1)$ is one $\chi_p$. $H = SO^+(1,3)$ or $SL(2, \mathbb C)$ acts on characters by $(h\cdot\chi_p)(a) = \chi_p(\varphi_{h^{-1}}(a)) = \chi_{\Lambda p}(a)$, i.e. on momenta by $p \mapsto \Lambda p$ ($\Lambda = \pi(h)$ for $SL(2, \mathbb C)$).
>
> *Source: P. Woit, Quantum Theory, Groups and Representations, §20.4 (Definition "Character group"; the characters $\alpha_p(a) = e^{ip\cdot a}$ of $\mathbb R^d$ and the dual action $\alpha \mapsto \alpha\circ\Phi_k^{-1}$, with the Euclidean product) (https://www.math.columbia.edu/~woit/QM/qmbook.pdf) · the sign $+ip\cdot a$ (Minkowski product) is the course's: $U(\mathbb 1, a)|p, \sigma\rangle = e^{ip\cdot a}|p, \sigma\rangle$ ([[§C3.6★ Particle States and the Little Group#^thm-c3-6-2|Theorem §C3.6.2]], 1, from the exponential form of translations, [[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra#^thm-c3-4-3|Theorem §C3.4.3]], 3); H. Osborn, Group Theory Lecture Notes (DAMTP, 2023), eq. (4.112), $T[a]|p\rangle = e^{ia_\mu p^\mu}|p\rangle$, has the same sign (https://www.damtp.cam.ac.uk/user/ho10/GNotes.pdf) · $(h\cdot\chi_p) = \chi_{\Lambda p}$ written here*

^def-cb-19-6

> [!definition] Definition §CB.19.7: The Euclidean Group of the Plane
> $ISO(2) = E(2) = \mathbb R^2\rtimes SO(2)$ ([[§CB.19★ The Poincaré Group and Induced Representations#^def-cb-19-1|Def. §CB.19.1]]), with $SO(2)$ acting by rotation; its double cover is $\mathbb C\rtimes U(1)$ with $e^{i\theta/2}$ acting on $\mathbb C$ by multiplication with $e^{i\theta}$.
>
> *Source: P. Woit, Quantum Theory, Groups and Representations, §18.1, Definition "Euclidean group" ($E(d) = ISO(d) = \mathbb R^d\rtimes SO(d)$) (https://www.math.columbia.edu/~woit/QM/qmbook.pdf) · the double cover written here; it is the little group of Theorem §CB.19.8, as in H. Osborn, Group Theory Lecture Notes (DAMTP, 2023), §4.5.5, eq. (4.190)*

^def-cb-19-7

> [!theorem] Theorem §CB.19.8: The Little Groups in SL(2,ℂ)
> For the action of $SL(2, \mathbb C)$ on momenta (Def. §CB.19.6):
> 1. the stabilizer of $k = (m, 0, 0, 0)$, $m > 0$, is $SU(2)$, the double cover of the little group $SO(3)$;
> 2. the stabilizer of $k = (\kappa, 0, 0, \kappa)$, $\kappa > 0$, is conjugate in $SL(2, \mathbb C)$ to $\Bigl\{\begin{pmatrix} e^{i\theta/2} & z\\ 0 & e^{-i\theta/2}\end{pmatrix} : \theta \in \mathbb R, z \in \mathbb C\Bigr\}$, isomorphic to the double cover $\mathbb C\rtimes U(1)$ of $ISO(2)$ ([[§CB.19★ The Poincaré Group and Induced Representations#^def-cb-19-7|Def. §CB.19.7]]); with the covering $\pi$ of [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-4|Theorem §CB.15.4]] ($x \leftrightarrow x_\mu\sigma^\mu$) it is exactly the lower-triangular group $\Bigl\{\begin{pmatrix} e^{-i\theta/2} & 0\\ c & e^{i\theta/2}\end{pmatrix}\Bigr\}$.
>
> In both cases $\pi$ maps the stabilizer two-to-one onto the little group $G_k$, the stabilizer of $k$ in $SO^+(1,3)$ ([[§26 Stabilizers and Fixed Points#^def-26-1|493 Def. §26.1]]).
>
> *Source: [[§C3.6★ Particle States and the Little Group#^thm-c3-6-7|Theorem §C3.6.7]], [[§C3.7★ Massless Particles and Helicity#^thm-c3-7-1|Theorem §C3.7.1]] (the little groups in $SO^+(1,3)$) · H. Osborn, Group Theory Lecture Notes (DAMTP, 2023), §4.5.5, eqs. (4.183)–(4.190): the massless little group in $SL(2, \mathbb C)$, upper triangular in the convention $x \leftrightarrow x^0 + x^i\sigma^i$ (https://www.damtp.cam.ac.uk/user/ho10/GNotes.pdf) · P. Woit, Quantum Theory, Groups and Representations, §42.3.1, §42.3.5 ($SO(3)$, $E(2)$, half-integer helicity from the double cover) (https://www.math.columbia.edu/~woit/QM/qmbook.pdf) · the stabilizer computation written here · the course's little group: [[§C3.6★ Particle States and the Little Group#^def-c3-6-2|Def. §C3.6.2]] (moved here from the statement, CB ordering pass)*

^thm-cb-19-8

> [!proof]- Proof
> **0. The stabilizer as a matrix equation.** $\lambda \in SL(2, \mathbb C)$ acts on momenta by $p \mapsto \pi(\lambda)p$ (Def. §CB.19.6, Def. §CB.19.4), and $\pi$ is defined by $\lambda\,(x_\mu\sigma^\mu)\,\lambda^\dagger = (\pi(\lambda)x)_\mu\sigma^\mu$ ([[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-4|Theorem §CB.15.4]]). Since $x \mapsto x_\mu\sigma^\mu$ is a bijection onto the Hermitian matrices ([[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-3|Theorem §CB.15.3]]), with $K \equiv k_\mu\sigma^\mu$,
>
> $$
> \pi(\lambda)k = k \iff \lambda K\lambda^\dagger = K .
> $$
>
> The stabilizer $S_k = \{\lambda : \lambda K\lambda^\dagger = K\}$ is $\pi^{-1}(G_k)$, with $G_k \subset SO^+(1,3)$ the little group, the stabilizer of $k$ in $SO^+(1,3)$ ([[§26 Stabilizers and Fixed Points#^def-26-1|493 Def. §26.1]]).
>
> **1. Massive: the matrix.** $k = (m, 0, 0, 0)$ has $k_0 = m$, $k_i = 0$, so $K = m\sigma^0 = m\mathbb 1$.
>
> **2. Massive: the stabilizer.** $\lambda(m\mathbb 1)\lambda^\dagger = m\mathbb 1$ iff $\lambda\lambda^\dagger = \mathbb 1$ ($m > 0$), i.e. $\lambda \in U(2)$; with $\det\lambda = 1$ this is $SU(2)$. Conversely every $U \in SU(2)$ satisfies $UKU^\dagger = mUU^\dagger = K$. So $S_k = SU(2)$.
>
> **3. Massive: two-to-one onto $SO(3)$.** By [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-9|Theorem §CB.15.9]], 3, $\pi(U) = \operatorname{diag}(1, R(U))$ for $U \in SU(2)$, and $G_k = \{\operatorname{diag}(1, R) : R \in SO(3)\}$ ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-13|Theorem §CB.2.13]], Step 4: an element of $SO^+(1,3)$ fixing $e_0$ is $\operatorname{diag}(1, O)$ with $O \in SO(3)$, and each such matrix fixes $k = me_0$). $\pi|_{S_k}$ is onto $G_k$: for $W \in G_k$ choose $\lambda$ with $\pi(\lambda) = W$ (Theorem §CB.15.9, 1); then $\pi(\lambda)k = k$, so $\lambda \in S_k$. Its kernel is $\ker\pi = \{\pm\mathbb 1\}$ ([[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-5|Theorem §CB.15.5]]), which lies in $SU(2)$. So $SU(2) \to SO(3)$ is two-to-one: part 1.
>
> **4. Massless: the matrix.** $k = (\kappa, 0, 0, \kappa)$ has $k_0 = \kappa$, $k_3 = -\kappa$, so $K = \kappa\sigma^0 - \kappa\sigma^3 = \operatorname{diag}(0, 2\kappa)$, the matrix of Theorem §CB.15.3 with $x^0 - x^3 = 0$, $x^0 + x^3 = 2\kappa$. With $e_2 = (0, 1)^{\mathsf T}$, $K = 2\kappa\,e_2e_2^\dagger$, a Hermitian matrix of rank one.
>
> **5. Massless: the condition on the second column.** $\lambda K\lambda^\dagger = 2\kappa\,(\lambda e_2)(\lambda e_2)^\dagger$, so with $v = \lambda e_2$ (the second column of $\lambda$, nonzero as $\lambda$ is invertible) the condition is $vv^\dagger = e_2e_2^\dagger$. Apply both sides to $e_1 = (1, 0)^{\mathsf T}$: $v\,(v^\dagger e_1) = \bar v_1\,v$ on the left, $0$ on the right; as $v \neq 0$, $\bar v_1 = 0$. Then the $(2, 2)$ entry gives $|v_2|^2 = 1$, $v_2 = e^{i\varphi}$. Conversely $v = e^{i\varphi}e_2$ gives $vv^\dagger = e_2e_2^\dagger$.
>
> **6. Massless: the stabilizer.** So $\lambda = \begin{pmatrix}\alpha & 0\\ c & e^{i\varphi}\end{pmatrix}$, and $\det\lambda = \alpha e^{i\varphi} = 1$ forces $\alpha = e^{-i\varphi}$. Writing $\varphi = \theta/2$:
>
> $$
> S_k = \Bigl\{\begin{pmatrix} e^{-i\theta/2} & 0\\ c & e^{i\theta/2}\end{pmatrix} : \theta \in \mathbb R,\ c \in \mathbb C\Bigr\} .
> $$
>
> **7. Massless: conjugation to the upper-triangular form.** Let $\varepsilon = \begin{pmatrix}0 & 1\\ -1 & 0\end{pmatrix} \in SL(2, \mathbb C)$, $\varepsilon^{-1} = \begin{pmatrix}0 & -1\\ 1 & 0\end{pmatrix}$. For $M = \begin{pmatrix} e^{-i\theta/2} & 0\\ c & e^{i\theta/2}\end{pmatrix}$,
>
> $$
> M\varepsilon = \begin{pmatrix} 0 & e^{-i\theta/2}\\ -e^{i\theta/2} & c\end{pmatrix}, \qquad \varepsilon^{-1}M\varepsilon = \begin{pmatrix} e^{i\theta/2} & -c\\ 0 & e^{-i\theta/2}\end{pmatrix} .
> $$
>
> With $z = -c$ this runs over the group $B$ of the statement as $(\theta, c)$ runs over $\mathbb R\times\mathbb C$; so $S_k = \varepsilon B\varepsilon^{-1}$.
>
> **8. Massless: the group law of $B$.** Parametrize $B$ by $w = e^{i\theta/2} \in U(1)$ and $\zeta \in \mathbb C$: $u(w, \zeta) = \begin{pmatrix} w & \zeta\bar w\\ 0 & \bar w\end{pmatrix}$ (so $z = \zeta\bar w$; $w$ and $\zeta = zw$ are read off from the matrix, so the parametrization is bijective). Multiply, using $\bar w_1w_1 = 1$ to write $w_1\zeta_2\bar w_2 = (w_1^2\zeta_2)\,\bar w_1\bar w_2$:
>
> $$
> u(w_1, \zeta_1)\,u(w_2, \zeta_2) = \begin{pmatrix} w_1w_2 & w_1\zeta_2\bar w_2 + \zeta_1\bar w_1\bar w_2\\ 0 & \bar w_1\bar w_2\end{pmatrix} = u\bigl(w_1w_2,\ \zeta_1 + w_1^2\zeta_2\bigr) .
> $$
>
> This is the product $(\zeta_1, w_1)(\zeta_2, w_2) = (\zeta_1 + \varphi_{w_1}(\zeta_2), w_1w_2)$ of [[§CB.19★ The Poincaré Group and Induced Representations#^def-cb-19-1|Def. §CB.19.1]] with $\varphi_w(\zeta) = w^2\zeta$, i.e. of $\mathbb C\rtimes U(1)$ (Def. §CB.19.7: $e^{i\theta/2}$ acts by $e^{i\theta}$). So $(\zeta, w) \mapsto u(w, \zeta)$ is an isomorphism $\mathbb C\rtimes U(1) \to B$, and $S_k \cong B \cong \mathbb C\rtimes U(1)$.
>
> **9. Massless: the double cover of $ISO(2)$.** $(\zeta, w) \mapsto (\zeta, r_{\arg w^2})$, with $\zeta \in \mathbb C = \mathbb R^2$ and $r_\alpha$ the rotation by $\alpha$, is a homomorphism onto $ISO(2) = \mathbb R^2\rtimes SO(2)$, because the rotation $r_{\arg w^2}$ of $\mathbb R^2$ is multiplication by $w^2$ on $\mathbb C$, so products go to $(\zeta_1 + r_{\arg w_1^2}\zeta_2, r_{\arg w_1^2}r_{\arg w_2^2})$. Its kernel is $\{(0, w) : w^2 = 1\} = \{(0, \pm1)\}$: two-to-one. Independently, Step 3's argument (onto by Theorem §CB.15.9, 1; kernel $\{\pm\mathbb 1\} \subset S_k$) shows that $\pi$ maps $S_k$ two-to-one onto $G_k$. Both maps have kernel $\{\pm\mathbb 1\}$, which corresponds to $\{(0, \pm1)\}$ under $S_k \cong \mathbb C\rtimes U(1)$ (Steps 7–8: $-\mathbb 1 = u(-1, 0)$ commutes with $\varepsilon$), so the first isomorphism theorem ([[§41 The First and Second Isomorphism Theorems#^thm-41-1|493 Thm. §41.1]]) gives $G_k \cong S_k/\{\pm\mathbb 1\} \cong ISO(2)$: part 2.
>
> ⚑ By-product: the rotation $R_z(\theta) \in G_k$ lifts to $e^{-i\theta\sigma^3/2} = \operatorname{diag}(e^{-i\theta/2}, e^{i\theta/2}) \in S_k$ ([[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-9|Theorem §CB.15.9]], 2), the element with $c = 0$ in Step 6; at $\theta = 2\pi$ it is $-\mathbb 1$. A one-dimensional representation of $S_k$ trivial on the $c$-part sends it to $e^{-i\lambda\theta}$, and $\lambda \in \frac12\mathbb Z$ is exactly the condition for this to be well defined on the circle $\theta \in [0, 4\pi)$ → [[§C3.7★ Massless Particles and Helicity#^thm-c3-7-6|Theorem §C3.7.6]].
>
> **What the proof shows.**
> - The course's massive little group, $G_k = \{\operatorname{diag}(1, R) : R \in SO(3)\}$: [[§C3.6★ Particle States and the Little Group#^thm-c3-6-7|Theorem §C3.6.7]] (moved here from Step 3, CB ordering pass).
> - The course's massless little group, $G_k \cong ISO(2)$: [[§C3.7★ Massless Particles and Helicity#^thm-c3-7-1|Theorem §C3.7.1]] (moved here from Step 9, CB ordering pass).
> - Both little groups come from one matrix equation $\lambda K\lambda^\dagger = K$: for $K$ of full rank ($m > 0$) it is unitarity, for $K$ of rank one ($m = 0$) only the image line of $K$ is fixed, which leaves the nilpotent part $c$ free.
> - Upper or lower triangular is a convention: with the dictionary $x \leftrightarrow x^0 + x^i\sigma^i$ (Osborn, Theorem §CB.15.12) one has $K = \operatorname{diag}(2\kappa, 0)$ and the stabilizer is $B$ itself; with the course's $x_\mu\sigma^\mu$ it is $\varepsilon B\varepsilon^{-1}$.
> - Used in: the particle classification of [[§C3.6★ Particle States and the Little Group#^thm-c3-6-6|Theorem §C3.6.6]] at the level of the covering group, and half-integer helicity.

^pf-cb-19-8

*Uses:* [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-3|Theorem §CB.15.3]], [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-4|Theorem §CB.15.4]], [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-5|Theorem §CB.15.5]], [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-9|Theorem §CB.15.9]], [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-13|Theorem §CB.2.13]], [[§26 Stabilizers and Fixed Points#^def-26-1|493 Def. §26.1]], [[§41 The First and Second Isomorphism Theorems#^thm-41-1|493 Thm. §41.1]], [[§CB.19★ The Poincaré Group and Induced Representations#^def-cb-19-1|Def. §CB.19.1]], [[§CB.19★ The Poincaré Group and Induced Representations#^def-cb-19-7|Def. §CB.19.7]]

## Induced representations

> [!definition] Definition §CB.19.9: Induced Representation of ℝⁿ ⋊ H
> Let $G = \mathbb R^n\rtimes H$ with $H$ a matrix Lie group acting linearly on $\mathbb R^n$ and on momenta as in Def. §CB.19.6; let $\mathcal O$ be an $H$-orbit of momenta with an $H$-invariant measure $\mu$, $k \in \mathcal O$, $H_k$ the stabilizer of $k$, $\sigma$ a unitary representation of $H_k$ on a Hilbert space $\mathcal K$, and $p \mapsto L(p) \in H$ a measurable choice with $L(p)k = p$. The **induced representation** acts on $L^2(\mathcal O, \mu; \mathcal K)$ by
>
> $$
> \bigl(U(a, h)\psi\bigr)(p) = e^{ip\cdot a}\,\sigma\bigl(W(h, p)\bigr)\,\psi(h^{-1}p), \qquad W(h, p) = L(p)^{-1}\,h\,L(h^{-1}p) \in H_k .
> $$
>
> *Source: L. M. Borasi, Review and concrete description of the irreducible unitary representations of the universal cover of the complexified Poincaré group, arXiv:2108.10726, Cor. 3.11, eq. (17) (Wigner–Mackey embedding $\beta = L$; the Radon–Nikodym factor is $1$ for an invariant $\mu$; the phase is the translation part of $\chi_k\otimes\sigma$) (https://arxiv.org/abs/2108.10726) · P. Woit, Quantum Theory, Groups and Representations, §20.4 (orbit and little group, the construction described) · the course's form: [[§C3.6★ Particle States and the Little Group#^thm-c3-6-4|Theorem §C3.6.4]]; sign $e^{+ip\cdot a}$ and relativistic normalization checked against it in [[§CB.19★ The Poincaré Group and Induced Representations#^rem-cb-19-1|§CB.19, Remark: The course's law as an induced representation]], where the course's Wigner element is $W(\Lambda, \Lambda p)$ in this notation*

^def-cb-19-9

> [!theorem] Theorem §CB.19.10: The Induced Representation Is Unitary
> $U$ of [[§CB.19★ The Poincaré Group and Induced Representations#^def-cb-19-9|Def. §CB.19.9]] is a unitary representation of $G$; $W(h, p)$ lies in $H_k$ and satisfies $W(hh', p) = W(h, p)W(h', h^{-1}p)$. If $L$ is continuous outside a closed $\mu$-null set, $U$ is strongly continuous. A different choice of $L$, or of $k' = h_0k \in \mathcal O$ with $\sigma$ carried to $H_{k'} = h_0H_kh_0^{-1}$ as $\sigma'(x) = \sigma(h_0^{-1}xh_0)$, gives an equivalent representation.
>
> *Source: the computation follows the course's [[§C3.6★ Particle States and the Little Group#^thm-c3-6-3|Theorem §C3.6.3]] and [[§C3.6★ Particle States and the Little Group#^thm-c3-6-4|Theorem §C3.6.4]], transcribed to functions on the orbit · L. M. Borasi, Review and concrete description of the irreducible unitary representations of the universal cover of the complexified Poincaré group, arXiv:2108.10726, Prop. 3.8, Cor. 3.11 and Remark 3.9 (this realization; its continuity for a merely measurable section) (https://arxiv.org/abs/2108.10726) · the steps written out here*

^thm-cb-19-10

> [!proof]- Proof
> **0. Conventions.** The group law of $G$ is $(a, h)(a', h') = (a + ha', hh')$ (Def. §CB.19.1 with $\varphi_h(a) = ha$, written additively). $h$ acts on momenta by $\chi_{hp} = h\cdot\chi_p$ (Def. §CB.19.6), i.e. $e^{i(hp)\cdot a} = e^{ip\cdot(h^{-1}a)}$ for all $a$, so
>
> $$
> (hp)\cdot a = p\cdot(h^{-1}a), \qquad\text{equivalently}\qquad (hp)\cdot(hb) = p\cdot b ;
> $$
>
> for the Lorentz group, $hp = \Lambda p$ with $\Lambda = h$ or $\pi(h)$. Invariance of $\mu$ means $\mu(hE) = \mu(E)$, i.e. $\int_{\mathcal O}f(h^{-1}p)\,d\mu(p) = \int_{\mathcal O}f(q)\,d\mu(q)$ for measurable $f \ge 0$.
>
> **1. $W(h, p) \in H_k$.** Apply the three factors to $k$: $L(h^{-1}p)k = h^{-1}p$, then $h(h^{-1}p) = p$, then $L(p)^{-1}p = k$ because $L(p)k = p$. So $W(h, p)k = k$.
>
> **2. The cocycle identity.** Insert $\mathbb 1 = L(h^{-1}p)L(h^{-1}p)^{-1}$ between $h$ and $h'$:
>
> $$
> W(hh', p) = L(p)^{-1}h\,L(h^{-1}p)\,L(h^{-1}p)^{-1}h'\,L(h'^{-1}h^{-1}p) = W(h, p)\,W(h', h^{-1}p) ,
> $$
>
> since $(hh')^{-1}p = h'^{-1}(h^{-1}p)$. Also $W(\mathbb 1, p) = L(p)^{-1}L(p) = \mathbb 1$.
>
> **3. Each $U(a, h)$ is a well-defined isometry.** $|e^{ip\cdot a}| = 1$ and $\sigma(W(h, p))$ is unitary on $\mathcal K$, so pointwise $\|(U(a, h)\psi)(p)\|_{\mathcal K} = \|\psi(h^{-1}p)\|_{\mathcal K}$; integrating and substituting $q = h^{-1}p$ (invariance of $\mu$, Step 0),
>
> $$
> \|U(a, h)\psi\|^2 = \int_{\mathcal O}\|\psi(h^{-1}p)\|_{\mathcal K}^2\,d\mu(p) = \int_{\mathcal O}\|\psi(q)\|_{\mathcal K}^2\,d\mu(q) = \|\psi\|^2 .
> $$
>
> If $\psi = \psi'$ outside a null set $E$, then $U(a, h)\psi = U(a, h)\psi'$ outside $hE$, again null; so $U(a, h)$ acts on classes in $L^2$. ($p \mapsto \sigma(W(h, p))\psi(h^{-1}p)$ is measurable because $L$ is measurable and $\sigma$, the group operations and the action are continuous.)
>
> **4. The homomorphism property.** Let $\phi = U(a', h')\psi$, so $\phi(q) = e^{iq\cdot a'}\sigma(W(h', q))\psi(h'^{-1}q)$. At $q = h^{-1}p$:
>
> $$
> \bigl(U(a, h)\phi\bigr)(p) = e^{ip\cdot a}\,e^{i(h^{-1}p)\cdot a'}\;\sigma\bigl(W(h, p)\bigr)\,\sigma\bigl(W(h', h^{-1}p)\bigr)\;\psi\bigl(h'^{-1}h^{-1}p\bigr) .
> $$
>
> - phase: $(h^{-1}p)\cdot a' = p\cdot(ha')$ (Step 0 with $h^{-1}$), so the phases combine to $e^{ip\cdot(a + ha')}$;
> - operators: $\sigma$ is a representation, so $\sigma(W(h, p))\sigma(W(h', h^{-1}p)) = \sigma(W(hh', p))$ by Step 2;
> - argument: $h'^{-1}h^{-1}p = (hh')^{-1}p$.
>
> The result is $\bigl(U(a + ha', hh')\psi\bigr)(p)$, so $U(a, h)U(a', h') = U\bigl((a, h)(a', h')\bigr)$.
>
> **5. Unitarity.** $U(0, \mathbb 1)\psi = \psi$, as $e^{ip\cdot0} = 1$ and $\sigma(W(\mathbb 1, p)) = \sigma(\mathbb 1) = \mathbb 1$ (Step 2). By Step 4, $U(g)U(g^{-1}) = U(g^{-1})U(g) = U(0, \mathbb 1) = \mathbb 1$, so each $U(g)$ is invertible; an invertible isometry (Step 3) is unitary.
>
> **6. Strong continuity, when $L$ is continuous off a null set $Z$.** Let $(a_n, h_n) \to (0, \mathbb 1)$ and first take $\psi$ continuous with compact support $S$. For $h_n$ in a compact neighbourhood $N$ of $\mathbb 1$, $(U(a_n, h_n)\psi)(p) \ne 0$ only if $h_n^{-1}p \in S$, i.e. $p \in NS$, a compact set (image of $N\times S$), of finite measure ($\mu$ finite on compact sets, as $d^3p/2E_{\mathbf p}$ is). For $p \notin Z$: $h_n^{-1}p \to p$, so $W(h_n, p) = L(p)^{-1}h_nL(h_n^{-1}p) \to L(p)^{-1}L(p) = \mathbb 1$ ($L$ is continuous on the open set $\mathcal O\setminus Z$, $Z$ closed, which contains $h_n^{-1}p$ for large $n$; for the course's choices $Z$ is empty or a half-line of the cone); then
>
> $$
> (U(a_n, h_n)\psi)(p) - \psi(p) = e^{ip\cdot a_n}\sigma(W_n)\bigl[\psi(h_n^{-1}p) - \psi(p)\bigr] + \bigl[e^{ip\cdot a_n}\sigma(W_n) - \mathbb 1\bigr]\psi(p) \to 0
> $$
>
> (the first bracket by continuity of $\psi$, the second by strong continuity of $\sigma$). The integrand $\|(U(a_n, h_n)\psi)(p) - \psi(p)\|^2 \le 4\sup\|\psi\|^2$ on $NS \cup S$, zero elsewhere, so dominated convergence gives $U(a_n, h_n)\psi \to \psi$. For general $\psi$ pick such $\phi$ with $\|\psi - \phi\| < \epsilon$ (continuous compactly supported functions are dense in $L^2(\mathcal O, \mu; \mathcal K)$); by Step 3, $\|U\psi - \psi\| \le \|U(\psi - \phi)\| + \|U\phi - \phi\| + \|\phi - \psi\| \le 2\epsilon + \|U\phi - \phi\|$.
>
> **7. Another $L$ gives an equivalent representation.** Let $L'(p)k = p$ too, and $w(p) = L(p)^{-1}L'(p)$. Then $w(p)k = L(p)^{-1}p = k$, so $w(p) \in H_k$, $L' = Lw$, and
>
> $$
> W'(h, p) = w(p)^{-1}L(p)^{-1}h\,L(h^{-1}p)\,w(h^{-1}p) = w(p)^{-1}\,W(h, p)\,w(h^{-1}p) .
> $$
>
> Define $(T\psi)(p) = \sigma(w(p))^{-1}\psi(p)$: unitary, with inverse $\psi \mapsto \sigma(w(\cdot))\psi$, pointwise unitary. Then
>
> $$
> \bigl(U'(a, h)T\psi\bigr)(p) = e^{ip\cdot a}\,\sigma(w(p))^{-1}\sigma(W(h, p))\,\sigma(w(h^{-1}p))\,\sigma(w(h^{-1}p))^{-1}\psi(h^{-1}p) = \bigl(TU(a, h)\psi\bigr)(p) ,
> $$
>
> so $U' = TUT^{-1}$.
>
> **8. Another standard momentum.** Let $k' = h_0k$. $x \in H$ fixes $k'$ iff $h_0^{-1}xh_0$ fixes $k$, so $H_{k'} = h_0H_kh_0^{-1}$, and $\sigma'(x) = \sigma(h_0^{-1}xh_0)$ is a unitary representation of it. $L'(p) = L(p)h_0^{-1}$ satisfies $L'(p)k' = L(p)k = p$, and $W'(h, p) = h_0L(p)^{-1}hL(h^{-1}p)h_0^{-1} = h_0W(h, p)h_0^{-1}$, so $\sigma'(W'(h, p)) = \sigma(W(h, p))$: the operators $U'(a, h)$ and $U(a, h)$ coincide on $L^2(\mathcal O, \mu; \mathcal K)$. With Step 7 any other $L'$ for $k'$ gives an equivalent representation.
>
> **What the proof shows.**
> - For the massive orbit, $\mu$ is $d^3p/(2\pi)^32E_{\mathbf p}$ ([[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-3|Theorem §C2a.4.3]]). (Moved here from Step 0, CB ordering pass.)
> - Step 1: (Same loop as Step 1 of [[§C3.6★ Particle States and the Little Group#^der-c3-6-3|Derivation §C3.6.3]].) (Moved here, CB ordering pass.)
> - ⚑ By-product: on the forward null cone no choice of $L$ is continuous everywhere ([[§C3.7★ Massless Particles and Helicity#^def-c3-7-1|Def. §C3.7.1]]: "no choice is continuous on the whole sphere"), which is why the continuity hypothesis is "off a null set". For a merely measurable $L$, continuity follows from Step 7 (equivalence with a continuous choice) when one exists, and in general from Mackey's realization (Borasi, Remark 3.9). (Moved here from Step 6, CB ordering pass.)
> - The comparison with the course's law (formerly Step 9) is the remark after this proof.
> - Unitarity uses exactly three things: $|e^{ip\cdot a}| = 1$, unitarity of $\sigma$, and invariance of $\mu$ (otherwise a factor $\sqrt{d\mu(h^{-1}p)/d\mu(p)}$ is needed, Borasi eq. (17)); the group law uses only the cocycle identity.
> - The choices ($L$, $k$) change the representation only by a pointwise unitary relabelling of $\mathcal K$ at each momentum, the statement of [[§C3.6★ Particle States and the Little Group#^rem-c3-6-1|§C3.6, Remark: What the definition fixes, and what it leaves free]].
> - Assumption used for continuity: $L$ continuous off a closed null set; true for the standard boosts of the massive orbit and for the massless choice of Def. §C3.7.1.
> - Used next: irreducibility (Theorem §CB.19.11) and the classification (Theorem §CB.19.12).

^pf-cb-19-10

*Uses:* [[§CB.19★ The Poincaré Group and Induced Representations#^def-cb-19-1|Def. §CB.19.1]], [[§CB.19★ The Poincaré Group and Induced Representations#^def-cb-19-6|Def. §CB.19.6]], [[§CB.19★ The Poincaré Group and Induced Representations#^def-cb-19-9|Def. §CB.19.9]]

> [!remark]- ★ Remark: The course's law as an induced representation
> *Moved here from the statement and Step 9 of the proof of Theorem §CB.19.10 (CB ordering pass, 2026-10-08): it compares with physics and is not used in the proof.* For $\mathbb R^{1,3}\rtimes SO^+(1,3)$ (or $SL(2, \mathbb C)$), $L = V$ and $\sigma = D$, the induced representation $U$ of Theorem §CB.19.10 is the law of [[§C3.6★ Particle States and the Little Group#^thm-c3-6-4|Theorem §C3.6.4]] written for the coefficients of wave packets.
>
> **9. The course's law.** Take a particle of [[§C3.6★ Particle States and the Little Group#^pr-c3-6-1|Principle §C3.6.1]] with $L = V$ ([[§C3.6★ Particle States and the Little Group#^def-c3-6-1|Def. §C3.6.1]]), $\sigma = D$, and a wave packet $|\psi\rangle = \int d\mu(p)\sum_\sigma\psi_\sigma(p)|p, \sigma\rangle$; by the normalization of [[§C3.6★ Particle States and the Little Group#^thm-c3-6-5|Theorem §C3.6.5]], $\langle\psi|\phi\rangle = \int d\mu\sum_\sigma\overline{\psi_\sigma}\phi_\sigma$, so $|\psi\rangle \mapsto (\psi_\sigma)$ is unitary onto $L^2(\mathcal O, \mu; \mathbb C^N)$. By Theorem §C3.6.4, 2,
>
> $$
> U(\Lambda, a)|\psi\rangle = \int d\mu(p)\sum_{\sigma, \sigma'}\psi_\sigma(p)\,e^{i(\Lambda p)\cdot a}\,D_{\sigma'\sigma}\bigl(W_{\rm C3}(\Lambda, p)\bigr)\,|\Lambda p, \sigma'\rangle ,
> $$
>
> with $W_{\rm C3}(\Lambda, p) = V(\Lambda p)^{-1}\Lambda V(p)$ ([[§C3.6★ Particle States and the Little Group#^def-c3-6-2|Def. §C3.6.2]]). Substitute $q = \Lambda p$, $d\mu(p) = d\mu(q)$ (Theorem §C2a.4.3): the coefficient of $|q, \sigma'\rangle$ is
>
> $$
> e^{iq\cdot a}\sum_\sigma D_{\sigma'\sigma}\bigl(W_{\rm C3}(\Lambda, \Lambda^{-1}q)\bigr)\,\psi_\sigma(\Lambda^{-1}q), \qquad W_{\rm C3}(\Lambda, \Lambda^{-1}q) = V(q)^{-1}\Lambda V(\Lambda^{-1}q) = W(\Lambda, q) ,
> $$
>
> which is Def. §CB.19.9 with $(a, h) = (a, \Lambda)$: both mean $x \mapsto \Lambda x + a$ (Def. §CB.19.3, [[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra#^pr-c3-4-1|Principle §C3.4.1]]), and the phase $e^{+iq\cdot a}$ is the course's sign.
>
> ⚑ By-product: the two Wigner elements differ in their second argument, $W_{\rm C3}(\Lambda, p) = W(\Lambda, \Lambda p)$: the course labels it by the momentum *before* the transformation (acting on states), this section by the momentum *after* (acting on functions).

^rem-cb-19-1

> [!theorem] Theorem §CB.19.11: Irreducibility (Mackey)
> The induced representation of [[§CB.19★ The Poincaré Group and Induced Representations#^def-cb-19-9|Def. §CB.19.9]] is irreducible if and only if $\sigma$ is irreducible; induced representations from different orbits, or from inequivalent $\sigma$, are inequivalent.
>
> *Source: Mackey's theorem for regular semidirect products with abelian normal subgroup, stated in L. M. Borasi, Review and concrete description of the irreducible unitary representations of the universal cover of the complexified Poincaré group, arXiv:2108.10726, Theorem 3.5 (https://arxiv.org/abs/2108.10726), which cites E. Kaniuth and K. F. Taylor, Induced Representations of Locally Compact Groups (Cambridge, 2013), Theorem 4.28, p. 168, for the proof · P. Woit, Quantum Theory, Groups and Representations, §20.4 (stated: "We did not show this, but this construction gives an irreducible representation …") (https://www.math.columbia.edu/~woit/QM/qmbook.pdf)*

^thm-cb-19-11

> [!proof]- Proof (to be filled)
> *To be filled. The half "$\sigma$ reducible ⇒ $U$ reducible" is the argument of Step 6 of [[§C3.6★ Particle States and the Little Group#^der-c3-6-4|Derivation §C3.6.4]]: a closed $\sigma(H_k)$-invariant subspace $\mathcal K_0 \subset \mathcal K$ gives the closed $U$-invariant subspace $L^2(\mathcal O, \mu; \mathcal K_0)$, since $\sigma(W(h, p))$ maps $\mathcal K_0$ to itself. The converse and the inequivalence need the commutant of the multiplication operators $e^{ip\cdot a}$ (decomposable operators) and an ergodicity argument on $\mathcal O$, or Mackey's imprimitivity theorem; proof in E. Kaniuth and K. F. Taylor, Induced Representations of Locally Compact Groups (Cambridge, 2013), Theorem 4.28.*
> <!-- searched: Woit qmbook §20.4, Ch. 42 (stated, not proved); Bekaert–Boulanger hep-th/0611263 §3.1 (Weinberg-style, no proof of irreducibility); Borasi arXiv:2108.10726 §3 (statement, cites Kaniuth–Taylor Thm 4.28); Rosenberg, C*-algebras and Mackey's theory of group representations (survey, no proof); Osborn DAMTP Group Theory notes §4.5 (construction only); the user's PHY 513 notes Ch. 7 §7.7 and Yu §3.3 (converse stated, not proved) — no freely available text with a complete proof found -->

^pf-cb-19-11

> [!theorem] Theorem §CB.19.12: Every Irreducible Unitary Representation Is Induced (Wigner–Mackey)
> If the $H$-orbits on momenta are locally closed (true for the Lorentz group acting on $\mathbb R^{1,3}$), every irreducible unitary representation of $\mathbb R^n\rtimes H$ is equivalent to an induced representation (Def. §CB.19.9) from exactly one orbit $\mathcal O$ and one irreducible $\sigma$, up to equivalence. For $\mathbb R^{1,3}\rtimes SL(2, \mathbb C)$ this is Wigner's classification of particles by mass and spin or helicity.
>
> *Source: L. M. Borasi, Review and concrete description of the irreducible unitary representations of the universal cover of the complexified Poincaré group, arXiv:2108.10726, Theorem 3.5 with Definitions 3.2, 3.4 and Proposition 3.3 (a sufficient condition for "Mackey compatibility": the orbit space almost Hausdorff, $G/N$ σ-compact) (https://arxiv.org/abs/2108.10726), citing E. Kaniuth and K. F. Taylor, Induced Representations of Locally Compact Groups (Cambridge, 2013), Theorem 4.28, p. 168, Proposition 4.6, p. 155, Remark 4.26, p. 159 · P. Woit, Quantum Theory, Groups and Representations, §20.4, §42.2–§42.3 (the classification by orbits and little groups, stated) (https://www.math.columbia.edu/~woit/QM/qmbook.pdf) · the course: [[§C3.6★ Particle States and the Little Group#^pr-c3-6-1|Principle §C3.6.1]], [[§C3.6★ Particle States and the Little Group#^thm-c3-6-2|Theorem §C3.6.2]]*

^thm-cb-19-12

> [!proof]- Proof (to be filled)
> *Stated only (beyond the course). The first step is [[§C3.6★ Particle States and the Little Group#^thm-c3-6-2|Theorem §C3.6.2]]: the joint spectral measure of the translations of an irreducible representation is carried by the orbits of one invariant set. The remaining steps — that measure is quasi-invariant and ergodic, hence concentrated on one orbit when the orbit space is regular, and the representation is induced from the stabilizer by Mackey's imprimitivity theorem — are proved in E. Kaniuth and K. F. Taylor, Induced Representations of Locally Compact Groups (Cambridge, 2013), Theorem 4.28 (with Proposition 4.6 for the orbit condition), as cited in Borasi, Theorem 3.5.*
> <!-- searched: Woit qmbook §20.4, Ch. 42 (stated); Bekaert–Boulanger hep-th/0611263 (Weinberg's argument, no completeness proof); Borasi arXiv:2108.10726 (statement with precise reference); Rosenberg, C*-algebras and Mackey's theory (survey); Osborn DAMTP notes §4.5; the user's PHY 513 notes Ch. 7 §7.7, Yu §3.3 — no freely available text with a complete proof found -->

^pf-cb-19-12

The course's induced representation on one-particle states and its massless little group are physics: [[§C3.6★ Particle States and the Little Group#^thm-c3-6-4|Theorem §C3.6.4]], [[§C3.7★ Massless Particles and Helicity#^thm-c3-7-1|Theorem §C3.7.1]].

> [!remark]- Connections
> - The semidirect structure is why momentum labels states first and spin second: translations form an abelian normal subgroup, so they can be diagonalized first ([[§CB.6 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-6-6|Theorem §CB.6.6]] in its infinite-dimensional form), and the Lorentz group only permutes their eigenvalues.
> - The double cover of $ISO(2)$ in Theorem §CB.19.8 is why helicities of massless particles may be half-integers ([[§C3.7★ Massless Particles and Helicity#^thm-c3-7-6|Theorem §C3.7.6]]).
> - **Used in**: Definitions §CB.19.1–§CB.19.4 — [[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra#^pr-c3-4-1|Principle §C3.4.1]], [[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra#^thm-c3-4-5|Theorem §C3.4.5]]; Theorem §CB.19.8 — [[§C3.6★ Particle States and the Little Group#^thm-c3-6-6|Theorem §C3.6.6]], [[§C3.6★ Particle States and the Little Group#^thm-c3-6-7|Theorem §C3.6.7]], [[§C3.7★ Massless Particles and Helicity#^thm-c3-7-1|Theorem §C3.7.1]], [[§C4.3★ Massive Polarization Vectors and Plane Waves|§C4.3★]]; Definition §CB.19.9–Theorem §CB.19.12 — [[§C3.6★ Particle States and the Little Group#^thm-c3-6-4|Theorem §C3.6.4]], [[§C3.6★ Particle States and the Little Group#^thm-c3-6-5|Theorem §C3.6.5]], [[§C3.6★ Particle States and the Little Group#^pr-c3-6-1|Principle §C3.6.1]], [[§C3.7★ Massless Particles and Helicity#^thm-c3-7-6|Theorem §C3.7.6]]; Theorem §CB.19.5 — [[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra|§C3.4]] (embedded); Definition §CB.19.3 — [[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra|§C3.4]] (embedded); Definition §CB.19.4 — [[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra|§C3.4]] (embedded); Theorem §CB.19.8 — [[§C3.6★ Particle States and the Little Group|§C3.6★]] (embedded), [[§C3.7★ Massless Particles and Helicity|§C3.7★]] (embedded); Definition §CB.19.6 — [[§C3.6★ Particle States and the Little Group|§C3.6★]] (embedded); Definition §CB.19.9 — [[§C3.6★ Particle States and the Little Group|§C3.6★]] (embedded); Theorem §CB.19.10 — [[§C3.6★ Particle States and the Little Group|§C3.6★]] (embedded); Theorem §CB.19.11 — [[§C3.6★ Particle States and the Little Group|§C3.6★]] (embedded); Theorem §CB.19.12 — [[§C3.6★ Particle States and the Little Group|§C3.6★]] (embedded); Definition §CB.19.7 — [[§C3.7★ Massless Particles and Helicity|§C3.7★]] (embedded).
