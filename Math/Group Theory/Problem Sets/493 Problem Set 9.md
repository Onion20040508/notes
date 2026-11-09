---
type: problem-set
subject: "[[Group Theory]]"
problem_set: 9
tags: [group-theory, math493]
---
← [[493 Problem Set 8]] · ↑ [[Group Theory]]

# Problem Set 9

*Due Thursday, November 12; submitted. Each problem is treated in the main text, at the location indicated.*

> [!question] Problem 9.1: Extensions of Solvable Groups
> Let $G$ be a group with a normal subgroup $N$. Suppose that $N$ and $G/N$ are solvable; recall that this means that there are chains $\{1\} = N_0 \trianglelefteq N_1 \trianglelefteq N_2 \trianglelefteq \cdots \trianglelefteq N_a = N$ and $\{1\} = H_0 \trianglelefteq H_1 \trianglelefteq H_2 \trianglelefteq \cdots \trianglelefteq H_b = G/N$ such that all of the quotients $N_i/N_{i-1}$ and $H_j/H_{j-1}$ are abelian.
>
> Show that $G$ is solvable, so you will need to invent a chain of subgroups $\{1\} = G_0 \trianglelefteq G_1 \trianglelefteq \cdots \trianglelefteq G_c = G$ with $G_k/G_{k-1}$ abelian.

^hw-9-1

*Treated in [[§48 Solvable Groups|§48]] (Theorem [[§48 Solvable Groups#^thm-48-7|§48.7]]).*

> [!question] Problem 9.2: Idempotents
> Let $V$ be a vector space. A linear map $\pi: V \to V$ is called **idempotent** if $\pi^2 = \pi$. Show that, if $\pi$ is idempotent, then $V$ is the direct sum of $\operatorname{Ker}(\pi)$ and $\operatorname{Im}(\pi)$.

^hw-9-2

*Treated in [[§60 Direct Sums and Maschke's Theorem|§60]] (Lemma [[§60 Direct Sums and Maschke's Theorem#^lem-60-5|§60.5]], Proposition [[§60 Direct Sums and Maschke's Theorem#^prop-60-6|§60.6]]).*

> [!question] Problem 9.3: Maschke's Theorem
> In this problem, we prove Maschke's theorem. Let $G$ be a finite group and let $k$ be a field where $|G| \neq 0$. Let $W$ be a representation of $G$ and let $U$ be a subrepresentation. We must construct a second subrepresentation $V$ such that $W$ is the direct sum of $U$ and $V$.
>
> Let $P: W \to U$ be an idempotent with image $U$. We are not requiring that $P$ is a homomorphism of representations, just an idempotent linear map with image $U$.
>
> 1. Explain why such a $P$ exists. Hint: Just write down bases.
>
> Define
>
> $$
> \pi(w) = \frac{1}{|G|}\sum_{h \in G} h^{-1}P(hw).
> $$
>
> 2. Show that $\pi(u) = u$ for $u \in U$ and that $\operatorname{Im}(\pi) = U$. Show that $\pi$ is idempotent.
>
> Thus, by Problem 9.2, $W$ is the direct sum of $\operatorname{Ker}(\pi)$ and $\operatorname{Im}(\pi)$.
>
> 3. Show that $\pi$ is a homomorphism of representations, meaning that $\pi(gw) = g\pi(w)$ for all $g \in G$ and $w \in W$. Deduce that $\operatorname{Ker}(\pi)$ is a subrepresentation of $W$.

^hw-9-3

*Treated in [[§60 Direct Sums and Maschke's Theorem|§60]] (Lemmas [[§60 Direct Sums and Maschke's Theorem#^lem-60-8|§60.8]] and [[§60 Direct Sums and Maschke's Theorem#^lem-60-9|§60.9]], the proof of Theorem [[§60 Direct Sums and Maschke's Theorem#^thm-60-10|§60.10]]) and [[§59 Representations and Subrepresentations|§59]] (Proposition [[§59 Representations and Subrepresentations#^prop-59-4|§59.4]]).*

> [!question] Problem 9.4: When Maschke's Theorem Fails
> In this problem, we will see that Maschke's theorem becomes false when the hypotheses that $|G|$ is finite, or that $|G| \neq 0$ in $k$, are wrong.
>
> 1. Let $G = \mathbb{Z}$ and define $\rho: G \to GL_2(\mathbb{R})$ by $\rho(x) = \left(\begin{smallmatrix} 1 & x \\ 0 & 1 \end{smallmatrix}\right)$. Show that $\mathbb{R}\left(\begin{smallmatrix} 1 \\ 0 \end{smallmatrix}\right)$ is a subrepresentation of $\mathbb{R}^2$, but there is not a second subrepresentation $V$ with $\mathbb{R}^2 = \mathbb{R}\left(\begin{smallmatrix} 1 \\ 0 \end{smallmatrix}\right) \oplus V$.
> 2. Let $p$ be prime, let $G = \mathbb{Z}/p\mathbb{Z}$ and let $\mathbb{F} = \mathbb{Z}/p\mathbb{Z}$. Define $\rho: G \to GL_2(\mathbb{F})$ by $\rho(x) = \left(\begin{smallmatrix} 1 & x \\ 0 & 1 \end{smallmatrix}\right)$. Show that $\mathbb{F}\left(\begin{smallmatrix} 1 \\ 0 \end{smallmatrix}\right)$ is a subrepresentation of $\mathbb{F}^2$, but there is not a second subrepresentation $V$ with $\mathbb{F}^2 = \mathbb{F}\left(\begin{smallmatrix} 1 \\ 0 \end{smallmatrix}\right) \oplus V$.

^hw-9-4

*Treated in [[§60 Direct Sums and Maschke's Theorem|§60]] (Examples [[§60 Direct Sums and Maschke's Theorem#^ex-60-3|§60.3]] and [[§60 Direct Sums and Maschke's Theorem#^ex-60-4|§60.4]]).*

> [!question] Problem 9.5: Affine Maps and Semidirect Products
> In this problem, we will see a situation where we can understand semidirect products concretely in terms of matrices. Let $V$ be a vector space over a field $k$. Let $G$ be a subgroup of $GL(V)$ and let $L \subseteq V$ be a subgroup of the additive group of $V$ with the property that $gL = L$ for each $g \in G$. Define $\Gamma$ to be the set of affine linear transformations of the form $x \mapsto gx + \lambda$, for $g \in G$ and $\lambda \in L$.
>
> 1. Check that $\Gamma$ is a group (under composition).
> 2. Check that $\Gamma \cong L \rtimes G$ for a certain action of $G$ on $L$ and describe that action.
>
> The problem set illustrates this on its second page with a tiling of the plane by lizards. $V$ is that copy of $\mathbb{R}^2$, with the origin at a marked point in the centre of the image. $G$ is a copy of $\mathbb{Z}/3\mathbb{Z}$, acting by rotations by $120^\circ$ around that point, and $L$ consists of the translations which slide the lizards to themselves. Then $\Gamma$ is the full group of symmetries of the tiling, decomposed as $L \rtimes G$. (The problem set says “direct product” here; $L \rtimes G$ is a semidirect product.) This is one of seventeen “wallpaper” groups which mathematicians have classified.

^hw-9-5

*Treated in [[§58 Semidirect Products|§58]] (Proposition [[§58 Semidirect Products#^prop-58-8|§58.8]]; the lizard tiling's group in the form of Example [[§58 Semidirect Products#^ex-58-7|§58.7]]).*
