---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 5.8", "SL O SO U are manifolds"]
tags: [differentiable-manifolds, hub]
---
![[§5 Topological Groups and Classical Matrix Groups#^thm-5-8]]

## Treated in
- [[§5 Topological Groups and Classical Matrix Groups#^thm-5-8|Theorem §5.8: Classical Groups Are Manifolds]], in [[§5 Topological Groups and Classical Matrix Groups]]

## Its proof uses
- [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^thm-3-5|Theorem §3.5: Subspaces Inherit Both Conditions]]
- [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^prop-3-6|Proposition §3.6: Open Subsets of Manifolds Are Manifolds]]
- [[§5 Topological Groups and Classical Matrix Groups#^cor-5-13|Corollary §5.13: mathrmSL(n,ℝ) Is a Manifold of Dimension n² - 1]]
- [[§10 Vector Spaces and Matrix Groups#^ex-10-1|Example §10.1: mathrmO(n) Is a Smooth Manifold of Dimension tfracn(n-1)2]]
- [[§10 Vector Spaces and Matrix Groups#^ex-10-2|Example §10.2: mathrmU(n) Is a Smooth Manifold of Dimension n²]]
- [[§11 Tangent Spaces I꞉ The Geometric Picture#^thm-11-5|Theorem §11.5: The Classical Groups]]

## Used in (Differentiable Manifolds)
- [[§11 Tangent Spaces I꞉ The Geometric Picture#^thm-11-5|Theorem §11.5: The Classical Groups]]

## Connections
- **Used for.** These are the groups whose actions build the quotient manifolds: ℂPⁿ = S²ⁿ⁺¹/U(1) ([[§6 Group Actions and Orbit Spaces#^ex-6-3|Ex. §6.3]]), S² ≅ SO(3)/SO(2) ([[§7 Homogeneous Spaces#^ex-7-3|Ex. §7.3]]) and the Grassmannians O(n)/(O(k) × O(n − k)) ([[§7 Homogeneous Spaces#^cor-7-13|§7.13]]). Their dimensions and tangent spaces at I are tabulated in [[§11 Tangent Spaces I꞉ The Geometric Picture#^thm-11-5|§11.5]], which lets dim G/H = dim G − dim H be checked in examples ([[§11 Tangent Spaces I꞉ The Geometric Picture#^rem-11-9|Dimension Checks through Homogeneous Spaces]]).
- **How, and what can go wrong.** GL is open in matrix space; SL, O and U are regular level sets ([[Regular Value Theorem (Euclidean)]], [[Regular Level Sets Are Smooth Manifolds]]), for SL via [[Jacobi's Formula]]. The codomain must be chosen right: gg^T lands in Sym(n), and with Mat(n) as codomain I would be a regular value nowhere ([[§10 Vector Spaces and Matrix Groups#^rem-10-7|§10, Remark]]). U(n) has to be done over ℝ, since gg* is not holomorphic, and dim U(n) = n² can be odd ([[§10 Vector Spaces and Matrix Groups#^rem-10-11|Why over ℝ]]).
- **Same idea elsewhere.** The groups themselves are in 493 ([[Matrix groups GLₙ, SLₙ and O(n)]]), where SL_n is the kernel of det ([[§15 Homomorphisms#^ex-15-1|493 Ex. §15.1]]). O(n) is the group of isometries of ℝⁿ ([[7D Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-49|LADR 7.49]]). GL(n,ℝ) is disconnected because det maps it continuously onto ℝ ∖ {0} ([[§5 Topological Groups and Classical Matrix Groups#^prop-5-5|§5.5]], [[Continuous Image of a Connected Space is Connected]]).
- **Coming later in the course.** These are the basic examples of Lie groups, and their tangent spaces at I (trace-zero, skew-symmetric and skew-Hermitian matrices) will be their Lie algebras.
