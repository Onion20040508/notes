---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: CB
section: CB.4
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification]] · ↑ [[· CB Lie Groups, Lie Algebras and Representations]] · [[§CB.5 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs]] →

*Sources (proofs written from these, each checked against the text): B. C. Hall, An Elementary Introduction to Groups and Representations, Chs. 3, 5 (https://arxiv.org/abs/math-ph/0005032) · P. Woit, Quantum Theory, Groups and Representations, §§5.5, 21.2, 40.2 (https://www.math.columbia.edu/~woit/QM/qmbook.pdf) · P. Etingof, Lie Groups and Lie Algebras, MIT 18.755 notes, §9.4, Exercise 11.4, Remark 17.3 (https://ocw.mit.edu/courses/18-755-lie-groups-and-lie-algebras-ii-spring-2024/mit18_755_s24_lec_full.pdf) · the user's PHY 513 notes, Ch. 7 §§7.2, 7.4 (J± and "the algebra decomposes") · PHY 513 Lecture 7 · PHY 513, Problem Set 5, Problem 1 (as the user wrote it) · Yu Zhao-Huan, 量子场论讲义, §3.2, Exercises 3.1, 3.7 · Peskin & Schroeder, §3.1 · the rest written here.*

Which real Lie algebra is the Lorentz algebra, and in which sense is it "two copies of the rotation algebra"? With the complexification and the real forms of [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification|§CB.3]], this section splits the complexified Lorentz algebra by $\mathbf J_\pm = \frac12(\mathbf J \pm i\mathbf K)$ into two commuting copies of $\mathfrak{sl}(2, \mathbb C)$, contrasts the Euclidean $\mathfrak{so}(4)$, which splits already over $\mathbb R$, shows that $\mathfrak{so}(1,3)$ and $\mathfrak{so}(4)$ are two real forms of one complex algebra (and that $\mathfrak{sl}(2, \mathbb C)$ has two real forms of its own), identifies the real Lie algebra of $SL(2, \mathbb C)$ with the Lorentz algebra, and proves that real forms have the same representations, the input to Weyl's unitary trick in [[§CB.5 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs|§CB.5]]. The course defines the Lorentz algebra in [[§C3.2 The Lorentz Algebra|§C3.2]]; its statements are shown as embeds where they become instances. The complexification of $\mathfrak{sl}(2, \mathbb C)_{\mathbb R}$ and its representations continue in [[§CB.14 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover|§CB.14]].

<!-- Planned content (OPTION1-PLAN §5, row "CB.2a"; batch B1): the C3.2 boxes arrive at the head of this section, before Theorem §CB.4.1 — Def §C3.2.1, Thm §C3.2.1 (3 derivations), Remark "Where derived", Def §C3.2.2, Thm §C3.2.2, Remark "infinitesimal tensor law", new box "one-dimensional representations of 𝔰𝔬(1,3) are zero" (from Thm §C3.4.4); then Thm §C3.2.3 replaces its embed after Theorem §CB.4.1, Thm §C3.2.4 follows, and Remark "What the split does and does not mean" replaces the embed of §C3.3 rem-c3-3-4. In B0 (2026-10-08) Def §CB.4.5, Thm §CB.4.6, Thm §CB.4.7 and the Remark after it were placed here (not at the head of §CB.14 as the plan proposed) because Weyl's unitary trick (Theorem §CB.5.15) uses them. -->

## The Lorentz algebra: the split J± = ½(J ± iK) and the conjugation picture

> [!theorem] Theorem §CB.4.1: The Split of the Complexified Lorentz Algebra
> Let $J_i$, $K_i$ be the rotation and boost generators of the vector representation ([[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-2|Def. §C1a.6.2]]), so that $-iJ_i$, $-iK_i$ are a basis of $\mathfrak{so}(1,3)$ and $J_i, K_i \in i\,\mathfrak{so}(1,3) \subset \mathfrak{so}(1,3)_{\mathbb C}$ ([[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-5|Theorem §CB.3.5]]). In $\mathfrak{so}(1,3)_{\mathbb C}$ ([[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-4|Theorem §CB.3.4]]) put
>
> $$
> J_{\pm i} = \tfrac12\bigl(J_i \pm iK_i\bigr) .
> $$
>
> 1. **Both directions.** $J_i = J_{+i} + J_{-i}$ and $K_i = -i\bigl(J_{+i} - J_{-i}\bigr)$; so $\{J_{+i}, J_{-i}\}$ is a complex basis of $\mathfrak{so}(1,3)_{\mathbb C}$, while no nonzero complex combination of the $J_{+i}$ alone lies in $\mathfrak{so}(1,3)$ or in $i\,\mathfrak{so}(1,3)$.
> 2. **Two commuting copies of 𝔰𝔩(2,ℂ).** $[J_{+i}, J_{+j}] = i\varepsilon_{ijk}J_{+k}$, $[J_{-i}, J_{-j}] = i\varepsilon_{ijk}J_{-k}$, $[J_{+i}, J_{-j}] = 0$. Hence $\mathfrak a_\pm = \operatorname{span}_{\mathbb C}\{J_{\pm i}\}$ are ideals ([[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-3-7|Def. §CB.3.7]]), $\mathfrak{so}(1,3)_{\mathbb C} = \mathfrak a_+ \oplus \mathfrak a_-$ ([[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-3-8|Def. §CB.3.8]]), and $J_{\pm i} \mapsto \frac12\sigma^i$ is an isomorphism $\mathfrak a_\pm \cong \mathfrak{sl}(2, \mathbb C) \cong \mathfrak{su}(2)_{\mathbb C}$, the complexified rotation algebra ([[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-4|Theorem §CB.3.4]]).
> 3. **The conjugation exchanges the copies.** The conjugation $c$ of $\mathfrak{so}(1,3)_{\mathbb C}$ with fixed set $\mathfrak{so}(1,3)$ ([[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-3|Theorem §CB.3.3]]) satisfies $c(J_{\pm i}) = -J_{\mp i}$, so $c(\mathfrak a_\pm) = \mathfrak a_\mp$, and
>
> $$
> \mathfrak{so}(1,3) = \{A + c(A) : A \in \mathfrak a_+\} .
> $$
>
> *Source: the user's PHY 513 notes, Ch. 7 §7.4 (Derivation "The rotation–boost algebra and its complex split") · PHY 513, Problem Set 5, Problem 1(a) (as the user wrote it) · Woit, §40.2 (the split $A_j$, $B_j$ and $\mathfrak{so}(3,1)\otimes\mathbb C = \mathfrak{sl}(2, \mathbb C)\oplus\mathfrak{sl}(2, \mathbb C)$) · Yu, Exercise 3.1 · written here (parts 1 and 3)*

^thm-cb-4-1

