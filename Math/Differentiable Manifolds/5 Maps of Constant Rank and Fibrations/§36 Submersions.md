---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 5
section: 36
tags: [differentiable-manifolds, math591]
---
← [[§35 Local Diffeomorphisms]] · ↑ [[· 5 Maps of Constant Rank and Fibrations]] · [[§37 Regular Submanifolds]] →

*Stage: maps — Maps with surjective differentials: locally projections, by the normal form — the tool that makes the regular value theorem work on any manifold ([[§37 Regular Submanifolds|§37]]).*

> [!definition] Definition §36.1: Submersion
> Let $F : M \to N$ be smooth and $p \in M$. $F$ is a **submersion at $p$** if $F_{\ast p}$ is onto, and a **submersion** if it is a submersion at every point.
>
> *Lee: Ch. 4, Maps of Constant Rank*

^def-36-1

> [!remark]- Connections
> - Submersion at $p$ = regular point: [[§30 The Differential in Coordinates#^def-30-3|Def. §30.3]], [[§36 Submersions#^def-36-3|Def. §36.3]].

> [!definition] Definition §36.2: Immersion
> Let $F : M \to N$ be smooth and $p \in M$. $F$ is an **immersion at $p$** if $F_{\ast p}$ is injective, and an **immersion** if it is one at every point.
>
> *Lee: Ch. 4, Maps of Constant Rank*

^def-36-2

> [!remark]- Connections
> - The lecture's definition of immersion, with its normal form: [[§41 Immersions#^def-41-1|Def. §41.1]], [[§41 Immersions#^thm-41-1|§41.1]].

The submersion half is the lecture's definition. Immersions were listed as the third special type and treated in Lecture 13 ([[§41 Immersions|§41]]); the definition is recorded here in Lee's form so that the three types can be compared. In the language of Definition [[§30 The Differential in Coordinates#^def-30-3|§30.3]], $F$ is a submersion at $p$ exactly when $p$ is a regular point.

> [!theorem] Proposition §36.1: Dimension Constraints
> Let $F : M \to N$ be smooth, $m = \dim M$, $n = \dim N$, and $p \in M$.
> 1. If $F$ is a submersion at $p$ then $n \le m$; if $F$ is an immersion at $p$ then $m \le n$.
> 2. $F$ is a local diffeomorphism if and only if it is both a submersion and an immersion; in that case $m = n$.
> 3. If $m = n$ and $F$ is a submersion, or an immersion, at every point, then $F$ is a local diffeomorphism.
>
> *Lee: Proposition 4.8*

^prop-36-1

> [!proof]+ Proof
> Throughout, $F_{\ast p} : T_pM \to T_{F(p)}N$ is a linear map (Proposition [[§28 Derivations and the Abstract Tangent Space#^prop-28-5|§28.5]]) between spaces of dimensions $m$ and $n$ (Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-9|§29.9]]), so rank–nullity (Proposition [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]](1)) applies to it:
>
> $$
> m = \dim T_pM = \dim\ker F_{\ast p} + \operatorname{rank} F_{\ast p} .
> $$
>
> *(1)* By rank–nullity (Proposition [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]](1)), a surjective linear map $T_pM \to T_{F(p)}N$ forces $n \le m$, and an injective one forces $m \le n$. In detail: if $F$ is a submersion at $p$, then $F_{\ast p}$ is onto (Definition [[§36 Submersions#^def-36-1|§36.1]]), so $\operatorname{rank} F_{\ast p} = n$ and $m = \dim\ker F_{\ast p} + n \ge n$. If $F$ is an immersion at $p$, then $F_{\ast p}$ is injective (Definition [[§36 Submersions#^def-36-2|§36.2]]), so $\ker F_{\ast p} = 0$ and $m = \operatorname{rank} F_{\ast p} \le n$, the image being a subspace of the $n$-dimensional $T_{F(p)}N$.
>
> *(2)* By Theorem [[§35 Local Diffeomorphisms#^thm-35-2|§35.2]], $F$ is a local diffeomorphism if and only if $F_{\ast p}$ is bijective for every $p \in M$. A linear map is bijective if and only if it is injective and surjective, so this is Theorem [[§35 Local Diffeomorphisms#^thm-35-2|§35.2]]: “$F_{\ast p}$ surjective for every $p$” says that $F$ is a submersion, and “$F_{\ast p}$ injective for every $p$” that it is an immersion (Definitions [[§36 Submersions#^def-36-1|§36.1]] and [[§36 Submersions#^def-36-2|§36.2]]). Then (1) gives $m = n$: at any $p \in M$ (the claim tacitly assumes $M \neq \emptyset$), the submersion half gives $n \le m$ and the immersion half gives $m \le n$.
>
> *(3)* Between spaces of the same finite dimension, a linear map is injective iff surjective iff bijective (Proposition [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]](1)). So if $m = n$ and $F$ is a submersion at every point, each $F_{\ast p}$ is a surjection between spaces of the same dimension $m = n$, hence bijective; and if $F$ is an immersion at every point, each $F_{\ast p}$ is an injection between such spaces, hence again bijective. In either case apply Theorem [[§35 Local Diffeomorphisms#^thm-35-2|§35.2]]: $F$ is a local diffeomorphism.

^pf-36-1

*Uses:* [[§36 Submersions#^def-36-1|Def. §36.1]], [[§36 Submersions#^def-36-2|Def. §36.2]], [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]], [[§35 Local Diffeomorphisms#^thm-35-2|§35.2]], [[Fundamental theorem of linear maps|LADR 3.21]], [[Injectivity is equivalent to surjectivity (if dim V = dim W ＜ ∞)|LADR 3.65]], [[§28 Derivations and the Abstract Tangent Space#^prop-28-5|§28.5]], [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-9|§29.9]]

> [!example] Example §36.1: Projections Are Submersions
> The projection $\pi : \mathbb{R}^k \times \mathbb{R}^l \to \mathbb{R}^k$, $(x, y) \mapsto x$, is a submersion.

^ex-36-1

> [!proof]+ Proof
> $\pi$ is linear, hence smooth; we show that $\pi_{\ast a}$ is onto $T_{\pi(a)}\mathbb{R}^k$ for every $a \in \mathbb{R}^k \times \mathbb{R}^l = \mathbb{R}^{k+l}$ (Definition [[§36 Submersions#^def-36-1|§36.1]]). By Proposition [[§30 The Differential in Coordinates#^prop-30-5|§30.5]], applied with $W = \mathbb{R}^{k+l}$ and $F = \pi$, under the identifications $T_a\mathbb{R}^{k+l} \cong \mathbb{R}^{k+l}$ and $T_{\pi(a)}\mathbb{R}^k \cong \mathbb{R}^k$ the differential $\pi_{\ast a}$ is the Jacobian $\pi'(a)$. The components of $\pi$ are $\pi^i(r) = r^i$ for $i = 1, \ldots, k$, so $\partial \pi^i/\partial r^j(a) = \delta^i_j$ for $j = 1, \ldots, k+l$ (which is $0$ for every $j > k$), and row $i$ of the Jacobian is the $i$-th standard row vector (Definition [[§7 The Regular Value Theorem#^def-7-1|§7.1]]):
>
> $$
> \pi'(a) = \big(I_k \mid 0\big),
> $$
>
> a $k \times (k+l)$ matrix of rank $k$, since its first $k$ columns are the standard basis of $\mathbb{R}^k$. So $\pi'(a) : \mathbb{R}^{k+l} \to \mathbb{R}^k$ is onto, and $\pi_{\ast a}$, which corresponds to it under linear isomorphisms, is onto as well. As $a$ was arbitrary, $\pi$ is a submersion.

^pf-ex-36-1

*Uses:* [[§30 The Differential in Coordinates#^prop-30-5|§30.5]], [[§36 Submersions#^def-36-1|Def. §36.1]], [[§7 The Regular Value Theorem#^def-7-1|Def. §7.1]]

**Transcription note.** Page 28 of the handwritten notes writes the projection as $\mathbb{R}^m \times \mathbb{R}^l \to \mathbb{R}^k$; for a projection onto a factor the factor must be the target, $\mathbb{R}^k \times \mathbb{R}^l \to \mathbb{R}^k$. Projections of *product manifolds* $M_1 \times M_2 \to M_1$ are submersions for the same reason, but that needs the tangent space of a product — “they will be direct sums of tangent spaces” — which Uribe postponed to the next lecture.

Lecture 11 supplied it (Theorem [[§31 Tangent Vectors as Velocities of Curves#^thm-31-4|§31.4]]):

> [!example] Example §36.2: Projections of Product Manifolds Are Submersions
> The projection $\pi_1 : M_1 \times M_2 \to M_1$ is a submersion, and so is $\pi_2$.
>
> *Lee: Proposition 3.14*

^ex-36-2

> [!proof]+ Proof
> Fix $p = (p_1, p_2) \in M_1 \times M_2$, and let $\iota_1 = \iota^{p_2}$ and $\iota_2 = \iota^{p_1}$ be the slice inclusions through $p$ (Definition [[§19 Smooth Functions and Smooth Maps#^def-19-8|§19.8]]), as in Theorem [[§31 Tangent Vectors as Velocities of Curves#^thm-31-4|§31.4]]. We must show that $\pi_{1\ast} : T_p(M_1 \times M_2) \to T_{p_1}M_1$ is onto. Two identities are needed. First, $\pi_1 \circ \iota_1 = \mathrm{id}_{M_1}$, since $\pi_1(\iota_1(q)) = \pi_1(q, p_2) = q$; so the Chain Rule (Theorem [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]]), which also gives $(\mathrm{id})_\ast = \mathrm{id}$, yields $\pi_{1\ast}\iota_{1\ast} = \mathrm{id}$. Second, $\pi_1 \circ \iota_2$ is constant, $\pi_1(\iota_2(q)) = \pi_1(p_1, q) = p_1$; so its pushforward is zero (Lemma [[§28 Derivations and the Abstract Tangent Space#^lem-28-10|§28.10]]), and the Chain Rule yields $\pi_{1\ast}\iota_{2\ast} = (\pi_1 \circ \iota_2)_{\ast} = 0$. With the linearity of $\pi_{1\ast}$ (Proposition [[§28 Derivations and the Abstract Tangent Space#^prop-28-5|§28.5]]), for $v \in T_{p_1}M_1$ and $w \in T_{p_2}M_2$,
>
> $$
> \pi_{1\ast}\big(\Theta(v, w)\big) = \pi_{1\ast}\big(\iota_{1\ast}v + \iota_{2\ast}w\big) = \pi_{1\ast}\iota_{1\ast}v + \pi_{1\ast}\iota_{2\ast}w = v + 0 = v ,
> $$
>
> by the definition of $\Theta$ in Theorem [[§31 Tangent Vectors as Velocities of Curves#^thm-31-4|§31.4]] and the two identities; so $\pi_{1\ast}$ is onto $T_{p_1}M_1$: given $v$, the vector $\Theta(v, 0) = \iota_{1\ast}v$ is a preimage. As $p$ was arbitrary, $\pi_1$ is a submersion.
>
> For $\pi_2$ the same two arguments, with the indices $1$ and $2$ exchanged, give $\pi_{2\ast}\iota_{2\ast} = \mathrm{id}$ from $\pi_2 \circ \iota_2 = \mathrm{id}_{M_2}$, and $\pi_{2\ast}\iota_{1\ast} = 0$ from the constant map $\pi_2 \circ \iota_1$, with value $p_2$ (Lemma [[§28 Derivations and the Abstract Tangent Space#^lem-28-10|§28.10]]); hence
>
> $$
> \pi_{2\ast}\big(\Theta(v, w)\big) = \pi_{2\ast}\iota_{1\ast}v + \pi_{2\ast}\iota_{2\ast}w = 0 + w = w ,
> $$
>
> so $\Theta(0, w) = \iota_{2\ast}w$ is a preimage of any $w \in T_{p_2}M_2$, and $\pi_{2\ast}$ is onto.

^pf-ex-36-2

*Uses:* [[§19 Smooth Functions and Smooth Maps#^def-19-8|Def. §19.8]], [[§31 Tangent Vectors as Velocities of Curves#^thm-31-4|§31.4]], [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]], [[§28 Derivations and the Abstract Tangent Space#^lem-28-10|§28.10]], [[§28 Derivations and the Abstract Tangent Space#^prop-28-5|§28.5]]

The projection $S^{2n+1} \to \mathbb{CP}^n$, a submersion, is collected in [[§44 Projective Spaces and the Hopf Fibration|§44]].

> [!definition] Definition §36.3: Regular Points and Critical Points
> Let $F : M \to N$ be smooth, with $\dim M = m$ and $\dim N = n$.
> 1. $p \in M$ is a **regular point** of $F$ if $F$ is a submersion at $p$, i.e. $F_{\ast p}$ is onto — which forces $n \le m$. Otherwise $p$ is a **critical point**, also called a **singular point**.

^def-36-3

> [!remark]- Connections
> - The two earlier definitions of regular point: [[§7 The Regular Value Theorem#^def-7-3|Def. §7.3]] (Euclidean, Lecture 3) and [[§30 The Differential in Coordinates#^def-30-3|Def. §30.3]] (manifolds, via rank).

> [!definition] Definition §36.4: Regular Values and Critical Values
> Let $F : M \to N$ be smooth, with $\dim M = m$ and $\dim N = n$.
> 2. $q \in N$ is a **regular value** of $F$ if $F$ is a submersion at every $p \in F^{-1}(q)$, and a **critical value** otherwise.
> 3. In particular every $q \notin F(M)$ is a regular value: its preimage is empty, and “everything is true for the empty set.”
>
> These are the notions of Definitions [[§30 The Differential in Coordinates#^def-30-3|§30.3]] and [[§30 The Differential in Coordinates#^def-30-4|§30.4]], now with critical points and the empty-preimage convention made explicit; for maps between open subsets of Euclidean spaces they are those of Definitions [[§7 The Regular Value Theorem#^def-7-3|§7.3]] and [[§7 The Regular Value Theorem#^def-7-4|§7.4]].

^def-36-4

> [!remark]- Connections
> - The two earlier definitions of regular value: [[§7 The Regular Value Theorem#^def-7-4|Def. §7.4]] (Euclidean, Lecture 3) and [[§30 The Differential in Coordinates#^def-30-4|Def. §30.4]] (manifolds, via rank).

Uribe called (3) “kind of a trivial way to be [regular], but important”: it matters in Sard's theorem, about the set of regular values, which is still to come. **Transcription note.** Page 29 of the handwritten notes has “if $q \in \operatorname{Im} F$, then $q$ is regular”; the audio has “if $q$ is not in the image of $F$”, as in (3). The same page writes the preimage in (2) as $F^{-1}(p)$ for $F^{-1}(q)$.

> [!theorem] Proposition §36.2: Critical Points of Real-Valued Functions
> Let $f : M \to \mathbb{R}$ be smooth. Then $df_p$ is either onto or zero, so
>
> $$
> p \text{ is a critical point of } f \iff df_p = 0 \iff \frac{\partial f}{\partial x^i}(p) = 0 \text{ for all } i,
> $$
>
> in any chart at $p$.
>
> *Lee: Exercise 11.24*

^prop-36-2

> [!proof]+ Proof
> Here $N = \mathbb{R}$, so $n = 1$, and by Definition [[§36 Submersions#^def-36-3|§36.3]] $p$ is a critical point of $f$ exactly when $f_{\ast p} : T_pM \to T_{f(p)}\mathbb{R}$ is not onto.
>
> *The dichotomy.* The image of the linear map $df_p$ is a subspace of the one-dimensional $T_{f(p)}\mathbb{R} \cong \mathbb{R}$ (Definition [[§32 The Cotangent Space#^def-32-3|§32.3]]), so it is $0$ or everything — “dimensions of images cannot be fractional.” In detail: $df_p = \iota_{f(p)} \circ f_{\ast p}$ (Definition [[§32 The Cotangent Space#^def-32-5|§32.5]]), where $\iota_{f(p)} : T_{f(p)}\mathbb{R} \to \mathbb{R}$ is a linear isomorphism (Proposition [[§32 The Cotangent Space#^prop-32-1|§32.1]](3)). The image of $df_p$ is a subspace of $\mathbb{R}$, of dimension $0$ or $1$; so either $df_p = 0$ or $df_p$ is onto $\mathbb{R}$.
>
> *The first equivalence.* Since $\iota_{f(p)}$ is a bijection, $f_{\ast p}$ is onto $T_{f(p)}\mathbb{R}$ if and only if $df_p = \iota_{f(p)} \circ f_{\ast p}$ is onto $\mathbb{R}$. Hence
>
> $$
> p \text{ critical} \iff f_{\ast p} \text{ not onto} \iff df_p \text{ not onto} \iff df_p = 0 ,
> $$
>
> the last step by the dichotomy.
>
> *The second equivalence* is Lemma [[§33 Covectors in Coordinates#^lem-33-1|§33.1]]: in any chart at $p$, $df_p = \sum_i \partial f/\partial x^i(p)\, dx^i|_p$, and the $dx^i|_p$ form a basis of $T_p^{\ast}M$, so this combination is $0$ if and only if every coefficient $\partial f/\partial x^i(p)$ is $0$.

^pf-36-2

*Uses:* [[§36 Submersions#^def-36-3|Def. §36.3]], [[§32 The Cotangent Space#^def-32-4|Def. §32.4]], [[§33 Covectors in Coordinates#^lem-33-1|§33.1]], [[§32 The Cotangent Space#^def-32-3|Def. §32.3]], [[§32 The Cotangent Space#^def-32-5|Def. §32.5]], [[§32 The Cotangent Space#^prop-32-1|§32.1]]

> [!remark]- Connections
> - In $\mathbb{R}^n$, critical points are where extrema can occur: [[§17 Optimization and Lagrange Multipliers#^thm-17-1|452 §17.1]] (Fermat's theorem).

This is the definition of critical point Uribe sent to the class by email, and it agrees with Definition [[§7 The Regular Value Theorem#^def-7-3|§7.3]] for $m = 1$: there $p$ is regular iff $\nabla F(p) \ne 0$.

> [!definition] Definition §36.5: Critical Set
> Let $f : M \to \mathbb{R}$ be smooth. The **critical set** of $f$ is
>
> $$
> \operatorname{Crit}(f) = \{\, p \in M : df_p = 0 \,\},
> $$
>
> the set of critical points of $f$ in the sense of Definition [[§36 Submersions#^def-36-3|§36.3]], by Proposition [[§36 Submersions#^prop-36-2|§36.2]].

^def-36-5

*(Not from lecture: the notation of Assignment 5, Problem 3, used later, in [[§52 Critical Points and the Hessian|§52]].)*

> [!theorem] Proposition §36.3: Local Extrema Are Critical Points
> Let $f : M \to \mathbb{R}$ be smooth and $p \in M$. If $f$ has a local extremum at $p$ — $f(q) \le f(p)$ for all $q$ in some neighbourhood of $p$, or $f(q) \ge f(p)$ for all such $q$ — then $df_p = 0$, that is, $p \in \operatorname{Crit}(f)$.

^prop-36-3

> [!proof]+ Proof
> *(Not from lecture; filled in. The argument is the one of Assignment 5, Problem 4(b), where it is applied to the restriction of a function to a regular level set; it works on any manifold.)* By Definition [[§36 Submersions#^def-36-5|§36.5]] we must show $df_p = 0$, that is, $df_p(v) = 0$ for every $v \in T_pM$. Fix $v \in T_pM$. By Theorem [[§31 Tangent Vectors as Velocities of Curves#^thm-31-2|§31.2]] there is a smooth curve $\gamma : (-\varepsilon, \varepsilon) \to M$ with $\gamma(0) = p$ and $D_\gamma = v$. Let $W$ be a neighbourhood of $p$ — an open subset of $M$ containing $p$ (Definition [[§1 Point-Set Topology Review#^def-1-4|§1.4]]) — on which $f \le f(p)$ (or $f \ge f(p)$). As $\gamma$ is continuous, $\gamma^{-1}(W)$ is open in $(-\varepsilon, \varepsilon)$ and contains $0$, so it contains an interval $(-\delta, \delta)$; for $|t| < \delta$, $(f \circ \gamma)(t) \le f(p) = (f \circ \gamma)(0)$ (or $\ge$). So the function $f \circ \gamma$ of one variable, smooth by Lemma [[§19 Smooth Functions and Smooth Maps#^lem-19-5|§19.5]], has a local maximum (or minimum) at the interior point $0$, and its derivative there is $0$ (the one-variable fact: at an interior local extremum of a differentiable function the derivative vanishes). By Proposition [[§32 The Cotangent Space#^prop-32-2|§32.2]] and Definition [[§31 Tangent Vectors as Velocities of Curves#^def-31-2|§31.2]],
>
> $$
> df_p(v) = D_\gamma[f] = \frac{d}{dt}\Big|_{t=0} f\big(\gamma(t)\big) = (f \circ \gamma)'(0) = 0 .
> $$
>
> As $v$ was arbitrary, $df_p = 0$; by Proposition [[§36 Submersions#^prop-36-2|§36.2]], $p$ is a critical point of $f$.

^pf-36-3

*Uses:* [[§36 Submersions#^def-36-5|Def. §36.5]], [[§31 Tangent Vectors as Velocities of Curves#^thm-31-2|§31.2]], [[§1 Point-Set Topology Review#^def-1-4|Def. §1.4]], [[§19 Smooth Functions and Smooth Maps#^lem-19-5|§19.5]], [[§32 The Cotangent Space#^prop-32-2|§32.2]], [[§31 Tangent Vectors as Velocities of Curves#^def-31-2|Def. §31.2]], [[§36 Submersions#^prop-36-2|§36.2]]

> [!remark]- Connections
> - In $\mathbb{R}^n$: [[§17 Optimization and Lagrange Multipliers#^thm-17-1|Fermat's theorem in Rⁿ, 452 Thm. §17.1]]; in one variable: [[§29 The Mean Value Theorem#^thm-29-1|Interior Extremum Theorem, Single Variable Analysis §29.1]], [[Fermat's Theorem on Local Extrema|Calc hub]].

> [!theorem] Proposition §36.4: Submersions to $\mathbb{R}^k$ and Independent Differentials
> Let $G = (G^1, \ldots, G^k) : M \to \mathbb{R}^k$ be smooth, where $G^j = r^j \circ G$ for the standard coordinates $r^1, \ldots, r^k$ of $\mathbb{R}^k$, and let $p \in M$.
>
> 1. For every $v \in T_pM$,
>
> $$
> G_{\ast p}v = \sum_{j=1}^k dG^j|_p(v)\, \frac{\partial}{\partial r^j}\Big|_{G(p)} .
> $$
>
> 2. $G$ is a submersion at $p$ if and only if the covectors $dG^1|_p, \ldots, dG^k|_p$ are linearly independent in $T_p^{\ast}M$.

^prop-36-4

> [!proof]+ Proof
> *(Not from lecture. Assignment 5, Problem 4(b), at a point of a regular level set $G^{-1}(0)$: (1) and the direction ($\Rightarrow$) of (2) are the submitted solution's argument, written out; ($\Leftarrow$) is filled in. The Jacobian argument is the second proof below.)* Each $G^j = r^j \circ G$ is smooth, as a composite of smooth maps (Lemma [[§19 Smooth Functions and Smooth Maps#^lem-19-5|§19.5]]), so $dG^j|_p \in T_p^{\ast}M$ is defined.
>
> *(1) The components of $G_{\ast p}$.* For $v \in T_pM$, the vector $G_{\ast p}v \in T_{G(p)}\mathbb{R}^k$ is, by the universal formula of Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]] in the identity chart of $\mathbb{R}^k$, $G_{\ast p}v = \sum_j (G_{\ast p}v)[r^j]\, \partial/\partial r^j|_{G(p)}$, and its coefficients are, by the definition of the pushforward (Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-6|§28.6]]) and Proposition [[§32 The Cotangent Space#^prop-32-2|§32.2]],
>
> $$
> \big(G_{\ast p}v\big)[r^j] = v\big[r^j \circ G\big] = v\big[G^j\big] = dG^j|_p(v) .
> $$
>
> Substituting these coefficients gives the formula of (1).
>
> *(2), ($\Rightarrow$): linear independence, without coordinates.* Let $G$ be a submersion at $p$, so that $G_{\ast p}$ is onto $T_{G(p)}\mathbb{R}^k$ (Definition [[§36 Submersions#^def-36-1|§36.1]]). Suppose $\sum_{j=1}^k c_j\, dG^j|_p = 0$ for some $c = (c_1, \ldots, c_k) \in \mathbb{R}^k$; we show $c = 0$. Since $G_{\ast p}$ is onto, the vector $\sum_j c_j\, \partial/\partial r^j|_{G(p)}$ of $T_{G(p)}\mathbb{R}^k$ is $G_{\ast p}v$ for some $v \in T_pM$. Comparing with (1), and using that the coefficients of a vector in the basis $\partial/\partial r^j|_{G(p)}$ are unique (Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]]), $dG^j|_p(v) = c_j$ for every $j$. Evaluating the assumed relation at this $v$, with the pointwise operations of $T_p^{\ast}M$,
>
> $$
> 0 = \Big(\sum_{j=1}^k c_j\, dG^j|_p\Big)(v) = \sum_{j=1}^k c_j\, dG^j|_p(v) = \sum_{j=1}^k c_j^{\,2} = |c|^2 ,
> $$
>
> so $c = 0$. In the assignment's words: the relation says $c \cdot G_{\ast p}(v) = 0$ for every $v$, and since $G_{\ast p}$ is onto we may take $G_{\ast p}(v) = c$.
>
> *(2), ($\Leftarrow$).* Let $dG^1|_p, \ldots, dG^k|_p$ be linearly independent; we show that $G_{\ast p}$ is onto. Let $\Lambda : T_pM \to \mathbb{R}^k$, $\Lambda(v) = \big(dG^1|_p(v), \ldots, dG^k|_p(v)\big)$, a linear map since each $dG^j|_p$ is linear. By (1), $G_{\ast p} = \beta \circ \Lambda$, where $\beta : \mathbb{R}^k \to T_{G(p)}\mathbb{R}^k$, $\beta(c) = \sum_j c_j\, \partial/\partial r^j|_{G(p)}$, is a linear isomorphism, the $\partial/\partial r^j|_{G(p)}$ being a basis (Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]]); so $G_{\ast p}$ is onto if and only if $\Lambda$ is. Suppose $\Lambda$ were not onto. Its image $E$ is then a subspace of $\mathbb{R}^k$ of some dimension $d < k$; choose a basis $a_1, \ldots, a_d$ of $E$ and let $B$ be the $d \times k$ matrix with rows $a_1^{\mathsf T}, \ldots, a_d^{\mathsf T}$. By rank–nullity (Proposition [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]](1)) for $B : \mathbb{R}^k \to \mathbb{R}^d$, $\dim\ker B \ge k - d \ge 1$, so there is $c \neq 0$ with $Bc = 0$, that is, $a_i \cdot c = 0$ for every $i$, and hence $w \cdot c = 0$ for every $w \in E$, by linearity of the dot product. Then for every $v \in T_pM$,
>
> $$
> \Big(\sum_{j=1}^k c_j\, dG^j|_p\Big)(v) = \sum_{j=1}^k c_j\, dG^j|_p(v) = c \cdot \Lambda(v) = 0 ,
> $$
>
> as $\Lambda(v) \in E$; so $\sum_j c_j\, dG^j|_p = 0$ with $c \neq 0$, contradicting the independence. Hence $\Lambda$, and with it $G_{\ast p}$, is onto: $G$ is a submersion at $p$ (Definition [[§36 Submersions#^def-36-1|§36.1]]).

^pf-36-4

*Uses:* [[§19 Smooth Functions and Smooth Maps#^lem-19-5|§19.5]], [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]], [[§28 Derivations and the Abstract Tangent Space#^def-28-6|Def. §28.6]], [[§32 The Cotangent Space#^prop-32-2|§32.2]], [[§36 Submersions#^def-36-1|Def. §36.1]], [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]]

> [!proof]+ Second proof of (2), by the Jacobian
> *(The second independence argument of the submitted solution, Assignment 5, Problem 4(b), run in both directions.)* Fix any chart $(U, \varphi = (x^1, \ldots, x^m))$ of $M$ at $p$, and let $J$ be the $k \times m$ matrix with entries $J_{ji} = \partial G^j/\partial x^i(p)$. By Lemma [[§33 Covectors in Coordinates#^lem-33-1|§33.1]], $dG^j|_p = \sum_{i=1}^m J_{ji}\, dx^i|_p$: row $j$ of $J$ holds the components of $dG^j|_p$. Hence, for $c \in \mathbb{R}^k$, collecting the coefficient of each $dx^i|_p$,
>
> $$
> \sum_{j=1}^k c_j\, dG^j|_p = \sum_{i=1}^m \Big(\sum_{j=1}^k c_j J_{ji}\Big) dx^i|_p ,
> $$
>
> and since the $dx^i|_p$ form a basis of $T_p^{\ast}M$ (Lemma [[§33 Covectors in Coordinates#^lem-33-1|§33.1]]), this is $0$ if and only if $\sum_j c_j J_{ji} = 0$ for every $i$, that is, $J^{\mathsf T} c = 0$. So the $dG^j|_p$ are linearly independent if and only if $\ker J^{\mathsf T} = 0$. Next, $J$ is the matrix of $G_{\ast p}$ in the bases $\partial/\partial x^i|_p$ and $\partial/\partial r^j|_{G(p)}$: by (1) with $v = \partial/\partial x^i|_p$ and Proposition [[§32 The Cotangent Space#^prop-32-2|§32.2]], which gives $dG^j|_p(\partial/\partial x^i|_p) = \partial G^j/\partial x^i(p)$, we have $G_{\ast p}(\partial/\partial x^i|_p) = \sum_j J_{ji}\, \partial/\partial r^j|_{G(p)}$, so the $i$-th column of $J$ holds the coordinates of the image of the $i$-th basis vector (Proposition [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]](3)). Therefore
>
> $$
> G \text{ submersion at } p \iff \operatorname{rank} G_{\ast p} = k \iff \operatorname{rank} J = k \iff \operatorname{rank} J^{\mathsf T} = k \iff \ker J^{\mathsf T} = 0 \iff dG^1|_p, \ldots, dG^k|_p \text{ independent}.
> $$
>
> The first equivalence holds because $G_{\ast p}$ is onto the $k$-dimensional $T_{G(p)}\mathbb{R}^k$ (Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]]) exactly when its image has dimension $k$, a subspace of the same finite dimension being the whole space; the second and third because the rank of a linear map is the rank of its matrix, which equals the rank of the transpose (Proposition [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]](3)); the fourth by rank–nullity for $J^{\mathsf T} : \mathbb{R}^k \to \mathbb{R}^m$ (Proposition [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]](1)), $\dim\ker J^{\mathsf T} = k - \operatorname{rank} J^{\mathsf T}$; and the last by the first part of this proof.

^pf-36-4-2

*Uses:* [[§33 Covectors in Coordinates#^lem-33-1|§33.1]], [[§32 The Cotangent Space#^prop-32-2|§32.2]], [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]], [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]]

> [!theorem] Lemma §36.5: Diffeomorphisms onto Open Sets Are Charts
> Let $U \subseteq M$ be open and $\hat\varphi : U \to \mathbb{R}^m$ smooth, with $\hat\varphi(U)$ open and $\hat\varphi : U \to \hat\varphi(U)$ a diffeomorphism. Then $(U, \hat\varphi)$ is a smooth chart of $M$.
>
> *Lee: cf. Ch. 2, Diffeomorphisms*

^lem-36-5

> [!proof]+ Proof
> *It is a chart.* $\hat\varphi : U \to \hat\varphi(U)$ is a diffeomorphism, so it is a bijection that is continuous with continuous inverse (smooth maps are continuous, Definition [[§19 Smooth Functions and Smooth Maps#^def-19-3|§19.3]]): it is a homeomorphism onto an open subset of $\mathbb{R}^m$, so it is a chart (Definition [[§17 Differentiable Structures#^def-17-1|§17.1]]).
>
> *It is compatible with every smooth chart.* Let $(W, \chi)$ be any smooth chart of $M$; if $U \cap W = \emptyset$ there is nothing to check (Definition [[§17 Differentiable Structures#^def-17-4|§17.4]]). Otherwise the transition maps are
>
> $$
> \hat\varphi \circ \chi^{-1} : \chi(U \cap W) \to \hat\varphi(U \cap W), \qquad \chi \circ \hat\varphi^{-1} : \hat\varphi(U \cap W) \to \chi(U \cap W) .
> $$
>
> The first is the coordinate representation of the smooth map $\hat\varphi$, restricted to the open set $U \cap W$, in the charts $(U \cap W, \chi|_{U \cap W})$ of $M$ and $(\hat\varphi(U), \mathrm{id})$ of the open set $\hat\varphi(U) \subseteq \mathbb{R}^m$; the second is the coordinate representation of the smooth map $\hat\varphi^{-1}$ in the charts $(\hat\varphi(U \cap W), \mathrm{id})$ and $(U \cap W, \chi|_{U \cap W})$. Both are smooth, because these maps are (Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-2|§19.2]], which allows any pair of smooth charts). They are inverse to each other, so the transition function is a diffeomorphism, and $(U, \hat\varphi)$ is compatible with $(W, \chi)$.
>
> *Conclusion.* So $(U, \hat\varphi)$ is compatible with every chart of the maximal atlas $\mathcal{A}$ of $M$, and therefore belongs to it (Theorem [[§17 Differentiable Structures#^thm-17-5|§17.5]]): the set $\overline{\mathcal{A}}$ of charts compatible with every chart of $\mathcal{A}$ is the unique maximal atlas containing $\mathcal{A}$, which is $\mathcal{A}$ itself.

^pf-36-5

*Uses:* [[§19 Smooth Functions and Smooth Maps#^prop-19-2|§19.2]], [[§17 Differentiable Structures#^thm-17-5|§17.5]], [[§19 Smooth Functions and Smooth Maps#^def-19-3|Def. §19.3]], [[§17 Differentiable Structures#^def-17-1|Def. §17.1]], [[§17 Differentiable Structures#^def-17-4|Def. §17.4]]

> [!theorem] Theorem §36.6: Local Normal Form for Submersions
> Let $F : M \to N$ be a submersion at $p$, with $\dim M = m$ and $\dim N = n$. Then there are charts $(U, \varphi)$ at $p$ and $(V, \psi)$ at $F(p)$ with $F(U) \subseteq V$ in which the coordinate representation $\tilde F = \psi \circ F \circ \varphi^{-1} : \varphi(U) \to \psi(V)$ is the projection onto the first $n$ coordinates:
>
> $$
> \tilde F\big(r^1, \ldots, r^m\big) = \big(r^1, \ldots, r^n\big).
> $$
>
> Equivalently, with coordinate functions $x^i = r^i \circ \varphi$ on $U$ and $y^j = r^j \circ \psi$ on $V$: $\;y^j \circ F = x^j$ on $U$ for $j = 1, \ldots, n$. In particular $n \le m$.
>
> *Lee: Theorem 4.12, the rank theorem*

^thm-36-6

> [!remark]- Connections
> - The counterpart for immersions: [[§41 Immersions#^thm-41-1|§41.1]]. The main application: the regular value theorem for manifolds, [[§37 Regular Submanifolds#^thm-37-12|§37.12]].

Stated in Lecture 10 and proved in Lecture 11, below. The inequality $n \le m$ needs no theorem — a surjective linear map cannot raise dimension — but the normal form does: it says that every submersion, in suitable coordinates, *is* a projection.

![[m591-14-3.svg]]
*The normal form as a square: in the charts $\varphi$ and $\psi$ of the theorem, $F$ becomes the projection $(r^1, \ldots, r^m) \mapsto (r^1, \ldots, r^n)$.*

![[m591-14-4.svg]]
*What the normal form says, for $m = 2$ and $n = 1$. Left: near $p$ the fibres $F^{-1}(c)$ of a submersion are curves, one through each point, which $F$ collapses to the points of an interval. Right: in the charts of the theorem the fibres are straightened into vertical lines, and $\tilde F$ forgets the second coordinate. Every submersion looks, locally and up to a change of coordinates, like the projection of Example [[§36 Submersions#^ex-36-1|§36.1]].*

*Lecture 11. “Back to submersions.” Uribe now made the vocabulary official, with the letters matched to the dimensions: $\dim M = m$ and $\dim N = n$. (In [[§7 The Regular Value Theorem|§7]], following the earlier lecture, $F : \mathbb{R}^N \to \mathbb{R}^m$ had $m$ as the dimension of the target.)*

Uribe singled out Lemma [[§36 Submersions#^lem-36-5|§36.5]] as “an intellectual step that should not be overlooked”: in the proof below, a map is shown to be a local diffeomorphism, and this lemma is what makes it a coordinate system.

> [!proof]+ Proof (Lecture 11)
> The steps are the lecture's, in the lecture's order. Sentences marked *(Completion.)* fill in details the lecture passed over.
>
> *1. Start with any coordinates.* “I start with any coordinates”: smooth charts $(U_0, \varphi_0 = (x^1, \ldots, x^m))$ at $p$ and $(V, \psi = (y^1, \ldots, y^n))$ at $F(p)$ with $F(U_0) \subseteq V$. *(Completion.)* Such charts exist by Lemma [[§19 Smooth Functions and Smooth Maps#^lem-19-3|§19.3]], applied to $F$ at $p$: take any charts and replace $U_0$ by the open set $U_0 \cap F^{-1}(V)$, open because $F$ is continuous, and $\varphi_0$ by its restriction, again a smooth chart (Lemma [[§17 Differentiable Structures#^lem-17-6|§17.6]](1)).
>
> *2. The components and their matrix.* As before, define the components of $F$, $F^j = y^j \circ F : U_0 \to \mathbb{R}$. The submersion condition says that the matrix
>
> $$
> J = \Big[\frac{\partial F^j}{\partial x^i}(p)\Big]
> $$
>
> has rank $n$. It “has $m$ columns, which are the $x$'s, and $n$ rows, that are the gradients” of the $F^j$. *(Completion.)* By Theorem [[§30 The Differential in Coordinates#^thm-30-2|§30.2]], $J$ is the matrix of $F_{\ast p}$ in the coordinate bases, and $F_{\ast p}$ is onto, so $J$ has rank $n$: the rank of $F_{\ast p}$ is $\dim T_{F(p)}N = n$ (Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-9|§29.9]]), and the rank of a linear map is the rank of its matrix (Proposition [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]](3)).
>
> *3. “It's the same matrix.”* A student asked whether the matrix should be written with $\tilde F$. Uribe: “It's the same thing… That's how we define partials. We define them by going downstairs and taking the ordinary partial derivative downstairs. So it's the same matrix.” That is Proposition [[§30 The Differential in Coordinates#^prop-30-1|§30.1]]: writing $G = \psi \circ F \circ \varphi_0^{-1}$ for the coordinate representation in these first charts (the lecture's $\tilde F$ at this stage),
>
> $$
> \frac{\partial F^j}{\partial x^i}(p) = \frac{\partial G^j}{\partial r^i}\big(\varphi_0(p)\big), \qquad J = G'\big(\varphi_0(p)\big).
> $$
>
> *(Completion.)* The same proposition gives the identity of functions $F^j \circ \varphi_0^{-1} = G^j$ on $\varphi_0(U_0)$, used in step 7.
>
> *4. Reindex — “the only thing we need to do.”* $J$ has $n$ linearly independent columns; “I just put them at the beginning.” *(Completion.)* The rank of a matrix is the dimension of its column space, so among the $m$ columns of $J$, which has rank $n$, some $n$ are linearly independent. Rearranging the $x^i$, we can write $J$ in block form
>
> $$
> J = \big(\, A \ \big|\ B \,\big), \qquad A \text{ an } n \times n \text{ non-singular matrix}, \quad B \text{ of size } n \times (m - n),
> $$
>
> where $B$ is “the stuff that remains here that I'm not going to care about.” *(Completion.)* $A$ consists of the $n$ independent columns, so it is a square matrix with independent columns, hence non-singular. Rearranging the coordinates replaces $\varphi_0$ by $P \circ \varphi_0$ for a permutation $P$ of $\mathbb{R}^m$. This is again a smooth chart, by Lemma [[§17 Differentiable Structures#^lem-17-6|§17.6]](2) with $h = P$: a linear isomorphism of $\mathbb{R}^m$, hence a diffeomorphism of $\mathbb{R}^m$ onto itself (it and its inverse $P^{-1}$ are linear, hence smooth), defined on all of $\mathbb{R}^m \supseteq \varphi_0(U_0)$. It permutes the columns of $J$ in the same way. From now on $\varphi_0 = (x^1, \ldots, x^m)$, $G$ and $J$ denote the rearranged chart, its coordinate representation, and its matrix.
>
> *5. The coordinates we want.* “The thing to do, you see, is to take the first $n$ components of $F$ as the first $n$ coordinate functions, and then we keep the remaining ones”:
>
> $$
> \hat\varphi = \big(F^1, \ldots, F^n, x^{n+1}, \ldots, x^m\big) : U_0 \to \mathbb{R}^m .
> $$
>
> *(Completion.)* This makes sense because $n \le m$ — the theorem's “in particular”, true since $F_{\ast p}$ is onto (Proposition [[§36 Submersions#^prop-36-1|§36.1]]) — so there are $m - n \ge 0$ remaining coordinates. $\hat\varphi$ is smooth because its components are. It has $m$ components, so it maps into $\mathbb{R}^m$ (see the transcription note below).
>
> *6. The claim.* $\hat\varphi$ is a local diffeomorphism in a neighbourhood of $p$.
>
> *7. The Jacobian of $\hat\varphi$ in the old coordinates.* “Gradient across”: the first $n$ rows are the gradients of $F^1, \ldots, F^n$, which give the matrix $J = (A \mid B)$; the last $m - n$ rows are the gradients of $x^{n+1}, \ldots, x^m$. These give the $(m-n) \times (m-n)$ identity, and zero in the first $n$ columns, “because I would be taking partials of these $x$'s with respect to $x$'s that come before.” So
>
> $$
> \begin{pmatrix} A & B \\ 0 & I_{m-n} \end{pmatrix},
> $$
>
> and “by the block nature, the fact that we have a big zero there, this is non-degenerate” at $p$: its determinant is $\det A \ne 0$. *(Completion.)* “The Jacobian of $\hat\varphi$ in the $x$-coordinates” is the Jacobian at $\varphi_0(p)$ of the ordinary map $H = \hat\varphi \circ \varphi_0^{-1} : \varphi_0(U_0) \to \mathbb{R}^m$. Its rows are the partials of the components of $\hat\varphi$ by Proposition [[§30 The Differential in Coordinates#^prop-30-1|§30.1]], applied with the identity chart on $\mathbb{R}^m$, and $\partial x^k/\partial x^i = \delta^k_i$ gives the identity and zero blocks. Concretely, for $r \in \varphi_0(U_0)$ put $q = \varphi_0^{-1}(r)$; then $F^j(q) = G^j(r)$ by step 3, and $x^k(q) = r^k$ because $x^k = r^k \circ \varphi_0$ (Definition [[§29 Coordinate Derivations and the Basis Theorem#^def-29-1|§29.1]]), so
>
> $$
> H(r) = \hat\varphi(q) = \big(F^1(q), \ldots, F^n(q), x^{n+1}(q), \ldots, x^m(q)\big) = \big(G^1(r), \ldots, G^n(r), r^{n+1}, \ldots, r^m\big).
> $$
>
> The first $n$ rows of $H'(\varphi_0(p))$ are therefore the rows of $G'(\varphi_0(p)) = J = (A \mid B)$, and row $n + l$ is the gradient of $r^{n+l}$, the standard row vector with $1$ in place $n + l$. The matrix is block upper triangular, so its determinant is the product $\det A \cdot \det I_{m-n} = \det A$ of the determinants of the diagonal blocks.
>
> *8. The inverse function theorem, “possibly after shrinking $U$.”* By the inverse function theorem (Theorem [[§35 Local Diffeomorphisms#^thm-35-1|§35.1]]), possibly after shrinking, $\hat\varphi$ is a diffeomorphism onto $\hat\varphi(U)$. *(Completion.)* The theorem gives an open $W \ni \varphi_0(p)$, contained in $\varphi_0(U_0)$, with $H|_W$ a diffeomorphism onto the open set $H(W) \subseteq \mathbb{R}^m$. (This is Theorem [[§35 Local Diffeomorphisms#^thm-35-1|§35.1]] with $\Phi = H$ on the open set $\varphi_0(U_0)$ and $a = \varphi_0(p)$, where $H'(a)$ is invertible by step 7; the open sets that theorem calls $U_0$ and $V_0$ are here $W$ and $H(W)$, not to be confused with the chart domain $U_0$.) Put $U = \varphi_0^{-1}(W)$, an open neighbourhood of $p$. Then $\hat\varphi|_U = H|_W \circ \varphi_0|_U$ is a composite of diffeomorphisms (Proposition [[§28 Derivations and the Abstract Tangent Space#^prop-28-9|§28.9]], Lemma [[§19 Smooth Functions and Smooth Maps#^lem-19-5|§19.5]]), mapping $U$ onto the open set $\hat\varphi(U) = H(W)$. In detail: $H \circ \varphi_0 = \hat\varphi \circ \varphi_0^{-1} \circ \varphi_0 = \hat\varphi$ on $U_0$; $\varphi_0|_U : U \to W$ is the restriction of the diffeomorphism $\varphi_0 : U_0 \to \varphi_0(U_0)$ to the open set $U$, onto $\varphi_0(U) = W$; $H|_W$ is a diffeomorphism of open subsets of $\mathbb{R}^m$, hence of manifolds (Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-4|§19.4]]); and the composite has the smooth inverse $(\varphi_0|_U)^{-1} \circ (H|_W)^{-1}$.
>
> *9. The intellectual step: $\hat\varphi$ is a chart.* “There's an intellectual step here that should not be overlooked. If I have a local diffeomorphism like this from an open set in $M$ into its image, which is open in $\mathbb{R}^m$, that is a chart”: it is a homeomorphism, and being smooth with smooth inverse makes it compatible with every other smooth chart, so it lies in the maximal atlas. This is Lemma [[§36 Submersions#^lem-36-5|§36.5]]. So $(U, \hat\varphi)$ is a smooth chart at $p$, and $F(U) \subseteq F(U_0) \subseteq V$.
>
> *10. Do not change the $y$-coordinates.* The chart $(V, \psi)$ on $N$ stays as it was. Only the chart on $M$ is new.
>
> *11. Going up and coming down.* Let $\tilde F = \psi \circ F \circ \hat\varphi^{-1} : \hat\varphi(U) \to \psi(V)$ be the coordinate representation of $F$ in the new chart. “I take a point down here, $r^1$ up to $r^m$, and I go upstairs”: going up means finding the point $q = \hat\varphi^{-1}(r)$ of $U$ whose values of the first $n$ functions $F^1, \ldots, F^n$ are the first $n$ coordinates of $r$. By the definition of $\hat\varphi$,
>
> $$
> F^i\big(\hat\varphi^{-1}(r^1, \ldots, r^m)\big) = r^i \qquad (i = 1, \ldots, n).
> $$
>
> *(Completion.)* For $r \in \hat\varphi(U)$ the point $q = \hat\varphi^{-1}(r) \in U$ satisfies $\hat\varphi(q) = r$, that is, $\big(F^1(q), \ldots, F^n(q), x^{n+1}(q), \ldots, x^m(q)\big) = (r^1, \ldots, r^m)$; comparing the first $n$ entries gives the display. Coming back down by $\psi$, the $i$-th coordinate of $\tilde F(r)$ is $y^i(F(q)) = F^i(q) = r^i$. *(Completion.)* In one chain, using the definition of $\tilde F$, then $y^i = r^i \circ \psi$ (Definition [[§29 Coordinate Derivations and the Basis Theorem#^def-29-1|§29.1]]), then $F^i = y^i \circ F$, then the display:
>
> $$
> r^i\big(\tilde F(r)\big) = r^i\big(\psi(F(q))\big) = y^i\big(F(q)\big) = F^i(q) = r^i \qquad (i = 1, \ldots, n).
> $$
>
> So $\tilde F(r^1, \ldots, r^m) = (r^1, \ldots, r^n)$: “this coordinate system labels every point in $U$; the first $n$ labels are the values of the $F$'s at that point.”
>
> *(Completion.)* The charts of the theorem are $(U, \hat\varphi)$ and $(V, \psi)$, with $F(U) \subseteq V$ by step 9. For the equivalent form, the coordinate functions of the new chart are $r^j \circ \hat\varphi$ (Definition [[§29 Coordinate Derivations and the Basis Theorem#^def-29-1|§29.1]]), and for $j \le n$ this is the $j$-th component of $\hat\varphi$, namely $F^j = y^j \circ F$. So, calling the new coordinate functions $x^j$ as in the statement, $y^j \circ F = F^j = x^j$ on $U$ for $j = 1, \ldots, n$. Finally $n \le m$ was shown in step 5.

^pf-36-6

*Uses:* [[§19 Smooth Functions and Smooth Maps#^lem-19-3|§19.3]], [[§17 Differentiable Structures#^lem-17-6|§17.6]], [[§30 The Differential in Coordinates#^thm-30-2|§30.2]], [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-9|§29.9]], [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]], [[§30 The Differential in Coordinates#^prop-30-1|§30.1]], [[§36 Submersions#^prop-36-1|§36.1]], [[§29 Coordinate Derivations and the Basis Theorem#^def-29-1|Def. §29.1]], [[§35 Local Diffeomorphisms#^thm-35-1|§35.1]], [[§28 Derivations and the Abstract Tangent Space#^prop-28-9|§28.9]], [[§19 Smooth Functions and Smooth Maps#^lem-19-5|§19.5]], [[§19 Smooth Functions and Smooth Maps#^prop-19-4|§19.4]], [[§36 Submersions#^lem-36-5|§36.5]]

![[m591-14-5.svg]]
*The change of chart in one diagram. The first chart $\varphi_0$ and the new chart $\hat\varphi$ differ by $H$, a diffeomorphism near $\varphi_0(p)$ by step 8. In the new chart, $F$ becomes $\tilde F$, the projection (step 11). The lecture used the letters $\phi$ and $\tilde F$ both for the first charts and for the new ones. The notes write $\varphi_0$ and $G$ for the first, and $\hat\varphi$ and $\tilde F$ for the new, to keep the two stages apart.*

**Transcription note.** In the lecture, $\hat\varphi$ was twice called “a map from $U$ into $\mathbb{R}^n$”, and page 30 of the handwritten notes writes $\phi : U \to \mathbb{R}$; it has $m$ components, so $\hat\varphi : U \to \mathbb{R}^m$. The matrix of partials was spoken as “$\partial x^j/\partial x^i$”, for $\partial F^j/\partial x^i$.

> [!theorem] Corollary §36.7: Being a Submersion Is an Open Condition
> If $F : M \to N$ is a submersion at $p$, then $F$ is a submersion at every point of some neighbourhood of $p$.
>
> *Lee: Proposition 4.1*

^cor-36-7

> [!proof]+ Proof
> Let $(U, \hat\varphi)$ and $(V, \psi)$ be the charts of the theorem: $p \in U$, $F(U) \subseteq V$, and $\tilde F = \psi \circ F \circ \hat\varphi^{-1}$ is the projection $\tilde F(r^1, \ldots, r^m) = (r^1, \ldots, r^n)$ on $\hat\varphi(U)$. The open set $U$ is a neighbourhood of $p$; we show that $F$ is a submersion at every $q \in U$.
>
> In the charts of the theorem, $\tilde F$ is the projection, whose Jacobian $(I_n \mid 0)$ has rank $n$ at every point of $\hat\varphi(U)$: its components are $\tilde F^j(r) = r^j$ ($j \le n$), so $\partial \tilde F^j/\partial r^i = \delta^j_i$ for $i = 1, \ldots, m$ at every point, and the first $n$ columns of the resulting matrix are the standard basis of $\mathbb{R}^n$. Now fix $q \in U$. The same two charts are charts at $q$ and at $F(q)$ with $F(U) \subseteq V$, so by Theorem [[§30 The Differential in Coordinates#^thm-30-2|§30.2]] the matrix of $F_{\ast q}$ in the coordinate bases is $\tilde F'(\hat\varphi(q)) = (I_n \mid 0)$. Hence $\operatorname{rank} F_{\ast q} = n$ (Proposition [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]](3)), and the image of $F_{\ast q}$ is an $n$-dimensional subspace of the $n$-dimensional space $T_{F(q)}N$ (Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-9|§29.9]]), so it is all of it. By Theorem [[§30 The Differential in Coordinates#^thm-30-2|§30.2]], $F_{\ast q}$ is onto for every $q \in U$.

^pf-36-7

*Uses:* [[§36 Submersions#^thm-36-6|§36.6]], [[§30 The Differential in Coordinates#^thm-30-2|§30.2]], [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]], [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-9|§29.9]]

> [!theorem] Corollary §36.8: The Critical Set Is Closed
> Let $f : M \to \mathbb{R}$ be smooth. Then $\operatorname{Crit}(f)$ (Definition [[§36 Submersions#^def-36-5|§36.5]]) is a closed subset of $M$.

^cor-36-8

> [!proof]+ Proof
> *(Not from lecture; filled in.)* We show that the complement $M \setminus \operatorname{Crit}(f)$ is open, by finding around each of its points an open set contained in it. Let $p \in M \setminus \operatorname{Crit}(f)$, so $df_p \neq 0$. By Proposition [[§36 Submersions#^prop-36-2|§36.2]], $p$ is not a critical point of $f$, that is (Definition [[§36 Submersions#^def-36-3|§36.3]]), $f$ is a submersion at $p$. By Corollary [[§36 Submersions#^cor-36-7|§36.7]], applied to $F = f : M \to \mathbb{R}$, there is a neighbourhood $U_p$ of $p$ — an open set containing $p$ — such that $f$ is a submersion at every $q \in U_p$. Each such $q$ is a regular point of $f$, so $df_q \neq 0$ by Proposition [[§36 Submersions#^prop-36-2|§36.2]] again, that is, $q \notin \operatorname{Crit}(f)$. Thus $U_p \subseteq M \setminus \operatorname{Crit}(f)$, and $M \setminus \operatorname{Crit}(f) = \bigcup_p U_p$ is open, as a union of open sets. Hence $\operatorname{Crit}(f)$ is closed.

^pf-36-8

*Uses:* [[§36 Submersions#^prop-36-2|§36.2]], [[§36 Submersions#^def-36-3|Def. §36.3]], [[§36 Submersions#^cor-36-7|§36.7]]

> [!theorem] Corollary §36.9: Submersions Are Open Maps
> If $F : M \to N$ is a submersion, then $F(W)$ is open in $N$ for every open $W \subseteq M$.
>
> *Lee: Proposition 4.28*

^cor-36-9

> [!proof]+ Proof
> $F$ is smooth, hence continuous, so by Definition [[§4 Quotient Spaces and Open Maps#^def-4-3|§4.3]] it remains to show that $F(W)$ is open for every open $W \subseteq M$. It suffices to find, for each point $q$ of $F(W)$, an open set containing $q$ and contained in $F(W)$, since then $F(W)$ is the union of these open sets.
>
> Let $q = F(p)$ with $p \in W$, and take the charts of the theorem at $p$, shrinking $U$ to $U \cap W$: the restriction of $\hat\varphi$ to the open set $U \cap W \ni p$ is again a smooth chart (Lemma [[§17 Differentiable Structures#^lem-17-6|§17.6]](1), with $U' = U \cap W$), still $F(U \cap W) \subseteq V$, and the coordinate representation is still the projection, now on $\hat\varphi(U \cap W)$. We write $U$ for $U \cap W$. Then $F(U) = \psi^{-1}\big(\mathrm{pr}(\hat\varphi(U))\big)$, where $\mathrm{pr} : \mathbb{R}^m \to \mathbb{R}^n$ is the projection onto the first $n$ coordinates. Indeed, on $U$ we have $F = \psi^{-1} \circ \tilde F \circ \hat\varphi$ (the definition of $\tilde F$, with $F(U) \subseteq V$), and $\tilde F = \mathrm{pr}$ on $\hat\varphi(U)$, so
>
> $$
> F(U) = \psi^{-1}\big(\tilde F(\hat\varphi(U))\big) = \psi^{-1}\big(\mathrm{pr}(\hat\varphi(U))\big) .
> $$
>
> Projections are open (Lemma [[§4 Quotient Spaces and Open Maps#^lem-4-3|§4.3]], for $\mathbb{R}^m = \mathbb{R}^n \times \mathbb{R}^{m-n}$), and $\hat\varphi(U)$ is open, being the image of a chart, so $\mathrm{pr}(\hat\varphi(U))$ is an open subset of $\psi(V)$; it lies in $\psi(V)$ because it equals $\tilde F(\hat\varphi(U))$. Since $\psi : V \to \psi(V)$ is a homeomorphism, $\psi^{-1}$ maps open subsets of $\psi(V)$ to open subsets of $V$ (Proposition [[§1 Point-Set Topology Review#^prop-1-5|§1.5]](2)), and $V$ is open in $N$; so $F(U)$ is open in $N$. It contains $q$ and lies in $F(W)$: $q = F(p)$ with $p \in U$, and $U \subseteq W$.

^pf-36-9

*Uses:* [[§4 Quotient Spaces and Open Maps#^def-4-3|Def. §4.3]], [[§17 Differentiable Structures#^lem-17-6|§17.6]], [[§4 Quotient Spaces and Open Maps#^lem-4-3|§4.3]], [[§1 Point-Set Topology Review#^prop-1-5|§1.5]]

> [!theorem] Theorem §36.10: Submersions from Compact Manifolds
> Let $M$ be compact ([[§18 Compact Spaces#^def-18-2|590 Def. §18.2]]) and nonempty, $N$ connected ([[§15 Connected Spaces#^def-15-2|590 Def. §15.2]]), and $F : M \to N$ a submersion ([[§36 Submersions#^def-36-1|Def. §36.1]]). Then $F$ is surjective, and $N$ is compact.

^thm-36-10

> [!proof]+ Proof
> *(Assignment 4, Problem 2, where $N = \mathbb{R}^k$; the same argument gives the general statement.)* $F(M)$ is open in $N$ because a submersion is an open map (Corollary [[§36 Submersions#^cor-36-9|§36.9]]), and compact, hence closed in the Hausdorff space $N$, because $M$ is compact. It is nonempty, and $N$ is connected, so $F(M) = N$. Then $N = F(M)$ is compact.
>
> In detail, the three properties of the subset $F(M) \subseteq N$ are:
> - *open:* Corollary [[§36 Submersions#^cor-36-9|§36.9]] with $W = M$;
> - *closed:* $F$ is continuous (Definition [[§19 Smooth Functions and Smooth Maps#^def-19-3|§19.3]]), so $F(M)$ is compact as the continuous image of the compact space $M$ (Proposition [[§1 Point-Set Topology Review#^prop-1-8|§1.8]](2)); $N$ is Hausdorff, being a manifold; and a compact subspace of a Hausdorff space is closed (Proposition [[§1 Point-Set Topology Review#^prop-1-8|§1.8]](4));
> - *nonempty:* $M \neq \emptyset$.
>
> In a connected space the only subsets that are both open and closed are $\emptyset$ and the whole space; $F(M)$ is such a subset and is not empty, so $F(M) = N$, i.e. $F$ is surjective. And $N = F(M)$ is compact, by the second item.

^pf-36-10

*Uses:* [[§36 Submersions#^cor-36-9|§36.9]], [[§2 Topological Manifolds#^def-2-2|Def. §2.2]], [[§18 Compact Spaces#^thm-18-3|590 §18.3]], [[§18 Compact Spaces#^thm-18-4|590 §18.4]], [[§15 Connected Spaces#^lem-15-1|590 §15.1]], [[§19 Smooth Functions and Smooth Maps#^def-19-3|Def. §19.3]], [[§1 Point-Set Topology Review#^prop-1-8|§1.8]]

> [!remark]- Connections
> - The point-set steps: [[Continuous Image of a Compact Space is Compact|590 §18.3]], [[Compact Subspace of a Hausdorff Space is Closed|590 §18.4]], and clopen subsets of a connected space, [[§15 Connected Spaces#^lem-15-1|590 Lem. §15.1]]; in 591, [[§1 Point-Set Topology Review#^prop-1-8|§1.8]] and [[§1 Point-Set Topology Review#^prop-1-7|§1.7]].

> [!theorem] Corollary §36.11: No Submersions from Compact Manifolds to Euclidean Space
> If $M$ is compact ([[§18 Compact Spaces#^def-18-2|590 Def. §18.2]]) and nonempty and $k \ge 1$, there is no submersion ([[§36 Submersions#^def-36-1|Def. §36.1]]) $M \to \mathbb{R}^k$.

^cor-36-11

> [!proof]+ Proof
> *(Assignment 4, Problem 2.)* $\mathbb{R}^k$ is connected but not compact, since it is unbounded; apply Theorem [[§36 Submersions#^thm-36-10|§36.10]].
>
> In detail, suppose $F : M \to \mathbb{R}^k$ were a submersion. The hypotheses of Theorem [[§36 Submersions#^thm-36-10|§36.10]] hold: $M$ is compact and nonempty, and $N = \mathbb{R}^k$ is connected (Proposition [[§1 Point-Set Topology Review#^prop-1-7|§1.7]](4)). So the theorem gives that $\mathbb{R}^k$ is compact. But for $k \ge 1$, $\mathbb{R}^k$ is not bounded — it contains the points $(t, 0, \ldots, 0)$ for all $t \in \mathbb{R}$ — so it is not compact by Heine–Borel (Proposition [[§1 Point-Set Topology Review#^prop-1-8|§1.8]](1)). This contradiction shows that no such $F$ exists.

^pf-36-11

*Uses:* [[§36 Submersions#^thm-36-10|§36.10]], [[§16 Connected Subspaces of ℝ#^thm-16-1|590 §16.1]], [[§15 Connected Spaces#^thm-15-6|590 §15.6]], [[Heine–Borel Theorem|590 §18.12]], [[§1 Point-Set Topology Review#^prop-1-7|§1.7]], [[§1 Point-Set Topology Review#^prop-1-8|§1.8]]

> [!remark]- Connections
> - Compact subsets of $\mathbb{R}^k$ are bounded: [[Heine–Borel Theorem]].

The submitted solution also noted the edge cases: for $k = 0$ the constant map $M \to \mathbb{R}^0$ is a submersion, since every differential maps onto the zero space; and for $M = \emptyset$ the empty map is vacuously one. In particular, a compact manifold carries no nonconstant submersion to $\mathbb{R}$ — the maximum of any smooth function $f : M \to \mathbb{R}$ is a [[§36 Submersions#^def-36-3|critical point]]. *(Filled in.)* Directly: if $M$ is compact and nonempty, $f(M)$ is a compact (Proposition [[§1 Point-Set Topology Review#^prop-1-8|§1.8]](2)), hence closed and bounded (Proposition [[§1 Point-Set Topology Review#^prop-1-8|§1.8]](1)), nonempty subset of $\mathbb{R}$, so it contains its supremum $f(p)$, $p \in M$. Then $f(q) \le f(p)$ for every $q$ in the neighbourhood $M$ of $p$, so $df_p = 0$ by Proposition [[§36 Submersions#^prop-36-3|§36.3]], and $f$ is not a submersion at $p$ (Proposition [[§36 Submersions#^prop-36-2|§36.2]]). (Constant functions are not submersions either, their differentials being zero; so for $M$ compact and nonempty there is no submersion $M \to \mathbb{R}$ at all, as Corollary [[§36 Submersions#^cor-36-11|§36.11]] says.)

![[m591-29-1.svg]]
*A compact $M$ (a sphere) and its height function $h : M \to \mathbb{R}$. The image $h(M) = [a, b]$ is compact and nonempty but not open in $\mathbb{R}$. At the top and bottom points $p_{\max}$ and $p_{\min}$ (red) the tangent planes are horizontal, so $dh = 0$ there: they are [[§36 Submersions#^def-36-3|critical points]] ([[§36 Submersions#^prop-36-2|§36.2]]), and $h$ is not a submersion. The box is the proof of [[§36 Submersions#^thm-36-10|Theorem §36.10]] and [[§36 Submersions#^cor-36-11|Corollary §36.11]]: the image of a submersion would be open ([[§36 Submersions#^cor-36-9|§36.9]]) as well as compact, hence closed, hence all of the connected $\mathbb{R}^k$, which is not compact. (Drawn for these notes in the vault; not in the course tex.)*
