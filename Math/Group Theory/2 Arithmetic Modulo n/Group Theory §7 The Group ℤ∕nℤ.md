---
type: section
subject: "[[Group Theory]]"
chapter: 2
section: 7
tags: [group-theory, math493]
---
← [[Group Theory §6 Divisibility and Congruence]] · ↑ [[Group Theory — 2 Arithmetic Modulo n]] · [[Group Theory §8 Invertibility and Unit Groups]] →

*Reference: Pinter Ch. 3 (the groups $\mathbb{Z}_n$), Ch. 23.*

> [!definition] Definition §7.1: The Cyclic Group $\mathbb{Z}/n\mathbb{Z} = C_n$
> Fix an integer $n \geq 1$, and let $[a] = a + n\mathbb{Z}$ denote residue classes modulo $n$ as [[Group Theory §6 Divisibility and Congruence#^def-6-4|above]]. Define
>
> $$ \mathbb{Z}/n\mathbb{Z} = \{[a] : a \in \mathbb{Z}\}, \qquad [a] + [b] := [a + b]. $$
>
> Then $\mathbb{Z}/n\mathbb{Z}$ is an abelian group with identity $[0]$ and inverse $-[a] = [-a]$, called the **cyclic group of order $n$** and also written $C_n$. By the [[Group Theory §6 Divisibility and Congruence#^lem-6-1|division algorithm]] every class equals exactly one of $[0], [1], \ldots, [n-1]$, so $|\mathbb{Z}/n\mathbb{Z}| = n$.

^def-7-1

> [!remark]- Connections
> - 590 counterpart: [[Topology §21 Algebra Prerequisites꞉ Groups#^ex-21-1|590 Ex. §21.1]], and $\mathbb{Z}/n\mathbb{Z}$ as a quotient in [[Topology §21 Algebra Prerequisites꞉ Groups#^ex-21-7|590 Ex. §21.7]].
> - The general construction: [[Group Theory §37 Quotient Groups#^def-37-1|Quotient Group]]; every cyclic group is one of these: [[Group Theory §17 Cyclic Groups#^thm-17-1|Classification of Cyclic Groups]].

> [!definition] Definition §7.2: Well-Defined
> Let $\sim$ be an equivalence relation on a set $X$. A rule assigning to each equivalence class $[x]$ a value $f([x])$ computed from a chosen representative $x$ is **well defined** if the value does not depend on the choice: $x \sim x'$ implies that the rule gives the same value for $x$ and $x'$. Only then does the rule define a function on the set of classes. The same applies to rules taking several classes as input, such as $[a] + [b] := [a + b]$.

^def-7-2

> [!remark]- Connections
> - The same issue for cosets of an arbitrary subgroup: [[Group Theory §34 Multiplying Cosets#^prop-34-1|When Coset Multiplication Is Well Defined]]; 590 version: [[Topology §21 Algebra Prerequisites꞉ Groups#^rem-21-19|Why Normality is Required]].

> [!theorem] Proposition §7.1: Addition of Residue Classes Is Well-Defined; $\mathbb{Z}/n\mathbb{Z}$ Is a Group
> Fix $n \geq 1$. The rule
>
> $$ [a] + [b] := [a + b] $$
>
> does not depend on the chosen representatives: if $[a] = [a']$ and $[b] = [b']$, then $[a + b] = [a' + b']$. With this operation $\mathbb{Z}/n\mathbb{Z}$ is an abelian group of order $n$, with identity $[0]$ and $-[a] = [-a]$.

^prop-7-1

> [!proof]+ Proof
> The one point requiring proof is that the operation is *well defined*: the formula $[a] + [b] = [a+b]$ uses the *representatives* $a, b$, so we must check the result does not depend on which representatives we choose. Suppose $[a] = [a']$ and $[b] = [b']$, i.e. $a' = a + kn$ and $b' = b + ln$ for some $k, l \in \mathbb{Z}$. Then
>
> $$ a' + b' = (a + b) + (k + l)n \equiv a + b \pmod{n}, $$
>
> so $[a' + b'] = [a + b]$. Given well-definedness, associativity and commutativity are inherited from $\mathbb{Z}$ (e.g. $([a]+[b])+[c] = [(a+b)+c] = [a+(b+c)] = [a]+([b]+[c])$), $[0] + [a] = [a]$, and $[a] + [-a] = [0]$.

^pf-7-1

*Uses:* [[Group Theory §7 The Group ℤ∕nℤ#^def-7-2|Def. §7.2]], [[Group Theory §6 Divisibility and Congruence#^def-6-3|Def. §6.3]], [[Group Theory §6 Divisibility and Congruence#^def-6-4|Def. §6.4]], [[Group Theory §3 Basic Examples of Groups#^def-3-1|Def. §3.1]], [[Group Theory §1 The Definition of a Group#^def-1-1|Def. §1.1]], [[Group Theory §1 The Definition of a Group#^def-1-2|Def. §1.2]]

> [!theorem] Lemma §7.2: Descending a Map to $\mathbb{Z}/n\mathbb{Z}$
> Fix $n \geq 1$, let $X$ be any set, and let $f: \mathbb{Z} \to X$ be a function.
> 1. There is a function $\bar f: \mathbb{Z}/n\mathbb{Z} \to X$ with $\bar f([k]) = f(k)$ for all $k \in \mathbb{Z}$ if and only if $f(k) = f(k + n)$ for all $k \in \mathbb{Z}$; and then $\bar f$ is unique.
> 2. If $X = G$ is a group and $f = \varphi$ is a homomorphism $(\mathbb{Z}, +) \to G$, the condition holds if and only if $n\mathbb{Z} \subseteq \operatorname{Ker}(\varphi)$, i.e. $\varphi(n) = 1$; and then $\bar\varphi$ is a homomorphism.

^lem-7-2

> [!proof]+ Proof
> **(1)** ($\Rightarrow$) If such $\bar f$ exists, then since $[k] = [k+n]$ we get $f(k) = \bar f([k]) = \bar f([k+n]) = f(k+n)$. ($\Leftarrow$) Suppose $f(k) = f(k+n)$ for all $k$; by induction, $f(k) = f(k + mn)$ for all $m \in \mathbb{Z}$ (for $m < 0$ apply the hypothesis at $k + mn$). Now define $\bar f([k]) := f(k)$. This is unambiguous: if $[k] = [k']$, then $k' = k + mn$ for some $m$, so $f(k') = f(k)$. Uniqueness is forced, since every class is $[k]$ for some $k$.
>
> **(2)** $\varphi(k + n) = \varphi(k)\varphi(n)$, so $\varphi(k+n) = \varphi(k)$ for all $k$ iff $\varphi(n) = 1$ iff $n \in \operatorname{Ker}\varphi$, and $\operatorname{Ker}\varphi$ is a subgroup, so this is equivalent to $n\mathbb{Z} \subseteq \operatorname{Ker}\varphi$. Given this, $\bar\varphi([k] + [l]) = \bar\varphi([k+l]) = \varphi(k+l) = \varphi(k)\varphi(l) = \bar\varphi([k])\bar\varphi([l])$.

^pf-7-2

*Uses:* [[Group Theory §6 Divisibility and Congruence#^def-6-4|Def. §6.4]], [[Group Theory §7 The Group ℤ∕nℤ#^def-7-2|Def. §7.2]], [[Group Theory §15 Homomorphisms#^def-15-1|Def. §15.1]], [[Group Theory §15 Homomorphisms#^def-15-2|Def. §15.2]], [[Group Theory §15 Homomorphisms#^prop-15-2|§15.2]], [[Group Theory §4 Subgroups#^prop-4-6|§4.6]], [[Single Variable Analysis §1 The Set ℕ of Natural Numbers#^thm-1-1|451 §1.1]]

![[m493-7-1.svg]]
*The Descent Lemma: $f$ factors as $f = \bar f \circ \pi$ through the projection $\pi(k) = [k]$ exactly when $f(k) = f(k+n)$ for all $k$. The dashed red arrow is the one whose existence (and uniqueness) the lemma asserts.*

> [!remark]- Connections
> - Topological analogue: [[Universal Property of Quotient Maps]] (590 §12.3), same factorization triangle.
> - Generalized to arbitrary normal subgroups by the [[Group Theory §38 The First Isomorphism Theorem#^thm-38-1|First Isomorphism Theorem]].

> [!remark] Remark: Where This Is Used
> Well-definedness of a map out of $\mathbb{Z}/n\mathbb{Z}$ is the recurring technical step in these notes: addition and multiplication of residue classes ([[Group Theory §7 The Group ℤ∕nℤ#^prop-7-1|above]], and for $U_n$ [[Group Theory §8 Invertibility and Unit Groups#^prop-8-3|below]]), the isomorphisms $\mathbb{Z}/4\mathbb{Z} \to U_5$, $k \mapsto 2^k$, and $\mathbb{Z}/6\mathbb{Z} \to U_7$, $k \mapsto 3^k$ ([[Group Theory §16 Isomorphisms#^prop-16-7|§16.7]], [[Group Theory §16 Isomorphisms#^prop-16-8|§16.8]]), the Classification of Cyclic Groups ([[Group Theory §17 Cyclic Groups#^thm-17-1|§17.1]]), and $\langle g \rangle \cong \mathbb{Z}/N\mathbb{Z}$ ([[Group Theory §17 Cyclic Groups#^prop-17-3|§17.3]]). In each case the verification is the same: check the formula is unchanged when the representative is shifted by $n$.

^rem-7-1