> [!proof]- Proof
> *Source: the user's PHY 513 notes, Ch. 7 §7.4, Derivation "The rotation–boost algebra and its complex split" (the brackets of part 2, as in [[§C3.2 The Lorentz Algebra#^der-c3-2-1c|Derivation §C3.2.1 (the J, K form and the J± split)]], steps 6–8) · P. Woit, Quantum Theory, Groups and Representations, §40.2 (the same split in the real basis $l_j = -iJ_j$, $k_j = -iK_j$; "this construction … requires that we complexify") (https://www.math.columbia.edu/~woit/QM/qmbook.pdf). Parts 1 and 3 are written here from Theorems §CB.3.3–§CB.3.5.*
>
> **Step 1** (where $J_i$, $K_i$ live). $-iJ_i$, $-iK_i$ are the generators $M^{jk}$, $M^{0i}$ of the vector representation ([[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-2|Def. §C1a.6.2]]), a real basis of $\mathfrak{so}(1,3)$, hence a complex basis of $\mathfrak{so}(1,3)_{\mathbb C}$, which [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-4|Theorem §CB.3.4]] realizes inside $M_4(\mathbb C)$. So $J_i = i(-iJ_i)$, $K_i = i(-iK_i)$ lie in $i\,\mathfrak{so}(1,3)$, and $\{J_i, K_i\}$ is also a complex basis. Their brackets, computed as $4\times4$ matrices, are ([[§C3.2 The Lorentz Algebra#^thm-c3-2-1|Theorem §C3.2.1]])
>
> $$
> [J_i, J_j] = i\varepsilon_{ijk}J_k, \qquad [J_i, K_j] = i\varepsilon_{ijk}K_k, \qquad [K_i, J_j] = i\varepsilon_{ijk}K_k, \qquad [K_i, K_j] = -i\varepsilon_{ijk}J_k ,
> $$
>
> the third from the second by antisymmetry and $\varepsilon_{jik} = -\varepsilon_{ijk}$.
>
> **Step 2** (part 1: both directions). Adding and subtracting the definitions, $J_{+i} + J_{-i} = J_i$ and $J_{+i} - J_{-i} = iK_i$, so $K_i = -i(J_{+i} - J_{-i})$. The change of basis $\{J_i, K_i\} \leftrightarrow \{J_{+i}, J_{-i}\}$ is invertible over $\mathbb C$, so $\{J_{\pm i}\}$ is a complex basis of $\mathfrak{so}(1,3)_{\mathbb C}$.
>
> **Step 3** (part 2: the copies commute; user's notes, step 6). By bilinearity, all four terms, and Step 1:
>
> $$
> [J_{+i}, J_{-j}] = \tfrac14\bigl([J_i, J_j] - i[J_i, K_j] + i[K_i, J_j] + [K_i, K_j]\bigr) = \tfrac14\bigl(i\varepsilon_{ijk}J_k + \varepsilon_{ijk}K_k - \varepsilon_{ijk}K_k - i\varepsilon_{ijk}J_k\bigr) = 0 .
> $$
>
> **Step 4** (part 2: each copy is an angular momentum; user's notes, step 7). With the same sign in both slots, $(\pm i)^2 = -1$:
>
> $$
> [J_{\pm i}, J_{\pm j}] = \tfrac14\bigl([J_i, J_j] \pm i[J_i, K_j] \pm i[K_i, J_j] - [K_i, K_j]\bigr) = \tfrac14\bigl(2i\varepsilon_{ijk}J_k \mp 2\varepsilon_{ijk}K_k\bigr) = i\varepsilon_{ijk}\cdot\tfrac12\bigl(J_k \pm iK_k\bigr) = i\varepsilon_{ijk}J_{\pm k} ,
> $$
>
> using $\mp\varepsilon K_k = i\varepsilon(\pm iK_k)$.
>
> **Step 5** (part 2: ideals and the isomorphism). By Steps 3–4, $[\mathfrak a_\pm, \mathfrak a_\pm] \subset \mathfrak a_\pm$ and $[\mathfrak a_\mp, \mathfrak a_\pm] = 0$, so $[\mathfrak{so}(1,3)_{\mathbb C}, \mathfrak a_\pm] \subset \mathfrak a_\pm$: both are ideals ([[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-3-7|Def. §CB.3.7]]), and with Step 2 the space is their direct sum, a direct sum of Lie algebras ([[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-3-8|Def. §CB.3.8]]). The matrices $\tau^i = \frac12\sigma^i$ are a complex basis of the traceless $2\times2$ matrices $\mathfrak{sl}(2, \mathbb C)$ (three independent traceless matrices, [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-11|Theorem §CB.1.11]]: complex dimension $3$) with $[\tau^i, \tau^j] = i\varepsilon_{ijk}\tau^k$ ([[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-1|Theorem §C3.1.1]]). The linear bijection $J_{\pm i} \mapsto \tau^i$ matches the brackets of Step 4 on a basis, hence everywhere: $\mathfrak a_\pm \cong \mathfrak{sl}(2, \mathbb C)$, which is $\mathfrak{su}(2)_{\mathbb C}$ by Theorem §CB.3.4.
>
> **Step 6** (part 3: the conjugation). $J_i, K_i \in i\,\mathfrak{so}(1,3)$, so $c(J_i) = -J_i$, $c(K_i) = -K_i$ ([[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-5|Theorem §CB.3.5]], 2). $c$ is conjugate-linear, so
>
> $$
> c(J_{\pm i}) = \tfrac12\bigl(c(J_i) \mp i\,c(K_i)\bigr) = \tfrac12\bigl(-J_i \pm iK_i\bigr) = -J_{\mp i},
> $$
>
> and $c$ maps the complex span $\mathfrak a_\pm$ onto $\mathfrak a_\mp$.
>
> **Step 7** (part 3: the real algebra). For $A \in \mathfrak a_+$, $c(A + cA) = cA + A$ ($c^2 = \mathbb 1$), so $A + cA \in \mathfrak{so}(1,3)$, the fixed set of $c$. The real-linear map $A \mapsto A + cA$ is injective: $A + cA = 0$ gives $A = -cA \in \mathfrak a_+ \cap \mathfrak a_- = \{0\}$. Both spaces have real dimension $6$, so it is onto: $\mathfrak{so}(1,3) = \{A + c(A) : A \in \mathfrak a_+\}$.
>
> **Step 8** (the rest of part 1). If $A \in \mathfrak a_+$ lies in $\mathfrak{so}(1,3)$, then $A = cA \in \mathfrak a_-$, so $A = 0$; if it lies in $i\,\mathfrak{so}(1,3)$, then $A = -cA \in \mathfrak a_-$, so again $A = 0$.
>
> **What the proof shows.**
> - ⚑ By-product: the split exists only after complexifying; neither copy contains a nonzero real Lorentz generator (Step 8). Each real generator is a pair $A + c(A)$, one component in each copy, tied together by conjugation: the "complex angles $\boldsymbol\theta \mp i\boldsymbol\eta$, complex conjugates of each other" of the user's notes, Ch. 7 §7.4.
> - The brackets were computed in the vector representation, but by [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-2|Theorem §C3.1.2]] they hold in every representation; that is [[§C3.2 The Lorentz Algebra#^thm-c3-2-3|Theorem §C3.2.3]].

^pf-cb-4-1

*Uses:* [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-2|Def. §C1a.6.2]], [[§C3.2 The Lorentz Algebra#^thm-c3-2-1|Theorem §C3.2.1]], [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-1|Theorem §C3.1.1]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-11|Theorem §CB.1.11]], [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-3-7|Def. §CB.3.7]], [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-3-8|Def. §CB.3.8]], [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-4|Theorem §CB.3.4]], [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-5|Theorem §CB.3.5]]

The representation-level statement, a pair of commuting angular momenta on a complex space, proved in [[§C3.2 The Lorentz Algebra|§C3.2]]:

![[§C3.2 The Lorentz Algebra#^thm-c3-2-3]]

> [!theorem] Theorem §CB.4.2: The Euclidean 𝔰𝔬(4) Splits Already over ℝ
> In $\mathfrak{so}(4)$ (real antisymmetric $4\times4$ matrices, coordinates $x^0, \dots, x^3$) let $J_i$ be the physicists' generators of rotations of $x^1, x^2, x^3$ and $\tilde K_i$ those of rotations in the $(x^0, x^i)$ planes, with signs chosen so that
>
> $$
> [J_i, J_j] = i\varepsilon_{ijk}J_k, \qquad [J_i, \tilde K_j] = i\varepsilon_{ijk}\tilde K_k, \qquad [\tilde K_i, \tilde K_j] = +i\varepsilon_{ijk}J_k .
> $$
>
> Then $A_{\pm i} = \frac12(J_i \pm \tilde K_i)$, with **no** $i$, obey $[A_{\pm i}, A_{\pm j}] = i\varepsilon_{ijk}A_{\pm k}$ and $[A_{+i}, A_{-j}] = 0$, and $-iA_{\pm i} \in \mathfrak{so}(4)$. So $\mathfrak{so}(4) = \mathfrak b_+ \oplus \mathfrak b_-$ with real ideals $\mathfrak b_\pm = \operatorname{span}_{\mathbb R}\{-iA_{\pm i}\} \cong \mathfrak{su}(2)$; and $\mathfrak{so}(4)_{\mathbb C} = (\mathfrak b_+)_{\mathbb C} \oplus (\mathfrak b_-)_{\mathbb C} \cong \mathfrak{sl}(2, \mathbb C)\oplus\mathfrak{sl}(2, \mathbb C)$, with the conjugation of $\mathfrak{so}(4)_{\mathbb C}$ mapping each summand to itself.
>
> *Source: the user's PHY 513 notes, Ch. 7 §7.4.6 · Woit, §21.2 (the split $M = \frac12(L + K)$, $N = \frac12(L - K)$ of $\mathfrak{so}(4)$) · [[§C8.1★ Symmetries, Conservation Laws and Degeneracies#^thm-c8-1-5|QM Theorem §C8.1.5]] (the same split for the Coulomb problem) · the explicit generators written here*

^thm-cb-4-2

> [!proof]- Proof
> *Source: P. Woit, Quantum Theory, Groups and Representations, §21.2 "so(4) symmetry and the Coulomb potential": from $[L_j, L_k] = i\epsilon_{jkl}L_l$, $[L_j, K_k] = i\epsilon_{jkl}K_l$, $[K_j, K_k] = i\epsilon_{jkl}L_l$ "one has" the two commuting copies $M$, $N$ (https://www.math.columbia.edu/~woit/QM/qmbook.pdf) · the user's PHY 513 notes, Ch. 7 §7.4.6 ("That happens for $\mathfrak{so}(4)$, the Euclidean case, where the two copies are real"). The explicit choice of $J_i$, $\tilde K_i$ that realizes the hypothesis (Steps 1–3) is written here.*
>
> **Step 1** (a basis of $\mathfrak{so}(4)$). For $0 \le a, b \le 3$ let $E_{ab} = e_ae_b^{\mathsf T} - e_be_a^{\mathsf T}$, real antisymmetric; $\{E_{ab}\}_{a<b}$ is a basis of $\mathfrak{so}(4)$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-11|Theorem §CB.1.11]]). Multiplying out with $e_b^{\mathsf T}e_c = \delta_{bc}$ (all four products in each of $E_{ab}E_{cd}$ and $E_{cd}E_{ab}$) gives
>
> $$
> [E_{ab}, E_{cd}] = \delta_{bc}E_{ad} - \delta_{ac}E_{bd} - \delta_{bd}E_{ac} + \delta_{ad}E_{bc} .
> $$
>
> **Step 2** (the generators). Put $J_1 = -iE_{23}$, $J_2 = -iE_{31}$, $J_3 = -iE_{12}$ (i.e. $J_i = -\frac i2\varepsilon_{ijk}E_{jk}$; then $-iJ_3 = -E_{12}$ is the generator $M^{12}$ of the active rotation of $(x^1, x^2)$, [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-3|Theorem §C1a.6.3]], so on $x^1, x^2, x^3$ these are the rotation generators $(J^k)_{lm} = -i\varepsilon^{klm}$ of [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-1|Theorem §C3.1.1]]) and $\tilde K_i = -iE_{0i}$. Then by Step 1:
> - $[J_1, J_2] = (-i)^2[E_{23}, E_{31}] = -E_{21} = E_{12} = iJ_3$;
> - $[\tilde K_1, \tilde K_2] = (-i)^2[E_{01}, E_{02}] = -(-E_{12}) = E_{12} = iJ_3$;
> - $[J_1, \tilde K_2] = -[E_{23}, E_{02}] = -(-E_{03}) = E_{03} = i\tilde K_3$; $[J_2, \tilde K_1] = -[E_{31}, E_{01}] = -E_{03} = -i\tilde K_3$; $[J_1, \tilde K_1] = -[E_{23}, E_{01}] = 0$.
>
> **Step 3** (all index pairs). The cyclic relabelling $\pi$: $0 \mapsto 0$, $1 \mapsto 2$, $2 \mapsto 3$, $3 \mapsto 1$ is realized by the orthogonal permutation matrix $Pe_a = e_{\pi(a)}$, and $PE_{ab}P^{-1} = Pe_ae_b^{\mathsf T}P^{\mathsf T} - \cdots = E_{\pi(a)\pi(b)}$. So $X \mapsto PXP^{-1}$ (a Lie algebra automorphism, [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-9|Theorem §CB.2.9]], 4) sends $J_1 \mapsto J_2 \mapsto J_3 \mapsto J_1$ and $\tilde K_1 \mapsto \tilde K_2 \mapsto \tilde K_3 \mapsto \tilde K_1$, while $\varepsilon_{ijk}$ is invariant under cyclic relabelling. Applying it once and twice to the identities of Step 2, and using antisymmetry of the bracket for $[J_j, J_i]$, $[\tilde K_j, \tilde K_i]$, gives for all $i, j$
>
> $$
> [J_i, J_j] = i\varepsilon_{ijk}J_k, \qquad [J_i, \tilde K_j] = i\varepsilon_{ijk}\tilde K_k, \qquad [\tilde K_i, \tilde K_j] = +i\varepsilon_{ijk}J_k ,
> $$
>
> the hypothesis of the theorem. The sign of the last bracket differs from the Lorentz case ($-i\varepsilon_{ijk}J_k$, [[§C3.2 The Lorentz Algebra#^thm-c3-2-1|Theorem §C3.2.1]]) because $(E_{0i})^2$ is negative on its plane, $(M^{0i})^2$ positive ([[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-3|Theorem §C1a.6.3]]).
>
> **Step 4** (the split with no $i$; Woit). With $A_{\pm i} = \frac12(J_i \pm \tilde K_i)$ and $[\tilde K_i, J_j] = -[J_j, \tilde K_i] = i\varepsilon_{ijk}\tilde K_k$:
>
> $$
> [A_{\pm i}, A_{\pm j}] = \tfrac14\bigl(i\varepsilon_{ijk}J_k \pm i\varepsilon_{ijk}\tilde K_k \pm i\varepsilon_{ijk}\tilde K_k + i\varepsilon_{ijk}J_k\bigr) = i\varepsilon_{ijk}A_{\pm k},
> $$
>
> $$
> [A_{+i}, A_{-j}] = \tfrac14\bigl(i\varepsilon_{ijk}J_k - i\varepsilon_{ijk}\tilde K_k + i\varepsilon_{ijk}\tilde K_k - i\varepsilon_{ijk}J_k\bigr) = 0 .
> $$
>
> **Step 5** (real ideals). $-iA_{\pm i} = \frac12(-iJ_i \mp i\tilde K_i) = \frac12\bigl(-\tfrac12\varepsilon_{ijk}E_{jk} \mp E_{0i}\bigr)$ is a real antisymmetric matrix, so $-iA_{\pm i} \in \mathfrak{so}(4)$. By Step 4, $[-iA_{\pm i}, -iA_{\pm j}] = -[A_{\pm i}, A_{\pm j}] = \varepsilon_{ijk}(-iA_{\pm k})$ and $[-iA_{+i}, -iA_{-j}] = 0$: $\mathfrak b_\pm = \operatorname{span}_{\mathbb R}\{-iA_{\pm i}\}$ are commuting subalgebras with the structure constants $\varepsilon_{ijk}$ of $\mathfrak{su}(2)$ in the basis $-i\tau^k$ (Theorem §C3.1.1), so $\mathfrak b_\pm \cong \mathfrak{su}(2)$. Since $J_i = A_{+i} + A_{-i}$ and $\tilde K_i = A_{+i} - A_{-i}$, the six $-iA_{\pm i}$ span the six $-iJ_i$, $-i\tilde K_i$, i.e. all of $\mathfrak{so}(4)$; six vectors spanning a six-dimensional space are a basis, so $\mathfrak{so}(4) = \mathfrak b_+ \oplus \mathfrak b_-$, and each $\mathfrak b_\pm$ is an ideal ([[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-3-7|Def. §CB.3.7]], [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-3-8|Def. §CB.3.8]]).
>
> **Step 6** (complexification and conjugation). Complex combinations of the basis of Step 5 give $\mathfrak{so}(4)_{\mathbb C} = (\mathfrak b_+)_{\mathbb C}\oplus(\mathfrak b_-)_{\mathbb C}$, and $(\mathfrak b_\pm)_{\mathbb C} \cong \mathfrak{su}(2)_{\mathbb C} \cong \mathfrak{sl}(2, \mathbb C)$ ([[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-4|Theorem §CB.3.4]]). The conjugation fixes $\mathfrak b_\pm \subset \mathfrak{so}(4)$ and, being conjugate-linear, maps $(\mathfrak b_\pm)_{\mathbb C} = \mathfrak b_\pm + i\mathfrak b_\pm$ to itself.
>
> **What the proof shows.**
> - ⚑ By-product: one sign, $[\tilde K_i, \tilde K_j] = +i\varepsilon_{ijk}J_k$ versus $-i\varepsilon_{ijk}J_k$ for boosts, decides whether the split is real (here) or needs complexification (Theorem §CB.4.1).
> - The real split is why $SU(2)\times SU(2)$ covers $SO(4)$ and why the hydrogen spectrum is organized by two angular momenta ([[§C8.1★ Symmetries, Conservation Laws and Degeneracies#^thm-c8-1-5|QM Theorem §C8.1.5]]; Woit §21.2).

^pf-cb-4-2

*Uses:* [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-11|Theorem §CB.1.11]], [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-9|Theorem §CB.2.9]], [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-1|Theorem §C3.1.1]], [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-3-7|Def. §CB.3.7]], [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-3-8|Def. §CB.3.8]], [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-4|Theorem §CB.3.4]]

> [!theorem] Theorem §CB.4.3: 𝔰𝔬(1,3) and 𝔰𝔬(4) Are Two Real Forms of One Complex Algebra
> 1. $J_{\pm i} \mapsto A_{\pm i}$ extends to an isomorphism of complex Lie algebras $\mathfrak{so}(1,3)_{\mathbb C} \cong \mathfrak{so}(4)_{\mathbb C} \cong \mathfrak{sl}(2, \mathbb C)\oplus\mathfrak{sl}(2, \mathbb C)$ ([[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^thm-cb-4-1|Theorem §CB.4.1]], [[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^thm-cb-4-2|Theorem §CB.4.2]]); under it $\mathfrak{so}(1,3)$ and $\mathfrak{so}(4)$ are real forms ([[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-3-10|Def. §CB.3.10]]) of the same complex algebra.
> 2. Their conjugations differ ([[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-11|Theorem §CB.3.11]]): that of $\mathfrak{so}(4)$ maps each $\mathfrak{sl}(2, \mathbb C)$ summand to itself, that of $\mathfrak{so}(1,3)$ exchanges the two.
> 3. $\mathfrak{so}(1,3)$ is simple as a real Lie algebra ([[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-3-9|Def. §CB.3.9]]). In particular $\mathfrak{so}(1,3) \not\cong \mathfrak{su}(2)\oplus\mathfrak{su}(2) \cong \mathfrak{so}(4)$: the real Lorentz algebra is **not** two copies of the rotation algebra; only its complexification is two copies of the complexified rotation algebra $\mathfrak{sl}(2, \mathbb C)$.
>
> *Source: the user's PHY 513 notes, Ch. 7 §§7.4.1, 7.4.6 ("The accurate statement is that the algebra … decomposes") · Woit, §§21.2, 40.2 · Etingof, Lie Groups and Lie Algebras, §9.4, Remark 17.3 · written here (the proof)*

^thm-cb-4-3

> [!proof]- Proof
> *Written here, along the route recorded in batch 1 (an ideal of $\mathfrak{so}(1,3)$ complexifies to a $c$-stable ideal of $\mathfrak a_+\oplus\mathfrak a_-$). Context: P. Etingof, Lie Groups and Lie Algebras (MIT 18.755), §9.4 (real forms as fixed sets of antilinear involutions) and Remark 17.3 ("if $\mathfrak g$ is a simple complex Lie algebra regarded as a real Lie algebra then $\mathfrak g_{\mathbb C} \cong \mathfrak g\oplus\mathfrak g$ is semisimple but not simple") (https://ocw.mit.edu/courses/18-755-lie-groups-and-lie-algebras-ii-spring-2024/mit18_755_s24_lec_full.pdf); P. Woit, §40.2 and §21.2 for the two splits. No source found with this proof for $\mathfrak{so}(1,3)$ itself.*
>
> **Step 1** (part 1). $\{J_{\pm i}\}$ and $\{A_{\pm i}\}$ are complex bases of $\mathfrak{so}(1,3)_{\mathbb C}$ and $\mathfrak{so}(4)_{\mathbb C}$ ([[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^thm-cb-4-1|Theorem §CB.4.1]], 1; Step 5 of the proof of [[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^thm-cb-4-2|Theorem §CB.4.2]]) with identical brackets: $[X_{\pm i}, X_{\pm j}] = i\varepsilon_{ijk}X_{\pm k}$, $[X_{+i}, X_{-j}] = 0$ for $X = J$ and for $X = A$. So the complex-linear bijection $\alpha : J_{\pm i} \mapsto A_{\pm i}$ preserves brackets on a basis, hence everywhere. Each of $\mathfrak{so}(1,3)$, $\mathfrak{so}(4)$ is a real form of its own complexification (the fixed set of $c$, [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-3|Theorem §CB.3.3]]), and $\alpha^{-1}(\mathfrak{so}(4))$ is a real form of $\mathfrak{so}(1,3)_{\mathbb C}$ isomorphic to $\mathfrak{so}(4)$; with Theorem §CB.4.1, 2, both are real forms of $\mathfrak{sl}(2, \mathbb C)\oplus\mathfrak{sl}(2, \mathbb C)$.
>
> **Step 2** (part 2). Transported by $\alpha$, the conjugation of $\mathfrak{so}(4)_{\mathbb C}$ becomes $\sigma' = \alpha^{-1}c_{(4)}\alpha$, which maps each $\mathfrak a_\pm = \alpha^{-1}((\mathfrak b_\pm)_{\mathbb C})$ to itself (Theorem §CB.4.2, Step 6 of its proof), while the conjugation $c$ of $\mathfrak{so}(1,3)_{\mathbb C}$ exchanges $\mathfrak a_+$ and $\mathfrak a_-$ (Theorem §CB.4.1, 3). The two conjugations differ, as they must for non-isomorphic real forms ([[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-11|Theorem §CB.3.11]]); that the real forms are indeed non-isomorphic is Step 6.
>
> **Step 3** ($\mathfrak{sl}(2, \mathbb C)$ is simple). Basis $H = \operatorname{diag}(1, -1)$, $E = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$, $F = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}$; multiplying out, $[H, E] = 2E$, $[H, F] = -2F$, $[E, F] = H$. Let $I \ne 0$ be an ideal and $X = aE + bH + cF \in I$, $X \ne 0$. Then $[E, X] = b[E, H] + c[E, F] = -2bE + cH \in I$ and $[E, [E, X]] = c[E, H] = -2cE \in I$. If $c \ne 0$, $E \in I$. If $c = 0$, $b \ne 0$: $[E, X] = -2bE$, so $E \in I$. If $b = c = 0$: $X = aE$, $a \ne 0$, so $E \in I$. In every case $E \in I$, then $H = [E, F] \in I$ and $F = -\frac12[H, F] \in I$: $I = \mathfrak{sl}(2, \mathbb C)$. It is not abelian, so it is simple ([[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-3-9|Def. §CB.3.9]]).
>
> **Step 4** (the ideals of $\mathfrak a_+\oplus\mathfrak a_-$). Let $I$ be an ideal of $\mathfrak a_+\oplus\mathfrak a_-$ (each $\mathfrak a_\pm \cong \mathfrak{sl}(2, \mathbb C)$, simple by Step 3, hence with trivial centre, since the centre is an ideal $\ne \mathfrak a_\pm$). If some $(x_+, x_-) \in I$ has $x_+ \ne 0$, pick $y \in \mathfrak a_+$ with $[y, x_+] \ne 0$; then $[(y, 0), (x_+, x_-)] = ([y, x_+], 0) \in I \cap \mathfrak a_+$, a nonzero ideal of $\mathfrak a_+$ (brackets with $\mathfrak a_-$ vanish), so $\mathfrak a_+ \subset I$. Likewise for the minus component. Hence $I \in \{0, \mathfrak a_+, \mathfrak a_-, \mathfrak a_+\oplus\mathfrak a_-\}$.
>
> **Step 5** (part 3: $\mathfrak{so}(1,3)$ is simple). Let $\mathfrak i$ be an ideal of $\mathfrak{so}(1,3)$ and $\mathfrak i_{\mathbb C} = \mathfrak i + i\mathfrak i \subset \mathfrak{so}(1,3)_{\mathbb C}$. It is a complex ideal: for $X, Y \in \mathfrak{so}(1,3)$, $A, B \in \mathfrak i$, $[X + iY, A + iB] = ([X, A] - [Y, B]) + i([X, B] + [Y, A]) \in \mathfrak i + i\mathfrak i$. It is $c$-stable: $c(A + iB) = A - iB$. By Step 4 it is $0$, $\mathfrak a_+$, $\mathfrak a_-$ or everything, and $c(\mathfrak a_\pm) = \mathfrak a_\mp \ne \mathfrak a_\pm$ excludes the middle two. Since $\mathfrak i = \mathfrak i_{\mathbb C} \cap \mathfrak{so}(1,3)$ (the $c$-fixed part of $A + iB$ is $A$), $\mathfrak i = 0$ or $\mathfrak i = \mathfrak{so}(1,3)$. And $\mathfrak{so}(1,3)$ is not abelian ($[-iJ_1, -iJ_2] = -iJ_3 \ne 0$). So it is simple.
>
> **Step 6** (not two rotation algebras). $\mathfrak{su}(2)\oplus\mathfrak{su}(2)$ has the ideal $\mathfrak{su}(2)\oplus0$, neither $0$ nor everything, so it is not simple, and by Step 5 it is not isomorphic to $\mathfrak{so}(1,3)$. By Theorem §CB.4.2 it is isomorphic to $\mathfrak{so}(4)$.
>
> **What the proof shows.**
> - ⚑ By-product: "the Lorentz algebra is two copies of the rotation algebra" is true only after complexification; the real algebra is simple, and the two copies are glued by the conjugation → [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^rem-c3-3-4|§C3.3, Remark: What the split does and does not mean]].
> - Simplicity of $\mathfrak{so}(1,3)$ is the hypothesis of Theorem §CB.5.16 (no finite-dimensional unitary representations).

