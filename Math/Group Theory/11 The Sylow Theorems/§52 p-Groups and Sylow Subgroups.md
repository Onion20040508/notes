---
type: section
subject: "[[Group Theory]]"
chapter: 11
section: 52
tags: [group-theory, math493]
---
← [[§51 S₃, S₄ and Aₙ]] · ↑ [[· 11 The Sylow Theorems]] · [[§53 The Sylow Theorems]] →

*Reference: Worksheet 10. Throughout, $p$ is a prime.*

Worksheet 10 begins by restating the definition of a $p$-group, already met with the [[§35 The Center#^def-35-2|center]]:

![[§35 The Center#^def-35-3]]

Nontrivial $p$-groups have nontrivial center ([[§35 The Center#^thm-35-3|Theorem §35.3]], PS 3.5).

> [!definition] Definition §52.1: $p$-Subgroup
> For a group $G$, a **$p$-subgroup** of $G$ is a [[§4 Subgroups#^def-4-1|subgroup]] of $G$ which is a $p$-group ([[§35 The Center#^def-35-3|Def. §35.3]]).
>
> *Source: WS 10*

^def-52-1

> [!theorem] Proposition §52.1: Fixed Points of a $p$-Group Action
> Let $P$ be a $p$-group and let $X$ be a finite set on which $P$ [[§25 Actions#^def-25-1|acts]]. If $|X| \not\equiv 0 \pmod p$, then $P$ [[§26 Stabilizers and Fixed Points#^def-26-2|fixes]] some point of $X$.
>
> *Source: WS 10.1*

^prop-52-1

> [!proof]- Proof
> *[To be proved.]*

^pf-52-1

Let $G$ be a finite group, and factor $|G| = p^k m$ where $p$ does not divide $m$.

> [!definition] Definition §52.2: Sylow $p$-Subgroup
> A **Sylow $p$-subgroup** of $G$ is a [[§4 Subgroups#^def-4-1|subgroup]] of $G$ of [[§4 Subgroups#^def-4-6|order]] $p^k$.
>
> *Source: WS 10*

^def-52-2

Worksheet 10 quotes from the coming problem set the order

$$ |GL_n(\mathbb{F}_p)| = p^{\binom{n}{2}} \prod_{k=1}^{n} (p^k - 1) $$

(homework, not proved here), so a Sylow $p$-subgroup of $GL_n(\mathbb{F}_p)$ ([[§3 Basic Examples of Groups#^def-3-6|Def. §3.6]], with $\mathbb{F}_p$ the field of [[§8 Invertibility and Unit Groups#^prop-8-4|§8.4]]) would be a group of order $p^{\binom{n}{2}}$.

> [!theorem] Proposition §52.2: The Unitriangular Matrices Are a Sylow $p$-Subgroup of $GL_n(\mathbb{F}_p)$
> Let $P \subseteq GL_n(\mathbb{F}_p)$ be the group of matrices of the form
>
> $$ \begin{bmatrix} 1 & b_{12} & b_{13} & \cdots & b_{1(n-1)} & b_{1n} \\ 0 & 1 & b_{23} & \cdots & b_{2(n-1)} & b_{2n} \\ 0 & 0 & 1 & \cdots & b_{3(n-1)} & b_{3n} \\ & & & \ddots & & \vdots \\ 0 & 0 & 0 & \cdots & 1 & b_{(n-1)n} \\ 0 & 0 & 0 & \cdots & 0 & 1 \end{bmatrix}. $$
>
> Then $P$ is a Sylow $p$-subgroup of $GL_n(\mathbb{F}_p)$ ([[§52 p-Groups and Sylow Subgroups#^def-52-2|Def. §52.2]]).
>
> *Source: WS 10.2*

^prop-52-2

> [!proof]- Proof
> *[To be proved.]*

^pf-52-2

*$GL_n$ elsewhere:* ← [[§48 S₃, Aₙ and GLₙ#GLₙ, SLₙ and O(n)|Chapter 9]] · no later appearance yet · [[Matrix groups GLₙ, SLₙ and O(n)|all appearances]]
