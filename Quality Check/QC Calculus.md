---
type: quality-check
subject: "[[Calculus]]"
date: 2026-10-04
tags: [quality-check]
---
# Quality check: Calculus
↑ [[Quality Check 2026-10-04]]

## Summary
Calculus (158 notes: home, 17 chapter notes, 121 section notes, 19 hubs) is in very good shape. The mechanical checks were scripted: frontmatter, nav lines, Sources lines, block labels against IDs, numbering, *Uses:* lines, hubs against sections, `$` balance, cycles in the *Uses:* graph, and every link into another subject. They found almost nothing wrong. Every section was read at least at skim level. About 30 sections were read in depth: all of Chapters 1–3, the proofs in §8–§19 and §26–§28, §44, §47 and §50. All 82 worked examples taken from the MATH 233 exams and reviews were also read in depth, with the computations re-checked by hand and with sympy/numpy. One statement was imprecise and has been corrected: in §10, Example §10.5 cited the I/D Test where the derivative vanishes at a point. The other changes are three missing "Rigorous treatment" links in hubs, hub wording that only made sense inside the section note, one duplicated heading, the home note's wording, eight added links to Math hubs and blocks, and a cross-link between two notes that solve the same exam problem.

## Edits made
### Correctness
- [[§10 Continuity]], Example §10.5 (last paragraph). Old text: "(It is the only real root: $f'(x) = 12x^2 - 12x + 3 = 3(2x - 1)^2 \ge 0$, so $f$ is increasing; see Theorem §27.1.)". Theorem §27.1 needs $f' > 0$, but here $f'(\tfrac12) = 0$. The new text says $f' > 0$ except at $\tfrac12$ and gives the exact form $f(x) = \tfrac12(2x - 1)^3 - \tfrac32$, which shows $f$ is increasing on $\mathbb{R}$, and the exact root $\tfrac12(1 + \sqrt[3]{3}) \approx 1.2211$. Both were verified with sympy.

### Structure
- [[· 16 Vector Calculus]]: the headings "## Summary of the fundamental theorems" and "## Summary: The Fundamental Theorems" stood back to back. They are merged under the first, which matches the sentence-case style of the other chapter headings. No content was removed, and neither heading was linked from anywhere.
- [[Calculus]]: the diagram legend said "Dashed arrows to the Math subjects", and the "Rigorous treatment" line said "to each Math subject". Both lists include Applied Math subjects (ODE, Complex Variables, ALA, Fourier), so they now read "Math and Applied Math".

