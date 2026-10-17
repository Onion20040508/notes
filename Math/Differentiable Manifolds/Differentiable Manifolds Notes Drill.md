---
type: review
subject: "[[Differentiable Manifolds]]"
tags: [differentiable-manifolds, math591, review]
---
↑ [[Differentiable Manifolds]] · [[Differentiable Manifolds Midterm Review|Midterm Review]] · [[Differentiable Manifolds HW Drill|HW Drill]]

# Notes Drill: definitions, core proofs, class exercises

The companion of the [[Differentiable Manifolds HW Drill|HW Drill]] for everything in the notes that the homework does not cover:
- every definition of the Midterm Review's Language lists, and others the true/false part can use;
- the core proofs (★★, ★, and other results essential for the exam);
- **every result Uribe left as practice in class**, tagged **[class exercise, Lecture N]**;
- the equivalences between the course's different versions of one object (the table "How the definitions grew").

Questions are ordered so that answering them in turn reproduces the definition or the proof:
- **[state]** and **[def]**: state exactly, with every hypothesis;
- **[why]**: what fails without a hypothesis.

The route of each proof in the notes is folded under **Hints**. Results that are homework problems point to the HW Drill instead of repeating them.

**Priorities.** Inside each topic, entries are grouped by where they come from. Work top-down and stop at Priority 2 if time is short.
1. **Homework**: the entry is a homework problem or extends one.
2. **Class**: stated or done in lecture, or left there as an exercise.
3. **Homework technique**: filled in by the notes, but its proof uses a strategy the homework drills often (S1, S2, S4, S5, S6, S7, S8, S9, S10, S13, S14, S15).
4. **Notes only**: optional before the midterm.

Entries: 63 homework, 210 class, 13 homework technique, 16 notes only (Lie-group entries excluded).

# T1. Topological manifolds, quotients, group actions

## Definitions T1

### Priority 1 · homework (directly or extended)

#### Basis of neighborhoods at a point · P1

A basis of neighborhoods (local basis) of $p \in X$ is a collection $(V_\alpha)_{\alpha \in A_p}$ of neighborhoods of $p$ such that every neighborhood $U$ of $p$ contains some $V_\alpha$, see Definition [[§1 Point-Set Topology Review#^def-1-5|§1.5]]. *Source: Lecture 1; used in [[Differentiable Manifolds HW Drill#^hw1-4|HW1.4]].*

^nd-def-1-5

- [ ] Q1 **[def]** State the definition. Must the $V_\alpha$ be open?
- [ ] Q2 **[example]** Give a countable basis of neighborhoods of a point of $\mathbb{R}^n$.
- [ ] Q3 **[use]** How is a basis of the topology of $X$ (Definition [[§1 Point-Set Topology Review#^def-1-1|§1.1]]) related to bases of neighborhoods of its points?
- [ ] Q4 **[why]** Is $\{(-1/n, 1/n)\}$ a basis of neighborhoods of $0$ in $\mathbb{R}$? Is $\{(-1, 1/n)\}$? Which "for every $U$" fails?

> [!tip]- Hints: where it lives
> - Definition [[§1 Point-Set Topology Review#^def-1-5|§1.5]]; used in Definition [[§1 Point-Set Topology Review#^def-1-7|§1.7]] and Proposition [[§1 Point-Set Topology Review#^prop-1-4|§1.4]].

#### First countable · P1

$X$ is first countable at $x_0$ if $x_0$ has a countable basis of neighborhoods, and first countable if it is so at every point, see Definition [[§1 Point-Set Topology Review#^def-1-7|§1.7]]. A second countable space is first countable (Proposition [[§1 Point-Set Topology Review#^prop-1-4|§1.4]]). *Source: Lecture 1; [[Differentiable Manifolds HW Drill#^hw1-4|HW1.4]].*

^nd-def-1-7

- [ ] Q1 **[def]** State first countable at a point, and first countable, through Definition [[§1 Point-Set Topology Review#^def-1-5|§1.5]].
- [ ] Q2 **[use]** Why does second countable imply first countable? From a countable basis $\mathcal{B}$, which members form a local basis at $x_0$? → drilled as [[Differentiable Manifolds HW Drill#^hw1-4-a|HW1.4(a)]].
- [ ] Q3 **[use]** Why is the contrapositive the useful direction? What does one point that is not first countable prove?
- [ ] Q4 **[why]** Is every metric space first countable? Is every metric space second countable? (Think of $\mathbb{R}$ with the discrete metric.)
- [ ] Q5 **[example]** In $\mathbb{R}/\mathbb{Z}$ with all integers collapsed to one point $x_0$, which point fails to be first countable? → drilled as [[Differentiable Manifolds HW Drill#^hw1-4-b|HW1.4(b)]].

> [!tip]- Hints: where it lives, examples
> - Definition [[§1 Point-Set Topology Review#^def-1-7|§1.7]], Proposition [[§1 Point-Set Topology Review#^prop-1-4|§1.4]] (the remark after it: the contrapositive).
> - Q4: balls $B(x, 1/n)$ give a countable local basis in any metric space; the discrete metric on $\mathbb{R}$ is first countable but not second countable (Example [[§1 Point-Set Topology Review#^ex-1-2|§1.2]]).
> - Q5: the bouquet of countably many circles, Example [[§4 Quotient Spaces and Open Maps#^ex-4-4|§4.4]]: a diagonal argument shrinks every candidate neighborhood.

### Priority 2 · stated or done in class

#### Second countable · P2

$X$ is second countable if it has a basis $\{U_\alpha\}_{\alpha \in A}$ with $A$ countable, see Definition [[§1 Point-Set Topology Review#^def-1-6|§1.6]]. *Source: Lecture 1.*

^nd-def-1-6

- [ ] Q1 **[def]** State what a basis of the topology of $X$ is (the "for every $p$ and every open $U \ni p$" form), then state second countable.
- [ ] Q2 **[example]** Why is $\mathbb{R}^n$ second countable? Name a countable basis.
- [ ] Q3 **[why]** Why is $\mathbb{R}$ with the discrete topology not second countable? What must every basis contain?
- [ ] Q4 **[use]** Which constructions preserve second countability (subspaces, products, quotients), and which extra hypothesis does the quotient result need?

> [!tip]- Hints: where it lives, examples
> - Definition [[§1 Point-Set Topology Review#^def-1-6|§1.6]]; basis: Definition [[§1 Point-Set Topology Review#^def-1-1|§1.1]].
> - Example [[§1 Point-Set Topology Review#^ex-1-1|§1.1]] (balls with rational centres and rational radii). Non-examples: Example [[§1 Point-Set Topology Review#^ex-1-2|§1.2]] (every singleton is forced into the basis), Example [[§2 Topological Manifolds#^ex-2-3|§2.3]].
> - Used in: Theorem [[§3 Subspaces and Products#^thm-3-5|§3.5]], Theorem [[§3 Subspaces and Products#^thm-3-12|§3.12]], Theorem [[§6 Open Quotients#^thm-6-3|§6.3]] (needs an open relation; Example [[§4 Quotient Spaces and Open Maps#^ex-4-4|§4.4]] shows a quotient that is not second countable).

#### Hausdorff · P2

Distinct points have disjoint neighbourhoods, see Definition [[§1 Point-Set Topology Review#^def-1-8|§1.8]]. *Source: Lecture 1.*

^nd-def-1-8

- [ ] Q1 **[def]** State the Hausdorff ($T_2$) condition with all quantifiers.
- [ ] Q2 **[example]** Why is every metric space Hausdorff?
- [ ] Q3 **[why]** Why is the line with two origins not Hausdorff? Which two points cannot be separated, and why does every pair of neighbourhoods meet?
- [ ] Q4 **[why]** "Each point has a Euclidean neighbourhood, Euclidean points can be separated, so a locally Euclidean space is Hausdorff." Where exactly does this argument break?
- [ ] Q5 **[use]** For an open relation on $X$, which condition on the graph $\Gamma \subseteq X \times X$ is equivalent to $X/{\sim}$ being Hausdorff?

> [!tip]- Hints: where it lives, examples
> - Definition [[§1 Point-Set Topology Review#^def-1-8|§1.8]].
> - Example [[§1 Point-Set Topology Review#^ex-1-3|§1.3]]; non-example Example [[§1 Point-Set Topology Review#^ex-1-4|§1.4]] and Example [[§2 Topological Manifolds#^ex-2-1|§2.1]]; the trap: the remark *The Exam Trap* in [[§2 Topological Manifolds|§2]] (two points need not share a chart).
> - Used in: Theorem [[§6 Open Quotients#^thm-6-1|§6.1]] Hausdorff Criterion (graph: Definition [[§6 Open Quotients#^def-6-1|§6.1]]), Theorem [[§13 Group Actions and Orbit Spaces#^thm-13-5|§13.5]], Theorem [[§14 Homogeneous Spaces#^thm-14-2|§14.2]] (points closed).

#### Locally Euclidean · P2

There is $n$ such that every point has a neighbourhood homeomorphic to $\mathbb{R}^n$, see Definition [[§2 Topological Manifolds#^def-2-1|§2.1]]. *Source: Lecture 1.*

^nd-def-2-1

- [ ] Q1 **[def]** State locally Euclidean of dimension $n$. Where does "$\exists n$" stand relative to "$\forall p$" in this course?
- [ ] Q2 **[class exercise, Lecture 1]** Show that replacing "homeomorphic to $\mathbb{R}^n$" by "homeomorphic to an open subset of $\mathbb{R}^n$" gives an equivalent definition. Which direction needs a homeomorphism from a ball onto $\mathbb{R}^n$?
- [ ] Q3 **[example]** Why is $S^2$ locally Euclidean? Give two charts.
- [ ] Q4 **[why]** Why is $\mathbb{Q}$ not locally Euclidean of any dimension?

> [!tip]- Hints: where it lives, examples
> - Definition [[§2 Topological Manifolds#^def-2-1|§2.1]]; the quantifier order: the remark *Quantifier Order* in [[§2 Topological Manifolds|§2]].
> - Q2 is Proposition [[§2 Topological Manifolds#^prop-2-3|§2.3]] (Lee leaves it as Exercise 1.1; Uribe called it an exercise in Lecture 1).
> - Example [[§8 Spheres#^ex-8-2|§8.2]]; non-example Example [[§2 Topological Manifolds#^ex-2-2|§2.2]] (a neighbourhood would be countable, $\mathbb{R}^n$ is not, unless $n = 0$, and then points would be open).

#### Topological manifold · P2

A second countable, Hausdorff, locally Euclidean space of dimension $n$, see Definition [[§2 Topological Manifolds#^def-2-2|§2.2]]. *Source: Lecture 1.*

^nd-def-2-2

- [ ] Q1 **[def]** State the definition of a topological manifold of dimension $n$ (three conditions).
- [ ] Q2 **[example]** Why is $S^n$ a topological manifold? Which of the three conditions are inherited from $\mathbb{R}^{n+1}$, and which needs charts?
- [ ] Q3 **[why]** Drop each condition in turn: give a space satisfying the other two but not it (three spaces).
- [ ] Q4 **[class exercise, Lecture 1]** Uribe said he would not prove that the line with two origins is second countable. Prove it: exhibit a countable basis.
- [ ] Q5 **[why]** In the line with two origins, which two of the three conditions hold? Why does having a Euclidean neighbourhood at each point not separate the two origins?

> [!tip]- Hints: where it lives, examples
> - Definition [[§2 Topological Manifolds#^def-2-2|§2.2]]; why the three conditions: the remark *Why These Three Conditions?* in [[§2 Topological Manifolds|§2]].
> - Examples: Proposition [[§8 Spheres#^prop-8-1|§8.1]]; regular level sets, Theorem [[§7 The Regular Value Theorem#^thm-7-3|§7.3]].
> - Q3, Q5: Proposition [[§2 Topological Manifolds#^prop-2-4|§2.4]] with Example [[§2 Topological Manifolds#^ex-2-1|§2.1]] (not $T_2$), Example [[§2 Topological Manifolds#^ex-2-2|§2.2]] (not locally Euclidean), Example [[§2 Topological Manifolds#^ex-2-3|§2.3]] (not second countable).
> - Q4: rational intervals on each copy, plus the sets $(-\varepsilon, 0) \cup \{0_i\} \cup (0, \varepsilon)$ with rational $\varepsilon$; see Example [[§2 Topological Manifolds#^ex-2-1|§2.1]].

#### Chart · P2

A chart at $p$ is a homeomorphism $\varphi : U \to A$ from an open neighbourhood $U$ of $p$ onto an open $A \subseteq \mathbb{R}^n$, see Definition [[§2 Topological Manifolds#^def-2-3|§2.3]]. *Source: Lecture 1.*

^nd-def-2-3

- [ ] Q1 **[def]** State the definition of a chart at $p$, and of the transition function from $(U, \varphi)$ to $(V, \psi)$, including its domain and target.
- [ ] Q2 **[example]** Give two different charts of $S^1$ at the same point.
- [ ] Q3 **[why]** Why is every transition function a homeomorphism between open subsets of $\mathbb{R}^n$, and why is that not enough to do calculus on the manifold?
- [ ] Q4 **[why]** Why can $S^1$ not be covered by a single chart?

> [!tip]- Hints: where it lives, examples
> - Definition [[§2 Topological Manifolds#^def-2-3|§2.3]], Definition [[§2 Topological Manifolds#^def-2-4|§2.4]]; Proposition [[§2 Topological Manifolds#^prop-2-11|§2.11]].
> - Q2: Example [[§17 Differentiable Structures#^ex-17-2|§17.2]], Example [[§17 Differentiable Structures#^ex-17-3|§17.3]]. Q3: the remark *Preview: What Makes a Manifold Differentiable* in [[§2 Topological Manifolds|§2]]. Q4: Proposition [[§17 Differentiable Structures#^prop-17-3|§17.3]].

#### Subspace topology · P2

$V \subseteq S$ is open iff $V = U \cap S$ for some open $U \subseteq X$, see Definition [[§3 Subspaces and Products#^def-3-1|§3.1]]. *Source: Lecture 2.*

^nd-def-3-1

- [ ] Q1 **[def]** State the subspace topology on $S \subseteq X$.
- [ ] Q2 **[use]** State the universal property: when is a map $f : Z \to S$ continuous?
- [ ] Q3 **[example]** Is $[0, 1)$ open in the subspace $[0, 2] \subseteq \mathbb{R}$? Is it open in $\mathbb{R}$?
- [ ] Q4 **[why]** Which properties does a subspace inherit (Hausdorff, second countable), and which does it not (compactness, being a manifold)?

> [!tip]- Hints: where it lives, examples
> - Definition [[§3 Subspaces and Products#^def-3-1|§3.1]]; Proposition [[§3 Subspaces and Products#^prop-3-3|§3.3]]; Theorem [[§3 Subspaces and Products#^thm-3-5|§3.5]]; the remark *What Subspaces Do Not Inherit* in [[§3 Subspaces and Products|§3]].
> - Used for: regular level sets, Definition [[§37 Regular Submanifolds#^def-37-2|§37.2]] (a regular submanifold carries the subspace topology), Definition [[§42 Embeddings#^def-42-1|§42.1]].

#### Product topology · P2

The topology on $X \times Y$ with basis the boxes $U \times V$, $U$, $V$ open, see Definition [[§3 Subspaces and Products#^def-3-3|§3.3]]. *Source: Lecture 2.*

^nd-def-3-3

- [ ] Q1 **[def]** State the product topology on $X \times Y$ via its basis.
- [ ] Q2 **[use]** State the universal property of the product: when is $f = (f_1, f_2) : Z \to X \times Y$ continuous?
- [ ] Q3 **[class exercise, Lecture 2]** Prove the projection $\pi_X : X \times Y \to X$ is open, and that a product of Hausdorff spaces is Hausdorff (both stated "without proof").
- [ ] Q4 **[why]** Is every open subset of $X \times Y$ a box? What is the correct description of open sets (the "box around each point" picture)?

> [!tip]- Hints: where it lives, examples
> - Definition [[§3 Subspaces and Products#^def-3-3|§3.3]]; Proposition [[§3 Subspaces and Products#^prop-3-8|§3.8]]; Theorem [[§3 Subspaces and Products#^thm-3-10|§3.10]]; Q3: Example [[§4 Quotient Spaces and Open Maps#^ex-4-2|§4.2]] (an open set is a union of boxes, and $\pi_X(U \times V) = U$), Theorem [[§3 Subspaces and Products#^thm-3-12|§3.12]] (separate by boxes).
> - The box picture is used again in Theorem [[§6 Open Quotients#^thm-6-1|§6.1]] and Lemma [[§13 Group Actions and Orbit Spaces#^lem-13-3|§13.3]].

#### Quotient topology · P2

$W \subseteq X/{\sim}$ is open iff $\pi^{-1}(W)$ is open in $X$, see Definition [[§4 Quotient Spaces and Open Maps#^def-4-2|§4.2]]. *Source: Lecture 2.*

^nd-def-4-2

- [ ] Q1 **[def]** Define the quotient space $X/{\sim}$, the projection $\pi$, and the quotient topology.
- [ ] Q2 **[use]** Why is $\pi$ continuous, and in what sense is the quotient topology the finest such topology?
- [ ] Q3 **[example]** Describe $\mathbb{CP}^n$ as a quotient of $S^{2n+1}$; which subsets of $\mathbb{CP}^n$ are open?
- [ ] Q4 **[why]** Give a quotient of a metrizable space that is not Hausdorff, and one of a second countable space that is not second countable.
- [ ] Q5 **[class exercise, Lecture 2]** Show that the quotient of two disjoint lines by $(x, 1) \sim (x, 2)$ for $x \neq 0$ is homeomorphic to the line with two origins defined by neighbourhood bases. What do you compare, and on which basic sets?

> [!tip]- Hints: where it lives, examples
> - Definition [[§4 Quotient Spaces and Open Maps#^def-4-1|§4.1]], Definition [[§4 Quotient Spaces and Open Maps#^def-4-2|§4.2]]; Proposition [[§4 Quotient Spaces and Open Maps#^prop-4-1|§4.1]]; the remark *Warning: Nothing Is Automatically Inherited* in [[§4 Quotient Spaces and Open Maps|§4]].
> - Q3: Definition [[§9 Complex Projective Space#^def-9-1|§9.1]]. Q4: Example [[§4 Quotient Spaces and Open Maps#^ex-4-1|§4.1]], Example [[§4 Quotient Spaces and Open Maps#^ex-4-4|§4.4]].
> - Q5: Proposition [[§4 Quotient Spaces and Open Maps#^prop-4-2|§4.2]], whose proof the notes leave as an exercise ("Assigned in lecture"): pull each basic set of Example [[§1 Point-Set Topology Review#^ex-1-4|§1.4]] back along $\pi$.

#### Quotient map · P2

A surjection $F : X \to Y$ with $U$ open iff $F^{-1}(U)$ open, see Definition [[§5 Quotient Maps#^def-5-1|§5.1]]. *Source: Lecture 2.*

^nd-def-5-1

- [ ] Q1 **[def]** State the definition of a quotient map; which direction of the "iff" is plain continuity?
- [ ] Q2 **[example]** Why is the projection $\pi : X \to X/{\sim}$ a quotient map, and why is a continuous open surjection a quotient map?
- [ ] Q3 **[use]** State the universal property: for $g : X \to Z$ constant on the fibres of $p$, what exists, and when is it continuous?
- [ ] Q4 **[why]** Drop the "$\Leftarrow$" (only continuity): give a continuous bijection that is not a quotient map. What goes wrong with the universal property?
- [ ] Q5 **[why]** Is every quotient map open? Give a quotient map that is not open.

> [!tip]- Hints: where it lives, examples
> - Definition [[§5 Quotient Maps#^def-5-1|§5.1]]; constant on fibres: Definition [[§5 Quotient Maps#^def-5-2|§5.2]]; Theorem [[§5 Quotient Maps#^thm-5-1|§5.1]].
> - Q2: Example [[§5 Quotient Maps#^ex-5-1|§5.1]], Proposition [[§5 Quotient Maps#^prop-5-5|§5.5]] (→ also drilled as [[Differentiable Manifolds HW Drill#^hw1-5|HW1.5]]).
> - Q4: Example [[§15 The Topology of G∕H and Real Grassmannians#^ex-15-2|§15.2]] ($\mathbb{R}_{\mathrm{disc}} \to \mathbb{R}$; a bijective quotient map is a homeomorphism). Q5: the projection of Example [[§4 Quotient Spaces and Open Maps#^ex-4-3|§4.3]].

#### Open map · P2

A continuous $F$ with $F(U)$ open for every open $U$, see Definition [[§4 Quotient Spaces and Open Maps#^def-4-3|§4.3]]. *Source: Lecture 2.*

^nd-def-4-3

- [ ] Q1 **[def]** State the definition of an open map (as in the notes, continuity is part of it).
- [ ] Q2 **[example]** Why is $\pi_X : X \times Y \to X$ open? Why is a submersion open?
- [ ] Q3 **[why]** Give a continuous surjection that is not open (from the notes' gluing example).
- [ ] Q4 **[use]** Which theorems about quotients need the projection to be open?

> [!tip]- Hints: where it lives, examples
> - Definition [[§4 Quotient Spaces and Open Maps#^def-4-3|§4.3]]; Example [[§4 Quotient Spaces and Open Maps#^ex-4-2|§4.2]]; Corollary [[§36 Submersions#^cor-36-9|§36.9]] ("locally they are projections").
> - Q3: Example [[§4 Quotient Spaces and Open Maps#^ex-4-3|§4.3]]. Q4: Proposition [[§5 Quotient Maps#^prop-5-5|§5.5]], Theorem [[§6 Open Quotients#^thm-6-1|§6.1]], Theorem [[§6 Open Quotients#^thm-6-3|§6.3]].

#### Open equivalence relation · P2

$\sim$ is open if $\pi : X \to X/{\sim}$ is an open map, see Definition [[§4 Quotient Spaces and Open Maps#^def-4-4|§4.4]]. *Source: Lecture 2.*

^nd-def-4-4

- [ ] Q1 **[def]** State the definition, and the equivalent form in terms of saturations of open sets.
- [ ] Q2 **[example]** Why is the orbit relation of a continuous group action open? Write the saturation of an open $U$ as a union.
- [ ] Q3 **[why]** Glue $0 \sim 1$ in $\mathbb{R}$: compute the saturation of $(-\tfrac12, \tfrac12)$. Why is the relation not open?
- [ ] Q4 **[use]** State the two theorems that make an open quotient Hausdorff, resp. second countable.
- [ ] Q5 **[why]** Where does the proof of second countability use openness? Which non-open quotient of $\mathbb{R}$ fails to be second countable?

> [!tip]- Hints: where it lives, examples
> - Definition [[§4 Quotient Spaces and Open Maps#^def-4-4|§4.4]]; Proposition [[§4 Quotient Spaces and Open Maps#^prop-4-5|§4.5]].
> - Q2: Lemma [[§13 Group Actions and Orbit Spaces#^lem-13-3|§13.3]] ($\tilde U = \bigcup_{g} gU$, each $gU$ open by Lemma [[§13 Group Actions and Orbit Spaces#^lem-13-2|§13.2]]). Q3: Example [[§4 Quotient Spaces and Open Maps#^ex-4-3|§4.3]].
> - Q4: Theorem [[§6 Open Quotients#^thm-6-1|§6.1]], Theorem [[§6 Open Quotients#^thm-6-3|§6.3]]. Q5: images of a countable basis are open only if $\pi$ is open (Lemma [[§5 Quotient Maps#^lem-5-6|§5.6]]); Example [[§4 Quotient Spaces and Open Maps#^ex-4-4|§4.4]].

#### Saturation · P2

$\tilde U = \pi^{-1}(\pi(U))$, the union of the classes meeting $U$, see Definition [[§4 Quotient Spaces and Open Maps#^def-4-5|§4.5]]. *Source: Lecture 2.*

^nd-def-4-5

- [ ] Q1 **[def]** Define the saturation $\tilde U$ of $U \subseteq X$ in three equivalent ways.
- [ ] Q2 **[example]** For the orbit relation of an action of $G$ on $X$, write $\tilde U$ in terms of translates of $U$.
- [ ] Q3 **[why]** Why is $\pi(\tilde U) = \pi(U)$ while in general $\tilde U \neq U$? Give an example with $\tilde U \neq U$.
- [ ] Q4 **[use]** Restate "$\sim$ is open" using saturations.

> [!tip]- Hints: where it lives, examples
> - Definition [[§4 Quotient Spaces and Open Maps#^def-4-5|§4.5]]; Lemma [[§4 Quotient Spaces and Open Maps#^lem-4-3|§4.3]].
> - Q2: Lemma [[§13 Group Actions and Orbit Spaces#^lem-13-3|§13.3]] (Uribe stressed: the saturation is the union of the translates $gU$). Q3: Example [[§4 Quotient Spaces and Open Maps#^ex-4-3|§4.3]]. Q4: Proposition [[§4 Quotient Spaces and Open Maps#^prop-4-5|§4.5]].

#### Saturated set · P2

$S$ is saturated if $S = \tilde S$, equivalently a union of classes, equivalently $S = \pi^{-1}(W)$, see Definition [[§4 Quotient Spaces and Open Maps#^def-4-6|§4.6]]. *Source: Lecture 2.*

^nd-def-4-6

- [ ] Q1 **[def]** State the three equivalent forms of "saturated".
- [ ] Q2 **[why]** Prove the three forms agree.
- [ ] Q3 **[use]** State the saturation correspondence: which subsets of $X$ correspond to the open subsets of $X/{\sim}$?
- [ ] Q4 **[example]** For the orbit relation of $\mathrm{SO}(2)$ on $\mathbb{R}^2$, which open sets are saturated?

> [!tip]- Hints: where it lives, examples
> - Definition [[§4 Quotient Spaces and Open Maps#^def-4-6|§4.6]]; Lemma [[§4 Quotient Spaces and Open Maps#^lem-4-3|§4.3]] (part 4); Proposition [[§4 Quotient Spaces and Open Maps#^prop-4-4|§4.4]].
> - Q4: Example [[§13 Group Actions and Orbit Spaces#^ex-13-4|§13.4]] (orbits are the circles about $0$ and the origin).

#### Topological group · P2

A group with a topology in which multiplication and inversion are continuous, see Definition [[§11 Topological Groups and Classical Matrix Groups#^def-11-1|§11.1]]. *Source: Lecture 3.*

^nd-def-11-1

- [ ] Q1 **[def]** State the definition (which topology on $G \times G$?).
- [ ] Q2 **[example]** Why is $\mathrm{GL}(n, \mathbb{R})$ a topological group? Why is any group with the discrete topology one?
- [ ] Q3 **[why]** Why is every subgroup, with the subspace topology, a topological group?
- [ ] Q4 **[why]** Which axioms make left translation $L_g$ a homeomorphism, and where is that used for group actions?

> [!tip]- Hints: where it lives, examples
> - Definition [[§11 Topological Groups and Classical Matrix Groups#^def-11-1|§11.1]]; Proposition [[§11 Topological Groups and Classical Matrix Groups#^prop-11-4|§11.4]], Example [[§11 Topological Groups and Classical Matrix Groups#^ex-11-1|§11.1]], Proposition [[§11 Topological Groups and Classical Matrix Groups#^prop-11-1|§11.1]].
> - Q4: Lemma [[§13 Group Actions and Orbit Spaces#^lem-13-2|§13.2]], used in Lemma [[§13 Group Actions and Orbit Spaces#^lem-13-3|§13.3]]. Smooth version: Definition [[§57 Lie Groups and Left-Invariant Vector Fields#^def-57-1|§57.1]].

#### Continuous action · P2

An action $G \times X \to X$ of a topological group that is continuous for the product topology, see Definition [[§13 Group Actions and Orbit Spaces#^def-13-2|§13.2]]. *Source: Lecture 3.*

^nd-def-13-2

- [ ] Q1 **[def]** State the two axioms of a (left) action, then continuity.
- [ ] Q2 **[example]** Give the action of $\mathrm{SO}(n)$ on $\mathbb{R}^n$ and of $S^1 = \mathrm{U}(1)$ on $S^{2n+1}$; why are they continuous?
- [ ] Q3 **[why]** $\mathbb{R}^{+}$ acts continuously on $\mathbb{R}^2 \setminus \{0\}$ by $t \cdot (x, y) = (tx, y/t)$. Which conclusion about the orbit space fails, and which hypothesis of the positive theorem is missing?
- [ ] Q4 **[use]** For a continuous action, why is each map $x \mapsto g \cdot x$ a homeomorphism, and why is the orbit map $g \mapsto g \cdot x_0$ continuous?

> [!tip]- Hints: where it lives, examples
> - Definition [[§13 Group Actions and Orbit Spaces#^def-13-1|§13.1]], Definition [[§13 Group Actions and Orbit Spaces#^def-13-2|§13.2]]; Example [[§13 Group Actions and Orbit Spaces#^ex-13-1|§13.1]], Example [[§13 Group Actions and Orbit Spaces#^ex-13-3|§13.3]].
> - Q3: Example [[§13 Group Actions and Orbit Spaces#^ex-13-6|§13.6]] versus Theorem [[§13 Group Actions and Orbit Spaces#^thm-13-5|§13.5]] (needs $G$ compact) → drilled as [[Differentiable Manifolds HW Drill#^hw1-3|HW1.3]].
> - Q4: Lemma [[§13 Group Actions and Orbit Spaces#^lem-13-2|§13.2]], Definition [[§14 Homogeneous Spaces#^def-14-4|§14.4]].

#### Orbit space · P2

$X/G$, the quotient of $X$ by the orbit relation $x \sim y \iff y = g \cdot x$ for some $g$, see Definition [[§13 Group Actions and Orbit Spaces#^def-13-5|§13.5]]. *Source: Lectures 3–4.*

^nd-def-13-5

- [ ] Q1 **[def]** State the orbit relation and the orbit space with its topology; when is $W \subseteq X/G$ open?
- [ ] Q2 **[class exercise, Lecture 3]** Prove that the orbit relation is an equivalence relation and that its classes are the orbits ("a cute exercise").
- [ ] Q3 **[example]** Show that $\mathbb{CP}^n$ is an orbit space. Of which action?
- [ ] Q4 **[why]** Why is an orbit space always an open quotient, but not always Hausdorff? Give the example and the extra hypothesis that repairs it.

> [!tip]- Hints: where it lives, examples
> - Definition [[§13 Group Actions and Orbit Spaces#^def-13-4|§13.4]], Definition [[§13 Group Actions and Orbit Spaces#^def-13-5|§13.5]]; Q2 is Proposition [[§13 Group Actions and Orbit Spaces#^prop-13-1|§13.1]] (inverses for symmetry, products for transitivity; the notes date it Lecture 4, the recording has it on Sep 4, Lecture 3).
> - Q3: Example [[§13 Group Actions and Orbit Spaces#^ex-13-3|§13.3]]. Q4: Lemma [[§13 Group Actions and Orbit Spaces#^lem-13-3|§13.3]]; Example [[§13 Group Actions and Orbit Spaces#^ex-13-6|§13.6]]; Theorem [[§13 Group Actions and Orbit Spaces#^thm-13-5|§13.5]], Corollary [[§13 Group Actions and Orbit Spaces#^cor-13-4|§13.4]].

#### Proper map (topological) · P2

A continuous map is proper if preimages of compact sets are compact, see Definition [[§13 Group Actions and Orbit Spaces#^def-13-6|§13.6]]. *Source: Lecture 4 (remark), Lecture 14.*

^nd-def-13-6

- [ ] Q1 **[def]** State the definition.
- [ ] Q2 **[example]** Why is every continuous map from a compact space to a Hausdorff space proper?
- [ ] Q3 **[why]** Why is the inclusion of an open interval into $\mathbb{R}$ not proper?
- [ ] Q4 **[use]** Which property of proper maps into manifolds replaces compactness in later proofs?

> [!tip]- Hints: where it lives, examples
> - Definition [[§13 Group Actions and Orbit Spaces#^def-13-6|§13.6]] (the same notion is Definition [[§42 Embeddings#^def-42-2|§42.2]]).
> - Q2: compact subsets of a Hausdorff space are closed, closed subsets of a compact space are compact (Proposition [[§1 Point-Set Topology Review#^prop-1-8|§1.8]]). Q4: Proposition [[§42 Embeddings#^prop-42-4|§42.4]] (proper maps into manifolds are closed).

#### Proper action · P2

A continuous action is proper if $\Psi : G \times X \to X \times X$, $\Psi(g, x) = (x, g \cdot x)$, is a proper map, see Definition [[§13 Group Actions and Orbit Spaces#^def-13-7|§13.7]]. *Source: Lecture 4.*

^nd-def-13-7

- [ ] Q1 **[def]** State the definition, including the map $\Psi$.
- [ ] Q2 **[use]** What is the image of $\Psi$, and which hypothesis of the Hausdorff criterion does it concern?
- [ ] Q3 **[example]** Why is every action of a compact group on a Hausdorff space proper?
- [ ] Q4 **[why]** In the proof that $X/G$ is Hausdorff for $G$ and $X$ compact, compactness made $\operatorname{im} \Psi$ closed. Which property of $\Psi$ does that job when $G$ is not compact?

> [!tip]- Hints: where it lives, examples
> - Definition [[§13 Group Actions and Orbit Spaces#^def-13-7|§13.7]]; the map $(\ast)$ in the proof of Corollary [[§13 Group Actions and Orbit Spaces#^cor-13-4|§13.4]]; the remark *Proper Actions* in [[§13 Group Actions and Orbit Spaces|§13]].
> - Q2: $\operatorname{im} \Psi = \Gamma$, the graph of the orbit relation; Theorem [[§6 Open Quotients#^thm-6-1|§6.1]]. Q4: Proposition [[§42 Embeddings#^prop-42-4|§42.4]] (the notes do not prove the proper-action theorem; Lee Ch. 21, Proposition 21.4).

#### Homogeneous space · P2

$X$ is homogeneous for $G$ if $G$ acts continuously and transitively on $X$, see Definition [[§14 Homogeneous Spaces#^def-14-2|§14.2]]. *Source: Lecture 4.*

^nd-def-14-2

- [ ] Q1 **[def]** State transitive action and homogeneous space.
- [ ] Q2 **[example]** Show $S^2$ is homogeneous for $\mathrm{SO}(3)$; what is the isotropy group of $e_3$?
- [ ] Q3 **[use]** State the theorem comparing $G/H_{x_0}$ with $X$: what is $\Phi$, when is it a continuous bijection, when a homeomorphism?
- [ ] Q4 **[why]** Give a homogeneous space where $\Phi : G/H \to X$ is a continuous bijection but not a homeomorphism. Which hypothesis fails?

> [!tip]- Hints: where it lives, examples
> - Definition [[§14 Homogeneous Spaces#^def-14-1|§14.1]], Definition [[§14 Homogeneous Spaces#^def-14-2|§14.2]]; Example [[§14 Homogeneous Spaces#^ex-14-3|§14.3]], Corollary [[§15 The Topology of G∕H and Real Grassmannians#^cor-15-8|§15.8]] (Grassmannians).
> - Q3: Theorem [[§15 The Topology of G∕H and Real Grassmannians#^thm-15-3|§15.3]] → drilled as [[Differentiable Manifolds HW Drill#^hw2-1|HW2.1]]. Q4: Example [[§15 The Topology of G∕H and Real Grassmannians#^ex-15-2|§15.2]].

#### Isotropy subgroup · P2

$H_{x_0} = \{g \in G : g \cdot x_0 = x_0\}$, see Definition [[§14 Homogeneous Spaces#^def-14-3|§14.3]]. *Source: Lecture 4.*

^nd-def-14-3

- [ ] Q1 **[def]** State the definition of the isotropy (stabilizer) subgroup of $x_0$.
- [ ] Q2 **[class exercise, Lecture 4]** Prove $H_{x_0}$ is a subgroup.
- [ ] Q3 **[class exercise, Lecture 4]** Prove $H_{x_0}$ is closed when points of $X$ are closed. Which map is it the preimage under?
- [ ] Q4 **[why]** Show that without "points closed" the conclusion fails: $\mathbb{R}$ acting on $\mathbb{R}/\mathbb{Q}$.
- [ ] Q5 **[example]** What is the isotropy of the north pole under $\mathrm{SO}(3)$?

> [!tip]- Hints: where it lives, examples
> - Definition [[§14 Homogeneous Spaces#^def-14-3|§14.3]]; Q2: Proposition [[§14 Homogeneous Spaces#^prop-14-1|§14.1]]; Q3: Theorem [[§14 Homogeneous Spaces#^thm-14-2|§14.2]] ($H_{x_0} = \theta_{x_0}^{-1}(\{x_0\})$, orbit map Definition [[§14 Homogeneous Spaces#^def-14-4|§14.4]]; Uribe: "this is a closed subgroup", stated without the hypothesis, which the notes add).
> - Q4: Example [[§14 Homogeneous Spaces#^ex-14-1|§14.1]]. Q5: Example [[§14 Homogeneous Spaces#^ex-14-2|§14.2]].

#### Coset space · P2

$G/H = \{gH : g \in G\}$ with the quotient topology from $\pi(g) = gH$, see Definition [[§14 Homogeneous Spaces#^def-14-6|§14.6]]. *Source: Lecture 4.*

^nd-def-14-6

- [ ] Q1 **[def]** Define the left coset $gH$, the coset space $G/H$, the canonical projection, and the topology on $G/H$.
- [ ] Q2 **[use]** Show that $G/H$ is the orbit space of an action of $H$ on $G$. Which action? What does this give for free about $\pi$?
- [ ] Q3 **[why]** When is $G/H$ a group? Why does the course never need that?
- [ ] Q4 **[why]** Under which hypotheses on $G$ and $H$ is $G/H$ compact Hausdorff and second countable?

> [!tip]- Hints: where it lives, examples
> - Definition [[§14 Homogeneous Spaces#^def-14-5|§14.5]], Definition [[§14 Homogeneous Spaces#^def-14-6|§14.6]], Definition [[§14 Homogeneous Spaces#^def-14-7|§14.7]], Definition [[§15 The Topology of G∕H and Real Grassmannians#^def-15-1|§15.1]].
> - Q2: Proposition [[§14 Homogeneous Spaces#^prop-14-4|§14.4]] ($(h, g) \mapsto gh^{-1}$); then $\pi$ is open by Lemma [[§13 Group Actions and Orbit Spaces#^lem-13-3|§13.3]]. Q4: Corollary [[§15 The Topology of G∕H and Real Grassmannians#^cor-15-5|§15.5]].

## Proofs T1

### Priority 1 · homework (directly or extended)

#### Connected manifolds are path connected · P1

Theorem [[§2 Topological Manifolds#^thm-2-8|§2.8]] → drilled as [[Differentiable Manifolds HW Drill#^hw1-1|HW1.1]].

#### Universal property of a quotient map · P1

If $p : X \to Y$ is a quotient map and $g : X \to Z$ is constant on the fibres of $p$, there is a unique $f$ with $f \circ p = g$; $f$ is continuous iff $g$ is, and a quotient map iff $g$ is, see Theorem [[§5 Quotient Maps#^thm-5-1|§5.1]] (the form for $X/{\sim}$ is Corollary [[§5 Quotient Maps#^cor-5-2|§5.2]]). *Source: MATH 590 material, not proved in lecture, used constantly ([[Differentiable Manifolds HW Drill#^hw2-1|HW2.1]], [[Differentiable Manifolds HW Drill#^hw2-2|HW2.2]]); proof in the notes.*

^nd-thm-5-1

- [ ] Q1 **[def]** Define a quotient map (Definition [[§5 Quotient Maps#^def-5-1|§5.1]]).
- [ ] Q2 **[state]** State the theorem, all three conclusions.
- [ ] Q3 Construct $f$: how is $f(y)$ defined, why is it independent of choices, and why is $f$ unique?
- [ ] Q4 Continuity ($\Leftarrow$): for $V \subseteq Z$ open, compute $p^{-1}(f^{-1}(V))$. Which property of $p$ finishes it?
- [ ] Q5 Quotient part: if $g$ is a quotient map, show $f^{-1}(V)$ open $\Rightarrow V$ open. Deduce that a composite of quotient maps is a quotient map.
- [ ] Q6 **[why]** Where are surjectivity of $p$ and "constant on fibres" used? Give a $g$ not constant on fibres for which no $f$ exists.

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S3 (maps out of a quotient go through the universal property).
> - $f(y) := g(x)$ for any $x \in p^{-1}(y)$; surjectivity gives existence and uniqueness.
> - $p^{-1}(f^{-1}(V)) = g^{-1}(V)$ open $\Rightarrow f^{-1}(V)$ open, as $p$ is a quotient map.
> - (2): chain of equivalences $V$ open $\iff f^{-1}(V)$ open $\iff g^{-1}(V)$ open.

#### $\mathbb{CP}^n$ is Hausdorff and second countable · P1

Proposition [[§9 Complex Projective Space#^prop-9-1|§9.1]] → drilled as [[Differentiable Manifolds HW Drill#^hw2-2-a|HW2.2(a)]].

#### Homogeneous spaces are homeomorphic to coset spaces · P1

Theorem [[§15 The Topology of G∕H and Real Grassmannians#^thm-15-3|§15.3]] → drilled as [[Differentiable Manifolds HW Drill#^hw2-1|HW2.1]].

### Priority 2 · stated or done in class

#### Charts onto open subsets suffice · P2

Locally Euclidean may be defined with homeomorphisms $\varphi : U \to A$ onto *open* sets $A \subseteq \mathbb{R}^n$ instead of onto $\mathbb{R}^n$, see Proposition [[§2 Topological Manifolds#^prop-2-3|§2.3]]. *Source: Lecture 1 (reason given in words, "maybe this should be an exercise"); details filled in.* **[class exercise, Lecture 1]**

^nd-prop-2-3

- [ ] Q1 **[state]** State the two versions of "locally Euclidean of dimension $n$" and the claim that they are equivalent.
- [ ] Q2 Which implication is trivial, and why?
- [ ] Q3 Given $\varphi : U \to A$ with $A$ open and $p \in U$, which smaller neighbourhood $U'$ of $p$ do you take, and why is it open in $X$ (not just in $U$)?
- [ ] Q4 Write down an explicit homeomorphism $h : B(c,r) \to \mathbb{R}^n$ and its inverse $g$; check $g \circ h = \mathrm{id}$ and $h \circ g = \mathrm{id}$.
- [ ] Q5 Conclude: which composite is the required chart at $p$?
- [ ] Q6 **[why]** Why is this equivalence the reason restricting a chart to a smaller open set still gives a chart (Lemma [[§2 Topological Manifolds#^lem-2-10|§2.10]])?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: shrink to a ball, then a ball is homeomorphic to $\mathbb{R}^n$.
> - Step 1: take $B = B(\varphi(p), r) \subseteq A$ and $U' = \varphi^{-1}(B)$, open in $U$, hence in $X$.
> - Step 2: $h(y) = (y-c)/(r - |y-c|)$, $g(z) = c + rz/(1+|z|)$ are mutually inverse and continuous.
> - Step 3: the chart is $h \circ \varphi|_{U'}$.

#### The line with two origins: second countable and locally Euclidean, not Hausdorff · P2

The line with two origins is second countable and locally Euclidean of dimension $1$ but not $T_2$, see Example [[§2 Topological Manifolds#^ex-2-1|§2.1]] (the space is Example [[§1 Point-Set Topology Review#^ex-1-4|§1.4]]). *Source: Lecture 1 ("I won't prove [second countability]"); verifications filled in.* **[class exercise, Lecture 1]**

^nd-ex-2-1

- [ ] Q1 **[def]** Define the line with two origins by its neighbourhood bases: what are the basic neighbourhoods $N_i(\varepsilon)$ of $0_1$ and $0_2$?
- [ ] Q2 Why can $0_1$ and $0_2$ not be separated? (Intersect $N_1(\varepsilon)$ with $N_2(\delta)$.)
- [ ] Q3 Give a countable basis. Why do intervals with rational endpoints and the $N_i(q)$, $q \in \mathbb{Q}_{>0}$, suffice?
- [ ] Q4 Give a chart at $0_i$: the map $N_i(\varepsilon) \to (-\varepsilon, \varepsilon)$ sending $0_i \mapsto 0$. What is the image of the basic set $(-m,0) \cup (0,m)$, and why is the map open and continuous?
- [ ] Q5 **[why]** Which of the three manifold axioms does this example show to be independent of the other two? And where does the intuition "locally Euclidean ⇒ Hausdorff" break?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: counterexample library; check each axiom on a basis.
> - Not $T_2$: $N_1(\varepsilon) \cap N_2(\delta) = (-m,0) \cup (0,m) \neq \emptyset$.
> - Second countable: rational intervals in the rays plus $N_i(q)$, $q$ rational.
> - Locally Euclidean: $\varphi$ is a bijection carrying a basis of $N_i(\varepsilon)$ to open sets, and preimages of intervals are open.
> - Used in Proposition [[§2 Topological Manifolds#^prop-2-4|§2.4]] and, as a quotient, in Example [[§10 The Line with Two Origins#^ex-10-1|§10.1]] ([[Differentiable Manifolds HW Drill#^hw1-2|HW1.2]]).

#### The three conditions are independent · P2

Second countability, Hausdorff and locally Euclidean are independent: for each, a space with the other two but not it, see Proposition [[§2 Topological Manifolds#^prop-2-4|§2.4]]. *Source: Lecture 1 (three examples, one-line reasons).*

^nd-prop-2-4

- [ ] Q1 **[state]** State the proposition: what does "independent" mean here?
- [ ] Q2 A space that is $T_2$ and locally Euclidean but not second countable: which one (Example [[§2 Topological Manifolds#^ex-2-3|§2.3]]), and why does no countable basis exist?
- [ ] Q3 A space that is $T_2$ and second countable but not locally Euclidean: why does $\mathbb{Q}$ fail (Example [[§2 Topological Manifolds#^ex-2-2|§2.2]])? Use a cardinality or connectedness argument.
- [ ] Q4 A space that is second countable and locally Euclidean but not $T_2$: the line with two origins (see the entry above).
- [ ] Q5 **[why]** Why does the definition of a manifold need all three? Name one theorem of the course that uses each condition.

> [!tip]- Hints: route of the proof in the notes
> - Strategy: counterexample library.
> - $\mathbb{R}_{\mathrm{disc}} \times \mathbb{R}$: uncountably many disjoint open lines $\{t\} \times \mathbb{R}$, each must contain a basis element.
> - $\mathbb{Q}$: a neighbourhood homeomorphic to $\mathbb{R}^n$ would be countable (so $n = 0$) yet points of $\mathbb{Q}$ are not open.
> - Line with two origins: Example [[§2 Topological Manifolds#^ex-2-1|§2.1]].

#### Transition functions are homeomorphisms · P2

For two charts $(U,\varphi)$, $(V,\psi)$ of a topological manifold, $\varphi(U \cap V)$, $\psi(U \cap V)$ are open in $\mathbb{R}^n$ and $\psi \circ \varphi^{-1}$ is a homeomorphism between them, see Proposition [[§2 Topological Manifolds#^prop-2-11|§2.11]]. *Source: Lecture 1 (stated); filled in.*

^nd-prop-2-11

- [ ] Q1 **[state]** State the proposition, with the domain and codomain of $\psi \circ \varphi^{-1}$.
- [ ] Q2 Why is $\varphi(U \cap V)$ open in $\mathbb{R}^n$? (Two steps: open in $\varphi(U)$, then in $\mathbb{R}^n$.)
- [ ] Q3 Write $\psi \circ \varphi^{-1}$ as a composite of two restricted homeomorphisms.
- [ ] Q4 What is its inverse?
- [ ] Q5 **[why]** Why is "homeomorphism" the most one can say for a topological manifold, and what extra requirement turns an atlas into a smooth one (Definition [[§17 Differentiable Structures#^def-17-4|§17.4]])?

> [!tip]- Hints: route of the proof in the notes
> - Homeomorphisms are open maps; open in open is open (Lemma [[§3 Subspaces and Products#^lem-3-2|§3.2]]).
> - $\psi \circ \varphi^{-1} = \psi|_{U \cap V} \circ \varphi^{-1}|_{\varphi(U \cap V)}$, inverse $\varphi \circ \psi^{-1}$.

#### Manifolds are locally compact · P2

Every point of a topological manifold has an open neighbourhood with compact closure, see Proposition [[§2 Topological Manifolds#^prop-2-12|§2.12]]. *Source: Lecture 14 (asked to be added to the notes).*

^nd-prop-2-12

- [ ] Q1 **[state]** State the proposition; define "locally compact" as used in the notes.
- [ ] Q2 Choose a chart at $q$ and a closed ball $\overline B_\varepsilon(\varphi(q)) \subseteq \varphi(U)$. Define $V$ and $K$.
- [ ] Q3 Why is $K$ compact, and why is it closed in $M$? (Which axiom of a manifold is used?)
- [ ] Q4 Conclude $\overline V \subseteq K$ is compact.
- [ ] Q5 **[why]** Where is this used later (proper maps into manifolds are closed, Proposition [[§42 Embeddings#^prop-42-4|§42.4]])?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: go down to Euclidean space, take a ball, pull it up.
> - $K = \varphi^{-1}(\overline B)$ is compact as a continuous image of a compact set; compact in Hausdorff is closed.
> - $V = \varphi^{-1}(B) \subseteq K$, so $\overline V \subseteq K$, a closed subset of a compact set.

#### Subspaces and products inherit $T_2$ and second countability · P2

A subspace of a $T_2$ (resp. second countable) space is $T_2$ (resp. second countable), see Theorem [[§3 Subspaces and Products#^thm-3-5|§3.5]]; a product of two $T_2$ (resp. second countable) spaces is $T_2$ (resp. second countable), see Theorem [[§3 Subspaces and Products#^thm-3-12|§3.12]]. *Source: Lecture 2 ("I won't prove it … theorem without proof"); filled in.* **[class exercise, Lecture 2]**

^nd-thm-3-5

- [ ] Q1 **[state]** State both theorems (four statements).
- [ ] Q2 Subspace, $T_2$: given $p \ne q$ in $S$, which open sets of $S$ separate them?
- [ ] Q3 Subspace, second countable: which family is a countable basis of $S$, and which lemma says it is a basis (Lemma [[§3 Subspaces and Products#^lem-3-1|§3.1]])?
- [ ] Q4 Product, $T_2$: if $(x,y) \ne (x',y')$, say $x \ne x'$, which two open sets of $X \times Y$ separate them?
- [ ] Q5 Product, second countable: why is $\{U_\alpha \times V_\beta\}$ a basis? (Use the box characterization, Proposition [[§3 Subspaces and Products#^prop-3-8|§3.8]].)
- [ ] Q6 **[why]** Quotients do *not* inherit these properties: which two examples show it (Example [[§4 Quotient Spaces and Open Maps#^ex-4-1|§4.1]], Example [[§4 Quotient Spaces and Open Maps#^ex-4-4|§4.4]])?

> [!tip]- Hints: route of the proof in the notes
> - Subspace: intersect the separating sets (resp. the basis) with $S$.
> - Product: $U \times Y$ and $U' \times Y$; countable product of countable index sets.
> - Used for: open subsets of manifolds, products of manifolds, $X \times X$ Hausdorff in Corollary [[§13 Group Actions and Orbit Spaces#^cor-13-4|§13.4]].

#### Projections are open · P2

$\pi_X : X \times Y \to X$ is an open map, see Example [[§4 Quotient Spaces and Open Maps#^ex-4-2|§4.2]]. *Source: Lecture 2 ("go home and prove them. Check yourself"); filled in.* **[class exercise, Lecture 2]**

^nd-ex-4-2

- [ ] Q1 **[def]** Define an open map (Definition [[§4 Quotient Spaces and Open Maps#^def-4-3|§4.3]]).
- [ ] Q2 Compute $\pi_X(U \times V)$ for a basic open set. What if $V = \emptyset$?
- [ ] Q3 Write a general open $A \subseteq X \times Y$ as a union of boxes; why does $\pi_X$ commute with unions?
- [ ] Q4 **[why]** Is $\pi_X$ closed? Give a closed set of $\mathbb{R}^2$ whose projection is not closed (e.g. the hyperbola $xy = 1$).
- [ ] Q5 How does this give that projections are quotient maps ([[Differentiable Manifolds HW Drill#^hw1-5|HW1.5]], via Proposition [[§5 Quotient Maps#^prop-5-5|§5.5]])?

> [!tip]- Hints: route of the proof in the notes
> - Images commute with unions; images of basis elements are $U$ or $\emptyset$.
> - Then a continuous open surjection is a quotient map: see [[Differentiable Manifolds HW Drill#^hw1-5|HW1.5]].

#### The two constructions of the line with two origins agree · P2

The quotient of two copies of $\mathbb{R}$ glued along $x \neq 0$ is homeomorphic to the line with two origins defined by neighbourhood bases, see Proposition [[§4 Quotient Spaces and Open Maps#^prop-4-2|§4.2]]. *Source: Lecture 2 ("you can check … that the topology we described on Monday is the quotient topology"); the proof in the notes is a sketch, left as an exercise.* **[class exercise, Lecture 2]**

^nd-prop-4-2

- [ ] Q1 **[state]** State the proposition: which bijection, which two topologies?
- [ ] Q2 **[def]** Define the quotient topology (Definition [[§4 Quotient Spaces and Open Maps#^def-4-2|§4.2]]).
- [ ] Q3 For each basic set of Example [[§1 Point-Set Topology Review#^ex-1-4|§1.4]] (an interval in a ray, $N_i(\varepsilon)$), compute its preimage under $\pi$ in $(\mathbb{R} \times \{1\}) \cup (\mathbb{R} \times \{2\})$. Is it open?
- [ ] Q4 Conversely, for $W$ open in the quotient topology and a point of $W$, find a basic set of Example [[§1 Point-Set Topology Review#^ex-1-4|§1.4]] around it inside $W$.
- [ ] Q5 **[why]** How is this used: why does it let you prove non-Hausdorffness by the Hausdorff criterion instead (Example [[§10 The Line with Two Origins#^ex-10-1|§10.1]])?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S2 (compare the two topologies on basic sets, pulling back along $\pi$).
> - $\pi^{-1}(N_1(\varepsilon)) = \big((-\varepsilon,\varepsilon) \times \{1\}\big) \cup \big(((-\varepsilon,0)\cup(0,\varepsilon)) \times \{2\}\big)$, open.
> - The notes leave the details; the verification is the point of the exercise.

#### Openness via saturations · P2

An equivalence relation is open iff the saturation $\tilde U = \pi^{-1}(\pi(U))$ of every open $U$ is open, see Proposition [[§4 Quotient Spaces and Open Maps#^prop-4-5|§4.5]]. *Source: Lecture 2 (stated); proof filled in.*

^nd-prop-4-5

- [ ] Q1 **[def]** Define an open equivalence relation (Definition [[§4 Quotient Spaces and Open Maps#^def-4-4|§4.4]]) and the saturation (Definition [[§4 Quotient Spaces and Open Maps#^def-4-5|§4.5]]).
- [ ] Q2 **[state]** State the proposition.
- [ ] Q3 By the definition of the quotient topology, when is $\pi(U)$ open in $X/{\sim}$?
- [ ] Q4 Conclude the equivalence in one line.
- [ ] Q5 **[why]** Give a relation that is not open (Example [[§4 Quotient Spaces and Open Maps#^ex-4-3|§4.3]]): which open set has a non-open saturation?

> [!tip]- Hints: route of the proof in the notes
> - $\pi(U)$ open $\iff \pi^{-1}(\pi(U))$ open, by definition of the quotient topology.
> - This is the form in which openness is checked in practice: Lemma [[§13 Group Actions and Orbit Spaces#^lem-13-3|§13.3]], Proposition [[§15 The Topology of G∕H and Real Grassmannians#^prop-15-1|§15.1]].

#### Open surjections push bases forward · P2

If $\pi : Y \to Q$ is a continuous open surjection and $\mathcal{B}$ a basis of $Y$, then $\pi(\mathcal{B})$ is a basis of $Q$; so second countability descends, see Lemma [[§5 Quotient Maps#^lem-5-6|§5.6]]. *Source: Lecture 2 (one line); proof in the notes.*

^nd-lem-5-6

- [ ] Q1 **[state]** State the lemma.
- [ ] Q2 Why is each $\pi(B)$ open?
- [ ] Q3 Given $q \in W$ open: lift $q$ to $y$, find $B \in \mathcal{B}$ with $y \in B \subseteq \pi^{-1}(W)$, and conclude $q \in \pi(B) \subseteq W$.
- [ ] Q4 **[why]** Which hypotheses are used where? Why does a non-open quotient map fail to preserve second countability (Example [[§4 Quotient Spaces and Open Maps#^ex-4-4|§4.4]])?

> [!tip]- Hints: route of the proof in the notes
> - Openness gives open images; continuity and surjectivity give the basis property; $\pi(\pi^{-1}(W)) \subseteq W$.

#### Hausdorff criterion · P2

For an open equivalence relation $\sim$ on $X$ with graph $\Gamma$: $X/{\sim}$ is $T_2$ iff $\Gamma$ is closed in $X \times X$, see Theorem [[§6 Open Quotients#^thm-6-1|§6.1]]. *Source: Lecture 2, given in full.*

^nd-thm-6-1

- [ ] Q1 **[def]** Define the graph $\Gamma$ of a relation (Definition [[§6 Open Quotients#^def-6-1|§6.1]]).
- [ ] Q2 **[state]** State the criterion with its hypothesis.
- [ ] Q3 ($\Leftarrow$) For $x \not\sim y$, use that the complement of $\Gamma$ is open to get a box $U \times V$ around $(x,y)$ missing $\Gamma$. Which two open sets of the quotient separate $[x]$ and $[y]$, and why are they open?
- [ ] Q4 Prove the claim $\pi(U) \cap \pi(V) = \emptyset$.
- [ ] Q5 ($\Rightarrow$) Given disjoint $A \ni [x]$, $B \ni [y]$ in the quotient, which neighbourhood of $(x,y)$ in $X \times X$ misses $\Gamma$? Prove it does.
- [ ] Q6 **[why]** Which direction uses openness of $\sim$? Deduce the diagonal criterion (Corollary [[§6 Open Quotients#^cor-6-2|§6.2]]).

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S4 (quotient → manifold: Hausdorff via a closed relation).
> - ($\Leftarrow$) box characterization, then push forward $U$, $V$ (open because $\sim$ is open); a common point would give $(a,b) \in (U \times V) \cap \Gamma$.
> - ($\Rightarrow$) pull back: $\pi^{-1}(A) \times \pi^{-1}(B)$; openness of $\sim$ not needed.

#### Second countability of open quotients · P2

If $\sim$ is open and $X$ is second countable, then $X/{\sim}$ is second countable, see Theorem [[§6 Open Quotients#^thm-6-3|§6.3]]. *Source: Lecture 2 ("project the countable basis").*

^nd-thm-6-3

- [ ] Q1 **[state]** State the theorem.
- [ ] Q2 Why is $\pi : X \to X/{\sim}$ a continuous open surjection?
- [ ] Q3 Which lemma finishes, and what is the countable basis of the quotient?
- [ ] Q4 **[why]** Without openness the conclusion fails: describe $\mathbb{R}$ with $\mathbb{Z}$ collapsed (Example [[§4 Quotient Spaces and Open Maps#^ex-4-4|§4.4]], [[Differentiable Manifolds HW Drill#^hw1-4-b|HW1.4(b)]]).

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S4.
> - Lemma [[§5 Quotient Maps#^lem-5-6|§5.6]]: $\{\pi(B)\}$ for a countable basis $\{B\}$ of $X$.

#### Orbits partition $X$ · P2

The orbit relation $x \sim y \iff y = g \cdot x$ for some $g$ is an equivalence relation whose classes are the orbits, see Proposition [[§13 Group Actions and Orbit Spaces#^prop-13-1|§13.1]]. *Source: Lecture 3 ("a nice exercise, cute exercise to check"; the notes date the claim to Lecture 4); filled in.* **[class exercise, Lecture 3]**

^nd-prop-13-1

- [ ] Q1 **[def]** Define a continuous action (Definition [[§13 Group Actions and Orbit Spaces#^def-13-2|§13.2]]) and the orbit $\mathcal{O}_x$.
- [ ] Q2 **[state]** State the proposition.
- [ ] Q3 Prove reflexivity and symmetry. Which action axioms do you use?
- [ ] Q4 Prove transitivity.
- [ ] Q5 **[why]** Where is it essential that $G$ is a group (inverses), not just a monoid?

> [!tip]- Hints: route of the proof in the notes
> - $x = e \cdot x$; $y = g \cdot x \Rightarrow x = g^{-1} \cdot y$; $z = h \cdot (g \cdot x) = (hg) \cdot x$.

#### Left translations are homeomorphisms · P2

For a continuous action, $L_g(x) = g \cdot x$ is continuous, $L_g \circ L_{g'} = L_{gg'}$, $L_e = \mathrm{id}$, and $L_g$ is a homeomorphism with inverse $L_{g^{-1}}$, see Lemma [[§13 Group Actions and Orbit Spaces#^lem-13-2|§13.2]]. *Source: Lecture 4, in full ("to model what is expected of you").*

^nd-lem-13-2

- [ ] Q1 **[state]** State the three parts.
- [ ] Q2 Write $L_g$ as a composite $X \to G \times X \to X$. Why is the first map continuous (Theorem [[§3 Subspaces and Products#^thm-3-10|§3.10]])?
- [ ] Q3 Prove $L_g \circ L_{g'} = L_{gg'}$ and $L_e = \mathrm{id}_X$ from the action axioms.
- [ ] Q4 Deduce that $L_g$ is a homeomorphism.
- [ ] Q5 **[why]** Why is "a bijection that is continuous" not enough by itself, and what supplies the continuity of the inverse here?

> [!tip]- Hints: route of the proof in the notes
> - $x \mapsto (g,x)$ has continuous components (constant, identity); then the action.
> - $L_g \circ L_{g^{-1}} = L_e = \mathrm{id}$ both ways; $L_{g^{-1}}$ continuous by (1).

#### Orbit relations are open · P2

For a continuous action, the orbit relation is open: the saturation of an open $U$ is $\bigcup_{g} L_g(U)$, see Lemma [[§13 Group Actions and Orbit Spaces#^lem-13-3|§13.3]]. *Source: Lecture 4 (stressed: "the saturation is the union of its translates").*

^nd-lem-13-3

- [ ] Q1 **[state]** State the lemma in both forms.
- [ ] Q2 By which proposition is it enough to show saturations of open sets are open?
- [ ] Q3 Prove the claim $\tilde U = \bigcup_{g \in G} L_g(U)$ by unwinding the definitions.
- [ ] Q4 Why is each $L_g(U)$ open?
- [ ] Q5 **[why]** Which hypothesis on the action is used? Is compactness of $G$ needed? So what does this give for every orbit space $X/G$ with $X$ second countable?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S4 (orbit spaces are open quotients).
> - Proposition [[§4 Quotient Spaces and Open Maps#^prop-4-5|§4.5]]; $y \sim x$ for some $x \in U$ iff $y = g \cdot x$, i.e. $y \in L_g(U)$.
> - Lemma [[§13 Group Actions and Orbit Spaces#^lem-13-2|§13.2]]: homeomorphisms are open; union of open is open.
> - Consequence: Theorem [[§6 Open Quotients#^thm-6-3|§6.3]] applies to every continuous action.

#### Hausdorff orbit spaces (compact group, compact Hausdorff space) · P2

If $G$ and $X$ are compact and $X$ is Hausdorff, a continuous action has Hausdorff orbit space $X/G$, see Corollary [[§13 Group Actions and Orbit Spaces#^cor-13-4|§13.4]]. *Source: Lecture 4.*

^nd-cor-13-4

- [ ] Q1 **[state]** State the corollary.
- [ ] Q2 Which criterion do you apply, and which of its two hypotheses is Lemma [[§13 Group Actions and Orbit Spaces#^lem-13-3|§13.3]]?
- [ ] Q3 Write the graph $\Gamma$ of the orbit relation as the image of a continuous map $\Psi : G \times X \to X \times X$.
- [ ] Q4 Why is $\Gamma$ compact, and why is it closed?
- [ ] Q5 **[why]** Without compactness of $G$ this fails: which example (Example [[§13 Group Actions and Orbit Spaces#^ex-13-6|§13.6]], [[Differentiable Manifolds HW Drill#^hw1-3|HW1.3]])?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S4, S13 (compactness gives closed images).
> - $\Psi(g,x) = (x, g \cdot x)$, image $\Gamma$; $G \times X$ compact; $X \times X$ Hausdorff (Theorem [[§3 Subspaces and Products#^thm-3-12|§3.12]]); compact in Hausdorff is closed.
> - Then Theorem [[§6 Open Quotients#^thm-6-1|§6.1]].

#### Compactness of $X$ is not needed · P2

If a compact group $G$ acts continuously on a Hausdorff space $X$, then $X/G$ is Hausdorff, see Theorem [[§13 Group Actions and Orbit Spaces#^thm-13-5|§13.5]]. *Source: Lecture 4 stated it and declined the proof ("I won't prove it here … another ten minutes"); the tube-lemma proof is filled in.* **[class exercise, Lecture 4]**

^nd-thm-13-5

- [ ] Q1 **[state]** State the theorem and say how it differs from Corollary [[§13 Group Actions and Orbit Spaces#^cor-13-4|§13.4]].
- [ ] Q2 By Lemma [[§13 Group Actions and Orbit Spaces#^lem-13-3|§13.3]] and Theorem [[§6 Open Quotients#^thm-6-1|§6.1]], what is left to show?
- [ ] Q3 Fix $(x,y) \notin \Gamma$. For each $g$, which disjoint open sets $U_g \ni g \cdot x$, $V_g \ni y$, and which $A_g \ni g$, $B_g \ni x$ (continuity of the action at $(g,x)$) do you choose?
- [ ] Q4 Where does compactness of $G$ enter? Define $B$ and $V$.
- [ ] Q5 Show $(B \times V) \cap \Gamma = \emptyset$.
- [ ] Q6 **[why]** Why can't you just say "$\Gamma = \Psi(G \times X)$ is compact" as in the corollary?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S4 plus a tube-lemma argument (S13).
> - Finitely many $A_{g_1}, \ldots, A_{g_m}$ cover $G$; $B = \bigcap B_{g_i}$, $V = \bigcap V_{g_i}$.
> - If $y' = a \cdot x'$ with $x' \in B$, $a \in A_{g_i}$, then $y' \in U_{g_i} \cap V_{g_i} = \emptyset$.

#### The isotropy is a subgroup · P2

$H_{x_0} = \{ g : g \cdot x_0 = x_0 \}$ is a subgroup of $G$, see Proposition [[§14 Homogeneous Spaces#^prop-14-1|§14.1]]. *Source: Lecture 4 ("exercise: claim this is a subgroup").* **[class exercise, Lecture 4]**

^nd-prop-14-1

- [ ] Q1 **[def]** Define the isotropy subgroup (Definition [[§14 Homogeneous Spaces#^def-14-3|§14.3]]).
- [ ] Q2 Show $e \in H_{x_0}$ and closure under products.
- [ ] Q3 Show closure under inverses.
- [ ] Q4 **[why]** Compute the isotropy of a point for $\mathrm{SO}(3)$ acting on $S^2$. Why does it depend on $x_0$ only up to conjugation (Proposition [[§15 The Topology of G∕H and Real Grassmannians#^prop-15-4|§15.4]])?

> [!tip]- Hints: route of the proof in the notes
> - Each step is one action axiom: $(gg') \cdot x_0 = g \cdot (g' \cdot x_0)$; $g^{-1} \cdot x_0 = g^{-1} \cdot (g \cdot x_0)$.

#### Isotropy subgroups are closed · P2

If $G$ acts continuously on $X$ and points of $X$ are closed, then $H_{x_0}$ is closed in $G$, see Theorem [[§14 Homogeneous Spaces#^thm-14-2|§14.2]]. *Source: Lecture 4 ("it's going to be closed … that may be the next assignment … a good exercise"); the notes give only the route.* **[class exercise, Lecture 4]**

^nd-thm-14-2

- [ ] Q1 **[state]** State the theorem with its hypothesis on $X$.
- [ ] Q2 **[def]** Define the orbit map $\theta_{x_0}$ (Definition [[§14 Homogeneous Spaces#^def-14-4|§14.4]]). Why is it continuous?
- [ ] Q3 Write $H_{x_0}$ as a preimage under $\theta_{x_0}$.
- [ ] Q4 Conclude, naming exactly where the hypothesis on $X$ is used.
- [ ] Q5 **[why]** The board statement had no hypothesis on $X$. Give the counterexample (Example [[§14 Homogeneous Spaces#^ex-14-1|§14.1]]): which action, which isotropy group, why not closed?

> [!tip]- Hints: route of the proof in the notes
> - $\theta_{x_0}$ is the action composed with $g \mapsto (g, x_0)$.
> - $H_{x_0} = \theta_{x_0}^{-1}(\{x_0\})$, preimage of a closed point.
> - Counterexample: $\mathbb{R}$ acting on $\mathbb{R}/\mathbb{Q}$ (indiscrete), $H_{[0]} = \mathbb{Q}$.

#### $G/H$ is an orbit space · P2

For $H \le G$, $(h, g) \mapsto g h^{-1}$ is an action of $H$ on $G$ whose orbits are the left cosets, so $G/H$ is its orbit space, see Proposition [[§14 Homogeneous Spaces#^prop-14-4|§14.4]]. *Source: Lecture 4 ("you can check this is an action"; the action law was checked on the board).* **[class exercise, Lecture 4]**

^nd-prop-14-4

- [ ] Q1 **[state]** State the proposition.
- [ ] Q2 Check $e \cdot g = g$ and $(hh') \cdot g = h \cdot (h' \cdot g)$.
- [ ] Q3 Show $\mathcal{O}_g = gH$.
- [ ] Q4 **[why]** Why $gh^{-1}$ and not $gh$? Which axiom fails for $(h,g) \mapsto gh$?
- [ ] Q5 What does this buy: which results on orbit spaces now apply to $G/H$ (Corollary [[§15 The Topology of G∕H and Real Grassmannians#^cor-15-5|§15.5]])?

> [!tip]- Hints: route of the proof in the notes
> - $(hh') \cdot g = g h'^{-1} h^{-1} = h \cdot (h' \cdot g)$.
> - $h \mapsto h^{-1}$ is a bijection of $H$, so $\{gh^{-1}\} = gH$.
> - Then Lemma [[§13 Group Actions and Orbit Spaces#^lem-13-3|§13.3]], Corollary [[§13 Group Actions and Orbit Spaces#^cor-13-4|§13.4]], Theorem [[§6 Open Quotients#^thm-6-3|§6.3]] apply to $G/H$.

#### Homogeneous spaces are coset spaces (the bijection) · P2

If $G$ acts transitively on $X$, $x_0 \in X$, $H = H_{x_0}$, then $\Phi(gH) = g \cdot x_0$ is a well-defined bijection $G/H \to X$, see Lemma [[§14 Homogeneous Spaces#^lem-14-5|§14.5]]. *Source: Lecture 4 (well-definedness on the board); rest filled in.*

^nd-lem-14-5

- [ ] Q1 **[state]** State the lemma.
- [ ] Q2 When are two cosets equal (Lemma [[§14 Homogeneous Spaces#^lem-14-3|§14.3]])? Use it to show $\Phi$ is well defined.
- [ ] Q3 Show $\Phi$ is injective.
- [ ] Q4 Show $\Phi$ is surjective. Which hypothesis?
- [ ] Q5 **[why]** Continuity and the homeomorphism question are a separate matter: see [[Differentiable Manifolds HW Drill#^hw2-1|HW2.1]] and the continuous bijection that is not a homeomorphism (Example [[§15 The Topology of G∕H and Real Grassmannians#^ex-15-2|§15.2]]).

> [!tip]- Hints: route of the proof in the notes
> - $gH = g'H \iff g^{-1}g' \in H$.
> - Injective: apply $L_{g^{-1}}$ to $g \cdot x_0 = g' \cdot x_0$.
> - Surjective: transitivity.

#### $\mathrm{O}(n)$ acts transitively on the Grassmannian · P2

$g \cdot V = gV$ defines a transitive action of $\mathrm{O}(n)$ on $\mathrm{Gr}_k(\mathbb{R}^n)$, see Proposition [[§15 The Topology of G∕H and Real Grassmannians#^prop-15-6|§15.6]]; the isotropy of $V_0 = \mathrm{span}(e_1, \ldots, e_k)$ is $\mathrm{O}(k) \times \mathrm{O}(n-k)$, see Proposition [[§15 The Topology of G∕H and Real Grassmannians#^prop-15-7|§15.7]]. *Source: Lecture 4 ("it's a linear algebra exercise"; Gram–Schmidt indicated); filled in.* **[class exercise, Lecture 4]**

^nd-prop-15-6

- [ ] Q1 **[state]** State both propositions.
- [ ] Q2 Why is $gV$ again a $k$-plane, and why is this an action?
- [ ] Q3 Transitivity: from orthonormal bases adapted to $V$ and to $W$, build $g$ with $gV = W$. Why is $g$ orthogonal?
- [ ] Q4 Isotropy: write $g$ in blocks; why does $gV_0 = V_0$ force the lower-left block $D = 0$, and why then also $C = 0$?
- [ ] Q5 **[why]** Conclude $\mathrm{Gr}_k(\mathbb{R}^n) \cong \mathrm{O}(n)/(\mathrm{O}(k) \times \mathrm{O}(n-k))$ (Corollary [[§15 The Topology of G∕H and Real Grassmannians#^cor-15-8|§15.8]]). Which theorem upgrades the bijection to a homeomorphism, and which hypotheses does it need?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S7 (linear algebra), S15.
> - Gram–Schmidt on $V$, extend by an orthonormal basis of $V^\perp$; $g v_i = w_i$ preserves dot products.
> - Orthogonal maps preserve orthogonal complements: $(gu) \cdot v = u \cdot g^{-1}v = 0$.
> - Then Theorem [[§15 The Topology of G∕H and Real Grassmannians#^thm-15-3|§15.3]] ($\mathrm{O}(n)$ compact, Grassmannian Hausdorff).

### Priority 3 · filled in, using a technique the homework drills

#### The coset projection is open; $G/H$ Hausdorff and second countable · P3

$\pi : G \to G/H$ is a continuous open surjection, hence a quotient map (Proposition [[§15 The Topology of G∕H and Real Grassmannians#^prop-15-1|§15.1]], Corollary [[§15 The Topology of G∕H and Real Grassmannians#^cor-15-2|§15.2]]); if $G$ is compact Hausdorff and $H$ compact, then $G/H$ is compact Hausdorff, and second countable if $G$ is, see Corollary [[§15 The Topology of G∕H and Real Grassmannians#^cor-15-5|§15.5]]. *Source: notes (filled in).*

^nd-cor-15-5

- [ ] Q1 **[state]** State Corollary [[§15 The Topology of G∕H and Real Grassmannians#^cor-15-5|§15.5]].
- [ ] Q2 Why is $\pi$ open? Compute $\pi^{-1}(\pi(U))$ for $U$ open.
- [ ] Q3 Via Proposition [[§14 Homogeneous Spaces#^prop-14-4|§14.4]], which corollary gives Hausdorff, and why is $G/H$ compact?
- [ ] Q4 Which theorem gives second countability?
- [ ] Q5 **[why]** Where is compactness of $H$ needed (hint: $H$ plays the role of the acting group)?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S4, S15 (cosets as orbits).
> - $\pi^{-1}(\pi(U)) = UH = \bigcup_h Uh$, right translations are homeomorphisms.
> - Corollary [[§13 Group Actions and Orbit Spaces#^cor-13-4|§13.4]] for $H$ acting on $G$; $G/H = \pi(G)$; Theorem [[§6 Open Quotients#^thm-6-3|§6.3]].

### Priority 4 · notes only (optional before the midterm)

#### Restricting and recomposing charts; open subsets are manifolds · P4

(1) A chart restricted to an open $U' \subseteq U$ is a chart; (2) a chart composed with a homeomorphism $h$ of an open $W \supseteq \varphi(U)$ onto an open set is a chart, see Lemma [[§2 Topological Manifolds#^lem-2-10|§2.10]]; hence an open subset of a topological $n$-manifold is a topological $n$-manifold, see Proposition [[§3 Subspaces and Products#^prop-3-6|§3.6]]. *Source: notes (filled in).*

^nd-lem-2-10

- [ ] Q1 **[state]** State both parts of the lemma and the proposition on open subsets.
- [ ] Q2 In (1), why is $\varphi(U')$ open in $\mathbb{R}^n$?
- [ ] Q3 In (2), why is $h(\varphi(U))$ open in $\mathbb{R}^n$?
- [ ] Q4 For an open $S \subseteq X$: which theorem gives Hausdorff and second countable, and which chart do you use at $p \in S$?
- [ ] Q5 **[why]** Where does "open" matter? Give a subset of $\mathbb{R}^2$ that is not open and not a $2$-manifold.

> [!tip]- Hints: route of the proof in the notes
> - Homeomorphisms restrict to homeomorphisms onto the image; open in open is open.
> - Open subsets: Theorem [[§3 Subspaces and Products#^thm-3-5|§3.5]] for $T_2$ and second countability, then $(U \cap S, \varphi|_{U \cap S})$, then Proposition [[§2 Topological Manifolds#^prop-2-3|§2.3]].

#### Open surjections are quotient maps · P4

A continuous open surjection is a quotient map, see Proposition [[§5 Quotient Maps#^prop-5-5|§5.5]]. *Source: notes (filled in).*

^nd-prop-5-5

- [ ] Q1 **[state]** State the proposition; what has to be shown, given the definition of quotient map?
- [ ] Q2 Which direction of "$U$ open $\iff F^{-1}(U)$ open" is continuity?
- [ ] Q3 For the other direction, compute $F(F^{-1}(U))$. Which hypotheses do you use, and where?
- [ ] Q4 **[why]** Give a quotient map that is not open (the quotient of Example [[§4 Quotient Spaces and Open Maps#^ex-4-3|§4.3]]), so the converse fails.
- [ ] Q5 Name two places the course uses this: projections ([[Differentiable Manifolds HW Drill#^hw1-5|HW1.5]]), the coset map $G \to G/H$ (Corollary [[§15 The Topology of G∕H and Real Grassmannians#^cor-15-2|§15.2]]).

> [!tip]- Hints: route of the proof in the notes
> - $F(F^{-1}(U)) = U$ by surjectivity, and it is open because $F$ is open.

# T2. Regular values in Euclidean space and the classical groups

## Definitions T2

### Priority 1 · homework (directly or extended)

#### Unitary group · P1

$\mathrm{U}(n) = \{g \in \mathrm{GL}(n, \mathbb{C}) : g^{-1} = g^\ast\}$, see Definition [[§11 Topological Groups and Classical Matrix Groups#^def-11-10|§11.10]]. *Source: Lecture 3; Assignment 2.*

^nd-def-11-10

- [ ] Q1 **[def]** Define $\mathrm{U}(n)$ and its characterization by the Hermitian inner product.
- [ ] Q2 **[example]** What is $\mathrm{U}(1)$?
- [ ] Q3 **[use]** Which map and value exhibit $\mathrm{U}(n)$ as a manifold, and what is its dimension? → drilled as [[Differentiable Manifolds HW Drill#^hw2-4|HW2.4]].
- [ ] Q4 **[why]** Why is $\mathrm{Herm}(n)$ only a real vector space, and why does that matter for counting the dimension?
- [ ] Q5 **[example]** State $T_I \mathrm{U}(n)$.

> [!tip]- Hints: where it lives, examples
> - Definition [[§11 Topological Groups and Classical Matrix Groups#^def-11-10|§11.10]]; Example [[§11 Topological Groups and Classical Matrix Groups#^ex-11-3|§11.3]] ($S^1$); Example [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-23-2|§23.2]], Proposition [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^prop-23-4|§23.4]]; Definition [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^def-23-2|§23.2]] ($(iA)^\ast = -iA$).
> - Q5: skew-Hermitian matrices, Example [[§25 The Geometric Tangent Space#^ex-25-3|§25.3]].

### Priority 2 · stated or done in class

#### Rank of a Jacobian · P2

The rank of $DF_p$ is the dimension of its image; full rank $m$ for $F : \mathbb{R}^N \to \mathbb{R}^m$ means $DF_p$ is onto, see Definition [[§7 The Regular Value Theorem#^def-7-2|§7.2]]. *Source: Lecture 3.*

^nd-def-7-2

- [ ] Q1 **[def]** Define the Jacobian $DF_p$ of $F : \mathbb{R}^N \to \mathbb{R}^m$ (rows, columns) and its rank; list the three equivalent forms of "rank $m$".
- [ ] Q2 **[example]** For $m = 1$ and $m = 2$, what does rank $m$ say about the gradients?
- [ ] Q3 **[why]** Why is rank $m$ impossible when $N < m$, and what is special about $N = m$?
- [ ] Q4 **[use]** Which theorem turns "rank $m$ at every point of $F^{-1}(c)$" into "$F^{-1}(c)$ is a manifold of dimension $N - m$"?

> [!tip]- Hints: where it lives, examples
> - Definition [[§7 The Regular Value Theorem#^def-7-1|§7.1]], Definition [[§7 The Regular Value Theorem#^def-7-2|§7.2]].
> - Q3: Proposition [[§7 The Regular Value Theorem#^prop-7-5|§7.5]], the remark *The Constraint $N \ge m$* in [[§7 The Regular Value Theorem|§7]]. Q4: Theorem [[§7 The Regular Value Theorem#^thm-7-3|§7.3]], Corollary [[§7 The Regular Value Theorem#^cor-7-4|§7.4]].

#### Regular point (in $\mathbb{R}^N$) · P2

$p$ is a regular point of $F : \mathbb{R}^N \to \mathbb{R}^m$ if $DF_p$ is surjective; otherwise critical, see Definition [[§7 The Regular Value Theorem#^def-7-3|§7.3]]. *Source: Lecture 3.*

^nd-def-7-3

- [ ] Q1 **[def]** State regular point and critical point; what does it mean for scalar $F$?
- [ ] Q2 **[example]** Find the critical points of $f(x, y) = x^2 + y^2$.
- [ ] Q3 **[why]** Why does the regular value theorem need regularity at every point of the level set, and not just at most points? Use the level set $f^{-1}(0)$.
- [ ] Q4 **[use]** What replaces "$DF_p$ surjective" for a smooth map of manifolds?

> [!tip]- Hints: where it lives, examples
> - Definition [[§7 The Regular Value Theorem#^def-7-3|§7.3]]; Example [[§7 The Regular Value Theorem#^ex-7-1|§7.1]].
> - Q4: Definition [[§30 The Differential in Coordinates#^def-30-3|§30.3]], Definition [[§36 Submersions#^def-36-3|§36.3]] ($F_{\ast p}$ onto).

#### Regular value (in $\mathbb{R}^N$) · P2

$c$ is a regular value of $F$ if every point of $F^{-1}(c)$ is a regular point; an empty preimage counts, see Definition [[§7 The Regular Value Theorem#^def-7-4|§7.4]]. *Source: Lecture 3.*

^nd-def-7-4

- [ ] Q1 **[def]** State the definition, including the empty-preimage convention.
- [ ] Q2 **[example]** For $f = x^2 + y^2$, classify every $c \in \mathbb{R}$ as regular or critical, and describe $f^{-1}(c)$.
- [ ] Q3 **[why]** Drop the regular-value hypothesis: give a level set that is not a manifold of the predicted dimension.
- [ ] Q4 **[why]** Is "regular value" a condition on $c$ or on the points of $F^{-1}(c)$? Can a value be regular if $F$ has critical points elsewhere?
- [ ] Q5 **[use]** Which regular values give the classical groups? Name the map and the value for $\mathrm{SL}(n)$, $\mathrm{O}(n)$, $\mathrm{U}(n)$.

> [!tip]- Hints: where it lives, examples
> - Definition [[§7 The Regular Value Theorem#^def-7-4|§7.4]]; Example [[§7 The Regular Value Theorem#^ex-7-1|§7.1]] (one critical point on the level set makes the value critical).
> - Q5: Corollary [[§12 The Classical Groups Are Topological Manifolds#^cor-12-3|§12.3]] ($\det$, value $1$), Example [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-23-1|§23.1]] ($g \mapsto gg^{\mathsf T}$, value $I$), Example [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-23-2|§23.2]] ($g \mapsto gg^\ast$, value $I$).
> - Coordinate-free form: Corollary [[§22 The Differential of a Map Between Vector Spaces#^cor-22-4|§22.4]]. Manifold version: Definition [[§36 Submersions#^def-36-4|§36.4]].

#### Coordinate representation · P2

For linear coordinates $L$ on $X$ and $K$ on $Y$, $\widetilde F = K \circ F \circ L^{-1}$; for manifolds, $\psi \circ F \circ \varphi^{-1}$, see Definition [[§22 The Differential of a Map Between Vector Spaces#^def-22-2|§22.2]]. *Source: Lecture 7 (vector spaces), Lecture 5 (manifolds).*

^nd-def-22-2

- [ ] Q1 **[def]** State the coordinate representation of $F : X \to Y$ between vector spaces, of a function $f$ in a chart, and of $F : M \to N$ in charts $(U, \varphi)$, $(V, \psi)$ with $F(U) \subseteq V$.
- [ ] Q2 **[why]** Why is the condition $F(U) \subseteq V$ needed for $\psi \circ F \circ \varphi^{-1}$ to make sense, and how can one always arrange it for continuous $F$?
- [ ] Q3 **[why]** Why does smoothness of the coordinate representation not depend on the choice of coordinates? Which maps appear on either side?
- [ ] Q4 **[example]** Write the coordinate representation of $f(t) = t$ on $\mathbb{R}$ in the chart $\psi(t) = t^{1/3}$.

> [!tip]- Hints: where it lives, examples
> - Definition [[§22 The Differential of a Map Between Vector Spaces#^def-22-1|§22.1]], Definition [[§22 The Differential of a Map Between Vector Spaces#^def-22-2|§22.2]]; Definition [[§29 Coordinate Derivations and the Basis Theorem#^def-29-1|§29.1]] (part 3); Definition [[§19 Smooth Functions and Smooth Maps#^def-19-3|§19.3]].
> - Q2: Lemma [[§19 Smooth Functions and Smooth Maps#^lem-19-3|§19.3]]. Q3: Lemma [[§22 The Differential of a Map Between Vector Spaces#^lem-22-1|§22.1]] (linear changes), Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-2|§19.2]] (transition maps).
> - Q4: Example [[§19 Smooth Functions and Smooth Maps#^ex-19-1|§19.1]] ($f_\psi(s) = s^3$).

#### Differential of a map between vector spaces · P2

$dF_p = K^{-1} \circ \widetilde F'(\tilde p) \circ L$, the linear map making the coordinate square commute, see Definition [[§22 The Differential of a Map Between Vector Spaces#^def-22-5|§22.5]]. *Source: Lecture 7.*

^nd-def-22-5

- [ ] Q1 **[def]** State the definition of $dF_p$ for smooth $F : X \to Y$ between finite-dimensional vector spaces; draw the square.
- [ ] Q2 **[class exercise, Lecture 7]** Prove $dF_p(v) = \frac{d}{dt}\big|_{t=0} F(p + tv)$ ("I really, really encourage you to prove it"). Conclude that $dF_p$ does not depend on $L$, $K$.
- [ ] Q3 **[example]** Compute $d(\det)_g(A)$ and $dF_g(A)$ for $F(g) = gg^{\mathsf T}$ by the curve formula.
- [ ] Q4 **[why]** Why can one not simply define $dF_p$ as "the Jacobian" when $X = \mathrm{Mat}(n, \mathbb{R})$? What would have to be checked?

> [!tip]- Hints: where it lives, examples
> - Definition [[§22 The Differential of a Map Between Vector Spaces#^def-22-5|§22.5]]; Q2: Theorem [[§22 The Differential of a Map Between Vector Spaces#^thm-22-3|§22.3]] (curve $t \mapsto p + tv$ in coordinates, chain rule, $K^{-1}$ commutes with $\frac{d}{dt}$); the remark *What the Curve Method Computes* in [[§22 The Differential of a Map Between Vector Spaces|§22]].
> - Q3: Proposition [[§12 The Classical Groups Are Topological Manifolds#^prop-12-1|§12.1]] ($\det(g)\operatorname{tr}(g^{-1}A)$), Proposition [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^prop-23-1|§23.1]] ($gA^{\mathsf T} + Ag^{\mathsf T}$).
> - Q4: Lemma [[§22 The Differential of a Map Between Vector Spaces#^lem-22-1|§22.1]], Corollary [[§22 The Differential of a Map Between Vector Spaces#^cor-22-4|§22.4]]. The ladder of versions: the equivalence entry *The differential* below.

#### General linear group · P2

$\mathrm{GL}(n, \mathbb{R}) = \det^{-1}(\mathbb{R} \setminus \{0\})$, open in $\mathrm{Mat}(n, \mathbb{R}) \cong \mathbb{R}^{n^2}$, see Definition [[§11 Topological Groups and Classical Matrix Groups#^def-11-5|§11.5]]. *Source: Lecture 3.*

^nd-def-11-5

- [ ] Q1 **[def]** Define $\mathrm{GL}(n, \mathbb{R})$ and its topology.
- [ ] Q2 **[why]** Why is it open in $\mathrm{Mat}(n, \mathbb{R})$, hence a manifold of dimension $n^2$, with no regular value theorem needed?
- [ ] Q3 **[why]** Is $\mathrm{GL}(n, \mathbb{R})$ connected? How many components, and why can it not be fewer?
- [ ] Q4 **[example]** What is its tangent space at $I$?

> [!tip]- Hints: where it lives, examples
> - Definition [[§11 Topological Groups and Classical Matrix Groups#^def-11-2|§11.2]], Definition [[§11 Topological Groups and Classical Matrix Groups#^def-11-5|§11.5]]; Proposition [[§11 Topological Groups and Classical Matrix Groups#^prop-11-3|§11.3]] ($\det$ continuous).
> - Q3: Proposition [[§16 The Classical Groups#^prop-16-1|§16.1]]; Theorem [[§16 The Classical Groups#^thm-16-2|§16.2]] (exactly two, quoted). Q4: all of $\mathrm{Mat}(n, \mathbb{R})$, Theorem [[§25 The Geometric Tangent Space#^thm-25-5|§25.5]].

#### Special linear group · P2

$\mathrm{SL}(n, \mathbb{R}) = \det^{-1}(1)$, see Definition [[§11 Topological Groups and Classical Matrix Groups#^def-11-6|§11.6]]. *Source: Lecture 3.*

^nd-def-11-6

- [ ] Q1 **[def]** Define $\mathrm{SL}(n, \mathbb{R})$. Why is it a closed subgroup?
- [ ] Q2 **[use]** Why is $1$ a regular value of $\det$? Give $\nabla \det(g) \cdot A$.
- [ ] Q3 **[why]** Is $0$ a regular value of $\det$? What goes wrong at $g = 0$ for $n \ge 2$?
- [ ] Q4 **[example]** State its dimension and its tangent space at $I$.

> [!tip]- Hints: where it lives, examples
> - Definition [[§11 Topological Groups and Classical Matrix Groups#^def-11-6|§11.6]]; Proposition [[§12 The Classical Groups Are Topological Manifolds#^prop-12-1|§12.1]], Corollary [[§12 The Classical Groups Are Topological Manifolds#^cor-12-3|§12.3]] (take $A = g$: $\operatorname{tr}(I) = n \neq 0$), Corollary [[§12 The Classical Groups Are Topological Manifolds#^cor-12-5|§12.5]].
> - Q4: dimension $n^2 - 1$, tangent space the trace-zero matrices, Theorem [[§25 The Geometric Tangent Space#^thm-25-5|§25.5]].

#### Orthogonal group · P2

$\mathrm{O}(n) = \{g : (gx) \cdot (gy) = x \cdot y\} = \{g : g^{\mathsf T} g = I\}$, see Definition [[§11 Topological Groups and Classical Matrix Groups#^def-11-7|§11.7]]. *Source: Lecture 3.*

^nd-def-11-7

- [ ] Q1 **[def]** Define $\mathrm{O}(n)$ and prove the equivalence with $g^{\mathsf T} g = I$ and $g^{-1} = g^{\mathsf T}$.
- [ ] Q2 **[use]** Which map and which regular value exhibit $\mathrm{O}(n)$ as a smooth manifold? Why must the target be $\mathrm{Sym}(n)$ and not $\mathrm{Mat}(n)$?
- [ ] Q3 **[example]** State $\dim \mathrm{O}(n)$ and $T_I \mathrm{O}(n)$; derive the latter from a curve.
- [ ] Q4 **[why]** Why is $\mathrm{O}(n)$ compact, and why is it not connected?

> [!tip]- Hints: where it lives, examples
> - Definition [[§11 Topological Groups and Classical Matrix Groups#^def-11-7|§11.7]]; Q1: Proposition [[§11 Topological Groups and Classical Matrix Groups#^prop-11-5|§11.5]].
> - Q2: Example [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-23-1|§23.1]], Proposition [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^prop-23-1|§23.1]] (into $\mathrm{Mat}(n)$, $I$ would not be a regular value: the image of $dF$ lies in $\mathrm{Sym}(n)$). Definition [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^def-23-1|§23.1]].
> - Q3: Example [[§25 The Geometric Tangent Space#^ex-25-2|§25.2]] ($\mathrm{Skew}(n)$, dimension $n(n-1)/2$). Q4: Corollary [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^cor-23-2|§23.2]]; $\det = \pm 1$, Example [[§16 The Classical Groups#^ex-16-1|§16.1]].

#### Special orthogonal group · P2

$\mathrm{SO}(n) = \mathrm{O}(n) \cap \mathrm{SL}(n)$, see Definition [[§11 Topological Groups and Classical Matrix Groups#^def-11-8|§11.8]]. *Source: Lecture 3.*

^nd-def-11-8

- [ ] Q1 **[def]** Define $\mathrm{SO}(n)$.
- [ ] Q2 **[why]** Why is $\mathrm{SO}(n) \neq \mathrm{O}(n)$? Give an element of the difference.
- [ ] Q3 **[use]** Why is $\mathrm{SO}(n)$ a smooth manifold of the same dimension as $\mathrm{O}(n)$ (which subset of $\mathrm{O}(n)$ is it)?
- [ ] Q4 **[example]** Describe $T_I \mathrm{SO}(3)$ by the hat map; which rotations does $\hat v$ generate?

> [!tip]- Hints: where it lives, examples
> - Definition [[§11 Topological Groups and Classical Matrix Groups#^def-11-8|§11.8]]; Q2: Example [[§16 The Classical Groups#^ex-16-1|§16.1]].
> - Q3: Corollary [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^cor-23-2|§23.2]] ($\mathrm{SO}(n) = \mathrm{O}(n) \cap \det^{-1}(0, \infty)$ is open in $\mathrm{O}(n)$, since $\det = \pm 1$ there).
> - Q4: Definition [[§25 The Geometric Tangent Space#^def-25-3|§25.3]], Example [[§25 The Geometric Tangent Space#^ex-25-4|§25.4]].

#### Complex general linear group · P2

$\mathrm{GL}(n, \mathbb{C}) = \det^{-1}(\mathbb{C} \setminus \{0\})$ in $\mathrm{Mat}(n, \mathbb{C}) \cong \mathbb{R}^{2n^2}$, see Definition [[§11 Topological Groups and Classical Matrix Groups#^def-11-9|§11.9]]. *Source: Lecture 3.*

^nd-def-11-9

- [ ] Q1 **[def]** State how $\mathrm{Mat}(n, \mathbb{C})$ is topologized and define $\mathrm{GL}(n, \mathbb{C})$.
- [ ] Q2 **[why]** Why is it open, and of which real dimension?
- [ ] Q3 **[why]** Why is the real rank of a complex-linear map twice its complex rank, and where is this used?

> [!tip]- Hints: where it lives, examples
> - Definition [[§11 Topological Groups and Classical Matrix Groups#^def-11-9|§11.9]].
> - Q2: real dimension $2n^2$. Q3: Lemma [[§7 The Regular Value Theorem#^lem-7-6|§7.6]], used for Corollary [[§7 The Regular Value Theorem#^cor-7-7|§7.7]].

#### External description · P2

Near $p$, $X \cap W = F^{-1}(\vec 0)$ for a smooth $F : W \to \mathbb{R}^k$ with $\vec 0$ a regular value, see Definition [[§20 Manifolds in Euclidean Space#^def-20-1|§20.1]]. *Source: Lecture 5.*

^nd-def-20-1

- [ ] Q1 **[def]** State the external (level-set) description of $X \subseteq \mathbb{R}^{n+k}$ near $p$.
- [ ] Q2 **[example]** Describe $S^2$ externally near the north pole.
- [ ] Q3 **[why]** Why must $\vec 0$ be a regular value, and not just a value with $X \cap W = F^{-1}(\vec 0)$? Give a curve with a cusp that is a level set.
- [ ] Q4 **[use]** Which other descriptions is it equivalent to? (See the equivalence entry *Submanifolds of $\mathbb{R}^N$* below.)

> [!tip]- Hints: where it lives, examples
> - Definition [[§20 Manifolds in Euclidean Space#^def-20-1|§20.1]]; Theorem [[§20 Manifolds in Euclidean Space#^thm-20-1|§20.1]].
> - Q3: the cusp $y^2 = x^3$ is $F^{-1}(0)$ for $F = y^2 - x^3$, with $\nabla F(0) = 0$ (not in the notes); in the notes, the point $f^{-1}(0)$ of Example [[§7 The Regular Value Theorem#^ex-7-1|§7.1]] is a level set but not a $1$-manifold.

#### Internal description · P2

Near $p$, $X \cap W$ is the image of a smooth $\alpha : V \to \mathbb{R}^{n+k}$, $V \subseteq \mathbb{R}^n$ open, a homeomorphism onto $X \cap W$ with $D\alpha$ of rank $n$, see Definition [[§20 Manifolds in Euclidean Space#^def-20-2|§20.2]]. *Source: Lecture 5.*

^nd-def-20-2

- [ ] Q1 **[def]** State the internal (parametric) description near $p$, with all three conditions on $\alpha$.
- [ ] Q2 **[example]** Give the graph parametrization $\alpha(x) = (x, h(x))$; why does it satisfy all three conditions?
- [ ] Q3 **[why]** Drop "homeomorphism onto $X \cap W$": give an injective immersion whose image is not locally a graph.
- [ ] Q4 **[why]** Drop "rank $n$": give a smooth homeomorphism onto a curve with a cusp.

> [!tip]- Hints: where it lives, examples
> - Definition [[§20 Manifolds in Euclidean Space#^def-20-2|§20.2]]; Definition [[§20 Manifolds in Euclidean Space#^def-20-3|§20.3]] (a parametrization is an inverse chart); Theorem [[§20 Manifolds in Euclidean Space#^thm-20-1|§20.1]].
> - Q3: Example [[§42 Embeddings#^ex-42-1|§42.1]] (the figure-eight), Example [[§41 Immersions#^ex-41-2|§41.2]]. Q4: $\alpha(t) = (t^2, t^3)$ (not in the notes): smooth, injective, a homeomorphism onto the cusp $y^2 = x^3$, with $D\alpha_0 = 0$.

## Proofs T2

### Priority 1 · homework (directly or extended)

#### Regular value theorem (in $\mathbb{R}^{n+k}$) · P1

Theorem [[§7 The Regular Value Theorem#^thm-7-3|§7.3]] → drilled as [[Differentiable Manifolds HW Drill#^hw1-6|HW1.6]]. (The version for an open domain and any value, Corollary [[§7 The Regular Value Theorem#^cor-7-4|§7.4]], is the same proof.)

#### Holomorphic regular value theorem · P1

If $F : W \subseteq \mathbb{C}^{n+k} \to \mathbb{C}^k$ is holomorphic and $F'(p)$ has complex rank $k$ on $F^{-1}(c)$, then $F^{-1}(c)$ is a manifold of real dimension $2n$; the real rank of a $\mathbb{C}$-linear map is twice its complex rank, see Corollary [[§7 The Regular Value Theorem#^cor-7-7|§7.7]] and Lemma [[§7 The Regular Value Theorem#^lem-7-6|§7.6]]. *Source: Assignment 2 (used in [[Differentiable Manifolds HW Drill#^hw2-3|HW2.3]]); proof in the notes.*

^nd-cor-7-7

- [ ] Q1 **[state]** State the corollary, including the dimension count.
- [ ] Q2 Prove the lemma: if $v_1, \ldots, v_r$ is a complex basis of the image, why are $v_1, iv_1, \ldots, v_r, iv_r$ a real basis?
- [ ] Q3 Why is complex rank $k$ the same as maximal real rank for $\mathbb{R}^{2n+2k} \to \mathbb{R}^{2k}$?
- [ ] Q4 Which theorem then gives the manifold, and of which dimension?
- [ ] Q5 **[why]** Why is the kernel of $F'(p)$ a complex subspace, and what does this say about the tangent space (Theorem [[§25 The Geometric Tangent Space#^thm-25-3|§25.3]])? Why can a holomorphic $F : \mathbb{C}^N \to \mathbb{C}$ never have real rank $1$?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S5 (regular value theorem), S7 (linear algebra).
> - $\sum c_j v_j = \sum (\operatorname{Re} c_j\, v_j + \operatorname{Im} c_j\, iv_j)$ for spanning; real independence from complex independence.
> - Real rank $2k$ = maximal; Theorem [[§7 The Regular Value Theorem#^thm-7-3|§7.3]] in the form of Corollary [[§7 The Regular Value Theorem#^cor-7-4|§7.4]].

#### Non-degenerate pairings · P1

If $B : V \times W \to \mathbb{R}$ is bilinear and non-degenerate and $V$ or $W$ is finite-dimensional, then $\dim V = \dim W$ and $V \cong W^\ast$, $W \cong V^\ast$ via $B$, see Theorem [[§21 Linear Algebra Toolkit#^thm-21-5|§21.5]]. *Source: linear algebra toolkit (not from lecture); the engine of [[Differentiable Manifolds HW Drill#^hw3-3|HW3.3]].*

^nd-thm-21-5

- [ ] Q1 **[def]** Define a bilinear pairing and non-degeneracy (Definition [[§21 Linear Algebra Toolkit#^def-21-4|§21.4]], Definition [[§21 Linear Algebra Toolkit#^def-21-5|§21.5]]), and the maps $B^\flat$, $B^\sharp$.
- [ ] Q2 **[state]** State the theorem.
- [ ] Q3 Show $W$ is finite-dimensional with $\dim W \le \dim V$. Which non-degeneracy do you use?
- [ ] Q4 Show $\dim V \le \dim W$.
- [ ] Q5 Conclude that $B^\flat$ and $B^\sharp$ are isomorphisms.
- [ ] Q6 **[why]** Why are *both* non-degeneracy conditions needed? Give a degenerate pairing on $\mathbb{R}^2 \times \mathbb{R}$ that is non-degenerate on one side.

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S7 (an injective map between spaces of equal dimension is onto).
> - $B^\sharp : W \hookrightarrow V^\ast$ gives $\dim W \le n$; $B^\flat : V \hookrightarrow W^\ast$ gives $n \le \dim W$.
> - Used in Theorem [[§34 The Cotangent Space from Germs#^thm-34-4|§34.4]].

#### $\mathrm{U}(n)$ is a smooth manifold of dimension $n^2$ · P1

Example [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-23-2|§23.2]] (with Lemma [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^lem-23-3|§23.3]], Proposition [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^prop-23-4|§23.4]]) → drilled as [[Differentiable Manifolds HW Drill#^hw2-4|HW2.4]].

### Priority 2 · stated or done in class

#### Derivative of the determinant (Jacobi's formula) · P2

For $g$ invertible, $\frac{d}{dt}|_{0} \det(g + tA) = \det(g) \operatorname{tr}(g^{-1}A)$; equivalently $\nabla \det(g) = \det(g)(g^{-1})^{\mathsf T}$, see Proposition [[§12 The Classical Groups Are Topological Manifolds#^prop-12-1|§12.1]] and Corollary [[§12 The Classical Groups Are Topological Manifolds#^cor-12-2|§12.2]]. *Source: Lecture 3.*

^nd-prop-12-1

- [ ] Q1 **[state]** State Jacobi's formula in the directional form and the gradient form.
- [ ] Q2 Why is $\nabla \det(g) \cdot A$ the derivative along the line $g + tA$?
- [ ] Q3 Reduce to $g = I$: factor $g + tA = g(I + tV)$. Which property of $\det$ is used?
- [ ] Q4 Show $\frac{d}{dt}|_0 \det(I + tV) = \operatorname{tr} V$ from the Leibniz formula: which permutations contribute?
- [ ] Q5 Read off the gradient: why is $\operatorname{tr}(g^{-1}A) = (g^{-1})^{\mathsf T} \cdot A$?
- [ ] Q6 **[why]** Why must you differentiate before setting $t = 0$ (the student's correction in lecture)?

> [!tip]- Hints: route of the proof in the notes
> - Chain rule along $\gamma(t) = g + tA$; $\det(g + tA) = \det g \det(I + tV)$, $V = g^{-1}A$.
> - Product rule on $\prod_i (\delta_{i\sigma(i)} + tV_{i\sigma(i)})$; a permutation fixing $n-1$ symbols is the identity.

#### $1$ is a regular value of $\det$; $\mathrm{SL}(n,\mathbb{R})$ is a manifold · P2

$\nabla \det(g) \neq 0$ on $\det^{-1}(1)$ (Corollary [[§12 The Classical Groups Are Topological Manifolds#^cor-12-3|§12.3]]; every $c \neq 0$ in Corollary [[§12 The Classical Groups Are Topological Manifolds#^cor-12-4|§12.4]]), so $\mathrm{SL}(n,\mathbb{R})$ is a topological manifold of dimension $n^2 - 1$, see Corollary [[§12 The Classical Groups Are Topological Manifolds#^cor-12-5|§12.5]]. *Source: Lecture 3 (hand-waved; "you will write it in homework six"); filled in.*

^nd-cor-12-5

- [ ] Q1 **[state]** State both corollaries.
- [ ] Q2 **[def]** What does "$1$ is a regular value of $\det$" mean (Definition [[§7 The Regular Value Theorem#^def-7-4|§7.4]])? Which rank is needed?
- [ ] Q3 Which direction $A$ do you plug into Jacobi's formula to show $\nabla \det(g) \neq 0$, and what do you get?
- [ ] Q4 Apply the regular value theorem: to which map, on which $\mathbb{R}^{n+k}$, with which $k$?
- [ ] Q5 **[why]** Why is $0$ a critical value of $\det$ (for $n \ge 2$)? What is $\nabla \det$ at the zero matrix?
- [ ] Q6 How do you upgrade this to a *smooth* manifold (Proposition [[§20 Manifolds in Euclidean Space#^prop-20-2|§20.2]])?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S5 (regular value theorem on a well-chosen map).
> - $A = g$: $\nabla \det(g) \cdot g = \det(g)\operatorname{tr}(I) = cn \neq 0$.
> - $F = \det - 1$ on $\mathbb{R}^{n^2} = \mathbb{R}^{(n^2-1)+1}$, $k = 1$, then Theorem [[§7 The Regular Value Theorem#^thm-7-3|§7.3]].

#### The two descriptions of a submanifold of $\mathbb{R}^{n+k}$ agree · P2

For $X \subseteq \mathbb{R}^{n+k}$ and $p \in X$: the external description (regular level set near $p$), the internal one (parametrization) and the graph description (G) are equivalent, see Theorem [[§20 Manifolds in Euclidean Space#^thm-20-1|§20.1]]. *Source: not given in lecture (Lecture 5 closing remark); proof in the notes.*

^nd-thm-20-1

- [ ] Q1 **[def]** State the external and the internal description (Definition [[§20 Manifolds in Euclidean Space#^def-20-1|§20.1]], Definition [[§20 Manifolds in Euclidean Space#^def-20-2|§20.2]]) and the graph condition (G).
- [ ] Q2 External ⇒ (G): which earlier proof is this, and which theorem produces $h$?
- [ ] Q3 (G) ⇒ external: which defining map $F$, and why does its Jacobian have rank $k$?
- [ ] Q4 (G) ⇒ internal: which parametrization, and what is its inverse?
- [ ] Q5 Internal ⇒ (G): which $n$ rows of $D\alpha_q$ do you use, and where does the inverse function theorem enter? Why is $\alpha(V_1)$ a piece $X \cap (V_2 \times V')$?
- [ ] Q6 **[why]** In the internal description, why is "$\alpha$ is a homeomorphism onto $X \cap W$" needed, not just "injective immersion"? (Think of the figure eight.)

> [!tip]- Hints: route of the proof in the notes
> - External ⇒ (G): Steps 1–3 of Theorem [[§7 The Regular Value Theorem#^thm-7-3|§7.3]] (permute, implicit function theorem).
> - (G) ⇒ external: $F(x,y) = y - h(x)$, Jacobian $(-Dh_x \mid I_k)$.
> - (G) ⇒ internal: $\alpha(x) = (x, h(x))$, inverse the projection.
> - Internal ⇒ (G): $\alpha = (\alpha_1, \alpha_2)$ with $D\alpha_1$ invertible; $h = \alpha_2 \circ \alpha_1^{-1}$.

#### Regular level sets are smooth manifolds · P2

If $W \subseteq \mathbb{R}^{n+k}$ is open, $F : W \to \mathbb{R}^k$ smooth and $c$ a regular value, the graph charts $(U_J, \varphi_J)$ form a smooth atlas on $M = F^{-1}(c)$, so $M$ is a smooth $n$-manifold, see Proposition [[§20 Manifolds in Euclidean Space#^prop-20-2|§20.2]]. *Source: Lecture 6 (a surface first, Example [[§20 Manifolds in Euclidean Space#^ex-20-1|§20.1]], then the general argument).*

^nd-prop-20-2

- [ ] Q1 **[state]** State the proposition. What are the charts $(U_J, \varphi_J)$: which coordinates does $\varphi_J$ keep?
- [ ] Q2 Why is each $(U_J, \varphi_J)$ a chart, and why do the $U_J$ cover $M$?
- [ ] Q3 Why is $\varphi_J^{-1} : V_J \to \mathbb{R}^{n+k}$ smooth in the Euclidean sense?
- [ ] Q4 Factor the transition map $\varphi_{J'} \circ \varphi_J^{-1}$ through $\mathbb{R}^{n+k}$. Why is it smooth?
- [ ] Q5 **[why]** Why do the charts have to be computed in the ambient space? Could you check compatibility without knowing $h_J$ explicitly?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S1 (transition maps), S5.
> - Charts from Theorem [[§7 The Regular Value Theorem#^thm-7-3|§7.3]], Step 3 (Corollary [[§7 The Regular Value Theorem#^cor-7-4|§7.4]] for open $W$, value $c$).
> - $\varphi_J^{-1}(u)$ has components $u^l$ ($l \in I$) or $h_J^l(u)$ ($l \in J$).
> - $\varphi_{J'} \circ \varphi_J^{-1} = \pi_{I'} \circ \varphi_J^{-1}$: smooth parametrization up, linear projection down.

#### Smooth maps into and out of regular level sets · P2

For a regular level set $M \subseteq \mathbb{R}^{n+k}$: (1) restrictions of smooth maps on open $W' \subseteq \mathbb{R}^{n+k}$ to $M \cap W'$ are smooth; (2) a smooth $G : P \to \mathbb{R}^{n+k}$ with image in $M$ is smooth into $M$, see Lemma [[§20 Manifolds in Euclidean Space#^lem-20-3|§20.3]]. *Source: notes (filled in).*

^nd-lem-20-3

- [ ] Q1 **[state]** State both parts.
- [ ] Q2 **[def]** What has to be checked for smoothness of a map between manifolds (Definition [[§19 Smooth Functions and Smooth Maps#^def-19-3|§19.3]])?
- [ ] Q3 (1): which charts do you use on $M$ and on $\mathbb{R}^l$? Write the coordinate representation as a composite of Euclidean smooth maps.
- [ ] Q4 (2): continuity into $M$ comes from which property of the subspace topology? Write $\varphi_J \circ G$ and say why it is smooth.
- [ ] Q5 **[why]** Part (2) fails for images of injective immersions that are not embedded (the figure eight): which step uses that $M$ carries the subspace topology?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S1.
> - (1): $H \circ \varphi_J^{-1}$ on $\varphi_J(U_J \cap W')$.
> - (2): $\varphi_J \circ G = \pi_I \circ G$, linear after smooth; continuity by Proposition [[§3 Subspaces and Products#^prop-3-3|§3.3]].
> - Generalized later by Lemma [[§37 Regular Submanifolds#^lem-37-5|§37.5]].

#### Linear coordinates: a vector space is a smooth manifold · P2

Smoothness of $F : X \to Y$ in linear coordinates does not depend on the coordinates (Lemma [[§22 The Differential of a Map Between Vector Spaces#^lem-22-1|§22.1]]); any two linear coordinate systems are compatible charts, so a finite-dimensional vector space has a canonical smooth structure, see Proposition [[§22 The Differential of a Map Between Vector Spaces#^prop-22-2|§22.2]]. *Source: Lecture 7 ("a little observation"); filled in.*

^nd-lem-22-1

- [ ] Q1 **[def]** Define a linear coordinate system and the coordinate representation $\widetilde F = K \circ F \circ L^{-1}$ (Definition [[§22 The Differential of a Map Between Vector Spaces#^def-22-1|§22.1]], Definition [[§22 The Differential of a Map Between Vector Spaces#^def-22-2|§22.2]]).
- [ ] Q2 **[state]** State the lemma and the proposition.
- [ ] Q3 Express $\widetilde F'$ in terms of $\widetilde F$ for another choice $L'$, $K'$. Why is it smooth?
- [ ] Q4 Why are the charts $(X, L)$, $(X, L')$ compatible, and why do they give the same maximal atlas?
- [ ] Q5 **[why]** Why is the topology on $X$ independent of $L$? What would go wrong in infinite dimensions?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S1.
> - $\widetilde F' = (K'K^{-1}) \circ \widetilde F \circ (LL'^{-1})$, linear isomorphisms are smooth.
> - Transition $L' \circ L^{-1}$ is a linear isomorphism; uniqueness in Theorem [[§17 Differentiable Structures#^thm-17-5|§17.5]].

#### Coordinate-free formula for the differential; regular values without coordinates · P2

For $F : X \to Y$ smooth between vector spaces, $dF_p(v) = \frac{d}{dt}|_{t=0} F(p + tv)$, so $dF_p$ is independent of bases (Theorem [[§22 The Differential of a Map Between Vector Spaces#^thm-22-3|§22.3]]); hence $c$ is a regular value iff $dF_p$ is onto for all $p \in F^{-1}(c)$ (Corollary [[§22 The Differential of a Map Between Vector Spaces#^cor-22-4|§22.4]]). *Source: Lecture 7 ("this will be an exercise for you … I really encourage you to prove it").* **[class exercise, Lecture 7]**

^nd-thm-22-3

- [ ] Q1 **[def]** Define $dF_p$ via linear coordinates (Definition [[§22 The Differential of a Map Between Vector Spaces#^def-22-5|§22.5]]): which square commutes?
- [ ] Q2 **[state]** State the theorem and the corollary.
- [ ] Q3 Write $F(p + tv)$ through $\widetilde F$: what is the coordinate curve of $t \mapsto p + tv$?
- [ ] Q4 Differentiate $\widetilde F(\tilde p + t\tilde v)$ at $0$ by the chain rule. Why does $K^{-1}$ commute with $d/dt$?
- [ ] Q5 Corollary: show $\widetilde F'(\tilde p)$ onto $\iff dF_p$ onto, using that the vertical arrows are bijections.
- [ ] Q6 **[why]** Where do you use the vector space structures of $X$ (forming $p + tv$) and of $Y$ (the difference quotient)? Why does this formula not make sense on a manifold, and what replaces it (Corollary [[§31 Tangent Vectors as Velocities of Curves#^cor-31-3|§31.3]])?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S10 (compute differentials with curves).
> - $L(p + tv) = \tilde p + t\tilde v$; $F(p + tv) = K^{-1}(\widetilde F(\tilde p + t\tilde v))$.
> - Chain rule: $\frac{d}{dt}|_0 \widetilde F(\tilde p + t\tilde v) = \widetilde F'(\tilde p)\tilde v$; $K^{-1}$ linear and continuous.
> - Corollary: $\widetilde F'(\tilde p) = K \circ dF_p \circ L^{-1}$; maximal rank $=$ onto when $\dim X \ge \dim Y$.

#### $\mathrm{O}(n)$ is a smooth manifold; the kernel of the differential · P2

$F(g) = gg^{\mathsf T} : \mathrm{Mat}(n,\mathbb{R}) \to \mathrm{Sym}(n,\mathbb{R})$ has $I$ as a regular value, so $\mathrm{O}(n) = F^{-1}(I)$ is a smooth manifold of dimension $\frac{n(n-1)}{2}$ (Example [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-23-1|§23.1]]), and $\ker dF_g = g \cdot \mathrm{Skew}(n,\mathbb{R})$ (Proposition [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^prop-23-1|§23.1]]). *Source: Lectures 6–7 (the differential by curves; the choice $A = \frac12 Sg$: "we can check it again on Wednesday, but check that this works").* **[class exercise, Lecture 6]**

^nd-ex-23-1

- [ ] Q1 **[state]** State the example and the proposition, with the dimension count.
- [ ] Q2 Why does $F$ land in $\mathrm{Sym}(n,\mathbb{R})$, and why is $F^{-1}(I) = \mathrm{O}(n)$?
- [ ] Q3 Compute $dF_g(A)$ with the curve $g + tA$.
- [ ] Q4 Surjectivity: given $S$ symmetric, find $A$ with $dF_g(A) = S$ and check it. Where do you use $S^{\mathsf T} = S$ and $gg^{\mathsf T} = I$?
- [ ] Q5 Which theorems turn "$dF_g$ onto for all $g \in F^{-1}(I)$" into "smooth manifold of dimension $n^2 - \frac{n(n+1)}{2}$"?
- [ ] Q6 Kernel: substitute $A = gB$ and show $dF_g(gB) = g(B + B^{\mathsf T})g^{\mathsf T}$. Conclude $\ker dF_g = g\,\mathrm{Skew}(n)$ and count its dimension.
- [ ] Q7 **[why]** Why is $F$ taken with values in $\mathrm{Sym}(n)$ and not in $\mathrm{Mat}(n)$? What would fail?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S5, S10, S7.
> - $dF_g(A) = Ag^{\mathsf T} + gA^{\mathsf T} = X + X^{\mathsf T}$ with $X = Ag^{\mathsf T}$; $A = \frac12 Sg$.
> - Corollary [[§22 The Differential of a Map Between Vector Spaces#^cor-22-4|§22.4]] then Proposition [[§20 Manifolds in Euclidean Space#^prop-20-2|§20.2]] (transported by $L$).
> - The kernel is the geometric tangent space at $g$: Example [[§25 The Geometric Tangent Space#^ex-25-2|§25.2]].

#### $\mathrm{SO}(n)$ is a smooth manifold; $\mathrm{O}(n)$ is compact · P2

$\mathrm{SO}(n)$ is open and closed in $\mathrm{O}(n)$, hence a smooth manifold of dimension $\frac{n(n-1)}{2}$; $\mathrm{O}(n)$ is compact, see Corollary [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^cor-23-2|§23.2]]. *Source: notes (filled in).*

^nd-cor-23-2

- [ ] Q1 **[state]** State the corollary.
- [ ] Q2 Why is $\det g = \pm 1$ on $\mathrm{O}(n)$, and why does this make $\mathrm{SO}(n)$ open (and closed) in $\mathrm{O}(n)$?
- [ ] Q3 Which result makes an open subset of a smooth manifold a smooth manifold of the same dimension?
- [ ] Q4 Compactness: why closed, and why bounded (columns are unit vectors)?
- [ ] Q5 **[why]** Is $\mathrm{SL}(n,\mathbb{R})$ compact? Why does the boundedness argument fail there?

> [!tip]- Hints: route of the proof in the notes
> - $\mathrm{SO}(n) = \mathrm{O}(n) \cap \det^{-1}(0,\infty)$; Proposition [[§17 Differentiable Structures#^prop-17-7|§17.7]].
> - $(g^{\mathsf T}g)_{jj} = \sum_i g_{ij}^2 = 1$, so $\|g\|^2 = n$; Heine–Borel.

# T3. Smooth structures and smooth maps

## Definitions T3

### Priority 2 · stated or done in class

#### Smoothly compatible charts · P2

$(U, \varphi)$ and $(V, \psi)$ are compatible if $\psi \circ \varphi^{-1} : \varphi(U \cap V) \to \psi(U \cap V)$ is a diffeomorphism (vacuous if $U \cap V = \emptyset$), see Definition [[§17 Differentiable Structures#^def-17-4|§17.4]]. *Source: Lecture 5.*

^nd-def-17-4

- [ ] Q1 **[def]** State $C^\infty$-compatibility of two charts, with the domain and target of the transition function.
- [ ] Q2 **[why]** Why is "smooth" alone not enough for the transition function, i.e. why must its inverse be smooth too? (Which transition is a smooth homeomorphism with non-smooth inverse?)
- [ ] Q3 **[why]** Compatibility is reflexive and symmetric. Show it is not transitive, with three charts on $\mathbb{R}$.
- [ ] Q4 **[use]** Why is compatibility the right condition: what does it guarantee about "smooth in the sense of $\varphi$" versus "of $\psi$" on $U \cap V$?

> [!tip]- Hints: where it lives, examples
> - Definition [[§17 Differentiable Structures#^def-17-4|§17.4]]; diffeomorphism of open sets Definition [[§17 Differentiable Structures#^def-17-3|§17.3]]; smooth in the sense of a chart Definition [[§17 Differentiable Structures#^def-17-2|§17.2]].
> - Q2, Q3: Proposition [[§17 Differentiable Structures#^prop-17-2|§17.2]] ($\mathrm{id}$ on $\mathbb{R}$, $\mathrm{id}$ on $(0, \infty)$, $t \mapsto t^3$ on $\mathbb{R}$; the transition $t \mapsto t^{1/3}$ is not differentiable at $0$).
> - Q4: Theorem [[§17 Differentiable Structures#^thm-17-1|§17.1]] (both directions; the remark *The Board Version* in [[§17 Differentiable Structures|§17]]).

#### Atlas · P2

A family of pairwise compatible charts whose domains cover $M$, see Definition [[§17 Differentiable Structures#^def-17-6|§17.6]]. *Source: Lecture 5.*

^nd-def-17-6

- [ ] Q1 **[def]** State the definition of a ($C^\infty$) atlas on a topological $n$-manifold.
- [ ] Q2 **[example]** Give two atlases of $S^1$ and check one transition map.
- [ ] Q3 **[why]** Why does $S^1$ need at least two charts?
- [ ] Q4 **[example]** Give the standard atlas of $\mathbb{CP}^n$ and its transition maps $\varphi_j \circ \varphi_i^{-1}$.

> [!tip]- Hints: where it lives, examples
> - Definition [[§17 Differentiable Structures#^def-17-6|§17.6]]; Example [[§17 Differentiable Structures#^ex-17-2|§17.2]] (four half-circles), Example [[§17 Differentiable Structures#^ex-17-3|§17.3]] (stereographic), Example [[§17 Differentiable Structures#^ex-17-4|§17.4]] (angle).
> - Q3: Proposition [[§17 Differentiable Structures#^prop-17-3|§17.3]]. Q4: Definition [[§18 Projective Spaces as Smooth Manifolds#^def-18-2|§18.2]], Theorem [[§18 Projective Spaces as Smooth Manifolds#^thm-18-2|§18.2]] → drilled as [[Differentiable Manifolds HW Drill#^hw2-2|HW2.2]].

#### Compatible atlases · P2

Two atlases are compatible if every chart of one is compatible with every chart of the other, equivalently their union is an atlas, see Definition [[§17 Differentiable Structures#^def-17-7|§17.7]]. *Source: Lecture 5.*

^nd-def-17-7

- [ ] Q1 **[def]** State compatibility of atlases in both forms.
- [ ] Q2 **[example]** Show the four-chart, stereographic and angle atlases of $S^1$ are pairwise compatible (one transition map each suffices to see the pattern).
- [ ] Q3 **[why]** The atlases $\{(\mathbb{R}, \mathrm{id})\}$ and $\{(\mathbb{R}, t \mapsto t^{1/3})\}$ are not compatible. Why not, and why are the two manifolds nonetheless diffeomorphic?
- [ ] Q4 **[use]** What does compatibility of atlases say about the maximal atlases they generate?

> [!tip]- Hints: where it lives, examples
> - Definition [[§17 Differentiable Structures#^def-17-7|§17.7]]; Q2: Proposition [[§24 The Circle#^prop-24-1|§24.1]].
> - Q3: Example [[§19 Smooth Functions and Smooth Maps#^ex-19-1|§19.1]], Example [[§19 Smooth Functions and Smooth Maps#^ex-19-2|§19.2]], Corollary [[§19 Smooth Functions and Smooth Maps#^cor-19-9|§19.9]] → drilled as [[Differentiable Manifolds HW Drill#^hw3-1|HW3.1]].
> - Q4: Theorem [[§17 Differentiable Structures#^thm-17-5|§17.5]] (same maximal atlas iff compatible).

#### Maximal atlas · P2

An atlas containing every chart compatible with all its charts, see Definition [[§17 Differentiable Structures#^def-17-8|§17.8]]. *Source: Lectures 5–6.*

^nd-def-17-8

- [ ] Q1 **[def]** State the definition of a maximal atlas, in both forms.
- [ ] Q2 **[use]** Given an atlas $\mathcal{A}$, what is the maximal atlas it generates? Write $\overline{\mathcal{A}}$ as a set.
- [ ] Q3 **[why]** Why is $\overline{\mathcal{A}}$ an atlas at all? Which step would be trivial if compatibility were transitive, and how is the lack of transitivity overcome?
- [ ] Q4 **[why]** Why work with maximal atlases rather than atlases: what would go wrong with "smooth map" or "smooth chart" if a smooth structure were just an atlas?
- [ ] Q5 **[example]** Is $(\mathbb{R}, t \mapsto t^3)$ in the maximal atlas of standard $\mathbb{R}$? Is $((0, \infty), t \mapsto t^3)$?

> [!tip]- Hints: where it lives, examples
> - Definition [[§17 Differentiable Structures#^def-17-8|§17.8]]; Theorem [[§17 Differentiable Structures#^thm-17-5|§17.5]] (cover; pairwise compatible by factoring $\chi \circ \psi^{-1} = (\chi \circ \varphi^{-1}) \circ (\varphi \circ \psi^{-1})$ near each point with $\varphi$ from $\mathcal{A}$; maximal; unique).
> - Q4: two atlases of the same structure would give "different" manifolds; and charts like restrictions (Lemma [[§17 Differentiable Structures#^lem-17-6|§17.6]]) must be allowed.
> - Q5: no (the transition $t \mapsto t^{1/3}$ fails at $0$), yes (Proposition [[§17 Differentiable Structures#^prop-17-2|§17.2]]).

#### Smooth manifold structure · P2

A smooth structure on a topological manifold is a maximal atlas; a smooth manifold is a pair $(M, \mathcal{A})$, see Definition [[§17 Differentiable Structures#^def-17-9|§17.9]]. *Source: Lectures 5–6.*

^nd-def-17-9

- [ ] Q1 **[def]** State the definition of a smooth structure and of a smooth manifold ("the fundamental definition").
- [ ] Q2 **[use]** Why does any atlas specify a smooth structure, and when do two atlases specify the same one?
- [ ] Q3 **[why]** Why must the underlying space already be a topological manifold (Hausdorff and second countable)? Can an atlas make the line with two origins a smooth manifold?
- [ ] Q4 **[why]** "Distinct smooth structures" versus "non-diffeomorphic smooth manifolds": give two distinct structures on $\mathbb{R}$ that are diffeomorphic, and explain why such examples are cheap.
- [ ] Q5 **[example]** Give the smooth structure on a finite-dimensional vector space and explain "one, hence every, linear chart".

> [!tip]- Hints: where it lives, examples
> - Definition [[§17 Differentiable Structures#^def-17-9|§17.9]]; Theorem [[§17 Differentiable Structures#^thm-17-5|§17.5]].
> - Q3: the line with two origins has a smooth atlas (two charts, identity transitions) but is not Hausdorff, so it is not a manifold (Example [[§2 Topological Manifolds#^ex-2-1|§2.1]]).
> - Q4: Example [[§19 Smooth Functions and Smooth Maps#^ex-19-1|§19.1]], Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-8|§19.8]], Definition [[§19 Smooth Functions and Smooth Maps#^def-19-6|§19.6]], the remark *Distinct Structures versus Non-Diffeomorphic Manifolds* in [[§19 Smooth Functions and Smooth Maps|§19]].
> - Q5: Definition [[§22 The Differential of a Map Between Vector Spaces#^def-22-4|§22.4]], Proposition [[§22 The Differential of a Map Between Vector Spaces#^prop-22-2|§22.2]].

#### Smooth chart · P2

A chart belonging to the maximal atlas, equivalently compatible with every chart of some generating atlas, see Definition [[§19 Smooth Functions and Smooth Maps#^def-19-1|§19.1]]. *Source: Lecture 5.*

^nd-def-19-1

- [ ] Q1 **[def]** State the definition, in both forms.
- [ ] Q2 **[use]** Why are restrictions of smooth charts to open subsets, and compositions $h \circ \varphi$ with a diffeomorphism $h$ of open subsets of $\mathbb{R}^n$, again smooth charts?
- [ ] Q3 **[why]** Is every chart of the topological manifold $\mathbb{R}$ a smooth chart of standard $\mathbb{R}$? Give one that is not.
- [ ] Q4 **[example]** Why is a smooth chart $\varphi : U \to \varphi(U)$ a diffeomorphism onto its image?

> [!tip]- Hints: where it lives, examples
> - Definition [[§19 Smooth Functions and Smooth Maps#^def-19-1|§19.1]]; Q2: Lemma [[§17 Differentiable Structures#^lem-17-6|§17.6]]. Q3: $t \mapsto t^{1/3}$ (Example [[§19 Smooth Functions and Smooth Maps#^ex-19-1|§19.1]]). Q4: Proposition [[§28 Derivations and the Abstract Tangent Space#^prop-28-9|§28.9]], Lemma [[§36 Submersions#^lem-36-5|§36.5]] (the converse: diffeomorphisms onto open sets are charts).

#### Smooth function on a manifold · P2

$f : M \to \mathbb{R}$ is smooth if every $p$ lies in a smooth chart $(U, \varphi)$ with $f_\varphi = f|_U \circ \varphi^{-1}$ smooth, see Definition [[§19 Smooth Functions and Smooth Maps#^def-19-2|§19.2]]. *Source: Lectures 5–7.*

^nd-def-19-2

- [ ] Q1 **[def]** State the definition; what is $f_\varphi$?
- [ ] Q2 **[class exercise, Lecture 7]** Show that if $f$ is smooth then $f_\psi$ is smooth for every smooth chart $(V, \psi)$ ("a small point in logic"). Which identity does it use?
- [ ] Q3 **[why]** Why could "smooth in some chart at $p$" fail to mean anything without compatibility? Give $f(t) = t^{1/3}$ on $\widetilde{\mathbb{R}}$ (cube-root chart): is it smooth?
- [ ] Q4 **[example]** Why are the coordinate functions $x^i$ of a chart smooth on $U$?

> [!tip]- Hints: where it lives, examples
> - Definition [[§19 Smooth Functions and Smooth Maps#^def-19-2|§19.2]]; Q2: Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-1|§19.1]] ($f_\psi = f_\varphi \circ (\varphi \circ \psi^{-1})$ near each point; the proof was left to the class).
> - Q3: the remark *The Problem This Creates* in [[§17 Differentiable Structures|§17]]; on $\widetilde{\mathbb{R}}$, $f_\psi(s) = f(s^3) = s$, smooth.
> - Q4: $(x^i)_\varphi = r^i$, Definition [[§29 Coordinate Derivations and the Basis Theorem#^def-29-1|§29.1]].

#### Smooth map · P2

$F : M \to N$ is smooth if it is continuous and every $p$ has charts $(U, \varphi) \ni p$, $(V, \psi)$ with $F(U) \subseteq V$ and $\psi \circ F \circ \varphi^{-1}$ smooth, see Definition [[§19 Smooth Functions and Smooth Maps#^def-19-3|§19.3]]. *Source: Lecture 5.*

^nd-def-19-3

- [ ] Q1 **[def]** State the definition with all its conditions.
- [ ] Q2 **[why]** Why is continuity of $F$ part of the definition? What does it buy (think of $F(U) \subseteq V$)?
- [ ] Q3 **[use]** Prove that then the coordinate representation is smooth for every pair of smooth charts with $F(U') \subseteq V'$.
- [ ] Q4 **[use]** Prove that a composite of smooth maps is smooth.
- [ ] Q5 **[example]** Why are projections and slice inclusions of a product smooth? Why is the inclusion of an open subset smooth?

> [!tip]- Hints: where it lives, examples
> - Definition [[§19 Smooth Functions and Smooth Maps#^def-19-3|§19.3]]; Q2: Lemma [[§19 Smooth Functions and Smooth Maps#^lem-19-3|§19.3]] (shrink $U$ to $U \cap F^{-1}(V)$, which needs $F$ continuous).
> - Q3: Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-2|§19.2]] (sandwich between transition maps). Q4: Lemma [[§19 Smooth Functions and Smooth Maps#^lem-19-5|§19.5]].
> - Q5: Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-11|§19.11]], Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-6|§19.6]].

#### Diffeomorphism · P2

A smooth bijection with smooth inverse, see Definition [[§19 Smooth Functions and Smooth Maps#^def-19-4|§19.4]]. *Source: Lecture 6.*

^nd-def-19-4

- [ ] Q1 **[def]** State the definition, for open subsets of $\mathbb{R}^n$ and for manifolds.
- [ ] Q2 **[why]** Give a smooth homeomorphism that is not a diffeomorphism. Which part of the definition fails?
- [ ] Q3 **[example]** Why is $h : \widetilde{\mathbb{R}} \to \mathbb{R}$, $h(t) = t^{1/3}$, a diffeomorphism, although $h$ is not differentiable as a map of standard $\mathbb{R}$?
- [ ] Q4 **[use]** Why do the two notions agree on open subsets of Euclidean space? (See the equivalence entry *Diffeomorphism* below.)
- [ ] Q5 **[use]** Which criterion detects a diffeomorphism by its differential?

> [!tip]- Hints: where it lives, examples
> - Definition [[§17 Differentiable Structures#^def-17-3|§17.3]], Definition [[§19 Smooth Functions and Smooth Maps#^def-19-4|§19.4]], Definition [[§19 Smooth Functions and Smooth Maps#^def-19-5|§19.5]].
> - Q2: $t \mapsto t^3$ on $\mathbb{R}$. Q3: Example [[§19 Smooth Functions and Smooth Maps#^ex-19-2|§19.2]], Corollary [[§19 Smooth Functions and Smooth Maps#^cor-19-9|§19.9]]. Q4: Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-4|§19.4]].
> - Q5: Corollary [[§35 Local Diffeomorphisms#^cor-35-3|§35.3]] (bijective local diffeomorphism).

#### Product manifold · P2

$M_1 \times M_2$ with the structure generated by the product charts $\varphi_1 \times \varphi_2$, see Definition [[§19 Smooth Functions and Smooth Maps#^def-19-7|§19.7]]. *Source: Lecture 11.*

^nd-def-19-7

- [ ] Q1 **[def]** Define the product charts and the product manifold; what are its coordinate functions?
- [ ] Q2 **[why]** Why are product charts pairwise compatible? Write the transition map.
- [ ] Q3 **[use]** State the tangent space of a product, and name the map giving the isomorphism.
- [ ] Q4 **[example]** Why is the torus $S^1 \times S^1$ a smooth manifold of dimension $2$, and why is $\mathrm{pr}_1 : M_1 \times M_2 \to M_1$ a submersion?

> [!tip]- Hints: where it lives, examples
> - Definition [[§19 Smooth Functions and Smooth Maps#^def-19-7|§19.7]]; Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-10|§19.10]] (transition $(\psi_1 \circ \varphi_1^{-1}) \times (\psi_2 \circ \varphi_2^{-1})$).
> - Q3: Theorem [[§31 Tangent Vectors as Velocities of Curves#^thm-31-4|§31.4]] ($\Theta(v, w) = \iota_{1\ast}v + \iota_{2\ast}w$ from $T_{p_1}M_1 \oplus T_{p_2}M_2$, with inverse $D \mapsto (\pi_{1\ast}D, \pi_{2\ast}D)$). Q4: Example [[§36 Submersions#^ex-36-2|§36.2]].

## Proofs T3

### Priority 1 · homework (directly or extended)

#### The standard atlas of $\mathbb{CP}^n$ is smooth · P1

Theorem [[§18 Projective Spaces as Smooth Manifolds#^thm-18-2|§18.2]] → drilled as [[Differentiable Manifolds HW Drill#^hw2-2-c|HW2.2(c)]] (each $\varphi_i$ is a chart, Proposition [[§18 Projective Spaces as Smooth Manifolds#^prop-18-1|§18.1]] → [[Differentiable Manifolds HW Drill#^hw2-2-b|HW2.2(b)]]).

#### Real projective space · P1

$\mathbb{RP}^n$ with $U_i = \{x_i \neq 0\}$, $\varphi_i([x]) = (x_k/x_i)_{k \neq i}$ is a compact smooth $n$-manifold, see Corollary [[§18 Projective Spaces as Smooth Manifolds#^cor-18-5|§18.5]]. *Source: notes (filled in; the real version of [[Differentiable Manifolds HW Drill#^hw2-2|HW2.2]]); used in [[Differentiable Manifolds HW Drill#^hw3-5|HW3.5]].*

^nd-cor-18-5

- [ ] Q1 **[state]** State the corollary.
- [ ] Q2 Hausdorff, second countable, compact: which group acts on $S^n$, and which results give the three properties?
- [ ] Q3 Why is $U_i$ open, and why is $\varphi_i$ well defined and a homeomorphism onto $\mathbb{R}^n$? What is its inverse?
- [ ] Q4 Compute $\varphi_i \circ \varphi_j^{-1}$ and its domain. Why is it smooth?
- [ ] Q5 **[why]** Why is the real dimension $n$ here but $2n$ for $\mathbb{CP}^n$?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S4, S2, S1 (the $\mathbb{CP}^n$ argument with $\mathbb{R}$, $\{\pm1\}$, $S^n$).
> - $\{\pm 1\}$ finite, acts by isometries: Corollary [[§13 Group Actions and Orbit Spaces#^cor-13-4|§13.4]], Theorem [[§6 Open Quotients#^thm-6-3|§6.3]].
> - Transition $(w_k/w_i)_{k \neq i}$ with $w_j := 1$, on $\{w_i \neq 0\}$: rational, nonvanishing denominator.

#### Single-chart structures on $\mathbb{R}^n$ · P1

Corollary [[§19 Smooth Functions and Smooth Maps#^cor-19-9|§19.9]] → drilled as [[Differentiable Manifolds HW Drill#^hw3-1|HW3.1]].

#### Two smooth structures on $\mathbb{R}$ · P1

The charts $\varphi = \mathrm{id}$ and $\psi = \sqrt[3]{\cdot}$ give two different smooth structures on $\mathbb{R}$, which are nevertheless diffeomorphic via $x \mapsto x^3$, see Example [[§19 Smooth Functions and Smooth Maps#^ex-19-1|§19.1]]. *Source: Lecture 5 ("not compatible, but isomorphic"), Lecture 6 ("we're going to say diffeomorphic"). The "diffeomorphic" half is [[Differentiable Manifolds HW Drill#^hw3-1|HW3.1]].*

^nd-ex-19-1

- [ ] Q1 **[state]** State precisely what the example claims, in the language of compatibility and diffeomorphism.
- [ ] Q2 Why is each one-chart atlas automatically smooth?
- [ ] Q3 Compute the two transition functions. Which is not smooth, and where?
- [ ] Q4 Show that the identity map $\mathbb{R} \to \widetilde{\mathbb{R}}$ is not smooth, and that $C^\infty(\mathbb{R}) \subsetneq C^\infty(\widetilde{\mathbb{R}})$.
- [ ] Q5 Show $\Phi(x) = x^3$ is a diffeomorphism $\mathbb{R} \to \widetilde{\mathbb{R}}$ (coordinate representations).
- [ ] Q6 **[why]** True or false: "two smooth structures on the same topological manifold that are diffeomorphic are equal." Explain with this example.

> [!tip]- Hints: route of the proof in the notes
> - Counterexample library.
> - $\psi \circ \varphi^{-1} = \sqrt[3]{x}$ (not differentiable at $0$), $\varphi \circ \psi^{-1} = y^3$.
> - $\psi \circ \Phi \circ \varphi^{-1}(t) = t$; the diffeomorphism is not the identity map.

### Priority 2 · stated or done in class

#### Compatibility means the two notions of smoothness agree · P2

Two overlapping charts are $C^\infty$-compatible iff they declare the same functions on $U \cap V$ smooth, see Theorem [[§17 Differentiable Structures#^thm-17-1|§17.1]]. *Source: notes (filled in; reconciles the phrasings of Lectures 5 and 6).*

^nd-thm-17-1

- [ ] Q1 **[def]** Define "smooth in the sense of a chart" (Definition [[§17 Differentiable Structures#^def-17-2|§17.2]]) and smooth compatibility (Definition [[§17 Differentiable Structures#^def-17-4|§17.4]]).
- [ ] Q2 **[state]** State the theorem.
- [ ] Q3 (1 ⇒ 2): if $h = f \circ \varphi$ with $f$ smooth, which $g$ gives $h = g \circ \psi$? Why is it smooth?
- [ ] Q4 (2 ⇒ 1): which test functions $h$ do you feed in to recover smoothness of $\tau = \psi \circ \varphi^{-1}$ (think of the coordinate functions of $\psi$)?
- [ ] Q5 **[why]** Why must *both* $\tau$ and $\tau^{-1}$ be smooth? Use the charts $x$ and $x^{1/3}$ on $\mathbb{R}$ (Example [[§19 Smooth Functions and Smooth Maps#^ex-19-1|§19.1]]).

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S1.
> - $g = f \circ \tau^{-1}$, $f = g \circ \tau$; chain rule.
> - For the converse, the components of $\psi$ are smooth in the sense of $\psi$, hence in the sense of $\varphi$: that says $\tau$ is smooth.

#### Every atlas lies in a unique maximal atlas · P2

For an atlas $\mathcal{A}$, the set $\overline{\mathcal{A}}$ of all charts compatible with every chart of $\mathcal{A}$ is the unique maximal atlas containing $\mathcal{A}$; two atlases are compatible iff they lie in the same maximal atlas, see Theorem [[§17 Differentiable Structures#^thm-17-5|§17.5]]. *Source: Lecture 5 (uniqueness), Lecture 6 (sketch), completed in the notes.*

^nd-thm-17-5

- [ ] Q1 **[def]** Define atlas, compatible atlases, maximal atlas, smooth structure (Definition [[§17 Differentiable Structures#^def-17-6|§17.6]], Definition [[§17 Differentiable Structures#^def-17-7|§17.7]], Definition [[§17 Differentiable Structures#^def-17-8|§17.8]], Definition [[§17 Differentiable Structures#^def-17-9|§17.9]]).
- [ ] Q2 **[state]** State the theorem.
- [ ] Q3 Why do the domains of $\overline{\mathcal{A}}$ cover $M$?
- [ ] Q4 The key claim: two charts $(V,\psi)$, $(W,\chi) \in \overline{\mathcal{A}}$ are compatible with each other. Near $\psi(p)$, through which chart of $\mathcal{A}$ do you factor $\chi \circ \psi^{-1}$, and why is the factorization smooth?
- [ ] Q5 Maximality, then uniqueness: if $\mathcal{M} \supseteq \mathcal{A}$ is maximal, show $\mathcal{M} \subseteq \overline{\mathcal{A}}$ and conclude.
- [ ] Q6 **[why]** Why is "smooth" a local property needed in Q4? Why is a smooth structure defined as a maximal atlas and not just an atlas?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S1 (factor through a chart of $\mathcal{A}$).
> - On $\psi(U \cap V \cap W)$: $\chi \circ \psi^{-1} = (\chi \circ \varphi^{-1}) \circ (\varphi \circ \psi^{-1})$, with $(U,\varphi) \in \mathcal{A}$ at $p$.
> - Uniqueness: every chart of $\mathcal{M}$ is compatible with $\mathcal{A}$, so $\mathcal{M} \subseteq \overline{\mathcal{A}}$; maximality of $\mathcal{M}$ gives equality.

#### The circle needs more than one chart · P2

$S^1$ has no one-chart atlas, see Proposition [[§17 Differentiable Structures#^prop-17-3|§17.3]]. *Source: Lecture 5 (the reason given); filled in.*

^nd-prop-17-3

- [ ] Q1 **[state]** State the proposition.
- [ ] Q2 If $\varphi : S^1 \to \varphi(S^1) \subseteq \mathbb{R}$ were a chart, why would $\varphi(S^1)$ be open and compact?
- [ ] Q3 Why is it then closed, and what does connectedness of $\mathbb{R}$ force?
- [ ] Q4 **[why]** Generalize: which compact manifolds admit a one-chart atlas?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S13 (compactness), connectedness.
> - Nonempty clopen in $\mathbb{R}$ ⇒ all of $\mathbb{R}$, not compact.

#### Some chart suffices: smoothness of a function · P2

If $f : M \to \mathbb{R}$ is smooth (smooth in *some* chart around each point), then $f \circ \psi^{-1}$ is smooth for *every* smooth chart $(V, \psi)$, see Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-1|§19.1]]. *Source: Lecture 7 ("another exercise: show that if $f$ is smooth … for any smooth chart"; "a small point in logic"); filled in.* **[class exercise, Lecture 7]**

^nd-prop-19-1

- [ ] Q1 **[def]** Define a smooth function on a manifold (Definition [[§19 Smooth Functions and Smooth Maps#^def-19-2|§19.2]]). Where is "there exists" in it?
- [ ] Q2 **[state]** State the proposition: the upgrade from "some" to "every".
- [ ] Q3 Fix $(V,\psi)$ and $q \in V$. Which chart $(U,\varphi)$ do you bring in, and on which open set do you work?
- [ ] Q4 Write $f_\psi$ as a composite of $f_\varphi$ and a transition function. Why is each factor smooth?
- [ ] Q5 **[why]** Why is it enough to prove smoothness near each point? What would go wrong with a chart not in the maximal atlas?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S1.
> - On $\psi(U \cap V)$: $f \circ \psi^{-1} = (f \circ \varphi^{-1}) \circ (\varphi \circ \psi^{-1})$.
> - Both charts are in the maximal atlas, hence compatible.

#### Composition of smooth maps · P2

If $F : M \to N$ and $G : N \to P$ are smooth, so is $G \circ F$, see Lemma [[§19 Smooth Functions and Smooth Maps#^lem-19-5|§19.5]]. *Source: Lecture 7 ("something I would trust ChatGPT to prove"); filled in.*

^nd-lem-19-5

- [ ] Q1 **[state]** State the lemma; what has to be produced at each $p$?
- [ ] Q2 Step 1: which charts for $G$ at $F(p)$ do you choose first, and why first?
- [ ] Q3 Step 2: given charts $(U_0, \varphi)$, $(V_0, \psi_0)$ for $F$ at $p$, how do you shrink $U_0$ so that $F$ lands in the $V$ of Step 1? Why is $\psi \circ F \circ \varphi^{-1}$ smooth on $\varphi(U)$?
- [ ] Q4 Step 3: write the coordinate representation of $G \circ F$ and conclude.
- [ ] Q5 **[why]** What goes wrong if you choose the charts for $F$ first? Which lemma handles the shrinking (Lemma [[§19 Smooth Functions and Smooth Maps#^lem-19-3|§19.3]])?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S1; order of choices matters.
> - $U = U_0 \cap F^{-1}(V)$; $\psi \circ F \circ \varphi^{-1} = (\psi \circ \psi_0^{-1}) \circ (\psi_0 \circ F \circ \varphi^{-1})$.
> - $\chi \circ (G \circ F) \circ \varphi^{-1} = (\chi \circ G \circ \psi^{-1}) \circ (\psi \circ F \circ \varphi^{-1})$.

#### The product smooth structure; projections and slices are smooth · P2

Product charts $(U_1 \times U_2, \varphi_1 \times \varphi_2)$ form a smooth atlas on $M_1 \times M_2$, of dimension $m_1 + m_2$ (Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-10|§19.10]]); projections and slice inclusions are smooth (Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-11|§19.11]]). *Source: Lecture 11.*

^nd-prop-19-10

- [ ] Q1 **[def]** Define the product manifold and the slice inclusions (Definition [[§19 Smooth Functions and Smooth Maps#^def-19-7|§19.7]], Definition [[§19 Smooth Functions and Smooth Maps#^def-19-8|§19.8]]).
- [ ] Q2 **[state]** State both propositions.
- [ ] Q3 Why is $M_1 \times M_2$ Hausdorff and second countable, and why are product charts charts?
- [ ] Q4 Compute the transition function of two product charts. Why is it smooth?
- [ ] Q5 Compute the coordinate representations of $\pi_1$ and of $\iota^{p_2}$ in product charts.
- [ ] Q6 **[why]** Where is this used: the tangent space of a product (Theorem [[§31 Tangent Vectors as Velocities of Curves#^thm-31-4|§31.4]]) and the 2025 graph–diagonal problem.

> [!tip]- Hints: route of the proof in the notes
> - Theorem [[§3 Subspaces and Products#^thm-3-12|§3.12]]; $\varphi_1 \times \varphi_2$ continuous with continuous inverse by the universal property of the product.
> - Transition $= (\varphi_1' \circ \varphi_1^{-1}) \times (\varphi_2' \circ \varphi_2^{-1})$.
> - $(r,s) \mapsto r$; $r \mapsto (r, \varphi_2(p_2))$.

#### The three circle atlases define one smooth structure · P2

The four-chart (projection) atlas, the angle atlas and the stereographic atlas on $S^1$ are pairwise compatible and generate the structure of $S^1 = F^{-1}(1)$, $F = x^2 + y^2$, see Proposition [[§24 The Circle#^prop-24-1|§24.1]]. *Source: notes.*

^nd-prop-24-1

- [ ] Q1 **[state]** State the proposition.
- [ ] Q2 Why are the graph charts of Proposition [[§20 Manifolds in Euclidean Space#^prop-20-2|§20.2]] for $S^1$ exactly the four projection charts?
- [ ] Q3 For each angle or stereographic chart $\chi$, show (a) $\chi^{-1}$ is smooth into $\mathbb{R}^2$ and (b) $\chi$ extends to a smooth $\hat\chi$ on an open set of $\mathbb{R}^2$. Give $\hat\chi$ for $\sigma_N$.
- [ ] Q4 Why do (a) and (b) give compatibility with every graph chart (transition $= \hat\chi \circ \varphi^{-1}$ or $\varphi \circ \chi^{-1} = \pi \circ \chi^{-1}$)?
- [ ] Q5 How does uniqueness of the maximal atlas finish?
- [ ] Q6 **[why]** Why does the angle chart need a branch of the argument on the plane minus a ray, and why cannot one angle chart cover $S^1$?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S1; compare everything with one reference atlas.
> - $\sigma_N = x/(1-y)$ on $\{y < 1\}$; $\sigma_N^{-1}(u) = (2u, u^2 - 1)/(u^2 + 1)$.
> - Transitions: $\pi_I \circ \chi^{-1}$ (linear after smooth) and $\hat\chi \circ \varphi^{-1}$.
> - Theorem [[§17 Differentiable Structures#^thm-17-5|§17.5]]: each atlas lies in $\overline{\mathcal{A}}$.

### Priority 3 · filled in, using a technique the homework drills

#### Restricting and recomposing smooth charts; open subsets are smooth manifolds · P3

A smooth chart restricted to an open subset, or composed with a diffeomorphism of Euclidean open sets, is again a chart of the smooth structure (Lemma [[§17 Differentiable Structures#^lem-17-6|§17.6]]); an open subset $S$ of a smooth manifold is a smooth manifold whose charts are the charts of $M$ inside $S$ (Proposition [[§17 Differentiable Structures#^prop-17-7|§17.7]]). *Source: notes (filled in).*

^nd-lem-17-6

- [ ] Q1 **[state]** State the lemma (both parts) and the proposition.
- [ ] Q2 For the lemma, what must be checked for the new pair to lie in the maximal atlas?
- [ ] Q3 (1): write the transition functions of $(U', \varphi|_{U'})$ with $(V, \chi)$ as restrictions. (2): write them for $(U, h \circ \varphi)$.
- [ ] Q4 For the proposition: why do the restricted charts form an atlas on $S$?
- [ ] Q5 **[why]** Why does (2) require $h$ to be a diffeomorphism and not just a homeomorphism?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S1; membership by maximality.
> - (2): $\chi \circ (h \circ \varphi)^{-1} = (\chi \circ \varphi^{-1}) \circ h^{-1}$ and $h \circ (\varphi \circ \chi^{-1})$.
> - Proposition: transition of restrictions $=$ restriction of the transition.

#### Smoothness of a map does not depend on the charts · P3

If $F : M \to N$ is smooth, then $\psi' \circ F \circ \varphi'^{-1}$ is smooth for every pair of smooth charts with $F(U') \subseteq V'$, see Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-2|§19.2]]. *Source: notes (filled in).*

^nd-prop-19-2

- [ ] Q1 **[def]** Define a smooth map between manifolds (Definition [[§19 Smooth Functions and Smooth Maps#^def-19-3|§19.3]]).
- [ ] Q2 **[state]** State the proposition.
- [ ] Q3 Fix $a \in \varphi'(U')$, $p = \varphi'^{-1}(a)$. Which charts $(U,\varphi)$, $(V,\psi)$ does the definition give, and on which open set around $a$ do you work?
- [ ] Q4 Write $\psi' \circ F \circ \varphi'^{-1}$ there as a composite of three maps. Which are transition functions?
- [ ] Q5 **[why]** Why is continuity of $F$ part of the definition? (Without it, $F^{-1}(V)$ need not be open and the charts cannot be shrunk; see Lemma [[§19 Smooth Functions and Smooth Maps#^lem-19-3|§19.3]].)

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S1.
> - $\psi' \circ F \circ \varphi'^{-1} = (\psi' \circ \psi^{-1}) \circ (\psi \circ F \circ \varphi^{-1}) \circ (\varphi \circ \varphi'^{-1})$ on $\varphi'(U \cap U')$.

### Priority 4 · notes only (optional before the midterm)

#### Compatibility is not an equivalence relation · P4

$C^\infty$-compatibility is reflexive and symmetric but not transitive, see Proposition [[§17 Differentiable Structures#^prop-17-2|§17.2]]. *Source: notes (filled in).*

^nd-prop-17-2

- [ ] Q1 **[state]** State the proposition.
- [ ] Q2 Reflexive and symmetric: which transition functions appear?
- [ ] Q3 Not transitive: give three charts on $\mathbb{R}$ (on $\mathbb{R}$, on $(0,\infty)$, the cube) with $1 \sim 2$, $2 \sim 3$, $1 \not\sim 3$. Check each pair.
- [ ] Q4 **[why]** Why does this make the proof of Theorem [[§17 Differentiable Structures#^thm-17-5|§17.5]] non-trivial (which step would otherwise be formal)?

> [!tip]- Hints: route of the proof in the notes
> - Overlaps with $(0,\infty)$ avoid $0$, where $t^{1/3}$ is not smooth.
> - The middle chart's domain misses the bad point, so it is compatible with both.

#### A chart mapped into a given chart · P4

For continuous $F : M \to N$, $p \in M$: every chart $(U_0,\varphi_0)$ at $p$ can be shrunk to $U = U_0 \cap F^{-1}(V)$ with $F(U) \subseteq V$ for a given chart $(V,\psi)$ at $F(p)$; charts can be chosen inside any neighbourhood; and if $F$ is smooth the coordinate representation is smooth, see Lemma [[§19 Smooth Functions and Smooth Maps#^lem-19-3|§19.3]]. *Source: notes (filled in).*

^nd-lem-19-3

- [ ] Q1 **[state]** State the three parts.
- [ ] Q2 (1): why is $U$ open, why is $(U, \varphi_0|_U)$ a smooth chart, and why is $F(U) \subseteq V$?
- [ ] Q3 (2): how do you also get $U \subseteq W$?
- [ ] Q4 (3): which proposition gives smoothness of the coordinate representation?
- [ ] Q5 **[why]** Where is continuity of $F$ used, and why is this lemma used "tacitly" in almost every proof about smooth maps?

> [!tip]- Hints: route of the proof in the notes
> - $F^{-1}(V)$ open by continuity; Lemma [[§17 Differentiable Structures#^lem-17-6|§17.6]](1); then Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-2|§19.2]].

#### The two notions of diffeomorphism agree · P4

For open $A \subseteq \mathbb{R}^m$, $B \subseteq \mathbb{R}^n$ with their standard structures, $F : A \to B$ is smooth as a map of manifolds iff it is smooth in the Euclidean sense; so the two notions of diffeomorphism agree, see Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-4|§19.4]]. *Source: notes (filled in).*

^nd-prop-19-4

- [ ] Q1 **[state]** State the proposition.
- [ ] Q2 Euclidean-smooth ⇒ smooth: which charts, and what is the coordinate representation?
- [ ] Q3 Smooth ⇒ Euclidean-smooth: given charts $(U,\varphi)$, $(V,\psi)$ of the standard structures with $\psi \circ F \circ \varphi^{-1}$ smooth, why are $\varphi$ and $\psi^{-1}$ smooth in the Euclidean sense?
- [ ] Q4 Write $F|_U = \psi^{-1} \circ (\psi \circ F \circ \varphi^{-1}) \circ \varphi$ and conclude.
- [ ] Q5 **[why]** On $\widetilde{\mathbb{R}}$ (the cube-root structure, Example [[§19 Smooth Functions and Smooth Maps#^ex-19-2|§19.2]]) the identity is not smooth: which hypothesis of the proposition fails?

> [!tip]- Hints: route of the proof in the notes
> - Charts of the standard structure are compatible with the identity charts, so they are Euclidean diffeomorphisms onto their images.

#### Inclusions of, and maps into, open subsets · P4

For $S \subseteq M$ open: the inclusion $\iota$ is smooth, restrictions of smooth maps are smooth, and $G : P \to S$ is smooth iff $\iota \circ G$ is, see Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-6|§19.6]]. *Source: notes (filled in).*

^nd-prop-19-6

- [ ] Q1 **[state]** State the three parts.
- [ ] Q2 (1): which chart do you use at $p \in S$ on both sides, and what is the coordinate representation of $\iota$?
- [ ] Q3 (3), ⇐: why is $G$ continuous *into $S$*, and why is its coordinate representation in a chart inside $S$ the same as that of $\iota \circ G$?
- [ ] Q4 **[why]** Part (3) fails for a non-open subset with the "wrong" topology (a figure eight in $\mathbb{R}^2$): which step uses openness?

> [!tip]- Hints: route of the proof in the notes
> - Charts of $S$ are the charts of $M$ with domain in $S$ (Proposition [[§17 Differentiable Structures#^prop-17-7|§17.7]]); $\varphi \circ \iota \circ \varphi^{-1} = \mathrm{id}$.
> - Open in $S$ ⇒ open in $M$ (Lemma [[§3 Subspaces and Products#^lem-3-2|§3.2]]).

#### Diffeomorphic is an equivalence relation; transport of structure · P4

Being diffeomorphic is an equivalence relation, and diffeomorphic manifolds are homeomorphic (Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-7|§19.7]]); a homeomorphism $h : X \to N$ onto a smooth manifold transports a unique smooth structure making $h$ a diffeomorphism (Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-8|§19.8]]). *Source: notes (filled in).*

^nd-prop-19-8

- [ ] Q1 **[state]** State both propositions.
- [ ] Q2 Transitivity of "diffeomorphic": which lemma, and what is the inverse of $G \circ F$?
- [ ] Q3 Transport: what is the atlas $\mathcal{A}_h$, and why are its transition functions smooth?
- [ ] Q4 Why is $h$ a diffeomorphism for this structure (coordinate representation)?
- [ ] Q5 Uniqueness: if $h$ is a diffeomorphism for some structure $\mathcal{S}$ on $X$, show every chart $(W,\chi)$ of $\mathcal{S}$ is compatible with every $\psi \circ h$ (read both transition functions as coordinate representations of $h$ and $h^{-1}$). Why does maximality then give $\mathcal{S} = \overline{\mathcal{A}_h}$?
- [ ] Q6 **[why]** Use this to explain why $\widetilde{\mathbb{R}}$ and $\mathbb{R}$ are diffeomorphic but their structures differ.

> [!tip]- Hints: route of the proof in the notes
> - Lemma [[§19 Smooth Functions and Smooth Maps#^lem-19-5|§19.5]]; inverse $F^{-1} \circ G^{-1}$.
> - $(\psi' \circ h) \circ (\psi \circ h)^{-1} = \psi' \circ \psi^{-1}$.
> - In charts $(h^{-1}(V), \psi \circ h)$ and $(V, \psi)$ the representation of $h$ is the identity.

# T4. Tangent spaces

## Definitions T4

### Priority 1 · homework (directly or extended)

#### Velocity of a curve · P1

$D_\gamma = \gamma_{\ast 0}(\frac{d}{dt}|_0)$, so $D_\gamma[f] = \frac{d}{dt}\big|_{t=0} f(\gamma(t))$, see Definition [[§31 Tangent Vectors as Velocities of Curves#^def-31-2|§31.2]]. *Source: Lecture 11; Assignment 3.*

^nd-def-31-2

- [ ] Q1 **[def]** Define a smooth curve and its velocity $D_\gamma \in T_{\gamma(0)}M$, in both forms.
- [ ] Q2 **[use]** Express $D_\gamma$ in a chart; what does it depend on?
- [ ] Q3 **[use]** Show $F_{\ast p}(D_\gamma) = D_{F \circ \gamma}$, and explain how this computes differentials.
- [ ] Q4 **[why]** Two different curves can have the same velocity. When exactly do $\gamma_1$, $\gamma_2$ through $p$ give the same tangent vector?
- [ ] Q5 **[use]** Is every tangent vector a velocity? → drilled as [[Differentiable Manifolds HW Drill#^hw3-2|HW3.2]].

> [!tip]- Hints: where it lives, examples
> - Definition [[§31 Tangent Vectors as Velocities of Curves#^def-31-1|§31.1]], Definition [[§31 Tangent Vectors as Velocities of Curves#^def-31-2|§31.2]]; Q2, Q4: Proposition [[§31 Tangent Vectors as Velocities of Curves#^prop-31-1|§31.1]] (same velocity iff the coordinate curves have the same derivative at $0$).
> - Q3: Corollary [[§31 Tangent Vectors as Velocities of Curves#^cor-31-3|§31.3]] (chain rule). Q5: Theorem [[§31 Tangent Vectors as Velocities of Curves#^thm-31-2|§31.2]].

### Priority 2 · stated or done in class

#### Geometric tangent space · P2

$T^{\mathrm{geo}}_pM$ is the set of velocities $\gamma'(0)$ of smooth curves $\gamma : (-\varepsilon, \varepsilon) \to \mathbb{R}^{n+k}$ with values in $M$ and $\gamma(0) = p$, see Definition [[§25 The Geometric Tangent Space#^def-25-1|§25.1]]. *Source: Lectures 7–8.*

^nd-def-25-1

- [ ] Q1 **[def]** State the definition, including where $\gamma$ takes values and in which space $\gamma'(0)$ lives.
- [ ] Q2 **[class exercise, Lecture 8]** For the graph $M$ of a smooth $G : A \to \mathbb{R}^k$, show $T^{\mathrm{geo}}_pM = \{(u, G'(x_0)u)\}$ ("not a trivial exercise"). Which inclusion needs a curve to be built?
- [ ] Q3 **[example]** Compute $T^{\mathrm{geo}}_I \mathrm{O}(n)$ from a curve of orthogonal matrices.
- [ ] Q4 **[why]** Why is it not obvious from the definition that $T^{\mathrm{geo}}_pM$ is a vector space? What has to be proved, and how?
- [ ] Q5 **[why]** Why can this definition not be used for an abstract manifold such as $\mathbb{CP}^n$?

> [!tip]- Hints: where it lives, examples
> - Definition [[§25 The Geometric Tangent Space#^def-25-1|§25.1]]; Q2: Lemma [[§25 The Geometric Tangent Space#^lem-25-2|§25.2]] ($\supseteq$: the lifted line $t \mapsto (x_0 + tu, G(x_0 + tu))$).
> - Q3: Example [[§25 The Geometric Tangent Space#^ex-25-2|§25.2]]. Q4: Theorem [[§25 The Geometric Tangent Space#^thm-25-3|§25.3]] (it equals $\ker F'(p)$), Lemma [[§25 The Geometric Tangent Space#^lem-25-1|§25.1]].
> - Q5: there is no ambient $\mathbb{R}^{n+k}$; hence derivations, Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-2|§28.2]]. Equivalence: the entry *Tangent space* below.

#### Germ · P2

A germ at $p$ is a class of pairs $(f, U)$, $f$ smooth on an open $U \ni p$, two pairs being equivalent if they agree on some open $W \ni p$, see Definition [[§27 Germs#^def-27-2|§27.2]]. *Source: Lecture 8.*

^nd-def-27-2

- [ ] Q1 **[def]** State the relation "agree near $p$" and the definition of a germ and of $C^\infty_p(M)$.
- [ ] Q2 **[why]** Prove the relation is transitive. Why does the argument break for infinitely many representatives at once?
- [ ] Q3 **[use]** Define sum, product and evaluation of germs; why are they well defined?
- [ ] Q4 **[why]** Is a germ determined by its Taylor series at $p$? Give a nonzero germ with zero Taylor series.
- [ ] Q5 **[use]** Why does every germ have a representative defined on all of $M$?

> [!tip]- Hints: where it lives, examples
> - Definition [[§27 Germs#^def-27-1|§27.1]], Definition [[§27 Germs#^def-27-2|§27.2]], Definition [[§27 Germs#^def-27-3|§27.3]]; Proposition [[§27 Germs#^prop-27-1|§27.1]], Proposition [[§27 Germs#^prop-27-2|§27.2]].
> - Q2: intersect the two sets $W$; Example [[§27 Germs#^ex-27-1|§27.1]]. Q4: Example [[§27 Germs#^ex-27-2|§27.2]], Definition [[§27 Germs#^def-27-4|§27.4]] ($e^{-1/s}$).
> - Q5: Corollary [[§53 Vector Fields#^cor-53-5|§53.5]] (bump function).

#### Derivation at a point · P2

An $\mathbb{R}$-linear $D : C^\infty_p(M) \to \mathbb{R}$ with $D([f][g]) = f(p)D[g] + g(p)D[f]$, see Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-1|§28.1]]. *Source: Lecture 9.*

^nd-def-28-1

- [ ] Q1 **[def]** State the definition of a derivation at $p$ (domain, target, both conditions).
- [ ] Q2 **[class exercise, Lecture 9]** Prove that $D$ kills constant germs, and that $D[f] = D[f - f(p)]$.
- [ ] Q3 **[why]** Drop the Leibniz rule: give a linear map $C^\infty_p(M) \to \mathbb{R}$ that is not a derivation. Which property of Q2 fails?
- [ ] Q4 **[use]** Show $D$ vanishes on $I_p^2$. → drilled as [[Differentiable Manifolds HW Drill#^hw3-3|HW3.3]].
- [ ] Q5 **[example]** Why is $[f] \mapsto \frac{d}{dt}\big|_{t=0} f(\gamma(t))$ a derivation at $\gamma(0)$?

> [!tip]- Hints: where it lives, examples
> - Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-1|§28.1]]; Q2, Q4: Lemma [[§28 Derivations and the Abstract Tangent Space#^lem-28-2|§28.2]] ($D[1] = D[1 \cdot 1] = 2D[1]$; Uribe set (a) and (b) as an exercise, (b) is part of Assignment 3).
> - Q3: evaluation $[f] \mapsto f(p)$ is linear but sends $[1]$ to $1$. Q5: Proposition [[§31 Tangent Vectors as Velocities of Curves#^prop-31-1|§31.1]].

#### Abstract tangent space · P2

$T_pM$, the vector space of all derivations at $p$, see Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-2|§28.2]]. *Source: Lecture 9.*

^nd-def-28-2

- [ ] Q1 **[def]** Define $T_pM$ and its vector space operations. What kind of object is a tangent vector here?
- [ ] Q2 **[why]** Why derivations of germs rather than of $C^\infty(M)$? What would one have to prove to use global functions?
- [ ] Q3 **[use]** Why may one identify $T_pU = T_pM$ for open $U \ni p$?
- [ ] Q4 **[why]** What is $\dim T_pM$, and what fails in the basis theorem if the functions in Hadamard's lemma were not smooth?
- [ ] Q5 **[example]** For $M \subseteq \mathbb{R}^{n+k}$ a regular level set, how does a geometric tangent vector $v$ give a derivation?

> [!tip]- Hints: where it lives, examples
> - Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-2|§28.2]]; the remark *Two Faces of a Tangent Vector* in [[§28 Derivations and the Abstract Tangent Space|§28]].
> - Q2: Proposition [[§28 Derivations and the Abstract Tangent Space#^prop-28-3|§28.3]] (needs bump functions, Corollary [[§53 Vector Fields#^cor-53-5|§53.5]]). Q3: Lemma [[§28 Derivations and the Abstract Tangent Space#^lem-28-8|§28.8]].
> - Q4: Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]], Lemma [[§29 Coordinate Derivations and the Basis Theorem#^lem-29-3|§29.3]] (Uribe: smoothness of the $g_i$ is "a key point": one applies $D$ to them).
> - Q5: $D_v$, Definition [[§25 The Geometric Tangent Space#^def-25-4|§25.4]], Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-7|§29.7]].

#### Pullback of germs · P2

$F^\ast_p : C^\infty_{F(p)}(N) \to C^\infty_p(M)$, $F^\ast_p[g] = [g \circ F]$, see Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-5|§28.5]]. *Source: Lecture 9.*

^nd-def-28-5

- [ ] Q1 **[def]** State the definition, with the representative $(g \circ F, F^{-1}(V))$; why is $F^{-1}(V)$ open and $g \circ F$ smooth?
- [ ] Q2 **[why]** Why is $F^\ast_p$ well defined on germs?
- [ ] Q3 **[use]** Show $F^\ast_p$ is an algebra homomorphism with $(F^\ast_p[g])(p) = g(F(p))$, so $F^\ast_p(I_{F(p)}) \subseteq I_p$.
- [ ] Q4 **[use]** How do pullbacks compose: $(G \circ F)^\ast_p = ?$ Why is the order reversed?

> [!tip]- Hints: where it lives, examples
> - Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-5|§28.5]]; Proposition [[§28 Derivations and the Abstract Tangent Space#^prop-28-4|§28.4]].
> - Q4: the proof of Theorem [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]] ("one line": associativity of composition).

#### Pushforward (differential) $F_{\ast,p}$ · P2

$(F_{\ast p}D)[g] = D[g \circ F]$: pull the germ back, then apply $D$, see Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-6|§28.6]]. *Source: Lectures 9–10.*

^nd-def-28-6

- [ ] Q1 **[def]** State the definition of the pushforward of a derivation $D \in T_pM$ along $F$: what does $F_{\ast p}D$ eat, and what does it return?
- [ ] Q2 **[use]** Prove $F_{\ast p}D$ is a derivation at $F(p)$ and $F_{\ast p}$ is linear.
- [ ] Q3 **[class exercise, Lecture 10]** From $(G \circ F)^\ast_p = F^\ast_p \circ G^\ast_{F(p)}$, conclude the chain rule $(G \circ F)_{\ast p} = G_{\ast F(p)} \circ F_{\ast p}$ ("use this to conclude the proof").
- [ ] Q4 **[why]** Why is $F_{\ast p}D$ a derivation at $F(p)$ and not at some other point? Where is $(F^\ast_p[g])(p) = g(F(p))$ used?
- [ ] Q5 **[example]** Compute $F_{\ast p}(\partial/\partial x^i|_p)$ in charts. Compute $\Phi_{\ast p}$ for a diffeomorphism and $\kappa_{\ast p}$ for a constant map.

> [!tip]- Hints: where it lives, examples
> - Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-6|§28.6]]; Q2: Proposition [[§28 Derivations and the Abstract Tangent Space#^prop-28-5|§28.5]]; Q3: Theorem [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]] (dualize: $D \circ F^\ast_p \circ G^\ast_{F(p)}$).
> - Q4: the Leibniz rule for $F_{\ast p}D$ produces $g(F(p))$.
> - Q5: Theorem [[§30 The Differential in Coordinates#^thm-30-2|§30.2]] (the Jacobian of $\psi \circ F \circ \varphi^{-1}$), Corollary [[§28 Derivations and the Abstract Tangent Space#^cor-28-7|§28.7]], Lemma [[§28 Derivations and the Abstract Tangent Space#^lem-28-10|§28.10]]. By curves: Corollary [[§31 Tangent Vectors as Velocities of Curves#^cor-31-3|§31.3]].

#### Coordinate functions of a chart · P2

$x^i = r^i \circ \varphi$, so $\varphi = (x^1, \ldots, x^n)$, see Definition [[§29 Coordinate Derivations and the Basis Theorem#^def-29-1|§29.1]]. *Source: Lecture 8.*

^nd-def-29-1

- [ ] Q1 **[def]** Define the standard coordinates $r^i$ on $\mathbb{R}^n$, the coordinate functions $x^i$ of a chart, and the coordinate representation $f_\varphi$.
- [ ] Q2 **[why]** Why does Uribe insist on $r^i$ for $\mathbb{R}^n$ and $x^i$ for $M$? What is $(x^i)_\varphi$?
- [ ] Q3 **[example]** For the polar chart on the slit plane, write $x$, $y$ as functions of the coordinate functions $r$, $\theta$.

> [!tip]- Hints: where it lives, examples
> - Definition [[§29 Coordinate Derivations and the Basis Theorem#^def-29-1|§29.1]]; $(x^i)_\varphi = r^i$ on $\varphi(U)$. Q3: Example [[§30 The Differential in Coordinates#^ex-30-1|§30.1]].

#### Coordinate derivation $\partial/\partial x^j|_p$ · P2

$\frac{\partial}{\partial x^j}\big|_p[f] = \frac{\partial f_\varphi}{\partial r^j}(\varphi(p))$, see Definition [[§29 Coordinate Derivations and the Basis Theorem#^def-29-2|§29.2]]. *Source: Lecture 8.*

^nd-def-29-2

- [ ] Q1 **[def]** State the definition of $\partial/\partial x^j|_p$ for a smooth chart $(U, \varphi = (x^1, \ldots, x^n))$ at $p$: on what does it act, which function is differentiated, at which point, in which variable.
- [ ] Q2 **[use]** Prove it is well defined on germs and is a derivation at $p$.
- [ ] Q3 **[why]** Does $\partial/\partial x^1|_p$ depend only on the function $x^1$, or on the whole chart? Compare the charts $(x, y)$ and $(x, y + x)$ on $\mathbb{R}^2$.
- [ ] Q4 **[use]** Compute $\partial/\partial x^i|_p[x^j]$, and state how the $\partial/\partial x^i|_p$ change under a change of chart.
- [ ] Q5 **[example]** Express $\partial/\partial r$ and $\partial/\partial \theta$ in terms of $\partial/\partial x$, $\partial/\partial y$.

> [!tip]- Hints: where it lives, examples
> - Definition [[§29 Coordinate Derivations and the Basis Theorem#^def-29-2|§29.2]] ("defined by going downstairs"); Q2: Proposition [[§29 Coordinate Derivations and the Basis Theorem#^prop-29-2|§29.2]].
> - Q3: by Corollary [[§30 The Differential in Coordinates#^cor-30-4|§30.4]], with $\tilde x = x$, $\tilde y = y + x$: $\partial/\partial \tilde x = \partial/\partial x - \partial/\partial y$ (not in the notes; a standard check).
> - Q4: $\delta^j_i$, Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]] (Step 4), Corollary [[§30 The Differential in Coordinates#^cor-30-4|§30.4]]. Q5: Example [[§30 The Differential in Coordinates#^ex-30-1|§30.1]].

## Proofs T4

### Priority 1 · homework (directly or extended)

#### $I_p$, $I_p^2$ and the first properties of derivations · P1

$I_p$ is an ideal and $I_p^2 \subseteq I_p$ (Lemma [[§28 Derivations and the Abstract Tangent Space#^lem-28-1|§28.1]]); a derivation at $p$ kills constants, so $D[f] = D[f - f(p)]$, and kills $I_p^2$ (Lemma [[§28 Derivations and the Abstract Tangent Space#^lem-28-2|§28.2]]). *Source: Lecture 9 ("exercise: for any derivation $D$ of a constant is zero … part B of the exercise is homework"); part (2) is also in [[Differentiable Manifolds HW Drill#^hw3-3-a|HW3.3(a)]].* **[class exercise, Lecture 9]**

^nd-lem-28-2

- [ ] Q1 **[def]** Define a derivation at $p$, $T_pM$, $I_p$ and $I_p^2$ (Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-1|§28.1]], Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-2|§28.2]], Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-3|§28.3]], Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-4|§28.4]]).
- [ ] Q2 **[state]** State the lemma, both parts and their consequences.
- [ ] Q3 Prove $D[\underline 1] = 0$ from the Leibniz rule; extend to all constants.
- [ ] Q4 Deduce that $D$ is determined by its values on $I_p$.
- [ ] Q5 Prove $D([f][g]) = 0$ for $[f], [g] \in I_p$, and extend to $I_p^2$.
- [ ] Q6 **[why]** Why does this, combined with Taylor–Hadamard, mean a derivation "only sees first derivatives"? Which later theorem makes this precise?

> [!tip]- Hints: route of the proof in the notes
> - $D[\underline 1] = D([\underline 1][\underline 1]) = 2D[\underline 1]$.
> - $[f] = [f - \underline{f(p)}] + [\underline{f(p)}]$.
> - Leibniz with $f(p) = g(p) = 0$; linearity for finite sums.
> - Used in Corollary [[§29 Coordinate Derivations and the Basis Theorem#^cor-29-5|§29.5]] and Theorem [[§34 The Cotangent Space from Germs#^thm-34-4|§34.4]].

#### Regular level sets of maps between manifolds are topological manifolds · P1

If $F : M^m \to N^n$ is smooth and $c$ a regular value, $F^{-1}(c)$ is a topological manifold of dimension $m - n$ (Corollary [[§30 The Differential in Coordinates#^cor-30-9|§30.9]]); when $F^{-1}(c)$ lies in one chart, $c$ is regular for $F$ iff $\psi(c)$ is regular for $\tilde F$ (Proposition [[§30 The Differential in Coordinates#^prop-30-8|§30.8]]). *Source: notes (used in [[Differentiable Manifolds HW Drill#^hw3-4|HW3.4]]).*

^nd-cor-30-9

- [ ] Q1 **[def]** Define rank, regular point and regular value of a smooth map (Definition [[§30 The Differential in Coordinates#^def-30-2|§30.2]], Definition [[§30 The Differential in Coordinates#^def-30-3|§30.3]], Definition [[§30 The Differential in Coordinates#^def-30-4|§30.4]]).
- [ ] Q2 **[state]** State both results.
- [ ] Q3 Proposition: why does $\varphi$ carry $F^{-1}(c)$ onto $\tilde F^{-1}(\tilde c)$, and why are the two regularity conditions the same (matrix theorem)?
- [ ] Q4 Corollary: at $p \in F^{-1}(c)$, which charts do you choose, and why is $c$ still a regular value of $F|_U$?
- [ ] Q5 **[why]** This gives only a *topological* manifold. Which later theorem gives the smooth (regular submanifold) structure (Theorem [[§37 Regular Submanifolds#^thm-37-12|§37.12]])?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S1, S5.
> - $\tilde F(x) = \tilde c \iff F(\varphi^{-1}x) = c$ ($\psi$ injective on $V$).
> - Lemma [[§19 Smooth Functions and Smooth Maps#^lem-19-3|§19.3]](1) for the charts; $(F|_U)_\ast = F_\ast$ under $T_qU = T_qM$; then Corollary [[§7 The Regular Value Theorem#^cor-7-4|§7.4]].

#### Maps with zero differential are constant · P1

Proposition [[§30 The Differential in Coordinates#^prop-30-10|§30.10]] → drilled as [[Differentiable Manifolds HW Drill#^hw4-1|HW4.1]].

#### Velocity in coordinates · P1

$D_\gamma = \gamma_{\ast 0}(\frac{d}{dt}|_0)$ is a derivation at $p$ and $D_\gamma = \sum_j (x^j \circ \gamma)'(0)\, \frac{\partial}{\partial x^j}|_p$, see Proposition [[§31 Tangent Vectors as Velocities of Curves#^prop-31-1|§31.1]]. *Source: Assignment 3 (velocities of curves); proof in the notes.*

^nd-prop-31-1

- [ ] Q1 **[def]** Define a smooth curve and its velocity (Definition [[§31 Tangent Vectors as Velocities of Curves#^def-31-1|§31.1]], Definition [[§31 Tangent Vectors as Velocities of Curves#^def-31-2|§31.2]]).
- [ ] Q2 **[state]** State the proposition.
- [ ] Q3 Why is $D_\gamma$ a derivation without any computation?
- [ ] Q4 Compute its coefficients $D_\gamma[x^j]$ via the universal formula.
- [ ] Q5 **[why]** Why does $D_\gamma$ depend only on the velocity of the coordinate curve $\varphi \circ \gamma$? Give two different curves with the same velocity.

> [!tip]- Hints: route of the proof in the notes
> - $d/dt|_0$ is a coordinate derivation, pushed forward by $\gamma$ (Proposition [[§28 Derivations and the Abstract Tangent Space#^prop-28-5|§28.5]]).
> - $D_\gamma[x^j] = \frac{d}{dt}|_0 x^j(\gamma(t))$.

#### Every tangent vector is a velocity · P1

Theorem [[§31 Tangent Vectors as Velocities of Curves#^thm-31-2|§31.2]] → drilled as [[Differentiable Manifolds HW Drill#^hw3-2|HW3.2]].

### Priority 2 · stated or done in class

#### The geometric tangent space of a graph · P2

For $M = \{(x, G(x)) : x \in A\}$, $A \subseteq \mathbb{R}^n$ open, $G$ smooth, and $p = (x_0, G(x_0))$: $T^{\mathrm{geo}}_pM = \{(u, G'(x_0)u) : u \in \mathbb{R}^n\}$, an $n$-dimensional subspace, see Lemma [[§25 The Geometric Tangent Space#^lem-25-2|§25.2]]. *Source: Lecture 8 ("I'm going to leave that as an exercise … it's not a trivial exercise … I won't prove the claim"); filled in.* **[class exercise, Lecture 8]**

^nd-lem-25-2

- [ ] Q1 **[state]** State the lemma: "the tangent space to a graph is the graph of the derivative".
- [ ] Q2 $\subseteq$: write a curve in $M$ as $\gamma = (\gamma_1, \gamma_2)$. Why is $\gamma_2 = G \circ \gamma_1$, and what does the chain rule give at $t = 0$?
- [ ] Q3 $\supseteq$: given $u$, which curve in $M$ through $p$ has velocity $(u, G'(x_0)u)$? Why is it defined for small $|t|$?
- [ ] Q4 Why is the result a linear subspace of dimension $n$?
- [ ] Q5 **[why]** Why are both inclusions needed (what does $\subseteq$ alone give)? Which construction in $\supseteq$ reappears later (lifting a straight line from a chart, e.g. in Theorem [[§31 Tangent Vectors as Velocities of Curves#^thm-31-2|§31.2]])?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S10 (curves), S14 (differentiate an identity).
> - $\gamma_2'(0) = G'(x_0)\gamma_1'(0)$.
> - $\gamma(t) = (x_0 + tu, G(x_0 + tu))$ for $|t| < r/(|u|+1)$.
> - Dimension: $u \mapsto (u, G'(x_0)u)$ is injective linear.

#### The geometric tangent space is the kernel of the Jacobian · P2

For a regular level set $M = F^{-1}(c) \subseteq \mathbb{R}^{n+k}$ and $p \in M$, $T^{\mathrm{geo}}_pM = \ker F'(p)$, of dimension $n$, see Theorem [[§25 The Geometric Tangent Space#^thm-25-3|§25.3]] (and Theorem [[§25 The Geometric Tangent Space#^thm-25-7|§25.7]], Corollary [[§25 The Geometric Tangent Space#^cor-25-4|§25.4]]: also $= \operatorname{im} D\alpha_a$ for the graph parametrization). *Source: Lecture 7 (the inclusion), Lecture 8 (sketch: "we must have equality").*

^nd-thm-25-3

- [ ] Q1 **[state]** State the theorem, with the hypotheses on $F$ and $c$.
- [ ] Q2 Prove $T^{\mathrm{geo}}_pM \subseteq \ker F'(p)$: which identity do you differentiate?
- [ ] Q3 Why may you assume $M$ is a graph near $p$? Which two facts justify the reduction (a coordinate permutation; Lemma [[§25 The Geometric Tangent Space#^lem-25-1|§25.1]])?
- [ ] Q4 What does the graph lemma give for $\dim T^{\mathrm{geo}}_pM$?
- [ ] Q5 Compute $\dim \ker F'(p)$. Which hypothesis is used?
- [ ] Q6 Conclude equality.
- [ ] Q7 **[why]** Without the regular value hypothesis, which inclusion can fail? Try $F(x,y) = y^2 - x^3$ at $0$, or $F(x,y) = x^2 + y^2$ at $c = 0$.

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S6 (prove $\subseteq$, then count dimensions), S7.
> - $F \circ \gamma \equiv c$, so $F'(p)\gamma'(0) = 0$.
> - Steps 1–3 of Theorem [[§7 The Regular Value Theorem#^thm-7-3|§7.3]] make $M$ locally a graph; Lemma [[§25 The Geometric Tangent Space#^lem-25-2|§25.2]] gives dimension $n$.
> - Rank–nullity: $\dim \ker F'(p) = (n+k) - k$. An $n$-dimensional subspace of an $n$-dimensional space is everything.

#### Tangent spaces of the classical groups · P2

$T^{\mathrm{geo}}_I\mathrm{O}(n) = \mathrm{Skew}(n)$ (Example [[§25 The Geometric Tangent Space#^ex-25-2|§25.2]]), $T^{\mathrm{geo}}_I\mathrm{U}(n) = \mathfrak{u}(n)$ (Example [[§25 The Geometric Tangent Space#^ex-25-3|§25.3]]), $T^{\mathrm{geo}}_I\mathrm{SL}(n) = \{\operatorname{tr} A = 0\}$, and $T^{\mathrm{geo}}_gG = g \cdot T^{\mathrm{geo}}_IG = T^{\mathrm{geo}}_IG \cdot g$, see Theorem [[§25 The Geometric Tangent Space#^thm-25-5|§25.5]]. *Source: notes (the groups of Lectures 3 and 6–7).*

^nd-thm-25-5

- [ ] Q1 **[state]** State the table: each group, its presentation, dimension and tangent space at $I$.
- [ ] Q2 $\mathrm{O}(n)$ at $I$ directly: differentiate $\gamma(t)\gamma(t)^{\mathsf T} = I$. What do you get, and why is that enough (dimension count)?
- [ ] Q3 $\mathrm{SL}(n)$: using Jacobi's formula, what is $\ker d(\det)_g$? Show it equals $g \cdot \mathfrak{sl}(n)$ and $\mathfrak{sl}(n) \cdot g$.
- [ ] Q4 $\mathrm{O}(n)$ at $g$: why is $g\,\mathrm{Skew}(n) = \mathrm{Skew}(n)\,g$? (Conjugation by orthogonal $g$ preserves skew matrices.)
- [ ] Q5 Why is $T_g\mathrm{SO}(n) = T_g\mathrm{O}(n)$?
- [ ] Q6 **[why]** Why is $\dim \mathfrak{sl}(n) = n^2 - 1$? Why is $\mathfrak{u}(n)$ not a complex subspace of $\mathrm{Mat}(n,\mathbb{C})$?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S6, S10, S15 (translate from $I$ to $g$).
> - $\ker dF_g$ from Proposition [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^prop-23-1|§23.1]]; Theorem [[§25 The Geometric Tangent Space#^thm-25-3|§25.3]] in its vector-space form.
> - $\mathrm{SL}$: $A \in T_g$ iff $\operatorname{tr}(g^{-1}A) = 0$; write $A = gB$ or $A = Bg$.
> - $(gXg^{-1})^{\mathsf T} = -gXg^{-1}$; $\mathrm{SO}(n)$ open in $\mathrm{O}(n)$ and Lemma [[§25 The Geometric Tangent Space#^lem-25-1|§25.1]].

#### Germs: the equivalence relation and the algebra · P2

Agreement near $p$ is an equivalence relation (Proposition [[§27 Germs#^prop-27-1|§27.1]]); germs form a commutative $\mathbb{R}$-algebra $C^\infty_p(M)$ with well-defined evaluation (Proposition [[§27 Germs#^prop-27-2|§27.2]]). *Source: Lecture 8 (operations sketched, checks "tedious"); filled in.*

^nd-prop-27-1

- [ ] Q1 **[def]** Define agreement near $p$ and the germ of $f$ at $p$ (Definition [[§27 Germs#^def-27-1|§27.1]], Definition [[§27 Germs#^def-27-2|§27.2]]).
- [ ] Q2 **[state]** State both propositions.
- [ ] Q3 Prove transitivity. Which property of open sets is used?
- [ ] Q4 Define $[f] + [g]$ and $[f][g]$ and show they do not depend on the representatives.
- [ ] Q5 Why is evaluation $[f] \mapsto f(p)$ well defined?
- [ ] Q6 **[why]** Why is a germ not determined by a single function on a fixed neighbourhood (Example [[§27 Germs#^ex-27-1|§27.1]]), and why is it more than its Taylor series (Example [[§27 Germs#^ex-27-2|§27.2]])?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S2 (define on representatives, check well-definedness).
> - Transitivity on $W_1 \cap W_2$ (finite intersections of open sets are open).
> - Sums and products of representatives agree on $W_1 \cap W_2$.

#### Germ derivations and global derivations · P2

$D \mapsto (f \mapsto D[f])$ is a linear isomorphism from derivations of germs at $p$ to Lee's derivations of $C^\infty(M)$ at $p$, granting bump functions, see Proposition [[§28 Derivations and the Abstract Tangent Space#^prop-28-3|§28.3]]. *Source: notes (comparison with Lee).*

^nd-prop-28-3

- [ ] Q1 **[state]** State the proposition: both notions of tangent vector.
- [ ] Q2 Why is $v_D$ a derivation of $C^\infty(M)$, and why is $D \mapsto v_D$ linear?
- [ ] Q3 Where do bump functions enter (injectivity: every germ has a global representative)?
- [ ] Q4 **[why]** Which result of the course is assumed and not proved here (Proposition [[§53 Vector Fields#^prop-53-4|§53.4]])? Why does the course prefer germs?

> [!tip]- Hints: route of the proof in the notes
> - $f \mapsto [f]$ is an algebra map compatible with evaluation.
> - $\psi f$ extended by zero represents $[f]$; surjectivity: global derivations are local.

#### Pullback of germs; the pushforward is a linear map of tangent spaces · P2

$F_p^\ast[g] = [g \circ F]$ is a well-defined algebra homomorphism with $F_p^\ast(I_{F(p)}) \subseteq I_p$ (Proposition [[§28 Derivations and the Abstract Tangent Space#^prop-28-4|§28.4]]); $F_{\ast p}D = D \circ F_p^\ast$ is a derivation at $F(p)$ and $F_{\ast p}$ is linear (Proposition [[§28 Derivations and the Abstract Tangent Space#^prop-28-5|§28.5]]). *Source: Lectures 9–10 ("one has to check this [is a] derivation").*

^nd-prop-28-5

- [ ] Q1 **[def]** Define the pullback of germs and the pushforward $F_{\ast p}$ (Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-5|§28.5]], Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-6|§28.6]]).
- [ ] Q2 **[state]** State both propositions.
- [ ] Q3 Why is $F_p^\ast$ well defined on germs? Which property of $F$ is used?
- [ ] Q4 Prove the Leibniz rule for $F_{\ast p}D$ at $F(p)$. Which two properties of $F_p^\ast$ do you use?
- [ ] Q5 **[why]** Why does pulling back go the opposite way to $F$, and why does that make the pushforward of a derivation possible while functions cannot be pushed forward?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S2.
> - $g = g'$ on $W$ ⇒ $g \circ F = g' \circ F$ on $F^{-1}(W)$, open by continuity.
> - $(F_{\ast p}D)([g][h]) = D(F_p^\ast[g] \cdot F_p^\ast[h])$, then Leibniz at $p$ and $(F_p^\ast[g])(p) = g(F(p))$.

#### The chain rule · P2

$(G \circ F)_{\ast p} = G_{\ast F(p)} \circ F_{\ast p}$ and $(\mathrm{id}_M)_{\ast p} = \mathrm{id}$, see Theorem [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]]. *Source: Lecture 10 ("the proof of the chain rule is one line"; "I will leave it as an exercise. Use this to conclude the proof").* **[class exercise, Lecture 10]**

^nd-thm-28-6

- [ ] Q1 **[state]** State the chain rule.
- [ ] Q2 Prove that pullbacks compose in the opposite order: $(G \circ F)_p^\ast = F_p^\ast \circ G_{F(p)}^\ast$.
- [ ] Q3 Dualize: evaluate $(G \circ F)_{\ast p}D$ on a germ $[g]$ and rewrite step by step until you reach $G_{\ast F(p)}(F_{\ast p}D)[g]$.
- [ ] Q4 Prove $(\mathrm{id}_M)_{\ast p} = \mathrm{id}$.
- [ ] Q5 **[why]** Deduce that a diffeomorphism induces isomorphisms $\Phi_{\ast p}$ (Corollary [[§28 Derivations and the Abstract Tangent Space#^cor-28-7|§28.7]]). Why does $F_{\ast p}$ bijective at one point *not* make $F$ a diffeomorphism?

> [!tip]- Hints: route of the proof in the notes
> - $g \circ (G \circ F) = (g \circ G) \circ F$ (associativity).
> - Four equalities, each one application of Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-6|§28.6]].
> - Corollary: apply the rule to $\Phi^{-1} \circ \Phi = \mathrm{id}$ and $\Phi \circ \Phi^{-1} = \mathrm{id}$.

#### Coordinate derivations are derivations · P2

$\frac{\partial}{\partial x^i}|_p[f] = \frac{\partial f_\varphi}{\partial r^i}(\varphi(p))$ is well defined on germs and a derivation at $p$ (Proposition [[§29 Coordinate Derivations and the Basis Theorem#^prop-29-2|§29.2]]); and $\partial f/\partial x^j$ is smooth on $U$ with coordinate representation $\partial f_\varphi/\partial r^j$ (Lemma [[§29 Coordinate Derivations and the Basis Theorem#^lem-29-1|§29.1]]). *Source: Lecture 8 ("it's linear, and the product rule will be inherited"); well-definedness filled in.*

^nd-prop-29-2

- [ ] Q1 **[def]** Define the coordinate functions of a chart and the coordinate derivations (Definition [[§29 Coordinate Derivations and the Basis Theorem#^def-29-1|§29.1]], Definition [[§29 Coordinate Derivations and the Basis Theorem#^def-29-2|§29.2]]). Why $r^i$ on $\mathbb{R}^n$ and $x^i$ on $M$?
- [ ] Q2 **[state]** State the proposition.
- [ ] Q3 Well defined: if $(f, U_1) \sim (g, U_2)$, why are the two partial derivatives at $\varphi(p)$ equal?
- [ ] Q4 Linearity and Leibniz: from which properties of ordinary partial derivatives?
- [ ] Q5 **[why]** Compute $\frac{\partial}{\partial x^i}|_p[x^j]$. Why does this already give linear independence of the coordinate derivations?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S1, S2.
> - $f_\varphi = g_\varphi$ on $\varphi(W \cap U)$, open; partial derivatives are local.
> - $(fg)_\varphi = f_\varphi g_\varphi$ and the product rule in $\mathbb{R}^n$.
> - $(x^j)_\varphi = r^j$, so the value is $\delta^j_i$.

#### Hadamard's lemma and Taylor–Hadamard · P2

For $f$ smooth near $a \in \mathbb{R}^n$ and a ball $B$ centred at $a$: $f(r) = f(a) + \sum_i (r^i - a^i) f_i(r)$ with $f_i$ smooth on $B$ and $f_i(a) = \partial f/\partial r^i(a)$ (Lemma [[§29 Coordinate Derivations and the Basis Theorem#^lem-29-3|§29.3]]); applied twice, $f = f(a) + \sum_i (r^i - a^i)\partial_i f(a) + \sum_{i,j}(r^i - a^i)(r^j - a^j) f_{ij}$ (Lemma [[§29 Coordinate Derivations and the Basis Theorem#^lem-29-4|§29.4]]). *Source: Lecture 9 ("delightfully simple"; smoothness of the $f_i$ is "a key point").*

^nd-lem-29-3

- [ ] Q1 **[state]** State Hadamard's lemma, including the formula for $f_i$.
- [ ] Q2 Why does the segment from $a$ to $r$ stay in the domain, and what is $h(t)$?
- [ ] Q3 Apply the fundamental theorem of calculus and the chain rule to get the identity.
- [ ] Q4 Why is each $f_i$ smooth on $B$?
- [ ] Q5 Derive Taylor–Hadamard by applying the lemma to each $f_i$ and substituting.
- [ ] Q6 **[why]** Why is smoothness of the $f_i$ "a key point" (what would fail in the basis theorem if $f_i$ were only continuous)? Why a ball and not any open set?

> [!tip]- Hints: route of the proof in the notes
> - $h(t) = f(a + t(r-a))$, $f(r) - f(a) = \int_0^1 h'(t)\,dt$.
> - $h'(t) = \sum_i \partial_i f(a + t(r-a))(r^i - a^i)$; pull $(r^i - a^i)$ out of the integral.
> - Differentiation under the integral sign.

#### Derivations on $\mathbb{R}^n$ · P2

For a derivation $D$ at $a$ on open $W \subseteq \mathbb{R}^n$: $D = \sum_i D[r^i]\, \frac{\partial}{\partial r^i}|_a$, see Corollary [[§29 Coordinate Derivations and the Basis Theorem#^cor-29-5|§29.5]]. *Source: Lecture 9.*

^nd-cor-29-5

- [ ] Q1 **[state]** State the corollary.
- [ ] Q2 Why may you replace a representative by its restriction to a ball?
- [ ] Q3 Write $[f]$ as a sum of germs using Taylor–Hadamard.
- [ ] Q4 Apply $D$: which terms vanish, and by which part of Lemma [[§28 Derivations and the Abstract Tangent Space#^lem-28-2|§28.2]]?
- [ ] Q5 **[why]** Why is $D[r^i - a^i] = D[r^i]$? Why are $(r^i - a^i)$ and $(r^j - a^j)f_{ij}$ in $I_a$?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S9 (a derivation is determined by the coordinate functions).
> - Constant term: Lemma [[§28 Derivations and the Abstract Tangent Space#^lem-28-2|§28.2]](1); quadratic terms: products of two germs in $I_a$, Lemma [[§28 Derivations and the Abstract Tangent Space#^lem-28-2|§28.2]](2).

#### Basis theorem · P2

For any chart $(U, \varphi)$ at $p$, the $\frac{\partial}{\partial x^i}|_p$ form a basis of $T_pM$, and $D = \sum_i D[x^i]\, \frac{\partial}{\partial x^i}|_p$ (universal formula), see Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]]. *Source: Lecture 9.*

^nd-thm-29-6

- [ ] Q1 **[state]** State the theorem and the universal formula.
- [ ] Q2 Step 1: push $D$ down by the chart. What is $\tilde D[g]$, and why is this legitimate (Lemma [[§28 Derivations and the Abstract Tangent Space#^lem-28-8|§28.8]], Proposition [[§28 Derivations and the Abstract Tangent Space#^prop-28-9|§28.9]])?
- [ ] Q3 Step 2: apply Corollary [[§29 Coordinate Derivations and the Basis Theorem#^cor-29-5|§29.5]] downstairs.
- [ ] Q4 Step 3: read it back upstairs with $g = f_\varphi$. Why is $\tilde D[r^i] = D[x^i]$ and $\partial f_\varphi/\partial r^i(a) = \frac{\partial}{\partial x^i}|_p[f]$?
- [ ] Q5 Step 4: linear independence and uniqueness of the coefficients.
- [ ] Q6 **[why]** Why does $\dim T_pM = n$ not depend on the chart (Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-9|§29.9]]), and how does this give smooth invariance of dimension (Corollary [[§29 Coordinate Derivations and the Basis Theorem#^cor-29-10|§29.10]])?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S9.
> - $\tilde D[g] = D[g \circ \varphi]$; $r^i \circ \varphi = x^i$.
> - Independence: evaluate $\sum c_i \partial/\partial x^i|_p$ on $[x^j]$.
> - Invariance: a diffeomorphism $U \to V$ gives an isomorphism $T_pU \cong T_{F(p)}V$ of dimensions $m$ and $n$.

#### Ambient and abstract tangent spaces agree · P2

For a regular level set $M \subseteq \mathbb{R}^{n+k}$, $v \mapsto D_v$, $D_v(f) = \frac{d}{dt}|_0 f(\gamma(t))$, is an isomorphism $T^{\mathrm{geo}}_pM \to T_pM$, see Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-7|§29.7]] (with Proposition [[§25 The Geometric Tangent Space#^prop-25-8|§25.8]], Proposition [[§25 The Geometric Tangent Space#^prop-25-9|§25.9]]). *Source: announced in lecture in answer to a student ("they are the same, but it has to be proved"); Lecture 17: "from now on" $T^{\mathrm{geo}}_pM = T_pM$.*

^nd-thm-29-7

- [ ] Q1 **[def]** Define $D_v$ (Definition [[§25 The Geometric Tangent Space#^def-25-4|§25.4]]).
- [ ] Q2 **[state]** State the theorem.
- [ ] Q3 Why does $D_v(f)$ depend only on the germ of $f$ and only on $v$, not on the curve? (Use the graph chart: $D_v(f) = u \cdot \nabla f_\varphi(x_0)$.)
- [ ] Q4 Why is $D_v$ a derivation, and why is $v \mapsto D_v$ linear?
- [ ] Q5 Injectivity: compute $D_v(x^i)$ for the graph-chart coordinates.
- [ ] Q6 Surjectivity: which dimension count?
- [ ] Q7 **[why]** Why is it not obvious that the two spaces are "the same"? What does each one need that the other does not (an ambient space; a smooth structure)?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S7 (injective between equal dimensions).
> - Locally a graph; $\varphi \circ \sigma$ has velocity $u$, then the chain rule.
> - $D_v(x^i) = u^i$; $\dim T^{\mathrm{geo}}_pM = n$ (Theorem [[§25 The Geometric Tangent Space#^thm-25-3|§25.3]]) $= \dim T_pM$ (Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]]).

#### The matrix of the differential · P2

$F_{\ast p}(\frac{\partial}{\partial x^i}|_p) = \sum_j \frac{\partial F^j}{\partial x^i}(p)\, \frac{\partial}{\partial y^j}|_{F(p)}$, and $\frac{\partial F^j}{\partial x^i}(p) = \frac{\partial \tilde F^j}{\partial r^i}(\varphi(p))$: the matrix of $F_{\ast p}$ is the Jacobian of $\tilde F = \psi \circ F \circ \varphi^{-1}$, see Theorem [[§30 The Differential in Coordinates#^thm-30-2|§30.2]] and Proposition [[§30 The Differential in Coordinates#^prop-30-1|§30.1]]. *Source: Lecture 10 ("a one-line proof").*

^nd-thm-30-2

- [ ] Q1 **[state]** State the theorem and the upstairs–downstairs identity.
- [ ] Q2 Prove $F^j \circ \varphi^{-1} = \tilde F^j$ (where $F^j = y^j \circ F$).
- [ ] Q3 Put $E = F_{\ast p}(\partial/\partial x^i|_p)$. By the universal formula at $F(p)$, what are its coefficients?
- [ ] Q4 Compute $E[y^j]$ from the definition of the pushforward.
- [ ] Q5 **[why]** Why does the theorem need charts with $F(U) \subseteq V$? Deduce the chain rule in coordinates (Corollary [[§30 The Differential in Coordinates#^cor-30-3|§30.3]]): matrices multiply.

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S9 (universal formula: coefficients are values on the $y^j$).
> - $E[y^j] = \frac{\partial}{\partial x^i}|_p[y^j \circ F] = \frac{\partial F^j}{\partial x^i}(p)$.
> - Coordinates: $y^j = r^j \circ \psi$.

#### Change of coordinates · P2

For two charts at $p$: $\frac{\partial}{\partial \tilde x^j}|_p = \sum_i \frac{\partial x^i}{\partial \tilde x^j}(p)\frac{\partial}{\partial x^i}|_p$; components transform by $v[\tilde x^j] = \sum_i \frac{\partial \tilde x^j}{\partial x^i}(p) v[x^i]$; the two matrices are inverse, see Corollary [[§30 The Differential in Coordinates#^cor-30-4|§30.4]]. *Source: Lecture 10 (item 1); items 2–3 filled in.*

^nd-cor-30-4

- [ ] Q1 **[state]** State the three items.
- [ ] Q2 (1): apply the matrix theorem to which map, with which charts? Why must you first restrict both charts to $U \cap \tilde U$?
- [ ] Q3 (2): use the universal formula for $v$ in the $x$-chart and evaluate on $[\tilde x^j]$.
- [ ] Q4 (3): evaluate $\partial/\partial \tilde x^l|_p$ on $[\tilde x^j]$ in two ways.
- [ ] Q5 **[why]** Why do basis vectors and components transform with *inverse* matrices? Which Jacobians are these (transition functions in the two directions)?

> [!tip]- Hints: route of the proof in the notes
> - (1): the identity map $(U \cap \tilde U, \tilde\varphi) \to (U \cap \tilde U, \varphi)$, Theorem [[§30 The Differential in Coordinates#^thm-30-2|§30.2]].
> - (2): $v = \sum_i v[x^i]\partial/\partial x^i|_p$, apply to $[\tilde x^j]$.
> - (3): $\delta^j_l = \sum_i \frac{\partial \tilde x^j}{\partial x^i}\frac{\partial x^i}{\partial \tilde x^l}$.

#### Agreement with the vector-space differential; translations · P2

For $F : W \subseteq \mathbb{R}^m \to \mathbb{R}^n$, $F_{\ast a}$ corresponds to the Jacobian $F'(a)$ and $v \leftrightarrow D_v$ (Proposition [[§30 The Differential in Coordinates#^prop-30-5|§30.5]]); for a vector space $V$, $v \mapsto D_v|_a$ is a basis-free isomorphism $V \cong T_aV$ with $L_{\ast}D_v = D_{Lv}$ (Corollary [[§30 The Differential in Coordinates#^cor-30-6|§30.6]]); translations $\tau_p$ carry $D_v|_0$ to $D_v|_p$ (Proposition [[§30 The Differential in Coordinates#^prop-30-7|§30.7]]). *Source: Lecture 17 ("its pushforward is the identification"); filled in.*

^nd-prop-30-5

- [ ] Q1 **[state]** State the three results.
- [ ] Q2 Proposition: with identity charts, what is $\tilde F$, and what does the matrix theorem give?
- [ ] Q3 Corollary: why is $D_v|_a$ well defined on germs, and why is $L_\ast(D_v|_a) = D_{Lv}|_{La}$ for linear $L$?
- [ ] Q4 Translations: why is $\tau_p$ a diffeomorphism, and compute $(\tau_p)_{\ast 0}(D_v|_0)[g]$.
- [ ] Q5 **[why]** Why is this what lets you write $T_g\mathrm{GL}(n) = \mathrm{Mat}(n)$ and compute $d(\text{conjugation})_I$ as a matrix map (2021 exam)?

> [!tip]- Hints: route of the proof in the notes
> - Identity charts: $\tilde F = F$; $\partial/\partial r^i|_a \mapsto e_i$.
> - $D_w|_b[g \circ L] = \frac{d}{dt}|_0 g(Lb + tLw)$.
> - $(g \circ \tau_p)(tv) = g(p + tv)$.

#### Velocity of a composite: computing differentials by curves · P2

$D_{F \circ \gamma} = F_{\ast p}(D_\gamma)$; so $F_{\ast p}(D) = D_{F \circ \gamma}$ for any curve with $D_\gamma = D$, see Corollary [[§31 Tangent Vectors as Velocities of Curves#^cor-31-3|§31.3]]. *Source: notes (the course's main computational tool; Lecture 6: "you use curves").*

^nd-cor-31-3

- [ ] Q1 **[state]** State the corollary.
- [ ] Q2 Prove $D_{F \circ \gamma} = F_{\ast p}(D_\gamma)$ from the definition of velocity and the chain rule.
- [ ] Q3 Why does such a curve exist for every $D$?
- [ ] Q4 Use it: compute $d(\det)_I(A)$ with $\gamma(t) = I + tA$ (or $e^{tA}$).
- [ ] Q5 **[why]** Why is the answer independent of the curve chosen? What would you do if $\gamma$ were not defined on an interval around $0$?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S10.
> - $(F \circ \gamma)_{\ast 0} = F_{\ast p} \circ \gamma_{\ast 0}$ applied to $d/dt|_0$.
> - Existence: Theorem [[§31 Tangent Vectors as Velocities of Curves#^thm-31-2|§31.2]] ([[Differentiable Manifolds HW Drill#^hw3-2|HW3.2]]).

#### The tangent space of a product · P2

$\Theta(v, w) = \iota_{1\ast}v + \iota_{2\ast}w$ is an isomorphism $T_{p_1}M_1 \oplus T_{p_2}M_2 \to T_p(M_1 \times M_2)$ with inverse $(\pi_{1\ast}, \pi_{2\ast})$, see Theorem [[§31 Tangent Vectors as Velocities of Curves#^thm-31-4|§31.4]]; in product coordinates the summands are spanned by the $\partial/\partial x^i$ and the $\partial/\partial y^j$ (Corollary [[§31 Tangent Vectors as Velocities of Curves#^cor-31-5|§31.5]]), and $D_\gamma = \iota_{1\ast}D_{\gamma_1} + \iota_{2\ast}D_{\gamma_2}$ (Corollary [[§31 Tangent Vectors as Velocities of Curves#^cor-31-6|§31.6]]). *Source: Lecture 11 ("you can check that it's injective, so I won't do it").* **[class exercise, Lecture 11]**

^nd-thm-31-4

- [ ] Q1 **[state]** State the theorem. Which maps are $\iota_1$, $\iota_2$, $\pi_1$, $\pi_2$?
- [ ] Q2 Why are $\Theta$ and $\Psi$ linear and chart-free?
- [ ] Q3 Prove the four identities $\pi_{1\ast}\iota_{1\ast} = \mathrm{id}$, $\pi_{2\ast}\iota_{2\ast} = \mathrm{id}$, $\pi_{2\ast}\iota_{1\ast} = 0$, $\pi_{1\ast}\iota_{2\ast} = 0$.
- [ ] Q4 Deduce $\Psi \circ \Theta = \mathrm{id}$, hence $\Theta$ injective; in particular $\iota_{1\ast}$ is injective (the class exercise).
- [ ] Q5 Conclude that $\Theta$ is an isomorphism. Which dimension count?
- [ ] Q6 **[why]** For a curve $\gamma = (\gamma_1, \gamma_2)$, show $D_\gamma = \iota_{1\ast}D_{\gamma_1} + \iota_{2\ast}D_{\gamma_2}$. Where is this used (the 2025 graph–diagonal transversality item)?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S14, S7.
> - $\pi_1 \circ \iota_1 = \mathrm{id}$; $\pi_2 \circ \iota_1$ is constant, so Lemma [[§28 Derivations and the Abstract Tangent Space#^lem-28-10|§28.10]] gives $0$.
> - $\dim = m_1 + m_2$ on both sides (Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]], Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-10|§19.10]]).
> - Curves: $\pi_{i\ast}D_\gamma = D_{\pi_i \circ \gamma}$ by Corollary [[§31 Tangent Vectors as Velocities of Curves#^cor-31-3|§31.3]].

#### Partial derivatives in one factor · P2

For $\varphi \in C^\infty(M \times N)$ and $v \in T_pM$, $\partial_v\varphi(q) = \frac{d}{dt}|_0 \varphi(\gamma(t), q)$ for any curve adapted to $v$, $= \sum_j v^j \frac{\partial \varphi}{\partial x^j}(p, q)$, and $\partial_v\varphi \in C^\infty(N)$, see Proposition [[§31 Tangent Vectors as Velocities of Curves#^prop-31-7|§31.7]]. *Source: Lecture 18 (curves, then coordinates).*

^nd-prop-31-7

- [ ] Q1 **[def]** Define $\partial_v\varphi$ (Definition [[§31 Tangent Vectors as Velocities of Curves#^def-31-3|§31.3]]).
- [ ] Q2 **[state]** State the three parts.
- [ ] Q3 (1): why is $t \mapsto (\gamma(t), q)$ a "horizontal" curve, and what is its velocity?
- [ ] Q4 (2): expand $v$ in the $x$-coordinates and use product coordinates.
- [ ] Q5 **[why]** Why does (2) make smoothness in $q$ evident, while (1) does not? Where is this used (smoothness of left-invariant vector fields, T11)?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S10 then S1.
> - $\partial_v\varphi(q) = v[\varphi \circ \iota^q] = D_\gamma[\varphi \circ \iota^q]$.
> - Corollary [[§31 Tangent Vectors as Velocities of Curves#^cor-31-6|§31.6]] and Corollary [[§31 Tangent Vectors as Velocities of Curves#^cor-31-5|§31.5]]; partials of a smooth function are smooth (Lemma [[§29 Coordinate Derivations and the Basis Theorem#^lem-29-1|§29.1]]).

### Priority 3 · filled in, using a technique the homework drills

#### The pushforward along a constant map · P3

A constant map $\kappa$ is smooth with $\kappa_{\ast x} = 0$; and if $F \circ \iota$ is constant then $\iota_{\ast p}(T_pS) \subseteq \ker F_{\ast \iota(p)}$, see Lemma [[§28 Derivations and the Abstract Tangent Space#^lem-28-10|§28.10]]. *Source: notes (filled in).*

^nd-lem-28-10

- [ ] Q1 **[state]** State both parts.
- [ ] Q2 Why is $\kappa$ smooth (coordinate representation)?
- [ ] Q3 Compute $(\kappa_{\ast x}D)[g]$. Which property of derivations finishes it?
- [ ] Q4 Deduce (2) from (1) and the chain rule.
- [ ] Q5 **[why]** Where is (2) used: the inclusion $T_pM \subseteq \ker F_{\ast p}$ for a level set $M = F^{-1}(c)$, and the identities $\pi_{2\ast}\iota_{1\ast} = 0$ in the product theorem.

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S14 (differentiate the identity "$F \circ \iota$ = const").
> - $g \circ \kappa$ is the constant $g(q_0)$; Lemma [[§28 Derivations and the Abstract Tangent Space#^lem-28-2|§28.2]](1).

### Priority 4 · notes only (optional before the midterm)

#### Locality of the geometric tangent space · P4

If $M' \subseteq M$ is open in $M$ and $p \in M'$, then $T^{\mathrm{geo}}_pM' = T^{\mathrm{geo}}_pM$, see Lemma [[§25 The Geometric Tangent Space#^lem-25-1|§25.1]]. *Source: notes.*

^nd-lem-25-1

- [ ] Q1 **[def]** Define the geometric tangent space (Definition [[§25 The Geometric Tangent Space#^def-25-1|§25.1]]).
- [ ] Q2 **[state]** State the lemma.
- [ ] Q3 Prove $\subseteq$ in one line.
- [ ] Q4 Prove $\supseteq$: given a curve in $M$ through $p$, why does it stay in $M'$ for $|t| < \delta$, and why does restricting it not change the velocity?
- [ ] Q5 **[why]** Where is "open in $M$" used? Give a non-open $M' \subseteq M$ (a point of a line) where the equality fails.

> [!tip]- Hints: route of the proof in the notes
> - $M' = M \cap O$, $O$ open; $\gamma^{-1}(O)$ is open in the interval and contains $0$.
> - Same difference quotients for small $t$.

#### The adjoint action · P4

For $G = \mathrm{SL}(n), \mathrm{O}(n), \mathrm{SO}(n), \mathrm{U}(n)$ and $\mathfrak{g} = T^{\mathrm{geo}}_IG$, $\mathrm{Ad}_g(X) = gXg^{-1}$ is a linear isomorphism of $\mathfrak{g}$ with $\mathrm{Ad}_{gh} = \mathrm{Ad}_g \circ \mathrm{Ad}_h$, and $L_g = R_g \circ \mathrm{Ad}_g$, see Proposition [[§25 The Geometric Tangent Space#^prop-25-6|§25.6]]. *Source: notes.*

^nd-prop-25-6

- [ ] Q1 **[def]** Define the adjoint action (Definition [[§25 The Geometric Tangent Space#^def-25-2|§25.2]]).
- [ ] Q2 **[state]** State the proposition.
- [ ] Q3 Check that $\mathrm{Ad}_g$ maps $\mathfrak{g}$ into itself, case by case ($\operatorname{tr}$, skew, skew-Hermitian).
- [ ] Q4 Prove the composition law and deduce that $\mathrm{Ad}_g$ is invertible.
- [ ] Q5 **[why]** How does this connect to the 2021 exam item on the differential of conjugation at $I$ (compute it with curves, Corollary [[§31 Tangent Vectors as Velocities of Curves#^cor-31-3|§31.3]])?

> [!tip]- Hints: route of the proof in the notes
> - $\operatorname{tr}(gXg^{-1}) = \operatorname{tr} X$; $(gXg^{\mathsf T})^{\mathsf T} = gX^{\mathsf T}g^{\mathsf T}$.
> - $\mathrm{Ad}_{g^{-1}}$ is the inverse; $R_g(\mathrm{Ad}_g X) = gX$.

#### Open subsets have the same tangent spaces; charts are diffeomorphisms · P4

For $U \subseteq M$ open, restriction of germs is an algebra isomorphism and $\iota_{\ast p} : T_pU \to T_pM$ is an isomorphism (Lemma [[§28 Derivations and the Abstract Tangent Space#^lem-28-8|§28.8]]); a chart $\varphi : U \to \varphi(U)$ is a diffeomorphism, so $\varphi_{\ast p} : T_pM \to T_{\varphi(p)}\mathbb{R}^n$ is an isomorphism (Proposition [[§28 Derivations and the Abstract Tangent Space#^prop-28-9|§28.9]]). *Source: notes.*

^nd-lem-28-8

- [ ] Q1 **[state]** State the lemma and the proposition.
- [ ] Q2 Why is restriction of germs surjective? Why injective? Where is openness of $U$ used?
- [ ] Q3 How does an algebra isomorphism compatible with evaluation give an isomorphism of derivations?
- [ ] Q4 Why is $\varphi : U \to \varphi(U)$ a diffeomorphism (coordinate representations of $\varphi$, $\varphi^{-1}$)?
- [ ] Q5 **[why]** Where does the basis theorem use this (Step 1: push $D$ down by the chart)? What would fail for the geometric tangent space if $U$ were not open (Lemma [[§25 The Geometric Tangent Space#^lem-25-1|§25.1]])?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S11 (local, then global).
> - A germ on $U$ is represented on $V' \subseteq U$, open in $M$.
> - In charts $(U, \varphi)$ and $(\varphi(U), \mathrm{id})$ both maps are the identity; then Corollary [[§28 Derivations and the Abstract Tangent Space#^cor-28-7|§28.7]].

# T5. Cotangent spaces

## Definitions T5

### Priority 1 · homework (directly or extended)

#### The ideal $I_p$ and its square · P1

$I_p = \{[f] : f(p) = 0\}$, and $I_p^2$ = finite sums of products of two elements of $I_p$, see Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-3|§28.3]]. *Source: Lecture 9; Assignment 3.*

^nd-def-28-3

- [ ] Q1 **[def]** Define $I_p$ and $I_p^2$ (finite sums!).
- [ ] Q2 **[use]** Why is $I_p$ an ideal and $I_p^2 \subseteq I_p$ a subspace?
- [ ] Q3 **[why]** Characterize $I_p^2$ by derivatives: which germs lie in it? Why is the germ of $x^1 - x^1(p)$ in $I_p$ but not in $I_p^2$?
- [ ] Q4 **[use]** Why does every derivation vanish on $I_p^2$?

> [!tip]- Hints: where it lives, examples
> - Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-3|§28.3]], Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-4|§28.4]]; Lemma [[§28 Derivations and the Abstract Tangent Space#^lem-28-1|§28.1]].
> - Q3: Proposition [[§34 The Cotangent Space from Germs#^prop-34-1|§34.1]] ($f(p) = 0$ and $df_p = 0$; the hard direction is Hadamard, → drilled as [[Differentiable Manifolds HW Drill#^hw3-3|HW3.3]]). Q4: Lemma [[§28 Derivations and the Abstract Tangent Space#^lem-28-2|§28.2]].

#### The space $I_p/I_p^2$ · P1

The quotient vector space of $I_p$ by $I_p^2$, with classes ${[}[f]{]}$, see Definition [[§34 The Cotangent Space from Germs#^def-34-1|§34.1]]. *Source: Lecture 15; Assignment 3.*

^nd-def-34-1

- [ ] Q1 **[def]** Define $I_p/I_p^2$ and when ${[}[f]{]} = {[}[f']{]}$.
- [ ] Q2 **[use]** Give a basis of $I_p/I_p^2$ in a chart and the expansion of ${[}[f]{]}$.
- [ ] Q3 **[why]** Why does a derivation "see only the first derivatives"? Phrase it with $I_p/I_p^2$.
- [ ] Q4 **[use]** Which isomorphism $I_p/I_p^2 \to T^\ast_pM$ is there, and why is it defined without charts? (See the equivalence entry *Cotangent space* below.)

> [!tip]- Hints: where it lives, examples
> - Definition [[§34 The Cotangent Space from Germs#^def-34-1|§34.1]]; Q2: Proposition [[§34 The Cotangent Space from Germs#^prop-34-2|§34.2]] (${[}[x^i - x^i(p)]{]}$, coefficients $\partial f/\partial x^i(p)$).
> - Q3: the remark *A Derivation Sees Only the First Derivatives* in [[§29 Coordinate Derivations and the Basis Theorem|§29]]. Q4: Theorem [[§34 The Cotangent Space from Germs#^thm-34-4|§34.4]], ${[}[f]{]} \mapsto df_p$.

#### The pairing of $T_pM$ with $I_p/I_p^2$ · P1

$\langle D, {[}[f]{]} \rangle = D[f]$, see Definition [[§34 The Cotangent Space from Germs#^def-34-2|§34.2]]. *Source: Assignment 3.*

^nd-def-34-2

- [ ] Q1 **[def]** Define the pairing; what is a non-degenerate pairing?
- [ ] Q2 **[why]** Why is it well defined? Which property of derivations is used?
- [ ] Q3 **[use]** Prove it is non-degenerate on both sides.
- [ ] Q4 **[use]** Which linear-algebra theorem turns a non-degenerate pairing into isomorphisms, and what finiteness does it need?

> [!tip]- Hints: where it lives, examples
> - Definition [[§34 The Cotangent Space from Germs#^def-34-2|§34.2]], Definition [[§21 Linear Algebra Toolkit#^def-21-4|§21.4]], Definition [[§21 Linear Algebra Toolkit#^def-21-5|§21.5]]; Proposition [[§34 The Cotangent Space from Germs#^prop-34-3|§34.3]] → drilled as [[Differentiable Manifolds HW Drill#^hw3-3|HW3.3]].
> - Q4: Theorem [[§21 Linear Algebra Toolkit#^thm-21-5|§21.5]] (one side finite-dimensional).

### Priority 2 · stated or done in class

#### Cotangent space · P2

$T^\ast_pM = (T_pM)^\ast$, the dual of the abstract tangent space, see Definition [[§32 The Cotangent Space#^def-32-4|§32.4]]. *Source: Lecture 10.*

^nd-def-32-4

- [ ] Q1 **[def]** Define $T^\ast_pM$; what is a covector at $p$?
- [ ] Q2 **[use]** Give a basis of $T^\ast_pM$ in a chart, and say what it is dual to.
- [ ] Q3 **[why]** Why is $\dim T^\ast_pM = \dim M$? Which theorem about $T_pM$ is needed?
- [ ] Q4 **[example]** Give a covector at $p$ that is not $df_p$ for any $f$, or explain why none exists.

> [!tip]- Hints: where it lives, examples
> - Definition [[§32 The Cotangent Space#^def-32-4|§32.4]]; Definition [[§21 Linear Algebra Toolkit#^def-21-1|§21.1]], Definition [[§21 Linear Algebra Toolkit#^def-21-2|§21.2]].
> - Q2: Lemma [[§33 Covectors in Coordinates#^lem-33-1|§33.1]]. Q3: Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]].
> - Q4: none: $\sum_i \xi_i\,dx^i|_p = d\big(\sum_i \xi_i x^i\big)_p$. Pointwise every covector is a differential; for one-forms this fails (Proposition [[§51 One-Forms#^prop-51-3|§51.3]]).

#### Differential of a function $df_p$ · P2

$df_p = \iota_{f(p)} \circ f_{\ast p} : T_pM \to \mathbb{R}$, so $df_p(D) = (f_{\ast p}D)[r] = D[f]$, see Definition [[§32 The Cotangent Space#^def-32-5|§32.5]]. *Source: Lecture 10.*

^nd-def-32-5

- [ ] Q1 **[def]** Define $df_p$ through $f_{\ast p}$ and the identification $T_{f(p)}\mathbb{R} \cong \mathbb{R}$; what is that identification?
- [ ] Q2 **[use]** Prove $df_p(D) = D[f]$.
- [ ] Q3 **[use]** Prove $df_p = \sum_i \frac{\partial f}{\partial x^i}(p)\,dx^i|_p$.
- [ ] Q4 **[why]** Why is $df_p$ a covector and not the gradient vector? What extra structure would identify the two?
- [ ] Q5 **[example]** Compute $d(fg)_p$ and $d(h \circ f)_p$.

> [!tip]- Hints: where it lives, examples
> - Definition [[§32 The Cotangent Space#^def-32-1|§32.1]], Definition [[§32 The Cotangent Space#^def-32-3|§32.3]], Definition [[§32 The Cotangent Space#^def-32-5|§32.5]]; Q2: Proposition [[§32 The Cotangent Space#^prop-32-2|§32.2]] ($r \circ f = f$).
> - Q3: Lemma [[§33 Covectors in Coordinates#^lem-33-1|§33.1]]. Q4: the remark *Differential --- Not Gradient* in [[§33 Covectors in Coordinates|§33]]; Proposition [[§33 Covectors in Coordinates#^prop-33-3|§33.3]] (the dot product). Q5: Corollary [[§32 The Cotangent Space#^cor-32-3|§32.3]].

#### Components of a covector · P2

$\xi_i = \xi(\partial/\partial x^i|_p)$, so $\xi = \sum_i \xi_i\,dx^i|_p$, see Definition [[§33 Covectors in Coordinates#^def-33-1|§33.1]]. *Source: Lectures 10, 15.*

^nd-def-33-1

- [ ] Q1 **[def]** Define the components of $\xi \in T^\ast_pM$ in a chart, and of $v \in T_pM$.
- [ ] Q2 **[use]** Prove the expansion $\xi = \sum_j \xi_j\,dx^j|_p$ and the uniqueness of the coefficients.
- [ ] Q3 **[why]** How do the components $\xi_i$ change under a change of chart, compared with the components $v^i$? Why "transpose of the inverse"?
- [ ] Q4 **[example]** What are the components of $df_p$?

> [!tip]- Hints: where it lives, examples
> - Definition [[§33 Covectors in Coordinates#^def-33-1|§33.1]]; Q2: Corollary [[§33 Covectors in Coordinates#^cor-33-2|§33.2]]. Q3: Proposition [[§50 The Cotangent Bundle#^prop-50-2|§50.2]] versus Corollary [[§30 The Differential in Coordinates#^cor-30-4|§30.4]].
> - Q4: $\partial f/\partial x^i(p)$, Lemma [[§33 Covectors in Coordinates#^lem-33-1|§33.1]].

#### Pullback of covectors · P2

$F^\ast_p : T^\ast_{F(p)}N \to T^\ast_pM$, $(F^\ast_p\alpha)(v) = \alpha(F_{\ast p}v)$, the dual map of $F_{\ast p}$, see Definition [[§34 The Cotangent Space from Germs#^def-34-3|§34.3]]. *Source: Lecture 15.*

^nd-def-34-3

- [ ] Q1 **[def]** Define $F^\ast_p$ on covectors; in which direction does it go and why?
- [ ] Q2 **[use]** Prove $F^\ast_p(df_{F(p)}) = d(f \circ F)_p$.
- [ ] Q3 **[why]** $F_{\ast p}$ injective iff $F^\ast_p$ surjective, and $F_{\ast p}$ surjective iff $F^\ast_p$ injective. Why? Restate "immersion" and "submersion" with $F^\ast_p$.
- [ ] Q4 **[use]** How is $F^\ast_p$ on covectors induced by the pullback of germs on $I_q/I_q^2$?

> [!tip]- Hints: where it lives, examples
> - Definition [[§21 Linear Algebra Toolkit#^def-21-3|§21.3]], Definition [[§34 The Cotangent Space from Germs#^def-34-3|§34.3]]; the remark *One Symbol for Two Pullbacks* in [[§34 The Cotangent Space from Germs|§34]].
> - Q2: Proposition [[§34 The Cotangent Space from Germs#^prop-34-6|§34.6]]. Q3: Proposition [[§21 Linear Algebra Toolkit#^prop-21-4|§21.4]] (part 3). Q4: Proposition [[§34 The Cotangent Space from Germs#^prop-34-7|§34.7]].

## Proofs T5

### Priority 1 · homework (directly or extended)

#### The cotangent space from germs (the pairing and the isomorphism) · P1

Theorem [[§34 The Cotangent Space from Germs#^thm-34-4|§34.4]] and Proposition [[§34 The Cotangent Space from Germs#^prop-34-3|§34.3]] (with the key step Proposition [[§34 The Cotangent Space from Germs#^prop-34-1|§34.1]], (3) ⇒ (1)) → drilled as [[Differentiable Manifolds HW Drill#^hw3-3|HW3.3]].

#### A basis of $I_p/I_p^2$; the dimension of $T_p^\ast M$ · P1

For $[f] \in I_p$, ${[}[f]{]} = \sum_i \frac{\partial f}{\partial x^i}(p)\, {[}[x^i - x^i(p)]{]}$, and these classes form a basis of $I_p/I_p^2$ (Proposition [[§34 The Cotangent Space from Germs#^prop-34-2|§34.2]]); so $\dim T_p^\ast M = \dim I_p/I_p^2 = \dim T_pM = m$ (Theorem [[§34 The Cotangent Space from Germs#^thm-34-5|§34.5]]). *Source: notes (Assignment 3 material).*

^nd-prop-34-2

- [ ] Q1 **[def]** Define $I_p/I_p^2$ (Definition [[§34 The Cotangent Space from Germs#^def-34-1|§34.1]]).
- [ ] Q2 **[state]** State the proposition.
- [ ] Q3 Expansion: given $[f] \in I_p$, why does $g = f - \sum_i c_i(x^i - x^i(p))$, $c_i = \partial f/\partial x^i(p)$, lie in $I_p^2$? Which proposition do you use?
- [ ] Q4 Independence: if $\sum_i c_i {[}[x^i - x^i(p)]{]} = 0$, why is every $c_j = 0$?
- [ ] Q5 **[why]** Why do you need Hadamard's lemma (and not only Taylor's theorem with remainder) to know that a germ with vanishing value and first partials lies in $I_p^2$?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S9.
> - $\partial(x^i - x^i(p))/\partial x^j(p) = \delta^i_j$; Proposition [[§34 The Cotangent Space from Germs#^prop-34-1|§34.1]] (3) ⇒ (1) and (1) ⇒ (3).
> - Theorem [[§34 The Cotangent Space from Germs#^thm-34-5|§34.5]]: also via the isomorphism $\Phi$ of Theorem [[§34 The Cotangent Space from Germs#^thm-34-4|§34.4]].

### Priority 2 · stated or done in class

#### The differential of a function evaluates derivations · P2

$df_p(D) = D[f]$; in particular $df_p(\partial/\partial x^j|_p) = \partial f/\partial x^j(p)$ (Proposition [[§32 The Cotangent Space#^prop-32-2|§32.2]]); hence $d$ is linear, satisfies the product rule $d(fg)_p = f(p)\,dg_p + g(p)\,df_p$ and the chain rule $d(h \circ f)_p = h'(f(p))\,df_p$ (Corollary [[§32 The Cotangent Space#^cor-32-3|§32.3]]). *Source: Lecture 10 (the cotangent space and $df_p$); the properties filled in.*

^nd-prop-32-2

- [ ] Q1 **[def]** Define $T_p^\ast M$ and $df_p$ (Definition [[§32 The Cotangent Space#^def-32-4|§32.4]], Definition [[§32 The Cotangent Space#^def-32-5|§32.5]]). What is the identification $T_{f(p)}\mathbb{R} \cong \mathbb{R}$ (Proposition [[§32 The Cotangent Space#^prop-32-1|§32.1]])?
- [ ] Q2 **[state]** State the proposition and the three properties.
- [ ] Q3 Prove $df_p(D) = D[f]$ by unwinding the definitions ($r \circ f = f$).
- [ ] Q4 Prove the product rule for $d$: evaluate both sides on an arbitrary $D$.
- [ ] Q5 **[why]** Why is $dc_p = 0$ for a constant $c$? Why does $df_p$ need $f$ only near $p$?

> [!tip]- Hints: route of the proof in the notes
> - $df_p(D) = (f_{\ast p}D)[r] = D[r \circ f]$.
> - Equalities in a dual space are checked on every $D$; then linearity and Leibniz of $D$.

#### The differential in coordinates · P2

In a chart, $\{dx^i|_p\}$ is the basis dual to $\{\partial/\partial x^i|_p\}$, so $\dim T_p^\ast M = m$, and $df_p = \sum_i \frac{\partial f}{\partial x^i}(p)\, dx^i|_p$, see Lemma [[§33 Covectors in Coordinates#^lem-33-1|§33.1]]; every covector is $\xi = \sum_j \xi(\partial/\partial x^j|_p)\, dx^j|_p$ (Corollary [[§33 Covectors in Coordinates#^cor-33-2|§33.2]]). *Source: Lecture 10 ("it suffices to check the identity on basis vectors"); Lecture 15.*

^nd-lem-33-1

- [ ] Q1 **[def]** Define the dual basis (Definition [[§21 Linear Algebra Toolkit#^def-21-2|§21.2]]) and the components of a covector (Definition [[§33 Covectors in Coordinates#^def-33-1|§33.1]]).
- [ ] Q2 **[state]** State the lemma and the corollary.
- [ ] Q3 Compute $dx^i|_p(\partial/\partial x^j|_p)$.
- [ ] Q4 Prove the formula for $df_p$ by evaluating both sides on the basis vectors $\partial/\partial x^j|_p$.
- [ ] Q5 Why are the components of $\xi$ unique?
- [ ] Q6 **[why]** In lecture a student first proposed an $m \times 1$ matrix for $f_{\ast p}$: why is it a $1 \times m$ row ("gradients are across")? How do the components of $df_p$ change under a change of chart (compare Corollary [[§30 The Differential in Coordinates#^cor-30-4|§30.4]])?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S9, S7 (linear functionals agreeing on a basis are equal).
> - $dx^i|_p(\partial/\partial x^j|_p) = \partial r^i/\partial r^j = \delta^i_j$; dual basis by Proposition [[§21 Linear Algebra Toolkit#^prop-21-2|§21.2]].
> - $df_p(\partial/\partial x^j|_p) = \partial f/\partial x^j(p)$ (Proposition [[§32 The Cotangent Space#^prop-32-2|§32.2]]).

#### Vectors as covectors through the dot product · P2

On open $U \subseteq \mathbb{R}^n$, $\xi_v(D_w|_p) = v \cdot w$ defines an isomorphism $\mathbb{R}^n \cong T_p^\ast U$ with $\xi_v = \sum_i v^i dr^i|_p$, and $\xi_{\nabla h(p)} = dh_p$, see Proposition [[§33 Covectors in Coordinates#^prop-33-3|§33.3]]. *Source: notes (filled in).*

^nd-prop-33-3

- [ ] Q1 **[def]** Define the gradient (Definition [[§33 Covectors in Coordinates#^def-33-2|§33.2]]).
- [ ] Q2 **[state]** State the three parts.
- [ ] Q3 Why is $\xi_v$ a covector, and why is $v \mapsto \xi_v$ an isomorphism?
- [ ] Q4 Show $dh_p(D_w|_p) = \nabla h(p) \cdot w$.
- [ ] Q5 **[why]** Which extra structure (the dot product) does this identification use? Why is there no such identification $T_pM \cong T_p^\ast M$ on a bare manifold?

> [!tip]- Hints: route of the proof in the notes
> - $D_w|_p = \sum_i w^i \partial/\partial r^i|_p$, so $\xi_v(\partial/\partial r^i|_p) = v^i$.
> - $dh_p(D_w|_p) = D_w|_p[h] = \sum_i w^i\, \partial_i h(p)$.

#### Pullback commutes with $d$ · P2

For $F : M \to N$ smooth and $f$ smooth near $F(p)$: $F_p^\ast(df_{F(p)}) = d(f \circ F)_p$, see Proposition [[§34 The Cotangent Space from Germs#^prop-34-6|§34.6]]. *Source: Lecture 15 ("every equal sign is a definition").*

^nd-prop-34-6

- [ ] Q1 **[def]** Define the pullback of covectors $F_p^\ast$ (Definition [[§34 The Cotangent Space from Germs#^def-34-3|§34.3]]).
- [ ] Q2 **[state]** State the proposition.
- [ ] Q3 Evaluate both sides on $v \in T_pM$ and justify each of the four equalities by a definition.
- [ ] Q4 **[why]** Why do covectors (like functions) move backwards along $F$? Use the proposition to show $F_p^\ast(dy^j|_{F(p)}) = dF^j_p = \sum_i \frac{\partial F^j}{\partial x^i}(p)\, dx^i|_p$.

> [!tip]- Hints: route of the proof in the notes
> - $F_p^\ast(df)(v) = df(F_{\ast p}v) = (F_{\ast p}v)[f] = v[f \circ F] = d(f \circ F)_p(v)$.

#### Pullback of covectors from the pullback of germs · P2

$F_p^\ast$ on germs maps $I_q \to I_p$ and $I_q^2 \to I_p^2$, hence induces $\bar F_p^\ast : I_q/I_q^2 \to I_p/I_p^2$, which under $\Phi$ is the pullback of covectors, see Proposition [[§34 The Cotangent Space from Germs#^prop-34-7|§34.7]]. *Source: notes (filled in).*

^nd-prop-34-7

- [ ] Q1 **[state]** State the proposition with its commutative square.
- [ ] Q2 Why does $F_p^\ast$ map $I_q^2$ into $I_p^2$?
- [ ] Q3 How does the universal property of quotient spaces (Proposition [[§21 Linear Algebra Toolkit#^prop-21-6|§21.6]]) give $\bar F_p^\ast$?
- [ ] Q4 Check the square on a class ${[}[g]{]}$.
- [ ] Q5 **[why]** Why does this show the germ picture of $T_p^\ast M$ is natural (no chart needed anywhere)?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S2.
> - $F_p^\ast$ is an algebra homomorphism with $F_p^\ast(I_q) \subseteq I_p$ (Proposition [[§28 Derivations and the Abstract Tangent Space#^prop-28-4|§28.4]]).
> - $\Phi_p{[}[g \circ F]{]} = d(g \circ F)_p = F_p^\ast(dg_q)$ by Proposition [[§34 The Cotangent Space from Germs#^prop-34-6|§34.6]].

# T6. Local diffeomorphisms and submersions

## Definitions T6

### Priority 2 · stated or done in class

#### Local diffeomorphism · P2

Every $p$ has neighbourhoods $U \ni p$, $V = F(U) \ni F(p)$ such that $F|_U : U \to V$ has a smooth inverse, see Definition [[§35 Local Diffeomorphisms#^def-35-1|§35.1]]. *Source: Lecture 10.*

^nd-def-35-1

- [ ] Q1 **[def]** State the definition, including what a local inverse is.
- [ ] Q2 **[example]** Why is $t \mapsto (\cos t, \sin t)$, $\mathbb{R} \to S^1$, a local diffeomorphism? Is it injective?
- [ ] Q3 **[use]** State the criterion by the differential, and the characterization of diffeomorphisms among local diffeomorphisms.
- [ ] Q4 **[why]** $t \mapsto t^3$ is a smooth homeomorphism of $\mathbb{R}$. Why is it not a local diffeomorphism, and where does the criterion fail?
- [ ] Q5 **[why]** Is a local diffeomorphism an open map? Is a bijective local diffeomorphism a diffeomorphism? Is an injective one?

> [!tip]- Hints: where it lives, examples
> - Definition [[§35 Local Diffeomorphisms#^def-35-1|§35.1]]; Example [[§35 Local Diffeomorphisms#^ex-35-1|§35.1]]; the remark *Covering Maps* in [[§35 Local Diffeomorphisms|§35]].
> - Q3: Theorem [[§35 Local Diffeomorphisms#^thm-35-2|§35.2]] (from the inverse function theorem, Theorem [[§35 Local Diffeomorphisms#^thm-35-1|§35.1]], quoted), Corollary [[§35 Local Diffeomorphisms#^cor-35-3|§35.3]].
> - Q4: $F_{\ast 0} = 0$. Q5: yes (locally a diffeomorphism onto an open set), yes (Corollary [[§35 Local Diffeomorphisms#^cor-35-3|§35.3]]), yes onto its open image.

#### Submersion · P2

$F$ is a submersion at $p$ if $F_{\ast p}$ is onto, and a submersion if it is one at every point, see Definition [[§36 Submersions#^def-36-1|§36.1]]. *Source: Lecture 10.*

^nd-def-36-1

- [ ] Q1 **[def]** State the definition; which dimension inequality does it force?
- [ ] Q2 **[example]** Why are projections $M_1 \times M_2 \to M_1$ submersions? Why is every fibration a submersion?
- [ ] Q3 **[use]** State the local normal form for submersions. What does it require at $p$ only, and what does it then give near $p$?
- [ ] Q4 **[why]** Drop "at every point": is $f(x) = x^2$ a submersion? At which points? Is $f$ open?
- [ ] Q5 **[why]** True or false: there is a submersion from $S^2$ to $\mathbb{R}$. Which property of submersions decides it?

> [!tip]- Hints: where it lives, examples
> - Definition [[§36 Submersions#^def-36-1|§36.1]]; Example [[§36 Submersions#^ex-36-1|§36.1]], Example [[§36 Submersions#^ex-36-2|§36.2]], Proposition [[§38 Fibrations#^prop-38-1|§38.1]] (part 2).
> - Q3: Theorem [[§36 Submersions#^thm-36-6|§36.6]]; Corollary [[§36 Submersions#^cor-36-7|§36.7]], Corollary [[§36 Submersions#^cor-36-9|§36.9]] (open: "locally they are projections").
> - Q4: $0$ is critical; $f(\mathbb{R}) = [0, \infty)$ is not open. Q5: Theorem [[§36 Submersions#^thm-36-10|§36.10]], Corollary [[§36 Submersions#^cor-36-11|§36.11]] → drilled as [[Differentiable Manifolds HW Drill#^hw4-2|HW4.2]].
> - Also: for $G : M \to \mathbb{R}^k$, submersion at $p$ iff the $dG^j|_p$ are independent, Proposition [[§36 Submersions#^prop-36-4|§36.4]].

#### Immersion · P2

$F$ is an immersion at $p$ if $F_{\ast p}$ is injective, and an immersion if it is one at every point, see Definition [[§36 Submersions#^def-36-2|§36.2]]. *Source: Lectures 10, 13.*

^nd-def-36-2

- [ ] Q1 **[def]** State the definition; which dimension inequality does it force?
- [ ] Q2 **[example]** Give an immersion $\mathbb{R} \to \mathbb{R}^2$ that is not injective, and an injective immersion that is not a homeomorphism onto its image.
- [ ] Q3 **[why]** Is $t \mapsto (t^2, t^3)$ an immersion? Is it injective? Is its image a submanifold?
- [ ] Q4 **[use]** State the local normal form for immersions.
- [ ] Q5 **[why]** Is an immersion with $\dim M = \dim N$ a local diffeomorphism? Why?

> [!tip]- Hints: where it lives, examples
> - Definition [[§36 Submersions#^def-36-2|§36.2]] (= Definition [[§41 Immersions#^def-41-1|§41.1]]); Proposition [[§36 Submersions#^prop-36-1|§36.1]].
> - Q2: Example [[§41 Immersions#^ex-41-1|§41.1]], Example [[§41 Immersions#^ex-41-2|§41.2]]. Q3: injective, not an immersion at $0$ (velocity $0$); the image is the cusp.
> - Q4: Theorem [[§41 Immersions#^thm-41-1|§41.1]]. Q5: Proposition [[§36 Submersions#^prop-36-1|§36.1]] (part 3).

#### Regular point and critical point (manifolds) · P2

$p$ is a regular point of $F : M \to N$ if $F_{\ast p}$ is onto; otherwise critical, see Definition [[§36 Submersions#^def-36-3|§36.3]]. *Source: Lecture 11.*

^nd-def-36-3

- [ ] Q1 **[def]** State the definition; why does a regular point force $\dim N \le \dim M$?
- [ ] Q2 **[use]** For $f : M \to \mathbb{R}$, show $p$ is critical iff $df_p = 0$ iff all $\partial f/\partial x^i(p) = 0$.
- [ ] Q3 **[why]** If $\dim M < \dim N$, which points are regular?
- [ ] Q4 **[example]** Why is a local maximum of $f$ a critical point? Why is the set of critical points of $f$ closed?

> [!tip]- Hints: where it lives, examples
> - Definition [[§30 The Differential in Coordinates#^def-30-3|§30.3]], Definition [[§36 Submersions#^def-36-3|§36.3]]; Q2: Proposition [[§36 Submersions#^prop-36-2|§36.2]] ($df_p$ is onto or zero).
> - Q3: none. Q4: Proposition [[§36 Submersions#^prop-36-3|§36.3]], Corollary [[§36 Submersions#^cor-36-8|§36.8]], Definition [[§36 Submersions#^def-36-5|§36.5]].

#### Regular value and critical value (manifolds) · P2

$q \in N$ is a regular value of $F$ if $F$ is a submersion at every $p \in F^{-1}(q)$; every $q \notin F(M)$ is regular, see Definition [[§36 Submersions#^def-36-4|§36.4]]. *Source: Lecture 11.*

^nd-def-36-4

- [ ] Q1 **[def]** State the definition, with the empty-preimage convention.
- [ ] Q2 **[use]** State the regular value theorem for manifolds, including the tangent space of the level set.
- [ ] Q3 **[why]** Can a critical value have a level set that is a manifold? Give an example on $\mathbb{R}^2$, and explain why the theorem is only an implication.
- [ ] Q4 **[why]** If $\dim M < \dim N$, which values are regular, and what does the theorem then say?
- [ ] Q5 **[example]** For the height function on $S^2$, find the critical values.

> [!tip]- Hints: where it lives, examples
> - Definition [[§30 The Differential in Coordinates#^def-30-4|§30.4]], Definition [[§36 Submersions#^def-36-4|§36.4]]; Q2: Theorem [[§37 Regular Submanifolds#^thm-37-12|§37.12]].
> - Q3: $f(x, y) = y^2$ on $\mathbb{R}^2$: $0$ is critical, yet $f^{-1}(0)$ is the $x$-axis, a submanifold (not in the notes).
> - Q4: exactly the values not attained; the preimage is empty. Q5: $\pm 1$ (the poles).

#### Critical set · P2

$\operatorname{Crit}(f) = \{p : df_p = 0\}$ for $f : M \to \mathbb{R}$, see Definition [[§36 Submersions#^def-36-5|§36.5]]. *Source: Lecture 11.*

^nd-def-36-5

- [ ] Q1 **[def]** Define $\operatorname{Crit}(f)$ and relate it to critical points in the sense of submersions.
- [ ] Q2 **[why]** Why is $\operatorname{Crit}(f)$ closed?
- [ ] Q3 **[use]** Where do critical points of $f$ sit in $T^\ast M$ (in terms of $df$ and the zero section)?

> [!tip]- Hints: where it lives, examples
> - Definition [[§36 Submersions#^def-36-5|§36.5]]; Proposition [[§36 Submersions#^prop-36-2|§36.2]]; Q2: Corollary [[§36 Submersions#^cor-36-8|§36.8]] (the regular points form an open set, Corollary [[§36 Submersions#^cor-36-7|§36.7]]).
> - Q3: $p \in \operatorname{Crit}(f)$ iff $df(p)$ lies on the zero section, Theorem [[§52 Critical Points and the Hessian#^thm-52-10|§52.10]].

## Proofs T6

### Priority 1 · homework (directly or extended)

#### Critical points of real-valued functions; local extrema · P1

For $f : M \to \mathbb{R}$, $df_p$ is onto or zero, so $p$ is critical iff $df_p = 0$ iff all $\partial f/\partial x^i(p) = 0$ (Proposition [[§36 Submersions#^prop-36-2|§36.2]]); local extrema are critical points (Proposition [[§36 Submersions#^prop-36-3|§36.3]]); $\mathrm{Crit}(f)$ is closed (Corollary [[§36 Submersions#^cor-36-8|§36.8]]). *Source: notes (the extremum argument is the one of [[Differentiable Manifolds HW Drill#^hw5-4-b|HW5.4(b)]]).*

^nd-prop-36-2

- [ ] Q1 **[def]** Define regular and critical points and the critical set (Definition [[§36 Submersions#^def-36-3|§36.3]], Definition [[§36 Submersions#^def-36-5|§36.5]]).
- [ ] Q2 **[state]** State the three results.
- [ ] Q3 Why is $df_p$ either onto or $0$ ("dimensions of images cannot be fractional")?
- [ ] Q4 Local extremum: for $v \in T_pM$ pick a curve with $D_\gamma = v$. Why is $(f \circ \gamma)'(0) = 0$, and why is that $df_p(v)$?
- [ ] Q5 Critical set closed: which corollary shows the complement is open?
- [ ] Q6 **[why]** Is the converse of the extremum statement true? ($x^3$ at $0$.) Why does the extremum argument need $p$ to be an interior point of a manifold without boundary?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S10 (curves), S7.
> - Image of $df_p$ is a subspace of $\mathbb{R}$; Lemma [[§33 Covectors in Coordinates#^lem-33-1|§33.1]] for the coordinate form.
> - Every vector is a velocity (Theorem [[§31 Tangent Vectors as Velocities of Curves#^thm-31-2|§31.2]]); one-variable calculus.
> - Corollary [[§36 Submersions#^cor-36-7|§36.7]] applied at regular points.

#### Submersions to $\mathbb{R}^k$ and independent differentials · P1

For $G = (G^1, \ldots, G^k) : M \to \mathbb{R}^k$: $G_{\ast p}v = \sum_j dG^j_p(v)\, \partial/\partial r^j$, and $G$ is a submersion at $p$ iff $dG^1_p, \ldots, dG^k_p$ are linearly independent, see Proposition [[§36 Submersions#^prop-36-4|§36.4]]. *Source: notes ([[Differentiable Manifolds HW Drill#^hw5-4-b|HW5.4(b)]] at a point of a level set).*

^nd-prop-36-4

- [ ] Q1 **[state]** State both parts.
- [ ] Q2 (1): compute the coefficients $(G_{\ast p}v)[r^j]$.
- [ ] Q3 (2) ⇒: given $\sum_j c_j dG^j_p = 0$, choose $v$ with $G_{\ast p}v = \sum_j c_j \partial/\partial r^j$ and conclude $|c|^2 = 0$.
- [ ] Q4 (2) ⇐: if the image of $G_{\ast p}$ is a proper subspace, find a nonzero $c$ orthogonal to it; what relation among the $dG^j_p$ results?
- [ ] Q5 **[why]** Two regular values $a$ of $f$ and $b$ of $g$ do not make $(a,b)$ a regular value of $(f,g)$: give an example where $df_p$ and $dg_p$ are dependent (2021 exam, Part 2.6).

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S7 (linear algebra), S9.
> - $(G_{\ast p}v)[r^j] = v[G^j] = dG^j_p(v)$.
> - Equivalently: the Jacobian has rank $k$ iff its rows (the $dG^j_p$) are independent.

#### Submersions from compact manifolds · P1

If $M$ is compact and nonempty, $N$ connected and $F : M \to N$ a submersion, then $F$ is surjective and $N$ is compact, see Theorem [[§36 Submersions#^thm-36-10|§36.10]]. *Source: the generalization of Assignment 4, Problem 2; the core argument is drilled as [[Differentiable Manifolds HW Drill#^hw4-2|HW4.2]] (and Corollary [[§36 Submersions#^cor-36-11|§36.11]] → [[Differentiable Manifolds HW Drill#^hw4-2|HW4.2]]).*

^nd-thm-36-10

- [ ] Q1 **[state]** State the theorem, all hypotheses.
- [ ] Q2 Which three properties of $F(M) \subseteq N$ do you prove, and with which results?
- [ ] Q3 **[why]** Drop "connected": give a submersion from a compact manifold that is not surjective. Drop "compact": give a non-surjective submersion to a connected $N$.
- [ ] Q4 **[why]** True or false, with proof or counterexample: (a) every submersion $S^1 \to S^1$ is surjective; (b) every submersion $S^1 \to S^1$ is a diffeomorphism (think of $z \mapsto z^2$).

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S13 (compactness: closed image), S13′ (connectedness: clopen).
> - Open: Corollary [[§36 Submersions#^cor-36-9|§36.9]]; closed: compact in Hausdorff; nonempty.

### Priority 2 · stated or done in class

#### Inverse function theorem (quoted) · P2

If $\Phi : W \subseteq \mathbb{R}^n \to \mathbb{R}^n$ is smooth and $\Phi'(a)$ is invertible, then $\Phi$ maps an open $U_0 \ni a$ bijectively onto an open $V_0 \ni \Phi(a)$ with smooth inverse, see Theorem [[§35 Local Diffeomorphisms#^thm-35-1|§35.1]]. *Source: analysis; not proved in the course (proof "to be filled"): quote it.*

^nd-thm-35-1

- [ ] Q1 **[state]** State the theorem precisely: hypotheses, and what "local" means in the conclusion.
- [ ] Q2 **[why]** Why is the conclusion only local? Give a smooth $\Phi : \mathbb{R}^2 \to \mathbb{R}^2$ with $\Phi'$ invertible everywhere that is not injective ($e^x(\cos y, \sin y)$).
- [ ] Q3 **[why]** Why is invertibility of $\Phi'(a)$ needed? Consider $x \mapsto x^3$ at $0$: it is a smooth bijection; why is it not a diffeomorphism?
- [ ] Q4 How is it used: in the regular value theorem (via the implicit function theorem, Theorem [[§7 The Regular Value Theorem#^thm-7-1|§7.1]]), in Theorem [[§35 Local Diffeomorphisms#^thm-35-2|§35.2]], and in the submersion normal form (step 8)?

> [!tip]- Hints: what to know
> - Quote, do not prove (Lee, Theorem C.34).
> - The implicit function theorem follows by applying it to $(x,y) \mapsto (x, \Phi(x,y))$.

#### Local diffeomorphisms are detected by the differential · P2

A smooth $F : M \to N$ is a local diffeomorphism iff $F_{\ast p}$ is bijective for every $p$, see Theorem [[§35 Local Diffeomorphisms#^thm-35-2|§35.2]]. *Source: Lecture 10 (the forward direction from a student; for the converse "the inverse function theorem is really what's paying the bills").*

^nd-thm-35-2

- [ ] Q1 **[def]** Define a local diffeomorphism (Definition [[§35 Local Diffeomorphisms#^def-35-1|§35.1]]).
- [ ] Q2 **[state]** State the theorem.
- [ ] Q3 (⇒): with a local inverse $G$, apply the chain rule to $G \circ F|_U = \mathrm{id}_U$ and $F|_U \circ G = \mathrm{id}_V$. Why is $(F|_U)_{\ast p}$ the same as $F_{\ast p}$?
- [ ] Q4 (⇐): choose charts with $F(U) \subseteq V$. Why is $\dim M = \dim N$, and why is $\tilde F'(\varphi(p))$ invertible?
- [ ] Q5 Apply the inverse function theorem to $\tilde F$ and pull the local inverse back up: what is the local inverse of $F$?
- [ ] Q6 **[why]** A local diffeomorphism need not be injective or a diffeomorphism: give Example [[§35 Local Diffeomorphisms#^ex-35-1|§35.1]]. Where does the 2021 exam item on a nonsingular $dF_p$ with image in a half-space fit (local diffeomorphisms are open maps)?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S1 (charts), then the inverse function theorem.
> - (⇒) $G_\ast \circ F_\ast = \mathrm{id}$ and $F_\ast \circ G_\ast = \mathrm{id}$; $T_pU = T_pM$ (Lemma [[§28 Derivations and the Abstract Tangent Space#^lem-28-8|§28.8]]).
> - (⇐) Matrix of $F_{\ast p}$ is $\tilde F'(\varphi(p))$ (Theorem [[§30 The Differential in Coordinates#^thm-30-2|§30.2]]); local inverse $\varphi^{-1} \circ (\tilde F|_{\tilde A})^{-1} \circ \psi|_{V'}$.

#### Diffeomorphisms are the bijective local diffeomorphisms · P2

$F$ is a diffeomorphism iff it is a bijective local diffeomorphism; so a smooth bijection with every $F_{\ast p}$ bijective is a diffeomorphism, see Corollary [[§35 Local Diffeomorphisms#^cor-35-3|§35.3]]. *Source: notes.*

^nd-cor-35-3

- [ ] Q1 **[state]** State the corollary.
- [ ] Q2 (⇐): given $q \in N$, why does $F^{-1}$ agree near $q$ with a local inverse $G$? Which hypothesis is used?
- [ ] Q3 Why do "continuous" and "smooth" for $F^{-1}$ follow from agreeing locally with smooth maps?
- [ ] Q4 Deduce the last sentence from Theorem [[§35 Local Diffeomorphisms#^thm-35-2|§35.2]].
- [ ] Q5 **[why]** Why is "smooth bijection" not enough? (The cube map $\mathbb{R} \to \mathbb{R}$, $x \mapsto x^3$.)

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S11 (local, then global).
> - $F(G(y)) = y = F(F^{-1}(y))$ and injectivity give $G = F^{-1}$ on $V$.

#### The circle covered by a line · P2

$F(t) = (\cos t, \sin t)$, $\mathbb{R} \to S^1$, is a local diffeomorphism (also on $(0, 4\pi)$), but not injective, see Example [[§35 Local Diffeomorphisms#^ex-35-1|§35.1]]. *Source: Lecture 10 (stated without proof); filled in.*

^nd-ex-35-1

- [ ] Q1 **[state]** State what the example shows.
- [ ] Q2 Why is $F$ smooth *into $S^1$* (Lemma [[§20 Manifolds in Euclidean Space#^lem-20-3|§20.3]])?
- [ ] Q3 For $t_0$, which neighbourhoods $U = (t_0 - \pi, t_0 + \pi)$ and $V$ make $F|_U : U \to V$ bijective? Which chart of $S^1$ is the inverse?
- [ ] Q4 Shorter route: compute $F_{\ast t}$ by curves and apply Theorem [[§35 Local Diffeomorphisms#^thm-35-2|§35.2]].
- [ ] Q5 **[why]** Why is the restriction to $(0, 4\pi)$ a local diffeomorphism that is not a covering map? What does this say about "local diffeomorphism + surjective ⇒ diffeomorphism"?

> [!tip]- Hints: route of the proof in the notes
> - $F(t) = F(t') \iff t - t' \in 2\pi\mathbb{Z}$.
> - $V = S^1 \setminus \{F(t_0 + \pi)\}$; the inverse is an angle chart (Proposition [[§24 The Circle#^prop-24-1|§24.1]]).

#### Dimension constraints · P2

If $F$ is a submersion at $p$ then $n \le m$, an immersion then $m \le n$; $F$ is a local diffeomorphism iff it is both; if $m = n$, either alone gives a local diffeomorphism, see Proposition [[§36 Submersions#^prop-36-1|§36.1]]. *Source: notes.*

^nd-prop-36-1

- [ ] Q1 **[def]** Define submersion and immersion (Definition [[§36 Submersions#^def-36-1|§36.1]], Definition [[§36 Submersions#^def-36-2|§36.2]]).
- [ ] Q2 **[state]** State the three parts.
- [ ] Q3 Prove (1) by rank–nullity.
- [ ] Q4 Prove (2) and (3) from Theorem [[§35 Local Diffeomorphisms#^thm-35-2|§35.2]].
- [ ] Q5 **[why]** Give a submersion that is not a local diffeomorphism and an immersion that is not one (projections; the inclusion of $S^1$ in $\mathbb{R}^2$).

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S7.
> - $m = \dim\ker F_{\ast p} + \operatorname{rank} F_{\ast p}$; equal dimensions: injective ⇔ surjective.

#### Local normal form for submersions · P2

If $F : M^m \to N^n$ is a submersion at $p$, there are charts $(U, \varphi)$ at $p$, $(V, \psi)$ at $F(p)$, $F(U) \subseteq V$, with $\psi \circ F \circ \varphi^{-1}(r^1, \ldots, r^m) = (r^1, \ldots, r^n)$, see Theorem [[§36 Submersions#^thm-36-6|§36.6]]; diffeomorphisms onto open sets are charts (Lemma [[§36 Submersions#^lem-36-5|§36.5]]). *Source: stated Lecture 10, proved Lecture 11.*

^nd-thm-36-6

- [ ] Q1 **[state]** State the theorem, in both forms ($\tilde F$ is a projection; $y^j \circ F = x^j$ for $j \le n$).
- [ ] Q2 Start with any charts with $F(U_0) \subseteq V$. What is the matrix $J = [\partial F^j/\partial x^i(p)]$, and why does it have rank $n$?
- [ ] Q3 Reindex so that $J = (A \mid B)$ with $A$ invertible. Why is the reindexed chart still a smooth chart?
- [ ] Q4 Define the new coordinates $\hat\varphi = (F^1, \ldots, F^n, x^{n+1}, \ldots, x^m)$. Compute its Jacobian in the old coordinates and its determinant.
- [ ] Q5 Why is $\hat\varphi$, after shrinking, a smooth chart (inverse function theorem, then Lemma [[§36 Submersions#^lem-36-5|§36.5]])?
- [ ] Q6 Compute $\psi \circ F \circ \hat\varphi^{-1}$: why is its $i$-th component $r^i$ for $i \le n$?
- [ ] Q7 **[why]** Why is the normal form only *local*? Which chart was changed and which kept? What does the theorem give for the fibres $F^{-1}(c)$ (Theorem [[§37 Regular Submanifolds#^thm-37-12|§37.12]])?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S8 (normal forms give charts).
> - $J$ is the matrix of $F_{\ast p}$ (Theorem [[§30 The Differential in Coordinates#^thm-30-2|§30.2]]), rank $n$ since $F_{\ast p}$ is onto.
> - Jacobian $\begin{pmatrix} A & B \\ 0 & I_{m-n} \end{pmatrix}$, determinant $\det A \neq 0$.
> - $F^i(\hat\varphi^{-1}(r)) = r^i$ by definition of $\hat\varphi$; $\psi$ unchanged.

#### Submersions are open maps · P2

A submersion maps open sets to open sets, see Corollary [[§36 Submersions#^cor-36-9|§36.9]]. *Source: notes; stressed in lecture: open "because locally they are projections".*

^nd-cor-36-9

- [ ] Q1 **[state]** State the corollary; what has to be shown for an open $W$?
- [ ] Q2 For $q = F(p)$, $p \in W$: shrink the normal-form chart to $U \cap W$. Why is it still a chart in which $F$ is the projection?
- [ ] Q3 Show $F(U) = \psi^{-1}(\mathrm{pr}(\varphi(U)))$. Why is this open?
- [ ] Q4 **[why]** Is a submersion a closed map? Give an example (the projection $\mathbb{R}^2 \to \mathbb{R}$ and the hyperbola $xy = 1$).

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S8.
> - Projections are open (Example [[§4 Quotient Spaces and Open Maps#^ex-4-2|§4.2]]); $\psi^{-1}$ maps open subsets of $\psi(V)$ to open subsets of $V$.

### Priority 4 · notes only (optional before the midterm)

#### Being a submersion is an open condition · P4

If $F$ is a submersion at $p$, it is a submersion on a neighbourhood of $p$, see Corollary [[§36 Submersions#^cor-36-7|§36.7]]. *Source: notes (from the normal form).*

^nd-cor-36-7

- [ ] Q1 **[state]** State the corollary.
- [ ] Q2 In the normal-form charts, what is the Jacobian of $\tilde F$ at *every* point of $\varphi(U)$?
- [ ] Q3 Why does this give $F_{\ast q}$ onto for all $q \in U$?
- [ ] Q4 **[why]** Give a second proof via continuity: some $n \times n$ minor of the Jacobian is nonzero at $p$, hence near $p$. Is "being an immersion" also open? Is "being a local diffeomorphism at $p$"?

> [!tip]- Hints: route of the proof in the notes
> - $\tilde F'(r) = (I_n \mid 0)$ everywhere on $\varphi(U)$; Theorem [[§30 The Differential in Coordinates#^thm-30-2|§30.2]] at each $q \in U$.

# T7. Regular submanifolds and transversality

## Definitions T7

### Priority 1 · homework (directly or extended)

#### Codimension · P1

For a manifold $S \subseteq \mathbb{R}^k$ of dimension $s$, $\operatorname{codim} S = k - s$; for a regular submanifold, the number $k$ of defining equations, see Definition [[§26 Transversality#^def-26-1|§26.1]]. *Source: Assignment 2; Lecture 12.*

^nd-def-26-1

- [ ] Q1 **[def]** Define the codimension of $S \subseteq \mathbb{R}^k$ and of a regular submanifold $S \subseteq M$.
- [ ] Q2 **[use]** What happens to codimension under transverse preimages and transverse intersections?
- [ ] Q3 **[why]** Why is the codimension of $F^{-1}(S)$ the codimension of $S$, and not its dimension? Which spaces are isomorphic?
- [ ] Q4 **[example]** What is the codimension of $\{c\} \subseteq N$, and what does the transverse-preimage theorem then say?

> [!tip]- Hints: where it lives, examples
> - Definition [[§26 Transversality#^def-26-1|§26.1]], Definition [[§37 Regular Submanifolds#^def-37-2|§37.2]].
> - Q2: Theorem [[§26 Transversality#^thm-26-1|§26.1]], Proposition [[§26 Transversality#^prop-26-4|§26.4]], Theorem [[§37 Regular Submanifolds#^thm-37-15|§37.15]], Corollary [[§37 Regular Submanifolds#^cor-37-17|§37.17]].
> - Q3: Proposition [[§37 Regular Submanifolds#^prop-37-16|§37.16]] (the normal spaces are isomorphic). Q4: $\dim N$; Corollary [[§37 Regular Submanifolds#^cor-37-17|§37.17]] (part 1).

#### Transversality (Euclidean) · P1

$F \pitchfork S$ if $\operatorname{im} F'(p) + T^{\mathrm{geo}}_{F(p)}S = \mathbb{R}^k$ for every $p \in F^{-1}(S)$, see Definition [[§26 Transversality#^def-26-2|§26.2]]. *Source: Assignment 2, Problem 5.*

^nd-def-26-2

- [ ] Q1 **[def]** State the definition, with the set of points where it is imposed and the empty case.
- [ ] Q2 **[use]** With $S = G^{-1}(0)$, $0$ a regular value of $G$, show $F \pitchfork S$ iff $0$ is a regular value of $G \circ F$.
- [ ] Q3 **[why]** Let $S$ be the $x$-axis. For $F(t) = (t, 0)$ and $F(t) = (t, t^2)$, what goes wrong with the conclusions of the transverse-preimage theorem? Which conclusion fails in each?
- [ ] Q4 **[example]** For the sphere and the plane $z = c$, for which $c$ is the intersection transverse?

> [!tip]- Hints: where it lives, examples
> - Definition [[§26 Transversality#^def-26-2|§26.2]]; Q2: Proposition [[§26 Transversality#^prop-26-2|§26.2]] → drilled as [[Differentiable Manifolds HW Drill#^hw2-5|HW2.5]].
> - Q3: Example [[§26 Transversality#^ex-26-2|§26.2]] (dimension wrong; tangent formula wrong). Q4: Example [[§26 Transversality#^ex-26-1|§26.1]], Definition [[§26 Transversality#^def-26-3|§26.3]].

#### Transverse intersection · P1

Regular level sets $S_1, S_2 \subseteq \mathbb{R}^k$ intersect transversally if $T^{\mathrm{geo}}_qS_1 + T^{\mathrm{geo}}_qS_2 = \mathbb{R}^k$ at every $q \in S_1 \cap S_2$, see Definition [[§26 Transversality#^def-26-3|§26.3]]. *Source: Assignment 2.*

^nd-def-26-3

- [ ] Q1 **[def]** State the definition, Euclidean and for regular submanifolds $S, S' \subseteq N$.
- [ ] Q2 **[use]** Show it is the condition $\iota' \pitchfork S$, and that it is symmetric in $S$, $S'$.
- [ ] Q3 **[why]** Two curves in $\mathbb{R}^3$ meeting at a point: can they intersect transversally? What does the dimension count say?
- [ ] Q4 **[use]** What are the codimension and tangent space of a transverse intersection?

> [!tip]- Hints: where it lives, examples
> - Definition [[§26 Transversality#^def-26-3|§26.3]]; Corollary [[§37 Regular Submanifolds#^cor-37-17|§37.17]] (part 2), Proposition [[§26 Transversality#^prop-26-4|§26.4]].
> - Q3: no: $1 + 1 < 3$, so the sum of the tangent lines cannot be $\mathbb{R}^3$; only disjoint curves are transverse.

#### Transversality to a submanifold · P1

$F \pitchfork S$ if $F_{\ast p}(T_pM) + \iota_{\ast F(p)}(T_{F(p)}S) = T_{F(p)}N$ at every $p \in F^{-1}(S)$, see Definition [[§37 Regular Submanifolds#^def-37-5|§37.5]]. *Source: Assignment 5, Problem 2.*

^nd-def-37-5

- [ ] Q1 **[def]** State the definition, with the inclusion $\iota$ and where the sum is taken.
- [ ] Q2 **[why]** Why is the condition automatic at every $p$ where $F_{\ast p}$ is onto? Give an immersion $\mathbb{R} \to \mathbb{R}^2$ that is not transverse to the $x$-axis.
- [ ] Q3 **[why]** What does $F \pitchfork \{c\}$ mean? Why is transversality a generalization of "regular value"?
- [ ] Q4 **[use]** State the transverse-preimage theorem for manifolds, with the tangent space formula.
- [ ] Q5 **[example]** In $\mathbb{R}^2$, is the inclusion of the line $y = 1$ transverse to the unit circle? The line $y = \tfrac12$? What is the preimage in each case?

> [!tip]- Hints: where it lives, examples
> - Definition [[§37 Regular Submanifolds#^def-37-5|§37.5]]; Q2: Corollary [[§37 Regular Submanifolds#^cor-37-17|§37.17]] (part 3); Example [[§26 Transversality#^ex-26-2|§26.2]] (b), $t \mapsto (t, t^2)$.
> - Q3: Corollary [[§37 Regular Submanifolds#^cor-37-17|§37.17]] (part 1). Q4: Theorem [[§37 Regular Submanifolds#^thm-37-15|§37.15]] → drilled as [[Differentiable Manifolds HW Drill#^hw5-2|HW5.2]].
> - Q5: $y = 1$ is tangent at $(0, 1)$ (the tangent lines coincide), so not transverse; $y = \tfrac12$ meets in two points, transversally. Compare Example [[§26 Transversality#^ex-26-1|§26.1]].

### Priority 2 · stated or done in class

#### Regular submanifold · P2

$S \subseteq M$ (subspace topology) is a regular submanifold of codimension $k$ if every $p \in S$ lies in a smooth chart $(U, \varphi)$ of $M$ with $U \cap S = \{q \in U : x_b(q) = \vec 0\}$, $x_b$ the last $k$ coordinates, see Definition [[§37 Regular Submanifolds#^def-37-2|§37.2]]. *Source: Lecture 12.*

^nd-def-37-2

- [ ] Q1 **[def]** State the definition with all its data: dimension of $M$, codimension $k$, the topology on $S$, the chart condition.
- [ ] Q2 **[use]** Which smooth structure does $S$ get, and what is its dimension? What are its charts?
- [ ] Q3 **[why]** Drop "subspace topology" (allow any manifold topology on $S$ with an injective immersion): give a subset of $T^2$ that is an immersed submanifold but not a regular one. Why does the definition fail?
- [ ] Q4 **[why]** Is the figure-eight image in $\mathbb{R}^2$ a regular submanifold? Which point is the problem, and why?
- [ ] Q5 **[example]** Why is an open subset a regular submanifold of codimension $0$, and a regular level set $F^{-1}(q)$ one of codimension $\dim N$?

> [!tip]- Hints: where it lives, examples
> - Definition [[§37 Regular Submanifolds#^def-37-2|§37.2]]; Q2: Proposition [[§37 Regular Submanifolds#^prop-37-3|§37.3]] ($\varphi_S = x_a|_{U \cap S}$, dimension $m - k$).
> - Q3: Proposition [[§42 Embeddings#^prop-42-12|§42.12]], Example [[§42 Embeddings#^ex-42-1|§42.1]] (dense, so would be open, Corollary [[§42 Embeddings#^cor-42-8|§42.8]]). Q4: Example [[§42 Embeddings#^ex-42-1|§42.1]] (removing the origin leaves four components).
> - Q5: Proposition [[§37 Regular Submanifolds#^prop-37-4|§37.4]], Theorem [[§37 Regular Submanifolds#^thm-37-12|§37.12]]. Also: maps into $M$ with image in $S$ are smooth into $S$, Lemma [[§37 Regular Submanifolds#^lem-37-5|§37.5]].

#### Adapted chart · P2

A smooth chart $(U, \varphi)$ of $M$ with $U \cap S = \{x^{m-k+1} = \cdots = x^m = 0\}$, see Definition [[§37 Regular Submanifolds#^def-37-3|§37.3]]. *Source: Lecture 12.*

^nd-def-37-3

- [ ] Q1 **[def]** State the definition. Is every chart of $M$ at $p \in S$ adapted?
- [ ] Q2 **[use]** Show the value $\vec 0$ may be replaced by any constant and the last $k$ coordinates by any $k$ of them.
- [ ] Q3 **[use]** In an adapted chart, what is $\iota_{\ast p}(T_pS)$, and what is the conormal space?
- [ ] Q4 **[why]** Why does an adapted chart give a local defining map, i.e. why is $S$ locally a regular level set? Is the converse true?
- [ ] Q5 **[example]** Give a chart of $\mathbb{R}^2$ adapted to $S^1$ near $(1, 0)$.

> [!tip]- Hints: where it lives, examples
> - Definition [[§37 Regular Submanifolds#^def-37-3|§37.3]] ("a random chart of $M$ is not adapted"); Q2: Proposition [[§37 Regular Submanifolds#^prop-37-2|§37.2]].
> - Q3: Proposition [[§37 Regular Submanifolds#^prop-37-6|§37.6]], Proposition [[§37 Regular Submanifolds#^prop-37-8|§37.8]]. Q4: Proposition [[§37 Regular Submanifolds#^prop-37-7|§37.7]]; converse: Lemma [[§37 Regular Submanifolds#^lem-37-11|§37.11]] (part 2).
> - Q5: polar coordinates $(\theta, r - 1)$ on the slit plane, or the graph construction in the proof of Proposition [[§37 Regular Submanifolds#^prop-37-9|§37.9]].

#### Conormal space · P2

$N_pS = \{\xi \in T^\ast_pM : \xi = 0 \text{ on } \iota_{\ast p}(T_pS)\}$, the annihilator of $T_pS$, see Definition [[§37 Regular Submanifolds#^def-37-4|§37.4]]. *Source: Lecture 12.*

^nd-def-37-4

- [ ] Q1 **[def]** State the definition.
- [ ] Q2 **[use]** Give a basis of $N_pS$ in an adapted chart, and for $S = G^{-1}(0)$ with $0$ a regular value.
- [ ] Q3 **[why]** Why does the course use conormal covectors instead of normal vectors? What would identify them?
- [ ] Q4 **[example]** For $M \subseteq \mathbb{R}^n$, how does $N_pM$ match $(T^{\mathrm{geo}}_pM)^\perp$?

> [!tip]- Hints: where it lives, examples
> - Definition [[§37 Regular Submanifolds#^def-37-4|§37.4]]; Q2: Proposition [[§37 Regular Submanifolds#^prop-37-8|§37.8]] ($dx^{m-k+1}|_p, \ldots, dx^m|_p$), Proposition [[§37 Regular Submanifolds#^prop-37-19|§37.19]] ($dG^j|_p$).
> - Q3: the remark *No Normal Vectors Without a Metric* in [[§37 Regular Submanifolds|§37]]. Q4: Proposition [[§40 The Normal Bundle of a Submanifold of Euclidean Space#^prop-40-3|§40.3]]. Bundle version: Definition [[§52 Critical Points and the Hessian#^def-52-6|§52.6]].

#### Open submanifold of a smooth manifold · P2

An open $S \subseteq M$ with the smooth charts of $M$ whose domains lie in $S$, see Definition [[§37 Regular Submanifolds#^def-37-1|§37.1]]. *Source: Lecture 12.*

^nd-def-37-1

- [ ] Q1 **[def]** State the definition; what are its charts?
- [ ] Q2 **[use]** Why is the inclusion smooth, and why is a map into $S$ smooth iff it is smooth into $M$?
- [ ] Q3 **[why]** Why is $T_pS = T_pM$ for $p \in S$, but not for a closed subset?
- [ ] Q4 **[example]** Why are $\mathrm{GL}(n, \mathbb{R})$ and the domains $\pi^{-1}(U_\alpha)$ of a fibration open submanifolds?

> [!tip]- Hints: where it lives, examples
> - Definition [[§37 Regular Submanifolds#^def-37-1|§37.1]], Definition [[§3 Subspaces and Products#^def-3-2|§3.2]]; Proposition [[§17 Differentiable Structures#^prop-17-7|§17.7]], Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-6|§19.6]].
> - Q3: Lemma [[§28 Derivations and the Abstract Tangent Space#^lem-28-8|§28.8]] (germs see only a neighbourhood). Q4: Definition [[§11 Topological Groups and Classical Matrix Groups#^def-11-5|§11.5]], Definition [[§38 Fibrations#^def-38-1|§38.1]]; Proposition [[§37 Regular Submanifolds#^prop-37-4|§37.4]].

#### Transverse submanifolds · P2

Regular submanifolds $S_1,S_2\subseteq N$ intersect transversally, $S_1\pitchfork S_2$, if $T_qS_1+T_qS_2=T_qN$ for every $q\in S_1\cap S_2$, see Definition [[§37 Regular Submanifolds#^def-37-7|§37.7]]. *Source: review session (class), Oct 16.*

^nd-def-37-7

- [ ] Q1 **[def]** State the definition. In which space does the sum $T_qS_1+T_qS_2$ live, and through which maps?
- [ ] Q2 **[use]** Restate it as a condition on a map transverse to a submanifold (Definition [[§37 Regular Submanifolds#^def-37-5|§37.5]]).
- [ ] Q3 **[why]** Why does it hold when $S_1\cap S_2=\emptyset$? Uribe's remark on the notation $S_1\pitchfork S_2$: a statement, not a set.
- [ ] Q4 **[why]** Two lines in $\mathbb{R}^3$ meeting at a point: transverse or not? Count codimensions.

> [!tip]- Hints: where it lives
> - Definition [[§37 Regular Submanifolds#^def-37-7|§37.7]], Proposition [[§37 Regular Submanifolds#^prop-37-21|§37.21]], Theorem [[§37 Regular Submanifolds#^thm-37-22|§37.22]].
> - Q4: $1+1<3$, so the tangent lines cannot span $\mathbb{R}^3$; codimensions $2+2=4>3$ would force an empty intersection.

### Priority 4 · notes only (optional before the midterm)

#### Normal space · P4

$T_pM / \iota_{\ast p}(T_pS)$, see Definition [[§37 Regular Submanifolds#^def-37-6|§37.6]]. *Source: notes (not from lecture).*

^nd-def-37-6

- [ ] Q1 **[def]** State the definition; what is its dimension?
- [ ] Q2 **[why]** Why is the normal space a quotient and not a subspace of $T_pM$? How does it relate to the conormal space?
- [ ] Q3 **[use]** For $F \pitchfork S$, which map identifies the normal spaces of $F^{-1}(S)$ and of $S$?

> [!tip]- Hints: where it lives, examples
> - Definition [[§37 Regular Submanifolds#^def-37-6|§37.6]], Definition [[§21 Linear Algebra Toolkit#^def-21-6|§21.6]].
> - Q2: no complement is singled out without a metric; $N_pS$ is the dual of the normal space (annihilator of $T_pS$). Q3: Proposition [[§37 Regular Submanifolds#^prop-37-16|§37.16]].

## Proofs T7

### Priority 1 · homework (directly or extended)

#### Preimages of transverse level sets (Euclidean) · P1

If $F:\mathbb{R}^N\to\mathbb{R}^k$ is transverse to the regular level set $S=G^{-1}(0)$, then $F^{-1}(S)$ is a manifold of codimension $\operatorname{codim}S$ with $T^{\mathrm{geo}}_pF^{-1}(S)=F'(p)^{-1}(T^{\mathrm{geo}}_{F(p)}S)$, see Theorem [[§26 Transversality#^thm-26-1|§26.1]]. → drilled as [[Differentiable Manifolds HW Drill#^hw2-5|HW2.5]].

^nd-thm-26-1

#### Transversality is the regular value condition · P1

For $p\in F^{-1}(S)$, $q=F(p)$: $\operatorname{im}F'(p)+T^{\mathrm{geo}}_qS=\mathbb{R}^k$ if and only if $(G\circ F)'(p)$ is onto; so $F\pitchfork S$ if and only if $0$ is a regular value of $G\circ F$, see Proposition [[§26 Transversality#^prop-26-2|§26.2]]. *Source: filled in (setting of Assignment 2, Problem 5).*

^nd-prop-26-2

- [ ] Q1 **[state]** State the equivalence precisely: the setting ($F$, $G$, $S$, what is assumed of $0$), the point $p$, and both conditions.
- [ ] Q2 **[def]** Write $T^{\mathrm{geo}}_qS$ and $(G\circ F)'(p)$ in terms of $G'(q)$ and $F'(p)$. Which theorem and which rule do you use?
- [ ] Q3 (⇒) Given $w\in\mathbb{R}^\ell$, which $u\in\mathbb{R}^k$ do you choose first, and why does it exist?
- [ ] Q4 (⇒) How does transversality split $u$, and why does one of the two pieces disappear when you apply $G'(q)$?
- [ ] Q5 (⇐) Given $u\in\mathbb{R}^k$, how do you find $v\in\mathbb{R}^N$ with $u-F'(p)v\in T^{\mathrm{geo}}_qS$?
- [ ] Q6 For "consequently": why is $F^{-1}(S)=(G\circ F)^{-1}(0)$, and why does that turn the pointwise equivalence into the regular-value statement?
- [ ] Q7 **[why]** Where is "$0$ is a regular value of $G$" used? For $F(t)=(t,t^2)$ and $G(x,y)=y$ (Example [[§26 Transversality#^ex-26-2|§26.2]](b)), compute $(G\circ F)'(0)$ and say which conclusion of Theorem [[§26 Transversality#^thm-26-1|§26.1]] fails.

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S12 (transversality = the images span), S7 (linear algebra).
> - $T^{\mathrm{geo}}_qS=\ker G'(q)$ (Theorem [[§25 The Geometric Tangent Space#^thm-25-3|§25.3]]) and $(G\circ F)'(p)=G'(q)F'(p)$.
> - (⇒) $w=G'(q)u$; write $u=F'(p)v+t$ with $t\in\ker G'(q)$; then $w=G'(q)F'(p)v$.
> - (⇐) $G'(q)u=G'(q)F'(p)v$ for some $v$, so $u-F'(p)v\in\ker G'(q)$.
> - The condition involves only $F$ and $S$: $G$ disappears from the statement, only the proof chooses it.

#### Adapted charts give local defining maps · P1

For an adapted chart $(U,\varphi=(x_a,x_b))$, the map $x_b:U\to\mathbb{R}^k$ is smooth, a submersion at every point of $U$, $U\cap S=x_b^{-1}(\vec 0)$ with $\vec 0$ a regular value, and $\iota_{\ast q}(T_qS)=\ker(x_b)_{\ast q}$ for $q\in U\cap S$: a regular submanifold is locally a regular level set, see Proposition [[§37 Regular Submanifolds#^prop-37-7|§37.7]]. *Source: filled in (Step 2 of Assignment 5, Problem 2).*

^nd-prop-37-7

- [ ] Q1 **[state]** State the four parts and the "in particular".
- [ ] Q2 Write the coordinate representation of $x_b$ in the charts $\varphi$ and $\mathrm{id}_{\mathbb{R}^k}$, and its Jacobian. What is $(x_b)_{\ast q}(\partial/\partial x^i|_q)$?
- [ ] Q3 Why is $x_b$ a submersion at every point of $U$, and why is $\vec 0$ a regular value?
- [ ] Q4 For (4), prove $\iota_{\ast q}(T_qS)\subseteq\ker(x_b)_{\ast q}$.
- [ ] Q5 For (4), compute both dimensions and conclude.
- [ ] Q6 **[why]** In (4), where is it used that the chart is adapted in codimension exactly $k$, rather than only "$U\cap S\subseteq x_b^{-1}(\vec 0)$"?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S1, S7 (a subspace of the same dimension is everything).
> - Coordinate representation $(r^1,\dots,r^m)\mapsto(r^{m-k+1},\dots,r^m)$, Jacobian $(0\mid I_k)$.
> - Inclusion: $(x_b)_{\ast q}$ kills $\partial/\partial x^i|_q$ for $i\le m-k$, whose span is $\iota_{\ast q}(T_qS)$ (Proposition [[§37 Regular Submanifolds#^prop-37-6|§37.6]]).
> - Dimensions: $m-k$ on both sides (rank–nullity, $\operatorname{rank}(x_b)_{\ast q}=k$).
> - This is the input of Step 2 of Theorem [[§37 Regular Submanifolds#^thm-37-15|§37.15]].

#### Facts about an adapted chart in $\mathbb{R}^n$ · P1

For a chart of $\mathbb{R}^n$ adapted to $M$ with $G=(x^{m+1},\dots,x^n)$: $J(q)=G'(q)$ has rank $n-m$, $T^{\mathrm{geo}}_qM=\ker J(q)$, the columns $X_1(q),\dots,X_m(q)$ of $(\varphi^{-1})'(\varphi(q))$ span $T^{\mathrm{geo}}_qM$, and the gradients $\nabla G^s(q)$ are a basis of $(T^{\mathrm{geo}}_qM)^\perp$, see Lemma [[§37 Regular Submanifolds#^lem-37-10|§37.10]]. These are the steps of Assignment 5, Problem 5(a). → drilled as [[Differentiable Manifolds HW Drill#^hw5-5|HW5.5]].

^nd-lem-37-10

#### Preimages of transverse submanifolds · P1

If $F\pitchfork S$ with $S\subseteq N$ a regular submanifold of codimension $k$, then $F^{-1}(S)$ is a regular submanifold of $M$ of codimension $k$ and $j_{\ast p}(T_pF^{-1}(S))=(F_{\ast p})^{-1}(\iota_{\ast F(p)}(T_{F(p)}S))$, see Theorem [[§37 Regular Submanifolds#^thm-37-15|§37.15]]. → drilled as [[Differentiable Manifolds HW Drill#^hw5-2|HW5.2]].

^nd-thm-37-15

#### Critical points of a restriction · P1

$N_pS=\ker\iota_p^\ast$, $df_p=\iota_p^\ast(d\Phi_p)$ for $f=\Phi|_S$, and $p$ is critical for $f$ iff $d\Phi_p\in N_pS$, see Proposition [[§37 Regular Submanifolds#^prop-37-18|§37.18]]. → drilled as [[Differentiable Manifolds HW Drill#^hw5-4|HW5.4]].

^nd-prop-37-18

#### The conormal space of a regular level set · P1

For $S=G^{-1}(0)$ with $0$ a regular value, $dG^1|_p,\dots,dG^k|_p$ is a basis of $N_pS$, see Proposition [[§37 Regular Submanifolds#^prop-37-19|§37.19]]. → drilled as [[Differentiable Manifolds HW Drill#^hw5-4|HW5.4]].

^nd-prop-37-19

#### Lagrange multipliers · P1

$p\in S=G^{-1}(0)$ is critical for $\Phi|_S$ iff $d\Phi_p=\sum_j\lambda_j\,dG^j|_p$ for unique $\lambda_j$, see Theorem [[§37 Regular Submanifolds#^thm-37-20|§37.20]]. → drilled as [[Differentiable Manifolds HW Drill#^hw5-4|HW5.4]].

^nd-thm-37-20

### Priority 2 · stated or done in class

#### Transverse intersections of submanifolds in a manifold · P2

If $S_1,S_2\subseteq N$ are regular submanifolds with $S_1\pitchfork S_2$, then $S_1\cap S_2$ is a regular submanifold, $\operatorname{codim}(S_1\cap S_2)=\operatorname{codim}S_1+\operatorname{codim}S_2$ and $T_q(S_1\cap S_2)=T_qS_1\cap T_qS_2$, see Theorem [[§37 Regular Submanifolds#^thm-37-22|§37.22]]; and $S_1\pitchfork S_2$ iff the inclusion of $S_1$ is transverse to $S_2$, see Proposition [[§37 Regular Submanifolds#^prop-37-21|§37.21]]. *Source: review session (class), Oct 16: Uribe, "the theorem that you proved in homework"; the manifold version is filled in.*

^nd-thm-37-22

- [ ] Q1 **[state]** State the theorem with the definition of $S_1\pitchfork S_2$ (Definition [[§37 Regular Submanifolds#^def-37-7|§37.7]]), including the case $S_1\cap S_2=\emptyset$.
- [ ] Q2 Why is "$S_1\pitchfork S_2$" the same as "$\iota_1\pitchfork S_2$" (Definition [[§37 Regular Submanifolds#^def-37-5|§37.5]])? Identify $\iota_1^{-1}(S_2)$ and $(\iota_1)_{\ast q}(T_qS_1)$.
- [ ] Q3 Near $q\in S_1\cap S_2$, write each $S_i$ as the zero set of a local defining map $G_i:U_i\to\mathbb{R}^{k_i}$. Where does $G_i$ come from, and why is $\ker(dG_i)_q=T_qS_i$?
- [ ] Q4 With $G=(G_1,G_2)$, what is $\ker dG_q$? Using the dimension formula for $K_1+K_2$, show: $T_qS_1+T_qS_2=T_qN$ iff $dG_q$ is onto.
- [ ] Q5 Which theorem finishes, and why does "regular submanifold" being a local condition let you pass from $W\cap S_1\cap S_2$ to $S_1\cap S_2$?
- [ ] Q6 **[why]** A surface and a curve in $\mathbb{R}^3$ meeting transversally: what is the intersection? Two surfaces tangent at a point: which conclusion fails? (Compare Example [[§26 Transversality#^ex-26-1|§26.1]].)

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S5 (regular value theorem on a well-chosen map), S7 (linear algebra closes the gap); the Euclidean case is Proposition [[§26 Transversality#^prop-26-4|§26.4]].
> - $G_i$ = the last $k_i$ coordinates of a slice chart (Definition [[§37 Regular Submanifolds#^def-37-2|§37.2]]); $T_qS_i$ via Proposition [[§37 Regular Submanifolds#^prop-37-6|§37.6]].
> - $\dim(K_1\cap K_2)=2n-k_1-k_2-\dim(K_1+K_2)$, so the sum is everything iff $\dim\ker dG_q=n-k_1-k_2$ iff rank $k_1+k_2$.
> - Theorem [[§37 Regular Submanifolds#^thm-37-12|§37.12]] on $W=U_1\cap U_2$.

#### Two observations on adapted charts · P2

If, in a chart $(U,\varphi)$, $U\cap S$ is cut out by setting $k$ of the coordinates equal to constants, $x^{i_1}=c_1,\dots,x^{i_k}=c_k$, then there is an adapted chart with the same domain $U$, see Proposition [[§37 Regular Submanifolds#^prop-37-2|§37.2]]. *Source: Lecture 12 ("obvious observations"), filled in.* **[class exercise, Lecture 12]**

^nd-prop-37-2

- [ ] Q1 **[state]** State the two observations: what may replace the value $\vec 0$, and what may replace "the last $k$ coordinates".
- [ ] Q2 **[def]** Define a chart adapted to $S$ in codimension $k$ (Definition [[§37 Regular Submanifolds#^def-37-3|§37.3]]).
- [ ] Q3 Write the permutation $P$ and the translation $T$ of $\mathbb{R}^m$, and the new chart $A\circ\varphi$ with $A=T\circ P$.
- [ ] Q4 Why is $(U,A\circ\varphi)$ again a smooth chart? Name the lemma and say what the transition maps are.
- [ ] Q5 Check that the last $k$ coordinates of $A\circ\varphi$ vanish exactly on $U\cap S$.
- [ ] Q6 **[why]** The observation needs the equations to be *coordinates* set equal to constants. If $U\cap S$ is cut out by $k$ arbitrary smooth equations $g_1=\dots=g_k=0$, is there always an adapted chart on $U$? Give a counterexample in $\mathbb{R}^2$.

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S1 (work in a chart; modify the chart by a diffeomorphism of $\mathbb{R}^m$).
> - $P$ moves positions $i_1,\dots,i_k$ to the end; $T(s)=s-(\vec 0,\vec c)$; $A=T\circ P$ is an affine diffeomorphism.
> - Lemma [[§17 Differentiable Structures#^lem-17-6|§17.6]](2): composing a smooth chart with a diffeomorphism of $\mathbb{R}^m$ gives a smooth chart.
> - The last $k$ entries of $A\circ\varphi$ are $x^{i_l}-c_l$. Used in Lemma [[§37 Regular Submanifolds#^lem-37-11|§37.11]](2) and the regular value theorem.
> - For Q6: $g=xy$ on $\mathbb{R}^2$ cuts out a cross, which is no submanifold near $0$.

#### The induced smooth structure on a regular submanifold · P2

For each adapted chart $(U,\varphi=(x_a,x_b))$, $\varphi_S=x_a|_{U\cap S}$ is a homeomorphism of the open set $U\cap S$ of $S$ onto an open subset of $\mathbb{R}^{m-k}$, and these charts form a smooth atlas; so $S$ is a smooth manifold of dimension $m-k$, see Proposition [[§37 Regular Submanifolds#^prop-37-3|§37.3]]. *Source: Lecture 12 claimed (1) ("easy to check") and gave the reason for (2); completed in the notes.* **[class exercise, Lecture 12]**

^nd-prop-37-3

- [ ] Q1 **[state]** State the proposition: what $\varphi_S$ is, parts (1) and (2), and the dimension of $S$.
- [ ] Q2 Why is $S$ Hausdorff and second countable? Why is $U\cap S$ open in $S$?
- [ ] Q3 With $j(r)=(r,\vec 0)$ and $\mathrm{pr}(r,s)=r$, show $\varphi(U\cap S)=\varphi(U)\cap j(\mathbb{R}^{m-k})$, and deduce that $\varphi_S(U\cap S)=j^{-1}(\varphi(U))$ is open in $\mathbb{R}^{m-k}$.
- [ ] Q4 What is the inverse of $\varphi_S$? Why is it continuous as a map into the subspace $U\cap S$?
- [ ] Q5 Write the transition map $\psi_S\circ\varphi_S^{-1}$ in terms of $\psi\circ\varphi^{-1}$, $j$ and $\mathrm{pr}$, and give its domain. Why is it a diffeomorphism?
- [ ] Q6 **[why]** Why can one not simply restrict an arbitrary chart $(U,\varphi)$ of $M$ to $U\cap S$ to get a chart of $S$? Use the circle in $\mathbb{R}^2$.

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S1 (everything reduces to the local model $\mathbb{R}^{m-k}\times\{0\}\subseteq\mathbb{R}^m$).
> - Hausdorff and second countable are inherited by subspaces (Theorem [[§3 Subspaces and Products#^thm-3-5|§3.5]]).
> - $\varphi_S=\mathrm{pr}\circ\varphi|_{U\cap S}$ with inverse $r\mapsto\varphi^{-1}(j(r))$, using $\varphi(q)=j(\mathrm{pr}(\varphi(q)))$ for $q\in U\cap S$.
> - $\psi_S\circ\varphi_S^{-1}=\mathrm{pr}\circ(\psi\circ\varphi^{-1})\circ j$ on $j^{-1}(\varphi(U\cap V))$: "restrictions to $\mathbb{R}^{m-k}$ of $C^\infty$ maps"; the reverse transition has the same form.
> - For Q6: $\varphi(U\cap S)$ is a piece of a curve, not open in $\mathbb{R}^2$.

#### Smooth maps into and out of regular submanifolds · P2

(1) The inclusion $\iota:S\to M$ is smooth, with coordinate representation $j(r)=(r,\vec 0)$ in an adapted chart and its induced chart; (2) if $G:X\to M$ is smooth and $G(X)\subseteq S$, then $G$ is smooth as a map into $S$, see Lemma [[§37 Regular Submanifolds#^lem-37-5|§37.5]]. *Source: (1) Lecture 12, "immediate from the definitions"; (2) not from lecture; both filled in.* **[class exercise, Lecture 12]**

^nd-lem-37-5

- [ ] Q1 **[state]** State both parts, with the topology and the smooth structure that $S$ carries.
- [ ] Q2 (1) Why is $\iota$ continuous? Compute $\varphi\circ\iota\circ\varphi_S^{-1}$ in an adapted chart and its induced chart.
- [ ] Q3 (2) Why is $G$ continuous as a map into $S$?
- [ ] Q4 (2) Which charts do you take at $x\in X$ and at $G(x)$ (why shrink the chart at $x$ to $G^{-1}(U)$)? Compute $\varphi_S\circ G\circ\chi^{-1}$ and say why it is smooth.
- [ ] Q5 **[why]** In (2), at which step is it used that $S$ carries the *subspace* topology?
- [ ] Q6 Give two places later in the notes where (2) is used (e.g. fibres of a fibration, an embedding onto its image).

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S1 (check in a chart).
> - $\varphi_S=\mathrm{pr}\circ\varphi$ and $\varphi_S^{-1}=\varphi^{-1}\circ j$ on the induced chart, so $\varphi\circ\iota\circ\varphi_S^{-1}=j$.
> - (2) Continuity: $G^{-1}(O\cap S)=G^{-1}(O)$ because $G(X)\subseteq S$, and the sets $O\cap S$ are the open sets of $S$.
> - (2) Smoothness: $\varphi_S\circ G\circ\chi^{-1}=\mathrm{pr}\circ(\varphi\circ G\circ\chi^{-1})$.
> - Used in Proposition [[§38 Fibrations#^prop-38-2|§38.2]] and Corollary [[§42 Embeddings#^cor-42-3|§42.3]].

#### Tangent spaces of a regular submanifold · P2

$\iota_{\ast p}:T_pS\to T_pM$ is injective; in an adapted chart, $\iota_{\ast p}(\partial/\partial x^i|^S_p)=\partial/\partial x^i|_p$ for $i\le m-k$, so $\iota_{\ast p}(T_pS)$ is the span of the first $m-k$ coordinate vectors; by curves, $\iota_{\ast p}D_\gamma=D_{\iota\circ\gamma}$, see Proposition [[§37 Regular Submanifolds#^prop-37-6|§37.6]]. *Source: Lecture 12, "immediate from the definitions"; filled in.* **[class exercise, Lecture 12]**

^nd-prop-37-6

- [ ] Q1 **[state]** State the proposition, in both the coordinate form and the curve form.
- [ ] Q2 Which bases of $T_pS$ and $T_pM$ do you use, and what is the coordinate representation of $\iota$ (Lemma [[§37 Regular Submanifolds#^lem-37-5|§37.5]])?
- [ ] Q3 Compute the Jacobian of $j$ and read off $\iota_{\ast p}(\partial/\partial x^i|^S_p)$ from the matrix of a differential.
- [ ] Q4 Deduce the image of $\iota_{\ast p}$ and its injectivity.
- [ ] Q5 Which corollary gives the curve form, and what is $\iota\circ\gamma$?
- [ ] Q6 **[why]** The clean formula needs an *adapted* chart. In an arbitrary chart of $M$ at $p$, what can you still say about $\iota_{\ast p}(T_pS)$, and which property survives (dimension, injectivity)?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S1 (compute in coordinates), S10 (curves).
> - The Jacobian of $j(r)=(r,\vec 0)$ is the $m\times(m-k)$ matrix with $I_{m-k}$ on top and $0$ below.
> - Theorem [[§30 The Differential in Coordinates#^thm-30-2|§30.2]]: column $i$ of the Jacobian lists the components of $\iota_{\ast p}(\partial/\partial x^i|^S_p)$.
> - Injective: independent columns, or the $\partial/\partial x^i|_p$ are part of a basis.
> - Curves: Corollary [[§31 Tangent Vectors as Velocities of Curves#^cor-31-3|§31.3]] with $F=\iota$.

#### Level sets near a regular point · P2

If $G:V\to N$ is a submersion at the single point $p$, $c=G(p)$, there are charts $\theta=(z^i)$ at $p$ and $\chi$ at $c$ with $\chi(G(p'))=(z^1(p'),\dots,z^n(p'))$, so that $W\cap G^{-1}(c)=\{z^1=c_1,\dots,z^n=c_n\}$; $\hat\theta=(z^{n+1},\dots,z^m,z^1-c_1,\dots,z^n-c_n)$ is adapted to $G^{-1}(c)$; and $\iota_{\ast p}(T_pS)=\ker G_{\ast p}$ for a submanifold $S$ that agrees with $G^{-1}(c)$ near $p$, see Lemma [[§37 Regular Submanifolds#^lem-37-11|§37.11]]. *Source: Lecture 12's argument for the regular value theorem, isolated in the notes.*

^nd-lem-37-11

- [ ] Q1 **[state]** State the three parts. What is assumed of $G$ at $p$, and only at $p$?
- [ ] Q2 (1) Which theorem gives the charts? Why is a submersion at the single point $p$ enough? Translate the normal form into $\chi(G(p'))=(z^1(p'),\dots,z^n(p'))$.
- [ ] Q3 (1) Why is $G(p')=c$ equivalent to $\chi(G(p'))=\chi(c)$ for $p'\in W$?
- [ ] Q4 (2) Which proposition turns "$n$ coordinates equal to constants" into an adapted chart? Write it.
- [ ] Q5 (3) Show $\iota_{\ast p}(T_pS)\subseteq\ker G_{\ast p}$ by differentiating a constant composite, then compare dimensions.
- [ ] Q6 **[why]** Give a smooth $G:\mathbb{R}^2\to\mathbb{R}$ and a critical point $p$ where $G^{-1}(G(p))$ is not a submanifold near $p$. Which step of the proof fails there?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S8 (normal forms give charts), S6 (tangent space = kernel: inclusion, then dimensions).
> - Theorem [[§36 Submersions#^thm-36-6|§36.6]] needs the submersion only at $p$; it gives $\chi\circ G\circ\theta^{-1}(r)=(r^1,\dots,r^n)$.
> - (1) $\chi$ is injective on $Y\supseteq G(W)$.
> - (2) Proposition [[§37 Regular Submanifolds#^prop-37-2|§37.2]] with $\vec c=\chi(c)$.
> - (3) $G\circ\iota$ is constant near $p$, so $G_{\ast p}\circ\iota_{\ast p}=0$; both sides have dimension $m-n$. For Q6: $G=xy$ at $0$.

#### The regular value theorem for manifolds · P2

If $q\in N$ is a regular value of $F:M\to N$, then $S=F^{-1}(q)$ is a regular submanifold of codimension $n$ (possibly empty), and $\iota_{\ast p}(T_pS)=\ker F_{\ast p}$ for $p\in S$, see Theorem [[§37 Regular Submanifolds#^thm-37-12|§37.12]]. *Source: Lecture 12; the tangent space "I won't bother checking the kernel thing" is completed in the notes.* **[class exercise, Lecture 12]**

^nd-thm-37-12

- [ ] Q1 **[state]** State the theorem, with the definition of a regular value (Definition [[§36 Submersions#^def-36-4|§36.4]]). Where does the regular value live?
- [ ] Q2 What has to be produced at each $p\in S$? What if $S=\emptyset$?
- [ ] Q3 In the normal-form charts at $p$ and $q$, what are the equations of $S\cap U$? Justify each equivalence.
- [ ] Q4 Why are these equations "of the type $x_a$ equals a constant", and how do you get an adapted chart of codimension $n$ from them?
- [ ] Q5 The tangent space: prove $\iota_{\ast p}(T_pS)=\ker F_{\ast p}$ (the "kernel thing" left in lecture).
- [ ] Q6 **[why]** Why does the empty set count, and why is the theorem consistent with a $q\notin F(M)$ being a regular value? Give an $F$ and a critical value $q$ for which $F^{-1}(q)$ is not a submanifold.

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S8 (normal form), S5 (regular value theorem), S6 (tangent space = kernel).
> - Normal form: $\tilde F(r)=(r^1,\dots,r^n)$, so $q'\in S\cap U$ iff $(x^1(q'),\dots,x^n(q'))=\psi(q)$.
> - Proposition [[§37 Regular Submanifolds#^prop-37-2|§37.2]] gives the adapted chart $(x^{n+1},\dots,x^m,x^1-y^1(q),\dots,x^n-y^n(q))$; this is Lemma [[§37 Regular Submanifolds#^lem-37-11|§37.11]] with $V=M$.
> - Kernel: $F\circ\iota$ is constant, so $\iota_{\ast p}(T_pS)\subseteq\ker F_{\ast p}$; both have dimension $m-n$.
> - For Q6: $F(x,y)=x^2-y^2$ and $q=0$ (a cross).

#### Fibres of submersions are regular submanifolds · P2

If $F:M\to N$ is a submersion, every fibre $F^{-1}(q)$ is a regular submanifold of codimension $n$, possibly empty, see Corollary [[§37 Regular Submanifolds#^cor-37-13|§37.13]]. *Source: Lecture 12.*

^nd-cor-37-13

- [ ] Q1 **[state]** State the corollary.
- [ ] Q2 Why is every $q\in N$ a regular value of a submersion, including $q\notin F(M)$?
- [ ] Q3 Which theorem finishes the proof?
- [ ] Q4 **[why]** Are all the fibres of a surjective submersion diffeomorphic to one another? Use Example [[§38 Fibrations#^ex-38-1|§38.1]].
- [ ] Q5 Where is the corollary used for fibrations and for the vertical space (Definition [[§38 Fibrations#^def-38-5|§38.5]])?

> [!tip]- Hints: route of the proof in the notes
> - A submersion is onto at every point, so every point of every fibre is regular; empty fibres are vacuous.
> - Theorem [[§37 Regular Submanifolds#^thm-37-12|§37.12]].
> - The punctured plane over $\mathbb{R}$: one fibre is disconnected, the others are lines.
> - Used in Proposition [[§38 Fibrations#^prop-38-2|§38.2]] and to read $V_y$ as the tangent space of the fibre.

#### Charts of a submanifold extend to adapted charts · P2

Every chart of a regular submanifold $S\subseteq M$ near $p$ is, near $p$, the induced chart of a chart of $M$ adapted to $S$. No box in the notes: stated in Lecture 12 after Proposition [[§37 Regular Submanifolds#^prop-37-3|§37.3]] (paragraph *Extending charts*), not proved. *Source: Lecture 12, a student's question; Uribe: "The answer is yes".* **[class exercise, Lecture 12]**

^nd-cx-12-1

- [ ] Q1 **[state]** State the claim precisely: given a chart $(V,\psi)$ of $S$ at $p$, what chart of $M$ do you want, and what should its induced chart be?
- [ ] Q2 Fix an adapted chart $(U,\varphi=(x_a,x_b))$ at $p$. What kind of map is $h=\psi\circ\varphi_S^{-1}$, and between which open subsets of $\mathbb{R}^{m-k}$?
- [ ] Q3 Define $\Psi=(h\circ x_a,\,x_b)$ on $U'=\{q\in U: x_a(q)\in\varphi_S(U\cap V)\}$. Why is $U'$ open, and why is $\Psi$ a smooth chart of $M$?
- [ ] Q4 Check that $\Psi$ is adapted to $S$ and that its induced chart is $\psi$ near $p$.
- [ ] Q5 **[why]** Why does the construction need an adapted chart to start from? Would it work starting from an arbitrary chart of $M$?

> [!tip]- Hints: route (not in the notes; a sketch)
> - Strategy: S1 (reduce to the local model).
> - $h$ is a diffeomorphism between open subsets of $\mathbb{R}^{m-k}$ (a transition map of $S$).
> - In the chart $\varphi$, $\Psi$ reads $(r,s)\mapsto(h(r),s)$, a diffeomorphism with inverse $(r',s)\mapsto(h^{-1}(r'),s)$; compose with $\varphi$ (Lemma [[§17 Differentiable Structures#^lem-17-6|§17.6]]).
> - The last $k$ coordinates are still $x_b$, so $U'\cap S=\{x_b=0\}$, and the induced chart is $h\circ\varphi_S=\psi$.

#### Smooth functions on a submanifold extend locally · P2

A smooth function on a regular submanifold $S\subseteq M$ extends, near each point of $S$, to a smooth function on an open set of $M$. No box in the notes: stated in Lecture 12 (paragraph *Extending charts* after Proposition [[§37 Regular Submanifolds#^prop-37-3|§37.3]]), not proved. *Source: Lecture 12.* **[class exercise, Lecture 12]**

^nd-cx-12-2

- [ ] Q1 **[state]** State the local extension claim: given $f\in C^\infty(S)$ and $p\in S$, what do you want to produce?
- [ ] Q2 In an adapted chart $(U,\varphi=(x_a,x_b))$ at $p$, what is $f\circ\varphi_S^{-1}$, and on which open set of $\mathbb{R}^{m-k}$ is it smooth?
- [ ] Q3 Define $\tilde f=(f\circ\varphi_S^{-1})\circ x_a$ on $\{q\in U:x_a(q)\in\varphi_S(U\cap S)\}$. Why is it smooth, and why does it agree with $f$ on $S$ there?
- [ ] Q4 **[why]** Why is the statement only local? What extra tool (not in the notes) would be needed to extend $f$ to a whole neighbourhood of $S$, or to all of $M$ when $S$ is closed?

> [!tip]- Hints: route (not in the notes; a sketch)
> - Strategy: S1, S11 (local, then global).
> - $\tilde f$ is constant in the $x_b$ directions; on $S$, $x_a=\varphi_S$, so $\tilde f=f$.
> - Gluing local extensions needs partitions of unity (Lee, Ch. 2); the notes only have bump functions (Proposition [[§53 Vector Fields#^prop-53-4|§53.4]]).

### Priority 3 · filled in, using a technique the homework drills

#### Transverse intersections of level sets · P3

For regular level sets $S_i=G_i^{-1}(0)\subseteq\mathbb{R}^k$ and $q\in S_1\cap S_2$: $T_qS_1+T_qS_2=\mathbb{R}^k$ if and only if $(G_1,G_2)'(q)$ is onto; if the intersection is transverse, $S_1\cap S_2$ is a manifold with $\operatorname{codim}(S_1\cap S_2)=\operatorname{codim}S_1+\operatorname{codim}S_2$ and $T_q(S_1\cap S_2)=T_qS_1\cap T_qS_2$, see Proposition [[§26 Transversality#^prop-26-4|§26.4]]. *Source: filled in.*

^nd-prop-26-4

- [ ] Q1 **[state]** State the proposition, with the definition of a transverse intersection (Definition [[§26 Transversality#^def-26-3|§26.3]]) and what happens when $S_1\cap S_2=\emptyset$.
- [ ] Q2 Write the Jacobian of $(G_1,G_2)$ at $q$ as a stacked matrix. What is its kernel?
- [ ] Q3 Using rank–nullity, turn "$(G_1,G_2)'(q)$ is onto" into a condition on $\dim(T_1\cap T_2)$, where $T_i=T^{\mathrm{geo}}_qS_i$.
- [ ] Q4 Using the dimension formula for a sum of subspaces, turn "$T_1+T_2=\mathbb{R}^k$" into a condition on $\dim(T_1\cap T_2)$. Why are the two conditions the same?
- [ ] Q5 Write $S_1\cap S_2$ as a level set. Which theorems give that it is a manifold, its codimension and its tangent space?
- [ ] Q6 **[why]** Example [[§26 Transversality#^ex-26-1|§26.1]]: for $S^2$ and the plane $z=c$, for which $c$ is the intersection transverse? At $c=\pm1$, what is the intersection, and which conclusion fails?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S7 (linear algebra closes the gap), S5 (regular value theorem on a well-chosen map).
> - $\dim T_i=k-\ell_i$; the kernel of the stacked Jacobian is $T_1\cap T_2$.
> - Both conditions say $\dim(T_1\cap T_2)=k-\ell_1-\ell_2$.
> - $S_1\cap S_2=(G_1,G_2)^{-1}(0)$, so $0$ is a regular value of $(G_1,G_2)$ exactly when the intersection is transverse; then use Theorem [[§7 The Regular Value Theorem#^thm-7-3|§7.3]] and Theorem [[§25 The Geometric Tangent Space#^thm-25-3|§25.3]].

#### A basis of the conormal space · P3

In an adapted chart at $p$, $\xi=\sum_i\xi_i\,dx^i|_p$ lies in $N_pS$ if and only if $\xi_i=0$ for $i\le m-k$; so $dx^{m-k+1}|_p,\dots,dx^m|_p$ is a basis of $N_pS$ and $\dim N_pS=k$, see Proposition [[§37 Regular Submanifolds#^prop-37-8|§37.8]]. *Source: filled in.*

^nd-prop-37-8

- [ ] Q1 **[state]** State the proposition.
- [ ] Q2 **[def]** Define the conormal space $N_pS$ (Definition [[§37 Regular Submanifolds#^def-37-4|§37.4]]). What are the components $\xi_i$ of a covector?
- [ ] Q3 Why does a covector vanish on $\iota_{\ast p}(T_pS)$ exactly when it vanishes on $\partial/\partial x^i|_p$ for $i\le m-k$?
- [ ] Q4 Conclude the basis and the dimension.
- [ ] Q5 **[why]** Why do the notes speak of a *conormal* space rather than a normal vector space at $p$? What would identify $N_pS$ with a space of normal vectors?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S1, S7.
> - $\iota_{\ast p}(T_pS)=\operatorname{span}\{\partial/\partial x^i|_p:i\le m-k\}$ (Proposition [[§37 Regular Submanifolds#^prop-37-6|§37.6]]); $\xi_i=\xi(\partial/\partial x^i|_p)$.
> - $\xi\in N_pS$ iff $\xi=\sum_{j>m-k}\xi_j\,dx^j|_p$.
> - No metric, no orthogonality: with an inner product $T_p^\ast M\cong T_pM$ and $N_pS$ becomes the normal space (remark *No Normal Vectors Without a Metric*).
> - Used in Proposition [[§37 Regular Submanifolds#^prop-37-19|§37.19]] ([[Differentiable Manifolds HW Drill#^hw5-4|HW5.4]]).

#### Regular submanifolds of Euclidean space: the slice description · P3

For $X\subseteq\mathbb{R}^{n+k}$ and $p\in X$: $X$ is described externally (equivalently internally, or as a graph) near $p$ if and only if there is a chart of $\mathbb{R}^{n+k}$ at $p$ adapted to $X$; so the regular submanifolds of $\mathbb{R}^{n+k}$ are exactly the manifolds of the geometric stage, see Proposition [[§37 Regular Submanifolds#^prop-37-9|§37.9]]. *Source: filled in.*

^nd-prop-37-9

- [ ] Q1 **[state]** State the equivalence and the "in particular".
- [ ] Q2 Which two implications suffice, given that the external, internal and graph descriptions are already equivalent?
- [ ] Q3 Graph ⇒ slice: write $\Phi(x,y)=(x,y-h(x))$. Why is it a diffeomorphism of $V\times V'$ onto an open set, and why is it adapted to $X$?
- [ ] Q4 Slice ⇒ external: why does $F=x_b$ have rank $k$ at every point of $U$?
- [ ] Q5 Write two adapted charts of $S^2$ near the north pole.
- [ ] Q6 **[why]** In "slice ⇒ external", the chart must be a *diffeomorphism* onto its image. Show what goes wrong with the homeomorphism $(x,y)\mapsto(x,y^3)$ of $\mathbb{R}^2$ and $X$ the $x$-axis.

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S1, S14 (differentiate $\varphi^{-1}\circ\varphi=\mathrm{id}$).
> - Graph ⇒ slice: inverse $(x,z)\mapsto(x,z+h(x))$; the image is the preimage of $V\times V'$ under that continuous map; $y-h(x)=0$ iff the point is on the graph.
> - Slice ⇒ external: $\varphi'(q)$ is invertible (chain rule on $\varphi^{-1}\circ\varphi$), so its last $k$ rows, the rows of $F'(q)$, are independent.
> - Examples: $(x,y,z)\mapsto(x,y,z-\sqrt{1-x^2-y^2})$ and $(x,y,z)\mapsto(x,y,x^2+y^2+z^2-1)$.
> - For Q6: $F=y^3$ has $F'=0$ on the axis, so $0$ is not a regular value.

#### Normal spaces under a transverse map · P3

With $K_p=(F_{\ast p})^{-1}(\iota_{\ast q}(T_qS))$, $F_{\ast p}$ induces a well-defined injective linear map $\bar F_{\ast p}:T_pM/K_p\to T_qN/\iota_{\ast q}(T_qS)$, which is onto exactly when $F$ is transverse to $S$ at $p$; if $F\pitchfork S$ it is an isomorphism of normal spaces, see Proposition [[§37 Regular Submanifolds#^prop-37-16|§37.16]]. *Source: filled in.*

^nd-prop-37-16

- [ ] Q1 **[state]** State the three parts and the transverse case.
- [ ] Q2 **[def]** Define the normal space $T_pM/\iota_{\ast p}(T_pS)$ (Definition [[§37 Regular Submanifolds#^def-37-6|§37.6]]). What is its dimension, and why is $K_p$ a subspace?
- [ ] Q3 (1) With $A=\pi_N\circ F_{\ast p}$, compute $\ker A$. Which universal property gives $\bar F_{\ast p}$?
- [ ] Q4 (2) Why is $\bar F_{\ast p}$ injective?
- [ ] Q5 (3) Show: $\bar F_{\ast p}$ onto ⇔ every $u\in T_qN$ lies in $F_{\ast p}(T_pM)+\iota_{\ast q}(T_qS)$.
- [ ] Q6 **[why]** Read the isomorphism as a dimension count: why does it explain that transversality preserves codimension? In Example [[§26 Transversality#^ex-26-2|§26.2]](a), which normal space is too small?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S2 (well-definedness via the quotient), S7.
> - $\ker A=K_p$ because $\ker\pi_N=\iota_{\ast q}(T_qS)$; Proposition [[§21 Linear Algebra Toolkit#^prop-21-6|§21.6]] gives $\bar F_{\ast p}$ with $\bar F_{\ast p}\circ\pi_M=A$.
> - Onto: $u+E=F_{\ast p}v+E$ iff $u-F_{\ast p}v\in E$.
> - Transverse case: $\dim T_pM/K_p=k=\dim T_qN/E$.

#### Special cases of transversality · P3

(1) $F\pitchfork\{c\}$ iff $c$ is a regular value, and Theorem [[§37 Regular Submanifolds#^thm-37-15|§37.15]] returns the regular value theorem; (2) if $S,S'\subseteq N$ intersect transversally, $S'\cap S$ is a regular submanifold of $S'$ of codimension $k$ and of $N$ of codimension $k+k'$, with $T_p(S'\cap S)=T_pS'\cap T_pS$; (3) a submersion is transverse to every regular submanifold, see Corollary [[§37 Regular Submanifolds#^cor-37-17|§37.17]]. *Source: filled in.*

^nd-cor-37-17

- [ ] Q1 **[state]** State the three special cases precisely, with the definition of transverse intersection.
- [ ] Q2 (1) Why is $\{c\}$ a regular submanifold of codimension $n$, and what does the transversality condition reduce to at $p\in F^{-1}(c)$?
- [ ] Q3 (2) Why is "$S$ and $S'$ intersect transversally" the condition $\iota'\pitchfork S$? What does Theorem [[§37 Regular Submanifolds#^thm-37-15|§37.15]] applied to $\iota'$ give inside $S'$?
- [ ] Q4 (2) Inside $N$: with local defining maps $x_b$, $x'_b$ and $H=(x_b,x'_b)$, compute $H^{-1}(\vec 0)$ and $\ker H_{\ast p}$, and show $H$ is a submersion at $p$.
- [ ] Q5 (2) Use $A(A^{-1}(E))=\operatorname{im}A\cap E$ to get $T_p(S'\cap S)=T_pS'\cap T_pS$.
- [ ] Q6 (3) Why is a submersion transverse to every regular submanifold?
- [ ] Q7 **[why]** Two curves in $\mathbb{R}^3$ meet in a single point $p$. Can they intersect transversally at $p$? What does the dimension count $1+1$ versus $3$ say?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S12 (transversality = images span), S7.
> - (1) $\{c\}=\mathrm{id}_N^{-1}(c)$ (Corollary [[§37 Regular Submanifolds#^cor-37-13|§37.13]]); $T_c\{c\}=0$, so transversality says $F_{\ast p}$ is onto.
> - (2) $\dim\ker H_{\ast p}=(n-k)+(n-k')-n$, so $\operatorname{rank}H_{\ast p}=k+k'$; then Lemma [[§37 Regular Submanifolds#^lem-37-11|§37.11]](2), (3).
> - (3) $F_{\ast p}(T_pM)=T_{F(p)}N$ already.
> - For Q7: the two tangent lines span at most a plane.

### Priority 4 · notes only (optional before the midterm)

#### Open submanifolds are the regular submanifolds of codimension 0 · P4

An open subset $S\subseteq M$ is a regular submanifold of codimension $0$ whose induced structure is the open-submanifold structure; conversely a regular submanifold of codimension $0$ is open, see Proposition [[§37 Regular Submanifolds#^prop-37-4|§37.4]]. *Source: filled in.*

^nd-prop-37-4

- [ ] Q1 **[state]** State both directions.
- [ ] Q2 For $k=0$, what does the condition on an adapted chart $(U,\varphi)$ say about $U$ and $S$?
- [ ] Q3 (1) For $S$ open, which charts are adapted? What is $\varphi_S$ for such a chart, and why do the two smooth structures coincide?
- [ ] Q4 (2) Why is a codimension-$0$ regular submanifold a union of open subsets of $M$?
- [ ] Q5 **[why]** True or false: a regular submanifold $S\subseteq M$ with $\dim S=\dim M$ is all of $M$ when $M$ is connected. What extra hypothesis would make it true?

> [!tip]- Hints: route of the proof in the notes
> - With $k=0$ there are no last coordinates: adapted means $U\cap S=U$, i.e. $U\subseteq S$.
> - (1) Restrict any chart at $p$ to $U\cap S$; then $\varphi_S=\varphi$, and the induced atlas is the open-submanifold atlas (Theorem [[§17 Differentiable Structures#^thm-17-5|§17.5]] gives equality of the structures).
> - (2) $S=\bigcup_p U_p$ with each $U_p\subseteq S$ open in $M$.
> - For Q5: $(0,1)\subseteq\mathbb{R}$ is open, not closed; a closed and open subset of a connected $M$ is all of $M$.

# T8. Fibrations

## Definitions T8

### Priority 1 · homework (directly or extended)

#### Local section · P1

A smooth $s : U \to E$ on an open $U \subseteq B$ with $\pi \circ s = \mathrm{id}_U$, see Definition [[§38 Fibrations#^def-38-4|§38.4]]. *Source: Lecture 13; Assignment 4.*

^nd-def-38-4

- [ ] Q1 **[def]** State the definition.
- [ ] Q2 **[use]** Show that a local trivialization over $U$ gives local sections over $U$.
- [ ] Q3 **[why]** For the Hopf fibration, a local section gives a local trivialization. Why does this use the $S^1$-action, and why does it fail for a general fibration? → drilled as [[Differentiable Manifolds HW Drill#^hw4-4|HW4.4]].
- [ ] Q4 **[example]** Write a local section of the Hopf fibration over $U_i = \{z_i \neq 0\}$.

> [!tip]- Hints: where it lives, examples
> - Definition [[§38 Fibrations#^def-38-4|§38.4]]; Q2: Proposition [[§38 Fibrations#^prop-38-4|§38.4]] ($s(u) = \phi^{-1}(u, f_0)$).
> - Q3: Proposition [[§44 Projective Spaces and the Hopf Fibration#^prop-44-1|§44.1]]; the remark *Trivializations and Frames* in [[§49 The Tangent Bundle|§49]] (one section suffices because the fibre is one orbit). Q4: Corollary [[§44 Projective Spaces and the Hopf Fibration#^cor-44-2|§44.2]].

### Priority 2 · stated or done in class

#### Fibration · P2

$\pi : M \to B$ is a fibration with fibre $F$ if $B$ has an open cover $\{U_\alpha\}$ with diffeomorphisms $\phi_\alpha : \pi^{-1}(U_\alpha) \to U_\alpha \times F$ satisfying $\mathrm{pr}_1 \circ \phi_\alpha = \pi$, see Definition [[§38 Fibrations#^def-38-1|§38.1]]. *Source: Lectures 11–13.*

^nd-def-38-1

- [ ] Q1 **[def]** State the definition: the data ($M$, $B$, $F$, $\pi$), the cover, the local trivializations, and the commuting condition. What does $\mathrm{pr}_1 \circ \phi_\alpha = \pi$ say in words? Give three fibrations from the notes, with base and fibre.
- [ ] Q2 **[class exercise, Lecture 12]** Check that a fibration is a submersion ("by using the commutativity of the diagram"), and surjective if $F \neq \emptyset$.
- [ ] Q3 **[use]** Show every fibre $\pi^{-1}(b)$ is a regular submanifold diffeomorphic to $F$.
- [ ] Q4 **[why]** Remove the point $(0, 1)$ from $\mathbb{R}^2$ and project to the $x$-axis: a surjective submersion. Why is it not a fibration?
- [ ] Q5 **[why]** State Ehresmann's theorem. Which hypothesis does the punctured plane violate? Why do diffeomorphic fibres not suffice?

> [!tip]- Hints: where it lives, examples
> - Definition [[§38 Fibrations#^def-38-1|§38.1]]; Q2: Proposition [[§38 Fibrations#^prop-38-1|§38.1]] (part 2: $\pi|_W = \mathrm{pr}_1 \circ \phi_\alpha$, chain rule; stated in lecture as "chain rule and stuff").
> - Q3: Proposition [[§38 Fibrations#^prop-38-2|§38.2]]. Q4: Example [[§38 Fibrations#^ex-38-1|§38.1]] (fibres change: a line, then a line minus a point). Q5: Theorem [[§38 Fibrations#^thm-38-3|§38.3]] (proper; quoted), Example [[§38 Fibrations#^ex-38-2|§38.2]].
> - Q1 examples: Example [[§39 Examples of Fibrations#^ex-39-1|§39.1]] (product), Proposition [[§39 Examples of Fibrations#^prop-39-1|§39.1]] (Möbius band), Example [[§44 Projective Spaces and the Hopf Fibration#^ex-44-3|§44.3]] (Hopf), Corollary [[§49 The Tangent Bundle#^cor-49-3|§49.3]] ($TM$), Proposition [[§40 The Normal Bundle of a Submanifold of Euclidean Space#^prop-40-2|§40.2]] (normal bundle).

#### Trivial fibration · P2

A fibration with a single trivialization over all of $B$: $\phi : M \to B \times F$, $\mathrm{pr}_1 \circ \phi = \pi$, see Definition [[§38 Fibrations#^def-38-2|§38.2]]. *Source: Lecture 12.*

^nd-def-38-2

- [ ] Q1 **[def]** State the definition.
- [ ] Q2 **[example]** Why is $\mathrm{pr}_1 : B \times F \to B$ trivial, and why is every trivial fibration this one up to diffeomorphism?
- [ ] Q3 **[why]** Why is the Hopf fibration $S^{2n+1} \to \mathbb{CP}^n$, $n \ge 1$, not trivial? Which object would a trivialization produce?
- [ ] Q4 **[why]** The Möbius band "looks like a strip wherever you cut it". Where does its pair of trivializations disagree, and why does that make a single global trivialization implausible?

> [!tip]- Hints: where it lives, examples
> - Definition [[§38 Fibrations#^def-38-2|§38.2]]; Q2: Example [[§39 Examples of Fibrations#^ex-39-1|§39.1]].
> - Q3: a global trivialization gives a global section (Proposition [[§38 Fibrations#^prop-38-4|§38.4]]), and there is none, Corollary [[§44 Projective Spaces and the Hopf Fibration#^cor-44-2|§44.2]], the remark *Sections Need Not Exist* in [[§44 Projective Spaces and the Hopf Fibration|§44]].
> - Q4: Proposition [[§39 Examples of Fibrations#^prop-39-1|§39.1]] (part 3: a sign on one arc). The notes do not prove non-triviality.

#### Section · P2

A smooth $s : B \to E$ with $\pi \circ s = \mathrm{id}_B$, see Definition [[§38 Fibrations#^def-38-3|§38.3]]. *Source: Lecture 13.*

^nd-def-38-3

- [ ] Q1 **[def]** State the definition ("first go up, then down").
- [ ] Q2 **[example]** Give the zero section of $TM$ and of $T^\ast M$, and say why a vector field and a one-form are sections.
- [ ] Q3 **[use]** Differentiate $\pi \circ s = \mathrm{id}$: what do you learn about $s_{\ast p}$ and $\pi_{\ast s(p)}$, and how does $T_{s(p)}E$ split?
- [ ] Q4 **[why]** Why is a section an embedding with closed image? → drilled as [[Differentiable Manifolds HW Drill#^hw5-1|HW5.1]].
- [ ] Q5 **[why]** Does every fibration have a global section? Does every vector bundle?

> [!tip]- Hints: where it lives, examples
> - Definition [[§38 Fibrations#^def-38-3|§38.3]]; Q2: Definition [[§49 The Tangent Bundle#^def-49-3|§49.3]], Definition [[§50 The Cotangent Bundle#^def-50-3|§50.3]], Definition [[§53 Vector Fields#^def-53-1|§53.1]], Definition [[§51 One-Forms#^def-51-1|§51.1]].
> - Q3: Proposition [[§38 Fibrations#^prop-38-5|§38.5]]. Q4: Proposition [[§42 Embeddings#^prop-42-10|§42.10]].
> - Q5: no (Hopf, Corollary [[§44 Projective Spaces and the Hopf Fibration#^cor-44-2|§44.2]]); yes, the zero section (the remark *Sections Need Not Exist* in [[§44 Projective Spaces and the Hopf Fibration|§44]]).

#### Vertical space · P2

$V_y = \ker \pi_{\ast y} \subseteq T_yE$, see Definition [[§38 Fibrations#^def-38-5|§38.5]]. *Source: Lecture 13.*

^nd-def-38-5

- [ ] Q1 **[def]** State the definition.
- [ ] Q2 **[use]** If $\pi$ is a submersion, show $V_y$ is the tangent space of the fibre through $y$. Which theorem gives this?
- [ ] Q3 **[use]** Given a section $s$ with $s(p) = y$, show $T_yE = s_{\ast p}(T_pM) \oplus V_y$ and give the projection onto $V_y$.
- [ ] Q4 **[why]** Is there a canonical "horizontal" complement to $V_y$ at every $y$? When is there one?
- [ ] Q5 **[example]** Compute the vertical space of $T^\ast M$ along the zero section.

> [!tip]- Hints: where it lives, examples
> - Definition [[§38 Fibrations#^def-38-5|§38.5]]; Q2: Theorem [[§37 Regular Submanifolds#^thm-37-12|§37.12]] ($\iota_{\ast}(T_yE_b) = \ker \pi_{\ast y}$).
> - Q3: Proposition [[§38 Fibrations#^prop-38-5|§38.5]] ($P = \mathrm{id} - s_{\ast p} \circ \pi_{\ast y}$). Q4: no in general; along the image of a section, yes (Q3).
> - Q5: Proposition [[§52 Critical Points and the Hessian#^prop-52-8|§52.8]] (spanned by $\partial/\partial \xi_j$).

#### Vector bundle · P2

A fibration $\pi : E \to M$ whose fibres are vector spaces and whose local trivializations are linear isomorphisms on each fibre; the notes give only the remark, the definition is Lee's (Ch. 10). *Source: Lecture 12 (remark; definition postponed); Lee Ch. 10; asked on the 2025 midterm.*

^nd-cx-vb

- [ ] Q1 **[def]** Start from the fibration definition with model fibre $\mathbb{R}^k$. Which extra structure does each fibre $E_p = \pi^{-1}(p)$ carry? Which extra condition must each local trivialization $\Phi : \pi^{-1}(U) \to U \times \mathbb{R}^k$ satisfy on each $E_q$, $q \in U$?
- [ ] Q2 **[def]** Now write the full definition of a smooth (real) vector bundle of rank $k$: the data, $\pi$ smooth and surjective, the vector space structure on fibres, the local trivializations (diffeomorphisms, $\mathrm{pr}_1 \circ \Phi = \pi$, linear on fibres).
- [ ] Q3 **[why]** For two trivializations $\Phi$ over $U$ and $\Psi$ over $V$, show $\Phi \circ \Psi^{-1}(p, v) = (p, \tau(p)v)$ for a map $\tau : U \cap V \to \mathrm{GL}(k, \mathbb{R})$. Where is "linear on fibres" used? Is $\tau$ smooth?
- [ ] Q4 **[example]** Show $TM \to M$ is a vector bundle of rank $m$: name the trivializations and the transition maps $\tau$. Do the same for $T^\ast M$, for the normal bundle of $M \subseteq \mathbb{R}^n$, and for the Möbius band with fibre $\mathbb{R}$ in place of $(-1, 1)$ (what is $\tau$ on the two arcs?).
- [ ] Q5 **[why]** Why is the Hopf fibration $S^{2n+1} \to \mathbb{CP}^n$ not a vector bundle for any choice of structure? (Two reasons: the fibre, and sections.)

> [!tip]- Hints: where it lives, sources
> - The notes: the remark *Vector Bundles* in [[§49 The Tangent Bundle|§49]] ("the fibres are abstract vector spaces, and you can find trivializations which restrict to linear isomorphisms fibrewise"); the fibration it refines: Definition [[§38 Fibrations#^def-38-1|§38.1]].
> - Lee, *Introduction to Smooth Manifolds* (2nd ed.), Ch. 10, "Vector Bundles": the definition of a (smooth) vector bundle of rank $k$; Lemma 10.5 for the transition functions $\tau : U \cap V \to \mathrm{GL}(k, \mathbb{R})$ (smooth); Example 10.3 for the Möbius bundle.
> - Q4: Corollary [[§49 The Tangent Bundle#^cor-49-3|§49.3]] (part 2: linear on each $T_pM$), Proposition [[§49 The Tangent Bundle#^prop-49-2|§49.2]] ($\tau$ = Jacobian of the chart change), Proposition [[§50 The Cotangent Bundle#^prop-50-2|§50.2]] (transpose inverse), Proposition [[§40 The Normal Bundle of a Submanifold of Euclidean Space#^prop-40-2|§40.2]] (part 2).
> - Möbius: Proposition [[§39 Examples of Fibrations#^prop-39-1|§39.1]] (part 3: $\tau = \pm 1$). Q5: fibre $S^1$ is not a vector space; a vector bundle has the zero section, the Hopf fibration has no global section (Corollary [[§44 Projective Spaces and the Hopf Fibration#^cor-44-2|§44.2]]).

## Proofs T8

### Priority 1 · homework (directly or extended)

#### Local trivializations give local sections · P1

If $\phi:\pi^{-1}(U)\to U\times F$ is a local trivialization and $f_0\in F$, then $s(u)=\phi^{-1}(u,f_0)$ is a local section over $U$, see Proposition [[§38 Fibrations#^prop-38-4|§38.4]]. *Source: filled in (principle behind Assignment 4, Problem 4).*

^nd-prop-38-4

- [ ] Q1 **[state]** State the proposition.
- [ ] Q2 **[def]** Define a section and a local section (Definitions [[§38 Fibrations#^def-38-3|§38.3]], [[§38 Fibrations#^def-38-4|§38.4]]).
- [ ] Q3 Why is $s$ smooth? Write it as a composite of three smooth maps.
- [ ] Q4 Prove $\pi\circ s=\mathrm{id}_U$ from the commuting triangle.
- [ ] Q5 **[why]** Does a single local section always give a local trivialization? For which fibration in the notes does it, and what structure makes it work? Does a fibration always have a *global* section?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S14 (use $\mathrm{pr}_1\circ\phi=\pi$).
> - $s=\iota_{\pi^{-1}(U)}\circ\phi^{-1}\circ\iota^{f_0}$ with the slice inclusion $\iota^{f_0}(u)=(u,f_0)$ (Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-11|§19.11]]).
> - $\pi(s(u))=\mathrm{pr}_1(\phi(\phi^{-1}(u,f_0)))=u$.
> - Q5: the Hopf fibration, where $S^1$ acts freely and transitively on fibres (Proposition [[§44 Projective Spaces and the Hopf Fibration#^prop-44-1|§44.1]]); it has no global section (remark *Sections Need Not Exist*). For $TM$ one needs $m$ independent sections (remark *Trivializations and Frames*).

#### Splitting along a section · P1

If $\pi\circ s=\mathrm{id}_M$, $y=s(p)$: $\pi_{\ast y}\circ s_{\ast p}=\mathrm{id}$, so $s_{\ast p}$ is injective and $\pi_{\ast y}$ onto; $T_yE=s_{\ast p}(T_pM)\oplus V_y$; the projection onto $V_y$ is $\mathrm{id}-s_{\ast p}\circ\pi_{\ast y}$, see Proposition [[§38 Fibrations#^prop-38-5|§38.5]]. *Source: filled in; (1) is the heart of Assignment 5, Problem 1.*

^nd-prop-38-5

- [ ] Q1 **[state]** State the three parts and the dimension formula.
- [ ] Q2 **[def]** Define the vertical space $V_y$ (Definition [[§38 Fibrations#^def-38-5|§38.5]]). For a submersion, what is it the tangent space of?
- [ ] Q3 (1) Which identity do you differentiate, and why does it give injectivity of $s_{\ast p}$ and surjectivity of $\pi_{\ast y}$?
- [ ] Q4 (2) Write $w\in T_yE$ as a sum of a vector in $s_{\ast p}(T_pM)$ and a vertical vector.
- [ ] Q5 (2) Why do the two subspaces meet only in $0$?
- [ ] Q6 (3) Check that $P=\mathrm{id}-s_{\ast p}\circ\pi_{\ast y}$ is the identity on $V_y$ and zero on $s_{\ast p}(T_pM)$.
- [ ] Q7 **[why]** Which of the two summands depends on the section $s$, and which does not? Where is this splitting used for $T^\ast M$ along the zero section?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S14 (differentiate $\pi\circ s=\mathrm{id}_M$), S7.
> - $u=s_{\ast p}(\pi_{\ast y}w)$ and $w-u\in V_y$ by (1).
> - If $w=s_{\ast p}v\in V_y$, then $v=\pi_{\ast y}w=0$.
> - $V_y=\ker\pi_{\ast y}$ is intrinsic; the horizontal complement $s_{\ast p}(T_pM)$ changes with $s$. Used in Proposition [[§52 Critical Points and the Hessian#^prop-52-8|§52.8]] ([[Differentiable Manifolds HW Drill#^hw5-3|HW5.3]]).

#### The normal bundle of a submanifold of $\mathbb{R}^n$ is a submanifold · P1

$\mathcal{N}=\{(p,v):p\in M,\ v\perp T^{\mathrm{geo}}_pM\}$ is a regular submanifold of $\mathbb{R}^{2n}$ of dimension $n$, see Proposition [[§40 The Normal Bundle of a Submanifold of Euclidean Space#^prop-40-1|§40.1]]. → drilled as [[Differentiable Manifolds HW Drill#^hw5-5|HW5.5]] (part (a)).

^nd-prop-40-1

#### Focal points of the parabola · P1

The focal points of $y=x^2$ are the image of $\mathbf r(a)=(-4a^3,3a^2+\tfrac12)$, see Example [[§40 The Normal Bundle of a Submanifold of Euclidean Space#^ex-40-1|§40.1]]. → drilled as [[Differentiable Manifolds HW Drill#^hw5-5|HW5.5]] (part (b)).

^nd-ex-40-1

#### Local sections of the Hopf fibration give trivializations · P1

For a local section $s$ of the Hopf fibration, $\Psi_s(u,\lambda)=\lambda s(u)$ is an equivariant diffeomorphism $U\times S^1\to\pi^{-1}(U)$, see Proposition [[§44 Projective Spaces and the Hopf Fibration#^prop-44-1|§44.1]]. → drilled as [[Differentiable Manifolds HW Drill#^hw4-4|HW4.4]].

^nd-prop-44-1

#### Local but not global sections of the Hopf fibration · P1

The explicit local sections $s_i$ over $U_i$ and their trivializations, see Corollary [[§44 Projective Spaces and the Hopf Fibration#^cor-44-2|§44.2]]. → drilled as [[Differentiable Manifolds HW Drill#^hw4-4|HW4.4]].

^nd-cor-44-2

### Priority 2 · stated or done in class

#### Fibres and fibrations · P2

For a fibration $\pi:M\to B$ with fibre $F$: (1) each $\phi_\alpha$ restricts to a homeomorphism $\pi^{-1}(b)\to\{b\}\times F\cong F$; (2) $\pi$ is a submersion, onto if $F\neq\emptyset$; (3) $\pi$ is an open map, see Proposition [[§38 Fibrations#^prop-38-1|§38.1]]. *Source: stated in Lecture 11 ("chain rule and stuff"); Lecture 12: "Exercise: check that these are submersions"; filled in.* **[class exercise, Lectures 11–12]**

^nd-prop-38-1

- [ ] Q1 **[state]** State the three parts.
- [ ] Q2 **[def]** Define a fibration with fibre $F$ (Definition [[§38 Fibrations#^def-38-1|§38.1]]). What does the commuting triangle $\mathrm{pr}_1\circ\phi_\alpha=\pi$ say about $\phi_\alpha(x)$?
- [ ] Q3 (1) Show that $\phi_\alpha$ maps $\pi^{-1}(b)$ onto $\{b\}\times F$: one inclusion from the triangle, the other from bijectivity.
- [ ] Q4 (1) Why is the restriction a homeomorphism for the subspace topologies, and why is $\{b\}\times F$ homeomorphic to $F$?
- [ ] Q5 (2) Fix $p$, $W=\pi^{-1}(U_\alpha)$. Why is $(\pi|_W)_{\ast p}$ onto? How do you pass from $\pi|_W$ to $\pi$?
- [ ] Q6 (2), (3) Why is $\pi$ onto when $F\neq\emptyset$, and why is it open?
- [ ] Q7 **[why]** Is the converse of (2) true: is every surjective submersion a fibration? Give the counterexample of the notes.

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S14 (differentiate the identity $\pi|_W=\mathrm{pr}_1\circ\phi_\alpha$).
> - (1) $\mathrm{pr}_1(\phi_\alpha(x))=\pi(x)=b$; conversely $x=\phi_\alpha^{-1}(b,f)$ has $\pi(x)=\mathrm{pr}_1(b,f)=b$.
> - (2) $(\phi_\alpha)_{\ast p}$ is an isomorphism and $(\mathrm{pr}_1)_\ast$ is onto (Example [[§36 Submersions#^ex-36-2|§36.2]]); then $\pi_{\ast p}\circ(\iota_W)_{\ast p}=(\iota_{U_\alpha})_\ast\circ(\pi|_W)_{\ast p}$ with $(\iota_{U_\alpha})_\ast$ an isomorphism (Lemma [[§28 Derivations and the Abstract Tangent Space#^lem-28-8|§28.8]]).
> - (3) Submersions are open (Corollary [[§36 Submersions#^cor-36-9|§36.9]]).
> - Q7: Example [[§38 Fibrations#^ex-38-1|§38.1]].

#### Fibres are copies of the model fibre · P2

For a fibration $\pi:E\to B$ with fibre $F$ and $b\in B$, $\pi^{-1}(b)$ is a regular submanifold of $E$, and $\phi_\alpha$ restricts to a diffeomorphism $\pi^{-1}(b)\to\{b\}\times F\cong F$, see Proposition [[§38 Fibrations#^prop-38-2|§38.2]]. *Source: claimed in Lecture 12 ("I claim that they are diffeomorphic to this fibre"); filled in.* **[class exercise, Lecture 12]**

^nd-prop-38-2

- [ ] Q1 **[state]** State the proposition.
- [ ] Q2 Why are $\pi^{-1}(b)\subseteq E$ and $\{b\}\times F\subseteq U_\alpha\times F$ regular submanifolds? Which structures do they carry?
- [ ] Q3 Why does $\phi_\alpha$ restrict to a bijection $\Phi:\pi^{-1}(b)\to\{b\}\times F$?
- [ ] Q4 Why is $\Phi$ smooth? Factor it through $\phi_\alpha\circ\iota$ and say which lemma lets you shrink the target to $\{b\}\times F$.
- [ ] Q5 Why is $\Phi^{-1}$ smooth? Why is $\{b\}\times F\to F$, $(b,f)\mapsto f$, a diffeomorphism?
- [ ] Q6 **[why]** Proposition [[§38 Fibrations#^prop-38-1|§38.1]](1) only gives a homeomorphism. Which two inputs upgrade it to a diffeomorphism? And why is "every fibre is a submanifold" not enough to make all fibres diffeomorphic?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S14; the key tool is Lemma [[§37 Regular Submanifolds#^lem-37-5|§37.5]](2) (maps into a submanifold).
> - Submanifolds: $\pi$ and $\mathrm{pr}_1$ are submersions (Proposition [[§38 Fibrations#^prop-38-1|§38.1]](2), Example [[§36 Submersions#^ex-36-2|§36.2]]); then Corollary [[§37 Regular Submanifolds#^cor-37-13|§37.13]].
> - $\Phi$: $\iota$ is smooth into the open set $\pi^{-1}(U_\alpha)$, then $\phi_\alpha$; values lie in $\{b\}\times F$.
> - $\Phi^{-1}$: $\phi_\alpha^{-1}\circ\iota'$ with values in $\pi^{-1}(b)$. $\{b\}\times F\cong F$ via $\mathrm{pr}_2\circ\iota'$ and the slice inclusion (Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-11|§19.11]]).
> - Q6: Example [[§38 Fibrations#^ex-38-1|§38.1]].

#### A submersion that is not a fibration · P2

$\pi:\mathbb{R}^2\setminus\{(0,1)\}\to\mathbb{R}$, $\pi(x,y)=x$, is a surjective submersion but not a fibration, see Example [[§38 Fibrations#^ex-38-1|§38.1]]. *Source: Lecture 12.*

^nd-ex-38-1

- [ ] Q1 **[state]** State the example: total space, map, and the three claims.
- [ ] Q2 Why is $\pi$ a submersion? Why is it onto?
- [ ] Q3 Describe every fibre. Which one is different?
- [ ] Q4 Suppose $\pi$ were a fibration. Which proposition forces all fibres to be homeomorphic, and which topological property gives the contradiction?
- [ ] Q5 **[why]** Which hypothesis of Ehresmann's theorem (Theorem [[§38 Fibrations#^thm-38-3|§38.3]]) fails here? Exhibit a compact $K\subseteq\mathbb{R}$ with $\pi^{-1}(K)$ not compact.

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S14 (restriction of a projection to an open set), invariants under homeomorphism.
> - $\pi=\mathrm{pr}\circ\iota_E$ with $(\iota_E)_\ast$ an isomorphism (Example [[§36 Submersions#^ex-36-1|§36.1]]); $(x,0)\mapsto x$ shows onto.
> - Fibres: vertical lines, except $\{0\}\times(\mathbb{R}\setminus\{1\})$, two half-lines.
> - Proposition [[§38 Fibrations#^prop-38-2|§38.2]]: all fibres would be diffeomorphic; but $\{1\}\times\mathbb{R}$ is connected and $\{0\}\times(\mathbb{R}\setminus\{1\})$ is not (Proposition [[§1 Point-Set Topology Review#^prop-1-7|§1.7]]).
> - Q5: $\pi^{-1}([-1,1])=([-1,1]\times\mathbb{R})\setminus\{(0,1)\}$ is unbounded (and not even closed in $\mathbb{R}^2$), hence not compact. Ehresmann is sufficient, not necessary: $\mathbb{R}^2\to\mathbb{R}$ is a fibration without being proper.

#### Ehresmann's theorem · P2

A surjective proper submersion $\pi:E\to B$ onto a connected $B$ is a fibration, see Theorem [[§38 Fibrations#^thm-38-3|§38.3]]. *Source: stated in Lecture 13, proof not given (uses connections); quote it.*

^nd-thm-38-3

- [ ] Q1 **[state]** State the theorem, with all three hypotheses.
- [ ] Q2 **[def]** Define a proper map (Definition [[§42 Embeddings#^def-42-2|§42.2]]).
- [ ] Q3 **[why]** In Example [[§38 Fibrations#^ex-38-1|§38.1]] (punctured plane), which hypothesis fails, and which conclusion fails?
- [ ] Q4 **[why]** In Example [[§38 Fibrations#^ex-38-2|§38.2]] all fibres are diffeomorphic (why?) and still $\pi$ is not a fibration. Which hypothesis fails?
- [ ] Q5 **[why]** Why is $B$ assumed connected? What can go wrong with the fibres over two components of $B$?
- [ ] Q6 How used: if $E$ is compact, $B$ connected and $\pi:E\to B$ a surjective submersion, what can you conclude, and why is such a $\pi$ proper?

> [!tip]- Hints: what to know about the statement
> - Proper: preimages of compact sets are compact; a map out of a compact space into a Hausdorff space is proper (proof of Corollary [[§42 Embeddings#^cor-42-6|§42.6]]).
> - Example [[§38 Fibrations#^ex-38-2|§38.2]]: each fibre is a plane minus two points, all diffeomorphic by affine maps; the missing points collide as $t\to0$; $\pi$ is not proper.
> - A fibration has one model fibre $F$; over different components the fibres could be different manifolds.
> - Uribe's intuition: lift paths in $B$ via a connection, flow fibre to fibre; properness lets the flow run long enough.

#### The Möbius band is a fibration · P2

For $E=(\mathbb{R}\times(-1,1))/\sim$, $(s,t)\sim(s+n,(-1)^nt)$: $E$ is a topological $2$-manifold with the two charts $\psi_a=(q|_{I_a\times(-1,1)})^{-1}$, $a\in\{0,\tfrac12\}$, forming a smooth atlas; $\pi[s,t]=[s]$ is smooth and $\phi_a[s,t]=([s],t)$ are local trivializations; on the overlap they differ by $t\mapsto-t$ on one arc, see Proposition [[§39 Examples of Fibrations#^prop-39-1|§39.1]]. *Source: Lecture 12 gave the picture (Example [[§39 Examples of Fibrations#^ex-39-2|§39.2]]); the proof is filled in.*

^nd-prop-39-1

- [ ] Q1 **[state]** State the three parts, with $I_a=(a,a+1)$, $U_a$ and $W_a$.
- [ ] Q2 Why is the quotient map $q$ open? Which group action is behind the relation?
- [ ] Q3 Why is $q$ restricted to $I_a\times(-1,1)$ a homeomorphism onto the open set $W_a$?
- [ ] Q4 Why is $E$ Hausdorff and second countable? (Which two points need a separate argument?)
- [ ] Q5 Compute the transition map $\psi_{1/2}\circ\psi_0^{-1}$ on both arcs. Why is it smooth with smooth inverse?
- [ ] Q6 Why is $\pi$ smooth and $\pi^{-1}(U_a)=W_a$? Why is $\phi_a$ a diffeomorphism with $\mathrm{pr}_1\circ\phi_a=\pi$?
- [ ] Q7 **[why]** The two trivializations differ by a sign on one arc. Does that alone prove that $E$ is not the product $S^1\times(-1,1)$? What does the notes' picture use instead?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S4 (quotient → manifold), S1.
> - $\sim$ is the orbit relation of $\mathbb{Z}$ acting by $g_n(s,t)=(s+n,(-1)^nt)$; orbit relations are open (Lemma [[§13 Group Actions and Orbit Spaces#^lem-13-3|§13.3]]).
> - Injective on $I_a\times(-1,1)$ because $|s'-s|<1$ forces $n=0$.
> - Transition: $(s,t)$ for $\tfrac12<s<1$, $(s+1,-t)$ for $0<s<\tfrac12$.
> - $\phi_a=(\chi_a^{-1}\times\mathrm{id})\circ\psi_a$. Non-triviality is stated, not proved: one boundary curve versus two.

#### Spheres cover projective spaces · P2

$\pi:S^n\to\mathbb{RP}^n$, $x\mapsto[x]$, is a local diffeomorphism and exactly two-to-one, see Example [[§44 Projective Spaces and the Hopf Fibration#^ex-44-1|§44.1]]. *Source: stated in Lecture 10 as an example, without proof; filled in.* **[class exercise, Lecture 10]**

^nd-ex-44-1

- [ ] Q1 **[state]** State the example, including the definition of a local diffeomorphism (Definition [[§35 Local Diffeomorphisms#^def-35-1|§35.1]]).
- [ ] Q2 Define the open hemispheres $U_i^\varepsilon$. Why do they cover $S^n$, and why does $\pi$ map $U_i^\varepsilon$ bijectively onto $U_i=\{x_i\neq0\}$?
- [ ] Q3 Write $h=\varphi_i\circ\pi$ on $U_i^\varepsilon$ and its inverse $\kappa(y)=\varepsilon\hat y/|\hat y|$. Why are both smooth (which lemma for maps out of and into $S^n$)?
- [ ] Q4 Conclude that $\pi|_{U_i^\varepsilon}$ is a diffeomorphism onto $U_i$ and that $\pi$ is smooth.
- [ ] Q5 Why is every fibre exactly $\{x,-x\}$?
- [ ] Q6 **[why]** $\pi$ is a surjective local diffeomorphism. Why is it not a diffeomorphism? Which hypothesis of Corollary [[§35 Local Diffeomorphisms#^cor-35-3|§35.3]] fails?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S1 (compute in the standard charts of Corollary [[§18 Projective Spaces as Smooth Manifolds#^cor-18-5|§18.5]]).
> - A line $[x]$ with $x_i\neq0$ meets $S^n$ in $\pm x/|x|$, exactly one of which lies in $U_i^\varepsilon$.
> - $h(x)=(x_k/x_i)_{k\neq i}$ is smooth on $\{x_i\neq0\}$; $\kappa$ is smooth since $|\hat y|\ge1$; Lemma [[§20 Manifolds in Euclidean Space#^lem-20-3|§20.3]].
> - $\pi|_{U_i^\varepsilon}=\varphi_i^{-1}\circ h$. Two-to-one: $y=\lambda x$ with $|\lambda|=1$.

#### The projection $S^{2n+1}\to\mathbb{CP}^n$ is a submersion · P2

The quotient map $S^{2n+1}\to\mathbb{CP}^n$ is a submersion, see Example [[§44 Projective Spaces and the Hopf Fibration#^ex-44-2|§44.2]]. *Source: stated in Lecture 10 without proof; the notes deduce it from the Hopf fibration.* **[class exercise, Lecture 10]**

^nd-ex-44-2

- [ ] Q1 **[state]** State the claim. Are the dimensions consistent with a submersion?
- [ ] Q2 Which two results of the notes give it at once?
- [ ] Q3 Describe the fibres. Are they regular submanifolds, and of what dimension?
- [ ] Q4 **[why]** Why is this map not a local diffeomorphism, unlike $S^n\to\mathbb{RP}^n$?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: a fibration is a submersion.
> - Example [[§44 Projective Spaces and the Hopf Fibration#^ex-44-3|§44.3]] (it is a fibration) and Proposition [[§38 Fibrations#^prop-38-1|§38.1]](2).
> - Fibres are the circles $\{\lambda z:|\lambda|=1\}$ (Corollary [[§37 Regular Submanifolds#^cor-37-13|§37.13]]): dimension $(2n+1)-2n=1$.
> - Dimensions differ, so the differential cannot be bijective.

#### The Hopf fibration · P2

$\pi:S^{2n+1}\to\mathbb{CP}^n$, $\pi(z)=[z]$, is a fibration with fibre $S^1$, with local trivializations $\phi_j(z)=([z],z_j/|z_j|)$ over $U_j=\{z_j\neq0\}$, see Example [[§44 Projective Spaces and the Hopf Fibration#^ex-44-3|§44.3]]. *Source: claimed in Lecture 11 ("We claim that this projection that we work with in homework is a fibration. What do you think the fibre is?"); the trivialization is filled in.* **[class exercise, Lecture 11]**

^nd-ex-44-3

- [ ] Q1 **[state]** State the example: fibre, cover, trivializations, and the inverse $([w],\lambda)\mapsto\lambda\hat w/|\hat w|$.
- [ ] Q2 Why do the $U_j$ cover $\mathbb{CP}^n$, and why is $\pi^{-1}(U_j)$ open in $S^{2n+1}$?
- [ ] Q3 Why is $\phi_j$ smooth? Treat its two components separately.
- [ ] Q4 Why is the proposed inverse $\psi_j$ smooth, with values in $\pi^{-1}(U_j)$?
- [ ] Q5 Check $\psi_j\circ\phi_j=\mathrm{id}$, $\phi_j\circ\psi_j=\mathrm{id}$ and $\mathrm{pr}_1\circ\phi_j=\pi$.
- [ ] Q6 **[why]** The Hopf fibration has local sections but no global one (for $n\ge1$). If it had a global section, what would Proposition [[§44 Projective Spaces and the Hopf Fibration#^prop-44-1|§44.1]] give? Why is that impossible (stated, not proved)?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S1 (the charts $\varphi_j$ of $\mathbb{CP}^n$, Proposition [[§18 Projective Spaces as Smooth Manifolds#^prop-18-1|§18.1]]), and Lemma [[§20 Manifolds in Euclidean Space#^lem-20-3|§20.3]] for maps out of and into level sets.
> - First component: $\varphi_j\circ\pi(z)=(z_k/z_j)_{k\neq j}$; second: $z_j/|z_j|$, smooth where $z_j\neq0$, values in $S^1$.
> - $\psi_j$ in the chart is $(u,\lambda)\mapsto\lambda\hat w(u)/|\hat w(u)|$ with $|\hat w(u)|\ge1$.
> - $\psi_j(\phi_j(z))=\frac{z_j}{|z_j|}\cdot\frac{z}{z_j}\cdot\frac{|z_j|}{|z|}=z$.
> - Q6: a global trivialization $S^{2n+1}\cong\mathbb{CP}^n\times S^1$ (the fundamental group rules it out).

### Priority 3 · filled in, using a technique the homework drills

#### The normal bundle is a fibration · P3

Over a chart $(U,\varphi)$ of $\mathbb{R}^n$ adapted to $M$, with $J(q)=G'(q)$, $G=(x^{m+1},\dots,x^n)$: $J(q)J(q)^{\mathsf T}$ is invertible on $U$, $\Phi_U(q,v)=(q,(JJ^{\mathsf T})^{-1}Jv)$ is a diffeomorphism $\pi^{-1}(U\cap M)\to(U\cap M)\times\mathbb{R}^{n-m}$ with inverse $(q,c)\mapsto(q,J^{\mathsf T}c)$, linear on fibres; so $\pi:\mathcal{N}\to M$ is a fibration with fibre $\mathbb{R}^{n-m}$, see Proposition [[§40 The Normal Bundle of a Submanifold of Euclidean Space#^prop-40-2|§40.2]]. *Source: filled in (not from the assignment).*

^nd-prop-40-2

- [ ] Q1 **[state]** State the three parts.
- [ ] Q2 Why is $\pi$ smooth, and why is $\pi^{-1}(U\cap M)=\mathcal{N}\cap(U\times\mathbb{R}^n)$ open in $\mathcal{N}$?
- [ ] Q3 (1) Why do the gradients $\nabla G^s(q)$ form a basis of $(T^{\mathrm{geo}}_qM)^\perp$? Why is $JJ^{\mathsf T}$ invertible at every $q\in U$?
- [ ] Q4 (2) Check that $\Phi_U$ and $\Theta_U(q,c)=(q,J^{\mathsf T}c)$ land in the right sets and are mutually inverse.
- [ ] Q5 (2) Why is $\Phi_U$ smooth? Why is $\Theta_U$ smooth as a map into $\mathcal{N}$?
- [ ] Q6 (3) Assemble the fibration: open cover, trivializations, commuting triangle.
- [ ] Q7 **[why]** Where is it used that $J(q)$ has rank $n-m$ at every $q\in U$, and not only at points of $M$?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S1, S7; recipe of the remark *Where Explicit Trivializations Come From* (a smoothly varying basis of each fibre).
> - (1) Lemma [[§37 Regular Submanifolds#^lem-37-10|§37.10]](4); $JJ^{\mathsf T}c=0$ gives $|J^{\mathsf T}c|^2=0$, and $c\mapsto J^{\mathsf T}c$ is injective.
> - (2) $(JJ^{\mathsf T})^{-1}JJ^{\mathsf T}c=c$; for $v=J^{\mathsf T}c$, $J^{\mathsf T}(JJ^{\mathsf T})^{-1}Jv=v$.
> - Smooth: entries of $(JJ^{\mathsf T})^{-1}$ by the cofactor formula; $\Theta_U$ smooth into $\mathbb{R}^{2n}$ with values in $\mathcal{N}$, then Lemma [[§37 Regular Submanifolds#^lem-37-5|§37.5]](2).
> - Q7: the formula $\hat\Phi$ is written on all of $U\times\mathbb{R}^n$, which needs $\det(JJ^{\mathsf T})\neq0$ on $U$.

# T9. Immersions and embeddings

## Definitions T9

### Priority 1 · homework (directly or extended)

#### Locally closed subset · P1

$S \subseteq N$ is locally closed if each point of $S$ has an open $V \subseteq N$ with $S \cap V$ closed in $V$; equivalently $S$ is closed in an open subset of $N$, see Definition [[§42 Embeddings#^def-42-3|§42.3]]. *Source: notes (prompted by Assignment 4, Problem 5).*

^nd-def-42-3

- [ ] Q1 **[def]** State the definition in both forms; prove they agree.
- [ ] Q2 **[use]** Why is every regular submanifold locally closed? Use an adapted chart.
- [ ] Q3 **[why]** Why is the image of the irrational line not locally closed in $T^2$, and what does that prove?
- [ ] Q4 **[example]** Is an open disc in $\mathbb{R}^2$ locally closed? Is $\mathbb{Q} \subseteq \mathbb{R}$?

> [!tip]- Hints: where it lives, examples
> - Definition [[§42 Embeddings#^def-42-3|§42.3]]; Q2: Proposition [[§42 Embeddings#^prop-42-7|§42.7]].
> - Q3: it is dense, so it would be open (Corollary [[§42 Embeddings#^cor-42-8|§42.8]]); hence not a regular submanifold. Q4: yes (open); no (dense with empty interior).

### Priority 2 · stated or done in class

#### Immersion (local picture) · P2

$F$ is an immersion at $p$ if $F_{\ast p}$ is injective (forcing $m \le n$), see Definition [[§41 Immersions#^def-41-1|§41.1]]. *Source: Lecture 13.*

^nd-def-41-1

- [ ] Q1 **[def]** State the definition, and the local normal form at a point where $F$ is an immersion.
- [ ] Q2 **[use]** In the normal-form charts, why is $F|_U$ injective with $F(U)$ a regular submanifold? So what is an immersion locally?
- [ ] Q3 **[why]** "Locally an embedding" does not make $F(M)$ a submanifold. Give the two curves of the notes that show what goes wrong globally, and the property each one lacks.
- [ ] Q4 **[why]** Why is an immersion that is open onto its image enough for $F(M)$ to be a regular submanifold, even without injectivity? Give a non-injective example.

> [!tip]- Hints: where it lives, examples
> - Definition [[§41 Immersions#^def-41-1|§41.1]] (= Definition [[§36 Submersions#^def-36-2|§36.2]]); Theorem [[§41 Immersions#^thm-41-1|§41.1]], Corollary [[§41 Immersions#^cor-41-2|§41.2]].
> - Q3: Example [[§41 Immersions#^ex-41-1|§41.1]] (not injective, X-shaped image), Example [[§41 Immersions#^ex-41-2|§41.2]] (injective, T-shaped image: not a homeomorphism onto the image).
> - Q4: Proposition [[§42 Embeddings#^prop-42-2|§42.2]]; the remark *Where Is Injectivity Used?* in [[§42 Embeddings|§42]] ($\mathbb{R} \to S^1$, $S^2 \to \mathbb{RP}^2$).

#### Embedding · P2

A smooth immersion $F : M \to N$ that is a homeomorphism onto $F(M)$ with the subspace topology, see Definition [[§42 Embeddings#^def-42-1|§42.1]]. *Source: Lecture 14.*

^nd-def-42-1

- [ ] Q1 **[def]** State the definition. Why is "injective" redundant in it?
- [ ] Q2 **[use]** What is the image of an embedding, and how is $F : M \to F(M)$ then related to the induced structure on $F(M)$?
- [ ] Q3 **[why]** Drop "homeomorphism onto the image": give an injective immersion that is not an embedding, and point to the exact failure (an open set of $M$ whose image is not open in $F(M)$).
- [ ] Q4 **[why]** Drop "immersion": give a smooth homeomorphism onto its image that is not an embedding.
- [ ] Q5 **[use]** State two sufficient conditions for an injective immersion to be an embedding (properness, compactness), and when an embedding has closed image.

> [!tip]- Hints: where it lives, examples
> - Definition [[§42 Embeddings#^def-42-1|§42.1]]; Q2: Theorem [[§42 Embeddings#^thm-42-1|§42.1]], Corollary [[§42 Embeddings#^cor-42-3|§42.3]].
> - Q3: Example [[§41 Immersions#^ex-41-2|§41.2]], Proposition [[§42 Embeddings#^prop-42-12|§42.12]] (irrational line, → drilled as [[Differentiable Manifolds HW Drill#^hw4-5|HW4.5]]), Example [[§42 Embeddings#^ex-42-1|§42.1]] (figure-eight).
> - Q4: $t \mapsto (t^3, 0)$ onto the $x$-axis, or the cusp $t \mapsto (t^2, t^3)$ (not immersions at $0$).
> - Q5: Theorem [[§42 Embeddings#^thm-42-5|§42.5]], Corollary [[§42 Embeddings#^cor-42-6|§42.6]], Proposition [[§42 Embeddings#^prop-42-9|§42.9]]. Example: every section is a closed embedding, Proposition [[§42 Embeddings#^prop-42-10|§42.10]] → drilled as [[Differentiable Manifolds HW Drill#^hw5-1|HW5.1]].

#### Proper map · P2

A continuous $F$ with $F^{-1}(K)$ compact for every compact $K$, see Definition [[§42 Embeddings#^def-42-2|§42.2]]. *Source: Lecture 14.*

^nd-def-42-2

- [ ] Q1 **[def]** State the definition.
- [ ] Q2 **[use]** Why is a proper map into a manifold closed? Which property of manifolds is used?
- [ ] Q3 **[use]** How does properness turn an injective immersion into an embedding?
- [ ] Q4 **[why]** Is the irrational line $\mathbb{R} \to T^2$ proper? Is the inclusion $(0, 1) \to \mathbb{R}$? Which conclusion fails for each?
- [ ] Q5 **[why]** Which hypothesis of Ehresmann's theorem is properness, and what does the punctured-plane projection show about dropping it?

> [!tip]- Hints: where it lives, examples
> - Definition [[§42 Embeddings#^def-42-2|§42.2]] (= Definition [[§13 Group Actions and Orbit Spaces#^def-13-6|§13.6]]); Q2: Proposition [[§42 Embeddings#^prop-42-4|§42.4]] (manifolds are locally compact, Proposition [[§2 Topological Manifolds#^prop-2-12|§2.12]]).
> - Q3: Theorem [[§42 Embeddings#^thm-42-5|§42.5]] (closed map onto the image ⇒ homeomorphism onto the image). Q4: no ($T^2$ compact, $\mathbb{R}$ not); no (image not closed, Proposition [[§42 Embeddings#^prop-42-9|§42.9]]).
> - Q5: Theorem [[§38 Fibrations#^thm-38-3|§38.3]], Example [[§38 Fibrations#^ex-38-1|§38.1]].

#### Immersed submanifold · P2

$S \subseteq N$ with some manifold topology and smooth structure making the inclusion a smooth immersion, see Definition [[§42 Embeddings#^def-42-4|§42.4]]. *Source: notes (Lecture 14 material).*

^nd-def-42-4

- [ ] Q1 **[def]** State the definition. Which topology is $S$ allowed to have?
- [ ] Q2 **[use]** Show the image of an injective immersion is an immersed submanifold. Is the structure unique?
- [ ] Q3 **[why]** When is an immersed submanifold a regular one? State the three equivalent conditions.
- [ ] Q4 **[example]** Give an immersed submanifold of $T^2$ that is not regular, and one of $\mathbb{R}^2$.

> [!tip]- Hints: where it lives, examples
> - Definition [[§42 Embeddings#^def-42-4|§42.4]]; Q2: Proposition [[§42 Embeddings#^prop-42-13|§42.13]]; every regular submanifold is one, Proposition [[§42 Embeddings#^prop-42-14|§42.14]].
> - Q3: Proposition [[§42 Embeddings#^prop-42-15|§42.15]]. Q4: Example [[§42 Embeddings#^ex-42-1|§42.1]].

## Proofs T9

### Priority 1 · homework (directly or extended)

#### Images of embeddings are locally closed · P1

Every regular submanifold of $N$, in particular the image of an embedding, is locally closed: closed in some open subset of $N$ containing it, see Proposition [[§42 Embeddings#^prop-42-7|§42.7]]. *Source: filled in (prompted by Assignment 4, Problem 5).*

^nd-prop-42-7

- [ ] Q1 **[state]** State the proposition. **[def]** Define a locally closed subset (Definition [[§42 Embeddings#^def-42-3|§42.3]]) and its equivalent form.
- [ ] Q2 In an adapted chart $(V,\psi)$, why is $S\cap V$ closed in $V$?
- [ ] Q3 With $U$ the union of these $V$'s, why is $U\setminus S$ open, so that $S$ is closed in $U$?
- [ ] Q4 Prove the converse in the equivalence.
- [ ] Q5 **[why]** Is every regular submanifold closed in $N$? Give an embedding with non-closed image.

> [!tip]- Hints: route of the proof in the notes
> - $S\cap V$ is the preimage of $\{\vec 0\}$ under the continuous $(y^{m+1},\dots,y^n)$.
> - $V\setminus S$ is open in $V$, hence in $N$.
> - Q5: an open interval embedded in $\mathbb{R}^2$.

#### Sections are closed embeddings · P1

If $\pi\circ s=\mathrm{id}_M$, then $s$ is an embedding with closed image, see Proposition [[§42 Embeddings#^prop-42-10|§42.10]]. → drilled as [[Differentiable Manifolds HW Drill#^hw5-1|HW5.1]].

^nd-prop-42-10

#### The irrational line on the torus · P1

$\gamma(t)=(e^{2\pi it},e^{2\pi i\alpha t})$, $\alpha$ irrational, is an injective immersion with dense image, not an embedding, see Proposition [[§42 Embeddings#^prop-42-12|§42.12]]. → drilled as [[Differentiable Manifolds HW Drill#^hw4-5|HW4.5]].

^nd-prop-42-12

### Priority 2 · stated or done in class

#### Local normal form for immersions · P2

If $F:M\to N$ is an immersion at $p$ ($m\le n$), there are charts $(U,\varphi)$ at $p$ and $(V,\psi)$ at $F(p)$ with $F(U)\subseteq V$ and $\psi\circ F\circ\varphi^{-1}(r)=(r,\vec 0)$, see Theorem [[§41 Immersions#^thm-41-1|§41.1]]. *Source: stated in Lecture 13, proved in Lecture 14; details completed in the notes.*

^nd-thm-41-1

- [ ] Q1 **[state]** State the theorem. **[def]** Define an immersion at $p$ (Definition [[§41 Immersions#^def-41-1|§41.1]]) and say why it forces $m\le n$.
- [ ] Q2 Start with charts $(U_0,\varphi_0)$ at $p$ and $(V_0,\psi)$ at $F(p)$ with $F(U_0)\subseteq V_0$. What is the size of the Jacobian $J=[\partial F^j/\partial x^i(p)]$, and why does it have rank $m$?
- [ ] Q3 Why may you reorder the $y^j$ so that the top $m\times m$ block $A$ of $J$ is invertible? Why is the reordered $\psi$ still a smooth chart?
- [ ] Q4 Why is $\tilde\varphi=(F^1,\dots,F^m)$ a chart on a smaller neighbourhood $U$ of $p$? Which theorem, applied to which map?
- [ ] Q5 In the charts $\tilde\varphi$ and $\psi$, show $\hat F(r)=(r,G(r))$. What is $G$?
- [ ] Q6 Define the straightening $\Sigma(y_a,y_b)=(y_a,y_b-G(y_a))$. Why is $\tilde\psi=\Sigma\circ\psi$ a chart on a suitable $V$ with $F(U)\subseteq V$, and why is $\tilde\psi\circ F\circ\tilde\varphi^{-1}(r)=(r,\vec 0)$?
- [ ] Q7 **[why]** Compare with the submersion normal form (Theorem [[§36 Submersions#^thm-36-6|§36.6]]): which chart is changed there, and why must the chart on $N$ change here? What does the irrational line show about how *local* this normal form is?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S8 (normal forms give charts), inverse function theorem.
> - $J$ is $n\times m$; $F_{\ast p}$ injective gives rank $m$ (rank–nullity), so $m$ rows are independent.
> - Permutation of coordinates: Lemma [[§17 Differentiable Structures#^lem-17-6|§17.6]](2).
> - The Jacobian of $(F^1,\dots,F^m)\circ\varphi_0^{-1}$ at $\varphi_0(p)$ is $A$; Theorem [[§35 Local Diffeomorphisms#^thm-35-1|§35.1]] and Lemma [[§36 Submersions#^lem-36-5|§36.5]].
> - $\Sigma$ has inverse $(y_a,z)\mapsto(y_a,z+G(y_a))$ on $\tilde\varphi(U)\times\mathbb{R}^{n-m}$; take $V=\psi^{-1}(\tilde\varphi(U)\times\mathbb{R}^{n-m})\cap V_0$.

#### The local image of an immersion · P2

In the charts of the normal form, $F|_U$ is injective and $F(U)$ is a regular submanifold of $N$ of codimension $n-m$, see Corollary [[§41 Immersions#^cor-41-2|§41.2]]. *Source: idea in Lecture 13 ("possibly after restricting $U$"); completed in the notes by shrinking $V$.*

^nd-cor-41-2

- [ ] Q1 **[state]** State the corollary.
- [ ] Q2 Why is $F|_U$ injective? Use $\psi(F(u))=(\varphi(u),\vec 0)$.
- [ ] Q3 Define $V'=\{q\in V:(y^1(q),\dots,y^m(q))\in\varphi(U)\}$. Why is it open, and why does it contain $F(U)$?
- [ ] Q4 Prove $F(U)=\{q\in V':y^{m+1}(q)=\dots=y^n(q)=0\}$ (both inclusions).
- [ ] Q5 **[why]** What was Uribe's worry, and why does passing from $V$ to $V'$ remove it? Why does this not show that the whole image $F(M)$ is a submanifold?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S8.
> - Injective: $\varphi$ and $\psi$ are injective.
> - $V'=(\mathrm{pr}\circ\psi)^{-1}(\varphi(U))$.
> - "⊇": $\psi(q)=(r,\vec 0)=\tilde F(r)=\psi(F(\varphi^{-1}(r)))$, and $\psi$ is injective.
> - Points of $\psi(V)\cap(\mathbb{R}^m\times\{0\})$ with first block outside $\varphi(U)$ are removed by $V'$; other parts of $F(M)$ may still enter $V'$ (Theorem [[§42 Embeddings#^thm-42-1|§42.1]]).

#### An immersion that crosses itself · P2

$\gamma(t)=(t^2-1,t^3-t)$ is an immersion $\mathbb{R}\to\mathbb{R}^2$, not injective, whose image is not a regular submanifold, see Example [[§41 Immersions#^ex-41-1|§41.1]]. *Source: Lecture 13 (a curve drawn crossing itself); the curve and the full argument are filled in.*

^nd-ex-41-1

- [ ] Q1 **[state]** State the three claims.
- [ ] Q2 Why is $\gamma$ an immersion? Compute $\gamma_{\ast t}(\partial/\partial r|_t)$.
- [ ] Q3 Which two parameters map to the origin?
- [ ] Q4 Suppose the image $C$ were a regular submanifold of codimension $k$. Why would $\iota_{\ast0}(T_0C)$ contain $\gamma'(1)$ and $\gamma'(-1)$, and what does that force on $k$?
- [ ] Q5 Why is $k=0$ impossible here?
- [ ] Q6 **[why]** Uribe's argument: "remove the point from an X". Which invariant of the image near $0$ distinguishes it from a $1$-manifold?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S10 (velocities), S1.
> - $\gamma'(t)=(2t,3t^2-1)$ never vanishes.
> - $\gamma=\iota\circ c$ with $c$ smooth into $C$ (Lemma [[§37 Regular Submanifolds#^lem-37-5|§37.5]](2)); $(\mp2,2)$ are independent, so $\dim\iota_{\ast0}(T_0C)=2$, $k=0$.
> - $k=0$ means an open $U\ni0$ lies in $C$ (Proposition [[§37 Regular Submanifolds#^prop-37-4|§37.4]]), but $(0,s)\notin C$ for $s\neq0$.
> - Removing the crossing point leaves four components locally, a point of an interval leaves two.

#### An injective immersion that is not a homeomorphism onto its image · P2

An injective immersion $\gamma:(a,b)\to\mathbb{R}^2$ whose end returns to a point $P=\gamma(t_0)$ of its image is not a homeomorphism onto its image, see Example [[§41 Immersions#^ex-41-2|§41.2]]. *Source: Lecture 13 ("making a hook with a piece of wire"); the argument is filled in.*

^nd-ex-41-2

- [ ] Q1 **[state]** State the example.
- [ ] Q2 Why is $\gamma$ a bijection onto $\gamma((a,b))$, and which topology does the image carry?
- [ ] Q3 Take $t_k\to b$. Why does $\gamma(t_k)\to P$ in the image?
- [ ] Q4 Why does this show that $\gamma^{-1}$ is not continuous at $P$?
- [ ] Q5 **[why]** Is the image a regular submanifold? What does it look like near $P$, and what does Lee's figure-eight $\beta(t)=(\sin2t,\sin t)$ add?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S14 (sequences).
> - Every open set of the image containing $P$ is $O\cap\gamma((a,b))$ with $O$ open in $\mathbb{R}^2$.
> - $\gamma^{-1}(\gamma(t_k))=t_k\to b\neq t_0=\gamma^{-1}(P)$.
> - Near $P$ the image is a T (three pieces after removing $P$); the figure-eight gives an X.

#### The image of an embedding is a regular submanifold · P2

If $F:M\to N$ is an embedding, $F(M)$ is a regular submanifold of $N$ of codimension $n-m$, see Theorem [[§42 Embeddings#^thm-42-1|§42.1]]. *Source: Lecture 14; the final equality completed with Corollary [[§41 Immersions#^cor-41-2|§41.2]].*

^nd-thm-42-1

- [ ] Q1 **[state]** State the theorem. **[def]** Define an embedding (Definition [[§42 Embeddings#^def-42-1|§42.1]]).
- [ ] Q2 What must be produced at a point $q=F(p)$ of $F(M)$?
- [ ] Q3 From the normal form and Corollary [[§41 Immersions#^cor-41-2|§41.2]], what does $(\ast)$ say about $F(U)$? Why is it not yet a statement about $F(M)\cap V'$?
- [ ] Q4 The key step: why is $F(U)$ open in $F(M)$, and what open $W\subseteq N$ does that give?
- [ ] Q5 Shrink to $V'\cap W$: prove $F(M)\cap(V'\cap W)=\{x\in V'\cap W:y^{m+1}(x)=\dots=y^n(x)=0\}$.
- [ ] Q6 **[why]** Where is the homeomorphism hypothesis used, and is injectivity used at all? Which example shows the theorem fails for an injective immersion?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S8 (normal forms give adapted charts).
> - $(\ast)$: $F(U)=\{x\in V':y^{m+1}(x)=\dots=y^n(x)=0\}$; other pieces of $F(M)$ may pass through $V'$.
> - Homeomorphisms are open, so $F(U)=W\cap F(M)$ (subspace topology).
> - $F(M)\cap(V'\cap W)=(F(M)\cap W)\cap V'=F(U)$.
> - Only openness of $F$ onto its image is used (remark *Where Is Injectivity Used?*, Proposition [[§42 Embeddings#^prop-42-2|§42.2]]); fails for the irrational line (Proposition [[§42 Embeddings#^prop-42-12|§42.12]]).

#### Immersions that are open onto their images · P2

If $F:M\to N$ is an immersion and $F:M\to F(M)$ is open (subspace topology), then $F(M)$ is a regular submanifold of codimension $n-m$; $F$ need not be injective, see Proposition [[§42 Embeddings#^prop-42-2|§42.2]]. *Source: the class discussion in Lecture 14, confirmed in Uribe's follow-up email.*

^nd-prop-42-2

- [ ] Q1 **[state]** State the proposition.
- [ ] Q2 Which two ingredients of the proof of Theorem [[§42 Embeddings#^thm-42-1|§42.1]] are used, and which step changes its justification?
- [ ] Q3 Why does neither the normal form nor Corollary [[§41 Immersions#^cor-41-2|§41.2]] use injectivity of $F$?
- [ ] Q4 Check the example $t\mapsto(\cos t,\sin t)$: immersion, open onto $S^1$, not injective.
- [ ] Q5 **[why]** Show the figure-eight $\beta$ is not open onto its image: which open set of $(-\pi,\pi)$ has non-open image?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S8.
> - Ingredients: the normal form, and $F(U)$ open in $F(M)$.
> - The injectivity used in Corollary [[§41 Immersions#^cor-41-2|§41.2]] is that of the chart $\psi$.
> - $\mathbb{R}\to S^1$ is a local diffeomorphism onto $S^1$, hence open.
> - $\beta((-\pi/2,\pi/2))$: every neighbourhood of $(0,0)$ contains $\beta(t)$ for $t$ near $\pm\pi$.

#### An embedding is a diffeomorphism onto its image · P2

If $F:M\to N$ is an embedding, then $F:M\to F(M)$ is a diffeomorphism, $F(M)$ with its induced structure, see Corollary [[§42 Embeddings#^cor-42-3|§42.3]]. *Source: stated in Lecture 14 ("an embedding restricts to a diffeomorphism between $M$ and the image"); filled in.* **[class exercise, Lecture 14]**

^nd-cor-42-3

- [ ] Q1 **[state]** State the corollary. What is the dimension of $F(M)$?
- [ ] Q2 Why is $\bar F:M\to F(M)$ smooth?
- [ ] Q3 Why is $\bar F$ an immersion? Use $F=\iota\circ\bar F$.
- [ ] Q4 Why is $\bar F$ a local diffeomorphism?
- [ ] Q5 Why is $\bar F$ a diffeomorphism?
- [ ] Q6 **[why]** For an injective immersion that is not an embedding (the irrational line), which step breaks: is $F(M)$ even a manifold in the subspace topology?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S7 (dimensions), Lemma [[§37 Regular Submanifolds#^lem-37-5|§37.5]](2).
> - $F(M)$ is a regular submanifold of dimension $m$ (Theorem [[§42 Embeddings#^thm-42-1|§42.1]]).
> - $F_{\ast p}=\iota_{\ast F(p)}\circ\bar F_{\ast p}$ is injective, so $\bar F_{\ast p}$ is.
> - Equal dimensions: Proposition [[§36 Submersions#^prop-36-1|§36.1]](3); bijective local diffeomorphism: Corollary [[§35 Local Diffeomorphisms#^cor-35-3|§35.3]].
> - Q6: the image is not a regular submanifold (Example [[§42 Embeddings#^ex-42-1|§42.1]]).

#### Proper maps into manifolds are closed · P2

A continuous proper map $F:M\to N$ into a topological manifold is closed, see Proposition [[§42 Embeddings#^prop-42-4|§42.4]]. *Source: Lecture 14 ("you go back and forth literally"); Claim 2 not finished in lecture, "you can check the second claim"; completed in the notes.* **[class exercise, Lecture 14]**

^nd-prop-42-4

- [ ] Q1 **[state]** State the proposition. **[def]** Define a proper map (Definition [[§42 Embeddings#^def-42-2|§42.2]]).
- [ ] Q2 What has to be shown about $\overline{F(C)}$ for $C\subseteq M$ closed?
- [ ] Q3 Claim 1: for $K\subseteq N$ compact, why is $F(C)\cap K$ closed? Prove $F(C\cap F^{-1}(K))=F(C)\cap K$.
- [ ] Q4 Claim 2: for $q\in\overline{F(C)}$ and $V\ni q$ with compact closure, why is $q\in\overline{F(C)\cap\overline V}$?
- [ ] Q5 Conclude that $q\in F(C)$.
- [ ] Q6 **[why]** Which properties of $N$ are used, and at which steps?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S13 (compactness upgrades local to global).
> - Claim 1: $C\cap F^{-1}(K)$ is closed in the compact $F^{-1}(K)$, so compact; its image is compact, hence closed in the Hausdorff $N$ (Proposition [[§1 Point-Set Topology Review#^prop-1-8|§1.8]]).
> - Claim 2: any open $O\ni q$ gives $O\cap V\ni q$, which meets $F(C)$.
> - Conclusion: Claim 1 with $K=\overline V$.
> - $N$ Hausdorff (compact ⇒ closed) and locally compact (Proposition [[§2 Topological Manifolds#^prop-2-12|§2.12]]).

#### Injective proper immersions are embeddings · P2

An injective proper immersion $F:M\to N$ is an embedding, see Theorem [[§42 Embeddings#^thm-42-5|§42.5]]. *Source: Lecture 14 reduced it to Proposition [[§42 Embeddings#^prop-42-4|§42.4]]; the last step is filled in.*

^nd-thm-42-5

- [ ] Q1 **[state]** State the theorem.
- [ ] Q2 What remains to be shown, given that $F$ is an immersion?
- [ ] Q3 Why is $F:M\to F(M)$ a continuous bijection?
- [ ] Q4 Let $G$ be its inverse. Why is $G^{-1}(C)=F(C)$ closed in $F(M)$ for $C$ closed in $M$?
- [ ] Q5 **[why]** Give an injective immersion that is not proper and not an embedding. Show it is not proper.

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S13.
> - Continuity of the inverse via closed sets: $F(C)$ is closed in $N$ (Proposition [[§42 Embeddings#^prop-42-4|§42.4]]), so $F(C)=F(C)\cap F(M)$ is closed in $F(M)$.
> - Q5: the figure-eight $\beta$ on $(-\pi,\pi)$: the preimage of its compact image is $(-\pi,\pi)$; or the irrational line.

#### Injective immersions of compact manifolds · P2

If $M$ is compact, every injective immersion $F:M\to N$ is an embedding, see Corollary [[§42 Embeddings#^cor-42-6|§42.6]]. *Source: Uribe's follow-up email ("$F$ is proper if $M$ is compact, a fact that can be very useful!"); filled in.*

^nd-cor-42-6

- [ ] Q1 **[state]** State the corollary.
- [ ] Q2 Why is every continuous map from a compact $M$ to a Hausdorff $N$ proper?
- [ ] Q3 Which theorem finishes the proof?
- [ ] Q4 **[why]** Is compactness of the *target* enough instead? Use the irrational line $\mathbb{R}\to T^2$.

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S13.
> - $K$ compact in $N$ ⇒ closed ⇒ $F^{-1}(K)$ closed in compact $M$ ⇒ compact (Proposition [[§1 Point-Set Topology Review#^prop-1-8|§1.8]]).
> - Theorem [[§42 Embeddings#^thm-42-5|§42.5]].
> - $T^2$ is compact, the irrational line is an injective immersion, and it is not an embedding (Proposition [[§42 Embeddings#^prop-42-12|§42.12]]).

#### Closed embeddings are the proper ones · P2

An embedding is proper if and only if its image is closed; an injective proper immersion is exactly an embedding with closed image, see Proposition [[§42 Embeddings#^prop-42-9|§42.9]]. *Source: filled in.*

^nd-prop-42-9

- [ ] Q1 **[state]** State the proposition.
- [ ] Q2 Proper ⇒ closed image: which proposition?
- [ ] Q3 Closed image ⇒ proper: for $K$ compact, why is $K\cap F(M)$ compact, and why is $F^{-1}(K)$ compact? Where is the embedding hypothesis used?
- [ ] Q4 Prove the last sentence from the two directions and Theorem [[§42 Embeddings#^thm-42-5|§42.5]].
- [ ] Q5 **[why]** The figure-eight has compact, hence closed, image. Why is that not a contradiction? Is local closedness of the image sufficient for an embedding?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S13.
> - Proper ⇒ closed map (Proposition [[§42 Embeddings#^prop-42-4|§42.4]]), so $F(M)$ is closed.
> - $F^{-1}(K)=F^{-1}(K\cap F(M))$ is the image of a compact set under the continuous inverse of $F:M\to F(M)$.
> - Q5: the figure-eight is not an embedding at all; closedness only helps for embeddings.

### Priority 4 · notes only (optional before the midterm)

#### Dense regular submanifolds are open · P4

A dense regular submanifold of $N$ is open in $N$ and has codimension $0$; so the image of an embedding with $\dim M<\dim N$ is never dense, see Corollary [[§42 Embeddings#^cor-42-8|§42.8]]. *Source: filled in.*

^nd-cor-42-8

- [ ] Q1 **[state]** State the corollary and the "in particular".
- [ ] Q2 Why is $S$ open? Use that $S$ is closed in an open $U\supseteq S$ and dense in $U$.
- [ ] Q3 Why must the codimension be $0$? (No nonempty open subset of $\mathbb{R}^n$ lies in $\mathbb{R}^{n-k}\times\{0\}$ for $k\ge1$.)
- [ ] Q4 Deduce the "in particular".
- [ ] Q5 **[why]** Apply it to the irrational line on $T^2$. Which property of the image is enough to rule out an embedding, without any sequence argument?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S13′-type (closed + dense in $U$ ⇒ all of $U$).
> - Proposition [[§42 Embeddings#^prop-42-7|§42.7]]; density in $N$ gives density in $U$.
> - Codimension: $\psi(S\cap V)$ would be a nonempty open subset of $\mathbb{R}^n$ inside a hyperplane.
> - Q5: the image is dense (Proposition [[§42 Embeddings#^prop-42-12|§42.12]]).

#### Images of injective immersions · P4

For an injective immersion $F:M\to N$ there is exactly one topology and smooth structure on $S=F(M)$ making $F:M\to S$ a diffeomorphism, and with them $S$ is an immersed submanifold, see Proposition [[§42 Embeddings#^prop-42-13|§42.13]]. *Source: filled in (not from lecture).*

^nd-prop-42-13

- [ ] Q1 **[state]** State the proposition. **[def]** Define an immersed submanifold (Definition [[§42 Embeddings#^def-42-4|§42.4]]).
- [ ] Q2 Which topology do you declare on $S$? Why is $h=F^{-1}:S\to M$ a homeomorphism?
- [ ] Q3 Which proposition gives the smooth structure?
- [ ] Q4 Why are the topology and the smooth structure unique?
- [ ] Q5 Why is the inclusion $\iota=F\circ h$ an immersion?
- [ ] Q6 **[why]** For the irrational line, is this topology the subspace topology of $T^2$? What would it mean if it were?

> [!tip]- Hints: route of the proof in the notes
> - $U\subseteq S$ open iff $F^{-1}(U)$ open in $M$.
> - Transport of structure, Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-8|§19.8]].
> - $\iota_{\ast q}=F_{\ast h(q)}\circ h_{\ast q}$: an injective map after an isomorphism.
> - Q6: no; by Proposition [[§42 Embeddings#^prop-42-15|§42.15]] it would make $\gamma$ an embedding.

#### When an immersed submanifold is regular · P4

For an injective immersion $F$ and $S=F(M)$ with the structure of Proposition [[§42 Embeddings#^prop-42-13|§42.13]], the following are equivalent: (1) $F$ is an embedding; (2) the topology of $S$ is the subspace topology; (3) $S$ is a regular submanifold whose induced structure is that structure, see Proposition [[§42 Embeddings#^prop-42-15|§42.15]]. *Source: filled in (not from lecture).*

^nd-prop-42-15

- [ ] Q1 **[state]** State the three equivalent conditions.
- [ ] Q2 (1) ⇔ (2): why is the equality of the two topologies the definition of an embedding, for an immersion?
- [ ] Q3 (1) ⇒ (3): which theorem and corollary, and which uniqueness statement?
- [ ] Q4 (3) ⇒ (2): which topology does the induced structure of a regular submanifold have?
- [ ] Q5 **[why]** Example [[§42 Embeddings#^ex-42-1|§42.1]]: for the figure-eight and the irrational line, which of the three conditions fail, and why?

> [!tip]- Hints: route of the proof in the notes
> - (1) ⇒ (3): Theorem [[§42 Embeddings#^thm-42-1|§42.1]] and Corollary [[§42 Embeddings#^cor-42-3|§42.3]], then uniqueness in Proposition [[§42 Embeddings#^prop-42-13|§42.13]].
> - (3) ⇒ (2): Definition [[§37 Regular Submanifolds#^def-37-2|§37.2]] uses the subspace topology.
> - Figure-eight: neighbourhoods of the origin are X's; irrational line: dense, so it would be open (Corollary [[§42 Embeddings#^cor-42-8|§42.8]]), but it meets a circle in a countable set.

# T10. Tangent and cotangent bundles, one-forms, the Hessian

## Definitions T10

### Priority 1 · homework (directly or extended)

#### Hessian matrix · P1

In a chart, $H_{ij}(p) = \frac{\partial^2 f_\varphi}{\partial r^i\,\partial r^j}(\varphi(p))$, see Definition [[§52 Critical Points and the Hessian#^def-52-1|§52.1]]. *Source: notes (Assignment 5).*

^nd-def-52-1

- [ ] Q1 **[def]** Define the Hessian matrix of $f$ at $p$ in a chart.
- [ ] Q2 **[use]** State the change-of-coordinates formula for $H_p$. Which term disappears at a critical point?
- [ ] Q3 **[why]** Show the Hessian matrix depends on the chart away from critical points: $f(t) = t$ at $p = 0$ in the charts $t$ and $t + t^2$.
- [ ] Q4 **[use]** Express $H_p$ as the Jacobian of $\big(\partial f/\partial x^1, \ldots, \partial f/\partial x^m\big)$ in coordinates.

> [!tip]- Hints: where it lives, examples
> - Definition [[§52 Critical Points and the Hessian#^def-52-1|§52.1]]; Q2: Proposition [[§52 Critical Points and the Hessian#^prop-52-2|§52.2]] ($H^{(x)} = J^{\mathsf T}H^{(y)}J + \sum_k \frac{\partial f}{\partial y^k}(p)\,\partial^2 y^k$).
> - Q3: Example [[§52 Critical Points and the Hessian#^ex-52-1|§52.1]] ($0$ versus $-2$). Q4: Proposition [[§52 Critical Points and the Hessian#^prop-52-1|§52.1]].

#### Hessian at a critical point · P1

For $p \in \operatorname{Crit}(f)$, $\operatorname{Hess}_pf(v, w) = \sum_{i,j} H_{ij}(p)\,v^iw^j$, a chart-independent symmetric bilinear form on $T_pM$, see Definition [[§52 Critical Points and the Hessian#^def-52-2|§52.2]]. *Source: notes (Assignment 5).*

^nd-def-52-2

- [ ] Q1 **[def]** State the definition, including the components $v^i$, $w^j$.
- [ ] Q2 **[why]** Prove it does not depend on the chart. Exactly where is $df_p = 0$ used?
- [ ] Q3 **[use]** Express $\operatorname{Hess}_pf$ with vector fields: $\operatorname{Hess}_pf(v, w) = ?$ for fields $\mathbf{X}$, $\mathbf{Y}$ with $\mathbf{X}_p = v$, $\mathbf{Y}_p = w$.
- [ ] Q4 **[example]** Compute the Hessian of $x^2 - y^2$ at $0$.

> [!tip]- Hints: where it lives, examples
> - Definition [[§52 Critical Points and the Hessian#^def-52-2|§52.2]]; Q2: Proposition [[§52 Critical Points and the Hessian#^prop-52-3|§52.3]] via Proposition [[§52 Critical Points and the Hessian#^prop-52-2|§52.2]].
> - Q3: Proposition [[§55 Lie Bracket and Lie Algebra#^prop-55-3|§55.3]]. Q4: $\mathrm{diag}(2, -2)$, the remark *The Morse Lemma* in [[§52 Critical Points and the Hessian|§52]].

#### Nondegenerate critical point · P1

$p \in \operatorname{Crit}(f)$ is nondegenerate if $\operatorname{Hess}_pf$ is a non-degenerate pairing, see Definition [[§52 Critical Points and the Hessian#^def-52-3|§52.3]]. *Source: notes (Assignment 5).*

^nd-def-52-3

- [ ] Q1 **[def]** State the definition via $(\operatorname{Hess}_pf)^\flat : T_pM \to T^\ast_pM$.
- [ ] Q2 **[use]** List the equivalent conditions (determinant in one chart, in every chart, independence of $d(\partial f/\partial x^i)_p$).
- [ ] Q3 **[why]** Why is $0$ a degenerate critical point of $x^3$ and a nondegenerate one of $x^2$? Picture $df$ against the zero section.
- [ ] Q4 **[use]** Why are nondegenerate critical points isolated?

> [!tip]- Hints: where it lives, examples
> - Definition [[§52 Critical Points and the Hessian#^def-52-3|§52.3]], Definition [[§21 Linear Algebra Toolkit#^def-21-5|§21.5]]; Q2: Proposition [[§52 Critical Points and the Hessian#^prop-52-4|§52.4]].
> - Q3: Example [[§52 Critical Points and the Hessian#^ex-52-2|§52.2]]. Q4: Theorem [[§52 Critical Points and the Hessian#^thm-52-10|§52.10]], Corollary [[§52 Critical Points and the Hessian#^cor-52-11|§52.11]] → drilled as [[Differentiable Manifolds HW Drill#^hw5-3|HW5.3]].

#### Morse function · P1

A smooth $f$ all of whose critical points are nondegenerate, see Definition [[§52 Critical Points and the Hessian#^def-52-4|§52.4]]. *Source: notes (Assignment 5).*

^nd-def-52-4

- [ ] Q1 **[def]** State the definition. Is a function without critical points Morse?
- [ ] Q2 **[use]** State the characterization by transversality of $df$ to the zero section.
- [ ] Q3 **[why]** Why does a Morse function on a compact manifold have finitely many critical points? Which two facts combine?
- [ ] Q4 **[example]** Is the height function on $S^2$ Morse? Is $x^3$ on $\mathbb{R}$? What is the index of each critical point of $x^2 - y^2$?

> [!tip]- Hints: where it lives, examples
> - Definition [[§52 Critical Points and the Hessian#^def-52-4|§52.4]], Definition [[§52 Critical Points and the Hessian#^def-52-5|§52.5]]; Q2: Theorem [[§52 Critical Points and the Hessian#^thm-52-10|§52.10]] → drilled as [[Differentiable Manifolds HW Drill#^hw5-3|HW5.3]].
> - Q3: Corollary [[§52 Critical Points and the Hessian#^cor-52-11|§52.11]] (discrete) and compactness, Corollary [[§52 Critical Points and the Hessian#^cor-52-12|§52.12]]. Q4: yes (two nondegenerate critical points); no (Example [[§52 Critical Points and the Hessian#^ex-52-2|§52.2]]); index $1$.

#### Conormal bundle · P1

$N^\ast S = \{(p, \alpha) \in T^\ast M : p \in S, \alpha \in N_pS\}$, see Definition [[§52 Critical Points and the Hessian#^def-52-6|§52.6]]. *Source: notes (Assignment 5).*

^nd-def-52-6

- [ ] Q1 **[def]** State the definition.
- [ ] Q2 **[use]** Show $N^\ast S$ is a regular submanifold of $T^\ast M$ of dimension $m$, whatever the codimension of $S$. Which coordinates vanish in an adapted chart?
- [ ] Q3 **[why]** What is $N^\ast S$ when $S$ is a point, and when $S = M$?
- [ ] Q4 **[use]** Relate the critical points of $\Phi|_S$ to $N^\ast S$.

> [!tip]- Hints: where it lives, examples
> - Definition [[§52 Critical Points and the Hessian#^def-52-6|§52.6]]; Q2: Proposition [[§52 Critical Points and the Hessian#^prop-52-6|§52.6]] ($\bar x^{m-k+1}, \ldots, \bar x^m$ and $\xi_1, \ldots, \xi_{m-k}$).
> - Q3: the remark *Extreme Cases of the Conormal Bundle* in [[§52 Critical Points and the Hessian|§52]] (the fibre $T^\ast_pM$; the zero section). Q4: Corollary [[§52 Critical Points and the Hessian#^cor-52-7|§52.7]].

### Priority 2 · stated or done in class

#### Tangent bundle (as a set) · P2

$TM = \{(p, v) : p \in M, v \in T_pM\}$ with $\pi(p, v) = p$ and zero section $\zeta(p) = (p, 0)$, see Definition [[§49 The Tangent Bundle#^def-49-1|§49.1]]. *Source: Lecture 12.*

^nd-def-49-1

- [ ] Q1 **[def]** Define $TM$, the projection $\pi$, and the zero section $\zeta$.
- [ ] Q2 **[why]** Why write pairs $(p, v)$ instead of the union of the $T_pM$? (Could two tangent spaces share an element?)
- [ ] Q3 **[use]** Which structure does $TM$ eventually carry, of which dimension, and what is $\zeta(M)$ inside it?
- [ ] Q4 **[example]** For $M$ an open subset of $\mathbb{R}^m$, what is $TM$?

> [!tip]- Hints: where it lives, examples
> - Definition [[§49 The Tangent Bundle#^def-49-1|§49.1]], Definition [[§49 The Tangent Bundle#^def-49-2|§49.2]], Definition [[§49 The Tangent Bundle#^def-49-3|§49.3]]; the remark *The Picture Changes* in [[§49 The Tangent Bundle|§49]].
> - Q2: the zero vectors of different $T_pM$ must be different points of $TM$. Q3: Proposition [[§49 The Tangent Bundle#^prop-49-4|§49.4]], Corollary [[§49 The Tangent Bundle#^cor-49-3|§49.3]]. Q4: $U \times \mathbb{R}^m$ via one chart.

#### Local trivialization of $TM$ · P2

For a chart $(U, \varphi = (x^i))$, $\Phi : TU \to U \times \mathbb{R}^m$, $\Phi(p, v) = (p, v^1, \ldots, v^m)$ with $v = \sum_i v^i\,\partial/\partial x^i|_p$, see Definition [[§49 The Tangent Bundle#^def-49-4|§49.4]]. *Source: Lecture 13.*

^nd-def-49-4

- [ ] Q1 **[def]** State the definition. How are the $v^i$ computed from $v$?
- [ ] Q2 **[why]** Why is $\Phi$ a bijection, and why does $\mathrm{pr}_1 \circ \Phi = \pi$ make it a "trivialization"?
- [ ] Q3 **[why]** Is $\Phi$ linear on each fibre $T_pM$? Why is that the extra feature that makes $TM$ a vector bundle?
- [ ] Q4 **[use]** Which local sections does $\Phi$ give? (The coordinate frame.)

> [!tip]- Hints: where it lives, examples
> - Definition [[§49 The Tangent Bundle#^def-49-4|§49.4]]; $v^i = v[x^i]$, Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]].
> - Q3: Corollary [[§49 The Tangent Bundle#^cor-49-3|§49.3]] (part 2); the remark *Vector Bundles* in [[§49 The Tangent Bundle|§49]]. Q4: the remark *Trivializations and Frames* in [[§49 The Tangent Bundle|§49]].

#### Charts of $TM$ (the tangent bundle atlas) · P2

$\tilde\varphi(p, v) = (x^1(p), \ldots, x^m(p), v^1, \ldots, v^m)$ on $TU$, for each smooth chart $(U, \varphi)$ of $M$, see Definition [[§49 The Tangent Bundle#^def-49-5|§49.5]]. *Source: Lecture 13.*

^nd-def-49-5

- [ ] Q1 **[def]** State the chart $\tilde\varphi$ on $TU$ and its inverse.
- [ ] Q2 **[use]** Which topology on $TM$ makes every $\tilde\varphi$ a homeomorphism onto $\varphi(U) \times \mathbb{R}^m$? Why is it Hausdorff and second countable?
- [ ] Q3 **[use]** Compute the transition map $\tilde\psi \circ \tilde\varphi^{-1}$. Why is it smooth?
- [ ] Q4 **[why]** What would go wrong if one used arbitrary bases of $T_pM$, chosen point by point, instead of the coordinate bases?
- [ ] Q5 **[example]** For $M = \mathbb{R}$ with the charts $\mathrm{id}$ and $t \mapsto t^3$ on $(0, \infty)$, write the transition map of $TM$.

> [!tip]- Hints: where it lives, examples
> - Definition [[§49 The Tangent Bundle#^def-49-5|§49.5]]; Q2: Proposition [[§49 The Tangent Bundle#^prop-49-1|§49.1]] (countably many charts; separate points in one chart or by disjoint $TU$, $TV$).
> - Q3: Proposition [[§49 The Tangent Bundle#^prop-49-2|§49.2]]: $(r, v) \mapsto (\psi \circ \varphi^{-1}(r), J(r)v)$ with $J$ the Jacobian of the chart change.
> - Q4: the transition maps need not even be continuous; the coordinate bases vary smoothly with $p$. Q5: $(r, v) \mapsto (r^3, 3r^2 v)$.

#### Charts of $T^\ast M$ (the cotangent bundle atlas) · P2

$\hat\varphi(p, \xi) = (x^1(p), \ldots, x^m(p), \xi_1, \ldots, \xi_m)$ with $\xi = \sum_i \xi_i\,dx^i|_p$, $\xi_i = \xi(\partial/\partial x^i|_p)$, see Definition [[§50 The Cotangent Bundle#^def-50-5|§50.5]]. *Source: Lectures 13, 15.*

^nd-def-50-5

- [ ] Q1 **[def]** Define $T^\ast M$ as a set, the local trivialization $\Psi$ over a chart, and the chart $\hat\varphi$ with its inverse.
- [ ] Q2 **[use]** Prove the transition law $\eta_j = \sum_i \frac{\partial x^i}{\partial y^j}(p)\,\xi_i$ and write $\hat\psi \circ \hat\varphi^{-1}$.
- [ ] Q3 **[why]** Covector components transform by the transpose of the inverse Jacobian, vector components by the Jacobian. Why, and why is either one smooth?
- [ ] Q4 **[use]** Why is $\pi : T^\ast M \to M$ a fibration (indeed a vector bundle), and the zero section a submanifold of codimension $m$?
- [ ] Q5 **[example]** For $M = \mathbb{R}$ with charts $x$ and $y = x^3$ on $(0, \infty)$, express $dx$ in terms of $dy$ and write the transition map.

> [!tip]- Hints: where it lives, examples
> - Definition [[§50 The Cotangent Bundle#^def-50-1|§50.1]], Definition [[§50 The Cotangent Bundle#^def-50-4|§50.4]], Definition [[§50 The Cotangent Bundle#^def-50-5|§50.5]]; Corollary [[§33 Covectors in Coordinates#^cor-33-2|§33.2]].
> - Q2, Q3: Proposition [[§50 The Cotangent Bundle#^prop-50-2|§50.2]] ($(r, \xi) \mapsto (\tau(r), (\tau'(r)^{-1})^{\mathsf T}\xi)$). Topology: Proposition [[§50 The Cotangent Bundle#^prop-50-1|§50.1]].
> - Q4: Corollary [[§50 The Cotangent Bundle#^cor-50-3|§50.3]], Proposition [[§52 Critical Points and the Hessian#^prop-52-5|§52.5]]. Q5: $dx = \frac{1}{3x^2}\,dy$; $(r, \xi) \mapsto (r^3, \xi/(3r^2))$.

#### One-form · P2

A smooth map $\theta : M \to T^\ast M$ with $\theta_p \in T^\ast_pM$, i.e. a section of $T^\ast M$, see Definition [[§51 One-Forms#^def-51-1|§51.1]]. *Source: Lecture 15.*

^nd-def-51-1

- [ ] Q1 **[def]** State the definition, in both forms.
- [ ] Q2 **[use]** In a chart, $\theta = \sum_j \theta_j\,dx^j$. Prove $\theta$ is smooth iff the $\theta_j$ are smooth.
- [ ] Q3 **[example]** Why is $df$ a one-form for $f \in C^\infty(M)$? Write it in coordinates.
- [ ] Q4 **[why]** Is every one-form $df$ for some $f$? Give the necessary condition and a one-form on $\mathbb{R}^2$ that fails it.
- [ ] Q5 **[why]** The condition is not sufficient: give the one-form on $\mathbb{R}^2 \setminus \{0\}$ that satisfies it but is not $df$, and the integral that proves it.

> [!tip]- Hints: where it lives, examples
> - Definition [[§51 One-Forms#^def-51-1|§51.1]], Definition [[§51 One-Forms#^def-51-2|§51.2]]; Q2: Proposition [[§51 One-Forms#^prop-51-1|§51.1]]. Q3: Proposition [[§51 One-Forms#^prop-51-2|§51.2]].
> - Q4: Proposition [[§51 One-Forms#^prop-51-3|§51.3]] (mixed partials), Example [[§51 One-Forms#^ex-51-1|§51.1]] ($\tfrac12(x\,dy - y\,dx)$).
> - Q5: the remark *The Condition Is Not Sufficient* in [[§51 One-Forms|§51]] ($\frac{x\,dy - y\,dx}{x^2 + y^2}$ around the circle gives $2\pi$).

#### Pullback of a one-form · P2

$(F^\ast\theta)_p(v) = \theta_{F(p)}(F_{\ast p}v)$, see Definition [[§51 One-Forms#^def-51-4|§51.4]]. *Source: Lecture 15.*

^nd-def-51-4

- [ ] Q1 **[def]** State the definition: at which point is $\theta$ evaluated, and on which vector?
- [ ] Q2 **[use]** Compute $F^\ast\big(\sum_j \theta_j\,dy^j\big)$ in coordinates; conclude $F^\ast\theta$ is smooth.
- [ ] Q3 **[use]** Prove $F^\ast(df) = d(F^\ast f)$.
- [ ] Q4 **[example]** Pull back $x\,dy - y\,dx$ along $t \mapsto (\cos t, \sin t)$.
- [ ] Q5 **[why]** Why can one-forms be pulled back along every smooth $F$, while vector fields cannot be pushed forward? Name the two obstructions (non-injective, non-surjective $F$).

> [!tip]- Hints: where it lives, examples
> - Definition [[§51 One-Forms#^def-51-3|§51.3]], Definition [[§51 One-Forms#^def-51-4|§51.4]]; the remark *Vector Fields Do Not Push Forward* in [[§56 Related Vector Fields|§56]].
> - Q2: Proposition [[§51 One-Forms#^prop-51-5|§51.5]]. Q3: Corollary [[§51 One-Forms#^cor-51-4|§51.4]]. Q4: $dt$.

## Proofs T10

### Priority 1 · homework (directly or extended)

#### Change of coordinates for the Hessian · P1

For two charts at $p$ with $J_{ki}=\partial y^k/\partial x^i(p)$: $H^{(x)}_{ij}=\sum_{k,l}J_{ki}J_{lj}H^{(y)}_{kl}+\sum_k\frac{\partial f}{\partial y^k}(p)\frac{\partial^2y^k}{\partial x^i\partial x^j}(p)$; at a critical point $H^{(x)}_p=J^{\mathsf T}H^{(y)}_pJ$ and $\det H^{(x)}_p=(\det J)^2\det H^{(y)}_p$, see Proposition [[§52 Critical Points and the Hessian#^prop-52-2|§52.2]]. *Source: filled in (context of Assignment 5, Problem 3).*

^nd-prop-52-2

- [ ] Q1 **[state]** State the formula, its form at a critical point, and the determinant identity. **[def]** Define the Hessian matrix in a chart (Definition [[§52 Critical Points and the Hessian#^def-52-1|§52.1]]).
- [ ] Q2 With the transition map $\tau=\psi\circ\varphi^{-1}$, why is $f_\varphi=f_\psi\circ\tau$? How are $J$ and $\partial^2y^k/\partial x^i\partial x^j(p)$ expressed through $\tau$?
- [ ] Q3 Differentiate $f_\varphi=f_\psi\circ\tau$ once (chain rule), then again (product rule and chain rule).
- [ ] Q4 Identify each term at $r=\varphi(p)$.
- [ ] Q5 At a critical point, why does the second sum vanish? Why is $J$ invertible?
- [ ] Q6 **[why]** Example [[§52 Critical Points and the Hessian#^ex-52-1|§52.1]]: for $f(t)=t$ on $\mathbb{R}$ and the charts $x=t$, $y=t+t^2$, compute both Hessians at $0$. What does this show at non-critical points?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S1 (differentiate downstairs).
> - $y^k\circ\varphi^{-1}=\tau^k$, so $J_{kj}=\partial_j\tau^k(a)$ and $\partial^2y^k/\partial x^i\partial x^j(p)=\partial_i\partial_j\tau^k(a)$.
> - $\partial_jf_\varphi=\sum_l(\partial_lf_\psi\circ\tau)\,\partial_j\tau^l$, then differentiate in $r^i$.
> - Critical: $\partial f/\partial y^k(p)=0$ (Proposition [[§36 Submersions#^prop-36-2|§36.2]]); $J^{-1}=[\partial x^i/\partial y^k(p)]$ (Corollary [[§30 The Differential in Coordinates#^cor-30-4|§30.4]]).
> - Q6: $H^{(x)}(0)=0$, $H^{(y)}(0)=-2$: even the rank depends on the chart.

#### The Hessian as a map $T_pM\to T_p^\ast M$ · P1

At $p\in\operatorname{Crit}(f)$, $B=\operatorname{Hess}_pf$ satisfies $B^\flat=B^\sharp$, $B^\flat(\partial/\partial x^i|_p)=d(\partial f/\partial x^i)_p$, with matrix $H_p$; and $p$ is nondegenerate iff $B^\flat$ is injective, iff bijective, iff $\det H_p\neq0$ in one (every) chart, iff the $d(\partial f/\partial x^i)_p$ are independent, see Proposition [[§52 Critical Points and the Hessian#^prop-52-4|§52.4]]. *Source: filled in (condition (f) is the form used in Assignment 5, Problem 3).*

^nd-prop-52-4

- [ ] Q1 **[state]** State part (1) and the six equivalent conditions of part (2).
- [ ] Q2 Compute the components of $B^\sharp(\partial/\partial x^j|_p)$. Why is it $d(\partial f/\partial x^j)_p$?
- [ ] Q3 Why is $B^\flat=B^\sharp$, and why is the matrix of $B^\flat$ equal to $H_p$?
- [ ] Q4 Prove (a)⇔(b)⇔(c)⇔(d).
- [ ] Q5 Why does $\det H_p\neq0$ in one chart give it in every chart? Give two reasons.
- [ ] Q6 **[why]** Is $0$ a nondegenerate critical point of $x^3$? Is it isolated? What does this say about the converse of Corollary [[§52 Critical Points and the Hessian#^cor-52-11|§52.11]]?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S7 (linear algebra: same dimension, injective ⇔ bijective).
> - Components of $B^\sharp(\partial_j)$ are $B(\partial_i,\partial_j)=H_{ij}(p)$; Proposition [[§52 Critical Points and the Hessian#^prop-52-1|§52.1]](3).
> - $\dim T_pM=\dim T_p^\ast M=m$.
> - Every chart: $B^\flat$ is chart-free; or $\det H^{(x)}_p=(\det J)^2\det H^{(y)}_p$.
> - Q6: Example [[§52 Critical Points and the Hessian#^ex-52-2|§52.2]]: degenerate but isolated.

#### The zero section of $T^\ast M$ is a regular submanifold · P1

$\mathcal Z$ is cut out by $\xi_1=\dots=\xi_m=0$ in standard coordinates, and $\zeta_{\ast p}(\partial/\partial x^i|_p)=\partial/\partial\bar x^i|_{(p,0)}$, see Proposition [[§52 Critical Points and the Hessian#^prop-52-5|§52.5]]. → drilled as [[Differentiable Manifolds HW Drill#^hw5-3|HW5.3]] (the warm-up; see also Corollary [[§50 The Cotangent Bundle#^cor-50-3|§50.3]](3)).

^nd-prop-52-5

#### The differential of $df$ at a critical point · P1

$(s_f)_{\ast q}(\partial/\partial x^i|_q)=\partial/\partial\bar x^i+\sum_jH_{ij}(q)\,\partial/\partial\xi_j$; at a critical point the vertical part of $(s_f)_{\ast p}v$ is $\operatorname{Hess}_pf(v,\cdot)$, see Proposition [[§52 Critical Points and the Hessian#^prop-52-9|§52.9]]. → drilled as [[Differentiable Manifolds HW Drill#^hw5-3|HW5.3]].

^nd-prop-52-9

#### Transversality to the zero section · P1

$s_f\pitchfork\mathcal Z$ iff every critical point of $f$ is nondegenerate, see Theorem [[§52 Critical Points and the Hessian#^thm-52-10|§52.10]]. → drilled as [[Differentiable Manifolds HW Drill#^hw5-3|HW5.3]] (part (a)).

^nd-thm-52-10

#### Critical points of a Morse function are isolated · P1

For a Morse function, $\operatorname{Crit}(f)=s_f^{-1}(\mathcal Z)$ is a regular submanifold of dimension $0$, hence discrete, see Corollary [[§52 Critical Points and the Hessian#^cor-52-11|§52.11]]. → drilled as [[Differentiable Manifolds HW Drill#^hw5-3|HW5.3]] (part (b)).

^nd-cor-52-11

### Priority 2 · stated or done in class

#### The topology of the tangent bundle · P2

There is a unique topology on $TM$ for which every $TU$ is open and every chart $\tilde\varphi=(\varphi\times\mathrm{id})\circ\Phi:TU\to\varphi(U)\times\mathbb{R}^m$ is a homeomorphism; with it $TM$ is a topological manifold of dimension $2m$, see Proposition [[§49 The Tangent Bundle#^prop-49-1|§49.1]]. *Source: stated in Lecture 13 without proof ("it's all point-set topology ... see Lee"); filled in.* **[class exercise, Lecture 13]**

^nd-prop-49-1

- [ ] Q1 **[state]** State the proposition.
- [ ] Q2 **[def]** Define $TM$ as a set, the local trivialization $\Phi$ over a chart, and the chart $\tilde\varphi$ (Definitions [[§49 The Tangent Bundle#^def-49-1|§49.1]], [[§49 The Tangent Bundle#^def-49-4|§49.4]], [[§49 The Tangent Bundle#^def-49-5|§49.5]]).
- [ ] Q3 Prove the two set-theoretic facts: $TU\cap TV=\pi^{-1}(U\cap V)$ and $\tilde\varphi(TU\cap TV)=\varphi(U\cap V)\times\mathbb{R}^m$, an open set.
- [ ] Q4 Define the candidate topology $\tau$. Check the three axioms; where is injectivity of $\tilde\varphi$ used?
- [ ] Q5 Why is each $TU$ open? Why is $\tilde\varphi$ open and continuous? (Which property of the transition maps do you need?) Why is the topology unique?
- [ ] Q6 Prove Hausdorff (two cases) and second countable.
- [ ] Q7 **[why]** Where is it used that $M$ is Hausdorff, and that it is second countable? What would go wrong for $TM$ if $M$ were the line with two origins?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S1; Lee's smooth manifold chart lemma.
> - Every list of components occurs at each $p$ (Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]]); $\varphi(U\cap V)$ is open (Proposition [[§2 Topological Manifolds#^prop-2-11|§2.11]]).
> - $W$ open iff $\tilde\varphi(W\cap TU)$ open in $\mathbb{R}^{2m}$ for every chart.
> - Continuity: $\tilde\psi(W\cap TV)=(\tilde\psi\circ\tilde\varphi^{-1})(O\cap(\varphi(U\cap V)\times\mathbb{R}^m))$; transition maps are homeomorphisms (computed in Proposition [[§49 The Tangent Bundle#^prop-49-2|§49.2]] without any topology).
> - Hausdorff: same base point — use one chart; different base points — disjoint chart domains. Second countable: countably many chart domains $U_B$ from a countable basis.

#### The smooth atlas of the tangent bundle · P2

The charts $(TU,\tilde\varphi)$ form a smooth atlas on $TM$, with transition map $\tilde\psi\circ\tilde\varphi^{-1}(r,v)=(\tau(r),\tau'(r)v)$, $\tau=\psi\circ\varphi^{-1}$, see Proposition [[§49 The Tangent Bundle#^prop-49-2|§49.2]]. *Source: Lecture 13 ("the only thing that I want to have a look at is ... the transition functions"); completed in the notes.*

^nd-prop-49-2

- [ ] Q1 **[state]** State the proposition with the transition formula.
- [ ] Q2 Why are the $(TU,\tilde\varphi)$ charts, and why do they cover $TM$? What is the domain of the transition map?
- [ ] Q3 Derive the change of basis formula $\partial/\partial x^j|_p=\sum_i\frac{\partial y^i}{\partial x^j}(p)\,\partial/\partial y^i|_p$ from the universal formula.
- [ ] Q4 Deduce $w^i=\sum_j\frac{\partial y^i}{\partial x^j}(p)v^j$ for the components in the two bases.
- [ ] Q5 Why is $\frac{\partial y^i}{\partial x^j}(\varphi^{-1}(r))$ the entry of $\tau'(r)$? Conclude smoothness of the transition map.
- [ ] Q6 Why is the inverse transition map smooth, so that the charts are compatible?
- [ ] Q7 **[why]** Proposition [[§49 The Tangent Bundle#^prop-49-1|§49.1]] uses this transition formula before $TM$ has a topology. Why is that not circular?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S1, S9 (a derivation is determined by its values on coordinate functions).
> - The coefficient of $D$ on $\partial/\partial y^i|_p$ is $D[y^i]$ (Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]]); apply it to $D=\partial/\partial x^j|_p$.
> - Proposition [[§30 The Differential in Coordinates#^prop-30-1|§30.1]] with $F=\mathrm{id}_M$: upstairs partials are downstairs partials of $\tau$.
> - Components $\tau^i(r)$ and $\sum_j\partial_j\tau^i(r)v^j$ are smooth in $(r,v)$.
> - The formula only uses the definitions of the charts as bijections.

#### The tangent bundle is a fibration · P2

$TM$ is a smooth manifold of dimension $2m$, $\pi:TM\to M$ is smooth, the $\Phi$ are local trivializations (linear on fibres), so $\pi$ is a fibration with fibre $\mathbb{R}^m$, and the zero section $\zeta(M)$ is a submanifold of codimension $m$, see Corollary [[§49 The Tangent Bundle#^cor-49-3|§49.3]]. *Source: Lecture 13 ("a beautiful fibration"); details and the zero section filled in.*

^nd-cor-49-3

- [ ] Q1 **[state]** State the three parts.
- [ ] Q2 Why is $\pi$ smooth? What is its coordinate representation in $\tilde\varphi$ and $\varphi$?
- [ ] Q3 Why is $\Phi=(\varphi^{-1}\times\mathrm{id})\circ\tilde\varphi$ a diffeomorphism $TU\to U\times\mathbb{R}^m$ with $\mathrm{pr}_1\circ\Phi=\pi$?
- [ ] Q4 Why is $\Phi$ a linear isomorphism $T_pM\to\{p\}\times\mathbb{R}^m$ on each fibre?
- [ ] Q5 Why is every chart $\tilde\varphi$ adapted to $\zeta(M)$?
- [ ] Q6 **[why]** A vector bundle is a fibration whose fibres are vector spaces with trivializations linear on fibres (remark *Vector Bundles*). Which part of this corollary is the extra "vector bundle" information, beyond being a fibration with fibre $\mathbb{R}^m$?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S1.
> - $\varphi\circ\pi\circ\tilde\varphi^{-1}(r,v)=r$.
> - $\tilde\varphi$ is a chart of $TU$, $\varphi^{-1}\times\mathrm{id}$ the inverse of a product chart (Proposition [[§28 Derivations and the Abstract Tangent Space#^prop-28-9|§28.9]]).
> - $v\mapsto v[x^i]$ is linear and the coordinate vectors are a basis.
> - $\zeta(M)\cap TU=\{v^1=\dots=v^m=0\}$.

#### The smooth atlas of the cotangent bundle · P2

The standard charts $(T^\ast U,\hat\varphi)$, $\hat\varphi(p,\xi)=(x^1(p),\dots,x^m(p),\xi_1,\dots,\xi_m)$ with $\xi_i=\xi(\partial/\partial x^i|_p)$, form a smooth atlas on $T^\ast M$; covector components transform by $\eta_j=\sum_i\frac{\partial x^i}{\partial y^j}(p)\xi_i$, so the transition map is $(r,\xi)\mapsto(\tau(r),(\tau'(r)^{-1})^{\mathsf T}\xi)$, see Proposition [[§50 The Cotangent Bundle#^prop-50-2|§50.2]]. *Source: Lecture 13 ("completely analogous", with the formula for $dx^i$); the rest filled in.*

^nd-prop-50-2

- [ ] Q1 **[state]** State the proposition: the two transformation formulas and the transition map.
- [ ] Q2 **[def]** Define the local trivialization $\Psi$ and the standard coordinates $\hat\varphi$ of $T^\ast M$ (Definitions [[§50 The Cotangent Bundle#^def-50-4|§50.4]], [[§50 The Cotangent Bundle#^def-50-5|§50.5]]). How are the components $\xi_i$ computed?
- [ ] Q3 Derive $dx^i|_p=\sum_j\frac{\partial x^i}{\partial y^j}(p)\,dy^j|_p$. Which lemma, applied to which function?
- [ ] Q4 Substitute into $\xi=\sum_i\xi_i\,dx^i|_p$ and read off $\eta_j$.
- [ ] Q5 Why is $B=[\partial x^i/\partial y^j(p)]$ the inverse of $A=[\partial y^i/\partial x^j(p)]$? Conclude that covector components transform by $(A^{-1})^{\mathsf T}$.
- [ ] Q6 Why is the transition map smooth (entries of $\tau'(r)^{-1}$), and why do the charts form an atlas? Where does the topology of $T^\ast M$ come from (Proposition [[§50 The Cotangent Bundle#^prop-50-1|§50.1]])?
- [ ] Q7 **[why]** Why can the covector components not transform by the same matrix $A$ as vector components? Which quantity must be independent of the chart?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S1, S7.
> - Lemma [[§33 Covectors in Coordinates#^lem-33-1|§33.1]] for $f=x^i$ in the chart $\psi$.
> - Collect coefficients of $dy^j|_p$; they are unique.
> - $BA=I$: Corollary [[§30 The Differential in Coordinates#^cor-30-4|§30.4]](3), or evaluate the formula for $dx^i|_p$ on $\partial/\partial x^k|_p$.
> - Cramer's rule: entries of $\tau'(r)^{-1}$ are cofactors over a nonzero determinant. Topology: Proposition [[§49 The Tangent Bundle#^prop-49-1|§49.1]] word for word.
> - Q7: $\xi(v)=\sum_i\xi_iv^i$ must not depend on the chart. The fibration statement: Corollary [[§50 The Cotangent Bundle#^cor-50-3|§50.3]].

#### One-forms in coordinates · P2

For a section $\theta$ of $T^\ast M$ (not assumed smooth) and a chart $(U,(x^i))$: $\theta=\sum_j\theta_j\,dx^j$ on $U$ with $\theta_j(p)=\theta_p(\partial/\partial x^j|_p)$; its coordinate representation is $r\mapsto(r,\theta_1(\varphi^{-1}(r)),\dots,\theta_m(\varphi^{-1}(r)))$; and $\theta$ is smooth on $U$ iff the $\theta_j$ are, see Proposition [[§51 One-Forms#^prop-51-1|§51.1]]. *Source: stated in Lecture 15; filled in.*

^nd-prop-51-1

- [ ] Q1 **[state]** State the three parts. **[def]** Define a one-form (Definition [[§51 One-Forms#^def-51-1|§51.1]]).
- [ ] Q2 (1) Why is $\theta_p=\sum_j\theta_p(\partial/\partial x^j|_p)\,dx^j|_p$?
- [ ] Q3 (2) Why does $\theta$ map $U$ into $T^\ast U$? Compute $\hat\varphi\circ\theta\circ\varphi^{-1}$.
- [ ] Q4 (3) Prove both directions. In "smooth coefficients ⇒ smooth", why must continuity of $\theta$ be checked, and how?
- [ ] Q5 **[why]** Where is it used that the charts $\hat\varphi$ are homeomorphisms (Proposition [[§50 The Cotangent Bundle#^prop-50-1|§50.1]])?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S1.
> - Corollary [[§33 Covectors in Coordinates#^cor-33-2|§33.2]] (covectors in the dual basis).
> - $\pi\circ\theta=\mathrm{id}$, so $\theta(U)\subseteq T^\ast U$.
> - Continuity: $\theta|_U=\hat\varphi^{-1}\circ(\hat\varphi\circ\theta\circ\varphi^{-1})\circ\varphi$; Definition [[§19 Smooth Functions and Smooth Maps#^def-19-3|§19.3]] asks for continuity.

#### The differential of a function is a one-form · P2

For $f\in C^\infty(M)$, $df:p\mapsto df_p$ is a one-form, $df=\sum_j\frac{\partial f}{\partial x^j}dx^j$ in a chart, and $d$ is $\mathbb{R}$-linear with $d(fg)=f\,dg+g\,df$, see Proposition [[§51 One-Forms#^prop-51-2|§51.2]]. *Source: Lecture 15 recalled the coordinate formula; the rest filled in.*

^nd-prop-51-2

- [ ] Q1 **[state]** State the proposition.
- [ ] Q2 Why is $df$ a section of $T^\ast M$, and why does it have the stated coordinate formula?
- [ ] Q3 Why are the coefficients $\partial f/\partial x^j$ smooth on $U$? Which proposition turns this into smoothness of $df$?
- [ ] Q4 Prove linearity and the product rule by evaluating at a point $p$ and a vector $v$.
- [ ] Q5 **[why]** Is every one-form a differential $df$? Give the example of the notes and the test that rules it out.

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S1, S9.
> - Lemma [[§33 Covectors in Coordinates#^lem-33-1|§33.1]] at each $p$; $df_p(\partial/\partial x^j|_p)=\partial f/\partial x^j(p)$ (Proposition [[§32 The Cotangent Space#^prop-32-2|§32.2]]).
> - Lemma [[§29 Coordinate Derivations and the Basis Theorem#^lem-29-1|§29.1]], then Proposition [[§51 One-Forms#^prop-51-1|§51.1]](3).
> - $d(fg)_p(v)=v[fg]=f(p)v[g]+g(p)v[f]$.
> - Q5: Proposition [[§51 One-Forms#^prop-51-3|§51.3]].

#### A necessary condition for being a differential · P2

If $\theta=\sum_j\theta_j\,dx^j=df$ on a chart domain, then $\partial\theta_j/\partial x^k=\partial\theta_k/\partial x^j$; so $\theta=\tfrac12(x\,dy-y\,dx)$ is not $df$ on any open subset of $\mathbb{R}^2$, see Proposition [[§51 One-Forms#^prop-51-3|§51.3]]. *Source: Lecture 15.*

^nd-prop-51-3

- [ ] Q1 **[state]** State the proposition and the example.
- [ ] Q2 If $\theta=df$, why is $\theta_j=\partial f/\partial x^j$?
- [ ] Q3 Why are $\partial\theta_j/\partial x^k$ and $\partial\theta_k/\partial x^j$ equal? Translate to the coordinate representation $f_\varphi$.
- [ ] Q4 Check that $\theta=\tfrac12(x\,dy-y\,dx)$ violates the condition at every point.
- [ ] Q5 **[why]** The condition is not sufficient. Check that $\omega=(x\,dy-y\,dx)/(x^2+y^2)$ on $\mathbb{R}^2\setminus\{0\}$ satisfies it, and show $\omega\neq df$ by integrating along the unit circle.

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S1 (uniqueness of coefficients in the dual basis).
> - $\partial\theta_j/\partial x^k(p)=\partial^2f_\varphi/\partial r^k\partial r^j(\varphi(p))$; Clairaut.
> - $\theta_x=-y/2$, $\theta_y=x/2$: $\tfrac12\neq-\tfrac12$.
> - Q5 (remark *The Condition Is Not Sufficient*): $\omega(c'(t))=1$ along $c(t)=(\cos t,\sin t)$, so $f(c(2\pi))-f(c(0))=2\pi$ would be needed.

#### Pullback commutes with $d$ · P2

For $F:M\to N$ smooth and $f\in C^\infty(N)$, $F^\ast(df)=d(F^\ast f)$, where $(F^\ast\theta)_p(v)=\theta_{F(p)}(F_{\ast p}v)$ and $F^\ast f=f\circ F$, see Corollary [[§51 One-Forms#^cor-51-4|§51.4]]. *Source: Lecture 15 ("the pullback map commutes with $d$").*

^nd-cor-51-4

- [ ] Q1 **[state]** State the corollary. **[def]** Define the pullback of functions and of one-forms (Definitions [[§51 One-Forms#^def-51-3|§51.3]], [[§51 One-Forms#^def-51-4|§51.4]]).
- [ ] Q2 Compute the value of the left side at $p$.
- [ ] Q3 Compute the value of the right side at $p$; why is $F^\ast f$ smooth?
- [ ] Q4 Which pointwise proposition identifies the two? Prove it by evaluating on $v\in T_pM$.
- [ ] Q5 **[why]** One-forms can always be pulled back along a smooth map. Why can vector fields in general not be pushed forward (two reasons)?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: compare values at each point.
> - Left: $F_p^\ast(df_{F(p)})$; right: $d(f\circ F)_p$.
> - Proposition [[§34 The Cotangent Space from Germs#^prop-34-6|§34.6]]: $df_{F(p)}(F_{\ast p}v)=(F_{\ast p}v)[f]=v[f\circ F]$.
> - Q5: $F$ not injective — several candidates; not surjective — no candidate (remark *Vector Fields Do Not Push Forward*, §56).

### Priority 3 · filled in, using a technique the homework drills

#### Pullbacks in coordinates · P3

In charts $(x^i)$ on $M$ and $(y^j)$ on $N$ with $F^j=y^j\circ F$: $F^\ast(\sum_j\theta_j\,dy^j)=\sum_i(\sum_j(\theta_j\circ F)\,\partial F^j/\partial x^i)\,dx^i$; in particular $F^\ast\theta$ is smooth, see Proposition [[§51 One-Forms#^prop-51-5|§51.5]]. *Source: filled in.*

^nd-prop-51-5

- [ ] Q1 **[state]** State the formula and the smoothness claim.
- [ ] Q2 Why does it suffice to evaluate both sides on the basis vectors $\partial/\partial x^i|_p$?
- [ ] Q3 Evaluate the left side on $\partial/\partial x^i|_p$, using the matrix of $F_{\ast p}$.
- [ ] Q4 Why are the coefficients $c_i$ smooth? Which proposition then gives smoothness of $F^\ast\theta$?
- [ ] Q5 **[why]** The formula needs $F(U)\subseteq V$. What do you do if the chart at $p$ is not mapped into $V$, and why does that not change the conclusion?
- [ ] Q6 Compute $\gamma^\ast(x\,dy-y\,dx)$ for $\gamma(t)=(\cos t,\sin t)$.

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S1.
> - $F_{\ast p}(\partial/\partial x^i|_p)=\sum_j\frac{\partial F^j}{\partial x^i}(p)\,\partial/\partial y^j|_{F(p)}$ (Theorem [[§30 The Differential in Coordinates#^thm-30-2|§30.2]]).
> - $\theta_j\circ F$ and $\partial F^j/\partial x^i$ are smooth (Lemma [[§29 Coordinate Derivations and the Basis Theorem#^lem-29-1|§29.1]]); Proposition [[§51 One-Forms#^prop-51-1|§51.1]](3).
> - Shrink $U$ to $U\cap F^{-1}(V)$ (Lemma [[§19 Smooth Functions and Smooth Maps#^lem-19-3|§19.3]]).
> - Q6: $dt$.

#### The Hessian at a critical point is well defined · P3

At $p\in\operatorname{Crit}(f)$, $\sum_{i,j}H_{ij}(p)v^iw^j$ (with $v^i=v[x^i]$, $w^j=w[x^j]$) does not depend on the chart and is bilinear and symmetric in $(v,w)$: the Hessian $\operatorname{Hess}_pf$, see Proposition [[§52 Critical Points and the Hessian#^prop-52-3|§52.3]]. *Source: filled in.*

^nd-prop-52-3

- [ ] Q1 **[state]** State the proposition, and the resulting definition of $\operatorname{Hess}_pf$ (Definition [[§52 Critical Points and the Hessian#^def-52-2|§52.2]]).
- [ ] Q2 How do the components of $v$ transform from the chart $(x^i)$ to $(y^k)$?
- [ ] Q3 Substitute into $\sum_{k,l}H^{(y)}_{kl}v^{(y)k}w^{(y)l}$ and use Proposition [[§52 Critical Points and the Hessian#^prop-52-2|§52.2]] at the critical point.
- [ ] Q4 Why is the expression bilinear, and why symmetric?
- [ ] Q5 **[why]** Why must $p$ be a critical point? Which example shows that no chart-free Hessian exists at a regular point?
- [ ] Q6 **[def]** Define a nondegenerate critical point and a Morse function (Definitions [[§52 Critical Points and the Hessian#^def-52-3|§52.3]], [[§52 Critical Points and the Hessian#^def-52-4|§52.4]]).

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S2 (define in a chart, check independence).
> - $v^{(y)k}=v[y^k]=\sum_iJ_{ki}v^i$ (Corollary [[§30 The Differential in Coordinates#^cor-30-4|§30.4]](2)).
> - $\sum_{k,l}J_{ki}H^{(y)}_{kl}J_{lj}=H^{(x)}_{ij}$ at a critical point.
> - Symmetry: $H_{ij}=H_{ji}$ (Clairaut, Proposition [[§52 Critical Points and the Hessian#^prop-52-1|§52.1]](2)).
> - Q5: Example [[§52 Critical Points and the Hessian#^ex-52-1|§52.1]].

#### Morse functions on compact manifolds · P3

$\operatorname{Crit}(f)$ is closed for any smooth $f$; if $f$ is Morse and $M$ is compact, $\operatorname{Crit}(f)$ is finite, see Corollary [[§52 Critical Points and the Hessian#^cor-52-12|§52.12]]. *Source: filled in.*

^nd-cor-52-12

- [ ] Q1 **[state]** State both parts.
- [ ] Q2 (1) Give an argument that $M\setminus\operatorname{Crit}(f)$ is open, using a partial derivative $\partial f/\partial x^j$ that is nonzero at a regular point.
- [ ] Q3 (1) Give a second argument using $s_f$ and the zero section.
- [ ] Q4 (2) Why is $\operatorname{Crit}(f)$ compact, and why does isolatedness make it finite?
- [ ] Q5 **[why]** Is compactness needed in (2)? Show that $\sin x$ on $\mathbb{R}$ is a Morse function with infinitely many critical points.

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S13 (compactness upgrades local to global).
> - (1) Corollary [[§36 Submersions#^cor-36-8|§36.8]]; or $\operatorname{Crit}(f)=s_f^{-1}(\mathcal Z)$ with $\mathcal Z$ closed.
> - (2) Closed in compact ⇒ compact (Proposition [[§1 Point-Set Topology Review#^prop-1-8|§1.8]]); the open cover by the singletons $W_p\cap\operatorname{Crit}(f)=\{p\}$ (Corollary [[§52 Critical Points and the Hessian#^cor-52-11|§52.11]]) has a finite subcover.
> - Q5: at $\cos x=0$, $(\sin)''=-\sin x=\mp1\neq0$.

# T11. Vector fields and Lie groups

## Definitions T11

### Priority 2 · stated or done in class

#### Vector field · P2

A smooth map $\mathbf{X} : M \to TM$ with $\mathbf{X}(p) \in T_pM$ for every $p$, i.e. a section of $TM$, see Definition [[§53 Vector Fields#^def-53-1|§53.1]]. *Source: Lecture 13.*

^nd-def-53-1

- [ ] Q1 **[def]** State the definition, in both forms. Which smooth structure on $TM$ is meant?
- [ ] Q2 **[use]** In a chart, $\mathbf{X} = \sum_j \mathbf{X}^j\,\partial/\partial x^j$. Prove $\mathbf{X}$ is smooth on $U$ iff the $\mathbf{X}^j$ are smooth.
- [ ] Q3 **[why]** Drop "smooth": give a rough section of $T\mathbb{R}$ that is not a vector field. Which test detects smoothness without charts?
- [ ] Q4 **[use]** Why is $f \mapsto \mathbf{X}f$, $(\mathbf{X}f)(p) = \mathbf{X}_p[f]$, a derivation of $C^\infty(M)$, and why does every derivation arise this way?
- [ ] Q5 **[example]** Give the coordinate fields $\partial/\partial x^j$ on a chart domain; why are they only local vector fields?

> [!tip]- Hints: where it lives, examples
> - Definition [[§53 Vector Fields#^def-53-1|§53.1]]; Q2: Proposition [[§53 Vector Fields#^prop-53-1|§53.1]].
> - Q3: $p \mapsto \mathbf{1}_{p > 0}\,\partial/\partial r|_p$ (not in the notes); Lemma [[§53 Vector Fields#^lem-53-8|§53.8]] ($\mathbf{X}f$ smooth for every $f$).
> - Q4: Lemma [[§53 Vector Fields#^lem-53-3|§53.3]], Proposition [[§53 Vector Fields#^prop-53-7|§53.7]]. Q5: the trivialization frame, the remark *Trivializations and Frames* in [[§49 The Tangent Bundle|§49]].

#### Derivation of $C^\infty(M)$ · P2

An $\mathbb{R}$-linear $D : C^\infty(M) \to C^\infty(M)$ with $D(fg) = f\,Dg + g\,Df$, see Definition [[§53 Vector Fields#^def-53-5|§53.5]]. *Source: Lecture 16.*

^nd-def-53-5

- [ ] Q1 **[def]** State the definition, and compare it with a derivation at a point.
- [ ] Q2 **[use]** Prove every derivation is local: $f = g$ on open $U$ implies $Df = Dg$ on $U$. Which auxiliary function is used?
- [ ] Q3 **[use]** Prove every derivation is $D_\mathbf{X}$ for a unique vector field $\mathbf{X}$. How is $\mathbf{X}_p$ defined, and why is it a derivation on germs?
- [ ] Q4 **[why]** Is the composite $\mathbf{X} \circ \mathbf{Y}$ of two derivations a derivation? What is the correction term?

> [!tip]- Hints: where it lives, examples
> - Definition [[§53 Vector Fields#^def-53-4|§53.4]], Definition [[§53 Vector Fields#^def-53-5|§53.5]], Definition [[§53 Vector Fields#^def-53-6|§53.6]]; Q2: Lemma [[§53 Vector Fields#^lem-53-6|§53.6]] (a bump function, Definition [[§53 Vector Fields#^def-53-9|§53.9]]).
> - Q3: Proposition [[§53 Vector Fields#^prop-53-7|§53.7]] ($\mathbf{X}_p[f] = (D\tilde f)(p)$ with $\tilde f$ a global representative, Corollary [[§53 Vector Fields#^cor-53-5|§53.5]]).
> - Q4: no; $\mathbf{X}\mathbf{Y}(fg)$ has the extra terms $(\mathbf{X}f)(\mathbf{Y}g) + (\mathbf{Y}f)(\mathbf{X}g)$, which cancel in the bracket, Lemma [[§55 Lie Bracket and Lie Algebra#^lem-55-1|§55.1]].

#### Bump function · P2

A compactly supported smooth $\chi$ with $\chi \equiv 1$ near $p$, see Definition [[§53 Vector Fields#^def-53-9|§53.9]]. *Source: Lecture 16.*

^nd-def-53-9

- [ ] Q1 **[def]** Define the support, $C^\infty_0(M)$, and a bump function at $p$ (subordinate to $U$).
- [ ] Q2 **[why]** Why is the support defined as a closure? What would go wrong in "$\chi f$ extended by $0$ is smooth" otherwise?
- [ ] Q3 **[use]** Where are bump functions used: germs with global representatives, locality of derivations, global versus germ tangent spaces.
- [ ] Q4 **[example]** Build a bump function on $\mathbb{R}$ from $h(s) = e^{-1/s}$ ($s > 0$), $h = 0$ ($s \le 0$).

> [!tip]- Hints: where it lives, examples
> - Definition [[§53 Vector Fields#^def-53-7|§53.7]], Definition [[§53 Vector Fields#^def-53-8|§53.8]], Definition [[§53 Vector Fields#^def-53-9|§53.9]]; existence: Proposition [[§53 Vector Fields#^prop-53-4|§53.4]] (quoted; Uribe: lower priority).
> - Q2: smoothness of the extension at points of $\partial U$ needs $\chi = 0$ on a neighbourhood of them. Q3: Corollary [[§53 Vector Fields#^cor-53-5|§53.5]], Lemma [[§53 Vector Fields#^lem-53-6|§53.6]], Proposition [[§28 Derivations and the Abstract Tangent Space#^prop-28-3|§28.3]].
> - Q4: $\chi(x) = \dfrac{h(2 - |x|)}{h(2 - |x|) + h(|x| - 1)}$, equal to $1$ on $[-1, 1]$ (not in the notes; check it).

#### Lie bracket of vector fields · P2

$[\mathbf{X}, \mathbf{Y}]f = \mathbf{X}(\mathbf{Y}f) - \mathbf{Y}(\mathbf{X}f)$, see Definition [[§55 Lie Bracket and Lie Algebra#^def-55-1|§55.1]]. *Source: Lecture 16.*

^nd-def-55-1

- [ ] Q1 **[def]** State the definition, as an operator on $C^\infty(M)$.
- [ ] Q2 **[use]** Prove $[\mathbf{X}, \mathbf{Y}]$ is a derivation, hence a vector field.
- [ ] Q3 **[class exercise, Lecture 16]** Derive the bracket in coordinates, $\sum_j \big(\mathbf{X}(Y^j) - \mathbf{Y}(X^j)\big)\,\partial_j$ ("an exercise in multivariable calculus"). Where do the second derivatives cancel?
- [ ] Q4 **[why]** Why is $\mathbf{X} \circ \mathbf{Y}$ alone not a vector field (what is its order as a differential operator)?
- [ ] Q5 **[example]** Compute $[a\,\partial_x, b\,\partial_y]$ on $\mathbb{R}^2$.

> [!tip]- Hints: where it lives, examples
> - Definition [[§55 Lie Bracket and Lie Algebra#^def-55-1|§55.1]]; Q2: Lemma [[§55 Lie Bracket and Lie Algebra#^lem-55-1|§55.1]]. Q3: Proposition [[§55 Lie Bracket and Lie Algebra#^prop-55-2|§55.2]] (equality of mixed partials).
> - Q4: it has order $2$; Proposition [[§55 Lie Bracket and Lie Algebra#^prop-55-6|§55.6]] (commutators lower the order). Q5: Example [[§55 Lie Bracket and Lie Algebra#^ex-55-1|§55.1]].

#### Lie algebra · P2

A real vector space with a bilinear, skew-symmetric bracket satisfying the Jacobi identity, see Definition [[§55 Lie Bracket and Lie Algebra#^def-55-2|§55.2]]. *Source: Lecture 16.*

^nd-def-55-2

- [ ] Q1 **[def]** State the definition with the Jacobi identity.
- [ ] Q2 **[example]** Why is $\mathrm{Mat}(n, \mathbb{R})$ with $[A, B] = AB - BA$ a Lie algebra? Why is $\mathbb{R}^3$ with the cross product one?
- [ ] Q3 **[use]** Why is $(\mathfrak{X}(M), [\cdot, \cdot])$ a Lie algebra? Which general fact about associative products gives Jacobi for free?
- [ ] Q4 **[why]** Is $\mathfrak{X}(M)$ a Lie algebra over $C^\infty(M)$? Compute $[f\mathbf{X}, \mathbf{Y}]$.

> [!tip]- Hints: where it lives, examples
> - Definition [[§55 Lie Bracket and Lie Algebra#^def-55-2|§55.2]]; Q2: Example [[§55 Lie Bracket and Lie Algebra#^ex-55-2|§55.2]], Example [[§55 Lie Bracket and Lie Algebra#^ex-55-3|§55.3]]. Q3: Proposition [[§55 Lie Bracket and Lie Algebra#^prop-55-4|§55.4]], Corollary [[§55 Lie Bracket and Lie Algebra#^cor-55-5|§55.5]].
> - Q4: no: $[f\mathbf{X}, \mathbf{Y}] = f[\mathbf{X}, \mathbf{Y}] - (\mathbf{Y}f)\mathbf{X}$, not $C^\infty(M)$-bilinear.

#### Pushforward of a vector field by a diffeomorphism · P2

$(F_\ast\mathbf{X})_q = dF_{F^{-1}(q)}(\mathbf{X}_{F^{-1}(q)})$, see Definition [[§56 Related Vector Fields#^def-56-1|§56.1]]. *Source: Lecture 17.*

^nd-def-56-1

- [ ] Q1 **[def]** State the definition. Why must $F$ be a diffeomorphism?
- [ ] Q2 **[why]** Give the two obstructions to pushing a field forward along a general smooth map.
- [ ] Q3 **[use]** Show $F_\ast\mathbf{X}$ is smooth, is the unique field $F$-related to $\mathbf{X}$, and $(F_\ast\mathbf{X})g = (\mathbf{X}(g \circ F)) \circ F^{-1}$.
- [ ] Q4 **[use]** Why do diffeomorphisms preserve brackets: $F_\ast[\mathbf{X}, \mathbf{Y}] = [F_\ast\mathbf{X}, F_\ast\mathbf{Y}]$?

> [!tip]- Hints: where it lives, examples
> - Definition [[§56 Related Vector Fields#^def-56-1|§56.1]]; Q2: the remark *Vector Fields Do Not Push Forward* in [[§56 Related Vector Fields|§56]].
> - Q3: Proposition [[§56 Related Vector Fields#^prop-56-2|§56.2]]. Q4: Corollary [[§56 Related Vector Fields#^cor-56-4|§56.4]].

#### $F$-related vector fields · P2

$\mathbf{X} \in \mathfrak{X}(M)$ and $\mathbf{Y} \in \mathfrak{X}(N)$ are $F$-related if $dF_p(\mathbf{X}_p) = \mathbf{Y}_{F(p)}$ for every $p \in M$, see Definition [[§56 Related Vector Fields#^def-56-2|§56.2]]. *Source: Lecture 17.*

^nd-def-56-2

- [ ] Q1 **[def]** State the definition.
- [ ] Q2 **[use]** Prove: $\mathbf{X}$ and $\mathbf{Y}$ are $F$-related iff $\mathbf{X}(g \circ F) = (\mathbf{Y}g) \circ F$ for all $g \in C^\infty(N)$.
- [ ] Q3 **[class exercise, Lecture 17]** Prove the naturality of the bracket: if $\mathbf{X}_i$ is $F$-related to $\mathbf{Y}_i$ ($i = 1, 2$), then $[\mathbf{X}_1, \mathbf{X}_2]$ is $F$-related to $[\mathbf{Y}_1, \mathbf{Y}_2]$ ("you just play with the symbols; it all comes out").
- [ ] Q4 **[why]** For $\pi(x, y) = x$ and $\mathbf{Y} = b(x)\,d/dx$, which fields on $\mathbb{R}^2$ are $\pi$-related to $\mathbf{Y}$? Why is the $F$-related field not unique, and when can none exist?
- [ ] Q5 **[use]** Restate left-invariance of a field on a Lie group as relatedness.

> [!tip]- Hints: where it lives, examples
> - Definition [[§56 Related Vector Fields#^def-56-2|§56.2]]; Q2: Proposition [[§56 Related Vector Fields#^prop-56-1|§56.1]] ($\mathbf{X} \circ F^\ast = F^\ast \circ \mathbf{Y}$).
> - Q3: Proposition [[§56 Related Vector Fields#^prop-56-3|§56.3]] (omitted in Lecture 17 as an exercise; apply Q2 twice).
> - Q4: Example [[§56 Related Vector Fields#^ex-56-1|§56.1]] ($c(x, y)\,\partial_y$ arbitrary); none if $F$ is not injective and the values disagree. Q5: Lemma [[§57 Lie Groups and Left-Invariant Vector Fields#^lem-57-3|§57.3]].

## Proofs T11

### Priority 2 · stated or done in class

#### Vector fields in coordinates · P2

For a section $\mathbf X$ of $TM$ (not assumed smooth) and a chart $(U,(x^j))$: $\mathbf X=\sum_j\mathbf X^j\,\partial/\partial x^j$ on $U$ with $\mathbf X^j(p)=\mathbf X_p[x^j]=dx^j|_p(\mathbf X_p)$, and $\mathbf X$ is smooth on $U$ iff the $\mathbf X^j$ are, see Proposition [[§53 Vector Fields#^prop-53-1|§53.1]]. *Source: stated in Lecture 15, "analogously" to one-forms; filled in.*

^nd-prop-53-1

- [ ] Q1 **[state]** State the proposition. **[def]** Define a vector field (Definition [[§53 Vector Fields#^def-53-1|§53.1]]).
- [ ] Q2 Why is $\mathbf X_p=\sum_j\mathbf X_p[x^j]\,\partial/\partial x^j|_p$, and why is $\mathbf X_p[x^j]=dx^j|_p(\mathbf X_p)$?
- [ ] Q3 Compute the coordinate representation $\tilde\varphi\circ\mathbf X\circ\varphi^{-1}$ in the charts of $M$ and $TM$.
- [ ] Q4 Prove both directions of the smoothness criterion; where is continuity of $\mathbf X$ checked?
- [ ] Q5 **[why]** Why does the proposition start from a section "not assumed smooth"? Where is this used later (derivations, left-invariant extensions)?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S1, S9.
> - Universal formula (Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]]) and Proposition [[§32 The Cotangent Space#^prop-32-2|§32.2]].
> - $\tilde\varphi\circ\mathbf X\circ\varphi^{-1}(r)=(r,\mathbf X^1(\varphi^{-1}(r)),\dots,\mathbf X^m(\varphi^{-1}(r)))$.
> - Continuity: $\mathbf X=\tilde\varphi^{-1}\circ(\tilde\varphi\circ\mathbf X\circ\varphi^{-1})\circ\varphi$ (Proposition [[§49 The Tangent Bundle#^prop-49-1|§49.1]]).
> - Q5: Proposition [[§53 Vector Fields#^prop-53-7|§53.7]] step 4 and Proposition [[§57 Lie Groups and Left-Invariant Vector Fields#^prop-57-6|§57.6]] build a section first and prove smoothness after.

#### A vector field is a derivation · P2

For $\mathbf X\in\mathfrak X(M)$, $D_{\mathbf X}f:p\mapsto\mathbf X_p[f]$ is smooth, $D_{\mathbf X}f=\sum_j\mathbf X^j\,\partial f/\partial x^j$ in a chart, and $D_{\mathbf X}$ is a derivation of $C^\infty(M)$, see Lemma [[§53 Vector Fields#^lem-53-3|§53.3]]. *Source: Lecture 15 (linearity and product rule "an immediate consequence of the corresponding properties for tangent vectors"); smoothness filled in.* **[class exercise, Lecture 15]**

^nd-lem-53-3

- [ ] Q1 **[state]** State the lemma. **[def]** Define a derivation of $C^\infty(M)$ (Definition [[§53 Vector Fields#^def-53-5|§53.5]]) and compare it with a derivation at a point.
- [ ] Q2 Derive the chart formula for $(D_{\mathbf X}f)(p)$.
- [ ] Q3 Why is $D_{\mathbf X}f$ smooth? Write $(D_{\mathbf X}f)\circ\varphi^{-1}$ in terms of $\mathbf X^j\circ\varphi^{-1}$ and $\partial f_\varphi/\partial r^j$.
- [ ] Q4 Prove linearity and the product rule pointwise, using germs.
- [ ] Q5 **[why]** Which step needs $\mathbf X$ to be smooth, and not merely a section? What would $D_{\mathbf X}$ fail to be for a non-smooth section?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S1, pointwise properties.
> - $\mathbf X_p=\sum_j\mathbf X^j(p)\,\partial/\partial x^j|_p$ applied to $[f]$.
> - $\mathbf X^j$ smooth by Proposition [[§53 Vector Fields#^prop-53-1|§53.1]]; $f_\varphi$ smooth.
> - The germ of $fg$ is $[f][g]$ (Proposition [[§27 Germs#^prop-27-2|§27.2]]); Leibniz rule of $\mathbf X_p$ (Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-1|§28.1]]).
> - Q5: smoothness of $D_{\mathbf X}f$ (an operator on $C^\infty(M)$ must land in $C^\infty(M)$); compare Lemma [[§53 Vector Fields#^lem-53-8|§53.8]].

#### Every germ has a global representative · P2

If $f\in C^\infty(U)$ represents a germ at $p$ and $\chi$ is a bump function at $p$ subordinate to $U$, then $\tilde f=\chi f$ on $U$, $0$ outside $U$, is smooth on $M$ and has the same germ at $p$; bump functions exist (Proposition [[§53 Vector Fields#^prop-53-4|§53.4]], quoted), see Corollary [[§53 Vector Fields#^cor-53-5|§53.5]]. *Source: Lecture 16; the existence of bump functions is stated in Lectures 15–16, proof deferred ("technical things that you will not be using in homework").*

^nd-cor-53-5

- [ ] Q1 **[state]** State the corollary, and the existence of bump functions. **[def]** Define support, $C^\infty_0(M)$ and a bump function at $p$ (Definitions [[§53 Vector Fields#^def-53-7|§53.7]]–[[§53 Vector Fields#^def-53-9|§53.9]]).
- [ ] Q2 Which two open sets cover $M$, and why is $\tilde f$ smooth on each?
- [ ] Q3 Why does $\tilde f$ represent the same germ as $f$ at $p$?
- [ ] Q4 **[why]** Why must the support be the *closure* of $\{\chi\neq0\}$? Where would the proof break with the non-closed set? Why can a bump function not be analytic?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S11 (local, then global).
> - $U$ and $M\setminus\operatorname{supp}\chi$ (open because the support is closed); they cover since $\operatorname{supp}\chi\subseteq U$.
> - $\chi\equiv1$ on an open $V\ni p$, so $\tilde f=f$ on $V\cap U$ (Definition [[§27 Germs#^def-27-1|§27.1]]).
> - Q4: $M\setminus\operatorname{supp}\chi$ must be open; an analytic function equal to $1$ on an open set is $1$ on the connected domain.

#### Derivations are local · P2

Every derivation $D$ of $C^\infty(M)$ is local: if $f|_U=g|_U$ for an open $U$, then $(Df)|_U=(Dg)|_U$, see Lemma [[§53 Vector Fields#^lem-53-6|§53.6]]. *Source: Lecture 16, in full ("you'll see how incredibly powerful the product rule is").*

^nd-lem-53-6

- [ ] Q1 **[state]** State the lemma. **[def]** Define a local operator (Definition [[§53 Vector Fields#^def-53-6|§53.6]]).
- [ ] Q2 Reduce to: $h|_U=0$ ⇒ $(Dh)|_U=0$. Why does linearity allow this?
- [ ] Q3 Fix $p\in U$ and a bump function $\chi$ at $p$ subordinate to $U$. Why is $\chi h$ the zero function?
- [ ] Q4 Apply the product rule to $D(\chi h)$ and evaluate at $p$.
- [ ] Q5 **[why]** Which two ingredients make the proof work? Is an arbitrary $\mathbb{R}$-linear operator on $C^\infty(M)$ local? (Think of $f\mapsto f(q_0)\cdot1$.)

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S11; "like showing injectivity by showing the kernel is zero".
> - $\chi h=0$: on $U$, $h=0$; off $U$, $\chi=0$.
> - $0=\chi(p)(Dh)(p)+h(p)(D\chi)(p)=(Dh)(p)$.
> - Ingredients: the product rule and bump functions (Proposition [[§53 Vector Fields#^prop-53-4|§53.4]]).

#### Derivations are vector fields · P2

Every derivation $D$ of $C^\infty(M)$ is $D_{\mathbf X}$ for a unique $\mathbf X\in\mathfrak X(M)$, see Proposition [[§53 Vector Fields#^prop-53-7|§53.7]]. *Source: Lecture 16, in the lecture's steps; the smoothness details ("I'm going to skip a little bit the details"), the derivation property of $\mathbf X_p$ and uniqueness are filled in.* **[class exercise, Lecture 16]**

^nd-prop-53-7

- [ ] Q1 **[state]** State the proposition.
- [ ] Q2 Define $\mathbf X_p(\gamma)$ for a germ $\gamma$ at $p$. Which corollary supplies a global representative?
- [ ] Q3 Why is $\mathbf X_p(\gamma)$ well defined? Which lemma is used?
- [ ] Q4 Why is each $\mathbf X_p$ a derivation at $p$?
- [ ] Q5 Why is $\mathbf X$ smooth? Use one bump function and the extensions $\tilde x^j=\chi x^j$ to compute the coefficients on a neighbourhood $V$.
- [ ] Q6 Why is $D_{\mathbf X}=D$, and why is $\mathbf X$ unique?
- [ ] Q7 **[why]** Why is the result "not an immediate thing at all"? What is the mismatch between tangent vectors and derivations of $C^\infty(M)$ that locality and bump functions repair?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S11, S9.
> - $\mathbf X_p(\gamma)=(Df)(p)$ with $[f]=\gamma$, $f\in C^\infty(M)$ (Corollary [[§53 Vector Fields#^cor-53-5|§53.5]]).
> - Two representatives agree on an open $W\ni p$; Lemma [[§53 Vector Fields#^lem-53-6|§53.6]].
> - Linearity and Leibniz of $D$ evaluated at $p$.
> - Smoothness: $\mathbf X^j(q)=\mathbf X_q(x^j)=D(\tilde x^j)(q)$ for $q\in V$, a smooth function; Proposition [[§53 Vector Fields#^prop-53-1|§53.1]].
> - Tangent vectors act on germs (local), $D$ acts on global functions.

#### A smoothness criterion for vector fields · P2

A section $\mathbf X$ of $TM$ is smooth iff $\mathbf Xf:p\mapsto\mathbf X_p[f]$ is smooth for every $f\in C^\infty(M)$, see Lemma [[§53 Vector Fields#^lem-53-8|§53.8]]. *Source: filled in, for Lecture 17's theorem on Lie algebras (the argument is step 4 of Proposition [[§53 Vector Fields#^prop-53-7|§53.7]]; Lecture 18 used it).*

^nd-lem-53-8

- [ ] Q1 **[state]** State the criterion.
- [ ] Q2 (⇒) Which lemma gives it?
- [ ] Q3 (⇐) Fix $p$ and a chart; why are the coefficients $\mathbf X^j$ equal to $\mathbf X\tilde x^j$ near $p$, for the extensions $\tilde x^j=\chi x^j$?
- [ ] Q4 Conclude with the coordinate criterion.
- [ ] Q5 **[why]** Why can one not simply apply the hypothesis to the coordinate functions $x^j$ themselves?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S11, S9.
> - (⇒) Lemma [[§53 Vector Fields#^lem-53-3|§53.3]].
> - On $V$ (where $\chi\equiv1$), $\tilde x^j$ and $x^j$ have the same germ, so $\mathbf X_q[x^j]=\mathbf X_q[\tilde x^j]$.
> - Q5: $x^j$ is only defined on the chart domain, not in $C^\infty(M)$.

#### Vector fields and multiplication operators · P2

$m_g\circ D_{\mathbf X}=D_{g\mathbf X}$ and $D_{\mathbf X}\circ m_g=m_g\circ D_{\mathbf X}+m_{\mathbf Xg}$; for instance $[\partial,m_x]=\mathrm{id}$ on $\mathbb{R}$, see Proposition [[§54 Differential Operators#^prop-54-2|§54.2]]. *Source: filled in (Lecture 15 introduced the ring of differential operators in passing).*

^nd-prop-54-2

- [ ] Q1 **[state]** State both identities. **[def]** Define the multiplication operator $m_g$ and the ring of differential operators (Definitions [[§54 Differential Operators#^def-54-1|§54.1]], [[§54 Differential Operators#^def-54-2|§54.2]]).
- [ ] Q2 Prove the first identity at a function $f$ and a point $p$.
- [ ] Q3 Prove the second identity from the product rule of $D_{\mathbf X}$.
- [ ] Q4 Use it to show $\partial\circ m_x-m_x\circ\partial=\mathrm{id}$ on $\mathbb{R}$ (Example [[§54 Differential Operators#^ex-54-2|§54.2]]).
- [ ] Q5 **[why]** The operator $\partial\circ m_x-m_x\circ\partial$ is written with a vector field in each term. What is its order, and why does that show the order is not "the number of vector fields in an expression"?

> [!tip]- Hints: route of the proof in the notes
> - $(m_g\circ D_{\mathbf X}f)(p)=g(p)\mathbf X_p[f]=(g\mathbf X)_p[f]$.
> - $D_{\mathbf X}(gf)=g\,D_{\mathbf X}f+f\,D_{\mathbf X}g$.
> - $\mathbf Xx=x'=1$ and $m_1=\mathrm{id}$.
> - Order $0$ (Definition [[§54 Differential Operators#^def-54-3|§54.3]]): it equals $\mathrm{id}$.

#### The bracket of vector fields is a vector field · P2

For $\mathbf X,\mathbf Y\in\mathfrak X(M)$, $[\mathbf X,\mathbf Y]f=\mathbf X(\mathbf Yf)-\mathbf Y(\mathbf Xf)$ is a derivation of $C^\infty(M)$, hence a vector field, see Lemma [[§55 Lie Bracket and Lie Algebra#^lem-55-1|§55.1]]. *Source: Lecture 16 ("tedious algebra ... the key thing is the product rule"; "linearity of the commutator is trivial. Check").* **[class exercise, Lecture 16]**

^nd-lem-55-1

- [ ] Q1 **[state]** State the lemma. **[def]** Define the Lie bracket of vector fields (Definition [[§55 Lie Bracket and Lie Algebra#^def-55-1|§55.1]]).
- [ ] Q2 Why does $[\mathbf X,\mathbf Y]$ map $C^\infty(M)$ to $C^\infty(M)$?
- [ ] Q3 Prove linearity.
- [ ] Q4 Expand $\mathbf X(\mathbf Y(fg))$ and $\mathbf Y(\mathbf X(fg))$. Which terms cancel in the difference, and why?
- [ ] Q5 Which proposition turns the derivation into a vector field?
- [ ] Q6 **[why]** Is the composite $\mathbf X\circ\mathbf Y$ a derivation? Test the product rule on $fg$ and name the extra terms.

> [!tip]- Hints: route of the proof in the notes
> - Strategy: algebra with the product rule; S9.
> - $\mathbf Yf$ is smooth (Lemma [[§53 Vector Fields#^lem-53-3|§53.3]]), so $\mathbf X(\mathbf Yf)$ is.
> - Cross terms $\mathbf Xf\,\mathbf Yg$ and $\mathbf Xg\,\mathbf Yf$ appear in both expansions and cancel.
> - Proposition [[§53 Vector Fields#^prop-53-7|§53.7]].
> - Q6: $\mathbf X\mathbf Y(fg)$ contains $\mathbf Xf\,\mathbf Yg+\mathbf Xg\,\mathbf Yf$; it is second order.

#### A bracket in the plane · P2

For $\mathbf X=a\,\partial_x$, $\mathbf Y=b\,\partial_y$ on $\mathbb{R}^2$: $[\mathbf X,\mathbf Y]=a\,\frac{\partial b}{\partial x}\partial_y-b\,\frac{\partial a}{\partial y}\partial_x$, see Example [[§55 Lie Bracket and Lie Algebra#^ex-55-1|§55.1]]. *Source: Lecture 16 ("an exercise in multivariable calculus").* **[class exercise, Lecture 16]**

^nd-ex-55-1

- [ ] Q1 **[state]** State the formula.
- [ ] Q2 Why does it suffice to compare the two sides as operators on every $f\in C^\infty(\mathbb{R}^2)$?
- [ ] Q3 Compute $\mathbf X\mathbf Yf$ and $\mathbf Y\mathbf Xf$.
- [ ] Q4 Why do the second-order terms cancel?
- [ ] Q5 **[why]** Compute $[\partial_x,x\,\partial_y]$ and $[\partial_x,\partial_y]$. Is the bracket of two fields with constant coefficients always zero? Is the bracket $C^\infty(M)$-bilinear?

> [!tip]- Hints: route of the proof in the notes
> - A field is determined by its operator (uniqueness in Proposition [[§53 Vector Fields#^prop-53-7|§53.7]]).
> - $\mathbf X\mathbf Yf=a\,b_x f_y+ab\,f_{yx}$, $\mathbf Y\mathbf Xf=b\,a_y f_x+ba\,f_{xy}$.
> - Clairaut.
> - Q5: $[\partial_x,x\partial_y]=\partial_y$; $[\mathbf X,g\mathbf Y]=g[\mathbf X,\mathbf Y]+(\mathbf Xg)\mathbf Y$, so not $C^\infty$-bilinear.

#### The bracket in coordinates · P2

$[\mathbf X,\mathbf Y]=\sum_j(\mathbf X(Y^j)-\mathbf Y(X^j))\,\partial_j=\sum_j\sum_i(X^i\partial_iY^j-Y^i\partial_iX^j)\,\partial_j$, see Proposition [[§55 Lie Bracket and Lie Algebra#^prop-55-2|§55.2]]. *Source: filled in.*

^nd-prop-55-2

- [ ] Q1 **[state]** State the formula.
- [ ] Q2 Why is the $j$-th coefficient of $[\mathbf X,\mathbf Y]$ equal to $[\mathbf X,\mathbf Y]_p[x^j]$?
- [ ] Q3 The bracket acts on $C^\infty(M)$, but $x^j$ lives on $U$. How do you replace $x^j$ by a global function near $p$, and why does that not change $\mathbf Y\tilde x^j$ near $p$?
- [ ] Q4 Conclude $[\mathbf X,\mathbf Y]_p[x^j]=\mathbf X_p[Y^j]-\mathbf Y_p[X^j]$ and expand.
- [ ] Q5 **[why]** Without the bump-function step, which expression in the computation is not defined?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S9 (a field is determined by its values on coordinate functions), S11.
> - Proposition [[§53 Vector Fields#^prop-53-1|§53.1]] applied to the field $[\mathbf X,\mathbf Y]$.
> - $\tilde x^j=\chi x^j$ (Corollary [[§53 Vector Fields#^cor-53-5|§53.5]]); on $V$, $\mathbf Y\tilde x^j=Y^j$ and $\mathbf X\tilde x^j=X^j$.
> - Q5: $\mathbf Y(x^j)$ as an element of $C^\infty(M)$.

#### Commutators of an associative product · P2

The commutator $[X,Y]=X\ast Y-Y\ast X$ of a bilinear associative product is bilinear, skew-symmetric and satisfies the Jacobi identity, see Proposition [[§55 Lie Bracket and Lie Algebra#^prop-55-4|§55.4]]. *Source: stated in Lecture 16 as "a general fact" ("the key thing is that it be an associative product"); filled in.* **[class exercise, Lecture 16]**

^nd-prop-55-4

- [ ] Q1 **[state]** State the proposition. **[def]** Define a Lie algebra (Definition [[§55 Lie Bracket and Lie Algebra#^def-55-2|§55.2]]).
- [ ] Q2 Prove skew-symmetry and bilinearity.
- [ ] Q3 Expand $[X,[Y,Z]]$ into four words, and obtain the other two terms of the Jacobi identity by cyclic renaming.
- [ ] Q4 Check that each of the six words cancels.
- [ ] Q5 **[why]** Where is associativity used? Which example shows why the cross product on $\mathbb{R}^3$ is a Lie algebra without the "big computation"?

> [!tip]- Hints: route of the proof in the notes
> - Associativity lets you write $XYZ$ without parentheses.
> - $[X,[Y,Z]]=XYZ-XZY-YZX+ZYX$.
> - Q5: Example [[§55 Lie Bracket and Lie Algebra#^ex-55-3|§55.3]]: the hat map carries $\times$ to the matrix commutator.

#### Vector fields form a Lie algebra · P2

$(\mathfrak X(M),[\cdot,\cdot])$ is a Lie algebra, see Corollary [[§55 Lie Bracket and Lie Algebra#^cor-55-5|§55.5]]. *Source: Lecture 16 ("it comes from the product, which is the composition, which is associative"; Jacobi "I don't recommend you check by hand"); filled in.* **[class exercise, Lecture 16]**

^nd-cor-55-5

- [ ] Q1 **[state]** State the corollary.
- [ ] Q2 Why do the linear operators on $C^\infty(M)$ form an associative algebra under composition?
- [ ] Q3 Why is $\mathbf X\mapsto D_{\mathbf X}$ linear and injective, with $D_{[\mathbf X,\mathbf Y]}=[D_{\mathbf X},D_{\mathbf Y}]$?
- [ ] Q4 Transfer bilinearity, skew-symmetry and Jacobi from operators to fields.
- [ ] Q5 **[why]** Why is injectivity of $\mathbf X\mapsto D_{\mathbf X}$ needed for the transfer?

> [!tip]- Hints: route of the proof in the notes
> - Proposition [[§55 Lie Bracket and Lie Algebra#^prop-55-4|§55.4]] for the operators.
> - Injective: uniqueness in Proposition [[§53 Vector Fields#^prop-53-7|§53.7]]; closure under brackets: Lemma [[§55 Lie Bracket and Lie Algebra#^lem-55-1|§55.1]].
> - An identity between fields holds once it holds between their operators.

#### Related fields as operators · P2

$\mathbf X\in\mathfrak X(M)$ and $\mathbf Y\in\mathfrak X(N)$ are $F$-related iff $\mathbf X(g\circ F)=(\mathbf Yg)\circ F$ for every $g\in C^\infty(N)$, i.e. $\mathbf X\circ F^\ast=F^\ast\circ\mathbf Y$, see Proposition [[§56 Related Vector Fields#^prop-56-1|§56.1]]. *Source: Lecture 17 ("let's have a peek at the proof ... it should be easy to complete the details"); the converse is filled in.* **[class exercise, Lecture 17]**

^nd-prop-56-1

- [ ] Q1 **[state]** State the proposition. **[def]** Define $F$-related vector fields (Definition [[§56 Related Vector Fields#^def-56-2|§56.2]]).
- [ ] Q2 Compute $\mathbf X(g\circ F)(p)$ and $((\mathbf Yg)\circ F)(p)$ in terms of $dF_p(\mathbf X_p)$ and $\mathbf Y_{F(p)}$.
- [ ] Q3 Prove "related ⇒ intertwining".
- [ ] Q4 Prove "intertwining ⇒ related". Why do global functions $g$ suffice to test equality of two derivations at $F(p)$?
- [ ] Q5 **[why]** Without bump functions (global representatives of germs), which direction would fail?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S9, S11.
> - $\mathbf X_p[g\circ F]=dF_p(\mathbf X_p)[g]$ (Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-6|§28.6]]).
> - Every germ at $F(p)$ has a global representative (Corollary [[§53 Vector Fields#^cor-53-5|§53.5]]).

#### Fields related by a projection · P2

For $\pi(x,y)=x$ and $\mathbf Y=b(x)\,d/dx$ on $\mathbb{R}$, the fields on $\mathbb{R}^2$ that are $\pi$-related to $\mathbf Y$ are exactly $b(x)\,\partial_x+c(x,y)\,\partial_y$ with $c$ arbitrary, see Example [[§56 Related Vector Fields#^ex-56-1|§56.1]]. *Source: Lecture 17, a question to the class ("What can I put in the blanks here?"); the computation is filled in.* **[class exercise, Lecture 17]**

^nd-ex-56-1

- [ ] Q1 **[state]** State the example.
- [ ] Q2 Compute $d\pi(\partial_x|_{(x,y)})$ and $d\pi(\partial_y|_{(x,y)})$ by applying them to a germ $[g]$ at $x$.
- [ ] Q3 For $\mathbf X=a\,\partial_x+c\,\partial_y$, compute $d\pi(\mathbf X_{(x,y)})$ and derive the condition on $a$.
- [ ] Q4 Why is every such $b(x)\partial_x+c\,\partial_y$ a smooth vector field?
- [ ] Q5 **[why]** For $F$ not surjective or not injective, is there always a field $F$-related to a given $\mathbf X$? Give the two obstructions.

> [!tip]- Hints: route of the proof in the notes
> - $d\pi(\partial_x)[g]=\partial_x(g\circ\pi)=g'(x)$; $d\pi(\partial_y)=0$.
> - $a(x,y)\,d/dx|_x=b(x)\,d/dx|_x$ iff $a(x,y)=b(x)$.
> - Remark *Vector Fields Do Not Push Forward*: several candidates at one point, or none.

#### Pushforward by a diffeomorphism · P2

For a diffeomorphism $F$, $F_\ast\mathbf X$ (with $(F_\ast\mathbf X)_q=dF_{F^{-1}(q)}(\mathbf X_{F^{-1}(q)})$) is smooth, is the unique field $F$-related to $\mathbf X$, and $(F_\ast\mathbf X)g=(\mathbf X(g\circ F))\circ F^{-1}$, see Proposition [[§56 Related Vector Fields#^prop-56-2|§56.2]]. *Source: filled in.*

^nd-prop-56-2

- [ ] Q1 **[state]** State the proposition. **[def]** Define $F_\ast\mathbf X$ (Definition [[§56 Related Vector Fields#^def-56-1|§56.1]]).
- [ ] Q2 Derive the formula for $(F_\ast\mathbf X)g$.
- [ ] Q3 Why is $F_\ast\mathbf X$ smooth? Which criterion do you use?
- [ ] Q4 Why is it $F$-related to $\mathbf X$, and why is it the only one?
- [ ] Q5 **[why]** Which property of $F$ is used for smoothness, and which for uniqueness?

> [!tip]- Hints: route of the proof in the notes
> - $(F_\ast\mathbf X)_q[g]=\mathbf X_p[g\circ F]$, $p=F^{-1}(q)$.
> - Smoothness: Lemma [[§53 Vector Fields#^lem-53-8|§53.8]], since $F^{-1}$ is smooth.
> - Uniqueness: $F$ is onto, so every $q$ is some $F(p)$.

#### Naturality of the bracket · P2

If $\mathbf X_i$ is $F$-related to $\mathbf Y_i$ ($i=1,2$), then $[\mathbf X_1,\mathbf X_2]$ is $F$-related to $[\mathbf Y_1,\mathbf Y_2]$, see Proposition [[§56 Related Vector Fields#^prop-56-3|§56.3]]. *Source: omitted in Lecture 17 as an exercise ("it's just a matter of chasing the definitions"); filled in.* **[class exercise, Lecture 17]**

^nd-prop-56-3

- [ ] Q1 **[state]** State the proposition.
- [ ] Q2 Which characterization of relatedness do you use, and what must be shown?
- [ ] Q3 Compute $\mathbf X_1\mathbf X_2(g\circ F)$ in two steps. Why is $\mathbf Y_2g$ a legitimate function to apply relatedness to?
- [ ] Q4 Compute $\mathbf X_2\mathbf X_1(g\circ F)$ and subtract.
- [ ] Q5 **[why]** Why is the operator characterization the right tool here, rather than the definition with $dF_p$? What would you have to know about $[\mathbf X_1,\mathbf X_2]_p$ to use the definition directly?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: chase the definitions; Proposition [[§56 Related Vector Fields#^prop-56-1|§56.1]].
> - $\mathbf X_1\mathbf X_2(g\circ F)=\mathbf X_1((\mathbf Y_2g)\circ F)=(\mathbf Y_1\mathbf Y_2g)\circ F$; $\mathbf Y_2g\in C^\infty(N)$ by Lemma [[§53 Vector Fields#^lem-53-3|§53.3]].
> - The bracket is defined as an operator; its value at $p$ has no direct formula in terms of $\mathbf X_{1,p}$, $\mathbf X_{2,p}$.

#### Diffeomorphisms preserve brackets · P2

For a diffeomorphism $F$, $F_\ast[\mathbf X_1,\mathbf X_2]=[F_\ast\mathbf X_1,F_\ast\mathbf X_2]$, see Corollary [[§56 Related Vector Fields#^cor-56-4|§56.4]]. *Source: filled in.*

^nd-cor-56-4

- [ ] Q1 **[state]** State the corollary.
- [ ] Q2 Why is $[\mathbf X_1,\mathbf X_2]$ $F$-related to $[F_\ast\mathbf X_1,F_\ast\mathbf X_2]$?
- [ ] Q3 Which uniqueness statement finishes the proof?
- [ ] Q4 **[why]** For a smooth $F$ that is not a diffeomorphism, can the statement even be formulated? What replaces it?

> [!tip]- Hints: route of the proof in the notes
> - Proposition [[§56 Related Vector Fields#^prop-56-2|§56.2]] gives $\mathbf X_i$ related to $F_\ast\mathbf X_i$; then Proposition [[§56 Related Vector Fields#^prop-56-3|§56.3]].
> - The only field related to $[\mathbf X_1,\mathbf X_2]$ is $F_\ast[\mathbf X_1,\mathbf X_2]$.
> - Q4: $F_\ast$ is undefined; naturality for related fields replaces it.

## Not on the midterm: Lie groups

*Uribe's email (Oct 14): "Nothing about Lie groups is included." Kept for the final.*

#### Lie group

A topological group with a smooth structure in which multiplication and inversion are smooth, see Definition [[§57 Lie Groups and Left-Invariant Vector Fields#^def-57-1|§57.1]]. *Source: Lecture 16.*

^nd-def-57-1

- [ ] Q1 **[def]** State the definition.
- [ ] Q2 **[example]** Why are $\mathrm{GL}(n, \mathbb{R})$, $\mathrm{O}(n)$, $\mathrm{U}(n)$ Lie groups? What is the extra input for a subgroup cut out by equations?
- [ ] Q3 **[why]** Why is left translation $L_g$ a diffeomorphism? Which axioms are used?
- [ ] Q4 **[why]** Is every Lie group a matrix group?
- [ ] Q5 **[use]** Why does every Lie group have $T_gG = (L_g)_{\ast e}(T_eG)$, so that it is parallelizable?

> [!tip]- Hints: where it lives, examples
> - Definition [[§57 Lie Groups and Left-Invariant Vector Fields#^def-57-1|§57.1]], Definition [[§11 Topological Groups and Classical Matrix Groups#^def-11-1|§11.1]]; Q2: Proposition [[§57 Lie Groups and Left-Invariant Vector Fields#^prop-57-1|§57.1]] (restriction of smooth maps to a regular submanifold, Lemma [[§37 Regular Submanifolds#^lem-37-5|§37.5]]); Definition [[§57 Lie Groups and Left-Invariant Vector Fields#^def-57-7|§57.7]].
> - Q3: Lemma [[§57 Lie Groups and Left-Invariant Vector Fields#^lem-57-2|§57.2]] (inverse $L_{g^{-1}}$). Q4: no, the remark *Nonlinear Groups* in [[§57 Lie Groups and Left-Invariant Vector Fields|§57]].
> - Q5: left-invariant extension, Definition [[§57 Lie Groups and Left-Invariant Vector Fields#^def-57-5|§57.5]], Proposition [[§57 Lie Groups and Left-Invariant Vector Fields#^prop-57-6|§57.6]].

#### Left-invariant vector field

$\mathbf{X} \in \mathfrak{X}(G)$ with $(L_g)_{\ast h}\mathbf{X}_h = \mathbf{X}_{gh}$ for all $g, h$, see Definition [[§57 Lie Groups and Left-Invariant Vector Fields#^def-57-3|§57.3]]. *Source: Lecture 17.*

^nd-def-57-3

- [ ] Q1 **[def]** State the definition, and its form as "$L_g$-related to itself".
- [ ] Q2 **[example]** Find all left-invariant fields on $\mathrm{GL}(n, \mathbb{R})$, and on a vector space under addition.
- [ ] Q3 **[use]** Why is a left-invariant field determined by its value at $e$? Conversely, why is $g \mapsto (L_g)_{\ast e}v$ smooth?
- [ ] Q4 **[why]** Why is the bracket of two left-invariant fields left-invariant? What fails for right translations versus left, and where does the choice show?
- [ ] Q5 **[why]** Drop "smooth" from the definition of vector field: is $g \mapsto (L_g)_{\ast e}v$ automatically a vector field, or does that need proof?

> [!tip]- Hints: where it lives, examples
> - Definition [[§57 Lie Groups and Left-Invariant Vector Fields#^def-57-2|§57.2]], Definition [[§57 Lie Groups and Left-Invariant Vector Fields#^def-57-3|§57.3]]; Lemma [[§57 Lie Groups and Left-Invariant Vector Fields#^lem-57-3|§57.3]].
> - Q2: Example [[§57 Lie Groups and Left-Invariant Vector Fields#^ex-57-1|§57.1]] ($\mathbf{X}^A_g = gA$), Example [[§57 Lie Groups and Left-Invariant Vector Fields#^ex-57-2|§57.2]] (constant fields).
> - Q3: Lemma [[§57 Lie Groups and Left-Invariant Vector Fields#^lem-57-5|§57.5]], Proposition [[§57 Lie Groups and Left-Invariant Vector Fields#^prop-57-6|§57.6]], Theorem [[§57 Lie Groups and Left-Invariant Vector Fields#^thm-57-7|§57.7]]. Q4: Corollary [[§57 Lie Groups and Left-Invariant Vector Fields#^cor-57-4|§57.4]] (naturality), the remark *Why Left?* in [[§57 Lie Groups and Left-Invariant Vector Fields|§57]].
> - Q5: it needs proof (a "rough" field, Definition [[§57 Lie Groups and Left-Invariant Vector Fields#^def-57-5|§57.5]]), Proposition [[§57 Lie Groups and Left-Invariant Vector Fields#^prop-57-6|§57.6]].

#### Lie algebra of a Lie group

$\mathfrak{g}$, the left-invariant vector fields with the bracket of vector fields, identified with $T_eG$, see Definition [[§57 Lie Groups and Left-Invariant Vector Fields#^def-57-4|§57.4]]. *Source: Lectures 16–17.*

^nd-def-57-4

- [ ] Q1 **[def]** Define $\mathfrak{g}$ and the bracket on $T_eG$.
- [ ] Q2 **[use]** Prove $\mathrm{ev} : \mathfrak{g} \to T_eG$, $\mathbf{X} \mapsto \mathbf{X}_e$, is a linear isomorphism; so $\dim \mathfrak{g} = \dim G$.
- [ ] Q3 **[example]** Show the bracket on $T_I\mathrm{GL}(n, \mathbb{R}) = \mathrm{Mat}(n, \mathbb{R})$ is $AB - BA$.
- [ ] Q4 **[why]** Why is $\mathfrak{g}$ a Lie subalgebra of $\mathfrak{X}(G)$, although $\mathfrak{X}(G)$ is infinite-dimensional?
- [ ] Q5 **[use]** How does a Lie group morphism $F : H \to G$ induce a Lie algebra morphism?

> [!tip]- Hints: where it lives, examples
> - Definition [[§57 Lie Groups and Left-Invariant Vector Fields#^def-57-4|§57.4]], Definition [[§57 Lie Groups and Left-Invariant Vector Fields#^def-57-6|§57.6]]; Q2: Theorem [[§57 Lie Groups and Left-Invariant Vector Fields#^thm-57-7|§57.7]]. Q3: Theorem [[§57 Lie Groups and Left-Invariant Vector Fields#^thm-57-8|§57.8]].
> - Q4: Corollary [[§57 Lie Groups and Left-Invariant Vector Fields#^cor-57-4|§57.4]]. Q5: Definition [[§57 Lie Groups and Left-Invariant Vector Fields#^def-57-8|§57.8]], Definition [[§57 Lie Groups and Left-Invariant Vector Fields#^def-57-9|§57.9]], Lemma [[§57 Lie Groups and Left-Invariant Vector Fields#^lem-57-9|§57.9]], Proposition [[§57 Lie Groups and Left-Invariant Vector Fields#^prop-57-10|§57.10]].

#### The classical groups are Lie groups

$\mathrm{GL}(n,\mathbb{R})$, $\mathrm{GL}(n,\mathbb{C})$, $\mathrm{SL}(n,\mathbb{R})$, $\mathrm O(n)$, $\mathrm{SO}(n)$, $\mathrm U(n)$ and $\mathrm{SU}(2)$ are Lie groups, see Proposition [[§57 Lie Groups and Left-Invariant Vector Fields#^prop-57-1|§57.1]]. *Source: stated in Lecture 16 ("all the matrix groups that we have seen ... are Lie groups"); filled in.* **[class exercise, Lecture 16]**

^nd-prop-57-1

- [ ] Q1 **[state]** State the proposition. **[def]** Define a Lie group (Definition [[§57 Lie Groups and Left-Invariant Vector Fields#^def-57-1|§57.1]]).
- [ ] Q2 Each group is open in, or a regular submanifold of, a matrix space. Why is a smooth map into the matrix space with values in $G$ smooth into $G$, in both cases?
- [ ] Q3 Why is multiplication $G\times G\to G$ smooth?
- [ ] Q4 Why is inversion smooth?
- [ ] Q5 **[why]** Which step needs $G$ to be a subgroup (closed under products and inverses)? Which needs $G$ to be a submanifold or open, and not an arbitrary subgroup?

> [!tip]- Hints: route of the proof in the notes
> - Lemma [[§37 Regular Submanifolds#^lem-37-5|§37.5]](2) for submanifolds; restricted linear charts for open subsets (Theorem [[§25 The Geometric Tangent Space#^thm-25-5|§25.5]]).
> - Entries of $AB$ are polynomials; $(\iota\times\iota)$ is smooth.
> - $g^{-1}=\operatorname{adj}(g)/\det g$ on the open set of invertible matrices.

#### Left translations are diffeomorphisms

$L_g(h)=gh$ is a diffeomorphism of a Lie group $G$ with inverse $L_{g^{-1}}$, see Lemma [[§57 Lie Groups and Left-Invariant Vector Fields#^lem-57-2|§57.2]]. *Source: filled in, as for topological groups.*

^nd-lem-57-2

- [ ] Q1 **[state]** State the lemma.
- [ ] Q2 Write $L_g$ as a composite of a slice inclusion and multiplication. Why is it smooth?
- [ ] Q3 Why is $L_{g^{-1}}$ its inverse?
- [ ] Q4 **[why]** For $g\neq e$, $L_g$ is a diffeomorphism of $G$. Why is it not a Lie group morphism?

> [!tip]- Hints: route of the proof in the notes
> - $L_g=\mu\circ\iota^g$ (Definition [[§19 Smooth Functions and Smooth Maps#^def-19-8|§19.8]], Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-11|§19.11]]).
> - Associativity: $g(g^{-1}h)=h$.
> - Q4: $L_g(e)=g\neq e$.

#### Left-invariant fields on $\mathrm{GL}(n,\mathbb{R})$

The left-invariant vector fields on $\mathrm{GL}(n,\mathbb{R})$ are exactly $\mathbf X^A_g=gA$, $A\in\mathrm{Mat}(n,\mathbb{R})=T_IG$, see Example [[§57 Lie Groups and Left-Invariant Vector Fields#^ex-57-1|§57.1]]. *Source: filled in.*

^nd-ex-57-1

- [ ] Q1 **[state]** State the example. **[def]** Define a left-invariant vector field (Definition [[§57 Lie Groups and Left-Invariant Vector Fields#^def-57-3|§57.3]]).
- [ ] Q2 Why is $(L_g)_{\ast h}(v)=gv$ under $T_hG=\mathrm{Mat}(n,\mathbb{R})$?
- [ ] Q3 Show every left-invariant field is some $\mathbf X^A$.
- [ ] Q4 Show every $\mathbf X^A$ is left-invariant and smooth.
- [ ] Q5 **[why]** What would the right-invariant fields be? How does the choice of left versus right show up in the bracket (remark *Left or Right*)?

> [!tip]- Hints: route of the proof in the notes
> - $L_g$ is the restriction of the linear map $h\mapsto gh$; Corollary [[§30 The Differential in Coordinates#^cor-30-6|§30.6]].
> - Take $h=I$: $\mathbf X_g=g\mathbf X_I$.
> - $g(hA)=(gh)A$; coefficients $(gA)_{ij}$ are linear in $g$.
> - Right-invariant: $Ag$; the bracket changes sign.

#### $\mathfrak g$ is a Lie subalgebra of $\mathfrak X(G)$

$\mathbf X$ is left-invariant iff it is $L_g$-related to itself for every $g$; hence brackets of left-invariant fields are left-invariant, and $\mathfrak g$ is a Lie subalgebra of $\mathfrak X(G)$, see Lemma [[§57 Lie Groups and Left-Invariant Vector Fields#^lem-57-3|§57.3]] and Corollary [[§57 Lie Groups and Left-Invariant Vector Fields#^cor-57-4|§57.4]]. *Source: Lecture 17 ("the big observation").*

^nd-cor-57-4

- [ ] Q1 **[state]** State the lemma and the corollary. **[def]** Define the Lie algebra $\mathfrak g$ of $G$ (Definition [[§57 Lie Groups and Left-Invariant Vector Fields#^def-57-4|§57.4]]).
- [ ] Q2 Rephrase left-invariance as relatedness.
- [ ] Q3 Why is $[\mathbf X,\mathbf Y]$ left-invariant for $\mathbf X,\mathbf Y\in\mathfrak g$?
- [ ] Q4 Why is $\mathfrak g$ a linear subspace, and why does the bracket on $\mathfrak g$ satisfy the Lie algebra axioms?
- [ ] Q5 **[why]** At this point, could $\mathfrak g$ be infinite-dimensional, or zero? Which theorem settles it?

> [!tip]- Hints: route of the proof in the notes
> - $d(L_g)_h(\mathbf X_h)=\mathbf X_{gh}$ is relatedness with $F=L_g$, $\mathbf Y=\mathbf X$.
> - Proposition [[§56 Related Vector Fields#^prop-56-3|§56.3]] with $F=L_g$.
> - Linearity of $d(L_g)_h$; axioms inherited from Corollary [[§55 Lie Bracket and Lie Algebra#^cor-55-5|§55.5]].
> - Q5: Theorem [[§57 Lie Groups and Left-Invariant Vector Fields#^thm-57-7|§57.7]].

#### The left-invariant extension is left-invariant

For $v\in T_eG$, $\mathbf X^v_g=d(L_g)_e(v)$ satisfies $\mathbf X^v_e=v$ and $d(L_g)_h(\mathbf X^v_h)=\mathbf X^v_{gh}$; every $\mathbf X\in\mathfrak g$ is the extension of $\mathbf X_e$, see Lemma [[§57 Lie Groups and Left-Invariant Vector Fields#^lem-57-5|§57.5]]. *Source: Lecture 17's steps; Lecture 18: "You can check that ... we have a left invariant field"; (2) filled in.* **[class exercise, Lecture 18]**

^nd-lem-57-5

- [ ] Q1 **[state]** State the three parts. **[def]** Define the left-invariant extension (Definition [[§57 Lie Groups and Left-Invariant Vector Fields#^def-57-5|§57.5]]).
- [ ] Q2 (1) Why does $\mathbf X^v_g$ lie in $T_gG$, and why is $\mathbf X^v_e=v$?
- [ ] Q3 (2) Prove the left-invariance identity with $L_g\circ L_h=L_{gh}$ and the chain rule.
- [ ] Q4 (3) Why is every left-invariant field the extension of its value at $e$?
- [ ] Q5 **[why]** Why is $\mathbf X^v$ only a *rough* field at this stage? What is still missing to call it an element of $\mathfrak g$?

> [!tip]- Hints: route of the proof in the notes
> - $L_e=\mathrm{id}$; Theorem [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]].
> - $d(L_g)_h\,d(L_h)_e(v)=d(L_{gh})_e(v)$.
> - Left-invariance at $h=e$.
> - Smoothness: Proposition [[§57 Lie Groups and Left-Invariant Vector Fields#^prop-57-6|§57.6]].

#### The left-invariant extension is smooth

For $v\in T_eG$ and $f\in C^\infty(G)$, with $\varphi(g,x)=f(gx)$: $\mathbf X^vf=\partial_v\varphi$ is smooth; hence $\mathbf X^v\in\mathfrak g$, see Proposition [[§57 Lie Groups and Left-Invariant Vector Fields#^prop-57-6|§57.6]]. *Source: Lecture 18, completing Lecture 17 ("a trick that occurred to me").*

^nd-prop-57-6

- [ ] Q1 **[state]** State the proposition.
- [ ] Q2 Why does it suffice to show that $\mathbf X^vf$ is smooth for every $f\in C^\infty(G)$?
- [ ] Q3 Why is $(\mathbf X^vf)(g)=v[f\circ L_g]$?
- [ ] Q4 Why is $\varphi$ smooth, and why is $(\mathbf X^vf)(g)=\partial_v\varphi(g)$, the partial derivative in the second variable?
- [ ] Q5 **[why]** Why is "$\mathbf X^vf$ is a well-defined function" true even before smoothness of $\mathbf X^v$ is known, and why is smoothness of $\varphi$ in *both* variables essential?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: S11, smoothness criterion Lemma [[§53 Vector Fields#^lem-53-8|§53.8]].
> - $d(L_g)_e(v)[f]=v[f\circ L_g]$ (Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-6|§28.6]]).
> - $\varphi=f\circ\mu$; Definition [[§31 Tangent Vectors as Velocities of Curves#^def-31-3|§31.3]] and Proposition [[§31 Tangent Vectors as Velocities of Curves#^prop-31-7|§31.7]](3).
> - A partial derivative of a function smooth in $(g,x)$ is smooth in $g$; smoothness of $f\circ L_g$ for each fixed $g$ would not be enough.

#### The Lie algebra is the tangent space at the identity

$\mathrm{ev}:\mathfrak g\to T_eG$, $\mathbf X\mapsto\mathbf X_e$, is a linear isomorphism; so $\dim\mathfrak g=\dim G$, see Theorem [[§57 Lie Groups and Left-Invariant Vector Fields#^thm-57-7|§57.7]]. *Source: Lecture 17 ("an incomplete proof"), completed in Lecture 18.*

^nd-thm-57-7

- [ ] Q1 **[state]** State the theorem.
- [ ] Q2 Why is $\mathrm{ev}$ linear?
- [ ] Q3 The basic idea: why is a left-invariant field determined by its value at $e$? Deduce injectivity.
- [ ] Q4 Surjectivity: given $v\in T_eG$, which field must you take, and which two facts make it an element of $\mathfrak g$?
- [ ] Q5 **[why]** Which step was "the incompleteness" in Lecture 17, and why is it not automatic?
- [ ] Q6 **[def]** Define the Lie bracket on $T_eG$ (Definition [[§57 Lie Groups and Left-Invariant Vector Fields#^def-57-6|§57.6]]). Why does $\mathrm{ev}$ become an isomorphism of Lie algebras?

> [!tip]- Hints: route of the proof in the notes
> - Strategy: "there is only one choice": the left-invariant extension.
> - $\mathbf X_g=d(L_g)_e(\mathbf X_e)$ (Lemma [[§57 Lie Groups and Left-Invariant Vector Fields#^lem-57-5|§57.5]](3)).
> - Surjective: Lemma [[§57 Lie Groups and Left-Invariant Vector Fields#^lem-57-5|§57.5]](1), (2) and Proposition [[§57 Lie Groups and Left-Invariant Vector Fields#^prop-57-6|§57.6]].
> - $\dim T_eG=\dim G$ (Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-9|§29.9]]).

#### The additive group of a vector space

For a vector space $V$ under addition, the left-invariant fields are the constant fields $p\mapsto D_v|_p$, and all brackets vanish: $\mathfrak g\cong V$ with the zero bracket, see Example [[§57 Lie Groups and Left-Invariant Vector Fields#^ex-57-2|§57.2]]. *Source: filled in (after a remark in Lecture 17).*

^nd-ex-57-2

- [ ] Q1 **[state]** State the example.
- [ ] Q2 Why is $V$ a Lie group, and what is $L_p$?
- [ ] Q3 Why is the left-invariant extension of $D_v|_0$ the constant field $p\mapsto D_v|_p$?
- [ ] Q4 Compute the coefficients in linear coordinates and the bracket.
- [ ] Q5 **[why]** On $\mathrm{GL}(n,\mathbb{R})$ the left-invariant fields $\mathbf X^A_g=gA$ do not have constant coefficients in the matrix entries. Why does that allow nonzero brackets, unlike on $V$? What is the bracket of two commuting matrices?

> [!tip]- Hints: route of the proof in the notes
> - $L_p=\tau_p$, translation; Proposition [[§30 The Differential in Coordinates#^prop-30-7|§30.7]](2).
> - Constant coefficients $v^i$; Proposition [[§55 Lie Bracket and Lie Algebra#^prop-55-2|§55.2]].
> - Q5: $[A,B]=AB-BA=0$ when $A$, $B$ commute (Theorem [[§57 Lie Groups and Left-Invariant Vector Fields#^thm-57-8|§57.8]]).

#### The Lie algebra of $\mathrm{GL}(d,\mathbb{R})$

The Lie bracket on $T_I\mathrm{GL}(d,\mathbb{R})=\mathrm{Mat}(d,\mathbb{R})$ is the matrix commutator $[A,B]=AB-BA$, see Theorem [[§57 Lie Groups and Left-Invariant Vector Fields#^thm-57-8|§57.8]]. *Source: stated in Lecture 17; proof "to be filled" (planned for Lecture 19). Quote it.*

^nd-thm-57-8

- [ ] Q1 **[state]** State the theorem, including how the bracket on $T_IG$ is defined.
- [ ] Q2 Write the left-invariant extensions $\mathbf X^A$, $\mathbf X^B$ (Example [[§57 Lie Groups and Left-Invariant Vector Fields#^ex-57-1|§57.1]]) and the three steps "extend, commute, evaluate at $I$".
- [ ] Q3 **[why]** With right-invariant fields, what would the answer be?
- [ ] Q4 How used: for a linear group $H\subseteq\mathrm{GL}(d,\mathbb{R})$, how does Proposition [[§57 Lie Groups and Left-Invariant Vector Fields#^prop-57-10|§57.10]] applied to the inclusion compute the bracket on $T_IH$?
- [ ] Q5 How used: check that $\mathfrak{so}(3)$, the skew matrices, is closed under $AB-BA$.

> [!tip]- Hints: what to know about the statement
> - $[A,B]=[\mathbf X^A,\mathbf X^B]_I$ (Definition [[§57 Lie Groups and Left-Invariant Vector Fields#^def-57-6|§57.6]], remark *From Now On*).
> - Right-invariant fields give $-(AB-BA)$ (remark *Left or Right*).
> - The inclusion is a Lie group morphism with injective differential, so brackets on $T_IH$ are matrix commutators.
> - $(AB-BA)^{\mathsf T}=B^{\mathsf T}A^{\mathsf T}-A^{\mathsf T}B^{\mathsf T}=-(AB-BA)$ for skew $A$, $B$ (Example [[§55 Lie Bracket and Lie Algebra#^ex-55-3|§55.3]]).

#### Left-invariant fields related by a morphism

For a Lie group morphism $F:H\to G$ and $A\in T_eH$, the left-invariant extensions $\mathbf X^A$ and $\mathbf Y^{\tilde A}$, $\tilde A=dF_e(A)$, are $F$-related, see Lemma [[§57 Lie Groups and Left-Invariant Vector Fields#^lem-57-9|§57.9]]. *Source: Lecture 18 (the "claim"); the diagram chase, left to the class ("just chase where $A$ goes under this diagram"), is completed in the notes.* **[class exercise, Lecture 18]**

^nd-lem-57-9

- [ ] Q1 **[state]** State the lemma. **[def]** Define a Lie group morphism (Definition [[§57 Lie Groups and Left-Invariant Vector Fields#^def-57-8|§57.8]]).
- [ ] Q2 Why is $F(e)=e$?
- [ ] Q3 Why does $F\circ L_h=L_{F(h)}\circ F$ hold, and what does the chain rule give at $e$?
- [ ] Q4 Chase $A$ along the two routes of the square of differentials.
- [ ] Q5 **[why]** Which step uses that $F$ is a group morphism, and not merely a smooth map with $F(e)=e$?

> [!tip]- Hints: route of the proof in the notes
> - $F(e)=F(ee)=F(e)F(e)$.
> - $F(hx)=F(h)F(x)$; $dF_h\circ d(L_h)_e=d(L_{F(h)})_e\circ dF_e$.
> - One route gives $dF_h(\mathbf X^A_h)$, the other $\mathbf Y^{\tilde A}_{F(h)}$.

#### Lie group morphisms preserve brackets

For a Lie group morphism $F:H\to G$, $dF_e([A,B])=[dF_e(A),dF_e(B)]$: $dF_e:\mathfrak h\to\mathfrak g$ is a Lie algebra morphism, see Proposition [[§57 Lie Groups and Left-Invariant Vector Fields#^prop-57-10|§57.10]]. *Source: Lecture 18 ("I claim that the proposition follows from this. Can you see why?").* **[class exercise, Lecture 18]**

^nd-prop-57-10

- [ ] Q1 **[state]** State the proposition. **[def]** Define a Lie algebra morphism (Definition [[§57 Lie Groups and Left-Invariant Vector Fields#^def-57-9|§57.9]]).
- [ ] Q2 Why must one pass to vector fields to prove it?
- [ ] Q3 Given the claim (Lemma [[§57 Lie Groups and Left-Invariant Vector Fields#^lem-57-9|§57.9]]), which proposition gives relatedness of the brackets?
- [ ] Q4 Evaluate at $e$ and identify both sides with Definition [[§57 Lie Groups and Left-Invariant Vector Fields#^def-57-6|§57.6]].
- [ ] Q5 **[why]** Where is $F(e)=e$ used in the last step?

> [!tip]- Hints: route of the proof in the notes
> - The bracket on $T_eG$ is defined through left-invariant fields.
> - Proposition [[§56 Related Vector Fields#^prop-56-3|§56.3]].
> - $dF_e([\mathbf X^A,\mathbf X^B]_e)=[\mathbf Y^{\tilde A},\mathbf Y^{\tilde B}]_{F(e)}$ and $F(e)=e$.

#### The unit quaternions

$S^3\subseteq\mathbb{H}$ is a regular submanifold, a group with smooth multiplication and inversion, and connected, see Proposition [[§45 The Unit Quaternions and SU(2)#^prop-45-4|§45.4]]. → drilled as [[Differentiable Manifolds HW Drill#^hw4-3|HW4.3]].

^nd-prop-45-4

#### $S^3$ is $\mathrm{SU}(2)$

$F:S^3\to\mathrm{SU}(2)$ is a group isomorphism and a diffeomorphism, see Proposition [[§45 The Unit Quaternions and SU(2)#^prop-45-5|§45.5]]. → drilled as [[Differentiable Manifolds HW Drill#^hw4-3|HW4.3]].

^nd-prop-45-5

#### The tangent space of $\mathrm{SU}(2)$ at the identity

the matrices $\sigma_1=F_{\ast1}(i)$, $\sigma_2=F_{\ast1}(j)$, $\sigma_3=F_{\ast1}(k)$ form a basis of $\mathfrak{su}(2)$, see Proposition [[§45 The Unit Quaternions and SU(2)#^prop-45-6|§45.6]]. → drilled as [[Differentiable Manifolds HW Drill#^hw4-3|HW4.3]] (part (a)).

^nd-prop-45-6

#### Translating the differential

For a smooth homomorphism $G$ of matrix groups, $G_{\ast g}=(L_{G(g)})_{\ast I}\circ G_{\ast I}\circ(L_{g^{-1}})_{\ast g}$, see Lemma [[§46 SU(2) → SO(3)꞉ The Double Cover#^lem-46-3|§46.3]]. → drilled as [[Differentiable Manifolds HW Drill#^hw4-3|HW4.3]] (part (b)).

^nd-lem-46-3

#### The double cover $\mathrm{SU}(2)\to\mathrm{SO}(3)$

$G=C\circ F^{-1}$ is a surjective smooth homomorphism and a two-to-one local diffeomorphism with $G_{\ast I}(\sigma_j)=2\hat e_j$, see Theorem [[§46 SU(2) → SO(3)꞉ The Double Cover#^thm-46-4|§46.4]]. → drilled as [[Differentiable Manifolds HW Drill#^hw4-3|HW4.3]] (part (b)).

^nd-thm-46-4

# Equivalences

## Equivalences

### Tangent space

The geometric tangent space $T^{\mathrm{geo}}_pM = \ker F'(p)$, the derivations $T_pM$ with the coordinate basis $\partial/\partial x^i|_p$, and the velocities $D_\gamma$ describe one $n$-dimensional space, see Theorem [[§25 The Geometric Tangent Space#^thm-25-3|§25.3]], Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]], Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-7|§29.7]], Theorem [[§31 Tangent Vectors as Velocities of Curves#^thm-31-2|§31.2]]. *Source: Lectures 7–9, 11; Assignment 3; one class exercise (Lecture 8).*

^nd-eq-1

- [ ] Q1 **[state]** State the four versions (Definition [[§25 The Geometric Tangent Space#^def-25-1|§25.1]], Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-2|§28.2]], Definition [[§29 Coordinate Derivations and the Basis Theorem#^def-29-2|§29.2]], Definition [[§31 Tangent Vectors as Velocities of Curves#^def-31-2|§31.2]]) and the four theorems connecting them, with hypotheses ($M = F^{-1}(c)$ regular level set where needed).
- [ ] Q2 **[state]** Geometric = kernel, first half: prove $T^{\mathrm{geo}}_pM \subseteq \ker F'(p)$. What is differentiated?
- [ ] Q3 **[class exercise, Lecture 8]** Geometric = kernel, second half: reduce to a graph (permutation, implicit function theorem, locality), prove the tangent space of a graph is the graph of $G'(x_0)$, and conclude by a dimension count.
- [ ] Q4 **[state]** Basis theorem: for $D \in T_pM$, push $D$ down by the chart, apply the Euclidean formula $\tilde D[g] = \sum_i \frac{\partial g}{\partial r^i}(a)\,\tilde D[r^i]$, and read it back up. Then prove independence. Which lemma supplies the Euclidean formula?
- [ ] Q5 **[state]** Ambient = abstract: define $v \mapsto D_v$, show $D_v$ is a derivation, the map is linear and injective; why is it then onto?
- [ ] Q6 **[state]** Velocities: show $D_\gamma = \sum_j (x^j \circ \gamma)'(0)\,\partial/\partial x^j|_p$; then every $D$ is a velocity → drilled as [[Differentiable Manifolds HW Drill#^hw3-2|HW3.2]].
- [ ] Q7 **[why]** Two steps close by "equal dimensions": which ones? What would break in Q4 if the functions in Hadamard's lemma were merely continuous?

> [!tip]- Hints: route of the proofs in the notes
> - Strategy: S6 (tangent space of a level set = kernel), S7 (linear algebra closes the gap), S9 (Hadamard), S10 (curves).
> - Q2–Q3: Theorem [[§25 The Geometric Tangent Space#^thm-25-3|§25.3]]: $F \circ \gamma \equiv c$ and the chain rule; then Lemma [[§25 The Geometric Tangent Space#^lem-25-1|§25.1]], Lemma [[§25 The Geometric Tangent Space#^lem-25-2|§25.2]] (set as "not a trivial exercise"), rank–nullity, $n$-dimensional subspace of an $n$-dimensional space.
> - Q4: Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]]: $\tilde D = \varphi_{\ast p}D$, Corollary [[§29 Coordinate Derivations and the Basis Theorem#^cor-29-5|§29.5]] (from Lemma [[§29 Coordinate Derivations and the Basis Theorem#^lem-29-3|§29.3]]), $g = f_\varphi$; independence by $\partial/\partial x^i|_p[x^j] = \delta^j_i$.
> - Q5: Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-7|§29.7]]: Definition [[§25 The Geometric Tangent Space#^def-25-4|§25.4]], Proposition [[§25 The Geometric Tangent Space#^prop-25-8|§25.8]], Proposition [[§25 The Geometric Tangent Space#^prop-25-9|§25.9]], both dimensions $n$.
> - Q6: Proposition [[§31 Tangent Vectors as Velocities of Curves#^prop-31-1|§31.1]], Theorem [[§31 Tangent Vectors as Velocities of Curves#^thm-31-2|§31.2]] ($\gamma = \varphi^{-1}(\varphi(p) + ta)$, $a^i = D[x^i]$).
> - Q7: Q3 and Q5; in Q4 one applies $D$ to the functions $g_i$, so they must be smooth.

### Cotangent space

The dual $T^\ast_pM = (T_pM)^\ast$, the dual basis $dx^i|_p$, and the germ space $I_p/I_p^2$ agree: $dx^i|_p$ is dual to $\partial/\partial x^i|_p$, and ${[}[f]{]} \mapsto df_p$ is a chart-free isomorphism $I_p/I_p^2 \cong T^\ast_pM$, see Lemma [[§33 Covectors in Coordinates#^lem-33-1|§33.1]], Theorem [[§34 The Cotangent Space from Germs#^thm-34-4|§34.4]]. *Source: Lectures 10, 15; Assignment 3.*

^nd-eq-2

- [ ] Q1 **[state]** State the three versions (Definition [[§32 The Cotangent Space#^def-32-4|§32.4]], Definition [[§33 Covectors in Coordinates#^def-33-1|§33.1]], Definition [[§34 The Cotangent Space from Germs#^def-34-1|§34.1]]) and the two theorems connecting them.
- [ ] Q2 **[state]** Prove $df_p(D) = D[f]$, then $dx^i|_p(\partial/\partial x^j|_p) = \delta^i_j$. Why does this make $\{dx^i|_p\}$ a basis?
- [ ] Q3 **[state]** Prove $df_p = \sum_i \frac{\partial f}{\partial x^i}(p)\,dx^i|_p$. Which principle reduces it to a check on basis vectors?
- [ ] Q4 **[state]** Define the pairing $\langle D, {[}[f]{]} \rangle = D[f]$; prove it is well defined and bilinear → drilled as [[Differentiable Manifolds HW Drill#^hw3-3|HW3.3]].
- [ ] Q5 **[state]** Prove the pairing is non-degenerate on both sides. Which side uses that derivations kill constants, and which uses "$f(p) = 0$ and $df_p = 0$ imply $[f] \in I_p^2$"?
- [ ] Q6 **[state]** Conclude $\Phi : I_p/I_p^2 \to T^\ast_pM$ is an isomorphism with $\Phi({[}[f]{]}) = df_p$, sending ${[}[x^i - x^i(p)]{]}$ to $dx^i|_p$.
- [ ] Q7 **[why]** Why quotient by $I_p^2$ (what does $I_p^2$ contain, and why is $D$ blind to it)? Which finiteness hypothesis does the pairing theorem need, and where does it come from?

> [!tip]- Hints: route of the proofs in the notes
> - Strategy: S2 (define on representatives, check well-definedness), S9 (Hadamard), S7.
> - Q2: Proposition [[§32 The Cotangent Space#^prop-32-2|§32.2]] ($r \circ f = f$), Lemma [[§33 Covectors in Coordinates#^lem-33-1|§33.1]] (Step 1), Proposition [[§21 Linear Algebra Toolkit#^prop-21-2|§21.2]]. Q3: Lemma [[§33 Covectors in Coordinates#^lem-33-1|§33.1]] (Step 2).
> - Q4: Proposition [[§34 The Cotangent Space from Germs#^prop-34-3|§34.3]] (difference in $I_p^2$, Leibniz). Q5: left: $D[f] = D[f - f(p)]$, Lemma [[§28 Derivations and the Abstract Tangent Space#^lem-28-2|§28.2]]; right: Proposition [[§34 The Cotangent Space from Germs#^prop-34-1|§34.1]] ((2)⇒(1) by Hadamard).
> - Q6: Theorem [[§21 Linear Algebra Toolkit#^thm-21-5|§21.5]] with $\dim T_pM = m$ (Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]]), Theorem [[§34 The Cotangent Space from Germs#^thm-34-4|§34.4]]; basis also from Proposition [[§34 The Cotangent Space from Germs#^prop-34-2|§34.2]].

### The differential

The Jacobian differential $dF_p$ of a map between vector spaces, the pushforward $F_{\ast p}$ of derivations, and the curve formula agree: $dF_p(v) = \frac{d}{dt}|_0 F(p + tv)$, the matrix of $F_{\ast p}$ is the Jacobian of $\psi \circ F \circ \varphi^{-1}$, and $F_{\ast p}(D_\gamma) = D_{F \circ \gamma}$, see Theorem [[§22 The Differential of a Map Between Vector Spaces#^thm-22-3|§22.3]], Theorem [[§30 The Differential in Coordinates#^thm-30-2|§30.2]], Corollary [[§31 Tangent Vectors as Velocities of Curves#^cor-31-3|§31.3]]. *Source: Lectures 7, 10; one class exercise (Lecture 7).*

^nd-eq-3

- [ ] Q1 **[state]** State the three versions (Definition [[§22 The Differential of a Map Between Vector Spaces#^def-22-5|§22.5]], Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-6|§28.6]], by curves) and the connecting results.
- [ ] Q2 **[class exercise, Lecture 7]** Prove $dF_p(v) = \frac{d}{dt}\big|_{t=0} F(p + tv)$ from $dF_p = K^{-1} \circ \widetilde F'(\tilde p) \circ L$; conclude independence of $L$, $K$.
- [ ] Q3 **[state]** Prove $F_{\ast p}(\partial/\partial x^i|_p) = \sum_j \frac{\partial F^j}{\partial x^i}(p)\,\partial/\partial y^j|_{F(p)}$. Which coefficient formula for a derivation at $F(p)$ is used?
- [ ] Q4 **[state]** Show the upstairs partials $\frac{\partial F^j}{\partial x^i}(p)$ are the entries of $\tilde F'(\varphi(p))$; for $W \subseteq \mathbb{R}^m$ open, conclude that $F_{\ast a}$ is $F'(a)$ under $\partial/\partial r^i|_a \mapsto e_i$.
- [ ] Q5 **[state]** For a vector space $V$, identify $V \cong T_aV$ by $v \mapsto D_v|_a$; why is this canonical, and why does it match Q2 with Q4?
- [ ] Q6 **[state]** Prove $F_{\ast p}(D_\gamma) = D_{F \circ \gamma}$ and explain how, with "every vector is a velocity", it computes $F_{\ast p}$ by curves.
- [ ] Q7 **[why]** The map $F_{\ast p}$ is intrinsic, its matrix is not. Which properties of $F_{\ast p}$ may therefore be read off a matrix in any charts?

> [!tip]- Hints: route of the proofs in the notes
> - Strategy: S1 (compute in a chart, show independence), S10 (curves).
> - Q2: Theorem [[§22 The Differential of a Map Between Vector Spaces#^thm-22-3|§22.3]] (coordinate curve $\tilde p + t\tilde v$, chain rule, $K^{-1}$ linear and continuous; Uribe: "I really encourage you to prove it").
> - Q3: Theorem [[§30 The Differential in Coordinates#^thm-30-2|§30.2]] ($E[y^j] = \partial/\partial x^i|_p[y^j \circ F]$, universal formula Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]]). Q4: Proposition [[§30 The Differential in Coordinates#^prop-30-1|§30.1]], Proposition [[§30 The Differential in Coordinates#^prop-30-5|§30.5]].
> - Q5: Corollary [[§30 The Differential in Coordinates#^cor-30-6|§30.6]], Proposition [[§30 The Differential in Coordinates#^prop-30-7|§30.7]]. Q6: Corollary [[§31 Tangent Vectors as Velocities of Curves#^cor-31-3|§31.3]] (chain rule, Theorem [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]]), Theorem [[§31 Tangent Vectors as Velocities of Curves#^thm-31-2|§31.2]].
> - Q7: the remark *The Map Is Intrinsic --- the Matrix Is Not* in [[§30 The Differential in Coordinates|§30]]: rank, kernel, image.

### Smooth structure

An atlas determines a unique maximal atlas, so "atlas" and "maximal atlas" give the same smooth structures, and smoothness of maps can be tested in any charts, see Theorem [[§17 Differentiable Structures#^thm-17-5|§17.5]], Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-2|§19.2]]. *Source: Lectures 5–7; one class exercise (Lecture 7).*

^nd-eq-4

- [ ] Q1 **[state]** State Theorem [[§17 Differentiable Structures#^thm-17-5|§17.5]] (with the explicit $\overline{\mathcal{A}}$) and Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-2|§19.2]].
- [ ] Q2 **[state]** Show $\overline{\mathcal{A}}$ contains $\mathcal{A}$, so its domains cover $M$. Which property of compatibility is used for a chart with itself?
- [ ] Q3 **[state]** Show two charts $(V, \psi)$, $(W, \chi)$ of $\overline{\mathcal{A}}$ are compatible: factor $\chi \circ \psi^{-1}$ near $\psi(p)$ through a chart of $\mathcal{A}$ at $p$. Why does it suffice to prove smoothness near each point?
- [ ] Q4 **[state]** Show $\overline{\mathcal{A}}$ is maximal and is the only maximal atlas containing $\mathcal{A}$; then: two atlases are compatible iff they lie in the same maximal atlas.
- [ ] Q5 **[class exercise, Lecture 7]** Show smoothness of $f : M \to \mathbb{R}$ in some chart at each point gives smoothness in every chart; then the same for maps $F : M \to N$ (sandwich between transition maps).
- [ ] Q6 **[why]** Compatibility is not transitive. Point to the exact step in Q3 where this matters and how the factorization avoids it.

> [!tip]- Hints: route of the proofs in the notes
> - Strategy: S1 (check in a chart, then show the choice does not matter).
> - Q2–Q4: Theorem [[§17 Differentiable Structures#^thm-17-5|§17.5]] (reflexivity, Proposition [[§17 Differentiable Structures#^prop-17-2|§17.2]]; $\chi \circ \psi^{-1} = (\chi \circ \varphi^{-1}) \circ (\varphi \circ \psi^{-1})$ on $\psi(U \cap V \cap W)$).
> - Q5: Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-1|§19.1]] (left to the class), Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-2|§19.2]] ($\psi' F \varphi'^{-1} = (\psi'\psi^{-1})(\psi F \varphi^{-1})(\varphi\varphi'^{-1})$), Lemma [[§19 Smooth Functions and Smooth Maps#^lem-19-3|§19.3]].
> - Q6: Proposition [[§17 Differentiable Structures#^prop-17-2|§17.2]] ($\mathrm{id}$, $\mathrm{id}|_{(0,\infty)}$, $t^3$).

### Submanifolds of $\mathbb{R}^N$

For $X \subseteq \mathbb{R}^{n+k}$ near $p$: external (regular level set), internal (parametrization), graph, and slice (adapted chart) descriptions are equivalent, see Theorem [[§20 Manifolds in Euclidean Space#^thm-20-1|§20.1]], Proposition [[§37 Regular Submanifolds#^prop-37-9|§37.9]]. *Source: Lectures 5–6, 12 (proofs not from lecture).*

^nd-eq-5

- [ ] Q1 **[state]** State the four descriptions (Definition [[§20 Manifolds in Euclidean Space#^def-20-1|§20.1]], Definition [[§20 Manifolds in Euclidean Space#^def-20-2|§20.2]], the graph condition (G), Definition [[§37 Regular Submanifolds#^def-37-3|§37.3]]) and the two theorems.
- [ ] Q2 **[state]** External ⇒ graph: which columns of $F'(p)$ are used, and which theorem produces $h$?
- [ ] Q3 **[state]** Graph ⇒ external and graph ⇒ internal: give $F$ and $\alpha$ explicitly, and check the rank conditions and the homeomorphism.
- [ ] Q4 **[state]** Internal ⇒ graph: choose $n$ independent rows of $D\alpha_q$, invert $\alpha_1$ locally, set $h = \alpha_2 \circ \alpha_1^{-1}$.
- [ ] Q5 **[state]** Graph ⇒ slice: show $\Phi(x, y) = (x, y - h(x))$ is a smooth chart adapted to $X$. Slice ⇒ external: why does $x_b$ have $\vec 0$ as a regular value?
- [ ] Q6 **[why]** In Q4, where exactly is "$\alpha$ is a homeomorphism onto $X \cap W$" used? Give a curve where dropping it makes "internal ⇒ graph" fail.

> [!tip]- Hints: route of the proofs in the notes
> - Strategy: S8 (normal forms give charts), S5 (regular value theorem).
> - Q2: Theorem [[§20 Manifolds in Euclidean Space#^thm-20-1|§20.1]], i.e. Steps 1–3 of Theorem [[§7 The Regular Value Theorem#^thm-7-3|§7.3]] ($k$ independent columns, implicit function theorem Theorem [[§7 The Regular Value Theorem#^thm-7-1|§7.1]]).
> - Q3: $F(x, y) = y - h(x)$ with Jacobian $(-Dh \mid I_k)$; $\alpha(x) = (x, h(x))$ with inverse the projection.
> - Q4: inverse function theorem (Theorem [[§35 Local Diffeomorphisms#^thm-35-1|§35.1]]); then $\alpha(V_1)$ is open in $X \cap W$ because $\alpha$ is a homeomorphism onto it, so it is $X \cap$ (a box).
> - Q5: Proposition [[§37 Regular Submanifolds#^prop-37-9|§37.9]] (smooth, injective, open image, smooth inverse $(x, z) \mapsto (x, z + h(x))$; the rows of $\varphi'(q)$ are independent). Q6: Example [[§42 Embeddings#^ex-42-1|§42.1]] (figure-eight).

### Regular value theorem

The Euclidean theorem ($F^{-1}(\vec 0)$ a topological, then smooth, manifold by graph charts) and the manifold theorem ($F^{-1}(q)$ a regular submanifold with $\iota_\ast(T_pS) = \ker F_{\ast p}$) agree on open subsets of $\mathbb{R}^{n+k}$, see Theorem [[§7 The Regular Value Theorem#^thm-7-3|§7.3]], Theorem [[§37 Regular Submanifolds#^thm-37-12|§37.12]], Proposition [[§37 Regular Submanifolds#^prop-37-14|§37.14]]. *Source: Lectures 3, 6, 12; Assignment 1.*

^nd-eq-6

- [ ] Q1 **[state]** State the three results, with the notion of regular value used in each.
- [ ] Q2 **[state]** Euclidean version: why is $F^{-1}(\vec 0)$ Hausdorff and second countable, and how does the implicit function theorem give charts? → drilled as [[Differentiable Manifolds HW Drill#^hw1-6|HW1.6]].
- [ ] Q3 **[state]** Manifold version: from the submersion normal form at $p \in S$, show $S$ is cut out near $p$ by $x^1 = c_1, \ldots, x^n = c_n$, and turn this into an adapted chart.
- [ ] Q4 **[class exercise, Lecture 12]** Tangent space ("I won't bother checking the kernel thing"): prove $\iota_{\ast p}(T_pS) \subseteq \ker F_{\ast p}$ (what is $F \circ \iota$?), then compare dimensions.
- [ ] Q5 **[state]** The two smooth structures on $S = F^{-1}(c)$ agree: show $\Phi(x, y) = (x, F(x, y) - c)$ is a smooth chart of $W$ adapted to $S$ near $p$, whose induced chart is the graph chart.
- [ ] Q6 **[state]** The two tangent spaces agree: under $T_pW = \mathbb{R}^{n+k}$, show $\iota_{\ast p}(T_pS) = T^{\mathrm{geo}}_pS = \ker F'(p)$ (use the lifted line).
- [ ] Q7 **[why]** Why must Q5 be checked at all? Could one set carry two different smooth structures, both with "the right charts"? And why is "regular value" the same condition in both settings?

> [!tip]- Hints: route of the proofs in the notes
> - Strategy: S5 (regular value theorem), S8 (normal forms give charts), S6 (tangent space = kernel), S7.
> - Q2: Theorem [[§7 The Regular Value Theorem#^thm-7-3|§7.3]] (subspace inheritance, Theorem [[§3 Subspaces and Products#^thm-3-5|§3.5]]; permutation, IFT, graph chart). Smooth: Proposition [[§20 Manifolds in Euclidean Space#^prop-20-2|§20.2]].
> - Q3: Theorem [[§37 Regular Submanifolds#^thm-37-12|§37.12]], Lemma [[§37 Regular Submanifolds#^lem-37-11|§37.11]] (parts 1–2), Proposition [[§37 Regular Submanifolds#^prop-37-2|§37.2]] (constants and any $k$ coordinates).
> - Q4: Lemma [[§28 Derivations and the Abstract Tangent Space#^lem-28-10|§28.10]] ($F \circ \iota$ constant), Lemma [[§37 Regular Submanifolds#^lem-37-11|§37.11]] (part 3): both sides have dimension $m - n$.
> - Q5: Proposition [[§37 Regular Submanifolds#^prop-37-14|§37.14]] (1) (block lower triangular Jacobian, inverse function theorem, Lemma [[§36 Submersions#^lem-36-5|§36.5]]). Q6: Proposition [[§37 Regular Submanifolds#^prop-37-14|§37.14]] (2), Definition [[§25 The Geometric Tangent Space#^def-25-4|§25.4]], Corollary [[§30 The Differential in Coordinates#^cor-30-6|§30.6]].
> - Q7: Example [[§19 Smooth Functions and Smooth Maps#^ex-19-1|§19.1]] (same set, different structures); regular in both senses since the matrix of $F_{\ast p}$ is $F'(p)$, Theorem [[§30 The Differential in Coordinates#^thm-30-2|§30.2]].

### Transversality

The Euclidean notion ($\operatorname{im} F'(p) + T^{\mathrm{geo}}S = \mathbb{R}^k$, $S$ a regular level set) is the manifold notion ($F_{\ast p}(T_pM) + \iota_\ast(T_qS) = T_qN$) read in $\mathbb{R}^N$; both give preimages of the same codimension, and the manifold theorem contains the regular value theorem and transverse intersections, see Theorem [[§26 Transversality#^thm-26-1|§26.1]], Theorem [[§37 Regular Submanifolds#^thm-37-15|§37.15]], Corollary [[§37 Regular Submanifolds#^cor-37-17|§37.17]]. *Source: Assignments 2 and 5 (not from lecture).*

^nd-eq-7

- [ ] Q1 **[state]** State both definitions (Definition [[§26 Transversality#^def-26-2|§26.2]], Definition [[§37 Regular Submanifolds#^def-37-5|§37.5]]) and the three results.
- [ ] Q2 **[state]** Show the two definitions agree for $F : \mathbb{R}^N \to \mathbb{R}^k$ and $S = G^{-1}(0)$: what do $F_{\ast p}(T_p\mathbb{R}^N)$ and $\iota_{\ast q}(T_qS)$ become under $T_q\mathbb{R}^k = \mathbb{R}^k$?
- [ ] Q3 **[state]** Euclidean theorem: show $F \pitchfork S$ iff $0$ is a regular value of $G \circ F$, and read off $F^{-1}(S)$ and its tangent space → drilled as [[Differentiable Manifolds HW Drill#^hw2-5|HW2.5]].
- [ ] Q4 **[state]** Manifold theorem: replace $G$ by the local defining map $x_b$ of an adapted chart at $q = F(p)$; show $x_b \circ F$ is a submersion at $p$, get an adapted chart for $F^{-1}(S)$, and compute the kernel → drilled as [[Differentiable Manifolds HW Drill#^hw5-2|HW5.2]].
- [ ] Q5 **[state]** Special cases: a point $S = \{c\}$ (recovers the regular value theorem), two submanifolds ($\iota' \pitchfork S$, codimensions add, $T(S \cap S') = TS \cap TS'$), and submersions.
- [ ] Q6 **[why]** Without transversality, which conclusions fail (dimension, tangent formula)? Why is the codimension, not the dimension, preserved?

> [!tip]- Hints: route of the proofs in the notes
> - Strategy: S12 (transversality = the images span; reduce to a regular value of a composite), S5, S8.
> - Q2: Proposition [[§37 Regular Submanifolds#^prop-37-14|§37.14]] (2) and Proposition [[§30 The Differential in Coordinates#^prop-30-5|§30.5]]: $\operatorname{im} F'(p)$ and $T^{\mathrm{geo}}_qS = \ker G'(q)$.
> - Q3: Proposition [[§26 Transversality#^prop-26-2|§26.2]], Theorem [[§26 Transversality#^thm-26-1|§26.1]]. Q4: Theorem [[§37 Regular Submanifolds#^thm-37-15|§37.15]] (Steps 1–7; Proposition [[§37 Regular Submanifolds#^prop-37-7|§37.7]], Lemma [[§37 Regular Submanifolds#^lem-37-11|§37.11]]).
> - Q5: Corollary [[§37 Regular Submanifolds#^cor-37-17|§37.17]], Proposition [[§26 Transversality#^prop-26-4|§26.4]]. Q6: Example [[§26 Transversality#^ex-26-2|§26.2]]; Proposition [[§37 Regular Submanifolds#^prop-37-16|§37.16]] (normal spaces isomorphic).

### Diffeomorphism

For open $A \subseteq \mathbb{R}^m$, $B \subseteq \mathbb{R}^n$ with their standard structures, smooth in the manifold sense = smooth in the Euclidean sense, so the two notions of diffeomorphism agree, see Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-4|§19.4]]. *Source: notes (not from lecture).*

^nd-eq-8

- [ ] Q1 **[state]** State both definitions (Definition [[§17 Differentiable Structures#^def-17-3|§17.3]], Definition [[§19 Smooth Functions and Smooth Maps#^def-19-4|§19.4]]) and Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-4|§19.4]].
- [ ] Q2 **[state]** Euclidean-smooth ⇒ smooth: which charts witness it?
- [ ] Q3 **[state]** Smooth ⇒ Euclidean-smooth: given charts $(U, \varphi)$, $(V, \psi)$ of the standard structures with $\psi \circ F \circ \varphi^{-1}$ smooth, write $F$ on $U$ as a composite of Euclidean-smooth maps. Why are $\varphi$ and $\psi^{-1}$ Euclidean-smooth?
- [ ] Q4 **[state]** Pass to diffeomorphisms by applying the result to $F$ and $F^{-1}$.
- [ ] Q5 **[why]** Where is "standard smooth structure" used? Give a diffeomorphism $\widetilde{\mathbb{R}} \to \mathbb{R}$ that is not a Euclidean diffeomorphism of $\mathbb{R}$.

> [!tip]- Hints: route of the proofs in the notes
> - Strategy: S1.
> - Q2: the identity charts, coordinate representation $F$ itself. Q3: $F = \psi^{-1} \circ (\psi \circ F \circ \varphi^{-1}) \circ \varphi$; $\varphi$, $\psi$ are compatible with the identity charts (Theorem [[§17 Differentiable Structures#^thm-17-5|§17.5]]), so they and their inverses are Euclidean-smooth.
> - Q5: $h(t) = t^{1/3}$, Example [[§19 Smooth Functions and Smooth Maps#^ex-19-2|§19.2]], Corollary [[§19 Smooth Functions and Smooth Maps#^cor-19-9|§19.9]].
