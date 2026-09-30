---
subject: math
type: theorem
source: "[[Group Theory]]"
aliases: ["MATH 493 23.3", "group actions and homomorphisms to S_X"]
tags: [group-theory, hub]
---
![[§23 Actions#^thm-23-3]]

## Treated in
- [[§23 Actions#^thm-23-3|Theorem §23.3: Actions Are Homomorphisms to S_X]], in [[§23 Actions]]

## Its proof uses
- [[§3 Basic Examples of Groups#^def-3-5|Definition §3.5: Symmetric Groups S_X and Sₙ]]
- [[§15 Homomorphisms#^prop-15-1|Proposition §15.1: Homomorphisms Preserve Identity and Inverses]]
- [[§15 Homomorphisms#^def-15-1|Definition §15.1: Group Homomorphism]]
- [[§23 Actions#^def-23-1|Definition §23.1: Action; Right Action]]
- [[§23 Actions#^prop-23-2|Proposition §23.2: Each Group Element Acts Bijectively]]

## Used in (Group Theory)
- [[§23 Actions#^prop-23-4|Proposition §23.4: Faithful Actions Embed G in S_X]]
- [[§32 Conjugation as an Action and the Class Equation#^prop-32-1|Proposition §32.1: The Conjugation Action]]
- [[§36 Sources of Normal Subgroups#^thm-36-5|Theorem §36.5: A Normal Subgroup Inside a Subgroup of Finite Index]]
- [[§39 Simple Groups#^prop-39-10|Proposition §39.10: The Pair-Partition Homomorphism S_4 → S_3]]

## Connections
- **Used for.** Every action now yields a homomorphism whose kernel and image can be studied. Faithful actions embed G in S_X ([[§23 Actions#^prop-23-4|§23.4]]), which gives [[Cayley's Theorem]]. The action on G/H gives a normal subgroup inside H ([[§36 Sources of Normal Subgroups#^thm-36-5|§36.5]]), and the action of S₄ on pair partitions gives S₄/V ≅ S₃ ([[§39 Simple Groups#^prop-39-10|§39.10]]).
- **The identity axiom matters.** Without e ⋆ x = x the assignment g ↦ ĝ still respects products but need not land in S_X: the trivial group acting on {0, 1} by e ⋆ 0 = e ⋆ 1 = 0 ([[§23 Actions#^ex-23-1|Ex. §23.1]], [[§23 Actions#^rem-23-5|Why the Identity Axiom Matters]]).
- **Same idea elsewhere.** Replacing S_X by GL(V) gives a [[§19 Polynomial Rings, Permutation Matrices, and Representations#^def-19-6|representation]] (§19.6). S_n acting on kⁿ by permutation matrices is both at once ([[§19 Polynomial Rings, Permutation Matrices, and Representations#^prop-19-4|§19.4]]), and the conjugation action gives the [[Class Equation]].
- **Coming later in the course.** Representation theory studies homomorphisms G → GL_n(k), the linear version of this theorem.
