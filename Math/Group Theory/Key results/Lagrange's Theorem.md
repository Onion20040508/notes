---
subject: math
type: theorem
source: "[[Group Theory]]"
aliases: ["MATH 493 29.2", "Lagrange"]
tags: [group-theory, hub]
---
![[§29 The Index and Lagrange's Theorem#^thm-29-2]]

## Treated in
- [[§29 The Index and Lagrange's Theorem#^thm-29-2|Theorem §29.2: Lagrange]], in [[§29 The Index and Lagrange's Theorem]]

## Its proof uses
- [[§28 Left and Right Cosets#^prop-28-2|Proposition §28.2: Cosets Are the Equivalence Classes]]
- [[§29 The Index and Lagrange's Theorem#^def-29-1|Definition §29.1: Index]]
- [[§29 The Index and Lagrange's Theorem#^prop-29-1|Proposition §29.1: All Cosets Have the Same Size]]

## Used in (Group Theory)
- [[§29 The Index and Lagrange's Theorem#^ex-29-1|Example §29.1: The Converse of Lagrange Fails: A_4]]
- [[§29 The Index and Lagrange's Theorem#^cor-29-3|Corollary §29.3: Order of an Element Divides ∣G∣; g^(∣G∣) = e]]
- [[§29 The Index and Lagrange's Theorem#^thm-29-7|Theorem §29.7: Groups of Prime Order]]
- [[§29 The Index and Lagrange's Theorem#^cor-29-8|Corollary §29.8: Groups of Prime Order Have No Proper Nontrivial Subgroups]]
- [[§30 Orbit–Stabilizer#^thm-30-3|Theorem §30.3: Orbit–Stabilizer]]
- [[§30 Orbit–Stabilizer#^cor-30-5|Corollary §30.5: Index of the Stabilizer]]
- [[§39 Sources of Normal Subgroups#^prop-39-6|Proposition §39.6: The Normal Core]]
- [[§40 Quotient Groups#^thm-40-1|Theorem §40.1: G/N Is a Group]]
- [[§41 The First and Second Isomorphism Theorems#^cor-41-8|Corollary §41.8: Index of an Intersection, Normal Case]]
- [[§43 Simple Groups#^prop-43-6|Proposition §43.6: A_5 Is Simple]]

## Connections
- **Used for.** ord(g) divides |G| and g^|G| = e ([[§29 The Index and Lagrange's Theorem#^cor-29-3|§29.3]]), hence [[§29 The Index and Lagrange's Theorem#^cor-29-4|Fermat's Little Theorem]]. Also [[Groups of Prime Order Are Cyclic]] and the [[Orbit–Stabilizer Theorem]]. It rules out subgroups, e.g. S₃ has none of order 4 or 5 ([[§29 The Index and Lagrange's Theorem#^rem-29-1|Uses of Lagrange]]), and together with class sizes it proves [[§43 Simple Groups#^prop-43-6|A₅ Is Simple]].
- **Index of an intersection.** For A ≤ G and H ≤ G of finite index, [A : A ∩ H] ≤ [G : H] ([[§29 The Index and Lagrange's Theorem#^prop-29-9|§29.9]]); it need not divide [G : H] ([[§29 The Index and Lagrange's Theorem#^ex-29-2|Ex. §29.2]]) unless H is normal, when Lagrange in G/H gives divisibility ([[§41 The First and Second Isomorphism Theorems#^cor-41-8|§41.8]]).
- **The converse fails.** |A₄| = 12 but A₄ has no subgroup of order 6 ([[§29 The Index and Lagrange's Theorem#^ex-29-1|Ex. §29.1]]). Only prime divisors are guaranteed, by [[§29 The Index and Lagrange's Theorem#^thm-29-6|Cauchy's Theorem]] ([[§29 The Index and Lagrange's Theorem#^rem-29-2|A Partial Converse to Lagrange]]).
- **Same idea elsewhere.** The 590 notes state it without proof ([[§26 Algebra Prerequisites꞉ Groups#^prop-26-1|590 Prop. §26.1]], part 3). For a subspace U of a finite vector space over 𝔽_p, |V| = |U| · |V/U| is Lagrange. Taking log_p gives dim V/U = dim V − dim U ([[§11 Products and Quotients of Vector Spaces#^ladr-3-105|LADR 3.105]]), as in [[§41 The First and Second Isomorphism Theorems#^rem-41-2|Rank–Nullity]].
- **Coming later in the course.** The Sylow theorems give a converse for prime powers: G has a subgroup of order pᵏ whenever pᵏ divides |G|.
- **Elementary instance in [[Logic and Proofs]]:** Gauss's proof of Fermat ([[§24★ Congruence Modulo a Prime#^rem-24-1|250 Remark §24.1]], one of three proofs of Fermat) splits the nonzero residues mod p into classes of equal size, which is this proof for the subgroup of powers of a; the order of a divides p − 1 there as [[§24★ Congruence Modulo a Prime#^prop-24-3|250 Prop. §24.3]].
