---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 4
section: 24
tags: [differentiable-manifolds, math591]
---
← [[§23 Tangent Spaces I꞉ The Geometric Picture]] · ↑ [[· 4 Tangent and Cotangent Spaces]] · [[§25 Tangent Spaces II꞉ Germs]] →

*Stage: geometric — When is the preimage of a regular level set again a regular level set? A condition that does not mention the defining map.*

*Assignment 2, Problem 5. The problem ends with a parenthetical that is the point of the whole exercise: the transversality condition “does not mention $G$ explicitly — keep this in mind, for the future.”*

Throughout this section $F : \mathbb{R}^N \to \mathbb{R}^k$ and $G : \mathbb{R}^k \to \mathbb{R}^\ell$ are smooth, $0$ is a regular value of $G$, and

$$
S = G^{-1}(0) \subseteq \mathbb{R}^k ,
$$

a smooth manifold of dimension $k - \ell$ with $T^{\mathrm{geo}}_qS = \ker G'(q)$ for $q \in S$ ([[§23 Tangent Spaces I꞉ The Geometric Picture#^thm-23-3|Theorem §23.3]]). Its codimension, in the sense of the next definition, is $\operatorname{codim} S = k - \dim S = \ell$, the number of equations cutting it out.

> [!definition] Definition §24.1: Codimension
> If $S \subseteq \mathbb{R}^k$ is a manifold of dimension $s$ — for instance a regular level set — its **codimension** in $\mathbb{R}^k$ is $\operatorname{codim} S = k - s$.
>
> *Lee: Ch. 5, Embedded Submanifolds*

^def-24-1

(Everything below works verbatim with $F$ and $G$ defined only on open subsets.)

> [!definition] Definition §24.2: Transversality
> $F$ is **transverse** to $S$, written $F \pitchfork S$, if
>
> $$
> \operatorname{im} F'(p) \;+\; T^{\mathrm{geo}}_{F(p)}S \;=\; \mathbb{R}^k \qquad \text{for every } p \in F^{-1}(S).
> $$
>
> The condition is imposed only at points of the preimage, and holds vacuously if $F^{-1}(S) = \emptyset$.

^def-24-2

> [!remark] Remark
> In words: at each point where $F$ meets $S$, the directions $F$ can move in, together with the directions along $S$, fill up the whole ambient space. The condition involves $F$ and $S$ only — not the function $G$ used to cut $S$ out.

^rem-24-1

> [!theorem] Theorem §24.1: Preimages of Transverse Level Sets
> If $F \pitchfork S$, then $M = F^{-1}(S)$ is a smooth manifold of dimension $N - \ell$ (or empty), and for $p \in M$
>
> $$
> T^{\mathrm{geo}}_pM = F'(p)^{-1}\big(T^{\mathrm{geo}}_{F(p)}S\big) = \{\, v \in \mathbb{R}^N \mid F'(p)v \in T^{\mathrm{geo}}_{F(p)}S \,\}.
> $$
>
> In particular $\operatorname{codim} M = \operatorname{codim} S = \ell$.
>
> *Lee: Theorem 6.30(a)*

^thm-24-1

![[m591-11-3.svg]]
*The spaces: $M = F^{-1}(S)$ inside $\mathbb{R}^N$ over $S$ inside $\mathbb{R}^k$, and the composite $G \circ F$ that cuts $M$ out.*

![[m591-11-4.svg]]
*Their linearizations at $p$ and $q = F(p)$.*

