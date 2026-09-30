---
subject: math
type: theorem
source: "[[Group Theory]]"
aliases: ["MATH 493 23.5"]
tags: [group-theory, hub]
---
![[§23 Actions#^thm-23-5]]

## Treated in
- [[§23 Actions#^thm-23-5|Theorem §23.5: Cayley's Theorem]], in [[§23 Actions]]

## Its proof uses
- [[§23 Actions#^ex-23-2|Example §23.2: Actions]]
- [[§23 Actions#^def-23-3|Definition §23.3: Kernel of an Action; Faithful Action]]
- [[§23 Actions#^prop-23-4|Proposition §23.4: Faithful Actions Embed G in S_X]]

## Used in (Group Theory)
- [[§23 Actions#^cor-23-6|Corollary §23.6: Every Finite Group Is a Matrix Group]]

## Connections
- **Used for.** [[§23 Actions#^cor-23-6|Every Finite Group Is a Matrix Group]] (§23.6): compose G → S_n with permutation matrices ([[§19 Polynomial Rings, Permutation Matrices, and Representations#^prop-19-5|§19.5]]). So every finite group has a faithful representation.
- **Through the First Isomorphism Theorem.** Left multiplication has trivial kernel, so G ≅ G/{e} is isomorphic to its image in S_G ([[§38 The First Isomorphism Theorem#^rem-38-3|PS 3.1 and PS 3.2 as Instances]]). The same action on G/H instead of G gives the normal core of H ([[§36 Sources of Normal Subgroups#^thm-36-5|§36.5]], [[§36 Sources of Normal Subgroups#^prop-36-6|§36.6]]).
- **Inefficient.** A group of order n lands in S_n, of order n! ([[§23 Actions#^rem-23-7|Why Cayley's Theorem Matters]]). Smaller faithful actions are usually more useful. The rotation group of the cube has order 24, but acting on the 4 body diagonals it is ≅ S₄ ([[§30 Examples꞉ Linear Groups and the Cube#^thm-30-5|§30.5]]), which is far smaller than S₂₄.
- **Coming later in the course.** Representation theory looks for small faithful and irreducible representations G → GL_n(k), rather than the regular one.