### Hubs
- [[Integration by Parts]]: added "Rigorous treatment: 451 Thm. §34.3". It is the definite form (Theorem §44.2) and has weaker hypotheses. Copied from the section's Connections.
- [[Rolle's Theorem]]: added "Rigorous treatment: 451 Thm. §29.2", same route via 451 Thm. §29.1, leading to 451 Thm. §29.3 and the [[Mean Value Theorem]] hub. Checked against the 451 proof.
- [[Quotient Rule]]: added "Rigorous treatment: 451 Thm. §28.2", which states the quotient rule and says it is proved in the same way.
- [[Chain Rule]]: "the tempting argument (3)" now points to Equation (3) of Remark: Why It Works in §17, with a link. "which is $f'(b) + \varepsilon_2$ here" now links the proof of Theorem §17.2.
- [[Alternating Series Test]], [[Taylor's Inequality]]: the references to Theorem §73.2 and Theorem §78.3 were plain text and are now links.
- [[Arc Length Formula]]: "Here $x$ itself is the parameter" now names and links the proof of Theorem §52.1.
- [[Derivative of an Inverse Function]]: the hub's "Its proof uses" listed Def. §12.3, but the proof's *Uses:* line did not. The proof does cite Definition §12.3 explicitly, so Def. §12.3 was added to the *Uses:* line in [[§19 Derivatives of Logarithmic and Inverse Trigonometric Functions]]. The hub was already right. The link was already inside the proof callout, so the computed chapter counts should not change.
- All 19 hubs were checked against their sections after these edits. "Its proof uses" now agrees with the *Uses:* lines in every hub. "Used in (Calculus)" matches the proofs that cite the result, plus examples that link it inline. Every hub whose section has a rigorous-treatment link now carries it.

### Connections
- [[§69 Sequences]]: added a Connections callout after Theorem §69.4 (Squeeze Theorem for Sequences). It links 451 Thm. §8.1 (same proof), the [[Squeeze Theorem]] hub and Theorem §8.7. 451 already links back. The 451 Monotone Convergence link after Theorem §69.9 now also names the [[Monotone Convergence Theorem]] hub.
- [[§36 The Fundamental Theorem of Calculus]]: both Connections callouts (FTC 1 and FTC 2) now name the [[Fundamental Theorem of Calculus]] hub.
- [[§96 Maximum and Minimum Values]]: the 452 Thm. §14.4 link now names the [[Second Derivative Test in Several Variables]] hub.
- [[§44 Integration by Parts]]: the 452 Thm. §17.2 link now names the [[Green's First Identity]] hub.
- [[§44 Integration by Parts]] and [[§109 The Fundamental Theorem for Line Integrals]]: Example §44.5 and Example §109.5(b) evaluate the same work integral from the same exam problem, by different routes. Each now links the other.

### Writing / consistency
- [[§51 Improper Integrals]]: the link label "551 Rem. §15.1" pointed to an unnumbered remark. It now reads "551 Remark: Characterization of Integrability", the vault's style for remarks.
- Sources lines in [[§44 Integration by Parts]], [[§45 Trigonometric Integrals]], [[§108 Line Integrals]], [[§110 Green's Theorem]] and [[§114 Stokes' Theorem]] wrote question parts as "Q6b". They now read "Q6(b)", as in the other 31 MATH 233 Sources lines and all in-body *Source:* lines.

## Flagged for the author (not edited)
- [[§101 Applications of Double Integrals]] says its section "was not on the course syllabus". The Course record in [[Calculus]] lists Exam 2 as "14.7, 14.8, 15.1–15.8", which includes 15.4 (§101). The range may be shorthand. It was not changed because the course facts cannot be verified here.
- The same exam problem is cited two ways: "233 Practice Final Set 2, Q3(b)" in [[§44 Integration by Parts]] (Example §44.5) and "233 Practice Final Set 2, Part II Q3" in [[§109 The Fundamental Theorem for Line Integrals]] (Example §109.5). One label is probably incomplete, but the source documents are not available to check which.
- [[§28 Indeterminate Forms and L'Hospital's Rule]]: the note itself says that the $\frac{\infty}{\infty}$ case of l'Hospital's Rule is proved neither in Stewart nor anywhere in the vault. 451 Thm. §30.1 states it but proves only $\frac00$. This is a known gap for the author to decide on. The proofs were not written.
- Hub aliases: Calculus uses "Calc 8.1", while [[Applied Linear Algebra]] uses "MATH 235 20.1". This is logged only, and existing aliases were left alone.
- There is no `Examples/` folder, although README and Home describe one per subject. Candidate recurring examples, each already reused by cross-links:
  - the CN Tower falling ball: Examples §2.3, §6.3, §12.2;
  - the helix $\langle \cos t, \sin t, t\rangle$: §86, §87, §88;
  - the folium of Descartes: Example §18.2, Example §94.5;
  - $x^3 - x$: §13, §26 and others;
  - the field $e^y\sin x\,\mathbf i + e^y\cos x\,\mathbf j$: Example §44.5, Example §109.5.

  No Example notes were created. Embedding hubs would add little to the cross-links that already exist, and new notes would make README's note count stale, which is outside this scope.
- The *Uses:* graph has one formal cycle at block level. Theorem §8.1 (Law 3 uses Law 8) cites Theorem §8.2. Theorem §8.2 (Law 7) cites Corollary §10.8, which leads through Theorems §10.6, §10.2 and §10.1 back to Theorem §8.1. This is not a logical circle: Law 8 is proved directly, and [[§8 Calculating Limits Using the Limit Laws]] explains this for Law 11. Splitting Theorem §8.2 into Laws 8–10 and Law 7 would remove the cycle. Not edited.
- Chapter "Builds on / Used by (N)" counts: a reconstruction that counts block-to-block links inside callouts plus *Uses:* lines reproduces most counts exactly, for example 3←2 = 42, 1←2 = 3, 4←3 = 19 and 7←16 = 3. It differs by one or two in some others, for example 2←1 gives 10 against the stored 9. The original counting rule is not known exactly, so no count was changed. The counts in [[Calculus]] (the Mermaid edge labels and the "Rigorous treatment" totals) agree exactly with the chapter notes' "Developed further in" lines.
- Main results with no rigorous counterpart anywhere in Math/, so no link can be added:
  - the Limit Comparison Test (Theorem §72.2);
  - the rearrangement theorem (Theorem §73.4);
  - the error bounds for the Trapezoidal, Midpoint and Simpson's Rules (§50).

## Placeholder proofs still open
None. A grep for "to be proved", "to be filled", "next lecture", "to be added", "TODO", "homework" and similar found nothing. All 392 proof callouts have content. The 10 folded proofs are complete proofs folded for length, in §8, §10, §16, §41, §48, §49, §85, §88, §89 and §119.

## Requests outside my scope
- 95 links from Calculus section notes into Math/ blocks have no link back from the target note. They are listed in the scratch file `qc-calculus/nonreciprocal_math_links.txt`. Most are side remarks and need no reciprocal link. Ones the SVA and MVA owners might want, as "Computational version" lines:
  - 451 §31 Taylor's Theorem ← [[§23 Linear Approximations and Differentials]];
  - 452 §6 Differentiability ← [[§17 The Chain Rule]] and [[§23 Linear Approximations and Differentials]];
  - 452 §15 Multivariable Integration ← [[§110 Green's Theorem]];
  - 551 §18 Differentiation Theory ← [[§36 The Fundamental Theorem of Calculus]].
- README says "Course codes refer to courses at the University of Michigan unless marked otherwise". Calculus is marked "(UMass)" in README, so this is consistent and no change is needed. It is noted here only because Calculus.md's alias "Calculus III" covers just Chapters 12–16.

## Checks run
- Frontmatter of all 121 section notes has the same keys (type, subject, chapter, section, stewart, aliases, tags). Each `stewart` value matches its "Stewart X.Y" alias, its `section` value and its Sources line.
- All 121 nav lines (`← · ↑ · →`) point to the correct previous section, next section and chapter note.
- Sources lines: 71 plain, 41 that mention MATH 233 (36 of them cite exam questions), 6 Appendix, and 3 that cite proofs from Appendix F (121 in all).
- 1,357 numbered callouts (553 examples, 371 definitions, 326 theorems, 63 propositions, 37 corollaries, 7 lemmas), plus 266 remarks with IDs. Every label matches its block ID, and numbering is continuous in every section. Proof IDs all match a block in the same note.
- All 392 proofs are followed by a *Uses:* line, and no *Uses:* line stands anywhere else.
- References written as "Theorem/Definition/Example §a.b", linked or plain, all name an existing block of the right kind.
- 643 block links from Calculus into other subjects (250 SVA, 209 MVA, 71 ODE, 58 Complex Variables, 51 ALA, 38 LADR, 37 Fourier/PDE, 28 Logic and Proofs, 22 Measure Theory, 15 Topology, 4 Manifolds) were checked: type and number in each label match the target header. The context of all 643 was read to confirm each lands on the claimed result.
- The 19 hubs were checked against their sections (embed, Treated in, Its proof uses, Used in, Connections). The Central results lists in [[Calculus]] and in the chapter notes match the hub set.
- The Mermaid edge labels and the "Rigorous treatment" counts in [[Calculus]] were recomputed from the chapter notes and match exactly.
- `$`/`$$` balance and callout syntax were checked in every file, including all edited files after editing. There are no duplicate headings left.
- The *Uses:* graph was checked for cycles: one formal cycle, explained above.
- The numbers were recomputed in about 60 worked examples, all correct: the CO₂ model, falling ball, exponential models, related rates, Midpoint/Trapezoid tables, partial fractions (sympy `apart`), Lotka–Volterra peaks and period (RK4), cross products, determinants, distances, and the multiple, line and surface integrals in Chapters 12–16.
- `links.py`: no unresolved links or block references in any Calculus file or in this log.
