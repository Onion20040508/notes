---
type: section
subject: "[[Applied Linear Algebra]]"
chapter: 4
section: 24
lay: "4.2"
aliases: ["Lay 4.2"]
tags: [applied-linear-algebra, math235]
---
← [[§23 Vector Spaces and Subspaces]] · ↑ [[· 4 Vector Spaces]] · [[§25 Linearly Independent Sets; Bases]] →

*Lay, Section 4.2 · MATH 235 lectures L10, L14.*

Subspaces of $\mathbb{R}^n$ usually arise in one of two ways: as the set of all solutions of a homogeneous linear system, or as the set of all linear combinations of given vectors. For a matrix $A$ these are its null space $\operatorname{Nul} A$, defined *implicitly* by the condition $A\mathbf{x} = \mathbf{0}$, and its column space $\operatorname{Col} A$, defined *explicitly* as a span. Solving $A\mathbf{x} = \mathbf{0}$ turns the implicit description into an explicit one. The two spaces behave very differently, and the section contrasts them; it ends by extending them to any linear transformation between vector spaces, as its kernel and range. (The lecture: every subspace of $\mathbb{R}^n$ is $\operatorname{Nul} A$ for some $A$ and also $\operatorname{Col} B$ for some $B$.)

## The Null Space of a Matrix

> [!definition] Definition §24.1: Null Space
> The **null space** of an $m \times n$ matrix $A$, written $\operatorname{Nul} A$, is the set of all solutions of the homogeneous equation $A\mathbf{x} = \mathbf{0}$:
>
> $$
> \operatorname{Nul} A = \{\mathbf{x} : \mathbf{x} \text{ is in } \mathbb{R}^n \text{ and } A\mathbf{x} = \mathbf{0}\} .
> $$
>
> Dynamically, $\operatorname{Nul} A$ is the set of all $\mathbf{x}$ in $\mathbb{R}^n$ that the linear transformation $\mathbf{x} \mapsto A\mathbf{x}$ maps to the zero vector of $\mathbb{R}^m$.
>
> *Lay: 4.2, Definition*

^def-24-1

> [!theorem] Theorem §24.1: The Null Space Is a Subspace
> The null space of an $m \times n$ matrix $A$ is a subspace of $\mathbb{R}^n$. Equivalently, the set of all solutions of a system $A\mathbf{x} = \mathbf{0}$ of $m$ homogeneous linear equations in $n$ unknowns is a subspace of $\mathbb{R}^n$.
>
> *Lay: Theorem 2 (4.2)*

^thm-24-1

