---
type: problem-set
subject: "[[Group Theory]]"
problem_set: 8
tags: [group-theory, math493]
---
← [[493 Problem Set 7]] · ↑ [[Group Theory]] · [[493 Problem Set 9]] →

# Problem Set 8

*Due Thursday, November 5; submitted. Each problem is treated in the main text, at the location indicated.*

> [!question] Problem 8.1: The Product Formula
> Let $G$ be a finite group and let $A$ and $B$ be subgroups of $G$. Recall that $AB = \{ab : a \in A,\ b \in B\}$.
>
> 1. Show that each element $c \in AB$ can be written in exactly $|A \cap B|$ many different ways as $ab$, for $a \in A$ and $b \in B$. Hint: If $a_1b_1 = a_2b_2$, what can you deduce?
> 2. Deduce that $|AB| = \dfrac{|A|\cdot|B|}{|A \cap B|}$, even when neither $A$ nor $B$ is normal.

^hw-8-1

*Treated in [[§30 Orbit–Stabilizer|§30]] (Proposition [[§30 Orbit–Stabilizer#^prop-30-6|§30.6]]).*

> [!question] Problem 8.2: Subgroups of Index $2$
> Let $G$ be a group and let $H$ be a subgroup with $[G : H] = 2$. Show that $H$ is normal.

^hw-8-2

*Treated in [[§39 Sources of Normal Subgroups|§39]] (Proposition [[§39 Sources of Normal Subgroups#^prop-39-1|§39.1]], second proof).*

> [!question] Problem 8.3: Groups of Order $pq$
> Let $p < q$ be prime numbers. In this problem, we will discuss the classification of groups of order $pq$.
>
> Let $G$ be a group of order $pq$, let $P$ be a $p$-Sylow subgroup and let $Q$ be a $q$-Sylow subgroup. We know from Problem 2.5 that $P \cong \mathbb{Z}/p\mathbb{Z}$ and $Q \cong \mathbb{Z}/q\mathbb{Z}$.
>
> 1. If $q \not\equiv 1 \bmod p$, show that $P$ and $Q$ are normal, and deduce that $G \cong Q \times P$.
> 2. If $q \equiv 1 \bmod p$, show that $Q$ is still normal (though maybe $P$ isn't) and deduce that $G \cong Q \rtimes_\phi P$ for some map from $P$ to $\operatorname{Aut}(Q)$. (The problem set prints $Q \cong Q \rtimes_\phi P$ here; $G$ is meant.)
> 3. Show that every automorphism of $Q$ is of the form $x \mapsto ax$ for some $a \in (\mathbb{Z}/q\mathbb{Z})^\times$. Show that giving a homomorphism from $P$ to $\operatorname{Aut}(Q)$ is the same as finding a solution to $a^p \equiv 1 \bmod q$.
>
> I won't have you do the rest of this, because it is really number theory, not group theory but, whenever $q \equiv 1 \bmod p$, there are exactly $p$ solutions to $a^p \equiv 1 \bmod q$. The trivial solution $a = 1$ corresponds to $G \cong \mathbb{Z}/p\mathbb{Z} \times \mathbb{Z}/q\mathbb{Z}$. The $p - 1$ nontrivial roots give a non-abelian group of order $pq$; all of these non-abelian groups of order $pq$ are isomorphic to each other.

^hw-8-3

*Treated in [[§55 The Sylow Theorems|§55]] (Proposition [[§55 The Sylow Theorems#^prop-55-11|§55.11]], second proof) and [[§60 Groups of Order pq as Semidirect Products|§60]] (Proposition [[§60 Groups of Order pq as Semidirect Products#^prop-60-1|§60.1]], Lemma [[§60 Groups of Order pq as Semidirect Products#^lem-60-2|§60.2]], Proposition [[§60 Groups of Order pq as Semidirect Products#^prop-60-3|§60.3]], Theorem [[§60 Groups of Order pq as Semidirect Products#^thm-60-4|§60.4]]).*

> [!question] Problem 8.4: Simple Groups of Order $60$, Again
> We try to repair Problem 7.1 on the last problem set. I don't think that it was false as stated, but it was certainly too hard and the hints weren't well-phrased. Let $G$ be a simple group of order $60$.
>
> 1. Show that $G$ has six $5$-Sylow subgroups.
>
> Let $X_5$ be the set of $5$-Sylow subgroups, and let $G$ act on $X_5$ by $g \ast P = gPg^{-1}$. This gives a map $G \to S_6$.
>
> 2. Show that $G \to S_6$ is injective, and show that the image of $G$ lands in $A_6$.
>
> Thus, we can (and will) think of $G$ as a subgroup of $A_6$. Let $Y = A_6/G$.
>
> 3. Show that $|Y| = 6$, so we get a map $G \to S_6$ (again!).
> 4. Show that the image of $G$ actually lands in a copy of $S_5$.
> 5. Show that $G \cong A_5$.
>
> The strange thing is that our first embedding of $G$ into $A_6$, by the action on $X_5$, doesn't land in the obvious copy of $A_5$ – none of the $5$-Sylows is fixed. It is only the second map $G \to S_6$, using the action on $Y$, which makes this work.

^hw-8-4

*Treated in [[§56 Simple Groups of Small Order|§56]] (Theorem [[§56 Simple Groups of Small Order#^thm-56-20|§56.20]], second proof, and the remark *Two Maps from $G$ to $S_6$*).*

> [!question] Problem 8.5: The Trace
> Let's review some linear algebra! Let $M$ be a square $n \times n$ matrix. We define the **trace** of $M$ to be $\sum_{i=1}^n M_{ii}$, and we write this $\operatorname{Tr}(M)$.
>
> 1. Let $A$ be an $m \times n$ matrix and let $B$ be a $n \times m$ matrix. Show that $\operatorname{Tr}(AB) = \operatorname{Tr}(BA)$.
> 2. Let $M$ be an $n \times n$ matrix and let $S$ be an invertible $n \times n$ matrix. Show that $\operatorname{Tr}(M) = \operatorname{Tr}(SMS^{-1})$.
> 3. Suppose that $M$ is diagonalizable, with eigenvalues $\lambda_1, \lambda_2, \dots, \lambda_n$. Give a formula for $\operatorname{Tr}(M)$ in terms of the $\lambda$'s.

^hw-8-5

*Treated in [[§66 Invariant Vectors|§66]] (Definition [[§66 Invariant Vectors#^def-66-1|§66.1]], Proposition [[§66 Invariant Vectors#^prop-66-1|§66.1]], Corollary [[§66 Invariant Vectors#^cor-66-2|§66.2]], Proposition [[§66 Invariant Vectors#^prop-66-3|§66.3]]).*
