---
type: quality-check
subject: "[[Topology]]"
date: 2026-10-04
tags: [quality-check]
---
# Quality check: Topology
↑ [[Quality Check 2026-10-04]]

> [!note] Record only
> None of the changes in this log were applied. The notes are as they were before the check, and every change below is a **proposal**. The exact text of each proposed change is kept in the coordinator's saved patch (see [[Quality Check 2026-10-04]]). Locations are given as note, block and old → new.

## Summary
Topology (MATH 590, Munkres) is in good shape. All 29 section notes follow the same header pattern, every callout has a block ID, numbering is continuous, and every proof either has a *Uses:* line or is self-contained. I checked every link alias against its target block, every cross-subject label (451, 493, 591, 342), and every hub against the *Uses:* lines. I read all sections at skim level, and the point-set chapters (order topology, connectedness, compactness, countability) and the π₁ chapters in depth. The real problems are few and local. There is one gap in a proof (Thm §15.10, Step 3), one wrong table row (Rem §21.11), one logically reversed sentence (Cor §26.4), a broken hub link, and several stale labels and counts. The proposals below fix these without removing any content.

## Proposed edits (not applied)
### Correctness
- [[§15 Compact Spaces]], proof of Thm §15.10, Step (3). The old text reads "In either case, there exists $d < c$ such that $(d, c] \subseteq A_c$ (taking $d = a$ if $c = a$)." This is impossible when $c = a$, since $(a, a]$ is empty and is not a neighbourhood. The proposal deletes that sentence and adds after the case split: "If $c = a$, then $c \in C$ by Step (2). So assume $a < c$; then there exists $d < c$ such that $(d, c] \subseteq A_c$."
- [[§21 Algebra Prerequisites꞉ Groups]], Rem §21.11 table, row $\mathbb{Z}/n\mathbb{Z}$. The old text reads "Lens spaces, $P^n$ ($n \geq 2$)". This is wrong because $\pi_1(P^n) = \mathbb{Z}/2$ and the letter $n$ is reused. Proposed: "Lens spaces; for $n = 2$, $P^m$ ($m \geq 2$)".
- [[§26 Deformation Retracts and Homotopy Type]], Cor §26.4, paragraph "Up". The old text reads "any property [[§21 Algebra Prerequisites꞉ Groups#^prop-21-9|inherited by subgroups]] transfers upward". This is reversed: being abelian is inherited by subgroups but does not transfer up. Proposed: "$\pi_1(X)$ contains an isomorphic copy of $\pi_1(A)$ ([[§21 Algebra Prerequisites꞉ Groups#^prop-21-9|§21.9]]), so any property that a group has as soon as one of its subgroups has it transfers upward." The examples that follow stay unchanged.
- [[§3 Order Topology]], Def §3.3 (dictionary order). In "$a_1 < a_2$" the ordering should be $<_A$, which matches the rest of the display.
- [[§3 Order Topology]], Ex §3.4, "Key insight". The old text reads "open sets in the dictionary order topology are unions of vertical line segments and rays. The topology is much finer in the horizontal direction." Rays are not open sets here. Proposed: every open set is a union of open vertical segments $\{a\} \times (b, d)$, and horizontally the topology is discrete, because $\{a\} \times (b-1, b+1)$ is open. It is the product $\mathbb{R}_{\text{discrete}} \times \mathbb{R}_{\text{std}}$ ([[§4 Product Topology#^ex-4-3|Example §4.3]]), which is strictly finer than the standard topology on $\mathbb{R}^2$.
- [[§21 Algebra Prerequisites꞉ Groups]], proof of Thm §21.5: "Since $f$ is surjective, there exist unique $x, y$" → "Since $f$ is bijective". Uniqueness needs injectivity.
- [[§13 Connected Spaces]], proof of Thm §13.3. The justification is garbled: it reads "(By surjectivity.)", then "open, ≠ ∅. By surjectivity, hence there exists a separation". Proposed: "$g^{-1}(A) \cup g^{-1}(B) = g^{-1}(A \cup B) = X$ … They are open because $g$ is continuous, and nonempty because $g$ is surjective and $A, B \neq \emptyset$. Hence $g^{-1}(A), g^{-1}(B)$ is a separation of $X$, a contradiction."

### Labels and cross-subject references
- [[§29 The Seifert–van Kampen Theorem]], *Uses:* line of the §29.1 proof: [[First Isomorphism Theorem for Groups]] is labelled "493 §38.1"; the block is 493 §41.1.
- [[Functoriality of π₁]], Connections: [[Chain Rule for Differentials]] is labelled "591 Thm. §12.11"; the block is 591 Thm. §26.6.
- [[· 7 Algebraic Foundations]] and [[· 11 Computing π₁]], "Builds on (other subjects): [[Linear Algebra]] (1)" → "[[Group Theory]] (1)". The single citation in each chapter is the First Isomorphism Theorem for Groups (Def §21.11 and the §29.1 proof), not Linear Algebra. The count of 1 is unchanged.
- [[Algebraic Topology Toolkit]]: the example title "Example §35.1: Constructing Spaces" uses a section number that does not exist, so it becomes "Example: Constructing Spaces". The block ID `^ex-35-1` stays, because [[Projective plane]] links to it and embeds it.

### Writing
- [[§9 Continuous Functions]], Def §9.1: "(Generalizes ε-δ since metric definition.)" → "(This generalizes the ε-δ definition of continuity for metric spaces.)"
- [[§12 Quotient Topology]], Cor §12.4: "induces a bijection continuous map" → "induces a continuous bijection".
- [[§15 Compact Spaces]], remark on book material. The old text reads "It will be removed if covered later, or kept as supplementary material." This is stale, so it becomes "…is important; it is kept as supplementary material."
- [[Algebraic Topology Toolkit]], remark on the table. The old text reads "This table will grow as we cover more spaces and tools." This is stale, so it becomes "The table collects the spaces computed in the course."
- [[Algebraic Topology Toolkit]], Example "Constructing Spaces": "$P^2 \vee P^2 \times S^2$" → "$(P^2 \vee P^2) \times S^2$" for precedence.
- [[§18 Countability Axioms]], Ex §18.8 (two places) and Prop §18.4: `\mathbb{R}_l` → `\mathbb{R}_\ell`. Ex §2.3 and the rest of the vault use $\mathbb{R}_\ell$.

### Connections
- [[§25 The Fundamental Theorem of Algebra]], Connections. This is the reciprocal of the Complex Variables link. Add the bullet: "Step 3 is the homotopy invariance behind Rouché's theorem, [[§94 Rouché's Theorem#^thm-94-1|342 Thm. §94.1]] (hub [[Rouché's Theorem]]): $|t(a_{n-1}z^{n-1} + \cdots + a_0)| < |z^n|$ on $S^1$ keeps the homotopy $F$ away from $0$, so $z^n$ and $p(z)$ wind equally often around $0$." I checked that the target block exists and states Rouché's theorem.
- [[§17 Local Compactness]], proof of Thm §17.6: the citation of "Munkres Lemma 26.4" also points to the [[§15 Compact Spaces#^pf-15-4|proof of Theorem §15.4]], where the same separation argument is carried out.

### Hubs
- [[Pasting Lemma]], Used in. The link `[[Topology §22 Homotopy of Paths#^prop-22-4|Proposition §22.4: Well-Definedness of [f] * [g]]]` is broken: the note name is wrong, and the `]` in the alias ends the link early. It becomes `[[§22 Homotopy of Paths#^prop-22-4|Proposition §22.4: Well-Definedness of the Product of Path Classes]]`.
- [[Tube Lemma]], Used in (Topology): "(not cited later in the course)" → [[§15 Compact Spaces#^thm-15-8|Theorem §15.8]]. Its proof cites the tube lemma.
- [[Closed Subspace of a Compact Space is Compact]], [[Compact Subspace of a Hausdorff Space is Closed]] and [[Continuous Image of a Compact Space is Compact]]: add [[§12 Quotient Topology#^thm-12-5|Theorem §12.5]] to Used in (Topology). Its *Uses:* line cites §15.2, §15.3 and §15.4.
- [[Fundamental Group of the Circle]]: add [[§23 The Fundamental Group#^cor-23-8|Corollary §23.8]] (torus) to Used in.
- [[Lebesgue Number Lemma]]: add [[§16 Limit Point Compactness#^thm-16-2|Theorem §16.2]] to Used in. The proof of (3)⇒(1) uses it.

### Other (frontmatter)
- Add the missing `munkres:` key: [[§1 Topological Spaces]] gets "§12", and [[§6 Closed Sets and Limit Points]], [[§7 Interior and Closure]] and [[§8 Hausdorff Spaces]] get "§17". In [[§26 Deformation Retracts and Homotopy Type]], "§58" → "§55, §58", because the no-retraction and Brouwer theorems (Thm §26.6, §26.7) are Munkres 55.2 and 55.6.

## Flagged for the author (not edited)
- [[§9 Continuous Functions]], Rem §9.2: the lower bound in Prop §9.2 is "omitted here", so the argument is incomplete. I did not edit it because the omission is the author's choice.
- [[§29 The Seifert–van Kampen Theorem]]: the remarks `^rem-29-3` "Recipe for Finding N" and `^rem-29-4` "How to Find N: The Recipe" nearly duplicate each other. The author could merge them. Both are linked, so neither was touched.
- [[§28 Fundamental Group of Some Surfaces]], §28.5: the retraction of the double torus onto the figure eight is described only informally. A precise map, or a citation of Munkres §74, would complete it.
- [[§8 Hausdorff Spaces]], Prop §8.2 ("T₁ axiom") is a definition labelled as a proposition. Renaming it would change linked titles, so I left it.
- Home-note counting rule. In [[Topology]], "Linear Algebra 2.26 Basis (1)" is correct, because §2 "Remark: Why Bases?" cites it. The home "Prerequisites from other subjects" counts include non-Connections remarks. The chapter "Builds on (other subjects)" counts include only non-remark callouts, so the two rules differ. For example, Chapter 5's Single Variable Analysis count would be 2 under the home rule. No count is wrong under its own rule, so nothing was changed.

## Placeholder proofs still open
- [[§11 Metric Topology]], Thm §11.3 ($\mathbb{R}^\omega$ is metrizable): the proof reads "To be completed."

## Requests outside my scope
- None needed. The Complex Variables ⇄ Topology (Rouché) link is now reciprocal. Every cross-subject target I checked resolves and says what is claimed.

## Checks run
- 76 notes: 29 sections, 11 chapter notes, 25 hubs, 9 examples, home and toolkit. There are 853 callouts and 149 proofs; all have block IDs. The 11 proofs without *Uses:* are self-contained.
- Frontmatter keys, nav lines `← · ↑ · →` and dollar-sign balance were checked on all sections; `munkres:` was missing on 4 sections.
- Link aliases against target block numbers: 4 stale labels and 1 broken link were found.
- Cross-subject labels (451, 493, 591, 342): 2 stale labels were found.
- Hubs, "Its proof uses" against *Uses:* plus statement links: no mismatch. "Used in": 5 hubs were missing users.
- Chapter "Builds on (other subjects)" counts were recounted under the generator's rule: 2 had the wrong subject.
- `links.py` lists no unresolved link in Topology or in this log.
