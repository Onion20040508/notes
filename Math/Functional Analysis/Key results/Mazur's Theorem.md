---
subject: math
type: theorem
source: "[[Functional Analysis]]"
aliases: ["MATH 556 43.7", "weak limit in the closed convex hull", "Lax §10.1, Thm 6"]
tags: [functional-analysis, hub]
---
![[§43 Weak and Weak-Star Convergence#^thm-43-7]]

## Treated in
- [[§43 Weak and Weak-Star Convergence#^thm-43-7|Theorem §43.7: Mazur's Theorem]], in [[§43 Weak and Weak-Star Convergence]]

## Its proof uses
- [[§3 Linear Maps, Convexity, and Linear Functionals#^def-3-4|Definition §3.4: Convex Hull]]
- [[§43 Weak and Weak-Star Convergence#^thm-43-5|Theorem §43.5: Hyperplane Separation in a Normed Space]]

## Used in (Functional Analysis)
- (not cited later in the course)

## Connections
- **How.** Let $K$ be the closed convex hull of the $x_n$. If $x_0 \notin K$, [[Hyperplane Separation in a Normed Space]] gives $\ell \in X'$ and $a$ with $\ell(x_0) > a > \ell(x_n)$ for all $n$, which contradicts $\ell(x_n) \to \ell(x_0)$. Over $\mathbb{C}$ use real parts ([[§43 Weak and Weak-Star Convergence#^cor-43-6|§43.6]]).
- **What it says.** A weak limit can be reached strongly, not by the sequence itself but by convex combinations of its terms. Equivalently, a closed convex set contains the weak limits of its sequences.
- **Example.** $e_n \rightharpoonup 0$ in $\ell^2$ but $\|e_n\| = 1$ ([[§43 Weak and Weak-Star Convergence#^ex-43-1|Ex. §43.1]]); the averages $\frac1n(e_1 + \cdots + e_n)$ have norm $n^{-1/2} \to 0$.
- **In Lax.** Lax proves it with support functions (§10.1, Thm 6); the lecture uses the separation theorem.
