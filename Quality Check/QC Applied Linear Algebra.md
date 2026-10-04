---
type: quality-check
subject: "[[Applied Linear Algebra]]"
date: 2026-10-04
tags: [quality-check]
---
# Quality check: Applied Linear Algebra
↑ [[Quality Check 2026-10-04]]

> [!note] Record only
> None of the changes in this log were applied: every note is exactly as it was before the check. Each change below is a **proposal**. The exact text of every proposed change is saved in `Quality Check/proposed-edits.patch` (see [[Quality Check 2026-10-04]]).

## Summary
I checked all 80 notes: 53 sections, 8 chapter notes, the home note and 18 hubs. Every section note was read, and the proofs and worked computations were read in depth for most of them. Mechanically, the notes are in very good shape: frontmatter, nav lines, block IDs, numbering, *Uses:* lines and all 223 LADR links are consistent. I re-checked every computation I tested, by script or with sympy, and found no mathematical error. The real problems are elsewhere:
- **Stale counts.** The cross-subject counts on the home note and chapter notes leave out ODE, Fourier and Complex Variables.
- **Hubs.** Several hubs lack the rigorous-treatment link that their section has, and three hubs' "Its proof uses" lists disagree with the *Uses:* lines.
- **Citations.** Two citations are mislabelled.
- **Wording.** A few sentences were unclear.

Following the coordinator's later RECORD ONLY instruction, the changes below are proposals, not applied edits. They were made in the working tree before that instruction and are saved as a patch: they appear in commit c48deba plus the uncommitted diff, both against c48deba~1. Each change is described below precisely enough to re-apply.

## Proposed edits (not applied)

### Correctness (citations)
- [[§9 The Matrix of a Linear Transformation]]
  - **Where:** the Connections callout after Theorem §9.2.
  - **Problem:** the two LADR citations were in the wrong order. "$\mathbb{R}^4 \to \mathbb{R}^3$ is never one-to-one" is LADR 3.22 (not injective), and "$\mathbb{R}^2 \to \mathbb{R}^3$ never onto" is LADR 3.24 (not surjective).
  - **Change:** `are [[...#^ladr-3-24|LADR 3.24]] and [[...#^ladr-3-22|LADR 3.22]].` → `are [[§8 Null Spaces and Ranges#^ladr-3-22|LADR 3.22]] and [[§8 Null Spaces and Ranges#^ladr-3-24|LADR 3.24]], respectively.`
- [[§51★ The Singular Value Decomposition]]
  - **Where:** the *Uses:* line of the proof of Theorem §51.4 (line 212).
  - **Problem:** §41.1 is the theorem "orthogonal sets of nonzero vectors are independent", but it was labelled as if it extended an orthonormal set.
  - **Change:** `[[§41 Orthogonal Sets#^thm-41-1|§41.1]] (extending an orthonormal set)` → `[[§41 Orthogonal Sets#^thm-41-1|§41.1]] (the extended orthonormal set is independent)`.

### Structure (*Uses:* lines, to match the proofs)
- [[§49★ Quadratic Forms]]
  - **Where:** the proof of the Principal Axes Theorem (§49.2).
  - **Why:** the proof's last step cites Example §49.1(a).
  - **Change:** append `, [[§49★ Quadratic Forms#^ex-49-1|Ex. §49.1]](a) (a diagonal matrix gives only squares)` to its *Uses:* line, after `[[§41 Orthogonal Sets#^thm-41-4|§41.4]] ($P^TP = I$)`.
- [[§33 The Characteristic Equation]]
  - **Where:** the proof of Theorem §33.4.
  - **Why:** the proof cites "equation (3) of §32", which is inside Definition §32.2.
  - **Change:** insert `[[§32 Eigenvectors and Eigenvalues#^def-32-2|Def. §32.2]] (equation (3)), ` after `Def. §32.1]], ` in its *Uses:* line.
- Both additions are within one chapter, so the chapter "Builds on/Used by" counts do not change.

