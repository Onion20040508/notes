---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 34.4", "I_p/I_p² ≅ T_p*M", "Lee Problem 11-4"]
tags: [differentiable-manifolds, hub]
---
![[§34 The Cotangent Space from Germs#^thm-34-4]]

## Treated in
- [[§34 The Cotangent Space from Germs#^thm-34-4|Theorem §34.4: The Cotangent Space from Germs]], in [[§34 The Cotangent Space from Germs]]

## Its proof uses
- [[§21 Linear Algebra Toolkit#^def-21-4|Definition §21.4: Bilinear Pairing]]
- [[§21 Linear Algebra Toolkit#^thm-21-5|Theorem §21.5: Non-Degenerate Pairings]]
- [[§28 Derivations and the Abstract Tangent Space#^lem-28-2|Lemma §28.2: First Properties of Derivations]]
- [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-5|Theorem §29.5: Basis Theorem]]
- [[§32 The Cotangent Space#^prop-32-2|Proposition §32.2: The Differential Evaluates Derivations]]
- [[§32 The Cotangent Space#^cor-32-3|Corollary §32.3: Properties of the Differential of a Function]]
- [[§33 Covectors in Coordinates#^lem-33-1|Lemma §33.1: The Differential in Coordinates]]
- [[§34 The Cotangent Space from Germs#^def-34-2|Definition §34.2: The Pairing Between Tangent Vectors and I_p/I_p²]]
- [[§34 The Cotangent Space from Germs#^prop-34-3|Proposition §34.3: The Pairing Is Well Defined and Non-Degenerate]]

## Used in (Differentiable Manifolds)
- [[§34 The Cotangent Space from Germs#^thm-34-5|Theorem §34.5: Dimension of the Cotangent Space]]
- [[§34 The Cotangent Space from Germs#^prop-34-7|Proposition §34.7: Pullback of Covectors from the Pullback of Germs]]

## Connections
- **What it gives.** T*_pM, defined as the dual (T_pM)*, also has a description with no dualizing: I_p/I_p², with the class of f going to df_p. So one could define the cotangent space first and the tangent space as its dual, the order Uribe called in some ways more natural ([[§29 Coordinate Derivations and the Basis Theorem#^rem-29-3|A Derivation Sees Only the First Derivatives]]). Lecture 15 recalled it when building the cotangent bundle ([[§48 The Cotangent Bundle#Lecture 15 and the Standard Coordinates|§48]]); the recap of covectors restates it ([[§46 Recap꞉ Covectors and the Four Differentials|§46]], Step 4).
- **What each ingredient does.** I_p² is exactly the set of germs vanishing to second order ([[§34 The Cotangent Space from Germs#^prop-34-1|§34.1]], via [[Hadamard's Lemma]]), so the quotient remembers first derivatives only. The pairing (D, class of f) ↦ D[f] is non-degenerate ([[§34 The Cotangent Space from Germs#^prop-34-3|§34.3]]), and [[Non-Degenerate Pairings]] turns that into the isomorphism, using finite dimension from the [[Basis Theorem for Tangent Spaces]]. Without finite dimension that step fails: V → V** is not onto when V is infinite-dimensional ([[§21 Linear Algebra Toolkit#^rem-21-2|§21, Remark]]).
- **Same idea elsewhere.** The linear algebra is LADR's quotient spaces ([[§11 Products and Quotients of Vector Spaces#^ladr-3-99|LADR 3.99]]) and dual bases ([[§12 Duality#^ladr-3-112|LADR 3.112]]): the classes of xⁱ − xⁱ(p) form a basis of I_p/I_p² ([[§34 The Cotangent Space from Germs#^prop-34-2|§34.2]]) and go to the dual basis dxⁱ|_p. A derivation kills I_p², so it descends to the quotient by the universal property of quotient spaces ([[§21 Linear Algebra Toolkit#^prop-21-6|§21.6]]), the linear twin of the [[Universal Property of Quotient Maps]].
- **One-forms.** A one-form picks an element of T*_pM at each point p, smoothly ([[§49 One-Forms#^def-49-1|Def. §49.1]]), and df is the first example ([[§49 One-Forms#^prop-49-2|§49.2]]). Higher-degree differential forms are still to come; on open subsets of ℝⁿ they are the k-forms of 452 ([[§36 Introduction to Differential Forms#^def-36-2|452 Def. §36.2]]).
