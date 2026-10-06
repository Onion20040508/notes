---
subject: math
type: theorem
source: "[[Group Theory]]"
aliases: ["MATH 493 25.3", "group actions and homomorphisms to S_X"]
tags: [group-theory, hub]
---
![[§25 Actions#^thm-25-3]]

## Treated in
- [[§25 Actions#^thm-25-3|Theorem §25.3: Actions Are Homomorphisms to S_X]], in [[§25 Actions]]

## Its proof uses
- [[§3 Basic Examples of Groups#^def-3-5|Definition §3.5: Symmetric Groups S_X and Sₙ]]
- [[§15 Homomorphisms#^def-15-1|Definition §15.1: Group Homomorphism]]
- [[§15 Homomorphisms#^prop-15-1|Proposition §15.1: Homomorphisms Preserve Identity and Inverses]]
- [[§25 Actions#^def-25-1|Definition §25.1: Action; Right Action]]
- [[§25 Actions#^prop-25-2|Proposition §25.2: Each Group Element Acts Bijectively]]

## Used in (Group Theory)
- [[§25 Actions#^prop-25-4|Proposition §25.4: Faithful Actions Embed G in S_X]]
- [[§34 Conjugation as an Action and the Class Equation#^prop-34-1|Proposition §34.1: The Conjugation Action]]
- [[§39 Sources of Normal Subgroups#^thm-39-5|Theorem §39.5: A Normal Subgroup Inside a Subgroup of Finite Index]]
- [[§43 Simple Groups#^prop-43-10|Proposition §43.10: The Pair-Partition Homomorphism S_4 → S_3]]

## Connections
- **Used for.** Every action now yields a homomorphism whose kernel and image can be studied. Faithful actions embed G in S_X ([[§25 Actions#^prop-25-4|§25.4]]), which gives [[Cayley's Theorem]]. The action on G/H gives a normal subgroup inside H ([[§39 Sources of Normal Subgroups#^thm-39-5|§39.5]]), and the action of S₄ on pair partitions gives S₄/V ≅ S₃ ([[§43 Simple Groups#^prop-43-10|§43.10]]).
- **The identity axiom matters.** Without e ⋆ x = x the assignment g ↦ ĝ still respects products but need not land in S_X: the trivial group acting on {0, 1} by e ⋆ 0 = e ⋆ 1 = 0 ([[§25 Actions#^ex-25-1|Ex. §25.1]], [[§25 Actions#^rem-25-5|Why the Identity Axiom Matters]]).
- **Same idea elsewhere.** Replacing S_X by GL(V) gives a [[§20 Polynomial Rings, Permutation Matrices, and Representations#^def-20-7|representation]] (Def. §20.7). S_n acting on kⁿ by permutation matrices is both at once ([[§20 Polynomial Rings, Permutation Matrices, and Representations#^prop-20-4|§20.4]]), and the conjugation action gives the [[Class Equation]]. For a continuous action of a [[§11 Topological Groups and Classical Matrix Groups#^def-11-1|topological group]] (591 Def. §10.1) each translation is a homeomorphism with inverse the translation by the inverse ([[§13 Group Actions and Orbit Spaces#^lem-13-2|591 Lemma §13.2]]), so the homomorphism lands in the homeomorphisms of X.
- **Coming later in the course.** Representation theory studies homomorphisms G → GL_n(k), the linear version of this theorem.
