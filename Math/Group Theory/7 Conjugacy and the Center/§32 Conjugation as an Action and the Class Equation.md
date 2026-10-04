---
type: section
subject: "[[Group Theory]]"
chapter: 7
section: 32
tags: [group-theory, math493]
---
← [[§31 Conjugacy Classes]] · ↑ [[· 7 Conjugacy and the Center]] · [[§33 The Center]] →

*Reference: Pinter Ch. 13, Ex. I; Ch. 15, Ex. G (the class equation).*

> [!definition] Definition §32.1: Centralizer
> For $g$ in a group $G$, the **centralizer** of $g$ is $C_G(g) := \{h \in G : hg = gh\}$, the set of elements commuting with $g$. ([[493 Problem Set 3#^hw-3-4|Problem Set 3]] writes $Z(g)$; these notes reserve $Z(G)$ for the [[§33 The Center#^def-33-1|center]].)

^def-32-1

> [!theorem] Proposition §32.1: The Conjugation Action
> A group $G$ acts on itself by conjugation, $h \star g := hgh^{-1}$. Under this action, for $g \in G$:
> 1. the orbit of $g$ is its conjugacy class $\operatorname{Conj}(g)$;
> 2. the stabilizer of $g$ is the centralizer $C_G(g)$; in particular $C_G(g)$ is a subgroup of $G$;
> 3. $g$ has a one-point orbit if and only if $C_G(g) = G$, if and only if $g$ is central.
>
> The corresponding homomorphism $G \to S_G$ ([[§23 Actions#^thm-23-3|§23.3]]) is $h \mapsto c_h$, with image the inner automorphisms ([[§18 Conjugation, Products, and Pointwise Products#^def-18-2|Def. §18.2]]) and kernel $\{h : hgh^{-1} = g \text{ for all } g\} = Z(G)$.

^prop-32-1

> [!proof]+ Proof
> It is an action: $e \star g = g$, and $h_1 \star (h_2 \star g) = h_1 h_2 g h_2^{-1} h_1^{-1} = (h_1h_2) \star g$. (1) is the definition of $\operatorname{Conj}(g)$. (2) $h$ fixes $g$ iff $hgh^{-1} = g$ iff $hg = gh$; it is a subgroup because stabilizers are ([[§24 Stabilizers and Fixed Points#^prop-24-1|§24.1]]). (3) The orbit is $\{g\}$ iff every $h$ fixes $g$ iff $C_G(g) = G$ iff $hg = gh$ for all $h$. The kernel of $h \mapsto c_h$ is the set of $h$ acting trivially on every $g$, i.e. commuting with everything.

^pf-32-1

*Uses:* [[§23 Actions#^def-23-1|Def. §23.1]], [[§25 Orbits#^def-25-1|Def. §25.1]], [[§31 Conjugacy Classes#^def-31-1|Def. §31.1]], [[§24 Stabilizers and Fixed Points#^def-24-1|Def. §24.1]], [[§32 Conjugation as an Action and the Class Equation#^def-32-1|Def. §32.1]], [[§24 Stabilizers and Fixed Points#^prop-24-1|§24.1]], [[§23 Actions#^thm-23-3|§23.3]], [[§23 Actions#^def-23-3|Def. §23.3]], [[§18 Conjugation, Products, and Pointwise Products#^def-18-2|Def. §18.2]], [[§33 The Center#^def-33-1|Def. §33.1]]

> [!remark]- Connections
> - For a matrix group, conjugation X ↦ gXg⁻¹ applied to tangent vectors at the identity is the adjoint action, [[§23 Tangent Spaces I꞉ The Geometric Picture#^def-23-2|591 Def. §23.2]].

> [!theorem] Corollary §32.2: Class Sizes Divide the Group Order
> For every $g$ in a finite group $G$, $|\operatorname{Conj}(g)| = [G : C_G(g)]$ divides $|G|$, and $|\operatorname{Conj}(g)| \cdot |C_G(g)| = |G|$.
>
> *Source: PS 3.4(1)*

^cor-32-2

> [!proof]+ Proof
> [[§28 Orbit–Stabilizer#^thm-28-3|Orbit–Stabilizer, §28.3]] applied to the conjugation action.

^pf-32-2

*Uses:* [[§28 Orbit–Stabilizer#^thm-28-3|§28.3]], [[§32 Conjugation as an Action and the Class Equation#^prop-32-1|§32.1]]

> [!remark] Remark: Notation: $C_G(g)$ versus $Z(g)$
> [[493 Problem Set 3#^hw-3-4|Problem Set 3]] writes $Z(g)$ for the centralizer of $g$; these notes write $C_G(g)$, reserving $Z(G)$ for the center. They are related by $Z(G) = \bigcap_{g} C_G(g)$, and $g \in Z(G)$ iff $C_G(g) = G$.

^rem-32-1

> [!theorem] Corollary §32.3: The Class Equation, Reciprocal Form
> Let $G$ be finite and let $g_1, \ldots, g_c$ be one representative from each conjugacy class. Then
>
> $$
> \sum_{i=1}^{c} \frac{1}{|C_G(g_i)|} = 1.
> $$
>
> *Source: PS 3.4(2)*

^cor-32-3

> [!proof]+ Proof
> The conjugacy classes partition $G$, so $|G| = \sum_i |\operatorname{Conj}(g_i)|$. By [[§32 Conjugation as an Action and the Class Equation#^cor-32-2|Class Sizes Divide the Group Order]], $|\operatorname{Conj}(g_i)| = |G|/|C_G(g_i)|$. Divide by $|G|$.

^pf-32-3

*Uses:* [[§32 Conjugation as an Action and the Class Equation#^prop-32-1|§32.1]], [[§25 Orbits#^prop-25-1|§25.1]], [[§32 Conjugation as an Action and the Class Equation#^cor-32-2|§32.2]]

> [!theorem] Theorem §32.4: The Class Equation
> Let $G$ be a finite group and let $g_1, \ldots, g_r$ be representatives of the conjugacy classes with more than one element. Then
>
> $$
> |G| = |Z(G)| + \sum_{i=1}^{r} [G : C_G(g_i)],
> $$
>
> where each summand $[G : C_G(g_i)]$ is a divisor of $|G|$ greater than $1$.
>
> *Source: cf. Pinter Ch. 15, Ex. G*

^thm-32-4

> [!proof]+ Proof
> $G$ is the disjoint union of its conjugacy classes ([[§25 Orbits#^prop-25-1|orbits partition, §25.1]]). The one-element classes are exactly $\{z\}$ for $z \in Z(G)$ by (3) [[§32 Conjugation as an Action and the Class Equation#^prop-32-1|above]], contributing $|Z(G)|$; the remaining classes are $\operatorname{Conj}(g_i)$, of size $[G : C_G(g_i)]$ by [[§32 Conjugation as an Action and the Class Equation#^cor-32-2|Class Sizes Divide the Group Order]].

^pf-32-4

*Uses:* [[§25 Orbits#^prop-25-1|§25.1]], [[§32 Conjugation as an Action and the Class Equation#^prop-32-1|§32.1]], [[§32 Conjugation as an Action and the Class Equation#^cor-32-2|§32.2]], [[§33 The Center#^def-33-1|Def. §33.1]]

> [!remark]- Connections
> - The key input for [[§33 The Center#^thm-33-3|Groups of Prime-Power Order Have Nontrivial Center, §33.3]] and [[§33 The Center#^cor-33-4|§33.4]]; one route to [[§27 The Index and Lagrange's Theorem#^thm-27-6|Cauchy's Theorem, §27.6]].

> [!example] Example §32.1: Class Equations of $S_3$ and $S_4$
> For $S_3$, the classes have sizes $1, 3, 2$ ([[§31 Conjugacy Classes#^ex-31-2|Ex. §31.2]]), so $6 = 1 + 3 + 2$ with $Z(S_3) = \{e\}$; the centralizers have orders $6, 2, 3$. For $S_4$: $24 = 1 + 6 + 3 + 8 + 6$, again with trivial center. In an abelian group every class is a singleton and the equation reads $|G| = |Z(G)|$.

^ex-32-1

> [!theorem] Proposition §32.5: Three Conjugacy Classes Force Order at Most $6$
> If $G$ is a finite group with exactly $3$ conjugacy classes, then $|G| \leq 6$.
>
> *Source: PS 3.6*

^prop-32-5

> [!proof]+ Proof
> Take representatives $g_1 = e, g_2, g_3$ (the class of $e$ is $\{e\}$). Then $C_G(e) = G$, and write $a = |C_G(g_2)| \leq b = |C_G(g_3)|$ after relabelling; both are at most $|G|$. The [[§32 Conjugation as an Action and the Class Equation#^cor-32-3|reciprocal class equation]] reads
>
> $$
> \frac{1}{a} + \frac{1}{b} + \frac{1}{|G|} = 1, \qquad \frac{1}{a} \geq \frac{1}{b} \geq \frac{1}{|G|}.
> $$
>
> Replacing each term by the largest, $1 \leq 3/a$, so $a \leq 3$; and $a \neq 1$, since otherwise the other two positive terms would sum to $0$. If $a = 2$: $\frac{1}{b} + \frac{1}{|G|} = \frac{1}{2}$ gives $\frac{1}{2} \leq \frac{2}{b}$, so $b \leq 4$; $b = 2$ is impossible, $b = 3$ gives $|G| = 6$, and $b = 4$ gives $|G| = 4$. If $a = 3$: $\frac{1}{b} + \frac{1}{|G|} = \frac{2}{3}$ gives $b \leq 3$, so $b = 3$ and $|G| = 3$. In every case $|G| \in \{3, 4, 6\}$.

^pf-32-5

*Uses:* [[§32 Conjugation as an Action and the Class Equation#^cor-32-3|§32.3]], [[§32 Conjugation as an Action and the Class Equation#^def-32-1|Def. §32.1]]

> [!theorem] Proposition §32.6: Groups of Order $4$ Are Abelian
> Every group of order $4$ is abelian.
>
> *Source: not from class*

^prop-32-6

> [!proof]+ Proof
> By [[§27 The Index and Lagrange's Theorem#^cor-27-3|Lagrange]] every element has order $1$, $2$ or $4$. If some element has order $4$, the group is cyclic, hence abelian. Otherwise $x^2 = e$ for all $x$, i.e. $x = x^{-1}$ for all $x$, whence $ab = (ab)^{-1} = b^{-1}a^{-1} = ba$.

^pf-32-6

*Uses:* [[§27 The Index and Lagrange's Theorem#^cor-27-3|§27.3]], [[§17 Cyclic Groups#^cor-17-2|§17.2]], [[§4 Subgroups#^def-4-5|Def. §4.5]], [[§2 First Consequences of the Axioms#^prop-2-4|§2.4]]

> [!theorem] Corollary §32.7: Exactly Three Conjugacy Classes: Order $3$ or $6$
> A finite group with exactly three conjugacy classes has order $3$ or $6$, and both occur: $\mathbb{Z}/3\mathbb{Z}$ and $S_3$.
>
> *Source: not from class*

^cor-32-7

> [!proof]+ Proof
> By Three Conjugacy Classes Force Order at Most $6$ ([[§32 Conjugation as an Action and the Class Equation#^prop-32-5|§32.5]]), $|G| \in \{3, 4, 6\}$. The case $|G| = 4$ solves the equation but not the problem: a group of order $4$ is abelian ([[§32 Conjugation as an Action and the Class Equation#^prop-32-6|§32.6]]), so its conjugacy classes are singletons and there are $4$ of them. Finally $\mathbb{Z}/3\mathbb{Z}$ has $3$ classes, and $S_3$ has $3$ classes, of sizes $1, 3, 2$.

^pf-32-7

*Uses:* [[§32 Conjugation as an Action and the Class Equation#^prop-32-5|§32.5]], [[§32 Conjugation as an Action and the Class Equation#^prop-32-6|§32.6]], [[§33 The Center#^prop-33-1|§33.1]], [[§31 Conjugacy Classes#^ex-31-2|Ex. §31.2]]

![[m493-32-1.svg]]
*The reciprocal class equation as a division of $G$: in each bar the class of $g_i$ takes up the fraction $|\operatorname{Conj}(g_i)|/|G| = 1/|C_G(g_i)|$. With three classes, $\tfrac1{|G|} + \tfrac1a + \tfrac1b = 1$ has only the solutions $|G| = 6$ (realized by $S_3$: $e$, the three transpositions, the two $3$-cycles), $|G| = 3$ (realized by $\mathbb{Z}/3\mathbb{Z}$), and $|G| = 4$, which is excluded (dashed) because a group of order $4$ is abelian and so has $4$ classes.*

> [!remark] Remark: Reading Chapter 7 Through Actions
> Everything in this chapter is an orbit or stabilizer computation for a conjugation action: the conjugacy classes of $S_n$ are the orbits of $S_n$ on itself, [[§31 Conjugacy Classes#^thm-31-3|classified by cycle type]]; the conjugacy class of a matrix is its orbit under $GL_n(\mathbb{C})$ acting on $\operatorname{Mat}_n(\mathbb{C})$ by $P \star A = PAP^{-1}$, classified (for distinct eigenvalues) by the [[§31 Conjugacy Classes#^prop-31-4|characteristic polynomial]]; and [[§33 The Center#^prop-33-1|WS 3.5]] and [[§33 The Center#^prop-33-2|3.6]] below say, in this language, that the center is the set of fixed points of the action and the kernel of the associated homomorphism.

^rem-32-2
