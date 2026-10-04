---
type: section
subject: "[[Measure Theory]]"
chapter: 1
section: 2
tags: [measure-theory, math551]
---
← [[§1 Countability and Set Theory]] · ↑ [[· 1 Set Theory Prerequisites]] · [[§3 Countability of Rationals and Unions]] →

> [!theorem] Theorem §2.1: Cantor–Bernstein
> Assume there exists an injection $f: X \to Y$ and an injection $g: Y \to X$. Then $X \sim Y$.

^thm-2-1

> [!remark] Remark
> An injection from $X$ to $Y$ shows that $X$ can be embedded into $Y$, i.e., $X$ is equivalent to a subset of $Y$. The Cantor–Bernstein theorem says that if each set can be embedded into the other, then they are equivalent.

^rem-2-1

> [!remark]- Connections
> - As a proof technique: [[Measure Theory Problem-Solving Techniques#^rem-19-6|Technique 2: The Cantor–Bernstein Squeeze]], applied in [[Measure Theory Problem-Solving Techniques#^ex-19-9|Ex. T2 (HW1)]].
> - Elementary version: [[§14 Counting Infinite Sets#^thm-14-14|250 Thm. §14.14]], with a complete proof by chains of images.

The proof relies on the following lemma.

> [!theorem] Lemma §2.2: Key Lemma for Cantor–Bernstein
> Let $f: X \to Y$ and $g: Y \to X$ be functions. Then there exist subsets $A \subseteq X$ and $B \subseteq Y$ such that $f(A) = B$ and $g(Y \setminus B) = X \setminus A$.

^lem-2-2

![[m551-2-1.svg]]
*What the lemma produces: cuts $X = A \sqcup A^c$ and $Y = B \sqcup B^c$ such that $f$ carries $A$ onto $B$ (blue) and $g$ carries $B^c$ onto $A^c$ (red). For injective $f$ and $g$ both restrictions are bijections, and the proof below glues them into $F = f$ on $A$, $F = g^{-1}$ on $A^c$ — a bijection $X \to Y$.*

> [!remark] Note: Notation
> For a subset $A \subseteq X$, we write $A^c = X \setminus A$ for the complement of $A$ in $X$.

^rem-2-2

> [!proof]+ Proof of Cantor–Bernstein assuming the Lemma
> Assume the [[§2 The Cantor–Bernstein Theorem#^lem-2-2|lemma]] holds. Let $f, g$ be injections and let $A \subseteq X$, $B \subseteq Y$ be as given by the lemma, so that:
> - $f(A) = B$
> - $g(B^c) = A^c$  (where $B^c = Y \setminus B$)
>
> Define $F: X \to Y$ by:
>
> $$
> F(x) = \begin{cases}
> f(x) & \text{if } x \in A \\
> g^{-1}(x) & \text{if } x \in A^c
> \end{cases}
> $$
>
> We claim $F$ is a bijection.
>
> **Step 1: $F$ is well-defined.**
>
> On $A$, we have $F(x) = f(x)$, which is well-defined since $f$ is a function.
>
> On $A^c$, we need $g^{-1}(x)$ to be well-defined. Since $g(B^c) = A^c$, for any $x \in A^c$, there exists $y \in B^c$ such that $g(y) = x$. Moreover, this $y$ is unique because $g$ is [[§1 Countability and Set Theory#^def-1-3|injective]]: if $g(y_1) = g(y_2) = x$, then $y_1 = y_2$. Thus $g^{-1}: A^c \to B^c$ is well-defined.
>
> **Step 2: $F$ is injective.**
>
> Let $x_1, x_2 \in X$ with $F(x_1) = F(x_2)$. We consider three cases.
>
> *Case 1:* $x_1, x_2 \in A$. Then $F(x_1) = f(x_1)$ and $F(x_2) = f(x_2)$. Since $f$ is injective, $f(x_1) = f(x_2)$ implies $x_1 = x_2$.
>
> *Case 2:* $x_1, x_2 \in A^c$. Then $F(x_1) = g^{-1}(x_1)$ and $F(x_2) = g^{-1}(x_2)$. If $g^{-1}(x_1) = g^{-1}(x_2)$, applying $g$ to both sides gives $x_1 = x_2$.
>
> *Case 3:* $x_1 \in A$ and $x_2 \in A^c$ (or vice versa). Then $F(x_1) = f(x_1) \in f(A) = B$ and $F(x_2) = g^{-1}(x_2) \in B^c$. Since $B \cap B^c = \emptyset$, we have $F(x_1) \neq F(x_2)$. This case cannot occur if $F(x_1) = F(x_2)$.
>
> Thus $F$ is injective.
>
> **Step 3: $F$ is surjective.**
>
> Let $y \in Y$. We show there exists $x \in X$ with $F(x) = y$.
>
> *Case 1:* $y \in B$. Since $f(A) = B$, there exists $x \in A$ such that $f(x) = y$. Then $F(x) = f(x) = y$.
>
> *Case 2:* $y \in B^c$. Let $x = g(y)$. Since $g(B^c) = A^c$, we have $x \in A^c$. Then $F(x) = g^{-1}(x) = g^{-1}(g(y)) = y$.
>
> Thus $F$ is [[§1 Countability and Set Theory#^def-1-4|surjective]].
>
> Since $F$ is a [[§1 Countability and Set Theory#^def-1-6|bijection]], we conclude $X \sim Y$.

^pf-2-1

*Uses:* [[§2 The Cantor–Bernstein Theorem#^lem-2-2|§2.2]], [[§1 Countability and Set Theory#^def-1-3|Def. §1.3]], [[§1 Countability and Set Theory#^def-1-4|Def. §1.4]], [[§1 Countability and Set Theory#^def-1-6|Def. §1.6]], [[§1 Countability and Set Theory#^def-1-7|Def. §1.7]]

> [!proof]+ Proof of the Lemma
> The strategy is to construct $A \subseteq X$ satisfying a certain property, then set $B = f(A)$.
>
> **Step 1: Define the collection $\mathcal{T}$.**
>
> Let
>
> $$
> \mathcal{T} = \{E \subseteq X \mid E \cap g(Y \setminus f(E)) = \emptyset\}.
> $$
>
> In words, $E \in \mathcal{T}$ if and only if $E$ is disjoint from $g(f(E)^c)$.
>
> Note that $\mathcal{T} \neq \emptyset$ since $\emptyset \in \mathcal{T}$: we have $\emptyset \cap g(Y \setminus f(\emptyset)) = \emptyset \cap g(Y) = \emptyset$.
>
> **Step 2: Define $A$ and show $A \in \mathcal{T}$.**
>
> Let $A = \bigcup_{E \in \mathcal{T}} E$.
>
> **Claim:** $A \in \mathcal{T}$, i.e., $A \cap g(Y \setminus f(A)) = \emptyset$.
>
> Suppose for contradiction that $A \cap g(Y \setminus f(A)) \neq \emptyset$. Let $x \in A \cap g(Y \setminus f(A))$.
>
> Since $x \in A = \bigcup_{E \in \mathcal{T}} E$, there exists $E_0 \in \mathcal{T}$ such that $x \in E_0$.
>
> Since $E_0 \subseteq A$, we have $f(E_0) \subseteq f(A)$, which implies $Y \setminus f(A) \subseteq Y \setminus f(E_0)$.
>
> Applying $g$ (which preserves subset relations): $g(Y \setminus f(A)) \subseteq g(Y \setminus f(E_0))$.
>
> Since $x \in g(Y \setminus f(A))$, we get $x \in g(Y \setminus f(E_0))$.
>
> But $E_0 \in \mathcal{T}$ means $E_0 \cap g(Y \setminus f(E_0)) = \emptyset$. Since $x \in E_0$, we must have $x \notin g(Y \setminus f(E_0))$.
>
> This is a contradiction. Therefore $A \cap g(Y \setminus f(A)) = \emptyset$, i.e., $A \in \mathcal{T}$.
>
> **Step 3: Define $B$ and verify the required properties.**
>
> Let $B = f(A)$. We need to show $g(Y \setminus B) = A^c$, i.e., $g(B^c) = A^c$.
>
> **Part (a): $g(B^c) \subseteq A^c$.**
>
> From Step 2, we have $A \cap g(Y \setminus f(A)) = \emptyset$, i.e., $A \cap g(B^c) = \emptyset$.
>
> This means $g(B^c) \subseteq A^c$.
>
> **Part (b): $A^c \subseteq g(B^c)$.**
>
> Suppose for contradiction that $A^c \not\subseteq g(B^c)$. Then there exists $x_0 \in A^c$ such that $x_0 \notin g(B^c) = g(Y \setminus f(A))$.
>
> Let $A_1 = A \cup \{x_0\}$. We claim $A_1 \in \mathcal{T}$, i.e., $A_1 \cap g(Y \setminus f(A_1)) = \emptyset$.
>
> To show this, we verify that both $A$ and $\{x_0\}$ are disjoint from $g(Y \setminus f(A_1))$.
>
> *For $A$:* Since $A \subseteq A_1$, we have $f(A) \subseteq f(A_1)$, so $Y \setminus f(A_1) \subseteq Y \setminus f(A)$.
>
> Thus $g(Y \setminus f(A_1)) \subseteq g(Y \setminus f(A))$.
>
> Since $A \cap g(Y \setminus f(A)) = \emptyset$ (from Step 2), we have $A \cap g(Y \setminus f(A_1)) = \emptyset$.
>
> *For $\{x_0\}$:* Since $f(A) \subseteq f(A_1)$, we have $Y \setminus f(A_1) \subseteq Y \setminus f(A)$, so $g(Y \setminus f(A_1)) \subseteq g(Y \setminus f(A))$.
>
> By choice of $x_0$, we have $x_0 \notin g(Y \setminus f(A))$.
>
> Therefore $x_0 \notin g(Y \setminus f(A_1))$, i.e., $\{x_0\} \cap g(Y \setminus f(A_1)) = \emptyset$.
>
> Combining: $A_1 \cap g(Y \setminus f(A_1)) = (A \cup \{x_0\}) \cap g(Y \setminus f(A_1)) = \emptyset$.
>
> Thus $A_1 \in \mathcal{T}$.
>
> But $A = \bigcup_{E \in \mathcal{T}} E$ is the union of *all* sets in $\mathcal{T}$. Since $A_1 \in \mathcal{T}$, we must have $A_1 \subseteq A$. In particular, $x_0 \in A$.
>
> This contradicts $x_0 \in A^c$. Therefore $A^c \subseteq g(B^c)$.
>
> **Conclusion:** We have shown $g(B^c) = A^c$ and $f(A) = B$ by definition. This completes the proof of the lemma.

^pf-2-2
