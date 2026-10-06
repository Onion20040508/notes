---
subject: math
type: theorem
source: "[[Group Theory]]"
aliases: ["MATH 493 25.5"]
tags: [group-theory, hub]
---
![[§25 Actions#^thm-25-5]]

## Treated in
- [[§25 Actions#^thm-25-5|Theorem §25.5: Cayley's Theorem]], in [[§25 Actions]]

## Its proof uses
- [[§25 Actions#^ex-25-2|Example §25.2: Actions]]
- [[§25 Actions#^prop-25-4|Proposition §25.4: Faithful Actions Embed G in S_X]]
- [[§25 Actions#^def-25-5|Definition §25.5: Faithful Action]]

## Used in (Group Theory)
- [[§25 Actions#^cor-25-6|Corollary §25.6: Every Finite Group Is a Matrix Group]]

## Connections
- **Used for.** [[§25 Actions#^cor-25-6|Every Finite Group Is a Matrix Group]] (§25.6): compose G → S_n with permutation matrices ([[§20 Polynomial Rings, Permutation Matrices, and Representations#^prop-20-5|§20.5]]). So every finite group has a faithful representation.
- **Through the First Isomorphism Theorem.** Left multiplication has trivial kernel, so G ≅ G/{e} is isomorphic to its image in S_G ([[§41 The First and Second Isomorphism Theorems#^rem-41-3|PS 3.1 and PS 3.2 as Instances]]). The same action on G/H instead of G gives the normal core of H ([[§39 Sources of Normal Subgroups#^thm-39-5|§39.5]], [[§39 Sources of Normal Subgroups#^prop-39-6|§39.6]]).
- **Inefficient.** A group of order n lands in S_n, of order n! ([[§25 Actions#^rem-25-7|Why Cayley's Theorem Matters]]). Smaller faithful actions are usually more useful. The rotation group of the cube has order 24, but acting on the 4 body diagonals it is ≅ S₄ ([[§32 Linear Groups, the Cube, S₃ and A₄#^thm-32-5|§32.5]]), which is far smaller than S₂₄.
- **Coming later in the course.** Representation theory looks for small faithful and irreducible representations G → GL_n(k), rather than the regular one.
