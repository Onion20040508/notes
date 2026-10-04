---
type: quality-check
subject: "[[Linear Algebra]]"
date: 2026-10-04
tags: [quality-check]
---
# Quality check: Linear Algebra
↑ [[Quality Check 2026-10-04]]

> [!note] Record only
> None of the changes in this log were applied: every note is exactly as it was before the check. Each change below is a **proposal**. The exact text of every proposed change is saved in `Quality Check/proposed-edits.patch` (see [[Quality Check 2026-10-04]]).

## Summary
All 35 section notes, 9 chapter notes, 26 hubs and the home note were checked mechanically (frontmatter, nav lines, block IDs, *Uses:* lines, empty callouts, `$` balance, hub-versus-*Uses:* agreement, hub "Used in" lists, link aliases, cross-subject reciprocity), and the proofs and worked computations of about a third of the sections were read in depth, with sympy checks where useful. The mathematics is sound: I found no wrong statement or proof. The problems are in the metadata. The hubs' "Its proof uses" and "Used in" lists often disagree with the section notes' *Uses:* lines; about 25 callout titles and link aliases lost a symbol (∗, ′, ˜, superscripts, lowercase letters); 20 Axler notation callouts are empty; three theorems nest their proof inside the statement box; the "box after …" pointers hide real dependencies in several *Uses:* lines; and the subject has almost no links to the analysis subjects that cite it. Per the coordinator's decision (record only), none of the edits below are applied. Each is described precisely enough to apply later. I had applied them during the run; the coordinator has since restored the notes.

## Proposed edits (not applied)

