---
type: section
subject: "[[Group Theory]]"
chapter: 1
section: 1
tags: [group-theory, math493]
---
↑ [[· 1 Groups and Subgroups]] · [[§2 First Consequences of the Axioms]] →

*Reference: Pinter Ch. 2 (operations), Ch. 3 (the definition of groups).*

> [!definition] Definition §1.1: Group
> A **group** $G$ is a set with a binary operation $*: G \times G \to G$ obeying the properties:
> 1. **(Identity)** There is an element $e \in G$ such that $e * g = g * e = g$ for all $g \in G$.
> 2. **(Inverses)** For all $g \in G$, there is an element $g^{-1}$ obeying $g * g^{-1} = g^{-1} * g = e$.
> 3. **(Associativity)** For all $g_1, g_2, g_3 \in G$, we have $(g_1 * g_2) * g_3 = g_1 * (g_2 * g_3)$.

^def-1-1

> [!remark]- Connections
> - MATH 590 counterpart (same axioms, different order): [[§21 Algebra Prerequisites꞉ Groups#^def-21-1|590 Definition §21.1: Group]].
> - A group with a compatible topology: [[§5 Topological Groups and Classical Matrix Groups#^def-5-1|591 Def. §5.1]] (topological group), the setting of the 591 matrix groups and actions.

> [!definition] Definition §1.2: Abelian Group
> A group $G$ is **abelian** (or **commutative**) if $a * b = b * a$ for all $a, b \in G$. Commutativity is *not* one of the group axioms; groups such as $S_n$ ($n \geq 3$) and $GL_n(k)$ ($n \geq 2$) are non-abelian.

^def-1-2

> [!remark] Remark: Notation
> Depending on context, we may denote $*$ by $*$, $\times$, $\cdot$, or no symbol at all, and the identity has been written $1$ (Worksheet 1), $e$ (lectures), or $\operatorname{Id}$. These notes write $e$, and $e_G$, $e_H$, … whenever more than one group is in play. When the operation is written additively ($+$), the identity is written $0$ and the inverse of $g$ is written $-g$. Additive notation is used only for abelian groups (Worksheet 3: “we never use these notations for a non-abelian group”), so the symbol $+$ itself signals commutativity.

^rem-1-1

> [!remark]- Connections
> - Every vector space is an abelian group under addition: [[§2 Definition of Vector Space#^ladr-1-20|LADR 1.20]] (commutativity, associativity, additive identity and inverses).

> [!theorem] Proposition §1.1: Generalized Associativity
> For any $g_1, \ldots, g_n \in G$, all ways of parenthesizing the product $g_1 * g_2 * \cdots * g_n$ give the same element. Consequently parentheses may be omitted from products, as they are from now on.

^prop-1-1

> [!proof]+ Proof
> Let $L_n = (\cdots((g_1g_2)g_3)\cdots)g_n$ be the left-normed product; we show by induction on $n$ that every parenthesization equals $L_n$. The cases $n \leq 2$ are trivial. For $n \geq 3$, any parenthesization has an outermost multiplication $A \cdot B$, where $A$ is a parenthesization of $g_1 \cdots g_j$ and $B$ of $g_{j+1} \cdots g_n$ for some $1 \leq j < n$. By induction $A = L_j$ and $B$ equals the left-normed product of $g_{j+1}, \ldots, g_n$. If $j = n - 1$, then $B = g_n$ and $AB = L_{n-1}g_n = L_n$. If $j < n - 1$, write $B = B'g_n$ with $B'$ the left-normed product of $g_{j+1}, \ldots, g_{n-1}$; then $AB = A(B'g_n) = (AB')g_n$ by axiom (3), and $AB'$ is a parenthesization of $g_1 \cdots g_{n-1}$, hence equals $L_{n-1}$ by induction. So $AB = L_{n-1}g_n = L_n$.

^pf-1-1

*Uses:* [[§1 The Definition of a Group#^def-1-1|Def. §1.1]], [[§1 The Set ℕ of Natural Numbers#^thm-1-1|451 §1.1]]

![[m493-1-1.svg]]
*The five ways to parenthesize $g_1 g_2 g_3 g_4$, joined by an edge when a single use of axiom (3), $(xy)z = x(yz)$, turns one into the other. The graph is connected, so all five products are equal; the proof above routes every bracketing to the left-normed product $L_4$ (blue).*

> [!remark] Remark: Comparison with MATH 590
> This is the same definition as in the algebra-prerequisites section of the topology notes ([[§21 Algebra Prerequisites꞉ Groups#^def-21-1|590 Def. §21.1]]), with the axioms listed in a different order. [[§2 First Consequences of the Axioms|WS 1.1–1.4]] below establish the basic uniqueness and cancellation facts, which appeared as [[§21 Algebra Prerequisites꞉ Groups#^rem-21-2|remarks in the 590 notes]].

^rem-1-2