^pf-cb-4-3

*Uses:* [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-3-9|Def. §CB.3.9]], [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-3|Theorem §CB.3.3]], [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-11|Theorem §CB.3.11]], [[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^thm-cb-4-1|Theorem §CB.4.1]], [[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^thm-cb-4-2|Theorem §CB.4.2]]

The course's remark on what the split does and does not mean, in [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra|§C3.3]] (see also [[§C3.2 The Lorentz Algebra#^cau-c3-2-1|§C3.2, Caution: The algebra decomposes; it is not "reducible"]]):

![[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^rem-c3-3-4]]

> [!theorem] Theorem §CB.4.4: Two Real Forms of 𝔰𝔩(2,ℂ)
> $\mathfrak{su}(2)$ and $\mathfrak{sl}(2, \mathbb R)$ are real forms of $\mathfrak{sl}(2, \mathbb C)$, with conjugations $X \mapsto -X^\dagger$ and $X \mapsto \bar X$. They are not isomorphic: $\mathfrak{su}(2)$ has no element $X \ne 0$ for which $\mathrm{ad}_X$ ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^def-cb-2-8|Def. §CB.2.8]]) has a nonzero real eigenvalue, while $H = \operatorname{diag}(1, -1) \in \mathfrak{sl}(2, \mathbb R)$ has $\mathrm{ad}_H$-eigenvalues $0, \pm2$. Moreover $\mathfrak{sl}(2, \mathbb R) \cong \mathfrak{so}(1,2)$ and $\mathfrak{su}(2) \cong \mathfrak{so}(3)$.
>
> *Source: Etingof, Lie Groups and Lie Algebras (MIT 18.755), §9.4 (the same argument for $\mathfrak u(n) \not\cong \mathfrak{gl}(n, \mathbb R)$, via $\mathrm{ad}$) · Hall, An Elementary Introduction to Groups and Representations, Ch. 3 §9 (real forms, Exercise 11) · written here (the details)*

