---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 8
section: 60
tags: [differentiable-manifolds, math591]
---
← [[§59 Sard's Theorem]] · ↑ [[· 8 Sard's Theorem]] · [[§61 The Whitney Embedding Theorem]] →

*Stage: analysis — Transversality of a whole family passes, by Sard's theorem, to almost every member.*

*Lecture 20. “Next topic … one of my favorite theorems in the whole course … a really beautiful, useful theorem, called the transversality theorem of René Thom, or parametric transversality, that will have really beautiful consequences together with Sard's theorem.”*

> [!definition] Definition §60.1: Smooth Family of Maps
> Let $S$, $M$, $N$ be smooth manifolds. A **smooth family** of maps $M \to N$, parametrized by $S$, is a collection $\{F_s\}_{s \in S}$ of maps $F_s : M \to N$ such that $F : S \times M \to N$, $F(s, p) = F_s(p)$, is smooth. $S$ is the **parameter space**.
>
> *Lee: Ch. 6, The Transversality Homotopy Theorem*

^def-60-1

“Smoothness of the family is the same as smoothness of the big map” — jointly in $s$ and $p$. Each $F_s = F \circ \iota_s$, with $\iota_s : M \to S \times M$, $p \mapsto (s, p)$, the slice inclusion (Definition [[§19 Smooth Functions and Smooth Maps#^def-19-8|§19.8]]), so each $F_s$ is smooth.

> [!theorem] Theorem §60.1: Parametric Transversality
> Let $F : S \times M \to N$ be smooth, $Z \subseteq N$ a regular submanifold, and suppose $F \pitchfork Z$ (Definition [[§37 Regular Submanifolds#^def-37-5|§37.5]]). Then $W = F^{-1}(Z)$ is a regular submanifold of $S \times M$, and with $\pi : W \to S$ the restriction of the projection $(s, p) \mapsto s$: for $s \in S$,
>
> $$
> s \text{ is a regular value of } \pi \iff F_s : M \to N \text{ is transverse to } Z .
> $$
>
> *Lee: Theorem 6.35 (proof)*

^thm-60-1

> [!proof]+ Proof
> *(Lecture 20 — “a nice exercise” — proved the direction “that matters for applications”, $(\Rightarrow)$; the converse is filled in.)*
>
> *Preliminaries.* $W$ is a regular submanifold of $S \times M$ and, for $(s, p) \in W$ with $q = F(s, p)$,
>
> $$
> T_{(s,p)}W = \big(dF_{(s,p)}\big)^{-1}\big(T_qZ\big) \tag{1}
> $$
>
> (Theorem [[§37 Regular Submanifolds#^thm-37-15|§37.15]]; a student supplied this in class: “it's the preimage of the tangent space of $Z$ by the differential”). $\pi$ is smooth, as the restriction of the smooth projection to a regular submanifold. Write tangent vectors to $S \times M$ as pairs $(\sigma, u) \in T_sS \oplus T_pM$ (Theorem [[§31 Tangent Vectors as Velocities of Curves#^thm-31-4|§31.4]]); then $d\pi(\sigma, u) = \sigma$, and
>
> $$
> dF_{(s,p)}(0, u) = d(F_s)_p(u), \tag{2}
> $$
>
> because $F_s = F \circ \iota_s$ and $d(\iota_s)_p(u) = (0, u)$: “it's a partial derivative … when I compute this derivative, I freeze the first entry to $s$” (Definition [[§31 Tangent Vectors as Velocities of Curves#^def-31-3|§31.3]]).
>
> *$(\Rightarrow)$* Let $s$ be a regular value of $\pi$, and $p \in M$ with $q = F_s(p) = F(s,p) \in Z$. We must show $\operatorname{Im} d(F_s)_p + T_qZ = T_qN$; “clearly we have one inclusion.” Let $w \in T_qN$. Since $F \pitchfork Z$, there are $(\sigma, u) \in T_{(s,p)}(S \times M)$ and $v \in T_qZ$ with
>
> $$
> w = dF_{(s,p)}(\sigma, u) + v . \tag{$\ast$}
> $$
>
> “Since $s$ is a regular value of $\pi$ … I can hit $\sigma$”: there is a tangent vector to $W$ at $(s, p)$ projecting to $\sigma$, and since $d\pi$ only reads the first component, it has the form $(\sigma, \tau)$ for some $\tau \in T_pM$. Write $(\sigma, u) = (\sigma, \tau) + (0, u - \tau)$ and substitute into $(\ast)$:
>
> $$
> w = dF_{(s,p)}(\sigma, \tau) + dF_{(s,p)}(0, u - \tau) + v = d(F_s)_p(u - \tau) + \big(dF_{(s,p)}(\sigma, \tau) + v\big),
> $$
>
> by (2). By (1), $dF_{(s,p)}(\sigma, \tau) \in T_qZ$, so the bracket is tangent to $Z$, and $w \in \operatorname{Im} d(F_s)_p + T_qZ$. “So this implies that $F_s$ intersects $Z$ transversely.”
>
> *$(\Leftarrow)$* *(Filled in.)* Suppose $F_s \pitchfork Z$, and let $(s, p) \in \pi^{-1}(s)$, so $q = F_s(p) \in Z$; we show $d\pi_{(s,p)}$ is onto $T_sS$. Let $\sigma \in T_sS$. By transversality of $F_s$, $dF_{(s,p)}(\sigma, 0) = d(F_s)_p(u) + v$ for some $u \in T_pM$, $v \in T_qZ$. By (2), $dF_{(s,p)}(\sigma, -u) = dF_{(s,p)}(\sigma, 0) - d(F_s)_p(u) = v \in T_qZ$, so $(\sigma, -u) \in T_{(s,p)}W$ by (1), and $d\pi(\sigma, -u) = \sigma$.

^pf-60-1

*Uses:* [[§37 Regular Submanifolds#^thm-37-15|§37.15]], [[§31 Tangent Vectors as Velocities of Curves#^thm-31-4|§31.4]], [[§31 Tangent Vectors as Velocities of Curves#^def-31-3|Def. §31.3]]

![[m591-60-1.svg]]

The cartoon, in $S \times M$ with $S$ horizontal. $W = F^{-1}(Z)$ is the orange curve and $\pi$ projects it to $S$. At $s$ the slice $\{s\} \times M$ crosses $W$ transversally: $s$ is a regular value of $\pi$, and $F_s \pitchfork Z$. At $s'$ the slice is tangent to $W$: $s'$ is a singular value, and $F_{s'}$ need not be transverse to $Z$. At $s''$ the slice misses $W$: $F_{s''}(M) \cap Z = \varnothing$, vacuously transverse. (“I can't make a useful cartoon of what happens to the right.”)

![[m591-60-3.svg]]

*(Not from lecture; figure added.)* An explicit instance of the cartoon. Take $S = M = \mathbb{R}$, $N = \mathbb{R}^2$, $Z = \{ y = x^2 \}$ and $F(s, x) = (x, s)$, so $F_s$ parametrizes the horizontal line at height $s$. Then $F$ is a diffeomorphism, so $F \pitchfork Z$, and $W = F^{-1}(Z) = \{ (s, x) : s = x^2 \}$. Parametrizing $W$ by $x \mapsto (x^2, x)$, the projection is $\pi(x^2, x) = x^2$, with derivative $2x$: the only critical point is $x = 0$, and the only critical value is $s = 0$. For $s > 0$, $F_s$ crosses $Z$ transversally at $x = \pm\sqrt{s}$; for $s < 0$, $F_s^{-1}(Z) = \varnothing$; at $s = 0$, $\operatorname{Im} d(F_0)_0 = \operatorname{span}\{(1, 0)\} = T_{(0,0)}Z$, so $F_0$ is tangent to $Z$, not transverse — exactly as Theorem [[§60 Parametric Transversality#^thm-60-1|§60.1]] predicts.

> [!theorem] Corollary §60.2: Almost Every Member Is Transverse
> If $F : S \times M \to N$ is smooth and $F \pitchfork Z$, then $F_s \pitchfork Z$ for almost every $s \in S$: the set of $s$ with $F_s$ not transverse to $Z$ has measure zero in $S$.
>
> *Lee: Theorem 6.35*

^cor-60-2

> [!proof]+ Proof
> *(Lecture 20: “pairing this with Sard's theorem”.)* By Sard's theorem (Theorem [[§59 Sard's Theorem#^thm-59-3|§59.3]]) applied to $\pi : W \to S$, the singular values of $\pi$ form a set of measure zero; for every other $s$, $F_s \pitchfork Z$ by Theorem [[§60 Parametric Transversality#^thm-60-1|§60.1]].

^pf-60-2

*Uses:* [[§59 Sard's Theorem#^thm-59-3|§59.3]], [[§60 Parametric Transversality#^thm-60-1|§60.1]]

“You go from transversality of the family to transversality of individual elements in the family. That's the beauty of this.”

> [!example] Example §60.1: Translates Are Generically Transverse
> Let $Y, Z \subseteq \mathbb{R}^d$ be regular submanifolds. For almost every $a \in \mathbb{R}^d$, the translate $a + Y$ intersects $Z$ transversally.

^ex-60-1

> [!proof]+ Proof
> *(Lecture 20, the “first classical, very geometric application”; details filled in.)* The parameter space is $\mathbb{R}^d$ itself: $F : \mathbb{R}^d \times Y \to \mathbb{R}^d$, $F(a, p) = a + p$, “I use the vector space structure to translate.” Then $F_a(Y) = a + Y$. *$F$ is a submersion*: fixing $p$ and varying $a$, $dF_{(a,p)}(\sigma, 0) = \sigma$ for every $\sigma \in T_a\mathbb{R}^d = \mathbb{R}^d$ — “if you just vary $a$, you get anything.” So $F \pitchfork Z$ (Corollary [[§37 Regular Submanifolds#^cor-37-17|§37.17]](3)), and $F^{-1}(Z) = \{ (a, p) : a + p \in Z \}$. By Corollary [[§60 Parametric Transversality#^cor-60-2|§60.2]], $F_a \pitchfork Z$ for almost every $a$. Finally $F_a : Y \to \mathbb{R}^d$ is the inclusion of $a + Y$ composed with the diffeomorphism $Y \to a + Y$, $p \mapsto a + p$ (“the translate … just the inclusion”), and $a + Y$ is a regular submanifold, a translate of one, so $F_a \pitchfork Z$ says $(a + Y) \pitchfork Z$ (Proposition [[§37 Regular Submanifolds#^prop-37-21|§37.21]]).

^pf-ex-60-1

*Uses:* [[§37 Regular Submanifolds#^cor-37-17|§37.17]], [[§60 Parametric Transversality#^cor-60-2|§60.2]], [[§37 Regular Submanifolds#^prop-37-21|§37.21]]

“Isn't that nice?” If $\dim Y + \dim Z < d$, a transverse intersection must be empty, since $T_qY + T_qZ$ has dimension at most $\dim Y + \dim Z$. So two curves in $\mathbb{R}^3$ ($1 + 1 < 3$): “translate one by a generic vector, it'll cease to intersect the other one.” For two curves in the plane that are tangent, a generic translate either separates them or makes them cross transversally. This is the idea of *general position*: a configuration is not in general position if moving one of the objects a little changes the geometry radically. “General position things are transverse, which may mean that they don't intersect. But vacuous intersection is a statement. It's a powerful statement.”

![[m591-60-2.svg]]

Uribe's picture: $Z$ (blue) and $Y$ (red) tangent at a point, not transverse; a translate $a + Y$ meeting $Z$ in two transverse crossings; another translate $a' + Y$ disjoint from $Z$. Only translates making them tangent again are excluded, and those form a set of measure zero.

“I will give you a homework problem, an application of this … to show that if you have a manifold inside $\mathbb{R}^2$ [as transcribed], almost all linear functions restricted to the manifold are Morse. So you have a lot of Morse functions” (Definition [[§52 Critical Points and the Hessian#^def-52-4|§52.4]]).

**Transcription note (Lecture 20).** Page 54 of the handwritten notes writes “$\pi$ onto” under $F^{-1}(Z) \to \mathbb{R}^d$; Uribe paused (“that's not at all … yeah, it's onto”), and it is onto — for $p \in Y$ and $z \in Z$, $(z - p, p) \in F^{-1}(Z)$ when $Z \neq \varnothing$ — but surjectivity plays no role in the argument.
