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
| $T_pM$: derivations of germs $C_p^\infty(M)$ | $T_pM$: derivations of $C^\infty(M)$ at $p$ | Isomorphic, by Proposition [[§26 Derivations and the Abstract Tangent Space#^prop-26-3\|§26.3]]; Lee's version needs bump functions. |
| $T^{\mathrm{geo}}_pM$, the geometric tangent space | $\mathbb{R}^n_a$ in $\mathbb{R}^n$; $T_pS \subseteq T_pM$ for embedded $S$ | Theorem [[§27 Coordinate Derivations and the Basis Theorem#^thm-27-6\|§27.6]]; Lee, Propositions 3.2 and 5.38. |
| $F_{*p}$ | $dF_p$ | The notes keep $dF_p$ for the vector-space differential (Definition [[§21 The Differential of a Map Between Vector Spaces#^def-21-4\|§21.4]]) and $df_p$ for functions. |
| $D_\gamma$, the velocity | $\gamma'(0)$ | The notes keep $\gamma'(0)$ for the ordinary derivative of a curve in $\mathbb{R}^N$, a geometric vector (Definition [[§29 Tangent Vectors as Velocities of Curves#^def-29-1\|§29.1]]). |
| $D_v$, $D_v\vert_a$ | $D_v\vert_a$ | The directional derivative (Definition [[§25 Tangent Spaces II꞉ Germs#^def-25-1\|§25.1]]). |
| $[f] \in C_p^\infty(M)$, germs | — | Lee works with global functions $C^\infty(M)$ (Definition [[§25 Tangent Spaces II꞉ Germs#^def-25-3\|§25.3]]). |
| $f_\varphi = f \circ \varphi^{-1}$, $\tilde F = \psi \circ F \circ \varphi^{-1}$ | $\hat f$, $\widehat F$ | Coordinate representations (Definition [[§27 Coordinate Derivations and the Basis Theorem#^def-27-1\|§27.1]]). |
| $\sum_i a^i\, \partial/\partial x^i\vert_p$ | $a^i\, \partial/\partial x^i\vert_p$ | Lee uses the Einstein summation convention; the notes always write the sum. |
| $T_p^*M$, $df_p$, $dx^i\vert_p$ | the same | Definition [[§30 Tangent Spaces III꞉ The Cotangent Space#^def-30-1\|§30.1]], Lemma [[§30 Tangent Spaces III꞉ The Cotangent Space#^lem-30-2\|§30.2]]. |
| $I_p$, $I_p^2$, $I_p/I_p^2$, of germs | $I_p$, $I_p^2$ of global functions (Problem 11-4) | Theorem [[§30 Tangent Spaces III꞉ The Cotangent Space#^thm-30-7\|§30.7]]; Lee's version needs bump functions. |
| $\Gamma = \{(x, g \cdot x)\}$, the orbit relation | $\mathcal{O} = \{(g \cdot p, p)\}$ | The same set with the factors swapped (proof of Lee, Proposition 21.4). |
| $H_{x_0}$, the isotropy group | $G_p$ | Definition [[§13 Homogeneous Spaces#^def-13-2\|§13.2]]. |
| $\Phi : G/H \to X$, $gH \mapsto g \cdot x_0$ | $F : G/G_p \to M$ | Theorem [[§14 The Topology of G∕H and Real Grassmannians#^thm-14-3\|§14.3]]; Lee, Theorem 21.18. |
| $\mathfrak{g} = T^{\mathrm{geo}}_I G$ | $\mathrm{Lie}(G) \cong T_eG$ | The notes' $\mathfrak{g}$ is the geometric tangent space at $I$; Lee defines $\mathrm{Lie}(G)$ by left-invariant vector fields (Chapter 8). |
| $\widetilde{\mathbb{R}}$: the chart $\sqrt[3]{x}$ | Example 1.23: the chart $x^3$ | Two different non-standard structures — the transition map between them is $y \mapsto y^9$ — both diffeomorphic to $\mathbb{R}$ (Corollary [[§18 Smooth Functions and Smooth Maps#^cor-18-7\|§18.7]]). |

## A.2 Where the routes diverge

Each row is expanded in a **Comparison with Lee** paragraph at the place indicated.

| Topic | These notes | Lee |
|---|---|---|
| Hausdorff quotients | One criterion for all open quotients (Theorems [[§6 Open Quotients#^thm-6-1\|§6.1]] and [[§6 Open Quotients#^thm-6-3\|§6.3]]), reused for orbit and coset spaces | Checked example by example (Example 1.5, Problem 1-9) |
| Regular level sets | Implicit function theorem, topological first (Theorem [[§7 The Regular Value Theorem#^thm-7-3\|§7.3]]), smooth afterwards (Proposition [[§19 Manifolds in Euclidean Space#^prop-19-2\|§19.2]]) | Example 1.32 for one function; Corollary 5.14 via the constant-rank theorem |
| Hausdorff orbit spaces | Compact group on a Hausdorff space, purely topological (Theorem [[§12 Group Actions and Orbit Spaces#^thm-12-5\|§12.5]]) | Proper actions of Lie groups (Proposition 21.4, Corollary 21.6) |
| Homogeneous spaces | $G/H$ compact and $X$ Hausdorff (Theorem [[§14 The Topology of G∕H and Real Grassmannians#^thm-14-3\|§14.3]]); the hypothesis is needed (Example [[§14 The Topology of G∕H and Real Grassmannians#^ex-14-2\|§14.2]]) | Smooth version, no compactness (Theorem 21.18) |
| Tangent vectors | Derivations of germs; locality is built in, and no bump functions are needed | Derivations of $C^\infty(M)$; locality from bump functions (Proposition 3.8) |
| Order of ideas | Geometric first, $T^{\mathrm{geo}}_pM = \ker F'(p)$ (Theorem [[§23 Tangent Spaces I꞉ The Geometric Picture#^thm-23-3\|§23.3]]), then derivations | Derivations first; $T_pS = \ker d\Phi_p$ later (Proposition 5.38) |
| Cotangent space | The dual, and also $I_p/I_p^2$ of germs, via a non-degenerate pairing (Theorem [[§30 Tangent Spaces III꞉ The Cotangent Space#^thm-30-7\|§30.7]]) | The dual in the text (Chapter 11); $I_p/I_p^2$ of global functions, via $f \mapsto df_p$, as Problem 11-4 |
| Transversality | Level sets in Euclidean space (Theorem [[§24 Transversality#^thm-24-1\|§24.1]]) | Embedded submanifolds (Theorem 6.30) |
| Linear algebra | The toolkit of [[§20 Linear Algebra Toolkit\|§20]], including the pairing theorem (Theorem [[§20 Linear Algebra Toolkit#^thm-20-5\|§20.5]]) | Appendix B; dual spaces in Chapter 11 |

## A.3 Chapter map

| These notes | Lee |
|---|---|
| [[§1 Point-Set Topology Review\|§1]] Point-set review | Appendix A, *Topological Spaces* and *Connectedness and Compactness* |
| [[§2 Topological Manifolds\|§2]] Topological manifolds | Chapter 1, *Topological Manifolds*; Problems 1-1 and 1-2 |
| [[§3 Subspaces and Products\|§3]]–[[§6 Open Quotients\|§6]] Subspaces, products, quotients | Appendix A, *Subspaces, Products, Disjoint Unions, and Quotients*; Problem 1-9 |
| [[§7 The Regular Value Theorem\|§7]] Regular value theorem | Appendix C (Theorem C.40); Example 1.32; Corollary 5.14 |
| [[§10 Topological Groups and Classical Matrix Groups\|§10]]–[[§11 The Classical Groups Are Topological Manifolds\|§11]] Topological and matrix groups | Chapter 7, Examples 7.27–7.30; Propositions 21.34 and 21.35; Problem 7-4 |
| [[§12 Group Actions and Orbit Spaces\|§12]] Actions and orbit spaces | Chapter 7, *Group Actions and Equivariant Maps*; Lemma 21.1, Proposition 21.4 |
| [[§13 Homogeneous Spaces\|§13]]–[[§14 The Topology of G∕H and Real Grassmannians\|§14]] Homogeneous spaces | Theorems 21.17–21.20; Examples 1.36 and 21.21 |
| [[§16 Differentiable Structures\|§16]]–[[§18 Smooth Functions and Smooth Maps\|§18]] Differentiable structures | Chapter 1, *Smooth Structures*, Examples 1.22–1.34; Chapter 2 |
| [[§19 Manifolds in Euclidean Space\|§19]] Manifolds in Euclidean space | Example 1.32; Chapter 5 |
| [[§20 Linear Algebra Toolkit\|§20]]–[[§22 The Orthogonal and Unitary Groups as Smooth Manifolds\|§22]] Vector spaces and matrix groups | Appendix B; Chapter 11 (dual spaces); Example 1.24; Examples 7.27 and 7.29 |
| [[§23 Tangent Spaces I꞉ The Geometric Picture\|§23]]–[[§24 Transversality\|§24]] Tangent spaces I: geometric | Propositions 3.2, 5.37 and 5.38; Theorem 6.30 |
| [[§25 Tangent Spaces II꞉ Germs\|§25]]–[[§29 Tangent Vectors as Velocities of Curves\|§29]] Tangent spaces II: abstract | Chapter 3 throughout, including Proposition 3.14 (products) |
| [[§30 Tangent Spaces III꞉ The Cotangent Space\|§30]] Tangent spaces III: cotangent | Chapter 11, *Covectors*; Problem 11-4 for $I_p/I_p^2$ |
| [[§31 Local Diffeomorphisms\|§31]]–[[§32 Submersions\|§32]] Local diffeomorphisms, submersions | Chapter 4 (Propositions 4.1 and 4.28, Theorem 4.12); Theorem C.34 |
| [[§33 Submanifolds\|§33]] Submanifolds | Chapter 5, *Embedded Submanifolds* (Theorem 5.8, Corollary 5.14, Propositions 5.35–5.38) |
| [[§34 Fibrations\|§34]] Fibrations | smooth fiber bundles (Chapter 10); Ehresmann's theorem is not in Lee |
| [[§35 The Tangent Bundle\|§35]] The tangent bundle | Chapter 3, *The Tangent Bundle* (Lemma 1.35, Proposition 3.18); Proposition 11.9 (cotangent bundle); Chapter 8 (vector fields); Chapter 10 (sections) |
| [[§36 Immersions\|§36]] Immersions | Chapter 4, *Immersions* (Theorem 4.12); Example 4.19 |
| [[§37 Embeddings\|§37]] Embeddings | Chapter 4, *Embeddings* (Proposition 4.22, Example 4.20); Proposition 5.2; Theorem A.57; Proposition 1.12 |
| [[§39 Worked Example꞉ The Double Cover SU(2) → SO(3)\|§39]] The double cover $\mathrm{SU}(2) \to \mathrm{SO}(3)$ | Problems 7-22 and 7-23 (quaternions); Examples 7.27–7.30 (matrix groups) |

## A.4 Index from Lee to these notes

Every numbered result of Lee's cited in these notes, in Lee's order, with the boxes that correspond to it. The table is generated from the *Lee:* lines in the boxes, so the two always agree.

| Lee | These notes |
|---|---|
| Theorem 1.2 | [[§2 Topological Manifolds#^thm-2-1\|Thm. §2.1]], [[§2 Topological Manifolds#^cor-2-2\|Cor. §2.2]] |
| Example 1.4 | [[§8 Example꞉ Spheres#^ex-8-1\|Ex. §8.1]], [[§8 Example꞉ Spheres#^prop-8-1\|Prop. §8.1]], [[§16 Differentiable Structures#^ex-16-2\|Ex. §16.2]] |
| Example 1.5 | [[§17 Projective Spaces as Smooth Manifolds#^prop-17-6\|Prop. §17.6]] |
| Example 1.8 | [[§3 Subspaces and Products#^thm-3-12\|Thm. §3.12]] |
| Proposition 1.11 | [[§2 Topological Manifolds#^prop-2-6\|Prop. §2.6]], [[§2 Topological Manifolds#^thm-2-8\|Thm. §2.8]], [[§2 Topological Manifolds#^cor-2-9\|Cor. §2.9]] |
| Proposition 1.12 | [[§2 Topological Manifolds#^prop-2-12\|Prop. §2.12]] |
| Proposition 1.17 | [[§16 Differentiable Structures#^def-16-7\|Def. §16.7]], [[§16 Differentiable Structures#^thm-16-5\|Thm. §16.5]] |
| Example 1.21 | [[§2 Topological Manifolds#^prop-2-5\|Prop. §2.5]] |
| Example 1.22 | [[§16 Differentiable Structures#^ex-16-1\|Ex. §16.1]] |
| Example 1.23 | [[§18 Smooth Functions and Smooth Maps#^ex-18-1\|Ex. §18.1]], [[§18 Smooth Functions and Smooth Maps#^cor-18-7\|Cor. §18.7]], [[§18 Smooth Functions and Smooth Maps#^ex-18-2\|Ex. §18.2]] |
| Example 1.24 | [[§21 The Differential of a Map Between Vector Spaces#^def-21-1\|Def. §21.1]], [[§21 The Differential of a Map Between Vector Spaces#^prop-21-2\|Prop. §21.2]], [[§21 The Differential of a Map Between Vector Spaces#^def-21-3\|Def. §21.3]] |
| Example 1.25 | [[§10 Topological Groups and Classical Matrix Groups#^def-10-2\|Def. §10.2]] |
| Example 1.26 | [[§3 Subspaces and Products#^prop-3-6\|Prop. §3.6]], [[§3 Subspaces and Products#^def-3-2\|Def. §3.2]] |
| Example 1.27 | [[§10 Topological Groups and Classical Matrix Groups#^def-10-4\|Def. §10.4]], [[§10 Topological Groups and Classical Matrix Groups#^prop-10-4\|Prop. §10.4]], [[§11 The Classical Groups Are Topological Manifolds#^thm-11-6\|Thm. §11.6]] |
| Example 1.31 | [[§16 Differentiable Structures#^ex-16-2\|Ex. §16.2]] |
| Example 1.32 | [[§7 The Regular Value Theorem#^thm-7-3\|Thm. §7.3]], [[§19 Manifolds in Euclidean Space#^prop-19-2\|Prop. §19.2]] |
| Example 1.33 | [[§17 Projective Spaces as Smooth Manifolds#^cor-17-5\|Cor. §17.5]], [[§17 Projective Spaces as Smooth Manifolds#^prop-17-6\|Prop. §17.6]] |
| Example 1.34 | [[§18 Smooth Functions and Smooth Maps#^prop-18-8\|Prop. §18.8]] |
| Lemma 1.35 | [[§35 The Tangent Bundle#^prop-35-1\|Prop. §35.1]] |
| Example 1.36 | [[§14 The Topology of G∕H and Real Grassmannians#^def-14-3\|Def. §14.3]], [[§14 The Topology of G∕H and Real Grassmannians#^cor-14-8\|Cor. §14.8]] |
| Problem 1-1 | [[§1 Point-Set Topology Review#^ex-1-4\|Ex. §1.4]], [[§2 Topological Manifolds#^prop-2-4\|Prop. §2.4]], [[§4 Quotient Spaces and Open Maps#^ex-4-1\|Ex. §4.1]] |
| Problem 1-2 | [[§2 Topological Manifolds#^ex-2-3\|Ex. §2.3]], [[§2 Topological Manifolds#^prop-2-4\|Prop. §2.4]] |
| Problem 1-6 | [[§18 Smooth Functions and Smooth Maps#^prop-18-6\|Prop. §18.6]], [[§18 Smooth Functions and Smooth Maps#^def-18-5\|Def. §18.5]], [[§18 Smooth Functions and Smooth Maps#^cor-18-7\|Cor. §18.7]] |
| Problem 1-7 | [[§16 Differentiable Structures#^ex-16-3\|Ex. §16.3]] |
| Problem 1-9 | [[§9 Example꞉ Complex Projective Space#^def-9-1\|Def. §9.1]], [[§9 Example꞉ Complex Projective Space#^prop-9-1\|Prop. §9.1]], [[§9 Example꞉ Complex Projective Space#^prop-9-2\|Prop. §9.2]], [[§9 Example꞉ Complex Projective Space#^prop-9-3\|Prop. §9.3]], [[§12 Group Actions and Orbit Spaces#^ex-12-3\|Ex. §12.3]], [[§17 Projective Spaces as Smooth Manifolds#^def-17-1\|Def. §17.1]], [[§17 Projective Spaces as Smooth Manifolds#^def-17-2\|Def. §17.2]], [[§17 Projective Spaces as Smooth Manifolds#^prop-17-1\|Prop. §17.1]], [[§17 Projective Spaces as Smooth Manifolds#^thm-17-2\|Thm. §17.2]] |
| Proposition 2.5 | [[§18 Smooth Functions and Smooth Maps#^prop-18-2\|Prop. §18.2]] |
| Proposition 2.10 | [[§18 Smooth Functions and Smooth Maps#^lem-18-4\|Lem. §18.4]] |
| Proposition 2.15 | [[§18 Smooth Functions and Smooth Maps#^prop-18-5\|Prop. §18.5]] |
| Proposition 2.25 | [[§26 Derivations and the Abstract Tangent Space#^prop-26-3\|Prop. §26.3]] |
| Lemma 3.1 | [[§26 Derivations and the Abstract Tangent Space#^lem-26-2\|Lem. §26.2]] |
| Proposition 3.2 | [[§25 Tangent Spaces II꞉ Germs#^def-25-1\|Def. §25.1]], [[§25 Tangent Spaces II꞉ Germs#^prop-25-2\|Prop. §25.2]], [[§27 Coordinate Derivations and the Basis Theorem#^lem-27-2\|Lem. §27.2]], [[§27 Coordinate Derivations and the Basis Theorem#^cor-27-4\|Cor. §27.4]], [[§27 Coordinate Derivations and the Basis Theorem#^thm-27-6\|Thm. §27.6]] |
| Corollary 3.3 | [[§27 Coordinate Derivations and the Basis Theorem#^cor-27-4\|Cor. §27.4]], [[§27 Coordinate Derivations and the Basis Theorem#^thm-27-5\|Thm. §27.5]], [[§28 The Differential in Coordinates#^prop-28-5\|Prop. §28.5]] |
| Lemma 3.4 | [[§26 Derivations and the Abstract Tangent Space#^lem-26-2\|Lem. §26.2]] |
| Proposition 3.6 | [[§26 Derivations and the Abstract Tangent Space#^thm-26-6\|Thm. §26.6]], [[§26 Derivations and the Abstract Tangent Space#^cor-26-7\|Cor. §26.7]] |
| Proposition 3.8 | [[§26 Derivations and the Abstract Tangent Space#^prop-26-3\|Prop. §26.3]] |
| Proposition 3.9 | [[§26 Derivations and the Abstract Tangent Space#^lem-26-8\|Lem. §26.8]] |
| Proposition 3.10 | [[§27 Coordinate Derivations and the Basis Theorem#^cor-27-7\|Cor. §27.7]] |
| Proposition 3.13 | [[§28 The Differential in Coordinates#^prop-28-5\|Prop. §28.5]], [[§28 The Differential in Coordinates#^cor-28-6\|Cor. §28.6]] |
| Proposition 3.14 | [[§29 Tangent Vectors as Velocities of Curves#^thm-29-4\|Thm. §29.4]], [[§29 Tangent Vectors as Velocities of Curves#^cor-29-5\|Cor. §29.5]], [[§32 Submersions#^ex-32-2\|Ex. §32.2]] |
| Proposition 3.15 | [[§27 Coordinate Derivations and the Basis Theorem#^thm-27-5\|Thm. §27.5]] |
| Proposition 3.18 | [[§35 The Tangent Bundle#^def-35-2\|Def. §35.2]], [[§35 The Tangent Bundle#^prop-35-1\|Prop. §35.1]], [[§35 The Tangent Bundle#^prop-35-2\|Prop. §35.2]], [[§35 The Tangent Bundle#^prop-35-4\|Prop. §35.4]] |
| Proposition 3.23 | [[§29 Tangent Vectors as Velocities of Curves#^thm-29-2\|Thm. §29.2]] |
| Proposition 3.24 | [[§29 Tangent Vectors as Velocities of Curves#^cor-29-3\|Cor. §29.3]] |
| Corollary 3.25 | [[§21 The Differential of a Map Between Vector Spaces#^thm-21-3\|Thm. §21.3]], [[§29 Tangent Vectors as Velocities of Curves#^cor-29-3\|Cor. §29.3]] |
| Proposition 4.1 | [[§32 Submersions#^cor-32-5\|Cor. §32.5]] |
| Theorem 4.5 | [[§31 Local Diffeomorphisms#^thm-31-2\|Thm. §31.2]] |
| Proposition 4.6 | [[§31 Local Diffeomorphisms#^cor-31-3\|Cor. §31.3]] |
| Proposition 4.8 | [[§31 Local Diffeomorphisms#^thm-31-2\|Thm. §31.2]], [[§32 Submersions#^prop-32-1\|Prop. §32.1]] |
| Theorem 4.12 | [[§32 Submersions#^thm-32-4\|Thm. §32.4]], [[§36 Immersions#^thm-36-1\|Thm. §36.1]] |
| Example 4.20 | [[§37 Embeddings#^prop-37-11\|Prop. §37.11]] |
| Lemma 4.21 | [[§37 Embeddings#^lem-37-10\|Lem. §37.10]] |
| Proposition 4.22 | [[§37 Embeddings#^thm-37-5\|Thm. §37.5]], [[§37 Embeddings#^cor-37-6\|Cor. §37.6]] |
| Proposition 4.28 | [[§32 Submersions#^cor-32-6\|Cor. §32.6]] |
| Problem 4-5 | [[§17 Projective Spaces as Smooth Manifolds#^prop-17-4\|Prop. §17.4]], [[§38 Example꞉ Projective Spaces and the Hopf Fibration#^ex-38-2\|Ex. §38.2]], [[§38 Example꞉ Projective Spaces and the Hopf Fibration#^ex-38-3\|Ex. §38.3]] |
| Proposition 5.2 | [[§37 Embeddings#^thm-37-1\|Thm. §37.1]] |
| Proposition 5.5 | [[§37 Embeddings#^prop-37-9\|Prop. §37.9]] |
| Theorem 5.8 | [[§33 Submanifolds#^def-33-1\|Def. §33.1]], [[§33 Submanifolds#^prop-33-2\|Prop. §33.2]] |
| Corollary 5.14 | [[§7 The Regular Value Theorem#^thm-7-3\|Thm. §7.3]], [[§19 Manifolds in Euclidean Space#^prop-19-2\|Prop. §19.2]], [[§33 Submanifolds#^thm-33-6\|Thm. §33.6]] |
| Corollary 5.30 | [[§33 Submanifolds#^lem-33-3\|Lem. §33.3]] |
| Proposition 5.35 | [[§33 Submanifolds#^prop-33-4\|Prop. §33.4]] |
| Proposition 5.37 | [[§23 Tangent Spaces I꞉ The Geometric Picture#^def-23-1\|Def. §23.1]], [[§23 Tangent Spaces I꞉ The Geometric Picture#^cor-23-4\|Cor. §23.4]], [[§27 Coordinate Derivations and the Basis Theorem#^thm-27-6\|Thm. §27.6]], [[§33 Submanifolds#^prop-33-4\|Prop. §33.4]] |
| Proposition 5.38 | [[§23 Tangent Spaces I꞉ The Geometric Picture#^thm-23-3\|Thm. §23.3]], [[§23 Tangent Spaces I꞉ The Geometric Picture#^cor-23-4\|Cor. §23.4]], [[§27 Coordinate Derivations and the Basis Theorem#^thm-27-6\|Thm. §27.6]], [[§33 Submanifolds#^thm-33-6\|Thm. §33.6]] |
| Theorem 6.30 | [[§24 Transversality#^thm-24-1\|Thm. §24.1]], [[§24 Transversality#^def-24-3\|Def. §24.3]], [[§24 Transversality#^prop-24-4\|Prop. §24.4]] |
| Example 7.3 | [[§10 Topological Groups and Classical Matrix Groups#^prop-10-4\|Prop. §10.4]] |
| Proposition 7.26 | [[§13 Homogeneous Spaces#^def-13-3\|Def. §13.3]] |
| Example 7.27 | [[§10 Topological Groups and Classical Matrix Groups#^prop-10-5\|Prop. §10.5]], [[§11 The Classical Groups Are Topological Manifolds#^thm-11-6\|Thm. §11.6]], [[§22 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-22-1\|Ex. §22.1]], [[§22 The Orthogonal and Unitary Groups as Smooth Manifolds#^cor-22-2\|Cor. §22.2]], [[§23 Tangent Spaces I꞉ The Geometric Picture#^thm-23-5\|Thm. §23.5]] |
| Example 7.28 | [[§11 The Classical Groups Are Topological Manifolds#^thm-11-6\|Thm. §11.6]], [[§23 Tangent Spaces I꞉ The Geometric Picture#^thm-23-5\|Thm. §23.5]] |
| Example 7.29 | [[§10 Topological Groups and Classical Matrix Groups#^def-10-8\|Def. §10.8]], [[§11 The Classical Groups Are Topological Manifolds#^thm-11-6\|Thm. §11.6]], [[§22 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-22-2\|Ex. §22.2]], [[§22 The Orthogonal and Unitary Groups as Smooth Manifolds#^cor-22-5\|Cor. §22.5]], [[§23 Tangent Spaces I꞉ The Geometric Picture#^thm-23-5\|Thm. §23.5]] |
| Example 7.30 | [[§10 Topological Groups and Classical Matrix Groups#^def-10-8\|Def. §10.8]], [[§11 The Classical Groups Are Topological Manifolds#^thm-11-6\|Thm. §11.6]], [[§23 Tangent Spaces I꞉ The Geometric Picture#^thm-23-5\|Thm. §23.5]] |
| Problem 7-4 | [[§11 The Classical Groups Are Topological Manifolds#^prop-11-1\|Prop. §11.1]], [[§11 The Classical Groups Are Topological Manifolds#^cor-11-2\|Cor. §11.2]] |
| Problem 7-22 | [[§39 Worked Example꞉ The Double Cover SU(2) → SO(3)#^def-39-1\|Def. §39.1]] |
| Example 10.3 | [[§34 Fibrations#^ex-34-2\|Ex. §34.2]] |
| Proposition 11.1 | [[§20 Linear Algebra Toolkit#^def-20-1\|Def. §20.1]], [[§20 Linear Algebra Toolkit#^prop-20-2\|Prop. §20.2]] |
| Proposition 11.4 | [[§20 Linear Algebra Toolkit#^def-20-2\|Def. §20.2]], [[§20 Linear Algebra Toolkit#^prop-20-4\|Prop. §20.4]] |
| Proposition 11.8 | [[§20 Linear Algebra Toolkit#^prop-20-3\|Prop. §20.3]] |
| Proposition 11.9 | [[§35 The Tangent Bundle#^def-35-5\|Def. §35.5]], [[§35 The Tangent Bundle#^prop-35-5\|Prop. §35.5]] |
| Proposition 11.20 | [[§30 Tangent Spaces III꞉ The Cotangent Space#^cor-30-3\|Cor. §30.3]] |
| Problem 11-4 | [[§26 Derivations and the Abstract Tangent Space#^def-26-3\|Def. §26.3]], [[§30 Tangent Spaces III꞉ The Cotangent Space#^prop-30-4\|Prop. §30.4]], [[§30 Tangent Spaces III꞉ The Cotangent Space#^prop-30-5\|Prop. §30.5]], [[§30 Tangent Spaces III꞉ The Cotangent Space#^thm-30-7\|Thm. §30.7]] |
| Theorem 17.26 | [[§2 Topological Manifolds#^thm-2-1\|Thm. §2.1]] |
| Lemma 21.1 | [[§12 Group Actions and Orbit Spaces#^lem-12-2\|Lem. §12.2]], [[§12 Group Actions and Orbit Spaces#^lem-12-3\|Lem. §12.3]], [[§14 The Topology of G∕H and Real Grassmannians#^prop-14-1\|Prop. §14.1]] |
| Example 21.3 | [[§12 Group Actions and Orbit Spaces#^ex-12-6\|Ex. §12.6]] |
| Proposition 21.4 | [[§12 Group Actions and Orbit Spaces#^def-12-4\|Def. §12.4]], [[§12 Group Actions and Orbit Spaces#^cor-12-4\|Cor. §12.4]], [[§12 Group Actions and Orbit Spaces#^thm-12-5\|Thm. §12.5]] |
| Corollary 21.6 | [[§12 Group Actions and Orbit Spaces#^cor-12-4\|Cor. §12.4]], [[§12 Group Actions and Orbit Spaces#^thm-12-5\|Thm. §12.5]] |
| Example 21.14 | [[§14 The Topology of G∕H and Real Grassmannians#^ex-14-1\|Ex. §14.1]] |
| Example 21.15 | [[§13 Homogeneous Spaces#^def-13-1\|Def. §13.1]], [[§13 Homogeneous Spaces#^ex-13-3\|Ex. §13.3]] |
| Theorem 21.17 | [[§13 Homogeneous Spaces#^def-13-4\|Def. §13.4]], [[§13 Homogeneous Spaces#^lem-13-3\|Lem. §13.3]], [[§13 Homogeneous Spaces#^def-13-5\|Def. §13.5]], [[§13 Homogeneous Spaces#^prop-13-4\|Prop. §13.4]], [[§14 The Topology of G∕H and Real Grassmannians#^def-14-1\|Def. §14.1]], [[§14 The Topology of G∕H and Real Grassmannians#^prop-14-1\|Prop. §14.1]], [[§14 The Topology of G∕H and Real Grassmannians#^cor-14-2\|Cor. §14.2]], [[§14 The Topology of G∕H and Real Grassmannians#^cor-14-5\|Cor. §14.5]] |
| Theorem 21.18 | [[§13 Homogeneous Spaces#^thm-13-2\|Thm. §13.2]], [[§13 Homogeneous Spaces#^lem-13-5\|Lem. §13.5]], [[§14 The Topology of G∕H and Real Grassmannians#^thm-14-3\|Thm. §14.3]] |
| Example 21.19 | [[§13 Homogeneous Spaces#^ex-13-3\|Ex. §13.3]] |
| Theorem 21.20 | [[§14 The Topology of G∕H and Real Grassmannians#^def-14-2\|Def. §14.2]], [[§14 The Topology of G∕H and Real Grassmannians#^prop-14-4\|Prop. §14.4]] |
| Example 21.21 | [[§14 The Topology of G∕H and Real Grassmannians#^prop-14-6\|Prop. §14.6]], [[§14 The Topology of G∕H and Real Grassmannians#^prop-14-7\|Prop. §14.7]], [[§14 The Topology of G∕H and Real Grassmannians#^cor-14-8\|Cor. §14.8]] |
| Proposition 21.34 | [[§15 Example꞉ The Classical Groups#^thm-15-2\|Thm. §15.2]] |
| Proposition 21.35 | [[§15 Example꞉ The Classical Groups#^prop-15-1\|Prop. §15.1]], [[§15 Example꞉ The Classical Groups#^thm-15-2\|Thm. §15.2]] |
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
| Theorem A.57 | [[§37 Embeddings#^prop-37-4\|Prop. §37.4]] |
| Corollary B.21 | [[§20 Linear Algebra Toolkit#^prop-20-1\|Prop. §20.1]] |
| Proposition B.24 | [[§20 Linear Algebra Toolkit#^prop-20-1\|Prop. §20.1]] |
| Theorem C.15 | [[§27 Coordinate Derivations and the Basis Theorem#^lem-27-2\|Lem. §27.2]], [[§27 Coordinate Derivations and the Basis Theorem#^lem-27-3\|Lem. §27.3]] |
| Theorem C.34 | [[§31 Local Diffeomorphisms#^thm-31-1\|Thm. §31.1]] |
| Example C.37 | [[§28 The Differential in Coordinates#^ex-28-1\|Ex. §28.1]] |
| Theorem C.40 | [[§7 The Regular Value Theorem#^thm-7-1\|Thm. §7.1]], [[§7 The Regular Value Theorem#^cor-7-2\|Cor. §7.2]] |
