---
subject: math
type: theorem
source: "[[Group Theory]]"
aliases: ["MATH 493 7.2", "descending a map to Z/nZ", "well-defined maps out of Z/nZ"]
tags: [group-theory, hub]
---
![[§7 The Group ℤ∕nℤ#^lem-7-2]]

## Treated in
- [[§7 The Group ℤ∕nℤ#^lem-7-2|Lemma §7.2: Descending a Map to ℤ/nℤ]], in [[§7 The Group ℤ∕nℤ]]

## Its proof uses
- [[§4 Subgroups#^prop-4-6|Proposition §4.6: ⟨g⟩ Is the Smallest Subgroup Containing g]]
- [[§6 Divisibility and Congruence#^def-6-4|Definition §6.4: Residue Classes]]
- [[§7 The Group ℤ∕nℤ#^def-7-2|Definition §7.2: Well-Defined]]
- [[§15 Homomorphisms#^def-15-1|Definition §15.1: Group Homomorphism]]
- [[§15 Homomorphisms#^prop-15-2|Proposition §15.2: Image and Kernel Are Subgroups]]
- [[§15 Homomorphisms#^def-15-3|Definition §15.3: Kernel]]

## Its proof uses (other subjects)
- [[§1 The Set ℕ of Natural Numbers#^thm-1-1|451 §1.1: Principle of Mathematical Induction]]

## Used in (Group Theory)
- [[§17 Cyclic Groups#^thm-17-1|Theorem §17.1: Classification of Cyclic Groups]]
- [[§17 Cyclic Groups#^prop-17-3|Proposition §17.3: The Homomorphism k ↦ g^k and ⟨g⟩ ≅ ℤ/Nℤ]]

## Connections
- **Used for.** Every well-definedness check for maps out of ℤ/nℤ ([[§7 The Group ℤ∕nℤ#^rem-7-1|Where This Is Used]]): ℤ/4ℤ → U₅, k ↦ 2ᵏ ([[§16 Isomorphisms#^prop-16-7|§16.7]]); the [[Classification of Cyclic Groups]]; ⟨g⟩ ≅ ℤ/Nℤ ([[§17 Cyclic Groups#^prop-17-3|§17.3]]).
- **The hypothesis is the content.** φ descends exactly when φ(n) = e, i.e. nℤ ⊆ Ker φ. So k ↦ gᵏ descends to ℤ/Nℤ for N = ord(g), because its kernel is Nℤ ([[§17 Cyclic Groups#^prop-17-3|§17.3]]). But k ↦ 2ᵏ in U₅ does not descend to ℤ/3ℤ, since 2³ ≠ 1 mod 5.
- **Generalized.** ℤ/nℤ is the quotient of ℤ by nℤ ([[§40 Quotient Groups#^ex-40-1|Ex. §40.1]]). For any normal subgroup N, a homomorphism that kills N factors through G/N. With N = Ker α this is the [[First Isomorphism Theorem for Groups]].
- **Same idea elsewhere.** A continuous map that is constant on fibers descends through a quotient map ([[Universal Property of Quotient Maps]], 590 Thm. §13.3). A linear map descends to V/null T ([[First isomorphism theorem]], LADR 3.107).
- **Set-level version in [[Logic and Proofs]]:** [[§22 Partitions and Equivalence Relations#^prop-22-5|250 Prop. §22.5]] (a surjection induces a bijection from the quotient set; the text after it states the general rule for defining maps on classes).
