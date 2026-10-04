---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 11.6", "SL O SO U are manifolds", "Lee Example 1.27", "Lee Example 7.27"]
tags: [differentiable-manifolds, hub]
---
![[§11 The Classical Groups Are Topological Manifolds#^thm-11-6]]

## Treated in
- [[§11 The Classical Groups Are Topological Manifolds#^thm-11-6|Theorem §11.6: Classical Groups Are Manifolds]], in [[§11 The Classical Groups Are Topological Manifolds]]

## Its proof uses
- [[§3 Subspaces and Products#^thm-3-5|Theorem §3.5: Subspaces Inherit Both Conditions]]
- [[§3 Subspaces and Products#^prop-3-6|Proposition §3.6: Open Subsets of Manifolds Are Manifolds]]
- [[§11 The Classical Groups Are Topological Manifolds#^cor-11-5|Corollary §11.5: SL(n,ℝ) Is a Manifold of Dimension n² − 1]]
- [[§22 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-22-1|Example §22.1: O(n) Is a Smooth Manifold of Dimension n(n-1)/2]]
- [[§22 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-22-2|Example §22.2: U(n) Is a Smooth Manifold of Dimension n²]]
- [[§23 Tangent Spaces I꞉ The Geometric Picture#^thm-23-5|Theorem §23.5: The Classical Groups]]

## Used in (Differentiable Manifolds)
- [[§23 Tangent Spaces I꞉ The Geometric Picture#^thm-23-5|Theorem §23.5: The Classical Groups]]

## Connections
- **Used for.** These are the groups whose actions build the quotient manifolds: ℂPⁿ = S²ⁿ⁺¹/U(1) ([[§12 Group Actions and Orbit Spaces#^ex-12-3|Ex. §12.3]]), S² ≅ SO(3)/SO(2) ([[§13 Homogeneous Spaces#^ex-13-3|Ex. §13.3]]) and the Grassmannians O(n)/(O(k) × O(n − k)) ([[§14 The Topology of G∕H and Real Grassmannians#^cor-14-8|§14.8]]). Their dimensions and tangent spaces at I are tabulated in [[§23 Tangent Spaces I꞉ The Geometric Picture#^thm-23-5|§23.5]], which lets dim G/H = dim G − dim H be checked in examples ([[§23 Tangent Spaces I꞉ The Geometric Picture#^rem-23-9|Dimension Checks through Homogeneous Spaces]]).
- **How, and what can go wrong.** GL is open in matrix space; SL, O and U are regular level sets ([[Regular Value Theorem (Euclidean)]], [[Regular Level Sets Are Smooth Manifolds]]), for SL via [[Jacobi's Formula]]. The codomain must be chosen right: gg^T lands in Sym(n), and with Mat(n) as codomain I would be a regular value nowhere ([[§22 The Orthogonal and Unitary Groups as Smooth Manifolds#^rem-22-1|§22, Remark]]). U(n) has to be done over ℝ, since gg* is not holomorphic, and dim U(n) = n² can be odd ([[§22 The Orthogonal and Unitary Groups as Smooth Manifolds#^rem-22-5|Why over ℝ]]).
- **Same idea elsewhere.** The groups themselves are in 493 ([[Matrix groups GLₙ, SLₙ and O(n)]]), where SL_n is the kernel of det ([[§15 Homomorphisms#^ex-15-1|493 Ex. §15.1]]). O(n) is the group of isometries of ℝⁿ ([[§25 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-49|LADR 7.49]]). GL(n,ℝ) is disconnected because det maps it continuously onto ℝ ∖ {0} ([[§15 Example꞉ The Classical Groups#^prop-15-1|§15.1]], [[Continuous Image of a Connected Space is Connected]]).
- **Coming later in the course.** These are the basic examples of Lie groups, and their tangent spaces at I (trace-zero, skew-symmetric and skew-Hermitian matrices) will be their Lie algebras.
