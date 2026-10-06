---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 4
section: 31
tags: [differentiable-manifolds, math591]
---
← [[§30 The Differential in Coordinates]] · ↑ [[· 4 Tangent and Cotangent Spaces]] · [[§32 The Cotangent Space]] →

*Stage: abstract — The other face of a tangent vector: every derivation is the velocity of a curve, on every manifold. Tangent spaces of products split.*

*Assignment 3, Problem 2.* Tangent vectors were introduced with two faces: velocities of curves, and derivations (the [[§28 Derivations and the Abstract Tangent Space#^rem-28-1|remark]] at the start of [[§28 Derivations and the Abstract Tangent Space|§28, Derivations and the Abstract Tangent Space]]). For regular level sets the two were identified by Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]], through the ambient space. This section identifies them on *every* smooth manifold, with no ambient space at all.

> [!definition] Definition §31.1: Smooth Curve
> Let $J \subseteq \mathbb{R}$ be an open interval containing $0$, with its standard smooth structure and coordinate $t$. A **smooth curve** in $M$ is a smooth map $\gamma : J \to M$.
>
> *Lee: Ch. 3, Velocity Vectors of Curves*

^def-31-1

> [!definition] Definition §31.2: Velocity of a Curve
> Let $\gamma : J \to M$ be a smooth curve ([[§31 Tangent Vectors as Velocities of Curves#^def-31-1|Definition §31.1]]). If $\gamma(0) = p$, the **velocity** of $\gamma$ at $0$ is the abstract tangent vector
>
> $$
> D_\gamma = \gamma_{*0}\Big(\frac{d}{dt}\Big|_0\Big) \in T_pM, \qquad\text{explicitly}\qquad D_\gamma[f] = \frac{d}{dt}\Big|_{t=0} f\big(\gamma(t)\big).
> $$
>
> *Lee: Ch. 3, Velocity Vectors of Curves*

^def-31-2

> [!remark]- Connections
> - The geometric velocity $\gamma'(0)$ of a curve in $\mathbb{R}^N$: [[§25 The Geometric Tangent Space#^def-25-1|Def. §25.1]]; differentials computed by curves between vector spaces: [[§22 The Differential of a Map Between Vector Spaces#^thm-22-3|§22.3]].
> - In ℝ³ the velocity is $\mathbf r'(t)$: [[§104 Motion in Space꞉ Velocity and Acceleration#^def-104-1|Calc Def. §104.1]], [[§101 Derivatives and Integrals of Vector Functions#^def-101-2|Calc Def. §101.2]] (with worked examples).

The explicit formula is the definition of the pushforward: $\gamma_{\ast 0}(d/dt|_0)[f] = d/dt|_0\,[f \circ \gamma]$, the ordinary derivative at $0$ of the function $f \circ \gamma$, which is defined near $0$. Lee writes $\gamma'(0)$ for $D_\gamma$. These notes keep $\gamma'(0)$ for the ordinary derivative of a curve in $\mathbb{R}^N$, which is a *geometric* tangent vector, and write $D_\gamma$ for the abstract one, as Assignment 3 does.

> [!theorem] Proposition §31.1: Velocity in Coordinates
> $D_\gamma$ is a derivation at $p$. In a chart $(U, \varphi)$ at $p$ with coordinate functions $x^1, \ldots, x^n$,
>
> $$
> D_\gamma = \sum_{j=1}^n \big(x^j \circ \gamma\big)'(0)\, \frac{\partial}{\partial x^j}\Big|_p .
> $$
>
> In particular $D_\gamma$ depends only on the velocity $(\varphi \circ \gamma)'(0) \in \mathbb{R}^n$ of the coordinate curve $\varphi \circ \gamma$.
>
> *Lee: Ch. 3, Velocity Vectors of Curves*

^prop-31-1

> [!proof]+ Proof
> $D_\gamma$ is a pushforward of a derivation, hence a derivation (Proposition [[§28 Derivations and the Abstract Tangent Space#^prop-28-5|§28.5]]) — which is why Assignment 3 could waive the check. By the universal formula (Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-5|§29.5]]), the $j$-th coefficient of $D_\gamma$ is $D_\gamma[x^j] = (x^j \circ \gamma)'(0)$.

^pf-31-1

*Uses:* [[§31 Tangent Vectors as Velocities of Curves#^def-31-2|Def. §31.2]], [[§28 Derivations and the Abstract Tangent Space#^prop-28-5|§28.5]], [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-5|§29.5]]

The same formula comes out of the chain rule directly, as in the assignment's solution. With $c = \varphi \circ \gamma$ and $c^j = r^j \circ c = x^j \circ \gamma$, near $0$ one has $f \circ \gamma = f_\varphi \circ c$, so

$$
D_\gamma[f] = \frac{d}{dt}\Big|_0 f_\varphi\big(c(t)\big) = \sum_{j} \frac{\partial f_\varphi}{\partial r^j}\big(\varphi(p)\big)\,(c^j)'(0) = \sum_j (c^j)'(0)\,\frac{\partial}{\partial x^j}\Big|_p[f].
$$

Each input $r^j$ of $f_\varphi$ moves at speed $(c^j)'(0)$ along the curve, and contributes $\partial f_\varphi/\partial r^j \cdot (c^j)'(0)$ to the rate of change.

> [!theorem] Theorem §31.2: Every Tangent Vector Is a Velocity
> For every $D \in T_pM$ there is a smooth curve $\gamma : (-\varepsilon, \varepsilon) \to M$ with $\gamma(0) = p$ and $D_\gamma = D$.
>
> *Lee: Proposition 3.23*

^thm-31-2

> [!proof]+ Proof
> *(Assignment 3, Problem 2.)* Fix a chart $(U, \varphi)$ at $p$ with coordinate functions $x^i$, and put $a^i = D[x^i]$ and $a = (a^1, \ldots, a^n) \in \mathbb{R}^n$. These are the coefficients of $D$ in the universal formula; the freedom lies in the curve.
>
> *The curve downstairs.* Let $c(t) = \varphi(p) + t\,a$. Since $\varphi(U)$ is open, some ball $B(\varphi(p), r)$ lies in it. If $a \ne 0$ take $\varepsilon = r/|a|$, so that $|c(t) - \varphi(p)| = |t|\,|a| < r$ for $|t| < \varepsilon$. If $a = 0$, which happens exactly when $D = 0$, take $\varepsilon = 1$. In either case $c : (-\varepsilon, \varepsilon) \to \varphi(U)$ is smooth, being affine, with $c(0) = \varphi(p)$ and $c'(0) = a$.
>
> *The curve upstairs.* Let $\gamma = \varphi^{-1} \circ c$. It is smooth, since its coordinate representation in the chart $(U,\varphi)$ is $\varphi \circ \gamma = c$, and $\gamma(0) = p$. Its coordinate curve is $\varphi \circ \gamma = c$, so $(x^j \circ \gamma)'(0) = (c^j)'(0) = a^j$.
>
> *Conclusion.* By Proposition [[§31 Tangent Vectors as Velocities of Curves#^prop-31-1|§31.1]] and the universal formula,
>
> $$
> D_\gamma = \sum_j a^j\, \frac{\partial}{\partial x^j}\Big|_p = \sum_j D[x^j]\, \frac{\partial}{\partial x^j}\Big|_p = D.
> $$

^pf-31-2

*Uses:* [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-5|§29.5]], [[§31 Tangent Vectors as Velocities of Curves#^prop-31-1|§31.1]], [[§29 Coordinate Derivations and the Basis Theorem#^def-29-1|Def. §29.1]], [[§31 Tangent Vectors as Velocities of Curves#^def-31-1|Def. §31.1]], [[§31 Tangent Vectors as Velocities of Curves#^def-31-2|Def. §31.2]], [[§19 Smooth Functions and Smooth Maps#^def-19-3|Def. §19.3]]

Assignment 3's solution first treats the basis vectors $\partial/\partial x^i|_p$, using curves with $c'(0) = e_i$, and then the general case. The general argument contains the basis case, with $a = e_i$ and $c(t) = \varphi(p) + t\,e_i$, so it is presented here alone.

> [!theorem] Corollary §31.3: Velocity of a Composite — Computing Differentials by Curves
> Let $F : M \to N$ be smooth and $\gamma$ a smooth curve in $M$ with $\gamma(0) = p$. Then $D_{F \circ \gamma} = F_{*p}(D_\gamma)$. Consequently, for every $D \in T_pM$,
>
> $$
> F_{*p}(D) = D_{F \circ \gamma} \qquad \text{for any smooth curve } \gamma \text{ with } \gamma(0) = p \text{ and } D_\gamma = D,
> $$
>
> and such a curve exists by Theorem [[§31 Tangent Vectors as Velocities of Curves#^thm-31-2|§31.2]].
>
> *Lee: Proposition 3.24 and Corollary 3.25*

^cor-31-3

> [!proof]+ Proof
> By the Chain Rule (Theorem [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]]), $D_{F \circ \gamma} = (F \circ \gamma)_{*0}(d/dt|_0) = F_{*p}\big(\gamma_{*0}(d/dt|_0)\big) = F_{*p}(D_\gamma)$.

^pf-31-3

*Uses:* [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]], [[§31 Tangent Vectors as Velocities of Curves#^def-31-2|Def. §31.2]], [[§31 Tangent Vectors as Velocities of Curves#^thm-31-2|§31.2]]

This is Lee's main computational tool: to find $F_{*p}(D)$, choose any curve with velocity $D$ and differentiate $F$ along it. It is the manifold version of Theorem [[§22 The Differential of a Map Between Vector Spaces#^thm-22-3|§22.3]], and it is how Lee computes the differential of the determinant (Problem 7-4).

![[m591-12-14.svg]]
*The proof in one picture. Downstairs, in the chart, the curve is the straight line through $\varphi(p)$ in the direction of the coefficient vector $a = (D[x^1], \ldots, D[x^n])$. The chart carries it upstairs to a curve $\gamma$ in $M$, bent by whatever distortion $\varphi^{-1}$ introduces. The bending is invisible to the velocity, which depends only on $(\varphi \circ \gamma)'(0) = a$ — so the velocity is $D$.*

![[m591-12-15.svg]]
*The same construction as a diagram: the curve is built downstairs as $c$ and lifted by $\varphi^{-1}$, and the triangle commutes, $\varphi \circ \gamma = c$.*

> [!remark] Remark: The Two Faces Reconciled
> Theorem [[§31 Tangent Vectors as Velocities of Curves#^thm-31-2|§31.2]] says the map $\gamma \mapsto D_\gamma$, from smooth curves through $p$ to $T_pM$, is onto. By Proposition [[§31 Tangent Vectors as Velocities of Curves#^prop-31-1|§31.1]], two curves have the same velocity exactly when their coordinate curves have the same velocity in one chart, and then in every chart. So $T_pM$ may equally be described as *curves through $p$, modulo having the same velocity in coordinates* — the intrinsic “velocities of curves” definition of the tangent space, now a theorem, on every manifold, with no ambient space. For a regular level set, the abstract velocity $D_\gamma$ is the derivation $D_{\gamma'(0)}$ attached to the geometric velocity $\gamma'(0) \in T^{\mathrm{geo}}_pM$ (Proposition [[§25 The Geometric Tangent Space#^prop-25-8|§25.8]](2)). So the identification of Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]] is the statement that the two notions of velocity agree.

^rem-31-1

## Tangent Spaces of Products

*Lecture 11. “There is a natural isomorphism” between the tangent space of a product and the direct sum of the tangent spaces of the factors — “natural meaning coordinate-free.” Uribe gave three ways to see it: by the inclusions of the factors, by curves, and in coordinates. He added that this part of the course is, in his experience, “the most abstract, somehow the hardest part”, and that while physicists tend to favour coordinates and pure mathematicians abstract settings, “you need both.”*

Throughout, $p = (p_1, p_2) \in M_1 \times M_2$, and $\iota_1 = \iota^{p_2} : M_1 \to M_1 \times M_2$, $\iota_2 = \iota^{p_1} : M_2 \to M_1 \times M_2$ are the slice inclusions through $p$ (Definition [[§19 Smooth Functions and Smooth Maps#^def-19-8|§19.8]]).

> [!theorem] Theorem §31.4: The Tangent Space of a Product
> The linear map
>
> $$
> \Theta : T_{p_1}M_1 \oplus T_{p_2}M_2 \longrightarrow T_p(M_1 \times M_2), \qquad \Theta(v, w) = \iota_{1*}v + \iota_{2*}w,
> $$
>
> is an isomorphism, defined without charts, with inverse $\Psi(D) = (\pi_{1*}D, \pi_{2*}D)$. In particular $\iota_{1*}$ and $\iota_{2*}$ are injective, and $T_p(M_1 \times M_2)$ is the internal direct sum of their images, $\Theta\big(T_{p_1}M_1 \oplus \{0\}\big)$ and $\Theta\big(\{0\} \oplus T_{p_2}M_2\big)$.
>
> *Lee: Proposition 3.14*

^thm-31-4

> [!proof]+ Proof
> *(Stated in lecture; Uribe left the injectivity as “check”.)* First, the pushforward along a constant map is zero: if $\kappa$ is constant with value $q_0$ and $[g]$ is a germ at $q_0$, then $g \circ \kappa$ is constant, so $(\kappa_{\ast} D)[g] = D[g \circ \kappa] = 0$ because derivations kill constants (Lemma [[§28 Derivations and the Abstract Tangent Space#^lem-28-2|§28.2]]). Now $\pi_1 \circ \iota_1 = \mathrm{id}_{M_1}$ and $\pi_2 \circ \iota_2 = \mathrm{id}_{M_2}$, while $\pi_2 \circ \iota_1$ and $\pi_1 \circ \iota_2$ are constant. By the Chain Rule (Theorem [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]]),
>
> $$
> \pi_{1*}\iota_{1*} = \mathrm{id}, \qquad \pi_{2*}\iota_{2*} = \mathrm{id}, \qquad \pi_{2*}\iota_{1*} = 0, \qquad \pi_{1*}\iota_{2*} = 0,
> $$
>
> so $\Psi(\Theta(v, w)) = (v, w)$, and $\Theta$ is injective. Both spaces have dimension $m_1 + m_2$ (Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-5|§29.5]] and Propositions [[§19 Smooth Functions and Smooth Maps#^prop-19-8|§19.8]], [[§21 Linear Algebra Toolkit#^prop-21-7|§21.7]]), so $\Theta$ is an isomorphism (Proposition [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]](1)) with inverse $\Psi$. The last sentence is Proposition [[§21 Linear Algebra Toolkit#^prop-21-7|§21.7]](1), carried across $\Theta$.

^pf-31-4

*Uses:* [[§28 Derivations and the Abstract Tangent Space#^lem-28-2|§28.2]], [[§28 Derivations and the Abstract Tangent Space#^def-28-6|Def. §28.6]], [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]], [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-5|§29.5]], [[§19 Smooth Functions and Smooth Maps#^prop-19-8|§19.8]], [[§19 Smooth Functions and Smooth Maps#^def-19-7|Def. §19.7]], [[§19 Smooth Functions and Smooth Maps#^def-19-8|Def. §19.8]], [[§21 Linear Algebra Toolkit#^prop-21-7|§21.7]], [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]]

![[m591-12-16.svg]]

![[m591-12-17.svg]]
*The slice inclusions and the projections through $p$. The four identities $\pi_1 \iota_1 = \mathrm{id}$, $\pi_2 \iota_2 = \mathrm{id}$, and $\pi_2 \iota_1$, $\pi_1 \iota_2$ constant, pushed forward to tangent spaces, are the whole proof that $\Psi \circ \Theta = \mathrm{id}$.*

> [!remark]- Connections
> - Linear algebra of products and direct sums: [[§11 Products and Quotients of Vector Spaces#^ladr-3-92|LADR 3.92]] (dimension of a product), [[§11 Products and Quotients of Vector Spaces#^ladr-3-93|LADR 3.93]] (products and direct sums).
> - The product smooth structure it rests on: [[§19 Smooth Functions and Smooth Maps#^prop-19-8|§19.8]]; projections of products are submersions: [[§34 Submersions#^ex-34-2|Ex. §34.2]].

**Partial derivatives in the $M_1$ variables.** For $v \in T_{p_1}M_1$ and a germ $[f]$ at $p$,

$$
(\iota_{1*}v)[f] = v\big[f \circ \iota_1\big], \qquad (f \circ \iota_1)(q) = f(q, p_2) :
$$

to push $v$ forward, restrict $f$ to the slice $M_1 \times \{p_2\}$ and differentiate there. So the first summand consists of derivations “only with respect to the $M_1$ variables”, with $p_2$ held fixed — partial derivatives in the direction of $M_1$ — and the second of partial derivatives in the direction of $M_2$.

![[m591-12-18.svg]]
*The isomorphism in one picture. Through $p$ run the two slices, $M_1 \times \{p_2\}$ and $\{p_1\} \times M_2$. Pushing $v$ and $w$ forward along the slice inclusions gives tangent vectors along the slices, and every $D \in T_p(M_1 \times M_2)$ is uniquely their sum. The projections take $D$ back to $v$ and $w$: $\Psi(D) = (\pi_{1\ast}D, \pi_{2\ast}D) = (v, w)$.*

> [!theorem] Corollary §31.5: Product Coordinates
> In product coordinates $(x^1, \ldots, x^{m_1}, y^1, \ldots, y^{m_2})$ at $p$,
>
> $$
> \iota_{1*}\Big(\frac{\partial}{\partial x^i}\Big|_{p_1}\Big) = \frac{\partial}{\partial x^i}\Big|_p, \qquad \iota_{2*}\Big(\frac{\partial}{\partial y^j}\Big|_{p_2}\Big) = \frac{\partial}{\partial y^j}\Big|_p .
> $$
>
> So the $\partial/\partial x^i|_p$ form a basis of the first summand and the $\partial/\partial y^j|_p$ a basis of the second.
>
> *Lee: Proposition 3.14*

^cor-31-5

> [!proof]+ Proof
> By Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-9|§19.9]] the coordinate representation of $\iota_1$ is $r \mapsto (r, \varphi_2(p_2))$, with Jacobian $\binom{I_{m_1}}{0}$. By Theorem [[§30 The Differential in Coordinates#^thm-30-2|§30.2]] its $i$-th column says $\iota_{1*}(\partial/\partial x^i|_{p_1}) = \partial/\partial x^i|_p$. The same for $\iota_2$.

^pf-31-5

*Uses:* [[§19 Smooth Functions and Smooth Maps#^prop-19-9|§19.9]], [[§30 The Differential in Coordinates#^thm-30-2|§30.2]], [[§31 Tangent Vectors as Velocities of Curves#^thm-31-4|§31.4]]

> [!theorem] Corollary §31.6: Velocities of Curves in a Product
> Let $\gamma = (\gamma_1, \gamma_2)$ be a smooth curve in $M_1 \times M_2$ with $\gamma(0) = p$. Then $\Psi(D_\gamma) = (D_{\gamma_1}, D_{\gamma_2})$, that is, $D_\gamma = \iota_{1*}D_{\gamma_1} + \iota_{2*}D_{\gamma_2}$. In particular, if $\gamma_2$ is constant — a “horizontal” curve $\gamma(t) = (\gamma_1(t), p_2)$ — then $D_\gamma = \iota_{1*}D_{\gamma_1}$ lies in the first summand.

^cor-31-6

> [!proof]+ Proof
> $\gamma_i = \pi_i \circ \gamma$, so $\pi_{i*}D_\gamma = D_{\pi_i \circ \gamma} = D_{\gamma_i}$ by Corollary [[§31 Tangent Vectors as Velocities of Curves#^cor-31-3|§31.3]]. If $\gamma_2$ is constant, $D_{\gamma_2} = 0$.

^pf-31-6

*Uses:* [[§31 Tangent Vectors as Velocities of Curves#^cor-31-3|§31.3]], [[§31 Tangent Vectors as Velocities of Curves#^thm-31-4|§31.4]], [[§31 Tangent Vectors as Velocities of Curves#^def-31-2|Def. §31.2]]

This is the second of Uribe's three views, and it uses the velocities of Assignment 3, Problem 2 ([[§31 Tangent Vectors as Velocities of Curves|§31, Tangent Vectors as Velocities of Curves]]).
