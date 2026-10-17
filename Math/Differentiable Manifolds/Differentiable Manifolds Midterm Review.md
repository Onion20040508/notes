---
type: review
subject: "[[Differentiable Manifolds]]"
tags: [differentiable-manifolds, math591, review]
---
↑ [[Differentiable Manifolds]]

# Midterm Review: Plan and Checklist

**The exam.** Wednesday Oct 21, 6–8 pm. **Scope (Uribe's email, Oct 14): everything through commutators of vector fields** — vector fields as sections of $TM$ and as operators on functions, the commutator of two vector fields ("make sure you know how to compute it"), and the notion and properties of $F$-related fields, finished in Lecture 17 (Fri Oct 9). "Nothing about Lie groups is included", so §57 and Chapter 8 (Sard) are out. Review session Friday Oct 16 (previous exams and your questions; you can email him topics or old exam questions in advance). He is not available during the break, but a meeting on Wednesday Oct 21 can be arranged by email. Two past midterms (2025, 2021) have the same three parts, 5 points per item:
1. **Working with definitions**: explain or define precisely, e.g. $\partial/\partial x^j|_p$, $F_{\ast,p}$, a vector bundle, an atlas of $T^\ast M$, injective immersion vs embedding.
2. **True or false with justification**: a proof or a counterexample.
3. **Short proofs and computations**: a lecture theorem reproved from a normal form, a transversality condition, a matrix manifold and its tangent space, a differential computed from the definition.

Results from lecture may be quoted (2021 also allowed the textbooks), and clarity counts. The exam rewards three skills, which are the three layers of this plan:
- **language**: definitions stated exactly;
- **strategies**: knowing which move proves what;
- **a library of examples**: so a true/false item takes a minute.

**From the recordings.** In the Lecture 17 recording (Fri Oct 9), Uribe described the exam:
- There will be "a section where we work with definitions", because "there are so many definitions in this class", then "quick true/false questions", then "short proofs".
- The short proofs "will be either identical to homework problems, or very close to pieces of homework problems, or quick things". **So the homework, broken into pieces, is the core of the review**, which is exactly the [[Differentiable Manifolds HW Drill]].
- The exam is planned as 1.5 hours in the 2-hour slot, in exam booklets. **Update (review session, Oct 16): 100 minutes; bring only writing instruments.**
- There will be a review session (ask him to go over specific things), he will distribute previous exams, and he will post homework solutions.
- Technical proofs that are "not used in homework" (bump functions, Lecture 16) are lower priority.

**From the review session (Fri Oct 16).** "Everything that is contained in the assignments is fair game." The class asked about five topics; each answer is now a box in the notes:
1. the standard atlases of $TM$ and $T^\ast M$ (Remark *Review Session: The Standard Atlases* in [[§50 The Cotangent Bundle#^rem-50-1|§50]]);
2. two submanifolds intersecting transversally: [[§37 Regular Submanifolds#^def-37-7|Definition §37.7]], its equivalence with the map version, and [[§37 Regular Submanifolds#^thm-37-22|Theorem §37.22]] (codimensions add);
3. open relations and orbit relations ([[§6 Open Quotients|§6]]; no new box);
4. the two definitions of $T_pM$, curves and derivations (Remark *Review Session: The Two Definitions of* $T_pM$ in [[§31 Tangent Vectors as Velocities of Curves#^rem-31-3|§31]]); the germ version $T_p^\ast M \cong I_p/I_p^2$ (Remark in [[§34 The Cotangent Space from Germs#^rem-34-3|§34]]);
5. why the Hessian needs a critical point (Remark *Review Session: Why the Hessian Needs a Critical Point* in [[§52 Critical Points and the Hessian#^rem-52-4|§52]]).

Points he stressed in lecture, and where they live:
- the line with two origins as *the* interesting non-example (Example [[§2 Topological Manifolds#^ex-2-1|§2.1]] Fails $T_2$: The Line with Two Origins);
- the saturation of an open set under a group action is the union of its translates (Lemma [[§13 Group Actions and Orbit Spaces#^lem-13-3|§13.3]] Orbit Relations Are Open);
- coordinates on $\mathbb{R}^n$ are $r^i$, never $x^i$, when relating $M$ to $\mathbb{R}^n$ (Definition [[§29 Coordinate Derivations and the Basis Theorem#^def-29-2|§29.2]] Coordinate Derivations);
- the smoothness of the functions in Hadamard's lemma is "a key point" (Lemma [[§29 Coordinate Derivations and the Basis Theorem#^lem-29-3|§29.3]] Hadamard's Lemma);
- normal forms are *local*: the irrational line shows what goes wrong globally (Proposition [[§42 Embeddings#^prop-42-12|§42.12]] The Irrational Line on the Torus);
- submersions are open "because locally they are projections" (Corollary [[§36 Submersions#^cor-36-9|§36.9]] Submersions Are Open Maps);
- a smooth structure is a *maximal* atlas, "the fundamental definition" (Definition [[§17 Differentiable Structures#^def-17-9|§17.9]] Smooth Manifold Structure).

**How to use this note.**
- Every topic below has three checklists:
  - **Language**: state each definition from memory, then give one example and one non-example.
  - **Proofs**: reproduce closed-book. ★★ marks the core results (the past exams' Part 3 is built from these), ★ the supporting ones.
  - **Drill**: the homework parts that exercise the topic, broken into small questions in [[Differentiable Manifolds HW Drill]]; the definitions, core proofs and everything Uribe left as practice in class, broken the same way in [[Differentiable Manifolds Notes Drill]]; and the past-exam items, mapped but not solved; they are your self-test.
- Tick a box only when you can do it on paper without looking.
- The **Strategies** and **Counterexamples** sections at the end are the grammar and the vocabulary of the course; every proof checklist item names the strategy it uses.

**Suggested order of passes** (topics are independent; no dates). Priority follows what the exam draws on: what was **said in class** and what the **homework** did, directly or through its techniques. The [[Differentiable Manifolds Notes Drill]] groups every topic's entries this way:
- **Priority 1**: homework.
- **Priority 2**: class.
- **Priority 3**: a technique the homework drills.
- **Priority 4**: notes only.

1. *Diagnostic.* Take the 2021 midterm cold, 2 hours, closed notes. Mark which topics hurt.
2. *Language pass.* The Language boxes and the Notes Drill definitions at Priority 1–2. This is the fastest gain on Part 1 and Part 2.
3. *Homework drill.* All of [[Differentiable Manifolds HW Drill]]: the short proofs are "identical or close to" homework. Redo each full problem once its pieces are ticked.
4. *Proof pass.* Notes Drill Priority 1–2 proofs, ★★ first; then Priority 3 for topics the diagnostic showed weak. Skip Priority 4 before the midterm.
5. *Mock.* The 2025 midterm under exam conditions, 2 hours. Then repair, using the strategy and counterexample lists.

**Not proved in the notes, so quote them:**
- Theorem [[§35 Local Diffeomorphisms#^thm-35-1|§35.1]] Inverse Function Theorem;
- Theorem [[§38 Fibrations#^thm-38-3|§38.3]] Ehresmann's Theorem;
- Proposition [[§53 Vector Fields#^prop-53-4|§53.4]] Bump Functions Exist;
- Theorem [[§2 Topological Manifolds#^thm-2-1|§2.1]] Topological Invariance of Dimension;
- Theorem [[§16 The Classical Groups#^thm-16-2|§16.2]] Exactly Two Components.

**Gap to close:** the definition of a **vector bundle** is not a box in the notes. Uribe postponed it; see the remark *Vector Bundles* in [[§49 The Tangent Bundle|§49]] and Lee Ch. 10, *Vector Bundles*. The 2025 midterm asked for it (Part 1.3). Write your own definition box, modelled on Definition [[§38 Fibrations#^def-38-1|§38.1]] Fibration plus "fibres are vector spaces, trivializations are linear on fibres".

## How the definitions grew
The notes show the course building each object more than once and then proving the versions agree. Knowing the ladder *is* knowing the language: each row is drilled as a proof in [[Differentiable Manifolds Notes Drill#Equivalences|Notes Drill: Equivalences]].

| Object | Versions in the notes | The theorem that connects them |
| --- | --- | --- |
| Tangent space | geometric $T^{\mathrm{geo}}_pM$ (Definition [[§25 The Geometric Tangent Space#^def-25-1\|§25.1]]), derivations of germs (Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-2\|§28.2]]), coordinate basis (Definition [[§29 Coordinate Derivations and the Basis Theorem#^def-29-2\|§29.2]]), velocities (Definition [[§31 Tangent Vectors as Velocities of Curves#^def-31-2\|§31.2]]) | Theorem [[§25 The Geometric Tangent Space#^thm-25-3\|§25.3]] The Geometric Tangent Space Is the Kernel of the Jacobian; Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6\|§29.6]] Basis Theorem; Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-7\|§29.7]] Ambient and Abstract Agree; Theorem [[§31 Tangent Vectors as Velocities of Curves#^thm-31-2\|§31.2]] Every Tangent Vector Is a Velocity |
| Cotangent space | dual of $T_pM$ (Definition [[§32 The Cotangent Space#^def-32-4\|§32.4]]), dual basis $dx^i$ (Definition [[§33 Covectors in Coordinates#^def-33-1\|§33.1]]), germs $I_p/I_p^2$ (Definition [[§34 The Cotangent Space from Germs#^def-34-1\|§34.1]]) | Lemma [[§33 Covectors in Coordinates#^lem-33-1\|§33.1]] The Differential in Coordinates; Theorem [[§34 The Cotangent Space from Germs#^thm-34-4\|§34.4]] The Cotangent Space from Germs |
| Differential | Jacobian (Definition [[§22 The Differential of a Map Between Vector Spaces#^def-22-5\|§22.5]]), pushforward of derivations (Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-6\|§28.6]]), on curves | Theorem [[§22 The Differential of a Map Between Vector Spaces#^thm-22-3\|§22.3]] Coordinate-Free Formula for the Differential; Theorem [[§30 The Differential in Coordinates#^thm-30-2\|§30.2]] The Matrix of the Differential; Corollary [[§31 Tangent Vectors as Velocities of Curves#^cor-31-3\|§31.3]] Velocity of a Composite |
| Smooth structure | atlas (Definition [[§17 Differentiable Structures#^def-17-6\|§17.6]]), maximal atlas (Definition [[§17 Differentiable Structures#^def-17-8\|§17.8]]) | Theorem [[§17 Differentiable Structures#^thm-17-5\|§17.5]] Every Atlas Lies in a Unique Maximal Atlas; Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-2\|§19.2]] Smoothness of a Map Does Not Depend on the Charts |
| Submanifold of $\mathbb{R}^N$ | external and internal descriptions (Definition [[§20 Manifolds in Euclidean Space#^def-20-1\|§20.1]], Definition [[§20 Manifolds in Euclidean Space#^def-20-2\|§20.2]]), regular level set | Theorem [[§20 Manifolds in Euclidean Space#^thm-20-1\|§20.1]] The Two Descriptions Agree; Proposition [[§37 Regular Submanifolds#^prop-37-9\|§37.9]] Regular Submanifolds of $\mathbb{R}^{n+k}$: The Fourth Description |
| Regular value theorem | in $\mathbb{R}^N$, for manifolds | Theorem [[§7 The Regular Value Theorem#^thm-7-3\|§7.3]] Regular Value Theorem; Theorem [[§37 Regular Submanifolds#^thm-37-12\|§37.12]] The Regular Value Theorem for Manifolds; Proposition [[§37 Regular Submanifolds#^prop-37-14\|§37.14]] The Old and New Versions Agree |
| Transversality | level sets in $\mathbb{R}^N$, maps to a submanifold | Theorem [[§26 Transversality#^thm-26-1\|§26.1]] Preimages of Transverse Level Sets; Theorem [[§37 Regular Submanifolds#^thm-37-15\|§37.15]] Preimages of Transverse Submanifolds; Corollary [[§37 Regular Submanifolds#^cor-37-17\|§37.17]] Special Cases of Transversality |
| Diffeomorphism | two notions | Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-4\|§19.4]] The Two Notions of Diffeomorphism Agree |

## T1. Topological manifolds, quotients, group actions (§1–§16)
**Language**
- [x] Definition [[§1 Point-Set Topology Review#^def-1-6|§1.6]] Second Countable and Definition [[§1 Point-Set Topology Review#^def-1-8|§1.8]] Hausdorff ($T_2$)
- [x] Definition [[§1 Point-Set Topology Review#^def-1-5|§1.5]] Basis of Neighborhoods at a Point and Definition [[§1 Point-Set Topology Review#^def-1-7|§1.7]] First Countable at a Point: first countability, the local version of second countability (Proposition [[§1 Point-Set Topology Review#^prop-1-4|§1.4]] Second Countable Implies First Countable; HW1.4)
- [ ] Definition [[§2 Topological Manifolds#^def-2-1|§2.1]] Locally Euclidean, Definition [[§2 Topological Manifolds#^def-2-2|§2.2]] Topological Manifold, Definition [[§2 Topological Manifolds#^def-2-3|§2.3]] Chart
- [ ] Definition [[§3 Subspaces and Products#^def-3-1|§3.1]] Subspace Topology, Definition [[§3 Subspaces and Products#^def-3-3|§3.3]] Product Topology
- [ ] Definition [[§4 Quotient Spaces and Open Maps#^def-4-2|§4.2]] Quotient Topology, Definition [[§5 Quotient Maps#^def-5-1|§5.1]] Quotient Map, Definition [[§4 Quotient Spaces and Open Maps#^def-4-3|§4.3]] Open Map, Definition [[§4 Quotient Spaces and Open Maps#^def-4-4|§4.4]] Open Equivalence Relation
- [ ] Definition [[§4 Quotient Spaces and Open Maps#^def-4-5|§4.5]] Saturation and Definition [[§4 Quotient Spaces and Open Maps#^def-4-6|§4.6]] Saturated Set
- [ ] Definition [[§11 Topological Groups and Classical Matrix Groups#^def-11-1|§11.1]] Topological Group, Definition [[§13 Group Actions and Orbit Spaces#^def-13-2|§13.2]] Continuous Action, Definition [[§13 Group Actions and Orbit Spaces#^def-13-5|§13.5]] Orbit Space, Definition [[§13 Group Actions and Orbit Spaces#^def-13-7|§13.7]] Proper Action
- [ ] Definition [[§14 Homogeneous Spaces#^def-14-2|§14.2]] Homogeneous Space, Definition [[§14 Homogeneous Spaces#^def-14-3|§14.3]] Isotropy Subgroup, Definition [[§14 Homogeneous Spaces#^def-14-6|§14.6]] The Coset Space

**Proofs**
- [ ] ★★ Theorem [[§5 Quotient Maps#^thm-5-1|§5.1]] Universal Property of a Quotient Map: the tool for maps *out of* a quotient.
- [ ] ★★ Proposition [[§5 Quotient Maps#^prop-5-5|§5.5]] Open Surjections Are Quotient Maps
- [ ] ★★ Theorem [[§6 Open Quotients#^thm-6-1|§6.1]] Hausdorff Criterion and Theorem [[§6 Open Quotients#^thm-6-3|§6.3]] Second Countability of Open Quotients: the two conditions for a quotient to be a manifold.
- [ ] ★★ Lemma [[§13 Group Actions and Orbit Spaces#^lem-13-3|§13.3]] Orbit Relations Are Open, so orbit spaces are open quotients.
- [ ] ★★ Theorem [[§13 Group Actions and Orbit Spaces#^thm-13-5|§13.5]] Compactness of $X$ Is Not Needed: Hausdorff orbit spaces from compact groups.
- [ ] ★ Proposition [[§9 Complex Projective Space#^prop-9-1|§9.1]] $\mathbb{CP}^n$ is Hausdorff and Second Countable: $\mathbb{CP}^n$ via the two criteria.
- [ ] ★ Theorem [[§15 The Topology of G∕H and Real Grassmannians#^thm-15-3|§15.3]] Homogeneous Spaces Are Homeomorphic to Coset Spaces
- [ ] ★ Proposition [[§2 Topological Manifolds#^prop-2-4|§2.4]] The Three Conditions Are Independent: each axiom is independent.
- [ ] ★ Theorem [[§2 Topological Manifolds#^thm-2-8|§2.8]] Connected Manifolds Are Path Connected
- [ ] ★ Theorem [[§3 Subspaces and Products#^thm-3-5|§3.5]] Subspaces Inherit Both Conditions and Theorem [[§3 Subspaces and Products#^thm-3-12|§3.12]] Products Inherit Both Conditions

**Drill**
- [ ] Notes drill: [[Differentiable Manifolds Notes Drill#Definitions T1|definitions]] · [[Differentiable Manifolds Notes Drill#Proofs T1|proofs and class exercises]]
- [ ] 2021 midterm, Part 2.3: an orbit space of an $\mathbb{R}$-action, second countable? (T1, open quotients)
- [ ] 2025 midterm, Part 2.4: second countable + locally Euclidean ⇒ Hausdorff? (counterexample library)
- [ ] Homework drills: [[Differentiable Manifolds HW Drill#^hw1-1|HW1.1]], [[Differentiable Manifolds HW Drill#^hw1-2|HW1.2]], [[Differentiable Manifolds HW Drill#^hw1-3|HW1.3]], [[Differentiable Manifolds HW Drill#^hw1-4|HW1.4]], [[Differentiable Manifolds HW Drill#^hw1-5|HW1.5]], [[Differentiable Manifolds HW Drill#^hw2-1|HW2.1]], [[Differentiable Manifolds HW Drill#^hw2-2|HW2.2]]

## T2. Regular values in $\mathbb{R}^N$ and the classical groups (§7, §11–§12, §20–§23)
**Language**
- [ ] Definition [[§7 The Regular Value Theorem#^def-7-2|§7.2]] Rank, Definition [[§7 The Regular Value Theorem#^def-7-3|§7.3]] Regular Point, Definition [[§7 The Regular Value Theorem#^def-7-4|§7.4]] Regular Value
- [ ] Definition [[§22 The Differential of a Map Between Vector Spaces#^def-22-5|§22.5]] The Differential
- [ ] Definition [[§11 Topological Groups and Classical Matrix Groups#^def-11-5|§11.5]] General Linear Group to Definition [[§11 Topological Groups and Classical Matrix Groups#^def-11-10|§11.10]] Unitary Group: which equations cut out each group.

**Proofs**
- [ ] ★★ Theorem [[§7 The Regular Value Theorem#^thm-7-3|§7.3]] Regular Value Theorem, from the implicit function theorem (quote it).
- [ ] ★★ Corollary [[§12 The Classical Groups Are Topological Manifolds#^cor-12-3|§12.3]] $1$ Is a Regular Value of $\det$ and Corollary [[§12 The Classical Groups Are Topological Manifolds#^cor-12-5|§12.5]] $\mathrm{SL}({n,\mathbb{R}})$ Is a Manifold of Dimension $n^2 - 1$: $\mathrm{SL}(n)$.
- [ ] ★★ $\mathrm{O}(n)$ and $\mathrm{U}(n)$ as regular level sets: Example [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-23-1|§23.1]] $\mathrm{O}(n)$ Is a Smooth Manifold of Dimension $\tfrac{n(n-1)}{2}$, Example [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-23-2|§23.2]] $\mathrm{U}(n)$ Is a Smooth Manifold of Dimension $n^2$. The differential's kernel and surjectivity, Proposition [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^prop-23-1|§23.1]] The Kernel of the Differential.
- [ ] ★ Theorem [[§22 The Differential of a Map Between Vector Spaces#^thm-22-3|§22.3]] Coordinate-Free Formula for the Differential, Corollary [[§22 The Differential of a Map Between Vector Spaces#^cor-22-4|§22.4]] Regular Values Without Coordinates
- [ ] ★ Theorem [[§20 Manifolds in Euclidean Space#^thm-20-1|§20.1]] The Two Descriptions Agree

**Drill**
- [ ] Notes drill: [[Differentiable Manifolds Notes Drill#Definitions T2|definitions]] · [[Differentiable Manifolds Notes Drill#Proofs T2|proofs and class exercises]]
- [ ] Homework drills: [[Differentiable Manifolds HW Drill#^hw1-6|HW1.6]], [[Differentiable Manifolds HW Drill#^hw2-3|HW2.3]], [[Differentiable Manifolds HW Drill#^hw2-4|HW2.4]], [[Differentiable Manifolds HW Drill#^hw4-3|HW4.3]]
- [ ] 2025 midterm, Part 3.10: Hermitian matrices with fixed eigenvalues, a manifold, and its tangent space (regular value + kernel; the hint says which map).

## T3. Smooth structures and smooth maps (§17–§19, §24)
**Language**
- [ ] Definition [[§17 Differentiable Structures#^def-17-4|§17.4]] Smoothly Compatible Charts, Definition [[§17 Differentiable Structures#^def-17-6|§17.6]] Atlas, Definition [[§17 Differentiable Structures#^def-17-7|§17.7]] Compatible Atlases, Definition [[§17 Differentiable Structures#^def-17-8|§17.8]] Maximal Atlas, Definition [[§17 Differentiable Structures#^def-17-9|§17.9]] Smooth Manifold Structure
- [ ] Definition [[§19 Smooth Functions and Smooth Maps#^def-19-1|§19.1]] Smooth Chart, Definition [[§19 Smooth Functions and Smooth Maps#^def-19-2|§19.2]] Smooth Function on a Manifold, Definition [[§19 Smooth Functions and Smooth Maps#^def-19-3|§19.3]] Smooth Map, Definition [[§19 Smooth Functions and Smooth Maps#^def-19-4|§19.4]] Diffeomorphism, Definition [[§19 Smooth Functions and Smooth Maps#^def-19-7|§19.7]] Product Manifold

**Proofs**
- [ ] ★★ Theorem [[§17 Differentiable Structures#^thm-17-5|§17.5]] Every Atlas Lies in a Unique Maximal Atlas
- [ ] ★★ Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-2|§19.2]] Smoothness of a Map Does Not Depend on the Charts: well-definedness via transition maps (strategy S1).
- [ ] ★★ Lemma [[§19 Smooth Functions and Smooth Maps#^lem-19-5|§19.5]] Composition of Smooth Maps
- [ ] ★★ Theorem [[§18 Projective Spaces as Smooth Manifolds#^thm-18-2|§18.2]] The Standard Atlas Is Smooth: compute the transition maps of $\mathbb{CP}^n$.
- [ ] ★ Lemma [[§17 Differentiable Structures#^lem-17-6|§17.6]] Restricting and Recomposing Smooth Charts, Lemma [[§19 Smooth Functions and Smooth Maps#^lem-19-3|§19.3]] A Chart Mapped into a Given Chart
- [ ] ★ Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-4|§19.4]] The Two Notions of Diffeomorphism Agree, Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-10|§19.10]] The Product Smooth Structure
- [ ] ★ Proposition [[§24 The Circle#^prop-24-1|§24.1]] The Three Circle Atlases Define One Smooth Structure: three circle atlases, one structure.
- [ ] ★ Example [[§19 Smooth Functions and Smooth Maps#^ex-19-1|§19.1]] Two Smooth Structures on the Real Line: two different smooth structures on $\mathbb{R}$, diffeomorphic anyway.

**Drill**
- [ ] Notes drill: [[Differentiable Manifolds Notes Drill#Definitions T3|definitions]] · [[Differentiable Manifolds Notes Drill#Proofs T3|proofs and class exercises]]
- [ ] Homework drills: [[Differentiable Manifolds HW Drill#^hw3-1|HW3.1]]

## T4. Tangent spaces (§25–§31)
**Language**: Part 1 of both past exams lives here.
- [ ] Definition [[§25 The Geometric Tangent Space#^def-25-1|§25.1]] Geometric Tangent Space
- [ ] Definition [[§27 Germs#^def-27-2|§27.2]] Germs of Smooth Functions, Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-1|§28.1]] Derivation at a Point, Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-2|§28.2]] The Abstract Tangent Space
- [ ] Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-5|§28.5]] Pullback of Germs and Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-6|§28.6]] Pushforward: *define $F_{\ast,p}$* (2025 Part 1.2).
- [ ] Definition [[§29 Coordinate Derivations and the Basis Theorem#^def-29-1|§29.1]] Coordinate Functions of a Chart and Definition [[§29 Coordinate Derivations and the Basis Theorem#^def-29-2|§29.2]] Coordinate Derivations: *explain $\partial/\partial x^j|_p$* (2025 Part 1.1).
- [ ] Definition [[§31 Tangent Vectors as Velocities of Curves#^def-31-2|§31.2]] Velocity of a Curve

**Proofs**
- [ ] ★★ Theorem [[§25 The Geometric Tangent Space#^thm-25-3|§25.3]] The Geometric Tangent Space Is the Kernel of the Jacobian
- [ ] ★★ Lemma [[§28 Derivations and the Abstract Tangent Space#^lem-28-2|§28.2]] First Properties of Derivations: $D(\text{const}) = 0$, and locality.
- [ ] ★★ Theorem [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]] The Chain Rule
- [ ] ★★ Lemma [[§29 Coordinate Derivations and the Basis Theorem#^lem-29-3|§29.3]] Hadamard's Lemma ⇒ Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]] Basis Theorem: a derivation is determined by its values on the coordinate functions (strategy S9).
- [ ] ★★ Theorem [[§30 The Differential in Coordinates#^thm-30-2|§30.2]] The Matrix of the Differential
- [ ] ★★ Theorem [[§31 Tangent Vectors as Velocities of Curves#^thm-31-2|§31.2]] Every Tangent Vector Is a Velocity and Corollary [[§31 Tangent Vectors as Velocities of Curves#^cor-31-3|§31.3]] Velocity of a Composite: computing differentials with curves.
- [ ] ★★ Example [[§25 The Geometric Tangent Space#^ex-25-2|§25.2]] The Orthogonal Group, Example [[§25 The Geometric Tangent Space#^ex-25-3|§25.3]] The Unitary Group, Theorem [[§25 The Geometric Tangent Space#^thm-25-5|§25.5]] The Classical Groups: tangent spaces of the classical groups at $I$.
- [ ] ★ Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-7|§29.7]] Ambient and Abstract Agree, Lemma [[§28 Derivations and the Abstract Tangent Space#^lem-28-8|§28.8]] Open Subsets Have the Same Abstract Tangent Spaces, Proposition [[§28 Derivations and the Abstract Tangent Space#^prop-28-9|§28.9]] Charts Are Diffeomorphisms
- [ ] ★ Theorem [[§31 Tangent Vectors as Velocities of Curves#^thm-31-4|§31.4]] The Tangent Space of a Product
- [ ] ★ Corollary [[§30 The Differential in Coordinates#^cor-30-4|§30.4]] Change of Coordinates, Proposition [[§30 The Differential in Coordinates#^prop-30-10|§30.10]] Maps with Zero Differential Are Constant

**Drill**
- [ ] Notes drill: [[Differentiable Manifolds Notes Drill#Definitions T4|definitions]] · [[Differentiable Manifolds Notes Drill#Proofs T4|proofs and class exercises]]
- [ ] 2021 midterm, Part 3.10: $d(\text{conjugation})_I$ on $G \subseteq \mathrm{GL}(n)$. Curves, plus Proposition [[§30 The Differential in Coordinates#^prop-30-5|§30.5]] Agreement with the Vector-Space Differential.
- [ ] Homework drills: [[Differentiable Manifolds HW Drill#^hw3-2|HW3.2]], [[Differentiable Manifolds HW Drill#^hw3-4|HW3.4]], [[Differentiable Manifolds HW Drill#^hw4-1|HW4.1]]

## T5. Cotangent spaces and differentials of functions (§32–§34)
**Language**
- [ ] Definition [[§32 The Cotangent Space#^def-32-4|§32.4]] Cotangent Space, Definition [[§32 The Cotangent Space#^def-32-5|§32.5]] The Differential of a Function, Definition [[§33 Covectors in Coordinates#^def-33-1|§33.1]] Components of a Covector, Definition [[§34 The Cotangent Space from Germs#^def-34-1|§34.1]] The Space $I_p/I_p^2$, Definition [[§34 The Cotangent Space from Germs#^def-34-3|§34.3]] Pullback of Covectors

**Proofs**
- [ ] ★★ Lemma [[§33 Covectors in Coordinates#^lem-33-1|§33.1]] The Differential in Coordinates
- [ ] ★★ Theorem [[§34 The Cotangent Space from Germs#^thm-34-4|§34.4]] The Cotangent Space from Germs
- [ ] ★ Proposition [[§34 The Cotangent Space from Germs#^prop-34-6|§34.6]] Pullback Commutes with $d$, Proposition [[§34 The Cotangent Space from Germs#^prop-34-3|§34.3]] The Pairing Is Well Defined and Non-Degenerate

**Drill**
- [ ] Notes drill: [[Differentiable Manifolds Notes Drill#Definitions T5|definitions]] · [[Differentiable Manifolds Notes Drill#Proofs T5|proofs and class exercises]]
- [ ] Homework drills: [[Differentiable Manifolds HW Drill#^hw3-3|HW3.3]]

## T6. Local diffeomorphisms and submersions (§35–§36)
**Language**
- [ ] Definition [[§35 Local Diffeomorphisms#^def-35-1|§35.1]] Local Diffeomorphism, Definition [[§36 Submersions#^def-36-1|§36.1]] Submersion, Definition [[§36 Submersions#^def-36-2|§36.2]] Immersion, Definition [[§36 Submersions#^def-36-3|§36.3]] Regular Points and Critical Points, Definition [[§36 Submersions#^def-36-4|§36.4]] Regular Values and Critical Values

**Proofs**
- [ ] ★★ Theorem [[§35 Local Diffeomorphisms#^thm-35-2|§35.2]] Local Diffeomorphisms Are Detected by the Differential, from the inverse function theorem.
- [ ] ★★ Theorem [[§36 Submersions#^thm-36-6|§36.6]] Local Normal Form for Submersions: the engine of T7.
- [ ] ★★ Corollary [[§36 Submersions#^cor-36-9|§36.9]] Submersions Are Open Maps (stressed in lecture: "locally they are projections"), Theorem [[§36 Submersions#^thm-36-10|§36.10]] Submersions from Compact Manifolds
- [ ] ★ Corollary [[§36 Submersions#^cor-36-7|§36.7]] Being a Submersion Is an Open Condition
- [ ] ★ Corollary [[§35 Local Diffeomorphisms#^cor-35-3|§35.3]] Diffeomorphisms Are the Bijective Local Diffeomorphisms, Proposition [[§36 Submersions#^prop-36-4|§36.4]] Submersions to $\mathbb{R}^k$ and Independent Differentials

**Drill**
- [ ] Notes drill: [[Differentiable Manifolds Notes Drill#Definitions T6|definitions]] · [[Differentiable Manifolds Notes Drill#Proofs T6|proofs and class exercises]]
- [ ] Homework drills: [[Differentiable Manifolds HW Drill#^hw4-2|HW4.2]], [[Differentiable Manifolds HW Drill#^hw3-5|HW3.5]]
- [ ] 2021 midterm, Part 3.8: nonsingular $dF_p$ with image in a half-space. Which property of local diffeomorphisms decides it?
- [ ] 2021 midterm, Part 2.6: two regular values, and the pair $(f, g)$ (compare Proposition [[§36 Submersions#^prop-36-4|§36.4]] Submersions to $\mathbb{R}^k$ and Independent Differentials).

## T7. Regular submanifolds and transversality (§26, §37)
**Language**
- [ ] Definition [[§37 Regular Submanifolds#^def-37-2|§37.2]] Regular Submanifold, Definition [[§37 Regular Submanifolds#^def-37-3|§37.3]] Adapted Chart
- [ ] Definition [[§26 Transversality#^def-26-2|§26.2]] Transversality, Definition [[§37 Regular Submanifolds#^def-37-5|§37.5]] Transversality to a Submanifold
- [ ] Definition [[§37 Regular Submanifolds#^def-37-4|§37.4]] Conormal Space, Definition [[§37 Regular Submanifolds#^def-37-6|§37.6]] Normal Space

**Proofs**
- [ ] ★★ Proposition [[§37 Regular Submanifolds#^prop-37-3|§37.3]] The Induced Smooth Structure
- [ ] ★★ Proposition [[§37 Regular Submanifolds#^prop-37-6|§37.6]] Tangent Spaces of a Regular Submanifold
- [ ] ★★ Lemma [[§37 Regular Submanifolds#^lem-37-11|§37.11]] Level Sets Near a Regular Point ⇒ Theorem [[§37 Regular Submanifolds#^thm-37-12|§37.12]] The Regular Value Theorem for Manifolds
- [ ] ★★ Theorem [[§37 Regular Submanifolds#^thm-37-15|§37.15]] Preimages of Transverse Submanifolds and Corollary [[§37 Regular Submanifolds#^cor-37-17|§37.17]] Special Cases of Transversality: HW5.2.
- [ ] ★★ Lemma [[§37 Regular Submanifolds#^lem-37-5|§37.5]] Smooth Maps and Regular Submanifolds: maps into and out of submanifolds.
- [ ] ★ Proposition [[§37 Regular Submanifolds#^prop-37-7|§37.7]] Adapted Charts Give Local Defining Maps, Proposition [[§37 Regular Submanifolds#^prop-37-9|§37.9]] Regular Submanifolds of $\mathbb{R}^{n+k}$: The Fourth Description, Theorem [[§26 Transversality#^thm-26-1|§26.1]] Preimages of Transverse Level Sets, Proposition [[§26 Transversality#^prop-26-4|§26.4]] Transverse Intersections
- [ ] ★ Theorem [[§37 Regular Submanifolds#^thm-37-20|§37.20]] Lagrange Multipliers: HW5.4.

**Drill**
- [ ] Notes drill: [[Differentiable Manifolds Notes Drill#Definitions T7|definitions]] · [[Differentiable Manifolds Notes Drill#Proofs T7|proofs and class exercises]]
- [ ] 2025 midterm, Part 2.6: is a submersion transverse to every submanifold?
- [ ] 2025 midterm, Part 3.9: graph and diagonal transverse. Use the tangent space of a product, Theorem [[§31 Tangent Vectors as Velocities of Curves#^thm-31-4|§31.4]] The Tangent Space of a Product.
- [ ] 2021 midterm, Part 2.7: intersection of submanifolds of $\mathbb{R}^3$ vs transversality.
- [ ] 2021 midterm, Part 3.9: the differential of a restriction to an invariant submanifold.
- [ ] Homework drills: [[Differentiable Manifolds HW Drill#^hw2-5|HW2.5]], [[Differentiable Manifolds HW Drill#^hw5-2|HW5.2]], [[Differentiable Manifolds HW Drill#^hw5-4|HW5.4]]

## T8. Fibrations (§38–§40)
**Language**
- [ ] Definition [[§38 Fibrations#^def-38-1|§38.1]] Fibration, Definition [[§38 Fibrations#^def-38-2|§38.2]] Trivial Fibration, Definition [[§38 Fibrations#^def-38-3|§38.3]] Section, Definition [[§38 Fibrations#^def-38-4|§38.4]] Local Section, Definition [[§38 Fibrations#^def-38-5|§38.5]] Vertical Space
- [ ] Vector bundle: your own box (see the gap above).

**Proofs**
- [ ] ★★ Proposition [[§38 Fibrations#^prop-38-1|§38.1]] Fibres and Fibrations, Proposition [[§38 Fibrations#^prop-38-2|§38.2]] Fibres Are Copies of the Model Fibre
- [ ] ★★ Proposition [[§38 Fibrations#^prop-38-4|§38.4]] Local Trivializations Give Local Sections
- [ ] ★ Proposition [[§39 Examples of Fibrations#^prop-39-1|§39.1]] The Möbius Band Is a Fibration, Proposition [[§38 Fibrations#^prop-38-5|§38.5]] Splitting Along a Section, Proposition [[§40 The Normal Bundle of a Submanifold of Euclidean Space#^prop-40-2|§40.2]] The Normal Bundle Is a Fibration
- [ ] Know the statement of Theorem [[§38 Fibrations#^thm-38-3|§38.3]] Ehresmann's Theorem, and why each hypothesis is needed: Example [[§38 Fibrations#^ex-38-1|§38.1]] A Submersion That Is Not a Fibration, Example [[§38 Fibrations#^ex-38-2|§38.2]] All Fibres Diffeomorphic but Not a Fibration.

**Drill**
- [ ] Notes drill: [[Differentiable Manifolds Notes Drill#Definitions T8|definitions]] · [[Differentiable Manifolds Notes Drill#Proofs T8|proofs and class exercises]]
- [ ] Homework drills: [[Differentiable Manifolds HW Drill#^hw4-4|HW4.4]], [[Differentiable Manifolds HW Drill#^hw5-5|HW5.5]]
- [ ] 2025 midterm, Part 2.5: the punctured plane over a line, a fibration?
- [ ] 2021 midterm, Part 2.5: is every surjective submersion a fibration?
- [ ] 2025 midterm, Part 1.3: explain a vector bundle.

## T9. Immersions and embeddings (§41–§42)
**Language**
- [ ] Definition [[§41 Immersions#^def-41-1|§41.1]] Immersions, Definition [[§42 Embeddings#^def-42-1|§42.1]] Embedding, Definition [[§42 Embeddings#^def-42-2|§42.2]] Proper Map, Definition [[§42 Embeddings#^def-42-3|§42.3]] Locally Closed Subset, Definition [[§42 Embeddings#^def-42-4|§42.4]] Immersed Submanifold

**Proofs**
- [ ] ★★ Theorem [[§41 Immersions#^thm-41-1|§41.1]] Local Normal Form for Immersions
- [ ] ★★ Theorem [[§42 Embeddings#^thm-42-1|§42.1]] The Image of an Embedding Is a Regular Submanifold: 2025 Part 3.8 asked exactly this, using the immersion normal form.
- [ ] ★★ Theorem [[§42 Embeddings#^thm-42-5|§42.5]] Injective Proper Immersions Are Embeddings and Corollary [[§42 Embeddings#^cor-42-6|§42.6]] Injective Immersions of Compact Manifolds
- [ ] ★★ Corollary [[§42 Embeddings#^cor-42-3|§42.3]] An Embedding Is a Diffeomorphism onto Its Image
- [ ] ★ Proposition [[§42 Embeddings#^prop-42-10|§42.10]] Sections Are Closed Embeddings: HW5.1.
- [ ] ★ Proposition [[§42 Embeddings#^prop-42-12|§42.12]] The Irrational Line on the Torus, Proposition [[§42 Embeddings#^prop-42-13|§42.13]] Images of Injective Immersions, Proposition [[§42 Embeddings#^prop-42-15|§42.15]] When an Immersed Submanifold Is Regular

**Drill**
- [ ] Notes drill: [[Differentiable Manifolds Notes Drill#Definitions T9|definitions]] · [[Differentiable Manifolds Notes Drill#Proofs T9|proofs and class exercises]]
- [ ] Homework drills: [[Differentiable Manifolds HW Drill#^hw4-5|HW4.5]], [[Differentiable Manifolds HW Drill#^hw5-1|HW5.1]]
- [ ] 2021 midterm, Part 1.1: injective immersion vs embedding, compared and contrasted.
- [ ] 2021 midterm, Part 2.4: is a composition of embeddings an embedding?
- [ ] 2025 midterm, Part 2.7: is an injective immersion of $S^m$ an embedding?

## T10. Tangent and cotangent bundles, one-forms, the Hessian (§47–§52)
**Language**
- [ ] Definition [[§49 The Tangent Bundle#^def-49-1|§49.1]] The Tangent Bundle as a Set, Definition [[§49 The Tangent Bundle#^def-49-4|§49.4]] Local Trivializations of $TM$, Definition [[§49 The Tangent Bundle#^def-49-5|§49.5]] Charts of $TM$
- [ ] Definition [[§50 The Cotangent Bundle#^def-50-5|§50.5]] Charts of $T^{\ast}M$: *give a smooth atlas of $T^\ast M$* (2021 Part 1.2).
- [ ] Definition [[§51 One-Forms#^def-51-1|§51.1]] One-Form, Definition [[§52 Critical Points and the Hessian#^def-52-2|§52.2]] Hessian at a Critical Point, Definition [[§52 Critical Points and the Hessian#^def-52-3|§52.3]] Nondegenerate Critical Point, Definition [[§52 Critical Points and the Hessian#^def-52-4|§52.4]] Morse Function

**Proofs**
- [ ] ★★ Proposition [[§49 The Tangent Bundle#^prop-49-1|§49.1]] The Topology of $TM$ and Proposition [[§49 The Tangent Bundle#^prop-49-2|§49.2]] The Smooth Atlas of $TM$: topology, then atlas.
- [ ] ★★ Proposition [[§50 The Cotangent Bundle#^prop-50-2|§50.2]] The Smooth Atlas of $T^{\ast}M$, Corollary [[§49 The Tangent Bundle#^cor-49-3|§49.3]] The Tangent Bundle Is a Fibration
- [ ] ★★ Proposition [[§51 One-Forms#^prop-51-2|§51.2]] The Differential of a Function Is a One-Form
- [ ] ★ Proposition [[§52 Critical Points and the Hessian#^prop-52-3|§52.3]] The Hessian at a Critical Point Is Well Defined, Theorem [[§52 Critical Points and the Hessian#^thm-52-10|§52.10]] Transversality to the Zero Section (HW5.3), Corollary [[§52 Critical Points and the Hessian#^cor-52-11|§52.11]] Critical Points of a Morse Function Are Isolated

**Drill**
- [ ] Notes drill: [[Differentiable Manifolds Notes Drill#Definitions T10|definitions]] · [[Differentiable Manifolds Notes Drill#Proofs T10|proofs and class exercises]]
- [ ] Homework drills: [[Differentiable Manifolds HW Drill#^hw5-3|HW5.3]]

## T11. Vector fields, the bracket, $F$-related fields (§53–§56)
In scope exactly as Uribe's email lists it. Lie groups (§57) are **not** on the midterm.

**Language**
- [ ] Definition [[§53 Vector Fields#^def-53-1|§53.1]] Vector Field, Definition [[§53 Vector Fields#^def-53-2|§53.2]] The Space of Vector Fields, Definition [[§53 Vector Fields#^def-53-3|§53.3]] Product of a Function and a Vector Field: a vector field as a section of $TM$.
- [ ] Definition [[§53 Vector Fields#^def-53-4|§53.4]] Operator on $C^\infty(M)$, Definition [[§53 Vector Fields#^def-53-5|§53.5]] Derivation of $C^\infty(M)$, Definition [[§53 Vector Fields#^def-53-6|§53.6]] Local Operator: a vector field as an operator on functions.
- [ ] Definition [[§55 Lie Bracket and Lie Algebra#^def-55-1|§55.1]] The Lie Bracket of Vector Fields, Definition [[§55 Lie Bracket and Lie Algebra#^def-55-2|§55.2]] Lie Algebra
- [ ] Definition [[§56 Related Vector Fields#^def-56-1|§56.1]] Pushforward of a Vector Field by a Diffeomorphism, Definition [[§56 Related Vector Fields#^def-56-2|§56.2]] $F$-Related Vector Fields

**Proofs**
- [ ] ★★ Lemma [[§53 Vector Fields#^lem-53-3|§53.3]] A Vector Field Is a Derivation and Proposition [[§53 Vector Fields#^prop-53-7|§53.7]] Derivations Are Vector Fields: the two views agree (derivations of $C^\infty(M)$ are vector fields).
- [ ] ★★ Lemma [[§53 Vector Fields#^lem-53-6|§53.6]] Derivations Are Local: derivations are local; uses Corollary [[§53 Vector Fields#^cor-53-5|§53.5]] Every Germ Has a Global Representative (quote Proposition [[§53 Vector Fields#^prop-53-4|§53.4]] Bump Functions Exist).
- [ ] ★★ Lemma [[§55 Lie Bracket and Lie Algebra#^lem-55-1|§55.1]] The Bracket of Vector Fields Is a Vector Field: the bracket is again a vector field.
- [ ] ★★ Proposition [[§55 Lie Bracket and Lie Algebra#^prop-55-2|§55.2]] The Bracket in Coordinates: **compute brackets in coordinates**, e.g. Example [[§55 Lie Bracket and Lie Algebra#^ex-55-1|§55.1]] A Bracket in the Plane.
- [ ] ★★ Proposition [[§56 Related Vector Fields#^prop-56-1|§56.1]] Related Fields as Operators and Proposition [[§56 Related Vector Fields#^prop-56-3|§56.3]] Naturality of the Bracket: $F$-related fields as operators, and naturality of the bracket.
- [ ] ★ Lemma [[§53 Vector Fields#^lem-53-8|§53.8]] A Smoothness Criterion for Vector Fields, Proposition [[§55 Lie Bracket and Lie Algebra#^prop-55-4|§55.4]] Commutators of an Associative Product, Corollary [[§55 Lie Bracket and Lie Algebra#^cor-55-5|§55.5]] Vector Fields Form a Lie Algebra, Proposition [[§56 Related Vector Fields#^prop-56-2|§56.2]] Pushforward by a Diffeomorphism, Corollary [[§56 Related Vector Fields#^cor-56-4|§56.4]] Diffeomorphisms Preserve Brackets, Example [[§56 Related Vector Fields#^ex-56-1|§56.1]] Fields Related by a Projection

**Drill**
- [ ] Notes drill: [[Differentiable Manifolds Notes Drill#Definitions T11|definitions]] · [[Differentiable Manifolds Notes Drill#Proofs T11|proofs and class exercises]]

## Strategies: the grammar of 591
Each one is a reusable move. Before writing a proof, name the move.

- **S1 Check in a chart, then show the choice of chart does not matter.** Transition maps are smooth, so "smooth in some chart" means "smooth in every chart": Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-1|§19.1]] Some Chart Suffices, Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-2|§19.2]] Smoothness of a Map Does Not Depend on the Charts, Definition [[§29 Coordinate Derivations and the Basis Theorem#^def-29-2|§29.2]] Coordinate Derivations.
- **S2 Define on representatives, then check well-definedness.** Germs, cosets, quotients, $[f]$ in $I_p/I_p^2$, $\ell_0$ on a span.
- **S3 Maps out of a quotient go through the universal property**: Theorem [[§5 Quotient Maps#^thm-5-1|§5.1]] Universal Property of a Quotient Map.
- **S4 Quotient → manifold.** Hausdorff via a closed relation; second countable via images of a countable basis under an open quotient map: Theorem [[§6 Open Quotients#^thm-6-1|§6.1]] Hausdorff Criterion, Theorem [[§6 Open Quotients#^thm-6-3|§6.3]] Second Countability of Open Quotients.
- **S5 Regular value theorem on a well-chosen map**, e.g. $A \mapsto A^{\mathsf T} A$, $\det$, (trace, det): Theorem [[§7 The Regular Value Theorem#^thm-7-3|§7.3]] Regular Value Theorem, Theorem [[§37 Regular Submanifolds#^thm-37-12|§37.12]] The Regular Value Theorem for Manifolds.
- **S6 Tangent space of a level set = kernel of the differential.** Prove $\subseteq$, then count dimensions: Theorem [[§25 The Geometric Tangent Space#^thm-25-3|§25.3]] The Geometric Tangent Space Is the Kernel of the Jacobian, Proposition [[§37 Regular Submanifolds#^prop-37-6|§37.6]] Tangent Spaces of a Regular Submanifold.
- **S7 Linear algebra closes the gap.** An injective map between spaces of equal dimension is onto; rank–nullity; a subspace of full dimension is everything.
- **S8 Normal forms give charts.** Submersion and immersion normal forms ⇒ adapted charts: Theorem [[§36 Submersions#^thm-36-6|§36.6]] Local Normal Form for Submersions, Theorem [[§41 Immersions#^thm-41-1|§41.1]] Local Normal Form for Immersions.
- **S9 A derivation is determined by the coordinate functions** (Hadamard): Lemma [[§29 Coordinate Derivations and the Basis Theorem#^lem-29-3|§29.3]] Hadamard's Lemma, Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]] Basis Theorem.
- **S10 Compute $F_{\ast}$ with curves**: $F_{\ast}(\gamma'(0)) = (F \circ \gamma)'(0)$, Corollary [[§31 Tangent Vectors as Velocities of Curves#^cor-31-3|§31.3]] Velocity of a Composite.
- **S11 Local, then global.** Germs, shrinking neighbourhoods, bump functions: Lemma [[§28 Derivations and the Abstract Tangent Space#^lem-28-8|§28.8]] Open Subsets Have the Same Abstract Tangent Spaces, Corollary [[§53 Vector Fields#^cor-53-5|§53.5]] Every Germ Has a Global Representative.
- **S12 Transversality = the images span.** Reduce to a regular value of a composite with a local defining map: Theorem [[§37 Regular Submanifolds#^thm-37-15|§37.15]] Preimages of Transverse Submanifolds.
- **S13 Compactness upgrades local to global**: closed images, proper maps, finitely many critical points: Theorem [[§36 Submersions#^thm-36-10|§36.10]] Submersions from Compact Manifolds, Theorem [[§42 Embeddings#^thm-42-5|§42.5]] Injective Proper Immersions Are Embeddings, Corollary [[§52 Critical Points and the Hessian#^cor-52-12|§52.12]] Morse Functions on Compact Manifolds.
- **S13′ Connectedness upgrades local to global**: a local property plus a clopen set gives a global one, Theorem [[§2 Topological Manifolds#^thm-2-8|§2.8]] Connected Manifolds Are Path Connected, Proposition [[§30 The Differential in Coordinates#^prop-30-10|§30.10]] Maps with Zero Differential Are Constant.
- **S14 Differentiate an identity**, e.g. $\pi \circ s = \mathrm{id}$ or $G \circ F =$ const. Test closedness, Hausdorffness and continuity with sequences.
- **S15 Symmetry**: prove it at one point (or on one slice), then move it by the group: homogeneous spaces, classical groups, $\mathrm{SU}(2)$.

(The [[Differentiable Manifolds HW Drill]] lists which homework problems use which move, in its last section.)

## Counterexamples: the vocabulary for Part 2
Know each one's picture and the exact property it breaks.
- [ ] Line with two origins (locally Euclidean + second countable, not Hausdorff): Example [[§2 Topological Manifolds#^ex-2-1|§2.1]] Fails $T_2$: The Line with Two Origins, Example [[§10 The Line with Two Origins#^ex-10-1|§10.1]] The Line with Two Origins
- [ ] $\mathbb{Q}$ (not locally Euclidean); $\mathbb{R}_{\mathrm{disc}} \times \mathbb{R}$ (not second countable): Example [[§2 Topological Manifolds#^ex-2-2|§2.2]] Fails Locally Euclidean: $\mathbb{Q}$, Example [[§2 Topological Manifolds#^ex-2-3|§2.3]] Fails Second Countability: $\mathbb{R}_{\mathrm{disc}} \times \mathbb{R}$
- [ ] A non-open relation, and a non-second-countable quotient: Example [[§4 Quotient Spaces and Open Maps#^ex-4-3|§4.3]] Non-Example, Example [[§4 Quotient Spaces and Open Maps#^ex-4-4|§4.4]] Failure of Second Countability
- [ ] A non-Hausdorff orbit space (the group must be compact): Example [[§13 Group Actions and Orbit Spaces#^ex-13-6|§13.6]] Compactness Is Needed: a Non-Hausdorff Orbit Space; an isotropy group that is not closed: Example [[§14 Homogeneous Spaces#^ex-14-1|§14.1]] An Isotropy Group That Is Not Closed
- [ ] A continuous bijection that is not a homeomorphism: Example [[§15 The Topology of G∕H and Real Grassmannians#^ex-15-2|§15.2]] A Continuous Bijection That Is Not a Homeomorphism
- [ ] Two smooth structures on $\mathbb{R}$ (the $x^3$ chart): Example [[§19 Smooth Functions and Smooth Maps#^ex-19-1|§19.1]] Two Smooth Structures on the Real Line, Example [[§19 Smooth Functions and Smooth Maps#^ex-19-2|§19.2]] The Real Line with the Cube-Root Chart
- [ ] Transversality failing two ways: Example [[§26 Transversality#^ex-26-2|§26.2]] Two Ways Transversality Can Fail
- [ ] A surjective submersion that is not a fibration (punctured plane), and all fibres diffeomorphic but still not a fibration: Example [[§38 Fibrations#^ex-38-1|§38.1]] A Submersion That Is Not a Fibration, Example [[§38 Fibrations#^ex-38-2|§38.2]] All Fibres Diffeomorphic but Not a Fibration
- [ ] An immersion that crosses itself; an injective immersion that is not a homeomorphism onto its image: Example [[§41 Immersions#^ex-41-1|§41.1]] An Immersion That Crosses Itself, Example [[§41 Immersions#^ex-41-2|§41.2]] An Injective Immersion That Is Not a Homeomorphism onto Its Image
- [ ] Immersed but not regular (the irrational line on the torus): Example [[§42 Embeddings#^ex-42-1|§42.1]] Immersed but Not Regular, Proposition [[§42 Embeddings#^prop-42-12|§42.12]] The Irrational Line on the Torus
- [ ] A Hessian matrix that depends on the chart (away from critical points): Example [[§52 Critical Points and the Hessian#^ex-52-1|§52.1]] The Hessian Matrix Depends on the Chart

## Past midterms
The files are in the course folder (`Midterm/midterm-1.pdf` is 2021 and `Midterm/midterm.pdf` is 2025). Each item is mapped to its topic above and deliberately not solved here; use them as timed self-tests.

| Exam | Part 1 | Part 2 | Part 3 |
| --- | --- | --- | --- |
| 2021 (Oct 27) | 1 T9 · 2 T10 | 3 T1 · 4 T9 · 5 T8 · 6 T6 · 7 T7 | 8 T6 · 9 T7 · 10 T4 |
| 2025 (Oct 15) | 1 T4 · 2 T4 · 3 T8 | 4 T1 · 5 T8 · 6 T7 · 7 T9 | 8 T9 · 9 T7 · 10 T2 |

**Drill**
- [ ] Notes drill: [[Differentiable Manifolds Notes Drill#Definitions T11|definitions]] · [[Differentiable Manifolds Notes Drill#Proofs T11|proofs and class exercises]]

