---
type: section
subject: "[[Group Theory]]"
chapter: 6
section: 23
tags: [group-theory, math493]
---
← [[§22 Equivalence Relations and Partitions]] · ↑ [[· 6 Group Actions, Cosets, and Lagrange's Theorem]] · [[§24 Stabilizers and Fixed Points]] →

*Reference: Pinter Ch. 13, Ex. J (group acting on a set); Ch. 9 (Cayley's theorem).*

## Definition and Examples

> [!remark] Remark: Motivation
> Groups arise as sets of maps $X \to X$ preserving some structure on $X$, with group multiplication corresponding to composition. An *action* reverses the viewpoint: starting from an abstract group $G$, it specifies how each element of $G$ is to move the points of a set $X$, compatibly with multiplication.

^rem-23-1

> [!definition] Definition §23.1: Action; Right Action
> Let $G$ be a group and let $X$ be a set. An **action** of $G$ on $X$ is a map $\star: G \times X \to X$ obeying
>
> $$
> (g_1 \star g_2) \star x = g_1 \star (g_2 \star x) \quad\text{and}\quad e \star x = x \qquad \text{for all } g_1, g_2 \in G,\ x \in X,
> $$
>
> where on the left of the first identity $g_1 \star g_2$ is the product in $G$. Depending on context, $\star$ may be written $\ast$, $\times$, $\cdot$, or omitted. This is also called a **left action**; a **right action** is a map $X \times G \to X$ obeying $x \star (g_2 \star g_1) = (x \star g_2) \star g_1$ (and $x \star e = x$).
>
> *Source: WS 4*

^def-23-1

> [!remark]- Connections
> - Same definition in 591, [[§12 Group Actions and Orbit Spaces#^def-12-1|591 Def. §12.1]]; for a topological group acting on a space one also asks that the action map be continuous, [[§12 Group Actions and Orbit Spaces#^def-12-2|591 Def. §12.2]].

> [!definition] Definition §23.2: Arrow Notation
> - $f: X \to Y$ denotes a **function** from the set $X$ to the set $Y$; the arrow $\to$ goes between *sets*.
> - $x \mapsto y$ records that the *element* $x$ is sent to the element $y$; e.g. $f: \mathbb{Z} \to \mathbb{Z}$, $n \mapsto n^2$.
> - $G \curvearrowright X$ denotes a **left action** of the group $G$ on the set $X$, and $X \curvearrowleft G$ a **right action**; the group is written on the side from which it acts, as in the [[§25 Orbits#^def-25-2|orbit spaces]] $G \backslash X$ and $X/G$.
>
> The three are not interchangeable. In particular an action is not a function $G \to X$, which would send group elements to points; it is a function $G \times X \to X$, or equivalently a homomorphism $G \to S_X$ (Actions Are Homomorphisms to $S_X$, [[§23 Actions#^thm-23-3|below]]).
>
> *Source: lecture*

^def-23-2

> [!remark] Remark: Reading the Axiom
> The first axiom says that “multiply in $G$, then act” equals “act by $g_2$, then act by $g_1$”: the group product becomes composition of the maps $x \mapsto g \star x$. It has the shape of associativity, and for $G$ acting on itself by multiplication it *is* associativity. In a right action the factors act in the written order, $g_2$ first.

^rem-23-2

> [!example] Example §23.1: Why $e \star x = x$ Must Be an Axiom
> The first axiom does not imply the second. Let $G = \{e\}$ be the trivial group and $X = \{0, 1\}$, and set $e \star 0 = 0$, $e \star 1 = 0$. Then $e \star (e \star x) = 0 = (e \star e) \star x$ for both $x$, so the compatibility axiom holds; but $e \star 1 = 0 \neq 1$, so $e$ does not act as the identity. Such a map is a *monoid action* but not a group action: the second axiom is genuinely independent and must be imposed. (The map $x \mapsto e \star x$ here is idempotent, $\hat e^2 = \hat e$, rather than the identity.)
>
> *Source: lecture*

^ex-23-1

> [!example] Example §23.2: Actions
> 1. $S_X$ acts on $X$ by $\sigma \star x = \sigma(x)$; the axioms are $(\sigma\tau)(x) = \sigma(\tau(x))$ and $\operatorname{id}(x) = x$.
> 2. $G = \mathbb{R}^\times$ acts on any real vector space $V$ by scalar multiplication, $c \star v = cv$: $c_1(c_2 v) = (c_1 c_2)v$ and $1 v = v$.
> 3. $GL_n(k)$ acts on $k^n$ by $A \star v = Av$: associativity of matrix multiplication and $I v = v$.
> 4. $S_n$ acts on $k^n$ by $\sigma \star v = M(\sigma) v$, and on $k[x_1, \ldots, x_n]$ by permuting variables ([[§19 Polynomial Rings, Permutation Matrices, and Representations#^def-19-3|§19]]); the [[§19 Polynomial Rings, Permutation Matrices, and Representations#^prop-19-1|compatibility proved there]] is the first axiom.
> 5. Every group acts on itself by **left multiplication**, $g \star x = gx$ (the axioms are associativity and $ex = x$), and by **conjugation**, $g \star x = gxg^{-1}$ (the axiom is $c_g \circ c_h = c_{gh}$, [[§18 Conjugation, Products, and Pointwise Products#^prop-18-1|§18.1]]).
> 6. The **trivial action**: $g \star x = x$ for all $g, x$.

^ex-23-2

> [!remark]- Connections
> - The vector-space axioms behind (2): [[§2 Definition of Vector Space#^ladr-1-20|LADR 1.20]]; associativity of matrix multiplication behind (3): [[§7 Vector Space of Linear Maps#^ladr-3-8|LADR 3.8]], [[§9 Matrices#^ladr-3-43|LADR 3.43]].
> - The conjugation action is studied in [[§32 Conjugation as an Action and the Class Equation#^prop-32-1|The Conjugation Action]]; left multiplication gives [[§23 Actions#^thm-23-5|Cayley's Theorem]].

> [!theorem] Proposition §23.1: A Left Action Gives a Right Action
> Let $G \times X \to X$, $(g, x) \mapsto gx$, be a left action. Then $X \times G \to X$, $(x, g) \mapsto g^{-1}x$, is a right action.
>
> *Source: WS 4.1*

^prop-23-1

> [!proof]+ Proof
> Write $x \star g := g^{-1}x$. Then $x \star e = e^{-1}x = ex = x$, and
>
> $$
> (x \star g_2) \star g_1 = g_1^{-1}(g_2^{-1} x) = (g_1^{-1}g_2^{-1})x = (g_2 g_1)^{-1} x = x \star (g_2 g_1),
> $$
>
> using the left-action axiom and $(g_2g_1)^{-1} = g_1^{-1}g_2^{-1}$. This is the right-action axiom.

^pf-23-1

*Uses:* [[§23 Actions#^def-23-1|Def. §23.1]], [[§2 First Consequences of the Axioms#^prop-2-4|§2.4]]

> [!remark] Remark: Left and Right Are Interchangeable
> The proposition (and its mirror image) show that left and right actions carry the same information: inverting the group element converts one into the other. The distinction matters only for bookkeeping the order of composition. The same inversion produces the bijection $gH \mapsto Hg^{-1}$ between left and right cosets ([[§26 Left and Right Cosets#^prop-26-3|§26.3]]).

^rem-23-3

## Actions as Homomorphisms to $S_X$

> [!theorem] Proposition §23.2: Each Group Element Acts Bijectively
> Let $G$ act on $X$.
> 1. $e \star x = x$ for all $x \in X$.
> 2. For each $g \in G$, the map $\hat g: X \to X$, $\hat g(x) = g \star x$, is a bijection, with inverse $\widehat{g^{-1}}$.
>
> *Source: WS 4.2*

^prop-23-2

> [!proof]+ Proof
> (1) is the second axiom. (2) For $x \in X$, $\widehat{g^{-1}}(\hat g(x)) = g^{-1} \star (g \star x) = (g^{-1}g) \star x = e \star x = x$, and symmetrically $\hat g(\widehat{g^{-1}}(x)) = x$. So $\widehat{g^{-1}}$ is a two-sided inverse of $\hat g$, which is therefore a bijection.

^pf-23-2

*Uses:* [[§23 Actions#^def-23-1|Def. §23.1]], [[§21 Algebra Prerequisites꞉ Groups#^prop-21-4|590 §21.4]]

> [!remark]- Connections
> - A two-sided inverse means bijective, in MATH 590: [[§21 Algebra Prerequisites꞉ Groups#^prop-21-4|Bijectivity via Two-Sided Inverse]] (590 §21.4).

> [!theorem] Theorem §23.3: Actions Are Homomorphisms to $S_X$
> Let $G$ be a group and $X$ a set, and recall that $S_X$ is the group of all bijections $X \to X$, with operation composition ($\sigma\tau = \sigma \circ \tau$), identity $\operatorname{id}_X$, and inverses the inverse functions ([[§3 Basic Examples of Groups#^def-3-5|Def. §3.5]]). An action of $G$ on $X$ is the same thing as a group homomorphism $\varphi: G \to S_X$. Precisely:
> 1. given an action, the rule $\varphi(g) := \hat g$, where $\hat g: X \to X$, $\hat g(x) = g \star x$, defines a homomorphism $\varphi: G \to S_X$;
> 2. given a homomorphism $\varphi: G \to S_X$, the rule $g \star x := \varphi(g)(x)$ defines an action of $G$ on $X$;
> 3. the two constructions are inverse to each other.
>
> *Source: WS 4.3*

^thm-23-3

> [!remark] Remark: From a Function of Two Variables to a Function of One
> An action is a function of two variables, $G \times X \to X$, $(g, x) \mapsto g \star x$. Freezing the first variable at $g$ leaves a function of one variable, $\hat g = g \star (\,\cdot\,): X \to X$, telling how $g$ moves the points of $X$. So an action produces an assignment $g \mapsto \hat g$ from $G$ to maps $X \to X$. The theorem makes two claims about this assignment: its values are *bijections*, hence elements of $S_X$; and it converts the *multiplication of $G$* into the *operation of $S_X$*, which is composition.

^rem-23-4

> [!proof]+ Proof
> **(1) Action $\Rightarrow$ homomorphism.** There are two things to check.
>
> *The values lie in $S_X$.* An element of $S_X$ is a bijection $X \to X$. For each $g$, the map $\hat g: X \to X$ has the two-sided inverse $\widehat{g^{-1}}$ ([[§23 Actions#^prop-23-2|WS 4.2]]): for every $x$,
>
> $$
> \widehat{g^{-1}}\big(\hat g(x)\big) = g^{-1} \star (g \star x) = (g^{-1}g) \star x = e \star x = x,
> $$
>
> and symmetrically $\hat g\big(\widehat{g^{-1}}(x)\big) = x$. So $\hat g$ is a bijection, i.e. $\hat g \in S_X$, and $\varphi$ is a well-defined map $G \to S_X$.
>
> *Products go to products.* The product of $\varphi(g_1)$ and $\varphi(g_2)$ in $S_X$ is the composition $\hat g_1 \circ \hat g_2$. For every $x \in X$,
>
> $$
> \varphi(g_1 g_2)(x) = \widehat{g_1 g_2}(x) = (g_1 g_2) \star x \overset{\text{axiom}}{=} g_1 \star (g_2 \star x) = \hat g_1\big(\hat g_2(x)\big) = (\hat g_1 \circ \hat g_2)(x).
> $$
>
> Two maps $X \to X$ agreeing at every $x$ are equal, so $\varphi(g_1g_2) = \hat g_1 \circ \hat g_2 = \varphi(g_1)\varphi(g_2)$. Thus the action axiom $(g_1g_2) \star x = g_1 \star (g_2 \star x)$ is *literally* the statement that $\varphi$ carries the product in $G$ to the product in $S_X$.
>
> *Consistency with the identity and inverses of $S_X$.* Although automatic for any homomorphism ([[§15 Homomorphisms#^prop-15-1|§15.1]]), it is instructive to see these directly. The identity of $S_X$ is $\operatorname{id}_X$, and $\varphi(e) = \hat e$ satisfies $\hat e(x) = e \star x = x$, so $\varphi(e) = \operatorname{id}_X$: this is the second action axiom. The inverse of $\varphi(g)$ in $S_X$ is the inverse function of $\hat g$, which by the computation above is $\widehat{g^{-1}} = \varphi(g^{-1})$: this is [[§23 Actions#^prop-23-2|WS 4.2]].
>
> **(2) Homomorphism $\Rightarrow$ action.** Let $\varphi: G \to S_X$ be a homomorphism. For each $g$, $\varphi(g)$ is an element of $S_X$, i.e. a map $X \to X$; so $\varphi(g)(x) \in X$ is defined for every $x$, and $g \star x := \varphi(g)(x)$ defines a map $G \times X \to X$. The axioms:
>
> $$
> (g_1g_2) \star x = \varphi(g_1g_2)(x) = \big(\varphi(g_1) \circ \varphi(g_2)\big)(x) = \varphi(g_1)\big(\varphi(g_2)(x)\big) = g_1 \star (g_2 \star x),
> $$
>
> using that $\varphi$ is a homomorphism *and that the operation of $S_X$ is composition*; and $e \star x = \varphi(e)(x) = \operatorname{id}_X(x) = x$, using that a homomorphism sends $e$ to the identity element of $S_X$, which is $\operatorname{id}_X$.
>
> **(3) Inverse constructions.** Starting from an action $\star$, forming $\varphi$, and then forming an action from $\varphi$ gives $(g, x) \mapsto \varphi(g)(x) = \hat g(x) = g \star x$, the original action. Starting from $\varphi$, forming the action $g \star x = \varphi(g)(x)$, and then forming its homomorphism gives $g \mapsto \big(x \mapsto \varphi(g)(x)\big) = \varphi(g)$, the original homomorphism.

^pf-23-3

*Uses:* [[§23 Actions#^def-23-1|Def. §23.1]], [[§23 Actions#^prop-23-2|§23.2]], [[§3 Basic Examples of Groups#^def-3-5|Def. §3.5]], [[§15 Homomorphisms#^def-15-1|Def. §15.1]], [[§15 Homomorphisms#^prop-15-1|§15.1]]

> [!remark]- Connections
> - Actions used to manufacture homomorphisms later: [[§29 G Acting on Coset Spaces#^prop-29-1|The Action of G on G/H]], [[§36 Sources of Normal Subgroups#^thm-36-5|§36.5]], [[§40 Simple Groups#^prop-40-10|The Pair-Partition Homomorphism]].
> - Topological version: for a continuous action each translation is a homeomorphism with inverse the translation by the inverse, [[§12 Group Actions and Orbit Spaces#^lem-12-2|591 Lemma §12.2]], so the homomorphism lands in the homeomorphisms of X.

> [!example] Example §23.3: Seeing the Permutations
> **Rotating a triangle.** Let $G = \mathbb{Z}/3\mathbb{Z}$ act on the vertices $X = \{1, 2, 3\}$ of a triangle by rotation, $[k] \star i = $ the vertex $k$ steps further around (so $[1] \star 1 = 2$, $[1] \star 2 = 3$, $[1] \star 3 = 1$). Freezing $g$ and reading off where each vertex goes gives an element of $S_3$ in cycle notation:
>
> $$
> \varphi([0]) = e, \qquad \varphi([1]) = (1\,2\,3), \qquad \varphi([2]) = (1\,3\,2).
> $$
>
> The homomorphism property can be checked directly, e.g. $\varphi([1] + [1]) = \varphi([2]) = (1\,3\,2) = (1\,2\,3)^2 = \varphi([1])\varphi([1])$. Here $\varphi$ is injective, with image the subgroup $A_3 = \langle (1\,2\,3) \rangle \leq S_3$.
>
> **A non-injective example.** Let $G = \mathbb{Z}/4\mathbb{Z}$ act on $X = \{1, 2\}$ by $[k] \star i = i$ if $k$ is even and swapping $1 \leftrightarrow 2$ if $k$ is odd. Then $\varphi([0]) = \varphi([2]) = e$ and $\varphi([1]) = \varphi([3]) = (1\,2)$, so $\operatorname{Ker}\varphi = \{[0], [2]\}$: the element $[2]$ acts trivially, and the action is not faithful.
>
> **The cube.** For the rotation group of the cube acting on its six faces ([[§30 Examples꞉ Linear Groups and the Cube#^prop-30-3|§30.3]]), the $90^\circ$ rotation about the vertical axis fixes the top and bottom faces and cycles the four side faces, so $\varphi$ sends it to a $4$-cycle in $S_6$; the $120^\circ$ rotation about a body diagonal cycles the three faces meeting at one end and the three at the other, giving a product of two disjoint $3$-cycles.

^ex-23-3

![[m493-23-2.svg]]
*$\mathbb{Z}/3\mathbb{Z}$ rotating the vertices of a triangle. Freezing $[1]$ (blue) sends $1 \to 2 \to 3 \to 1$, the $3$-cycle $(1\,2\,3)$; freezing $[2]$ (red; two steps around is one step backwards) sends $1 \to 3 \to 2 \to 1$, i.e. $(1\,3\,2)$. Reading off where each vertex goes is the homomorphism $\varphi: \mathbb{Z}/3\mathbb{Z} \to S_3$ of [[§23 Actions#^thm-23-3|Theorem §23.3]].*

> [!remark] Remark: Why the Identity Axiom Is What Lands $\varphi$ in $S_X$
> [[§23 Actions#^thm-23-3|Part (2)]] never used that $\varphi(g)$ is a *bijection*, only that it is a map $X \to X$ and that composition matches multiplication. One could therefore consider assignments $g \mapsto \hat g$ into all maps $X \to X$ respecting products. The [[§23 Actions#^ex-23-1|lecture's example]] of the trivial group acting on $\{0, 1\}$ by $e \star 0 = e \star 1 = 0$ is exactly such an assignment: it sends $e$ to the map $0 \mapsto 0,\ 1 \mapsto 0$, which satisfies $\hat e \circ \hat e = \hat e$ but is not a bijection, so it is *not* an element of $S_X$. The axiom $e \star x = x$ is precisely what forces $\hat e = \operatorname{id}_X$, and then $\widehat{g^{-1}} \circ \hat g = \hat e = \operatorname{id}_X$ forces every $\hat g$ to be a bijection.

^rem-23-5

> [!remark] Remark: Two Languages for One Thing
> “$G$ acts on $X$” and “there is a homomorphism $G \to S_X$” are interchangeable, and each is useful: the action language describes what happens to points of $X$; the homomorphism language brings in kernels, images, and the results of [[· 4 Homomorphisms and Isomorphisms|Chapter 4]].

^rem-23-6

## Faithful Actions and Cayley's Theorem

> [!definition] Definition §23.3: Kernel of an Action; Faithful Action
> The **kernel** of an action of $G$ on $X$ is the [[§15 Homomorphisms#^def-15-2|kernel]] of the associated homomorphism $\varphi: G \to S_X$, namely $\{g \in G : g \star x = x \text{ for all } x \in X\}$, the elements acting trivially on every point. The action is **faithful** if its kernel is $\{e\}$, i.e. if only the identity fixes every point.

^def-23-3

> [!remark]- Connections
> - Faithful and non-faithful actions of the cube group: [[§30 Examples꞉ Linear Groups and the Cube#^prop-30-4|§30.4]], [[§30 Examples꞉ Linear Groups and the Cube#^ex-30-1|Ex. §30.1]].

> [!theorem] Proposition §23.4: Faithful Actions Embed $G$ in $S_X$
> If $G$ acts faithfully on $X$, then $\varphi: G \to S_X$ is injective and $G \cong \varphi(G) \leq S_X$. If moreover $|X| = n$, then $G$ is isomorphic to a subgroup of $S_n$.

^prop-23-4

> [!proof]+ Proof
> $\varphi$ is injective iff its kernel is trivial ([[§15 Homomorphisms#^prop-15-3|Surjectivity and Injectivity via Image and Kernel]], §15), and an injective homomorphism is an isomorphism onto its image ([[§15 Homomorphisms#^prop-15-4|Images and Preimages of Subgroups]]). For $|X| = n$, choose a bijection $f: \{1, \ldots, n\} \to X$; then $\sigma \mapsto f^{-1} \circ \sigma \circ f$ is an isomorphism $S_X \to S_n$ (a bijection with inverse $\tau \mapsto f \tau f^{-1}$, and $f^{-1}\sigma\sigma' f = (f^{-1}\sigma f)(f^{-1}\sigma' f)$), so $\varphi(G)$ is carried to an isomorphic subgroup of $S_n$.

^pf-23-4

*Uses:* [[§23 Actions#^def-23-3|Def. §23.3]], [[§23 Actions#^thm-23-3|§23.3]], [[§15 Homomorphisms#^prop-15-3|§15.3]], [[§15 Homomorphisms#^prop-15-4|§15.4]], [[§16 Isomorphisms#^def-16-1|Def. §16.1]], [[§3 Basic Examples of Groups#^def-3-5|Def. §3.5]]

> [!theorem] Theorem §23.5: Cayley's Theorem
> Every group $G$ is isomorphic to a subgroup of $S_G$. In particular, a group with $n$ elements is isomorphic to a subgroup of $S_n$.
>
> *Source: PS 3.1(1)*

^thm-23-5

> [!proof]+ Proof
> $G$ acts on itself by left multiplication, $g \star x = gx$: the axioms are $ex = x$ and associativity. The action is faithful: if $g$ acts trivially on every point then in particular $g = ge = e$ (equivalently, $\hat g_1 = \hat g_2$ gives $g_1 = g_1e = g_2e = g_2$). By Faithful Actions Embed $G$ in $S_X$ ([[§23 Actions#^prop-23-4|§23.4]]), the homomorphism $\varphi: G \to S_G$, $\varphi(g) = (x \mapsto gx)$, is injective, $G \cong \varphi(G) \leq S_G$, and relabelling the $n$ elements of $G$ as $1, \ldots, n$ gives an isomorphism $S_G \cong S_n$.

^pf-23-5

*Uses:* [[§23 Actions#^ex-23-2|Ex. §23.2]], [[§23 Actions#^def-23-3|Def. §23.3]], [[§23 Actions#^prop-23-4|§23.4]]

> [!remark]- Connections
> - Revisited through the First Isomorphism Theorem: [[§38 The First Isomorphism Theorem#^rem-38-3|PS 3.1 and PS 3.2 as Instances]].

> [!theorem] Corollary §23.6: Every Finite Group Is a Matrix Group
> Let $G$ be a group with $n$ elements and $k$ any field. Then $G$ is isomorphic to a subgroup of $GL_n(k)$.
>
> *Source: PS 3.1(2)*

^cor-23-6

> [!proof]+ Proof
> Compose the injective homomorphism $G \to S_n$ of [[§23 Actions#^thm-23-5|Cayley's theorem]] with the permutation representation $S_n \to GL_n(k)$, $\sigma \mapsto M(\sigma)$, which is an injective homomorphism ([[§19 Polynomial Rings, Permutation Matrices, and Representations#^prop-19-5|§19.5]]). The composite is an injective homomorphism, so it is an isomorphism onto its image, a subgroup of $GL_n(k)$ ([[§15 Homomorphisms#^prop-15-4|Images and Preimages of Subgroups]]).

^pf-23-6

*Uses:* [[§23 Actions#^thm-23-5|§23.5]], [[§19 Polynomial Rings, Permutation Matrices, and Representations#^prop-19-5|§19.5]], [[§15 Homomorphisms#^prop-15-4|§15.4]], [[§3 Basic Examples of Groups#^def-3-6|Def. §3.6]]

![[m493-23-1.svg]]
*The embedding of a group of order $n$ into $GL_n(k)$: Cayley's theorem, relabelling, and the permutation representation, each injective. Their composite (blue) is the embedding of Corollary §23.6.*

> [!remark]- Connections
> - The small representations the next remark asks for begin with characters: [[§41 Characters#^rem-41-4|One-Dimensional Representations]].

> [!remark] Remark: Why Cayley's Theorem Matters, and Why It Is Not the End
> Cayley's theorem says that “abstract group” and “group of permutations” are the same notion: nothing is lost by studying only subgroups of symmetric groups. Its corollary is the first appearance of the idea behind the second half of the course — every finite group has a faithful [[§19 Polynomial Rings, Permutation Matrices, and Representations#^def-19-6|representation]] by matrices. The embedding is, however, very inefficient: a group of order $n$ is placed inside $S_n$, of order $n!$, or into $n \times n$ matrices. Much of representation theory is about finding the small, informative representations instead.

^rem-23-7
