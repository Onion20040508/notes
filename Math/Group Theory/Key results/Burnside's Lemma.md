---
subject: math
type: theorem
source: "[[Group Theory]]"
aliases: ["MATH 493 30.6", "Cauchy–Frobenius lemma", "orbit counting"]
tags: [group-theory, hub]
---
![[§30 Orbit–Stabilizer#^thm-30-6]]

## Treated in
- [[§30 Orbit–Stabilizer#^thm-30-6|Theorem §30.6: Burnside's Lemma]], in [[§30 Orbit–Stabilizer]]

## Its proof uses
- [[§26 Stabilizers and Fixed Points#^def-26-1|Definition §26.1: Stabilizer; Fixed Points]]
- [[§27 Orbits#^def-27-1|Definition §27.1: Orbit; Orbit Space]]
- [[§27 Orbits#^prop-27-1|Proposition §27.1: Orbits Partition X]]
- [[§30 Orbit–Stabilizer#^thm-30-3|Theorem §30.3: Orbit–Stabilizer]]

## Used in (Group Theory)
- (not cited later in the course)

## Connections
- **Proof idea.** Count the pairs (x, g) with g ⋆ x = x in two ways. Grouped by x, the count is Σ|Stab(x)|, and by the [[Orbit–Stabilizer Theorem]] each orbit contributes |G| ([[§30 Orbit–Stabilizer#^pf-30-6|proof]]).
- **Examples.** The 24 rotations of the cube fix 6 + 9 · 2 faces in total, so they act on the faces with one orbit ([[§30 Orbit–Stabilizer#^ex-30-3|Ex. §30.3]]). For the conjugation action Fix(g) is the centralizer ([[§34 Conjugation as an Action and the Class Equation#^def-34-1|Def. §34.1]]), so the number of conjugacy classes is the average order of a centralizer. For S₃ this gives 3.
- **Same idea elsewhere.** |Fix(g)| is the trace of the permutation matrix of g ([[§20 Polynomial Rings, Permutation Matrices, and Representations#^def-20-6|Def. §20.6]], [[§33 Trace꞉ A Connection Between Matrices and Operators#^ladr-8-47|LADR 8.47]]). So the lemma says that the average trace of the permutation representation counts the orbits.
- **Coming later in the course.** In representation theory this becomes the statement that the number of orbits is the multiplicity of the trivial representation in the permutation representation.
