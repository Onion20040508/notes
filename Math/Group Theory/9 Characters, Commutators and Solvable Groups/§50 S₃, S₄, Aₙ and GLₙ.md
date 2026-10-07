---
type: section
subject: "[[Group Theory]]"
chapter: 9
section: 50
tags: [group-theory, math493]
---
← [[§49 The Derived Series]] · ↑ [[· 9 Characters, Commutators and Solvable Groups]] · [[§51 p-Groups and Sylow Subgroups]] →

*The recurring groups as Chapter 9 saw them: characters take values in abelian groups, so they cannot separate conjugates and they kill commutators; and the solvable groups are those built from abelian pieces. Each part gathers the chapter's items about one group, in order.*

## The Symmetric Group S₃

$S_3$ shows why a character needs an abelian target: the identity map $S_3 \to S_3$ separates the conjugate transpositions $(1\,2)$ and $(1\,3)$.

![[§46 Characters#^rem-46-3]]

$S_3$ is solvable without being abelian: the chain $\{e\} \trianglelefteq A_3 \trianglelefteq S_3$ has the abelian quotients $\mathbb{Z}/3\mathbb{Z}$ and $\{\pm 1\}$, and the derived series $S_3 \trianglerighteq A_3 \trianglerighteq \{e\}$ reaches $\{e\}$ in two steps.

![[§48 Solvable Groups#^prop-48-1]]

![[§49 The Derived Series#^ex-49-1]]

*$S_3$ elsewhere:* ← [[§45 S₃, S₄, A₄ and A₅#The Symmetric Group S₃|Chapter 8]] · no later appearance yet · [[The symmetric group S₃|all appearances]]

## S₄, A₄ and the Klein Four-Group K

$S_4$ is solvable through $\{e\} \trianglelefteq K \trianglelefteq A_4 \trianglelefteq S_4$, with quotients $K$, $\mathbb{Z}/3\mathbb{Z}$ and $\{\pm 1\}$, and this chain is its derived series: $D(S_4) = A_4$, $D(A_4) = K$, $D(K) = \{e\}$. Here $K$ is normal in all of $S_4$, more than the definition asks ([[§48 Solvable Groups#^rem-48-1|Remark: Normal in the Next Term Only]]).

[[§48 Solvable Groups#^prop-48-1|Proposition §48.1]] (WS 9.1) gives the chain; [[§49 The Derived Series#^ex-49-1|Example §49.1]](2) computes the derived series, finding $(1\,2)(3\,4)$ as a commutator of two $3$-cycles of $A_4$ (both in the $S_3$ part).

$A_4$ also appears in the $A_n$ part below, as the case $n = 4$ of the commutator computations.

*$S_4$, $A_4$ and $K$ elsewhere:* ← [[§45 S₃, S₄, A₄ and A₅#S₄, A₄ and the Klein Four-Group K|Chapter 8]] · no later appearance yet · [[S₄, A₄ and the Klein four-group|all appearances]]

## The Alternating Groups Aₙ

$A_n$ is the commutator subgroup of $S_n$: every $3$-cycle is a commutator ([[§47 Commutators#^prop-47-2|PS 2.4(3)]]) and no transposition is ([[§47 Commutators#^prop-47-3|PS 2.4(4)]]). Hence every character of $S_n$ is trivial on $A_n$, and the abelianization of $S_n$ is $S_n/A_n \cong \{\pm 1\}$. For $n \geq 5$, $A_n$ is also its own commutator subgroup, so its characters are trivial; $A_3$ and $A_4$ show that the bound is sharp.

![[§47 Commutators#^thm-47-5]]

![[§47 Commutators#^ex-47-1]]

![[§47 Commutators#^lem-47-9]]

![[§47 Commutators#^thm-47-10]]

![[§47 Commutators#^rem-47-5]]

For $n \geq 5$, $A_n$ is not solvable, and hence neither is $S_n$: a simple non-abelian group has no chain with abelian quotients, and the derived series of $S_n$ stalls at $A_n = D(A_n)$. So $S_n$ is solvable exactly for $n \leq 4$.

![[§49 The Derived Series#^cor-49-2]]

[[§49 The Derived Series#^ex-49-1|Example §49.1]](3) (in the $S_3$ part) shows the derived series stalling; the corollary proves non-solvability from the [[§43 Simple Groups#^thm-43-9|simplicity]] of $A_n$ and [[§48 Solvable Groups#^prop-48-2|Proposition §48.2]].

*$A_n$ elsewhere:* ← [[§45 S₃, S₄, A₄ and A₅#The Alternating Groups Aₙ|Chapter 8]] · no later appearance yet · [[The alternating group A₅|all appearances]]

## GLₙ, SLₙ and O(n)

The determinant is the model character of $GL_n(k)$, and a character is the same thing as a $1$-dimensional representation, a homomorphism into $GL_1(k) = k^\times$.

![[§46 Characters#^ex-46-1]]

![[§46 Characters#^rem-46-4]]

![[§47 Commutators#^ex-47-2]]

*$GL_n$ elsewhere:* ← [[§45 S₃, S₄, A₄ and A₅#GLₙ, SLₙ and O(n)|Chapter 8]] · [[§51 p-Groups and Sylow Subgroups#^prop-51-2|Chapter 10]] → (where $GL_n(\mathbb{F}_p)$ appears once) · [[Matrix groups GLₙ, SLₙ and O(n)|all appearances]]
