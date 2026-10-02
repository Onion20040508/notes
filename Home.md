# Home

## Subjects
**Math**
- [[Logic and Proofs]]
- [[Linear Algebra]]
- [[Single Variable Analysis]]
- [[Multivariable Analysis]]
- [[Functional Analysis]]
- [[Differentiable Manifolds]]
- [[Topology]]
- [[Measure Theory]]
- [[Group Theory]]

**Applied Math**
- [[Calculus]]
- [[Applied Linear Algebra]]
- [[Ordinary Differential Equations]]

**Physics**
- [[Classical Mechanics]]
- [[Electromagnetism]]
- [[Oscillations, Waves and Optics]]
- [[Thermal and Statistical Physics]]
- [[Relativity]]
- [[Quantum Mechanics]]
- [[Quantum Field Theory I]]
- Conventions: [[University Physics]] (introductory level), [[Larsen PHY 513]]

## Layout
- `Math/` (proof-based), `Applied Math/` (computational courses; their main items link to the rigorous treatment in `Math/`) and `Physics/` hold one folder per **subject**, named by content. Course code, term, instructor, textbook and status are properties of the subject's home note.
- Inside a subject: the home note (with a diagram of how chapters build on each other), then one folder per **chapter**. Each chapter folder has a chapter note (builds on / used by, sections, central results) and that chapter's notes.
- Note names carry no subject prefix (the folder says which subject): section notes are `§N Title` (numbered continuously through the subject; Linear Algebra's carry Axler's section as an alias, e.g. `LADR 3A`), a chapter note is `· N Title` (the middle dot makes it sort first in its folder), summaries are `<Subject> Toolkit` etc. Names must stay unique across the vault, since links resolve by name.
- Every concept has one home, in the subject where it is developed; other subjects link to it by name. `Key results/` inside a subject holds its hub notes (load-bearing results, each embedding its statement from the section where it is proved); `Examples/` holds workhorse examples that recur across chapters.
- `attachments/` figures, `refs/` PDFs, `templates/` note templates.

## Callouts
Math: `definition`, `theorem`, `example`, `remark`, `proof` (add `-` or `+` after the type to make it foldable).
Physics: `principle`, `derivation`, `caution`.

## Rules of thumb
- A concept gets its own note once it is used in a second place.
- Link to where something is proved or defined; backlinks show where it is used.
- Physics notes name their conventions in the `conventions` property.
