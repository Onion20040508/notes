---
type: quality-check
subject: "[[Measure Theory]]"
date: 2026-10-04
tags: [quality-check]
---
# Quality check: Measure Theory
↑ [[Quality Check 2026-10-04]]

> [!note] Record only
> No change in this log was applied; the notes are as they were before the check. Each change below is a **proposal**. The coordinator's saved patch has the exact text of every proposed change (see [[Quality Check 2026-10-04]]). Locations are given as note, block, and old → new.

## Summary
Measure Theory (MATH 551) is complete and carefully cross-referenced. All 19 section notes share the same header pattern. Every callout has a block ID, and every proof has a *Uses:* line, except for two whose *Uses:* line sits next to the proof. I checked every link alias against its target block, every cross-subject label, and every hub against the *Uses:* lines. I read §11–§19 in depth, including the proofs of Egorov, Lusin, the density theorems, the Vitali/Dini/BV/AC chain and the Lᵖ theory. I skimmed §1–§10, the chapter notes, the hubs, the examples and the Problem-Solving Techniques note.

The main findings:
- One proof needs restructuring: the proof in Thm §18.27 that $f' = 0$ a.e. together with AC implies constant. Its estimates are vague, and $r$ was chosen after it was used.
- Two sentences misstate the precise claim: Rem §18.3 and the $n = 1$ step of Thm §16.7.
- The home note's description of which parts follow Axler is inaccurate.
- The Techniques note's example labels clash with §19's numbering.

