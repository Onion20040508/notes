---
type: review
subject: "[[Differentiable Manifolds]]"
tags: [differentiable-manifolds, math591, review]
---
↑ [[Differentiable Manifolds]]

# Midterm Review: Plan and Checklist

**The exam.** Wednesday Oct 21, 6–8 pm. **Scope (Uribe's email, Oct 14): everything through commutators of vector fields** — vector fields as sections of $TM$ and as operators on functions, the commutator of two vector fields ("make sure you know how to compute it"), and the notion and properties of $F$-related fields, finished in Lecture 17 (Fri Oct 9). "Nothing about Lie groups is included", so §60–§61 and Chapter 9 (Sard) are out. Review session Friday Oct 16 (previous exams and your questions; you can email him topics or old exam questions in advance). He is not available during the break, but a meeting on Wednesday Oct 21 can be arranged by email. Two past midterms (2025, 2021) have the same three parts, 5 points per item:
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
1. the standard atlases of $TM$ and $T^\ast M$ (Remark *Review Session: The Standard Atlases* in [[§52 The Cotangent Bundle#^rem-52-1|§52]]);
2. two submanifolds intersecting transversally: [[§39 Transversality and Lagrange Multipliers#^def-39-3|Definition §39.3]], its equivalence with the map version, and [[§39 Transversality and Lagrange Multipliers#^thm-39-8|Theorem §39.8]] (codimensions add);
3. open relations and orbit relations ([[§6 Open Quotients|§6]]; no new box);
4. the two definitions of $T_pM$, curves and derivations (Remark *Review Session: The Two Definitions of* $T_pM$ in [[§31 Tangent Vectors as Velocities of Curves#^rem-31-3|§31]]); the germ version $T_p^\ast M \cong I_p/I_p^2$ (Remark in [[§34 The Cotangent Space from Germs#^rem-34-3|§34]]);
5. why the Hessian needs a critical point (Remark *Review Session: Why the Hessian Needs a Critical Point* in [[§55 Morse Functions and the Zero Section#^rem-55-3|§55]]).

Points he stressed in lecture, and where they live:
- the line with two origins as *the* interesting non-example (Example [[§2 Topological Manifolds#^ex-2-1|§2.1]] Fails $T_2$: The Line with Two Origins);
- the saturation of an open set under a group action is the union of its translates (Lemma [[§13 Group Actions and Orbit Spaces#^lem-13-3|§13.3]] Orbit Relations Are Open);
- coordinates on $\mathbb{R}^n$ are $r^i$, never $x^i$, when relating $M$ to $\mathbb{R}^n$ (Definition [[§29 Coordinate Derivations and the Basis Theorem#^def-29-2|§29.2]] Coordinate Derivations);
- the smoothness of the functions in Hadamard's lemma is "a key point" (Lemma [[§29 Coordinate Derivations and the Basis Theorem#^lem-29-3|§29.3]] Hadamard's Lemma);
- normal forms are *local*: the irrational line shows what goes wrong globally (Proposition [[§44 Embeddings#^prop-44-12|§44.12]] The Irrational Line on the Torus);
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
- Theorem [[§40 Fibrations#^thm-40-3|§40.3]] Ehresmann's Theorem;
- Proposition [[§56 Vector Fields#^prop-56-4|§56.4]] Bump Functions Exist;
- Theorem [[§2 Topological Manifolds#^thm-2-1|§2.1]] Topological Invariance of Dimension;
- Theorem [[§16 The Classical Groups#^thm-16-2|§16.2]] Exactly Two Components.

**Gap to close:** the definition of a **vector bundle** is not a box in the notes. Uribe postponed it; see the remark *Vector Bundles* in [[§51 The Tangent Bundle|§51]] and Lee Ch. 10, *Vector Bundles*. The 2025 midterm asked for it (Part 1.3). Write your own definition box, modelled on Definition [[§40 Fibrations#^def-40-1|§40.1]] Fibration plus "fibres are vector spaces, trivializations are linear on fibres".

## How the definitions grew
The notes show the course building each object more than once and then proving the versions agree. Knowing the ladder *is* knowing the language: each row is drilled as a proof in [[Differentiable Manifolds Notes Drill#Equivalences|Notes Drill: Equivalences]].

| Object | Versions in the notes | The theorem that connects them |
| --- | --- | --- |
| Tangent space | geometric $T^{\mathrm{geo}}_pM$ (Definition [[§25 The Geometric Tangent Space#^def-25-1\|§25.1]]), derivations of germs (Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-2\|§28.2]]), coordinate basis (Definition [[§29 Coordinate Derivations and the Basis Theorem#^def-29-2\|§29.2]]), velocities (Definition [[§31 Tangent Vectors as Velocities of Curves#^def-31-2\|§31.2]]) | Theorem [[§25 The Geometric Tangent Space#^thm-25-3\|§25.3]] The Geometric Tangent Space Is the Kernel of the Jacobian; Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6\|§29.6]] Basis Theorem; Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-7\|§29.7]] Ambient and Abstract Agree; Theorem [[§31 Tangent Vectors as Velocities of Curves#^thm-31-4\|§31.4]] Every Tangent Vector Is a Velocity |
| Cotangent space | dual of $T_pM$ (Definition [[§32 The Cotangent Space#^def-32-4\|§32.4]]), dual basis $dx^i$ (Definition [[§33 Covectors in Coordinates#^def-33-1\|§33.1]]), germs $I_p/I_p^2$ (Definition [[§34 The Cotangent Space from Germs#^def-34-1\|§34.1]]) | Lemma [[§33 Covectors in Coordinates#^lem-33-1\|§33.1]] The Differential in Coordinates; Theorem [[§34 The Cotangent Space from Germs#^thm-34-4\|§34.4]] The Cotangent Space from Germs |
| Differential | Jacobian (Definition [[§22 The Differential of a Map Between Vector Spaces#^def-22-5\|§22.5]]), pushforward of derivations (Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-6\|§28.6]]), on curves | Theorem [[§22 The Differential of a Map Between Vector Spaces#^thm-22-3\|§22.3]] Coordinate-Free Formula for the Differential; Theorem [[§30 The Differential in Coordinates#^thm-30-2\|§30.2]] The Matrix of the Differential; Corollary [[§31 Tangent Vectors as Velocities of Curves#^cor-31-5\|§31.5]] Velocity of a Composite |
| Smooth structure | atlas (Definition [[§17 Differentiable Structures#^def-17-6\|§17.6]]), maximal atlas (Definition [[§17 Differentiable Structures#^def-17-8\|§17.8]]) | Theorem [[§17 Differentiable Structures#^thm-17-5\|§17.5]] Every Atlas Lies in a Unique Maximal Atlas; Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-2\|§19.2]] Smoothness of a Map Does Not Depend on the Charts |
| Submanifold of $\mathbb{R}^N$ | external and internal descriptions (Definition [[§20 Manifolds in Euclidean Space#^def-20-1\|§20.1]], Definition [[§20 Manifolds in Euclidean Space#^def-20-2\|§20.2]]), regular level set | Theorem [[§20 Manifolds in Euclidean Space#^thm-20-1\|§20.1]] The Two Descriptions Agree; Proposition [[§37 Regular Submanifolds#^prop-37-9\|§37.9]] Regular Submanifolds of $\mathbb{R}^{n+k}$: The Fourth Description |
| Regular value theorem | in $\mathbb{R}^N$, for manifolds | Theorem [[§7 The Regular Value Theorem#^thm-7-3\|§7.3]] Regular Value Theorem; Theorem [[§38 The Regular Value Theorem for Manifolds#^thm-38-2\|§38.2]] The Regular Value Theorem for Manifolds; Proposition [[§38 The Regular Value Theorem for Manifolds#^prop-38-4\|§38.4]] The Old and New Versions Agree |
| Transversality | level sets in $\mathbb{R}^N$, maps to a submanifold | Theorem [[§26 Transversality#^thm-26-1\|§26.1]] Preimages of Transverse Level Sets; Theorem [[§39 Transversality and Lagrange Multipliers#^thm-39-1\|§39.1]] Preimages of Transverse Submanifolds; Corollary [[§39 Transversality and Lagrange Multipliers#^cor-39-3\|§39.3]] Special Cases of Transversality |
| Diffeomorphism | two notions | Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-4\|§19.4]] The Two Notions of Diffeomorphism Agree |

## T1. Topological manifolds, quotients, group actions (§1–§16)
**Language**
- [x] Definition [[§1 Point-Set Topology Review#^def-1-6|§1.6]] Second Countable and Definition [[§1 Point-Set Topology Review#^def-1-8|§1.8]] Hausdorff ($T_2$)
- [x] Definition [[§1 Point-Set Topology Review#^def-1-5|§1.5]] Basis of Neighborhoods at a Point and Definition [[§1 Point-Set Topology Review#^def-1-7|§1.7]] First Countable at a Point: first countability, the local version of second countability (Proposition [[§1 Point-Set Topology Review#^prop-1-4|§1.4]] Second Countable Implies First Countable; HW1.4)
- [x] Definition [[§2 Topological Manifolds#^def-2-1|§2.1]] Locally Euclidean, Definition [[§2 Topological Manifolds#^def-2-2|§2.2]] Topological Manifold, Definition [[§2 Topological Manifolds#^def-2-3|§2.3]] Chart
- [x] Definition [[§3 Subspaces and Products#^def-3-1|§3.1]] Subspace Topology, Definition [[§3 Subspaces and Products#^def-3-3|§3.3]] Product Topology
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
- [ ] ★★ Theorem [[§31 Tangent Vectors as Velocities of Curves#^thm-31-4|§31.4]] Every Tangent Vector Is a Velocity and Corollary [[§31 Tangent Vectors as Velocities of Curves#^cor-31-5|§31.5]] Velocity of a Composite: computing differentials with curves.
- [ ] ★★ Example [[§25 The Geometric Tangent Space#^ex-25-2|§25.2]] The Orthogonal Group, Example [[§25 The Geometric Tangent Space#^ex-25-3|§25.3]] The Unitary Group, Theorem [[§25 The Geometric Tangent Space#^thm-25-5|§25.5]] The Classical Groups: tangent spaces of the classical groups at $I$.
- [ ] ★ Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-7|§29.7]] Ambient and Abstract Agree, Lemma [[§28 Derivations and the Abstract Tangent Space#^lem-28-8|§28.8]] Open Subsets Have the Same Abstract Tangent Spaces, Proposition [[§28 Derivations and the Abstract Tangent Space#^prop-28-9|§28.9]] Charts Are Diffeomorphisms
- [ ] ★ Theorem [[§31 Tangent Vectors as Velocities of Curves#^thm-31-6|§31.6]] The Tangent Space of a Product
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

## T7. Regular submanifolds and transversality (§26, §37–§39)
**Language**
- [ ] Definition [[§37 Regular Submanifolds#^def-37-2|§37.2]] Regular Submanifold, Definition [[§37 Regular Submanifolds#^def-37-3|§37.3]] Adapted Chart
- [ ] Definition [[§26 Transversality#^def-26-2|§26.2]] Transversality, Definition [[§39 Transversality and Lagrange Multipliers#^def-39-1|§39.1]] Transversality to a Submanifold
- [ ] Definition [[§37 Regular Submanifolds#^def-37-4|§37.4]] Conormal Space, Definition [[§39 Transversality and Lagrange Multipliers#^def-39-2|§39.2]] Normal Space

**Proofs**
- [ ] ★★ Proposition [[§37 Regular Submanifolds#^prop-37-3|§37.3]] The Induced Smooth Structure
- [ ] ★★ Proposition [[§37 Regular Submanifolds#^prop-37-6|§37.6]] Tangent Spaces of a Regular Submanifold
- [ ] ★★ Lemma [[§38 The Regular Value Theorem for Manifolds#^lem-38-1|§38.1]] Level Sets Near a Regular Point ⇒ Theorem [[§38 The Regular Value Theorem for Manifolds#^thm-38-2|§38.2]] The Regular Value Theorem for Manifolds
- [ ] ★★ Theorem [[§39 Transversality and Lagrange Multipliers#^thm-39-1|§39.1]] Preimages of Transverse Submanifolds and Corollary [[§39 Transversality and Lagrange Multipliers#^cor-39-3|§39.3]] Special Cases of Transversality: HW5.2.
- [ ] ★★ Lemma [[§37 Regular Submanifolds#^lem-37-5|§37.5]] Smooth Maps and Regular Submanifolds: maps into and out of submanifolds.
- [ ] ★ Proposition [[§37 Regular Submanifolds#^prop-37-7|§37.7]] Adapted Charts Give Local Defining Maps, Proposition [[§37 Regular Submanifolds#^prop-37-9|§37.9]] Regular Submanifolds of $\mathbb{R}^{n+k}$: The Fourth Description, Theorem [[§26 Transversality#^thm-26-1|§26.1]] Preimages of Transverse Level Sets, Proposition [[§26 Transversality#^prop-26-4|§26.4]] Transverse Intersections
- [ ] ★ Theorem [[§39 Transversality and Lagrange Multipliers#^thm-39-6|§39.6]] Lagrange Multipliers: HW5.4.

**Drill**
- [ ] Notes drill: [[Differentiable Manifolds Notes Drill#Definitions T7|definitions]] · [[Differentiable Manifolds Notes Drill#Proofs T7|proofs and class exercises]]
- [ ] 2025 midterm, Part 2.6: is a submersion transverse to every submanifold?
- [ ] 2025 midterm, Part 3.9: graph and diagonal transverse. Use the tangent space of a product, Theorem [[§31 Tangent Vectors as Velocities of Curves#^thm-31-6|§31.6]] The Tangent Space of a Product.
- [ ] 2021 midterm, Part 2.7: intersection of submanifolds of $\mathbb{R}^3$ vs transversality.
- [ ] 2021 midterm, Part 3.9: the differential of a restriction to an invariant submanifold.
- [ ] Homework drills: [[Differentiable Manifolds HW Drill#^hw2-5|HW2.5]], [[Differentiable Manifolds HW Drill#^hw5-2|HW5.2]], [[Differentiable Manifolds HW Drill#^hw5-4|HW5.4]]

## T8. Fibrations (§40–§42)
**Language**
- [ ] Definition [[§40 Fibrations#^def-40-1|§40.1]] Fibration, Definition [[§40 Fibrations#^def-40-2|§40.2]] Trivial Fibration, Definition [[§40 Fibrations#^def-40-3|§40.3]] Section, Definition [[§40 Fibrations#^def-40-4|§40.4]] Local Section, Definition [[§40 Fibrations#^def-40-5|§40.5]] Vertical Space
- [ ] Vector bundle: your own box (see the gap above).

**Proofs**
- [ ] ★★ Proposition [[§40 Fibrations#^prop-40-1|§40.1]] Fibres and Fibrations, Proposition [[§40 Fibrations#^prop-40-2|§40.2]] Fibres Are Copies of the Model Fibre
- [ ] ★★ Proposition [[§40 Fibrations#^prop-40-4|§40.4]] Local Trivializations Give Local Sections
- [ ] ★ Proposition [[§41 Examples of Fibrations#^prop-41-1|§41.1]] The Möbius Band Is a Fibration, Proposition [[§40 Fibrations#^prop-40-5|§40.5]] Splitting Along a Section, Proposition [[§42 The Normal Bundle of a Submanifold of Euclidean Space#^prop-42-2|§42.2]] The Normal Bundle Is a Fibration
- [ ] Know the statement of Theorem [[§40 Fibrations#^thm-40-3|§40.3]] Ehresmann's Theorem, and why each hypothesis is needed: Example [[§40 Fibrations#^ex-40-1|§40.1]] A Submersion That Is Not a Fibration, Example [[§40 Fibrations#^ex-40-2|§40.2]] All Fibres Diffeomorphic but Not a Fibration.

**Drill**
- [ ] Notes drill: [[Differentiable Manifolds Notes Drill#Definitions T8|definitions]] · [[Differentiable Manifolds Notes Drill#Proofs T8|proofs and class exercises]]
- [ ] Homework drills: [[Differentiable Manifolds HW Drill#^hw4-4|HW4.4]], [[Differentiable Manifolds HW Drill#^hw5-5|HW5.5]]
- [ ] 2025 midterm, Part 2.5: the punctured plane over a line, a fibration?
- [ ] 2021 midterm, Part 2.5: is every surjective submersion a fibration?
- [ ] 2025 midterm, Part 1.3: explain a vector bundle.

## T9. Immersions and embeddings (§43–§44)
**Language**
- [ ] Definition [[§43 Immersions#^def-43-1|§43.1]] Immersions, Definition [[§44 Embeddings#^def-44-1|§44.1]] Embedding, Definition [[§44 Embeddings#^def-44-2|§44.2]] Proper Map, Definition [[§44 Embeddings#^def-44-3|§44.3]] Locally Closed Subset, Definition [[§44 Embeddings#^def-44-4|§44.4]] Immersed Submanifold

**Proofs**
- [ ] ★★ Theorem [[§43 Immersions#^thm-43-1|§43.1]] Local Normal Form for Immersions
- [ ] ★★ Theorem [[§44 Embeddings#^thm-44-1|§44.1]] The Image of an Embedding Is a Regular Submanifold: 2025 Part 3.8 asked exactly this, using the immersion normal form.
- [ ] ★★ Theorem [[§44 Embeddings#^thm-44-5|§44.5]] Injective Proper Immersions Are Embeddings and Corollary [[§44 Embeddings#^cor-44-6|§44.6]] Injective Immersions of Compact Manifolds
- [ ] ★★ Corollary [[§44 Embeddings#^cor-44-3|§44.3]] An Embedding Is a Diffeomorphism onto Its Image
- [ ] ★ Proposition [[§44 Embeddings#^prop-44-10|§44.10]] Sections Are Closed Embeddings: HW5.1.
- [ ] ★ Proposition [[§44 Embeddings#^prop-44-12|§44.12]] The Irrational Line on the Torus, Proposition [[§44 Embeddings#^prop-44-13|§44.13]] Images of Injective Immersions, Proposition [[§44 Embeddings#^prop-44-15|§44.15]] When an Immersed Submanifold Is Regular

**Drill**
- [ ] Notes drill: [[Differentiable Manifolds Notes Drill#Definitions T9|definitions]] · [[Differentiable Manifolds Notes Drill#Proofs T9|proofs and class exercises]]
- [ ] Homework drills: [[Differentiable Manifolds HW Drill#^hw4-5|HW4.5]], [[Differentiable Manifolds HW Drill#^hw5-1|HW5.1]]
- [ ] 2021 midterm, Part 1.1: injective immersion vs embedding, compared and contrasted.
- [ ] 2021 midterm, Part 2.4: is a composition of embeddings an embedding?
- [ ] 2025 midterm, Part 2.7: is an injective immersion of $S^m$ an embedding?

## T10. Tangent and cotangent bundles, one-forms, the Hessian (§49–§55)
**Language**
- [ ] Definition [[§51 The Tangent Bundle#^def-51-1|§51.1]] The Tangent Bundle as a Set, Definition [[§51 The Tangent Bundle#^def-51-4|§51.4]] Local Trivializations of $TM$, Definition [[§51 The Tangent Bundle#^def-51-5|§51.5]] Charts of $TM$
- [ ] Definition [[§52 The Cotangent Bundle#^def-52-5|§52.5]] Charts of $T^{\ast}M$: *give a smooth atlas of $T^\ast M$* (2021 Part 1.2).
- [ ] Definition [[§53 One-Forms#^def-53-1|§53.1]] One-Form, Definition [[§54 Critical Points and the Hessian#^def-54-2|§54.2]] Hessian at a Critical Point, Definition [[§54 Critical Points and the Hessian#^def-54-3|§54.3]] Nondegenerate Critical Point, Definition [[§54 Critical Points and the Hessian#^def-54-4|§54.4]] Morse Function

**Proofs**
- [ ] ★★ Proposition [[§51 The Tangent Bundle#^prop-51-3|§51.3]] The Topology and Smooth Structure of $TM$ and Proposition [[§51 The Tangent Bundle#^prop-51-2|§51.2]] The Transition Maps of $TM$: topology, then atlas.
- [ ] ★★ Proposition [[§52 The Cotangent Bundle#^prop-52-1|§52.1]] The Transition Maps of $T^{\ast}M$, Proposition [[§51 The Tangent Bundle#^prop-51-3|§51.3]] The Topology and Smooth Structure of $TM$
- [ ] ★★ Proposition [[§53 One-Forms#^prop-53-2|§53.2]] The Differential of a Function Is a One-Form
- [ ] ★ Proposition [[§54 Critical Points and the Hessian#^prop-54-3|§54.3]] The Hessian at a Critical Point Is Well Defined, Theorem [[§55 Morse Functions and the Zero Section#^thm-55-7|§55.7]] Transversality to the Zero Section (HW5.3), Corollary [[§55 Morse Functions and the Zero Section#^cor-55-8|§55.8]] Critical Points of a Morse Function Are Isolated

**Drill**
- [ ] Notes drill: [[Differentiable Manifolds Notes Drill#Definitions T10|definitions]] · [[Differentiable Manifolds Notes Drill#Proofs T10|proofs and class exercises]]
- [ ] Homework drills: [[Differentiable Manifolds HW Drill#^hw5-3|HW5.3]]

## T11. Vector fields, the bracket, $F$-related fields (§56–§59)
In scope exactly as Uribe's email lists it. Lie groups (§60–§61) are **not** on the midterm.

**Language**
- [ ] Definition [[§56 Vector Fields#^def-56-1|§56.1]] Vector Field, Definition [[§56 Vector Fields#^def-56-2|§56.2]] The Space of Vector Fields, Definition [[§56 Vector Fields#^def-56-3|§56.3]] Product of a Function and a Vector Field: a vector field as a section of $TM$.
- [ ] Definition [[§56 Vector Fields#^def-56-4|§56.4]] Operator on $C^\infty(M)$, Definition [[§56 Vector Fields#^def-56-5|§56.5]] Derivation of $C^\infty(M)$, Definition [[§56 Vector Fields#^def-56-6|§56.6]] Local Operator: a vector field as an operator on functions.
- [ ] Definition [[§58 Lie Bracket and Lie Algebra#^def-58-1|§58.1]] The Lie Bracket of Vector Fields, Definition [[§58 Lie Bracket and Lie Algebra#^def-58-2|§58.2]] Lie Algebra
- [ ] Definition [[§59 Related Vector Fields#^def-59-1|§59.1]] Pushforward of a Vector Field by a Diffeomorphism, Definition [[§59 Related Vector Fields#^def-59-2|§59.2]] $F$-Related Vector Fields

**Proofs**
- [ ] ★★ Lemma [[§56 Vector Fields#^lem-56-3|§56.3]] A Vector Field Is a Derivation and Proposition [[§56 Vector Fields#^prop-56-7|§56.7]] Derivations Are Vector Fields: the two views agree (derivations of $C^\infty(M)$ are vector fields).
- [ ] ★★ Lemma [[§56 Vector Fields#^lem-56-6|§56.6]] Derivations Are Local: derivations are local; uses Corollary [[§56 Vector Fields#^cor-56-5|§56.5]] Every Germ Has a Global Representative (quote Proposition [[§56 Vector Fields#^prop-56-4|§56.4]] Bump Functions Exist).
- [ ] ★★ Lemma [[§58 Lie Bracket and Lie Algebra#^lem-58-1|§58.1]] The Bracket of Vector Fields Is a Vector Field: the bracket is again a vector field.
- [ ] ★★ Proposition [[§58 Lie Bracket and Lie Algebra#^prop-58-2|§58.2]] The Bracket in Coordinates: **compute brackets in coordinates**, e.g. Example [[§58 Lie Bracket and Lie Algebra#^ex-58-1|§58.1]] A Bracket in the Plane.
- [ ] ★★ Proposition [[§59 Related Vector Fields#^prop-59-1|§59.1]] Related Fields as Operators and Proposition [[§59 Related Vector Fields#^prop-59-3|§59.3]] Naturality of the Bracket: $F$-related fields as operators, and naturality of the bracket.
- [ ] ★ Lemma [[§56 Vector Fields#^lem-56-8|§56.8]] A Smoothness Criterion for Vector Fields, Proposition [[§58 Lie Bracket and Lie Algebra#^prop-58-4|§58.4]] Commutators of an Associative Product, Corollary [[§58 Lie Bracket and Lie Algebra#^cor-58-5|§58.5]] Vector Fields Form a Lie Algebra, Proposition [[§59 Related Vector Fields#^prop-59-2|§59.2]] Pushforward by a Diffeomorphism, Corollary [[§59 Related Vector Fields#^cor-59-4|§59.4]] Diffeomorphisms Preserve Brackets, Example [[§59 Related Vector Fields#^ex-59-1|§59.1]] Fields Related by a Projection

**Drill**
- [ ] Notes drill: [[Differentiable Manifolds Notes Drill#Definitions T11|definitions]] · [[Differentiable Manifolds Notes Drill#Proofs T11|proofs and class exercises]]

## Strategies: the grammar of 591
Each one is a reusable move. Before writing a proof, name the move.

- **S1 Check in a chart, then show the choice of chart does not matter.** Transition maps are smooth, so "smooth in some chart" means "smooth in every chart": Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-1|§19.1]] Some Chart Suffices, Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-2|§19.2]] Smoothness of a Map Does Not Depend on the Charts, Definition [[§29 Coordinate Derivations and the Basis Theorem#^def-29-2|§29.2]] Coordinate Derivations.
- **S2 Define on representatives, then check well-definedness.** Germs, cosets, quotients, $[f]$ in $I_p/I_p^2$, $\ell_0$ on a span.
- **S3 Maps out of a quotient go through the universal property**: Theorem [[§5 Quotient Maps#^thm-5-1|§5.1]] Universal Property of a Quotient Map.
- **S4 Quotient → manifold.** Hausdorff via a closed relation; second countable via images of a countable basis under an open quotient map: Theorem [[§6 Open Quotients#^thm-6-1|§6.1]] Hausdorff Criterion, Theorem [[§6 Open Quotients#^thm-6-3|§6.3]] Second Countability of Open Quotients.
- **S5 Regular value theorem on a well-chosen map**, e.g. $A \mapsto A^{\mathsf T} A$, $\det$, (trace, det): Theorem [[§7 The Regular Value Theorem#^thm-7-3|§7.3]] Regular Value Theorem, Theorem [[§38 The Regular Value Theorem for Manifolds#^thm-38-2|§38.2]] The Regular Value Theorem for Manifolds.
- **S6 Tangent space of a level set = kernel of the differential.** Prove $\subseteq$, then count dimensions: Theorem [[§25 The Geometric Tangent Space#^thm-25-3|§25.3]] The Geometric Tangent Space Is the Kernel of the Jacobian, Proposition [[§37 Regular Submanifolds#^prop-37-6|§37.6]] Tangent Spaces of a Regular Submanifold.
- **S7 Linear algebra closes the gap.** An injective map between spaces of equal dimension is onto; rank–nullity; a subspace of full dimension is everything.
- **S8 Normal forms give charts.** Submersion and immersion normal forms ⇒ adapted charts: Theorem [[§36 Submersions#^thm-36-6|§36.6]] Local Normal Form for Submersions, Theorem [[§43 Immersions#^thm-43-1|§43.1]] Local Normal Form for Immersions.
- **S9 A derivation is determined by the coordinate functions** (Hadamard): Lemma [[§29 Coordinate Derivations and the Basis Theorem#^lem-29-3|§29.3]] Hadamard's Lemma, Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]] Basis Theorem.
- **S10 Compute $F_{\ast}$ with curves**: $F_{\ast}(\gamma'(0)) = (F \circ \gamma)'(0)$, Corollary [[§31 Tangent Vectors as Velocities of Curves#^cor-31-5|§31.5]] Velocity of a Composite.
- **S11 Local, then global.** Germs, shrinking neighbourhoods, bump functions: Lemma [[§28 Derivations and the Abstract Tangent Space#^lem-28-8|§28.8]] Open Subsets Have the Same Abstract Tangent Spaces, Corollary [[§56 Vector Fields#^cor-56-5|§56.5]] Every Germ Has a Global Representative.
- **S12 Transversality = the images span.** Reduce to a regular value of a composite with a local defining map: Theorem [[§39 Transversality and Lagrange Multipliers#^thm-39-1|§39.1]] Preimages of Transverse Submanifolds.
- **S13 Compactness upgrades local to global**: closed images, proper maps, finitely many critical points: Theorem [[§36 Submersions#^thm-36-10|§36.10]] Submersions from Compact Manifolds, Theorem [[§44 Embeddings#^thm-44-5|§44.5]] Injective Proper Immersions Are Embeddings, Corollary [[§55 Morse Functions and the Zero Section#^cor-55-8|§55.8]] Critical Points of a Morse Function Are Isolated.
- **S13′ Connectedness upgrades local to global**: a local property plus a clopen set gives a global one, Theorem [[§2 Topological Manifolds#^thm-2-8|§2.8]] Connected Manifolds Are Path Connected, Proposition [[§30 The Differential in Coordinates#^prop-30-10|§30.10]] Maps with Zero Differential Are Constant.
- **S14 Differentiate an identity**, e.g. $\pi \circ s = \mathrm{id}$ or $G \circ F =$ const. Test closedness, Hausdorffness and continuity with sequences.
- **S15 Symmetry**: prove it at one point (or on one slice), then move it by the group: homogeneous spaces, classical groups, $\mathrm{SU}(2)$.

(The [[Differentiable Manifolds HW Drill]] lists which homework problems use which move, in its last section.)

## Counterexamples: the vocabulary for Part 2
Know each one's picture and the exact property it breaks.
- [ ] Line with two origins (locally Euclidean + second countable, not Hausdorff): Example [[§2 Topological Manifolds#^ex-2-1|§2.1]] Fails $T_2$: The Line with Two Origins, Example [[§10 The Line with Two Origins#^ex-10-1|§10.1]] The Line with Two Origins
- [ ] $\mathbb{Q}$ (not locally Euclidean); $\mathbb{R}_{\mathrm{disc}} \times \mathbb{R}$ (not second countable): Example [[§2 Topological Manifolds#^ex-2-2|§2.2]] Fails Locally Euclidean: $\mathbb{Q}$, Example [[§2 Topological Manifolds#^ex-2-3|§2.3]] Fails Second Countability: $\mathbb{R}_{\mathrm{disc}} \times \mathbb{R}$
- [ ] A non-open relation, and a non-second-countable quotient: Example [[§4 Quotient Spaces and Open Maps#^ex-4-2|§4.2]] Non-Example, Example [[§4 Quotient Spaces and Open Maps#^ex-4-3|§4.3]] Failure of Second Countability
- [ ] A non-Hausdorff orbit space (the group must be compact): Example [[§13 Group Actions and Orbit Spaces#^ex-13-6|§13.6]] Compactness Is Needed: a Non-Hausdorff Orbit Space; an isotropy group that is not closed: Example [[§14 Homogeneous Spaces#^ex-14-1|§14.1]] An Isotropy Group That Is Not Closed
- [ ] A continuous bijection that is not a homeomorphism: Example [[§15 The Topology of G∕H and Real Grassmannians#^ex-15-2|§15.2]] A Continuous Bijection That Is Not a Homeomorphism
- [ ] Two smooth structures on $\mathbb{R}$ (the $x^3$ chart): Example [[§19 Smooth Functions and Smooth Maps#^ex-19-1|§19.1]] Two Smooth Structures on the Real Line, Example [[§19 Smooth Functions and Smooth Maps#^ex-19-2|§19.2]] The Real Line with the Cube-Root Chart
- [ ] Transversality failing two ways: Example [[§26 Transversality#^ex-26-2|§26.2]] Two Ways Transversality Can Fail
- [ ] A surjective submersion that is not a fibration (punctured plane), and all fibres diffeomorphic but still not a fibration: Example [[§40 Fibrations#^ex-40-1|§40.1]] A Submersion That Is Not a Fibration, Example [[§40 Fibrations#^ex-40-2|§40.2]] All Fibres Diffeomorphic but Not a Fibration
- [ ] An immersion that crosses itself; an injective immersion that is not a homeomorphism onto its image: Example [[§43 Immersions#^ex-43-1|§43.1]] An Immersion That Crosses Itself, Example [[§43 Immersions#^ex-43-2|§43.2]] An Injective Immersion That Is Not a Homeomorphism onto Its Image
- [ ] Immersed but not regular (the irrational line on the torus): Example [[§44 Embeddings#^ex-44-1|§44.1]] Immersed but Not Regular, Proposition [[§44 Embeddings#^prop-44-12|§44.12]] The Irrational Line on the Torus
- [ ] A Hessian matrix that depends on the chart (away from critical points): Example [[§54 Critical Points and the Hessian#^ex-54-1|§54.1]] The Hessian Matrix Depends on the Chart

## Past midterms
The files are in the course folder (`Midterm/midterm-1.pdf` is 2021 and `Midterm/midterm.pdf` is 2025). Each item is mapped to its topic above and deliberately not solved here; use them as timed self-tests.

| Exam | Part 1 | Part 2 | Part 3 |
| --- | --- | --- | --- |
| 2021 (Oct 27) | 1 T9 · 2 T10 | 3 T1 · 4 T9 · 5 T8 · 6 T6 · 7 T7 | 8 T6 · 9 T7 · 10 T4 |
| 2025 (Oct 15) | 1 T4 · 2 T4 · 3 T8 | 4 T1 · 5 T8 · 6 T7 · 7 T9 | 8 T9 · 9 T7 · 10 T2 |

**Drill**
- [ ] Notes drill: [[Differentiable Manifolds Notes Drill#Definitions T11|definitions]] · [[Differentiable Manifolds Notes Drill#Proofs T11|proofs and class exercises]]

