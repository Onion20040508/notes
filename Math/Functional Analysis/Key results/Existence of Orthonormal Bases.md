---
subject: math
type: theorem
source: "[[Functional Analysis]]"
aliases: ["MATH 556 20.12", "Lax §6.4, Thm 9"]
tags: [functional-analysis, hub]
---
![[§20 Orthonormal Sets and Bases#^thm-20-12]]

## Treated in
- [[§20 Orthonormal Sets and Bases#^thm-20-12|Theorem §20.12: Existence of Orthonormal Bases]], in [[§20 Orthonormal Sets and Bases]]

## Its proof uses
- [[§4 Proof of the Hahn–Banach Theorem#^thm-4-2|Theorem §4.2: Zorn's Lemma]]
- [[§20 Orthonormal Sets and Bases#^def-20-1|Definition §20.1: Orthogonal and Orthonormal Sets]]
- [[§20 Orthonormal Sets and Bases#^def-20-2|Definition §20.2: Complete Orthogonal Set]]
- [[§20 Orthonormal Sets and Bases#^thm-20-8|Theorem §20.8: Characterizations of an Orthonormal Basis]]

## Used in (Functional Analysis)
- (not cited later in the course)

## Connections
- **How.** Apply [[Zorn's Lemma]] to orthonormal sets ordered by inclusion ([[Functional Analysis Problem-Solving Techniques#^rem-t3|Technique 3]]). The union of a chain is orthonormal, because any two of its members lie in one set of the chain. A maximal set is complete: a nonzero x orthogonal to all of it could be normalized and added. A complete set is a basis by [[Characterizations of an Orthonormal Basis]]. Lax shows instead that a maximal set has closed span H, via Bessel ([[Functional Analysis Lax Concordance|Concordance C.2]]).
- **Finite dimensions.** Gram–Schmidt suffices ([[Gram–Schmidt procedure]], [[§20 Orthonormal Bases#^ladr-6-35|LADR 6.35]]). The step-by-step construction looks countable but need not be, so Zorn replaces the enumeration ([[§20 Orthonormal Sets and Bases#^rem-20-10|Remark §20]]). When a countable dense set is available, Gram–Schmidt along it does work ([[Separable Hilbert Spaces Have Countable Orthonormal Bases]]).
- **Size of the basis.** Bare existence is “almost useless, because there are too many” (Wu). In a separable space every orthonormal set is countable ([[§26 Position Eigenstates and Continuous Resolutions#^prop-26-1|§26.1]]), so every orthonormal basis of L²(ℝⁿ) is countably infinite ([[§26 Position Eigenstates and Continuous Resolutions#^thm-26-2|§26.2]]). The uncountable family of position eigenstates therefore cannot be one.
