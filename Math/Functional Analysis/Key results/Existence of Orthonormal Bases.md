---
subject: math
type: theorem
source: "[[Functional Analysis]]"
aliases: ["MATH 556 24.12", "Lax §6.4, Thm 9"]
tags: [functional-analysis, hub]
---
![[§24 Orthonormal Sets and Bases#^thm-24-12]]

## Treated in
- [[§24 Orthonormal Sets and Bases#^thm-24-12|Theorem §24.12: Existence of Orthonormal Bases]], in [[§24 Orthonormal Sets and Bases]]

## Its proof uses
- [[§5 Proof of the Hahn–Banach Theorem#^thm-5-2|Theorem §5.2: Zorn's Lemma]]
- [[§24 Orthonormal Sets and Bases#^def-24-1|Definition §24.1: Orthogonal and Orthonormal Sets]]
- [[§24 Orthonormal Sets and Bases#^def-24-2|Definition §24.2: Complete Orthogonal Set]]
- [[§24 Orthonormal Sets and Bases#^thm-24-8|Theorem §24.8: Characterizations of an Orthonormal Basis]]

## Used in (Functional Analysis)
- (not cited later in the course)

## Connections
- **How.** Apply [[Zorn's Lemma]] to orthonormal sets ordered by inclusion ([[Functional Analysis Problem-Solving Techniques#^rem-t3|Technique 3]]). The union of a chain is orthonormal, because any two of its members lie in one set of the chain. A maximal set is complete: a nonzero x orthogonal to all of it could be normalized and added. A complete set is a basis by [[Characterizations of an Orthonormal Basis]]. Lax shows instead that a maximal set has closed span H, via Bessel ([[Functional Analysis Lax Concordance|Concordance C.2]]).
- **Finite dimensions.** Gram–Schmidt suffices ([[Gram–Schmidt procedure]], [[§21 Orthonormal Bases#^ladr-6-35|LADR 6.35]]). The step-by-step construction looks countable but need not be, so Zorn replaces the enumeration ([[§24 Orthonormal Sets and Bases#^rem-24-10|Remark §24]]). When a countable dense set is available, Gram–Schmidt along it does work ([[Separable Hilbert Spaces Have Countable Orthonormal Bases]]).
- **Size of the basis.** Bare existence is “almost useless, because there are too many” (Wu). In a separable space every orthonormal set is countable ([[§32 Position Eigenstates and Continuous Resolutions#^prop-32-1|§32.1]]), so every orthonormal basis of L²(ℝⁿ) is countably infinite ([[§32 Position Eigenstates and Continuous Resolutions#^thm-32-2|§32.2]]). The uncountable family of position eigenstates therefore cannot be one.
- **Also in [[Applied Linear Algebra]]:** [[§53 The Gram–Schmidt Process#^cor-53-2|235 Cor. §53.2]] (subspaces of ℝⁿ, by Gram–Schmidt, with worked examples).
