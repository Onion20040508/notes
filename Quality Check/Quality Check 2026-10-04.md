---
type: quality-check
date: 2026-10-04
scope: "Math/ and Applied Math/"
mode: record only
tags: [quality-check]
---
# Quality Check 2026-10-04

A quality check of the 14 subjects in `Math/` and `Applied Math/` (1,210 notes), covering structure and arrangement, writing quality, connections, and correctness.

> [!note] Record only
> **No note was changed.** Every note in `Math/` and `Applied Math/` is exactly as it was at commit `77b885d` (vault backup 2026-10-04 15:25). The findings are recorded in the subject logs below. Every proposed change is also saved, as exact text, in `Quality Check/proposed-edits.patch`: 385 files, +1004 / −689 lines, made against `77b885d`.

## Subject logs
Each log has the same sections: Summary · Proposed edits (not applied), grouped by kind · Flagged for the author · Placeholder proofs still open · Requests outside its scope · Checks run.

| Subject | Notes | Files the patch touches | Log |
|---|---|---|---|
| [[Logic and Proofs]] | 54 | 7 | [[QC Logic and Proofs]] |
| [[Linear Algebra]] | 71 | 55 | [[QC Linear Algebra]] |
| [[Single Variable Analysis]] | 58 | 17 | [[QC Single Variable Analysis]] |
| [[Multivariable Analysis]] | 56 | 19 | [[QC Multivariable Analysis]] |
| [[Topology]] | 76 | 26 | [[QC Topology]] |
| [[Measure Theory]] | 61 | 14 | [[QC Measure Theory]] |
| [[Functional Analysis]] | 79 | 17 | [[QC Functional Analysis]] |
| [[Differentiable Manifolds]] | 86 | 44 | [[QC Differentiable Manifolds]] |
| [[Group Theory]] | 103 | 23 | [[QC Group Theory]] |
| [[Calculus]] | 158 | 21 | [[QC Calculus]] |
| [[Applied Linear Algebra]] | 80 | 31 | [[QC Applied Linear Algebra]] |
| [[Ordinary Differential Equations]] | 60 | 19 | [[QC Ordinary Differential Equations]] |
| [[Fourier Series and PDEs]] | 88 | 26 | [[QC Fourier Series and PDEs]] |
| [[Complex Variables]] | 180 | 66 | [[QC Complex Variables]] |

The logs list a few proposals that are **not** in the patch, because they were planned but never written into the notes. Most of these are in [[QC Single Variable Analysis]]: about 150 new `*Uses:*` lines and `type: section` frontmatter for 37 notes. [[QC Logic and Proofs]] and [[QC Linear Algebra]] are in the same situation for some items. Their logs give the exact text to add.

## How the check was done
- **Scripts over every note:**
  - every wikilink, block reference and embed resolves;
  - frontmatter keys;
  - the nav line `← · ↑ · →`;
  - callout syntax, and the block ID of every definition, theorem and example box;
  - numbering continuity;
  - `$` balance;
  - macros against `preamble.sty`;
  - visible "§N.M" labels against the block each one links to;
  - each hub's "Its proof uses" list against the section's `*Uses:*` line;
  - duplicate headings;
  - placeholders.
- **Reading:** every section note at least at skim level, and a large share in depth. All hubs, chapter notes and home notes were read in full.
- **Recomputation:** several hundred worked computations were redone by hand or with sympy, numpy or mpmath.
- **Rules:**
  - Nothing developed was to be removed.
  - No file was renamed and no block ID changed.
  - A mathematical change was proposed only after it had been verified.
  - Placeholder proofs, which include live coursework in 493, 556 and 591, were listed but not written.

## Overall verdict
The vault is in very good shape:
- Across the in-depth reading, no theorem statement was found to be false. Every recomputed example agreed with the notes, except for the one error in a remark listed below.
- Of 86,000+ links, one is broken ([[Pasting Lemma]]).
- No macro is undefined, and every `$` is balanced.

Most proposals are **bookkeeping that has fallen behind the notes' growth**: stale "§N" labels left by renumbering, hub dependency lists that disagree with the proofs, and status lines older than the latest lectures. The rest are wording fixes and new cross-subject connections.

## Highest-priority proposals (correctness)
- **[[Multivariable Analysis]] §18, rem-18-8:** calls a solid hemisphere and a solid cone "non-convex". Both are convex. → [[QC Multivariable Analysis]]
- **[[Topology]] §15, Thm 15.10, Step (3):** "taking $d = a$ if $c = a$" is impossible, because $(a, a]$ is empty. The case $c = a$ belongs to Step (2). → [[QC Topology]]
- **[[Topology]] §21, Rem 21.11 table:** lists "$P^n$" for $\mathbb{Z}/n\mathbb{Z}$, but $\pi_1(P^n) = \mathbb{Z}/2$.
- **[[Topology]] §26, Cor 26.4 "Up":** the direction of inheritance is reversed.
- **[[Topology]] §21.5:** "surjective" should be "bijective".
- **[[Measure Theory]] §18, Thm 18.27 proof:** $r$ is used before it is chosen, and the gap sums are undefined. The proposal restructures the proof; the argument is unchanged. → [[QC Measure Theory]]
- **[[Measure Theory]] §18, Cor 18.14(iii):** a spurious $h'$ term.
- **[[Measure Theory]] §16.7 and §19.19:** "equality only on transition intervals" should be "vanishes outside".
- **[[Single Variable Analysis]] §32.7:** the proof ends with $\le\varepsilon$ where the criterion needs $<\varepsilon$.
- **[[Single Variable Analysis]] §19.5:** misses the case $M = 0$.
- **[[Single Variable Analysis]] §2.7:** cites Thm 2.5 where it means 2.6. → [[QC Single Variable Analysis]]
- **[[Calculus]] §10, Ex 10.5:** "$f' \ge 0$, so $f$ is increasing" cites a test that needs $f' > 0$. The proposal gives the exact cube form and the exact root. → [[QC Calculus]]
- **[[Multivariable Analysis]] §4.1:** a missing step in the final estimate.
- **[[Multivariable Analysis]] §15.1:** a garbled sentence in the proof.
- **[[Linear Algebra]], dependency records:** 7.21, 8.9 and 9.12 cite the box *before* the result they use. The 3.21 annotation "(Filled in; implicit in Axler)" is inaccurate. → [[QC Linear Algebra]]
- **[[Complex Variables]] §76:** cites a single-curve Green's theorem for a region with holes. → [[QC Complex Variables]]
- **[[Applied Linear Algebra]] §9:** two LADR citations are swapped. → [[QC Applied Linear Algebra]]

