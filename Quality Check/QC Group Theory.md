---
type: quality-check
subject: "[[Group Theory]]"
date: 2026-10-04
tags: [quality-check]
---
# Quality check: Group Theory
↑ [[Quality Check 2026-10-04]]

> [!note] Record only
> None of the changes in this log were applied: every note is exactly as it was before the check. Each change below is a **proposal**. The exact text of every proposed change is saved in `Quality Check/proposed-edits.patch` (see [[Quality Check 2026-10-04]]).

## Summary
Group Theory (MATH 493, in progress) is carefully built: all 47 sections share the header pattern, numbering is continuous, and every numbered box has a block ID and its proofs have *Uses:* lines. I checked every link alias against its target block and compared every hub with its section note's *Uses:* line. The newest material (Chapters 8–9) was read in depth, and the permutation computations in §43 and §46 were verified by script. The problems were bookkeeping, not mathematics: summaries and chapter notes had not caught up with the lectures of Sept 28 – Oct 2 and Problem Set 4, two stale 591 labels, LaTeX names that had been stripped badly in hub titles, ambiguous bare labels on examples, and three hubs whose "Its proof uses" disagreed with the proof. A few genuine connections to Logic and Proofs and Differentiable Manifolds were added. No proof was written and no course-record fact was changed.

## Proposed edits (not applied)
### Correctness (labels and references)
- [[§30 Orbit–Stabilizer]] and [[Orbit–Stabilizer Theorem]] — [[Homogeneous Spaces Are Coset Spaces]] was labelled "591 Thm. §7.8"; it embeds 591 Thm. §14.3, and the label now says so.
- [[§3 Basic Examples of Groups]] — [[Classical Groups Are Manifolds]] was labelled "591 Thm. §5.8"; it is 591 Thm. §11.6.
- Ambiguous labels: definitions, the theorem family and examples are numbered separately, so a bare "§38.1" reads as Prop. §38.1. Bare labels pointing to examples or definitions now carry the kind: [[§28 Left and Right Cosets]] ("A Non-Normal Subgroup of S₃, Ex. §38.1"), [[§3 Basic Examples of Groups]] ("The Group S₃ in Detail, Ex. §10.1"), [[Actions Are Homomorphisms to S_X]] ("representation (Def. §20.6)"). A script found no other bare label that points to a definition or example.

### Structure / stale status
- [[Group Theory Toolkit]] — "Current through the lecture of Fri Sept 25" now reads "Current through the lecture of Fri Oct 2 … and Problem Set 4", because the Toolkit already cites §42 (Oct 2), §43 (Sept 28–30) and §46 (PS 4).
- [[· 9 Characters and Commutators]] — the source line listed only "PS 2.3 and 2.4", but the chapter treats PS 4.2, 4.4 and 4.5 (abelianization, commuting normal subgroups, characters of Sₙ, as in the Course Log). Those were added.
- Chapter source lines brought in line with the [[Group Theory Course Log]]'s problem-set mapping: [[· 4 Homomorphisms and Isomorphisms]] (WS 3.1, 3.4; PS 1.2–1.4, PS 2.2), [[· 6 Group Actions, Cosets, and Lagrange's Theorem]] (PS 3.1, 3.3), [[· 7 Conjugacy and the Center]] (PS 3.4–3.6), [[· 8 Normal Subgroups and Quotient Groups]] (PS 3.2, 4.1, 4.3).
- [[Group Theory Conventions and Notation]] — the provenance row linked PS 1–3 only; PS 4 was added.
- [[Group Theory]] — the Mermaid diagram declares a Topology node with no edges. Topology is cited once each from Chapters 1 and 6, below the drawing threshold of 2. The caption now explains the node without arrows; no edges or counts were invented.
- [[§39 Sources of Normal Subgroups]] — the caption of the S₄ figure said "Apart from {e} and S₄, no other union of classes…", which seemed to exclude V and A₄. It now reads "Apart from these two, {e} and S₄, no union…" (the class sizes 1, 6, 3, 8, 6 were rechecked: the only unions containing e whose sizes divide 24 are 1, 4, 12 and 24).

