---
type: review
subject: "[[Quantum Field Theory]]"
tags: [quantum-field-theory, phy513, review]
---
↑ [[Quantum Field Theory]] · [[PHY 513 Midterm Review|Midterm Review]] · [[PHY 513 Notes Drill|Notes Drill]]

# PHY 513 Problem-Set Drill (PS1–PS7)

Every problem and part of Problem Sets 1–7, all submitted (Problem Set 7 on 2026-10-13), broken into small questions in order. Statements follow Larsen's problem sets (in the notes' notation where marked); the hints point to the homes in the notes and say, neutrally, how the submitted solution went. The midterm (Friday Oct 16) has one short-response problem "of exactly this type" as Problem Set 7, Problem 1 (Problem Set 7 PDF); the plan is in [[PHY 513 Midterm Review]].

**How to drill.**
1. Read the statement and answer the questions top to bottom on paper, closed book.
2. Tags: **[def]** a definition to state exactly; **[why]** why a step or an approximation holds; **[conv]** a sign or convention check (course vs Peskin–Schroeder vs Yu, [[Larsen PHY 513]]).
3. Tick a question when you can answer it without looking; when all are ticked, redo the whole problem in one go.
4. Open **Hints** only when stuck: the route (technique codes K1–K16, listed at the end), the boxes used, and a note on your submitted solution.

## Problem Set 1 (due Sep 4): Relativistic Invariance

### PS1.1 Index bonanza, part 1: legal and illegal index structures

A sum is implied over a repeated index; two indices contracted this way (one up, one down) form a Lorentz invariant, e.g. $x^2 = x^\mu x_\mu$. Indices that are not contracted indicate how an expression transforms under Lorentz transformations. Determine if the index structures of the expressions below are legal or illegal.

*Parts: (a), (b), (c), (d), (e), (f), (g), (h), (i), (j).*

^ps1-1

> [!tip]- Hint: route for the whole problem
> **Strategy (K2).** In each term list every index with its height and its number of occurrences; a repeated index must appear exactly twice, once up and once down; in an equation the free indices and their heights must agree on both sides.

#### (a)

$a_\mu a_\nu b^{\mu\nu}$.

^ps1-1-a

- [x] Q1 **[def]** State the rules for a legal single term: how often may an index appear, and at which heights?
- [x] Q2 List each index of $a_\mu a_\nu b^{\mu\nu}$ with its height and count. Which are dummies, which are free?
- [x] Q3 Legal or illegal? If legal, what kind of object is it (scalar, vector, covector, which tensor type)?

#### (b)

$a_\mu a_\nu b^{\mu\rho}$.

^ps1-1-b

- [x] Q1 List each index with its height and count.
- [x] Q2 Legal or illegal?
- [x] Q3 If legal, name its free indices with their heights and its tensor type.

#### (c)

$a_\mu a_\nu b^{\mu\rho}a_\rho$.

^ps1-1-c

- [x] Q1 List each index with its height and count.
- [x] Q2 Legal or illegal? If legal, what object is it?
- [x] Q3 **[why]** Write how $b^{\mu\rho}a_\rho$ transforms under $\Lambda$ and show that the $\Lambda$'s carried by $\rho$ cancel. Which property of $\Lambda$ is used?

#### (d)

$a_\mu a_\nu b^{\mu\rho}a_\nu$.

^ps1-1-d

- [x] Q1 Count the occurrences and heights of $\nu$.
- [x] Q2 Legal or illegal? Which rule decides it?
- [x] Q3 **[why]** Write $\sum_\nu a_\nu a_\nu$ in components and compare it with $a^\nu a_\nu$ under a boost along $x^1$. Why is the first not an invariant?

#### (e)

$a_\rho a_\nu b^{\mu\rho}a_\rho$.

^ps1-1-e

- [x] Q1 Count the occurrences and heights of $\rho$.
- [x] Q2 Legal or illegal? Which rule decides it?
- [x] Q3 Rename one index so that the expression becomes legal. What tensor type do you get?

#### (f)

$a_\rho a_\nu b^{\rho\mu} = B_\nu{}^{\mu}$.

^ps1-1-f

- [x] Q1 **[def]** State the extra rule for an equation between two index expressions.
- [x] Q2 List the free indices of the left-hand side with their heights, and those of the right-hand side.
- [x] Q3 Legal or illegal?
- [x] Q4 **[conv]** For a tensor without symmetry, are $B_\nu{}^\mu$ and $B^\mu{}_\nu$ the same object? Does the horizontal order of the slots matter?

#### (g)

$a_\rho a_\nu b^{\rho\mu} = B^{\mu\sigma}{}_{\nu}\,h_\sigma$.

^ps1-1-g

- [x] Q1 What is the status of $\sigma$ on the right-hand side?
- [x] Q2 Compare the free indices and heights of the two sides.
- [x] Q3 Legal or illegal?

#### (h)

$a_\rho a_\nu b^{\rho\mu} = B_\nu{}^{\mu\rho}$.

^ps1-1-h

- [x] Q1 What is the status of $\rho$ on each side?
- [x] Q2 Legal or illegal?
- [x] Q3 **[why]** A free index records a transformation factor $\Lambda$. Why can an index that is summed on one side not be free on the other?

#### (i)

$a_\rho a_\nu b^{\rho\mu} = B^{\mu\nu}$.

^ps1-1-i

- [x] Q1 Compare the heights of $\nu$ on the two sides.
- [x] Q2 Legal or illegal?
- [x] Q3 **[conv]** How would you repair the equation with the metric, and on which side?

#### (j)

$a_\rho a_\nu b^{\rho\mu} = B^{\mu\rho}{}_{\nu}\,z_\rho$.

^ps1-1-j

- [x] Q1 The letter $\rho$ appears on both sides. Is each occurrence a dummy within its own side? Does reusing the letter on both sides cause a problem?
- [x] Q2 Compare the free indices and heights of the two sides.
- [x] Q3 Legal or illegal?

