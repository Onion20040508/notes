---
subject: math
type: theorem
source: "[[Group Theory]]"
aliases: ["MATH 493 15.3", "kernel criterion for injectivity"]
tags: [group-theory, hub]
---
![[§15 Homomorphisms#^prop-15-3]]

## Treated in
- [[§15 Homomorphisms#^prop-15-3|Proposition §15.3: Surjectivity and Injectivity via Image and Kernel]], in [[§15 Homomorphisms]]

## Its proof uses
- [[§15 Homomorphisms#^prop-15-1|Proposition §15.1: Homomorphisms Preserve Identity and Inverses]]
- [[§15 Homomorphisms#^def-15-2|Definition §15.2: Image and Kernel]]
- [[§16 Isomorphisms#^def-16-1|Definition §16.1: Isomorphism; Isomorphic Groups]]

## Used in (Group Theory)
- [[§17 Cyclic Groups#^thm-17-1|Theorem §17.1: Classification of Cyclic Groups]]
- [[§17 Cyclic Groups#^prop-17-3|Proposition §17.3: The Homomorphism k ↦ g^k and ⟨g⟩ ≅ ℤ/Nℤ]]
- [[§23 Actions#^prop-23-4|Proposition §23.4: Faithful Actions Embed G in S_X]]
- [[§39 Simple Groups#^prop-39-3|Proposition §39.3: Homomorphisms out of a Simple Group]]

## Connections
- **Used for.** Proving isomorphisms, such as ⟨g⟩ ≅ ℤ/Nℤ ([[§17 Cyclic Groups#^prop-17-3|§17.3]]) and the [[Classification of Cyclic Groups]]. Also faithful actions embed G in S_X ([[§23 Actions#^prop-23-4|§23.4]]), which gives [[Cayley's Theorem]], and homomorphisms out of a simple group are injective or trivial ([[§39 Simple Groups#^prop-39-3|§39.3]]).
- **Homomorphisms only.** For an arbitrary map, the fiber over one point says nothing about the others. The criterion works because φ(g₁) = φ(g₂) can be rewritten as φ(g₁g₂⁻¹) = e ([[§15 Homomorphisms#^rem-15-2|Kernel as the Measure of Non-Injectivity]]).
- **Same idea elsewhere.** [[3B Null Spaces and Ranges#^ladr-3-15|Injectivity ⟺ null space equals {0}]] (LADR 3.15), and its 590 counterpart ([[§21 Algebra Prerequisites꞉ Groups#^prop-21-8|590 §21.8]]). The quantitative version is |G| = |Ker φ| · |Im φ| ([[§38 The First Isomorphism Theorem#^cor-38-2|§38.2]]).
