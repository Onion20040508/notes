---
type: section
subject: "[[Group Theory]]"
chapter: 8
section: 44
tags: [group-theory, math493]
---
← [[§43 Simple Groups]] · ↑ [[· 8 Normal Subgroups and Quotient Groups]] · [[§45 S₃, S₄, A₄ and A₅]] →

*Source: Problem Set 5, Problem 2. PS 5 writes $Z_G(g)$ for the centralizer $C_G(g)$ ([[§34 Conjugation as an Action and the Class Equation#^def-34-1|Def. §34.1]]).*

Two elements of a [[§38 Normal Subgroups#^def-38-1|normal subgroup]] $N$ that are conjugate in $G$ need not be conjugate in $N$: conjugating within $N$ allows fewer conjugators. The criterion below says exactly when they are, and explains how a conjugacy class of $S_5$ splits in $A_5$.

> [!theorem] Proposition §44.1: Conjugacy Relative to a Normal Subgroup
> Let $N \trianglelefteq G$, $g \in N$ and $h \in G$, so that $g$ and $hgh^{-1}$ both lie in $N$ and are conjugate in $G$. Then $hgh^{-1}$ is conjugate to $g$ *in $N$* (i.e. $hgh^{-1} = ngn^{-1}$ for some $n \in N$) if and only if $h \in C_G(g)N$.
>
> *Source: PS 5.2(1)*

^prop-44-1

> [!proof]+ Proof
> ($\Rightarrow$) If $hgh^{-1} = ngn^{-1}$ with $n \in N$, then $z := n^{-1}h$ satisfies $zgz^{-1} = n^{-1}(hgh^{-1})n = g$, so $z \in C_G(g)$. Then $h = nz = z\,(z^{-1}nz)$ with $z^{-1}nz \in N$ by normality, so $h \in C_G(g)N$.
>
> ($\Leftarrow$) If $h = zn'$ with $z \in C_G(g)$ and $n' \in N$, put $n'' = zn'z^{-1} \in N$. Since $zgz^{-1} = g$,
>
> $$ hgh^{-1} = zn'gn'^{-1}z^{-1} = (zn'z^{-1})(zgz^{-1})(zn'^{-1}z^{-1}) = n''\,g\,n''^{-1}. $$

^pf-44-1

*Uses:* [[§34 Conjugation as an Action and the Class Equation#^def-34-1|Def. §34.1]], [[§38 Normal Subgroups#^def-38-1|Def. §38.1]], [[§41 The First and Second Isomorphism Theorems#^def-41-1|Def. §41.1]]

> [!theorem] Proposition §44.2: Two Pairs of Elements of $A_5$
> 1. $(1\,2\,3)$ and $(1\,3\,2)$ are conjugate in $A_5$.
> 2. $C_{S_5}\big((1\,2\,3\,4\,5)\big) = \langle (1\,2\,3\,4\,5) \rangle$, and $(1\,2\,3\,4\,5)$ and $(1\,2\,3\,5\,4)$ are *not* conjugate in $A_5$.
>
> *Source: PS 5.2(2)*

^prop-44-2

> [!proof]+ Proof
> Apply the criterion ([[§44 Conjugacy in a Normal Subgroup#^prop-44-1|Proposition §44.1]]) with $G = S_5$ and $N = A_5$.
>
> **(1)** Let $g = (1\,2\,3)$ and $h = (1\,2)$. By Conjugation Relabels the Entries ([[§33 Conjugacy Classes#^lem-33-1|§33.1]]), $hgh^{-1} = (2\,1\,3) = (1\,3\,2)$. Now $z = (4\,5)$ is disjoint from $g$, so $z \in C_{S_5}(g)$, and $h = (4\,5)\cdot\big((4\,5)(1\,2)\big)$ with $(4\,5)(1\,2) \in A_5$. So $h \in C_{S_5}(g)A_5$, and $(1\,3\,2)$ is conjugate to $(1\,2\,3)$ in $A_5$ (explicitly, by $(1\,2)(4\,5)$).
>
> **(2)** Let $g = (1\,2\,3\,4\,5)$. Powers of $g$ commute with $g$. Conversely, if $hgh^{-1} = g$, then by relabelling
>
> $$ \big(h(1)\ h(2)\ h(3)\ h(4)\ h(5)\big) = (1\,2\,3\,4\,5); $$
>
> reading points mod $5$, the left side sends $h(k) \mapsto h(k+1)$ and the right side sends $h(k) \mapsto h(k) + 1$, so $h(k+1) = h(k) + 1$ for all $k$, and $h = g^{h(1) - 1}$. Thus $C_{S_5}(g) = \langle g \rangle$. A $5$-cycle is even, being a product of four transpositions, so $C_{S_5}(g) \subseteq A_5$ and $C_{S_5}(g)A_5 = A_5$. Now $h = (4\,5)$ gives $hgh^{-1} = (1\,2\,3\,5\,4)$, and $h$ is odd, so $h \notin C_{S_5}(g)A_5$: the two $5$-cycles are not conjugate in $A_5$.

^pf-44-2

*Uses:* [[§44 Conjugacy in a Normal Subgroup#^prop-44-1|§44.1]], [[§33 Conjugacy Classes#^lem-33-1|§33.1]], [[§34 Conjugation as an Action and the Class Equation#^def-34-1|Def. §34.1]]

> [!example] Example §44.1: The Conjugacy Classes of $A_5$, Explained
> The criterion explains the class table of WS 7.4 ($A_5$ Is Simple, [[§43 Simple Groups#^prop-43-6|Proposition §43.6]]). Fix the odd permutation $\tau = (4\,5)$. For $g \in A_5$ with $S_5$-class $K$, every element of $K$ is $hgh^{-1}$ with $h$ even or $h$ odd; the even $h$ give the $A_5$-class of $g$, and the odd $h$ give the $A_5$-class of $\tau g\tau^{-1}$ (since $h = (h\tau)\tau$ with $h\tau$ even). So $K$ is one $A_5$-class if $C_{S_5}(g)$ contains an odd permutation, so that $C_{S_5}(g)A_5 = S_5$, and otherwise splits into two $A_5$-classes, swapped by $x \mapsto \tau x \tau^{-1}$, of size $|K|/2$ each. For the even cycle types of $S_5$:
> - $3$-cycles: $|K| = \binom{5}{3} \cdot 2 = 20$, and $(4\,5)$ centralizes $(1\,2\,3)$: one class of size $20$;
> - double transpositions: $|K| = 5 \cdot 3 = 15$, and $(1\,2)$ centralizes $(1\,2)(3\,4)$: one class of size $15$;
> - $5$-cycles: $|K| = 5!/5 = 24$, and $C_{S_5}(g) = \langle g \rangle \subseteq A_5$: two classes of size $12$.
>
> With the identity this gives $1 + 20 + 15 + 12 + 12 = 60$, the worksheet's table.
>
> *Source: not from class*

^ex-44-1

> [!example] Example §44.2: Rotations by $\pm 90^\circ$
> $A = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$ and $B = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ are conjugate in $GL_2(\mathbb{R})$ but not in $SL_2(\mathbb{R})$. With $h = \begin{pmatrix} -1 & 0 \\ 0 & 1 \end{pmatrix}$ ($h^{-1} = h$, $\det h = -1$) one computes $hAh^{-1} = B$. Writing $z = \begin{pmatrix} a & c \\ b & d \end{pmatrix}$, the equation $zA = Az$ reads $\begin{pmatrix} -c & a \\ -d & b \end{pmatrix} = \begin{pmatrix} b & d \\ -a & -c \end{pmatrix}$, i.e. $b = -c$ and $a = d$; so
>
> $$ C_{GL_2(\mathbb{R})}(A) = \left\{ \begin{pmatrix} a & -b \\ b & a \end{pmatrix} : (a, b) \neq (0, 0) \right\}, $$
>
> all of determinant $a^2 + b^2 > 0$. Hence every element of $C_{GL_2(\mathbb{R})}(A)\,SL_2(\mathbb{R})$ has positive determinant, $h$ is not among them, and by the criterion ([[§44 Conjugacy in a Normal Subgroup#^prop-44-1|Proposition §44.1]], with $N = SL_2(\mathbb{R})$) $B$ is not conjugate to $A$ in $SL_2(\mathbb{R})$.
>
> *Source: PS 5.2(3)*

^ex-44-2
