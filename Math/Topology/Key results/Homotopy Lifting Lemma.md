---
subject: math
type: theorem
source: "[[Topology]]"
aliases: ["Topology 32.2"]
tags: [topology, hub]
---
![[§32 Lifting and the Fundamental Group of the Circle#^lem-32-2]]

## Treated in
- [[§32 Lifting and the Fundamental Group of the Circle#^lem-32-2|Lemma §32.2: Homotopy Lifting Lemma]], in [[§31 Covering Spaces]]

## Its proof uses
- [[§10 Continuous Functions#^thm-10-5|Theorem §10.5: Pasting Lemma]]
- [[§15 Connected Spaces#^thm-15-3|Theorem §15.3: Continuous Image of Connected Space]]
- [[§15 Connected Spaces#^lem-15-4|Lemma §15.4: Connected Subspace and Separation]]
- [[§19 Limit Point Compactness#^lem-19-2|Lemma §19.2: Lebesgue Number Lemma]]
- [[§32 Lifting and the Fundamental Group of the Circle#^lem-32-1|Lemma §32.1: Path Lifting Lemma]]

## Used in (Topology)
- [[§32 Lifting and the Fundamental Group of the Circle#^thm-32-3|Theorem §32.3: Lifts of Path-Homotopic Paths]]

## Connections
- **Proof.** It runs the [[Path Lifting Lemma]] argument on I × I. The [[Lebesgue Number Lemma]] cuts the square into small rectangles, each lifted through one slice. Connectedness pins down the slice, and a path homotopy lifts to a path homotopy.
- **Main consequence.** [[§32 Lifting and the Fundamental Group of the Circle#^thm-32-3|Lifts of Path-Homotopic Paths]] (§24.8): path-homotopic paths have lifts with the same endpoint. This makes the [[§32 Lifting and the Fundamental Group of the Circle#^def-32-2|lifting correspondence]] well defined ([[§32 Lifting and the Fundamental Group of the Circle#^rem-32-9|Well-Definedness]]). The contrapositive, that different endpoints mean not homotopic, is the working tool ([[§32 Lifting and the Fundamental Group of the Circle#^rem-32-10|The Contrapositive is the Real Tool]]).
- **Used for.** Through §24.8, lifted endpoints become homotopy invariants. This underlies [[Fundamental Group of the Circle]] and the proof that the figure eight has non-abelian π₁ ([[§38 Fundamental Group of Some Surfaces#^thm-38-4|Theorem §38.4]]).
