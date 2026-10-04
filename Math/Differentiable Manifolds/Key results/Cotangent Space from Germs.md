---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 27.7", "I_p/I_p² ≅ T_p*M", "Lee Problem 11-4"]
tags: [differentiable-manifolds, hub]
---
![[§27 Tangent Spaces III꞉ The Cotangent Space#^thm-27-7]]

## Treated in
- [[§27 Tangent Spaces III꞉ The Cotangent Space#^thm-27-7|Theorem §27.7: The Cotangent Space from Germs]], in [[§27 Tangent Spaces III꞉ The Cotangent Space]]

## Its proof uses
- [[§17 Linear Algebra Toolkit#^thm-17-5|Theorem §17.5: Non-Degenerate Pairings]]
- [[§23 Derivations and the Abstract Tangent Space#^lem-23-2|Lemma §23.2: First Properties of Derivations]]
- [[§24 Coordinate Derivations and the Basis Theorem#^thm-24-5|Theorem §24.5: Basis Theorem]]
- [[§27 Tangent Spaces III꞉ The Cotangent Space#^prop-27-1|Proposition §27.1: The Differential Evaluates Derivations]]
- [[§27 Tangent Spaces III꞉ The Cotangent Space#^lem-27-2|Lemma §27.2: The Differential in Coordinates]]
- [[§27 Tangent Spaces III꞉ The Cotangent Space#^def-27-3|Definition §27.3: The Pairing Between Tangent Vectors and I_p/I_p²]]
- [[§27 Tangent Spaces III꞉ The Cotangent Space#^prop-27-6|Proposition §27.6: The Pairing Is Well Defined and Non-Degenerate]]

## Used in (Differentiable Manifolds)
- [[§27 Tangent Spaces III꞉ The Cotangent Space#^thm-27-8|Theorem §27.8: Dimension of the Cotangent Space]]

## Connections
- **What it gives.** T*_pM, defined as the dual (T_pM)*, also has a description with no dualizing: I_p/I_p², with the class of f going to df_p. So one could define the cotangent space first and the tangent space as its dual, the order Uribe called in some ways more natural ([[§24 Coordinate Derivations and the Basis Theorem#^rem-24-3|A Derivation Sees Only the First Derivatives]]). It is not cited later in the course.
- **What each ingredient does.** I_p² is exactly the set of germs vanishing to second order ([[§27 Tangent Spaces III꞉ The Cotangent Space#^prop-27-4|§27.4]], via [[Hadamard's Lemma]]), so the quotient remembers first derivatives only. The pairing (D, class of f) ↦ D[f] is non-degenerate ([[§27 Tangent Spaces III꞉ The Cotangent Space#^prop-27-6|§27.6]]), and [[Non-Degenerate Pairings]] turns that into the isomorphism, using finite dimension from the [[Basis Theorem for Tangent Spaces]]. Without finite dimension that step fails: V → V** is not onto when V is infinite-dimensional ([[§17 Linear Algebra Toolkit#^rem-17-2|§17, Remark]]).
- **Same idea elsewhere.** The linear algebra is LADR's quotient spaces ([[§11 Products and Quotients of Vector Spaces#^ladr-3-99|LADR 3.99]]) and dual bases ([[§12 Duality#^ladr-3-112|LADR 3.112]]): the classes of xⁱ − xⁱ(p) form a basis of I_p/I_p² ([[§27 Tangent Spaces III꞉ The Cotangent Space#^prop-27-5|§27.5]]) and go to the dual basis dxⁱ|_p. A derivation kills I_p², so it descends to the quotient by the universal property of quotient spaces ([[§17 Linear Algebra Toolkit#^prop-17-6|§17.6]]), the linear twin of the [[Universal Property of Quotient Maps]].
- **Coming later in the course.** Differential forms are built from covectors: a 1-form picks an element of T*_pM at each point p, and df is the first example.
