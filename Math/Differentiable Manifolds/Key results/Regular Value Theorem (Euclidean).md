---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 7.3", "regular level sets are manifolds", "Lee Example 1.32", "Lee Corollary 5.14"]
tags: [differentiable-manifolds, hub]
---
![[§7 The Regular Value Theorem#^thm-7-3]]

## Treated in
- [[§7 The Regular Value Theorem#^thm-7-3|Theorem §7.3: Regular Value Theorem]], in [[§7 The Regular Value Theorem]]

## Its proof uses
- [[§2 Topological Manifolds#^prop-2-3|Proposition §2.3: Charts onto Open Subsets Suffice]]
- [[§3 Subspaces and Products#^prop-3-3|Proposition §3.3: Universal Property of the Subspace Topology]]
- [[§3 Subspaces and Products#^thm-3-5|Theorem §3.5: Subspaces Inherit Both Conditions]]
- [[§3 Subspaces and Products#^thm-3-10|Theorem §3.10: Universal Property of the Product]]
- [[§7 The Regular Value Theorem#^thm-7-1|Theorem §7.1: Implicit Function Theorem — Lee Theorem C.40]]
- [[§7 The Regular Value Theorem#^def-7-2|Definition §7.2: Regular Point and Regular Value]]

## Its proof uses (other subjects)
- [[§9 Matrices#^ladr-3-57|LADR 3.57 Column rank equals row rank]]
- [[Multivariable Chain Rule]] (Multivariable Analysis)

## Used in (Differentiable Manifolds)
- [[§7 The Regular Value Theorem#^ex-7-2|Example §7.2: A Level Set in ℝ⁴]]
- [[§7 The Regular Value Theorem#^cor-7-4|Corollary §7.4: Open Domains and Arbitrary Values]]
- [[§7 The Regular Value Theorem#^prop-7-5|Proposition §7.5: Regular Points When N ≤ m]]
- [[§7 The Regular Value Theorem#^cor-7-7|Corollary §7.7: Holomorphic Regular Value Theorem]]
- [[§9 The Classical Groups Are Topological Manifolds#^cor-9-4|Corollary §9.4: Every Nonzero Value Is a Regular Value of det]]
- [[§9 The Classical Groups Are Topological Manifolds#^cor-9-5|Corollary §9.5: SL(n,ℝ) Is a Manifold of Dimension n² − 1]]
- [[§16 Manifolds in Euclidean Space#^thm-16-1|Theorem §16.1: The Two Descriptions Agree]]
- [[§16 Manifolds in Euclidean Space#^prop-16-2|Proposition §16.2: Regular Level Sets Are Smooth Manifolds]]
- [[§20 Tangent Spaces I꞉ The Geometric Picture#^thm-20-3|Theorem §20.3: The Geometric Tangent Space Is the Kernel of the Jacobian]]
- [[§21 Transversality#^thm-21-1|Theorem §21.1: Preimages of Transverse Level Sets]]
- [[§21 Transversality#^cor-21-3|Corollary §21.3: The Regular Value Theorem as a Special Case]]
- [[§21 Transversality#^prop-21-4|Proposition §21.4: Transverse Intersections]]

## Connections
- **Used for.** SL(n,ℝ) and every det⁻¹(c) with c ≠ 0 ([[§9 The Classical Groups Are Topological Manifolds#^cor-9-4|§9.4]], [[§9 The Classical Groups Are Topological Manifolds#^cor-9-5|§9.5]]), the level set in ℝ⁴ of [[§7 The Regular Value Theorem#^ex-7-2|Ex. §7.2]], and holomorphic level sets of even real dimension ([[§7 The Regular Value Theorem#^cor-7-7|§7.7]]). Its smooth upgrade is [[Regular Level Sets Are Smooth Manifolds]], its tangent spaces are given by [[Geometric Tangent Space Is the Kernel of the Jacobian]], and it is the case S = {c} of the [[Transverse Preimage Theorem]] ([[§21 Transversality#^cor-21-3|§21.3]]).
- **Where the hypothesis matters.** The rank must be full at every point of the level set, though it may drop elsewhere ([[§7 The Regular Value Theorem#^ex-7-1|Ex. §7.1]], [[§7 The Regular Value Theorem#^rem-7-6|§4, Remark]]). The unit sphere and the plane z = 1 meet only at the north pole, where their tangent planes coincide, and the intersection is a point instead of a curve ([[§21 Transversality#^ex-21-1|Ex. §21.1]]). If N < m, the only regular level set is the empty one ([[§7 The Regular Value Theorem#^prop-7-5|§7.5]]).
- **Same idea elsewhere.** Each independent equation costs one dimension; for a linear map this is rank–nullity ([[Fundamental theorem of linear maps]]). Lagrange multipliers in 452 assume the same independence of the constraint gradients ([[§14 Optimization and Lagrange Multipliers#^thm-14-3|452 §14.3]]).
- **Coming later in the course.** Sard's theorem: the critical values of a smooth map have measure zero, so the theorem applies to almost every level set.
