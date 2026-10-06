---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 30.8", "I_p/I_p² ≅ T_p*M", "Lee Problem 11-4"]
tags: [differentiable-manifolds, hub]
---
![[§30 The Cotangent Space#^thm-30-8]]

## Treated in
- [[§30 The Cotangent Space#^thm-30-8|Theorem §30.8: The Cotangent Space from Germs]], in [[§30 The Cotangent Space]]

## Its proof uses
- [[§20 Linear Algebra Toolkit#^thm-20-5|Theorem §20.5: Non-Degenerate Pairings]]
- [[§26 Derivations and the Abstract Tangent Space#^lem-26-2|Lemma §26.2: First Properties of Derivations]]
- [[§27 Coordinate Derivations and the Basis Theorem#^thm-27-5|Theorem §27.5: Basis Theorem]]
- [[§30 The Cotangent Space#^prop-30-1|Proposition §30.1: The Differential Evaluates Derivations]]
- [[§30 The Cotangent Space#^lem-30-2|Lemma §30.2: The Differential in Coordinates]]
- [[§30 The Cotangent Space#^def-30-4|Definition §30.4: The Pairing Between Tangent Vectors and I_p/I_p²]]
- [[§30 The Cotangent Space#^prop-30-7|Proposition §30.7: The Pairing Is Well Defined and Non-Degenerate]]

## Used in (Differentiable Manifolds)
- [[§30 The Cotangent Space#^thm-30-9|Theorem §30.9: Dimension of the Cotangent Space]]

## Connections
- **What it gives.** T*_pM, defined as the dual (T_pM)*, also has a description with no dualizing: I_p/I_p², with the class of f going to df_p. So one could define the cotangent space first and the tangent space as its dual, the order Uribe called in some ways more natural ([[§27 Coordinate Derivations and the Basis Theorem#^rem-27-3|A Derivation Sees Only the First Derivatives]]). Lecture 15 recalled it when building the cotangent bundle ([[§42 The Cotangent Bundle#Lecture 15 and the Standard Coordinates|§42]]); the recap of covectors restates it ([[§40 Recap꞉ Covectors and the Four Differentials|§40]], Step 4).
- **What each ingredient does.** I_p² is exactly the set of germs vanishing to second order ([[§30 The Cotangent Space#^prop-30-5|§30.5]], via [[Hadamard's Lemma]]), so the quotient remembers first derivatives only. The pairing (D, class of f) ↦ D[f] is non-degenerate ([[§30 The Cotangent Space#^prop-30-7|§30.7]]), and [[Non-Degenerate Pairings]] turns that into the isomorphism, using finite dimension from the [[Basis Theorem for Tangent Spaces]]. Without finite dimension that step fails: V → V** is not onto when V is infinite-dimensional ([[§20 Linear Algebra Toolkit#^rem-20-2|§20, Remark]]).
- **Same idea elsewhere.** The linear algebra is LADR's quotient spaces ([[§11 Products and Quotients of Vector Spaces#^ladr-3-99|LADR 3.99]]) and dual bases ([[§12 Duality#^ladr-3-112|LADR 3.112]]): the classes of xⁱ − xⁱ(p) form a basis of I_p/I_p² ([[§30 The Cotangent Space#^prop-30-6|§30.6]]) and go to the dual basis dxⁱ|_p. A derivation kills I_p², so it descends to the quotient by the universal property of quotient spaces ([[§20 Linear Algebra Toolkit#^prop-20-6|§20.6]]), the linear twin of the [[Universal Property of Quotient Maps]].
- **One-forms.** A one-form picks an element of T*_pM at each point p, smoothly ([[§43 One-Forms#^def-43-1|Def. §43.1]]), and df is the first example ([[§43 One-Forms#^prop-43-2|§43.2]]). Higher-degree differential forms are still to come; on open subsets of ℝⁿ they are the k-forms of 452 ([[§21 Introduction to Differential Forms#^def-21-new1|452 Def. §21.1]]).