## Proposed edits (not applied)
### Correctness
- [[§18 Differentiation Theory]], proof of Thm §18.27 ($f$ AC with $f' = 0$ a.e. ⇒ constant).
  - Problems in the old text:
    - $r$ was chosen only at the end ("Take $r = \frac{|f(c) - f(a)|}{2(c-a)}$"), yet it had already been used to build the Vitali cover $\Gamma$.
    - $\Gamma$ allowed $h \leq 0$.
    - The gap estimate was written with undefined expressions such as "$\sum |f(\text{gap endpoints})|$" and "$\sum_{\text{gaps}} |f \text{ change}|$".
  - Proposed changes:
    - Fix $r = \frac{|f(c)-f(a)|}{2(c-a)} > 0$ first.
    - Define $\Gamma = \{[x, x+h] : x \in A,\ h > 0,\ [x, x+h] \subseteq (a, c),\ |f(x+h) - f(x)| < r\,h\}$.
    - Name the gaps $(u_0, v_0) = (a, x_1)$, $(u_i, v_i) = (x_i + h_i, x_{i+1})$ and $(u_p, v_p) = (x_p + h_p, c)$, with total length $< \delta$.
    - Write each estimate with $\sum_{i=0}^{p} |f(v_i) - f(u_i)|$.
    - Note that $\varepsilon_0 = \frac12|f(c) - f(a)|$ does not depend on $\delta$.
  - The argument and its conclusion are unchanged.
- [[§18 Differentiation Theory]], Rem §18.3. "In other words, some upper Dini derivative strictly exceeds the corresponding lower one" → "the upper Dini derivative on one side strictly exceeds the lower Dini derivative on the other side". The displayed condition $D^+ > D_-$ or $D^- > D_+$ compares opposite sides.
- [[§18 Differentiation Theory]], Cor §18.14 (iii). The old text was "Differentiating: $(\sum g_k)' = h' = (\int_c^x h\,dt)' = h(x) = \sum g_k'(x)$ a.e." The new text: "Differentiating, the constant $\sum g_k(c)$ drops out and [[§18 Differentiation Theory#^thm-18-26|differentiation of the integral]] gives $(\sum g_k)'(x) = (\int_c^x h\,dt)' = h(x) = \sum g_k'(x)$ a.e." The old "$h'$" was wrong, because $h$ is the integrand, not the antiderivative.
- [[§16 The L¹ Space and Density Theorems]], Thm §16.7, step $n = 1$. "$|g - \chi_{(a,b)}| \leq 1$ with equality only on the two transition intervals" → "$|g - \chi_{(a,b)}| \leq 1$, and $g - \chi_{(a,b)}$ vanishes outside the two transition intervals, of total length $4\varepsilon'$". The difference is nonzero there but is not equal to 1.
- [[§19 Normed Linear Spaces and Lᵖ Spaces]], Thm §19.19 (iii) (not yet edited; same issue). "$|\chi_R(x) - g(x)| \leq 1$ with equality only on transition regions of total measure $\leq C\varepsilon'$" → "$|\chi_R(x) - g(x)| \leq 1$, and $\chi_R - g$ vanishes outside transition regions of total measure $\leq C\varepsilon'$".
- [[§18 Differentiation Theory]], proof of Thm §18.9 (iii). The bound sentence was tangled: "$f(t) \geq f(b)$ for $t \in [b, b+1/n]$ (using the extension $f(t) = f(b)$ for $t > b$, so actually $f(t) = f(b)$), and $f(t) \leq f(a+1/n)$ … More precisely:". The new text: "By the extension, $f(t) = f(b)$ for $t \in [b, b+1/n]$; since $f$ is increasing, $f(t) \geq f(a)$ for $t \in [a, a+1/n]$. Hence:". The displayed bounds are unchanged.

### Labels and cross-subject references
- [[§11 Borel Sets and Measure Spaces]]: [[Cosets Partition a Group]] is labelled "493 Prop. §26.2", but the block is 493 Prop. §28.2.
- [[Measure Theory Problem-Solving Techniques]]: the example titles "Example §19.8" … "Example §19.27" clash with §19's own Example §19.7 and with Def. §19.8 and §19.9. They were relabelled with their technique numbers: 19.8–19.15 → T1–T8 and 19.16–19.27 → T10–T21 (Technique 9 has no example). The block IDs (`^ex-19-8` …) are kept because they are linked. The aliases that quote the old labels were updated to match: [[Cantor–Bernstein Theorem]] and [[§2 The Cantor–Bernstein Theorem]] ("Ex. §19.9" → "Ex. T2"), and [[§6 Open Covers and the Heine–Borel Theorem]] ("Ex. §19.8" → "Ex. T1").

### Structure
- [[Measure Theory]], course line. The old text was "following Axler, *Measure, Integration & Real Analysis* (chapters 1–5); references …", but §18 does not follow Axler Ch. 4. The proposed text keeps all the references and says:
  - §8–§17 correspond to Axler Ch. 1–3 and 5.
  - §19 corresponds to Axler Ch. 7.
  - §1–§4 are not from Axler.
  - §18 (Vitali covering, Dini derivatives, BV and Jordan decomposition, absolute continuity) follows Royden–Fitzpatrick Ch. 6, not Axler's Hardy–Littlewood route.

### Writing
- [[§4 Uncountability]], Example §4.2 title: "Interval 0-1 is uncountable" → "The interval $[0,1]$ is uncountable".
- [[§6 Open Covers and the Heine–Borel Theorem]], proof title: "Proof of Theorem 6.1" → "Proof of Theorem §6.1".

### Connections (*Uses:* lines)
- [[§19 Normed Linear Spaces and Lᵖ Spaces]], Thm §19.21 ($L^\infty$ is not separable): the general-$E$ step uses continuity of measure, so add [[Continuity of Measure|§11.12]] to its *Uses:* line.
- [[§13 Egorov's and Lusin's Theorems]], *Uses:* lines of the Egorov and Lusin proofs: both rest on the definition of a measurable function (measurability of the sets they build), so add [[§12 Measurable Functions#^def-12-2|Def. §12.2]] to both.

### Hubs
- [[Tonelli's Theorem]], Used in (Measure Theory): add [[§16 The L¹ Space and Density Theorems#^thm-16-7|Theorem §16.7]], whose *Uses:* line cites Tonelli (§17.3).
- [[Riesz–Fischer Theorem]] and [[Riemann Integrable Implies Lebesgue Integrable]], Used in: change the link title "Proposition §17.8: Lᵖ[a,b] as a Completion" to "Proposition §17.8: Lᵖ as a Completion". `links.py` flags the bracket inside the alias.

## Flagged for the author (not edited)
- [[The Vitali Set is Not Measurable]] has the alias "Vitali set", which collides with the example note [[Vitali set]], so `[[Vitali set]]` is ambiguous in the author's intent. I did not change it, because existing aliases must not be removed.
- Measure Theory hubs do not list Applied Math users. Fubini, Tonelli and dominated convergence are cited from Fourier Series and PDEs, ODE and Complex Variables notes (convolution, infinite and semi-infinite rods, several ★ sections). The author could add a "Used in (Applied Math)" section or a Connections bullet. This was not done, because the generator's layout has no such section.
- [[§14 The Lebesgue Integral for Simple Functions]], Thm §14.14 (decreasing MCT): the "subtraction rule" $\int(f-g) = \int f - \int g$ is linked to Thm §14.8 (linearity). It follows from §14.8 applied to $g + (f - g)$ with $\int g < \infty$. One clause stating this would make the step explicit. It is minor.
- [[§13 Egorov's and Lusin's Theorems]], Lusin, Step 1: continuity on the closed set is argued through Lemma §13.2 applied to bounded pieces. This is correct but terse.

## Placeholder proofs still open
- None found in Measure Theory.

## Requests outside my scope
- Functional Analysis hubs [[Completion of a Normed Space]] and [[Continuous Functions with the Sup Norm Form a Banach Space]] use the same link title "Lᵖ[a,b] as a Completion", which `links.py` lists under "aliases containing [ ]". This belongs to the Functional Analysis owner.

## Checks run
- 61 notes: 19 sections, 6 chapter notes, 28 hubs, 6 examples, the home note and the Techniques note. They contain 729 callouts and 162 proofs. Every callout has a block ID, and every proof has a *Uses:* line, two of them placed next to the proof (§4 Ex. §4.2(c) and the proof of Thm §17.8).
- Frontmatter keys, nav lines and dollar-sign balance were checked on all sections; no problems.
- Link aliases were checked against target block numbers: 1 stale label (493). The cross-subject links to 451, 452, 493, 556 and Topology were checked; all other targets exist and say what is claimed.
- I checked each hub's "Its proof uses" against the *Uses:* lines and the statement links and found no mismatch. In the hubs' "Used in" lists, 1 user was missing (Tonelli).
- `links.py` lists no unresolved link and no bracketed alias in Measure Theory or in this log.