### Writing
- [[§11 Matrix Operations]], Example §11.1(c): "Only one row of a product needs only one row of the left factor" → "A single row of a product needs only one row of the left factor".
- [[§18 Subspaces of ℝⁿ]], the end of the subspace examples: "every line through the origin and one of its vectors," → "the whole line through the origin and any one of its vectors,".
- [[§21 Properties of Determinants]], the geometric remark after the multiplicative property:
  - **Problem:** the equation already carries absolute values, so "at least up to sign" was confusing.
  - **Change:** "So $|\det AB| = |\det A|\,|\det B|$, at least up to sign." → "So $|\det AB| = |\det A|\,|\det B|$: the geometric argument gives the multiplicative property up to sign."
- [[§25 Linearly Independent Sets; Bases]], Example §25.2(c):
  - **Problem:** the old wording invited confusion with the Fundamental Theorem of Algebra.
  - **Change:** "(a fundamental theorem of algebra)" → "(a basic fact of algebra, [[§13 Polynomials#^ladr-4-8|LADR 4.8]])".
- [[§51★ The Singular Value Decomposition]], the Connections callout after Definition §51.2 (not in the patch): link "Definition §51.4" as `[[§51★ The Singular Value Decomposition#^def-51-4|Definition §51.4]]`.

### Connections
Each addition is a new `> [!remark]- Connections` callout, or a new bullet, placed right after the *Uses:* line named. All targets were opened and checked.
- [[§32 Eigenvectors and Eigenvalues]], after the *Uses:* line of Theorem §32.1:
  - `- Rigorous treatment: [[§16 Upper-Triangular Matrices#^ladr-5-41|LADR 5.41]] (the eigenvalues of an operator with an upper-triangular matrix are exactly its diagonal entries), proved there without determinants.`
- [[§33 The Characteristic Equation]], after the *Uses:* line of Theorem §33.4:
  - `- Rigorous treatment: [[§14 Invariant Subspaces#^ladr-5-7|LADR 5.7]] ($\lambda$ is an eigenvalue $\Leftrightarrow$ $T - \lambda I$ is not invertible) together with [[§34 Determinants#^ladr-9-50|LADR 9.50]] (invertible $\Leftrightarrow$ $\det \ne 0$), the same two steps. Axler identifies his characteristic polynomial with $\det(zI - T)$ only later, [[§34 Determinants#^ladr-9-62|LADR 9.62]].`
- [[§34 Diagonalization]], after the *Uses:* line of Theorem §34.2:
  - `- Rigorous treatment: [[§17 Diagonalizable Operators#^ladr-5-58|LADR 5.58]] (an operator on $V$ with $\dim V$ distinct eigenvalues is diagonalizable), by the same argument from [[§14 Invariant Subspaces#^ladr-5-11|LADR 5.11]].`
- [[§40 Inner Product, Length, and Orthogonality]], after the *Uses:* line of the Pythagorean Theorem (§40.4). Both targets already link back to §40.4. Two bullets:
  - `- Rigorous treatment: [[§19 Inner Products and Norms#^ladr-6-12|LADR 6.12]], for any inner product space; Axler states only the direction "orthogonal $\Rightarrow$ the identity". The converse holds over $\mathbb{R}$ by the same computation, but fails over $\mathbb{C}$, where the identity says only $\operatorname{Re}\langle u, v \rangle = 0$.`
  - `- Hilbert-space version, with its extension to finitely many orthonormal vectors: [[§24 Orthonormal Sets and Bases#^lem-24-1|556 Lem. §24.1]].`
- [[§42 Orthogonal Projections]], a new last bullet in the Connections callout after Definition §42.2 (the Best Approximation callout):
  - `- Fourier version: for the integral inner product of [[§46 Inner Product Spaces|§46]], the truncated Fourier series is the best mean-square approximation by trigonometric polynomials, [[§11★ Mean Error and Convergence in Mean#^thm-11-2|341 Thm. §11.2]].`
