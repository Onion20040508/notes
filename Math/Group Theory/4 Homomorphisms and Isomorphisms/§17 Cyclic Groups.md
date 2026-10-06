---
type: section
subject: "[[Group Theory]]"
chapter: 4
section: 17
tags: [group-theory, math493]
---
← [[§16 Isomorphisms]] · ↑ [[· 4 Homomorphisms and Isomorphisms]] · [[§18 Conjugation, Products, and Pointwise Products]] →

*Reference: Pinter Ch. 11.*

> [!theorem] Theorem §17.1: Classification of Cyclic Groups
> Let $G = \langle g \rangle$ be a cyclic group.
> 1. If $g$ has finite order $n$, then $G = \{e, g, \ldots, g^{n-1}\}$ has exactly $n$ elements, and $\mathbb{Z}/n\mathbb{Z} \to G$, $k \mapsto g^k$, is an isomorphism. So every cyclic group of order $n$ is isomorphic to $\mathbb{Z}/n\mathbb{Z}$.
> 2. If $g$ has infinite order, then the powers $g^k$ ($k \in \mathbb{Z}$) are pairwise distinct, and $\mathbb{Z} \to G$, $k \mapsto g^k$, is an isomorphism. So every infinite cyclic group is isomorphic to $\mathbb{Z}$.
>
> Consequently two cyclic groups are isomorphic if and only if they have the same order.
>
> *Source: cf. MATH 412*

^thm-17-1