> [!tip]- Hints: definitions, results and your solution for the whole problem
> **Topic and definitions.** T1 index notation. Four-vectors and index positions Definition [[§C1a.5 Vectors, Tensors and Index Notation#^def-c1a-5-1|§C1a.5.1]] Four-Vectors and Index Positions in Natural Units; vectors and covectors through the metric Theorem [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-2|§C1a.5.2]] The Metric Identifies Vectors with Covectors; Lorentz transformation Definition [[§C1a.4 The Lorentz Group#^def-c1a-4-1|§C1a.4.1]] Lorentz Transformation, Active Reading.
>
> **Key results.** [[§C1a.5 Vectors, Tensors and Index Notation#^cau-c1a-5-2|§C1a.5, Caution: Index bookkeeping: legal, illegal, and matrix products]] (home of Problem Set 1, Problems 1–2); a contraction is a plain sum [[§C1a.5 Vectors, Tensors and Index Notation#^cau-c1a-5-1|§C1a.5, Caution: A contraction is a plain sum; the signs live in the components]]; [[§C1a.5 Vectors, Tensors and Index Notation|§C1a.5]] Vectors, Tensors and Index Notation.
>
> **Difficulty 1** (all parts). Submitted solution: opens with the two bookkeeping rules (an index at most twice, once up and once down; equal free indices on both sides of an equation) and gives a one-line reason per part; the verdicts agree with the course solution in all ten parts. The vault's [[§C1a.5 Vectors, Tensors and Index Notation#^cau-c1a-5-2|§C1a.5, Caution: Index bookkeeping: legal, illegal, and matrix products]] is built from these two problems.

### PS1.2 Index bonanza, part 2: rearranging, covariance, relabelling

Individual terms in index notation are numbers, so unlike matrices they commute; index names are arbitrary, so $x^\mu x_\mu$, $x^\rho x_\rho$ and $x_\mu x^\mu$ are the same quantity. The flexibility must be used consistently.

*Parts: (a), (b), (c), (d).*

^ps1-2

> [!tip]- Hint: route for the whole problem
> **Strategy (K2).** Reorder the commuting factors so that each contraction joins the second index of one factor to the first index of the next; rename dummies freely within a term; for symmetric factors, index heights may be swapped and a fully contracted chain is a trace.

#### (a)

Rearrange the terms so the expression is equivalent to matrix multiplication: $C_{\sigma\lambda}B^{\nu}{}_{\rho}B^{\mu}{}_{\nu}D^{\rho\sigma}$.

^ps1-2-a

- [x] Q1 **[def]** When is an index expression a matrix product: which index of one factor must be contracted with which index of the next?
- [x] Q2 Identify the free indices with their heights. Which factor must stand first and which last?
- [x] Q3 Chain the remaining factors through the dummies and write the result as one matrix element.
- [x] Q4 **[why]** Why is the reordering allowed for the components, although the matrices themselves do not commute?

#### (b)

Place indices on $B$ such that the equation $A^{\mu}{}_{\nu}\eta^{\nu\rho}A^{\alpha}{}_{\mu} = B$ is covariant (the Lorentz transformation of both sides is identical).

^ps1-2-b

- [x] Q1 Which indices on the left are contracted and which are free, at which heights?
- [x] Q2 Write the left-hand side as a matrix product including the metric, and read off the indices $B$ must carry.
- [x] Q3 **[why]** Why do equal free indices at equal heights make the two sides transform identically?
- [x] Q4 **[why]** Does the order of the two indices on $B$ matter? Test whether $(AA\eta^{-1})^{\alpha\rho}$ is symmetric for a general matrix $A$.

#### (c)

Relabel indices to show that the two expressions are the same: $A^{\rho}{}_{\mu}B^{\nu\lambda}D^{\mu}{}_{\nu}C_{\lambda\rho} \overset{?}{=} C_{\lambda}{}^{\sigma}D^{\rho}{}_{\mu}A_{\sigma\rho}B^{\mu\lambda}$.

^ps1-2-c

- [x] Q1 Reorder each side so that contracted indices are neighbours. Which cyclic chain of factors appears on each side?
- [x] Q2 Find a renaming of the dummies of the right-hand side that maps it onto the left-hand side.
- [x] Q3 **[why]** Why may a contracted pair exchange heights, $C_{\lambda}{}^{\rho}A_{\rho\mu} = C_{\lambda\rho}A^{\rho}{}_{\mu}$?
- [x] Q4 Write both sides as the trace of one product of matrices.

#### (d)

If $A$, $B$, $C$, $D$ are symmetric matrices, which of the following three expressions are identical? $B^{\lambda}{}_{\rho}D^{\alpha}{}_{\mu}A^{\mu}{}_{\lambda}C^{\rho}{}_{\alpha}$, $\ A^{\mu}{}_{\lambda}D^{\alpha}{}_{\mu}B^{\rho}{}_{\alpha}C^{\lambda}{}_{\rho}$, $\ B^{\alpha}{}_{\mu}D^{\lambda}{}_{\rho}A^{\mu}{}_{\lambda}C^{\rho}{}_{\alpha}$.

^ps1-2-d

- [x] Q1 **[def]** What does "symmetric" mean for a tensor with indices $T_{\mu\nu}$, and what does it allow for $T^{\mu}{}_{\nu}$ versus $T_{\nu}{}^{\mu}$?
- [x] Q2 Write each expression as the trace of a product, using cyclicity to put $A$ first.
- [x] Q3 For general matrices, are the three traces equal?
- [x] Q4 Using $\operatorname{tr}M = \operatorname{tr}M^{\mathsf T}$ and the symmetry of each factor, decide which cyclic orders become equal.
- [x] Q5 **[why]** Transposing a product reverses the cyclic order. Why does that identity need every factor to be symmetric?

> [!tip]- Hints: definitions, results and your solution for the whole problem
> **Topic and definitions.** T1 index notation. Four-vectors and index positions Definition [[§C1a.5 Vectors, Tensors and Index Notation#^def-c1a-5-1|§C1a.5.1]] Four-Vectors and Index Positions in Natural Units; metric identification Theorem [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-2|§C1a.5.2]] The Metric Identifies Vectors with Covectors; Lorentz transformation Definition [[§C1a.4 The Lorentz Group#^def-c1a-4-1|§C1a.4.1]] Lorentz Transformation, Active Reading.
>
> **Key results.** [[§C1a.5 Vectors, Tensors and Index Notation#^cau-c1a-5-2|§C1a.5, Caution: Index bookkeeping: legal, illegal, and matrix products]] (matrix products, dummy renaming; home of Problem Set 1, Problems 1–2); [[§C1a.5 Vectors, Tensors and Index Notation|§C1a.5]] Vectors, Tensors and Index Notation.
>
> **Difficulty 1** (all parts). Submitted solution: (a) reorders the factors as in the course solution; (b) gives $B^{\alpha\rho}$; the course solution adds that either index order is correct because $A^2$ is symmetric "even if $A$ does not itself have any particular symmetry", which fails for a general $A$ (flagged here, not in ERRATA; it does not affect the answer $B^{\alpha\rho}$); (c) reorders both sides into one chain and renames three dummies, the course solution writes both as one trace; (d) argues by which factor is contracted with which, the course solution by traces and the transpose; same conclusion.

### PS1.3 The Levi-Civita symbol

The condition $\eta_{\mu\nu}\Lambda^{\mu}{}_{\rho}\Lambda^{\nu}{}_{\sigma} = \eta_{\rho\sigma}$, in matrix form $\Lambda^{\mathsf T}\eta\Lambda = \eta$, says that $\eta_{\mu\nu}$ is an invariant tensor of $O(1,3)$; taking the determinant gives $(\det\Lambda)^2 = 1$. Proper Lorentz transformations form $SO(1,3)$, $\det\Lambda = +1$. The invariant object associated with $\det\Lambda = +1$ is the Levi-Civita symbol $\epsilon^{\mu\nu\rho\sigma}$, totally antisymmetric, equal to $+1$ if $(\mu\nu\rho\sigma)$ is an even permutation of $(0123)$, $-1$ if odd, $0$ otherwise (an even/odd permutation needs an even/odd number of exchanges of two indices).

*Parts: (a), (b).*

^ps1-3

#### (a)

What are the values of $\epsilon^{0123}$, $\epsilon^{1230}$ and $\epsilon^{1213}$?

^ps1-3-a

- [x] Q1 **[def]** Define $\epsilon^{\mu\nu\rho\sigma}$ and an even or odd permutation.
- [x] Q2 Count the exchanges that take $(0123)$ to $(1230)$, and give the sign.
- [x] Q3 Why does $(1213)$ give zero? Name the property of $\epsilon$ that forces it.
- [x] Q4 **[conv]** With the course's $\epsilon^{0123} = +1$, what is $\epsilon_{0123}$? Which sign do Peskin–Schroeder use, and which quantities change sign between the two conventions?

> [!tip]- Hint (a): route
> **Strategy (K2).** Count transpositions; a repeated index gives zero.

#### (b)

Just as $p^2 = p^\mu p_\mu$ is invariant thanks to $\Lambda^{\mathsf T}\eta\Lambda = \eta$, $\epsilon^{\mu\nu\rho\sigma}p_{1\mu}p_{2\nu}p_{3\rho}p_{4\sigma}$ is invariant under proper Lorentz transformations $SO(1,3)$ ($p_{i\mu}$ four distinct 4-momenta, $i = 1,\dots,4$). Show that $\epsilon^{\mu\nu\rho\sigma}p_{1\mu}p_{2\nu}p_{3\rho}p_{4\sigma} = 0$ if the four momenta satisfy $\sum_{i=1}^4 p_i^\mu = 0$.

^ps1-3-b

- [x] Q1 **[why]** Why is the contraction invariant under $SO(1,3)$ but not under all of $O(1,3)$? Which identity relating $\epsilon$ and $\det\Lambda$ do you use?
- [x] Q2 Show that conservation also holds with lower indices.
- [x] Q3 Substitute $p_4 = -(p_1 + p_2 + p_3)$ and write the three resulting terms.
- [x] Q4 Prove that a tensor antisymmetric in a pair of indices contracted with one symmetric in the same pair gives zero, and apply it to each term.
- [x] Q5 Second route: identify the contraction with $\pm$ a $4\times4$ determinant whose columns are the four momenta. Which column operation shows that it vanishes?
- [x] Q6 **[why]** For four arbitrary vectors, when does the contraction vanish?

> [!tip]- Hint (b): route
> **Strategy (K2).** Eliminate $p_4$ by conservation and contract a symmetric pair with an antisymmetric symbol; or read the contraction as a determinant with the momenta as columns.

> [!tip]- Hints: definitions, results and your solution for the whole problem
> **Topic and definitions.** T1. Levi-Civita symbol Definition [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-16|§CB.0.16]] The Levi-Civita Symbol; Lorentz transformation Definition [[§C1a.4 The Lorentz Group#^def-c1a-4-1|§C1a.4.1]] Lorentz Transformation, Active Reading; the sign convention [[§C1a.5 Vectors, Tensors and Index Notation#^cau-c1a-5-5|§C1a.5, Caution: The sign of ε⁰¹²³: these notes versus Peskin–Schroeder]].
>
> **Key results.** Example [[§C1a.5 Vectors, Tensors and Index Notation#^ex-c1a-5-1|§C1a.5.1]] Momentum Conservation Kills ε p₁p₂p₃p₄ (home of 3(b)); the symbol and the determinant Theorem [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-4|§C1a.5.4]] The Levi-Civita Symbol and the Determinant; contraction identities Theorem [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-3|§C1a.5.3]] Contraction Identities of the Levi-Civita Symbol; components version Theorem [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-18|§CB.0.18]] The Levi-Civita Symbol and the Determinant.
>
> **Difficulty** (a) 1, (b) 1. Submitted solution: (a) counts three exchanges; (b) expands the sum term by term into $2\times2$, then $3\times3$ cofactor expansions, identifies the $4\times4$ determinant of the momenta (with the particle label in bold to keep it apart from the component index), and adds columns 1–3 to column 4; long. The vault's Example [[§C1a.5 Vectors, Tensors and Index Notation#^ex-c1a-5-1|§C1a.5.1]] Momentum Conservation Kills ε p₁p₂p₃p₄ takes the same determinant route through Theorem [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-4|§C1a.5.4]] The Levi-Civita Symbol and the Determinant, 4; the course solution uses the symmetric–antisymmetric argument.

### PS1.4 Relativistic kinematics and natural units: $e^+e^- \to \gamma\gamma$

In the laboratory frame a positron of energy $E$ annihilates a stationary electron, $e^+ + e^- \to \gamma + \gamma$. The energy of the photons in the centre-of-mass frame (the frame where the total momentum of both particles vanishes) is, in natural units $c = \hbar = 1$, $E_{\rm CM} = \sqrt{2m_e(E + m_e)}$, with $m_e$ the electron (= positron) mass.

*Parts: (a), (b), (c), (d).*

^ps1-4

#### (a)

Derive the formula for $E_{\rm CM}$, setting $c = 1$ from the start. (Hint: $p_\mu q^\mu$ is Lorentz invariant.)

^ps1-4-a

- [x] Q1 **[def]** Define the centre-of-mass frame. Write the lab four-momenta of the positron and the electron, with the mass-shell condition.
- [x] Q2 Which invariant equals $E_{\rm CM}^2$, and why is it the same before and after the annihilation?
- [x] Q3 Evaluate it in the lab frame.
- [x] Q4 Evaluate it in the centre-of-mass frame and equate.
- [x] Q5 **[why]** Why may the invariant be evaluated with the initial particles in one frame and read as the photons' energy in another?

> [!tip]- Hint (a): route
> **Strategy (K1).** The square of the total four-momentum, evaluated in the lab and in the centre-of-mass frame.

#### (b)

Put back the missing factors of $c$ in the result of (a).

^ps1-4-b

- [ ] Q1 **[def]** Which combination of $m_e$ and $c$ is an energy? What is the type of $E_{\rm CM}$?
- [ ] Q2 Restore $c$ in each of the two terms under the root separately.
- [ ] Q3 **[why]** Why must the terms of a sum be restored one at a time rather than the formula as a whole?
- [ ] Q4 Check your formula at threshold, $E \to m_ec^2$.

> [!tip]- Hint (b): route
> **Strategy (K8).** Every term under the square root must become an energy squared.

#### (c)

What is the energy of each photon in the centre-of-mass frame?

^ps1-4-c

- [x] Q1 What does the definition of the centre-of-mass frame say about the two photon three-momenta?
- [x] Q2 **[why]** Why does masslessness then force equal energies?
- [x] Q3 Express $E_\gamma$ in terms of $E$ and $m_e$.

> [!tip]- Hint (c): route
> **Strategy (K1).** Back-to-back massless momenta.

#### (d)

Suppose $E = 50$ MeV. What length scales will typically be probed by the photons produced?

^ps1-4-d

- [ ] Q1 Compute $E_{\rm CM}$ and $E_\gamma$ numerically ($m_e = 0.511$ MeV).
- [ ] Q2 **[def]** Which length does a photon of energy $E_\gamma$ resolve: the wavelength $2\pi\hbar c/E_\gamma$ or the reduced wavelength $\hbar c/E_\gamma$? Compute both.
- [ ] Q3 **[conv]** Is the factor $2\pi$ between the two physics or convention? Compare the scale with the size of a nucleon.

> [!tip]- Hint (d): route
> **Strategy (K8).** Convert an energy to a length with $\hbar c \simeq 197.3$ MeV fm.

> [!tip]- Hints: definitions, results and your solution for the whole problem
> **Topic and definitions.** T1 natural units and invariants. Natural units Definition [[§C1a.2 Natural Units and Dimensional Analysis#^def-c1a-2-1|§C1a.2.1]] Natural Units; mass dimension Definition [[§C1a.2 Natural Units and Dimensional Analysis#^def-c1a-2-2|§C1a.2.2]] Mass Dimension; four-momentum and mass shell Definition [[§C1a.5 Vectors, Tensors and Index Notation#^def-c1a-5-1|§C1a.5.1]] Four-Vectors and Index Positions in Natural Units.
>
> **Key results.** Example [[§C1a.2 Natural Units and Dimensional Analysis#^ex-c1a-2-1|§C1a.2.1]] The Annihilation Photons (home of 4(a)–(d)); compute invariants [[§C1a.5 Vectors, Tensors and Index Notation#^rem-c1a-5-1|§C1a.5, Remark: Compute invariants, not transformations]]; rules of dimensional counting Theorem [[§C1a.2 Natural Units and Dimensional Analysis#^thm-c1a-2-3|§C1a.2.3]] Rules of Dimensional Counting; the exponent rule Theorem [[§C1a.2 Natural Units and Dimensional Analysis#^thm-c1a-2-1|§C1a.2.1]] The Exponent Rule; [[§C1a.2 Natural Units and Dimensional Analysis#^cau-c1a-2-1|§C1a.2, Caution: One number, several readings]]; [[P4 Restoring ħ and c#^p4-5|P4, step 5]].
>
> **Difficulty 1** (all parts). Submitted solution: (a)–(c) as the course solution; (d) quotes the wavelength $\lambda = 2\pi\hbar c/E_\gamma$, the course solution the reduced length $\hbar c/E_\gamma$; the vault's Example [[§C1a.2 Natural Units and Dimensional Analysis#^ex-c1a-2-1|§C1a.2.1]] The Annihilation Photons, Step 3, records both and calls the $2\pi$ a convention.

### PS1.5 Relativistic kinematics of two-body scattering

A particle of mass $m_2$ is at rest in the laboratory. It is struck by a particle of mass $m_1$, momentum $p_{\rm lab}$ and total energy $E_{\rm lab}$; the two are transformed into particles of masses $m_3$, $m_4$ moving at angles $\theta_3$, $\theta_4$ with respect to particle 1. In the centre-of-mass system (cms, total momentum zero) the initial momenta are $\vec p\,'$ and $-\vec p\,'$, the final momenta $\vec q\,'$ and $-\vec q\,'$, and particle 3 moves at angle $\theta'$ with respect to particle 1.

*Parts: (a), (b), (c), (d), (e), (f).*

^ps1-5

#### (a)

Sketch the kinematic configuration in the laboratory frame and in the cms.

^ps1-5-a

- [ ] Q1 **[def]** Define the cms.
- [ ] Q2 Sketch the lab frame: what is at rest, and from which axis are $\theta_3$, $\theta_4$ measured?
- [ ] Q3 Sketch the cms: which momenta are back to back, and where is $\theta'$?
- [ ] Q4 **[why]** Why is the cms obtained from the lab by a boost along the beam axis?

#### (b)

Use invariant scalar products between four-vectors to show that the total cms energy satisfies $E_{\rm cms}^2 = m_1^2 + m_2^2 + 2m_2E_{\rm lab}$.

^ps1-5-b

- [ ] Q1 Write the lab four-momenta $p_1$, $p_2$.
- [ ] Q2 **[def]** Define $s$. Why does it equal $E_{\rm cms}^2$?
- [ ] Q3 Expand $(p_1 + p_2)^2 = p_1^2 + p_2^2 + 2p_1\cdot p_2$ and evaluate each term in the lab.

> [!tip]- Hint (b): route
> **Strategy (K1).** $s = (p_1 + p_2)^2$ in the lab and in the cms.

#### (c)

Use (b) to explain why, to explore high-energy processes, it is much more efficient to collide beams in their cms than to expose a stationary target to a high-energy beam.

^ps1-5-c

- [ ] Q1 How does $E_{\rm cms}$ scale with $E_{\rm lab}$ when $E_{\rm lab} \gg m_1, m_2$?
- [ ] Q2 For two equal beams colliding head-on, what is $E_{\rm cms}$ in terms of the beam energy?
- [ ] Q3 **[why]** In the fixed-target case, where does the rest of the lab energy go?
- [ ] Q4 **[why]** Give practical reasons why fixed-target experiments are still used.

#### (d)

Show that the 3-momentum of the beam particle in the cms is $p' = m_2p_{\rm lab}/E_{\rm cms}$, $p' = \lvert\vec p\,'\rvert$. (Warning: messy head-on; consider the tensor $T_{\mu\nu} \equiv \epsilon_{\mu\nu\rho\sigma}(p_1 + p_2)^\sigma(p_1 - p_2)^\rho$ in the two frames.)

^ps1-5-d

- [ ] Q1 **[def]** Write the transformation law of $T_{\mu\nu}$ under $\Lambda$.
- [ ] Q2 For a boost along $x^1$, which components of $\Lambda$ are trivial, and which components of $T_{\mu\nu}$ are therefore unchanged?
- [ ] Q3 Write $T_{23}$ explicitly: which components of $\epsilon_{23\rho\sigma}$ survive?
- [ ] Q4 Evaluate $T_{23}$ in the lab.
- [ ] Q5 Evaluate $T_{23}$ in the cms and equate.
- [ ] Q6 **[conv]** How does the sign of $\epsilon_{2301}$ depend on the convention for $\epsilon^{0123}$, and why does it drop out of the result?

> [!tip]- Hint (d): route
> **Strategy (K1, K2).** A tensor component transverse to the boost is the same in both frames; evaluate it in each and equate.

#### (e)

⏸ **Skipped for now — to be redone.** Define the four-momentum transfer $q = p_1 - p_3$. For elastic scattering ($m_1 = m_3$, $m_2 = m_4$) show that $t \equiv q^2 = -2m_4(E_4 - m_4)$, where $E_4$ is the final lab energy of the particle initially at rest.

^ps1-5-e

- [ ] Q1 **[def]** Use conservation to write $q$ as a difference involving $p_2$ and $p_4$.
- [ ] Q2 Expand $q^2$ and identify the squares as masses.
- [ ] Q3 Evaluate $p_2\cdot p_4$ in the lab.
- [ ] Q4 Impose the elastic masses.
- [ ] Q5 **[why]** Why is $q = p_4 - p_2$ the better form here than $p_1 - p_3$?

> [!tip]- Hint (e): route
> **Strategy (K1).** Rewrite $q$ with conservation so that the target appears, then evaluate in the lab.

#### (f)

⏸ **Skipped for now — to be redone.** Show that for elastic scattering $s \equiv (p_1 + p_2)^2 = E_{\rm cms}^2$ and $t = -4p'^2\sin^2(\theta'/2)$, with $p'$ the cms momentum and $\theta'$ the cms scattering angle.

^ps1-5-f

- [ ] Q1 Evaluate $s$ in the cms.
- [ ] Q2 Write $t$ in the cms in terms of $E_1'$, $E_3'$, $p'$, $q'$ and $\theta'$.
- [ ] Q3 Show $\lvert\vec q\,'\rvert = \lvert\vec p\,'\rvert$ for elastic scattering (energy conservation in the cms and monotonicity).
- [ ] Q4 Conclude $E_1' = E_3'$ and simplify $t$ with a half-angle identity.
- [ ] Q5 **[why]** What sign does $t$ have for physical scattering, and when does it vanish?

> [!tip]- Hint (f): route
> **Strategy (K1).** Evaluate both invariants in the cms; elastic kinematics fixes $\lvert\vec q\,'\rvert = \lvert\vec p\,'\rvert$.

> [!tip]- Hints: definitions, results and your solution for the whole problem
> **Topic and definitions.** T1 invariants. Four-momentum Definition [[§C1a.5 Vectors, Tensors and Index Notation#^def-c1a-5-1|§C1a.5.1]] Four-Vectors and Index Positions in Natural Units; Mandelstam variables Definition [[§C1a.5 Vectors, Tensors and Index Notation#^def-c1a-5-2|§C1a.5.2]] Mandelstam Variables; Lorentz transformation Definition [[§C1a.4 The Lorentz Group#^def-c1a-4-1|§C1a.4.1]] Lorentz Transformation, Active Reading; Levi-Civita symbol Definition [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-16|§CB.0.16]] The Levi-Civita Symbol.
>
> **Key results.** Definition [[§C1a.5 Vectors, Tensors and Index Notation#^def-c1a-5-2|§C1a.5.2]] Mandelstam Variables (Problem 5); Theorem [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-1|§C1a.5.1]] The Mandelstam Sum Rule and the Momentum Transfer (home of 5(e)–(f)); Example [[§C1a.5 Vectors, Tensors and Index Notation#^ex-c1a-5-2|§C1a.5.2]] The Centre-of-Mass Momentum from a Transverse Component (home of 5(d)); [[§C1a.5 Vectors, Tensors and Index Notation#^rem-c1a-5-1|§C1a.5, Remark: Compute invariants, not transformations]] (5(b)); Theorem [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-4|§C1a.5.4]] The Levi-Civita Symbol and the Determinant; [[§C1a.5 Vectors, Tensors and Index Notation#^cau-c1a-5-5|§C1a.5, Caution: The sign of ε⁰¹²³: these notes versus Peskin–Schroeder]].
>
> **Difficulty** (a) 1, (b) 1, (c) 1, (d) 2, (e) 1, (f) 2. Submitted solution: (b) the total-momentum square in two frames; (c) the $\sqrt{E_{\rm lab}}$ growth and the head-on comparison (the course solution adds three practical reasons for fixed targets); (d) a boost along $x^1$ and $T_{23}$ with $\epsilon_{2301} = +1$, noting that the convention only flips a common sign; the vault's Example [[§C1a.5 Vectors, Tensors and Index Notation#^ex-c1a-5-2|§C1a.5.2]] The Centre-of-Mass Momentum from a Transverse Component uses $\epsilon_{0123} = -1$ and gets the opposite sign of $T_{23}$, the same $p'$; the course solution uses a $z$-boost and $T_{xy}$; (f) proves $p' = q'$ by strict monotonicity of $\sqrt{x + m_1^2} + \sqrt{x + m_2^2}$, which the course solution states without proof.

### PS1.6 Derivatives with four-vectors

⏸ **Skipped for now — to be redone.** $\rho = x_\mu x^\mu$ is a radial coordinate on spacetime (a length squared; do not also use $\rho$ as a dummy index). Notation: $\partial_\mu = \partial/\partial x^\mu$, $\Box = \partial_\mu\partial^\mu$.

*Parts: (a), (b), (c), (d), (e), (f).*

^ps1-6

> [!tip]- Hint: route for the whole problem
> **Strategy (K2).** Rename the dummy in $\rho$, then product and chain rules with $\partial_\mu x^\nu = \delta^\nu{}_\mu$.

#### (a)

Compute $\partial_\mu\rho$.

^ps1-6-a

- [ ] Q1 **[def]** What is $\partial_\mu x^\nu$? And $\partial_\mu x_\nu$?
- [ ] Q2 Rename the dummy in $\rho$ and apply the product rule.
- [ ] Q3 **[why]** What goes wrong if you differentiate $x_\mu x^\mu$ with $\partial_\mu$ without renaming?

#### (b)

Compute $\partial_\mu\partial_\nu\rho$.

^ps1-6-b

- [ ] Q1 Differentiate the result of (a) once more.
- [ ] Q2 Express $\partial_\mu x_\nu$ through the metric.
- [ ] Q3 **[why]** The result must be symmetric in $\mu\nu$. Why, and is it?

#### (c)

Compute $\Box\rho$.

^ps1-6-c

- [ ] Q1 Contract the result of (b) with $g^{\mu\nu}$.
- [ ] Q2 **[def]** What is $\delta^\nu{}_\nu$ in $d$ spacetime dimensions?
- [ ] Q3 **[conv]** Which symbols for the d'Alembertian do the lectures, Peskin–Schroeder and the vault use?

#### (d)

Compute $\Box^2\rho^2$.

^ps1-6-d

- [ ] Q1 Compute $\partial_\mu\rho^2$ with the chain rule.
- [ ] Q2 Compute $\Box\rho^2$ with the product rule. Which terms appear?
- [ ] Q3 Apply $\Box$ once more.
- [ ] Q4 Derive the general formula for $\Box f(\rho)$ in terms of $f'$ and $f''$, and check (c) and (d) against it.

#### (e)

Compute $\partial_\sigma\bigl(x^\mu\partial_\mu f(\rho)\bigr)$ for any function $f(\rho)$.

^ps1-6-e

- [ ] Q1 Compute $\partial_\mu f(\rho)$.
- [ ] Q2 Simplify $x^\mu\partial_\mu f$ in terms of $\rho$ and $f'$.
- [ ] Q3 Apply $\partial_\sigma$.
- [ ] Q4 **[why]** Compare the route "product rule on $x^\mu\partial_\mu f$" with "simplify first, then differentiate": do the two forms agree?

#### (f)

Show that $f(\rho) = c_1/\rho + c_2$ solves $\Box f = 0$ for $\rho \ne 0$.

^ps1-6-f

- [ ] Q1 Compute $\partial_\mu(1/\rho)$.
- [ ] Q2 Compute $\Box(1/\rho)$ with the product rule.
- [ ] Q3 **[why]** Why is $\rho \ne 0$ needed? Is $\Box(1/x^2)$ zero as a distribution, and where would a source sit?
- [ ] Q4 Using the formula of (d), Q4, show that these are the only functions of $\rho$ alone with $\Box f = 0$ away from $\rho = 0$.

> [!tip]- Hints: definitions, results and your solution for the whole problem
> **Topic and definitions.** T1 index calculus. Four-vectors and index positions Definition [[§C1a.5 Vectors, Tensors and Index Notation#^def-c1a-5-1|§C1a.5.1]] Four-Vectors and Index Positions in Natural Units; names for the d'Alembertian [[§C1a.5 Vectors, Tensors and Index Notation#^cau-c1a-5-8|§C1a.5, Caution: Names for the d'Alembertian]].
>
> **Key results.** Theorem [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-8|§C1a.5.8]] The d'Alembertian of a Function of x² (home of Problem 6); Theorem [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-7|§C1a.5.7]] Basic Derivative Identities; [[§C1a.5 Vectors, Tensors and Index Notation#^cau-c1a-5-7|§C1a.5, Caution: The Hessian is not the wave operator]]; [[§C1a.5 Vectors, Tensors and Index Notation#^rem-c1a-5-3|§C1a.5, Remark: In what sense 1/x² is harmonic, and where the source sits]] (6(f)); [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^cau-c1b-2-3|§C1b.2, Caution: Rename the dummy index before differentiating]].
>
> **Difficulty 1** (all parts). Submitted solution: renames the dummy once at the start and uses the product rule throughout; (d) expands the inner $\Box(\rho\rho)$ term by term; (e) gives $4x_\sigma(f' + \rho f'')$, the course solution the same as $4x_\sigma\,d(\rho f')/d\rho$; (f) does not mention the distributional source at $\rho = 0$ that the course solution notes; the vault has it in [[§C1a.5 Vectors, Tensors and Index Notation#^rem-c1a-5-3|§C1a.5, Remark: In what sense 1/x² is harmonic, and where the source sits]].

## Problem Set 2 (due Sep 11): Relativistic Field Theory

### PS2.1 The dilaton theory

Consider the 4-dimensional Lagrangian $\mathcal L = -f^2e^{-2\tau}(\partial\tau)^2$ (the common, slightly sloppy terminology: "Lagrangian" for the Lagrangian density; $(\partial\tau)^2 = \partial^\mu\tau\,\partial_\mu\tau$).

*Parts: (a), (b).*

^ps2-1

#### (a)

Compute the mass dimension of the dilaton $\tau$ and of the constant $f$.

^ps2-1-a

- [ ] Q1 **[def]** Define the mass dimension. Why is $[\mathcal L] = 4$ in four dimensions?
- [ ] Q2 **[why]** Why must $\tau$ be dimensionless?
- [ ] Q3 Find $[\partial_\mu\tau]$ and $[(\partial\tau)^2]$.
- [ ] Q4 Solve for $[f]$.
- [ ] Q5 **[conv]** With the metric $(+,-,-,-)$, does $-f^2e^{-2\tau}(\partial\tau)^2$ have the sign of a standard kinetic term? Does the overall sign affect the field equation of (b)?

> [!tip]- Hint (a): route
> **Strategy (K8).** A field in an exponent is dimensionless; $[\mathcal L] = 4$ fixes the rest.

#### (b)

Use the Euler–Lagrange equation to show that the EOM for $\tau$ is $\Box\tau = +(\partial\tau)^2$.

^ps2-1-b

- [ ] Q1 **[def]** State the Euler–Lagrange equation for one field.
- [ ] Q2 Compute $\partial\mathcal L/\partial(\partial_\mu\tau)$. Why do both factors of $(\partial\tau)^2$ contribute?
- [ ] Q3 Take the divergence: where does the product rule act on $e^{-2\tau}$?
- [ ] Q4 Compute $\partial\mathcal L/\partial\tau$.
- [ ] Q5 Equate and simplify. Why may you divide by $f^2e^{-2\tau}$?
- [ ] Q6 **[why]** Two terms proportional to $(\partial\tau)^2$ meet in the final equation. Where does each come from, and with which relative sign?

> [!tip]- Hint (b): route
> **Strategy (K2).** Rename the dummy, differentiate both factors of $(\partial\tau)^2$, and keep the derivative of the exponential.

> [!tip]- Hints: definitions, results and your solution for the whole problem
> **Topic and definitions.** T3. Mass dimension Definition [[§C1a.2 Natural Units and Dimensional Analysis#^def-c1a-2-2|§C1a.2.2]] Mass Dimension; Lagrangian density Definition [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^def-c1b-2-1|§C1b.2.1]] Lagrangian Density; [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^cau-c1b-2-1|§C1b.2, Caution: Action, Lagrangian, Lagrangian density]].
>
> **Key results.** Example [[§C1b.3 Mass Dimension, Locality and Power Counting#^ex-c1b-3-1|§C1b.3.1]] A Field in an Exponent: the Dilaton (home of 1(a)); Example [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^ex-c1b-2-1|§C1b.2.1]] A Nonlinear Field Equation: the Dilaton (home of 1(b)); the action is dimensionless Theorem [[§C1b.3 Mass Dimension, Locality and Power Counting#^thm-c1b-3-1|§C1b.3.1]] The Action Is Dimensionless; counting rules Theorem [[§C1a.2 Natural Units and Dimensional Analysis#^thm-c1a-2-3|§C1a.2.3]] Rules of Dimensional Counting; Euler–Lagrange equations Theorem [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-4|§C1b.2.4]] Euler–Lagrange Equations for Fields; [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^cau-c1b-2-3|§C1b.2, Caution: Rename the dummy index before differentiating]]; Theorem [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-10|§C1a.5.10]] Derivatives with Respect to a Four-Vector.
>
> **Difficulty** (a) 1, (b) 1. Submitted solution: (a) argues from the power series of $e^{-2\tau}$; (b) writes $\partial_\mu\tau = a_\mu$ and differentiates through $g^{\nu\gamma}$; agrees with the course solution. ERRATA notes that the sheet's sign of $\mathcal L$ is the mostly-plus one, with no effect on the equation.

### PS2.2 Two scalar fields without the canonical ½

Two scalar fields with $\mathcal L = \partial_\mu\phi_1\partial^\mu\phi_1 + \partial_\mu\phi_2\partial^\mu\phi_2 - m^2\phi_1^2 - \mu\,\phi_1\phi_2^2 - \lambda\,\phi_1^2\phi_2^2$. (The standard, "canonical", kinetic term is $\frac12\partial_\mu\phi\partial^\mu\phi$; here there is no $\frac12$, so unusual factors of $\frac12$ and $2$ may appear.)

*Parts: (a), (b), (c), (d).*

^ps2-2

#### (a)

Use the Euler–Lagrange equations to find the equations of motion for $\phi_1$ and $\phi_2$.

^ps2-2-a

- [ ] Q1 **[def]** Write the Euler–Lagrange equation for $\phi_i$.
- [ ] Q2 Compute $\partial\mathcal L/\partial(\partial_\mu\phi_i)$ for a kinetic term without $\frac12$.
- [ ] Q3 Compute $\partial\mathcal L/\partial\phi_1$ and $\partial\mathcal L/\partial\phi_2$: which potential terms contribute to each?
- [ ] Q4 Assemble both equations and divide by the common factor. Which coefficient ends up fractional, and why?
- [ ] Q5 **[why]** Rescale to canonically normalised fields $\phi_i = \chi_i/\sqrt2$. What are the mass and the couplings in the canonical form?

> [!tip]- Hint (a): route
> **Strategy (K2).** One Euler–Lagrange equation per field; the kinetic term without $\frac12$ doubles the derivative term.

#### (b)

Calculate the conjugate momenta for $\phi_1$ and $\phi_2$.

^ps2-2-b

- [ ] Q1 **[def]** Define the momentum density conjugate to $\phi_i$.
- [ ] Q2 Write the kinetic terms in time and space components.
- [ ] Q3 Compute $\pi_1$ and $\pi_2$.
- [ ] Q4 **[conv]** Compare with the canonical normalisation, where $\pi = \dot\phi$. What changes?

#### (c)

Construct the Hamiltonian density $\mathcal H$.

^ps2-2-c

- [ ] Q1 **[def]** State the Legendre transform for two fields.
- [ ] Q2 Compute $\mathcal H$ in terms of the velocities.
- [ ] Q3 Eliminate the velocities in favour of $\pi_1$, $\pi_2$.
- [ ] Q4 **[why]** Why must the Hamiltonian contain no time derivatives?

> [!tip]- Hint (c): route
> **Strategy.** Legendre transform, then eliminate every velocity.

#### (d)

Compute the mass dimension of $\{m^2, \mu, \lambda\}$ in natural units.

^ps2-2-d

- [ ] Q1 **[def]** Why is $[\mathcal L] = 4$, and $[\partial_\mu] = 1$?
- [ ] Q2 Find $[\phi_i]$ from the kinetic term. Does the missing $\frac12$ change it?
- [ ] Q3 Find $[m^2]$, $[\mu]$, $[\lambda]$.
- [ ] Q4 **[why]** Classify each term as relevant, marginal or irrelevant.

> [!tip]- Hint (d): route
> **Strategy (K8).** $[\mathcal L] = 4$; the kinetic term fixes $[\phi_i]$; each term then fixes its coupling.

> [!tip]- Hints: definitions, results and your solution for the whole problem
> **Topic and definitions.** T3. Euler–Lagrange equations Theorem [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-4|§C1b.2.4]] Euler–Lagrange Equations for Fields; canonical momentum density Definition [[§C1b.4 Hamiltonian Field Theory#^def-c1b-4-1|§C1b.4.1]] Canonical Momentum Density; Hamiltonian density Definition [[§C1b.4 Hamiltonian Field Theory#^def-c1b-4-2|§C1b.4.2]] Hamiltonian Density and Hamiltonian (Legendre Transform); mass dimension Definition [[§C1a.2 Natural Units and Dimensional Analysis#^def-c1a-2-2|§C1a.2.2]] Mass Dimension.
>
> **Key results.** [[§C1b.4 Hamiltonian Field Theory#^rem-c1b-4-2|§C1b.4, Remark: Several fields, and a non-canonical normalization]] (home of 2(b)–(c)); [[§C1b.4 Hamiltonian Field Theory#^cau-c1b-4-1|§C1b.4, Caution: What the conjugate momentum is not]] (2(c)); Theorem [[§C1b.3 Mass Dimension, Locality and Power Counting#^thm-c1b-3-2|§C1b.3.2]] Mass Dimension of Fields, Theorem [[§C1b.3 Mass Dimension, Locality and Power Counting#^thm-c1b-3-3|§C1b.3.3]] Mass Dimension of Couplings (2(d)); Theorem [[§C1b.4 Hamiltonian Field Theory#^thm-c1b-4-2|§C1b.4.2]] Hamiltonian Density of the Free Real Field (the canonical case); [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^cau-c1b-2-3|§C1b.2, Caution: Rename the dummy index before differentiating]].
>
> **Difficulty 1** (all parts). Submitted solution: as the course solution in every part; (c) writes $\mathcal H$ first in the velocities and then in the momenta (the course solution stresses the rewriting); the vault's [[§C1b.4 Hamiltonian Field Theory#^rem-c1b-4-2|§C1b.4, Remark: Several fields, and a non-canonical normalization]] records the factors of the non-canonical normalisation.

### PS2.3 The complex scalar field: Euler–Lagrange, Hamiltonian, U(1) and its current

The Lagrangian for a complex scalar field is $\mathcal L = \partial_\mu\phi^{\ast}\partial^\mu\phi - m^2\phi^{\ast}\phi - V(\phi^{\ast}\phi)$, with $V$ a smooth function of its argument.

*Parts: (a), (b), (c), (d).*

^ps2-3

#### (a)

Find the Euler–Lagrange equations.

^ps2-3-a

- [ ] Q1 **[def]** Why may $\phi$ and $\phi^{\ast}$ be treated as independent variables?
- [ ] Q2 Compute $\partial\mathcal L/\partial(\partial_\mu\phi)$ and $\partial\mathcal L/\partial(\partial_\mu\phi^{\ast})$. How many factors respond, compared with the real field?
- [ ] Q3 Compute $\partial V/\partial\phi$ by the chain rule.
- [ ] Q4 Write both equations.
- [ ] Q5 **[why]** Why are the two equations complex conjugates of each other, and does one suffice?

> [!tip]- Hint (a): route
> **Strategy (K2).** Treat $\phi$ and $\phi^{\ast}$ as independent; the chain rule through $V$.

#### (b)

Determine the canonical momenta and the Hamiltonian.

^ps2-3-b

- [ ] Q1 **[def]** Define $\pi$ and $\pi^{\ast}$. Which velocity is conjugate to $\phi$?
- [ ] Q2 Carry out the Legendre transform.
- [ ] Q3 Eliminate the velocities.
- [ ] Q4 **[conv]** With $\phi = (\phi_1 + i\phi_2)/\sqrt2$, check that the result is two canonically normalised real fields. Why is there no $\frac12$ in the complex Lagrangian?

#### (c)

Show that the Lagrangian is invariant under simultaneous phase rotations $\phi \to e^{i\alpha}\phi$ and $\phi^{\ast} \to e^{-i\alpha}\phi^{\ast}$.

^ps2-3-c

- [ ] Q1 **[def]** What does it mean for a transformation to be a symmetry of the action, and what is $\mathcal J^\mu$ here?
- [ ] Q2 Transform each of the three terms.
- [ ] Q3 **[why]** Where is the constancy of $\alpha$ used? What fails for $\alpha(x)$?

#### (d)

Find the Noether current corresponding to the symmetry identified in (c).

^ps2-3-d

- [ ] Q1 **[def]** State Noether's current formula, including $\mathcal J^\mu$.
- [ ] Q2 Read off the generators $\Delta\phi$ and $\Delta\phi^{\ast}$.
- [ ] Q3 Assemble $j^\mu$, summing over $\phi$ and $\phi^{\ast}$.
- [ ] Q4 Check $\partial_\mu j^\mu = 0$ with the equations of (a), the potential included.
- [ ] Q5 **[conv]** The overall sign of $j^\mu$ follows the sign of $\alpha$. Compare with PS eq. (2.16) and Lecture 3, slide 22. What sign does $j^0$ have on a positive-frequency solution?

> [!tip]- Hint (d): route
> **Strategy (K12).** Generators $\Delta\phi = i\phi$, $\Delta\phi^{\ast} = -i\phi^{\ast}$, $\mathcal J = 0$, sum over both fields.

> [!tip]- Hints: definitions, results and your solution for the whole problem
> **Topic and definitions.** T3 (a)–(b), T4 (c)–(d). Free complex scalar Model [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^mod-c1b-2-7|§C1b.2.7]] The Free Complex Scalar Field; canonical momentum density Definition [[§C1b.4 Hamiltonian Field Theory#^def-c1b-4-1|§C1b.4.1]] Canonical Momentum Density; generator Definition [[§C1b.5 Noether's Theorem#^def-c1b-5-3|§C1b.5.3]] Generator of a Continuous Transformation; symmetry of the action and $\mathcal J$ Definition [[§C1b.5 Noether's Theorem#^def-c1b-5-5|§C1b.5.5]] Symmetry of the Action; the Vector 𝒥.
>
> **Key results.** Theorem [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-9|§C1b.2.9]] Field and Conjugate as Independent Variables, [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^rem-c1b-2-6|§C1b.2, Remark: The symmetry the real field lacks, and a potential]] (3(a)); Theorem [[§C1b.4 Hamiltonian Field Theory#^thm-c1b-4-3|§C1b.4.3]] Hamiltonian Density of the Free Complex Field (3(b)); Theorem [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-8|§C1b.2.8]] The Complex Field Is Two Real Fields of Equal Mass, Example [[§C1b.5 Noether's Theorem#^ex-c1b-5-1|§C1b.5.1]] δℒ for the Complex Scalar Phase, by Both Routes (3(c)); Theorem [[§C1b.6 Conserved Charges and Internal Symmetries#^thm-c1b-6-3|§C1b.6.3]] The U(1) Current of the Complex Scalar Field (home of 3(c)–(d)); Theorem [[§C1b.5 Noether's Theorem#^thm-c1b-5-4|§C1b.5.4]] Noether's Theorem; Theorem [[§C1b.5 Noether's Theorem#^thm-c1b-5-1|§C1b.5.1]] Generators of the Standard Transformations; [[§C1b.5 Noether's Theorem#^rem-c1b-5-8|§C1b.5, Remark: What the sum over fields runs over]]; [[§C1b.6 Conserved Charges and Internal Symmetries#^cau-c1b-6-3|§C1b.6, Caution: Sign and normalization of the U(1) current]].
>
> **Difficulty 1** (all parts). Submitted solution: (a) varies with respect to both $\phi$ and $\phi^{\ast}$ with $V'$ by the chain rule; (b) as the course solution; (d) the current $i(\phi\partial^\mu\phi^{\ast} - \phi^{\ast}\partial^\mu\phi)$, as the course solution and PS (2.16); the conservation check is not written out (the course solution does it). ERRATA records the sign slip on the Lecture 3 slide ([[§C1b.6 Conserved Charges and Internal Symmetries#^cau-c1b-6-3|§C1b.6, Caution: Sign and normalization of the U(1) current]]).

### PS2.4 The electromagnetic field and its energy–momentum (PS Problem 2.1)

In the absence of sources classical electromagnetism follows from $S = \int d^4x\,\bigl(-\frac14F_{\mu\nu}F^{\mu\nu}\bigr)$, $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$, with the gauge field $A_\mu$ (four components) as dynamical variables.

*Parts: (a), (b), (c), (d), (e).*

^ps2-4

#### (a)

Derive Maxwell's equations as the Euler–Lagrange equations of $S$, treating the components $A_\mu(x)$ as the dynamical variables. The result should be in covariant form.

^ps2-4-a

- [ ] Q1 **[def]** Write the Euler–Lagrange equation for each component $A_\nu$. Why is $\partial\mathcal L/\partial A_\nu = 0$?
- [ ] Q2 Compute $\partial F_{\alpha\beta}/\partial(\partial_\mu A_\nu)$.
- [ ] Q3 Compute $\partial(F_{\alpha\beta}F^{\alpha\beta})/\partial(\partial_\mu A_\nu)$, raising indices with the metric. Where does antisymmetry enter?
- [ ] Q4 Assemble the four equations.
- [ ] Q5 **[why]** Why do only four of Maxwell's equations come out? Where do the other two come from?

> [!tip]- Hint (a): route
> **Strategy (K2).** Differentiate $F_{\alpha\beta}F^{\alpha\beta}$ with respect to the sixteen independent $\partial_\mu A_\nu$; both factors respond and antisymmetry collects four equal terms.

#### (b)

Write the result of (a) in three-vector notation with $E^i = -F^{0i}$, $\epsilon^{ijk}B^k = -F^{ij}$; the four equations are Gauss' law (one) and Ampère's law (three).

^ps2-4-b

- [ ] Q1 Split $\partial_\mu F^{\mu\nu}$ into its time and space parts. Why does no minus sign appear?
- [ ] Q2 Take $\nu = 0$ and identify Gauss' law.
- [ ] Q3 Take $\nu = j$ and bring $\epsilon^{ijk}\partial_iB^k$ to the form of a curl.
- [ ] Q4 **[conv]** Compare the identification with the vault's $F^{0i}$, $F^{ij}$ and with Griffiths' sign of $F^{\mu\nu}$.
- [ ] Q5 **[why]** Where do Faraday's law and $\nabla\cdot\mathbf B = 0$ come from in this formalism?

> [!tip]- Hint (b): route
> **Strategy (K2).** Split the contracted index into time and space with no signs, fix the free index, and put the free index first in $\epsilon$ before naming a curl.

#### (c)

Construct the energy–momentum tensor $T^{\mu\nu}$ by Noether's theorem (the canonical construction).

^ps2-4-c

- [ ] Q1 **[def]** Define the canonical $T^\mu{}_\nu$. What are the roles of the three indices $\mu$, $\nu$, $\lambda$?
- [ ] Q2 Find the generator $\Delta_\nu A_\lambda$ of a translation.
- [ ] Q3 Show that $\delta\mathcal L = a^\nu\partial_\nu\mathcal L$ is a divergence and read off $\mathcal J^\mu{}_\nu$. How is $a^\nu$ factored out?
- [ ] Q4 Assemble $T^\mu{}_\nu$ and raise the second index.
- [ ] Q5 **[why]** Why is $T^{\mu\nu}$ neither symmetric nor gauge invariant?

> [!tip]- Hint (c): route
> **Strategy (K12).** Translations: $\Delta_\nu A_\lambda = \partial_\nu A_\lambda$, $\mathcal J^\mu{}_\nu = \delta^\mu{}_\nu\mathcal L$; then raise $\nu$.

#### (d)

Add $\partial_\lambda K^{\lambda\mu\nu}$ with $K^{\lambda\mu\nu}$ antisymmetric in its first two indices; $\hat T^{\mu\nu} = T^{\mu\nu} + \partial_\lambda K^{\lambda\mu\nu}$ is divergenceless with the same conserved energy and momentum. Show that $K^{\lambda\mu\nu} = F^{\mu\lambda}A^\nu$ makes $\hat T^{\mu\nu}$ symmetric.

^ps2-4-d

- [ ] Q1 **[def]** Why is $\partial_\mu\partial_\lambda K^{\lambda\mu\nu} = 0$ identically for $K$ antisymmetric in $\lambda\mu$?
- [ ] Q2 Check that $F^{\mu\lambda}A^\nu$ is antisymmetric in $\lambda\mu$.
- [ ] Q3 Apply the product rule to $\partial_\lambda(F^{\mu\lambda}A^\nu)$ and use (a).
- [ ] Q4 Combine with $-F^{\mu\lambda}\partial^\nu A_\lambda$ into a product of two field tensors.
- [ ] Q5 Prove the symmetry by relabelling dummies.
- [ ] Q6 **[why]** Why are the charges $P^\nu$ unchanged? Which fall-off is needed?

> [!tip]- Hint (d): route
> **Strategy (K2).** Product rule on $\partial_\lambda K$, Maxwell's equations, then combine with the first term of $T$ into $FF$.

#### (e)

Show that the result of (d) reproduces the energy density and momentum density $\mathcal E = \hat T^{00} = \frac12(\mathbf E^2 + \mathbf B^2)$, $S^i = \hat T^{0i} = (\mathbf E\times\mathbf B)^i$.

^ps2-4-e

- [ ] Q1 Compute $F_{\rho\sigma}F^{\rho\sigma}$ in terms of $\mathbf E$ and $\mathbf B$.
- [ ] Q2 Prove $\epsilon^{ijk}\epsilon^{ijk'} = 2\delta^{kk'}$.
- [ ] Q3 Compute $\hat T^{00}$.
- [ ] Q4 Compute $\hat T^{0i}$: which term drops, and which index moves cost a sign?
- [ ] Q5 **[conv]** In which system of units are these the energy density and Poynting vector? What would change in SI?

> [!tip]- Hint (e): route
> **Strategy (K2).** One metric sign per lowered spatial index; $\epsilon^{ijk}\epsilon^{ijk'} = 2\delta^{kk'}$.

> [!tip]- Hints: definitions, results and your solution for the whole problem
> **Topic and definitions.** T3 (a), T1 (b), T4 (c)–(e). Four-potential and field tensor Definition [[§C1a.7 Relativistic Electrodynamics in Index Form#^def-c1a-7-2|§C1a.7.2]] Four-Potential and Field Tensor in Natural Units; Euler–Lagrange equations Theorem [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-4|§C1b.2.4]] Euler–Lagrange Equations for Fields; canonical energy–momentum tensor Definition [[§C1b.7 Spacetime Symmetries꞉ Energy and Momentum#^def-c1b-7-2|§C1b.7.2]] Canonical Energy–Momentum Tensor; improvement terms Theorem [[§C1b.6 Conserved Charges and Internal Symmetries#^thm-c1b-6-2|§C1b.6.2]] Improvement Terms.
>
> **Key results.** Example [[§C1b.8 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^ex-c1b-8-2|§C1b.8.2]] The Electromagnetic Field (home of Problem 4); Theorem [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-11|§C1a.5.11]] Derivatives with Respect to Tensor Components (4(a)); Theorem [[§C1a.7 Relativistic Electrodynamics in Index Form#^thm-c1a-7-1|§C1a.7.1]] Maxwell's Equations in Heaviside–Lorentz Form, [[§C1a.7 Relativistic Electrodynamics in Index Form#^rem-c1a-7-1|§C1a.7, Remark: Index techniques in Maxwell's equations]] (4(b)); Theorem [[§C1b.7 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-7-5|§C1b.7.5]] Translation Invariance Conserves the Energy–Momentum Tensor (4(c)); [[§C1b.8 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^rem-c1b-8-2|§C1b.8, Remark: Index moves for the electromagnetic tensor]]; Theorem [[§C1b.8 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^thm-c1b-8-4|§C1b.8.4]] The Belinfante Tensor; Theorem [[§C1a.7 Relativistic Electrodynamics in Index Form#^thm-c1a-7-2|§C1a.7.2]] Duality Exchanges E and B; the Two Invariants (4(e)); [[§C1a.7 Relativistic Electrodynamics in Index Form#^cau-c1a-7-1|§C1a.7, Caution: Conventions for F across the sources]].
>
> **Difficulty** (a) 2, (b) 1, (c) 2, (d) 2, (e) 2. Submitted solution: (a) differentiates through $g^{\alpha\rho}g^{\beta\sigma}$, four terms; (b) reorders $\epsilon$ explicitly to name the curl; (c) a long derivation of $\mathcal J^\mu{}_\nu = \delta^\mu{}_\nu\mathcal L$ by choosing $a$ along each axis, with a remark that it is fixed only up to identically conserved terms; (d) two proofs (expanding $F$ in $A$, and the product rule with Maxwell's equations); the vault's Example [[§C1b.8 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^ex-c1b-8-2|§C1b.8.2]] The Electromagnetic Field follows the second; (e) as the course solution and the vault.

## Problem Set 3 (due Sep 18): The Quantum Field

### PS3.1 The Lorentz-invariant measure

Show that the measure $\int\widetilde{d^3k} \equiv \int\frac{d^3k}{(2\pi)^3\,2\omega_k}$ is Lorentz invariant.

*Parts: (a), (b), (c), (d), (e).*

^ps3-1

#### (a)

Show that the measure $d^4k$ is invariant under Lorentz transformations.

^ps3-1-a

- [ ] Q1 **[def]** State the defining condition of a Lorentz transformation and the change-of-variables formula.
- [ ] Q2 Compute the Jacobian matrix of $k \mapsto \Lambda k$.
- [ ] Q3 Derive $\lvert\det\Lambda\rvert = 1$.
- [ ] Q4 **[why]** For an improper $\Lambda$ ($\det\Lambda = -1$), why is the integral still invariant?

> [!tip]- Hint (a): route
> **Strategy (K14).** The Jacobian of $k \to \Lambda k$ is $\det\Lambda$.

#### (b)

Show that $\int d^4k\,\delta(k^2 - m^2)\,\theta(k^0)$ is invariant under Lorentz transformations ($\theta(x) = 0$ for $x < 0$, $1$ for $x \ge 0$).

^ps3-1-b

- [ ] Q1 Why is $\delta(k^2 - m^2)$ invariant?
- [ ] Q2 **[why]** $\theta(k^0)$ is not invariant in general. For which $k$ can a Lorentz transformation flip the sign of $k^0$, and why does that not matter here?
- [ ] Q3 Show that a boost preserves the sign of $k^0$ for timelike $k$.
- [ ] Q4 **[conv]** Which Lorentz transformations are excluded from the statement?
- [ ] Q5 **[conv]** The sheet sets $\theta(0) = 1$. Does $\theta(0)$ matter here? Where does the value of $\theta(0)$ matter later in the course?

> [!tip]- Hint (b): route
> **Strategy (K14).** Measure, δ and θ separately; θ only matters on the mass shell.

#### (c)

Write $k^2 - m^2$ in terms of only $k^0$ and $\omega_k \equiv +(\lvert\mathbf k\rvert^2 + m^2)^{1/2}$. At which values of $k^0$ is it zero?

^ps3-1-c

- [ ] Q1 Expand $k^2 - m^2$ in components.
- [ ] Q2 Find the zeros in $k^0$.
- [ ] Q3 **[def]** Why is $\omega_k$ defined as the positive root?

#### (d)

With $\delta(f(x)) = \sum_i\frac{1}{\lvert f'(x_i)\rvert}\delta(x - x_i)$ (sum over the zeros of $f$), evaluate the $dk^0$ integral that is part of $d^4k$ in (b).

^ps3-1-d

- [ ] Q1 **[def]** State the composition rule with its hypothesis on the zeros.
- [ ] Q2 Compute $f'(k^0)$ at both roots.
- [ ] Q3 Apply $\theta(k^0)$ and do the integral.
- [ ] Q4 **[why]** In what sense is $\delta(f(x))$ defined, and what would go wrong at a double zero?

> [!tip]- Hint (d): route
> **Strategy (K13).** Composition of δ with a function with simple zeros.

#### (e)

Combine the results to argue that $\int\frac{d^3k}{(2\pi)^3\,2\omega_k}$ is Lorentz invariant (the factors of $2\pi$ are convenient normalisations).

^ps3-1-e

- [ ] Q1 Split $d^4k = d^3k\,dk^0$ and insert (d).
- [ ] Q2 Conclude, saying which transformations the invariance covers.
- [ ] Q3 **[conv]** Write the measure in Peskin–Schroeder's form with $\frac{d^4k}{(2\pi)^4}\,2\pi\,\delta(k^2 - m^2)\,\theta(k^0)$. Where do the factors of $2\pi$ go?
- [ ] Q4 **[conv]** The sheet and Lectures 4–5 write $\omega_k$; the vault writes $E_{\mathbf k}$. Same object?

> [!tip]- Hints: definitions, results and your solution for the whole problem
> **Topic and definitions.** T5 (tools of T6). Lorentz transformation Definition [[§C1a.4 The Lorentz Group#^def-c1a-4-1|§C1a.4.1]] Lorentz Transformation, Active Reading; invariant measure Definition [[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-2|§C2a.4.2]] Invariant Measure and One-Particle Completeness; what "Lorentz invariant" means [[§C1a.4 The Lorentz Group#^rem-c1a-4-1|§C1a.4, Remark: What "Lorentz invariant" means in field theory]]; $\omega$ versus $E$ [[§C2a.1 Canonical Quantization of Fields#^cau-c2a-1-1|§C2a.1, Caution: Eₚ, not ωₚ; π, not Π]].
>
> **Key results.** Theorem [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-3|§C2a.4.3]] The Invariant Measure (home of Problem 1); invariant volume elements Theorem [[§C1a.4 The Lorentz Group#^thm-c1a-4-1|§C1a.4.1]] Invariant Volume Elements; orbits of $SO^+(1,3)$ Theorem [[§C1a.4 The Lorentz Group#^thm-c1a-4-2|§C1a.4.2]] The Orbits of SO⁺(1,3) on Spacetime; composition of δ Theorem [[§CA.2 Generalized Functions#^thm-ca-2-6|§CA.2.6]] Composition of δ with a Function; invariant distributions on the mass shell Theorem [[§CA.2 Generalized Functions#^thm-ca-2-7|§CA.2.7]] Invariant Distributions on the Mass Shell and the Light Cone; [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^cau-c2b-6-1|§C2b.6, Caution: The step function at zero]].
>
> **Difficulty 1** (all parts). Submitted solution: (a) Jacobian $= \Lambda$, $\lvert\det\Lambda\rvert = 1$; (b) treats measure, δ and θ separately and proves that rotations and boosts preserve the sign of $k^0$ for timelike $k$ by an explicit boost inequality, restricting the claim to proper orthochronous transformations; the course solution adds a remark on improper ones for $d^4k$; (c)–(e) as the course solution.

### PS3.2 Quantization of the complex scalar field (PS Problem 2.2(a)–(c))

A complex scalar field with $S = \int d^4x\,\bigl(\partial_\mu\phi^{\ast}\partial^\mu\phi - m^2\phi^{\ast}\phi\bigr)$, so that $\phi$ and $\phi^{\ast}$ each obey the Klein–Gordon equation; treat $\phi$ and $\phi^{\ast}$ as independent fields (as in PS2.3).

*Parts: (a1), (a2), (b), (c).*

^ps3-2

#### (a1)

Find the momenta $\pi$ and $\pi^{\ast}$ conjugate to $\phi$ and $\phi^{\ast}$ and write down the canonical commutation relations. Show that $H = \int d^3x\,\bigl(\pi^{\ast}\pi + \nabla\phi^{\ast}\cdot\nabla\phi + m^2\phi^{\ast}\phi\bigr)$. (Careful: with this Lagrangian $\pi = \partial\mathcal L/\partial\dot\phi$ is $\dot\phi^{\ast}$, not $\dot\phi$.)

^ps3-2-a1

- [ ] Q1 **[def]** Define the conjugate momenta. Which velocity is conjugate to $\phi$?
- [ ] Q2 **[def]** Write the equal-time commutation relations: which commutators are nonzero, which vanish?
- [ ] Q3 Carry out the Legendre transform and eliminate the velocities.
- [ ] Q4 **[why]** Does the operator order of $\pi^{\ast}\pi$ in $H$ matter at this stage?

#### (a2)

Compute the Heisenberg equation $i\partial_tO = [O, H]$ for $O = \phi$, and then for the conjugate momentum. Show that the two combine into the Klein–Gordon equation.

^ps3-2-a2

- [ ] Q1 Compute $[\phi(\mathbf x), H]$: which term of $H$ contributes?
- [ ] Q2 Compute $[\pi(\mathbf x), H]$. How do you handle $[\pi(\mathbf x), \nabla\phi(\mathbf y)]$?
- [ ] Q3 **[why]** Integrate $\nabla\phi^{\ast}\cdot\nabla_y\delta^3(\mathbf x - \mathbf y)$ by parts. In what sense is this integral defined, and why does the boundary term vanish?
- [ ] Q4 Combine the two equations into the Klein–Gordon equation. For which field do you get it first, and how do you get the other?

> [!tip]- Hint (a2): route
> **Strategy (K11).** Commute with $H$ term by term; integrate the gradient of δ by parts.

#### (b)

Diagonalize $H$ by introducing creation and annihilation operators. Show that the theory contains two independent sets of particles, both of mass $m$. The conventional expansion is $\phi(x) = \int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2\omega_p}}\bigl(a_{\mathbf p}e^{-ipx} + b^\dagger_{\mathbf p}e^{ipx}\bigr)$. Composite operators are defined by normal ordering: upon introduction of the oscillators, $a_{\mathbf p}$ is placed to the right of $a^\dagger_{\mathbf p}$ (and $b_{\mathbf p}$ of $b^\dagger_{\mathbf p}$) from the outset; operators in the "wrong" order are first reordered without taking the commutator into account and only then promoted to noncommuting operators.

^ps3-2-b

- [ ] Q1 Write the general solution for $\phi$ with two independent coefficients per $\mathbf p$. How is the expansion of $\phi^{\ast}$ related to it?
- [ ] Q2 Write the expansions of $\pi = \dot\phi^{\ast}$ and $\pi^{\ast} = \dot\phi$.
- [ ] Q3 Substitute into $H$ and do the $d^3x$ integrals. Which δ's appear, and what phases survive?
- [ ] Q4 Show that the number-changing terms ($ab$ and $b^\dagger a^\dagger$) cancel. What do you need for that?
- [ ] Q5 **[why]** The commutators $[a, a^\dagger]$, $[b, b^\dagger]$, $[a, b]$, $[a, b^\dagger]$: are they assumed or derived? Derive them from the canonical relations of (a1) by inverting the expansions.
- [ ] Q6 **[conv]** Apply the sheet's normal-ordering prescription. What constant would reordering with the commutator have produced instead, and what is it physically?
- [ ] Q7 Read off the particle content: how many species, which energy–momentum relation?

> [!tip]- Hint (b): route
> **Strategy (K9, K10, K11).** Expand $\phi$, $\phi^\dagger$, $\pi$, $\pi^\dagger$ in modes, substitute into $H$, do the $d^3x$ integrals, show the number-changing terms vanish, normal-order.

#### (c)

The action is invariant under $\phi \to e^{i\alpha}\phi$, $\phi^{\ast} \to e^{-i\alpha}\phi^{\ast}$ (PS2.3); the conserved charge, in PS's normalisation, is $Q = \int d^3x\,\frac i2\bigl(\phi^{\ast}\pi^{\ast} - \pi\phi\bigr)$. Rewrite $Q$ in terms of creation and annihilation operators and determine the charge of the particles of each type. (The overall normalisation is a convention: $Q$ differs by a constant factor from the Noether charge of PS2.3(d); only the ratio of the two charges is physical.)

^ps3-2-c

- [ ] Q1 Substitute the expansions of $\phi^\dagger$, $\pi^\dagger$, $\pi$, $\phi$ into $Q$.
- [ ] Q2 Do the $d^3x$ integrals. Why are the energy ratios $\sqrt{\omega_q/\omega_p}$ harmless?
- [ ] Q3 Show that the number-changing terms drop out.
- [ ] Q4 Normal-order and express $Q$ through the number operators $N_a$, $N_b$.
- [ ] Q5 **[conv]** Compare the normalisation and sign with the Noether charge of PS2.3(d) and with Yu's charge. Which feature is physical?
- [ ] Q6 **[why]** Why must the vacuum carry zero charge, and what would the unordered $Q$ give on it?

> [!tip]- Hint (c): route
> **Strategy (K9).** Same substitution as (b); the δ's equate the energies and kill the number-changing terms; normal-order.

> [!tip]- Hints: definitions, results and your solution for the whole problem
> **Topic and definitions.** T5. The complex quantum field Model [[§C2a.5 The Complex Scalar Field and Its Charge#^mod-c2a-5-1|§C2a.5.1]] The Free Complex Scalar Quantum Field; equal-time commutation relations Principle [[§C2a.1 Canonical Quantization of Fields#^pr-c2a-1-2|§C2a.1.2]] Equal-Time Canonical Commutation Relations; normal ordering Definition [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^def-c2a-3-1|§C2a.3.1]] Normal Ordering; the charge operator Definition [[§C2a.5 The Complex Scalar Field and Its Charge#^def-c2a-5-1|§C2a.5.1]] The U(1) Charge Operator.
>
> **Key results.** Theorem [[§C1b.4 Hamiltonian Field Theory#^thm-c1b-4-3|§C1b.4.3]] Hamiltonian Density of the Free Complex Field (2(a1)); the real field's Heisenberg equations Theorem [[§C2b.1 Heisenberg Fields#^thm-c2b-1-2|§C2b.1.2]] The Heisenberg Equations Are the Klein–Gordon Equation and the complex case in [[§C2a.5 The Complex Scalar Field and Its Charge|§C2a.5]] The Complex Scalar Field and Its Charge, Connections (2(a2)); Theorem [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-2|§C2a.5.2]] Mode Expansion of the Complex Field, Theorem [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-3|§C2a.5.3]] Mode Algebra of the Complex Field, Theorem [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-4|§C2a.5.4]] Hamiltonian of the Complex Field (home of 2(b)); Theorem [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-6|§C2a.5.6]] The Charge Counts Particles Minus Antiparticles, Theorem [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-7|§C2a.5.7]] Particles and Antiparticles (home of 2(c)); [[§C2a.5 The Complex Scalar Field and Its Charge#^cau-c2a-5-1|§C2a.5, Caution: Normalization and sign of the charge]]; [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^rem-c2a-3-2|§C2a.3, Remark: Normal ordering is a choice of quantization]]; Theorem [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-4|§C2a.3.4]] The Zero-Point Energy; Theorem [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-2|§C2a.3.2]] δ³(0) Has No Value; in a Box It Is the Volume; [[§C2a.2 Mode Expansion and the Mode Algebra#^rem-c2a-2-2|§C2a.2, Remark: Two bookkeeping rules for mode integrals]]; Theorem [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|§CA.3.3]] Plane Waves Integrate to a Delta Function; [[P1 Canonical Quantization#^p1-6|P1, step 6]], [[P1 Canonical Quantization#^p1-7|P1, step 7]], [[P1 Canonical Quantization#^p1-8|P1, step 8]].
>
> **Difficulty** (a1) 1, (a2) 2, (b) 3, (c) 2. Submitted solution: (a2) commutes $\pi$ (conjugate to $\phi$) with $H$, integrates $\nabla\delta$ by parts and obtains the Klein–Gordon equation for $\phi^{\ast}$ first; the course solution uses $\pi_{\phi^{\ast}}$. (b) builds the expansions from two independent solutions plus conjugation, inverts them to derive the oscillator algebra from the canonical relations (including $[a_{\mathbf p}, b_{\mathbf q}] = 0$ from the factor $\omega_p - \omega_q$ on $\delta^3(\mathbf p + \mathbf q)$), cancels the number-changing terms by a relabelling and $[b_{\mathbf p}, a_{-\mathbf p}] = 0$, then reorders with the commutator, identifies the zero-point term and subtracts it; the sheet asks to reorder before promoting; same final $H$ ([[§C2a.3 Energy, Momentum and the Zero-Point Energy#^rem-c2a-3-2|§C2a.3, Remark: Normal ordering is a choice of quantization]]). About four pages. (c) the number-changing terms drop once the δ sets the energies equal; normal-orders $bb^\dagger$ at the end; result as the course solution and Theorem [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-6|§C2a.5.6]] The Charge Counts Particles Minus Antiparticles.

### PS3.3 Canonical commutation relations imply the oscillator algebra

A real scalar field $\hat\phi(\mathbf x)$ with conjugate momentum $\hat\Pi(\mathbf x)$, expanded as $\hat\phi(\mathbf x) = \int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2\omega_{\mathbf p}}}\bigl(a_{\mathbf p}e^{i\mathbf p\cdot\mathbf x} + a^\dagger_{\mathbf p}e^{-i\mathbf p\cdot\mathbf x}\bigr)$, $\hat\Pi(\mathbf x) = \int\frac{d^3p}{(2\pi)^3}(-i)\sqrt{\frac{\omega_{\mathbf p}}{2}}\bigl(a_{\mathbf p}e^{i\mathbf p\cdot\mathbf x} - a^\dagger_{\mathbf p}e^{-i\mathbf p\cdot\mathbf x}\bigr)$. In PS and Lecture 4, $[a_{\mathbf k}, a^\dagger_{\mathbf p}] = (2\pi)^3\delta^{(3)}(\mathbf k - \mathbf p)$ was shown to imply $[\hat\phi(\mathbf x), \hat\Pi(\mathbf x')] = i\delta^{(3)}(\mathbf x - \mathbf x')$; verify the opposite direction. Define the Heisenberg field $\hat\phi_H(x) = \int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2\omega_{\mathbf p}}}\bigl[a_{\mathbf p}e^{-ipx} + a^\dagger_{\mathbf p}e^{ipx}\bigr]$, $px = \omega_{\mathbf p}t - \mathbf p\cdot\mathbf x$, with $\hat\phi_H\rvert_{t=0} = \hat\phi(\mathbf x)$ and $\partial_t\hat\phi_H\rvert_{t=0} = \hat\Pi(\mathbf x)$, and the sesquilinear form $(f, g) \equiv i\int d^3x\,f^{\ast}(x)\overleftrightarrow{\partial_0}g(x)$, $f^{\ast}\overleftrightarrow{\partial_0}g \equiv f^{\ast}\partial_0g - (\partial_0f^{\ast})g$, an inner product on the solutions of the Klein–Gordon equation with a given mass.

*Parts: (a), (b), (c).*

^ps3-3

#### (a)

The $d^3x$ integration is taken at fixed time. Show that $(f, g)$ is independent of that time: take the time derivative and show that it vanishes by the Klein–Gordon equation.

^ps3-3-a

- [ ] Q1 **[def]** Define $(f, g)$. In which argument is it antilinear?
- [ ] Q2 Differentiate in $t$: which terms cancel by the product rule?
- [ ] Q3 Use the Klein–Gordon equation for $g$ and for $f^{\ast}$. Why is $f^{\ast}$ a solution too?
- [ ] Q4 Integrate the Laplacian terms by parts. What happens to the boundary terms?
- [ ] Q5 **[why]** Is $(f, f)$ positive for every solution? In what sense is $(f, g)$ an "inner product"?

> [!tip]- Hint (a): route
> **Strategy.** Product rule, Klein–Gordon equation, integration by parts.

#### (b)

Show that $a_{\mathbf p} = (f_p(x), \hat\phi_H(x))$ with $f_p(x) = \frac{1}{\sqrt{2\omega_{\mathbf p}}}e^{-ip\cdot x}$; this inverts the expansions of $\phi$, $\Pi$ by writing $a$ in terms of $\phi$ and $\dot\phi = \Pi$.

^ps3-3-b

- [ ] Q1 Compute $f_p^{\ast}$ and $\partial_0f_p^{\ast}$.
- [ ] Q2 **[why]** Why may you evaluate $(f_p, \hat\phi_H)$ at any one time, for instance $t = 0$?
- [ ] Q3 Compute the two halves of the product separately; which δ's appear?
- [ ] Q4 Which operator contributions cancel and which add?
- [ ] Q5 **[conv]** The sheet's $\hat\phi(\mathbf x)$ carries $e^{+i\mathbf p\cdot\mathbf x}$ on $a_{\mathbf p}$ while $\hat\phi_H$ carries $e^{-ipx}$. Check that they agree at $t = 0$.

> [!tip]- Hint (b): route
> **Strategy (K10).** Evaluate the conserved product at a convenient time; the $d^3x$ integrals give δ's; the $a^\dagger$ pieces cancel between the two halves of $\overleftrightarrow{\partial_0}$.

#### (c)

Express $[a_{\mathbf k}, a^\dagger_{\mathbf p}]$ with (b) and its Hermitian conjugate; trade time derivatives for canonical momenta; use the equal-time commutators and simplify. You should recover $(2\pi)^3\delta^{(3)}(\mathbf k - \mathbf p)$.

^ps3-3-c

- [ ] Q1 Obtain $a^\dagger_{\mathbf p}$ from (b). Which property of $\hat\phi_H$ is used?
- [ ] Q2 At $t = 0$, write $a_{\mathbf k}$ and $a^\dagger_{\mathbf p}$ as integrals of $\hat\Pi$ and $\hat\phi$.
- [ ] Q3 Expand the commutator by bilinearity. Which field commutators vanish?
- [ ] Q4 Insert the canonical relations and do both integrals.
- [ ] Q5 **[why]** The prefactor $(\omega_{\mathbf k} + \omega_{\mathbf p})/(2\sqrt{\omega_{\mathbf k}\omega_{\mathbf p}})$ appears. Why may it be set to $1$?
- [ ] Q6 **[conv]** Where does the $(2\pi)^3$ sit in $[a, a^\dagger]$ and in the measure, and what does Lecture 4's normalisation slide drop?

> [!tip]- Hint (c): route
> **Strategy (K10, K11).** At $t = 0$, $a_{\mathbf k}$ and $a^\dagger_{\mathbf p}$ are integrals of $\hat\Pi$ and $\hat\phi$; bilinearity and the canonical relations leave one δ.

> [!tip]- Hints: definitions, results and your solution for the whole problem
> **Topic and definitions.** T5. Klein–Gordon inner product Definition [[§C2a.2 Mode Expansion and the Mode Algebra#^def-c2a-2-1|§C2a.2.1]] Klein–Gordon Inner Product; equal-time commutation relations Principle [[§C2a.1 Canonical Quantization of Fields#^pr-c2a-1-2|§C2a.1.2]] Equal-Time Canonical Commutation Relations; Heisenberg field Definition [[§C2b.1 Heisenberg Fields#^def-c2b-1-1|§C2b.1.1]] Heisenberg Field.
>
> **Key results.** Theorem [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-3|§C2a.2.3]] Conservation and Orthonormality of the Modes (home of 3(a)); Theorem [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-5|§C2a.2.5]] Mode Extraction (home of 3(b)); Theorem [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|§C2a.2.6]] The Mode Algebra (home of 3(c)); Theorem [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-2|§C2a.2.2]] Mode Expansion of the Real Field; Theorem [[§C2b.1 Heisenberg Fields#^thm-c2b-1-4|§C2b.1.4]] Time Dependence of the Modes; the Covariant Mode Expansion; [[§C2a.2 Mode Expansion and the Mode Algebra#^rem-c2a-2-4|§C2a.2, Remark: Why this inner product, and why it is indefinite]]; Theorem [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|§CA.3.3]] Plane Waves Integrate to a Delta Function.
>
> **Difficulty** (a) 1, (b) 2, (c) 2. Submitted solution: (a) as the course solution, with the integration by parts written out; (b) evaluates at $t = 0$ (justified by (a)) and splits the product into two terms; the course solution keeps general $t$; (c) explicit Fourier integrals of $\hat\Pi$ and $\hat\phi$ at $t = 0$; the course solution reduces the commutator to $(f_k, f_p)$ instead.

### PS3.4 Coherent states

A free scalar field quantized with $[a_{\mathbf k}, a^\dagger_{\mathbf p}] = (2\pi)^3\delta(\mathbf k - \mathbf p)$ and a vacuum $a_{\mathbf k}\lvert0\rangle = 0$. A coherent state, characterised by complex numbers $\eta_{\mathbf k}$, is $\lvert\{\eta_{\mathbf k}\}\rangle \equiv \mathcal N\exp\Bigl\{\int\frac{d^3k}{(2\pi)^3}\frac{\eta_{\mathbf k}a^\dagger_{\mathbf k}}{\sqrt{2E_{\mathbf k}}}\Bigr\}\lvert0\rangle$, with $\mathcal N$ a normalisation factor.

*Parts: (a), (b), (c), (d), (e).*

^ps3-4

#### (a)

Show that $a_{\mathbf p}\lvert\{\eta_{\mathbf k}\}\rangle = \frac{\eta_{\mathbf p}}{\sqrt{2E_{\mathbf p}}}\lvert\{\eta_{\mathbf k}\}\rangle$, e.g. by first establishing $\bigl[a_{\mathbf p}, \exp\{\cdots\}\bigr] = \frac{\eta_{\mathbf p}}{\sqrt{2E_{\mathbf p}}}\exp\{\cdots\}$ with the schematic formula $[a_{\mathbf p}, (a^\dagger_{\mathbf k})^m] = m(a^\dagger_{\mathbf k})^{m-1}(2\pi)^3\delta(\mathbf p - \mathbf k)$.

^ps3-4-a

- [ ] Q1 **[def]** Name the exponent $K$. Compute $[a_{\mathbf p}, K]$. Why is it a c-number?
- [ ] Q2 Compute $[a_{\mathbf p}, K^n]$ by the Leibniz rule for commutators.
- [ ] Q3 Resum the exponential series.
- [ ] Q4 Act on the vacuum and conclude.
- [ ] Q5 **[why]** Make the schematic formula precise for $m$ different momenta $\mathbf k_1, \dots, \mathbf k_m$. How do the δ and the $(2\pi)^3$ remove one momentum integral?

> [!tip]- Hint (a): route
> **Strategy (K11).** $[a_{\mathbf p}, K]$ is a c-number for the exponent $K$; Leibniz rule on $K^n$; resum.

#### (b)

Determine $\mathcal N$ such that the norm of the state is $1$.

^ps3-4-b

- [ ] Q1 **[def]** Write the bra $\langle\{\eta_{\mathbf k}\}\rvert$ explicitly.
- [ ] Q2 Use (a) to evaluate the exponential of annihilators acting on the ket.
- [ ] Q3 Why is $\langle0\rvert e^K\lvert0\rangle = 1$?
- [ ] Q4 Solve for $\lvert\mathcal N\rvert$.
- [ ] Q5 **[why]** What remains undetermined in $\mathcal N$, and why does it not matter?

#### (c)

Compute the expectation value of the quantum field, $\bar\phi(x) \equiv \langle\{\eta_{\mathbf k}\}\rvert\phi(x)\lvert\{\eta_{\mathbf k}\}\rangle$ (in a coherent state some classical properties are recovered).

^ps3-4-c

- [ ] Q1 Expand $\phi(x)$ in modes.
- [ ] Q2 Act with $a_{\mathbf p}$ on the ket and with $a^\dagger_{\mathbf p}$ on the bra.
- [ ] Q3 Write $\bar\phi(x)$.
- [ ] Q4 **[why]** Which equation does $\bar\phi(x)$ solve, and in what sense is it classical?
- [ ] Q5 **[why]** What is the mean field in a state of definite particle number, and why?

> [!tip]- Hint (c): route
> **Strategy (K9).** Annihilators act to the right, creators to the left, by (a).

#### (d)

Compute the average particle number $\bar N = \langle\{\eta_{\mathbf k}\}\rvert N\lvert\{\eta_{\mathbf k}\}\rangle$, $N \equiv \int\frac{d^3k}{(2\pi)^3}a^\dagger_{\mathbf k}a_{\mathbf k}$.

^ps3-4-d

- [ ] Q1 **[def]** Why is $a^\dagger_{\mathbf k}a_{\mathbf k}$ already in the convenient order?
- [ ] Q2 Compute $\bar N$.
- [ ] Q3 Relate $\bar N$ to the normalisation found in (b).

#### (e)

Calculate the mean-square dispersion $\langle\Delta N^2\rangle \equiv \langle\{\eta_{\mathbf k}\}\rvert(N - \bar N)^2\lvert\{\eta_{\mathbf k}\}\rangle$. What is the condition on $\{\eta_k\}$ for the relative fluctuation to be small, $\sqrt{\langle\Delta N^2\rangle} \ll \bar N$? (For such states the quantum field behaves essentially like a classical field.)

^ps3-4-e

- [ ] Q1 Reduce $\langle\Delta N^2\rangle$ to $\langle N^2\rangle - \bar N^2$.
- [ ] Q2 In $\langle N^2\rangle$ the inner pair $a_{\mathbf p}a^\dagger_{\mathbf q}$ is in the wrong order. Reorder it.
- [ ] Q3 Evaluate both resulting terms; which one is $\bar N^2$?
- [ ] Q4 State $\langle\Delta N^2\rangle$ and the condition for small relative fluctuations.
- [ ] Q5 **[why]** Which distribution has this mean–variance relation? Why must a state with a definite field have an indefinite particle number?

> [!tip]- Hint (e): route
> **Strategy (K11).** Reorder the inner pair of $N^2$ with the commutator.

> [!tip]- Hints: definitions, results and your solution for the whole problem
> **Topic and definitions.** T5. Coherent state Definition [[§C2a.6 Coherent States and the Classical Field#^def-c2a-6-1|§C2a.6.1]] Coherent State of the Field; vacuum and Fock space Principle [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^pr-c2a-3-3|§C2a.3.3]] The Vacuum and the Fock Space; the mode algebra Theorem [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|§C2a.2.6]] The Mode Algebra.
>
> **Key results.** Theorem [[§C2a.6 Coherent States and the Classical Field#^thm-c2a-6-2|§C2a.6.2]] Coherent States Are Eigenstates of Every Annihilator (home of 4(a)–(b)); Theorem [[§C2a.6 Coherent States and the Classical Field#^thm-c2a-6-4|§C2a.6.4]] The Mean Field Is a Classical Solution (home of 4(c)); Theorem [[§C2a.6 Coherent States and the Classical Field#^thm-c2a-6-6|§C2a.6.6]] Poisson Number Statistics (home of 4(d)–(e)); [[§C2a.6 Coherent States and the Classical Field#^rem-c2a-6-1|§C2a.6, Remark: Why a definite field needs an indefinite particle number]] (4(e)); Theorem [[§C2a.6 Coherent States and the Classical Field#^thm-c2a-6-1|§C2a.6.1]] A State of Definite Particle Number Has No Mean Field; Theorem [[§C2a.6 Coherent States and the Classical Field#^thm-c2a-6-3|§C2a.6.3]] A Coherent State Is the Displaced Vacuum.
>
> **Difficulty** (a) 2, (b) 1, (c) 1, (d) 1, (e) 2. Submitted solution: (a) gives two derivations, the Leibniz rule on $K^n$ and the multi-mode product formula; (b) uses the $K^\dagger$ eigenvalue and writes $\mathcal N = e^{-\lambda/2}$, later identifying $\lambda$ with $\bar N$; (c)–(e) as the course solution; (e) states the condition on the integral as a whole. The vault's Theorem [[§C2a.6 Coherent States and the Classical Field#^thm-c2a-6-6|§C2a.6.6]] Poisson Number Statistics adds the Poisson distribution.

## Problem Set 4: Green's Functions (due Sep 25)

### PS4.0 Generalized functions: a survival guide

(0 points; "a lot of text but no questions that must be responded to".) Test functions $\varphi(x)$ are smooth and vanish outside a finite region; a generalized function is a linear map from test functions to numbers. Examples: (1) $\varphi \mapsto \int dx\,\psi(x)\varphi(x)$ for an ordinary function $\psi$, which can be reconstructed from the map by feeding it test functions sharply peaked at $x_0$ with $\int\varphi = 1$; (2) $\varphi \mapsto \int dx\,\varphi(x)$, the constant function $1$, which is not a test function; (3) $\varphi \mapsto \varphi(0)$, read through (1) as $\psi = \delta$. A Green's function $G(x - x')$ of a differential operator $(-\Delta_x)$, "such as the Klein–Gordon operator $-\Delta_x = -\partial_\mu\partial^\mu + m^2$", encodes the solutions of $(-\Delta_x)\psi = j$ (4) as $\psi(x) = \int dx'\,G(x - x')j(x')$ (5), written as $(-\Delta_x)G(x - x') = \delta(x - x')$ (6). Since a physical source $j$ is a test function, what is defined is the linear map (5), not an ordinary function; it is not unique: there is one map, and one Green's function, for each boundary condition.

^ps4-0

- [ ] Q1 **[def]** Define a test function and a generalized function. Which property of a test function makes $\varphi \mapsto \int\psi\varphi$ well defined for every locally integrable $\psi$, including the constant $1$?
- [ ] Q2 Explain how the ordinary function $\psi$ is recovered from the map $\varphi \mapsto \int\psi\varphi$. Which test functions do you feed it, and why does their smoothness not get in the way?
- [ ] Q3 **[def]** Write the $\delta$ function as a map on test functions. Why is there no locally integrable $\psi$ with $\int\psi\varphi = \varphi(0)$ for every $\varphi$?
- [ ] Q4 Given $(\partial^2 + m^2)D_C(x - y) = -i\delta^4(x - y)$, show that $\phi(x) = i\int d^4y\,D_C(x - y)j(y)$ solves $(\partial^2 + m^2)\phi = j$. What licenses moving the operator inside the integral when $j$ is a test function?
- [ ] Q5 **[why]** Why can a Green's function not be unique? Show that two of them differ by a solution of the homogeneous equation, and say what fixes the choice.
- [ ] Q6 **[conv]** With the metric $(+,-,-,-)$, write the Klein–Gordon operator and compare it with the statement's "$-\Delta_x = -\partial_\mu\partial^\mu + m^2$". How is the statement's $G$ of (6) related to the vault's $D_C$ (factor and sign)?

> [!tip]- Hints: definitions, results, route, your solution
> **Topic and definitions.** T6. Test functions Definition [[§CA.2 Generalized Functions#^def-ca-2-1|§CA.2.1]] Test Functions: the Spaces 𝒟 and 𝒮; generalized function, tempered distribution Definition [[§CA.2 Generalized Functions#^def-ca-2-2|§CA.2.2]] Generalized Function; Tempered Distribution; Green's function of the Klein–Gordon operator Definition [[§C2b.5 Green's Functions and Contours#^def-c2b-5-1|§C2b.5.1]] Green's Function of the Klein–Gordon Operator; fundamental solution Definition [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^def-ca-6-1|§CA.6.1]] Fundamental Solution.
>
> **Key results.** [[§CA.2 Generalized Functions#^rem-ca-2-1|§CA.2, Remark: What changes from the working delta function]] (the three examples, this problem); [[§C2b.5 Green's Functions and Contours#^rem-c2b-5-1|§C2b.5, Remark: What a Green's "function" is, and why it is not unique]] (this problem: the kernel of a linear map, non-uniqueness, the factor $-i$, the sign of $-\Delta_x$); Theorem [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-7|§CA.6.7]] Fundamental Solutions Differ by Homogeneous Solutions; Theorem [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-8|§CA.6.8]] Convolution with a Fundamental Solution Solves the Sourced Equation; Theorem [[§C2b.8 Particle Production by a Classical Source#^thm-c2b-8-4|§C2b.8.4]] The Source Is a Test Function; Why $\bar N$ Is Finite (the source is a test function); [[§CA.2 Generalized Functions#^rem-ca-2-3|§CA.2, Remark: What the language buys in field theory]].
>
> **Strategy (K13).** Read every "function" as a linear map on test functions; the $\delta$-source equation (6) is shorthand for the map $j \mapsto \psi$ of (5).
>
> **Difficulty 1.** No submission: Problem 0 has no questions, and the user's write-up starts at Problem 1. The vault records the sign of $\partial^2$ in the statement's $-\Delta_x$ as a slip of the problem set (`ERRATA.md`; [[§C2b.5 Green's Functions and Contours#^rem-c2b-5-1|§C2b.5, Remark: What a Green's "function" is, and why it is not unique]]).

### PS4.1 Complex contour integration: a survival guide

*Parts: (a), (b), (c), (d), (e), (f), (g), (h), (i).*

^ps4-1

#### (a)

For $f(z) = 1/z$, evaluate $\int_C f(z)\,dz$ (7) when $C$ is the circle of radius $R > 0$ about the origin, traversed counterclockwise. (Hint: $z = Re^{i\phi}$, $\phi \in [0, 2\pi[$.)

^ps4-1-a

- [ ] Q1 **[def]** Define $\int_C f\,dz$ for a contour given by a parametrization $z(s)$, $a \le s \le b$.
- [ ] Q2 Write $z(\phi)$ and $z'(\phi)$ for the counterclockwise circle and substitute into the definition. What is the integrand in $\phi$?
- [ ] Q3 **[why]** The result does not depend on $R$. Explain why from the integrand you obtained in Q2.

> [!tip]- Hint (a): route
> **Strategy (K13).** Parametrize and integrate.

#### (b)

What is the result for the integral in (a) when the contour is traversed clockwise?

^ps4-1-b

- [ ] Q1 Write a parametrization of the clockwise circle and repeat (a).
- [ ] Q2 **[why]** Show from the definition of a contour integral that reversing the orientation of any contour flips the sign of the integral.
- [ ] Q3 Which later part of this problem needs this sign, and where does it enter there?

> [!tip]- Hint (b): route
> **Strategy (K13).** Parametrize the reversed circle, or use the orientation rule.

#### (c)

A function is holomorphic (analytic) if it has no singularities in the complex plane; it can be written as $\sum_{n\ge0}a_n(z - z_0)^n$. Evaluate (7) for $f_n(z) = z^n$, $n = 0, 1, \dots$, on the contour of (a).

^ps4-1-c

- [ ] Q1 **[def]** Define an analytic (holomorphic) function in the vault's sense, and compare with the statement's "no singularities in the complex plane".
- [ ] Q2 Compute $\oint z^n\,dz$ on the circle by the parametrization. Where do you use $n + 1 \ne 0$, and where that $n + 1$ is an integer?
- [ ] Q3 Deduce $\oint f\,dz$ for $f$ given by a power series about $0$. What do you need to integrate the series term by term?
- [ ] Q4 **[why]** Compare with Cauchy's theorem. Which hypothesis of that theorem does a power series converging on the closed disc satisfy?

> [!tip]- Hint (c): route
> **Strategy (K13).** Same parametrization; the exponential integrates to zero over a full period.

#### (d)

$1/z$ is not holomorphic (singular at $z = 0$); functions with isolated singularities are meromorphic and expand on $f_n(z) = (z - z_0)^n$ with $n$ any integer; a power-law singularity at $z_0$ is a pole. Evaluate (7) for $f_n$ with pole $z_0 = 0$ on the contour of (a), for every negative $n$.

^ps4-1-d

- [ ] Q1 **[def]** Define the Laurent expansion at an isolated singularity, a pole of order $k$, and the residue.
- [ ] Q2 Compute $\oint z^n\,dz$ for $n \le -1$; treat $n = -1$ and $n \le -2$ separately.
- [ ] Q3 Combine with (c) into one formula valid for every integer $n$ (the problem's "table of integrals").
- [ ] Q4 **[why]** The problem says the result holds for any contour surrounding the pole. Which theorem lets you deform the circle, and what may the deformation not cross?
- [ ] Q5 Redo (a) the other way the problem suggests: integrate $1/z$ to $\log z$ and account for the jump across the branch cut on the negative real axis. What is the jump, and why is a cut a worse obstacle than a pole?

> [!tip]- Hint (d): route
> **Strategy (K13).** As in (c), with the one exponent where the integrand is constant.

#### (e)

For $I = \int_{-\infty}^\infty\frac{dx}{1 + x^2}$, close the contour with the upper semicircle $z = Re^{i\phi}$, $\phi \in [0, \pi]$, $R \to \infty$. Show that closing the contour does not change the value of the integral.

^ps4-1-e

- [ ] Q1 **[def]** State the ML inequality.
- [ ] Q2 Write the closed contour as the segment $[-L, L]$ plus the arc of radius $L$. Why take $L > 1$?
- [ ] Q3 Bound $|1 + L^2e^{2i\phi}|$ from below on the arc (reverse triangle inequality).
- [ ] Q4 Show that the arc integral tends to $0$. How fast must an integrand decay on the arc for this estimate to work?
- [ ] Q5 **[why]** For $\int\frac{e^{ikx}dx}{x^2 + 1}$ with $k > 0$, in which half-plane may you close, and which lemma is needed then that the ML estimate alone does not give?

> [!tip]- Hint (e): route
> **Strategy (K13).** Bound the arc by the ML inequality.

#### (f)

Decompose $\frac{1}{1 + z^2} = \frac{A}{z - z_0} + \frac{A'}{z - z_0'}$, where $z_0$, $z_0'$ are the two poles and $A$, $A'$ the residues.

^ps4-1-f

- [ ] Q1 Find the zeros of $1 + z^2$ and write the ansatz.
- [ ] Q2 Equate numerators and match powers of $z$; solve for $A$, $A'$.
- [ ] Q3 **[def]** Check $A$ against the residue formula $g(z_0)/h'(z_0)$ at a simple zero of the denominator.
- [ ] Q4 **[why]** What must $A + A'$ be, judging only from the behaviour of $1/(1 + z^2)$ at large $|z|$? Why?

> [!tip]- Hint (f): route
> **Strategy (K13).** Partial fractions by matching coefficients.

#### (g)

Evaluate $I$ using the results of (a)–(d).

^ps4-1-g

- [ ] Q1 Which pole does the closed contour of (e) enclose, and with which orientation?
- [ ] Q2 Shrink the contour to a small circle about that pole. Which theorem justifies it, and which radii keep the other pole outside?
- [ ] Q3 Evaluate the two partial-fraction pieces on the small circle: one by (a)/(d) with the centre shifted, the other by expanding it in nonnegative powers of $(z - z_0)$ and using (c).
- [ ] Q4 Assemble $I$, then check it in one line with the residue theorem.

> [!tip]- Hint (g): route
> **Strategy (K13).** Shrink the closed contour around the enclosed pole; use the table of (c)–(d).

#### (h)

It is equally justified to close the contour in the lower half-plane. Compute $I$ this way.

^ps4-1-h

- [ ] Q1 Write the lower closed contour so that the real segment still runs from $-L$ to $L$. What is its orientation?
- [ ] Q2 Show that the lower arc also vanishes as $L \to \infty$.
- [ ] Q3 **[conv]** Evaluate $I$. Which two minus signs appear (orientation, residue), and how do they combine?

> [!tip]- Hint (h): route
> **Strategy (K13).** As in (g), around the other pole, with the opposite orientation.

#### (i)

Evaluate $I$ by standard methods. (Hint: $x = \tan u$.)

^ps4-1-i

- [ ] Q1 Substitute $x = \tan u$: the range of $u$, and $dx$ in terms of $du$. Why is the substitution a bijection?
- [ ] Q2 Simplify the integrand and integrate.
- [ ] Q3 **[why]** For $\int\frac{dx}{x^2 + a^2}$, $a > 0$, how does the answer scale with $a$? Which residue produces that scaling?

> [!tip]- Hint (i): route
> **Strategy.** Substitution.

> [!tip]- Hints: definitions, results and your solution for the whole problem
> **Topic and definitions.** T6 (the tools of the propagator computations). Contour and contour integral Definition [[§CA.4 Contour Integration#^def-ca-4-1|§CA.4.1]] Contour; Contour Integral; analytic (holomorphic) function Definition [[§CA.4 Contour Integration#^def-ca-4-2|§CA.4.2]] Analytic Function; isolated singularity Definition [[§CA.4 Contour Integration#^def-ca-4-3|§CA.4.3]] Isolated Singularity; Laurent expansion, pole Definition [[§CA.4 Contour Integration#^def-ca-4-4|§CA.4.4]] Laurent Expansion; Removable Singularity, Pole and Essential Singularity; residue Definition [[§CA.4 Contour Integration#^def-ca-4-5|§CA.4.5]] Residue.
>
> **Key results.** Theorem [[§CA.4 Contour Integration#^thm-ca-4-1|§CA.4.1]] The ML Inequality and the Basic Integral (this problem, (a)–(d): the basic integral and the ML inequality); Example [[§CA.4 Contour Integration#^ex-ca-4-1|§CA.4.1]] Two Lorentzian Integrals (this problem, (e)–(i), for $1/(x^2 + a^2)$); Theorem [[§CA.4 Contour Integration#^thm-ca-4-2|§CA.4.2]] Cauchy's Theorem; Deformation of Contours (deformation of contours); Theorem [[§CA.4 Contour Integration#^thm-ca-4-4|§CA.4.4]] Computing Residues (computing residues); Theorem [[§CA.4 Contour Integration#^thm-ca-4-5|§CA.4.5]] Residue Theorem (residue theorem); Theorem [[§CA.4 Contour Integration#^thm-ca-4-6|§CA.4.6]] Closing the Contour: the ML Estimate and Jordan's Lemma (closing the contour); Theorem [[§CA.4 Contour Integration#^thm-ca-4-8|§CA.4.8]] Integrals around a Branch Cut (branch cuts); Theorem [[§CA.4 Contour Integration#^thm-ca-4-9|§CA.4.9]] Working Rules for Contour Integrals (working rules).
>
> **Difficulty** (a)–(d) 1, (e)–(i) 1. Submitted solution: every part from the definition $\int_C f\,dz = \int f(C(\phi))C'(\phi)\,d\phi$; (d) gives the single formula for all $n$; (e) by the reverse triangle inequality and an explicit bound on the arc; (g) and (h) shrink to a small circle and expand the other partial fraction in a geometric series, so the residue theorem itself is not quoted; (h) notes the two cancelling signs; (i) by $x = \tan u$. The vault's Example [[§CA.4 Contour Integration#^ex-ca-4-1|§CA.4.1]] Two Lorentzian Integrals does (e)–(i) for $1/(x^2 + a^2)$ by residues.

### PS4.2 Green's functions: the massless case

For the real scalar field define the Wightman function $D_W(x) \equiv \langle0|\phi(x)\phi(0)|0\rangle = \int\frac{d^3p}{(2\pi)^3}\frac{1}{2E_p}e^{-ipx}$ (8), the commutator function $iD(x) \equiv \langle0|[\phi(x), \phi(0)]|0\rangle$ (9) and the Hadamard function $D_1(x) \equiv \langle0|\{\phi(x), \phi(0)\}|0\rangle$ (10). PS write $D(x)$ for $D_W(x)$ and name no other function. Compute these functions for a massless field.

*Parts: (a), (b).*

^ps4-2

#### (a)

Compute $D_W(x)$ of (8) for a massless field, with the regulator $(t, \mathbf x) \to (t - i\epsilon, \mathbf x)$ so that the integrals converge. The result should hold for spacelike, timelike and null $x$.

^ps4-2-a

- [ ] Q1 **[def]** State $D_W$ as a vacuum expectation value and as a mode integral. What does $E_{\mathbf p}$ become for $m = 0$?
- [ ] Q2 Do the angular integrals: choose the polar axis, integrate the azimuth and $\cos\theta$. What single radial integral is left, and for which $r$ is the $\cos\theta$ step valid?
- [ ] Q3 **[why]** The radial integral does not converge as written. Show that $t \to t - i\epsilon$ makes it absolutely convergent. Why does $-i\epsilon$, and not $+i\epsilon$, damp it?
- [ ] Q4 Evaluate the two exponential integrals and combine them into one expression in $(t - i\epsilon)$ and $r$.
- [ ] Q5 Take $\epsilon \to 0$ off the light cone and write $D_W$ in terms of $x^2$. What is its sign at $t = 0$?
- [ ] Q6 **[why]** What happens on the light cone as $\epsilon \to 0$? In what sense is $D_W$ still defined there, and why must the $i\epsilon$ be kept in the formula?
- [ ] Q7 **[conv]** The problem set's $D_W$ is PS's $D$ (PS eq. (2.50)). Which object does the vault call $D$, and which name does Yu use for the commutator?

> [!tip]- Hint (a): route
> **Strategy (K13, K9).** Spherical coordinates with the polar axis along $\mathbf x$; angular integrals; the radial integral damped by $e^{-\epsilon\rho}$; combine the two terms before $\epsilon \to 0$.

#### (b)

Compute $D(x)$ and $D_1(x)$, for example from (a) with $\frac{1}{s - i\epsilon} = \frac{\mathcal P}{s} + i\pi\delta(s)$ (11), $s$ real, where the first term is real and odd and the second purely imaginary and even.

^ps4-2-b

- [ ] Q1 **[def]** Using that $\phi$ is Hermitian, express $\langle0|\phi(0)\phi(x)|0\rangle$ through $D_W(x)$, and then $D$ and $D_1$ through $\operatorname{Re}D_W$ and $\operatorname{Im}D_W$.
- [ ] Q2 Factor $(t - i\epsilon)^2 - r^2$ and split its inverse into partial fractions in $t$.
- [ ] Q3 **[def]** State the Sokhotski–Plemelj formula, including the sign of the $\delta$ term for $1/(s - i\epsilon)$ versus $1/(s + i\epsilon)$.
- [ ] Q4 Apply it at $s = t - r$ and at $s = t + r$, and read off $D$ and $D_1$.
- [ ] Q5 **[why]** Which of $D$, $D_1$ must be odd and which even under $x \to -x$, and why (translation invariance)? Check your results.
- [ ] Q6 Write $D$ covariantly with $\operatorname{sgn}(x^0)\,\delta(x^2)$ (compose $\delta$ with $x^2 = t^2 - r^2$). What are $D$ and $D_1$ off the light cone, and which principle does the value of $D$ there express?
- [ ] Q7 **[why]** Formula (11) is a statement about distributions in one real variable. In which variables is the limit taken here, and what does the vault's statement in $\mathcal S'(\mathbb R^4)$ add?

> [!tip]- Hint (b): route
> **Strategy (K13, K11).** Hermiticity gives $D$ and $D_1$ as the imaginary and real parts of $D_W$; partial fractions in $t$; Sokhotski–Plemelj at each sheet of the light cone.

> [!tip]- Hints: definitions, results and your solution for the whole problem
> **Topic and definitions.** T6. Wightman function Definition [[§C2b.2 The Wightman Function#^def-c2b-2-1|§C2b.2.1]] Wightman Function; commutator function Definition [[§C2b.4 Microcausality and the Commutator Function#^def-c2b-4-1|§C2b.4.1]] Commutator Function; Hadamard function Definition [[§C2b.4 Microcausality and the Commutator Function#^def-c2b-4-2|§C2b.4.2]] Hadamard Function; principal value Definition [[§CA.2 Generalized Functions#^def-ca-2-10|§CA.2.10]] Principal Value; names across sources [[§C2b.4 Microcausality and the Commutator Function#^cau-c2b-4-1|§C2b.4, Caution: One letter, four objects]].
>
> **Key results.** Theorem [[§C2b.2 The Wightman Function#^thm-c2b-2-1|§C2b.2.1]] The Wightman Function as a Mode Integral; Theorem [[§C2b.2 The Wightman Function#^thm-c2b-2-5|§C2b.2.5]] The Wightman Function Is a Boundary Value (the prescription $t \to t - i\varepsilon$ as a boundary value; this problem (a)); Theorem [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-5|§C2b.3.5]] The Wightman Function near the Light Cone (the massless function, exact for $m = 0$; this problem (a)); Theorem [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-6|§C2b.3.6]] The Wightman Function as a Distribution: Off the Cone and on It (as a distribution, off the cone and on it); Theorem [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-3|§C2b.4.3]] The Commutator and Hadamard Functions Are the Parts of the Wightman Function, Theorem [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-4|§C2b.4.4]] The Commutator and Hadamard Functions as Distributions (this problem); Theorem [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-8|§C2b.4.8]] Commutator and Hadamard Functions of the Massless Field (this problem (b)); Theorem [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-2|§CA.6.2]] Sokhotski–Plemelj Formula (eq. (11)); Theorem [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-4|§CA.6.4]] The Light-Cone Boundary Value (the light-cone boundary value); Theorem [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-8|§CA.3.8]] Angular Integrals (angular integrals).
>
> **Difficulty** (a) 2, (b) 2. Submitted solution: (a) the explicit spherical integral with the damping $e^{-\epsilon\rho}$, both terms combined at finite $\epsilon$, then three cases (timelike or spacelike: an ordinary real function; null: grows like $1/\epsilon$, defined only as a generalized function). (b) $D = 2\operatorname{Im}D_W$, $D_1 = 2\operatorname{Re}D_W$ from hermiticity; exact partial fractions at $\epsilon > 0$, real and imaginary parts at $\epsilon > 0$ with a parity check, then (11) "as distributions in $t$" at fixed $r > 0$; the results agree with Theorem [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-8|§C2b.4.8]] Commutator and Hadamard Functions of the Massless Field. The vault states the limit in $\mathcal S'(\mathbb R^4)$ through the light-cone boundary value Theorem [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-4|§CA.6.4]] The Light-Cone Boundary Value.

### PS4.3 Green's functions: explicit expressions for massive fields

*Parts: (a), (b).*

^ps4-3

#### (a)

For a free scalar field of mass $m$, introduce radial coordinates and show that, for spacelike $x$ with $x^2 = -r^2$,
$D_W(r) = -\frac{i}{2(2\pi)^2r}\int_0^\infty dp\,\frac{p}{\sqrt{p^2 + m^2}}\bigl(e^{ipr} - e^{-ipr}\bigr)$ (12).
The integral is ambiguous; the prescription is to evaluate $e^{ipr}$ ($e^{-ipr}$) with $r \to r + i\epsilon$ ($r \to r - i\epsilon$), so that the exponential is damped, and take $\epsilon \to 0$ afterwards. Show that then $D_W(x) = \frac{m}{4\pi^2\sqrt{-x^2}}K_1\bigl(m\sqrt{-x^2}\bigr)$ (13).

^ps4-3-a

- [ ] Q1 **[why]** Why may $D_W$ at spacelike $x$ be computed in a frame where $x^0 = 0$? Name the two facts used (invariance of the measure and of $D_W$; the orbit of a spacelike vector).
- [ ] Q2 Do the angular integral and obtain (12). Why does the radial integral in (12) not converge?
- [ ] Q3 Apply the prescription: write the two damped integrals and check that they converge absolutely for $\epsilon > 0$.
- [ ] Q4 Substitute $p = m\sinh v$. Write the integrand with $\sin(mr\sinh v)$ and express it as $-\partial_r$ of a cosine integral $F_\epsilon(r)$.
- [ ] Q5 **[def]** Which integral representation of $K_0$, and which derivative identity between $K_0$ and $K_1$, finish the computation? Is that representation of $K_0$ absolutely convergent?
- [ ] Q6 **[why]** The computation takes $\epsilon \to 0$ in $F_\epsilon$ and then differentiates in $r$. Which exchange is this, and what extra estimate makes it legitimate?
- [ ] Q7 **[conv]** Is the damping $e^{-\epsilon p}$ of this prescription the same as the covariant $t \to t - i\epsilon$ of Problem 2? Why does the difference not matter at spacelike $x$?

> [!tip]- Hint (a): route
> **Strategy (K14, K1, K13).** Go to a frame with $x^0 = 0$; angular integral; damp; substitute $p = m\sinh v$; write the sine as an $r$-derivative of a cosine integral, recognize $K_0$, and use $K_0' = -K_1$.

#### (b)

Compute the commutator and Hadamard functions from the Wightman function at spacelike $x$. Then determine their behaviour at large distance, including the overall prefactor that is a power of $r$.

^ps4-3-b

- [ ] Q1 Express $D$ and $D_1$ through $D_W$ as in Problem 2(b). Why does that relation hold for $m > 0$ as well?
- [ ] Q2 **[def]** Show from an integral representation that $K_1(z)$ is real and positive for real $z > 0$.
- [ ] Q3 Conclude $D$ and $D_1$ at spacelike $x$. Which principle does the value of $D$ express?
- [ ] Q4 **[def]** State the large-argument expansion of $K_\nu$, with its first correction for $\nu = 1$.
- [ ] Q5 Obtain the large-$r$ behaviour of $D_1$ with its full prefactor (power of $r$ and constants). What sets the decay length?
- [ ] Q6 **[why]** At spacelike separation $D$ vanishes but $D_1$ does not. What does each function measure?

> [!tip]- Hint (b): route
> **Strategy (K14).** $D_W$ is real at spacelike $x$, so $D$ and $D_1$ follow at once; the large-argument expansion of $K_1$.

> [!tip]- Hints: definitions, results and your solution for the whole problem
> **Topic and definitions.** T6 (T1 for the choice of frame). Wightman, commutator and Hadamard functions Definition [[§C2b.2 The Wightman Function#^def-c2b-2-1|§C2b.2.1]] Wightman Function, Definition [[§C2b.4 Microcausality and the Commutator Function#^def-c2b-4-1|§C2b.4.1]] Commutator Function, Definition [[§C2b.4 Microcausality and the Commutator Function#^def-c2b-4-2|§C2b.4.2]] Hadamard Function; modified Bessel function $K_\nu$ Definition [[§CA.5 Gaussian Integrals, Stationary Phase and Bessel Functions#^def-ca-5-1|§CA.5.1]] Modified Bessel Function of the Second Kind.
>
> **Key results.** Theorem [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-3|§C2b.3.3]] The Wightman Function at Spacelike Separation (this problem (a); its third derivation route, "real variables only", is this computation); Theorem [[§C2b.2 The Wightman Function#^thm-c2b-2-3|§C2b.2.3]] Lorentz Invariance of the Wightman Function (Lorentz invariance of $D_W$); Theorem [[§C1a.4 The Lorentz Group#^thm-c1a-4-2|§C1a.4.2]] The Orbits of SO⁺(1,3) on Spacetime (orbits: a spacelike vector has an equal-time frame); Theorem [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-3|§C2a.4.3]] The Invariant Measure (the invariant measure); Theorem [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-8|§CA.3.8]] Angular Integrals; Theorem [[§CA.5 Gaussian Integrals, Stationary Phase and Bessel Functions#^thm-ca-5-3|§CA.5.3]] Properties of $K_\nu$, Theorem [[§CA.5 Gaussian Integrals, Stationary Phase and Bessel Functions#^thm-ca-5-4|§CA.5.4]] Further Representations; Imaginary Argument (properties and representations of $K_\nu$); Theorem [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|§CA.1.1]] Dominated Convergence and Differentiation under the Integral, Theorem [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-2|§CA.1.2]] Conditionally Convergent Integrals: Dirichlet's Test and Abel's Theorem, Theorem [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-3|§CA.1.3]] Limits of Derivatives (exchanging limits, derivatives and integrals); for (b): Theorem [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-3|§C2b.4.3]] The Commutator and Hadamard Functions Are the Parts of the Wightman Function, Theorem [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-5|§C2b.4.5]] The Free Field Is Microcausal (microcausality), Theorem [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-9|§C2b.4.9]] Commutator and Hadamard Functions of the Massive Field (this problem (b)), [[§C2b.4 Microcausality and the Commutator Function#^rem-c2b-4-3|§C2b.4, Remark: Influence and correlation]] (this problem (b)).
>
> **Difficulty** (a) 3, (b) 1. Submitted solution: (a) the equal-time frame from the Lorentz invariance of $d^3p/(2\pi)^32E_{\mathbf p}$ (citing Problem Set 3, Problem 1), the angular integral, the damping $e^{-p\epsilon}$, $p = mu$ then $u = \sinh v$, $F_\epsilon$, $F_\epsilon \to K_0(mr)$ (AS 9.6.21) and $K_0' = -K_1$ (AS 9.6.27). This is the third route of Theorem [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-3|§C2b.3.3]] The Wightman Function at Spacelike Separation, except that the vault proves that the limit may be taken after the $r$-derivative (Step 4, a uniform-convergence estimate) and quotes Abel's theorem for $F_\epsilon \to K_0$; the submission takes the limit of $F_\epsilon$ and then differentiates without comment. (b) reality of $K_1$ from AS 9.6.24, the asymptotic form from AS 9.7.2; the large-distance form agrees with [[§C2b.4 Microcausality and the Commutator Function#^rem-c2b-4-3|§C2b.4, Remark: Influence and correlation]].

### PS4.4 The Feynman propagator

*Parts: (a), (b), (c).*

^ps4-4

#### (a)

Expand a free scalar field $\phi$ in the oscillators $a_p$, $a_p^\dagger$ and show that $\langle0|T(\phi(x)\phi(y))|0\rangle = \theta(x^0 - y^0)D_W(x - y) + \theta(y^0 - x^0)D_W(y - x)$, where $D_W(x - y) = \int\frac{d^3p}{(2\pi)^3}\frac{1}{2E_p}e^{-ip(x - y)}$.

^ps4-4-a

- [ ] Q1 **[def]** Write the mode expansion of the free real field and the commutator $[a_{\mathbf p}, a^\dagger_{\mathbf q}]$ with its $(2\pi)^3$; state how $a_{\mathbf p}$ and $a^\dagger_{\mathbf p}$ act on $|0\rangle$ and $\langle0|$.
- [ ] Q2 Insert the expansion into $\langle0|\phi(x)\phi(y)|0\rangle$. Which three of the four terms vanish, and why?
- [ ] Q3 Commute the surviving term to evaluate it, and do the $\mathbf q$ integral. What sets $q^0$ once $\mathbf q = \mathbf p$?
- [ ] Q4 **[def]** Define $T(\phi(x)\phi(y))$ with step functions. Why can the step functions be taken out of the vacuum expectation value?
- [ ] Q5 **[conv]** What value of $\theta(0)$ does the vault use, and why is the choice harmless for $\phi\phi$ at equal times? Which earlier problem set uses another value?

> [!tip]- Hint (a): route
> **Strategy (K9, K11).** Insert the modes, kill three of the four terms on the vacuum, commute the fourth.

#### (b)

Show that the Wightman function satisfies the homogeneous Klein–Gordon equation.

^ps4-4-b

- [ ] Q1 Compute $\partial^2e^{-ip\cdot x}$ for fixed $p$, keeping track of index positions.
- [ ] Q2 **[why]** Why is $p^2 = m^2$ for every term of the integral? What would fail if $p^0$ were an independent integration variable?
- [ ] Q3 Pass $\partial^2$ through the integral and conclude. What justifies this, given that the integral converges absolutely for no real argument?
- [ ] Q4 **[conv]** Acting on $e^{-ip\cdot x}$, does $\partial^2 + m^2$ give the factor $p^2 + m^2$ or $m^2 - p^2$? Check with $\partial_t^2 - \nabla^2 + m^2$.

> [!tip]- Hint (b): route
> **Strategy (K9).** Differentiate under the integral; on-shell $p^0$.

#### (c)

With $D_F(x - y) \equiv \langle0|T(\phi(x)\phi(y))|0\rangle$, show that the Feynman propagator is a Green's function: it satisfies the Klein–Gordon equation with a $\delta$-function source. (Hint: use $iD(x - y) = D_W(x - y) - D_W(y - x) = [\phi(x), \phi(y)]$.)

^ps4-4-c

- [ ] Q1 **[def]** State what "Green's function" means here, with the vault's normalization of the $\delta^4$ source.
- [ ] Q2 Apply $\partial^2$ to $\theta(x^0 - y^0)D_W(x - y)$ (the spatial derivatives do not touch $\theta$). Which terms carry $\delta$, and which $\partial_0\delta$?
- [ ] Q3 Show that the terms without $\delta$'s cancel by (b). What must you check for $D_W(y - x)$ as a function of $x$?
- [ ] Q4 Collect the $\delta$ terms into $iD$ and $\partial_0(iD)$. Show that $\partial_{x^0}[\phi(x), \phi(y)] = [\pi(x), \phi(y)]$.
- [ ] Q5 **[why]** Rewrite $(\partial_0\delta)\,iD$ with the product rule. Why does $\delta(x^0 - y^0)\,iD(x - y)$ vanish while $\delta(x^0 - y^0)\,\partial_0iD(x - y)$ does not?
- [ ] Q6 Use the equal-time canonical commutator to finish. What is the right-hand side, sign and factor included?
- [ ] Q7 **[why]** For $\langle T\{\phi(x)\phi(y_1)\cdots\phi(y_n)\}\rangle$-type products, what does $\partial_x^2 + m^2$ give, and where do the $\delta$'s come from?

> [!tip]- Hint (c): route
> **Strategy (K11, K13).** Product rule on $\theta\cdot D_W$; contact terms from $\partial_0\theta = \pm\delta$; equal-time commutators.

> [!tip]- Hints: definitions, results and your solution for the whole problem
> **Topic and definitions.** T6 (T5 for the mode expansion). Time-ordered product Definition [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^def-c2b-6-1|§C2b.6.1]] Time-Ordered Product; Wightman function Definition [[§C2b.2 The Wightman Function#^def-c2b-2-1|§C2b.2.1]] Wightman Function; commutator function Definition [[§C2b.4 Microcausality and the Commutator Function#^def-c2b-4-1|§C2b.4.1]] Commutator Function; Green's function of the Klein–Gordon operator Definition [[§C2b.5 Green's Functions and Contours#^def-c2b-5-1|§C2b.5.1]] Green's Function of the Klein–Gordon Operator; equal-time commutators Principle [[§C2a.1 Canonical Quantization of Fields#^pr-c2a-1-2|§C2a.1.2]] Equal-Time Canonical Commutation Relations.
>
> **Key results.** Theorem [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-2|§C2a.2.2]] Mode Expansion of the Real Field (mode expansion); Theorem [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|§C2a.2.6]] The Mode Algebra (mode algebra); Theorem [[§C2b.2 The Wightman Function#^thm-c2b-2-1|§C2b.2.1]] The Wightman Function as a Mode Integral (this problem (a)); Theorem [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-2|§C2b.6.2]] The Feynman Propagator (this problem (a)); Theorem [[§C2b.2 The Wightman Function#^thm-c2b-2-4|§C2b.2.4]] The Wightman Function Is a Homogeneous Solution; Reversal Is Conjugation (this problem (b)); Theorem [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-5|§C2b.6.5]] The Free Schwinger–Dyson Equation (this problem (c); its derivation names this route); Theorem [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-2|§C2b.4.2]] The Field Commutator Is a c-Number; Theorem [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-10|§C2b.4.10]] Commutators at Unequal Times; Theorem [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-1|§C2b.6.1]] Properties of Time Ordering; Theorem [[§CA.2 Generalized Functions#^thm-ca-2-4|§CA.2.4]] Every Generalized Function Is Differentiable; [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^cau-c2b-6-1|§C2b.6, Caution: The step function at zero]]; [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^cau-c2b-6-2|§C2b.6, Caution: Signs that slip]].
>
> **Difficulty** (a) 1, (b) 1, (c) 2. Submitted solution: (a) the full double mode integral, vacuum annihilation on both sides, one commutator, then the step-function form; $\theta(0)$ is not discussed. (b) an index-by-index computation of $\partial^2e^{-ipx}$ and the on-shell condition. (c) both time derivatives at once with the product rule, cancellation of the non-contact terms by (b) (with the remark that $\partial_x^2 = \partial_z^2$ for $z = y - x$), $\partial_0$ of the commutator as $[\pi(x), \phi(y)]$, and the contact term handled by $(\partial_0\delta)\,iD = \partial_0(\delta\,iD) - \delta\,\partial_0(iD)$. The vault's derivation of Theorem [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-5|§C2b.6.5]] The Free Schwinger–Dyson Equation takes one time derivative at a time and names this as the route of Problem Set 4, Problem 4(c).

### PS4.5 Lorentz algebra

*Parts: (a), (b), (c).*

^ps4-5

#### (a)

The vector-representation generators are given by PS (3.18) as $(\mathcal J^{\rho\sigma})_{\mu\nu} = i(\delta^\rho_\mu\delta^\sigma_\nu - \delta^\rho_\nu\delta^\sigma_\mu)$, with matrix multiplication $(AB)_{\alpha\gamma} = A_{\alpha\beta}B^\beta{}_\gamma$; equivalently, in mixed form, $(\mathcal J^{\rho\sigma})^\mu{}_\nu = i(g^{\rho\mu}\delta^\sigma_\nu - g^{\sigma\mu}\delta^\rho_\nu)$ (14). Using either form, verify the Lorentz algebra $[\mathcal J^{\mu\nu}, \mathcal J^{\rho\sigma}] = i(g^{\nu\rho}\mathcal J^{\mu\sigma} - g^{\mu\rho}\mathcal J^{\nu\sigma} - g^{\nu\sigma}\mathcal J^{\mu\rho} + g^{\mu\sigma}\mathcal J^{\nu\rho})$ (15).

^ps4-5-a

- [ ] Q1 **[def]** Write the mixed-index generators (14). Which index pair labels the generator, and which pair is the matrix entry?
- [ ] Q2 **[conv]** PS's (3.18) has both matrix indices down. Raise one with $g$ and show it gives (14). Why is the lower-lower array not itself the matrix that acts on $v^\beta$?
- [ ] Q3 Strip the $i$'s ($\mathcal J = iM$) and compute $(M^{\mu\nu}M^{\rho\sigma})^\alpha{}_\beta$ by contracting the deltas.
- [ ] Q4 Obtain the second product $M^{\rho\sigma}M^{\mu\nu}$ by relabelling rather than recomputing. Which exchange of labels?
- [ ] Q5 Pair the eight terms of the commutator so that each pair is a component of one $M$ with free indices $\alpha$, $\beta$; use the antisymmetry of $M$ in its labels to reach the order of (15).
- [ ] Q6 **[why]** Restore the $i$'s: why does the overall $i^2$ on the left become a single $i$ on the right of (15)?
- [ ] Q7 Check one instance: compute $[\mathcal J^{12}, \mathcal J^{23}]$ from (15). Which generator results, and is it a rotation?

> [!tip]- Hint (a): route
> **Strategy (K3, K2).** Mixed form, $\mathcal J = iM$, contract the deltas, pair the eight terms.

#### (b)

Verify $[\gamma^\mu, S^{\rho\sigma}] = (\mathcal J^{\rho\sigma})^\mu{}_\nu\gamma^\nu$ with the vector matrices (14) and the spinor generators $S^{\mu\nu} = \frac i4[\gamma^\mu, \gamma^\nu]$. You will need $\{\gamma^\mu, \gamma^\nu\} = 2g^{\mu\nu}$ and may use $[A, BC] = \{A, B\}C - B\{A, C\}$.

^ps4-5-b

- [ ] Q1 **[def]** State the Clifford relation and the definition of $S^{\mu\nu}$.
- [ ] Q2 Prove the reordering identity $[A, BC] = \{A, B\}C - B\{A, C\}$.
- [ ] Q3 Apply it to $\bigl[\gamma^\mu, [\gamma^\rho, \gamma^\sigma]\bigr]$. Why may the anticommutators be moved freely in the products?
- [ ] Q4 Compare with $(\mathcal J^{\rho\sigma})^\mu{}_\nu\gamma^\nu$ from (14). Which symmetry of $g$ is used?
- [ ] Q5 **[why]** Read the identity as the infinitesimal form of $\Lambda_{1/2}^{-1}\gamma^\mu\Lambda_{1/2} = \Lambda^\mu{}_\nu\gamma^\nu$. Where is that statement used later (which equation becomes covariant)?

> [!tip]- Hint (b): route
> **Strategy (K5, K11).** The reordering identity turns every commutator into anticommutators.

#### (c)

Show that the spinor generators satisfy the Lorentz algebra (15).

^ps4-5-c

- [ ] Q1 Write $[S^{\mu\nu}, S^{\rho\sigma}] = \frac i4\bigl[\,[\gamma^\mu, \gamma^\nu], S^{\rho\sigma}\bigr]$ and expand with $[AB, C] = A[B, C] + [A, C]B$.
- [ ] Q2 Insert (b) and write out the eight terms.
- [ ] Q3 Pair the terms into commutators of two $\gamma$'s and convert each into an $S$.
- [ ] Q4 Use the antisymmetry of $S$ and the symmetry of $g$ to reach the order of (15).
- [ ] Q5 **[why]** Why does (c) follow from (b) with no further Clifford algebra? What structure does (b) express?
- [ ] Q6 **[conv]** With PS's $\sigma^{\mu\nu} = \frac i2[\gamma^\mu, \gamma^\nu]$, what is $S^{\mu\nu}$ in terms of $\sigma^{\mu\nu}$? Which other normalization appears in Problem Set 5?

> [!tip]- Hint (c): route
> **Strategy (K5, K11).** Expand with $[AB, C] = A[B, C] + [A, C]B$, insert (b), pair into commutators.

> [!tip]- Hints: definitions, results and your solution for the whole problem
> **Topic and definitions.** T7. Generators of the vector representation Definition [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-1|§C1a.6.1]] Generators of the Vector Representation (the same as Definition [[§CB.5 The Lorentz Algebra꞉ Generators and Commutation Relations#^def-cb-5-2|§CB.5.2]] The Generators of the Vector Representation); representation of the Lorentz algebra Definition [[§CB.5 The Lorentz Algebra꞉ Generators and Commutation Relations#^def-cb-5-7|§CB.5.7]] Representation of the Lorentz Algebra; Dirac matrices Definition [[§CB.11 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^def-cb-11-11|§CB.11.11]] The Dirac Matrices; spinor generators Definition [[§CB.14 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-14-16|§CB.14.16]] The Spinor Generators; the two roles of the indices [[§C3.1 Index Slots, Rotations and Spin in Field Theory#^cau-c3-1-1|§C3.1, Caution: Four spacetime indices in two roles]]; one symbol per realization [[§C3.1 Index Slots, Rotations and Spin in Field Theory#^rem-c3-1-1|§C3.1, Remark: One symbol for each realization of the generators]].
>
> **Key results.** Theorem [[§CB.5 The Lorentz Algebra꞉ Generators and Commutation Relations#^thm-cb-5-6|§CB.5.6]] The Lorentz Algebra (the Lorentz algebra; (a) as the user wrote it is [[§CB.5 The Lorentz Algebra꞉ Generators and Commutation Relations#^der-cb-5-6b|Derivation §CB.5.6, second route]]); Theorem [[§CB.14 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-14-17|§CB.14.17]] The Dirac Matrices Rotate as a Vector (this problem (b)); Theorem [[§CB.14 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-14-18|§CB.14.18]] The Spinor Generators Obey the Lorentz Algebra (this problem (c)); Theorem [[§CB.11 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^thm-cb-11-12|§CB.11.12]] First Consequences of the Clifford Algebra; [[§CB.5 The Lorentz Algebra꞉ Generators and Commutation Relations#^rem-cb-5-1|§CB.5, Remark: Where the Lorentz algebra is derived]] (where the algebra is derived).
>
> **Difficulty** (a) 2, (b) 1, (c) 2. Submitted solution: (a) the mixed form with $\mathcal J = iM$, all eight terms written out and paired so that $\alpha$, $\beta$ stay free, kept in the vault as [[§CB.5 The Lorentz Algebra꞉ Generators and Commutation Relations#^der-cb-5-6b|Derivation §CB.5.6, second route]]; (b) the reordering relation, as in Theorem [[§CB.14 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-14-17|§CB.14.17]] The Dirac Matrices Rotate as a Vector; (c) the product rule for commutators and (b), as in Theorem [[§CB.14 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-14-18|§CB.14.18]] The Spinor Generators Obey the Lorentz Algebra.

## Problem Set 5: Spin ½ Particles (due Oct 4)

### PS5.1 Representations of SO(1,3)

(Based on PS Problem 3.1(a)–(b).) The generators $J^{\mu\nu} = -J^{\nu\mu}$ satisfy $[J^{\mu\nu}, J^{\rho\sigma}] = i(g^{\nu\rho}J^{\mu\sigma} - g^{\mu\rho}J^{\nu\sigma} - g^{\nu\sigma}J^{\mu\rho} + g^{\mu\sigma}J^{\nu\rho})$ (1). Define $L^i = \frac12\epsilon^{ijk}J^{jk}$, $K^i = J^{i0}$ (2), so that an infinitesimal Lorentz transformation acts on a field as $\Phi \to (1 - i\boldsymbol\theta\cdot\mathbf L - i\boldsymbol\beta\cdot\mathbf K)\Phi$ (3), with rotation angles $\boldsymbol\theta$ and boost parameters $\boldsymbol\beta$.

*Parts: (a), (b).*

^ps5-1

#### (a)

Use (1) to compute $[L^i, L^j]$, $[L^i, K^j]$ and $[K^i, K^j]$. Then show that $\mathbf J_\pm = \frac12(\mathbf L \pm i\mathbf K)$ (4) commute with one another, $[J^i_+, J^j_-] = 0$, and that each satisfies $[J^i_\pm, J^j_\pm] = i\epsilon^{ijk}J^k_\pm$ (5).

^ps5-1-a

- [ ] Q1 **[def]** Write $L^i$ and $K^i$ in terms of $J^{\mu\nu}$ as the problem set does and as the vault does. Invert the first: express $J^{jk}$ through $\mathbf L$.
- [ ] Q2 Compute $[L^i, L^j]$ from (1). Which metric components appear, and which $\varepsilon\varepsilon$ contraction reduces each of the four terms?
- [ ] Q3 Compute $[L^i, K^j]$ and $[K^i, K^j]$. Which components of $g$ make terms drop out?
- [ ] Q4 **[conv]** Redo Q3 with the vault's $K_i = \mathcal J^{0i}$. Which of the three commutators change sign? Explain from how each one depends on $\mathbf K$.
- [ ] Q5 Form $\mathbf J_\pm$ and show $[J^i_+, J^j_-] = 0$ term by term.
- [ ] Q6 Show $[J^i_\pm, J^j_\pm] = i\epsilon^{ijk}J^k_\pm$.
- [ ] Q7 **[why]** The split needs the complex combinations $\mathbf L \pm i\mathbf K$. Which sign in Q3 rules out a real split, and in which algebra do $\mathbf J_\pm$ live? Why is the change of basis $(\mathbf L, \mathbf K) \leftrightarrow (\mathbf J_+, \mathbf J_-)$ invertible?

> [!tip]- Hint (a): route
> **Strategy (K3, K2).** Spatial metric $g^{ab} = -\delta^{ab}$, one $\varepsilon\varepsilon$ contraction per term, then bilinearity for the $\mathbf J_\pm$.

#### (b)

The finite-dimensional representations of the rotation algebra are labelled by $j = 0, \frac12, 1, \dots$; by (a) those of the Lorentz algebra are labelled by a pair $(j_+, j_-)$, of dimension $(2j_+ + 1)(2j_- + 1)$. Using $\mathbf J = \frac12\boldsymbol\sigma$ in spin $\frac12$, write (3) explicitly for the two-component objects in $(\frac12, 0)$ and $(0, \frac12)$, and show that they reproduce the left- and right-handed Weyl spinors of PS, $\psi_L \to (1 - i\boldsymbol\theta\cdot\frac{\boldsymbol\sigma}2 - \boldsymbol\beta\cdot\frac{\boldsymbol\sigma}2)\psi_L$, $\psi_R \to (1 - i\boldsymbol\theta\cdot\frac{\boldsymbol\sigma}2 + \boldsymbol\beta\cdot\frac{\boldsymbol\sigma}2)\psi_R$ (6).

^ps5-1-b

- [ ] Q1 **[def]** Define the representation $(j_+, j_-)$: what acts on which tensor factor, and what is its dimension?
- [ ] Q2 Invert (4): write $\mathbf L$ and $\mathbf K$ through $\mathbf J_\pm$, and rewrite (3) in terms of $\mathbf J_\pm$.
- [ ] Q3 **[why]** Why must all generators vanish on a one-dimensional (spin-$0$) space?
- [ ] Q4 Substitute $(\frac12, 0)$ and $(0, \frac12)$ and compare with (6).
- [ ] Q5 **[conv]** With the vault's $K_i = \mathcal J^{0i}$: how are the problem set's $\mathbf J_\pm$ related to the vault's $\mathbf J_\pm$, and the problem set's $\boldsymbol\beta$ to the vault's rapidity $\boldsymbol\eta$? Which vault label, $(\frac12, 0)$ or $(0, \frac12)$, does the problem set's $(\frac12, 0)$ carry?
- [ ] Q6 **[conv]** Eq. (6) quotes PS (3.37), where $\boldsymbol\beta$ belongs to PS's $K^i = J^{0i}$. Reading $\boldsymbol\beta$ as PS's boost parameter, which of PS's $\psi_L$, $\psi_R$ transforms like the problem set's $(\frac12, 0)$? Does anything physical depend on the labels?
- [ ] Q7 **[why]** Exponentiate the two laws for a boost along $z$. Which factors are not unitary, and why can no finite-dimensional representation of the Lorentz group make boosts unitary?

> [!tip]- Hint (b): route
> **Strategy (K16, K4).** Invert (4), substitute the spin-$\frac12$ and spin-$0$ matrices.

> [!tip]- Hints: definitions, results and your solution for the whole problem
> **Topic and definitions.** T7. Rotation and boost generators Definition [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-2|§C1a.6.2]] Rotation and Boost Generators (the vault's $K_i = \mathcal J^{0i}$; the same as Definition [[§CB.5 The Lorentz Algebra꞉ Generators and Commutation Relations#^def-cb-5-4|§CB.5.4]] Rotation and Boost Generators); representation of the Lorentz algebra Definition [[§CB.5 The Lorentz Algebra꞉ Generators and Commutation Relations#^def-cb-5-7|§CB.5.7]] Representation of the Lorentz Algebra; the representation $(j_+, j_-)$ Definition [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^def-cb-17-3|§CB.17.3]] The Representation (j₊, j₋); Weyl and Dirac fields Definition [[§C3.3 How Fields Transform under the Lorentz Group#^def-c3-3-2|§C3.3.2]] Spinor Fields.
>
> **Key results.** Theorem [[§CB.5 The Lorentz Algebra꞉ Generators and Commutation Relations#^thm-cb-5-6|§CB.5.6]] The Lorentz Algebra (the $\mathbf J$, $\mathbf K$ form); [[§CB.5 The Lorentz Algebra꞉ Generators and Commutation Relations#^der-cb-5-6c|Derivation §CB.5.6, the J, K form and the J± split]] (this problem (a), as the user wrote it, rewritten with $K_i = \mathcal J^{0i}$); Theorem [[§CB.6 The Lorentz Algebra꞉ the Split J±, Real Forms and 𝔰𝔩(2,ℂ) as a Real Lie Algebra#^thm-cb-6-1|§CB.6.1]] The Split of the Complexified Lorentz Algebra, Theorem [[§CB.6 The Lorentz Algebra꞉ the Split J±, Real Forms and 𝔰𝔩(2,ℂ) as a Real Lie Algebra#^thm-cb-6-2|§CB.6.2]] A Representation of the Lorentz Algebra Is a Pair of Commuting Angular Momenta (the split and its converse); Theorem [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^thm-c3-2-1|§C3.2.1]] The Representations (½, 0) and (0, ½) (this problem (b), converted to the vault's convention); [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^cau-c3-2-2|§C3.2, Caution: Which one is (½, 0) depends on the sign of K]] (which one is $(\frac12, 0)$ depends on the sign of $\mathbf K$); Theorem [[§CB.5 The Lorentz Algebra꞉ Generators and Commutation Relations#^thm-cb-5-9|§CB.5.9]] One-Dimensional Representations of the Lorentz Algebra Are Zero, Theorem [[§C3.3 How Fields Transform under the Lorentz Group#^thm-c3-3-4|§C3.3.4]] A One-Component Field Carries the Trivial Representation (spin $0$: generators vanish); Theorem [[§CB.10 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-10-3|§CB.10.3]] The Irreducible Representations of the Rotation Algebra (Highest Weight) (spin $j$); Theorem [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-17-6|§CB.17.6]] Every Finite-Dimensional Representation Is a Sum of (j₊, j₋); Theorem [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-2|§C5a.3.2]] The Dirac Representation Is (½, 0) ⊕ (0, ½); Theorem [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-3|§C1a.5.3]] Contraction Identities of the Levi-Civita Symbol ($\varepsilon$ contractions).
>
> **Difficulty** (a) 2, (b) 2. Submitted solution: (a) in the problem set's convention ($K^i = J^{i0}$), each of the four terms of $[L^i, L^j]$ reduced to $J^{ij}$ with $\varepsilon^{abc}\varepsilon^{ade}$, then the three boxed commutators and the $\mathbf J_\pm$ relations by bilinearity; the vault keeps it as [[§CB.5 The Lorentz Algebra꞉ Generators and Commutation Relations#^der-cb-5-6c|Derivation §CB.5.6, the J, K form and the J± split]] with $K_i = \mathcal J^{0i}$. (b) inversion of (4), the remark that the $\mathbf J_\pm$ relations are equivalent to (1), spin $0$ forcing $\mathbf J = 0$ because numbers commute (kept in Theorem [[§CB.5 The Lorentz Algebra꞉ Generators and Commutation Relations#^thm-cb-5-9|§CB.5.9]] One-Dimensional Representations of the Lorentz Algebra Are Zero), and the substitution. The result is right within the statement's convention; the statement itself pairs $K^i = J^{i0}$ with PS's (3.37), whose $\boldsymbol\beta$ goes with $K = J^{0i}$ (`ERRATA.md`), and the vault states the converted table in Theorem [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^thm-c3-2-1|§C3.2.1]] The Representations (½, 0) and (0, ½) with [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^cau-c3-2-2|§C3.2, Caution: Which one is (½, 0) depends on the sign of K]].

### PS5.2 Contraction identities

Let $k$, $p$, $q$ be arbitrary four-vectors. Using the anticommutation relations of the Dirac matrices, prove the identities (a)–(d) below, with $\slashed{k} = k^\mu\gamma_\mu$ ("kay-slash") and similarly for other vectors. They are PS (5.8)–(5.9), needed for Feynman diagrams with spin-$\frac12$ particles.

*Parts: (a), (b), (c), (d).*

^ps5-2

#### (a)

$\gamma_\mu\gamma^\mu = 4$.

^ps5-2-a

- [ ] Q1 **[def]** State the Clifford relation. What is $\gamma_\mu$ in terms of $\gamma^\mu$ for $\mu = 0$ and for $\mu = i$?
- [ ] Q2 Compute $(\gamma^0)^2$ and $(\gamma^i)^2$ from the Clifford relation alone.
- [ ] Q3 Sum over $\mu$. **[why]** Where does the dimension of spacetime enter, and what is $\gamma_\mu\gamma^\mu$ in $d$ dimensions?

> [!tip]- Hint (a): route
> **Strategy (K5).** Square each $\gamma$ with the Clifford relation and sum.

#### (b)

$\gamma_\mu\slashed{k}\gamma^\mu = -2\slashed{k}$.

^ps5-2-b

- [ ] Q1 **[def]** Define $\slashed{k}$. Why may the components $k^\nu$ be moved through the $\gamma$'s?
- [ ] Q2 Short route: anticommute $\gamma^\mu$ past $\gamma_\nu$ in $\gamma_\mu\gamma_\nu\gamma^\mu$ and use (a).
- [ ] Q3 Component route: split $\mu$ into $0$ and $i$, and in each spatial term find which components of $\slashed{k}$ anticommute with $\gamma^i$ and which commute.
- [ ] Q4 **[why]** Redo the short route in $d$ dimensions. Which number replaces $-2$?

> [!tip]- Hint (b): route
> **Strategy (K5).** One anticommutation and (a); or component by component.

#### (c)

$\gamma_\mu\slashed{p}\slashed{q}\gamma^\mu = 4\,p\cdot q$.

^ps5-2-c

- [ ] Q1 Anticommute the $\gamma$ of $\slashed{q}$ past $\gamma^\mu$ (Clifford relation with one index lowered). Which two terms appear?
- [ ] Q2 Reduce them with (a) and (b).
- [ ] Q3 Recombine $\slashed{p}\slashed{q} + \slashed{q}\slashed{p}$. Which slash identity is that?
- [ ] Q4 **[why]** Why is the result a multiple of the identity matrix?

> [!tip]- Hint (c): route
> **Strategy (K5).** Move the last $\gamma$ through $\gamma^\mu$, then (a), (b).

#### (d)

$\gamma_\mu\slashed{k}\slashed{p}\slashed{q}\gamma^\mu = -2\slashed{q}\slashed{p}\slashed{k}$.

^ps5-2-d

- [ ] Q1 Anticommute $\gamma^\mu$ to the left past $\slashed{q}$. Which two terms appear?
- [ ] Q2 Evaluate one of them with (c).
- [ ] Q3 In the other, anticommute $\slashed{k}$ past $\slashed{p}$ to reverse the order, and collect.
- [ ] Q4 **[why]** The right side has the reversed order. Test the identity with $k = p = q$: what do both sides give, and is it consistent with (b)?
- [ ] Q5 **[conv]** Do these identities depend on the basis of the $\gamma$'s, on the signature convention, or on the spacetime dimension?

> [!tip]- Hint (d): route
> **Strategy (K5).** As in (c): one anticommutation, then (c) and a reordering.

> [!tip]- Hints: definitions, results and your solution for the whole problem
> **Topic and definitions.** T8. Dirac matrices Definition [[§CB.11 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^def-cb-11-11|§CB.11.11]] The Dirac Matrices; Feynman slash Definition [[§C5a.7 The Dirac Equation and Its Lagrangian#^def-c5a-7-2|§C5a.7.2]] Feynman Slash.
>
> **Key results.** Theorem [[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-2|§C5a.11.2]] Contraction Identities (this problem; its second derivation route is the submission); Theorem [[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-1|§C5a.11.1]] Slash Algebra (slash algebra); Theorem [[§CB.11 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^thm-cb-11-12|§CB.11.12]] First Consequences of the Clifford Algebra (squares and anticommutation of the $\gamma$'s).
>
> **Difficulty** (a) 1, (b) 1, (c) 1, (d) 2. Submitted solution: (a) and (b) component by component, with explicit sums over $\mu = 0$ and $i = 1, 2, 3$ (the vault's main derivation of Theorem [[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-2|§C5a.11.2]] Contraction Identities moves $\gamma^\mu$ through one slash at a time with $\slashed{a}\gamma^\mu = 2a^\mu - \gamma^\mu\slashed{a}$; the submission is kept there as the second route); (c) and (d) by anticommuting with lowered indices and reusing (a) and (c).

### PS5.3 The Gordon identity

(Based on PS Problem 3.2.) Derive $\bar u(p')\gamma^\mu u(p) = \bar u(p')\Bigl[\frac{p^\mu + p'^\mu}{2m} + \frac{i\sigma^{\mu\nu}q_\nu}{2m}\Bigr]u(p)$, where $q^\mu = (p' - p)^\mu$ and $\sigma^{\mu\nu} = \frac i2[\gamma^\mu, \gamma^\nu]$ (PS §3.4).

^ps5-3

- [ ] Q1 **[def]** Define $\bar u$ and $\sigma^{\mu\nu}$ (PS's normalization), and state the on-shell conditions on $u(p)$ and $\bar u(p')$: which matrix, acting from which side?
- [ ] Q2 Derive $\slashed{p}\,u(p) = m\,u(p)$ from the plane wave $u(p)e^{-ip\cdot x}$.
- [ ] Q3 Derive the condition on $\bar u(p')$: take the Hermitian conjugate and insert $\gamma^0$. Which hermiticity property of the $\gamma$'s is needed, and in which basis is it checked?
- [ ] Q4 Expand $i\sigma^{\mu\nu}q_\nu$ into products of $\gamma^\mu$ with $\slashed{p}$ and $\slashed{p}'$.
- [ ] Q5 Reorder each product so that $\slashed{p}'$ stands next to $\bar u(p')$ and $\slashed{p}$ next to $u(p)$. Which slash identity does this?
- [ ] Q6 Apply the on-shell conditions and collect. **[why]** Where exactly is on-shellness used, and why is the Gordon identity therefore not a $4\times4$ matrix identity?
- [ ] Q7 **[conv]** Problem 5(d) of the same set writes $\sigma^{\mu\nu} = \frac1{4i}[\gamma^\mu, \gamma^\nu]$. With that normalization, what would the coefficient of the spin term be?

> [!tip]- Hints: definitions, results, route, your solution
> **Topic and definitions.** T8. Dirac conjugate Definition [[§C5a.2 The Dirac Form#^def-c5a-2-1|§C5a.2.1]] The Dirac Conjugate; positive-frequency solutions Definition [[§C5a.9 Plane-Wave Solutions#^def-c5a-9-1|§C5a.9.1]] Positive- and Negative-Frequency Solutions; $\sigma^{\mu\nu}$ Definition [[§C5a.6 The Dirac Conjugate and the Bilinears#^def-c5a-6-2|§C5a.6.2]] The Sixteen Bilinears; its normalizations [[§C5a.6 The Dirac Conjugate and the Bilinears#^cau-c5a-6-1|§C5a.6, Caution: Three normalizations of σ^μν]].
>
> **Key results.** Theorem [[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-9|§C5a.11.9]] The Gordon Identity (this problem; [[§C5a.11 Gamma-Matrix Technology#^der-c5a-11-9b|Derivation §C5a.11.9, second route]] is the submission); Theorem [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-1|§C5a.9.1]] Plane Waves Turn the Dirac Equation into Algebra ($\slashed{p}u = mu$); Theorem [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-10|§C5a.9.10]] The Dirac Conjugate of u(p) (the Dirac equation acting from the right on $\bar u$); Theorem [[§C5a.2 The Dirac Form#^thm-c5a-2-1|§C5a.2.1]] Hermiticity of the Dirac Matrices ($\gamma^{\mu\dagger} = \gamma^0\gamma^\mu\gamma^0$); Theorem [[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-6|§C5a.7.6]] The Field Equations of the Dirac Lagrangian and [[§C5a.7 The Dirac Equation and Its Lagrangian#^cau-c5a-7-3|§C5a.7, Caution: The order of γ⁰ and γ^μ in the conjugate equation]] (the conjugate equation); Theorem [[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-1|§C5a.11.1]] Slash Algebra (slash algebra); [[§C5a.11 Gamma-Matrix Technology#^rem-c5a-11-4|§C5a.11, Remark: What the Gordon identity says]] (what the identity says).
>
> **Strategy (K6, K5, K7).** Expand $\sigma^{\mu\nu}q_\nu$, reorder so that $\slashed{p}'$ meets $\bar u(p')$ and $\slashed{p}$ meets $u(p)$, then go on shell.
>
> **Difficulty 2.** Submitted solution: starts from the right-hand side, expands $\sigma^{\mu\nu}$, reorders with the Clifford relation, and derives both on-shell conditions explicitly (the conjugate one from $\gamma^0\gamma^{\mu\dagger}\gamma^0 = \gamma^\mu$, citing PS for the hermiticity of the $\gamma$'s); kept in the vault as [[§C5a.11 Gamma-Matrix Technology#^der-c5a-11-9b|Derivation §C5a.11.9, second route]].

### PS5.4 The momentum operator for the Dirac field

The canonical energy–momentum tensor of the Dirac field is $T_{\mu\nu} = i\bar\psi\gamma_\mu\partial_\nu\psi - g_{\mu\nu}\mathcal L$, with $\mathcal L = \bar\psi(i\gamma^\mu\partial_\mu - m)\psi$.

*Parts: (a), (b).*

^ps5-4

#### (a)

Use the Dirac equation to show that the energy–momentum tensor is conserved.

^ps5-4-a

- [ ] Q1 **[def]** Write the Dirac equation and derive the conjugate equation for $\bar\psi$. On which side of $\gamma^{\mu\dagger}$ must $\gamma^0$ be inserted?
- [ ] Q2 **[def]** From the general canonical tensor $\frac{\partial\mathcal L}{\partial(\partial_\mu\phi)}\partial^\nu\phi - g^{\mu\nu}\mathcal L$, obtain the given $T^{\mu\nu}$. Which index is the current index, and why does $\bar\psi$ contribute nothing to the first term?
- [ ] Q3 Take $\partial^\mu T_{\mu\nu}$ with the product rule, renaming the dummy index inside $\mathcal L$.
- [ ] Q4 Use the Dirac equation and its conjugate on the right terms. Show that the mass terms and the second-derivative terms cancel separately.
- [ ] Q5 **[why]** Why is $T^{\mu\nu}$ conserved only on solutions? What is $\mathcal L$ on solutions, and what does that do to $T^{\mu\nu}$?
- [ ] Q6 **[why]** Is this $T^{\mu\nu}$ symmetric? Which tensor is, and why would one want it?

> [!tip]- Hint (a): route
> **Strategy (K12, K7).** Divergence on the first index; the Dirac equation and its conjugate kill the terms pairwise.

#### (b)

Write the momentum operator for the Dirac field (no derivation needed; one equation). The momentum operator is the operator of the conserved Noether charge of spacetime translations, not the canonically conjugate momentum of the equal-time commutation relations.

^ps5-4-b

- [ ] Q1 **[def]** Define the momentum as a Noether charge: which components of $T$, integrated over what?
- [ ] Q2 Compute $T^{0i}$. Why does the $g^{0i}\mathcal L$ term drop, and what is $\bar\psi\gamma^0$?
- [ ] Q3 **[conv]** Track the sign of $\partial^i$ versus $\partial_i$ to write the vector $\mathbf P$. Check on a positive-frequency plane wave $\psi = w\,e^{-ip\cdot x}$ that the momentum density points along $+\mathbf p$.
- [ ] Q4 **[why]** What is the canonical momentum $\pi_\psi$, and why is it not the momentum operator?
- [ ] Q5 After quantization with anticommutators, what reordering does the antiparticle term of $\hat{\mathbf P}$ need, and does it leave a constant behind?

> [!tip]- Hint (b): route
> **Strategy (K12).** $P^i = \int d^3x\,T^{0i}$.

> [!tip]- Hints: definitions, results and your solution for the whole problem
> **Topic and definitions.** T8 (T4 for the Noether charges). The free Dirac field Model [[§C5a.7 The Dirac Equation and Its Lagrangian#^mod-c5a-7-3|§C5a.7.3]] The Free Dirac Field; the Dirac equation Definition [[§C5a.7 The Dirac Equation and Its Lagrangian#^def-c5a-7-1|§C5a.7.1]] The Dirac Equation; Dirac conjugate Definition [[§C5a.2 The Dirac Form#^def-c5a-2-1|§C5a.2.1]] The Dirac Conjugate; canonical energy–momentum tensor Definition [[§C1b.7 Spacetime Symmetries꞉ Energy and Momentum#^def-c1b-7-2|§C1b.7.2]] Canonical Energy–Momentum Tensor.
>
> **Key results.** Theorem [[§C5a.8 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-8-5|§C5a.8.5]] The Canonical Energy–Momentum Tensor of the Dirac Field (this problem (a)); Theorem [[§C5a.8 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-8-6|§C5a.8.6]] Energy and Momentum of the Dirac Field (this problem (b)); Theorem [[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-6|§C5a.7.6]] The Field Equations of the Dirac Lagrangian (the conjugate Dirac equation; this problem (a)); [[§C5a.7 The Dirac Equation and Its Lagrangian#^cau-c5a-7-3|§C5a.7, Caution: The order of γ⁰ and γ^μ in the conjugate equation]]; Theorem [[§C1b.7 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-7-5|§C1b.7.5]] Translation Invariance Conserves the Energy–Momentum Tensor, Theorem [[§C1b.7 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-7-6|§C1b.7.6]] Energy and Momentum of a Field (translations conserve $T^{\mu\nu}$; energy and momentum as charges); Theorem [[§C5a.8 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-8-1|§C5a.8.1]] Canonical Momenta of the Dirac Field (canonical momentum); Theorem [[§C5a.8 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-8-7|§C5a.8.7]] The Dirac Momentum Generates Spatial Translations; [[§C5a.8 Canonical Structure and Noether Currents of the Dirac Field#^rem-c5a-8-1|§C5a.8, Remark: Why P is the momentum, for the Dirac field]] (why $\mathbf P$ is the momentum); Theorem [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-7|§C5b.3.7]] Momentum of the Dirac Field (the quantized $\hat{\mathbf P}$ in modes).
>
> **Difficulty** (a) 1, (b) 1. Submitted solution: (a) the conjugate equation by Hermitian conjugation with $\gamma^0\gamma^{\mu\dagger}\gamma^0 = \gamma^\mu$, conservation stated on the first index, and the four terms cancelled in two pairs; (b) one boxed equation from $T^{0i}$, as the problem asks; operator ordering is not discussed (the mode form is Theorem [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-7|§C5b.3.7]] Momentum of the Dirac Field).

### PS5.5 The γ⁵ matrix

$\gamma^5 \equiv i\gamma^0\gamma^1\gamma^2\gamma^3$; there is no way to lower the "5" ($\gamma_5$ is a typo). The sixteen matrices $1, \gamma^\mu, \sigma^{\mu\nu}, \gamma^5\gamma^\mu, \gamma^5$ are a basis of all $4\times4$ matrices; (c) and (d) reduce antisymmetric products of three or four $\gamma$'s to this basis and show that $\gamma^5\sigma_{\mu\nu}$ is not needed.

*Parts: (a), (b), (c), (d).*

^ps5-5

#### (a)

Show $\gamma^5\gamma^\mu = -\gamma^\mu\gamma^5$.

^ps5-5-a

- [ ] Q1 **[def]** Define $\gamma^5$. Why is there no $\gamma_5$?
- [ ] Q2 Move $\gamma^\mu$ from the right of $\gamma^0\gamma^1\gamma^2\gamma^3$ to the left one factor at a time. What terms with $g^{a\mu}$ appear, and with which signs?
- [ ] Q3 For fixed $\mu$ only one of these terms survives. Simplify it and compare with $\gamma^\mu\gamma^5$.
- [ ] Q4 Short route: $\gamma^\mu$ equals one of the four factors. With how many factors does it anticommute, and with how many does it commute?
- [ ] Q5 **[why]** In $d$ spacetime dimensions, does the product of all $d$ gamma matrices anticommute with each $\gamma^\mu$? What changes when $d$ is odd?

> [!tip]- Hint (a): route
> **Strategy (K5).** Move $\gamma^\mu$ through the four factors.

#### (b)

Show that $\gamma^5$ is Hermitian and $(\gamma^5)^2 = 1$, using the hermiticity of the $\gamma$'s from their explicit form in PS.

^ps5-5-b

- [ ] Q1 **[def]** State the hermiticity of $\gamma^0$ and $\gamma^i$, and check it from the chiral-basis matrices.
- [ ] Q2 Take the adjoint of $\gamma^5$: reverse the order and conjugate $i$. How many transpositions restore the order $0123$?
- [ ] Q3 Compute $(\gamma^5)^2$ by pairing equal factors from the middle outward.
- [ ] Q4 **[why]** Hermiticity was checked in one basis. In which other bases does it hold, and why is $(\gamma^5)^2 = 1$ true in every basis?
- [ ] Q5 Find $\gamma^5$ in the chiral basis. What are its eigenspaces?

> [!tip]- Hint (b): route
> **Strategy (K5, K7).** Reverse the product under $\dagger$; count transpositions.

#### (c)

Show $\gamma^5 = -\frac{i}{24}\epsilon_{\kappa\lambda\mu\nu}\gamma^\kappa\gamma^\lambda\gamma^\mu\gamma^\nu$ and $\gamma^{[\kappa}\gamma^\lambda\gamma^\mu\gamma^{\nu]} = -i\epsilon^{\kappa\lambda\mu\nu}\gamma^5$, with $\epsilon^{0123} = +1$, $\epsilon_{0123} = -1$, where $[\cdots]$ is antisymmetrization, $\gamma^{[\kappa}\gamma^\lambda\gamma^\mu\gamma^{\nu]} = \frac1{24}(\gamma^\kappa\gamma^\lambda\gamma^\mu\gamma^\nu - \gamma^\lambda\gamma^\kappa\gamma^\mu\gamma^\nu + \dots)$ (24 terms).

^ps5-5-c

- [ ] Q1 **[conv]** State the course's $\varepsilon$ convention ($\varepsilon^{0123}$, $\varepsilon_{0123}$) and PS's. Which signs in (c) and (d) would flip under PS's stated convention?
- [ ] Q2 For distinct indices, relate $\gamma^\kappa\gamma^\lambda\gamma^\mu\gamma^\nu$ to $\gamma^0\gamma^1\gamma^2\gamma^3$. Why does this need the indices to be distinct?
- [ ] Q3 Count the nonzero terms of $\epsilon_{\kappa\lambda\mu\nu}\gamma^\kappa\gamma^\lambda\gamma^\mu\gamma^\nu$, evaluate the sum and solve for $\gamma^5$.
- [ ] Q4 **[def]** Define the antisymmetrization with its $1/4!$. Show that it equals the plain product when the indices are distinct.
- [ ] Q5 Show that it vanishes when two indices coincide, and conclude the second identity for all index values.
- [ ] Q6 **[conv]** Check the convention-free statement $\gamma^0\gamma^1\gamma^2\gamma^3 = -i\gamma^5$ against the second identity at $(\kappa\lambda\mu\nu) = (0123)$.

> [!tip]- Hint (c): route
> **Strategy (K5).** For distinct indices a product of $\gamma$'s is the sign of the permutation times $\gamma^0\gamma^1\gamma^2\gamma^3$.

#### (d)

Show $\gamma^{[\lambda}\gamma^\mu\gamma^{\nu]} = i\epsilon^{\lambda\mu\nu\kappa}\gamma_\kappa\gamma^5$ and $\gamma^5\sigma_{\mu\nu} = \frac i2\epsilon_{\mu\nu\lambda\kappa}\sigma^{\lambda\kappa}$, with the "standard notation" $\sigma^{\mu\nu} = \frac1{4i}[\gamma^\mu, \gamma^\nu]$.

^ps5-5-d

- [ ] Q1 Show that $\gamma^{[\lambda}\gamma^\mu\gamma^{\nu]}$ vanishes unless $\lambda$, $\mu$, $\nu$ are distinct, and equals the plain product when they are.
- [ ] Q2 Contract the second identity of (c) with $\gamma_\kappa$. Which single $\kappa$ survives on the left, and what is $\gamma_\kappa\gamma^\kappa$ with no sum?
- [ ] Q3 Move the contracted index of $\varepsilon$ to the last slot. How many transpositions, and what sign?
- [ ] Q4 **[conv]** Compare the statement's $\sigma^{\mu\nu} = \frac1{4i}[\gamma^\mu, \gamma^\nu]$ with PS's $\sigma^{\mu\nu}$ (used in Problem 3) and with $S^{\mu\nu}$. **[why]** Why does the second identity hold in every normalization?
- [ ] Q5 Derive the second identity with upper indices: contract the first identity with $\gamma_\lambda$, express $\gamma^{[\mu}\gamma^{\nu]}$ through $\sigma^{\mu\nu}$, and antisymmetrize the remaining $\gamma_\lambda\gamma_\kappa$.
- [ ] Q6 Lower all indices (what is $\varepsilon_{0123}$ then?) and move $\gamma^5$ to the left. Why does $\gamma^5$ commute with $\sigma^{\mu\nu}$?
- [ ] Q7 **[why]** Following the closing paragraph, reduce $\gamma^\mu\gamma^\nu\gamma^\rho$ to the sixteen-element basis. Why is $\gamma^5\sigma^{\mu\nu}$ never needed as a separate element?

> [!tip]- Hint (d): route
> **Strategy (K5, K2).** Contract the identity of (c) with $\gamma_\kappa$, then the first identity of (d) with $\gamma_\lambda$; reshuffle $\varepsilon$ indices; lower all indices.

> [!tip]- Hints: definitions, results and your solution for the whole problem
> **Topic and definitions.** T8. $\gamma^5$ Definition [[§CB.12 Clifford Algebras꞉ Grading, Basis and the Volume Element#^def-cb-12-14|§CB.12.14]] The Matrix γ⁵; antisymmetrized products Definition [[§CB.12 Clifford Algebras꞉ Grading, Basis and the Volume Element#^def-cb-12-8|§CB.12.8]] Antisymmetrized Products of γ Matrices; Dirac matrices Definition [[§CB.11 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^def-cb-11-11|§CB.11.11]] The Dirac Matrices; the chiral basis Example [[§CB.11 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^ex-cb-11-13|§CB.11.13]] The Chiral Dirac Matrices; the sign of $\varepsilon^{0123}$ [[§C1a.5 Vectors, Tensors and Index Notation#^cau-c1a-5-5|§C1a.5, Caution: The sign of ε⁰¹²³: these notes versus Peskin–Schroeder]]; $\sigma^{\mu\nu}$ Definition [[§C5a.6 The Dirac Conjugate and the Bilinears#^def-c5a-6-2|§C5a.6.2]] The Sixteen Bilinears and its normalizations [[§C5a.6 The Dirac Conjugate and the Bilinears#^cau-c5a-6-1|§C5a.6, Caution: Three normalizations of σ^μν]].
>
> **Key results.** Theorem [[§CB.12 Clifford Algebras꞉ Grading, Basis and the Volume Element#^thm-cb-12-15|§CB.12.15]] Algebraic Properties of γ⁵ (this problem (a)–(b)); Theorem [[§C5a.2 The Dirac Form#^thm-c5a-2-1|§C5a.2.1]] Hermiticity of the Dirac Matrices (hermiticity of the $\gamma$'s; (b)); Example [[§CB.12 Clifford Algebras꞉ Grading, Basis and the Volume Element#^ex-cb-12-16|§CB.12.16]] γ⁵ in the Chiral Basis ($\gamma^5$ in the chiral basis); Theorem [[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-5|§C5a.11.5]] γ⁵ as a Totally Antisymmetric Product (this problem (c)); Theorem [[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-6|§C5a.11.6]] The Antisymmetric Product of Three γ's, Theorem [[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-7|§C5a.11.7]] γ⁵ Dualizes σ^μν (this problem (d)); Theorem [[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-8|§C5a.11.8]] Every Product of γ's Reduces to the Standard Basis (the closing paragraph); Theorem [[§CB.12 Clifford Algebras꞉ Grading, Basis and the Volume Element#^thm-cb-12-9|§CB.12.9]] The Sixteen Products Are a Basis (the sixteen products are a basis); [[§C5a.11 Gamma-Matrix Technology#^cau-c5a-11-1|§C5a.11, Caution: The sign of the ε trace across sources]] (the $\varepsilon$ sign across sources).
>
> **Difficulty** (a) 1, (b) 1, (c) 2, (d) 3. Submitted solution: (a) $\gamma^\mu$ moved through one factor at a time with the anticommutator, then a case check for each $\mu$; (b) the chiral-basis hermiticity, reversal with transposition counting, and $(\gamma^5)^2$ by pairing; (c) permutation signs and the count $4\cdot3\cdot2 = 24$, with the repeated-index case treated separately; (d) contraction with $\gamma_\kappa$, then with $\gamma_\lambda$, the statement's $\frac1{4i}$ normalization throughout, lowering with $\varepsilon_{0123} = -1$. The vault keeps (c) and (d) as Theorem [[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-5|§C5a.11.5]] γ⁵ as a Totally Antisymmetric Product–Theorem [[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-7|§C5a.11.7]] γ⁵ Dualizes σ^μν and notes that the second identity is homogeneous in $\sigma$.

### PS5.6 Helicity spinors

The positive-frequency solution is $u(p) = \bigl(\sqrt{\sigma\cdot p}\,\xi,\ \sqrt{\bar\sigma\cdot p}\,\xi\bigr) = \bigl(\sqrt{E - \boldsymbol\sigma\cdot\mathbf p}\,\xi,\ \sqrt{E + \boldsymbol\sigma\cdot\mathbf p}\,\xi\bigr)$; $u^+$ ($u^-$) has $\xi$ of positive (negative) helicity, spin $\pm\frac12$ along the direction of motion. Determine the two-component helicity spinors $\xi_\pm(\hat{\mathbf p})$ from $\bigl(\hat{\mathbf p}\cdot\frac{\boldsymbol\sigma}2\bigr)\xi_\pm(\hat{\mathbf p}) = \pm\frac12\xi_\pm(\hat{\mathbf p})$, for a particle of mass $m$ and momentum $\mathbf p = p(\sin\theta\cos\phi, \sin\theta\sin\phi, \cos\theta)$, $p = |\mathbf p|$. Normalize $\xi^\dagger\xi = 1$ and choose the overall phases so that for motion along $+\hat z$ they reduce to $\xi_+ = (1, 0)^T$, $\xi_- = (0, 1)^T$.

^ps5-6

- [ ] Q1 **[def]** Define the helicity of a Dirac spinor and the helicity two-spinors. Why is the helicity of $u(p)$ fixed by $\xi$ alone?
- [ ] Q2 Write $\hat{\mathbf p}\cdot\boldsymbol\sigma$ as a $2\times2$ matrix in $\theta$, $\phi$. Find its eigenvalues without solving for the eigenvectors.
- [ ] Q3 Solve for the eigenvectors. Which phase substitution of the two components removes $\phi$ from the equations, and which form of the eigenvector relation stays valid at $\theta = 0$?
- [ ] Q4 Normalize with the half-angle identities. Where does the normalization divide by $\cos\frac\theta2$, and for which $\theta$ is that allowed?
- [ ] Q5 Fix the overall phases so that the spinors reduce to $(1, 0)^T$ and $(0, 1)^T$ for $\hat{\mathbf p} = +\hat z$; then verify the eigenvalue equation and the normalization directly for every $0 \le \theta \le \pi$.
- [ ] Q6 **[why]** At $\theta = \pi$ your spinors still depend on $\phi$, which is meaningless there. Why can no choice of phases avoid this on the whole sphere?
- [ ] Q7 **[conv]** Build $u_\pm$ from $\xi_\pm$, with the square roots acting as numbers. For $h = +\frac12$ at high energy, which two-component block of $u_+$ dominates, and is it the left- or the right-handed one in the chiral basis?

> [!tip]- Hints: definitions, results, route, your solution
> **Topic and definitions.** T8. Helicity of a Dirac spinor Definition [[§C5a.10 Normalization, Spin Sums and Helicity#^def-c5a-10-1|§C5a.10.1]] Helicity of a Dirac Spinor; helicity two-spinors Definition [[§C5a.10 Normalization, Spin Sums and Helicity#^def-c5a-10-2|§C5a.10.2]] Helicity Two-Spinors; spin basis Definition [[§C5a.9 Plane-Wave Solutions#^def-c5a-9-3|§C5a.9.3]] Spin Basis; the square roots $\sqrt{p\cdot\sigma}$, $\sqrt{p\cdot\bar\sigma}$ Definition [[§C5a.9 Plane-Wave Solutions#^def-c5a-9-5|§C5a.9.5]] The Square Roots √(p·σ) and √(p·σ̄).
>
> **Key results.** Theorem [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-11|§C5a.10.11]] The Helicity Two-Spinors (this problem); [[§C5a.10 Normalization, Spin Sums and Helicity#^cau-c5a-10-2|§C5a.10, Caution: No phase convention is smooth on the whole sphere]] (no phase convention is smooth on the whole sphere); Theorem [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-12|§C5a.10.12]] Helicity Spinors u± (the helicity spinors $u_\pm$); Theorem [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-9|§C5a.9.9]] The Positive-Frequency Spinors u(p); Theorem [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-14|§C5a.10.14]] The Massless and High-Energy Limit: Helicity Becomes Chirality (massless and high-energy limit: helicity becomes chirality).
>
> **Strategy (K4).** Eigenvectors of $\hat{\mathbf p}\cdot\boldsymbol\sigma$; a phase substitution removes $\phi$; half-angle identities; fix the phases at $\theta = 0$.
>
> **Difficulty 2.** Submitted solution: the substitution $x = e^{-i\phi/2}x'$, $y = e^{i\phi/2}y'$, the undivided relations with $1 + \cos\theta$ to keep $\theta = 0$, normalization with half angles (valid for $\theta < \pi$), phases fixed at $\theta = 0$ by $\alpha = \phi/2$, $\beta = -\phi/2$, and a closing direct check that also covers $\theta = \pi$. The vault states the result as Theorem [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-11|§C5a.10.11]] The Helicity Two-Spinors and adds [[§C5a.10 Normalization, Spin Sums and Helicity#^cau-c5a-10-2|§C5a.10, Caution: No phase convention is smooth on the whole sphere]] on the south pole.

## Problem Set 6: Quantization of Fermions (due Oct 11; submitted)

### PS6.1 The momentum operator in modes

Verify PS eqn 2.33. In other words, show that the momentum operator $\mathbf P = -\int d^3x\,:\!\pi(\mathbf x)\nabla\phi(\mathbf x)\!:$ can be written in terms of scalar field ladder operators as $\mathbf P = \int\frac{d^3p}{(2\pi)^3}\,\mathbf p\,a^\dagger_{\mathbf p}a_{\mathbf p}$. In the formula defining $\mathbf P$ the colons mean "normal ordering": the introduction of operators through quantization comes with the instruction that $a_{\mathbf p}$ is placed to the right of $a^\dagger_{\mathbf p}$ from the outset; it amounts to the prescription that the (potentially infinite) constant due to reordering of $a_{\mathbf p}$ and $a^\dagger_{\mathbf p}$ must be omitted.

^ps6-1

- [ ] Q1 **[def]** State the definition of the normal-ordered product $:\!\hat X\!:$ for scalar ladder operators. What does Larsen's phrasing ("placed to the right … from the outset") add to it?
- [ ] Q2 **[def]** Write the mode expansions of $\hat\phi(x)$ and $\hat\pi(x)$ with all factors ($\sqrt{2E_{\mathbf p}}$, $(2\pi)^3$, signs of the exponents), and compute $\nabla e^{\mp ip\cdot x}$.
- [ ] Q3 **[why]** Why may $\hat{\mathbf P}$ be evaluated at $t = 0$? Which terms would carry time dependence if $t$ were kept, and why does that not matter for the result?
- [ ] Q4 Do the $\mathbf x$ integral of the product of the two expansions. Which of the four operator products comes with $\delta^3(\mathbf p - \mathbf q)$ and which with $\delta^3(\mathbf p + \mathbf q)$, and what does the $\mathbf q$ integral leave in the square-root factor?
- [ ] Q5 Show that $\int\frac{d^3p}{(2\pi)^3}\,\mathbf p\,\hat a_{\mathbf p}\hat a_{-\mathbf p}$ and its $\hat a^\dagger\hat a^\dagger$ partner vanish. Which two facts are used?
- [ ] Q6 Normal-order the two remaining terms and collect the factors to reach the stated form.
- [ ] Q7 **[why]** Without the colons, what constant would appear (in terms of $\delta^3(\mathbf 0)$, or the volume $V$ in a box)? Why does it vanish for $\hat{\mathbf P}$ but not for $\hat H$?

> [!tip]- Hints: definitions, results, route, your solution
> **Topic and definitions.** T5 (with T4: the field momentum as a Noether charge).
> - Normal ordering: Definition [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^def-c2a-3-1|§C2a.3.1]] Normal Ordering
> - Field momentum of the real scalar, $\mathbf P = -\int d^3x\,\pi\nabla\phi$: Theorem [[§C1b.7 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-7-7|§C1b.7.7]] Energy and Momentum of the Free Real Scalar Field
> - Mode expansion of $\hat\phi$, $\hat\pi$: Theorem [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-2|§C2a.2.2]] Mode Expansion of the Real Field; mode algebra Theorem [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|§C2a.2.6]] The Mode Algebra
>
> **Key results.** Example [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^ex-c2a-3-1|§C2a.3.1]] The Momentum, Normal-Ordered from the Outset (this problem); Theorem [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-5|§C2a.3.5]] Momentum in Mode Form; plane waves integrate to a delta function Theorem [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|§CA.3.3]] Plane Waves Integrate to a Delta Function; $\delta^3(0)$ as a volume Theorem [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-2|§C2a.3.2]] δ³(0) Has No Value; in a Box It Is the Volume; [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^rem-c2a-3-2|§C2a.3, Remark: Normal ordering is a choice of quantization]].
>
> **Strategy (K9).** Substitute the mode expansions at $t = 0$, do the $\mathbf x$ integral to $\delta^3$'s, remove the $\hat a\hat a$ and $\hat a^\dagger\hat a^\dagger$ terms by $\mathbf p \to -\mathbf p$, normal-order the rest.
>
> **Difficulty 1.** Submitted solution: the route above, $t = 0$ justified by conservation of $\mathbf P$, the normal ordering applied after expanding; a closing remark computes the unordered constant $\frac V2\int\frac{d^3p}{(2\pi)^3}\,\mathbf p$ and notes that it vanishes for a rotationally symmetric cutoff. The vault integrates it as Example [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^ex-c2a-3-1|§C2a.3.1]] The Momentum, Normal-Ordered from the Outset (the user's derivation); Theorem [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-5|§C2a.3.5]] Momentum in Mode Form states the same result without colons, since the omitted constant is zero.

### PS6.2 The Dirac charge in modes

Verify PS eqn 3.113, i.e. show that the charge operator $Q = \int d^3x\,:\!\psi^\dagger(x)\psi(x)\!:$ can be written in terms of fermionic ladder operators as $Q = \int\frac{d^3p}{(2\pi)^3}\sum_s\bigl(a^{s\dagger}_{\mathbf p}a^s_{\mathbf p} - b^{s\dagger}_{\mathbf p}b^s_{\mathbf p}\bigr)$.

^ps6-2

- [ ] Q1 **[def]** Write the mode expansions of $\hat\psi(x)$ and $\hat\psi^\dagger(x)$: which mode operator goes with $u^s(p)$, which with $v^s(p)$, and with which exponentials?
- [ ] Q2 **[def]** State the normal-ordering rule for fermion operators. What is $:\!\hat b^r_{\mathbf p}\hat b^{s\dagger}_{\mathbf q}\!:$?
- [ ] Q3 Multiply the expansions at $t = 0$ and do the $\mathbf x$ integral. Which pairs of mode operators get $\delta^3(\mathbf p - \mathbf q)$ and which $\delta^3(\mathbf p + \mathbf q)$? Write $u^r(q)$, $v^r(q)$ at $\mathbf q = -\mathbf p$ with $\tilde p$.
- [ ] Q4 State the spinor products needed: $u^{s\dagger}(p)u^r(p)$, $v^{s\dagger}(p)v^r(p)$, and $u^{s\dagger}(p)v^r(\tilde p)$, $v^{s\dagger}(p)u^r(\tilde p)$. Which terms of $\hat Q$ do the last two remove?
- [ ] Q5 **[why]** Why is the orthogonality needed at opposite three-momenta and not at equal ones? What is $u^{r\dagger}(p)v^s(p)$?
- [ ] Q6 Reorder $\hat b^s_{\mathbf p}\hat b^{s\dagger}_{\mathbf p}$ with the anticommutator. Which constant appears, and what do normal ordering and the fermion sign do to the term?
- [ ] Q7 **[conv]** The Noether charge of $\psi \to e^{i\alpha}\psi$ with the vault's sign convention ([[§C1b.6 Conserved Charges and Internal Symmetries#^cau-c1b-6-3|§C1b.6, Caution: Sign and normalization of the U(1) current]]): is it $+\hat Q$ or $-\hat Q$ (Definition [[§C5b.5 The U(1) Charge, Particles and Antiparticles#^def-c5b-5-1|§C5b.5.1]] The U(1) Charge of the Dirac Field)?

> [!tip]- Hints: definitions, results, route, your solution
> **Topic and definitions.** T9.
> - The U(1) charge of the Dirac field: Definition [[§C5b.5 The U(1) Charge, Particles and Antiparticles#^def-c5b-5-1|§C5b.5.1]] The U(1) Charge of the Dirac Field
> - Normal ordering of fermion operators: Definition [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^def-c5b-3-1|§C5b.3.1]] Normal Ordering of Fermion Operators
> - Mode expansion of $\hat\psi$ and the conjugate fields: Theorem [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-1|§C5b.2.1]] Mode Expansion of the Dirac Field, Theorem [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-2|§C5b.2.2]] The Conjugate Fields ψ† and ψ̄; anticommutators Theorem [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-4|§C5b.2.4]] The Mode Algebra of the Dirac Field
>
> **Key results.** Theorem [[§C5b.5 The U(1) Charge, Particles and Antiparticles#^thm-c5b-5-3|§C5b.5.3]] The Charge Counts Fermions Minus Antifermions (this problem), Theorem [[§C5b.5 The U(1) Charge, Particles and Antiparticles#^thm-c5b-5-1|§C5b.5.1]] The Charge in Modes, before Any Algebra (the charge in modes before any algebra); spinor products Theorem [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-1|§C5a.10.1]] u†u = 2E, Theorem [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-3|§C5a.10.3]] v†v = 2E, Theorem [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-6|§C5a.10.6]] u and v Are Orthogonal at Opposite Three-Momenta; scalar analogue Theorem [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-6|§C2a.5.6]] The Charge Counts Particles Minus Antiparticles.
>
> **Strategy (K9, K11).** Multiply the mode expansions at $t = 0$, integrate over $\mathbf x$, kill the cross terms by $u$–$v$ orthogonality at opposite momenta, then normal-order $\hat b\hat b^\dagger$ with the fermion sign.
>
> **Difficulty 2.** Submitted solution: the same layout as PS6.1 at $t = 0$, with $\tilde p$ for the flipped momentum; the spinor products cited from PS (3.61), (3.67) (vault: Theorem [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-1|§C5a.10.1]] u†u = 2E, Theorem [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-3|§C5a.10.3]] v†v = 2E, Theorem [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-6|§C5a.10.6]] u and v Are Orthogonal at Opposite Three-Momenta); normal ordering written as $:\!\hat b\hat b^\dagger\!: = -\hat b^\dagger\hat b$, dropping $(2\pi)^3\delta^3(\mathbf 0)$. The vault cites it in Theorem [[§C5b.5 The U(1) Charge, Particles and Antiparticles#^thm-c5b-5-3|§C5b.5.3]] The Charge Counts Fermions Minus Antifermions (steps 1–2 of its derivation are this route).

### PS6.3 Representations of the Dirac matrices

The Dirac matrices are $4\times4$ matrices satisfying $\{\gamma^\mu, \gamma^\nu\} = 2g^{\mu\nu}$. PS chooses $\gamma^0_W = \begin{pmatrix}0&1\\1&0\end{pmatrix}$, $\gamma^i_W = \begin{pmatrix}0&\sigma^i\\-\sigma^i&0\end{pmatrix}$; all $\gamma$'s are off-diagonal in $2\times2$ blocks, so all Lorentz generators $S^{\mu\nu} = \frac i4[\gamma^\mu, \gamma^\nu]$ are block diagonal; this is the Weyl representation (subscript $W$).

*Parts: (a), (b), (c), (d).*

^ps6-3

#### (a)

Consider $\gamma^\mu = U\gamma^\mu_WU^\dagger$ with $U$ a unitary $4\times4$ matrix. Show that these $\gamma^\mu$ satisfy the Dirac algebra as well. (Comment: all realizations of the Dirac algebra are unitarily equivalent.)

^ps6-3-a

- [ ] Q1 **[def]** State the Dirac algebra with the course's metric. What are $g^{00}$, $g^{ij}$, $g^{0i}$?
- [ ] Q2 Check $\{\gamma^0_W, \gamma^0_W\}$, $\{\gamma^i_W, \gamma^j_W\}$ and $\{\gamma^0_W, \gamma^i_W\}$ by block multiplication. Which Pauli identity enters?
- [ ] Q3 Show $\{U\gamma^\mu_WU^\dagger, U\gamma^\nu_WU^\dagger\} = U\{\gamma^\mu_W, \gamma^\nu_W\}U^\dagger$ and conclude. Where is $U^\dagger U = \mathbb 1$ used, and would any invertible $S$ (with $S^{-1}$ in place of $U^\dagger$) do?
- [ ] Q4 **[why]** Larsen's comment says all realizations are unitarily equivalent. Which theorem states it, and which extra condition on the two sets of matrices makes the intertwiner unitary rather than merely invertible?

> [!tip]- Hint (a): route
> **Strategy (K5).** Check the Weyl matrices by $2\times2$ block products, then conjugation by $U$ preserves products.

#### (b)

A frequent alternative corresponds to $U_D = \frac1{\sqrt2}(1 - \gamma^5_W\gamma^0_W) = \frac1{\sqrt2}\begin{pmatrix}1&1\\-1&1\end{pmatrix}$, defining the Dirac representation ("also sometimes called the standard representation but that is misleading"). Show that $U_D$ is unitary and find the Dirac matrices in the Dirac representation.

^ps6-3-b

- [ ] Q1 **[def]** Write $\gamma^5$ in the chiral basis (course definition and sign) and compute $\gamma^5_W\gamma^0_W$ in blocks, to confirm the block form of $U_D$.
- [ ] Q2 Write $U_D^\dagger$ and check $U_D^\dagger U_D = U_DU_D^\dagger = \mathbb 1$.
- [ ] Q3 Compute $U_D\gamma^\mu_WU_D^\dagger$ in blocks in terms of $\sigma^\mu$, $\bar\sigma^\mu$; then set $\mu = 0$ and $\mu = i$.
- [ ] Q4 **[conv]** The vault's matrix $U$ in Example [[§C5a.5 Chirality and Weyl Spinors#^ex-c5a-5-1|§C5a.5.1]] The Dirac Basis Is Equivalent to the Chiral Basis carries the Dirac basis to the chiral one. How are $U$ and $U_D$ related, and which of them multiplies the spinor components, $\psi_D = (\,?\,)\psi$?
- [ ] Q5 **[why]** Which matrix is diagonal in each basis ($\gamma^0$ or $\gamma^5$), and why can both never be diagonal in the same basis (Theorem [[§CB.12 Clifford Algebras꞉ Grading, Basis and the Volume Element#^thm-cb-12-17|§CB.12.17]] γ⁰ and γ⁵ Cannot Be Diagonal in the Same Basis)?

> [!tip]- Hint (b): route
> **Strategy (K5).** Block multiplication; write $\gamma^\mu_W = \begin{pmatrix}0&\sigma^\mu\\\bar\sigma^\mu&0\end{pmatrix}$ and conjugate once for all $\mu$.

#### (c)

Write the positive frequency solutions as $\psi(x) = u(p)e^{-ipx}$. Verify that the solution in the Dirac representation is $u_D(p) = \frac1{\sqrt{E_p + m}}\begin{pmatrix}(E_p + m)\xi\\ \vec\sigma\cdot\vec p\,\xi\end{pmatrix}$.

^ps6-3-c

- [ ] Q1 **[def]** Write $u(p)$ in the chiral basis, and $p\cdot\sigma$, $p\cdot\bar\sigma$ in terms of $E_{\mathbf p}$ and $\mathbf p\cdot\boldsymbol\sigma$.
- [ ] Q2 **[why]** Why does $U_Du(p)$ solve the Dirac equation written with the $\gamma_D$'s? (One line, using (b).)
- [ ] Q3 Show $(\boldsymbol\sigma\cdot\mathbf p)^2 = |\mathbf p|^2\,\mathbb 1$ from $\sigma^i\sigma^j = \delta^{ij} + i\varepsilon^{ijk}\sigma^k$.
- [ ] Q4 Show $(p\cdot\sigma + m)^2 = 2(E_{\mathbf p} + m)\,p\cdot\sigma$. Why is $(p\cdot\sigma + m)/\sqrt{2(E_{\mathbf p} + m)}$ the positive square root?
- [ ] Q5 Substitute into $U_Du$ using the sum and the difference of $p\cdot\sigma$ and $p\cdot\bar\sigma$, and simplify to the stated $u_D$.
- [ ] Q6 **[conv]** Distinguish $\boldsymbol\sigma\cdot\mathbf p = \sum_ip^i\sigma^i$ from $p\cdot\sigma = p_\mu\sigma^\mu$: where does the lowered index put the minus sign?

> [!tip]- Hint (c): route
> **Strategy (K6, K5).** $u_D = U_Du$ with $u = (\sqrt{p\cdot\sigma}\,\xi, \sqrt{p\cdot\bar\sigma}\,\xi)$ and the explicit square root $\sqrt{p\cdot\sigma} = (p\cdot\sigma + m)/\sqrt{2(E_{\mathbf p} + m)}$.

#### (d)

Show that the solution above is normalized in the conventional way, so that $\bar uu = 2m$. (Comments after the problem: in the Dirac representation the lower components vanish in the rest frame and are small for small momentum, so the upper two are the nonrelativistic two-component wave function; the Weyl representation is better for relativistic processes; in the Majorana representation all Dirac matrices are real.)

^ps6-3-d

- [ ] Q1 **[def]** State the conventional normalization (with $\xi^{r\dagger}\xi^s$) and the definition of $\bar u$. With which $\gamma^0$ is $\bar u_D$ formed?
- [ ] Q2 Compute $\bar u_D(p)$, using that $\boldsymbol\sigma\cdot\mathbf p$ is Hermitian.
- [ ] Q3 Multiply $\bar u^r_Du^s_D$ and reduce with $(\boldsymbol\sigma\cdot\mathbf p)^2 = |\mathbf p|^2$ and $E_{\mathbf p}^2 = m^2 + |\mathbf p|^2$.
- [ ] Q4 **[why]** $\bar uu$ does not depend on the basis. Which property of $U_D$ guarantees that $\bar\psi$ keeps its form (Theorem [[§C5a.2 The Dirac Form#^thm-c5a-2-2|§C5a.2.2]] Which Changes of Basis Preserve ψ̄)?
- [ ] Q5 Larsen's comment: what are the lower components of $u_D$ at rest, and how small are they for $|\mathbf p| \ll m$? Why is the Dirac basis the one used at low energy?

> [!tip]- Hint (d): route
> **Strategy (K5).** $\bar u_D = u_D^\dagger\gamma^0_D$ with $\gamma^0_D$ from (b).

> [!tip]- Hints: definitions, results and your solution for the whole problem
> **Topic and definitions.** T8 (with T7 for the equivalence of bases).
> - Chiral (Weyl) basis and $\sigma^\mu$, $\bar\sigma^\mu$: Definition [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-3|§C5a.1.3]] The Chiral Basis, Definition [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-2|§C5a.1.2]] The Matrices σ^μ and σ̄^μ
> - Dirac conjugate: Definition [[§C5a.2 The Dirac Form#^def-c5a-2-1|§C5a.2.1]] The Dirac Conjugate; normalization of the spinors Definition [[§C5a.9 Plane-Wave Solutions#^def-c5a-9-4|§C5a.9.4]] Normalization of the Spinors
> - $\gamma^5$: Definition [[§CB.12 Clifford Algebras꞉ Grading, Basis and the Volume Element#^def-cb-12-14|§CB.12.14]] The Matrix γ⁵
>
> **Key results.** Theorem [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-2|§C5a.1.2]] The Chiral Matrices Satisfy the Clifford Algebra; Pauli's theorem Theorem [[§CB.13 Complex Clifford Algebras and Clifford Modules#^thm-cb-13-12|§CB.13.12]] Pauli's Fundamental Theorem; Example [[§C5a.5 Chirality and Weyl Spinors#^ex-c5a-5-1|§C5a.5.1]] The Dirac Basis Is Equivalent to the Chiral Basis ($U_D$, part (b)); Example [[§C5a.9 Plane-Wave Solutions#^ex-c5a-9-1|§C5a.9.1]] The Plane-Wave Spinors in the Dirac Basis (parts (c)–(d)); [[§C5a.5 Chirality and Weyl Spinors#^rem-c5a-5-5|§C5a.5, Remark: Why each basis is used]] (the comments); square roots Theorem [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-6|§C5a.9.6]] Explicit Square Roots, Theorem [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-7|§C5a.9.7]] The Square-Root Identities; $u(p)$ Theorem [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-9|§C5a.9.9]] The Positive-Frequency Spinors u(p); components under a change of basis Theorem [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-5|§CB.0.5]] Components Change with U, Matrices with U and U⁻¹; Theorem [[§C5a.2 The Dirac Form#^thm-c5a-2-2|§C5a.2.2]] Which Changes of Basis Preserve ψ̄; [[§C5a.5 Chirality and Weyl Spinors#^rem-c5a-5-6|§C5a.5, ★ Remark: The Majorana basis]].
>
> **Difficulty** (a) 1, (b) 1, (c) 2, (d) 1. Submitted solution: (a) all three cases of the Weyl anticommutators by blocks, then conjugation; (b) unitarity in both orders, $\gamma_D^\mu$ through $\sigma^\mu$, $\bar\sigma^\mu$; (c) $u_D = U_Du$, the square-root identity proved with a positivity check of the eigenvalues; (d) with $\gamma^0_D = \operatorname{diag}(\mathbb 1, -\mathbb 1)$. Integrated as the second route of Example [[§C5a.5 Chirality and Weyl Spinors#^ex-c5a-5-1|§C5a.5.1]] The Dirac Basis Is Equivalent to the Chiral Basis ($U_D = U^\dagger$, the same change of basis read in the other direction) and the two derivations of Example [[§C5a.9 Plane-Wave Solutions#^ex-c5a-9-1|§C5a.9.1]] The Plane-Wave Spinors in the Dirac Basis. The comment's Majorana sentence is Larsen's text; ERRATA records that with $(+,-,-,-)$ it is $i\gamma^\mu$ that is real ([[§C5a.5 Chirality and Weyl Spinors#^rem-c5a-5-6|§C5a.5, ★ Remark: The Majorana basis]]).

### PS6.4 Lorentz transformations as 4×4 matrices

The Lorentz transformations are given in any representation by $\Lambda(\omega) = \exp(-\frac i2\omega_{\mu\nu}J^{\mu\nu})$, where $J^{\mu\nu}$ are the representation matrices of the algebra and $\omega_{\mu\nu}$ parametrize the group element.

*Parts: (a), (b), (c), (d).*

^ps6-4

#### (a)

For a boost along the 3rd axis the only nonvanishing $\omega_{\mu\nu}$ are $\omega_{03} = \eta$ and $\omega_{30} = -\eta$. What are the boost matrices $\Lambda(\eta)$ in the vector and spinor representations? (No derivation needed; write all components as $4\times4$ matrices, no $2\times2$ sub-matrices.)

^ps6-4-a

- [ ] Q1 **[def]** Write $(\mathcal J^{\mu\nu})^\alpha{}_\beta$ for the vector representation and $S^{\mu\nu}$ for the spinor representation (course normalization).
- [ ] Q2 Reduce $-\frac i2\omega_{\mu\nu}J^{\mu\nu}$ to a single generator for $\omega_{03} = -\omega_{30} = \eta$. Which antisymmetry is used?
- [ ] Q3 Vector: which entries of $-i\eta\,\mathcal J^{03}$ are nonzero? What is the square of that block, and what does the exponential series give?
- [ ] Q4 Spinor: compute $S^{03}$ in the chiral basis. Why can the exponential be taken entry by entry?
- [ ] Q5 **[conv]** Apply the vector $\Lambda(\eta)$ to $(m, 0, 0, 0)$: which way does $\omega_{03} = +\eta$ boost? How does Yu's passive reading of the same $\omega$ change "the rapidity" ([[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^cau-c1a-6-1|§C1a.6, Caution: Which ω is a rotation by θ]])?

> [!tip]- Hint (a): route
> **Strategy (K4).** Reduce the exponent to one generator; exponentiate a $2\times2$ block (vector) or a diagonal matrix (spinor).

#### (b)

A boost leaves invariant the components of a 4-vector transverse to the boost. Does the Dirac spinor have any invariant components?

^ps6-4-b

- [ ] Q1 **[def]** Restate "component $k$ is invariant for every $\psi$" as a condition on row $k$ of the matrix.
- [ ] Q2 Apply $\Lambda_{1/2}(\eta)$ of (a) to $\psi = (\psi_L, \psi_R)$: what happens to each of the four components?
- [ ] Q3 Show the answer holds in every basis: if row $k$ of $U\Lambda_{1/2}U^\dagger$ were a unit row, which eigenvector, with which eigenvalue, would $\Lambda_{1/2}$ have?
- [ ] Q4 **[why]** Compare with the eigenvalues of the vector boost: which directions are fixed there, and why does no spinor direction have eigenvalue $1$?

> [!tip]- Hint (b): route
> **Strategy (K4).** Read off the diagonal spinor boost; for basis independence, an invariant component is a left eigenvector with eigenvalue 1.

#### (c)

For a rotation around the third axis the only nonvanishing $\omega_{\mu\nu}$ are $\omega_{12} = \theta$ and $\omega_{21} = -\theta$. What are the corresponding group matrices $\Lambda(\theta)$ in the vector and spinor representations?

^ps6-4-c

- [ ] Q1 **[def]** Which generator remains for $\omega_{12} = -\omega_{21} = \theta$? Write $J_3$ in terms of $S^{12}$ and $\Sigma^3$.
- [ ] Q2 Vector: find the nonzero entries of $-i\theta\,\mathcal J^{12}$ (watch $g^{11} = g^{22} = -1$) and exponentiate.
- [ ] Q3 Spinor: compute $S^{12}$ in the chiral basis and exponentiate entry by entry.
- [ ] Q4 **[why]** Why is the spinor rotation matrix unitary while the spinor boost of (a) is not ([[§C5a.3 The Lorentz Action on Spinor Space#^rem-c5a-3-2|§C5a.3, Remark: Spinor boosts are not unitary]])?

> [!tip]- Hint (c): route
> **Strategy (K4).** As in (a), with $\mathcal J^{12}$ and $S^{12}$.

#### (d)

How do vectors and spinors transform under rotations by $2\pi$, i.e. rotations that go all the way back to the starting point?

^ps6-4-d

- [ ] Q1 Set $\theta = 2\pi$ in both matrices of (c). What does a vector return to, and what does a spinor return to?
- [ ] Q2 **[why]** Why is the result independent of the basis of spinor space?
- [ ] Q3 **[def]** State the rule for the sign of a $2\pi$ rotation on $(j_+, j_-)$, and check it on the vector and on the Dirac spinor (Theorem [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-17-9|§CB.17.9]] Rotation Content and the Sign of a 2π Rotation).
- [ ] Q4 At which angle does the spinor matrix first return to $\mathbb 1_4$?

> [!tip]- Hint (d): route
> **Strategy (K4).** Set $\theta = 2\pi$ in (c).

> [!tip]- Hints: definitions, results and your solution for the whole problem
> **Topic and definitions.** T7 (with T1, T8).
> - Vector generators and $\Lambda = \exp(-\frac i2\omega_{\alpha\beta}\mathcal J^{\alpha\beta})$: Definition [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-1|§C1a.6.1]] Generators of the Vector Representation; rotation and boost generators Definition [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-2|§C1a.6.2]] Rotation and Boost Generators
> - Spinor generators: Definition [[§C5a.3 The Lorentz Action on Spinor Space#^def-c5a-3-2|§C5a.3.2]] Spin Matrices of the Dirac Representation, Theorem [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-1|§C5a.3.1]] The Generators in the Chiral Basis, Example [[§C5a.3 The Lorentz Action on Spinor Space#^ex-c5a-3-1|§C5a.3.1]] The Six Spinor Generators as 4×4 Matrices
>
> **Key results.** Theorem [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-6|§C1a.6.6]] The Rotation Matrices in the Vector Representation, Theorem [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-7|§C1a.6.7]] The Boost Matrices in the Vector Representation, Theorem [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-4|§C5a.4.4]] The Rotation Matrices in the Dirac Representation, Entry by Entry, Theorem [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-5|§C5a.4.5]] The Boost Matrices in the Dirac Representation, Entry by Entry, Example [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^ex-c5a-4-1|§C5a.4.1]] One Rotation, Two Matrices, Example [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^ex-c5a-4-2|§C5a.4.2]] One Boost, Two Matrices, Theorem [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-6|§C5a.4.6]] A Boost Leaves No Spinor Component Invariant (part (b)); [[§C5a.3 The Lorentz Action on Spinor Space#^rem-c5a-3-1|§C5a.3, Remark: Why half the angle]]; [[§C5a.3 The Lorentz Action on Spinor Space#^rem-c5a-3-2|§C5a.3, Remark: Spinor boosts are not unitary]]; [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^cau-c1a-6-1|§C1a.6, Caution: Which ω is a rotation by θ]]; the sign of a $2\pi$ rotation Theorem [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-17-9|§CB.17.9]] Rotation Content and the Sign of a 2π Rotation.
>
> **Difficulty** (a) 1, (b) 2, (c) 1, (d) 1. Submitted solution: (a) vector matrix from the entries of $-i\eta\,\mathcal J^{03}$, spinor matrix from $S^{0i} = -\frac i2\operatorname{diag}(\sigma^i, -\sigma^i)$, cited from PS §3.1–§3.3; (b) "No", the diagonal matrix plus a basis-independence argument via left eigenvectors (also for any invertible change of basis); (c) the same layout; (d) $\mathbb 1_4$ and $-\mathbb 1_4$, with a remark that $-\mathbb 1_4$ is basis independent. The vault records the same signs in Theorem [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-5|§C5a.4.5]] The Boost Matrices in the Dirac Representation, Entry by Entry and Theorem [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-4|§C5a.4.4]] The Rotation Matrices in the Dirac Representation, Entry by Entry; Theorem [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-6|§C5a.4.6]] A Boost Leaves No Spinor Component Invariant is built from part (b).

### PS6.5 Chiral symmetry

The transformation $\psi \to e^{i\alpha\gamma^5}\psi$ acts on spinors for any real $\alpha$. It is called a chiral transformation.

*Parts: (a), (b), (c), (d), (e).*

^ps6-5

#### (a)

How does the conjugate spinor $\bar\psi$ transform?

^ps6-5-a

- [ ] Q1 **[def]** Define $\bar\psi$. State the Hermiticity of $\gamma^5$ and its anticommutation with $\gamma^\mu$.
- [ ] Q2 Take the adjoint of $e^{i\alpha\gamma^5}\psi$: what is $(e^{i\alpha\gamma^5})^\dagger$?
- [ ] Q3 Move $\gamma^0$ to the left through $(\gamma^5)^n$: which sign per power, and which exponential results?
- [ ] Q4 **[why]** Compare with the phase $\psi \to e^{i\alpha}\psi$: why does the exponent keep its sign in $\bar\psi$ here, while it flips for the phase?

> [!tip]- Hint (a): route
> **Strategy (K7).** Adjoint of the exponential, then move $\gamma^0$ through the power series.

#### (b)

How does the vector bilinear $V^\mu = \bar\psi\gamma^\mu\psi$ transform?

^ps6-5-b

- [ ] Q1 Write the transformed $\mathsf V^\mu$ using (a), and show $e^{i\alpha\gamma^5}\gamma^\mu = \gamma^\mu e^{-i\alpha\gamma^5}$.
- [ ] Q2 Conclude for $\mathsf V^\mu$.
- [ ] Q3 **[why]** Run the same steps for $\mathsf A^\mu = \bar\psi\gamma^\mu\gamma^5\psi$. Does the extra $\gamma^5$ change anything, and why?

> [!tip]- Hint (b): route
> **Strategy (K7).** Commute $e^{i\alpha\gamma^5}$ past $\gamma^\mu$.

#### (c)

Show that the Dirac Lagrangian $\mathcal L = \bar\psi(i\gamma^\mu\partial_\mu - m)\psi$ is invariant under chiral transformations in the massless case $m = 0$, but not for general mass $m \neq 0$.

^ps6-5-c

- [ ] Q1 **[def]** Write the free Dirac Lagrangian with the course's signs, split into kinetic and mass terms.
- [ ] Q2 Why does $\partial_\mu$ pass through $e^{i\alpha\gamma^5}$, and why is the kinetic term then invariant?
- [ ] Q3 Compute $e^{2i\alpha\gamma^5}$ as a combination of $\mathbb 1$ and $\gamma^5$, and write the transformed mass term.
- [ ] Q4 Give $\delta\mathcal L$ to first order in $\alpha$, and express it through $\mathsf P = \bar\psi\,i\gamma^5\psi$.
- [ ] Q5 **[why]** For which finite $\alpha$ is the mass term nevertheless invariant? Why is the first-order test enough to decide the whole one-parameter family (Theorem [[§C1b.5 Noether's Theorem#^thm-c1b-5-3|§C1b.5.3]] The First-Order Test Decides the Whole Family)?

> [!tip]- Hint (c): route
> **Strategy (K7).** Kinetic term as in (b); mass term via $e^{2i\alpha\gamma^5}$ and $(\gamma^5)^2 = \mathbb 1$.

#### (d)

Determine the Noether current $j^\mu_5$ that follows from the symmetry in the massless case.

^ps6-5-d

- [ ] Q1 **[def]** State Noether's theorem in the form used: the current in terms of $\partial\mathcal L/\partial(\partial_\mu\phi_i)$, $\Delta\phi_i$ and $\mathcal J^\mu$, with $\delta\phi_i = \alpha\Delta\phi_i$, $\delta\mathcal L = \alpha\partial_\mu\mathcal J^\mu$.
- [ ] Q2 Which fields enter the sum ($\psi_a$ and $\bar\psi_a$ independent)? Compute $\Delta\psi_a$ and $\Delta\bar\psi_a$.
- [ ] Q3 Compute $\partial\mathcal L/\partial(\partial_\mu\psi_a)$ and $\partial\mathcal L/\partial(\partial_\mu\bar\psi_a)$ for $m = 0$. What is $\mathcal J^\mu$, and why?
- [ ] Q4 Assemble $j^\mu_5$ as a row times a column.
- [ ] Q5 **[conv]** Compare the overall sign with the axial current $j^{\mu5} = \mathsf A^\mu$ of Theorem [[§C5a.8 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-8-4|§C5a.8.4]] The Axial Current. Which convention fixes the sign, and does it change any physical statement?

> [!tip]- Hint (d): route
> **Strategy (K12).** $\Delta\psi$, $\Delta\bar\psi$ from (a); $\partial\mathcal L/\partial(\partial_\mu\psi_a)$; $\mathcal J^\mu = 0$.

#### (e)

Compute the divergence $\partial_\mu j^\mu_5$ of the current identified in (d), using the Dirac equation for general $m$. The result should vanish for $m = 0$, but not for $m \neq 0$.

^ps6-5-e

- [ ] Q1 Apply the product rule to $\partial_\mu j^\mu_5$ and bring the second term to the form $\bar\psi\gamma^5(\gamma^\mu\partial_\mu\psi)$.
- [ ] Q2 **[def]** Write the Dirac equation and the equation for $\bar\psi$ obtained by Hermitian conjugation (mind the order of $\gamma^0$ and $\gamma^\mu$, [[§C5a.7 The Dirac Equation and Its Lagrangian#^cau-c5a-7-3|§C5a.7, Caution: The order of γ⁰ and γ^μ in the conjugate equation]]).
- [ ] Q3 Substitute both and collect.
- [ ] Q4 **[why]** Why is $\bar\psi\gamma^5\psi$ not identically zero when $m \neq 0$? Give a choice of Weyl components that shows it.
- [ ] Q5 **[why]** Read the result as Theorem [[§C1b.5 Noether's Theorem#^thm-c1b-5-5|§C1b.5.5]] The Divergence of the Current When the Test Fails: what plays the role of the first-order variation of $\mathcal L$, and is it consistent with (c)?

> [!tip]- Hint (e): route
> **Strategy (K7, K5).** Product rule, move $\gamma^5$ to the left in the second term, substitute both Dirac equations.

> [!tip]- Hints: definitions, results and your solution for the whole problem
> **Topic and definitions.** T8, T4.
> - $\gamma^5$ and its algebra: Definition [[§CB.12 Clifford Algebras꞉ Grading, Basis and the Volume Element#^def-cb-12-14|§CB.12.14]] The Matrix γ⁵, Theorem [[§CB.12 Clifford Algebras꞉ Grading, Basis and the Volume Element#^thm-cb-12-15|§CB.12.15]] Algebraic Properties of γ⁵
> - Dirac conjugate Definition [[§C5a.2 The Dirac Form#^def-c5a-2-1|§C5a.2.1]] The Dirac Conjugate; the bilinears Definition [[§C5a.6 The Dirac Conjugate and the Bilinears#^def-c5a-6-2|§C5a.6.2]] The Sixteen Bilinears; the free Dirac field Model [[§C5a.7 The Dirac Equation and Its Lagrangian#^mod-c5a-7-3|§C5a.7.3]] The Free Dirac Field
> - Generator of a transformation Definition [[§C1b.5 Noether's Theorem#^def-c1b-5-3|§C1b.5.3]] Generator of a Continuous Transformation; symmetry of the action and $\mathcal J^\mu$ Definition [[§C1b.5 Noether's Theorem#^def-c1b-5-5|§C1b.5.5]] Symmetry of the Action; the Vector 𝒥
> - Chirality projectors: Definition [[§C5a.5 Chirality and Weyl Spinors#^def-c5a-5-1|§C5a.5.1]] Chirality Projectors
>
> **Key results.** Example [[§C5a.8 Canonical Structure and Noether Currents of the Dirac Field#^ex-c5a-8-1|§C5a.8.1]] Chiral Symmetry (this problem, results 1–5); the axial current Theorem [[§C5a.8 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-8-4|§C5a.8.4]] The Axial Current; Noether Theorem [[§C1b.5 Noether's Theorem#^thm-c1b-5-4|§C1b.5.4]] Noether's Theorem; two routes to $\delta\mathcal L$ Theorem [[§C1b.5 Noether's Theorem#^thm-c1b-5-2|§C1b.5.2]] Two Routes to δℒ; divergence when the test fails Theorem [[§C1b.5 Noether's Theorem#^thm-c1b-5-5|§C1b.5.5]] The Divergence of the Current When the Test Fails; the conjugate field equation Theorem [[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-6|§C5a.7.6]] The Field Equations of the Dirac Lagrangian, [[§C5a.7 The Dirac Equation and Its Lagrangian#^cau-c5a-7-3|§C5a.7, Caution: The order of γ⁰ and γ^μ in the conjugate equation]].
>
> **Difficulty** (a) 1, (b) 1, (c) 1, (d) 2, (e) 2. Submitted solution: power-series manipulations with the $\gamma^5$ anticommutation and $(\gamma^5)^2 = \mathbb 1$ (cited from PS5, Problem 5); (c) both the finite-$\alpha$ form and the first-order variation; (d) eight independent components, $j^\mu_5 = -\bar\psi\gamma^\mu\gamma^5\psi$; (e) $\partial_\mu j^\mu_5 = -2im\,\bar\psi\gamma^5\psi$, non-vanishing shown with $\psi_R = i\psi_L$. The vault records results 1–5 in Example [[§C5a.8 Canonical Structure and Noether Currents of the Dirac Field#^ex-c5a-8-1|§C5a.8.1]] Chiral Symmetry; the overall sign opposite to $j^{\mu5}$ of Theorem [[§C5a.8 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-8-4|§C5a.8.4]] The Axial Current is the Noether sign convention of Theorem [[§C1b.5 Noether's Theorem#^thm-c1b-5-4|§C1b.5.4]] Noether's Theorem, noted there as the same statement (not an erratum).

## Problem Set 7: Discrete Transformations (due Oct 18; submitted Oct 13)

### PS7.1 Short-response questions (the midterm format)

These questions call for short answers: a formula, a number, or a phrase. No derivations are needed and none are expected; just give the result. One of the problems on the midterm will be of exactly this type, so treat this as practice with the format as well as with the material.

*Parts: (a), (b), (c), (d).*

^ps7-1

> [!tip]- Hint: route for the whole problem
> **Strategy (K8, K5, K16).** Recall, then one line of checking: dimensions from the mass terms, the Euler–Lagrange equation term by term, the Clifford relation for contractions, dimension and the $2\pi$ sign for the labels. Aim for under a minute per item.

#### (a)

In four spacetime dimensions, what are the mass dimensions of a real scalar field $\phi$, of a Dirac field $\psi$, and of the coupling $g$ in an interaction term $g\,\phi\bar\psi\psi$? Write each answer as $M^\alpha$.

^ps7-1-a

- [ ] Q1 **[def]** Mass dimension of $S$, of $d^4x$ and of $\mathcal L$ (numbers).
- [ ] Q2 $[\phi]$ as $M^\alpha$.
- [ ] Q3 $[\psi]$ as $M^\alpha$.
- [ ] Q4 $[g]$ as $M^\alpha$; relevant, marginal or irrelevant (one word)?
- [ ] Q5 **[why]** In one phrase: why do the kinetic term and the mass term give the same $[\psi]$?

#### (b)

Write the Euler–Lagrange equation of motion for the theory $\mathcal L = \frac12\partial_\mu\phi\,\partial^\mu\phi - \frac12m^2\phi^2 - \frac\lambda{3!}\phi^3$.

^ps7-1-b

- [ ] Q1 **[def]** The Euler–Lagrange equation for one scalar field (formula).
- [ ] Q2 $\partial\mathcal L/\partial(\partial_\mu\phi)$ and $\partial\mathcal L/\partial\phi$ for this $\mathcal L$ (formulas).
- [ ] Q3 The equation of motion (formula).
- [ ] Q4 **[why]** Why is the coupling written $\lambda/3!$ (phrase)? $[\lambda] = M^{?}$ (number).

#### (c)

Evaluate $\gamma_\mu\gamma^\mu$ and $\gamma_\mu\slashed k\gamma^\mu$.

^ps7-1-c

- [ ] Q1 $\gamma_\mu\gamma^\mu$ (a number times $\mathbb 1_4$).
- [ ] Q2 $\gamma_\mu\slashed k\gamma^\mu$ (formula).
- [ ] Q3 The next two on the list: $\gamma_\mu\slashed p\slashed q\gamma^\mu$ and $\gamma_\mu\slashed k\slashed p\slashed q\gamma^\mu$ (formulas).
- [ ] Q4 **[why]** Which single relation moves $\gamma^\mu$ past $\slashed k$, and where would the number of spacetime dimensions enter the answer (phrase)?

#### (d)

The finite dimensional representations of the Lorentz algebra are labelled by a pair $(j_+, j_-)$. Give the labels of a four-vector field and of a left-handed Weyl spinor.

^ps7-1-d

- [ ] Q1 **[def]** Of which two commuting sets of generators are $j_+$, $j_-$ the spins (formula for $\mathbf J_\pm$)?
- [ ] Q2 Label of a four-vector field (pair).
- [ ] Q3 Labels of a left-handed Weyl spinor, a right-handed Weyl spinor and a Dirac spinor (pairs).
- [ ] Q4 Dimension of $(j_+, j_-)$ (formula); its spins under rotations (phrase).
- [ ] Q5 **[conv]** Which sign convention for $\mathbf K$ ($K_i = \mathcal J^{0i}$ or $\mathcal J^{i0}$) decides which Weyl spinor is called $(\frac12, 0)$ (phrase)? Which one did Problem Set 5 use?

#### Extra short-response practice (Lectures 1–12)

Same format: a formula, a number or a phrase; no derivation. Not from a problem set; homes in the hints.

^ps7-1-x

- [ ] X1 (T1) In the course's convention, $\varepsilon^{0123} = ?$ and $\varepsilon_{0123} = ?$ (numbers). And in Peskin–Schroeder?
- [ ] X2 (T5) $[\hat a_{\mathbf p}, \hat a^\dagger_{\mathbf q}] = ?$ in the course normalization, and $|\mathbf p\rangle$ in terms of $\hat a^\dagger_{\mathbf p}$ and $|0\rangle$ (formulas).
- [ ] X3 (T6) The Feynman propagator of a real scalar in momentum space, with its $i\varepsilon$ (formula). Above or below which pole does the Feynman contour pass (phrase)?
- [ ] X4 (T6) $[\hat\phi(x), \hat\phi(y)]$ for spacelike $x - y$ (number); the name of the principle this expresses (phrase).
- [ ] X5 (T8) $\operatorname{tr}(\gamma^\mu\gamma^\nu) = ?$, $\bar u^r(p)u^s(p) = ?$, $\bar v^r(p)v^s(p) = ?$ (formulas).
- [ ] X6 (T7) The label $(j_+, j_-)$ of an antisymmetric tensor field $F^{\mu\nu}$ (pair); the factor a Dirac spinor acquires under a rotation by $2\pi$ (number).
- [ ] X7 (T9) $:\!\hat b^r_{\mathbf p}\hat b^{s\dagger}_{\mathbf q}\!: = ?$ (formula); the sign of the Dirac field's zero-point energy compared with the scalar's (phrase).
- [ ] X8 (T10) Under $\Theta = CPT$ a bilinear with $n$ Lorentz indices is multiplied by ? (formula); $U(\mathcal T)^2$ on a one-fermion state (number); which of $U(\mathcal P)$, $U(\mathcal C)$, $U(\mathcal T)$ is antiunitary (phrase)?

> [!tip]- Hints: where each answer lives
> - X1: [[§C1a.5 Vectors, Tensors and Index Notation#^cau-c1a-5-5|§C1a.5, Caution: The sign of ε⁰¹²³: these notes versus Peskin–Schroeder]]
> - X2: Theorem [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|§C2a.2.6]] The Mode Algebra, Definition [[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-1|§C2a.4.1]] Relativistic Normalization
> - X3: Theorem [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-9|§C2b.6.9]] The $i\varepsilon$ Prescriptions, Theorem [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-2|§C2b.6.2]] The Feynman Propagator
> - X4: Theorem [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-5|§C2b.4.5]] The Free Field Is Microcausal, Principle [[§C2b.4 Microcausality and the Commutator Function#^pr-c2b-4-1|§C2b.4.1]] Microcausality
> - X5: Theorem [[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-3|§C5a.11.3]] Traces of γ Matrices, Theorem [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-2|§C5a.10.2]] ūu = 2m, Theorem [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-4|§C5a.10.4]] v̄v = −2m
> - X6: [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^rem-c3-2-3|§C3.2, Remark: The representations met in the course]], Theorem [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-17-9|§CB.17.9]] Rotation Content and the Sign of a 2π Rotation
> - X7: Definition [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^def-c5b-3-1|§C5b.3.1]] Normal Ordering of Fermion Operators, Theorem [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-6|§C5b.3.6]] The Fermionic Zero-Point Energy Is Negative
> - X8: Theorem [[§C9.9 CPT and the CPT Theorem#^thm-c9-9-5|§C9.9.5]] The Bilinears under C, P, T and CPT, Theorem [[§C9.8 Time Reversal#^thm-c9-8-16|§C9.8.16]] Time Reversal Twice Is −1 on Fermions, Theorem [[§C9.8 Time Reversal#^thm-c9-8-2|§C9.8.2]] Time Reversal Is Antiunitary

> [!tip]- Hints: definitions, results and your solution for the whole problem
> **Topic and definitions.** T3 (parts (a), (b)), T8 (part (c)), T7 (part (d)).
> - Mass dimension: Definition [[§C1a.2 Natural Units and Dimensional Analysis#^def-c1a-2-2|§C1a.2.2]] Mass Dimension; the action is dimensionless Theorem [[§C1b.3 Mass Dimension, Locality and Power Counting#^thm-c1b-3-1|§C1b.3.1]] The Action Is Dimensionless
> - Euler–Lagrange equations: Theorem [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-4|§C1b.2.4]] Euler–Lagrange Equations for Fields
> - Feynman slash: Definition [[§C5a.7 The Dirac Equation and Its Lagrangian#^def-c5a-7-2|§C5a.7.2]] Feynman Slash
> - The representation $(j_+, j_-)$: Definition [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^def-cb-17-3|§CB.17.3]] The Representation (j₊, j₋); "acting as spin $j$" Definition [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^def-cb-17-1|§CB.17.1]] Acting as Spin j
>
> **Key results.** (a) Example [[§C1b.3 Mass Dimension, Locality and Power Counting#^ex-c1b-3-2|§C1b.3.2]] The Yukawa Coupling Is Dimensionless, Theorem [[§C1b.3 Mass Dimension, Locality and Power Counting#^thm-c1b-3-2|§C1b.3.2]] Mass Dimension of Fields, Theorem [[§C1b.3 Mass Dimension, Locality and Power Counting#^thm-c1b-3-3|§C1b.3.3]] Mass Dimension of Couplings; (b) Example [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^ex-c1b-2-2|§C1b.2.2]] The Field Equation of a Cubic Self-Interaction; (c) Theorem [[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-2|§C5a.11.2]] Contraction Identities; (d) Theorem [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^thm-c3-2-2|§C3.2.2]] The Vector Representation Is (½, ½), [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^der-c3-2-2b|Derivation §C3.2.2, second route]], Theorem [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^thm-c3-2-1|§C3.2.1]] The Representations (½, 0) and (0, ½), Theorem [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-17-7|§CB.17.7]] The Vector Representation Is (½, ½), [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^cau-c3-2-2|§C3.2, Caution: Which one is (½, 0) depends on the sign of K]], [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^cau-c3-2-3|§C3.2, Caution: Components, not states]], [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^rem-c3-2-3|§C3.2, Remark: The representations met in the course]].
>
> **Difficulty 1.** Submitted solution: boxed answers, each followed by a short justification although none was required: (a) from the mass terms; (b) term by term; (c) $(\gamma^0)^2 = \mathbb 1$, $(\gamma^i)^2 = -\mathbb 1$ and one anticommutation; (d) dimension count $(2j_+ + 1)(2j_- + 1) = 4$, then the sign of a $2\pi$ rotation to choose among $(\frac32, 0)$, $(0, \frac32)$, $(\frac12, \frac12)$, and the left-handed spinor from Problem Set 5's law ($K_i = \mathcal J^{i0}$). The vault integrates (a) as Example [[§C1b.3 Mass Dimension, Locality and Power Counting#^ex-c1b-3-2|§C1b.3.2]] The Yukawa Coupling Is Dimensionless, (b) as Example [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^ex-c1b-2-2|§C1b.2.2]] The Field Equation of a Cubic Self-Interaction, (d) as [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^der-c3-2-2b|Derivation §C3.2.2, second route]] (convention stated there; its "joint eigenvectors" are component arrays, not states, [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^cau-c3-2-3|§C3.2, Caution: Components, not states]]).

### PS7.2 P, C and T for fermion bilinears

The transformation properties of fermion bilinears under the discrete transformations $C$, $P$, $T$ are summarized in the table on PS page 71.

*Parts: (a), (b), (c).*

^ps7-2

> [!tip]- Hint: route for the whole problem
> **Strategy (K15, K5, K7).** Transform $\hat\psi$ and $\hat{\bar\psi}$, sandwich the matrix, reduce the matrix product with the Clifford relations (for $C$: transposes and the fermion swap; for $T$: complex conjugation, no swap).

#### (a)

Verify the parity transformation properties of the pseudo-vector $A^\mu = \bar\psi\gamma^\mu\gamma^5\psi$ and the tensor $T^{\mu\nu} = \bar\psi\sigma^{\mu\nu}\psi$. (The pseudo-vector is sometimes called an axial vector, hence $A^\mu$, not the gauge potential.)

^ps7-2-a

- [ ] Q1 **[def]** Write $U(\mathcal P)\hat\psi(x)U(\mathcal P)^{-1}$ and derive $U(\mathcal P)\hat{\bar\psi}(x)U(\mathcal P)^{-1}$. Where does $\eta_a^{\ast}$ come from, and why does $|\eta_a|^2$ drop out of every bilinear?
- [ ] Q2 From the Clifford relation, show $\gamma^0\gamma^\mu\gamma^0 = 2g^{\mu0}\gamma^0 - \gamma^\mu$ for every $\mu$, and rewrite it with $\mathcal P^\mu{}_\nu$.
- [ ] Q3 Compute $\gamma^0\gamma^\mu\gamma^5\gamma^0$ and conclude for $\mathsf A^\mu$: which components change sign?
- [ ] Q4 Compute $\gamma^0\sigma^{\mu\nu}\gamma^0$ (insert $(\gamma^0)^2 = \mathbb 1$ between the two $\gamma$'s) and conclude for $\mathsf T^{\mu\nu}$ in the cases $(0, i)$ and $(i, j)$.
- [ ] Q5 **[conv]** The course conjugates as $U(\mathcal P)\hat\psi U(\mathcal P)^{-1}$, Peskin–Schroeder as $P\psi P$. When do the two agree, and what changes otherwise ([[§C9.3 Parity on States, Spinors and the Dirac Field#^cau-c9-3-1|§C9.3, Caution: Which side the inverse is on, and the names of the phases]])? The problem set's $(-1)^\mu$ is not a tensor: how do the vault's statements write it ([[§C9.4 Fermion Bilinears under Parity#^cau-c9-4-3|§C9.4, Caution: The (−1)^μ notation and the lowered index of slide 23]])?

#### (b)

Verify the transformations under charge conjugation of the vector $V^\mu = \bar\psi\gamma^\mu\psi$ and the pseudo-vector $A^\mu = \bar\psi\gamma^\mu\gamma^5\psi$.

^ps7-2-b

- [ ] Q1 **[def]** Rewrite the $C$ law as $U(\mathcal C)\hat\psi U(\mathcal C)^{-1} = (\text{matrix})\,\hat\psi^{\dagger\mathsf T}$ and derive the law for the row $\hat{\bar\psi}$.
- [ ] Q2 Write $U(\mathcal C)\,\hat{\bar\psi}\Gamma\hat\psi\,U(\mathcal C)^{-1}$ with spinor indices. Why does putting the two field factors back in order cost a minus sign, and what happens to the c-number anticommutator?
- [ ] Q3 In the chiral basis, which $\gamma^\mu$ are symmetric and which antisymmetric? Show $(\gamma^\mu)^{\mathsf T}\gamma^0\gamma^2 = -\gamma^0\gamma^2\gamma^\mu$ and reduce $\gamma^0\gamma^2(\gamma^\mu)^{\mathsf T}\gamma^0\gamma^2$.
- [ ] Q4 Conclude for $\mathsf V^\mu$. Then repeat with $\Gamma = \gamma^\mu\gamma^5$: what are $(\gamma^\mu\gamma^5)^{\mathsf T}$ and $(\gamma^5)^{\mathsf T}$, and what does moving $\gamma^5$ through $\gamma^0\gamma^2$ cost?
- [ ] Q5 **[why]** List the signs that enter $\mathsf V^\mu$: $(-i)^2$, the fermion swap, the matrix identity. Which would be lost by treating $\hat\psi$ as a c-number, and what wrong conclusion would follow?
- [ ] Q6 **[why]** The steps use chiral-basis transposes. What is the basis-free form of the rule (Theorem [[§C9.6 Charge Conjugation on the Field and Bilinears#^thm-c9-6-7|§C9.6.7]] Charge Conjugation on a General Bilinear, part 2)?

#### (c)

Verify the transformations under time-reversal of the pseudo-scalar $P = i\bar\psi\gamma^5\psi$ and the vector $V^\mu = \bar\psi\gamma^\mu\psi$.

^ps7-2-c

- [ ] Q1 **[def]** What does antiunitarity of $U(\mathcal T)$ do to a c-number, to a $\gamma$-matrix entry, and to the order of a product of operators?
- [ ] Q2 Derive $U(\mathcal T)\hat{\bar\psi}U(\mathcal T)^{-1}$ from the field law. Where do $\gamma^3\gamma^1$ and the reality of $\gamma^0$ enter?
- [ ] Q3 Show $U(\mathcal T)\,\hat{\bar\psi}\Gamma\hat\psi(x)\,U(\mathcal T)^{-1} = \hat{\bar\psi}(x_T)\,\gamma^3\gamma^1\,\Gamma^{\ast}\,\gamma^1\gamma^3\,\hat\psi(x_T)$. Which chiral $\gamma$'s are real and which imaginary?
- [ ] Q4 Apply it to $\mathsf P = \hat{\bar\psi}\,i\gamma^5\hat\psi$: what happens to the $i$, and to $\gamma^5$ passing $\gamma^3\gamma^1$?
- [ ] Q5 Apply it to $\mathsf V^\mu$: which $\gamma^\mu$ commute with $\gamma^1\gamma^3$, and what does the conjugation of $\gamma^2$ add? Which components flip?
- [ ] Q6 **[why]** Why is there no fermion reordering sign under $T$, unlike under $C$?
- [ ] Q7 **[conv]** PS eq. (3.139) has $-\gamma^1\gamma^3$ where the course has $\gamma^1\gamma^3$. Does the sign affect any bilinear ([[§C9.8 Time Reversal#^cau-c9-8-4|§C9.8, Caution: Signs and names in Peskin–Schroeder and Yu]])?

> [!tip]- Hints: definitions, results and your solution for the whole problem
> **Topic and definitions.** T10.
> - The bilinears: Definition [[§C5a.6 The Dirac Conjugate and the Bilinears#^def-c5a-6-2|§C5a.6.2]] The Sixteen Bilinears; normalizations of $\sigma^{\mu\nu}$ [[§C5a.6 The Dirac Conjugate and the Bilinears#^cau-c5a-6-1|§C5a.6, Caution: Three normalizations of σ^μν]]; the $i$ in the pseudoscalar [[§C9.4 Fermion Bilinears under Parity#^cau-c9-4-1|§C9.4, Caution: The i in the pseudoscalar]]
> - Parity matrix and $\tilde x$: Definition [[§C9.1 Discrete Lorentz Transformations#^def-c9-1-2|§C9.1.2]] Parity Matrix and Parity Images; time-reversed point $x_T$ Definition [[§C9.8 Time Reversal#^def-c9-8-1|§C9.8.1]] The Time-Reversed Point
> - Transposed adjoint $\hat\psi^{\dagger\mathsf T}$: Definition [[§C9.5 Charge Conjugation on Oscillators and Spinors#^def-c9-5-2|§C9.5.2]] The Transposed Adjoint of a Field Operator; antiunitary operator Definition [[§CB.19 Projective Representations, Wigner's Theorem and Antiunitary Symmetries#^def-cb-19-4|§CB.19.4]] Antiunitary Operator
>
> **Key results.** The table Theorem [[§C9.9 CPT and the CPT Theorem#^thm-c9-9-5|§C9.9.5]] The Bilinears under C, P, T and CPT. Parity: Theorem [[§C9.3 Parity on States, Spinors and the Dirac Field#^thm-c9-3-5|§C9.3.5]] Parity on the Dirac Field, Theorem [[§C9.4 Fermion Bilinears under Parity#^thm-c9-4-1|§C9.4.1]] Parity on the Dirac Conjugate Field, Theorem [[§C9.4 Fermion Bilinears under Parity#^thm-c9-4-3|§C9.4.3]] Conjugating the Sixteen Matrices by γ⁰, Theorem [[§C9.4 Fermion Bilinears under Parity#^thm-c9-4-4|§C9.4.4]] The Sixteen Bilinears under Parity, [[§C9.4 Fermion Bilinears under Parity#^der-c9-4-4b|Derivation §C9.4.4, second route for rows 4–5]] (part (a)). Charge conjugation: Theorem [[§C9.6 Charge Conjugation on the Field and Bilinears#^thm-c9-6-2|§C9.6.2]] Charge Conjugation on the Dirac Field, Theorem [[§C9.6 Charge Conjugation on the Field and Bilinears#^thm-c9-6-4|§C9.6.4]] Charge Conjugation on ψ† and ψ̄, Theorem [[§C9.5 Charge Conjugation on Oscillators and Spinors#^thm-c9-5-4|§C9.5.4]] Transposes and Conjugates of the Chiral Dirac Matrices, Theorem [[§C9.6 Charge Conjugation on the Field and Bilinears#^thm-c9-6-6|§C9.6.6]] The Vector Current Changes Sign under Charge Conjugation, Theorem [[§C9.6 Charge Conjugation on the Field and Bilinears#^thm-c9-6-7|§C9.6.7]] Charge Conjugation on a General Bilinear, Theorem [[§C9.6 Charge Conjugation on the Field and Bilinears#^thm-c9-6-9|§C9.6.9]] The Axial Vector Is Charge-Conjugation Invariant (part (b)). Time reversal: Theorem [[§C9.8 Time Reversal#^thm-c9-8-3|§C9.8.3]] Time Reversal Conjugates Every Number in the Field, Theorem [[§C9.8 Time Reversal#^thm-c9-8-7|§C9.8.7]] Time Reversal on the Dirac Field, Theorem [[§C9.8 Time Reversal#^thm-c9-8-8|§C9.8.8]] Time Reversal on the Dirac Conjugate Field, Theorem [[§C9.8 Time Reversal#^thm-c9-8-10|§C9.8.10]] Time Reversal on a General Bilinear, Theorem [[§C9.8 Time Reversal#^thm-c9-8-12|§C9.8.12]] The Pseudoscalar Bilinear Changes Sign under Time Reversal, Theorem [[§C9.8 Time Reversal#^thm-c9-8-9|§C9.8.9]] The Vector Current under Time Reversal, [[§C9.8 Time Reversal#^der-c9-8-9b|Derivation §C9.8.9, second route]] (part (c)).
>
> **Difficulty** (a) 2, (b) 3, (c) 2. Submitted solution: (a) through $\gamma^0\gamma^\mu\gamma^0 = 2g^{\mu0}\gamma^0 - \gamma^\mu$ and PS's index-dependent sign $(-1)^\mu$ (no sum); (b) componentwise, with the fermion sign stated explicitly and the dropped c-number anticommutator justified by normal ordering, chiral-basis transposes; (c) $T$ conjugates the entries of $\Gamma$ and does not reorder. The six signs agree with the table (noted under Theorem [[§C9.9 CPT and the CPT Theorem#^thm-c9-9-5|§C9.9.5]] The Bilinears under C, P, T and CPT); the vault uses the solution as [[§C9.4 Fermion Bilinears under Parity#^der-c9-4-4b|Derivation §C9.4.4, second route for rows 4–5]], Theorem [[§C9.6 Charge Conjugation on the Field and Bilinears#^thm-c9-6-9|§C9.6.9]] The Axial Vector Is Charge-Conjugation Invariant and Theorem [[§C9.8 Time Reversal#^thm-c9-8-12|§C9.8.12]] The Pseudoscalar Bilinear Changes Sign under Time Reversal, [[§C9.8 Time Reversal#^der-c9-8-9b|Derivation §C9.8.9, second route]]; the vault writes $(-1)^\mu$ as $\mathcal P^\mu{}_\nu$ ([[§C9.4 Fermion Bilinears under Parity#^cau-c9-4-3|§C9.4, Caution: The (−1)^μ notation and the lowered index of slide 23]]).

### PS7.3 CPT for the Dirac field

CPT is the operation that performs the three discrete symmetry transformations in succession. Define $\Theta \equiv CPT$. Show that under $\Theta$ the Dirac field transforms as $\Theta\psi(x)\Theta^\dagger = \gamma^5\psi^{\ast}(-x)$, where $\psi(x)^{\ast} \equiv (\psi(x)^\dagger)^{\mathsf T}$. Take the phase associated with parity $\eta_a = 1$.

^ps7-3

- [ ] Q1 **[def]** Define $\Theta$ and $\Theta^\dagger$ as products. In which order do the three operators act on $\hat\psi(x)$ in $\Theta\hat\psi(x)\Theta^\dagger$?
- [ ] Q2 **[conv]** The problem writes $\psi^{\ast}(x) \equiv (\psi(x)^\dagger)^{\mathsf T}$. Give the vault's symbol for this object and its $a$-th component. Why do the vault notes avoid a star on a field operator ([[§C9.5 Charge Conjugation on Oscillators and Spinors#^cau-c9-5-1|§C9.5, Caution: Names for the transposed adjoint]])?
- [ ] Q3 Apply $U(\mathcal T)$, then $U(\mathcal P)$ with $\eta_a = 1$: which matrix and which argument after two steps? Why may $U(\mathcal P)$ and then $U(\mathcal C)$ pass through the c-number matrices produced by the earlier steps unchanged?
- [ ] Q4 Apply $U(\mathcal C)$ to $\hat\psi(-x)$ and write $-i(\hat{\bar\psi}\gamma^0\gamma^2)^{\mathsf T}$ as a matrix times $\hat\psi^{\dagger\mathsf T}(-x)$.
- [ ] Q5 Reduce $\gamma^1\gamma^3\gamma^0\gamma^2$ to a multiple of $\gamma^5$. Which commutations are used, and which definition of $\gamma^5$ (with which sign convention behind it)?
- [ ] Q6 **[why]** Why must the image contain $\hat\psi^{\dagger\mathsf T}$ rather than $\hat\psi$ (what does $\Theta$ do to particles and antiparticles)? Where would $\eta_a$ appear for a general phase ([[§C9.9 CPT and the CPT Theorem#^cau-c9-9-1|§C9.9, Caution: The transposed adjoint in CPT]])?

> [!tip]- Hints: definitions, results, route, your solution
> **Topic and definitions.** T10.
> - $\Theta$: Definition [[§C9.9 CPT and the CPT Theorem#^def-c9-9-1|§C9.9.1]] The CPT Operator Θ; it is antiunitary Theorem [[§C9.9 CPT and the CPT Theorem#^thm-c9-9-2|§C9.9.2]] Θ Is Antiunitary
> - Transposed adjoint: Definition [[§C9.5 Charge Conjugation on Oscillators and Spinors#^def-c9-5-2|§C9.5.2]] The Transposed Adjoint of a Field Operator, [[§C9.5 Charge Conjugation on Oscillators and Spinors#^cau-c9-5-1|§C9.5, Caution: Names for the transposed adjoint]]
> - $\gamma^5$: Definition [[§CB.12 Clifford Algebras꞉ Grading, Basis and the Volume Element#^def-cb-12-14|§CB.12.14]] The Matrix γ⁵; the sign of $\varepsilon^{0123}$ [[§C1a.5 Vectors, Tensors and Index Notation#^cau-c1a-5-5|§C1a.5, Caution: The sign of ε⁰¹²³: these notes versus Peskin–Schroeder]]
>
> **Key results.** Theorem [[§C9.9 CPT and the CPT Theorem#^thm-c9-9-3|§C9.9.3]] CPT on the Dirac Field (this problem, with $\eta_a$); [[§C9.9 CPT and the CPT Theorem#^der-c9-9-3b|Derivation §C9.9.3, second route]] (the user's route); Theorem [[§C9.9 CPT and the CPT Theorem#^thm-c9-9-1|§C9.9.1]] The Three Matrices Multiply to γ⁵; Theorem [[§C9.9 CPT and the CPT Theorem#^thm-c9-9-4|§C9.9.4]] CPT in Another Order; [[§C9.9 CPT and the CPT Theorem#^cau-c9-9-1|§C9.9, Caution: The transposed adjoint in CPT]]; the three field laws Theorem [[§C9.3 Parity on States, Spinors and the Dirac Field#^thm-c9-3-5|§C9.3.5]] Parity on the Dirac Field, Theorem [[§C9.6 Charge Conjugation on the Field and Bilinears#^thm-c9-6-2|§C9.6.2]] Charge Conjugation on the Dirac Field, Theorem [[§C9.8 Time Reversal#^thm-c9-8-7|§C9.8.7]] Time Reversal on the Dirac Field.
>
> **Strategy (K15, K5).** Act from the inside out ($T$ first, then $P$, then $C$), collect the c-number matrices, reduce their product to $\gamma^5$.
>
> **Difficulty 2.** Submitted solution: the inside-out order stated first; the $C$ step on $\hat\psi(-x)$ via $\hat{\bar\psi}\gamma^0\gamma^2 = \hat\psi^\dagger\gamma^2$ and $(\gamma^2)^{\mathsf T} = \gamma^2$; then $\gamma^1\gamma^3\gamma^0\gamma^2 = i\gamma^5$ and the boxed result. The vault states it with the phase, $\eta_a\gamma^5\hat\psi^{\dagger\mathsf T}(-x)$, in Theorem [[§C9.9 CPT and the CPT Theorem#^thm-c9-9-3|§C9.9.3]] CPT on the Dirac Field, with this solution as [[§C9.9 CPT and the CPT Theorem#^der-c9-9-3b|Derivation §C9.9.3, second route]].

### PS7.4 C, P and T for the complex boson

Adapted from PS Problem 3.7(b)+(c); questions renumbered, notation more careful.

*Parts: (a), (b), (c).*

^ps7-4

#### (a)

Let $\phi(x)$ be a complex-valued Klein–Gordon field (PS Problem 2.2, HW3 Problem 2). Find unitary operators $\mathcal P$, $\mathcal C$, and an anti-unitary operator $\mathcal T$, that give $\mathcal P\phi(t, \mathbf x)\mathcal P^\dagger = \phi(t, -\mathbf x)$, $\mathcal C\phi(t, \mathbf x)\mathcal C^\dagger = \phi^{\ast}(t, \mathbf x)$, $\mathcal T\phi(t, \mathbf x)\mathcal T^\dagger = \phi(-t, \mathbf x)$. The operators should all be defined by their action on the annihilation operators $a_{\mathbf p}$, $b_{\mathbf p}$ for the particles and antiparticles.

^ps7-4-a

- [ ] Q1 **[def]** Write $\hat\phi(x)$ and $\hat\phi^\dagger(x)$ in modes. Which operator multiplies $e^{-ip\cdot x}$ in each?
- [ ] Q2 For a linear $O$ and for an antilinear $O$, write $O\hat\phi(x)O^{-1}$ in terms of $O\hat a_{\mathbf p}O^{-1}$, $O\hat b^\dagger_{\mathbf p}O^{-1}$ and the exponentials.
- [ ] Q3 **[why]** Why may the coefficients of $e^{-ip\cdot x}$ and $e^{+ip\cdot x}$ be matched separately?
- [ ] Q4 **[why]** Show that a map $\hat a_{\mathbf p} \mapsto \hat c^\dagger_{\mathbf k}$ (annihilator to creator) contradicts the mode algebra. Which sign comes out wrong?
- [ ] Q5 Parity: write $\hat\phi(\tilde x)$ as an expansion in $x$ and read off $U(\mathcal P)$ on $\hat a_{\mathbf p}$ and $\hat b_{\mathbf p}$. Why is the antilinear option excluded?
- [ ] Q6 Charge conjugation: match $\hat\phi^\dagger(x)$ and read off $U(\mathcal C)$ on $\hat a_{\mathbf p}$, $\hat b_{\mathbf p}$.
- [ ] Q7 Time reversal: using $p\cdot x_T = -\tilde p\cdot x$, show that the annihilators in $\hat\phi(x_T)$ multiply $e^{+ip\cdot x}$. Which option survives, and what does that imply for $U(\mathcal T)$?

> [!tip]- Hint (a): route
> **Strategy (K9, K15, K11).** Conjugate the mode expansion (linear or antilinear), write the required image as a mode expansion in $x$ (relabel $\mathbf p \to -\mathbf p$), match the coefficients of $e^{\mp ip\cdot x}$; the mode algebra excludes mapping annihilators to creators.

#### (b)

Find the transformation properties of the current $J^\mu = i[\phi^{\ast}(\partial^\mu\phi) - (\partial^\mu\phi^{\ast})\phi]$ under $\mathcal P$, $\mathcal C$ and $\mathcal T$.

^ps7-4-b

- [ ] Q1 **[conv]** As an operator, how is the problem's $J^\mu$ related to the vault's current $\hat j^\mu$ of Theorem [[§C9.10 C, T and CPT for the Complex Scalar Field#^thm-c9-10-4|§C9.10.4]] The U(1) Current under P, C and T, and does the relation change any of the $P$, $C$, $T$ signs?
- [ ] Q2 **[def]** From (a), derive the images of $\hat\phi^\dagger(x)$ under $U(\mathcal P)$, $U(\mathcal C)$, $U(\mathcal T)$.
- [ ] Q3 How does $\partial^\mu\hat\phi$ transform under each (chain rule at $\tilde x$ and $x_T$)? Why does conjugation commute with $\partial_\mu$ even for the antilinear $U(\mathcal T)$?
- [ ] Q4 Parity: collect the factor carried by both terms.
- [ ] Q5 Time reversal: name the two sources of sign (the derivative and the $i$) and combine them.
- [ ] Q6 **[why]** Charge conjugation: after $\hat\phi \leftrightarrow \hat\phi^\dagger$, why may each product be put back in order without a sign? What is dropped, and why is that allowed?

> [!tip]- Hint (b): route
> **Strategy (K15, K11).** Transform $\hat\phi^\dagger$ with (a), carry the chain rule through the derivatives, count the signs (and the $i$ under $T$).

#### (c)

Argue that any Hermitian, local, Lorentz-scalar operator built from a Dirac spinor $\psi(x)$, a complex scalar $\phi(x)$ and their conjugates is invariant under CPT. Not a formal proof: a qualitative argument that captures why the conclusion is difficult to avoid.

^ps7-4-c

- [ ] Q1 **[def]** State what "Hermitian, local, Lorentz-scalar operator" allows: which products, at which points, with which contractions; are pseudoscalars included?
- [ ] Q2 Compose the scalar laws of (a) to get $\Theta\hat\phi(x)\Theta^{-1}$, and recall $\Theta\hat\psi(x)\Theta^{-1}$ from Problem 3.
- [ ] Q3 What does $PT$ do to the argument of a local operator? What sign does each Lorentz index acquire (a derivative, a vector bilinear, the current of (b))?
- [ ] Q4 Show that $C$, with the antilinearity of $T$, acts on a term $c\,\hat X_1\cdots\hat X_k$ as Hermitian conjugation up to $(-1)^n$. Why does the reversed order cost nothing?
- [ ] Q5 **[why]** Why is $n$ even for a Lorentz scalar, and which hypothesis (Hermitian, local, scalar) removes which obstruction? Why is the action, not only the density at a point, invariant?
- [ ] Q6 **[why]** What does the CPT theorem (Theorem [[§C9.9 CPT and the CPT Theorem#^thm-c9-9-6|§C9.9.6]] The CPT Theorem) assert beyond this argument, and what would a proof need ([[§C9.9 CPT and the CPT Theorem#^der-c9-9-6b|★ Derivation §C9.9.6, beyond the lecture)]] for one ingredient)?

> [!tip]- Hint (c): route
> **Strategy (K14, K15).** $\Theta$ on the building blocks; then $x \to -x$, a sign per Lorentz index, and Hermitian conjugation; contracted indices come in even numbers.

> [!tip]- Hints: definitions, results and your solution for the whole problem
> **Topic and definitions.** T10 (with T5).
> - The free complex scalar quantum field: Model [[§C2a.5 The Complex Scalar Field and Its Charge#^mod-c2a-5-1|§C2a.5.1]] The Free Complex Scalar Quantum Field; mode expansion Theorem [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-2|§C2a.5.2]] Mode Expansion of the Complex Field; mode algebra Theorem [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-3|§C2a.5.3]] Mode Algebra of the Complex Field
> - Parity, charge conjugation and time reversal on its Fock space: Definition [[§C9.2 Parity of the Scalar Field#^def-c9-2-1|§C9.2.1]] Parity on the Hilbert Space of the Complex Scalar Field, Definition [[§C9.10 C, T and CPT for the Complex Scalar Field#^def-c9-10-1|§C9.10.1]] Charge Conjugation on the Hilbert Space of the Complex Scalar Field, Definition [[§C9.10 C, T and CPT for the Complex Scalar Field#^def-c9-10-2|§C9.10.2]] Time Reversal on the Hilbert Space of the Complex Scalar Field; antiunitary operator Definition [[§CB.19 Projective Representations, Wigner's Theorem and Antiunitary Symmetries#^def-cb-19-4|§CB.19.4]] Antiunitary Operator
> - The U(1) current: Theorem [[§C1b.6 Conserved Charges and Internal Symmetries#^thm-c1b-6-3|§C1b.6.3]] The U(1) Current of the Complex Scalar Field, [[§C1b.6 Conserved Charges and Internal Symmetries#^cau-c1b-6-3|§C1b.6, Caution: Sign and normalization of the U(1) current]]; the problem's $\phi^{\ast}$ as $\hat\phi^\dagger$ [[§C9.10 C, T and CPT for the Complex Scalar Field#^cau-c9-10-1|§C9.10, Caution: The star of a scalar field operator is the adjoint]]
>
> **Key results.** Parity Theorem [[§C9.2 Parity of the Scalar Field#^thm-c9-2-2|§C9.2.2]] Parity on the Complex Scalar Field, Theorem [[§C9.2 Parity of the Scalar Field#^thm-c9-2-4|§C9.2.4]] Parity on the Adjoint Field, Theorem [[§C9.2 Parity of the Scalar Field#^thm-c9-2-5|§C9.2.5]] Parity on the Derivatives of the Field; Theorem [[§C9.10 C, T and CPT for the Complex Scalar Field#^thm-c9-10-1|§C9.10.1]] Charge Conjugation on the Complex Scalar Field, Theorem [[§C9.10 C, T and CPT for the Complex Scalar Field#^thm-c9-10-2|§C9.10.2]] Time Reversal on the Complex Scalar Field, Theorem [[§C9.10 C, T and CPT for the Complex Scalar Field#^thm-c9-10-3|§C9.10.3]] Charge Conjugation and Time Reversal on the Derivatives, Theorem [[§C9.10 C, T and CPT for the Complex Scalar Field#^thm-c9-10-4|§C9.10.4]] The U(1) Current under P, C and T, Theorem [[§C9.10 C, T and CPT for the Complex Scalar Field#^thm-c9-10-6|§C9.10.6]] CPT on the Complex Scalar Field; time reversal must be antilinear Theorem [[§C9.8 Time Reversal#^thm-c9-8-1|§C9.8.1]] Time Reversal Must Be Antilinear; part (c): Example [[§C9.9 CPT and the CPT Theorem#^ex-c9-9-2|§C9.9.2]] Why a Hermitian, Local Lorentz Scalar Is CPT Invariant (a Qualitative Argument), Theorem [[§C9.9 CPT and the CPT Theorem#^thm-c9-9-6|§C9.9.6]] The CPT Theorem, [[§C9.9 CPT and the CPT Theorem#^der-c9-9-6b|★ Derivation §C9.9.6, beyond the lecture)]].
>
> **Difficulty** (a) 3, (b) 2, (c) 3. Submitted solution: (a) a general linear/antilinear step, matching of $e^{\mp ip\cdot x}$, and the commutator argument excluding annihilator-to-creator maps, giving all phases $1$ (the tex source also carries a commented-out note with three reasons why $T$ is antiunitary, not part of the submitted text); (b) $(-1)^\mu J^\mu(\tilde x)$, $-J^\mu(x)$, $(-1)^\mu J^\mu(x_T)$, the $C$ step via bosonic reordering under normal ordering; (c) $\Theta\hat O(x)\Theta^\dagger = (-1)^n\hat O^\dagger(-x)$, then even $n$ and Hermiticity, with a closing remark on the complexified Lorentz group. The vault integrates (a)–(b) in [[§C9.10 C, T and CPT for the Complex Scalar Field|§C9.10]] C, T and CPT for the Complex Scalar Field (Definition [[§C9.10 C, T and CPT for the Complex Scalar Field#^def-c9-10-1|§C9.10.1]] Charge Conjugation on the Hilbert Space of the Complex Scalar Field, Definition [[§C9.10 C, T and CPT for the Complex Scalar Field#^def-c9-10-2|§C9.10.2]] Time Reversal on the Hilbert Space of the Complex Scalar Field, Theorem [[§C9.10 C, T and CPT for the Complex Scalar Field#^thm-c9-10-4|§C9.10.4]] The U(1) Current under P, C and T: the same rules for $\hat j^\mu = -J^\mu$) and (c) as Example [[§C9.9 CPT and the CPT Theorem#^ex-c9-9-2|§C9.9.2]] Why a Hermitian, Local Lorentz Scalar Is CPT Invariant (a Qualitative Argument).

## Technique codes
The moves named in the hints; where each is used, with the boxes: [[PHY 513 Midterm Review#Techniques: the moves of 513|Midterm Review: Techniques]].
- **K1** invariants in a convenient frame
- **K2** index calculus and dummy renaming
- **K3** Lorentz commutators by index contraction
- **K4** exponentiating a generator (projectors, half angles)
- **K5** γ-matrix algebra and traces
- **K6** on-shell replacement, Gordon
- **K7** conjugating bilinears, chirality projectors
- **K8** dimensional analysis, power counting
- **K9** mode substitution (δ³, p → −p, E₋ₚ = Eₚ, normal ordering)
- **K10** extracting mode operators (KG product; u†, v† orthogonality)
- **K11** (anti)commutator algebra, BCH
- **K12** Noether recipe (Δφ, 𝒥^μ, current, charge)
- **K13** contours, iε, δ(f(x)), Sokhotski–Plemelj
- **K14** Lorentz-invariance arguments (equal-time frame, microcausality)
- **K15** a discrete symmetry on a field (act on modes, rewrite spinors, read off the matrix)
- **K16** identifying a representation (intertwiner, or Casimirs + classification)
