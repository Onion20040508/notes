---
type: problem-set
subject: "[[Group Theory]]"
problem_set: 6
tags: [group-theory, math493]
---
← [[493 Problem Set 5]] · ↑ [[Group Theory]]

# Problem Set 6

*Submitted. Each problem is treated in the main text, at the location indicated.*

> [!question] Problem 6.1: Normality Is Not Transitive
> Let $G_3 = S_4$ and let $G_2$ be the Klein $4$-group $K = \{e, (1\,2)(3\,4), (1\,3)(2\,4), (1\,4)(2\,3)\} \subset S_4$ ([[§39 Sources of Normal Subgroups#^def-39-1|Klein four-group]]). Give an example of a subgroup $G_1$ of $K$ which is [[§38 Normal Subgroups#^def-38-1|normal]] in $K$, but which is not normal in $S_4$; so $G_1 \trianglelefteq G_2 \trianglelefteq G_3$ but $G_1$ is not normal in $G_3$.

^hw-6-1

*Treated in [[§39 Sources of Normal Subgroups|§39]] (Ex. [[§39 Sources of Normal Subgroups#^ex-39-4|§39.4]]).*

> [!question] Problem 6.2: Simple Abelian Groups
> Let $A$ be a non-trivial abelian group.
> 1. Show that every subgroup of $A$ is normal.
>
> Let $g$ be a nontrivial element of $A$.
> 2. If $\langle g \rangle g \neq A$, show that $A$ is not [[§43 Simple Groups#^def-43-1|simple]].
> 3. If the [[§4 Subgroups#^def-4-7|order]] of $g$ is infinite, show that $A$ is not simple.
> 4. If the order of $g$ is a finite composite number, show that $A$ is not simple.
>
> So the only case where $A$ is simple is $A = \langle g \rangle \cong \mathbb{Z}/p\mathbb{Z}$ for a prime $p$.

^hw-6-2

*Treated in [[§43 Simple Groups|§43]] (second proof of Theorem [[§43 Simple Groups#^thm-43-1|§43.1]]); (1) is [[§38 Normal Subgroups#^prop-38-1|§38.1]](1).*

> [!question] Problem 6.3: Groups of Order $p^2$
> Let $p$ be prime and $|G| = p^2$; by Problem 3.5 there is $z \neq e$ with $zg = gz$ for all $g \in G$.
> 1. Show that $z$ has order $p$ or $p^2$, and that if it has order $p^2$ then $G = \langle z \rangle \cong \mathbb{Z}/p^2\mathbb{Z}$.
>
> Assume now that $z$ has order $p$.
> 2. Show that $\langle z \rangle$ is normal in $G$ and $G/\langle z \rangle \cong \mathbb{Z}/p\mathbb{Z}$ ([[§40 Quotient Groups#^def-40-1|quotient group]]).
>
> Let $\bar g$ generate $G/\langle z \rangle$ and let $g$ be a preimage.
> 3. Show that $g^p = z^a$ for some $0 \leq a < p$.
> 4. If $a \neq 0$, show that $G = \langle g \rangle \cong \mathbb{Z}/p^2\mathbb{Z}$.
> 5. If $a = 0$, show that $G \cong \mathbb{Z}/p\mathbb{Z} \times \mathbb{Z}/p\mathbb{Z}$.

^hw-6-3

*Treated in [[§52 p-Groups and Sylow Subgroups|§52]] ([[§52 p-Groups and Sylow Subgroups#^thm-52-7|§52.7]], [[§52 p-Groups and Sylow Subgroups#^lem-52-6|§52.6]], [[§52 p-Groups and Sylow Subgroups#^cor-52-8|§52.8]]).*

> [!question] Problem 6.4: The Order of $GL_n(\mathbb{F}_p)$
> 1. Prove by induction on $k$ that the number of linearly independent $k$-tuples $(\vec v_1, \ldots, \vec v_k)$ in $\mathbb{F}_p^n$ is $(p^n - 1)(p^n - p) \cdots (p^n - p^{k-1})$.
> 2. Show that $|GL_n(\mathbb{F}_p)| = (p^n - 1)(p^n - p) \cdots (p^n - p^{n-1})$ ([[§3 Basic Examples of Groups#^def-3-6|general linear group]]).

^hw-6-4

*Treated in [[§52 p-Groups and Sylow Subgroups|§52]] ([[§52 p-Groups and Sylow Subgroups#^lem-52-2|§52.2]], [[§52 p-Groups and Sylow Subgroups#^lem-52-3|§52.3]], [[§52 p-Groups and Sylow Subgroups#^prop-52-4|§52.4]]).*
