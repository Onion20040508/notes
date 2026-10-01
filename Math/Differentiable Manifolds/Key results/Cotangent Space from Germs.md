---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 13.7", "I_p/I_p² ≅ T_p*M", "Lee Problem 11-4"]
tags: [differentiable-manifolds, hub]
---
![[§13 Tangent Spaces III꞉ The Cotangent Space#^thm-13-7]]

## Treated in
- [[§13 Tangent Spaces III꞉ The Cotangent Space#^thm-13-7|Theorem §13.7: The Cotangent Space from Germs]], in [[§13 Tangent Spaces III꞉ The Cotangent Space]]

## Its proof uses
- [[§10 Vector Spaces and Matrix Groups#^thm-10-5|Theorem §10.5: Non-Degenerate Pairings]]
- [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^lem-12-6|Lemma §12.6: First Properties of Derivations]]
- [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^thm-12-16|Theorem §12.16: Basis Theorem]]
- [[§13 Tangent Spaces III꞉ The Cotangent Space#^prop-13-1|Proposition §13.1: The Differential Evaluates Derivations]]
- [[§13 Tangent Spaces III꞉ The Cotangent Space#^lem-13-2|Lemma §13.2: The Differential in Coordinates]]
- [[§13 Tangent Spaces III꞉ The Cotangent Space#^def-13-3|Definition §13.3: The Pairing Between Tangent Vectors and I_p/I_p²]]
- [[§13 Tangent Spaces III꞉ The Cotangent Space#^prop-13-6|Proposition §13.6: The Pairing Is Well Defined and Non-Degenerate]]

## Used in (Differentiable Manifolds)
- (not cited later in the course)

## Connections
- **What it gives.** T*_pM, defined as the dual (T_pM)*, also has a description with no dualizing: I_p/I_p², with the class of f going to df_p. So one could define the cotangent space first and the tangent space as its dual, the order Uribe called in some ways more natural ([[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^rem-12-10|A Derivation Sees Only the First Derivatives]]). It is not cited later in the course.
- **What each ingredient does.** I_p² is exactly the set of germs vanishing to second order ([[§13 Tangent Spaces III꞉ The Cotangent Space#^prop-13-4|§13.4]], via [[Hadamard's Lemma]]), so the quotient remembers first derivatives only. The pairing (D, class of f) ↦ D[f] is non-degenerate ([[§13 Tangent Spaces III꞉ The Cotangent Space#^prop-13-6|§13.6]]), and [[Non-Degenerate Pairings]] turns that into the isomorphism, using finite dimension from the [[Basis Theorem for Tangent Spaces]]. Without finite dimension that step fails: V → V** is not onto when V is infinite-dimensional ([[§10 Vector Spaces and Matrix Groups#^rem-10-2|§10, Remark]]).
- **Same idea elsewhere.** The linear algebra is LADR's quotient spaces ([[§11 Products and Quotients of Vector Spaces#^ladr-3-99|LADR 3.99]]) and dual bases ([[§12 Duality#^ladr-3-112|LADR 3.112]]): the classes of xⁱ − xⁱ(p) form a basis of I_p/I_p² ([[§13 Tangent Spaces III꞉ The Cotangent Space#^prop-13-5|§13.5]]) and go to the dual basis dxⁱ|_p. A derivation kills I_p², so it descends to the quotient by the universal property of quotient spaces ([[§10 Vector Spaces and Matrix Groups#^prop-10-6|§10.6]]), the linear twin of the [[Universal Property of Quotient Maps]].
- **Coming later in the course.** Differential forms are built from covectors: a 1-form picks an element of T*_pM at each point p, and df is the first example.
