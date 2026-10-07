---
type: subject
discipline: math
course: MATH 591
term: Fall 2026
instructor: Alejandro Uribe
textbook: "Lee, Introduction to Smooth Manifolds (2nd ed.)"
status: current
aliases: ["MATH 591", "Smooth Manifolds", "Introduction to Differentiable Manifolds"]
tags: [subject, differentiable-manifolds]
---
# Differentiable Manifolds

MATH 591, *Introduction to Differentiable Manifolds* (Fall 2026, Alejandro Uribe), a first-year PhD course; text Lee, *Introduction to Smooth Manifolds* (2nd ed.), reference Tu, *An Introduction to Manifolds*. Section numbers §1–§49 are the notes' own; every box ends with its counterpart in Lee (*Lee: …*), and [[Differentiable Manifolds Lee Concordance]] reads the two side by side. [[Differentiable Manifolds Course Log]] records the lectures and the homework. LaTeX source (still being extended during the term): `tex/math591_manifolds_notes.tex`.

## Roadmap
These notes follow the course, and the course builds manifolds in two ways that run as parallel threads. Along the *equations* thread, manifolds are cut out of Euclidean space as level sets: spheres, then $\mathrm{SL}(n,\mathbb{R})$, $\mathrm{O}(n)$, $\mathrm{U}(n)$. Along the *quotients* thread, they are glued together by identifying points: $\mathbb{CP}^n$, orbit spaces, coset spaces $G/H$, Grassmannians. Chapters 1 and 2 develop the two threads side by side, and in Chapters 3 and 4 they part ways over tangent spaces. A manifold built by equations has an ambient space, and its tangent vectors can be taken as velocities inside it (the *geometric* stage). A manifold built by quotients has none, and needs the *abstract* tangent space of derivations. Between them sits a *linear* stage, the linear algebra that both need. The threads meet again in the theorem that the two tangent spaces agree wherever both exist. After that the course turns to maps and what they build. Submersions come first ([[§32 The Cotangent Space|§32]]): their normal form makes the regular value theorem work on any manifold, completing the equations thread in submanifolds ([[§33 Local Diffeomorphisms|§33]]); the submersions that are locally products are the fibrations ([[§34 Submersions|§34]]); and the tangent spaces themselves assemble into one, the tangent bundle ([[§35 Submanifolds|§35]]). Immersions, the maps dual to submersions, begin a new arc ([[§36 Fibrations|§36]]), which leads to embeddings, the immersions whose images are submanifolds ([[§37 Immersions|§37]]).

![[m591-0-1.svg]]
*The roadmap: the equations thread (teal), the quotients thread (violet), the linear stage (orange), and the bundles (blue); arrow labels are the bridges.*

The labels on the arrows are the bridges. The regular value theorem ([[§7 The Regular Value Theorem|§7]]) turns equations into manifolds, and graph charts ([[Regular Level Sets Are Smooth Manifolds|§20.2]]) make them smooth. The differential between vector spaces ([[§21 Linear Algebra Toolkit|§21]]) gives $T^{\mathrm{geo}}_pM = \ker F'(p)$ ([[Geometric Tangent Space Is the Kernel of the Jacobian|§25.3]]). For the quotient-built manifolds, atlases are written down by hand ([[§17 Differentiable Structures|§17]]), and only the abstract tangent space reaches them. The two tangent spaces are identified by $v \mapsto D_v$ ([[Ambient and Abstract Tangent Spaces Agree|§29.6]]); the abstract differential agrees with the Jacobian ([[§30 The Differential in Coordinates#^prop-30-5|§30.5]]), and on any manifold the matrix of $F_{\ast p}$ in coordinates *is* the Jacobian of the coordinate representation ([[Matrix of the Differential|§30.2]]), because partial derivatives upstairs are defined downstairs ([[§30 The Differential in Coordinates#^prop-30-1|§30.1]]); and every abstract tangent vector is a velocity after all ([[Every Tangent Vector Is a Velocity|§31.2]]). At the bottom, the submersion normal form ([[Submersion Normal Form|§34.4]]) proves the regular value theorem for manifolds ([[Regular Value Theorem for Manifolds|§35.6]]), where the equations thread ends; fibrations and the tangent and cotangent spaces follow as bundles ([[§34 Submersions|§34]]–[[§35 Submanifolds|§35]]); and immersions, whose normal form is the twin of the submersion normal form, have images that are locally submanifolds ([[§36 Fibrations|§36]]), and globally so when they are embeddings ([[§37 Immersions|§37]]). Each section opens with a line placing it on this map.

## How the chapters build on each other
Solid arrows: a chapter's proofs rely on the earlier chapter (arrows implied by others are omitted; exact counts are in each chapter note). Dashed arrows labelled "on credit": results used before they are proved (forward references in the notes). Dashed arrows from other subjects: citations of their results, labelled with the number (only arrows with 2 or more citations are drawn).

