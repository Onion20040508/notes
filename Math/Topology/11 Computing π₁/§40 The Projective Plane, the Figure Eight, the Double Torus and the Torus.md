---
type: section
subject: "[[Topology]]"
chapter: 11
section: 40
tags: [topology, math590]
---
← [[§39 The Seifert–van Kampen Theorem]] · ↑ [[· 11 Computing π₁]]

*The recurring examples of Chapter 11, gathered in course order: the projective plane, the figure eight, the double torus and the torus. Each part embeds the chapter's items about one example, and the last part the items that compare the surfaces; the items themselves stay in their sections.*

## The Projective Plane P²

$P^2$ is $S^2$ with antipodal points identified. Its fundamental group $\mathbb{Z}/2\mathbb{Z}$ is computed twice: from the double cover $S^2 \to P^2$ ([[§38 Fundamental Group of Some Surfaces#^pf-38-2|proof]]) and by van Kampen, where $P^2$ is the case $n = 2$ of the $n$-fold dunce cap.

![[§38 Fundamental Group of Some Surfaces#^def-38-1]]

![[§38 Fundamental Group of Some Surfaces#^thm-38-1]]

![[§38 Fundamental Group of Some Surfaces#^thm-38-2]]

![[§38 Fundamental Group of Some Surfaces#^rem-38-1]]

![[§39 The Seifert–van Kampen Theorem#^ex-39-5]]

![[§39 The Seifert–van Kampen Theorem#^ex-39-6]]

*Chain: later in [[Algebraic Topology Toolkit#^ex-35-1|the Toolkit]] · [[Projective plane|all appearances]]*

## The Figure Eight

The wedge $S^1 \vee S^1$ of two circles. A covering space shows that its fundamental group is non-abelian ([[§38 Fundamental Group of Some Surfaces#^pf-38-4|proof]]), and van Kampen computes it in full as $\mathbb{Z} * \mathbb{Z} = F_2$.

![[§38 Fundamental Group of Some Surfaces#^def-38-4]]

![[§38 Fundamental Group of Some Surfaces#^thm-38-4]]

![[§39 The Seifert–van Kampen Theorem#^ex-39-2]]

*Chain: earlier in [[§36 The Punctured Plane, the Figure Eight and the Torus|Chapter 10]] · [[Figure eight|all appearances]]*

## The Double Torus

Two tori glued along a removed disk. The figure eight is a retract of $\Sigma_2$, so $\pi_1(\Sigma_2)$ is non-abelian; the theorem has two proofs, one through the injection $j_{\ast}$ ([[§38 Fundamental Group of Some Surfaces#^pf-38-5|Proof 1]]) and one through the surjection $r_{\ast}$ ([[§38 Fundamental Group of Some Surfaces#^pf-38-5-2|Proof 2]]).

![[§38 Fundamental Group of Some Surfaces#^def-38-5]]

![[§38 Fundamental Group of Some Surfaces#^thm-38-5]]

*Chain: earlier in [[§34 Retractions and Fixed Points#^ex-34-1|Chapter 10]] · [[Double torus|all appearances]]*

## The Torus

Van Kampen gives $\pi_1(T^2) \cong \mathbb{Z} \times \mathbb{Z}$ again. Removing a point removes the relation, and gluing the disk back adds the relation $aba^{-1}b^{-1} = e$.

![[§39 The Seifert–van Kampen Theorem#^ex-39-4]]

![[§39 The Seifert–van Kampen Theorem#^rem-39-6]]

*Chain: earlier in [[§36 The Punctured Plane, the Figure Eight and the Torus|Chapter 10]] · [[Torus|all appearances]]*

## The Surfaces Compared

$\pi_1$ tells $S^2$, $T^2$, $P^2$ and $\Sigma_2$ apart, and each surface is a polygon whose edges are glued according to a boundary word.

![[§38 Fundamental Group of Some Surfaces#^cor-38-6]]

![[§39 The Seifert–van Kampen Theorem#^ex-39-7]]

![[§39 The Seifert–van Kampen Theorem#^ex-39-8]]