^thm-cb-4-4

> [!proof]- Proof
> *Source: P. Etingof, Lie Groups and Lie Algebras, MIT 18.755 notes, §9.4: "$\mathfrak u(n) \not\cong \mathfrak{gl}_n(\mathbb R)$, since in the first algebra any element $x$ with nilpotent $\mathrm{ad}\,x$ must be zero, while in the second one it does not have to" (https://ocw.mit.edu/courses/18-755-lie-groups-and-lie-algebras-ii-spring-2024/mit18_755_s24_lec_full.pdf); Steps 2–3 run this argument with real eigenvalues of $\mathrm{ad}$ in place of nilpotency. The conjugations and the isomorphism with $\mathfrak{so}(1,2)$ are written here.*
>
> **Step 1** (the two conjugations). On $\mathfrak{sl}(2, \mathbb C)$ put $\sigma_1(X) = -X^\dagger$ and $\sigma_2(X) = \bar X$. Both map traceless matrices to traceless ones ($\operatorname{tr}X^\dagger = \operatorname{tr}\bar X = \overline{\operatorname{tr}X}$), are conjugate-linear and square to $\mathbb 1$. Brackets: $[\sigma_1X, \sigma_1Y] = X^\dagger Y^\dagger - Y^\dagger X^\dagger = (YX - XY)^\dagger = -[X, Y]^\dagger = \sigma_1[X, Y]$, and $\overline{XY - YX} = \bar X\bar Y - \bar Y\bar X$. Fixed sets: $-X^\dagger = X$ with $\operatorname{tr}X = 0$ is $\mathfrak{su}(2)$; $\bar X = X$ with $\operatorname{tr}X = 0$ is $\mathfrak{sl}(2, \mathbb R)$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-11|Theorem §CB.1.11]]). By [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-11|Theorem §CB.3.11]] both are real forms of $\mathfrak{sl}(2, \mathbb C)$.
>
> **Step 2** (in $\mathfrak{su}(2)$, $\mathrm{ad}$ has no nonzero real eigenvalue). On $\mathfrak{su}(2)$ let $B(X, Y) = -\operatorname{tr}(XY)$. It is real: $\overline{\operatorname{tr}(XY)} = \operatorname{tr}((XY)^\dagger) = \operatorname{tr}(Y^\dagger X^\dagger) = \operatorname{tr}(YX) = \operatorname{tr}(XY)$ for anti-Hermitian $X$, $Y$. It is positive definite: $B(X, X) = -\operatorname{tr}(X^2) = \operatorname{tr}(X^\dagger X) = \sum_{ij}|X_{ij}|^2$. It is invariant: $B([Z, X], Y) + B(X, [Z, Y]) = -\operatorname{tr}(ZXY - XZY + XZY - XYZ) = -\operatorname{tr}(ZXY) + \operatorname{tr}(XYZ) = 0$ by cyclicity of the trace. So for $Z \in \mathfrak{su}(2)$, if $\mathrm{ad}_ZX = \lambda X$ with $\lambda \in \mathbb R$, $X \ne 0$ in $\mathfrak{su}(2)$:
>
> $$
> \lambda B(X, X) = B([Z, X], X) = -B(X, [Z, X]) = -\lambda B(X, X) \quad\Longrightarrow\quad \lambda = 0 .
> $$
>
> **Step 3** (in $\mathfrak{sl}(2, \mathbb R)$ it has). With $E$, $F$ as in Step 3 of the proof of [[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^thm-cb-4-3|Theorem §CB.4.3]] (real matrices), $\mathrm{ad}_HE = 2E$, $\mathrm{ad}_HF = -2F$, $\mathrm{ad}_HH = 0$: eigenvalues $0, \pm2$. A Lie algebra isomorphism $f : \mathfrak{sl}(2, \mathbb R) \to \mathfrak{su}(2)$ would satisfy $\mathrm{ad}_{f(H)}f(E) = f([H, E]) = 2f(E)$ with $f(E) \ne 0$, contradicting Step 2. So $\mathfrak{su}(2) \not\cong \mathfrak{sl}(2, \mathbb R)$.
>
> **Step 4** ($\mathfrak{sl}(2, \mathbb R) \cong \mathfrak{so}(1,2)$). In $\mathfrak{so}(1,2)$, $\eta = \operatorname{diag}(1, -1, -1)$, the generators of [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-1|Def. §C1a.6.1]] (same formula, three dimensions) are $M^{01} = e_0e_1^{\mathsf T} + e_1e_0^{\mathsf T}$, $M^{02} = e_0e_2^{\mathsf T} + e_2e_0^{\mathsf T}$, $M^{12} = e_2e_1^{\mathsf T} - e_1e_2^{\mathsf T}$, and multiplying out (with $e_a^{\mathsf T}e_b = \delta_{ab}$)
>
> $$
> [M^{01}, M^{02}] = -M^{12}, \qquad [M^{12}, M^{01}] = M^{02}, \qquad [M^{12}, M^{02}] = -M^{01} .
> $$
>
> In $\mathfrak{sl}(2, \mathbb R)$ put $B_1 = \frac12H$, $B_2 = \frac12(E + F)$, $R = \frac12(F - E)$. With $[H, E] = 2E$, $[H, F] = -2F$, $[E, F] = H$: $[B_1, B_2] = \frac14(2E - 2F) = -R$; $[R, B_1] = \frac14([F, H] - [E, H]) = \frac14(2F + 2E) = B_2$; $[R, B_2] = \frac14([F, E] - [E, F]) = -\frac12H = -B_1$. The linear bijection $B_1 \mapsto M^{01}$, $B_2 \mapsto M^{02}$, $R \mapsto M^{12}$ matches all brackets on a basis: an isomorphism.
>
> **Step 5** ($\mathfrak{su}(2) \cong \mathfrak{so}(3)$). This is [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-1|Theorem §C3.1.1]].
>
> **What the proof shows.**
> - Compactness is visible in the algebra: an invariant positive-definite form (Step 2) forbids real $\mathrm{ad}$-eigenvalues; a "boost" ($H$, or $M^{01}$) has them. The same test shows $\mathfrak{so}(1,3)$ has no invariant inner product → Theorem §CB.5.16.
> - ⚑ By-product: one complex algebra $\mathfrak{sl}(2, \mathbb C)$, two real forms: rotations of $\mathbb R^3$ and Lorentz transformations of $\mathbb R^{1,2}$.

