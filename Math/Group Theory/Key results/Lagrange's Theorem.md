---
subject: math
type: theorem
source: "[[Group Theory]]"
aliases: ["MATH 493 27.2", "Lagrange"]
tags: [group-theory, hub]
---
![[Group Theory §27 The Index and Lagrange's Theorem#^thm-27-2]]

## Treated in
- [[Group Theory §27 The Index and Lagrange's Theorem#^thm-27-2|Theorem §27.2: Lagrange]], in [[Group Theory §27 The Index and Lagrange's Theorem]]

## Its proof uses
- [[Group Theory §26 Left and Right Cosets#^prop-26-2|Proposition §26.2: Cosets Are the Equivalence Classes]]
- [[Group Theory §27 The Index and Lagrange's Theorem#^def-27-1|Definition §27.1: Index]]
- [[Group Theory §27 The Index and Lagrange's Theorem#^prop-27-1|Proposition §27.1: All Cosets Have the Same Size]]

## Used in (Group Theory)
- [[Group Theory §27 The Index and Lagrange's Theorem#^ex-27-1|Example §27.1: The Converse of Lagrange Fails: A_4]]
- [[Group Theory §27 The Index and Lagrange's Theorem#^cor-27-3|Corollary §27.3: Order of an Element Divides ∣G∣; g^∣G∣ = e]]
- [[Group Theory §27 The Index and Lagrange's Theorem#^thm-27-7|Theorem §27.7: Groups of Prime Order]]
- [[Group Theory §27 The Index and Lagrange's Theorem#^cor-27-8|Corollary §27.8: Groups of Prime Order Have No Proper Nontrivial Subgroups]]
- [[Group Theory §28 Orbit–Stabilizer#^thm-28-3|Theorem §28.3: Orbit–Stabilizer]]
- [[Group Theory §28 Orbit–Stabilizer#^cor-28-5|Corollary §28.5: Index of the Stabilizer]]
- [[Group Theory §32 Conjugation as an Action and the Class Equation#^prop-32-6|Proposition §32.6: Groups of Order 4 Are Abelian]]
- [[Group Theory §36 Sources of Normal Subgroups#^ex-36-1|Example §36.1: Index-2 Examples]]
- [[Group Theory §36 Sources of Normal Subgroups#^prop-36-6|Proposition §36.6: The Normal Core]]
- [[Group Theory §37 Quotient Groups#^thm-37-1|Theorem §37.1: G/N Is a Group]]
- [[Group Theory §38 The First Isomorphism Theorem#^ex-38-1|Example §38.1: The First Isomorphism Theorem in Action]]
- [[Group Theory §39 Simple Groups#^prop-39-6|Proposition §39.6: A_5 Is Simple]]

## Connections
- **Used for.** ord(g) divides |G| and g^|G| = e ([[Group Theory §27 The Index and Lagrange's Theorem#^cor-27-3|§27.3]]), hence [[Group Theory §27 The Index and Lagrange's Theorem#^cor-27-4|Fermat's Little Theorem]]. Also [[Groups of Prime Order Are Cyclic]] and the [[Orbit–Stabilizer Theorem]]. It rules out subgroups, e.g. S₃ has none of order 4 or 5 ([[Group Theory §27 The Index and Lagrange's Theorem#^rem-27-1|Uses of Lagrange]]), and together with class sizes it proves [[Group Theory §39 Simple Groups#^prop-39-6|A₅ Is Simple]].
- **The converse fails.** |A₄| = 12 but A₄ has no subgroup of order 6 ([[Group Theory §27 The Index and Lagrange's Theorem#^ex-27-1|Ex. §27.1]]). Only prime divisors are guaranteed, by [[Group Theory §27 The Index and Lagrange's Theorem#^thm-27-6|Cauchy's Theorem]] ([[Group Theory §27 The Index and Lagrange's Theorem#^rem-27-2|A Partial Converse to Lagrange]]).
- **Same idea elsewhere.** The 590 notes state it without proof ([[Topology §21 Algebra Prerequisites꞉ Groups#^prop-21-1|590 §21.1]], part 3). For a subspace U of a finite vector space over 𝔽_p, |V| = |U| · |V/U| is Lagrange. Taking log_p gives dim V/U = dim V − dim U ([[Linear Algebra 3E Products and Quotients of Vector Spaces#^ladr-3-105|LADR 3.105]]), as in [[Group Theory §38 The First Isomorphism Theorem#^rem-38-2|Rank–Nullity]].
- **Coming later in the course.** The Sylow theorems give a converse for prime powers: G has a subgroup of order pᵏ whenever pᵏ divides |G|.