- [[§43 The Gram–Schmidt Process]], after the *Uses:* line of Corollary §43.2:
  - `- Rigorous treatment: [[§20 Orthonormal Bases#^ladr-6-35|LADR 6.35]] (every finite-dimensional inner product space has an orthonormal basis, by the same argument) and [[§20 Orthonormal Bases#^ladr-6-36|LADR 6.36]] (every orthonormal list extends to an orthonormal basis, the step used to complete $U$ in the proof of the SVD, [[§51★ The Singular Value Decomposition#^thm-51-4|Theorem §51.4]]).`

### Hubs
Unless stated otherwise, each addition goes under "## Connections", after the "- See … for context and examples." line. Where a hub copies a section callout, the text is the section's own, verbatim.
- [[The Best Approximation Theorem]]: add the two bullets of the §42 callout after Definition §42.2:
  - Rigorous treatment, LADR 6.61.
  - The closed-convex-set bullet, 556 Thm. §22.2.
- [[The Change-of-Coordinates Matrix]]: add the §29 rigorous-treatment bullet: LADR 3.82, LADR 3.84 and Theorem §35.2. It also adds "(Lay: [[§29 Change of Basis#^thm-29-2|Theorem §29.2]])" after LADR 3.82.
- [[The Coordinate Mapping Is an Isomorphism]]: add the two bullets of the §26 callout after Definition §26.3:
  - LADR 3.69 and 3.70, the hub [[Dimension shows whether vector spaces are isomorphic]], and Theorem §27.2.
  - 250 Def. §9.1 and 250 Thm. §9.2.
- [[The Principal Axes Theorem]]: add the three bullets of the §49 callout after Definition §49.3:
  - LADR 9.23(b) and 9.13.
  - Calc Def. §85.3.
  - 341 Def. §40.1.
- [[The Diagonalization Theorem]]:
  - **Where:** the end of the existing ODE bullet.
  - **Why:** the section callout cites 331 Thm. §31.2, but the hub did not.
  - **Change:** `[[§33★ Fundamental Matrices#^thm-33-8|331 Thm. §33.8]]).` → `[[§33★ Fundamental Matrices#^thm-33-8|331 Thm. §33.8]]); the eigenvector solutions $\mathbf{v}e^{\lambda t}$ form a fundamental set, [[§31 Homogeneous Linear Systems with Constant Coefficients#^thm-31-2|331 Thm. §31.2]].`
- [[The Fundamental Subspaces Are Orthogonal Complements]], Connections line 27: replace the section-relative text "(Proposition §40.7 and Corollary §40.8 below)" with `([[§40 Inner Product, Length, and Orthogonality#^prop-40-7|Proposition §40.7]] and [[§40 Inner Product, Length, and Orthogonality#^cor-40-8|Corollary §40.8]])`.
- [[The Invertible Matrix Theorem]]:
  - **Change:** remove `- [[§19 Dimension and Rank#^thm-19-3|Theorem §19.3: The Invertible Matrix Theorem (Continued)]]` from "Its proof uses".
  - **Why:**
    - The proof's *Uses:* line does not cite §19.3.
    - The only mention of §19.3 is the forward pointer "Continued with statements (m)–(r)" inside the theorem statement.
    - §19.3 itself uses §13.1, so listing it also made the dependency circular.
- [[Eigenvalues Are the Roots of the Characteristic Equation]]: add the same rigorous-treatment bullet as in §33 (LADR 5.7, 9.50, 9.62).
  - Its "Its proof uses" already lists Definition §32.2. With the *Uses:* fix above, the hub and section agree.
