---
type: demo
subject: "[[Quantum Field Theory]]"
tags: [demo]
---
**DEMO** — preview of the proposed layout (option 1): the CB home of the abstract content of [[§C5a.3 The Lorentz Action on Spinor Space]]; its physics side is [[Demo §C5a.3 The Lorentz Action on Spinor Space (option 1)]]; see [[Demo README]]; delete after review.

↑ [[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element|§CB.7]] (Clifford modules, volume element) · [[§CB.8 Complex Clifford Algebras and Clifford Modules|§CB.8]] (irreducible modules) · physics: [[Demo §C5a.3 The Lorentz Action on Spinor Space (option 1)|§C5a.3 (demo)]] →

*Sources: Peskin & Schroeder, An Introduction to Quantum Field Theory, §3.2, pp. 40–43, eqs. (3.23)–(3.24), (3.30), and §3.4, p. 50 · PHY 513, Problem Set 4, Problem 5(b)–(c) (as the user wrote them; submitted) · PHY 513 Lecture 7 (Larsen), Part B ("Claim: $S^{\mu\nu}$ satisfy Lorentz algebra"); Lecture 8, Part A ("Compute (using Dirac algebra)"), Part B · the user's PHY 513 notes, Ch. 8 §8.1 (Derivations "Proof of the claim", "Hermiticity of the Dirac matrices: Consequence for the generators", "What replaces unitarity", Step 1) · Yu Zhao-Huan, 量子场论讲义, §5.1, eqs. (5.8)–(5.16), (5.24) · the basis-free splitting by the volume element written here.*

Which representation of the Lie algebra $\mathfrak{so}(1,3)$ does a Clifford module of $\mathrm{Cl}(1,3)$ carry? A Clifford module is a complex vector space $W$ with four linear maps $\gamma^\mu$ obeying $\gamma^\mu\gamma^\nu + \gamma^\nu\gamma^\mu = 2g^{\mu\nu}\mathbb 1$ ([[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^def-cb-7-9|Def. §CB.7.9]], [[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-10|Theorem §CB.7.10]]); nothing in that definition mentions $\mathfrak{so}(1,3)$. This section shows that the antisymmetrized products $S^{\mu\nu} = \frac i4[\gamma^\mu, \gamma^\nu]$ act on the $\gamma$'s as $\mathfrak{so}(1,3)$ acts on $\mathbb R^{1,3}$, that they obey the commutation relations of $\mathfrak{so}(1,3)$ and so define a representation on $W$, that on a four-dimensional module the volume element splits this representation into $(\frac12, 0)\oplus(0, \frac12)$ without choosing a basis, and how the generators behave under the adjoint of a Hermitian module.

