---
type: section
subject: "[[Topology]]"
chapter: 7
section: 21
munkres: "§69"
tags: [topology, math590]
---
← [[Topology §20 Normal Spaces]] · ↑ [[Topology — 7 Algebraic Foundations]] · [[Topology §22 Homotopy of Paths]] →

## Part II: Algebraic Topology

> [!remark] Remark: The Central Question of Algebraic Topology
> **Q:** Given topological spaces $X$ and $Y$, are $X$ and $Y$ [[Topology §9 Continuous Functions#^def-9-2|homeomorphic]]?
>
> Point-set topology provides some invariants: [[Topology §15 Compact Spaces#^def-15-2|compactness]], [[Topology §13 Connected Spaces#^def-13-1|connectedness]], [[Topology §8 Hausdorff Spaces#^def-8-1|Hausdorff]], etc. These suffice for simple cases:
> - $[0,1] \not\cong (0,1)$: one is compact, the other is not.
> - $\mathbb{R} \not\cong \mathbb{R}^2$: removing a point from $\mathbb{R}$ gives a disconnected space, but $\mathbb{R}^2 \setminus \{p\}$ is still connected.
>
> But these tools are not enough: **is $\mathbb{R}^2 \cong \mathbb{R}^3$?** Both are connected, non-compact, Hausdorff, second-countable, and removing a point from either leaves a connected space. We need a new technique.
>
> The idea: $\mathbb{R}^2 \setminus \{p\}$ has loops that cannot be “shrunk to a point,” while in $\mathbb{R}^3 \setminus \{p\}$ every loop can be contracted. This is captured by the **[[Topology §23 The Fundamental Group#^def-23-2|fundamental group]]** $\pi_1$. The key concept is **[[Topology §23 The Fundamental Group#^def-23-3|simply connected]]**: a space is simply connected if every closed curve can be continuously shrunk to a point.

^rem-II-1

> [!remark] Remark: The Role of the Quotient Space Toolkit in Part II
> Many spaces whose $\pi_1$ we want to compute are built by **gluing**: $S^1 = [0, 2\pi]/(0 \sim 2\pi)$, the torus $T^2 = [0, 2\pi]^2/(\text{opposite edges})$, $S^n = B^n/(\text{collapse boundary})$. To compute $\pi_1$ of these spaces, we repeatedly need to:
> 1. **Build homotopies on a simple space** (a square, an interval, a ball) where geometry is easy — straight lines, rays, linear interpolations all work.
> 2. **Descend them to the quotient space** (a torus, a circle, a sphere) where the topology lives.
>
> Step 2 is where the **[[Universal Property of Quotient Maps|Universal Property of Quotient Maps]]** ([[Universal Property of Quotient Maps|§12.3]]) enters: it guarantees that if a map on the simple space respects the gluing (sends identified points to the same place), then it descends to a well-defined continuous map on the quotient. The [[Topology §12 Quotient Topology#^rem-12-8|Quotient Space Toolkit]] (Theorems A, B, C from [[Topology §12 Quotient Topology|§12]]) will appear in:
> - The **[[Topology §26 Deformation Retracts and Homotopy Type#^lem-26-8|nullhomotopy lemma]]**: $\pi: S^n \times I \to B^{n+1}$ by $\pi(x,t) = (1-t)x$ is a quotient map ([[Topology §12 Quotient Topology#^rem-12-8|Thm A]]); a nullhomotopy $H$ descends to an extension $k: B^{n+1} \to X$ ([[Universal Property of Quotient Maps|Thm C]]).
> - The **[[Topology §24 Covering Spaces#^thm-24-2|covering map]]** $p: \mathbb{R} \to S^1$: the interval $[0, 2\pi]$ quotients to $S^1$ ([[Topology §12 Quotient Topology#^rem-12-8|Thm A]]); the winding number computation uses the fact that $p$ is a quotient map.
> - **$\pi_1(T^2) \cong \mathbb{Z} \times \mathbb{Z}$** ([[Topology §23 The Fundamental Group#^cor-23-8|Corollary §23.8]]): $[0, 2\pi]^2$ quotients to $T^2$ ([[Topology §12 Quotient Topology#^thm-12-5|Thm B]]); deformation retracts on the square descend to the torus ([[Universal Property of Quotient Maps|Thm C]]).
>
> The pattern is always the same: **work upstairs, check the gluing, descend**.

^rem-II-2

*This section is a self-contained review of the group theory needed for algebraic topology. No prior algebra is assumed.*

> [!remark] Remark: Why Groups in Topology?
> The central idea of algebraic topology is to assign algebraic objects (groups) to topological spaces in a way that respects continuous maps. If two spaces are homeomorphic, they get isomorphic groups; if the groups are different, the spaces cannot be homeomorphic. The **[[Topology §23 The Fundamental Group#^def-23-2|fundamental group]]** $\pi_1(X, x_0)$ captures the “loop structure” of a space. To make this precise, we need the language of groups.

^rem-21-1

## Groups

> [!definition] Definition §21.1: Group
> A **group** is a set $G$ together with a binary operation $\cdot\,: G \times G \to G$, $(a, b) \mapsto a \cdot b$, satisfying:
> 1. **Associativity:** $(a \cdot b) \cdot c = a \cdot (b \cdot c)$ for all $a, b, c \in G$.
> 2. **Identity:** There exists $e \in G$ such that $e \cdot g = g \cdot e = g$ for all $g \in G$.
> 3. **Inverses:** For each $g \in G$, there exists $g^{-1} \in G$ such that $g \cdot g^{-1} = g^{-1} \cdot g = e$.
>
> If additionally $a \cdot b = b \cdot a$ for all $a, b \in G$, we say $G$ is **abelian**.

^def-21-1

> [!remark] Remark: Uniqueness of Identity and Inverses
> The identity is unique: if $e$ and $e'$ are both identities, then $e = e \cdot e' = e'$. Inverses are unique: if $g \cdot h = e$ and $g \cdot h' = e$, left-multiplying by $g^{-1}$ gives $h = h'$.

^rem-21-2

> [!example] Example §21.1: Key Examples
> - $(\mathbb{Z}, +)$: integers under addition. Identity: $0$. Inverse of $n$: $-n$. Abelian.
> - $(\mathbb{Z}/n\mathbb{Z}, +)$: integers mod $n$. Elements $\{0, 1, \ldots, n-1\}$ with addition mod $n$. Abelian, $|G| = n$.
> - $(S_n, \circ)$: permutations of $\{1, \ldots, n\}$ under composition. **Not abelian** for $n \geq 3$.
> - The **trivial group**: $G = \{e\}$.

^ex-21-1

## Subgroups

> [!definition] Definition §21.2: Subgroup
> $H \subseteq G$ is a **subgroup** ($H \leq G$) if $H$ is a group under the inherited operation. Equivalently: (1) $e \in H$, (2) $a, b \in H \Rightarrow ab \in H$, (3) $a \in H \Rightarrow a^{-1} \in H$.

^def-21-2

> [!remark]- Connections
> - Linear-algebra analogue: [[Linear Algebra 1C Subspaces#^ladr-1-34|Conditions for a subspace]].

> [!theorem] Proposition §21.1: Properties Inherited by Subgroups
> Let $H \leq G$ be a subgroup. Then:
> 1. If $G$ is abelian, then $H$ is abelian.
> 2. If $G$ is [[Topology §21 Algebra Prerequisites꞉ Groups#^def-21-7|cyclic]], then $H$ is cyclic.
> 3. If $G$ is finite of order $n$, then $|H|$ divides $n$ (Lagrange's theorem).

^prop-21-1

> [!proof]+ Proof
> **(1)** If $a, b \in H$, then $a, b \in G$, so $ab = ba$ (since $G$ is abelian). The same equation holds in $H$.
>
> **(2)** If $G = \langle g \rangle$, every element of $H$ has the form $g^k$ for some $k$. Let $m$ be the smallest positive integer with $g^m \in H$. Then $H = \langle g^m \rangle$ (one can show every element of $H$ is a power of $g^m$ by the division algorithm).
>
> **(3)** Lagrange's theorem — the proof uses cosets and is standard in algebra. We state it without proof.

^pf-21-1

*Uses:* [[Topology §21 Algebra Prerequisites꞉ Groups#^def-21-2|Def. §21.2]], [[Topology §21 Algebra Prerequisites꞉ Groups#^def-21-7|Def. §21.7]]

> [!theorem] Proposition §21.2: Contrapositive: Detecting Non-Abelian Groups
> If $G$ contains a non-abelian subgroup $H$, then $G$ is non-abelian.

^prop-21-2

> [!proof]+ Proof
> This is the contrapositive of [[Topology §21 Algebra Prerequisites꞉ Groups#^prop-21-1|(1) above]]. If $G$ were abelian, then every subgroup $H$ would be abelian (since the operation in $H$ is inherited from $G$). So if $H$ is non-abelian, $G$ cannot be abelian.
>
> Explicitly: there exist $a, b \in H$ with $ab \neq ba$. Since $H \subseteq G$, these same $a, b$ are in $G$ with $ab \neq ba$. So $G$ is non-abelian.

^pf-21-2

*Uses:* [[Topology §21 Algebra Prerequisites꞉ Groups#^prop-21-1|§21.1]]

## Homomorphisms and Isomorphisms

> [!definition] Definition §21.3: Homomorphism
> A map $f: G \to G'$ (both groups) is a **homomorphism** if $f(x \cdot y) = f(x) \cdot f(y)$ for all $x, y \in G$.

^def-21-3

> [!theorem] Theorem §21.3: Homomorphisms Preserve Identity and Inverses
> Let $f: G \to G'$ be a homomorphism. Then:
> 1. $f(e_G) = e_{G'}$.
> 2. $f(a^{-1}) = f(a)^{-1}$ for all $a \in G$.

^thm-21-3

> [!proof]+ Proof
> **(1)** We have $f(e_G) = f(e_G \cdot e_G) = f(e_G) \cdot f(e_G)$. Left-multiplying both sides by $f(e_G)^{-1}$:
>
> $$
> f(e_G)^{-1} \cdot f(e_G) = f(e_G)^{-1} \cdot f(e_G) \cdot f(e_G) \implies e_{G'} = f(e_G).
> $$
>
> **(2)** We have $f(a) \cdot f(a^{-1}) = f(a \cdot a^{-1}) = f(e_G) = e_{G'}$ by (1). Similarly, $f(a^{-1}) \cdot f(a) = f(a^{-1} \cdot a) = e_{G'}$. So $f(a^{-1})$ is both a left and right inverse of $f(a)$. Since [[Topology §21 Algebra Prerequisites꞉ Groups#^rem-21-2|inverses in a group are unique]], $f(a^{-1}) = f(a)^{-1}$.

^pf-21-3

*Uses:* [[Topology §21 Algebra Prerequisites꞉ Groups#^def-21-3|Def. §21.3]]

> [!remark]- Connections
> - Linear-algebra version of (1): [[Linear Algebra 3A Vector Space of Linear Maps#^ladr-3-10|Linear maps take 0 to 0]].

> [!remark] Remark
> Note that only the homomorphism property $f(xy) = f(x)f(y)$ is assumed — preservation of identity and inverses follows automatically. This is why the definition of homomorphism only requires preserving the operation.

^rem-21-3

> [!theorem] Proposition §21.4: Bijectivity via Two-Sided Inverse
> A map $f: A \to B$ is bijective if and only if there exists a map $g: B \to A$ such that $f \circ g = \operatorname{id}_B$ and $g \circ f = \operatorname{id}_A$.
>
> Moreover, each condition alone gives half the result:
> - $g \circ f = \operatorname{id}_A$ alone $\Rightarrow$ $f$ is injective.
> - $f \circ g = \operatorname{id}_B$ alone $\Rightarrow$ $f$ is surjective.

^prop-21-4

> [!proof]+ Proof
> **Injective from $g \circ f = \operatorname{id}_A$:** If $f(x) = f(y)$, apply $g$: $x = g(f(x)) = g(f(y)) = y$.
>
> **Surjective from $f \circ g = \operatorname{id}_B$:** For any $b \in B$, set $a = g(b)$. Then $f(a) = f(g(b)) = b$.
>
> **Both together:** $f$ is injective and surjective, hence bijective. The map $g$ is then the inverse function $f^{-1}$.

^pf-21-4

> [!remark]- Connections
> - Linear-algebra version: [[Linear Algebra 3D Invertibility and Isomorphisms#^ladr-3-63|Invertibility ⟺ injectivity and surjectivity]].

> [!remark] Remark
> This is the standard technique for proving bijectivity in algebraic topology: construct two maps, show they compose to the identity in both orders. It appears repeatedly: the [[Basepoint Independence of π₁|basepoint independence isomorphism]] ([[Topology §23 The Fundamental Group|§23]]), the [[Topology §23 The Fundamental Group#^cor-23-6|functorial corollary that π₁ is a topological invariant]] ([[Topology §23 The Fundamental Group|§23]]), and the [[Deformation Retract Induces Isomorphism on π₁|deformation retract theorem]] ([[Topology §26 Deformation Retracts and Homotopy Type|§26]]) all use exactly this pattern.

^rem-21-4

> [!definition] Definition §21.4: Isomorphism
> A [[Topology §21 Algebra Prerequisites꞉ Groups#^def-21-3|homomorphism]] $f: G \to G'$ is an **isomorphism** if $f$ is bijective. We write $G \cong G'$.

^def-21-4

> [!remark]- Connections
> - Linear-algebra version: [[Linear Algebra 3D Invertibility and Isomorphisms#^ladr-3-69|Isomorphism, isomorphic]].

> [!theorem] Theorem §21.5: Inverse of an Isomorphism is a Homomorphism
> If $f: G \to G'$ is an isomorphism, then $f^{-1}: G' \to G$ is also a homomorphism (and hence an isomorphism).

^thm-21-5

> [!proof]+ Proof
> Let $x', y' \in G'$. Since $f$ is surjective, there exist unique $x, y \in G$ with $f(x) = x'$ and $f(y) = y'$. Then:
>
> $$
> f^{-1}(x' \cdot y') = f^{-1}(f(x) \cdot f(y)) = f^{-1}(f(x \cdot y)) = x \cdot y = f^{-1}(x') \cdot f^{-1}(y')
> $$
>
> where the second equality uses that $f$ is a homomorphism: $f(x) \cdot f(y) = f(x \cdot y)$.

^pf-21-5

*Uses:* [[Topology §21 Algebra Prerequisites꞉ Groups#^def-21-3|Def. §21.3]], [[Topology §21 Algebra Prerequisites꞉ Groups#^def-21-4|Def. §21.4]]

> [!remark] Remark: Contrast with Topology
> In topology, a continuous bijection does *not* automatically have a continuous inverse — this is why [[Topology §9 Continuous Functions#^def-9-2|homeomorphism]] requires both directions, and why the [[Bijection from Compact to Hausdorff is a Homeomorphism|compact-to-Hausdorff theorem]] is needed to get the inverse for free. For groups, bijectivity + forward homomorphism gives the inverse homomorphism for free. So “isomorphism = bijective homomorphism” is a *theorem*, not merely a convention: you only need to check one direction.

^rem-21-5

> [!theorem] Theorem §21.6: Isomorphisms Preserve All Algebraic Properties
> If $f: G \to G'$ is an isomorphism, then $G$ and $G'$ have identical group-theoretic structure. In particular:
> 1. $|G| = |G'|$ (same cardinality).
> 2. $G$ is abelian if and only if $G'$ is abelian.
> 3. $G$ is [[Topology §21 Algebra Prerequisites꞉ Groups#^def-21-7|cyclic]] if and only if $G'$ is cyclic.
> 4. For each $n$, $G$ has an element of order $n$ if and only if $G'$ does.

^thm-21-6

> [!proof]+ Proof
> **(1)** $f$ is a bijection.
>
> **(2)** Suppose $G$ is abelian. For any $x', y' \in G'$, write $x' = f(x)$, $y' = f(y)$. Then $x' \cdot y' = f(x) \cdot f(y) = f(xy) = f(yx) = f(y) \cdot f(x) = y' \cdot x'$. The converse follows by applying the same argument to $f^{-1}$.
>
> **(3)** If $G = \langle a \rangle$, then every element of $G'$ has the form $f(a^n) = f(a)^n$, so $G' = \langle f(a) \rangle$. Converse via $f^{-1}$.
>
> **(4)** If $a \in G$ has order $n$ (i.e., $a^n = e$ and $n$ is minimal), then $f(a)^n = f(a^n) = f(e) = e'$. If $f(a)^k = e'$ for some $k < n$, then $f(a^k) = e'$, so $a^k = e$ (since $f$ is injective), contradicting minimality. So $f(a)$ has order $n$.

^pf-21-6

*Uses:* [[Topology §21 Algebra Prerequisites꞉ Groups#^thm-21-5|§21.5]], [[Topology §21 Algebra Prerequisites꞉ Groups#^thm-21-3|§21.3]], [[Topology §21 Algebra Prerequisites꞉ Groups#^def-21-7|Def. §21.7]]

> [!remark] Remark: Why Isomorphisms Matter
> An isomorphism is a **perfect dictionary** between two groups: you can do all your work in whichever group is more convenient, then translate the answer back. For algebraic topology, this has two consequences:
>
> **Computation:** [[Fundamental Group of the Circle|π₁(S¹) ≅ ℤ]] means that everything about loops on $S^1$ can be answered by doing arithmetic in $\mathbb{Z}$. How many essentially different loops? Countably many, indexed by winding number. What happens when you concatenate a loop of winding number $3$ with one of winding number $-2$? Winding number $1$. The isomorphism converts hard topology into easy algebra.
>
> **Distinguishing spaces:** If $\pi_1(X) \not\cong \pi_1(Y)$ — meaning no isomorphism exists — then the groups have genuinely different structure that no relabeling can reconcile. Since homeomorphisms induce isomorphisms ([[Topology §23 The Fundamental Group#^cor-23-6|Corollary §23.6]]), this forces $X \not\cong Y$. For instance, $\mathbb{Z} \not\cong \{e\}$ (different cardinalities), so $S^1 \not\cong \mathbb{R}^2$. And $\mathbb{Z} \not\cong \mathbb{Z}^2$ (one is cyclic, the other is not), so $S^1 \not\cong T^2$.

^rem-21-6

> [!remark]- Connections
> - The inputs: [[Topology §23 The Fundamental Group#^ex-23-1|ℝⁿ is simply connected]], [[Topology §23 The Fundamental Group#^cor-23-8|Fundamental Group of the Torus]]. More such arguments: [[Topology §24 Covering Spaces#^rem-24-14|How to Establish or Refute Isomorphisms]].

> [!remark] Remark: Analogy: Topology $\leftrightarrow$ Algebra
> | | **Topology** | **Algebra** |
> |---|---|---|
> | Objects | Topological spaces | Groups |
> | Structure-preserving maps | Continuous maps | Homomorphisms |
> | “Same” objects | Homeomorphisms | Isomorphisms |
>
> Algebraic topology connects these: it assigns groups to spaces and homomorphisms to continuous maps.

^rem-21-7

> [!remark]- Connections
> - The assignment on maps: [[Topology §23 The Fundamental Group#^def-23-4|Induced Homomorphism]], with [[Functoriality of π₁|Functoriality of π₁]].

> [!definition] Definition §21.5: Direct Product of Groups
> Let $G$ and $H$ be groups. The **direct product** $G \times H$ is the set of ordered pairs $\{(g, h) : g \in G, h \in H\}$ with the componentwise operation:
>
> $$
> (g_1, h_1) \cdot (g_2, h_2) = (g_1 \cdot g_2, \; h_1 \cdot h_2).
> $$
>
> The identity is $(e_G, e_H)$ and the inverse of $(g, h)$ is $(g^{-1}, h^{-1})$.

^def-21-5

> [!remark]- Connections
> - Linear-algebra version: [[Linear Algebra 3E Products and Quotients of Vector Spaces#^ladr-3-87|Product of vector spaces]].
> - Appears as $\pi_1$ of a product: [[Topology §23 The Fundamental Group#^thm-23-7|π₁ of a Product Space]].

> [!example] Example §21.2
> $\mathbb{Z} \times \mathbb{Z}$ is the group of integer pairs $(m, n)$ with addition $(m_1, n_1) + (m_2, n_2) = (m_1 + m_2, n_1 + n_2)$. Identity is $(0, 0)$, inverse of $(m, n)$ is $(-m, -n)$. This is abelian: $(m_1, n_1) + (m_2, n_2) = (m_2, n_2) + (m_1, n_1)$.

^ex-21-2

> [!theorem] Theorem §21.7: Products of Isomorphic Groups
> If $G \cong G'$ and $H \cong H'$, then $G \times H \cong G' \times H'$.

^thm-21-7

> [!proof]+ Proof
> Let $f: G \to G'$ and $g: H \to H'$ be isomorphisms. The natural candidate is “apply $f$ and $g$ separately”: define
>
> $$
> (f \times g): G \times H \to G' \times H', \qquad (f \times g)(a, b) = (f(a), \; g(b)).
> $$
>
> **Bijective:** The [[Topology §21 Algebra Prerequisites꞉ Groups#^prop-21-4|two-sided inverse]] is $f^{-1} \times g^{-1}: G' \times H' \to G \times H$. Check both compositions:
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

^pf-21-7

*Uses:* [[Topology §21 Algebra Prerequisites꞉ Groups#^prop-21-4|§21.4]], [[Topology §21 Algebra Prerequisites꞉ Groups#^def-21-5|Def. §21.5]]

## Kernel and Image

> [!definition] Definition §21.6: Kernel and Image
> Let $f: G \to G'$ be a homomorphism.
>
> $$
> \ker(f) = \{g \in G \mid f(g) = e_{G'}\}, \qquad \operatorname{im}(f) = \{f(g) \mid g \in G\}.
> $$

^def-21-6

> [!remark]- Connections
> - Linear-algebra versions: [[Linear Algebra 3B Null Spaces and Ranges#^ladr-3-11|Null space, null T]] (the kernel) and [[Linear Algebra 3B Null Spaces and Ranges#^ladr-3-16|Range]] (the image).

> [!theorem] Proposition §21.8
> $\ker(f) \leq G$ and $\operatorname{im}(f) \leq G'$. Moreover, $f$ is injective if and only if $\ker(f) = \{e\}$.

^prop-21-8

> [!proof]+ Proof
> **Kernel is subgroup:** $f(e) = e'$ so $e \in \ker(f)$. If $a, b \in \ker(f)$, then $f(ab^{-1}) = f(a)f(b)^{-1} = e'(e')^{-1} = e'$.
>
> **Image is subgroup:** $e' = f(e) \in \operatorname{im}(f)$. If $f(a), f(b) \in \operatorname{im}(f)$, then $f(a)f(b)^{-1} = f(ab^{-1}) \in \operatorname{im}(f)$.
>
> **Injectivity:** $(\Rightarrow)$: If $f$ injective and $f(g) = e' = f(e)$, then $g = e$. $(\Leftarrow)$: If $f(a) = f(b)$, then $f(ab^{-1}) = e'$, so $ab^{-1} = e$, giving $a = b$.

^pf-21-8

*Uses:* [[Topology §21 Algebra Prerequisites꞉ Groups#^thm-21-3|§21.3]], [[Topology §21 Algebra Prerequisites꞉ Groups#^def-21-2|Def. §21.2]]

> [!remark]- Connections
> - Linear-algebra versions: [[Linear Algebra 3B Null Spaces and Ranges#^ladr-3-13|The null space is a subspace]], [[Linear Algebra 3B Null Spaces and Ranges#^ladr-3-18|The range is a subspace]], [[Linear Algebra 3B Null Spaces and Ranges#^ladr-3-15|Injectivity ⟺ null space equals {0}]].

> [!theorem] Proposition §21.9: Injective Homomorphisms Preserve Subgroup Structure
> Let $f: G \to G'$ be an injective homomorphism. Then:
> 1. $f(G)$ is a subgroup of $G'$ isomorphic to $G$.
> 2. If $G$ is non-abelian, then $f(G)$ is a non-abelian subgroup of $G'$, and hence $G'$ is non-abelian.
> 3. If $G$ is infinite, then $G'$ contains an infinite subgroup, so $G'$ is infinite.

^prop-21-9

> [!proof]+ Proof
> **(1)** $f(G) \leq G'$: $f(e_G) = e_{G'} \in f(G)$; if $f(a), f(b) \in f(G)$, then $f(a)f(b) = f(ab) \in f(G)$; $f(a)^{-1} = f(a^{-1}) \in f(G)$. Since $f$ is injective, $f: G \to f(G)$ is a bijective homomorphism, hence an isomorphism.
>
> **(2)** Since $f: G \to f(G)$ is an isomorphism, $f(G)$ is non-abelian ([[Topology §21 Algebra Prerequisites꞉ Groups#^thm-21-6|isomorphisms preserve abelianness]]). By the contrapositive ([[Topology §21 Algebra Prerequisites꞉ Groups#^prop-21-2|§21.2]]): a group containing a non-abelian subgroup is itself non-abelian. So $G'$ is non-abelian.
>
> **(3)** Since $f$ is injective, $|f(G)| = |G| = \infty$.

^pf-21-9

*Uses:* [[Topology §21 Algebra Prerequisites꞉ Groups#^thm-21-3|§21.3]], [[Topology §21 Algebra Prerequisites꞉ Groups#^def-21-4|Def. §21.4]], [[Topology §21 Algebra Prerequisites꞉ Groups#^thm-21-6|§21.6]], [[Topology §21 Algebra Prerequisites꞉ Groups#^prop-21-2|§21.2]]

> [!theorem] Proposition §21.10: Surjective Homomorphisms Preserve Abelianness
> Let $f: G \to G'$ be a surjective homomorphism. If $G$ is abelian, then $G'$ is abelian.
>
> Equivalently (contrapositive): if $G'$ is non-abelian, then $G$ is non-abelian.

^prop-21-10

> [!proof]+ Proof
> Let $x', y' \in G'$. Since $f$ is surjective, there exist $x, y \in G$ with $f(x) = x'$ and $f(y) = y'$. Then:
>
> $$
> x' \cdot y' = f(x) \cdot f(y) = f(x \cdot y) = f(y \cdot x) = f(y) \cdot f(x) = y' \cdot x',
> $$
>
> where the third equality uses $x \cdot y = y \cdot x$ (since $G$ is abelian). So $G'$ is abelian.

^pf-21-10

> [!remark] Remark: Why This Matters for $\pi_1$: Two Directions from a Retraction
> If $A$ is a [[Topology §26 Deformation Retracts and Homotopy Type#^def-26-1|retract]] of $X$ (with retraction $r$ and inclusion $j$), then $r_* \circ j_* = \operatorname{id}$ on $\pi_1(A)$, giving two [[Topology §23 The Fundamental Group#^def-23-4|induced maps]]:
>
> **$j_*: \pi_1(A) \hookrightarrow \pi_1(X)$ (injective):** Embeds $\pi_1(A)$ as a subgroup of $\pi_1(X)$. Conclusion: $\pi_1(X)$ is *at least as complicated* as $\pi_1(A)$.
>
> **$r_*: \pi_1(X) \twoheadrightarrow \pi_1(A)$ (surjective):** Maps $\pi_1(X)$ onto $\pi_1(A)$. Conclusion: $\pi_1(X)$ *cannot be simpler* than $\pi_1(A)$ (an abelian group can only surject onto abelian groups).
>
> Both directions detect non-abelianness:
> - Via $j_*$: non-abelian $\pi_1(A)$ embeds $\Rightarrow$ non-abelian subgroup $\Rightarrow$ non-abelian $\pi_1(X)$ ([[Topology §21 Algebra Prerequisites꞉ Groups#^prop-21-9|§21.9]]).
> - Via $r_*$: if $\pi_1(X)$ were abelian, $r_*$ surjects onto abelian image $\Rightarrow$ $\pi_1(A)$ abelian, contradiction ([[Topology §21 Algebra Prerequisites꞉ Groups#^prop-21-10|§21.10]]).

^rem-21-8

> [!remark]- Connections
> - Made precise in [[Topology §26 Deformation Retracts and Homotopy Type#^prop-26-3|Algebraic Properties of Retractions]] and [[Topology §26 Deformation Retracts and Homotopy Type#^cor-26-4|What Properties Transfer via Retraction]]; applied in [[Topology §28 Fundamental Group of Some Surfaces#^thm-28-5|π₁(Σ₂) is Non-Abelian]].

## Cyclic Groups and Free Groups

> [!definition] Definition §21.7: Powers and Generators
> Let $G$ be a group and $x \in G$. We define the **powers** of $x$:
> - $x^n = \underbrace{x \cdot x \cdots x}_{n}$ for $n > 0$ (the $n$-fold product of $x$ with itself),
> - $x^0 = e$ (the identity element),
> - $x^{-n} = \underbrace{x^{-1} \cdot x^{-1} \cdots x^{-1}}_{n}$ for $n > 0$.
>
> If the set $\{x^m \mid m \in \mathbb{Z}\}$ equals all of $G$, then $G$ is called a **cyclic group** and $x$ is called a **generator** of $G$. We write $G = \langle x \rangle$.

^def-21-7

> [!remark] Remark
> Every cyclic group is isomorphic to either $\mathbb{Z}$ (infinite cyclic) or $\mathbb{Z}/n\mathbb{Z}$ (cyclic of order $n$).
>
> **Infinite cyclic:** $G = \langle x \rangle \cong \mathbb{Z}$, where $x^m = x^n$ only if $m = n$. The elements $\ldots, x^{-2}, x^{-1}, e, x, x^2, \ldots$ are all distinct.
>
> **Finite cyclic of order $n$:** $G = \langle x \mid x^n = e \rangle \cong \mathbb{Z}/n\mathbb{Z}$. The relation $x^n = e$ forces everything to wrap around: $x^n = e$, $x^{n+1} = x$, $x^{-1} = x^{n-1}$. Exactly $n$ distinct elements: $\{e, x, x^2, \ldots, x^{n-1}\}$.
>
> **Why $\mathbb{Z}$ is “free on one generator”:** If $G = \langle x \rangle \cong \mathbb{Z}$ and $H$ is *any* group with an element $h \in H$, there is a unique homomorphism $\varphi: G \to H$ with $\varphi(x) = h$, defined by $\varphi(x^n) = h^n$. This is well-defined because there are no relations to check — the only constraint is $x \cdot x^{-1} = e$, and $h \cdot h^{-1} = e$ holds automatically in any group. You can map the generator *anywhere*, no questions asked.

^rem-21-9

> [!remark]- Connections
> - Linear-algebra analogue of “map the generator anywhere”: [[Linear map lemma]].

> [!definition] Definition §21.8: Free Group
> The **free group** $F_n$ on generators $\{a_1, \ldots, a_n\}$ consists of all **reduced words** in the symbols $a_i$ and $a_i^{-1}$. A **word** is a finite sequence like $a_1^2 a_3^{-1} a_2 a_1^{-1}$. A word is **reduced** if no adjacent pair cancels (no $a_i a_i^{-1}$ or $a_i^{-1} a_i$ appears). The group operation is concatenation followed by reduction, the identity is the empty word $\varepsilon$, and the inverse of $s_1 \cdots s_k$ is $s_k^{-1} \cdots s_1^{-1}$.
>
> “Free” means **no relations** between generators other than $a_i a_i^{-1} = e$. In particular, $F_1 \cong \mathbb{Z}$ (one generator, no relations — just powers $a^n$). For $F_2 = \langle a, b \rangle$: $ab \neq ba$ (the group is non-abelian), and every different-looking reduced word is a different element.

^def-21-8

> [!remark]- Connections
> - Formal version: [[Topology §21 Algebra Prerequisites꞉ Groups#^def-21-10|Free Group on Elements]]. $F_n$ is $\pi_1$ of a wedge of $n$ circles: [[Topology §29 The Seifert–van Kampen Theorem#^ex-29-3|Example §29.3]].

> [!example] Example §21.3: Multiplication in $F_2$
> The operation is “concatenate, then cancel adjacent inverse pairs until reduced”:
> 1. $(ab^{-1}) \cdot (ba) = ab^{-1}ba$. The $b^{-1}$ and $b$ cancel: $\to a \cdot a = a^2$.
> 2. $(ab) \cdot (b^{-1}a^{-1}) = abb^{-1}a^{-1} \to aa^{-1} \to \varepsilon$. Cascading cancellation; confirms $(ab)^{-1} = b^{-1}a^{-1}$.
> 3. $(aba) \cdot (a^{-1}b) = abaa^{-1}b \to ab^2$. Only the inner $a, a^{-1}$ pair cancels.
> 4. $(ab^{-1}) \cdot (ba^{-1}) = ab^{-1}ba^{-1} \to aa^{-1} \to \varepsilon$. Two rounds of cancellation.
> 5. $ab \cdot ba = abba = ab^2a$. No cancellation at all — $b$ and $b$ are from the same generator, so they combine to $b^2$.
>
> **What “no relations” really means:** Two reduced words are equal if and only if they are literally the same string. In particular: $ab \neq ba$ (different strings, both reduced), $aba^{-1}b^{-1} \neq \varepsilon$ (already reduced, no adjacent pair cancels), $a^2b^3 \neq b^3a^2$ (different strings). Compare with $\mathbb{Z} \times \mathbb{Z}$: there the relation $ab = ba$ lets you rearrange any word into $a^m b^n$. In $F_2$, order is permanent.

^ex-21-3

> [!definition] Definition §21.9: Free Product of Groups
> Let $G$ and $H$ be groups. The **free product** $G * H$ is the group whose elements are **reduced words** — finite alternating sequences of nontrivial elements from $G$ and $H$:
>
> $$
> g_1 h_1 g_2 h_2 \cdots \qquad \text{or} \qquad h_1 g_1 h_2 g_2 \cdots
> $$
>
> where each $g_i \in G \setminus \{e_G\}$ and each $h_i \in H \setminus \{e_H\}$. “Reduced” means no adjacent elements come from the same group (if they did, multiply them using that group's operation).
>
> The group operation is **concatenation followed by reduction**:
>
> $$
> (a_1 \cdots a_n) * (b_1 \cdots b_m) = a_1 \cdots a_n b_1 \cdots b_m \quad \text{(then reduce if $a_n$ and $b_1$ are in the same group)}.
> $$
>
> The identity is the empty word. The inverse of $a_1 \cdots a_n$ is $a_n^{-1} \cdots a_1^{-1}$.

^def-21-9

> [!remark]- Connections
> - Where free products arise as $\pi_1$: [[Topology §29 The Seifert–van Kampen Theorem#^cor-29-2|Free Product Formula]].

> [!example] Example §21.4: $\mathbb{Z} * \mathbb{Z} \cong F_2$
> Let $G = \mathbb{Z} = \{a^n \mid n \in \mathbb{Z}\}$ and $H = \mathbb{Z} = \{b^m \mid m \in \mathbb{Z}\}$. Then $G * H$ consists of all reduced words in powers of $a$ and powers of $b$:
>
> $$
> \mathbb{Z} * \mathbb{Z} = \{a^{n_1} b^{m_1} a^{n_2} b^{m_2} \cdots a^{n_j} b^{m_j} \mid n_i, m_i \in \mathbb{Z} \setminus \{0\} \text{ (except possibly first/last)}\}.
> $$
>
> This is exactly $F_2$: reduced words in $a, a^{-1}, b, b^{-1}$.
>
> **Not abelian:** $a * b \neq b * a$ (both are already reduced, and they are different words).
>
> **Compare with $\mathbb{Z} \times \mathbb{Z}$:** In the direct product, $a^{n_1}b^{m_1}a^{n_2}b^{m_2} = a^{n_1+n_2}b^{m_1+m_2}$ (rearrange using commutativity). In the free product, you *cannot* rearrange — order matters.

^ex-21-4

![[m590-21-1.svg]]
*Why order is permanent in $F_2$ but not in $\mathbb{Z} \times \mathbb{Z}$. In both pictures the vertices are group elements and an edge joins $w$ to $wa$ (blue) or to $wb$ (red). From the identity, the words $ab$ and $ba$ (gray paths) end at *different* vertices of the tree for $F_2$: a tree has no cycles, so each reduced word is its own path and no relation closes the square. In the grid for $\mathbb{Z} \times \mathbb{Z}$ the relation $ab = ba$ closes every square, and both words land on the same vertex.*

> [!remark]- Connections
> - Realized as $\pi_1$ of the figure eight: [[Topology §29 The Seifert–van Kampen Theorem#^ex-29-2|Example §29.2]].

> [!example] Example §21.5: Multiplication in $\mathbb{Z}/2\mathbb{Z} * \mathbb{Z}/3\mathbb{Z}$
> Let $G = \langle a \mid a^2 = e \rangle$ and $H = \langle b \mid b^3 = e \rangle$. The nontrivial elements of $G$: just $a$ (since $a^2 = e$, $a = a^{-1}$). The nontrivial elements of $H$: $b$ and $b^2$ (since $b^3 = e$, $b^{-1} = b^2$). Some multiplications:
> 1. $a \cdot a = a^2 = e_G$. Both from $G$, so multiply in $G$: cancels to $\varepsilon$.
> 2. $b \cdot b = b^2$. Both from $H$, multiply in $H$: stays as $b^2$.
> 3. $a \cdot b = ab$. Different groups, no simplification.
> 4. $ab \cdot ab = abab$. No adjacent pair from same group. Result: $abab$.
> 5. $(aba) \cdot (ab^2) = abaab^2$. The two $a$'s are adjacent, both from $G$: $a \cdot a = e$, delete. Left with $ab \cdot b^2 = ab^3$. Now $b^3 = e_H$, so $ab^3 = a$. **Two rounds of cascading cancellation.**
>
> This group is infinite — alternating strings $ababab\cdots$ of any length are all distinct — even though both factors are finite ($|G| = 2$, $|H| = 3$). Compare with $G \times H = \mathbb{Z}/2 \times \mathbb{Z}/3 \cong \mathbb{Z}/6$, which has only $6$ elements.

^ex-21-5

> [!remark] Remark: Direct Product vs Free Product
> | | **Direct Product $G \times H$** | **Free Product $G * H$** |
> |---|---|---|
> | Elements | Pairs $(g, h)$ | Reduced alternating words |
> | Relation | $G$ and $H$ commute: $(g, e)(e, h) = (e, h)(g, e)$ | No relation between $G$ and $H$ |
> | Size | $\vert G\vert \cdot \vert H\vert$ | Much larger (usually infinite) |
> | Abelian? | Yes if $G, H$ abelian | Almost never |
> | $\pi_1$ of | Product spaces ($X \times Y$) | Wedge sums ($X \vee Y$, via van Kampen) |
>
> The free product is the “most general” way to combine two groups: no relations imposed. The direct product forces commutativity between the factors. Every other way of combining $G$ and $H$ is a quotient of $G * H$ (impose relations to get a smaller group).

^rem-21-10

> [!remark]- Connections
> - The last row: [[Topology §23 The Fundamental Group#^thm-23-7|π₁ of a Product Space]]; [[Topology §28 Fundamental Group of Some Surfaces#^def-28-3|Wedge Sum]] with the [[Topology §29 The Seifert–van Kampen Theorem#^cor-29-2|Free Product Formula]].

> [!remark] Remark: Groups in Algebraic Topology
> | **Group** | **Description** | **Appears as $\pi_1$ of** |
> |---|---|---|
> | $\{e\}$ | Trivial | Simply connected spaces ($\mathbb{R}^n$, $S^n$ for $n \geq 2$) |
> | $\mathbb{Z}$ | Infinite cyclic | $S^1$, cylinder, Möbius band |
> | $\mathbb{Z}/n\mathbb{Z}$ | Finite cyclic | Lens spaces, $P^n$ ($n \geq 2$) |
> | $\mathbb{Z}^n$ | Free abelian (direct product) | Torus $T^n = (S^1)^n$ |
> | $F_n \cong \mathbb{Z} * \cdots * \mathbb{Z}$ | Free on $n$ generators (free product) | Wedge of $n$ circles |

^rem-21-11

> [!remark]- Connections
> - Trivial: [[Topology §23 The Fundamental Group#^ex-23-1|ℝⁿ is Simply Connected]], [[Sⁿ is Simply Connected for n ≥ 2|Sⁿ is Simply Connected for n ≥ 2]]. Infinite cyclic: [[Fundamental Group of the Circle|π₁(S¹) ≅ ℤ]].
> - Finite cyclic: [[Topology §28 Fundamental Group of Some Surfaces#^thm-28-3|π₁(Pⁿ) for all n]]. Free abelian: [[Topology §23 The Fundamental Group#^cor-23-8|Fundamental Group of the Torus]]. Free: [[Topology §29 The Seifert–van Kampen Theorem#^ex-29-3|Example §29.3]].

> [!remark] Remark: The Hierarchy of Relations
> $$
> \underbrace{\mathbb{Z}/n\mathbb{Z}}_{\text{one gen, one rel}} \;\longleftarrow\; \underbrace{\mathbb{Z} \cong F_1}_{\text{one gen, no rel}} \;\longleftarrow\; \underbrace{F_n = \mathbb{Z} * \cdots * \mathbb{Z}}_{\text{$n$ gen, no rel}} \;\overset{\text{add rels $ab = ba$}}{\longrightarrow}\; \underbrace{\mathbb{Z}^n}_{\text{$n$ gen, all commute}}
> $$
>
> Each arrow represents adding a relation, which makes the group smaller. The free group $F_n$ is the largest group on $n$ generators — every other group with $\leq n$ generators is a quotient of it. In particular:
>
> $$
> G \times H = (G * H) / \langle ghg^{-1}h^{-1} \mid g \in G, h \in H \rangle.
> $$
>
> You start with the free product (no relations between factors) and impose commutativity. This shrinks the group whenever both factors are nontrivial: $F_2$ is non-abelian, while $\mathbb{Z}^2$ is abelian, so the quotient map $F_2 \to \mathbb{Z}^2$ sends the nontrivial element $aba^{-1}b^{-1}$ to the identity. Adding relations kills elements.

^rem-21-12

## Group Presentations

> [!definition] Definition §21.10: Free Group on Elements
> Let $\{a_\alpha\}_{\alpha \in J}$ be an arbitrary indexed family. For each $\alpha$, let $G_\alpha = \{a_\alpha^n \mid n \in \mathbb{Z}\} \cong \mathbb{Z}$. The [[Topology §21 Algebra Prerequisites꞉ Groups#^def-21-9|free product]] $*_{\alpha \in J}\, G_\alpha$ is called the **free group on the elements** $\{a_\alpha\}$, and $\{a_\alpha\}$ is called a **system of free generators**.

^def-21-10

> [!definition] Definition §21.11: Group Presentation
> Let $G$ be a group with a family of generators $\{a_\alpha\}_{\alpha \in J}$. Let $F$ be the [[Topology §21 Algebra Prerequisites꞉ Groups#^def-21-10|free group]] on $\{a_\alpha\}$. Then there exists a surjective homomorphism $h: F \to G$ with $h(a_\alpha) = a_\alpha$.
>
> Let $N = \ker(h)$, which is a [[Topology §21 Algebra Prerequisites꞉ Groups#^def-21-12|normal subgroup]] of $F$. Then $F/N \cong G$ (by the [[First isomorphism theorem|first isomorphism theorem]]). Each element of $N$ is called a **relation** on $F$.
>
> If $\{r_\beta\}_{\beta \in I}$ is a set of elements of $F$ such that $\{r_\beta\}$ and their conjugates generate $N$, then $\{r_\beta\}$ is called a **complete set of relations** for $G$.
>
> A **presentation** for $G$ is denoted
>
> $$
> G \cong \langle\, a_\alpha \mid r_\beta \,\rangle
> $$
>
> consisting of a family of generators $\{a_\alpha\}$ and a complete set of relations $\{r_\beta\}$.

^def-21-11

> [!remark]- Connections
> - Vector-space version of the first isomorphism theorem: [[First isomorphism theorem]] (with [[Linear Algebra 3E Products and Quotients of Vector Spaces#^ladr-3-99|Quotient space, V∕U]]).
> - Why $\ker(h)$ is normal: [[Topology §21 Algebra Prerequisites꞉ Groups#^rem-21-17|Remark after Definition §21.12]]; the quotient $F/N$: [[Topology §21 Algebra Prerequisites꞉ Groups#^def-21-13|Cosets and Quotient Group]].

> [!remark] Remark: Reading the $\langle \mid \rangle$ Notation
> The bar $\mid$ separates *what you have* (generators) from *what you force* (relations). Building up:
> - $\langle a \rangle$ = the group generated by $a$ = all powers $\{\ldots, a^{-2}, a^{-1}, e, a, a^2, \ldots\}$. With no relations, this is $\mathbb{Z}$.
> - $\langle a, b \rangle$ = the group generated by $a$ and $b$ = all reduced words in $a, b$. With no relations, this is $F_2 = \mathbb{Z} * \mathbb{Z}$.
> - $\langle a \mid a^n \rangle$ = $\langle a \rangle$ with $a^n$ forced to $e$. Only $\{e, a, \ldots, a^{n-1}\}$ survive. This is $\mathbb{Z}/n\mathbb{Z}$.
> - $\langle a, b \mid aba^{-1}b^{-1} \rangle$ = $\langle a, b \rangle$ with $ab = ba$ forced. Every word simplifies to $a^m b^n$. This is $\mathbb{Z} \times \mathbb{Z}$.
>
> Formally: $\langle a_1, \ldots, a_k \mid r_1, \ldots, r_m \rangle = F_k / \langle\!\langle r_1, \ldots, r_m \rangle\!\rangle$ where $F_k$ is the free group and $\langle\!\langle \cdot \rangle\!\rangle$ denotes the normal closure (smallest normal subgroup containing $r_1, \ldots, r_m$).

^rem-21-13

> [!example] Example §21.6: Standard Presentations
> 1. $\langle\, a \mid \emptyset\,\rangle = \langle\, a \,\rangle \cong \mathbb{Z}$. One generator, no relations: the free group on one element.
> 2. $\langle\, a, b \mid \emptyset\,\rangle \cong \mathbb{Z} * \mathbb{Z} = F_2$. Two generators, no relations: the free group on two elements. Elements are reduced words like $a^2 b^{-1} a b^3$.
> 3. $\langle\, a \mid a^n \,\rangle \cong \mathbb{Z}/n\mathbb{Z}$. One generator, one relation $a^n = e$: the cyclic group of order $n$.
> 4. $\langle\, a, b \mid aba^{-1}b^{-1} \,\rangle \cong \mathbb{Z} \times \mathbb{Z}$. Two generators, one relation $ab = ba$: the free *abelian* group on two generators. This is $F_2$ with commutativity forced.
> 5. $\langle\, a, b \mid a^3, b^4 \,\rangle \cong \mathbb{Z}/3\mathbb{Z} * \mathbb{Z}/4\mathbb{Z}$. Two generators, each constrained independently: free product.

^ex-21-6

> [!remark] Remark: Simplifying Presentations
> Three techniques for reducing $\langle \text{generators} \mid \text{relations} \rangle$:
>
> **1. Elimination.** If a relation lets you solve for one generator in terms of others (e.g., $a = \text{word in } b$), substitute everywhere and eliminate that generator. This reduces the number of generators.
>
> *Example:* $\langle a, b \mid aba^{-1}b^{-1}, a \rangle$. The relation $a = e$ lets us substitute $a = e$ everywhere. The other relation becomes $ebe^{-1}b^{-1} = bb^{-1} = e$ (automatic). Result: $\langle b \rangle \cong \mathbb{Z}$.
>
> **2. Splitting.** If each relation involves only one generator, the group splits as a free product: $\langle a, b \mid r(a), s(b) \rangle \cong \langle a \mid r(a) \rangle * \langle b \mid s(b) \rangle$.
>
> *Example:* $\langle a, b \mid b^4 \rangle$. The relation constrains only $b$; $a$ is free. So $\langle a \rangle * \langle b \mid b^4 \rangle \cong \mathbb{Z} * \mathbb{Z}/4\mathbb{Z}$.
>
> **3. Abelianization.** If the relation forces all generators to commute (contains $a_i a_j a_i^{-1} a_j^{-1}$ for all pairs $i, j$), the free product becomes a direct product.
>
> *Example:* $\langle a, b \mid aba^{-1}b^{-1} \rangle$. The relation $ab = ba$ turns $F_2$ into $\mathbb{Z} \times \mathbb{Z}$.

^rem-21-14

> [!remark] Remark: Connection to Van Kampen
> The [[Seifert–van Kampen Theorem|Seifert-van Kampen theorem]] ([[Topology §29 The Seifert–van Kampen Theorem|§29]]) outputs a group as $(G * H)/N$. The $\langle \mid \rangle$ notation makes this concrete. If $G = \langle a_1, \ldots \mid R_1, \ldots \rangle$ and $H = \langle b_1, \ldots \mid S_1, \ldots \rangle$, then:
> - **Free product** (pool generators, keep existing relations, no new ones):
>
>   $$
>   G * H = \langle a_1, \ldots, b_1, \ldots \mid R_1, \ldots, S_1, \ldots \rangle.
>   $$
>
> - **Quotient by $N$** (add new relations from $A \cap B$):
>
>   $$
>   (G * H)/N = \langle a_1, \ldots, b_1, \ldots \mid R_1, \ldots, S_1, \ldots, \underbrace{i_1(t_1) \cdot i_2(t_1)^{-1}, \ldots}_{\text{new: force } i_1(t) = i_2(t)} \rangle.
>   $$
>
> So $(G * H)/N$ means: take the free product (maximum freedom between $G$ and $H$), then add relations that identify loops in $A \cap B$ as seen from both sides. The recipe for computing $i_1(t)$ and $i_2(t)$ — tracing loops through $A$ and $B$ — is the [[Topology §29 The Seifert–van Kampen Theorem#^rem-29-4|geometric step]] in [[Topology §29 The Seifert–van Kampen Theorem|§29]].

^rem-21-15

## Normal Subgroups and Quotient Groups

The notation $\langle a, b \mid r \rangle$ means “force $r = e$.” But what does “force” mean rigorously? Quotient groups are the answer — they are the machinery that makes presentations well-defined.

> [!remark] Remark: The Problem Presentations Solve
> When we write $\langle a, b \mid a^3 \rangle$ and say “force $a^3 = e$, simplify words using this rule,” we are implicitly claiming: (1) the result is a group, (2) the operation is well-defined (simplifying in different orders gives the same answer), and (3) we know which words are “the same.” Quotient groups provide the rigorous foundation for all three claims.

^rem-21-16

> [!definition] Definition §21.12: Normal Subgroup
> $N \leq G$ is **normal** ($N \trianglelefteq G$) if $gng^{-1} \in N$ for all $g \in G$, $n \in N$. Equivalently: conjugating any element of $N$ by anything in $G$ stays in $N$.

^def-21-12

> [!remark] Remark
> Every subgroup of an abelian group is normal ($gng^{-1} = n \in N$, since conjugation does nothing). The [[Topology §21 Algebra Prerequisites꞉ Groups#^def-21-6|kernel]] of any homomorphism is always normal: if $f(n) = e$, then $f(gng^{-1}) = f(g) \cdot e \cdot f(g)^{-1} = e$, so $gng^{-1} \in \ker(f)$.

^rem-21-17

> [!definition] Definition §21.13: Cosets and Quotient Group
> The **left coset** of $N$ by $g$ is $gN = \{gn \mid n \in N\}$. If $N \trianglelefteq G$, the **quotient group** $G/N = \{gN \mid g \in G\}$ with operation $(gN)(hN) = (gh)N$. The canonical map $p: G \to G/N$, $x \mapsto xN$, is a surjective homomorphism with $\ker(p) = N$.

^def-21-13

> [!remark]- Connections
> - Linear-algebra versions: cosets ↔ [[Linear Algebra 3E Products and Quotients of Vector Spaces#^ladr-3-97|Translate]], $G/N$ ↔ [[Linear Algebra 3E Products and Quotients of Vector Spaces#^ladr-3-99|Quotient space, V∕U]], $p$ ↔ [[Linear Algebra 3E Products and Quotients of Vector Spaces#^ladr-3-104|Quotient map, π]].
> - Topological version: [[Topology §12 Quotient Topology#^def-12-3|Quotient Space]].

> [!remark] Remark: What the Slash Means
> $G/N$ means: take $G$, declare everything in $N$ to be the identity, see what's left. Two elements $g, h \in G$ become “the same” in $G/N$ if they differ by something in $N$ — i.e., $g^{-1}h \in N$. The slash is literally division: you divide $G$ into groups of equivalent elements (cosets). Each coset $gN$ is one element of $G/N$. The elements of $N$ itself all collapse to the identity coset $eN = N$.
>
> The notation is consistent across mathematics:
>
> | **Context** | **Notation** | **Meaning** |
> |---|---|---|
> | Integers | $\mathbb{Z}/n\mathbb{Z}$ | Force multiples of $n$ to $0$ (mod $n$) |
> | Groups | $G/N$ | Force $N = e$ (collapse a subgroup) |
> | Topology | $X/{\sim}$ | Force $x \sim y$ (glue points together) |
>
> Same idea everywhere: identify things, see what remains.

^rem-21-18

> [!remark] Remark: Why Normality is Required
> The operation on $G/N$ is $(gN)(hN) = (gh)N$: multiply representatives, take the coset of the result. This requires **well-definedness**: if we pick different representatives $g' \in gN$ and $h' \in hN$, we need $(g'h')N = (gh)N$.
>
> Suppose $g' = gn_1$ and $h' = hn_2$ for some $n_1, n_2 \in N$. Then:
>
> $$
> g'h' = gn_1 \cdot hn_2 = g \cdot (n_1 h) \cdot n_2 = g \cdot h \cdot \underbrace{(h^{-1} n_1 h)}_{\in N?} \cdot n_2.
> $$
>
> We need $h^{-1}n_1 h \in N$, i.e., conjugation by any $h \in G$ must send $N$ back into $N$. This is exactly the **normality** condition $gNg^{-1} \subseteq N$. If $N$ is not normal, the “multiplication” gives different answers depending on which representative you pick — not a well-defined operation, not a group.
>
> For abelian groups (like $\mathbb{Z}$), every subgroup is automatically normal ($gng^{-1} = n$), so this is never an issue. For non-abelian groups, you must check.

^rem-21-19

> [!example] Example §21.7: $\mathbb{Z}/n\mathbb{Z}$
> $n\mathbb{Z} \trianglelefteq \mathbb{Z}$ (normal since $\mathbb{Z}$ abelian). Force all multiples of $n$ to equal $0$: then $n = 0$, so $n+1 = 1$, $n+2 = 2$, $2n = 0$, etc. Everything wraps around. Only $n$ distinct elements survive: $\{[0], [1], \ldots, [n-1]\}$ with addition mod $n$.
>
> *Concrete case $n = 3$:* Start with $\mathbb{Z} = \{\ldots, -3, -2, -1, 0, 1, 2, 3, 4, 5, \ldots\}$. Force $3\mathbb{Z} = \{\ldots, -6, -3, 0, 3, 6, 9, \ldots\}$ to equal $0$. Since $3 = 0$: $4 = 3+1 = 1$, $5 = 3+2 = 2$, $7 = 6+1 = 1$, $-1 = -3+2 = 2$. Every integer collapses to its remainder mod $3$. Result: $\mathbb{Z}/3\mathbb{Z} = \{[0], [1], [2]\}$ with $[2] + [1] = [0]$.

^ex-21-7

> [!example] Example §21.8: Forcing Commutativity
> Start with $F_2 = \langle a, b \rangle$ (all words in $a, b$, no simplification). Force $aba^{-1}b^{-1} = e$, i.e., $ab = ba$. Now every word reduces to $a^m b^n$: for instance, $bab^{-1} = a$, $a^2ba^{-1} = ab$, $baba = a^2b^2$. Result: $\mathbb{Z} \times \mathbb{Z}$.

^ex-21-8

> [!remark] Remark: How Quotient Groups Make Presentations Rigorous
> The presentation $\langle a_1, \ldots, a_k \mid r_1, \ldots, r_m \rangle$ is formally defined as $F_k / \langle\!\langle r_1, \ldots, r_m \rangle\!\rangle$:
> 1. Start with the free group $F_k = \langle a_1, \ldots, a_k \rangle$ — all reduced words, no relations.
> 2. “Force $r_j = e$” means: declare two words $u, v$ to be the same whenever they differ by insertions/deletions of $r_j$ and its conjugates $gr_jg^{-1}$. (Why conjugates? If $r = e$, then $grg^{-1} = geg^{-1} = e$ too — logical consequence.)
> 3. The set of all words that become trivial forms $N = \langle\!\langle r_1, \ldots, r_m \rangle\!\rangle$ — the **normal closure**, the smallest normal subgroup containing all the $r_j$.
> 4. The resulting group is $F_k / N$: the free group modulo the relations.
>
> You do not need quotient groups to *use* presentations — “force $r = e$, simplify words” gives correct answers. The quotient group is the proof that this process is well-defined and gives a group.

^rem-21-20