### Hubs
- [[First Isomorphism Theorem for Groups]] and [[Quotient Groups]] — the link title "∣G∣ = ∣Keralpha∣ · ∣Imalpha∣" (`\alpha` dropped) is now "∣G∣ = ∣Ker α∣ · ∣Im α∣". [[Cosets Partition a Group]] — "alpha(n)", "alpha⁻¹(n)" became "α(n)", "α⁻¹(n)".
- [[First Isomorphism Theorem for Groups]] — "Coming later in the course: the second and third isomorphism theorems…" is out of date, since the Second is proved in §42.2. It is now "Next in the course", saying that the Second is proved (with a link), the Third is stated with its proof to come, and the correspondence theorem is still to come.
- [[Second Isomorphism Theorem for Groups]] — Connections were written in `$…$` LaTeX, unlike the sibling hubs; they were rewritten in plain Unicode with the same content. The "How." link now goes to the proof block, and "Next." now says the Third Isomorphism Theorem's proof is still to come. [[Orbit–Stabilizer Theorem]] — the one `$p_{\ast}\pi_1(E, e_0)$` was rewritten as p_∗π₁(E, e₀).
- "Its proof uses" aligned with the proofs' *Uses:* lines after reading each proof:
  - [[Cancellation Laws in Groups]] — Ex. §2.1 was removed from the list. The proof does not use it; the example is still listed under "Used in" and Connections.
  - [[Subgroups of Cyclic Groups Are Cyclic]] — Prop. §5.1 was removed from the list. The proof only remarks that the ℤ case is §5.1; it is still in Connections ("Subgroups of ℤ").
  - [[Quotient Groups]] — the two §38 remarks were removed from the list, because the proof cites them only as the lecture's alternative argument. They are now named in a sentence under Connections, with both links kept.
  - [[§42 The Second and Third Isomorphism Theorems]] — the proof of §42.2 uses the projection π of Def. §40.1. Def. §40.1 was added to its *Uses:* line, which now agrees with the hub.
