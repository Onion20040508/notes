---
type: section
subject: "[[Group Theory]]"
chapter: 9
section: 49
tags: [group-theory, math493]
---
← [[§48 Solvable Groups]] · ↑ [[· 9 Characters, Commutators and Solvable Groups]] · [[§50 S₃, S₄, Aₙ and GLₙ]] →

*Reference: not covered in the Pinter chapters used so far.*

> [!remark] Remark: The Derived Subgroup
> Worksheet 9 recalls the commutator subgroup $D(G) = [G, G]$ ([[§47 Commutators#^def-47-2|Definition §47.2]]), also called the *derived subgroup*. Its [[§38 Normal Subgroups#^def-38-1|normality]] (WS 9.4) and the commutativity of $G^{\mathrm{ab}} = G/D(G)$ (WS 9.5) were proved in [[§47 Commutators|§47]]: Properties of the Commutator Subgroup ([[§47 Commutators#^prop-47-4|Proposition §47.4]]) and The Abelianization Is Abelian ([[§47 Commutators#^prop-47-6|Proposition §47.6]]).

^rem-49-1

> [!definition] Definition §49.1: Derived Series
> The **derived series** of $G$ is the chain $G \trianglerighteq D(G) \trianglerighteq D(D(G)) \trianglerighteq \cdots$. Its $k$-th term is written $D_k(G)$: $D_0(G) = G$ and $D_{k+1}(G) = D(D_k(G))$.
>
> *Source: WS 9*

^def-49-1

> [!theorem] Theorem §49.1: Solvability via the Derived Series
> $G$ is [[§48 Solvable Groups#^def-48-1|solvable]] if and only if $D_N(G) = \{e\}$ for some $N$.
>
> *Source: WS 9.6*

^thm-49-1

> [!proof]- Proof
> *[To be proved.]*

^pf-49-1

> [!example] Example §49.1: Derived Series of $S_3$, $S_4$ and $S_n$
> 1. $S_3 \trianglerighteq A_3 \trianglerighteq \{e\}$: $D(S_3) = A_3$ by The Commutator Subgroup and Characters of $S_n$ ([[§47 Commutators#^thm-47-5|Theorem §47.5]]), and $D(A_3) = \{e\}$ since $A_3$ is [[§1 The Definition of a Group#^def-1-2|abelian]].
> 2. $S_4 \trianglerighteq A_4 \trianglerighteq K \trianglerighteq \{e\}$. Here $D(A_4) = K$: on one hand $A_4/K \cong \mathbb{Z}/3\mathbb{Z}$ is abelian, so every [[§47 Commutators#^def-47-1|commutator]] of $A_4$ maps to the identity of $A_4/K$, i.e. $D(A_4) \subseteq K$; on the other hand $(1\,2\,3)(1\,2\,4)(1\,2\,3)^{-1}(1\,2\,4)^{-1} = (1\,2)(3\,4)$, and $D(A_4)$ is [[§47 Commutators#^prop-47-4|normal]] in $A_4$, so it also contains the conjugates $(1\,3)(2\,4)$ and $(1\,4)(2\,3)$ of $(1\,2)(3\,4)$ by $(1\,2\,3)$ and $(1\,3\,2)$. Finally $D(K) = \{e\}$ since $K$ is abelian.
> 3. For $n \geq 5$: $D(S_n) = A_n$ and $D(A_n) = A_n$ (Characters of $A_n$ Are Trivial for $n \geq 5$, [[§47 Commutators#^thm-47-10|Theorem §47.10]]), so the series is $S_n \trianglerighteq A_n \trianglerighteq A_n \trianglerighteq \cdots$ and never reaches $\{e\}$.
>
> *Source: not from class*

^ex-49-1

> [!theorem] Corollary §49.2: $A_n$ and $S_n$ Are Not Solvable for $n \geq 5$
> For $n \geq 5$, neither $A_n$ nor $S_n$ is [[§48 Solvable Groups#^def-48-1|solvable]]. Hence $S_n$ is solvable if and only if $n \leq 4$.
>
> *Source: not from class*

^cor-49-2

> [!proof]+ Proof
> Let $n \geq 5$ and suppose $\{e\} = G_0 \trianglelefteq \cdots \trianglelefteq G_N = A_n$ is a chain with abelian quotients. Let $j$ be the largest index with $G_j \neq A_n$. Then $G_j \trianglelefteq G_{j+1} = A_n$, and $A_n$ is [[§43 Simple Groups#^def-43-1|simple]] ([[§43 Simple Groups#^thm-43-9|Theorem §43.9]]), so $G_j = \{e\}$; but then $G_{j+1}/G_j \cong A_n$ is not abelian, a contradiction. So $A_n$ is not solvable, and neither is $S_n$, which contains $A_n$ (Subgroups of Solvable Groups Are Solvable, [[§48 Solvable Groups#^prop-48-2|Proposition §48.2]]). For $n \leq 4$, $S_n$ is a subgroup of $S_4$ (fixing the remaining points), hence solvable ([[§48 Solvable Groups#^prop-48-1|Proposition §48.1]]). (This argument uses simplicity of $A_n$; by WS 9.6 ([[§49 The Derived Series#^thm-49-1|Theorem §49.1]]) the derived series in [[§49 The Derived Series#^ex-49-1|Example §49.1]] gives the same conclusion.)

^pf-49-2

*Uses:* [[§48 Solvable Groups#^def-48-1|Def. §48.1]], [[§43 Simple Groups#^def-43-1|Def. §43.1]], [[§43 Simple Groups#^thm-43-9|§43.9]], [[§48 Solvable Groups#^prop-48-2|§48.2]], [[§48 Solvable Groups#^prop-48-1|§48.1]], [[§49 The Derived Series#^thm-49-1|§49.1]], [[§49 The Derived Series#^ex-49-1|Ex. §49.1]]
