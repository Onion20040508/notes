---
type: quality-check
subject: "[[Complex Variables]]"
date: 2026-10-04
tags: [quality-check]
---
# Quality check: Complex Variables
↑ [[Quality Check 2026-10-04]]

## Summary
Complex Variables (180 notes: 140 sections, 12 chapter notes, 27 hubs, home note) is in very good shape: frontmatter, nav lines, `B&C` header lines, block IDs, numbering and `*Uses:*` lines were consistent throughout. No mathematical errors turned up. I read §1–§37 and §93 in depth, skimmed §38–§49 with spot checks, and skimmed the structure and opening paragraphs of every other section. About 40 stated numerical values were checked with sympy/mpmath (residue integrals in §85–§92, §46–§47 bounds, derivatives in §20). The main problems were in the hubs. The [[Cauchy–Riemann Equations]] hub ended mid-sentence, two "Its proof uses" lists contained items that are only "compare" references, cross-subject proof dependencies were missing, and several hubs carried section-relative wording. I also linked 64 unlinked cross-section references, replaced Brown–Churchill numbering ("Theorem 1") with vault numbering where it could be confused, added four missing `*Uses:*` lines and added five connection items (Topology, Fourier Series and PDEs, Multivariable Analysis).

## Edits made

### Hubs
- [[Cauchy–Riemann Equations]]: the Connections bullet stopped at "with Jacobian matrix ([[§13 The Inverse Function Theorem#^def-13-1|452 Def. §13.1]])". Restored the matrix display and the rest of the remark from [[§21 Cauchy–Riemann Equations]]: rotation–scaling matrix, the converse in §23, and [[§6 Differentiability#^thm-6-2|452 Thm. §6.2]]. Added a link to the §23 theorem and its hub. The source's "Used in Electromagnetism" bullet was left out to match every other hub in the vault.
- "Its proof uses" brought into line with the proof's `*Uses:*` line (both items had been taken from "compare" remarks inside the proof, not from what it uses):
  - [[Antiderivatives and Independence of Path (complex)]]: removed [[§45 Some Examples (Contour Integrals)#^ex-45-2|Example §45.2]] (the proof only says "Compare").
  - [[Maximum Modulus Principle]]: removed [[§28★ Uniquely Determined Analytic Functions#^lem-28-1|Lemma §28.1]] (the proof only says "the approach is similar").
- Added the standard section "Its proof uses (other subjects)" from the proofs' `*Uses:*` lines in six hubs:
  - [[Cauchy–Riemann Equations]] (452 §4.1)
  - [[Analytic Functions Have Harmonic Components]] (452 §5.1)
  - [[Bromwich Inversion Formula]] (341 §14.1, §15.2 def., §15.2 thm.)
  - [[Laurent's Theorem]] (Calc §96.3)
  - [[ML-Inequality]] (451 §33.7)
  - [[Sufficient Conditions for Complex Differentiability]] (451 §29.3)
- Section-relative wording in hub Connections replaced by links to the actual block:
  - [[Jordan's Lemma]]: "Example §88.1 below" now links [[§88★ Jordan's Lemma#^ex-88-1|Example §88.1]].
  - [[Sufficient Conditions for Complex Differentiability]]: "Step 1 … the proof above … Equations (2)–(3)" now refers to the linked proof of Theorem §23.1.
  - [[Cauchy Integral Formula for Derivatives]]: "Steps 4–5" now refers to the linked proof of Theorem §56.1.
  - [[Cauchy Integral Formula]]: "formula (1)" now reads "formula (1) of Theorem §54.1" (linked).
  - [[Cauchy–Goursat Theorem]]: "Lemma §51.1" linked.
  - [[Analytic Functions Have Harmonic Components]]: "Example §27.1" linked.
  - [[Laurent's Theorem]]: "the first step" now refers to the linked proof.
  - [[Taylor's Theorem for Analytic Functions]]: "the proof" linked.
- [[Rouché's Theorem]]: added the Topology connection (see Connections below), kept in step with the new remark in §94.
- [[Cauchy's Residue Theorem]]: Green's-theorem citation made precise (see Correctness).

### Correctness (citations)
- [[§76 Cauchy's Residue Theorem]] and its hub: the old text was "the complex form of Green's theorem for a region with holes, [[§16 Line Integrals and Green's Theorem#^thm-16-1|452 Thm. §16.1]]". That theorem is stated for a region bounded by one simple closed curve. The text now cites [[§110 Green's Theorem#^thm-110-4|Calc Thm. §110.4]] for regions with holes and notes that 452 Thm. §16.1 extends to them by the same cutting.

### Connections
- [[§94 Rouché's Theorem]]: new Connections remark after the proof. Rouché's theorem is the homotopy invariance of the winding number: $f + tg$ does not vanish on $C$. Step 3 of the topological proof of the fundamental theorem of algebra ([[§25 The Fundamental Theorem of Algebra#^thm-25-1|590 Thm. §25.1]]) is this same homotopy; links to [[Fundamental Group of the Circle]].
- [[§59 Maximum Modulus Principle]]: new Connections remark after Corollary §59.5. It links the maximum principle for harmonic functions [[§39 Potential in a Disk#^thm-39-5|341 Thm. §39.5]] and [[§39 Potential in a Disk#^cor-39-6|341 Cor. §39.6]], and [[§115★ Harmonic Conjugates#^thm-115-4|Theorem §115.4]]. This is the reciprocal of the existing link from Fourier Series and PDEs.
- [[§53 Multiply Connected Domains]]: added the rigorous [[§16 Line Integrals and Green's Theorem#^thm-16-1|452 Thm. §16.1]] next to the Calculus Green's theorem for regions with holes.
- I checked every cross-subject link (≈570): each label's kind and number agree with the target block. The connections named in the task are present and land correctly:
  - Topology: argument principle, winding numbers, covering spaces for log z, simply connected domains, compactness.
  - Multivariable Analysis: Green's theorem for Cauchy's theorem, Jacobians, mixed partials.
  - Fourier Series and PDEs: harmonic functions, Poisson integral, mean value property, Laplace transforms.
  - Calculus.

### Structure
- Added the four missing `*Uses:*` lines:
  - [[§58 Liouville's Theorem and the Fundamental Theorem of Algebra]] (proof of Lemma §58.3)
  - [[§88★ Jordan's Lemma]] (proof of Lemma §88.1, concavity test)
  - [[§98★ Mappings by 1∕z]] (proofs of Propositions §98.1 and §98.2)

### Writing and consistency
- Brown–Churchill numbering in running text replaced by vault numbering with links:
  - [[§82 Zeros of Analytic Functions]] intro: "(Theorem 1/2/3)".
  - [[§83 Zeros and Poles]] intro "(Theorem 1), and conversely … (Theorem 2)": now links Theorem §83.1, Proposition §83.3 and Theorem §83.2.
  - [[§83 Zeros and Poles]] proofs: "Theorem 1 of §82" and "Theorem 1 in §82".
- [[§57 Some Consequences of the Extension]]: Example §57.1 title "No Real Analogue of Theorem 1" changed to "… of Theorem §57.1". No link uses this title.
- [[§64 Examples (Proof of Taylor's Theorem)]]: in the proof of Proposition §64.1, "(Example 2.)" … "(Example 6.)" changed to "(B&C's Example n.)", matching "(B&C's Example 1 …)" and avoiding confusion with Examples §64.n.
- [[§30 The Exponential Function]] and [[§37 The Trigonometric Functions sin z and cos z]]: an own-subject link labelled "342 Prop. §64.1" relabelled "Proposition §64.1".

### Navigation
- Linked 64 plain-text references of the form "Theorem §N.k" / "Example §N.k" that point to another section. No wording was changed. Notes involved:
  - Chapters 1–3: [[§6 Complex Conjugates]], [[§11 Examples (Roots of Complex Numbers)]], [[§16 Theorems on Limits]], [[§17 Limits Involving the Point at Infinity]], [[§20 Rules for Differentiation]], [[§25 Analytic Functions]], [[§26 Further Examples (Analytic Functions)]], [[§28★ Uniquely Determined Analytic Functions]], [[§30 The Exponential Function]], [[§35 The Power Function]], [[§36 Examples (The Power Function)]], [[§37 The Trigonometric Functions sin z and cos z]], [[§39★ Hyperbolic Functions]]
  - Chapters 4–5: [[§42 Definite Integrals of Functions w(t)]], [[§44 Contour Integrals]], [[§45 Some Examples (Contour Integrals)]], [[§49 Proof of the Theorem (Antiderivatives)]], [[§50 Cauchy–Goursat Theorem]], [[§57 Some Consequences of the Extension]], [[§59 Maximum Modulus Principle]], [[§62 Taylor Series]], [[§67 Proof of Laurent's Theorem]], [[§69★ Absolute and Uniform Convergence of Power Series]], [[§70★ Continuity of Sums of Power Series]], [[§72★ Uniqueness of Series Representations]], [[§73★ Multiplication and Division of Power Series]]
  - Chapters 6–8: [[§81 Examples (Residues at Poles)]], [[§83 Zeros and Poles]], [[§86 Example (Evaluation of Improper Integrals)]], [[§87 Improper Integrals from Fourier Analysis]], [[§88★ Jordan's Lemma]], [[§89★ An Indented Path]], [[§101★ Mappings of the Upper Half Plane]], [[§102★ Examples (Mappings of the Upper Half Plane)]], [[§111★ Surfaces for Related Functions]]
  - Chapters 9–12: [[§117★ Transformations of Boundary Conditions]], [[§119★ Steady Temperatures in a Half Plane]], [[§120★ A Related Problem (Steady Temperatures in a Half Plane)]], [[§121★ Temperatures in a Quadrant]], [[§122★ Electrostatic Potential]], [[§128★ Schwarz–Christoffel Transformation]], [[§133★ Electrostatic Potential about an Edge of a Conducting Plate]], [[§135★ Dirichlet Problem for a Disk]], [[§137★ Related Boundary Value Problems]]

- Coordinator follow-up: the two entries removed from "Its proof uses" lists ([[Antiderivatives and Independence of Path (complex)]]: Ex. §45.2; [[Maximum Modulus Principle]]: Lemma §28.1) were re-added to each hub's Connections as "Compare" pointers, so no hub loses a link.

## Flagged for the author (not edited)
- Hub Connections omit the source remarks' "Used in Electromagnetism" bullets: [[Analytic Functions Have Harmonic Components]], [[Conformal Mappings Preserve Angles]], [[Schwarz–Christoffel Transformation]], [[Cauchy–Riemann Equations]]. No hub anywhere in the vault carries such bullets, so I took this as the generator's policy and did not add them.
- Seven hubs have only the line `See [[§N]] for context and examples.` under Connections, because their theorem has no Connections remark in the section: [[Casorati–Weierstrass Theorem]], [[Harmonic Functions Under Conformal Maps]], [[Linear Fractional Transformation Through Three Points]], [[Liouville's Theorem]], [[Morera's Theorem]], [[Principle of Deformation of Paths]], [[Schwarz–Christoffel Transformation]]. They could be enriched; for example, Harmonic Functions Under Conformal Maps could link [[§35 Potential Equation#^thm-35-3|341 Thm. §35.3]], as §116 does. Judgement call.
- Hub "Used in (Complex Variables)" lists include examples that cite the result only in their text (examples carry no `*Uses:*` lines). Theorem-level entries agree exactly with the `*Uses:*` lines. I left the generator's convention unchanged.
- Computed counts are now slightly stale, because the added `*Uses:*` lines and Connections links (Topology, Fourier Series and PDEs, Multivariable Analysis, Calculus) postdate the generator. This affects the chapter-note "Builds on / Used by / Developed further in (N)" counts, the "N later results" counts and the counts in the home note's "Rigorous treatment" line and Mermaid labels. I could not reproduce the generator's counting rule exactly (counting from `*Uses:*` lines alone gives different numbers), so I did not change them.
- [[§88★ Jordan's Lemma]]: the new `*Uses:*` line cites [[§27 What Derivatives Tell Us About the Shape of a Graph#^thm-27-3|Calc Thm. §27.3]]. The proof uses "concave down implies above the chord", whereas Calculus defines concavity through tangents. No vault note states the chord form. Judgement call.

## Placeholder proofs still open
- None. No `[To be proved.]`, "to be filled" or homework placeholders occur. Six results deliberately have no proof, each stating why ("B&C omits the proof"):
  - [[§43 Contours#^thm-43-4|Jordan curve theorem]]
  - [[§79 Examples (The Three Types of Isolated Singular Points)#^thm-79-1|Picard's theorem]]
  - [[§28★ Uniquely Determined Analytic Functions#^thm-28-3|coincidence principle]] (sketched from §82.2)
  - [[§115★ Harmonic Conjugates#^lem-115-3|Lemma §115.3]] (pointer to Calculus)
  - [[§122★ Electrostatic Potential#^prop-122-1|Proposition §122.1]] and [[§124★ Two-Dimensional Fluid Flow#^prop-124-3|Bernoulli's equation]] (physics)

## Requests outside my scope
- Fourier Series and PDEs hub [[Mean Value Property of Harmonic Functions]]: the wording "proof of (b) above" (about l.21) is section-relative and should point at the linked proof. That folder is not mine.
- Topology, [[§25 The Fundamental Theorem of Algebra]] Connections and the [[Fundamental Group of the Circle]] hub: optionally add a reciprocal pointer to [[§94 Rouché's Theorem#^thm-94-1|342 Thm. §94.1]] (the homotopy behind Step 3 is Rouché's theorem). Both currently link only Example §94.2 and Theorem §93.4.
- Home note counts: see the computed-counts item above.

## Checks run
- Frontmatter keys: 140 sections, 27 hubs, 12 chapter notes, home note; all consistent by type.
- Nav lines `← · ↑ · →` against section order: 140/140 correct. `*Brown–Churchill, Section N*` header present in 140/140.
- Callouts: 1366 checked. Every non-Connections callout has a block ID, the ID prefix matches the callout kind, and the label number matches the ID. Numbering is continuous per section (theorem-type items share one counter; definitions, examples and remarks have their own). No empty callouts, duplicate IDs or duplicate headings.
- `*Uses:*` after every proof: 283/287 before this pass, 287/287 after. No placeholder text.
- Links:
  - Within-subject links whose label disagrees with the target ID: 0.
  - Heading links that do not resolve: 0.
  - Cross-subject links (≈570): kind and number agree with the target block.
  - Unlinked other-section references: 64 found, all linked.
- Hubs (27): embed resolves; "Treated in" titles match; "Its proof uses" now equals the `*Uses:*` line (2 fixed, 6 other-subject sections added); "Used in" theorem-level entries equal the citing `*Uses:*` lines; Connections compared with the source remark (1 truncation fixed); scanned for "below/above/Step/(N)".
- Chapter notes (12): section lists match the folders; central-result lists and numbers match the hubs and the home note.
- Text: inline `$` and `**` balanced on every line; `$$` balanced in every file; callout syntax rechecked in all 66 changed files.
- Numerical verification (sympy/mpmath), all agreeing with the notes: §6.4 maximum, §20.4 derivatives, §40.3, §42.3, §46.3–§46.4, §47.1/§47.3/§47.4/§47.5, §85.2–§85.3, §86.4, §87.4, §88.1–§88.2, §89.2, §90.1 (three values of a), §91.3, §92.2–§92.5. Residues in §95.3 checked by hand.
- `links.py`: no unresolved links or block references in Complex Variables or in this log.
