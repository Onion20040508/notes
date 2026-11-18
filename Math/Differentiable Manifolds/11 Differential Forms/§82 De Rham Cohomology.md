---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 11
section: 82
tags: [differentiable-manifolds, math591]
---
← [[§81 The Exterior Derivative]] · ↑ [[· 11 Differential Forms]]

*Stage: forms — The kernel of $d$ modulo the image of $d$: real vector spaces attached to a manifold, invariant under homotopy; in degree zero, one dimension for each connected component.*

*(Lecture 32, last minutes.)* With $d$ in hand, the de Rham cohomology can be defined. By convention $\Omega^{-1}(M) = 0$, and $d : \Omega^{-1}(M) \to \Omega^0(M)$ is the zero map. Since each $d : \Omega^k(M) \to \Omega^{k+1}(M)$ is linear, its kernel is a linear subspace of $\Omega^k(M)$, possibly infinite-dimensional ($\Omega^k(M)$ is infinite-dimensional when $0 \le k \le m$ and $m \ge 1$), and so is the image of the previous $d$.

> [!definition] Definition §82.1: Closed Form
> *(Not from lecture: Lee's terminology.)* A form $\omega \in \Omega^k(M)$ is **closed** if $d\omega = 0$. For one-forms this is the notion of Definition [[§53 One-Forms#^def-53-5|§53.5]] (see the end of [[§81 The Exterior Derivative|§81]]).
>
> *Lee: Ch. 17, The de Rham Cohomology Groups*

^def-82-1

> [!remark]- Connections
> - For one-forms: [[§53 One-Forms#^def-53-5|Def. §53.5]]. In MATH 452, on open subsets of $\mathbb{R}^n$: [[§39 Closed and Exact Forms#^def-39-2|452 Def. §39.2]].

> [!definition] Definition §82.2: Exact Form
> *(Not from lecture: Lee's terminology.)* A form $\omega \in \Omega^k(M)$, $k \ge 1$, is **exact** if $\omega = d\eta$ for some $\eta \in \Omega^{k-1}(M)$. For one-forms this is the notion of Definition [[§53 One-Forms#^def-53-6|§53.6]].
>
> *Lee: Ch. 17, The de Rham Cohomology Groups*

^def-82-2

> [!remark]- Connections
> - For one-forms: [[§53 One-Forms#^def-53-6|Def. §53.6]]. In MATH 452: [[§39 Closed and Exact Forms#^def-39-3|452 Def. §39.3]]; a closed form that is not exact, [[§39 Closed and Exact Forms#^prop-39-6|452 Prop. §39.6]]; on star-shaped domains every closed form is exact, the [[Poincaré Lemma]].

> [!theorem] Lemma §82.1: Exact Forms Are Closed
> *(Not from lecture; filled in.)* $\operatorname{im}\big(d : \Omega^{k-1}(M) \to \Omega^k(M)\big) \subseteq \ker\big(d : \Omega^k(M) \to \Omega^{k+1}(M)\big)$.

^lem-82-1

> [!proof]+ Proof
> If $\omega = d\eta$, then $d\omega = d(d\eta) = 0$ by Theorem [[§81 The Exterior Derivative#^thm-81-7|§81.7]](3). For $k = 0$ the image is $0$.

^pf-82-1

*Uses:* [[§81 The Exterior Derivative#^thm-81-7|§81.7]]

So the image is a linear subspace of the kernel, and the quotient vector space makes sense.

> [!definition] Definition §82.3: De Rham Cohomology
> The **$k$-th de Rham cohomology space** of $M$ is the real vector space
>
> $$
> H^k(M) = \frac{\ker\big(d : \Omega^k(M) \to \Omega^{k+1}(M)\big)}{\operatorname{im}\big(d : \Omega^{k-1}(M) \to \Omega^k(M)\big)} = \frac{\{\text{closed } k\text{-forms on } M\}}{\{\text{exact } k\text{-forms on } M\}} .
> $$
>
> In particular, since there is nothing to divide by in degree $0$,
>
> $$
> H^0(M) = \ker\big(d : C^\infty(M) \to \Omega^1(M)\big) .
> $$
>
> *Lee: Ch. 17, The de Rham Cohomology Groups*

^def-82-3

**Transcription note (Lecture 32).** The board wrote the denominator as $\operatorname{Im}\big(d : \Omega^{k+1} \to \Omega^k\big)$; the map into $\Omega^k$ is $d : \Omega^{k-1} \to \Omega^k$, from the previous term of the sequence.

These are real vector spaces. (In MATH 592 a different type of homology and cohomology appears, with groups instead of vector spaces; Lee also says “de Rham groups”.) A real vector space, at least a finite-dimensional one, has only one invariant, its dimension.

> [!definition] Definition §82.4: Betti Numbers
> The **$k$-th Betti number** of $M$ is $b_k(M) = \dim H^k(M)$, a nonnegative integer or $\infty$.

^def-82-4

The board writes $\beta_k$ (see the remark *Notation of Lecture 32* in [[§81 The Exterior Derivative|§81]]). The spaces $H^k(M)$, and so the Betti numbers, turn out to be topological invariants of $M$, and in fact homotopy invariants; this will be proved (Lee, Theorem 17.11 and Corollary 17.12). In general they can be hard to compute; for the unitary group, for instance, the cohomology is an interesting problem, with a beautiful answer. The first step towards invariance is naturality.

> [!theorem] Proposition §82.2: Smooth Maps Act on Cohomology
> *(Not from lecture; filled in.)* Let $F : M \to N$ be smooth. Then $F^{\ast}$ maps closed forms to closed forms and exact forms to exact forms, so it induces linear maps
>
> $$
> F^\# : H^k(N) \to H^k(M), \qquad F^\#[\omega] = [F^{\ast}\omega] .
> $$
>
> Moreover $(G \circ F)^\# = F^\# \circ G^\#$ and $\mathrm{id}^\# = \mathrm{id}$; hence a diffeomorphism $F$ induces isomorphisms $F^\#$, and diffeomorphic manifolds have isomorphic de Rham cohomology and the same Betti numbers.
>
> *Lee: Proposition 17.2; Corollary 17.4*

^prop-82-2

> [!proof]+ Proof
> By naturality (Theorem [[§81 The Exterior Derivative#^thm-81-7|§81.7]](4)), if $d\omega = 0$ then $d(F^{\ast}\omega) = F^{\ast}(d\omega) = 0$, and if $\omega = d\eta$ then $F^{\ast}\omega = d(F^{\ast}\eta)$. So the linear map $F^{\ast}$ sends the kernel into the kernel and the image into the image, and therefore induces a linear map of the quotients; $F^\#[\omega]$ does not depend on the representative, because two representatives differ by an exact form. The composition rules follow from Lemma [[§81 The Exterior Derivative#^lem-81-4|§81.4]](1), and for a diffeomorphism $(F^{-1})^\#$ is an inverse of $F^\#$.

^pf-82-2

*Uses:* [[§81 The Exterior Derivative#^thm-81-7|§81.7]], [[§81 The Exterior Derivative#^lem-81-4|§81.4]]

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

Next: $H^1(S^1)$, announced for the beginning of the next lecture, as an exercise to think about beforehand.