> [!proof]+ Proof
> $\operatorname{Nul} A$ is a subset of $\mathbb{R}^n$ because $A$ has $n$ columns. We check the three properties of a subspace ([[§23 Vector Spaces and Subspaces#^def-23-2|Definition §23.2]]). Certainly $A\mathbf{0} = \mathbf{0}$, so $\mathbf{0}$ is in $\operatorname{Nul} A$. Let $\mathbf{u}$ and $\mathbf{v}$ be in $\operatorname{Nul} A$, so $A\mathbf{u} = \mathbf{0}$ and $A\mathbf{v} = \mathbf{0}$. By the properties of matrix–vector multiplication ([[§4 The Matrix Equation Ax = b#^thm-4-5|Theorem §4.5]], Theorem 5 of 1.4),
>
> $$
> A(\mathbf{u} + \mathbf{v}) = A\mathbf{u} + A\mathbf{v} = \mathbf{0} + \mathbf{0} = \mathbf{0}, \qquad A(c\mathbf{u}) = c(A\mathbf{u}) = c\mathbf{0} = \mathbf{0},
> $$
>
> so $\mathbf{u} + \mathbf{v}$ and $c\mathbf{u}$ are in $\operatorname{Nul} A$. Thus $\operatorname{Nul} A$ is a subspace of $\mathbb{R}^n$.

^pf-24-1

*Uses:* [[§23 Vector Spaces and Subspaces#^def-23-2|Def. §23.2]], [[§4 The Matrix Equation Ax = b#^thm-4-5|§4.5]]

> [!remark]- Connections
> - Rigorous treatment: [[§8 Null Spaces and Ranges#^ladr-3-11|LADR 3.11]], [[§8 Null Spaces and Ranges#^ladr-3-13|LADR 3.13]] (the null space of any linear map is a subspace), and homogeneous systems with more unknowns than equations have nonzero solutions, [[§8 Null Spaces and Ranges#^ladr-3-26|LADR 3.26]].

> [!example] Example §24.1: Testing Membership; Subspaces Given by Equations
> **(a)** Let $A = \begin{bmatrix} 1 & -3 & -2 \\ -5 & 9 & 1 \end{bmatrix}$ and $\mathbf{u} = (5, 3, -2)$. Is $\mathbf{u}$ in $\operatorname{Nul} A$? Simply compute:
>
> $$
> A\mathbf{u} = \begin{bmatrix} 1 & -3 & -2 \\ -5 & 9 & 1 \end{bmatrix}\begin{bmatrix} 5 \\ 3 \\ -2 \end{bmatrix} = \begin{bmatrix} 5 - 9 + 4 \\ -25 + 27 - 2 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix} .
> $$
>
> So $\mathbf{u}$ is in $\operatorname{Nul} A$.
>
> **(b)** Let $H$ be the set of all vectors in $\mathbb{R}^4$ whose coordinates $a, b, c, d$ satisfy $a - 2b + 5c = d$ and $c - a = b$. Rearranged, $H$ is the solution set of the homogeneous system
>
> $$
> \begin{aligned} a - 2b + 5c - d &= 0 \\ -a - b + c \phantom{{}- d} &= 0 \end{aligned}
> $$
>
> so $H = \operatorname{Nul}\begin{bmatrix} 1 & -2 & 5 & -1 \\ -1 & -1 & 1 & 0 \end{bmatrix}$ is a subspace of $\mathbb{R}^4$ by Theorem §24.1. It matters that the equations are *homogeneous*: the solution set of a nonhomogeneous system never contains $\mathbf{0}$, so it is never a subspace (and it may be empty).
>
> *Lay: Examples 4.2.1 and 4.2.2*

^ex-24-1

## An Explicit Description of Nul A

There is no obvious relation between the vectors in $\operatorname{Nul} A$ and the entries of $A$: $\operatorname{Nul} A$ is defined *implicitly*, by a condition. Solving $A\mathbf{x} = \mathbf{0}$ (as in [[§5 Solution Sets of Linear Systems#^prop-5-2|Proposition §5.2]], 1.5) produces an *explicit* description, a spanning set.

> [!remark] Remark: Method — A Spanning Set for Nul A
> 1. Row reduce the augmented matrix $[A \ \mathbf{0}]$ to *reduced* echelon form, so that each basic variable is expressed in terms of the free variables.
> 2. Write the general solution $\mathbf{x}$ with the basic variables replaced by these expressions.
> 3. Decompose $\mathbf{x}$ as a linear combination of vectors **whose weights are the free variables**. These vectors span $\operatorname{Nul} A$.
>
> If there are no free variables, $\operatorname{Nul} A = \{\mathbf{0}\}$.

^rem-24-1

> [!example] Example §24.2: A Spanning Set for a Null Space
> Find a spanning set for the null space of
>
> $$
> A = \begin{bmatrix} -3 & 6 & -1 & 1 & -7 \\ 1 & -2 & 2 & 3 & -1 \\ 2 & -4 & 5 & 8 & -4 \end{bmatrix} .
> $$
>
> Row reduce $[A \ \mathbf{0}]$ to reduced echelon form:
>
> $$
> \begin{bmatrix} 1 & -2 & 0 & -1 & 3 & 0 \\ 0 & 0 & 1 & 2 & -2 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 \end{bmatrix}, \qquad \begin{aligned} x_1 - 2x_2 \phantom{{}+ x_3} - x_4 + 3x_5 &= 0 \\ x_3 + 2x_4 - 2x_5 &= 0 \\ 0 &= 0 . \end{aligned}
> $$
>
> The general solution is $x_1 = 2x_2 + x_4 - 3x_5$, $x_3 = -2x_4 + 2x_5$, with $x_2$, $x_4$, $x_5$ free. Decompose with the free variables as weights:
>
> $$
> \begin{bmatrix} x_1 \\ x_2 \\ x_3 \\ x_4 \\ x_5 \end{bmatrix} = \begin{bmatrix} 2x_2 + x_4 - 3x_5 \\ x_2 \\ -2x_4 + 2x_5 \\ x_4 \\ x_5 \end{bmatrix} = x_2\underbrace{\begin{bmatrix} 2 \\ 1 \\ 0 \\ 0 \\ 0 \end{bmatrix}}_{\mathbf{u}} + x_4\underbrace{\begin{bmatrix} 1 \\ 0 \\ -2 \\ 1 \\ 0 \end{bmatrix}}_{\mathbf{v}} + x_5\underbrace{\begin{bmatrix} -3 \\ 0 \\ 2 \\ 0 \\ 1 \end{bmatrix}}_{\mathbf{w}} . \qquad (3)
> $$
>
> Every linear combination of $\mathbf{u}$, $\mathbf{v}$, $\mathbf{w}$ is in $\operatorname{Nul} A$ and vice versa, so $\{\mathbf{u}, \mathbf{v}, \mathbf{w}\}$ spans $\operatorname{Nul} A$.
>
> *Lay: Example 4.2.3*

^ex-24-2

> [!theorem] Proposition §24.2: The Spanning Set Produced by the Method
> When $\operatorname{Nul} A$ contains nonzero vectors, the spanning set produced by the method of Remark §24.1
> 1. is automatically linearly independent, and
> 2. has as many vectors as there are free variables in $A\mathbf{x} = \mathbf{0}$.
>
> *Lay: 4.2 (text after Example 3)*

^prop-24-2

> [!proof]+ Proof
> Part 2 is the construction: one vector for each free variable. For part 1, let $x_{j_1}, \ldots, x_{j_k}$ be the free variables and $\mathbf{u}_1, \ldots, \mathbf{u}_k$ the vectors, with $\mathbf{x} = x_{j_1}\mathbf{u}_1 + \cdots + x_{j_k}\mathbf{u}_k$. Entry $j_i$ of $\mathbf{x}$ is the free variable $x_{j_i}$ itself, so entry $j_i$ of $\mathbf{u}_i$ is $1$ and entry $j_i$ of every other $\mathbf{u}_l$ is $0$ (in Example §24.2, look at entries 2, 4, 5). Hence if $c_1\mathbf{u}_1 + \cdots + c_k\mathbf{u}_k = \mathbf{0}$, entry $j_i$ of the left side is $c_i$, so every $c_i = 0$.

^pf-24-2

*Uses:* [[§7 Linear Independence#^def-7-1|Def. §7.1]] (linear independence)

## The Column Space of a Matrix

> [!definition] Definition §24.2: Column Space
> The **column space** of an $m \times n$ matrix $A$, written $\operatorname{Col} A$, is the set of all linear combinations of the columns of $A$. If $A = [\mathbf{a}_1 \ \cdots \ \mathbf{a}_n]$, then
>
> $$
> \operatorname{Col} A = \operatorname{Span}\{\mathbf{a}_1, \ldots, \mathbf{a}_n\} .
> $$
>
> Since $A\mathbf{x}$ stands for a linear combination of the columns of $A$ with weights the entries of $\mathbf{x}$,
>
> $$
> \operatorname{Col} A = \{\mathbf{b} : \mathbf{b} = A\mathbf{x} \text{ for some } \mathbf{x} \text{ in } \mathbb{R}^n\},
> $$
>
> the *range* of the linear transformation $\mathbf{x} \mapsto A\mathbf{x}$.
>
> *Lay: 4.2, Definition*

^def-24-2

> [!theorem] Theorem §24.3: The Column Space Is a Subspace
> The column space of an $m \times n$ matrix $A$ is a subspace of $\mathbb{R}^m$.
>
> *Lay: Theorem 3 (4.2)*

^thm-24-3

> [!proof]+ Proof
> The columns of $A$ are in $\mathbb{R}^m$, and their span is a subspace of $\mathbb{R}^m$ by [[§23 Vector Spaces and Subspaces#^thm-23-4|Theorem §23.4]]. (The lecture checks it directly from $\operatorname{Col} A = \{A\mathbf{x}\}$: $A\mathbf{0} = \mathbf{0}$, $A\mathbf{b} + A\mathbf{c} = A(\mathbf{b} + \mathbf{c})$, $c(A\mathbf{b}) = A(c\mathbf{b})$.)

^pf-24-3

*Uses:* [[§23 Vector Spaces and Subspaces#^thm-23-4|§23.4]]

> [!theorem] Proposition §24.4: When Col A Is All of ℝᵐ
> The column space of an $m \times n$ matrix $A$ is all of $\mathbb{R}^m$ if and only if the equation $A\mathbf{x} = \mathbf{b}$ has a solution for each $\mathbf{b}$ in $\mathbb{R}^m$.
>
> *Lay: 4.2 (boxed restatement of Theorem 4 of 1.4)*

^prop-24-4

> [!proof]+ Proof
> $A\mathbf{x} = \mathbf{b}$ has a solution exactly when $\mathbf{b}$ is a linear combination of the columns of $A$, that is, when $\mathbf{b} \in \operatorname{Col} A$. So "a solution for each $\mathbf{b}$" means "every $\mathbf{b}$ is in $\operatorname{Col} A$", that is, $\operatorname{Col} A = \mathbb{R}^m$. (Equivalently, $A$ has a pivot position in every row: [[§4 The Matrix Equation Ax = b#^thm-4-3|Theorem §4.3]], Theorem 4 of 1.4.)

^pf-24-4

*Uses:* [[§24 Null Spaces, Column Spaces, and Linear Transformations#^def-24-2|Def. §24.2]], [[§4 The Matrix Equation Ax = b#^thm-4-3|§4.3]]

> [!example] Example §24.3: A Subspace as a Column Space
> Find a matrix $A$ such that $W = \operatorname{Col} A$, where $W = \{(6a - b,\ a + b,\ -7a) : a, b \in \mathbb{R}\}$.
>
> First write $W$ as a set of linear combinations:
>
> $$
> W = \left\{ a\begin{bmatrix} 6 \\ 1 \\ -7 \end{bmatrix} + b\begin{bmatrix} -1 \\ 1 \\ 0 \end{bmatrix} : a, b \in \mathbb{R} \right\} = \operatorname{Span}\left\{ \begin{bmatrix} 6 \\ 1 \\ -7 \end{bmatrix}, \begin{bmatrix} -1 \\ 1 \\ 0 \end{bmatrix} \right\} .
> $$
>
> Then use the spanning vectors as the columns: $A = \begin{bmatrix} 6 & -1 \\ 1 & 1 \\ -7 & 0 \end{bmatrix}$ has $\operatorname{Col} A = W$. $W$ is a plane through the origin in $\mathbb{R}^3$.
>
> *Lay: Example 4.2.4*

^ex-24-3

## The Row Space of a Matrix

The course checklist lists the row space with $\operatorname{Nul} A$ and $\operatorname{Col} A$; the 6th edition introduces it here, the 5th in 4.6 ([[§28 Rank|§28]]).

> [!definition] Definition §24.3: Row Space
> If $A$ is an $m \times n$ matrix, each row of $A$ has $n$ entries and can be identified with a vector in $\mathbb{R}^n$. The set of all linear combinations of the row vectors is the **row space** of $A$, written $\operatorname{Row} A$. Since the rows of $A$ are the columns of $A^T$,
>
> $$
> \operatorname{Row} A = \operatorname{Col} A^T ,
> $$
>
> and $\operatorname{Row} A$ is a subspace of $\mathbb{R}^n$ (Theorem §24.3 for $A^T$). For example, the rows of $A = \begin{bmatrix} 1 & -3 & -2 \\ -5 & 9 & 1 \end{bmatrix}$ span the subspace $\operatorname{Row} A = \operatorname{Span}\{(1, -3, -2), (-5, 9, 1)\}$ of $\mathbb{R}^3$. Row operations do not change the row space, and the nonzero rows of an echelon form of $A$ form a basis of $\operatorname{Row} A$ ([[§28 Rank#^thm-28-1|Theorem §28.1]], Theorem 13 of 4.6; used in [[§25 Linearly Independent Sets; Bases#^rem-25-2|Remark §25.2]]). Row operations change the linear dependence relations among the rows, though, so an echelon form does not tell which rows *of $A$* to keep.
>
> *Lay: 4.6, Definition (text)*
> *Source: 235 lecture L16*

^def-24-3

## The Contrast Between Nul A and Col A

> [!example] Example §24.4: Nul A and Col A Live in Different Spaces
> Let
>
> $$
> A = \begin{bmatrix} 2 & 4 & -2 & 1 \\ -2 & -5 & 7 & 3 \\ 3 & 7 & -8 & 6 \end{bmatrix} .
> $$
>
> **(a) Where they live.** The columns of $A$ have three entries, so $\operatorname{Col} A$ is a subspace of $\mathbb{R}^k$ with $k = 3$. A vector $\mathbf{x}$ for which $A\mathbf{x}$ is defined has four entries, so $\operatorname{Nul} A$ is a subspace of $\mathbb{R}^k$ with $k = 4$.
>
> **(b) Finding a vector in each.** Any column is in $\operatorname{Col} A$, for instance $(2, -2, 3)$. For $\operatorname{Nul} A$, row reduce:
>
> $$
> [A \ \mathbf{0}] \sim \begin{bmatrix} 1 & 0 & 9 & 0 & 0 \\ 0 & 1 & -5 & 0 & 0 \\ 0 & 0 & 0 & 1 & 0 \end{bmatrix} ,
> $$
>
> so $x_1 = -9x_3$, $x_2 = 5x_3$, $x_4 = 0$, $x_3$ free; $x_3 = 1$ gives $(-9, 5, 1, 0) \in \operatorname{Nul} A$.
>
> **(c) Testing membership.** Let $\mathbf{u} = (3, -2, -1, 0)$ and $\mathbf{v} = (3, -1, 3)$. For $\mathbf{u}$, no description of $\operatorname{Nul} A$ is needed:
>
> $$
> A\mathbf{u} = \begin{bmatrix} 6 - 8 + 2 + 0 \\ -6 + 10 - 7 + 0 \\ 9 - 14 + 8 + 0 \end{bmatrix} = \begin{bmatrix} 0 \\ -3 \\ 3 \end{bmatrix} \ne \mathbf{0},
> $$
>
> so $\mathbf{u} \notin \operatorname{Nul} A$; and with four entries $\mathbf{u}$ cannot be in $\operatorname{Col} A \subseteq \mathbb{R}^3$. For $\mathbf{v}$, row reduce $[A \ \mathbf{v}]$:
>
> $$
> \begin{bmatrix} 2 & 4 & -2 & 1 & 3 \\ -2 & -5 & 7 & 3 & -1 \\ 3 & 7 & -8 & 6 & 3 \end{bmatrix} \sim \begin{bmatrix} 2 & 4 & -2 & 1 & 3 \\ 0 & 1 & -5 & -4 & -2 \\ 0 & 0 & 0 & 17 & 1 \end{bmatrix} .
> $$
>
> There is no row $[0 \ 0 \ 0 \ 0 \ b]$ with $b \ne 0$, so $A\mathbf{x} = \mathbf{v}$ is consistent and $\mathbf{v} \in \operatorname{Col} A$; with three entries, $\mathbf{v}$ cannot be in $\operatorname{Nul} A \subseteq \mathbb{R}^4$.
>
> *Lay: Examples 4.2.5–4.2.7*

^ex-24-4

When $A$ is not square, as here, $\operatorname{Nul} A$ and $\operatorname{Col} A$ live in different "universes". When $A$ is square they share the zero vector, and in special cases some nonzero vectors belong to both. A surprising connection between them appears in [[§28 Rank#^thm-28-3|Theorem §28.3]] (the Rank Theorem).

> [!remark] Remark: Contrast Between Nul A and Col A for an m × n Matrix A
> | | $\operatorname{Nul} A$ | $\operatorname{Col} A$ |
> |---|---|---|
> | 1 | a subspace of $\mathbb{R}^n$ | a subspace of $\mathbb{R}^m$ |
> | 2 | defined implicitly: only a condition ($A\mathbf{x} = \mathbf{0}$) is given | defined explicitly: you are told how to build its vectors |
> | 3 | finding vectors takes row operations on $[A \ \mathbf{0}]$ | easy to find vectors: the columns of $A$ and their combinations |
> | 4 | no obvious relation to the entries of $A$ | each column of $A$ is in $\operatorname{Col} A$ |
> | 5 | a typical $\mathbf{v}$ satisfies $A\mathbf{v} = \mathbf{0}$ | for a typical $\mathbf{v}$, $A\mathbf{x} = \mathbf{v}$ is consistent |
> | 6 | easy to test $\mathbf{v}$: compute $A\mathbf{v}$ | testing $\mathbf{v}$ takes row operations on $[A \ \mathbf{v}]$ |
> | 7 | $= \{\mathbf{0}\}$ iff $A\mathbf{x} = \mathbf{0}$ has only the trivial solution | $= \mathbb{R}^m$ iff $A\mathbf{x} = \mathbf{b}$ has a solution for every $\mathbf{b}$ |
> | 8 | $= \{\mathbf{0}\}$ iff $\mathbf{x} \mapsto A\mathbf{x}$ is one-to-one | $= \mathbb{R}^m$ iff $\mathbf{x} \mapsto A\mathbf{x}$ maps $\mathbb{R}^n$ onto $\mathbb{R}^m$ |
>
> Item 8 restates Theorems 11 and 12(a) of 1.9 ([[§9 The Matrix of a Linear Transformation#^thm-9-2|Theorem §9.2]], [[§9 The Matrix of a Linear Transformation#^thm-9-3|Theorem §9.3]]).

^rem-24-2

## Kernel and Range of a Linear Transformation

> [!definition] Definition §24.4: Linear Transformation
> A **linear transformation** $T$ from a vector space $V$ into a vector space $W$ is a rule that assigns to each vector $\mathbf{x}$ in $V$ a unique vector $T(\mathbf{x})$ in $W$, such that
>
> (i) $T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v})$ for all $\mathbf{u}$, $\mathbf{v}$ in $V$, and
>
> (ii) $T(c\mathbf{u}) = cT(\mathbf{u})$ for all $\mathbf{u}$ in $V$ and all scalars $c$.
>
> This generalizes the definition for $V = \mathbb{R}^n$, $W = \mathbb{R}^m$ in [[§8 Introduction to Linear Transformations#^def-8-3|Definition §8.3]] (1.8).
>
> *Lay: 4.2, Definition*

^def-24-4

> [!definition] Definition §24.5: Kernel and Range
> Let $T: V \to W$ be a linear transformation. The **kernel** (or **null space**) of $T$ is the set of all $\mathbf{u}$ in $V$ such that $T(\mathbf{u}) = \mathbf{0}$, the zero vector of $W$. The **range** of $T$ is the set of all vectors in $W$ of the form $T(\mathbf{x})$ for some $\mathbf{x}$ in $V$. If $T$ is a matrix transformation, $T(\mathbf{x}) = A\mathbf{x}$, then the kernel and the range of $T$ are the null space and the column space of $A$.
>
> *Lay: 4.2 (text)*

^def-24-5

> [!theorem] Theorem §24.5: Kernel and Range Are Subspaces
> If $T: V \to W$ is a linear transformation, then the kernel of $T$ is a subspace of $V$ and the range of $T$ is a subspace of $W$.
>
> *Lay: 4.2 (text); Exercise 30*

^thm-24-5

> [!proof]+ Proof
> First, $T(\mathbf{0}) = T(0 \cdot \mathbf{0}) = 0\,T(\mathbf{0}) = \mathbf{0}$ by (ii) and [[§23 Vector Spaces and Subspaces#^prop-23-2|Proposition §23.2]].
>
> **Kernel** (Lay: "essentially the same" as the proof of Theorem §24.1). $\mathbf{0}$ is in the kernel. If $T(\mathbf{u}) = \mathbf{0}$ and $T(\mathbf{v}) = \mathbf{0}$, then $T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v}) = \mathbf{0}$ and $T(c\mathbf{u}) = cT(\mathbf{u}) = c\mathbf{0} = \mathbf{0}$.
>
> **Range.** $\mathbf{0} = T(\mathbf{0})$ is in the range. If $\mathbf{w}_1 = T(\mathbf{x}_1)$ and $\mathbf{w}_2 = T(\mathbf{x}_2)$ are in the range, then $\mathbf{w}_1 + \mathbf{w}_2 = T(\mathbf{x}_1 + \mathbf{x}_2)$ and $c\mathbf{w}_1 = T(c\mathbf{x}_1)$ are in the range.

^pf-24-5

*Uses:* [[§24 Null Spaces, Column Spaces, and Linear Transformations#^def-24-4|Def. §24.4]], [[§24 Null Spaces, Column Spaces, and Linear Transformations#^def-24-5|Def. §24.5]], [[§23 Vector Spaces and Subspaces#^def-23-2|Def. §23.2]], [[§23 Vector Spaces and Subspaces#^prop-23-2|§23.2]]

> [!remark]- Connections
> - Rigorous treatment: linear maps [[§7 Vector Space of Linear Maps#^ladr-3-1|LADR 3.1]]; null space and range are subspaces, [[§8 Null Spaces and Ranges#^ladr-3-13|LADR 3.13]], [[§8 Null Spaces and Ranges#^ladr-3-18|LADR 3.18]]; injective iff null space $= \{0\}$, [[§8 Null Spaces and Ranges#^ladr-3-15|LADR 3.15]] (item 8 of the table). Their dimensions add up to $\dim V$: the [[§8 Null Spaces and Ranges#^ladr-3-21|fundamental theorem of linear maps (LADR 3.21)]], whose matrix form is the Rank Theorem, [[§28 Rank#^thm-28-3|Theorem §28.3]].
> - One-to-one and onto as properties of functions: [[§9 Injections, Surjections and Bijections#^def-9-1|250 Def. §9.1]].

In applications a subspace usually arises as the kernel or the range of a suitable linear transformation. For instance, the solutions of a homogeneous linear differential equation form the kernel of a linear transformation built from derivatives.

> [!example] Example §24.5: Differentiation (Calculus Required)
> **(a)** Let $V$ be the space of real-valued functions $f$ on $[a, b]$ that are differentiable with continuous derivative on $[a, b]$, let $W = C[a, b]$ be the space of continuous functions on $[a, b]$, and let $D: V \to W$ send $f$ to $f'$. The rules $D(f + g) = D(f) + D(g)$ and $D(cf) = cD(f)$ of calculus say that $D$ is a linear transformation. Its kernel is the set of constant functions on $[a, b]$ (a function with $f' = 0$ on an interval is constant, by the Mean Value Theorem), and its range is all of $W$ (every continuous $g$ is the derivative of $f(t) = \int_a^t g(s)\,ds$, by the Fundamental Theorem of Calculus). Lay states these two facts ("it can be shown"); the parenthetical reasons are the standard calculus theorems.
>
> **(b)** The differential equation
>
> $$
> y'' + \omega^2 y = 0 , \qquad (4)
> $$
>
> with $\omega$ constant, describes a weighted spring, a pendulum, and the voltage in an inductance–capacitance circuit. Its solution set is precisely the kernel of the linear transformation that maps $y = f(t)$ to $f''(t) + \omega^2 f(t)$, so it is a vector space. Finding it explicitly is a problem in differential equations; it is the space of functions $c_1\cos\omega t + c_2\sin\omega t$ (Lay's Exercise 19 of 4.1).
>
> *Lay: Examples 4.2.8 and 4.2.9*

^ex-24-5
