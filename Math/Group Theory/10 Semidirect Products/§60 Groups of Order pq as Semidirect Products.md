---
type: section
subject: "[[Group Theory]]"
chapter: 10
section: 60
tags: [group-theory, math493]
---
← [[§59 Groups of Affine Maps]] · ↑ [[· 10 Semidirect Products]] · [[§61 Representations and Subrepresentations]] →

*Source: Problem Set 8, Problem 8.3 (submitted Thu Nov 5). The example at the end is not from class.*

In [[§55 The Sylow Theorems|§55]], a group of order $pq$ with $q \not\equiv 1 \pmod p$ was shown to be cyclic, because both Sylow subgroups are normal (Proposition [[§55 The Sylow Theorems#^prop-55-11|§55.11]]). Without that hypothesis only the Sylow $q$-subgroup has to be normal, and the group is a semidirect product. The possible actions are then listed by solving a congruence.

> [!theorem] Proposition §60.1: Groups of Order $pq$ Are Semidirect Products
> Let $p < q$ be primes, let $G$ be a group of order $pq$, let $P$ be a Sylow $p$-subgroup and $Q$ a Sylow $q$-subgroup of $G$. Then:
>
> 1. $Q$ is normal in $G$.
> 2. $Q \cap P = \{e\}$ and $QP = G$, so $G$ is the internal semidirect product of $Q$ and $P$ (Definition [[§58 Semidirect Products#^def-58-1|§58.1]]).
> 3. The map $\varphi \colon P \to \operatorname{Aut}(Q)$, $\varphi(x)(y) = xyx^{-1}$, is a homomorphism, and $(y, x) \mapsto yx$ is an isomorphism $Q \rtimes_\varphi P \to G$.
>
> *Source: PS 8.3(2)*

^prop-60-1

> [!proof]+ Proof
> *Idea:* $n_q$ divides $p$ and is $\equiv 1 \pmod q$, so $n_q = 1$; the product formula gives $QP = G$, and $(y, x) \mapsto yx$ turns the semidirect multiplication into the multiplication of $G$.
>
> *(Problem Set 8, Problem 8.3(2), as submitted, where $q \equiv 1 \pmod p$ is assumed; the argument does not use this assumption. “As in (1)” refers to Problem 8.3(1), the second proof of Proposition [[§55 The Sylow Theorems#^prop-55-11|§55.11]].)*
>
> **Sylow counts.** As in (1), $n_q \mid p$ and $n_q \equiv 1 \pmod q$ force $n_q = 1$, so $Q$ is normal in $G$. On the other hand, $n_p \mid q$ and $n_p \equiv 1 \pmod p$, and now both divisors $1$ and $q$ of $q$ are congruent to $1$ modulo $p$, so $n_p \in \{1, q\}$ and $P$ need not be normal.
>
> **$Q \cap P = \{e\}$ and $QP = G$.** As in (1), by Lagrange's theorem $|Q \cap P|$ divides both $q$ and $p$, so $Q \cap P = \{e\}$; and by Problem 8.1 (The Product Formula, Proposition [[§30 Orbit–Stabilizer#^prop-30-6|§30.6]]), $|QP| = \frac{|Q|\cdot|P|}{|Q \cap P|} = pq = |G|$, so $QP = G$.
>
> **The map $\varphi \colon P \to \operatorname{Aut}(Q)$.** For $x \in P$, define $\varphi(x) \colon Q \to Q$ by $\varphi(x)(y) = xyx^{-1}$, which lies in $Q$ since $Q$ is normal. Each $\varphi(x)$ is a homomorphism, since $x y_1y_2 x^{-1} = (xy_1x^{-1})(xy_2x^{-1})$, and it is bijective with inverse $\varphi(x^{-1})$; so $\varphi(x) \in \operatorname{Aut}(Q)$. Moreover, for $x_1, x_2 \in P$ and $y \in Q$,
>
> $$
> \varphi(x_1x_2)(y) = x_1x_2\,y\,x_2^{-1}x_1^{-1} = \varphi(x_1)\big(\varphi(x_2)(y)\big),
> $$
>
> so $\varphi \colon P \to \operatorname{Aut}(Q)$ is a group homomorphism. Let $Q \rtimes_\varphi P$ be the semidirect product, with multiplication $(y_1, x_1)\cdot(y_2, x_2) = \big(y_1\,\varphi(x_1)(y_2),\ x_1x_2\big)$.
>
> **The isomorphism.** Define
>
> $$
> \Phi \colon Q \rtimes_\varphi P \to G, \qquad \Phi(y, x) = yx.
> $$
>
> *Homomorphism.* For $(y_1, x_1), (y_2, x_2) \in Q \rtimes_\varphi P$, inserting $x_1^{-1}x_1 = e$,
>
> $$
> \begin{aligned}\Phi(y_1, x_1)\,\Phi(y_2, x_2) &= y_1x_1y_2x_2 = y_1\,(x_1y_2x_1^{-1})\,x_1x_2 \\
> &= y_1\,\varphi(x_1)(y_2)\,x_1x_2 = \Phi\big((y_1, x_1)\cdot(y_2, x_2)\big).\end{aligned}
> $$
>
> *Injective.* If $\Phi(y, x) = yx = e$, then $y = x^{-1} \in P$ and $y \in Q$, so $y \in Q \cap P = \{e\}$; thus $y = e$ and $x = e$.
>
> *Surjective.* Every $g \in G = QP$ is of the form $yx = \Phi(y, x)$ with $y \in Q$, $x \in P$.
>
> Hence $\Phi$ is an isomorphism, and $G \cong Q \rtimes_\varphi P$ for the homomorphism $\varphi \colon P \to \operatorname{Aut}(Q)$ given by conjugation.
>
> *(Not submitted.)* The last two steps are the case $N = Q$, $S = P$ of $S$ Acts on $N$ by Automorphisms (Proposition [[§58 Semidirect Products#^prop-58-3|§58.3]]) and of Internal and External Semidirect Products Agree (Theorem [[§58 Semidirect Products#^thm-58-6|§58.6]](1)); the submitted proof checks them directly.

^pf-60-1

*Uses:* [[§55 The Sylow Theorems#^prop-55-11|§55.11]], [[§30 Orbit–Stabilizer#^prop-30-6|§30.6]], [[§58 Semidirect Products#^prop-58-3|§58.3]], [[§58 Semidirect Products#^thm-58-6|§58.6]]

By Proposition [[§60 Groups of Order pq as Semidirect Products#^prop-60-1|§60.1]], the group $G$ is known once the homomorphism $\varphi \colon P \to \operatorname{Aut}(Q)$ is known. Here $P \cong \mathbb{Z}/p\mathbb{Z}$ and $Q \cong \mathbb{Z}/q\mathbb{Z}$, since groups of prime order are cyclic (Theorem [[§29 The Index and Lagrange's Theorem#^thm-29-7|§29.7]]).

*(Problem Set 8, Problem 8.3(3), as submitted.)* **Reduction.** Fix isomorphisms $\iota_Q \colon \mathbb{Z}/q\mathbb{Z} \to Q$ and $\iota_P \colon \mathbb{Z}/p\mathbb{Z} \to P$. Then $\alpha \mapsto \iota_Q^{-1} \circ \alpha \circ \iota_Q$ is a group isomorphism $\operatorname{Aut}(Q) \to \operatorname{Aut}(\mathbb{Z}/q\mathbb{Z})$, and composing with $\iota_P$ identifies homomorphisms $P \to \operatorname{Aut}(Q)$ with homomorphisms $\mathbb{Z}/p\mathbb{Z} \to \operatorname{Aut}(\mathbb{Z}/q\mathbb{Z})$. Hence we may take $Q = \mathbb{Z}/q\mathbb{Z}$ and $P = \mathbb{Z}/p\mathbb{Z}$, both written additively.

> [!theorem] Lemma §60.2: Automorphisms of $\mathbb{Z}/q\mathbb{Z}$
> Let $q$ be a prime. For $a \in (\mathbb{Z}/q\mathbb{Z})^\times$ define $\alpha_a \colon \mathbb{Z}/q\mathbb{Z} \to \mathbb{Z}/q\mathbb{Z}$ by $\alpha_a(x) = ax$.
>
> 1. Each $\alpha_a$ is an automorphism of the additive group $\mathbb{Z}/q\mathbb{Z}$.
> 2. Every automorphism $\rho$ of $\mathbb{Z}/q\mathbb{Z}$ is $\alpha_a$ for exactly one $a \in (\mathbb{Z}/q\mathbb{Z})^\times$, namely $a = \rho(1)$.
> 3. $\alpha_a \circ \alpha_b = \alpha_{ab}$ and $\alpha_1 = \mathrm{id}$, so $a \mapsto \alpha_a$ is an isomorphism $(\mathbb{Z}/q\mathbb{Z})^\times \to \operatorname{Aut}(\mathbb{Z}/q\mathbb{Z})$.
>
> *Source: PS 8.3(3), first half*

^lem-60-2

> [!proof]+ Proof
> *Idea:* A homomorphism out of $\mathbb{Z}/q\mathbb{Z}$ is determined by the image $a$ of $1$, and it is injective only if $a \neq 0$.
>
> *(Problem Set 8, Problem 8.3(3), as submitted; there $Q = \mathbb{Z}/q\mathbb{Z}$.)* For $a \in (\mathbb{Z}/q\mathbb{Z})^\times$, define $\alpha_a \colon \mathbb{Z}/q\mathbb{Z} \to \mathbb{Z}/q\mathbb{Z}$ by $\alpha_a(x) = ax$. It is a homomorphism, since $a(x + y) = ax + ay$, and it is bijective with inverse $\alpha_{a^{-1}}$; so $\alpha_a \in \operatorname{Aut}(Q)$.
>
> Conversely, let $\rho \in \operatorname{Aut}(Q)$ and set $a = \rho(1)$. Every element of $\mathbb{Z}/q\mathbb{Z}$ is represented by some $k \in \{0, 1, \dots, q-1\}$; writing it as $1 + \cdots + 1$ ($k$ times) and using that $\rho$ is a homomorphism,
>
> $$
> \rho(k) = \rho(1) + \cdots + \rho(1) = k\,\rho(1) = ak.
> $$
>
> Since $\rho$ is injective and $\rho(0) = 0$, $a = \rho(1) \neq 0$; as $q$ is prime, every nonzero element of $\mathbb{Z}/q\mathbb{Z}$ is a unit, so $a \in (\mathbb{Z}/q\mathbb{Z})^\times$. Hence $\rho = \alpha_a$, and every automorphism of $Q$ is of the form $x \mapsto ax$ for some $a \in (\mathbb{Z}/q\mathbb{Z})^\times$.
>
> Moreover $\alpha_a \circ \alpha_b = \alpha_{ab}$, $\alpha_1 = \mathrm{id}_Q$, and $\alpha_a = \alpha_b$ implies $a = \alpha_a(1) = \alpha_b(1) = b$.
>
> *(Not submitted.)* The last line says that $a \mapsto \alpha_a$ is an injective homomorphism $(\mathbb{Z}/q\mathbb{Z})^\times \to \operatorname{Aut}(\mathbb{Z}/q\mathbb{Z})$; it is surjective by (2), which gives (3).

^pf-60-2

> [!remark]- Connections
> - The unit group $(\mathbb{Z}/q\mathbb{Z})^\times$: [[§8 Invertibility and Unit Groups#^def-8-4|Def. §8.4]]; automorphism groups: [[§18 Conjugation, Products, and Pointwise Products#^def-18-1|Def. §18.1]].

> [!theorem] Proposition §60.3: Homomorphisms $\mathbb{Z}/p\mathbb{Z} \to \operatorname{Aut}(\mathbb{Z}/q\mathbb{Z})$
> Let $p$ and $q$ be primes, and let $\alpha_a$ be as in Lemma [[§60 Groups of Order pq as Semidirect Products#^lem-60-2|§60.2]]. Sending a homomorphism $\psi \colon \mathbb{Z}/p\mathbb{Z} \to \operatorname{Aut}(\mathbb{Z}/q\mathbb{Z})$ to the element $a$ with $\psi(1) = \alpha_a$ is a bijection
>
> $$
> \{\text{homomorphisms } \mathbb{Z}/p\mathbb{Z} \to \operatorname{Aut}(\mathbb{Z}/q\mathbb{Z})\} \longrightarrow \{a \in \mathbb{Z}/q\mathbb{Z} : a^p = 1\}.
> $$
>
> Its inverse sends a solution $a$ to the homomorphism $\psi_a$, $\psi_a(k \bmod p) = \alpha_{a^k}$.
>
> *Source: PS 8.3(3), second half*

^prop-60-3

> [!proof]+ Proof
> *Idea:* A homomorphism out of $\mathbb{Z}/p\mathbb{Z}$ is determined by the image $\alpha_a$ of $1$, and the only condition on it is that its $p$-th power is the identity, $\alpha_{a^p} = \alpha_1$.
>
> *(Problem Set 8, Problem 8.3(3), as submitted.)* Let $\psi \colon \mathbb{Z}/p\mathbb{Z} \to \operatorname{Aut}(Q)$ be a homomorphism, and write $\psi(1) = \alpha_a$ with $a \in (\mathbb{Z}/q\mathbb{Z})^\times$. Every element of $\mathbb{Z}/p\mathbb{Z}$ is $k \cdot 1$ for some $k \in \{0, 1, \dots, p-1\}$, and for such $k$,
>
> $$
> \psi(k \cdot 1) = \psi(1) \circ \cdots \circ \psi(1) \ (k \text{ times}) = \alpha_a^{\,k} = \alpha_{a^k},
> $$
>
> so $\psi$ is determined by $a$. Since $p \cdot 1 = 0$ in $\mathbb{Z}/p\mathbb{Z}$ and $\psi(p \cdot 1) = \psi(1)^p$ for any homomorphism,
>
> $$
> \alpha_{a^p} = \alpha_a^{\,p} = \psi(p \cdot 1) = \psi(0) = \mathrm{id}_Q = \alpha_1,
> $$
>
> so $a^p \equiv 1 \pmod q$.
>
> Conversely, let $a \in \mathbb{Z}/q\mathbb{Z}$ with $a^p \equiv 1 \pmod q$; then $a \neq 0$, so $a \in (\mathbb{Z}/q\mathbb{Z})^\times$. Define $\psi_a \colon \mathbb{Z}/p\mathbb{Z} \to \operatorname{Aut}(Q)$ by $\psi_a(k \bmod p) = \alpha_{a^k}$ for $k \in \mathbb{Z}$; here $a^k$ makes sense for negative $k$ since $a$ is a unit. It is well defined: if $k \equiv k' \pmod p$, then $k' = k + mp$ for some $m \in \mathbb{Z}$, and
>
> $$
> a^{k'} = a^k\,(a^p)^m \equiv a^k \cdot 1^m = a^k \pmod q,
> $$
>
> so $\alpha_{a^{k'}} = \alpha_{a^k}$. It is a homomorphism: for $k, l \in \mathbb{Z}$,
>
> $$
> \psi_a\big((k + l) \bmod p\big) = \alpha_{a^{k+l}} = \alpha_{a^ka^l} = \alpha_{a^k} \circ \alpha_{a^l} = \psi_a(k \bmod p) \circ \psi_a(l \bmod p).
> $$
>
> And $\psi_a(1) = \alpha_a$.
>
> Therefore $\psi \mapsto a$, where $\psi(1) = \alpha_a$, is a bijection from homomorphisms $P \to \operatorname{Aut}(Q)$ to solutions $a \in \mathbb{Z}/q\mathbb{Z}$ of $a^p \equiv 1 \pmod q$, with inverse $a \mapsto \psi_a$. That is, giving a homomorphism from $P$ to $\operatorname{Aut}(Q)$ is the same as finding a solution to $a^p \equiv 1 \pmod q$.

^pf-60-3

> [!theorem] Theorem §60.4: Classification of Groups of Order $pq$
> Let $p < q$ be primes.
>
> 1. If $q \not\equiv 1 \pmod p$, every group of order $pq$ is isomorphic to $\mathbb{Z}/pq\mathbb{Z}$.
> 2. If $q \equiv 1 \pmod p$, the congruence $a^p \equiv 1 \pmod q$ has exactly $p$ solutions. The solution $a = 1$ gives $\mathbb{Z}/p\mathbb{Z} \times \mathbb{Z}/q\mathbb{Z}$. Each of the $p - 1$ other solutions gives a non-abelian group $\mathbb{Z}/q\mathbb{Z} \rtimes_{\psi_a} \mathbb{Z}/p\mathbb{Z}$ of order $pq$, and these non-abelian groups are all isomorphic to each other.
>
> So there is one group of order $pq$ up to isomorphism in the first case, and two in the second.
>
> *Source: PS 8.3, closing paragraph (stated without proof)*

^thm-60-4

> [!proof]+ Proof (not given in this course)
> Part (1) is Proposition [[§55 The Sylow Theorems#^prop-55-11|§55.11]]. In part (2), every group of order $pq$ is isomorphic to $\mathbb{Z}/q\mathbb{Z} \rtimes_{\psi_a} \mathbb{Z}/p\mathbb{Z}$ for a solution $a$ of $a^p \equiv 1 \pmod q$ (Propositions [[§60 Groups of Order pq as Semidirect Products#^prop-60-1|§60.1]] and [[§60 Groups of Order pq as Semidirect Products#^prop-60-3|§60.3]], with the reduction between them), and for $a = 1$ the action is trivial, so the semidirect product is the direct product (Proposition [[§58 Semidirect Products#^prop-58-7|§58.7]](1)). The number of solutions, and the isomorphism between the non-abelian groups, are stated on Problem Set 8 without proof; the problem set leaves them out as number theory rather than group theory.

^pf-60-4

*Uses:* [[§55 The Sylow Theorems#^prop-55-11|§55.11]], [[§60 Groups of Order pq as Semidirect Products#^prop-60-1|§60.1]], [[§60 Groups of Order pq as Semidirect Products#^prop-60-3|§60.3]], [[§58 Semidirect Products#^prop-58-7|§58.7]]

> [!example] Example §60.1: The Orders $6$, $15$ and $21$
> *(Not from class.)*
>
> 1. *Order $6$ ($p = 2$, $q = 3$, $3 \equiv 1 \pmod 2$).* The solutions of $a^2 \equiv 1 \pmod 3$ are $a = 1$ and $a = 2 = -1$: two solutions, as $p = 2$. They give $\mathbb{Z}/3\mathbb{Z} \times \mathbb{Z}/2\mathbb{Z} \cong \mathbb{Z}/6\mathbb{Z}$ and, for $\alpha_{-1}(x) = -x$, the group $\mathbb{Z}/3\mathbb{Z} \rtimes \mathbb{Z}/2\mathbb{Z} \cong S_3$ of Example [[§58 Semidirect Products#^ex-58-4|§58.4]].
> 2. *Order $15$ ($p = 3$, $q = 5$, $5 \not\equiv 1 \pmod 3$).* Modulo $5$ the cubes of $1, 2, 3, 4$ are $1, 3, 2, 4$, so $a^3 \equiv 1 \pmod 5$ has the single solution $a = 1$. The only homomorphism $\mathbb{Z}/3\mathbb{Z} \to \operatorname{Aut}(\mathbb{Z}/5\mathbb{Z})$ is the trivial one, in agreement with Example [[§55 The Sylow Theorems#^ex-55-3|§55.3]]: every group of order $15$ is cyclic.
> 3. *Order $21$ ($p = 3$, $q = 7$, $7 \equiv 1 \pmod 3$).* Modulo $7$ the cubes of $1, \ldots, 6$ are $1, 1, 6, 1, 6, 6$, so the solutions of $a^3 \equiv 1 \pmod 7$ are $a = 1, 2, 4$: three solutions, as $p = 3$. The solution $a = 2$ gives the group of Example [[§58 Semidirect Products#^ex-58-3|§58.3]]. The solution $a = 4 = 2^2$ gives an isomorphic group: $(x, k) \mapsto (x, 2k)$ is an isomorphism $\mathbb{Z}/7\mathbb{Z} \rtimes_{\psi_4} \mathbb{Z}/3\mathbb{Z} \to \mathbb{Z}/7\mathbb{Z} \rtimes_{\psi_2} \mathbb{Z}/3\mathbb{Z}$, since $k \mapsto 2k$ is a bijection of $\mathbb{Z}/3\mathbb{Z}$ and
>
> $$
> (x_1, 2k_1)(x_2, 2k_2) = (x_1 + 2^{2k_1}x_2,\ 2k_1 + 2k_2) = (x_1 + 4^{k_1}x_2,\ 2(k_1 + k_2)).
> $$
>
> So the groups of order $21$ are $\mathbb{Z}/21\mathbb{Z}$ and one non-abelian group.

^ex-60-1

> [!remark]- Connections
> - The order $21$ from the Sylow side, with the two candidates $n_3 = 1$ and $n_3 = 7$: [[§56 Simple Groups of Small Order#^ex-56-1|Example §56.1]].
