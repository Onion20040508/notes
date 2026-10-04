---
type: quality-check
subject: "[[Functional Analysis]]"
date: 2026-10-04
tags: [quality-check]
---
# Quality check: Functional Analysis
↑ [[Quality Check 2026-10-04]]

## Summary
Functional Analysis (MATH 556, in progress) is in good shape: all 33 section notes have the same header pattern, continuous numbering, block IDs on every numbered box and *Uses:* lines after the proofs. Every link alias in the subject was checked against the block it points to. Every hub was compared with its section note's *Uses:* line, and a share of the proofs and computations was checked by hand. Most of the work was stale "§N.M" labels left over from an older numbering (six, one of them a proof title) and LaTeX names that had been stripped badly in the hub titles. Two hubs disagreed with their proof's *Uses:* line and were aligned. The Lax–Milgram hub now says plainly that the proof is still to come. The course log contradicted itself about Thm. §26.5(2) and now does not. No mathematics needed correcting, and no placeholder proof was filled in.

## Edits made
### Correctness (labels and references)
- [[Lax–Milgram Theorem]] — plan of the proof cited Bounded Sesquilinear Forms Are Bounded Operators as "§23.1"; now "§28.1".
- [[Functional Analysis Course Log]] — Lecture 10 row labelled the link to `^pf-26-5-2` "Thm. §21.5 (2)"; now "Thm. §26.5 (2)".
- [[Standard unit vectors eₙ]] — "Theorem §15.5" (the non-compact unit ball) is now "Theorem §18.5".
- [[§24 Orthonormal Sets and Bases]] — proof of Gram–Schmidt: "the remark before Theorem §20.12" is now "the remark before Theorem §24.12" (the link target `^rem-24-10` comes just before `^thm-24-12`).
- [[§16 Minkowski's Inequality and the Spaces ℓᵖ]] — the proof callout of Theorem §16.1 was titled "Proof of Theorem §13.1" (stale number); it is now titled "Proof".
- [[§22 Projection and Orthogonal Decomposition]] — the *Uses:* line of Prop. §22.8 cited the FTC hub as "451 §34.4". The proof uses ∫ₐᵇ f′ = f(b) − f(a), which is FTC I, 451 Thm. §34.1 (the block the hub embeds). The label is now "451 §34.1".

### Structure / consistency
- [[Functional Analysis Course Log]] — "Proofs deferred in lecture … or still open" listed part (2) of Thm. §26.5, while the Lecture 9 row and the proof itself ("(Lecture 10.)") say it was proved in Lecture 10. Part (2) is now recorded as deferred at the end of Lecture 9 and proved in Lecture 10, with a link to the proof. The three open placeholders were added to the list: Thm. §27.4 and Thm. §28.2 (announced for the next lecture) and Prop. §26.3 (homework). No dates and no lecture/HW mapping were changed.
- [[Functional Analysis]] — the summaries line said the Techniques note has "fifteen" strategies; it has 18 (T1–T18). It now says "eighteen".
- [[Functional Analysis]] — Roadmap: the sentence "…a point where two of them meet: [[· 6 Bounded Linear Maps|Chapter 6]] begins the study of linear maps…" ran into the list of four threads. The Chapter 6 clause now goes with the three stages, and the colon introduces the threads again.
- [[Functional Analysis]] — the Mermaid diagram declares a Topology node with no edges, because Topology is cited once, below the drawing threshold of 2. The caption now explains this. No edge or count was changed.
- [[§1 Linear Spaces]] — stage line "Threads: dimension" (one thread) is now "Thread: dimension", matching the other sections.

### Hubs
- [[Lax–Milgram Theorem]] — "Its proof uses" said "(proof in the next lecture)". It now says the proof is pending: it was announced in Lecture 10, the proof box in §28 is a placeholder, and the planned route goes through §28.1 and Riesz. The Connections "Plan" line links the plan remark in §28.
- [[Closest Point in a Closed Convex Set]] — "Its proof uses" listed Lemma §22.1 (continuity of the inner product), which is not on the proof's *Uses:* line. The proof itself says "continuity of the norm suffices here". The entry was removed from the list, and the fact (Wu supplied §22.1 at this point in lecture) was kept as a sentence under Connections, with the link. The proof checks out with Prop. §10.4 only.
- [[Every Subspace Has a Complement]] — the proof's *Uses:* line cites Theorem §4.2 (the chain argument in Hahn–Banach's proof), but the hub left it out. It was added to "Its proof uses".
- [[Separable Hilbert Spaces Have Countable Orthonormal Bases]] — "Its proof uses" listed Prop. §25.1. The proof only compares with it ("as for ℓᵖ"), and the *Uses:* line leaves it out, so it was removed from the list. It is still linked under Connections. "onto $\mathbb{F}^n$ or $\ell^2$" was rewritten as plain Unicode, like the sibling hubs.
- [[Characterizations of an Orthonormal Basis]] — the alias "Theorem §24.11: The Fourier Basis of L²[0,2π]" ended in `]]]`, which left a stray bracket; it now uses ［0,2π］, the vault's convention in note names. "ell²" is now "ℓ²".
- LaTeX names that had been stripped badly in hub link titles were fixed: [[Interior Points via the Gauge]] ("Exactly p_K < 1" → "Exactly {p_K < 1}"), [[X ≅ X∕Y ⊕ Y]] ("X/Y oplus Y" → "X/Y ⊕ Y"), [[Orthogonal Decomposition Theorem]] ("M^perp" → "M^⊥"), [[ℓᵖ Is a Banach Space]] ("Lᵖ(Omega) and L^∞(Omega)" → "Lᵖ(Ω) and L^∞(Ω)"), [[Continuous Functions with the Sup Norm Form a Banach Space]] ("theta = 1" → "θ = 1"; "(C²[a,b], ∣·∣_X)" → "(C²[a,b], ‖·‖_X)", since it is the norm).
- [[Closest Point in a Closed Convex Set]] — "as in Step 2 of [[Riesz's Lemma]]" now links the proof block `^pf-18-2`, where that Step 2 is.

### Connections
- No missing connections were found that justified an edit. The subject already links LADR, 551, 590, 451, 235, 341, ODE and Physics in its Connections callouts, and a sample of these was checked against their targets.

## Flagged for the author (not edited)
- [[Functional Analysis]] and the chapter notes — computed counts do not match a recount from *Uses:* lines. For example, Measure Theory → Chapter 4 is labelled 13, but Chapter 4's *Uses:* lines contain 8 Measure Theory links; Chapter 4 "Builds on 3 Normed Linear Spaces (27)" against 26 links; Chapter 5 "Builds on … (28)" against 25; Chapter 2 "Linear Algebra (1)" against 0. The generator evidently also counted citations in proof bodies, so the counts could not be reproduced exactly. They were left unchanged (rule 6).
- Hub "Used in" lists — they list only *later* results, and they draw on citations in proof bodies as well as *Uses:* lines. So [[Zorn's Lemma]] lists only §24.12, although §1.8 and the proof of §4.2 cite it on their *Uses:* lines (both are named in its Connections). This looks like a deliberate design and was not changed.
- [[§1 Linear Spaces]] — the proof of Prop. §1.1 says "A subspace is nonempty by convention", but Def. §1.2 does not state non-emptiness. Adding "nonempty" to the definition is the author's call.
- [[· 7 Functional Analysis and Quantum Mechanics]] has no "Central results" section, unlike the other chapter notes, because it has no hubs. This is consistent with the generator and was left as is.
- The figure file names (m556-21-1.svg for §26, m556-23-2.svg for §28, and others) carry an older numbering. This is cosmetic. Renaming them would touch attachments/, which is out of scope.

## Placeholder proofs still open
- [[§26 Boundedness and Continuity#^pf-26-3|Prop. §26.3]] (∂ₓ₁ unbounded in the maximum norm): "Homework; to be added after submission." This is live homework from Lecture 10.
- [[§27 Dual Spaces#^thm-27-4|Thm. §27.4]] ((Lᵖ)′ = Lᵖ′): "Next lecture."
- [[§28 Sesquilinear Forms and the Lax–Milgram Theorem#^pf-28-2|Thm. §28.2]] (Lax–Milgram): "Next lecture." It is a Central result with a hub, and the hub now says the proof is pending.
- [[§17 The Function Spaces Lᵖ(Ω)#^thm-17-4|Thm. §17.4]] (density): deferred in lecture. Wu may present a proof without heavy measure theory; it is cited from MATH 551 meanwhile.

## Requests outside my scope
- None needed for this subject. Reciprocal links from the Applied Math subjects into Functional Analysis are already in place where checked: [[§41 Orthogonal Sets]] (235), and the Fourier Series and PDEs hubs such as [[Parseval's Equality for Fourier Series]].

## Checks run
- Frontmatter keys by note type (33 sections, 7 chapters, 29 hubs, 6 examples, 3 summaries, 1 home): uniform.
- Nav lines on all 33 sections; section numbers §1–§33 continuous; numbering within each section continuous for the theorem family, definitions and examples, and every header number agrees with its block ID (script over all numbered boxes in both subjects; 0 mismatches).
- Every callout of a definition, theorem or example in a section note has a block ID; no empty callouts; no callout types outside the README list; no duplicate headings; `$` balance per line: 0 problems.
- Link-alias audit: every "§N.M" in an alias was compared with the header of the block it links to (direct block links and hub embeds), including cross-subject labels such as "451 §…" and "551 §…". 6 stale labels were found and fixed. No bare "§N.M" label points to a definition or example without a kind word.
- Hub audit: "Its proof uses" compared with the proof's *Uses:* line for all 29 hubs. 3 real mismatches were fixed; the remaining differences are script artefacts (proofs located in another section, or `pf-` references).
- Placeholder search: 4 open items, listed above.
- links.py after the edits: no unresolved links or block refs in Functional Analysis.
