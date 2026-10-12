---
type: section
subject: "[[Group Theory]]"
chapter: 10
section: 51
tags: [group-theory, math493]
---
← [[§50 S₃, S₄, Aₙ and GLₙ]] · ↑ [[· 10 The Sylow Theorems]] · [[§52 The Sylow Theorems]] →

*Reference: Worksheet 10. Throughout, $p$ is a prime.*

> [!remark] Remark: The Question
> By Lagrange ([[§29 The Index and Lagrange's Theorem#^thm-29-2|Theorem §29.2]]), if $H \leq G$ and $G$ is finite, then $|H|$ divides $|G|$. Conversely, if $m$ divides $|G|$, is there a subgroup of order $m$? Not in general: $A_4$ has order $12$ but no subgroup of order $6$ (The Converse of Lagrange Fails: $A_4$, [[§29 The Index and Lagrange's Theorem#^ex-29-1|Example §29.1]]). The lecture's answer is yes when $m$ is a power of a prime. The case of a prime $m = p$ is Cauchy's theorem ([[§29 The Index and Lagrange's Theorem#^thm-29-6|Theorem §29.6]]), and the case of the largest power of $p$ dividing $|G|$ is the First Sylow Theorem ([[§52 The Sylow Theorems#^thm-52-4|Theorem §52.4]]). For example, $|S_3| = 6$, and $\langle (1\,2) \rangle$ and $\langle (1\,2\,3) \rangle$ have orders $2$ and $3$. The lecture also asked for a subgroup of order $8$ in $S_4$, of order $24$ ([[§51 p-Groups and Sylow Subgroups#^ex-51-1|Example §51.1]] below).
>
> *Source: lecture 10/12*

^rem-51-1

Worksheet 10 begins by restating the definition of a $p$-group, already met with the [[§35 The Center#^def-35-2|center]]:

![[§35 The Center#^def-35-3]]

Nontrivial $p$-groups have nontrivial center ([[§35 The Center#^thm-35-3|Theorem §35.3]], PS 3.5).

> [!definition] Definition §51.1: $p$-Subgroup
> For a group $G$, a **$p$-subgroup** of $G$ is a [[§4 Subgroups#^def-4-1|subgroup]] of $G$ which is a $p$-group ([[§35 The Center#^def-35-3|Def. §35.3]]).
>
> *Source: WS 10*

^def-51-1

> [!theorem] Proposition §51.1: Fixed Points of a $p$-Group Action
> Let $P$ be a $p$-group and let $X$ be a finite set on which $P$ [[§25 Actions#^def-25-1|acts]]. If $|X| \not\equiv 0 \pmod p$, then $P$ [[§26 Stabilizers and Fixed Points#^def-26-2|fixes]] some point of $X$.
>
> *Source: WS 10.1*

^prop-51-1

> [!proof]- Proof
> *[To be proved.]*

^pf-51-1

Let $G$ be a finite group, and factor $|G| = p^k m$ where $p$ does not divide $m$.

> [!definition] Definition §51.2: Sylow $p$-Subgroup
> A **Sylow $p$-subgroup** of $G$ is a [[§4 Subgroups#^def-4-1|subgroup]] of $G$ of [[§4 Subgroups#^def-4-6|order]] $p^k$.
>
> *Source: WS 10*

^def-51-2

> [!example] Example §51.1: Sylow Subgroups of $S_3$ and $S_4$
> 1. $|S_3| = 6 = 2 \cdot 3$. The [[§51 p-Groups and Sylow Subgroups#^def-51-2|Sylow]] $2$-subgroups are $\langle (1\,2) \rangle$, $\langle (1\,3) \rangle$, $\langle (2\,3) \rangle$, and the only Sylow $3$-subgroup is $A_3 = \langle (1\,2\,3) \rangle$.
> 2. $|S_4| = 24 = 2^3 \cdot 3$. The Sylow $2$-subgroups have order $8$: they are the three subgroups $K \cup \tau K$ ($\tau$ a transposition) containing $K$, found in The Correspondence for $S_4$ and $K$ ([[§45 S₃, S₄, A₄ and A₅#^ex-45-2|Example §45.2]]). The Sylow $3$-subgroups are the four subgroups $\langle (1\,2\,3) \rangle$, $\langle (1\,2\,4) \rangle$, $\langle (1\,3\,4) \rangle$, $\langle (2\,3\,4) \rangle$.
>
> The numbers of Sylow subgroups are $3, 1$ for $S_3$ and $3, 4$ for $S_4$, each $\equiv 1 \pmod p$, as the Third Sylow Theorem ([[§52 The Sylow Theorems#^thm-52-7|Theorem §52.7]]) predicts.
>
> *Source: lecture 10/12; the counts are not from class*

^ex-51-1

> [!theorem] Proposition §51.2: The Order of $GL_n(\mathbb{F}_p)$
>
> $$ |GL_n(\mathbb{F}_p)| = p^{\binom{n}{2}} \prod_{k=1}^{n} (p^k - 1). $$
>
> In particular a [[§51 p-Groups and Sylow Subgroups#^def-51-2|Sylow $p$-subgroup]] of $GL_n(\mathbb{F}_p)$ ([[§3 Basic Examples of Groups#^def-3-6|Def. §3.6]], with $\mathbb{F}_p$ the field of [[§8 Invertibility and Unit Groups#^prop-8-4|§8.4]]) has order $p^{\binom{n}{2}}$, since $p \nmid p^k - 1$.
>
> *Source: stated on WS 10; PS 6*

^prop-51-2

> [!proof]- Proof
> *[To be proved.]*

^pf-51-2

Worksheet 10 quotes this order from the coming problem set (Problem Set 6, open; the proof is held back until it is submitted).

> [!theorem] Proposition §51.3: The Unitriangular Matrices Are a Sylow $p$-Subgroup of $GL_n(\mathbb{F}_p)$
> Let $P \subseteq GL_n(\mathbb{F}_p)$ be the group of matrices of the form
>
> $$ \begin{bmatrix} 1 & b_{12} & b_{13} & \cdots & b_{1(n-1)} & b_{1n} \\ 0 & 1 & b_{23} & \cdots & b_{2(n-1)} & b_{2n} \\ 0 & 0 & 1 & \cdots & b_{3(n-1)} & b_{3n} \\ & & & \ddots & & \vdots \\ 0 & 0 & 0 & \cdots & 1 & b_{(n-1)n} \\ 0 & 0 & 0 & \cdots & 0 & 1 \end{bmatrix}. $$
>
> Then $P$ is a Sylow $p$-subgroup of $GL_n(\mathbb{F}_p)$ ([[§51 p-Groups and Sylow Subgroups#^def-51-2|Def. §51.2]]).
>
> *Source: WS 10.2*

^prop-51-3

> [!proof]- Proof
> *[To be proved.]*

^pf-51-3

*$GL_n$ elsewhere:* ← [[§50 S₃, S₄, Aₙ and GLₙ#GLₙ, SLₙ and O(n)|Chapter 9]] · no later appearance yet · [[Matrix groups GLₙ, SLₙ and O(n)|all appearances]]
