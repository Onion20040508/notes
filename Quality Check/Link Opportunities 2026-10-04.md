---
type: quality-check
date: 2026-10-04
scope: "Math/ and Applied Math/"
mode: record only
status: paused (candidates found, verification not done)
tags: [quality-check, links]
---
# Link Opportunities 2026-10-04

The question: which concepts in `Math/` and `Applied Math/` could be linked to the notes where they are developed? Companion to [[Quality Check 2026-10-04]].

> [!note] Record only, paused
> No note was changed. Script-generated candidates are saved below. The verification pass was stopped before any results were written, so **every candidate is still unverified** and some are false positives.

## What was done
1. **Index.**
   - Built from the 1,210 notes in the 14 subjects.
   - Contains all 4,492 definition/theorem blocks (title, subject, note, block ID) and the 370 hub and example notes with their aliases.
2. **Parallel treatments.**
   - Blocks with the same normalised title in two different subjects: 390 cross-subject pairs.
   - 183 are linked both ways, 45 one way, and **162 not at all**.
   - Saved in `link-candidates/par_<Subject>.json`. Each pair is listed under both of its subjects, so the files hold the 207 pairs that are not linked both ways.
3. **Unlinked mentions.**
   - Plain-text uses of a concept that another subject defines or proves, in a note with no link to any of that concept's homes.
   - Everyday words were filtered out. What remains: multi-word concepts, named results, and a hand-picked list of technical single words.
   - That leaves **4,253 candidates**, saved in `link-candidates/cand_<Subject>.json` with note, line, term, context and up to 4 suggested targets (`Subject|Note#^blockid` or a hub name).

| Subject | Mention candidates | Parallel pairs |
|---|---|---|
| [[Logic and Proofs]] | 69 | 10 |
| [[Linear Algebra]] | 168 | 27 |
| [[Single Variable Analysis]] | 174 | 40 |
| [[Multivariable Analysis]] | 253 | 22 |
| [[Topology]] | 249 | 26 |
| [[Measure Theory]] | 166 | 31 |
| [[Functional Analysis]] | 440 | 19 |
| [[Differentiable Manifolds]] | 553 | 39 |
| [[Group Theory]] | 343 | 20 |
| [[Calculus]] | 391 | 68 |
| [[Applied Linear Algebra]] | 294 | 33 |
| [[Ordinary Differential Equations]] | 242 | 16 |
| [[Fourier Series and PDEs]] | 509 | 21 |
| [[Complex Variables]] | 402 | 42 |

## Early observations (from the scan, not yet verified)
**Most frequent unlinked cross-subject concepts:**

| Concept | Unlinked notes |
|---|---|
| continuous function | 118 |
| open set | 84 |
| linear map | 75 |
| fundamental theorem of calculus | 49 |
| power series | 41 |
| interior point | 36 |
| chain rule | 35 |
| inner product space | 27 |
| mean value theorem | 27 |
| simply connected | 25 |
| Hilbert space | 20 |
| orthonormal set | 19 |
| equivalence relation | 19 |
| Laplace's equation | 19 |
| initial value problem | 17 |

**Likely real parallel treatments with no link either way:**
- chain rule: Complex Variables thm-20-4 ↔ Single Variable Analysis thm-28-3
- intermediate value theorem: Calculus thm-10-10 ↔ Topology thm-14-3
- Rolle's theorem and mean value theorem: Calculus ↔ Multivariable Analysis
- similar matrices: Applied Linear Algebra ↔ Group Theory, def-33-3 in both
- term-by-term integration and differentiation: Complex Variables §71 ↔ Fourier Series and PDEs §10
- antiderivative: Calculus ↔ Complex Variables
- periodic function: Calculus ↔ Fourier Series and PDEs
- Taylor/Maclaurin series: Calculus ↔ Complex Variables
- orthogonal complement: Applied Linear Algebra ↔ Functional Analysis
- reverse triangle inequality: Complex Variables ↔ Functional Analysis

**Known false friends to drop:**
- "Cauchy's theorem": Group Theory vs Complex Variables
- "Bernoulli equation": ODE vs fluid flow
- "normal": operator, space or subgroup
- "range": of a function vs of an operator

## Next steps to finish
For each subject, check every candidate in context. Keep it only if:
- it is the same concept;
- the note actually relies on it;
- a link would help a reader.

Then pick the best target, preferring a hub over the defining block, and write the exact wikilink. The review instructions used are reproduced in the session; the record format per subject is `Quality Check/Links <Subject>.md`.