*Setting.* $g = \operatorname{diag}(+,-,-,-)$ on $\mathbb R^{1,3}$; $W$ a complex Clifford module of $\mathrm{Cl}(1,3)$ with maps $\gamma^\mu \in \operatorname{End}(W)$ (in the physics chapter: spinor space $V$ with the Dirac maps $\Gamma^\mu$, [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-9|Def. §C5a.1.9]], whose matrices are the Dirac matrices); $\mathfrak{so}(1,3)$ with the basis $\mathcal J^{\rho\sigma}$ of [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-1|Def. §C1a.6.1]] and the relations of [[§C3.2 The Lorentz Algebra#^thm-c3-2-1|Theorem §C3.2.1]] (Hermitian-generator convention, [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-5|Theorem §CB.2.5]]); $J_i = \frac12\varepsilon_{ijk}S^{jk}$, $K_i = S^{0i}$, $\mathbf J_\pm = \frac12(\mathbf J \pm i\mathbf K)$ ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-12|Theorem §CB.2.12]]).

## The generators of a Clifford module

> [!definition] Definition §CB.11.1: The Generators of a Clifford Module
> For a Clifford module $(W, \gamma^\mu)$ of $\mathrm{Cl}(1,3)$ ([[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^def-cb-7-9|Def. §CB.7.9]]), the six **generators** are the elements of $\operatorname{End}(W)$
>
> $$
> S^{\mu\nu} = \frac i4\,[\gamma^\mu, \gamma^\nu] = -S^{\nu\mu}, \qquad\text{equivalently}\qquad S^{\mu\nu} = \frac i2\bigl(\gamma^\mu\gamma^\nu - g^{\mu\nu}\mathbb 1\bigr) .
> $$
>
> *Source: PS §3.2, eq. (3.23) · PHY 513 Lecture 7, Part B ("Given such $\gamma^\mu$, form a $4\times4$ matrix for each $(\mu\nu)$ pair") · the user's PHY 513 notes, Ch. 8 §8.1 (Definition "The spinor generators", eq. (Sdef)) · Yu §5.1, eqs. (5.8)–(5.9)*

^demo-cb-11-def-1

The second form follows from $\gamma^\nu\gamma^\mu = 2g^{\mu\nu} - \gamma^\mu\gamma^\nu$: $[\gamma^\mu, \gamma^\nu] = 2\gamma^\mu\gamma^\nu - 2g^{\mu\nu}$. For $\mu \ne \nu$, $S^{\mu\nu} = \frac i2\gamma^\mu\gamma^\nu$; $S^{\mu\mu} = 0$. Each $S^{\mu\nu}$ lies in the image of the even part $\mathrm{Cl}^0(1,3)$ ([[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^def-cb-7-12|Def. §CB.7.12]]); their span is the Lie algebra of the spin group (§CB.9 in the plan).

> [!theorem] Theorem §CB.11.2: The Generators Act on the γ's as on Vectors
> With the generators $(\mathcal J^{\rho\sigma})^\mu{}_\nu = i(g^{\rho\mu}\delta^\sigma{}_\nu - g^{\sigma\mu}\delta^\rho{}_\nu)$ of $\mathfrak{so}(1,3)$ on $\mathbb R^{1,3}$ ([[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-1|Def. §C1a.6.1]]) and $S^{\rho\sigma}$ of Def. §CB.11.1,
>
> $$
> [\gamma^\mu, S^{\rho\sigma}] = (\mathcal J^{\rho\sigma})^\mu{}_\nu\,\gamma^\nu = i\bigl(g^{\mu\rho}\gamma^\sigma - g^{\mu\sigma}\gamma^\rho\bigr) :
> $$
>
> on the span of the $\gamma^\mu$, the commutator with $S^{\rho\sigma}$ acts on the label $\mu$ as $\mathcal J^{\rho\sigma}$ acts on the components of a vector of $\mathbb R^{1,3}$.
>
> *Source: PHY 513, Problem Set 4, Problem 5(b) (as the user wrote it) · PS §3.2, p. 42 (stated, "with a short computation") · PHY 513 Lecture 8, Part A ("Compute (using Dirac algebra)") · the user's PHY 513 notes, Ch. 8 §8.1 (Derivation "Proof of the claim", Step 1, eq. (gammaS)) · Yu §5.1, eqs. (5.11), (5.24)*

^demo-cb-11-thm-2

> [!proof]- Proof
> (The user's solution of Problem Set 4, Problem 5(b).)
>
> **1. Pull out the factor.** By linearity of the commutator, $[\gamma^\mu, S^{\rho\sigma}] = \frac i4[\gamma^\mu, [\gamma^\rho, \gamma^\sigma]]$, and $[\gamma^\mu, [\gamma^\rho, \gamma^\sigma]] = [\gamma^\mu, \gamma^\rho\gamma^\sigma] - [\gamma^\mu, \gamma^\sigma\gamma^\rho]$.
>
> **2. The reordering identity.** For any elements of an associative algebra, $[A, BC] = \{A, B\}C - B\{A, C\}$: the right side is $ABC + BAC - BAC - BCA = ABC - BCA$. Applied to both terms:
>
> $$
> [\gamma^\mu, [\gamma^\rho, \gamma^\sigma]] = \{\gamma^\mu, \gamma^\rho\}\gamma^\sigma - \gamma^\rho\{\gamma^\mu, \gamma^\sigma\} - \{\gamma^\mu, \gamma^\sigma\}\gamma^\rho + \gamma^\sigma\{\gamma^\mu, \gamma^\rho\} .
> $$
>
> **3. Insert the Clifford relation.** Each anticommutator is $2g\,\mathbb 1$, a number times the identity, which commutes with every $\gamma$ and may be moved freely: the four terms are $2g^{\mu\rho}\gamma^\sigma - 2g^{\mu\sigma}\gamma^\rho - 2g^{\mu\sigma}\gamma^\rho + 2g^{\mu\rho}\gamma^\sigma = 4(g^{\mu\rho}\gamma^\sigma - g^{\mu\sigma}\gamma^\rho)$.
>
> **4. Restore the factor and read off 𝒥.** $[\gamma^\mu, S^{\rho\sigma}] = \frac i4\cdot4(g^{\mu\rho}\gamma^\sigma - g^{\mu\sigma}\gamma^\rho) = i(g^{\mu\rho}\gamma^\sigma - g^{\mu\sigma}\gamma^\rho)$. Write $\gamma^\sigma = \delta^\sigma{}_\nu\gamma^\nu$, $\gamma^\rho = \delta^\rho{}_\nu\gamma^\nu$ and use $g^{\mu\rho} = g^{\rho\mu}$: $i(g^{\rho\mu}\delta^\sigma{}_\nu - g^{\sigma\mu}\delta^\rho{}_\nu)\gamma^\nu = (\mathcal J^{\rho\sigma})^\mu{}_\nu\gamma^\nu$.
>
> **What the proof shows**
> - Only the Clifford relation was used: the result holds for every Clifford module, in every basis, of every dimension, and with $g$ replaced by any nondegenerate symmetric form.
> - Used next: the commutation relations of the $S$'s (Theorem §CB.11.3).

^demo-cb-11-pf-2

*Uses:* [[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-10|Theorem §CB.7.10]], [[Demo §CB.11 Spin(1,3) and the Lorentz Algebra on Spinor Space#^demo-cb-11-def-1|Def. §CB.11.1]], [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-1|Def. §C1a.6.1]]

> [!theorem] Theorem §CB.11.3: The Generators Represent 𝔰𝔬(1,3)
>
> $$
> [S^{\mu\nu}, S^{\rho\sigma}] = i\bigl(g^{\nu\rho}S^{\mu\sigma} - g^{\mu\rho}S^{\nu\sigma} - g^{\nu\sigma}S^{\mu\rho} + g^{\mu\sigma}S^{\nu\rho}\bigr) ,
> $$
>
> the relations of [[§C3.2 The Lorentz Algebra#^thm-c3-2-1|Theorem §C3.2.1]] with $\mathcal J \to S$. Hence $\mathcal J^{\mu\nu} \mapsto S^{\mu\nu}$ (Def. §CB.11.1) is a representation of $\mathfrak{so}(1,3)$ on $W$ ([[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-6|Def. §C3.1.6]]), the **Clifford representation**. With $g$ replaced by $\operatorname{diag}(\mathbb 1_p, -\mathbb 1_q)$ the same holds for $\mathfrak{so}(p, q)$ on every Clifford module of $\mathrm{Cl}(p, q)$.
>
> *Source: PHY 513, Problem Set 4, Problem 5(c) (as the user wrote it) · PS §3.2, p. 40 ("By repeated use of (3.22), it is easy to verify") · PHY 513 Lecture 7, Part B ("Claim: $S^{\mu\nu}$ satisfy Lorentz algebra") · the user's PHY 513 notes, Ch. 8 §8.1 (Derivation "Proof of the claim", Step 2) · Yu §5.1, eq. (5.12)*

^demo-cb-11-thm-3

> [!proof]- Proof
> (The user's solution of Problem Set 4, Problem 5(c).)
>
> **1. Pull out the factor.** $[S^{\mu\nu}, S^{\rho\sigma}] = \frac i4X$ with $X \equiv [[\gamma^\mu, \gamma^\nu], S^{\rho\sigma}] = [\gamma^\mu\gamma^\nu, S^{\rho\sigma}] - [\gamma^\nu\gamma^\mu, S^{\rho\sigma}]$.
>
> **2. Product rule.** With $[AB, C] = A[B, C] + [A, C]B$ (expand: $ABC - ACB + ACB - CAB$):
>
> $$
> X = \gamma^\mu[\gamma^\nu, S^{\rho\sigma}] + [\gamma^\mu, S^{\rho\sigma}]\gamma^\nu - \gamma^\nu[\gamma^\mu, S^{\rho\sigma}] - [\gamma^\nu, S^{\rho\sigma}]\gamma^\mu .
> $$
>
> **3. Insert Theorem §CB.11.2.** $[\gamma^\mu, S^{\rho\sigma}] = i(g^{\rho\mu}\gamma^\sigma - g^{\sigma\mu}\gamma^\rho)$ and $[\gamma^\nu, S^{\rho\sigma}] = i(g^{\rho\nu}\gamma^\sigma - g^{\sigma\nu}\gamma^\rho)$. Expanding all four products into eight terms:
>
> $$
> X = i\bigl[g^{\rho\nu}\gamma^\mu\gamma^\sigma - g^{\sigma\nu}\gamma^\mu\gamma^\rho + g^{\rho\mu}\gamma^\sigma\gamma^\nu - g^{\sigma\mu}\gamma^\rho\gamma^\nu - g^{\rho\mu}\gamma^\nu\gamma^\sigma + g^{\sigma\mu}\gamma^\nu\gamma^\rho - g^{\rho\nu}\gamma^\sigma\gamma^\mu + g^{\sigma\nu}\gamma^\rho\gamma^\mu\bigr] .
> $$
>
> **4. Pair into commutators.** First with seventh, second with eighth, third with fifth, fourth with sixth:
>
> $$
> X = i\bigl[g^{\rho\nu}[\gamma^\mu, \gamma^\sigma] - g^{\sigma\nu}[\gamma^\mu, \gamma^\rho] + g^{\rho\mu}[\gamma^\sigma, \gamma^\nu] - g^{\sigma\mu}[\gamma^\rho, \gamma^\nu]\bigr] .
> $$
>
> **5. Back to S.** From Def. §CB.11.1, $[\gamma^a, \gamma^b] = -4iS^{ab}$, so $X = i(-4i)[g^{\rho\nu}S^{\mu\sigma} - g^{\sigma\nu}S^{\mu\rho} + g^{\rho\mu}S^{\sigma\nu} - g^{\sigma\mu}S^{\rho\nu}] = 4[\dots]$.
>
> **6. Restore the factor and reorder.** $[S^{\mu\nu}, S^{\rho\sigma}] = \frac i4X = i(g^{\nu\rho}S^{\mu\sigma} - g^{\nu\sigma}S^{\mu\rho} + g^{\mu\rho}S^{\sigma\nu} - g^{\mu\sigma}S^{\rho\nu})$; with $S^{\sigma\nu} = -S^{\nu\sigma}$, $S^{\rho\nu} = -S^{\nu\rho}$ and the symmetry of $g$ this is $i(g^{\nu\rho}S^{\mu\sigma} - g^{\mu\rho}S^{\nu\sigma} - g^{\nu\sigma}S^{\mu\rho} + g^{\mu\sigma}S^{\nu\rho})$.
>
> **What the proof shows**
> - The commutation relations of $\mathfrak{so}(1,3)$ are a consequence of the Clifford relation alone, through Theorem §CB.11.2: in any dimension and signature, $\frac i4[\gamma, \gamma]$ represents the corresponding orthogonal algebra. In three dimensions with $\gamma^j = i\sigma^j$ (signature $(0,3)$) it gives $S^{ij} = \frac12\varepsilon^{ijk}\sigma^k$, spin ½ (PS (3.24)).
> - Exponentiating the six $S$'s gives a representation of a group only because they obey its Lie algebra (Def. §CB.11.4); the group so obtained covers $SO^+(1,3)$ twice ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-8|Theorem §C5a.4.8]]; §CB.9 in the plan). Yu's route (5.11)–(5.12) is the same computation, with $[S^{\mu\nu}, \gamma^\rho]$ in place of $[\gamma^\mu, S^{\rho\sigma}]$.

^demo-cb-11-pf-3

*Uses:* [[Demo §CB.11 Spin(1,3) and the Lorentz Algebra on Spinor Space#^demo-cb-11-def-1|Def. §CB.11.1]], [[Demo §CB.11 Spin(1,3) and the Lorentz Algebra on Spinor Space#^demo-cb-11-thm-2|Theorem §CB.11.2]], [[§C3.2 The Lorentz Algebra#^thm-c3-2-1|Theorem §C3.2.1]]

> [!definition] Definition §CB.11.4: The Exponentiated Clifford Representation
> For real parameters $\omega_{\mu\nu} = -\omega_{\nu\mu}$ ([[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-1|Def. §C1a.6.1]]) and the generators of Def. §CB.11.1,
>
> $$
> \Lambda_W(\omega) = \exp\Bigl(-\frac i2\,\omega_{\mu\nu}S^{\mu\nu}\Bigr) \in GL(W) ,
> $$
>
> the matrix exponential ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-1|Def. §CB.1.1]]) of the Clifford representation (Theorem §CB.11.3).
>
> *Source: PS §3.2, eq. (3.30) · PHY 513 Lecture 7, Part B ("Finite Lorentz Transformations in Dirac Representation") · the user's PHY 513 notes, Ch. 8 §8.1 (Definition "The spinor Lorentz transformation $\Lambda_{1/2}$", eq. (Lhalf)) · Yu §5.1, eqs. (5.14), (5.16)*

^demo-cb-11-def-4

The exponent is linear in the six parameters; $\Lambda_W$ depends on them nonlinearly. $\Lambda_W(\omega)^{-1} = \Lambda_W(-\omega)$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-2|Theorem §CB.1.2]]; Yu (5.16)).

## The splitting by the volume element

> [!theorem] Theorem §CB.11.5: The Volume Element Splits a Four-Dimensional Clifford Module into (½, 0) ⊕ (0, ½)
> Let $\dim W = 4$ (an irreducible module, [[§CB.8 Complex Clifford Algebras and Clifford Modules#^thm-cb-8-7|Theorem §CB.8.7]]) and $\gamma^5 = i\gamma^0\gamma^1\gamma^2\gamma^3$, the image of $i$ times the volume element ([[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-19|Theorem §CB.7.19]]). With $J_i$, $K_i$, $\mathbf J_\pm$ of the Clifford representation (Theorem §CB.11.3):
> 1. $[\gamma^5, S^{\mu\nu}] = 0$ and $K_i = i\gamma^5J_i$, hence $\mathbf J_\pm = \frac12(\mathbb 1 \mp \gamma^5)\,\mathbf J$.
> 2. $W = W_-\oplus W_+$, the eigenspaces of $\gamma^5$ for $-1$ and $+1$; both are two-dimensional and invariant under every $S^{\mu\nu}$ and every $\Lambda_W(\omega)$ (Def. §CB.11.4).
> 3. On $W_-$, $\mathbf J_- = 0$ and $\mathbf J_+ = \mathbf J$ has spin ½; on $W_+$, $\mathbf J_+ = 0$ and $\mathbf J_- = \mathbf J$ has spin ½. So $W_- \cong (\frac12, 0)$, $W_+ \cong (0, \frac12)$ ([[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^def-c3-3-1|Def. §C3.3.1]]), and $W \cong (\frac12, 0)\oplus(0, \frac12)$.
> 4. $e^{-2\pi iJ_3} = -\mathbb 1_W$: the Clifford representation is a spinor representation ([[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^def-c3-3-2|Def. §C3.3.2]]).
>
> *Source: PS §3.4, p. 50 ("$[\gamma^5, S^{\mu\nu}] = 0$. Thus the Dirac representation must be reducible …") · PHY 513 Lecture 7, Part B ("4 dim. Dirac spinor representation is reducible") · the user's PHY 513 notes, Ch. 8 §8.2 ("How the two halves transform"), Ch. 9 §9.6 · the basis-free route (part 1, the relation $K_i = i\gamma^5J_i$, and parts 2–4) written here*

^demo-cb-11-thm-5

> [!proof]- Proof
> **1. γ⁵ commutes with the generators.** $\gamma^5$ anticommutes with each $\gamma^\mu$ ([[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-19|Theorem §CB.7.19]], 3; [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-1|Theorem §C5a.5.1]]), so it commutes with a product of two: $\gamma^5\gamma^\mu\gamma^\nu = -\gamma^\mu\gamma^5\gamma^\nu = \gamma^\mu\gamma^\nu\gamma^5$, and hence with $S^{\mu\nu} = \frac i2(\gamma^\mu\gamma^\nu - g^{\mu\nu}\mathbb 1)$.
>
> **2. K = iγ⁵J.** Let $(i, j, k)$ be a cyclic permutation of $(1, 2, 3)$. Then $J_i = \frac12(S^{jk} - S^{kj}) = S^{jk} = \frac i2\gamma^j\gamma^k$ and $K_i = S^{0i} = \frac i2\gamma^0\gamma^i$. A cyclic permutation of three anticommuting factors is two transpositions, so $\gamma^1\gamma^2\gamma^3 = \gamma^i\gamma^j\gamma^k$ and $\gamma^5 = i\gamma^0\gamma^i\gamma^j\gamma^k$. Then
>
> $$
> \gamma^5J_i = i\cdot\tfrac i2\,\gamma^0\gamma^i\,(\gamma^j\gamma^k\gamma^j\gamma^k) = -\tfrac12\gamma^0\gamma^i\bigl(-(\gamma^j)^2(\gamma^k)^2\bigr) = -\tfrac12\gamma^0\gamma^i\bigl(-(-1)(-1)\bigr) = \tfrac12\gamma^0\gamma^i = -iK_i ,
> $$
>
> using $\gamma^k\gamma^j = -\gamma^j\gamma^k$ and $(\gamma^j)^2 = (\gamma^k)^2 = -\mathbb 1$. So $K_i = i\gamma^5J_i$, and $\mathbf J_\pm = \frac12(\mathbf J \pm i\cdot i\gamma^5\mathbf J) = \frac12(\mathbb 1 \mp \gamma^5)\mathbf J$.
>
> **3. The two eigenspaces.** $(\gamma^5)^2 = \mathbb 1$ (Theorem §CB.7.19, 2, times $i^2$), so $P_\mp = \frac12(\mathbb 1 \mp \gamma^5)$ are complementary projections and $W = P_-W \oplus P_+W = W_-\oplus W_+$. $\operatorname{tr}\gamma^5 = 0$ (Theorem §C5a.5.1), so the eigenvalues $-1$ and $+1$ occur equally often: $\dim W_\pm = 2$. A map commuting with $\gamma^5$ maps each eigenspace into itself; this holds for every $S^{\mu\nu}$ (step 1) and for $\Lambda_W(\omega)$, a power series in them.
>
> **4. The labels.** On $W_-$, $\gamma^5 = -1$, so by step 2 $\mathbf J_+ = \mathbf J$ and $\mathbf J_- = 0$; on $W_+$ the reverse. The $J_i$ obey $[J_i, J_j] = i\varepsilon_{ijk}J_k$ (Theorem §CB.11.3 for spatial indices), and $J_i^2 = -\frac14\gamma^j\gamma^k\gamma^j\gamma^k = \frac14(\gamma^j)^2(\gamma^k)^2 = \frac14\mathbb 1$. On the two-dimensional $W_-$, $J_3 = -i[J_1, J_2]$ is a commutator, so it is traceless; $J_3^2 = \frac14$ makes it diagonalizable with eigenvalues in $\{\frac12, -\frac12\}$, so its weights are $\frac12$ and $-\frac12$, once each, which by [[§CB.6 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-6-4|Theorem §CB.6.4]] is spin ½. With $\mathbf J_- = 0$ this is $(\frac12, 0)$ (Def. §C3.3.1 with $j_+ = \frac12$, $j_- = 0$); likewise $W_+ \cong (0, \frac12)$.
>
> **5. The 2π rotation.** $(2J_3)^2 = \mathbb 1$, so $e^{-2\pi iJ_3} = e^{-i\pi(2J_3)} = \cos\pi\,\mathbb 1 - i\sin\pi\,(2J_3) = -\mathbb 1$.
>
> **What the proof shows**
> - No basis was chosen: the splitting is fixed by $\gamma^5$ alone, and any basis adapted to $W_-\oplus W_+$ makes all six generators block diagonal (in physics: the chiral basis).
> - $W_\pm$ are irreducible and inequivalent ([[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-1|Theorem §C3.3.1]]): the half-spin representations (§CB.12 in the plan).

^demo-cb-11-pf-5

*Uses:* [[Demo §CB.11 Spin(1,3) and the Lorentz Algebra on Spinor Space#^demo-cb-11-thm-3|Theorem §CB.11.3]], [[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-19|Theorem §CB.7.19]], [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-1|Theorem §C5a.5.1]], [[§CB.6 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-6-4|Theorem §CB.6.4]], [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^def-c3-3-1|Def. §C3.3.1]]

## Adjoints of the generators

> [!theorem] Theorem §CB.11.6: Adjoints of the Generators of a Hermitian Clifford Module
> Let $W$ carry an inner product in which $\gamma^{\mu\dagger} = \gamma^0\gamma^\mu\gamma^0$ (for the Dirac matrices: [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-11|Theorem §C5a.1.11]]).
> 1. $S^{\mu\nu\dagger} = \gamma^0S^{\mu\nu}\gamma^0$. In particular $S^{ij}$ commutes with $\gamma^0$ and is Hermitian; $S^{0i}$ anticommutes with $\gamma^0$ and is anti-Hermitian.
> 2. $\Lambda_W(\omega)$ (Def. §CB.11.4) is unitary when only the $\omega_{ij}$ are nonzero, and Hermitian with positive eigenvalues, not unitary, when only the $\omega_{0i}$ are nonzero: the spin-½ case of [[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-3-16|Theorem §CB.3.16]] ([[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-10|Theorem §C3.3.10]]).
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.1 (Derivation "Hermiticity of the Dirac matrices", "Consequence for the generators"; Derivation "What replaces unitarity", Step 1; Caution "Spinor boosts are not unitary") · PHY 513 Lecture 8, Part B (slides "The Hermitean Conjugate Spinor", "The Dirac Conjugate Spinor") · PS §3.2, p. 41 ("The boost generators $S^{0i}$ are not Hermitian") and p. 43*

^demo-cb-11-thm-6

> [!proof]- Proof
> **1. Adjoint of a commutator.** $[A, B]^\dagger = (AB - BA)^\dagger = B^\dagger A^\dagger - A^\dagger B^\dagger = [B^\dagger, A^\dagger]$, and the $i$ is conjugated: $S^{\mu\nu\dagger} = -\frac i4[\gamma^{\nu\dagger}, \gamma^{\mu\dagger}]$.
>
> **2. Insert the hypothesis.** With $\gamma^{\mu\dagger} = \gamma^0\gamma^\mu\gamma^0$: $[\gamma^0\gamma^\nu\gamma^0, \gamma^0\gamma^\mu\gamma^0] = \gamma^0\gamma^\nu\gamma^0\gamma^0\gamma^\mu\gamma^0 - \gamma^0\gamma^\mu\gamma^0\gamma^0\gamma^\nu\gamma^0 = \gamma^0[\gamma^\nu, \gamma^\mu]\gamma^0$, using $(\gamma^0)^2 = \mathbb 1$ in the middle of each product. So $S^{\mu\nu\dagger} = -\frac i4\gamma^0[\gamma^\nu, \gamma^\mu]\gamma^0 = \frac i4\gamma^0[\gamma^\mu, \gamma^\nu]\gamma^0 = \gamma^0S^{\mu\nu}\gamma^0$.
>
> **3. The two cases.** $S^{ij} = \frac i2\gamma^i\gamma^j$ ($i \ne j$): moving $\gamma^0$ through two $\gamma$'s gives $(-1)^2$, so $\gamma^0S^{ij} = S^{ij}\gamma^0$ and $S^{ij\dagger} = S^{ij}(\gamma^0)^2 = S^{ij}$. $S^{0i} = \frac i2\gamma^0\gamma^i$: $\gamma^0$ anticommutes with $\gamma^i$ and commutes with itself, so $\gamma^0S^{0i} = -S^{0i}\gamma^0$ and $S^{0i\dagger} = -S^{0i}$.
>
> **4. Part 2.** With only $\omega_{ij} \ne 0$ the exponent is $-iX$ with $X = \frac12\omega_{ij}S^{ij}$ Hermitian: $(e^{-iX})^\dagger = e^{iX} = (e^{-iX})^{-1}$, unitary. With only $\omega_{0i} \ne 0$ the exponent is $-i\omega_{0i}S^{0i}$, Hermitian because $S^{0i}$ is anti-Hermitian; the exponential of a Hermitian matrix is Hermitian with positive eigenvalues $e^\lambda$, and unitary only if all $\lambda = 0$, i.e. $\omega = 0$.
>
> **What the proof shows**
> - $\gamma^0$ turns the adjoint into the inverse: $\Lambda_W(\omega)^\dagger = \gamma^0\Lambda_W(\omega)^{-1}\gamma^0$, so the form $\chi^\dagger\gamma^0\psi$ is invariant where $\chi^\dagger\psi$ is not ([[§CB.5 Hermitian Forms, Signature and Pseudo-Unitary Groups|§CB.5]]; physics: [[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-1|Theorem §C5a.6.1]]).

^demo-cb-11-pf-6

*Uses:* [[Demo §CB.11 Spin(1,3) and the Lorentz Algebra on Spinor Space#^demo-cb-11-def-1|Def. §CB.11.1]], [[Demo §CB.11 Spin(1,3) and the Lorentz Algebra on Spinor Space#^demo-cb-11-def-4|Def. §CB.11.4]], [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-11|Theorem §C5a.1.11]], [[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-3-16|Theorem §CB.3.16]]

> [!remark]- Connections
> - The Clifford relation is the multiplication rule of a "square root of the metric", and the orthogonal algebra follows from it: in every dimension and signature $\frac i4[\gamma, \gamma]$ represents it, with spin ½ for rotations in three dimensions as the case $\gamma^j = i\sigma^j$ — [[§C5.1 Rotations and the Angular-Momentum Commutation Relations#^thm-c5-1-4|QM Theorem §C5.1.4]], [[§B6.1 Spin One-Half and the Pauli Matrices#^thm-b6-1-4|QM Theorem §B6.1.4]].
> - Theorem §CB.11.5 is the Lorentz case of the general fact that the volume element, central in the even subalgebra for even $n$, splits an irreducible Clifford module into two half-spin modules — [[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-19|Theorem §CB.7.19]], [[§CB.8 Complex Clifford Algebras and Clifford Modules|§CB.8]].
> - Theorem §CB.11.6, 2 is the noncompactness of $\mathfrak{so}(1,3)$ seen on four dimensions — [[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-3-16|Theorem §CB.3.16]].
> - **Used in**: Def. §CB.11.1 — [[Demo §C5a.3 The Lorentz Action on Spinor Space (option 1)#^demo-c5a-3-def-1|Def. §C5a.3.1 (demo)]], [[Demo §C5a.3 The Lorentz Action on Spinor Space (option 1)#^demo-c5a-3-thm-1|Theorem §C5a.3.1 (demo)]], [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-2|Theorem §C5a.5.2]], [[§C5a.6 The Dirac Conjugate and the Bilinears#^def-c5a-6-2|Def. §C5a.6.2]], [[§C5a.8 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-8-8|Theorem §C5a.8.8]]; Theorem §CB.11.2 — [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-11|Theorem §C5a.4.11]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^rem-c5a-4-3|§C5a.4, Remark: The lecture's form of the covariance]]; Theorem §CB.11.3 — [[Demo §C5a.3 The Lorentz Action on Spinor Space (option 1)#^demo-c5a-3-def-1|Def. §C5a.3.1 (demo)]], [[§C3.4 How Fields Transform under the Lorentz Group#^cau-c3-4-2|§C3.4, Caution: Two meanings of S^μν]]; Def. §CB.11.4 — [[Demo §C5a.3 The Lorentz Action on Spinor Space (option 1)#^demo-c5a-3-def-1|Def. §C5a.3.1 (demo)]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-9|Theorem §C5a.4.9]]; Theorem §CB.11.5 — [[Demo §C5a.3 The Lorentz Action on Spinor Space (option 1)#^demo-c5a-3-thm-2|Theorem §C5a.3.2 (demo)]], [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-2|Theorem §C5a.5.2]], [[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-9|Theorem §C5a.7.9]]; Theorem §CB.11.6 — [[Demo §C5a.3 The Lorentz Action on Spinor Space (option 1)#^demo-c5a-3-rem-2|Demo §C5a.3, Remark: Spinor boosts are not unitary]], [[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-1|Theorem §C5a.6.1]], [[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-2|Theorem §C5a.6.2]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^ex-c5a-4-2|Example §C5a.4.2]].
