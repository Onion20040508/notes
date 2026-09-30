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
| $T_pM$: derivations of germs $C_p^\infty(M)$ | $T_pM$: derivations of $C^\infty(M)$ at $p$ | Isomorphic, by Proposition [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^prop-12-7\|§12.7]]; Lee's version needs bump functions. |
| $T^{\mathrm{geo}}_pM$, the geometric tangent space | $\mathbb{R}^n_a$ in $\mathbb{R}^n$; $T_pS \subseteq T_pM$ for embedded $S$ | Theorem [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^thm-12-8\|§12.8]]; Lee, Propositions 3.2 and 5.38. |
| $F_{*p}$ | $dF_p$ | The notes keep $dF_p$ for the vector-space differential (Definition [[§10 Vector Spaces and Matrix Groups#^def-10-9\|§10.9]]) and $df_p$ for functions. |
| $D_\gamma$, the velocity | $\gamma'(0)$ | The notes keep $\gamma'(0)$ for the ordinary derivative of a curve in $\mathbb{R}^N$, a geometric vector (Definition [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^def-12-14\|§12.14]]). |
| $D_v$, $D_v\vert_a$ | $D_v\vert_a$ | The directional derivative (Definition [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^def-12-1\|§12.1]]). |
| $[f] \in C_p^\infty(M)$, germs | — | Lee works with global functions $C^\infty(M)$ (Definition [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^def-12-3\|§12.3]]). |
| $f_\varphi = f \circ \varphi^{-1}$, $\tilde F = \psi \circ F \circ \varphi^{-1}$ | $\hat f$, $\widehat F$ | Coordinate representations (Definition [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^def-12-11\|§12.11]]). |
| $\sum_i a^i\, \partial/\partial x^i\vert_p$ | $a^i\, \partial/\partial x^i\vert_p$ | Lee uses the Einstein summation convention; the notes always write the sum. |
| $T_p^*M$, $df_p$, $dx^i\vert_p$ | the same | Definition [[§13 Tangent Spaces III꞉ The Cotangent Space#^def-13-1\|§13.1]], Lemma [[§13 Tangent Spaces III꞉ The Cotangent Space#^lem-13-2\|§13.2]]. |
| $I_p$, $I_p^2$, $I_p/I_p^2$, of germs | $I_p$, $I_p^2$ of global functions (Problem 11-4) | Theorem [[§13 Tangent Spaces III꞉ The Cotangent Space#^thm-13-7\|§13.7]]; Lee's version needs bump functions. |
| $\Gamma = \{(x, g \cdot x)\}$, the orbit relation | $\mathcal{O} = \{(g \cdot p, p)\}$ | The same set with the factors swapped (proof of Lee, Proposition 21.4). |
| $H_{x_0}$, the isotropy group | $G_p$ | Definition [[§7 Homogeneous Spaces#^def-7-2\|§7.2]]. |
| $\Phi : G/H \to X$, $gH \mapsto g \cdot x_0$ | $F : G/G_p \to M$ | Theorem [[§7 Homogeneous Spaces#^thm-7-8\|§7.8]]; Lee, Theorem 21.18. |
| $\mathfrak{g} = T^{\mathrm{geo}}_I G$ | $\mathrm{Lie}(G) \cong T_eG$ | The notes' $\mathfrak{g}$ is the geometric tangent space at $I$; Lee defines $\mathrm{Lie}(G)$ by left-invariant vector fields (Chapter 8). |
| $\widetilde{\mathbb{R}}$: the chart $\sqrt[3]{x}$ | Example 1.23: the chart $x^3$ | Two different non-standard structures — the transition map between them is $y \mapsto y^9$ — both diffeomorphic to $\mathbb{R}$ (Corollary [[§8 Differentiable Structures#^cor-8-18\|§8.18]]). |

## A.2 Where the routes diverge

Each row is expanded in a **Comparison with Lee** paragraph at the place indicated.

| Topic | These notes | Lee |
|---|---|---|
| Hausdorff quotients | One criterion for all open quotients (Theorems [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^thm-3-26\|§3.26]] and [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^thm-3-28\|§3.28]]), reused for orbit and coset spaces | Checked example by example (Example 1.5, Problem 1-9) |
| Regular level sets | Implicit function theorem, topological first (Theorem [[§4 The Regular Value Theorem#^thm-4-3\|§4.3]]), smooth afterwards (Proposition [[§9 Manifolds in Euclidean Space#^prop-9-2\|§9.2]]) | Example 1.32 for one function; Corollary 5.14 via the constant-rank theorem |
| Hausdorff orbit spaces | Compact group on a Hausdorff space, purely topological (Theorem [[§6 Group Actions and Orbit Spaces#^thm-6-5\|§6.5]]) | Proper actions of Lie groups (Proposition 21.4, Corollary 21.6) |
| Homogeneous spaces | $G/H$ compact and $X$ Hausdorff (Theorem [[§7 Homogeneous Spaces#^thm-7-8\|§7.8]]); the hypothesis is needed (Example [[§7 Homogeneous Spaces#^ex-7-5\|§7.5]]) | Smooth version, no compactness (Theorem 21.18) |
| Tangent vectors | Derivations of germs; locality is built in, and no bump functions are needed | Derivations of $C^\infty(M)$; locality from bump functions (Proposition 3.8) |
| Order of ideas | Geometric first, $T^{\mathrm{geo}}_pM = \ker F'(p)$ (Theorem [[§11 Tangent Spaces I꞉ The Geometric Picture#^thm-11-3\|§11.3]]), then derivations | Derivations first; $T_pS = \ker d\Phi_p$ later (Proposition 5.38) |
| Cotangent space | The dual, and also $I_p/I_p^2$ of germs, via a non-degenerate pairing (Theorem [[§13 Tangent Spaces III꞉ The Cotangent Space#^thm-13-7\|§13.7]]) | The dual in the text (Chapter 11); $I_p/I_p^2$ of global functions, via $f \mapsto df_p$, as Problem 11-4 |
| Transversality | Level sets in Euclidean space (Theorem [[§11 Tangent Spaces I꞉ The Geometric Picture#^thm-11-7\|§11.7]]) | Embedded submanifolds (Theorem 6.30) |
| Linear algebra | The toolkit of [[§10 Vector Spaces and Matrix Groups\|§10]], including the pairing theorem (Theorem [[§10 Vector Spaces and Matrix Groups#^thm-10-5\|§10.5]]) | Appendix B; dual spaces in Chapter 11 |

## A.3 Chapter map

| These notes | Lee |
|---|---|
| [[§1 Point-Set Topology Review\|§1]] Point-set review | Appendix A, *Topological Spaces* and *Connectedness and Compactness* |
| [[§2 Topological Manifolds\|§2]] Topological manifolds | Chapter 1, *Topological Manifolds*; Problems 1-1 and 1-2 |
| [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients\|§3]] Subspaces, products, quotients | Appendix A, *Subspaces, Products, Disjoint Unions, and Quotients*; Problem 1-9 |
| [[§4 The Regular Value Theorem\|§4]] Regular value theorem | Appendix C (Theorem C.40); Example 1.32; Corollary 5.14 |
| [[§5 Topological Groups and Classical Matrix Groups\|§5]] Topological and matrix groups | Chapter 7, Examples 7.27–7.30; Propositions 21.34 and 21.35; Problem 7-4 |
| [[§6 Group Actions and Orbit Spaces\|§6]] Actions and orbit spaces | Chapter 7, *Group Actions and Equivariant Maps*; Lemma 21.1, Proposition 21.4 |
| [[§7 Homogeneous Spaces\|§7]] Homogeneous spaces | Theorems 21.17–21.20; Examples 1.36 and 21.21 |
| [[§8 Differentiable Structures\|§8]] Differentiable structures | Chapter 1, *Smooth Structures*, Examples 1.22–1.34; Chapter 2 |
| [[§9 Manifolds in Euclidean Space\|§9]] Manifolds in Euclidean space | Example 1.32; Chapter 5 |
| [[§10 Vector Spaces and Matrix Groups\|§10]] Vector spaces and matrix groups | Appendix B; Chapter 11 (dual spaces); Example 1.24; Examples 7.27 and 7.29 |
| [[§11 Tangent Spaces I꞉ The Geometric Picture\|§11]] Tangent spaces I: geometric | Propositions 3.2, 5.37 and 5.38; Theorem 6.30 |
| [[§12 Tangent Spaces II꞉ The Abstract Tangent Space\|§12]] Tangent spaces II: abstract | Chapter 3 throughout, including Proposition 3.14 (products) |
| [[§13 Tangent Spaces III꞉ The Cotangent Space\|§13]] Tangent spaces III: cotangent | Chapter 11, *Covectors*; Problem 11-4 for $I_p/I_p^2$ |
| [[§14 Local Diffeomorphisms and Submersions\|§14]] Local diffeomorphisms, submersions | Chapter 4 (Propositions 4.1 and 4.28, Theorem 4.12); Theorem C.34 |
| [[§15 Submanifolds\|§15]] Submanifolds | Chapter 5, *Embedded Submanifolds* (Theorem 5.8, Corollary 5.14, Propositions 5.35–5.38) |
| [[§16 Fibrations\|§16]] Fibrations | smooth fiber bundles (Chapter 10); Ehresmann's theorem is not in Lee |
| [[§17 The Tangent Bundle\|§17]] The tangent bundle | Chapter 3, *The Tangent Bundle* (Lemma 1.35, Proposition 3.18); Proposition 11.9 (cotangent bundle); Chapter 8 (vector fields); Chapter 10 (sections) |
| [[§18 Immersions\|§18]] Immersions | Chapter 4, *Immersions* (Theorem 4.12); Example 4.19 |

## A.4 Index from Lee to these notes

Every numbered result of Lee's cited in these notes, in Lee's order, with the boxes that correspond to it. The table is generated from the *Lee:* lines in the boxes, so the two always agree.

| Lee | These notes |
|---|---|
| Theorem 1.2 | [[§2 Topological Manifolds#^thm-2-1\|Thm. §2.1]], [[§2 Topological Manifolds#^cor-2-2\|Cor. §2.2]] |
| Example 1.4 | [[§2 Topological Manifolds#^ex-2-4\|Ex. §2.4]], [[§2 Topological Manifolds#^prop-2-7\|Prop. §2.7]], [[§8 Differentiable Structures#^ex-8-2\|Ex. §8.2]] |
| Example 1.5 | [[§8 Differentiable Structures#^prop-8-11\|Prop. §8.11]] |
| Example 1.8 | [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^thm-3-12\|Thm. §3.12]] |
| Proposition 1.11 | [[§2 Topological Manifolds#^prop-2-6\|Prop. §2.6]], [[§2 Topological Manifolds#^thm-2-9\|Thm. §2.9]], [[§2 Topological Manifolds#^cor-2-10\|Cor. §2.10]] |
| Proposition 1.17 | [[§8 Differentiable Structures#^def-8-7\|Def. §8.7]], [[§8 Differentiable Structures#^thm-8-5\|Thm. §8.5]] |
| Example 1.21 | [[§2 Topological Manifolds#^prop-2-5\|Prop. §2.5]] |
| Example 1.22 | [[§8 Differentiable Structures#^ex-8-1\|Ex. §8.1]] |
| Example 1.23 | [[§8 Differentiable Structures#^ex-8-5\|Ex. §8.5]], [[§8 Differentiable Structures#^cor-8-18\|Cor. §8.18]], [[§8 Differentiable Structures#^ex-8-6\|Ex. §8.6]] |
| Example 1.24 | [[§10 Vector Spaces and Matrix Groups#^def-10-6\|Def. §10.6]], [[§10 Vector Spaces and Matrix Groups#^prop-10-9\|Prop. §10.9]], [[§10 Vector Spaces and Matrix Groups#^def-10-8\|Def. §10.8]] |
| Example 1.25 | [[§5 Topological Groups and Classical Matrix Groups#^def-5-2\|Def. §5.2]] |
| Example 1.26 | [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^prop-3-6\|Prop. §3.6]], [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^def-3-2\|Def. §3.2]] |
| Example 1.27 | [[§5 Topological Groups and Classical Matrix Groups#^def-5-4\|Def. §5.4]], [[§5 Topological Groups and Classical Matrix Groups#^prop-5-4\|Prop. §5.4]], [[§5 Topological Groups and Classical Matrix Groups#^thm-5-8\|Thm. §5.8]] |
| Example 1.31 | [[§8 Differentiable Structures#^ex-8-2\|Ex. §8.2]] |
| Example 1.32 | [[§4 The Regular Value Theorem#^thm-4-3\|Thm. §4.3]], [[§9 Manifolds in Euclidean Space#^prop-9-2\|Prop. §9.2]] |
| Example 1.33 | [[§8 Differentiable Structures#^cor-8-10\|Cor. §8.10]], [[§8 Differentiable Structures#^prop-8-11\|Prop. §8.11]] |
| Example 1.34 | [[§8 Differentiable Structures#^prop-8-19\|Prop. §8.19]] |
| Lemma 1.35 | [[§17 The Tangent Bundle#^prop-17-2\|Prop. §17.2]] |
| Example 1.36 | [[§7 Homogeneous Spaces#^def-7-8\|Def. §7.8]], [[§7 Homogeneous Spaces#^cor-7-13\|Cor. §7.13]] |
| Problem 1-1 | [[§1 Point-Set Topology Review#^ex-1-4\|Ex. §1.4]], [[§2 Topological Manifolds#^prop-2-4\|Prop. §2.4]], [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^ex-3-1\|Ex. §3.1]] |
| Problem 1-2 | [[§2 Topological Manifolds#^prop-2-4\|Prop. §2.4]], [[§2 Topological Manifolds#^ex-2-3\|Ex. §2.3]] |
| Problem 1-6 | [[§8 Differentiable Structures#^prop-8-17\|Prop. §8.17]], [[§8 Differentiable Structures#^def-8-16\|Def. §8.16]], [[§8 Differentiable Structures#^cor-8-18\|Cor. §8.18]] |
| Problem 1-7 | [[§8 Differentiable Structures#^ex-8-3\|Ex. §8.3]] |
| Problem 1-9 | [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^def-3-11\|Def. §3.11]], [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^prop-3-29\|Prop. §3.29]], [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^prop-3-30\|Prop. §3.30]], [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^prop-3-31\|Prop. §3.31]], [[§6 Group Actions and Orbit Spaces#^ex-6-3\|Ex. §6.3]], [[§8 Differentiable Structures#^def-8-10\|Def. §8.10]], [[§8 Differentiable Structures#^def-8-11\|Def. §8.11]], [[§8 Differentiable Structures#^prop-8-6\|Prop. §8.6]], [[§8 Differentiable Structures#^thm-8-7\|Thm. §8.7]] |
| Proposition 2.5 | [[§8 Differentiable Structures#^prop-8-13\|Prop. §8.13]] |
| Proposition 2.10 | [[§8 Differentiable Structures#^lem-8-15\|Lem. §8.15]] |
| Proposition 2.15 | [[§8 Differentiable Structures#^prop-8-16\|Prop. §8.16]] |
| Proposition 2.25 | [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^prop-12-7\|Prop. §12.7]] |
| Lemma 3.1 | [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^lem-12-6\|Lem. §12.6]] |
| Proposition 3.2 | [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^def-12-1\|Def. §12.1]], [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^prop-12-2\|Prop. §12.2]], [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^thm-12-8\|Thm. §12.8]], [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^lem-12-17\|Lem. §12.17]], [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^cor-12-19\|Cor. §12.19]] |
| Corollary 3.3 | [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^thm-12-16\|Thm. §12.16]], [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^cor-12-19\|Cor. §12.19]], [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^prop-12-25\|Prop. §12.25]] |
| Lemma 3.4 | [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^lem-12-6\|Lem. §12.6]] |
| Proposition 3.6 | [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^thm-12-11\|Thm. §12.11]], [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^cor-12-12\|Cor. §12.12]] |
| Proposition 3.8 | [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^prop-12-7\|Prop. §12.7]] |
| Proposition 3.9 | [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^lem-12-13\|Lem. §12.13]] |
| Proposition 3.10 | [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^cor-12-20\|Cor. §12.20]] |
| Proposition 3.13 | [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^prop-12-25\|Prop. §12.25]], [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^cor-12-26\|Cor. §12.26]] |
| Proposition 3.14 | [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^thm-12-32\|Thm. §12.32]], [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^cor-12-33\|Cor. §12.33]], [[§14 Local Diffeomorphisms and Submersions#^ex-14-4\|Ex. §14.4]] |
| Proposition 3.15 | [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^thm-12-16\|Thm. §12.16]] |
| Proposition 3.18 | [[§17 The Tangent Bundle#^prop-17-1\|Prop. §17.1]], [[§17 The Tangent Bundle#^def-17-2\|Def. §17.2]], [[§17 The Tangent Bundle#^prop-17-2\|Prop. §17.2]], [[§17 The Tangent Bundle#^prop-17-3\|Prop. §17.3]] |
| Proposition 3.23 | [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^thm-12-30\|Thm. §12.30]] |
| Proposition 3.24 | [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^cor-12-31\|Cor. §12.31]] |
| Corollary 3.25 | [[§10 Vector Spaces and Matrix Groups#^thm-10-10\|Thm. §10.10]], [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^cor-12-31\|Cor. §12.31]] |
| Proposition 4.1 | [[§14 Local Diffeomorphisms and Submersions#^cor-14-8\|Cor. §14.8]] |
| Theorem 4.5 | [[§14 Local Diffeomorphisms and Submersions#^thm-14-2\|Thm. §14.2]] |
| Proposition 4.6 | [[§14 Local Diffeomorphisms and Submersions#^cor-14-3\|Cor. §14.3]] |
| Proposition 4.8 | [[§14 Local Diffeomorphisms and Submersions#^thm-14-2\|Thm. §14.2]], [[§14 Local Diffeomorphisms and Submersions#^prop-14-4\|Prop. §14.4]] |
| Theorem 4.12 | [[§14 Local Diffeomorphisms and Submersions#^thm-14-5\|Thm. §14.5]], [[§18 Immersions#^thm-18-1\|Thm. §18.1]] |
| Proposition 4.28 | [[§14 Local Diffeomorphisms and Submersions#^cor-14-9\|Cor. §14.9]] |
| Problem 4-5 | [[§8 Differentiable Structures#^prop-8-9\|Prop. §8.9]], [[§14 Local Diffeomorphisms and Submersions#^ex-14-5\|Ex. §14.5]], [[§16 Fibrations#^ex-16-1\|Ex. §16.1]] |
| Theorem 5.8 | [[§15 Submanifolds#^def-15-1\|Def. §15.1]], [[§15 Submanifolds#^prop-15-2\|Prop. §15.2]] |
| Corollary 5.14 | [[§4 The Regular Value Theorem#^thm-4-3\|Thm. §4.3]], [[§9 Manifolds in Euclidean Space#^prop-9-2\|Prop. §9.2]], [[§15 Submanifolds#^thm-15-6\|Thm. §15.6]] |
| Corollary 5.30 | [[§15 Submanifolds#^lem-15-3\|Lem. §15.3]] |
| Proposition 5.35 | [[§15 Submanifolds#^prop-15-4\|Prop. §15.4]] |
| Proposition 5.37 | [[§11 Tangent Spaces I꞉ The Geometric Picture#^def-11-1\|Def. §11.1]], [[§11 Tangent Spaces I꞉ The Geometric Picture#^cor-11-4\|Cor. §11.4]], [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^thm-12-8\|Thm. §12.8]], [[§15 Submanifolds#^prop-15-4\|Prop. §15.4]] |
| Proposition 5.38 | [[§11 Tangent Spaces I꞉ The Geometric Picture#^thm-11-3\|Thm. §11.3]], [[§11 Tangent Spaces I꞉ The Geometric Picture#^cor-11-4\|Cor. §11.4]], [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^thm-12-8\|Thm. §12.8]], [[§15 Submanifolds#^thm-15-6\|Thm. §15.6]] |
| Theorem 6.30 | [[§11 Tangent Spaces I꞉ The Geometric Picture#^thm-11-7\|Thm. §11.7]], [[§11 Tangent Spaces I꞉ The Geometric Picture#^def-11-6\|Def. §11.6]], [[§11 Tangent Spaces I꞉ The Geometric Picture#^prop-11-10\|Prop. §11.10]] |
| Example 7.3 | [[§5 Topological Groups and Classical Matrix Groups#^prop-5-4\|Prop. §5.4]] |
| Proposition 7.26 | [[§7 Homogeneous Spaces#^def-7-3\|Def. §7.3]] |
| Example 7.27 | [[§5 Topological Groups and Classical Matrix Groups#^prop-5-7\|Prop. §5.7]], [[§5 Topological Groups and Classical Matrix Groups#^thm-5-8\|Thm. §5.8]], [[§10 Vector Spaces and Matrix Groups#^ex-10-1\|Ex. §10.1]], [[§10 Vector Spaces and Matrix Groups#^cor-10-13\|Cor. §10.13]], [[§11 Tangent Spaces I꞉ The Geometric Picture#^thm-11-5\|Thm. §11.5]] |
| Example 7.28 | [[§5 Topological Groups and Classical Matrix Groups#^thm-5-8\|Thm. §5.8]], [[§11 Tangent Spaces I꞉ The Geometric Picture#^thm-11-5\|Thm. §11.5]] |
| Example 7.29 | [[§5 Topological Groups and Classical Matrix Groups#^def-5-8\|Def. §5.8]], [[§5 Topological Groups and Classical Matrix Groups#^thm-5-8\|Thm. §5.8]], [[§10 Vector Spaces and Matrix Groups#^ex-10-2\|Ex. §10.2]], [[§10 Vector Spaces and Matrix Groups#^cor-10-16\|Cor. §10.16]], [[§11 Tangent Spaces I꞉ The Geometric Picture#^thm-11-5\|Thm. §11.5]] |
| Example 7.30 | [[§5 Topological Groups and Classical Matrix Groups#^def-5-8\|Def. §5.8]], [[§5 Topological Groups and Classical Matrix Groups#^thm-5-8\|Thm. §5.8]], [[§11 Tangent Spaces I꞉ The Geometric Picture#^thm-11-5\|Thm. §11.5]] |
| Problem 7-4 | [[§5 Topological Groups and Classical Matrix Groups#^prop-5-9\|Prop. §5.9]], [[§5 Topological Groups and Classical Matrix Groups#^cor-5-10\|Cor. §5.10]] |
| Example 10.3 | [[§16 Fibrations#^ex-16-3\|Ex. §16.3]] |
| Proposition 11.1 | [[§10 Vector Spaces and Matrix Groups#^def-10-1\|Def. §10.1]], [[§10 Vector Spaces and Matrix Groups#^prop-10-2\|Prop. §10.2]] |
| Proposition 11.4 | [[§10 Vector Spaces and Matrix Groups#^def-10-2\|Def. §10.2]], [[§10 Vector Spaces and Matrix Groups#^prop-10-4\|Prop. §10.4]] |
| Proposition 11.8 | [[§10 Vector Spaces and Matrix Groups#^prop-10-3\|Prop. §10.3]] |
| Proposition 11.9 | [[§17 The Tangent Bundle#^def-17-5\|Def. §17.5]], [[§17 The Tangent Bundle#^prop-17-5\|Prop. §17.5]] |
| Proposition 11.20 | [[§13 Tangent Spaces III꞉ The Cotangent Space#^cor-13-3\|Cor. §13.3]] |
| Problem 11-4 | [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^def-12-8\|Def. §12.8]], [[§13 Tangent Spaces III꞉ The Cotangent Space#^prop-13-4\|Prop. §13.4]], [[§13 Tangent Spaces III꞉ The Cotangent Space#^prop-13-5\|Prop. §13.5]], [[§13 Tangent Spaces III꞉ The Cotangent Space#^thm-13-7\|Thm. §13.7]] |
| Theorem 17.26 | [[§2 Topological Manifolds#^thm-2-1\|Thm. §2.1]] |
| Lemma 21.1 | [[§6 Group Actions and Orbit Spaces#^lem-6-2\|Lem. §6.2]], [[§6 Group Actions and Orbit Spaces#^lem-6-3\|Lem. §6.3]], [[§7 Homogeneous Spaces#^prop-7-6\|Prop. §7.6]] |
| Example 21.3 | [[§6 Group Actions and Orbit Spaces#^ex-6-6\|Ex. §6.6]] |
| Proposition 21.4 | [[§6 Group Actions and Orbit Spaces#^def-6-4\|Def. §6.4]], [[§6 Group Actions and Orbit Spaces#^cor-6-4\|Cor. §6.4]], [[§6 Group Actions and Orbit Spaces#^thm-6-5\|Thm. §6.5]] |
| Corollary 21.6 | [[§6 Group Actions and Orbit Spaces#^cor-6-4\|Cor. §6.4]], [[§6 Group Actions and Orbit Spaces#^thm-6-5\|Thm. §6.5]] |
| Example 21.14 | [[§7 Homogeneous Spaces#^ex-7-4\|Ex. §7.4]] |
| Example 21.15 | [[§7 Homogeneous Spaces#^def-7-1\|Def. §7.1]], [[§7 Homogeneous Spaces#^ex-7-3\|Ex. §7.3]] |
| Theorem 21.17 | [[§7 Homogeneous Spaces#^def-7-4\|Def. §7.4]], [[§7 Homogeneous Spaces#^lem-7-3\|Lem. §7.3]], [[§7 Homogeneous Spaces#^def-7-5\|Def. §7.5]], [[§7 Homogeneous Spaces#^prop-7-4\|Prop. §7.4]], [[§7 Homogeneous Spaces#^def-7-6\|Def. §7.6]], [[§7 Homogeneous Spaces#^prop-7-6\|Prop. §7.6]], [[§7 Homogeneous Spaces#^cor-7-7\|Cor. §7.7]], [[§7 Homogeneous Spaces#^cor-7-10\|Cor. §7.10]] |
| Theorem 21.18 | [[§7 Homogeneous Spaces#^thm-7-2\|Thm. §7.2]], [[§7 Homogeneous Spaces#^lem-7-5\|Lem. §7.5]], [[§7 Homogeneous Spaces#^thm-7-8\|Thm. §7.8]] |
| Example 21.19 | [[§7 Homogeneous Spaces#^ex-7-3\|Ex. §7.3]] |
| Theorem 21.20 | [[§7 Homogeneous Spaces#^def-7-7\|Def. §7.7]], [[§7 Homogeneous Spaces#^prop-7-9\|Prop. §7.9]] |
| Example 21.21 | [[§7 Homogeneous Spaces#^prop-7-11\|Prop. §7.11]], [[§7 Homogeneous Spaces#^prop-7-12\|Prop. §7.12]], [[§7 Homogeneous Spaces#^cor-7-13\|Cor. §7.13]] |
| Proposition 21.34 | [[§5 Topological Groups and Classical Matrix Groups#^thm-5-6\|Thm. §5.6]] |
| Proposition 21.35 | [[§5 Topological Groups and Classical Matrix Groups#^prop-5-5\|Prop. §5.5]], [[§5 Topological Groups and Classical Matrix Groups#^thm-5-6\|Thm. §5.6]] |
| Example A.4 | [[§1 Point-Set Topology Review#^ex-1-2\|Ex. §1.2]] |
| Example A.5 | [[§1 Point-Set Topology Review#^ex-1-3\|Ex. §1.3]], [[§1 Point-Set Topology Review#^prop-1-6\|Prop. §1.6]] |
| Proposition A.17 | [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^prop-3-3\|Prop. §3.3]], [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^cor-3-4\|Cor. §3.4]] |
| Lemma A.19 | [[§1 Point-Set Topology Review#^prop-1-5\|Prop. §1.5]] |
| Proposition A.23 | [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^thm-3-10\|Thm. §3.10]], [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^cor-3-11\|Cor. §3.11]] |
| Theorem A.27 | [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^prop-3-16\|Prop. §3.16]], [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^thm-3-18\|Thm. §3.18]], [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^cor-3-20\|Cor. §3.20]], [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^lem-3-24\|Lem. §3.24]], [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^lem-3-25\|Lem. §3.25]] |
| Theorem A.30 | [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^thm-3-18\|Thm. §3.18]], [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^cor-3-19\|Cor. §3.19]] |
| Theorem A.31 | [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^prop-3-21\|Prop. §3.21]] |
| Proposition A.39 | [[§1 Point-Set Topology Review#^prop-1-7\|Prop. §1.7]] |
| Proposition A.41 | [[§1 Point-Set Topology Review#^prop-1-7\|Prop. §1.7]] |
| Proposition A.43 | [[§1 Point-Set Topology Review#^prop-1-7\|Prop. §1.7]] |
| Proposition A.45 | [[§1 Point-Set Topology Review#^prop-1-8\|Prop. §1.8]] |
| Proposition A.50 | [[§1 Point-Set Topology Review#^prop-1-8\|Prop. §1.8]] |
| Lemma A.52 | [[§1 Point-Set Topology Review#^prop-1-8\|Prop. §1.8]] |
| Corollary B.21 | [[§10 Vector Spaces and Matrix Groups#^prop-10-1\|Prop. §10.1]] |
| Proposition B.24 | [[§10 Vector Spaces and Matrix Groups#^prop-10-1\|Prop. §10.1]] |
| Theorem C.15 | [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^lem-12-17\|Lem. §12.17]], [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^lem-12-18\|Lem. §12.18]] |
| Theorem C.34 | [[§14 Local Diffeomorphisms and Submersions#^thm-14-1\|Thm. §14.1]] |
| Example C.37 | [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^ex-12-3\|Ex. §12.3]] |
| Theorem C.40 | [[§4 The Regular Value Theorem#^thm-4-1\|Thm. §4.1]], [[§4 The Regular Value Theorem#^cor-4-2\|Cor. §4.2]] |
