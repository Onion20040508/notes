---
type: problem-set
subject: "[[Group Theory]]"
problem_set: 5
tags: [group-theory, math493]
---
← [[493 Problem Set 4]] · ↑ [[Group Theory]]

# Problem Set 5

*Submitted. Each problem is treated in the main text, at the location indicated.*

> [!question] Problem 5.1: The Index of an Intersection
> Let $H \leq G$ with $G/H$ finite, $A \leq G$ and $B = A \cap H$.
> 1. Show that $[A : B] \leq [G : H]$ ([[§29 The Index and Lagrange's Theorem#^def-29-1|index]]). Hint: consider the action of $B$ on $G/H$.
> 2. Prove or disprove: $[A : B]$ divides $[G : H]$.

^hw-5-1

*Treated in [[§29 The Index and Lagrange's Theorem|§29]] ([[§29 The Index and Lagrange's Theorem#^prop-29-9|§29.9]], [[§29 The Index and Lagrange's Theorem#^ex-29-2|Ex. §29.2]]); the normal case in [[§41 The First and Second Isomorphism Theorems#^cor-41-8|§41.8]].*

> [!question] Problem 5.2: Conjugacy in a Normal Subgroup
> Let $N \trianglelefteq G$ ([[§38 Normal Subgroups#^def-38-1|normal subgroup]]), $g \in N$, and $Z_G(g) = \{h \in G : gh = hg\}$ (the [[§34 Conjugation as an Action and the Class Equation#^def-34-1|centralizer]]).
> 1. For $h \in G$, show that $hgh^{-1}$ is conjugate to $g$ in $N$ iff $h \in Z_G(g)N$.
> 2. Show that $(1\,2\,3)$ and $(1\,3\,2)$ are conjugate in $A_5$, but $(1\,2\,3\,4\,5)$ and $(1\,2\,3\,5\,4)$ are not.
> 3. Show that $\begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$ and $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ are conjugate in $GL_2(\mathbb{R})$ but not in $SL_2(\mathbb{R})$.

^hw-5-2

*Treated in [[§44 Conjugacy in a Normal Subgroup|§44]] ([[§44 Conjugacy in a Normal Subgroup#^prop-44-1|§44.1]], [[§44 Conjugacy in a Normal Subgroup#^prop-44-2|§44.2]], [[§44 Conjugacy in a Normal Subgroup#^ex-44-2|Ex. §44.2]]).*

> [!question] Problem 5.3: Characters of the Alternating Group
> Let $n \geq 5$ and $\psi: A_n \to A$ a [[§46 Characters#^def-46-1|character]].
> 1. Show that every $3$-cycle is a commutator in $A_n$.
> 2. Show that $\psi((i\,j\,k)) = 1$.
> 3. Show that $\psi(\sigma) = 1$ for all $\sigma \in A_n$.

^hw-5-3

*Treated in [[§47 Commutators|§47]] ([[§47 Commutators#^lem-47-9|§47.9]], [[§47 Commutators#^thm-47-10|§47.10]]).*

> [!question] Problem 5.4: Elements of $D(G)$ That Are Not Commutators
> For the group $G$ of block matrices $\begin{bmatrix} I_p & A & C \\ 0 & I_q & B \\ 0 & 0 & I_r \end{bmatrix}$:
> 1. check the formulas for the inverse and the commutator;
> 2. show that $D(G)$ consists of the matrices $\begin{bmatrix} I_p & 0 & M \\ 0 & I_q & 0 \\ 0 & 0 & I_r \end{bmatrix}$;
> 3. show that if such a matrix is a commutator then $\operatorname{rank} M \leq 2q$, so that for $p, r > 2q$ there are elements of $D(G)$ that are not commutators.

^hw-5-4

*Treated in [[§47 Commutators|§47]] ([[§47 Commutators#^ex-47-2|Ex. §47.2]]).*
