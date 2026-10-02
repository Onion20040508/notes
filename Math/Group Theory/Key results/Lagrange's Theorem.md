---
subject: math
type: theorem
source: "[[Group Theory]]"
aliases: ["MATH 493 27.2", "Lagrange"]
tags: [group-theory, hub]
---
![[§27 The Index and Lagrange's Theorem#^thm-27-2]]

## Treated in
- [[§27 The Index and Lagrange's Theorem#^thm-27-2|Theorem §27.2: Lagrange]], in [[§27 The Index and Lagrange's Theorem]]

## Its proof uses
- [[§26 Left and Right Cosets#^prop-26-2|Proposition §26.2: Cosets Are the Equivalence Classes]]
- [[§27 The Index and Lagrange's Theorem#^prop-27-1|Proposition §27.1: All Cosets Have the Same Size]]
- [[§27 The Index and Lagrange's Theorem#^def-27-1|Definition §27.1: Index]]

## Used in (Group Theory)
- [[§27 The Index and Lagrange's Theorem#^ex-27-1|Example §27.1: The Converse of Lagrange Fails: A_4]]
- [[§27 The Index and Lagrange's Theorem#^cor-27-3|Corollary §27.3: Order of an Element Divides ∣G∣; g^(∣G∣) = e]]
- [[§27 The Index and Lagrange's Theorem#^thm-27-7|Theorem §27.7: Groups of Prime Order]]
- [[§27 The Index and Lagrange's Theorem#^cor-27-8|Corollary §27.8: Groups of Prime Order Have No Proper Nontrivial Subgroups]]
- [[§28 Orbit–Stabilizer#^thm-28-3|Theorem §28.3: Orbit–Stabilizer]]
- [[§28 Orbit–Stabilizer#^cor-28-5|Corollary §28.5: Index of the Stabilizer]]
- [[§36 Sources of Normal Subgroups#^ex-36-1|Example §36.1: Index-2 Examples]]
- [[§36 Sources of Normal Subgroups#^prop-36-6|Proposition §36.6: The Normal Core]]
- [[§37 Quotient Groups#^thm-37-1|Theorem §37.1: G/N Is a Group]]
- [[§38 The First Isomorphism Theorem#^ex-38-1|Example §38.1: The First Isomorphism Theorem in Action]]
- [[§40 Simple Groups#^prop-40-6|Proposition §40.6: A_5 Is Simple]]

## Connections
- **Used for.** ord(g) divides |G| and g^|G| = e ([[§27 The Index and Lagrange's Theorem#^cor-27-3|§27.3]]), hence [[§27 The Index and Lagrange's Theorem#^cor-27-4|Fermat's Little Theorem]]. Also [[Groups of Prime Order Are Cyclic]] and the [[Orbit–Stabilizer Theorem]]. It rules out subgroups, e.g. S₃ has none of order 4 or 5 ([[§27 The Index and Lagrange's Theorem#^rem-27-1|Uses of Lagrange]]), and together with class sizes it proves [[§40 Simple Groups#^prop-40-6|A₅ Is Simple]].
- **The converse fails.** |A₄| = 12 but A₄ has no subgroup of order 6 ([[§27 The Index and Lagrange's Theorem#^ex-27-1|Ex. §27.1]]). Only prime divisors are guaranteed, by [[§27 The Index and Lagrange's Theorem#^thm-27-6|Cauchy's Theorem]] ([[§27 The Index and Lagrange's Theorem#^rem-27-2|A Partial Converse to Lagrange]]).
- **Same idea elsewhere.** The 590 notes state it without proof ([[§21 Algebra Prerequisites꞉ Groups#^prop-21-1|590 §21.1]], part 3). For a subspace U of a finite vector space over 𝔽_p, |V| = |U| · |V/U| is Lagrange. Taking log_p gives dim V/U = dim V − dim U ([[§11 Products and Quotients of Vector Spaces#^ladr-3-105|LADR 3.105]]), as in [[§38 The First Isomorphism Theorem#^rem-38-2|Rank–Nullity]].
- **Coming later in the course.** The Sylow theorems give a converse for prime powers: G has a subgroup of order pᵏ whenever pᵏ divides |G|.
- **Elementary instance in [[Logic and Proofs]]:** Gauss's proof of Fermat ([[§24★ Congruence Modulo a Prime#^rem-24-1|250 Remark §24.1]], one of three proofs of Fermat) splits the nonzero residues mod p into classes of equal size, which is this proof for the subgroup of powers of a; the order of a divides p − 1 there as [[§24★ Congruence Modulo a Prime#^prop-24-3|250 Prop. §24.3]].
