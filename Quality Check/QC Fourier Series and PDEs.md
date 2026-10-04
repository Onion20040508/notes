---
type: quality-check
subject: "[[Fourier Series and PDEs]]"
date: 2026-10-04
tags: [quality-check]
---
# Quality check: Fourier Series and PDEs
↑ [[Quality Check 2026-10-04]]

> [!note] Record only
> None of the changes in this log were applied: every note is exactly as it was before the check. Each change below is a **proposal**. The exact text of every proposed change is saved in `Quality Check/proposed-edits.patch` (see [[Quality Check 2026-10-04]]).

## Summary
The subject (home note, 8 chapter notes, 59 section notes, 20 hubs) is mechanically clean: frontmatter, nav lines, block IDs, numbering, callout titles and `*Uses:*` lines are consistent, and the proofs and computations checked (the convergence proof of §12★, coefficient formulas of §8, the convection eigenvalues and coefficients of §22, the cylinder series of §46★, the error-function examples of §28★) are correct. The problems were in the hubs (proof-uses lists not matching the `*Uses:*` lines, a hub claiming "no proof" for a result proved in §12★, section-relative wording) and in the course record, which did not agree with how ★ was applied to §27 Infinite Rod. Both were fixed; the ★ convention is now stated in the home note. Seven cross-subject connections were added (Functional Analysis, Measure Theory, Complex Variables, Applied Linear Algebra, Multivariable Analysis).

