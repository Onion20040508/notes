---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 11
section: 82
tags: [differentiable-manifolds, math591]
---
← [[§81 The Exterior Derivative]] · ↑ [[· 11 Differential Forms]] · [[§83 The First Cohomology of the Circle]] →

*Stage: forms — The kernel of $d$ modulo the image of $d$: real vector spaces attached to a manifold, invariant under homotopy; in degree zero, one dimension for each connected component.*

*(Lecture 32, last minutes.)* With $d$ in hand, the de Rham cohomology can be defined. By convention $\Omega^{-1}(M) = 0$, and $d : \Omega^{-1}(M) \to \Omega^0(M)$ is the zero map. Since each $d : \Omega^k(M) \to \Omega^{k+1}(M)$ is linear, its kernel is a linear subspace of $\Omega^k(M)$, possibly infinite-dimensional ($\Omega^k(M)$ is infinite-dimensional when $0 \le k \le m$ and $m \ge 1$), and so is the image of the previous $d$.

> [!definition] Definition §82.1: Closed Form
> A form $\omega \in \Omega^k(M)$ is **closed** if $d\omega = 0$. The space of all closed $k$-forms is written
>
> $$
> Z^k(M) = \{ \text{all closed } k\text{-forms on } M \} = \ker\big(d : \Omega^k(M) \to \Omega^{k+1}(M)\big) .
> $$
>
> For one-forms this is the notion of Definition [[§53 One-Forms#^def-53-5|§53.5]] (see the end of [[§81 The Exterior Derivative|§81]]).
>
> *Source: Lecture 33 · Lee's terminology*
>
> *Lee: Ch. 17, The de Rham Cohomology Groups*

^def-82-1

These notes used the term *closed* before Lecture 33, in the material of Lecture 32.

> [!remark]- Connections
> - For one-forms: [[§53 One-Forms#^def-53-5|Def. §53.5]]. In MATH 452, on open subsets of $\mathbb{R}^n$: [[§39 Closed and Exact Forms#^def-39-2|452 Def. §39.2]].

> [!definition] Definition §82.2: Exact Form
> A form $\omega \in \Omega^k(M)$, $k \ge 1$, is **exact** if $\omega = d\alpha$ for some $\alpha \in \Omega^{k-1}(M)$. The space of all exact $k$-forms is written
>
> $$
> B^k(M) = \{ \text{all exact } k\text{-forms on } M \} = \operatorname{im}\big(d : \Omega^{k-1}(M) \to \Omega^k(M)\big) ,
> $$
>
> with $B^0(M) = 0$. For one-forms this is the notion of Definition [[§53 One-Forms#^def-53-6|§53.6]].
>
> *Source: Lecture 33 · Lee's terminology*
>
> *Lee: Ch. 17, The de Rham Cohomology Groups*

^def-82-2

> [!remark]- Connections
> - For one-forms: [[§53 One-Forms#^def-53-6|Def. §53.6]]. In MATH 452: [[§39 Closed and Exact Forms#^def-39-3|452 Def. §39.3]]; a closed form that is not exact, [[§39 Closed and Exact Forms#^prop-39-6|452 Prop. §39.6]]; on star-shaped domains every closed form is exact, the [[Poincaré Lemma]].

> [!theorem] Lemma §82.1: Exact Forms Are Closed
> $B^k(M) \subseteq Z^k(M)$ for every $k$. More precisely, $d \circ d = 0$ on $\Omega^{k-1}(M)$ if and only if $B^k(M) \subseteq Z^k(M)$; so $d^2 = 0$ is equivalent to $B^k(M) \subseteq Z^k(M)$ for all $k$.

^lem-82-1

> [!proof]+ Proof
> *(Lecture 33 stated the equivalence; the one-line proof is filled in.)* $B^k(M) \subseteq Z^k(M)$ says that $d(d\eta) = 0$ for every $\eta \in \Omega^{k-1}(M)$, which is $d \circ d = 0$ on $\Omega^{k-1}(M)$. By Theorem [[§81 The Exterior Derivative#^thm-81-7|§81.7]](3) it holds. For $k = 0$, $B^0(M) = 0$.

^pf-82-1

*Uses:* [[§81 The Exterior Derivative#^thm-81-7|§81.7]]

So the image is a linear subspace of the kernel, and the quotient vector space makes sense.

> [!definition] Definition §82.3: De Rham Cohomology
> The **$k$-th de Rham cohomology space** of $M$ is the real vector space
>
> $$
> H^k(M) = \frac{\ker\big(d : \Omega^k(M) \to \Omega^{k+1}(M)\big)}{\operatorname{im}\big(d : \Omega^{k-1}(M) \to \Omega^k(M)\big)} = \frac{Z^k(M)}{B^k(M)} = \frac{\{\text{closed } k\text{-forms on } M\}}{\{\text{exact } k\text{-forms on } M\}} .
> $$
>
> The class of a closed form $\omega$ is written $[\omega] \in H^k(M)$.
> In particular, since there is nothing to divide by in degree $0$,
>
> $$
> H^0(M) = \ker\big(d : C^\infty(M) \to \Omega^1(M)\big) .
> $$
>
> *Lee: Ch. 17, The de Rham Cohomology Groups*

^def-82-3

**Transcription note (Lecture 32).** The board wrote the denominator as $\operatorname{Im}\big(d : \Omega^{k+1} \to \Omega^k\big)$; the map into $\Omega^k$ is $d : \Omega^{k-1} \to \Omega^k$, from the previous term of the sequence.

$H^k(M)$ measures the failure of equality between exact and closed forms. *(Lecture 33.)* The sequence $\cdots \to \Omega^k(M) \xrightarrow{d} \Omega^{k+1}(M) \xrightarrow{d} \cdots$ is a co-chain complex; in MATH 592 the same algebra appears with the arrows reversed, a boundary map from $k$-chains to $(k-1)$-chains, and that is a chain complex. These are real vector spaces. (In MATH 592 a different type of homology and cohomology appears, with groups instead of vector spaces; Lee also says “de Rham groups”.) A real vector space, at least a finite-dimensional one, has only one invariant, its dimension.

> [!definition] Definition §82.4: Betti Numbers
> The **$k$-th Betti number** of $M$ is $b_k(M) = \dim H^k(M)$, a nonnegative integer or $\infty$.

^def-82-4

The board writes $\beta_k$ (see the remark *Notation of Lecture 32* in [[§81 The Exterior Derivative|§81]]). The spaces $H^k(M)$, and so the Betti numbers, turn out to be topological invariants of $M$, and in fact homotopy invariants; this will be proved (Lee, Theorem 17.11 and Corollary 17.12). In general they can be hard to compute; for the unitary group, for instance, the cohomology is an interesting problem, with a beautiful answer. The first step towards invariance is naturality.

> [!theorem] Proposition §82.2: Smooth Maps Act on Cohomology
> Let $F : M \to N$ be smooth. Then $F^{\ast}$ maps closed forms to closed forms and exact forms to exact forms, $F^{\ast} : Z^k(N) \to Z^k(M)$ and $F^{\ast} : B^k(N) \to B^k(M)$, so it induces linear maps, also denoted $F^{\ast}$,
>
> $$
> F^{\ast} : H^k(N) \to H^k(M), \qquad F^{\ast}[\omega] = [F^{\ast}\omega] .
> $$
>
> Moreover $(G \circ F)^{\ast} = F^{\ast} \circ G^{\ast}$ for smooth $G : N \to P$, and $\mathrm{id}^{\ast} = \mathrm{id}$; hence if $F$ is a diffeomorphism, then for every $k$, $F^{\ast} : H^k(N) \to H^k(M)$ is a linear bijection, and diffeomorphic manifolds have isomorphic de Rham cohomology and the same Betti numbers.
>
> *Source: Lecture 33*
>
> *Lee: Proposition 17.2; Corollary 17.4*

^prop-82-2

> [!proof]+ Proof
> *(Lecture 33; written out.)* By naturality (Theorem [[§81 The Exterior Derivative#^thm-81-7|§81.7]](4)), $d F^{\ast} = F^{\ast} d$: if $d\omega = 0$ then $d(F^{\ast}\omega) = F^{\ast}(d\omega) = 0$, and if $\omega = d\eta$ then $F^{\ast}\omega = d(F^{\ast}\eta)$. So the linear map $F^{\ast}$ sends $Z^k(N)$ into $Z^k(M)$ and $B^k(N)$ into $B^k(M)$, and therefore induces a linear map of the quotients, by pulling back representatives of classes; $[F^{\ast}\omega]$ does not depend on the representative $\omega$, because two representatives differ by an exact form, whose pullback is exact. The composition rules follow from Lemma [[§81 The Exterior Derivative#^lem-81-4|§81.4]](1) on representatives. For a diffeomorphism, take $G = F^{-1}$: then $F^{\ast} \circ (F^{-1})^{\ast} = (F^{-1} \circ F)^{\ast} = \mathrm{id}$ and likewise in the other order, so $(F^{-1})^{\ast}$ is an inverse of $F^{\ast}$ on $H^k$.

^pf-82-2

*Uses:* [[§81 The Exterior Derivative#^thm-81-7|§81.7]], [[§81 The Exterior Derivative#^lem-81-4|§81.4]]

![[m591-80-1.svg]]

*(Figure after the board.)* The co-chain complexes of $N$ and $M$, one above the other, with the differentials horizontal and the pullbacks vertical (the diagram after Definition [[§81 The Exterior Derivative#^def-81-1|§81.1]], around degree $k$). Naturality says that every square commutes, and Proposition [[§82 De Rham Cohomology#^prop-82-2|§82.2]] is the consequence for the quotients $Z^k/B^k$.

The induced map is written with the same star as the pullback of forms, and the context says which is meant. (Before Lecture 33 these notes wrote it $F^\#$.) Note the order: $(G \circ F)^{\ast} = F^{\ast} \circ G^{\ast}$, pullbacks compose in reverse. A diffeomorphism therefore preserves Betti numbers; in fact the Betti numbers are homotopy invariants, which will be proved once Cartan's magic formula is available (announced for Lecture 34).

> [!theorem] Proposition §82.3: Cohomology in Degree Zero
> $H^0(M) = \{ f \in C^\infty(M) : df = 0 \}$ is the space of locally constant smooth functions on $M$, and $b_0(M)$ is the number of connected components of $M$.
>
> *Lee: Proposition 17.5; Proposition 17.6*

^prop-82-3

> [!remark]- Connections
> - A manifold has at most countably many components, all open: [[§2 Topological Manifolds#^prop-2-6|§2.6]].
> - The step from $df = 0$ to locally constant is Assignment 4, Problem 1: [[§30 The Differential in Coordinates#^prop-30-11|§30.11]].

> [!proof]+ Proof
> *(Lecture 32: the first statement from a homework problem, the second as the answer to the question; details filled in.)* *$df = 0$ if and only if $f$ is locally constant.* Since $df_p = \iota_{f(p)} \circ f_{\ast p}$ with $\iota_{f(p)}$ an isomorphism (Definition [[§32 The Cotangent Space#^def-32-5|§32.5]]), $df = 0$ means $f_{\ast p} = 0$ for every $p$. If so, let $p \in M$ and let $U$ be a connected open neighbourhood of $p$ (the preimage of an open ball under a chart); by Proposition [[§30 The Differential in Coordinates#^prop-30-11|§30.11]] (Assignment 4: a smooth map with zero differential on a connected manifold is constant), applied to $f|_U$, $f$ is constant on $U$. Conversely, if $f$ is constant near $p$, then $df_p(v) = v[f] = 0$ (Proposition [[§32 The Cotangent Space#^prop-32-2|§32.2]]), since a derivation depends only on the germ of $f$ and kills constants.
>
> *Counting.* The connected components of $M$ are open (Proposition [[§2 Topological Manifolds#^prop-2-6|§2.6]] and its proof: $M$ is locally connected), and there are at most countably many. A locally constant function is constant on each component $C$: it has zero differential on the connected open submanifold $C$, so Proposition [[§30 The Differential in Coordinates#^prop-30-11|§30.11]] applies. Conversely, a function that is constant on each component is locally constant, because the components are open, hence smooth. So $f \mapsto (f|_C)_C$ is a linear isomorphism from $H^0(M)$ onto the space of all real-valued functions on the set of components. If $M$ has $r$ components, this space is $\mathbb{R}^r$ and $b_0(M) = r$; if $M$ has infinitely many, it is infinite-dimensional, and $b_0(M) = \infty$.

^pf-82-3

*Uses:* [[§32 The Cotangent Space#^def-32-5|Def. §32.5]], [[§30 The Differential in Coordinates#^prop-30-11|§30.11]], [[§32 The Cotangent Space#^prop-32-2|§32.2]], [[§2 Topological Manifolds#^prop-2-6|§2.6]]

So $b_0(M)$ is a topological invariant, by inspection. (The homework, Assignment 4, proved that $f$ is constant when $M$ is connected; but $M$ need not be connected, and in general $df = 0$ says only that $f$ is locally constant.)

![[m591-79-5.svg]]

*(Not from lecture; figure added.)* A surface $M$ with three connected components (one of them an annulus). A smooth function with $df = 0$ is constant on each component, with independent values, here $2$, $-1$ and $0$; so $H^0(M) \cong \mathbb{R}^3$, by $f \mapsto$ its three values, and $b_0(M) = 3$. The hole of the annulus plays no role in $H^0$.

Next: $H^1(S^1)$ ([[§83 The First Cohomology of the Circle|§83]]).