^pf-cb-4-4

*Uses:* [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-11|Theorem §CB.1.11]], [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-11|Theorem §CB.3.11]], [[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^thm-cb-4-3|Theorem §CB.4.3]] (Step 3 of its proof), [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-1|Def. §C1a.6.1]], [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-1|Theorem §C3.1.1]]

## 𝔰𝔩(2,ℂ) as a real Lie algebra

> [!definition] Definition §CB.4.5: Underlying Real Lie Algebra
> The **underlying real Lie algebra** (realification) $\mathfrak h_{\mathbb R}$ of a complex Lie algebra $\mathfrak h$ is $\mathfrak h$ with scalars restricted to $\mathbb R$; $\dim_{\mathbb R}\mathfrak h_{\mathbb R} = 2\dim_{\mathbb C}\mathfrak h$. The Lie algebra of the matrix Lie group $SL(2, \mathbb C)$ ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^def-c5a-4-3|Def. §C5a.4.3]]) is $\mathfrak{sl}(2, \mathbb C)_{\mathbb R}$, of real dimension $6$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-11|Theorem §CB.1.11]]).
>
> *Source: written here*

^def-cb-4-5

> [!theorem] Theorem §CB.4.6: The Real Lie Algebra of SL(2,ℂ) Is the Lorentz Algebra
> The differential ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-3|Theorem §CB.2.3]]) of the covering $\pi : SL(2, \mathbb C) \to SO^+(1,3)$ of [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-7|Theorem §C5a.4.7]] is an isomorphism of real Lie algebras $\mathfrak{sl}(2, \mathbb C)_{\mathbb R} \cong \mathfrak{so}(1,3)$ ([[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^def-cb-4-5|Def. §CB.4.5]]); in the conventions of Theorem §C5a.4.7 it sends $-\frac i2\sigma^k \mapsto -iJ_k$ and $-\frac12\sigma^k \mapsto -iK_k$.
>
> *Source: [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-7|Theorem §C5a.4.7]], 3, differentiated · Yu, Exercise 3.7 · the user's PHY 513 notes, Ch. 8 §8.2 · conventions checked against [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-2|Def. §C1a.6.2]] and [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-3|Theorem §C1a.6.3]] (batch 2)*

