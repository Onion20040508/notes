---
subject: math
type: theorem
source: "[[Group Theory]]"
aliases: ["MATH 493 40.1", "G/N is a group"]
tags: [group-theory, hub]
---
![[§40 Quotient Groups#^thm-40-1]]

## Treated in
- [[§40 Quotient Groups#^thm-40-1|Theorem §40.1: G/N Is a Group]], in [[§40 Quotient Groups]]

## Its proof uses
- [[§1 The Definition of a Group#^def-1-1|Definition §1.1: Group]]
- [[§29 The Index and Lagrange's Theorem#^def-29-1|Definition §29.1: Index]]
- [[§29 The Index and Lagrange's Theorem#^thm-29-2|Theorem §29.2: Lagrange]]
- [[§37 Multiplying Cosets#^prop-37-1|Proposition §37.1: When Coset Multiplication Is Well Defined]]

## Used in (Group Theory)
- [[§40 Quotient Groups#^prop-40-2|Proposition §40.2: Every Normal Subgroup Is a Kernel]]
- [[§41 The First and Second Isomorphism Theorems#^cor-41-2|Corollary §41.2: ∣G∣ = ∣Keralpha∣ · ∣Imalpha∣]]
- [[§47 Commutators#^prop-47-6|Proposition §47.6: The Abelianization Is Abelian]]

## Connections
- **Normality is needed.** Coset multiplication is well defined exactly when gHg⁻¹ ⊆ H ([[§37 Multiplying Cosets#^prop-37-1|§37.1]]). For H = {e, (1 2)} in S₃ it is not ([[§38 Normal Subgroups#^ex-38-1|Ex. §38.1]], [[Characterizations of Normality]]). The lecture's second proof that coset multiplication is well defined for normal N, by multiplying sets, is the remark [[§38 Normal Subgroups#^rem-38-3|Second Proof of (⇐)]] in §38, after [[§38 Normal Subgroups#^rem-38-2|Multiplying Sets]].
- **Used for.** [[§40 Quotient Groups#^prop-40-2|Every Normal Subgroup Is a Kernel]] (§40.2), the [[First Isomorphism Theorem for Groups]], and the abelianization G/[G, G] ([[§47 Commutators#^prop-47-6|§47.6]]). The model case is ℤ/nℤ ([[§40 Quotient Groups#^ex-40-1|Ex. §40.1]]), and |G/N| = |G|/|N| by [[Lagrange's Theorem]].
- **Same idea elsewhere.** The 590 counterpart is [[§27 Free Groups and Presentations#^def-27-9|Quotient Group]], where quotients make presentations rigorous ([[§27 Free Groups and Presentations#^rem-27-20|How Quotient Groups Make Presentations Rigorous]]). The vector-space version, [[§11 Products and Quotients of Vector Spaces#^ladr-3-103|Quotient space is a vector space]] (LADR 3.103), needs no normality because addition commutes. The topological version is the [[§13 Quotient Topology#^def-13-3|Quotient Space]] with its [[Universal Property of Quotient Maps]].
- **Coming later in the course.** Composition series and the Jordan–Hölder theorem break a finite group into simple quotients. A finite group is solvable when all these quotients (its composition factors) are abelian, i.e. cyclic of prime order.