## Proposed edits (not applied)
### Hubs
- [[Convergence Theorem for Fourier Series]] — said "Its proof uses: (no proof in the notes)" and "Treated in" only §8. Added §12★ Theorem §12.4 and Corollary §12.5 to "Treated in", and filled "Its proof uses" (and "(other subjects)") from their `*Uses:*` lines.
- [[Sturm–Liouville Orthogonality Theorem]] — removed Thm. §23.5 (unproved; cited in the proof only for the existence of infinitely many eigenvalues) from "Its proof uses", which now matches the `*Uses:*` line (Def. §23.1, Prop. §23.1); added a Connections bullet explaining that the first sentence of the statement is Thm. §23.5(a). "See the remark below" → link to Remark: Self-Adjointness (`^rem-23-3`).
- [[Orthogonality of Legendre Polynomials]] — removed Ex. §23.2 (context, not used).
- [[Poisson Integral Formula]] — added [[§15★ Complex Methods]] (Exercise 1.10.5a, cited in the `*Uses:*` line).
- [[Uniform Convergence of Fourier Series]], [[Parseval's Equality for Fourier Series]], [[Convergence of Eigenfunction Expansions]] — "(no proof in the notes)" replaced by pointers to what the section notes say: the non-Powers argument in Remark: Where Theorem §9.3 Comes From; 556 Thm. §24.8 with §24.11; the special case proved in §12★.
- Added **Its proof uses (other subjects)** from the `*Uses:*` lines to [[General Solution of Bessel's Equation]], [[Green's Function for Boundary Value Problems]], [[Heat Kernel Solution of the Infinite Rod]], [[Heaviside's Expansion Formula]], [[Laplacian in Polar Coordinates]] (its same-subject line "(only definitions)" was inaccurate and now reads "(none in this subject)"), [[Maximum Principle for Laplace's Equation]], [[Mean Value Property of Harmonic Functions]], [[Poisson Integral Formula]], [[Solution of the Fixed-End Heat Problem]], [[d'Alembert's Solution of the Wave Equation]].
- Section-relative wording reworded with links: [[Series Solution of the Vibrating String]] ("problem (6)–(7)" now states the problem and names §30; "(12) below" → Example §30.1), [[Convergence of Eigenfunction Expansions]] ("remark below" → `^rem-24-1`), [[Mean Value Property of Harmonic Functions]] ("the proof of (b) above" → link to `^pf-39-4`).

### Structure: ★ versus the course record
- Finding: ★ in this subject means "not part of the syllabus coverage" (home note list 1.1–1.5, 1.9, 2.1–2.10, 3.1–3.4, 4.1–4.5, 5.2–5.3), and the ★ notes say "the course did not cover this section". §27 Infinite Rod (Powers 2.11) is outside that list but unstarred, and its header records lectures 10.22 and 10.24, HW 9 and Midterm 2 (Example §27.2 is Midterm 2 Q2), so it was in fact taught; starring it would contradict its own record, and file names cannot change. Conversely §1★, §11★, §15★, §28★ were touched in lectures or supply course problems but were not syllabus sections, so their ★ is right but their ★ notes were partly inconsistent with their headers.
- [[Fourier Series and PDEs]] — coverage sentence now adds that the lectures also solved the infinite rod, 2.11 (lectures 10.22, 10.24, HW 9, Midterm 2), "which is therefore not starred", and states the convention: a starred section can still have been touched on in a lecture (0.1, 1.6, 1.10) or supply course problems as worked examples (1.10, 2.12, 3.6, 6.2), as its header records. Course table row "7–8" now reads "2.7–2.10 …; 2.11 infinite rod | §23–§27"; the midterm line adds "with an infinite-rod problem from 2.11". Nothing was removed.
- [[§15★ Complex Methods]] — ★ note "the course did not cover this section" now adds "apart from presenting the complex form as a bonus topic in lecture 10.3, which the bonus questions of both midterms used" (as the intro already said).
- [[§11★ Mean Error and Convergence in Mean]] — ★ note now says "beyond remarks in lectures 9.10 and 9.12" (as the header says).
- [[§28★ The Error Function]] — ★ note adds that Examples §28.2–§28.4 revisit course problems (HW 9, Midterm 2, Practice Midterm 2).

### Connections (added in my files; targets checked)
- [[§11★ Mean Error and Convergence in Mean]] — new Connections for Thm. §11.6: the completeness relation, 556 Thm. §31.2 and Ex. §31.2; the converse direction needs completeness of $L^2$, [[Riesz–Fischer Theorem]] (551).
- [[§6 Periodic Functions and Fourier Series]] — new Connections for Prop. §6.4: the coordinate formula in an orthogonal basis, 235 Thm. §41.2 and §46.2.
- [[§14 Fourier Integral]] and hub [[Fourier Integral Theorem]] — Bromwich inversion is this theorem in disguise, 342 Thm. §95.4.
- [[§15★ Complex Methods]] — transforms of rational functions by residues, 342 Prop. §87.1.
- [[§53★ Partial Differential Equations]] — the residue theorem, 342 Thm. §76.1, behind "close the line to the left".
- [[§23 Sturm–Liouville Problems]] and hub [[Sturm–Liouville Orthogonality Theorem]] — Green's second identity, 452 Thm. §17.3, as the several-variable form of the integration by parts.
- Checked on request: [[§39 Potential in a Disk]] (Thm. §39.5) and [[Maximum Principle for Laplace's Equation]] already link 342 Cor. §59.5; no change needed.

## Flagged for the author (not edited)
- The course table's week numbers (e.g. "9–10" for lectures 10.29–11.5, "7–8" for lectures up to 10.24) do not match a calendar count from 8.26 (those lectures fall in weeks 10–11 and 8–9). This may be the author's own week numbering; left as is.
- The coverage list may be in 6th-edition numbering (the course used the 6th edition). The notes map it to 5th-edition sections; if the 6th edition numbers the infinite rod differently, the added "2.11" remark should be adjusted.
- Equation numbers follow Powers, so they appear out of order inside notes; by design, logged only.
- Chapter-note and home-note counts were not recounted (they do not follow from the `*Uses:*` lines alone); the Connections links added today are not reflected in the home note's "Rigorous treatment" counts.

## Placeholder proofs still open
None. Results stated without proof by design (Powers omits the proof; the note says so, often with a pointer or a non-Powers argument): Thms. §8.1 (proved in §12★), §9.1–§9.3, §10.3, §10.4, §10.7, §11.4, §13.1, §14.1, §14.3, §17.4, §19.4, §23.5, §24.2, §33.2, §45.6, §46.3, §48.1, §49.9, §51.1, §52.1, §52.3, §55.2, §56.1, §57.3, Props. §49.1, §52.4, Thms. §1.7, §1.8, §2.4, and the convergence of the double series in §43.

## Requests outside my scope
- Applied Math hubs in other subjects lack the "Its proof uses (other subjects)" section; same treatment suggested.
- Home-note counts ("Rigorous treatment", Mermaid edge labels) should be regenerated if they are to include today's added links.

## Checks run
- All 59 section notes: frontmatter keys (59/59 identical sets), section/chapter numbers, ★ ⇔ `extension` tag (59/59 consistent), nav lines — no problems.
- Every theorem/definition/example callout has a block ID; numbering continuous; no duplicate IDs or headings; no empty callouts; titles in standard format.
- 13 proofs without `*Uses:*` lines: all self-contained (no citations).
- Link labels "§X.Y" vs block IDs: 0 mismatches. Inline `$` balance: no problems.
- 20 hubs: "Its proof uses" compared with `*Uses:*` lines (5 corrected, 10 given an "(other subjects)" section, 3 no-proof hubs given pointers); "Used in" lists checked against citations (all entries do cite the result); section-relative wording: 4 fixed.
- Incoming cross-subject links without a link back were listed and the substantive ones reciprocated (above).
- links.py: no unresolved links or block refs in this subject.