^thm-cb-4-6

> [!proof]- Proof
> *Source: the vault's [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-7|Theorem §C5a.4.7]], part 3 (from the user's PHY 513 notes, Ch. 8 §8.2, and Yu, Exercise 3.7), differentiated with [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-3|Theorem §CB.2.3]]. Convention check (batch 2): Larsen's register, $\Lambda = e^{-i\boldsymbol\theta\cdot\mathbf J - i\boldsymbol\eta\cdot\mathbf K}$ with $-iJ_i = M^{jk}$ ($ijk$ cyclic) and $-iK_i = M^{0i}$ ([[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-2|Def. §C1a.6.2]]); the statement's two assignments are confirmed in Steps 2–3, so the statement stands unchanged.*
>
> **Step 1** (a real basis). $\mathfrak{sl}(2, \mathbb C)_{\mathbb R}$ consists of the traceless complex $2\times2$ matrices ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-11|Theorem §CB.1.11]]); $\sigma^1, \sigma^2, \sigma^3$ are a complex basis of them, so the six matrices $-\frac i2\sigma^k$, $-\frac12\sigma^k$ are a real basis. Likewise $-iJ_k$, $-iK_k$ are a real basis of $\mathfrak{so}(1,3)$.
>
> **Step 2** (rotations). By Theorem §C5a.4.7, 3, $\pi(U) = \operatorname{diag}(1, R(U))$ for $U \in SU(2)$, and $R(e^{-is\sigma^k/2})$ is the rotation by $s$ about $x^k$ ([[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-6|QM Theorem §C5.2.6]], 2), which in the vector representation is $e^{-isJ_k} = e^{sM^{ij}}$ ($ijk$ cyclic; [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-3|Theorem §C1a.6.3]], 3). By the formula of Theorem §CB.2.3,
>
> $$
> \pi_\ast\bigl(-\tfrac i2\sigma^k\bigr) = \frac{d}{ds}\pi\bigl(e^{-is\sigma^k/2}\bigr)\Big|_{s=0} = \frac{d}{ds}e^{-isJ_k}\Big|_{s=0} = -iJ_k .
> $$
>
> **Step 3** (boosts). By Theorem §C5a.4.7, 3, $\pi(e^{-\boldsymbol\eta\cdot\boldsymbol\sigma/2})$ is the pure boost $e^\omega$ with $\omega_{0i} = \eta_i$, $\omega_{ij} = 0$; for $\boldsymbol\eta = s\,\mathbf e_k$ this is $e^{sM^{0k}} = e^{-isK_k}$ (Def. §C1a.6.2: $-\frac i2\omega_{\mu\nu}\mathcal J^{\mu\nu} = -i\boldsymbol\eta\cdot\mathbf K$). Hence
>
> $$
> \pi_\ast\bigl(-\tfrac12\sigma^k\bigr) = \frac{d}{ds}\pi\bigl(e^{-s\sigma^k/2}\bigr)\Big|_{s=0} = \frac{d}{ds}e^{-isK_k}\Big|_{s=0} = -iK_k .
> $$
>
> **Step 4** (isomorphism). $\pi_\ast$ is real-linear and preserves brackets (Theorem §CB.2.3) and maps the real basis of Step 1 onto the real basis of Step 1: it is bijective, hence an isomorphism of real Lie algebras $\mathfrak{sl}(2, \mathbb C)_{\mathbb R} \cong \mathfrak{so}(1,3)$ ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^def-cb-2-2|Def. §CB.2.2]]).
>
> **Step 5** (a check on brackets). $[-\frac i2\sigma^1, -\frac i2\sigma^2] = -\frac14[\sigma^1, \sigma^2] = -\frac14\cdot2i\sigma^3 = -\frac i2\sigma^3$, matching $[-iJ_1, -iJ_2] = -[J_1, J_2] = -iJ_3$; and $[-\frac12\sigma^1, -\frac12\sigma^2] = \frac14\cdot2i\sigma^3 = -(-\frac i2\sigma^3)$, matching $[-iK_1, -iK_2] = -[K_1, K_2] = iJ_3 = -(-iJ_3)$ ([[§C3.2 The Lorentz Algebra#^thm-c3-2-1|Theorem §C3.2.1]]).
>
> **What the proof shows.**
> - ⚑ By-product: in $\mathfrak{sl}(2, \mathbb C)$ a boost generator is a complex multiple of a rotation generator, $-\frac12\sigma^k = -i\bigl(-\frac i2\sigma^k\bigr)$. So multiplication by $i$ on $\mathfrak{sl}(2, \mathbb C)$ becomes, on $\mathfrak{so}(1,3)$, the real-linear map $-iJ_k \mapsto iK_k$, $-iK_k \mapsto -iJ_k$ (it squares to $-\mathbb 1$) — a complex structure on $\mathfrak{so}(1,3)$ that is invisible from its definition → Theorem §CB.14.1.
> - The opposite sign convention for $\mathbf K$ ([[§C1a.6 Infinitesimal Lorentz Transformations and Generators|§C1a.6]], after Def. §C1a.6.2: some sources use $K^i = \mathcal J^{i0}$) would flip the second assignment.

^pf-cb-4-6

*Uses:* [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-7|Theorem §C5a.4.7]], [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-6|QM Theorem §C5.2.6]], [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-2|Def. §C1a.6.2]], [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-3|Theorem §C1a.6.3]], [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^def-cb-2-2|Def. §CB.2.2]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-11|Theorem §CB.1.11]], [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-3|Theorem §CB.2.3]], [[§C3.2 The Lorentz Algebra#^thm-c3-2-1|Theorem §C3.2.1]]

> [!theorem] Theorem §CB.4.7: Real Forms Have the Same Representations
> If $\mathfrak g_1$ and $\mathfrak g_2$ are real forms of the same complex Lie algebra $\mathfrak h$ ([[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-3-10|Def. §CB.3.10]]), then restriction and complex-linear extension ([[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-6|Theorem §CB.3.6]]) give bijections between the representations of $\mathfrak g_1$ on complex spaces, the complex-linear representations of $\mathfrak h$, and the representations of $\mathfrak g_2$ on complex spaces, preserving invariant subspaces, irreducibility, direct sums and intertwiners. Example: the finite-dimensional complex representations of $\mathfrak{so}(1,3)$, $\mathfrak{so}(4)$, $\mathfrak{su}(2)\oplus\mathfrak{su}(2)$ and $\mathfrak{sl}(2, \mathbb C)_{\mathbb R}$ correspond to one another (Theorems §CB.4.3, §CB.4.6).
>
> *Source: Hall, An Elementary Introduction to Groups and Representations, Ch. 5 §1, Prop. 5.5 (each correspondence) · Woit, §5.5 · written here (the composition)*

^thm-cb-4-7

> [!proof]- Proof
> *Written here as a composition of two instances of [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-6|Theorem §CB.3.6]] (B. C. Hall, An Elementary Introduction to Groups and Representations, Prop. 5.5, https://arxiv.org/abs/math-ph/0005032; P. Woit, §5.5, whose example is exactly this use: representations of $\mathfrak{su}(2)$ through $\mathfrak{sl}(2, \mathbb C)$).*
>
> **Step 1** (from $\mathfrak g_1$ to $\mathfrak h$). $\mathfrak g_1$ is a real form of $\mathfrak h$, so $X + iY \mapsto X + iY$ is an isomorphism $(\mathfrak g_1)_{\mathbb C} \cong \mathfrak h$ ([[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-3-10|Def. §CB.3.10]]). Composing with it, Theorem §CB.3.6 says: a representation $d$ of $\mathfrak g_1$ on a complex space $W$ extends uniquely to the complex-linear representation $\tilde d(X + iY) = d(X) + i\,d(Y)$ of $\mathfrak h$ ($X, Y \in \mathfrak g_1$), and every complex-linear representation of $\mathfrak h$ arises so, by restriction to $\mathfrak g_1 \subset \mathfrak h$.
>
> **Step 2** (from $\mathfrak h$ to $\mathfrak g_2$). The same for $\mathfrak g_2$: restriction of complex-linear representations of $\mathfrak h$ to $\mathfrak g_2$ is a bijection onto the representations of $\mathfrak g_2$ on complex spaces, with inverse the complex-linear extension.
>
> **Step 3** (composition). $d \mapsto \tilde d|_{\mathfrak g_2}$ is a bijection from representations of $\mathfrak g_1$ to representations of $\mathfrak g_2$ on the same space $W$, inverse to the analogous map in the other direction. Invariant subspaces, irreducibility, direct sums and intertwiners are preserved at each of the two steps (Theorem §CB.3.6, 2), hence by the composition.
>
> **Step 4** (the example). $\mathfrak{so}(1,3)$ and $\mathfrak{so}(4)$ are real forms of one complex algebra ([[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^thm-cb-4-3|Theorem §CB.4.3]], 1). A Lie algebra isomorphism $f : \mathfrak g \to \mathfrak g'$ turns representations of $\mathfrak g'$ into those of $\mathfrak g$ by $d' \mapsto d'\circ f$, bijectively and preserving all four structures; apply it to $\mathfrak{so}(4) \cong \mathfrak{su}(2)\oplus\mathfrak{su}(2)$ ([[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^thm-cb-4-2|Theorem §CB.4.2]]) and $\mathfrak{sl}(2, \mathbb C)_{\mathbb R} \cong \mathfrak{so}(1,3)$ ([[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^thm-cb-4-6|Theorem §CB.4.6]]).
>
> **What the proof shows.**
> - Only the complex-linear algebra structure is transported; unitarity and integrability to a group are not (Remark below; [[§CB.5 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-5-15|Theorem §CB.5.15]] uses this theorem together with the compact group to recover complete reducibility).
> - ⚑ By-product: the finite-dimensional representations of the Lorentz algebra are classified by those of $\mathfrak{su}(2)\oplus\mathfrak{su}(2)$, i.e. by pairs of spins → [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-2|Theorem §C3.3.2]].

^pf-cb-4-7

*Uses:* [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-3-10|Def. §CB.3.10]], [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-6|Theorem §CB.3.6]], [[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^thm-cb-4-2|Theorem §CB.4.2]], [[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^thm-cb-4-3|Theorem §CB.4.3]], [[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^thm-cb-4-6|Theorem §CB.4.6]]

