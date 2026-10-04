---
type: quality-check
subject: "[[Ordinary Differential Equations]]"
date: 2026-10-04
tags: [quality-check]
---
# Quality check: Ordinary Differential Equations
↑ [[Quality Check 2026-10-04]]

> [!note] Record only
> None of the changes in this log were applied: every note is exactly as it was before the check. Each change below is a **proposal**. The exact text of every proposed change is saved in `Quality Check/proposed-edits.patch` (see [[Quality Check 2026-10-04]]).

## Summary
The subject (home note, 5 chapter notes, 35 section notes, 19 hubs) is in very good shape: frontmatter, nav lines, block IDs, numbering, callout titles and `*Uses:*` lines are consistent throughout, and no mathematical error was found in the proofs and worked computations that were checked (about 30 numerical results recomputed with python/mpmath, including the Euler tables of §10, the finance and cooling numbers of §6, the pulse and ramp responses of §24). The main defects were in the hubs: several "Its proof uses" lists had been built from every link in a proof rather than from its `*Uses:*` line, and cross-subject uses were not listed at all. These were regenerated from the `*Uses:*` lines. Other edits: one broken inline-math line, one doubled word, a clarified ★ note, and six new cross-subject connections (Applied Linear Algebra, Calculus, Complex Variables).

## Proposed edits (not applied)
### Correctness
- [[§6 Modeling with First-Order Differential Equations]] — Example §6.3(a): missing spaces around inline math broke the rendering ("`$\$80{,}000$was invested; the remaining$\$508{,}313$ … $\$508{,}948$at$r = 7.5\%$and$\approx …`"). Spaces restored; the numbers were recomputed and are correct.

### Hubs
- [[Principle of Superposition (linear ODEs)]] — "Its proof uses" listed Cor. §14.7, which itself uses Thm. §14.2 (circular); now only Def. §14.1, as in the `*Uses:*` line of §14.2.
- [[Abel's Theorem (Wronskian)]] — removed Thm. §5.1 (mentioned in the proof only as an alternative reading; the `*Uses:*` line is Def. §14.2 and Thm. §4.2).
- [[Classification of 2×2 Linear Systems]] — removed Examples §31.1 and §31.2 (cited as BDP's route, not used by the general proof).
- [[Table of Elementary Laplace Transforms]] — removed Cor. §22.2 and Thms. §23.1–§23.3, §25.2, §26.2 from "Its proof uses": they are the "where proved" column of the embedded table (forward references), not uses of the proof; the `*Uses:*` line lists only §21–§22 results and Taylor's theorem.
- Added the section **Its proof uses (other subjects)** (from the `*Uses:*` lines) to [[Integrating Factor Solution Formula]], [[Solution of Separable Equations]], [[Test for Exact Equations]], [[Variation of Parameters Formula]], [[Laplace Transform of a Derivative]], [[Convolution Theorem for the Laplace Transform]], [[Table of Elementary Laplace Transforms]]. Applied Math hubs had no such section, although the hub layout includes it.
- [[Variation of Parameters Formula]] — Connections: "the extra condition (21)" (an equation number of §18★, invisible in the hub) now states the condition and links [[§18★ Variation of Parameters]].

### Structure / other
- [[§18★ Variation of Parameters]] — the ★ note ("the course skipped this section") sat oddly beside the header's "MATH 331 Written HW 4"; added that Example §18.2 re-solves a HW 4 problem set for undetermined coefficients. ★ in this subject consistently means "section of a taught chapter that the course skipped" (2.9, 3.6, 6.6, 7.7–7.9), matching the home note's homework table.

### Writing
- [[§22 Solution of Initial Value Problems]] — "solves all of them at once once …" → "at once, as soon as …".

### Connections (added in my files; targets checked)
- [[§14 Solutions of Linear Homogeneous Equations; the Wronskian]] — discrete analogue: 235 Thm. §30.5 (n-dimensional solution space of a difference equation) and 235 Prop. §30.6 (Casoratian, either never or always zero).
- [[§17 Nonhomogeneous Equations; Method of Undetermined Coefficients]] — 235 Thm. §30.7 (particular plus homogeneous for difference equations).
- [[§19 Mechanical and Electrical Vibrations]] — Calc Def. §57.4 and Prop. §57.3 (Stewart's spring equation).
- [[§32 Complex-Valued Eigenvalues]] — Calc Def. §62.1 and Ex. §62.2 (predator–prey cycles in the phase plane, as around a center).
- [[§34★ Repeated Eigenvalues]] — new Connections for Prop. §34.1: 235 Thm. §34.3 (geometric ≤ algebraic multiplicity; diagonalizability).
- [[§21 Definition of the Laplace Transform]] — new Connections for Thm. §21.2: the same estimate for complex $s$ starts the Bromwich inversion of 342 §95★ (which cites Thm. §21.2).

## Flagged for the author (not edited)
- Equation numbers follow BDP, so they appear out of order inside notes (e.g. §14 runs (2), (8), (22)–(28)); by design, logged only.
- Chapter-note counts ("Builds on/Used by (N)") and the home note's "Rigorous treatment" counts could not be recounted exactly (they do not follow from the `*Uses:*` lines alone), so they were left; the six new Connections links above (2 to Applied Linear Algebra counted twice in §14, 3 to Calculus, 1 to Complex Variables) are not reflected in the home-note counts.
- Hub "Used in" lists include examples that link the result in their body (not only `*Uses:*` citations); this looks intended and was left. [[Second Shifting Theorem]] and [[Convolution Theorem for the Laplace Transform]] list Thm. §22.6 under "Used in" because the table's "where proved" column cites them.

## Placeholder proofs still open
None. Results stated without proof by design (BDP omits the proof; the note says so): Thm. §14.1, §21.1, §22.4, §27.2, §27.3, §29.1, §29.3, Def. §34.3.

## Requests outside my scope
- The other Applied Math subjects' hubs (Calculus, Applied Linear Algebra, Complex Variables) also lack "Its proof uses (other subjects)"; worth the same treatment for consistency.
- Home-note "Rigorous treatment" counts (ODE home note) should be regenerated by the coordinator's tool if they are meant to include the links added today.

## Checks run
- All 35 section notes: frontmatter keys (35/35 identical sets), section/chapter numbers, ★ ⇔ `extension` tag, nav lines (prev/up/next) — no problems.
- Every theorem/definition/example callout has a block ID; numbering sequences per kind continuous; no duplicate IDs or headings; no empty callouts; callout titles all in the standard format.
- 4 proofs without `*Uses:*` lines (pf-3-1, pf-11-1, pf-17-3, pf-27-1): all self-contained, no citations.
- Link labels "§X.Y" vs block IDs: 0 mismatches. Inline `$` balance in every note; one broken line found and fixed.
- 19 hubs: "Its proof uses" compared with the `*Uses:*` line of the proof (10 hubs changed); section-relative wording (below/above/(N)/Step) searched; 1 fixed.
- Placeholder search (to be proved, next lecture, homework, TODO): none.
- links.py: no unresolved links or block refs in this subject.
