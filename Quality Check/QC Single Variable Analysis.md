---
type: quality-check
subject: "[[Single Variable Analysis]]"
date: 2026-10-04
tags: [quality-check]
---
# Quality check: Single Variable Analysis
↑ [[Quality Check 2026-10-04]]

> [!note] Record only
> None of the changes in this log were applied: every note is exactly as it was before the check. Each change below is a **proposal**. The exact text of the proposed edits that were drafted is saved in `Quality Check/proposed-edits.patch` (see [[Quality Check 2026-10-04]]; also captured in the checkpoint commit `c48deba` before being reverted). The *Uses:* lines, frontmatter keys and hub changes below were planned but never written; their exact content is given here.

## Summary
Single Variable Analysis (home note, 6 chapter notes, 37 section notes, 10 hubs, examples) is mathematically sound: nav lines, block IDs and numbering are consistent, and links.py finds no unresolved link in the subject. Its main gap is structural: unlike every other subject, its 37 section notes have no `type: section` key and its 158 proofs have no *Uses:* lines, so the hubs' "Its proof uses" / "Used in" lists cannot be checked against the sections. All proofs were read to build a citation list (given below); with it, the chapter note's figure of 40 results depending on the [[Characterization of the Supremum]] is reproduced exactly, while the hub says "about 38". Proof-level problems found: a wrong theorem number in §2, an argument in §32 that ends at "≤ ε" without closing the strict inequality, a missing $M = 0$ case in §19, and references to "Part II/III" that no longer match the chapter structure. The four short or stub sections (§12, §16, §21–§22, §27) get a remark each pointing to where the material is developed.

## Proposed edits (not applied)
### Correctness
- [[§2 The Set ℚ of Rational Numbers]], proof of Theorem §2.7. Old: "Since $\overline{\mathbb{Q}}$ is countable (Theorem 2.5)". Countability of the algebraic numbers is Theorem §2.6. New: "([[§2 The Set ℚ of Rational Numbers#^thm-2-6|Theorem 2.6]])". In the same proof "(to be proved later)" → "(not proved in this course; see the Connections below)".
- [[§2 The Set ℚ of Rational Numbers]]: "Later we will see that $\mathbb{R}$ is uncountable." → "The real line $\mathbb{R}$ is uncountable. This course uses the fact without proof; it is proved by Cantor's diagonal argument in 250 Thm. §14.12 and, for $[0,1]$, in 551 Ex. §4.2." (the course never proves it; both targets checked).
- [[§32 The Definition of the Riemann Integral]], proof of Theorem §32.7. The proof ends with $U(f,P) - L(f,P) \le \varepsilon$, while the Cauchy criterion (Theorem §32.4) asks for $< \varepsilon$. Append: "Since $\varepsilon > 0$ was arbitrary (running the argument with $\tfrac\varepsilon2$ in place of $\varepsilon$ gives $U(f,P) - L(f,P) \leq \tfrac\varepsilon2 < \varepsilon$), the Cauchy criterion holds, and $f$ is integrable."
- [[§19 Uniform Continuity]], proof of Theorem §19.5. Old: "take $\delta = \varepsilon / M$:". New: "take $\delta = \varepsilon / M$ (if $M = 0$, then $f$ is constant and any $\delta$ works):".
- [[§1 The Set ℕ of Natural Numbers]], proof of Theorem §1.1: "By (I1) … By (I2)" → "By the initial step (1) … By the induction step (2)" (the statement labels the steps (1), (2); "I1/I2" is never defined).

