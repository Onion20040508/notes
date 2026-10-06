---
subject: math
type: theorem
source: "[[Group Theory]]"
aliases: ["MATH 493 41.4", "diamond isomorphism theorem", "H/(H ∩ N) ≅ HN/N"]
tags: [group-theory, hub]
---
![[§41 The First and Second Isomorphism Theorems#^thm-41-4]]

## Treated in
- [[§41 The First and Second Isomorphism Theorems#^thm-41-4|Theorem §41.4: Second Isomorphism Theorem]], in [[§41 The First and Second Isomorphism Theorems]]

## Its proof uses
- [[§15 Homomorphisms#^def-15-2|Definition §15.2: Image and Kernel]]
- [[§39 Sources of Normal Subgroups#^prop-39-2|Proposition §39.2: Kernels Are Normal]]
- [[§40 Quotient Groups#^def-40-1|Definition §40.1: Quotient Group]]
- [[§40 Quotient Groups#^prop-40-2|Proposition §40.2: Every Normal Subgroup Is a Kernel]]
- [[§41 The First and Second Isomorphism Theorems#^def-41-1|Definition §41.1: The Product Set HN]]
- [[§41 The First and Second Isomorphism Theorems#^thm-41-1|Theorem §41.1: First Isomorphism Theorem]]
- [[§41 The First and Second Isomorphism Theorems#^lem-41-3|Lemma §41.3: HN Is a Subgroup When N Is Normal]]

## Used in (Group Theory)
- [[§41 The First and Second Isomorphism Theorems#^cor-41-7|Corollary §41.7: Subgroup Representatives, Again]]
- [[§41 The First and Second Isomorphism Theorems#^cor-41-8|Corollary §41.8: Index of an Intersection, Normal Case]]
- [[§45 S₃, S₄, A₄ and A₅#^ex-45-3|Example §45.3: GL_2^+(ℝ), SL_2(ℝ) and the Scalars]]

## Connections
- **How.** Two applications of the [[First Isomorphism Theorem for Groups]] to the projection $\pi : G \to G/N$: restricted to $H$ it has kernel $H \cap N$, restricted to $HN$ kernel $N$, and the two images agree, $\pi(H) = \pi(HN)$ ([[§41 The First and Second Isomorphism Theorems#^thm-41-4|§41.4]]).
- **Picture.** The diamond $H \cap N \le H, N \le HN$ ([[m493-38-3.svg|figure]] in [[§41 The First and Second Isomorphism Theorems|§41]]): the quotients on opposite edges agree, $HN/N \cong H/(H \cap N)$.
- **Special case.** When a set of representatives for $G/N$ is a subgroup $S$, then $G/N \cong S$ ([[§41 The First and Second Isomorphism Theorems#^cor-41-7|§41.7]], first proved directly in [[§40 Quotient Groups#^prop-40-4|§40.4]]); with $H = \operatorname{Stab}(4)$ it gives $S_4/V \cong S_3$ ([[§45 S₃, S₄, A₄ and A₅#^ex-45-1|Ex. §45.1]]).
- **Restriction view (lecture 10/5).** Both isomorphisms come from restricting $\pi$ and reading off kernels ([[§41 The First and Second Isomorphism Theorems#^lem-41-5|§41.5]], [[§41 The First and Second Isomorphism Theorems#^rem-41-4|Remark]]); counting gives $|SN| = |S|\,|N|/|S \cap N|$ ([[§41 The First and Second Isomorphism Theorems#^cor-41-6|§41.6]]), the analogue of $\dim(L_1 + L_2) = \dim L_1 + \dim L_2 - \dim(L_1 \cap L_2)$ ([[§6 Dimension#^ladr-2-43|LADR 2.43]]).
- **Next.** Subgroups of $G/N$ and quotients of quotients: the [[Correspondence Theorem for Groups]] and the [[Third Isomorphism Theorem for Groups]] ([[§42 The Correspondence and Third Isomorphism Theorems|§42]]).
