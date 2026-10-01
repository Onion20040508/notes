# Notes

My mathematics and physics notes, kept as an [Obsidian](https://obsidian.md) vault. Each subject is organized by chapter and section, written in LaTeX-style callouts, and densely cross-linked, so a theorem links to the results its proof uses and, through backlinks, to every place it is used later.

**815 notes · 443 sections · 195 key results · ~800 figures · 25,000+ links**

---

## Subjects

### Mathematics

| Subject | Source | Status |
|---|---|---|
| [Logic and Proofs](Math/Logic%20and%20Proofs) | MAT 250 (Stony Brook) · Eccles, *An Introduction to Mathematical Reasoning* | complete |
| [Linear Algebra](Math/Linear%20Algebra) | Axler, *Linear Algebra Done Right*, 4th ed. | complete (Ch. 1–9) |
| [Single Variable Analysis](Math/Single%20Variable%20Analysis) | MATH 451 · Ross, *Elementary Analysis* | complete |
| [Multivariable Analysis](Math/Multivariable%20Analysis) | MATH 452 · Courant & John, Vol. II | complete |
| [Topology](Math/Topology) | MATH 590 · Munkres, *Topology* | complete |
| [Measure Theory](Math/Measure%20Theory) | MATH 551 · Axler, *Measure, Integration & Real Analysis* | complete |
| [Functional Analysis](Math/Functional%20Analysis) | MATH 556 · Lax, *Functional Analysis* | in progress |
| [Differentiable Manifolds](Math/Differentiable%20Manifolds) | MATH 591 · Lee, *Introduction to Smooth Manifolds* | in progress |
| [Group Theory](Math/Group%20Theory) | MATH 493 · Pinter, *A Book of Abstract Algebra* | in progress |

### Applied Mathematics

Computational courses, each linked to the rigorous treatment of the same results in the Mathematics subjects.

| Subject | Source | Status |
|---|---|---|
| [Calculus](Applied%20Math/Calculus) | MATH 233 (UMass) · Stewart, *Calculus: Early Transcendentals*, 9th ed. | complete |

### Physics

Physics subjects are built in levels: **A** introductory, **B** upper-level, **C** graduate.

| Subject | Main sources | Status |
|---|---|---|
| [Classical Mechanics](Physics/Classical%20Mechanics) | OpenStax Vol. 1 · Marion & Thornton · Landau & Lifshitz | level A in progress |
| [Electromagnetism](Physics/Electromagnetism) | OpenStax Vol. 2 · Griffiths · Zangwill | level A in progress |
| [Oscillations, Waves and Optics](Physics/Oscillations,%20Waves%20and%20Optics) | OpenStax Vol. 1, 3 · French · Fowles | level A in progress |
| [Thermal and Statistical Physics](Physics/Thermal%20and%20Statistical%20Physics) | OpenStax Vol. 2 · Blundell & Blundell | level A in progress |
| [Relativity](Physics/Relativity) | Morin · Hartle | level A in progress |
| [Quantum Mechanics](Physics/Quantum%20Mechanics) | Griffiths · Sakurai | level A in progress |
| [Quantum Field Theory I](Physics/Quantum%20Field%20Theory%20I) | PHY 513 · Schwartz | in progress |

Sign, unit and Fourier conventions are recorded in [`Physics/Conventions`](Physics/Conventions), and each physics note names the convention it follows.

---

## How the vault is organized

```
Math/ · Physics/
└── <Subject>/
    ├── <Subject>.md          subject home: sources, course info, chapter dependency diagram
    ├── 1 <Chapter>/
    │   ├── · 1 <Chapter>.md  chapter note: builds on / used by, sections, central results
    │   └── §1 <Section>.md   section notes, numbered continuously through the subject
    ├── Key results/          hub notes for load-bearing results
    ├── Examples/             workhorse examples that recur across chapters
    └── tex/                  LaTeX sources, where the notes began as LaTeX
attachments/                  figures (SVG) with their TikZ sources in src/
templates/                    note templates
preamble.sty                  shared LaTeX macros, loaded by Obsidian's MathJax
```

**Layers of knowledge.** Every subject home note has a diagram of how its chapters depend on each other. Each chapter note lists which earlier chapters it builds on and which later ones use it, with counts. Dashed edges mark results used before they are proved.

**One note per section.** A section note keeps everything in the order it was developed: definitions, results, proofs, examples, remarks and figures. Each box has a block ID, such as `^ladr-3-21` or `^thm-18-1`, so any single result can be linked, previewed on hover, or embedded elsewhere without being copied.

**Hubs.** A result gets its own note in `Key results/` only when it is load-bearing, meaning it is used across sections or subjects. A hub embeds its statement live from the section where it is proved, then lists what its proof uses, where it is used later, and its connections to other subjects.

**One home per concept.** A concept lives in the subject where it is developed, and other subjects link to it by name. For example, the triangle inequality lives in Linear Algebra, and Single Variable Analysis links to it for $|x+y|\le|x|+|y|$. Note names are unique across the vault for this reason.

---

## Anatomy of a note

```markdown
> [!theorem] 3.21 Fundamental theorem of linear maps
> Suppose $V$ is finite-dimensional and $T\in\mathcal{L}(V,W)$. Then …

^ladr-3-21

> [!proof]+
> …

*Uses:* [[Every linearly independent list extends to a basis|2.32]], …

> [!remark]- Connections
> - Physics: …
```

| Callout | Used for |
|---|---|
| `definition` | definitions |
| `theorem` | theorems, propositions, lemmas, corollaries |
| `example` | examples and counterexamples |
| `remark` | remarks, notes, connections |
| `proof` | proofs (`+` expanded, `-` folded) |
| `principle` · `derivation` · `caution` | physics: assumed principles, derivations, pitfalls |

Physics statements are also labelled by their epistemic layer: **principles** (assumed), **laws** (empirical, with their range of validity), **theorems** (derived, with a derivation) and **models** (idealizations).

---

## Using the vault

### Requirements

- [Obsidian](https://obsidian.md)
- Community plugins, all included in `.obsidian/plugins`:
  - **Extended MathJax** (`obsidian-latex`) loads the macros in `preamble.sty`, such as `\R`, `\Span`, `\nullsp`, `\ket`.
  - **Obsidian Git** handles automatic commit and sync.
  - **Image Toolkit** handles zoomable figures.
- CSS snippets in `.obsidian/snippets`:
  - `boxes.css` styles the callouts with tcolorbox-like colors.
  - `figure-size.css` and `figures-dark.css` handle figure layout and dark-theme figures.

### Opening

```bash
git clone https://github.com/Onion20040508/notes.git Notes
```

Then in Obsidian choose **Open folder as vault**, select `Notes`, and enable the community plugins when asked. The [Home](Home.md) note is the entry point.

On Windows, run `git config --global core.longpaths true` before cloning, because some paths exceed the default length limit.

### Syncing between machines

Obsidian Git pulls on startup and commits and pushes every 10 minutes. Before switching machines, run **Obsidian Git: Commit and sync**, so the two copies never edit the same note out of step.

### Graph view

In the global graph's settings, color by subject with groups such as `path:"Math/Linear Algebra"` and turn off tags and attachments. Each subject then forms its own cluster, and the edges between clusters are the cross-subject connections.

---

## Sources and licensing

These are personal study notes. Statements and proofs are written in my own words, following the cited textbooks' numbering and proof routes. Item numbers, titles and theorem names are the authors'.

- *Linear Algebra Done Right* (4th ed.) and *Measure, Integration & Real Analysis* by Sheldon Axler are open access under [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/).
- The OpenStax *University Physics* volumes are licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
- All other textbooks are cited for reference only. No textbook PDFs or other copyrighted materials are included in this repository.

Course codes refer to courses at the University of Michigan unless marked otherwise. These notes are not affiliated with or endorsed by the authors, publishers or instructors.
