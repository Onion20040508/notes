---
type: quality-check
subject: "[[Logic and Proofs]]"
date: 2026-10-04
tags: [quality-check]
---
# Quality check: Logic and Proofs
↑ [[Quality Check 2026-10-04]]

> [!note] Record only
> None of the changes in this log were applied: every note is exactly as it was before the check. Each change below is a **proposal**. The exact text of every proposed change is saved in `Quality Check/proposed-edits.patch` (see [[Quality Check 2026-10-04]]).

## Summary
All 25 section notes, 7 chapter notes, 21 hubs and the home note were checked mechanically (frontmatter, nav lines, block IDs, *Uses:* lines, empty callouts, `$` balance, hub-versus-*Uses:* agreement, numeric gcd and congruence claims), and §1, §2, §11, §14 and §20 were read in depth. The subject is in very good shape. The writing is careful, every proof I checked is correct, and the hubs mostly agree with the *Uses:* lines. The problems are small: a few hub entries that mention a result without using it, aliases that spell out symbols ("chi", "equiv"), one garbled source line, one stale count, and two hub links that `links.py` cannot parse. Per the coordinator's decision (record only), none of the edits below are applied.

## Proposed edits (not applied)

### Hubs
- [[Well-Ordering Principle]]: "Used in" lists [[§4 Proof by Contradiction#^ex-4-7|Ex. §4.7]], which only mentions the principle by contrast (the positive reals have no least element). Proposed: remove it from "Used in" and add to Connections: "Contrast: the positive *reals* have no least element, [[§4 Proof by Contradiction#^ex-4-7|Example §4.7: No Smallest Positive Real Number]]."
- [[Inclusion–Exclusion Principle]]: "Used in" lists Corollary §12.11, which only remarks that $\sum(-1)^i\binom ni=0$ is "the identity behind" the principle. Proposed: move it to Connections ("The alternating row sum …, the identity behind the principle's signs, comes from the binomial theorem in Corollary §12.11").
- [[Solvability of Linear Congruences]]: "Its proof uses" lists Proposition §11.10, which the proof cites only with "cf." (coprimality is shown directly from Bézout), and the *Uses:* line omits it. Proposed: remove it and add to Connections: "That $a/d$ and $m/d$ are coprime is shown in the proof directly from Bézout; compare Proposition §11.10."
- [[Laws of the Algebra of Sets]]: the hub lists Example §6.7, and the proof relies on it ("for the second distributive law this is done in Example §6.7"), but the *Uses:* line of [[§6 The Language of Set Theory]] Theorem §6.3 omits it. Proposed: add `[[§6 The Language of Set Theory#^ex-6-7|Ex. §6.7]]` to that *Uses:* line, after Def. §6.10. This changes no chapter count.
- [[Fermat's Little Theorem]] and [[Pigeonhole Principle]]: the alias "Theorem §21.6: Solving [a][x] = [b] in ℤ_m" contains square brackets, and `links.py` reports both links as unresolved. Proposed alias: "Theorem §21.6: Solving ⟨a⟩⟨x⟩ = ⟨b⟩ in ℤ_m", or simply "Theorem §21.6".

### Writing
- [[· 7 Surfaces and the Euler Characteristic]] line 10: "*Eccles, not in Eccles (MAT 250 lecture).*" → "*Not in Eccles: a MAT 250 lecture unit.*"
- Aliases that spell out the symbol: "chi" → "χ" in [[Euler Characteristic of Surfaces]] (2 links) and [[· 7 Surfaces and the Euler Characteristic]] (3 links), e.g. "Lemma §25.1: Subdivision Does Not Change chi". "aᵖ equiv a" → "aᵖ ≡ a" in [[Fermat's Little Theorem]]. The frontmatter alias "chi = 2 - 2h - b" is kept; an extra alias "χ = 2 − 2h − b" could be added.

### Counts (recounted exactly)
- The method behind "Developed further in" (links inside *Connections* callouts of the chapter's section notes to other Math subjects) reproduces every recorded figure except one. Chapter 3 → [[Single Variable Analysis]] is now **20**, recorded as 18. Proposed: update [[· 3 Numbers and Counting]] ("Single Variable Analysis (18)" → "(20)"), the [[Logic and Proofs]] Mermaid edge `C3 -.->|18| X1` → `|20|`, and the home's "Developed further in" total for Single Variable Analysis 49 → 51. Recount after any connection edits below.

### Connections (outward; targets verified, not applied)
The subject already links widely to [[Group Theory]] (64), [[Single Variable Analysis]] (51), [[Measure Theory]] (20) and [[Topology]] (16). Inbound links are a matter for those subjects. Genuinely useful outward links still missing:
- [[§7 Quantifiers]] Theorem §7.4 (interchanging quantifiers): continuity versus uniform continuity, [[§19 Uniform Continuity#^def-19-1|451 Def. §19.1]], and pointwise versus uniform convergence, [[§24 Uniform Convergence#^def-24-2|451 Def. §24.2]]. 451's own note on Def. §24.2 calls this "the same quantifier move".
- [[§9 Injections, Surjections and Bijections]] Definition §9.4 (image and pre-image of a subset): continuity is defined by pre-images, [[§9 Continuous Functions#^def-9-1|590 Def. §9.1]], and so is measurability, [[§12 Measurable Functions#^def-12-2|551 Def. §12.2]]. The remark after §9.4 already mentions both subjects, without links.
- [[§12★ Counting Functions and Subsets]] Definition §12.3 (permutation): the symmetric group, [[§3 Basic Examples of Groups#^def-3-5|493 Def. §3.5]], whose order $n!$ is Corollary §12.3. Definition §12.4 (characteristic function): [[§12 Measurable Functions#^def-12-3|551 Def. §12.3]].
- [[§11 Properties of Finite Sets]] Definition §11.1 (maximum and minimum): [[§4 The Completeness Axiom#^def-4-1|451 Def. §4.1]], then sup and inf.
- [[§9 Injections, Surjections and Bijections]] Definition §9.6 (Peano's axioms): Ross's version, [[§1 The Set ℕ of Natural Numbers#^def-1-1|451 Def. §1.1]]. It is linked from Remark §1.1 but not from §9.6.

## Flagged for the author (not edited)
- [[§14 Counting Infinite Sets]], proof of Theorem §14.12: "$0 \le b \le 0.1 + 0.1 < 1$" is correct but reads oddly. The bound $b \le 0.111\ldots < 1$ is the natural one; the stated one avoids summing the tail.
- [[§25 Surfaces and the Euler Characteristic]] has no `aliases` key (every other section has "Eccles N"). It is not in Eccles; add an alias only if wanted.

## Placeholder proofs still open
None found.

## Requests outside my scope
- None required. The inbound-link imbalance ("foundation of the others" but few links into Logic) can only be fixed from the other subjects: for example, [[Single Variable Analysis]] §19 and §24 could link back to Theorem §7.4, and [[Topology]] §9 to Definition §9.4.

## Checks run
- Hub "Its proof uses" vs. *Uses:* lines: 21 hubs, 3 real mismatches (above); Euclidean Algorithm and Fermat were false positives.
- "Used in" vs. inline citations: 2 mention-only entries.
- *Uses:* completeness against proof links: 3 gaps, all "cf." mentions except Ex. §6.7.
- Python check of every `\gcd(a,b)=d` and `a \equiv b \pmod m` claim: 57 claims checked; the 6 flagged were parsing artefacts.
- Truth-table spot checks in §1 and §2.
- Frontmatter: uniform. Nav lines: correct, §1–§25 continuous. `$` balance: OK. Empty callouts: none. Duplicate headings: none.
- `links.py`: the only unresolved items in Logic files are the two "[a][x]" aliases above.
