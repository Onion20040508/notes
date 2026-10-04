---
type: section
subject: "[[Group Theory]]"
chapter: 8
section: 44
tags: [group-theory, math493]
---
← [[§43 Simple Groups]] · ↑ [[· 8 Normal Subgroups and Quotient Groups]] · [[§45 Characters]] →

*The recurring groups as Chapter 8 saw them: which subgroups are normal, what the quotients are, and which groups are simple. The simplicity of $A_5$ and of $A_n$ for $n \geq 5$ is the subject of [[§43 Simple Groups|§43]] itself; the parts below gather the rest, one group at a time, in order.*

## The Symmetric Group S₃

$S_3$ has exactly three normal subgroups, $\{e\}$, $A_3$ and $S_3$: $\langle (1\,2) \rangle$ is the standard non-normal subgroup, while $A_3$ is normal of index $2$ and $S_3/A_3 \cong \mathbb{Z}/2\mathbb{Z}$, realized by the subgroup $\langle (2\,3) \rangle$. $S_3$ also shows that a product $AB$ of subgroups need not be a subgroup, and it returns as the quotient $S_4/V$ and as $PSL_2(\mathbb{F}_2)$.

![[§38 Normal Subgroups#^ex-38-1]]

![[§39 Sources of Normal Subgroups#^ex-39-1]]

![[§39 Sources of Normal Subgroups#^prop-39-3]]

![[§39 Sources of Normal Subgroups#^ex-39-3]]

![[§40 Quotient Groups#^ex-40-3]]

![[§40 Quotient Groups#^rem-40-3]]

> [!example] Example §44.1: The Second Isomorphism Theorem in Action
> 1. $G = S_3$, $N = A_3$ ([[§21 The Sign Homomorphism and the Alternating Group#^def-21-3|Def. §21.3]]), $H = \langle (1\,2) \rangle$: $H \cap N = \{e\}$ and $HN = S_3$, so $\langle (1\,2) \rangle \cong S_3/A_3$.
> 2. $G = S_4$, $N = V$ ([[§39 Sources of Normal Subgroups#^ex-39-3|Ex. §39.3]]), $H = \operatorname{Stab}(4) \cong S_3$ ([[§26 Stabilizers and Fixed Points#^def-26-1|Def. §26.1]]): every non-identity element of $V$ moves $4$, so $H \cap V = \{e\}$, and $HV/V \cong H$ has $6 = 24/4 = |S_4/V|$ elements, so $HV/V = S_4/V$. Hence $S_4/V \cong S_3$, recovering [[§43 Simple Groups#^prop-43-10|The Pair-Partition Homomorphism]] (§43) by a second route.

^ex-44-1

![[§42 The Second and Third Isomorphism Theorems#^ex-42-1]]

$S_3/A_3$ first appears as item (3) of [[§40 Quotient Groups#^ex-40-1|Quotient Groups]] (in the ℤ part); $S_4/V \cong S_3$ and $PSL_2(\mathbb{F}_2) \cong S_3$ are in [[§43 Simple Groups#^prop-43-10|The Pair-Partition Homomorphism]] and [[§43 Simple Groups#^ex-43-3|The Two Exceptions]] (in the $S_4$ part).

*$S_3$ elsewhere:* ← [[§36 S₃, S₄ and GLₙ#The Symmetric Group S₃|Chapter 7]] · [[§47 S₃, Aₙ and GLₙ#The Symmetric Group S₃|Chapter 9]] → · [[The symmetric group S₃|all appearances]]

## S₄, A₄ and the Klein Four-Group V

The normal subgroups of $S_4$ are $\{e\}$, $V$, $A_4$ and $S_4$, read off from its class sizes. The pair-partition homomorphism $S_4 \to S_3$ has kernel $V$, so $S_4/V \cong S_3$; inside $A_4$ it makes $V$ normal and keeps $(1\,2\,3)$ and $(1\,3\,2)$ apart, which is why $A_4$ is the one non-simple $A_n$ with $n \geq 3$.

![[§43 Simple Groups#^prop-43-10]]

![[§43 Simple Groups#^ex-43-1]]

![[§43 Simple Groups#^rem-43-6]]

![[§43 Simple Groups#^ex-43-3]]

The normal subgroups of $S_4$ and the Second Isomorphism Theorem route to $S_4/V \cong S_3$ are in [[§39 Sources of Normal Subgroups#^ex-39-3|Normal Subgroups of S₃ and S₄]] and [[§44 S₃, S₄, A₄ and A₅#^ex-44-1|The Second Isomorphism Theorem in Action]] (in the $S_3$ part); [[§43 Simple Groups#^cor-43-11|Which Aₙ Are Simple]] records $A_4$ as the exception.

*$S_4$, $A_4$ and $V$ elsewhere:* ← [[§36 S₃, S₄ and GLₙ#S₄, A₄ and the Klein Four-Group V|Chapter 7]] · no later appearance yet · [[S₄, A₄ and the Klein four-group|all appearances]]

## The Alternating Groups Aₙ

$A_n$ is normal in $S_n$ twice over, as a subgroup of index $2$ and as the kernel of the sign, and $S_n/A_n \cong \{\pm 1\}$; so $S_n$ is not simple for $n \geq 3$. [[§43 Simple Groups|§43]] then proves that $A_5$, and every $A_n$ with $n \geq 5$, is simple.

![[§39 Sources of Normal Subgroups#^ex-39-2]]

![[§41 The First Isomorphism Theorem#^ex-41-1]]

Index $2$ is item (2) of [[§39 Sources of Normal Subgroups#^ex-39-1|Index-2 Examples]] (in the $S_3$ part). In [[§43 Simple Groups|§43]]: [[§43 Simple Groups#^cor-43-2|Sₙ Is Not Simple for n ≥ 3]], [[§43 Simple Groups#^prop-43-4|Homomorphisms into a Simple Group]] (ℤ/3ℤ into A₅), [[§43 Simple Groups#^prop-43-6|A₅ Is Simple]], [[§43 Simple Groups#^thm-43-7|A₅ Is the Smallest Non-Abelian Simple Group]], [[§43 Simple Groups#^lem-43-8|3-Cycles Are Conjugate in Aₙ]], [[§43 Simple Groups#^thm-43-9|Aₙ Is Simple for n ≥ 5]], [[§43 Simple Groups#^cor-43-11|Which Aₙ Are Simple]].

*$A_n$ elsewhere:* ← [[§23 S₃, Aₙ, Uₙ and GLₙ#The Alternating Groups Aₙ|Chapter 5]] · [[§47 S₃, Aₙ and GLₙ#The Alternating Groups Aₙ|Chapter 9]] → · [[The alternating group A₅|all appearances]]

## ℤ and nℤ

$\mathbb{Z}$ modulo $n\mathbb{Z}$ is the model for every quotient: $\mathbb{Z}/n\mathbb{Z}$ is the quotient of $\mathbb{Z}$ by the normal subgroup $n\mathbb{Z}$, so the notation of [[· 2 Arithmetic Modulo n|Chapter 2]] is an instance of the general one.

![[§37 Multiplying Cosets#^rem-37-1]]

![[§40 Quotient Groups#^ex-40-1]]

*$\mathbb{Z}$ elsewhere:* ← [[§19 S₃, ℤ∕nℤ and Uₙ#ℤ and nℤ|Chapter 4]] · no later appearance yet · [[The integers ℤ and the subgroups nℤ|all appearances]]

## ℤ/nℤ and Uₙ

$\mathbb{Z}/4\mathbb{Z}$ is the first quotient computed with representatives: $(\mathbb{Z}/4\mathbb{Z})/\{0, 2\}$ is cyclic of order $2$, but unlike $S_3/A_3$ no subgroup of representatives realizes it. The First Isomorphism Theorem explains Chapter 4's $\mathbb{Z}/6\mathbb{Z} \to U_7$, and the abelian simple groups are exactly the $\mathbb{Z}/p\mathbb{Z}$.

![[§40 Quotient Groups#^ex-40-2]]

![[§43 Simple Groups#^thm-43-1]]

The contrast with $S_3/A_3$ is [[§40 Quotient Groups#^rem-40-3|Life Is Especially Nice When S Is a Subgroup]] (in the $S_3$ part); $\mathbb{Z}/6\mathbb{Z} \to U_7$ is item (3) of [[§41 The First Isomorphism Theorem#^ex-41-1|The First Isomorphism Theorem in Action]] (in the $A_n$ part).

*$\mathbb{Z}/n\mathbb{Z}$ and $U_n$ elsewhere:* ← [[§32 Linear Groups, the Cube, S₃ and A₄#ℤ/nℤ and Uₙ|Chapter 6]] · no later appearance yet · [[ℤ∕nℤ and the unit groups Uₙ|all appearances]]

## GLₙ, SLₙ and O(n)

$SL_n$ is normal in $GL_n$ as the kernel of $\det$, with $GL_n(k)/SL_n(k) \cong k^\times$, while the diagonal and upper triangular subgroups of $GL_2(\mathbb{R})$ are not normal. Dividing $SL_n(F)$ by its scalar matrices gives $PSL_n(F)$, which is simple except for $PSL_2(\mathbb{F}_2) \cong S_3$ and $PSL_2(\mathbb{F}_3) \cong A_4$.

![[§39 Sources of Normal Subgroups#^prop-39-8]]

![[§43 Simple Groups#^def-43-2]]

![[§43 Simple Groups#^thm-43-13]]

$\det$ is item (2) of [[§39 Sources of Normal Subgroups#^ex-39-2|Kernels]] and of [[§41 The First Isomorphism Theorem#^ex-41-1|The First Isomorphism Theorem in Action]] (both in the $A_n$ part); the exceptions are [[§43 Simple Groups#^ex-43-3|The Two Exceptions]] (in the $S_4$ part).

*$GL_n$ elsewhere:* ← [[§36 S₃, S₄ and GLₙ#GLₙ, SLₙ and O(n)|Chapter 7]] · [[§47 S₃, Aₙ and GLₙ#GLₙ, SLₙ and O(n)|Chapter 9]] → · [[Matrix groups GLₙ, SLₙ and O(n)|all appearances]]
