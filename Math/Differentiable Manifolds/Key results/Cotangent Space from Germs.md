---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 30.8", "I_p/I_p² ≅ T_p*M", "Lee Problem 11-4"]
tags: [differentiable-manifolds, hub]
---
![[§32 The Cotangent Space#^thm-32-8]]

## Treated in
- [[§32 The Cotangent Space#^thm-32-8|Theorem §32.8: The Cotangent Space from Germs]], in [[§32 The Cotangent Space]]

## Its proof uses
- [[§21 Linear Algebra Toolkit#^thm-21-5|Theorem §21.5: Non-Degenerate Pairings]]
- [[§28 Derivations and the Abstract Tangent Space#^lem-28-2|Lemma §28.2: First Properties of Derivations]]
- [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-5|Theorem §29.5: Basis Theorem]]
- [[§32 The Cotangent Space#^prop-32-1|Proposition §32.1: The Differential Evaluates Derivations]]
- [[§32 The Cotangent Space#^lem-32-2|Lemma §32.2: The Differential in Coordinates]]
- [[§32 The Cotangent Space#^def-32-4|Definition §32.4: The Pairing Between Tangent Vectors and I_p/I_p²]]
- [[§32 The Cotangent Space#^prop-32-7|Proposition §32.7: The Pairing Is Well Defined and Non-Degenerate]]

## Used in (Differentiable Manifolds)
- [[§32 The Cotangent Space#^thm-32-9|Theorem §32.9: Dimension of the Cotangent Space]]

## Connections
- **What it gives.** T*_pM, defined as the dual (T_pM)*, also has a description with no dualizing: I_p/I_p², with the class of f going to df_p. So one could define the cotangent space first and the tangent space as its dual, the order Uribe called in some ways more natural ([[§29 Coordinate Derivations and the Basis Theorem#^rem-29-3|A Derivation Sees Only the First Derivatives]]). Lecture 15 recalled it when building the cotangent bundle ([[§45 The Cotangent Bundle#Lecture 15 and the Standard Coordinates|§42]]); the recap of covectors restates it ([[§43 Recap꞉ Covectors and the Four Differentials|§43]], Step 4).
- **What each ingredient does.** I_p² is exactly the set of germs vanishing to second order ([[§32 The Cotangent Space#^prop-32-5|§32.5]], via [[Hadamard's Lemma]]), so the quotient remembers first derivatives only. The pairing (D, class of f) ↦ D[f] is non-degenerate ([[§32 The Cotangent Space#^prop-32-7|§32.7]]), and [[Non-Degenerate Pairings]] turns that into the isomorphism, using finite dimension from the [[Basis Theorem for Tangent Spaces]]. Without finite dimension that step fails: V → V** is not onto when V is infinite-dimensional ([[§21 Linear Algebra Toolkit#^rem-21-2|§20, Remark]]).
- **Same idea elsewhere.** The linear algebra is LADR's quotient spaces ([[§11 Products and Quotients of Vector Spaces#^ladr-3-99|LADR 3.99]]) and dual bases ([[§12 Duality#^ladr-3-112|LADR 3.112]]): the classes of xⁱ − xⁱ(p) form a basis of I_p/I_p² ([[§32 The Cotangent Space#^prop-32-6|§32.6]]) and go to the dual basis dxⁱ|_p. A derivation kills I_p², so it descends to the quotient by the universal property of quotient spaces ([[§21 Linear Algebra Toolkit#^prop-21-6|§21.6]]), the linear twin of the [[Universal Property of Quotient Maps]].
- **One-forms.** A one-form picks an element of T*_pM at each point p, smoothly ([[§46 One-Forms#^def-46-1|Def. §46.1]]), and df is the first example ([[§46 One-Forms#^prop-46-2|§46.2]]). Higher-degree differential forms are still to come; on open subsets of ℝⁿ they are the k-forms of 452 ([[§36 Introduction to Differential Forms#^def-36-2|452 Def. §36.2]]).