- [[Bézout's Identity]] — "the subgroup proof above" (section-relative wording) now points to §5.2 explicitly.

### Connections
- [[Cosets Partition a Group]] — added "Foundation in [[Logic and Proofs]]": 250 Thm. §22.3 (classes are equal or disjoint) and [[Equivalence Relations Are Partitions]] (250 Cor. §22.4). The target blocks were checked.
- [[Actions Are Homomorphisms to S_X]] — added the topological version: for a continuous action each translation is a homeomorphism (591 Lemma §12.2; the target was checked).
- [[Matrix groups GLₙ, SLₙ and O(n)]] — added a pointer to the reciprocal 591 workhorse example [[Classical groups O(n), U(n), SL(n,ℝ)]], which already links back here.
- Checked but not needed: the modular-arithmetic notes already link Logic and Proofs throughout §6–§9 and §24 (2–7 links each). The CRT has no counterpart in Logic and Proofs. The 590/591 links in Chapters 1, 4 and 6 are dense and their labels match their targets.

## Flagged for the author (not edited)
- [[Group Theory]] and the chapter notes — computed counts do not match a recount from *Uses:* lines. For example, Linear Algebra → Chapter 5 is labelled 17, but Chapter 5's *Uses:* lines contain 14 LADR links; → Chapter 6 is labelled 7 against 6; → Chapter 7 is labelled 5 against 4. The home's "Prerequisites" list gives Definition 3.31 (2) against 1 *Uses:* link. The generator evidently also counted body citations. The counts were left unchanged (rule 6).
- Hub "Used in" lists include citations from proof bodies and only *later* results. For example, [[Subgroups of ℤ]] lists §17.4, whose *Uses:* line does not cite §5.1; [[Lagrange's Theorem]] omits §17.6, which cites it from an earlier section. This looks like a deliberate design and was not changed.
- The coordinator asked about two circularities: the proof of §11.6 citing §23.5 and back, and Thm. §27.6 deferring to its own corollary §27.7. Neither is in Group Theory or Functional Analysis: GT has no §11.6, §23.5, §27.6 or §27.7 blocks. They match Differentiable Manifolds (591 Thm. §11.6 *Classical Groups Are Topological Manifolds* ↔ §23; 591 §27 *Coordinate Derivations and the Basis Theorem*, Cor. §27.7). Forwarded under "Requests outside my scope".
- No "SU(2) hub" exists in Group Theory, so the ambiguous-label fix was applied wherever a bare label points to an example or definition (see above).
- [[· 9 Characters and Commutators]] has no "Central results" section, because it has no hubs. This is consistent with the generator.

## Placeholder proofs still open
All are `*[To be proved.]*` and were left unwritten. Several are live coursework.
- [[§29 The Index and Lagrange's Theorem#^thm-29-6|Thm. §29.6]] (Cauchy's theorem); [[Group Theory Toolkit]] trap 8 says it is not proved in these notes, which is consistent.
- [[§32 Linear Groups, the Cube, S₃ and A₄#^thm-32-5|Thm. §32.5]] (the rotation group of the cube is S₄).
- [[§38 Normal Subgroups#^thm-38-3|Thm. §38.3]] (five characterizations of normality; WS 6.1).
- [[§39 Sources of Normal Subgroups#^prop-39-4|Prop. §39.4]] (preimages and images of normal subgroups; WS 6.6).
- [[§39 Sources of Normal Subgroups#^prop-39-8|Prop. §39.8]] (normal subgroups of GL₂(ℝ); WS 6.3).
- [[§42 The Second and Third Isomorphism Theorems#^thm-42-4|Thm. §42.4]] (Third Isomorphism Theorem; named in lecture 10/2).
- [[§43 Simple Groups#^thm-43-7|Thm. §43.7]] (A₅ is the smallest non-abelian simple group; not from class).
- [[§43 Simple Groups#^thm-43-12|Thm. §43.12]] (classification of finite fields; stated "for culture").
- [[§43 Simple Groups#^thm-43-13|Thm. §43.13]] (PSLₙ(F) is simple).
- [[§43 Simple Groups#^ex-43-3|Ex. §43.3]] (PSL₂(𝔽₂) ≅ S₃, PSL₂(𝔽₃) ≅ A₄).

## Requests outside my scope
- README.md — the four Group Theory problem-set notes use the callout `[!question]` (22 callouts: [[493 Problem Set 1|PS 1]] 6, [[493 Problem Set 2|PS 2]] 5, [[493 Problem Set 3|PS 3]] 6, [[493 Problem Set 4|PS 4]] 5), which is not in the README callout table or the Home callout list. Either add `question` ("problem-set problems") to both lists or decide on another type.
- Differentiable Manifolds QC: check the two circularities reported to me under Group Theory. These are the proof of 591 Thm. §11.6 ↔ §23.5, and 591 Thm. §27.6, whose proof defers to its own Cor. §27.7 (the Connections remark in §27 says "Proved in detail in … §27.7").

## Checks run
- Frontmatter keys by note type (47 sections, 9 chapters, 32 hubs, 7 examples, 3 summaries, 4 problem sets, 1 home): uniform.
- Nav lines on all 47 sections; sections §1–§47 continuous; numbering within each section continuous, and every header number agrees with its block ID (0 mismatches over all numbered boxes).
- Callout of a definition, theorem or example without a block ID, empty callouts, duplicate headings, `$` balance per line: 0 problems. The only callout type outside the README list is `question`, in the problem sets (reported above).
- Link-alias audit, including cross-subject labels such as "591 Thm. §…", "590 §…" and "LADR …": 2 stale 591 labels fixed. Bare-label audit: 3 fixed.
- Hub audit for all 32 hubs ("Its proof uses" against *Uses:*): 4 mismatches fixed. Garbled-title scan of hub link titles: 3 fixed.
- Chapter "Central results" lists against the home list and the Key results folder: 32 = 32 = 32.
- §43.9 (the 5-cycle and two-3-cycle cases), §42 Ex. §42.1, §46.2 and the A₅ class-sum list in §43.6 were recomputed by script: all correct.
- links.py after the edits: no unresolved links or block refs in Group Theory.
