---
subject: math
type: theorem
source: "[[Topology]]"
aliases: ["Topology 29.2", "change of basepoint"]
tags: [topology, hub]
---
![[§29 The Fundamental Group#^thm-29-2]]

## Treated in
- [[§29 The Fundamental Group#^thm-29-2|Theorem §29.2: Basepoint Independence]], in [[§29 The Fundamental Group]]

## Its proof uses
- [[§26 Algebra Prerequisites꞉ Groups#^def-26-4|Definition §26.4: Isomorphism]]
- [[§26 Algebra Prerequisites꞉ Groups#^prop-26-4|Proposition §26.4: Bijectivity via Two-Sided Inverse]]
- [[§28 Homotopy of Paths#^thm-28-6|Theorem §28.6: Properties of Path Concatenation]]

## Used in (Topology)
- [[§29 The Fundamental Group#^cor-29-3|Corollary §29.3: π₁ is Independent of Basepoint for Path-Connected Spaces]]
- [[§35 Deformation Retracts and Homotopy Type#^lem-35-4|Lemma §35.4: Homotopic Maps and π₁: General Case]]
- [[§35 Deformation Retracts and Homotopy Type#^thm-35-5|Theorem §35.5: Homotopy Equivalence Induces Isomorphism on π₁]]

## Connections
- **Immediate consequence.** For path-connected X the isomorphism type of π₁(X, x₀) does not depend on x₀ ([[§29 The Fundamental Group#^cor-29-3|Corollary §29.3]]); this is why simple connectivity can be checked at a single basepoint and why one writes π₁(S¹) ≅ ℤ without one ([[§32 Lifting and the Fundamental Group of the Circle#^rem-32-13|remark in §24]]).
- **Not canonical.** The isomorphism α̂ depends on the path α: a different path changes it by conjugation, so all choices agree when π₁ is abelian ([[§29 The Fundamental Group#^rem-29-3|remark after Corollary §23.3]]).
- **Moving basepoints.** α̂ is the correction term in [[§35 Deformation Retracts and Homotopy Type#^lem-35-4|Homotopic Maps and π₁: General Case]] (§26.14), k∗ = α̂ ∘ h∗, which is what proves [[§35 Deformation Retracts and Homotopy Type#^thm-35-5|Homotopy Equivalence Induces Isomorphism on π₁]] (§26.15).
- **Proof pattern.** The group identities come from [[Properties of Path Concatenation]]; bijectivity is shown by exhibiting the two-sided inverse β̂ for the reverse path, the technique of [[§26 Algebra Prerequisites꞉ Groups#^rem-26-4|the remark after Proposition §21.4]].