> [!proof]+ Proof
> Define $\varphi(k) = g^k$ on $\mathbb{Z}$; it is a homomorphism $(\mathbb{Z}, +) \to G$ by the [[§4 Subgroups#^lem-4-4|Exponent Laws]] ($g^{k+l} = g^k g^l$), and surjective since $G = \langle g \rangle$.
>
> **(1)** *Kernel:* $g^k = e$ iff $n \mid k$: if $k = qn + r$ with $0 \leq r < n$, then $g^k = (g^n)^q g^r = g^r$, which is $e$ iff $r = 0$ by minimality of $n$. So $\operatorname{Ker}\varphi = n\mathbb{Z}$. *Descent to $\mathbb{Z}/n\mathbb{Z}$:* since $\operatorname{Ker}\varphi = n\mathbb{Z}$, the [[§7 The Group ℤ∕nℤ#^lem-7-2|Descent Lemma]] (§7.2) gives a well-defined homomorphism $\bar\varphi([k]) = g^k$ on $\mathbb{Z}/n\mathbb{Z}$ — explicitly, $k' = k + nm$ implies $g^{k'} = g^k (g^n)^m = g^k$ — still surjective. *Injective:* $\bar\varphi([k]) = e$ iff $n \mid k$ iff $[k] = [0]$, so $\operatorname{Ker}\bar\varphi = \{[0]\}$; by the [[§15 Homomorphisms#^prop-15-3|injectivity criterion]], $\bar\varphi$ is injective. Hence $\bar\varphi$ is an isomorphism, and $|G| = n$ with $G = \{g^0, \ldots, g^{n-1}\}$.
>
> **(2)** If $g^k = g^l$ with $k < l$, then $g^{l-k} = e$ with $l - k \geq 1$, contradicting infinite order; so $\varphi$ is injective, and being surjective, an isomorphism $\mathbb{Z} \to G$.
>
> **Consequence:** $\cong$ is transitive, and $|G|$ is an isomorphism invariant.

^pf-17-1

*Uses:* [[§4 Subgroups#^lem-4-4|§4.4]], [[§4 Subgroups#^def-4-6|Def. §4.6]], [[§6 Divisibility and Congruence#^lem-6-1|§6.1]], [[§7 The Group ℤ∕nℤ#^lem-7-2|§7.2]], [[§15 Homomorphisms#^prop-15-3|§15.3]], [[§16 Isomorphisms#^prop-16-2|§16.2]], [[§16 Isomorphisms#^prop-16-5|§16.5]]

> [!remark]- Connections
> - Worksheet form: [[§17 Cyclic Groups#^prop-17-3|The Homomorphism k ↦ gᵏ (WS 3.1)]] (§17.3).
> - MATH 590 statement (without proof): [[§27 Free Groups and Presentations#^rem-27-9|Remark after Definition §21.7]] (590 §26), with [[§27 Free Groups and Presentations#^def-27-2|Cyclic Groups and Generators]] (590 §21.7).

> [!theorem] Corollary §17.2: Cyclic iff There Is an Element of Order $|G|$
> A group $G$ of finite order $n$ is cyclic if and only if it contains an element of order $n$; the elements of order $n$ are then exactly the generators.

^cor-17-2

> [!proof]+ Proof
> For any $g$, $\operatorname{ord}(g) = |\langle g \rangle|$ by the [[§17 Cyclic Groups#^thm-17-1|Classification of Cyclic Groups]]. If $\operatorname{ord}(g) = n$, then $\langle g \rangle$ is a subset of $G$ with $n = |G|$ elements, hence equals $G$. Conversely, if $G = \langle g \rangle$, then $\operatorname{ord}(g) = |\langle g \rangle| = |G| = n$.

^pf-17-2

*Uses:* [[§17 Cyclic Groups#^thm-17-1|§17.1]], [[§4 Subgroups#^def-4-6|Def. §4.6]]

> [!remark] Remark: WS 2.5 and WS 2.7(2) as Instances
> $U_5 = \langle 2 \rangle$ with $2$ of order $4$, and $U_7 = \langle 3 \rangle$ with $3$ of order $6$; [[§17 Cyclic Groups#^thm-17-1|the theorem]] gives $U_5 \cong \mathbb{Z}/4\mathbb{Z}$ and $U_7 \cong \mathbb{Z}/6\mathbb{Z}$ with the same maps $k \mapsto 2^k$, $k \mapsto 3^k$ constructed there ([[§16 Isomorphisms#^prop-16-7|WS 2.5]], [[§16 Isomorphisms#^prop-16-8|WS 2.7(2)]]). In each case the well-definedness step (“$2^4 \equiv 1$”) is exactly the computation of the kernel $n\mathbb{Z}$. The theorem also explains why $U_8$ is not cyclic: a cyclic group of order $4$ would be $\cong \mathbb{Z}/4\mathbb{Z}$, which has an element of order $4$, and $U_8$ has none.

^rem-17-1

> [!theorem] Proposition §17.3: The Homomorphism $k \mapsto g^k$ and $\langle g \rangle \cong \mathbb{Z}/N\mathbb{Z}$
> Let $G$ be a group and $g \in G$.
> 1. The map $\varphi_g: \mathbb{Z} \to G$, $k \mapsto g^k$, is a group homomorphism from $(\mathbb{Z}, +)$ to $G$.
> 2. If $g$ has order $N$, then $\operatorname{Ker}(\varphi_g) = N\mathbb{Z}$.
> 3. If $g$ has order $N$, then $\langle g \rangle \cong \mathbb{Z}/N\mathbb{Z}$, via $[k] \mapsto g^k$.
> 4. If $g$ does not have finite order, then $\operatorname{Ker}(\varphi_g) = \{0\}$ and $\langle g \rangle \cong \mathbb{Z}$, via $k \mapsto g^k$.
>
> *Source: WS 3.1*

^prop-17-3

> [!proof]+ Proof
> **(1)** $\varphi_g(k + l) = g^{k+l} = g^k g^l = \varphi_g(k)\varphi_g(l)$ by the [[§4 Subgroups#^lem-4-4|Exponent Laws]] (§4.4). Its image is $\{g^k : k \in \mathbb{Z}\} = \langle g \rangle$.
>
> **(2)** $g^k = e$ iff $N \mid k$: write $k = qN + r$ with $0 \leq r < N$; then $g^k = (g^N)^q g^r = g^r$, which equals $e$ iff $r = 0$, by minimality of $N$. So $\operatorname{Ker}\varphi_g = N\mathbb{Z}$.
>
> **(3)** *Well-defined:* if $[k] = [k']$ in $\mathbb{Z}/N\mathbb{Z}$, then $k' = k + Nm$ for some $m \in \mathbb{Z}$, so
>
> $$
> g^{k'} = g^{k + Nm} = g^k (g^N)^m = g^k \cdot e^m = g^k,
> $$
>
> using the Exponent Laws and $g^N = e$. Hence $\bar\varphi_g([k]) := g^k$ depends only on the class $[k]$, and is the unique such map ([[§7 The Group ℤ∕nℤ#^lem-7-2|Descending a Map to ℤ∕nℤ]], §7.2, applied to $\varphi_g$, whose kernel contains $N\mathbb{Z}$ by (2)). It is a homomorphism by (1), surjective onto $\langle g \rangle$, and injective since $\bar\varphi_g([k]) = e$ iff $N \mid k$ iff $[k] = [0]$ ([[§15 Homomorphisms#^prop-15-3|injectivity criterion]], §15.3). Hence $\bar\varphi_g: \mathbb{Z}/N\mathbb{Z} \to \langle g \rangle$ is an isomorphism, and $|\langle g \rangle| = N$.
>
> **(4)** If $g^k = e$ with $k \neq 0$, then $g^{|k|} = e$ (using $g^{-k} = (g^k)^{-1}$), so $g$ would have finite order. Hence $\operatorname{Ker}\varphi_g = \{0\}$, $\varphi_g$ is injective, and $\varphi_g: \mathbb{Z} \to \langle g \rangle$ is an isomorphism. The statements modify as: the kernel is $0\mathbb{Z} = \{0\}$, and $\langle g \rangle \cong \mathbb{Z}/0\mathbb{Z} = \mathbb{Z}$ — consistently with the finite case if one regards “infinite order” as “order $0$.”

^pf-17-3

*Uses:* [[§4 Subgroups#^lem-4-4|§4.4]], [[§4 Subgroups#^def-4-3|Def. §4.3]], [[§4 Subgroups#^def-4-6|Def. §4.6]], [[§6 Divisibility and Congruence#^lem-6-1|§6.1]], [[§7 The Group ℤ∕nℤ#^lem-7-2|§7.2]], [[§15 Homomorphisms#^prop-15-3|§15.3]]

![[m493-17-2.svg]]
*The homomorphism $\varphi_g: \mathbb{Z} \to \langle g \rangle$, $k \mapsto g^k$, for $g$ of order $N = 6$ (nonnegative $k$ shown). The integers (blue spiral) wind around $\langle g \rangle$ once every $6$ steps, and all integers on one ray have the same image. The ray to $e$ (red) carries the kernel $6\mathbb{Z}$; identifying the points on each ray is passing to $\mathbb{Z}/6\mathbb{Z} \cong \langle g \rangle$.*

> [!remark]- Connections
> - Lecture form: [[§17 Cyclic Groups#^thm-17-1|Classification of Cyclic Groups]] (§17.1).

> [!remark] Remark: Relation to the Classification of Cyclic Groups
> This is the [[§17 Cyclic Groups#^thm-17-1|Classification of Cyclic Groups]] (§17.1), now stated on the worksheet: every cyclic group is $\mathbb{Z}/N\mathbb{Z}$ or $\mathbb{Z}$, and $\operatorname{ord}(g) = |\langle g \rangle|$. The kernel computation in (2) is the general form of the “well-definedness” step in [[§16 Isomorphisms#^prop-16-7|WS 2.5]] and [[§16 Isomorphisms#^prop-16-8|2.7(2)]].

^rem-17-2

> [!theorem] Theorem §17.4: Subgroups of Cyclic Groups Are Cyclic
> Let $G = \langle g \rangle$ be cyclic and $H \leq G$. Then $H$ is cyclic. More precisely, if $H \neq \{e\}$, let $m$ be the least positive integer with $g^m \in H$; then $H = \langle g^m \rangle$, and every integer $t$ with $g^t \in H$ is a multiple of $m$.
>
> *Source: cf. Pinter Ch. 11, Thm. 2; MATH 412*

^thm-17-4

> [!proof]+ Proof
> If $H = \{e\}$, then $H = \langle e \rangle$. Otherwise $H$ contains some $g^t$ with $t \neq 0$, and also its inverse $g^{-t}$, so it contains a positive power of $g$; by [[§1 The Set ℕ of Natural Numbers#^thm-1-2|well-ordering]] the least such exponent $m$ exists. Since $g^m \in H$, $\langle g^m \rangle \subseteq H$. Conversely let $g^t \in H$ and write $t = qm + r$ with $0 \leq r < m$. Then $g^r = g^t (g^m)^{-q} \in H$, so minimality of $m$ forces $r = 0$: $t = qm$ and $g^t = (g^m)^q \in \langle g^m \rangle$. So $H = \langle g^m \rangle$, and the argument shows every such $t$ is a multiple of $m$. (For $G = \mathbb{Z}$ this is the [[§5 A Zoo of Subgroups#^prop-5-1|classification of subgroups of ℤ]], §5.1, by the same division-algorithm argument.)

^pf-17-4

*Uses:* [[§4 Subgroups#^prop-4-6|§4.6]], [[§4 Subgroups#^lem-4-4|§4.4]], [[§6 Divisibility and Congruence#^lem-6-1|§6.1]], [[§1 The Set ℕ of Natural Numbers#^thm-1-2|451 §1.2]]

> [!remark]- Connections
> - MATH 590 version: [[§26 Algebra Prerequisites꞉ Groups#^prop-26-1|Properties Inherited by Subgroups]] (590 §21.1, part 2).
> - The well-ordering step: [[§5 The Induction Principle#^cor-5-7|250 Cor. §5.7]] (proved there from induction).

> [!theorem] Proposition §17.5: The Order of a Power
> Let $g$ have finite order $n$ and let $k \in \mathbb{Z}$. Then
>
> $$
> \operatorname{ord}(g^k) = \frac{n}{\gcd(n, k)}.
> $$
>
> *Source: cf. Pinter Ch. 10, Ex. F*

^prop-17-5

> [!proof]+ Proof
> Let $d = \gcd(n, k)$ and write $n = dn'$, $k = dk'$ with $\gcd(n', k') = 1$. For $m \in \mathbb{Z}$: $(g^k)^m = g^{km} = e$ iff $n \mid km$ ([[§17 Cyclic Groups#^prop-17-3|§17.3]], since the exponents killing $g$ are exactly the multiples of $n$) iff $n' \mid k'm$ iff $n' \mid m$, the last step by [[§9 Euclid's Lemma, Unique Factorization, and the Chinese Remainder Theorem#^lem-9-1|Euclid's Lemma]] in its general form (§9.1), as $\gcd(n', k') = 1$. So the least positive $m$ with $(g^k)^m = e$ is $n' = n/d$.

^pf-17-5

*Uses:* [[§8 Invertibility and Unit Groups#^def-8-1|Def. §8.1]], [[§4 Subgroups#^lem-4-4|§4.4]], [[§17 Cyclic Groups#^prop-17-3|§17.3]], [[§9 Euclid's Lemma, Unique Factorization, and the Chinese Remainder Theorem#^lem-9-1|§9.1]]

![[m493-17-3.svg]]
*The order of a power in a cyclic group of order $12$ (dot $j$ stands for $g^j$). Stepping around by $k$ returns to $e = g^0$ after $12/\gcd(12, k)$ steps: $g^5$ (blue) visits all twelve elements, so it is a generator ([[§17 Cyclic Groups#^cor-17-6|§17.6]]); $g^8$ and $g^9$ (red) close up after $3$ and $4$ steps, tracing the subgroups $\langle g^4 \rangle$ and $\langle g^3 \rangle$ of orders $3$ and $4$.*

> [!theorem] Corollary §17.6: Generators and Subgroups of a Finite Cyclic Group
> Let $G = \langle g \rangle$ be cyclic of order $n$.
> 1. $g^k$ generates $G$ if and only if $\gcd(k, n) = 1$. In particular $G$ has exactly $\varphi(n)$ generators.
> 2. For each positive divisor $d$ of $n$, $G$ has exactly one subgroup of order $d$, namely $\langle g^{n/d} \rangle$; and $G$ has no subgroups of other orders.
>
> *Source: cf. Pinter Ch. 11, Exs. C–D*

^cor-17-6

> [!proof]+ Proof
> **(1)** $g^k$ generates $G$ iff $\operatorname{ord}(g^k) = n$ (Cyclic iff There Is an Element of Order $|G|$, [[§17 Cyclic Groups#^cor-17-2|§17.2]]), iff $n/\gcd(n,k) = n$, iff $\gcd(k, n) = 1$. The elements of $G$ are $g^0, \ldots, g^{n-1}$, so the generators correspond to the $k \in \{0, \ldots, n-1\}$ coprime to $n$, of which there are $\varphi(n)$.
>
> **(2)** *Existence:* $\operatorname{ord}(g^{n/d}) = n/\gcd(n, n/d) = n/(n/d) = d$, so $\langle g^{n/d} \rangle$ has order $d$. *Uniqueness:* let $H \leq G$ have order $d$. By [[§17 Cyclic Groups#^thm-17-4|Subgroups of Cyclic Groups Are Cyclic]] (above), $H = \langle g^m \rangle$ with $m$ the least positive exponent in $H$, and since $g^n = e \in H$, $m \mid n$. Then $|H| = \operatorname{ord}(g^m) = n/\gcd(n, m) = n/m$, so $|H| = d$ forces $m = n/d$ and $H = \langle g^{n/d} \rangle$. The last clause is [[§29 The Index and Lagrange's Theorem#^thm-29-2|Lagrange]] (§29.2).

^pf-17-6

*Uses:* [[§17 Cyclic Groups#^cor-17-2|§17.2]], [[§17 Cyclic Groups#^prop-17-5|§17.5]], [[§17 Cyclic Groups#^thm-17-1|§17.1]], [[§8 Invertibility and Unit Groups#^def-8-3|Def. §8.3]], [[§17 Cyclic Groups#^thm-17-4|§17.4]], [[§29 The Index and Lagrange's Theorem#^thm-29-2|§29.2]]

> [!example] Example §17.1: The Subgroups of $\mathbb{Z}/12\mathbb{Z}$
> The divisors of $12$ are $1, 2, 3, 4, 6, 12$, so $\mathbb{Z}/12\mathbb{Z}$ has exactly six subgroups: $\{[0]\}$, $\langle [6] \rangle$, $\langle [4] \rangle$, $\langle [3] \rangle$, $\langle [2] \rangle$, and the whole group $\langle [1] \rangle$. Its generators are $[1], [5], [7], [11]$, the $\varphi(12) = 4$ classes coprime to $12$.

^ex-17-1

![[m493-17-1.svg]]
*The subgroup lattice of $\mathbb{Z}/12\mathbb{Z}$: one subgroup for each divisor of $12$ (its order is shown at the right). All are normal, the group being abelian.*
