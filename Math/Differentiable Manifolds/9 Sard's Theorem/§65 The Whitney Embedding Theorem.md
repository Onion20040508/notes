---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 9
section: 65
tags: [differentiable-manifolds, math591]
---
← [[§64 Parametric Transversality]] · ↑ [[· 9 Sard's Theorem]] ·  →

*Stage: analysis — Every manifold sits inside some Euclidean space; Sard's theorem pushes the dimension down to $2m + 1$.*

*Lecture 21. “There isn't enough time in the semester to cover everything that's on the syllabus, and the only way to cover more is to skip some proofs … I never quite get to degree theory, which is a really cool topic that is officially on the syllabus. So I will be assigning reading.” Then: “Today we're going to talk about the Whitney embedding and immersion theorems.”*

The proof, for $M$ compact, has two parts with “totally different” ideas: bump functions embed $M$ in some $\mathbb{R}^k$ (Lemma [[§65 The Whitney Embedding Theorem#^lem-65-1|§65.1]]), and projections along well-chosen lines lower the dimension (Lemmas [[§65 The Whitney Embedding Theorem#^lem-65-2|§65.2]] and [[§65 The Whitney Embedding Theorem#^lem-65-3|§65.3]]). The lemmas come first; Theorem [[§65 The Whitney Embedding Theorem#^thm-65-4|§65.4]] assembles them.

> [!theorem] Lemma §65.1: Compact Manifolds Embed in Some $\mathbb{R}^k$
> Let $M$ be a compact smooth manifold of dimension $m$. Then there is an embedding $F : M \to \mathbb{R}^k$ for some $k$.
>
> *Lee: proof of Theorem 6.15*

^lem-65-1

> [!proof]+ Proof
> *(Lecture 21, Part I of the proof of Theorem [[§65 The Whitney Embedding Theorem#^thm-65-4|§65.4]], in the lecture's steps with details filled in.)* “We're going to use bump functions” — “this idea of partition of unity … is kind of behind it.”
>
> *The cover.* For every $x \in M$ choose a chart $(U_x, \varphi_x)$ at $x$ and an open coordinate ball $B_x \ni x$ with $\overline{B_x} \subseteq U_x$ and $\varphi_x(\overline{B_x})$ a closed ball in $\mathbb{R}^m$ — possible because $\varphi_x(U_x)$ is open, so it contains a closed Euclidean ball about $\varphi_x(x)$, “and then I pull it back.” Let $\chi_x \in C^\infty_0(M)$ with $\operatorname{supp}\chi_x \subseteq U_x$ and $\chi_x \equiv 1$ on $\overline{B_x}$ (the proof of Proposition [[§56 Vector Fields#^prop-56-4|§56.4]]). The *open* balls $B_x$ cover $M$ — in lecture Uribe first wrote the cover with the $U_x$, and corrected it: “I want to put a $B$. It's very important.” $M$ is compact, so finitely many cover; relabel them $B_1, \ldots, B_n$, with charts $(U_i, \varphi_i)$ and bump functions $\chi_i$.
>
> *The map.* Each $\chi_i\varphi_i : M \to \mathbb{R}^m$, defined as $\chi_i \varphi_i$ on $U_i$ and $0$ outside, is smooth: it is smooth on $U_i$ and zero on the open set $M \setminus \operatorname{supp}\chi_i$, and these cover $M$ ($\operatorname{supp}\chi_i$ is compact, hence closed). Define
>
> $$
> F = \big(\chi_1\varphi_1, \ldots, \chi_n\varphi_n, \chi_1, \ldots, \chi_n\big) : M \to \mathbb{R}^{nm + n},
> $$
>
> “a super big” Euclidean space: $n$ blocks of $m$ components, then $n$ scalars. “It's really very, very clever.”
>
> *$F$ is injective.* Suppose $F(p) = F(q)$. There is $i$ with $p \in B_i$, so $\chi_i(p) = 1$. The last $n$ components of $F$ are the $\chi$'s, so $\chi_i(q) = \chi_i(p) = 1$; in particular $\chi_i(q) \neq 0$, so $q \in U_i$, because $\chi_i$ vanishes outside $U_i$. “I don't know that $q$ is in $B_i$, but I don't care.” The $i$-th block gives $\chi_i(p)\varphi_i(p) = \chi_i(q)\varphi_i(q)$, that is, $\varphi_i(p) = \varphi_i(q)$; “the charts are bijective, so $p = q$.” “Because we put the $\chi$'s here, we are able to conclude that $p$ and $q$ … are in the same coordinate chart.”
>
> *$F$ is an immersion.* Write $F = (F_1, \ldots, F_n, \chi_1, \ldots, \chi_n)$ with $F_j = \chi_j\varphi_j : M \to \mathbb{R}^m$. Let $p \in M$, $v \in T_pM$, and $\gamma$ a curve with $\gamma(0) = p$ and $D_\gamma = v$ (Theorem [[§31 Tangent Vectors as Velocities of Curves#^thm-31-2|§31.2]]). “Use curves”: $dF_p(v) = \frac{d}{dt}\big|_{t=0} F(\gamma(t)) = (v_1, \ldots, v_n, \ldots)$, with $v_j = d(F_j)_p(v) \in \mathbb{R}^m$, componentwise. Choose $i$ with $p \in B_i$. Then $\chi_i \equiv 1$ on the open set $B_i \ni p$, so $F_i = \varphi_i$ near $p$ and $v_i = d(\varphi_i)_p(v)$ — equivalently $d(\chi_i)_p = 0$, since $\chi_i \equiv 1$ in a neighbourhood of $p$. As $\varphi_i$ is a diffeomorphism onto its image (Proposition [[§28 Derivations and the Abstract Tangent Space#^prop-28-9|§28.9]]), $v \neq 0$ gives $v_i \neq 0$, so $dF_p(v) \neq 0$: $dF_p$ is injective.
>
> *An embedding.* An injective immersion of a compact manifold is an embedding (Corollary [[§44 Embeddings#^cor-44-6|§44.6]]). “End of Part I.”

^pf-65-1

*Uses:* [[§56 Vector Fields#^prop-56-4|§56.4]], [[§31 Tangent Vectors as Velocities of Curves#^thm-31-2|§31.2]], [[§28 Derivations and the Abstract Tangent Space#^prop-28-9|§28.9]], [[§44 Embeddings#^cor-44-6|§44.6]]

![[m591-61-1.svg]]

Uribe's cartoon for injectivity: $\chi_i \equiv 1$ on $\overline{B}_i$ (“it could be one a little bit outside too”), and zero outside $U_i$. So $\chi_i(q) = 1$ forces $q \in U_i$, where the chart $\varphi_i$ separates points.

*Part II: lower the ambient dimension.* By Lemma [[§65 The Whitney Embedding Theorem#^lem-65-1|§65.1]], a compact $M$ may be taken to be a regular submanifold $M \subseteq \mathbb{R}^N$ (the image of the embedding, Theorem [[§44 Embeddings#^thm-44-1|§44.1]]). Regard $\mathbb{R}^{N-1} \subseteq \mathbb{R}^N$ by $x \mapsto (x, 0)$. To every line $\ell \subseteq \mathbb{R}^N$ through $0$ that is transverse to $\mathbb{R}^{N-1}$, that is, not contained in it, so that $\mathbb{R}^N = \mathbb{R}^{N-1} \oplus \ell$, associate the projection along $\ell$, a linear map $\mathbb{R}^N \to \mathbb{R}^{N-1}$ with kernel $\ell$, and its restriction

$$
\pi_\ell : M \longrightarrow \mathbb{R}^{N-1} .
$$

(“Do you guys know the difference between complementary and supplementary? I learned that in elementary school, and I'm still trying to figure out what the difference is.”) We want: *if $N > 2m + 1$, there is an $\ell$ such that $\pi_\ell$ is an embedding.* Applying this repeatedly lowers $N$ to $2m + 1$, “until we're out of parameters.”

> [!theorem] Lemma §65.2: Projections That Stay Injective
> Let $M \subseteq \mathbb{R}^N$ be a regular submanifold of dimension $m$, with $N > 2m + 1$. Then the lines $\ell \subseteq \mathbb{R}^N$ through $0$ for which $\ell \subseteq \mathbb{R}^{N-1}$, or $\pi_\ell : M \to \mathbb{R}^{N-1}$ is not injective, form a set of measure zero in $\mathbb{RP}^{N-1}$. In particular there are lines $\ell \not\subseteq \mathbb{R}^{N-1}$ with $\pi_\ell$ injective.
>
> *Lee: Lemma 6.13*

^lem-65-2

> [!proof]+ Proof
> *(Lecture 21, Part II of the proof of Theorem [[§65 The Whitney Embedding Theorem#^thm-65-4|§65.4]].)* “The clever idea”: let $\Delta = \{ (p, p) : p \in M \}$, closed in $M \times M$ since $M$ is Hausdorff, and
>
> $$
> \sigma : (M \times M) \setminus \Delta \longrightarrow \mathbb{RP}^{N-1}, \qquad (p, q) \longmapsto \operatorname{span}(q - p),
> $$
>
> the line through $0$ parallel to the secant from $p$ to $q$, “the vector $\vec{pq}$, as in Calc 3”; $q - p \neq 0$ because $p \neq q$. *(Filled in.)* $\sigma$ is smooth: it is $(p, q) \mapsto q - p \in \mathbb{R}^N \setminus \{0\}$ followed by the quotient map to $\mathbb{RP}^{N-1}$, which in the chart $\varphi_i$ of Corollary [[§18 Projective Spaces as Smooth Manifolds#^cor-18-5|§18.5]] is $w \mapsto (w_k/w_i)_{k \neq i}$, rational with nonvanishing denominator. Its domain is open in $M \times M$, of dimension $2m$, and $\dim \mathbb{RP}^{N-1} = N - 1$. If $2m < N - 1$, the image of $\sigma$ has measure zero (Corollary [[§63 Sard's Theorem#^cor-63-4|§63.4]]). So do the lines contained in $\mathbb{R}^{N-1}$: they form a copy of $\mathbb{RP}^{N-2}$, of lower dimension — “the things that are not transverse to $\mathbb{R}^{N-1}$ is a projective space of lower dimension” — whose image under the smooth inclusion has measure zero by the same corollary. A union of two sets of measure zero has measure zero (Proposition [[§62 Sets of Measure Zero#^prop-62-4|§62.4]]), so its complement is dense (Lemma [[§62 Sets of Measure Zero#^lem-62-1|§62.1]](4), in charts): “pick $\ell$ not in the image and transverse to $\mathbb{R}^{N-1}$.” For such $\ell$, $\pi_\ell$ is injective: $\pi_\ell(p) = \pi_\ell(q)$ means $q - p \in \ker = \ell$, so for $p \neq q$, $\ell = \operatorname{span}(q - p) = \sigma(p, q)$, contrary to the choice. “I'm going to lose injectivity precisely when I have a $p$ and a $q$ parallel to the line of projection.” The condition $2m < N - 1$ is $N > 2m + 1$, “precisely the bound.”

^pf-65-2

*Uses:* [[§18 Projective Spaces as Smooth Manifolds#^cor-18-5|§18.5]], [[§63 Sard's Theorem#^cor-63-4|§63.4]], [[§62 Sets of Measure Zero#^prop-62-4|§62.4]], [[§62 Sets of Measure Zero#^lem-62-1|§62.1]]

![[m591-61-2.svg]]

Projection along a line $\ell$, in the plane ($N = 2$). Points of $M$ slide along lines parallel to $\ell$ onto $\mathbb{R}^{N-1}$. Two points $p \neq q$ collide exactly when the secant $q - p$ is parallel to $\ell$; choosing $\ell$ outside the image of $\sigma$ avoids every such pair. “That's a beautiful proof of the non-optimal Whitney embedding theorem.”

![[m591-61-3.svg]]

*(Not from lecture; figure added.)* Why the bound is $2m + 1$. For a curve ($m = 1$) in $\mathbb{R}^3$ ($N = 3$), $(M \times M) \setminus \Delta$ has dimension $2m = 2 = N - 1$, so the secant directions $\sigma(p, q)$ can fill an open set of $\mathbb{RP}^2$ and Corollary [[§63 Sard's Theorem#^cor-63-4|§63.4]] does not apply. Indeed, projecting a curve in space onto a plane along $\ell$ typically produces crossings: here $q - p$ is parallel to $\ell$, and $\pi_\ell(p) = \pi_\ell(q)$. The shadow is still an immersed curve, matching the immersion into $\mathbb{R}^{2m}$ of Theorem [[§65 The Whitney Embedding Theorem#^thm-65-4|§65.4]], but not an embedded one.

> [!theorem] Lemma §65.3: Projections That Stay Immersions
> Let $M \subseteq \mathbb{R}^N$ be a regular submanifold of dimension $m$, with $N > 2m + 1$. Then the lines $\ell \subseteq \mathbb{R}^N$ through $0$ for which $\ell \subseteq \mathbb{R}^{N-1}$, or $\pi_\ell : M \to \mathbb{R}^{N-1}$ is not an immersion, form a set of measure zero in $\mathbb{RP}^{N-1}$.
>
> *Lee: Lemma 6.13*

^lem-65-3

> [!proof]+ Proof (to be filled)
> *(A homework problem. Uribe's sketch from Lecture 21 is recorded as given; the proof is to be filled in after the assignment is submitted.)* “The same idea … instead of pairs $(p, q)$ to create a line, you take tangent vectors. You take $p$ and $q$ infinitesimally close together”: map nonzero tangent vectors to lines,
>
> $$
> TM \setminus \mathcal{Z} \longrightarrow \mathbb{RP}^{N-1}, \qquad (p, v) \longmapsto \mathbb{R}v ,
> $$
>
> with $T_pM \subseteq \mathbb{R}^N$ (“in the homework you replace this by $v$ of length one”), and choose $\ell$ also outside its image. “What remains to be proved is that if you have a line that is not in here, then you get an immersion, and that's going to be precisely because the differential of the projection is just the projection.” To be filled.

^pf-65-3

> [!theorem] Theorem §65.4: The Whitney Embedding and Immersion Theorems
> Let $M$ be a smooth manifold of dimension $m$. Then there is an embedding $M \to \mathbb{R}^{2m+1}$ and an immersion $M \to \mathbb{R}^{2m}$.
>
> *Lee: Theorems 6.15 and 6.18*

^thm-65-4

“In other words, any manifold is diffeomorphic to a submanifold of some Euclidean space” (Theorem [[§44 Embeddings#^thm-44-1|§44.1]]). The course proves it for $M$ compact. The noncompact case, which first makes the embedding proper, is assigned as reading in Lee (Lemma 6.14 and Theorem 6.15): “he has a beautiful picture.”

> [!remark] Remark: The Hard Version
> In the “hard” version the dimensions are one less: an embedding into $\mathbb{R}^{2m}$ and an immersion into $\mathbb{R}^{2m-1}$ (for $m > 1$ in the second; Lee, Theorems 6.19 and 6.20). “We will not discuss this at all. The proof is very specialized and really long … The smaller the codimension, the tighter it is, and you have to wrestle the manifold more to get it in there. It's like packing your clothes in a suitcase.”

^rem-65-1

> [!proof]+ Proof for $M$ compact
> *(Lecture 21, “two steps … totally different. The technology, the ideas are totally different.” The steps are Lemma [[§65 The Whitney Embedding Theorem#^lem-65-1|§65.1]] and Lemmas [[§65 The Whitney Embedding Theorem#^lem-65-2|§65.2]]–[[§65 The Whitney Embedding Theorem#^lem-65-3|§65.3]]; the immersion lemma is a homework problem, to be filled in after the assignment.)*
>
> *Step 1: some Euclidean space.* By Lemma [[§65 The Whitney Embedding Theorem#^lem-65-1|§65.1]] there is an embedding $M \to \mathbb{R}^N$ for some $N$. Its image is a regular submanifold diffeomorphic to $M$ (Theorem [[§44 Embeddings#^thm-44-1|§44.1]]); replace $M$ by it.
>
> *Step 2: one dimension less.* Suppose $N > 2m + 1$. By Lemmas [[§65 The Whitney Embedding Theorem#^lem-65-2|§65.2]] and [[§65 The Whitney Embedding Theorem#^lem-65-3|§65.3]], the lines $\ell$ that lie in $\mathbb{R}^{N-1}$, or for which $\pi_\ell$ is not injective, or not an immersion, form the union of two sets of measure zero in $\mathbb{RP}^{N-1}$, which has measure zero (Proposition [[§62 Sets of Measure Zero#^prop-62-4|§62.4]]). A set of measure zero contains no nonempty open set (Lemma [[§62 Sets of Measure Zero#^lem-62-1|§62.1]](4), in a chart), so it is not all of $\mathbb{RP}^{N-1}$: choose $\ell$ outside it. Then $\pi_\ell : M \to \mathbb{R}^{N-1}$ is an injective immersion of a compact manifold, hence an embedding (Corollary [[§44 Embeddings#^cor-44-6|§44.6]]), and its image is a regular submanifold of $\mathbb{R}^{N-1}$ diffeomorphic to $M$.
>
> *Step 3: repeat.* Apply Step 2 while $N > 2m + 1$, lowering $N$ by one each time, “until we're out of parameters”: this ends with an embedding $M \to \mathbb{R}^{2m+1}$. The immersion into $\mathbb{R}^{2m}$ is part of the same homework, and is likewise to be filled.

^pf-65-4

*Uses:* [[§65 The Whitney Embedding Theorem#^lem-65-1|§65.1]], [[§65 The Whitney Embedding Theorem#^lem-65-2|§65.2]], [[§65 The Whitney Embedding Theorem#^lem-65-3|§65.3]], [[§44 Embeddings#^thm-44-1|§44.1]], [[§62 Sets of Measure Zero#^prop-62-4|§62.4]], [[§62 Sets of Measure Zero#^lem-62-1|§62.1]], [[§44 Embeddings#^cor-44-6|§44.6]]