### Structure
- All 37 section notes: insert `type: section` as the first frontmatter key (every other Math subject has it; other keys unchanged).
- [[· 4 Sequences and Series of Functions]]: add a "## Central results" section (every other chapter has one) before "## Load-bearing results", with block links: Theorem §23.2 (Radius of Convergence), Theorem §24.2 (Uniform Limits Preserve Continuity), Theorem §25.3 (Weierstrass M-Test), Theorem §26.4 (Term-by-Term Calculus for Power Series).
- Stub/short sections, each given a remark (no proofs written):
  - [[§12 Lim Sup and Lim Inf Continued (Skipped)]]: rem-12-1 "Where lim sup and lim inf are treated in these notes" (Def. §10.2–§10.3, Prop. §10.5, Thm. §10.6, Thm. §11.6; uses in §14.9, §14.10, §23.2; Measure Theory §12).
  - [[§16 Decimal Expansions of Real Numbers (Not Covered)]]: rem-16-1 "Decimal expansions elsewhere in the vault" (§4 rem-4-4, 250 Def./Prop. §13.5, Ex. §13.4, §6★ Ex. §6★.2).
  - [[§21 More on Metric Spaces꞉ Continuity]]: rem-21-1 "Where the metric-space theory continues" (590 Thm. §11.7, §11.9, §15.3, §15 remark; Thm. §17.1, §19.1).
  - [[§22 More on Metric Spaces꞉ Connectedness]]: rem-22-1 "Connectedness" (590 Def. §13.1, Thm. §14.4 and the intervals of ℝ).
  - [[§27 Weierstrass's Approximation Theorem (Not Covered)]]: rem-27-1 "The statement, and where it is used": the statement in the language of Def. §24.2; used in Functional Analysis Prop. §11.7; contrast with Taylor polynomials (§31.2).

### Writing
- "Part II / Part III" → chapter links (the notes are organized in six chapters): [[§15 Alternating Series and Integral Tests]] (rem-15-3, "Part III" → Chapter 6), [[§18 Properties of Continuous Functions]] (rem-18-1, "Part II" → Chapter 5), [[§19 Uniform Continuity]] (Thm. §19.5 proof, "(Part II)" → "(Chapter 5, §29)"), [[§23 Power Series]] (rem-23-2), [[§25 More on Uniform Convergence]] (Thm. §25.1 proof), [[§26 Differentiation and Integration of Power Series]] (Thm. §26.4 proof, "proved in Part III" → "proved in Chapter 6, §34").
- [[§22 More on Metric Spaces꞉ Connectedness]], proof: "By the corollary of §18" → link to Corollary §18.5; link the density remark to rem-17-4.
- Proof titles that read "Proof" where several proofs follow one another: [[§10 Monotone Sequences and Cauchy Sequences]] → "Proof of Theorem 10.8"; [[§28 Basic Properties of the Derivative]] (chain rule) → "Proof (first attempt)" / "Proof (repaired)"; [[§30 L'Hospital's Rule]] → "Proof of L'Hospital's Rule (the case $\tfrac00$ as $x \to a^-$)"; [[§32 The Definition of the Riemann Integral]] (pf-32-1) → "Proof of Theorem 32.1".

### Connections
- Added in the stub remarks above (590, 250, 551, 556 targets, all checked to exist and say what is claimed).

### Hubs
Computed from the *Uses:* lines proposed below (union only; nothing removed):
- [[Characterization of the Supremum]]: "about 38 later results rest on it" → "40 later results" (recount with the proposed *Uses:* lines gives exactly 40 theorem-level dependents, as in [[· 1 Introduction]]). Its proof uses: add Def. §4.3. Used in: add Theorem §32.4, Corollary §6★.13.
- [[Completeness Axiom]], line 16: label "Completion of the Construction –- Exercises" → "Completion of the Construction — Exercises" (the block title has an em dash). Used in: add Proposition §5.1.
- [[Monotone Convergence Theorem]]: add the missing "## Used in (Single Variable Analysis)" section before "## Used in (Measure Theory)": Theorem §14.7 (Comparison Test), Theorem §15.3 (Integral Test).
- [[Bolzano–Weierstrass Theorem]]: Its proof uses: add Def. §10.3, Lemma §10.4.
- [[Fundamental Theorem of Calculus]]: Its proof uses: add Theorem §17.1, §32.4, §33.3, §33.4, §33.5.
- [[Squeeze Theorem]]: Its proof uses: add Def. §7.2. Used in: add Proposition §32.5, Theorem §9.9.
- [[Archimedean Property]]: Used in: add Theorem §6★.12. [[Extreme Value Theorem]]: Used in: add Theorem §33.10.

### Proposed *Uses:* lines
One line `*Uses:* …` directly after each `^pf-…` ID, in the vault's format: a block that a hub embeds is linked as `[[Hub|§x.y]]`, otherwise `[[§N Title#^id|§x.y]]`; definitions `Def. §x.y`, examples `Ex. §x.y`, remarks `§N Rem. (title)` (rem-20-2 as "§20 Rem. (limit laws)"). 150 of the 158 proofs; pf-2-1, 2-4, 2-5, 10-4, 13-4, 14-5, 31-1, 32-2 cite nothing and get no line. Citation list (proof ID: cited block IDs):

```
pf-1-1: def-1-1 · pf-1-2: thm-1-1
pf-2-2: rem-2-4 · pf-2-7: thm-2-6, def-2-10
pf-3-1: def-3-1, def-3-2 · pf-3-2: prop-3-1 · pf-3-3: def-3-4, def-3-2, prop-3-1 · pf-3-4: thm-3-3, def-3-5
pf-4-1: def-4-1, def-3-2 · pf-4-2: def-4-1, def-4-2 · pf-4-3: def-4-3 · pf-4-4: def-4-4, def-4-3 · pf-4-5: def-4-4, prop-4-3 · pf-4-6: thm-4-5, prop-3-1 · pf-4-7: thm-4-5, thm-1-2, prop-3-1
pf-5-1: def-4-4, cor-4-4, def-4-3 · pf-5-2: prop-4-3, cor-4-4
pf-6-1: thm-4-5, thm-4-7 · pf-6-3: prop-6-1 · pf-6-4: prop-6-3
pf-6s-1: thm-3-3, def-6s-1 · pf-6s-2: def-6s-2, thm-3-3 · pf-6s-3: lem-6s-1, thm-3-3, def-6s-2 · pf-6s-4: def-6s-1 · pf-6s-5: lem-6s-4, prop-6s-3, thm-3-3, def-3-1, [[§22 Partitions and Equivalence Relations#^thm-22-9|250 §22.9]] · pf-6s-6: lem-6s-4, def-6s-4 · pf-6s-7: lem-6s-6, thm-6s-5, def-3-2 · pf-6s-8: lem-6s-1, lem-6s-6 · pf-6s-9: prop-6s-8 · pf-6s-10: prop-6s-8, thm-6s-7, cor-6s-9 · pf-6s-11: prop-6s-8, cor-6s-9 · pf-6s-12: thm-4-7, def-10-4, thm-10-8, cor-9-6, thm-4-5, thm-10-7, thm-9-3, prop-9-5 · pf-6s-13: prop-9-5, thm-4-7, prop-6-1, def-4-4, prop-4-3, thm-6s-12 · pf-6s-14: prop-3-1, thm-6s-12
pf-7-1: def-7-2, thm-3-3
pf-8-1: def-7-2
pf-9-1: def-7-2, thm-3-3, ex-4-1 · pf-9-2: def-7-2 · pf-9-3: def-7-2, thm-3-3, thm-9-1 · pf-9-4: def-7-2, ex-8-9, thm-3-3 · pf-9-5: thm-9-2, thm-9-3 · pf-9-7: def-9-1 · pf-9-8: def-9-1, thm-9-1 · pf-9-9: def-7-2, ex-8-5, ex-9-10, lem-9-7, thm-8-1
pf-10-1: def-4-4, prop-4-3 · pf-10-2: thm-4-5 · pf-10-3: def-9-1 · pf-10-5: prop-5-1, prop-9-5 · pf-10-6: prop-9-5, thm-8-1 · pf-10-7: thm-3-3 · pf-10-9: thm-3-3, ex-4-1 · pf-10-8: lem-10-9, thm-10-6, lem-10-4, prop-9-5
pf-11-1: def-11-1 · pf-11-2: thm-11-1 · pf-11-3: def-11-1 · pf-11-4: def-9-1, def-11-1 · pf-11-5: prop-4-3, thm-8-1, lem-10-4, def-10-3 · pf-11-6: thm-11-5, thm-11-1, prop-9-5
pf-13-1: def-13-2 · pf-13-2: prop-13-1, thm-10-8 · pf-13-3: thm-11-5, thm-11-1, prop-11-3, prop-13-1 · pf-13-5: def-13-5, def-13-2
pf-14-1: def-14-3, thm-10-7, thm-10-8 · pf-14-2: thm-14-1 · pf-14-3: thm-9-2, thm-9-3 · pf-14-4: prop-14-3 · pf-14-6: thm-14-1, thm-3-3 · pf-14-7: thm-14-1, prop-14-6, thm-10-1, thm-10-3, lem-9-7 · pf-14-8: thm-14-7 · pf-14-9: ex-14-4, thm-14-7, cor-14-2, lem-10-4 · pf-14-10: ex-14-4, thm-14-7, cor-14-2, ex-9-4
pf-15-1: thm-14-1 · pf-15-2: cor-14-2, thm-14-7 · pf-15-3: thm-10-1, thm-10-3
pf-17-1: def-17-1, def-7-2 · pf-17-2: thm-3-3 · pf-17-3: thm-9-3, thm-9-4, cor-9-6, def-17-1 · pf-17-4: def-17-1 · pf-17-5: thm-17-2, thm-17-3 · pf-17-6: thm-4-7, def-17-1
pf-18-1: thm-11-5, prop-9-5, thm-9-1, def-4-4, thm-8-1, thm-7-1 · pf-18-2: thm-17-3 · pf-18-3: def-4-4, prop-4-3, prop-9-5 · pf-18-4: thm-18-3 · pf-18-5: thm-18-1, thm-18-3 · pf-18-6: cor-18-4 · pf-18-7: thm-18-3 · pf-18-8: thm-18-3, cor-18-4 · pf-18-9: cor-18-5, thm-18-3, thm-11-5, thm-7-1, prop-9-5
pf-19-1: thm-11-5, prop-9-5, thm-3-3 · pf-19-2: thm-19-1 · pf-19-3: def-19-1, def-10-4 · pf-19-4: thm-11-5, thm-10-7, thm-19-3, thm-10-8, thm-9-1 · pf-19-5: thm-29-3 · pf-19-6: thm-3-3
pf-20-1: def-20-1, def-17-1 · pf-20-2: rem-20-1
pf-22-1: cor-18-5, rem-17-4
pf-23-2: thm-14-10
pf-24-1: def-24-2 · pf-24-2: def-24-2, thm-17-1, thm-3-3 · pf-24-3: def-24-2, thm-3-3
pf-25-1: def-24-2, thm-33-3, thm-33-4 · pf-25-2: thm-17-3, thm-24-2 · pf-25-3: thm-14-7, thm-14-1, thm-24-1
pf-26-1: thm-23-2, thm-25-3 · pf-26-2: thm-26-1, thm-25-2 · pf-26-3: thm-25-1 · pf-26-4: thm-26-3, thm-26-1, cor-26-2, thm-23-2, ex-9-4, thm-34-4
pf-28-1: rem-20-2 · pf-28-2: rem-20-2, thm-28-1 · pf-28-3: thm-28-1 · pf-28-3-2: thm-28-1, thm-20-1, thm-17-4 · pf-28-4: thm-28-1, thm-20-2
pf-29-1: def-28-1, thm-20-2, prop-9-5 · pf-29-2: thm-18-1, thm-29-1 · pf-29-3: thm-29-2 · pf-29-4: thm-29-3 · pf-29-5: cor-29-4 · pf-29-6: cor-29-4, cor-29-5 · pf-29-7: thm-29-3 · pf-29-8: thm-29-3 · pf-29-9: thm-18-1, thm-29-1 · pf-29-10: thm-18-9, thm-18-3, thm-9-4, def-20-1
pf-30-2: thm-29-2 · pf-30-1: thm-30-2, thm-29-2, prop-9-5
pf-31-2: thm-29-2
pf-32-3: lem-32-2 · pf-32-1: lem-32-3 · pf-32-4: lem-32-2, thm-32-1, prop-4-3 · pf-32-5: thm-32-1, thm-8-1 · pf-32-7: thm-19-1, thm-32-4
pf-33-1: thm-32-4 · pf-33-2: thm-32-4, lem-32-2 · pf-33-3: thm-33-2 · pf-33-4: thm-32-4, thm-3-3, thm-33-3, thm-33-2 · pf-33-5: thm-32-4 · pf-33-6: thm-32-4, lem-32-2 · pf-33-7: thm-33-3, thm-33-5, thm-17-1 · pf-33-8: thm-33-7 · pf-33-9: thm-18-1, thm-33-3, thm-18-3 · pf-33-10: thm-18-1, thm-33-3, thm-33-7, thm-18-3 · pf-33-11: thm-33-10, thm-18-1, thm-18-3, thm-33-7, thm-33-2 · pf-33-12: thm-24-2, thm-32-7, thm-33-2, thm-33-4, thm-33-3
pf-34-1: thm-32-4, thm-29-3 · pf-34-2: thm-32-4, thm-33-2 · pf-34-3: lem-34-2, thm-34-1, thm-28-2, thm-32-7 · pf-34-4: thm-33-3, thm-33-4, thm-33-5, thm-17-1
pf-36-1: def-36-3 · pf-36-2: thm-36-1, def-36-3
```

## Flagged for the author (not edited)
- [[Squeeze Theorem]] lists Proposition §29.8 under Used in, but its proof only bounds $f'(c)$ between $m$ and $M$ (no limit is taken). Probably spurious; not removed.
- [[Mean Value Theorem]] lists Theorem §30.2 under Used in; its proof uses Rolle's theorem (§29.2), not the MVT. [[Completeness Axiom]] lists Theorem §13.2 (uses it only through Theorem §10.8) and Proposition §6.5 (stated without proof). Left, since removing hub entries is a judgement call.
- Results stated without proof: [[§32 The Definition of the Riemann Integral]] Thm. §32.6; [[§6 Dedekind Cuts]] Prop. §6.2, §6.5; [[§13 Some Topological Concepts in Metric Spaces]] Prop. §13.6; Thm. §23.1 in [[§23 Power Series]]. They appear deliberate (exercises or deferred).

## Placeholder proofs still open
None found ("to be proved later" in §2 refers to the uncountability of ℝ, not to a missing proof).

## Requests outside my scope
- Functional Analysis: Prop. §11.7 cites the Weierstrass approximation theorem; it could link [[§27 Weierstrass's Approximation Theorem (Not Covered)]] once rem-27-1 is applied.
- Logic and Proofs, Measure Theory: the uncountability of ℝ (250 Thm. §14.12, 551 Ex. §4.2) could point back to §2 of these notes.

## Checks run
- Frontmatter: 37/37 sections lack `type: section` (proposed). Nav lines, block IDs on every callout, numbering continuity: no problems.
- *Uses:* lines: 0 of 158 proofs (proposed list covers 150). Hubs vs proposed *Uses:* lines: 10 hubs compared; differences listed under Hubs and Flagged.
- Transitive dependents of Prop. §4.3 recomputed: 40 theorem-level results (52 blocks), matching the chapter note.
- `$` balance and callout syntax in every file with a proposed edit: clean. links.py: no unresolved link or block ref in Single Variable Analysis (its "labels containing [ ]" notice for [[Extreme Value Theorem]] and [[Fundamental Theorem of Calculus]] is about Functional Analysis block titles like "C[a,b]" and renders correctly).
