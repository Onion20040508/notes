---
subject: math
type: theorem
source: "[[Functional Analysis]]"
aliases: ["MATH 556 28.1", "Lax §6.4, Thm 9"]
tags: [functional-analysis, hub]
---
![[§28 Existence of Orthonormal Bases and Separability#^thm-28-1]]

## Treated in
- [[§28 Existence of Orthonormal Bases and Separability#^thm-28-1|Theorem §28.1: Existence of Orthonormal Bases]], in [[§28 Existence of Orthonormal Bases and Separability]]

## Its proof uses
- [[§6 Proof of the Hahn–Banach Theorem#^thm-6-2|Theorem §6.2: Zorn's Lemma]]
- [[§27 Orthonormal Sets and Bases#^def-27-1|Definition §27.1: Orthogonal and Orthonormal Sets]]
- [[§27 Orthonormal Sets and Bases#^def-27-2|Definition §27.2: Complete Orthogonal Set]]
- [[§27 Orthonormal Sets and Bases#^thm-27-8|Theorem §27.8: Characterizations of an Orthonormal Basis]]

## Used in (Functional Analysis)
- (not cited later in the course)

## Connections
- **How.** Apply [[Zorn's Lemma]] to orthonormal sets ordered by inclusion ([[Functional Analysis Problem-Solving Techniques#^rem-t3|Technique 3]]). The union of a chain is orthonormal, because any two of its members lie in one set of the chain. A maximal set is complete: a nonzero x orthogonal to all of it could be normalized and added. A complete set is a basis by [[Characterizations of an Orthonormal Basis]]. Lax shows instead that a maximal set has closed span H, via Bessel ([[Functional Analysis Lax Concordance|Concordance C.2]]).
- **Finite dimensions.** Gram–Schmidt suffices ([[Gram–Schmidt procedure]], [[§21 Orthonormal Bases#^ladr-6-35|LADR 6.35]]). The step-by-step construction looks countable but need not be, so Zorn replaces the enumeration ([[§28 Existence of Orthonormal Bases and Separability#^rem-28-1|Remark §28]]). When a countable dense set is available, Gram–Schmidt along it does work ([[Separable Hilbert Spaces Have Countable Orthonormal Bases]]).
- **Size of the basis.** Bare existence is “almost useless, because there are too many” (Wu). In a separable space every orthonormal set is countable ([[§39 Position Eigenstates and Continuous Resolutions#^prop-39-1|§39.1]]), so every orthonormal basis of L²(ℝⁿ) is countably infinite ([[§39 Position Eigenstates and Continuous Resolutions#^thm-39-2|§39.2]]). The uncountable family of position eigenstates therefore cannot be one.
- **Also in [[Applied Linear Algebra]]:** [[§53 The Gram–Schmidt Process#^cor-53-2|235 Cor. §53.2]] (subspaces of ℝⁿ, by Gram–Schmidt, with worked examples).