> [!remark] Remark: What the correspondence does not transport
> Theorem §CB.4.7 transports the algebra of the representations, not unitarity and not the group: a representation of $\mathfrak{so}(4)$ that is unitary for $SU(2)\times SU(2)$ becomes a representation of $\mathfrak{so}(1,3)$ whose boosts are not unitary ([[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-10|Theorem §C3.3.10]]). Complete reducibility does survive, which is Weyl's unitary trick ([[§CB.5 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs|§CB.5]]): it needs the compact-group theorem of §CB.5, so it is stated there, after that theorem, and not here.

^rem-cb-4-1

> [!remark]- Connections
> - The same algebra, $\mathfrak{so}(4) \cong \mathfrak{su}(2)\oplus\mathfrak{su}(2)$ over $\mathbb R$, is the hidden symmetry of the hydrogen atom ([[§C8.1★ Symmetries, Conservation Laws and Degeneracies#^thm-c8-1-5|QM Theorem §C8.1.5]]): there the split needs no $i$ (Theorem §CB.4.2), for the Lorentz algebra it does (Theorem §CB.4.3).
> - **Used in**: Theorem §CB.4.1 — [[§C3.2 The Lorentz Algebra#^thm-c3-2-3|Theorem §C3.2.3]], [[§C3.2 The Lorentz Algebra#^thm-c3-2-4|Theorem §C3.2.4]], [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^def-c3-3-1|Def. §C3.3.1]], [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^rem-c3-3-3|§C3.3, Remark: What the labels (j₊, j₋) mean]], [[§C1a.7 Relativistic Electrodynamics in Index Form#^thm-c1a-7-3|Theorem §C1a.7.3]]; Theorems §CB.4.2–§CB.4.3 — [[§C3.2 The Lorentz Algebra#^cau-c3-2-1|§C3.2, Caution: The algebra decomposes; it is not "reducible"]], [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^rem-c3-3-4|§C3.3, Remark: What the split does and does not mean]], [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-2|Theorem §C3.3.2]]; Theorem §CB.4.6 — [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^def-c5a-4-3|Def. §C5a.4.3]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-8|Theorem §C5a.4.8]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-9|Theorem §C5a.4.9]]
