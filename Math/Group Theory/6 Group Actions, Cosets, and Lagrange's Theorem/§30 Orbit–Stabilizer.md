---
type: section
subject: "[[Group Theory]]"
chapter: 6
section: 30
tags: [group-theory, math493]
---
← [[§29 The Index and Lagrange's Theorem]] · ↑ [[· 6 Group Actions, Cosets, and Lagrange's Theorem]] · [[§31 G Acting on Coset Spaces]] →

*Reference: Pinter Ch. 13, Ex. J.*

> [!theorem] Proposition §30.1: When Two Group Elements Move $x$ to the Same Place
> Let $G$ act on $X$, $x \in X$, and $g_1, g_2 \in G$. The following are equivalent:
> 1. $g_1 \star x = g_2 \star x$;
> 2. $g_1^{-1}g_2 \in \operatorname{Stab}(x)$;
> 3. $g_1\operatorname{Stab}(x) = g_2\operatorname{Stab}(x)$.
>
> *Source: WS 5.1*

^prop-30-1

> [!proof]+ Proof
> (1) $\Leftrightarrow$ (2): apply $g_1^{-1}$ to both sides of (1) to get $x = (g_1^{-1}g_2) \star x$, which is (2); apply $g_1$ to (2) to recover (1). (2) $\Leftrightarrow$ (3): this is the coset criterion of [[§28 Left and Right Cosets#^prop-28-2|§28.2]], $g_1H = g_2H \iff g_1^{-1}g_2 \in H$, with $H = \operatorname{Stab}(x)$.

^pf-30-1

*Uses:* [[§25 Actions#^def-25-1|Def. §25.1]], [[§26 Stabilizers and Fixed Points#^def-26-1|Def. §26.1]], [[§26 Stabilizers and Fixed Points#^prop-26-1|§26.1]], [[§28 Left and Right Cosets#^prop-28-2|§28.2]]

> [!theorem] Proposition §30.2: The Orbit Bijection
> Let $G$ act on $X$ and $x \in X$. The map
>
> $$
> G/\operatorname{Stab}(x) \longrightarrow Gx, \qquad g\operatorname{Stab}(x) \longmapsto g \star x,
> $$
>
> is well defined and bijective.
>
> *Source: WS 5.2*

^prop-30-2

> [!proof]+ Proof
> Write $H = \operatorname{Stab}(x)$. Three things must be checked, and the first is the one that is easy to overlook.
>
> **Well defined.** The formula uses a representative $g$ of the coset $gH$, so we must check the value is unchanged if another representative is used. Suppose $g_1 H = g_2 H$. Then $g_1 = g_2 h$ for some $h \in H$ ([[§28 Left and Right Cosets#^prop-28-2|§28.2]]), and since $h \star x = x$ by definition of the stabilizer,
>
> $$
> g_1 \star x = (g_2 h) \star x = g_2 \star (h \star x) = g_2 \star x,
> $$
>
> the middle equality being the action axiom.
>
> **Injective.** Suppose $g_1 \star x = g_2 \star x$. Applying $g_2^{-1}$ to both sides, $(g_2^{-1}g_1) \star x = x$, so $g_2^{-1}g_1 = h$ for some $h \in H$; then $g_1 = g_2 h$ and $g_1 H = g_2 H$.
>
> **Surjective.** Let $x' \in Gx$, say $x' = g' \star x$ with $g' \in G$. Then $g'H \mapsto x'$.
>
> (The first two steps are the two directions of one statement — $g_1 \star x = g_2 \star x$ if and only if $g_1H = g_2H$ — which is [[§30 Orbit–Stabilizer#^prop-30-1|WS 5.1]]; written as a chain of “if and only if” they collapse into a single computation.)

^pf-30-2

*Uses:* [[§25 Actions#^def-25-1|Def. §25.1]], [[§26 Stabilizers and Fixed Points#^def-26-1|Def. §26.1]], [[§27 Orbits#^def-27-1|Def. §27.1]], [[§28 Left and Right Cosets#^prop-28-2|§28.2]], [[§30 Orbit–Stabilizer#^prop-30-1|§30.1]]

![[m493-28-1.svg]]
*The orbit map $g \mapsto g \star x$ factors through the coset space $G/\operatorname{Stab}(x)$, and the induced map is a bijection onto the orbit.*

> [!remark]- Connections
> - The same “factor through the quotient” shape: [[§41 The First and Second Isomorphism Theorems#^thm-41-1|First Isomorphism Theorem, §41.1]]; in topology, [[Universal Property of Quotient Maps|590 Thm. §13.3 (Universal Property of Quotient Maps)]].
> - Topological upgrade: for a continuous transitive action the same bijection G/H → X is continuous, and a homeomorphism when G/H is compact and X Hausdorff, [[§14 Homogeneous Spaces#^lem-14-5|591 Lemma §14.5]], [[Homogeneous Spaces Are Coset Spaces|591 Thm. §14.3]].

> [!theorem] Theorem §30.3: Orbit–Stabilizer
> Let $G$ act on $X$ and $x \in X$. Then
>
> $$
> |G| = |Gx| \cdot |\operatorname{Stab}(x)|,
> $$
>
> in the sense of Lagrange's theorem ([[§29 The Index and Lagrange's Theorem#^thm-29-2|§29.2]]): the left side is finite iff both factors are, and then equality holds. In particular, for finite $G$ the size of every orbit divides $|G|$.
>
> *Source: WS 5.3*

^thm-30-3

> [!proof]+ Proof
> By [[§30 Orbit–Stabilizer#^prop-30-2|WS 5.2]], $|Gx| = |G/\operatorname{Stab}(x)| = [G : \operatorname{Stab}(x)]$, and $\operatorname{Stab}(x)$ is a subgroup ([[§26 Stabilizers and Fixed Points#^prop-26-1|WS 4.4]]). Lagrange gives $|G| = |\operatorname{Stab}(x)| \cdot [G : \operatorname{Stab}(x)]$.

^pf-30-3

*Uses:* [[§30 Orbit–Stabilizer#^prop-30-2|§30.2]], [[§26 Stabilizers and Fixed Points#^prop-26-1|§26.1]], [[§29 The Index and Lagrange's Theorem#^def-29-1|Def. §29.1]], [[§29 The Index and Lagrange's Theorem#^thm-29-2|§29.2]]

> [!remark]- Connections
> - Applied to conjugation: [[§34 Conjugation as an Action and the Class Equation#^cor-34-2|Class Sizes Divide the Group Order, §34.2]]; to the cube: [[§32 Linear Groups, the Cube, S₃ and A₄#^prop-32-3|Rotational Symmetries of the Cube, §32.3]].

> [!remark] Remark: The Structural Picture
> Every action of $G$ on $X$ is now understood in outline: $X$ breaks into orbits, and each orbit $O = Gx$ is in natural bijection with the coset space $G/H$ for the subgroup $H = \operatorname{Stab}(x)$, with $|O| = [G : H]$. [[§31 G Acting on Coset Spaces#^prop-31-1|WS 5.4]] provides the converse: every coset space $G/H$ is itself an orbit of a $G$-action with a point of stabilizer exactly $H$, so “orbits of actions” and “coset spaces of subgroups” are the same objects.

^rem-30-1

> [!example] Example §30.1: A Group of Order 8 Acting on a Four-Petal Figure
> Let $X$ be the four-petal figure drawn in lecture (four congruent petals along the coordinate axes), and $G$ its group of symmetries: the four rotations by multiples of $90^\circ$ and the four reflections (in the two axes and the two diagonals), so $|G| = 8$. Let $x_1$ be the tip of the top petal. Its orbit is the set of the four tips, $Gx_1 = \{x_1, x_2, x_3, x_4\}$, since rotations carry the top petal to each of the others. Its stabilizer consists of the symmetries fixing the top tip: the identity and the reflection in the vertical axis, so $\operatorname{Stab}(x_1) = \{e, r_v\}$. Consistently with the [[§30 Orbit–Stabilizer#^thm-30-3|orbit–stabilizer theorem]], $8 = 2 \cdot 4$. The center of the figure, by contrast, is fixed by everything: its orbit is a single point and its stabilizer is all of $G$, again $8 = 8 \cdot 1$.
>
> *Source: lecture*

^ex-30-1

![[m493-28-2.svg]]
*The four-petal figure from lecture. Red: the orbit $\{x_1, x_2, x_3, x_4\}$ of the tip $x_1$. Green: the vertical axis, whose reflection $r_v$ together with $e$ forms $\operatorname{Stab}(x_1)$. Dotted: the other three reflection axes.*

> [!remark] Remark: Where Orbit–Stabilizer Has Already Appeared
> Two instances: the cosets of the point stabilizer in $S_n$ ([[§30 Orbit–Stabilizer#^cor-30-5|next subsection]]), where the orbit of $n$ is all of $\{1, \ldots, n\}$ and $n! = (n-1)! \cdot n$; and the conjugacy classes of a group ([[· 7 Conjugacy and the Center|Chapter 7]]), which are the orbits of the conjugation action, so that their sizes divide $|G|$ — e.g. $1, 6, 3, 8, 6$ in $S_4$.

^rem-30-2

## Example: The Point Stabilizer in $S_n$

*Source: PS 2.1.*

> [!definition] Definition §30.1: The Point Stabilizer in $S_n$
> For $n \geq 1$, let
>
> $$
> H := \{ \sigma \in S_n : \sigma(n) = n \},
> $$
>
> the *stabilizer* of the point $n$ — that is, $H = \operatorname{Stab}(n)$ for the action of $S_n$ on $\{1, \ldots, n\}$ in the sense of [[§26 Stabilizers and Fixed Points#^def-26-1|Def. §26.1]]. It is a subgroup of $S_n$ (a special case of [[§26 Stabilizers and Fixed Points#^prop-26-1|WS 4.4]], checked directly here): $e(n) = n$; if $\sigma(n) = \tau(n) = n$ then $(\sigma\tau)(n) = \sigma(\tau(n)) = \sigma(n) = n$; and $\sigma(n) = n$ gives $\sigma^{-1}(n) = n$. Restricting a $\sigma \in H$ to $\{1, \ldots, n-1\}$ identifies $H \cong S_{n-1}$, so $|H| = (n-1)!$.

^def-30-1

*Uses:* [[§26 Stabilizers and Fixed Points#^def-26-1|Def. §26.1]], [[§26 Stabilizers and Fixed Points#^prop-26-1|§26.1]], [[§4 Subgroups#^def-4-1|Def. §4.1]], [[§3 Basic Examples of Groups#^def-3-5|Def. §3.5]]

> [!theorem] Proposition §30.4: Left Cosets Record $\alpha(n)$, Right Cosets Record $\alpha^{-1}(n)$
> Let $H = \{\sigma \in S_n : \sigma(n) = n\}$ and $\alpha, \beta \in S_n$. Then
>
> $$
> \alpha H = \beta H \iff \alpha(n) = \beta(n), \qquad\qquad H\alpha = H\beta \iff \alpha^{-1}(n) = \beta^{-1}(n).
> $$
>
> *Source: PS 2.1*

^prop-30-4

> [!proof]+ Proof
> **Left cosets.** ($\Rightarrow$) Since $e \in H$, $\alpha = \alpha e \in \alpha H = \beta H$, so $\alpha = \beta h$ for some $h \in H$; evaluating at $n$ and using $h(n) = n$,
>
> $$
> \alpha(n) = \beta(h(n)) = \beta(n).
> $$
>
> ($\Leftarrow$) Suppose $\alpha(n) = \beta(n)$. Then $(\beta^{-1}\alpha)(n) = \beta^{-1}(\alpha(n)) = \beta^{-1}(\beta(n)) = n$, so $\beta^{-1}\alpha \in H$. Given $\alpha h_1 \in \alpha H$, put $h_2 = (\beta^{-1}\alpha)h_1 \in H$ (closure); then $\beta h_2 = \beta\beta^{-1}\alpha h_1 = \alpha h_1$, so $\alpha H \subseteq \beta H$. The hypothesis is symmetric in $\alpha, \beta$, so the reverse inclusion follows likewise.
>
> *(Alternatively: by [[§28 Left and Right Cosets#^prop-28-2|§28.2]], $\alpha H = \beta H$ iff $\alpha^{-1}\beta \in H$ iff $(\alpha^{-1}\beta)(n) = n$ iff $\beta(n) = \alpha(n)$.)*
>
> **Right cosets.** ($\Rightarrow$) $\alpha = e\alpha \in H\alpha = H\beta$ gives $\alpha = h\beta$ with $h \in H$; then $\alpha^{-1} = \beta^{-1}h^{-1}$, so $\alpha^{-1}h = \beta^{-1}$ and, evaluating at $n$ with $h(n) = n$, $\beta^{-1}(n) = \alpha^{-1}(h(n)) = \alpha^{-1}(n)$. ($\Leftarrow$) If $\alpha^{-1}(n) = \beta^{-1}(n)$, then $(\beta\alpha^{-1})(n) = \beta(\beta^{-1}(n)) = n$, so $\beta\alpha^{-1} \in H$; for $h_2\beta \in H\beta$ put $h_1 = h_2(\beta\alpha^{-1}) \in H$, giving $h_1\alpha = h_2\beta$, so $H\beta \subseteq H\alpha$, and symmetrically.

^pf-30-4

*Uses:* [[§30 Orbit–Stabilizer#^def-30-1|Def. §30.1]], [[§28 Left and Right Cosets#^def-28-2|Def. §28.2]], [[§4 Subgroups#^def-4-1|Def. §4.1]], [[§28 Left and Right Cosets#^prop-28-2|§28.2]]

> [!theorem] Corollary §30.5: Index of the Stabilizer
> The map $\alpha H \mapsto \alpha(n)$ is a bijection from the set $S_n/H$ of left cosets to $\{1, 2, \ldots, n\}$. Hence $[S_n : H] = n$, and Lagrange gives
>
> $$
> n! = |S_n| = |H| \cdot [S_n : H] = (n-1)!\cdot n.
> $$

^cor-30-5

> [!proof]+ Proof
> [[§30 Orbit–Stabilizer#^prop-30-4|The proposition]] says precisely that $\alpha H \mapsto \alpha(n)$ is well defined and injective. It is surjective: given $i \in \{1, \ldots, n\}$, any $\alpha$ with $\alpha(n) = i$ (e.g. the transposition $(i\ n)$, or $e$ if $i = n$) has $\alpha H \mapsto i$.

^pf-30-5

*Uses:* [[§30 Orbit–Stabilizer#^prop-30-4|§30.4]], [[§29 The Index and Lagrange's Theorem#^def-29-1|Def. §29.1]], [[§29 The Index and Lagrange's Theorem#^thm-29-2|§29.2]], [[§30 Orbit–Stabilizer#^def-30-1|Def. §30.1]]

> [!example] Example §30.2: Left and Right Cosets of $H$ in $S_3$
> Take $n = 3$, so $H = \{e, (1\,2)\}$, and let $\alpha = (1\,2\,3)$, $\beta = (1\,3)$. Then $\alpha(3) = 1 = \beta(3)$, so $\alpha H = \beta H$ by [[§30 Orbit–Stabilizer#^prop-30-4|Left Cosets Record α(n)]]. But $\alpha^{-1}(3) = 2$ while $\beta^{-1}(3) = 1$, so $H\alpha \neq H\beta$. This is the same pair of cosets computed directly in [[§28 Left and Right Cosets#^ex-28-2|Ex. §28.2]].

^ex-30-2

![[m493-28-3.svg]]
*The cosets of $H = \{e, (1\,2)\}$ in $S_3$, sorted as in §30.4: each left coset $\alpha H$ (row) collects the permutations with one value of $\alpha(3)$, each right coset $H\alpha$ (column) those with one value of $\alpha^{-1}(3)$. The pair $\alpha = (1\,2\,3)$, $\beta = (1\,3)$ (red) share a row, since $\alpha(3) = \beta(3) = 1$, but not a column, since $\alpha^{-1}(3) = 2 \neq 1 = \beta^{-1}(3)$. The left half is the orbit bijection $S_3/H \to \{1,2,3\}$ of §30.5.*

> [!remark] Remark: Why the Bijection $G/H \to H\backslash G$ Uses $g^{-1}$
> This example explains the shape of the map in [[§28 Left and Right Cosets#^prop-28-3|§28.3]]. Left cosets of the stabilizer record $\alpha(n)$; right cosets record $\alpha^{-1}(n)$. The two decompositions of $S_n$ are therefore genuinely different — they sort permutations by different data — but they are matched by the operation $\alpha \mapsto \alpha^{-1}$, which converts one datum into the other. This is exactly why the natural bijection is $gH \mapsto Hg^{-1}$ and not $gH \mapsto Hg$.

^rem-30-3

> [!remark] Remark: As an Instance of Orbit–Stabilizer
> This example is the orbit–stabilizer theorem for $G = S_n$ acting on $X = \{1, \ldots, n\}$ and $x = n$: the proposition is [[§30 Orbit–Stabilizer#^prop-30-1|WS 5.1]]'s criterion for this action, the corollary is the [[§30 Orbit–Stabilizer#^prop-30-2|orbit bijection]] $G/\operatorname{Stab}(n) \to Gn = X$ together with $|S_n| = |\operatorname{Stab}(n)| \cdot |X|$, and the “why $g^{-1}$” remark is [[§25 Actions#^prop-25-1|WS 4.1]] read off in a concrete case. It was proved on [[493 Problem Set 2#^hw-2-1|Problem Set 2]] before the general theory, which is why it appears here with its own direct proofs.

^rem-30-4

## Counting Orbits: Burnside's Lemma

> [!theorem] Theorem §30.6: Burnside's Lemma
> Let a finite group $G$ act on a finite set $X$. Then the number of orbits is the average number of fixed points:
>
> $$
> \frac{1}{|G|} \sum_{g \in G} |\operatorname{Fix}(g)| = |G \backslash X|.
> $$
>
> *Source: PS 3.3*

^thm-30-6

> [!proof]+ Proof
> Count the set $P = \{(x, g) \in X \times G : g \star x = x\}$ in two ways. Grouping by $g$, the pairs with second entry $g$ are those with $x \in \operatorname{Fix}(g)$; grouping by $x$, those with first entry $x$ are those with $g \in \operatorname{Stab}(x)$. So
>
> $$
> \sum_{g \in G} |\operatorname{Fix}(g)| = |P| = \sum_{x \in X} |\operatorname{Stab}(x)| = \sum_{x \in X} \frac{|G|}{|Gx|} = |G| \sum_{x \in X} \frac{1}{|Gx|},
> $$
>
> by [[§30 Orbit–Stabilizer#^thm-30-3|orbit–stabilizer]]. The orbits partition $X$ ([[§27 Orbits#^prop-27-1|§27.1]]), and every point $y$ of an orbit $O$ has $Gy = O$; so the points of $O$ contribute $|O| \cdot \frac{1}{|O|} = 1$ to the last sum, which therefore equals the number of orbits. Dividing by $|G|$ gives the result.

^pf-30-6

*Uses:* [[§26 Stabilizers and Fixed Points#^def-26-1|Def. §26.1]], [[§26 Stabilizers and Fixed Points#^def-26-2|Def. §26.2]], [[§27 Orbits#^def-27-1|Def. §27.1]], [[§27 Orbits#^def-27-2|Def. §27.2]], [[§30 Orbit–Stabilizer#^thm-30-3|§30.3]], [[§27 Orbits#^prop-27-1|§27.1]]

> [!example] Example §30.3: Burnside's Lemma in Action
> 1. *$S_3$ on $\{1, 2, 3\}$.* The identity fixes $3$ points, each transposition $1$, each $3$-cycle $0$: $\frac{1}{6}(3 + 1 + 1 + 1 + 0 + 0) = 1$ orbit.
> 2. *The cube on its faces.* Among the $24$ rotations ([[§32 Linear Groups, the Cube, S₃ and A₄#^prop-32-3|§32.3]]): the identity fixes $6$ faces; the $6$ rotations by $\pm 90^\circ$ and the $3$ by $180^\circ$ about face axes each fix $2$; the $8$ rotations about body diagonals and the $6$ about edge axes fix none. So $\frac{1}{24}(6 + 9 \cdot 2) = 1$ orbit, as it must be.
> 3. *Conjugation.* For $G$ acting on itself by conjugation, $\operatorname{Fix}(g) = C_G(g) = \{h : hg = gh\}$, the centralizer of $g$ ([[§34 Conjugation as an Action and the Class Equation#^def-34-1|Def. §34.1]]), and the orbits are the conjugacy classes, so the number of conjugacy classes is the average size of a centralizer, $\frac{1}{|G|}\sum_g |C_G(g)|$. For $S_3$: $\frac{1}{6}(6 + 2 + 2 + 2 + 3 + 3) = 3$.

^ex-30-3

![[m493-28-4.svg]]
*The double count in the proof of Burnside's lemma, for $S_3$ acting on $\{1,2,3\}$ (part 1 of the example): a dot marks each pair with $g \star x = x$. The row sums are $|\operatorname{Fix}(g)|$ (blue) and the column sums are $|\operatorname{Stab}(x)| = 6/|Gx| = 2$ (red); both add up to $|P| = 6$, so the average number of fixed points is $6/6 = 1$ orbit.*
