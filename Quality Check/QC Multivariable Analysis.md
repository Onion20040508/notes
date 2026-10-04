---
type: quality-check
subject: "[[Multivariable Analysis]]"
date: 2026-10-04
tags: [quality-check]
---
# Quality check: Multivariable Analysis
↑ [[Quality Check 2026-10-04]]

> [!note] Record only
> None of the changes in this log were applied: every note is exactly as it was before the check. Each change below is a **proposal**. The exact text of every proposed change is saved in `Quality Check/proposed-edits.patch` (see [[Quality Check 2026-10-04]]); the edits were also captured in the checkpoint commit `c48deba` before being reverted.

## Summary
Multivariable Analysis (home note, 7 chapter notes, 23 section notes, 20 hubs, examples) is in good shape: nav lines, frontmatter, block IDs, numbering and *Uses:* lines (61 proofs, 71 *Uses:* lines) are all consistent, and links.py finds no unresolved link in the subject. Every section was skimmed and the proofs of §3–§6, §9–§10, §12–§13, §15, §17–§18 and §22 were read in depth. The one real inconsistency in the dependency record is that the proof of the [[Divergence Theorem in ℝⁿ]] (§17) uses the graph area element of [[Surface Area via the Gram Matrix|§18.1]] before it is proved, which the *Uses:* line, the hub and the home diagram did not show. One example was wrong (§18, simple domains), one proof sentence in §15 was garbled, one estimate in §4 was stated loosely, and four hub citations of Differentiable Manifolds pointed at old section numbers. The rest of the proposals are navigation (heading levels in §15–§17), links, and short clarifying remarks.