```mermaid
graph TD
  C1["1 Topological Manifolds"]
  C2["2 Topological Groups and Homogeneous Spaces"]
  C3["3 Smooth Structures"]
  C4["4 Tangent and Cotangent Spaces"]
  C5["5 Maps of Constant Rank and Fibrations"]
  C6["6 Tangent and Cotangent Bundles"]
  C7["7 Vector Fields and Lie Groups"]
  X1["Topology (590)"]
  X2["Multivariable Analysis (452)"]
  X3["Linear Algebra (LADR)"]
  X4["Group Theory (493)"]
  X5["Single Variable Analysis (451)"]
  C1 --> C2
  C2 --> C3
  C3 --> C4
  C4 --> C5
  C5 --> C6
  C6 --> C7
  C2 -.->|on credit| C1
  C3 -.->|on credit| C1
  C3 -.->|on credit| C2
  C4 -.->|on credit| C1
  C4 -.->|on credit| C2
  C5 -.->|on credit| C1
  C5 -.->|on credit| C3
  X4 -.->|9| C2
  X4 -.->|7| C5
  X3 -.->|8| C1
  X3 -.->|18| C2
  X3 -.->|10| C3
  X3 -.->|16| C4
  X3 -.->|15| C5
  X3 -.->|4| C6
  X3 -.->|2| C7
  X2 -.->|5| C1
  X2 -.->|6| C2
  X2 -.->|14| C3
  X2 -.->|11| C4
  X2 -.->|6| C5
  X2 -.->|2| C6
  X5 -.->|3| C4
  X1 -.->|66| C1
  X1 -.->|16| C2
  X1 -.->|21| C3
  X1 -.->|6| C4
  X1 -.->|44| C5
  X1 -.->|3| C6
  X1 -.->|2| C7
```

## Chapters
- [[· 1 Topological Manifolds]]
- [[· 2 Topological Groups and Homogeneous Spaces]]
- [[· 3 Smooth Structures]]
- [[· 4 Tangent and Cotangent Spaces]]
- [[· 5 Maps of Constant Rank and Fibrations]]
- [[· 6 Tangent and Cotangent Bundles]]
- [[· 7 Vector Fields and Lie Groups]]

## Planned topics (syllabus)
Smooth manifolds ✓; tangent and cotangent bundles ✓; vector fields ✓ (§47, as derivations of $C^\infty(M)$; the Lie bracket, §48); one-forms ✓ (§46; differential forms of higher degree to come); submanifolds ✓; immersions/submersions ✓ (immersion normal form stated); Sard's theorem; transversality (in Euclidean space, §26); Lie groups and algebras (begun: Lie groups, left-invariant vector fields and the Lie algebra of a Lie group, §49; classical matrix groups and their tangent spaces at $I$); Stokes' theorem; de Rham cohomology; other topics time permitting.