## Patterns that recur across subjects
1. **Stale numbers left by renumbering.**
   - [[Differentiable Manifolds]] has about 24 (the Course Log, remark labels, and the Immersion Normal Form hub).
   - [[Functional Analysis]] has 6.
   - Cross-subject citations of [[Group Theory]] are stale: "493 §38.1" should be §41.1, and "493 §26.2" should be §28.2.
   - Citations of Manifolds from [[Multivariable Analysis]] hubs and from [[Topology]] are stale too.
2. **Hub "Its proof uses" lists disagree with the proofs' `*Uses:*` lines.** This affects dozens of hubs across ODE, Fourier, Complex Variables, Linear Algebra, Group Theory, Manifolds and Calculus. The patch touches 137 hub files in all. The lists seem to have been generated from every link inside a proof, including "compare" pointers. The proposal moves each wrong entry to Connections and does not drop it.
3. **Section wording copied into hubs** ("below", "above", "(3)", "Steps 4–5", "proof of (b) above"). These point at nothing inside the hub, and the proposal relinks each one.
4. **Truncated or garbled hub text.**
   - Truncated: the [[Cauchy–Riemann Equations]] hub stops mid-sentence, and so does the "rank–nullity" line in [[Fundamental theorem of linear maps]].
   - Garbled: LaTeX was stripped from some titles, giving "Keralpha", "oplus", "M^perp", "Simultaneous diagonalizablity", and adjoint stars missing in LADR 7.6 and 7.9.
5. **Missing "Rigorous treatment" links in Applied Math hubs** that the section notes have. Calculus has 3 and Applied Linear Algebra has 6.
6. **Stale status lines.**
   - Manifolds says the immersion normal form is "stated only".
   - The Group Theory Toolkit says it is current through Sept 25.
   - Functional Analysis says "fifteen" strategies; there are 18.
   - The Functional Analysis Course Log says Thm 26.5(2) is still open.
   - The [[Measure Theory]] home note says Axler chapters 1–5; §18 and Lᵖ follow other sources.
7. **Generated counts can't be reproduced.** These are the "Builds on / Used by (N)" counts, the "N later results" counts and the Mermaid edge labels. Most agents could not reproduce the generator's counting rule from the `*Uses:*` lines and left the counts alone. Applied Linear Algebra and Logic could reproduce theirs exactly, and their logs propose corrected counts.
8. **Connection gaps.**
   - [[Linear Algebra]] has almost no links back to the analysis subjects that cite it 77 times.
   - [[Logic and Proofs]] has few inbound links.
   - [[Applied Linear Algebra]]'s "Developed further in" lines omit ODE (62 links), Fourier (23) and Complex Variables (23).
   - Applied Math hubs had no "Its proof uses (other subjects)" section.
   - In all, the patch adds about 470 links. These are new cross-subject connections and rigorous-treatment links, plus plain-text references such as "Theorem §N.k" turned into links. Every target was checked.

## Open placeholder proofs (not written; several are live coursework)
- **[[Group Theory]]:** 10 marked `[To be proved.]`: §29.6 Cauchy, §32.5, §38.3, §39.4, §39.8, §42.4 Third Isomorphism Theorem, §43.7, §43.12, §43.13, Ex. §43.3.
- **[[Differentiable Manifolds]]:** 9 marked "(to be filled)", plus the Prop. §4.2 exercise and the Thm §13.2 outline.
- **[[Functional Analysis]]:**
  - §26.3 (homework, after submission);
  - §27.4 and §28.2 Lax–Milgram ("next lecture");
  - §17.4 (density, cited from 551 for now).
- **[[Topology]]:** §11.3, $\mathbb{R}^\omega$ is metrizable ("To be completed").

## Requests outside Math/ and Applied Math/
- **README.md:**
  - The statistics are stale: 815 / 443 / 195 / 25,000+ against the actual 1,892 notes / 1,226 sections / 326 hubs / 86,000+ links.
  - Applied Linear Algebra also has Ch. 8 (Lay Appendix B).
  - The callout table lacks `question`, `law` and `model`.
  - The `Physics/Conventions` link is broken.
- **Physics notes:** "Mathematical Methods (planned)" appears in 36 Physics notes. Applied Math already covers many of those targets: Picard–Lindelöf, Sturm–Liouville, Bessel/Legendre and contour integration.

## Applying proposals later
`proposed-edits.patch` is an ordinary `git diff` against commit `77b885d`. From the vault root:
- **Apply everything:** `git apply --3way "Quality Check/proposed-edits.patch"`
- **One subject:** `git apply --3way --include='Math/Topology/*' "Quality Check/proposed-edits.patch"`
- **Inspect first:** `git apply --stat …` or open the file in any diff viewer.

`--3way` lets git merge the changes into notes you have edited since 15:25 today. Any real overlap is marked as a conflict for you to resolve.
