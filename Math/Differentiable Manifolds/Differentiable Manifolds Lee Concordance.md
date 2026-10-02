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
| $T_pM$: derivations of germs $C_p^\infty(M)$ | $T_pM$: derivations of $C^\infty(M)$ at $p$ | Isomorphic, by Proposition [[§23 Derivations and the Abstract Tangent Space#^prop-23-3\|§23.3]]; Lee's version needs bump functions. |
| $T^{\mathrm{geo}}_pM$, the geometric tangent space | $\mathbb{R}^n_a$ in $\mathbb{R}^n$; $T_pS \subseteq T_pM$ for embedded $S$ | Theorem [[§24 Coordinate Derivations and the Basis Theorem#^thm-24-6\|§24.6]]; Lee, Propositions 3.2 and 5.38. |
| $F_{*p}$ | $dF_p$ | The notes keep $dF_p$ for the vector-space differential (Definition [[§18 The Differential of a Map Between Vector Spaces#^def-18-4\|§18.4]]) and $df_p$ for functions. |
| $D_\gamma$, the velocity | $\gamma'(0)$ | The notes keep $\gamma'(0)$ for the ordinary derivative of a curve in $\mathbb{R}^N$, a geometric vector (Definition [[§26 Tangent Vectors as Velocities of Curves#^def-26-1\|§26.1]]). |
| $D_v$, $D_v\vert_a$ | $D_v\vert_a$ | The directional derivative (Definition [[§22 Tangent Spaces II꞉ Germs#^def-22-1\|§22.1]]). |
| $[f] \in C_p^\infty(M)$, germs | — | Lee works with global functions $C^\infty(M)$ (Definition [[§22 Tangent Spaces II꞉ Germs#^def-22-3\|§22.3]]). |
| $f_\varphi = f \circ \varphi^{-1}$, $\tilde F = \psi \circ F \circ \varphi^{-1}$ | $\hat f$, $\widehat F$ | Coordinate representations (Definition [[§24 Coordinate Derivations and the Basis Theorem#^def-24-1\|§24.1]]). |
| $\sum_i a^i\, \partial/\partial x^i\vert_p$ | $a^i\, \partial/\partial x^i\vert_p$ | Lee uses the Einstein summation convention; the notes always write the sum. |
| $T_p^*M$, $df_p$, $dx^i\vert_p$ | the same | Definition [[§27 Tangent Spaces III꞉ The Cotangent Space#^def-27-1\|§27.1]], Lemma [[§27 Tangent Spaces III꞉ The Cotangent Space#^lem-27-2\|§27.2]]. |
| $I_p$, $I_p^2$, $I_p/I_p^2$, of germs | $I_p$, $I_p^2$ of global functions (Problem 11-4) | Theorem [[§27 Tangent Spaces III꞉ The Cotangent Space#^thm-27-7\|§27.7]]; Lee's version needs bump functions. |
| $\Gamma = \{(x, g \cdot x)\}$, the orbit relation | $\mathcal{O} = \{(g \cdot p, p)\}$ | The same set with the factors swapped (proof of Lee, Proposition 21.4). |
| $H_{x_0}$, the isotropy group | $G_p$ | Definition [[§11 Homogeneous Spaces#^def-11-2\|§11.2]]. |
| $\Phi : G/H \to X$, $gH \mapsto g \cdot x_0$ | $F : G/G_p \to M$ | Theorem [[§12 The Topology of G∕H and Real Grassmannians#^thm-12-3\|§12.3]]; Lee, Theorem 21.18. |
| $\mathfrak{g} = T^{\mathrm{geo}}_I G$ | $\mathrm{Lie}(G) \cong T_eG$ | The notes' $\mathfrak{g}$ is the geometric tangent space at $I$; Lee defines $\mathrm{Lie}(G)$ by left-invariant vector fields (Chapter 8). |
| $\widetilde{\mathbb{R}}$: the chart $\sqrt[3]{x}$ | Example 1.23: the chart $x^3$ | Two different non-standard structures — the transition map between them is $y \mapsto y^9$ — both diffeomorphic to $\mathbb{R}$ (Corollary [[§15 Smooth Functions and Smooth Maps#^cor-15-7\|§15.7]]). |

## A.2 Where the routes diverge

Each row is expanded in a **Comparison with Lee** paragraph at the place indicated.

| Topic | These notes | Lee |
|---|---|---|
| Hausdorff quotients | One criterion for all open quotients (Theorems [[§6 Open Quotients and Complex Projective Space#^thm-6-1\|§6.1]] and [[§6 Open Quotients and Complex Projective Space#^thm-6-3\|§6.3]]), reused for orbit and coset spaces | Checked example by example (Example 1.5, Problem 1-9) |
| Regular level sets | Implicit function theorem, topological first (Theorem [[§7 The Regular Value Theorem#^thm-7-3\|§7.3]]), smooth afterwards (Proposition [[§16 Manifolds in Euclidean Space#^prop-16-2\|§16.2]]) | Example 1.32 for one function; Corollary 5.14 via the constant-rank theorem |
| Hausdorff orbit spaces | Compact group on a Hausdorff space, purely topological (Theorem [[§10 Group Actions and Orbit Spaces#^thm-10-5\|§10.5]]) | Proper actions of Lie groups (Proposition 21.4, Corollary 21.6) |
| Homogeneous spaces | $G/H$ compact and $X$ Hausdorff (Theorem [[§12 The Topology of G∕H and Real Grassmannians#^thm-12-3\|§12.3]]); the hypothesis is needed (Example [[§12 The Topology of G∕H and Real Grassmannians#^ex-12-2\|§12.2]]) | Smooth version, no compactness (Theorem 21.18) |
| Tangent vectors | Derivations of germs; locality is built in, and no bump functions are needed | Derivations of $C^\infty(M)$; locality from bump functions (Proposition 3.8) |
| Order of ideas | Geometric first, $T^{\mathrm{geo}}_pM = \ker F'(p)$ (Theorem [[§20 Tangent Spaces I꞉ The Geometric Picture#^thm-20-3\|§20.3]]), then derivations | Derivations first; $T_pS = \ker d\Phi_p$ later (Proposition 5.38) |
| Cotangent space | The dual, and also $I_p/I_p^2$ of germs, via a non-degenerate pairing (Theorem [[§27 Tangent Spaces III꞉ The Cotangent Space#^thm-27-7\|§27.7]]) | The dual in the text (Chapter 11); $I_p/I_p^2$ of global functions, via $f \mapsto df_p$, as Problem 11-4 |
| Transversality | Level sets in Euclidean space (Theorem [[§21 Transversality#^thm-21-1\|§21.1]]) | Embedded submanifolds (Theorem 6.30) |
| Linear algebra | The toolkit of [[§17 Linear Algebra Toolkit\|§17]], including the pairing theorem (Theorem [[§17 Linear Algebra Toolkit#^thm-17-5\|§17.5]]) | Appendix B; dual spaces in Chapter 11 |

## A.3 Chapter map

| These notes | Lee |
|---|---|
| [[§1 Point-Set Topology Review\|§1]] Point-set review | Appendix A, *Topological Spaces* and *Connectedness and Compactness* |
| [[§2 Topological Manifolds\|§2]] Topological manifolds | Chapter 1, *Topological Manifolds*; Problems 1-1 and 1-2 |
| [[§3 Subspaces and Products\|§3]]–[[§6 Open Quotients and Complex Projective Space\|§6]] Subspaces, products, quotients | Appendix A, *Subspaces, Products, Disjoint Unions, and Quotients*; Problem 1-9 |
| [[§7 The Regular Value Theorem\|§7]] Regular value theorem | Appendix C (Theorem C.40); Example 1.32; Corollary 5.14 |
| [[§8 Topological Groups and Classical Matrix Groups\|§8]]–[[§9 The Classical Groups Are Topological Manifolds\|§9]] Topological and matrix groups | Chapter 7, Examples 7.27–7.30; Propositions 21.34 and 21.35; Problem 7-4 |
| [[§10 Group Actions and Orbit Spaces\|§10]] Actions and orbit spaces | Chapter 7, *Group Actions and Equivariant Maps*; Lemma 21.1, Proposition 21.4 |
| [[§11 Homogeneous Spaces\|§11]]–[[§12 The Topology of G∕H and Real Grassmannians\|§12]] Homogeneous spaces | Theorems 21.17–21.20; Examples 1.36 and 21.21 |
| [[§13 Differentiable Structures\|§13]]–[[§15 Smooth Functions and Smooth Maps\|§15]] Differentiable structures | Chapter 1, *Smooth Structures*, Examples 1.22–1.34; Chapter 2 |
| [[§16 Manifolds in Euclidean Space\|§16]] Manifolds in Euclidean space | Example 1.32; Chapter 5 |
| [[§17 Linear Algebra Toolkit\|§17]]–[[§19 The Orthogonal and Unitary Groups as Smooth Manifolds\|§19]] Vector spaces and matrix groups | Appendix B; Chapter 11 (dual spaces); Example 1.24; Examples 7.27 and 7.29 |
| [[§20 Tangent Spaces I꞉ The Geometric Picture\|§20]]–[[§21 Transversality\|§21]] Tangent spaces I: geometric | Propositions 3.2, 5.37 and 5.38; Theorem 6.30 |
| [[§22 Tangent Spaces II꞉ Germs\|§22]]–[[§26 Tangent Vectors as Velocities of Curves\|§26]] Tangent spaces II: abstract | Chapter 3 throughout, including Proposition 3.14 (products) |
| [[§27 Tangent Spaces III꞉ The Cotangent Space\|§27]] Tangent spaces III: cotangent | Chapter 11, *Covectors*; Problem 11-4 for $I_p/I_p^2$ |
| [[§28 Local Diffeomorphisms and Submersions\|§28]] Local diffeomorphisms, submersions | Chapter 4 (Propositions 4.1 and 4.28, Theorem 4.12); Theorem C.34 |
| [[§29 Submanifolds\|§29]] Submanifolds | Chapter 5, *Embedded Submanifolds* (Theorem 5.8, Corollary 5.14, Propositions 5.35–5.38) |
| [[§30 Fibrations\|§30]] Fibrations | smooth fiber bundles (Chapter 10); Ehresmann's theorem is not in Lee |
| [[§31 The Tangent Bundle\|§31]] The tangent bundle | Chapter 3, *The Tangent Bundle* (Lemma 1.35, Proposition 3.18); Proposition 11.9 (cotangent bundle); Chapter 8 (vector fields); Chapter 10 (sections) |
| [[§32 Immersions\|§32]] Immersions | Chapter 4, *Immersions* (Theorem 4.12); Example 4.19 |

## A.4 Index from Lee to these notes

Every numbered result of Lee's cited in these notes, in Lee's order, with the boxes that correspond to it. The table is generated from the *Lee:* lines in the boxes, so the two always agree.

| Lee | These notes |
|---|---|
| Theorem 1.2 | [[§2 Topological Manifolds#^thm-2-1\|Thm. §2.1]], [[§2 Topological Manifolds#^cor-2-2\|Cor. §2.2]] |
| Example 1.4 | [[§2 Topological Manifolds#^ex-2-4\|Ex. §2.4]], [[§2 Topological Manifolds#^prop-2-7\|Prop. §2.7]], [[§13 Differentiable Structures#^ex-13-2\|Ex. §13.2]] |
| Example 1.5 | [[§14 Projective Spaces as Smooth Manifolds#^prop-14-6\|Prop. §14.6]] |
| Example 1.8 | [[§3 Subspaces and Products#^thm-3-12\|Thm. §3.12]] |
| Proposition 1.11 | [[§2 Topological Manifolds#^prop-2-6\|Prop. §2.6]], [[§2 Topological Manifolds#^thm-2-9\|Thm. §2.9]], [[§2 Topological Manifolds#^cor-2-10\|Cor. §2.10]] |
| Proposition 1.17 | [[§13 Differentiable Structures#^def-13-7\|Def. §13.7]], [[§13 Differentiable Structures#^thm-13-5\|Thm. §13.5]] |
| Example 1.21 | [[§2 Topological Manifolds#^prop-2-5\|Prop. §2.5]] |
| Example 1.22 | [[§13 Differentiable Structures#^ex-13-1\|Ex. §13.1]] |
| Example 1.23 | [[§15 Smooth Functions and Smooth Maps#^ex-15-1\|Ex. §15.1]], [[§15 Smooth Functions and Smooth Maps#^cor-15-7\|Cor. §15.7]], [[§15 Smooth Functions and Smooth Maps#^ex-15-2\|Ex. §15.2]] |
| Example 1.24 | [[§18 The Differential of a Map Between Vector Spaces#^def-18-1\|Def. §18.1]], [[§18 The Differential of a Map Between Vector Spaces#^prop-18-2\|Prop. §18.2]], [[§18 The Differential of a Map Between Vector Spaces#^def-18-3\|Def. §18.3]] |
| Example 1.25 | [[§8 Topological Groups and Classical Matrix Groups#^def-8-2\|Def. §8.2]] |
| Example 1.26 | [[§3 Subspaces and Products#^prop-3-6\|Prop. §3.6]], [[§3 Subspaces and Products#^def-3-2\|Def. §3.2]] |
| Example 1.27 | [[§8 Topological Groups and Classical Matrix Groups#^def-8-4\|Def. §8.4]], [[§8 Topological Groups and Classical Matrix Groups#^prop-8-4\|Prop. §8.4]], [[§9 The Classical Groups Are Topological Manifolds#^thm-9-6\|Thm. §9.6]] |
| Example 1.31 | [[§13 Differentiable Structures#^ex-13-2\|Ex. §13.2]] |
| Example 1.32 | [[§7 The Regular Value Theorem#^thm-7-3\|Thm. §7.3]], [[§16 Manifolds in Euclidean Space#^prop-16-2\|Prop. §16.2]] |
| Example 1.33 | [[§14 Projective Spaces as Smooth Manifolds#^cor-14-5\|Cor. §14.5]], [[§14 Projective Spaces as Smooth Manifolds#^prop-14-6\|Prop. §14.6]] |
| Example 1.34 | [[§15 Smooth Functions and Smooth Maps#^prop-15-8\|Prop. §15.8]] |
| Lemma 1.35 | [[§31 The Tangent Bundle#^prop-31-1\|Prop. §31.1]] |
| Example 1.36 | [[§12 The Topology of G∕H and Real Grassmannians#^def-12-3\|Def. §12.3]], [[§12 The Topology of G∕H and Real Grassmannians#^cor-12-8\|Cor. §12.8]] |
| Problem 1-1 | [[§1 Point-Set Topology Review#^ex-1-4\|Ex. §1.4]], [[§2 Topological Manifolds#^prop-2-4\|Prop. §2.4]], [[§4 Quotient Spaces and Open Maps#^ex-4-1\|Ex. §4.1]] |
| Problem 1-2 | [[§2 Topological Manifolds#^prop-2-4\|Prop. §2.4]], [[§2 Topological Manifolds#^ex-2-3\|Ex. §2.3]] |
| Problem 1-6 | [[§15 Smooth Functions and Smooth Maps#^prop-15-6\|Prop. §15.6]], [[§15 Smooth Functions and Smooth Maps#^def-15-5\|Def. §15.5]], [[§15 Smooth Functions and Smooth Maps#^cor-15-7\|Cor. §15.7]] |
| Problem 1-7 | [[§13 Differentiable Structures#^ex-13-3\|Ex. §13.3]] |
| Problem 1-9 | [[§6 Open Quotients and Complex Projective Space#^def-6-2\|Def. §6.2]], [[§6 Open Quotients and Complex Projective Space#^prop-6-4\|Prop. §6.4]], [[§6 Open Quotients and Complex Projective Space#^prop-6-5\|Prop. §6.5]], [[§6 Open Quotients and Complex Projective Space#^prop-6-6\|Prop. §6.6]], [[§10 Group Actions and Orbit Spaces#^ex-10-3\|Ex. §10.3]], [[§14 Projective Spaces as Smooth Manifolds#^def-14-1\|Def. §14.1]], [[§14 Projective Spaces as Smooth Manifolds#^def-14-2\|Def. §14.2]], [[§14 Projective Spaces as Smooth Manifolds#^prop-14-1\|Prop. §14.1]], [[§14 Projective Spaces as Smooth Manifolds#^thm-14-2\|Thm. §14.2]] |
| Proposition 2.5 | [[§15 Smooth Functions and Smooth Maps#^prop-15-2\|Prop. §15.2]] |
| Proposition 2.10 | [[§15 Smooth Functions and Smooth Maps#^lem-15-4\|Lem. §15.4]] |
| Proposition 2.15 | [[§15 Smooth Functions and Smooth Maps#^prop-15-5\|Prop. §15.5]] |
| Proposition 2.25 | [[§23 Derivations and the Abstract Tangent Space#^prop-23-3\|Prop. §23.3]] |
| Lemma 3.1 | [[§23 Derivations and the Abstract Tangent Space#^lem-23-2\|Lem. §23.2]] |
| Proposition 3.2 | [[§22 Tangent Spaces II꞉ Germs#^def-22-1\|Def. §22.1]], [[§22 Tangent Spaces II꞉ Germs#^prop-22-2\|Prop. §22.2]], [[§24 Coordinate Derivations and the Basis Theorem#^thm-24-6\|Thm. §24.6]], [[§24 Coordinate Derivations and the Basis Theorem#^lem-24-2\|Lem. §24.2]], [[§24 Coordinate Derivations and the Basis Theorem#^cor-24-4\|Cor. §24.4]] |
| Corollary 3.3 | [[§24 Coordinate Derivations and the Basis Theorem#^thm-24-5\|Thm. §24.5]], [[§24 Coordinate Derivations and the Basis Theorem#^cor-24-4\|Cor. §24.4]], [[§25 The Differential in Coordinates#^prop-25-5\|Prop. §25.5]] |
| Lemma 3.4 | [[§23 Derivations and the Abstract Tangent Space#^lem-23-2\|Lem. §23.2]] |
| Proposition 3.6 | [[§23 Derivations and the Abstract Tangent Space#^thm-23-6\|Thm. §23.6]], [[§23 Derivations and the Abstract Tangent Space#^cor-23-7\|Cor. §23.7]] |
| Proposition 3.8 | [[§23 Derivations and the Abstract Tangent Space#^prop-23-3\|Prop. §23.3]] |
| Proposition 3.9 | [[§23 Derivations and the Abstract Tangent Space#^lem-23-8\|Lem. §23.8]] |
| Proposition 3.10 | [[§24 Coordinate Derivations and the Basis Theorem#^cor-24-7\|Cor. §24.7]] |
| Proposition 3.13 | [[§25 The Differential in Coordinates#^prop-25-5\|Prop. §25.5]], [[§25 The Differential in Coordinates#^cor-25-6\|Cor. §25.6]] |
| Proposition 3.14 | [[§26 Tangent Vectors as Velocities of Curves#^thm-26-4\|Thm. §26.4]], [[§26 Tangent Vectors as Velocities of Curves#^cor-26-5\|Cor. §26.5]], [[§28 Local Diffeomorphisms and Submersions#^ex-28-4\|Ex. §28.4]] |
| Proposition 3.15 | [[§24 Coordinate Derivations and the Basis Theorem#^thm-24-5\|Thm. §24.5]] |
| Proposition 3.18 | [[§31 The Tangent Bundle#^prop-31-4\|Prop. §31.4]], [[§31 The Tangent Bundle#^def-31-2\|Def. §31.2]], [[§31 The Tangent Bundle#^prop-31-1\|Prop. §31.1]], [[§31 The Tangent Bundle#^prop-31-2\|Prop. §31.2]] |
| Proposition 3.23 | [[§26 Tangent Vectors as Velocities of Curves#^thm-26-2\|Thm. §26.2]] |
| Proposition 3.24 | [[§26 Tangent Vectors as Velocities of Curves#^cor-26-3\|Cor. §26.3]] |
| Corollary 3.25 | [[§18 The Differential of a Map Between Vector Spaces#^thm-18-3\|Thm. §18.3]], [[§26 Tangent Vectors as Velocities of Curves#^cor-26-3\|Cor. §26.3]] |
| Proposition 4.1 | [[§28 Local Diffeomorphisms and Submersions#^cor-28-8\|Cor. §28.8]] |
| Theorem 4.5 | [[§28 Local Diffeomorphisms and Submersions#^thm-28-2\|Thm. §28.2]] |
| Proposition 4.6 | [[§28 Local Diffeomorphisms and Submersions#^cor-28-3\|Cor. §28.3]] |
| Proposition 4.8 | [[§28 Local Diffeomorphisms and Submersions#^thm-28-2\|Thm. §28.2]], [[§28 Local Diffeomorphisms and Submersions#^prop-28-4\|Prop. §28.4]] |
| Theorem 4.12 | [[§28 Local Diffeomorphisms and Submersions#^thm-28-7\|Thm. §28.7]], [[§32 Immersions#^thm-32-1\|Thm. §32.1]] |
| Proposition 4.28 | [[§28 Local Diffeomorphisms and Submersions#^cor-28-9\|Cor. §28.9]] |
| Problem 4-5 | [[§14 Projective Spaces as Smooth Manifolds#^prop-14-4\|Prop. §14.4]], [[§28 Local Diffeomorphisms and Submersions#^ex-28-5\|Ex. §28.5]], [[§30 Fibrations#^ex-30-1\|Ex. §30.1]] |
| Theorem 5.8 | [[§29 Submanifolds#^def-29-1\|Def. §29.1]], [[§29 Submanifolds#^prop-29-2\|Prop. §29.2]] |
| Corollary 5.14 | [[§7 The Regular Value Theorem#^thm-7-3\|Thm. §7.3]], [[§16 Manifolds in Euclidean Space#^prop-16-2\|Prop. §16.2]], [[§29 Submanifolds#^thm-29-6\|Thm. §29.6]] |
| Corollary 5.30 | [[§29 Submanifolds#^lem-29-3\|Lem. §29.3]] |
| Proposition 5.35 | [[§29 Submanifolds#^prop-29-4\|Prop. §29.4]] |
| Proposition 5.37 | [[§20 Tangent Spaces I꞉ The Geometric Picture#^def-20-1\|Def. §20.1]], [[§20 Tangent Spaces I꞉ The Geometric Picture#^cor-20-4\|Cor. §20.4]], [[§24 Coordinate Derivations and the Basis Theorem#^thm-24-6\|Thm. §24.6]], [[§29 Submanifolds#^prop-29-4\|Prop. §29.4]] |
| Proposition 5.38 | [[§20 Tangent Spaces I꞉ The Geometric Picture#^thm-20-3\|Thm. §20.3]], [[§20 Tangent Spaces I꞉ The Geometric Picture#^cor-20-4\|Cor. §20.4]], [[§24 Coordinate Derivations and the Basis Theorem#^thm-24-6\|Thm. §24.6]], [[§29 Submanifolds#^thm-29-6\|Thm. §29.6]] |
| Theorem 6.30 | [[§21 Transversality#^thm-21-1\|Thm. §21.1]], [[§21 Transversality#^def-21-3\|Def. §21.3]], [[§21 Transversality#^prop-21-4\|Prop. §21.4]] |
| Example 7.3 | [[§8 Topological Groups and Classical Matrix Groups#^prop-8-4\|Prop. §8.4]] |
| Proposition 7.26 | [[§11 Homogeneous Spaces#^def-11-3\|Def. §11.3]] |
| Example 7.27 | [[§8 Topological Groups and Classical Matrix Groups#^prop-8-7\|Prop. §8.7]], [[§9 The Classical Groups Are Topological Manifolds#^thm-9-6\|Thm. §9.6]], [[§19 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-19-1\|Ex. §19.1]], [[§19 The Orthogonal and Unitary Groups as Smooth Manifolds#^cor-19-2\|Cor. §19.2]], [[§20 Tangent Spaces I꞉ The Geometric Picture#^thm-20-5\|Thm. §20.5]] |
| Example 7.28 | [[§9 The Classical Groups Are Topological Manifolds#^thm-9-6\|Thm. §9.6]], [[§20 Tangent Spaces I꞉ The Geometric Picture#^thm-20-5\|Thm. §20.5]] |
| Example 7.29 | [[§8 Topological Groups and Classical Matrix Groups#^def-8-8\|Def. §8.8]], [[§9 The Classical Groups Are Topological Manifolds#^thm-9-6\|Thm. §9.6]], [[§19 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-19-2\|Ex. §19.2]], [[§19 The Orthogonal and Unitary Groups as Smooth Manifolds#^cor-19-5\|Cor. §19.5]], [[§20 Tangent Spaces I꞉ The Geometric Picture#^thm-20-5\|Thm. §20.5]] |
| Example 7.30 | [[§8 Topological Groups and Classical Matrix Groups#^def-8-8\|Def. §8.8]], [[§9 The Classical Groups Are Topological Manifolds#^thm-9-6\|Thm. §9.6]], [[§20 Tangent Spaces I꞉ The Geometric Picture#^thm-20-5\|Thm. §20.5]] |
| Problem 7-4 | [[§9 The Classical Groups Are Topological Manifolds#^prop-9-1\|Prop. §9.1]], [[§9 The Classical Groups Are Topological Manifolds#^cor-9-2\|Cor. §9.2]] |
| Example 10.3 | [[§30 Fibrations#^ex-30-3\|Ex. §30.3]] |
| Proposition 11.1 | [[§17 Linear Algebra Toolkit#^def-17-1\|Def. §17.1]], [[§17 Linear Algebra Toolkit#^prop-17-2\|Prop. §17.2]] |
| Proposition 11.4 | [[§17 Linear Algebra Toolkit#^def-17-2\|Def. §17.2]], [[§17 Linear Algebra Toolkit#^prop-17-4\|Prop. §17.4]] |
| Proposition 11.8 | [[§17 Linear Algebra Toolkit#^prop-17-3\|Prop. §17.3]] |
| Proposition 11.9 | [[§31 The Tangent Bundle#^def-31-5\|Def. §31.5]], [[§31 The Tangent Bundle#^prop-31-5\|Prop. §31.5]] |
| Proposition 11.20 | [[§27 Tangent Spaces III꞉ The Cotangent Space#^cor-27-3\|Cor. §27.3]] |
| Problem 11-4 | [[§23 Derivations and the Abstract Tangent Space#^def-23-3\|Def. §23.3]], [[§27 Tangent Spaces III꞉ The Cotangent Space#^prop-27-4\|Prop. §27.4]], [[§27 Tangent Spaces III꞉ The Cotangent Space#^prop-27-5\|Prop. §27.5]], [[§27 Tangent Spaces III꞉ The Cotangent Space#^thm-27-7\|Thm. §27.7]] |
| Theorem 17.26 | [[§2 Topological Manifolds#^thm-2-1\|Thm. §2.1]] |
| Lemma 21.1 | [[§10 Group Actions and Orbit Spaces#^lem-10-2\|Lem. §10.2]], [[§10 Group Actions and Orbit Spaces#^lem-10-3\|Lem. §10.3]], [[§12 The Topology of G∕H and Real Grassmannians#^prop-12-1\|Prop. §12.1]] |
| Example 21.3 | [[§10 Group Actions and Orbit Spaces#^ex-10-6\|Ex. §10.6]] |
| Proposition 21.4 | [[§10 Group Actions and Orbit Spaces#^def-10-4\|Def. §10.4]], [[§10 Group Actions and Orbit Spaces#^cor-10-4\|Cor. §10.4]], [[§10 Group Actions and Orbit Spaces#^thm-10-5\|Thm. §10.5]] |
| Corollary 21.6 | [[§10 Group Actions and Orbit Spaces#^cor-10-4\|Cor. §10.4]], [[§10 Group Actions and Orbit Spaces#^thm-10-5\|Thm. §10.5]] |
| Example 21.14 | [[§12 The Topology of G∕H and Real Grassmannians#^ex-12-1\|Ex. §12.1]] |
| Example 21.15 | [[§11 Homogeneous Spaces#^def-11-1\|Def. §11.1]], [[§11 Homogeneous Spaces#^ex-11-3\|Ex. §11.3]] |
| Theorem 21.17 | [[§11 Homogeneous Spaces#^def-11-4\|Def. §11.4]], [[§11 Homogeneous Spaces#^lem-11-3\|Lem. §11.3]], [[§11 Homogeneous Spaces#^def-11-5\|Def. §11.5]], [[§11 Homogeneous Spaces#^prop-11-4\|Prop. §11.4]], [[§12 The Topology of G∕H and Real Grassmannians#^def-12-1\|Def. §12.1]], [[§12 The Topology of G∕H and Real Grassmannians#^prop-12-1\|Prop. §12.1]], [[§12 The Topology of G∕H and Real Grassmannians#^cor-12-2\|Cor. §12.2]], [[§12 The Topology of G∕H and Real Grassmannians#^cor-12-5\|Cor. §12.5]] |
| Theorem 21.18 | [[§11 Homogeneous Spaces#^thm-11-2\|Thm. §11.2]], [[§11 Homogeneous Spaces#^lem-11-5\|Lem. §11.5]], [[§12 The Topology of G∕H and Real Grassmannians#^thm-12-3\|Thm. §12.3]] |
| Example 21.19 | [[§11 Homogeneous Spaces#^ex-11-3\|Ex. §11.3]] |
| Theorem 21.20 | [[§12 The Topology of G∕H and Real Grassmannians#^def-12-2\|Def. §12.2]], [[§12 The Topology of G∕H and Real Grassmannians#^prop-12-4\|Prop. §12.4]] |
| Example 21.21 | [[§12 The Topology of G∕H and Real Grassmannians#^prop-12-6\|Prop. §12.6]], [[§12 The Topology of G∕H and Real Grassmannians#^prop-12-7\|Prop. §12.7]], [[§12 The Topology of G∕H and Real Grassmannians#^cor-12-8\|Cor. §12.8]] |
| Proposition 21.34 | [[§8 Topological Groups and Classical Matrix Groups#^thm-8-6\|Thm. §8.6]] |
| Proposition 21.35 | [[§8 Topological Groups and Classical Matrix Groups#^prop-8-5\|Prop. §8.5]], [[§8 Topological Groups and Classical Matrix Groups#^thm-8-6\|Thm. §8.6]] |
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
| Corollary B.21 | [[§17 Linear Algebra Toolkit#^prop-17-1\|Prop. §17.1]] |
| Proposition B.24 | [[§17 Linear Algebra Toolkit#^prop-17-1\|Prop. §17.1]] |
| Theorem C.15 | [[§24 Coordinate Derivations and the Basis Theorem#^lem-24-2\|Lem. §24.2]], [[§24 Coordinate Derivations and the Basis Theorem#^lem-24-3\|Lem. §24.3]] |
| Theorem C.34 | [[§28 Local Diffeomorphisms and Submersions#^thm-28-1\|Thm. §28.1]] |
| Example C.37 | [[§25 The Differential in Coordinates#^ex-25-1\|Ex. §25.1]] |
| Theorem C.40 | [[§7 The Regular Value Theorem#^thm-7-1\|Thm. §7.1]], [[§7 The Regular Value Theorem#^cor-7-2\|Cor. §7.2]] |
