---
type: section
subject: "[[Functional Analysis]]"
chapter: 1
section: 2
tags: [functional-analysis, math556]
---
← [[§1 Linear Spaces]] · ↑ [[· 1 Linear Spaces]] · [[§3 Statement and Motivation]] →

*Stage: algebra — Threads: functionals, convexity. Introduces the two objects that [[· 2 The Hahn–Banach Theorem|Chapter 2]] connects.*

## Linear Maps and Isomorphisms

> [!definition] Definition §2.1: Linear Map
> Let $X, Y$ be linear spaces over the same field $\mathbb{F}$. A map $M : X \to Y$ is called a **linear map** if
>
> $$
> M(a_1 x_1 + a_2 x_2) = a_1 M(x_1) + a_2 M(x_2) \qquad \text{for all } x_1, x_2 \in X,\ a_1, a_2 \in \mathbb{F}.
> $$
>
> That is, $M$ preserves the linear operations.
>
> *Lax: Ch. 1, definition of linear map*

^def-2-1

> [!remark]- Connections
> - Linear maps in linear algebra: [[§7 Vector Space of Linear Maps#^ladr-3-1|LADR 3.1]].
> - With norms, the bounded ones: [[§21 Boundedness and Continuity#^def-21-2|Def. §21.2]].

> [!definition] Definition §2.2: Isomorphism
> A map $M : X \to Y$ is an **isomorphism** (or **linear isomorphism**) if $M$ is linear, one-to-one, and onto.
>
> *Lax: Ch. 1, definition of isomorphism; Remark 2*

^def-2-2

> [!remark]- Connections
> - Isomorphisms in linear algebra: [[§10 Invertibility and Isomorphisms#^ladr-3-69|LADR 3.69]].

> [!remark] Remark
> If there is an isomorphism $X \to Y$, the two linear spaces can be regarded as identical as far as the linear structure is concerned: every statement about linear combinations in $X$ transfers to $Y$ and back.

^rem-2-1

> [!theorem] Lemma §2.1: Inverse of an Isomorphism
> Let $A, B$ be linear spaces over the same field and $\varphi : A \to B$ an isomorphism. Then $\varphi^{-1} : B \to A$ is an isomorphism.
>
> *Source: HW1*

^lem-2-1

> [!proof]+ Proof
> $\varphi^{-1}$ exists and is bijective since $\varphi$ is. For linearity, let $u_1, u_2 \in B$, $a, b \in \mathbb{F}$, and set $v = a\,\varphi^{-1}(u_1) + b\,\varphi^{-1}(u_2) \in A$. By linearity of $\varphi$ and $\varphi \circ \varphi^{-1} = \mathrm{id}_B$,
>
> $$
> \varphi(v) = a\,\varphi(\varphi^{-1}(u_1)) + b\,\varphi(\varphi^{-1}(u_2)) = a u_1 + b u_2,
> $$
>
> and applying $\varphi^{-1}$ gives $\varphi^{-1}(a u_1 + b u_2) = v$, which is linearity of $\varphi^{-1}$. (From HW1.)

^pf-2-1

*Uses:* [[§2 Linear Maps, Convexity, and Linear Functionals#^def-2-2|Def. §2.2]], [[§2 Linear Maps, Convexity, and Linear Functionals#^def-2-1|Def. §2.1]]

> [!remark]- Connections
> - In linear algebra the same argument is part of the proof of [[§10 Invertibility and Isomorphisms#^ladr-3-63|LADR 3.63]] (the inverse of a bijective linear map is linear).

## Convex Sets

> [!definition] Definition §2.3: Convex Set
> Let $X$ be a linear space over $\mathbb{R}$. A set $K \subset X$ is called **convex** if for all $x_1, x_2 \in K$ and all $a \in [0, 1]$,
>
> $$
> a x_1 + (1 - a) x_2 \in K.
> $$
>
> *Lax: Ch. 1, definition of convex set*

^def-2-3

> [!remark]- Connections
> - Convex sets return through the gauge, [[§5 Convex Sets and the Gauge#^def-5-2|Def. §5.2]], and the separation theorem, [[§6 The Hyperplane Separation Theorem#^thm-6-1|§6.1]].

> [!remark] Remark
> As $a$ runs over $[0, 1]$, the point $a x_1 + (1 - a) x_2$ runs over the line segment from $x_2$ (at $a = 0$) to $x_1$ (at $a = 1$). So $K$ is convex if and only if it contains the segment joining any two of its points. Values $a > 1$ or $a < 0$ would leave the segment, continuing beyond $x_1$ or beyond $x_2$ respectively; these are excluded.

^rem-2-2

> [!definition] Definition §2.4: Convex Hull
> The **convex hull** of a subset $S \subset X$ is the smallest convex set containing $S$.
>
> *Lax: Ch. 1, definition of convex hull*

^def-2-4

> [!theorem] Proposition §2.2: The Smallest Convex Set Exists
> The intersection of any family of convex sets is convex, and the convex hull of $S$ is the intersection of all convex subsets of $X$ containing $S$.
>
> *Lax: Ch. 1, Thm 5(vi) and Thm 6(i)*

^prop-2-2

> [!proof]+ Proof
> Let $\{K_i\}$ be convex and $K = \bigcap_i K_i$. If $x_1, x_2 \in K$ and $a \in [0,1]$ then $a x_1 + (1-a) x_2 \in K_i$ for every $i$, so it lies in $K$. The family of convex sets containing $S$ is nonempty ($X$ is convex), and its intersection is convex, contains $S$, and is contained in every convex set containing $S$; it is therefore the convex hull.

^pf-2-2

*Uses:* [[§2 Linear Maps, Convexity, and Linear Functionals#^def-2-3|Def. §2.3]], [[§2 Linear Maps, Convexity, and Linear Functionals#^def-2-4|Def. §2.4]]

> [!example] Example §2.1: Convex Hull of a Star
> Let $S \subset \mathbb{R}^2$ be a four-pointed star (the boundary of the region obtained from a square by pushing the midpoints of its edges inward). The convex hull of $S$ is the filled square with the star's four tips as vertices. Indeed, taking any two tips, the whole segment between them must be included; taking any point of $S$ and any point already included, the segment between them must be included; iterating fills the square, which is itself convex.
>
> ![[m556-2-1.svg]]
> *Left: a convex set contains the segment (red) between any two of its points. Right: the star $S$ (solid) and its convex hull, the filled square on its four tips (shaded, dashed red edge) — the hull fills in the four notches, which no convex set containing the tips can avoid.*

^ex-2-1

## Linear Functionals

> [!definition] Definition §2.5: Linear Functional
> Let $X$ be a linear space over $\mathbb{F}$. A linear map $\ell : X \to \mathbb{F}$ is called a **linear functional** on $X$.
>
> *Lax: §3.1, definition of linear functional*

^def-2-5

> [!remark]- Connections
> - Linear functionals in linear algebra: [[§12 Duality#^ladr-3-108|LADR 3.108]].
> - With a norm, the bounded ones: [[§19 Bounded Linear Functionals and the Riesz Representation Theorem#^def-19-1|Def. §19.1]].

Here $\mathbb{F}$ is regarded as a one-dimensional linear space over itself, so a linear functional is simply a linear map into the scalars.

> [!example] Example §2.2: Linear Functionals on $\mathbb{R}^n$
> Let $a = (a_1, \ldots, a_n) \in \mathbb{R}^n$. Then
>
> $$
> \ell(x) = a_1 x_1 + \cdots + a_n x_n = a \cdot x, \qquad x = (x_1, \ldots, x_n),
> $$
>
> is a linear functional on $\mathbb{R}^n$. Conversely, *every* linear functional on $\mathbb{R}^n$ has this form: writing $x = \sum_{i=1}^n x_i e_i$ in the standard basis and setting $a_i = \ell(e_i)$, linearity gives
>
> $$
> \ell(x) = \sum_{i=1}^n x_i\, \ell(e_i) = \sum_{i=1}^n a_i x_i = a \cdot x.
> $$
>
> So on $\mathbb{R}^n$ a linear functional is determined by its $n$ values on a basis, and there is nothing else to say.

^ex-2-2

> [!remark]- Connections
> - The finite-dimensional Riesz representation: [[Riesz representation theorem|LADR 6.42]]; for bounded functionals on a Hilbert space: [[§19 Bounded Linear Functionals and the Riesz Representation Theorem#^thm-19-2|§19.2]].

> [!remark] Remark: Why Abstract Tools are Needed
> On $\mathbb{R}^n$ linear functionals are completely explicit because a basis is available. On a general linear space $X$ there is no such description: we do not even know the dimension, and there is no canonical way to write down a linear functional. The [[§3 Statement and Motivation#^thm-3-2|Hahn–Banach theorem]] below is the basic tool for *constructing* linear functionals on a general $X$.

^rem-2-3