Top, the spaces; bottom, their linearizations at $p$ and $q = F(p)$. In each, the square says the top-left corner is everything upstairs that lands in the bottom-left corner — $M = F^{-1}(S)$ and $T^{\mathrm{geo}}_pM = F'(p)^{-1}(T^{\mathrm{geo}}_qS)$ — and the triangle says the same set is cut out by the composite, $M = (G\circ F)^{-1}(0)$ and $T^{\mathrm{geo}}_pM = \ker (G\circ F)'(p)$. The theorem asserts that the preimage in the lower diagram is the geometric tangent space of the preimage in the upper one; [[§24 Transversality#^ex-24-2|Example §24.2]](b) shows this can fail without transversality.

> [!proof]+ Proof
> If $M = \emptyset$ there is nothing to prove, so assume otherwise; then $S \neq \emptyset$, and surjectivity of $G'(q) : \mathbb{R}^k \to \mathbb{R}^\ell$ at some $q \in S$ gives $k \ge \ell$.
>
> *$M$ is a level set.* $p \in F^{-1}(S) \iff F(p) \in G^{-1}(0) \iff G(F(p)) = 0$, so $M = (G \circ F)^{-1}(0)$, with $G \circ F : \mathbb{R}^N \to \mathbb{R}^\ell$ smooth.
>
> *$0$ is a regular value of $G \circ F$.* Let $p \in M$ and $q = F(p)$. By the [[Multivariable Chain Rule|chain rule]] $(G \circ F)'(p) = G'(q)\,F'(p)$. Given $w \in \mathbb{R}^\ell$, choose $u \in \mathbb{R}^k$ with $G'(q)u = w$, possible as $G'(q)$ is surjective. By transversality write $u = F'(p)v + t$ with $v \in \mathbb{R}^N$ and $t \in T^{\mathrm{geo}}_qS = \ker G'(q)$. Then
>
> $$
> w = G'(q)u = G'(q)F'(p)v + G'(q)t = G'(q)F'(p)v ,
> $$
>
> so $(G\circ F)'(p)$ is surjective. As $p \in M$ was arbitrary, $0$ is a regular value, and surjectivity at a point of $M$ forces $N \ge \ell$.
>
> *Conclusion.* By Theorem [[§7 The Regular Value Theorem#^thm-7-3|§7.3]] and Proposition [[§19 Manifolds in Euclidean Space#^prop-19-2|§19.2]], $M$ is a smooth manifold of dimension $N - \ell$, so $\operatorname{codim} M = N - (N - \ell) = \ell = \operatorname{codim} S$. By [[§23 Tangent Spaces I꞉ The Geometric Picture#^thm-23-3|Theorem §23.3]],
>
> $$
> T^{\mathrm{geo}}_pM = \ker\big(G'(q)F'(p)\big) = \{v \mid F'(p)v \in \ker G'(q)\} = F'(p)^{-1}(T^{\mathrm{geo}}_qS).
> $$

^pf-24-1

*Uses:* [[§24 Transversality#^def-24-2|Def. §24.2]], [[§24 Transversality#^def-24-1|Def. §24.1]], [[§7 The Regular Value Theorem#^def-7-2|Def. §7.2]], [[§7 The Regular Value Theorem#^thm-7-3|§7.3]], [[§19 Manifolds in Euclidean Space#^prop-19-2|§19.2]], [[§23 Tangent Spaces I꞉ The Geometric Picture#^thm-23-3|§23.3]], [[Multivariable Chain Rule|452 §10.2]]

**Comparison with Lee.** Lee's Theorem 6.30 states this for a smooth map transverse to an *embedded submanifold* $S \subseteq M$, after the theory of submanifolds (Chapter 5). The course's version, for level sets in Euclidean space, needs only the regular value theorem. It is the case where $S$ is cut out by a single global defining map $G$, and the proof — pull $G$ back along $F$ — is the one Lee uses locally.

> [!theorem] Proposition §24.2: Transversality Is the Regular Value Condition
> For $p \in F^{-1}(S)$ with $q = F(p)$,
>
> $$
> \operatorname{im} F'(p) + T^{\mathrm{geo}}_qS = \mathbb{R}^k \iff (G \circ F)'(p) \text{ is surjective.}
> $$
>
> Consequently $F \pitchfork S$ if and only if $0$ is a regular value of $G \circ F$.

^prop-24-2

> [!proof]+ Proof
> ($\Rightarrow$) is the middle step of the proof of [[§24 Transversality#^pf-24-1|Theorem §24.1]]. ($\Leftarrow$) Suppose $G'(q)F'(p)$ is surjective and let $u \in \mathbb{R}^k$. Then $G'(q)u = G'(q)F'(p)v$ for some $v \in \mathbb{R}^N$, so $u - F'(p)v \in \ker G'(q) = T^{\mathrm{geo}}_qS$, and
>
> $$
> u = F'(p)v + \big(u - F'(p)v\big) \in \operatorname{im} F'(p) + T^{\mathrm{geo}}_qS.
> $$

^pf-24-2

*Uses:* [[§24 Transversality#^def-24-2|Def. §24.2]], [[§24 Transversality#^thm-24-1|§24.1]], [[§23 Tangent Spaces I꞉ The Geometric Picture#^thm-23-3|§23.3]], [[§7 The Regular Value Theorem#^def-7-2|Def. §7.2]]

> [!remark] Remark: An Intrinsic Statement with a Chosen Proof
> [[§24 Transversality#^prop-24-2|Proposition §24.2]] is the precise content of the parenthetical. Transversality is not merely a sufficient condition: it *is* the regular value condition for $G \circ F$, rewritten so that $G$ disappears. The hypothesis of [[§24 Transversality#^thm-24-1|Theorem §24.1]] and both of its conclusions — that $M$ is a manifold, and the formula for $T^{\mathrm{geo}}_pM$ — involve only $F$ and $S$; only the proof picks a defining function $G$. This is the same pattern as for charts: a statement that does not depend on a choice, proved by making one. Two things remain for later. The smooth structure on $M$ is built through $G$, and its independence of $G$ is a statement about submanifolds. And $S$ need only be cut out by some $G$ *near each point*, which will turn out to hold for every embedded submanifold, so the theorem localizes.

^rem-24-2

> [!theorem] Corollary §24.3: The Regular Value Theorem as a Special Case
> Let $c \in \mathbb{R}^k$ and $S = \{c\}$. Then $F \pitchfork \{c\}$ if and only if $c$ is a regular value of $F$, and in that case [[§24 Transversality#^thm-24-1|Theorem §24.1]] returns [[§7 The Regular Value Theorem#^thm-7-3|Theorem §7.3]] together with $T^{\mathrm{geo}}_pM = \ker F'(p)$.

^cor-24-3

> [!proof]+ Proof
> $\{c\} = G^{-1}(0)$ for $G(y) = y - c$, whose Jacobian is the identity, so $0$ is a regular value of $G$ with $\ell = k$, and $T^{\mathrm{geo}}_c\{c\} = \ker I = 0$. Transversality then reads $\operatorname{im} F'(p) = \mathbb{R}^k$ at every $p \in F^{-1}(c)$ — the [[§7 The Regular Value Theorem#^def-7-2|definition of a regular value]]. The conclusions are $\dim M = N - k$ and $T^{\mathrm{geo}}_pM = F'(p)^{-1}(0) = \ker F'(p)$.

^pf-24-3

*Uses:* [[§24 Transversality#^def-24-2|Def. §24.2]], [[§24 Transversality#^thm-24-1|§24.1]], [[§23 Tangent Spaces I꞉ The Geometric Picture#^thm-23-3|§23.3]], [[§7 The Regular Value Theorem#^def-7-2|Def. §7.2]], [[§7 The Regular Value Theorem#^thm-7-3|§7.3]]

> [!remark]- Connections
> - The regular value theorem for maps between manifolds: [[§33 Submanifolds#^thm-33-6|§33.6]], compared with this version in [[§33 Submanifolds#^prop-33-8|§33.8]].

> [!definition] Definition §24.3: Transverse Intersection
> Regular level sets $S_1, S_2 \subseteq \mathbb{R}^k$ **intersect transversally** if
>
> $$
> T^{\mathrm{geo}}_qS_1 + T^{\mathrm{geo}}_qS_2 = \mathbb{R}^k \qquad\text{for every } q \in S_1 \cap S_2 ,
> $$
>
> a condition that holds vacuously when $S_1 \cap S_2 = \emptyset$.
>
> *Lee: Theorem 6.30(b)*

^def-24-3

> [!theorem] Proposition §24.4: Transverse Intersections
> Let $G_i : \mathbb{R}^k \to \mathbb{R}^{\ell_i}$, $i = 1,2$, be smooth with $0$ a regular value, and $S_i = G_i^{-1}(0)$. For $q \in S_1 \cap S_2$,
>
> $$
> T^{\mathrm{geo}}_qS_1 + T^{\mathrm{geo}}_qS_2 = \mathbb{R}^k \iff (G_1, G_2)'(q) : \mathbb{R}^k \to \mathbb{R}^{\ell_1 + \ell_2} \text{ is surjective.}
> $$
>
> If $S_1$ and $S_2$ intersect transversally ([[§24 Transversality#^def-24-3|Definition §24.3]]), then $S_1 \cap S_2$ is a smooth manifold with
>
> $$
> \operatorname{codim}(S_1 \cap S_2) = \operatorname{codim} S_1 + \operatorname{codim} S_2, \qquad T^{\mathrm{geo}}_q(S_1 \cap S_2) = T^{\mathrm{geo}}_qS_1 \cap T^{\mathrm{geo}}_qS_2 .
> $$
>
> *Lee: Theorem 6.30(b)*

^prop-24-4

> [!proof]+ Proof
> Write $T_i = T^{\mathrm{geo}}_qS_i = \ker G_i'(q)$, of dimension $k - \ell_i$. The kernel of the stacked map $(G_1,G_2)'(q) = \begin{pmatrix} G_1'(q) \\ G_2'(q)\end{pmatrix}$ is $T_1 \cap T_2$, so by [[Fundamental theorem of linear maps|rank–nullity]] it is surjective iff $\dim(T_1 \cap T_2) = k - \ell_1 - \ell_2$. On the other hand
>
> $$
> \dim(T_1 + T_2) = \dim T_1 + \dim T_2 - \dim(T_1 \cap T_2) = (k - \ell_1) + (k - \ell_2) - \dim(T_1 \cap T_2),
> $$
>
> which equals $k$ iff $\dim(T_1 \cap T_2) = k - \ell_1 - \ell_2$. The two conditions coincide. When they hold throughout $S_1 \cap S_2 = (G_1,G_2)^{-1}(0)$, the point $0$ is a regular value of $(G_1, G_2)$, and Theorems [[§7 The Regular Value Theorem#^thm-7-3|§7.3]] and [[§23 Tangent Spaces I꞉ The Geometric Picture#^thm-23-3|§23.3]] give a manifold of codimension $\ell_1 + \ell_2$ with geometric tangent space $\ker(G_1,G_2)'(q) = T_1 \cap T_2$.

^pf-24-4

*Uses:* [[§24 Transversality#^def-24-3|Def. §24.3]], [[§24 Transversality#^def-24-1|Def. §24.1]], [[§23 Tangent Spaces I꞉ The Geometric Picture#^thm-23-3|§23.3]], [[§7 The Regular Value Theorem#^def-7-2|Def. §7.2]], [[§7 The Regular Value Theorem#^thm-7-3|§7.3]], [[Fundamental theorem of linear maps|LADR 3.21]], [[§6 Dimension#^ladr-2-43|LADR 2.43]]

> [!example] Example §24.1: The Sphere and the Plane Re-read
> The figure in [[§7 The Regular Value Theorem#^rem-7-3|§7]] was a transversality picture. Let $S_1 = S^2$ and $S_2 = \{z = c\}$ in $\mathbb{R}^3$, so $T^{\mathrm{geo}}_qS_1 = q^\perp$ and $T^{\mathrm{geo}}_qS_2 = e_3^\perp$, the horizontal plane. Two planes through the origin in $\mathbb{R}^3$ sum to $\mathbb{R}^3$ iff they are distinct, so the intersection is transverse at $q$ iff $q^\perp \neq e_3^\perp$, i.e. iff $q \neq \pm e_3$ — iff the two normals $q$ and $e_3$ are independent, which is what the figure's caption said in the language of gradients.
> - $|c| < 1$: every point of $S_1 \cap S_2$ has $x^2 + y^2 = 1 - c^2 > 0$, so $q \neq \pm e_3$ and the intersection is transverse. Codimensions add, $1 + 1 = 2$, and $S_1 \cap S_2$ is a curve: the circle of radius $\sqrt{1-c^2}$.
> - $c = \pm 1$: $S_1 \cap S_2 = \{\pm e_3\}$, where $T^{\mathrm{geo}}_qS_1 = T^{\mathrm{geo}}_qS_2$. Not transverse, and the intersection is a point rather than the predicted curve.
> - $|c| > 1$: the intersection is empty, and transversality holds vacuously.

^ex-24-1

The sphere through the course: a topological manifold with hemisphere charts in [[§8 Example꞉ Spheres|Example: Spheres]]; the homogeneous space $\mathrm{SO}(3)/\mathrm{SO}(2)$ in [[§13 Homogeneous Spaces#^ex-13-3|the sphere as a homogeneous space]]; the Riemann sphere $\mathbb{CP}^1$ in [[§17 Projective Spaces as Smooth Manifolds#^prop-17-4|the Riemann sphere]]; its geometric tangent spaces in [[§23 Tangent Spaces I꞉ The Geometric Picture#^ex-23-1|the tangent space of the sphere]] and its transverse intersection with a plane in [[§24 Transversality#^ex-24-1|the sphere and the plane re-read]]; the double cover $S^n \to \mathbb{RP}^n$ and the Hopf fibration $S^{2n+1} \to \mathbb{CP}^n$ in [[§38 Example꞉ Projective Spaces and the Hopf Fibration|Example: Projective Spaces and the Hopf Fibration]]; and $S^3 = \mathrm{SU}(2)$ in [[§39 Worked Example꞉ The Double Cover SU(2) → SO(3)#^prop-39-5|the unit quaternions as SU(2)]].

> [!example] Example §24.2: Two Ways Transversality Can Fail
> Let $S$ be the $x$-axis in $\mathbb{R}^2$, cut out by $G(x,y) = y$, so $T^{\mathrm{geo}}_qS$ is the $x$-axis at every $q \in S$, and $\ell = 1$. For $F : \mathbb{R} \to \mathbb{R}^2$ the theorem predicts $\dim F^{-1}(S) = 1 - 1 = 0$.
> - (a) $F(t) = (t, 0)$. Then $F^{-1}(S) = \mathbb{R}$, of dimension $1$: the *dimension* is wrong. Here $\operatorname{im} F'(t)$ is the $x$-axis, so $\operatorname{im} F'(t) + T S$ is the $x$-axis, not $\mathbb{R}^2$.
> - (b) $F(t) = (t, t^2)$. Then $F^{-1}(S) = \{0\}$, which has the predicted dimension $0$; but $F'(0) = (1,0)$ lies in $T^{\mathrm{geo}}_0S$, so $F'(0)^{-1}(T^{\mathrm{geo}}_0S) = \mathbb{R}$, while the geometric tangent space of a point is $0$: the *tangent formula* is wrong. Correspondingly $(G \circ F)(t) = t^2$ has $(G\circ F)'(0) = 0$, as [[§24 Transversality#^prop-24-2|Proposition §24.2]] predicts.
> - (c) $F(t) = (t, t^2 - \varepsilon)$ with $\varepsilon > 0$. Now $F^{-1}(S) = \{\pm\sqrt\varepsilon\}$, and at these points $F'(t) = (1, 2t)$ has nonzero second component, so $\operatorname{im} F'(t) + TS = \mathbb{R}^2$: transverse, two points, and every conclusion of the theorem holds.

^ex-24-2

![[m591-11-5.svg]]
*The three maps of the example against the $x$-axis $S$ (blue): (a) the image lies in $S$; (b) the parabola is tangent to $S$ at the origin, its velocity (orange) lying in $S$; (c) the lowered parabola crosses $S$ transversally at two points.*

> [!remark] Remark
> Transversality protects the dimension and the tangent formula *independently*: (a) loses the first, (b) keeps the first and loses the second. And (c) shows what happens to the tangency of (b) under an arbitrarily small perturbation: it disappears, replaced by two transverse crossings (for $\varepsilon > 0$) or by no intersection at all (for $\varepsilon < 0$). The same happens to the tangent plane of [[§24 Transversality#^ex-24-1|Example §24.1]] when it is moved slightly up or down.

^rem-24-3

> [!remark] Remark: Looking Ahead: Transversality Is Generic
> Two points of [[§24 Transversality#^rem-24-3|the remark above]] will be taken up once abstract manifolds and submanifolds are in place. First, the definition makes sense verbatim for a smooth map $F : X \to Y$ between abstract manifolds and a submanifold $S \subseteq Y$, with *abstract* tangent spaces and the differential of [[§26 Derivations and the Abstract Tangent Space#Pushing Derivations Forward|§26]] in place of $T^{\mathrm{geo}}$ and the Jacobian:
>
> $$
> dF_p(T_pX) + T_{F(p)}S = T_{F(p)}Y \qquad \text{for all } p \in F^{-1}(S),
> $$
>
> and [[§24 Transversality#^thm-24-1|Theorem §24.1]] becomes the statement that *the preimage of a submanifold under a transverse map is a submanifold of the same codimension*. Second, as [[§24 Transversality#^ex-24-2|Example §24.2]](c) suggests, transversality is the *typical* situation: any smooth map can be made transverse to a given submanifold by an arbitrarily small perturbation, and tangencies are non-generic accidents. This is the transversality theorem of Thom, and it is the entry point to intersection theory (Guillemin–Pollack, Ch. 2). Neither is part of the course yet.

^rem-24-4

> [!remark] Remark: What Is Still Missing
> Everything above presupposes an ambient $\mathbb{R}^{n+k}$: [[§23 Tangent Spaces I꞉ The Geometric Picture#^def-23-1|Definition §23.1]] of the geometric tangent space $T^{\mathrm{geo}}_pM$ uses its vector space structure to differentiate $\gamma$, and [[§23 Tangent Spaces I꞉ The Geometric Picture#^thm-23-3|Theorem §23.3]] uses the Jacobian of the defining map $F$. For an abstract smooth manifold neither is available — “if you have a sphere you can think of the tangent plane, but that is a subspace of $\mathbb{R}^3$. If you do not have $\mathbb{R}^3$, then what do you do? You do not have room to put your vectors.” [[§25 Tangent Spaces II꞉ Germs|The next sections]] build the *abstract* tangent space $T_pM$ from the charts alone.

^rem-24-5
