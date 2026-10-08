---
type: demo
tags: [demo]
---
**DEMO** — a readable preview of layout option 1 for the CB chapter. No existing note was edited. Delete this folder after review.

# What the demo shows

**Option 1:** every statement that stays true with the physics words removed lives in CB. The physics section keeps the physical statements and the concrete realizations used in calculations. It opens with a block "The mathematics used here" that embeds the CB statements it relies on, in lecture order.

The subject is [[§C5a.3 The Lorentz Action on Spinor Space]], shown as two demo notes:

- [[Demo §CB.11 Spin(1,3) and the Lorentz Algebra on Spinor Space]] is the CB home of the abstract content. It works over a Clifford module $W$ with maps $\gamma^\mu$, has full proofs and ends with a "Used in" list.
- [[Demo §C5a.3 The Lorentz Action on Spinor Space (option 1)]] is the physics section as it would read under option 1.

All block IDs are `^demo-…`, so none collides with a real ID. Box numbers are what they would become after the move, so the physics boxes are renumbered (table below).

# Box by box: current note → option 1

| Current box in §C5a.3 | Option 1 | Where it is now |
|---|---|---|
| Def. §C5a.3.1 Spinor generators | **moved to CB**, embedded | Def. §CB.11.1 (stated for any Clifford module) |
| Thm §C5a.3.1 γ rotates as a vector (Problem Set 4.5(b)) | **moved to CB**, linked, not embedded (to keep to 4 embeds) | Thm §CB.11.2; also listed in "What the calculations use" |
| Thm §C5a.3.2 Lorentz algebra (Problem Set 4.5(c)) | **moved to CB**, embedded | Thm §CB.11.3 |
| Def. §C5a.3.2 Dirac representation | **split**: the exponential $\Lambda_W(\omega)$ goes to CB (Def. §CB.11.4); the Dirac spinor and the field law $\psi'(x) = \Lambda_{1/2}\psi(\Lambda^{-1}x)$ **stay** | demo Def. §C5a.3.1 |
| Def. §C5a.3.3 Spin matrices | **stays** (notation used in calculations) | demo Def. §C5a.3.2 |
| Thm §C5a.3.3 Generators in the chiral basis | **stays** | demo Thm §C5a.3.1 |
| Example §C5a.3.1 4×4 matrices | **stays** | demo Example §C5a.3.1 |
| 3 embeds from §C3.3 (spinor representation, tensor/spinor split, remark on labels) | **dropped from the page** and replaced by links. They are representation theory, so under option 1 they would sit in the CB chain. | links in demo Thm §C5a.3.2 and Connections |
| Thm §C5a.3.4 Dirac rep = (½,0) ⊕ (0,½) | **split**: a new basis-free version (the volume element $\gamma^5$ splits the module, and a 2π rotation gives −1) goes to CB, embedded; the chiral-basis reading **stays** | Thm §CB.11.5 + demo Thm §C5a.3.2 "The Weyl Halves in the Chiral Basis" |
| Remark: Why half the angle | **stays** | demo Remark |
| Thm §C5a.3.5 Adjoints of the generators | **moved to CB**, embedded; its physics bullets (ψ†ψ, ψ̄, "ψ is a classical field") **stay** as a remark | Thm §CB.11.6 + demo "Remark: Spinor boosts are not unitary" |
| Connections, bullet 1 (Clifford ⇒ orthogonal algebra in any dimension) | **moved to CB** Connections; the physics note keeps a one-line pointer | — |
| — | **new**: "Remark: What the calculations use" (a summary of the working formulas, with links) | demo Remark |

# Size

| | lines | characters |
|---|---|---|
| Current §C5a.3 | 271 | 34.4 k |
| Demo physics §C5a.3, source | 175 | 27.1 k |
| Demo physics §C5a.3, as rendered (adds ≈ 31 lines of embedded statements; proofs not embedded) | ≈ 206 | — |
| Demo §CB.11, source (new; holds the moved proofs plus the new basis-free proof) | 198 | 25.7 k |

The physics source shrinks by about a third in lines but only by about a fifth in characters. What stays (the explicit matrices, the example, the remarks) is the dense part. The moved proofs were collapsed derivations, so on screen the page gets less shorter than the line count suggests.

# Assessment of readability

**What reads better.**
- The physics page now runs: question → tools → transformation law → explicit matrices → Weyl halves → half angle → non-unitarity. Each box on it answers a physical question.
- The two long Clifford-algebra proofs (Problem Set 4, Problem 5(b)–(c)) no longer sit between the definition of $S^{\mu\nu}$ and the definition of $\Lambda_{1/2}$.
- CB gains something the current note lacks: a proof that the Dirac representation is $(\frac12, 0)\oplus(0, \frac12)$ without choosing a basis, through $K_i = i\gamma^5J_i$. The chiral-basis computation still remains where the physicist computes.
- The "Used in" list in CB makes clear how much of the chapter depends on these few statements.

**What reads worse.**
1. *Embed density at the top.* Four theorem boxes in a row come before any physics, and they use the CB notation: $W$, "Clifford representation", $\Lambda_W$. The physics page then says the same things in its own notation: $V$, "Dirac representation", $\Lambda_{1/2}$. So the reader meets two names for each object within a screen, and a conventions sentence ("here $W = V$") has to translate.
2. *Duplication.* The splitting into $(\frac12, 0)\oplus(0, \frac12)$ appears twice on the same rendered page: the abstract embed (Thm §CB.11.5) and the chiral-basis theorem (demo Thm §C5a.3.2). Non-unitarity also appears twice: the embed (Thm §CB.11.6) and the physics remark.
3. *Jumping for proofs.* The proofs of the user's own Problem Set 4 solutions are no longer expandable in place; they are one click away in CB. Embedding the collapsed proofs as well would fix this but would double the embed block.
4. *The lemma "γ^μ is a vector" fell out of the main flow.* The 4-embed cap meant it appears only as a link and in the calculation summary, although physicists use it (covariance of the Dirac equation).
5. *Renumbering cost.* 61 links from 24 other notes point at the boxes that move (Def. §C5a.3.1, Thms §C5a.3.1, §C5a.3.2, §C5a.3.4, §C5a.3.5). Each one would have to be retargeted to CB. Counting every §C5a.3 ID, 151 incoming links would be touched, because the boxes that stay are renumbered too.
6. *It reverses the approved inventory.* `CB-INVENTORY.md` marks these boxes **STAY+EMBED**: the course home keeps the box and CB embeds it. Option 1 does the opposite for everything a course source teaches.

**Verdict.** The page reads well as physics and is self-contained at the level of statements. The weak spot is the opening block: a wall of abstract boxes in a second notation, which then repeat in concrete form.

A middle course would probably read better:
- at most 2–3 embeds;
- each embed placed at its point of use, not in one block at the top (generators before the Dirac representation, the splitting before the Weyl halves, the adjoints before the non-unitarity remark);
- CB statements written in the physics notation ($\gamma^\mu$ on $V$), so that nothing needs translating.
