---
subject: math
type: theorem
source: "[[Functional Analysis]]"
aliases: ["MATH 556 44.4", "weak sequential compactness in reflexive spaces", "Lax §10.2, Thm 7"]
tags: [functional-analysis, hub]
---
![[§44 Weak Sequential Compactness#^thm-44-4]]

## Treated in
- [[§44 Weak Sequential Compactness#^thm-44-4|Theorem §44.4: Eberlein's Theorem]], in [[§44 Weak Sequential Compactness]]

## Its proof uses
- [[§11 Normed Linear Spaces#^lem-11-8|Lemma §11.8: The Closed Linear Span is the Smallest Closed Subspace]]
- [[§37 Separable Duals and Reflexive Spaces#^prop-37-5|Proposition §37.5: The Canonical Embedding X → X'']]
- [[§37 Separable Duals and Reflexive Spaces#^cor-37-7|Corollary §37.7: Separability of X and X' for Reflexive X]]
- [[§37 Separable Duals and Reflexive Spaces#^thm-37-8|Theorem §37.8: Closed Subspaces of Reflexive Spaces are Reflexive]]
- [[§44 Weak Sequential Compactness#^thm-44-1|Theorem §44.1: Helly's Theorem]]
- [[§44 Weak Sequential Compactness#^lem-44-3|Lemma §44.3: The Closed Span of a Countable Set is Separable]]

## Used in (Functional Analysis)
- [[§44 Weak Sequential Compactness#^cor-44-5|Corollary §44.5: Closed Balls of a Reflexive Space]]
- [[§44 Weak Sequential Compactness#^cor-44-7|Corollary §44.7: Bounded Closed Convex Sets in a Reflexive Space]]
- [[§44 Weak Sequential Compactness#^thm-44-10|Theorem §44.10: Closest Point in a Closed Convex Subset of a Reflexive Space]]

## Connections
- **What it says.** In a reflexive Banach space every bounded sequence has a weakly convergent subsequence. This is the replacement for the Bolzano–Weierstrass theorem, which fails for strong convergence in infinite dimensions ([[The Unit Ball of an Infinite-Dimensional Space Is Not Compact]]).
- **How.** If $X$ is separable, so is $X'$ ([[§37 Separable Duals and Reflexive Spaces#^cor-37-7|Cor. §37.7]]); [[Helly's Theorem]] applied to $X'$ gives a weak-$\ast$ limit in $X'' = X$, which is a weak limit in $X$. In general, pass to the closed span of the sequence, which is separable ([[§44 Weak Sequential Compactness#^lem-44-3|Lemma §44.3]]) and reflexive ([[Closed Subspaces of Reflexive Spaces are Reflexive]]).
- **Why the hypotheses.** Reflexivity is exactly what is needed: if the closed unit ball is weakly sequentially compact, the space is reflexive ([[§44 Weak Sequential Compactness#^thm-44-6|Thm. §44.6]], not proved in these notes).
- **Used for.** With [[Mazur's Theorem]], bounded closed convex sets are weakly sequentially compact ([[§44 Weak Sequential Compactness#^cor-44-7|Cor. §44.7]]); with the norm bound for weak limits, [[Closest Point in a Reflexive Space]].
- **In Hilbert space.** A Hilbert space is reflexive ([[§37 Separable Duals and Reflexive Spaces#^ex-37-3|Ex. §37.3]]), so every bounded sequence in a Hilbert space has a weakly convergent subsequence; the orthonormal sequence $e_n \rightharpoonup 0$ ([[§43 Weak and Weak-Star Convergence#^ex-43-1|Ex. §43.1]]) shows the limit can lose norm.
- **In Lax.** §10.2, Thm 7; Lax runs the diagonal process directly on a dense subset of the dual of the closed span.
