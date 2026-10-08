---
type: summary
subject: "[[Differentiable Manifolds]]"
tags: [differentiable-manifolds, math591]
---
↑ [[Differentiable Manifolds]]

# Concordance with Lee

These notes follow the course, and Lee's *Introduction to Smooth Manifolds* (2nd ed.) is the course text. The two cover the same mathematics by different routes. The course is more algebraic — germs, derivations of germs, the ideal $I_p$ — and it builds tangent spaces from the geometric picture towards the abstract one, where Lee starts abstract. This appendix is for reading the two side by side. It records where the notation differs, where the routes diverge, which parts of Lee each section corresponds to, and, for every result of Lee's cited in these notes, where its counterpart is. Throughout the notes, the line *Lee:* at the foot of a box gives the same information locally.

## A.1 Notation

| These notes | Lee | Remark |
|---|---|---|
| $T_pM$: derivations of germs $C_p^\infty(M)$ | $T_pM$: derivations of $C^\infty(M)$ at $p$ | Isomorphic, by Proposition [[§28 Derivations and the Abstract Tangent Space#^prop-28-3\|§28.3]]; Lee's version needs bump functions. |
| $T^{\mathrm{geo}}_pM$, the geometric tangent space | $\mathbb{R}^n_a$ in $\mathbb{R}^n$; $T_pS \subseteq T_pM$ for embedded $S$ | Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6\|§29.6]]; Lee, Propositions 3.2 and 5.38. |
| $F_{*p}$ | $dF_p$ | The notes keep $dF_p$ for the vector-space differential (Definition [[§22 The Differential of a Map Between Vector Spaces#^def-22-5\|§22.5]]) and $df_p$ for functions. |
| $D_\gamma$, the velocity | $\gamma'(0)$ | The notes keep $\gamma'(0)$ for the ordinary derivative of a curve in $\mathbb{R}^N$, a geometric vector (Definition [[§31 Tangent Vectors as Velocities of Curves#^def-31-2\|§31.2]]). |
| $D_v$, $D_v\vert_a$ | $D_v\vert_a$ | The directional derivative (Definition [[§25 The Geometric Tangent Space#^def-25-4\|§25.4]]). |
| $[f] \in C_p^\infty(M)$, germs | — | Lee works with global functions $C^\infty(M)$ (Definition [[§27 Germs#^def-27-2\|§27.2]]). |
| $f_\varphi = f \circ \varphi^{-1}$, $\tilde F = \psi \circ F \circ \varphi^{-1}$ | $\hat f$, $\widehat F$ | Coordinate representations (Definition [[§29 Coordinate Derivations and the Basis Theorem#^def-29-1\|§29.1]]). |
| $\sum_i a^i\, \partial/\partial x^i\vert_p$ | $a^i\, \partial/\partial x^i\vert_p$ | Lee uses the Einstein summation convention; the notes always write the sum. |
| $T_p^*M$, $df_p$, $dx^i\vert_p$ | the same | Definition [[§32 The Cotangent Space#^def-32-1\|§32.1]], Lemma [[§32 The Cotangent Space#^lem-32-2\|§32.2]]. |
| $I_p$, $I_p^2$, $I_p/I_p^2$, of germs | $I_p$, $I_p^2$ of global functions (Problem 11-4) | Theorem [[§32 The Cotangent Space#^thm-32-8\|§32.8]]; Lee's version needs bump functions. |
| $\Gamma = \{(x, g \cdot x)\}$, the orbit relation | $\mathcal{O} = \{(g \cdot p, p)\}$ | The same set with the factors swapped (proof of Lee, Proposition 21.4). |
| $H_{x_0}$, the isotropy group | $G_p$ | Definition [[§14 Homogeneous Spaces#^def-14-3\|§14.3]]. |
| $\Phi : G/H \to X$, $gH \mapsto g \cdot x_0$ | $F : G/G_p \to M$ | Theorem [[§15 The Topology of G∕H and Real Grassmannians#^thm-15-3\|§15.3]]; Lee, Theorem 21.18. |
| $\mathfrak{g} = T^{\mathrm{geo}}_I G$ | $\mathrm{Lie}(G) \cong T_eG$ | The notes' $\mathfrak{g}$ is the geometric tangent space at $I$; Lee defines $\mathrm{Lie}(G)$ by left-invariant vector fields (Chapter 8). |
| $\widetilde{\mathbb{R}}$: the chart $\sqrt[3]{x}$ | Example 1.23: the chart $x^3$ | Two different non-standard structures — the transition map between them is $y \mapsto y^9$ — both diffeomorphic to $\mathbb{R}$ (Corollary [[§19 Smooth Functions and Smooth Maps#^cor-19-7\|§19.7]]). |

## A.2 Where the routes diverge

Each row is expanded in a **Comparison with Lee** paragraph at the place indicated.

| Topic | These notes | Lee |
|---|---|---|
| Hausdorff quotients | One criterion for all open quotients (Theorems [[§6 Open Quotients#^thm-6-1\|§6.1]] and [[§6 Open Quotients#^thm-6-3\|§6.3]]), reused for orbit and coset spaces | Checked example by example (Example 1.5, Problem 1-9) |
| Regular level sets | Implicit function theorem, topological first (Theorem [[§7 The Regular Value Theorem#^thm-7-3\|§7.3]]), smooth afterwards (Proposition [[§20 Manifolds in Euclidean Space#^prop-20-2\|§20.2]]) | Example 1.32 for one function; Corollary 5.14 via the constant-rank theorem |
| Hausdorff orbit spaces | Compact group on a Hausdorff space, purely topological (Theorem [[§13 Group Actions and Orbit Spaces#^thm-13-5\|§13.5]]) | Proper actions of Lie groups (Proposition 21.4, Corollary 21.6) |
| Homogeneous spaces | $G/H$ compact and $X$ Hausdorff (Theorem [[§15 The Topology of G∕H and Real Grassmannians#^thm-15-3\|§15.3]]); the hypothesis is needed (Example [[§15 The Topology of G∕H and Real Grassmannians#^ex-15-2\|§15.2]]) | Smooth version, no compactness (Theorem 21.18) |
| Tangent vectors | Derivations of germs; locality is built in, and no bump functions are needed | Derivations of $C^\infty(M)$; locality from bump functions (Proposition 3.8) |
| Order of ideas | Geometric first, $T^{\mathrm{geo}}_pM = \ker F'(p)$ (Theorem [[§25 The Geometric Tangent Space#^thm-25-3\|§25.3]]), then derivations | Derivations first; $T_pS = \ker d\Phi_p$ later (Proposition 5.38) |
| Cotangent space | The dual, and also $I_p/I_p^2$ of germs, via a non-degenerate pairing (Theorem [[§32 The Cotangent Space#^thm-32-8\|§32.8]]) | The dual in the text (Chapter 11); $I_p/I_p^2$ of global functions, via $f \mapsto df_p$, as Problem 11-4 |
| Transversality | Level sets in Euclidean space (Theorem [[§26 Transversality#^thm-26-1\|§26.1]]) | Embedded submanifolds (Theorem 6.30) |
| Linear algebra | The toolkit of [[§21 Linear Algebra Toolkit\|§21]], including the pairing theorem (Theorem [[§21 Linear Algebra Toolkit#^thm-21-5\|§21.5]]) | Appendix B; dual spaces in Chapter 11 |

## A.3 Chapter map

| These notes | Lee |
|---|---|
| [[§1 Point-Set Topology Review\|§1]] Point-set review | Appendix A, *Topological Spaces* and *Connectedness and Compactness* |
| [[§2 Topological Manifolds\|§2]] Topological manifolds | Chapter 1, *Topological Manifolds*; Problems 1-1 and 1-2 |
| [[§3 Subspaces and Products\|§3]]–[[§6 Open Quotients\|§6]] Subspaces, products, quotients | Appendix A, *Subspaces, Products, Disjoint Unions, and Quotients*; Problem 1-9 |
| [[§7 The Regular Value Theorem\|§7]] Regular value theorem | Appendix C (Theorem C.40); Example 1.32; Corollary 5.14 |
| [[§11 Topological Groups and Classical Matrix Groups\|§11]] Topological and matrix groups | Chapter 7, Examples 7.27–7.30; Propositions 21.34 and 21.35; Problem 7-4 |
| [[§13 Group Actions and Orbit Spaces\|§13]] Actions and orbit spaces | Chapter 7, *Group Actions and Equivariant Maps*; Lemma 21.1, Proposition 21.4 |
| [[§14 Homogeneous Spaces\|§14]] Homogeneous spaces | Theorems 21.17–21.20; Examples 1.36 and 21.21 |
| [[§17 Differentiable Structures\|§17]] Differentiable structures | Chapter 1, *Smooth Structures*, Examples 1.22–1.34; Chapter 2 |
| [[§20 Manifolds in Euclidean Space\|§20]] Manifolds in Euclidean space | Example 1.32; Chapter 5 |
| [[§21 Linear Algebra Toolkit\|§21]] Vector spaces and matrix groups | Appendix B; Chapter 11 (dual spaces); Example 1.24; Examples 7.27 and 7.29 |
| [[§25 The Geometric Tangent Space\|§25]] The geometric tangent space | Propositions 3.2, 5.37 and 5.38; Theorem 6.30 |
| [[§27 Germs\|§27]]–[[§31 Tangent Vectors as Velocities of Curves\|§31]] Germs, derivations, the abstract tangent space | Chapter 3 throughout, including Proposition 3.14 (products) |
| [[§32 The Cotangent Space\|§32]] The cotangent space | Chapter 11, *Covectors*; Problem 11-4 for $I_p/I_p^2$ |
| [[§33 Local Diffeomorphisms\|§33]]–[[§34 Submersions\|§34]] Local diffeomorphisms, submersions | Chapter 4 (Propositions 4.1 and 4.28, Theorem 4.12); Theorem C.34 |
| [[§35 Submanifolds\|§35]] Submanifolds | Chapter 5, *Embedded Submanifolds* (Theorem 5.8, Corollary 5.14, Propositions 5.35–5.38) |
| [[§36 Fibrations\|§36]] Fibrations | smooth fiber bundles (Chapter 10); Chapter 10 (sections); Ehresmann's theorem is not in Lee |
| [[§37 Immersions\|§37]] Immersions | Chapter 4, *Immersions* (Theorem 4.12); Example 4.19 |
| [[§38 Embeddings\|§38]] Embeddings | Chapter 4, *Embeddings* (Proposition 4.22, Example 4.20); Proposition 5.2; Theorem A.57; Proposition 1.12 |
| [[§40 The Unit Quaternions and SU(2)\|§40]]–[[§41 SU(2) → SO(3)꞉ The Double Cover\|§41]] The unit quaternions and the double cover $\mathrm{SU}(2) \to \mathrm{SO}(3)$ | Problems 7-22 and 7-23 (quaternions); Examples 7.27–7.30 (matrix groups) |
| [[§42 Recap꞉ Germs, Derivations and Tangent Vectors\|§42]]–[[§43 Recap꞉ Covectors and the Four Differentials\|§43]] Recaps: tangent vectors, covectors | Chapters 3 and 11 (overview) |
| [[§44 The Tangent Bundle\|§44]] The tangent bundle | Chapter 3, *The Tangent Bundle* (Lemma 1.35, Proposition 3.18) |
| [[§45 The Cotangent Bundle\|§45]] The cotangent bundle | Chapter 11, *The Cotangent Bundle* (Proposition 11.9); Lemma 1.35 |
| [[§46 One-Forms\|§46]] One-forms, the operator $d$, pullbacks | Chapter 11, *Covector Fields* (Propositions 11.11 and 11.25, Example 11.36, Corollary 11.50) |
| [[§47 Vector Fields\|§47]] Vector fields | Chapter 8 (Propositions 8.1 and 8.15); Proposition 2.25 and Lemma 2.26 (bump functions, extension) |
| [[§48 Lie Bracket and Lie Algebra\|§48]] Lie bracket and Lie algebra | Chapter 8, *Lie Brackets* and *Lie Algebras* (Lemma 8.25, Propositions 8.26 and 8.28) |
| [[§49 Lie Groups and Left-Invariant Vector Fields\|§49]] Lie groups and left-invariant vector fields | Chapter 7 (Examples 7.3, 7.27–7.30); Chapter 8, *Lie Algebras* |

## A.4 Index from Lee to these notes

Every numbered result of Lee's cited in these notes, in Lee's order, with the boxes that correspond to it. The table is generated from the *Lee:* lines in the boxes, so the two always agree.

| Lee | These notes |
|---|---|
| Theorem 1.2 | [[§2 Topological Manifolds#^thm-2-1\|Thm. §2.1]], [[§2 Topological Manifolds#^cor-2-2\|Cor. §2.2]] |
| Example 1.4 | [[§8 Spheres#^ex-8-1\|Ex. §8.1]], [[§8 Spheres#^prop-8-1\|Prop. §8.1]], [[§17 Differentiable Structures#^ex-17-2\|Ex. §17.2]] |
| Example 1.5 | [[§18 Projective Spaces as Smooth Manifolds#^prop-18-6\|Prop. §18.6]] |
| Example 1.8 | [[§3 Subspaces and Products#^thm-3-12\|Thm. §3.12]] |
| Proposition 1.11 | [[§2 Topological Manifolds#^prop-2-6\|Prop. §2.6]], [[§2 Topological Manifolds#^thm-2-8\|Thm. §2.8]], [[§2 Topological Manifolds#^cor-2-9\|Cor. §2.9]] |
| Proposition 1.12 | [[§2 Topological Manifolds#^prop-2-12\|Prop. §2.12]] |
| Proposition 1.17 | [[§17 Differentiable Structures#^def-17-7\|Def. §17.7]], [[§17 Differentiable Structures#^thm-17-5\|Thm. §17.5]] |
| Example 1.21 | [[§2 Topological Manifolds#^prop-2-5\|Prop. §2.5]] |
| Example 1.22 | [[§17 Differentiable Structures#^ex-17-1\|Ex. §17.1]] |
| Example 1.23 | [[§19 Smooth Functions and Smooth Maps#^ex-19-1\|Ex. §19.1]], [[§19 Smooth Functions and Smooth Maps#^cor-19-7\|Cor. §19.7]], [[§19 Smooth Functions and Smooth Maps#^ex-19-2\|Ex. §19.2]] |
| Example 1.24 | [[§22 The Differential of a Map Between Vector Spaces#^def-22-1\|Def. §22.1]], [[§22 The Differential of a Map Between Vector Spaces#^def-22-2\|Def. §22.2]], [[§22 The Differential of a Map Between Vector Spaces#^prop-22-2\|Prop. §22.2]], [[§22 The Differential of a Map Between Vector Spaces#^def-22-4\|Def. §22.4]] |
| Example 1.25 | [[§11 Topological Groups and Classical Matrix Groups#^def-11-2\|Def. §11.2]] |
| Example 1.26 | [[§3 Subspaces and Products#^prop-3-6\|Prop. §3.6]], [[§3 Subspaces and Products#^def-3-2\|Def. §3.2]] |
| Example 1.27 | [[§11 Topological Groups and Classical Matrix Groups#^def-11-5\|Def. §11.5]], [[§11 Topological Groups and Classical Matrix Groups#^prop-11-4\|Prop. §11.4]], [[§12 The Classical Groups Are Topological Manifolds#^thm-12-6\|Thm. §12.6]] |
| Example 1.31 | [[§17 Differentiable Structures#^ex-17-2\|Ex. §17.2]] |
| Example 1.32 | [[§7 The Regular Value Theorem#^thm-7-3\|Thm. §7.3]], [[§20 Manifolds in Euclidean Space#^prop-20-2\|Prop. §20.2]] |
| Example 1.33 | [[§18 Projective Spaces as Smooth Manifolds#^cor-18-5\|Cor. §18.5]], [[§18 Projective Spaces as Smooth Manifolds#^prop-18-6\|Prop. §18.6]] |
| Example 1.34 | [[§19 Smooth Functions and Smooth Maps#^prop-19-8\|Prop. §19.8]] |
| Lemma 1.35 | [[§44 The Tangent Bundle#^prop-44-1\|Prop. §44.1]], [[§45 The Cotangent Bundle#^prop-45-1\|Prop. §45.1]] |
| Example 1.36 | [[§15 The Topology of G∕H and Real Grassmannians#^def-15-3\|Def. §15.3]], [[§15 The Topology of G∕H and Real Grassmannians#^cor-15-8\|Cor. §15.8]] |
| Problem 1-1 | [[§1 Point-Set Topology Review#^ex-1-4\|Ex. §1.4]], [[§2 Topological Manifolds#^prop-2-4\|Prop. §2.4]], [[§4 Quotient Spaces and Open Maps#^ex-4-1\|Ex. §4.1]] |
| Problem 1-2 | [[§2 Topological Manifolds#^ex-2-3\|Ex. §2.3]], [[§2 Topological Manifolds#^prop-2-4\|Prop. §2.4]] |
| Problem 1-6 | [[§19 Smooth Functions and Smooth Maps#^prop-19-6\|Prop. §19.6]], [[§19 Smooth Functions and Smooth Maps#^def-19-6\|Def. §19.6]], [[§19 Smooth Functions and Smooth Maps#^cor-19-7\|Cor. §19.7]] |
| Problem 1-7 | [[§17 Differentiable Structures#^ex-17-3\|Ex. §17.3]] |
| Problem 1-9 | [[§9 Complex Projective Space#^def-9-1\|Def. §9.1]], [[§9 Complex Projective Space#^prop-9-1\|Prop. §9.1]], [[§9 Complex Projective Space#^prop-9-2\|Prop. §9.2]], [[§9 Complex Projective Space#^prop-9-3\|Prop. §9.3]], [[§13 Group Actions and Orbit Spaces#^ex-13-3\|Ex. §13.3]], [[§18 Projective Spaces as Smooth Manifolds#^def-18-1\|Def. §18.1]], [[§18 Projective Spaces as Smooth Manifolds#^def-18-2\|Def. §18.2]], [[§18 Projective Spaces as Smooth Manifolds#^prop-18-1\|Prop. §18.1]], [[§18 Projective Spaces as Smooth Manifolds#^thm-18-2\|Thm. §18.2]] |
| Proposition 2.5 | [[§19 Smooth Functions and Smooth Maps#^prop-19-2\|Prop. §19.2]] |
| Proposition 2.10 | [[§19 Smooth Functions and Smooth Maps#^lem-19-4\|Lem. §19.4]] |
| Proposition 2.15 | [[§19 Smooth Functions and Smooth Maps#^prop-19-5\|Prop. §19.5]] |
| Proposition 2.25 | [[§28 Derivations and the Abstract Tangent Space#^prop-28-3\|Prop. §28.3]], [[§47 Vector Fields#^prop-47-3\|Prop. §47.3]] |
| Lemma 2.26 | [[§47 Vector Fields#^cor-47-4\|Cor. §47.4]] |
| Lemma 3.1 | [[§28 Derivations and the Abstract Tangent Space#^lem-28-2\|Lem. §28.2]] |
| Proposition 3.2 | [[§25 The Geometric Tangent Space#^def-25-4\|Def. §25.4]], [[§25 The Geometric Tangent Space#^prop-25-9\|Prop. §25.9]], [[§29 Coordinate Derivations and the Basis Theorem#^lem-29-2\|Lem. §29.2]], [[§29 Coordinate Derivations and the Basis Theorem#^cor-29-4\|Cor. §29.4]], [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6\|Thm. §29.6]] |
| Corollary 3.3 | [[§29 Coordinate Derivations and the Basis Theorem#^cor-29-4\|Cor. §29.4]], [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-5\|Thm. §29.5]], [[§30 The Differential in Coordinates#^prop-30-5\|Prop. §30.5]] |
| Lemma 3.4 | [[§28 Derivations and the Abstract Tangent Space#^lem-28-2\|Lem. §28.2]] |
| Proposition 3.6 | [[§28 Derivations and the Abstract Tangent Space#^thm-28-6\|Thm. §28.6]], [[§28 Derivations and the Abstract Tangent Space#^cor-28-7\|Cor. §28.7]] |
| Proposition 3.8 | [[§28 Derivations and the Abstract Tangent Space#^prop-28-3\|Prop. §28.3]] |
| Proposition 3.9 | [[§28 Derivations and the Abstract Tangent Space#^lem-28-8\|Lem. §28.8]] |
| Proposition 3.10 | [[§29 Coordinate Derivations and the Basis Theorem#^cor-29-7\|Cor. §29.7]] |
| Proposition 3.13 | [[§30 The Differential in Coordinates#^prop-30-5\|Prop. §30.5]], [[§30 The Differential in Coordinates#^cor-30-6\|Cor. §30.6]] |
| Proposition 3.14 | [[§31 Tangent Vectors as Velocities of Curves#^thm-31-4\|Thm. §31.4]], [[§31 Tangent Vectors as Velocities of Curves#^cor-31-5\|Cor. §31.5]], [[§34 Submersions#^ex-34-2\|Ex. §34.2]] |
| Proposition 3.15 | [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-5\|Thm. §29.5]] |
| Proposition 3.18 | [[§44 The Tangent Bundle#^def-44-4\|Def. §44.4]], [[§44 The Tangent Bundle#^def-44-5\|Def. §44.5]], [[§44 The Tangent Bundle#^prop-44-1\|Prop. §44.1]], [[§44 The Tangent Bundle#^prop-44-2\|Prop. §44.2]], [[§44 The Tangent Bundle#^prop-44-4\|Prop. §44.4]] |
| Proposition 3.23 | [[§31 Tangent Vectors as Velocities of Curves#^thm-31-2\|Thm. §31.2]] |
| Proposition 3.24 | [[§31 Tangent Vectors as Velocities of Curves#^cor-31-3\|Cor. §31.3]] |
| Corollary 3.25 | [[§22 The Differential of a Map Between Vector Spaces#^thm-22-3\|Thm. §22.3]], [[§31 Tangent Vectors as Velocities of Curves#^cor-31-3\|Cor. §31.3]] |
| Proposition 4.1 | [[§34 Submersions#^cor-34-5\|Cor. §34.5]] |
| Theorem 4.5 | [[§33 Local Diffeomorphisms#^thm-33-2\|Thm. §33.2]] |
| Proposition 4.6 | [[§33 Local Diffeomorphisms#^cor-33-3\|Cor. §33.3]] |
| Proposition 4.8 | [[§33 Local Diffeomorphisms#^thm-33-2\|Thm. §33.2]], [[§34 Submersions#^prop-34-1\|Prop. §34.1]] |
| Theorem 4.12 | [[§34 Submersions#^thm-34-4\|Thm. §34.4]], [[§37 Immersions#^thm-37-1\|Thm. §37.1]] |
| Example 4.20 | [[§38 Embeddings#^prop-38-11\|Prop. §38.11]] |
| Lemma 4.21 | [[§38 Embeddings#^lem-38-10\|Lem. §38.10]] |
| Proposition 4.22 | [[§38 Embeddings#^thm-38-5\|Thm. §38.5]], [[§38 Embeddings#^cor-38-6\|Cor. §38.6]] |
| Proposition 4.28 | [[§34 Submersions#^cor-34-6\|Cor. §34.6]] |
| Problem 4-5 | [[§18 Projective Spaces as Smooth Manifolds#^prop-18-4\|Prop. §18.4]], [[§39 Projective Spaces and the Hopf Fibration#^ex-39-2\|Ex. §39.2]], [[§39 Projective Spaces and the Hopf Fibration#^ex-39-3\|Ex. §39.3]] |
| Proposition 5.2 | [[§38 Embeddings#^thm-38-1\|Thm. §38.1]] |
| Proposition 5.5 | [[§38 Embeddings#^prop-38-9\|Prop. §38.9]] |
| Theorem 5.8 | [[§35 Submanifolds#^def-35-1\|Def. §35.1]], [[§35 Submanifolds#^def-35-2\|Def. §35.2]], [[§35 Submanifolds#^prop-35-2\|Prop. §35.2]] |
| Corollary 5.14 | [[§7 The Regular Value Theorem#^thm-7-3\|Thm. §7.3]], [[§20 Manifolds in Euclidean Space#^prop-20-2\|Prop. §20.2]], [[§35 Submanifolds#^thm-35-7\|Thm. §35.7]] |
| Corollary 5.30 | [[§35 Submanifolds#^lem-35-3\|Lem. §35.3]] |
| Proposition 5.35 | [[§35 Submanifolds#^prop-35-4\|Prop. §35.4]] |
| Proposition 5.37 | [[§25 The Geometric Tangent Space#^def-25-1\|Def. §25.1]], [[§25 The Geometric Tangent Space#^cor-25-4\|Cor. §25.4]], [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6\|Thm. §29.6]], [[§35 Submanifolds#^prop-35-4\|Prop. §35.4]] |
| Proposition 5.38 | [[§25 The Geometric Tangent Space#^thm-25-3\|Thm. §25.3]], [[§25 The Geometric Tangent Space#^cor-25-4\|Cor. §25.4]], [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6\|Thm. §29.6]], [[§35 Submanifolds#^thm-35-7\|Thm. §35.7]] |
| Theorem 6.30 | [[§26 Transversality#^thm-26-1\|Thm. §26.1]], [[§26 Transversality#^def-26-3\|Def. §26.3]], [[§26 Transversality#^prop-26-4\|Prop. §26.4]] |
| Example 7.3 | [[§11 Topological Groups and Classical Matrix Groups#^prop-11-4\|Prop. §11.4]], [[§49 Lie Groups and Left-Invariant Vector Fields#^prop-49-1\|Prop. §49.1]] |
| Proposition 7.26 | [[§14 Homogeneous Spaces#^def-14-4\|Def. §14.4]] |
| Example 7.27 | [[§11 Topological Groups and Classical Matrix Groups#^prop-11-5\|Prop. §11.5]], [[§12 The Classical Groups Are Topological Manifolds#^thm-12-6\|Thm. §12.6]], [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-23-1\|Ex. §23.1]], [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^cor-23-2\|Cor. §23.2]], [[§25 The Geometric Tangent Space#^thm-25-5\|Thm. §25.5]], [[§49 Lie Groups and Left-Invariant Vector Fields#^prop-49-1\|Prop. §49.1]] |
| Example 7.28 | [[§12 The Classical Groups Are Topological Manifolds#^thm-12-6\|Thm. §12.6]], [[§25 The Geometric Tangent Space#^thm-25-5\|Thm. §25.5]], [[§49 Lie Groups and Left-Invariant Vector Fields#^prop-49-1\|Prop. §49.1]] |
| Example 7.29 | [[§11 Topological Groups and Classical Matrix Groups#^def-11-9\|Def. §11.9]], [[§11 Topological Groups and Classical Matrix Groups#^def-11-10\|Def. §11.10]], [[§12 The Classical Groups Are Topological Manifolds#^thm-12-6\|Thm. §12.6]], [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-23-2\|Ex. §23.2]], [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^cor-23-5\|Cor. §23.5]], [[§25 The Geometric Tangent Space#^thm-25-5\|Thm. §25.5]], [[§49 Lie Groups and Left-Invariant Vector Fields#^prop-49-1\|Prop. §49.1]] |
| Example 7.30 | [[§11 Topological Groups and Classical Matrix Groups#^def-11-9\|Def. §11.9]], [[§11 Topological Groups and Classical Matrix Groups#^def-11-10\|Def. §11.10]], [[§12 The Classical Groups Are Topological Manifolds#^thm-12-6\|Thm. §12.6]], [[§25 The Geometric Tangent Space#^thm-25-5\|Thm. §25.5]], [[§49 Lie Groups and Left-Invariant Vector Fields#^prop-49-1\|Prop. §49.1]] |
| Problem 7-4 | [[§12 The Classical Groups Are Topological Manifolds#^prop-12-1\|Prop. §12.1]], [[§12 The Classical Groups Are Topological Manifolds#^cor-12-2\|Cor. §12.2]] |
| Problem 7-22 | [[§40 The Unit Quaternions and SU(2)#^def-40-1\|Def. §40.1]] |
| Proposition 8.1 | [[§47 Vector Fields#^prop-47-1\|Prop. §47.1]] |
| Proposition 8.15 | [[§47 Vector Fields#^prop-47-7\|Prop. §47.7]] |
| Lemma 8.25 | [[§48 Lie Bracket and Lie Algebra#^lem-48-1\|Lem. §48.1]] |
| Proposition 8.26 | [[§48 Lie Bracket and Lie Algebra#^prop-48-2\|Prop. §48.2]] |
| Proposition 8.28 | [[§48 Lie Bracket and Lie Algebra#^cor-48-4\|Cor. §48.4]] |
| Example 10.3 | [[§36 Fibrations#^ex-36-2\|Ex. §36.2]] |
| Proposition 11.1 | [[§21 Linear Algebra Toolkit#^def-21-1\|Def. §21.1]], [[§21 Linear Algebra Toolkit#^def-21-2\|Def. §21.2]], [[§21 Linear Algebra Toolkit#^prop-21-2\|Prop. §21.2]] |
| Proposition 11.4 | [[§21 Linear Algebra Toolkit#^def-21-3\|Def. §21.3]], [[§21 Linear Algebra Toolkit#^prop-21-4\|Prop. §21.4]] |
| Proposition 11.8 | [[§21 Linear Algebra Toolkit#^prop-21-3\|Prop. §21.3]] |
| Proposition 11.9 | [[§45 The Cotangent Bundle#^def-45-1\|Def. §45.1]], [[§45 The Cotangent Bundle#^prop-45-2\|Prop. §45.2]], [[§45 The Cotangent Bundle#^def-45-4\|Def. §45.4]], [[§45 The Cotangent Bundle#^def-45-5\|Def. §45.5]], [[§45 The Cotangent Bundle#^prop-45-1\|Prop. §45.1]], [[§45 The Cotangent Bundle#^cor-45-3\|Cor. §45.3]] |
| Proposition 11.11 | [[§46 One-Forms#^prop-46-1\|Prop. §46.1]] |
| Proposition 11.20 | [[§32 The Cotangent Space#^cor-32-4\|Cor. §32.4]] |
| Proposition 11.25 | [[§32 The Cotangent Space#^prop-32-10\|Prop. §32.10]], [[§46 One-Forms#^cor-46-4\|Cor. §46.4]] |
| Problem 11-4 | [[§28 Derivations and the Abstract Tangent Space#^def-28-3\|Def. §28.3]], [[§28 Derivations and the Abstract Tangent Space#^def-28-4\|Def. §28.4]], [[§32 The Cotangent Space#^prop-32-5\|Prop. §32.5]], [[§32 The Cotangent Space#^prop-32-6\|Prop. §32.6]], [[§32 The Cotangent Space#^thm-32-8\|Thm. §32.8]], [[§32 The Cotangent Space#^prop-32-7\|Prop. §32.7]] |
| Theorem 17.26 | [[§2 Topological Manifolds#^thm-2-1\|Thm. §2.1]] |
| Lemma 21.1 | [[§13 Group Actions and Orbit Spaces#^lem-13-2\|Lem. §13.2]], [[§13 Group Actions and Orbit Spaces#^lem-13-3\|Lem. §13.3]], [[§15 The Topology of G∕H and Real Grassmannians#^prop-15-1\|Prop. §15.1]] |
| Example 21.3 | [[§13 Group Actions and Orbit Spaces#^ex-13-6\|Ex. §13.6]] |
| Proposition 21.4 | [[§13 Group Actions and Orbit Spaces#^def-13-4\|Def. §13.4]], [[§13 Group Actions and Orbit Spaces#^cor-13-4\|Cor. §13.4]], [[§13 Group Actions and Orbit Spaces#^thm-13-5\|Thm. §13.5]] |
| Corollary 21.6 | [[§13 Group Actions and Orbit Spaces#^cor-13-4\|Cor. §13.4]], [[§13 Group Actions and Orbit Spaces#^thm-13-5\|Thm. §13.5]] |
| Example 21.14 | [[§15 The Topology of G∕H and Real Grassmannians#^ex-15-1\|Ex. §15.1]] |
| Example 21.15 | [[§14 Homogeneous Spaces#^def-14-1\|Def. §14.1]], [[§14 Homogeneous Spaces#^def-14-2\|Def. §14.2]], [[§14 Homogeneous Spaces#^ex-14-3\|Ex. §14.3]] |
| Theorem 21.17 | [[§14 Homogeneous Spaces#^def-14-5\|Def. §14.5]], [[§14 Homogeneous Spaces#^def-14-6\|Def. §14.6]], [[§14 Homogeneous Spaces#^lem-14-3\|Lem. §14.3]], [[§14 Homogeneous Spaces#^def-14-7\|Def. §14.7]], [[§14 Homogeneous Spaces#^prop-14-4\|Prop. §14.4]], [[§15 The Topology of G∕H and Real Grassmannians#^def-15-1\|Def. §15.1]], [[§15 The Topology of G∕H and Real Grassmannians#^prop-15-1\|Prop. §15.1]], [[§15 The Topology of G∕H and Real Grassmannians#^cor-15-2\|Cor. §15.2]], [[§15 The Topology of G∕H and Real Grassmannians#^cor-15-5\|Cor. §15.5]] |
| Theorem 21.18 | [[§14 Homogeneous Spaces#^thm-14-2\|Thm. §14.2]], [[§14 Homogeneous Spaces#^lem-14-5\|Lem. §14.5]], [[§15 The Topology of G∕H and Real Grassmannians#^thm-15-3\|Thm. §15.3]] |
| Example 21.19 | [[§14 Homogeneous Spaces#^ex-14-3\|Ex. §14.3]] |
| Theorem 21.20 | [[§15 The Topology of G∕H and Real Grassmannians#^def-15-2\|Def. §15.2]], [[§15 The Topology of G∕H and Real Grassmannians#^prop-15-4\|Prop. §15.4]] |
| Example 21.21 | [[§15 The Topology of G∕H and Real Grassmannians#^prop-15-6\|Prop. §15.6]], [[§15 The Topology of G∕H and Real Grassmannians#^prop-15-7\|Prop. §15.7]], [[§15 The Topology of G∕H and Real Grassmannians#^cor-15-8\|Cor. §15.8]] |
| Proposition 21.34 | [[§16 The Classical Groups#^thm-16-2\|Thm. §16.2]] |
| Proposition 21.35 | [[§16 The Classical Groups#^prop-16-1\|Prop. §16.1]], [[§16 The Classical Groups#^thm-16-2\|Thm. §16.2]] |
