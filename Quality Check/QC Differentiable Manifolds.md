---
type: quality-check
subject: "[[Differentiable Manifolds]]"
date: 2026-10-04
tags: [quality-check]
---
# Quality check: Differentiable Manifolds
↑ [[Quality Check 2026-10-04]]

## Summary
I checked all 86 notes in `Math/Differentiable Manifolds/` (`tex/` excluded): 39 section notes, 5 chapter notes, the home note, the Course Log, the Lee Concordance, 32 hubs and 7 workhorse-example notes. The subject is in good shape. Proofs are careful, the provenance tags are consistent, and the links into Topology, Multivariable Analysis, Linear Algebra and Group Theory are dense and accurate. Most problems were left over from the recent renumbering: 24 stale "§N" labels and section pointers, 10 links naming the wrong kind of item, and stale status lines about the immersion normal form and the end of the roadmap. I fixed all of them. I also brought eight hub "Its proof uses" lists into line with the proofs' *Uses:* lines and corrected five hub "Used in" lists. The concordance chapter map now has rows for §8, §9, §15 and §38, and Group Theory now appears in the chapter notes. I wrote no proofs, and the 11 open placeholders are listed below. The course is in progress, so I changed course-record facts only where the record contradicted itself.

## Edits made

### Correctness and consistency (stale references after the renumbering)
- [[Immersion Normal Form]]: in Connections, "§33.1" and "§33.5" now read §37.1 and §37.5, matching the hubs they link ([[Images of Embeddings Are Submanifolds]], [[Injective Proper Immersions Are Embeddings]]).
- [[Differentiable Manifolds Course Log]]: eight "Rem. in §N" labels pointed at other sections. They now name the section of the linked remark: rem-19-1 "§16"→§19, rem-26-1 "§23"→§26, rem-20-3 "§17"→§20, rem-36-1 "§32"→§36, rem-23-7 "§20"→§23, rem-28-5 "§25"→§28, rem-38-2 "§31"→§38, rem-38-1 "§32"→§38. In the Lecture 2 and Lecture 4 rows, the group label "[[§6 Open Quotients|§6]]" wrapped items that now live in §9 (Def./Prop. §9.1). Those rows now carry a §9 group. Lecture 2 keeps a separate §6 link, because the tex banner places §6 (the Hausdorff criterion) in Lecture 2.
- [[§38 Projective Spaces and the Hopf Fibration]]: "Rem. in §32" → "Rem. in §35" (it links rem-35-2).
- [[§12 Group Actions and Orbit Spaces]]: "the remark after §12.2" → "§14.2" (rem-14-1 follows Cor. §14.2). The proof title "Proof of Theorem §10.5" → "Proof of Theorem §12.5" (it is ^pf-12-5).
- [[§14 The Topology of G∕H and Real Grassmannians]]: in the *Uses:* line, "Remark after §12.2" → "Remark after §14.2".
- [[§16 Differentiable Structures]]: "Remark after §14.4" → "Remark after §17.4" (rem-17-2 follows Prop. §17.4).
- [[§18 Smooth Functions and Smooth Maps]]: "remark after Ex. §15.1" now reads "Remark: Distinct Structures versus Non-Diffeomorphic Manifolds, after Ex. §18.2".
- [[§34 Fibrations]]: "Remark: Covering Maps (§28)" → "(§31)" and "Remark: Vector Bundles (§32)" → "(§35)".
- [[§37 Embeddings]]: "Remark: Embeddings — Next Time (§33)" → "(§36)".
- [[§17 Projective Spaces as Smooth Manifolds]]: in Prop. §17.6(1), the Grassmannian coset space was attributed to "[[§13 Homogeneous Spaces|§13]]". It is in §14, so the link now points to [[§14 The Topology of G∕H and Real Grassmannians#^cor-14-8|Cor. §14.8]].
- [[§15 The Classical Groups]] and [[§10 Topological Groups and Classical Matrix Groups]]: both said "U(1) = S¹" was collected in §15, but it is Example §10.3 and §15 has no U(1) content. Both now point to Ex. §10.3.
- Links that named the wrong kind of item (10 occurrences): "Proposition §5.2" → "Corollary §5.2" in [[§3 Subspaces and Products]], [[§5 Quotient Maps]], [[§12 Group Actions and Orbit Spaces]] and [[§14 The Topology of G∕H and Real Grassmannians]] (×2). "Proposition §11.5" → "Corollary" in [[§7 The Regular Value Theorem]] (×2). "Theorem §7.2" → "Corollary §7.2" in [[§11 The Classical Groups Are Topological Manifolds]]. "Proposition §26.6" → "Theorem §26.6" in [[§26 Derivations and the Abstract Tangent Space]] and [[§28 The Differential in Coordinates]].

### Stale status
- [[Differentiable Manifolds]], under "Planned topics": the text said "immersion normal form stated", and [[Differentiable Manifolds Course Log]] said "immersion normal form stated only". The Lecture 14 row and [[§36 Immersions]] (Status, and "Proof (Lecture 14)") show it was proved. Both now read "both local normal forms proved, §32 and §36; embeddings, §37".
- [[Differentiable Manifolds]] roadmap: it ended at §37. I added one sentence to the first paragraph and one clause to the bridges paragraph to cover §38 (the projections onto projective spaces and the Hopf fibration) and §39 (the double cover SU(2) → SO(3)).
- [[§36 Immersions]]: "References: Lee Ch. 4. Lecture 13." → "Lectures 13–14", since the proof is Lecture 14.

### Structure
- [[Differentiable Manifolds Lee Concordance]], A.3: I added rows for [[§8 Spheres|§8]] (Example 1.4), [[§9 Complex Projective Space|§9]] (Problem 1-9; Example 1.5 for ℝPⁿ), [[§15 The Classical Groups|§15]] (Propositions 21.34 and 21.35) and [[§38 Projective Spaces and the Hopf Fibration|§38]] (Problem 4-5(a), the Hopf map of Ch. 21, Example 10.18 and Proposition 10.19). All counterparts come from those sections' own *Lee:* lines, which agree with A.4. "Propositions 21.34 and 21.35" moved from the §10–§11 row to the new §15 row: no box in §10 or §11 cites them, and A.4 maps them to §15 only.
- *References:* lines added to [[§32 Submersions]], [[§35 The Tangent Bundle]] and [[§38 Projective Spaces and the Hopf Fibration]]. They were the only Ch. 5 sections without one, and their content comes from the Course Log and the sections' *Lee:* lines.
- [[§1 Point-Set Topology Review]] and [[§2 Topological Manifolds]]: the opening line "*Foundations — …*" → "*Stage: foundations — …*", like §16–§18, so that every section opens with a Thread/Stage label.
- [[· 1 Topological Manifolds]], [[· 2 Topological Groups and Homogeneous Spaces]] and [[· 3 Smooth Structures]]: removed the doubled blank lines under the ↑ line, so all five chapter notes match.

### Writing
- [[§1 Point-Set Topology Review]], Remark rem-1-10: it said both (∗) items "were not recorded" in 590. Its own Connections callout says (1) is proved in 590 after Def. §9.1, and I confirmed that in the Topology note. The remark now says the first is also in 590 and the second is not.
- [[§7 The Regular Value Theorem]], proof of Cor. §7.2: "Set $h = F$ in Lee's notation" was ambiguous. It now reads "Take $W' = V_0$, $J = W_0$, and for $h$ the function called $F$ in that theorem (Lee's notation)".
- [[§9 Complex Projective Space]]: two consecutive transcription notes reported the same board error ($S^{2n+2}$ for $S^{2n+1}$). I merged them into one, keeping every detail (board, page 7, why the target is $S^{2n+1} \times S^{2n+1}$).
- Unbalanced quotation marks in *Lee:* lines fixed in [[§13 Homogeneous Spaces]] ("closed by continuity"), [[§16 Differentiable Structures]] ("smoothly compatible", "smooth atlas") and [[§19 Manifolds in Euclidean Space]] ("local parametrization").
- [[§13 Homogeneous Spaces]], Theorem §13.2: the provenance tag said "filled in", but the box (titled "Exercise") only outlines the argument and ends "the argument is left here". The tag now says "outline only". The proof itself was not touched (see the placeholder list).

### Connections
- [[§10 Topological Groups and Classical Matrix Groups]], proof of Prop. §10.2: "(1)–(3) are proved in MATH 493 (Dummit–Foote §3.5)" now links the vault's home for those results, [[§21 The Sign Homomorphism and the Alternating Group|493 §21]], and keeps the Dummit–Foote reference. The vault's MATH 493 notes follow Pinter.
- I checked the links to Multivariable Analysis. The implicit function theorem ([[Implicit Function Theorem (vector-valued)]], §7.1) and the inverse function theorem (§31.1) both link [[Implicit Function Theorem]] / [[Inverse Function Theorem (several variables)]] and say correctly what 452 proves: the one-equation IFT, and the inverse function theorem in two variables. The rank theorem and the regular value theorems have no 452 counterpart; their 452 links (Lagrange multipliers, constraint sets) are accurate. Nothing in the subject claims that [[Generalized Stokes' Theorem]] or the [[Poincaré Lemma]] is proved here; they appear only as "Coming later in the course". No edit was needed.

### Hubs
"Its proof uses" now matches the proof's *Uses:* line. I checked each proof; the removed entries were pointers or comparisons, not uses:
- [[Hausdorff Criterion for Open Quotients]]: removed Theorem §6.3. It appears only in the statement's *Lee:* line ("see the comparison below Theorem §6.3").
- [[ℂPⁿ Is Hausdorff and Second Countable]]: removed Corollary §12.4. The proof title calls it "the general form", a forward pointer.
- [[Images of Embeddings Are Submanifolds]]: removed Remark rem-37-1, a pointer to "the remark after the proof".
- [[Injective Proper Immersions Are Embeddings]]: removed Def. §36.1 and Def. §37.2. They are cited in the statement, not in the proof's *Uses:* line.
- [[Regular Value Theorem for Manifolds]]: removed Theorem §23.3. The proof mentions it only as "the argument of Lecture 8 … one level up". For the same reason, Theorem §33.6 was removed from the "Used in" list of [[Geometric Tangent Space Is the Kernel of the Jacobian]].
- [[Implicit Function Theorem (vector-valued)]]: removed [[Implicit Function Theorem]] (452) from "Its proof uses (other subjects)". The sketch cites it only as "special cases are proved in MATH 452"; it remains in the hub's Connections.
- [[SU(2) Is a Double Cover of SO(3)]]: removed 590 Def. §9.2. It is cited in the statement only.
- [[Immersion Normal Form]]: the hub listed Def. §16.3 and Def. §18.3, which the proof's completion of step 4 does cite inline but the *Uses:* line of [[§36 Immersions]] omitted. I added both to that *Uses:* line, so hub and line agree.

"Used in" lists:
- [[Geometric Tangent Space Is the Kernel of the Jacobian]] and [[Regular Level Sets Are Smooth Manifolds]]: added Example §7.2, whose *Uses:* line cites both results.
- [[Regular Level Sets Are Smooth Manifolds]]: removed Example §19.2. It mentions Prop. §19.2 only as "the same picture is what Proposition §19.2 formalizes", and Prop. §19.2's proof uses the example, not the reverse.
- [[Tangent Bundle Is a Smooth Manifold]]: added Prop. §35.1, whose proof uses the transition computation of Prop. §35.2.

### Computed counts
- [[· 2 Topological Groups and Homogeneous Spaces]] and [[· 5 Maps of Constant Rank and Bundles]]: "Builds on (other subjects)" left out [[Group Theory]], although the home Mermaid diagram draws Group Theory → Ch 2 (9) and → Ch 5 (7). The *Uses:* lines cite Group Theory 8 times in Ch 2 and 7 times in Ch 5. I added "[[Group Theory]] (9)" and "(7)", using the numbers already in the diagram so that the chapter notes and the diagram agree. The 9 vs 8 difference is flagged below. All the other chapter-note counts already agree with the diagram, and every "Builds on"/"Used by" pair is reciprocal.

## Flagged for the author (not edited)
- **Computed counts cannot be reproduced exactly.** Counting the subject-resolved links on *Uses:* lines (both at HEAD and at commit fd9c72e) matches many chapter-note counts exactly: Linear Algebra in every chapter, Multivariable Analysis for Ch 2 and Ch 3, Single Variable Analysis, and Group Theory for Ch 5. It does not match these (recount vs stated): Ch 1 Topology 46 vs 65 and Multivariable Analysis 3 vs 5; Ch 2 Ch 1 48 vs 53 and Group Theory 8 vs 9; Ch 3 Linear Algebra 9 vs 10, Ch 1 39 vs 41 and Ch 2 13 vs 12; Ch 4 Topology 5 vs 6, Multivariable Analysis 10 vs 11, Ch 1 16 vs 17, Ch 2 3 vs 4 and Ch 3 28 vs 35; Ch 5 Topology 37 vs 47, Multivariable Analysis 5 vs 7, Ch 1 33 vs 37, Ch 2 7 vs 6 and Ch 3 35 vs 44. Because the generator's method is unknown, I left these counts, and the Mermaid labels, unchanged.
- [[§3 Subspaces and Products]], Remark "Why the Universal Property Matters": it calls the characteristic property of the product topology "Lee Prop. A.16", while the box's *Lee:* line (and the concordance) gives Proposition A.23(a). I cannot check Lee's numbering here.
- Hub "Used in" lists also include items that cite the result only in their body and have no *Uses:* line: Ex. §23.2 and Ex. §23.3, Ex. §14.1 and Ex. §14.2, Ex. §12.3, Cor. §27.7, Prop. §37.2 and Prop. §37.11. I checked that each body does cite the hub result, so I left them. Several examples in [[§12 Group Actions and Orbit Spaces]], [[§14 The Topology of G∕H and Real Grassmannians]] and [[§23 Tangent Spaces I꞉ The Geometric Picture]] have no *Uses:* line, while others (e.g. Ex. §8.2) do. Whether examples should carry one is the author's convention.
- [[§27 Coordinate Derivations and the Basis Theorem]], Hadamard's lemma: the transcription note and the paragraph after it both report the student's correction of the integration path. This is mild duplication, and I left it because the two paragraphs make different points.
- [[Differentiable Manifolds Course Log]], Lecture 10 row: Ex. §38.1 and Ex. §38.2 are grouped under the §31 and §32 headers. Their labels are correct and the grouping looks deliberate (taught with those sections), so I left it.
- [[Differentiable Manifolds]]: the roadmap figure (m591-0-1.svg, in attachments/, outside my scope) may not show §38–§39, which the text now mentions.

## Placeholder proofs still open
None of these was written, since the course is in progress.
- [[§1 Point-Set Topology Review]]: Proof (to be filled) of Prop. §1.5(2)–(4) (^pf-1-5-2), Prop. §1.6 (^pf-1-6), Prop. §1.7(1),(2),(4) (^pf-1-7-2) and Prop. §1.8 (^pf-1-8). All four are proved in MATH 590 and linked there.
- [[§2 Topological Manifolds]]: Theorem §2.1, topological invariance of dimension (^pf-2-1); not proved in the course (Lee Thm 17.26).
- [[§15 The Classical Groups]]: Theorem §15.2, GL(n,ℝ) has exactly two components (^pf-15-2).
- [[§20 Linear Algebra Toolkit]]: Prop. §20.1, standing facts from linear algebra (^pf-20-1); imported from [[Linear Algebra]].
- [[§31 Local Diffeomorphisms]]: Theorem §31.1, the inverse function theorem (^pf-31-1); taken from analysis.
- [[§34 Fibrations]]: Theorem §34.3, Ehresmann's theorem (^pf-34-3); needs connections, which the course does not cover.
- [[§4 Quotient Spaces and Open Maps]]: Prop. §4.2, the two constructions of the line with two origins agree. The proof is an "Exercise … assigned in lecture and left here" (^pf-4-2).
- [[§13 Homogeneous Spaces]]: Theorem §13.2, isotropy subgroups are closed. The box is an outline only, and the lecture said closedness "may be the next assignment" (^pf-13-2).

There are nine "(to be filled)" boxes in all; the prompt counted ten. With the two exercise/outline boxes the total is eleven. Also cited but not proved, by design: Lemma §37.10 (Dirichlet, cited from Lee) and Borel's theorem in Ex. §25.2.

## Requests outside my scope
- Multivariable Analysis: the hub [[Inverse Function Theorem (several variables)]] has the alias "inverse function theorem in ℝⁿ", but the theorem it embeds (452 §13.2) is the two-variable statement. Manifolds §7 and §31 describe 452 as proving "the two-variable case". The MVA owner may want to adjust the alias or the hub text.
- No other-subject note currently links into Manifolds with a stale §-label. I scanned the whole vault; the stale labels in the MVA hubs (Hadamard, chain rule, IFT) had already been corrected by the MVA pass.

## Checks run
- Frontmatter keys, `chapter`/`section` values, nav lines, and item numbering (each kind runs 1, 2, … per section) in all 39 section notes: no problems.
- Every definition/theorem/example callout followed by a block ID matching its title number: no problems. Proofs without a *Uses:* line: only the 9 "(to be filled)" boxes and the §4.2 exercise.
- Every "§N"/"§N.M" link label (and every hub label) checked against the block or embedded hub target: 18 mismatches found and fixed, and none remain apart from three correct "Remark after §X.Y" labels. Plain-text § references reviewed by hand: 1 more fixed (§12 proof title).
- Link labels naming the item kind (Prop./Cor./Thm.) checked against block IDs: 10 fixed.
- Hub "Its proof uses" compared with proof *Uses:* lines for all 32 hubs: 8 hubs corrected. "Used in" lists compared with backlinks: 5 changes, 8 body-only citations accepted.
- Central-results labels on the home and chapter notes checked against the hub embeds: all 32 agree.
- Course Log: lecture dates and weekdays, exam weekdays, and group headers vs the items they contain all checked.
- Citation recounts from *Uses:* lines at HEAD and at fd9c72e (see Flagged).
- Unbalanced quotation marks across the subject: 4 fixed.
- Computations re-checked by hand: stereographic transition $1/u$, the angle-atlas transition, Example §7.2 (rank locus, kernel at $x_0$) and Example §7.3 ($M \cong \mathbb{C}^\times$), the Jacobi formula/cofactor identity, O(n) and U(n) surjectivity and $dF_g(ih)$, the Hopf trivialization and its inverse, $\Psi_s^{-1}$ in Prop. §38.1, the quaternion matrices $F(q)$ and $R_q$, $\sigma_j$, $G_{*I}(\sigma_j) = 2\hat e_j$, and the immersion normal-form construction. No errors found.
- `links.py`: no unresolved links or block references in `Math/Differentiable Manifolds/`. `$` parity and callout syntax re-checked in all 43 edited files.
