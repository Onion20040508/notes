---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 4.3", "regular level sets are manifolds", "Lee Example 1.32", "Lee Corollary 5.14"]
tags: [differentiable-manifolds, hub]
---
![[§4 The Regular Value Theorem#^thm-4-3]]

## Treated in
- [[§4 The Regular Value Theorem#^thm-4-3|Theorem §4.3: Regular Value Theorem]], in [[§4 The Regular Value Theorem]]

## Its proof uses
- [[§2 Topological Manifolds#^prop-2-3|Proposition §2.3: Charts onto Open Subsets Suffice]]
- [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^prop-3-3|Proposition §3.3: Universal Property of the Subspace Topology]]
- [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^thm-3-5|Theorem §3.5: Subspaces Inherit Both Conditions]]
- [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^thm-3-10|Theorem §3.10: Universal Property of the Product]]
- [[§4 The Regular Value Theorem#^thm-4-1|Theorem §4.1: Implicit Function Theorem — Lee Theorem C.40]]
- [[§4 The Regular Value Theorem#^def-4-2|Definition §4.2: Regular Point and Regular Value]]

## Its proof uses (other subjects)
- [[3C Matrices#^ladr-3-57|LADR 3.57 Column rank equals row rank]]
- [[Multivariable Chain Rule]] (Multivariable Analysis)

## Used in (Differentiable Manifolds)
- [[§4 The Regular Value Theorem#^ex-4-2|Example §4.2: A Level Set in ℝ^4]]
- [[§4 The Regular Value Theorem#^cor-4-4|Corollary §4.4: Open Domains and Arbitrary Values]]
- [[§4 The Regular Value Theorem#^prop-4-5|Proposition §4.5: Regular Points When N le m]]
- [[§4 The Regular Value Theorem#^cor-4-7|Corollary §4.7: Holomorphic Regular Value Theorem]]
- [[§5 Topological Groups and Classical Matrix Groups#^cor-5-12|Corollary §5.12: Every Nonzero Value Is a Regular Value of det]]
- [[§5 Topological Groups and Classical Matrix Groups#^cor-5-13|Corollary §5.13: mathrmSL(n,ℝ) Is a Manifold of Dimension n² - 1]]
- [[§9 Manifolds in Euclidean Space#^thm-9-1|Theorem §9.1: The Two Descriptions Agree]]
- [[§9 Manifolds in Euclidean Space#^prop-9-2|Proposition §9.2: Regular Level Sets Are Smooth Manifolds]]
- [[§11 Tangent Spaces I꞉ The Geometric Picture#^thm-11-3|Theorem §11.3: The Geometric Tangent Space Is the Kernel of the Jacobian]]
- [[§11 Tangent Spaces I꞉ The Geometric Picture#^thm-11-7|Theorem §11.7: Preimages of Transverse Level Sets]]
- [[§11 Tangent Spaces I꞉ The Geometric Picture#^cor-11-9|Corollary §11.9: The Regular Value Theorem as a Special Case]]
- [[§11 Tangent Spaces I꞉ The Geometric Picture#^prop-11-10|Proposition §11.10: Transverse Intersections]]

## Connections
- **Used for.** SL(n,ℝ) and every det⁻¹(c) with c ≠ 0 ([[§5 Topological Groups and Classical Matrix Groups#^cor-5-12|§5.12]], [[§5 Topological Groups and Classical Matrix Groups#^cor-5-13|§5.13]]), the level set in ℝ⁴ of [[§4 The Regular Value Theorem#^ex-4-2|Ex. §4.2]], and holomorphic level sets of even real dimension ([[§4 The Regular Value Theorem#^cor-4-7|§4.7]]). Its smooth upgrade is [[Regular Level Sets Are Smooth Manifolds]], its tangent spaces are given by [[Geometric Tangent Space Is the Kernel of the Jacobian]], and it is the case S = {c} of the [[Transverse Preimage Theorem]] ([[§11 Tangent Spaces I꞉ The Geometric Picture#^cor-11-9|§11.9]]).
- **Where the hypothesis matters.** The rank must be full at every point of the level set, though it may drop elsewhere ([[§4 The Regular Value Theorem#^ex-4-1|Ex. §4.1]], [[§4 The Regular Value Theorem#^rem-4-6|§4, Remark]]). The unit sphere and the plane z = 1 meet only at the north pole, where their tangent planes coincide, and the intersection is a point instead of a curve ([[§11 Tangent Spaces I꞉ The Geometric Picture#^ex-11-5|Ex. §11.5]]). If N < m, the only regular level set is the empty one ([[§4 The Regular Value Theorem#^prop-4-5|§4.5]]).
- **Same idea elsewhere.** Each independent equation costs one dimension; for a linear map this is rank–nullity ([[Fundamental theorem of linear maps]]). Lagrange multipliers in 452 assume the same independence of the constraint gradients ([[§14 Optimization and Lagrange Multipliers#^thm-14-3|452 §14.3]]).
- **Coming later in the course.** Sard's theorem: the critical values of a smooth map have measure zero, so the theorem applies to almost every level set.