### Correctness (dependency records)
- [[§22 Self-Adjoint and Normal Operators]], Theorem 7.21: the proof says "Write 7.20 for … (box after [[§22 Self-Adjoint and Normal Operators#^ladr-7-19|7.19]])", and its *Uses:* line lists 7.19 (Example 7.19, normal but not self-adjoint) where the dependency is Theorem 7.20. Proposed: replace "(box after `[[…#^ladr-7-19|7.19]]`)" with "([[§22 Self-Adjoint and Normal Operators#^ladr-7-20|7.20]])", and in the *Uses:* line replace `[[§22 Self-Adjoint and Normal Operators#^ladr-7-19|7.19]]` with `[[§22 Self-Adjoint and Normal Operators#^ladr-7-20|7.20]]`. Also, in the Connections of Definition 7.18, replace "(7.20, below `[[…#^ladr-7-19|7.19]]`)" with "(`[[…#^ladr-7-20|7.20]]`)".
- [[§28 Generalized Eigenvectors and Nilpotent Operators]], proof of 8.9: "By 8.4 (box after `[[…#^ladr-8-3|8.3]]`)" → "By [[§28 Generalized Eigenvectors and Nilpotent Operators#^ladr-8-4|8.4]]". In the *Uses:* line, `…#^ladr-8-3|8.3]]` → `…#^ladr-8-4|8.4]]`. The proof applies $V=\nullsp T^n\oplus\range T^n$, which is 8.4, not 8.3. In Example 8.6, "as 8.4 promises" → link 8.4. In Theorem 8.4's statement box, "(see 8.6)" → "(see `[[…#^ladr-8-6|8.6]]`)".
- [[§32 Bilinear Forms and Quadratic Forms]], proof of 9.12: "(9.17, after `[[…#^ladr-9-16|9.16]]`)" → "([[§32 Bilinear Forms and Quadratic Forms#^ladr-9-17|9.17]])". In the *Uses:* line, `9.16` → `9.17`, because the proof uses the uniqueness in 9.17. In the proof of 9.21, "(9.17)" → link 9.17, and add the missing line `*Uses:* [[§32 Bilinear Forms and Quadratic Forms#^ladr-9-17|9.17]]` after the proof.
- [[§8 Null Spaces and Ranges]], 3.21: the annotation "*(Filled in; implicit in Axler.)*" wrongly suggests that Axler gives no proof. Axler proves 3.21; only the first step (null T is finite-dimensional) is left implicit. Proposed: "*(First step filled in: Axler takes the finite-dimensionality of $\nullsp T$ for granted; the rest follows Axler's proof.)*". The proof also links 2.25, which is missing from the *Uses:* line: change it to `[[§4 Span and Linear Independence#^ladr-2-25|2.25]], [[Every linearly independent list extends to a basis|2.32]]`.
- [[§34 Determinants]], 9.56: the proof's (b) uses 3.132, but the *Uses:* line omits it. Insert `[[§12 Duality#^ladr-3-132|3.132]]` after 9.37.
- [[§23 Spectral Theorem]], proof of 7.31: "(7.20)" → "([[§22 Self-Adjoint and Normal Operators#^ladr-7-20|7.20]])", and add 7.20 to the *Uses:* line after 7.9.
- [[§26 Singular Value Decomposition]], proof of 7.69: "(spectral theorem)" → "(spectral theorem, [[Real spectral theorem|7.29]], [[Complex spectral theorem|7.31]]: $S^*S$ is diagonal in an orthonormal basis)", and append 7.29 and 7.31 to its *Uses:* line.
- [[§21 Orthogonal Complements and Minimization Problems]], Definition 6.68 remark: "agrees with $T^\dagger$ by 7.75" → link [[§26 Singular Value Decomposition#^ladr-7-75|7.75]].

### Structure
- Theorems 7.20 ([[§22 Self-Adjoint and Normal Operators]]), 8.4 ([[§28 Generalized Eigenvectors and Nilpotent Operators]]) and 9.17 ([[§32 Bilinear Forms and Quadratic Forms]]) put the proof as a nested `> > [!proof]+` inside the statement box and have no *Uses:* line, unlike every other result. Each one carries a `%% ex:… %%` marker (`ex:7.19-normal`, `ex:8.3-thm84`, `ex:9.16-sym-alt`), so they were probably inserted by the figure tool. Proposed: move the nested proof out into its own `> [!proof]+ Proof` callout after the block ID, keeping the remaining text ("Substitute for $V=\nullsp T\oplus\range T$ …", "In matrices: …") in the statement box, and add the *Uses:* lines `7.16` / `8.3, 1.46, 3.21` / `9.16`. Block IDs stay attached to the statements.
- 20 empty `[!remark] Notation` callouts (title only). Proposed one-line bodies, stating Axler's notation:
  - [[§1 Rⁿ and Cⁿ]] 1.6, "Throughout, $\F$ stands for either $\R$ or $\C$; elements of $\F$ are called *scalars*." 1.10, retitle "N" → "n", "Fix a positive integer $n$ for the rest of the chapter." 1.15, "$0$ also denotes the list of length $n$ whose coordinates are all $0$."
  - [[§2 Definition of Vector Space]] 1.24, $\F^S$ = functions $S\to\F$ with pointwise operations. 1.28, "$-v$ is the additive inverse of $v$ (unique by 1.27); $w-v$ means $w+(-v)$." 1.29, "From now on $V$ denotes a vector space over $\F$."
  - [[§4 Span and Linear Independence]] 2.1, lists of vectors written without parentheses. 2.12, $\Poly_m(\F)$ = polynomials of degree at most $m$.
  - [[§7 Vector Space of Linear Maps]] 3.2, $\Lin(V,W)$ and $\Lin(V)=\Lin(V,V)$.
  - [[§9 Matrices]] 3.39, retitle to `$\F^{m,n}$`, "the set of $m$-by-$n$ matrices with entries in $\F$". 3.44, retitle to `$A_{j,\cdot}$, $A_{\cdot,k}$`, "row $j$ as a $1$-by-$n$ matrix; column $k$ as an $m$-by-$1$ matrix".
  - [[§10 Invertibility and Isomorphisms]] 3.61, $T^{-1}$ is the unique element of $\Lin(W,V)$ with $T^{-1}T=I_V$ and $TT^{-1}=I_W$.
  - [[§11 Products and Quotients of Vector Spaces]] 3.95, retitle "V + U" → "v + U", "$v+U=\{v+u:u\in U\}$". 3.106, retitle "̃T" → `$\tilde T$`, "$\tilde T:V/(\nullsp T)\to W$, $\tilde T(v+\nullsp T)=Tv$".
  - [[§14 Invariant Subspaces]] 5.13, $T^m$, $T^0=I$, $T^{-m}=(T^{-1})^m$. 5.14, retitle "P(T)" → "p(T)", $p(T)=a_0I+a_1T+\dots+a_mT^m$.
  - [[§19 Inner Products and Norms]] 6.5, "In this chapter and the next, $V$ and $W$ denote inner product spaces over $\F$."
  - [[§24 Positive Operators]] 7.40, $\sqrt T$ is the unique positive square root (link 7.39).
  - [[§27 Consequences of Singular Value Decomposition]] 7.98, $T(\Omega)=\{Tv:v\in\Omega\}$.
  - [[§35 Tensor Products]] 9.84, retitle to `$V_1,\dots,V_m$`, "$m>1$ and $V_1,\dots,V_m$ are finite-dimensional vector spaces."
- [[Linear Algebra]] (home): sparse compared with the sibling home notes. Proposed additions, with nothing removed:
  - Frontmatter `status: completed` and `textbook: "Axler, Linear Algebra Done Right, 4th ed."`, matching the README's "complete (Ch. 1–9)".
  - A "## Central results" list of all 26 hubs in Axler order, in the form `- [[Linear dependence lemma]] (2.19)`: 1.45, 2.19, 2.22, 2.30, 2.32, 3.4, 3.21, 3.65, 3.70, 3.107, 4.12, 5.11, 5.19, 5.22, 5.47, 6.14, 6.17, 6.32, 6.42, 7.29, 7.31, 7.70, 8.22, 8.29, 8.46, 9.50.
  - A "## Developed further in" section like the one in [[Logic and Proofs]]. Counts of links in *Connections* callouts from these notes, as of now: [[Applied Linear Algebra]] 293, [[Group Theory]] 55, [[Functional Analysis]] 45, [[Differentiable Manifolds]] 45, [[Ordinary Differential Equations]] 36, [[Calculus]] 26, [[Complex Variables]] 21, [[Multivariable Analysis]] 13, [[Measure Theory]] 5, [[Single Variable Analysis]] 4, [[Topology]] 3. Recount after the connection edits below are applied.
- Hub layout: all other subjects use "## Its proof uses", and the 22 LA hubs use "## Proof uses". Proposed: rename the heading; nothing links to it. Four hubs ([[Condition for a direct sum]], [[Fundamental theorem of algebra, first version]], [[Linear dependence lemma]], [[Linearly independent eigenvectors]]) have no proof-uses section because their proofs cite nothing. Add "## Its proof uses" with "- (only definitions)", the convention used elsewhere in the vault.

### Writing (titles and aliases)
- Callout titles to fix, with the aliases that repeat them:
  - 7.6 "Null space and range of T" → "… of T∗". Also the alias in [[· 7 Operators on Inner Product Spaces]].
  - 7.9 "Matrix of T" → "Matrix of T∗". Also the alias "Matrix of T (LADR 7.9)" in [[§12 Duality]].
  - 7.20 "T∗v": use the ∗ glyph used by 7.1, 7.7 and 7.64.
  - 5.29 "Q(T) = 0 ⟺ …" → "q(T) = 0 ⟺ …", in [[§15 The Minimal Polynomial]]. Also the aliases in [[· 5 Eigenvalues and Eigenvectors]], [[§13 Polynomials]] and [[Existence, uniqueness, and degree of minimal polynomial]].
  - 5.76 "diagonalizablity" → "diagonalizability".
  - 4.2 "Complex conjugate, z," → "z̄".
  - 3.29 "Aj,k" → `$A_{j,k}$`.
  - 3.40 "Dim Fᵐ’ⁿ = mn" → `$\dim\F^{m,n}=mn$`.
  - 3.83 "Matrix of identity on F" → "… on F²". The example uses bases of $\F^2$.
  - 3.121 "U0" → "U⁰".
  - 8.6 "F (p. 299)" → `$\F^3=\nullsp T^3\oplus\range T^3$ (p. 299)`.
  - 9.25 "M-linear form, V" → "m-linear form, V⁽ᵐ⁾". 9.26, 9.85, 9.86 and 9.91 "M-linear" → "m-linear".
  - 9.40 "ΑT" (a capital Alpha) → `$\alpha_T$`.
  - 9.76 "Tensor product of element of F" → "… of element of Fᵐ with element of Fⁿ".
  - 1.10 "N" → "n". 3.95 "V + U" → "v + U". 5.14 "P(T)" → "p(T)".
- Aliases with a lost prime, in [[§12 Duality]] and [[Fundamental theorem of linear maps]]: "The null space of T" → "… of T′" (3.128), "The range of T" → "… of T′" (3.130), and "Matrix of T (LADR 3.132)" → "Matrix of T′ (LADR 3.132)". The last one also occurs in [[§34 Determinants]].
- [[§1 Rⁿ and Cⁿ]] line 144: the alias "Commutativity of addition in F" → "… in Fⁿ".
- [[Fundamental theorem of linear maps]] line 49 is truncated: "…it becomes the matrix rank–nullity" → "…it becomes the matrix rank–nullity theorem: $\dim V=\dim\nullsp T+\operatorname{rank}\mathcal{M}(T)$." The wording comes from §10, 3.78 Connections.
- Chapter notes 4, 6, 7, 8 and 9: "(1 citations)" → "(1 citation)", 7 occurrences.
- [[Cayley–Hamilton theorem]] Connections: "$T^{-1}$ and every power $T^k$ are polynomials in $T$ of degree $<\dim V$" omits the hypothesis. Proposed: "every power $T^k$ ($k\ge0$) is a polynomial in $T$ of degree $<\dim V$, and, when $T$ is invertible, so is $T^{-1}$ (the constant term of the characteristic polynomial is then nonzero, since $0$ is not an eigenvalue)."
- [[Triangle inequality]] Connections: link the bare mentions. "of [[Single Variable Analysis]]" → add "[[§3 The Set ℝ of Real Numbers#^thm-3-3|451 Thm. §3.3]](i)", and "(in the sense of Single Variable Analysis §13)" → "[[§13 Some Topological Concepts in Metric Spaces#^def-13-1|451 Def. §13.1]]".

### Hubs ("Its proof uses" made to match the *Uses:* lines; every proof was checked)
- [[If F = C, then every operator on V has an upper-triangular matrix]]: 4.13, 5.44, 5.80, 5.41, 5.81 → 4.13, 5.44. The proof (§16 line 171) uses only those two. Move 5.41 and 5.81 into Connections ("eigenvalues are the diagonal entries, 5.41"; "commuting pairs, 5.80, with consequence 5.81").
- [[Invertible ⟺ nonzero determinant]]: 3.80 → [[Injectivity is equivalent to surjectivity (if dim V = dim W ＜ ∞)|3.65]].
- [[Cayley–Hamilton theorem]]: drop 5.24, which the proof doesn't use. Add to Connections: "relation to the minimal polynomial (5.24): the characteristic polynomial is a multiple of it (8.30)".
- [[Cauchy–Schwarz inequality]]: add 6.12. [[Gram–Schmidt procedure]]: add 2.39. [[Riesz representation theorem]]: add 6.35. [[Real spectral theorem]]: add 7.9. [[Complex spectral theorem]]: add 7.9 and 7.20, the latter once linked in the proof. [[Fundamental theorem of linear maps]]: add 2.25, once added to the *Uses:* line.
- "Used in (Linear Algebra)" corrections. Additions were checked against the *Uses:* lines; each removal was checked by reading the cited proof.
  - [[Cauchy–Schwarz inequality]]: add 7.91.
  - [[Real spectral theorem]] and [[Complex spectral theorem]]: add 7.39, remove 7.92. Its proof cites neither theorem. 7.69 stays once its proof links them.
  - [[Dimension shows whether vector spaces are isomorphic]]: add 3.78.
  - [[Every linearly independent list extends to a basis]]: add 3.125 and 5.44.
  - [[Existence of eigenvalues]]: add 5.34, remove 5.76. 5.76 doesn't use it; 5.78 is already listed.
  - [[Fundamental theorem of linear maps]]: add 5.22 and 8.31, replace 8.3 by 8.4 (8.4 is the one citing 3.21), remove 6.57.
  - [[Injectivity is equivalent to surjectivity (if dim V = dim W ＜ ∞)]]: add 7.61 and 9.50.
  - [[Invertible ⟺ nonzero determinant]]: add 9.56.
  - [[Linear map lemma]]: add 3.72 and 3.125, replace 3.111 by 3.112 (the dual-basis remark), remove 3.28 and 7.38.
  - [[Linearly independent eigenvectors]]: remove 8.11, whose proof is self-contained. Add to Connections: "generalized-eigenvector version: 8.12".
  - [[Riesz representation theorem]]: add 7.4, remove 6.57. The revisit 6.58 is already in Connections.

### Connections (reciprocal links to analysis subjects; every target verified)
Multivariable Analysis, Measure Theory, Single Variable Analysis and Topology link into LA about 77 times, and LA links back to them almost never. Proposed bullets, appended to the Connections callout of each block (or a new callout for 6.42):
- 6.14 (§19): [[Hölder's Inequality|551 Thm. §19.5]] (p = 2) and [[Directional Derivative Formula|452 Thm. §7.1]] (steepest ascent). The same two go in the [[Cauchy–Schwarz inequality]] hub.
- 6.17 (§19): [[§3 The Set ℝ of Real Numbers#^thm-3-3|451 Thm. §3.3]](i), [[§13 Some Topological Concepts in Metric Spaces#^def-13-1|451 Def. §13.1]] and [[Minkowski's Inequality|551 Thm. §19.9]].
- 7.29 (§23), 7.38 (§24) and 9.18 (§32): [[Second Derivative Test in Several Variables|452 Thm. §14.4]]. 9.18 also gets [[Multivariable Taylor's Theorem|452 Thm. §9.2]].
- 9.17 (§32): [[§22 The Algebra of Differential Forms#^prop-22-8|452 Prop. §22.8]].
- 9.61 (§34): [[§15 Multivariable Integration#^prop-15-19|452 Prop. §15.19]], [[Change of Variables Formula (multiple integrals)|452 Thm. §15.17]] and [[§18 Differentiation Theory#^thm-18-22|551 Thm. §18.22]].
- 9.50 (§34): [[Inverse Function Theorem (several variables)|452 Thm. §13.2]] and [[Implicit Function Theorem|452 Thm. §12.1]].
- 3.108 (§12): [[§8 The Differential#^def-8-1|452 Def. §8.1]]. 6.42 (§20): the gradient as the Riesz representer, [[Directional Derivative Formula|452 Thm. §7.1]].
- 3.43 (§9): [[Multivariable Chain Rule|452 Thm. §10.2]]. 3.101 (§11): [[§11 Borel Sets and Measure Spaces#^def-11-12|551 Def. §11.12]] ([[The Vitali Set is Not Measurable]]).
- 4.12 (§13): the compactness input via [[Heine–Borel Theorem]] and [[Continuous Image of a Compact Space is Compact]] (interval case: [[Extreme Value Theorem]]), and the topological proof [[§25 The Fundamental Theorem of Algebra#^thm-25-1|590 Thm. §25.1]].

## Flagged for the author (not edited)
- **Hub "Used in" lists and chapter counts come from Axler's own citations, not from the *Uses:* lines.** A recount of chapter-to-chapter *Uses:* citations does not reproduce any "Builds on (N citations)" figure. For example, ch. 9 → ch. 3 is 9 by the *Uses:* lines and 14 as recorded. I could not recount these exactly, so I left them. Decide which source the counts should follow.
- [[Existence, uniqueness, and degree of minimal polynomial]] lists 5.34 as a use. The proof of 5.34 uses the minimal polynomial without citing 5.22. Either add 5.22 to that *Uses:* line or drop the entry.
- 7.92 ([[§27 Consequences of Singular Value Decomposition]]) has no *Uses:* line, although the proof uses Bessel's inequality (6.26) and the SVD (7.70). 8.9 uses 5.19 ("$T$ has an eigenvalue") without citing it.
- The 46 `%% ex:<n>-<tag> %%` comments mark figure-insertion points, mostly before "…, pictured" example boxes. No link can target them, and the boxes have no `^` IDs. Three of them sit on theorems (7.20, 8.4, 9.17; see Structure). Adding `^ex-…` IDs would be additive, but the naming scheme is the author's call, so I left them.
- Many titles flatten sub- and superscripts ("P3(R)", "V1 ⊗ ⋯ ⊗ Vm", "E(s1f1, ...,snfn)", "qβ"). They are readable; I listed only the ones that lose meaning.
- The 9.12 proof only works when $2\ne0$ in $\F$, which holds since $\F$ is $\R$ or $\C$. It could say so explicitly, as 9.16's proof does.

## Placeholder proofs still open
None. There are no "[To be proved]", "to be filled" or similar markers in the subject.

## Requests outside my scope
- None needed for the LA aliases: no other subject repeats the garbled LA titles (checked).
- [[Multivariable Analysis]] and [[Measure Theory]] already link to LA. Once the reciprocal bullets above are applied, the links are two-way.

## Checks run
- Hub "Its proof uses" vs. the *Uses:* lines: 26 hubs, 8 mismatches (listed). "Used in" vs. citing proofs: 13 hubs corrected.
- *Uses:* completeness against proof links: 2 gaps (3.21, 9.56). Searched for unlinked "N.M" references: 7 "box after …" or bare numbers.
- Frontmatter keys: uniform across 35 sections, 9 chapters and 26 hubs. Nav lines: all correct. Section numbering §1–§35 has no gaps. `$` balance: OK. Duplicate headings: none.
- Empty callouts: 20 (all Notation). Statement callouts without block ID: none, apart from the "pictured" boxes.
- Sympy: Example 6.44 projections onto $\Poly_2$ and $\Poly_5$ verified.
- `links.py`: no unresolved links in LA files.
