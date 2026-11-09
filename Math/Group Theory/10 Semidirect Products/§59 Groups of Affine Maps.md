---
type: section
subject: "[[Group Theory]]"
chapter: 10
section: 59
tags: [group-theory, math493]
---
← [[§58 Semidirect Products]] · ↑ [[· 10 Semidirect Products]] · [[§60 Groups of Order pq as Semidirect Products]] →

*Source: Problem Set 9, Problem 9.5 (submitted). The examples after the proposition are not from class.*

Semidirect products appear concretely as groups of affine maps $x \mapsto gx + \lambda$ of a vector space: the translations form the normal subgroup, and the linear parts act on them.

> [!theorem] Proposition §59.1: Groups of Affine Maps Are Semidirect Products
> Let $V$ be a vector space over a field $k$, let $G$ be a subgroup of $GL(V)$, and let $L \subseteq V$ be a subgroup of the additive group of $V$ with $gL = L$ for each $g \in G$. For $g \in G$ and $\lambda \in L$ let $\sigma_{(g, \lambda)}: V \to V$, $\sigma_{(g, \lambda)}(x) = gx + \lambda$, and let $\Gamma = \{\sigma_{(g, \lambda)} : g \in G,\ \lambda \in L\}$.
>
> 1. $\Gamma$ is a group under composition, and
>
> $$
> \sigma_{(g_1, \lambda_1)} \circ \sigma_{(g_2, \lambda_2)} = \sigma_{(g_1 g_2,\ g_1\lambda_2 + \lambda_1)}.
> $$
>
> 2. $\varphi(g)(\lambda) = g\lambda$ defines a homomorphism $\varphi: G \to \operatorname{Aut}(L)$, and $\Psi(\lambda, g) = \sigma_{(g, \lambda)}$ is an isomorphism $L \rtimes_\varphi G \to \Gamma$ (Definition [[§58 Semidirect Products#^def-58-2|§58.2]]). So $\Gamma \cong L \rtimes G$, where $G$ acts on $L$ through its action on $V$.
>
> *Source: PS 9.5*

^prop-59-1

> [!proof]+ Proof
> *Idea:* Composing two affine maps multiplies the linear parts and adds the first linear part applied to the second translation, which is exactly the multiplication rule of $L \rtimes G$.
>
> *(Problem Set 9, Problem 9.5, as submitted.)* We use throughout that $gL = L$ for every $g \in G$.
>
> **(1)** *Closure.* Let $g_1, g_2 \in G$ and $\lambda_1, \lambda_2 \in L$. For $x \in V$, by linearity of $g_1$,
>
> $$
> \sigma_{(g_1, \lambda_1)} \circ \sigma_{(g_2, \lambda_2)}(x) = g_1(g_2 x + \lambda_2) + \lambda_1 = g_1 g_2\, x + (g_1\lambda_2 + \lambda_1).
> $$
>
> Here $g_1 g_2 \in G$ since $G$ is a group, $g_1 \lambda_2 \in g_1 L = L$, and $g_1\lambda_2 + \lambda_1 \in L$ since $L$ is closed under addition. Hence
>
> $$
> \sigma_{(g_1, \lambda_1)} \circ \sigma_{(g_2, \lambda_2)} = \sigma_{(g_1 g_2,\ g_1\lambda_2 + \lambda_1)} \in \Gamma. \tag{$\dagger$}
> $$
>
> *Identity.* Since $I \in G$ and $0 \in L$, $\sigma_{(I, 0)} \in \Gamma$, and $\sigma_{(I, 0)}(x) = x$ for all $x \in V$, so $\sigma_{(I, 0)} = \mathrm{id}_V$.
>
> *Inverses.* Let $g \in G$ and $\lambda \in L$. Then $g^{-1} \in G$, $g^{-1}\lambda \in g^{-1}L = L$, and $-g^{-1}\lambda \in L$ since $L$ is a subgroup; so $\sigma_{(g^{-1}, -g^{-1}\lambda)} \in \Gamma$. By $(\dagger)$,
>
> $$
> \begin{aligned}\sigma_{(g^{-1}, -g^{-1}\lambda)} \circ \sigma_{(g, \lambda)} &= \sigma_{(g^{-1}g,\ g^{-1}\lambda - g^{-1}\lambda)} = \sigma_{(I, 0)}, \\
> \sigma_{(g, \lambda)} \circ \sigma_{(g^{-1}, -g^{-1}\lambda)} &= \sigma_{(gg^{-1},\ -gg^{-1}\lambda + \lambda)} = \sigma_{(I, 0)}.\end{aligned}
> $$
>
> Hence $\sigma_{(g^{-1}, -g^{-1}\lambda)}$ is an inverse of $\sigma_{(g, \lambda)}$ in $\Gamma$.
>
> *Associativity.* Composition of functions is associative.
>
> Hence $\Gamma$ is a group under composition.
>
> **(2)** *The action.* Define $\varphi: G \to \operatorname{Aut}(L)$ by
>
> $$
> \varphi(g)(\lambda) = g\lambda \qquad (g \in G,\ \lambda \in L).
> $$
>
> For $g \in G$: since $gL = L$, $\varphi(g)$ maps $L$ onto $L$; it is injective since $g$ is invertible; and $g(\lambda + \mu) = g\lambda + g\mu$ by linearity of $g$. Hence $\varphi(g)$ is an automorphism of the additive group $L$. For $g_1, g_2 \in G$ and $\lambda \in L$,
>
> $$
> \varphi(g_1 g_2)(\lambda) = g_1(g_2\lambda) = \varphi(g_1)\big(\varphi(g_2)(\lambda)\big),
> $$
>
> so $\varphi$ is a group homomorphism. Thus $G$ acts on $L$ by $g \cdot \lambda = g\lambda$, and the external semidirect product $L \rtimes_\varphi G$ is the set of pairs $(\lambda, g)$ with $\lambda \in L$, $g \in G$, and multiplication
>
> $$
> (\lambda_1, g_1)(\lambda_2, g_2) = \big(\lambda_1 + \varphi(g_1)(\lambda_2),\ g_1 g_2\big) = \big(\lambda_1 + g_1\lambda_2,\ g_1 g_2\big).
> $$
>
> *The isomorphism.* Define
>
> $$
> \Psi: L \rtimes_\varphi G \to \Gamma, \qquad \Psi(\lambda, g) = \sigma_{(g, \lambda)}.
> $$
>
> By $(\dagger)$,
>
> $$
> \Psi(\lambda_1, g_1) \circ \Psi(\lambda_2, g_2) = \sigma_{(g_1, \lambda_1)} \circ \sigma_{(g_2, \lambda_2)} = \sigma_{(g_1 g_2,\ \lambda_1 + g_1\lambda_2)} = \Psi\big((\lambda_1, g_1)(\lambda_2, g_2)\big),
> $$
>
> so $\Psi$ is a homomorphism. It is surjective by the definition of $\Gamma$. For injectivity, suppose $\sigma_{(g, \lambda)} = \sigma_{(g', \lambda')}$. Evaluating at $x = 0$ gives $\lambda = \lambda'$, and then $gx = g'x$ for all $x \in V$, so $g = g'$. Hence $\Psi$ is an isomorphism, and
>
> $$
> \Gamma \cong L \rtimes_\varphi G,
> $$
>
> where $G$ acts on $L$ through its action on $V$: $g \cdot \lambda = g\lambda$.

^pf-59-1

The injectivity step shows that an element of $\Gamma$ determines its pair: $\lambda = \sigma_{(g, \lambda)}(0)$, and then $g$. So $g$ is well defined as the *linear part* of $\sigma_{(g, \lambda)}$, and $\lambda$ as its *translation part*.

> [!theorem] Proposition §59.2: Translations Form the Normal Subgroup
> In the setting of Proposition [[§59 Groups of Affine Maps#^prop-59-1|§59.1]], let $T = \{\sigma_{(I, \lambda)} : \lambda \in L\}$, the translations by elements of $L$, and $G_0 = \{\sigma_{(g, 0)} : g \in G\}$, the elements of $\Gamma$ fixing $0$.
>
> 1. The linear part $\ell: \Gamma \to G$, $\ell(\sigma_{(g, \lambda)}) = g$, is a surjective homomorphism with kernel $T$. So $T \trianglelefteq \Gamma$ and $\Gamma/T \cong G$.
> 2. Conjugating a translation by $\sigma_{(g, \lambda)}$ applies the linear part to the translation vector:
>
> $$
> \sigma_{(g, \lambda)} \circ \sigma_{(I, \mu)} \circ \sigma_{(g, \lambda)}^{-1} = \sigma_{(I, g\mu)}.
> $$
>
> 3. $\Gamma$ is the internal semidirect product of $T$ and $G_0$ (Definition [[§58 Semidirect Products#^def-58-1|§58.1]]).
>
> *Source: not from class*

^prop-59-2

> [!proof]+ Proof
> *Idea:* Everything follows from the composition rule $(\dagger)$ in the proof of Proposition [[§59 Groups of Affine Maps#^prop-59-1|§59.1]].
>
> *(Not from class; filled in.)* **(1)** $\ell$ is well defined by the remark before the proposition. By the composition rule of Proposition [[§59 Groups of Affine Maps#^prop-59-1|§59.1]](1), $\ell(\sigma_{(g_1, \lambda_1)} \circ \sigma_{(g_2, \lambda_2)}) = g_1g_2 = \ell(\sigma_{(g_1, \lambda_1)})\,\ell(\sigma_{(g_2, \lambda_2)})$, so $\ell$ is a homomorphism. It is surjective, since $\ell(\sigma_{(g, 0)}) = g$. Its kernel consists of the $\sigma_{(g, \lambda)}$ with $g = I$, which is $T$. So $T \trianglelefteq \Gamma$, as a kernel, and $\Gamma/T \cong G$ by the First Isomorphism Theorem (Theorem [[§41 The First and Second Isomorphism Theorems#^thm-41-1|§41.1]]).
>
> **(2)** By the proof of Proposition [[§59 Groups of Affine Maps#^prop-59-1|§59.1]](1), $\sigma_{(g, \lambda)}^{-1} = \sigma_{(g^{-1}, -g^{-1}\lambda)}$. Applying the composition rule twice,
>
> $$
> \sigma_{(I, \mu)} \circ \sigma_{(g^{-1}, -g^{-1}\lambda)} = \sigma_{(g^{-1},\ -g^{-1}\lambda + \mu)}, \qquad \sigma_{(g, \lambda)} \circ \sigma_{(g^{-1},\ -g^{-1}\lambda + \mu)} = \sigma_{(gg^{-1},\ g(-g^{-1}\lambda + \mu) + \lambda)} = \sigma_{(I, g\mu)}.
> $$
>
> **(3)** $T$ is normal by (1). $G_0$ is a subgroup: $\sigma_{(I, 0)} \in G_0$, $\sigma_{(g_1, 0)} \circ \sigma_{(g_2, 0)} = \sigma_{(g_1g_2, 0)}$ by the composition rule, and $\sigma_{(g, 0)}^{-1} = \sigma_{(g^{-1}, 0)}$ by the formula for inverses in (2). If $\sigma_{(I, \lambda)} = \sigma_{(g, 0)}$, then $\lambda = 0$ and $g = I$ by the remark before the proposition, so $T \cap G_0 = \{\mathrm{id}_V\}$. Finally, by the composition rule, every element of $\Gamma$ is a product
>
> $$
> \sigma_{(g, \lambda)} = \sigma_{(I, \lambda)} \circ \sigma_{(g, 0)} \in TG_0.
> $$

^pf-59-2

*Uses:* [[§59 Groups of Affine Maps#^prop-59-1|§59.1]], [[§41 The First and Second Isomorphism Theorems#^thm-41-1|§41.1]]

By (2), the conjugation action of $G_0$ on $T$ (Proposition [[§58 Semidirect Products#^prop-58-3|§58.3]]) is $\sigma_{(I, \mu)} \mapsto \sigma_{(I, g\mu)}$, which is the action $\varphi$ of Proposition [[§59 Groups of Affine Maps#^prop-59-1|§59.1]] under $\lambda \mapsto \sigma_{(I, \lambda)}$. So the internal description (3) and the external one agree, as Internal and External Semidirect Products Agree (Theorem [[§58 Semidirect Products#^thm-58-6|§58.6]]) predicts.

> [!example] Example §59.1: The Affine Group
> *(Not from class.)* Take $L = V$ and $G = GL(V)$; every invertible linear map maps $V$ onto $V$. Then $\Gamma$ is the group $\operatorname{Aff}(V)$ of all maps $x \mapsto gx + \lambda$ with $g \in GL(V)$ and $\lambda \in V$, and Proposition [[§59 Groups of Affine Maps#^prop-59-1|§59.1]] gives
>
> $$
> \operatorname{Aff}(V) \cong V \rtimes GL(V).
> $$
>
> For $V = k$ these are the maps $x \mapsto ax + b$ with $a \in k^\times$ and $b \in k$, so $\operatorname{Aff}(k) \cong k \rtimes k^\times$, with $k^\times$ acting on the additive group $k$ by multiplication. For $k = \mathbb{F}_p$ this group has $p(p-1)$ elements. For $p = 3$ it has $6$ elements and permutes the three elements of $\mathbb{F}_3$. Only the identity map fixes all three: $ax + b = x$ at $x = 0$ gives $b = 0$, and then at $x = 1$ gives $a = 1$. So the permutation homomorphism $\operatorname{Aff}(\mathbb{F}_3) \to S_{\mathbb{F}_3} \cong S_3$ is injective between groups of order $6$, hence an isomorphism:
>
> $$
> S_3 \cong \mathbb{F}_3 \rtimes \mathbb{F}_3^\times = \mathbb{Z}/3\mathbb{Z} \rtimes \{\pm 1\},
> $$
>
> with $-1$ acting by $x \mapsto -x$, as in Example [[§58 Semidirect Products#^ex-58-4|§58.4]].

^ex-59-1

> [!example] Example §59.2: The Symmetries of $\mathbb{Z}$ in $\mathbb{R}$
> *(Not from class.)* Take $V = \mathbb{R}$, $G = \{\pm 1\} \subseteq GL_1(\mathbb{R})$ and $L = \mathbb{Z}$, so that $\pm\mathbb{Z} = \mathbb{Z}$. Then $\Gamma$ consists of the translations $x \mapsto x + n$ and the maps $x \mapsto -x + n$, $n \in \mathbb{Z}$. The map $x \mapsto -x + n$ is the reflection of $\mathbb{R}$ in the point $n/2$, since it fixes $n/2$ and sends $n/2 + t$ to $n/2 - t$. By Proposition [[§59 Groups of Affine Maps#^prop-59-1|§59.1]], $\Gamma \cong \mathbb{Z} \rtimes \mathbb{Z}/2\mathbb{Z}$, with the generator of $\mathbb{Z}/2\mathbb{Z}$ acting by $n \mapsto -n$. This group is not abelian. By Proposition [[§59 Groups of Affine Maps#^prop-59-2|§59.2]](2), conjugating the translation $t(x) = x + 1$ by the reflection $s(x) = -x$ gives $sts^{-1} = t^{-1}$, the translation by $-1$. These are the symmetries of the integer points of the line, the infinite analogue of the symmetries of a regular polygon.

^ex-59-2

> [!example] Example §59.3: A Wallpaper Group with Rotations by $120^\circ$
> *(Not from class; the problem set illustrates the case with a tiling by lizards.)* Let $V = \mathbb{R}^2$, let $r$ be the rotation by $120^\circ$ about $0$, $G = \{I, r, r^2\} \cong \mathbb{Z}/3\mathbb{Z}$, and let
>
> $$
> L = \mathbb{Z}\omega_1 + \mathbb{Z}\omega_2, \qquad \omega_1 = (1, 0), \quad \omega_2 = \big(\tfrac12, \tfrac{\sqrt3}{2}\big),
> $$
>
> the triangular lattice. Then $r\omega_1 = (-\frac12, \frac{\sqrt3}{2}) = \omega_2 - \omega_1$ and $r\omega_2 = (-1, 0) = -\omega_1$, so $rL \subseteq L$. Hence also $r^2L \subseteq rL \subseteq L$, and $L = r^3L = r(r^2L) \subseteq rL$; so $gL = L$ for every $g \in G$. By Proposition [[§59 Groups of Affine Maps#^prop-59-1|§59.1]], $\Gamma \cong L \rtimes G \cong \mathbb{Z}^2 \rtimes \mathbb{Z}/3\mathbb{Z}$. It is the symmetry group of a pattern that has rotations by $120^\circ$ but no reflections, such as the figure below. In the classification of the seventeen wallpaper groups it is called $p3$.
>
> $\Gamma$ contains rotations about other points than $0$. Let $\lambda \in L$. Since $r$ has no nonzero fixed vector, $I - r$ is invertible, and with $c = (I - r)^{-1}\lambda$,
>
> $$
> \sigma_{(r, \lambda)}(x) - c = rx + (I - r)c - c = r(x - c).
> $$
>
> So $\sigma_{(r, \lambda)}$ is the rotation by $120^\circ$ about $c$. These centres are the $x = a\omega_1 + b\omega_2$ ($a, b \in \mathbb{R}$) with $(I - r)x \in L$. Since $(I - r)\omega_1 = 2\omega_1 - \omega_2$ and $(I - r)\omega_2 = \omega_1 + \omega_2$,
>
> $$
> (I - r)x = (2a + b)\,\omega_1 + (b - a)\,\omega_2,
> $$
>
> which lies in $L$ if and only if $2a + b$ and $b - a$ are integers. Then $3a = (2a + b) - (b - a) \in \mathbb{Z}$ and $b \in a + \mathbb{Z}$. So the centres of rotation are the points of
>
> $$
> L, \qquad c_1 + L, \qquad 2c_1 + L, \qquad c_1 = \tfrac13(\omega_1 + \omega_2):
> $$
>
> the lattice points and the centres of the two kinds of triangles of the lattice, those pointing up and those pointing down.

^ex-59-3

> [!remark]- Connections
> - The problem set's own picture is a tiling by lizards with the same group; the figure below uses an abstract motif.

![[m493-58-1.svg]]

*(Not from lecture; figure added.)* The wallpaper group $\Gamma = L \rtimes \mathbb{Z}/3\mathbb{Z}$ of Example [[§59 Groups of Affine Maps#^ex-59-3|§59.3]]. The blue motifs are the images $\gamma(F)$ of one motif $F$ under all $\gamma \in \Gamma$: at each lattice point (black) three copies, turned by $0^\circ$, $120^\circ$ and $240^\circ$. The arrows $\omega_1$, $\omega_2$ from the chosen origin $0$ (circled) span the translations $T \cong L$. Every element $\sigma_{(r, \lambda)}$ of $\Gamma$ is a rotation by $120^\circ$, about the point $(I - r)^{-1}\lambda$. These centres come in the three classes $L$ (black), $c_1 + L$ (red) and $2c_1 + L$ (orange), and the pattern looks the same when turned by $120^\circ$ about any of them. There is no mirror symmetry, because the motif is not symmetric.

> [!theorem] Corollary §59.3: Semidirect Products of Solvable Groups Are Solvable
> Let $\varphi: S \to \operatorname{Aut}(N)$ be a homomorphism. Then $N \rtimes_\varphi S$ is solvable if and only if $N$ and $S$ are solvable.
>
> *Source: not from class*

^cor-59-3

> [!proof]+ Proof
> *(Not from class; filled in.)* By Internal and External Semidirect Products Agree (Theorem [[§58 Semidirect Products#^thm-58-6|§58.6]](2)), $N \rtimes_\varphi S$ is the internal semidirect product of its subgroups $\tilde N \cong N$ and $\tilde S \cong S$, with $\tilde N$ normal. By The Quotient by $N$ (Proposition [[§58 Semidirect Products#^prop-58-1|§58.1]]), $(N \rtimes_\varphi S)/\tilde N \cong \tilde S \cong S$. Being solvable is preserved by isomorphisms, since an isomorphism carries a chain with abelian quotients to one. So by Corollary [[§48 Solvable Groups#^cor-48-8|§48.8]], $N \rtimes_\varphi S$ is solvable if and only if $\tilde N \cong N$ and $S$ are solvable.

^pf-59-3

*Uses:* [[§58 Semidirect Products#^thm-58-6|§58.6]], [[§58 Semidirect Products#^prop-58-1|§58.1]], [[§48 Solvable Groups#^cor-48-8|§48.8]]

All the groups of affine maps above are solvable, since in each of them $L$ and $G$ are abelian: $\operatorname{Aff}(k) \cong k \rtimes k^\times$, $\mathbb{Z} \rtimes \mathbb{Z}/2\mathbb{Z}$ and $\mathbb{Z}^2 \rtimes \mathbb{Z}/3\mathbb{Z}$.

> [!example] Example §59.4: Groups of Order $pq$ Are Solvable
> *(Not from class.)* Let $p < q$ be primes and $|G| = pq$. The number $n_q$ of Sylow $q$-subgroups divides $p$ and is $\equiv 1 \pmod q$ (The Number of Sylow Subgroups Divides $|G|$, Corollary [[§55 The Sylow Theorems#^cor-55-10|§55.10]]). Since $p < q$, the only divisor of $p$ that is $\equiv 1 \pmod q$ is $1$, so $n_q = 1$. The Sylow $q$-subgroup $Q$, which exists by the First Sylow Theorem (Theorem [[§55 The Sylow Theorems#^thm-55-4|§55.4]]), is therefore normal (A Normal Sylow Subgroup Is the Only One, Corollary [[§55 The Sylow Theorems#^cor-55-7|§55.7]](2)). $Q$ has prime order $q$ and $G/Q$ has prime order $p$. A group of prime order is cyclic, generated by any non-identity element by Lagrange's theorem, hence abelian and solvable. By Corollary [[§48 Solvable Groups#^cor-48-8|§48.8]], $G$ is solvable. This covers the case $q \equiv 1 \pmod p$ as well, where $G$ need not be cyclic (Example [[§55 The Sylow Theorems#^ex-55-4|§55.4]]).

^ex-59-4
