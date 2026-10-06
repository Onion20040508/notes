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
- [[§25 Actions#^prop-25-4|Proposition §25.4: Faithful Actions Embed G in S_X]]
- [[§43 Simple Groups#^prop-43-3|Proposition §43.3: Homomorphisms out of a Simple Group]]

## Connections
- **Used for.** Proving isomorphisms, such as ⟨g⟩ ≅ ℤ/Nℤ ([[§17 Cyclic Groups#^prop-17-3|§17.3]]) and the [[Classification of Cyclic Groups]]. Also faithful actions embed G in S_X ([[§25 Actions#^prop-25-4|§25.4]]), which gives [[Cayley's Theorem]], and homomorphisms out of a simple group are injective or trivial ([[§43 Simple Groups#^prop-43-3|§43.3]]).
- **Homomorphisms only.** For an arbitrary map, the fiber over one point says nothing about the others. The criterion works because φ(g₁) = φ(g₂) can be rewritten as φ(g₁g₂⁻¹) = e ([[§15 Homomorphisms#^rem-15-2|Kernel as the Measure of Non-Injectivity]]).
- **Same idea elsewhere.** [[§8 Null Spaces and Ranges#^ladr-3-15|Injectivity ⟺ null space equals {0}]] (LADR 3.15), and its 590 counterpart ([[§21 Algebra Prerequisites꞉ Groups#^prop-21-8|590 Prop. §21.8]]). The quantitative version is |G| = |Ker φ| · |Im φ| ([[§41 The First and Second Isomorphism Theorems#^cor-41-2|§41.2]]).
- **Also in [[Applied Linear Algebra]]:** [[§9 The Matrix of a Linear Transformation#^thm-9-2|235 Thm. §9.2]] (linear maps ℝⁿ → ℝᵐ: one-to-one iff T(x) = 0 has only the trivial solution, with worked examples).
