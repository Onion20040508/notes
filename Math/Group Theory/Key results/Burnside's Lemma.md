---
subject: math
type: theorem
source: "[[Group Theory]]"
aliases: ["MATH 493 28.6", "Cauchy–Frobenius lemma", "orbit counting"]
tags: [group-theory, hub]
---
![[§28 Orbit–Stabilizer#^thm-28-6]]

## Treated in
- [[§28 Orbit–Stabilizer#^thm-28-6|Theorem §28.6: Burnside's Lemma]], in [[§28 Orbit–Stabilizer]]

## Its proof uses
- [[§24 Stabilizers and Fixed Points#^def-24-1|Definition §24.1: Stabilizer; Fixed Points]]
- [[§25 Orbits#^def-25-1|Definition §25.1: Orbit; Orbit Space]]
- [[§25 Orbits#^prop-25-1|Proposition §25.1: Orbits Partition X]]
- [[§28 Orbit–Stabilizer#^thm-28-3|Theorem §28.3: Orbit–Stabilizer]]

## Used in (Group Theory)
- (not cited later in the course)

## Connections
- **Proof idea.** Count the pairs (x, g) with g ⋆ x = x in two ways. Grouped by x, the count is Σ|Stab(x)|, and by the [[Orbit–Stabilizer Theorem]] each orbit contributes |G| ([[§28 Orbit–Stabilizer#^pf-28-6|proof]]).
- **Examples.** The 24 rotations of the cube fix 6 + 9 · 2 faces in total, so they act on the faces with one orbit ([[§28 Orbit–Stabilizer#^ex-28-3|Ex. §28.3]]). For the conjugation action Fix(g) is the centralizer ([[§32 Conjugation as an Action and the Class Equation#^def-32-1|Def. §32.1]]), so the number of conjugacy classes is the average order of a centralizer. For S₃ this gives 3.
- **Same idea elsewhere.** |Fix(g)| is the trace of the permutation matrix of g ([[§19 Polynomial Rings, Permutation Matrices, and Representations#^def-19-5|Def. §19.5]], [[§31 Trace꞉ A Connection Between Matrices and Operators#^ladr-8-47|LADR 8.47]]). So the lemma says that the average trace of the permutation representation counts the orbits.
- **Coming later in the course.** In representation theory this becomes the statement that the number of orbits is the multiplicity of the trivial representation in the permutation representation.
