---
type: review
subject: "[[Quantum Field Theory]]"
tags: [quantum-field-theory, phy513, review]
---
↑ [[Quantum Field Theory]] · [[PHY 513 Midterm Review|Midterm Review]] · [[PHY 513 PS Drill|PS Drill]]

# PHY 513 Notes Drill: definitions, derivations, class exercises

The companion of the [[PHY 513 PS Drill|PS Drill]] for what the problem sets do not cover:
- every definition and convention of the Midterm Review's Language lists, stated exactly with signs and factors (and, for conventions, course vs Peskin–Schroeder vs Yu: [[Larsen PHY 513]]);
- the core derivations, ★★ (done on the slides) and ★ (supporting), as ordered questions that rebuild them;
- **everything Larsen left as an exercise or a "check this"** in class, tagged **[class exercise, Lecture N]**;
- the equivalences between the course's versions of one object (the table "How the objects grew" in [[PHY 513 Midterm Review]]), in the last section.

Levels: **★★** core (a derivation done on the slides), **★** supporting. These are review levels; a ★ inside a note's name or before a box's kind word ("★ Theorem") is the notes' own mark for material beyond the course.

Question tags: **[state]** and **[def]** state exactly, with every sign and factor; **[why]** why a step holds or what fails without a hypothesis; **[conv]** a sign or convention check. The route in the notes is folded under **Hints**. An item that is a problem-set part points to the PS Drill instead of repeating it.

# T1. Relativity, index notation and natural units

## Definitions and conventions T1

### Natural units
Natural units set $\hbar = c = 1$, so that $M = E = L^{-1} = T^{-1}$, with $\hbar c \simeq 197.3$ MeV fm and $\hbar \simeq 6.582\times10^{-22}$ MeV s, see Definition [[§C1a.2 Natural Units and Dimensional Analysis#^def-c1a-2-1|§C1a.2.1]] Natural Units. *Source: Lecture 2 (Sep 2), slides "Dimensional Analysis", "Mass Dimensions" · the user's notes Ch. 2 §2.4*

^nd-def-c1a-2-1

- [ ] Q1 **[def]** State what natural units set equal to one, and which kinds of quantity are then measured in one common unit.
- [ ] Q2 **[def]** Give the two conversion constants of the course ($\hbar c$ in MeV fm, $\hbar$ in MeV s), and convert $1\ \text{GeV}^{-1}$ into a length and into a time.
- [ ] Q3 **[why]** Why can a natural-units number such as $1\ \text{GeV}^{-1}$ not be converted back without knowing what it measures? What decides the reading?
- [ ] Q4 **[conv]** Do the course, PS and Yu use the same units? Which electromagnetic units go with them?

> [!tip]- Hints: route in the notes
> - Technique: K8 (dimensional analysis)
> - The readings of one number: [[§C1a.2 Natural Units and Dimensional Analysis#^cau-c1a-2-1|§C1a.2, Caution: One number, several readings]]; restoring them is Theorem [[§C1a.2 Natural Units and Dimensional Analysis#^thm-c1a-2-1|§C1a.2.1]] The Exponent Rule.
> - Units row of the register `Larsen PHY 513`; electromagnetic units Definition [[§C1a.7 Relativistic Electrodynamics in Index Form#^def-c1a-7-1|§C1a.7.1]] Heaviside–Lorentz Natural Units.

### Mass dimension
Every quantity has one mass dimension $[Q] = d$: a pure number times $(\text{mass})^d$, with $d = 1$ for masses, energies, momenta, $d = -1$ for lengths and times, $d = 0$ for velocities, actions and angular momenta, see Definition [[§C1a.2 Natural Units and Dimensional Analysis#^def-c1a-2-2|§C1a.2.2]] Mass Dimension. *Source: Lecture 2 (Sep 2), slide "Mass Dimensions" ("$M \sim$ energy $\sim 1/L$") · the user's notes Ch. 2 §2.4*

^nd-def-c1a-2-2

- [ ] Q1 **[def]** Define the mass dimension $[Q]$ of a quantity in natural units.
- [ ] Q2 Give $[\cdot]$ of a mass, an energy, a momentum, a length, a time, a velocity, an action, an angular momentum.
- [ ] Q3 **[why]** Why are velocity and action dimensionless once $\hbar = c = 1$?
- [ ] Q4 Give $[\partial_\mu]$, $[d^4x]$, $[\mathcal L]$ and $[\phi]$ for the canonically normalized scalar (Lecture 2's list).

> [!tip]- Hints: route in the notes
> - Technique: K8
> - The table of common quantities: [[§C1a.2 Natural Units and Dimensional Analysis#^rem-c1a-2-2|§C1a.2, Remark: Mass dimensions of common quantities]]; the counting rules Theorem [[§C1a.2 Natural Units and Dimensional Analysis#^thm-c1a-2-3|§C1a.2.3]] Rules of Dimensional Counting; the field and density: Theorem [[§C1b.3 Mass Dimension, Locality and Power Counting#^thm-c1b-3-1|§C1b.3.1]] The Action Is Dimensionless, Theorem [[§C1b.3 Mass Dimension, Locality and Power Counting#^thm-c1b-3-2|§C1b.3.2]] Mass Dimension of Fields.

### Lorentz transformation, active reading
A Lorentz transformation is a real $4\times4$ matrix with $\Lambda^{\mathsf T}g\Lambda = g$, $g = \operatorname{diag}(1, -1, -1, -1)$; the course reads it actively ($x \mapsto \Lambda x$, one observer), see Definition [[§C1a.4 The Lorentz Group#^def-c1a-4-1|§C1a.4.1]] Lorentz Transformation, Active Reading. *Source: Lecture 1 (Aug 31), slides "The Lorentz Group", "Four - Vectors" · the user's notes Ch. 1 §§1.2–1.3*

^nd-def-c1a-4-1

- [ ] Q1 **[def]** State the defining condition of the Lorentz group in matrix form and in components; write the metric.
- [ ] Q2 **[def]** What do "active" and "passive" readings of the same matrix mean? Which does the course use?
- [ ] Q3 **[conv]** Course and PS versus Yu: which reading does each use, and how is Yu's passive boost to velocity $\beta$ related to the active boost matrix?
- [ ] Q4 **[def]** What does "Lorentz invariant" mean in field theory: invariant under which subgroup of $O(1,3)$?
- [ ] Q5 **[why]** Which statements are the same in both readings, and which change sign?

> [!tip]- Hints: route in the notes
> - Technique: K14
> - Readings: [[§C1a.4 The Lorentz Group#^cau-c1a-4-1|§C1a.4, Caution: Active and passive readings]]; the subgroup: [[§C1a.4 The Lorentz Group#^rem-c1a-4-1|§C1a.4, Remark: What "Lorentz invariant" means in field theory]], with the components Theorem [[§CB.3 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-3-12|§CB.3.12]] The Four Components Are the Cosets of SO⁺(1,3).
> - Register row "Lorentz transformations" in `Larsen PHY 513`.

### Active rotation, boost and rapidity
The active rotation by $\theta$ about $z$ and the active boost along $z$, $B_z = \gamma\begin{pmatrix}1 & v\\ v & 1\end{pmatrix}$ on $(t, z)$, with rapidity $\tanh\eta = v$, $B_z(\eta) = \begin{pmatrix}\cosh\eta & \sinh\eta\\ \sinh\eta & \cosh\eta\end{pmatrix}$, see Definition [[§C1a.4 The Lorentz Group#^def-c1a-4-2|§C1a.4.2]] Active Rotation and Boost and Definition [[§C1a.4 The Lorentz Group#^def-c1a-4-3|§C1a.4.3]] Rapidity. *Source: Lecture 1 (Aug 31), slides "(Special) Theory of Relativity", "General Lorentz transformations" · the user's notes Ch. 1 §1.2*

^nd-def-c1a-4-3

- [ ] Q1 **[def]** Write the active boost along $z$ in terms of $v$ and $\gamma$, and in terms of the rapidity. Where does it send a particle at rest?
- [ ] Q2 **[def]** Define the rapidity and express $\cosh\eta$, $\sinh\eta$ through $v$ and $\gamma$.
- [ ] Q3 **[conv]** The Lecture 1 slide writes the rotation about $z$ with $+\sin\theta$ in the upper-right entry. Is it active or passive? What is the active rotation by $\theta$ in terms of that matrix?
- [ ] Q4 **[why]** Why do two boosts along the same axis compose by adding rapidities but not velocities?

> [!tip]- Hints: route in the notes
> - Technique: K14
> - The slide's rotation: [[§C1a.4 The Lorentz Group#^cau-c1a-4-3|§C1a.4, Caution: The slides' rotation matrix is passive]].
> - For Q4: multiply two $B_z(\eta)$ and use the addition formulas for cosh and sinh.

### Four-vectors, index positions and the d'Alembertian
$x^\mu = (t, \mathbf x)$, $x_\mu = g_{\mu\nu}x^\nu = (t, -\mathbf x)$, $x^2 = t^2 - \mathbf x^2$, $p^2 = E^2 - \mathbf p^2 = m^2$, $\partial_\mu = (\partial_t, \nabla)$, $\partial^\mu = (\partial_t, -\nabla)$, $\partial^2 = \partial_t^2 - \nabla^2$, see Definition [[§C1a.5 Vectors, Tensors and Index Notation#^def-c1a-5-1|§C1a.5.1]] Four-Vectors and Index Positions in Natural Units. *Source: Lecture 1 (Aug 31), slides "Invariants", "Index Gymnastics"; Lecture 2 (Sep 2), slides "Derivatives", "Klein Gordon Equation" · the user's notes Ch. 1 §1.4, Ch. 2 §2.3*

^nd-def-c1a-5-1

- [ ] Q1 **[def]** Write $x^\mu$, $x_\mu$, $p^\mu$, $p\cdot x$ and the mass-shell condition with the course's metric.
- [ ] Q2 **[def]** Write $\partial_\mu$ and $\partial^\mu$ in components. Which one has no minus sign on its spatial part, and why (Lecture 2)?
- [ ] Q3 **[conv]** The d'Alembertian: which symbol do the course, PS and Yu use, and what sign has Griffiths' $\Box^2$ relative to $\partial^2$?
- [ ] Q4 **[why]** $a^\mu b_\mu$ is a plain sum of four products. Where does the minus sign of $a^0b^0 - \mathbf a\cdot\mathbf b$ come from? With which sign does $\nabla\cdot\mathbf j$ enter $\partial_\mu j^\mu$?
- [ ] Q5 **[def]** Name the three "deltas" $\delta^\mu{}_\nu$, $g_{\mu\nu}$, $\delta_{ij}$. Which are Lorentz tensors, and what are $\delta^\mu{}_\mu$ and $g_{\mu\nu}g^{\mu\nu}$?

> [!tip]- Hints: route in the notes
> - Technique: K2
> - Names: [[§C1a.5 Vectors, Tensors and Index Notation#^cau-c1a-5-8|§C1a.5, Caution: Names for the d'Alembertian]]; plain sums: [[§C1a.5 Vectors, Tensors and Index Notation#^cau-c1a-5-1|§C1a.5, Caution: A contraction is a plain sum; the signs live in the components]]; deltas: [[§C1a.5 Vectors, Tensors and Index Notation#^cau-c1a-5-3|§C1a.5, Caution: Three deltas that are not the same object]].
> - Why $\partial_\mu$ carries a lower index: Theorem [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-7|§C1a.5.7]] Basic Derivative Identities and Theorem [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-10|§C1a.5.10]] Derivatives with Respect to a Four-Vector, part 1.

### Index bookkeeping: legal terms and matrix products
Within a term an index appears at most twice, once up and once down; free indices agree on both sides; an index expression is a matrix product when each contraction joins the second index of one factor to the first of the next, see [[§C1a.5 Vectors, Tensors and Index Notation#^cau-c1a-5-2|§C1a.5, Caution: Index bookkeeping: legal, illegal, and matrix products]]. *Source: the user's notes Ch. 1 §1.4 · PS1.1–1.2*

^nd-cau-c1a-5-2

→ drilled as [[PHY 513 PS Drill#^ps1-1|PS1.1]] and [[PHY 513 PS Drill#^ps1-2|PS1.2]]

### The sign of the Levi-Civita symbol
The course and Yu take $\varepsilon^{0123} = +1$, hence $\varepsilon_{0123} = -1$; Peskin–Schroeder take $\varepsilon^{0123} = -1$, and every quantity with one $\varepsilon$ flips sign between them, see [[§C1a.5 Vectors, Tensors and Index Notation#^cau-c1a-5-5|§C1a.5, Caution: The sign of ε⁰¹²³: these notes versus Peskin–Schroeder]]. *Source: PS1 Problem 3 (the definition) · the user's notes Ch. 1 §1.5*

^nd-cau-c1a-5-5

- [ ] Q1 **[def]** Define the Levi-Civita symbol $\varepsilon^{\mu\nu\rho\sigma}$ (PS1 Problem 3) and give the course's $\varepsilon_{0123}$. Why does lowering all four indices cost a sign?
- [ ] Q2 **[conv]** State the value of $\varepsilon^{0123}$ in the course, in PS and in Yu.
- [ ] Q3 **[conv]** Which of these change sign between the course and PS: $\tilde F^{\mu\nu}$, $F_{\mu\nu}F^{\mu\nu}$, $\varepsilon^{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma}$, $\varepsilon_{\mu\nu\rho\sigma}\varepsilon^{\mu\nu\rho\sigma}$?
- [ ] Q4 **[why]** How can one compare a pseudoscalar sign between two sources safely without trusting their stated $\varepsilon$?
- (The values $\varepsilon^{0123}$, $\varepsilon^{1230}$, $\varepsilon^{1213}$ → drilled as [[PHY 513 PS Drill#^ps1-3-a|PS1.3(a)]].)

> [!tip]- Hints: route in the notes
> - Technique: K2
> - $FF$ and $F\tilde F$ in both conventions: Theorem [[§C1a.7 Relativistic Electrodynamics in Index Form#^thm-c1a-7-2|§C1a.7.2]] Duality Exchanges E and B; the Two Invariants, part 2 and step 6 of its derivation.
> - Register row "Levi-Civita"; the γ-matrix route ($\gamma^0\gamma^1\gamma^2\gamma^3 = -i\gamma^5$) is in the register and the skill's notation rules.

### Mandelstam variables
For $1 + 2 \to 3 + 4$ on shell, $s = (p_1 + p_2)^2$, $t = (p_1 - p_3)^2$, $u = (p_1 - p_4)^2$; $s$ is the squared centre-of-mass energy, $t$ the squared momentum transfer, see Definition [[§C1a.5 Vectors, Tensors and Index Notation#^def-c1a-5-2|§C1a.5.2]] Mandelstam Variables. *Source: PS1 Problem 5 · the user's notes Ch. 1 §1.4*

^nd-def-c1a-5-2

- [ ] Q1 **[def]** Define $s$, $t$, $u$ for a two-body process. Which momentum transfer is $t$ the square of, and why are $p_1 - p_3$ and $p_4 - p_2$ the same vector?
- [ ] Q2 **[why]** Why is $s$ the squared centre-of-mass energy? Evaluate it in the centre-of-mass frame.
- [ ] Q3 **[why]** Why is it better to compute $s$ than to transform energies between frames (Lecture 1, "Invariants")?

> [!tip]- Hints: route in the notes
> - Technique: K1 (invariants in a convenient frame)
> - [[§C1a.5 Vectors, Tensors and Index Notation#^rem-c1a-5-1|§C1a.5, Remark: Compute invariants, not transformations]]; the lab form of $s$ → PS1.5(b).

### Heaviside–Lorentz natural units
Field theory measures electromagnetism in Heaviside–Lorentz units with $\hbar = c = 1$: Maxwell's equations without $4\pi$, Coulomb's potential $Q/4\pi r$, $\alpha = e^2/4\pi \approx 1/137$, see Definition [[§C1a.7 Relativistic Electrodynamics in Index Form#^def-c1a-7-1|§C1a.7.1]] Heaviside–Lorentz Natural Units. *Source: register (units row) · the user's notes Ch. 1 §1.7*

^nd-def-c1a-7-1

- [ ] Q1 **[def]** Write Maxwell's equations and the Lorentz force in Heaviside–Lorentz natural units.
- [ ] Q2 **[def]** Where does the $4\pi$ go, and what is $e$ in terms of $\alpha$?
- [ ] Q3 **[why]** Why can $\hbar$, $c$, $\varepsilon_0$ and $e$ not all be set to $1$?
- [ ] Q4 **[conv]** How do Gaussian charges and fields differ from Heaviside–Lorentz ones?

> [!tip]- Hints: route in the notes
> - Technique: K8
> - The dictionary: Theorem [[§C1a.7 Relativistic Electrodynamics in Index Form#^thm-c1a-7-4|§C1a.7.4]] The SI–Heaviside–Lorentz Dictionary; the charge row of [[§C1a.2 Natural Units and Dimensional Analysis#^rem-c1a-2-2|§C1a.2, Remark: Mass dimensions of common quantities]].

### Four-potential and field-strength tensor
$A^\mu = (\Phi, \mathbf A)$, $F^{\mu\nu} = \partial^\mu A^\nu - \partial^\nu A^\mu$, $F^{0i} = -E^i$, $F^{ij} = -\varepsilon_{ijk}B^k$, gauge invariant under $A^\mu \to A^\mu + \partial^\mu\lambda$, see Definition [[§C1a.7 Relativistic Electrodynamics in Index Form#^def-c1a-7-2|§C1a.7.2]] Four-Potential and Field Tensor in Natural Units. *Source: Lecture 1 (Aug 31), slide "Example: Relativistic Electrodynamics" (Jackson 11.10) · PS2 Problem 4(b) (the identification) · the user's notes Ch. 1 §1.7*

^nd-def-c1a-7-2

- [ ] Q1 **[def]** Define $F^{\mu\nu}$ from $A^\mu$ and give $F^{0i}$, $F^{ij}$, $F_{0i}$, $F_{ij}$ in terms of $\mathbf E$, $\mathbf B$.
- [ ] Q2 Write the matrix $F_{\mu\nu}$ of the Lecture 1 slide. How do you recover $E^i$ and $B^i$ from $F$?
- [ ] Q3 **[why]** Why is $F$ unchanged by $A^\mu \to A^\mu + \partial^\mu\lambda$?
- [ ] Q4 **[conv]** Which overall sign does Griffiths' $F^{\mu\nu}$ have relative to the course's, and why? Which quantities built from $F$ differ in sign with PS?

> [!tip]- Hints: route in the notes
> - Technique: K2
> - [[§C1a.7 Relativistic Electrodynamics in Index Form#^cau-c1a-7-1|§C1a.7, Caution: Conventions for F across the sources]]; for Q3, symmetric second derivatives against antisymmetry ([[§C1a.5 Vectors, Tensors and Index Notation#^cau-c1a-5-7|§C1a.5, Caution: The Hessian is not the wave operator]]).

## Derivations T1

### The exponent rule for restoring ħ and c ★
A quantity of ordinary dimension $M^\alpha L^\beta T^\gamma$ has mass dimension $d = \alpha - \beta - \gamma$ and restores as $Q = Q_{\text{nat}}\,\hbar^{\beta + \gamma}c^{-\beta - 2\gamma}$, uniquely, see Theorem [[§C1a.2 Natural Units and Dimensional Analysis#^thm-c1a-2-1|§C1a.2.1]] The Exponent Rule. *Source: the user's notes Ch. 2 §2.4 · Lecture 2 (Sep 2), slide "Dimensional Analysis"*

^nd-thm-c1a-2-1

- [ ] Q1 **[state]** State the exponent rule: the mass dimension and the powers of $\hbar$ and $c$ in terms of $(\alpha, \beta, \gamma)$.
- [ ] Q2 What is the ordinary dimension of $\hbar^ac^b$?
- [ ] Q3 Write the three counter equations ($M$, $L$, $T$) that $Q = Q_{\text{nat}}\hbar^ac^b$ must satisfy, and solve them.
- [ ] Q4 Why is the solution unique?
- [ ] Q5 Check the rule on an energy and on a length: what do $m$ and $1/m$ restore to?
- [ ] Q6 **[why]** Why is the physical type of the quantity the one piece of information needed, and what goes wrong without it?

> [!tip]- Hints: route in the notes
> - Technique: K8
> - Steps 1–5 of the derivation of Theorem [[§C1a.2 Natural Units and Dimensional Analysis#^thm-c1a-2-1|§C1a.2.1]] The Exponent Rule: dimension of $\hbar^ac^b$; match counters; solve; determinant $\ne 0$; checks.
> - Procedure P4, steps 1 and 4; the structural reason: Theorem [[§C1a.2 Natural Units and Dimensional Analysis#^thm-c1a-2-2|§C1a.2.2]] Natural Units Are a Change of Basis Followed by a Quotient.

### Natural units as a change of basis and a quotient ★
$M$, $[\hbar]$, $[c]$ form a basis of the dimension lattice; setting $\hbar = c = 1$ is the projection $(d, a, b) \mapsto d$, which has no canonical inverse, see Theorem [[§C1a.2 Natural Units and Dimensional Analysis#^thm-c1a-2-2|§C1a.2.2]] Natural Units Are a Change of Basis Followed by a Quotient with Definition [[§C1a.2 Natural Units and Dimensional Analysis#^def-c1a-2-3|§C1a.2.3]] Dimensions as One-Dimensional Vector Spaces. *Source: the user's notes App. A (after Tao)*

^nd-thm-c1a-2-2

- [ ] Q1 **[def]** In the vector-space formulation, what is a dimension, what is a unit, and when is a formula admissible?
- [ ] Q2 **[state]** State the three parts of the theorem.
- [ ] Q3 Show that $(1,0,0)$, $(1,2,-1)$, $(0,1,-1)$ form a basis of $\mathbb Z^3$.
- [ ] Q4 Identify the kernel of the projection and its fibre over a given $d$.
- [ ] Q5 **[why]** Why does counting in powers of length instead of mass reverse the sign of every $d$, and why does that not change any physics?

> [!tip]- Hints: route in the notes
> - Technique: K8
> - Derivation of Theorem [[§C1a.2 Natural Units and Dimensional Analysis#^thm-c1a-2-2|§C1a.2.2]] Natural Units Are a Change of Basis Followed by a Quotient, steps 1–3 (basis matrix with determinant $\pm1$; units of $V_{[\hbar]}$, $V_{[c]}$ identified with $\mathbb R$; fibre a coset).

### Rules of dimensional counting ★
Only equal dimensions add; arguments of transcendental functions are dimensionless; powers multiply dimensions; derivatives divide and integrals multiply by the dimension of their variable ($[\delta^4(x)] = 4$); $[\delta/\delta\phi(x)] = 4 - [\phi]$, see Theorem [[§C1a.2 Natural Units and Dimensional Analysis#^thm-c1a-2-3|§C1a.2.3]] Rules of Dimensional Counting. *Source: the user's notes Ch. 2 §2.4, App. A*

^nd-thm-c1a-2-3

- [ ] Q1 **[state]** State the six rules.
- [ ] Q2 Why must the argument of $\exp$ be dimensionless? Use the power series.
- [ ] Q3 Derive $[\partial_\mu] = 1$, $[d^4x] = -4$, $[\delta^4(x)] = 4$, $[\delta^4(p)] = -4$.
- [ ] Q4 Derive $[\delta/\delta\phi(x)] = 4 - [\phi]$ from $\delta\phi(x)/\delta\phi(y) = \delta^4(x - y)$.
- [ ] Q5 **[why]** What hidden scale do $e^{-mt}$, $\log r$ and $r^\eta$ (non-integer $\eta$) carry?

> [!tip]- Hints: route in the notes
> - Technique: K8
> - Derivation of Theorem [[§C1a.2 Natural Units and Dimensional Analysis#^thm-c1a-2-3|§C1a.2.3]] Rules of Dimensional Counting, steps 1–6 (one step per rule, in the vector-space language of Definition [[§C1a.2 Natural Units and Dimensional Analysis#^def-c1a-2-3|§C1a.2.3]] Dimensions as One-Dimensional Vector Spaces).

### Annihilation photons: restoring c and a length
$E_{\text{CM}} = \sqrt{2m_e(E + m_e)}$, each photon carries $\frac12E_{\text{CM}}$, and for $E = 50$ MeV the photons probe tens to hundreds of fermi, see Example [[§C1a.2 Natural Units and Dimensional Analysis#^ex-c1a-2-1|§C1a.2.1]] The Annihilation Photons. *Source: PS1 Problem 4*

^nd-ex-c1a-2-1

→ drilled as [[PHY 513 PS Drill#^ps1-4|PS1.4]] (parts (a)–(d))

### Invariant volume elements ★
For every $\Lambda \in O(1,3)$, $d^4x' = d^4x$ and $d^4p' = d^4p$; integrals of scalar fields and of scalar distributions such as $\theta(p^0)\delta(p^2 - m^2)$ (orthochronous $\Lambda$) are invariant, see Theorem [[§C1a.4 The Lorentz Group#^thm-c1a-4-1|§C1a.4.1]] Invariant Volume Elements. *Source: the user's notes Ch. 1 §1.3 · PS3 Problem 1(a)–(b)*

^nd-thm-c1a-4-1

- [ ] Q1 **[state]** State the theorem, including which integrals become invariant and under which transformations.
- [ ] Q2 What is the Jacobian matrix of $x \mapsto \Lambda x$, and why is $|\det\Lambda| = 1$?
- [ ] Q3 For a scalar field ($f'(\Lambda x) = f(x)$), show $\int d^4x\,f' = \int d^4x\,f$.
- [ ] Q4 **[why]** Why does $\theta(p^0)$ need $\Lambda$ orthochronous, while $\delta(p^2 - m^2)$ does not?
- (The measure $d^4k$ and $d^4k\,\delta(k^2 - m^2)\theta(k^0)$ themselves → drilled as [[PHY 513 PS Drill#^ps3-1-a|PS3.1(a)]]–(b).)

> [!tip]- Hints: route in the notes
> - Technique: K14
> - Derivation of Theorem [[§C1a.4 The Lorentz Group#^thm-c1a-4-1|§C1a.4.1]] Invariant Volume Elements, steps 1–4; invariance of $\theta(p^0)$ on the mass shell: Theorem [[§C1a.4 The Lorentz Group#^thm-c1a-4-3|§C1a.4.3]] Parity and Time Reversal Permute the Orbits, part 3.

### The orbits of SO⁺(1,3): timelike, spacelike, null ★★
The orbits are the future and past sheets $x^2 = m^2$, $\pm x^0 > 0$, the one-sheeted hyperboloids $x^2 = -a^2$, the future and past null cones, and the origin; $x$, $y$ share an orbit iff $x^2 = y^2$ and, for nonzero $x^2 \ge 0$, $\operatorname{sgn}x^0 = \operatorname{sgn}y^0$, see Theorem [[§C1a.4 The Lorentz Group#^thm-c1a-4-2|§C1a.4.2]] The Orbits of SO⁺(1,3) on Spacetime. *Source: Lecture 2 (Sep 2), slides "Causal Classification", "Future vs. Past" · the user's notes Ch. 1 §1.3*

^nd-thm-c1a-4-2

- [ ] Q1 **[def]** Classify a point $x$ relative to the origin as timelike, spacelike or null (Lecture 2), and say what an observer at $x$ can do in each case.
- [ ] Q2 **[state]** List the orbits of $SO^+(1,3)$ on spacetime with a normal form for each.
- [ ] Q3 Why do orbits lie in level sets of $x^2$, and why is $\operatorname{sgn}x^0$ kept on timelike and null vectors by orthochronous $\Lambda$?
- [ ] Q4 Show that every point of the future sheet $x^2 = m^2$, $x^0 > 0$ is reached from $m e_0$. Which boost does it?
- [ ] Q5 Bring a spacelike $x$ to $a e_3$: which rotation, then which rapidity?
- [ ] Q6 Bring a future null vector to $e_0 + e_3$: why does a boost rescale it?
- [ ] Q7 **[why]** Why is "future" an invariant notion for timelike displacements but not for spacelike ones (Lecture 2: "$\epsilon(x^0)$ is not defined")?

> [!tip]- Hints: route in the notes
> - Technique: K14, K1
> - Derivation of Theorem [[§C1a.4 The Lorentz Group#^thm-c1a-4-2|§C1a.4.2]] The Orbits of SO⁺(1,3) on Spacetime, steps 1–7; the boost $B(u)$: Theorem [[§CB.3 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-3-13|§CB.3.13]] SO⁺(1,3) Is the Component of the Identity, part 1.
> - The lecture's $\epsilon(x^0)$ is the notes' $\operatorname{sgn}x^0$: [[§C1a.3 Causal Structure and the Causality of a Single Particle#^cau-c1a-3-1|§C1a.3, Caution: sgn x⁰, not ε(x⁰)]].

### Parity and time reversal permute the orbits ★★
$\mathcal P$ maps each orbit to itself; $\mathcal T$ and $\mathcal P\mathcal T$ exchange the future and past sheets and cones; so $\operatorname{sgn}x^0$ on timelike and null vectors and $\theta(p^0)$ on the mass shell are invariant under orthochronous transformations, while every spacelike $x$ is carried to $-x$ by some $\Lambda \in SO^+(1,3)$, see Theorem [[§C1a.4 The Lorentz Group#^thm-c1a-4-3|§C1a.4.3]] Parity and Time Reversal Permute the Orbits. *Source: Lecture 2 (Sep 2), slide "Future vs. Past" · the user's notes Ch. 1 §1.3*

^nd-thm-c1a-4-3

- [ ] Q1 **[state]** State the three parts.
- [ ] Q2 Why does $\mathcal P$ keep every orbit, using the complete invariants of the orbit theorem?
- [ ] Q3 Why do $\mathcal T$ and $-\mathbb 1$ exchange the two sheets but keep each spacelike hyperboloid?
- [ ] Q4 Construct $\Lambda \in SO^+(1,3)$ with $\Lambda x = -x$ for spacelike $x$. Which rotation by $\pi$ is used?
- [ ] Q5 **[why]** Why is "positive energy" a Lorentz-invariant statement for a massive particle, and what fails for a spacelike momentum?
- [ ] Q6 **[why]** Why does the orbit picture change in $1+1$ dimensions?

> [!tip]- Hints: route in the notes
> - Technique: K14
> - Derivation of Theorem [[§C1a.4 The Lorentz Group#^thm-c1a-4-3|§C1a.4.3]] Parity and Time Reversal Permute the Orbits, steps 1–5; the four components as cosets: Theorem [[§CB.3 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-3-12|§CB.3.12]] The Four Components Are the Cosets of SO⁺(1,3); dimension: [[§C1a.4 The Lorentz Group#^cau-c1a-4-4|§C1a.4, Caution: The orbit picture depends on the dimension]].
> - Where this returns: microcausality, [[§C1a.4 The Lorentz Group#^rem-c1a-4-2|§C1a.4, Remark: Why the orbits matter in field theory]].

### The Mandelstam sum rule and the momentum transfer ★
$s + t + u = \sum_i m_i^2$; with particle 2 at rest, $t = m_2^2 + m_4^2 - 2m_2E_4$; for elastic scattering in the centre-of-mass frame $t = -4p'^2\sin^2(\theta'/2) \le 0$, see Theorem [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-1|§C1a.5.1]] The Mandelstam Sum Rule and the Momentum Transfer. *Source: PS1 Problem 5(e)–(f) · the user's notes Ch. 1 §1.4*

^nd-thm-c1a-5-1

- [ ] Q1 **[state]** State the sum rule $s + t + u = \,?$ with its hypotheses.
- [ ] Q2 Expand $s$, $t$, $u$ using $p_i^2 = m_i^2$.
- [ ] Q3 Add, and use momentum conservation to remove the cross terms. Which combination of momenta appears, and what does it equal?
- [ ] Q4 **[why]** Why is $t \le 0$ in elastic scattering, and when is it zero?
- (Parts 2 and 3 → drilled as [[PHY 513 PS Drill#^ps1-5-e|PS1.5(e)]]–(f).)

> [!tip]- Hints: route in the notes
> - Technique: K1
> - Derivation of Theorem [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-1|§C1a.5.1]] The Mandelstam Sum Rule and the Momentum Transfer, steps 1–2 (part 1); steps 3–5 are the PS parts.

### The metric identifies vectors with covectors ★
$g$ is symmetric, nondegenerate and indefinite; $x \mapsto x^\flat = g(x, \cdot)$ is an isomorphism $V \to V^\ast$ with components $x_\mu = g_{\mu\nu}x^\nu$ and inverse $g^{\mu\nu}$, see Theorem [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-2|§C1a.5.2]] The Metric Identifies Vectors with Covectors. *Source: the user's notes Ch. 1 §1.5 · Lecture 1 (Aug 31), slide "Index Gymnastics"*

^nd-thm-c1a-5-2

- [ ] Q1 **[state]** State what lowering an index is, as a map between which spaces.
- [ ] Q2 Show $x^\flat$ is a linear functional and compute its components.
- [ ] Q3 Why is $x \mapsto x^\flat$ injective, and why does injectivity give bijectivity here?
- [ ] Q4 Identify the matrix of the inverse map. Why is $g^{\mu\nu}$ numerically equal to $g_{\mu\nu}$?
- [ ] Q5 **[why]** In what sense is $x_\mu x^\mu$ "a functional evaluated on a vector"? Why does Lecture 1 call the row vector $x^{\mathsf T}g$ covariant?

> [!tip]- Hints: route in the notes
> - Technique: K2
> - Derivation of Theorem [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-2|§C1a.5.2]] The Metric Identifies Vectors with Covectors, steps 1–4.

### Contraction identities of the Levi-Civita symbol ★
With $\varepsilon^{0123} = +1$: $\varepsilon_{\mu\nu\rho\sigma}\varepsilon^{\alpha\beta\gamma\delta} = -\delta^{\alpha\beta\gamma\delta}_{\mu\nu\rho\sigma}$, and successive contractions give $-\delta^{\beta\gamma\delta}_{\nu\rho\sigma}$, $-2(\delta^\gamma_\rho\delta^\delta_\sigma - \delta^\gamma_\sigma\delta^\delta_\rho)$, $-6\delta^\delta_\sigma$, $-24$; in three Euclidean dimensions the same without the minus sign, see Theorem [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-3|§C1a.5.3]] Contraction Identities of the Levi-Civita Symbol. *Source: the user's notes Ch. 1 §1.5*

^nd-thm-c1a-5-3

- [ ] Q1 **[state]** State the four-dimensional identity and its contractions down to $\varepsilon\varepsilon$ fully contracted.
- [ ] Q2 Why do both sides vanish together when two indices coincide?
- [ ] Q3 For distinct indices, why is the left side $-\operatorname{sgn}\tau\operatorname{sgn}\pi$? Where does the overall minus come from?
- [ ] Q4 Contract one index pair in a $k\times k$ generalized delta in $n$ dimensions: what factor appears?
- [ ] Q5 **[why]** Why is there no minus sign in the three-dimensional Euclidean identity $\varepsilon_{ijk}\varepsilon_{ilm} = \delta_{jl}\delta_{km} - \delta_{jm}\delta_{kl}$?

> [!tip]- Hints: route in the notes
> - Technique: K2
> - Derivation of Theorem [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-3|§C1a.5.3]] Contraction Identities of the Levi-Civita Symbol, steps 1–5 (vanishing; permutation signs with $\varepsilon_{0123} = -1$; one contraction gives the factor $n - k + 1$).

### The Levi-Civita symbol and the determinant ★
$\varepsilon_{\mu\nu\rho\sigma}A^\mu{}_\alpha A^\nu{}_\beta A^\rho{}_\gamma A^\sigma{}_\delta = (\det A)\varepsilon_{\alpha\beta\gamma\delta}$, the determinant and inverse as $\varepsilon\varepsilon$ contractions, and $\varepsilon_{\mu\nu\rho\sigma}a^\mu b^\nu c^\rho d^\sigma = -\det[a|b|c|d]$, see Theorem [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-4|§C1a.5.4]] The Levi-Civita Symbol and the Determinant. *Source: the user's notes Ch. 1 §1.5*

^nd-thm-c1a-5-4

- [ ] Q1 **[state]** State parts 1 and 4.
- [ ] Q2 Prove part 1: why is the left side totally antisymmetric in $\alpha\beta\gamma\delta$, and what is it at $(0123)$?
- [ ] Q3 Contract part 1 with $\varepsilon^{\alpha\beta\gamma\delta}$ to get part 2. Which identity supplies the $-24$?
- [ ] Q4 **[why]** Why is $\varepsilon^{\mu\nu\rho\sigma}p_{1\mu}p_{2\nu}p_{3\rho}p_{4\sigma}$ invariant only under $\det\Lambda = +1$?
- (The momentum-conservation application → drilled as [[PHY 513 PS Drill#^ps1-3-b|PS1.3(b)]].)

> [!tip]- Hints: route in the notes
> - Technique: K2
> - Derivation of Theorem [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-4|§C1a.5.4]] The Levi-Civita Symbol and the Determinant, steps 1, 2, 4; the identity of Theorem [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-3|§C1a.5.3]] Contraction Identities of the Levi-Civita Symbol.

### Momentum conservation kills ε p₁p₂p₃p₄
For $\sum_i p_i = 0$, $\varepsilon^{\mu\nu\rho\sigma}p_{1\mu}p_{2\nu}p_{3\rho}p_{4\sigma} = 0$, see Example [[§C1a.5 Vectors, Tensors and Index Notation#^ex-c1a-5-1|§C1a.5.1]] Momentum Conservation Kills ε p₁p₂p₃p₄. *Source: PS1 Problem 3*

^nd-ex-c1a-5-1

→ drilled as [[PHY 513 PS Drill#^ps1-3|PS1.3]]

### The centre-of-mass momentum from a transverse tensor component
$p' = m_2p_{\rm lab}/E_{\rm cm}$ from $T_{23}$ of $T_{\mu\nu} = \varepsilon_{\mu\nu\rho\sigma}P^\sigma Q^\rho$ evaluated in two frames, see Example [[§C1a.5 Vectors, Tensors and Index Notation#^ex-c1a-5-2|§C1a.5.2]] The Centre-of-Mass Momentum from a Transverse Component. *Source: PS1 Problem 5(d)*

^nd-ex-c1a-5-2

→ drilled as [[PHY 513 PS Drill#^ps1-5-d|PS1.5(d)]]

### Trace, symmetric and antisymmetric parts do not mix ★★
$T^{\mu\nu}$ splits uniquely into a symmetric traceless part (9), an antisymmetric part (6) and a trace part (1), each mapped into itself by every Lorentz transformation, see Theorem [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-5|§C1a.5.5]] The Trace, Symmetric and Antisymmetric Parts Do Not Mix. *Source: Lecture 1 (Aug 31), slide "Tensors" ("Irreducible parts of two-tensor representation") · the user's notes Ch. 1 §1.5*

^nd-thm-c1a-5-5

- [ ] Q1 **[def]** How does a two-tensor $T^{\mu\nu}$ transform (Lecture 1)? Why is a general two-tensor not a product $p^\mu q^\nu$?
- [ ] Q2 **[state]** State the decomposition with the dimension of each piece.
- [ ] Q3 Show that a symmetric (antisymmetric) tensor stays symmetric (antisymmetric) under $\Lambda$.
- [ ] Q4 Show that $g_{\mu\nu}T^{\mu\nu}$ is invariant. Which property of $\Lambda$ is used?
- [ ] Q5 Show that $T^{(\mu\nu)} - \frac14g^{\mu\nu}T^\rho{}_\rho$ is traceless and that the trace part transforms into itself.
- [ ] Q6 **[why]** The theorem says "mapped into itself". Where is irreducibility proved, and what extra happens to the antisymmetric part over $\mathbb C$?

> [!tip]- Hints: route in the notes
> - Technique: K2, K14
> - Derivation of Theorem [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-5|§C1a.5.5]] The Trace, Symmetric and Antisymmetric Parts Do Not Mix, steps 1–4; [[§C1a.5 Vectors, Tensors and Index Notation#^cau-c1a-5-4|§C1a.5, Caution: A tensor is not a product of vectors]]; the complex split: Theorem [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-6|§C1a.5.6]] Duality Squares to −1 on Antisymmetric Tensors, part 3.

### Duality squares to −1 on antisymmetric tensors ★
$(\star A)^{\mu\nu} = \frac12\varepsilon^{\mu\nu\rho\sigma}A_{\rho\sigma}$ satisfies $\star\star = -1$, commutes with proper and anticommutes with improper Lorentz transformations, and over $\mathbb C$ splits the six-dimensional space into the $\pm i$ eigenspaces, see Theorem [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-6|§C1a.5.6]] Duality Squares to −1 on Antisymmetric Tensors. *Source: the user's notes Ch. 1 §1.5*

^nd-thm-c1a-5-6

- [ ] Q1 **[state]** State the three parts.
- [ ] Q2 Lower the indices of $\star A$ and write $\star\star A$ as an $\varepsilon\varepsilon$ contraction.
- [ ] Q3 Bring the contracted pair to the front of $\varepsilon^{\mu\nu\rho\sigma}$: what sign does that permutation have?
- [ ] Q4 Apply the double-contraction identity and finish part 1.
- [ ] Q5 **[why]** Why do the $\pm i$ eigenspaces need complex numbers, and why does $\mathcal P$ exchange them?

> [!tip]- Hints: route in the notes
> - Technique: K2
> - Derivation of Theorem [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-6|§C1a.5.6]] Duality Squares to −1 on Antisymmetric Tensors, steps 1–6; the identity of Theorem [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-3|§C1a.5.3]] Contraction Identities of the Levi-Civita Symbol.

### Basic derivative identities and plane waves ★★
$\partial_\mu x^\nu = \delta^\nu{}_\mu$, $\partial_\mu x^\mu = 4$, $\partial_\mu(x^2) = 2x_\mu$, and $\partial_\mu e^{-ik\cdot x} = -ik_\mu e^{-ik\cdot x}$, $\partial^2e^{-ik\cdot x} = -k^2e^{-ik\cdot x}$, see Theorem [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-7|§C1a.5.7]] Basic Derivative Identities. *Source: Lecture 2 (Sep 2), slides "Derivatives" ("Proof that $\partial_\mu$ transforms like $x_\mu$"), "Plane-Wave Solutions to the Klein Gordon Equation"; Lecture 3 (Sep 9), slide "Solutions to the Klein-Gordon Equation" · the user's notes Ch. 2 §2.3*

^nd-thm-c1a-5-7

- [ ] Q1 **[state]** State $\partial_\mu x^\nu$, $\partial^\mu x^\nu$, $\partial_\mu x^\mu$, $\partial_\mu(x^2)$, $\partial_\mu\partial_\nu(x^2)$.
- [ ] Q2 Derive $\partial_\mu(x^2) = 2x_\mu$ by the product rule. Why does Lecture 2 call this the proof that $\partial_\mu$ has a lower index?
- [ ] Q3 Which momentum, upper or lower index, does $\partial_\mu$ pull down from $e^{-ik\cdot x}$, with $k\cdot x = \omega t - \mathbf k\cdot\mathbf x$?
- [ ] Q4 Insert $\phi_0e^{-ik\cdot x}$ into the Klein–Gordon equation (Lecture 3, "insert ansatz"): what condition on $\omega$, $\mathbf k$ results, and which particle relation is it?
- [ ] Q5 **[why]** What sign error in the equation would show up in the dispersion relation, and why does Lecture 3 call the mass helpful for "getting our signs right"?

> [!tip]- Hints: route in the notes
> - Technique: K2
> - Derivation of Theorem [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-7|§C1a.5.7]] Basic Derivative Identities, steps 1–3; the Hessian is not the wave operator: [[§C1a.5 Vectors, Tensors and Index Notation#^cau-c1a-5-7|§C1a.5, Caution: The Hessian is not the wave operator]]; [[§C1b.1 Fields and Their Transformation Laws#^rem-c1b-1-3|§C1b.1, Remark: What the Klein–Gordon equation is, and what it is not]].

### The d'Alembertian of a function of x²
$\partial^2f(\rho) = 8f' + 4\rho f''$ for $\rho = x^2$; $f = c_1/\rho + c_2$ are the harmonic functions of $\rho$ off the cone, see Theorem [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-8|§C1a.5.8]] The d'Alembertian of a Function of x². *Source: PS1 Problem 6*

^nd-thm-c1a-5-8

→ drilled as [[PHY 513 PS Drill#^ps1-6|PS1.6]] (parts (a)–(f))

### Taylor expansion in index notation ★
$f(x + a) = \sum_n\frac1{n!}a^{\nu_1}\cdots a^{\nu_n}\partial_{\nu_1}\cdots\partial_{\nu_n}f(x) = e^{a\cdot\partial}f(x)$; on a plane wave the series is exact, and $a\cdot\partial = -ia\cdot\hat p$ generates translations, see Theorem [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-9|§C1a.5.9]] Taylor Expansion in Index Notation. *Source: the user's notes Ch. 2 §2.3*

^nd-thm-c1a-5-9

- [ ] Q1 **[state]** State the expansion and the plane-wave statement.
- [ ] Q2 Reduce to one variable with $g(s) = f(x + sa)$: what is $g^{(n)}(s)$?
- [ ] Q3 Group the ordered index strings into the multi-index form: where does $n!/(k_0!\cdots k_3!)$ come from?
- [ ] Q4 Show the series is exact on $e^{-ik\cdot x}$ and identify $\hat p^0$, $\hat p^j$.
- [ ] Q5 **[why]** Name the three different Taylor expansions classical field theory uses (in coordinates, in a parameter, in the fields) and where each enters.

> [!tip]- Hints: route in the notes
> - Technique: K2
> - Derivation of Theorem [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-9|§C1a.5.9]] Taylor Expansion in Index Notation, steps 1–5; [[§C1a.5 Vectors, Tensors and Index Notation#^rem-c1a-5-4|§C1a.5, Remark: Three expansions, not one]].

### Derivatives with respect to a four-vector ★★
$\partial/\partial a^\mu$ is a covector; $\partial a^\nu/\partial a^\mu = \delta^\nu{}_\mu$, $\partial a_\nu/\partial a^\mu = g_{\mu\nu}$; $\partial(a_\nu a^\nu)/\partial a^\mu = 2a_\mu$, and for $\mathcal L = \frac12\partial_\nu\phi\,\partial^\nu\phi$, $\partial\mathcal L/\partial(\partial_\mu\phi) = \partial^\mu\phi$, see Theorem [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-10|§C1a.5.10]] Derivatives with Respect to a Four-Vector. *Source: Lecture 3 (Sep 9), slide "Example: the Scalar Field" · the user's notes Ch. 2 §2.3 · **[class exercise, Lecture 3]**: "you double check" the derivative of the kinetic term component by component*

^nd-thm-c1a-5-10

- [ ] Q1 **[state]** State the four index forms of $\partial a/\partial a$ and the factor-of-two rule.
- [ ] Q2 Why does an index in the denominator flip height? Use the chain rule with $a = \Lambda^{-1}a'$.
- [ ] Q3 Derive $\partial(a_\nu a^\nu)/\partial a^\mu$ by differentiating both factors of $g_{\nu\rho}a^\nu a^\rho$.
- [ ] Q4 **[class exercise, Lecture 3]** Compute $\partial\mathcal L/\partial(\partial_\mu\phi)$ for $\mathcal L = \frac12\partial_\nu\phi\,\partial^\nu\phi$ with the dummy renamed, then check it component by component ($\mu = 0$ and $\mu = i$).
- [ ] Q5 **[why]** Why do the components have to be independent? What goes wrong if one differentiates by $p^\mu$ after imposing the mass shell, or treats $\partial_\mu\phi$ and $\partial^\mu\phi$ as independent?

> [!tip]- Hints: route in the notes
> - Technique: K2
> - Derivation of Theorem [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-10|§C1a.5.10]] Derivatives with Respect to a Four-Vector, steps 1–4; the hygiene rule [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^cau-c1b-2-3|§C1b.2, Caution: Rename the dummy index before differentiating]] (it contains the component check).

### Derivatives with respect to tensor components ★
For independent components, $\partial T^\alpha{}_\beta/\partial T^\mu{}_\nu = \delta^\alpha{}_\mu\delta_\beta{}^\nu$; $\partial(T_{\alpha\beta}T^{\alpha\beta})/\partial T_{\mu\nu} = 2T^{\mu\nu}$; for antisymmetric $F$ either convention gives $\delta(FF) = 2F\,\delta F$; and $\partial(F_{\alpha\beta}F^{\alpha\beta})/\partial(\partial_\mu A_\nu) = 4F^{\mu\nu}$, see Theorem [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-11|§C1a.5.11]] Derivatives with Respect to Tensor Components. *Source: the user's notes Ch. 2 §2.3 · PS2 Problem 4(a)*

^nd-thm-c1a-5-11

- [ ] Q1 **[state]** State parts 1–3.
- [ ] Q2 Why is the derivative of a component with respect to a component a product of deltas, slot by slot?
- [ ] Q3 Derive $\partial(T_{\alpha\beta}T^{\alpha\beta})/\partial T_{\mu\nu}$: which two terms appear, and why are they equal?
- [ ] Q4 **[why]** For antisymmetric $F$, why does it not matter whether one treats six or sixteen components as independent, as long as one is consistent?
- (Part 4 and Maxwell's equations from $-\frac14F^2$ → drilled as [[PHY 513 PS Drill#^ps2-4-a|PS2.4(a)]].)

> [!tip]- Hints: route in the notes
> - Technique: K2
> - Derivation of Theorem [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-11|§C1a.5.11]] Derivatives with Respect to Tensor Components, steps 1–3.

### Maxwell's equations in Heaviside–Lorentz form ★
$\partial_\mu F^{\mu\nu} = J^\nu$ and $\partial_\mu\tilde F^{\mu\nu} = 0$, the latter equivalent to the cyclic Bianchi identity and automatic for $F = dA$; consistency requires $\partial_\nu J^\nu = 0$, see Theorem [[§C1a.7 Relativistic Electrodynamics in Index Form#^thm-c1a-7-1|§C1a.7.1]] Maxwell's Equations in Heaviside–Lorentz Form. *Source: the user's notes Ch. 1 §1.7*

^nd-thm-c1a-7-1

- [ ] Q1 **[state]** State both covariant equations, which of Maxwell's four each contains, and the consistency condition.
- [ ] Q2 Show that $\partial_\mu\tilde F^{\mu\nu} = 0$ holds identically when $F_{\rho\sigma} = \partial_\rho A_\sigma - \partial_\sigma A_\rho$.
- [ ] Q3 Show that $\partial_\nu J^\nu = 0$ follows from the first equation. Which symmetry argument is used?
- [ ] Q4 **[why]** Why does the cyclic sum $\partial^\rho F^{\mu\nu} + \partial^\mu F^{\nu\rho} + \partial^\nu F^{\rho\mu}$ have only four independent components?
- (Splitting $\partial_\mu F^{\mu\nu} = J^\nu$ into Gauss and Ampère–Maxwell → drilled as [[PHY 513 PS Drill#^ps2-4-b|PS2.4(b)]].)

> [!tip]- Hints: route in the notes
> - Technique: K2
> - Derivation of Theorem [[§C1a.7 Relativistic Electrodynamics in Index Form#^thm-c1a-7-1|§C1a.7.1]] Maxwell's Equations in Heaviside–Lorentz Form, steps 4–6 (steps 1–3 are the PS part); index moves [[§C1a.7 Relativistic Electrodynamics in Index Form#^rem-c1a-7-1|§C1a.7, Remark: Index techniques in Maxwell's equations]].

### Duality exchanges E and B; the two invariants ★
$\tilde F^{0i} = -B^i$, $\tilde F^{ij} = \varepsilon_{ijk}E^k$; $F_{\mu\nu}F^{\mu\nu} = 2(\mathbf B^2 - \mathbf E^2)$, $F_{\mu\nu}\tilde F^{\mu\nu} = -4\,\mathbf E\cdot\mathbf B$ (course; $+$ in PS for the $\varepsilon FF$ form), see Theorem [[§C1a.7 Relativistic Electrodynamics in Index Form#^thm-c1a-7-2|§C1a.7.2]] Duality Exchanges E and B; the Two Invariants. *Source: the user's notes Ch. 1 §1.7*

^nd-thm-c1a-7-2

- [ ] Q1 **[state]** State the components of $\tilde F$ and the four invariants.
- [ ] Q2 Compute $\tilde F^{0i}$: which $\rho\sigma$ contribute, and how is $\varepsilon^{0ijk}$ related to $\varepsilon_{ijk}$?
- [ ] Q3 Compute $F_{\mu\nu}F^{\mu\nu}$ by splitting into time–space and space–space terms. Why does the time–space term appear twice?
- [ ] Q4 Compute $F_{\mu\nu}\tilde F^{\mu\nu}$ the same way.
- [ ] Q5 **[conv]** Which of the invariants change sign in PS's convention, and why does the scalar not?

> [!tip]- Hints: route in the notes
> - Technique: K2
> - Derivation of Theorem [[§C1a.7 Relativistic Electrodynamics in Index Form#^thm-c1a-7-2|§C1a.7.2]] Duality Exchanges E and B; the Two Invariants, steps 1–6; [[§C1a.5 Vectors, Tensors and Index Notation#^cau-c1a-5-5|§C1a.5, Caution: The sign of ε⁰¹²³: these notes versus Peskin–Schroeder]].

### E ± iB: the self-dual halves of F ★
$F \pm i\tilde F$ are the $\mp i$ eigenvectors of duality, carried by $\mathbf E \pm i\mathbf B$; proper Lorentz transformations act on $\mathbf E + i\mathbf B$ by complex orthogonal matrices, parity exchanges the halves, and the two invariants form one complex invariant, see Theorem [[§C1a.7 Relativistic Electrodynamics in Index Form#^thm-c1a-7-3|§C1a.7.3]] E ± iB: the Self-Dual Halves of F. *Source: the user's notes Ch. 1 §1.5 (the remark on $\mathbf E \pm i\mathbf B$); items 2–3 derived in the vault*

^nd-thm-c1a-7-3

- [ ] Q1 **[state]** State the three parts.
- [ ] Q2 Using $\star\star = -1$, show $F + i\tilde F$ is an eigenvector of $\star$ and find its eigenvalue.
- [ ] Q3 Why does a proper $\Lambda$ preserve each eigenspace, and why is the induced $3\times3$ matrix complex orthogonal?
- [ ] Q4 **[why]** Compute $(\mathbf E + i\mathbf B)^2$ and relate it to $FF$ and $F\tilde F$. Why is one complex invariant the same information as two real ones?

> [!tip]- Hints: route in the notes
> - Technique: K2
> - Derivation of Theorem [[§C1a.7 Relativistic Electrodynamics in Index Form#^thm-c1a-7-3|§C1a.7.3]] E ± iB: the Self-Dual Halves of F, steps 1–4; Theorem [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-6|§C1a.5.6]] Duality Squares to −1 on Antisymmetric Tensors.

### Lecture 1's boost of E_x ★★
Under the active boost along $z$, $E'_x = F'_{01} = \Lambda_0{}^0\Lambda_1{}^1F_{01} + \Lambda_0{}^3\Lambda_1{}^1F_{31} = \gamma(E_x + vB_y)$; the slide's $\gamma(E_x - vB_y)$ is the passive sign, see Example [[§C1a.7 Relativistic Electrodynamics in Index Form#^ex-c1a-7-1|§C1a.7.1]] The Lecture's Boost Example, Done with the Active Boost and [[§C1a.7 Relativistic Electrodynamics in Index Form#^cau-c1a-7-2|§C1a.7, Caution: The sign of the v × B term]]. *Source: Lecture 1 (Aug 31), slide "Example: Relativistic Electrodynamics" · the user's notes Ch. 1 §1.7*

^nd-ex-c1a-7-1

- [ ] Q1 **[def]** Write the transformation law of $F_{\mu\nu}$ (Lecture 1). Why does it use $\Lambda_\mu{}^\lambda$, and how are those entries related to $\Lambda^{-1}$?
- [ ] Q2 For the boost along $z$, which $\lambda$, $\sigma$ contribute to $F'_{01}$, and why does the second index force $\sigma = 1$?
- [ ] Q3 Compute $\Lambda_0{}^0$ and $\Lambda_0{}^3$ from the active boost matrix, and $F_{31}$ in terms of $\mathbf B$.
- [ ] Q4 **[conv]** The slide writes $E'_x = \gamma(E_x - vB_y)$. Which reading of the boost gives that sign, and why must the two readings not be mixed in one calculation?
- [ ] Q5 **[why]** Check the result against the passive formula $\mathbf E'_\perp = \gamma(\mathbf E + \mathbf u\times\mathbf B)_\perp$: what is $\mathbf u$ for the active boost by $+v\hat{\mathbf z}$?

> [!tip]- Hints: route in the notes
> - Technique: K2, K14
> - Example [[§C1a.7 Relativistic Electrodynamics in Index Form#^ex-c1a-7-1|§C1a.7.1]] The Lecture's Boost Example, Done with the Active Boost (one computation); [[§C1a.4 The Lorentz Group#^cau-c1a-4-1|§C1a.4, Caution: Active and passive readings]]; Definition [[§C1a.4 The Lorentz Group#^def-c1a-4-2|§C1a.4.2]] Active Rotation and Boost.

### The SI–Heaviside–Lorentz dictionary ★
$\mathbf E_{\rm HL} = \sqrt{\varepsilon_0}\mathbf E_{\rm SI}$, $\mathbf B_{\rm HL} = \mathbf B_{\rm SI}/\sqrt{\mu_0}$, $q_{\rm HL} = q_{\rm SI}/\sqrt{\varepsilon_0}$ turn SI electrodynamics into the rationalized form with $\alpha = e^2/4\pi\hbar c$, see Theorem [[§C1a.7 Relativistic Electrodynamics in Index Form#^thm-c1a-7-4|§C1a.7.4]] The SI–Heaviside–Lorentz Dictionary. *Source: the user's pre-course notes §1.2; dictionary derived in the vault*

^nd-thm-c1a-7-4

- [ ] Q1 **[state]** State the substitutions and the resulting four equations with $c$ kept.
- [ ] Q2 Substitute into Gauss's law and Ampère–Maxwell's law: where does $\mu_0\varepsilon_0 = 1/c^2$ enter?
- [ ] Q3 Show the Lorentz force becomes $q(\mathbf E + \frac{\mathbf v}{c}\times\mathbf B)$.
- [ ] Q4 **[why]** Why is $\alpha$ the same number in SI, Gaussian and Heaviside–Lorentz units, while $e$ is not?

> [!tip]- Hints: route in the notes
> - Technique: K8
> - Derivation of Theorem [[§C1a.7 Relativistic Electrodynamics in Index Form#^thm-c1a-7-4|§C1a.7.4]] The SI–Heaviside–Lorentz Dictionary, steps 1–5.

### Checking that boosts and rotations are Lorentz, and that products are ★★
**[class exercise, Lecture 1]** The boost $B_z(\eta)$ satisfies $\Lambda^{\mathsf T}g\Lambda = g$ by $\cosh^2 - \sinh^2 = 1$ (done on the slide); the rotation "you can check in much the same way" (transcript: "it's actually easier"); a product of two Lorentz matrices is Lorentz. Homes: Definition [[§C1a.4 The Lorentz Group#^def-c1a-4-1|§C1a.4.1]] Lorentz Transformation, Active Reading, Definition [[§C1a.4 The Lorentz Group#^def-c1a-4-3|§C1a.4.3]] Rapidity, Definition [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-1|§CB.1.1]] Matrix Groups (the group property itself is Relativity's, REL Theorem §B1.2.3, outside the QFT catalogue). *Source: Lecture 1 (Aug 31), slide "Consistency Checks" and transcript · the user's notes Ch. 1 §1.3 (Derivation "Consistency checks on the definition")*

^nd-cx-1-1

- [ ] Q1 **[def]** State the defining condition of a Lorentz matrix.
- [ ] Q2 Verify $B_z(\eta)^{\mathsf T}gB_z(\eta) = g$ on the $(t, z)$ block. Which identity closes it?
- [ ] Q3 **[class exercise, Lecture 1]** Verify the condition for the rotation about $z$. Why is it easier ("the $\pm1$ entries of $g$ are not mixed")? To which condition on the spatial block does it reduce?
- [ ] Q4 Show that $\Lambda_1\Lambda_2$ satisfies the condition when $\Lambda_1$, $\Lambda_2$ do; show $\Lambda^{-1}$ exists and satisfies it.
- [ ] Q5 **[why]** Why does Lecture 1 advise "don't write down your matrix; just know that it satisfies $\Lambda^{\mathsf T}g\Lambda = g$"? What does it buy in practice?

> [!tip]- Hints: route in the notes
> - Technique: K14
> - Take determinants of $\Lambda^{\mathsf T}g\Lambda = g$ for invertibility (step 2 of the derivation of Theorem [[§C1a.4 The Lorentz Group#^thm-c1a-4-1|§C1a.4.1]] Invariant Volume Elements); for products, insert $g = \Lambda_1^{\mathsf T}g\Lambda_1$ in the middle (Lecture 1 slide).

### All solutions of ΛᵀgΛ = g: six parameters, boosts times rotations ★
**[class exercise, Lecture 1]** "You can think a bit harder and see that you get a six-parameter family of solutions to this equation" and "you can get as a homework exercise to figure out what matrices do that" (transcript); the user's notes: "Finding the matrices that satisfy it, and recognizing them as boosts and rotations, is a homework exercise." Not set in PS1. Homes: every $\Lambda \in SO^+(1,3)$ is $B(u)R$, see Theorem [[§CB.3 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-3-13|§CB.3.13]] SO⁺(1,3) Is the Component of the Identity; the four components Theorem [[§CB.3 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-3-12|§CB.3.12]] The Four Components Are the Cosets of SO⁺(1,3); six parameters from the infinitesimal form Theorem [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-1|§C1a.6.1]] Infinitesimal Lorentz Transformations Are Antisymmetric (drilled with T7). *Source: Lecture 1 (Aug 31), transcript · the user's notes Ch. 1 §1.3*

^nd-cx-1-2

- [ ] Q1 **[state]** State the decomposition of a proper orthochronous $\Lambda$ into a boost and a rotation, and how the boost is read off from $\Lambda$.
- [ ] Q2 Count the parameters: how many independent conditions does $\Lambda^{\mathsf T}g\Lambda = g$ impose on sixteen entries?
- [ ] Q3 Given $\Lambda$, let $u = \Lambda e_0$. Why is $u^2 = 1$ and $u^0 \ge 1$? Show that $B(u)^{-1}\Lambda$ fixes $e_0$.
- [ ] Q4 Show that a Lorentz matrix fixing $e_0$ has the form $\operatorname{diag}(1, O)$ with $O \in SO(3)$ when $\det\Lambda = 1$.
- [ ] Q5 **[why]** Which elements of $O(1,3)$ are not of this form, and why can they not be reached continuously from $\mathbb 1$?

> [!tip]- Hints: route in the notes
> - Technique: K14
> - Theorem [[§CB.3 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-3-13|§CB.3.13]] SO⁺(1,3) Is the Component of the Identity, part 1 and its derivation (embedded in §C1a.4); components Theorem [[§CB.3 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-3-12|§CB.3.12]] The Four Components Are the Cosets of SO⁺(1,3); the count: $\Lambda^{\mathsf T}g\Lambda - g$ is symmetric.

### Index form of a matrix acting on a column ★
**[class exercise, Lecture 1]** "You can check that this is really the shorthand for how to multiply a four-dimensional column vector with a four-by-four matrix": $x'^\mu = \Lambda^\mu{}_\nu x^\nu$, one equation per $\mu$, summed over $\nu$; $x^{\mathsf T}gy = x_\mu y^\mu$. Homes: Definition [[§C1a.5 Vectors, Tensors and Index Notation#^def-c1a-5-1|§C1a.5.1]] Four-Vectors and Index Positions in Natural Units, [[§C1a.5 Vectors, Tensors and Index Notation#^cau-c1a-5-2|§C1a.5, Caution: Index bookkeeping: legal, illegal, and matrix products]]. *Source: Lecture 1 (Aug 31), slides "Four - Vectors", "Invariants" and transcript*

^nd-cx-1-3

- [ ] Q1 **[def]** Which index of $\Lambda^\mu{}_\nu$ labels the row and which the column? Write $x'^0$ as an explicit sum.
- [ ] Q2 **[class exercise, Lecture 1]** Check that $\Lambda^\mu{}_\nu x^\nu$ for $\mu = 0, \dots, 3$ reproduces the matrix product $\Lambda x$.
- [ ] Q3 Write $x^{\mathsf T}gy$ in index form and show its invariance under $x \to \Lambda x$, $y \to \Lambda y$ in both notations.
- [ ] Q4 **[why]** Index expressions commute but matrices do not. What replaces the order of factors in index notation?
- (Reordering a given index expression into a matrix product → drilled as [[PHY 513 PS Drill#^ps1-2-a|PS1.2(a)]].)

> [!tip]- Hints: route in the notes
> - Technique: K2
> - Lecture 1 slide "Invariants" ($x^{\mathsf T}\Lambda^{\mathsf T}g\Lambda x$); [[§C1a.5 Vectors, Tensors and Index Notation#^cau-c1a-5-2|§C1a.5, Caution: Index bookkeeping: legal, illegal, and matrix products]], bullet "Matrix products".

# T2. Causality and the single particle

## Definitions and conventions T2

### Particle number is not conserved
In relativistic processes particles are created and annihilated ($\gamma \to e^+e^-$ near a nucleus, $e^+e^- \to \gamma\gamma$); additive charges are conserved, particle number is not, see Law [[§C1a.1 Why Quantum Field Theory#^law-c1a-1-1|§C1a.1.1]] Particle Number Is Not Conserved. *Source: Lecture 1 (Aug 31), slide "Motivation 1: Technical" · the user's notes Ch. 1 §1.1*

^nd-law-c1a-1-1

- [ ] Q1 **[state]** State the law and its domain of validity.
- [ ] Q2 **[why]** Why does "quantum + relativity" without fields fail (Lecture 1: "an independent wave function for 1, 2, … particles")? What structure replaces it?
- [ ] Q3 **[why]** Give Lecture 1's other two motivations for fields (electromagnetism; long-distance description) in one sentence each.
- [ ] Q4 **[why]** In which process does $E = mc^2$ make the particle number change, and what sets the threshold?

> [!tip]- Hints: route in the notes
> - Law [[§C1a.1 Why Quantum Field Theory#^law-c1a-1-1|§C1a.1.1]] Particle Number Is Not Conserved, [[§C1a.1 Why Quantum Field Theory#^rem-c1a-1-1|§C1a.1, Remark: One quantum theory for any number of particles]], [[§C1a.1 Why Quantum Field Theory#^rem-c1a-1-2|§C1a.1, Remark: Electromagnetism forces relativity and photons]], [[§C1a.1 Why Quantum Field Theory#^rem-c1a-1-3|§C1a.1, Remark: Fields as the long-distance description]].

### Causality
The entire response to a disturbance at a point lies at future timelike or null separation from it; spacelike points neither affect it nor are affected, see Principle [[§C1a.3 Causal Structure and the Causality of a Single Particle#^pr-c1a-3-1|§C1a.3.1]] Causality. *Source: Lecture 2 (Sep 2), slide "Definition: Causality" · the user's notes Ch. 2 §2.1*

^nd-pr-c1a-3-1

- [ ] Q1 **[state]** State the principle as Lecture 2 does.
- [ ] Q2 **[conv]** The lecture writes $\epsilon(x^0)$ for the sign of the time component. What do the notes write, and why?
- [ ] Q3 **[why]** Why is "future" well defined for the causal future of a point but not for spacelike separations?
- [ ] Q4 **[why]** How does causality differ from time-reversal symmetry of the equations of motion?
- [ ] Q5 **[def]** What is the operator form of causality for quantum fields (name and statement)?

> [!tip]- Hints: route in the notes
> - Technique: K14
> - [[§C1a.3 Causal Structure and the Causality of a Single Particle#^cau-c1a-3-1|§C1a.3, Caution: sgn x⁰, not ε(x⁰)]], [[§C1a.3 Causal Structure and the Causality of a Single Particle#^rem-c1a-3-2|§C1a.3, Remark: Causality and time-reversal symmetry]]; orbits Theorem [[§C1a.4 The Lorentz Group#^thm-c1a-4-2|§C1a.4.2]] The Orbits of SO⁺(1,3) on Spacetime, Theorem [[§C1a.4 The Lorentz Group#^thm-c1a-4-3|§C1a.4.3]] Parity and Time Reversal Permute the Orbits; microcausality Principle [[§C2b.4 Microcausality and the Commutator Function#^pr-c2b-4-1|§C2b.4.1]] Microcausality.

### Single-particle propagation amplitude
$U(t, \mathbf x) = \langle\mathbf x|e^{-i\hat Ht}|\mathbf 0\rangle$ for $\hat H = E(\hat{\mathbf P})$, with $\langle\mathbf x|\mathbf p\rangle = e^{i\mathbf p\cdot\mathbf x}$, $\langle\mathbf p|\mathbf p'\rangle = (2\pi)^3\delta^3(\mathbf p - \mathbf p')$; causality would need $U = 0$ for $|\mathbf x| > |t|$, see Definition [[§C1a.3 Causal Structure and the Causality of a Single Particle#^def-c1a-3-1|§C1a.3.1]] Single-Particle Propagation Amplitude. *Source: Lecture 2 (Sep 2), slide "Quantum Causality of Free Particle I" · the user's notes Ch. 2 §2.2 · PS §2.1*

^nd-def-c1a-3-1

- [ ] Q1 **[def]** Define $U(t, \mathbf x)$ and state the normalizations of $|\mathbf x\rangle$, $|\mathbf p\rangle$ used.
- [ ] Q2 **[def]** Why is $U(t, \cdot)$ defined as a kernel rather than as a matrix element between states?
- [ ] Q3 **[conv]** In this section $p$ and $r$ denote what, and how does a reader tell $p^2 = \mathbf p^2$ from the four-vector square?
- [ ] Q4 **[why]** What would causality require of $U$, and why is "$U \ne 0$ outside the cone" a violation?

> [!tip]- Hints: route in the notes
> - Definition [[§C1a.3 Causal Structure and the Causality of a Single Particle#^def-c1a-3-1|§C1a.3.1]] Single-Particle Propagation Amplitude; [[§C1a.3 Causal Structure and the Causality of a Single Particle#^cau-c1a-3-2|§C1a.3, Caution: One symbol, two meanings]].

### How field theory repairs causality
With any number of particles, "one in, one out" happens in two orderings; at spacelike separation the ordering is not invariant, and the criterion for influence becomes the commutator of fields, which vanishes there, see [[§C1a.3 Causal Structure and the Causality of a Single Particle#^rem-c1a-3-3|§C1a.3, Remark: How field theory repairs causality]]. *Source: Lecture 2 (Sep 2), slide "Resolution in Quantum Field Theory" · the user's notes Ch. 2 §2.2*

^nd-rem-c1a-3-3

- [ ] Q1 **[state]** State Lecture 2's resolution in your own words.
- [ ] Q2 **[why]** Why is "propagation from $\mathbf x_0$ to $\mathbf x$" at spacelike separation not an invariant notion?
- [ ] Q3 **[why]** What replaces the amplitude $U$ as the criterion for influence in field theory, and why does it vanish at spacelike separation?
- [ ] Q4 **[why]** For a charged field, what is the second ordering physically?

> [!tip]- Hints: route in the notes
> - Technique: K14
> - [[§C1a.3 Causal Structure and the Causality of a Single Particle#^rem-c1a-3-3|§C1a.3, Remark: How field theory repairs causality]]; Principle [[§C2b.4 Microcausality and the Commutator Function#^pr-c2b-4-1|§C2b.4.1]] Microcausality, Theorem [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-7|§C2b.4.7]] Forward and Backward Amplitudes; orbits Theorem [[§C1a.4 The Lorentz Group#^thm-c1a-4-3|§C1a.4.3]] Parity and Time Reversal Permute the Orbits, part 3.

## Derivations T2

### The amplitude is the Fourier transform of the phase ★
$U(t, \mathbf x) = \int\frac{d^3p}{(2\pi)^3}e^{-iE(\mathbf p)t + i\mathbf p\cdot\mathbf x}$, a tempered distribution, with $U(t, \cdot) \to \delta^3$ as $t \to 0$, see Theorem [[§C1a.3 Causal Structure and the Causality of a Single Particle#^thm-c1a-3-2|§C1a.3.2]] The Amplitude Is the Fourier Transform of the Phase. *Source: Lecture 2 (Sep 2), slide "Quantum Causality of Free Particle I" (insert a complete basis) · the user's notes Ch. 2 §2.2*

^nd-thm-c1a-3-2

- [ ] Q1 **[state]** State the formula and the sense in which it holds.
- [ ] Q2 Insert a complete set of momentum states into $\langle\mathbf x|e^{-i\hat Ht}|\mathbf 0\rangle$: which measure and which overlaps appear?
- [ ] Q3 Why does the integral not converge as an ordinary integral, and why is it still a tempered distribution?
- [ ] Q4 **[why]** Why does $U(t, \cdot) \to \delta^3$ as $t \to 0$? Which convergence theorem is used?

> [!tip]- Hints: route in the notes
> - Technique: K13 (distributions, Fourier tricks)
> - Derivation of Theorem [[§C1a.3 Causal Structure and the Causality of a Single Particle#^thm-c1a-3-2|§C1a.3.2]] The Amplitude Is the Fourier Transform of the Phase, steps 1–3; the Fourier transform on $\mathcal S'$: Definition [[§CA.3 Fourier Transforms and Fourier Tricks#^def-ca-3-1|§CA.3.1]] Fourier Transform in Space and Spacetime.

### The nonrelativistic amplitude is nonzero everywhere ★★
For $E = \mathbf p^2/2m$, $U(t, \mathbf x) = (m/2\pi it)^{3/2}e^{imr^2/2t}$, of modulus $(m/2\pi|t|)^{3/2}$ at every $\mathbf x$, see Theorem [[§C1a.3 Causal Structure and the Causality of a Single Particle#^thm-c1a-3-3|§C1a.3.3]] The Nonrelativistic Amplitude Is Nonzero Everywhere. *Source: Lecture 2 (Sep 2), slides "Quantum Causality of Free Particle I–II" · the user's notes Ch. 2 §2.2 · PS §2.1 p. 14*

^nd-thm-c1a-3-3

- [ ] Q1 **[state]** State the result and what it says about causality.
- [ ] Q2 Complete the square in $-i\frac{\mathbf p^2}{2m}t + i\mathbf p\cdot\mathbf x$ and do the Gaussian integral in each component.
- [ ] Q3 Compute the modulus. Why is it independent of $\mathbf x$?
- [ ] Q4 **[why]** How can the modulus at fixed $\mathbf x \ne 0$ grow as $t \to 0$ while $U \to \delta^3$?
- [ ] Q5 **[why]** Lecture 2: where is "the error" in this computation, and what replaces $\mathbf p^2/2m$?

> [!tip]- Hints: route in the notes
> - Technique: K13
> - Derivation of Theorem [[§C1a.3 Causal Structure and the Causality of a Single Particle#^thm-c1a-3-3|§C1a.3.3]] The Nonrelativistic Amplitude Is Nonzero Everywhere, steps 1–3 (the Gaussian is the QM free propagator).

### The relativistic amplitude is a boundary value ★
$U(z, \mathbf x) = \int\frac{d^3p}{(2\pi)^3}e^{-iE_{\mathbf p}z + i\mathbf p\cdot\mathbf x}$ converges and is analytic for $\operatorname{Im}z < 0$, and $U(t, \cdot) = \lim_{\varepsilon\to0^+}U(t - i\varepsilon, \cdot)$, see Theorem [[§C1a.3 Causal Structure and the Causality of a Single Particle#^thm-c1a-3-4|§C1a.3.4]] The Relativistic Amplitude Is a Boundary Value. *Source: the user's notes Ch. 2 §2.2 (the $t \to t - i\varepsilon$ step)*

^nd-thm-c1a-3-4

- [ ] Q1 **[state]** State the theorem.
- [ ] Q2 Bound $|e^{-iE_{\mathbf p}z}|$ for $z = a - ib$, $b > 0$, and show the integral converges absolutely.
- [ ] Q3 Why may the $z$-derivative be taken under the integral?
- [ ] Q4 **[why]** Why is $t - i\varepsilon$ (and not $t + i\varepsilon$) the side on which positive-energy integrals converge?

> [!tip]- Hints: route in the notes
> - Technique: K13
> - Derivation of Theorem [[§C1a.3 Causal Structure and the Causality of a Single Particle#^thm-c1a-3-4|§C1a.3.4]] The Relativistic Amplitude Is a Boundary Value, steps 1–4; boundary values: [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions|§CA.6]] Boundary Values, iε Limits and Fundamental Solutions.

### The relativistic amplitude as a radial integral ★★
$U(z, r) = \frac{1}{2\pi^2r}\int_0^\infty dp\,p\sin(pr)e^{-iE_pz} = \frac{1}{4\pi^2ir}\int_{-\infty}^\infty dp\,p\,e^{i(pr - E_pz)}$, see Theorem [[§C1a.3 Causal Structure and the Causality of a Single Particle#^thm-c1a-3-5|§C1a.3.5]] The Relativistic Amplitude as a Radial Integral. *Source: Lecture 2 (Sep 2), slide "Relativistic Quantum Causality" · the user's notes Ch. 2 §2.2 · PS §2.1 p. 14 · **[class exercise, Lecture 2]**: the angular integral, "this is something you should probably check"*

^nd-thm-c1a-3-5

- [ ] Q1 **[state]** State both radial forms and the sense in which they hold at real $t$.
- [ ] Q2 Set up spherical coordinates with $\mathbf x$ along the polar axis: what does the integrand depend on, and what does the azimuthal integral give?
- [ ] Q3 **[class exercise, Lecture 2]** Do the $\theta$ integral with $u = \cos\theta$. How does the sign of $du$ restore the order of the limits, and where does $\sin(pr)/r$ come from?
- [ ] Q4 Fold onto the whole line: why is the integrand even in $p$, and what substitution turns the $e^{-ipr}$ term into the $e^{ipr}$ term?
- [ ] Q5 **[conv]** Why does Lecture 2 warn "$|\mathbf p| = p$, $|\mathbf x| = r$"?
- [ ] Q6 **[why]** At real $t$ the integrand grows like $p$. Why is the formula still meaningful?

> [!tip]- Hints: route in the notes
> - Technique: K13
> - Derivation of Theorem [[§C1a.3 Causal Structure and the Causality of a Single Particle#^thm-c1a-3-5|§C1a.3.5]] The Relativistic Amplitude as a Radial Integral, steps 1–3; [[§C1a.3 Causal Structure and the Causality of a Single Particle#^cau-c1a-3-2|§C1a.3, Caution: One symbol, two meanings]]; the boundary value Theorem [[§C1a.3 Causal Structure and the Causality of a Single Particle#^thm-c1a-3-4|§C1a.3.4]] The Relativistic Amplitude Is a Boundary Value.

### The exact radial integral: a Bessel function
**[class exercise, Lecture 2]** "There's obviously a Bessel function … I won't do that because that should be your own joy and homework." The exact amplitude is $U = 2i\partial_tD_W$ with the Wightman function in closed form, see Theorem [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-7|§C2b.3.7]] The Single-Particle Amplitude Is a Time Derivative of the Wightman Function and Theorem [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-8|§C2b.3.8]] The Relativistic Amplitude at Spacelike Separation (digest B). *Source: Lecture 2 (Sep 2), slide "Saddle Point Approximation" ("Details in HW4") and transcript*

^nd-cx-2-1

→ drilled as [[PHY 513 PS Drill#^ps4-3-a|PS4.3(a)]] (the massive Wightman function with $K_1$); the link to $U$ is in NOTES-DIGEST-B (T6)

### The leak is exponentially small but not zero ★★
For $r > |t|$ and $m\rho \gg 1$, $\rho = \sqrt{r^2 - t^2}$, $U \simeq \frac{i m^{3/2}t}{(2\pi\rho)^{3/2}\rho}e^{-m\rho}$: nonzero outside the cone, damped over the Compton wavelength, see Theorem [[§C1a.3 Causal Structure and the Causality of a Single Particle#^thm-c1a-3-6|§C1a.3.6]] The Leak Is Exponentially Small but Not Zero. *Source: Lecture 2 (Sep 2), slides "Saddle Point Approximation", "Quantum Causality id Violated" · the user's notes Ch. 2 §2.2 · PS §2.1 p. 14*

^nd-thm-c1a-3-6

- [ ] Q1 **[state]** State the leading behaviour of $U$ outside the light cone and its decay length.
- [ ] Q2 Write the phase $S(p) = pr - t\sqrt{p^2 + m^2}$ and find its stationary points. Why is the root real inside the cone and imaginary outside?
- [ ] Q3 Which branch of $\sqrt{p_0^2 + m^2}$ does $S'(p_0) = 0$ force at the saddle?
- [ ] Q4 Evaluate $S(p_0)$ and show $e^{iS(p_0)} = e^{-m\rho}$.
- [ ] Q5 Compute $S''(p_0)$ and the Gaussian factor; assemble the prefactor with $f(p_0) = p_0$.
- [ ] Q6 **[why]** Why is the steepest-descent step not automatic here (the saddle lies on a cut), and what justifies it?
- [ ] Q7 **[why]** What does Lecture 2 conclude about a relativistic single-particle theory, and why is the exponentially small leak still fatal in principle?

> [!tip]- Hints: route in the notes
> - Technique: K13 (saddle point on a contour)
> - Derivation of Theorem [[§C1a.3 Causal Structure and the Causality of a Single Particle#^thm-c1a-3-6|§C1a.3.6]] The Leak Is Exponentially Small but Not Zero, steps 1–7; the same exponent: Example [[§CA.5 Gaussian Integrals, Stationary Phase and Bessel Functions#^ex-ca-5-1|§CA.5.1]] The Exponent of the Wightman Function Outside the Light Cone; exact form Theorem [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-8|§C2b.3.8]] The Relativistic Amplitude at Spacelike Separation.

# T3. Classical field theory: action, Euler–Lagrange, Hamiltonian, mass dimension

## Definitions and conventions T3

### Classical field and field configuration
A classical field is a collection of real functions $\phi_a(x)$ on spacetime (a complex component counts as two); a configuration is one such collection, and the values at one time are the coordinates of the system, one set per point of space, see Definition [[§C1b.1 Fields and Their Transformation Laws#^def-c1b-1-1|§C1b.1.1]] Classical Field; Field Configuration. *Source: Lecture 2 (Sep 2), slide "Transformations of Relativistic Fields" · the user's notes Ch. 2 §2.3*

^nd-def-c1b-1-1

- [ ] Q1 **[def]** Define a classical field and a field configuration.
- [ ] Q2 **[why]** In what sense is a field theory mechanics with "one coordinate per point of space"? What plays the role of the index $i$ of $q_i$?
- [ ] Q3 **[why]** How many real components does a complex scalar have, and why does that matter when counting Euler–Lagrange equations?

> [!tip]- Hints: route in the notes
> - Definition [[§C1b.1 Fields and Their Transformation Laws#^def-c1b-1-1|§C1b.1.1]] Classical Field; Field Configuration; Lecture 3 slide "Hamiltonian in Mechanics" ("$i$ = spatial variable $\vec x$").

### Transformation law of a scalar field
$\phi$ is a scalar (spin 0) if $\phi'(x') = \phi(x)$ for $x' = \Lambda x + a$, equivalently $\phi'(x) = \phi(\Lambda^{-1}(x - a))$, see Definition [[§C1b.1 Fields and Their Transformation Laws#^def-c1b-1-2|§C1b.1.2]] Transformation Law of a Scalar Field. *Source: Lecture 2 (Sep 2), slide "Transformations of Relativistic Fields" · the user's notes Ch. 2 §2.3, Ch. 7 · PS (3.2)*

^nd-def-c1b-1-2

- [ ] Q1 **[def]** State the scalar law in both forms.
- [ ] Q2 **[why]** Why is the law not $\phi(\Lambda x) = \phi(x)$? What does that equation say instead?
- [ ] Q3 **[why]** Why the inverse in $\phi(\Lambda^{-1}x)$: give the active-picture reason and the composition reason.
- [ ] Q4 **[conv]** Which picture do the slides use (one event, two labels) and which does PS use? Do they give the same law?
- [ ] Q5 **[def]** Which field of Lecture 2 does change under Lorentz transformations, and what is its spin?

> [!tip]- Hints: route in the notes
> - Technique: K14
> - [[§C1b.1 Fields and Their Transformation Laws#^cau-c1b-1-1|§C1b.1, Caution: What "the scalar does not change" does not mean]], [[§C1b.1 Fields and Their Transformation Laws#^rem-c1b-1-1|§C1b.1, Remark: Why the inverse, and the two readings]]; composition: Theorem [[§C1b.1 Fields and Their Transformation Laws#^thm-c1b-1-1|§C1b.1.1]] The Field Laws Represent the Poincaré Group.

### Transformation law of a general field
$\phi'_a(x') = D(\Lambda)_a{}^b\phi_b(x)$ with $D$ a finite-dimensional representation, $D = 1 + \frac12\omega_{\mu\nu}S^{\mu\nu}$, and translations not acting on the index, see Definition [[§C1b.1 Fields and Their Transformation Laws#^def-c1b-1-3|§C1b.1.3]] Transformation Law of a General Field. *Source: the user's notes Ch. 3 §3.5, Ch. 7 · PS (3.8)*

^nd-def-c1b-1-3

- [ ] Q1 **[def]** State the law and define the spin generators $S^{\mu\nu}$.
- [ ] Q2 What are $D$ and $S^{\mu\nu}$ for a scalar and for a four-vector field?
- [ ] Q3 **[why]** Why must $D$ be a representation, $D(\Lambda_2)D(\Lambda_1) = D(\Lambda_2\Lambda_1)$?
- [ ] Q4 **[conv]** Which convention for $S^{\mu\nu}$ (real or Hermitian) does this box use, and where is the other one?

> [!tip]- Hints: route in the notes
> - Definition [[§C1b.1 Fields and Their Transformation Laws#^def-c1b-1-3|§C1b.1.3]] Transformation Law of a General Field, Example [[§C1b.1 Fields and Their Transformation Laws#^ex-c1b-1-1|§C1b.1.1]] The Four-Vector Field; two meanings of $S^{\mu\nu}$: [[§C3.3 How Fields Transform under the Lorentz Group#^cau-c3-3-2|§C3.3, Caution: Two meanings of S^μν]].

### Lagrangian density, Lagrangian, action
$\mathcal L(\phi_a, \partial_\mu\phi_a)$ at one point; $S = \int d^4x\,\mathcal L = \int dt\,L$ with $L = \int d^3x\,\mathcal L$, see Definition [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^def-c1b-2-1|§C1b.2.1]] Lagrangian Density and Definition [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^def-c1b-2-2|§C1b.2.2]] Action. *Source: Lecture 2 (Sep 2), slide "Actions and Lagrangians"; Lecture 3 (Sep 9), slide "Lagrangean for Scalar Fields" ("density often omitted, sorry") · the user's notes Ch. 3 §3.2*

^nd-def-c1b-2-2

- [ ] Q1 **[def]** Define the Lagrangian density, the Lagrangian and the action, and how they are related.
- [ ] Q2 **[conv]** Which of the three do PS, Yu, the lectures and the problem sets call "the Lagrangian"? What does a problem set mean by "the Hamiltonian" (Lecture 3, transcript)?
- [ ] Q3 **[why]** Why does $\mathcal L$ depend only on the fields and their first derivatives?
- [ ] Q4 **[why]** Why does $L$ itself almost never appear in relativistic field theory?

> [!tip]- Hints: route in the notes
> - [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^cau-c1b-2-1|§C1b.2, Caution: Action, Lagrangian, Lagrangian density]], [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^rem-c1b-2-1|§C1b.2, Remark: Why only first derivatives]].

### Variation and functional derivative
A variation is $\phi_a \to \phi_a + \varepsilon\eta_a$ with $\eta$ a test function supported inside $R$, compared at the same point; $\delta S/\delta\phi_a(x)$ is the kernel of the first variation, a distribution, with $\delta\phi(y)/\delta\phi(x) = \delta^4(x - y)$, see Definition [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^def-c1b-2-3|§C1b.2.3]] Variation; First Variation and Definition [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^def-c1b-2-4|§C1b.2.4]] Functional Derivative. *Source: the user's notes Ch. 3 §3.3*

^nd-def-c1b-2-4

- [ ] Q1 **[def]** Define a variation and the first variation.
- [ ] Q2 **[def]** Define the functional derivative.
- [ ] Q3 Compute $\delta\phi(y)/\delta\phi(x)$ from the definition. Why is it a distribution and not a function?
- [ ] Q4 **[why]** Why must variations vanish near the boundary of $R$, and why "at the same point"?

> [!tip]- Hints: route in the notes
> - [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^rem-c1b-2-2|§C1b.2, Remark: The functional derivative is a distribution]]; test functions Definition [[§CA.2 Generalized Functions#^def-ca-2-1|§CA.2.1]] Test Functions: the Spaces 𝒟 and 𝒮.

### Stationary action for fields
A configuration is a classical solution exactly when $\delta S_R[\phi; \eta] = 0$ for every test function $\eta$ supported inside every bounded region $R$, see Principle [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^pr-c1b-2-3|§C1b.2.3]] Stationary Action for Fields. *Source: Lecture 3 (Sep 9), slide "Lagrangean for Scalar Fields" ("Principle of least action") · the user's notes Ch. 3 §3.3 · PS §2.2*

^nd-pr-c1b-2-3

- [ ] Q1 **[state]** State the principle precisely.
- [ ] Q2 **[why]** Why "stationary" and not "least"?
- [ ] Q3 **[why]** Which boundary condition does the principle choose, and what else could one choose?
- [ ] Q4 **[why]** What role does stationarity play in the quantum theory as $\hbar \to 0$?

> [!tip]- Hints: route in the notes
> - [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^cau-c1b-2-2|§C1b.2, Caution: Boundary conditions are a choice]].

### The free real and complex scalar fields
$\mathcal L = \frac12\partial_\mu\phi\,\partial^\mu\phi - \frac12m^2\phi^2$ (real) and $\mathcal L = \partial_\mu\phi^\ast\partial^\mu\phi - m^2\phi^\ast\phi$ (complex, no $\frac12$), see Model [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^mod-c1b-2-6|§C1b.2.6]] The Free Real Scalar Field and Model [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^mod-c1b-2-7|§C1b.2.7]] The Free Complex Scalar Field. *Source: Lecture 2 (Sep 2), slide "Lagrangian and Action for a Scalar Field"; Lecture 3 (Sep 9), slide "Example 2: Charge Conservation" · the user's notes Ch. 2 §2.3*

^nd-mod-c1b-2-7

- [ ] Q1 **[def]** Write both Lagrangian densities, with and without indices.
- [ ] Q2 **[why]** Which terms are kinetic and which potential energy (Lecture 2)? Why does the kinetic term have no "mass" in front?
- [ ] Q3 **[why]** Why does the complex Lagrangian have no $\frac12$? Where is it hidden?
- [ ] Q4 **[why]** Which assumptions does "free" encode, and what fixes $[\phi] = 1$?
- [ ] Q5 **[def]** What is $m$ in the classical model, and what does it become after quantization?

> [!tip]- Hints: route in the notes
> - [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^rem-c1b-2-5|§C1b.2, Remark: Kinetic minus potential, read term by term]], [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^rem-c1b-2-4|§C1b.2, Remark: The mass parameter after quantization]]; the hidden $\frac12$: Theorem [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-8|§C1b.2.8]] The Complex Field Is Two Real Fields of Equal Mass, step 3.

### Canonical momentum density
$\pi_a = \partial\mathcal L/\partial\dot\phi_a$, taken with the fields, spatial derivatives and other velocities fixed; $(\phi_a(\mathbf x), \pi_a(\mathbf x))$ on one slice are the canonical data, see Definition [[§C1b.4 Hamiltonian Field Theory#^def-c1b-4-1|§C1b.4.1]] Canonical Momentum Density. *Source: Lecture 3 (Sep 9), slide "Hamiltonian in Field Theory" ("one per spatial point") · the user's notes Ch. 3 §3.4 · PS (2.4)*

^nd-def-c1b-4-1

- [ ] Q1 **[def]** Define $\pi_a$ and the canonical data.
- [ ] Q2 **[conv]** The slides and PS3 write $\Pi$; the board, PS and the notes write $\pi$. Which is used in the vault, and why does the name matter later?
- [ ] Q3 **[why]** $\pi$ is the time component of which object? Compute it for the free real field.
- [ ] Q4 **[why]** Give three things $\pi$ is not: the field's momentum, mass times velocity, always defined. Example of each?

> [!tip]- Hints: route in the notes
> - [[§C1b.4 Hamiltonian Field Theory#^cau-c1b-4-1|§C1b.4, Caution: What the conjugate momentum is not]]; register row "Momentum density"; [[§C2a.1 Canonical Quantization of Fields#^cau-c2a-1-1|§C2a.1, Caution: Eₚ, not ωₚ; π, not Π]].

### Hamiltonian density and Hamiltonian
$\mathcal H = \sum_a\pi_a\dot\phi_a - \mathcal L$ with every velocity eliminated, $H = \int d^3x\,\mathcal H$, a functional of the canonical data, see Definition [[§C1b.4 Hamiltonian Field Theory#^def-c1b-4-2|§C1b.4.2]] Hamiltonian Density and Hamiltonian (Legendre Transform). *Source: Lecture 3 (Sep 9), slides "Hamiltonian in Mechanics", "Hamiltonian in Field Theory" · the user's notes Ch. 3 §3.4*

^nd-def-c1b-4-2

- [ ] Q1 **[def]** Define $\mathcal H$ and $H$. When can the Legendre transform be performed?
- [ ] Q2 **[why]** Lecture 3: "A function of $(p, q)$ and not $\dot q$. Eliminate $\dot q$!" Why is an expression still containing $\dot\phi$ not yet a Hamiltonian?
- [ ] Q3 **[why]** Why is $H$ not a Lorentz scalar (Lecture 3, "Towards Quantization"), and what is the trade-off against path integrals?
- [ ] Q4 **[def]** With several fields, how many momenta and Legendre terms are there?

> [!tip]- Hints: route in the notes
> - [[§C1b.4 Hamiltonian Field Theory#^rem-c1b-4-1|§C1b.4, Remark: Why a Hamiltonian, and what it costs]], [[§C1b.4 Hamiltonian Field Theory#^rem-c1b-4-2|§C1b.4, Remark: Several fields, and a non-canonical normalization]]; why $H$ is not a scalar: [[§C1b.7 Spacetime Symmetries꞉ Energy and Momentum#^rem-c1b-7-1|§C1b.7, Remark: Why the 00 component is the Hamiltonian density]].

### Poisson bracket of field functionals
$\{F, G\} = \sum_a\int d^3z\bigl(\frac{\delta F}{\delta\phi_a(\mathbf z)}\frac{\delta G}{\delta\pi_a(\mathbf z)} - \frac{\delta F}{\delta\pi_a(\mathbf z)}\frac{\delta G}{\delta\phi_a(\mathbf z)}\bigr)$, see Definition [[§C1b.4 Hamiltonian Field Theory#^def-c1b-4-3|§C1b.4.3]] Poisson Bracket of Field Functionals. *Source: the user's notes Ch. 3 §3.4*

^nd-def-c1b-4-3

- [ ] Q1 **[def]** Define the field Poisson bracket and its sign convention.
- [ ] Q2 **[why]** When is the bracket defined, and why does smearing with test functions help?
- [ ] Q3 **[why]** What does canonical quantization do to the bracket, with which factor of $i$?

> [!tip]- Hints: route in the notes
> - [[§C1b.4 Hamiltonian Field Theory#^rem-c1b-4-5|§C1b.4, Remark: From brackets to commutators]]; the fundamental brackets Theorem [[§C1b.4 Hamiltonian Field Theory#^thm-c1b-4-5|§C1b.4.5]] Fundamental Brackets of Fields.

### Locality, relativistic invariance and the three principles
Locality: $\mathcal L(x)$ depends on the fields and finitely many derivatives at the single point $x$; relativistic invariance: $\mathcal L$ is a scalar; with causality these are Lecture 2's three principles, see Principle [[§C1b.3 Mass Dimension, Locality and Power Counting#^pr-c1b-3-4|§C1b.3.4]] Locality, Principle [[§C1b.3 Mass Dimension, Locality and Power Counting#^pr-c1b-3-5|§C1b.3.5]] Relativistic Invariance and [[§C1b.3 Mass Dimension, Locality and Power Counting#^rem-c1b-3-1|§C1b.3, Remark: The three principles of quantum field theory]]. *Source: Lecture 2 (Sep 2), slides "Locality", "Symmetry", "Principles of Quantum Field Theory" · the user's notes Ch. 2 §2.4*

^nd-pr-c1b-3-4

- [ ] Q1 **[state]** State the principles of locality and relativistic invariance.
- [ ] Q2 **[def]** Name Lecture 2's three principles of quantum field theory.
- [ ] Q3 **[why]** Why do minor nonlocalities of a microscopic theory become derivative terms at long distances?
- [ ] Q4 **[why]** "Quantum field theory is a low energy theory; it is mostly determined by symmetry." Explain both halves.

> [!tip]- Hints: route in the notes
> - [[§C1b.3 Mass Dimension, Locality and Power Counting#^rem-c1b-3-2|§C1b.3, Remark: Why local terms dominate at long distances]], [[§C1b.3 Mass Dimension, Locality and Power Counting#^rem-c1b-3-1|§C1b.3, Remark: The three principles of quantum field theory]]; the consequence: Theorem [[§C1b.3 Mass Dimension, Locality and Power Counting#^thm-c1b-3-6|§C1b.3.6]] Symmetry and Power Counting Fix the Scalar Lagrangian.

### Relevant, marginal and irrelevant terms
A term $g_{\mathcal O}\mathcal O$ is relevant, marginal or irrelevant as $[g_{\mathcal O}] = 4 - [\mathcal O]$ is positive, zero or negative; irrelevant effects at energy $E$ are suppressed by $(E/\Lambda)^k$, see Definition [[§C1b.3 Mass Dimension, Locality and Power Counting#^def-c1b-3-1|§C1b.3.1]] Relevant, Marginal and Irrelevant Terms. *Source: Lecture 2 (Sep 2), slide "Low Energy Effective Theory" · the user's notes Ch. 2 §2.4*

^nd-def-c1b-3-1

- [ ] Q1 **[def]** Define the three classes.
- [ ] Q2 Classify $m^2\phi^2$, $\phi^3$, $\phi^4$, $\phi^6$, $(\partial\phi)^4$ in four dimensions.
- [ ] Q3 **[why]** Why do irrelevant terms die at low energy? Estimate the suppression.
- [ ] Q4 **[why]** Lecture 2: "More fields cost the same as more derivatives." Why, for scalars in four dimensions?

> [!tip]- Hints: route in the notes
> - Technique: K8
> - [[§C1b.3 Mass Dimension, Locality and Power Counting#^rem-c1b-3-3|§C1b.3, Remark: Why irrelevant terms die at low energy]]; the dimensions: Theorem [[§C1b.3 Mass Dimension, Locality and Power Counting#^thm-c1b-3-3|§C1b.3.3]] Mass Dimension of Couplings.

## Derivations T3

### The field laws represent the Poincaré group ★
$(T(g)\phi)_a(x) = D(\Lambda)_a{}^b\phi_b(g^{-1}x)$ is linear, $T(1, 0) = 1$, and $T(g_2)T(g_1) = T(g_2g_1)$; without the inverse the order would reverse, see Theorem [[§C1b.1 Fields and Their Transformation Laws#^thm-c1b-1-1|§C1b.1.1]] The Field Laws Represent the Poincaré Group. *Source: the user's notes Ch. 7 ("The inverse is not a typo")*

^nd-thm-c1b-1-1

- [ ] Q1 **[state]** State the theorem and the "without the inverse" remark.
- [ ] Q2 How do Poincaré transformations compose, $g_2g_1 = (\,?, \,?)$?
- [ ] Q3 Apply $T(g_1)$, then $T(g_2)$: which argument and which matrix product result?
- [ ] Q4 **[why]** Show that $S(g)\phi(x) = \phi(gx)$ composes in the reverse order.

> [!tip]- Hints: route in the notes
> - Technique: K14
> - Derivation of Theorem [[§C1b.1 Fields and Their Transformation Laws#^thm-c1b-1-1|§C1b.1.1]] The Field Laws Represent the Poincaré Group, steps 1–6.

### Infinitesimal form of the field laws ★
For $\Lambda = 1 + \omega$ and small $a$: $\phi'(x) = \phi - a^\mu\partial_\mu\phi + \frac12\omega_{\mu\nu}(x^\mu\partial^\nu - x^\nu\partial^\mu)\phi$, plus $\frac12\omega_{\mu\nu}S^{\mu\nu}$ on the components for a general field, see Theorem [[§C1b.1 Fields and Their Transformation Laws#^thm-c1b-1-2|§C1b.1.2]] Infinitesimal Form of the Field Laws. *Source: the user's notes Ch. 3 §3.5, Ch. 7 · PS §2.2 p. 18*

^nd-thm-c1b-1-2

- [ ] Q1 **[state]** State both formulas and name the orbital and spin parts.
- [ ] Q2 Expand $\Lambda^{-1}$ to first order and write the shifted point $g^{-1}x$.
- [ ] Q3 Taylor expand $\phi_b(g^{-1}x)$. Which second-order term is dropped?
- [ ] Q4 Lower the index on $\omega$ and antisymmetrize: show $\omega_{\rho\nu}x^\nu\partial^\rho = \frac12\omega_{\rho\nu}(x^\nu\partial^\rho - x^\rho\partial^\nu)$.
- [ ] Q5 **[why]** Why does the factor $\frac12$ appear with $\omega_{\mu\nu}$, and what doubles if it is dropped?

> [!tip]- Hints: route in the notes
> - Technique: K2
> - Derivation of Theorem [[§C1b.1 Fields and Their Transformation Laws#^thm-c1b-1-2|§C1b.1.2]] Infinitesimal Form of the Field Laws, steps 1–7; antisymmetry of $\omega$: Theorem [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-1|§C1a.6.1]] Infinitesimal Lorentz Transformations Are Antisymmetric.

### The four-vector field's spin generators ★
For $A^\alpha$, $D = \Lambda$ and $(S^{\mu\nu})^\alpha{}_\beta = g^{\mu\alpha}\delta^\nu{}_\beta - g^{\nu\alpha}\delta^\mu{}_\beta$ with $\frac12\omega_{\mu\nu}S^{\mu\nu} = \omega$, see Example [[§C1b.1 Fields and Their Transformation Laws#^ex-c1b-1-1|§C1b.1.1]] The Four-Vector Field. *Source: the user's notes Ch. 3 §3.5 · PS §3.1 p. 37*

^nd-ex-c1b-1-1

- [ ] Q1 **[state]** State $D$ and $S^{\mu\nu}$ for upper and for lower components.
- [ ] Q2 Check $\frac12\omega_{\mu\nu}(S^{\mu\nu})^\alpha{}_\beta = \omega^\alpha{}_\beta$ term by term.
- [ ] Q3 Why are the lower-component generators minus the transpose?
- [ ] Q4 **[why]** Which two representations act at once on a vector field configuration?

> [!tip]- Hints: route in the notes
> - Technique: K2
> - The check in Example [[§C1b.1 Fields and Their Transformation Laws#^ex-c1b-1-1|§C1b.1.1]] The Four-Vector Field; [[§C1b.1 Fields and Their Transformation Laws#^rem-c1b-1-2|§C1b.1, Remark: Two representations at once]].

### The Klein–Gordon equation is Poincaré covariant ★★
If $\phi'(x) = \phi(\Lambda^{-1}(x - a))$, then $((\partial^2 + m^2)\phi')(x) = ((\partial^2 + m^2)\phi)(\Lambda^{-1}(x - a))$, so Poincaré transforms of solutions are solutions, see Theorem [[§C1b.1 Fields and Their Transformation Laws#^thm-c1b-1-3|§C1b.1.3]] The Klein–Gordon Equation Is Poincaré Covariant. *Source: Lecture 2 (Sep 2), slide "Klein Gordon Equation" ("Simplest relativistically invariant equation of motion") · PS (3.3)–(3.5) · the user's notes Ch. 2 §2.3*

^nd-thm-c1b-1-3

- [ ] Q1 **[state]** State the theorem.
- [ ] Q2 Compute $\partial_\mu\phi'(x)$ by the chain rule. Why does the translation drop out?
- [ ] Q3 Compute $\partial^2\phi'(x)$. Which property of $\Lambda^{-1}$ turns $g^{\mu\nu}(\Lambda^{-1})^\rho{}_\mu(\Lambda^{-1})^\sigma{}_\nu$ into $g^{\rho\sigma}$?
- [ ] Q4 Why does the converse (solution of the transformed equation implies solution of the original) hold?
- [ ] Q5 **[why]** Lecture 2 calls KG "the simplest relativistically invariant equation". Why must the two second derivatives enter with opposite signs, and which index placement test does that correspond to?

> [!tip]- Hints: route in the notes
> - Technique: K14, K2
> - Derivation of Theorem [[§C1b.1 Fields and Their Transformation Laws#^thm-c1b-1-3|§C1b.1.3]] The Klein–Gordon Equation Is Poincaré Covariant, steps 1–6; [[§C1b.1 Fields and Their Transformation Laws#^rem-c1b-1-3|§C1b.1, Remark: What the Klein–Gordon equation is, and what it is not]].

### The nonrelativistic limit of Klein–Gordon
**[class exercise, Lecture 2]** Asked whether Klein–Gordon is "the relativistic limit of the Schrödinger equation", Larsen: "this goes the wrong way … you can check the other way around … that the Klein–Gordon equation gives a sensible non-relativistic limit." No QFT box carries the limit; [[§C1b.1 Fields and Their Transformation Laws#^rem-c1b-1-3|§C1b.1, Remark: What the Klein–Gordon equation is, and what it is not]] records it and points to Relativity §B4.1 (outside the QFT catalogue). *Source: Lecture 2 (Sep 2), transcript (Q&A at the end) · the user's notes Ch. 2 §2.3 (Discussion)*

^nd-cx-2-2

- [ ] Q1 **[state]** What is to be checked: which equation should emerge, for which part of the solution, in which limit?
- [ ] Q2 Restore $c$ in the Klein–Gordon equation and write $\phi = e^{-imc^2t/\hbar}\psi$.
- [ ] Q3 Insert, and identify the term with $\ddot\psi$ that is small compared with $mc^2\dot\psi/\hbar$. Which equation for $\psi$ remains?
- [ ] Q4 **[why]** Why can one not go the other way and derive Klein–Gordon from Schrödinger?
- [ ] Q5 **[why]** Which solutions are lost or misread when one keeps only the positive-frequency factor?

> [!tip]- Hints: route in the notes
> - Technique: K8 (restoring $c$ first: P4, step 2)
> - [[§C1b.1 Fields and Their Transformation Laws#^rem-c1b-1-3|§C1b.1, Remark: What the Klein–Gordon equation is, and what it is not]]; Relativity §B4.1 (Connections) for the limit itself.

### A scalar Lagrangian density gives an invariant action ★
If the fields transform by their laws and $\mathcal L$ is a scalar, $S_{gR}[\phi'] = S_R[\phi]$ and transforms of stationary configurations are stationary, see Theorem [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-1|§C1b.2.1]] A Scalar Lagrangian Density Gives an Invariant Action. *Source: PS (3.5) · the user's notes Ch. 3 §3.3 · Lecture 2 (Sep 2), slide "Lagrangian and Action for a Scalar Field" ("Total Lagrangian density is relativistically invariant")*

^nd-thm-c1b-2-1

- [ ] Q1 **[state]** State the theorem with its hypothesis on $\mathcal L$.
- [ ] Q2 Change variables $x = gy$: what is the Jacobian, and why is it $1$?
- [ ] Q3 Show that $\partial_\mu\phi'\,\partial^\mu\phi'$ at $x$ equals $\partial_\mu\phi\,\partial^\mu\phi$ at $y$.
- [ ] Q4 **[why]** Why are variations carried along by $T(g)$, so that stationarity transfers?

> [!tip]- Hints: route in the notes
> - Technique: K14
> - Derivation of Theorem [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-1|§C1b.2.1]] A Scalar Lagrangian Density Gives an Invariant Action, steps 1–4; Theorem [[§C1a.4 The Lorentz Group#^thm-c1a-4-1|§C1a.4.1]] Invariant Volume Elements.

### The variation commutes with derivatives ★★
At fixed argument, $\delta(\partial_\mu\phi_a) = \partial_\mu(\delta\phi_a)$ and $\delta\mathcal L = \sum_a[\frac{\partial\mathcal L}{\partial\phi_a}\delta\phi_a + \frac{\partial\mathcal L}{\partial(\partial_\mu\phi_a)}\partial_\mu(\delta\phi_a)]$, see Theorem [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-2|§C1b.2.2]] The Variation Commutes with Derivatives. *Source: Lecture 3 (Sep 9), slide "Euler-Lagrange Equations" ("Notes: $\delta(\partial_\mu\phi) = \partial_\mu(\delta\phi)$") · the user's notes Ch. 3 §3.3*

^nd-thm-c1b-2-2

- [ ] Q1 **[state]** State both identities and the hypothesis "at fixed argument".
- [ ] Q2 Prove the first by linearity of $\partial_\mu$.
- [ ] Q3 Derive the second from Taylor's theorem in the $5n$ arguments of $\mathcal L$.
- [ ] Q4 **[why]** Why does the first identity fail when the transformation also moves the point? Which extra term appears?

> [!tip]- Hints: route in the notes
> - Technique: K2
> - Derivation of Theorem [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-2|§C1b.2.2]] The Variation Commutes with Derivatives, steps 1–3; [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^rem-c1b-2-3|§C1b.2, Remark: When the point moves, the variation no longer commutes with ∂]]; Theorem [[§C1b.7 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-7-1|§C1b.7.1]] Total and Fixed-Argument Variations.

### Euler–Lagrange equations for fields ★★
$\phi$ is stationary iff $\partial_\mu\frac{\partial\mathcal L}{\partial(\partial_\mu\phi_a)} - \frac{\partial\mathcal L}{\partial\phi_a} = 0$ for each $a$; the functional derivative of $S$ is $\frac{\partial\mathcal L}{\partial\phi_a} - \partial_\mu\frac{\partial\mathcal L}{\partial(\partial_\mu\phi_a)}$, see Theorem [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-4|§C1b.2.4]] Euler–Lagrange Equations for Fields. *Source: Lecture 3 (Sep 9), slide "Euler-Lagrange Equations" · the user's notes Ch. 3 §3.3 · PS (2.2)–(2.3)*

^nd-thm-c1b-2-4

- [ ] Q1 **[state]** State the Euler–Lagrange equations and the functional derivative of the action.
- [ ] Q2 Differentiate $S_R[\phi + \varepsilon\eta]$ at $\varepsilon = 0$. Why may the derivative pass under the integral?
- [ ] Q3 Use the product rule on $\Pi^\mu_a\partial_\mu\eta_a$. Which total derivative appears?
- [ ] Q4 Why does the boundary term vanish (Lecture 3: "we can impose boundary conditions so $\delta\phi = 0$ on the boundary")?
- [ ] Q5 Localize: why does $\int E_a\eta_a = 0$ for all test functions force $E_a = 0$ pointwise?
- [ ] Q6 **[why]** "Each step of the derivation is relativistically invariant" (Lecture 3). Why is that, and why is there one equation per real component?

> [!tip]- Hints: route in the notes
> - Technique: K2
> - Derivation of Theorem [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-4|§C1b.2.4]] Euler–Lagrange Equations for Fields, steps 1–7; [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^cau-c1b-2-2|§C1b.2, Caution: Boundary conditions are a choice]].

### A total divergence does not change the field equations ★
$\mathcal L$ and $\mathcal L + \partial_\mu K^\mu$ (local $K$) have the same first variation and the same stationary configurations; for $K^\mu(\phi, x)$ the Euler–Lagrange expressions coincide identically, see Theorem [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-5|§C1b.2.5]] A Total Divergence Does Not Change the Field Equations. *Source: PS §2.2 p. 17 · Lecture 3 (Sep 9), slide "Noether's Theorem" ("L is invariant up to a total derivative")*

^nd-thm-c1b-2-5

- [ ] Q1 **[state]** State the theorem.
- [ ] Q2 Write $S'_R - S_R$ as a surface integral.
- [ ] Q3 Why does the surface integral not change when $\phi$ is varied by a test function?
- [ ] Q4 For $K^\mu(\phi, x)$, compute the two Euler–Lagrange ingredients of $\partial_\nu K^\nu$ and show they cancel.
- [ ] Q5 **[why]** Why is this the reason Noether symmetries may change $\mathcal L$ "up to a total derivative"?

> [!tip]- Hints: route in the notes
> - Technique: K2
> - Derivation of Theorem [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-5|§C1b.2.5]] A Total Divergence Does Not Change the Field Equations, steps 1–4; [[§C1b.5 Noether's Theorem#^rem-c1b-5-5|§C1b.5, Remark: Why a total derivative is allowed]].

### The Klein–Gordon equation from its Lagrangian ★★
For $\mathcal L = \frac12\partial_\mu\phi\,\partial^\mu\phi - \frac12m^2\phi^2$: $\partial\mathcal L/\partial\phi = -m^2\phi$, $\partial\mathcal L/\partial(\partial_\mu\phi) = \partial^\mu\phi$, and the Euler–Lagrange equation is $(\partial^2 + m^2)\phi = 0$, see Model [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^mod-c1b-2-6|§C1b.2.6]] The Free Real Scalar Field and [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^cau-c1b-2-3|§C1b.2, Caution: Rename the dummy index before differentiating]]. *Source: Lecture 3 (Sep 9), slide "Example: the Scalar Field" · the user's notes Ch. 3 §3.3 · **[class exercise, Lecture 3]**: "you double check" the derivative of the kinetic term (with Q4 of the four-vector derivatives entry)*

^nd-mod-c1b-2-6

- [ ] Q1 **[state]** State the two ingredients and the resulting equation.
- [ ] Q2 Rename the dummy index in the kinetic term and differentiate with $\partial(\partial_\nu\phi)/\partial(\partial_\mu\phi) = \delta^\mu{}_\nu$. Why do both factors respond?
- [ ] Q3 **[conv]** "Sloppy notation: $(\partial\phi)^2$" (Lecture 3). What does it stand for, with which metric?
- [ ] Q4 Assemble the Euler–Lagrange equation and check the sign of the mass term.
- [ ] Q5 **[why]** Where does a stray factor $\frac12$ come from if $\partial_\mu\phi$ and $\partial^\mu\phi$ are treated as independent?

> [!tip]- Hints: route in the notes
> - Technique: K2
> - [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^cau-c1b-2-3|§C1b.2, Caution: Rename the dummy index before differentiating]] (the "act of hygiene"); Theorem [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-10|§C1a.5.10]] Derivatives with Respect to a Four-Vector, part 3; Theorem [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-4|§C1b.2.4]] Euler–Lagrange Equations for Fields.

### The dilaton's nonlinear field equation
$\mathcal L = -f^2e^{-2\tau}(\partial\tau)^2$ gives $\partial^2\tau = (\partial\tau)^2$, see Example [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^ex-c1b-2-1|§C1b.2.1]] A Nonlinear Field Equation: the Dilaton. *Source: PS2 Problem 1(b)*

^nd-ex-c1b-2-1

→ drilled as [[PHY 513 PS Drill#^ps2-1-b|PS2.1(b)]]

### The field equation of a cubic self-interaction
$\mathcal L = \frac12(\partial\phi)^2 - \frac12m^2\phi^2 - \frac{\lambda}{3!}\phi^3$ gives $(\partial^2 + m^2)\phi + \frac\lambda2\phi^2 = 0$, see Example [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^ex-c1b-2-2|§C1b.2.2]] The Field Equation of a Cubic Self-Interaction. *Source: PS7 Problem 1(b)*

^nd-ex-c1b-2-2

→ drilled as [[PHY 513 PS Drill#^ps7-1-b|PS7.1(b)]]

### The complex field is two real fields of equal mass ★
With $\phi = (\phi_1 + i\phi_2)/\sqrt2$, $\partial_\mu\phi^\ast\partial^\mu\phi - m^2\phi^\ast\phi = \sum_j[\frac12(\partial\phi_j)^2 - \frac12m^2\phi_j^2]$, and the phase $e^{i\alpha}$ is the rotation of $(\phi_1, \phi_2)$ by $\alpha$, see Theorem [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-8|§C1b.2.8]] The Complex Field Is Two Real Fields of Equal Mass. *Source: the user's notes Ch. 2 §2.3 · PS §2.2 p. 18*

^nd-thm-c1b-2-8

- [ ] Q1 **[state]** State the decomposition and the meaning of the phase rotation.
- [ ] Q2 Expand $\phi^\ast\phi$ in real components. Why do the cross terms cancel?
- [ ] Q3 Expand the kinetic term the same way.
- [ ] Q4 Write $e^{i\alpha}\phi$ in components and read off the rotation matrix.
- [ ] Q5 **[why]** Why does the complex Lagrangian carry no $\frac12$, and why does the $1/\sqrt2$ make each real component canonically normalized?
- (Invariance of the complex $\mathcal L$ with a potential $V(\phi^\ast\phi)$ → drilled as [[PHY 513 PS Drill#^ps2-3-c|PS2.3(c)]].)

> [!tip]- Hints: route in the notes
> - Technique: K2
> - Derivation of Theorem [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-8|§C1b.2.8]] The Complex Field Is Two Real Fields of Equal Mass, steps 1–4.

### Field and conjugate as independent variables ★
With $\partial/\partial\phi = \frac1{\sqrt2}(\partial_1 - i\partial_2)$ and $\partial/\partial\phi^\ast = \frac1{\sqrt2}(\partial_1 + i\partial_2)$, the two real Euler–Lagrange equations hold iff $\partial_\mu\frac{\partial\mathcal L}{\partial(\partial_\mu\phi^\ast)} - \frac{\partial\mathcal L}{\partial\phi^\ast} = 0$ (and its conjugate), see Theorem [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-9|§C1b.2.9]] Field and Conjugate as Independent Variables. *Source: the user's notes Ch. 2 §2.3, Ch. 3 §3.3 · PS §2.2 p. 18*

^nd-thm-c1b-2-9

- [ ] Q1 **[state]** State the theorem and the definitions of the two derivative operators.
- [ ] Q2 Check $\partial\phi/\partial\phi = 1$ and $\partial\phi^\ast/\partial\phi = 0$ with these definitions.
- [ ] Q3 Write $(E_1 + iE_2)/\sqrt2$ and $(E_1 - iE_2)/\sqrt2$ in terms of the complex derivatives.
- [ ] Q4 Why is the linear map $(E_1, E_2) \mapsto$ (complex combinations) invertible, and why is one complex equation enough?
- [ ] Q5 **[why]** Why is it legitimate to "treat $\phi$ and $\phi^\ast$ as independent" although they are not?
- (The equations with a potential $V(\phi^\ast\phi)$ → drilled as [[PHY 513 PS Drill#^ps2-3-a|PS2.3(a)]].)

> [!tip]- Hints: route in the notes
> - Technique: K2
> - Derivation of Theorem [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-9|§C1b.2.9]] Field and Conjugate as Independent Variables, steps 1–5.

### The action is dimensionless ★★
In natural units $[S] = 0$, so $[\mathcal L] = d$, i.e. $[\mathcal L] = 4$ in four dimensions, see Theorem [[§C1b.3 Mass Dimension, Locality and Power Counting#^thm-c1b-3-1|§C1b.3.1]] The Action Is Dimensionless. *Source: Lecture 2 (Sep 2), slides "Dimensional Analysis" ("Action in units of $\hbar$"), "Mass Dimensions" · the user's notes Ch. 2 §2.4*

^nd-thm-c1b-3-1

- [ ] Q1 **[state]** State the theorem.
- [ ] Q2 Why is an action a multiple of $\hbar$? Use the exponent rule on $ML^2T^{-1}$.
- [ ] Q3 **[why]** Why must $S/\hbar$ be a pure number in quantum mechanics?
- [ ] Q4 Derive $[\mathcal L] = d$ from $[d^dx] = -d$.
- [ ] Q5 Check $[\mathcal L] = 4$ from "energy per volume" in ordinary units.

> [!tip]- Hints: route in the notes
> - Technique: K8
> - Derivation of Theorem [[§C1b.3 Mass Dimension, Locality and Power Counting#^thm-c1b-3-1|§C1b.3.1]] The Action Is Dimensionless, steps 1–4.

### Mass dimension of fields ★★
$[\phi] = \frac{d - 2}{2}$, $[\psi] = \frac{d - 1}{2}$, $[A_\mu] = \frac{d - 2}{2}$ from canonically normalized kinetic terms; $1$, $\frac32$, $1$ in four dimensions, see Theorem [[§C1b.3 Mass Dimension, Locality and Power Counting#^thm-c1b-3-2|§C1b.3.2]] Mass Dimension of Fields. *Source: Lecture 2 (Sep 2), slides "Dimensional Analysis", "Mass Dimensions" ("$[\phi] = M$") · the user's notes Ch. 2 §2.4*

^nd-thm-c1b-3-2

- [ ] Q1 **[state]** State the three mass dimensions in $d$ dimensions.
- [ ] Q2 Derive $[\phi]$ from $\frac12\partial_\mu\phi\,\partial^\mu\phi$.
- [ ] Q3 Derive $[\psi]$ from $\bar\psi i\gamma^\mu\partial_\mu\psi$. Why are the $\gamma^\mu$ dimensionless?
- [ ] Q4 Derive $[A_\mu]$ from $F_{\mu\nu}F^{\mu\nu}$.
- [ ] Q5 **[why]** Why does the kinetic term decide, and what would a rescaling $\phi \to \kappa\phi$ with dimensionful $\kappa$ change?

> [!tip]- Hints: route in the notes
> - Technique: K8
> - Derivation of Theorem [[§C1b.3 Mass Dimension, Locality and Power Counting#^thm-c1b-3-2|§C1b.3.2]] Mass Dimension of Fields, steps 1–4.

### Mass dimension of couplings ★★
$[g_{\mathcal O}] = d - [\mathcal O]$; for $g_n\phi^n$, $[g_n] = d - n\frac{d - 2}{2}$, i.e. $4 - n$ in four dimensions, see Theorem [[§C1b.3 Mass Dimension, Locality and Power Counting#^thm-c1b-3-3|§C1b.3.3]] Mass Dimension of Couplings. *Source: Lecture 2 (Sep 2), slides "Mass Dimensions", "Symmetry" · the user's notes Ch. 2 §2.4 · PS2 Problem 2(d)*

^nd-thm-c1b-3-3

- [ ] Q1 **[state]** State the rule for a general term and for $\phi^n$.
- [ ] Q2 Derive it from "every term of $\mathcal L$ has dimension $d$".
- [ ] Q3 Give the four-dimensional dimensions of $m^2$, the $\phi^3$ and $\phi^4$ couplings, $c_6\phi^6$ and $(\partial\phi)^4$.
- [ ] Q4 In which dimension is $\phi^6$ marginal, and in which $\phi^3$? What is special about $d = 2$?
- [ ] Q5 **[why]** Lecture 2: "Option: add more powers of $\phi$. OK but not too many." Why, in terms of this rule?
- (The couplings of PS2 Problem 2 → drilled as [[PHY 513 PS Drill#^ps2-2-d|PS2.2(d)]].)

> [!tip]- Hints: route in the notes
> - Technique: K8
> - Derivation of Theorem [[§C1b.3 Mass Dimension, Locality and Power Counting#^thm-c1b-3-3|§C1b.3.3]] Mass Dimension of Couplings, steps 1–4.

### The dilaton's dimensions; the Yukawa coupling
$[\tau] = 0$, $[f] = 1$ for $\mathcal L = -f^2e^{-2\tau}(\partial\tau)^2$; $[\phi] = 1$, $[\psi] = \frac32$, $[g] = 0$ for $g\phi\bar\psi\psi$, see Example [[§C1b.3 Mass Dimension, Locality and Power Counting#^ex-c1b-3-1|§C1b.3.1]] A Field in an Exponent: the Dilaton and Example [[§C1b.3 Mass Dimension, Locality and Power Counting#^ex-c1b-3-2|§C1b.3.2]] The Yukawa Coupling Is Dimensionless. *Source: PS2 Problem 1(a); PS7 Problem 1(a)*

^nd-ex-c1b-3-1

→ drilled as [[PHY 513 PS Drill#^ps2-1-a|PS2.1(a)]] and [[PHY 513 PS Drill#^ps7-1-a|PS7.1(a)]]

### Units restored in the scalar action ★★
$\frac S\hbar = \int c\,dt\,d^3x\,[\frac{1}{2c^2}(\partial_t\phi)^2 - \frac12(\nabla\phi)^2 - \frac12(\frac{mc}{\hbar})^2\phi^2]$ and $\hbar\omega = \sqrt{(\hbar c\mathbf k)^2 + (mc^2)^2}$, see Example [[§C1b.3 Mass Dimension, Locality and Power Counting#^ex-c1b-3-3|§C1b.3.3]] Units Restored in the Scalar Action. *Source: Lecture 2 (Sep 2), slide "Dimensional Analysis" · the user's notes Ch. 2 §2.4 · **[class exercise, Lecture 2]**: "How do I restore them? … that's actually a pretty good exercise"*

^nd-ex-c1b-3-3

- [ ] Q1 **[state]** What is the target: which combination must be a pure number?
- [ ] Q2 What dimension must $\mathcal L$ have if $d^4x = c\,dt\,d^3x$?
- [ ] Q3 Anchor on the gradient term: what is $[\phi]$ in this normalization?
- [ ] Q4 Match the time-derivative term and the mass term: which powers of $c$ and $\hbar$ appear?
- [ ] Q5 Restore the dispersion relation by making every term an energy.
- [ ] Q6 **[conv]** The Lecture 2 slide writes $\frac{1}{c^2}(\partial_t\phi)^2$ without the $\frac12$. Which is right, and why?
- [ ] Q7 **[why]** Why is the "physical" dimension of $\phi$ a normalization convention while its mass dimension is not?

> [!tip]- Hints: route in the notes
> - Technique: K8
> - Example [[§C1b.3 Mass Dimension, Locality and Power Counting#^ex-c1b-3-3|§C1b.3.3]] Units Restored in the Scalar Action, steps 1–6; procedure P4, steps 1, 4, 5 (anchor and match); [[§C1b.3 Mass Dimension, Locality and Power Counting#^cau-c1b-3-1|§C1b.3, Caution: The physical dimension of a field is a normalization convention]].

### Symmetry and power counting fix the scalar Lagrangian ★★
A local, Lorentz-invariant polynomial in one real scalar with only relevant and marginal terms, positive kinetic term and bounded potential is, up to total derivatives, a constant, a shift and a rescaling, $\frac12(\partial\phi)^2 - \frac12m^2\phi^2 - \frac{g}{3!}\phi^3 - \frac{\lambda}{4!}\phi^4$; with $\phi \to -\phi$ symmetry and minimum at $0$, $g = 0$, see Theorem [[§C1b.3 Mass Dimension, Locality and Power Counting#^thm-c1b-3-6|§C1b.3.6]] Symmetry and Power Counting Fix the Scalar Lagrangian. *Source: Lecture 2 (Sep 2), slides "Symmetry", "Low Energy Effective Theory" ($V = \frac12m^2\phi^2 + \frac1{24}\lambda\phi^4$) · the user's notes Ch. 2 §2.4*

^nd-thm-c1b-3-6

- [ ] Q1 **[state]** State the theorem with all its hypotheses.
- [ ] Q2 Write the general local monomial and its dimension. What does "relevant or marginal" restrict $n + k$ to?
- [ ] Q3 Why must the number of derivatives be even, and which contractions are allowed?
- [ ] Q4 List the candidate operators with $k = 0$ and $k = 2$. Which are total derivatives, and which reduce to $\partial_\mu\phi\,\partial^\mu\phi$ up to one?
- [ ] Q5 Why may the kinetic coefficient be normalized to $\frac12$, and why must it be positive?
- [ ] Q6 Remove the constant and the linear term. What is $m^2$ in terms of $V$?
- [ ] Q7 **[why]** Why does $\phi \to -\phi$ with the minimum at $0$ kill the cubic term? Why not contract a single derivative with a vector $A^\mu$?

> [!tip]- Hints: route in the notes
> - Technique: K8, K14
> - Derivation of Theorem [[§C1b.3 Mass Dimension, Locality and Power Counting#^thm-c1b-3-6|§C1b.3.6]] Symmetry and Power Counting Fix the Scalar Lagrangian, steps 1–11; total derivatives Theorem [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-5|§C1b.2.5]] A Total Divergence Does Not Change the Field Equations; [[§C1b.3 Mass Dimension, Locality and Power Counting#^rem-c1b-3-4|§C1b.3, Remark: Why not contract one derivative with a vector, A^μ∂_μφ]].

### The momentum density is a functional derivative ★
$\delta L/\delta\dot\phi_a(\mathbf x) = \pi_a(\mathbf x)$; on a lattice of cells, $p_j = \pi(\mathbf x_j)\Delta V$: $\pi$ is momentum per unit volume, see Theorem [[§C1b.4 Hamiltonian Field Theory#^thm-c1b-4-1|§C1b.4.1]] The Momentum Density Is a Functional Derivative. *Source: PS §2.2 p. 16 · the user's notes Ch. 3 §3.4*

^nd-thm-c1b-4-1

- [ ] Q1 **[state]** State both forms.
- [ ] Q2 Vary the velocity field alone: why may the derivative pass under $\int d^3y$?
- [ ] Q3 Read off the kernel. Why is it a continuous function here?
- [ ] Q4 **[why]** On the lattice of cells, why does $\dot\phi_j$ occur in one term only, and where does $\Delta V$ come from?

> [!tip]- Hints: route in the notes
> - Derivation of Theorem [[§C1b.4 Hamiltonian Field Theory#^thm-c1b-4-1|§C1b.4.1]] The Momentum Density Is a Functional Derivative, steps 1–4.

### The Hamiltonian density of the free real field ★★
$\pi = \dot\phi$, $\mathcal H = \frac12\pi^2 + \frac12(\nabla\phi)^2 + \frac12m^2\phi^2$, $H \ge 0$, see Theorem [[§C1b.4 Hamiltonian Field Theory#^thm-c1b-4-2|§C1b.4.2]] Hamiltonian Density of the Free Real Field. *Source: Lecture 3 (Sep 9), slide "Hamiltonian of Free Scalar Theory" · the user's notes Ch. 3 §3.4 · PS (2.8)*

^nd-thm-c1b-4-2

- [ ] Q1 **[state]** State $\pi$, $\mathcal H$ and $H$.
- [ ] Q2 Write $\mathcal L$ without indices and compute $\pi$. Why "not $m\dot\phi$" (Lecture 3)?
- [ ] Q3 Do the Legendre transform. Which signs flip?
- [ ] Q4 Eliminate $\dot\phi$. Why is this step required before calling the result a Hamiltonian?
- [ ] Q5 **[why]** Why is $H \ge 0$, and what is the classical ground state for $m > 0$ and for $m = 0$?

> [!tip]- Hints: route in the notes
> - Derivation of Theorem [[§C1b.4 Hamiltonian Field Theory#^thm-c1b-4-2|§C1b.4.2]] Hamiltonian Density of the Free Real Field, steps 1–5; [[§C1b.4 Hamiltonian Field Theory#^cau-c1b-4-1|§C1b.4, Caution: What the conjugate momentum is not]].

### The Hamiltonian density of the free complex field
$\pi = \dot\phi^\ast$, $\pi^\ast = \dot\phi$, $\mathcal H = \pi^\ast\pi + \nabla\phi^\ast\cdot\nabla\phi + m^2\phi^\ast\phi$, see Theorem [[§C1b.4 Hamiltonian Field Theory#^thm-c1b-4-3|§C1b.4.3]] Hamiltonian Density of the Free Complex Field. *Source: PS2 Problem 3(b); PS3 Problem 2(a1)*

^nd-thm-c1b-4-3

→ drilled as [[PHY 513 PS Drill#^ps2-3-b|PS2.3(b)]] (with $V$) and [[PHY 513 PS Drill#^ps3-2-a1|PS3.2(a1)]]

### Hamilton's equations for fields ★
Stationarity of $\int d^4x(\sum\pi_a\dot\phi_a - \mathcal H)$ gives $\dot\phi_a = \delta H/\delta\pi_a$, $\dot\pi_a = -\delta H/\delta\phi_a = -\frac{\partial\mathcal H}{\partial\phi_a} + \nabla\cdot\frac{\partial\mathcal H}{\partial(\nabla\phi_a)}$, equivalent to the Euler–Lagrange equations, see Theorem [[§C1b.4 Hamiltonian Field Theory#^thm-c1b-4-4|§C1b.4.4]] Hamilton's Equations for Fields. *Source: the user's notes Ch. 3 §3.4 · Yu (1.171)–(1.175)*

^nd-thm-c1b-4-4

- [ ] Q1 **[state]** State Hamilton's equations for fields.
- [ ] Q2 Vary $\phi$ and $\pi$ independently in the phase-space action; move the time and space derivatives off the test functions.
- [ ] Q3 Why do the divergences integrate to zero?
- [ ] Q4 Compute $\delta H/\delta\phi_a$ on one slice: where does the $\nabla\cdot$ term come from?
- [ ] Q5 Show that the first equation inverts $\pi = \partial\mathcal L/\partial\dot\phi$, and the second reproduces Euler–Lagrange.
- [ ] Q6 **[why]** For the free real field, which term of $\dot\pi$ couples neighbouring points?

> [!tip]- Hints: route in the notes
> - Derivation of Theorem [[§C1b.4 Hamiltonian Field Theory#^thm-c1b-4-4|§C1b.4.4]] Hamilton's Equations for Fields, steps 1–8; Example [[§C1b.4 Hamiltonian Field Theory#^ex-c1b-4-1|§C1b.4.1]] Hamilton's Equations of the Free Real Field.

### Fundamental Poisson brackets of fields ★
$\{\phi_a(f), \pi_b(g)\} = \delta_{ab}\int fg$, others zero; in kernel form $\{\phi_a(\mathbf x), \pi_b(\mathbf y)\} = \delta_{ab}\delta^3(\mathbf x - \mathbf y)$; for the complex field $\{\phi, \pi\} = \{\phi^\ast, \pi^\ast\} = \delta^3$, $\{\phi, \pi^\ast\} = 0$, see Theorem [[§C1b.4 Hamiltonian Field Theory#^thm-c1b-4-5|§C1b.4.5]] Fundamental Brackets of Fields. *Source: the user's notes Ch. 3 §3.4*

^nd-thm-c1b-4-5

- [ ] Q1 **[state]** State the smeared and kernel forms.
- [ ] Q2 Compute the functional derivatives of the smeared field $\phi_a(f)$.
- [ ] Q3 Insert into the bracket: which term survives?
- [ ] Q4 For the complex field, compute $\{\phi, \pi\}$ and $\{\phi, \pi^\ast\}$ in real components.
- [ ] Q5 **[why]** Why is the kernel form an identity of distributions, and what fails at coinciding points?

> [!tip]- Hints: route in the notes
> - Derivation of Theorem [[§C1b.4 Hamiltonian Field Theory#^thm-c1b-4-5|§C1b.4.5]] Fundamental Brackets of Fields, steps 1–5; [[§C1b.4 Hamiltonian Field Theory#^rem-c1b-4-5|§C1b.4, Remark: From brackets to commutators]].

### Time evolution by the bracket ★
$dF/dt = \{F, H\}$ for functionals without explicit time dependence; in particular $\dot\phi_a = \{\phi_a, H\}$, $\dot\pi_a = \{\pi_a, H\}$, and $\{H, H\} = 0$, see Theorem [[§C1b.4 Hamiltonian Field Theory#^thm-c1b-4-6|§C1b.4.6]] Time Evolution by the Bracket. *Source: the user's pre-course notes §1.6 · CM analogue*

^nd-thm-c1b-4-6

- [ ] Q1 **[state]** State the theorem.
- [ ] Q2 Apply the chain rule for functionals along a solution.
- [ ] Q3 Insert Hamilton's equations and recognize the bracket.
- [ ] Q4 **[why]** Why is energy conserved, and which hypothesis on $\mathcal H$ is needed?

> [!tip]- Hints: route in the notes
> - Derivation of Theorem [[§C1b.4 Hamiltonian Field Theory#^thm-c1b-4-6|§C1b.4.6]] Time Evolution by the Bracket, steps 1–4.

# T4. Noether: currents, charges, energy–momentum tensor, Lorentz charges

## Definitions and conventions T4

### The instances of δ
$\delta\phi$ (arbitrary variation at fixed $x$), $\alpha\Delta\phi$ (symmetry variation at fixed $x$), $\delta x^\mu$ (displacement), $\bar\delta\phi = \phi'(x) - \phi(x)$, the total change $\phi'(x') - \phi(x)$, and derived $\delta(\partial\phi)$, $\delta\mathcal L$, $\delta S$, see Definition [[§C1b.5 Noether's Theorem#^def-c1b-5-1|§C1b.5.1]] The Instances of δ. *Source: the user's notes Ch. 3 §3.5 · Yu §1.7.1*

^nd-def-c1b-5-1

- [ ] Q1 **[def]** List the instances of δ and what each compares.
- [ ] Q2 **[why]** Which of them commute with $\partial_\mu$, and why?
- [ ] Q3 **[why]** In the lecture's Noether theorem the point never moves. Which instance is $\alpha\Delta\phi$ then?

> [!tip]- Hints: route in the notes
> - Definition [[§C1b.5 Noether's Theorem#^def-c1b-5-1|§C1b.5.1]] The Instances of δ; Theorem [[§C1b.7 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-7-1|§C1b.7.1]] Total and Fixed-Argument Variations; [[§C1b.5 Noether's Theorem#^rem-c1b-5-4|§C1b.5, Remark: Why the variation passes inside the derivative]].

### Continuous transformation, generator, symmetry variation
A continuous transformation is a family labelled by global, infinitesimal parameters $\alpha^a$; its generators are $\Delta_a\phi_i = \partial\phi'_i(x)/\partial\alpha^a|_0$, and the symmetry variation is $\delta\phi_i = \alpha^a\Delta_a\phi_i$, see Definition [[§C1b.5 Noether's Theorem#^def-c1b-5-2|§C1b.5.2]] Continuous Transformation; Parameters, Definition [[§C1b.5 Noether's Theorem#^def-c1b-5-3|§C1b.5.3]] Generator of a Continuous Transformation and Definition [[§C1b.5 Noether's Theorem#^def-c1b-5-4|§C1b.5.4]] Symmetry Variation. *Source: Lecture 3 (Sep 9), slide "Noether's Theorem" ("$\phi \to \phi + \alpha\Delta\phi$") · the user's notes Ch. 3 §3.5 · PS (2.9)*

^nd-def-c1b-5-4

- [ ] Q1 **[def]** Define a continuous transformation, its parameters (two adjectives), its generators and its symmetry variation.
- [ ] Q2 **[def]** What is the difference between $\delta\phi$ and $\Delta\phi$? Which one enters the current, and why?
- [ ] Q3 **[conv]** Transforming by $+\alpha$ or $-\alpha$: what changes in $\Delta\phi$ and in the current, and what does not?
- [ ] Q4 **[why]** Why is nothing lost by working to first order in $\alpha$?

> [!tip]- Hints: route in the notes
> - [[§C1b.5 Noether's Theorem#^rem-c1b-5-1|§C1b.5, Remark: δ and Δ side by side, and why only first order]], [[§C1b.5 Noether's Theorem#^rem-c1b-5-2|§C1b.5, Remark: The sign of a parameter is a convention]]; Theorem [[§C1b.5 Noether's Theorem#^thm-c1b-5-3|§C1b.5.3]] The First-Order Test Decides the Whole Family.

### Symmetry of the action; the vector 𝒥
A continuous transformation is a symmetry if, for every configuration, $\delta\mathcal L = \alpha^a\partial_\mu\mathcal J^\mu_a$; this defines $\mathcal J$, and the test has three outcomes: $\delta\mathcal L = 0$ ($\mathcal J = 0$), a nonzero divergence, or not a divergence, see Definition [[§C1b.5 Noether's Theorem#^def-c1b-5-5|§C1b.5.5]] Symmetry of the Action; the Vector 𝒥. *Source: Lecture 3 (Sep 9), slide "Noether's Theorem" ("L is invariant up to a total derivative … The total derivative defines $J^\mu(x)$") · the user's notes Ch. 3 §3.5 · PS (2.10)*

^nd-def-c1b-5-5

- [ ] Q1 **[def]** Define a symmetry of the action and the vector $\mathcal J^\mu$.
- [ ] Q2 **[def]** List the three outcomes of the test with one example each.
- [ ] Q3 **[why]** Why is a total derivative allowed? What does the action do on the boundary?
- [ ] Q4 **[why]** Must the test hold on solutions only, or for every configuration? Why does it matter?

> [!tip]- Hints: route in the notes
> - [[§C1b.5 Noether's Theorem#^rem-c1b-5-5|§C1b.5, Remark: Why a total derivative is allowed]], [[§C1b.5 Noether's Theorem#^rem-c1b-5-10|§C1b.5, Remark: The three outcomes of the test and their currents]].

### Charge density and Noether charge
$\rho = j^0$, $Q_V(t) = \int_Vd^3x\,j^0$, $Q = \int d^3x\,j^0$, one charge per parameter, see Definition [[§C1b.6 Conserved Charges and Internal Symmetries#^def-c1b-6-1|§C1b.6.1]] Charge Density and Definition [[§C1b.6 Conserved Charges and Internal Symmetries#^def-c1b-6-2|§C1b.6.2]] Noether Charge. *Source: Lecture 3 (Sep 9), slide "Noether's Charge" · the user's notes Ch. 3 §3.5 · PS (2.13)*

^nd-def-c1b-6-2

- [ ] Q1 **[def]** Define the charge density and the Noether charge of a current.
- [ ] Q2 **[why]** Lecture 3: "The charge density $j^0 = \rho$ is not necessarily electric charge density." Give a counterexample from the course.
- [ ] Q3 **[conv]** The Lecture 3 slide writes $\partial_\mu j^\mu = \partial_0j^0 - \vec\nabla\cdot\vec j$. What is the correct sign, and does the conclusion change?

> [!tip]- Hints: route in the notes
> - [[§C1b.6 Conserved Charges and Internal Symmetries#^cau-c1b-6-1|§C1b.6, Caution: The sign in the slides' continuity equation]]; Theorem [[§C1b.6 Conserved Charges and Internal Symmetries#^thm-c1b-6-1|§C1b.6.1]] Continuity Equation and Conservation of the Charge; the shift charge Example [[§C1b.6 Conserved Charges and Internal Symmetries#^ex-c1b-6-1|§C1b.6.1]] Shift Symmetry of the Massless Field, item 6.

### Symmetry of a transformation that moves the point
$x \to x + \delta x$, $\phi'_a(x') = \phi_a(x) + \delta\phi_a$ is a symmetry if $\int_{R'}d^4x'\,\mathcal L'(x') = \int_Rd^4x\,\mathcal L(x)$ to first order for every region and configuration, see Definition [[§C1b.7 Spacetime Symmetries꞉ Energy and Momentum#^def-c1b-7-1|§C1b.7.1]] Symmetry of a Transformation That Moves the Point. *Source: Yu §1.7.1 · the user's notes Ch. 3 §3.5*

^nd-def-c1b-7-1

- [ ] Q1 **[def]** Define a symmetry when the point moves.
- [ ] Q2 Give $\delta x^\mu$ for a translation, a Lorentz transformation and an internal symmetry.
- [ ] Q3 **[why]** Why is the region also transformed, $R \to R'$?

> [!tip]- Hints: route in the notes
> - Definition [[§C1b.7 Spacetime Symmetries꞉ Energy and Momentum#^def-c1b-7-1|§C1b.7.1]] Symmetry of a Transformation That Moves the Point; Theorem [[§C1b.7 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-7-2|§C1b.7.2]] The Volume Element to First Order.

### Canonical energy–momentum tensor
$T^\mu{}_\nu = \sum_a\frac{\partial\mathcal L}{\partial(\partial_\mu\phi_a)}\partial_\nu\phi_a - \delta^\mu{}_\nu\mathcal L$, $T^{\mu\nu} = g^{\nu\rho}T^\mu{}_\rho$; $\mu$ the current index, $\nu$ the translation, $a$ the field component, see Definition [[§C1b.7 Spacetime Symmetries꞉ Energy and Momentum#^def-c1b-7-2|§C1b.7.2]] Canonical Energy–Momentum Tensor. *Source: Lecture 3 (Sep 9), slide "Example 3: Spacetime Translation" · the user's notes Ch. 3 §3.5 · PS (2.17)*

^nd-def-c1b-7-2

- [ ] Q1 **[def]** Define $T^\mu{}_\nu$ and $T^{\mu\nu}$, and say what each index labels.
- [ ] Q2 **[conv]** The lecture and PS translate by $x \to x - a$; Yu by $x' = x + \varepsilon$. What sign does each current carry in terms of $T$, and is the tensor the same?
- [ ] Q3 **[why]** When is $T^{\mu\nu}$ a Lorentz tensor, and when is the canonical one symmetric?

> [!tip]- Hints: route in the notes
> - [[§C1b.7 Spacetime Symmetries꞉ Energy and Momentum#^cau-c1b-7-1|§C1b.7, Caution: One picture at a time; the sign of the displacement]]; the table of canonical tensors [[§C1b.7 Spacetime Symmetries꞉ Energy and Momentum#^rem-c1b-7-3|§C1b.7, Remark: The canonical tensor of the standard fields]].

### Angular-momentum and boost charges
$J^{\nu\rho} = \int d^3x\,\mathcal M^{0\nu\rho} = L^{\nu\rho} + S^{\nu\rho}$; $J^i = \frac12\varepsilon_{ijk}J^{jk}$, $\mathbf J = (J^{23}, J^{31}, J^{12})$; boost charges $K^i = J^{i0}$, see Definition [[§C1b.8 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^def-c1b-8-1|§C1b.8.1]] Angular-Momentum and Boost Charges. *Source: the user's notes Ch. 3 §3.5 · Yu §1.7.3*

^nd-def-c1b-8-1

- [ ] Q1 **[def]** Define $J^{\nu\rho}$, its orbital and spin parts, $\mathbf J$ and $K^i$.
- [ ] Q2 **[conv]** The register's "boost generator $K^i = J^{0i}$" and this $K^i = J^{i0}$: are they the same object? How are they related?
- [ ] Q3 **[conv]** How do Yu's $I^{\mu\nu}$, $J^{\mu\nu\rho}$, $\Theta^{\mu\nu}$ correspond to the notes' $S^{\mu\nu}$, $\mathcal M^{\mu\nu\rho}$, $T_B^{\mu\nu}$?

> [!tip]- Hints: route in the notes
> - [[§C1b.8 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^cau-c1b-8-1|§C1b.8, Caution: Notation in Yu and in the conventions table]]; register row "Lorentz transformations".

## Derivations T4

### Generators of the standard transformations ★★
Shift $\Delta\phi = 1$; phase $\Delta\phi = i\phi$, $\Delta\phi^\ast = -i\phi^\ast$; rotation of two real fields $\Delta\phi_1 = -\phi_2$, $\Delta\phi_2 = \phi_1$; translation $x \to x - a$, $\Delta_\nu\phi = \partial_\nu\phi$; Lorentz $\frac12\omega_{\mu\nu}(x^\mu\partial^\nu - x^\nu\partial^\mu)\phi$; scale $\phi + x^\mu\partial_\mu\phi$; and $\Delta(\partial_\mu\phi) = \partial_\mu(\Delta\phi)$, see Theorem [[§C1b.5 Noether's Theorem#^thm-c1b-5-1|§C1b.5.1]] Generators of the Standard Transformations. *Source: Lecture 3 (Sep 9), slides "Example 1: Field Translation", "Example 2: Charge Conservation", "Example 3: Spacetime Translation" · the user's notes Ch. 3 §3.5*

^nd-thm-c1b-5-1

- [ ] Q1 **[state]** Give the generator of each standard transformation.
- [ ] Q2 Expand $e^{i\alpha}\phi$ and the rotation matrix to first order and read off $\Delta$.
- [ ] Q3 For the translation $x \to x - a$, show $\phi'(x) = \phi(x + a)$ and $\Delta_\nu\phi = +\partial_\nu\phi$.
- [ ] Q4 For the Lorentz transformation, where does the factor $\frac12$ come from?
- [ ] Q5 **[why]** Why are derivatives of the field never transformed independently?
- [ ] Q6 **[why]** The shift has a generator in the massive theory too. Does having a generator make it a symmetry?

> [!tip]- Hints: route in the notes
> - Technique: K12
> - Derivation of Theorem [[§C1b.5 Noether's Theorem#^thm-c1b-5-1|§C1b.5.1]] Generators of the Standard Transformations, steps 1–8; [[§C1b.5 Noether's Theorem#^rem-c1b-5-3|§C1b.5, Remark: What step 1 does not decide]].

### Two routes to δℒ ★★
$\delta\mathcal L$ at fixed $x$ is given by substituting the transformed fields (finite or truncated) or by the chain rule $\alpha^a\sum_i[\frac{\partial\mathcal L}{\partial\phi_i}\Delta_a\phi_i + \frac{\partial\mathcal L}{\partial(\partial_\mu\phi_i)}\partial_\mu\Delta_a\phi_i]$, summed over every independent field variable; neither uses the equations of motion, see Theorem [[§C1b.5 Noether's Theorem#^thm-c1b-5-2|§C1b.5.2]] Two Routes to δℒ. *Source: Lecture 3 (Sep 9), slide "Noether's Theorem" ("Vary Lagrangean explicitly") · the user's notes Ch. 3 §3.5*

^nd-thm-c1b-5-2

- [ ] Q1 **[state]** State the two routes and over which variables the sum runs.
- [ ] Q2 Write route 1 as the derivative of $f(\alpha) = \mathcal L(\phi + \alpha\Delta\phi, \partial\phi + \alpha\partial\Delta\phi)$ at $\alpha = 0$.
- [ ] Q3 Why do the finite and the truncated substitutions give the same first-order result?
- [ ] Q4 Evaluate the derivative by the chain rule to get route 2.
- [ ] Q5 **[why]** A field without derivatives in $\mathcal L$ (such as $\bar\psi$): does it contribute to $\delta\mathcal L$, and does it contribute to the current?

> [!tip]- Hints: route in the notes
> - Technique: K12
> - Derivation of Theorem [[§C1b.5 Noether's Theorem#^thm-c1b-5-2|§C1b.5.2]] Two Routes to δℒ, steps 1–5; [[§C1b.5 Noether's Theorem#^rem-c1b-5-8|§C1b.5, Remark: What the sum over fields runs over]].

### δℒ for the complex scalar phase, by both routes
$\phi \to e^{i\alpha}\phi$ leaves $\partial_\mu\phi^\ast\partial^\mu\phi - m^2\phi^\ast\phi - V(\phi^\ast\phi)$ invariant: four chain-rule terms cancel in pairs, see Example [[§C1b.5 Noether's Theorem#^ex-c1b-5-1|§C1b.5.1]] δℒ for the Complex Scalar Phase, by Both Routes. *Source: PS2 Problem 3(c)*

^nd-ex-c1b-5-1

→ drilled as [[PHY 513 PS Drill#^ps2-3-c|PS2.3(c)]]

### δℒ for the Dirac phase, by both routes ★
For $\mathcal L = \bar\psi(i\gamma^\mu\partial_\mu - m)\psi$ and $\psi \to e^{i\alpha}\psi$, $\bar\psi \to e^{-i\alpha}\bar\psi$: route 1 gives $\delta\mathcal L = 0$ at once; route 2 needs the $\partial\mathcal L/\partial\bar\psi$ term although $\mathcal L$ has no $\partial\bar\psi$; the current is $-\bar\psi\gamma^\mu\psi$, see Example [[§C1b.5 Noether's Theorem#^ex-c1b-5-2|§C1b.5.2]] δℒ for the Dirac Phase, by Both Routes. *Source: PS §3.4 p. 51 · the user's notes Ch. 3 §3.5, Ch. 8 · read after Model [[§C5a.7 The Dirac Equation and Its Lagrangian#^mod-c5a-7-3|§C5a.7.3]] The Free Dirac Field*

^nd-ex-c1b-5-2

- [ ] Q1 **[state]** State the generators of $\psi$ and $\bar\psi$ under the phase, and why $\Delta\bar\psi = -i\bar\psi$.
- [ ] Q2 Route 1: why does the constant phase pass through $\partial_\mu$ and commute with $\gamma^\mu$?
- [ ] Q3 Route 2: compute the four derivatives $\partial\mathcal L/\partial\psi_c$, $\partial\mathcal L/\partial(\partial_\mu\psi_c)$, $\partial\mathcal L/\partial\bar\psi_a$, $\partial\mathcal L/\partial(\partial_\mu\bar\psi_a)$.
- [ ] Q4 Add the terms (a)–(c). Which term would be missing if $\bar\psi$ were dropped because it has no derivative?
- [ ] Q5 **[why]** Why does $\bar\psi$ contribute nothing to the Noether current although it is needed in $\delta\mathcal L$?

> [!tip]- Hints: route in the notes
> - Technique: K12
> - Example [[§C1b.5 Noether's Theorem#^ex-c1b-5-2|§C1b.5.2]] δℒ for the Dirac Phase, by Both Routes, items (a)–(d); Theorem [[§C5a.8 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-8-3|§C5a.8.3]] The Vector Current.

### The first-order test decides the whole family ★
If the first-order test holds for every configuration of a one-parameter group $T_\alpha$, then $\mathcal L[T_\alpha\phi] = \mathcal L[\phi] + \partial_\mu K^\mu_\alpha$ with $K_\alpha = \int_0^\alpha d\beta\,\mathcal J[T_\beta\phi]$; $\delta\mathcal L = 0$ for all configurations gives exact invariance, see Theorem [[§C1b.5 Noether's Theorem#^thm-c1b-5-3|§C1b.5.3]] The First-Order Test Decides the Whole Family. *Source: the user's notes Ch. 3 §3.5 ("finite transformations are compositions of small ones")*

^nd-thm-c1b-5-3

- [ ] Q1 **[state]** State the theorem.
- [ ] Q2 Use the group law to write a step $\beta \to \beta + \varepsilon$ as a small transformation of $T_\beta\phi$.
- [ ] Q3 Apply the test at $\chi = T_\beta\phi$ and get $g'(\beta)$.
- [ ] Q4 Integrate in $\beta$ and take $\partial_\mu$ outside. What justifies it?
- [ ] Q5 **[why]** Why must the test hold for every configuration, not only for $\phi$?

> [!tip]- Hints: route in the notes
> - Derivation of Theorem [[§C1b.5 Noether's Theorem#^thm-c1b-5-3|§C1b.5.3]] The First-Order Test Decides the Whole Family, steps 1–5.

### Noether's theorem ★★
For a symmetry with $\mathcal J^\mu_a$, $j^\mu_a = \sum_i\frac{\partial\mathcal L}{\partial(\partial_\mu\phi_i)}\Delta_a\phi_i - \mathcal J^\mu_a$ satisfies $\partial_\mu j^\mu_a = -\sum_i[\frac{\partial\mathcal L}{\partial\phi_i} - \partial_\mu\frac{\partial\mathcal L}{\partial(\partial_\mu\phi_i)}]\Delta_a\phi_i$ off shell, hence $\partial_\mu j^\mu_a = 0$ on shell, see Theorem [[§C1b.5 Noether's Theorem#^thm-c1b-5-4|§C1b.5.4]] Noether's Theorem. *Source: Lecture 3 (Sep 9), slides "Noether's Theorem" (both) · the user's notes Ch. 3 §3.5 · PS (2.11)–(2.12)*

^nd-thm-c1b-5-4

- [ ] Q1 **[state]** State the current, the off-shell identity and the on-shell conservation law.
- [ ] Q2 Formula 1: what does the symmetry give for $\delta\mathcal L$, for every configuration?
- [ ] Q3 Formula 2: compute $\delta\mathcal L$ by the chain rule with $\delta\phi = \alpha\Delta\phi$. Why is $\delta(\partial_\mu\phi) = \alpha\partial_\mu\Delta\phi$?
- [ ] Q4 Move the derivative with the product rule, keeping the total derivative. What is kept that the action principle discarded?
- [ ] Q5 Equate the two formulas and collect the divergences.
- [ ] Q6 **[why]** The Lecture 3 slide writes "$= \alpha\partial_\mu(\frac{\partial\mathcal L}{\partial(\partial_\mu\phi)}\Delta\phi)$" with "1. Impose equation of motion". At which step do the equations of motion enter, and why only there?
- [ ] Q7 **[why]** With several fields and parameters, how many currents are there, and what is summed?

> [!tip]- Hints: route in the notes
> - Technique: K12
> - Derivation of Theorem [[§C1b.5 Noether's Theorem#^thm-c1b-5-4|§C1b.5.4]] Noether's Theorem, steps 1–9; [[§C1b.5 Noether's Theorem#^rem-c1b-5-6|§C1b.5, Remark: The action principle's computation, run backwards]]; P3, steps 1–5.

### The divergence of the current when the test fails ★
If $\delta\mathcal L = \alpha(\partial_\mu\mathcal J^\mu + X)$, the would-be current $j^\mu = \sum_i\pi^\mu_i\Delta\phi_i - \mathcal J^\mu$ has $\partial_\mu j^\mu = X$ on shell, see Theorem [[§C1b.5 Noether's Theorem#^thm-c1b-5-5|§C1b.5.5]] The Divergence of the Current When the Test Fails. *Source: the user's notes Ch. 3 §3.5 (Example 1 with a mass)*

^nd-thm-c1b-5-5

- [ ] Q1 **[state]** State the off-shell and on-shell identities.
- [ ] Q2 Rederive them by the steps of Noether's proof with the remainder $X$ kept.
- [ ] Q3 **[why]** The split of $\delta\mathcal L$ into divergence and remainder is not unique. Why is the statement still well defined?
- [ ] Q4 **[why]** What does the theorem give for $dQ_V/dt$?

> [!tip]- Hints: route in the notes
> - Technique: K12
> - Derivation of Theorem [[§C1b.5 Noether's Theorem#^thm-c1b-5-5|§C1b.5.5]] The Divergence of the Current When the Test Fails, steps 1–7; [[§C1b.5 Noether's Theorem#^rem-c1b-5-10|§C1b.5, Remark: The three outcomes of the test and their currents]].

### Continuity equation and conservation of the charge ★★
$\partial_\mu j^\mu = 0$ is $\partial_t\rho + \nabla\cdot\mathbf j = 0$; $dQ_V/dt = -\oint_{\partial V}\mathbf j\cdot d\mathbf S$; $Q$ is constant if $|\mathbf j|$ falls off faster than $1/r^2$, see Theorem [[§C1b.6 Conserved Charges and Internal Symmetries#^thm-c1b-6-1|§C1b.6.1]] Continuity Equation and Conservation of the Charge. *Source: Lecture 3 (Sep 9), slide "Noether's Charge" · the user's notes Ch. 3 §3.5*

^nd-thm-c1b-6-1

- [ ] Q1 **[state]** State the continuity equation and the two conclusions.
- [ ] Q2 Write $\partial_\mu j^\mu$ in components. With which sign does $\nabla\cdot\mathbf j$ enter?
- [ ] Q3 Integrate over $V$ and move $d/dt$ outside. What justifies it?
- [ ] Q4 Apply the divergence theorem and bound the flux through a large sphere.
- [ ] Q5 **[conv]** Compare with the Lecture 3 slide's sign. Is the conclusion affected?
- [ ] Q6 **[why]** "Simplest setting: no flux at infinity." What fall-off is needed for $Q$, and what for moments such as $J^{\nu\rho}$?

> [!tip]- Hints: route in the notes
> - Derivation of Theorem [[§C1b.6 Conserved Charges and Internal Symmetries#^thm-c1b-6-1|§C1b.6.1]] Continuity Equation and Conservation of the Charge, steps 1–5; [[§C1b.6 Conserved Charges and Internal Symmetries#^cau-c1b-6-1|§C1b.6, Caution: The sign in the slides' continuity equation]]; moments: Theorem [[§C1b.8 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^thm-c1b-8-3|§C1b.8.3]] The Centre of Energy Moves Uniformly.

### Improvement terms ★
For antisymmetric $B^{\nu\mu}$, $\partial_\mu\partial_\nu B^{\nu\mu} = 0$ identically, so $j + \partial_\nu B^{\nu\mu}$ is conserved with the same charge if $B^{i0}$ falls off, see Theorem [[§C1b.6 Conserved Charges and Internal Symmetries#^thm-c1b-6-2|§C1b.6.2]] Improvement Terms. *Source: PS2 Problem 4(d) (statement) · the user's notes Ch. 3 §3.5*

^nd-thm-c1b-6-2

- [ ] Q1 **[state]** State both parts.
- [ ] Q2 Prove part 1 by relabelling dummies.
- [ ] Q3 Show that the charge density changes by a spatial divergence. Why does $B^{00}$ drop out?
- [ ] Q4 **[why]** What does the theorem say about the uniqueness of Noether currents, and what does it not say?

> [!tip]- Hints: route in the notes
> - Technique: K2
> - Derivation of Theorem [[§C1b.6 Conserved Charges and Internal Symmetries#^thm-c1b-6-2|§C1b.6.2]] Improvement Terms, steps 1–4; [[§C1b.6 Conserved Charges and Internal Symmetries#^cau-c1b-6-2|§C1b.6, Caution: What the theorem does and does not say]].

### Shift symmetry of the massless field ★★
For $\mathcal L = \frac12(\partial\phi)^2$, $\phi \to \phi + \alpha$ has $\Delta\phi = 1$, $\mathcal J = 0$, $j^\mu = \partial^\mu\phi$, conserved by the massless equation; with a mass, $\delta\mathcal L = -\alpha m^2\phi$ is not a divergence, see Example [[§C1b.6 Conserved Charges and Internal Symmetries#^ex-c1b-6-1|§C1b.6.1]] Shift Symmetry of the Massless Field. *Source: Lecture 3 (Sep 9), slide "Example 1: Field Translation" ("Check current conservation") · the user's notes Ch. 3 §3.5*

^nd-ex-c1b-6-1

- [ ] Q1 **[state]** State the generator, $\mathcal J$, the current and the charge.
- [ ] Q2 Substitute $\phi + \alpha$ into $\mathcal L$: why is it invariant?
- [ ] Q3 Check conservation of $j^\mu$ using the massless Klein–Gordon equation (slide), and off shell against the identity of Noether's theorem.
- [ ] Q4 With a mass, compute $\delta\mathcal L$. Show it is not a divergence using a bump configuration.
- [ ] Q5 **[why]** Lecture 3 (transcript): "symmetry, conservation law; no symmetry, no conservation law." Which line of the computation shows the second half?

> [!tip]- Hints: route in the notes
> - Technique: K12
> - Example [[§C1b.6 Conserved Charges and Internal Symmetries#^ex-c1b-6-1|§C1b.6.1]] Shift Symmetry of the Massless Field, items 1–6 and "With a mass"; Theorem [[§C1b.5 Noether's Theorem#^thm-c1b-5-5|§C1b.5.5]] The Divergence of the Current When the Test Fails.

### The U(1) current of the complex scalar field: checking conservation ★★
$j^\mu = i(\phi\partial^\mu\phi^\ast - \phi^\ast\partial^\mu\phi)$ for $\mathcal L = \partial_\mu\phi^\ast\partial^\mu\phi - m^2\phi^\ast\phi - V(\phi^\ast\phi)$ is conserved on solutions for every $m$ and $V$; its charge is the number charge, and a positive-frequency solution has $j^0 < 0$ in this sign, see Theorem [[§C1b.6 Conserved Charges and Internal Symmetries#^thm-c1b-6-3|§C1b.6.3]] The U(1) Current of the Complex Scalar Field. *Source: Lecture 3 (Sep 9), slide "Example 2: Charge Conservation" ("Check current conservation using equation of motion: HW") and transcript ("you can show … use the massive [Klein–Gordon] equation … it happens to cancel") · the user's notes Ch. 3 §3.5 ("This verification is a homework problem") · **[class exercise, Lecture 3]**: PS2 asks only for the current, not the check*

^nd-thm-c1b-6-3

- [ ] Q1 **[state]** State the current, its charge, and the sign of $j^0$ on a positive-frequency solution.
- [ ] Q2 **[class exercise, Lecture 3]** Compute $\partial_\mu j^\mu$ for an arbitrary configuration by the product rule. Which two terms cancel without any equation of motion?
- [ ] Q3 **[class exercise, Lecture 3]** Insert the field equations with mass and potential, $\partial^2\phi = \,?$ and $\partial^2\phi^\ast = \,?$. Show that the remaining terms cancel, and say why $V$ does not spoil it.
- [ ] Q4 Compare with the off-shell identity of Noether's theorem: which Euler–Lagrange expressions multiply $\Delta\phi$ and $\Delta\phi^\ast$?
- [ ] Q5 Evaluate $j^0$ on $\phi = Ae^{-iEt + i\mathbf p\cdot\mathbf x}$, $E > 0$.
- [ ] Q6 **[conv]** The Lecture 3 slide prints $j^\mu = -i((\partial^\mu\phi^\ast)\phi - (\partial^\mu\phi)\phi^\ast)$. Compare with the slide's own first line and with PS (2.16); what quantum charge does the course use, $\hat Q = \,?$, and how is it related to $\int:\!\hat j^0\!:$?
- (Finding the current itself → drilled as [[PHY 513 PS Drill#^ps2-3-d|PS2.3(d)]].)

> [!tip]- Hints: route in the notes
> - Technique: K12
> - Derivation of Theorem [[§C1b.6 Conserved Charges and Internal Symmetries#^thm-c1b-6-3|§C1b.6.3]] The U(1) Current of the Complex Scalar Field, steps 5–6; [[§C1b.6 Conserved Charges and Internal Symmetries#^cau-c1b-6-3|§C1b.6, Caution: Sign and normalization of the U(1) current]]; register row "Complex-field charge"; the quantum charge Definition [[§C2a.5 The Complex Scalar Field and Its Charge#^def-c2a-5-1|§C2a.5.1]] The U(1) Charge Operator.

### Two real fields: one rotation or two shifts ★
For two real fields of equal mass the rotation gives one current $\phi_1\partial^\mu\phi_2 - \phi_2\partial^\mu\phi_1$, equal to the U(1) current; for $m = 0$ two shifts give two more, see Example [[§C1b.6 Conserved Charges and Internal Symmetries#^ex-c1b-6-2|§C1b.6.2]] Two Real Fields: One Rotation or Two Shifts. *Source: the user's notes Ch. 3 §3.5*

^nd-ex-c1b-6-2

- [ ] Q1 **[state]** State the currents of the rotation and of the two shifts.
- [ ] Q2 Show the rotation leaves the kinetic and mass terms invariant to first order.
- [ ] Q3 Build the rotation current: one current from two fields.
- [ ] Q4 **[why]** How many conserved currents are there for $m = 0$ and for $m \ne 0$? What counts the currents, fields or parameters?

> [!tip]- Hints: route in the notes
> - Technique: K12
> - Example [[§C1b.6 Conserved Charges and Internal Symmetries#^ex-c1b-6-2|§C1b.6.2]] Two Real Fields: One Rotation or Two Shifts (a)–(b); [[§C1b.5 Noether's Theorem#^rem-c1b-5-7|§C1b.5, Remark: Several fields, several parameters]].

### A mass splitting breaks the phase symmetry ★
Adding $-\frac\lambda2(\phi^2 + \phi^{\ast2})$ splits the masses, $m_{1,2}^2 = m^2 \pm \lambda$; $\delta\mathcal L = -i\alpha\lambda(\phi^2 - \phi^{\ast2})$ is not a divergence, and $\partial_\mu j^\mu = 2\lambda\phi_1\phi_2$ on shell, see Example [[§C1b.6 Conserved Charges and Internal Symmetries#^ex-c1b-6-3|§C1b.6.3]] A Mass Splitting Breaks the Phase Symmetry. *Source: written in the vault as an illustration of Theorem [[§C1b.5 Noether's Theorem#^thm-c1b-5-5|§C1b.5.5]] The Divergence of the Current When the Test Fails*

^nd-ex-c1b-6-3

- [ ] Q1 **[state]** State $\delta\mathcal L$, the outcome of the test, and the divergence of the would-be current.
- [ ] Q2 Rewrite the extra term in real components: what does it do to the masses?
- [ ] Q3 Compute $\delta\mathcal L$ by route 1 and by route 2.
- [ ] Q4 Why is $X = 2\lambda\phi_1\phi_2$ not a divergence?
- [ ] Q5 Cross-check $\partial_\mu j^\mu$ directly from the field equations.
- [ ] Q6 **[why]** What happens to the number charge, and why do symmetry and conservation return together at $\lambda = 0$?

> [!tip]- Hints: route in the notes
> - Technique: K12
> - Example [[§C1b.6 Conserved Charges and Internal Symmetries#^ex-c1b-6-3|§C1b.6.3]] A Mass Splitting Breaks the Phase Symmetry, items 1–7.

### Total and fixed-argument variations ★
$\bar\delta\phi = \delta\phi - (\partial_\mu\phi)\delta x^\mu$; $\bar\delta$ commutes with $\partial_\mu$, while $\delta(\partial_\mu\phi) = \partial_\mu(\delta\phi) - (\partial_\nu\phi)\partial_\mu(\delta x^\nu)$, see Theorem [[§C1b.7 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-7-1|§C1b.7.1]] Total and Fixed-Argument Variations. *Source: Yu §1.7.1 · the user's notes Ch. 3 §3.5*

^nd-thm-c1b-7-1

- [ ] Q1 **[state]** State the three relations.
- [ ] Q2 Insert and subtract $\phi'(x)$; Taylor expand; drop a second-order term. Which one?
- [ ] Q3 Show $\bar\delta$ commutes with $\partial_\mu$.
- [ ] Q4 Derive the total change of $\partial_\mu\phi$. When does $\delta$ commute with $\partial_\mu$?
- [ ] Q5 **[why]** Why does Noether's proof for Lorentz transformations need $\bar\delta$ rather than $\delta$?

> [!tip]- Hints: route in the notes
> - Derivation of Theorem [[§C1b.7 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-7-1|§C1b.7.1]] Total and Fixed-Argument Variations, steps 1–7.

### The volume element to first order ★
$d^4x' = [1 + \partial_\mu(\delta x^\mu)]d^4x$; the correction vanishes for translations and Lorentz transformations, see Theorem [[§C1b.7 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-7-2|§C1b.7.2]] The Volume Element to First Order. *Source: Yu §1.7.1*

^nd-thm-c1b-7-2

- [ ] Q1 **[state]** State the result.
- [ ] Q2 Write the Jacobian as $\det(1 + A)$ and expand to first order. Why does only the identity permutation contribute?
- [ ] Q3 Show $\partial_\mu(\omega^\mu{}_\nu x^\nu) = 0$. Which property of $\omega$ is used?
- [ ] Q4 **[why]** What is the correction for a scale transformation $\delta x^\mu = -\alpha x^\mu$?

> [!tip]- Hints: route in the notes
> - Derivation of Theorem [[§C1b.7 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-7-2|§C1b.7.2]] The Volume Element to First Order, steps 1–4; [[§C1b.8 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^rem-c1b-8-4|§C1b.8, ★ Remark: Dilatations]] for Q4.

### Noether's theorem, general form ★
If the point-moving transformation is a symmetry, $j^\mu = \sum_a\frac{\partial\mathcal L}{\partial(\partial_\mu\phi_a)}\bar\delta\phi_a + \mathcal L\,\delta x^\mu$ is conserved on shell, see Theorem [[§C1b.7 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-7-3|§C1b.7.3]] Noether's Theorem, General Form. *Source: Yu §1.7.1 · the user's notes Ch. 3 §3.5*

^nd-thm-c1b-7-3

- [ ] Q1 **[state]** State the general current and its off-shell identity.
- [ ] Q2 Change variables in the transformed action and expand with the Jacobian.
- [ ] Q3 Convert the total change of $\mathcal L$ to the fixed-argument change.
- [ ] Q4 Apply the chain and product rules to $\bar\delta\mathcal L$ and assemble the divergence.
- [ ] Q5 **[why]** Why does "$\delta S = 0$ for every region" localize to a pointwise identity?

> [!tip]- Hints: route in the notes
> - Technique: K12
> - Derivation of Theorem [[§C1b.7 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-7-3|§C1b.7.3]] Noether's Theorem, General Form, steps 1–8.

### Translation invariance conserves the energy–momentum tensor ★★
If $\mathcal L$ depends on $x$ only through the fields, translations are a symmetry with $\mathcal J^\mu{}_\nu = \delta^\mu{}_\nu\mathcal L$, the currents are $T^\mu{}_\nu$, and $\partial_\mu T^{\mu\nu} = 0$ on shell, see Theorem [[§C1b.7 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-7-5|§C1b.7.5]] Translation Invariance Conserves the Energy–Momentum Tensor. *Source: Lecture 3 (Sep 9), slide "Example 3: Spacetime Translation" (in the transcript: "the last example that I didn't get to" — left to the slides) · the user's notes Ch. 3 §3.5 · PS §2.2 p. 19*

^nd-thm-c1b-7-5

- [ ] Q1 **[state]** State $\mathcal J^\mu{}_\nu$, the currents, and the off-shell identity.
- [ ] Q2 With $\Delta_\nu\phi_a = \partial_\nu\phi_a$, compute $\delta\mathcal L$ by the chain rule. Recognize it as $a^\nu\partial_\nu\mathcal L$: which hypothesis is used?
- [ ] Q3 Write $a^\nu\partial_\nu\mathcal L$ as a divergence and factor the parameter by inserting $\delta^\mu{}_\nu$. Why is that legitimate?
- [ ] Q4 Build the current and identify $T^\mu{}_\nu$.
- [ ] Q5 **[why]** Lecture 3: "New feature: L is invariant only up to a total derivative." What false conclusion follows if $\mathcal J$ is forgotten?
- [ ] Q6 **[why]** Why is a theory with an external source $J(x)\phi$ not translation invariant?

> [!tip]- Hints: route in the notes
> - Technique: K12
> - Derivation of Theorem [[§C1b.7 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-7-5|§C1b.7.5]] Translation Invariance Conserves the Energy–Momentum Tensor, steps 1–7; [[§C1b.8 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^rem-c1b-8-2|§C1b.8, Remark: Index moves for the electromagnetic tensor]], item 1; [[§C1b.5 Noether's Theorem#^rem-c1b-5-10|§C1b.5, Remark: The three outcomes of the test and their currents]].

### Energy and momentum of a field ★★
$P^\nu = \int d^3x\,T^{0\nu}$; $T^{00} = \sum\pi_a\dot\phi_a - \mathcal L = \mathcal H$, $H = P^0$, $T^{0i} = \sum\pi_a\partial^i\phi_a$, $\mathbf P = -\int d^3x\sum\pi_a\nabla\phi_a$, see Theorem [[§C1b.7 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-7-6|§C1b.7.6]] Energy and Momentum of a Field. *Source: Lecture 3 (Sep 9), slide "Energy Density" · the user's notes Ch. 3 §3.5 · PS (2.18)–(2.19)*

^nd-thm-c1b-7-6

- [ ] Q1 **[state]** State $T^{00}$, $T^{0i}$, $H$ and $\mathbf P$ in terms of $\pi$.
- [ ] Q2 Identify $\partial\mathcal L/\partial(\partial_0\phi_a)$ with $\pi_a$.
- [ ] Q3 Compute $T^{00}$ and recognize the Legendre transform.
- [ ] Q4 Compute $T^{0i}$. Where does the minus sign in $\mathbf P$ come from?
- [ ] Q5 **[why]** Why is the momentum of the field not $\int\pi$?

> [!tip]- Hints: route in the notes
> - Technique: K2
> - Derivation of Theorem [[§C1b.7 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-7-6|§C1b.7.6]] Energy and Momentum of a Field, steps 1–4; [[§C1b.4 Hamiltonian Field Theory#^cau-c1b-4-1|§C1b.4, Caution: What the conjugate momentum is not]]; [[§C1b.7 Spacetime Symmetries꞉ Energy and Momentum#^rem-c1b-7-2|§C1b.7, Remark: Why P is the momentum]].

### The real scalar field's energy–momentum tensor ★★
$T^{\mu\nu} = \partial^\mu\phi\,\partial^\nu\phi - g^{\mu\nu}\mathcal L$, symmetric; $T^{00} = \frac12\dot\phi^2 + \frac12(\nabla\phi)^2 + \frac12m^2\phi^2 = \mathcal H$; $\partial_\mu T^{\mu\nu} = (\partial^2 + m^2)\phi\,\partial^\nu\phi$, see Example [[§C1b.7 Spacetime Symmetries꞉ Energy and Momentum#^ex-c1b-7-1|§C1b.7.1]] The Real Scalar Field's Energy–Momentum Tensor. *Source: Lecture 3 (Sep 9), slides "Example 3: Spacetime Translation", "Energy Density" · the user's notes Ch. 3 §3.5*

^nd-ex-c1b-7-1

- [ ] Q1 **[state]** State $T^\mu{}_\nu$, $T^{\mu\nu}$, $T^{00}$ and $T^{0i}$.
- [ ] Q2 Raise the index $\nu$ with the metric. Why is the result symmetric?
- [ ] Q3 Compute $T^0{}_0$ as on the Lecture 3 slide. Why is it equal to $T^{00}$ here?
- [ ] Q4 Check conservation directly: which second-derivative terms cancel, and what is left?
- [ ] Q5 **[why]** Lecture 3: "This is energy density and closely related to the Hamiltonian." Is it equal, and why?

> [!tip]- Hints: route in the notes
> - Technique: K2, K12
> - Example [[§C1b.7 Spacetime Symmetries꞉ Energy and Momentum#^ex-c1b-7-1|§C1b.7.1]] The Real Scalar Field's Energy–Momentum Tensor, items 1–5; Theorem [[§C1b.4 Hamiltonian Field Theory#^thm-c1b-4-2|§C1b.4.2]] Hamiltonian Density of the Free Real Field.

### Energy and momentum of the free real scalar field ★
$H = \int d^3x[\frac12\pi^2 + \frac12(\nabla\phi)^2 + \frac12m^2\phi^2]$, $\mathbf P = -\int d^3x\,\pi\nabla\phi$, together $P^\mu$, conserved for fields falling off at infinity, see Theorem [[§C1b.7 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-7-7|§C1b.7.7]] Energy and Momentum of the Free Real Scalar Field. *Source: Lecture 3 (Sep 9), slide "Energy Density" · the user's notes Ch. 3 §3.5 · PS (2.17)–(2.19)*

^nd-thm-c1b-7-7

- [ ] Q1 **[state]** State $H$ and $\mathbf P$.
- [ ] Q2 Compute $T^{0i}$ index by index. Why does the $\mathcal L$ term drop, and what is $\partial^i$?
- [ ] Q3 Show conservation of $P^\nu$ from $\partial_\mu T^{\mu\nu} = 0$ and the fall-off.
- [ ] Q4 **[why]** On a real plane wave, show that the averaged momentum density points along $\mathbf k$.

> [!tip]- Hints: route in the notes
> - Derivation of Theorem [[§C1b.7 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-7-7|§C1b.7.7]] Energy and Momentum of the Free Real Scalar Field, steps 1–7; [[§C1b.7 Spacetime Symmetries꞉ Energy and Momentum#^rem-c1b-7-2|§C1b.7, Remark: Why P is the momentum]].

### Energy and momentum of the free complex scalar field ★
$H = \int d^3x(\pi^\ast\pi + \nabla\phi^\ast\cdot\nabla\phi + m^2\phi^\ast\phi)$, $\mathbf P = -\int d^3x(\pi\nabla\phi + \pi^\ast\nabla\phi^\ast)$, one term per canonical pair, real, and the sum of the two real momenta, see Theorem [[§C1b.7 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-7-8|§C1b.7.8]] Energy and Momentum of the Free Complex Scalar Field. *Source: the user's notes Ch. 3 §3.4–3.5*

^nd-thm-c1b-7-8

- [ ] Q1 **[state]** State $H$ and $\mathbf P$.
- [ ] Q2 Compute $T^{\mu\nu}$ summed over $\phi$ and $\phi^\ast$.
- [ ] Q3 Show $\mathbf P$ is real.
- [ ] Q4 Rewrite $\mathbf P$ in the real components.
- [ ] Q5 **[why]** Which momentum is conjugate to $\phi$, and why does that make $\pi\nabla\phi$ contain $\dot\phi^\ast$?

> [!tip]- Hints: route in the notes
> - Derivation of Theorem [[§C1b.7 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-7-8|§C1b.7.8]] Energy and Momentum of the Free Complex Scalar Field, steps 1–7.

### The field momentum generates spatial translations ★
$\{\phi_a(\mathbf x), \mathbf P\} = -\nabla\phi_a$, $\{\pi_a, \mathbf P\} = -\nabla\pi_a$, covariantly $\{\phi_a, P^\mu\} = \partial^\mu\phi_a$; $a_\mu P^\mu$ generates $\phi(x) \to \phi(x + \varepsilon a)$; $\{\mathbf P, H\} = 0$, see Theorem [[§C1b.7 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-7-9|§C1b.7.9]] The Field Momentum Generates Spatial Translations. *Source: the user's notes Ch. 3 §§3.4–3.5 · CM analogue*

^nd-thm-c1b-7-9

- [ ] Q1 **[state]** State the four parts.
- [ ] Q2 Compute $\delta P^i/\delta\pi_c$ and $\delta P^i/\delta\phi_c$. Which step needs an integration by parts?
- [ ] Q3 Evaluate $\{\phi_a(f), P^i\}$ with the smeared field.
- [ ] Q4 Raise the index and combine with $\{\phi, H\} = \dot\phi$ for the covariant form.
- [ ] Q5 **[why]** Why is $\{\mathbf P, H\} = 0$ exactly when $\mathcal H$ has no explicit $\mathbf x$ dependence?

> [!tip]- Hints: route in the notes
> - Derivation of Theorem [[§C1b.7 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-7-9|§C1b.7.9]] The Field Momentum Generates Spatial Translations, steps 1–7.

### The Lorentz current ★
Under $\Lambda = 1 + \omega$ the current is $\frac12\omega_{\nu\rho}\mathcal M^{\mu\nu\rho}$ with $\mathcal M^{\mu\nu\rho} = x^\nu T^{\mu\rho} - x^\rho T^{\mu\nu} + \mathcal S^{\mu\nu\rho}$, $\mathcal S^{\mu\nu\rho} = \sum_a\frac{\partial\mathcal L}{\partial(\partial_\mu\phi_a)}(S^{\nu\rho})_a{}^b\phi_b$: six conserved currents, see Theorem [[§C1b.8 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^thm-c1b-8-1|§C1b.8.1]] The Lorentz Current. *Source: the user's notes Ch. 3 §3.5 (Example 4) · Yu §1.7.3*

^nd-thm-c1b-8-1

- [ ] Q1 **[state]** State $\mathcal M^{\mu\nu\rho}$ with its orbital and spin parts.
- [ ] Q2 Write $\delta x^\mu$, the total change and the fixed-argument change of $\phi_a$.
- [ ] Q3 Insert into the general current; move the metric in $T^\mu{}_\sigma\omega^\sigma{}_\rho$.
- [ ] Q4 Antisymmetrize in $\nu\rho$ and read off $\mathcal M$.
- [ ] Q5 Choose one $\omega_{\nu\rho}$ at a time: why six currents?
- [ ] Q6 **[why]** Why is $\mathcal M$ purely orbital for a scalar field?

> [!tip]- Hints: route in the notes
> - Technique: K12, K2
> - Derivation of Theorem [[§C1b.8 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^thm-c1b-8-1|§C1b.8.1]] The Lorentz Current, steps 1–9; the general form Theorem [[§C1b.7 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-7-3|§C1b.7.3]] Noether's Theorem, General Form.

### The antisymmetric part of T is a divergence ★
On shell $T^{\nu\rho} - T^{\rho\nu} = -\partial_\mu\mathcal S^{\mu\nu\rho}$; the orbital current is conserved alone iff $T$ is symmetric, see Theorem [[§C1b.8 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^thm-c1b-8-2|§C1b.8.2]] The Antisymmetric Part of T Is a Divergence. *Source: the user's notes Ch. 3 §3.5 ("Conservation is easy to check and instructive") · Yu Exercise 1.10(a)*

^nd-thm-c1b-8-2

- [ ] Q1 **[state]** State the identity and its consequence for the orbital current.
- [ ] Q2 Compute $\partial_\mu(x^\nu T^{\mu\rho})$ on shell.
- [ ] Q3 Combine with conservation of $\mathcal M$.
- [ ] Q4 **[why]** Why is the canonical $T$ of a scalar symmetric, and why need it not be for fields with spin?

> [!tip]- Hints: route in the notes
> - Technique: K2
> - Derivation of Theorem [[§C1b.8 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^thm-c1b-8-2|§C1b.8.2]] The Antisymmetric Part of T Is a Divergence, steps 1–4.

### Angular momentum and boost charges of the scalar field ★
$\mathbf J = \int d^3x\,\mathbf x\times\boldsymbol{\mathcal P}$ with $\boldsymbol{\mathcal P} = -\pi\nabla\phi$, all orbital; $K^i = \int d^3x\,x^i\mathcal H - tP^i$, see Example [[§C1b.8 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^ex-c1b-8-1|§C1b.8.1]] Angular Momentum and Boost Charges of the Scalar Field. *Source: the user's notes Ch. 3 §3.5 · Yu §1.7.3*

^nd-ex-c1b-8-1

- [ ] Q1 **[state]** State $\mathbf J$ and $K^i$ for the real scalar.
- [ ] Q2 From $J^{jk}$, compute $J^i = \frac12\varepsilon_{ijk}J^{jk}$. Why are the two halves equal?
- [ ] Q3 Compute $K^i = J^{i0}$. Why does $x^0 = t$ come out of the integral?
- [ ] Q4 **[why]** In what sense is $K^i$ conserved although it depends explicitly on $t$?

> [!tip]- Hints: route in the notes
> - Technique: K2
> - Example [[§C1b.8 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^ex-c1b-8-1|§C1b.8.1]] Angular Momentum and Boost Charges of the Scalar Field; [[§C1b.8 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^rem-c1b-8-1|§C1b.8, Remark: What the boost charges are]].

### The centre of energy moves uniformly ★
For a scalar with $T^{\mu\nu}$ falling off faster than $1/r^3$, $P^i = H\,dX^i_E/dt$ with $X^i_E = \frac1H\int x^i\mathcal H$, see Theorem [[§C1b.8 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^thm-c1b-8-3|§C1b.8.3]] The Centre of Energy Moves Uniformly. *Source: the user's notes Ch. 3 §3.5 · Yu (1.249)–(1.252)*

^nd-thm-c1b-8-3

- [ ] Q1 **[state]** State the theorem.
- [ ] Q2 Why does conservation of $K^i$ need a faster fall-off than conservation of $P^i$?
- [ ] Q3 Differentiate $K^i$ in time and use conservation of $H$ and $P^i$.
- [ ] Q4 **[why]** What does the theorem become for slow matter?

> [!tip]- Hints: route in the notes
> - Derivation of Theorem [[§C1b.8 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^thm-c1b-8-3|§C1b.8.3]] The Centre of Energy Moves Uniformly, steps 1–4.

### The Belinfante tensor ★
$K^{\lambda\mu\nu} = \frac12(\mathcal S^{\lambda\mu\nu} + \mathcal S^{\mu\nu\lambda} + \mathcal S^{\nu\mu\lambda})$ is antisymmetric in $\lambda\mu$, and $T_B = T + \partial_\lambda K^{\lambda\mu\nu}$ is symmetric, conserved, has the same $P^\nu$, and its orbital current carries the total $J$, see Theorem [[§C1b.8 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^thm-c1b-8-4|§C1b.8.4]] The Belinfante Tensor. *Source: the user's notes Ch. 3 §3.5 · Yu Exercise 1.10*

^nd-thm-c1b-8-4

- [ ] Q1 **[state]** State the four properties.
- [ ] Q2 Show $K^{\mu\lambda\nu} = -K^{\lambda\mu\nu}$.
- [ ] Q3 Show the antisymmetric part of $K$ in its last two indices is $\mathcal S$, and deduce $T_B^{\mu\nu} = T_B^{\nu\mu}$.
- [ ] Q4 Why are conservation and $P^\nu$ unchanged? Which earlier theorem is used?
- [ ] Q5 **[conv]** The notes write $T_B$; PS2, PS and the user's notes write $\hat T$; Yu writes $\Theta$. Why does the vault avoid the hat?

> [!tip]- Hints: route in the notes
> - Technique: K2
> - Derivation of Theorem [[§C1b.8 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^thm-c1b-8-4|§C1b.8.4]] The Belinfante Tensor, steps 1–7; Theorem [[§C1b.6 Conserved Charges and Internal Symmetries#^thm-c1b-6-2|§C1b.6.2]] Improvement Terms; [[§C1b.8 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^cau-c1b-8-1|§C1b.8, Caution: Notation in Yu and in the conventions table]].

### The electromagnetic energy–momentum tensor
Canonical $T^{\mu\nu} = -F^{\mu\lambda}\partial^\nu A_\lambda + \frac14g^{\mu\nu}F^2$; with $K^{\lambda\mu\nu} = F^{\mu\lambda}A^\nu$, $T_B^{\mu\nu} = -F^{\mu\lambda}F^\nu{}_\lambda + \frac14g^{\mu\nu}F^2$, $T_B^{00} = \frac12(\mathbf E^2 + \mathbf B^2)$, $T_B^{0i} = (\mathbf E\times\mathbf B)^i$, see Example [[§C1b.8 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^ex-c1b-8-2|§C1b.8.2]] The Electromagnetic Field. *Source: PS2 Problem 4(c)–(e)*

^nd-ex-c1b-8-2

→ drilled as [[PHY 513 PS Drill#^ps2-4-c|PS2.4(c)]], [[PHY 513 PS Drill#^ps2-4-d|PS2.4(d)]] and [[PHY 513 PS Drill#^ps2-4-e|PS2.4(e)]]

### Dilatations ★
**[exercise in the user's notes, Ch. 3]** "Scale transformation (not a symmetry when $m \ne 0$, but a good exercise)." With $\Delta\phi = \phi + x^\mu\partial_\mu\phi$, $\delta\mathcal L = \alpha\partial_\nu(x^\nu\mathcal L) + \alpha m^2\phi^2$: for $m = 0$ a symmetry with $\mathcal J^\mu = x^\mu\mathcal L$ and current $x_\nu T^{\mu\nu} + \phi\partial^\mu\phi$; for $m \ne 0$ broken by the mass, see [[§C1b.8 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^rem-c1b-8-4|§C1b.8, ★ Remark: Dilatations]]. *Source: the user's notes Ch. 3 §3.5 (the exercise is the user's notes', not Larsen's)*

^nd-rem-c1b-8-4

- [ ] Q1 **[state]** State the generator, $\delta\mathcal L$, and the outcome of the test for $m = 0$ and $m \ne 0$.
- [ ] Q2 Derive the generator from $\phi'(x) = \lambda\phi(\lambda x)$ with $\lambda = e^\alpha$. Why the prefactor $\lambda^{[\phi]}$?
- [ ] Q3 Compute the change of the kinetic term and write it as $\alpha\partial_\nu(x^\nu\mathcal L_{\rm kin})$. Where does $\partial_\nu x^\nu = 4$ enter?
- [ ] Q4 Compute the change of the mass term. What is left over?
- [ ] Q5 Build the dilatation current for $m = 0$.
- [ ] Q6 **[why]** Why does a dimensionful parameter break scale invariance?

> [!tip]- Hints: route in the notes
> - Technique: K12, K8
> - [[§C1b.8 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^rem-c1b-8-4|§C1b.8, ★ Remark: Dilatations]]; Theorem [[§C1b.5 Noether's Theorem#^thm-c1b-5-1|§C1b.5.1]] Generators of the Standard Transformations (scale row); the not-a-divergence argument of Example [[§C1b.6 Conserved Charges and Internal Symmetries#^ex-c1b-6-1|§C1b.6.1]] Shift Symmetry of the Massless Field.

# T5. Canonical quantization of the scalar: modes, H, P, Q, states

## Definitions and conventions T5

### Notation: E_p and π, hats on operators

The course slides write $\omega_{\mathbf p}$ and $\Pi$; the vault writes $E_{\mathbf p} = +\sqrt{\mathbf p^2 + m^2}$ and $\pi$, and puts a hat on every operator on the Fock space, none on c-numbers, see [[§C2a.1 Canonical Quantization of Fields#^cau-c2a-1-1|§C2a.1, Caution: Eₚ, not ωₚ; π, not Π]]. *Source: Lectures 4–5 · Problem Set 3 · PS §2.3, p. 22 · the user's notes, Concordance*

^nd-cau-c2a-1-1

- [ ] Q1 **[def]** Define $E_{\mathbf p}$, including the sign of the square root. What does each source (slides, PS, Yu, the user's notes) call it?
- [ ] Q2 **[def]** Which objects carry a hat in the vault, and which do not? Classify $\hat\phi$, $u^s(p)$, $D_W$, $U(\Lambda)$, $\hat a^\dagger_{\mathbf p}$, $\gamma^\mu$.
- [ ] Q3 **[why]** Why is the frequency of mode $\mathbf p$ written as an energy and not as $\omega$? Which later theorem justifies the name?
- [ ] Q4 **[conv]** What does $u^{s\dagger}(p)$ denote, and what does $\hat a^{s\dagger}_{\mathbf p}$ denote? How do the hats keep the dagger unambiguous?

> [!tip]- Hints: route in the notes
> - Technique: none (notation).
> - Step 1: the caution box itself; register row "Energy" and "Operators" in the conventions register.
> - Step 2: the frequency is the particle energy by Theorem [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-1|§C2a.4.1]] The Spectrum: Particles.

### The free real scalar quantum field

A Hermitian field $\hat\phi(\mathbf x)$ and momentum density $\hat\pi(\mathbf x)$ obeying the equal-time relations, with $\hat H = \int d^3x\,[\frac12\hat\pi^2 + \frac12(\nabla\hat\phi)^2 + \frac12m^2\hat\phi^2]$ and $\hat{\mathbf P} = -\int d^3x\,\hat\pi\nabla\hat\phi$, see Model [[§C2a.1 Canonical Quantization of Fields#^mod-c2a-1-1|§C2a.1.1]] The Free Real Scalar Quantum Field. *Source: Lecture 4 (Sep 14), slide "Physical Content" · PS §2.3, eqs. (2.31)–(2.33) · the user's notes Ch. 4 §4.2*

^nd-mod-c2a-1-1

- [ ] Q1 **[def]** Write the Lagrangian density this model quantizes, and the classical momentum density conjugate to $\phi$.
- [ ] Q2 **[def]** Write $\hat H$ and $\hat{\mathbf P}$ in field form, with every factor and sign.
- [ ] Q3 **[why]** The classical relation $\pi = \dot\phi$ is used once. Where, and why does it not define $\hat\pi$ after quantization (Schrödinger picture)?
- [ ] Q4 **[conv]** Derive the sign in $\mathbf P = -\int\pi\nabla\phi$ from $P^i = \int d^3x\,T^{0i}$ with $T^{0i} = \dot\phi\,\partial^i\phi$. Where does the minus sign come from?
- [ ] Q5 **[why]** Which ordering issue does the model leave open for $\hat H$, and why does $\hat{\mathbf P}$ need no ordering choice?

> [!tip]- Hints: route in the notes
> - Technique: K2 (index calculus) for the sign of $\mathbf P$.
> - Step 1: the classical boxes recalled in [[§C2a.1 Canonical Quantization of Fields|§C2a.1]] Canonical Quantization of Fields: Definition [[§C1b.4 Hamiltonian Field Theory#^def-c1b-4-1|§C1b.4.1]] Canonical Momentum Density, Theorem [[§C1b.4 Hamiltonian Field Theory#^thm-c1b-4-2|§C1b.4.2]] Hamiltonian Density of the Free Real Field, Theorem [[§C1b.7 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-7-7|§C1b.7.7]] Energy and Momentum of the Free Real Scalar Field.
> - Step 2: ordering of $\hat H$ fixed later by Definition [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^def-c2a-3-1|§C2a.3.1]] Normal Ordering; $\hat{\mathbf P}$ by Theorem [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-5|§C2a.3.5]] Momentum in Mode Form.
> - Step 3: "a momentum with no time in sight": [[§C2a.1 Canonical Quantization of Fields#^rem-c2a-1-3|§C2a.1, Remark: A momentum with no time in sight]].

### Equal-time canonical commutation relations

$[\hat\phi_a(\mathbf x), \hat\pi_b(\mathbf y)] = i\delta_{ab}\delta^3(\mathbf x - \mathbf y)$, all other equal-time commutators zero, with $\hat H = H[\hat\phi, \hat\pi]$, see Principle [[§C2a.1 Canonical Quantization of Fields#^pr-c2a-1-2|§C2a.1.2]] Equal-Time Canonical Commutation Relations. *Source: Lecture 4 (Sep 14), slide "Quantization of Scalar Field" · PS §2.3, eq. (2.20) · Yu eq. (2.76) · the user's notes Ch. 4 §4.2*

^nd-pr-c2a-1-2

- [ ] Q1 **[state]** State the principle for a set of real bosonic fields: all three relations, and what happens to the Hamiltonian.
- [ ] Q2 **[why]** Why a delta function and not a Kronecker delta? Rebuild it from cells of volume $V_i$ with $\Pi_i = V_i\pi$.
- [ ] Q3 Check the mass dimensions: $[\hat\phi]$, $[\hat\pi]$, and the dimension of both sides.
- [ ] Q4 **[why]** Why only at equal times? What is assumed about $[\hat\phi(t, \mathbf x), \hat\phi(t', \mathbf y)]$ for $t \neq t'$, and where is it computed later?
- [ ] Q5 **[why]** What replaces commutators for fermion fields, and which box says so?

> [!tip]- Hints: route in the notes
> - Technique: none (postulate).
> - Step 1: [[§C2a.1 Canonical Quantization of Fields#^rem-c2a-1-2|§C2a.1, Remark: Why a delta function, and not a Kronecker delta]] for the cells.
> - Step 2: [[§C2b.1 Heisenberg Fields#^cau-c2b-1-1|§C2b.1, Caution: Equal times only]]; unequal times are Theorem [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-10|§C2b.4.10]] Commutators at Unequal Times.
> - Step 3: fermions, Principle [[§C5b.1 Canonical Quantization of the Dirac Field#^pr-c5b-1-6|§C5b.1.6]] Equal-Time Canonical Anticommutation Relations.

### The oscillator in natural units [class exercise, Lecture 4]

With $\hat x = (\hat a + \hat a^\dagger)/\sqrt{2m\omega}$, $\hat p = -i\sqrt{m\omega/2}\,(\hat a - \hat a^\dagger)$: $[\hat x, \hat p] = i \iff [\hat a, \hat a^\dagger] = 1$, and $\hat H = \omega(\hat a^\dagger\hat a + \frac12)$, see [[§C2a.1 Canonical Quantization of Fields#^rem-c2a-1-1|§C2a.1, Remark: The oscillator, recalled in natural units]]. Larsen in class: one should be "a little more careful to check that that number really is one". *Source: Lecture 4 (Sep 14), slides "Example: Simple Harmonic Oscillator", "Spectrum of Simple Harmonic Oscillator"; transcript · PS §2.3, eqs. (2.23)–(2.24)*

^nd-rem-c2a-1-1

- [ ] Q1 **[def]** Write $\hat x$ and $\hat p$ in terms of $\hat a$, $\hat a^\dagger$ with all factors.
- [ ] Q2 Compute $[\hat x, \hat p]$ from $[\hat a, \hat a^\dagger] = 1$ and check that the number is exactly $i$.
- [ ] Q3 Compute $\hat H$ in terms of $\hat a$, $\hat a^\dagger$ without reordering; then reorder.
- [ ] Q4 **[why]** Squaring $\hat x$ and $\hat p$: why must the two orderings $\hat a\hat a^\dagger$ and $\hat a^\dagger\hat a$ add and not cancel? What would a sign slip there produce?
- [ ] Q5 Show $[\hat H, \hat a^\dagger] = \omega\hat a^\dagger$ and conclude that $\hat a^\dagger$ raises the energy by $\omega$.

> [!tip]- Hints: route in the notes
> - Technique: K11 (commutator algebra).
> - Step 1: the remark box itself, which links the oscillator's home in the Quantum Mechanics notes.
> - Step 2: the cross terms $\hat a^2$, $\hat a^{\dagger2}$ cancel between kinetic and potential terms.

### Smeared field operators

$\hat\phi(f) = \int d^3x\,f(\mathbf x)\hat\phi(\mathbf x)$, $\hat\pi(g)$ likewise, for real $f, g \in \mathcal S(\mathbb R^3)$: $\hat\phi$ and $\hat\pi$ are operator-valued distributions, and $\hat\phi(\mathbf x)$ is only their kernel, see Definition [[§C2a.1 Canonical Quantization of Fields#^def-c2a-1-1|§C2a.1.1]] Smeared Field Operators. *Source: the user's notes Ch. 4 §4.8 (Caution "Two honesty points"), App. A §A.4*

^nd-def-c2a-1-1

- [ ] Q1 **[def]** Define the smeared field and the smeared momentum density. Which space do the smearing functions belong to?
- [ ] Q2 **[def]** Define an operator-valued distribution (Definition [[§CA.2 Generalized Functions#^def-ca-2-11|§CA.2.11]] Operator-Valued Distribution).
- [ ] Q3 **[why]** Why is $\hat\phi(\mathbf x)$ itself not an operator? Name one quantity that has no value if it is read as one.

> [!tip]- Hints: route in the notes
> - Technique: none.
> - Step 1: Definition [[§CA.2 Generalized Functions#^def-ca-2-1|§CA.2.1]] Test Functions: the Spaces 𝒟 and 𝒮 for $\mathcal S$; Theorem [[§C2a.1 Canonical Quantization of Fields#^thm-c2a-1-3|§C2a.1.3]] The Canonical Relations Are Identities after Smearing for the smeared canonical relations; Theorem [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-7|§C2a.4.7]] The Smeared Field Creates a State; the Field at a Point Does Not for the norm of $\hat\phi(\mathbf x)|0\rangle$.

### Two bookkeeping rules for mode integrals

At fixed time, $\int d^3x\,e^{\mp i(p \pm q)\cdot x} = e^{\mp i(E_{\mathbf p} \pm E_{\mathbf q})t}(2\pi)^3\delta^3(\mathbf p \pm \mathbf q)$ (split exponentials), and $\mathbf p \to -\mathbf p$ may be substituted in one term of an integral over all $\mathbf p$ (relabel), see [[§C2a.2 Mode Expansion and the Mode Algebra#^rem-c2a-2-2|§C2a.2, Remark: Two bookkeeping rules for mode integrals]]. *Source: the user's notes Ch. 4 §4.3 ("Tools, recalled") · Lecture 4 (Sep 14), board ("change my integration variable from p to minus p")*

^nd-rem-c2a-2-2

- [ ] Q1 **[state]** State both rules exactly, including which factor the $d^3x$ integral acts on.
- [ ] Q2 After the delta function of the split rule is used, what phase is left in a $p + q$ term and in a $p - q$ term?
- [ ] Q3 **[why]** Why is the relabelling $\mathbf p \to -\mathbf p$ legitimate (Jacobian, domain, $E_{-\mathbf p}$)? What changes in the integrand and what does not?
- [ ] Q4 **[conv]** Why give the two integration variables of a product different names, and why keep the label $-\mathbf p$ on a creation operator until the delta has been used? What spurious object appears if a sign is dropped?

> [!tip]- Hints: route in the notes
> - Technique: K9 (mode substitution).
> - Step 1: Theorem [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|§CA.3.3]] Plane Waves Integrate to a Delta Function (plane waves give a delta, in $\mathcal S'$); Theorem [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-6|§CA.3.6]] Exchanging the Space and Momentum Integrals (exchange of integrals for wave packets); Theorem [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|§CA.3.7]] Changes of Integration Variable: Relabelling, Shifting, Rescaling, Rotating part 1 (relabel).
> - Step 2: P1, step 7 and its "Pitfalls" list.

### Klein–Gordon inner product and positive-frequency modes

$(f, g) = i\int d^3x\,(f^\ast\partial_tg - (\partial_tf^\ast)g)$ on any time slice; positive-frequency modes $f_{\mathbf p} = e^{-ip\cdot x}/\sqrt{2E_{\mathbf p}}$, $p^0 = E_{\mathbf p}$, see Definition [[§C2a.2 Mode Expansion and the Mode Algebra#^def-c2a-2-1|§C2a.2.1]] Klein–Gordon Inner Product. *Source: Problem Set 3, Problem 3 (eq. (9)) · the user's notes Ch. 4 §4.5*

^nd-def-c2a-2-1

- [ ] Q1 **[def]** Write the Klein–Gordon inner product. In which argument is it antilinear?
- [ ] Q2 **[def]** Define the positive-frequency modes and their conjugates. Which sign of the time exponent is "positive frequency"?
- [ ] Q3 **[why]** Why is this product indefinite? What sign does $(f^\ast_{\mathbf p}, f^\ast_{\mathbf q})$ have?
- [ ] Q4 **[why]** Of which conserved current is $(f, g)$ the charge, and why does that make it independent of the slice?

> [!tip]- Hints: route in the notes
> - Technique: K10 (extracting mode operators).
> - Step 1: Theorem [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-3|§C2a.2.3]] Conservation and Orthonormality of the Modes; [[§C2a.2 Mode Expansion and the Mode Algebra#^rem-c2a-2-4|§C2a.2, Remark: Why this inner product, and why it is indefinite]] (projection, Noether charge, indefiniteness).

### Smeared mode operators

$\hat a(g) = \int\frac{d^3p}{(2\pi)^3}\overline{g(\mathbf p)}\hat a_{\mathbf p}$, $\hat a^\dagger(g) = \hat a(g)^\dagger$, for $g \in \mathcal S(\mathbb R^3)$; $\hat a^\dagger(g)$ creates one quantum in the packet $g$, see Definition [[§C2a.2 Mode Expansion and the Mode Algebra#^def-c2a-2-2|§C2a.2.2]] Smeared Mode Operators. *Source: the user's notes Ch. 4 §4.8 (Caution "Two honesty points")*

^nd-def-c2a-2-2

- [ ] Q1 **[def]** Define $\hat a(g)$ and $\hat a^\dagger(g)$. Which one is linear in $g$?
- [ ] Q2 **[why]** Why is $\hat a_{\mathbf p}|\psi\rangle$ a vector for wave-packet states $|\psi\rangle$ while $\hat a^\dagger_{\mathbf p}|0\rangle$ is not?
- [ ] Q3 What is $[\hat a(g), \hat a^\dagger(h)]$? Of which identity is $(2\pi)^3\delta^3(\mathbf p - \mathbf q)$ the kernel?

> [!tip]- Hints: route in the notes
> - Technique: K11.
> - Step 1: Theorem [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-7|§C2a.2.7]] The Mode Algebra Smeared parts 1–2.

### The vacuum and the Fock space

There is a normalized $|0\rangle$, unique up to a phase, with $\hat a_{\mathbf p}|0\rangle = 0$ for all $\mathbf p$; the state space is the Fock space $\bigoplus_n\operatorname{Sym}^n\mathcal H_1$ it generates, with inner products from the mode algebra, see Principle [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^pr-c2a-3-3|§C2a.3.3]] The Vacuum and the Fock Space. *Source: Lecture 4 (Sep 14), slide "Spectrum, Ground State" · PS §2.3, p. 22 · the user's notes Ch. 4 §4.8*

^nd-pr-c2a-3-3

- [ ] Q1 **[def]** Define the vacuum and the Fock space, including the symmetrization of $\mathcal H_n$.
- [ ] Q2 Compute $\langle0|\hat a_{\mathbf q}\hat a^\dagger_{\mathbf p}|0\rangle$ by moving the annihilator to the right.
- [ ] Q3 **[why]** What is asserted rather than derived here (uniqueness, irreducibility)? What changes in an interacting theory?
- [ ] Q4 **[conv]** The slide defines "vacuum has no energy by definition". Which choice makes $\hat H|0\rangle = 0$ true?

> [!tip]- Hints: route in the notes
> - Technique: K11.
> - Step 1: the principle box; Definition [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^def-c2a-3-1|§C2a.3.1]] Normal Ordering; [[§C2a.4 Particles and Relativistic Normalization#^rem-c2a-4-2|§C2a.4, Remark: Why ¦0⟩ is the vacuum]] (why $|0\rangle$ is the vacuum).

### Normal ordering

$:\!\hat X\!:$ puts all creation operators to the left of all annihilation operators as if they commuted; $:\!\hat H\!: = \int\frac{d^3p}{(2\pi)^3}E_{\mathbf p}\hat a^\dagger_{\mathbf p}\hat a_{\mathbf p}$, $:\!\hat H\!:|0\rangle = 0$, see Definition [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^def-c2a-3-1|§C2a.3.1]] Normal Ordering. *Source: Lecture 4 (Sep 14), slide "Diagonalizing the Hamiltonian: Details" ("Ignore!") · Problem Set 3 (instructions to Problem 2) · Problem Set 6, Problem 1 · PS §2.3, after eq. (2.31)*

^nd-def-c2a-3-1

- [ ] Q1 **[def]** Define normal ordering, including the phrase "as if they commuted". Give $:\!\hat a_{\mathbf p}\hat a^\dagger_{\mathbf q}\!:$.
- [ ] Q2 **[def]** State Larsen's instruction from Problem Sets 3 and 6 about when the reordering is done.
- [ ] Q3 **[why]** Why is normal ordering a choice of quantization and not a subtraction done afterwards? What does the classical expression $\int E_{\mathbf p}a^\ast_{\mathbf p}a_{\mathbf p}$ say?
- [ ] Q4 **[conv]** How do PS and Yu write normal ordering? What notation does the vault use?
- [ ] Q5 **[why]** For which operator is dropping the ordering constant harmless, and for which is it required by physics?

> [!tip]- Hints: route in the notes
> - Technique: K11.
> - Step 1: [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^rem-c2a-3-2|§C2a.3, Remark: Normal ordering is a choice of quantization]] (a choice of quantization); [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^rem-c2a-3-1|§C2a.3, Remark: Why the zero-point energy is dropped]] (why the zero-point energy is dropped).
> - Step 2: the charge, [[§C2a.5 The Complex Scalar Field and Its Charge#^rem-c2a-5-2|§C2a.5, Remark: Why the vacuum must be neutral]] (why the vacuum must be neutral).

### Relativistic normalization of states

$|\mathbf p\rangle = \sqrt{2E_{\mathbf p}}\,\hat a^\dagger_{\mathbf p}|0\rangle$ with $\langle\mathbf p|\mathbf q\rangle = 2E_{\mathbf p}(2\pi)^3\delta^3(\mathbf p - \mathbf q)$; multiparticle states with one factor $\sqrt{2E}$ per particle, see Definition [[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-1|§C2a.4.1]] Relativistic Normalization. *Source: Lecture 4 (Sep 14), slide "Normalization of States" · PS §2.3, eqs. (2.35)–(2.36) · Yu eq. (2.152) · the user's notes Ch. 4 §4.9*

^nd-def-c2a-4-1

- [ ] Q1 **[def]** Define $|\mathbf p\rangle$ and state $\langle\mathbf p|\mathbf q\rangle$ with all factors.
- [ ] Q2 **[conv]** The Lecture 4 slide writes $\langle\mathbf p|\mathbf q\rangle$ with one factor missing. Which, and why is it required given $[\hat a_{\mathbf p}, \hat a^\dagger_{\mathbf q}] = (2\pi)^3\delta^3(\mathbf p - \mathbf q)$?
- [ ] Q3 **[why]** Why the factor $\sqrt{2E_{\mathbf p}}$: what becomes Lorentz invariant with it, and what is the price elsewhere?
- [ ] Q4 **[why]** Why is $|\mathbf p\rangle$ not a vector of the Fock space? What are the physical one-particle states?

> [!tip]- Hints: route in the notes
> - Technique: K14 (Lorentz-invariance argument).
> - Step 1: [[§C2a.4 Particles and Relativistic Normalization#^cau-c2a-4-2|§C2a.4, Caution: The slides' normalization drops the (2π)³]]; Theorem [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-4|§C2a.4.4]] Invariance of the Relativistic Normalization; [[§C2a.4 Particles and Relativistic Normalization#^rem-c2a-4-3|§C2a.4, Remark: Sharp momentum or sharp position; why √(2E_p)]].
> - Step 2: [[§C2a.4 Particles and Relativistic Normalization#^cau-c2a-4-1|§C2a.4, Caution: Plane-wave states are not normalizable]]; Definition [[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-3|§C2a.4.3]] One-Particle Wave Packet.

### Invariant measure and one-particle completeness

$\int\frac{d^3p}{(2\pi)^3\,2E_{\mathbf p}} = \int\frac{d^4p}{(2\pi)^4}2\pi\delta(p^2 - m^2)\theta(p^0)$ and $\mathbb 1_{1\text{-particle}} = \int\frac{d^3p}{(2\pi)^3\,2E_{\mathbf p}}|\mathbf p\rangle\langle\mathbf p|$, see Definition [[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-2|§C2a.4.2]] Invariant Measure and One-Particle Completeness. *Source: Lecture 4 (Sep 14), slide "Details on Normalization (HW)" · PS §2.3, eqs. (2.39)–(2.40) · the user's notes Ch. 4 §4.9*

^nd-def-c2a-4-2

- [ ] Q1 **[def]** Write the invariant measure in its three-dimensional and four-dimensional forms, with every factor of $2\pi$.
- [ ] Q2 **[def]** Write the one-particle resolution of the identity. Check it on $|\mathbf q\rangle$.
- [ ] Q3 **[why]** Why would $\int\frac{d^3p}{(2\pi)^3}|\mathbf p\rangle\langle\mathbf p|$ (without $1/2E_{\mathbf p}$) not be the identity on one-particle states with this normalization?

> [!tip]- Hints: route in the notes
> - Technique: K13 ($\delta(f(x))$).
> - Step 1: the equivalence of the two forms is Theorem [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-3|§C2a.4.3]] The Invariant Measure (→ drilled as [[PHY 513 PS Drill#^ps3-1|PS3.1]]); the completeness check is step 4 of the derivation of Theorem [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-4|§C2a.4.4]] Invariance of the Relativistic Normalization.

### One-particle wave packet

For $g \in \mathcal S(\mathbb R^3)$, $|g\rangle = \int\frac{d^3p}{(2\pi)^3\,2E_{\mathbf p}}g(\mathbf p)|\mathbf p\rangle = \hat a^\dagger(g/\sqrt{2E})|0\rangle$; plane-wave states are not normalizable, see Definition [[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-3|§C2a.4.3]] One-Particle Wave Packet. *Source: the user's notes Ch. 4 §4.8 (Caution "Two honesty points") · Yu, Exercise 2.3*

^nd-def-c2a-4-3

- [ ] Q1 **[def]** Define the wave packet $|g\rangle$ in both forms.
- [ ] Q2 Compute $\langle g|h\rangle$ and $\langle\mathbf p|g\rangle$.
- [ ] Q3 **[why]** What is $\langle\mathbf p|\mathbf p\rangle$, and why does that exclude $|\mathbf p\rangle$ from the Fock space ([[§C2a.4 Particles and Relativistic Normalization#^cau-c2a-4-1|§C2a.4, Caution: Plane-wave states are not normalizable]])?

> [!tip]- Hints: route in the notes
> - Technique: K11.
> - Step 1: Theorem [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-5|§C2a.4.5]] The Overlap of Momentum States Is a Distribution parts 1–3.

### The free complex scalar quantum field

$\mathcal L = \partial_\mu\phi^\dagger\partial^\mu\phi - m^2\phi^\dagger\phi$ with $\hat\pi = \dot{\hat\phi}^\dagger$, $\hat\pi^\dagger = \dot{\hat\phi}$, and $[\hat\phi(\mathbf x), \hat\pi(\mathbf y)] = [\hat\phi^\dagger(\mathbf x), \hat\pi^\dagger(\mathbf y)] = i\delta^3(\mathbf x - \mathbf y)$, see Model [[§C2a.5 The Complex Scalar Field and Its Charge#^mod-c2a-5-1|§C2a.5.1]] The Free Complex Scalar Quantum Field.

^nd-mod-c2a-5-1

→ drilled as [[PHY 513 PS Drill#^ps3-2-a1|PS3.2(a1)]]

### The U(1) charge operator

$\hat Q = \frac i2\int d^3x\,:\!(\hat\phi^\dagger\hat\pi^\dagger - \hat\pi\hat\phi)\!:$, normal ordered; it is $-\frac12$ times the Noether charge of the current with $\Delta\phi = +i\phi$, see Definition [[§C2a.5 The Complex Scalar Field and Its Charge#^def-c2a-5-1|§C2a.5.1]] The U(1) Charge Operator. *Source: Problem Set 3, Problem 2(c), eq. (4) (= PS Problem 2.2(c)) · the user's notes Ch. 4 §4.7*

^nd-def-c2a-5-1

- [ ] Q1 **[def]** Write $\hat Q$ in terms of $\hat\phi$, $\hat\pi$ and in the form with $\overleftrightarrow{\partial_t}$.
- [ ] Q2 **[conv]** Compare with the Noether charge $\int d^3x\,j^0$ of the current with $\Delta\phi = +i\phi$: which factor and which sign relate them? What sign does a positive-frequency mode give to $j^0$?
- [ ] Q3 **[conv]** In the vault, PS and Problem Set 3 the $a$-quanta carry which charge? What does Yu's $\hat Q$ give? Which part of the convention is physical?
- [ ] Q4 **[why]** Why must $\hat Q$ be normal ordered, unlike $\hat{\mathbf P}$ of the real field?

> [!tip]- Hints: route in the notes
> - Technique: K12 (Noether recipe) for the comparison.
> - Step 1: [[§C2a.5 The Complex Scalar Field and Its Charge#^cau-c2a-5-1|§C2a.5, Caution: Normalization and sign of the charge]]; register row "Complex-field charge".
> - Step 2: [[§C2a.5 The Complex Scalar Field and Its Charge#^rem-c2a-5-2|§C2a.5, Remark: Why the vacuum must be neutral]] (a charged vacuum).
> - Step 3: the mode form is Theorem [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-6|§C2a.5.6]] The Charge Counts Particles Minus Antiparticles (→ drilled as [[PHY 513 PS Drill#^ps3-2-c|PS3.2(c)]]).

### Coherent state of the field

$|\{\eta\}\rangle = e^{-\bar N/2}\exp\{\int\frac{d^3k}{(2\pi)^3}\frac{\eta_{\mathbf k}\hat a^\dagger_{\mathbf k}}{\sqrt{2E_{\mathbf k}}}\}|0\rangle = \hat D(\eta)|0\rangle$ with $\bar N = \int\frac{d^3k}{(2\pi)^3}\frac{|\eta_{\mathbf k}|^2}{2E_{\mathbf k}} < \infty$, see Definition [[§C2a.6 Coherent States and the Classical Field#^def-c2a-6-1|§C2a.6.1]] Coherent State of the Field. *Source: Problem Set 3, Problem 4, eq. (11) · the user's notes Ch. 4 §4.10*

^nd-def-c2a-6-1

- [ ] Q1 **[def]** Write the coherent state in exponential form and in displacement-operator form.
- [ ] Q2 **[why]** Why must $\bar N$ be finite? What goes wrong for a plane-wave label $\eta_{\mathbf k} \propto \delta^3(\mathbf k - \mathbf k_0)$?
- [ ] Q3 **[why]** Why can a state of definite particle number not describe a classical field (Theorem [[§C2a.6 Coherent States and the Classical Field#^thm-c2a-6-1|§C2a.6.1]] A State of Definite Particle Number Has No Mean Field)?

> [!tip]- Hints: route in the notes
> - Technique: K11 (BCH).
> - Step 1: normalization and eigenvalue property are Theorem [[§C2a.6 Coherent States and the Classical Field#^thm-c2a-6-2|§C2a.6.2]] Coherent States Are Eigenstates of Every Annihilator (→ drilled as [[PHY 513 PS Drill#^ps3-4-a|PS3.4(a)]]–(b)); the displaced vacuum is Theorem [[§C2a.6 Coherent States and the Classical Field#^thm-c2a-6-3|§C2a.6.3]] A Coherent State Is the Displaced Vacuum.

## Derivations T5

### The canonical relations are identities after smearing ★

For real $f, g \in \mathcal S(\mathbb R^3)$, $[\hat\phi(f), \hat\pi(g)] = i\int d^3x\,f g$ and the other two smeared commutators vanish; at one point the relation would assign $i\delta^3(\mathbf 0)$, which has no value, see Theorem [[§C2a.1 Canonical Quantization of Fields#^thm-c2a-1-3|§C2a.1.3]] The Canonical Relations Are Identities after Smearing. *Source: the user's notes Ch. 4 §4.2, §4.8, App. A §A.4*

^nd-thm-c2a-1-3

- [ ] Q1 **[state]** State the smeared form of the canonical relations.
- [ ] Q2 Pair $[\hat\phi(\mathbf x), \hat\pi(\mathbf y)]$ with $f(\mathbf x)g(\mathbf y)$: what is the left side, and which theorem guarantees a unique kernel?
- [ ] Q3 Evaluate $\delta^3(\mathbf x - \mathbf y)$ on $f \otimes g$ by the change of variables $\mathbf u = \mathbf x - \mathbf y$, $\mathbf v = \mathbf y$.
- [ ] Q4 Find $f$, $g$ that make $\hat\phi(f)$, $\hat\pi(g)$ one canonical pair with $[\hat Q, \hat P] = i$.
- [ ] Q5 **[why]** Why is there no relation between operators at a single point? Use a nascent delta.

> [!tip]- Hints: route in the notes
> - Technique: none (distributions).
> - Step 1: kernel theorem Theorem [[§CA.2 Generalized Functions#^thm-ca-2-11|§CA.2.11]] The Kernel Theorem; change of variables Definition [[§CA.2 Generalized Functions#^def-ca-2-8|§CA.2.8]] Linear Change of Variables.
> - Step 2: nascent deltas Theorem [[§CA.2 Generalized Functions#^thm-ca-2-5|§CA.2.5]] Distributional Limits part 3; δ at its singular point Theorem [[§CA.2 Generalized Functions#^thm-ca-2-9|§CA.2.9]] Products Without a Value: θ·δ, δ² and δ(0) part 3.

### The free field is a set of independent oscillators ★★

Expanding the classical field at fixed time in spatial Fourier modes, $H = \int\frac{d^3p}{(2\pi)^3}\frac12[|\tilde\pi(\mathbf p)|^2 + E_{\mathbf p}^2|\tilde\phi(\mathbf p)|^2]$ and $\ddot{\tilde\phi} + E_{\mathbf p}^2\tilde\phi = 0$, see Theorem [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-1|§C2a.2.1]] The Free Field Is a Set of Independent Oscillators. *Source: Lecture 4 (Sep 14), slide "Physical Content" ("modes decouple, each value of p equivalent to a harmonic oscillator") · PS §2.3, eqs. (2.21)–(2.22) · the user's notes Ch. 4 §4.2*

^nd-thm-c2a-2-1

- [ ] Q1 **[state]** State what "the free field is a set of independent oscillators" means: the mass, frequency and label of each oscillator.
- [ ] Q2 Substitute the Fourier expansion into $\int d^3x\,\frac12\pi^2$ with different names $\mathbf p$, $\mathbf p'$. Which delta function appears, and what is eliminated?
- [ ] Q3 **[why]** Why does reality of $\pi$ turn $\tilde\pi(\mathbf p)\tilde\pi(-\mathbf p)$ into $|\tilde\pi(\mathbf p)|^2$?
- [ ] Q4 Do the gradient term: what does $\nabla$ bring down in each factor, and what is the product after the delta?
- [ ] Q5 Add the gradient and mass terms. Which relation makes them one frequency?
- [ ] Q6 **[why]** In position space the gradient term couples neighbouring points. Why does it not couple different modes in momentum space?

> [!tip]- Hints: route in the notes
> - Technique: K9 (mode substitution).
> - Step 1: derivation steps 1–3 (kinetic term, $d^3x$ integral, integrate the delta); step 4 (reality).
> - Step 2: steps 5–7 (gradient, mass, add); step 8 (equation of motion).
> - Step 3: [[§C2a.2 Mode Expansion and the Mode Algebra#^rem-c2a-2-1|§C2a.2, Remark: Why the modes decouple, and why the frequency is the energy]] (decoupling is translation invariance).

### Mode expansion of the real field ★★

Every real solution of $(\partial^2 + m^2)\phi = 0$ is $\phi = \int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}(a_{\mathbf p}e^{-ip\cdot x} + a^\ast_{\mathbf p}e^{ip\cdot x})$, and at $t = 0$ the quantum field is $\hat\phi(\mathbf x) = \int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}(\hat a_{\mathbf p} + \hat a^\dagger_{-\mathbf p})e^{i\mathbf p\cdot\mathbf x}$, $\hat\pi$ likewise with $(-i)\sqrt{E_{\mathbf p}/2}$ and a relative minus sign, see Theorem [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-2|§C2a.2.2]] Mode Expansion of the Real Field. *Source: Lecture 4 (Sep 14), slide "Oscillator Expansion" (posited by analogy with the oscillator) · PS §2.3, eqs. (2.25)–(2.28) · Yu eq. (2.122) · the user's notes Ch. 4 §4.4*

^nd-thm-c2a-2-2

- [ ] Q1 **[state]** Write $\hat\phi(\mathbf x)$ and $\hat\pi(\mathbf x)$ at $t = 0$ with every factor and sign.
- [ ] Q2 Act with $\partial^2 + m^2$ on $e^{-ik\cdot x}$. Which values of $k^0$ are allowed, and why are both signs needed?
- [ ] Q3 In the negative-frequency term substitute $\mathbf k = -\mathbf p$. What changes and what does not?
- [ ] Q4 **[why]** How does reality of $\phi$ fix the second coefficient in terms of the first?
- [ ] Q5 Pass to $t = 0$ and relabel in the $a^\ast$ term only. Why does $\hat a^\dagger_{-\mathbf p}$, not $\hat a^\dagger_{\mathbf p}$, accompany $\hat a_{\mathbf p}$?
- [ ] Q6 **[conv]** Which factor in the expansion is a normalization choice, and which later definition cashes it in? Is the expansion the same in PS and Yu?
- [ ] Q7 **[why]** Lecture 4 posited the expansion by analogy with the oscillator. Which two pieces of guidance did the slide give, and what verified the ansatz?

> [!tip]- Hints: route in the notes
> - Technique: K9.
> - Step 1: derivation steps 1–4 (plane waves, general solution, change of variables, reality); steps 5–7 (momentum density, fixed time, quantize).
> - Step 2: [[§C2a.2 Mode Expansion and the Mode Algebra#^rem-c2a-2-3|§C2a.2, Remark: Posited or derived]] (posited or derived); the ansatz is verified by the second route of Theorem [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|§C2a.2.6]] The Mode Algebra.
> - Step 3: normalization: Definition [[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-1|§C2a.4.1]] Relativistic Normalization, Theorem [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-6|§C2a.4.6]] The Field Creates a Particle at a Point; register row "Mode expansion".

### Conservation and orthonormality of the modes ★

$(f, g)$ is slice independent for solutions that fall off at infinity, and $(f_{\mathbf p}, f_{\mathbf q}) = (2\pi)^3\delta^3(\mathbf p - \mathbf q)$, $(f^\ast_{\mathbf p}, f^\ast_{\mathbf q}) = -(2\pi)^3\delta^3(\mathbf p - \mathbf q)$, $(f_{\mathbf p}, f^\ast_{\mathbf q}) = 0$, see Theorem [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-3|§C2a.2.3]] Conservation and Orthonormality of the Modes. Part 1 (slice independence) → drilled as [[PHY 513 PS Drill#^ps3-3-a|PS3.3(a)]]. *Source: Problem Set 3, Problem 3(a) · the user's notes Ch. 4 §4.5*

^nd-thm-c2a-2-3

- [ ] Q1 **[state]** State the three orthonormality relations.
- [ ] Q2 Compute $(f_{\mathbf p}, f_{\mathbf q})$ before the $d^3x$ integral: what are $\partial_tf_{\mathbf q}$ and $\partial_tf^\ast_{\mathbf p}$, and what factor multiplies $e^{i(p - q)\cdot x}$?
- [ ] Q3 Do the $d^3x$ integral and use the support of the delta to simplify the prefactor and the phase. What is left?
- [ ] Q4 Compute the mixed product $(f_{\mathbf p}, f^\ast_{\mathbf q})$. Which combination of energies multiplies $\delta^3(\mathbf p + \mathbf q)$, and why does it vanish?
- [ ] Q5 Derive $(f^\ast, g^\ast) = -(f, g)^\ast$ and use it for the negative-frequency norm.
- [ ] Q6 **[why]** Where does each relation enter the extraction formula and the mode algebra?

> [!tip]- Hints: route in the notes
> - Technique: K10 (extracting mode operators), K9.
> - Step 1: derivation steps 6–8 (positive-frequency product), step 9 (mixed product), steps 5 and 10 (conjugation, negative frequency).
> - Step 2: used in Theorem [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-5|§C2a.2.5]] Mode Extraction and Theorem [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|§C2a.2.6]] The Mode Algebra.

### Orthonormality for wave packets ★

For $g, h \in \mathcal S$ and $f_g = \int\frac{d^3p}{(2\pi)^3}g(\mathbf p)f_{\mathbf p}$: $(f_g, f_h) = \int\frac{d^3p}{(2\pi)^3}\bar gh$, $(f^\ast_g, f^\ast_h) = -\int\frac{d^3p}{(2\pi)^3}g\bar h$, $(f_g, f^\ast_h) = 0$, every integral absolutely convergent; the plane-wave relations are their kernels, see Theorem [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-4|§C2a.2.4]] Orthonormality for Wave Packets. *Source: the user's notes Ch. 4 §4.5, §4.8*

^nd-thm-c2a-2-4

- [ ] Q1 **[state]** State the three wave-packet identities.
- [ ] Q2 Compute $(f_g, f_h)$ by Plancherel: what multiplies $\bar AB$, and why do the time phases cancel?
- [ ] Q3 **[why]** In what precise sense is "$(f_{\mathbf p}, f_{\mathbf q}) = (2\pi)^3\delta^3(\mathbf p - \mathbf q)$" true?

> [!tip]- Hints: route in the notes
> - Technique: K9.
> - Step 1: derivation steps 1–3; Plancherel is Theorem [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-1|§CA.3.1]] Fourier Inversion and Plancherel on 𝒮 part 3; step 6 (the kernel).

### Mode extraction

$\hat a_{\mathbf p} = (f_{\mathbf p}, \hat\phi) = \frac{i}{\sqrt{2E_{\mathbf p}}}\int d^3x\,e^{ip\cdot x}(\hat\pi - iE_{\mathbf p}\hat\phi)$, $\hat a^\dagger_{\mathbf p} = -(f^\ast_{\mathbf p}, \hat\phi)$, independent of the slice, see Theorem [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-5|§C2a.2.5]] Mode Extraction.

^nd-thm-c2a-2-5

→ drilled as [[PHY 513 PS Drill#^ps3-3-b|PS3.3(b)]]

### The mode algebra, from the oscillators to the fields (Lecture 4's direction) ★★

The equal-time relations hold if and only if $[\hat a_{\mathbf p}, \hat a^\dagger_{\mathbf q}] = (2\pi)^3\delta^3(\mathbf p - \mathbf q)$ and the other commutators vanish, see Theorem [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|§C2a.2.6]] The Mode Algebra. The direction fields ⇒ oscillators → drilled as [[PHY 513 PS Drill#^ps3-3-c|PS3.3(c)]] [class exercise, Lecture 4: the slide "Canonical Commutation Relations" says "Proof of ⇒ is in HW"]. The questions rebuild the lecture's direction, oscillators ⇒ fields (the second route). *Source: Lecture 4 (Sep 14), slide "Canonical Commutation Relations"; transcript ("half of it was done on the homework") · PS §2.3, eqs. (2.29)–(2.30) · the user's notes Ch. 4 §4.5*

^nd-thm-c2a-2-6

- [ ] Q1 **[state]** State the equivalence: which relations on each side, and which expansions connect them.
- [ ] Q2 Write $[\hat\phi(\mathbf x), \hat\pi(\mathbf y)]$ with integration variables $\mathbf p$ and $\mathbf p'$ and expand the bracket of operators into all four commutators. Which two survive?
- [ ] Q3 **[why]** The two surviving terms must add, not cancel. Which features of the ansatz for $\hat\pi$ (relative sign, factor $-i\sqrt{E/2}$) make them add?
- [ ] Q4 Integrate the delta in $\mathbf p'$. What happens to the factor $\sqrt{E_{\mathbf p'}/E_{\mathbf p}}$, and what is the remaining $\mathbf p$ integral?
- [ ] Q5 Show $[\hat\phi(\mathbf x), \hat\phi(\mathbf y)] = 0$: which two terms appear, and why do they cancel?
- [ ] Q6 **[why]** The cancellation in Q5 is the first instance of which later statement about the field commutator?

> [!tip]- Hints: route in the notes
> - Technique: K9, K11.
> - Step 1: second-route derivation, steps 1–4 (write both fields; expand all four terms; integrate the delta; the other two relations).
> - Step 2: the first-route steps (extracted operators, KG product) are the PS3.3(c) drill; "the algebra is orthonormality in operator form".
> - Step 3: Q6: Theorem [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-5|§C2b.4.5]] The Free Field Is Microcausal.

### The mode algebra smeared ★

$[\hat a(g), \hat a^\dagger(h)] = \int\frac{d^3p}{(2\pi)^3}\bar gh$; annihilators at a point act on wave packets; $\hat\phi(f) = \hat a(g_f) + \hat a^\dagger(g_f)$ with $g_f = \tilde f/\sqrt{2E}$, see Theorem [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-7|§C2a.2.7]] The Mode Algebra Smeared. *Source: the user's notes Ch. 4 §4.5, §4.8*

^nd-thm-c2a-2-7

- [ ] Q1 **[state]** State the smeared mode algebra and the decomposition of $\hat\phi(f)$.
- [ ] Q2 Compute $\hat a_{\mathbf p}\hat a^\dagger(h)|0\rangle$.
- [ ] Q3 Smear the $t = 0$ field with a real $f$: which property of $\tilde f$ lets you identify the creation part as $\hat a^\dagger(g_f)$?
- [ ] Q4 **[why]** Why does $[\hat a_{\mathbf p}, \hat a^\dagger_{\mathbf p}]$ have no value while $[\hat a(g), \hat a^\dagger(g)]$ is a finite number?

> [!tip]- Hints: route in the notes
> - Technique: K11.
> - Step 1: derivation steps 1–3 (smear; act on packets; creators at a point), steps 4–5 (smear the field; reality $\tilde f(-\mathbf p) = \overline{\tilde f(\mathbf p)}$).

### Hamiltonian in mode form ★★

$\hat H$ read in the order written is $\int\frac{d^3p}{(2\pi)^3}\frac{E_{\mathbf p}}{2}(\hat a_{\mathbf p}\hat a^\dagger_{\mathbf p} + \hat a^\dagger_{\mathbf p}\hat a_{\mathbf p}) = \int\frac{d^3p}{(2\pi)^3}E_{\mathbf p}\hat a^\dagger_{\mathbf p}\hat a_{\mathbf p} + E_0$, the same on every slice, see Theorem [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-1|§C2a.3.1]] Hamiltonian in Mode Form. *Source: Lecture 4 (Sep 14), slides "Diagonalizing the Hamiltonian: Strategy" and "Details" · PS §2.3, eq. (2.31) · Yu eqs. (2.130)–(2.132) · the user's notes Ch. 4 §4.6*

^nd-thm-c2a-3-1

- [ ] Q1 **[state]** State $\hat H$ in mode form, both before and after reordering.
- [ ] Q2 Substitute the $t = 0$ expansions (variables $\mathbf p$, $\mathbf p'$) into the three terms of $\hat H$. Do the $d^3x$ integral and integrate the delta: which operator products remain, with which coefficients?
- [ ] Q3 Show that the coefficient of the gradient-plus-mass term equals that of the $\hat\pi^2$ term. Which relation is used?
- [ ] Q4 Expand both products into all four terms. Which terms cancel between $\hat\pi^2$ and the rest, and which add?
- [ ] Q5 Relabel $\mathbf p \to -\mathbf p$ in one surviving term and reorder with the mode algebra. What constant appears?
- [ ] Q6 **[why]** The number-changing terms $\hat a\hat a$ and $\hat a^\dagger\hat a^\dagger$ cancel. Which ingredient makes them cancel here, and where did the same ingredient appear on a general time slice?
- [ ] Q7 **[why]** The Lecture 4 slide says of the constant "cancels in differences. Ignore!". Is the symmetric ordering forced by the classical theory?

> [!tip]- Hints: route in the notes
> - Technique: K9 (mode substitution), K11.
> - Step 1: derivation steps 1–4 (substitute, $d^3x$ integral, delta, mass shell); steps 5–6 (expand, combine with $\mp E_{\mathbf p}/4$).
> - Step 2: steps 7–8 (relabel, reorder); steps 9–11 (any time slice: the $t$-dependent terms have vanishing coefficients).
> - Step 3: Theorem [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-4|§C2a.3.4]] The Zero-Point Energy, [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^rem-c2a-3-2|§C2a.3, Remark: Normal ordering is a choice of quantization]]; P1, step 7.

### δ³(0) has no value; in a box it is the volume ★

The constant $(2\pi)^3\delta^3(\mathbf 0)$ left by reordering is δ at its singular point; in a periodic box with cutoff $\Lambda$, $E_0(V, \Lambda) = \frac12\sum_{|\mathbf k| < \Lambda}E_{\mathbf k}$ and $E_0/V \to \int_{|\mathbf p| < \Lambda}\frac{d^3p}{(2\pi)^3}\frac{E_{\mathbf p}}{2}$, see Theorem [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-2|§C2a.3.2]] δ³(0) Has No Value; in a Box It Is the Volume. *Source: the user's notes Ch. 4 §4.6, §4.5, Ch. 6 §6.2*

^nd-thm-c2a-3-2

- [ ] Q1 **[state]** State both parts: why $\delta^3(\mathbf 0)$ has no value, and its box meaning.
- [ ] Q2 In a box of side $L$ with periodic conditions, which momenta are allowed, and what replaces $(2\pi)^3\delta^3(\mathbf k - \mathbf k')$?
- [ ] Q3 Reorder $\hat a_{\mathbf k}\hat a^\dagger_{\mathbf k}$ in the box and read off $E_0(V, \Lambda)$.
- [ ] Q4 Take $V \to \infty$ at fixed $\Lambda$: why does $\frac1V\sum_{\mathbf k}$ become $\int\frac{d^3p}{(2\pi)^3}$?
- [ ] Q5 **[why]** Which divergence is infrared and which ultraviolet? Which one does the box remove?

> [!tip]- Hints: route in the notes
> - Technique: none (regularization).
> - Step 1: derivation steps 1–6; box regularization Theorem [[§CA.2 Generalized Functions#^thm-ca-2-10|§CA.2.10]] Box Regularization of δ³(0); δ at its singular point Theorem [[§CA.2 Generalized Functions#^thm-ca-2-9|§CA.2.9]] Products Without a Value: θ·δ, δ² and δ(0) part 3.

### The zero-point energy ★★

$E_0 = \langle0|\hat H|0\rangle = V\int\frac{d^3p}{(2\pi)^3}\frac{E_{\mathbf p}}{2}$, $V = (2\pi)^3\delta^3(\mathbf 0)$; with a cutoff $\Lambda \gg m$ the density is $\varepsilon_0 \approx \Lambda^4/16\pi^2$; a c-number, see Theorem [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-4|§C2a.3.4]] The Zero-Point Energy. *Source: Lecture 4 (Sep 14), slide "Diagonalizing the Hamiltonian: Details" ("0-point energy cancels in differences") · PS §2.3, after eq. (2.31) · Yu eqs. (2.132), (2.134) · the user's notes Ch. 4 §4.6*

^nd-thm-c2a-3-4

- [ ] Q1 **[state]** State the zero-point energy and its two divergences.
- [ ] Q2 Show that the reordering constant is the vacuum expectation value of the unordered $\hat H$.
- [ ] Q3 Show $(2\pi)^3\delta^3(\mathbf 0) = \int d^3x$ from the plane-wave delta.
- [ ] Q4 Compute the energy density with a momentum cutoff $\Lambda \gg m$, to leading order.
- [ ] Q5 **[why]** Why is $E_0$ invisible to the Heisenberg equations and to energy differences? Which interaction does see it, and in what situation do differences of it become observable?
- [ ] Q6 **[conv]** How do the vault, PS and Yu name this constant, and what is it called for the complex scalar field?

> [!tip]- Hints: route in the notes
> - Technique: K9.
> - Step 1: derivation steps 1–3 (origin, vacuum value, δ as a volume); steps 4–5 (density, cutoff); step 6 (c-number).
> - Step 2: [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^cau-c2a-3-1|§C2a.3, Caution: Names for the zero-point energy]]; register row "Zero-point energy".

### Momentum in mode form [class exercise, Lecture 4]

$\hat{\mathbf P} = -\int d^3x\,\hat\pi\nabla\hat\phi = \int\frac{d^3p}{(2\pi)^3}\mathbf p\,\hat a^\dagger_{\mathbf p}\hat a_{\mathbf p}$, with no constant and no ordering choice, see Theorem [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-5|§C2a.3.5]] Momentum in Mode Form; the normal-ordered version is Example [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^ex-c2a-3-1|§C2a.3.1]] The Momentum, Normal-Ordered from the Outset. In Lecture 4 Larsen stated the result ("if you took the phi … and plugged it in here, this whole d3x integral will become a d3p integral") without the computation. *Source: Lecture 4 (Sep 14), slide "Comments"; transcript · Problem Set 6, Problem 1*

^nd-thm-c2a-3-5

→ drilled as [[PHY 513 PS Drill#^ps6-1|PS6.1]]

### The normal-ordered Hamiltonian acts on wave packets ★

$:\!\hat H\!:|0\rangle = 0$ and $:\!\hat H\!:$ maps $\hat a^\dagger(g_1)\cdots\hat a^\dagger(g_n)|0\rangle$ to a sum with one $g_j$ replaced by $E\,g_j$; in a box $\hat H_V = :\!\hat H_V\!: + E_0(V, \Lambda)$ exactly, see Theorem [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-6|§C2a.3.6]] The Normal-Ordered Hamiltonian Acts on Wave Packets. *Source: the user's notes Ch. 4 §4.6, §4.8*

^nd-thm-c2a-3-6

- [ ] Q1 **[state]** State how $:\!\hat H\!:$ acts on an $n$-particle wave-packet state.
- [ ] Q2 Compute $:\!\hat H\!:\hat a^\dagger(g)|0\rangle$ using $\hat a_{\mathbf p}\hat a^\dagger(g)|0\rangle$.
- [ ] Q3 **[why]** In which sense is $:\!\hat H\!:$ an operator while $\hat H$ in the order written is not?

> [!tip]- Hints: route in the notes
> - Technique: K11.
> - Step 1: derivation steps 1–3; step 4–5 (box).

### Ladder relations ★★

$[\hat H, \hat a^\dagger_{\mathbf p}] = E_{\mathbf p}\hat a^\dagger_{\mathbf p}$, $[\hat H, \hat a_{\mathbf p}] = -E_{\mathbf p}\hat a_{\mathbf p}$, and the same with $\hat{\mathbf P}$ and $\mathbf p$; so $\hat a^\dagger_{\mathbf p}$ adds energy $E_{\mathbf p}$ and momentum $\mathbf p$, see Theorem [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-7|§C2a.3.7]] Ladder Relations. *Source: Lecture 4 (Sep 14), slides "Spectrum of Simple Harmonic Oscillator" (proof for one oscillator), "Simplest Excited States" · PS §2.3, eq. (2.32) · the user's notes Ch. 4 §4.8*

^nd-thm-c2a-3-7

- [ ] Q1 **[state]** State the four ladder relations.
- [ ] Q2 **[why]** Why can the zero-point constant be dropped from every commutator?
- [ ] Q3 Compute $[\hat a^\dagger_{\mathbf q}\hat a_{\mathbf q}, \hat a^\dagger_{\mathbf p}]$ with the product rule for commutators.
- [ ] Q4 Integrate against $E_{\mathbf q}$ and use the delta.
- [ ] Q5 From $[\hat H, \hat a^\dagger_{\mathbf p}]$, show that $\hat a^\dagger_{\mathbf p}|\psi\rangle$ has energy $E + E_{\mathbf p}$ when $\hat H|\psi\rangle = E|\psi\rangle$.

> [!tip]- Hints: route in the notes
> - Technique: K11.
> - Step 1: derivation steps 1–4; step 5 (momentum); step 6 (eigenstates).

### The spectrum: particles ★★

$:\!\hat H\!: \ge 0$ with ground state $|0\rangle$; $\hat a^\dagger_{\mathbf p_1}\cdots\hat a^\dagger_{\mathbf p_n}|0\rangle$ has energy $\sum E_{\mathbf p_i}$ and momentum $\sum\mathbf p_i$; $\hat N$ counts particles and commutes with $\hat H$, $\hat{\mathbf P}$, see Theorem [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-1|§C2a.4.1]] The Spectrum: Particles. *Source: Lecture 4 (Sep 14), slides "Spectrum", "More on the Spectrum" · PS §2.3, p. 22 · the user's notes Ch. 4 §4.8*

^nd-thm-c2a-4-1

- [ ] Q1 **[state]** State the three parts of the theorem.
- [ ] Q2 Show $\langle\psi|\hat a^\dagger_{\mathbf p}\hat a_{\mathbf p}|\psi\rangle \ge 0$ and conclude $:\!\hat H\!: \ge 0$.
- [ ] Q3 Prove the energy of the $n$-particle state by induction, moving $\hat H$ through one creator at a time.
- [ ] Q4 Compute $[\hat N, \hat a^\dagger_{\mathbf p}]$ and the eigenvalue of $\hat N$ on the $n$-particle state.
- [ ] Q5 **[why]** The expansion contains negative frequencies. Why are there no negative-energy states?
- [ ] Q6 **[why]** Why is the label $\mathbf p$, introduced as a Fourier variable, the momentum of the particle?

> [!tip]- Hints: route in the notes
> - Technique: K11.
> - Step 1: derivation steps 1–5; Theorem [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-7|§C2a.3.7]] Ladder Relations.
> - Step 2: [[§C2a.4 Particles and Relativistic Normalization#^rem-c2a-4-1|§C2a.4, Remark: What the spectrum says]] (what the spectrum says).

### Bose symmetry and multiple occupation ★★

$\hat a^\dagger_{\mathbf p_1}\hat a^\dagger_{\mathbf p_2}|0\rangle = \hat a^\dagger_{\mathbf p_2}\hat a^\dagger_{\mathbf p_1}|0\rangle$ and the two-particle overlap has a direct and an exchanged term; one packet mode holds any number of quanta, see Theorem [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-2|§C2a.4.2]] Bose Symmetry and Multiple Occupation. *Source: Lecture 4 (Sep 14), slide "More on the Spectrum" ("Scalar particles are bosons") · PS §2.3, p. 22 · the user's notes Ch. 4 §4.8*

^nd-thm-c2a-4-2

- [ ] Q1 **[state]** State Bose symmetry and the two-particle overlap formula.
- [ ] Q2 Compute $\langle0|\hat a_{\mathbf q_2}\hat a_{\mathbf q_1}\hat a^\dagger_{\mathbf p_1}\hat a^\dagger_{\mathbf p_2}|0\rangle$ by moving annihilators to the right.
- [ ] Q3 For a normalized packet operator $\hat c^\dagger = \int\frac{d^3p}{(2\pi)^3}\psi(\mathbf p)\hat a^\dagger_{\mathbf p}$, compute $[\hat c, \hat c^\dagger]$.
- [ ] Q4 **[why]** Statistics were not imposed. Which equal-time relation forces Bose symmetry?

> [!tip]- Hints: route in the notes
> - Technique: K11.
> - Step 1: derivation steps 1–4.

### The invariant measure [class exercise, Lecture 4]

For proper orthochronous Lorentz transformations, $\theta(p^0)$ is invariant on the mass shell and $\int\frac{d^3p}{2E_{\mathbf p}}F = \int d^4p\,\delta(p^2 - m^2)\theta(p^0)F$, so $d^3p/2E_{\mathbf p}$ is invariant, see Theorem [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-3|§C2a.4.3]] The Invariant Measure. Lecture 4: "there's an exercise to do there in relativistic kinematics"; slide "Details on Normalization (HW)". *Source: Lecture 4 (Sep 14), slide and transcript · Problem Set 3, Problem 1*

^nd-thm-c2a-4-3

→ drilled as [[PHY 513 PS Drill#^ps3-1|PS3.1]]

### Invariance of the relativistic normalization ★

$2E_{\mathbf p}\delta^3(\mathbf p - \mathbf q)$ is Lorentz invariant, hence so are $\langle\mathbf p|\mathbf q\rangle$ and the one-particle resolution of the identity; $\delta^3(\mathbf p - \mathbf q)$ alone is not, see Theorem [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-4|§C2a.4.4]] Invariance of the Relativistic Normalization. *Source: PS §2.3, eqs. (2.34)–(2.36), (2.39) · Yu eqs. (2.155)–(2.157) · the user's notes Ch. 4 §4.9*

^nd-thm-c2a-4-4

- [ ] Q1 **[state]** State which of $\delta^3(\mathbf p - \mathbf q)$ and $2E_{\mathbf p}\delta^3(\mathbf p - \mathbf q)$ is invariant, and the consequences for states.
- [ ] Q2 First route: show that $2E_{\mathbf p}\delta^3$ is the kernel that reproduces scalar test functions against the invariant measure. Why does that make it invariant?
- [ ] Q3 Second route: boost along $z$. Compute $dp_3'/dp_3$ on the shell and express it through energies.
- [ ] Q4 Apply the composition rule for $\delta(p_3 - q_3)$ and conclude.
- [ ] Q5 **[why]** Give the physical reason with a box at rest and in a moving frame.

> [!tip]- Hints: route in the notes
> - Technique: K14, K13 ($\delta(f(x))$).
> - Step 1: first derivation steps 1–4; second derivation steps 1–3 (boost, derivative, delta of a function).

### The overlap of momentum states is a distribution ★

$\langle g|h\rangle = \int\frac{d^3p}{(2\pi)^3\,2E_{\mathbf p}}\bar gh$; $\langle\mathbf p|\mathbf q\rangle$ is the kernel; $\langle\mathbf p|\mathbf p\rangle$ has no value; $\langle\mathbf p|g\rangle = g(\mathbf p)$ and completeness holds between wave packets, see Theorem [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-5|§C2a.4.5]] The Overlap of Momentum States Is a Distribution. *Source: the user's notes Ch. 4 §4.8–4.9 · Yu, Exercise 2.3*

^nd-thm-c2a-4-5

- [ ] Q1 **[state]** State the three parts.
- [ ] Q2 Compute $\langle g|h\rangle$ as a commutator of smeared mode operators.
- [ ] Q3 **[why]** What is the one-particle Hilbert space, and with which measure?

> [!tip]- Hints: route in the notes
> - Technique: K11.
> - Step 1: derivation steps 1–5.

### The field creates a particle at a point ★

$\hat\phi(\mathbf x)|0\rangle = \int\frac{d^3p}{(2\pi)^3\,2E_{\mathbf p}}e^{-i\mathbf p\cdot\mathbf x}|\mathbf p\rangle$, $\langle0|\hat\phi(\mathbf x)|\mathbf p\rangle = e^{i\mathbf p\cdot\mathbf x}$; with time dependence $\langle0|\hat\phi(x)|\mathbf p\rangle = e^{-ip\cdot x}$, see Theorem [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-6|§C2a.4.6]] The Field Creates a Particle at a Point. *Source: PS §2.3, eqs. (2.41)–(2.42) · the user's notes Ch. 4 §4.9*

^nd-thm-c2a-4-6

- [ ] Q1 **[state]** State $\hat\phi(\mathbf x)|0\rangle$ and the two matrix elements.
- [ ] Q2 Act with the $t = 0$ field on $|0\rangle$: which term survives, and how do the two factors $1/\sqrt{2E}$ combine with the normalization of $|\mathbf p\rangle$?
- [ ] Q3 Project on $\langle\mathbf q|$ and integrate the delta.
- [ ] Q4 **[why]** Which quantum-mechanical overlap is this the analogue of, and where does the choice $1/\sqrt{2E_{\mathbf p}}$ pay off?

> [!tip]- Hints: route in the notes
> - Technique: K9.
> - Step 1: derivation steps 1–4; Definition [[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-1|§C2a.4.1]] Relativistic Normalization.

### The smeared field creates a state; the field at a point does not ★

$\hat\phi(f)|0\rangle = |\tilde f\rangle$ with finite norm $\int\frac{d^3p}{(2\pi)^3\,2E_{\mathbf p}}|\tilde f|^2$; as $f$ narrows to a point the norm diverges like $\Lambda^2/8\pi^2$, see Theorem [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-7|§C2a.4.7]] The Smeared Field Creates a State; the Field at a Point Does Not. *Source: the user's notes Ch. 4 §4.8–4.9*

^nd-thm-c2a-4-7

- [ ] Q1 **[state]** State the result for the smeared field and for the field at a point.
- [ ] Q2 Compute the norm of $\hat\phi(f)|0\rangle$.
- [ ] Q3 With $f_\varepsilon \to \delta^3$, estimate the norm with a cutoff $\Lambda$: which power of $\Lambda$?
- [ ] Q4 **[why]** Is the obstruction ultraviolet or infrared?

> [!tip]- Hints: route in the notes
> - Technique: K9.
> - Step 1: derivation steps 1–5; Theorem [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-7|§C2a.2.7]] The Mode Algebra Smeared part 3.

### Mode expansion of the complex field

$\hat\phi = \int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}(\hat a_{\mathbf p}e^{-ip\cdot x} + \hat b^\dagger_{\mathbf p}e^{ip\cdot x})$, $\hat a_{\mathbf p} = (f_{\mathbf p}, \hat\phi)$, $\hat b_{\mathbf p} = (f_{\mathbf p}, \hat\phi^\dagger)$, see Theorem [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-2|§C2a.5.2]] Mode Expansion of the Complex Field.

^nd-thm-c2a-5-2

→ drilled as [[PHY 513 PS Drill#^ps3-2-b|PS3.2(b)]]

### Mode algebra of the complex field

$[\hat a_{\mathbf p}, \hat a^\dagger_{\mathbf q}] = [\hat b_{\mathbf p}, \hat b^\dagger_{\mathbf q}] = (2\pi)^3\delta^3(\mathbf p - \mathbf q)$, all other commutators zero, including the mixed ones, see Theorem [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-3|§C2a.5.3]] Mode Algebra of the Complex Field.

^nd-thm-c2a-5-3

→ drilled as [[PHY 513 PS Drill#^ps3-2-b|PS3.2(b)]]

### Hamiltonian of the complex field

$\hat H = \int\frac{d^3p}{(2\pi)^3}E_{\mathbf p}(\hat a^\dagger\hat a + \hat b^\dagger\hat b) + 2E_0$: two species of mass $m$, see Theorem [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-4|§C2a.5.4]] Hamiltonian of the Complex Field.

^nd-thm-c2a-5-4

→ drilled as [[PHY 513 PS Drill#^ps3-2-b|PS3.2(b)]]

### Momentum of the complex field ★

$\hat{\mathbf P} = -\int d^3x\,(\hat\pi\nabla\hat\phi + \hat\pi^\dagger\nabla\hat\phi^\dagger) = \int\frac{d^3p}{(2\pi)^3}\mathbf p\,(\hat a^\dagger_{\mathbf p}\hat a_{\mathbf p} + \hat b^\dagger_{\mathbf p}\hat b_{\mathbf p})$, with no constant, see Theorem [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-5|§C2a.5.5]] Momentum of the Complex Field. *Source: the user's notes Ch. 4 §4.7 · Yu eq. (2.216)*

^nd-thm-c2a-5-5

- [ ] Q1 **[state]** State $\hat{\mathbf P}$ of the complex field in field form and in mode form.
- [ ] Q2 Substitute the $t = 0$ forms (momentum density over $\mathbf p$, gradient over $\mathbf p'$), do the $d^3x$ integral and the delta. How many terms are there?
- [ ] Q3 Show that the annihilator pairs $\hat a_{\mathbf p}\hat b_{-\mathbf p}$ cancel after a relabelling. Which commutator is used?
- [ ] Q4 Relabel the number-conserving terms. Why does an antiparticle of label $\mathbf p$ carry momentum $+\mathbf p$?
- [ ] Q5 **[why]** Compare the mechanism that kills the number-changing terms here with the one for the real field's $\hat{\mathbf P}$.

> [!tip]- Hints: route in the notes
> - Technique: K9, K11.
> - Step 1: derivation steps 1–3; steps 4–5 (annihilator and creator pairs); steps 6–7 (number-conserving terms, reorder).

### The charge counts particles minus antiparticles

$\hat Q = \frac12\int\frac{d^3p}{(2\pi)^3}(\hat a^\dagger_{\mathbf p}\hat a_{\mathbf p} - \hat b^\dagger_{\mathbf p}\hat b_{\mathbf p})$, conserved, see Theorem [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-6|§C2a.5.6]] The Charge Counts Particles Minus Antiparticles.

^nd-thm-c2a-5-6

→ drilled as [[PHY 513 PS Drill#^ps3-2-c|PS3.2(c)]]

### Particles and antiparticles ★

$\hat a^\dagger_{\mathbf p}|0\rangle$ and $\hat b^\dagger_{\mathbf p}|0\rangle$ have the same energy and momentum and opposite charges $\pm\frac12$; a real field admits no phase symmetry, so its quanta are their own antiparticles, see Theorem [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-7|§C2a.5.7]] Particles and Antiparticles. *Source: the user's notes Ch. 4 §4.7–4.8 · Yu eqs. (2.212)–(2.216)*

^nd-thm-c2a-5-7

- [ ] Q1 **[state]** State the quantum numbers of the two species and of a state with $n_a$, $n_b$ quanta.
- [ ] Q2 Use the ladder relations of $\hat H$, $\hat{\mathbf P}$, $\hat Q$ to derive them.
- [ ] Q3 **[why]** Why does a Hermitian field admit no U(1) phase rotation? What does that mean for its quanta?
- [ ] Q4 **[why]** Why do particle and antiparticle have the same mass?

> [!tip]- Hints: route in the notes
> - Technique: K11.
> - Step 1: derivation steps 1–4; [[§C2a.5 The Complex Scalar Field and Its Charge#^rem-c2a-5-3|§C2a.5, Remark: Charge, not probability]] (charge, not probability).

### A state of definite particle number has no mean field ★

If $\hat N|\psi\rangle = n|\psi\rangle$ then $\langle\psi|\hat\phi(x)|\psi\rangle = 0$ for every $x$, however large $n$, see Theorem [[§C2a.6 Coherent States and the Classical Field#^thm-c2a-6-1|§C2a.6.1]] A State of Definite Particle Number Has No Mean Field. *Source: the user's notes Ch. 4 §4.10*

^nd-thm-c2a-6-1

- [ ] Q1 **[state]** State the theorem.
- [ ] Q2 Show that $\hat a^\dagger_{\mathbf p}$ and $\hat a_{\mathbf p}$ shift the eigenvalue of $\hat N$ by $\pm1$.
- [ ] Q3 Conclude by orthogonality of eigenspaces of a Hermitian operator.
- [ ] Q4 **[why]** What kind of state is needed for a nonzero mean field?

> [!tip]- Hints: route in the notes
> - Technique: K11.
> - Step 1: derivation steps 1–4; [[§C2a.6 Coherent States and the Classical Field#^rem-c2a-6-1|§C2a.6, Remark: Why a definite field needs an indefinite particle number]].

### Coherent states are eigenstates of every annihilator

$\hat a_{\mathbf p}|\{\eta\}\rangle = \frac{\eta_{\mathbf p}}{\sqrt{2E_{\mathbf p}}}|\{\eta\}\rangle$ and $\langle\{\eta\}|\{\eta\}\rangle = 1$, see Theorem [[§C2a.6 Coherent States and the Classical Field#^thm-c2a-6-2|§C2a.6.2]] Coherent States Are Eigenstates of Every Annihilator.

^nd-thm-c2a-6-2

→ drilled as [[PHY 513 PS Drill#^ps3-4-a|PS3.4(a)]]–(b)

### A coherent state is the displaced vacuum ★

$\hat D(\eta)$ is unitary, $\hat D^\dagger\hat a_{\mathbf p}\hat D = \hat a_{\mathbf p} + \eta_{\mathbf p}/\sqrt{2E_{\mathbf p}}$, and $\hat D|0\rangle$ is the exponential form, see Theorem [[§C2a.6 Coherent States and the Classical Field#^thm-c2a-6-3|§C2a.6.3]] A Coherent State Is the Displaced Vacuum. *Source: the user's notes Ch. 4 §4.10 (Derivation "Three senses …", part 2)*

^nd-thm-c2a-6-3

- [ ] Q1 **[state]** State the three claims.
- [ ] Q2 Show $\hat D$ is unitary.
- [ ] Q3 Compute $[\hat a_{\mathbf p}, \hat K - \hat K^\dagger]$ and use the Baker–Hausdorff lemma to conjugate $\hat a_{\mathbf p}$.
- [ ] Q4 Split $e^{\hat K - \hat K^\dagger}$ with BCH: which c-number commutator appears, and what is its value?
- [ ] Q5 **[why]** Why do the shifted operators $\hat a_{\mathbf p} - \eta_{\mathbf p}/\sqrt{2E_{\mathbf p}}$ obey the same algebra, and for which state are they annihilators?

> [!tip]- Hints: route in the notes
> - Technique: K11 (BCH).
> - Step 1: derivation steps 1–6.

### The mean field is a classical solution

$\bar\phi(x) = \langle\{\eta\}|\hat\phi(x)|\{\eta\}\rangle = \int\frac{d^3p}{(2\pi)^3\,2E_{\mathbf p}}(\eta_{\mathbf p}e^{-ip\cdot x} + \eta^\ast_{\mathbf p}e^{ip\cdot x})$, a real Klein–Gordon solution, see Theorem [[§C2a.6 Coherent States and the Classical Field#^thm-c2a-6-4|§C2a.6.4]] The Mean Field Is a Classical Solution.

^nd-thm-c2a-6-4

→ drilled as [[PHY 513 PS Drill#^ps3-4-c|PS3.4(c)]]

### Coherent states stay coherent ★

$e^{-i:\hat H:t}|\{\eta_{\mathbf k}\}\rangle = |\{\eta_{\mathbf k}e^{-iE_{\mathbf k}t}\}\rangle$, and the mean field follows the classical solution for all time, see Theorem [[§C2a.6 Coherent States and the Classical Field#^thm-c2a-6-5|§C2a.6.5]] Coherent States Stay Coherent. *Source: the user's notes Ch. 4 §4.10 (Derivation "Three senses …", part 3)*

^nd-thm-c2a-6-5

- [ ] Q1 **[state]** State how the label of a coherent state evolves.
- [ ] Q2 Evolve one creator with $e^{-i\hat Ht}$, then the exponential, using $:\!\hat H\!:|0\rangle = 0$.
- [ ] Q3 **[why]** Why is Ehrenfest's theorem exact here?

> [!tip]- Hints: route in the notes
> - Technique: K11.
> - Step 1: derivation steps 1–5; Theorem [[§C2b.1 Heisenberg Fields#^thm-c2b-1-4|§C2b.1.4]] Time Dependence of the Modes; the Covariant Mode Expansion part 1.

### Poisson number statistics

$\langle\hat N\rangle = \bar N$, $\langle(\Delta\hat N)^2\rangle = \bar N$, $\Delta\hat N/\bar N = 1/\sqrt{\bar N}$, Poisson distribution, see Theorem [[§C2a.6 Coherent States and the Classical Field#^thm-c2a-6-6|§C2a.6.6]] Poisson Number Statistics.

^nd-thm-c2a-6-6

→ drilled as [[PHY 513 PS Drill#^ps3-4-d|PS3.4(d)]]–(e)

### The field fluctuates exactly as in the vacuum ★

$\langle\{\eta\}|(\hat\phi(x) - \bar\phi(x))(\hat\phi(y) - \bar\phi(y))|\{\eta\}\rangle = \langle0|\hat\phi(x)\hat\phi(y)|0\rangle$, independent of the amplitude, see Theorem [[§C2a.6 Coherent States and the Classical Field#^thm-c2a-6-7|§C2a.6.7]] The Field Fluctuates Exactly as in the Vacuum. *Source: the user's notes Ch. 4 §4.10 (Derivation "Three senses …", part 2)*

^nd-thm-c2a-6-7

- [ ] Q1 **[state]** State the theorem.
- [ ] Q2 Displace the field: what is $\hat D^\dagger\hat\phi(x)\hat D$?
- [ ] Q3 Insert $\hat D\hat D^\dagger = 1$ and conclude.
- [ ] Q4 **[why]** At $y = x$ both sides diverge. In which form is the statement an identity between finite numbers?

> [!tip]- Hints: route in the notes
> - Technique: K11.
> - Step 1: derivation steps 1–4; the smeared form is Theorem [[§C2a.6 Coherent States and the Classical Field#^thm-c2a-6-8|§C2a.6.8]] Smeared Fluctuations Are Finite and Independent of the Amplitude.

### Smeared fluctuations are finite and independent of the amplitude ★

For real $f \in \mathcal S$, the variance of $\hat\phi_t(f)$ in a coherent state is $\int d\mu\,|\tilde f|^2$ with $d\mu = d^3p/(2\pi)^32E_{\mathbf p}$, independent of $\eta$ and $t$, while $|\bar\phi_t(f)| \le 2\sqrt{\bar N}(\int d\mu|\tilde f|^2)^{1/2}$, see Theorem [[§C2a.6 Coherent States and the Classical Field#^thm-c2a-6-8|§C2a.6.8]] Smeared Fluctuations Are Finite and Independent of the Amplitude. *Source: the user's notes Ch. 4 §4.10, §4.8*

^nd-thm-c2a-6-8

- [ ] Q1 **[state]** State both parts.
- [ ] Q2 Write $\hat\phi_t(f)$ as one annihilator plus one creator smeared with $g_t$, and compute its vacuum variance.
- [ ] Q3 **[why]** Why does the ratio of mean to fluctuation grow like $\sqrt{\bar N}$, and what regime is that?

> [!tip]- Hints: route in the notes
> - Technique: K11.
> - Step 1: derivation steps 1–5; Theorem [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-7|§C2a.2.7]] The Mode Algebra Smeared.

# T6. Two-point functions, causality, Green's functions and propagators

## Definitions and conventions T6

### Heisenberg field

$\hat\phi(t, \mathbf x) \equiv e^{i\hat Ht}\hat\phi_S(\mathbf x)e^{-i\hat Ht}$, $\hat\pi$ likewise, so $\hat\phi(0, \mathbf x) = \hat\phi_S(\mathbf x)$; states are frozen at $t = 0$, see Definition [[§C2b.1 Heisenberg Fields#^def-c2b-1-1|§C2b.1.1]] Heisenberg Field. *Source: Lecture 5 (Sep 16), transcript ("Schrödinger and Heisenberg pictures") · PS §2.4, eq. (2.43) · the user's notes Ch. 5 §5.1*

^nd-def-c2b-1-1

- [ ] Q1 **[def]** Define the Heisenberg field and momentum density. At which time do the two pictures agree?
- [ ] Q2 Derive the Heisenberg equation $i\partial_t\hat{\mathcal O} = [\hat{\mathcal O}, \hat H]$ from the definition. Why does $\hat H$ itself not change between the pictures?
- [ ] Q3 **[why]** Why does field theory prefer the Heisenberg picture? What singles out time in the Schrödinger picture?

> [!tip]- Hints: route in the notes
> - Technique: K11.
> - Step 1: the definition; [[§C2b.1 Heisenberg Fields#^rem-c2b-1-1|§C2b.1, Remark: Why field theory works in the Heisenberg picture]].

### Wightman function

$D_W(x - y) \equiv \langle0|\hat\phi(x)\hat\phi(y)|0\rangle$, the amplitude for a quantum created at $y$ to be found at $x$, see Definition [[§C2b.2 The Wightman Function#^def-c2b-2-1|§C2b.2.1]] Wightman Function. *Source: Lecture 5 (Sep 16), transcript; Lecture 6 (Sep 21), slide "Cheat Sheet" · PS §2.4, eq. (2.50) · Problem Set 4, eq. (8) · the user's notes Ch. 5 §5.4*

^nd-def-c2b-2-1

- [ ] Q1 **[def]** Define $D_W$, with the order of the two fields.
- [ ] Q2 **[conv]** What does PS call this function, and what letter does the vault reserve for the commutator function instead?
- [ ] Q3 **[why]** Read the definition right to left: which operator acts first, and why is $D_W$ an amplitude for propagation from $y$ to $x$?
- [ ] Q4 **[why]** Why does $D_W$ depend only on $x - y$?

> [!tip]- Hints: route in the notes
> - Technique: none.
> - Step 1: [[§C2b.4 Microcausality and the Commutator Function#^cau-c2b-4-1|§C2b.4, Caution: One letter, four objects]]; register row "Green's functions"; [[§C2a.4 Particles and Relativistic Normalization#^rem-c2a-4-2|§C2a.4, Remark: Why ¦0⟩ is the vacuum]] (Poincaré-invariant vacuum).

### Microcausality

Local observables at spacelike separation commute; for observables built from $\hat\phi$, $[\hat\phi(x), \hat\phi(y)] = 0$ for $(x - y)^2 < 0$ suffices, see Principle [[§C2b.4 Microcausality and the Commutator Function#^pr-c2b-4-1|§C2b.4.1]] Microcausality. *Source: Lecture 5 (Sep 16), transcript ("causality clarified") · PS §2.4, p. 28 · the user's notes Ch. 5 §5.5*

^nd-pr-c2b-4-1

- [ ] Q1 **[state]** State the principle, and the extra condition for a complex field.
- [ ] Q2 **[why]** Why is the criterion a vanishing commutator and not a vanishing amplitude? Is $D_W$ zero outside the light cone?
- [ ] Q3 **[why]** Why can spacelike-separated events not be ordered invariantly, and why does that require commuting measurements?

> [!tip]- Hints: route in the notes
> - Technique: K14.
> - Step 1: [[§C2b.4 Microcausality and the Commutator Function#^rem-c2b-4-1|§C2b.4, Remark: Why the criterion is a commutator, not an amplitude]]; Theorem [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-3|§C2b.3.3]] The Wightman Function at Spacelike Separation ($D_W \neq 0$ at spacelike separation).

### Commutator function

$iD(x - y) \equiv \langle0|[\hat\phi(x), \hat\phi(y)]|0\rangle$ (Pauli–Jordan function), see Definition [[§C2b.4 Microcausality and the Commutator Function#^def-c2b-4-1|§C2b.4.1]] Commutator Function. *Source: Problem Set 4, eq. (9) · the user's notes Ch. 5 §5.5*

^nd-def-c2b-4-1

- [ ] Q1 **[def]** Define $D$, including the factor $i$.
- [ ] Q2 **[conv]** Yu calls the commutator itself the Pauli–Jordan function. How is his $D_{\mathrm{PJ}}$ related to $D$?
- [ ] Q3 **[why]** Why may the vacuum expectation value be dropped in the definition, i.e. why is $iD = [\hat\phi(x), \hat\phi(y)]$ as an operator?

> [!tip]- Hints: route in the notes
> - Technique: K11.
> - Step 1: Theorem [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-2|§C2b.4.2]] The Field Commutator Is a c-Number; [[§C2b.4 Microcausality and the Commutator Function#^cau-c2b-4-1|§C2b.4, Caution: One letter, four objects]].

### Hadamard function

$D_1(x - y) \equiv \langle0|\{\hat\phi(x), \hat\phi(y)\}|0\rangle$, see Definition [[§C2b.4 Microcausality and the Commutator Function#^def-c2b-4-2|§C2b.4.2]] Hadamard Function. *Source: Problem Set 4, eq. (10) · the user's notes Ch. 5 §5.5*

^nd-def-c2b-4-2

- [ ] Q1 **[def]** Define $D_1$.
- [ ] Q2 **[why]** Unlike the commutator, the anticommutator of two free fields is not a c-number. Why, and why does that make the vacuum expectation value essential here?
- [ ] Q3 **[why]** Which question does $D_1$ answer, as opposed to $D$ (influence or correlation)?

> [!tip]- Hints: route in the notes
> - Technique: none.
> - Step 1: [[§C2b.4 Microcausality and the Commutator Function#^rem-c2b-4-3|§C2b.4, Remark: Influence and correlation]] (influence and correlation).

### One letter, four objects

PS's $D(x - y)$ is the vault's $D_W$; PS name neither $D$ nor $D_1$; Yu's $D_{\mathrm{PJ}} = iD$; the Lecture 6 slides write a bare $D$ for a generic Green's function $D_C$, see [[§C2b.4 Microcausality and the Commutator Function#^cau-c2b-4-1|§C2b.4, Caution: One letter, four objects]]. *Source: Problem Set 4, Problem 2 ("Beware that PS uses an imprecise notation") · Lecture 6 (Sep 21) · Yu eq. (6.111)*

^nd-cau-c2b-4-1

- [ ] Q1 **[def]** For each of $D_W$, $D$, $D_1$, $D_C$: what do PS, Yu, Problem Set 4 and the Lecture 6 slides write?
- [ ] Q2 **[conv]** PS eq. (2.53) writes the field commutator as "$D(x - y) - D(y - x)$". Rewrite it in the vault's names.
- [ ] Q3 **[why]** Why does Problem Set 4 insist on the more precise notation?

> [!tip]- Hints: route in the notes
> - Technique: none.
> - Step 1: the caution box; register row "Green's functions".

### Scalar field with a classical source

$\mathcal L = \frac12(\partial\phi)^2 - \frac12m^2\phi^2 + j\phi$, so $(\partial^2 + m^2)\phi = j$, with $j$ external, smooth and of finite duration, see Model [[§C2b.5 Green's Functions and Contours#^mod-c2b-5-1|§C2b.5.1]] Scalar Field with a Classical Source. *Source: Lecture 6 (Sep 21), slide "External Sources" · PS §2.4, eqs. (2.61)–(2.62) · the user's notes Ch. 6 §6.1*

^nd-mod-c2b-5-1

- [ ] Q1 **[def]** Write the Lagrangian and the field equation, with the sign of the source term.
- [ ] Q2 Check the sign: derive the Euler–Lagrange equation from $\mathcal L$.
- [ ] Q3 **[why]** What does "external" mean here, and what will replace $j$ later?

> [!tip]- Hints: route in the notes
> - Technique: none (Euler–Lagrange, Theorem [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-4|§C1b.2.4]] Euler–Lagrange Equations for Fields).
> - Step 1: the model box; Lecture 6, "Beyond free fields: interactions".

### Green's function of the Klein–Gordon operator

$(\partial_x^2 + m^2)D_C(x - y) = -i\delta^4(x - y)$; then $\phi = \phi_0 + i\int d^4y\,D_C(x - y)j(y)$ solves the sourced equation for every $j$, see Definition [[§C2b.5 Green's Functions and Contours#^def-c2b-5-1|§C2b.5.1]] Green's Function of the Klein–Gordon Operator. *Source: Lecture 6 (Sep 21), slide "Definition of Green's Functions" ("Proof: act with … and use linearity") · PS §2.4, eq. (2.56) · Problem Set 4, Problem 0 · the user's notes Ch. 6 §6.1*

^nd-def-c2b-5-1

- [ ] Q1 **[def]** Write the defining equation with its normalization, and the solution formula for a source $j$.
- [ ] Q2 Verify the solution formula: act with $\partial_x^2 + m^2$ and use the defining equation (the slide's proof).
- [ ] Q3 **[conv]** Problem Set 4 (Problem 0) writes the defining equation without the $i$. How do the two normalizations differ, and which one is PS's? What normalization do Dirac Green's functions use?
- [ ] Q4 **[why]** Why is a Green's function not unique, and what labels the choice?
- [ ] Q5 **[why]** In the language of generalized functions, what is the Green's "function" really?

> [!tip]- Hints: route in the notes
> - Technique: none.
> - Step 1: [[§C2b.5 Green's Functions and Contours#^rem-c2b-5-1|§C2b.5, Remark: What a Green's "function" is, and why it is not unique]] (the check, non-uniqueness); Definition [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^def-ca-6-1|§CA.6.1]] Fundamental Solution; Theorem [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-8|§CA.6.8]] Convolution with a Fundamental Solution Solves the Sourced Equation.
> - Step 2: the Dirac normalization: P2, "Pitfalls" (the Dirac normalization is $+i\delta^4$).

### The Green's function of a contour

For a contour $C$ in the $p^0$-plane that follows the real axis except near $p^0 = \pm E_{\mathbf p}$, $D_C(\xi) = \int\frac{d^3p}{(2\pi)^3}e^{i\mathbf p\cdot\boldsymbol\xi}\int_C\frac{dp^0}{2\pi}\frac{ie^{-ip^0\xi^0}}{(p^0)^2 - E_{\mathbf p}^2}$, see Definition [[§C2b.5 Green's Functions and Contours#^def-c2b-5-2|§C2b.5.2]] The Green's Function of a Contour. *Source: Lecture 6 (Sep 21), slides "Important Mathematical Limitation", "Green's functions and Complex Contours" · the user's notes Ch. 6 §6.4*

^nd-def-c2b-5-2

- [ ] Q1 **[def]** Write $D_C$ as an iterated integral, with the $p^0$ integral along $C$.
- [ ] Q2 **[why]** Why does $\int\frac{d^4p}{(2\pi)^4}\frac{ie^{-ip\cdot\xi}}{p^2 - m^2}$ mean nothing without a contour?
- [ ] Q3 **[why]** How many inequivalent choices are there, and which two did Lecture 6 compute?

> [!tip]- Hints: route in the notes
> - Technique: K13 (contours).
> - Step 1: [[§C2b.5 Green's Functions and Contours#^rem-c2b-5-2|§C2b.5, Remark: The pole problem; two problems that are one]] (the pole problem); P2, steps 2–3.

### Principal-value Green's function

$\bar D \equiv \frac12(D_R + D_A)$, the average of the retarded and advanced functions, itself a Green's function, see Definition [[§C2b.5 Green's Functions and Contours#^def-c2b-5-3|§C2b.5.3]] Principal-Value Green's Function. *Source: the user's notes Ch. 6 §6.11*

^nd-def-c2b-5-3

- [ ] Q1 **[def]** Define $\bar D$.
- [ ] Q2 **[why]** Why is the average of two Green's functions again a Green's function, while their difference is not?
- [ ] Q3 What is its momentum-space transform, and why is it called "principal value"?

> [!tip]- Hints: route in the notes
> - Technique: K13.
> - Step 1: Theorem [[§C2b.7 Wick Rotation and the Two-Point Family#^thm-c2b-7-5|§C2b.7.5]] Relations in the Two-Point Family part 1; table in [[§C2b.7 Wick Rotation and the Two-Point Family#^rem-c2b-7-2|§C2b.7, Remark: The two-point functions at a glance]].

### Time-ordered product

$T\{\hat\phi(x)\hat\phi(y)\} \equiv \theta(x^0 - y^0)\hat\phi(x)\hat\phi(y) + \theta(y^0 - x^0)\hat\phi(y)\hat\phi(x)$, the later operator to the left, with $\theta(0) = \frac12$, see Definition [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^def-c2b-6-1|§C2b.6.1]] Time-Ordered Product. *Source: Lecture 6 (Sep 21), slide "Green's Functions and Boundary Conditions" · PS §2.4, eq. (2.60) · Yu eq. (6.108) · the user's notes Ch. 5 §5.6*

^nd-def-c2b-6-1

- [ ] Q1 **[def]** Define the time-ordered product of two fields and of $n$ fields.
- [ ] Q2 **[conv]** Which value of $\theta(0)$ does the definition need, and why? What does Problem Set 3's $\theta(0) = 1$ give at equal times?
- [ ] Q3 **[conv]** How do the vault, PS and Yu bracket the time-ordered product?
- [ ] Q4 **[why]** Why does the later operator stand to the left?

> [!tip]- Hints: route in the notes
> - Technique: none.
> - Step 1: [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^cau-c2b-6-1|§C2b.6, Caution: The step function at zero]] (the step function at zero); [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^cau-c2b-6-3|§C2b.6, Caution: Names for the time-ordered product]] (names); [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^rem-c2b-6-1|§C2b.6, Remark: Why the later operator stands to the left]] (why later to the left).

### Anti-time-ordered product

$\bar T\{\hat\phi(x)\hat\phi(y)\} \equiv \theta(y^0 - x^0)\hat\phi(x)\hat\phi(y) + \theta(x^0 - y^0)\hat\phi(y)\hat\phi(x)$, the earlier operator to the left, see Definition [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^def-c2b-6-2|§C2b.6.2]] Anti-Time-Ordered Product. *Source: the user's notes Ch. 6 §6.11*

^nd-def-c2b-6-2

- [ ] Q1 **[def]** Define $\bar T$.
- [ ] Q2 Which Green's function is minus its vacuum expectation value, and which contour belongs to it?
- [ ] Q3 **[why]** How is $\langle0|\bar T\{\hat\phi(x)\hat\phi(y)\}|0\rangle$ related to the complex conjugate of $\langle0|T\{\hat\phi(x)\hat\phi(y)\}|0\rangle$?

> [!tip]- Hints: route in the notes
> - Technique: none.
> - Step 1: Theorem [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-3|§C2b.6.3]] The Anti-Feynman Function; Theorem [[§C2b.7 Wick Rotation and the Two-Point Family#^thm-c2b-7-5|§C2b.7.5]] Relations in the Two-Point Family part 2.

### Signs that slip

$D_F(x - y) = D_R(x - y) + D_W(y - x)$ (arguments exchanged); $(\partial^2 + m^2)e^{-ip\cdot x} = (m^2 - p^2)e^{-ip\cdot x}$; closing a contour upward is always counterclockwise, see [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^cau-c2b-6-2|§C2b.6, Caution: Signs that slip]]. *Source: Lecture 6 (Sep 21), slides "Evaluation of the Feynman Propagator", "Green's Functions and Boundary Conditions" · the user's notes Ch. 6 §6.7*

^nd-cau-c2b-6-2

- [ ] Q1 **[state]** Write the relation between $D_F$ and $D_R$ with the correct argument of $D_W$. What goes wrong for $t < 0$ with the other argument?
- [ ] Q2 **[conv]** Compute $(\partial_t^2 - \nabla^2 + m^2)e^{-iEt + i\mathbf p\cdot\mathbf x}$. Which combination vanishes on shell?
- [ ] Q3 **[conv]** The Lecture 6 slide calls the loop for $x^0 < y^0$ "clockwise". Which orientation is it, and what is the sign relative to the retarded case?

> [!tip]- Hints: route in the notes
> - Technique: K13.
> - Step 1: the caution box; P2, "Pitfalls" (orientation, exchanged arguments, the sign of the operator).

### Euclidean propagator

$D_E(x_E) \equiv \int\frac{d^4p_E}{(2\pi)^4}\frac{e^{ip_E\cdot x_E}}{p_E^2 + m^2}$ with $x_E = (\tau, \mathbf x)$, Euclidean products; its denominator never vanishes, see Definition [[§C2b.7 Wick Rotation and the Two-Point Family#^def-c2b-7-1|§C2b.7.1]] Euclidean Propagator. *Source: Lecture 6 (Sep 21), slide "Another perspective: the Euclidean Green's Function" · the user's notes Ch. 2 §2.2, Ch. 6 §6.10*

^nd-def-c2b-7-1

- [ ] Q1 **[def]** Define $D_E$.
- [ ] Q2 **[why]** Why has the Euclidean integrand no poles on the real $p_4$ axis?
- [ ] Q3 What is its value as a function of $R = |x_E|$, and which theorem computes it?
- [ ] Q4 **[conv]** The slides write $p^0_E = ip^0_M$; the vault rotates $p^0 = ip_4$. Are they the same convention?

> [!tip]- Hints: route in the notes
> - Technique: K13.
> - Step 1: Theorem [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-1|§C2b.3.1]] The Wightman Function at Imaginary Time; [[§C2b.7 Wick Rotation and the Two-Point Family#^rem-c2b-7-1|§C2b.7, Remark: Why the Feynman contour is singled out]].

### Test functions: the spaces 𝒟 and 𝒮

$\mathcal D(\mathbb R^n)$: smooth functions vanishing outside a bounded set; $\mathcal S(\mathbb R^n)$: smooth functions with every seminorm $\sup|x^\alpha\partial^\beta\varphi|$ finite; with their notions of convergence, see Definition [[§CA.2 Generalized Functions#^def-ca-2-1|§CA.2.1]] Test Functions: the Spaces 𝒟 and 𝒮. *Source: Problem Set 4, Problem 0 · the user's notes App. A §A.4*

^nd-def-ca-2-1

- [ ] Q1 **[def]** Define $\mathcal D$ and $\mathcal S$ and convergence in each.
- [ ] Q2 Give a function in $\mathcal D(\mathbb R)$ and one in $\mathcal S$ but not in $\mathcal D$.
- [ ] Q3 **[why]** Which test functions does Problem Set 4 (Problem 0) use, and why are the sources of physics test functions?

> [!tip]- Hints: route in the notes
> - Technique: none.
> - Step 1: the definition; Theorem [[§CA.2 Generalized Functions#^thm-ca-2-1|§CA.2.1]] Regular and Singular Tempered Distributions part 1 (density of $\mathcal D$ in $\mathcal S$); Theorem [[§C2b.8 Particle Production by a Classical Source#^thm-c2b-8-4|§C2b.8.4]] The Source Is a Test Function; Why $\bar N$ Is Finite.

### Generalized function; tempered distribution

A generalized function is a continuous linear map $\varphi \mapsto T[\varphi]$ on test functions; a locally integrable function defines one by $\varphi \mapsto \int\psi\varphi$; a tempered distribution acts on $\mathcal S$, see Definition [[§CA.2 Generalized Functions#^def-ca-2-2|§CA.2.2]] Generalized Function; Tempered Distribution. *Source: Problem Set 4, Problem 0 · the user's notes App. A §A.4, Ch. 6 §6.2*

^nd-def-ca-2-2

- [ ] Q1 **[def]** Define a generalized function and a tempered distribution.
- [ ] Q2 Write $\delta$ and the constant function as generalized functions, as Problem Set 4 does.
- [ ] Q3 **[why]** Why is $\delta$ not a function in the ordinary sense, and in what sense does a generalized function "include" ordinary functions?

> [!tip]- Hints: route in the notes
> - Technique: none.
> - Step 1: the definition; Theorem [[§CA.2 Generalized Functions#^thm-ca-2-1|§CA.2.1]] Regular and Singular Tempered Distributions; [[§CA.2 Generalized Functions#^rem-ca-2-1|§CA.2, Remark: What changes from the working delta function]].

### Support and singular support

$\operatorname{supp}T$ is the complement of the largest open set on which $T$ vanishes; $\operatorname{sing\,supp}T$ the complement of the largest open set on which $T$ is a smooth function, see Definition [[§CA.2 Generalized Functions#^def-ca-2-3|§CA.2.3]] Support and Singular Support.

^nd-def-ca-2-3

- [ ] Q1 **[def]** Define both.
- [ ] Q2 Give support and singular support of $\delta$, $\theta$ and $\mathcal P\frac1x$.
- [ ] Q3 **[why]** Which of the two is the precise form of microcausality for $D$, and which describes the light-cone singularity of $D_W$?

> [!tip]- Hints: route in the notes
> - Technique: none.
> - Step 1: the definition's examples; Theorem [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-6|§C2b.4.6]] Microcausality as a Support Statement; Theorem [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-6|§C2b.3.6]] The Wightman Function as a Distribution: Off the Cone and on It part 2.

### Derivative of a generalized function; product with a smooth function

$T'[\varphi] \equiv -T[\varphi']$, $\partial_\mu T[\varphi] \equiv -T[\partial_\mu\varphi]$; $(gT)[\varphi] \equiv T[g\varphi]$ for smooth $g$, see Definition [[§CA.2 Generalized Functions#^def-ca-2-4|§CA.2.4]] Derivative of a Generalized Function, Definition [[§CA.2 Generalized Functions#^def-ca-2-5|§CA.2.5]] Product of a Generalized Function with a Smooth Function.

^nd-def-ca-2-4

- [ ] Q1 **[def]** Define the derivative and the product with a smooth function.
- [ ] Q2 Show that the definition of the derivative agrees with integration by parts for a differentiable $\psi$.
- [ ] Q3 **[why]** Why can two generalized functions not be multiplied in general? Give an example of a product that has no value.

> [!tip]- Hints: route in the notes
> - Technique: none.
> - Step 1: Theorem [[§CA.2 Generalized Functions#^thm-ca-2-4|§CA.2.4]] Every Generalized Function Is Differentiable; Theorem [[§CA.2 Generalized Functions#^thm-ca-2-8|§CA.2.8]] Products with Disjoint Singular Supports part 3; Theorem [[§CA.2 Generalized Functions#^thm-ca-2-9|§CA.2.9]] Products Without a Value: θ·δ, δ² and δ(0).

### Distributional limit; Fourier transform of a generalized function

$T_\varepsilon \to T$ means $T_\varepsilon[\varphi] \to T[\varphi]$ for every test function; $\tilde T[\varphi] \equiv T[\tilde\varphi]$, see Definition [[§CA.2 Generalized Functions#^def-ca-2-6|§CA.2.6]] Distributional Limit, Definition [[§CA.2 Generalized Functions#^def-ca-2-7|§CA.2.7]] Fourier Transform of a Generalized Function.

^nd-def-ca-2-6

- [ ] Q1 **[def]** Define both.
- [ ] Q2 What is the distributional meaning of "$\varepsilon \to 0^+$ at the end" in an $i\varepsilon$ expression?
- [ ] Q3 **[why]** Why may a limit be taken before or after Fourier transforming?

> [!tip]- Hints: route in the notes
> - Technique: K13.
> - Step 1: Theorem [[§CA.2 Generalized Functions#^thm-ca-2-5|§CA.2.5]] Distributional Limits; Theorem [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-2|§CA.3.2]] The Fourier Transform of Tempered Distributions part 2; Theorem [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-10|§C2b.6.10]] The $i\varepsilon$ Prescription Is a Limit in 𝒮′.

### Linear change of variables; invariant distribution

$T(Ax + a)[\varphi] \equiv |\det A|^{-1}T[\varphi(A^{-1}(\cdot - a))]$; $T$ is Lorentz invariant if $T[\varphi\circ\Lambda^{-1}] = T[\varphi]$ for every proper orthochronous $\Lambda$, see Definition [[§CA.2 Generalized Functions#^def-ca-2-8|§CA.2.8]] Linear Change of Variables, Definition [[§CA.2 Generalized Functions#^def-ca-2-9|§CA.2.9]] Invariant Distribution.

^nd-def-ca-2-8

- [ ] Q1 **[def]** Define both.
- [ ] Q2 Derive $\delta(\lambda x) = |\lambda|^{-n}\delta(x)$ from the definition.
- [ ] Q3 **[why]** Why can Lorentz invariance of $D_W$ not be stated pointwise on the light cone?

> [!tip]- Hints: route in the notes
> - Technique: K14.
> - Step 1: Theorem [[§CA.2 Generalized Functions#^thm-ca-2-6|§CA.2.6]] Composition of δ with a Function part 1; Theorem [[§C2b.2 The Wightman Function#^thm-c2b-2-3|§C2b.2.3]] Lorentz Invariance of the Wightman Function.

### Principal value

For a test function $\varphi$, $\mathcal P\int\frac{\varphi(s)}{s}ds \equiv \lim_{\delta\to0^+}(\int_{-\infty}^{-\delta} + \int_\delta^\infty)\frac{\varphi(s)}{s}ds$, a real, odd generalized function, see Definition [[§CA.2 Generalized Functions#^def-ca-2-10|§CA.2.10]] Principal Value.

^nd-def-ca-2-10

- [ ] Q1 **[def]** Define $\mathcal P\frac1s$, and give its equivalent form with $\varphi(s) - \varphi(0)$.
- [ ] Q2 **[why]** Why is $1/s$ alone not a distribution on $\mathbb R$?
- [ ] Q3 Where do principal values appear in the two-point family?

> [!tip]- Hints: route in the notes
> - Technique: K13.
> - Step 1: Theorem [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-2|§CA.6.2]] Sokhotski–Plemelj Formula; Theorem [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-8|§C2b.4.8]] Commutator and Hadamard Functions of the Massless Field ($D_1$ massless); Definition [[§C2b.5 Green's Functions and Contours#^def-c2b-5-3|§C2b.5.3]] Principal-Value Green's Function.

### Operator-valued distribution

A map $f \mapsto \Phi(f)$ from $\mathcal S(\mathbb R^n)$ to operators on a dense invariant domain, linear in $f$, with every matrix element a tempered distribution, see Definition [[§CA.2 Generalized Functions#^def-ca-2-11|§CA.2.11]] Operator-Valued Distribution.

^nd-def-ca-2-11

- [ ] Q1 **[def]** Define an operator-valued distribution.
- [ ] Q2 Which fields of C2a–C2b are operator-valued distributions, on which space (three or four dimensions)?
- [ ] Q3 **[why]** What does the kernel theorem add: in which sense is a two-point formula an identity between kernels?

> [!tip]- Hints: route in the notes
> - Technique: none.
> - Step 1: Definition [[§C2a.1 Canonical Quantization of Fields#^def-c2a-1-1|§C2a.1.1]] Smeared Field Operators; Theorem [[§C2b.1 Heisenberg Fields#^thm-c2b-1-6|§C2b.1.6]] The Heisenberg Field Is an Operator-Valued Distribution on Spacetime; Theorem [[§CA.2 Generalized Functions#^thm-ca-2-11|§CA.2.11]] The Kernel Theorem.

### Fourier conventions in space and spacetime

$f(\mathbf x) = \int\frac{d^3k}{(2\pi)^3}\tilde f(\mathbf k)e^{i\mathbf k\cdot\mathbf x}$, $f(x) = \int\frac{d^4p}{(2\pi)^4}\tilde f(p)e^{-ip\cdot x}$; all $2\pi$'s with the momentum integral, see Definition [[§CA.3 Fourier Transforms and Fourier Tricks#^def-ca-3-1|§CA.3.1]] Fourier Transform in Space and Spacetime, [[§CA.3 Fourier Transforms and Fourier Tricks#^cau-ca-3-1|§CA.3, Caution: Two conventions in the vault]]. *Source: register row "Fourier transform (4d)" · PS and Yu same*

^nd-def-ca-3-1

- [ ] Q1 **[def]** Write the forward and inverse transforms in space and in spacetime.
- [ ] Q2 **[conv]** Why do time and space carry opposite signs in $e^{-ip\cdot x}$? Which convention does Waves and Optics use instead, and why?
- [ ] Q3 **[conv]** Where do the factors of $2\pi$ go in $\int d^3x\,e^{i\mathbf k\cdot\mathbf x}$ and in the measures $d^3p/(2\pi)^3$, $d^4p/(2\pi)^4$?

> [!tip]- Hints: route in the notes
> - Technique: none.
> - Step 1: the definition; [[§CA.3 Fourier Transforms and Fourier Tricks#^cau-ca-3-1|§CA.3, Caution: Two conventions in the vault]]; Theorem [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|§CA.3.3]] Plane Waves Integrate to a Delta Function.

### Contour, analytic function, isolated singularities and residues

A contour integral $\int_\gamma f\,dz = \int_a^bf(z(s))z'(s)ds$; analytic means complex-differentiable (Cauchy–Riemann); poles and essential singularities from the Laurent expansion; the residue is the coefficient $a_{-1}$, see Definition [[§CA.4 Contour Integration#^def-ca-4-1|§CA.4.1]] Contour; Contour Integral, Definition [[§CA.4 Contour Integration#^def-ca-4-2|§CA.4.2]] Analytic Function, Definition [[§CA.4 Contour Integration#^def-ca-4-4|§CA.4.4]] Laurent Expansion; Removable Singularity, Pole and Essential Singularity, Definition [[§CA.4 Contour Integration#^def-ca-4-5|§CA.4.5]] Residue. *Source: Problem Set 4, Problem 1 · Lecture 6 (Sep 21), slide "Complex Analysis: a Survival Guide"*

^nd-def-ca-4-5

- [ ] Q1 **[def]** Define a contour integral, an analytic function, a pole of order $k$ and the residue.
- [ ] Q2 Show that $\bar z$ is not analytic.
- [ ] Q3 **[why]** Why is the residue not the value of $f$ at the pole? Which term of the Laurent series does a closed loop detect?
- [ ] Q4 **[why]** Why is a branch point not an isolated singularity, so that it has no residue?

> [!tip]- Hints: route in the notes
> - Technique: K13.
> - Step 1: [[§CA.4 Contour Integration#^rem-ca-4-1|§CA.4, Remark: What a residue is]]; Theorem [[§CA.4 Contour Integration#^thm-ca-4-1|§CA.4.1]] The ML Inequality and the Basic Integral part 2; Theorem [[§CA.4 Contour Integration#^thm-ca-4-8|§CA.4.8]] Integrals around a Branch Cut.

### Modified Bessel function of the second kind

$K_\nu(z) = \int_0^\infty du\,e^{-z\cosh u}\cosh(\nu u)$ for $\operatorname{Re}z > 0$, so $\int_{-\infty}^\infty du\,\cosh u\,e^{-z\cosh u} = 2K_1(z)$, see Definition [[§CA.5 Gaussian Integrals, Stationary Phase and Bessel Functions#^def-ca-5-1|§CA.5.1]] Modified Bessel Function of the Second Kind. *Source: Problem Set 4, Problem 3 · PS §2.4, eq. (2.52)*

^nd-def-ca-5-1

- [ ] Q1 **[def]** Write the integral representation of $K_\nu$.
- [ ] Q2 What are the small- and large-argument behaviours of $K_1$?
- [ ] Q3 **[why]** Which physical features of the spacelike Wightman function do the two ends of $K_1$ encode?

> [!tip]- Hints: route in the notes
> - Technique: none.
> - Step 1: Theorem [[§CA.5 Gaussian Integrals, Stationary Phase and Bessel Functions#^thm-ca-5-3|§CA.5.3]] Properties of $K_\nu$ parts 2–3; Theorem [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-3|§C2b.3.3]] The Wightman Function at Spacelike Separation.

### Fundamental solution

A distribution $G$ with $P(\partial)G = -i\delta^n$; for Klein–Gordon $(\partial^2 + m^2)G = -i\delta^4$, the PS normalization, see Definition [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^def-ca-6-1|§CA.6.1]] Fundamental Solution.

^nd-def-ca-6-1

- [ ] Q1 **[def]** Define a fundamental solution and state what $P(\partial)G = -i\delta^n$ means on test functions.
- [ ] Q2 **[conv]** Which factor fixes the normalization, and how is it undone in the solution formula $\phi = iG[j(x - \cdot)]$?
- [ ] Q3 **[why]** Why do two fundamental solutions differ by a homogeneous solution, and where is its transform supported?

> [!tip]- Hints: route in the notes
> - Technique: none.
> - Step 1: Theorem [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-7|§CA.6.7]] Fundamental Solutions Differ by Homogeneous Solutions; Theorem [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-8|§CA.6.8]] Convolution with a Fundamental Solution Solves the Sourced Equation.

### What the Sokhotski–Plemelj formula does and does not say

$\frac{1}{x - x_0 \pm i\varepsilon} \to \mathcal P\frac{1}{x - x_0} \mp i\pi\delta(x - x_0)$ is empty pointwise; its content sits at $x = x_0$, so an $i\varepsilon$ expression may be set to $\varepsilon = 0$ wherever the denominator does not vanish, see [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^cau-ca-6-1|§CA.6, Caution: What the formula does and does not say]].

^nd-cau-ca-6-1

- [ ] Q1 **[state]** State the formula with the correct signs.
- [ ] Q2 **[conv]** Mnemonic: a pole of $1/(x - x_0 - i\varepsilon)$ lies on which side of the real path, and which sign of $i\pi$ does it give?
- [ ] Q3 **[why]** What does the formula say at $x \neq x_0$? Why is that the reason "only the sign of $i\varepsilon$ matters, and only near the poles"?

> [!tip]- Hints: route in the notes
> - Technique: K13.
> - Step 1: Theorem [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-2|§CA.6.2]] Sokhotski–Plemelj Formula; P2, "Pitfalls" (only the sign of $i\varepsilon$ matters).

### Jordan's lemma needs g → 0

Jordan's lemma requires the non-exponential factor to tend to zero on the arc (no rate needed); a regulator such as $e^{-\varepsilon p}$ may not be kept on the arc, see [[§CA.4 Contour Integration#^cau-ca-4-1|§CA.4, Caution: Jordan's lemma needs g → 0]].

^nd-cau-ca-4-1

- [ ] Q1 **[state]** State Jordan's lemma and its hypothesis.
- [ ] Q2 For the equal-time Wightman integrand $pe^{ipr}/\sqrt{p^2 + m^2}$, does the lemma apply? What trick cures it?
- [ ] Q3 **[why]** Why can a damping $e^{-\varepsilon p}$ not be kept on the large arc?

> [!tip]- Hints: route in the notes
> - Technique: K13.
> - Step 1: Theorem [[§CA.4 Contour Integration#^thm-ca-4-6|§CA.4.6]] Closing the Contour: the ML Estimate and Jordan's Lemma part 2; second route of Theorem [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-3|§C2b.3.3]] The Wightman Function at Spacelike Separation.

## Derivations T6

### The equal-time relations hold at every time ★★

For every $t$, $[\hat\phi(t, \mathbf x), \hat\pi(t, \mathbf y)] = i\delta^3(\mathbf x - \mathbf y)$ and the other two vanish; nothing is asserted for two different times, see Theorem [[§C2b.1 Heisenberg Fields#^thm-c2b-1-1|§C2b.1.1]] The Equal-Time Relations Hold at Every Time. *Source: Lecture 5 (Sep 16), transcript ("equal-time field-field commutators vanish … valid only at the same time") · PS §2.4, eqs. (2.44)–(2.45) · the user's notes Ch. 5 §5.2*

^nd-thm-c2b-1-1

- [ ] Q1 **[state]** State the theorem and what it does not assert.
- [ ] Q2 Sandwich the Schrödinger commutator between $e^{i\hat Ht}$ and $e^{-i\hat Ht}$: what happens to the left side and to the c-number right side?
- [ ] Q3 **[why]** Which property of $e^{i\hat Ht}$ is used, and does the result depend on the form of $\hat H$ (free or interacting)?
- [ ] Q4 **[why]** Why may $(-\nabla^2 + m^2)\hat\phi$ not be replaced by $-\partial_t^2\hat\phi$ inside an equal-time commutator?

> [!tip]- Hints: route in the notes
> - Technique: K11.
> - Step 1: derivation steps 1–3.
> - Step 2: [[§C2b.1 Heisenberg Fields#^cau-c2b-1-1|§C2b.1, Caution: Equal times only]] (equal times only).

### The Heisenberg equations are the Klein–Gordon equation ★★ [class exercise, Lecture 5]

With the field form of $\hat H$ and the equal-time relations, $i\partial_t\hat{\mathcal O} = [\hat{\mathcal O}, \hat H]$ gives $\partial_t\hat\phi = \hat\pi$ and $\partial_t\hat\pi = (\nabla^2 - m^2)\hat\phi$, hence $(\partial^2 + m^2)\hat\phi = 0$, see Theorem [[§C2b.1 Heisenberg Fields#^thm-c2b-1-2|§C2b.1.2]] The Heisenberg Equations Are the Klein–Gordon Equation. Larsen: "it's very instructive to go and check this … let me not go there [the mode form]. Let me just use the actual Hamiltonian"; the user's notes: "the exercise is to see the equation of motion emerge from the canonical structure". The complex-field version is part of PS3.2(a2). *Source: Lecture 5 (Sep 16), transcript · PS §2.4, eqs. (2.44)–(2.45) · the user's notes Ch. 5 §5.2*

^nd-thm-c2b-1-2

- [ ] Q1 **[state]** State the two first-order equations and the resulting field equation.
- [ ] Q2 Compute $[\hat\phi(\mathbf x), \hat\pi(\mathbf x')^2]$ at equal times. Why are the two terms of the product rule equal?
- [ ] Q3 **[why]** Why does $\hat\phi(\mathbf x)$ commute with $(\nabla'\hat\phi(\mathbf x'))^2$, while the analogous move on $[\hat\phi, \hat\pi]$ would give $\nabla\delta^3$?
- [ ] Q4 Integrate over $\mathbf x'$ and read off $\partial_t\hat\phi$.
- [ ] Q5 For $\hat\pi$: rewrite the gradient term by integrating by parts, then commute $\hat\pi(\mathbf x)$ with the two terms. Which boundary assumption is used?
- [ ] Q6 Combine the two equations. Where is the mode expansion used in this derivation?
- [ ] Q7 **[why]** These are Hamilton's equations of the classical field. Which classical theorem is their counterpart?

> [!tip]- Hints: route in the notes
> - Technique: K11 (commutator algebra), K2.
> - Step 1: derivation steps 1–4 ($\hat\phi$ against the three terms); steps 5–7 (gradient term, $\hat\pi$ against two terms, integrate); step 8 (combine).
> - Step 2: classical counterpart Theorem [[§C1b.4 Hamiltonian Field Theory#^thm-c1b-4-4|§C1b.4.4]] Hamilton's Equations for Fields; [[§C2b.1 Heisenberg Fields#^cau-c2b-1-1|§C2b.1, Caution: Equal times only]].

### Free fields live on the mass shell ★

If $(\partial^2 + m^2)f = 0$ then $\tilde f(p) = 2\pi\delta(p^2 - m^2)g(p)$ and $f = \int\frac{d^3p}{(2\pi)^3\,2E_{\mathbf p}}[g(p)e^{-ip\cdot x} + g(-p)e^{ip\cdot x}]_{p^0 = E_{\mathbf p}}$, see Theorem [[§C2b.1 Heisenberg Fields#^thm-c2b-1-3|§C2b.1.3]] Free Fields Live on the Mass Shell. *Source: the user's notes Ch. 6 §6.3–6.4 · PS §2.4, eqs. (2.57)–(2.58)*

^nd-thm-c2b-1-3

- [ ] Q1 **[state]** State the theorem.
- [ ] Q2 Transform the equation: what multiplies $\tilde f$, and where must $\tilde f$ be supported?
- [ ] Q3 Do the $p^0$ integral with $\delta(p^2 - m^2)$ and relabel the negative-energy term.
- [ ] Q4 **[why]** What is left of $d^4p$ after the shell constraint, and why does a Green's function, unlike a free field, need off-shell components?

> [!tip]- Hints: route in the notes
> - Technique: K13 ($\delta(f(x))$).
> - Step 1: derivation steps 1–5; Theorem [[§CA.2 Generalized Functions#^thm-ca-2-6|§CA.2.6]] Composition of δ with a Function part 2; Theorem [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-2|§C2b.5.2]] A Green's Function Lives off the Shell.

### Time dependence of the modes; the covariant mode expansion ★★

$e^{i\hat Ht}\hat a_{\mathbf p}e^{-i\hat Ht} = \hat a_{\mathbf p}e^{-iE_{\mathbf p}t}$, hence $\hat\phi(x) = \int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}(\hat a_{\mathbf p}e^{-ip\cdot x} + \hat a^\dagger_{\mathbf p}e^{ip\cdot x})$ with $p^0 = E_{\mathbf p}$, and $\hat\pi = \partial_t\hat\phi$, see Theorem [[§C2b.1 Heisenberg Fields#^thm-c2b-1-4|§C2b.1.4]] Time Dependence of the Modes; the Covariant Mode Expansion. *Source: Lecture 5 (Sep 16), transcript ("exponentiating the Hamiltonian produces energy-dependent phase factors"); Lecture 6 (Sep 21), slide "Cheat Sheet" · PS §2.4, eqs. (2.46)–(2.47) · the user's notes Ch. 5 §5.1*

^nd-thm-c2b-1-4

- [ ] Q1 **[state]** State the three parts.
- [ ] Q2 From $[\hat H, \hat a_{\mathbf p}] = -E_{\mathbf p}\hat a_{\mathbf p}$, show $\hat H^n\hat a_{\mathbf p} = \hat a_{\mathbf p}(\hat H - E_{\mathbf p})^n$.
- [ ] Q3 Exponentiate to get the phase of $\hat a_{\mathbf p}$; take the adjoint for $\hat a^\dagger_{\mathbf p}$.
- [ ] Q4 Start from the Schrödinger field with $\hat a^\dagger_{\mathbf p}e^{-i\mathbf p\cdot\mathbf x}$ (not relabelled) and conjugate term by term. How do the spatial phases become $e^{\mp ip\cdot x}$?
- [ ] Q5 Differentiate in $t$ and compare with the expansion of $\hat\pi$.
- [ ] Q6 **[why]** What is still not covariant about this expansion, and where is the non-covariance hidden?

> [!tip]- Hints: route in the notes
> - Technique: K11, K9.
> - Step 1: derivation steps 1–6 (mode form of $\hat H$, one commutator, powers, exponentiate, adjoint); steps 7–9.
> - Step 2: [[§C2b.1 Heisenberg Fields#^rem-c2b-1-2|§C2b.1, Remark: What is covariant and what is not yet]] (what is covariant and what is not yet).

### Positive and negative frequency ★★

$\hat\phi = \hat\phi^+ + \hat\phi^-$ with $\hat\phi^+$ the $\hat a_{\mathbf p}e^{-ip\cdot x}$ part; $\hat\phi^+|0\rangle = 0$, and $\langle0|\hat\phi(x)|\mathbf p\rangle = e^{-ip\cdot x}$, $\langle\mathbf p|\hat\phi(x)|0\rangle = e^{ip\cdot x}$, see Theorem [[§C2b.1 Heisenberg Fields#^thm-c2b-1-5|§C2b.1.5]] Positive and Negative Frequency. *Source: Lecture 5 (Sep 16), transcript ("particle–wave duality"; "a superposition of positive- and negative-frequency wave solutions") · PS §2.4, p. 26 · the user's notes Ch. 5 §5.3*

^nd-thm-c2b-1-5

- [ ] Q1 **[state]** Define $\hat\phi^\pm$ and state the two matrix elements.
- [ ] Q2 Compute $\langle0|\hat\phi(x)|\mathbf p\rangle$: which part of $\hat\phi$ contributes, and how does the relativistic normalization cancel the $1/\sqrt{2E}$?
- [ ] Q3 **[why]** Why is negative frequency creation and not negative energy?
- [ ] Q4 **[conv]** Which sign of the time exponent goes with annihilation, in the vault and in PS?

> [!tip]- Hints: route in the notes
> - Technique: K9.
> - Step 1: derivation steps 1–6; [[§C2b.1 Heisenberg Fields#^rem-c2b-1-3|§C2b.1, Remark: Negative frequency is creation, not negative energy]].

### The Heisenberg field is an operator-valued distribution on spacetime ★

$\hat\phi(f) = \int d^4x\,f\hat\phi = \int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}(\tilde f(-p)\hat a_{\mathbf p} + \tilde f(p)\hat a^\dagger_{\mathbf p})$ depends on $\tilde f$ only on the shell, and $\hat\phi((\partial^2 + m^2)f) = 0$, see Theorem [[§C2b.1 Heisenberg Fields#^thm-c2b-1-6|§C2b.1.6]] The Heisenberg Field Is an Operator-Valued Distribution on Spacetime. *Source: the user's notes App. A §A.4, Ch. 6 §6.2*

^nd-thm-c2b-1-6

- [ ] Q1 **[state]** State the three parts.
- [ ] Q2 Smear term by term and identify the transforms that appear.
- [ ] Q3 **[why]** In what precise sense does the operator equation $(\partial^2 + m^2)\hat\phi = 0$ hold?

> [!tip]- Hints: route in the notes
> - Technique: K9.
> - Step 1: derivation steps 1–5.

### The Wightman function as a mode integral ★★

$D_W(\xi) = \int\frac{d^3p}{(2\pi)^3\,2E_{\mathbf p}}e^{-ip\cdot\xi} = \int\frac{d^4p}{(2\pi)^4}2\pi\theta(p^0)\delta(p^2 - m^2)e^{-ip\cdot\xi}$, $\xi = x - y$, see Theorem [[§C2b.2 The Wightman Function#^thm-c2b-2-1|§C2b.2.1]] The Wightman Function as a Mode Integral. The mode integral is also the first step of PS4.4(a). *Source: Lecture 5 (Sep 16), transcript; Lecture 6 (Sep 21), slide "Cheat Sheet" · PS §2.4, eq. (2.50) · the user's notes Ch. 5 §5.4*

^nd-thm-c2b-2-1

- [ ] Q1 **[state]** State both forms of $D_W$.
- [ ] Q2 Write $\hat\phi(x)\hat\phi(y)$ with momenta $\mathbf p$, $\mathbf q$ and expand into four terms. Which vacuum expectation values vanish and why?
- [ ] Q3 Use the surviving commutator and integrate the delta. Which factors combine into $1/2E_{\mathbf p}$?
- [ ] Q4 Show the four-dimensional form: do the $p^0$ integral with $\theta(p^0)\delta(p^2 - m^2)$.
- [ ] Q5 **[why]** Does the mode integral converge at any real $\xi$? In what sense is the formula true?

> [!tip]- Hints: route in the notes
> - Technique: K9, K13.
> - Step 1: derivation steps 1–4 (two fields, all four terms, vacuum expectation values, integrate the delta); step 5 (four-dimensional form); step 6 (no convergence).
> - Step 2: Theorem [[§C2b.2 The Wightman Function#^thm-c2b-2-2|§C2b.2.2]] The Wightman Function Is a Tempered Distribution for the distributional meaning.

### The Wightman function is a tempered distribution ★

$\langle0|\hat\phi(f)\hat\phi(g)|0\rangle = \int\frac{d^3p}{(2\pi)^3\,2E_{\mathbf p}}\tilde f(-p)\tilde g(p)$ is finite, and its kernel $D_W$ is the transform of $2\pi\theta(p^0)\delta(p^2 - m^2)$; at fixed time $D_W(t, \cdot)$ is a distribution in $\boldsymbol\xi$ smooth in $t$, see Theorem [[§C2b.2 The Wightman Function#^thm-c2b-2-2|§C2b.2.2]] The Wightman Function Is a Tempered Distribution. *Source: the user's notes App. A §A.4, Ch. 5 §5.4*

^nd-thm-c2b-2-2

- [ ] Q1 **[state]** State how $D_W$ acts on a test function.
- [ ] Q2 Why does the kernel depend only on $x - y$?
- [ ] Q3 **[why]** Why does "smooth in time with values in spatial distributions" matter later, for $\theta(\xi^0)D_W$?

> [!tip]- Hints: route in the notes
> - Technique: none.
> - Step 1: derivation steps 1–6; Theorem [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-4|§C2b.6.4]] The Feynman Propagator as a Distribution: the Products θ·D_W.

### Lorentz invariance of the Wightman function ★★

For every $\Lambda \in SO^+(1,3)$, $D_W[f\circ\Lambda^{-1}] = D_W[f]$; off the light cone $D_W(\Lambda\xi) = D_W(\xi)$, so $D_W$ is a function of $\xi^2$ (and inside the cone of $\operatorname{sgn}\xi^0$), see Theorem [[§C2b.2 The Wightman Function#^thm-c2b-2-3|§C2b.2.3]] Lorentz Invariance of the Wightman Function. *Source: Lecture 5 (Sep 16), transcript · PS §2.4, p. 27 · the user's notes Ch. 5 §5.4*

^nd-thm-c2b-2-3

- [ ] Q1 **[state]** State the invariance and its consequence for the dependence on $\xi$.
- [ ] Q2 Substitute $p = \Lambda p'$ in the four-dimensional form. Which three facts make the integrand invariant?
- [ ] Q3 **[why]** Why is $\theta(p^0)$ invariant here, though $\theta$ of a general four-vector is not?
- [ ] Q4 **[why]** Why is the three-dimensional form not manifestly invariant?

> [!tip]- Hints: route in the notes
> - Technique: K14 (Lorentz-invariance arguments).
> - Step 1: derivation steps 1–4; Theorem [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-3|§C2a.4.3]] The Invariant Measure; Theorem [[§CA.2 Generalized Functions#^thm-ca-2-7|§CA.2.7]] Invariant Distributions on the Mass Shell and the Light Cone.

### The Wightman function is a homogeneous solution; reversal is conjugation

$(\partial_x^2 + m^2)D_W(x - y) = 0$ and $D_W(-\xi) = \overline{D_W(\xi)}$, see Theorem [[§C2b.2 The Wightman Function#^thm-c2b-2-4|§C2b.2.4]] The Wightman Function Is a Homogeneous Solution; Reversal Is Conjugation. Part 2 is used in the equivalence "D and D₁ from D_W" below.

^nd-thm-c2b-2-4

→ drilled as [[PHY 513 PS Drill#^ps4-4-b|PS4.4(b)]] (part 1)

### The Wightman function is a boundary value ★

$W(z, \boldsymbol\xi) = \int\frac{d^3p}{(2\pi)^3\,2E_{\mathbf p}}e^{-iE_{\mathbf p}z + i\mathbf p\cdot\boldsymbol\xi}$ converges and is analytic for $\operatorname{Im}z < 0$, and $D_W(\xi) = \lim_{\varepsilon\to0^+}W(\xi^0 - i\varepsilon, \boldsymbol\xi)$ in $\mathcal S'$, see Theorem [[§C2b.2 The Wightman Function#^thm-c2b-2-5|§C2b.2.5]] The Wightman Function Is a Boundary Value. *Source: the user's notes Ch. 5 §5.4 · Problem Set 4, Problem 2(a) (the prescription $t \to t - i\varepsilon$)*

^nd-thm-c2b-2-5

- [ ] Q1 **[state]** State where $W$ is analytic and how $D_W$ is recovered.
- [ ] Q2 Compute the modulus of the integrand at $z = t - i\varepsilon$. Which physical fact makes it decay?
- [ ] Q3 **[why]** Why does the sign of $i\varepsilon$ in Problem Set 4's $t \to t - i\varepsilon$ have to be this one?
- [ ] Q4 **[why]** In which sense is the limit taken, and why is the limit the same along every direction in the forward cone?

> [!tip]- Hints: route in the notes
> - Technique: K13.
> - Step 1: derivation steps 1–4; Theorem [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-1|§CA.6.1]] Boundary Values of Analytic Functions Are Distributions; dominated convergence Theorem [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|§CA.1.1]] Dominated Convergence and Differentiation under the Integral.

### The Wightman function at imaginary time ★

For $\tau > 0$, $W(-i\tau, \boldsymbol\xi) = \int\frac{d^4p_E}{(2\pi)^4}\frac{e^{ip_E\cdot x_E}}{p_E^2 + m^2} = \frac{m}{4\pi^2R}K_1(mR)$, $R = \sqrt{\tau^2 + \boldsymbol\xi^2}$; for $m = 0$, $1/4\pi^2R^2$, see Theorem [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-1|§C2b.3.1]] The Wightman Function at Imaginary Time. *Source: the user's notes Ch. 2 §2.2, Ch. 5 §5.4*

^nd-thm-c2b-3-1

- [ ] Q1 **[state]** State the result and its massless limit.
- [ ] Q2 Recover the three-dimensional integral from the four-dimensional Euclidean one by doing the $p_4$ integral by residues. Where are the poles?
- [ ] Q3 Use Schwinger's parametrization for $1/(p_E^2 + m^2)$ and do the Gaussian $\mathbf p$ and $p_4$ integrals.
- [ ] Q4 Change variables in the remaining $s$ integral to recognize $K_1$.
- [ ] Q5 **[why]** Why is the result a function of the Euclidean distance alone?

> [!tip]- Hints: route in the notes
> - Technique: K13, K1.
> - Step 1: derivation steps 1–2 (residue); steps 3–4 (Schwinger, Gaussian, Theorem [[§CA.5 Gaussian Integrals, Stationary Phase and Bessel Functions#^thm-ca-5-1|§CA.5.1]] Gaussian Integrals in n Dimensions; Schwinger Parametrization); steps 5–6 ($K_1$, Definition [[§CA.5 Gaussian Integrals, Stationary Phase and Bessel Functions#^def-ca-5-1|§CA.5.1]] Modified Bessel Function of the Second Kind); step 7 ($m = 0$).

### The Wightman function in the lower half-plane ★

For $\operatorname{Im}z < 0$, $W(z, \boldsymbol\xi) = \frac{mK_1(ms)}{4\pi^2s}$ with $s = \sqrt{\boldsymbol\xi^2 - z^2}$ on the principal branch; every value of $D_W$ is a boundary value of this one function, see Theorem [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-2|§C2b.3.2]] The Wightman Function in the Lower Half-Plane. *Source: the user's notes Ch. 5 §5.4*

^nd-thm-c2b-3-2

- [ ] Q1 **[state]** State the formula and the branch.
- [ ] Q2 Where does $s^2$ go as $z$ ranges over the lower half-plane? Why is the right side analytic there?
- [ ] Q3 **[why]** Which theorem turns agreement on the imaginary ray into agreement everywhere?

> [!tip]- Hints: route in the notes
> - Technique: K13.
> - Step 1: derivation steps 1–5; identity theorem Theorem [[§CA.4 Contour Integration#^thm-ca-4-3|§CA.4.3]] Identity Theorem.

### The Wightman function at spacelike separation

$D_W(\xi) = \frac{m}{4\pi^2r}K_1(mr)$ for $\xi^2 = -r^2 < 0$, real and positive, with $\simeq\frac{\sqrt m}{2(2\pi r)^{3/2}}e^{-mr}$ for $mr \gg 1$, see Theorem [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-3|§C2b.3.3]] The Wightman Function at Spacelike Separation. The angular integral was left to practise in Lecture 5 ("this integral, I think I did tell you that you practice"). *Source: Lecture 5 (Sep 16), transcript · PS §2.4, eq. (2.52) · Problem Set 4, Problem 3(a)*

^nd-thm-c2b-3-3

→ drilled as [[PHY 513 PS Drill#^ps4-3-a|PS4.3(a)]]

### The Wightman function at timelike separation ★

For $\xi^2 = \tau^2 > 0$, $D_W = \frac{m}{8\pi\tau}[Y_1(m\tau) + i\operatorname{sgn}(\xi^0)J_1(m\tau)]$; at $\boldsymbol\xi = 0$, $mt \gg 1$, $D_W \propto t^{-3/2}e^{-imt}$, see Theorem [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-4|§C2b.3.4]] The Wightman Function at Timelike Separation. *Source: Lecture 5 (Sep 16), transcript ("at late time … what really matters is the lowest energy … m") · PS §2.4, eq. (2.51) · the user's notes Ch. 5 §5.4*

^nd-thm-c2b-3-4

- [ ] Q1 **[state]** State the timelike form and its late-time behaviour at $\boldsymbol\xi = 0$.
- [ ] Q2 Take the limit of $s$ for $t > 0$ and $t < 0$: on which side of the cut does each land?
- [ ] Q3 Use $K_1$ at imaginary argument to get $J_1$ and $Y_1$.
- [ ] Q4 **[why]** Why does only the lowest energy $E = m$ survive at late times, and where does $t^{-3/2}$ come from?
- [ ] Q5 **[why]** Why are the values on the future and past sheets complex conjugates?

> [!tip]- Hints: route in the notes
> - Technique: K13.
> - Step 1: derivation steps 1–5; Theorem [[§CA.5 Gaussian Integrals, Stationary Phase and Bessel Functions#^thm-ca-5-4|§CA.5.4]] Further Representations; Imaginary Argument parts 3–4; Theorem [[§C2b.2 The Wightman Function#^thm-c2b-2-4|§C2b.2.4]] The Wightman Function Is a Homogeneous Solution; Reversal Is Conjugation part 2.

### The Wightman function near the light cone

As $\xi^2 \to 0$, $D_W = -\frac{1}{4\pi^2[(\xi^0 - i\varepsilon)^2 - \boldsymbol\xi^2]} + \frac{m^2}{8\pi^2}\ln\frac{ms}{2} + \cdots$; the leading term is the massless Wightman function, exact for $m = 0$, see Theorem [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-5|§C2b.3.5]] The Wightman Function near the Light Cone.

^nd-thm-c2b-3-5

→ drilled as [[PHY 513 PS Drill#^ps4-2-a|PS4.2(a)]] (the massless function)

### The Wightman function as a distribution, off the cone and on it ★

Off the light cone $D_W$ is the real-analytic Bessel function; its singular support is the whole cone; on $\mathbb R^4$, $D_W = -\frac{1}{4\pi^2}\mathcal P\frac{1}{\xi^2} - \frac{i}{4\pi}\operatorname{sgn}(\xi^0)\delta(\xi^2) + L$ with $L$ locally integrable, see Theorem [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-6|§C2b.3.6]] The Wightman Function as a Distribution: Off the Cone and on It. *Source: the user's notes Ch. 5 §5.4, §5.7*

^nd-thm-c2b-3-6

- [ ] Q1 **[state]** State the three parts.
- [ ] Q2 Split off the light-cone term with the light-cone boundary value. What are its real and imaginary parts?
- [ ] Q3 **[why]** Which part depends on the mass, and which does not?

> [!tip]- Hints: route in the notes
> - Technique: K13.
> - Step 1: derivation steps 1–7; Theorem [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-4|§CA.6.4]] The Light-Cone Boundary Value.

### The single-particle amplitude is a time derivative of the Wightman function ★

$U(z, \mathbf x) = 2i\partial_zW(z, \mathbf x)$ and $U = 2i\partial_tD_W$ in $\mathcal S'$, linking Lecture 2's single-particle amplitude to the field's two-point function, see Theorem [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-7|§C2b.3.7]] The Single-Particle Amplitude Is a Time Derivative of the Wightman Function. *Source: the user's notes Ch. 2 §2.2, Ch. 5 §5.4*

^nd-thm-c2b-3-7

- [ ] Q1 **[state]** State the relation.
- [ ] Q2 Compare the two mode integrals: which weights do $U$ and $D_W$ carry, and how does $\partial_t$ convert one into the other?
- [ ] Q3 **[why]** What does the difference of weights say about the normalization of states?

> [!tip]- Hints: route in the notes
> - Technique: K9.
> - Step 1: derivation steps 1–2; the amplitude is Theorem [[§C1a.3 Causal Structure and the Causality of a Single Particle#^thm-c1a-3-4|§C1a.3.4]] The Relativistic Amplitude Is a Boundary Value.

### The relativistic single-particle amplitude outside the light cone ★★

For $r > |t|$, $U = \frac{im^2t}{2\pi^2\rho^2}K_2(m\rho)$ with $\rho = \sqrt{r^2 - t^2}$, nonzero at every spacelike point with $t \neq 0$; for $m\rho \gg 1$, $U \propto e^{-m\rho}$, see Theorem [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-8|§C2b.3.8]] The Relativistic Amplitude at Spacelike Separation, Theorem [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-9|§C2b.3.9]] The Spacelike Amplitude at Large Distance. *Source: Lecture 2 (Sep 2), slides "The exact radial integral: a Bessel function", "Quantum Causality is Violated" · PS §2.1, p. 14 · the user's notes Ch. 2 §2.2*

^nd-thm-c2b-3-8

- [ ] Q1 **[state]** State the closed form and its large-distance behaviour.
- [ ] Q2 Differentiate $W = mK_1(ms)/4\pi^2s$ twice in $z$ using the recursion for $K_\nu$.
- [ ] Q3 Take the spacelike limit and show $U$ is purely imaginary and odd in $t$.
- [ ] Q4 **[why]** Why does relativistic kinematics not cure the leak outside the cone, and how does field theory resolve it?

> [!tip]- Hints: route in the notes
> - Technique: K13.
> - Step 1: derivation steps 1–7 of Theorem [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-8|§C2b.3.8]] The Relativistic Amplitude at Spacelike Separation; Theorem [[§CA.5 Gaussian Integrals, Stationary Phase and Bessel Functions#^thm-ca-5-3|§CA.5.3]] Properties of $K_\nu$ part 1.
> - Step 2: resolution: Theorem [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-7|§C2b.4.7]] Forward and Backward Amplitudes; Theorem [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-9|§C2b.3.9]] The Spacelike Amplitude at Large Distance for the asymptotics.

### The spacelike amplitude at large distance ★

For $r > |t|$ and $m\rho \gg 1$, $U = \frac{im^{3/2}t}{(2\pi\rho)^{3/2}\rho}e^{-m\rho}(1 + \frac{15}{8m\rho} + \cdots)$, nonzero at every spacelike point with $t \neq 0$; the leading term is the saddle-point result of Lecture 2, see Theorem [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-9|§C2b.3.9]] The Spacelike Amplitude at Large Distance. *Source: Lecture 2 (Sep 2), slide "Quantum Causality is Violated" · PS §2.1, p. 14 · the user's notes Ch. 2 §2.2*

^nd-thm-c2b-3-9

- [ ] Q1 **[state]** State the large-distance form and the range of the leak.
- [ ] Q2 Insert the large-argument form of $K_2$ into the closed form of $U$.
- [ ] Q3 Compare the relative correction with the one for $D_W$: which value of $\nu$ in the same series gives each?
- [ ] Q4 **[why]** Why does "small but not zero" violate the single-particle causality principle, and which saddle-point theorem gives the same exponent?

> [!tip]- Hints: route in the notes
> - Technique: K13.
> - Step 1: derivation steps 1–3; Theorem [[§CA.5 Gaussian Integrals, Stationary Phase and Bessel Functions#^thm-ca-5-3|§CA.5.3]] Properties of $K_\nu$ part 2; Theorem [[§C1a.3 Causal Structure and the Causality of a Single Particle#^thm-c1a-3-6|§C1a.3.6]] The Leak Is Exponentially Small but Not Zero.

### The single-particle amplitude inside the light cone ★

For $|t| > r$, $U(t, \mathbf x) = \frac{m^2t}{4\pi\tau^2}H^{(2)}_2(m\tau)$ for $t > 0$, $U(-t, \mathbf x) = \overline{U(t, \mathbf x)}$, oscillating, see Theorem [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-10|§C2b.3.10]] The Relativistic Amplitude at Timelike Separation. *Source: the user's notes Ch. 2 §2.2*

^nd-thm-c2b-3-10

- [ ] Q1 **[state]** State the timelike form.
- [ ] Q2 Continue $K_2$ to imaginary argument: which Hankel function appears for $t > 0$?
- [ ] Q3 **[why]** Why are the moduli inside and outside the cone of the same form, and what differs?

> [!tip]- Hints: route in the notes
> - Technique: K13.
> - Step 1: derivation steps 1–5; Theorem [[§CA.5 Gaussian Integrals, Stationary Phase and Bessel Functions#^thm-ca-5-4|§CA.5.4]] Further Representations; Imaginary Argument part 3.

### Units restored in the single-particle amplitude ★

Restoring $\hbar$ and $c$: $U = \frac{im^2c^3t}{2\pi^2\hbar^2\rho^2}K_2(mc\rho/\hbar)$; the leak has the range of the reduced Compton wavelength, see Example [[§C2b.3 Explicit Forms of the Wightman Function#^ex-c2b-3-1|§C2b.3.1]] Units Restored in the Single-Particle Amplitude. *Source: the user's notes Ch. 2 §2.4*

^nd-ex-c2b-3-1

- [ ] Q1 **[state]** What dimension must $U$ have, and why?
- [ ] Q2 Make the argument of $K_2$ dimensionless with $\hbar$ and $c$.
- [ ] Q3 Fix the powers of $\hbar$ and $c$ in the prefactor by dimensional analysis.
- [ ] Q4 **[why]** Before any integral, what does dimensional analysis say about the range of the leak? Give its size for an electron.

> [!tip]- Hints: route in the notes
> - Technique: K8 (dimensional analysis).
> - Step 1: steps 1–5 of the example; P4, step 4.

### The field commutator is a c-number ★★

$[\hat\phi(x), \hat\phi(y)] = D_W(x - y) - D_W(y - x) = \int\frac{d^3p}{(2\pi)^3\,2E_{\mathbf p}}(e^{-ip\cdot(x - y)} - e^{ip\cdot(x - y)}) = iD(x - y)$, the same number in every state, see Theorem [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-2|§C2b.4.2]] The Field Commutator Is a c-Number. *Source: Lecture 5 (Sep 16), transcript ("the commutator, formed from opposite operator orderings") · PS §2.4, eq. (2.53) · the user's notes Ch. 5 §5.5*

^nd-thm-c2b-4-2

- [ ] Q1 **[state]** State the commutator in terms of $D_W$ and as a mode integral.
- [ ] Q2 Expand $[\hat\phi(x), \hat\phi(y)]$ with momenta $\mathbf p$, $\mathbf q$: which of the four commutators survive?
- [ ] Q3 Integrate the deltas. Why is the result proportional to the identity operator?
- [ ] Q4 **[why]** Read the two terms as orderings of creation and annihilation: which propagates from $y$ to $x$ and which back?

> [!tip]- Hints: route in the notes
> - Technique: K9, K11.
> - Step 1: derivation steps 1–4; [[§C2b.4 Microcausality and the Commutator Function#^rem-c2b-4-2|§C2b.4, Remark: Two orderings that cancel; why antiparticles must exist]] (two orderings that cancel).

### The commutator and Hadamard functions as distributions ★

$iD = D_W(\xi) - D_W(-\xi)$ and $D_1 = D_W(\xi) + D_W(-\xi)$ in $\mathcal S'$, real, with transforms $\tilde D = -2\pi i\operatorname{sgn}(p^0)\delta(p^2 - m^2)$, $\tilde D_1 = 2\pi\delta(p^2 - m^2)$; both solve the homogeneous equation, see Theorem [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-4|§C2b.4.4]] The Commutator and Hadamard Functions as Distributions. *Source: the user's notes Ch. 5 §5.5, §5.7 · Problem Set 4, Problem 2*

^nd-thm-c2b-4-4

- [ ] Q1 **[state]** State the transforms of $D$ and $D_1$.
- [ ] Q2 Derive them from the transform of $D_W(\pm\xi)$.
- [ ] Q3 What are the spatial transforms of $D$ and $D_1$ at fixed $\xi^0 = t$?
- [ ] Q4 **[why]** In what sense do the sine and cosine mode integrals converge?

> [!tip]- Hints: route in the notes
> - Technique: K13.
> - Step 1: derivation steps 1–7.

### The free field is microcausal ★★

$D(\xi) = 0$ for $\xi^2 < 0$, while inside the cone $D$ does not vanish identically, see Theorem [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-5|§C2b.4.5]] The Free Field Is Microcausal. *Source: Lecture 5 (Sep 16), transcript ("the commutator … vanishes at spacelike separation and provides the causality condition") · PS §2.4, eq. (2.53), Fig. 2.4 · the user's notes Ch. 5 §5.5*

^nd-thm-c2b-4-5

- [ ] Q1 **[state]** State the theorem.
- [ ] Q2 For spacelike $\xi$, construct $\Lambda \in SO^+(1,3)$ with $\Lambda\xi = -\xi$: which frame do you first go to, and which rotation reverses the vector?
- [ ] Q3 Combine with the invariance of $D_W$ to conclude $D(\xi) = 0$. Why is pointwise use of invariance legitimate at spacelike $\xi$?
- [ ] Q4 **[why]** Why is the construction impossible for timelike $\xi$?
- [ ] Q5 **[why]** Each Wightman function is nonzero at spacelike separation. What exactly cancels, and why does that need antiparticles for a complex field?

> [!tip]- Hints: route in the notes
> - Technique: K14 (equal-time frame, microcausality), K1.
> - Step 1: derivation steps 1–3 (a Lorentz transformation that reverses $\xi$, Theorem [[§C1a.4 The Lorentz Group#^thm-c1a-4-3|§C1a.4.3]] Parity and Time Reversal Permute the Orbits part 3); step 4 (conclude); step 5 (inside the cone).
> - Step 2: the second route (reality of $D_W$) is in the equivalence "Microcausality in three forms" below; [[§C2b.4 Microcausality and the Commutator Function#^rem-c2b-4-2|§C2b.4, Remark: Two orderings that cancel; why antiparticles must exist]].

### Microcausality as a support statement ★

$\operatorname{supp}D \subseteq \{\xi^2 \ge 0\}$ (the cone surface for $m = 0$, the whole closed cone for $m > 0$); equivalently $[\hat\phi(f), \hat\phi(g)] = 0$ for test functions with spacelike-separated supports, see Theorem [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-6|§C2b.4.6]] Microcausality as a Support Statement. *Source: the user's notes Ch. 5 §5.5, App. A §A.4*

^nd-thm-c2b-4-6

- [ ] Q1 **[state]** State both forms.
- [ ] Q2 Show that $D$ vanishes as a distribution on the open spacelike region.
- [ ] Q3 **[why]** Why is microcausality a statement about where a distribution vanishes, not about values at points?

> [!tip]- Hints: route in the notes
> - Technique: K14.
> - Step 1: derivation steps 1–3; Definition [[§CA.2 Generalized Functions#^def-ca-2-3|§CA.2.3]] Support and Singular Support.

### Forward and backward amplitudes ★

$U(t, \mathbf x) + U(-t, \mathbf x) = -2\partial_tD$, which vanishes outside the cone, and $U(t, \mathbf x) - U(-t, \mathbf x) = 2i\partial_tD_1$; outside the cone $U = i\partial_tD_1$, see Theorem [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-7|§C2b.4.7]] Forward and Backward Amplitudes. *Source: the user's notes Ch. 2 §2.2 (Caution "Particles moving backward in time") · Lecture 2 (Sep 2), slide "Resolution in Quantum Field Theory"*

^nd-thm-c2b-4-7

- [ ] Q1 **[state]** State the three relations.
- [ ] Q2 Write the forward and backward amplitudes as mode integrals and form sum and difference.
- [ ] Q3 **[why]** What does the theorem say about the leak of the single-particle amplitude: influence or correlation?

> [!tip]- Hints: route in the notes
> - Technique: K9.
> - Step 1: derivation steps 1–5; [[§C2b.4 Microcausality and the Commutator Function#^rem-c2b-4-3|§C2b.4, Remark: Influence and correlation]].

### Commutator and Hadamard functions of the massless field

$D = -\frac{1}{2\pi}\operatorname{sgn}(\xi^0)\delta(\xi^2) = -\frac{1}{4\pi r}[\delta(t - r) - \delta(t + r)]$, $D_1 = -\frac{1}{2\pi^2}\mathcal P\frac{1}{\xi^2}$, see Theorem [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-8|§C2b.4.8]] Commutator and Hadamard Functions of the Massless Field.

^nd-thm-c2b-4-8

→ drilled as [[PHY 513 PS Drill#^ps4-2-b|PS4.2(b)]]

### Commutator and Hadamard functions of the massive field

Outside the cone $D = 0$, $D_1 = \frac{mK_1(mr)}{2\pi^2r}$; inside, $D = \operatorname{sgn}(\xi^0)\frac{mJ_1(m\tau)}{4\pi\tau}$, $D_1 = \frac{mY_1(m\tau)}{4\pi\tau}$; on the cone the massless delta, see Theorem [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-9|§C2b.4.9]] Commutator and Hadamard Functions of the Massive Field. The inside-the-cone forms follow from Theorem [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-4|§C2b.3.4]] The Wightman Function at Timelike Separation by the same relations.

^nd-thm-c2b-4-9

→ drilled as [[PHY 513 PS Drill#^ps4-3-b|PS4.3(b)]] (outside the cone)

### Commutators at unequal times ★

$[\hat\phi(x), \hat\phi(y)] = iD(x - y)$, $[\hat\phi(x), \hat\pi(y)] = i\partial_{y^0}D(x - y)$, $[\hat\pi(x), \hat\pi(y)] = i\partial_{x^0}\partial_{y^0}D(x - y)$, reducing to the canonical relations at equal times, see Theorem [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-10|§C2b.4.10]] Commutators at Unequal Times. This answers the question left open in Lecture 5 ("how commutators behave at different times"). *Source: Lecture 5 (Sep 16), transcript · the user's notes Ch. 5 §5.7*

^nd-thm-c2b-4-10

- [ ] Q1 **[state]** State the three commutators.
- [ ] Q2 **[why]** Why may $\partial_{y^0}$ be taken outside the commutator?
- [ ] Q3 Compute $[\hat\phi(x), \hat\pi(y)]$ as a mode integral. Which trigonometric function appears?
- [ ] Q4 Check the equal-time limits of all three.
- [ ] Q5 **[why]** What is postulated and what is derived about commutators of the free field?

> [!tip]- Hints: route in the notes
> - Technique: K11, K9.
> - Step 1: derivation steps 1–4; Theorem [[§C2b.1 Heisenberg Fields#^thm-c2b-1-4|§C2b.1.4]] Time Dependence of the Modes; the Covariant Mode Expansion part 3 ($\hat\pi = \partial_t\hat\phi$).

### Commutators at unequal times as distributions ★

At fixed $t = x^0 - y^0$ the three kernels are tempered distributions in $\mathbf x - \mathbf y$ with spatial transforms $-\sin(E_{\mathbf p}t)/E_{\mathbf p}$, $\cos(E_{\mathbf p}t)$, $-E_{\mathbf p}\sin(E_{\mathbf p}t)$ (times $i$); as $t \to 0$ they tend to $0$, $i\delta^3$, $0$ in $\mathcal S'$, see Theorem [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-11|§C2b.4.11]] Commutators at Unequal Times as Distributions. *Source: the user's notes Ch. 5 §5.7*

^nd-thm-c2b-4-11

- [ ] Q1 **[state]** State the spatial transforms and the equal-time limits.
- [ ] Q2 Derive the transform of $[\hat\phi, \hat\pi]$ from the one of $D$ by a time derivative.
- [ ] Q3 **[why]** Why are the equal-time relations recovered as limits rather than values, and why does that matter for contact terms?

> [!tip]- Hints: route in the notes
> - Technique: K13.
> - Step 1: derivation steps 1–5.

### Cauchy data of the commutator function ★

$D$ is the unique solution of $(\partial^2 + m^2)D = 0$ with $D(0, \boldsymbol\xi) = 0$, $\partial_0D(0, \boldsymbol\xi) = -\delta^3(\boldsymbol\xi)$, see Theorem [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-12|§C2b.4.12]] Cauchy Data of the Commutator Function. *Source: the user's notes Ch. 5 §5.7*

^nd-thm-c2b-4-12

- [ ] Q1 **[state]** State the Cauchy data of $D$.
- [ ] Q2 Derive them from the equal-time canonical relations.
- [ ] Q3 Prove uniqueness for tempered solutions: why is a solution with zero data zero?
- [ ] Q4 **[why]** What does the theorem say about quantizing on one time slice?

> [!tip]- Hints: route in the notes
> - Technique: K11.
> - Step 1: derivation steps 1–3; Theorem [[§C2b.1 Heisenberg Fields#^thm-c2b-1-3|§C2b.1.3]] Free Fields Live on the Mass Shell.

### The commutator function propagates the field ★

$\hat\phi(x) = -\int d^3y\,[D(x - y)\hat\pi(y) - \partial_{y^0}D(x - y)\hat\phi(y)]$ for every $y^0$; since $D$ vanishes outside the cone, $\hat\phi(x)$ is fixed by data inside the backward cone of $x$, see Theorem [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-13|§C2b.4.13]] The Commutator Function Propagates the Field. *Source: the user's notes Ch. 5 §5.7*

^nd-thm-c2b-4-13

- [ ] Q1 **[state]** State the propagation formula and its causal consequence.
- [ ] Q2 Show the right side is independent of $y^0$. Which equation do both factors obey in $y$, and which integration by parts is used?
- [ ] Q3 Evaluate at $y^0 = x^0$ using the Cauchy data of $D$.
- [ ] Q4 **[why]** For $m = 0$, why is the field fixed by data on the surface of the backward cone alone?

> [!tip]- Hints: route in the notes
> - Technique: K11.
> - Step 1: derivation steps 1–4; Theorem [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-12|§C2b.4.12]] Cauchy Data of the Commutator Function; [[§C2b.4 Microcausality and the Commutator Function#^rem-c2b-4-5|§C2b.4, Remark: Microcausality and the domain of dependence are one statement]].

### A Green's function lives off the shell ★★

For a tempered Green's function, $(m^2 - p^2)\tilde D_C(p) = -i$, so $\tilde D_C = \frac{i}{p^2 - m^2}$ wherever $p^2 \neq m^2$; on the shell the equation does not determine it, see Theorem [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-2|§C2b.5.2]] A Green's Function Lives off the Shell. *Source: Lecture 6 (Sep 21), slide "Green's Functions: Explicit Form" · PS §2.4, pp. 29–30 · the user's notes Ch. 6 §6.3–6.4*

^nd-thm-c2b-5-2

- [ ] Q1 **[state]** State the momentum-space form of a Green's function and where it is determined.
- [ ] Q2 Insert $D_C(x - y) = \int\frac{d^4p}{(2\pi)^4}\tilde D_C(p)e^{-ip\cdot(x - y)}$ and $\delta^4 = \int\frac{d^4p}{(2\pi)^4}e^{-ip\cdot(x - y)}$ into the defining equation. What does $\partial_x^2 + m^2$ do to the exponential?
- [ ] Q3 **[conv]** Check the sign of $\tilde D_C$ from the sign of $m^2 - p^2$ and the $-i$ normalization.
- [ ] Q4 **[why]** A free field has its transform on the shell. Why must a Green's function have off-shell components, and why is the shell where the difficulty sits?

> [!tip]- Hints: route in the notes
> - Technique: K13.
> - Step 1: derivation steps 1–2; P2, step 1; Theorem [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-4|§CA.3.4]] Rules of the Fourier Transform part 2.
> - Step 2: Theorem [[§C2b.1 Heisenberg Fields#^thm-c2b-1-3|§C2b.1.3]] Free Fields Live on the Mass Shell; [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^cau-c2b-6-2|§C2b.6, Caution: Signs that slip]].

### Contours are boundary conditions ★★

Every contour passing the two poles gives a Green's function, and two contours give Green's functions that differ by a homogeneous solution built from on-shell waves: choosing a contour is choosing a boundary condition, see Theorem [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-3|§C2b.5.3]] Contours Are Boundary Conditions. *Source: Lecture 6 (Sep 21), slides "Green's functions and Complex Contours", "Green's Functions and Boundary Conditions" ("DF and DR differ only by a homogenous solution") · PS §2.4, p. 31 · the user's notes Ch. 6 §6.8*

^nd-thm-c2b-5-3

- [ ] Q1 **[state]** State both parts.
- [ ] Q2 Apply $\partial^2 + m^2$ under the integral: what cancels the denominator, and why may the contour then be moved back to the real axis?
- [ ] Q3 Which delta functions result from the $p^0$ and $\mathbf p$ integrals?
- [ ] Q4 Two contours differ by small loops around the poles. What does each loop contribute, and why is the difference a homogeneous solution?
- [ ] Q5 **[why]** Why are "the ambiguity in giving the integral a meaning" and "the ambiguity of boundary conditions" the same ambiguity?

> [!tip]- Hints: route in the notes
> - Technique: K13.
> - Step 1: derivation steps 1–3 (apply the operator; back to the real axis; delta functions); steps 4–5 (two contours; homogeneous).
> - Step 2: Theorem [[§CA.4 Contour Integration#^thm-ca-4-5|§CA.4.5]] Residue Theorem (residue theorem); Theorem [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-7|§CA.6.7]] Fundamental Solutions Differ by Homogeneous Solutions.

### Each contour is a fundamental solution ★

$D_C$ is a tempered distribution; at fixed $\mathbf p$, $\tilde D_C = \frac{i}{(p^0 - E_{\mathbf p} + i0\sigma_+)(p^0 + E_{\mathbf p} + i0\sigma_-)}$, and $(\partial^2 + m^2)D_C = -i\delta^4$ in $\mathcal S'$; every tempered fundamental solution is $D_C + H$ with $H$ on the shell, see Theorem [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-4|§C2b.5.4]] Each Contour Is a Fundamental Solution. *Source: the user's notes Ch. 6 §6.2, §6.8–6.9*

^nd-thm-c2b-5-4

- [ ] Q1 **[state]** State the boundary-value form of $\tilde D_C$ and what $\sigma_\pm$ mean.
- [ ] Q2 **[why]** Passing a pole above corresponds to moving it which way? Why?
- [ ] Q3 **[why]** Without a contour, why is $i/(p^2 - m^2)$ not a distribution near the shell?

> [!tip]- Hints: route in the notes
> - Technique: K13.
> - Step 1: derivation steps 1–6; Theorem [[§CA.4 Contour Integration#^thm-ca-4-7|§CA.4.7]] Poles on the Contour: the Half-Residue Lemma; Theorem [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-2|§CA.6.2]] Sokhotski–Plemelj Formula.

### The retarded Green's function ★★

The contour $C_R$ passing above both poles gives $D_R(\xi) = \theta(\xi^0)[D_W(\xi) - D_W(-\xi)] = \theta(\xi^0)iD(\xi)$, zero unless $x$ is in the causal future of $y$; mode by mode $\theta(t)(-i\sin E_{\mathbf p}t)/E_{\mathbf p}$, see Theorem [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-5|§C2b.5.5]] The Retarded Green's Function. *Source: Lecture 6 (Sep 21), slides "Retarded Contour: Qualitative Behavior", "Retarded Green's Function: Explicit Evaluation" · PS §2.4, eqs. (2.54)–(2.56) · the user's notes Ch. 6 §6.6*

^nd-thm-c2b-5-5

- [ ] Q1 **[state]** State $D_R$ in terms of $D_W$ and of $D$, and its support.
- [ ] Q2 Separate the $p^0$ integral. For $t < 0$, in which half-plane does $e^{-ip^0t}$ decay? Close there: which poles are enclosed?
- [ ] Q3 Show that the arc vanishes. Which estimate suffices for this integrand?
- [ ] Q4 For $t > 0$ close the other way. What is the orientation, which poles are enclosed, and what are their residues?
- [ ] Q5 Return to three momenta: relabel the negative-frequency term and recognize $D_W(\xi)$ and $D_W(-\xi)$.
- [ ] Q6 Check mode by mode: which jump in $G_R'(t)$ at $t = 0$ produces $-i\delta(t)$?
- [ ] Q7 **[why]** Why is $D_R$ causal "in both senses at once": zero before the source and zero outside the cone?

> [!tip]- Hints: route in the notes
> - Technique: K13 (contours, residues).
> - Step 1: derivation steps 1–5 (P2, steps 2–6); step 6 (P2, step 7); step 7 (operator form).
> - Step 2: residues Theorem [[§CA.4 Contour Integration#^thm-ca-4-4|§CA.4.4]] Computing Residues part 3; closing Theorem [[§CA.4 Contour Integration#^thm-ca-4-6|§CA.4.6]] Closing the Contour: the ML Estimate and Jordan's Lemma; orientation Theorem [[§CA.4 Contour Integration#^thm-ca-4-9|§CA.4.9]] Working Rules for Contour Integrals part 1.
> - Step 3: [[§C2b.5 Green's Functions and Contours#^rem-c2b-5-3|§C2b.5, Remark: Retarded means late; the sign of the exponent carries causality]]; Theorem [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-5|§C2b.4.5]] The Free Field Is Microcausal.

### The product θ(ξ⁰)D is defined; retarded means supported in the future ★

$\theta(\xi^0)D$ is defined slice by slice since $D$ is smooth in $\xi^0$ with values in $\mathcal S'(\mathbb R^3)$; it equals the contour's $D_R/i$; $D_R$ is the only tempered fundamental solution vanishing for $\xi^0 < 0$; for $m = 0$, $D_R = -\frac{i}{4\pi r}\delta(\xi^0 - r)$, see Theorem [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-6|§C2b.5.6]] The Product θ(ξ⁰)D Is Defined; Retarded Means Supported in the Future. *Source: the user's notes Ch. 6 §6.6, §6.2, App. A §A.4*

^nd-thm-c2b-5-6

- [ ] Q1 **[state]** State the three parts.
- [ ] Q2 **[why]** Away from $\xi = 0$, why is $\theta(\xi^0)D$ a product with disjoint singular supports?
- [ ] Q3 At $\xi = 0$ extensions differ by derivatives of $\delta^4$. Which condition singles out one extension?
- [ ] Q4 **[why]** Why is "retarded" a support condition, and why does it fix the Green's function uniquely?

> [!tip]- Hints: route in the notes
> - Technique: K13.
> - Step 1: derivation steps 1–6; Theorem [[§CA.2 Generalized Functions#^thm-ca-2-2|§CA.2.2]] Distributions Supported at a Point; Theorem [[§CA.2 Generalized Functions#^thm-ca-2-8|§CA.2.8]] Products with Disjoint Singular Supports; Theorem [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-7|§CA.6.7]] Fundamental Solutions Differ by Homogeneous Solutions part 3.

### The advanced Green's function ★ [class exercise, Lecture 6]

The contour $C_A$ passing below both poles gives $D_A(\xi) = -\theta(-\xi^0)iD(\xi) = D_R(-\xi)$, zero unless $x$ is in the causal past of $y$, see Theorem [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-7|§C2b.5.7]] The Advanced Green's Function. Lecture 6 computed $D_R$ and $D_F$ and left the other contours as practice: "the key steps that you want to practice at home … assume something about this, then see what sign the exponential must have to be damped". *Source: Lecture 6 (Sep 21), transcript · the user's notes Ch. 6 §6.8, §6.11*

^nd-thm-c2b-5-7

- [ ] Q1 **[state]** State $D_A$ in terms of $D$ and of $D_R$.
- [ ] Q2 For $t > 0$ close downward: which poles are enclosed?
- [ ] Q3 For $t < 0$ close upward: what is the orientation, and what results after relabelling?
- [ ] Q4 **[why]** Why is $D_A$ the time mirror of $D_R$? What is its boundary condition as a support statement?

> [!tip]- Hints: route in the notes
> - Technique: K13.
> - Step 1: derivation steps 1–5; P2, "Instances" (advanced).

### Practise the contour choice for every contour [class exercise, Lecture 6]

For each of the four contours (retarded, advanced, Feynman, anti-Feynman) and each sign of $t$: decide where $e^{-ip^0t}$ decays, close there, check the arc, collect the enclosed residues with the orientation sign, and recognize the result in terms of $D_W(\pm\xi)$. Larsen: "See if you can get the contour to make the whole thing go away. If not, where is the spot that obstruction?"; the transcript summary lists it as the action item. No single box; the procedure is P2 and the four results are Theorem [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-5|§C2b.5.5]] The Retarded Green's Function, Theorem [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-7|§C2b.5.7]] The Advanced Green's Function, Theorem [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-2|§C2b.6.2]] The Feynman Propagator, Theorem [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-3|§C2b.6.3]] The Anti-Feynman Function. *Source: Lecture 6 (Sep 21), transcript and summary*

^nd-cx-6-1

- [ ] Q1 **[state]** List the four contours by how each passes $-E_{\mathbf p}$ and $+E_{\mathbf p}$.
- [ ] Q2 For each sign of $t$, in which half-plane must each contour be closed?
- [ ] Q3 Fill a table: for each contour and each sign of $t$, which poles are enclosed and with which orientation?
- [ ] Q4 Express each result through $D_W(\xi)$, $D_W(-\xi)$ and step functions.
- [ ] Q5 **[why]** For which contours and signs of $t$ is the answer zero, and what does that say about the boundary condition?

> [!tip]- Hints: route in the notes
> - Technique: K13.
> - Step 1: P2, steps 2–6 and its "Instances" table.
> - Step 2: orientation Theorem [[§CA.4 Contour Integration#^thm-ca-4-9|§CA.4.9]] Working Rules for Contour Integrals part 1; [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^cau-c2b-6-2|§C2b.6, Caution: Signs that slip]].

### Properties of time ordering ★

$T\{\hat\phi(x)\hat\phi(y)\}$ is symmetric; at equal times it gives $\hat\phi\hat\phi$ (ambiguous for $\hat\phi\hat\pi$); it is frame independent because of microcausality; $\partial_{x^0}T\{\hat A(x)\hat B(y)\} = T\{\partial_0\hat A\hat B\} + \delta(x^0 - y^0)[\hat A(x), \hat B(y)]$, see Theorem [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-1|§C2b.6.1]] Properties of Time Ordering. *Source: the user's notes Ch. 5 §5.6, Ch. 6 §6.7 · Yu eqs. (6.108)–(6.113)*

^nd-thm-c2b-6-1

- [ ] Q1 **[state]** State the four properties.
- [ ] Q2 **[why]** Why is $T\{\hat\phi(x)\hat\phi(y)\}$ the same in every inertial frame? Treat timelike and spacelike separation separately.
- [ ] Q3 Differentiate the step-function form in $x^0$: where does the contact term come from?
- [ ] Q4 **[why]** At equal times, why is the value unambiguous for $\hat\phi\hat\phi$ but not for $\hat\phi\hat\pi$?

> [!tip]- Hints: route in the notes
> - Technique: K14 (microcausality), K11.
> - Step 1: derivation steps 1–5; Theorem [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-5|§C2b.4.5]] The Free Field Is Microcausal; $\theta' = \delta$, Theorem [[§CA.2 Generalized Functions#^thm-ca-2-4|§CA.2.4]] Every Generalized Function Is Differentiable.

### The Feynman propagator by contour integration ★★

The Feynman contour, below $-E_{\mathbf p}$ and above $+E_{\mathbf p}$, gives $D_F(\xi) = \theta(\xi^0)D_W(\xi) + \theta(-\xi^0)D_W(-\xi) = \langle0|T\{\hat\phi(x)\hat\phi(y)\}|0\rangle$; $D_F$ is even, invariant, and $D_F = D_R + D_W(-\xi)$, see Theorem [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-2|§C2b.6.2]] The Feynman Propagator. The operator side ($\theta D_W + \theta D_W$ is the time-ordered product) → drilled as [[PHY 513 PS Drill#^ps4-4-a|PS4.4(a)]]. *Source: Lecture 6 (Sep 21), slides "The Feynman Propagator", "Evaluation of the Feynman Propagator", "Green's Functions and Boundary Conditions" · PS §2.4, eqs. (2.59)–(2.60) · the user's notes Ch. 6 §6.7*

^nd-thm-c2b-6-2

- [ ] Q1 **[state]** State $D_F$ in terms of $D_W$, as a vacuum expectation value, and its relation to $D_R$.
- [ ] Q2 For $t > 0$ close downward: which of the two poles lies inside, and why is the other outside?
- [ ] Q3 For $t < 0$ close upward: which pole is enclosed, what is the orientation, and how does the sign compare with the retarded case?
- [ ] Q4 Relabel $\mathbf p \to -\mathbf p$ in the $t < 0$ result and recognize $D_W(-\xi)$.
- [ ] Q5 Show $D_F - D_R = D_W(-\xi)$ for both signs of $t$. Why does this make $D_F$ a Green's function?
- [ ] Q6 **[why]** Why is $D_F$ even in $\xi$ and Lorentz invariant, although its definition uses $\theta(\xi^0)$?
- [ ] Q7 **[why]** In words: what does the Feynman function say about which of $x$, $y$ came first, compared with the retarded function?

> [!tip]- Hints: route in the notes
> - Technique: K13, K14.
> - Step 1: derivation steps 1–4 (set up, $t > 0$, $t < 0$, relabel; P2, steps 2–6); step 5 (operator side); step 6 (properties).
> - Step 2: [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^cau-c2b-6-2|§C2b.6, Caution: Signs that slip]]; Theorem [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-1|§C2b.6.1]] Properties of Time Ordering part 3 for invariance.

### The anti-Feynman function ★ [class exercise, Lecture 6]

The contour above $-E_{\mathbf p}$ and below $+E_{\mathbf p}$ gives $D_{\bar F}(\xi) = -\theta(\xi^0)D_W(-\xi) - \theta(-\xi^0)D_W(\xi) = -\langle0|\bar T\{\hat\phi(x)\hat\phi(y)\}|0\rangle$, see Theorem [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-3|§C2b.6.3]] The Anti-Feynman Function. One of the contours left to practise in Lecture 6. *Source: Lecture 6 (Sep 21), transcript · the user's notes Ch. 6 §6.8, §6.11*

^nd-thm-c2b-6-3

- [ ] Q1 **[state]** State $D_{\bar F}$ in terms of $D_W$ and of $\bar T$.
- [ ] Q2 Evaluate for $t > 0$ and $t < 0$: which pole is enclosed each time, with which orientation?
- [ ] Q3 **[why]** How is the anti-Feynman contour related to the Feynman contour, and what is the sign of its $i\varepsilon$?

> [!tip]- Hints: route in the notes
> - Technique: K13.
> - Step 1: derivation steps 1–3; Definition [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^def-c2b-6-2|§C2b.6.2]] Anti-Time-Ordered Product.

### The Feynman propagator as a distribution: the products θ·D_W ★

$D_W(\pm\xi)$ is smooth in $\xi^0$ with values in $\mathcal S'(\mathbb R^3)$, so $\theta(\pm\xi^0)D_W(\pm\xi)$ are defined slice by slice and $D_F \in \mathcal S'(\mathbb R^4)$; at $\xi = 0$ the slice definition is the unique extension that is a fundamental solution, see Theorem [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-4|§C2b.6.4]] The Feynman Propagator as a Distribution: the Products θ·D_W. *Source: the user's notes Ch. 5 §5.6, Ch. 6 §6.2, §6.7*

^nd-thm-c2b-6-4

- [ ] Q1 **[state]** State in which sense $\theta(\xi^0)D_W(\xi)$ is defined.
- [ ] Q2 **[why]** Why does the value $\theta(0)$ not enter?
- [ ] Q3 **[why]** At $\xi = 0$ both factors are singular. What selects the extension, and what would another extension add?

> [!tip]- Hints: route in the notes
> - Technique: K13.
> - Step 1: derivation steps 1–4; Theorem [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-6|§C2b.5.6]] The Product θ(ξ⁰)D Is Defined; Retarded Means Supported in the Future for the same argument with $D$.

### The free Schwinger–Dyson equation

For distinct times, $(\partial_x^2 + m^2)T\{\hat\phi(x)\hat\phi(y_1)\cdots\hat\phi(y_n)\} = -i\sum_k\delta^4(x - y_k)T\{\cdots\widehat{\hat\phi(y_k)}\cdots\}$; for $n = 1$, $(\partial^2 + m^2)D_F = -i\delta^4$, see Theorem [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-5|§C2b.6.5]] The Free Schwinger–Dyson Equation. The general-$n$ case repeats the $n = 1$ computation between consecutive times.

^nd-thm-c2b-6-5

→ drilled as [[PHY 513 PS Drill#^ps4-4-c|PS4.4(c)]] (the case $n = 1$)

### Contractions: normal ordering against time ordering ★

$\hat\phi(x)\hat\phi(y) = :\!\hat\phi(x)\hat\phi(y)\!: + D_W(x - y)$ and $T\{\hat\phi(x)\hat\phi(y)\} = :\!\hat\phi(x)\hat\phi(y)\!: + D_F(x - y)$, see Theorem [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-6|§C2b.6.6]] Contractions: Normal Ordering against Time Ordering. *Source: the user's notes Ch. 6 §6.7 ("a first look at Wick's theorem") · Yu eqs. (6.132)–(6.133)*

^nd-thm-c2b-6-6

- [ ] Q1 **[state]** State both decompositions.
- [ ] Q2 Split $\hat\phi = \hat\phi^+ + \hat\phi^-$ and expand $\hat\phi(x)\hat\phi(y)$. Which term is not normal ordered?
- [ ] Q3 Normal order it: why is the commutator $[\hat\phi^+(x), \hat\phi^-(y)]$ a number, and which number?
- [ ] Q4 Time order both sides. Why is $:\!\hat\phi(x)\hat\phi(y)\!:$ unaffected by time ordering?
- [ ] Q5 **[why]** This is the $n = 2$ case of which theorem, and what is the name of $D_F$ in this role?

> [!tip]- Hints: route in the notes
> - Technique: K11.
> - Step 1: derivation steps 1–4; Theorem [[§C2b.1 Heisenberg Fields#^thm-c2b-1-5|§C2b.1.5]] Positive and Negative Frequency; Definition [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^def-c2a-3-1|§C2a.3.1]] Normal Ordering.

### Normal ordering removes the coincident singularity ★

Between wave-packet states $:\!\hat\phi(x)\hat\phi(y)\!:$ has smooth matrix elements, including at $x = y$, so $:\!\hat\phi^2\!:$ is defined; the whole coincident singularity sits in the c-number $D_W$, see Theorem [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-7|§C2b.6.7]] Normal Ordering Removes the Coincident Singularity. *Source: the user's notes Ch. 6 §6.2, §6.7*

^nd-thm-c2b-6-7

- [ ] Q1 **[state]** State the three parts.
- [ ] Q2 Compute a one-particle matrix element of $:\!\hat\phi(x)\hat\phi(y)\!:$. Why is it smooth at $x = y$?
- [ ] Q3 **[why]** Why does a Wick power need smearing in spacetime to give a normalizable state?

> [!tip]- Hints: route in the notes
> - Technique: K9.
> - Step 1: derivation steps 1–5; Theorem [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-6|§C2b.3.6]] The Wightman Function as a Distribution: Off the Cone and on It part 2.

### The iε prescriptions ★★ [class exercise, Lecture 6]

Moving the poles off the real axis is equivalent to deforming the contour: $\tilde D_F = \frac{i}{p^2 - m^2 + i\varepsilon}$, $\tilde D_{\bar F} = \frac{i}{p^2 - m^2 - i\varepsilon}$, $\tilde D_R = \frac{i}{(p^0 + i\varepsilon)^2 - E_{\mathbf p}^2}$, $\tilde D_A = \frac{i}{(p^0 - i\varepsilon)^2 - E_{\mathbf p}^2}$, see Theorem [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-9|§C2b.6.9]] The $i\varepsilon$ Prescriptions. Larsen left the pole positions to the class: "It's up to you to go and say, oh, where do I have my zeros?". *Source: Lecture 6 (Sep 21), slides "Deforming Integrand: the Feynman Propagator", "Relativistic Form of Feynman Propagator"; transcript · PS §2.4, eq. (2.59) · Yu eq. (6.210) · the user's notes Ch. 6 §6.9*

^nd-thm-c2b-6-9

- [ ] Q1 **[state]** State the four $i\varepsilon$ forms.
- [ ] Q2 Find the zeros of $p^2 - m^2 + i\varepsilon$ in $p^0$ to first order in $\varepsilon$. On which side of the real axis does each lie?
- [ ] Q3 **[why]** Why is moving a pole down equivalent to passing it above?
- [ ] Q4 Start from poles at $p^0 = \pm(E_{\mathbf p} - i\varepsilon)$ and show the denominator is $p^2 - m^2 + i\varepsilon$ after renaming the infinitesimal. Which property of $E_{\mathbf p}$ is used?
- [ ] Q5 Do the same for the retarded poles. Why can $\tilde D_R$ not be written through $p^2$ alone?
- [ ] Q6 **[why]** Which of the four prescriptions are Lorentz invariant, and under which transformations?

> [!tip]- Hints: route in the notes
> - Technique: K13 ($i\varepsilon$).
> - Step 1: derivation steps 1–5; Theorem [[§CA.4 Contour Integration#^thm-ca-4-7|§CA.4.7]] Poles on the Contour: the Half-Residue Lemma; Theorem [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-6|§CA.6.6]] The iε Limits of the Propagator Denominators part 3.

### The iε prescription is a limit in 𝒮′ ★

For $\varepsilon > 0$, $i/(p^2 - m^2 + i\varepsilon)$ is a bounded smooth function; as $\varepsilon \to 0^+$ it tends to $i\mathcal P\frac{1}{p^2 - m^2} + \pi\delta(p^2 - m^2)$ in $\mathcal S'$, independently of how the infinitesimal is written, and its transform is the contour's $D_F$, see Theorem [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-10|§C2b.6.10]] The $i\varepsilon$ Prescription Is a Limit in 𝒮′. *Source: the user's notes Ch. 6 §6.9*

^nd-thm-c2b-6-10

- [ ] Q1 **[state]** State the limit and the claim about the form of the infinitesimal.
- [ ] Q2 Apply Sokhotski–Plemelj in $p^0$ at fixed $\mathbf p$. What are the real and imaginary parts?
- [ ] Q3 **[why]** Why may the Fourier transform be exchanged with the limit? Does the four-dimensional integral converge at fixed $\xi$?

> [!tip]- Hints: route in the notes
> - Technique: K13.
> - Step 1: derivation steps 1–6; Theorem [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-6|§CA.6.6]] The iε Limits of the Propagator Denominators; Theorem [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-2|§CA.3.2]] The Fourier Transform of Tempered Distributions part 2.

### Differences on the mass shell ★

$\tilde D_F - \tilde D_{\bar F} = 2\pi\delta(p^2 - m^2)$, $\tilde D_R - \tilde D_A = 2\pi\operatorname{sgn}(p^0)\delta(p^2 - m^2)$, $\tilde D_W = 2\pi\theta(p^0)\delta(p^2 - m^2)$, see Theorem [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-11|§C2b.6.11]] Differences on the Mass Shell. *Source: the user's notes Ch. 6 §6.9*

^nd-thm-c2b-6-11

- [ ] Q1 **[state]** State the three shell transforms.
- [ ] Q2 Derive the first two with Sokhotski–Plemelj.
- [ ] Q3 **[why]** Why must every difference of two Green's functions live on the shell?

> [!tip]- Hints: route in the notes
> - Technique: K13.
> - Step 1: derivation steps 1–2; Theorem [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-7|§CA.6.7]] Fundamental Solutions Differ by Homogeneous Solutions part 2.

### Wick rotation of a momentum integral ★★

If $F$ is analytic in the first and third quadrants of the $p^0$-plane and decays fast enough, the real $p^0$ axis can be rotated counterclockwise onto $p^0 = ip_4$ without crossing a Feynman pole, and $\int\frac{d^4p}{(2\pi)^4}\frac{iF(p)}{p^2 - m^2 + i\varepsilon} = \int\frac{d^4p_E}{(2\pi)^4}\frac{F(ip_4, \mathbf p)}{p_E^2 + m^2}$, see Theorem [[§C2b.7 Wick Rotation and the Two-Point Family#^thm-c2b-7-1|§C2b.7.1]] Wick Rotation of a Momentum Integral. *Source: Lecture 6 (Sep 21), slide "Another perspective: the Euclidean Green's Function" ("rotate 90° counter-clockwise") · the user's notes Ch. 6 §6.10*

^nd-thm-c2b-7-1

- [ ] Q1 **[state]** State the rotation and its hypotheses.
- [ ] Q2 Locate the Feynman poles: in which quadrants are they, and which quadrants does the rotation sweep?
- [ ] Q3 Close the contour with the two arcs. Why do they vanish?
- [ ] Q4 Substitute $p^0 = ip_4$: what do $dp^0$ and $p^2 - m^2$ become, and where does the $i$ go?
- [ ] Q5 **[why]** Why is the rotation forbidden with the retarded prescription?
- [ ] Q6 **[why]** With a factor $e^{-ip^0t}$ present, why may $p^0$ not be rotated alone?

> [!tip]- Hints: route in the notes
> - Technique: K13.
> - Step 1: derivation steps 1–4; Cauchy Theorem [[§CA.4 Contour Integration#^thm-ca-4-2|§CA.4.2]] Cauchy's Theorem; Deformation of Contours.
> - Step 2: P2, "Pitfalls" (Wick rotation with a time); Theorem [[§C2b.7 Wick Rotation and the Two-Point Family#^thm-c2b-7-2|§C2b.7.2]] The Feynman Function at Imaginary Time.

### The Feynman function at imaginary time ★

With $t = -i\tau$, $\tau > 0$, $D_F(-i\tau, \boldsymbol\xi) = D_E(\tau, \boldsymbol\xi)$, see Theorem [[§C2b.7 Wick Rotation and the Two-Point Family#^thm-c2b-7-2|§C2b.7.2]] The Feynman Function at Imaginary Time. *Source: Lecture 6 (Sep 21) · the user's notes Ch. 6 §6.10*

^nd-thm-c2b-7-2

- [ ] Q1 **[state]** State the identity and the direction of rotation of $t$.
- [ ] Q2 Which piece of $D_F$ is used for $\tau > 0$, and on which ray is it evaluated?
- [ ] Q3 **[why]** Why must $t$ be rotated together with $p^0$ so that $p^0t$ stays real?

> [!tip]- Hints: route in the notes
> - Technique: K13.
> - Step 1: derivation steps 1–3; Theorem [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-1|§C2b.3.1]] The Wightman Function at Imaginary Time.

### The Feynman function in position space ★

$D_F(\xi) = \frac{mK_1(ms)}{4\pi^2s}$ with $s = \sqrt{-\xi^2 + i\varepsilon}$ for all real $\xi$; even, real at spacelike separation, with the same branch for both signs of $\xi^0$: the infinitesimal Wick rotation $t \to t(1 - i\varepsilon)$, see Theorem [[§C2b.7 Wick Rotation and the Two-Point Family#^thm-c2b-7-3|§C2b.7.3]] The Feynman Function in Position Space. *Source: the user's notes Ch. 6 §6.10*

^nd-thm-c2b-7-3

- [ ] Q1 **[state]** State the formula and its branch.
- [ ] Q2 Combine the two orderings for $\xi^0 > 0$ and $\xi^0 < 0$ into one formula.
- [ ] Q3 **[why]** Why does time ordering correspond to "the same branch everywhere"? Compare with $D_W$ inside the cone.

> [!tip]- Hints: route in the notes
> - Technique: K13.
> - Step 1: derivation steps 1–4; Theorem [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-2|§C2b.3.2]] The Wightman Function in the Lower Half-Plane, Theorem [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-4|§C2b.3.4]] The Wightman Function at Timelike Separation.

### The late-time field of a classical source ★★

$\hat\phi(x) = \hat\phi_0(x) + i\int d^4y\,D_R(x - y)j(y)$; after the source has acted, $\hat\phi$ is free with $\hat b_{\mathbf p} = \hat a_{\mathbf p} + \frac{i\tilde j(p)}{\sqrt{2E_{\mathbf p}}}|_{p^0 = E_{\mathbf p}}$, and $[\hat b_{\mathbf p}, \hat b^\dagger_{\mathbf q}] = (2\pi)^3\delta^3(\mathbf p - \mathbf q)$, see Theorem [[§C2b.8 Particle Production by a Classical Source#^thm-c2b-8-1|§C2b.8.1]] The Late-Time Field. *Source: Lecture 6 (Sep 21), slides "Particle Production by Classical Source I–II" · PS §2.4, eqs. (2.63)–(2.64) · the user's notes Ch. 6 §6.13*

^nd-thm-c2b-8-1

- [ ] Q1 **[state]** State the retarded solution and the late-time mode operators.
- [ ] Q2 **[why]** Why the retarded function and not $D_F$? Which condition on the state fixes it?
- [ ] Q3 Insert $D_R$ in modes. Once $x^0$ is later than the support of $j$, what happens to $\theta(x^0 - y^0)$?
- [ ] Q4 Exchange the integrals: which four-dimensional transform of $j$ appears, and at which $p^0$?
- [ ] Q5 Sort the terms by frequency and read off $\hat b_{\mathbf p}$. Why is the algebra unchanged?
- [ ] Q6 **[conv]** Which sign of the exponent defines $\tilde j(p)$ in the vault and on the slide, and how does that sign put $\tilde j$ next to $\hat a_{\mathbf p}$ rather than $\hat a^\dagger_{\mathbf p}$?

> [!tip]- Hints: route in the notes
> - Technique: K9, K13.
> - Step 1: derivation steps 1–6; Definition [[§CA.3 Fourier Transforms and Fourier Tricks#^def-ca-3-1|§CA.3.1]] Fourier Transform in Space and Spacetime; [[§C2b.8 Particle Production by a Classical Source#^rem-c2b-8-2|§C2b.8, Remark: The boundary condition was physics]] (the boundary condition was physics).

### The final state is a coherent state ★

$\hat b_{\mathbf p}|0\rangle = \frac{i\tilde j(p)}{\sqrt{2E_{\mathbf p}}}|0\rangle$: the in-vacuum is a coherent state of the out-particles with $\eta_{\mathbf p} = i\tilde j(E_{\mathbf p}, \mathbf p)$, and the number produced is Poisson distributed, see Theorem [[§C2b.8 Particle Production by a Classical Source#^thm-c2b-8-2|§C2b.8.2]] The Final State Is a Coherent State. *Source: the user's notes Ch. 6 §6.13*

^nd-thm-c2b-8-2

- [ ] Q1 **[state]** State the eigenvalue equation and the identification of $\eta$.
- [ ] Q2 Derive the eigenvalue from the late-time $\hat b_{\mathbf p}$.
- [ ] Q3 **[why]** In what precise sense does a classical source produce classical radiation?

> [!tip]- Hints: route in the notes
> - Technique: K11.
> - Step 1: derivation steps 1–3; Definition [[§C2a.6 Coherent States and the Classical Field#^def-c2a-6-1|§C2a.6.1]] Coherent State of the Field; Theorem [[§C2a.6 Coherent States and the Classical Field#^thm-c2a-6-6|§C2a.6.6]] Poisson Number Statistics.

### Energy and number of particles produced ★★

$\Delta E = \int\frac{d^3p}{(2\pi)^3}\frac12|\tilde j(p)|^2$ and $\bar N = \int\frac{d^3p}{(2\pi)^3}\frac{|\tilde j(p)|^2}{2E_{\mathbf p}}$, $p^0 = E_{\mathbf p}$, see Theorem [[§C2b.8 Particle Production by a Classical Source#^thm-c2b-8-3|§C2b.8.3]] Energy and Number of Particles Produced. *Source: Lecture 6 (Sep 21), slide "Particle Production by Classical Source: Interpretation" · PS §2.4, eqs. (2.65)–(2.66) · the user's notes Ch. 6 §6.13*

^nd-thm-c2b-8-3

- [ ] Q1 **[state]** State $\Delta E$ and $\bar N$.
- [ ] Q2 Write the late-time Hamiltonian in the $\hat b$'s and express it through the $\hat a$'s.
- [ ] Q3 Take the expectation value in $|0\rangle$: which of the four terms of the product survive?
- [ ] Q4 **[why]** Only the on-shell part of $\tilde j$ enters. What does a static source produce, and why?
- [ ] Q5 **[why]** PS call $|\tilde j|^2/2E_{\mathbf p}$ a probability density. When is that reading correct?

> [!tip]- Hints: route in the notes
> - Technique: K9, K11.
> - Step 1: derivation steps 1–4; [[§C2b.8 Particle Production by a Classical Source#^rem-c2b-8-1|§C2b.8, Remark: Only the on-shell part of the source radiates]] (only the on-shell part radiates).

### The source is a test function; why N̄ is finite ★

For $j \in \mathcal D(\mathbb R^4)$, $\tilde j \in \mathcal S$, so $\bar N$ and $\Delta E$ are finite; $\bar N = \|\hat\phi_0(j)|0\rangle\|^2$; an instantaneous point source produces infinitely many particles, see Theorem [[§C2b.8 Particle Production by a Classical Source#^thm-c2b-8-4|§C2b.8.4]] The Source Is a Test Function; Why $\bar N$ Is Finite. *Source: the user's notes Ch. 6 §6.13, §6.2 · Problem Set 4, Problem 0*

^nd-thm-c2b-8-4

- [ ] Q1 **[state]** State the three parts.
- [ ] Q2 Show $\bar N = \|\hat\phi_0(j)|0\rangle\|^2$.
- [ ] Q3 **[why]** Why does smoothness in time matter most for finiteness?

> [!tip]- Hints: route in the notes
> - Technique: K9.
> - Step 1: derivation steps; Theorem [[§C2b.1 Heisenberg Fields#^thm-c2b-1-6|§C2b.1.6]] The Heisenberg Field Is an Operator-Valued Distribution on Spacetime part 1.

### A point source switched on and off ★

For $j = g\delta^3(\mathbf x)e^{-t^2/2T^2}/\sqrt{2\pi}T$, $\bar N = \frac{g^2m^2}{16\pi^2}e^{-z}[K_1(z) - K_0(z)]$ with $z = \frac12m^2T^2$; sudden switching gives $\bar N \simeq g^2/8\pi^2T^2$, adiabatic switching an exponentially small $\bar N$, see Example [[§C2b.8 Particle Production by a Classical Source#^ex-c2b-8-1|§C2b.8.1]] A Point Source Switched On and Off. *Source: worked in the vault from the user's notes Ch. 6 §6.13 and PS eq. (2.66)*

^nd-ex-c2b-8-1

- [ ] Q1 **[state]** State the source, the quantity to compute, and the two regimes to compare.
- [ ] Q2 Compute $\tilde j(p)$ on the shell.
- [ ] Q3 Reduce $\bar N$ to a one-dimensional integral over $E$.
- [ ] Q4 Substitute $E = m\cosh u$ and recognize the Bessel functions.
- [ ] Q5 Take the limits $mT \ll 1$ and $mT \gg 1$.
- [ ] Q6 **[why]** Why does a slowly switched source leave the field in its vacuum? Which quantum-mechanical theorem is this the analogue of?

> [!tip]- Hints: route in the notes
> - Technique: K9, K8.
> - Step 1: steps 1–5 of the example; Definition [[§CA.5 Gaussian Integrals, Stationary Phase and Bessel Functions#^def-ca-5-1|§CA.5.1]] Modified Bessel Function of the Second Kind; Theorem [[§CA.5 Gaussian Integrals, Stationary Phase and Bessel Functions#^thm-ca-5-3|§CA.5.3]] Properties of $K_\nu$ parts 2–3.

### Dominated convergence and differentiation under the integral ★

If $f_n \to f$ a.e. with $|f_n| \le g$, $\int g < \infty$, then $\int f_n \to \int f$; if $|\partial_rf(p, r)| \le g(p)$ integrable, then $F'(r) = \int\partial_rf\,dp$, see Theorem [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|§CA.1.1]] Dominated Convergence and Differentiation under the Integral. *Source: the user's notes App. A*

^nd-thm-ca-1-1

- [ ] Q1 **[state]** State both parts with their hypotheses.
- [ ] Q2 Where in C2b is a limit $\varepsilon \to 0^+$ exchanged with an integral by this theorem?
- [ ] Q3 **[why]** Why is a bound that worsens as $\varepsilon \to 0$ not enough?

> [!tip]- Hints: route in the notes
> - Technique: none.
> - Step 1: "What the derivation shows"; Theorem [[§C2b.2 The Wightman Function#^thm-c2b-2-5|§C2b.2.5]] The Wightman Function Is a Boundary Value; Theorem [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-2|§CA.6.2]] Sokhotski–Plemelj Formula.

### Conditionally convergent integrals: Dirichlet's test and Abel's theorem ★

If $g$ decreases monotonically to $0$ and $|\int_0^Ph| \le M$, then $\int_0^\infty gh$ converges; if $\int_0^\infty f$ converges, $\lim_{\varepsilon\to0^+}\int_0^\infty e^{-\varepsilon p}f = \int_0^\infty f$, see Theorem [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-2|§CA.1.2]] Conditionally Convergent Integrals: Dirichlet's Test and Abel's Theorem.

^nd-thm-ca-1-2

- [ ] Q1 **[state]** State both tests.
- [ ] Q2 Show that $\int_0^\infty\frac{\cos pr}{\sqrt{p^2 + m^2}}dp$ converges for $r > 0$.
- [ ] Q3 **[why]** What does Abel's theorem not license: removing a regulator from a divergent integral, or exchanging the limit with a derivative?

> [!tip]- Hints: route in the notes
> - Technique: none.
> - Step 1: the derivation; Theorem [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-3|§CA.1.3]] Limits of Derivatives.

### Limits of derivatives ★

If $F_n(r_0)$ converges and $F_n' \to G$ uniformly on an interval, then $F_n \to F$ with $F' = G$; pointwise convergence of the derivatives is not enough, see Theorem [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-3|§CA.1.3]] Limits of Derivatives.

^nd-thm-ca-1-3

- [ ] Q1 **[state]** State the theorem.
- [ ] Q2 In which evaluation of the Wightman function is this step needed?
- [ ] Q3 **[why]** Why does pointwise convergence of $F_n'$ not suffice?

> [!tip]- Hints: route in the notes
> - Technique: none.
> - Step 1: third route of Theorem [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-3|§C2b.3.3]] The Wightman Function at Spacelike Separation, step 4.

### Regular and singular tempered distributions ★

$\mathcal D$ is dense in $\mathcal S$; a locally integrable $\psi$ with polynomial growth defines a tempered distribution, injectively; $\partial^\alpha\delta$ is tempered and is no function, see Theorem [[§CA.2 Generalized Functions#^thm-ca-2-1|§CA.2.1]] Regular and Singular Tempered Distributions.

^nd-thm-ca-2-1

- [ ] Q1 **[state]** State the three parts.
- [ ] Q2 Which of $1$, $e^{i\mathbf k\cdot\mathbf x}$, $\theta(t)$, $1/|\mathbf x|^2$ on $\mathbb R^3$, $1/x$ on $\mathbb R$ define tempered distributions as functions?
- [ ] Q3 **[why]** Why does $1/x$ need the principal value?

> [!tip]- Hints: route in the notes
> - Technique: none.
> - Step 1: derivation; Definition [[§CA.2 Generalized Functions#^def-ca-2-10|§CA.2.10]] Principal Value.

### Distributions supported at a point ★

If $\operatorname{supp}T \subseteq \{a\}$ then $T = \sum_{|\alpha| \le N}c_\alpha\partial^\alpha\delta(x - a)$, see Theorem [[§CA.2 Generalized Functions#^thm-ca-2-2|§CA.2.2]] Distributions Supported at a Point.

^nd-thm-ca-2-2

- [ ] Q1 **[state]** State the theorem.
- [ ] Q2 **[why]** Why is this the freedom in extending $\theta(x^0)D(x)$ across $x = 0$?
- [ ] Q3 **[why]** What removes that freedom for a fundamental solution?

> [!tip]- Hints: route in the notes
> - Technique: none.
> - Step 1: Theorem [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-6|§C2b.5.6]] The Product θ(ξ⁰)D Is Defined; Retarded Means Supported in the Future; Theorem [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-7|§CA.6.7]] Fundamental Solutions Differ by Homogeneous Solutions part 3.

### Integration by parts; the gradient of a delta function ★

$\int_V(\partial_if)g = \oint_{\partial V}n_ifg - \int_Vf\partial_ig$; for fields falling off at infinity $\int\nabla f\cdot\nabla g = -\int f\nabla^2g$, and $\int d^3y\,f(\mathbf y)\nabla_{\mathbf y}\delta^3(\mathbf x - \mathbf y) = -\nabla f(\mathbf x)$, see Theorem [[§CA.2 Generalized Functions#^thm-ca-2-3|§CA.2.3]] Integration by Parts; the Gradient of a Delta Function.

^nd-thm-ca-2-3

- [ ] Q1 **[state]** State the three formulas.
- [ ] Q2 Derive the gradient-of-delta formula. Which factor kills the surface term?
- [ ] Q3 **[why]** Where is this used in the Heisenberg-equation derivation?

> [!tip]- Hints: route in the notes
> - Technique: none.
> - Step 1: derivation; Theorem [[§C2b.1 Heisenberg Fields#^thm-c2b-1-2|§C2b.1.2]] The Heisenberg Equations Are the Klein–Gordon Equation, step 5.

### Every generalized function is differentiable ★

Every generalized function has derivatives of all orders; $\theta' = \delta$ and $\delta'[\varphi] = -\varphi'(0)$, see Theorem [[§CA.2 Generalized Functions#^thm-ca-2-4|§CA.2.4]] Every Generalized Function Is Differentiable.

^nd-thm-ca-2-4

- [ ] Q1 **[state]** State the theorem.
- [ ] Q2 Prove $\theta' = \delta$ from the definition of the derivative.
- [ ] Q3 **[why]** Where does $\theta' = \delta$ produce the source of a Green's function?

> [!tip]- Hints: route in the notes
> - Technique: none.
> - Step 1: derivation; Theorem [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-1|§C2b.6.1]] Properties of Time Ordering part 4; P2, step 7.

### Distributional limits; nascent delta functions ★

Pointwise limits of tempered distributions are tempered; limits commute with derivatives and with multiplication by smooth polynomially bounded functions; $\rho_\varepsilon(x) = \varepsilon^{-n}\rho(x/\varepsilon) \to \delta$ for $\rho \in L^1$, $\int\rho = 1$, see Theorem [[§CA.2 Generalized Functions#^thm-ca-2-5|§CA.2.5]] Distributional Limits.

^nd-thm-ca-2-5

- [ ] Q1 **[state]** State the three parts.
- [ ] Q2 Prove part 3 for a test function $\varphi$ by the substitution $x = \varepsilon u$.
- [ ] Q3 **[why]** Why does the shape of a nascent delta not matter?

> [!tip]- Hints: route in the notes
> - Technique: none.
> - Step 1: derivation; dominated convergence Theorem [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|§CA.1.1]] Dominated Convergence and Differentiation under the Integral.

### Composition of δ with a function ★

$\delta(f(x)) = \sum_i\frac{\delta(x - x_i)}{|f'(x_i)|}$ over the simple zeros of $f$; in several variables $\delta(f)[\varphi] = \int_\Sigma\varphi\,dS/|\nabla f|$, see Theorem [[§CA.2 Generalized Functions#^thm-ca-2-6|§CA.2.6]] Composition of δ with a Function. Problem Set 3, Problem 1(d) gives the one-variable formula as a tool. *Source: Problem Set 3, Problem 1(d) · Lecture 4 (Sep 14), slide "Details on Normalization (HW)" ("Recall")*

^nd-thm-ca-2-6

- [ ] Q1 **[state]** State the one-variable formula and its hypothesis.
- [ ] Q2 Define $\delta(f(x))$ as a limit of $\rho_\varepsilon(f(x))$ and derive the formula near one simple zero.
- [ ] Q3 Apply it to $f(p^0) = (p^0)^2 - E_{\mathbf p}^2$.
- [ ] Q4 **[why]** What goes wrong at a zero with $f' = 0$, and why does $\delta(x^2)$ still exist on $\mathbb R^4$?

> [!tip]- Hints: route in the notes
> - Technique: K13 ($\delta(f(x))$).
> - Step 1: derivation; Theorem [[§CA.2 Generalized Functions#^thm-ca-2-7|§CA.2.7]] Invariant Distributions on the Mass Shell and the Light Cone.

### Invariant distributions on the mass shell and the light cone ★

$\theta(\pm p^0)\delta(p^2 - m^2)$ acts as $\varphi \mapsto \int d^3p\,\varphi(\pm E_{\mathbf p}, \mathbf p)/2E_{\mathbf p}$ and is Lorentz invariant; $\theta(\pm x^0)\delta(x^2)$ acts with $1/2r$ and is invariant; $\theta(p^0)$ alone is not, see Theorem [[§CA.2 Generalized Functions#^thm-ca-2-7|§CA.2.7]] Invariant Distributions on the Mass Shell and the Light Cone.

^nd-thm-ca-2-7

- [ ] Q1 **[state]** State the three parts.
- [ ] Q2 Derive the action of $\theta(p^0)\delta(p^2 - m^2)$ with the composition rule.
- [ ] Q3 **[why]** Why is $\theta(p^0)$ invariant on the shell but not by itself?

> [!tip]- Hints: route in the notes
> - Technique: K13, K14.
> - Step 1: derivation; Theorem [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-3|§C2a.4.3]] The Invariant Measure.

### Products with disjoint singular supports ★

$gT$ is defined for smooth $g$; $ST$ is defined when the singular supports are disjoint; in general no associative product extends both, since $(x\delta)\mathcal P\frac1x = 0$ while $\delta(x\mathcal P\frac1x) = \delta$, see Theorem [[§CA.2 Generalized Functions#^thm-ca-2-8|§CA.2.8]] Products with Disjoint Singular Supports.

^nd-thm-ca-2-8

- [ ] Q1 **[state]** State the three parts.
- [ ] Q2 Check $x\delta = 0$ and $x\mathcal P\frac1x = 1$.
- [ ] Q3 **[why]** Where do the singular supports of $\theta(x^0)$ and $D(x)$ meet, and what does that leave undefined?

> [!tip]- Hints: route in the notes
> - Technique: none.
> - Step 1: derivation; Theorem [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-6|§C2b.5.6]] The Product θ(ξ⁰)D Is Defined; Retarded Means Supported in the Future part 2.

### Products without a value: θ·δ, δ² and δ(0) ★

With smooth regularizations, $\theta_\varepsilon\delta_\varepsilon \to c\delta$ with $c$ depending on the regularization (any value in $[0, 1]$); $\delta_\varepsilon^2$ diverges; $\delta^n_\varepsilon(0) = \varepsilon^{-n}\rho(0)$ has no limit, see Theorem [[§CA.2 Generalized Functions#^thm-ca-2-9|§CA.2.9]] Products Without a Value: θ·δ, δ² and δ(0).

^nd-thm-ca-2-9

- [ ] Q1 **[state]** State the three parts.
- [ ] Q2 Compute $\lim\theta_\varepsilon\delta_\varepsilon$ for $\sigma = \rho$.
- [ ] Q3 **[why]** Where does each of these meaningless products appear in C2a–C2b, and how is each avoided?

> [!tip]- Hints: route in the notes
> - Technique: none.
> - Step 1: derivation; Theorem [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-2|§C2a.3.2]] δ³(0) Has No Value; in a Box It Is the Volume; Theorem [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-1|§C2b.6.1]] Properties of Time Ordering; [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^cau-c2b-6-1|§C2b.6, Caution: The step function at zero]].

### Box regularization of δ³(0) ★

In a periodic box of volume $V$, $\int_Vd^3x\,e^{i(\mathbf k - \mathbf k')\cdot\mathbf x} = V\delta_{\mathbf k\mathbf k'}$; as $L \to \infty$, $\sum_{\mathbf k} \leftrightarrow V\int\frac{d^3k}{(2\pi)^3}$ and $(2\pi)^3\delta^3(\mathbf 0) \leftrightarrow V$, see Theorem [[§CA.2 Generalized Functions#^thm-ca-2-10|§CA.2.10]] Box Regularization of δ³(0).

^nd-thm-ca-2-10

- [ ] Q1 **[state]** State the dictionary.
- [ ] Q2 Compute the box integral for $\mathbf k \neq \mathbf k'$ and for $\mathbf k = \mathbf k'$.
- [ ] Q3 **[why]** Is $\delta^3(\mathbf 0)$ an infrared or an ultraviolet divergence?

> [!tip]- Hints: route in the notes
> - Technique: none.
> - Step 1: derivation; Theorem [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-2|§C2a.3.2]] δ³(0) Has No Value; in a Box It Is the Volume.

### The kernel theorem ★

A bilinear form on $\mathcal S(\mathbb R^n) \times \mathcal S(\mathbb R^m)$, continuous in each argument, has a unique kernel $K \in \mathcal S'(\mathbb R^{n+m})$ with $B(f, g) = K[f \otimes g]$, see Theorem [[§CA.2 Generalized Functions#^thm-ca-2-11|§CA.2.11]] The Kernel Theorem. (Stated; one example worked.)

^nd-thm-ca-2-11

- [ ] Q1 **[state]** State the theorem.
- [ ] Q2 Name two two-point quantities of C2a–C2b whose kernels it defines.
- [ ] Q3 **[why]** How does the theorem justify reading "$[\hat\phi(\mathbf x), \hat\pi(\mathbf y)] = i\delta^3$" as an identity?

> [!tip]- Hints: route in the notes
> - Technique: none.
> - Step 1: Theorem [[§C2a.1 Canonical Quantization of Fields#^thm-c2a-1-3|§C2a.1.3]] The Canonical Relations Are Identities after Smearing; Theorem [[§C2b.2 The Wightman Function#^thm-c2b-2-2|§C2b.2.2]] The Wightman Function Is a Tempered Distribution.

### Fourier inversion and Plancherel on 𝒮 ★

The transform maps $\mathcal S$ onto $\mathcal S$ and inverts with the momentum measure $d^3k/(2\pi)^3$; $\int d^3x\,\bar fg = \int\frac{d^3k}{(2\pi)^3}\overline{\tilde f}\tilde g$, see Theorem [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-1|§CA.3.1]] Fourier Inversion and Plancherel on 𝒮.

^nd-thm-ca-3-1

- [ ] Q1 **[state]** State inversion, the multiplication formula and Plancherel in the vault's convention.
- [ ] Q2 **[conv]** On which side does the factor $(2\pi)^{-3}$ sit in Plancherel, and why?
- [ ] Q3 **[why]** Why are plane waves not covered by this theorem?

> [!tip]- Hints: route in the notes
> - Technique: none.
> - Step 1: derivation; Theorem [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-2|§CA.3.2]] The Fourier Transform of Tempered Distributions.

### The Fourier transform of tempered distributions ★

$\tilde T[\varphi] \equiv T[\tilde\varphi]$ is a bijection of $\mathcal S'$, continuous under limits; $\tilde\delta = 1$ and the transform of $1$ is $(2\pi)^n\delta^n$, see Theorem [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-2|§CA.3.2]] The Fourier Transform of Tempered Distributions.

^nd-thm-ca-3-2

- [ ] Q1 **[state]** State the three parts.
- [ ] Q2 Compute $\tilde\delta$ from the definition.
- [ ] Q3 **[why]** Why may an $i\varepsilon$ expression be transformed first and the limit taken afterwards?

> [!tip]- Hints: route in the notes
> - Technique: K13.
> - Step 1: derivation; Theorem [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-10|§C2b.6.10]] The $i\varepsilon$ Prescription Is a Limit in 𝒮′ part 3.

### Plane waves integrate to a delta function ★

$\int d^nx\,e^{i\mathbf k\cdot\mathbf x} = (2\pi)^n\delta^n(\mathbf k)$ and $\int d^4x\,e^{ip\cdot x} = (2\pi)^4\delta^4(p)$ as tempered distributions; the $\mathbf x$ integral alone converges for no $\mathbf k$, see Theorem [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|§CA.3.3]] Plane Waves Integrate to a Delta Function.

^nd-thm-ca-3-3

- [ ] Q1 **[state]** State the identity and its precise meaning (which integral is done first).
- [ ] Q2 Derive it from Fourier inversion.
- [ ] Q3 Second route: compute the box integral $\int_{[-L, L]^n}$ and take $L \to \infty$ against a test function.
- [ ] Q4 **[why]** Different regulators give the same distribution. What do they assign to $\delta^n(\mathbf 0)$?

> [!tip]- Hints: route in the notes
> - Technique: none.
> - Step 1: both derivations; Theorem [[§CA.2 Generalized Functions#^thm-ca-2-10|§CA.2.10]] Box Regularization of δ³(0).

### Rules of the Fourier transform ★

Plane waves give deltas; $\partial_\mu \leftrightarrow -ip_\mu$, so $\partial^2 + m^2 \leftrightarrow m^2 - p^2$; convolution becomes a product; real $f$ gives $\tilde f(-p) = \overline{\tilde f(p)}$, scalars give scalars, see Theorem [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-4|§CA.3.4]] Rules of the Fourier Transform.

^nd-thm-ca-3-4

- [ ] Q1 **[state]** State the four rules.
- [ ] Q2 Derive $\partial_\mu \leftrightarrow -ip_\mu$ from $f(x) = \int\frac{d^4p}{(2\pi)^4}\tilde fe^{-ip\cdot x}$.
- [ ] Q3 **[conv]** With this convention, what does $\partial^2 + m^2$ become, and with which sign?

> [!tip]- Hints: route in the notes
> - Technique: none.
> - Step 1: derivation; [[§CA.3 Fourier Transforms and Fourier Tricks#^rem-ca-3-1|§CA.3, Remark: A linear equation becomes algebra]]; [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^cau-c2b-6-2|§C2b.6, Caution: Signs that slip]].

### Translation, phase, and the rules in 𝒮′ ★

$f(x - a)$ has transform $e^{ip\cdot a}\tilde f(p)$; $e^{-iq\cdot x}f$ has $\tilde f(p - q)$; the derivative rule holds for every $T \in \mathcal S'$, the convolution rule for $D \in \mathcal S'$ and $j \in \mathcal S$, see Theorem [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-5|§CA.3.5]] Translation, Phase, and the Rules in 𝒮′.

^nd-thm-ca-3-5

- [ ] Q1 **[state]** State the translation and phase rules in the vault's convention.
- [ ] Q2 **[why]** Under what condition does the convolution rule hold, and why is that the case for a Green's function acting on a source?
- [ ] Q3 How does translation invariance of a two-point function show up in its transform?

> [!tip]- Hints: route in the notes
> - Technique: none.
> - Step 1: derivation; Theorem [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-8|§CA.6.8]] Convolution with a Fundamental Solution Solves the Sourced Equation.

### Exchanging the space and momentum integrals ★

For wave packets $A, B \in \mathcal S$, $\int d^3x\,a(\mathbf x)b(\mathbf x) = \int\frac{d^3p}{(2\pi)^3}A(\mathbf p)B(-\mathbf p)$, every integral absolutely convergent; the physicists' route through $(2\pi)^3\delta^3(\mathbf p + \mathbf q)$ computes the same number, see Theorem [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-6|§CA.3.6]] Exchanging the Space and Momentum Integrals.

^nd-thm-ca-3-6

- [ ] Q1 **[state]** State the identity.
- [ ] Q2 Derive it by Fubini and Fourier inversion.
- [ ] Q3 **[why]** For operator coefficients such as $\hat a_{\mathbf p}$, in which sense does the identity hold?

> [!tip]- Hints: route in the notes
> - Technique: K9.
> - Step 1: derivation; [[§C2a.2 Mode Expansion and the Mode Algebra#^rem-c2a-2-2|§C2a.2, Remark: Two bookkeeping rules for mode integrals]].

### Changes of integration variable ★

Over all of $\mathbb R^n$: relabel $\mathbf p \to -\mathbf p$, shift, rescale (with $|\lambda|^n$), rotate or boost; the domain is unchanged and $E_{-\mathbf p} = E_{R\mathbf p} = E_{\mathbf p}$, see Theorem [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|§CA.3.7]] Changes of Integration Variable: Relabelling, Shifting, Rescaling, Rotating.

^nd-thm-ca-3-7

- [ ] Q1 **[state]** State the four changes and the Jacobian of each.
- [ ] Q2 **[why]** What is the one thing to track in a relabelling, and what does a dropped sign produce in a commutator?
- [ ] Q3 **[why]** Why is a box not shift invariant unless the functions are periodic?

> [!tip]- Hints: route in the notes
> - Technique: K9.
> - Step 1: derivation; Theorem [[§CA.2 Generalized Functions#^thm-ca-2-10|§CA.2.10]] Box Regularization of δ³(0).

### Angular integrals [class exercise, Lecture 5]

For radial $f$, $\int d^3p\,f(|\mathbf p|)e^{i\mathbf p\cdot\mathbf r} = \frac{4\pi}{r}\int_0^\infty dp\,pf(p)\sin pr$; $\int d^3p\,p^if = 0$, $\int d^3p\,p^ip^jf = \frac13\delta^{ij}\int d^3p\,\mathbf p^2f$; $p^ie^{i\mathbf p\cdot\mathbf r} = -i\partial_{r^i}e^{i\mathbf p\cdot\mathbf r}$, see Theorem [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-8|§CA.3.8]] Angular Integrals. In Lecture 5 the angular integral of the equal-time Wightman function was left to practise ("this integral, I think I did tell you that you practice"); its use for $D_W$ is part of PS4.3(a). *Source: Lecture 5 (Sep 16), transcript · Problem Set 4, Problem 3(a)*

^nd-thm-ca-3-8

- [ ] Q1 **[state]** State the three formulas.
- [ ] Q2 Derive part 1: choose the polar axis along $\mathbf r$ and do the $\cos\theta$ integral.
- [ ] Q3 Derive part 2 by symmetry: why must the first vanish and the second be proportional to $\delta^{ij}$? Fix the constant by taking the trace.
- [ ] Q4 **[why]** Why is "choose the polar axis along $\mathbf r$" legitimate?

> [!tip]- Hints: route in the notes
> - Technique: K1 (convenient frame).
> - Step 1: derivation; Theorem [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|§CA.3.7]] Changes of Integration Variable: Relabelling, Shifting, Rescaling, Rotating part 4; second route of Theorem [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-3|§C2b.3.3]] The Wightman Function at Spacelike Separation, step 2.

### Fourier transforms of Lorentz-invariant functions ★

An invariant $\tilde f$ has an invariant $f$, a function of $x^2$ (and of $\operatorname{sgn}x^0$ inside the cone); the Euclidean radial transform is $\frac{4\pi^2}{R}\int_0^\infty dp\,p^2F(p)J_1(pR)$; in Minkowski signature choose the frame, see Theorem [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-9|§CA.3.9]] Fourier Transforms of Lorentz-Invariant Functions.

^nd-thm-ca-3-9

- [ ] Q1 **[state]** State the three parts.
- [ ] Q2 Which frame is chosen at spacelike $x$, and which at timelike $x$, and what does each reduce the integral to?
- [ ] Q3 **[why]** Why can a continuous invariant function depend on $\operatorname{sgn}x^0$ only inside the cone?

> [!tip]- Hints: route in the notes
> - Technique: K1, K14.
> - Step 1: derivation; Theorem [[§C2b.2 The Wightman Function#^thm-c2b-2-3|§C2b.2.3]] Lorentz Invariance of the Wightman Function.

### Cauchy's theorem; deformation of contours ★

If $f$ is analytic on and inside a closed contour, $\oint f\,dz = 0$; integrals between two points do not depend on the path as long as no singularity is crossed, see Theorem [[§CA.4 Contour Integration#^thm-ca-4-2|§CA.4.2]] Cauchy's Theorem; Deformation of Contours. *Source: Problem Set 4, Problem 1 (text) · Lecture 6 (Sep 21), slide "Complex Analysis: a Survival Guide"*

^nd-thm-ca-4-2

- [ ] Q1 **[state]** State Cauchy's theorem and the deformation principle.
- [ ] Q2 Derive it from Green's theorem and the Cauchy–Riemann equations.
- [ ] Q3 **[why]** Where are contours moved in C2b, and what must never be crossed?

> [!tip]- Hints: route in the notes
> - Technique: K13.
> - Step 1: derivation; Theorem [[§CA.4 Contour Integration#^thm-ca-4-9|§CA.4.9]] Working Rules for Contour Integrals part 4.

### Identity theorem ★

Analytic $f$, $g$ on a connected open set that agree on a set with an accumulation point agree everywhere; analytic continuation is unique, see Theorem [[§CA.4 Contour Integration#^thm-ca-4-3|§CA.4.3]] Identity Theorem.

^nd-thm-ca-4-3

- [ ] Q1 **[state]** State the theorem.
- [ ] Q2 How is it used to get the Wightman function everywhere from one Euclidean evaluation?
- [ ] Q3 **[why]** Why is connectedness essential?

> [!tip]- Hints: route in the notes
> - Technique: K13.
> - Step 1: Theorem [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-2|§C2b.3.2]] The Wightman Function in the Lower Half-Plane, step 5.

### Computing residues ★

At a simple pole $\operatorname{Res} = \lim(z - z_0)f = g(z_0)/h'(z_0)$; at a pole of order $k$ by $k - 1$ derivatives; for the propagator integrand, $\operatorname{Res}_{p^0 = \pm E}\frac{e^{-ip^0t}}{(p^0)^2 - E^2} = \pm\frac{e^{\mp iEt}}{2E}$, see Theorem [[§CA.4 Contour Integration#^thm-ca-4-4|§CA.4.4]] Computing Residues.

^nd-thm-ca-4-4

- [ ] Q1 **[state]** State the rules for simple poles and poles of order $k$.
- [ ] Q2 Compute both residues of the propagator integrand.
- [ ] Q3 **[why]** Which residue carries the positive-energy wave, and which becomes the reversed Wightman function?

> [!tip]- Hints: route in the notes
> - Technique: K13.
> - Step 1: derivation; P2, step 2.

### Residue theorem ★

$\oint_\Gamma f\,dz = \pm2\pi i\sum_k\operatorname{Res}_{z_k}f$ over the enclosed singularities, $+$ counterclockwise, $-$ clockwise, see Theorem [[§CA.4 Contour Integration#^thm-ca-4-5|§CA.4.5]] Residue Theorem.

^nd-thm-ca-4-5

- [ ] Q1 **[state]** State the theorem with the orientation sign.
- [ ] Q2 Derive it from Cauchy's theorem and the basic integral $\oint(z - z_0)^n dz$.
- [ ] Q3 **[why]** What happens to a pole lying on $\Gamma$?

> [!tip]- Hints: route in the notes
> - Technique: K13.
> - Step 1: derivation; Theorem [[§CA.4 Contour Integration#^thm-ca-4-1|§CA.4.1]] The ML Inequality and the Basic Integral; Theorem [[§CA.4 Contour Integration#^thm-ca-4-7|§CA.4.7]] Poles on the Contour: the Half-Residue Lemma.

### Closing the contour: the ML estimate and Jordan's lemma ★

On the upper semicircle $C_R$: if $|f| \le C/R^{1+\delta}$ the arc vanishes; if $\max|g| \to 0$ and $\lambda > 0$, $\int_{C_R}ge^{i\lambda z}dz \to 0$; so close $e^{-ip^0t}$ upward for $t < 0$ and downward for $t > 0$, see Theorem [[§CA.4 Contour Integration#^thm-ca-4-6|§CA.4.6]] Closing the Contour: the ML Estimate and Jordan's Lemma.

^nd-thm-ca-4-6

- [ ] Q1 **[state]** State both estimates.
- [ ] Q2 Prove the ML estimate for the arc. Why is $1/R^{1+\delta}$ needed?
- [ ] Q3 For $e^{-ip^0t}$, compute $|e^{-ip^0t}|$ and decide where to close for each sign of $t$.
- [ ] Q4 **[why]** The sign of $t$ decides the contour. What physical statement does that encode?

> [!tip]- Hints: route in the notes
> - Technique: K13.
> - Step 1: derivation; [[§CA.4 Contour Integration#^cau-ca-4-1|§CA.4, Caution: Jordan's lemma needs g → 0]]; P2, step 4.

### Poles on the contour: the half-residue lemma ★

Passing a simple pole above (clockwise small semicircle) contributes $-i\pi\operatorname{Res}$, below $+i\pi\operatorname{Res}$; so the two passings differ by $2\pi i\operatorname{Res}$ and the principal value is their average, see Theorem [[§CA.4 Contour Integration#^thm-ca-4-7|§CA.4.7]] Poles on the Contour: the Half-Residue Lemma.

^nd-thm-ca-4-7

- [ ] Q1 **[state]** State the lemma.
- [ ] Q2 Compute the small semicircle integral of $g/(z - x_0)$ as its radius tends to zero.
- [ ] Q3 **[why]** Why is passing above a pole the same as moving the pole down by $i\varepsilon$?

> [!tip]- Hints: route in the notes
> - Technique: K13.
> - Step 1: derivation; Theorem [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-2|§CA.6.2]] Sokhotski–Plemelj Formula, second route.

### A step function from a pole ★

$\lim_{\varepsilon\to0^+}\int\frac{dx}{2\pi i}\frac{e^{ikx}}{x - i\varepsilon} = \theta(k)$, see Example [[§CA.4 Contour Integration#^ex-ca-4-2|§CA.4.2]] A Step Function from a Pole.

^nd-ex-ca-4-2

- [ ] Q1 **[state]** State the result.
- [ ] Q2 For $k > 0$ and $k < 0$: where do you close, and which pole is enclosed?
- [ ] Q3 **[why]** Read $k$ as a time: what does the side of the pole decide?

> [!tip]- Hints: route in the notes
> - Technique: K13.
> - Step 1: the example; Theorem [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-5|§CA.6.5]] Damping Factors: the Transform of the Step Function.

### Integrals around a branch cut ★

A branch point has no Laurent series and no residue; make the function single-valued by a cut and deform the contour onto it, so the integral becomes the integral of the discontinuity, see Theorem [[§CA.4 Contour Integration#^thm-ca-4-8|§CA.4.8]] Integrals around a Branch Cut.

^nd-thm-ca-4-8

- [ ] Q1 **[state]** State the procedure.
- [ ] Q2 For $\sqrt{p^2 + m^2}$, where are the branch points, and where does the equal-time Wightman computation put the cut?
- [ ] Q3 **[why]** Why do the lips' values depend on the branch but the total does not?

> [!tip]- Hints: route in the notes
> - Technique: K13.
> - Step 1: derivation; second route of Theorem [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-3|§C2b.3.3]] The Wightman Function at Spacelike Separation, steps 4–6.

### Working rules for contour integrals ★

Orientation sign; close where the integrand decays; check the arc (ML or Jordan); deform freely through analyticity; residues by $g/h'$; poles on the path need a prescription; branch points need cuts, see Theorem [[§CA.4 Contour Integration#^thm-ca-4-9|§CA.4.9]] Working Rules for Contour Integrals.

^nd-thm-ca-4-9

- [ ] Q1 **[state]** List the seven rules from memory.
- [ ] Q2 Apply them to $\int\frac{dp^0}{2\pi}\frac{ie^{-ip^0t}}{(p^0)^2 - E^2}$ on the Feynman contour for $t > 0$.
- [ ] Q3 **[why]** Which rule fails silently most often, and how do you check it?

> [!tip]- Hints: route in the notes
> - Technique: K13.
> - Step 1: the theorem box; P2.

### Gaussian integrals in n dimensions; Schwinger parametrization ★

$\int\frac{d^np}{(2\pi)^n}e^{-s\mathbf p^2 + i\mathbf p\cdot\mathbf x} = (4\pi s)^{-n/2}e^{-\mathbf x^2/4s}$ for $\operatorname{Re}s > 0$; $\frac{1}{A^\nu} = \frac{1}{\Gamma(\nu)}\int_0^\infty ds\,s^{\nu - 1}e^{-sA}$, see Theorem [[§CA.5 Gaussian Integrals, Stationary Phase and Bessel Functions#^thm-ca-5-1|§CA.5.1]] Gaussian Integrals in n Dimensions; Schwinger Parametrization.

^nd-thm-ca-5-1

- [ ] Q1 **[state]** State both formulas.
- [ ] Q2 Derive the Gaussian by completing the square in one dimension.
- [ ] Q3 **[why]** Why does Schwinger's trick help with $1/(p_E^2 + m^2)$?

> [!tip]- Hints: route in the notes
> - Technique: none.
> - Step 1: derivation; [[§CA.5 Gaussian Integrals, Stationary Phase and Bessel Functions#^rem-ca-5-1|§CA.5, Remark: Why the parametrization helps]]; Theorem [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-1|§C2b.3.1]] The Wightman Function at Imaginary Time, steps 3–4.

### Steepest descent and Laplace's method ★

For $I(\lambda) = \int fe^{\lambda\Phi}$, $\lambda \gg 1$: Laplace at a real maximum, steepest descent through a complex saddle; $|I| \propto e^{\lambda\operatorname{Re}\Phi(p_0)}$, see Theorem [[§CA.5 Gaussian Integrals, Stationary Phase and Bessel Functions#^thm-ca-5-2|§CA.5.2]] Steepest Descent and Laplace's Method.

^nd-thm-ca-5-2

- [ ] Q1 **[state]** State both versions with their prefactors.
- [ ] Q2 Derive Laplace's method by expanding $\Phi$ to second order.
- [ ] Q3 **[why]** What fixes the exponent, and what only the prefactor?

> [!tip]- Hints: route in the notes
> - Technique: none.
> - Step 1: derivation; [[§CA.5 Gaussian Integrals, Stationary Phase and Bessel Functions#^rem-ca-5-2|§CA.5, Remark: When the saddle sits on a branch cut]].

### The exponent of the Wightman function outside the light cone ★

For $0 < t < r$, the saddle of $S(p) = pr - t\sqrt{p^2 + m^2}$ is at $p_0 = imr/\rho$, $\rho = \sqrt{r^2 - t^2}$, giving $D_W \simeq \frac{\sqrt m}{2(2\pi\rho)^{3/2}}e^{-m\rho}$, see Example [[§CA.5 Gaussian Integrals, Stationary Phase and Bessel Functions#^ex-ca-5-1|§CA.5.1]] The Exponent of the Wightman Function Outside the Light Cone.

^nd-ex-ca-5-1

- [ ] Q1 **[state]** State the leading behaviour.
- [ ] Q2 Find the stationary points inside and outside the cone. Why is the saddle complex outside?
- [ ] Q3 Evaluate $S(p_0)$ and $S''(p_0)$, choosing the branch by the saddle condition.
- [ ] Q4 **[why]** Why does Laplace's method on the cut give the same answer?

> [!tip]- Hints: route in the notes
> - Technique: K13.
> - Step 1: steps 1–8 of the example.

### Properties of K_ν ★

Recursion $K_{\nu+1} - K_{\nu-1} = \frac{2\nu}{z}K_\nu$, $\frac{d}{dz}[z^{-\nu}K_\nu] = -z^{-\nu}K_{\nu+1}$; large argument $\sqrt{\pi/2z}e^{-z}[1 + \frac{4\nu^2 - 1}{8z}]$; small argument $K_1 \simeq 1/z$, $K_0 \simeq -\ln\frac z2 - \gamma_E$, see Theorem [[§CA.5 Gaussian Integrals, Stationary Phase and Bessel Functions#^thm-ca-5-3|§CA.5.3]] Properties of $K_\nu$.

^nd-thm-ca-5-3

- [ ] Q1 **[state]** State the recursion, the derivative rule and the two asymptotic forms.
- [ ] Q2 Derive the large-argument form by Laplace's method at $u = 0$.
- [ ] Q3 **[why]** Which ends of $K_1$ give the light-cone singularity and the Compton-length decay?

> [!tip]- Hints: route in the notes
> - Technique: none.
> - Step 1: derivation; Theorem [[§CA.5 Gaussian Integrals, Stationary Phase and Bessel Functions#^thm-ca-5-2|§CA.5.2]] Steepest Descent and Laplace's Method.

### Further representations of K_ν; imaginary argument ★

$\int_m^\infty\frac{\rho e^{-\rho r}d\rho}{\sqrt{\rho^2 - m^2}} = mK_1(mr)$; $K_0(x) = \int_0^\infty\frac{\cos xt}{\sqrt{t^2 + 1}}dt$; $K_1(ix) = -\frac\pi2[J_1(x) - iY_1(x)]$, see Theorem [[§CA.5 Gaussian Integrals, Stationary Phase and Bessel Functions#^thm-ca-5-4|§CA.5.4]] Further Representations; Imaginary Argument.

^nd-thm-ca-5-4

- [ ] Q1 **[state]** State the cut representation of $mK_1(mr)$ and the continuation to imaginary argument.
- [ ] Q2 Derive the cut representation by the substitution $\rho = m\cosh u$.
- [ ] Q3 **[why]** How does decay outside the cone turn into oscillation inside?

> [!tip]- Hints: route in the notes
> - Technique: none.
> - Step 1: derivation; Theorem [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-4|§C2b.3.4]] The Wightman Function at Timelike Separation.

### Boundary values of analytic functions are distributions ★

If $F$ is analytic on a strip above the real axis with a polynomial bound in $x$ and $y^{-k}$, then $F(x + i0)$ exists in $\mathcal S'$; in $n$ variables, from a tube over an open convex cone, independently of the direction of approach, see Theorem [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-1|§CA.6.1]] Boundary Values of Analytic Functions Are Distributions.

^nd-thm-ca-6-1

- [ ] Q1 **[state]** State the one-variable version.
- [ ] Q2 Name three boundary values used in C2b.
- [ ] Q3 **[why]** What is assigned a value at $\varepsilon = 0$, and what is not?

> [!tip]- Hints: route in the notes
> - Technique: K13.
> - Step 1: derivation; Theorem [[§C2b.2 The Wightman Function#^thm-c2b-2-5|§C2b.2.5]] The Wightman Function Is a Boundary Value.

### Sokhotski–Plemelj formula ★

$\frac{1}{x - x_0 \pm i\varepsilon} \to \mathcal P\frac{1}{x - x_0} \mp i\pi\delta(x - x_0)$ as generalized functions, see Theorem [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-2|§CA.6.2]] Sokhotski–Plemelj Formula. Problem Set 4 gives it as a tool (eq. (11)) for Problem 2(b). *Source: Problem Set 4, eq. (11) · the user's notes App. A §A.5*

^nd-thm-ca-6-2

- [ ] Q1 **[state]** State the formula with signs.
- [ ] Q2 Split $\frac{1}{s + i\varepsilon}$ into real and imaginary parts.
- [ ] Q3 Show that the real part, paired with a test function, tends to the principal value.
- [ ] Q4 Show that the imaginary part is a nascent delta function with total weight $\pi$.
- [ ] Q5 Second route: rederive it from the half-residue lemma. What does this route need that the first does not?
- [ ] Q6 **[why]** Why is the formula empty at $x \neq x_0$?

> [!tip]- Hints: route in the notes
> - Technique: K13 (Sokhotski–Plemelj).
> - Step 1: direct derivation (Lorentzian real and imaginary parts); Theorem [[§CA.2 Generalized Functions#^thm-ca-2-5|§CA.2.5]] Distributional Limits part 3; Definition [[§CA.2 Generalized Functions#^def-ca-2-10|§CA.2.10]] Principal Value.
> - Step 2: second route, Theorem [[§CA.4 Contour Integration#^thm-ca-4-7|§CA.4.7]] Poles on the Contour: the Half-Residue Lemma; [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^cau-ca-6-1|§CA.6, Caution: What the formula does and does not say]].

### Logarithm and powers at the real axis ★

$\log(x \pm i0) = \ln|x| \pm i\pi\theta(-x)$; its derivative is $\frac{1}{x \pm i0} = \mathcal P\frac1x \mp i\pi\delta$; $\frac{1}{(x \pm i0)^2}$ by one more derivative, see Theorem [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-3|§CA.6.3]] Logarithm and Powers at the Real Axis.

^nd-thm-ca-6-3

- [ ] Q1 **[state]** State the three formulas.
- [ ] Q2 Derive the first from the principal branch of $\log$.
- [ ] Q3 **[why]** Why is the logarithm the mildest boundary value, and where do such logarithms appear in $D_W$?

> [!tip]- Hints: route in the notes
> - Technique: K13.
> - Step 1: derivation; Theorem [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-5|§C2b.3.5]] The Wightman Function near the Light Cone.

### The light-cone boundary value ★

$F_\varepsilon = 1/(-(t - i\varepsilon)^2 + r^2)$ converges in $\mathcal S'(\mathbb R^4)$ to $1/(-x^2 + i0x^0)$, with imaginary part $-\pi\operatorname{sgn}(x^0)\delta(x^2)$ and real part $-\mathcal P\frac{1}{x^2}$; Lorentz invariant, singular on the cone, see Theorem [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-4|§CA.6.4]] The Light-Cone Boundary Value.

^nd-thm-ca-6-4

- [ ] Q1 **[state]** State the limit and its real and imaginary parts.
- [ ] Q2 Use partial fractions in $t$ at fixed $r$ and apply Sokhotski–Plemelj to each term.
- [ ] Q3 **[why]** The prescription singles out $x^0$. Why is the limit still Lorentz invariant?

> [!tip]- Hints: route in the notes
> - Technique: K13.
> - Step 1: derivation; Theorem [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-8|§C2b.4.8]] Commutator and Hadamard Functions of the Massless Field, steps 2–5.

### Damping factors: the transform of the step function ★

$\int_0^\infty dt\,e^{i\omega t - \varepsilon t} = \frac{i}{\omega + i\varepsilon}$, so $\tilde\theta(\omega) = \frac{i}{\omega + i0} = i\mathcal P\frac1\omega + \pi\delta(\omega)$; conversely the inverse transform of $\frac{i}{\omega + i\varepsilon}$ is $\theta(t)e^{-\varepsilon t}$, see Theorem [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-5|§CA.6.5]] Damping Factors: the Transform of the Step Function.

^nd-thm-ca-6-5

- [ ] Q1 **[state]** State the transform of $\theta$.
- [ ] Q2 Compute the damped integral and take the limit.
- [ ] Q3 **[why]** On which side of the real axis does damping on $t > 0$ put the pole, and what does that encode?

> [!tip]- Hints: route in the notes
> - Technique: K13.
> - Step 1: derivation; Example [[§CA.4 Contour Integration#^ex-ca-4-2|§CA.4.2]] A Step Function from a Pole.

### The iε limits of the propagator denominators ★

$\frac{i}{p^2 - m^2 + i\varepsilon} \to i\mathcal P\frac{1}{p^2 - m^2} + \pi\delta(p^2 - m^2)$; $\frac{1}{(p^0 + i\varepsilon)^2 - \mathbf p^2 - m^2} \to \mathcal P\frac{1}{p^2 - m^2} - i\pi\operatorname{sgn}(p^0)\delta(p^2 - m^2)$; replacing $\varepsilon$ by $\varepsilon c(\mathbf p)$, $c > 0$, changes nothing, see Theorem [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-6|§CA.6.6]] The iε Limits of the Propagator Denominators.

^nd-thm-ca-6-6

- [ ] Q1 **[state]** State both limits and the claim about $c(\mathbf p)$.
- [ ] Q2 At fixed $\mathbf p$, factor the denominator in $p^0$ and apply Sokhotski–Plemelj at each zero.
- [ ] Q3 Where does $\operatorname{sgn}(p^0)$ come from in the retarded case?
- [ ] Q4 **[why]** Why may $2E_{\mathbf p}\varepsilon$ be renamed $\varepsilon$?

> [!tip]- Hints: route in the notes
> - Technique: K13.
> - Step 1: derivation; Theorem [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-2|§CA.6.2]] Sokhotski–Plemelj Formula; Theorem [[§CA.2 Generalized Functions#^thm-ca-2-6|§CA.2.6]] Composition of δ with a Function.

### Fundamental solutions differ by homogeneous solutions ★

Two fundamental solutions differ by a homogeneous solution, and conversely; for tempered Klein–Gordon solutions $(m^2 - p^2)\tilde H = 0$ puts $\tilde H$ on the shell; a homogeneous solution supported at a point is zero, see Theorem [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-7|§CA.6.7]] Fundamental Solutions Differ by Homogeneous Solutions.

^nd-thm-ca-6-7

- [ ] Q1 **[state]** State the three parts.
- [ ] Q2 Show that $\operatorname{supp}\tilde H$ lies on the shell.
- [ ] Q3 **[why]** Why does part 3 remove the δ-ambiguity in extending $\theta(x^0)D$?

> [!tip]- Hints: route in the notes
> - Technique: K13.
> - Step 1: derivation; Theorem [[§CA.2 Generalized Functions#^thm-ca-2-2|§CA.2.2]] Distributions Supported at a Point; Theorem [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-6|§C2b.5.6]] The Product θ(ξ⁰)D Is Defined; Retarded Means Supported in the Future.

### Convolution with a fundamental solution solves the sourced equation ★

For a test-function source $j$, $\phi(x) = iG[j(x - \cdot)]$ is smooth and $P(\partial)\phi = j$, see Theorem [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-8|§CA.6.8]] Convolution with a Fundamental Solution Solves the Sourced Equation.

^nd-thm-ca-6-8

- [ ] Q1 **[state]** State the theorem.
- [ ] Q2 Prove it: move the derivatives onto $j$ and use the definition of a fundamental solution.
- [ ] Q3 **[why]** Why must the source be a test function for the result to be smooth?

> [!tip]- Hints: route in the notes
> - Technique: none.
> - Step 1: derivation; Definition [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^def-ca-6-1|§CA.6.1]] Fundamental Solution; Definition [[§C2b.5 Green's Functions and Contours#^def-c2b-5-1|§C2b.5.1]] Green's Function of the Klein–Gordon Operator.

### Basic contour integrals and Lorentzian integrals

$\oint(z - z_0)^n dz = 2\pi i\delta_{n,-1}$ on a counterclockwise circle (Theorem [[§CA.4 Contour Integration#^thm-ca-4-1|§CA.4.1]] The ML Inequality and the Basic Integral); $\int\frac{dx}{x^2 + a^2} = \pi/a$ and $\int\frac{e^{ikx}dx}{x^2 + a^2} = \frac\pi ae^{-a|k|}$ (Example [[§CA.4 Contour Integration#^ex-ca-4-1|§CA.4.1]] Two Lorentzian Integrals).

^nd-thm-ca-4-1

→ drilled as [[PHY 513 PS Drill#^ps4-1|PS4.1]] (parts (a)–(d) the basic integral; (e)–(i) the Lorentzian integral)

# T7. Lorentz group, algebra and representations

## Definitions and conventions T7

### Generators of the vector representation

The six $4\times4$ matrices $(\mathcal J^{\alpha\beta})^\mu{}_\nu = i(g^{\alpha\mu}\delta^\beta{}_\nu - g^{\beta\mu}\delta^\alpha{}_\nu) = iM^{\alpha\beta}$, antisymmetric in the label $\alpha\beta$, with $\Lambda = \exp(\frac12\omega_{\alpha\beta}M^{\alpha\beta}) = \exp(-\frac i2\omega_{\alpha\beta}\mathcal J^{\alpha\beta})$, see Definition [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-1|§C1a.6.1]] Generators of the Vector Representation. *Source: Lecture 7 (Sep 23), slide "Vector Representation" · Problem Set 4, Problem 5, eq. (14) · the user's notes Ch. 1 §1.6, Ch. 7 · PS eq. (3.18)*

^nd-def-c1a-6-1

- [ ] Q1 **[def]** Write the generators $(\mathcal J^{\alpha\beta})^\mu{}_\nu$ of the vector representation with the index positions the course uses, and say which pair of indices is the label and which the matrix entry.
- [ ] Q2 **[def]** Write the finite transformation $\Lambda(\omega)$ in both the real convention ($M$) and the Hermitian convention ($\mathcal J$); what is the relation between $M$ and $\mathcal J$?
- [ ] Q3 How many independent generators are there, and which labels are rotations and which boosts?
- [ ] Q4 **[conv]** Why is the both-lower form $(\mathcal J^{\alpha\beta})_{\mu\nu}$ of PS (3.18) not the matrix that acts on $v^\nu$, and what must be done to it first?
- [ ] Q5 **[why]** Why does the factor $\frac12$ appear in $\frac12\omega_{\alpha\beta}M^{\alpha\beta}$, and what happens to the angles if it is dropped?

> [!tip]- Hints: route in the notes
> - Technique: K2 (index calculus and dummy renaming)
> - The definition and both exponentials: Definition [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-1|§C1a.6.1]] Generators of the Vector Representation; the factor ½ and the antisymmetry of ω: [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^rem-c1a-6-1|§C1a.6, Remark: The factor ½ and why ω may be taken antisymmetric]].
> - Label versus matrix entry, and PS's both-lower form: [[§C3.1 Index Slots, Rotations and Spin in Field Theory#^cau-c3-1-1|§C3.1, Caution: Four spacetime indices in two roles]].

### Rotation and boost generators

$J_i = \frac12\varepsilon_{ijk}\mathcal J^{jk}$, $K_i = \mathcal J^{0i}$, so that $-\frac i2\omega_{\mu\nu}\mathcal J^{\mu\nu} = -i\boldsymbol\theta\cdot\mathbf J - i\boldsymbol\eta\cdot\mathbf K$ with $\theta_i = \frac12\varepsilon_{ijk}\omega_{jk}$, $\eta_i = \omega_{0i}$, see Definition [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-2|§C1a.6.2]] Rotation and Boost Generators. *Source: Lecture 7, slide "Lorentz Algebra: Defining Representation" · the user's notes Ch. 1 §1.6 · Problem Set 5, Problem 1 (statement, with the other sign of K)*

^nd-def-c1a-6-2

- [ ] Q1 **[def]** Define $\mathbf J$ and $\mathbf K$ from the six $\mathcal J^{\mu\nu}$, and the angles $\boldsymbol\theta$ and rapidities $\boldsymbol\eta$ from $\omega_{\mu\nu}$.
- [ ] Q2 Rewrite $-\frac i2\omega_{\mu\nu}\mathcal J^{\mu\nu}$ in terms of $\boldsymbol\theta\cdot\mathbf J$ and $\boldsymbol\eta\cdot\mathbf K$: which terms of the double sum combine, and where does the $\frac12$ go?
- [ ] Q3 **[conv]** Problem Set 5 defines $K_i$ with the other index order. Which one, what does it do to the sign of the boost parameter, and which of $\mathbf J_\pm$ does it exchange?
- [ ] Q4 **[conv]** The Noether boost charge of §C1b.8 is written $K^i \equiv J^{i0}$. How is it related to the generator $K_i$ here and to the Hilbert-space $\hat K^i$?
- [ ] Q5 **[why]** Why can the antisymmetric pair $jk$ be traded for one index in three dimensions, while the pair $0i$ of a boost has no such partner?

> [!tip]- Hints: route in the notes
> - Technique: K2 (index calculus)
> - Regrouping: Definition [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-2|§C1a.6.2]] Rotation and Boost Generators; one index for a pair: [[§C3.1 Index Slots, Rotations and Spin in Field Theory#^rem-c3-1-2|§C3.1, Remark: Why rotations felt simpler]].
> - Signs of K across sources: [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^cau-c3-2-2|§C3.2, Caution: Which one is (½, 0) depends on the sign of K]], [[Larsen PHY 513|register: Lorentz transformations]]; the Noether boost charge: Theorem [[§C3.5 Covariant Quantum Fields and the Free Scalar's Representation#^thm-c3-5-6|§C3.5.6]] The Noether Charges Are the Generators (last line).

### Which ω is a rotation by θ

The matrices $\Lambda = e^{-\frac i2\omega_{\mu\nu}\mathcal J^{\mu\nu}}$ are the same in PS, the lectures and Yu; actively $\omega_{12} = \theta$ rotates by $+\theta$ about $z$ and $\omega_{03} = \eta$ boosts to $+z$, while Yu reads $\Lambda$ passively, see [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^cau-c1a-6-1|§C1a.6, Caution: Which ω is a rotation by θ]]. *Source: Lecture 7, slides "Example: Rotation around z-axis", "Example: Boost Along x-axis" · the user's notes Ch. 7 (Caution "The index order in the boost example") · Yu §3.1*

^nd-cau-c1a-6-1

- [ ] Q1 **[def]** In the active reading, which parameter $\omega_{\mu\nu}$ gives a rotation by $+\theta$ about $z$, and which a boost to rapidity $+\eta$ along $+z$?
- [ ] Q2 **[conv]** The Lecture 7 boost example labels its parameter $\omega_{10} = -\omega_{01} = \eta$. Which parameter does the displayed matrix actually belong to, and what would the label as written give?
- [ ] Q3 **[conv]** How are Yu's angle and rapidity related to the course's $\omega_{12}$ and $\omega_{01}$?
- [ ] Q4 **[why]** Which formulas are identical in every source, and which flip sign between the active and passive readings?

> [!tip]- Hints: route in the notes
> - Technique: K2
> - All in [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^cau-c1a-6-1|§C1a.6, Caution: Which ω is a rotation by θ]]; active versus passive: [[§C1a.4 The Lorentz Group#^cau-c1a-4-1|§C1a.4, Caution: Active and passive readings]]; the sign in the exponent across sources: [[§C3.1 Index Slots, Rotations and Spin in Field Theory#^cau-c3-1-3|§C3.1, Caution: The sign in the exponent across sources]].

### Index slots

An index names a slot, a vector space on which a Lorentz transformation acts by its own rule: spacetime indices, generator labels (an antisymmetric pair) and matrix indices of a representation, see Definition [[§C3.1 Index Slots, Rotations and Spin in Field Theory#^def-c3-1-1|§C3.1.1]] Index Slots. *Source: the user's notes Ch. 7 §7.1 · Lecture 7, Parts A–B*

^nd-def-c3-1-1

- [ ] Q1 **[def]** Name the three kinds of index slot and the rule by which each transforms.
- [ ] Q2 In $(\mathcal J^{\mu\nu})^\alpha{}_\beta$, which indices are labels and which are matrix entries? In $(S^{\mu\nu})_{ab}$? In $(\gamma^\mu)_{ab}$?
- [ ] Q3 **[why]** Why do label and matrix indices look alike for the vector representation but not for the Dirac representation?
- [ ] Q4 **[why]** Why are spinor indices never raised or lowered with $g$?

> [!tip]- Hints: route in the notes
> - Technique: K2
> - Definition [[§C3.1 Index Slots, Rotations and Spin in Field Theory#^def-c3-1-1|§C3.1.1]] Index Slots; the table of symbols: [[§C3.1 Index Slots, Rotations and Spin in Field Theory#^rem-c3-1-1|§C3.1, Remark: One symbol for each realization of the generators]]; two roles of spacetime indices: [[§C3.1 Index Slots, Rotations and Spin in Field Theory#^cau-c3-1-1|§C3.1, Caution: Four spacetime indices in two roles]]; Dirac indices: [[§C5a.5 Chirality and Weyl Spinors#^rem-c5a-5-4|§C5a.5, Remark: What each Dirac index labels]].

### Generators of a representation

For a representation $D$ of $SO^+(1,3)$ on a finite-dimensional complex space, the six matrices $D(\mathcal J^{\mu\nu}) = -D(\mathcal J^{\nu\mu})$ defined by $D(e^{s\omega}) = \mathbb 1 - \frac{is}2\omega_{\mu\nu}D(\mathcal J^{\mu\nu}) + O(s^2)$, so that $D(e^\omega) = \exp(-\frac i2\omega_{\mu\nu}D(\mathcal J^{\mu\nu}))$, see Definition [[§CB.5 The Lorentz Algebra꞉ Generators and Commutation Relations#^def-cb-5-1|§CB.5.1]] Generators of a Representation. *Source: Lecture 7, slide "Transformation of General Fields" · the user's notes Ch. 7*

^nd-def-cb-5-1

- [ ] Q1 **[def]** Define the generators of a representation $D$ from the expansion of $D(e^{s\omega})$.
- [ ] Q2 Why does the exponential formula $D(e^\omega) = \exp(\dots)$ follow from the first-order definition (what property of $s \mapsto D(e^{s\omega})$ is used)?
- [ ] Q3 **[conv]** In this convention, are the generators of a rotation Hermitian or anti-Hermitian in the vector representation? Of a boost?
- [ ] Q4 **[why]** Why are the generators of every representation forced to obey the same commutation relations?

> [!tip]- Hints: route in the notes
> - Technique: K4 (exponentiating a generator)
> - Definition [[§CB.5 The Lorentz Algebra꞉ Generators and Commutation Relations#^def-cb-5-1|§CB.5.1]] Generators of a Representation; the common algebra: Theorem [[§CB.5 The Lorentz Algebra꞉ Generators and Commutation Relations#^thm-cb-5-6|§CB.5.6]] The Lorentz Algebra and its group-law derivation [[§CB.5 The Lorentz Algebra꞉ Generators and Commutation Relations#^der-cb-5-6|Derivation §CB.5.6, from the group law]]; the reason in general: Theorem [[§CB.3 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-3-8|§CB.3.8]] A Group Representation Gives an Algebra Representation.

### Representation of the Lorentz algebra

Six matrices $D(\mathcal J^{\mu\nu}) = -D(\mathcal J^{\nu\mu})$ on a complex space obeying the covariant Lorentz algebra form a representation of the Lorentz algebra, with $J_i = \frac12\varepsilon_{ijk}D(\mathcal J^{jk})$, $K_i = D(\mathcal J^{0i})$ and $\mathbf J_\pm = \frac12(\mathbf J \pm i\mathbf K)$, see Definition [[§CB.5 The Lorentz Algebra꞉ Generators and Commutation Relations#^def-cb-5-7|§CB.5.7]] Representation of the Lorentz Algebra. *Source: Lecture 7, slide "Representations of Angular Momentum" (the rotation analogue) and "Lorentz Algebra: Defining Representation" ("All representations realize the abstract algebra")*

^nd-def-cb-5-7

- [ ] Q1 **[def]** What does it mean for six matrices to "represent the Lorentz algebra"? Write the covariant relation they must satisfy.
- [ ] Q2 **[def]** For the rotation algebra, the lecture's "spin j" is a choice of what? How many matrices, of what size?
- [ ] Q3 **[why]** Lecture 7 says the rotation algebra has "one representation for each dimension". Which two qualifiers make this true, and what goes wrong without each?
- [ ] Q4 **[why]** Why is the same statement false for the Lorentz algebra already in dimension 4?

> [!tip]- Hints: route in the notes
> - Technique: K16 (identifying a representation)
> - Definition [[§CB.5 The Lorentz Algebra꞉ Generators and Commutation Relations#^def-cb-5-7|§CB.5.7]] Representation of the Lorentz Algebra; the two qualifiers: [[§C3.1 Index Slots, Rotations and Spin in Field Theory#^rem-c3-1-4|§C3.1, Remark: "One representation for each dimension" needs two qualifiers]]; two inequivalent four-dimensional representations: Theorem [[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-18-5|§CB.18.5]] The Dirac Representation Is Not the Vector Representation.

### Orbital generators

On functions of $x$ the six differential operators $L^{\mu\nu} = i(x^\mu\partial^\nu - x^\nu\partial^\mu)$ act on the argument of a field, not on its components, see Definition [[§C3.3 How Fields Transform under the Lorentz Group#^def-c3-3-1|§C3.3.1]] Orbital Generators. *Source: Lecture 7, slide "Lorentz Algebra: Defining Representation" ($J^{\mu\nu} = i(x^\mu\partial^\nu - x^\nu\partial^\mu)$) and slide "Quantum Angular Momentum" · PS eq. (3.16)*

^nd-def-c3-3-1

- [ ] Q1 **[def]** Write $L^{\mu\nu}$ with its index positions, and the three-dimensional orbital angular momentum it contains.
- [ ] Q2 **[conv]** The rotation slide writes $J^{ij} = -i(x^i\partial_j - x^j\partial_i)$ with lower derivatives; reconcile this sign with the $+i$ and upper derivatives of $L^{\mu\nu}$.
- [ ] Q3 **[why]** Why does the factor $i$ make the rotation generators Hermitian on functions?
- [ ] Q4 **[why]** On what space do the $L^{\mu\nu}$ act, and why is it infinite-dimensional?

> [!tip]- Hints: route in the notes
> - Technique: K2
> - Definition [[§C3.3 How Fields Transform under the Lorentz Group#^def-c3-3-1|§C3.3.1]] Orbital Generators; the sign: [[§C3.1 Index Slots, Rotations and Spin in Field Theory#^cau-c3-1-2|§C3.1, Caution: The sign of the orbital generator]]; three realizations of one algebra: [[§C3.3 How Fields Transform under the Lorentz Group#^rem-c3-3-1|§C3.3, Remark: Three realizations of one algebra]].

### Complexification, and where J± live

The complexification $\mathfrak g_{\mathbb C}$ of a real Lie algebra is the space of complex combinations with the bracket extended complex-bilinearly; the combinations $J_{\pm i} = \frac12(J_i \pm iK_i)$ lie in $\mathfrak{so}(1,3)_{\mathbb C}$, and no nonzero element of either copy lies in $\mathfrak{so}(1,3)$ itself, see Definition [[§CB.4 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-4-3|§CB.4.3]] Complexification and Theorem [[§CB.6 The Lorentz Algebra꞉ the Split J±, Real Forms and 𝔰𝔩(2,ℂ) as a Real Lie Algebra#^thm-cb-6-1|§CB.6.1]] The Split of the Complexified Lorentz Algebra. *Source: the user's request for definitions before the (j₊, j₋) identification (2026-10-13) · Lecture 7, slide "Transformation of General Fields" ("2 copies of the angular momentum algebra")*

^nd-def-cb-4-3

- [ ] Q1 **[def]** Define the complexification of a real Lie algebra. Give the rotation example: which element is in $\mathfrak{so}(3)_{\mathbb C}$ but not in the real span of $J^1, J^2, J^3$?
- [ ] Q2 **[def]** In which space do $J_i$, $K_i$ live (the real algebra, or $i$ times it), given that the real basis is $-iJ_i$, $-iK_i$?
- [ ] Q3 Where do $J_{\pm i}$ live, and why is $J_{\pm i}$ not an element of $\mathfrak{so}(1,3)$?
- [ ] Q4 How does a representation $D$ of the real algebra act on $J_\pm$ (which extension of $D$ is used)?
- [ ] Q5 **[why]** Why is "the Lorentz algebra is two copies of the angular momentum algebra" false for the real algebra, and what is the true statement?

> [!tip]- Hints: route in the notes
> - Technique: K16
> - Definition [[§CB.4 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-4-3|§CB.4.3]] Complexification; where $J_i$, $K_i$ live: Step 1 of [[§CB.6 The Lorentz Algebra꞉ the Split J±, Real Forms and 𝔰𝔩(2,ℂ) as a Real Lie Algebra#^pf-cb-6-1|proof of Theorem §CB.6.1]]; no nonzero element of a copy in the real algebra: Step 8 there.
> - The complex-linear extension: Theorem [[§CB.4 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-4-9|§CB.4.9]] Complex Representations of 𝔤 Are Complex-Linear Representations of Its Complexification; the slide's word "reducible": [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^cau-c3-2-1|§C3.2, Caution: The algebra decomposes; it is not "reducible"]]; the objects called J: [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^rem-cb-17-1|§CB.17, Remark: The objects called J, and what the labels refer to]].

### Intertwiner and equivalence

A linear map $S$ with $S\,D_1(x) = D_2(x)\,S$ for every element $x$ is an intertwiner; $D_1$ and $D_2$ are equivalent iff an invertible intertwiner exists, see Definition [[§CB.7 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^def-cb-7-2|§CB.7.2]] Intertwiner. *Source: written for the rigorous (j₊, j₋) identification (the user's request, 2026-10-13)*

^nd-def-cb-7-2

- [ ] Q1 **[def]** Define an intertwiner between two representations of a group (or of a Lie algebra), and equivalence.
- [ ] Q2 For a Lie algebra, why is it enough to check the intertwining relation on a basis (the six generators)?
- [ ] Q3 **[why]** Why is a group intertwiner also an algebra intertwiner, and when does the converse hold?
- [ ] Q4 **[why]** Why does an intertwiner carry the Casimir operators of one representation to those of the other?

> [!tip]- Hints: route in the notes
> - Technique: K16
> - Definition [[§CB.7 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^def-cb-7-2|§CB.7.2]] Intertwiner; group versus algebra: step 3 of [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^pf-cb-17-2|proof of Theorem §CB.17.2]]; Casimirs under intertwiners: step 7(ii) of [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^pf-cb-17-7|proof of Theorem §CB.17.7]].

### Casimir operator

An operator built polynomially from the generators that commutes with every generator; for the rotation algebra $\mathbf J^2$; on an irreducible representation every Casimir is a multiple of the identity, see Definition [[§CB.7 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^def-cb-7-12|§CB.7.12]] Casimir Operator and Theorem [[§CB.7 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-7-13|§CB.7.13]] Casimir Operators Are Constant on Irreducible Representations. *Source: the user's notes Ch. 7 §7.4.3*

^nd-def-cb-7-12

- [ ] Q1 **[def]** Define a Casimir operator of a representation.
- [ ] Q2 Why does $\mathbf J^2$ commute with each $J^i$? (Which commutators are used?)
- [ ] Q3 **[why]** Why is a Casimir a multiple of the identity on an irreducible representation (which lemma)?
- [ ] Q4 Name the two Casimirs used to label Lorentz representations, and the values they take on $(j_+, j_-)$.
- [ ] Q5 **[why]** Why do the Casimir values alone not prove that a representation is irreducible?

> [!tip]- Hints: route in the notes
> - Technique: K16
> - Definition [[§CB.7 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^def-cb-7-12|§CB.7.12]] Casimir Operator, Theorem [[§CB.7 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-7-13|§CB.7.13]] Casimir Operators Are Constant on Irreducible Representations (Schur: Theorem [[§CB.7 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-7-4|§CB.7.4]] Schur's Lemma); values on $(j_+, j_-)$: Theorem [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-17-5|§CB.17.5]] (j₊, j₋) Is Irreducible.
> - Why values are not enough by themselves: step 7 of [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^pf-cb-17-7|proof of Theorem §CB.17.7]] needs the classification Theorem [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-17-6|§CB.17.6]] Every Finite-Dimensional Representation Is a Sum of (j₊, j₋) and the dimension count.

### The representation (j₊, j₋)

$V = \mathbb C^{2j_++1}\otimes\mathbb C^{2j_-+1}$ with $\mathbf J_+ = \mathbf J^{(j_+)}\otimes\mathbb 1$, $\mathbf J_- = \mathbb 1\otimes\mathbf J^{(j_-)}$, hence $\mathbf J = \mathbf J_+ + \mathbf J_-$ and $\mathbf K = -i(\mathbf J_+ - \mathbf J_-)$, see Definition [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^def-cb-17-3|§CB.17.3]] The Representation (j₊, j₋). *Source: Lecture 7, slide "Transformation of General Fields" (HW5 clue) · Problem Set 5, Problem 1(b) (statement) · the user's notes Ch. 7 §7.4.3*

^nd-def-cb-17-3

- [ ] Q1 **[def]** Define the representation $(j_+, j_-)$: the space and the matrices $\mathbf J_\pm$.
- [ ] Q2 Express $\mathbf J$ and $\mathbf K$ through $\mathbf J_\pm$. Which combination is the physical rotation generator?
- [ ] Q3 What is the dimension of $(j_+, j_-)$? Give the dimensions of $(\frac12, 0)$, $(\frac12, \frac12)$, $(1, 0)$, $(1, 1)$.
- [ ] Q4 **[why]** Why is neither label the spin of the field? What does a rotation see on $(j_+, j_-)$?
- [ ] Q5 **[conv]** Which other names do the pre-course notes and Weinberg use for the labels?

> [!tip]- Hints: route in the notes
> - Technique: K16
> - Definition [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^def-cb-17-3|§CB.17.3]] The Representation (j₊, j₋); neither label is the spin: [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^rem-c3-2-2|§C3.2, Remark: Neither label is the spin]]; rotation content: Theorem [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-17-9|§CB.17.9]] Rotation Content and the Sign of a 2π Rotation; the catalogue of the course's fields: [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^rem-c3-2-3|§C3.2, Remark: The representations met in the course]].

### Acting as spin j

A subspace invariant under the $+$ copy is one on which "the $+$ copy acts as spin $j$" if, as a representation of $\mathfrak a_+ \cong \mathfrak{sl}(2, \mathbb C)$, it is a direct sum of copies of $V_j$ (isotypic); that $V$ "is" $(j_+, j_-)$ is the stronger statement of an invertible intertwiner to the model, see Definition [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^def-cb-17-1|§CB.17.1]] Acting as Spin j. *Source: the user's notes Ch. 7 §7.4.3 (the informal "acts as spin j") · written for the rigor fix of 2026-10-13*

^nd-def-cb-17-1

- [ ] Q1 **[def]** State precisely what "the $+$ copy acts as spin $j$ on $W$" means.
- [ ] Q2 **[def]** What stronger statement is meant by "$V$ is $(j_+, j_-)$"?
- [ ] Q3 **[why]** Give the reason a space on which $\mathbf J_+^2 = j_+(j_+ + 1)$ and $\mathbf J_-^2 = j_-(j_- + 1)$ need not yet be called $(j_+, j_-)$: what further input closes the gap?
- [ ] Q4 **[why]** Through which map do $\mathbf J_\pm$ act on a representation space of the real algebra?

> [!tip]- Hints: route in the notes
> - Technique: K16
> - Definition [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^def-cb-17-1|§CB.17.1]] Acting as Spin j; the gap closed by the classification and dimensions: step 7 of [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^pf-cb-17-7|proof of Theorem §CB.17.7]]; the extension $D_{\mathbb C}$: Theorem [[§CB.4 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-4-9|§CB.4.9]] Complex Representations of 𝔤 Are Complex-Linear Representations of Its Complexification, [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^rem-cb-17-1|§CB.17, Remark: The objects called J, and what the labels refer to]] (item 3).

### Components, not states: D(Λ) versus U(Λ)

The labels $(j_+, j_-)$, the Casimirs $\mathbf J_\pm^2$ and the eigenvalues $m_\pm$ refer to the finite-dimensional space $V$ of a field's components, on which $D(\Lambda)$ acts; the unitary $U(\Lambda)$ acts on the Hilbert space of states, and the two meet only in $U(\Lambda)^{-1}\hat\Phi_a(x)U(\Lambda) = D(\Lambda)_a{}^b\hat\Phi_b(\Lambda^{-1}x)$, see [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^cau-c3-2-3|§C3.2, Caution: Components, not states]]. *Source: the user's critique while working on Problem Set 7 (2026-10-13) · the user's pre-course notes §5.2*

^nd-cau-c3-2-3

- [ ] Q1 **[def]** On which space does $D(\Lambda)$ act and on which $U(\Lambda)$? Give the dimension of each for a vector field.
- [ ] Q2 **[def]** Write the one formula in which $D(\Lambda)$ and $U(\Lambda)$ meet.
- [ ] Q3 For the four-vector, what are the joint eigenvectors of $J_{+3}$, $J_{-3}$ in $V$, with their labels $(m_+, m_-)$? Which component combinations of a field $V^\mu$ are their coefficients?
- [ ] Q4 **[why]** Why is "$\lvert m_+, m_-\rangle$" in the course's language not a state of the Hilbert space?
- [ ] Q5 **[why]** What labels the one-particle states instead, and why is $D$ allowed to be non-unitary while $U$ must be unitary?

> [!tip]- Hints: route in the notes
> - Technique: K16
> - [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^cau-c3-2-3|§C3.2, Caution: Components, not states]]; the eigenvectors $e_1 \pm ie_2$, $e_0 \pm e_3$: last bullet of [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^pf-cb-17-7b|proof of Theorem §CB.17.7, second route]].
> - Two kinds of representation side by side: [[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra#^rem-c3-4-2|§C3.4, Remark: Two kinds of representation]]; three different transformations: [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^cau-c5a-4-1|§C5a.4, Caution: Three different transformations]]; unitarity on states: Principle [[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra#^pr-c3-4-1|§C3.4.1]] Poincaré Invariance on the Hilbert Space, [[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra#^rem-c3-4-1|§C3.4, Remark: Why unitary, and why the covering group]].

### Spinor and tensor representations

A finite-dimensional representation is a tensor representation if the $2\pi$ rotation $e^{-2\pi iJ_3}$ acts as $+\mathbb 1$ and a spinor representation if it acts as $-\mathbb 1$; $(j_+, j_-)$ is tensorial for integer $j_+ + j_-$ and spinorial for half-odd $j_+ + j_-$, see Definition [[§CB.14 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-14-26|§CB.14.26]] Spinor and Tensor Representations and Theorem [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-17-11|§CB.17.11]] Every Finite-Dimensional Representation Splits into a Tensor and a Spinor Part. *Source: Problem Set 6, Problem 4(d) (vectors and spinors under 2π) · the user's notes Ch. 7*

^nd-def-cb-14-26

- [ ] Q1 **[def]** Define tensor and spinor representations by the $2\pi$ rotation.
- [ ] Q2 Which of $(0,0)$, $(\frac12, 0)$, $(\frac12, \frac12)$, $(1, 0)\oplus(0, 1)$, $(\frac12, 0)\oplus(0, \frac12)$ are spinorial?
- [ ] Q3 **[why]** Why can a single irreducible $(j_+, j_-)$ not mix the two signs?
- [ ] Q4 **[why]** Why is a spinor's $D(\Lambda)$ defined only up to sign on $SO^+(1,3)$, and on which group is it single-valued?

> [!tip]- Hints: route in the notes
> - Technique: K4 (exponentiating a generator)
> - Definition [[§CB.14 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-14-26|§CB.14.26]] Spinor and Tensor Representations, Theorem [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-17-11|§CB.17.11]] Every Finite-Dimensional Representation Splits into a Tensor and a Spinor Part; the sign: step 4 of [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^der-cb-17-9|Derivation §CB.17.9]]; up to sign: [[§C3.3 How Fields Transform under the Lorentz Group#^rem-c3-3-4|§C3.3, Remark: Why a spinor's matrix is fixed only up to sign]].

### Spinor fields

A left-handed Weyl field is a two-component field in $(\frac12, 0)$, a right-handed one in $(0, \frac12)$, a Dirac field a four-component field in $(\frac12, 0)\oplus(0, \frac12)$, each with $\psi'(x) = D(\Lambda)\psi(\Lambda^{-1}x)$, see Definition [[§C3.3 How Fields Transform under the Lorentz Group#^def-c3-3-2|§C3.3.2]] Spinor Fields. *Source: Lecture 7, slide "Transformation of Vector and Spinor Fields" · Lecture 8, "Cheat Sheet II"*

^nd-def-c3-3-2

- [ ] Q1 **[def]** Define Weyl and Dirac fields by their representations and write the field law.
- [ ] Q2 In the law $\psi \to \Lambda_{1/2}\psi(\Lambda^{-1}x)$, which matrix acts on the components and which on the argument?
- [ ] Q3 **[why]** Why is the argument $\Lambda^{-1}x$ and not $\Lambda x$ (the "bump" picture of the scalar slide)?
- [ ] Q4 **[why]** Why is $D(\Lambda)$ for these fields fixed by $\Lambda$ only up to sign?

> [!tip]- Hints: route in the notes
> - Technique: K14 (Lorentz-invariance arguments)
> - Definition [[§C3.3 How Fields Transform under the Lorentz Group#^def-c3-3-2|§C3.3.2]] Spinor Fields; the argument: Theorem [[§C3.3 How Fields Transform under the Lorentz Group#^thm-c3-3-1|§C3.3.1]] The Orbital Generators Move the Argument; the sign: [[§C3.3 How Fields Transform under the Lorentz Group#^rem-c3-3-4|§C3.3, Remark: Why a spinor's matrix is fixed only up to sign]].

### Poincaré invariance on the Hilbert space

A relativistic quantum theory has unitary $U(\Lambda, a)$ with $U(\mathbb 1, 0) = \mathbb 1$, $U(\Lambda_2, a_2)U(\Lambda_1, a_1) = U(\Lambda_2\Lambda_1, \Lambda_2a_1 + a_2)$ and an invariant vacuum (for half-integer spin, on the covering group), see Principle [[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra#^pr-c3-4-1|§C3.4.1]] Poincaré Invariance on the Hilbert Space. *Source: the user's notes Ch. 7 §7.6 · Yu §3.1–3.3*

^nd-pr-c3-4-1

- [ ] Q1 **[state]** State the three requirements on $U(\Lambda, a)$, with the composition law written out.
- [ ] Q2 **[why]** Why unitary and not antiunitary for the proper orthochronous group?
- [ ] Q3 **[why]** Why does the composition law hold only up to a sign on $SO^+(1,3)$ for half-integer spin, and how is that repaired?
- [ ] Q4 **[conv]** In the composition law, which translation comes out: $\Lambda_2a_1 + a_2$ or $\Lambda_1a_2 + a_1$? Check it by acting on a point.

> [!tip]- Hints: route in the notes
> - Technique: K14
> - Principle [[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra#^pr-c3-4-1|§C3.4.1]] Poincaré Invariance on the Hilbert Space; unitary and the covering group: [[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra#^rem-c3-4-1|§C3.4, Remark: Why unitary, and why the covering group]]; Wigner: Theorem [[§CB.19 Projective Representations, Wigner's Theorem and Antiunitary Symmetries#^thm-cb-19-7|§CB.19.7]] Wigner's Theorem.

### Generators of quantum Poincaré transformations

$U(\mathbb 1 + \omega, \varepsilon) = \mathbb 1 - \frac i2\omega_{\mu\nu}\hat J^{\mu\nu} + i\varepsilon_\mu\hat P^\mu + \dots$, with $\hat H = \hat P^0$, $\hat J^i = \frac12\varepsilon_{ijk}\hat J^{jk}$, $\hat K^i = \hat J^{0i}$, see Definition [[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra#^def-c3-4-1|§C3.4.1]] Generators of Quantum Poincaré Transformations. *Source: the user's notes Ch. 7 §7.6 · Yu §3.1*

^nd-def-c3-4-1

- [ ] Q1 **[def]** Write the expansion of $U$ near the identity that defines $\hat J^{\mu\nu}$ and $\hat P^\mu$, with both signs.
- [ ] Q2 **[conv]** With this sign of $\hat P$, what is $U(\mathbb 1, a)$ for a finite translation, and what is $U(\mathbb 1, a)$ on a one-particle momentum eigenstate?
- [ ] Q3 **[conv]** Compare the signs with Peskin–Schroeder and with Yu (which sources flip the sign of $\hat P$ or of the angle?).
- [ ] Q4 **[why]** Why is $\hat K^i$ Hermitian here while the boost generators $K_i$ of a finite-dimensional field representation are not?

> [!tip]- Hints: route in the notes
> - Technique: K14
> - Definition [[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra#^def-c3-4-1|§C3.4.1]] Generators of Quantum Poincaré Transformations; signs across sources: [[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra#^cau-c3-4-1|§C3.4, Caution: Signs and names across the sources]]; finite forms: Theorem [[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra#^thm-c3-4-3|§C3.4.3]] Finite Transformations as Exponentials; Hermiticity: Theorem [[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra#^thm-c3-4-2|§C3.4.2]] The Generators Are Hermitian versus Theorem [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-17-15|§CB.17.15]] No Finite-Dimensional Representation Is Unitary.

### Covariance of quantum fields

$U^{-1}(\Lambda, a)\,\hat\Phi_a(x)\,U(\Lambda, a) = D(\Lambda)_a{}^b\,\hat\Phi_b(\Lambda^{-1}(x - a))$, as operator-valued distributions, see Principle [[§C3.5 Covariant Quantum Fields and the Free Scalar's Representation#^pr-c3-5-1|§C3.5.1]] Covariance of Quantum Fields. *Source: the user's notes Ch. 7 §7.6 · [[Larsen PHY 513|register: Quantum Poincaré transformations]]*

^nd-pr-c3-5-1

- [ ] Q1 **[state]** Write the covariance law of a quantum field with the inverse on the correct side.
- [ ] Q2 **[conv]** Rewrite it with $U\hat\Phi U^{-1}$ on the left: what replaces $D(\Lambda)$ and the argument $\Lambda^{-1}(x - a)$?
- [ ] Q3 **[conv]** Lectures 11–12 and Problem Set 6 write the discrete transformations as $U\hat\psi U^{-1}$. Why does the side of the inverse matter for parity and charge conjugation less than for Lorentz transformations?
- [ ] Q4 **[why]** In what sense is this a principle (an axiom) and in what sense a theorem for the free scalar field?

> [!tip]- Hints: route in the notes
> - Technique: K14
> - Principle [[§C3.5 Covariant Quantum Fields and the Free Scalar's Representation#^pr-c3-5-1|§C3.5.1]] Covariance of Quantum Fields; both forms for the scalar: Theorem [[§C3.5 Covariant Quantum Fields and the Free Scalar's Representation#^thm-c3-5-5|§C3.5.5]] The Free Scalar Field Transforms as a Scalar; principle or theorem: [[§C3.5 Covariant Quantum Fields and the Free Scalar's Representation#^rem-c3-5-1|§C3.5, Remark: Principle or theorem]]; the side of the inverse for P, C, T: [[§C9.3 Parity on States, Spinors and the Dirac Field#^cau-c9-3-1|§C9.3, Caution: Which side the inverse is on, and the names of the phases]].

### The algebra decomposes; it is not "reducible"

Reducibility is a property of a representation; the true statement is that the complexified Lorentz algebra is a direct sum of two commuting copies of $\mathfrak{sl}(2, \mathbb C)$, while the real $\mathfrak{so}(1,3)$ does not split into two real rotation algebras, see [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^cau-c3-2-1|§C3.2, Caution: The algebra decomposes; it is not "reducible"]]. *Source: Lecture 7, slide "Transformation of General Fields" ("Lorentz algebra is reducible = 2 copies of the angular momentum algebra")*

^nd-cau-c3-2-1

- [ ] Q1 **[def]** Define a reducible representation. Why does the word not apply to an algebra?
- [ ] Q2 **[conv]** Restate the slide's clue correctly, naming the space in which the split happens.
- [ ] Q3 **[why]** The Euclidean $\mathfrak{so}(4)$ does split over the reals. Which sign in the boost–boost commutator makes the difference?
- [ ] Q4 **[why]** In what sense are $\mathfrak{so}(1,3)$ and $\mathfrak{so}(4)$ "the same" complex algebra?

> [!tip]- Hints: route in the notes
> - Technique: K3 (Lorentz commutators by index contraction)
> - [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^cau-c3-2-1|§C3.2, Caution: The algebra decomposes; it is not "reducible"]]; Theorem [[§CB.6 The Lorentz Algebra꞉ the Split J±, Real Forms and 𝔰𝔩(2,ℂ) as a Real Lie Algebra#^thm-cb-6-1|§CB.6.1]] The Split of the Complexified Lorentz Algebra; $\mathfrak{so}(4)$: Theorem [[§CB.6 The Lorentz Algebra꞉ the Split J±, Real Forms and 𝔰𝔩(2,ℂ) as a Real Lie Algebra#^thm-cb-6-4|§CB.6.4]] The Euclidean 𝔰𝔬(4) Splits Already over ℝ; two real forms: Theorem [[§CB.6 The Lorentz Algebra꞉ the Split J±, Real Forms and 𝔰𝔩(2,ℂ) as a Real Lie Algebra#^thm-cb-6-5|§CB.6.5]] 𝔰𝔬(1,3) and 𝔰𝔬(4) Are Two Real Forms of One Complex Algebra; the minus sign: [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^rem-c3-2-1|§C3.2, Remark: Two boosts make a rotation]].

### Which one is (½, 0) depends on the sign of K

With $K_i = \mathcal J^{0i}$ (these notes, PS) $(\frac12, 0)$ is PS's $\psi_L$; Problem Set 5 takes $K_i = \mathcal J^{i0}$, which exchanges $\mathbf J_\pm$ and makes its $\boldsymbol\beta = -\boldsymbol\eta$, see [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^cau-c3-2-2|§C3.2, Caution: Which one is (½, 0) depends on the sign of K]]. *Source: Problem Set 5, Problem 1 (statement and the user's solution) · the user's notes Ch. 7 §7.4.6*

^nd-cau-c3-2-2

- [ ] Q1 **[def]** Which sign of $\mathbf K$ do the course notes, PS and Problem Set 5 use?
- [ ] Q2 **[conv]** What does reversing $\mathbf K$ do to $\mathbf J_+$ and $\mathbf J_-$, and to the boost parameter?
- [ ] Q3 **[conv]** Under Problem Set 5's convention, which law does its $(\frac12, 0)$ obey, and which PS spinor is that when read with PS's $\boldsymbol\beta = \boldsymbol\eta$?
- [ ] Q4 **[why]** Why does the answer "a left-handed Weyl spinor is $(\frac12, 0)$" survive in both conventions?

> [!tip]- Hints: route in the notes
> - Technique: K16
> - [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^cau-c3-2-2|§C3.2, Caution: Which one is (½, 0) depends on the sign of K]]; the second route of the label question: [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^der-c3-2-2b|Derivation §C3.2.2, second route]] (convention bullet); the same swap for $\mathbf E \mp i\mathbf B$: [[§C3.3 How Fields Transform under the Lorentz Group#^cau-c3-3-1|§C3.3, Caution: Which half of F is called (1, 0)]].

## Derivations T7

### Infinitesimal Lorentz transformations are antisymmetric ★

For a path $\Lambda(s) = \mathbb 1 + s\omega + O(s^2)$ in $O(1,3)$, $\omega_{\mu\nu} = g_{\mu\rho}\omega^\rho{}_\nu = -\omega_{\nu\mu}$: six parameters, three rotations and three boosts; the mixed $\omega^\mu{}_\nu$ is not antisymmetric, see Theorem [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-1|§C1a.6.1]] Infinitesimal Lorentz Transformations Are Antisymmetric. *Source: Lecture 7, slide "Vector Representation" ("ω_μν are 6 'angles'") · the user's notes Ch. 1 §1.6*

^nd-thm-c1a-6-1

- [ ] Q1 **[state]** State the condition on $\omega$ and say for which index positions it holds.
- [ ] Q2 Insert $\Lambda(s)$ into the defining condition of the Lorentz group. Which form of that condition do you use?
- [ ] Q3 Lower the index of $\omega$ in both terms of the first-order coefficient. What must vanish?
- [ ] Q4 Count the independent parameters. Which are rotation angles and which rapidities?
- [ ] Q5 **[why]** Write $\omega^0{}_i$ and $\omega^i{}_0$ in terms of $\omega_{0i}$: why is the mixed matrix of a boost symmetric rather than antisymmetric?

> [!tip]- Hints: route in the notes
> - Technique: K2 (index calculus)
> - Steps 1–3 of [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^der-c1a-6-1|Derivation §C1a.6.1]]: first order of $g_{\rho\sigma}\Lambda^\rho{}_\mu\Lambda^\sigma{}_\nu = g_{\mu\nu}$.
> - Step 4 counts, step 5 raises one index with $g$.

### The generators reproduce ω ★★

As matrices on $v^\nu$, $-\frac i2\omega_{\alpha\beta}(\mathcal J^{\alpha\beta})^\mu{}_\nu = \omega^\mu{}_\nu$, so $\Lambda = e^\omega$ and $\delta v^\mu = \omega^\mu{}_\nu v^\nu$, see Theorem [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-2|§C1a.6.2]] The Generators Reproduce ω. *Source: Lecture 7, slide "Vector Representation" ($\delta v^\alpha = -\frac i2\omega_{\mu\nu}(\mathcal J^{\mu\nu})^\alpha{}_\beta v^\beta$) · the user's notes Ch. 7 (Derivation "What the vector generators do")*

^nd-thm-c1a-6-2

- [ ] Q1 **[state]** What does $-\frac i2\omega_{\alpha\beta}\mathcal J^{\alpha\beta}$ equal as a matrix acting on $v^\nu$?
- [ ] Q2 Contract $\omega_{\alpha\beta}$ with the first term $g^{\alpha\mu}\delta^\beta{}_\nu$ of $M^{\alpha\beta}$. What do you get?
- [ ] Q3 Contract with the second term. Which index has to be moved, and with which sign?
- [ ] Q4 Combine the two halves using the antisymmetry of $\omega$. Where does the factor $\frac12$ go?
- [ ] Q5 **[why]** Why does this make $\Lambda = e^\omega$ a matrix exponential of the mixed-index $\omega$, and what is $\delta v$ to first order?

> [!tip]- Hints: route in the notes
> - Technique: K2
> - Steps 1–3 of [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^der-c1a-6-2|Derivation §C1a.6.2]]; step 4 converts the Hermitian form; step 5 exponentiates.

### Rotations and boosts as exponentials ★★

$e^{\theta M^{12}}$ is the rotation by $\theta$ about $z$ ($\cos$, $\sin$ in the $(1,2)$ block, $(M^{12})^2 = -\mathbb 1$ there) and $e^{\eta M^{03}}$ the boost to rapidity $\eta$ along $z$ ($\cosh$, $\sinh$ in the $(0,3)$ block, $(M^{03})^2 = +\mathbb 1$ there), see Theorem [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-3|§C1a.6.3]] Rotations and Boosts as Exponentials. The finite $4\times4$ matrices along the axes are also Problem Set 6, Problem 4(a), (c). *Source: Lecture 7, slides "Example: Rotation around z-axis", "Example: Boost Along x-axis" · the user's notes Ch. 1 §1.6, Ch. 7*

^nd-thm-c1a-6-3

- [ ] Q1 **[state]** Which parameters $\omega_{\mu\nu}$ give the rotation about $z$ and the boost along $z$, and which $2\times2$ blocks of $\Lambda$ do they fill?
- [ ] Q2 Write the nonzero entries of $M^{12}$ and of $M^{03}$ (mixed indices). Why is one block antisymmetric and the other symmetric?
- [ ] Q3 Compute the square of each $2\times2$ block. How does the sign of the square decide between trigonometric and hyperbolic functions?
- [ ] Q4 Sum the exponential series, splitting even and odd powers.
- [ ] Q5 **[conv]** The slide's boost example writes $\omega_{10} = \eta$. Which label belongs to the displayed matrix?
- [ ] Q6 **[why]** Why does a boost have a rapidity and not an angle (what is the relation to $\gamma$ and $\gamma v$)?

> [!tip]- Hints: route in the notes
> - Technique: K4 (exponentiating a generator)
> - Steps 1–3 (rotation) and 4–5 (boost) of [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^der-c1a-6-3|Derivation §C1a.6.3]]; step 6 for the other axes.
> - The slide's label: [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^cau-c1a-6-1|§C1a.6, Caution: Which ω is a rotation by θ]].

### Every exponential is proper orthochronous ★

For every real antisymmetric $\omega_{\mu\nu}$, $\Lambda = e^\omega$ lies in $SO^+(1,3)$, see Theorem [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-4|§C1a.6.4]] Every Exponential Is Proper Orthochronous. *Source: the user's notes Ch. 7 · Yu §4.1, eqs. (4.9)–(4.12)*

^nd-thm-c1a-6-4

- [ ] Q1 **[state]** State the theorem: which three properties of $e^\omega$ are claimed?
- [ ] Q2 Write the antisymmetry of $\omega_{\mu\nu}$ as a matrix identity for the mixed $\omega$, and push it through the exponential series.
- [ ] Q3 Why is $\det e^\omega = 1$? (Which formula, and what is $\operatorname{tr}\omega$?)
- [ ] Q4 **[why]** Why is $e^\omega$ orthochronous (which continuity argument)?

> [!tip]- Hints: route in the notes
> - Technique: K4
> - Steps 1–3 of [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^der-c1a-6-4|Derivation §C1a.6.4]] (Lorentz), step 4 (Jacobi's formula), step 5 (a path from the identity).

### The generators as 4×4 matrices; rotations Hermitian, boosts not ★

$(J_k)^l{}_m = -i\varepsilon_{klm}$ with zero time row and column; $K_k = i(E_{0k} + E_{k0})$: each $J_k$ is $i$ times a real antisymmetric matrix (Hermitian), each $K_k$ is $i$ times a real symmetric matrix (anti-Hermitian), see Theorem [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-5|§C1a.6.5]] The Rotation and Boost Generators as 4×4 Matrices. **[class exercise, Lecture 7]** ("this one here … becomes symmetric. Thing to check it out"). *Source: Lecture 7 transcript (Sep 23), the boost example · PS eqs. (3.20)–(3.21) · Problem Set 6, Problem 4*

^nd-thm-c1a-6-5

- [ ] Q1 **[state]** Give the nonzero entries of $J_3$ and $K_3$ as $4\times4$ matrices with mixed indices.
- [ ] Q2 From $(\mathcal J^{0k})^\mu{}_\nu = i(g^{0\mu}\delta^k{}_\nu - g^{k\mu}\delta^0{}_\nu)$, find the two nonzero entries. Why do they come out with the same sign although $\mathcal J^{0k}$ is antisymmetric in its label?
- [ ] Q3 Use $(iA)^\dagger = -iA^{\mathsf T}$ for real $A$ to decide the Hermiticity of $J_k$ and of $K_k$.
- [ ] Q4 Find the eigenvalues of $J_3$ and of $K_3$ and their eigenvectors.
- [ ] Q5 **[why]** Why does the anti-Hermiticity of $K_k$ not signal a mistake? Which property replaces unitarity for $\Lambda$?

> [!tip]- Hints: route in the notes
> - Technique: K2
> - Steps 2–3 of [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^der-c1a-6-5|Derivation §C1a.6.5]] (entries), step 4 (Hermiticity), step 5 (eigenvectors).
> - Not unitary: [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^rem-c1a-6-2|§C1a.6, Remark: Hermitian generators do not make boosts unitary]], Theorem [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-17-15|§CB.17.15]] No Finite-Dimensional Representation Is Unitary.

### The rotation matrices in the vector representation

$R_z(\theta)$ and Rodrigues' formula for $R_{\hat{\mathbf n}}(\theta)$, see Theorem [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-6|§C1a.6.6]] The Rotation Matrices in the Vector Representation. → drilled as [[PHY 513 PS Drill#^ps6-4-c|PS6.4(c)]] (and the 2π rotation as [[PHY 513 PS Drill#^ps6-4-d|PS6.4(d)]]).

^nd-thm-c1a-6-6

### The boost matrices in the vector representation

$\Lambda_z(\eta)$ and the boost along $\hat{\mathbf n}$, see Theorem [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-7|§C1a.6.7]] The Boost Matrices in the Vector Representation. → drilled as [[PHY 513 PS Drill#^ps6-4-a|PS6.4(a)]].

^nd-thm-c1a-6-7

### The four-vector under rotations is 0 ⊕ 1 ★★

Restricted to rotations, the vector representation leaves $e_0$ invariant ($J_k = 0$ on it, spin 0) and acts on the spatial components by the spin-1 matrices $(J_k)^l{}_m = -i\varepsilon_{klm}$, see Example [[§C3.1 Index Slots, Rotations and Spin in Field Theory#^ex-c3-1-1|§C3.1.1]] The Four-Vector under Rotations Is 0 ⊕ 1. *Source: Lecture 7, slide "Spinors and Rotation" ("Unlike a 4-vector under rotation: spin-0 (time) and spin-1 (space)") · the user's notes Ch. 7 §7.3*

^nd-ex-c3-1-1

- [ ] Q1 **[state]** Into which spins does a four-vector decompose under rotations?
- [ ] Q2 Compute $(\mathcal J^{ij})^0{}_\nu$ and $(\mathcal J^{ij})^\mu{}_0$. What does this say about the time component?
- [ ] Q3 Compute $(J_k)^l{}_m$ on the spatial components, contracting with $\frac12\varepsilon_{kij}$.
- [ ] Q4 Evaluate $\mathbf J^2$ on the spatial block. Which spin does the value identify?
- [ ] Q5 **[why]** Why is the four-vector reducible under rotations but irreducible under the Lorentz group?

> [!tip]- Hints: route in the notes
> - Technique: K16 (identifying a representation)
> - The computation is in the box Example [[§C3.1 Index Slots, Rotations and Spin in Field Theory#^ex-c3-1-1|§C3.1.1]] The Four-Vector under Rotations Is 0 ⊕ 1; $\mathbf J^2 = \operatorname{diag}(0, 2, 2, 2)$ is step 3 of [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^pf-cb-17-7|proof of Theorem §CB.17.7]]; irreducible under boosts: first bullet of "What the proof shows" there.

### The Lorentz algebra from the group law ★

The generators of every representation obey $[\mathcal J^{\mu\nu}, \mathcal J^{\rho\sigma}] = i(g^{\nu\rho}\mathcal J^{\mu\sigma} - g^{\mu\rho}\mathcal J^{\nu\sigma} - g^{\nu\sigma}\mathcal J^{\mu\rho} + g^{\mu\sigma}\mathcal J^{\nu\rho})$, derived from the group law (conjugating a one-parameter subgroup), see Theorem [[§CB.5 The Lorentz Algebra꞉ Generators and Commutation Relations#^thm-cb-5-6|§CB.5.6]] The Lorentz Algebra. *Source: Lecture 7, slide "Lorentz Algebra: Defining Representation" (stated) · the user's notes Ch. 7 §7.3 ("automatically, by the group-law derivation")*

^nd-der-cb-5-6

- [ ] Q1 **[state]** Write the Lorentz algebra in covariant form, with all four terms and their signs.
- [ ] Q2 Conjugate the one-parameter subgroup $e^{s\omega'}$ by $\Lambda$. What is the parameter of the conjugated subgroup, and why is it again antisymmetric?
- [ ] Q3 Use the representation property to get the tensor law $D(\Lambda)^{-1}D(\mathcal J^{\rho\sigma})D(\Lambda) = \Lambda^\rho{}_\mu\Lambda^\sigma{}_\nu D(\mathcal J^{\mu\nu})$ (compare coefficients of $\omega'$).
- [ ] Q4 Make $\Lambda$ infinitesimal. Which commutator appears on the left, and which four terms on the right?
- [ ] Q5 Antisymmetrize, compare coefficients of $\omega_{\alpha\beta}$, and rename indices to reach the standard form.
- [ ] Q6 **[why]** Why does this route prove the algebra for every representation at once, while the vector-representation computation proves it for one?

> [!tip]- Hints: route in the notes
> - Technique: K3 (Lorentz commutators by index contraction)
> - Steps 1–4 of [[§CB.5 The Lorentz Algebra꞉ Generators and Commutation Relations#^der-cb-5-6|Derivation §CB.5.6, from the group law]] (tensor law; also Theorem [[§CB.5 The Lorentz Algebra꞉ Generators and Commutation Relations#^thm-cb-5-8|§CB.5.8]] The Generators Transform as a Tensor), steps 5–9 (infinitesimal $\Lambda$).
> - The general reason: Theorem [[§CB.3 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-3-8|§CB.3.8]] A Group Representation Gives an Algebra Representation.

### The Lorentz algebra in the vector representation

Direct $4\times4$ computation of $[\mathcal J^{\mu\nu}, \mathcal J^{\rho\sigma}]$, see [[§CB.5 The Lorentz Algebra꞉ Generators and Commutation Relations#^der-cb-5-6b|Derivation §CB.5.6, second route]]. → drilled as [[PHY 513 PS Drill#^ps4-5-a|PS4.5(a)]] (Lecture 7: "HW problem: $J^{\mu\nu}$ matrices satisfy Lorentz algebra").

^nd-der-cb-5-6b

### The J, K form and the J± split

$[J_i, J_j] = i\varepsilon_{ijk}J_k$, $[J_i, K_j] = i\varepsilon_{ijk}K_k$, $[K_i, K_j] = -i\varepsilon_{ijk}J_k$ and the two commuting copies $\mathbf J_\pm$, see [[§CB.5 The Lorentz Algebra꞉ Generators and Commutation Relations#^der-cb-5-6c|Derivation §CB.5.6, the J, K form and the J± split]]. → drilled as [[PHY 513 PS Drill#^ps5-1-a|PS5.1(a)]]. Includes the **[class exercise, Lecture 7]** "you can check … if … this is rotation in a plane and this is rotation in another plane … this thing collapses to the algebra" (step 2 of [[§CB.5 The Lorentz Algebra꞉ Generators and Commutation Relations#^der-cb-5-6c|Derivation §CB.5.6, the J, K form and the J± split]]).

^nd-der-cb-5-6c

### The orbital generators move the argument ★★

For $\Lambda = e^\omega$, $\phi(\Lambda^{-1}x) = (1 - \frac i2\omega_{\mu\nu}L^{\mu\nu})\phi(x) + O(\omega^2)$, with the same parameters and sign as $v \mapsto \Lambda v$; $L_i = -i(\mathbf x\times\nabla)_i$, $L^{0i} = -i(t\,\partial_i + x^i\partial_t)$, see Theorem [[§C3.3 How Fields Transform under the Lorentz Group#^thm-c3-3-1|§C3.3.1]] The Orbital Generators Move the Argument. *Source: Lecture 7, slide "Transformation of Scalar Fields" ($\phi(x) \to \phi(\Lambda^{-1}x)$) · the user's notes Ch. 7 §7.5*

^nd-thm-c3-3-1

- [ ] Q1 **[state]** State the first-order form of the scalar law $\phi'(x) = \phi(\Lambda^{-1}x)$ in terms of $L^{\mu\nu}$.
- [ ] Q2 **[why]** Why is the argument $\Lambda^{-1}x$ (the "bump" picture)?
- [ ] Q3 Expand $\phi(\Lambda^{-1}x)$ to first order with $(\Lambda^{-1})^\mu{}_\nu = \delta^\mu{}_\nu - \omega^\mu{}_\nu$. Which derivative appears?
- [ ] Q4 Antisymmetrize and identify $L^{\mu\nu}$, checking the sign against $\Lambda v = (1 - \frac i2\omega\mathcal J)v$.
- [ ] Q5 Evaluate $L_i$ and $L^{0i}$ in three-dimensional notation.

> [!tip]- Hints: route in the notes
> - Technique: K2
> - Steps 1–3 of [[§C3.3 How Fields Transform under the Lorentz Group#^der-c3-3-1|Derivation §C3.3.1]]; rotations step 4, boosts step 5.
> - The scalar law to first order: Theorem [[§C1b.1 Fields and Their Transformation Laws#^thm-c1b-1-2|§C1b.1.2]] Infinitesimal Form of the Field Laws.

### The orbital generators obey the Lorentz algebra ★★

$[L^{\mu\nu}, L^{\rho\sigma}] = i(g^{\nu\rho}L^{\mu\sigma} - g^{\mu\rho}L^{\nu\sigma} - g^{\nu\sigma}L^{\mu\rho} + g^{\mu\sigma}L^{\nu\rho})$, see Theorem [[§C3.3 How Fields Transform under the Lorentz Group#^thm-c3-3-2|§C3.3.2]] The Orbital Generators Obey the Lorentz Algebra. **[class exercise, Lecture 7]** ("This thing here, you plug in … Now you need to commute derivatives and x's … there were four terms … get cracking"). *Source: Lecture 7, slide "Lorentz Algebra: Defining Representation" and transcript (Sep 23)*

^nd-thm-c3-3-2

- [ ] Q1 **[state]** State the commutator of two orbital generators.
- [ ] Q2 Compute the elementary commutator $[x^\mu\partial^\nu, x^\rho\partial^\sigma]$. Which single term survives the product rule?
- [ ] Q3 Expand $[\ell^{\mu\nu}, \ell^{\rho\sigma}]$, $\ell^{\mu\nu} = x^\mu\partial^\nu - x^\nu\partial^\mu$, into four such commutators: how many terms in total?
- [ ] Q4 Collect the eight terms by their metric factor and recognize each pair as an $\ell$.
- [ ] Q5 **[why]** Restore the factors $i$: why does $i^2$ on the left produce exactly one $i$ on the right?
- [ ] Q6 **[why]** When all four labels are spatial, which familiar algebra does this reduce to?

> [!tip]- Hints: route in the notes
> - Technique: K3 (Lorentz commutators by index contraction)
> - Steps 1–4 of [[§C3.3 How Fields Transform under the Lorentz Group#^der-c3-3-2|Derivation §C3.3.2]].
> - The spatial reduction: step 2 of [[§CB.5 The Lorentz Algebra꞉ Generators and Commutation Relations#^der-cb-5-6c|Derivation §CB.5.6, the J, K form and the J± split]].

### Orbital plus spin ★

For a field with $D$, $\phi'_a(x) = \phi_a(x) - \frac i2\omega_{\mu\nu}(\mathbb J^{\mu\nu}\phi)_a$ with $\mathbb J^{\mu\nu} = L^{\mu\nu}\delta_a{}^b + D(\mathcal J^{\mu\nu})_a{}^b$; the parts commute, $\mathbb J$ obeys the algebra, and under rotations $\mathbb J_i = L_i + J_i$, see Theorem [[§C3.3 How Fields Transform under the Lorentz Group#^thm-c3-3-3|§C3.3.3]] Orbital Plus Spin. *Source: Lecture 7, slide "Transformation of General Fields" · the user's notes Ch. 7 §7.5*

^nd-thm-c3-3-3

- [ ] Q1 **[state]** Write the total generator of a field with index representation $D$.
- [ ] Q2 Expand $D(\Lambda)\phi(\Lambda^{-1}x)$ to first order: which factor gives the orbital part and which the spin part?
- [ ] Q3 Why do the two parts commute?
- [ ] Q4 Expand $[L + D, L + D]$. Which cross terms vanish, and why does the sum obey the algebra?
- [ ] Q5 **[conv]** The spin generators $S^{\mu\nu}$ of §C1b.1 are in the real convention. How are they related to $D(\mathcal J^{\mu\nu})$, and to the Dirac $S^{\mu\nu} = \frac i4[\gamma^\mu, \gamma^\nu]$?

> [!tip]- Hints: route in the notes
> - Technique: K3
> - Steps 1–3 of [[§C3.3 How Fields Transform under the Lorentz Group#^der-c3-3-3|Derivation §C3.3.3]]; step 4 (commute), step 5 (algebra), step 6 (rotations).
> - Two meanings of $S^{\mu\nu}$: [[§C3.3 How Fields Transform under the Lorentz Group#^cau-c3-3-2|§C3.3, Caution: Two meanings of S^μν]].

### One-component fields carry the trivial representation ★

Every one-dimensional representation of the Lorentz algebra is zero, so a one-component field is $(0, 0)$ with $D(\Lambda) = 1$ and total generator $L^{\mu\nu}$, see Theorem [[§C3.3 How Fields Transform under the Lorentz Group#^thm-c3-3-4|§C3.3.4]] A One-Component Field Carries the Trivial Representation and Theorem [[§CB.5 The Lorentz Algebra꞉ Generators and Commutation Relations#^thm-cb-5-9|§CB.5.9]] One-Dimensional Representations of the Lorentz Algebra Are Zero. *Source: Lecture 7, slide "Transformation of Scalar Fields" · the user's notes Ch. 7 §7.5*

^nd-thm-c3-3-4

- [ ] Q1 **[state]** State the theorem for a one-component field.
- [ ] Q2 In one dimension the six generators are numbers. What does the Lorentz algebra force on numbers whose commutators all vanish?
- [ ] Q3 **[why]** Then why can a one-component field still be a pseudoscalar? What does $(0, 0)$ not fix?

> [!tip]- Hints: route in the notes
> - Technique: K3
> - Steps 1–3 of [[§C3.3 How Fields Transform under the Lorentz Group#^der-c3-3-4|Derivation §C3.3.4]] (the commutators of numbers vanish, so the right sides do).
> - Scalars and pseudoscalars: [[§C3.3 How Fields Transform under the Lorentz Group#^rem-c3-3-3|§C3.3, Remark: Scalars, pseudoscalars and spin zero]].

### The split of the complexified Lorentz algebra ★★

In $\mathfrak{so}(1,3)_{\mathbb C}$, $J_{\pm i} = \frac12(J_i \pm iK_i)$ give $\mathbf J = \mathbf J_+ + \mathbf J_-$, $\mathbf K = -i(\mathbf J_+ - \mathbf J_-)$; the spans $\mathfrak a_\pm$ commute, each is a copy of $\mathfrak{sl}(2, \mathbb C)$, $\mathfrak{so}(1,3)_{\mathbb C} = \mathfrak a_+\oplus\mathfrak a_-$, and complex conjugation exchanges them, see Theorem [[§CB.6 The Lorentz Algebra꞉ the Split J±, Real Forms and 𝔰𝔩(2,ℂ) as a Real Lie Algebra#^thm-cb-6-1|§CB.6.1]] The Split of the Complexified Lorentz Algebra. *Source: Lecture 7, slide "Transformation of General Fields" (clue) · Problem Set 5, Problem 1(a) · the user's notes Ch. 7 §7.4*

^nd-thm-cb-6-1

- [ ] Q1 **[state]** State the split: the definition of $J_{\pm i}$, the inverse formulas, and the three claims about $\mathfrak a_\pm$.
- [ ] Q2 **[def]** In which space are $J_i$ and $K_i$ elements, given that $-iJ_i$, $-iK_i$ are a real basis of $\mathfrak{so}(1,3)$?
- [ ] Q3 Expand $[J_{+i}, J_{-j}]$ by bilinearity into four terms; which algebra relations make the sum vanish?
- [ ] Q4 Expand $[J_{\pm i}, J_{\pm j}]$; why do the boost–boost minus sign and $(\pm i)^2 = -1$ combine to give an angular-momentum algebra?
- [ ] Q5 **[why]** Why does complex conjugation of $\mathfrak{so}(1,3)_{\mathbb C}$ exchange $\mathfrak a_+$ and $\mathfrak a_-$, and why does this mean no nonzero element of $\mathfrak a_+$ lies in the real algebra?

> [!tip]- Hints: route in the notes
> - Technique: K3, K16
> - Step 1 of [[§CB.6 The Lorentz Algebra꞉ the Split J±, Real Forms and 𝔰𝔩(2,ℂ) as a Real Lie Algebra#^pf-cb-6-1|proof of Theorem §CB.6.1]] (where $J$, $K$ live), Steps 3–4 (commuting copies, angular momenta), Steps 6–8 (conjugation and the real algebra).
> - What the split does not mean: [[§CB.6 The Lorentz Algebra꞉ the Split J±, Real Forms and 𝔰𝔩(2,ℂ) as a Real Lie Algebra#^rem-cb-6-1|§CB.6, Remark: What the split does and does not mean]], [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^cau-c3-2-1|§C3.2, Caution: The algebra decomposes; it is not "reducible"]].

### A representation is a pair of commuting angular momenta ★

Part 1 (from the algebra to $\mathbf J_\pm$) is the split above; conversely, two commuting triples $A_i$, $B_i$ each obeying the rotation algebra give a representation with $\mathbf J = \mathbf A + \mathbf B$, $\mathbf K = -i(\mathbf A - \mathbf B)$, see Theorem [[§CB.6 The Lorentz Algebra꞉ the Split J±, Real Forms and 𝔰𝔩(2,ℂ) as a Real Lie Algebra#^thm-cb-6-2|§CB.6.2]] A Representation of the Lorentz Algebra Is a Pair of Commuting Angular Momenta. Part 1 → drilled as [[PHY 513 PS Drill#^ps5-1-a|PS5.1(a)]]. *Source: Problem Set 5, Problem 1 · the user's notes Ch. 7 §7.4*

^nd-thm-cb-6-2

- [ ] Q1 **[state]** State the converse: from which data, and which formulas for $\mathbf J$ and $\mathbf K$?
- [ ] Q2 Check $[J_i, J_j]$ for $\mathbf J = \mathbf A + \mathbf B$: which two of the four terms vanish?
- [ ] Q3 Check $[J_i, K_j]$ and $[K_i, K_j]$: where does the minus sign of the boost–boost relation come from?
- [ ] Q4 **[why]** Why does checking the $\mathbf J$, $\mathbf K$ relations suffice for the covariant relation of all fifteen commutators?

> [!tip]- Hints: route in the notes
> - Technique: K3
> - Steps 2–4 of [[§CB.6 The Lorentz Algebra꞉ the Split J±, Real Forms and 𝔰𝔩(2,ℂ) as a Real Lie Algebra#^der-cb-6-2|Derivation §CB.6.2]]; step 5 back to the covariant form (step 8 of [[§CB.5 The Lorentz Algebra꞉ Generators and Commutation Relations#^der-cb-5-6c|Derivation §CB.5.6, the J, K form and the J± split]]).

### Every Lorentz transformation factorizes ★

$D(e^\omega) = e^{-i\boldsymbol\theta\cdot\mathbf J - i\boldsymbol\eta\cdot\mathbf K} = e^{-i(\boldsymbol\theta - i\boldsymbol\eta)\cdot\mathbf J_+}\,e^{-i(\boldsymbol\theta + i\boldsymbol\eta)\cdot\mathbf J_-}$, the factors commuting, see Theorem [[§CB.6 The Lorentz Algebra꞉ the Split J±, Real Forms and 𝔰𝔩(2,ℂ) as a Real Lie Algebra#^thm-cb-6-3|§CB.6.3]] Every Lorentz Transformation Factorizes. *Source: Problem Set 5, Problem 1(b) (the Weyl laws) · the user's notes Ch. 7 §7.4*

^nd-thm-cb-6-3

- [ ] Q1 **[state]** Write the factorized form of $D(e^\omega)$.
- [ ] Q2 Substitute $\mathbf J$ and $\mathbf K$ in terms of $\mathbf J_\pm$ into the exponent; collect the coefficients of $\mathbf J_+$ and of $\mathbf J_-$.
- [ ] Q3 **[why]** Why does the exponential of the sum split into a product here (which property of $\mathbf J_\pm$)?
- [ ] Q4 **[why]** What are the two "angles" for a pure rotation and for a pure boost? Why are they complex conjugates?
- [ ] Q5 Apply it to $(\frac12, 0)$: which $2\times2$ matrix does a boost along $\hat{\mathbf n}$ give?

> [!tip]- Hints: route in the notes
> - Technique: K4 (exponentiating a generator)
> - Steps 1–3 of [[§CB.6 The Lorentz Algebra꞉ the Split J±, Real Forms and 𝔰𝔩(2,ℂ) as a Real Lie Algebra#^der-cb-6-3|Derivation §CB.6.3]]; step 4 for rotations and boosts; the $(\frac12, 0)$ case: step 3 of [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^der-c3-2-1|Derivation §C3.2.1]].

### (j₊, j₋) is irreducible ★

$(j_+, j_-)$ has dimension $(2j_+ + 1)(2j_- + 1)$, is irreducible, has $\mathbf J_\pm^2 = j_\pm(j_\pm + 1)\mathbb 1$, and different labels give inequivalent representations, see Theorem [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-17-5|§CB.17.5]] (j₊, j₋) Is Irreducible. *Source: Problem Set 5, Problem 1(b) (dimension) · the user's notes Ch. 7 §7.4.3 ("every vector feels both copies")*

^nd-thm-cb-17-5

- [ ] Q1 **[state]** State the four claims of the theorem.
- [ ] Q2 Why do the formulas of the definition represent the Lorentz algebra (which two facts about tensor products)?
- [ ] Q3 Take a nonzero invariant subspace $W$. How does a polynomial in $J_{+3}$, $J_{-3}$ extract a single basis vector $\lvert a\rangle\otimes\lvert b\rangle$ from $W$?
- [ ] Q4 How do the ladder operators of both copies then reach every basis vector?
- [ ] Q5 **[why]** Why do different labels give inequivalent representations? Which property of $j \mapsto j(j+1)$ is used?

> [!tip]- Hints: route in the notes
> - Technique: K16
> - Steps 1–3 of [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^der-cb-17-5|Derivation §CB.17.5]]; step 4 (projecting polynomial), step 5 (ladders), step 6 (inequivalence).

### Every finite-dimensional representation is a sum of (j₊, j₋) ★

Every representation of the Lorentz algebra on a finite-dimensional complex space is a direct sum of pieces $(j_+, j_-)$ with fixed multiplicities, and carries an inner product in which all $J_{\pm i}$ are Hermitian, see Theorem [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-17-6|§CB.17.6]] Every Finite-Dimensional Representation Is a Sum of (j₊, j₋). *Source: Problem Set 5, Problem 1(b) ("labelled by a pair (j₊, j₋)", statement) · the user's notes Ch. 7 §7.4.3 (stated)*

^nd-thm-cb-17-6

- [ ] Q1 **[state]** State the classification, including the claim about an inner product.
- [ ] Q2 Which compact group integrates the six matrices $-iJ_{\pm i}$? What input from Lie theory is quoted and not derived?
- [ ] Q3 How is an invariant inner product built by averaging, and why are the $J_{\pm i}$ Hermitian for it?
- [ ] Q4 How does Hermiticity give complete reducibility (orthogonal complements)?
- [ ] Q5 On one irreducible piece, why are $\mathbf J_\pm^2$ constants, and how do the highest-weight vectors of the $+$ copy build an isomorphism with $(j_+, j_-)$?
- [ ] Q6 **[why]** The compact group used is not the Lorentz group. Why is the trick legitimate ("Weyl's unitarian trick"), and why does it not make boosts unitary?

> [!tip]- Hints: route in the notes
> - Technique: K16
> - Steps 1–2 of [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^der-cb-17-6|Derivation §CB.17.6]] (two commuting $\mathfrak{su}(2)$'s), steps 3–4 (invariant inner product, Hermitian), step 5 (complete reducibility), steps 6–8 (one piece is $(j_+, j_-)$), step 9 (multiplicities).
> - Boosts stay non-unitary: Theorem [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-17-15|§CB.17.15]] No Finite-Dimensional Representation Is Unitary.

### The (½, 0) and (0, ½) representations

The table of $\mathbf J_\pm$, $\mathbf J$, $\mathbf K$ and $D(e^\omega)$ on $(\frac12, 0)$ and $(0, \frac12)$, matching PS's $\psi_L$, $\psi_R$, see Theorem [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^thm-c3-2-1|§C3.2.1]] The Representations (½, 0) and (0, ½). → drilled as [[PHY 513 PS Drill#^ps5-1-b|PS5.1(b)]].

^nd-thm-c3-2-1

### The vector representation is (½, ½): Casimirs and classification ★★

In the basis $(v^0, v^1, v^2, v^3)$, $\mathbf J^2 = \operatorname{diag}(0, 2, 2, 2)$, $\mathbf K^2 = -\operatorname{diag}(3, 1, 1, 1)$, $\mathbf J\cdot\mathbf K = \mathbf K\cdot\mathbf J = 0$, so $\mathbf J_\pm^2 = \frac34\mathbb 1$; with the classification and the dimension count, the vector representation is equivalent to $(\frac12, \frac12)$ by an invertible intertwiner, see Theorem [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-17-7|§CB.17.7]] The Vector Representation Is (½, ½) (the course's form Theorem [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^thm-c3-2-2|§C3.2.2]] The Vector Representation Is (½, ½)). *Source: the user's notes Ch. 7 §7.3, §7.4.3 · Yu §4.2.2 · the rigor fix of 2026-10-13 (the user's request)*

^nd-thm-cb-17-7

- [ ] Q1 **[state]** State what "the vector representation is $(\frac12, \frac12)$" means precisely (equivalence by what kind of map).
- [ ] Q2 Write $K_i$ and $J_i$ with matrix units $E_{ab}$. Compute $\mathbf J^2$ and $\mathbf K^2$.
- [ ] Q3 Compute $\mathbf J\cdot\mathbf K$ and $\mathbf K\cdot\mathbf J$. Why must both orders be checked?
- [ ] Q4 Expand $\mathbf J_\pm^2 = \frac14(\mathbf J \pm i\mathbf K)\cdot(\mathbf J \pm i\mathbf K)$ into four terms and evaluate.
- [ ] Q5 Run the identification: decompose $\mathbb C^4$ by the classification, transport the Casimirs through the intertwiners, solve $j(j+1) = \frac34$, and count dimensions. Which step needs the classification theorem?
- [ ] Q6 **[why]** Why do equal Casimir values on all of $\mathbb C^4$ not by themselves say "$\mathbb C^4$ is $(\frac12, \frac12)$"? What would remain possible without the dimension count?
- [ ] Q7 **[why]** Which by-product gives the rotation content $0\oplus1$, and why are time and space not "$\mathbf J_+$ and $\mathbf J_-$"?

> [!tip]- Hints: route in the notes
> - Technique: K16 (Casimirs + classification)
> - Steps 1–2 of [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^pf-cb-17-7|proof of Theorem §CB.17.7]] (generators), steps 3–5 (squares and mixed products), step 6 (Casimirs), step 7 (i)–(iv) (identification with Theorem [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-17-6|§CB.17.6]] Every Finite-Dimensional Representation Is a Sum of (j₊, j₋) and Theorem [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-17-5|§CB.17.5]] (j₊, j₋) Is Irreducible).
> - The course's $4\times4$ computation: [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^der-c3-2-2|Derivation §C3.2.2]]; components, not states: [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^cau-c3-2-3|§C3.2, Caution: Components, not states]].

### The vector representation is (½, ½): the explicit intertwiner ★★

$T(v) = (v_\mu\sigma^\mu)\,i\sigma^2$, read in $\mathbb C^2\otimes\mathbb C^2$ through $\sum Y_{ab}e_a\otimes e_b \leftrightarrow (Y_{ab})$, is an invertible map with $T\,R(X) = \rho(X)\,T$ for all six generators, $R$ the vector and $\rho$ the $(\frac12, \frac12)$ representation, see [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^pf-cb-17-7b|proof of Theorem §CB.17.7, second route]]. *Source: written for the rigor fix of 2026-10-13 (the user's request) · reading of the $SL(2, \mathbb C)$ covering*

^nd-pf-cb-17-7b

- [ ] Q1 **[state]** What exactly must $T$ satisfy, and why is it enough to check six generators?
- [ ] Q2 **[def]** Under the identification of $\mathbb C^2\otimes\mathbb C^2$ with $2\times2$ matrices $Y$, how do $A\otimes\mathbb 1$ and $\mathbb 1\otimes B$ act on $Y$? Write $\rho(J_i)Y$ and $\rho(K_i)Y$.
- [ ] Q3 Why is $T$ invertible?
- [ ] Q4 Move the right factor through $\varepsilon = i\sigma^2$: what is $\varepsilon\sigma_i^{\mathsf T}\varepsilon^{-1}$? Write $\rho(J_i)T(v)$ and $\rho(K_i)T(v)$ as a commutator and an anticommutator with $M = v_\mu\sigma^\mu$.
- [ ] Q5 Evaluate both with the Pauli algebra and compare with $T(J_iv)$ and $T(K_iv)$.
- [ ] Q6 **[why]** Which group statement is this the derivative of ($M \mapsto \lambda M\lambda^\dagger$ rewritten for $Y = M\varepsilon$)?
- [ ] Q7 **[why]** What does this proof establish that the Casimir proof does not, and what input of the Casimir proof does it avoid?

> [!tip]- Hints: route in the notes
> - Technique: K16 (intertwiner)
> - Step 1 of [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^pf-cb-17-7b|proof of Theorem §CB.17.7, second route]] (matrix picture), step 2 (the map), step 3 (through ε), steps 4–5 (rotations, boosts), step 7 (group behind it).
> - The dictionary $x \leftrightarrow x_\mu\sigma^\mu$: Theorem [[§CB.16 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-16-3|§CB.16.3]] Four-Vectors as Hermitian Matrices; ε: Theorem [[§CB.8 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-8-15|§CB.8.15]] ε on ℂ² and SL(2,ℂ) = Sp(2,ℂ).

### Labels of a four-vector and of a left-handed Weyl spinor

The short-response route: dimension $4$, then the $2\pi$ rotation decides $(\frac12, \frac12)$; $\psi_L$ is $(\frac12, 0)$, see [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^der-c3-2-2b|Derivation §C3.2.2, second route]]. → drilled as [[PHY 513 PS Drill#^ps7-1-d|PS7.1(d)]].

^nd-der-c3-2-2b

### Rotation content and the sign of a 2π rotation ★

Under rotations $(j_+, j_-)$ is $D^{(j_+)}\otimes D^{(j_-)}$, containing spins $\lvert j_+ - j_-\rvert, \dots, j_+ + j_-$ once each; a $2\pi$ rotation acts as $(-1)^{2(j_+ + j_-)}$, so half-integer $j_+ + j_-$ gives a two-valued representation of $SO^+(1,3)$, see Theorem [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-17-9|§CB.17.9]] Rotation Content and the Sign of a 2π Rotation. *Source: Problem Set 6, Problem 4(d) · Problem Set 7, Problem 1(d) (the user's route) · the user's notes Ch. 7 §7.4.3*

^nd-thm-cb-17-9

- [ ] Q1 **[state]** State the rotation content of $(j_+, j_-)$ and the action of a $2\pi$ rotation.
- [ ] Q2 Set $\boldsymbol\eta = 0$ in the factorization. Which tensor product of rotation matrices results?
- [ ] Q3 Which Clebsch–Gordan series gives the spins?
- [ ] Q4 **[why]** Why is the sign $(-1)^{2j}$ the same for every spin in the series?
- [ ] Q5 **[why]** Why does a sign $-1$ for the identity element $e^{2\pi M^{12}} = \mathbb 1$ mean $D$ is not a representation of $SO^+(1,3)$?

> [!tip]- Hints: route in the notes
> - Technique: K4
> - Steps 1–2 of [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^der-cb-17-9|Derivation §CB.17.9]], step 3 ($2\pi$), step 4 (consistency), step 5 (the identity of $SO^+(1,3)$).

### Tensor products add each copy separately ★

$(j_+, j_-)\otimes(j'_+, j'_-) = \bigoplus(J_+, J_-)$ with $J_\pm$ from $\lvert j_\pm - j'_\pm\rvert$ to $j_\pm + j'_\pm$; in particular $(\frac12, \frac12)\otimes(\frac12, \frac12) = (1, 1)\oplus(1, 0)\oplus(0, 1)\oplus(0, 0)$, see Theorem [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-17-12|§CB.17.12]] Tensor Products Add Each Copy Separately. *Source: the user's notes Ch. 7 · Lecture 8, slide "Fermion Bilinears" (scalar, vector, tensor from strings of γ's)*

^nd-thm-cb-17-12

- [ ] Q1 **[state]** State the rule for the product of two representations $(j_+, j_-)$ and $(j'_+, j'_-)$.
- [ ] Q2 What are the generators of $D\otimes D'$, and why do the $+$ copies add among themselves?
- [ ] Q3 Apply it to two four-vectors: which pieces, with which dimensions, and which tensors carry them (trace, antisymmetric part, symmetric traceless part)?
- [ ] Q4 **[why]** Why is the antisymmetric two-tensor $(1, 0)\oplus(0, 1)$ over $\mathbb C$ but irreducible over $\mathbb R$?

> [!tip]- Hints: route in the notes
> - Technique: K16
> - Steps 1–4 of [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^der-cb-17-12|Derivation §CB.17.12]]; step 5 for two vectors; the tensors: Theorem [[§C3.3 How Fields Transform under the Lorentz Group#^thm-c3-3-6|§C3.3.6]] Two-Index Tensor Fields; over ℝ: Theorem [[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-18-11|§CB.18.11]] Two-Forms Are (1, 0) ⊕ (0, 1).

### Vector fields, upper and lower index ★

$A'^\mu(x) = \Lambda^\mu{}_\nu A^\nu(\Lambda^{-1}x)$, generators $\mathcal J^{\mu\nu}$, representation $(\frac12, \frac12)$; lower components transform with $\Lambda_\mu{}^\nu = (\Lambda^{-1})^\nu{}_\mu$, an equivalent representation; the gradient of a scalar is a lower-index vector field, see Theorem [[§C3.3 How Fields Transform under the Lorentz Group#^thm-c3-3-5|§C3.3.5]] Vector Fields, Upper and Lower Index and Example [[§C3.3 How Fields Transform under the Lorentz Group#^ex-c3-3-1|§C3.3.1]] The Gradient of a Scalar Field. *Source: Lecture 7, slide "Transformation of Vector and Spinor Fields" · the user's notes Ch. 7 §7.5*

^nd-thm-c3-3-5

- [ ] Q1 **[state]** Write the transformation laws of $A^\mu$ and of $A_\mu$.
- [ ] Q2 Lower the index in $A'^\mu$ and use $\Lambda^{\mathsf T}g\Lambda = g$: which matrix acts on $A_\mu$, and why is it the inverse transpose?
- [ ] Q3 Differentiate $\phi'(x) = \phi(\Lambda^{-1}x)$ by the chain rule. Which matrix appears, and with which index on top?
- [ ] Q4 **[why]** Why is the lower-index representation equivalent to the upper one (which intertwiner)?
- [ ] Q5 **[why]** Why must every derivative in a Lagrangian be contracted?

> [!tip]- Hints: route in the notes
> - Technique: K2
> - Steps 1–2 of [[§C3.3 How Fields Transform under the Lorentz Group#^der-c3-3-5|Derivation §C3.3.5]], steps 3–5 (lower components, inverse transpose, equivalence through $g$); the gradient: Example [[§C3.3 How Fields Transform under the Lorentz Group#^ex-c3-3-1|§C3.3.1]] The Gradient of a Scalar Field.
> - Invariant Lagrangians: [[§C3.3 How Fields Transform under the Lorentz Group#^rem-c3-3-5|§C3.3, Remark: Invariant Lagrangians are (0, 0) pieces]].

### The field strength is (1, 0) ⊕ (0, 1) ★

$\delta\mathbf E = \boldsymbol\theta\times\mathbf E - \boldsymbol\eta\times\mathbf B$, $\delta\mathbf B = \boldsymbol\theta\times\mathbf B + \boldsymbol\eta\times\mathbf E$, so $\delta(\mathbf E \mp i\mathbf B) = (\boldsymbol\theta \mp i\boldsymbol\eta)\times(\mathbf E \mp i\mathbf B)$: $\mathbf E - i\mathbf B$ is $(1, 0)$, $\mathbf E + i\mathbf B$ is $(0, 1)$, see Theorem [[§C3.3 How Fields Transform under the Lorentz Group#^thm-c3-3-7|§C3.3.7]] The Field Strength Is (1, 0) ⊕ (0, 1). *Source: Lecture 8 transcript (Sep 28: "it mixes E and B fields according to certain rules") · the user's notes Ch. 7*

^nd-thm-c3-3-7

- [ ] Q1 **[state]** State how $\mathbf E \mp i\mathbf B$ transform and which label each carries.
- [ ] Q2 Write $\omega^\mu{}_\nu$ for a rotation and for a boost in terms of $\boldsymbol\theta$, $\boldsymbol\eta$.
- [ ] Q3 Compute $\delta F^{0j}$ and $\delta F^{jk}$ under a boost. Which fields mix?
- [ ] Q4 Form the complex combinations; compare with the factorized angles $\boldsymbol\theta \mp i\boldsymbol\eta$ of the two copies.
- [ ] Q5 **[conv]** Which two convention choices could swap the labels of $\mathbf E \pm i\mathbf B$?

> [!tip]- Hints: route in the notes
> - Technique: K2, K16
> - Steps 1–5 of [[§C3.3 How Fields Transform under the Lorentz Group#^der-c3-3-7|Derivation §C3.3.7]], step 6 (complex combinations), step 7 (compare with spin 1); the angles: Theorem [[§CB.6 The Lorentz Algebra꞉ the Split J±, Real Forms and 𝔰𝔩(2,ℂ) as a Real Lie Algebra#^thm-cb-6-3|§CB.6.3]] Every Lorentz Transformation Factorizes.
> - Labels: [[§C3.3 How Fields Transform under the Lorentz Group#^cau-c3-3-1|§C3.3, Caution: Which half of F is called (1, 0)]].

### Parity exchanges the two copies ★

The parity automorphism $\mathbf J \mapsto \mathbf J$, $\mathbf K \mapsto -\mathbf K$ preserves the algebra and swaps $\mathbf J_+ \leftrightarrow \mathbf J_-$; on four-vectors it is conjugation by $\mathcal P = \operatorname{diag}(1, -1, -1, -1)$, and a parity-invariant field contains $(j_+, j_-)$ and $(j_-, j_+)$ with equal multiplicity, see Theorem [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^thm-c3-2-3|§C3.2.3]] Parity on Four-Vectors; Parity-Invariant Fields Contain Both Copies and Theorem [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-17-13|§CB.17.13]] The Parity Automorphism Exchanges the Two Copies. *Source: the user's notes Ch. 7 §7.4.6 · Lecture 8 transcript (both Weyl halves needed for a mass)*

^nd-thm-c3-2-3

- [ ] Q1 **[state]** State what parity does to $\mathbf J$, $\mathbf K$, $\mathbf J_\pm$ and to the labels.
- [ ] Q2 Check that $\mathbf K \mapsto -\mathbf K$ preserves each of the three relations of the algebra.
- [ ] Q3 Compute $\mathcal P\mathcal J^{ij}\mathcal P^{-1}$ and $\mathcal P\mathcal J^{0i}\mathcal P^{-1}$ in the vector representation.
- [ ] Q4 **[why]** If an invertible $Q$ on $V$ implements parity, why do $(j_+, j_-)$ and $(j_-, j_+)$ appear equally often? Apply to the Dirac spinor.

> [!tip]- Hints: route in the notes
> - Technique: K16
> - Steps 1–3 of [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^der-cb-17-13|Derivation §CB.17.13]], step 4 (equal multiplicity); the vector case: [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^der-c3-2-3|Derivation §C3.2.3]].

### Complex conjugation exchanges the two copies ★

$\bar D(\Lambda) = D(\Lambda)^\ast$ is a representation with generators $-D(\mathcal J^{\mu\nu})^\ast$; the conjugate of $(j_+, j_-)$ is equivalent to $(j_-, j_+)$, the equivalence being the rotation by $\pi$ about the 2-axis, see Theorem [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-17-14|§CB.17.14]] Complex Conjugation Exchanges the Two Copies. *Source: the user's notes Ch. 7 §7.4.6, Ch. 8 (the conjugate of a left-handed spinor)*

^nd-thm-cb-17-14

- [ ] Q1 **[state]** State what conjugation does to the generators and to the labels.
- [ ] Q2 Conjugate the first-order expansion of $D(e^{s\omega})$: why does the generator acquire a minus sign as well as a star?
- [ ] Q3 Compute $\bar{\mathbf J}_\pm$ in terms of $\mathbf J_\mp^\ast$.
- [ ] Q4 **[why]** For spin $\frac12$, which matrix turns $-\boldsymbol\sigma^\ast/2$ back into $\boldsymbol\sigma/2$, and how does this show that $\sigma^2\psi_L^\ast$ is right-handed?

> [!tip]- Hints: route in the notes
> - Technique: K16
> - Steps 1–4 of [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^der-cb-17-14|Derivation §CB.17.14]], step 6 (assemble); the spin-½ case: Theorem [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-4|§C5a.5.4]] Dotted Indices, Conjugation and the Invariant Pairings, Theorem [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-1|§C5a.1.1]] Identities of σ^μ and σ̄^μ (part 3).

### No finite-dimensional representation is unitary ★★

In an inner product with $\mathbf J_\pm$ Hermitian, $\mathbf J$ is Hermitian and $\mathbf K$ anti-Hermitian, a boost is Hermitian positive and not unitary; a finite-dimensional representation of $SO^+(1,3)$ that is unitary for some inner product is trivial, see Theorem [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-17-15|§CB.17.15]] No Finite-Dimensional Representation Is Unitary. *Source: Lecture 8, slide "The Hermitean Conjugate Spinor" ("Rotations S^ij hermitean and boosts S^0i antihermitean") · the user's notes Ch. 7 (Principle "Hermitian generators do not make boosts unitary")*

^nd-thm-cb-17-15

- [ ] Q1 **[state]** State both parts of the theorem.
- [ ] Q2 From $\mathbf K = -i(\mathbf J_+ - \mathbf J_-)$ with $\mathbf J_\pm$ Hermitian, decide the Hermiticity of $\mathbf K$ and of $e^{-i\boldsymbol\eta\cdot\mathbf K}$.
- [ ] Q3 If $D$ were unitary, what would the generators have to be? What are the eigenvalues of $K_3$ on a piece $(j_+, j_-)$?
- [ ] Q4 Conclude that only $(0, 0)$ pieces can occur, and why the representation is then trivial.
- [ ] Q5 **[why]** Why is this no contradiction with the unitary $U(\Lambda)$ on states? Where does the infinite dimension come in?

> [!tip]- Hints: route in the notes
> - Technique: K16
> - Steps 1–2 of [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^der-cb-17-15|Derivation §CB.17.15]], steps 3–4 (unitary means Hermitian generators; imaginary eigenvalues of $K_3$), step 5 (trivial).
> - Two kinds of representation: [[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra#^rem-c3-4-2|§C3.4, Remark: Two kinds of representation]]; components, not states: [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^cau-c3-2-3|§C3.2, Caution: Components, not states]].

### The quantum generators are Hermitian ★

All ten generators $\hat J^{\mu\nu}$, $\hat P^\mu$ of a unitary $U(\Lambda, a)$ are Hermitian, boosts included, and $U^{-1} = \mathbb 1 + \frac i2\omega_{\mu\nu}\hat J^{\mu\nu} - i\varepsilon_\mu\hat P^\mu$ to first order, see Theorem [[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra#^thm-c3-4-2|§C3.4.2]] The Generators Are Hermitian. *Source: the user's notes Ch. 7 §7.6*

^nd-thm-c3-4-2

- [ ] Q1 **[state]** State the theorem and the first-order inverse.
- [ ] Q2 Take the adjoint of the first-order expansion. Why are $\omega_{\mu\nu}$ and $\varepsilon_\mu$ unaffected?
- [ ] Q3 Multiply $U^\dagger U$ to first order and impose unitarity. Which terms must cancel?
- [ ] Q4 **[why]** Contrast with the finite-dimensional $D(\Lambda)$: which hypothesis holds for $U$ and fails for $D$?

> [!tip]- Hints: route in the notes
> - Technique: K11 ((anti)commutator algebra)
> - Steps 1–4 of [[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra#^der-c3-4-2|Derivation §C3.4.2]]; the contrast: [[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra#^rem-c3-4-2|§C3.4, Remark: Two kinds of representation]], Theorem [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-17-15|§CB.17.15]] No Finite-Dimensional Representation Is Unitary.

### The Poincaré algebra ★

$U^{-1}\hat P^\rho U = \Lambda^\rho{}_\mu\hat P^\mu$ and the tensor law of $\hat J$ give $[\hat J^{\mu\nu}, \hat P^\rho] = i(g^{\nu\rho}\hat P^\mu - g^{\mu\rho}\hat P^\nu)$, $[\hat P^\mu, \hat P^\nu] = 0$; in three-dimensional form $[\hat K^i, \hat P^j] = -i\delta_{ij}\hat H$, $[\hat K^i, \hat H] = -i\hat P^i$, see Theorem [[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra#^thm-c3-4-5|§C3.4.5]] The Poincaré Algebra and Theorem [[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra#^thm-c3-4-4|§C3.4.4]] How the Generators Transform. *Source: the user's notes Ch. 7 §7.6 · Yu §3.2*

^nd-thm-c3-4-5

- [ ] Q1 **[state]** Write the commutators $[\hat J^{\mu\nu}, \hat P^\rho]$ and $[\hat P^\mu, \hat P^\nu]$.
- [ ] Q2 Conjugate a translation by a Lorentz transformation in the group. What is $U^{-1}(\Lambda)\hat P^\rho U(\Lambda)$?
- [ ] Q3 Take $\Lambda$ infinitesimal and compare the coefficients of $\omega_{\mu\nu}$ (antisymmetrized).
- [ ] Q4 Insert $g^{00} = 1$, $g^{ij} = -\delta_{ij}$ to get the three-dimensional relations for $\hat H$, $\hat{\mathbf P}$, $\hat{\mathbf J}$, $\hat{\mathbf K}$.
- [ ] Q5 **[why]** $[\hat K^i, \hat H] \ne 0$, yet the boost charge is conserved. How?

> [!tip]- Hints: route in the notes
> - Technique: K3
> - Steps 1–6 of [[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra#^der-c3-4-4|Derivation §C3.4.4]] (how the generators transform); Steps 1–3 of [[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra#^der-c3-4-5|Derivation §C3.4.5]] ($[\hat J, \hat P]$), step 4 ($[\hat P, \hat P]$), step 5 (three-dimensional form).
> - Conservation with explicit time dependence: [[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra#^rem-c3-4-4|§C3.4, Remark: What the algebra says: conservation, and no boost quantum number]].

### P² is a Casimir; an invariant vacuum has zero momentum ★

$\hat P^2$ commutes with all ten generators and is Poincaré invariant; a Lorentz-invariant vacuum eigenvector of $\hat P^\mu$ has $p_0^\mu = 0$, so the generators are the normal-ordered $\hat H$, $\hat{\mathbf P}$, see Theorem [[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra#^thm-c3-4-6|§C3.4.6]] P² Is a Casimir Operator and Theorem [[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra#^thm-c3-4-7|§C3.4.7]] An Invariant Vacuum Has Zero Four-Momentum. *Source: the user's notes Ch. 7 §7.6*

^nd-thm-c3-4-6

- [ ] Q1 **[state]** State both theorems.
- [ ] Q2 Lower an index in $[\hat P, \hat J]$ and apply the product rule to $[\hat P_\mu\hat P^\mu, \hat J^{\rho\sigma}]$. Why do the two terms cancel?
- [ ] Q3 For the vacuum: what is the four-momentum of $U(\Lambda)\lvert0\rangle$, and which four-vector is fixed by every $\Lambda$?
- [ ] Q4 **[why]** Why is a zero-point energy $E_0 \ne 0$ with $\hat{\mathbf P}\lvert0\rangle = 0$ incompatible with an invariant vacuum?

> [!tip]- Hints: route in the notes
> - Technique: K3, K14
> - Steps 1–3 of [[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra#^der-c3-4-6|Derivation §C3.4.6]]; Steps 1–4 of [[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra#^der-c3-4-7|Derivation §C3.4.7]].

### Lorentz transformations of a quantum field: orbital plus spin ★

From the covariance law, $[\hat\Phi_a(x), \hat J^{\mu\nu}] = L^{\mu\nu}\hat\Phi_a(x) + D(\mathcal J^{\mu\nu})_a{}^b\hat\Phi_b(x)$ and $[\hat\Phi_a(x), \hat P^\mu] = i\partial^\mu\hat\Phi_a(x)$, see Theorem [[§C3.5 Covariant Quantum Fields and the Free Scalar's Representation#^thm-c3-5-3|§C3.5.3]] Lorentz Transformations of a Field: Orbital plus Spin and Theorem [[§C3.5 Covariant Quantum Fields and the Free Scalar's Representation#^thm-c3-5-2|§C3.5.2]] Translations of a Field; the Heisenberg Equation. *Source: the user's notes Ch. 7 §7.6*

^nd-thm-c3-5-3

- [ ] Q1 **[state]** Write both commutators of a covariant field with the generators.
- [ ] Q2 Expand the left side $U^{-1}\hat\Phi U$ to first order in $\omega$: which commutator appears?
- [ ] Q3 Expand the right side $D(\Lambda)\hat\Phi(\Lambda^{-1}x)$: which part comes from the argument and which from the index?
- [ ] Q4 **[why]** Which operators in the result act on the Hilbert space and which on the components? Where do $D$ and $U$ meet?
- [ ] Q5 **[conv]** Why does the time component of the translation law reproduce the Heisenberg equation with the course's sign of $\hat P$?

> [!tip]- Hints: route in the notes
> - Technique: K14
> - Steps 1–5 of [[§C3.5 Covariant Quantum Fields and the Free Scalar's Representation#^der-c3-5-3|Derivation §C3.5.3]]; translations: Steps 1–6 of [[§C3.5 Covariant Quantum Fields and the Free Scalar's Representation#^der-c3-5-2|Derivation §C3.5.2]].
> - The meeting point: [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^cau-c3-2-3|§C3.2, Caution: Components, not states]].

### The free scalar field carries a unitary representation ★

On wave packets, $(U(\Lambda, a)g)(\mathbf p) = e^{ip\cdot a}g(\Lambda^{-1}\mathbf p)$ is a unitary representation of the Poincaré group, $U(\Lambda, a)\lvert\mathbf p\rangle = e^{i(\Lambda p)\cdot a}\lvert\Lambda\mathbf p\rangle$; it extends to Fock space with an invariant vacuum, and the mode operators transform with the factor $\sqrt{E_{\Lambda\mathbf p}/E_{\mathbf p}}$, see Theorem [[§C3.5 Covariant Quantum Fields and the Free Scalar's Representation#^thm-c3-5-4|§C3.5.4]] The Free Scalar Field Carries a Unitary Representation. *Source: the user's notes Ch. 7 §7.6 · Lecture 4 (relativistic normalization)*

^nd-thm-c3-5-4

- [ ] Q1 **[state]** State the action of $U(\Lambda, a)$ on wave packets, on $\lvert\mathbf p\rangle$ and on $\hat a^\dagger_{\mathbf p}$.
- [ ] Q2 **[def]** Which measure on the mass shell is Lorentz invariant, and why does $\Lambda$ map the shell onto itself?
- [ ] Q3 Compute the norm of a transformed wave packet. Which change of variables shows unitarity?
- [ ] Q4 Check the composition law by applying two transformations in turn.
- [ ] Q5 **[why]** Where does the factor $\sqrt{E_{\Lambda\mathbf p}/E_{\mathbf p}}$ in the law of $\hat a^\dagger_{\mathbf p}$ come from (which normalization of states)?
- [ ] Q6 **[why]** This $U$ is infinite-dimensional and unitary, the field's $D$ is trivial here. Which of the two does the label $(0, 0)$ describe?

> [!tip]- Hints: route in the notes
> - Technique: K9 (mode substitution), K14
> - Step 1 of [[§C3.5 Covariant Quantum Fields and the Free Scalar's Representation#^der-c3-5-4|Derivation §C3.5.4]] (invariant measure), steps 2–3 (norm, unitarity), step 4 (composition), steps 5–6 (kernel form, Fock space), step 7 (mode operators).
> - Components, not states: [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^cau-c3-2-3|§C3.2, Caution: Components, not states]].

### The Noether charges are the generators ★

For the free real scalar the normal-ordered Noether charges $\hat P^\mu = \int d^3x\,\hat T^{0\mu}$ and $\hat J^{\mu\nu} = \int d^3x\,\hat{\mathcal M}^{0\mu\nu}$ satisfy $[\hat\phi, \hat P^\mu] = i\partial^\mu\hat\phi$ and $[\hat\phi, \hat J^{\mu\nu}] = L^{\mu\nu}\hat\phi$, so they are the generators of Definition [[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra#^def-c3-4-1|§C3.4.1]] Generators of Quantum Poincaré Transformations; the boost generator is $\hat K^i = \hat J^{0i} = t\hat P^i - \int d^3x\,x^i\hat T^{00} = -\hat K^i_{\rm N}$, see Theorem [[§C3.5 Covariant Quantum Fields and the Free Scalar's Representation#^thm-c3-5-6|§C3.5.6]] The Noether Charges Are the Generators. *Source: the user's notes Ch. 7 §7.6 · Lecture 3 (Noether charges)*

^nd-thm-c3-5-6

- [ ] Q1 **[state]** State the two commutators and the identification with the generators, including the boost dictionary.
- [ ] Q2 Compute $[\hat\phi(\mathbf x), \hat\pi(\mathbf y)\partial^k\hat\phi(\mathbf y)]$ and $[\hat\phi(\mathbf x), \hat{\mathcal H}(\mathbf y)]$ at equal times.
- [ ] Q3 Integrate to get $[\hat\phi, \hat P^\mu]$. Which delta function is used?
- [ ] Q4 Do the rotations $\hat J^{jk}$ and then the boosts $\hat J^{0k}$: where does the explicit $t$ in the boost charge enter?
- [ ] Q5 **[conv]** Why is the generator $\hat K^i = \hat J^{0i}$ minus the Noether boost charge $\hat K^i_{\rm N} = \hat J^{i0}$?
- [ ] Q6 **[why]** Why must $\hat H$ be normal ordered for these to be the generators of a representation with an invariant vacuum?

> [!tip]- Hints: route in the notes
> - Technique: K11 ((anti)commutator algebra), K12
> - Steps 1–2 of [[§C3.5 Covariant Quantum Fields and the Free Scalar's Representation#^der-c3-5-6|Derivation §C3.5.6]], step 3 (momentum), steps 4–5 (rotations, boosts), step 6 (generators), step 7 (boost dictionary).
> - Normal ordering and the vacuum: Theorem [[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra#^thm-c3-4-7|§C3.4.7]] An Invariant Vacuum Has Zero Four-Momentum; [[Larsen PHY 513|register: Quantum Poincaré transformations]].

# T8. Spinors, the Dirac equation and its solutions

## Definitions and conventions T8

### Dirac matrices and the Clifford algebra

Four $n\times n$ matrices with $\{\gamma^\mu, \gamma^\nu\} = 2g^{\mu\nu}\mathbb 1_n$; $\mu$ is a spacetime index, rows and columns are spinor indices; $\gamma_\mu = g_{\mu\nu}\gamma^\nu$, see Definition [[§CB.11 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^def-cb-11-11|§CB.11.11]] The Dirac Matrices. *Source: Lecture 7, slide "The Dirac Representation" · Lecture 8, "Cheat Sheet I" ("4×4 identity matrix on RHS usually not written")*

^nd-def-cb-11-11

- [ ] Q1 **[def]** Write the Clifford relation, with the identity matrix shown.
- [ ] Q2 What are $(\gamma^0)^2$, $(\gamma^i)^2$, and $\gamma^\mu\gamma^\nu$ for $\mu \ne \nu$ in terms of each other?
- [ ] Q3 Split $\gamma^\mu\gamma^\nu$ into its symmetric and antisymmetric parts. What survives when it is contracted with a symmetric tensor such as $\partial_\mu\partial_\nu$?
- [ ] Q4 **[why]** Which indices of $(\gamma^\mu)_{ab}$ change under a change of basis of spinor space, and which under a Lorentz transformation?

> [!tip]- Hints: route in the notes
> - Technique: K5 (γ-matrix algebra)
> - Definition [[§CB.11 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^def-cb-11-11|§CB.11.11]] The Dirac Matrices; first consequences and the split: Theorem [[§CB.11 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^thm-cb-11-12|§CB.11.12]] First Consequences of the Clifford Algebra; slots: [[§C5a.5 Chirality and Weyl Spinors#^rem-c5a-5-8|§C5a.5, Remark: The index rule as a table]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^rem-c5a-4-3|§C5a.4, Remark: Why γ is fixed under a Lorentz transformation but not under a change of basis]].

### The matrices σ^μ and σ̄^μ

$\sigma^\mu = (\mathbb 1, \boldsymbol\sigma)$, $\bar\sigma^\mu = (\mathbb 1, -\boldsymbol\sigma)$, $\sigma_\mu = (\mathbb 1, -\boldsymbol\sigma)$; $X = x_\mu\sigma^\mu = x^0 - \mathbf x\cdot\boldsymbol\sigma$, $\bar X = x_\mu\bar\sigma^\mu = x^0 + \mathbf x\cdot\boldsymbol\sigma$, see Definition [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-2|§C5a.1.2]] The Matrices σ^μ and σ̄^μ. *Source: Lecture 8, slide "Dirac Equation in 2-Component Form" · Lecture 9, "Cheat Sheet"*

^nd-def-c5a-1-2

- [ ] Q1 **[def]** Define $\sigma^\mu$ and $\bar\sigma^\mu$ and write $p\cdot\sigma$, $p\cdot\bar\sigma$ for a four-vector $p$.
- [ ] Q2 **[conv]** Why does $p\cdot\sigma$ contain $-\mathbf p\cdot\boldsymbol\sigma$ although $\sigma^\mu$ has $+\boldsymbol\sigma$?
- [ ] Q3 What are $\operatorname{tr}(\sigma^\mu\bar\sigma^\nu)$, $\sigma^\mu\bar\sigma^\nu + \sigma^\nu\bar\sigma^\mu$ and $X\bar X$?
- [ ] Q4 **[why]** What does conjugation by $\sigma^2$ do to $(\sigma^\mu)^\ast$, and where is this used?

> [!tip]- Hints: route in the notes
> - Technique: K5
> - Definition [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-2|§C5a.1.2]] The Matrices σ^μ and σ̄^μ; identities: Steps 1–4 of [[§C5a.1 Spinor Space and the Clifford Action#^der-c5a-1-1|Derivation §C5a.1.1]].

### The chiral basis

$\gamma^0 = \begin{pmatrix}0 & \mathbb 1\\ \mathbb 1 & 0\end{pmatrix}$, $\gamma^i = \begin{pmatrix}0 & \sigma^i\\ -\sigma^i & 0\end{pmatrix}$, i.e. $\gamma^\mu = \begin{pmatrix}0 & \sigma^\mu\\ \bar\sigma^\mu & 0\end{pmatrix}$, with $\psi = (\psi_L, \psi_R)$, see Definition [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-3|§C5a.1.3]] The Chiral Basis. *Source: Lecture 7, slide "Explicit Form of Dirac Matrices" · Lecture 8, "Cheat Sheet I" and slide "Dirac Equation in 2-Component Form"*

^nd-def-c5a-1-3

- [ ] Q1 **[def]** Write the four chiral-basis $\gamma$'s in $2\times2$ blocks, and the compact $\sigma^\mu$, $\bar\sigma^\mu$ form.
- [ ] Q2 **[conv]** Which basis do the lecture, PS, the user's notes and Yu use, and which basis does Quantum Mechanics (Sakurai) use? What is $\gamma^0$ in each?
- [ ] Q3 **[conv]** The Lecture 7 slide calls the halves $\xi$, $\eta$; Lecture 8 calls them $\psi_L$, $\psi_R$. Which half is left-handed?
- [ ] Q4 **[why]** Why can no basis make $\gamma^0$ and $\gamma^5$ diagonal at once? What does each choice make visible?

> [!tip]- Hints: route in the notes
> - Technique: K5
> - Definition [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-3|§C5a.1.3]] The Chiral Basis; bases across sources: [[§C5a.5 Chirality and Weyl Spinors#^cau-c5a-5-2|§C5a.5, Caution: Bases and conventions across the sources]]; why each basis is used: [[§C5a.5 Chirality and Weyl Spinors#^rem-c5a-5-5|§C5a.5, Remark: Why each basis is used]], Theorem [[§CB.12 Clifford Algebras꞉ Grading, Basis and the Volume Element#^thm-cb-12-17|§CB.12.17]] γ⁰ and γ⁵ Cannot Be Diagonal in the Same Basis.

### Spinor space

Spinor space is a four-dimensional complex vector space $V$; a Dirac spinor at one point is an element of $V$; the column $\mathbb C^4$ appears only after a basis is chosen, see Definition [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-1|§C5a.1.1]] Spinor Space. *Source: the user's notes Ch. 8 §8.1, §8.3 (what each spinor index labels)*

^nd-def-c5a-1-1

- [ ] Q1 **[def]** Define spinor space and a Dirac spinor.
- [ ] Q2 List the structures added layer by layer (Clifford action, Dirac form, Lorentz action). What does $V$ not have at the first layer?
- [ ] Q3 **[why]** Why is "the upper two components" a basis-dependent notion?
- [ ] Q4 **[why]** Why is spinor space unique up to isomorphism once the Dirac maps are given?

> [!tip]- Hints: route in the notes
> - Technique: K5
> - Definition [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-1|§C5a.1.1]] Spinor Space, [[§C5a.1 Spinor Space and the Clifford Action#^rem-c5a-1-1|§C5a.1, Remark: What this layer contains, and what it does not]]; the layers: [[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation#^rem-c5a-0-5|§C5a.0, Remark: The structure of spinor space, layer by layer]]; uniqueness: Theorem [[§CB.13 Complex Clifford Algebras and Clifford Modules#^thm-cb-13-14|§CB.13.14]] Spinor Space Is Unique up to Isomorphism.

### The spinor generators

$S^{\mu\nu} = \frac i4[\gamma^\mu, \gamma^\nu] = \frac i2(\gamma^\mu\gamma^\nu - g^{\mu\nu}\mathbb 1)$, see Definition [[§CB.14 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-14-16|§CB.14.16]] The Spinor Generators; in the course's (Hermitian) convention $S^{\mu\nu} = D(\mathcal J^{\mu\nu})$ for the Dirac representation, and $\sigma^{\mu\nu} = 2S^{\mu\nu}$. *Source: Lecture 7, slide "The Dirac Representation" · Lecture 8, "Cheat Sheet I"*

^nd-def-cb-14-16

- [ ] Q1 **[def]** Define $S^{\mu\nu}$ in both forms and show the two agree.
- [ ] Q2 **[conv]** The §C1b.1 spin generators are in the real convention. What is the factor between them and the lecture's $S^{\mu\nu}$?
- [ ] Q3 **[conv]** Give the three normalizations of $\sigma^{\mu\nu}$ met in the course (PS, the generators, Problem Set 5).
- [ ] Q4 **[why]** What does the claim "$S^{\mu\nu}$ satisfy the Lorentz algebra" require of the $\gamma$'s, and nothing more?

> [!tip]- Hints: route in the notes
> - Technique: K5
> - Definition [[§CB.14 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-14-16|§CB.14.16]] The Spinor Generators; two meanings of $S^{\mu\nu}$: [[§C3.3 How Fields Transform under the Lorentz Group#^cau-c3-3-2|§C3.3, Caution: Two meanings of S^μν]]; normalizations of σ: [[§C5a.6 The Dirac Conjugate and the Bilinears#^cau-c5a-6-1|§C5a.6, Caution: Three normalizations of σ^μν]]; the algebra from Clifford alone: Theorem [[§CB.14 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-14-18|§CB.14.18]] The Spinor Generators Obey the Lorentz Algebra.

### The Dirac representation

$\Lambda_{1/2}(\omega) = \exp(-\frac i2\omega_{\mu\nu}S^{\mu\nu})$ acting on $\psi \in \mathbb C^4$; a Dirac field transforms as $\psi'(x) = \Lambda_{1/2}\psi(\Lambda^{-1}x)$, see Definition [[§C5a.3 The Lorentz Action on Spinor Space#^def-c5a-3-1|§C5a.3.1]] The Dirac Representation. *Source: Lecture 7, slides "Finite Lorentz Transformations in Dirac Representation", "Transformation of Vector and Spinor Fields" · Lecture 8, "Cheat Sheet II"*

^nd-def-c5a-3-1

- [ ] Q1 **[def]** Write $\Lambda_{1/2}(\omega)$ and the transformation law of a Dirac field.
- [ ] Q2 Which matrix transforms the field's components and which the spacetime coordinate in $\psi \to \Lambda_{1/2}\psi(\Lambda^{-1}x)$?
- [ ] Q3 **[why]** The Dirac spinor and the four-vector both have four components. Why are they different representations?
- [ ] Q4 **[conv]** The Lecture 7 slide previews the four entries as "spin up/down for particle/anti-particle". In what sense is this right, and in what sense wrong in the chiral basis?

> [!tip]- Hints: route in the notes
> - Technique: K16
> - Definition [[§C5a.3 The Lorentz Action on Spinor Space#^def-c5a-3-1|§C5a.3.1]] The Dirac Representation; not the vector representation: Theorem [[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-18-5|§CB.18.5]] The Dirac Representation Is Not the Vector Representation, [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^rem-c5a-4-1|§C5a.4, Remark: One transformation, two matrices]]; the preview: [[§C5a.5 Chirality and Weyl Spinors#^cau-c5a-5-3|§C5a.5, Caution: The upper components are not the particle]].

### Spin matrices of the Dirac representation

$S^i = \frac12\varepsilon^{ijk}S^{jk}$, $\Sigma^i = 2S^i$; in the chiral basis $\Sigma^i = \operatorname{diag}(\sigma^i, \sigma^i)$, see Definition [[§C5a.3 The Lorentz Action on Spinor Space#^def-c5a-3-2|§C5a.3.2]] Spin Matrices of the Dirac Representation. *Source: Lecture 7, slide "Spinors and Rotation" · Lecture 9, slide "Solution of the Dirac Equation: Step 3"*

^nd-def-c5a-3-2

- [ ] Q1 **[def]** Define $\mathbf S$ and $\boldsymbol\Sigma$ from $S^{jk}$, and give them in the chiral basis.
- [ ] Q2 What are the eigenvalues of $S^3$ on $\mathbb C^4$?
- [ ] Q3 **[conv]** The Lecture 9 slide labels $\operatorname{diag}(\sigma^k, \sigma^k)$ the angular momentum. What is it really?
- [ ] Q4 **[why]** Why are these matrices called $\mathbf S$ and not $\mathbf J$ in the vault?

> [!tip]- Hints: route in the notes
> - Technique: K5
> - Definition [[§C5a.3 The Lorentz Action on Spinor Space#^def-c5a-3-2|§C5a.3.2]] Spin Matrices of the Dirac Representation; the slide's factor: [[§C5a.9 Plane-Wave Solutions#^cau-c5a-9-1|§C5a.9, Caution: The slide's "angular momentum" is twice the angular momentum]].

### Weyl matrices and Weyl spinors

$\Lambda_L = e^{-\frac i2\boldsymbol\theta\cdot\boldsymbol\sigma - \frac12\boldsymbol\eta\cdot\boldsymbol\sigma}$, $\Lambda_R = e^{-\frac i2\boldsymbol\theta\cdot\boldsymbol\sigma + \frac12\boldsymbol\eta\cdot\boldsymbol\sigma}$, the matrices of $(\frac12, 0)$ and $(0, \frac12)$; a left-handed (right-handed) Weyl spinor is a column $\psi_L \to \Lambda_L\psi_L$ ($\psi_R \to \Lambda_R\psi_R$), see Definition [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^def-c5a-4-1|§C5a.4.1]] The Weyl Matrices and Definition [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^def-c5a-4-2|§C5a.4.2]] Weyl Spinors. *Source: Lecture 8, slide "Weyl Spinors" · PS eq. (3.37)*

^nd-def-c5a-4-2

- [ ] Q1 **[def]** Write $\Lambda_L$ and $\Lambda_R$ in terms of $\boldsymbol\theta$, $\boldsymbol\eta$, and define left- and right-handed Weyl spinors.
- [ ] Q2 Which part (rotation or boost) is the same in both, and which has the opposite sign?
- [ ] Q3 **[conv]** Which representation, $(\frac12, 0)$ or $(0, \frac12)$, is $\psi_L$, and on which convention for $\mathbf K$ does the answer depend?
- [ ] Q4 **[why]** Why can one consistently set $\psi_R = 0$ as a statement about Lorentz transformations, but not in the massive Dirac equation?

> [!tip]- Hints: route in the notes
> - Technique: K16
> - Definition [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^def-c5a-4-1|§C5a.4.1]] The Weyl Matrices, Definition [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^def-c5a-4-2|§C5a.4.2]] Weyl Spinors; the sign of K: [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^cau-c3-2-2|§C3.2, Caution: Which one is (½, 0) depends on the sign of K]]; kinematics versus mass: [[§C5a.5 Chirality and Weyl Spinors#^rem-c5a-5-2|§C5a.5, Remark: Kinematics allows one handedness, a mass needs both]].

### The Dirac conjugate

$\bar\psi \equiv \psi^\dagger\gamma^0$, a row; not the Hermitian conjugate; basis-free it is the functional $h_D(\psi, \cdot)$ of the Dirac form, and $\psi \mapsto \bar\psi$ is conjugate-linear, see Definition [[§C5a.2 The Dirac Form#^def-c5a-2-1|§C5a.2.1]] The Dirac Conjugate. *Source: Lecture 8, slide "The Dirac Conjugate Spinor"*

^nd-def-c5a-2-1

- [ ] Q1 **[def]** Define $\bar\psi$. Is it a row or a column, linear or conjugate-linear in $\psi$?
- [ ] Q2 What is $(\bar\psi)^\dagger$?
- [ ] Q3 **[why]** Why is $\psi^\dagger$ alone not the right partner for an invariant (which generators spoil it)?
- [ ] Q4 **[why]** Under which changes of basis does the formula $\psi^\dagger\gamma^0$ keep computing the same Dirac form?

> [!tip]- Hints: route in the notes
> - Technique: K7 (conjugating bilinears)
> - Definition [[§C5a.2 The Dirac Form#^def-c5a-2-1|§C5a.2.1]] The Dirac Conjugate; why $\psi^\dagger\psi$ fails: [[§C5a.6 The Dirac Conjugate and the Bilinears#^rem-c5a-6-1|§C5a.6, Remark: Why ψ†ψ is not a scalar]]; changes of basis: Theorem [[§C5a.2 The Dirac Form#^thm-c5a-2-2|§C5a.2.2]] Which Changes of Basis Preserve ψ̄; $\gamma^0$ in two roles: [[§C5a.2 The Dirac Form#^rem-c5a-2-1|§C5a.2, Remark: γ⁰ in two roles]].

### Fermion bilinear

$\bar\psi\,\Gamma\,\chi$ with $\Gamma$ a constant $4\times4$ matrix, usually a string of $\gamma$'s; a number with no spinor index, see Definition [[§C5a.6 The Dirac Conjugate and the Bilinears#^def-c5a-6-1|§C5a.6.1]] Fermion Bilinear. *Source: Lecture 8, slide "Fermion Bilinears"*

^nd-def-c5a-6-1

- [ ] Q1 **[def]** Define a fermion bilinear. Which index structure is left over?
- [ ] Q2 How does a bilinear transform when both fields transform with $\Lambda_{1/2}$ (which sandwich of $\Gamma$)?
- [ ] Q3 **[why]** The Lecture 8 slide lists "$\bar\psi\gamma^\mu\psi$, $\bar\psi\gamma^\mu\psi$" as the scalar and the vector. Which bilinear is the scalar?

> [!tip]- Hints: route in the notes
> - Technique: K7
> - Definition [[§C5a.6 The Dirac Conjugate and the Bilinears#^def-c5a-6-1|§C5a.6.1]] Fermion Bilinear; the transformation: step 1 of [[§C5a.6 The Dirac Conjugate and the Bilinears#^der-c5a-6-2|Derivation §C5a.6.2]].

### The sixteen bilinears

$\mathsf S = \bar\psi\psi$, $\mathsf P = \bar\psi i\gamma^5\psi$, $\mathsf V^\mu = \bar\psi\gamma^\mu\psi$, $\mathsf A^\mu = \bar\psi\gamma^\mu\gamma^5\psi$, $\mathsf T^{\mu\nu} = \bar\psi\sigma^{\mu\nu}\psi$, with $\sigma^{\mu\nu} = \frac i2[\gamma^\mu, \gamma^\nu] = 2S^{\mu\nu}$: $1 + 1 + 4 + 4 + 6 = 16$, see Definition [[§C5a.6 The Dirac Conjugate and the Bilinears#^def-c5a-6-2|§C5a.6.2]] The Sixteen Bilinears. *Source: Lecture 8, slide "Fermion Bilinears" · Lecture 11, slide 19 (names) · PS §3.4*

^nd-def-c5a-6-2

- [ ] Q1 **[def]** List the five standard bilinears with their matrices, and count them.
- [ ] Q2 **[conv]** Give the three normalizations of $\sigma^{\mu\nu}$ (PS, the generators, Problem Set 5). Which identities depend on the choice?
- [ ] Q3 **[conv]** Why does the pseudoscalar carry an explicit $i$?
- [ ] Q4 **[why]** Why do sixteen bilinears suffice (what do their matrices form)?

> [!tip]- Hints: route in the notes
> - Technique: K7
> - Definition [[§C5a.6 The Dirac Conjugate and the Bilinears#^def-c5a-6-2|§C5a.6.2]] The Sixteen Bilinears; normalizations: [[§C5a.6 The Dirac Conjugate and the Bilinears#^cau-c5a-6-1|§C5a.6, Caution: Three normalizations of σ^μν]]; reality and the $i$: Theorem [[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-4|§C5a.6.4]] The Bilinears Are Real; basis of $4\times4$ matrices: Theorem [[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-8|§C5a.11.8]] Every Product of γ's Reduces to the Standard Basis, Theorem [[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-18-14|§CB.18.14]] Cl(1,3) ≅ ΛV as a Representation; the Sixteen Bilinears.

### The matrix γ⁵

$\gamma^5 \equiv i\gamma^0\gamma^1\gamma^2\gamma^3$; the 5 is a label, not a Lorentz index; in the chiral basis $\gamma^5 = \operatorname{diag}(-\mathbb 1, \mathbb 1)$, see Definition [[§CB.12 Clifford Algebras꞉ Grading, Basis and the Volume Element#^def-cb-12-14|§CB.12.14]] The Matrix γ⁵. *Source: Problem Set 5, Problem 5 (statement) · the user's notes Ch. 9 §9.6*

^nd-def-cb-12-14

- [ ] Q1 **[def]** Define $\gamma^5$ and give it in the chiral basis.
- [ ] Q2 **[conv]** Why is "$\gamma_5$" a typo in the course's conventions?
- [ ] Q3 **[conv]** Which $\varepsilon^{0123}$ does the course use, and what is PS's? Which convention-free identity compares them?
- [ ] Q4 **[why]** Why does $\gamma^5$ commute with every $S^{\mu\nu}$ although it anticommutes with every $\gamma^\mu$?

> [!tip]- Hints: route in the notes
> - Technique: K5
> - Definition [[§CB.12 Clifford Algebras꞉ Grading, Basis and the Volume Element#^def-cb-12-14|§CB.12.14]] The Matrix γ⁵; properties: Theorem [[§CB.12 Clifford Algebras꞉ Grading, Basis and the Volume Element#^thm-cb-12-15|§CB.12.15]] Algebraic Properties of γ⁵ (→ PS5.5(a)–(b)); the ε convention: [[§C5a.11 Gamma-Matrix Technology#^cau-c5a-11-1|§C5a.11, Caution: The sign of the ε trace across sources]], [[Larsen PHY 513|register: Levi-Civita]]; commuting with $S^{\mu\nu}$: Theorem [[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-18-4|§CB.18.4]] γ⁵ Commutes with the Spinor Generators and Splits the Dirac Module.

### Chirality projectors

$P_L = \frac12(\mathbb 1 - \gamma^5)$, $P_R = \frac12(\mathbb 1 + \gamma^5)$; $\gamma^5\psi = -\psi$ is left-handed chirality; in the chiral basis $P_L\psi = (\psi_L, 0)$, $P_R\psi = (0, \psi_R)$, see Definition [[§C5a.5 Chirality and Weyl Spinors#^def-c5a-5-1|§C5a.5.1]] Chirality Projectors. *Source: PS §3.4 · the user's notes Ch. 8 §8.2*

^nd-def-c5a-5-1

- [ ] Q1 **[def]** Define $P_L$, $P_R$ and left- and right-handed chirality.
- [ ] Q2 Check $P_L^2 = P_L$ and $P_LP_R = 0$. Which property of $\gamma^5$ is used?
- [ ] Q3 **[conv]** With $\gamma^5 = \operatorname{diag}(-\mathbb 1, \mathbb 1)$, which half does $P_L$ keep?
- [ ] Q4 **[why]** Chirality versus helicity: which is a property of the representation and which of a state?

> [!tip]- Hints: route in the notes
> - Technique: K7 (chirality projectors)
> - Definition [[§C5a.5 Chirality and Weyl Spinors#^def-c5a-5-1|§C5a.5.1]] Chirality Projectors; properties: Theorem [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-2|§C5a.5.2]] Properties of the Chirality Projectors; helicity versus chirality: [[§C5a.7 The Dirac Equation and Its Lagrangian#^rem-c5a-7-6|§C5a.7, Remark: Why "left-handed"]].

### The Dirac equation

$(i\gamma^\mu\partial_\mu - m)\psi(x) = 0$, four coupled first-order linear PDEs, $m$ times the $4\times4$ identity, $\psi$ a Dirac field, see Definition [[§C5a.7 The Dirac Equation and Its Lagrangian#^def-c5a-7-1|§C5a.7.1]] The Dirac Equation. *Source: Lecture 8, slide "Introducing the Dirac Equation"*

^nd-def-c5a-7-1

- [ ] Q1 **[def]** Write the Dirac equation in matrix form and in components.
- [ ] Q2 **[conv]** Write $\gamma^\mu\partial_\mu$ with time and space separated. Where does a minus sign appear, and where not?
- [ ] Q3 What does the "$m$" stand for as a matrix, and which theorem justifies calling it the mass?
- [ ] Q4 **[why]** What does covariance of the equation show, and what does it not show? Why is the explicit $i$ not required by covariance?

> [!tip]- Hints: route in the notes
> - Technique: K5
> - Definition [[§C5a.7 The Dirac Equation and Its Lagrangian#^def-c5a-7-1|§C5a.7.1]] The Dirac Equation; the plus sign: [[§C5a.7 The Dirac Equation and Its Lagrangian#^cau-c5a-7-1|§C5a.7, Caution: γ^μ∂_μ has a plus sign]]; what covariance shows: [[§C5a.7 The Dirac Equation and Its Lagrangian#^rem-c5a-7-1|§C5a.7, Remark: What covariance shows and what it does not]]; the mass: Theorem [[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-8|§C5a.7.8]] Every Dirac Solution Solves the Klein–Gordon Equation.

### Feynman slash

$\slashed a \equiv \gamma^\mu a_\mu = \gamma^0a_0 + \gamma^ia_i$; the Dirac equation is $(i\slashed\partial - m)\psi = 0$; in the chiral basis $\slashed p = \begin{pmatrix}0 & p\cdot\sigma\\ p\cdot\bar\sigma & 0\end{pmatrix}$, see Definition [[§C5a.7 The Dirac Equation and Its Lagrangian#^def-c5a-7-2|§C5a.7.2]] Feynman Slash. *Source: Lecture 9, slide "Completeness for Dirac Spinors: the Result" ("Notation: γ^μp_μ ≡ p̸")*

^nd-def-c5a-7-2

- [ ] Q1 **[def]** Define $\slashed a$ and write $\slashed p$ in the chiral basis.
- [ ] Q2 What is $\slashed a\slashed a$?
- [ ] Q3 **[conv]** Write $\slashed p$ with $p^\mu = (E, \mathbf p)$: which sign does the spatial part get?
- [ ] Q4 **[why]** Why is $\slashed p$ "invariant" only in a restricted sense (what kind of object is it)?

> [!tip]- Hints: route in the notes
> - Technique: K5
> - Definition [[§C5a.7 The Dirac Equation and Its Lagrangian#^def-c5a-7-2|§C5a.7.2]] Feynman Slash; slash algebra: Theorem [[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-1|§C5a.11.1]] Slash Algebra; the restricted sense: Theorem [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-9|§C5a.10.9]] The Spin Sums Are Covariant.

### The free Dirac field and its Lagrangian

$\mathcal L = \bar\psi(i\gamma^\mu\partial_\mu - m)\psi$, with $\psi$ and $\bar\psi$ varied independently; classical commuting components (anticommuting after quantization), $m \ge 0$, see Model [[§C5a.7 The Dirac Equation and Its Lagrangian#^mod-c5a-7-3|§C5a.7.3]] The Free Dirac Field. *Source: Lecture 7, slide "Preview: Invariant Lagrangians" · Lecture 8, slide "The Dirac Lagrangian"*

^nd-mod-c5a-7-3

- [ ] Q1 **[def]** Write the Dirac Lagrangian density and list the model's assumptions.
- [ ] Q2 Which fields are treated as independent in the variation, and why is that legitimate for a complex field?
- [ ] Q3 **[why]** Why does the Lagrangian contain $\bar\psi$ and not $\psi^\dagger$?
- [ ] Q4 **[why]** Is $\mathcal L$ real? If not, why is the action still acceptable?

> [!tip]- Hints: route in the notes
> - Technique: K7
> - Model [[§C5a.7 The Dirac Equation and Its Lagrangian#^mod-c5a-7-3|§C5a.7.3]] The Free Dirac Field; invariance: Theorem [[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-4|§C5a.7.4]] The Dirac Lagrangian Is a Lorentz Scalar; reality: Theorem [[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-7|§C5a.7.7]] The Dirac Lagrangian Is Real up to a Divergence.

### The single-particle Hamiltonian

$H_{\text{s.p.}} = \gamma^0(-i\boldsymbol\gamma\cdot\nabla + m) = -i\boldsymbol\alpha\cdot\nabla + \beta m$, $\boldsymbol\alpha = \gamma^0\boldsymbol\gamma$, $\beta = \gamma^0$, Hermitian; $\mathcal H = \psi^\dagger H_{\text{s.p.}}\psi$, see Definition [[§C5a.7 The Dirac Equation and Its Lagrangian#^def-c5a-7-3|§C5a.7.3]] Single-Particle Hamiltonian. *Source: Lecture 10, slide 16 · the user's notes Ch. 10 §10.5 · PS eqs. (3.84)–(3.85)*

^nd-def-c5a-7-3

- [ ] Q1 **[def]** Define $H_{\text{s.p.}}$ in terms of $\gamma$'s and of $\boldsymbol\alpha$, $\beta$.
- [ ] Q2 Rewrite the Dirac equation as $i\partial_t\psi = H_{\text{s.p.}}\psi$: which matrix do you multiply by?
- [ ] Q3 **[conv]** What do PS, earlier vault drafts and Quantum Mechanics call this operator?
- [ ] Q4 **[why]** Why are $\boldsymbol\alpha$ and $\beta$ Hermitian although $\gamma^i$ is anti-Hermitian?

> [!tip]- Hints: route in the notes
> - Technique: K5
> - Definition [[§C5a.7 The Dirac Equation and Its Lagrangian#^def-c5a-7-3|§C5a.7.3]] Single-Particle Hamiltonian; names: [[§C5a.7 The Dirac Equation and Its Lagrangian#^cau-c5a-7-2|§C5a.7, Caution: Names for the single-particle Hamiltonian]]; Hermiticity: step 5 of [[§C5a.8 Canonical Structure and Noether Currents of the Dirac Field#^der-c5a-8-2|Derivation §C5a.8.2]].

### Weyl fields and the Weyl equations

For $m = 0$, a left-handed Weyl field obeys $i\bar\sigma^\mu\partial_\mu\psi_L = 0$ with $\mathcal L_L = i\psi_L^\dagger\bar\sigma^\mu\partial_\mu\psi_L$; a right-handed one $i\sigma^\mu\partial_\mu\psi_R = 0$, see Model [[§C5a.7 The Dirac Equation and Its Lagrangian#^mod-c5a-7-11|§C5a.7.11]] The Weyl Fields. *Source: Lecture 8, slide "Weyl Equation"*

^nd-mod-c5a-7-11

- [ ] Q1 **[def]** Write the two Weyl equations and Lagrangians.
- [ ] Q2 **[conv]** Which of $\sigma^\mu$, $\bar\sigma^\mu$ goes with $\psi_L$? (Check against the two-component Dirac equation.)
- [ ] Q3 **[why]** Why is it consistent to keep one Weyl field only when $m = 0$, both as representation theory and as dynamics?
- [ ] Q4 **[why]** Why does a Weyl theory have no parity symmetry?

> [!tip]- Hints: route in the notes
> - Technique: K16
> - Model [[§C5a.7 The Dirac Equation and Its Lagrangian#^mod-c5a-7-11|§C5a.7.11]] The Weyl Fields; the two-component Dirac equation: Theorem [[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-10|§C5a.7.10]] The Dirac Equation in Two-Component Form; parity: Theorem [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-17-13|§CB.17.13]] The Parity Automorphism Exchanges the Two Copies; when the description is useful: [[§C5a.7 The Dirac Equation and Its Lagrangian#^rem-c5a-7-7|§C5a.7, Remark: When the Weyl description is useful]].

### Positive- and negative-frequency solutions

$\psi = u(p)e^{-ip\cdot x}$ (positive frequency) and $\psi = v(p)e^{+ip\cdot x}$ (negative frequency), always with $p^0 = +E_{\mathbf p}$; "negative" refers to the sign in the exponent, see Definition [[§C5a.9 Plane-Wave Solutions#^def-c5a-9-1|§C5a.9.1]] Positive- and Negative-Frequency Solutions. *Source: Lecture 9, slides "Solution of the Dirac Equation: Step 2" ("Convention: always p⁰ = +√(p²+m²)"), "Negative Frequency Solutions I"*

^nd-def-c5a-9-1

- [ ] Q1 **[def]** Define the two kinds of plane-wave solution, with the convention for $p^0$.
- [ ] Q2 **[why]** Why put the sign in the exponent rather than in $p^0$? What would double-count?
- [ ] Q3 Write $e^{+ip\cdot x}$ with time and space separated. Which way does the spatial phase run?

> [!tip]- Hints: route in the notes
> - Technique: K9 (mode substitution)
> - Definition [[§C5a.9 Plane-Wave Solutions#^def-c5a-9-1|§C5a.9.1]] Positive- and Negative-Frequency Solutions; [[§C5a.9 Plane-Wave Solutions#^rem-c5a-9-1|§C5a.9, Remark: Why the sign sits in the exponent, not in p⁰]].

### The matrices p·σ and p·σ̄

$p\cdot\sigma = E_{\mathbf p} - \mathbf p\cdot\boldsymbol\sigma$, $p\cdot\bar\sigma = E_{\mathbf p} + \mathbf p\cdot\boldsymbol\sigma$, Hermitian, with eigenvalues $E_{\mathbf p} \mp \lvert\mathbf p\rvert$ and $E_{\mathbf p} \pm \lvert\mathbf p\rvert$ on the helicity eigenvectors, see Definition [[§C5a.9 Plane-Wave Solutions#^def-c5a-9-2|§C5a.9.2]] The Matrices p·σ and p·σ̄. *Source: Lecture 9, slides "Interpretation of Rapidity", "Practical Manipulations"*

^nd-def-c5a-9-2

- [ ] Q1 **[def]** Define $p\cdot\sigma$, $p\cdot\bar\sigma$ and write $\slashed p$ with them.
- [ ] Q2 What are their eigenvalues and eigenvectors?
- [ ] Q3 **[conv]** Problem Set 5 writes $\sqrt{\sigma\cdot p}$ and also $\sqrt{E - \boldsymbol\sigma\cdot\mathbf p}$: which three-vector product is meant by $\boldsymbol\sigma\cdot\mathbf p$ versus the four-vector contraction $p\cdot\sigma$?
- [ ] Q4 **[why]** Why are both matrices positive semidefinite on shell?

> [!tip]- Hints: route in the notes
> - Technique: K1 (invariants in a convenient frame)
> - Definition [[§C5a.9 Plane-Wave Solutions#^def-c5a-9-2|§C5a.9.2]] The Matrices p·σ and p·σ̄; the two products: Example [[§C5a.9 Plane-Wave Solutions#^ex-c5a-9-1|§C5a.9.1]] The Plane-Wave Spinors in the Dirac Basis; positivity: Definition [[§C5a.9 Plane-Wave Solutions#^def-c5a-9-5|§C5a.9.5]] The Square Roots √(p·σ) and √(p·σ̄).

### Spin basis

An orthonormal basis $\xi^s$ of $\mathbb C^2$ ($\xi^{r\dagger}\xi^s = \delta^{rs}$, $\sum_s\xi^s\xi^{s\dagger} = \mathbb 1_2$), likewise $\eta^s$; standard choice spin along $\pm z$; from Lecture 12 on $\eta^s = \xi^{-s} = -i\sigma^2(\xi^s)^\ast$, see Definition [[§C5a.9 Plane-Wave Solutions#^def-c5a-9-3|§C5a.9.3]] Spin Basis. *Source: Lecture 9, slides "Solution of the Dirac Equation: Step 3", "Summary I–II" · Lecture 12 (the choice of $\eta^s$)*

^nd-def-c5a-9-3

- [ ] Q1 **[def]** Define a spin basis by its two properties.
- [ ] Q2 **[conv]** Which $\eta^s$ do the Lecture 9 summary slides use, and which choice is fixed from Lecture 12 on? Write $\eta^1$, $\eta^2$ for the latter.
- [ ] Q3 **[conv]** The letter $\eta$ means three things in the course. Which?
- [ ] Q4 **[why]** Which results of the normalization and spin-sum section use only orthonormality and completeness?

> [!tip]- Hints: route in the notes
> - Technique: K10 (orthogonality of u, v)
> - Definition [[§C5a.9 Plane-Wave Solutions#^def-c5a-9-3|§C5a.9.3]] Spin Basis; η: [[§C5a.9 Plane-Wave Solutions#^cau-c5a-9-2|§C5a.9, Caution: η means two things]], [[Larsen PHY 513|register: Flipped labels]]; the L12 choice: Definition [[§C9.5 Charge Conjugation on Oscillators and Spinors#^def-c9-5-5|§C9.5.5]] The Antiparticle Two-Spinors η^s = ξ^{−s}.

### Normalization of the spinors

$u^s$, $v^s$ are normalized by orthonormal $\xi^s$, $\eta^s$ and the factor $\sqrt m$ at rest; equivalently $\bar u^ru^s = 2m\delta^{rs}$ (invariant) or $u^{r\dagger}u^s = 2E_{\mathbf p}\delta^{rs}$, see Definition [[§C5a.9 Plane-Wave Solutions#^def-c5a-9-4|§C5a.9.4]] Normalization of the Spinors. *Source: Lecture 9, slides "Normalization I", "Normalization II" · PS (3.55), (3.57)*

^nd-def-c5a-9-4

- [ ] Q1 **[def]** State the normalization convention in its two equivalent forms.
- [ ] Q2 **[conv]** Which of the two forms is Lorentz invariant, and which is PS's normalization condition?
- [ ] Q3 **[conv]** Quantum Mechanics (Sakurai) normalizes the free Dirac spinors differently. How?
- [ ] Q4 **[why]** Why does the factor $\sqrt m$ at rest fix both forms at once?

> [!tip]- Hints: route in the notes
> - Technique: K1
> - Definition [[§C5a.9 Plane-Wave Solutions#^def-c5a-9-4|§C5a.9.4]] Normalization of the Spinors; Theorem [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-1|§C5a.10.1]] u†u = 2E, Theorem [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-2|§C5a.10.2]] ūu = 2m; QM comparison: [[§C5a.9 Plane-Wave Solutions#^rem-c5a-9-7|§C5a.9, Remark: What the field theory adds to the free Dirac spinors of Quantum Mechanics]]; [[Larsen PHY 513|register: Spinor normalization]].

### The square roots √(p·σ) and √(p·σ̄)

The unique positive-semidefinite square roots, $\sqrt{p\cdot\sigma} = \sqrt{E - \lvert\mathbf p\rvert}\,\Pi_+ + \sqrt{E + \lvert\mathbf p\rvert}\,\Pi_-$ with $\Pi_\pm$ the projectors onto spin $\pm\frac12$ along $\hat{\mathbf p}$ (and $\sqrt{p\cdot\bar\sigma}$ with the roots exchanged); both Hermitian, see Definition [[§C5a.9 Plane-Wave Solutions#^def-c5a-9-5|§C5a.9.5]] The Square Roots √(p·σ) and √(p·σ̄). *Source: Lecture 9, slide "General Solution to Dirac Equation" · PS (3.50)*

^nd-def-c5a-9-5

- [ ] Q1 **[def]** Define $\sqrt{p\cdot\sigma}$ by diagonalization; what are the projectors $\Pi_\pm$?
- [ ] Q2 What are both roots at $\mathbf p = 0$?
- [ ] Q3 **[why]** Why is the square root unique only once positivity is required?
- [ ] Q4 **[why]** Why are the roots Hermitian, and where is this used (the Dirac conjugate of $u$)?

> [!tip]- Hints: route in the notes
> - Technique: K4 (projectors)
> - Definition [[§C5a.9 Plane-Wave Solutions#^def-c5a-9-5|§C5a.9.5]] The Square Roots √(p·σ) and √(p·σ̄); explicit form: Theorem [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-6|§C5a.9.6]] Explicit Square Roots; Hermitian roots in $\bar u$: step 1 of [[§C5a.9 Plane-Wave Solutions#^der-c5a-9-10|Derivation §C5a.9.10]].

### Helicity of a Dirac spinor

For $\mathbf p \ne 0$, $h = \hat{\mathbf p}\cdot\mathbf S = \frac12\operatorname{diag}(\hat{\mathbf p}\cdot\boldsymbol\sigma, \hat{\mathbf p}\cdot\boldsymbol\sigma)$; $h = +\frac12$ is called right-handed, $-\frac12$ left-handed, see Definition [[§C5a.10 Normalization, Spin Sums and Helicity#^def-c5a-10-1|§C5a.10.1]] Helicity of a Dirac Spinor. *Source: Problem Set 5, Problem 6 (statement) · the user's notes Ch. 9 §9.4*

^nd-def-c5a-10-1

- [ ] Q1 **[def]** Define the helicity operator on Dirac spinors.
- [ ] Q2 **[conv]** Both helicity and chirality use the words "left-handed" and "right-handed". Which operator defines each?
- [ ] Q3 **[why]** Why is helicity frame-dependent for a massive particle but not for a massless one?

> [!tip]- Hints: route in the notes
> - Technique: K1
> - Definition [[§C5a.10 Normalization, Spin Sums and Helicity#^def-c5a-10-1|§C5a.10.1]] Helicity of a Dirac Spinor; frame dependence: [[§C5a.10 Normalization, Spin Sums and Helicity#^rem-c5a-10-3|§C5a.10, Remark: The helicity of a massive particle depends on the frame]]; helicity becomes chirality: Theorem [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-14|§C5a.10.14]] The Massless and High-Energy Limit: Helicity Becomes Chirality.

### Helicity two-spinors

$\xi_\pm(\hat{\mathbf p})$: normalized eigenvectors of $\hat{\mathbf p}\cdot\boldsymbol\sigma$ with eigenvalues $\pm1$, each fixed up to a phase, see Definition [[§C5a.10 Normalization, Spin Sums and Helicity#^def-c5a-10-2|§C5a.10.2]] Helicity Two-Spinors. → their explicit form is drilled as [[PHY 513 PS Drill#^ps5-6|PS5.6]].

^nd-def-c5a-10-2

- [ ] Q1 **[def]** Define $\xi_\pm(\hat{\mathbf p})$.
- [ ] Q2 **[why]** Why can no phase convention make $\xi_\pm$ continuous on the whole sphere of directions?
- [ ] Q3 **[why]** Why do the square roots act as numbers on $\xi_\pm$?

> [!tip]- Hints: route in the notes
> - Technique: K4 (projectors)
> - Definition [[§C5a.10 Normalization, Spin Sums and Helicity#^def-c5a-10-2|§C5a.10.2]] Helicity Two-Spinors; [[§C5a.10 Normalization, Spin Sums and Helicity#^cau-c5a-10-2|§C5a.10, Caution: No phase convention is smooth on the whole sphere]]; numbers: step 2 of [[§C5a.10 Normalization, Spin Sums and Helicity#^der-c5a-10-12|Derivation §C5a.10.12]].

### Three different transformations of a spinor

A change of basis of $V$ ($\psi' = U\psi$, $\gamma' = U\gamma U^{-1}$, same point), a Lorentz transformation of a classical field ($\psi'(x) = \Lambda_{1/2}\psi(\Lambda^{-1}x)$, $\gamma$ unchanged) and a Lorentz transformation of the quantum field ($U(\Lambda)^{-1}\hat\psi(x)U(\Lambda) = \Lambda_{1/2}\hat\psi(\Lambda^{-1}x)$, $U$ unitary on the Hilbert space) are unrelated operations, see [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^cau-c5a-4-1|§C5a.4, Caution: Three different transformations]]. *Source: the user's notes Ch. 8 §8.3 · Problem Set 6, Problem 3 (change of basis)*

^nd-cau-c5a-4-1

- [ ] Q1 **[def]** For each of the three operations say what changes, which group acts, and how $\psi$ and $\gamma^\mu$ change.
- [ ] Q2 **[why]** Why is $\gamma^\mu$ unchanged under a Lorentz transformation but changed under a change of basis?
- [ ] Q3 **[why]** Which of the three must be unitary, and which may not be?
- [ ] Q4 **[conv]** In $U(\Lambda)^{-1}\hat\psi U(\Lambda) = \Lambda_{1/2}\hat\psi(\Lambda^{-1}x)$, which objects are operators on the Hilbert space and which are $4\times4$ matrices?

> [!tip]- Hints: route in the notes
> - Technique: K14
> - [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^cau-c5a-4-1|§C5a.4, Caution: Three different transformations]]; γ fixed versus changed: [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^rem-c5a-4-3|§C5a.4, Remark: Why γ is fixed under a Lorentz transformation but not under a change of basis]]; components, not states: [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^cau-c3-2-3|§C3.2, Caution: Components, not states]].

## Derivations T8

### Squaring a first-order equation: why the Clifford relation ★★

For constant $n\times n$ matrices $\gamma^\mu$ and $m \ge 0$, equivalent: (1) $(-i\gamma^\nu\partial_\nu - m)(i\gamma^\mu\partial_\mu - m) = \partial^2 + m^2$ on every $C^2$ function; (2) $(p_\mu\gamma^\mu)^2 = p^2\mathbb 1$ for every $p$; (3) $\{\gamma^\mu, \gamma^\nu\} = 2g^{\mu\nu}\mathbb 1$. The condition does not involve $m$, see Theorem [[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation#^thm-c5a-0-1|§C5a.0.1]] Squaring a First-Order Equation. *Source: Lecture 8, slide "Klein-Gordon Equation from Dirac Equation" · Lecture 9, slide "Solution of the Dirac Equation: Step 2" ($(\gamma^\mu p_\mu)^2 = p^2$) · the user's notes Ch. 8 §8.1 ("Square to ±1, or square root?")*

^nd-thm-c5a-0-1

- [ ] Q1 **[state]** State the three equivalent conditions and say what Dirac was looking for.
- [ ] Q2 Expand the product of the two first-order operators into four terms. Which terms cancel, and which survive?
- [ ] Q3 Why can $\gamma^\nu\gamma^\mu\partial_\nu\partial_\mu$ be replaced by $\frac12\{\gamma^\nu, \gamma^\mu\}\partial_\nu\partial_\mu$ (which property of $C^2$ functions)?
- [ ] Q4 For (1) ⇒ (2), which test functions do you apply the identity to?
- [ ] Q5 For (2) ⇒ (3), how does "polarization" recover the anticommutator from the squares $(p\cdot\gamma)^2$?
- [ ] Q6 **[why]** Why does the "wrong-sign" factor $(-i\slashed\partial - m)$ appear, and why is the mass irrelevant to the condition?

> [!tip]- Hints: route in the notes
> - Technique: K5 (γ-matrix algebra)
> - Steps 1–3 of [[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation#^der-c5a-0-1|Derivation §C5a.0.1]] (expand, symmetrize, (3) ⇒ (1)), step 4 (plane waves), step 5 (polarization), step 6 (components).
> - The algebra of square roots of $p^2$: [[§C5a.1 Spinor Space and the Clifford Action#^rem-c5a-1-2|§C5a.1, Remark: A square root of p²]], [[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation#^rem-c5a-0-2|§C5a.0, ★ Remark: What the Clifford relation induces]].

### The coefficients cannot commute ★

Dirac matrices are invertible and no two of them commute, so they cannot be numbers, and no basis makes all four diagonal, see Theorem [[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation#^thm-c5a-0-2|§C5a.0.2]] The Coefficients Cannot Commute. *Source: the user's notes Ch. 8 §8.1 · Lecture 8 transcript ("Linear is good, four coupled equations bad")*

^nd-thm-c5a-0-2

- [ ] Q1 **[state]** State the theorem.
- [ ] Q2 What is the inverse of $\gamma^\mu$ in terms of $\gamma^\mu$ itself?
- [ ] Q3 If $\gamma^\mu\gamma^\nu = \gamma^\nu\gamma^\mu$ for some $\mu \ne \nu$, combine with the anticommutator: what follows, and why is it impossible?
- [ ] Q4 **[why]** Why does this exclude a one-component field with a first-order equation squaring to Klein–Gordon?

> [!tip]- Hints: route in the notes
> - Technique: K5
> - Step 1 of [[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation#^der-c5a-0-2|Derivation §C5a.0.2]], resting on Theorem [[§CB.11 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^thm-cb-11-16|§CB.11.16]] Clifford Generators Are Invertible and Pairwise Non-Commuting (parts 1–3).

### The smallest Dirac matrices are 4×4 ★

Complex $n\times n$ Dirac matrices have $n$ even and $n \ge 4$, and $n = 4$ occurs (the chiral basis), see Theorem [[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation#^thm-c5a-0-3|§C5a.0.3]] The Smallest Coefficients Are 4×4 Matrices. *Source: the user's notes Ch. 8 §8.1 · Lecture 7 transcript ("four four-by-four matrices")*

^nd-thm-c5a-0-3

- [ ] Q1 **[state]** State the theorem.
- [ ] Q2 Why is each $\gamma^\mu$ traceless? (Use invertibility of another $\gamma$ and cyclicity.)
- [ ] Q3 What are the eigenvalues of $\gamma^0$ and of $\gamma^i$, and why does tracelessness force $n$ even?
- [ ] Q4 **[why]** Why is $n = 2$ impossible (how many mutually anticommuting $2\times2$ matrices exist, and what is missing)?

> [!tip]- Hints: route in the notes
> - Technique: K5
> - Step 1 of [[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation#^der-c5a-0-3|Derivation §C5a.0.3]]; parts 1–2 of Theorem [[§CB.13 Complex Clifford Algebras and Clifford Modules#^thm-cb-13-9|§CB.13.9]] Dirac Matrices Have Even Size, at Least Four.

### Two components suffice only without mass ★

The Weyl equation $i\bar\sigma^\mu\partial_\mu\psi_L = 0$ implies $\partial^2\psi_L = 0$; the massive pair $i\bar\sigma^\mu\partial_\mu\psi_L = m\psi_R$, $i\sigma^\mu\partial_\mu\psi_R = m\psi_L$ implies Klein–Gordon for both; no first-order equation for a single massive two-component field squares to Klein–Gordon, see Theorem [[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation#^thm-c5a-0-4|§C5a.0.4]] Two Components Suffice Only without Mass. *Source: Lecture 7 transcript ("two component spinors is something that is special for exactly massless particles") · Lecture 8, slides "Dirac Equation in 2-Component Form", "Weyl Equation"*

^nd-thm-c5a-0-4

- [ ] Q1 **[state]** State the three parts.
- [ ] Q2 Compute $(i\sigma^\nu\partial_\nu)(i\bar\sigma^\mu\partial_\mu)$ as an operator. Which identity of $\sigma$, $\bar\sigma$ is used?
- [ ] Q3 Apply it to the massive pair: how does the second equation close the first?
- [ ] Q4 For part 3, apply the assumed factorization to plane waves $w\,e^{-ip\cdot x}$ and compare powers of $t$ after $p \to tp$. What does order $t^0$ force, and order $t^1$?
- [ ] Q5 **[why]** Why does part 3 fail only for $m > 0$? What changes for $m = 0$?

> [!tip]- Hints: route in the notes
> - Technique: K5
> - Steps 1–3 of [[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation#^der-c5a-0-4|Derivation §C5a.0.4]]; part 3: steps 4–6; $m = 0$: step 7.
> - Why not two-component spinors: [[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation#^rem-c5a-0-4|§C5a.0, Remark: Why not two-component spinors?]].

### The chiral matrices satisfy the Clifford algebra ★★

$\{\gamma^\mu, \gamma^\nu\} = 2g^{\mu\nu}\mathbb 1_4$ for the chiral matrices, with $\gamma^\mu\gamma^\nu = \operatorname{diag}(\sigma^\mu\bar\sigma^\nu, \bar\sigma^\mu\sigma^\nu)$, see Theorem [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-2|§C5a.1.2]] The Chiral Matrices Satisfy the Clifford Algebra. **[class exercise, Lecture 7]** ("So here I checked some of these anti-commutators. Of course, I should check the rest as well"). *Source: Lecture 7, slide "Explicit Form of Dirac Matrices" ("Sample check of Dirac algebra") and transcript (Sep 23)*

^nd-thm-c5a-1-2

- [ ] Q1 **[state]** State what must be checked: how many anticommutators, and the expected right sides.
- [ ] Q2 Multiply two chiral $\gamma$'s in $2\times2$ blocks. Why is the product block diagonal?
- [ ] Q3 Add the product with $\mu \leftrightarrow \nu$. Which $\sigma$ identity finishes the proof for all pairs at once?
- [ ] Q4 Redo the lecture's sample check $\{\gamma^0, \gamma^i\} = 0$ and the squares $(\gamma^0)^2$, $(\gamma^i)^2$ explicitly.
- [ ] Q5 **[why]** Why is it enough, after this one basis, never to multiply $4\times4$ matrices again?

> [!tip]- Hints: route in the notes
> - Technique: K5
> - Step 1 of [[§C5a.1 Spinor Space and the Clifford Action#^der-c5a-1-2|Derivation §C5a.1.2]] (block product), step 2 (anticommutator via Theorem [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-1|§C5a.1.1]] Identities of σ^μ and σ̄^μ, part 2), step 3 (the lecture's explicit check).
> - Uniqueness up to basis: Theorem [[§CB.13 Complex Clifford Algebras and Clifford Modules#^thm-cb-13-12|§CB.13.12]] Pauli's Fundamental Theorem.

### Identities of σ^μ and σ̄^μ ★

$\operatorname{tr}(\sigma^\mu\bar\sigma^\nu) = 2g^{\mu\nu}$; $\sigma^\mu\bar\sigma^\nu + \sigma^\nu\bar\sigma^\mu = 2g^{\mu\nu}$ (and with bars exchanged), so $X\bar X = x^2$; $\sigma^2(\sigma^\mu)^\ast\sigma^2 = \bar\sigma^\mu$, see Theorem [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-1|§C5a.1.1]] Identities of σ^μ and σ̄^μ. *Source: Lecture 9, slide "Practical Manipulations" ($(p\cdot\sigma)(p\cdot\bar\sigma) = m^2$) · the user's notes Ch. 8*

^nd-thm-c5a-1-1

- [ ] Q1 **[state]** State the three identities.
- [ ] Q2 Check the anticommutator identity case by case ($\mu = \nu = 0$, one index zero, both spatial).
- [ ] Q3 Deduce $X\bar X = x^2\mathbb 1$; which symmetry of $x_\mu x_\nu$ is used?
- [ ] Q4 **[why]** Why does conjugation by $\sigma^2$ flip the sign of $\boldsymbol\sigma^\ast$ (which Pauli matrix is imaginary)?

> [!tip]- Hints: route in the notes
> - Technique: K5
> - Steps 1–4 of [[§C5a.1 Spinor Space and the Clifford Action#^der-c5a-1-1|Derivation §C5a.1.1]].

### The Dirac matrices rotate as a vector

$[\gamma^\mu, S^{\rho\sigma}] = (\mathcal J^{\rho\sigma})^\mu{}_\nu\gamma^\nu$, see Theorem [[§CB.14 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-14-17|§CB.14.17]] The Dirac Matrices Rotate as a Vector. → drilled as [[PHY 513 PS Drill#^ps4-5-b|PS4.5(b)]] (also Lecture 8, slide "'Transformation' of γ^μ: Derivation", "Compute (using Dirac algebra)").

^nd-thm-cb-14-17

### The spinor generators obey the Lorentz algebra

$[S^{\mu\nu}, S^{\rho\sigma}]$ = the Lorentz algebra with $\mathcal J \to S$, see Theorem [[§CB.14 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-14-18|§CB.14.18]] The Spinor Generators Obey the Lorentz Algebra. → drilled as [[PHY 513 PS Drill#^ps4-5-c|PS4.5(c)]] (Lecture 7, slide "The Dirac Representation": "Claim: S^μν satisfy Lorentz algebra"; transcript: "I have absolutely not shown that").

^nd-thm-cb-14-18

### The generators in the chiral basis ★★

$S^{ij} = \frac12\varepsilon^{ijk}\operatorname{diag}(\sigma^k, \sigma^k)$, $S^{0i} = -\frac i2\operatorname{diag}(\sigma^i, -\sigma^i)$: all block diagonal, $\mathbf J = \frac12\boldsymbol\Sigma$, $\mathbf K = -\frac i2\operatorname{diag}(\boldsymbol\sigma, -\boldsymbol\sigma)$, see Theorem [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-1|§C5a.3.1]] The Generators in the Chiral Basis. **[class exercise, Lecture 7]** ($S^{ij}$: "you could compute … that takes a little bit more work because you need to multiply"). *Source: Lecture 7, slide "Explicit Form of Dirac Matrices" and transcript · Lecture 8, "Cheat Sheet I"*

^nd-thm-c5a-3-1

- [ ] Q1 **[state]** Give $S^{ij}$ and $S^{0i}$ in the chiral basis.
- [ ] Q2 Write $S^{\mu\nu} = \frac i4[\gamma^\mu, \gamma^\nu]$ in blocks using the block product of two chiral $\gamma$'s.
- [ ] Q3 For $S^{0i}$: compute $\sigma^0\bar\sigma^i - \sigma^i\bar\sigma^0$ and $\bar\sigma^0\sigma^i - \bar\sigma^i\sigma^0$. Where does the relative sign between the blocks come from?
- [ ] Q4 For $S^{ij}$: use $\sigma^i\sigma^j = \delta^{ij} + i\varepsilon^{ijk}\sigma^k$. Which term survives the commutator?
- [ ] Q5 **[why]** Why does block diagonality of all six generators make the Dirac representation reducible, and why do the halves still mix through the equation of motion?

> [!tip]- Hints: route in the notes
> - Technique: K5
> - Step 1 of [[§C5a.3 The Lorentz Action on Spinor Space#^der-c5a-3-1|Derivation §C5a.3.1]] (block form), step 2 (rotations), step 3 (boosts), step 4 ($\mathbf J$, $\mathbf K$); all six as matrices: Example [[§C5a.3 The Lorentz Action on Spinor Space#^ex-c5a-3-1|§C5a.3.1]] The Six Spinor Generators as 4×4 Matrices.
> - The factor ½ and half angles: [[§C5a.3 The Lorentz Action on Spinor Space#^rem-c5a-3-1|§C5a.3, Remark: Why half the angle]].

### The Dirac representation is (½, 0) ⊕ (0, ½) ★★

In the chiral basis $\mathbf J_+ = \frac12\operatorname{diag}(\boldsymbol\sigma, 0)$, $\mathbf J_- = \frac12\operatorname{diag}(0, \boldsymbol\sigma)$: the upper half is $(\frac12, 0)$, the lower $(0, \frac12)$; a spinor representation ($2\pi$ gives $-1$), see Theorem [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-2|§C5a.3.2]] The Dirac Representation Is (½, 0) ⊕ (0, ½). *Source: Lecture 7, slide "Spinors and Boosts" ("4 dim. Dirac spinor representation is reducible") · Lecture 8, slide "Weyl Spinors"*

^nd-thm-c5a-3-2

- [ ] Q1 **[state]** State the decomposition and which half carries which label.
- [ ] Q2 Form $\mathbf J_\pm = \frac12(\mathbf J \pm i\mathbf K)$ from the chiral generators. What are they on each block?
- [ ] Q3 Identify each block with a model $(j_+, j_-)$. Which definition do you compare with?
- [ ] Q4 **[why]** Compute the $2\pi$ rotation on each block. Why is the Dirac representation spinorial?
- [ ] Q5 **[conv]** Lecture 7 calls the halves $\xi$ (particle) and $\eta$ (antiparticle). What do the halves really carry?

> [!tip]- Hints: route in the notes
> - Technique: K16 (identifying a representation)
> - Steps 1–3 of [[§C5a.3 The Lorentz Action on Spinor Space#^der-c5a-3-2|Derivation §C5a.3.2]]; basis-free: Theorem [[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-18-3|§CB.18.3]] The Dirac Module Restricted to SL(2,ℂ) Is (½, 0) ⊕ (0, ½); the preview's caution: [[§C5a.5 Chirality and Weyl Spinors#^cau-c5a-5-3|§C5a.5, Caution: The upper components are not the particle]].

### The spinor Lorentz matrices are pairs of Weyl matrices ★★

In the chiral basis $\Lambda_{1/2}(\omega) = \operatorname{diag}(\Lambda_L(\omega), \Lambda_R(\omega)) = \operatorname{diag}(e^{-\frac i2\boldsymbol\theta\cdot\boldsymbol\sigma - \frac12\boldsymbol\eta\cdot\boldsymbol\sigma}, e^{-\frac i2\boldsymbol\theta\cdot\boldsymbol\sigma + \frac12\boldsymbol\eta\cdot\boldsymbol\sigma})$, and $\lambda \mapsto \operatorname{diag}(\lambda, (\lambda^\dagger)^{-1})$ is a representation of $SL(2, \mathbb C)$, see Theorem [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-3|§C5a.4.3]] The Spinor Lorentz Matrices Are Pairs of Weyl Matrices. *Source: Lecture 8, slide "Weyl Spinors" (the two-component laws) · PS (3.37)*

^nd-thm-c5a-4-3

- [ ] Q1 **[state]** Write $\Lambda_{1/2}$ in the chiral basis in terms of $\boldsymbol\theta$, $\boldsymbol\eta$.
- [ ] Q2 Rewrite the exponent $-\frac i2\omega_{\mu\nu}S^{\mu\nu}$ with $\mathbf J$, $\mathbf K$ and insert the chiral generators.
- [ ] Q3 Why is the exponential of a block-diagonal matrix block diagonal with the exponentials of the blocks?
- [ ] Q4 Work out a rotation about $z$ and a boost along $x$ explicitly. Which functions of half the angle or rapidity appear?
- [ ] Q5 **[why]** Why is $\Lambda_R = (\Lambda_L^\dagger)^{-1}$, and why is the pair a representation of $SL(2, \mathbb C)$ but only a two-valued one of $SO^+(1,3)$?

> [!tip]- Hints: route in the notes
> - Technique: K4 (exponentiating a generator)
> - Step 1 of [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^der-c5a-4-3|Derivation §C5a.4.3]] (exponent), step 2 (blocks), steps 4–5 (examples), step 3 ($SL(2, \mathbb C)$); $\Lambda_R = (\Lambda_L^\dagger)^{-1}$: step 2 of [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^der-c5a-4-1|Derivation §C5a.4.1]].

### The Weyl matrices lie in SL(2, C) ★

$\det\Lambda_L = \det\Lambda_R = 1$; $\Lambda_R = (\Lambda_L^\dagger)^{-1}$; $\Lambda_L^\ast = \sigma^2\Lambda_R\sigma^2$; rotations give $\Lambda_L = \Lambda_R \in SU(2)$, pure boosts Hermitian positive, not unitary, see Theorem [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-1|§C5a.4.1]] The Weyl Matrices Lie in SL(2, C). *Source: the user's notes Ch. 8 §8.2 · Yu Exercise 3.7*

^nd-thm-c5a-4-1

- [ ] Q1 **[state]** State the four properties.
- [ ] Q2 Why is the determinant $1$ (which formula, and what is the trace of the exponent)?
- [ ] Q3 Take the adjoint of $\Lambda_L$ term by term. Which sign flips, and what does that give for $(\Lambda_L^\dagger)^{-1}$?
- [ ] Q4 **[why]** Why are pure boosts Hermitian and not unitary, while rotations are unitary?

> [!tip]- Hints: route in the notes
> - Technique: K4
> - Steps 1–4 of [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^der-c5a-4-1|Derivation §C5a.4.1]].

### The Weyl matrices cover the vector representation ★

$\Lambda_L(\omega)(x_\mu\sigma^\mu)\Lambda_L(\omega)^\dagger = (\Lambda x)_\mu\sigma^\mu$ with $\Lambda = e^\omega$ of the same parameters, equivalently $\Lambda_L^\dagger\bar\sigma^\mu\Lambda_L = \Lambda^\mu{}_\nu\bar\sigma^\nu$; $SL(2, \mathbb C) \to SO^+(1,3)$ is onto with kernel $\pm\mathbb 1$, see Theorem [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-2|§C5a.4.2]] The Weyl Matrices Cover the Vector Representation and Theorem [[§CB.16 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-16-9|§CB.16.9]] SL(2, C) Is the Double Cover of SO⁺(1,3). *Source: the user's notes Ch. 8 §8.2 · Yu Exercise 3.7*

^nd-thm-c5a-4-2

- [ ] Q1 **[state]** State the covering relation, and what "double cover" means here.
- [ ] Q2 Infinitesimally, compare $A_LX + XA_L^\dagger$ with the vector action $\omega x$ written as a matrix. Why do they agree?
- [ ] Q3 Why does the infinitesimal statement exponentiate (left and right multiplication commute)?
- [ ] Q4 Why is the kernel of $\lambda \mapsto \Lambda(\lambda)$ exactly $\pm\mathbb 1$?
- [ ] Q5 **[why]** Follow the lift of a $2\pi$ rotation from $\mathbb 1$: where does it end, and what does this say about the sign of a spinor?

> [!tip]- Hints: route in the notes
> - Technique: K4, K2
> - Steps 1–3 of [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^der-c5a-4-2|Derivation §C5a.4.2]]; the kernel: Steps 1–4 of [[§CB.16 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^der-cb-16-5|Derivation §CB.16.5]]; the lift: step 4 of [[§CB.16 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^der-cb-16-9|Derivation §CB.16.9]].

### Rotation and boost matrices in the Dirac representation; invariant components; 2π

The rotation matrices entry by entry (Theorem [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-4|§C5a.4.4]] The Rotation Matrices in the Dirac Representation, Entry by Entry, Example [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^ex-c5a-4-1|§C5a.4.1]] One Rotation, Two Matrices) → drilled as [[PHY 513 PS Drill#^ps6-4-c|PS6.4(c)]] and [[PHY 513 PS Drill#^ps6-4-d|PS6.4(d)]]; the boost matrices (Theorem [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-5|§C5a.4.5]] The Boost Matrices in the Dirac Representation, Entry by Entry, Example [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^ex-c5a-4-2|§C5a.4.2]] One Boost, Two Matrices) → drilled as [[PHY 513 PS Drill#^ps6-4-a|PS6.4(a)]]; no invariant spinor component under a boost (Theorem [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-6|§C5a.4.6]] A Boost Leaves No Spinor Component Invariant) → drilled as [[PHY 513 PS Drill#^ps6-4-b|PS6.4(b)]].

^nd-thm-c5a-4-4

### The Dirac matrices are an invariant vector of matrices ★★

$\Lambda_{1/2}^{-1}\gamma^\mu\Lambda_{1/2} = \Lambda^\mu{}_\nu\gamma^\nu$ for the same $\omega$ (also $S^{\mu\nu}$ as a tensor), the finite form of $[\gamma^\mu, S^{\rho\sigma}] = (\mathcal J^{\rho\sigma})^\mu{}_\nu\gamma^\nu$, see Theorem [[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-18-7|§CB.18.7]] The Dirac Matrices Are an Invariant Vector of Matrices. **[class exercise, Lecture 8]** ("what we have checked is entirely just this is true to linear order, and the claim is that once it's true to linear order, it's true"). *Source: Lecture 8, slides "'Transformation' of γ^μ: Derivation", "'Transformation' of γ^μ: Interpretation" and transcript (Sep 28)*

^nd-thm-cb-18-7

- [ ] Q1 **[state]** State the finite transformation law of $\gamma^\mu$ under $\Lambda_{1/2}$.
- [ ] Q2 From $[\gamma^\mu, S^{\rho\sigma}]$, compute $[\gamma^\mu, A]$ for $A = -\frac i2\omega_{\rho\sigma}S^{\rho\sigma}$.
- [ ] Q3 Define $F^\mu(t) = e^{-tA}\gamma^\mu e^{tA}$ and $G^\mu(t) = (e^{t\omega})^\mu{}_\nu\gamma^\nu$. Which linear ODE do both satisfy, with which initial value?
- [ ] Q4 Why does uniqueness of solutions give $F = G$ at $t = 1$? (Alternatively: sum the nested-commutator series.)
- [ ] Q5 **[conv]** Lecture 8 writes $\Lambda_{1/2}\gamma^\mu\Lambda_{1/2}^{-1} = (\Lambda^{-1})^\mu{}_\nu\gamma^\nu$. How is it related to the vault's form?
- [ ] Q6 **[why]** "$\gamma^\nu$ are just numbers. They do not transform!" In what sense is that compatible with this law?

> [!tip]- Hints: route in the notes
> - Technique: K4, K11
> - Step 1 of [[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^der-cb-18-7|Derivation §CB.18.7]] (infinitesimal), steps 2–4 (two curves, the same ODE, uniqueness); second route: Steps 1–3 of [[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^der-cb-18-7b|Derivation §CB.18.7, second route]].
> - The lecture's three forms: [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^rem-c5a-4-2|§C5a.4, Remark: The lecture's form of the covariance]]; "numbers": [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^rem-c5a-4-3|§C5a.4, Remark: Why γ is fixed under a Lorentz transformation but not under a change of basis]].

### The Dirac equation is covariant ★★

For $\psi'(x) = \Lambda_{1/2}\psi(\Lambda^{-1}x)$, $(i\gamma^\mu\partial_\mu - m)\psi'(x) = \Lambda_{1/2}[(i\gamma^\nu\partial_\nu - m)\psi](\Lambda^{-1}x)$ with the same $\gamma$ and $m$: $\gamma^\mu\partial_\mu\psi$ transforms like $\psi$, see Theorem [[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-1|§C5a.7.1]] The Dirac Equation Is Covariant. *Source: Lecture 8, slides "Relativistic Invariance of the Dirac Equation", "Transformations with 4-Vectors and 4-Spinors"*

^nd-thm-c5a-7-1

- [ ] Q1 **[state]** State the covariance identity and its consequence for solutions.
- [ ] Q2 Differentiate $\psi'(x)$ by the chain rule. Which matrix multiplies $(\partial_\nu\psi)(\Lambda^{-1}x)$?
- [ ] Q3 Multiply by $\gamma^\mu$ and insert $\mathbb 1 = \Lambda_{1/2}\Lambda_{1/2}^{-1}$. Which transformation law of $\gamma$ do you use?
- [ ] Q4 Contract the vector indices: why do $(\Lambda^{-1})^\nu{}_\mu$ and $\Lambda^\mu{}_\rho$ cancel?
- [ ] Q5 **[why]** Why does the mass term need $m$ to be a Lorentz scalar times $\mathbb 1$?
- [ ] Q6 **[why]** "Three transformations of $\gamma$ cancel three others": which indices of $\gamma^\mu$ are cancelled by $\partial_\mu$, by $\psi$, and which one survives?

> [!tip]- Hints: route in the notes
> - Technique: K2, K14
> - Step 1 of [[§C5a.7 The Dirac Equation and Its Lagrangian#^der-c5a-7-1|Derivation §C5a.7.1]] (chain rule), steps 2–3 (insert, Theorem [[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-18-7|§CB.18.7]] The Dirac Matrices Are an Invariant Vector of Matrices), step 4 (contract), steps 5–6 (mass, combine).
> - Index slots of $\gamma$: [[§C5a.5 Chirality and Weyl Spinors#^rem-c5a-5-4|§C5a.5, Remark: What each Dirac index labels]].

### Adjoints of the spinor generators ★★

In a Hermitian basis $S^{ij\dagger} = S^{ij}$ and $S^{0i\dagger} = -S^{0i}$: $\Lambda_{1/2}$ is unitary for rotations and Hermitian positive for boosts, see Theorem [[§CB.14 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-14-22|§CB.14.22]] Adjoints of the Generators. *Source: Lecture 8, slide "The Hermitean Conjugate Spinor" ("Rotations S^ij hermitean and boosts S^0i antihermitean")*

^nd-thm-cb-14-22

- [ ] Q1 **[state]** State the Hermiticity of $S^{ij}$ and $S^{0i}$ and the consequence for $\Lambda_{1/2}$.
- [ ] Q2 Take the adjoint of $\frac i4[\gamma^\mu, \gamma^\nu]$: what happens to the order and to the factor $i$?
- [ ] Q3 Insert $\gamma^{\mu\dagger} = \gamma^0\gamma^\mu\gamma^0$ and move $\gamma^0$ through $S^{ij}$ and through $S^{0i}$. Which one commutes and which anticommutes with $\gamma^0$?
- [ ] Q4 **[why]** Why does this make $\psi^\dagger\psi$ invariant under rotations but not under boosts?

> [!tip]- Hints: route in the notes
> - Technique: K5
> - Steps 1–3 of [[§CB.14 The Spin Group and the Double Cover Spin(V) → SO(V)#^der-cb-14-22|Derivation §CB.14.22]], step 4 (rotations unitary, boosts not).

### Λ½ is pseudo-unitary: γ⁰ compensates ★★

$\Lambda_{1/2}^\dagger\gamma^0 = \gamma^0\Lambda_{1/2}^{-1}$, equivalently $\Lambda_{1/2}^\dagger\gamma^0\Lambda_{1/2} = \gamma^0$: $\gamma^0$ is an indefinite Hermitian form preserved by every $\Lambda_{1/2}$, see Theorem [[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-18-13|§CB.18.13]] Λ½ Is Pseudo-Unitary. *Source: Lecture 8, slide "The Dirac Conjugate Spinor" ("γ⁰ can compensate for anti-hermiticity of boosts")*

^nd-thm-cb-18-13

- [ ] Q1 **[state]** State the identity in its three equivalent forms.
- [ ] Q2 Show $\gamma^0$ commutes with $S^{ij}$ and anticommutes with $S^{0i}$ by counting anticommutations.
- [ ] Q3 Combine with the Hermiticity pattern to get $(S^{\mu\nu})^\dagger\gamma^0 = \gamma^0S^{\mu\nu}$ for all $\mu\nu$.
- [ ] Q4 Pass this through the exponential series. Why do the real $\omega_{\mu\nu}$ matter?
- [ ] Q5 **[why]** What are the eigenvalues of $\gamma^0$, and why is the form indefinite? Why is that no problem for a field theory?

> [!tip]- Hints: route in the notes
> - Technique: K5, K7
> - Steps 1–2 of [[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^der-cb-18-13|Derivation §CB.18.13, the lecture's route]] (the lecture's route), step 3, steps 4–6 (exponent, series, other forms), step 7 (indefinite); second route: [[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^der-cb-18-13b|Derivation §CB.18.13, second route]].

### The Dirac conjugate transforms with the inverse ★★

$\bar\psi'(x) = \bar\psi(\Lambda^{-1}x)\Lambda_{1/2}^{-1}$, so $\bar\psi\chi$ is a scalar field; $(\bar\psi)^\dagger = \gamma^0\psi$, see Theorem [[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-1|§C5a.6.1]] The Dirac Conjugate Transforms with the Inverse. *Source: Lecture 8, slide "The Dirac Conjugate Spinor" ("Combination ψ̄ψ = ψ†γ⁰ψ is relativistically invariant")*

^nd-thm-c5a-6-1

- [ ] Q1 **[state]** State how $\bar\psi$ transforms and what follows for $\bar\psi\chi$.
- [ ] Q2 Take the adjoint of the transformed field. Which matrix appears on the right of $\psi^\dagger$?
- [ ] Q3 Multiply by $\gamma^0$ and use pseudo-unitarity. What is left?
- [ ] Q4 **[why]** Why is the pairing $\bar\psi\chi$ evaluated at the same point $\Lambda^{-1}x$ for both fields a scalar field?

> [!tip]- Hints: route in the notes
> - Technique: K7
> - Steps 1–4 of [[§C5a.6 The Dirac Conjugate and the Bilinears#^der-c5a-6-1|Derivation §C5a.6.1]]; pseudo-unitarity: Theorem [[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-18-13|§CB.18.13]] Λ½ Is Pseudo-Unitary.

### Scalar, vector and tensor bilinears ★★

A bilinear transforms as $\Lambda_{1/2}^{-1}\Gamma\Lambda_{1/2}$ does: $\bar\psi\chi$ is a scalar, $\bar\psi\gamma^\mu\chi$ a vector, $\bar\psi[\gamma^\mu, \gamma^\nu]\chi$ an antisymmetric tensor; $n$ $\gamma$'s give an $n$-index tensor, see Theorem [[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-2|§C5a.6.2]] Scalar, Vector and Tensor Bilinears. *Source: Lecture 8, slide "Fermion Bilinears" and transcript ("All the four spinor stuff is gone")*

^nd-thm-c5a-6-2

- [ ] Q1 **[state]** State the transformation of the three bilinears.
- [ ] Q2 Why does every bilinear transform through the sandwich $\Lambda_{1/2}^{-1}\Gamma\Lambda_{1/2}$?
- [ ] Q3 Do the vector case with the transformation law of $\gamma^\mu$.
- [ ] Q4 For two $\gamma$'s, where do you insert $\mathbb 1 = \Lambda_{1/2}\Lambda_{1/2}^{-1}$?
- [ ] Q5 **[why]** Why does $\bar\psi\gamma^\mu\gamma^\nu\psi$ (no commutator) contain a scalar piece as well as the tensor?

> [!tip]- Hints: route in the notes
> - Technique: K7
> - Steps 1–5 of [[§C5a.6 The Dirac Conjugate and the Bilinears#^der-c5a-6-2|Derivation §C5a.6.2]]; the split $\gamma^\mu\gamma^\nu = g^{\mu\nu} + \frac12[\gamma^\mu, \gamma^\nu]$: Theorem [[§CB.11 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^thm-cb-11-12|§CB.11.12]] First Consequences of the Clifford Algebra, part 3.

### Pseudoscalar and axial vector under proper Lorentz transformations ★

$\bar\psi i\gamma^5\psi$ and $\bar\psi\gamma^\mu\gamma^5\psi$ transform like a scalar and a vector under $SO^+(1,3)$; they differ from $\bar\psi\psi$, $\bar\psi\gamma^\mu\psi$ only by a sign under parity, see Theorem [[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-3|§C5a.6.3]] Pseudoscalar and Axial Vector under Proper Lorentz Transformations. *Source: Lecture 11 (parity) · PS §3.4*

^nd-thm-c5a-6-3

- [ ] Q1 **[state]** State the transformation of $\mathsf P$ and $\mathsf A^\mu$ under proper orthochronous $\Lambda$.
- [ ] Q2 Why is $\gamma^5$ invariant under $\Lambda_{1/2}$?
- [ ] Q3 For $\mathsf A^\mu$, insert the identity between $\gamma^\mu$ and $\gamma^5$. What remains?
- [ ] Q4 **[why]** Why does "pseudo" become visible only for improper transformations?

> [!tip]- Hints: route in the notes
> - Technique: K7
> - Steps 1–3 of [[§C5a.6 The Dirac Conjugate and the Bilinears#^der-c5a-6-3|Derivation §C5a.6.3]]; parity: Theorem [[§C9.4 Fermion Bilinears under Parity#^thm-c9-4-4|§C9.4.4]] The Sixteen Bilinears under Parity.

### The bilinears are real ★

For commuting components $(\bar\psi\Gamma\psi)^\ast = \bar\psi\bar\Gamma\psi$ with $\bar\Gamma = \gamma^0\Gamma^\dagger\gamma^0$; the five standard matrices have $\bar\Gamma = \Gamma$, so the standard bilinears are real, while $\bar\psi\gamma^5\psi$ is imaginary, see Theorem [[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-4|§C5a.6.4]] The Bilinears Are Real. *Source: PS §3.4 · the user's notes Ch. 8*

^nd-thm-c5a-6-4

- [ ] Q1 **[state]** State the reality criterion and the list.
- [ ] Q2 Why is the complex conjugate of a bilinear its adjoint, and what is $\bar\Gamma$?
- [ ] Q3 Compute $\bar\Gamma$ for $\gamma^\mu$, $\gamma^\mu\gamma^5$ and $\sigma^{\mu\nu}$.
- [ ] Q4 **[why]** Why does the pseudoscalar need the $i$ to be real?

> [!tip]- Hints: route in the notes
> - Technique: K7
> - Steps 1–3 of [[§C5a.6 The Dirac Conjugate and the Bilinears#^der-c5a-6-4|Derivation §C5a.6.4]]; Hermiticity: Theorem [[§C5a.2 The Dirac Form#^thm-c5a-2-1|§C5a.2.1]] Hermiticity of the Dirac Matrices.

### γ⁵ is Lorentz invariant and separates the Weyl halves ★

$\gamma^5$ commutes with every $S^{\mu\nu}$ and $\Lambda_{1/2}$; in the chiral basis $\gamma^5 = \operatorname{diag}(-\mathbb 1, \mathbb 1)$; on the Dirac representation $\gamma^5 = \frac43(\mathbf J_-^2 - \mathbf J_+^2)$, and its eigenspaces $\mp1$ carry $(\frac12, 0)$, $(0, \frac12)$ in every basis, see Theorem [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-1|§C5a.5.1]] γ⁵ Is Lorentz Invariant and Separates the Weyl Halves and Theorem [[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-18-4|§CB.18.4]] γ⁵ Commutes with the Spinor Generators and Splits the Dirac Module. *Source: the user's notes Ch. 8 §8.2 · PS §3.4*

^nd-thm-c5a-5-1

- [ ] Q1 **[state]** State the three parts.
- [ ] Q2 Compute $\gamma^5$ in the chiral basis from the block products $\gamma^0\gamma^1$ and $\gamma^2\gamma^3$.
- [ ] Q3 Why does $\gamma^5$ commute with $S^{\mu\nu}$ (how many $\gamma$'s does it pass)?
- [ ] Q4 Compute $\mathbf J\cdot\mathbf K$ in the chiral basis and relate it to $\gamma^5$ and to $\mathbf J_\pm^2$.
- [ ] Q5 **[why]** Why are the eigenspaces of $\gamma^5$ the Weyl halves in every basis, not only the chiral one?

> [!tip]- Hints: route in the notes
> - Technique: K5, K16
> - Step 1 of [[§C5a.5 Chirality and Weyl Spinors#^der-c5a-5-1|Derivation §C5a.5.1]] (chiral form), step 2 ($\mathbf J\cdot\mathbf K$), step 3 (eigenspaces); $K_i = i\gamma^5J_i$: Theorem [[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-18-4|§CB.18.4]] γ⁵ Commutes with the Spinor Generators and Splits the Dirac Module, part 1.

### Properties of the chirality projectors ★

$P_{L,R}$ are complementary projectors; $P_L\gamma^\mu = \gamma^\mu P_R$; they commute with $S^{\mu\nu}$ and $\Lambda_{1/2}$; $\overline{P_L\psi} = \bar\psi P_R$, see Theorem [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-2|§C5a.5.2]] Properties of the Chirality Projectors. *Source: the user's notes Ch. 8 · PS §3.4 · Problem Set 6, Problem 5 (chiral transformations)*

^nd-thm-c5a-5-2

- [ ] Q1 **[state]** State the four properties.
- [ ] Q2 Verify the projector relations from $(\gamma^5)^2 = \mathbb 1$.
- [ ] Q3 Pass $P_L$ through $\gamma^\mu$: which property of $\gamma^5$ changes $L$ into $R$?
- [ ] Q4 **[why]** Compute $\overline{P_L\psi}$: why does the bar turn $P_L$ into $P_R$? (Two facts about $\gamma^5$.)

> [!tip]- Hints: route in the notes
> - Technique: K7 (chirality projectors)
> - Steps 1–4 of [[§C5a.5 Chirality and Weyl Spinors#^der-c5a-5-2|Derivation §C5a.5.2]]; $\gamma^5$ properties: Theorem [[§CB.12 Clifford Algebras꞉ Grading, Basis and the Volume Element#^thm-cb-12-15|§CB.12.15]] Algebraic Properties of γ⁵.

### Pauli's theorem; the Dirac basis

Any two sets of $4\times4$ Dirac matrices are related by $\gamma' = U\gamma U^{-1}$ (Theorem [[§CB.13 Complex Clifford Algebras and Clifford Modules#^thm-cb-13-12|§CB.13.12]] Pauli's Fundamental Theorem) → drilled as [[PHY 513 PS Drill#^ps6-3-a|PS6.3(a)]]; the Dirac basis from the chiral one by $U_D$ (Example [[§C5a.5 Chirality and Weyl Spinors#^ex-c5a-5-1|§C5a.5.1]] The Dirac Basis Is Equivalent to the Chiral Basis) → drilled as [[PHY 513 PS Drill#^ps6-3-b|PS6.3(b)]].

^nd-thm-cb-13-12

### The Dirac Lagrangian is a Lorentz scalar ★★

$\mathcal L'(x) = \bar\psi'(i\slashed\partial - m)\psi'(x) = \mathcal L(\Lambda^{-1}x)$, so the action is invariant, see Theorem [[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-4|§C5a.7.4]] The Dirac Lagrangian Is a Lorentz Scalar. *Source: Lecture 8, slide "The Dirac Lagrangian" ("Proof of invariance: (iγ^μ∂_μ − m)ψ transforms like ψ")*

^nd-thm-c5a-7-4

- [ ] Q1 **[state]** State the transformation of $\mathcal L$ and the conclusion for $S$.
- [ ] Q2 How does the right factor $(i\slashed\partial - m)\psi$ transform (which theorem)?
- [ ] Q3 How does the left factor $\bar\psi$ transform?
- [ ] Q4 **[why]** Why does a density with $\mathcal L'(x) = \mathcal L(\Lambda^{-1}x)$ give an invariant action (which Jacobian)?

> [!tip]- Hints: route in the notes
> - Technique: K14
> - Steps 1–4 of [[§C5a.7 The Dirac Equation and Its Lagrangian#^der-c5a-7-4|Derivation §C5a.7.4]]; Theorem [[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-1|§C5a.7.1]] The Dirac Equation Is Covariant, Theorem [[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-1|§C5a.6.1]] The Dirac Conjugate Transforms with the Inverse.

### The field equations of the Dirac Lagrangian ★★

Varying $\bar\psi$ gives $(i\gamma^\mu\partial_\mu - m)\psi = 0$; varying $\psi$ gives $i\partial_\mu\bar\psi\gamma^\mu + m\bar\psi = 0$; each is the Hermitian conjugate of the other (times $\gamma^0$), see Theorem [[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-6|§C5a.7.6]] The Field Equations of the Dirac Lagrangian. **[class exercise, Lecture 8]** ("Yes, we could check that it's invariant, but it really is": the conjugate equation transforms like $\bar\psi$). *Source: Lecture 8, slide "The Dirac Lagrangian" and transcript (Sep 28)*

^nd-thm-c5a-7-6

- [ ] Q1 **[state]** State both field equations and their relation.
- [ ] Q2 Why may $\psi$ and $\bar\psi$ be varied independently (count the real fields)?
- [ ] Q3 Vary $\bar\psi$: why is this the easy direction?
- [ ] Q4 Vary $\psi$: which term needs an integration by parts, and which sign does it bring?
- [ ] Q5 Take the adjoint of the conjugate equation. Why must the product be written $\gamma^0\gamma^\mu$ and not $\gamma^\mu\gamma^0$ before daggering?
- [ ] Q6 **[why]** Show that the left side of the conjugate equation transforms like $\bar\psi$ (the class check): which laws of $\bar\psi$, $\gamma^\mu$ and $\partial_\mu$ combine?

> [!tip]- Hints: route in the notes
> - Technique: K12 (Noether recipe, the Euler–Lagrange part), K7
> - Step 1 of [[§C5a.7 The Dirac Equation and Its Lagrangian#^der-c5a-7-6|Derivation §C5a.7.6]], step 2 (vary ψ̄), steps 3–4 (vary ψ), steps 5–6 (conjugate, simplify the matrices).
> - The order of γ⁰ and γ^μ: [[§C5a.7 The Dirac Equation and Its Lagrangian#^cau-c5a-7-3|§C5a.7, Caution: The order of γ⁰ and γ^μ in the conjugate equation]]; the class check: Theorem [[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-1|§C5a.6.1]] The Dirac Conjugate Transforms with the Inverse with Theorem [[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-18-7|§CB.18.7]] The Dirac Matrices Are an Invariant Vector of Matrices and Theorem [[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-1|§C5a.7.1]] The Dirac Equation Is Covariant.

### Why the i ★★

Without the $i$, the two field equations would be $(\slashed\partial - m)\psi = 0$ and, after conjugation, $\gamma^0(\slashed\partial + m)\psi = 0$, forcing $m\psi = 0$; with the $i$, conjugation supplies the reconciling sign and makes $\mathcal L$ real, see [[§C5a.7 The Dirac Equation and Its Lagrangian#^rem-c5a-7-2|§C5a.7, Remark: Why the i]]. *Source: Lecture 8 transcript ("This is a place where you would see that I needed my i") · the user's notes Ch. 8*

^nd-rem-c5a-7-2

- [ ] Q1 **[state]** What goes wrong if the Lagrangian is written without the $i$?
- [ ] Q2 Derive the two field equations of $\bar\psi(\slashed\partial - m)\psi$.
- [ ] Q3 Conjugate the second one. Which sign comes out different from the first?
- [ ] Q4 **[why]** Which other property of $\mathcal L$ does the $i$ secure?

> [!tip]- Hints: route in the notes
> - Technique: K7
> - [[§C5a.7 The Dirac Equation and Its Lagrangian#^rem-c5a-7-2|§C5a.7, Remark: Why the i]]; steps 5–6 of [[§C5a.7 The Dirac Equation and Its Lagrangian#^der-c5a-7-6|Derivation §C5a.7.6]] without the factor $i$; reality: Theorem [[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-7|§C5a.7.7]] The Dirac Lagrangian Is Real up to a Divergence.

### The Dirac Lagrangian is real up to a divergence ★

$\mathcal L^\ast = \mathcal L - i\partial_\mu(\bar\psi\gamma^\mu\psi)$ off shell; the symmetric density $\frac i2(\bar\psi\gamma^\mu\partial_\mu\psi - \partial_\mu\bar\psi\gamma^\mu\psi) - m\bar\psi\psi$ is real and gives the same equations, see Theorem [[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-7|§C5a.7.7]] The Dirac Lagrangian Is Real up to a Divergence. *Source: the user's notes Ch. 8 · PS §3.2*

^nd-thm-c5a-7-7

- [ ] Q1 **[state]** State the relation between $\mathcal L^\ast$ and $\mathcal L$.
- [ ] Q2 Take the adjoint of the kinetic term $\bar\psi\gamma^\mu\partial_\mu\psi$. Which matrix identity simplifies $\gamma^{\mu\dagger}\gamma^0$?
- [ ] Q3 Use the product rule to bring the derivative back onto $\psi$.
- [ ] Q4 **[why]** Why do $\mathcal L$ and $\mathcal L_{\rm sym}$ give the same field equations?

> [!tip]- Hints: route in the notes
> - Technique: K7
> - Steps 1–5 of [[§C5a.7 The Dirac Equation and Its Lagrangian#^der-c5a-7-7|Derivation §C5a.7.7]], step 6 (symmetric form), step 7 (the action).

### Every Dirac solution solves Klein–Gordon ★★

$(-i\slashed\partial - m)(i\slashed\partial - m) = \partial^2 + m^2$, so each component of a Dirac solution obeys $(\partial^2 + m^2)\psi_a = 0$: $m^2$ is the mass squared; the converse fails, see Theorem [[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-8|§C5a.7.8]] Every Dirac Solution Solves the Klein–Gordon Equation. *Source: Lecture 8, slide "Klein-Gordon Equation from Dirac Equation" and transcript*

^nd-thm-c5a-7-8

- [ ] Q1 **[state]** State the theorem and the operator identity behind it.
- [ ] Q2 Multiply the Dirac equation by the "wrong-sign" operator and expand into four terms.
- [ ] Q3 Symmetrize $\gamma^\nu\gamma^\mu\partial_\nu\partial_\mu$. Which property of $\partial_\nu\partial_\mu$ allows it?
- [ ] Q4 Insert the Clifford relation. Why does each component decouple?
- [ ] Q5 **[why]** Why is the sign of $m$ a convention, and why does Klein–Gordon not imply Dirac (count candidates and solutions)?

> [!tip]- Hints: route in the notes
> - Technique: K5
> - Steps 1–4 of [[§C5a.7 The Dirac Equation and Its Lagrangian#^der-c5a-7-8|Derivation §C5a.7.8]], step 5 (sign of m), step 6 (converse fails).
> - The count: [[§C5a.7 The Dirac Equation and Its Lagrangian#^rem-c5a-7-3|§C5a.7, Remark: Eight candidates, four solutions]].

### The Dirac equation in two-component form ★★

In the chiral basis the Dirac equation is $i\bar\sigma^\mu\partial_\mu\psi_L = m\psi_R$, $i\sigma^\mu\partial_\mu\psi_R = m\psi_L$: kinetic operators act within each Weyl block, only the mass couples them, see Theorem [[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-10|§C5a.7.10]] The Dirac Equation in Two-Component Form. *Source: Lecture 8, slide "Dirac Equation in 2-Component Form" ("Mass-term mixes the two irreducible representations")*

^nd-thm-c5a-7-10

- [ ] Q1 **[state]** Write the two-component equations.
- [ ] Q2 Write $i\slashed\partial - m$ as a $2\times2$ block matrix. Where does the $-m$ sit, and why?
- [ ] Q3 Act on $(\psi_L, \psi_R)$ and read off the two equations.
- [ ] Q4 **[conv]** Which of $\sigma^\mu$, $\bar\sigma^\mu$ multiplies $\psi_L$ in its equation? Check against the Lecture 8 slide.
- [ ] Q5 **[why]** What happens at $m = 0$, and why is the electron of hydrogen nevertheless no Weyl particle?

> [!tip]- Hints: route in the notes
> - Technique: K5
> - Steps 1–3 of [[§C5a.7 The Dirac Equation and Its Lagrangian#^der-c5a-7-10|Derivation §C5a.7.10]]; the Weyl case: Model [[§C5a.7 The Dirac Equation and Its Lagrangian#^mod-c5a-7-11|§C5a.7.11]] The Weyl Fields; when Weyl is useful: [[§C5a.7 The Dirac Equation and Its Lagrangian#^rem-c5a-7-7|§C5a.7, Remark: When the Weyl description is useful]].

### Bilinears in Weyl components ★

$\bar\psi = (\psi_R^\dagger, \psi_L^\dagger)$; $\bar\psi\chi = \psi_R^\dagger\chi_L + \psi_L^\dagger\chi_R$; $\bar\psi\gamma^\mu\chi = \psi_L^\dagger\bar\sigma^\mu\chi_L + \psi_R^\dagger\sigma^\mu\chi_R$; so $\mathcal L = i\psi_L^\dagger\bar\sigma^\mu\partial_\mu\psi_L + i\psi_R^\dagger\sigma^\mu\partial_\mu\psi_R - m(\psi_L^\dagger\psi_R + \psi_R^\dagger\psi_L)$, see Theorem [[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-9|§C5a.7.9]] Bilinears in Weyl Components. *Source: PS §3.2 · the user's notes Ch. 8*

^nd-thm-c5a-7-9

- [ ] Q1 **[state]** Write $\bar\psi$, $\bar\psi\chi$, $\bar\psi\gamma^\mu\chi$ and the Lagrangian in Weyl components.
- [ ] Q2 Why does $\gamma^0$ exchange the halves in $\bar\psi$?
- [ ] Q3 Compute $\gamma^\mu\chi$ in blocks and multiply by $\bar\psi$.
- [ ] Q4 **[why]** Which terms couple $L$ to $R$, and why is that the reason a Dirac mass needs both chiralities?

> [!tip]- Hints: route in the notes
> - Technique: K7
> - Steps 1–6 of [[§C5a.7 The Dirac Equation and Its Lagrangian#^der-c5a-7-9|Derivation §C5a.7.9]]; kinematics versus mass: [[§C5a.5 Chirality and Weyl Spinors#^rem-c5a-5-2|§C5a.5, Remark: Kinematics allows one handedness, a mass needs both]].

### Weyl plane waves have fixed helicity ★

$\psi_L = \xi e^{-ip\cdot x}$ ($p^0 > 0$) solves the left-handed Weyl equation iff $p^2 = 0$ and $(\hat{\mathbf p}\cdot\boldsymbol\sigma)\xi = -\xi$, helicity $-\frac12$; a right-handed plane wave has helicity $+\frac12$, see Theorem [[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-12|§C5a.7.12]] Weyl Plane Waves Have Fixed Helicity. *Source: the user's notes Ch. 8 §8.10 · PS §3.2*

^nd-thm-c5a-7-12

- [ ] Q1 **[state]** State the condition on $p$ and on $\xi$ for each handedness.
- [ ] Q2 Insert the plane wave. Which $2\times2$ matrix must annihilate $\xi$?
- [ ] Q3 Why does a nonzero solution need $p^2 = 0$ (determinant)?
- [ ] Q4 Solve for the kernel. Which eigenvalue of $\hat{\mathbf p}\cdot\boldsymbol\sigma$ appears?
- [ ] Q5 **[why]** Why is the spin operator in each Weyl block $\frac12\boldsymbol\sigma$, so that the eigenvalue is a helicity?

> [!tip]- Hints: route in the notes
> - Technique: K1
> - Steps 1–2 of [[§C5a.7 The Dirac Equation and Its Lagrangian#^der-c5a-7-12|Derivation §C5a.7.12]], step 3 ($p^2 = 0$), step 4 (kernel), step 5 (right-handed), step 6 (helicity).

### Why "left-handed" ★★

The positive-frequency solutions of the left-handed Weyl equation have spin against momentum, helicity $-\frac12$ (left-hand screw); the label of the representation ($(\frac12, 0)$, $\gamma^5 = -1$, chirality) was named after this property of its massless particles; with a mass, chirality (Lorentz-invariant, of the field) and helicity (frame-dependent, of a state) separate, see [[§C5a.7 The Dirac Equation and Its Lagrangian#^rem-c5a-7-6|§C5a.7, Remark: Why "left-handed"]]. *Source: the user's question (2026-10-13) · Lecture 8, slide "Weyl Spinors"*

^nd-rem-c5a-7-6

- [ ] Q1 **[def]** Define chirality and helicity, each with the operator that measures it.
- [ ] Q2 For a massless positive-frequency solution of the left-handed equation, which helicity results, and which hand's screw sense does it follow?
- [ ] Q3 For $m > 0$, why can the helicity of a particle be reversed by a boost while its chirality label cannot change?
- [ ] Q4 In the massless limit of $u_\pm$, which Weyl half carries which helicity?
- [ ] Q5 **[why]** Why is the name "left-handed" for $(\frac12, 0)$ a statement about massless particles only, and what does the mass do to the two notions?
- [ ] Q6 **[conv]** With Problem Set 5's sign of $\mathbf K$, is "left-handed" still $(\frac12, 0)$?

> [!tip]- Hints: route in the notes
> - Technique: K1, K7
> - [[§C5a.7 The Dirac Equation and Its Lagrangian#^rem-c5a-7-6|§C5a.7, Remark: Why "left-handed"]]; Theorem [[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-12|§C5a.7.12]] Weyl Plane Waves Have Fixed Helicity; helicity becomes chirality: Theorem [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-14|§C5a.10.14]] The Massless and High-Energy Limit: Helicity Becomes Chirality; frame dependence: [[§C5a.10 Normalization, Spin Sums and Helicity#^rem-c5a-10-3|§C5a.10, Remark: The helicity of a massive particle depends on the frame]]; the sign of K: [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^cau-c3-2-2|§C3.2, Caution: Which one is (½, 0) depends on the sign of K]].

### The Dirac equation keeps its form when ψ and γ change together ★

With $\psi' = U\psi$, $\gamma'^\mu = U\gamma^\mu U^{-1}$, $(i\gamma'^\mu\partial_\mu - m)\psi' = U(i\gamma^\mu\partial_\mu - m)\psi$: the equation is basis-free; changing $\gamma$ without $\psi$ breaks solutions, see Theorem [[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-2|§C5a.7.2]] The Dirac Equation Keeps Its Form When ψ and γ Change Together. *Source: Problem Set 6, Problem 3 (the change of basis, statement) · the user's notes Ch. 8*

^nd-thm-c5a-7-2

- [ ] Q1 **[state]** State the form invariance under a change of basis.
- [ ] Q2 Why does $\partial_\mu$ pass through $U$?
- [ ] Q3 Insert $U^{-1}U$ in the kinetic term and finish.
- [ ] Q4 **[why]** Give the by-product example: why does replacing $\gamma$ by $\gamma^5\gamma\gamma^5$ while keeping $\psi$ break solutions?
- [ ] Q5 **[why]** Contrast with a Lorentz transformation: what compensates there that does not compensate here?

> [!tip]- Hints: route in the notes
> - Technique: K5
> - Steps 1–4 of [[§C5a.7 The Dirac Equation and Its Lagrangian#^der-c5a-7-2|Derivation §C5a.7.2]], step 5 (by-product); Lagrangian under a change of basis: Theorem [[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-5|§C5a.7.5]] The Dirac Lagrangian under a Change of Basis; three different transformations: [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^cau-c5a-4-1|§C5a.4, Caution: Three different transformations]].

### Canonical momenta of the Dirac field ★

$\pi_\psi = \partial\mathcal L/\partial(\partial_0\psi) = i\bar\psi\gamma^0 = i\psi^\dagger$, $\pi_{\bar\psi} = 0$: the momentum is not a function of $\dot\psi$, and $\psi$, $\psi^\dagger$ are themselves canonically conjugate, see Theorem [[§C5a.8 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-8-1|§C5a.8.1]] Canonical Momenta of the Dirac Field. *Source: Lecture 10 (canonical momentum and its puzzle) · the user's notes Ch. 8 · Course Log, Lecture 8 row*

^nd-thm-c5a-8-1

- [ ] Q1 **[state]** State both canonical momenta.
- [ ] Q2 Isolate the time-derivative part of $\mathcal L$ and differentiate component by component.
- [ ] Q3 Why is $\pi_{\bar\psi} = 0$?
- [ ] Q4 **[why]** Why is the Legendre map not invertible, and what does that imply for the phase space (how many real canonical pairs)?
- [ ] Q5 **[conv]** Which symbol do the slides and Problem Set 3 use for the momentum density, and which the vault?

> [!tip]- Hints: route in the notes
> - Technique: K12 (Noether recipe), K2
> - Steps 1–3 of [[§C5a.8 Canonical Structure and Noether Currents of the Dirac Field#^der-c5a-8-1|Derivation §C5a.8.1]]; [[Larsen PHY 513|register: Momentum density]].

### The Hamiltonian density of the Dirac field ★

$\mathcal H = \pi_\psi\dot\psi - \mathcal L = \bar\psi(-i\gamma^j\partial_j + m)\psi = \psi^\dagger(-i\boldsymbol\alpha\cdot\nabla + \beta m)\psi$, equal to $i\psi^\dagger\partial_t\psi$ on solutions, see Theorem [[§C5a.8 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-8-2|§C5a.8.2]] The Hamiltonian Density of the Dirac Field. *Source: Lecture 10, slide 16 · the user's notes Ch. 8 · Problem Set 5, Problem 4 (context)*

^nd-thm-c5a-8-2

- [ ] Q1 **[state]** Write $\mathcal H$ in the $\gamma$ form and in the $\boldsymbol\alpha$, $\beta$ form.
- [ ] Q2 Split $\mathcal L$ into time and space parts and subtract from $\pi_\psi\dot\psi$. Which terms cancel?
- [ ] Q3 Rewrite with $\psi^\dagger$ and check that $\boldsymbol\alpha$, $\beta$ are Hermitian.
- [ ] Q4 Use the Dirac equation to show the on-shell form.
- [ ] Q5 **[why]** Why can the classical $\mathcal H$ be negative (look at the spectrum of $H_{\text{s.p.}}$), and what repairs this after quantization?

> [!tip]- Hints: route in the notes
> - Technique: K12
> - Steps 1–4 of [[§C5a.8 Canonical Structure and Noether Currents of the Dirac Field#^der-c5a-8-2|Derivation §C5a.8.2]], step 5 (Hermiticity), step 6 (on shell), step 7 (spectrum); negative frequency and antiparticles: [[§C5a.7 The Dirac Equation and Its Lagrangian#^rem-c5a-7-4|§C5a.7, Remark: Negative frequency and antiparticles]].

### The vector current ★

The phase rotation $\psi \to e^{i\alpha}\psi$ leaves $\mathcal L$ invariant; with the conventional sign $j^\mu = \bar\psi\gamma^\mu\psi$, $\partial_\mu j^\mu = 0$ on solutions, $Q = \int d^3x\,\psi^\dagger\psi \ge 0$, see Theorem [[§C5a.8 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-8-3|§C5a.8.3]] The Vector Current. *Source: the user's notes Ch. 8 · Course Log, Lecture 8 row (Noether currents)*

^nd-thm-c5a-8-3

- [ ] Q1 **[state]** State the symmetry, the current and the charge.
- [ ] Q2 Find $\Delta\psi$, $\Delta\bar\psi$ and check $\delta\mathcal L = 0$.
- [ ] Q3 Apply the Noether recipe: which term of $\partial\mathcal L/\partial(\partial_\mu\cdot)$ contributes?
- [ ] Q4 Check conservation directly with the two Dirac equations.
- [ ] Q5 **[conv]** The recipe gives $-\bar\psi\gamma^\mu\psi$. Why is the sign flipped, and which convention of the complex scalar does it match?

> [!tip]- Hints: route in the notes
> - Technique: K12
> - Steps 1–4 of [[§C5a.8 Canonical Structure and Noether Currents of the Dirac Field#^der-c5a-8-3|Derivation §C5a.8.3]], step 5 (direct check), step 6 (charge); sign convention: [[§C1b.6 Conserved Charges and Internal Symmetries#^cau-c1b-6-3|§C1b.6, Caution: Sign and normalization of the U(1) current]].

### The axial current ★

$\partial_\mu(\bar\psi\gamma^\mu\gamma^5\psi) = 2im\bar\psi\gamma^5\psi$ on solutions: conserved iff $m = 0$, when $\psi \to e^{i\alpha\gamma^5}\psi$ is a symmetry and the chiral currents are separately conserved, see Theorem [[§C5a.8 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-8-4|§C5a.8.4]] The Axial Current. *Source: the user's notes Ch. 8 · Problem Set 6, Problem 5 (as the user wrote it)*

^nd-thm-c5a-8-4

- [ ] Q1 **[state]** State the divergence of the axial current.
- [ ] Q2 Use the conjugate Dirac equation on the first term of the product rule.
- [ ] Q3 Move $\gamma^5$ to the left in the second term and use the Dirac equation.
- [ ] Q4 **[why]** Why are $j^\mu_L$ and $j^\mu_R$ separately conserved at $m = 0$, and what are they in Weyl components?

> [!tip]- Hints: route in the notes
> - Technique: K7
> - Steps 1–4 of [[§C5a.8 Canonical Structure and Noether Currents of the Dirac Field#^der-c5a-8-4|Derivation §C5a.8.4]], step 6 (chiral currents).

### Energy–momentum tensor, momentum operator, chiral symmetry

The canonical tensor and its conservation (Theorem [[§C5a.8 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-8-5|§C5a.8.5]] The Canonical Energy–Momentum Tensor of the Dirac Field) → drilled as [[PHY 513 PS Drill#^ps5-4-a|PS5.4(a)]]; the momentum operator (Theorem [[§C5a.8 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-8-6|§C5a.8.6]] Energy and Momentum of the Dirac Field) → drilled as [[PHY 513 PS Drill#^ps5-4-b|PS5.4(b)]]; the chiral transformation, its Noether current and divergence (Example [[§C5a.8 Canonical Structure and Noether Currents of the Dirac Field#^ex-c5a-8-1|§C5a.8.1]] Chiral Symmetry) → drilled as [[PHY 513 PS Drill#^ps6-5|PS6.5]].

^nd-thm-c5a-8-5

### Plane waves turn the Dirac equation into algebra ★★

$u(p)e^{-ip\cdot x}$ solves the Dirac equation iff $(\slashed p - m)u = 0$ ($u$ an eigenvector of $\slashed p$ with eigenvalue $+m$); $v(p)e^{+ip\cdot x}$ iff $(\slashed p + m)v = 0$ (eigenvalue $-m$), see Theorem [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-1|§C5a.9.1]] Plane Waves Turn the Dirac Equation into Algebra. *Source: Lecture 9, slides "Solution of The Dirac Equation: Step 2", "Negative Frequency Solutions I"*

^nd-thm-c5a-9-1

- [ ] Q1 **[state]** State the algebraic conditions for $u$ and $v$.
- [ ] Q2 What does $\partial_\mu$ do to $e^{\mp ip\cdot x}$?
- [ ] Q3 Insert the positive-frequency wave and cancel the exponential. Why may it be cancelled?
- [ ] Q4 **[conv]** Redo it for $e^{+ip\cdot x}$. Where does the sign in "$-\gamma^\mu p_\mu - m$" (the slide's note) come from?

> [!tip]- Hints: route in the notes
> - Technique: K9 (mode substitution)
> - Steps 1–4 of [[§C5a.9 Plane-Wave Solutions#^der-c5a-9-1|Derivation §C5a.9.1]].

### The eigenvalues of p̸ ★★

On shell $\slashed p^2 = m^2$; for $m > 0$, $\slashed p$ is diagonalizable with eigenvalues $\pm m$, each twice, so exactly two $u$'s and two $v$'s; for $m = 0$, $\slashed p$ is nilpotent, not diagonalizable, with a two-dimensional kernel, see Theorem [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-2|§C5a.9.2]] The Eigenvalues of p̸. *Source: Lecture 9, slide "Solution of The Dirac Equation: Step 2" ("All eigenvalues of (γ^μp_μ) are either +m or −m … tr(γ^μp_μ) = 0")*

^nd-thm-c5a-9-2

- [ ] Q1 **[state]** State the eigenvalue result for $m > 0$ and for $m = 0$.
- [ ] Q2 Compute $\slashed p^2$ by symmetrizing. Which eigenvalues are possible?
- [ ] Q3 **[why]** "All eigenvalues are $\pm m$" does not yet give two of each. Why is $\slashed p$ diagonalizable for $m > 0$ (decompose $w$ with $\slashed p \pm m$)?
- [ ] Q4 Use $\operatorname{tr}\slashed p = 0$ to get the multiplicities. Why is the trace zero?
- [ ] Q5 **[why]** What changes at $m = 0$, and why do the $u$ and $v$ equations coincide there?

> [!tip]- Hints: route in the notes
> - Technique: K5
> - Steps 1–2 of [[§C5a.9 Plane-Wave Solutions#^der-c5a-9-2|Derivation §C5a.9.2]], step 3 (diagonalizable), step 4 (trace), step 5 ($m = 0$); second route via the determinant and $H_{\text{s.p.}}$: [[§C5a.9 Plane-Wave Solutions#^der-c5a-9-2b|Derivation §C5a.9.2, second route]].

### Rest-frame solutions ★★

At $p = (m, \mathbf 0)$: $u_0 = \sqrt m(\xi, \xi)$ and $v_0 = \sqrt m(\eta, -\eta)$ for arbitrary two-spinors, see Theorem [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-3|§C5a.9.3]] Rest-Frame Solutions. *Source: Lecture 9, slides "Solution of the Dirac Equation: Step 3", "Negative Frequency Solutions II" · PS (3.47)*

^nd-thm-c5a-9-3

- [ ] Q1 **[state]** Write $u_0$ and $v_0$.
- [ ] Q2 Write $\slashed p - m$ at rest in $2\times2$ blocks and solve for the halves of $u$.
- [ ] Q3 Do the same for $v$ with $\slashed p + m$. Where does the relative minus sign come from?
- [ ] Q4 **[why]** Why is the factor $\sqrt m$ a convention, and what fixes it?

> [!tip]- Hints: route in the notes
> - Technique: K1 (invariants in a convenient frame)
> - Steps 1–3 of [[§C5a.9 Plane-Wave Solutions#^der-c5a-9-3|Derivation §C5a.9.3]]; normalization: Definition [[§C5a.9 Plane-Wave Solutions#^def-c5a-9-4|§C5a.9.4]] Normalization of the Spinors.

### In the rest frame the two-spinor carries the spin ★★

$J^k = \frac12\operatorname{diag}(\sigma^k, \sigma^k)$ acts on $u_0(\xi)$ as $u_0(\frac12\sigma^k\xi)$, and a rotation acts as $u_0(D\xi)$ with $D$ the spin-½ matrix: $\xi$ is the nonrelativistic spin, see Theorem [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-4|§C5a.9.4]] In the Rest Frame the Two-Spinor Carries the Spin. *Source: Lecture 9, slide "Solution of the Dirac Equation: Step 3" · Lecture 9 (spoken: "the J operator is a half sigma")*

^nd-thm-c5a-9-4

- [ ] Q1 **[state]** How do the rotation generators and finite rotations act on $u_0(\xi)$?
- [ ] Q2 Apply $\frac12\operatorname{diag}(\sigma^k, \sigma^k)$ to $\sqrt m(\xi, \xi)$.
- [ ] Q3 Why does a finite rotation act by the same $2\times2$ matrix on both halves?
- [ ] Q4 **[conv]** The slide calls $\operatorname{diag}(\sigma^k, \sigma^k)$ the angular momentum. Correct it.
- [ ] Q5 **[why]** Why does $u_0$ describe one spin-½ particle, not two?

> [!tip]- Hints: route in the notes
> - Technique: K1
> - Steps 1–3 of [[§C5a.9 Plane-Wave Solutions#^der-c5a-9-4|Derivation §C5a.9.4]]; [[§C5a.9 Plane-Wave Solutions#^cau-c5a-9-1|§C5a.9, Caution: The slide's "angular momentum" is twice the angular momentum]]; [[§C5a.9 Plane-Wave Solutions#^rem-c5a-9-3|§C5a.9, Remark: One spin-½ particle, not two]].

### The spinor boost along z ★★

$\Lambda_{1/2} = e^{-i\eta S^{03}} = \operatorname{diag}(e^{-\eta\sigma^3/2}, e^{+\eta\sigma^3/2})$, with $e^{\mp\eta\sigma^3/2} = \cosh\frac\eta2 \mp \sinh\frac\eta2\,\sigma^3 = (\cosh\eta \mp \sinh\eta\,\sigma^3)^{1/2}$ (positive root), see Theorem [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-5|§C5a.9.5]] The Spinor Boost along z. *Source: Lecture 9, slide "Solution of the Dirac Equation: Step 4"*

^nd-thm-c5a-9-5

- [ ] Q1 **[state]** Write the spinor boost along $z$ in blocks, in half-rapidity form and as a square root.
- [ ] Q2 Which terms of $-\frac i2\omega_{\mu\nu}S^{\mu\nu}$ survive for $\omega_{03} = -\omega_{30} = \eta$, and what is $S^{03}$?
- [ ] Q3 Sum the series of $e^{-\eta\sigma^3/2}$ using $(\sigma^3)^2 = \mathbb 1$.
- [ ] Q4 Rewrite with the projectors $P_\pm = \frac12(\mathbb 1 \pm \sigma^3)$ and square. Why does squaring double the rapidity?
- [ ] Q5 **[why]** Why is "taking the square root does nothing" to the projectors, and which root is meant?

> [!tip]- Hints: route in the notes
> - Technique: K4 (projectors, half angles)
> - Steps 1–2 of [[§C5a.9 Plane-Wave Solutions#^der-c5a-9-5|Derivation §C5a.9.5]], step 3 (series), steps 4–5 (projectors, square), step 6 (which root).
> - Half rapidity: [[§C5a.9 Plane-Wave Solutions#^rem-c5a-9-4|§C5a.9, Remark: Why a square root restores the full rapidity]].

### Explicit square roots ★

For $m > 0$, $\sqrt{p\cdot\sigma} = (p\cdot\sigma + m)/\sqrt{2(E_{\mathbf p} + m)}$, likewise with $\bar\sigma$; the spinors are smooth with polynomial growth; for $m = 0$ the formula holds for $\mathbf p \ne 0$, see Theorem [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-6|§C5a.9.6]] Explicit Square Roots. *Source: Problem Set 6, Problem 3(c) (the user's route) · the user's notes Ch. 9 §9.3*

^nd-thm-c5a-9-6

- [ ] Q1 **[state]** State the explicit square root.
- [ ] Q2 What are $\operatorname{tr}(p\cdot\sigma)$ and $\det(p\cdot\sigma)$? Apply Cayley–Hamilton.
- [ ] Q3 Square the ansatz $(A + m)/c$. Which $c$ works?
- [ ] Q4 **[why]** Why is this the positive root (and hence the root of the definition)?

> [!tip]- Hints: route in the notes
> - Technique: K4
> - Steps 1–3 of [[§C5a.9 Plane-Wave Solutions#^der-c5a-9-6|Derivation §C5a.9.6]], step 4 (positivity), steps 5–6 (smoothness, $m = 0$).

### The square-root identities ★★

$\sqrt{p\cdot\sigma}\sqrt{p\cdot\sigma} = p\cdot\sigma$; $(p\cdot\sigma)(p\cdot\bar\sigma) = m^2$; $\sqrt{p\cdot\sigma}\sqrt{p\cdot\bar\sigma} = m$: "never take the square root of a $2\times2$ matrix", see Theorem [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-7|§C5a.9.7]] The Square-Root Identities. *Source: Lecture 9, slide "Practical Manipulations"*

^nd-thm-c5a-9-7

- [ ] Q1 **[state]** State the three identities.
- [ ] Q2 Expand $(p\cdot\sigma)(p\cdot\bar\sigma)$ with $\sigma^i\sigma^j$ symmetrized.
- [ ] Q3 Why do $\sqrt{p\cdot\sigma}$ and $\sqrt{p\cdot\bar\sigma}$ commute?
- [ ] Q4 **[why]** Their product is a positive matrix whose square is $m^2$. Why is it then $m\mathbb 1$?

> [!tip]- Hints: route in the notes
> - Technique: K6 (on-shell replacement)
> - Steps 1–4 of [[§C5a.9 Plane-Wave Solutions#^der-c5a-9-7|Derivation §C5a.9.7]].

### The spinor boost from rest to momentum p ★★

The pure boost along $\hat{\mathbf p}$ taking $(m, \mathbf 0)$ to $p$ has spinor matrix $\Lambda_{1/2}(p) = \operatorname{diag}(\sqrt{p\cdot\sigma/m}, \sqrt{p\cdot\bar\sigma/m})$; the rapidity disappears, see Theorem [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-8|§C5a.9.8]] The Spinor Boost from Rest to Momentum p. *Source: Lecture 9, slide "Interpretation of Rapidity"*

^nd-thm-c5a-9-8

- [ ] Q1 **[state]** State the boost matrix in terms of $p$.
- [ ] Q2 From the vector boost, express $\cosh\eta$ and $\sinh\eta$ in $E$, $\lvert\mathbf p\rvert$, $m$.
- [ ] Q3 Show $\cosh\eta - \sinh\eta\,\hat{\mathbf p}\cdot\boldsymbol\sigma = p\cdot\sigma/m$ and its partner.
- [ ] Q4 **[why]** Why does every step of the $z$ case go through for an arbitrary direction $\hat{\mathbf p}$?

> [!tip]- Hints: route in the notes
> - Technique: K4, K1
> - Steps 1–4 of [[§C5a.9 Plane-Wave Solutions#^der-c5a-9-8|Derivation §C5a.9.8]].

### The positive-frequency spinors u(p) ★★

$u^s(p) = (\sqrt{p\cdot\sigma}\,\xi^s, \sqrt{p\cdot\bar\sigma}\,\xi^s)$ with $(\slashed p - m)u^s = 0$; for $m > 0$ it is $\Lambda_{1/2}(p)u_0^s$; it holds in every direction and for $m = 0$, see Theorem [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-9|§C5a.9.9]] The Positive-Frequency Spinors u(p). *Source: Lecture 9, slide "General Solution to Dirac Equation" · PS (3.50)*

^nd-thm-c5a-9-9

- [ ] Q1 **[state]** Write $u^s(p)$.
- [ ] Q2 **[why]** Why is the boosted rest-frame solution again a solution (covariance), and with which momentum in the exponent?
- [ ] Q3 Multiply $\Lambda_{1/2}(p)$ into $\sqrt m(\xi, \xi)$.
- [ ] Q4 Why do $u^1$, $u^2$ span $\ker(\slashed p - m)$?
- [ ] Q5 **[why]** Why does the boost derivation fail at $m = 0$, although the formula survives?

> [!tip]- Hints: route in the notes
> - Technique: K1 (rest frame, then boost)
> - Steps 1–3 of [[§C5a.9 Plane-Wave Solutions#^der-c5a-9-9|Derivation §C5a.9.9]], step 4 (multiply), step 5 (span); $m = 0$: [[§C5a.9 Plane-Wave Solutions#^der-c5a-9-9b|Derivation §C5a.9.9, second route]].

### u(p) checked directly, valid for m ≥ 0 ★★

$\slashed p\,u = (p\cdot\sigma\sqrt{p\cdot\bar\sigma}\,\xi, p\cdot\bar\sigma\sqrt{p\cdot\sigma}\,\xi) = m\,u$ by the square-root identities, with no division by $m$, see [[§C5a.9 Plane-Wave Solutions#^der-c5a-9-9b|Derivation §C5a.9.9, second route]]. **[class exercise, Lecture 9]** ("Final result valid also for m = 0 (but needs new derivation)"; "Example: check u(p) satisfies Dirac equation in general frame"). *Source: Lecture 9, slides "General Solution to Dirac Equation", "Practical Manipulations"*

^nd-der-c5a-9-9b

- [ ] Q1 **[state]** What is to be checked, and for which $m$?
- [ ] Q2 Multiply the chiral $\slashed p$ into the column $u$.
- [ ] Q3 Split one factor $p\cdot\sigma = \sqrt{p\cdot\sigma}\sqrt{p\cdot\sigma}$ and use $\sqrt{p\cdot\sigma}\sqrt{p\cdot\bar\sigma} = m$.
- [ ] Q4 **[why]** At $m = 0$, why do $u^1$, $u^2$ still span the kernel of $\slashed p$?

> [!tip]- Hints: route in the notes
> - Technique: K6
> - Steps 1–3 of [[§C5a.9 Plane-Wave Solutions#^der-c5a-9-9b|Derivation §C5a.9.9, second route]]; the identities: Theorem [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-7|§C5a.9.7]] The Square-Root Identities.

### The Dirac conjugate of u(p) ★

$\bar u^s(p) = (\xi^{s\dagger}\sqrt{p\cdot\bar\sigma}, \xi^{s\dagger}\sqrt{p\cdot\sigma})$, a row with the roots exchanged, satisfying $\bar u(\slashed p - m) = 0$, see Theorem [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-10|§C5a.9.10]] The Dirac Conjugate of u(p). *Source: Lecture 9, slides "Normalization II", "Completeness for Dirac Spinors"*

^nd-thm-c5a-9-10

- [ ] Q1 **[state]** Write the row $\bar u^s(p)$ and its equation.
- [ ] Q2 Why do the roots pass through the dagger unchanged?
- [ ] Q3 What does right multiplication by $\gamma^0$ do to a row in the chiral basis?
- [ ] Q4 **[why]** Why does the Dirac equation act from the right on $\bar u$, with the same eigenvalue?

> [!tip]- Hints: route in the notes
> - Technique: K7
> - Steps 1–3 of [[§C5a.9 Plane-Wave Solutions#^der-c5a-9-10|Derivation §C5a.9.10]], step 4 (the conjugate equation); other routes: [[§C5a.9 Plane-Wave Solutions#^der-c5a-9-10b|Derivation §C5a.9.10, second route]], [[§C5a.9 Plane-Wave Solutions#^der-c5a-9-10c|Derivation §C5a.9.10, third route]].

### The negative-frequency spinors v(p) ★★

$v^s(p) = (\sqrt{p\cdot\sigma}\,\eta^s, -\sqrt{p\cdot\bar\sigma}\,\eta^s)$ with $(\slashed p + m)v^s = 0$; the $u$'s and $v$'s together are the four eigenvectors of $\slashed p$, see Theorem [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-11|§C5a.9.11]] The Negative-Frequency Spinors v(p). *Source: Lecture 9, slides "Negative Frequency Solutions I–II", "Summary II" · PS (3.62)*

^nd-thm-c5a-9-11

- [ ] Q1 **[state]** Write $v^s(p)$ and its algebraic equation.
- [ ] Q2 Repeat the four steps (ansatz, eigenvalue problem, rest frame, boost): which step brings the minus sign?
- [ ] Q3 Check $(\slashed p + m)v = 0$ directly with the square-root identities.
- [ ] Q4 **[conv]** Which $\eta^s$ does the course fix from Lecture 12 on?
- [ ] Q5 **[why]** Why is the boost matrix that produces $v(p)$ the same $\Lambda_{1/2}(p)$ as for $u$?

> [!tip]- Hints: route in the notes
> - Technique: K1
> - Steps 1–5 of [[§C5a.9 Plane-Wave Solutions#^der-c5a-9-11|Derivation §C5a.9.11]]; η: Definition [[§C5a.9 Plane-Wave Solutions#^def-c5a-9-3|§C5a.9.3]] Spin Basis, [[§C5a.9 Plane-Wave Solutions#^cau-c5a-9-2|§C5a.9, Caution: η means two things]].

### The Dirac conjugate of v(p) ★

$\bar v^s(p) = (-\eta^{s\dagger}\sqrt{p\cdot\bar\sigma}, \eta^{s\dagger}\sqrt{p\cdot\sigma})$, $\bar v(\slashed p + m) = 0$: the minus sign moves from the lower half of the column to the upper half of the row, see Theorem [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-12|§C5a.9.12]] The Dirac Conjugate of v(p). *Source: Lecture 9, slide "Completeness of v's" ("Sign of v̄ differs from ū in upper entry")*

^nd-thm-c5a-9-12

- [ ] Q1 **[state]** Write $\bar v^s(p)$.
- [ ] Q2 Take the dagger of the column block by block. Does the minus sign move?
- [ ] Q3 Multiply by $\gamma^0$. Where is the minus sign now?
- [ ] Q4 **[why]** What is $\bar v_0^s$ at rest in terms of $v_0^{s\dagger}$, and why the sign?

> [!tip]- Hints: route in the notes
> - Technique: K7
> - Steps 1–3 of [[§C5a.9 Plane-Wave Solutions#^der-c5a-9-12|Derivation §C5a.9.12]], step 5 (rest frame); second route: [[§C5a.9 Plane-Wave Solutions#^der-c5a-9-12b|Derivation §C5a.9.12, second route]].

### The plane-wave spinors in the Dirac basis

$u_D = U_Du = (E + m)^{-1/2}((E + m)\xi, \boldsymbol\sigma\cdot\mathbf p\,\xi)$ with $\bar u_Du_D = 2m$, see Example [[§C5a.9 Plane-Wave Solutions#^ex-c5a-9-1|§C5a.9.1]] The Plane-Wave Spinors in the Dirac Basis. → drilled as [[PHY 513 PS Drill#^ps6-3-c|PS6.3(c)]] and [[PHY 513 PS Drill#^ps6-3-d|PS6.3(d)]].

^nd-ex-c5a-9-1

### u†u = 2E ★★

$u^{r\dagger}(p)u^s(p) = 2E_{\mathbf p}\delta^{rs}$, frame-dependent, see Theorem [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-1|§C5a.10.1]] u†u = 2E. *Source: Lecture 9, slide "Normalization I"*

^nd-thm-c5a-10-1

- [ ] Q1 **[state]** State the normalization.
- [ ] Q2 Write the row $u^{s\dagger}$ (why are the roots unchanged?) and multiply upper with upper, lower with lower.
- [ ] Q3 Add $p\cdot\sigma + p\cdot\bar\sigma$. Which parts cancel?
- [ ] Q4 **[why]** Why is it not surprising that $u^\dagger u$ depends on the frame? Of which four-vector is it the time component?

> [!tip]- Hints: route in the notes
> - Technique: K6
> - Steps 1–3 of [[§C5a.10 Normalization, Spin Sums and Helicity#^der-c5a-10-1|Derivation §C5a.10.1]]; frame dependence: [[§C5a.10 Normalization, Spin Sums and Helicity#^rem-c5a-10-1|§C5a.10, Remark: Why u†u depends on the frame and ūu does not]].

### ūu = 2m ★★

$\bar u^r(p)u^s(p) = 2m\delta^{rs}$ in every frame, see Theorem [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-2|§C5a.10.2]] ūu = 2m. *Source: Lecture 9, slide "Normalization II"*

^nd-thm-c5a-10-2

- [ ] Q1 **[state]** State the invariant normalization.
- [ ] Q2 Multiply the row $\bar u^r$ by the column $u^s$. Which roots meet in each term?
- [ ] Q3 Which square-root identity finishes?
- [ ] Q4 **[why]** Why must $\bar uu$ be the same in every frame?

> [!tip]- Hints: route in the notes
> - Technique: K6
> - Steps 1–2 of [[§C5a.10 Normalization, Spin Sums and Helicity#^der-c5a-10-2|Derivation §C5a.10.2]]; Theorem [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-7|§C5a.9.7]] The Square-Root Identities part 3; invariance: Theorem [[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-1|§C5a.6.1]] The Dirac Conjugate Transforms with the Inverse.

### v†v = 2E ★★

$v^{r\dagger}(p)v^s(p) = 2E_{\mathbf p}\delta^{rs}$, see Theorem [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-3|§C5a.10.3]] v†v = 2E. **[class exercise, Lecture 9]** ("Normalization of v†v: repeat computation of u†u"). *Source: Lecture 9, slide "Normalization of v's"*

^nd-thm-c5a-10-3

- [ ] Q1 **[state]** State the normalization of $v^\dagger v$.
- [ ] Q2 Redo the $u^\dagger u$ computation for $v$. What happens to the minus sign in the lower half?
- [ ] Q3 **[why]** Why is $v^\dagger v$ positive, and what does that say about the classical charge density $\psi^\dagger\psi$?

> [!tip]- Hints: route in the notes
> - Technique: K6
> - The steps of [[§C5a.10 Normalization, Spin Sums and Helicity#^der-c5a-10-1|Derivation §C5a.10.1]] with $\xi \to \eta$; "What the derivation shows" of [[§C5a.10 Normalization, Spin Sums and Helicity#^der-c5a-10-3|Derivation §C5a.10.3]].

### v̄v = −2m ★★

$\bar v^r(p)v^s(p) = -2m\delta^{rs}$: invariant and negative, see Theorem [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-4|§C5a.10.4]] v̄v = −2m. **[class exercise, Lecture 9]** ("Normalization of v̄v: repeat computation of ūu. γ⁰ exchanges lower and upper entry, so an overall sign"). *Source: Lecture 9, slide "Normalization of v's"*

^nd-thm-c5a-10-4

- [ ] Q1 **[state]** State the normalization of $\bar vv$.
- [ ] Q2 Multiply the row $\bar v^r$ by the column $v^s$. Which halves meet, and with which signs?
- [ ] Q3 **[why]** Why does $\gamma^0$ produce an overall minus sign here but not for $v^\dagger v$?
- [ ] Q4 **[why]** Is the negative value a problem? Where does the same sign reappear (spin sum)?

> [!tip]- Hints: route in the notes
> - Technique: K6, K7
> - Steps 1–2 of [[§C5a.10 Normalization, Spin Sums and Helicity#^der-c5a-10-4|Derivation §C5a.10.4]]; [[§C5a.10 Normalization, Spin Sums and Helicity#^cau-c5a-10-1|§C5a.10, Caution: The sign of v̄v]].

### u and v are orthogonal under the Dirac conjugate ★★

$\bar v^r(p)u^s(p) = \bar u^r(p)v^s(p) = 0$ for all $r$, $s$ and all spin bases, see Theorem [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-5|§C5a.10.5]] u and v Are Orthogonal under the Dirac Conjugate. *Source: Lecture 9, slide "Bonus Material: Orthogonality of u and v"*

^nd-thm-c5a-10-5

- [ ] Q1 **[state]** State the orthogonality.
- [ ] Q2 Multiply $\bar v^r$ into $u^s$. Which two terms appear?
- [ ] Q3 Why do they cancel whether or not $r = s$ (which identity, and which sign)?
- [ ] Q4 **[why]** Why does the cancellation not depend on the choice of $\xi^s$, $\eta^s$?

> [!tip]- Hints: route in the notes
> - Technique: K10 (u, v orthogonality)
> - Steps 1–2 of [[§C5a.10 Normalization, Spin Sums and Helicity#^der-c5a-10-5|Derivation §C5a.10.5]].

### u and v are orthogonal at opposite three-momenta ★

$u^{r\dagger}(p)v^s(\tilde p) = v^{r\dagger}(p)u^s(\tilde p) = 0$ with $\tilde p = (E, -\mathbf p)$, while $u^{r\dagger}(p)v^s(p) = -2\xi^{r\dagger}(\mathbf p\cdot\boldsymbol\sigma)\eta^s$ in general, see Theorem [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-6|§C5a.10.6]] u and v Are Orthogonal at Opposite Three-Momenta. **[class exercise, Lecture 9]** (the slide's "Warning", stated without derivation). *Source: Lecture 9, slide "Bonus Material: Orthogonality of u and v"*

^nd-thm-c5a-10-6

- [ ] Q1 **[state]** State the two orthogonality relations at opposite momenta.
- [ ] Q2 What does $\mathbf p \to -\mathbf p$ do to $p\cdot\sigma$ and $p\cdot\bar\sigma$ (and their roots)?
- [ ] Q3 Multiply $u^{r\dagger}(p)v^s(\tilde p)$ upper with upper, lower with lower. Which identity cancels the terms?
- [ ] Q4 Compute $u^{r\dagger}(p)v^s(p)$ at equal momenta. Why is it not zero in general?
- [ ] Q5 **[why]** Where is this relation used (extracting mode operators from the field)?

> [!tip]- Hints: route in the notes
> - Technique: K10
> - Steps 1–4 of [[§C5a.10 Normalization, Spin Sums and Helicity#^der-c5a-10-6|Derivation §C5a.10.6]]; second route via the Hermitian $H_{\text{s.p.}}$: [[§C5a.10 Normalization, Spin Sums and Helicity#^der-c5a-10-6b|Derivation §C5a.10.6, second route]].

### The spin sum over u ★★

$\sum_s u^s(p)\bar u^s(p) = \slashed p + m$, a $4\times4$ matrix independent of the spin basis, see Theorem [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-7|§C5a.10.7]] The Spin Sum over u. *Source: Lecture 9, slides "Completeness for Dirac Spinors", "… the Result"*

^nd-thm-c5a-10-7

- [ ] Q1 **[state]** State the spin sum.
- [ ] Q2 **[def]** Why is "column times row" a matrix, and what is the two-spinor analogue $\sum_s\xi^s\xi^{s\dagger}$?
- [ ] Q3 Write $u^s\bar u^s$ block by block, then sum over $s$.
- [ ] Q4 Evaluate the four blocks with the square-root identities. Which are $m$, and which are the blocks of $\slashed p$?
- [ ] Q5 **[why]** Why is the sum not $2m\mathbb 1$ (what does it project onto)?

> [!tip]- Hints: route in the notes
> - Technique: K6
> - Steps 1–3 of [[§C5a.10 Normalization, Spin Sums and Helicity#^der-c5a-10-7|Derivation §C5a.10.7]]; [[§C5a.10 Normalization, Spin Sums and Helicity#^rem-c5a-10-2|§C5a.10, Remark: Why neither spin sum is the identity]].

### The spin sum over v ★★

$\sum_s v^s(p)\bar v^s(p) = \slashed p - m$, see Theorem [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-8|§C5a.10.8]] The Spin Sum over v. **[class exercise, Lecture 9]** ("structure only, same details as uū"). *Source: Lecture 9, slide "Completeness of v's"*

^nd-thm-c5a-10-8

- [ ] Q1 **[state]** State the $v$ spin sum.
- [ ] Q2 Track the signs: which entries of $v$ and of $\bar v$ carry the minus sign?
- [ ] Q3 Which blocks of the product change sign, and which do not?
- [ ] Q4 **[why]** Why does the change amount exactly to $m \to -m$?

> [!tip]- Hints: route in the notes
> - Technique: K6
> - The steps of [[§C5a.10 Normalization, Spin Sums and Helicity#^der-c5a-10-7|Derivation §C5a.10.7]] with the signs of Theorem [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-11|§C5a.9.11]] The Negative-Frequency Spinors v(p) and Theorem [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-12|§C5a.9.12]] The Dirac Conjugate of v(p); "What the derivation shows" of [[§C5a.10 Normalization, Spin Sums and Helicity#^der-c5a-10-8|Derivation §C5a.10.8]].

### The spin sums are covariant ★

$\Lambda_{1/2}\slashed p\Lambda_{1/2}^{-1} = \slashed{(\Lambda p)}$, so boosted spinors solve the equation at $\Lambda p$ and their spin sum is $\slashed{(\Lambda p)} \pm m$, see Theorem [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-9|§C5a.10.9]] The Spin Sums Are Covariant. *Source: the user's notes Ch. 9 §9.4*

^nd-thm-c5a-10-9

- [ ] Q1 **[state]** State the covariance of $\slashed p$ and of the spin sums.
- [ ] Q2 Contract the invariance law of $\gamma^\mu$ with $(\Lambda p)_\mu$.
- [ ] Q3 How does $\overline{\Lambda_{1/2}u}$ transform (pseudo-unitarity)?
- [ ] Q4 **[why]** In which sense is $\slashed p$ "invariant", given that it carries two spinor slots?

> [!tip]- Hints: route in the notes
> - Technique: K14
> - Steps 1–4 of [[§C5a.10 Normalization, Spin Sums and Helicity#^der-c5a-10-9|Derivation §C5a.10.9]].

### Completeness and the energy projectors ★

For $m > 0$, $\frac1{2m}\sum_s(u^s\bar u^s - v^s\bar v^s) = \mathbb 1$; $\Lambda_\pm = (\pm\slashed p + m)/2m$ are complementary projectors onto the $u$'s and the $v$'s, $\operatorname{tr}\Lambda_\pm = 2$, see Theorem [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-10|§C5a.10.10]] Completeness and the Energy Projectors. *Source: the user's notes Ch. 9 §9.4 (the check on basis vectors)*

^nd-thm-c5a-10-10

- [ ] Q1 **[state]** State the completeness relation and the projectors.
- [ ] Q2 Derive completeness from the two spin sums. Why does the $v$ sum enter with a minus sign?
- [ ] Q3 Check it on a basis vector $u^r$ and on $v^r$, using the normalizations and orthogonality.
- [ ] Q4 Verify $\Lambda_\pm^2 = \Lambda_\pm$ from $\slashed p^2 = m^2$.
- [ ] Q5 **[why]** Why is completeness a sum over all four solutions, not over the two $u$'s?

> [!tip]- Hints: route in the notes
> - Technique: K6
> - Steps 1–4 of [[§C5a.10 Normalization, Spin Sums and Helicity#^der-c5a-10-10|Derivation §C5a.10.10]].

### The helicity two-spinors

$\xi_\pm(\hat{\mathbf p})$ in polar angles with the stated phase convention, see Theorem [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-11|§C5a.10.11]] The Helicity Two-Spinors. → drilled as [[PHY 513 PS Drill#^ps5-6|PS5.6]].

^nd-thm-c5a-10-11

### Helicity spinors u± ★

With $\xi^s = \xi_\pm(\hat{\mathbf p})$ the roots act as numbers: $u_\pm = (\sqrt{E \mp \lvert\mathbf p\rvert}\,\xi_\pm, \sqrt{E \pm \lvert\mathbf p\rvert}\,\xi_\pm)$, $hu_\pm = \pm\frac12u_\pm$; with $\omega_\lambda = \sqrt{E + \lambda\lvert\mathbf p\rvert}$, $u_\lambda = (\omega_{-\lambda}\xi_\lambda, \omega_\lambda\xi_\lambda)$, see Theorem [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-12|§C5a.10.12]] Helicity Spinors u±. *Source: Problem Set 5, Problem 6 (context) · Yu (the helicity basis) · the user's notes Ch. 9 §9.4*

^nd-thm-c5a-10-12

- [ ] Q1 **[state]** Write $u_\pm$ in the helicity basis.
- [ ] Q2 What are $p\cdot\sigma\,\xi_\pm$ and $p\cdot\bar\sigma\,\xi_\pm$?
- [ ] Q3 Why do the square roots then act as numbers?
- [ ] Q4 **[conv]** Write $u_\lambda$ with Yu's $\omega_\lambda$; what is $\omega_\lambda\omega_{-\lambda}$?
- [ ] Q5 **[why]** Why do all normalizations and spin sums hold for this basis without recomputation?

> [!tip]- Hints: route in the notes
> - Technique: K4 (projectors)
> - Steps 1–4 of [[§C5a.10 Normalization, Spin Sums and Helicity#^der-c5a-10-12|Derivation §C5a.10.12]]; names: [[§C5a.9 Plane-Wave Solutions#^cau-c5a-9-3|§C5a.9, Caution: Names for the plane-wave spinors]].

### The v spinors in the helicity basis ★

With $\eta^s = \lambda\xi_{-\lambda}$, $v_\lambda = (\lambda\omega_\lambda\xi_{-\lambda}, -\lambda\omega_{-\lambda}\xi_{-\lambda})$ and $hv_\lambda = -\frac\lambda2v_\lambda$ (Yu's choice), see Theorem [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-13|§C5a.10.13]] The v Spinors in the Helicity Basis. *Source: Yu (the helicity basis) · the user's notes Ch. 9*

^nd-thm-c5a-10-13

- [ ] Q1 **[state]** Write $v_\lambda$ and its helicity.
- [ ] Q2 Act with the roots on $\xi_{-\lambda}$ and insert.
- [ ] Q3 **[why]** Why does $v_\lambda$ have helicity $-\lambda/2$ as a column, and why is that the right label for an antiparticle of helicity $\lambda$?
- [ ] Q4 **[conv]** Is $\{\lambda\xi_{-\lambda}\}$ the same as the Lecture 12 choice $\eta^s = \xi^{-s}$ for the helicity basis?

> [!tip]- Hints: route in the notes
> - Technique: K4
> - Steps 1–4 of [[§C5a.10 Normalization, Spin Sums and Helicity#^der-c5a-10-13|Derivation §C5a.10.13]]; Lecture 12's choice: Definition [[§C9.5 Charge Conjugation on Oscillators and Spinors#^def-c9-5-5|§C9.5.5]] The Antiparticle Two-Spinors η^s = ξ^{−s}.

### The massless and high-energy limit: helicity becomes chirality ★

At $m = 0$, $u_+ = \sqrt{2E}(0, \xi_+)$, $u_- = \sqrt{2E}(\xi_-, 0)$ and $\gamma^5u_\pm = \pm u_\pm$; for $E \gg m$ the other half is suppressed by $m/2E$, see Theorem [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-14|§C5a.10.14]] The Massless and High-Energy Limit: Helicity Becomes Chirality. *Source: PS §3.3 · the user's notes Ch. 9*

^nd-thm-c5a-10-14

- [ ] Q1 **[state]** State the massless limit of $u_\pm$ and their chirality.
- [ ] Q2 Which of $\sqrt{E \mp \lvert\mathbf p\rvert}$ vanishes at $m = 0$?
- [ ] Q3 For $m > 0$, estimate the small half: rationalize $E - \lvert\mathbf p\rvert$.
- [ ] Q4 **[why]** Why does helicity equal chirality only for massless (or ultra-relativistic) particles?

> [!tip]- Hints: route in the notes
> - Technique: K1
> - Steps 1–4 of [[§C5a.10 Normalization, Spin Sums and Helicity#^der-c5a-10-14|Derivation §C5a.10.14]]; [[§C5a.10 Normalization, Spin Sums and Helicity#^rem-c5a-10-4|§C5a.10, Remark: The mass is what connects the two chiral blocks]]; why "left-handed": [[§C5a.7 The Dirac Equation and Its Lagrangian#^rem-c5a-7-6|§C5a.7, Remark: Why "left-handed"]].

### Slash algebra ★

$\gamma^\mu\slashed a = 2a^\mu - \slashed a\gamma^\mu$, $\slashed a\slashed b + \slashed b\slashed a = 2a\cdot b$, $\slashed a\slashed b = a\cdot b - i\sigma^{\mu\nu}a_\mu b_\nu$, see Theorem [[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-1|§C5a.11.1]] Slash Algebra. *Source: the user's notes Ch. 9 §9.6 · Problem Set 5*

^nd-thm-c5a-11-1

- [ ] Q1 **[state]** State the slash identities.
- [ ] Q2 Contract the Clifford relation with $a_\nu$ and with $a_\mu b_\nu$.
- [ ] Q3 Split $\gamma^\mu\gamma^\nu$ into symmetric and antisymmetric parts to get the last identity.
- [ ] Q4 **[conv]** Which normalization of $\sigma^{\mu\nu}$ makes the coefficient $-i$?

> [!tip]- Hints: route in the notes
> - Technique: K5
> - [[§C5a.11 Gamma-Matrix Technology#^der-c5a-11-1|Derivation §C5a.11.1]]; normalizations: [[§C5a.6 The Dirac Conjugate and the Bilinears#^cau-c5a-6-1|§C5a.6, Caution: Three normalizations of σ^μν]].

### Contraction identities, γ⁵ identities, Gordon

$\gamma_\mu\gamma^\mu = 4$ etc. (Theorem [[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-2|§C5a.11.2]] Contraction Identities) → drilled as [[PHY 513 PS Drill#^ps5-2|PS5.2]] and [[PHY 513 PS Drill#^ps7-1-c|PS7.1(c)]]; properties of $\gamma^5$ (Theorem [[§CB.12 Clifford Algebras꞉ Grading, Basis and the Volume Element#^thm-cb-12-15|§CB.12.15]] Algebraic Properties of γ⁵) → drilled as [[PHY 513 PS Drill#^ps5-5-a|PS5.5(a)]], [[PHY 513 PS Drill#^ps5-5-b|PS5.5(b)]]; $\gamma^5$ as the antisymmetric product and duality (Theorem [[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-5|§C5a.11.5]] γ⁵ as a Totally Antisymmetric Product, Theorem [[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-6|§C5a.11.6]] The Antisymmetric Product of Three γ's, Theorem [[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-7|§C5a.11.7]] γ⁵ Dualizes σ^μν) → drilled as [[PHY 513 PS Drill#^ps5-5-c|PS5.5(c)]], [[PHY 513 PS Drill#^ps5-5-d|PS5.5(d)]]; the Gordon identity (Theorem [[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-9|§C5a.11.9]] The Gordon Identity) → drilled as [[PHY 513 PS Drill#^ps5-3|PS5.3]].

^nd-thm-c5a-11-2

### Traces of γ matrices ★

$\operatorname{tr}\mathbb 1 = 4$; traces of an odd number of $\gamma$'s vanish; $\operatorname{tr}(\gamma^\mu\gamma^\nu) = 4g^{\mu\nu}$; $\operatorname{tr}(\gamma^\mu\gamma^\nu\gamma^\rho\gamma^\sigma) = 4(g^{\mu\nu}g^{\rho\sigma} - g^{\mu\rho}g^{\nu\sigma} + g^{\mu\sigma}g^{\nu\rho})$, see Theorem [[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-3|§C5a.11.3]] Traces of γ Matrices. *Source: Lecture 9, slide "Solution of The Dirac Equation: Step 2" ($\operatorname{tr}(\gamma^\mu p_\mu) = 0$) · Yu §7.1, §8.2.2 · PS §5.1 (statements)*

^nd-thm-c5a-11-3

- [ ] Q1 **[state]** State the four trace rules.
- [ ] Q2 Why does the trace of an odd number of $\gamma$'s vanish (insert $(\gamma^5)^2$)?
- [ ] Q3 Derive $\operatorname{tr}(\gamma^\mu\gamma^\nu)$ from cyclicity and the anticommutator.
- [ ] Q4 Derive the four-$\gamma$ trace by anticommuting the first $\gamma$ to the end. Why do the signs alternate?
- [ ] Q5 **[why]** Why do these traces not depend on the basis?

> [!tip]- Hints: route in the notes
> - Technique: K5 (traces)
> - [[§C5a.11 Gamma-Matrix Technology#^der-c5a-11-3|Derivation §C5a.11.3]]; basis independence: Theorem [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-15|§CB.0.15]] Trace, Determinant and Eigenvalues Do Not Depend on the Basis.

### Traces with γ⁵ ★

$\operatorname{tr}\gamma^5 = 0$, $\operatorname{tr}(\gamma^\mu\gamma^\nu\gamma^5) = 0$, $\operatorname{tr}(\gamma^\mu\gamma^\nu\gamma^\rho\gamma^\sigma\gamma^5) = -4i\varepsilon^{\mu\nu\rho\sigma}$ with $\varepsilon^{0123} = +1$; convention-free $\operatorname{tr}(\gamma^0\gamma^1\gamma^2\gamma^3\gamma^5) = -4i$, see Theorem [[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-4|§C5a.11.4]] Traces with γ⁵. *Source: Yu §8.2.2 · PS §5.1 (statements)*

^nd-thm-c5a-11-4

- [ ] Q1 **[state]** State the three traces with $\gamma^5$.
- [ ] Q2 Why does $\operatorname{tr}(\gamma^\mu\gamma^\nu\gamma^5)$ vanish?
- [ ] Q3 Evaluate $\operatorname{tr}(\gamma^0\gamma^1\gamma^2\gamma^3\gamma^5)$ from the definition of $\gamma^5$.
- [ ] Q4 **[conv]** PS take $\varepsilon^{0123} = -1$. What is the sign of the $\varepsilon$ trace there, and which pages of PS are internally inconsistent?

> [!tip]- Hints: route in the notes
> - Technique: K5
> - [[§C5a.11 Gamma-Matrix Technology#^der-c5a-11-4|Derivation §C5a.11.4]]; [[§C5a.11 Gamma-Matrix Technology#^cau-c5a-11-1|§C5a.11, Caution: The sign of the ε trace across sources]]; [[Larsen PHY 513|register: Levi-Civita]].

### Every product of γ's reduces to the standard basis ★

A product of $n$ $\gamma$'s is a unique combination, with coefficients from $g$ and $\varepsilon$, of $\mathbb 1$, $\gamma^\mu$, $\sigma^{\mu\nu}$, $\gamma^\mu\gamma^5$, $\gamma^5$, only of the parity of $n$, see Theorem [[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-8|§C5a.11.8]] Every Product of γ's Reduces to the Standard Basis. *Source: Problem Set 5, Problem 5 (closing paragraph of the statement) · the user's notes Ch. 9 §9.6*

^nd-thm-c5a-11-8

- [ ] Q1 **[state]** State the reduction theorem.
- [ ] Q2 Describe the algorithm: what is done to two adjacent $\gamma$'s?
- [ ] Q3 Why do fully antisymmetric products of five or more $\gamma$'s vanish, and what are those of three and four?
- [ ] Q4 **[why]** Why is the combination unique (what do the sixteen matrices form)?

> [!tip]- Hints: route in the notes
> - Technique: K5
> - [[§C5a.11 Gamma-Matrix Technology#^der-c5a-11-8|Derivation §C5a.11.8]]; three and four: Theorem [[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-5|§C5a.11.5]] γ⁵ as a Totally Antisymmetric Product, Theorem [[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-6|§C5a.11.6]] The Antisymmetric Product of Three γ's; basis: Theorem [[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-18-14|§CB.18.14]] Cl(1,3) ≅ ΛV as a Representation; the Sixteen Bilinears.

# T9. Quantization of the Dirac field

## Definitions and conventions T9

### Names and hats for the Dirac field across sources

The course writes $\hat\psi$, $\hat a^s_{\mathbf p}$, $\hat b^s_{\mathbf p}$ with hats on operators and $\Pi_\psi$ for the momentum density; the notes write $\pi$; PS uses a provisional labelling on pp. 52–57 before eq. (3.99); Yu labels by helicity, see [[§C5b.1 Canonical Quantization of the Dirac Field#^cau-c5b-1-1|§C5b.1, Caution: Names for the Dirac field and its mode operators across sources]]. *Source: Lecture 10 (Oct 5), slides 10, 20 · the user's notes Ch. 10 · PS §3.5 · register row "Dirac field and mode operators"*

^nd-cau-c5b-1-1

- [ ] Q1 **[def]** Write the course's mode expansion of $\hat\psi(x)$ from memory: measure, sum, both terms, which spinor goes with which operator and which exponential.
- [ ] Q2 **[conv]** Which symbols do the slides, these notes, PS and Yu use for the momentum density, the antifermion annihilator and the spin label?
- [ ] Q3 **[conv]** Which labelling of PS §3.5 must be forgotten after eq. (3.99), and why does it differ from the final one?
- [ ] Q4 **[conv]** What does the superscript $c$ in $|\mathbf p, s\rangle^c$ stand for, and how does PS name the antifermion state?
- [ ] Q5 **[why]** Which objects carry a hat and which do not ($u^s(p)$, $v^s(p)$, $\gamma^\mu$, the classical $\psi$)?

> [!tip]- Hints: route in the notes
> - Technique: none (convention recall).
> - The caution's table: lecture vs notes vs PS vs Yu; hats on operators only (register row "Operators").
> - PS's provisional $b^s_{-\mathbf p}$ (3.87) and $\tilde b = b^\dagger$ (3.98) are superseded at (3.99).

### Equal-time canonical anticommutation relations

The Dirac field is quantized by $\{\hat\psi_a(\mathbf x), \hat\psi^\dagger_b(\mathbf y)\} = \delta_{ab}\delta^3(\mathbf x - \mathbf y)$, $\{\hat\psi, \hat\psi\} = \{\hat\psi^\dagger, \hat\psi^\dagger\} = 0$, equivalently $\{\hat\psi_a, \hat\pi_b\} = i\delta_{ab}\delta^3$ with $\hat\pi = i\hat\psi^\dagger$, see Principle [[§C5b.1 Canonical Quantization of the Dirac Field#^pr-c5b-1-6|§C5b.1.6]] Equal-Time Canonical Anticommutation Relations. *Source: Lecture 10 (Oct 5), slides 5–6, 23 · the user's notes Ch. 10 §10.1 · PS §3.5 · Yu (5.238)–(5.239)*

^nd-pr-c5b-1-6

- [ ] Q1 **[def]** State the three equal-time relations exactly, with spinor indices, and define $\{A, B\}$.
- [ ] Q2 **[def]** What is the "provisional" quantization of slide 5, and why did the slide call it "strange"?
- [ ] Q3 Rewrite the momentum form $\{\hat\psi_a, \hat\pi_b\} = i\delta_{ab}\delta^3$ as a field–field relation: where does the factor $i$ go?
- [ ] Q4 **[why]** Name the two "serious problems" (slide 6) that the commutator version has and that anticommutators fix.
- [ ] Q5 **[why]** Which name is attached to quantization with anticommutators, and what is left unfixed by the principle (operator ordering in $\hat H$)?
- [ ] Q6 **[conv]** In what sense are these relations identities: what is the value of $\{\hat\psi_a(\mathbf x), \hat\psi^\dagger_a(\mathbf x)\}$ at coinciding points, and what does smearing change?

> [!tip]- Hints: route in the notes
> - Technique: K11 ((anti)commutator algebra).
> - Momentum form ⇔ field form: Theorem [[§C5b.1 Canonical Quantization of the Dirac Field#^thm-c5b-1-1|§C5b.1.1]] The Conjugate Momentum Field of the Dirac Field, part 3.
> - Why strange: [[§C5b.1 Canonical Quantization of the Dirac Field#^rem-c5b-1-4|§C5b.1, Remark: Larsen's puzzle, a field–field relation that is canonical]] and [[§C5b.1 Canonical Quantization of the Dirac Field#^cau-c5b-1-2|§C5b.1, Caution: The provisional commutator quantization, and why it is strange]].
> - The two problems: Theorem [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-3|§C5b.3.3]] Commutators Allow No Positive Norm with Positive Energy (positivity) and Theorem [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-5|§C5b.7.5]] A Dirac Field with Commutators Is Not Causal (causality).
> - Smearing: Theorem [[§C5b.1 Canonical Quantization of the Dirac Field#^thm-c5b-1-8|§C5b.1.8]] The Anticommutators Are Identities after Smearing; Smeared Fermi Fields Are Bounded.

### The spin–statistics theorem as the course states it

Fields of integer spin are quantized with commutators (bosons), fields of half-odd-integer spin with anticommutators (fermions), given locality, Lorentz invariance, positivity and causal propagation; stated, not proved, see Principle [[§C5b.1 Canonical Quantization of the Dirac Field#^pr-c5b-1-7|§C5b.1.7]] The Spin–Statistics Theorem. *Source: Lecture 10 (Oct 5), slide 7 ("The proof is complicated") · PS §3.5, pp. 57–58*

^nd-pr-c5b-1-7

- [ ] Q1 **[state]** List the ingredients of the theorem as slide 7 gives them, and state the claim for integer and for half-odd-integer $s$.
- [ ] Q2 **[def]** What does "local QFT" mean on slide 7?
- [ ] Q3 **[def]** What does "causal propagation" require of the commutator or anticommutator?
- [ ] Q4 **[why]** Slide 7's "key issue": why does a first-order equation of motion make the momentum proportional to the field itself, and why does that matter?
- [ ] Q5 **[why]** Which two checks does the course make for the free Dirac field instead of the general proof, and which for the scalar?
- [ ] Q6 **[why]** In nonrelativistic QM the exclusion principle is a postulate. In what sense is it an output here?

> [!tip]- Hints: route in the notes
> - Technique: K14 (microcausality) for the causal check.
> - The free fields are checked in Theorem [[§C5b.9 Spin and Statistics#^thm-c5b-9-1|§C5b.9.1]] The Free Fields of the Course Obey the Spin–Statistics Theorem: positivity (Theorem [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-3|§C5b.3.3]] Commutators Allow No Positive Norm with Positive Energy) and causality (Theorem [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-5|§C5b.7.5]] A Dirac Field with Commutators Is Not Causal).
> - Key issue: $\pi_\psi = i\psi^\dagger$ (Theorem [[§C5b.1 Canonical Quantization of the Dirac Field#^thm-c5b-1-1|§C5b.1.1]] The Conjugate Momentum Field of the Dirac Field), not a velocity.
> - Output, not postulate: [[§C5b.1 Canonical Quantization of the Dirac Field#^rem-c5b-1-6|§C5b.1, Remark: Spin and statistics are an output]].

### Mode expansion of the Dirac field

$\hat\psi(x) = \int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}\sum_{s=1,2}\bigl(\hat a^s_{\mathbf p}u^s(p)e^{-ip\cdot x} + \hat b^{s\dagger}_{\mathbf p}v^s(p)e^{ip\cdot x}\bigr)$, $p^0 = E_{\mathbf p}$, see Theorem [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-1|§C5b.2.1]] Mode Expansion of the Dirac Field. *Source: Lecture 10 (Oct 5), slides 10–11, 23 · PS eq. (3.99) · Yu (5.216)*

^nd-thm-c5b-2-1

- [ ] Q1 **[def]** Write the expansion and state which spinors $u^s(p)$, $v^s(p)$ (from C5a) appear and what $p^0$ is.
- [ ] Q2 **[why]** Why does a complete basis of solutions need both frequencies and both spins?
- [ ] Q3 **[why]** Why are $\hat a$ and $\hat b^\dagger$ independent, as for the complex scalar (PS Problem 2.2)?
- [ ] Q4 **[why]** Why is the measure $\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}$ the scalar's, and why does the quantum field satisfy the Dirac equation?
- [ ] Q5 **[why]** In which picture is this expansion written (where is the time dependence)?
- [ ] Q6 The lecture posited the expansion; the notes derive it from the classical solutions. Outline that derivation: Fourier transform in space, diagonalize $H_{\rm s.p.}(\mathbf p)$, solve the ODE, relabel $\mathbf p \to -\mathbf p$.

> [!tip]- Hints: route in the notes
> - Technique: K9 (mode substitution).
> - Reading the expansion: [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^rem-c5b-2-1|§C5b.2, Remark: Reading the expansion]].
> - Derivation steps 1–5 under Theorem [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-1|§C5b.2.1]] Mode Expansion of the Dirac Field: $H_{\rm s.p.}(\mathbf p)^2 = E_{\mathbf p}^2$, eigenvectors $u^s(p)$ and $v^s(\tilde p)$, phases $e^{\mp iE_{\mathbf p}t}$, then $\mathbf p \to -\mathbf p$ in the second term.
> - Heisenberg picture: Theorem [[§C5b.6 The Heisenberg Dirac Field#^thm-c5b-6-1|§C5b.6.1]] Time Dependence of the Modes; the Covariant Mode Expansion.

### What anticommutes and what does not

The operators $\hat\psi$, $\hat a$, $\hat b$ and their adjoints anticommute; $u^s(p)$, $v^s(p)$ and the exponentials are ordinary c-numbers; $\bar uu$ is a number, $u\bar u$ a $4\times4$ matrix, see [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^cau-c5b-2-1|§C5b.2, Caution: What anticommutes and what does not]]. *Source: Lecture 10 (Oct 5), slide 22 · the user's notes Ch. 10*

^nd-cau-c5b-2-1

- [ ] Q1 **[def]** Which objects in $\hat\psi$ are operators and which are c-numbers?
- [ ] Q2 **[why]** May $\hat a\,u_a$ be written $u_a\,\hat a$? May $\hat a\hat b^\dagger$ be written $\hat b^\dagger\hat a$?
- [ ] Q3 **[conv]** Distinguish "matrix order" from "quantum order" in $\hat\psi^\dagger H_{\rm s.p.}\hat\psi$.
- [ ] Q4 In components, what is the $b$-th entry of $\hat\psi^\dagger$ and why does no row-versus-column question arise?

> [!tip]- Hints: route in the notes
> - Technique: K11.
> - The caution's four rules; component form: [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^rem-c5b-2-3|§C5b.2, Remark: A spinor-valued operator, component by component]].

### Normal ordering of fermion operators

$:\!X\!:$ puts creation operators left of annihilation operators with a factor $-1$ for every exchange of two fermion operators; so $:\!\hat b\hat b^\dagger\!: = -\hat b^\dagger\hat b$, see Definition [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^def-c5b-3-1|§C5b.3.1]] Normal Ordering of Fermion Operators. *Source: Lecture 10 (Oct 5), slide 19 and transcript · PS §3.5 · register row "Dirac states and normal ordering"*

^nd-def-c5b-3-1

- [ ] Q1 **[def]** State the definition, including the sign rule, and contrast it with the bosonic one.
- [ ] Q2 Compute $:\!\hat b^s_{\mathbf p}\hat b^{s\dagger}_{\mathbf p}\!:$ and $:\!\hat a^{s\dagger}_{\mathbf p}\hat a^s_{\mathbf p}\!:$.
- [ ] Q3 **[why]** Why is the vacuum expectation value of a normal-ordered product zero?
- [ ] Q4 **[why]** Why is the reordering constant dropped for $\hat H$ but would be observable for $\hat Q$?

> [!tip]- Hints: route in the notes
> - Technique: K11.
> - Uses: Theorem [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-5|§C5b.3.5]] The Hamiltonian of the Dirac Field (energy), Theorem [[§C5b.5 The U(1) Charge, Particles and Antiparticles#^thm-c5b-5-3|§C5b.5.3]] The Charge Counts Fermions Minus Antifermions and [[§C5b.5 The U(1) Charge, Particles and Antiparticles#^rem-c5b-5-1|§C5b.5, Remark: The vacuum charge, and why the order is forced]] (charge).

### The Dirac vacuum and the fermionic Fock space

There is a unique normalized $|0\rangle$ with $\hat a^s_{\mathbf p}|0\rangle = \hat b^s_{\mathbf p}|0\rangle = 0$, and the states form the Fock space of antisymmetric powers of the one-fermion and one-antifermion spaces, see Principle [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^pr-c5b-3-4|§C5b.3.4]] The Dirac Vacuum and the Fermionic Fock Space. *Source: Lecture 10 (Oct 5), slides 20–21 · PS §3.5, eq. (3.103)*

^nd-pr-c5b-3-4

- [ ] Q1 **[def]** State which operators annihilate the vacuum and what the space of states is.
- [ ] Q2 **[def]** What is the one-particle space $\mathcal H_1$ (labels, measure)?
- [ ] Q3 **[why]** What fixes that $\hat b$, and not $\hat b^\dagger$, annihilates the vacuum?
- [ ] Q4 **[why]** How are inner products of Fock states computed, and where do signs come from?

> [!tip]- Hints: route in the notes
> - Technique: K11.
> - Positivity: Theorem [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-3|§C5b.3.3]] Commutators Allow No Positive Norm with Positive Energy; empty vs filled: [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^rem-c5b-3-4|§C5b.3, Remark: Empty and filled are labels]].

### The U(1) charge of the Dirac field

$\hat Q = \int d^3x\,\hat{\bar\psi}\gamma^0\hat\psi = \int d^3x\,\hat\psi^\dagger\hat\psi$, normalized as in PS; the Noether charge of $\psi \to e^{i\alpha}\psi$ in the course's sign convention is $-\hat Q$, see Definition [[§C5b.5 The U(1) Charge, Particles and Antiparticles#^def-c5b-5-1|§C5b.5.1]] The U(1) Charge of the Dirac Field. *Source: PS §3.5, p. 62, eq. (3.113) · Problem Set 6, Problem 2*

^nd-def-c5b-5-1

- [ ] Q1 **[def]** Define $\hat Q$ as the integral of the time component of which current?
- [ ] Q2 **[conv]** How is $\hat Q$ related in sign and normalization to the Noether charge of the phase rotation (C1b convention)?
- [ ] Q3 **[why]** Why is $\hat Q$ fixed as an operator only after an ordering prescription?

> [!tip]- Hints: route in the notes
> - Technique: K12 (Noether recipe).
> - Current: Theorem [[§C5a.8 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-8-3|§C5a.8.3]] The Vector Current; sign: [[§C1b.6 Conserved Charges and Internal Symmetries#^cau-c1b-6-3|§C1b.6, Caution: Sign and normalization of the U(1) current]].

### Time-ordered product of fermion fields

$T\{\hat\psi_a(x)\hat{\bar\psi}_b(y)\} = \theta(x^0 - y^0)\hat\psi_a(x)\hat{\bar\psi}_b(y) - \theta(y^0 - x^0)\hat{\bar\psi}_b(y)\hat\psi_a(x)$, a sign for each transposition of fermion fields, see Definition [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^def-c5b-8-2|§C5b.8.2]] Time-Ordered Product of Fermion Fields. *Source: PS §3.5, eq. (3.121) and the text after it (reading; not on the slides)*

^nd-def-c5b-8-2

- [ ] Q1 **[def]** State the definition for two fields and the rule for $n$ fields.
- [ ] Q2 **[why]** Why the minus sign: what would go wrong at spacelike separation with a plus sign?
- [ ] Q3 **[conv]** How does it reduce to the bosonic definition for scalar fields?

> [!tip]- Hints: route in the notes
> - Technique: K14 (frame independence).
> - Frame independence: Theorem [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-2|§C5b.8.2]] Fermionic Time Ordering Is Frame Independent (spacelike: anticommutator vanishes, Theorem [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-3|§C5b.7.3]] Microcausality of the Dirac Field).

### Dirac Wightman functions and the anticommutator function

$S^+_W(x - y) = \langle0|\hat\psi(x)\hat{\bar\psi}(y)|0\rangle$, $S^-_W(x - y) = \langle0|\hat{\bar\psi}(y)\hat\psi(x)|0\rangle$, and $iS(x - y) = \langle0|\{\hat\psi(x), \hat{\bar\psi}(y)\}|0\rangle$, see Definition [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^def-c5b-7-1|§C5b.7.1]] Dirac Wightman Functions and Definition [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^def-c5b-7-2|§C5b.7.2]] Anticommutator Function. *Source: Lecture 10 (Oct 5), transcript ("causality checkpoint") · PS §3.5, eqs. (3.114)–(3.117)*

^nd-def-c5b-7-2

- [ ] Q1 **[def]** Define $S^\pm_W$ and $S$, with index placement and the order of the fields.
- [ ] Q2 **[conv]** What is the scalar analogue of $S$, and with which factor of $i$ is it defined?
- [ ] Q3 **[why]** Why are these $4\times4$ matrices of distributions in $\xi = x - y$ only?
- [ ] Q4 **[conv]** The letter $S$ means several things in this chapter: list them.

> [!tip]- Hints: route in the notes
> - Scalar: $iD = \langle0|[\hat\phi, \hat\phi]|0\rangle$, Definition [[§C2b.4 Microcausality and the Commutator Function#^def-c2b-4-1|§C2b.4.1]] Commutator Function.
> - The letter: [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^cau-c5b-7-1|§C5b.7, Caution: The letter S]].

## Derivations T9

### The conjugate momentum of the Dirac field ★★

$\pi_\psi = \partial\mathcal L/\partial\dot\psi = i\psi^\dagger$, $\pi_{\bar\psi} = 0$; a relation between canonical variables, not a new field, see Theorem [[§C5b.1 Canonical Quantization of the Dirac Field#^thm-c5b-1-1|§C5b.1.1]] The Conjugate Momentum Field of the Dirac Field. *Source: Lecture 10 (Oct 5), slide 5 · the user's notes Ch. 10 §10.1 · PS §3.5, p. 52*

^nd-thm-c5b-1-1

- [ ] Q1 **[state]** State the momenta of $\psi$ and of $\bar\psi$ for $\mathcal L = \bar\psi(i\gamma^\mu\partial_\mu - m)\psi$.
- [ ] Q2 Which term of $\mathcal L$ contains $\dot\psi$, and what does the $\gamma^0$ of that term do against the $\gamma^0$ in $\bar\psi$?
- [ ] Q3 **[why]** For the scalar, $\pi = \dot\phi$ is solved for the velocity. Why can that not be done here, and what does it mean that $\psi^\dagger$ is "not a further coordinate"?
- [ ] Q4 Insert $\hat\pi = i\hat\psi^\dagger$ into $\{\hat\psi_a, \hat\pi_b\} = i\delta_{ab}\delta^3$ and into $\{\hat\pi_a, \hat\pi_b\} = 0$: what field–field relations result?
- [ ] Q5 Why does $\hat{\bar\psi}$ need no relation of its own?
- [ ] Q6 **[why]** Slide 5 says "treat $\psi$ and $\psi^\dagger$ as independent fields". In what sense is that right, and in what sense is $\psi^\dagger$ not independent?

> [!tip]- Hints: route in the notes
> - Technique: K11.
> - Steps 1–6 of the derivation under Theorem [[§C5b.1 Canonical Quantization of the Dirac Field#^thm-c5b-1-1|§C5b.1.1]] The Conjugate Momentum Field of the Dirac Field; the recalled momenta Theorem [[§C5a.8 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-8-1|§C5a.8.1]] Canonical Momenta of the Dirac Field.
> - Partner field: [[§C5b.1 Canonical Quantization of the Dirac Field#^rem-c5b-1-2|§C5b.1, Remark: ψ† or ψ̄ as the partner field, one canonical structure]]; first-order system: [[§C5b.1 Canonical Quantization of the Dirac Field#^rem-c5b-1-3|§C5b.1, Remark: A first-order system: the momentum is ψ† itself]].
> - Not a velocity, not $\bar\psi$, not the field momentum: [[§C5b.1 Canonical Quantization of the Dirac Field#^rem-c5b-1-5|§C5b.1, Remark: What the conjugate momentum is not, for spinors]].

### Hamilton's equations of the Dirac field ★

With $H[\psi, \pi] = \int d^3x\,(-i\pi)H_{\rm s.p.}\psi$, Hamilton's equations are $\dot\psi = -iH_{\rm s.p.}\psi$ and its adjoint: one complex equation, the Dirac equation, see Theorem [[§C5b.1 Canonical Quantization of the Dirac Field#^thm-c5b-1-3|§C5b.1.3]] Hamilton's Equations of the Dirac Field. *Source: PS §3.5, eqs. (3.84)–(3.85) · the user's notes Ch. 10*

^nd-thm-c5b-1-3

- [ ] Q1 **[state]** Write $H$ as a functional of $\psi$ and $\pi$.
- [ ] Q2 Compute $\delta H/\delta\pi_b$ and read off the first Hamilton equation; multiply by $i$ and by $\gamma^0$: which equation is it?
- [ ] Q3 Compute $-\delta H/\delta\psi_c$ (integrate the derivative term by parts) and insert $\pi = i\psi^\dagger$.
- [ ] Q4 **[why]** Why are the two Hamilton equations one complex equation and not two independent ones?

> [!tip]- Hints: route in the notes
> - Technique: K2 (index calculus).
> - Steps 1–6 of the derivation under Theorem [[§C5b.1 Canonical Quantization of the Dirac Field#^thm-c5b-1-3|§C5b.1.3]] Hamilton's Equations of the Dirac Field; $H_{\rm s.p.}$: Definition [[§C5a.7 The Dirac Equation and Its Lagrangian#^def-c5a-7-3|§C5a.7.3]] Single-Particle Hamiltonian.

### Fields ⇔ oscillators: the mode algebra ★★ [class exercise, Lecture 10]

$\{\hat a^r_{\mathbf p}, \hat a^{s\dagger}_{\mathbf q}\} = \{\hat b^r_{\mathbf p}, \hat b^{s\dagger}_{\mathbf q}\} = (2\pi)^3\delta^{rs}\delta^3(\mathbf p - \mathbf q)$, all others zero, is equivalent to the equal-time field anticommutators, see Theorem [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-4|§C5b.2.4]] The Mode Algebra of the Dirac Field. *Source: Lecture 10 (Oct 5), slides 12–13 (oscillators ⇒ fields); the converse left ("technically, we should also go the other way around … you did that in an exercise for the scalar fields"); transcript: "strongly encouraged to write down these guys at home without looking at your notes"*

^nd-thm-c5b-2-4

- [ ] Q1 **[state]** State the oscillator anticommutators and the field anticommutators that they are equivalent to.
- [ ] Q2 Write both expansions at $t = 0$ with a common Fourier factor $e^{i\mathbf p\cdot\mathbf x}$: what is relabelled in the antiparticle term, and why is that allowed?
- [ ] Q3 Operators first: which of the four products of mode operators survive in $\{\hat\psi_a(\mathbf x), \hat\psi^\dagger_b(\mathbf y)\}$?
- [ ] Q4 Spin sum: combine $\sum_s u^s_a u^{s\dagger}_b$ and $\sum_s v^s_a(\tilde p)v^{s\dagger}_b(\tilde p)$ using the completeness relations for $u\bar u$ and $v\bar v$. Where does the $\gamma^0$ go, and what is the result?
- [ ] Q5 Last, the Fourier integral: what is left?
- [ ] Q6 **[class exercise]** Converse: extract $\hat a$ and $\hat b^\dagger$ from $\hat\psi$ and compute $\{\hat a, \hat a^\dagger\}$ and $\{\hat b, \hat b^\dagger\}$ from the field relation. In which order does the field relation enter for $\hat b$?
- [ ] Q7 **[why]** Why do $\{\hat a, \hat b\}$ and $\{\hat a, \hat b^\dagger\}$ vanish?

> [!tip]- Hints: route in the notes
> - Technique: K9 (relabel $\mathbf p \to -\mathbf p$), K10 (extraction), K11.
> - Slides' direction: second route under Theorem [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-4|§C5b.2.4]] The Mode Algebra of the Dirac Field, steps 1–5; spin sums Theorem [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-7|§C5a.10.7]] The Spin Sum over u, Theorem [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-8|§C5a.10.8]] The Spin Sum over v; "one thing at a time": [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^rem-c5b-2-6|§C5b.2, Remark: One thing at a time]].
> - Converse: first route, steps 1–5, with Theorem [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-3|§C5b.2.3]] Mode Extraction.

### The conjugate fields ψ† and ψ̄ in modes ★★

$\hat\psi^\dagger = \int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}\sum_s\bigl(\hat a^{s\dagger}_{\mathbf p}u^{s\dagger}(p)e^{ip\cdot x} + \hat b^s_{\mathbf p}v^{s\dagger}(p)e^{-ip\cdot x}\bigr)$ and $\hat{\bar\psi}$ with $\bar u$, $\bar v$; $\hat{\bar\psi}$ is $\hat\psi$ with particles and antiparticles interchanged, see Theorem [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-2|§C5b.2.2]] The Conjugate Fields ψ† and ψ̄. *Source: Lecture 10 (Oct 5), slide 22 · PS §3.5 · Yu (5.217)–(5.218)*

^nd-thm-c5b-2-2

- [ ] Q1 **[state]** Write $\hat{\bar\psi}(x)$ in modes.
- [ ] Q2 Take the adjoint of one term $c\,\hat A\,w$: what happens to the number, the operator and the column?
- [ ] Q3 Multiply by $\gamma^0$ on the right: which barred spinors appear?
- [ ] Q4 **[why]** Which operators does $\hat{\bar\psi}$ annihilate and create, and why do $\hat\psi^\dagger$ and $\hat{\bar\psi}$ have the same operator content?
- [ ] Q5 **[why]** "Particles and antiparticles are physically equivalent": which later symmetry makes that explicit?

> [!tip]- Hints: route in the notes
> - Technique: K9.
> - Steps 1–5 under Theorem [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-2|§C5b.2.2]] The Conjugate Fields ψ† and ψ̄; interchange: [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^rem-c5b-2-2|§C5b.2, Remark: ψ̄ is ψ with particles and antiparticles interchanged]]; made explicit by charge conjugation, Theorem [[§C9.6 Charge Conjugation on the Field and Bilinears#^thm-c9-6-3|§C9.6.3]] Charge Conjugation through the Dirac Conjugate.

### Mode extraction ★ [class exercise, Lecture 10]

$\hat a^s_{\mathbf p} = \frac{1}{\sqrt{2E_{\mathbf p}}}\int d^3x\,e^{ip\cdot x}u^{s\dagger}(p)\hat\psi(x)$, $\hat b^{s\dagger}_{\mathbf p} = \frac{1}{\sqrt{2E_{\mathbf p}}}\int d^3x\,e^{-ip\cdot x}v^{s\dagger}(p)\hat\psi(x)$, independent of $t$, see Theorem [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-3|§C5b.2.3]] Mode Extraction. *Source: needed for the converse direction left in Lecture 10 (transcript; done for the scalar in Problem Set 3) · the user's notes Ch. 10*

^nd-thm-c5b-2-3

- [ ] Q1 **[state]** Write the extraction formulas for $\hat a$ and $\hat b^\dagger$, and say from which field $\hat a^\dagger$ and $\hat b$ come.
- [ ] Q2 Substitute the expansion and split the exponentials: which $d^3x$ integrals appear?
- [ ] Q3 Integrate the deltas over $\mathbf q$: where is $\mathbf q = \mathbf p$ and where $\mathbf q = -\mathbf p$, and what happens to the time phases?
- [ ] Q4 Which orthogonality relations ($u^\dagger u$, $u^\dagger v$ at flipped momentum) finish the computation?
- [ ] Q5 **[why]** Why is the inner product used here positive, unlike the Klein–Gordon product of the scalar?

> [!tip]- Hints: route in the notes
> - Technique: K10 (extracting mode operators: $u^\dagger$, $v^\dagger$ orthogonality).
> - Steps 1–6 under Theorem [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-3|§C5b.2.3]] Mode Extraction; orthogonality Theorem [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-1|§C5a.10.1]] u†u = 2E; positive product [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^rem-c5b-2-5|§C5b.2, Remark: A positive inner product]].

### Commutators give the antiparticle modes a negative algebra ★

With the bosonic rule $[\hat\psi_a, \hat\psi^\dagger_b] = \delta_{ab}\delta^3$, the modes obey $[\hat a, \hat a^\dagger] = +(2\pi)^3\delta\delta$ but $[\hat b, \hat b^\dagger] = -(2\pi)^3\delta\delta$, see Theorem [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-5|§C5b.2.5]] Commutators Give the Antiparticle Modes a Negative Algebra. *Source: Lecture 10 (Oct 5), slide 6 · PS §3.5, eqs. (3.86)–(3.90)*

^nd-thm-c5b-2-5

- [ ] Q1 **[state]** State the commutators of the mode operators that follow from commutator quantization.
- [ ] Q2 From which field is $\hat b$ extracted, and from which $\hat b^\dagger$?
- [ ] Q3 So $[\hat b, \hat b^\dagger]$ contains the canonical relation in which order? Compute its sign.
- [ ] Q4 **[why]** Why does the same exchange cost nothing for an anticommutator?
- [ ] Q5 **[why]** Compare with the complex scalar: why is there no minus sign there?

> [!tip]- Hints: route in the notes
> - Technique: K10, K11.
> - Steps 1–3 under Theorem [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-5|§C5b.2.5]] Commutators Give the Antiparticle Modes a Negative Algebra; "one algebraic fact": [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^rem-c5b-2-7|§C5b.2, Remark: One algebraic fact]].

### The single-particle Hamiltonian on plane waves ★★

$H_{\rm s.p.} = \gamma^0(-i\boldsymbol\gamma\cdot\nabla + m)$ has $H_{\rm s.p.}u^s(p)e^{-ip\cdot x} = +E_{\mathbf p}u^s(p)e^{-ip\cdot x}$ and $H_{\rm s.p.}v^s(p)e^{ip\cdot x} = -E_{\mathbf p}v^s(p)e^{ip\cdot x}$, see Theorem [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-1|§C5b.3.1]] The Single-Particle Hamiltonian on Plane Waves. *Source: Lecture 10 (Oct 5), slides 16–17 · PS §3.5, p. 53 ($h_D$, eq. (3.85))*

^nd-thm-c5b-3-1

- [ ] Q1 **[def]** Define $H_{\rm s.p.}$ from the Hamiltonian density $\mathcal H = \pi\dot\psi - \mathcal L$.
- [ ] Q2 Split the Dirac equation into its time part and space part and multiply by $\gamma^0$: what equation does a solution satisfy?
- [ ] Q3 Act with $i\partial_0$ on $e^{-ip\cdot x}$ and on $e^{ip\cdot x}$: which eigenvalues?
- [ ] Q4 **[why]** The time derivative was removed from $\mathcal H$. Why can the eigenvalue still be read off from $i\partial_t$?
- [ ] Q5 **[why]** Why are negative eigenvalues a problem only if $\psi$ is a wave function (slide 17)?

> [!tip]- Hints: route in the notes
> - Technique: K9.
> - Steps 1–4 under Theorem [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-1|§C5b.3.1]] The Single-Particle Hamiltonian on Plane Waves; definition Definition [[§C5a.7 The Dirac Equation and Its Lagrangian#^def-c5a-7-3|§C5a.7.3]] Single-Particle Hamiltonian; [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^cau-c5b-3-1|§C5b.3, Caution: Negative energies are a problem only if ψ is a wave function]].

### The Hamiltonian in modes, before any algebra ★★ [class exercise, Lecture 10]

Substituting the expansion into $\hat H = \int d^3x\,\hat\psi^\dagger H_{\rm s.p.}\hat\psi$ gives $\hat H = \sum_s\int\frac{d^3p}{(2\pi)^3}E_{\mathbf p}\bigl(\hat a^{s\dagger}_{\mathbf p}\hat a^s_{\mathbf p} - \hat b^s_{\mathbf p}\hat b^{s\dagger}_{\mathbf p}\bigr)$; number-changing terms vanish, see Theorem [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-2|§C5b.3.2]] The Hamiltonian in Modes, before Any Algebra. *Source: Lecture 10 (Oct 5), slides 18–19; transcript: "that requires also a little bit of homework because you might be better off writing a few more intermediate things"*

^nd-thm-c5b-3-2

- [ ] Q1 **[state]** State the unreordered mode form of $\hat H$.
- [ ] Q2 **[why]** Why may $\hat H$ be evaluated at $t = 0$?
- [ ] Q3 Act with $H_{\rm s.p.}$ on the coefficients of $\hat a$ and $\hat b^\dagger$ in $\hat\psi$ (relabelled to $-\mathbf p$): which factors appear?
- [ ] Q4 Multiply by $\hat\psi^\dagger$ and do $\int d^3x$: which momenta are identified, and where does $\mathbf p \to -\mathbf p$ enter?
- [ ] Q5 Expand into four terms, operators in the order they stand: which orthogonality relations kill the $\hat a^\dagger\hat b^\dagger$ and $\hat b\hat a$ terms, and which normalizations give $2E_{\mathbf p}\delta^{rs}$?
- [ ] Q6 **[why]** The "negative energy" term has its oscillators in the "wrong" order. Which two signs meet in it?

> [!tip]- Hints: route in the notes
> - Technique: K9 (mode substitution, $E_{-\mathbf p} = E_{\mathbf p}$), K10 (orthogonality).
> - Lecture route: second derivation under Theorem [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-2|§C5b.3.2]] The Hamiltonian in Modes, before Any Algebra, steps 1–6; general-$t$ route: first derivation, steps 1–6.
> - Orthogonality and normalization: Theorem [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-1|§C5a.10.1]] u†u = 2E, Theorem [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-3|§C5a.10.3]] v†v = 2E, Theorem [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-6|§C5a.10.6]] u and v Are Orthogonal at Opposite Three-Momenta.

### Commutators allow no positive norm with positive energy ★

With commutators, either the antiparticle states have negative norm (if $\hat b$ annihilates the vacuum), or the energy is unbounded below (if $\hat d = \hat b^\dagger$ does); no Hilbert space with positive norm has $\hat H$ bounded below, see Theorem [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-3|§C5b.3.3]] Commutators Allow No Positive Norm with Positive Energy. *Source: Lecture 10 (Oct 5), slide 6 ("Hamiltonian not positive definite") · PS §3.5, p. 54 (after eq. (3.90)) · Yu Exercise 5.10*

^nd-thm-c5b-3-3

- [ ] Q1 **[state]** State the two alternatives and the conclusion.
- [ ] Q2 Option 1: compute $\|\hat b^{s\dagger}(g)|0\rangle\|^2$ with $[\hat b, \hat b^\dagger] < 0$. What is the energy of that state?
- [ ] Q3 Option 2: relabel $\hat d = \hat b^\dagger$. What sign does $[\hat d, \hat d^\dagger]$ have, and what does $\hat H$ look like in terms of $\hat d$?
- [ ] Q4 **[why]** Why is there no third option?
- [ ] Q5 **[why]** Compare with the classical field: what does Theorem [[§C5b.5 The U(1) Charge, Particles and Antiparticles#^thm-c5b-5-2|§C5b.5.2]] The Classical Dirac Energy Is Unbounded Below; the Classical Charge Is Positive say about the classical energy, and why is that not a contradiction?

> [!tip]- Hints: route in the notes
> - Technique: K11.
> - Steps 1–6 under Theorem [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-3|§C5b.3.3]] Commutators Allow No Positive Norm with Positive Energy, using Theorem [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-5|§C5b.2.5]] Commutators Give the Antiparticle Modes a Negative Algebra and Theorem [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-2|§C5b.3.2]] The Hamiltonian in Modes, before Any Algebra.

### The Hamiltonian of the Dirac field ★★

With anticommutators, $\hat H = \sum_s\int\frac{d^3p}{(2\pi)^3}E_{\mathbf p}(\hat a^{s\dagger}\hat a^s + \hat b^{s\dagger}\hat b^s) + E_0^{(\rm D)}$ and $:\!\hat H\!:$ is the same without the constant: both species carry positive energy, see Theorem [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-5|§C5b.3.5]] The Hamiltonian of the Dirac Field. *Source: Lecture 10 (Oct 5), slides 19, 23 · PS eq. (3.104)*

^nd-thm-c5b-3-5

- [ ] Q1 **[state]** State $\hat H$ and $:\!\hat H\!:$ in modes.
- [ ] Q2 Reorder $\hat b^s_{\mathbf p}\hat b^{s\dagger}_{\mathbf p}$ with the anticommutator: what constant appears, and what is its sign?
- [ ] Q3 Collect: what is the operator part, and what is the constant?
- [ ] Q4 **[why]** "Two minus signs make a plus": name them.
- [ ] Q5 **[why]** Slide 19 goes from $-\hat b\hat b^\dagger$ to $+\hat b^\dagger\hat b$ in one line. What has been dropped, and what does $\hat H$ then measure?

> [!tip]- Hints: route in the notes
> - Technique: K11, K9.
> - Steps 1–4 under Theorem [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-5|§C5b.3.5]] The Hamiltonian of the Dirac Field; [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^rem-c5b-3-1|§C5b.3, Remark: Two minus signs make a plus]]; energies from the vacuum [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^rem-c5b-3-2|§C5b.3, Remark: Energies are measured from the vacuum]].

### The fermionic zero-point energy ★

$E_0^{(\rm D)} = -2V\int\frac{d^3p}{(2\pi)^3}E_{\mathbf p} = -4E_0$ with $V = (2\pi)^3\delta^3(\mathbf 0)$: $-\frac12E_{\mathbf p}$ per fermionic mode, see Theorem [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-6|§C5b.3.6]] The Fermionic Zero-Point Energy Is Negative. *Source: Lecture 10 (Oct 5), transcript ("B B dagger … plus delta function … some infinity sitting in here") · Yu (5.269)*

^nd-thm-c5b-3-6

- [ ] Q1 **[state]** State $E_0^{(\rm D)}$ and compare it with the real scalar's $E_0$.
- [ ] Q2 Where does the constant come from in the reordering, and how is $\delta^3(\mathbf 0)$ read?
- [ ] Q3 Count the modes per momentum: how many, and what does each contribute?
- [ ] Q4 **[why]** Why do bosonic and fermionic zero-point energies have opposite signs?
- [ ] Q5 **[conv]** Which names do the sources use for the zero-point energy?

> [!tip]- Hints: route in the notes
> - Technique: K11.
> - Steps 1–3 under Theorem [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-6|§C5b.3.6]] The Fermionic Zero-Point Energy Is Negative; scalar Theorem [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-4|§C2a.3.4]] The Zero-Point Energy; names [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^cau-c2a-3-1|§C2a.3, Caution: Names for the zero-point energy]].

### Momentum of the Dirac field ★

$\hat{\mathbf P} = \int d^3x\,\hat\psi^\dagger(-i\nabla)\hat\psi = \sum_s\int\frac{d^3p}{(2\pi)^3}\mathbf p\,(\hat a^{s\dagger}\hat a^s + \hat b^{s\dagger}\hat b^s)$, with no constant, see Theorem [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-7|§C5b.3.7]] Momentum of the Dirac Field. *Source: PS §3.5, eq. (3.105) · Yu (5.219)*

^nd-thm-c5b-3-7

- [ ] Q1 **[state]** State $\hat{\mathbf P}$ in field form and in modes.
- [ ] Q2 Act with $-i\nabla$ on $e^{\mp iq\cdot x}$: which factors appear on the $\hat a$ and $\hat b^\dagger$ terms?
- [ ] Q3 Which steps of the $\hat H$ computation carry over unchanged?
- [ ] Q4 **[why]** Why does the reordering constant vanish here?

> [!tip]- Hints: route in the notes
> - Technique: K9.
> - Steps 1–3 under Theorem [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-7|§C5b.3.7]] Momentum of the Dirac Field; translations: Theorem [[§C5b.1 Canonical Quantization of the Dirac Field#^thm-c5b-1-9|§C5b.1.9]] The Field Momentum Generates Translations of ψ.

### Ladder relations ★

$[AB, C] = A\{B, C\} - \{A, C\}B$ gives $[\hat H, \hat a^{s\dagger}_{\mathbf p}] = E_{\mathbf p}\hat a^{s\dagger}_{\mathbf p}$, $[\hat H, \hat b^{s\dagger}_{\mathbf p}] = E_{\mathbf p}\hat b^{s\dagger}_{\mathbf p}$, and the same with $\hat{\mathbf P}$ and $\mathbf p$, see Theorem [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-8|§C5b.3.8]] Ladder Relations. *Source: Lecture 10 (Oct 5), slide 20 (one-particle states carry $E_{\mathbf p}$, $\mathbf p$)*

^nd-thm-c5b-3-8

- [ ] Q1 **[state]** State the identity for $[AB, C]$ and the four ladder relations.
- [ ] Q2 Prove the identity by expanding.
- [ ] Q3 Apply it to $[\hat a^{r\dagger}_{\mathbf q}\hat a^r_{\mathbf q}, \hat a^{s\dagger}_{\mathbf p}]$.
- [ ] Q4 **[why]** Why are these commutators, not anticommutators, although the fields anticommute?

> [!tip]- Hints: route in the notes
> - Technique: K11.
> - Steps 1–5 under Theorem [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-8|§C5b.3.8]] Ladder Relations.

### One-particle states and their normalization ★★

$|\mathbf p, s\rangle = \sqrt{2E_{\mathbf p}}\,\hat a^{s\dagger}_{\mathbf p}|0\rangle$, $|\mathbf p, s\rangle^c = \sqrt{2E_{\mathbf p}}\,\hat b^{s\dagger}_{\mathbf p}|0\rangle$, with $\langle\mathbf p, r|\mathbf q, s\rangle = 2E_{\mathbf p}(2\pi)^3\delta^{rs}\delta^3(\mathbf p - \mathbf q)$, see Theorem [[§C5b.4 Fermions, Fock Space and the Pauli Principle#^thm-c5b-4-1|§C5b.4.1]] Fermions and Antifermions. *Source: Lecture 10 (Oct 5), slide 20 · PS eqs. (3.106)–(3.107)*

^nd-thm-c5b-4-1

- [ ] Q1 **[def]** Define the fermion and antifermion one-particle states, with the normalization factor.
- [ ] Q2 Show they are eigenstates of $:\!\hat H\!:$ and $\hat{\mathbf P}$: which eigenvalues?
- [ ] Q3 Compute $\langle\mathbf p, r|\mathbf q, s\rangle$ by moving the annihilator to the right.
- [ ] Q4 Why is ${}^c\langle\mathbf p, r|\mathbf q, s\rangle = 0$?
- [ ] Q5 **[why]** Why is the factor $\sqrt{2E_{\mathbf p}}$ there (Lorentz invariance of the normalization)?
- [ ] Q6 **[why]** With commutators, what would the antifermion overlap have been?

> [!tip]- Hints: route in the notes
> - Technique: K11.
> - Steps 1–3 of the derivation under Theorem [[§C5b.4 Fermions, Fock Space and the Pauli Principle#^thm-c5b-4-1|§C5b.4.1]] Fermions and Antifermions; ladder relations Theorem [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-8|§C5b.3.8]] Ladder Relations.
> - Relativistic normalization: Definition [[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-1|§C2a.4.1]] Relativistic Normalization.

### Fermi–Dirac statistics and the Pauli principle ★★

$\hat a^{r\dagger}_{\mathbf p}\hat a^{s\dagger}_{\mathbf q} = -\hat a^{s\dagger}_{\mathbf q}\hat a^{r\dagger}_{\mathbf p}$; $\hat a^{s\dagger}(g)^2 = 0$; the two-particle overlap has a minus sign where bosons have a plus, see Theorem [[§C5b.4 Fermions, Fock Space and the Pauli Principle#^thm-c5b-4-2|§C5b.4.2]] Fermi–Dirac Statistics and the Pauli Exclusion Principle. *Source: Lecture 10 (Oct 5), slide 21 · PS §3.5, p. 57*

^nd-thm-c5b-4-2

- [ ] Q1 **[state]** State the three parts.
- [ ] Q2 Which anticommutator gives the antisymmetry?
- [ ] Q3 Pauli: why does $\{\hat a^{s\dagger}(g), \hat a^{s\dagger}(g)\} = 0$ mean $\hat a^{s\dagger}(g)^2 = 0$, and how is the kernel form read?
- [ ] Q4 Compute the two-particle overlap: move the first annihilator to the right; where does the minus sign arise?
- [ ] Q5 **[why]** Why is exclusion an input in hole theory but an output here?

> [!tip]- Hints: route in the notes
> - Technique: K11.
> - Steps 1–4 under Theorem [[§C5b.4 Fermions, Fock Space and the Pauli Principle#^thm-c5b-4-2|§C5b.4.2]] Fermi–Dirac Statistics and the Pauli Exclusion Principle; Dirac sea: [[§C5b.5 The U(1) Charge, Particles and Antiparticles#^rem-c5b-5-3|§C5b.5, Remark: The Dirac sea, read in the field]].

### Dirac quanta have spin one-half ★

At rest, $\hat J_z\hat a^{s\dagger}_{\mathbf 0}|0\rangle = \sum_r(\xi^{r\dagger}\frac{\sigma^3}{2}\xi^s)\hat a^{r\dagger}_{\mathbf 0}|0\rangle$ and $\hat J_z\hat b^{s\dagger}_{\mathbf 0}|0\rangle = -\sum_r(\eta^{s\dagger}\frac{\sigma^3}{2}\eta^r)\hat b^{r\dagger}_{\mathbf 0}|0\rangle$, see Theorem [[§C5b.4 Fermions, Fock Space and the Pauli Principle#^thm-c5b-4-3|§C5b.4.3]] Dirac Quanta Have Spin One-Half. *Source: PS §3.5, eq. (3.111)–(3.112) · Lecture 12 (Oct 12), slide 16 (the spin operator)*

^nd-thm-c5b-4-3

- [ ] Q1 **[state]** State the action of $\hat J_z$ on the two rest-frame one-particle states.
- [ ] Q2 Reduce $\hat J_z\hat a^{s\dagger}_{\mathbf 0}|0\rangle$ to a commutator: why is $\hat J_z|0\rangle = 0$?
- [ ] Q3 Why does the orbital part drop?
- [ ] Q4 Insert the rest-frame spinors $u^s(0)$, $v^s(0)$: which two-spinor matrix element survives?
- [ ] Q5 **[why]** Where does the extra minus sign for the antifermion come from, and what does it imply for the choice of $\eta^s$?

> [!tip]- Hints: route in the notes
> - Technique: K11.
> - Steps 1–6 under Theorem [[§C5b.4 Fermions, Fock Space and the Pauli Principle#^thm-c5b-4-3|§C5b.4.3]] Dirac Quanta Have Spin One-Half; the choice: Definition [[§C9.5 Charge Conjugation on Oscillators and Spinors#^def-c9-5-5|§C9.5.5]] The Antiparticle Two-Spinors η^s = ξ^{−s} and Theorem [[§C9.7 Physical Spin versus Wave-Function Spin#^thm-c9-7-3|§C9.7.3]] Particle and Antiparticle Created with Label s Have the Same Physical Spin.

### Charge in modes and fermions minus antifermions ★

$\hat Q = \sum_s\int\frac{d^3p}{(2\pi)^3}(\hat a^{s\dagger}\hat a^s + \hat b^s\hat b^{s\dagger})$ before any algebra, and $\int d^3x\,:\!\hat\psi^\dagger\hat\psi\!: = \hat N_a - \hat N_b$, see Theorem [[§C5b.5 The U(1) Charge, Particles and Antiparticles#^thm-c5b-5-1|§C5b.5.1]] The Charge in Modes, before Any Algebra and Theorem [[§C5b.5 The U(1) Charge, Particles and Antiparticles#^thm-c5b-5-3|§C5b.5.3]] The Charge Counts Fermions Minus Antifermions. *Source: Problem Set 6, Problem 2 (PS eq. (3.113))*

^nd-thm-c5b-5-3

→ drilled as [[PHY 513 PS Drill#^ps6-2|PS6.2]]

### Particles and antiparticles carry opposite charge ★

$[\hat Q, \hat a^{s\dagger}_{\mathbf p}] = \hat a^{s\dagger}_{\mathbf p}$, $[\hat Q, \hat b^{s\dagger}_{\mathbf p}] = -\hat b^{s\dagger}_{\mathbf p}$, $[\hat Q, \hat\psi] = -\hat\psi$; one-particle states have charge $\pm1$, see Theorem [[§C5b.5 The U(1) Charge, Particles and Antiparticles#^thm-c5b-5-4|§C5b.5.4]] Particles and Antiparticles Carry Opposite Charge. *Source: PS §3.5, p. 62 · the user's notes Ch. 10*

^nd-thm-c5b-5-4

- [ ] Q1 **[state]** State the commutators of $\hat Q$ with the four mode operators and with $\hat\psi$.
- [ ] Q2 Compute $[\hat Q, \hat b^{s\dagger}_{\mathbf p}]$ with the identity $[AB, C] = A\{B, C\} - \{A, C\}B$.
- [ ] Q3 Why does the reordering constant not matter for these commutators?
- [ ] Q4 **[why]** $\hat\psi$ lowers the charge by one unit in two ways. Which?
- [ ] Q5 **[why]** "Destroying a particle is not creating an antiparticle": what distinguishes them?

> [!tip]- Hints: route in the notes
> - Technique: K11.
> - Steps 1–7 under Theorem [[§C5b.5 The U(1) Charge, Particles and Antiparticles#^thm-c5b-5-4|§C5b.5.4]] Particles and Antiparticles Carry Opposite Charge; [[§C5b.5 The U(1) Charge, Particles and Antiparticles#^rem-c5b-5-2|§C5b.5, Remark: Destroying a particle is not creating an antiparticle]].

### The classical Dirac energy is unbounded below ★

For c-number amplitudes $H = \sum_s\int\frac{d^3p}{(2\pi)^3}E_{\mathbf p}(|a^s|^2 - |b^s|^2)$ is unbounded below, while $Q = \int d^3x\,\psi^\dagger\psi \ge 0$, see Theorem [[§C5b.5 The U(1) Charge, Particles and Antiparticles#^thm-c5b-5-2|§C5b.5.2]] The Classical Dirac Energy Is Unbounded Below; the Classical Charge Is Positive. *Source: PS §3.5, p. 54 (after eq. (3.90))*

^nd-thm-c5b-5-2

- [ ] Q1 **[state]** State $H$ and $Q$ for the classical field in amplitudes.
- [ ] Q2 Which configuration makes $H \to -\infty$?
- [ ] Q3 **[why]** Why is the positivity of $Q$ the positive probability density of Dirac's equation in QM?
- [ ] Q4 **[why]** After quantization with anticommutators, which of the two signs flips, $H$'s or $Q$'s?

> [!tip]- Hints: route in the notes
> - Technique: K9.
> - Steps 1–3 under Theorem [[§C5b.5 The U(1) Charge, Particles and Antiparticles#^thm-c5b-5-2|§C5b.5.2]] The Classical Dirac Energy Is Unbounded Below; the Classical Charge Is Positive; compare Theorem [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-5|§C5b.3.5]] The Hamiltonian of the Dirac Field and Theorem [[§C5b.5 The U(1) Charge, Particles and Antiparticles#^thm-c5b-5-3|§C5b.5.3]] The Charge Counts Fermions Minus Antifermions.

### Time dependence of the modes; the covariant mode expansion ★

With $\hat H$ of the Dirac field, $e^{i\hat Ht}\hat a^s_{\mathbf p}e^{-i\hat Ht} = \hat a^s_{\mathbf p}e^{-iE_{\mathbf p}t}$ and $e^{i\hat Ht}\hat b^{s\dagger}_{\mathbf p}e^{-i\hat Ht} = \hat b^{s\dagger}_{\mathbf p}e^{iE_{\mathbf p}t}$; the Heisenberg field is the expansion with time-independent operators and $e^{\mp ip\cdot x}$, and the equal-time anticommutators hold at every common time, see Theorem [[§C5b.6 The Heisenberg Dirac Field#^thm-c5b-6-1|§C5b.6.1]] Time Dependence of the Modes; the Covariant Mode Expansion. *Source: Lecture 10 (Oct 5), slide 10 ("Field in Heisenberg representation") · PS §3.5, eqs. (3.99), (3.104)*

^nd-thm-c5b-6-1

- [ ] Q1 **[state]** State the three parts.
- [ ] Q2 Let $\hat F(t) = e^{i\hat Ht}\hat a^s_{\mathbf p}e^{-i\hat Ht}$. Differentiate and use the ladder relation: which differential equation does $\hat F$ obey, and what is its solution?
- [ ] Q3 Do the same for $\hat b^{s\dagger}_{\mathbf p}$: why does it pick up $e^{+iE_{\mathbf p}t}$?
- [ ] Q4 Insert into the Schrödinger field at $t = 0$: how do the phases combine with $e^{\pm i\mathbf p\cdot\mathbf x}$ into $e^{\mp ip\cdot x}$?
- [ ] Q5 **[why]** Why do the equal-time anticommutators hold at every common time $t$, not only at $t = 0$?
- [ ] Q6 **[why]** Does the reordering constant $E_0^{(\rm D)}$ affect the time dependence?

> [!tip]- Hints: route in the notes
> - Technique: K11 (ladder relations), K9.
> - Steps 1–4 under Theorem [[§C5b.6 The Heisenberg Dirac Field#^thm-c5b-6-1|§C5b.6.1]] Time Dependence of the Modes; the Covariant Mode Expansion; ladder relations Theorem [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-8|§C5b.3.8]] Ladder Relations.

### The Heisenberg equation is the Dirac equation ★

With the equal-time anticommutators and $\hat H = \int\hat\psi^\dagger H_{\rm s.p.}\hat\psi$, $i\partial_t\hat\psi = [\hat\psi, \hat H]$ gives $(i\slashed\partial - m)\hat\psi = 0$, see Theorem [[§C5b.6 The Heisenberg Dirac Field#^thm-c5b-6-2|§C5b.6.2]] The Heisenberg Equation Is the Dirac Equation. *Source: the user's notes Ch. 10 · scalar analogue PS §2.4, eqs. (2.44)–(2.45)*

^nd-thm-c5b-6-2

- [ ] Q1 **[state]** State the result.
- [ ] Q2 Prove $[A, BC] = \{A, B\}C - B\{A, C\}$.
- [ ] Q3 Write $\hat H$ as a bilinear $\int\hat\psi^\dagger_b\hat C_b$: which anticommutators are needed, and what do they give?
- [ ] Q4 Integrate the delta and multiply by $\gamma^0$.
- [ ] Q5 **[why]** Does this computation distinguish commutators from anticommutators? What does that imply?

> [!tip]- Hints: route in the notes
> - Technique: K11.
> - Steps 1–5 under Theorem [[§C5b.6 The Heisenberg Dirac Field#^thm-c5b-6-2|§C5b.6.2]] The Heisenberg Equation Is the Dirac Equation; [[§C5b.6 The Heisenberg Dirac Field#^rem-c5b-6-1|§C5b.6, Remark: The field equation does not choose the statistics]]; time dependence of the modes Theorem [[§C5b.6 The Heisenberg Dirac Field#^thm-c5b-6-1|§C5b.6.1]] Time Dependence of the Modes; the Covariant Mode Expansion.

### One-particle wave functions ★

$\langle0|\hat\psi(x)|\mathbf p, s\rangle = u^s(p)e^{-ip\cdot x}$ and $\langle0|\hat{\bar\psi}(x)|\mathbf p, s\rangle^c = \bar v^s(p)e^{-ip\cdot x}$, see Theorem [[§C5b.6 The Heisenberg Dirac Field#^thm-c5b-6-3|§C5b.6.3]] Positive and Negative Frequency; One-Particle Wave Functions. *Source: the user's notes Ch. 10 · used for external fermion lines later (PS §4.7)*

^nd-thm-c5b-6-3

- [ ] Q1 **[state]** State both wave functions.
- [ ] Q2 Which part of $\hat\psi$ contributes to the first matrix element, and why?
- [ ] Q3 Do the $\mathbf q$ integral and the spin sum: where does $\sqrt{2E_{\mathbf p}}$ cancel?
- [ ] Q4 **[why]** Why does the antifermion wave function involve $\hat{\bar\psi}$ and $\bar v$?

> [!tip]- Hints: route in the notes
> - Technique: K11.
> - Steps 1–4 under Theorem [[§C5b.6 The Heisenberg Dirac Field#^thm-c5b-6-3|§C5b.6.3]] Positive and Negative Frequency; One-Particle Wave Functions.

### Dirac Wightman functions from the scalar one ★

$S^+_W(\xi) = \int\frac{d^3p}{(2\pi)^32E_{\mathbf p}}(\slashed p + m)e^{-ip\cdot\xi} = (i\slashed\partial_x + m)D_W(\xi)$, $S^-_W(\xi) = -(i\slashed\partial_x + m)D_W(-\xi)$, see Theorem [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-1|§C5b.7.1]] The Dirac Wightman Functions from the Scalar One. *Source: Lecture 10 (Oct 5), transcript ("a Wightman function plus a different Wightman function") · PS §3.5, eqs. (3.114)–(3.115)*

^nd-thm-c5b-7-1

- [ ] Q1 **[state]** State $S^\pm_W$ in momentum form and in terms of $D_W$.
- [ ] Q2 Which terms of $\hat\psi$ and $\hat{\bar\psi}$ survive between vacua in each ordering?
- [ ] Q3 Which spin sum appears in each, and with which sign?
- [ ] Q4 Pull the matrix out of the integral: why is $(\slashed p + m)e^{-ip\cdot\xi} = (i\slashed\partial_x + m)e^{-ip\cdot\xi}$?
- [ ] Q5 **[why]** Why do both satisfy the Dirac equation?

> [!tip]- Hints: route in the notes
> - Technique: K11, K5.
> - Steps 1–5 under Theorem [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-1|§C5b.7.1]] The Dirac Wightman Functions from the Scalar One; spin sums Theorem [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-7|§C5a.10.7]] The Spin Sum over u, Theorem [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-8|§C5a.10.8]] The Spin Sum over v; $D_W$ Definition [[§C2b.2 The Wightman Function#^def-c2b-2-1|§C2b.2.1]] Wightman Function.

### The field anticommutator is a c-number; microcausality ★

$\{\hat\psi_a(x), \hat{\bar\psi}_b(y)\} = iS_{ab}(x - y)\mathbf 1$ with $S = (i\slashed\partial_x + m)D$, and $S$ vanishes at spacelike separation, so fermion fields anticommute there, see Theorem [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-2|§C5b.7.2]] The Field Anticommutator Is a c-Number and Theorem [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-3|§C5b.7.3]] Microcausality of the Dirac Field. *Source: Lecture 10 (Oct 5), slide 6 and transcript · PS §3.5, p. 56*

^nd-thm-c5b-7-3

- [ ] Q1 **[state]** State the anticommutator at arbitrary $x$, $y$ and the microcausality statement.
- [ ] Q2 Substitute both expansions: which mode anticommutators survive?
- [ ] Q3 Express the result through $S^+_W + S^-_W$ and then through the commutator function $D$.
- [ ] Q4 Why does a derivative not enlarge the support of a distribution?
- [ ] Q5 **[why]** Does the commutator of the fields vanish at spacelike separation? Why is that not a violation of causality?

> [!tip]- Hints: route in the notes
> - Technique: K14 (microcausality), K11.
> - Steps 1–6 under Theorem [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-2|§C5b.7.2]] The Field Anticommutator Is a c-Number, steps 1–4 under Theorem [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-3|§C5b.7.3]] Microcausality of the Dirac Field; observables are even: [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^rem-c5b-7-1|§C5b.7, Remark: Why a field may anticommute: observables are even]].

### Bilinears commute at spacelike separation ★

For $\hat{\mathcal O}_i = :\!\hat{\bar\psi}\Gamma_i\hat\psi\!:$, $[\hat{\mathcal O}_1(x), \hat{\mathcal O}_2(y)] = 0$ for $(x - y)^2 < 0$, see Theorem [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-4|§C5b.7.4]] Bilinears Commute at Spacelike Separation. *Source: PS §3.5, p. 56 · the user's notes Ch. 10*

^nd-thm-c5b-7-4

- [ ] Q1 **[state]** State the result and why it is what microcausality requires.
- [ ] Q2 Prove the identity $[AB, CD] = A\{B, C\}D - AC\{B, D\} + \{A, C\}DB - C\{A, D\}B$.
- [ ] Q3 Apply it to two bilinears: which anticommutators appear, and why does each vanish at spacelike separation?
- [ ] Q4 **[why]** Why does normal ordering change nothing in the commutator?

> [!tip]- Hints: route in the notes
> - Technique: K11, K14.
> - Steps 1–4 under Theorem [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-4|§C5b.7.4]] Bilinears Commute at Spacelike Separation.

### A Dirac field with commutators is not causal ★

Under positivity, invariance and Lorentz invariance, $\langle0|\hat\psi\hat{\bar\psi}|0\rangle = A\,S^+_W$ and $\langle0|\hat{\bar\psi}\hat\psi|0\rangle = B\,S^-_W$; for $m > 0$ the commutator's vacuum expectation is nonzero at every spacelike $\xi$, the anticommutator's vanishes if $A = B$, see Theorem [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-5|§C5b.7.5]] A Dirac Field with Commutators Is Not Causal. *Source: Lecture 10 (Oct 5), slide 6 ("Propagation not causal") and transcript · PS §3.5, pp. 54–56, eqs. (3.93)–(3.96)*

^nd-thm-c5b-7-5

- [ ] Q1 **[state]** State the assumptions (i)–(iv) and the conclusion.
- [ ] Q2 Which two-point functions do the two orderings give, and why are the constants positive?
- [ ] Q3 Lecture route: write the commutator as a sum and the anticommutator as a difference of Wightman functions. Which is which?
- [ ] Q4 At spacelike $\xi$, what is $D_W(\xi)$ compared with $D_W(-\xi)$?
- [ ] Q5 **[why]** Why does a trace show the commutator's expectation is nonzero (the role of $\operatorname{tr}\gamma^\mu = 0$)?

> [!tip]- Hints: route in the notes
> - Technique: K14, K5 (traces).
> - First derivation steps 1–7, second route (Lecture 10) steps 1–4 under Theorem [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-5|§C5b.7.5]] A Dirac Field with Commutators Is Not Causal; $D_W$ at spacelike separation [[§C2b.3 Explicit Forms of the Wightman Function|§C2b.3]] Explicit Forms of the Wightman Function.

### Green's functions of the Dirac operator ★

$S_C = (i\slashed\partial + m)D_C$ satisfies $(i\slashed\partial_x - m)S_C(x - y) = i\delta^4(x - y)$ for $C = R, A, F$; retarded $S_R = \theta(\xi^0)iS$, see Theorem [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-1|§C5b.8.1]] Green's Functions of the Dirac Operator and Definition [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^def-c5b-8-1|§C5b.8.1]] Retarded and Advanced Functions of the Dirac Field. *Source: PS §3.5, eqs. (3.116)–(3.120) (reading)*

^nd-thm-c5b-8-1

- [ ] Q1 **[state]** State the Green's-function equation and the normalization of the scalar $D_C$.
- [ ] Q2 Compute $(i\slashed\partial - m)(i\slashed\partial + m)$.
- [ ] Q3 In momentum space, verify $(\slashed p - m)\frac{i(\slashed p + m)}{p^2 - m^2 + i\varepsilon} \to i$.
- [ ] Q4 **[conv]** Which normalization of the scalar Green's functions does the course use (compare PS), and which right-hand side does it give for the Dirac operator?

> [!tip]- Hints: route in the notes
> - Technique: K5, K13.
> - Steps 1–5 under Theorem [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-1|§C5b.8.1]] Green's Functions of the Dirac Operator; scalar Definition [[§C2b.5 Green's Functions and Contours#^def-c2b-5-1|§C2b.5.1]] Green's Function of the Klein–Gordon Operator.

### The Dirac Feynman propagator ★

$S_F(x - y) = \langle0|T\{\hat\psi(x)\hat{\bar\psi}(y)\}|0\rangle = \int\frac{d^4p}{(2\pi)^4}\frac{i(\slashed p + m)}{p^2 - m^2 + i\varepsilon}e^{-ip\cdot(x - y)} = (i\slashed\partial_x + m)D_F(x - y)$, see Theorem [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-3|§C5b.8.3]] The Dirac Feynman Propagator. *Source: PS §3.5, eq. (3.121) (reading; not on the slides) · the user's notes Ch. 10*

^nd-thm-c5b-8-3

- [ ] Q1 **[state]** State $S_F$ as a time-ordered product, through $S^\pm_W$, as a momentum integral and through $D_F$.
- [ ] Q2 Write $\theta(\xi^0)S^+_W - \theta(-\xi^0)S^-_W$ and relabel $\mathbf p \to -\mathbf p$ in the second term.
- [ ] Q3 Locate the poles of $\frac{i(\slashed p + m)}{p^2 - m^2 + i\varepsilon}$ in $p^0$ and compute the residues.
- [ ] Q4 Close the contour for $\xi^0 > 0$ and for $\xi^0 < 0$: which pole is picked up in each case?
- [ ] Q5 **[why]** Fermion forward, antifermion backward: read off the two time orderings.
- [ ] Q6 **[why]** Why does the minus sign of the fermionic time ordering make $S_F = (i\slashed\partial + m)D_F$ hold without a contact term?

> [!tip]- Hints: route in the notes
> - Technique: K13 (contours, $i\varepsilon$).
> - First derivation steps 1–6 (P2 in reverse) and second route steps 1–4 under Theorem [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-3|§C5b.8.3]] The Dirac Feynman Propagator; [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^rem-c5b-8-1|§C5b.8, Remark: Fermion forward, antifermion backward]].

### The Dirac propagator as a distribution and its matrix form ★

$\tilde S^\varepsilon_F \to i(\slashed p + m)\mathcal P\frac{1}{p^2 - m^2} + \pi(\slashed p + m)\delta(p^2 - m^2)$ in $\mathcal S'$, and $\tilde S_F = \frac{i}{\slashed p - m + i\varepsilon}$ is a matrix inverse taken before the limit, see Theorem [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-4|§C5b.8.4]] The Dirac Propagator as a Distribution and Theorem [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-5|§C5b.8.5]] The Matrix Form of the Propagator. *Source: PS §3.5, eqs. (3.120)–(3.121) · the user's notes Ch. 10*

^nd-thm-c5b-8-5

- [ ] Q1 **[state]** State the $\varepsilon \to 0^+$ limit and the matrix form.
- [ ] Q2 Compute $(\slashed p - M)(\slashed p + M)$ for a complex number $M$ and invert $\slashed p - m + i\varepsilon$.
- [ ] Q3 Why may the denominator's $2im\varepsilon$ be replaced by $i\varepsilon$ in the limit?
- [ ] Q4 **[why]** Why is multiplication by the polynomial $\slashed p + m$ continuous on $\mathcal S'$, and why does $\theta(0)$ not enter?

> [!tip]- Hints: route in the notes
> - Technique: K13 (Sokhotski–Plemelj), K5.
> - Steps 1–4 under Theorem [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-4|§C5b.8.4]] The Dirac Propagator as a Distribution; steps 1–3 under Theorem [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-5|§C5b.8.5]] The Matrix Form of the Propagator.

### The anticommutators are identities after smearing ★

$\{\hat\psi(f), \hat\psi^\dagger(g)\} = \langle f, g\rangle$; $\hat\psi(f)^2 = 0$ and $\|\hat\psi(f)\| = \|f\|_{L^2}$: smeared Fermi fields are bounded, unlike Bose fields, see Theorem [[§C5b.1 Canonical Quantization of the Dirac Field#^thm-c5b-1-8|§C5b.1.8]] The Anticommutators Are Identities after Smearing; Smeared Fermi Fields Are Bounded. *Source: the user's notes Ch. 10 (distributions justified)*

^nd-thm-c5b-1-8

- [ ] Q1 **[state]** Define the smeared field and state the three parts.
- [ ] Q2 Why is $\hat\psi(f)$ nilpotent?
- [ ] Q3 Show $\hat A^\dagger\hat A/\|f\|^2$ is a projection, and conclude the norm.
- [ ] Q4 **[why]** Why is the field at a point still not an operator? Why are bosonic smeared fields unbounded?

> [!tip]- Hints: route in the notes
> - Technique: K11.
> - Steps 1–5 under Theorem [[§C5b.1 Canonical Quantization of the Dirac Field#^thm-c5b-1-8|§C5b.1.8]] The Anticommutators Are Identities after Smearing; Smeared Fermi Fields Are Bounded; Definition [[§C5b.1 Canonical Quantization of the Dirac Field#^def-c5b-1-5|§C5b.1.5]] Smeared Dirac Field on a Time Slice; scalar Theorem [[§C2a.1 Canonical Quantization of Fields#^thm-c2a-1-3|§C2a.1.3]] The Canonical Relations Are Identities after Smearing.

### The field momentum generates translations of ψ ★

$[\hat\psi_a(\mathbf x), \hat{\mathbf P}] = -i\nabla\hat\psi_a(\mathbf x)$, commutators although the fields anticommute, because $\hat{\mathbf P}$ is bilinear, see Theorem [[§C5b.1 Canonical Quantization of the Dirac Field#^thm-c5b-1-9|§C5b.1.9]] The Field Momentum Generates Translations of ψ. *Source: written in the notes (scalar analogue: Yu §3.2)*

^nd-thm-c5b-1-9

- [ ] Q1 **[state]** State the result and the covariant translation law it belongs to.
- [ ] Q2 Use $[A, BC] = \{A, B\}C - B\{A, C\}$ with $B = \hat\psi^\dagger_b(\mathbf y)$, $C = \partial_k\hat\psi_b(\mathbf y)$: which anticommutator survives?
- [ ] Q3 Integrate the delta. What changes for $\hat\psi^\dagger$?
- [ ] Q4 **[conv]** Rewrite in terms of $\partial^k$ and match $[\hat\Phi, \hat P^\mu] = i\partial^\mu\hat\Phi$: where does the sign go?

> [!tip]- Hints: route in the notes
> - Technique: K11, K2.
> - Steps 1–5 under Theorem [[§C5b.1 Canonical Quantization of the Dirac Field#^thm-c5b-1-9|§C5b.1.9]] The Field Momentum Generates Translations of ψ; covariant law Theorem [[§C3.5 Covariant Quantum Fields and the Free Scalar's Representation#^thm-c3-5-2|§C3.5.2]] Translations of a Field; the Heisenberg Equation.

### The free fields of the course obey spin–statistics ★

The Dirac field admits no commutator quantization with positive norms and bounded energy, nor a causal one; the scalar with commutators is fine; both obey the principle, see Theorem [[§C5b.9 Spin and Statistics#^thm-c5b-9-1|§C5b.9.1]] The Free Fields of the Course Obey the Spin–Statistics Theorem. *Source: Lecture 10 (Oct 5), slides 6–7 · PS §3.5*

^nd-thm-c5b-9-1

- [ ] Q1 **[state]** State the two parts.
- [ ] Q2 Spin ½ from positivity: which theorem, in one sentence?
- [ ] Q3 Spin ½ from causality: which theorem, in one sentence?
- [ ] Q4 **[why]** Why do these checks not prove the general theorem?

> [!tip]- Hints: route in the notes
> - Technique: K14.
> - Steps 1–4 under Theorem [[§C5b.9 Spin and Statistics#^thm-c5b-9-1|§C5b.9.1]] The Free Fields of the Course Obey the Spin–Statistics Theorem; two arguments one answer [[§C5b.9 Spin and Statistics#^rem-c5b-9-1|§C5b.9, Remark: Two arguments, one answer]].

# T10. Discrete symmetries P, C, T and CPT

## Definitions and conventions T10

### Discrete Lorentz transformations and the four sectors [class exercise, Lecture 11]

A Lorentz transformation is discrete if it cannot be joined to the identity by a continuous path; the four sectors are $\mathcal I$, $\mathcal P = \operatorname{diag}(1, -1, -1, -1)$, $\mathcal T = \operatorname{diag}(-1, 1, 1, 1)$ and $\mathcal P\mathcal T = -\mathbb 1$, separated by $\det\Lambda$ and the sign of $\Lambda^0{}_0$, see Definition [[§C9.1 Discrete Lorentz Transformations#^def-c9-1-1|§C9.1.1]] Discrete Lorentz Transformation. *Source: Lecture 11 (Oct 7), slides 5–7; transcript: "you can try to persuade yourself" (no rotation flips all three axes; $\Lambda^0{}_0 \ge 1$ for boosts and their products) · PS §3.6, p. 64*

^nd-def-c9-1-1

- [ ] Q1 **[def]** Define a discrete Lorentz transformation and list the four sectors with their matrices.
- [ ] Q2 **[class exercise]** Why can no rotation send $\mathbf x \to -\mathbf x$ in three dimensions? Use the determinant, and say why an integer-valued continuous function cannot jump.
- [ ] Q3 **[class exercise]** Why does every boost, and every product of boosts and rotations, have $\Lambda^0{}_0 \ge 1$?
- [ ] Q4 **[conv]** Slide 7 says "$\mathcal T$, $\mathcal P$ have $\det\Lambda = 1$". Which determinants are correct, and which element has determinant $+1$?
- [ ] Q5 **[why]** Why does parity depend on the number of space dimensions (what is $-\mathbb 1_2$)?
- [ ] Q6 **[conv]** In this chapter, does "Lorentz transformation" include $\mathcal P$ and $\mathcal T$? What does "Lorentz invariant" mean elsewhere in the notes?

> [!tip]- Hints: route in the notes
> - Technique: K1 (invariants).
> - Two invariants: [[§C9.1 Discrete Lorentz Transformations#^rem-c9-1-2|§C9.1, Remark: What Lecture 11 adds to the four pieces]]; determinants: [[§C9.1 Discrete Lorentz Transformations#^cau-c9-1-2|§C9.1, Caution: Slide 7's determinants]]; dimensions: [[§C9.1 Discrete Lorentz Transformations#^cau-c9-1-1|§C9.1, Caution: Parity depends on the number of space dimensions]].
> - Components of $O(1,3)$: Theorem [[§CB.3 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-3-12|§CB.3.12]] The Four Components Are the Cosets of SO⁺(1,3).

### Parity matrix, parity images and their identities

$\mathcal P^\mu{}_\nu = \operatorname{diag}(1, -1, -1, -1)$, $\tilde x = (t, -\mathbf x)$, $\tilde p = (p^0, -\mathbf p)$, with $\mathcal P^2 = \mathbb 1$, $\tilde p\cdot\tilde q = p\cdot q$, $\tilde p\cdot x = p\cdot\tilde x$, the chain rule for $f(\tilde x)$ and $E_{-\mathbf p} = E_{\mathbf p}$, see Definition [[§C9.1 Discrete Lorentz Transformations#^def-c9-1-2|§C9.1.2]] Parity Matrix and Parity Images and Theorem [[§C9.1 Discrete Lorentz Transformations#^thm-c9-1-1|§C9.1.1]] Identities of the Parity Matrix. *Source: Lecture 11 (Oct 7), slides 12, 14 ("$\tilde px = p\tilde x$") · PS §3.6, p. 65*

^nd-def-c9-1-2

- [ ] Q1 **[def]** Define $\mathcal P^\mu{}_\nu$, $\tilde x$ and $\tilde p$. Is $\tilde p$ on shell when $p$ is?
- [ ] Q2 Prove $\tilde p\cdot x = p\cdot\tilde x$ in components.
- [ ] Q3 For $g(x) = f(\tilde x)$, compute $\partial_\mu g$ by the chain rule.
- [ ] Q4 **[why]** Why may $\mathbf p \to -\mathbf p$ be substituted in $\int d^3p$ without changing $E_{\mathbf p}$ or the measure?

> [!tip]- Hints: route in the notes
> - Technique: K2, K9.
> - Steps 1–5 under Theorem [[§C9.1 Discrete Lorentz Transformations#^thm-c9-1-1|§C9.1.1]] Identities of the Parity Matrix.

### Parity on the Hilbert space of the Dirac field

$U(\mathcal P)\hat a^s_{\mathbf p}U(\mathcal P)^{-1} = \eta_a\hat a^s_{-\mathbf p}$, $U(\mathcal P)\hat b^s_{\mathbf p}U(\mathcal P)^{-1} = \eta_b\hat b^s_{-\mathbf p}$, $U(\mathcal P)|0\rangle = |0\rangle$, unitary, phases of modulus 1, spin label untouched, see Definition [[§C9.3 Parity on States, Spinors and the Dirac Field#^def-c9-3-1|§C9.3.1]] Parity on the Hilbert Space of the Dirac Field. *Source: Lecture 11 (Oct 7), slides 10–11 · PS §3.6, eq. (3.123)*

^nd-def-c9-3-1

- [ ] Q1 **[def]** State the definition: action on both annihilators and on the vacuum.
- [ ] Q2 **[why]** Why do momentum flip and spin stay ($\mathbf s \sim \mathbf x \times \mathbf p$)?
- [ ] Q3 **[why]** Why does acting on the oscillators and the vacuum fix $U(\mathcal P)$ on every state, multiparticle and antiparticle states included?
- [ ] Q4 **[why]** Check that the definition respects $\{\hat a, \hat a^\dagger\} = (2\pi)^3\delta\delta$ and $\hat a|0\rangle = 0$.
- [ ] Q5 **[conv]** "$\eta$ means three things" in this chapter: which?

> [!tip]- Hints: route in the notes
> - Technique: K15 (act on modes).
> - [[§C9.3 Parity on States, Spinors and the Dirac Field#^rem-c9-3-2|§C9.3, Remark: Reading the definition]] (reading the definition); [[§C9.3 Parity on States, Spinors and the Dirac Field#^cau-c9-3-2|§C9.3, Caution: η means three things]].

### U(𝒫)…U(𝒫)⁻¹ versus P…P and P⁻¹…P

The course conjugates as $U(\mathcal P)\,\mathcal O\,U(\mathcal P)^{-1}$ (Problem Set 6: $\mathcal P\psi\mathcal P^\dagger$); PS write $P\mathcal OP$; Yu writes $P^{-1}\mathcal OP$; the two orders differ by conjugating the phases, see [[§C9.3 Parity on States, Spinors and the Dirac Field#^cau-c9-3-1|§C9.3, Caution: Which side the inverse is on, and the names of the phases]]. *Source: Lecture 11 (Oct 7), slide 11 ("PS writes POP which has different phases") · Problem Set 6, conventions before Problem 1 · PS eq. (3.123) · Yu (9.2)–(9.6)*

^nd-cau-c9-3-1

- [ ] Q1 **[state]** Write the parity law on $\hat a^s_{\mathbf p}$ in the course's form, in PS's form and in Yu's form.
- [ ] Q2 **[conv]** Replacing $U$ by $U^{-1}$: what happens to each phase?
- [ ] Q3 **[why]** When do all three forms coincide?
- [ ] Q4 **[conv]** Problem Set 6 writes $\mathcal P$, $\mathcal C$, $\mathcal T$ for the Hilbert-space operators. How do they relate to $U(\mathcal P)$, $U(\mathcal C)$, $U(\mathcal T)$, and what does Problem Set 6 say about the abbreviations $P = \gamma^0$, $C = -i\gamma^0\gamma^2$, $T = \gamma^1\gamma^3$?
- [ ] Q5 **[why]** Why does Larsen prefer the form with $U^{-1}$ (or $\mathcal P^\dagger$) on the right?

> [!tip]- Hints: route in the notes
> - The caution's bullets; register row "Parity on the Hilbert space".
> - Problem Set 6's preamble: unitarity manifest; $\mathcal P^\dagger$ and $\mathcal P$ differ by a phase.

### Intrinsic parity

The intrinsic parity of a species is the phase its one-particle state acquires under parity apart from the momentum flip: $\eta_a^{\ast}$ for the fermion, $\eta_b^{\ast}$ for the antifermion; at rest it is an eigenvalue of $U(\mathcal P)$, see Definition [[§C9.3 Parity on States, Spinors and the Dirac Field#^def-c9-3-3|§C9.3.3]] Intrinsic Parity. *Source: Lecture 11 (Oct 7), slide 16*

^nd-def-c9-3-3

- [ ] Q1 **[def]** Define intrinsic parity.
- [ ] Q2 **[conv]** Slide 16 writes "$U(\mathcal P)|\mathbf p, s\rangle = \eta_a|\mathbf p, s\rangle$". What is wrong with it, and when is it an eigenvalue equation?
- [ ] Q3 **[why]** Why is it $\eta_a^{\ast}$ and not $\eta_a$ on the state?

> [!tip]- Hints: route in the notes
> - Theorem [[§C9.3 Parity on States, Spinors and the Dirac Field#^thm-c9-3-1|§C9.3.1]] Parity on Creation Operators and One-Particle States; [[§C9.3 Parity on States, Spinors and the Dirac Field#^cau-c9-3-4|§C9.3, Caution: Slide 16's eigenvalue equation]].

### Names and signs of the fermion bilinears

$\mathsf S = \bar\psi\psi$, $\mathsf P = \bar\psi\,i\gamma^5\psi$, $\mathsf V^\mu = \bar\psi\gamma^\mu\psi$, $\mathsf A^\mu = \bar\psi\gamma^\mu\gamma^5\psi$, $\mathsf T^{\mu\nu} = \bar\psi\sigma^{\mu\nu}\psi$; the lecture writes the pseudoscalar without the $i$; slide 19's $\gamma^5$ has a typo; the vector rule is written $(-)^\mu$ or with a lowered index, see [[§C9.4 Fermion Bilinears under Parity#^cau-c9-4-1|§C9.4, Caution: The i in the pseudoscalar]]. *Source: Lecture 11 (Oct 7), slides 19, 22–23 · PS eq. (3.127) · register row "Fermion bilinears"*

^nd-cau-c9-4-1

- [ ] Q1 **[def]** List the five bilinears with their matrices and count their components to 16.
- [ ] Q2 **[conv]** Why does the notes' pseudoscalar carry an $i$? What is $(\bar\psi\gamma^5\psi)^\dagger$?
- [ ] Q3 **[conv]** Slide 19 writes "$\gamma^5 \equiv i\gamma^0\gamma^1\gamma^2\gamma^4$". Correct it, and give $\gamma^5$ in the chiral basis.
- [ ] Q4 **[conv]** What is "$(-)^\mu$", why is it not a tensor, and why did Larsen call "$\mathsf V^\mu \to \mathsf V_\mu$" abusive notation? How do the notes write the rule instead?

> [!tip]- Hints: route in the notes
> - [[§C9.4 Fermion Bilinears under Parity#^cau-c9-4-1|§C9.4, Caution: The i in the pseudoscalar]], [[§C9.4 Fermion Bilinears under Parity#^cau-c9-4-2|§C9.4, Caution: Slide 19's γ⁵]], [[§C9.4 Fermion Bilinears under Parity#^cau-c9-4-3|§C9.4, Caution: The (−1)^μ notation and the lowered index of slide 23]]; definitions Definition [[§C5a.6 The Dirac Conjugate and the Bilinears#^def-c5a-6-2|§C5a.6.2]] The Sixteen Bilinears.

### Discrete symmetries: optional, mandatory, and in nature

Continuous Lorentz transformations must be symmetries; $C$, $P$, $T$ need not be; $CPT$ is a symmetry of every local Lorentz-invariant QFT. QED and QCD respect $C$, $P$, $T$; the weak interaction violates $P$ and $C$ maximally; $CP$ and $T$ are violated slightly, see [[§C9.4 Fermion Bilinears under Parity#^rem-c9-4-3|§C9.4, Remark: Mandatory and optional symmetries]] and [[§C9.4 Fermion Bilinears under Parity#^rem-c9-4-4|§C9.4, Remark: Discrete symmetries in nature]]. *Source: Lecture 11 (Oct 7), slides 24–26 · Lecture 12 (Oct 12), slide 24*

^nd-rem-c9-4-4

- [ ] Q1 **[state]** Which transformations must a relativistic QFT respect, which may it violate, and which can it not violate?
- [ ] Q2 **[state]** Which of $C$, $P$, $T$, $CP$, $CPT$ do QED, QCD and the weak interaction respect?
- [ ] Q3 **[why]** Give a QED-like coupling that would violate parity.
- [ ] Q4 **[why]** Why is $CP$ violation equivalent to $T$ violation?
- [ ] Q5 **[why]** Why is it hard to "test" $CPT$, and what is tested instead?

> [!tip]- Hints: route in the notes
> - Technique: none (short response).
> - Axial coupling: Theorem [[§C9.4 Fermion Bilinears under Parity#^thm-c9-4-4|§C9.4.4]] The Sixteen Bilinears under Parity, rows 3–4; consequences: [[§C9.9 CPT and the CPT Theorem#^rem-c9-9-2|§C9.9, Remark: Consequences of the CPT theorem, and the status of the discrete symmetries]].

### Charge conjugation on the Hilbert space

$U(\mathcal C)\hat a^s_{\mathbf p}U(\mathcal C)^{-1} = \hat b^s_{\mathbf p}$, $U(\mathcal C)\hat b^s_{\mathbf p}U(\mathcal C)^{-1} = \hat a^s_{\mathbf p}$, $U(\mathcal C)|0\rangle = |0\rangle$, unitary, momentum and spin label kept, phases set to 1, see Definition [[§C9.5 Charge Conjugation on Oscillators and Spinors#^def-c9-5-1|§C9.5.1]] Charge Conjugation on the Hilbert Space. *Source: Lecture 12 (Oct 12), slide 5 · PS eq. (3.143)*

^nd-def-c9-5-1

- [ ] Q1 **[def]** State the definition.
- [ ] Q2 **[why]** Why may both phases be set to 1 here, when for parity they could not both be 1?
- [ ] Q3 Derive the action on the creators and on $|\mathbf p, s\rangle$, $|\mathbf p, s\rangle^c$.
- [ ] Q4 **[why]** What does "a particle of spin $s$ becomes the antiparticle of the same spin $s$" require of the antiparticle spinors?

> [!tip]- Hints: route in the notes
> - Technique: K15.
> - [[§C9.5 Charge Conjugation on Oscillators and Spinors#^rem-c9-5-1|§C9.5, Remark: Reading the definition]]; Theorem [[§C9.5 Charge Conjugation on Oscillators and Spinors#^thm-c9-5-1|§C9.5.1]] Charge Conjugation on Creation Operators and One-Particle States; the spin question is [[§C9.7 Physical Spin versus Wave-Function Spin|§C9.7]] Physical Spin versus Wave-Function Spin.

### The transposed adjoint of the field operator

$\hat\psi^{\dagger\mathsf T} \equiv (\hat\psi^\dagger)^{\mathsf T}$, $(\hat\psi^{\dagger\mathsf T})_a = (\hat\psi_a)^\dagger$: dagger on operators, complex conjugation on numbers, still a column; the lecture's "star" $\hat\psi^{\ast}$, PS's $\psi^{\ast}$ (3.145), see Definition [[§C9.5 Charge Conjugation on Oscillators and Spinors#^def-c9-5-2|§C9.5.2]] The Transposed Adjoint of a Field Operator and Theorem [[§C9.5 Charge Conjugation on Oscillators and Spinors#^thm-c9-5-2|§C9.5.2]] Mode Expansion of the Transposed Adjoint. *Source: Lecture 12 (Oct 12), slides 6, 9, 26 · PS eq. (3.145) · register row "Transposed adjoint"*

^nd-def-c9-5-2

- [ ] Q1 **[def]** Define $\hat\psi^{\dagger\mathsf T}$ component by component.
- [ ] Q2 Write its mode expansion: which operators multiply $u^s(p)^{\ast}$ and $v^s(p)^{\ast}$, and with which exponentials?
- [ ] Q3 **[conv]** Why did the lecture prefer a star to a dagger ("columns stay columns")? How do PS and Yu write it?
- [ ] Q4 **[conv]** For a scalar operator, what is the "star" $\hat\phi^{\ast}$ of Problem Set 7?

> [!tip]- Hints: route in the notes
> - Technique: K9.
> - Steps 1–2 under Theorem [[§C9.5 Charge Conjugation on Oscillators and Spinors#^thm-c9-5-2|§C9.5.2]] Mode Expansion of the Transposed Adjoint; names [[§C9.5 Charge Conjugation on Oscillators and Spinors#^cau-c9-5-1|§C9.5, Caution: Names for the transposed adjoint]]; scalar [[§C9.10 C, T and CPT for the Complex Scalar Field#^cau-c9-10-1|§C9.10, Caution: The star of a scalar field operator is the adjoint]].

### Flipped two-spinors and the label −s

$\xi^{-s} \equiv -i\sigma^2(\xi^s)^{\ast}$; for any family $X^s$, $X^{-1} \equiv X^2$, $X^{-2} \equiv -X^1$, so $X^{-(-s)} = -X^s$, see Definition [[§C9.5 Charge Conjugation on Oscillators and Spinors#^def-c9-5-3|§C9.5.3]] The Flipped Two-Spinor and Definition [[§C9.5 Charge Conjugation on Oscillators and Spinors#^def-c9-5-4|§C9.5.4]] The Label −s. *Source: Lecture 12 (Oct 12), slide 7 · PS eqs. (3.134)–(3.135), (3.137)*

^nd-def-c9-5-3

- [ ] Q1 **[def]** Define $\xi^{-s}$ and the label rule $X^{-s}$.
- [ ] Q2 Compute $-i\sigma^2(\xi^1)^{\ast}$ and $-i\sigma^2(\xi^2)^{\ast}$ for the standard basis.
- [ ] Q3 Compute the same for the helicity spinors $\xi^\uparrow$, $\xi^\downarrow$ of slide 7.
- [ ] Q4 **[conv]** The handwritten notes write "$i\sigma^2(\xi^s)^{\ast}$". Which sign is right, and what is the image of $s = 2$?
- [ ] Q5 **[why]** Why does flipping twice give $-X^s$?

> [!tip]- Hints: route in the notes
> - Example [[§C9.5 Charge Conjugation on Oscillators and Spinors#^ex-c9-5-1|§C9.5.1]] Conjugating the Helicity and the Standard Two-Spinors; [[§C9.5 Charge Conjugation on Oscillators and Spinors#^cau-c9-5-2|§C9.5, Caution: The sign in ξ^{−s}]].

### The antiparticle two-spinors η^s = ξ^{−s}

From Lecture 12 on, $\eta^s = \xi^{-s} = -i\sigma^2(\xi^s)^{\ast}$, so $\eta^1 = (0, 1)^{\mathsf T}$, $\eta^2 = (-1, 0)^{\mathsf T}$ for the standard $\xi^s$, see Definition [[§C9.5 Charge Conjugation on Oscillators and Spinors#^def-c9-5-5|§C9.5.5]] The Antiparticle Two-Spinors η^s = ξ^{−s}. *Source: Lecture 12 (Oct 12), slides 8, 14–15 · PS eq. (3.136) · Yu (5.196) · register row "Flipped labels"*

^nd-def-c9-5-5

- [ ] Q1 **[def]** State the choice and write $\eta^1$, $\eta^2$.
- [ ] Q2 **[why]** Why do the $\eta^s$ still form a spin basis, so that the normalizations, orthogonality and spin sums of C5a hold unchanged?
- [ ] Q3 **[why]** Which statements does the choice decide? (What compares the label $s$ of $\hat b^s$ with a spin?)
- [ ] Q4 **[conv]** What did PS §3.5 leave open, and what does PS §3.6 choose? What does Yu choose in the helicity basis?
- [ ] Q5 **[why]** Which two results of Lecture 12 need exactly this choice (one for $C$, one for spin)?

> [!tip]- Hints: route in the notes
> - [[§C9.7 Physical Spin versus Wave-Function Spin#^rem-c9-7-6|§C9.7, Remark: The choice η^s = ξ^{−s} in these notes, Peskin–Schroeder and Yu]] (the choice in the notes, PS and Yu).
> - $C$: Theorem [[§C9.6 Charge Conjugation on the Field and Bilinears#^thm-c9-6-2|§C9.6.2]] Charge Conjugation on the Dirac Field holds if and only if $\eta^s = \xi^{-s}$; spin: Theorem [[§C9.7 Physical Spin versus Wave-Function Spin#^thm-c9-7-3|§C9.7.3]] Particle and Antiparticle Created with Label s Have the Same Physical Spin.

### The charge-conjugation matrix B and the map c

A charge-conjugation matrix is an invertible $B$ with $B(\gamma^\mu)^{\ast}B^{-1} = -\gamma^\mu$; it exists, is unique up to a factor, unitary in a Hermitian basis with $BB^{\ast} = \mathbb 1$; $c(\psi) = B\psi^{\ast}$ is an antilinear real structure commuting with the spinor Lorentz matrices; in the chiral basis $B = -i\gamma^2$, see Definition [[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^def-cb-18-18|§CB.18.18]] The Charge-Conjugation Matrix, Theorem [[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-18-19|§CB.18.19]] Existence and Uniqueness of the Charge-Conjugation Matrix, and Its Square under Conjugation and Definition [[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^def-cb-18-20|§CB.18.20]] The Charge-Conjugation Map. *Source: written beyond Lecture 12 at the user's question (2026-10-12) · PS eqs. (3.144)–(3.145) (the matrix $-i\gamma^2$, unnamed) · Yu (9.98), (9.112)*

^nd-def-cb-18-18

- [ ] Q1 **[def]** Define a charge-conjugation matrix and the charge-conjugation map.
- [ ] Q2 **[why]** Why are $(\gamma^\mu)^{\ast}$ and $-\gamma^\mu$ again Dirac matrices, and why does that give existence and uniqueness of $B$ (which theorem)?
- [ ] Q3 Check that $B = -i\gamma^2$ works in the chiral basis: which $\gamma$ is imaginary?
- [ ] Q4 **[why]** Why does $c$ commute with every $\Lambda_{1/2}$ (so $c\psi$ transforms like $\psi$) although it anticommutes with each $\gamma^\mu$?
- [ ] Q5 **[conv]** How does $B$ change under a change of basis, and how is Yu's matrix $\mathcal C$ related to it?

> [!tip]- Hints: route in the notes
> - Technique: K16 (intertwiner), K5.
> - Theorem [[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-18-19|§CB.18.19]] Existence and Uniqueness of the Charge-Conjugation Matrix, and Its Square under Conjugation (Pauli's theorem; sign of $BB^{\ast}$), Theorem [[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-18-21|§CB.18.21]] The Charge-Conjugation Map Is a Real Structure Commuting with the Spinor Lorentz Matrices, Example [[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^ex-cb-18-22|§CB.18.22]] The Charge-Conjugation Matrix in Three Bases, and the Transpose Form; basis remark [[§C9.5 Charge Conjugation on Oscillators and Spinors#^cau-c9-5-4|§C9.5, Caution: −iγ² is a statement about the chiral basis]].

### Wave-function spin, the spin operator and physical spin

Wave-function spin is the $\frac12\sigma^3$ eigenvalue of the two-spinor in $u$ or $v$; the spin operator is $\hat{\mathbf S} = \int d^3x\,\hat\psi^\dagger\frac12\boldsymbol\Sigma\hat\psi$ with $\frac12\Sigma^3 = S^{12}$; physical spin is the eigenvalue of $\hat S^3$ on the state, see Definition [[§C9.7 Physical Spin versus Wave-Function Spin#^def-c9-7-1|§C9.7.1]] Wave-Function Spin, Definition [[§C9.7 Physical Spin versus Wave-Function Spin#^def-c9-7-2|§C9.7.2]] The Spin Operator of the Dirac Field, Definition [[§C9.7 Physical Spin versus Wave-Function Spin#^def-c9-7-3|§C9.7.3]] Physical Spin. *Source: Lecture 12 (Oct 12), slides 14–16 · PS eq. (3.111)*

^nd-def-c9-7-3

- [ ] Q1 **[def]** Define the three notions.
- [ ] Q2 **[def]** Write $\Sigma^3$ as a $4\times4$ matrix and relate it to $S^{12}$.
- [ ] Q3 **[state]** For an antiparticle, how are wave-function spin and physical spin related (slide 14)?
- [ ] Q4 **[why]** "Don't trust the wave functions": state the principle the lecture drew from this.

> [!tip]- Hints: route in the notes
> - [[§C9.7 Physical Spin versus Wave-Function Spin#^rem-c9-7-1|§C9.7, Remark: The puzzle]] (the puzzle); Principle [[§C9.7 Physical Spin versus Wave-Function Spin#^pr-c9-7-4|§C9.7.4]] Physical Spin Is the Eigenvalue of an Operator.

### Time reversal on the oscillators; the time-reversed point

$x_T = (-t, \mathbf x) = -\tilde x$; $U(\mathcal T)\hat a^s_{\mathbf p}U(\mathcal T)^{-1} = \hat a^{-s}_{-\mathbf p}$, $U(\mathcal T)\hat b^s_{\mathbf p}U(\mathcal T)^{-1} = \hat b^{-s}_{-\mathbf p}$, $U(\mathcal T)|0\rangle = |0\rangle$, with $\hat a^{-1} = \hat a^2$, $\hat a^{-2} = -\hat a^1$, see Definition [[§C9.8 Time Reversal#^def-c9-8-1|§C9.8.1]] The Time-Reversed Point and Definition [[§C9.8 Time Reversal#^def-c9-8-2|§C9.8.2]] Time Reversal on the Oscillators. *Source: Lecture 12 (Oct 12), slide 19 · PS eqs. (3.137)–(3.138)*

^nd-def-c9-8-2

- [ ] Q1 **[def]** Define $x_T$ and the action of $U(\mathcal T)$ on the oscillators.
- [ ] Q2 **[why]** Why do both momentum and spin flip ("a movie run backwards"), and why is the particle not turned into an antiparticle?
- [ ] Q3 **[def]** What does $\hat a^{-s}$ mean for $s = 1$ and for $s = 2$?
- [ ] Q4 **[state]** What form of law on the field is the goal (slide 19)?

> [!tip]- Hints: route in the notes
> - [[§C9.8 Time Reversal#^rem-c9-8-1|§C9.8, Remark: A movie run backwards]]; label rule Definition [[§C9.5 Charge Conjugation on Oscillators and Spinors#^def-c9-5-4|§C9.5.4]] The Label −s.

### Signs and names for time reversal in PS, Yu and Problem Set 6

The course: $U(\mathcal T)\hat\psi(t, \mathbf x)U(\mathcal T)^{-1} = \gamma^1\gamma^3\hat\psi(-t, \mathbf x)$; PS (3.139): $T\psi T = (-\gamma^1\gamma^3)\psi(-t, \mathbf x)$, an overall sign, a phase of $U(\mathcal T)$; Yu: $D(\mathcal T) = \mathcal C\gamma^5 = \gamma^1\gamma^3$, see [[§C9.8 Time Reversal#^cau-c9-8-4|§C9.8, Caution: Signs and names in Peskin–Schroeder and Yu]]. *Source: Lecture 12 (Oct 12), slides 22, 26 · Problem Set 6, conventions · PS eqs. (3.138)–(3.140) · Yu (9.202), (9.209)*

^nd-cau-c9-8-4

- [ ] Q1 **[state]** Write the course's law and PS's law for $T$ on $\psi$ and on $\bar\psi$.
- [ ] Q2 **[conv]** Why is the sign difference harmless? What would you have to change in $U(\mathcal T)$ to switch?
- [ ] Q3 **[conv]** What does Problem Set 6 mean by "$\mathcal Tc\mathcal T^\dagger = c^{\ast}$ on any complex number (including Dirac matrices)"?
- [ ] Q4 **[conv]** What is PS's spinor relation on p. 68, and how does it compare with the course's $u^s(p)^{\ast} = \gamma^1\gamma^3u^{-s}(\tilde p)$?

> [!tip]- Hints: route in the notes
> - The caution's bullets; Theorem [[§C9.8 Time Reversal#^thm-c9-8-5|§C9.8.5]] Time Reversal on the Positive-Frequency Spinors, Theorem [[§C9.8 Time Reversal#^thm-c9-8-7|§C9.8.7]] Time Reversal on the Dirac Field; register row "Time reversal on the Hilbert space".

### The CPT operator Θ

$\Theta \equiv U(\mathcal C)U(\mathcal P)U(\mathcal T)$, acting as $\Theta\hat{\mathcal O}\Theta^{-1}$: first $\mathcal T$, then $\mathcal P$, then $\mathcal C$; "any order will do" up to signs and phases, see Definition [[§C9.9 CPT and the CPT Theorem#^def-c9-9-1|§C9.9.1]] The CPT Operator Θ. *Source: Lecture 12 (Oct 12), slide 24 · Problem Set 7, Problem 3 ($\Theta \equiv CPT$) · Yu (9.320)*

^nd-def-c9-9-1

- [ ] Q1 **[def]** Define $\Theta$ and say which transformation acts first on an operator.
- [ ] Q2 **[why]** Why does the innermost conjugation act first?
- [ ] Q3 Write $\Theta^{-1}$.
- [ ] Q4 **[why]** Which of the three factors is antilinear, and what does that make $\Theta$?

> [!tip]- Hints: route in the notes
> - Theorem [[§C9.9 CPT and the CPT Theorem#^thm-c9-9-2|§C9.9.2]] Θ Is Antiunitary.

### The discrete transformations of the Dirac field in one statement

$U(\mathcal P)\hat\psi(t, \mathbf x)U(\mathcal P)^{-1} = \eta_a\gamma^0\hat\psi(t, -\mathbf x)$, $U(\mathcal C)\hat\psi(x)U(\mathcal C)^{-1} = -i\gamma^2\hat\psi^{\dagger\mathsf T}(x)$, $U(\mathcal T)\hat\psi(t, \mathbf x)U(\mathcal T)^{-1} = \gamma^1\gamma^3\hat\psi(-t, \mathbf x)$, $\Theta\hat\psi(x)\Theta^{-1} = \eta_a\gamma^5\hat\psi^{\dagger\mathsf T}(-x)$, see [[§C9.9 CPT and the CPT Theorem#^rem-c9-9-3|§C9.9, Remark: The discrete transformations of the Dirac field in one statement]]. *Source: Lecture 12 (Oct 12), slide 26 · Problem Set 6 and 7 conventions*

^nd-rem-c9-9-3

- [ ] Q1 **[state]** Write the four laws from memory, with their points and which operators are unitary or antiunitary.
- [ ] Q2 **[conv]** Slide 26 writes the parity law with $(t, \mathbf x)$ on both sides. Correct it.
- [ ] Q3 **[conv]** Write the $C$ law in the form of Problem Set 6 (through $\bar\psi$).
- [ ] Q4 **[why]** Which $\gamma$'s appear in $P$, $C$, $T$, and what is their product?

> [!tip]- Hints: route in the notes
> - [[§C9.9 CPT and the CPT Theorem#^cau-c9-9-3|§C9.9, Caution: Slide 26's parity rule]]; Theorem [[§C9.6 Charge Conjugation on the Field and Bilinears#^thm-c9-6-3|§C9.6.3]] Charge Conjugation through the Dirac Conjugate; [[§C9.9 CPT and the CPT Theorem#^rem-c9-9-1|§C9.9, Remark: Each γ once]] and Theorem [[§C9.9 CPT and the CPT Theorem#^thm-c9-9-1|§C9.9.1]] The Three Matrices Multiply to γ⁵.

### The star of a scalar field operator

Problem Set 7's $\phi^{\ast}$ for the operator is $\hat\phi^\dagger$; for the Dirac field the operator star is $\hat\psi^{\dagger\mathsf T}$, which for a single component is the adjoint, see [[§C9.10 C, T and CPT for the Complex Scalar Field#^cau-c9-10-1|§C9.10, Caution: The star of a scalar field operator is the adjoint]]. *Source: Problem Set 7, Problem 4 (the user's solution) · PS Problem 3.7*

^nd-cau-c9-10-1

- [ ] Q1 **[def]** What does $\phi^{\ast}$ mean in Problem Set 7 for the quantum field?
- [ ] Q2 **[conv]** How is Problem Set 7's current $J^\mu$ related to the notes' $\hat j^\mu$?
- [ ] Q3 **[why]** Why is $\hat\phi^{\dagger\mathsf T} = \hat\phi^\dagger$?

> [!tip]- Hints: route in the notes
> - [[§C9.10 C, T and CPT for the Complex Scalar Field#^cau-c9-10-1|§C9.10, Caution: The star of a scalar field operator is the adjoint]]; Theorem [[§C9.10 C, T and CPT for the Complex Scalar Field#^thm-c9-10-4|§C9.10.4]] The U(1) Current under P, C and T.

## Derivations T10

### Parity on creators and one-particle states ★★

$U(\mathcal P)\hat a^{s\dagger}_{\mathbf p}U(\mathcal P)^{-1} = \eta_a^{\ast}\hat a^{s\dagger}_{-\mathbf p}$, $U(\mathcal P)\hat b^{s\dagger}_{\mathbf p}U(\mathcal P)^{-1} = \eta_b^{\ast}\hat b^{s\dagger}_{-\mathbf p}$, so $U(\mathcal P)|\mathbf p, s\rangle = \eta_a^{\ast}|-\mathbf p, s\rangle$, see Theorem [[§C9.3 Parity on States, Spinors and the Dirac Field#^thm-c9-3-1|§C9.3.1]] Parity on Creation Operators and One-Particle States. *Source: Lecture 11 (Oct 7), slides 10–11*

^nd-thm-c9-3-1

- [ ] Q1 **[state]** State the action on both creators and both one-particle states.
- [ ] Q2 Take the adjoint of $U\hat a^s_{\mathbf p}U^{-1} = \eta_a\hat a^s_{-\mathbf p}$: why does the phase get conjugated, and why is $(U^{-1})^\dagger = U$?
- [ ] Q3 Insert $U^{-1}U$ before the vacuum and use $U|0\rangle = |0\rangle$.
- [ ] Q4 **[why]** Why does $\sqrt{2E_{\mathbf p}}$ not change under $\mathbf p \to -\mathbf p$?

> [!tip]- Hints: route in the notes
> - Technique: K15.
> - Steps 1–2 under Theorem [[§C9.3 Parity on States, Spinors and the Dirac Field#^thm-c9-3-1|§C9.3.1]] Parity on Creation Operators and One-Particle States.

### Parity on the spinors u and v ★★

$p\cdot\sigma = \tilde p\cdot\bar\sigma$ and $p\cdot\bar\sigma = \tilde p\cdot\sigma$, hence $u^s(p) = \gamma^0u^s(\tilde p)$ and $v^s(p) = -\gamma^0v^s(\tilde p)$; $\Lambda_{1/2}(\mathcal P) = \gamma^0$, see Theorem [[§C9.3 Parity on States, Spinors and the Dirac Field#^thm-c9-3-2|§C9.3.2]] Parity Exchanges p·σ and p·σ̄, Theorem [[§C9.3 Parity on States, Spinors and the Dirac Field#^thm-c9-3-3|§C9.3.3]] Parity on the Positive-Frequency Spinors, Theorem [[§C9.3 Parity on States, Spinors and the Dirac Field#^thm-c9-3-4|§C9.3.4]] Parity on the Negative-Frequency Spinors, Definition [[§C9.3 Parity on States, Spinors and the Dirac Field#^def-c9-3-2|§C9.3.2]] The Spinor Matrix of Parity. *Source: Lecture 11 (Oct 7), slides 12–13 ("The overall '−' is important") · PS §3.6, p. 65*

^nd-thm-c9-3-3

- [ ] Q1 **[state]** State the two spinor identities and the spinor matrix of parity.
- [ ] Q2 Prove $p\cdot\sigma = \tilde p\cdot\bar\sigma$ in components. Why does the same hold for the square roots on shell?
- [ ] Q3 Rewrite each half of $u^s(p)$ with tilded momenta: in which order do the square roots now stand?
- [ ] Q4 How does $\gamma^0$ act on a column of two two-component blocks? Conclude for $u$.
- [ ] Q5 Repeat for $v$: where does the overall minus sign come from?
- [ ] Q6 **[why]** What do the identities say about the plane waves $u\,e^{-ip\cdot x}$ and $v\,e^{ip\cdot x}$ evaluated at $\tilde x$?

> [!tip]- Hints: route in the notes
> - Technique: K15 (rewrite spinors, read off the matrix), K5.
> - Steps 1–3 under Theorem [[§C9.3 Parity on States, Spinors and the Dirac Field#^thm-c9-3-2|§C9.3.2]] Parity Exchanges p·σ and p·σ̄, 1–4 under Theorem [[§C9.3 Parity on States, Spinors and the Dirac Field#^thm-c9-3-3|§C9.3.3]] Parity on the Positive-Frequency Spinors, 1–4 under Theorem [[§C9.3 Parity on States, Spinors and the Dirac Field#^thm-c9-3-4|§C9.3.4]] Parity on the Negative-Frequency Spinors; plane waves [[§C9.3 Parity on States, Spinors and the Dirac Field#^rem-c9-3-3|§C9.3, Remark: What the identities say about the plane waves]].

### Parity on the Dirac field ★★

$U(\mathcal P)\hat\psi(x)U(\mathcal P)^{-1} = \eta_a\gamma^0\hat\psi(\tilde x)$ if and only if $\eta_b^{\ast} = -\eta_a$, see Theorem [[§C9.3 Parity on States, Spinors and the Dirac Field#^thm-c9-3-5|§C9.3.5]] Parity on the Dirac Field. *Source: Lecture 11 (Oct 7), slides 14–15 · PS eqs. (3.124)–(3.126)*

^nd-thm-c9-3-5

- [ ] Q1 **[state]** State the law and the condition on the phases.
- [ ] Q2 Act on the operators only: what does $U(\mathcal P)$ do to $\hat a^s_{\mathbf p}$ and to $\hat b^{s\dagger}_{\mathbf p}$ inside the expansion, and why do $u$, $v$ and the exponentials ride along?
- [ ] Q3 Change variables $\mathbf p \to -\mathbf p$: what happens to the spinors' arguments and to the exponents?
- [ ] Q4 Move the flip onto $x$ and use the spinor identities: which sign appears in the antiparticle term?
- [ ] Q5 Pull out $\gamma^0$ and compare with $\eta_a\gamma^0\hat\psi(\tilde x)$: what condition makes the two terms match?
- [ ] Q6 **[why]** Why is the condition needed ("unitary transformation of fields, needed for quantum consistency"): what would the transformed field be otherwise?

> [!tip]- Hints: route in the notes
> - Technique: K15, K9.
> - Steps 1–7 under Theorem [[§C9.3 Parity on States, Spinors and the Dirac Field#^thm-c9-3-5|§C9.3.5]] Parity on the Dirac Field; [[§C9.3 Parity on States, Spinors and the Dirac Field#^rem-c9-3-5|§C9.3, Remark: The field, the particles and the waves]]; $U(\mathcal P)$ vs $\gamma^0$: [[§C9.3 Parity on States, Spinors and the Dirac Field#^cau-c9-3-3|§C9.3, Caution: U(𝒫) and γ⁰ are different objects]].

### Fermion and antifermion have opposite intrinsic parity ★★

$\eta_b^{\ast} = -\eta_a \Leftrightarrow \eta_a\eta_b = -1$, so $\eta_a^{\ast}\eta_b^{\ast} = -1$; with real phases $\eta_a = \pm1$, $\eta_b = \mp1$; a fermion–antifermion pair with orbital $L$ has parity $(-1)^{L+1}$, see Theorem [[§C9.3 Parity on States, Spinors and the Dirac Field#^thm-c9-3-6|§C9.3.6]] The Parity Phases Multiply to −1, Theorem [[§C9.3 Parity on States, Spinors and the Dirac Field#^thm-c9-3-7|§C9.3.7]] Particles and Antiparticles Have Opposite Intrinsic Parity, Theorem [[§C9.3 Parity on States, Spinors and the Dirac Field#^thm-c9-3-8|§C9.3.8]] The Parity of a Fermion–Antifermion Pair. *Source: Lecture 11 (Oct 7), slides 15–16 ("Essential for particle/anti-particle bound states") · PS §3.6, pp. 66–67*

^nd-thm-c9-3-7

- [ ] Q1 **[state]** State the phase relation, the intrinsic parities and the pair parity.
- [ ] Q2 Prove $\eta_b^{\ast} = -\eta_a \Leftrightarrow \eta_a\eta_b = -1$ using $|\eta| = 1$.
- [ ] Q3 **[why]** Why can no convention (redefining $\hat b \to -\hat b$, or other phases of $u$, $v$) remove the relative sign?
- [ ] Q4 For the pair state, act on each creator and relabel $\mathbf p \to -\mathbf p$: where do $(-1)^L$ and the extra $-1$ come from?
- [ ] Q5 **[why]** What is the parity of the positronium ground state? Compare with a scalar particle–antiparticle pair.

> [!tip]- Hints: route in the notes
> - Technique: K15.
> - Steps 1–3 under Theorem [[§C9.3 Parity on States, Spinors and the Dirac Field#^thm-c9-3-6|§C9.3.6]] The Parity Phases Multiply to −1, Theorem [[§C9.3 Parity on States, Spinors and the Dirac Field#^thm-c9-3-7|§C9.3.7]] Particles and Antiparticles Have Opposite Intrinsic Parity, Theorem [[§C9.3 Parity on States, Spinors and the Dirac Field#^thm-c9-3-8|§C9.3.8]] The Parity of a Fermion–Antifermion Pair; [[§C9.3 Parity on States, Spinors and the Dirac Field#^rem-c9-3-4|§C9.3, Remark: Positronium and the pions]]; scalar Theorem [[§C9.2 Parity of the Scalar Field#^thm-c9-2-9|§C9.2.9]] The Parity of a Scalar Particle–Antiparticle Pair.

### Parity on ψ̄ and on a general bilinear ★★

$U(\mathcal P)\hat{\bar\psi}(x)U(\mathcal P)^{-1} = \eta_a^{\ast}\hat{\bar\psi}(\tilde x)\gamma^0$ and $U(\mathcal P)\hat{\bar\psi}\Gamma\hat\psi(x)U(\mathcal P)^{-1} = \hat{\bar\psi}(\tilde x)(\gamma^0\Gamma\gamma^0)\hat\psi(\tilde x)$, see Theorem [[§C9.4 Fermion Bilinears under Parity#^thm-c9-4-1|§C9.4.1]] Parity on the Dirac Conjugate Field and Theorem [[§C9.4 Fermion Bilinears under Parity#^thm-c9-4-2|§C9.4.2]] Parity on a Bilinear. *Source: Lecture 11 (Oct 7), slide 21 ("Take adjoint and right-multiply by $\gamma^0$") · PS eqs. (3.128)–(3.132)*

^nd-thm-c9-4-2

- [ ] Q1 **[state]** State both laws.
- [ ] Q2 Why does conjugation by a unitary commute with taking the adjoint?
- [ ] Q3 Take the adjoint of the field law and right-multiply by $\gamma^0$: where do $(\gamma^0)^\dagger = \gamma^0$ and the phase go?
- [ ] Q4 Insert $U^{-1}U$ between the fields of a bilinear: why do the phases cancel?
- [ ] Q5 **[why]** "$U(\mathcal P)$, $U(\mathcal P)^{-1}$ act on operators $\hat a$, $\hat a^\dagger$, not on $\gamma$-matrices" (slide 21): why is that true for $P$ and $C$ but not for $T$?

> [!tip]- Hints: route in the notes
> - Technique: K7 (conjugating bilinears), K15.
> - Steps 1–3 under Theorem [[§C9.4 Fermion Bilinears under Parity#^thm-c9-4-1|§C9.4.1]] Parity on the Dirac Conjugate Field, 1–4 under Theorem [[§C9.4 Fermion Bilinears under Parity#^thm-c9-4-2|§C9.4.2]] Parity on a Bilinear; contrast [[§C9.8 Time Reversal#^cau-c9-8-1|§C9.8, Caution: This goes against everything said so far]].

### The bilinears under parity: scalar, pseudoscalar, vector ★★

$\gamma^0\mathbb 1\gamma^0 = \mathbb 1$, $\gamma^0(i\gamma^5)\gamma^0 = -i\gamma^5$, $\gamma^0\gamma^\mu\gamma^0 = \mathcal P^\mu{}_\nu\gamma^\nu$; hence $\mathsf S \to +\mathsf S(\tilde x)$, $\mathsf P \to -\mathsf P(\tilde x)$, $\mathsf V^\mu \to \mathcal P^\mu{}_\nu\mathsf V^\nu(\tilde x)$, see Theorem [[§C9.4 Fermion Bilinears under Parity#^thm-c9-4-3|§C9.4.3]] Conjugating the Sixteen Matrices by γ⁰ and Theorem [[§C9.4 Fermion Bilinears under Parity#^thm-c9-4-4|§C9.4.4]] The Sixteen Bilinears under Parity. *Source: Lecture 11 (Oct 7), slides 21–23*

^nd-thm-c9-4-4

- [ ] Q1 **[state]** State the parity column of the table for $\mathsf S$, $\mathsf P$, $\mathsf V^\mu$, with the points.
- [ ] Q2 Compute $\gamma^0\gamma^5\gamma^0$: which property of $\gamma^5$ is used?
- [ ] Q3 Compute $\gamma^0\gamma^\mu\gamma^0$ for $\mu = 0$ and $\mu = i$.
- [ ] Q4 **[why]** "Pseudo" means what? Compare with angular momentum among the vectors.
- [ ] Q5 **[why]** Scalar and pseudoscalar are indistinguishable under continuous Lorentz transformations: why does $\gamma^5$ commute with $\Lambda_{1/2}$ but not with $\gamma^0$?

> [!tip]- Hints: route in the notes
> - Technique: K5, K7.
> - Steps 1–3 under Theorem [[§C9.4 Fermion Bilinears under Parity#^thm-c9-4-3|§C9.4.3]] Conjugating the Sixteen Matrices by γ⁰ and Theorem [[§C9.4 Fermion Bilinears under Parity#^thm-c9-4-4|§C9.4.4]] The Sixteen Bilinears under Parity; [[§C9.4 Fermion Bilinears under Parity#^rem-c9-4-2|§C9.4, Remark: Pseudo is to bilinears what axial is to J]].

### Axial vector and tensor under parity ★ [class exercise, Lecture 11]

$\mathsf A^\mu \to -\mathcal P^\mu{}_\nu\mathsf A^\nu(\tilde x)$ and $\mathsf T^{\mu\nu} \to \mathcal P^\mu{}_\rho\mathcal P^\nu{}_\sigma\mathsf T^{\rho\sigma}(\tilde x)$, see Theorem [[§C9.4 Fermion Bilinears under Parity#^thm-c9-4-4|§C9.4.4]] The Sixteen Bilinears under Parity, rows 4–5. *Source: Lecture 11 (Oct 7), transcript ("this one forms the opposite way. That's an exercise") · Problem Set 7, Problem 2(a)*

^nd-der-c9-4-4b

→ drilled as [[PHY 513 PS Drill#^ps7-2-a|PS7.2(a)]]

### The free Dirac Lagrangian is parity invariant ★★

$U(\mathcal P)\hat{\mathcal L}(x)U(\mathcal P)^{-1} = \hat{\mathcal L}(\tilde x)$ and the action is invariant, see Theorem [[§C9.4 Fermion Bilinears under Parity#^thm-c9-4-5|§C9.4.5]] The Free Dirac Lagrangian Is Parity Invariant. *Source: Lecture 11 (Oct 7), slide 23*

^nd-thm-c9-4-5

- [ ] Q1 **[state]** State the result for $\hat{\mathcal L}$ and for $\hat S$.
- [ ] Q2 The mass term: which row of the table?
- [ ] Q3 The kinetic term: compute $U\partial_\mu\hat\psi U^{-1}$ by the chain rule. Which factor $\mathcal P$ appears from the derivative and which from $\gamma^0\gamma^\mu\gamma^0$?
- [ ] Q4 Contract the two factors of $\mathcal P$: what is left?
- [ ] Q5 **[why]** Why is $\int d^4x\,\hat{\mathcal L}(\tilde x) = \int d^4x\,\hat{\mathcal L}(x)$?

> [!tip]- Hints: route in the notes
> - Technique: K2, K7.
> - Steps 1–6 under Theorem [[§C9.4 Fermion Bilinears under Parity#^thm-c9-4-5|§C9.4.5]] The Free Dirac Lagrangian Is Parity Invariant; $\mathcal P^\mu{}_\rho\mathcal P^\nu{}_\mu = \delta^\nu{}_\rho$, Theorem [[§C9.1 Discrete Lorentz Transformations#^thm-c9-1-1|§C9.1.1]] Identities of the Parity Matrix, 4.

### Parity on the complex scalar field ★

$U(\mathcal P)\hat a_{\mathbf p}U(\mathcal P)^{-1} = \eta_a\hat a_{-\mathbf p}$, $U(\mathcal P)\hat b_{\mathbf p}U(\mathcal P)^{-1} = \eta_b\hat b_{-\mathbf p}$ give $U(\mathcal P)\hat\phi(x)U(\mathcal P)^{-1} = \eta_a\hat\phi(\tilde x)$ if and only if $\eta_b = \eta_a^{\ast}$, see Definition [[§C9.2 Parity of the Scalar Field#^def-c9-2-1|§C9.2.1]] Parity on the Hilbert Space of the Complex Scalar Field and Theorem [[§C9.2 Parity of the Scalar Field#^thm-c9-2-2|§C9.2.2]] Parity on the Complex Scalar Field. *Source: Problem Set 7, Problem 4(a)*

^nd-thm-c9-2-2

→ drilled as [[PHY 513 PS Drill#^ps7-4-a|PS7.4(a)]]

### Scalar parity phases, intrinsic parity and the real field ★

For the complex scalar $\eta_a\eta_b = +1$: particle and antiparticle have the same intrinsic parity, a pair has $(-1)^L$; a real field needs $\eta = \pm1$ (scalar or pseudoscalar), both leaving the free Lagrangian invariant; for a complex field $\eta_a$ alone is a convention, see Theorem [[§C9.2 Parity of the Scalar Field#^thm-c9-2-3|§C9.2.3]] The Scalar Parity Phases Multiply to +1, Theorem [[§C9.2 Parity of the Scalar Field#^thm-c9-2-8|§C9.2.8]] Scalar Particles and Antiparticles Have the Same Intrinsic Parity, Theorem [[§C9.2 Parity of the Scalar Field#^thm-c9-2-10|§C9.2.10]] Parity on the Real Scalar Field, Theorem [[§C9.2 Parity of the Scalar Field#^thm-c9-2-14|§C9.2.14]] The Parity Phase of a Complex Field Is a Convention. *Source: the user's notes Ch. 11; Yu §9.1.1 (written in the notes with Problem Set 7)*

^nd-thm-c9-2-8

- [ ] Q1 **[state]** State the phase condition and the intrinsic-parity statement for the complex scalar, and contrast with the Dirac field.
- [ ] Q2 Real field: why must $\eta$ be real for $\hat\phi \to \eta\hat\phi(\tilde x)$? Define scalar and pseudoscalar fields.
- [ ] Q3 **[why]** Both $\eta = \pm1$ leave the free real Lagrangian invariant: what decides which a real field has?
- [ ] Q4 Show that $e^{-i\theta\hat Q}U(\mathcal P)$ is again a parity operator with $\eta_a' = e^{iq\theta}\eta_a$. What is preserved?
- [ ] Q5 **[why]** In one line: what is the only new input that turns the pair's intrinsic parity from $+1$ (scalar) to $-1$ (Dirac)?

> [!tip]- Hints: route in the notes
> - Technique: K15.
> - Theorem [[§C9.2 Parity of the Scalar Field#^thm-c9-2-3|§C9.2.3]] The Scalar Parity Phases Multiply to +1, Theorem [[§C9.2 Parity of the Scalar Field#^thm-c9-2-8|§C9.2.8]] Scalar Particles and Antiparticles Have the Same Intrinsic Parity, Theorem [[§C9.2 Parity of the Scalar Field#^thm-c9-2-10|§C9.2.10]] Parity on the Real Scalar Field, Definition [[§C9.2 Parity of the Scalar Field#^def-c9-2-3|§C9.2.3]] Scalar and Pseudoscalar Fields, Theorem [[§C9.2 Parity of the Scalar Field#^thm-c9-2-11|§C9.2.11]] The Free Real Lagrangian Is Invariant for Either Parity, Theorem [[§C9.2 Parity of the Scalar Field#^thm-c9-2-14|§C9.2.14]] The Parity Phase of a Complex Field Is a Convention; side by side [[§C9.2 Parity of the Scalar Field#^rem-c9-2-8|§C9.2, Remark: Scalar and spinor parity side by side]]; Dirac freedom [[§C9.2 Parity of the Scalar Field#^rem-c9-2-7|§C9.2, Remark: The same freedom for the Dirac field]].

### The parity of a scalar particle–antiparticle pair ★

For $|\phi\bar\phi\rangle_{LM} = \int d^3p\,\Phi_{LM}(\mathbf p)\,\hat a^\dagger_{\mathbf p}\hat b^\dagger_{-\mathbf p}|0\rangle$ with orbital parity $(-1)^L$, $U(\mathcal P)|\phi\bar\phi\rangle_{LM} = (-1)^L|\phi\bar\phi\rangle_{LM}$: orbital parity times the intrinsic parity $+1$ of the pair, independent of the phase convention, see Theorem [[§C9.2 Parity of the Scalar Field#^thm-c9-2-9|§C9.2.9]] The Parity of a Scalar Particle–Antiparticle Pair and Definition [[§C9.2 Parity of the Scalar Field#^def-c9-2-2|§C9.2.2]] Orbital Parity. *Source: the user's notes Ch. 11; Yu §9.1.1, eq. (9.35) (written in the notes with Problem Set 7)*

^nd-thm-c9-2-9

- [ ] Q1 **[state]** State the pair state and its parity eigenvalue.
- [ ] Q2 **[def]** Define orbital parity: what is $Y^M_L(-\hat{\mathbf p})$ in terms of $Y^M_L(\hat{\mathbf p})$?
- [ ] Q3 Act on each creation operator: which phases appear, and what is their product?
- [ ] Q4 Relabel $\mathbf p \to -\mathbf p$: what happens to $\Phi_{LM}$ and to the measure?
- [ ] Q5 Find the angles of $-\mathbf p$ and use them in the spherical harmonic.
- [ ] Q6 **[why]** Why is the eigenvalue observable although each phase $\eta_a$ is a convention? Compare with a fermion–antifermion pair.

> [!tip]- Hints: route in the notes
> - Technique: K15, K9.
> - Steps 1–6 under Theorem [[§C9.2 Parity of the Scalar Field#^thm-c9-2-9|§C9.2.9]] The Parity of a Scalar Particle–Antiparticle Pair; phases Theorem [[§C9.2 Parity of the Scalar Field#^thm-c9-2-8|§C9.2.8]] Scalar Particles and Antiparticles Have the Same Intrinsic Parity; fermion pair Theorem [[§C9.3 Parity on States, Spinors and the Dirac Field#^thm-c9-3-8|§C9.3.8]] The Parity of a Fermion–Antifermion Pair; [[§C9.2 Parity of the Scalar Field#^rem-c9-2-4|§C9.2, Remark: Parity is a multiplicative quantum number]].

### Conjugation reverses the spin of a two-spinor ★★ [class exercise, Lecture 12]

$J\xi = -i\sigma^2\xi^{\ast}$ is antilinear, preserves inner products up to conjugation, commutes with $SU(2)$, and $(-i\sigma^2)(\frac12\sigma^i)^{\ast}(-i\sigma^2)^{-1} = -\frac12\sigma^i$, so it reverses the spin along every axis; $J^2 = -\mathbb 1$, see Theorem [[§C9.5 Charge Conjugation on Oscillators and Spinors#^thm-c9-5-3|§C9.5.3]] Conjugation Reverses the Spin of a Two-Spinor. *Source: Lecture 12 (Oct 12), slide 7 ("$-i\sigma_2(\xi^s)^{\ast} = \xi^{-s}$ is general result"; "Proof (optional): rotation generators of two sides agree") · PS §3.6, p. 68*

^nd-thm-c9-5-3

- [ ] Q1 **[state]** State the four parts.
- [ ] Q2 Show $J$ is antilinear and compute $(J\xi)^\dagger(J\chi)$.
- [ ] Q3 **[class exercise]** Compute $(-i\sigma^2)(\frac12\sigma^i)^{\ast}(i\sigma^2)$ for $i = 1, 2, 3$: which $\sigma$'s are imaginary, and what does moving $\sigma^2$ past $\sigma^1$, $\sigma^3$ do?
- [ ] Q4 Conclude: if $(\hat{\mathbf n}\cdot\boldsymbol\sigma)\xi = \lambda\xi$, what is $(\hat{\mathbf n}\cdot\boldsymbol\sigma)J\xi$?
- [ ] Q5 Compute $J^2$.
- [ ] Q6 **[why]** Why is it a "general result", valid in any spin basis and not only for the helicity spinors?

> [!tip]- Hints: route in the notes
> - Technique: K5 (Pauli algebra), K11.
> - Steps 1–4 under Theorem [[§C9.5 Charge Conjugation on Oscillators and Spinors#^thm-c9-5-3|§C9.5.3]] Conjugation Reverses the Spin of a Two-Spinor; examples Example [[§C9.5 Charge Conjugation on Oscillators and Spinors#^ex-c9-5-1|§C9.5.1]] Conjugating the Helicity and the Standard Two-Spinors.

### Transposes and conjugates of the chiral γ's ★★

In the chiral basis $\gamma^0$, $\gamma^2$ are symmetric and $\gamma^1$, $\gamma^3$ antisymmetric; $\gamma^2$ is the only imaginary one, so $i\gamma^2$ is real and $(-i\gamma^2)^2 = \mathbb 1$; $(\gamma^\mu)^{\mathsf T}\gamma^0\gamma^2 = -\gamma^0\gamma^2\gamma^\mu$ and $\gamma^0\gamma^2\gamma^0\gamma^2 = \mathbb 1$, see Theorem [[§C9.5 Charge Conjugation on Oscillators and Spinors#^thm-c9-5-4|§C9.5.4]] Transposes and Conjugates of the Chiral Dirac Matrices. *Source: Lecture 12 (Oct 12), slides 8, 10–11 · PS §3.6, p. 70*

^nd-thm-c9-5-4

- [ ] Q1 **[state]** State the five parts.
- [ ] Q2 How does transposing a block off-diagonal matrix act on its blocks? Apply to each $\gamma^\mu$.
- [ ] Q3 Compute $(\gamma^2)^\dagger$ and $(-i\gamma^2)^2$.
- [ ] Q4 Show $\gamma^0\gamma^2$ anticommutes with $\gamma^0$, $\gamma^2$ and commutes with $\gamma^1$, $\gamma^3$; deduce $(\gamma^\mu)^{\mathsf T}\gamma^0\gamma^2 = -\gamma^0\gamma^2\gamma^\mu$.
- [ ] Q5 **[conv]** In the lecture $\gamma^2$ seemed antisymmetric. Is it? Where did the "missing" minus sign come from?

> [!tip]- Hints: route in the notes
> - Technique: K5.
> - Steps 1–5 under Theorem [[§C9.5 Charge Conjugation on Oscillators and Spinors#^thm-c9-5-4|§C9.5.4]] Transposes and Conjugates of the Chiral Dirac Matrices; [[§C9.6 Charge Conjugation on the Field and Bilinears#^cau-c9-6-1|§C9.6, Caution: Is γ² antisymmetric?]].

### The conjugate of u is a v, and of v a u ★★

With $\eta^s = \xi^{-s}$: $u^s(p)^{\ast} = -i\gamma^2v^s(p)$, $v^s(p)^{\ast} = -i\gamma^2u^s(p)$, equivalently $v^s(p) = -i\gamma^2u^s(p)^{\ast}$, see Theorem [[§C9.5 Charge Conjugation on Oscillators and Spinors#^thm-c9-5-5|§C9.5.5]] The Conjugate of u Is a v and Theorem [[§C9.5 Charge Conjugation on Oscillators and Spinors#^thm-c9-5-6|§C9.5.6]] The Conjugate of v Is a u. *Source: Lecture 12 (Oct 12), slide 8 ("$u^s(p)^{\ast} = -i\gamma^2v^{-s}(p)$") · PS eq. (3.144)*

^nd-thm-c9-5-5

- [ ] Q1 **[state]** State both relations and the condition on $\eta^s$.
- [ ] Q2 Conjugate the column $u^s(p)$: why is the conjugate of $\sqrt{p\cdot\sigma}$ the square root of $p\cdot\sigma^{\ast}$?
- [ ] Q3 Write $(\xi^s)^{\ast}$ through $\xi^{-s}$.
- [ ] Q4 Move $i\sigma^2$ to the left through $\sqrt{p\cdot\sigma^{\ast}}$: why does $\sigma^{\ast}$ become $\bar\sigma$ (slide 8: "$\ast$ flips $\sigma^2$ sign; commute $i\sigma^2$ past $p\cdot\sigma$ flips $\sigma^{1,3}$ sign")?
- [ ] Q5 Recognize $-i\gamma^2$ and a $v$: which off-diagonal matrix exchanges the halves and creates the relative minus sign?
- [ ] Q6 Deduce the $v$ relation from the $u$ relation using that $i\gamma^2$ is real and $(-i\gamma^2)^2 = \mathbb 1$.
- [ ] Q7 **[conv]** What does slide 8's "$v^{-s}(p)$" mean, and why is it not the label rule $X^{-s}$?

> [!tip]- Hints: route in the notes
> - Technique: K15, K5.
> - Steps 1–5 under Theorem [[§C9.5 Charge Conjugation on Oscillators and Spinors#^thm-c9-5-5|§C9.5.5]] The Conjugate of u Is a v, 1–3 under Theorem [[§C9.5 Charge Conjugation on Oscillators and Spinors#^thm-c9-5-6|§C9.5.6]] The Conjugate of v Is a u; [[§C9.5 Charge Conjugation on Oscillators and Spinors#^cau-c9-5-3|§C9.5, Caution: Which v Is the Conjugate of u?]].

### Charge conjugation on the Dirac field ★★

$U(\mathcal C)\hat\psi(x)U(\mathcal C)^{-1} = -i\gamma^2\hat\psi^{\dagger\mathsf T}(x)$, component $-i\sum_b(\gamma^2)_{ab}(\hat\psi_b(x))^\dagger$, at the same point, if and only if $\eta^s = \xi^{-s}$, see Theorem [[§C9.6 Charge Conjugation on the Field and Bilinears#^thm-c9-6-2|§C9.6.2]] Charge Conjugation on the Dirac Field. *Source: Lecture 12 (Oct 12), slide 9 · PS eq. (3.145)*

^nd-thm-c9-6-2

- [ ] Q1 **[state]** State the law, componentwise, and its condition.
- [ ] Q2 Act on the operators only: what replaces $\hat a^s_{\mathbf p}$ and $\hat b^{s\dagger}_{\mathbf p}$? Why does the result have $\hat b$ next to $e^{-ip\cdot x}$?
- [ ] Q3 Rewrite $u^s(p)$ and $v^s(p)$ through conjugates of $v$ and $u$, and pull out $-i\gamma^2$.
- [ ] Q4 Recognize the remaining integral as $\hat\psi^{\dagger\mathsf T}(x)$. Where did the plane waves "go"?
- [ ] Q5 **[why]** "Only if": what goes wrong without $\eta^s = \xi^{-s}$?
- [ ] Q6 **[why]** "Charge conjugation = roughly complex conjugation" (slide 9): in what precise sense?

> [!tip]- Hints: route in the notes
> - Technique: K15 (act on modes, rewrite spinors, read off the matrix).
> - Steps 1–6 under Theorem [[§C9.6 Charge Conjugation on the Field and Bilinears#^thm-c9-6-2|§C9.6.2]] Charge Conjugation on the Dirac Field; [[§C9.6 Charge Conjugation on the Field and Bilinears#^rem-c9-6-1|§C9.6, Remark: Where the plane waves went]], [[§C9.6 Charge Conjugation on the Field and Bilinears#^rem-c9-6-2|§C9.6, Remark: Charge conjugation is roughly complex conjugation]].

### Charge conjugation in any basis: the matrix B ★

If $v^s(p) = B\,u^s(p)^{\ast}$ for a unitary charge-conjugation matrix $B$, then $U(\mathcal C)\hat\psi(x)U(\mathcal C)^{-1} = B\,\hat\psi^{\dagger\mathsf T}(x)$, and conversely; $B\hat\psi^{\dagger\mathsf T}$ obeys the Dirac equation; in the chiral basis $B = -i\gamma^2$ and the condition is $\eta^s = \xi^{-s}$, see Theorem [[§C9.6 Charge Conjugation on the Field and Bilinears#^thm-c9-6-1|§C9.6.1]] Charge Conjugation on the Dirac Field in Any Basis. *Source: Lecture 12 (Oct 12), slide 9; written beyond the lecture at the user's question · the user's notes Ch. 12 §12.3*

^nd-thm-c9-6-1

- [ ] Q1 **[state]** State the condition, the law and the Dirac-equation statement.
- [ ] Q2 **[why]** Why is $v = Bu^{\ast}$ an admissible negative-frequency spinor (does it solve $(\slashed p + m)v = 0$)?
- [ ] Q3 Act on the operators, then express $u$ through $v^{\ast}$: where does $BB^{\ast} = \mathbb 1$ enter?
- [ ] Q4 Pull $B$ out and recognize $\hat\psi^{\dagger\mathsf T}$.
- [ ] Q5 **[why]** Why does $B\hat\psi^{\dagger\mathsf T}$ satisfy the Dirac equation (use $B(\gamma^\mu)^{\ast}B^{-1} = -\gamma^\mu$)?
- [ ] Q6 **[why]** Why is the physics basis-independent although the matrix $-i\gamma^2$ is not?

> [!tip]- Hints: route in the notes
> - Technique: K15, K16.
> - Steps 1–10 under Theorem [[§C9.6 Charge Conjugation on the Field and Bilinears#^thm-c9-6-1|§C9.6.1]] Charge Conjugation on the Dirac Field in Any Basis; Definition [[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^def-cb-18-18|§CB.18.18]] The Charge-Conjugation Matrix, Theorem [[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-18-19|§CB.18.19]] Existence and Uniqueness of the Charge-Conjugation Matrix, and Its Square under Conjugation, Example [[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^ex-cb-18-22|§CB.18.22]] The Charge-Conjugation Matrix in Three Bases, and the Transpose Form; [[§C9.5 Charge Conjugation on Oscillators and Spinors#^cau-c9-5-4|§C9.5, Caution: −iγ² is a statement about the chiral basis]].

### The scalar bilinear under charge conjugation ★★

$U(\mathcal C)\hat{\bar\psi}\hat\psi(x)U(\mathcal C)^{-1} = +\hat{\bar\psi}\hat\psi(x)$: the "row" and "column" forms, a fermion exchange, and $\gamma^0\gamma^2\gamma^0\gamma^2 = \mathbb 1$, see Theorem [[§C9.6 Charge Conjugation on the Field and Bilinears#^thm-c9-6-5|§C9.6.5]] The Scalar Bilinear Is Charge-Conjugation Invariant. *Source: Lecture 12 (Oct 12), slide 11 ("'−' from anticommutation of the fields") · PS eq. (3.147)*

^nd-thm-c9-6-5

- [ ] Q1 **[state]** State the result.
- [ ] Q2 Insert both laws in components: which "row" and which "column" appear?
- [ ] Q3 Exchange the two fermion fields to restore the order of a bilinear: what sign, and why is the c-number from the anticommutator dropped?
- [ ] Q4 Simplify the matrix with the transpose rules.
- [ ] Q5 **[why]** Where would the result be wrong if $\hat\psi$ were a commuting field?

> [!tip]- Hints: route in the notes
> - Technique: K7, K11.
> - Steps 1–4 under Theorem [[§C9.6 Charge Conjugation on the Field and Bilinears#^thm-c9-6-5|§C9.6.5]] The Scalar Bilinear Is Charge-Conjugation Invariant; laws Theorem [[§C9.6 Charge Conjugation on the Field and Bilinears#^thm-c9-6-4|§C9.6.4]] Charge Conjugation on ψ† and ψ̄.

### The vector current under charge conjugation ★★

$U(\mathcal C)\mathsf V^\mu(x)U(\mathcal C)^{-1} = -\mathsf V^\mu(x)$ for all $\mu$: the number current flips, see Theorem [[§C9.6 Charge Conjugation on the Field and Bilinears#^thm-c9-6-6|§C9.6.6]] The Vector Current Changes Sign under Charge Conjugation. *Source: Lecture 12 (Oct 12), slide 11 · Problem Set 7, Problem 2(b) · PS eq. (3.149)*

^nd-thm-c9-6-6

→ drilled as [[PHY 513 PS Drill#^ps7-2-b|PS7.2(b)]]

### The axial vector under charge conjugation ★

$U(\mathcal C)\mathsf A^\mu(x)U(\mathcal C)^{-1} = +\mathsf A^\mu(x)$, see Theorem [[§C9.6 Charge Conjugation on the Field and Bilinears#^thm-c9-6-9|§C9.6.9]] The Axial Vector Is Charge-Conjugation Invariant. *Source: Problem Set 7, Problem 2(b) · PS eq. (3.150)*

^nd-thm-c9-6-9

→ drilled as [[PHY 513 PS Drill#^ps7-2-b|PS7.2(b)]]

### Charge conjugation on a general bilinear ★

In the chiral basis $\hat{\bar\psi}\Gamma\hat\psi \to \hat{\bar\psi}\gamma^0\gamma^2\Gamma^{\mathsf T}\gamma^0\gamma^2\hat\psi$ at the same point; in any Hermitian basis $\hat{\bar\psi}\tilde B\Gamma^{\mathsf T}\tilde B^{-1}\hat\psi$ with $\tilde B = B(\gamma^0)^{\mathsf T}$ antisymmetric, see Theorem [[§C9.6 Charge Conjugation on the Field and Bilinears#^thm-c9-6-7|§C9.6.7]] Charge Conjugation on a General Bilinear. *Source: Lecture 12 (Oct 12), slide 11 (the computation for $\gamma^\mu$) · PS §3.6, pp. 70–71 · Yu (9.121)*

^nd-thm-c9-6-7

- [ ] Q1 **[state]** State the chiral rule and the basis-free rule.
- [ ] Q2 Insert the laws of $\hat\psi$ and $\hat{\bar\psi}$; exchange the fields; transpose the c-number matrix product. Where does each sign go?
- [ ] Q3 **[conv]** Show that in the chiral basis $\tilde B = i\gamma^0\gamma^2$ and the general rule reduces to the chiral one. How is it Yu's $\Gamma^{\rm C} = \mathcal C^{-1}\Gamma^{\mathsf T}\mathcal C$?
- [ ] Q4 **[why]** Compare with time reversal: why $\Gamma^{\mathsf T}$ and a fermion exchange here, but $\Gamma^{\ast}$ and none there?

> [!tip]- Hints: route in the notes
> - Technique: K7.
> - Steps 1–7 under Theorem [[§C9.6 Charge Conjugation on the Field and Bilinears#^thm-c9-6-7|§C9.6.7]] Charge Conjugation on a General Bilinear; $T$ analogue Theorem [[§C9.8 Time Reversal#^thm-c9-8-10|§C9.8.10]] Time Reversal on a General Bilinear.

### Pseudoscalar and tensor under charge conjugation ★

$\mathsf P \to +\mathsf P(x)$ and $\mathsf T^{\mu\nu} \to -\mathsf T^{\mu\nu}(x)$ under $U(\mathcal C)$, see Theorem [[§C9.6 Charge Conjugation on the Field and Bilinears#^thm-c9-6-8|§C9.6.8]] The Pseudoscalar Bilinear Is Charge-Conjugation Invariant and Theorem [[§C9.6 Charge Conjugation on the Field and Bilinears#^thm-c9-6-10|§C9.6.10]] The Tensor Bilinear Changes Sign under Charge Conjugation. *Source: the user's notes Ch. 12 ("the rest", filled in) · PS table p. 71 · Yu (9.122)–(9.129)*

^nd-thm-c9-6-10

- [ ] Q1 **[state]** State both results.
- [ ] Q2 Pseudoscalar: is $\gamma^5$ symmetric in the chiral basis? Does it commute with $\gamma^0\gamma^2$?
- [ ] Q3 Tensor: insert $(\gamma^0\gamma^2)^2 = \mathbb 1$ between the two $\gamma$'s of each product in $(\sigma^{\mu\nu})^{\mathsf T}$; why does the commutator reverse?
- [ ] Q4 **[why]** Check the pattern: which bilinears are $C$-even, which $C$-odd?

> [!tip]- Hints: route in the notes
> - Technique: K7, K5.
> - Steps 1–4 under Theorem [[§C9.6 Charge Conjugation on the Field and Bilinears#^thm-c9-6-8|§C9.6.8]] The Pseudoscalar Bilinear Is Charge-Conjugation Invariant, 1–3 under Theorem [[§C9.6 Charge Conjugation on the Field and Bilinears#^thm-c9-6-10|§C9.6.10]] The Tensor Bilinear Changes Sign under Charge Conjugation; table Theorem [[§C9.9 CPT and the CPT Theorem#^thm-c9-9-5|§C9.9.5]] The Bilinears under C, P, T and CPT.

### The free Dirac Lagrangian is C invariant ★

$U(\mathcal C)\hat{\mathcal L}(x)U(\mathcal C)^{-1} = \hat{\mathcal L}(x) - i\partial_\mu\mathsf V^\mu(x)$, so the action is invariant, see Theorem [[§C9.6 Charge Conjugation on the Field and Bilinears#^thm-c9-6-11|§C9.6.11]] The Free Dirac Lagrangian Is Charge-Conjugation Invariant. *Source: PS §3.6, p. 71*

^nd-thm-c9-6-11

- [ ] Q1 **[state]** State the result and why only the action is invariant.
- [ ] Q2 The mass term: which theorem?
- [ ] Q3 The kinetic term: after inserting the laws and exchanging, where does the derivative end up, and how does the product rule produce $-i\partial_\mu\mathsf V^\mu$?
- [ ] Q4 **[why]** Why does the total derivative drop from the action?

> [!tip]- Hints: route in the notes
> - Technique: K7, K2.
> - Steps 1–5 under Theorem [[§C9.6 Charge Conjugation on the Field and Bilinears#^thm-c9-6-11|§C9.6.11]] The Free Dirac Lagrangian Is Charge-Conjugation Invariant.

### The spin operator in oscillator form ★★

$\hat S^3 = \int\frac{d^3p}{(2\pi)^3}\frac{1}{2E_{\mathbf p}}\sum_{r,s}(\hat a^{r\dagger}\hat a^s\,u^{r\dagger}\frac12\Sigma^3u^s + \hat b^r\hat b^{s\dagger}\,v^{r\dagger}\frac12\Sigma^3v^s) + \hat S^3_{\rm pair}$; for momenta along $z$ the pair terms vanish and the coefficients reduce to $\xi^{r\dagger}\frac{\sigma^3}2\xi^s$, $\eta^{r\dagger}\frac{\sigma^3}2\eta^s$, see Theorem [[§C9.7 Physical Spin versus Wave-Function Spin#^thm-c9-7-1|§C9.7.1]] The Spin Operator in Oscillator Form. *Source: Lecture 12 (Oct 12), slide 16 ("Use orthogonality (not quite 'standard' due to insertion of $\Sigma$)"); transcript ("we check that") · PS §3.5, p. 61*

^nd-thm-c9-7-1

- [ ] Q1 **[state]** State the oscillator form for momenta along $z$.
- [ ] Q2 Insert both expansions: which $x$-integrals identify $\mathbf q = \mathbf p$ and which $\mathbf q = -\mathbf p$?
- [ ] Q3 For $\mathbf p$ along $z$, compute $u^{r\dagger}\frac12\Sigma^3u^s$: why does $\Sigma^3$ commute with $p\cdot\sigma$ there, and what factor $2E_{\mathbf p}$ appears?
- [ ] Q4 Why do the pair coefficients $u^\dagger(\tilde p)\Sigma^3v(p)$ vanish for $\mathbf p$ along $z$?
- [ ] Q5 **[why]** Why is the orthogonality "not quite standard" here, and what goes wrong for other momenta?

> [!tip]- Hints: route in the notes
> - Technique: K10, K9.
> - Steps 1–5 under Theorem [[§C9.7 Physical Spin versus Wave-Function Spin#^thm-c9-7-1|§C9.7.1]] The Spin Operator in Oscillator Form; other momenta [[§C9.7 Physical Spin versus Wave-Function Spin#^rem-c9-7-5|§C9.7, Remark: Other momenta, and why Ŝ alone is not enough]].

### The reordering sign in the spin operator ★★

$\sum_{r,s}\hat b^r\hat b^{s\dagger}\eta^{r\dagger}\frac{\sigma^3}2\eta^s = -\sum_{r,s}\hat b^{s\dagger}\hat b^r\eta^{r\dagger}\frac{\sigma^3}2\eta^s$ with no constant ($\operatorname{tr}\sigma^3 = 0$); with $\eta^s = \xi^{-s}$, $s = 1$ contributes $+\frac12$ and $s = 2$ contributes $-\frac12$ for both species, see Theorem [[§C9.7 Physical Spin versus Wave-Function Spin#^thm-c9-7-2|§C9.7.2]] The Reordering Sign in the Spin Operator. *Source: Lecture 12 (Oct 12), slide 16 ("Operator order in the second term ⇒ interchange gives '−'") · PS §3.5, p. 61*

^nd-thm-c9-7-2

- [ ] Q1 **[state]** State the reordered antiparticle term and the final integrand of $\hat S^3$.
- [ ] Q2 Reorder with the anticommutator: what is the constant, and why does it vanish?
- [ ] Q3 Compute $\eta^{r\dagger}\frac{\sigma^3}2\eta^s$ for $\eta^1 = (0, 1)^{\mathsf T}$, $\eta^2 = (-1, 0)^{\mathsf T}$.
- [ ] Q4 Collect: which number operators come with $+\frac12$ and which with $-\frac12$?
- [ ] Q5 **[why]** "Two minus signs, again": compare with the energy of an antiparticle.
- [ ] Q6 **[conv]** The handwritten notes have a slip in the antiparticle coefficient. Which?

> [!tip]- Hints: route in the notes
> - Technique: K11.
> - Steps 1–4 under Theorem [[§C9.7 Physical Spin versus Wave-Function Spin#^thm-c9-7-2|§C9.7.2]] The Reordering Sign in the Spin Operator; [[§C9.7 Physical Spin versus Wave-Function Spin#^rem-c9-7-4|§C9.7, Remark: Two minus signs, again]]; [[§C9.7 Physical Spin versus Wave-Function Spin#^cau-c9-7-1|§C9.7, Caution: A slip in the handwritten notes]].

### Particle and antiparticle with label s have the same physical spin ★★

With $\eta^s = \xi^{-s}$, $\hat J_z\hat a^{s\dagger}_{\mathbf 0}|0\rangle = \pm\frac12\hat a^{s\dagger}_{\mathbf 0}|0\rangle$ and $\hat J_z\hat b^{s\dagger}_{\mathbf 0}|0\rangle = \pm\frac12\hat b^{s\dagger}_{\mathbf 0}|0\rangle$ ($+$ for $s = 1$), although the antiparticle's wave-function spin is opposite, see Theorem [[§C9.7 Physical Spin versus Wave-Function Spin#^thm-c9-7-3|§C9.7.3]] Particle and Antiparticle Created with Label s Have the Same Physical Spin and Principle [[§C9.7 Physical Spin versus Wave-Function Spin#^pr-c9-7-4|§C9.7.4]] Physical Spin Is the Eigenvalue of an Operator. *Source: Lecture 12 (Oct 12), slides 14–16 · PS eq. (3.112) with (3.136)*

^nd-thm-c9-7-3

- [ ] Q1 **[state]** State the result and the principle behind it.
- [ ] Q2 Use the rest-frame formulas of the earlier $J_z$ computation: which matrix elements of $\frac{\sigma^3}2$ enter for particles and for antiparticles?
- [ ] Q3 Insert $\eta^s = \xi^{-s}$: why does the antiparticle sign come out as for the particle?
- [ ] Q4 **[why]** Why is $C$ consistent with spin: what does $U(\mathcal C)$ do to $\hat a^s$, and what to the wave functions?
- [ ] Q5 **[why]** In hole theory a missing spin-down electron looks like spin up. How is that "wave-function spin is opposite" in another language?

> [!tip]- Hints: route in the notes
> - Technique: K11.
> - Steps 1–3 under Theorem [[§C9.7 Physical Spin versus Wave-Function Spin#^thm-c9-7-3|§C9.7.3]] Particle and Antiparticle Created with Label s Have the Same Physical Spin; Theorem [[§C5b.4 Fermions, Fock Space and the Pauli Principle#^thm-c5b-4-3|§C5b.4.3]] Dirac Quanta Have Spin One-Half; [[§C9.7 Physical Spin versus Wave-Function Spin#^rem-c9-7-2|§C9.7, Remark: Why charge conjugation is consistent]], [[§C9.7 Physical Spin versus Wave-Function Spin#^rem-c9-7-3|§C9.7, Remark: No holes]].

### Time reversal must be antilinear ★★

If $U(\mathcal T)$ commutes with $\hat H$ and $U(\mathcal T)\hat\psi(t, \mathbf x)U(\mathcal T)^{-1} = M\hat\psi(-t, \mathbf x)$, then $U(\mathcal T)$ is not linear; it conjugates numbers, $U(\mathcal T)cU(\mathcal T)^{-1} = c^{\ast}$, so $U(\mathcal T)e^{-i\hat Ht}U(\mathcal T)^{-1} = e^{i\hat Ht}$, see Theorem [[§C9.8 Time Reversal#^thm-c9-8-1|§C9.8.1]] Time Reversal Must Be Antilinear. *Source: Lecture 12 (Oct 12), slide 21 · PS §3.6, p. 67, eq. (3.133)*

^nd-thm-c9-8-1

- [ ] Q1 **[state]** State the result and the definition of an antilinear operator.
- [ ] Q2 Write $\hat\psi(t, \mathbf x) = e^{i\hat Ht}\hat\psi(0, \mathbf x)e^{-i\hat Ht}$ and conjugate with a linear $U$ commuting with $\hat H$: which time do you get?
- [ ] Q3 **[why]** Why is the way out $U\hat HU^{-1} = -\hat H$ excluded?
- [ ] Q4 With $UcU^{-1} = c^{\ast}$, conjugate the power series of $e^{i\hat Ht}$ term by term.
- [ ] Q5 **[why]** Slide 21's examples: what are $U(\mathcal T)\gamma^\mu U(\mathcal T)^{-1}$ and $U(\mathcal T)u^s(p)U(\mathcal T)^{-1}$? Why does this "go against everything said so far"?

> [!tip]- Hints: route in the notes
> - Technique: K11.
> - Steps 1–4 under Theorem [[§C9.8 Time Reversal#^thm-c9-8-1|§C9.8.1]] Time Reversal Must Be Antilinear; Definition [[§CB.19 Projective Representations, Wigner's Theorem and Antiunitary Symmetries#^def-cb-19-3|§CB.19.3]] Antilinear Operator; [[§C9.8 Time Reversal#^cau-c9-8-1|§C9.8, Caution: This goes against everything said so far]].

### Time reversal is antiunitary; it conjugates every number ★

If time reversal is a symmetry, $U(\mathcal T)$ is antiunitary, $\langle U\Psi_1, U\Psi_2\rangle = \langle\Psi_1, \Psi_2\rangle^{\ast}$; on operator expressions it conjugates every c-number coefficient, keeps operator order and preserves adjoints, see Theorem [[§C9.8 Time Reversal#^thm-c9-8-2|§C9.8.2]] Time Reversal Is Antiunitary and Theorem [[§C9.8 Time Reversal#^thm-c9-8-3|§C9.8.3]] Time Reversal Conjugates Every Number in the Field. *Source: PS §3.6, p. 67 · Lecture 12 (Oct 12), slide 21 ("Examples")*

^nd-thm-c9-8-3

- [ ] Q1 **[state]** Define antiunitary and state the three rules for conjugating expressions.
- [ ] Q2 **[why]** Why does Wigner's theorem leave only "unitary or antiunitary", and why is unitary excluded?
- [ ] Q3 For a constant matrix $M$ on the spinor index, what is $U(\mathcal T)(M\hat\Psi)U(\mathcal T)^{-1}$?
- [ ] Q4 **[why]** Why is $U(\mathcal T)$ fixed by its action on the oscillators and the vacuum?

> [!tip]- Hints: route in the notes
> - Technique: K15.
> - Steps 1–3 under Theorem [[§C9.8 Time Reversal#^thm-c9-8-2|§C9.8.2]] Time Reversal Is Antiunitary; Theorem [[§CB.19 Projective Representations, Wigner's Theorem and Antiunitary Symmetries#^thm-cb-19-16|§CB.19.16]] Conjugation by an Antiunitary Operator; Definition [[§CB.19 Projective Representations, Wigner's Theorem and Antiunitary Symmetries#^def-cb-19-4|§CB.19.4]] Antiunitary Operator.

### The matrix γ¹γ³ ★★ [class exercise, Lecture 12]

In the chiral basis $\gamma^1\gamma^3 = \operatorname{diag}(i\sigma^2, i\sigma^2)$, real; $(\gamma^1\gamma^3)^2 = -\mathbb 1$, $(\gamma^1\gamma^3)^\dagger = \gamma^3\gamma^1 = (\gamma^1\gamma^3)^{-1}$; it commutes with $\gamma^0$, $\gamma^2$ and anticommutes with $\gamma^1$, $\gamma^3$; $(\gamma^\mu)^{\ast}\gamma^1\gamma^3 = \gamma^1\gamma^3\gamma_\mu$, see Theorem [[§C9.8 Time Reversal#^thm-c9-8-4|§C9.8.4]] The Matrix γ¹γ³. *Source: Lecture 12 (Oct 12), slides 20, 23; transcript ("We have to go and check. What about i's and all that? Yup, it turns out that just works")*

^nd-thm-c9-8-4

- [ ] Q1 **[state]** State the four parts.
- [ ] Q2 **[class exercise]** Multiply the off-diagonal blocks of $\gamma^1$ and $\gamma^3$ and check the $i$'s: which block-diagonal matrix results, and is it real?
- [ ] Q3 Compute the square, the adjoint and the inverse.
- [ ] Q4 Count signs when moving each $\gamma^\mu$ through $\gamma^1\gamma^3$.
- [ ] Q5 **[why]** Use that only $\gamma^2$ is imaginary to prove $(\gamma^\mu)^{\ast}\gamma^1\gamma^3 = \gamma^1\gamma^3\gamma_\mu$. Why the lower index?

> [!tip]- Hints: route in the notes
> - Technique: K5.
> - Steps 1–4 under Theorem [[§C9.8 Time Reversal#^thm-c9-8-4|§C9.8.4]] The Matrix γ¹γ³.

### Time reversal on the spinors u and v ★★ [class exercise, Lecture 12]

$u^s(p)^{\ast} = \gamma^1\gamma^3u^{-s}(\tilde p)$ and $v^s(p)^{\ast} = \gamma^1\gamma^3v^{-s}(\tilde p)$ (with $\eta^s = \xi^{-s}$): flipped momentum and flipped spin, see Theorem [[§C9.8 Time Reversal#^thm-c9-8-5|§C9.8.5]] Time Reversal on the Positive-Frequency Spinors and Theorem [[§C9.8 Time Reversal#^thm-c9-8-6|§C9.8.6]] Time Reversal on the Negative-Frequency Spinors. *Source: Lecture 12 (Oct 12), slide 20 ("The first step copied from analysis of charge conjugation"; "Similarly $v^s(p)^{\ast} = \gamma^1\gamma^3v^{-s}(\tilde p)$") · PS §3.6, p. 68*

^nd-thm-c9-8-5

- [ ] Q1 **[state]** State both relations.
- [ ] Q2 Copy the first steps of the charge-conjugation computation for $u^s(p)^{\ast}$: what column do you reach?
- [ ] Q3 **[why]** For charge conjugation the halves were exchanged back; why are they now left in place ($p\cdot\bar\sigma = \tilde p\cdot\sigma$)?
- [ ] Q4 Recognize $u$ at $\tilde p$ built on $\xi^{-s}$ and the matrix $\operatorname{diag}(i\sigma^2, i\sigma^2)$.
- [ ] Q5 **[class exercise]** Do the "similarly" for $v$: what is $(\eta^s)^{\ast}$ in terms of $\eta^{-s}$, and where does the relative minus sign of $v$ go?

> [!tip]- Hints: route in the notes
> - Technique: K15, K5.
> - Steps 1–3 under Theorem [[§C9.8 Time Reversal#^thm-c9-8-5|§C9.8.5]] Time Reversal on the Positive-Frequency Spinors, 1–4 under Theorem [[§C9.8 Time Reversal#^thm-c9-8-6|§C9.8.6]] Time Reversal on the Negative-Frequency Spinors; $J$ of Theorem [[§C9.5 Charge Conjugation on Oscillators and Spinors#^thm-c9-5-3|§C9.5.3]] Conjugation Reverses the Spin of a Two-Spinor.

### Time reversal on the Dirac field ★★

$U(\mathcal T)\hat\psi(t, \mathbf x)U(\mathcal T)^{-1} = \gamma^1\gamma^3\hat\psi(-t, \mathbf x)$, i.e. $\gamma^1\gamma^3\hat\psi(x_T)$, see Theorem [[§C9.8 Time Reversal#^thm-c9-8-7|§C9.8.7]] Time Reversal on the Dirac Field. *Source: Lecture 12 (Oct 12), slide 22 · PS eq. (3.139) (with $-\gamma^1\gamma^3$)*

^nd-thm-c9-8-7

- [ ] Q1 **[state]** State the law.
- [ ] Q2 Act antilinearly on the expansion: what happens to the operators, the spinors and the exponentials?
- [ ] Q3 Rewrite the conjugated spinors with the $T$ identities and pull out $\gamma^1\gamma^3$.
- [ ] Q4 Relabel $s \to -s$: why is $\sum_s\hat a^{-s}u^{-s} = \sum_s\hat a^su^s$?
- [ ] Q5 Change $\mathbf p \to -\mathbf p$ and rewrite the exponent: why is $i\tilde p\cdot x = -ip\cdot x_T$?
- [ ] Q6 **[conv]** Slide 22's second line has a wrong antiparticle term. What should it be?
- [ ] Q7 **[why]** Under smearing, why does antilinearity conjugate the test function?

> [!tip]- Hints: route in the notes
> - Technique: K15, K9.
> - Steps 1–6 under Theorem [[§C9.8 Time Reversal#^thm-c9-8-7|§C9.8.7]] Time Reversal on the Dirac Field; [[§C9.8 Time Reversal#^cau-c9-8-2|§C9.8, Caution: Slide 22's antiparticle term]].

### Time reversal on ψ̄ and on a general bilinear ★

$U(\mathcal T)\hat{\bar\psi}(t, \mathbf x)U(\mathcal T)^{-1} = \hat{\bar\psi}(-t, \mathbf x)\gamma^3\gamma^1$ and $U(\mathcal T)\hat{\bar\psi}\Gamma\hat\psi(x)U(\mathcal T)^{-1} = \hat{\bar\psi}(x_T)\gamma^3\gamma^1\Gamma^{\ast}\gamma^1\gamma^3\hat\psi(x_T)$, see Theorem [[§C9.8 Time Reversal#^thm-c9-8-8|§C9.8.8]] Time Reversal on the Dirac Conjugate Field and Theorem [[§C9.8 Time Reversal#^thm-c9-8-10|§C9.8.10]] Time Reversal on a General Bilinear. *Source: Lecture 12 (Oct 12), slide 22 ("adjoint and then right multiplication by $\gamma^0$") · PS eq. (3.140), p. 69*

^nd-thm-c9-8-10

- [ ] Q1 **[state]** State both laws.
- [ ] Q2 Take the adjoint of the field law: why is $(\gamma^1\gamma^3)^\dagger = \gamma^3\gamma^1$, and why does it pass $\gamma^0$?
- [ ] Q3 For the bilinear: why does $\Gamma$ become $\Gamma^{\ast}$?
- [ ] Q4 **[why]** Why is there no fermion exchange sign under $T$, unlike under $C$?

> [!tip]- Hints: route in the notes
> - Technique: K7, K15.
> - Steps 1–2 under Theorem [[§C9.8 Time Reversal#^thm-c9-8-8|§C9.8.8]] Time Reversal on the Dirac Conjugate Field, 1–3 under Theorem [[§C9.8 Time Reversal#^thm-c9-8-10|§C9.8.10]] Time Reversal on a General Bilinear.

### Pseudoscalar and vector under time reversal ★★

$\mathsf P \to -\mathsf P(x_T)$ and $\mathsf V^\mu \to \mathcal P^\mu{}_\nu\mathsf V^\nu(x_T)$ under $U(\mathcal T)$, see Theorem [[§C9.8 Time Reversal#^thm-c9-8-12|§C9.8.12]] The Pseudoscalar Bilinear Changes Sign under Time Reversal and Theorem [[§C9.8 Time Reversal#^thm-c9-8-9|§C9.8.9]] The Vector Current under Time Reversal. *Source: Lecture 12 (Oct 12), slide 23 ($\mathsf V^\mu$) · Problem Set 7, Problem 2(c) · PS eq. (3.142)*

^nd-thm-c9-8-9

→ drilled as [[PHY 513 PS Drill#^ps7-2-c|PS7.2(c)]]

### Scalar, axial vector and tensor under time reversal ★

$\mathsf S \to +\mathsf S(x_T)$, $\mathsf A^\mu \to +\mathcal P^\mu{}_\nu\mathsf A^\nu(x_T)$, $\mathsf T^{\mu\nu} \to -\mathcal P^\mu{}_\rho\mathcal P^\nu{}_\sigma\mathsf T^{\rho\sigma}(x_T)$, see Theorem [[§C9.8 Time Reversal#^thm-c9-8-11|§C9.8.11]] The Scalar Bilinear Is Time-Reversal Invariant, Theorem [[§C9.8 Time Reversal#^thm-c9-8-13|§C9.8.13]] The Axial Vector under Time Reversal, Theorem [[§C9.8 Time Reversal#^thm-c9-8-14|§C9.8.14]] The Tensor Bilinear under Time Reversal. *Source: the user's notes Ch. 12 ("the rest", filled in) · PS table p. 71 · Yu (9.221)–(9.225)*

^nd-thm-c9-8-13

- [ ] Q1 **[state]** State the three results with their points.
- [ ] Q2 Axial vector: insert $\gamma^1\gamma^3\gamma^3\gamma^1 = \mathbb 1$ between $(\gamma^\mu)^{\ast}$ and $\gamma^5$; what does $\gamma^5$ do with $\gamma^1\gamma^3$, and is $\gamma^5$ real?
- [ ] Q3 Tensor: what does the $i$ in $\sigma^{\mu\nu}$ do under conjugation, and what do the two $\gamma$'s do?
- [ ] Q4 **[why]** Compare $\mathsf T^{0i}$, $\mathsf T^{ij}$ under $T$ and under $P$.

> [!tip]- Hints: route in the notes
> - Technique: K7, K5.
> - Theorem [[§C9.8 Time Reversal#^thm-c9-8-11|§C9.8.11]] The Scalar Bilinear Is Time-Reversal Invariant; steps 1–3 under Theorem [[§C9.8 Time Reversal#^thm-c9-8-13|§C9.8.13]] The Axial Vector under Time Reversal and Theorem [[§C9.8 Time Reversal#^thm-c9-8-14|§C9.8.14]] The Tensor Bilinear under Time Reversal.

### The free Dirac Lagrangian is T invariant ★

$U(\mathcal T)\hat{\mathcal L}(t, \mathbf x)U(\mathcal T)^{-1} = \hat{\mathcal L}(-t, \mathbf x)$ and the action is invariant, see Theorem [[§C9.8 Time Reversal#^thm-c9-8-15|§C9.8.15]] The Free Dirac Lagrangian Is Time-Reversal Invariant. *Source: PS §3.6, p. 71*

^nd-thm-c9-8-15

- [ ] Q1 **[state]** State the result.
- [ ] Q2 The derivative of the transformed field: which components of $\partial_\mu$ change sign under $t \to -t$?
- [ ] Q3 The kinetic term: what happens to the explicit $i$, and how does it combine with the signs from $\gamma^\mu$ and $\partial_\mu$?
- [ ] Q4 **[why]** Why is the action invariant under $t' = -t$?

> [!tip]- Hints: route in the notes
> - Technique: K7, K2.
> - Steps 1–4 under Theorem [[§C9.8 Time Reversal#^thm-c9-8-15|§C9.8.15]] The Free Dirac Lagrangian Is Time-Reversal Invariant.

### Time reversal twice is −1 on fermions ★

$U(\mathcal T)^2\hat a^s_{\mathbf p}U(\mathcal T)^{-2} = -\hat a^s_{\mathbf p}$ (likewise $\hat b$), so $U(\mathcal T)^2 = (-1)^{\hat N_a + \hat N_b}$; on the complex scalar $U(\mathcal T)^2 = \mathbb 1$, see Theorem [[§C9.8 Time Reversal#^thm-c9-8-16|§C9.8.16]] Time Reversal Twice Is −1 on Fermions and [[§C9.10 C, T and CPT for the Complex Scalar Field#^rem-c9-10-1|§C9.10, Remark: Time reversal twice is +1 on the scalar field]]. *Source: PS §3.6, p. 68 ("two successive spin flips return a spin to $(-1)$ times the original state")*

^nd-thm-c9-8-16

- [ ] Q1 **[state]** State the result.
- [ ] Q2 Apply the definition twice for $s = 1$ and for $s = 2$ using the label rule.
- [ ] Q3 Why is $U(\mathcal T)^2$ linear and unitary?
- [ ] Q4 **[why]** Why does the scalar field give $+1$?
- [ ] Q5 **[why]** What degeneracy follows for an odd number of fermions?

> [!tip]- Hints: route in the notes
> - Technique: K15.
> - Steps 1–3 under Theorem [[§C9.8 Time Reversal#^thm-c9-8-16|§C9.8.16]] Time Reversal Twice Is −1 on Fermions; Kramers degeneracy (★, beyond the course): [[§C9.8 Time Reversal#^rem-c9-8-4|§C9.8, ★ Remark: Kramers degeneracy]].

### The three matrices multiply to γ⁵ ★

$\gamma^0(-i\gamma^2)(\gamma^1\gamma^3) = \gamma^5$ and $\gamma^1\gamma^3\gamma^0(-i\gamma^2) = \gamma^5$; in any order the product is $\pm\gamma^5$, see Theorem [[§C9.9 CPT and the CPT Theorem#^thm-c9-9-1|§C9.9.1]] The Three Matrices Multiply to γ⁵. *Source: Lecture 12 (Oct 12), transcript ("if you multiply them together, you get gamma five")*

^nd-thm-c9-9-1

- [ ] Q1 **[state]** State the two products.
- [ ] Q2 Reorder $\gamma^0\gamma^2\gamma^1\gamma^3$ to $\gamma^0\gamma^1\gamma^2\gamma^3$: how many exchanges, which sign?
- [ ] Q3 Do the same for $\gamma^1\gamma^3\gamma^0\gamma^2$.
- [ ] Q4 **[why]** Why does any order give $\pm\gamma^5$? Why does this suggest that $CPT$ is more symmetric than each factor?

> [!tip]- Hints: route in the notes
> - Technique: K5.
> - Steps 1–3 under Theorem [[§C9.9 CPT and the CPT Theorem#^thm-c9-9-1|§C9.9.1]] The Three Matrices Multiply to γ⁵; [[§C9.9 CPT and the CPT Theorem#^rem-c9-9-1|§C9.9, Remark: Each γ once]].

### Θ is antiunitary ★

$\Theta$ is antiunitary with $\Theta^{-1} = U(\mathcal T)^{-1}U(\mathcal P)^{-1}U(\mathcal C)^{-1}$ and $\Theta c\Theta^{-1} = c^{\ast}$, see Theorem [[§C9.9 CPT and the CPT Theorem#^thm-c9-9-2|§C9.9.2]] Θ Is Antiunitary. *Source: the user's notes Ch. 12 · Yu (9.320)–(9.322)*

^nd-thm-c9-9-2

- [ ] Q1 **[state]** State the result.
- [ ] Q2 **[why]** Why is a product of one antiunitary and two unitary operators antiunitary?
- [ ] Q3 Conjugate a number through the three factors in turn.

> [!tip]- Hints: route in the notes
> - Technique: K15.
> - Steps 1–3 under Theorem [[§C9.9 CPT and the CPT Theorem#^thm-c9-9-2|§C9.9.2]] Θ Is Antiunitary.

### CPT on the Dirac field ★★

$\Theta\hat\psi(x)\Theta^{-1} = \eta_a\gamma^5\hat\psi^{\dagger\mathsf T}(-x)$: multiplication by $\gamma^5$, a star and $x \to -x$, see Theorem [[§C9.9 CPT and the CPT Theorem#^thm-c9-9-3|§C9.9.3]] CPT on the Dirac Field. *Source: Lecture 12 (Oct 12), transcript · Problem Set 7, Problem 3*

^nd-thm-c9-9-3

→ drilled as [[PHY 513 PS Drill#^ps7-3|PS7.3]]

### CPT in another order ★ [class exercise, Lecture 12]

$\Theta' \equiv U(\mathcal T)U(\mathcal P)U(\mathcal C)$ (first $\mathcal C$) gives $\Theta'\hat\psi(x)\Theta'^{-1} = -\eta_a\gamma^5\hat\psi^{\dagger\mathsf T}(-x)$, the same up to a sign, see Theorem [[§C9.9 CPT and the CPT Theorem#^thm-c9-9-4|§C9.9.4]] CPT in Another Order. *Source: Lecture 12 (Oct 12), slide 24 ("first T, then P, then C — although in fact any order will do"; stated, not shown) · the user's notes Ch. 12*

^nd-thm-c9-9-4

- [ ] Q1 **[state]** State the result and what "any order will do" means.
- [ ] Q2 $C$ first: write the result componentwise as adjoints of $\hat\psi_b$.
- [ ] Q3 Then $P$ on the adjoint field: what phase and matrix appear?
- [ ] Q4 **[why]** Then $T$: why does it conjugate the coefficients $-i(\gamma^2)$ and $\eta_a^{\ast}\gamma^0$ but leave the operator order?
- [ ] Q5 Reduce the matrix $\gamma^2\gamma^0\gamma^1\gamma^3$ (with its numerical factor) to $\pm\gamma^5$.

> [!tip]- Hints: route in the notes
> - Technique: K15, K5.
> - Steps 1–5 under Theorem [[§C9.9 CPT and the CPT Theorem#^thm-c9-9-4|§C9.9.4]] CPT in Another Order; [[§C9.9 CPT and the CPT Theorem#^cau-c9-9-1|§C9.9, Caution: The transposed adjoint in CPT]].

### The bilinears under C, P, T and CPT ★

One table: $C$ at $x$, $P$ at $\tilde x$, $T$ at $x_T$, $CPT$ at $-x$; under $\Theta$ a bilinear with $n$ Lorentz indices is multiplied by $(-1)^n$, a derivative counting as an index, see Theorem [[§C9.9 CPT and the CPT Theorem#^thm-c9-9-5|§C9.9.5]] The Bilinears under C, P, T and CPT. *Source: PS §3.6, table on p. 71 · Problem Set 7, Problem 2 (parts) · the user's notes Ch. 12*

^nd-thm-c9-9-5

- [ ] Q1 **[state]** Reproduce the table for $\mathsf S$, $\mathsf P$, $\mathsf V^\mu$, $\mathsf A^\mu$, $\mathsf T^{\mu\nu}$ and $\partial_\mu$, with the points.
- [ ] Q2 Compose the columns in the order first $T$, then $P$, then $C$: why do the factors $\mathcal P^\mu{}_\nu$ cancel in pairs?
- [ ] Q3 Multiply the signs row by row and check the $CPT$ column.
- [ ] Q4 **[conv]** PS write $(-1)^\mu$; Yu $[-]^\mu$; the notes $\mathcal P^\mu{}_\nu$. Translate one row.
- [ ] Q5 **[why]** State the $(-1)^n$ rule and explain it from $\Theta\hat\psi\Theta^{-1} = \eta_a\gamma^5\hat\psi^{\dagger\mathsf T}(-x)$.

> [!tip]- Hints: route in the notes
> - Technique: K7, K15.
> - Steps 1–5 under Theorem [[§C9.9 CPT and the CPT Theorem#^thm-c9-9-5|§C9.9.5]] The Bilinears under C, P, T and CPT; register row "Bilinears under C, P, T, CPT".

### The axial vector under CPT ★★

$\mathsf A^\mu(t, \mathbf x) \to \mathsf A_\mu(-t, \mathbf x) \to -\mathsf A^\mu(-t, -\mathbf x) \to -\mathsf A^\mu(-t, -\mathbf x)$, so $\Theta\mathsf A^\mu(x)\Theta^{-1} = -\mathsf A^\mu(-x)$; vector indices always give a sign, see Example [[§C9.9 CPT and the CPT Theorem#^ex-c9-9-1|§C9.9.1]] The Axial Vector under CPT. *Source: Lecture 12 (Oct 12), slide 25*

^nd-ex-c9-9-1

- [ ] Q1 **[state]** State the three steps and the result.
- [ ] Q2 The $T$ step: which theorem, and why do its components match slide 25's $\mathsf A_\mu(-t, \mathbf x)$?
- [ ] Q3 The $P$ step: why the overall minus sign and the raised index?
- [ ] Q4 The $C$ step: why nothing changes.
- [ ] Q5 **[why]** "Upshot: vector indices always give a sign flip, whether on the field or on the argument". Why are $\mathsf A_\mu\mathsf A^\mu$ and $\partial_\mu\mathsf A^\mu$ CPT invariant?

> [!tip]- Hints: route in the notes
> - Technique: K15, K2.
> - The example's computation; Theorem [[§C9.8 Time Reversal#^thm-c9-8-13|§C9.8.13]] The Axial Vector under Time Reversal, Theorem [[§C9.4 Fermion Bilinears under Parity#^thm-c9-4-4|§C9.4.4]] The Sixteen Bilinears under Parity, Theorem [[§C9.6 Charge Conjugation on the Field and Bilinears#^thm-c9-6-9|§C9.6.9]] The Axial Vector Is Charge-Conjugation Invariant.

### The CPT theorem and the idea of proof ★★

Every local, Lorentz-invariant QFT (finitely many fields and derivatives) with a Hermitian Lagrangian has $\Theta\hat{\mathcal L}(x)\Theta^{-1} = \hat{\mathcal L}(-x)$ and an invariant action; idea: $\Theta$ reverses the whole four-vector and gives $(-1)^n$ per bilinear with $n$ indices, so contracted terms are invariant, see Theorem [[§C9.9 CPT and the CPT Theorem#^thm-c9-9-6|§C9.9.6]] The CPT Theorem. *Source: Lecture 12 (Oct 12), slides 24–25 ("Idea of proof: invariance under 4-vector inversion $x \to -x$"; "Full proof of CPT theorem: consider all possible terms") · PS §3.6, p. 71*

^nd-thm-c9-9-6

- [ ] Q1 **[state]** State the theorem with its hypotheses, and what "local" means on slide 24.
- [ ] Q2 What does $\Theta$ do to the Dirac field and to its argument?
- [ ] Q3 Why does each vector index, on a field or on the argument, give one sign?
- [ ] Q4 **[why]** Why do invariant terms have their indices in pairs (or contracted with $\varepsilon$, four indices), and why does Hermiticity matter?
- [ ] Q5 **[conv]** Slide 24: "tensor = gravity is not". What does the caution in the notes say about this?
- [ ] Q6 **[why]** Name two consequences of the theorem (masses, lifetimes) and explain why $CPT$ is "mandatory".

> [!tip]- Hints: route in the notes
> - Technique: K14 (Lorentz-invariance argument).
> - Idea-of-proof steps 1–5 under Theorem [[§C9.9 CPT and the CPT Theorem#^thm-c9-9-6|§C9.9.6]] The CPT Theorem; [[§C9.9 CPT and the CPT Theorem#^cau-c9-9-2|§C9.9, Caution: "Tensor = gravity is not"]]; [[§C9.9 CPT and the CPT Theorem#^rem-c9-9-2|§C9.9, Remark: Consequences of the CPT theorem, and the status of the discrete symmetries]]. The ★ derivation ($x \to -x$ as a complex Lorentz transformation) is beyond the lecture.

### CPT invariance of a Hermitian local Lorentz scalar (qualitative) ★

Any Hermitian, local, Lorentz-scalar operator built from a Dirac field, a complex scalar and their conjugates satisfies $\Theta\hat O(x)\Theta^{-1} = \hat O(-x)$, see Example [[§C9.9 CPT and the CPT Theorem#^ex-c9-9-2|§C9.9.2]] Why a Hermitian, Local Lorentz Scalar Is CPT Invariant (a Qualitative Argument). *Source: Problem Set 7, Problem 4(c)*

^nd-ex-c9-9-2

→ drilled as [[PHY 513 PS Drill#^ps7-4-c|PS7.4(c)]]

### C and T on the complex scalar field ★

$U(\mathcal C)\hat\phi(x)U(\mathcal C)^{-1} = \hat\phi^\dagger(x)$ from $\hat a \leftrightarrow \hat b$; $U(\mathcal T)\hat\phi(t, \mathbf x)U(\mathcal T)^{-1} = \hat\phi(-t, \mathbf x)$ from $\hat a_{\mathbf p} \to \hat a_{-\mathbf p}$ with $U(\mathcal T)$ antiunitary, see Theorem [[§C9.10 C, T and CPT for the Complex Scalar Field#^thm-c9-10-1|§C9.10.1]] Charge Conjugation on the Complex Scalar Field and Theorem [[§C9.10 C, T and CPT for the Complex Scalar Field#^thm-c9-10-2|§C9.10.2]] Time Reversal on the Complex Scalar Field. *Source: Problem Set 7, Problem 4(a) (PS Problem 3.7)*

^nd-thm-c9-10-1

→ drilled as [[PHY 513 PS Drill#^ps7-4-a|PS7.4(a)]]

### The U(1) current of the complex scalar under P, C and T ★

$\hat j^\mu \to +\mathcal P^\mu{}_\nu\hat j^\nu(\tilde x)$ under $P$, $-\hat j^\mu(x)$ under $C$, $+\mathcal P^\mu{}_\nu\hat j^\nu(x_T)$ under $T$, see Theorem [[§C9.10 C, T and CPT for the Complex Scalar Field#^thm-c9-10-4|§C9.10.4]] The U(1) Current under P, C and T. *Source: Problem Set 7, Problem 4(b)*

^nd-thm-c9-10-4

→ drilled as [[PHY 513 PS Drill#^ps7-4-b|PS7.4(b)]]

### C and T on the scalar's derivatives and Lagrangian; CPT on the scalar ★

$U(\mathcal C)\partial^\mu\hat\phi U(\mathcal C)^{-1} = \partial^\mu\hat\phi^\dagger$, $U(\mathcal T)\partial^\mu\hat\phi(x)U(\mathcal T)^{-1} = -\mathcal P^\mu{}_\nu(\partial^\nu\hat\phi)(x_T)$; the free complex Lagrangian is $C$ and $T$ invariant; $\Theta\hat\phi(x)\Theta^{-1} = \hat\phi^\dagger(-x)$ and each derivative index gives $-1$, see Theorem [[§C9.10 C, T and CPT for the Complex Scalar Field#^thm-c9-10-3|§C9.10.3]] Charge Conjugation and Time Reversal on the Derivatives, Theorem [[§C9.10 C, T and CPT for the Complex Scalar Field#^thm-c9-10-5|§C9.10.5]] The Free Complex Scalar Lagrangian Is C and T Invariant, Theorem [[§C9.10 C, T and CPT for the Complex Scalar Field#^thm-c9-10-6|§C9.10.6]] CPT on the Complex Scalar Field. *Source: the user's notes (with Problem Set 7, Problem 4) · Yu §9.1*

^nd-thm-c9-10-6

- [ ] Q1 **[state]** State the derivative rules under $C$ and $T$ and the $CPT$ law of the scalar field.
- [ ] Q2 Why does the time derivative change sign under $T$ while the space derivatives do not?
- [ ] Q3 Check $C$ and $T$ invariance of $\partial_\mu\hat\phi^\dagger\partial^\mu\hat\phi - m^2\hat\phi^\dagger\hat\phi$ (what does $C$ do to the order of the two factors, and does it matter for bosons?).
- [ ] Q4 Compose $T$, $P$, $C$ on $\hat\phi$ and on $\partial^\mu\hat\phi$.
- [ ] Q5 **[why]** Compare with the Dirac field: what replaces the $\gamma^5$, and why are the scalar laws "bare operations on modes and points"?

> [!tip]- Hints: route in the notes
> - Technique: K15, K2.
> - Theorem [[§C9.10 C, T and CPT for the Complex Scalar Field#^thm-c9-10-3|§C9.10.3]] Charge Conjugation and Time Reversal on the Derivatives, Theorem [[§C9.10 C, T and CPT for the Complex Scalar Field#^thm-c9-10-5|§C9.10.5]] The Free Complex Scalar Lagrangian Is C and T Invariant, Theorem [[§C9.10 C, T and CPT for the Complex Scalar Field#^thm-c9-10-6|§C9.10.6]] CPT on the Complex Scalar Field; side by side [[§C9.10 C, T and CPT for the Complex Scalar Field#^rem-c9-10-2|§C9.10, Remark: The complex scalar and the Dirac field side by side]].

# Equivalences

## Equivalences
Each entry shows that two versions of one object agree (the rows of "How the objects grew" in [[PHY 513 Midterm Review]]).

### Matrix and index forms of the invariant product
$x^{\mathsf T}gy$ (Lecture 1, matrices) and $x_\mu y^\mu = g_{\mu\nu}x^\mu y^\nu$ (indices) are the same number, and the invariance proofs $\Lambda^{\mathsf T}g\Lambda = g$ and $g_{\mu\nu}\Lambda^\mu{}_\alpha\Lambda^\nu{}_\beta = g_{\alpha\beta}$ are the same statement, see Definition [[§C1a.4 The Lorentz Group#^def-c1a-4-1|§C1a.4.1]] Lorentz Transformation, Active Reading and Theorem [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-2|§C1a.5.2]] The Metric Identifies Vectors with Covectors. *Source: Lecture 1 (Aug 31), slides "Invariants", "Index Gymnastics"*

^nd-eq-t1-1

- [ ] Q1 **[def]** Write the defining condition of $O(1,3)$ in both notations and show they agree entry by entry.
- [ ] Q2 Show that "lowering an index" is the row vector $x^{\mathsf T}g$ of Lecture 1.
- [ ] Q3 **[why]** Why is the transpose in $\Lambda^{\mathsf T}g\Lambda$ the change-of-basis rule of a bilinear form rather than of a linear map?

> [!tip]- Hints: route in the notes
> - Technique: K2
> - Theorem [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-2|§C1a.5.2]] The Metric Identifies Vectors with Covectors, steps 2 and 4; Definition [[§C1a.4 The Lorentz Group#^def-c1a-4-1|§C1a.4.1]] Lorentz Transformation, Active Reading.

### The dual Maxwell equation and the cyclic Bianchi identity
$\partial_\mu\tilde F^{\mu\nu} = 0 \Longleftrightarrow \partial^\rho F^{\mu\nu} + \partial^\mu F^{\nu\rho} + \partial^\nu F^{\rho\mu} = 0$, see Theorem [[§C1a.7 Relativistic Electrodynamics in Index Form#^thm-c1a-7-1|§C1a.7.1]] Maxwell's Equations in Heaviside–Lorentz Form. *Source: the user's notes Ch. 1 §1.7*

^nd-eq-t1-2

- [ ] Q1 **[state]** State both forms.
- [ ] Q2 Contract the cyclic sum with $\varepsilon_{\lambda\rho\mu\nu}$: what do the three terms give?
- [ ] Q3 Conversely, why does the dual equation, with four components, determine the totally antisymmetric cyclic sum?
- [ ] Q4 **[why]** Which two of Maxwell's four equations are these, and why do they hold identically for $F$ built from $A$?

> [!tip]- Hints: route in the notes
> - Technique: K2
> - Derivation of Theorem [[§C1a.7 Relativistic Electrodynamics in Index Form#^thm-c1a-7-1|§C1a.7.1]] Maxwell's Equations in Heaviside–Lorentz Form, steps 4–5.

### Active and passive forms of the E_x boost
$E'_x = \gamma(E_x + vB_y)$ (active boost by $+v\hat{\mathbf z}$, the vault) and $E'_x = \gamma(E_x - vB_y)$ (the Lecture 1 slide) are the same law read in the two conventions, see Example [[§C1a.7 Relativistic Electrodynamics in Index Form#^ex-c1a-7-1|§C1a.7.1]] The Lecture's Boost Example, Done with the Active Boost and [[§C1a.7 Relativistic Electrodynamics in Index Form#^cau-c1a-7-2|§C1a.7, Caution: The sign of the v × B term]]. *Source: Lecture 1 (Aug 31), slide "Example: Relativistic Electrodynamics"*

^nd-eq-t1-3

- [ ] Q1 **[state]** State both formulas and the matrix entry $\Lambda_0{}^3$ each corresponds to.
- [ ] Q2 Show that replacing $v \to -v$ maps one formula to the other, and say which observer moves in which direction in each reading.
- [ ] Q3 **[why]** Why are group statements (closure, orbits, generators in $\omega_{\mu\nu}$) identical in both readings while this formula is not?

> [!tip]- Hints: route in the notes
> - Technique: K14
> - [[§C1a.4 The Lorentz Group#^cau-c1a-4-1|§C1a.4, Caution: Active and passive readings]], [[§C1a.7 Relativistic Electrodynamics in Index Form#^cau-c1a-7-2|§C1a.7, Caution: The sign of the v × B term]].

### The two radial forms of the amplitude
$\frac{1}{2\pi^2r}\int_0^\infty dp\,p\sin(pr)e^{-iE_pz} = \frac{1}{4\pi^2ir}\int_{-\infty}^\infty dp\,p\,e^{i(pr - E_pz)}$ for $\operatorname{Im}z < 0$, see Theorem [[§C1a.3 Causal Structure and the Causality of a Single Particle#^thm-c1a-3-5|§C1a.3.5]] The Relativistic Amplitude as a Radial Integral. *Source: Lecture 2 (Sep 2), slide "Relativistic Quantum Causality"; PS (2.3)*

^nd-eq-t2-1

- [ ] Q1 **[state]** State the two forms and where each converges absolutely.
- [ ] Q2 Show the equality: evenness, $\int_0^\infty = \frac12\int_{-\infty}^\infty$, and the substitution $p \to -p$ in one exponential.
- [ ] Q3 **[why]** Why is the line form the one used for the saddle point?

> [!tip]- Hints: route in the notes
> - Technique: K13
> - Derivation of Theorem [[§C1a.3 Causal Structure and the Causality of a Single Particle#^thm-c1a-3-5|§C1a.3.5]] The Relativistic Amplitude as a Radial Integral, step 3.

### The single-particle amplitude and the Wightman function
$U(t, \mathbf x) = 2i\partial_tD_W(t, \mathbf x)$: the leak of the single particle is the Wightman function's, which field theory keeps as a correlation while the commutator vanishes, see Theorem [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-7|§C2b.3.7]] The Single-Particle Amplitude Is a Time Derivative of the Wightman Function and Theorem [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-7|§C2b.4.7]] Forward and Backward Amplitudes. *Source: the user's notes Ch. 2 §2.2, Ch. 5*

^nd-eq-t2-2

- [ ] Q1 **[state]** State the relation between $U$ and $D_W$.
- [ ] Q2 Differentiate the mode integral of $D_W$ in $t$: where does the factor $2E_{\mathbf p}$ of the measure go?
- [ ] Q3 **[why]** Why does the relativistic normalization of states make the factor $2i\partial_t$ appear?
- [ ] Q4 **[why]** Why is a nonzero $D_W$ at spacelike separation not a violation of causality in field theory?

> [!tip]- Hints: route in the notes
> - Technique: K9 (mode substitution)
> - Theorem [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-7|§C2b.3.7]] The Single-Particle Amplitude Is a Time Derivative of the Wightman Function; Theorem [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-7|§C2b.4.7]] Forward and Backward Amplitudes; [[§C1a.3 Causal Structure and the Causality of a Single Particle#^rem-c1a-3-3|§C1a.3, Remark: How field theory repairs causality]].

### Hamilton's equations and the Euler–Lagrange equation
For the free real field, $\dot\phi = \pi$ and $\dot\pi = \nabla^2\phi - m^2\phi$ combine into $(\partial_t^2 - \nabla^2 + m^2)\phi = 0$; in general the $2n$ first-order equations are equivalent to the $n$ Euler–Lagrange equations, see Example [[§C1b.4 Hamiltonian Field Theory#^ex-c1b-4-1|§C1b.4.1]] Hamilton's Equations of the Free Real Field and Theorem [[§C1b.4 Hamiltonian Field Theory#^thm-c1b-4-4|§C1b.4.4]] Hamilton's Equations for Fields. *Source: the user's notes Ch. 3 §3.4*

^nd-eq-t3-1

- [ ] Q1 **[state]** State the two first-order equations for the free real field.
- [ ] Q2 Combine them into the Klein–Gordon equation.
- [ ] Q3 In general, why does $\dot\phi = \partial\mathcal H/\partial\pi$ invert the definition of $\pi$?
- [ ] Q4 **[why]** Why is the first-order form "the form quantum mechanics wants"?

> [!tip]- Hints: route in the notes
> - Example [[§C1b.4 Hamiltonian Field Theory#^ex-c1b-4-1|§C1b.4.1]] Hamilton's Equations of the Free Real Field; derivation of Theorem [[§C1b.4 Hamiltonian Field Theory#^thm-c1b-4-4|§C1b.4.4]] Hamilton's Equations for Fields, steps 7–8.

### Complex field: complex and real Euler–Lagrange equations
The equations $\partial_\mu\frac{\partial\mathcal L}{\partial(\partial_\mu\phi^\ast)} = \frac{\partial\mathcal L}{\partial\phi^\ast}$ (and conjugate) are equivalent to the two real equations of $\phi_1$, $\phi_2$; the complex Lagrangian is two real ones of equal mass, see Theorem [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-8|§C1b.2.8]] The Complex Field Is Two Real Fields of Equal Mass and Theorem [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-9|§C1b.2.9]] Field and Conjugate as Independent Variables. *Source: the user's notes Ch. 2 §2.3, Ch. 3 §3.3*

^nd-eq-t3-2

- [ ] Q1 **[state]** State both forms of the field equations for the free complex field.
- [ ] Q2 Show that $(\partial^2 + m^2)\phi = 0$ is equivalent to $(\partial^2 + m^2)\phi_j = 0$ for $j = 1, 2$.
- [ ] Q3 **[why]** Why does the complex Hamiltonian density equal the sum of the two real ones, with $\pi = (\pi_1 - i\pi_2)/\sqrt2$?

> [!tip]- Hints: route in the notes
> - Theorem [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-9|§C1b.2.9]] Field and Conjugate as Independent Variables, step 4; Theorem [[§C1b.4 Hamiltonian Field Theory#^thm-c1b-4-3|§C1b.4.3]] Hamiltonian Density of the Free Complex Field, step 5 of its derivation.

### Three readings of the conjugate momentum
$\pi = \partial\mathcal L/\partial\dot\phi$ (density), $\pi = \delta L/\delta\dot\phi(\mathbf x)$ (functional derivative), $p_j = \pi(\mathbf x_j)\Delta V$ (cells), see Definition [[§C1b.4 Hamiltonian Field Theory#^def-c1b-4-1|§C1b.4.1]] Canonical Momentum Density and Theorem [[§C1b.4 Hamiltonian Field Theory#^thm-c1b-4-1|§C1b.4.1]] The Momentum Density Is a Functional Derivative. *Source: Lecture 3 (Sep 9), slides "Hamiltonian in Mechanics", "Hamiltonian in Field Theory" · PS §2.2 p. 16*

^nd-eq-t3-3

- [ ] Q1 **[state]** State the three forms.
- [ ] Q2 Show the first two agree for a local $\mathcal L$.
- [ ] Q3 **[why]** Why does the delta function $\delta^3(\mathbf x - \mathbf y)$ in the bracket correspond to $\delta_{ij}/\Delta V$ on the lattice?

> [!tip]- Hints: route in the notes
> - Derivation of Theorem [[§C1b.4 Hamiltonian Field Theory#^thm-c1b-4-1|§C1b.4.1]] The Momentum Density Is a Functional Derivative, steps 3–4; Theorem [[§C1b.4 Hamiltonian Field Theory#^thm-c1b-4-5|§C1b.4.5]] Fundamental Brackets of Fields.

### The lecture's Noether theorem and the general form
A point-moving symmetry is a symmetry of the action with $\alpha\Delta\phi = \bar\delta\phi$ and $\alpha\mathcal J^\mu = -\mathcal L\,\delta x^\mu$, and the two currents coincide term by term, see Theorem [[§C1b.7 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-7-4|§C1b.7.4]] The Two Forms of Noether's Theorem Agree. *Source: the user's notes Ch. 3 §3.5 ("The dictionary to the lecture's Δφ and 𝒥")*

^nd-eq-t4-1

- [ ] Q1 **[state]** State the dictionary between the two forms.
- [ ] Q2 From the symmetry condition, derive $\bar\delta\mathcal L = -\partial_\mu(\mathcal L\,\delta x^\mu)$.
- [ ] Q3 Compare the two currents term by term.
- [ ] Q4 **[conv]** Why must $\Delta\phi$ and $\mathcal J$ come from the same picture? Give the error that mixing produces.

> [!tip]- Hints: route in the notes
> - Technique: K12
> - Derivation of Theorem [[§C1b.7 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-7-4|§C1b.7.4]] The Two Forms of Noether's Theorem Agree, steps 1–4; [[§C1b.7 Spacetime Symmetries꞉ Energy and Momentum#^cau-c1b-7-1|§C1b.7, Caution: One picture at a time; the sign of the displacement]].

### T⁰⁰ from Noether and the Legendre transform
The charge density of time translations, $T^{00} = \sum\pi_a\dot\phi_a - \mathcal L$, is the Hamiltonian density of the Legendre transform, see Theorem [[§C1b.7 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-7-6|§C1b.7.6]] Energy and Momentum of a Field and [[§C1b.7 Spacetime Symmetries꞉ Energy and Momentum#^rem-c1b-7-1|§C1b.7, Remark: Why the 00 component is the Hamiltonian density]]. *Source: Lecture 3 (Sep 9), slide "Energy Density"*

^nd-eq-t4-2

- [ ] Q1 **[state]** State the equality and what each side is defined as.
- [ ] Q2 Show it for a general $\mathcal L(\phi_a, \partial_\mu\phi_a)$.
- [ ] Q3 **[why]** Why do the two constructions have to agree?
- [ ] Q4 **[why]** Why is $H$ the time component of a four-vector rather than a scalar?

> [!tip]- Hints: route in the notes
> - Theorem [[§C1b.7 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-7-6|§C1b.7.6]] Energy and Momentum of a Field, step 2 of its derivation; [[§C1b.7 Spacetime Symmetries꞉ Energy and Momentum#^rem-c1b-7-1|§C1b.7, Remark: Why the 00 component is the Hamiltonian density]].

### Two routes to the translation current
The lecture's route ($\Delta_\nu\phi = \partial_\nu\phi$, $\mathcal J^\mu{}_\nu = \delta^\mu{}_\nu\mathcal L$) and the general form ($\bar\delta\phi = -\varepsilon^\rho\partial_\rho\phi$, $j^\mu = -\varepsilon^\rho T^\mu{}_\rho$) give the same tensor with opposite parameter conventions, see Theorem [[§C1b.7 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-7-5|§C1b.7.5]] Translation Invariance Conserves the Energy–Momentum Tensor. *Source: Lecture 3 (Sep 9), slide "Example 3: Spacetime Translation" · Yu (1.209)*

^nd-eq-t4-3

- [ ] Q1 **[state]** State both currents and the relation between $a$ and $\varepsilon$.
- [ ] Q2 Run the second route: displacement, fixed-argument change, current.
- [ ] Q3 **[conv]** Why does the overall sign of a current never affect its conservation?

> [!tip]- Hints: route in the notes
> - Technique: K12
> - The two derivations of Theorem [[§C1b.7 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-7-5|§C1b.7.5]] Translation Invariance Conserves the Energy–Momentum Tensor; [[§C1b.7 Spacetime Symmetries꞉ Energy and Momentum#^cau-c1b-7-1|§C1b.7, Caution: One picture at a time; the sign of the displacement]].

### Two routes to the Lorentz current of a scalar
The general form ($\bar\delta\phi$, $\mathcal L\delta x$) and the lecture's form ($\Delta^{\nu\rho}\phi = x^\nu\partial^\rho\phi - x^\rho\partial^\nu\phi$ with $\mathcal J$ from the test) both give $\mathcal M^{\mu\nu\rho} = x^\nu T^{\mu\rho} - x^\rho T^{\mu\nu}$, see Theorem [[§C1b.8 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^thm-c1b-8-1|§C1b.8.1]] The Lorentz Current. *Source: the user's notes Ch. 3 §3.5 (Example 4)*

^nd-eq-t4-4

- [ ] Q1 **[state]** State the current of the second route.
- [ ] Q2 Compute $\delta\mathcal L$ in the second route and show it is $-\partial_\sigma(\omega^\sigma{}_\rho x^\rho\mathcal L)$. Which trace vanishes?
- [ ] Q3 Assemble the current and compare with the first route.
- [ ] Q4 **[why]** Why does the lecture's route need a nonzero $\mathcal J$ while the general form finds the same term as $\mathcal L\,\delta x^\mu$ without a test?

> [!tip]- Hints: route in the notes
> - Technique: K12
> - Second-route derivation of Theorem [[§C1b.8 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^thm-c1b-8-1|§C1b.8.1]] The Lorentz Current, steps 1–4.

### The U(1) current and the SO(2) rotation current
$i(\phi\partial^\mu\phi^\ast - \phi^\ast\partial^\mu\phi) = \phi_1\partial^\mu\phi_2 - \phi_2\partial^\mu\phi_1$ for $\phi = (\phi_1 + i\phi_2)/\sqrt2$, see Example [[§C1b.6 Conserved Charges and Internal Symmetries#^ex-c1b-6-2|§C1b.6.2]] Two Real Fields: One Rotation or Two Shifts and Theorem [[§C1b.6 Conserved Charges and Internal Symmetries#^thm-c1b-6-3|§C1b.6.3]] The U(1) Current of the Complex Scalar Field. *Source: the user's notes Ch. 3 §3.5*

^nd-eq-t4-5

- [ ] Q1 **[state]** State the identity.
- [ ] Q2 Expand $\phi\partial\phi^\ast$ and $\phi^\ast\partial\phi$ in real components and subtract.
- [ ] Q3 **[why]** Why must the phase current equal a rotation current, given the phase is a rotation of $(\phi_1, \phi_2)$?

> [!tip]- Hints: route in the notes
> - Example [[§C1b.6 Conserved Charges and Internal Symmetries#^ex-c1b-6-2|§C1b.6.2]] Two Real Fields: One Rotation or Two Shifts (a); Theorem [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-8|§C1b.2.8]] The Complex Field Is Two Real Fields of Equal Mass, part on the phase.

### Field commutators ⇔ oscillator algebra: the two directions

The equal-time relations of $\hat\phi$, $\hat\pi$ and the algebra $[\hat a_{\mathbf p}, \hat a^\dagger_{\mathbf q}] = (2\pi)^3\delta^3(\mathbf p - \mathbf q)$ are equivalent, given the expansion; Lecture 4 proved oscillators ⇒ fields, Problem Set 3 fields ⇒ oscillators, see Theorem [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|§C2a.2.6]] The Mode Algebra, Theorem [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-5|§C2a.2.5]] Mode Extraction. *Source: Lecture 4 (Sep 14), slide "Canonical Commutation Relations" · Problem Set 3, Problem 3 · the user's notes Ch. 4 §4.5*

^nd-eq-t5-1

- [ ] Q1 **[state]** State the equivalence and name what each direction assumes (expansion, extraction formula, slice independence).
- [ ] Q2 In the direction oscillators ⇒ fields, which mode functions are integrated against which? In the direction fields ⇒ oscillators, which inner product does the work?
- [ ] Q3 Why does the direction fields ⇒ oscillators need the extraction formula to be independent of the time slice?
- [ ] Q4 **[why]** In fields ⇒ oscillators, the commutator of two extracted operators equals the Klein–Gordon product of their mode functions. Why is the algebra "orthonormality in operator form"?
- [ ] Q5 **[why]** Why is the change of variables $(\hat\phi, \hat\pi) \leftrightarrow (\hat a, \hat a^\dagger)$ invertible at all? What would fail for a set of modes that is not complete?

> [!tip]- Hints: route in the notes
> - Technique: K10 (KG product), K9.
> - Step 1: the two derivations of Theorem [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|§C2a.2.6]] The Mode Algebra (first: extracted operators, steps 1–5; second: Lecture 4's route, steps 1–4).
> - Step 2: Theorem [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-3|§C2a.2.3]] Conservation and Orthonormality of the Modes, Theorem [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-5|§C2a.2.5]] Mode Extraction; general mode sets: [[§C2a.2 Mode Expansion and the Mode Algebra#^rem-c2a-2-5|§C2a.2, ★ Remark: Other mode functions, Bogoliubov transformations and the vacuum]].
> - Step 3: P1, step 6.

### Field form ⇔ mode form of H, P and Q: three ways the number-changing terms die

The field forms $\hat H = \int d^3x\,\mathcal H$, $\hat{\mathbf P} = -\int d^3x\,\hat\pi\nabla\hat\phi$, $\hat Q = \frac i2\int d^3x\,(\hat\phi^\dagger\hat\pi^\dagger - \hat\pi\hat\phi)$ become sums of number operators; the $\hat a\hat a$ and $\hat a^\dagger\hat a^\dagger$ terms vanish by different mechanisms, and the ordering constants differ, see Theorem [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-1|§C2a.3.1]] Hamiltonian in Mode Form, Theorem [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-5|§C2a.3.5]] Momentum in Mode Form, Theorem [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-4|§C2a.5.4]] Hamiltonian of the Complex Field, Theorem [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-5|§C2a.5.5]] Momentum of the Complex Field, Theorem [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-6|§C2a.5.6]] The Charge Counts Particles Minus Antiparticles. *Source: Lecture 4 (Sep 14) · Problem Set 3, Problem 2 · Problem Set 6, Problem 1 · the user's notes Ch. 4 §§4.6–4.7*

^nd-eq-t5-2

- [ ] Q1 **[state]** Write the field form and the mode form of $\hat H$ and $\hat{\mathbf P}$ (real field) and of $\hat Q$ (complex field).
- [ ] Q2 For the real field's $\hat H$: what makes the $\hat a_{\mathbf p}\hat a_{-\mathbf p}$ coefficient vanish, and what fails if $E_{\mathbf p}^2 \neq \mathbf p^2 + m^2$?
- [ ] Q3 For the real field's $\hat{\mathbf P}$: why do the number-changing terms vanish even off the mass shell?
- [ ] Q4 For the complex field's $\hat H$ and $\hat{\mathbf P}$: which commutator kills the number-changing terms?
- [ ] Q5 For $\hat Q$: how do the number-changing terms of the two products cancel?
- [ ] Q6 **[why]** Compare the ordering constants of $\hat H$, $\hat{\mathbf P}$ and $\hat Q$: which is infinite and harmless, which vanishes, and which must be removed for physical reasons?

> [!tip]- Hints: route in the notes
> - Technique: K9 (mode substitution).
> - Step 1: "What the derivation shows" in Theorem [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-1|§C2a.3.1]] Hamiltonian in Mode Form (mass shell), Theorem [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-5|§C2a.3.5]] Momentum in Mode Form (oddness), Theorem [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-4|§C2a.5.4]] Hamiltonian of the Complex Field and Theorem [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-5|§C2a.5.5]] Momentum of the Complex Field (species commute), Theorem [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-6|§C2a.5.6]] The Charge Counts Particles Minus Antiparticles (identical cancellation).
> - Step 2: constants: Theorem [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-4|§C2a.3.4]] The Zero-Point Energy; [[§C2a.5 The Complex Scalar Field and Its Charge#^rem-c2a-5-2|§C2a.5, Remark: Why the vacuum must be neutral]].

### Normal ordering from the outset ⇔ reorder, then drop the constant

Problem Sets 3 and 6 instruct that $\hat a_{\mathbf p}$ be placed to the right of $\hat a^\dagger_{\mathbf p}$ "from the outset", before the symbols become operators; computing in the order written and then reordering gives the same operator plus a constant, see Definition [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^def-c2a-3-1|§C2a.3.1]] Normal Ordering, [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^rem-c2a-3-2|§C2a.3, Remark: Normal ordering is a choice of quantization]], Example [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^ex-c2a-3-1|§C2a.3.1]] The Momentum, Normal-Ordered from the Outset. *Source: Problem Set 3 (instruction to Problem 2) · Problem Set 6, Problem 1 · the user's notes Ch. 4 §4.6*

^nd-eq-t5-3

- [ ] Q1 **[state]** State the two prescriptions precisely.
- [ ] Q2 For $\hat{\mathbf P}$, show that the two routes give the same operator. Which integral makes the would-be constant vanish, and under which regularization?
- [ ] Q3 For $\hat H$, by what constant do the two routes differ?
- [ ] Q4 For $\hat Q$, what would the unordered route give the vacuum, and why must that be dropped?
- [ ] Q5 **[why]** In what sense is normal ordering "a choice of quantization" rather than a subtraction?

> [!tip]- Hints: route in the notes
> - Technique: K11.
> - Step 1: step 8 of the derivation in Example [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^ex-c2a-3-1|§C2a.3.1]] The Momentum, Normal-Ordered from the Outset (the omitted constant); step 7 of Theorem [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-5|§C2a.3.5]] Momentum in Mode Form.
> - Step 2: Theorem [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-4|§C2a.3.4]] The Zero-Point Energy; step 6 of Theorem [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-6|§C2a.5.6]] The Charge Counts Particles Minus Antiparticles; [[§C2a.5 The Complex Scalar Field and Its Charge#^rem-c2a-5-2|§C2a.5, Remark: Why the vacuum must be neutral]].

### The real field as a constrained complex field, with one trap

Imposing $\hat\phi^\dagger = \hat\phi$ on the complex field's expansion and algebra gives $\hat b = \hat a$ and the real field; but setting $\hat b = \hat a$ in the complex Hamiltonian overcounts by a factor 2, see [[§C2a.5 The Complex Scalar Field and Its Charge#^rem-c2a-5-1|§C2a.5, Remark: The real field is a constrained complex field, with one trap]]. *Source: the user's notes Ch. 4 §§4.4–4.6*

^nd-eq-t5-4

- [ ] Q1 **[state]** Which identifications turn the complex field's mode expansion into the real one?
- [ ] Q2 Write $\hat\phi = (\hat\phi_1 + i\hat\phi_2)/\sqrt2$: how many real fields, of which masses?
- [ ] Q3 **[why]** Why does $\hat b = \hat a$ in the complex Hamiltonian give twice the real field's Hamiltonian?
- [ ] Q4 **[conv]** The complex field's zero-point constant is $2E_0$. Explain the factor from Q2.

> [!tip]- Hints: route in the notes
> - Technique: none.
> - Step 1: the remark box; Model [[§C2a.5 The Complex Scalar Field and Its Charge#^mod-c2a-5-1|§C2a.5.1]] The Free Complex Scalar Quantum Field; Theorem [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-4|§C2a.5.4]] Hamiltonian of the Complex Field; P1, "Pitfalls" (real from complex).

### Oscillators first ⇔ field first: two routes to the same quantum field

Lecture 4 quantized on one time slice and posited the mode expansion; the "field first" route derives the Klein–Gordon equation from the Heisenberg equations, expands its solutions and computes the algebra of the coefficients; both give the same field, see [[§C2b.1 Heisenberg Fields#^rem-c2b-1-4|§C2b.1, Remark: Two routes that meet]], Theorem [[§C2b.1 Heisenberg Fields#^thm-c2b-1-2|§C2b.1.2]] The Heisenberg Equations Are the Klein–Gordon Equation, Theorem [[§C2b.1 Heisenberg Fields#^thm-c2b-1-3|§C2b.1.3]] Free Fields Live on the Mass Shell. *Source: Lectures 4–5 · Yu §2.3 · the user's notes Ch. 4–5*

^nd-eq-t5-5

- [ ] Q1 **[state]** List the steps of each route.
- [ ] Q2 In the field-first route, which theorem says a solution of the Klein–Gordon equation has the mode form, and why only on the mass shell?
- [ ] Q3 Which postulates are common to both routes?
- [ ] Q4 **[why]** Where does each route use the form of $\hat H$, and which one never uses the mode expansion of $\hat H$?

> [!tip]- Hints: route in the notes
> - Technique: K9.
> - Step 1: Theorem [[§C2b.1 Heisenberg Fields#^thm-c2b-1-2|§C2b.1.2]] The Heisenberg Equations Are the Klein–Gordon Equation (only equal-time relations and the field form of $\hat H$); Theorem [[§C2b.1 Heisenberg Fields#^thm-c2b-1-3|§C2b.1.3]] Free Fields Live on the Mass Shell (mass shell); Theorem [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|§C2a.2.6]] The Mode Algebra.

### The Feynman propagator three ways: time-ordered product, contour, iε integral [class exercise, Lecture 6]

$D_F(x - y) = \langle0|T\{\hat\phi(x)\hat\phi(y)\}|0\rangle = \theta(\xi^0)D_W(\xi) + \theta(-\xi^0)D_W(-\xi)$ equals the Green's function of the Feynman contour and the limit $\varepsilon \to 0^+$ of $\int\frac{d^4p}{(2\pi)^4}\frac{ie^{-ip\cdot\xi}}{p^2 - m^2 + i\varepsilon}$, see Theorem [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-2|§C2b.6.2]] The Feynman Propagator, Theorem [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-9|§C2b.6.9]] The $i\varepsilon$ Prescriptions, Theorem [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-10|§C2b.6.10]] The $i\varepsilon$ Prescription Is a Limit in 𝒮′, Theorem [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-4|§C2b.6.4]] The Feynman Propagator as a Distribution: the Products θ·D_W. Larsen: "you want to practice a bit back and forth … three perspectives … how do you go back and forth from them?". *Source: Lecture 6 (Sep 21), slides "Evaluation of the Feynman Propagator" to "Relativistic Form of Feynman Propagator"; transcript · PS §2.4, eqs. (2.59)–(2.60) · the user's notes Ch. 6 §6.7, §6.9*

^nd-eq-t6-1

- [ ] Q1 **[state]** Write $D_F$ in the three forms.
- [ ] Q2 Contour → time-ordered: evaluate the Feynman contour for each sign of $t$ and recognize the two Wightman functions.
- [ ] Q3 Contour → $i\varepsilon$: which displacement of each pole reproduces the Feynman contour with the integral on the real axis? Show the denominator becomes $p^2 - m^2 + i\varepsilon$.
- [ ] Q4 Time-ordered → $i\varepsilon$ (Yu's direction): write $\theta(\pm t)$ as a contour integral and combine with the two Wightman mode integrals into one four-dimensional integral.
- [ ] Q5 **[why]** In which sense is the limit $\varepsilon \to 0^+$ taken, and why does the value $\theta(0)$ play no role in the slice definition?
- [ ] Q6 **[why]** Which form makes Lorentz invariance manifest, which makes the Green's-function property manifest, and which makes the physical ordering manifest?

> [!tip]- Hints: route in the notes
> - Technique: K13, K14.
> - Step 1: Theorem [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-2|§C2b.6.2]] The Feynman Propagator, both derivations (contour; second route from the time-ordered product, Yu (6.198)–(6.211)).
> - Step 2: Theorem [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-9|§C2b.6.9]] The $i\varepsilon$ Prescriptions step 2; Theorem [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-10|§C2b.6.10]] The $i\varepsilon$ Prescription Is a Limit in 𝒮′; Theorem [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-4|§C2b.6.4]] The Feynman Propagator as a Distribution: the Products θ·D_W; Green's-function property Theorem [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-5|§C2b.6.5]] The Free Schwinger–Dyson Equation.

### The commutator and Hadamard functions are the parts of the Wightman function

With $\xi = x - y$: $D = 2\operatorname{Im}D_W$, $D_1 = 2\operatorname{Re}D_W$, $D_W(\pm\xi) = \frac12(D_1(\xi) \pm iD(\xi))$; $D$ real and odd, $D_1$ real and even, both homogeneous solutions, see Theorem [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-3|§C2b.4.3]] The Commutator and Hadamard Functions Are the Parts of the Wightman Function. *Source: Problem Set 4, Problem 2 · the user's notes Ch. 5 §5.5*

^nd-eq-t6-2

- [ ] Q1 **[state]** Express $D$ and $D_1$ through $D_W(\xi)$ and $D_W(-\xi)$, and invert.
- [ ] Q2 Use $D_W(-\xi) = \overline{D_W(\xi)}$ to get the real and imaginary parts. Which property of $\hat\phi$ gives the conjugation rule?
- [ ] Q3 Show parity: $D$ odd, $D_1$ even.
- [ ] Q4 Write both as sine and cosine mode integrals.
- [ ] Q5 **[why]** Why is microcausality equivalent to the reality of $D_W$ at spacelike separation?

> [!tip]- Hints: route in the notes
> - Technique: K9.
> - Step 1: derivation steps 1–5; Theorem [[§C2b.2 The Wightman Function#^thm-c2b-2-4|§C2b.2.4]] The Wightman Function Is a Homogeneous Solution; Reversal Is Conjugation part 2.

### The Green's functions in terms of the Wightman function

$D_R = \theta(\xi^0)iD$, $D_A = -\theta(-\xi^0)iD$, $D_R - D_A = iD$, $\bar D = \frac12\operatorname{sgn}(\xi^0)iD$; $D_F = \frac12D_1 + \bar D = D_R + D_W(-\xi) = D_A + D_W(\xi)$; $D_{\bar F} = -\overline{D_F}$, $D_F - D_{\bar F} = D_1$; at spacelike separation $D_F = D_W = \frac12D_1$ and the others vanish, see Theorem [[§C2b.7 Wick Rotation and the Two-Point Family#^thm-c2b-7-5|§C2b.7.5]] Relations in the Two-Point Family. *Source: the user's notes Ch. 6 §6.8, §6.11 · Lecture 6 (Sep 21), slide "Green's Functions and Boundary Conditions"*

^nd-eq-t6-3

- [ ] Q1 **[state]** Write each of $D_R$, $D_A$, $\bar D$, $D_F$, $D_{\bar F}$ through $D_W(\pm\xi)$ and step functions.
- [ ] Q2 Derive $D_F = \frac12D_1 + \bar D$ from the step-function forms using $\theta(t) + \theta(-t) = 1$.
- [ ] Q3 Derive $D_F = D_R + D_W(-\xi)$ and $D_F = D_A + D_W(\xi)$.
- [ ] Q4 Second route, momentum space: split $\frac{i}{p^2 - m^2 + i\varepsilon}$ by Sokhotski–Plemelj. Which piece is $\tilde{\bar D}$ and which is $\frac12\tilde D_1$?
- [ ] Q5 Show that at spacelike separation all functions containing the commutator vanish. What is left?
- [ ] Q6 **[why]** Which of these functions are Green's functions and which homogeneous solutions? Why must every Green's function be "one Green's function plus a homogeneous solution"?

> [!tip]- Hints: route in the notes
> - Technique: K13.
> - Step 1: derivation steps 0–6 (position space); second derivation steps 1–3 (momentum space).
> - Step 2: the table [[§C2b.7 Wick Rotation and the Two-Point Family#^rem-c2b-7-2|§C2b.7, Remark: The two-point functions at a glance]]; Theorem [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-3|§C2b.5.3]] Contours Are Boundary Conditions.

### Contour ⇔ iε ⇔ boundary condition ⇔ support: the retarded case

The retarded function is at once the contour above both poles, the prescription $(p^0 + i\varepsilon)^2 - E_{\mathbf p}^2$, the boundary condition "nothing before the source", and the unique tempered fundamental solution supported in $\xi^0 \ge 0$, see Theorem [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-5|§C2b.5.5]] The Retarded Green's Function, Theorem [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-9|§C2b.6.9]] The $i\varepsilon$ Prescriptions, Theorem [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-6|§C2b.5.6]] The Product θ(ξ⁰)D Is Defined; Retarded Means Supported in the Future. *Source: Lecture 6 (Sep 21), slides "Retarded Contour: Qualitative Behavior", "Green's Functions and Boundary Conditions" · the user's notes Ch. 6 §6.6, §6.8*

^nd-eq-t6-4

- [ ] Q1 **[state]** State the four characterizations.
- [ ] Q2 Contour ⇒ support: why does the contour above both poles give zero for $t < 0$?
- [ ] Q3 Contour ⇔ $i\varepsilon$: which pole displacement corresponds to passing above both poles?
- [ ] Q4 Support ⇒ uniqueness: if two fundamental solutions vanish for $\xi^0 < 0$, why is their difference zero?
- [ ] Q5 **[why]** Which physical question fixes the retarded condition, and which one fixes the Feynman condition?

> [!tip]- Hints: route in the notes
> - Technique: K13.
> - Step 1: Theorem [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-5|§C2b.5.5]] The Retarded Green's Function steps 2–3; Theorem [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-9|§C2b.6.9]] The $i\varepsilon$ Prescriptions step 4; Theorem [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-6|§C2b.5.6]] The Product θ(ξ⁰)D Is Defined; Retarded Means Supported in the Future part 3.
> - Step 2: [[§C2b.7 Wick Rotation and the Two-Point Family#^rem-c2b-7-3|§C2b.7, Remark: Which Green's function when]] (which Green's function when); [[§C2b.8 Particle Production by a Classical Source#^rem-c2b-8-2|§C2b.8, Remark: The boundary condition was physics]].

### The Wightman function four ways

$D_W$ is the three-dimensional mode integral $\int\frac{d^3p}{(2\pi)^3\,2E_{\mathbf p}}e^{-ip\cdot\xi}$, the transform of $2\pi\theta(p^0)\delta(p^2 - m^2)$, the boundary value of the analytic $W(\xi^0 - i\varepsilon, \boldsymbol\xi)$, and (off the cone) the Bessel function $\frac{mK_1(ms)}{4\pi^2s}$, see Theorem [[§C2b.2 The Wightman Function#^thm-c2b-2-1|§C2b.2.1]] The Wightman Function as a Mode Integral, Theorem [[§C2b.2 The Wightman Function#^thm-c2b-2-2|§C2b.2.2]] The Wightman Function Is a Tempered Distribution, Theorem [[§C2b.2 The Wightman Function#^thm-c2b-2-5|§C2b.2.5]] The Wightman Function Is a Boundary Value, Theorem [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-2|§C2b.3.2]] The Wightman Function in the Lower Half-Plane. *Source: Lecture 5 (Sep 16) · PS §2.4, eqs. (2.50)–(2.52) · Problem Set 4 · the user's notes Ch. 5 §5.4*

^nd-eq-t6-5

- [ ] Q1 **[state]** Write the four forms.
- [ ] Q2 Three-dimensional ⇔ four-dimensional: do the $p^0$ integral of the shell distribution.
- [ ] Q3 Mode integral ⇔ boundary value: why does the mode integral converge for $\operatorname{Im}\xi^0 < 0$ and not for real $\xi$?
- [ ] Q4 Boundary value ⇔ Bessel form: which single integral is evaluated, and which theorem continues it?
- [ ] Q5 **[why]** Which form shows Lorentz invariance, which shows positivity of energy, and which gives the values at spacelike and timelike separation?

> [!tip]- Hints: route in the notes
> - Technique: K13, K14.
> - Step 1: Theorem [[§C2b.2 The Wightman Function#^thm-c2b-2-1|§C2b.2.1]] The Wightman Function as a Mode Integral step 5; Theorem [[§C2b.2 The Wightman Function#^thm-c2b-2-5|§C2b.2.5]] The Wightman Function Is a Boundary Value; Theorem [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-1|§C2b.3.1]] The Wightman Function at Imaginary Time, Theorem [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-2|§C2b.3.2]] The Wightman Function in the Lower Half-Plane; identity theorem Theorem [[§CA.4 Contour Integration#^thm-ca-4-3|§CA.4.3]] Identity Theorem.

### The spacelike Wightman function three ways

$D_W = \frac{m}{4\pi^2r}K_1(mr)$ at spacelike separation follows by analytic continuation of the Euclidean value, by wrapping a contour around the branch cut at equal times (Lecture 5's shortcut), and by real variables with a damping regulator (Problem Set 4's route), see Theorem [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-3|§C2b.3.3]] The Wightman Function at Spacelike Separation. The computation itself → drilled as [[PHY 513 PS Drill#^ps4-3-a|PS4.3(a)]]; the questions compare the routes. *Source: Lecture 5 (Sep 16), transcript · PS §2.4, eq. (2.52) · Problem Set 4, Problem 3(a) · the user's notes Ch. 5 §5.4*

^nd-eq-t6-6

- [ ] Q1 **[state]** State the result and name the three routes.
- [ ] Q2 Contour route: after the angular integral and folding onto the whole line, why can the contour not be closed with Jordan's lemma directly? What is done first?
- [ ] Q3 Where are the branch points of $\sqrt{p^2 + m^2}$, and why do the two lips of the cut add?
- [ ] Q4 Real-variable route: which exchange of a limit with a derivative needs uniform convergence?
- [ ] Q5 **[why]** The real-variable regulator $e^{-\varepsilon p}$ differs from the covariant $e^{-\varepsilon E_{\mathbf p}}$. Why does the choice not matter at spacelike separation?

> [!tip]- Hints: route in the notes
> - Technique: K13, K1.
> - Step 1: the three derivations of Theorem [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-3|§C2b.3.3]] The Wightman Function at Spacelike Separation (first: limit of the Bessel form; second: steps 1–8, keyhole; third: steps 1–5).
> - Step 2: [[§CA.4 Contour Integration#^cau-ca-4-1|§CA.4, Caution: Jordan's lemma needs g → 0]]; Theorem [[§CA.4 Contour Integration#^thm-ca-4-8|§CA.4.8]] Integrals around a Branch Cut; Theorem [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-3|§CA.1.3]] Limits of Derivatives.

### Microcausality in three forms

At spacelike separation $[\hat\phi(x), \hat\phi(y)] = 0$ ⇔ $D_W(\xi)$ is real (equal to $D_W(-\xi)$) ⇔ $\operatorname{supp}D$ lies in the closed light cone ⇔ $\hat\phi(x)$ is determined by the data in its backward cone, see Theorem [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-5|§C2b.4.5]] The Free Field Is Microcausal, Theorem [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-6|§C2b.4.6]] Microcausality as a Support Statement, Theorem [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-13|§C2b.4.13]] The Commutator Function Propagates the Field. *Source: Lecture 5 (Sep 16), transcript · the user's notes Ch. 5 §5.5, §5.7*

^nd-eq-t6-7

- [ ] Q1 **[state]** State the four forms.
- [ ] Q2 First route: Lorentz invariance of $D_W$ and a transformation reversing a spacelike $\xi$.
- [ ] Q3 Second route: why is $D_W$ real at spacelike separation as a function of $\xi^2$, and where is its cut?
- [ ] Q4 Show that the support statement implies the commutator of fields smeared over spacelike-separated regions vanishes.
- [ ] Q5 **[why]** Why are "commuting at spacelike separation" and "no propagation outside the cone" one statement?

> [!tip]- Hints: route in the notes
> - Technique: K14.
> - Step 1: both derivations of Theorem [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-5|§C2b.4.5]] The Free Field Is Microcausal; Theorem [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-6|§C2b.4.6]] Microcausality as a Support Statement; Theorem [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-13|§C2b.4.13]] The Commutator Function Propagates the Field; [[§C2b.4 Microcausality and the Commutator Function#^rem-c2b-4-5|§C2b.4, Remark: Microcausality and the domain of dependence are one statement]].

### Cauchy data: canonical relations ⇔ commutator function ⇔ retarded jump

The equal-time relations are the Cauchy data $D(0, \boldsymbol\xi) = 0$, $\partial_0D(0, \boldsymbol\xi) = -\delta^3$ of the commutator function, and $i$ times them are the data $D_R = 0$, $\partial_0D_R = -i\delta^3$ at $t = 0^+$ that make $D_R$ a Green's function, see Theorem [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-12|§C2b.4.12]] Cauchy Data of the Commutator Function, Theorem [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-10|§C2b.4.10]] Commutators at Unequal Times, Theorem [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-5|§C2b.5.5]] The Retarded Green's Function. *Source: the user's notes Ch. 5 §5.7, Ch. 6 §6.6*

^nd-eq-t6-8

- [ ] Q1 **[state]** State the data of $D$ and of $D_R$.
- [ ] Q2 Derive the data of $D$ from $[\hat\phi, \hat\phi]$ and $[\hat\phi, \hat\pi]$ at equal times.
- [ ] Q3 Show that a jump of $-i$ in $\partial_tG_R$ at $t = 0$ gives $-i\delta(t)$ in $G_R'' + E^2G_R$.
- [ ] Q4 **[why]** Why does quantizing on one time slice determine every commutator at every pair of times?

> [!tip]- Hints: route in the notes
> - Technique: K11, K13.
> - Step 1: Theorem [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-12|§C2b.4.12]] Cauchy Data of the Commutator Function steps 1–3; Theorem [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-5|§C2b.5.5]] The Retarded Green's Function step 6; P2, step 7.

### Normal ordering and the zero-point energy: modes ⇔ coincident points

The zero-point constant $V\int\frac{d^3p}{(2\pi)^3}\frac{E_{\mathbf p}}{2}$ from reordering modes equals $\frac12\int d^3x\lim_{y\to x}(\partial_{x^0}\partial_{y^0} + \nabla_x\cdot\nabla_y + m^2)D_W(x - y)$; normal ordering subtracts exactly the contraction, $\hat\phi\hat\phi = :\!\hat\phi\hat\phi\!: + D_W$, see Theorem [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-8|§C2b.6.8]] The Zero-Point Energy Is the Wightman Function at Coincident Points, Theorem [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-6|§C2b.6.6]] Contractions: Normal Ordering against Time Ordering, Theorem [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-4|§C2a.3.4]] The Zero-Point Energy. *Source: the user's notes Ch. 4 §4.6, Ch. 6 §6.7*

^nd-eq-t6-9

- [ ] Q1 **[state]** State both forms of the zero-point energy.
- [ ] Q2 Point-split the three products in $\hat H$ and separate the c-number part with the contraction.
- [ ] Q3 Do one mode: which combination of $E_{\mathbf p}^2$, $\mathbf p^2$ and $m^2$ appears, and how does it reduce to $E_{\mathbf p}/2$ per mode?
- [ ] Q4 Regulate at equal times with $e^{-\varepsilon E_{\mathbf p}}$: how fast does it diverge?
- [ ] Q5 **[why]** Why is the constant infinite, in terms of the singularity of $D_W$ on the light cone?

> [!tip]- Hints: route in the notes
> - Technique: K9.
> - Step 1: Theorem [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-8|§C2b.6.8]] The Zero-Point Energy Is the Wightman Function at Coincident Points steps 1–6; [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^rem-c2b-6-3|§C2b.6, Remark: One mechanism, two products]]; [[§CA.2 Generalized Functions#^rem-ca-2-2|§CA.2, Remark: Point splitting: how a product at one point is regularized]] (point splitting).

### Euclidean, Feynman and Wightman functions are one analytic function

$\mathcal W(s^2) = \frac{mK_1(ms)}{4\pi^2s}$ gives $D_E$ at Euclidean points, $D_F = \mathcal W(-\xi^2 + i0)$ and $D_W = \mathcal W(-\xi^2 + i0\xi^0)$ off the cone; in momentum space $\tilde D_F$ is the boundary value of $i/(w^2 - E_{\mathbf p}^2)$ from the first and third quadrants and becomes the Euclidean integrand on the imaginary axis, see Theorem [[§C2b.7 Wick Rotation and the Two-Point Family#^thm-c2b-7-4|§C2b.7.4]] Wick Rotation Continues One Distribution, Theorem [[§C2b.7 Wick Rotation and the Two-Point Family#^thm-c2b-7-2|§C2b.7.2]] The Feynman Function at Imaginary Time, Theorem [[§C2b.7 Wick Rotation and the Two-Point Family#^thm-c2b-7-3|§C2b.7.3]] The Feynman Function in Position Space. *Source: Lecture 6 (Sep 21), slide "Another perspective: the Euclidean Green's Function" ("Feynman prescription = Euclidean prescription, analytically continued") · the user's notes Ch. 6 §6.10*

^nd-eq-t6-10

- [ ] Q1 **[state]** State on which sets of $s^2$ the three functions are read.
- [ ] Q2 Momentum space: rotate $w = e^{i\vartheta}p^0$ and show that $iG(ip_4) = 1/(p_E^2 + m^2)$.
- [ ] Q3 Position space: show $D_F(-i\tau, \boldsymbol\xi) = D_E(\tau, \boldsymbol\xi)$.
- [ ] Q4 **[why]** Why does the light cone collapse to a point in Euclidean signature, and why is that useful?
- [ ] Q5 **[conv]** The slides write $p^0_E = ip^0_M$; the vault $p^0 = ip_4$. Check that both rotate counterclockwise.

> [!tip]- Hints: route in the notes
> - Technique: K13.
> - Step 1: Theorem [[§C2b.7 Wick Rotation and the Two-Point Family#^thm-c2b-7-4|§C2b.7.4]] Wick Rotation Continues One Distribution steps 1–5; Theorem [[§C2b.7 Wick Rotation and the Two-Point Family#^thm-c2b-7-1|§C2b.7.1]] Wick Rotation of a Momentum Integral; [[§C2b.7 Wick Rotation and the Two-Point Family#^rem-c2b-7-1|§C2b.7, Remark: Why the Feynman contour is singled out]].

### Differences of Green's functions: on the shell ⇔ homogeneous solutions

In momentum space $\tilde D_F - \tilde D_{\bar F} = 2\pi\delta(p^2 - m^2)$ and $\tilde D_R - \tilde D_A = 2\pi\operatorname{sgn}(p^0)\delta(p^2 - m^2)$; in position space these are $D_1$ and $iD$, homogeneous solutions, see Theorem [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-11|§C2b.6.11]] Differences on the Mass Shell, Theorem [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-3|§C2b.5.3]] Contours Are Boundary Conditions, Theorem [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-7|§CA.6.7]] Fundamental Solutions Differ by Homogeneous Solutions. *Source: the user's notes Ch. 6 §6.8–6.9*

^nd-eq-t6-11

- [ ] Q1 **[state]** State both differences in both spaces.
- [ ] Q2 Derive the momentum-space differences by Sokhotski–Plemelj.
- [ ] Q3 Transform back: identify $D_1$ and $iD$ through their shell transforms.
- [ ] Q4 **[why]** Why must the difference of two fundamental solutions be supported on the shell in momentum space?

> [!tip]- Hints: route in the notes
> - Technique: K13.
> - Step 1: Theorem [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-11|§C2b.6.11]] Differences on the Mass Shell; Theorem [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-4|§C2b.4.4]] The Commutator and Hadamard Functions as Distributions part 1; Theorem [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-7|§CA.6.7]] Fundamental Solutions Differ by Homogeneous Solutions part 2.

### iε from damping: a pole off the axis ⇔ a step function

A damping $e^{-\varepsilon t}$ on $t > 0$ makes $\tilde\theta(\omega) = \frac{i}{\omega + i\varepsilon}$, a pole below the real axis; conversely a pole just above the axis integrates to $\theta(k)$, see Theorem [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-5|§CA.6.5]] Damping Factors: the Transform of the Step Function, Example [[§CA.4 Contour Integration#^ex-ca-4-2|§CA.4.2]] A Step Function from a Pole. *Source: the user's notes App. A §A.5*

^nd-eq-t6-12

- [ ] Q1 **[state]** State both directions.
- [ ] Q2 Compute $\int_0^\infty dt\,e^{i\omega t - \varepsilon t}$.
- [ ] Q3 Invert: close the contour for each sign of $t$ and find which pole is enclosed.
- [ ] Q4 **[why]** How does this single fact underlie the positions of the poles in the retarded and Feynman prescriptions?

> [!tip]- Hints: route in the notes
> - Technique: K13.
> - Step 1: Theorem [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-5|§CA.6.5]] Damping Factors: the Transform of the Step Function; Example [[§CA.4 Contour Integration#^ex-ca-4-2|§CA.4.2]] A Step Function from a Pole; Theorem [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-9|§C2b.6.9]] The $i\varepsilon$ Prescriptions.

### Three forms of the Lorentz algebra

The covariant relation, the $\mathbf J$, $\mathbf K$ relations and two commuting angular-momentum algebras $\mathbf J_\pm$ are equivalent statements about six matrices, see [[§CB.5 The Lorentz Algebra꞉ Generators and Commutation Relations#^der-cb-5-6c|Derivation §CB.5.6, the J, K form and the J± split]] (step 8) and Theorem [[§CB.6 The Lorentz Algebra꞉ the Split J±, Real Forms and 𝔰𝔩(2,ℂ) as a Real Lie Algebra#^thm-cb-6-2|§CB.6.2]] A Representation of the Lorentz Algebra Is a Pair of Commuting Angular Momenta.

^nd-eq-t7-1

- [ ] Q1 **[state]** Write the three forms.
- [ ] Q2 Which change of basis connects $\{\mathcal J^{\mu\nu}\}$ with $\{J_i, K_i\}$, and which connects $\{J_i, K_i\}$ with $\{J_{\pm i}\}$? Over which field is each invertible?
- [ ] Q3 Why does each of the fifteen covariant commutators reduce to one of the $\mathbf J$, $\mathbf K$ relations?
- [ ] Q4 **[why]** The equivalence with the $\mathbf J_\pm$ form needs complex coefficients. Why is that harmless for a representation on a complex space?

> [!tip]- Hints: route in the notes
> - Technique: K3
> - Step 1 and step 8 of [[§CB.5 The Lorentz Algebra꞉ Generators and Commutation Relations#^der-cb-5-6c|Derivation §CB.5.6, the J, K form and the J± split]]; the converse: Theorem [[§CB.6 The Lorentz Algebra꞉ the Split J±, Real Forms and 𝔰𝔩(2,ℂ) as a Real Lie Algebra#^thm-cb-6-2|§CB.6.2]] A Representation of the Lorentz Algebra Is a Pair of Commuting Angular Momenta; complex-linear extension: Theorem [[§CB.4 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-4-9|§CB.4.9]] Complex Representations of 𝔤 Are Complex-Linear Representations of Its Complexification.

### Real and Hermitian conventions for generators

$\Lambda = e^{\frac12\omega_{\alpha\beta}M^{\alpha\beta}} = e^{-\frac i2\omega_{\alpha\beta}\mathcal J^{\alpha\beta}} = e^\omega$ with $\mathcal J = iM$; for fields, the real-convention spin generators of §C1b.1 are $S^{\mu\nu} = -iD(\mathcal J^{\mu\nu})$, so the lecture's Dirac $S^{\mu\nu} = \frac i4[\gamma^\mu, \gamma^\nu]$ is $D(\mathcal J^{\mu\nu})$, see Theorem [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-2|§C1a.6.2]] The Generators Reproduce ω and [[§C3.3 How Fields Transform under the Lorentz Group#^cau-c3-3-2|§C3.3, Caution: Two meanings of S^μν]].

^nd-eq-t7-2

- [ ] Q1 **[state]** Write the vector-representation exponential in both conventions and as $e^\omega$.
- [ ] Q2 **[conv]** Which convention does §C1b.1 use for the spin generators of a field, and which does the Dirac $S^{\mu\nu}$ of the lecture use? Give the factor between them.
- [ ] Q3 **[conv]** Yu writes $I^{\mu\nu} = iS^{\mu\nu}$. Which convention is that?
- [ ] Q4 **[why]** Why does the choice of convention not change the commutation relations' structure constants up to the overall factor of $i$?

> [!tip]- Hints: route in the notes
> - Technique: K2
> - Step 4 of [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^der-c1a-6-2|Derivation §C1a.6.2]]; [[§C3.3 How Fields Transform under the Lorentz Group#^cau-c3-3-2|§C3.3, Caution: Two meanings of S^μν]]; the sign in the exponent across sources: [[§C3.1 Index Slots, Rotations and Spin in Field Theory#^cau-c3-1-3|§C3.1, Caution: The sign in the exponent across sources]].

### The four-vector as (½, ½), as a bispinor and as (½, 0) ⊗ (0, ½)

The vector representation is equivalent to $(\frac12, \frac12)$ by the Casimirs and by the intertwiner $v \mapsto (v_\mu\sigma^\mu)i\sigma^2$; equivalently $X_{a\dot b} = x_\mu(\sigma^\mu)_{a\dot b}$ carries one undotted and one dotted index, $(\frac12, 0)\otimes(0, \frac12) = (\frac12, \frac12)$, see Theorem [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-17-7|§CB.17.7]] The Vector Representation Is (½, ½), Theorem [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-5|§C5a.5.5]] A Four-Vector Is a Bispinor and Theorem [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-17-12|§CB.17.12]] Tensor Products Add Each Copy Separately.

^nd-eq-t7-3

- [ ] Q1 **[state]** State the three descriptions of the four-vector representation.
- [ ] Q2 How does $x \to \Lambda x$ act on $X = x_\mu\sigma^\mu$ in terms of $\Lambda_L$? Which slot transforms with $\Lambda_L$ and which with $\Lambda_L^\ast$?
- [ ] Q3 Why is the conjugate of $(\frac12, 0)$ equivalent to $(0, \frac12)$, and what does the tensor-product rule give for $(\frac12, 0)\otimes(0, \frac12)$?
- [ ] Q4 **[why]** How is the intertwiner of [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^pf-cb-17-7b|proof of Theorem §CB.17.7, second route]] related to the matrix $X$ (what does the factor $i\sigma^2$ do)?

> [!tip]- Hints: route in the notes
> - Technique: K16
> - Steps 1–4 of [[§C5a.5 Chirality and Weyl Spinors#^der-c5a-5-5|Derivation §C5a.5.5]]; Theorem [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-17-14|§CB.17.14]] Complex Conjugation Exchanges the Two Copies; step 2 and the first bullet of "What the proof shows" of [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^pf-cb-17-7b|proof of Theorem §CB.17.7, second route]].

### The field law classically and as an operator commutator

Classically $\phi'_a(x) = \phi_a(x) - \frac i2\omega_{\mu\nu}(\mathbb J^{\mu\nu}\phi)_a$; for a quantum field $[\hat\Phi_a(x), \hat J^{\mu\nu}] = (\mathbb J^{\mu\nu}\hat\Phi)_a(x)$ with the same $\mathbb J = L + D(\mathcal J)$, see Theorem [[§C3.3 How Fields Transform under the Lorentz Group#^thm-c3-3-3|§C3.3.3]] Orbital Plus Spin and Theorem [[§C3.5 Covariant Quantum Fields and the Free Scalar's Representation#^thm-c3-5-3|§C3.5.3]] Lorentz Transformations of a Field: Orbital plus Spin.

^nd-eq-t7-4

- [ ] Q1 **[state]** Write both forms with the same total generator $\mathbb J^{\mu\nu}$.
- [ ] Q2 Starting from $U^{-1}\hat\Phi U = D\hat\Phi(\Lambda^{-1}x)$, show the operator form reduces to the classical first-order law with $\delta\hat\Phi = -\frac i2\omega_{\mu\nu}[\hat\Phi, \hat J^{\mu\nu}]$. Which sign of $U$ is used?
- [ ] Q3 **[why]** In which form do both $D$ and $U$ appear, and in which only $D$?

> [!tip]- Hints: route in the notes
> - Technique: K14
> - [[§C3.3 How Fields Transform under the Lorentz Group#^der-c3-3-3|Derivation §C3.3.3]] and Steps 2–5 of [[§C3.5 Covariant Quantum Fields and the Free Scalar's Representation#^der-c3-5-3|Derivation §C3.5.3]]; Noether charges as generators for the scalar: Theorem [[§C3.5 Covariant Quantum Fields and the Free Scalar's Representation#^thm-c3-5-6|§C3.5.6]] The Noether Charges Are the Generators.

### Two forms of the scalar field's transformation

$U(\Lambda, a)\hat\phi(x)U(\Lambda, a)^{-1} = \hat\phi(\Lambda x + a)$ is equivalent to $U^{-1}(\Lambda, a)\hat\phi(x)U(\Lambda, a) = \hat\phi(\Lambda^{-1}(x - a))$, see Theorem [[§C3.5 Covariant Quantum Fields and the Free Scalar's Representation#^thm-c3-5-5|§C3.5.5]] The Free Scalar Field Transforms as a Scalar.

^nd-eq-t7-5

- [ ] Q1 **[state]** Write both forms.
- [ ] Q2 Derive the second from the first by applying it to $(\Lambda, a)^{-1}$. What is $(\Lambda, a)^{-1}$?
- [ ] Q3 **[conv]** Which form is the vault's convention for all fields, and which form do Lectures 11–12 use for P, C, T?

> [!tip]- Hints: route in the notes
> - Technique: K14
> - Steps 3–4 of [[§C3.5 Covariant Quantum Fields and the Free Scalar's Representation#^der-c3-5-5|Derivation §C3.5.5]]; the inverse in the group: step 1 of [[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra#^der-c3-4-3|Derivation §C3.4.3]]; the side of the inverse for discrete symmetries: [[§C9.3 Parity on States, Spinors and the Dirac Field#^cau-c9-3-1|§C9.3, Caution: Which side the inverse is on, and the names of the phases]].

### Three forms of the covariance of γ

$\Lambda_{1/2}^{-1}\gamma^\mu\Lambda_{1/2} = \Lambda^\mu{}_\nu\gamma^\nu$ (vault), $\Lambda_{1/2}\gamma^\mu\Lambda_{1/2}^{-1} = (\Lambda^{-1})^\mu{}_\nu\gamma^\nu$ (Lecture 8), and $\gamma^\nu = \Lambda^\nu{}_\mu\Lambda_{1/2}\gamma^\mu\Lambda_{1/2}^{-1}$ ("$\gamma$ does not transform") are one statement, see Theorem [[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-18-7|§CB.18.7]] The Dirac Matrices Are an Invariant Vector of Matrices and [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^rem-c5a-4-2|§C5a.4, Remark: The lecture's form of the covariance]].

^nd-eq-t8-1

- [ ] Q1 **[state]** Write the three forms.
- [ ] Q2 Obtain the Lecture 8 form from the vault's by $\omega \to -\omega$. What are $\Lambda_{1/2}(-\omega)$ and $e^{-\omega}$?
- [ ] Q3 Obtain the third form by multiplying with $\Lambda^\nu{}_\mu$.
- [ ] Q4 **[conv]** PS's infinitesimal form has the opposite sign of $\omega$. Why is that no contradiction?

> [!tip]- Hints: route in the notes
> - Technique: K2
> - [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^rem-c5a-4-2|§C5a.4, Remark: The lecture's form of the covariance]]; Theorem [[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-18-7|§CB.18.7]] The Dirac Matrices Are an Invariant Vector of Matrices.

### The Dirac equation in three forms

$(i\slashed\partial - m)\psi = 0$; in chiral blocks $i\bar\sigma^\mu\partial_\mu\psi_L = m\psi_R$, $i\sigma^\mu\partial_\mu\psi_R = m\psi_L$; in Hamiltonian form $i\partial_t\psi = H_{\text{s.p.}}\psi$, see Theorem [[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-10|§C5a.7.10]] The Dirac Equation in Two-Component Form and Theorem [[§C5a.8 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-8-2|§C5a.8.2]] The Hamiltonian Density of the Dirac Field.

^nd-eq-t8-2

- [ ] Q1 **[state]** Write the three forms.
- [ ] Q2 Pass from the covariant form to the blocks.
- [ ] Q3 Pass from the covariant form to the Hamiltonian form: which matrix multiplies the equation, and what are $\boldsymbol\alpha$, $\beta$?
- [ ] Q4 **[why]** Which form makes covariance manifest, which the role of the mass, which the time evolution?

> [!tip]- Hints: route in the notes
> - Technique: K5
> - [[§C5a.7 The Dirac Equation and Its Lagrangian#^der-c5a-7-10|Derivation §C5a.7.10]]; step 6 of [[§C5a.8 Canonical Structure and Noether Currents of the Dirac Field#^der-c5a-8-2|Derivation §C5a.8.2]].

### Three forms of the Dirac Lagrangian

$\bar\psi(i\slashed\partial - m)\psi$; the real symmetric form $\frac i2(\bar\psi\gamma^\mu\partial_\mu\psi - \partial_\mu\bar\psi\gamma^\mu\psi) - m\bar\psi\psi$; the Weyl form $i\psi_L^\dagger\bar\sigma^\mu\partial_\mu\psi_L + i\psi_R^\dagger\sigma^\mu\partial_\mu\psi_R - m(\psi_L^\dagger\psi_R + \psi_R^\dagger\psi_L)$, see Theorem [[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-7|§C5a.7.7]] The Dirac Lagrangian Is Real up to a Divergence and Theorem [[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-9|§C5a.7.9]] Bilinears in Weyl Components.

^nd-eq-t8-3

- [ ] Q1 **[state]** Write the three forms.
- [ ] Q2 By how much do the first two differ, and why does it not change the field equations?
- [ ] Q3 Derive the Weyl form with $\bar\psi = (\psi_R^\dagger, \psi_L^\dagger)$.
- [ ] Q4 **[why]** Which form is real, and which shows that the mass couples the chiralities?

> [!tip]- Hints: route in the notes
> - Technique: K7
> - Step 6 of [[§C5a.7 The Dirac Equation and Its Lagrangian#^der-c5a-7-7|Derivation §C5a.7.7]]; step 6 of [[§C5a.7 The Dirac Equation and Its Lagrangian#^der-c5a-7-9|Derivation §C5a.7.9]].

### Three routes to u(p)

Boosting the rest-frame solution; checking $(\slashed p - m)u = 0$ directly with the square-root identities (also for $m = 0$); solving the two-component system for the lower half (Yu), see Theorem [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-9|§C5a.9.9]] The Positive-Frequency Spinors u(p) and [[§C5a.9 Plane-Wave Solutions#^der-c5a-9-9b|Derivation §C5a.9.9, second route]].

^nd-eq-t8-4

- [ ] Q1 **[state]** Outline the three routes and the result they share.
- [ ] Q2 Which route needs $m > 0$, and why?
- [ ] Q3 In the third route, express the lower half through the upper with $p\cdot\bar\sigma/m$ and choose the upper half to match the boost form.
- [ ] Q4 **[why]** Why must all routes agree up to the choice of $\xi$ (dimension of the kernel)?

> [!tip]- Hints: route in the notes
> - Technique: K1, K6
> - [[§C5a.9 Plane-Wave Solutions#^der-c5a-9-9|Derivation §C5a.9.9]]; [[§C5a.9 Plane-Wave Solutions#^der-c5a-9-9b|Derivation §C5a.9.9, second route]]; the third route follows [[§C5a.9 Plane-Wave Solutions#^der-c5a-9-9b|Derivation §C5a.9.9, second route]] in [[§C5a.9 Plane-Wave Solutions|§C5a.9]] Plane-Wave Solutions.

### Three routes to ū(p)

Daggering the column and multiplying by $\gamma^0$; daggering the Dirac equation; letting the bar carry the inverse boost, see Theorem [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-10|§C5a.9.10]] The Dirac Conjugate of u(p).

^nd-eq-t8-5

- [ ] Q1 **[state]** Outline the three routes.
- [ ] Q2 In the second route, why does $(\slashed p - m)^\dagger$ combine with $\gamma^0$ into $\gamma^0(\slashed p - m)$?
- [ ] Q3 In the third route, which identity turns $\Lambda_{1/2}^\dagger\gamma^0$ into $\gamma^0\Lambda_{1/2}^{-1}$?
- [ ] Q4 **[why]** Which route works for $m = 0$ and which does not?

> [!tip]- Hints: route in the notes
> - Technique: K7
> - [[§C5a.9 Plane-Wave Solutions#^der-c5a-9-10|Derivation §C5a.9.10]], [[§C5a.9 Plane-Wave Solutions#^der-c5a-9-10b|Derivation §C5a.9.10, second route]], [[§C5a.9 Plane-Wave Solutions#^der-c5a-9-10c|Derivation §C5a.9.10, third route]]; Theorem [[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-18-13|§CB.18.13]] Λ½ Is Pseudo-Unitary.

### The spinor boost in three forms

$e^{-i\eta S^{03}}$; $\operatorname{diag}(\cosh\frac\eta2 - \sinh\frac\eta2\sigma^3, \cosh\frac\eta2 + \sinh\frac\eta2\sigma^3)$; $\operatorname{diag}(\sqrt{p\cdot\sigma/m}, \sqrt{p\cdot\bar\sigma/m})$ for the boost from rest to $p$, see Theorem [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-5|§C5a.9.5]] The Spinor Boost along z and Theorem [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-8|§C5a.9.8]] The Spinor Boost from Rest to Momentum p.

^nd-eq-t8-6

- [ ] Q1 **[state]** Write the three forms for a boost along $z$.
- [ ] Q2 Pass from the exponential to the half-rapidity form.
- [ ] Q3 Pass to the square-root form using $\cosh\eta = E/m$, $\sinh\eta = \lvert\mathbf p\rvert/m$.
- [ ] Q4 **[why]** Why does the spinor see half the rapidity while the momentum sees the full one?

> [!tip]- Hints: route in the notes
> - Technique: K4
> - [[§C5a.9 Plane-Wave Solutions#^der-c5a-9-5|Derivation §C5a.9.5]]; [[§C5a.9 Plane-Wave Solutions#^der-c5a-9-8|Derivation §C5a.9.8]]; [[§C5a.9 Plane-Wave Solutions#^rem-c5a-9-4|§C5a.9, Remark: Why a square root restores the full rapidity]].

### Four forms of γ⁵

$\gamma^5 = i\gamma^0\gamma^1\gamma^2\gamma^3$; in the chiral basis $\operatorname{diag}(-\mathbb 1, \mathbb 1)$; $-\frac i{24}\varepsilon_{\kappa\lambda\mu\nu}\gamma^\kappa\gamma^\lambda\gamma^\mu\gamma^\nu$; on the Dirac representation $\frac43(\mathbf J_-^2 - \mathbf J_+^2)$, see Definition [[§CB.12 Clifford Algebras꞉ Grading, Basis and the Volume Element#^def-cb-12-14|§CB.12.14]] The Matrix γ⁵, Theorem [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-1|§C5a.5.1]] γ⁵ Is Lorentz Invariant and Separates the Weyl Halves and Theorem [[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-5|§C5a.11.5]] γ⁵ as a Totally Antisymmetric Product.

^nd-eq-t8-7

- [ ] Q1 **[state]** Write the four forms.
- [ ] Q2 From the definition, compute the chiral-basis form.
- [ ] Q3 Relate $\mathbf J\cdot\mathbf K$ to $\gamma^5$ and then to $\mathbf J_\pm^2$.
- [ ] Q4 **[conv]** In the $\varepsilon$ form, which sign of $\varepsilon^{0123}$ is assumed? (The proof is [[PHY 513 PS Drill#^ps5-5-c|PS5.5(c)]].)

> [!tip]- Hints: route in the notes
> - Technique: K5, K16
> - Steps 1–2 of [[§C5a.5 Chirality and Weyl Spinors#^der-c5a-5-1|Derivation §C5a.5.1]]; Theorem [[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-5|§C5a.11.5]] γ⁵ as a Totally Antisymmetric Product; ε convention: [[§C5a.11 Gamma-Matrix Technology#^cau-c5a-11-1|§C5a.11, Caution: The sign of the ε trace across sources]].

### Spin sums blockwise and by covariance

$\sum_su^s\bar u^s = \slashed p + m$ computed in blocks at general $p$, or at rest ($m(\gamma^0 + 1)$) and then boosted with $\Lambda_{1/2}\slashed p\Lambda_{1/2}^{-1} = \slashed{(\Lambda p)}$, see Theorem [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-7|§C5a.10.7]] The Spin Sum over u and Theorem [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-9|§C5a.10.9]] The Spin Sums Are Covariant.

^nd-eq-t8-8

- [ ] Q1 **[state]** State the spin sum and the covariance statement.
- [ ] Q2 Compute the sum at rest.
- [ ] Q3 Boost it: why is $\sum(\Lambda_{1/2}u)\overline{(\Lambda_{1/2}u)} = \Lambda_{1/2}(\sum u\bar u)\Lambda_{1/2}^{-1}$?
- [ ] Q4 **[why]** Why does the result not depend on the spin basis in either route?

> [!tip]- Hints: route in the notes
> - Technique: K1, K14
> - [[§C5a.10 Normalization, Spin Sums and Helicity#^der-c5a-10-7|Derivation §C5a.10.7]]; [[§C5a.10 Normalization, Spin Sums and Helicity#^der-c5a-10-9|Derivation §C5a.10.9]].

### Chirality three ways

The left-handed half of a Dirac spinor is the $\gamma^5 = -1$ eigenspace, the $(\frac12, 0)$ piece of the Dirac representation, and $P_L\psi = (\psi_L, 0)$ in the chiral basis, see Theorem [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-1|§C5a.5.1]] γ⁵ Is Lorentz Invariant and Separates the Weyl Halves, Theorem [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-2|§C5a.3.2]] The Dirac Representation Is (½, 0) ⊕ (0, ½) and Definition [[§C5a.5 Chirality and Weyl Spinors#^def-c5a-5-1|§C5a.5.1]] Chirality Projectors.

^nd-eq-t8-9

- [ ] Q1 **[state]** State the three descriptions of the left-handed half.
- [ ] Q2 Why is the $\gamma^5$ eigenspace invariant under $\Lambda_{1/2}$?
- [ ] Q3 Why does it carry $(\frac12, 0)$ in every basis, not only the chiral one?
- [ ] Q4 **[why]** Which of the three descriptions is basis-free, and which is a statement about components?

> [!tip]- Hints: route in the notes
> - Technique: K16, K7
> - Step 3 of [[§C5a.5 Chirality and Weyl Spinors#^der-c5a-5-1|Derivation §C5a.5.1]]; Theorem [[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-18-4|§CB.18.4]] γ⁵ Commutes with the Spinor Generators and Splits the Dirac Module; [[§C5a.3 The Lorentz Action on Spinor Space#^der-c5a-3-2|Derivation §C5a.3.2]].

### Orthogonality of u and v two ways

$u^{r\dagger}(p)v^s(\tilde p) = 0$ by the square-root identities, and as eigenvectors of the Hermitian $H_{\text{s.p.}}(\mathbf p)$ with eigenvalues $+E$ and $-E$, see Theorem [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-6|§C5a.10.6]] u and v Are Orthogonal at Opposite Three-Momenta.

^nd-eq-t8-10

- [ ] Q1 **[state]** State the relation and the two routes.
- [ ] Q2 Write $u(p)e^{-ip\cdot x}$ and $v(\tilde p)e^{+i\tilde p\cdot x}$ with the same spatial factor $e^{i\mathbf p\cdot\mathbf x}$. Which eigenvalues of $H_{\text{s.p.}}(\mathbf p)$ do they have?
- [ ] Q3 **[why]** Why are eigenvectors of a Hermitian matrix with different eigenvalues orthogonal, and why does this need $\tilde p$ rather than $p$?

> [!tip]- Hints: route in the notes
> - Technique: K10
> - [[§C5a.10 Normalization, Spin Sums and Helicity#^der-c5a-10-6|Derivation §C5a.10.6]]; [[§C5a.10 Normalization, Spin Sums and Helicity#^der-c5a-10-6b|Derivation §C5a.10.6, second route]].

### Momentum form and field form of the canonical relations

$\{\hat\psi_a, \hat\pi_b\} = i\delta_{ab}\delta^3$ with $\{\hat\pi, \hat\pi\} = 0$ is the same postulate as $\{\hat\psi_a, \hat\psi^\dagger_b\} = \delta_{ab}\delta^3$ with $\{\hat\psi^\dagger, \hat\psi^\dagger\} = 0$, see Theorem [[§C5b.1 Canonical Quantization of the Dirac Field#^thm-c5b-1-1|§C5b.1.1]] The Conjugate Momentum Field of the Dirac Field. *Source: Lecture 10 (Oct 5), slide 5*

^nd-eq-9-1

- [ ] Q1 **[state]** State both forms.
- [ ] Q2 Insert $\hat\pi = i\hat\psi^\dagger$: why may $i$ be pulled out of the anticommutator, and what happens to $i^2$ in the momentum–momentum relation?
- [ ] Q3 **[why]** Does the same equivalence hold with commutators?

> [!tip]- Hints: route in the notes
> - Technique: K11.
> - Steps 4–5 under Theorem [[§C5b.1 Canonical Quantization of the Dirac Field#^thm-c5b-1-1|§C5b.1.1]] The Conjugate Momentum Field of the Dirac Field.

### ψ† or ψ̄ as the partner field: one canonical structure

Varying $\psi$ and $\psi^\dagger$ (slide 5) or $\psi$ and $\bar\psi$ gives the same momentum of $\psi$, related partner momenta and the same bracket, see [[§C5b.1 Canonical Quantization of the Dirac Field#^rem-c5b-1-2|§C5b.1, Remark: ψ† or ψ̄ as the partner field, one canonical structure]]. *Source: Lecture 10 (Oct 5), slide 5 · the user's notes Ch. 10 §10.1*

^nd-eq-9-2

- [ ] Q1 **[state]** How are $\bar\psi$ and $\psi^\dagger$ related, and why is the change invertible?
- [ ] Q2 Why is $\partial\mathcal L/\partial\dot\psi$ the same in both choices?
- [ ] Q3 How are $\pi_{\bar\psi}$ and $\pi_{\psi^\dagger}$ related by the chain rule?
- [ ] Q4 **[why]** In what sense is "treat them as independent" right for varying the action but not for counting canonical coordinates?

> [!tip]- Hints: route in the notes
> - Technique: K2.
> - The remark's three bullets; Euler–Lagrange for complex fields Theorem [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-9|§C1b.2.9]] Field and Conjugate as Independent Variables.

### Field form of Ĥ equals its mode form, by two routes

$\int d^3x\,\hat\psi^\dagger H_{\rm s.p.}\hat\psi = \sum_s\int\frac{d^3p}{(2\pi)^3}E_{\mathbf p}(\hat a^\dagger\hat a - \hat b\hat b^\dagger)$, computed at general $t$ (exponentials split) or at $t = 0$ with flipped momenta (Lecture 10), see Theorem [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-2|§C5b.3.2]] The Hamiltonian in Modes, before Any Algebra. *Source: Lecture 10 (Oct 5), slides 18–19*

^nd-eq-9-3

- [ ] Q1 **[state]** State both sides.
- [ ] Q2 General-$t$ route: why do the time phases cancel in the surviving terms and why do the number-changing terms vanish anyway?
- [ ] Q3 $t = 0$ route: what replaces the time-phase argument?
- [ ] Q4 **[why]** Why is it legitimate to compute a time-independent operator at one time only?

> [!tip]- Hints: route in the notes
> - Technique: K9, K10.
> - First and second derivations under Theorem [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-2|§C5b.3.2]] The Hamiltonian in Modes, before Any Algebra.

### The Dirac Feynman propagator three ways

$S_F = \langle0|T\{\hat\psi\hat{\bar\psi}\}|0\rangle = \theta S^+_W - \theta S^-_W = \int\frac{d^4p}{(2\pi)^4}\frac{i(\slashed p + m)}{p^2 - m^2 + i\varepsilon}e^{-ip\cdot\xi} = (i\slashed\partial + m)D_F$, see Theorem [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-3|§C5b.8.3]] The Dirac Feynman Propagator. *Source: PS §3.5, eq. (3.121)*

^nd-eq-9-4

- [ ] Q1 **[state]** Write the four forms.
- [ ] Q2 Contour route: which closing gives which time ordering?
- [ ] Q3 Scalar route: apply $i\slashed\partial + m$ to $D_F = \theta D_W(\xi) + \theta D_W(-\xi)$; what happens to the term with $\partial_0\theta$?
- [ ] Q4 **[why]** Why does this contact term vanish ($D_W(\xi) - D_W(-\xi)$ at $\xi^0 = 0$)?

> [!tip]- Hints: route in the notes
> - Technique: K13.
> - Second route steps 1–4 under Theorem [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-3|§C5b.8.3]] The Dirac Feynman Propagator; $D_W(\xi) - D_W(-\xi) = iD(\xi)$, Theorem [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-2|§C2b.4.2]] The Field Commutator Is a c-Number.

### Spin–statistics: two arguments, one answer

PS reach anticommutators from causality (the two orderings must cancel outside the cone) and from positivity of the energy; both exclude commutators, see [[§C5b.9 Spin and Statistics#^rem-c5b-9-1|§C5b.9, Remark: Two arguments, one answer]]. *Source: Lecture 10 (Oct 5), slide 6 · PS §3.5*

^nd-eq-9-5

- [ ] Q1 **[state]** State the two arguments in one sentence each.
- [ ] Q2 Which theorem of the notes is each?
- [ ] Q3 **[why]** Why is it significant that two independent requirements give the same answer?

> [!tip]- Hints: route in the notes
> - Theorem [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-3|§C5b.3.3]] Commutators Allow No Positive Norm with Positive Energy (positivity), Theorem [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-5|§C5b.7.5]] A Dirac Field with Commutators Is Not Causal (causality), Theorem [[§C5b.9 Spin and Statistics#^thm-c5b-9-1|§C5b.9.1]] The Free Fields of the Course Obey the Spin–Statistics Theorem.

### Charge conjugation through the transposed adjoint and through the transposed ψ̄

$-i\gamma^2\hat\psi^{\dagger\mathsf T} = (-i\hat{\bar\psi}\gamma^0\gamma^2)^{\mathsf T}$: the course's law and the form of Problem Set 6 and PS (3.145) are the same, see Theorem [[§C9.6 Charge Conjugation on the Field and Bilinears#^thm-c9-6-3|§C9.6.3]] Charge Conjugation through the Dirac Conjugate. *Source: Lecture 12 (Oct 12), slide 10 · Problem Set 6, conventions · PS eq. (3.145)*

^nd-eq-10-1

- [ ] Q1 **[state]** Write both forms.
- [ ] Q2 Use that $\gamma^2$ is symmetric to move the transpose: $-i\gamma^2(\hat\psi^\dagger)^{\mathsf T} = (\,?\,)^{\mathsf T}$.
- [ ] Q3 Bring in $\hat{\bar\psi} = \hat\psi^\dagger\gamma^0$: which $\gamma^0$ had been dropped on the board, and why is it needed?
- [ ] Q4 Derive the laws for $\hat\psi^\dagger$ and $\hat{\bar\psi}$ from the field law. Which symmetry of $\gamma^0$ is used?
- [ ] Q5 **[why]** Which form is convenient for bilinears, and why?

> [!tip]- Hints: route in the notes
> - Technique: K7.
> - Steps 1–3 under Theorem [[§C9.6 Charge Conjugation on the Field and Bilinears#^thm-c9-6-3|§C9.6.3]] Charge Conjugation through the Dirac Conjugate, 1–3 under Theorem [[§C9.6 Charge Conjugation on the Field and Bilinears#^thm-c9-6-4|§C9.6.4]] Charge Conjugation on ψ† and ψ̄; [[§C9.6 Charge Conjugation on the Field and Bilinears#^rem-c9-6-3|§C9.6, Remark: The missing γ⁰]].

### The basis-free B form and the chiral −iγ² form of C

$U(\mathcal C)\hat\psi U(\mathcal C)^{-1} = B\hat\psi^{\dagger\mathsf T}$ (any Hermitian basis, condition $v = Bu^{\ast}$) reduces to $-i\gamma^2\hat\psi^{\dagger\mathsf T}$ (condition $\eta^s = \xi^{-s}$) in the chiral basis, see Theorem [[§C9.6 Charge Conjugation on the Field and Bilinears#^thm-c9-6-1|§C9.6.1]] Charge Conjugation on the Dirac Field in Any Basis and Theorem [[§C9.6 Charge Conjugation on the Field and Bilinears#^thm-c9-6-2|§C9.6.2]] Charge Conjugation on the Dirac Field. *Source: Lecture 12 (Oct 12), slide 9; the basis-free form written at the user's question*

^nd-eq-10-2

- [ ] Q1 **[state]** State both laws with their conditions.
- [ ] Q2 Show that $B = -i\gamma^2$ satisfies $B(\gamma^\mu)^{\ast}B^{-1} = -\gamma^\mu$ in the chiral basis.
- [ ] Q3 Show that $v^s = -i\gamma^2u^{s\ast}$ is exactly $\eta^s = \xi^{-s}$.
- [ ] Q4 **[why]** Under a change of basis $M$, how do $B$, $u$, $v$ transform so that the law keeps its form? What is $B$ in the Dirac basis (same $\gamma^i$)?

> [!tip]- Hints: route in the notes
> - Technique: K16.
> - Steps 2–3 under Theorem [[§C9.6 Charge Conjugation on the Field and Bilinears#^thm-c9-6-1|§C9.6.1]] Charge Conjugation on the Dirac Field in Any Basis; Theorem [[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-18-19|§CB.18.19]] Existence and Uniqueness of the Charge-Conjugation Matrix, and Its Square under Conjugation, part 4; Example [[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^ex-cb-18-22|§CB.18.22]] The Charge-Conjugation Matrix in Three Bases, and the Transpose Form; [[§C9.5 Charge Conjugation on Oscillators and Spinors#^cau-c9-5-4|§C9.5, Caution: −iγ² is a statement about the chiral basis]].

### Θ in two orders

$U(\mathcal C)U(\mathcal P)U(\mathcal T)$ gives $\eta_a\gamma^5\hat\psi^{\dagger\mathsf T}(-x)$ and $U(\mathcal T)U(\mathcal P)U(\mathcal C)$ gives $-\eta_a\gamma^5\hat\psi^{\dagger\mathsf T}(-x)$: the same up to a phase, see Theorem [[§C9.9 CPT and the CPT Theorem#^thm-c9-9-3|§C9.9.3]] CPT on the Dirac Field and Theorem [[§C9.9 CPT and the CPT Theorem#^thm-c9-9-4|§C9.9.4]] CPT in Another Order. *Source: Lecture 12 (Oct 12), slide 24 ("any order will do") · Problem Set 7, Problem 3*

^nd-eq-10-3

- [ ] Q1 **[state]** State both results.
- [ ] Q2 In which order do the matrices $\gamma^1\gamma^3$, $\gamma^0$, $-i\gamma^2$ appear in each computation, and where is a complex conjugation applied?
- [ ] Q3 Reduce each product to $\pm\gamma^5$.
- [ ] Q4 **[why]** Why is a sign difference physically irrelevant here?

> [!tip]- Hints: route in the notes
> - Technique: K5, K15.
> - Steps 1–4 under Theorem [[§C9.9 CPT and the CPT Theorem#^thm-c9-9-3|§C9.9.3]] CPT on the Dirac Field; steps 1–4 under Theorem [[§C9.9 CPT and the CPT Theorem#^thm-c9-9-4|§C9.9.4]] CPT in Another Order; Theorem [[§C9.9 CPT and the CPT Theorem#^thm-c9-9-1|§C9.9.1]] The Three Matrices Multiply to γ⁵.

### The laws on ψ̄ from the laws on ψ, for P, C and T

$U(\mathcal P)\hat{\bar\psi}U(\mathcal P)^{-1} = \eta_a^{\ast}\hat{\bar\psi}(\tilde x)\gamma^0$, $U(\mathcal C)\hat{\bar\psi}U(\mathcal C)^{-1} = (-i\gamma^0\gamma^2\hat\psi)^{\mathsf T}$, $U(\mathcal T)\hat{\bar\psi}U(\mathcal T)^{-1} = \hat{\bar\psi}(x_T)\gamma^3\gamma^1$: each by "take the adjoint, right-multiply by $\gamma^0$", see Theorem [[§C9.4 Fermion Bilinears under Parity#^thm-c9-4-1|§C9.4.1]] Parity on the Dirac Conjugate Field, Theorem [[§C9.6 Charge Conjugation on the Field and Bilinears#^thm-c9-6-4|§C9.6.4]] Charge Conjugation on ψ† and ψ̄, Theorem [[§C9.8 Time Reversal#^thm-c9-8-8|§C9.8.8]] Time Reversal on the Dirac Conjugate Field. *Source: Lecture 11 (Oct 7), slide 21 · Lecture 12 (Oct 12), slides 10, 22*

^nd-eq-10-4

- [ ] Q1 **[state]** State the three laws.
- [ ] Q2 Why does conjugation commute with the adjoint for unitary and for antiunitary operators?
- [ ] Q3 In each case, what happens to the c-number matrix when it is moved past $\gamma^0$ (and, for $T$, conjugated)?
- [ ] Q4 **[why]** Why does only the $C$ law turn $\hat{\bar\psi}$ into a transposed $\hat\psi$?

> [!tip]- Hints: route in the notes
> - Technique: K7.
> - Derivations under Theorem [[§C9.4 Fermion Bilinears under Parity#^thm-c9-4-1|§C9.4.1]] Parity on the Dirac Conjugate Field, Theorem [[§C9.6 Charge Conjugation on the Field and Bilinears#^thm-c9-6-4|§C9.6.4]] Charge Conjugation on ψ† and ψ̄, Theorem [[§C9.8 Time Reversal#^thm-c9-8-8|§C9.8.8]] Time Reversal on the Dirac Conjugate Field.

### The axial vector under CPT: step by step and from the table

Slide 25's three steps and the product of the $C$, $P$, $T$ columns of the table both give $\Theta\mathsf A^\mu(x)\Theta^{-1} = -\mathsf A^\mu(-x)$, see Example [[§C9.9 CPT and the CPT Theorem#^ex-c9-9-1|§C9.9.1]] The Axial Vector under CPT and Theorem [[§C9.9 CPT and the CPT Theorem#^thm-c9-9-5|§C9.9.5]] The Bilinears under C, P, T and CPT. *Source: Lecture 12 (Oct 12), slide 25*

^nd-eq-10-5

- [ ] Q1 **[state]** State the result.
- [ ] Q2 Multiply the signs of the $\mathsf A^\mu$ row and contract the two $\mathcal P$'s.
- [ ] Q3 Do the same directly from $\Theta\hat\psi\Theta^{-1} = \eta_a\gamma^5\hat\psi^{\dagger\mathsf T}(-x)$: how many indices, which sign?
- [ ] Q4 **[why]** Why must both routes agree whatever order of $C$, $P$, $T$ is used for bilinears?

> [!tip]- Hints: route in the notes
> - Technique: K15.
> - Example [[§C9.9 CPT and the CPT Theorem#^ex-c9-9-1|§C9.9.1]] The Axial Vector under CPT; steps 4–5 under Theorem [[§C9.9 CPT and the CPT Theorem#^thm-c9-9-5|§C9.9.5]] The Bilinears under C, P, T and CPT.

### The complex scalar and the Dirac field side by side

The discrete laws of the two fields match line by line: the same operations on modes, and the Dirac matrices $\gamma^0$, $-i\gamma^2$, $\gamma^1\gamma^3$, $\gamma^5$ come only from rewriting spinors; the phase conditions differ in sign ($\eta_a\eta_b = +1$ vs $-1$) and $U(\mathcal T)^2$ is $+1$ vs $(-1)^{\hat N_a + \hat N_b}$, see [[§C9.10 C, T and CPT for the Complex Scalar Field#^rem-c9-10-2|§C9.10, Remark: The complex scalar and the Dirac field side by side]] and [[§C9.2 Parity of the Scalar Field#^rem-c9-2-8|§C9.2, Remark: Scalar and spinor parity side by side]]. *Source: the user's notes Ch. 11–12 · Problem Set 7, Problem 4*

^nd-eq-10-6

- [ ] Q1 **[state]** For $C$, $P$, $T$ and $CPT$, write the scalar law and the Dirac law next to each other.
- [ ] Q2 Which single input changes the pair's intrinsic parity from $+1$ to $-1$?
- [ ] Q3 Which single input changes $U(\mathcal T)^2$ from $+1$ to $(-1)^{\hat N_a + \hat N_b}$?
- [ ] Q4 **[why]** Why do the currents $\hat j^\mu$ and $\mathsf V^\mu$ have the same signs under all four?

> [!tip]- Hints: route in the notes
> - The two tables; Theorem [[§C9.3 Parity on States, Spinors and the Dirac Field#^thm-c9-3-4|§C9.3.4]] Parity on the Negative-Frequency Spinors; Theorem [[§C9.8 Time Reversal#^thm-c9-8-16|§C9.8.16]] Time Reversal Twice Is −1 on Fermions; Theorem [[§C9.10 C, T and CPT for the Complex Scalar Field#^thm-c9-10-4|§C9.10.4]] The U(1) Current under P, C and T.
