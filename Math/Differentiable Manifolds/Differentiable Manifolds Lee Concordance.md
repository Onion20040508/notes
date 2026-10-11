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
| $F_{*p}$; from Lecture 17, $dF_p$ | $dF_p$ | Through [[§52 Lie Bracket and Lie Algebra\|§52]] the notes keep $dF_p$ for the vector-space differential (Definition [[§22 The Differential of a Map Between Vector Spaces#^def-22-5\|§22.5]]) and $df_p$ for functions; from Remark [[§53 Related Vector Fields#^rem-53-2\|Notation]] on, $dF_p$ is the pushforward, which agrees with the vector-space differential (Corollary [[§30 The Differential in Coordinates#^cor-30-6\|§30.6]]). |
| $D_\gamma$, the velocity | $\gamma'(0)$ | The notes keep $\gamma'(0)$ for the ordinary derivative of a curve in $\mathbb{R}^N$, a geometric vector (Definition [[§31 Tangent Vectors as Velocities of Curves#^def-31-2\|§31.2]]). |
| $D_v$, $D_v\vert_a$ | $D_v\vert_a$ | The directional derivative (Definition [[§25 The Geometric Tangent Space#^def-25-4\|§25.4]]). |
| $[f] \in C_p^\infty(M)$, germs | — | Lee works with global functions $C^\infty(M)$ (Definition [[§27 Germs#^def-27-2\|§27.2]]). |
| $f_\varphi = f \circ \varphi^{-1}$, $\tilde F = \psi \circ F \circ \varphi^{-1}$ | $\hat f$, $\widehat F$ | Coordinate representations (Definition [[§29 Coordinate Derivations and the Basis Theorem#^def-29-1\|§29.1]]). |
| $\sum_i a^i\, \partial/\partial x^i\vert_p$ | $a^i\, \partial/\partial x^i\vert_p$ | Lee uses the Einstein summation convention; the notes always write the sum. |
| $T_p^*M$, $df_p$, $dx^i\vert_p$ | the same | Definition [[§32 The Cotangent Space#^def-32-4\|§32.4]], Lemma [[§33 Covectors in Coordinates#^lem-33-1\|§33.1]]. |
| $I_p$, $I_p^2$, $I_p/I_p^2$, of germs | $I_p$, $I_p^2$ of global functions (Problem 11-4) | Theorem [[§34 The Cotangent Space from Germs#^thm-34-4\|§34.4]]; Lee's version needs bump functions. |
| $\Gamma = \{(x, g \cdot x)\}$, the orbit relation | $\mathcal{O} = \{(g \cdot p, p)\}$ | The same set with the factors swapped (proof of Lee, Proposition 21.4). |
| $H_{x_0}$, the isotropy group | $G_p$ | Definition [[§14 Homogeneous Spaces#^def-14-3\|§14.3]]. |
| $\Phi : G/H \to X$, $gH \mapsto g \cdot x_0$ | $F : G/G_p \to M$ | Theorem [[§15 The Topology of G∕H and Real Grassmannians#^thm-15-3\|§15.3]]; Lee, Theorem 21.18. |
| $\mathfrak{g} = T^{\mathrm{geo}}_I G$; from [[§54 Lie Groups and Left-Invariant Vector Fields\|§54]], the left-invariant fields | $\mathrm{Lie}(G) \cong T_eG$ | Before [[§54 Lie Groups and Left-Invariant Vector Fields\|§54]] the notes' $\mathfrak{g}$ is the geometric tangent space at $I$; from Definition [[§54 Lie Groups and Left-Invariant Vector Fields#^def-54-4\|§54.4]] it is Lee's $\mathrm{Lie}(G)$, identified with $T_eG$ by Theorem [[§54 Lie Groups and Left-Invariant Vector Fields#^thm-54-5\|§54.5]]. |
| $\widetilde{\mathbb{R}}$: the chart $\sqrt[3]{x}$ | Example 1.23: the chart $x^3$ | Two different non-standard structures — the transition map between them is $y \mapsto y^9$ — both diffeomorphic to $\mathbb{R}$ (Corollary [[§19 Smooth Functions and Smooth Maps#^cor-19-8\|§19.8]]). |

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
| Cotangent space | The dual, and also $I_p/I_p^2$ of germs, via a non-degenerate pairing (Theorem [[§34 The Cotangent Space from Germs#^thm-34-4\|§34.4]]) | The dual in the text (Chapter 11); $I_p/I_p^2$ of global functions, via $f \mapsto df_p$, as Problem 11-4 |
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
| [[§35 Local Diffeomorphisms\|§35]]–[[§36 Submersions\|§36]] Local diffeomorphisms, submersions | Chapter 4 (Propositions 4.1 and 4.28, Theorem 4.12); Theorem C.34 |
| [[§37 Regular Submanifolds\|§37]] Regular submanifolds | Chapter 5, *Embedded Submanifolds* (Theorem 5.8, Corollary 5.14, Propositions 5.35–5.38) |
| [[§38 Fibrations\|§38]] Fibrations | smooth fiber bundles (Chapter 10); Chapter 10 (sections); Ehresmann's theorem is not in Lee |
| [[§39 Immersions\|§39]] Immersions | Chapter 4, *Immersions* (Theorem 4.12); Example 4.19 |
| [[§40 Embeddings\|§40]] Embeddings | Chapter 4, *Embeddings* (Proposition 4.22, Example 4.20); Proposition 5.2; Theorem A.57; Proposition 1.12 |
| [[§41 Geometric and Abstract Manifolds\|§41]] Geometric and abstract manifolds (comparison) | Chapters 1, 3 and 5 (overview); Theorem 6.15 (Whitney embedding) |
| [[§43 The Unit Quaternions and SU(2)\|§43]]–[[§44 SU(2) → SO(3)꞉ The Double Cover\|§44]] The unit quaternions and the double cover $\mathrm{SU}(2) \to \mathrm{SO}(3)$ | Problems 7-22 and 7-23 (quaternions); Examples 7.27–7.30 (matrix groups) |
| [[§45 Recap꞉ Germs, Derivations and Tangent Vectors\|§45]]–[[§46 Recap꞉ Covectors and the Four Differentials\|§46]] Recaps: tangent vectors, covectors | Chapters 3 and 11 (overview) |
| [[§47 The Tangent Bundle\|§47]] The tangent bundle | Chapter 3, *The Tangent Bundle* (Lemma 1.35, Proposition 3.18) |
| [[§48 The Cotangent Bundle\|§48]] The cotangent bundle | Chapter 11, *The Cotangent Bundle* (Proposition 11.9); Lemma 1.35 |
| [[§49 One-Forms\|§49]] One-forms, the operator $d$, pullbacks | Chapter 11, *Covector Fields* (Propositions 11.11 and 11.25, Example 11.36, Corollary 11.50) |
| [[§50 Vector Fields\|§50]] Vector fields | Chapter 8 (Propositions 8.1, 8.14 and 8.15); Proposition 2.25 and Lemma 2.26 (bump functions, extension) |
| [[§52 Lie Bracket and Lie Algebra\|§52]] Lie bracket and Lie algebra; related fields | Chapter 8, *Lie Brackets* and *Lie Algebras* (Lemma 8.25, Propositions 8.26 and 8.28); *Vector Fields and Smooth Maps* (Propositions 8.16 and 8.19, Corollary 8.21); Proposition 8.30, Corollary 8.31 |
| [[§54 Lie Groups and Left-Invariant Vector Fields\|§54]] Lie groups and left-invariant vector fields | Chapter 7 (Examples 7.3, 7.27–7.30); Chapter 8, *Lie Algebras* (Proposition 8.33, Theorem 8.37) |

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
| Example 1.23 | [[§19 Smooth Functions and Smooth Maps#^ex-19-1\|Ex. §19.1]], [[§19 Smooth Functions and Smooth Maps#^cor-19-8\|Cor. §19.8]], [[§19 Smooth Functions and Smooth Maps#^ex-19-2\|Ex. §19.2]] |
| Example 1.24 | [[§22 The Differential of a Map Between Vector Spaces#^def-22-1\|Def. §22.1]], [[§22 The Differential of a Map Between Vector Spaces#^def-22-2\|Def. §22.2]], [[§22 The Differential of a Map Between Vector Spaces#^prop-22-2\|Prop. §22.2]], [[§22 The Differential of a Map Between Vector Spaces#^def-22-4\|Def. §22.4]] |
| Example 1.25 | [[§11 Topological Groups and Classical Matrix Groups#^def-11-2\|Def. §11.2]] |
| Example 1.26 | [[§3 Subspaces and Products#^prop-3-6\|Prop. §3.6]], [[§3 Subspaces and Products#^def-3-2\|Def. §3.2]] |
| Example 1.27 | [[§11 Topological Groups and Classical Matrix Groups#^def-11-5\|Def. §11.5]], [[§11 Topological Groups and Classical Matrix Groups#^prop-11-4\|Prop. §11.4]], [[§12 The Classical Groups Are Topological Manifolds#^thm-12-6\|Thm. §12.6]] |
| Example 1.31 | [[§17 Differentiable Structures#^ex-17-2\|Ex. §17.2]] |
| Example 1.32 | [[§7 The Regular Value Theorem#^thm-7-3\|Thm. §7.3]], [[§20 Manifolds in Euclidean Space#^prop-20-2\|Prop. §20.2]] |
| Example 1.33 | [[§18 Projective Spaces as Smooth Manifolds#^cor-18-5\|Cor. §18.5]], [[§18 Projective Spaces as Smooth Manifolds#^prop-18-6\|Prop. §18.6]] |
| Example 1.34 | [[§19 Smooth Functions and Smooth Maps#^prop-19-9\|Prop. §19.9]] |
| Lemma 1.35 | [[§47 The Tangent Bundle#^prop-47-1\|Prop. §47.1]], [[§48 The Cotangent Bundle#^prop-48-1\|Prop. §48.1]] |
| Example 1.36 | [[§15 The Topology of G∕H and Real Grassmannians#^def-15-3\|Def. §15.3]], [[§15 The Topology of G∕H and Real Grassmannians#^cor-15-8\|Cor. §15.8]] |
| Problem 1-1 | [[§1 Point-Set Topology Review#^ex-1-4\|Ex. §1.4]], [[§2 Topological Manifolds#^prop-2-4\|Prop. §2.4]], [[§4 Quotient Spaces and Open Maps#^ex-4-1\|Ex. §4.1]] |
| Problem 1-2 | [[§2 Topological Manifolds#^ex-2-3\|Ex. §2.3]], [[§2 Topological Manifolds#^prop-2-4\|Prop. §2.4]] |
| Problem 1-6 | [[§19 Smooth Functions and Smooth Maps#^prop-19-7\|Prop. §19.7]], [[§19 Smooth Functions and Smooth Maps#^def-19-6\|Def. §19.6]], [[§19 Smooth Functions and Smooth Maps#^cor-19-8\|Cor. §19.8]] |
| Problem 1-7 | [[§17 Differentiable Structures#^ex-17-3\|Ex. §17.3]] |
| Problem 1-9 | [[§9 Complex Projective Space#^def-9-1\|Def. §9.1]], [[§9 Complex Projective Space#^prop-9-1\|Prop. §9.1]], [[§9 Complex Projective Space#^prop-9-2\|Prop. §9.2]], [[§9 Complex Projective Space#^prop-9-3\|Prop. §9.3]], [[§13 Group Actions and Orbit Spaces#^ex-13-3\|Ex. §13.3]], [[§18 Projective Spaces as Smooth Manifolds#^def-18-1\|Def. §18.1]], [[§18 Projective Spaces as Smooth Manifolds#^def-18-2\|Def. §18.2]], [[§18 Projective Spaces as Smooth Manifolds#^prop-18-1\|Prop. §18.1]], [[§18 Projective Spaces as Smooth Manifolds#^thm-18-2\|Thm. §18.2]] |
| Proposition 2.5 | [[§19 Smooth Functions and Smooth Maps#^prop-19-2\|Prop. §19.2]] |
| Proposition 2.10 | [[§19 Smooth Functions and Smooth Maps#^lem-19-4\|Lem. §19.4]] |
| Proposition 2.15 | [[§19 Smooth Functions and Smooth Maps#^prop-19-6\|Prop. §19.6]] |
| Proposition 2.25 | [[§28 Derivations and the Abstract Tangent Space#^prop-28-3\|Prop. §28.3]], [[§50 Vector Fields#^prop-50-4\|Prop. §50.4]] |
| Lemma 2.26 | [[§50 Vector Fields#^cor-50-5\|Cor. §50.5]] |
| Lemma 3.1 | [[§28 Derivations and the Abstract Tangent Space#^lem-28-2\|Lem. §28.2]] |
| Proposition 3.2 | [[§25 The Geometric Tangent Space#^def-25-4\|Def. §25.4]], [[§25 The Geometric Tangent Space#^prop-25-9\|Prop. §25.9]], [[§29 Coordinate Derivations and the Basis Theorem#^lem-29-2\|Lem. §29.2]], [[§29 Coordinate Derivations and the Basis Theorem#^cor-29-4\|Cor. §29.4]], [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6\|Thm. §29.6]] |
| Corollary 3.3 | [[§29 Coordinate Derivations and the Basis Theorem#^cor-29-4\|Cor. §29.4]], [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-5\|Thm. §29.5]], [[§30 The Differential in Coordinates#^prop-30-5\|Prop. §30.5]] |
| Lemma 3.4 | [[§28 Derivations and the Abstract Tangent Space#^lem-28-2\|Lem. §28.2]] |
| Proposition 3.6 | [[§28 Derivations and the Abstract Tangent Space#^thm-28-6\|Thm. §28.6]], [[§28 Derivations and the Abstract Tangent Space#^cor-28-7\|Cor. §28.7]] |
| Proposition 3.8 | [[§28 Derivations and the Abstract Tangent Space#^prop-28-3\|Prop. §28.3]] |
| Proposition 3.9 | [[§28 Derivations and the Abstract Tangent Space#^lem-28-8\|Lem. §28.8]] |
| Proposition 3.10 | [[§29 Coordinate Derivations and the Basis Theorem#^cor-29-7\|Cor. §29.7]] |
| Proposition 3.13 | [[§30 The Differential in Coordinates#^prop-30-5\|Prop. §30.5]], [[§30 The Differential in Coordinates#^cor-30-6\|Cor. §30.6]] |
| Proposition 3.14 | [[§31 Tangent Vectors as Velocities of Curves#^thm-31-4\|Thm. §31.4]], [[§31 Tangent Vectors as Velocities of Curves#^cor-31-5\|Cor. §31.5]], [[§36 Submersions#^ex-36-2\|Ex. §36.2]] |
| Proposition 3.15 | [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-5\|Thm. §29.5]] |
| Proposition 3.18 | [[§47 The Tangent Bundle#^def-47-4\|Def. §47.4]], [[§47 The Tangent Bundle#^def-47-5\|Def. §47.5]], [[§47 The Tangent Bundle#^prop-47-1\|Prop. §47.1]], [[§47 The Tangent Bundle#^prop-47-2\|Prop. §47.2]], [[§47 The Tangent Bundle#^prop-47-4\|Prop. §47.4]] |
| Proposition 3.23 | [[§31 Tangent Vectors as Velocities of Curves#^thm-31-2\|Thm. §31.2]] |
| Proposition 3.24 | [[§31 Tangent Vectors as Velocities of Curves#^cor-31-3\|Cor. §31.3]] |
| Corollary 3.25 | [[§22 The Differential of a Map Between Vector Spaces#^thm-22-3\|Thm. §22.3]], [[§31 Tangent Vectors as Velocities of Curves#^cor-31-3\|Cor. §31.3]] |
| Proposition 4.1 | [[§36 Submersions#^cor-36-5\|Cor. §36.5]] |
| Theorem 4.5 | [[§35 Local Diffeomorphisms#^thm-35-2\|Thm. §35.2]] |
| Proposition 4.6 | [[§35 Local Diffeomorphisms#^cor-35-3\|Cor. §35.3]] |
| Proposition 4.8 | [[§35 Local Diffeomorphisms#^thm-35-2\|Thm. §35.2]], [[§36 Submersions#^prop-36-1\|Prop. §36.1]] |
| Theorem 4.12 | [[§36 Submersions#^thm-36-4\|Thm. §36.4]], [[§39 Immersions#^thm-39-1\|Thm. §39.1]] |
| Example 4.20 | [[§40 Embeddings#^prop-40-11\|Prop. §40.11]] |
| Lemma 4.21 | [[§40 Embeddings#^lem-40-10\|Lem. §40.10]] |
| Proposition 4.22 | [[§40 Embeddings#^thm-40-5\|Thm. §40.5]], [[§40 Embeddings#^cor-40-6\|Cor. §40.6]] |
| Proposition 4.28 | [[§36 Submersions#^cor-36-6\|Cor. §36.6]] |
| Problem 4-5 | [[§18 Projective Spaces as Smooth Manifolds#^prop-18-4\|Prop. §18.4]], [[§42 Projective Spaces and the Hopf Fibration#^ex-42-2\|Ex. §42.2]], [[§42 Projective Spaces and the Hopf Fibration#^ex-42-3\|Ex. §42.3]] |
| Proposition 5.2 | [[§40 Embeddings#^thm-40-1\|Thm. §40.1]] |
| Proposition 5.5 | [[§40 Embeddings#^prop-40-9\|Prop. §40.9]] |
| Theorem 5.8 | [[§37 Regular Submanifolds#^def-37-2\|Def. §37.2]], [[§37 Regular Submanifolds#^def-37-3\|Def. §37.3]], [[§37 Regular Submanifolds#^prop-37-3\|Prop. §37.3]] |
| Corollary 5.14 | [[§7 The Regular Value Theorem#^thm-7-3\|Thm. §7.3]], [[§20 Manifolds in Euclidean Space#^prop-20-2\|Prop. §20.2]], [[§37 Regular Submanifolds#^thm-37-9\|Thm. §37.9]] |
| Corollary 5.30 | [[§37 Regular Submanifolds#^lem-37-5\|Lem. §37.5]] |
| Proposition 5.35 | [[§37 Regular Submanifolds#^prop-37-6\|Prop. §37.6]] |
| Proposition 5.37 | [[§25 The Geometric Tangent Space#^def-25-1\|Def. §25.1]], [[§25 The Geometric Tangent Space#^cor-25-4\|Cor. §25.4]], [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6\|Thm. §29.6]], [[§37 Regular Submanifolds#^prop-37-6\|Prop. §37.6]] |
| Proposition 5.38 | [[§25 The Geometric Tangent Space#^thm-25-3\|Thm. §25.3]], [[§25 The Geometric Tangent Space#^cor-25-4\|Cor. §25.4]], [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6\|Thm. §29.6]], [[§37 Regular Submanifolds#^thm-37-9\|Thm. §37.9]] |
| Theorem 6.30 | [[§26 Transversality#^thm-26-1\|Thm. §26.1]], [[§26 Transversality#^def-26-3\|Def. §26.3]], [[§26 Transversality#^prop-26-4\|Prop. §26.4]] |
| Example 7.3 | [[§11 Topological Groups and Classical Matrix Groups#^prop-11-4\|Prop. §11.4]], [[§54 Lie Groups and Left-Invariant Vector Fields#^prop-54-1\|Prop. §54.1]] |
| Proposition 7.26 | [[§14 Homogeneous Spaces#^def-14-4\|Def. §14.4]] |
| Example 7.27 | [[§11 Topological Groups and Classical Matrix Groups#^prop-11-5\|Prop. §11.5]], [[§12 The Classical Groups Are Topological Manifolds#^thm-12-6\|Thm. §12.6]], [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-23-1\|Ex. §23.1]], [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^cor-23-2\|Cor. §23.2]], [[§25 The Geometric Tangent Space#^thm-25-5\|Thm. §25.5]], [[§54 Lie Groups and Left-Invariant Vector Fields#^prop-54-1\|Prop. §54.1]] |
| Example 7.28 | [[§12 The Classical Groups Are Topological Manifolds#^thm-12-6\|Thm. §12.6]], [[§25 The Geometric Tangent Space#^thm-25-5\|Thm. §25.5]], [[§54 Lie Groups and Left-Invariant Vector Fields#^prop-54-1\|Prop. §54.1]] |
| Example 7.29 | [[§11 Topological Groups and Classical Matrix Groups#^def-11-9\|Def. §11.9]], [[§11 Topological Groups and Classical Matrix Groups#^def-11-10\|Def. §11.10]], [[§12 The Classical Groups Are Topological Manifolds#^thm-12-6\|Thm. §12.6]], [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-23-2\|Ex. §23.2]], [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^cor-23-5\|Cor. §23.5]], [[§25 The Geometric Tangent Space#^thm-25-5\|Thm. §25.5]], [[§54 Lie Groups and Left-Invariant Vector Fields#^prop-54-1\|Prop. §54.1]] |
| Example 7.30 | [[§11 Topological Groups and Classical Matrix Groups#^def-11-9\|Def. §11.9]], [[§11 Topological Groups and Classical Matrix Groups#^def-11-10\|Def. §11.10]], [[§12 The Classical Groups Are Topological Manifolds#^thm-12-6\|Thm. §12.6]], [[§25 The Geometric Tangent Space#^thm-25-5\|Thm. §25.5]], [[§54 Lie Groups and Left-Invariant Vector Fields#^prop-54-1\|Prop. §54.1]] |
| Problem 7-4 | [[§12 The Classical Groups Are Topological Manifolds#^prop-12-1\|Prop. §12.1]], [[§12 The Classical Groups Are Topological Manifolds#^cor-12-2\|Cor. §12.2]] |
| Problem 7-22 | [[§43 The Unit Quaternions and SU(2)#^def-43-1\|Def. §43.1]] |
| Proposition 8.1 | [[§50 Vector Fields#^prop-50-1\|Prop. §50.1]] |
| Proposition 8.14 | [[§50 Vector Fields#^lem-50-8\|Lem. §50.8]] |
| Proposition 8.15 | [[§50 Vector Fields#^prop-50-7\|Prop. §50.7]] |
| Proposition 8.16 | [[§53 Related Vector Fields#^prop-53-1\|Prop. §53.1]] |
| Proposition 8.19 | [[§53 Related Vector Fields#^prop-53-2\|Prop. §53.2]] |
| Corollary 8.21 | [[§53 Related Vector Fields#^prop-53-2\|Prop. §53.2]] |
| Lemma 8.25 | [[§52 Lie Bracket and Lie Algebra#^lem-52-1\|Lem. §52.1]] |
| Proposition 8.26 | [[§52 Lie Bracket and Lie Algebra#^prop-52-2\|Prop. §52.2]] |
| Proposition 8.28 | [[§52 Lie Bracket and Lie Algebra#^cor-52-4\|Cor. §52.4]] |
| Proposition 8.30 | [[§53 Related Vector Fields#^prop-53-3\|Prop. §53.3]] |
| Corollary 8.31 | [[§53 Related Vector Fields#^cor-53-4\|Cor. §53.4]] |
| Proposition 8.33 | [[§54 Lie Groups and Left-Invariant Vector Fields#^cor-54-4\|Cor. §54.4]] |
| Theorem 8.37 | [[§54 Lie Groups and Left-Invariant Vector Fields#^thm-54-5\|Thm. §54.5]] |
| Example 10.3 | [[§38 Fibrations#^ex-38-2\|Ex. §38.2]] |
| Proposition 11.1 | [[§21 Linear Algebra Toolkit#^def-21-1\|Def. §21.1]], [[§21 Linear Algebra Toolkit#^def-21-2\|Def. §21.2]], [[§21 Linear Algebra Toolkit#^prop-21-2\|Prop. §21.2]] |
| Proposition 11.4 | [[§21 Linear Algebra Toolkit#^def-21-3\|Def. §21.3]], [[§21 Linear Algebra Toolkit#^prop-21-4\|Prop. §21.4]] |
| Proposition 11.8 | [[§21 Linear Algebra Toolkit#^prop-21-3\|Prop. §21.3]] |
| Proposition 11.9 | [[§48 The Cotangent Bundle#^def-48-4\|Def. §48.4]], [[§48 The Cotangent Bundle#^def-48-5\|Def. §48.5]], [[§48 The Cotangent Bundle#^prop-48-1\|Prop. §48.1]], [[§48 The Cotangent Bundle#^prop-48-2\|Prop. §48.2]], [[§48 The Cotangent Bundle#^cor-48-3\|Cor. §48.3]] |
| Proposition 11.11 | [[§49 One-Forms#^prop-49-1\|Prop. §49.1]] |
| Proposition 11.20 | [[§32 The Cotangent Space#^cor-32-3\|Cor. §32.3]] |
| Proposition 11.25 | [[§34 The Cotangent Space from Germs#^prop-34-6\|Prop. §34.6]], [[§49 One-Forms#^cor-49-4\|Cor. §49.4]] |
| Problem 11-4 | [[§28 Derivations and the Abstract Tangent Space#^def-28-3\|Def. §28.3]], [[§28 Derivations and the Abstract Tangent Space#^def-28-4\|Def. §28.4]], [[§34 The Cotangent Space from Germs#^prop-34-1\|Prop. §34.1]], [[§34 The Cotangent Space from Germs#^prop-34-2\|Prop. §34.2]], [[§34 The Cotangent Space from Germs#^thm-34-4\|Thm. §34.4]] |
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
| Example A.4 | [[§1 Point-Set Topology Review#^ex-1-2\|Ex. §1.2]] |
| Example A.5 | [[§1 Point-Set Topology Review#^ex-1-3\|Ex. §1.3]], [[§1 Point-Set Topology Review#^prop-1-6\|Prop. §1.6]] |
| Proposition A.17 | [[§3 Subspaces and Products#^prop-3-3\|Prop. §3.3]], [[§3 Subspaces and Products#^cor-3-4\|Cor. §3.4]] |
| Lemma A.19 | [[§1 Point-Set Topology Review#^prop-1-5\|Prop. §1.5]] |
| Proposition A.23 | [[§3 Subspaces and Products#^thm-3-10\|Thm. §3.10]], [[§3 Subspaces and Products#^cor-3-11\|Cor. §3.11]] |
| Theorem A.27 | [[§4 Quotient Spaces and Open Maps#^prop-4-4\|Prop. §4.4]], [[§5 Quotient Maps#^thm-5-1\|Thm. §5.1]], [[§5 Quotient Maps#^cor-5-3\|Cor. §5.3]], [[§5 Quotient Maps#^lem-5-7\|Lem. §5.7]], [[§5 Quotient Maps#^lem-5-8\|Lem. §5.8]] |
| Theorem A.30 | [[§5 Quotient Maps#^thm-5-1\|Thm. §5.1]], [[§5 Quotient Maps#^cor-5-2\|Cor. §5.2]] |
| Theorem A.31 | [[§5 Quotient Maps#^prop-5-4\|Prop. §5.4]] |
| Proposition A.39 | [[§1 Point-Set Topology Review#^prop-1-7\|Prop. §1.7]] |
| Proposition A.41 | [[§1 Point-Set Topology Review#^prop-1-7\|Prop. §1.7]] |
| Proposition A.43 | [[§1 Point-Set Topology Review#^prop-1-7\|Prop. §1.7]] |
| Proposition A.45 | [[§1 Point-Set Topology Review#^prop-1-8\|Prop. §1.8]] |
| Proposition A.50 | [[§1 Point-Set Topology Review#^prop-1-8\|Prop. §1.8]] |
| Lemma A.52 | [[§1 Point-Set Topology Review#^prop-1-8\|Prop. §1.8]] |
| Theorem A.57 | [[§40 Embeddings#^prop-40-4\|Prop. §40.4]] |
| Corollary B.21 | [[§21 Linear Algebra Toolkit#^prop-21-1\|Prop. §21.1]] |
| Proposition B.24 | [[§21 Linear Algebra Toolkit#^prop-21-1\|Prop. §21.1]] |
| Theorem C.15 | [[§29 Coordinate Derivations and the Basis Theorem#^lem-29-2\|Lem. §29.2]], [[§29 Coordinate Derivations and the Basis Theorem#^lem-29-3\|Lem. §29.3]] |
| Theorem C.34 | [[§35 Local Diffeomorphisms#^thm-35-1\|Thm. §35.1]] |
| Example C.37 | [[§30 The Differential in Coordinates#^ex-30-1\|Ex. §30.1]] |
| Theorem C.40 | [[§7 The Regular Value Theorem#^thm-7-1\|Thm. §7.1]], [[§7 The Regular Value Theorem#^cor-7-2\|Cor. §7.2]] |