## Proposed edits (not applied)
### Correctness
- [[§18 Surface Integrals]], rem-18-8 (simple domains). Old text: "- Convex domains (balls, ellipsoids, tetrahedra) are automatically simple. / - Many non-convex domains are also simple: a hemisphere, a solid cone, any region bounded above and below by graphs." A solid hemisphere and a solid cone are convex, and a region between two graphs is only guaranteed to be simple in the $z$-direction. New text: "- Convex domains (balls, ellipsoids, tetrahedra, a solid hemisphere, a solid cone) are automatically simple. / - Simplicity is weaker than convexity: the L-shaped block $\big([0,2]\times[0,1] \cup [0,1]\times[0,2]\big) \times [0,1]$ is not convex, yet every line parallel to a coordinate axis meets it in a single interval. A region bounded above and below by graphs satisfies the condition in the $z$-direction; the $x$- and $y$-directions must be checked separately."
- [[§15 Multivariable Integration]], proof of Theorem §15.1. Old text: "Choose the center $\mathbf{x}$ of $S$. Since $S$ is contained in the interior of itself, $\mathbf{x}$ is an interior point of both $D$ and $E$." New: "The center $\mathbf{x}$ of $S$ is an interior point of $S$, hence of both $D$ and $E$ (since $S \subseteq D$ and $S \subseteq E$)."
- [[§4 Partial Derivatives]], proof of Theorem §4.1, final estimate. Old: "$|f(x_0 + h, y_0 + k) - f(x_0, y_0)| \leq 2M \cdot \delta \leq \varepsilon$". New: "$\leq 2M\sqrt{h^2 + k^2} < 2M \cdot \delta \leq \varepsilon$" (the intermediate step was missing; the bound uses $|h|, |k| \le \sqrt{h^2+k^2} < \delta$).
- [[§17 The Divergence Theorem in Higher Dimensions and Green's Identities]], *Uses:* line of the proof of Theorem §17.1: add `[[Surface Area via the Gram Matrix|§18.1]]` before the 451 FTC entry. The proof takes $dS = \sqrt{1 + |\nabla h|^2}\,dA$ for a graph from §18.1.
- [[Multivariable Taylor's Theorem]] (Connections): "591 Lemma §12.17" → "591 Lemma §27.2"; [[Multivariable Chain Rule]]: "591 Thm. §12.11" → "591 Thm. §26.6"; [[Implicit Function Theorem]]: "591 Thm. §4.1" → "§7.1" and "591 Thm. §4.3" → "§7.3". The numbers were checked against the linked Differentiable Manifolds hubs.

### Structure
- [[Multivariable Analysis]] (home): add the edge `  C6 -.->|on credit| C5` after `C6 --> C7` in the Mermaid diagram, and extend the caption: "Dashed arrows labelled "on credit": results used before they are proved (the proof of the [[Divergence Theorem in ℝⁿ]] in §17 takes the graph area element from [[Surface Area via the Gram Matrix|§18.1]]). Dashed arrows from other subjects: citations of results from other subjects, …" (rest unchanged). Chapter counts ("Builds on 6 (1)" in Chapter 5, "3 later results" in Chapter 6) already include this edge and need no change.
- [[§15 Multivariable Integration]] (navigability, no split): add a **Contents:** line after the chapter line, linking the six `##` headings (Motivation, Jordan measure, Definition of the Integral, Properties, Fubini's Theorem: Rigorous Treatment, General Change of Variables); add `####` headings "First proof: linear case and Taylor linearization", "Second proof: via the Implicit Function Theorem", "Third proof: two-step decomposition (Courant–John)" before the three proofs of Theorem §15.14; move rem-15-12 and rem-15-13 (Jordan-measurable domains, general domains) under a new "#### Remarks: beyond rectangles" just before "### Extension to General Domains", with "The proof above assumes" → "The three proofs above assume". No block ID or linked heading changes.
- [[§16 Line Integrals and Green's Theorem]]: demote nine `##` sub-headings to `###` (Scalar/Work line integral, Setup and Orientation Convention, Assumption on the Domain, the two "Derivation" headings, Combining the Two Terms, Rewriting the Line Integral as a Flux Integral, Deriving the Divergence Theorem) so the outline shows them under their parent topics. None is linked.
- [[§17 The Divergence Theorem in Higher Dimensions and Green's Identities]]: demote to `###` Green's First/Second Identity, Applications of Green's Identities, Flux and the Continuity Equation, Incompressible Flow, Irrotational Flow, From Potential Functions to Laplace's Equation, Computing Δφ for a Radial Function, Solving the Radial ODE. None is linked.
- [[§10 Composition of Functions and the Chain Rule]]: move the proof of Theorem §10.2 (with `^pf-10-2` and its *Uses:* line) to directly after `^thm-10-2`; it was separated from the statement by other material.

### Writing
- [[§5 Equality of Mixed Partials]], proof of Theorem §5.1: add at "Motivation for $I(h,k)$": "(In this proof $f_{xy}$ means $\partial_x(\partial_y f)$ and $f_{yx}$ means $\partial_y(\partial_x f)$, as in the display below; §8 reads the subscripts in the other order, $f_{xy} = (f_x)_y$. Under the hypotheses of the theorem the two readings agree, which is exactly what is being proved.)"
- [[§15 Multivariable Integration]]: after "Throughout, assume $D$ is bounded and Jordan measurable…" add "In the proofs, $S_{\mathcal{T}}^+(f)$ and $S_{\mathcal{T}}^-(f)$ denote the upper and lower sums $U(f,\mathcal{T})$ and $L(f,\mathcal{T})$ of Def. §15.8." (the notation was used undefined).
- [[§17 The Divergence Theorem in Higher Dimensions and Green's Identities]], rem-17-3: stale "(to be covered if time permits)" → "([[§21 Introduction to Differential Forms|§21]]–[[§23 The Generalized Stokes' Theorem|§23]])".
- [[§22 The Algebra of Differential Forms]]: three link labels "§21.6" → "§21" (§21 has no block 21.6; the link goes to a heading).

### Connections
- [[§1 Sequences and Limits in ℝⁿ]] (thin section): add rem-1-1 "Remark: What MATH 451 already proved about sequences in ℝⁿ": coordinatewise criterion (451 Prop. §13.1), completeness (451 Thm. §13.2), Bolzano–Weierstrass (451 Thm. §13.3), and the [[Heine–Borel Theorem]] (590 Thm. §15.12). All four targets checked.
- [[§15 Multivariable Integration]]: add rem-15-15 "Remark: Scope of Theorem §15.12" after Theorem §15.12 (Tonelli): "measurable" there means Lebesgue measurable, which this course does not define, and the integrals may be $+\infty$; the statement is quoted without proof; precise statements and proofs are Measure Theory Thm. §17.3 ([[Tonelli's Theorem]]) and Thm. §17.6 (Fubini); used in Ex. §15.2 and Ex. §15.7 Step 1.
- [[§21 Introduction to Differential Forms]], rem-21-1: link "551 §15" to [[§15 The General Lebesgue Integral]] and "551 Thm. §15.10" to its block.
- [[§23 The Generalized Stokes' Theorem]], Connections: add "Proof: the course states the theorem without proof, after checking the four classical cases above. A proof for compact oriented manifolds with boundary is in Lee, *Introduction to Smooth Manifolds*, Ch. 16, the textbook of [[Differentiable Manifolds]]." No proof of either theorem exists elsewhere in the vault.

### Hubs
- [[Surface Area via the Gram Matrix]]: Used in "(not cited later in the course)" → "[[§17 The Divergence Theorem in Higher Dimensions and Green's Identities#^thm-17-1|Theorem §17.1: Divergence Theorem in ℝⁿ]] (cited on credit, ahead of §18, for the area element of a graph)".
- [[Generalized Stokes' Theorem]], [[Poincaré Lemma]]: "(no proof in the notes)" expanded to name Lee Ch. 16 / Ch. 17 (via [[Differentiable Manifolds]]) and, for Poincaré, the proved special cases 331 Thm. §9.2 (exactness on a rectangle) and 342 Thm. §115.4 (harmonic conjugates).
- [[Fubini's Theorem]]: add Theorem §15.7 (polar coordinates) to Used in (its proof cites Fubini).

## Flagged for the author (not edited)
- [[§12 The Implicit Function Theorem]], Theorem §12.2 (general IFT) is stated without proof and without the uniqueness clause; the proof of Theorem §13.2 in [[§13 The Inverse Function Theorem]] then only shows a right inverse (the left-inverse half needs uniqueness). Judgement call on how the course states it.
- [[§14 Optimization and Lagrange Multipliers]]: relies on the implicit function theorem for systems, which is not proved in the course.
- [[§15 Multivariable Integration]]: Proposition §15.19 says "measurable" in the Riemann–Jordan setting (probably "Jordan measurable"); the first proof of Theorem §15.14 has a topological gap the notes acknowledge. Not edited: may be deliberate.
- Angle-name conventions (which of θ, φ is polar) differ between [[§15 Multivariable Integration]], [[§18 Surface Integrals]], [[§19 The Laplacian in Spherical Coordinates]] and [[§22 The Algebra of Differential Forms]]. A global change would touch many formulas.
- [[§22 The Algebra of Differential Forms]]: Maxwell's equations written "$d{*}F = J$" with a loose sign/Hodge convention.
- Residual hub "Used in" entries that are examples or unproved propositions (e.g. [[Change of Variables Formula (multiple integrals)]] lists Ex. §15.8 and Ex. §22.4; [[Directional Derivative Formula]] lists Props §22.2, §22.6). They have no *Uses:* line to compare against, so they were left.
- Chapter 1 has no "Central results" section (no hub-level result there); left as is.

## Placeholder proofs still open
None. Results stated without proof (by design): Theorem §12.2, Generalized Stokes (§23), Poincaré lemma (§22), Theorem §15.12.

## Requests outside my scope
- Differentiable Manifolds: when Stokes' theorem on manifolds and the Poincaré lemma are proved there, add links back to [[Generalized Stokes' Theorem]] and [[Poincaré Lemma]], and these hubs' "no proof" lines can then point to them.
- Measure Theory: [[Tonelli's Theorem]] could list MVA Theorem §15.12 as an elementary statement of it.

## Checks run
- Frontmatter, nav lines, block IDs on every theorem/definition/example callout, numbering continuity: 23 sections, no problems.
- *Uses:* lines: 61 proofs, 71 lines; every proof has one. Hub "Its proof uses" vs *Uses:* lines: 20 hubs, all agree except the two no-proof hubs (they list outside sources).
- Link labels vs block IDs: 3 stale labels (§22, fixed in proposal), 4 stale 591 numbers in hubs.
- Chapter "Load-bearing" counts and "Builds on/Used by" counts recomputed from *Uses:* lines: all agree.
- `$` balance and callout syntax in every proposed file: clean. links.py: no unresolved link or block ref in Multivariable Analysis.
