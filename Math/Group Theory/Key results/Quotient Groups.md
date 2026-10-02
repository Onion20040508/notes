---
subject: math
type: theorem
source: "[[Group Theory]]"
aliases: ["MATH 493 37.1", "G/N is a group"]
tags: [group-theory, hub]
---
![[§37 Quotient Groups#^thm-37-1]]

## Treated in
- [[§37 Quotient Groups#^thm-37-1|Theorem §37.1: G/N Is a Group]], in [[§37 Quotient Groups]]

## Its proof uses
- [[§1 The Definition of a Group#^def-1-1|Definition §1.1: Group]]
- [[§27 The Index and Lagrange's Theorem#^def-27-1|Definition §27.1: Index]]
- [[§27 The Index and Lagrange's Theorem#^thm-27-2|Theorem §27.2: Lagrange]]
- [[§34 Multiplying Cosets#^prop-34-1|Proposition §34.1: When Coset Multiplication Is Well Defined]]

## Used in (Group Theory)
- [[§37 Quotient Groups#^prop-37-2|Proposition §37.2: Every Normal Subgroup Is a Kernel]]
- [[§38 The First Isomorphism Theorem#^cor-38-2|Corollary §38.2: ∣G∣ = ∣Keralpha∣ · ∣Imalpha∣]]
- [[§42 Commutators#^prop-42-6|Proposition §42.6: The Abelianization Is Abelian]]

## Connections
- **Normality is needed.** Coset multiplication is well defined exactly when gHg⁻¹ ⊆ H ([[§34 Multiplying Cosets#^prop-34-1|§34.1]]). For H = {e, (1 2)} in S₃ it is not ([[§35 Normal Subgroups#^ex-35-1|Ex. §35.1]], [[Characterizations of Normality]]).
- **Used for.** [[§37 Quotient Groups#^prop-37-2|Every Normal Subgroup Is a Kernel]] (§37.2), the [[First Isomorphism Theorem for Groups]], and the abelianization G/[G, G] ([[§42 Commutators#^prop-42-6|§42.6]]). The model case is ℤ/nℤ ([[§37 Quotient Groups#^ex-37-1|Ex. §37.1]]), and |G/N| = |G|/|N| by [[Lagrange's Theorem]].
- **Same idea elsewhere.** The 590 counterpart is [[§21 Algebra Prerequisites꞉ Groups#^def-21-13|Cosets and Quotient Group]], where quotients make presentations rigorous ([[§21 Algebra Prerequisites꞉ Groups#^rem-21-20|How Quotient Groups Make Presentations Rigorous]]). The vector-space version, [[§11 Products and Quotients of Vector Spaces#^ladr-3-103|Quotient space is a vector space]] (LADR 3.103), needs no normality because addition commutes. The topological version is the [[§12 Quotient Topology#^def-12-3|Quotient Space]] with its [[Universal Property of Quotient Maps]].
- **Coming later in the course.** Composition series and the Jordan–Hölder theorem break a finite group into simple quotients. A finite group is solvable when all these quotients (its composition factors) are abelian, i.e. cyclic of prime order.
