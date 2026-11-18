---
type: problem-set
subject: "[[Group Theory]]"
problem_set: 10
tags: [group-theory, math493]
---
← [[493 Problem Set 9]] · ↑ [[Group Theory]]

# Problem Set 10

*Due Thursday, November 19; submitted. Each problem is treated in the main text, at the location indicated.*

> [!question] Problem 10.1: Diagonalizability and Characters at the Inverse
> This problem is bumped from Worksheet 16, because we didn't have time to address it well in class. Let $G$ be a finite group and let $V$ be a finite dimensional representation of $G$ over the field $\mathbb{C}$. Let $g \in G$.
>
> 1. Show that there is a positive integer $N$ with $\rho_V(g)^N = 1$.
> 2. Show that $\rho_V(g)$ is diagonalizable and that the eigenvalues of $g$ are complex numbers of norm $1$.
> 3. Show that $\rho_V(g^{-1}) = \overline{\rho_V(g)}$, where the bar means complex conjugation.
>
> To keep this problem to a reasonable length, we won't do the real case. The corresponding result for real representations is that $\rho_V(g^{-1}) = \rho_V(g)$.

^hw-10-1

*Treated in [[§68 Homomorphisms Between Representations|§68]] (Proposition [[§68 Homomorphisms Between Representations#^prop-68-11|§68.11]]; for matrices, WS 16.4–16.5: Proposition [[§68 Homomorphisms Between Representations#^prop-68-9|§68.9]] and Corollary [[§68 Homomorphisms Between Representations#^cor-68-10|§68.10]]).*

> [!question] Problem 10.2: Annihilators and the Dual Representation
> Let $G$ be a group, let $V$ be a finite dimensional representation of $G$ and let $V^\vee$ be the dual representation. If $U$ is a vector subspace of $V$, then we define $U^\perp = \{\lambda \in V^\vee : \lambda(u) = 0\ \forall u \in U\}$.
>
> 1. If $U$ is a subrepresentation of $V$, show that $U^\perp$ is a subrepresentation of $V^\vee$.
> 2. Show that $\dim U^\perp = \dim V - \dim U$.
> 3. Let $V$ be a representation of $G$. Show that $V$ is simple if and only if $V^\vee$ is simple.

^hw-10-2

*Treated in [[§69 Dual Representations|§69]] (Definition [[§69 Dual Representations#^def-69-5|§69.5]], Propositions [[§69 Dual Representations#^prop-69-7|§69.7]] and [[§69 Dual Representations#^prop-69-8|§69.8]], Lemma [[§69 Dual Representations#^lem-69-9|§69.9]], Proposition [[§69 Dual Representations#^prop-69-10|§69.10]]).*

> [!question] Problem 10.3: $\operatorname{Hom}(V, W)$ as a Representation of $G \times H$
> Let $G$ and $H$ be finite groups. Let $V$ and $W$ be finite dimensional representations of $G$ and $H$ respectively (over the same field). Let $\operatorname{Hom}(V, W)$ be the set of linear maps $V \to W$. In this problem, we will investigate $\operatorname{Hom}(V, W)$ as a representation of $G \times H$. In this problem, we'll shorten $\operatorname{Hom}(V, W)$ to $X$.
>
> Let $G \times H$ act on $X$ by
>
> $$
> (g, h) \ast \alpha = \rho_W(h) \circ \alpha \circ \rho_V(g^{-1}).
> $$
>
> 1. Check that this is an action.
> 2. Show that $\chi_X(g, h) = \chi_V(g^{-1})\chi_W(h)$.
> 3. Assume that our field contains $\mathbb{Q}$. Show that
>
> $$
> \dim \operatorname{Hom}_{G \times H}(X, X) = \Big(\dim \operatorname{Hom}_G(V, V)\Big)\Big(\dim \operatorname{Hom}_H(W, W)\Big).
> $$
>
> 4. Suppose that our field is $\mathbb{C}$ and that $V$ and $W$ are simple representations of $G$ and $H$. Show that $X$ is a simple representation of $G \times H$.

^hw-10-3

*Treated in [[§70 Schur's Lemma and Multiplicities|§70]] (Definition [[§70 Schur's Lemma and Multiplicities#^def-70-3|§70.3]], Propositions [[§70 Schur's Lemma and Multiplicities#^prop-70-13|§70.13]], [[§70 Schur's Lemma and Multiplicities#^prop-70-14|§70.14]], [[§70 Schur's Lemma and Multiplicities#^prop-70-15|§70.15]] and [[§70 Schur's Lemma and Multiplicities#^prop-70-16|§70.16]]).*

> [!question] Problem 10.4: The Rotation Representation of $\mathbb{Z}/4\mathbb{Z}$
> Let $\mathbb{Z}/4\mathbb{Z}$ act on $\mathbb{R}^2$ by $\rho(k) = \left(\begin{smallmatrix} 0 & -1 \\ 1 & 0 \end{smallmatrix}\right)^k$.
>
> 1. Show that $\mathbb{R}^2$ is a simple representation of $\mathbb{Z}/4\mathbb{Z}$.
> 2. Show that $\operatorname{Hom}_{\mathbb{Z}/4\mathbb{Z}}(\mathbb{R}^2, \mathbb{R}^2)$ is $2$-dimensional, and give a basis for $\operatorname{Hom}_{\mathbb{Z}/4\mathbb{Z}}(\mathbb{R}^2, \mathbb{R}^2)$.
>
> Now, we switch from the ground field $\mathbb{R}$ to $\mathbb{C}$. Let $\mathbb{Z}/4\mathbb{Z}$ act on $\mathbb{C}^2$ by exactly the same formula: $\rho(k) = \left(\begin{smallmatrix} 0 & -1 \\ 1 & 0 \end{smallmatrix}\right)^k$.
>
> 3. Show that $\mathbb{C}^2$ is no longer simple, by explicitly writing down a nontrivial proper subrepresentation.
>
> If you want an additional challenge, generalize all of these results to $\mathbb{Z}/m\mathbb{Z}$ acting on $\mathbb{R}^2$ by $\rho(k) = \left(\begin{smallmatrix} \cos\frac{2\pi k}{m} & -\sin\frac{2\pi k}{m} \\ \sin\frac{2\pi k}{m} & \cos\frac{2\pi k}{m} \end{smallmatrix}\right)$, for any $m \geq 3$.

^hw-10-4

*Treated in [[§71 The Character Table|§71]] (Example [[§71 The Character Table#^ex-71-3|§71.3]]; the lecture's table is Example [[§71 The Character Table#^ex-71-2|§71.2]]). The additional challenge is not worked out.*
