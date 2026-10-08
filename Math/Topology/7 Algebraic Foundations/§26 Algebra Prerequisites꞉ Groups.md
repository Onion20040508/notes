---
type: section
subject: "[[Topology]]"
chapter: 7
section: 26
munkres: "§69"
tags: [topology, math590]
---
← [[§25 The Lower Limit Topology, ℝ^ω and Discrete Subspaces]] · ↑ [[· 7 Algebraic Foundations]] · [[§27 Free Groups and Presentations]] →

## Part II: Algebraic Topology

> [!remark] Remark: The Central Question of Algebraic Topology
> **Q:** Given topological spaces $X$ and $Y$, are $X$ and $Y$ [[§10 Continuous Functions#^def-10-2|homeomorphic]]?
>
> Point-set topology provides some invariants: [[§18 Compact Spaces#^def-18-2|compactness]], [[§15 Connected Spaces#^def-15-2|connectedness]], [[§9 Hausdorff Spaces#^def-9-1|Hausdorff]], etc. These suffice for simple cases:
> - $[0,1] \not\cong (0,1)$: one is compact, the other is not.
> - $\mathbb{R} \not\cong \mathbb{R}^2$: removing a point from $\mathbb{R}$ gives a disconnected space, but $\mathbb{R}^2 \setminus \{p\}$ is still connected.
>
> But these tools are not enough: **is $\mathbb{R}^2 \cong \mathbb{R}^3$?** Both are connected, non-compact, Hausdorff, second-countable, and removing a point from either leaves a connected space. We need a new technique.
>
> The idea: $\mathbb{R}^2 \setminus \{p\}$ has loops that cannot be “shrunk to a point,” while in $\mathbb{R}^3 \setminus \{p\}$ every loop can be contracted. This is captured by the **[[§29 The Fundamental Group#^def-29-2|fundamental group]]** $\pi_1$. The key concept is **[[§29 The Fundamental Group#^def-29-3|simply connected]]**: a space is simply connected if every closed curve can be continuously shrunk to a point.

^rem-II-1

> [!remark] Remark: The Role of the Quotient Space Toolkit in Part II
> Many spaces whose $\pi_1$ we want to compute are built by **gluing**: $S^1 = [0, 2\pi]/(0 \sim 2\pi)$, the torus $T^2 = [0, 2\pi]^2/(\text{opposite edges})$, $S^n = B^n/(\text{collapse boundary})$. To compute $\pi_1$ of these spaces, we repeatedly need to:
> 1. **Build homotopies on a simple space** (a square, an interval, a ball) where geometry is easy — straight lines, rays, linear interpolations all work.
> 2. **Descend them to the quotient space** (a torus, a circle, a sphere) where the topology lives.
>
> Step 2 is where the **[[Universal Property of Quotient Maps|Universal Property of Quotient Maps]]** ([[Universal Property of Quotient Maps|§13.3]]) enters: it guarantees that if a map on the simple space respects the gluing (sends identified points to the same place), then it descends to a well-defined continuous map on the quotient. The [[§13 Quotient Topology#^rem-13-8|Quotient Space Toolkit]] (Theorems A, B, C from [[§13 Quotient Topology|§13]]) will appear in:
> - The **[[§34 Retractions and Fixed Points#^lem-34-8|nullhomotopy lemma]]**: $\pi: S^n \times I \to B^{n+1}$ by $\pi(x,t) = (1-t)x$ is a quotient map ([[§13 Quotient Topology#^rem-13-8|Thm A]]); a nullhomotopy $H$ descends to an extension $k: B^{n+1} \to X$ ([[Universal Property of Quotient Maps|Thm C]]).
> - The **[[§31 Covering Spaces#^thm-31-2|covering map]]** $p: \mathbb{R} \to S^1$: the interval $[0, 2\pi]$ quotients to $S^1$ ([[§13 Quotient Topology#^rem-13-8|Thm A]]); the winding number computation uses the fact that $p$ is a quotient map.
> - **$\pi_1(T^2) \cong \mathbb{Z} \times \mathbb{Z}$** ([[§29 The Fundamental Group#^cor-29-8|Corollary §29.8]]): $[0, 2\pi]^2$ quotients to $T^2$ ([[§13 Quotient Topology#^thm-13-5|Thm B]]); deformation retracts on the square descend to the torus ([[Universal Property of Quotient Maps|Thm C]]).
>
> The pattern is always the same: **work upstairs, check the gluing, descend**.

^rem-II-2

*This section is a self-contained review of the group theory needed for algebraic topology. No prior algebra is assumed.*

> [!remark] Remark: Why Groups in Topology?
> The central idea of algebraic topology is to assign algebraic objects (groups) to topological spaces in a way that respects continuous maps. If two spaces are homeomorphic, they get isomorphic groups; if the groups are different, the spaces cannot be homeomorphic. The **[[§29 The Fundamental Group#^def-29-2|fundamental group]]** $\pi_1(X, x_0)$ captures the “loop structure” of a space. To make this precise, we need the language of groups.

^rem-26-1

## Groups

> [!definition] Definition §26.1: Group
> A **group** is a set $G$ together with a binary operation $\cdot\,: G \times G \to G$, $(a, b) \mapsto a \cdot b$, satisfying:
> 1. **Associativity:** $(a \cdot b) \cdot c = a \cdot (b \cdot c)$ for all $a, b, c \in G$.
> 2. **Identity:** There exists $e \in G$ such that $e \cdot g = g \cdot e = g$ for all $g \in G$.
> 3. **Inverses:** For each $g \in G$, there exists $g^{-1} \in G$ such that $g \cdot g^{-1} = g^{-1} \cdot g = e$.
>
> If additionally $a \cdot b = b \cdot a$ for all $a, b \in G$, we say $G$ is **abelian**.

^def-26-1

> [!remark]- Connections
> - Developed in full in Group Theory: [[§1 The Definition of a Group#^def-1-1|493 Def. §1.1]], with the uniqueness and cancellation facts in [[§2 First Consequences of the Axioms|493 §2]] and [[Cancellation Laws in Groups]].

> [!remark] Remark: Uniqueness of Identity and Inverses
> The identity is unique: if $e$ and $e'$ are both identities, then $e = e \cdot e' = e'$. Inverses are unique: if $g \cdot h = e$ and $g \cdot h' = e$, left-multiplying by $g^{-1}$ gives $h = h'$.

^rem-26-2

> [!example] Example §26.1: Key Examples
> - $(\mathbb{Z}, +)$: integers under addition. Identity: $0$. Inverse of $n$: $-n$. Abelian.
> - $(\mathbb{Z}/n\mathbb{Z}, +)$: integers mod $n$. Elements $\{0, 1, \ldots, n-1\}$ with addition mod $n$. Abelian, $|G| = n$.
> - $(S_n, \circ)$: permutations of $\{1, \ldots, n\}$ under composition ([[§3 Basic Examples of Groups#^def-3-5|493 Def. §3.5]]). **Not abelian** for $n \geq 3$.
> - The **trivial group**: $G = \{e\}$.

^ex-26-1

## Subgroups

> [!definition] Definition §26.2: Subgroup
> $H \subseteq G$ is a **subgroup** ($H \leq G$) if $H$ is a group under the inherited operation. Equivalently:
> 1. $e \in H$;
> 2. $a, b \in H \Rightarrow ab \in H$;
> 3. $a \in H \Rightarrow a^{-1} \in H$.

^def-26-2

> [!remark]- Connections
> - Linear-algebra analogue: [[§3 Subspaces#^ladr-1-34|Conditions for a subspace]].
> - Developed in full in Group Theory: [[§4 Subgroups#^def-4-1|493 Def. §4.1]], with the one-step test in [[Subgroup Criteria]].

> [!theorem] Proposition §26.1: Properties Inherited by Subgroups
> Let $H \leq G$ be a subgroup. Then:
> 1. If $G$ is abelian, then $H$ is abelian.
> 2. If $G$ is [[§27 Free Groups and Presentations#^def-27-2|cyclic]] (defined below), then $H$ is cyclic.
> 3. If $G$ is finite of order $n$, then $|H|$ divides $n$ (Lagrange's theorem).

^prop-26-1

> [!proof]+ Proof
> **(1)** If $a, b \in H$, then $a, b \in G$, so $ab = ba$ (since $G$ is abelian). The same equation holds in $H$.
>
> **(2)** If $G = \langle g \rangle$, every element of $H$ has the form $g^k$ for some $k$. If $H = \{e\}$, then $H = \langle e \rangle$. Otherwise $H$ contains some $g^k$ with $k \neq 0$, hence also $g^{-k}$, so it contains a positive power of $g$; let $m$ be the smallest positive integer with $g^m \in H$. Then $H = \langle g^m \rangle$ (one can show every element of $H$ is a power of $g^m$ by the [[Division Algorithm|division algorithm]]).
>
> **(3)** Lagrange's theorem — the proof uses cosets and is standard in algebra. We state it without proof.

^pf-26-1

*Uses:* [[§26 Algebra Prerequisites꞉ Groups#^def-26-2|Def. §26.2]], [[§27 Free Groups and Presentations#^def-27-2|Def. §27.2]], [[Division Algorithm|493 §6.1]]

> [!remark]- Connections
> - Proved in 493: (2) is [[§17 Cyclic Groups#^thm-17-4|493 Thm. §17.4]] ([[Subgroups of Cyclic Groups Are Cyclic]]) and (3), stated here without proof, is [[§29 The Index and Lagrange's Theorem#^thm-29-2|493 Thm. §29.2]] ([[Lagrange's Theorem]]).

> [!theorem] Proposition §26.2: Contrapositive: Detecting Non-Abelian Groups
> If $G$ contains a non-abelian subgroup $H$, then $G$ is non-abelian.

^prop-26-2

> [!proof]+ Proof
> This is the contrapositive of [[§26 Algebra Prerequisites꞉ Groups#^prop-26-1|(1) above]]. If $G$ were abelian, then every subgroup $H$ would be abelian (since the operation in $H$ is inherited from $G$). So if $H$ is non-abelian, $G$ cannot be abelian.
>
> Explicitly: there exist $a, b \in H$ with $ab \neq ba$. Since $H \subseteq G$, these same $a, b$ are in $G$ with $ab \neq ba$. So $G$ is non-abelian.

^pf-26-2

*Uses:* [[§26 Algebra Prerequisites꞉ Groups#^prop-26-1|§26.1]]

## Homomorphisms and Isomorphisms

> [!definition] Definition §26.3: Homomorphism
> A map $f: G \to G'$ (both groups) is a **homomorphism** if $f(x \cdot y) = f(x) \cdot f(y)$ for all $x, y \in G$.

^def-26-3

> [!remark]- Connections
> - Developed in full in Group Theory: [[§15 Homomorphisms#^def-15-1|493 Def. §15.1]].

> [!theorem] Theorem §26.3: Homomorphisms Preserve Identity and Inverses
> Let $f: G \to G'$ be a homomorphism. Then:
> 1. $f(e_G) = e_{G'}$.
> 2. $f(a^{-1}) = f(a)^{-1}$ for all $a \in G$.

^thm-26-3

> [!proof]+ Proof
> **(1)** We have $f(e_G) = f(e_G \cdot e_G) = f(e_G) \cdot f(e_G)$. Left-multiplying both sides by $f(e_G)^{-1}$:
>
> $$
> f(e_G)^{-1} \cdot f(e_G) = f(e_G)^{-1} \cdot f(e_G) \cdot f(e_G) \implies e_{G'} = f(e_G).
> $$
>
> **(2)** We have $f(a) \cdot f(a^{-1}) = f(a \cdot a^{-1}) = f(e_G) = e_{G'}$ by (1). Similarly, $f(a^{-1}) \cdot f(a) = f(a^{-1} \cdot a) = e_{G'}$. So $f(a^{-1})$ is both a left and right inverse of $f(a)$. Since [[§26 Algebra Prerequisites꞉ Groups#^rem-26-2|inverses in a group are unique]], $f(a^{-1}) = f(a)^{-1}$.

^pf-26-3

*Uses:* [[§26 Algebra Prerequisites꞉ Groups#^def-26-3|Def. §26.3]]

> [!remark]- Connections
> - Linear-algebra version of (1): [[§7 Vector Space of Linear Maps#^ladr-3-10|Linear maps take 0 to 0]].
> - 493 counterpart: [[§15 Homomorphisms#^prop-15-1|493 Prop. §15.1]].

> [!remark] Remark
> Note that only the homomorphism property $f(xy) = f(x)f(y)$ is assumed — preservation of identity and inverses follows automatically. This is why the definition of homomorphism only requires preserving the operation.

^rem-26-3

> [!theorem] Proposition §26.4: Bijectivity via Two-Sided Inverse
> A map $f: A \to B$ is bijective if and only if there exists a map $g: B \to A$ such that $f \circ g = \operatorname{id}_B$ and $g \circ f = \operatorname{id}_A$.
>
> Moreover, each condition alone gives half the result:
> - $g \circ f = \operatorname{id}_A$ alone $\Rightarrow$ $f$ is injective.
> - $f \circ g = \operatorname{id}_B$ alone $\Rightarrow$ $f$ is surjective.

^prop-26-4

> [!proof]+ Proof
> **Injective from $g \circ f = \operatorname{id}_A$:** If $f(x) = f(y)$, apply $g$: $x = g(f(x)) = g(f(y)) = y$.
>
> **Surjective from $f \circ g = \operatorname{id}_B$:** For any $b \in B$, set $a = g(b)$. Then $f(a) = f(g(b)) = b$.
>
> **Both together:** $f$ is injective and surjective, hence bijective. The map $g$ is then the inverse function $f^{-1}$.

^pf-26-4

> [!remark]- Connections
> - Linear-algebra version: [[§10 Invertibility and Isomorphisms#^ladr-3-63|Invertibility ⟺ injectivity and surjectivity]].
> - Elementary version: invertible means bijective, [[§9 Injections, Surjections and Bijections#^thm-9-2|250 Thm. §9.2]], and inverses via composition, [[§9 Injections, Surjections and Bijections#^prop-9-3|250 Prop. §9.3]].
> - In 493 this gives that each group element acts bijectively, [[§25 Actions#^prop-25-2|493 Prop. §25.2]], so that an action lands in the symmetric group [[§3 Basic Examples of Groups#^def-3-5|493 Def. §3.5]].

> [!remark] Remark
> This is the standard technique for proving bijectivity in algebraic topology: construct two maps, show they compose to the identity in both orders. It appears repeatedly: the [[Basepoint Independence of π₁|basepoint independence isomorphism]] ([[§29 The Fundamental Group|§29]]), the [[§29 The Fundamental Group#^cor-29-6|functorial corollary]] that $\pi_1$ is a topological invariant ([[§29 The Fundamental Group|§29]]), and the [[Deformation Retract Induces Isomorphism on π₁|deformation retract theorem]] ([[§35 Deformation Retracts and Homotopy Type|§35]]) all use exactly this pattern.

^rem-26-4

> [!definition] Definition §26.4: Isomorphism
> A [[§26 Algebra Prerequisites꞉ Groups#^def-26-3|homomorphism]] $f: G \to G'$ is an **isomorphism** if $f$ is bijective. We write $G \cong G'$.

^def-26-4

> [!remark]- Connections
> - Linear-algebra version: [[§10 Invertibility and Isomorphisms#^ladr-3-69|Isomorphism, isomorphic]].
> - 493 counterpart: [[§16 Isomorphisms#^def-16-1|493 Def. §16.1]], with isomorphism invariants in [[§16 Isomorphisms#^prop-16-5|493 §16.5]].

> [!theorem] Theorem §26.5: Inverse of an Isomorphism is a Homomorphism
> If $f: G \to G'$ is an isomorphism, then $f^{-1}: G' \to G$ is also a homomorphism (and hence an isomorphism).

^thm-26-5

> [!proof]+ Proof
> Let $x', y' \in G'$. Since $f$ is bijective, there exist unique $x, y \in G$ with $f(x) = x'$ and $f(y) = y'$. Then:
>
> $$
> f^{-1}(x' \cdot y') = f^{-1}(f(x) \cdot f(y)) = f^{-1}(f(x \cdot y)) = x \cdot y = f^{-1}(x') \cdot f^{-1}(y')
> $$
>
> where the second equality uses that $f$ is a homomorphism: $f(x) \cdot f(y) = f(x \cdot y)$.

^pf-26-5

*Uses:* [[§26 Algebra Prerequisites꞉ Groups#^def-26-3|Def. §26.3]], [[§26 Algebra Prerequisites꞉ Groups#^def-26-4|Def. §26.4]]

> [!remark]- Connections
> - 493 counterpart: [[§16 Isomorphisms#^prop-16-1|493 Prop. §16.1]].

> [!remark] Remark: Contrast with Topology
> In topology, a continuous bijection does *not* automatically have a continuous inverse — this is why [[§10 Continuous Functions#^def-10-2|homeomorphism]] requires both directions, and why the [[Bijection from Compact to Hausdorff is a Homeomorphism|compact-to-Hausdorff theorem]] is needed to get the inverse for free. For groups, bijectivity + forward homomorphism gives the inverse homomorphism for free. So “isomorphism = bijective homomorphism” is a *theorem*, not merely a convention: you only need to check one direction.

^rem-26-5

> [!theorem] Theorem §26.6: Isomorphisms Preserve All Algebraic Properties
> If $f: G \to G'$ is an isomorphism, then $G$ and $G'$ have identical group-theoretic structure. In particular:
> 1. $|G| = |G'|$ (same cardinality).
> 2. $G$ is abelian if and only if $G'$ is abelian.
> 3. $G$ is [[§27 Free Groups and Presentations#^def-27-2|cyclic]] (defined below) if and only if $G'$ is cyclic.
> 4. For each $n$, $G$ has an element of order $n$ if and only if $G'$ does.

^thm-26-6

> [!proof]+ Proof
> **(1)** $f$ is a bijection.
>
> **(2)** Suppose $G$ is abelian. For any $x', y' \in G'$, write $x' = f(x)$, $y' = f(y)$. Then $x' \cdot y' = f(x) \cdot f(y) = f(xy) = f(yx) = f(y) \cdot f(x) = y' \cdot x'$. The converse follows by applying the same argument to $f^{-1}$.
>
> **(3)** If $G = \langle a \rangle$, then every element of $G'$ has the form $f(a^n) = f(a)^n$, so $G' = \langle f(a) \rangle$. Converse via $f^{-1}$.
>
> **(4)** If $a \in G$ has order $n$ (i.e., $a^n = e$ and $n$ is minimal), then $f(a)^n = f(a^n) = f(e) = e'$. If $f(a)^k = e'$ for some $k < n$, then $f(a^k) = e'$, so $a^k = e$ (since $f$ is injective), contradicting minimality. So $f(a)$ has order $n$.

^pf-26-6

*Uses:* [[§26 Algebra Prerequisites꞉ Groups#^thm-26-5|§26.5]], [[§26 Algebra Prerequisites꞉ Groups#^thm-26-3|§26.3]], [[§27 Free Groups and Presentations#^def-27-2|Def. §27.2]]

> [!remark] Remark: Why Isomorphisms Matter
> An isomorphism is a **perfect dictionary** between two groups: you can do all your work in whichever group is more convenient, then translate the answer back. For algebraic topology, this has two consequences:
>
> **Computation:** $\pi_1(S^1) \cong \mathbb{Z}$ ([[Fundamental Group of the Circle|§32.5]]) means that everything about loops on $S^1$ can be answered by doing arithmetic in $\mathbb{Z}$. How many essentially different loops? Countably many, indexed by winding number. What happens when you concatenate a loop of winding number $3$ with one of winding number $-2$? Winding number $1$. The isomorphism converts hard topology into easy algebra.
>
> **Distinguishing spaces:** If $\pi_1(X) \not\cong \pi_1(Y)$ — meaning no isomorphism exists — then the groups have genuinely different structure that no relabeling can reconcile. Since homeomorphisms induce isomorphisms ([[§29 The Fundamental Group#^cor-29-6|Corollary §29.6]]), this forces $X \not\cong Y$. For instance, $\mathbb{Z} \not\cong \{e\}$ (different cardinalities), so $S^1 \not\cong \mathbb{R}^2$. And $\mathbb{Z} \not\cong \mathbb{Z}^2$ (one is cyclic, the other is not), so $S^1 \not\cong T^2$.

^rem-26-6

> [!remark]- Connections
> - The inputs: [[§29 The Fundamental Group#^ex-29-1|ℝⁿ is simply connected]], [[§29 The Fundamental Group#^cor-29-8|Fundamental Group of the Torus]]. More such arguments: [[§32 Lifting and the Fundamental Group of the Circle#^rem-32-14|How to Establish or Refute Isomorphisms]].
> - Proved item by item in 493: [[§16 Isomorphisms#^prop-16-5|493 Prop. §16.5]] (order, abelian, elements of each order, cyclic), with further invariants in [[§16 Isomorphisms#^prop-16-6|493 Prop. §16.6]].

> [!remark] Remark: Analogy: Topology $\leftrightarrow$ Algebra
> | | **Topology** | **Algebra** |
> |---|---|---|
> | Objects | Topological spaces | Groups |
> | Structure-preserving maps | Continuous maps | Homomorphisms |
> | “Same” objects | Homeomorphisms | Isomorphisms |
>
> Algebraic topology connects these: it assigns groups to spaces and homomorphisms to continuous maps.

^rem-26-7

> [!remark]- Connections
> - The assignment on maps: [[§29 The Fundamental Group#^def-29-4|Induced Homomorphism]], with [[Functoriality of π₁|Functoriality of π₁]].

> [!definition] Definition §26.5: Direct Product of Groups
> Let $G$ and $H$ be groups. The **direct product** $G \times H$ is the set of ordered pairs $\{(g, h) : g \in G, h \in H\}$ with the componentwise operation:
>
> $$
> (g_1, h_1) \cdot (g_2, h_2) = (g_1 \cdot g_2, \; h_1 \cdot h_2).
> $$
>
> The identity is $(e_G, e_H)$ and the inverse of $(g, h)$ is $(g^{-1}, h^{-1})$.

^def-26-5

> [!remark]- Connections
> - Linear-algebra version: [[§11 Products and Quotients of Vector Spaces#^ladr-3-87|Product of vector spaces]].
> - Appears as $\pi_1$ of a product: [[§29 The Fundamental Group#^thm-29-7|π₁ of a Product Space]].
> - 493 counterpart: [[§3 Basic Examples of Groups#^def-3-2|493 Def. §3.2]], with its universal property in [[§18 Conjugation, Products, and Pointwise Products#^prop-18-3|493 §18.3]].

> [!example] Example §26.2
> $\mathbb{Z} \times \mathbb{Z}$ is the group of integer pairs $(m, n)$ with addition $(m_1, n_1) + (m_2, n_2) = (m_1 + m_2, n_1 + n_2)$. Identity is $(0, 0)$, inverse of $(m, n)$ is $(-m, -n)$. This is abelian: $(m_1, n_1) + (m_2, n_2) = (m_2, n_2) + (m_1, n_1)$.

^ex-26-2

> [!theorem] Theorem §26.7: Products of Isomorphic Groups
> If $G \cong G'$ and $H \cong H'$, then $G \times H \cong G' \times H'$.

^thm-26-7

> [!proof]+ Proof
> Let $f: G \to G'$ and $g: H \to H'$ be isomorphisms. The natural candidate is “apply $f$ and $g$ separately”: define
>
> $$
> (f \times g): G \times H \to G' \times H', \qquad (f \times g)(a, b) = (f(a), \; g(b)).
> $$
>
> **Bijective:** The [[§26 Algebra Prerequisites꞉ Groups#^prop-26-4|two-sided inverse]] is $f^{-1} \times g^{-1}: G' \times H' \to G \times H$. Check both compositions:
>
> $$
> \begin{aligned}
> (f^{-1} \times g^{-1}) \circ (f \times g)(a, b) &= (f^{-1} \times g^{-1})(f(a), g(b)) = (f^{-1}(f(a)), \; g^{-1}(g(b))) = (a, b). \\
> (f \times g) \circ (f^{-1} \times g^{-1})(a', b') &= (f(f^{-1}(a')), \; g(g^{-1}(b'))) = (a', b').
> \end{aligned}
> $$
>
> **Homomorphism:** We verify $(f \times g)((a_1, b_1) \cdot (a_2, b_2)) = (f \times g)(a_1, b_1) \cdot (f \times g)(a_2, b_2)$:
>
> $$
> \begin{aligned}
> \text{LHS} &= (f \times g)(a_1 a_2, \; b_1 b_2) &\text{(definition of product in } G \times H\text{)}\\
> &= (f(a_1 a_2), \; g(b_1 b_2)) &\text{(definition of } f \times g\text{)}\\
> &= (f(a_1)f(a_2), \; g(b_1)g(b_2)) &\text{(}f, g \text{ are homomorphisms)}\\
> &= (f(a_1), g(b_1)) \cdot (f(a_2), g(b_2)) &\text{(definition of product in } G' \times H'\text{)}\\
> &= \text{RHS.}
> \end{aligned}
> $$

^pf-26-7

*Uses:* [[§26 Algebra Prerequisites꞉ Groups#^prop-26-4|§26.4]], [[§26 Algebra Prerequisites꞉ Groups#^def-26-5|Def. §26.5]]

## Kernel and Image

> [!definition] Definition §26.6: Kernel
> Let $f: G \to G'$ be a homomorphism.
>
> $$
> \ker(f) = \{g \in G \mid f(g) = e_{G'}\}.
> $$

^def-26-6

> [!definition] Definition §26.7: Image
> Let $f: G \to G'$ be a homomorphism.
>
> $$
> \operatorname{im}(f) = \{f(g) \mid g \in G\}.
> $$

^def-26-7

> [!remark]- Connections
> - Linear-algebra versions: [[§8 Null Spaces and Ranges#^ladr-3-11|Null space, null T]] (the kernel) and [[§8 Null Spaces and Ranges#^ladr-3-16|Range]] (the image).
> - 493 counterpart: [[§15 Homomorphisms#^def-15-3|493 Def. §15.3]], [[§15 Homomorphisms#^def-15-2|493 Def. §15.2]]; injectivity via the kernel in [[Injective iff Trivial Kernel]].

> [!theorem] Proposition §26.8
> $\ker(f) \leq G$ and $\operatorname{im}(f) \leq G'$. Moreover, $f$ is injective if and only if $\ker(f) = \{e\}$.

^prop-26-8

> [!proof]+ Proof
> **Kernel is subgroup:** $f(e) = e'$ so $e \in \ker(f)$. If $a, b \in \ker(f)$, then $f(ab^{-1}) = f(a)f(b)^{-1} = e'(e')^{-1} = e'$.
>
> **Image is subgroup:** $e' = f(e) \in \operatorname{im}(f)$. If $f(a), f(b) \in \operatorname{im}(f)$, then $f(a)f(b)^{-1} = f(ab^{-1}) \in \operatorname{im}(f)$.
>
> **Injectivity:** $(\Rightarrow)$: If $f$ injective and $f(g) = e' = f(e)$, then $g = e$. $(\Leftarrow)$: If $f(a) = f(b)$, then $f(ab^{-1}) = e'$, so $ab^{-1} = e$, giving $a = b$.

^pf-26-8

*Uses:* [[§26 Algebra Prerequisites꞉ Groups#^thm-26-3|§26.3]], [[§26 Algebra Prerequisites꞉ Groups#^def-26-2|Def. §26.2]]

> [!remark]- Connections
> - Linear-algebra versions: [[§8 Null Spaces and Ranges#^ladr-3-13|The null space is a subspace]], [[§8 Null Spaces and Ranges#^ladr-3-18|The range is a subspace]], [[§8 Null Spaces and Ranges#^ladr-3-15|Injectivity ⟺ null space equals {0}]].
> - 493 counterparts: [[§15 Homomorphisms#^prop-15-2|493 Prop. §15.2]] (kernel and image are subgroups) and [[§15 Homomorphisms#^prop-15-3|493 Prop. §15.3]] (hub [[Injective iff Trivial Kernel]]).

> [!theorem] Proposition §26.9: Injective Homomorphisms Preserve Subgroup Structure
> Let $f: G \to G'$ be an injective homomorphism. Then:
> 1. $f(G)$ is a subgroup of $G'$ isomorphic to $G$.
> 2. If $G$ is non-abelian, then $f(G)$ is a non-abelian subgroup of $G'$, and hence $G'$ is non-abelian.
> 3. If $G$ is infinite, then $G'$ contains an infinite subgroup, so $G'$ is infinite.

^prop-26-9

> [!proof]+ Proof
> **(1)** $f(G) \leq G'$: $f(e_G) = e_{G'} \in f(G)$; if $f(a), f(b) \in f(G)$, then $f(a)f(b) = f(ab) \in f(G)$; $f(a)^{-1} = f(a^{-1}) \in f(G)$. Since $f$ is injective, $f: G \to f(G)$ is a bijective homomorphism, hence an isomorphism.
>
> **(2)** Since $f: G \to f(G)$ is an isomorphism, $f(G)$ is non-abelian ([[§26 Algebra Prerequisites꞉ Groups#^thm-26-6|isomorphisms preserve abelianness]]). By the contrapositive ([[§26 Algebra Prerequisites꞉ Groups#^prop-26-2|§26.2]]): a group containing a non-abelian subgroup is itself non-abelian. So $G'$ is non-abelian.
>
> **(3)** Since $f$ is injective, $|f(G)| = |G| = \infty$.

^pf-26-9

*Uses:* [[§26 Algebra Prerequisites꞉ Groups#^thm-26-3|§26.3]], [[§26 Algebra Prerequisites꞉ Groups#^def-26-4|Def. §26.4]], [[§26 Algebra Prerequisites꞉ Groups#^thm-26-6|§26.6]], [[§26 Algebra Prerequisites꞉ Groups#^prop-26-2|§26.2]]

> [!theorem] Proposition §26.10: Surjective Homomorphisms Preserve Abelianness
> Let $f: G \to G'$ be a surjective homomorphism. If $G$ is abelian, then $G'$ is abelian.
>
> Equivalently (contrapositive): if $G'$ is non-abelian, then $G$ is non-abelian.

^prop-26-10

> [!proof]+ Proof
> Let $x', y' \in G'$. Since $f$ is surjective, there exist $x, y \in G$ with $f(x) = x'$ and $f(y) = y'$. Then:
>
> $$
> x' \cdot y' = f(x) \cdot f(y) = f(x \cdot y) = f(y \cdot x) = f(y) \cdot f(x) = y' \cdot x',
> $$
>
> where the third equality uses $x \cdot y = y \cdot x$ (since $G$ is abelian). So $G'$ is abelian.

^pf-26-10

*Uses:* [[§26 Algebra Prerequisites꞉ Groups#^def-26-3|Def. §26.3]]

> [!remark] Remark: Why This Matters for $\pi_1$: Two Directions from a Retraction
> If $A$ is a [[§34 Retractions and Fixed Points#^def-34-1|retract]] of $X$ (with retraction $r$ and inclusion $j$), then $r_* \circ j_* = \operatorname{id}$ on $\pi_1(A)$, giving two [[§29 The Fundamental Group#^def-29-4|induced maps]]:
>
> **$j_{\ast}: \pi_1(A) \hookrightarrow \pi_1(X)$ (injective):** Embeds $\pi_1(A)$ as a subgroup of $\pi_1(X)$. Conclusion: $\pi_1(X)$ is *at least as complicated* as $\pi_1(A)$.
>
> **$r_{\ast}: \pi_1(X) \twoheadrightarrow \pi_1(A)$ (surjective):** Maps $\pi_1(X)$ onto $\pi_1(A)$. Conclusion: $\pi_1(X)$ *cannot be simpler* than $\pi_1(A)$ (an abelian group can only surject onto abelian groups).
>
> Both directions detect non-abelianness:
> - Via $j_*$: non-abelian $\pi_1(A)$ embeds $\Rightarrow$ non-abelian subgroup $\Rightarrow$ non-abelian $\pi_1(X)$ ([[§26 Algebra Prerequisites꞉ Groups#^prop-26-9|§26.9]]).
> - Via $r_*$: if $\pi_1(X)$ were abelian, $r_*$ surjects onto abelian image $\Rightarrow$ $\pi_1(A)$ abelian, contradiction ([[§26 Algebra Prerequisites꞉ Groups#^prop-26-10|§26.10]]).

^rem-26-8

> [!remark]- Connections
> - Made precise in [[§34 Retractions and Fixed Points#^prop-34-3|Algebraic Properties of Retractions]] and [[§34 Retractions and Fixed Points#^cor-34-4|What Properties Transfer via Retraction]]; applied in [[§38 Fundamental Group of Some Surfaces#^thm-38-5|π₁(Σ₂) is Non-Abelian]].

*Continued in [[§27 Free Groups and Presentations]]: cyclic groups, free groups and free products, group presentations, normal subgroups and quotient groups.*