- [[Cofactor Expansion]]: add `- Rigorous treatment: LADR does not state the expansion itself; it follows from the permutation formula [[§34 Determinants#^ladr-9-46|LADR 9.46]] by grouping its $n!$ terms according to which entry of row $i$ (or column $j$) they contain (see the note after the theorem in [[§20 Introduction to Determinants]]).`
- **Hubs with nothing to add:**
  - [[Multiplicative Property of the Determinant]], [[The QR Factorization]], [[Least Squares via the Normal Equations]], [[The Basis Theorem]], [[Determinants as Area or Volume]] and [[Existence and Uniqueness Theorem for Linear Systems]] already match their sections.
  - [[Cramer's Rule]], [[Uniqueness of the Reduced Echelon Form]] and [[Convergence of Regular Markov Chains]] have no LADR counterpart.

### Other: computed counts (recounted exactly)
**How the counts were recounted.** I rebuilt the count script: it counts links to other subjects inside the `[!…] Connections` callouts of section notes, excluding Physics. It reproduces every existing number exactly: Linear Algebra 197, Calculus 25, Functional Analysis 20, Logic and Proofs 12, Group Theory 8, Multivariable Analysis 8, and each chapter value.

**What was wrong.** The old numbers simply omitted ODE, Fourier and Complex Variables. The Connections additions above also change some Linear Algebra, Functional Analysis and Fourier counts. Counts with the additions:

**[[Applied Linear Algebra]] (home note)**
- **Line 18:** "Dashed arrows to the Math subjects: where the rigorous treatment is," → "Dashed arrows to the Math and Applied Math subjects: where the rigorous treatment or a further development is,".
- **Line 123:**
  - Old: "…to each Math subject: [[Linear Algebra]] (197), [[Calculus]] (25), [[Functional Analysis]] (20), [[Logic and Proofs]] (12), [[Group Theory]] (8), [[Multivariable Analysis]] (8)."
  - New: "…to each Math and Applied Math subject: [[Linear Algebra]] (206), [[Ordinary Differential Equations]] (62), [[Calculus]] (25), [[Complex Variables]] (23), [[Fourier Series and PDEs]] (23), [[Functional Analysis]] (21), [[Logic and Proofs]] (12), [[Group Theory]] (8), [[Multivariable Analysis]] (8)."
  - Without the proposed Connections additions the numbers would be LA 197, ODE 62, CV 23, Fourier 22, FA 20.
- **Mermaid graph:**
  - Add the nodes `X7["Ordinary Differential Equations (331)"]`, `X8["Fourier Series and PDEs (341)"]` and `X9["Complex Variables (342)"]`.
  - Add these edges (only counts ≥3 are drawn):

| From | To X7 (ODE) | To X8 (Fourier) | To X9 (Complex Variables) |
|---|---|---|---|
| C1 | 4 | — | — |
| C3 | 3 | — | — |
| C4 | 8 | — | — |
| C5 | 37 | — | 6 |
| C6 | 3 | 12 | — |
| C7 | 3 | 8 | — |
| C8 | 4 | — | 17 |

  - Change existing labels: `C5 -.->|23| X1` → 29, `C6 -.->|29| X1` → 32, `C6 -.->|16| X4` → 17.

**Chapter "Developed further in (other subjects)" lines** (existing order kept; ODE, Fourier and CV appended after Calculus):
- [[· 1 Linear Equations in Linear Algebra]]: add [[Ordinary Differential Equations]] (4).
- [[· 2 Matrix Algebra]]: add [[Fourier Series and PDEs]] (1).
- [[· 3 Determinants]]: add Ordinary Differential Equations (3).
- [[· 4 Vector Spaces]]: add Ordinary Differential Equations (8).
- [[· 5 Matrix Eigenvalues and Eigenvectors]]: Linear Algebra 23 → 29; add Ordinary Differential Equations (37), Fourier Series and PDEs (2), [[Complex Variables]] (6).
- [[· 6 Orthogonality and Least Squares]]: Linear Algebra 29 → 32, Functional Analysis 16 → 17; add Ordinary Differential Equations (3), Fourier Series and PDEs (12).
- [[· 7★ Symmetric Matrices and Quadratic Forms]]: add Ordinary Differential Equations (3), Fourier Series and PDEs (8).
- [[· 8 Complex Numbers]]: add Ordinary Differential Equations (4), Complex Variables (17).

## Flagged for the author (not edited)
- **"Load-bearing results" counts in all 8 chapter notes cannot be reproduced from the current *Uses:* lines.**
  - Examples:
    - Theorem §33.1 is claimed to have 91 later results; the *Uses:* graph gives 3.
    - Theorem §51.3: 91 claimed; the graph gives 5.
    - Theorem §48.1: 91 claimed; the graph gives 20.
  - Eight results share the value 91. This suggests the generator used an older or different graph.
  - The counts were not edited, because I could not identify the counting rule exactly.
- **No `Examples/` folder exists.** Worked examples live only inside the section notes. Nothing was created, because that is a structural decision for the author.
- **Citation cycle.** [[§42 Orthogonal Projections]] (Theorem §42.1) → Corollary §43.2 → Theorem §43.1 → Theorem §42.1 is a cycle in the *Uses:* graph.
  - The proof of §42.1 explains why it is not circular: Gram–Schmidt only projects onto subspaces that already have an orthogonal basis.
  - This is fine mathematically. It is noted only because it affects any computed dependency counts.
- **Theorems stated without a proof block.** Each is deliberate and carries a note or remark: §6.1, §14.2, §20.1, §21.1, §21.9, §22.6, §31.3, §33.1, §33.3, §47.4, §53.1, §53.3. Most point to LADR or to a later section.
- **Possible new hubs (judgement call).** §50.1 (Extreme Values Are Extreme Eigenvalues) and §51.4 (The SVD) are central results without hubs. Adding hubs is a structural choice for the author.

## Placeholder proofs still open
None. No "[To be proved.]", "TODO", "(to be filled)" or similar text was found in any of the 80 notes.

## Requests outside my scope
- **README.md, line 32.** The status "complete (Ch. 1–7; Ch. 7 beyond the course)" leaves out Chapter 8 ([[· 8 Complex Numbers]], Lay Appendix B, §53). Suggested: "complete (Ch. 1–8; Ch. 7 beyond the course; Ch. 8 = Appendix B)".
- **[[Linear Algebra]] (optional reciprocal links).** These LADR blocks are now cited from Applied Linear Algebra, and the Linear Algebra owner may add back-links:
  - LADR 5.7, 5.41, 5.58, 6.35, 6.36, 9.50, 9.62 and 4.8.
  - Targets: Theorem §33.4, Theorem §32.1, Theorem §34.2, Corollary §43.2, Theorem §33.4 again, and Example §25.2.
  - LADR 6.12 and 556 Lem. §24.1 already link to §40.4.

## Checks run
- **Frontmatter, nav and headings** (53 section notes): frontmatter keys, nav lines `← · ↑ · →`, and duplicate headings. No problems.
- **Block IDs and numbering:** block-ID/title agreement and continuous numbering of every definition, theorem, proposition, corollary, lemma, example and remark. No problems.
- **Textual references:** every "Theorem §a.b" style reference resolves to a block of the right kind.
- **LADR links:** all 223 resolve, and each label number matches the block ID. Context review found 1 wrongly ordered pair (§9, above).
- **Hubs:** "Its proof uses" vs *Uses:* lines, and hub vs section Connections, for all 18 hubs. 3 proof-use mismatches and 6 missing rigorous-treatment or cross-subject links were found.
- **Computations:**
  - 114 consecutive row-equivalence steps and 44 matrix equality chains were checked by script: 0 errors.
  - sympy spot checks of the diet problem, LU, Leontief, determinants, Markov, characteristic polynomials and eigenvectors (§33–§39, §48–§52), the SVDs of Examples §51.1–§51.3 and the pseudoinverse, and the PCA numbers in §52: all correct.
- **Links and syntax:** `links.py` reports 0 problems in Applied Linear Algebra. Dollar-sign parity and callout syntax are clean in all 31 files touched by the proposals.
- **Placeholders:** search for placeholder text found 0.