## Central results
- [[Topological Invariance of Dimension]] (§2.1)
- [[Connected Manifolds Are Path Connected]] (§2.8)
- [[Hausdorff Criterion for Open Quotients]] (§6.1)
- [[Second Countability of Open Quotients]] (§6.3)
- [[Implicit Function Theorem (vector-valued)]] (§7.1)
- [[Regular Value Theorem (Euclidean)]] (§7.3)
- [[ℂPⁿ Is Hausdorff and Second Countable]] (§9.1)
- [[Jacobi's Formula]] (§12.1)
- [[Classical Groups Are Manifolds]] (§12.6)
- [[Orbit Spaces of Compact Groups Are Hausdorff]] (§13.5)
- [[Homogeneous Spaces Are Coset Spaces]] (§15.3)
- [[Unique Maximal Atlas]] (§17.5)
- [[Smoothness Is Chart-Independent]] (§19.2)
- [[Regular Level Sets Are Smooth Manifolds]] (§20.2)
- [[Non-Degenerate Pairings]] (§21.5)
- [[Geometric Tangent Space Is the Kernel of the Jacobian]] (§25.3)
- [[Transverse Preimage Theorem]] (§26.1)
- [[Chain Rule for Differentials]] (§28.6)
- [[Hadamard's Lemma]] (§29.2)
- [[Basis Theorem for Tangent Spaces]] (§29.5)
- [[Ambient and Abstract Tangent Spaces Agree]] (§29.6)
- [[Matrix of the Differential]] (§30.2)
- [[Every Tangent Vector Is a Velocity]] (§31.2)
- [[Cotangent Space from Germs]] (§32.8)
- [[Local Diffeomorphism Criterion]] (§33.2)
- [[Submersion Normal Form]] (§34.4)
- [[Regular Value Theorem for Manifolds]] (§35.6)
- [[Immersion Normal Form]] (§37.1)
- [[Images of Embeddings Are Submanifolds]] (§38.1)
- [[Injective Proper Immersions Are Embeddings]] (§38.5)
- [[SU(2) Is a Double Cover of SO(3)]] (§41.4)
- [[Tangent Bundle Is a Smooth Manifold]] (§44.2)

## Summaries
- [[Differentiable Manifolds Lee Concordance]]: notation, where the course's route differs from Lee's, the chapter map, and every Lee result cited in these notes with its counterpart here.
- [[Differentiable Manifolds Course Log]]: lectures and homework, and where each is in these notes.

## Prerequisites from other subjects
The results from other subjects that this course's proofs and definitions cite most, with the number of citing items. Chapter 1 re-proves much of [[Topology]] (the point-set review, subspaces, products, quotients) and §21 is a linear-algebra toolkit whose home is [[Linear Algebra]] 3E–3F; their Connections callouts point to those homes.

**[[Topology]]**
- [[Heine–Borel Theorem]] (10)
- [[§10 Continuous Functions#^thm-10-4|Theorem §10.4: Rules for Continuous Functions]] (10)
- [[Continuous Image of a Compact Space is Compact]] (7)
- [[Bijection from Compact to Hausdorff is a Homeomorphism]] (5)
- [[Compact Subspace of a Hausdorff Space is Closed]] (5)
- [[§15 Connected Spaces#^def-15-2|Definition §15.2: Connected Space]] (5)
- [[§10 Continuous Functions#^def-10-2|Definition §10.2: Homeomorphism]] (5)
- [[§11 Product Topology on Arbitrary Products#^thm-11-1|Theorem §11.1: Continuity into Product Spaces]] (5)

**[[Multivariable Analysis]]**
- [[Multivariable Chain Rule]] (28)
- [[Inverse Function Theorem (several variables)]] (4)
- [[Polar and spherical coordinates]] (2)
- [[§3 Continuity and Limits of Functions#^thm-3-2|Theorem §3.2: Product of Continuous Functions]] (2)
- [[§8 Algebra of Differentiable Functions#^thm-8-2|Theorem §8.2: Product Rule for Partial Derivatives]] (2)
- [[Schwarz–Clairaut Theorem]] (2)
- [[Implicit Function Theorem]] (1)
- [[§3 Continuity and Limits of Functions#^thm-3-1|Theorem §3.1: Sum and Difference of Continuous Functions]] (1)

**[[Linear Algebra]]**
- [[Fundamental theorem of linear maps]] (8)
- [[§37 Determinants#^ladr-9-49|Theorem 9.49: Determinant is multiplicative]] (7)
- [[Injectivity is equivalent to surjectivity (if dim V = dim W ＜ ∞)]] (6)
- [[Invertible ⟺ nonzero determinant]] (6)
- [[§9 Matrices#^ladr-3-57|Theorem 3.57: Column rank equals row rank]] (4)
- [[§37 Determinants#^ladr-9-56|Theorem 9.56: Determinant of transpose, dual, or adjoint]] (3)
- [[Linear map lemma]] (3)
- [[§37 Determinants#^ladr-9-46|Theorem 9.46: Formula for determinant of a matrix]] (2)

**[[Group Theory]]**
- [[§15 Homomorphisms#^def-15-1|Definition §15.1: Group Homomorphism]] (4)
- [[§4 Subgroups#^def-4-1|Definition §4.1: Subgroup]] (3)
- [[§21 The Sign Homomorphism and the Alternating Group#^cor-21-4|Corollary §21.4: Parity of a Permutation]] (1)
- [[§21 The Sign Homomorphism and the Alternating Group#^thm-21-2|Theorem §21.2: Three Formulas for the Sign]] (1)
- [[§21 The Sign Homomorphism and the Alternating Group#^thm-21-3|Theorem §21.3: The Sign Is a Homomorphism]] (1)
- [[§21 The Sign Homomorphism and the Alternating Group#^thm-21-7|Theorem §21.7: Generators of Sₙ]] (1)
- [[§24 Equivalence Relations and Partitions#^prop-24-1|Proposition §24.1: Equivalence Classes Partition a Set]] (1)
- [[§28 Left and Right Cosets#^def-28-2|Definition §28.2: Left and Right Cosets]] (1)

**[[Single Variable Analysis]]**
- [[§28 Basic Properties of the Derivative#^thm-28-2|Theorem §28.2: Arithmetic of Derivatives]] (1)
- [[§31 Taylor's Theorem#^ex-31-3|Example §31.3: A Smooth Function That Is Not Its Taylor Series]] (1)
- [[Fundamental Theorem of Calculus]] (1)
- [[§29 The Mean Value Theorem#^thm-29-3|Theorem §29.3: Mean Value Theorem]] (1)

## Workhorse examples
- [[The line with two origins]]: second countable and locally Euclidean but not Hausdorff, built from neighborhoods and as a quotient
- [[Spheres Sⁿ]]: hemisphere charts, regular level set, tangent space, homogeneous space, cover of projective space
- [[The circle S¹]]: three compatible atlases, no single chart, U(1) and ℝ/ℤ, covered by ℝ
- [[Real and complex projective spaces]]: the model quotient manifolds, with homogeneous-coordinate charts
- [[The Hopf fibration]]: S²ⁿ⁺¹ → ℂPⁿ as quotient, orbit map, submersion and fibration without a section
- [[Classical groups O(n), U(n), SL(n,ℝ)]]: matrix groups as level sets, with dimensions, tangent spaces and actions
- [[Grassmannians]]: k-planes in ℝⁿ as the homogeneous space O(n)/(O(k) × O(n−k))
