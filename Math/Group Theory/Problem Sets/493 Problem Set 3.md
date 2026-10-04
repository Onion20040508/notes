---
type: problem-set
subject: "[[Group Theory]]"
problem_set: 3
tags: [group-theory, math493]
---
← [[493 Problem Set 2]] · ↑ [[Group Theory]] · [[493 Problem Set 4]] →

# Problem Set 3

*Submitted. Each problem is treated as a proposition or theorem in the main text, at the location indicated.*

> [!question] Problem 3.1: Cayley's Theorem
> Let $G$ be a group with $n$ elements.
>
> 1. Show that $G$ is isomorphic to a subgroup of $S_n$.
> 2. Let $k$ be a field. Show that $G$ is isomorphic to a subgroup of $GL_n(k)$.

^hw-3-1

*Treated in [[§25 Actions|§25]] ([[§25 Actions#^thm-25-5|Cayley's Theorem]]; [[§25 Actions#^cor-25-6|Every Finite Group Is a Matrix Group]]).*

> [!question] Problem 3.2: A Normal Subgroup Inside a Finite-Index Subgroup
> Let $H$ be a subgroup of $G$ with $[G : H] = n$. Show that there is a normal subgroup $N$ of $G$ with $N \subseteq H \subseteq G$ and $[G : N] \leq n!$. (The sheet prints $[G : H] \leq n!$; the intended statement is $[G : N] \leq n!$.) Hint: make a homomorphism $G \to S_n$ and think about the kernel.

^hw-3-2

*Treated in [[§39 Sources of Normal Subgroups|§39]] ([[§39 Sources of Normal Subgroups#^thm-39-5|§39.5]]).*

> [!question] Problem 3.3: Burnside's Lemma
> Let $G$ be a finite group acting on a finite set $X$. Show that $\frac{1}{|G|}\sum_{g \in G} |\operatorname{Fix}(g)| = |G \backslash X|$. Hint: count the pairs $(x, g)$ with $g(x) = x$ in two ways.

^hw-3-3

*Treated in [[§30 Orbit–Stabilizer|§30]] ([[§30 Orbit–Stabilizer#^thm-30-6|§30.6]]).*

> [!question] Problem 3.4: Conjugacy Classes and Centralizers
> For $g \in G$ let $\operatorname{Conj}(g) = \{hgh^{-1} : h \in G\}$ and $Z(g) = \{h \in G : gh = hg\}$ (the centralizer). Suppose $G$ is finite.
>
> 1. Show that $|G| = |\operatorname{Conj}(g)| \cdot |Z(g)|$.
> 2. Let $g_1, \ldots, g_c$ be one representative from each conjugacy class. Prove the class equation $\sum_i 1/|Z(g_i)| = 1$.

^hw-3-4

*Treated in [[§34 Conjugation as an Action and the Class Equation|§34]] ([[§34 Conjugation as an Action and the Class Equation#^cor-34-2|Class Sizes Divide the Group Order]]; [[§34 Conjugation as an Action and the Class Equation#^cor-34-3|The Class Equation, Reciprocal Form]]).*

> [!question] Problem 3.5: Groups of Prime-Power Order
> Let $p$ be a prime and $|G| = p^k$ with $k \geq 1$.
>
> 1. Show that there is some $g \neq e$ with $\operatorname{Conj}(g) = \{g\}$.
> 2. Show that this $g$ commutes with every $h \in G$.

^hw-3-5

*Treated in [[§35 The Center|§35]] ([[§35 The Center#^thm-35-3|§35.3]]).*

> [!question] Problem 3.6: Three Conjugacy Classes
> Let $G$ be a finite group with $3$ conjugacy classes. Show that $|G| \leq 6$. Hint: see [[493 Problem Set 3#^hw-3-4|Problem 3.4]].

^hw-3-6

*Treated in [[§34 Conjugation as an Action and the Class Equation|§34]] ([[§34 Conjugation as an Action and the Class Equation#^prop-34-5|§34.5]]).*
