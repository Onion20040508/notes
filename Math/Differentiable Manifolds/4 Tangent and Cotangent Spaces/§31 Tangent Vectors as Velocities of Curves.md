---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 4
section: 31
tags: [differentiable-manifolds, math591]
---
← [[§30 The Differential in Coordinates]] · ↑ [[· 4 Tangent and Cotangent Spaces]] · [[§32 The Cotangent Space]] →

*Stage: abstract — The other face of a tangent vector: every derivation is the velocity of a curve, on every manifold. Tangent spaces of products split.*

*Assignment 3, Problem 2.* Tangent vectors were introduced with two faces: velocities of curves, and derivations (the [[§28 Derivations and the Abstract Tangent Space#^rem-28-1|remark]] at the start of [[§28 Derivations and the Abstract Tangent Space|§28, Derivations and the Abstract Tangent Space]]). For regular level sets the two were identified by Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-7|§29.7]], through the ambient space. This section identifies them on *every* smooth manifold, with no ambient space at all.

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
> Three things are claimed: $D_\gamma$ is a derivation at $p$; its coefficients in the basis $\partial/\partial x^j|_p$ are the $(x^j \circ \gamma)'(0)$; and so it depends only on $(\varphi \circ \gamma)'(0)$.
>
> *$D_\gamma$ is a derivation.* The interval $J$ is an open subset of $\mathbb{R}$ with the identity chart $t$, and $d/dt|_0$ is the coordinate derivation of this chart at $0$ (Definition [[§29 Coordinate Derivations and the Basis Theorem#^def-29-2|§29.2]]: the coordinate representation of $f$ in the identity chart is $f$ itself, so $d/dt|_0[f] = f'(0)$); it is a derivation at $0$ by Proposition [[§29 Coordinate Derivations and the Basis Theorem#^prop-29-2|§29.2]]. $D_\gamma = \gamma_{\ast 0}(d/dt|_0)$ is a pushforward of a derivation along the smooth map $\gamma$, hence a derivation at $\gamma(0) = p$ (Proposition [[§28 Derivations and the Abstract Tangent Space#^prop-28-5|§28.5]]) — which is why Assignment 3 could waive the check.
>
> *The coefficients.* By the universal formula (Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]]), applied to $D_\gamma \in T_pM$ in the chart $(U, \varphi)$,
>
> $$
> D_\gamma = \sum_{j=1}^n D_\gamma\big[x^j\big]\, \frac{\partial}{\partial x^j}\Big|_p ,
> $$
>
> so the $j$-th coefficient of $D_\gamma$ is $D_\gamma[x^j]$. The function $x^j \circ \gamma$ is defined on the open set $\gamma^{-1}(U) \ni 0$ ($\gamma$ is continuous), and by the explicit formula of Definition [[§31 Tangent Vectors as Velocities of Curves#^def-31-2|§31.2]], which is the definition of the pushforward,
>
> $$
> D_\gamma\big[x^j\big] = \gamma_{\ast 0}\Big(\frac{d}{dt}\Big|_0\Big)\big[x^j\big] = \frac{d}{dt}\Big|_{t=0} \big(x^j \circ \gamma\big)(t) = \big(x^j \circ \gamma\big)'(0) .
> $$
>
> Substituting into the universal formula gives the displayed formula.
>
> *Dependence on the coordinate curve.* By Definition [[§29 Coordinate Derivations and the Basis Theorem#^def-29-1|§29.1]](2), $x^j = r^j \circ \varphi$, so $x^j \circ \gamma = r^j \circ (\varphi \circ \gamma)$ is the $j$-th component of the coordinate curve $\varphi \circ \gamma$, and $(x^j \circ \gamma)'(0)$ is the $j$-th component of $(\varphi \circ \gamma)'(0) \in \mathbb{R}^n$. So all the coefficients of $D_\gamma$ are read off from $(\varphi \circ \gamma)'(0)$, and two curves through $p$ with the same velocity of their coordinate curves have the same $D_\gamma$.

^pf-31-1

*Uses:* [[§31 Tangent Vectors as Velocities of Curves#^def-31-2|Def. §31.2]], [[§28 Derivations and the Abstract Tangent Space#^prop-28-5|§28.5]], [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]], [[§29 Coordinate Derivations and the Basis Theorem#^def-29-2|Def. §29.2]], [[§29 Coordinate Derivations and the Basis Theorem#^prop-29-2|§29.2]], [[§29 Coordinate Derivations and the Basis Theorem#^def-29-1|Def. §29.1]]

The same formula comes out of the chain rule directly, as in the assignment's solution. With $c = \varphi \circ \gamma$ and $c^j = r^j \circ c = x^j \circ \gamma$, near $0$ one has $f \circ \gamma = f_\varphi \circ c$, so

$$
D_\gamma[f] = \frac{d}{dt}\Big|_0 f_\varphi\big(c(t)\big) = \sum_{j} \frac{\partial f_\varphi}{\partial r^j}\big(\varphi(p)\big)\,(c^j)'(0) = \sum_j (c^j)'(0)\,\frac{\partial}{\partial x^j}\Big|_p[f].
$$

Each input $r^j$ of $f_\varphi$ moves at speed $(c^j)'(0)$ along the curve, and contributes $\partial f_\varphi/\partial r^j \cdot (c^j)'(0)$ to the rate of change.

> [!definition] Definition §31.3: Velocity at Time $t$
> Let $\gamma : J \to M$ be a smooth curve and $t_0 \in J$. The **velocity** of $\gamma$ at time $t_0$ is
>
> $$
> \dot\gamma(t_0) = \frac{d\gamma}{dt}(t_0) := \gamma_{\ast t_0}\Big(\frac{d}{dt}\Big|_{t_0}\Big) \in T_{\gamma(t_0)}M, \qquad\text{explicitly}\qquad \dot\gamma(t_0)[f] = \frac{d}{dt}\Big|_{t=t_0} f\big(\gamma(t)\big)
> $$
>
> for a germ $f$ at $\gamma(t_0)$.
>
> *Lee: Ch. 3, Velocity Vectors of Curves*

^def-31-3

*(Added; the notes had the velocity only at time $0$, Definition [[§31 Tangent Vectors as Velocities of Curves#^def-31-2|§31.2]], and used it at other times informally.)* There is no difference quotient on $M$, so the velocity is a tangent vector: the pushforward of the coordinate tangent vector $\frac{d}{dt}|_{t_0}$ of the $1$-manifold $J$; and the right-hand side of the explicit formula is the ordinary derivative of the real function $f \circ \gamma$, so the definition makes sense on any manifold. It is the velocity at $0$ of the shifted curve $\sigma(s) = \gamma(t_0 + s)$, since $\frac{d}{ds}|_0 f(\gamma(t_0 + s)) = \frac{d}{dt}|_{t_0} f(\gamma(t))$: so $\dot\gamma(t_0) = D_\sigma$, and $\dot\gamma(0) = D_\gamma$ when $0 \in J$. (Lee writes $\gamma'(t_0)$; these notes keep $\gamma'$ for the ordinary derivative of a curve in $\mathbb{R}^N$, as for $D_\gamma$.)

> [!theorem] Corollary §31.2: Velocity at Time $t$ in Coordinates
> Let $\gamma : J \to M$ be smooth, $t_0 \in J$, and $(U, \varphi)$ a chart at $\gamma(t_0)$ with coordinate functions $x^1, \ldots, x^n$. Then
>
> $$
> \dot\gamma(t_0) = \sum_{j=1}^n \big(x^j \circ \gamma\big)'(t_0)\, \frac{\partial}{\partial x^j}\Big|_{\gamma(t_0)} .
> $$
>
> Writing $x^j(t) = x^j(\gamma(t))$, this is $\dot\gamma = \sum_j \dot x^j\, \partial/\partial x^j$.
>
> *Lee: Ch. 3, Velocity Vectors of Curves*

^cor-31-2

> [!proof]+ Proof
> *(Not from lecture.)* Let $\sigma(s) = \gamma(t_0 + s)$, a smooth curve with $\sigma(0) = \gamma(t_0)$, so $\dot\gamma(t_0) = D_\sigma$ (Definition [[§31 Tangent Vectors as Velocities of Curves#^def-31-3|§31.3]] and the paragraph after it). By Velocity in Coordinates (Proposition [[§31 Tangent Vectors as Velocities of Curves#^prop-31-1|§31.1]]), $D_\sigma = \sum_j (x^j \circ \sigma)'(0)\, \partial/\partial x^j|_{\gamma(t_0)}$, and by the chain rule in one variable $(x^j \circ \sigma)'(0) = \frac{d}{ds}|_0\, x^j(\gamma(t_0 + s)) = (x^j \circ \gamma)'(t_0)$.

^pf-31-2

*Uses:* [[§31 Tangent Vectors as Velocities of Curves#^def-31-3|Def. §31.3]], [[§31 Tangent Vectors as Velocities of Curves#^prop-31-1|§31.1]]

The coefficients are ordinary derivatives, computed *downstairs* on the coordinate curve $\varphi \circ \gamma$ in $\mathbb{R}^n$; the basis vectors live *upstairs* in $T_{\gamma(t_0)}M$, and were themselves defined by going downstairs, $\frac{\partial}{\partial x^j}\big|_p[f] = \frac{\partial f_\varphi}{\partial r^j}(\varphi(p))$ (Definition [[§29 Coordinate Derivations and the Basis Theorem#^def-29-2|§29.2]]).

> [!theorem] Proposition §31.3: Velocity at Time $t$ in a Level Set
> Let $M = F^{-1}(c) \subseteq \mathbb{R}^{n+k}$ be a regular level set and $\gamma : J \to M$ a smooth curve, $t_0 \in J$. Then the ordinary derivative $\gamma'(t_0)$ lies in $T^{\mathrm{geo}}_{\gamma(t_0)}M$, and $\dot\gamma(t_0) = D_{\gamma'(t_0)}$: under the isomorphism $v \mapsto D_v$ of Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-7|§29.7]], the abstract velocity is the ordinary derivative.
>
> *Lee: Ch. 3, Velocity Vectors of Curves*

^prop-31-3

> [!proof]+ Proof
> *(Not from lecture.)* $\gamma$ is smooth into $M$, hence smooth as a curve in $\mathbb{R}^{n+k}$. Let $\sigma(s) = \gamma(t_0 + s)$ for small $|s|$: a smooth curve in $\mathbb{R}^{n+k}$ with values in $M$, $\sigma(0) = \gamma(t_0)$ and $\sigma'(0) = \gamma'(t_0)$. So $\gamma'(t_0) \in T^{\mathrm{geo}}_{\gamma(t_0)}M$ by Definition [[§25 The Geometric Tangent Space#^def-25-1|§25.1]]. For a germ $f$ at $\gamma(t_0)$, Proposition [[§25 The Geometric Tangent Space#^prop-25-8|§25.8]](2), applied to the curve $\sigma$, gives $D_{\gamma'(t_0)}[f] = \frac{d}{ds}\big|_{0} f(\sigma(s)) = \frac{d}{dt}\big|_{t_0} f(\gamma(t)) = \dot\gamma(t_0)[f]$.

^pf-31-3

*Uses:* [[§25 The Geometric Tangent Space#^def-25-1|Def. §25.1]], [[§25 The Geometric Tangent Space#^prop-25-8|§25.8]]

> [!theorem] Theorem §31.4: Every Tangent Vector Is a Velocity
> For every $D \in T_pM$ there is a smooth curve $\gamma : (-\varepsilon, \varepsilon) \to M$ with $\gamma(0) = p$ and $D_\gamma = D$.
>
> *Lee: Proposition 3.23*

^thm-31-4

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

^pf-31-4

*Uses:* [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]], [[§31 Tangent Vectors as Velocities of Curves#^prop-31-1|§31.1]], [[§29 Coordinate Derivations and the Basis Theorem#^def-29-1|Def. §29.1]], [[§31 Tangent Vectors as Velocities of Curves#^def-31-1|Def. §31.1]], [[§31 Tangent Vectors as Velocities of Curves#^def-31-2|Def. §31.2]], [[§19 Smooth Functions and Smooth Maps#^def-19-3|Def. §19.3]]

Assignment 3's solution first treats the basis vectors $\partial/\partial x^i|_p$, using curves with $c'(0) = e_i$, and then the general case. The general argument contains the basis case, with $a = e_i$ and $c(t) = \varphi(p) + t\,e_i$, so it is presented here alone.

> [!theorem] Corollary §31.5: Velocity of a Composite — Computing Differentials by Curves
> Let $F : M \to N$ be smooth and $\gamma$ a smooth curve in $M$ with $\gamma(0) = p$. Then $D_{F \circ \gamma} = F_{*p}(D_\gamma)$. Consequently, for every $D \in T_pM$,
>
> $$
> F_{*p}(D) = D_{F \circ \gamma} \qquad \text{for any smooth curve } \gamma \text{ with } \gamma(0) = p \text{ and } D_\gamma = D,
> $$
>
> and such a curve exists by Theorem [[§31 Tangent Vectors as Velocities of Curves#^thm-31-4|§31.4]].
>
> *Lee: Proposition 3.24 and Corollary 3.25*

^cor-31-5

> [!proof]+ Proof
> *The identity $D_{F \circ \gamma} = F_{\ast p}(D_\gamma)$.* The composite $F \circ \gamma : J \to N$ is a smooth curve (Lemma [[§19 Smooth Functions and Smooth Maps#^lem-19-5|§19.5]]) with $(F \circ \gamma)(0) = F(p)$, so its velocity $D_{F \circ \gamma} \in T_{F(p)}N$ is defined. The Chain Rule (Theorem [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]]), applied to the maps $\gamma : J \to M$ and $F : M \to N$ at the point $0 \in J$, reads $(F \circ \gamma)_{\ast 0} = F_{\ast \gamma(0)} \circ \gamma_{\ast 0} = F_{\ast p} \circ \gamma_{\ast 0}$. Hence, using Definition [[§31 Tangent Vectors as Velocities of Curves#^def-31-2|§31.2]] at the first and last steps,
>
> $$
> D_{F \circ \gamma} = (F \circ \gamma)_{\ast 0}\Big(\frac{d}{dt}\Big|_0\Big) = F_{\ast p}\Big(\gamma_{\ast 0}\Big(\frac{d}{dt}\Big|_0\Big)\Big) = F_{\ast p}(D_\gamma) .
> $$
>
> *Consequence.* Let $D \in T_pM$ and let $\gamma$ be any smooth curve with $\gamma(0) = p$ and $D_\gamma = D$; such a curve exists by Theorem [[§31 Tangent Vectors as Velocities of Curves#^thm-31-4|§31.4]]. Then, by the identity just proved, $F_{\ast p}(D) = F_{\ast p}(D_\gamma) = D_{F \circ \gamma}$.

^pf-31-5

*Uses:* [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]], [[§31 Tangent Vectors as Velocities of Curves#^def-31-2|Def. §31.2]], [[§31 Tangent Vectors as Velocities of Curves#^def-31-1|Def. §31.1]], [[§31 Tangent Vectors as Velocities of Curves#^thm-31-4|§31.4]], [[§19 Smooth Functions and Smooth Maps#^lem-19-5|§19.5]]

This is Lee's main computational tool: to find $F_{*p}(D)$, choose any curve with velocity $D$ and differentiate $F$ along it. It is the manifold version of Theorem [[§22 The Differential of a Map Between Vector Spaces#^thm-22-3|§22.3]], and it is how Lee computes the differential of the determinant (Problem 7-4).
*(Computed; not from lecture.)* With $m = \dim M$, $n = \dim N$, charts $(U, \varphi = (x^1, \ldots, x^m))$ at $p$ and $(V, \psi = (y^1, \ldots, y^n))$ at $F(p)$ with $F(U) \subseteq V$, and $F^j = y^j \circ F$, the coefficients of $D_\gamma$ and $D_{F \circ \gamma}$ are $(x^i \circ \gamma)'(0)$ and $(y^j \circ F \circ \gamma)'(0)$ (Proposition [[§31 Tangent Vectors as Velocities of Curves#^prop-31-1|§31.1]]), and by Theorem [[§30 The Differential in Coordinates#^thm-30-2|§30.2]] the identity $D_{F \circ \gamma} = F_{\ast p}(D_\gamma)$ reads

$$
\begin{pmatrix} (y^1 \circ F \circ \gamma)'(0) \\ \vdots \\ (y^n \circ F \circ \gamma)'(0) \end{pmatrix}
= \begin{pmatrix}
\dfrac{\partial F^1}{\partial x^1}(p) & \cdots & \dfrac{\partial F^1}{\partial x^m}(p) \\[2mm]
\vdots & & \vdots \\[1mm]
\dfrac{\partial F^n}{\partial x^1}(p) & \cdots & \dfrac{\partial F^n}{\partial x^m}(p)
\end{pmatrix}
\begin{pmatrix} (x^1 \circ \gamma)'(0) \\ \vdots \\ (x^m \circ \gamma)'(0) \end{pmatrix} :
$$

the Jacobian carries the velocity of the coordinate curve $\varphi \circ \gamma$ to that of $\psi \circ F \circ \gamma$.

![[m591-12-14.svg]]
*The proof in one picture. Downstairs, in the chart, the curve is the straight line through $\varphi(p)$ in the direction of the coefficient vector $a = (D[x^1], \ldots, D[x^n])$. The chart carries it upstairs to a curve $\gamma$ in $M$, bent by whatever distortion $\varphi^{-1}$ introduces. The bending is invisible to the velocity, which depends only on $(\varphi \circ \gamma)'(0) = a$ — so the velocity is $D$.*

![[m591-12-a1.gif|420]]

*(Not from lecture; animation added, vault only.)* Four curves on $S^2$ through $p$ with the same velocity $v$, built as $\gamma_k(t) = (p + tv + t^2w_k)/|\cdot|$ with different $w_k$ (chosen for the picture). They bend apart at second order; zooming in at $p$, they become one straight segment along $v$. A tangent vector is what all of them share.

![[m591-12-15.svg]]
*The same construction as a diagram: the curve is built downstairs as $c$ and lifted by $\varphi^{-1}$, and the triangle commutes, $\varphi \circ \gamma = c$.*

> [!remark] Remark: The Two Faces Reconciled
> Theorem [[§31 Tangent Vectors as Velocities of Curves#^thm-31-4|§31.4]] says the map $\gamma \mapsto D_\gamma$, from smooth curves through $p$ to $T_pM$, is onto. By Proposition [[§31 Tangent Vectors as Velocities of Curves#^prop-31-1|§31.1]], two curves have the same velocity exactly when their coordinate curves have the same velocity in one chart, and then in every chart. So $T_pM$ may equally be described as *curves through $p$, modulo having the same velocity in coordinates* — the intrinsic “velocities of curves” definition of the tangent space, now a theorem, on every manifold, with no ambient space. For a regular level set, the abstract velocity $D_\gamma$ is the derivation $D_{\gamma'(0)}$ attached to the geometric velocity $\gamma'(0) \in T^{\mathrm{geo}}_pM$ (Proposition [[§25 The Geometric Tangent Space#^prop-25-8|§25.8]](2)). So the identification of Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-7|§29.7]] is the statement that the two notions of velocity agree.

^rem-31-1

> [!remark] Remark: From Lecture 17 On: One Tangent Space
> *Lecture 17, “something that I didn't say explicitly, and I want to say it explicitly.”* For $M \subseteq \mathbb{R}^N$ the course built two tangent spaces at $p$: the [[§25 The Geometric Tangent Space#^def-25-1|geometric one]], $T^{\mathrm{geo}}_pM \subseteq \mathbb{R}^N$, a vector subspace consisting of the velocities $\gamma'(0)$ of curves $\gamma : (-\varepsilon, \varepsilon) \to M$ with $\gamma(0) = p$; and the [[§28 Derivations and the Abstract Tangent Space#^def-28-2|abstract one]], $T_pM$, the [[§28 Derivations and the Abstract Tangent Space#^def-28-1|derivations]] of [[§27 Germs#^def-27-2|germs]] at $p$. The homework (Theorem [[§31 Tangent Vectors as Velocities of Curves#^thm-31-4|§31.4]], Assignment 3, Problem 2) showed that every derivation is realized by a curve, $D = D_\gamma$, and $D_\gamma = D_{\gamma'(0)}$ (the remark *[[§31 Tangent Vectors as Velocities of Curves#^rem-31-1|The Two Faces Reconciled]]* in [[§31 Tangent Vectors as Velocities of Curves|§31]]). So the two are identified,
>
> $$
> T^{\mathrm{geo}}_pM \;\cong\; T_pM, \qquad \gamma'(0) \longleftrightarrow D_\gamma ,
> $$
>
> and *from now on the course always makes this identification, “without further notice”*: “if you're working with submanifolds of $\mathbb{R}^n$, you can use a geometric tangent space in your computations, and we know that that agrees with the abstract notion.” For a regular level set the precise statement is Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-7|§29.7]]. Earlier chapters keep the notations $T^{\mathrm{geo}}_pM$ and $T_pM$ apart, and are left as they are.

^rem-31-2

> [!remark] Remark: Review Session: The Two Definitions of $T_pM$
> *Review session, Oct 16, in answer to “we have a lot of characterizations of the tangent space, like derivations and curves.”* “Those are the only two” — the ambient one is “more or less the same as curves.” For a regular submanifold $M \subseteq \mathbb{R}^N$, the ambient tangent space is $\{\, \dot{\tilde\gamma}(0) : \gamma : (-\varepsilon, \varepsilon) \to M,\ \gamma(0) = p \,\}$, where $\tilde\gamma = \iota \circ \gamma$ is $\gamma$ regarded as a curve in $\mathbb{R}^N$: the derivative $\dot{\tilde\gamma}(0)$ “uses the vector space structure of the ambient space,” through the difference quotient. “Ambient” is “our terminology … used in this classroom, nowhere else in the world. But I find it … pedagogically useful.” On an abstract manifold, $T_pM$ is the space of derivations of germs. The bridge is the homework proposition: a curve $\gamma$ through $p$ defines a derivation, $D_\gamma[f] = \frac{d}{dt}\big|_{0} f(\gamma(t))$, the $\dot\gamma(0)$ of the lecture (Definition [[§31 Tangent Vectors as Velocities of Curves#^def-31-2|§31.2]]), and every derivation arises this way (Theorem [[§31 Tangent Vectors as Velocities of Curves#^thm-31-4|§31.4]]); this is what identifies the two for $M \subseteq \mathbb{R}^N$ (Remark [[§31 Tangent Vectors as Velocities of Curves#^rem-31-2|remark]]). Lee's order of definitions differs: “everybody does it a little bit differently.”

^rem-31-3

> [!remark]- Connections
> - The two tangent spaces side by side: [[§45 Geometric and Abstract Manifolds#Tangent Vectors|§45, Tangent Vectors]].
> - The identification for a regular level set: [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-7|Theorem §29.7]].

## Tangent Spaces of Products

*Lecture 11. “There is a natural isomorphism” between the tangent space of a product and the direct sum of the tangent spaces of the factors — “natural meaning coordinate-free.” Uribe gave three ways to see it: by the inclusions of the factors, by curves, and in coordinates. He added that this part of the course is, in his experience, “the most abstract, somehow the hardest part”, and that while physicists tend to favour coordinates and pure mathematicians abstract settings, “you need both.”*

Throughout, $p = (p_1, p_2) \in M_1 \times M_2$, and $\iota_1 = \iota^{p_2} : M_1 \to M_1 \times M_2$, $\iota_2 = \iota^{p_1} : M_2 \to M_1 \times M_2$ are the slice inclusions through $p$ (Definition [[§19 Smooth Functions and Smooth Maps#^def-19-8|§19.8]]).

> [!theorem] Theorem §31.6: The Tangent Space of a Product
> The linear map
>
> $$
> \Theta : T_{p_1}M_1 \oplus T_{p_2}M_2 \longrightarrow T_p(M_1 \times M_2), \qquad \Theta(v, w) = \iota_{1*}v + \iota_{2*}w,
> $$
>
> is an isomorphism, defined without charts, with inverse $\Psi(D) = (\pi_{1*}D, \pi_{2*}D)$. In particular $\iota_{1*}$ and $\iota_{2*}$ are injective, and $T_p(M_1 \times M_2)$ is the internal direct sum of their images, $\Theta\big(T_{p_1}M_1 \oplus \{0\}\big)$ and $\Theta\big(\{0\} \oplus T_{p_2}M_2\big)$.
>
> *Lee: Proposition 3.14*

^thm-31-6

> [!proof]+ Proof
> *(Stated in lecture; Uribe left the injectivity as “check”.)* To show: $\Theta$ is a linear bijection with inverse $\Psi$; then the two consequences in the last sentence.
>
> *The maps.* Since $\iota_1(p_1) = (p_1, p_2) = p$ and $\iota_2(p_2) = p$, the pushforwards are $\iota_{1\ast} = (\iota_1)_{\ast p_1} : T_{p_1}M_1 \to T_pM$ and $\iota_{2\ast} = (\iota_2)_{\ast p_2} : T_{p_2}M_2 \to T_pM$, where $M = M_1 \times M_2$; since $\pi_i(p) = p_i$, also $\pi_{i\ast} = (\pi_i)_{\ast p} : T_pM \to T_{p_i}M_i$. All four maps $\iota_i$, $\pi_i$ are smooth (Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-11|§19.11]]), so the four pushforwards are linear (Proposition [[§28 Derivations and the Abstract Tangent Space#^prop-28-5|§28.5]]). Hence $\Theta(v, w) = \iota_{1\ast}v + \iota_{2\ast}w$ and $\Psi(D) = (\pi_{1\ast}D, \pi_{2\ast}D)$ are linear, with the componentwise operations of the direct sum (Definition [[§21 Linear Algebra Toolkit#^def-21-7|§21.7]]). They are built from pushforwards alone, so no chart is involved.
>
> *The pushforward along a constant map is zero.* By Lemma [[§28 Derivations and the Abstract Tangent Space#^lem-28-10|§28.10]](1), if $\kappa : X \to Y$ is constant, then $\kappa_{\ast x} = 0$ for every $x \in X$: for every $D \in T_xX$ and every germ $[g]$ at the value of $\kappa$, $(\kappa_{\ast x}D)[g] = D[g \circ \kappa] = 0$, since $g \circ \kappa$ is constant and derivations kill constants.
>
> *Four identities.* For $q \in M_1$, $\pi_1(\iota_1(q)) = \pi_1(q, p_2) = q$ and $\pi_2(\iota_1(q)) = \pi_2(q, p_2) = p_2$; for $q \in M_2$, $\pi_2(\iota_2(q)) = \pi_2(p_1, q) = q$ and $\pi_1(\iota_2(q)) = p_1$. So $\pi_1 \circ \iota_1 = \mathrm{id}_{M_1}$ and $\pi_2 \circ \iota_2 = \mathrm{id}_{M_2}$, while $\pi_2 \circ \iota_1$ and $\pi_1 \circ \iota_2$ are constant. By the Chain Rule (Theorem [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]]), which also gives $(\mathrm{id})_\ast = \mathrm{id}$, and the previous step for the constant maps $\pi_2 \circ \iota_1$ and $\pi_1 \circ \iota_2$ — that is, Lemma [[§28 Derivations and the Abstract Tangent Space#^lem-28-10|§28.10]](2) with $F = \pi_2$, $\iota = \iota_1$ and with $F = \pi_1$, $\iota = \iota_2$ —
>
> $$
> \pi_{1\ast}\iota_{1\ast} = \mathrm{id}, \qquad \pi_{2\ast}\iota_{2\ast} = \mathrm{id}, \qquad \pi_{2\ast}\iota_{1\ast} = 0, \qquad \pi_{1\ast}\iota_{2\ast} = 0 .
> $$
>
> *$\Psi \circ \Theta = \mathrm{id}$.* For $(v, w) \in T_{p_1}M_1 \oplus T_{p_2}M_2$, by the linearity of $\pi_{1\ast}$ and $\pi_{2\ast}$ and the four identities,
>
> $$
> \Psi\big(\Theta(v, w)\big) = \big(\pi_{1\ast}\iota_{1\ast}v + \pi_{1\ast}\iota_{2\ast}w,\ \pi_{2\ast}\iota_{1\ast}v + \pi_{2\ast}\iota_{2\ast}w\big) = (v + 0,\ 0 + w) = (v, w) .
> $$
>
> So $\Theta$ is injective: if $\Theta(v, w) = 0$, then $(v, w) = \Psi(\Theta(v,w)) = \Psi(0) = 0$.
>
> *$\Theta$ is an isomorphism with inverse $\Psi$.* Both spaces have dimension $m_1 + m_2$: $\dim T_{p_i}M_i = m_i$ (Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]]), so $\dim(T_{p_1}M_1 \oplus T_{p_2}M_2) = m_1 + m_2$ (Proposition [[§21 Linear Algebra Toolkit#^prop-21-7|§21.7]](2)); and $M_1 \times M_2$ has dimension $m_1 + m_2$ (Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-10|§19.10]]), so $\dim T_p(M_1 \times M_2) = m_1 + m_2$ (Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]]). An injective linear map between spaces of the same finite dimension is bijective (Proposition [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]](1)). So $\Theta$ is an isomorphism, and composing $\Psi \circ \Theta = \mathrm{id}$ on the right with $\Theta^{-1}$ gives $\Psi = \Theta^{-1}$.
>
> *The last sentence.* $\iota_{1\ast}v = \iota_{1\ast}v + \iota_{2\ast}0 = \Theta(v, 0)$, and $\pi_{1\ast}\iota_{1\ast} = \mathrm{id}$, so $\iota_{1\ast}$ is injective (if $\iota_{1\ast}v = 0$ then $v = \pi_{1\ast}\iota_{1\ast}v = 0$); likewise $\iota_{2\ast}w = \Theta(0, w)$ and $\pi_{2\ast}\iota_{2\ast} = \mathrm{id}$ make $\iota_{2\ast}$ injective. So the images of $\iota_{1\ast}$ and $\iota_{2\ast}$ are $\Theta(T_{p_1}M_1 \oplus \{0\})$ and $\Theta(\{0\} \oplus T_{p_2}M_2)$. By Proposition [[§21 Linear Algebra Toolkit#^prop-21-7|§21.7]](1), $T_{p_1}M_1 \oplus T_{p_2}M_2$ is the internal direct sum of $T_{p_1}M_1 \oplus \{0\}$ and $\{0\} \oplus T_{p_2}M_2$; carried across the isomorphism $\Theta$: every $D \in T_p(M_1 \times M_2)$ is $D = \Theta(\Psi D) = \Theta(v, 0) + \Theta(0, w)$ with $(v, w) = \Psi(D)$, and if also $D = \Theta(v', 0) + \Theta(0, w')$, then $\Theta(v, w) = \Theta(v', w')$ and injectivity gives $(v, w) = (v', w')$. So $T_p(M_1 \times M_2)$ is the internal direct sum of the two images (Definition [[§21 Linear Algebra Toolkit#^def-21-8|§21.8]]).

^pf-31-6

*Uses:* [[§19 Smooth Functions and Smooth Maps#^prop-19-11|§19.11]], [[§28 Derivations and the Abstract Tangent Space#^prop-28-5|§28.5]], [[§21 Linear Algebra Toolkit#^def-21-7|Def. §21.7]], [[§28 Derivations and the Abstract Tangent Space#^lem-28-10|§28.10]], [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]], [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]], [[§21 Linear Algebra Toolkit#^prop-21-7|§21.7]], [[§19 Smooth Functions and Smooth Maps#^prop-19-10|§19.10]], [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]], [[§21 Linear Algebra Toolkit#^def-21-8|Def. §21.8]]

![[m591-12-16.svg]]

![[m591-12-17.svg]]
*The slice inclusions and the projections through $p$. The four identities $\pi_1 \iota_1 = \mathrm{id}$, $\pi_2 \iota_2 = \mathrm{id}$, and $\pi_2 \iota_1$, $\pi_1 \iota_2$ constant, pushed forward to tangent spaces, are the whole proof that $\Psi \circ \Theta = \mathrm{id}$.*

> [!remark]- Connections
> - Linear algebra of products and direct sums: [[§11 Products and Quotients of Vector Spaces#^ladr-3-92|LADR 3.92]] (dimension of a product), [[§11 Products and Quotients of Vector Spaces#^ladr-3-93|LADR 3.93]] (products and direct sums).
> - The product smooth structure it rests on: [[§19 Smooth Functions and Smooth Maps#^prop-19-10|§19.10]]; projections of products are submersions: [[§36 Submersions#^ex-36-2|Ex. §36.2]].

**Partial derivatives in the $M_1$ variables.** For $v \in T_{p_1}M_1$ and a germ $[f]$ at $p$,

$$
(\iota_{1*}v)[f] = v\big[f \circ \iota_1\big], \qquad (f \circ \iota_1)(q) = f(q, p_2) :
$$

to push $v$ forward, restrict $f$ to the slice $M_1 \times \{p_2\}$ and differentiate there. So the first summand consists of derivations “only with respect to the $M_1$ variables”, with $p_2$ held fixed — partial derivatives in the direction of $M_1$ — and the second of partial derivatives in the direction of $M_2$.

![[m591-12-18.svg]]
*The isomorphism in one picture. Through $p$ run the two slices, $M_1 \times \{p_2\}$ and $\{p_1\} \times M_2$. Pushing $v$ and $w$ forward along the slice inclusions gives tangent vectors along the slices, and every $D \in T_p(M_1 \times M_2)$ is uniquely their sum. The projections take $D$ back to $v$ and $w$: $\Psi(D) = (\pi_{1\ast}D, \pi_{2\ast}D) = (v, w)$.*

> [!theorem] Corollary §31.7: Product Coordinates
> In product coordinates $(x^1, \ldots, x^{m_1}, y^1, \ldots, y^{m_2})$ at $p$,
>
> $$
> \iota_{1*}\Big(\frac{\partial}{\partial x^i}\Big|_{p_1}\Big) = \frac{\partial}{\partial x^i}\Big|_p, \qquad \iota_{2*}\Big(\frac{\partial}{\partial y^j}\Big|_{p_2}\Big) = \frac{\partial}{\partial y^j}\Big|_p .
> $$
>
> So the $\partial/\partial x^i|_p$ form a basis of the first summand and the $\partial/\partial y^j|_p$ a basis of the second.
>
> *Lee: Proposition 3.14*

^cor-31-7

> [!proof]+ Proof
> Let $(U_1, \varphi_1 = (x^1, \ldots, x^{m_1}))$ be a chart of $M_1$ at $p_1$ and $(U_2, \varphi_2 = (y^1, \ldots, y^{m_2}))$ a chart of $M_2$ at $p_2$; the product chart $(U_1 \times U_2, \varphi_1 \times \varphi_2)$ has the coordinate functions $x^i \circ \pi_1$ and $y^j \circ \pi_2$, written again $x^i$ and $y^j$ (Definition [[§19 Smooth Functions and Smooth Maps#^def-19-7|§19.7]]).
>
> *The first summand.* The slice inclusion $\iota_1$ maps $U_1$ into $U_1 \times U_2$, since $p_2 \in U_2$. By Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-11|§19.11]] its coordinate representation in the charts $\varphi_1$ and $\varphi_1 \times \varphi_2$ is $r \mapsto (r, \varphi_2(p_2))$ on $\varphi_1(U_1)$: its first $m_1$ components are $r \mapsto r^k$, and its last $m_2$ components are the constants $y^l(p_2)$. At $\varphi_1(p_1)$ the partial derivatives are $\partial r^k/\partial r^i = \delta^k_i$ and $0$ for the constants, so the Jacobian is
>
> $$
> \begin{pmatrix} I_{m_1} \\ 0 \end{pmatrix}
> \qquad (\text{$m_1$ rows from the $x$'s, then $m_2$ rows from the $y$'s}).
> $$
>
> By Theorem [[§30 The Differential in Coordinates#^thm-30-2|§30.2]], whose matrix entries are these Jacobian entries (Proposition [[§30 The Differential in Coordinates#^prop-30-1|§30.1]]), the $i$-th column says
>
> $$
> \iota_{1\ast }\Big(\frac{\partial}{\partial x^i}\Big|_{p_1}\Big) = \sum_{k=1}^{m_1} \delta^k_i\, \frac{\partial}{\partial x^k}\Big|_p + \sum_{l=1}^{m_2} 0 \cdot \frac{\partial}{\partial y^l}\Big|_p = \frac{\partial}{\partial x^i}\Big|_p .
> $$
>
> *The second summand.* The slice inclusion $\iota_2$ maps $U_2$ into $U_1 \times U_2$, and by Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-11|§19.11]] its coordinate representation is $s \mapsto (\varphi_1(p_1), s)$ on $\varphi_2(U_2)$: the first $m_1$ components are the constants $x^k(p_1)$, the last $m_2$ are $s \mapsto s^l$. Its Jacobian at $\varphi_2(p_2)$ is $\begin{pmatrix} 0 \\ I_{m_2} \end{pmatrix}$, and the $j$-th column says, by Theorem [[§30 The Differential in Coordinates#^thm-30-2|§30.2]],
>
> $$
> \iota_{2\ast }\Big(\frac{\partial}{\partial y^j}\Big|_{p_2}\Big) = \sum_{k=1}^{m_1} 0 \cdot \frac{\partial}{\partial x^k}\Big|_p + \sum_{l=1}^{m_2} \delta^l_j\, \frac{\partial}{\partial y^l}\Big|_p = \frac{\partial}{\partial y^j}\Big|_p .
> $$
>
> *The bases.* The $\partial/\partial x^i|_{p_1}$ form a basis of $T_{p_1}M_1$ (Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]]), and $\iota_{1\ast }$ is linear and injective (Theorem [[§31 Tangent Vectors as Velocities of Curves#^thm-31-6|§31.6]]). An injective linear map carries a basis of its domain to a basis of its image (the images span the image, and a linear relation among them pulls back to one among the originals). So the $\partial/\partial x^i|_p = \iota_{1\ast }(\partial/\partial x^i|_{p_1})$ form a basis of the first summand $\iota_{1\ast }(T_{p_1}M_1)$; in the same way, with $\iota_{2\ast }$ and the basis $\partial/\partial y^j|_{p_2}$ of $T_{p_2}M_2$, the $\partial/\partial y^j|_p$ form a basis of the second summand.
> *(Computed; not from lecture.)* Placing the two Jacobians side by side: in the basis $(\partial/\partial x^i|_{p_1}, 0), (0, \partial/\partial y^j|_{p_2})$ of $T_{p_1}M_1 \oplus T_{p_2}M_2$ and the product-coordinate basis of $T_p(M_1 \times M_2)$, the matrix of $\Theta(v, w) = \iota_{1\ast}v + \iota_{2\ast}w$ is
>
> $$
> \left(\begin{array}{c|c} I_{m_1} & 0 \\ \hline 0 & I_{m_2} \end{array}\right) = I_{m_1 + m_2},
> $$
>
> its first $m_1$ columns being the Jacobian of $\iota_1$ and its last $m_2$ columns that of $\iota_2$.

^pf-31-7

*Uses:* [[§19 Smooth Functions and Smooth Maps#^prop-19-11|§19.11]], [[§30 The Differential in Coordinates#^thm-30-2|§30.2]], [[§31 Tangent Vectors as Velocities of Curves#^thm-31-6|§31.6]], [[§19 Smooth Functions and Smooth Maps#^def-19-7|Def. §19.7]], [[§30 The Differential in Coordinates#^prop-30-1|§30.1]], [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]]

> [!theorem] Corollary §31.8: Velocities of Curves in a Product
> Let $\gamma = (\gamma_1, \gamma_2)$ be a smooth curve in $M_1 \times M_2$ with $\gamma(0) = p$. Then $\Psi(D_\gamma) = (D_{\gamma_1}, D_{\gamma_2})$, that is, $D_\gamma = \iota_{1*}D_{\gamma_1} + \iota_{2*}D_{\gamma_2}$. In particular, if $\gamma_2$ is constant — a “horizontal” curve $\gamma(t) = (\gamma_1(t), p_2)$ — then $D_\gamma = \iota_{1*}D_{\gamma_1}$ lies in the first summand.

^cor-31-8

> [!proof]+ Proof
> *The components.* The components of $\gamma$ are $\gamma_i = \pi_i \circ \gamma$, smooth curves (Lemma [[§19 Smooth Functions and Smooth Maps#^lem-19-5|§19.5]]) with $\gamma_i(0) = \pi_i(p) = p_i$. By Corollary [[§31 Tangent Vectors as Velocities of Curves#^cor-31-5|§31.5]], applied to the smooth map $\pi_i : M_1 \times M_2 \to M_i$ and the curve $\gamma$,
>
> $$
> \pi_{i\ast}D_\gamma = D_{\pi_i \circ \gamma} = D_{\gamma_i} \qquad (i = 1, 2).
> $$
>
> So $\Psi(D_\gamma) = (\pi_{1\ast}D_\gamma, \pi_{2\ast}D_\gamma) = (D_{\gamma_1}, D_{\gamma_2})$. Applying $\Theta = \Psi^{-1}$ (Theorem [[§31 Tangent Vectors as Velocities of Curves#^thm-31-6|§31.6]]),
>
> $$
> D_\gamma = \Theta\big(D_{\gamma_1}, D_{\gamma_2}\big) = \iota_{1\ast}D_{\gamma_1} + \iota_{2\ast}D_{\gamma_2} .
> $$
>
> *Horizontal curves.* If $\gamma_2$ is constant, $\gamma_2(t) = p_2$, then $D_{\gamma_2} = (\gamma_2)_{\ast0}(d/dt|_0) = 0$ by Definition [[§31 Tangent Vectors as Velocities of Curves#^def-31-2|§31.2]] and Lemma [[§28 Derivations and the Abstract Tangent Space#^lem-28-10|§28.10]](1), the pushforward along the constant map $\gamma_2$ being $0$. Explicitly, for every germ $[g]$ at $p_2$, $D_{\gamma_2}[g] = \frac{d}{dt}\big|_{t=0}\, g(p_2) = 0$, the derivative of a constant. So $D_{\gamma_2} = 0$, and $D_\gamma = \iota_{1\ast}D_{\gamma_1} + \iota_{2\ast}0 = \iota_{1\ast}D_{\gamma_1}$ lies in the first summand.

^pf-31-8

*Uses:* [[§19 Smooth Functions and Smooth Maps#^lem-19-5|§19.5]], [[§31 Tangent Vectors as Velocities of Curves#^cor-31-5|§31.5]], [[§31 Tangent Vectors as Velocities of Curves#^thm-31-6|§31.6]], [[§31 Tangent Vectors as Velocities of Curves#^def-31-2|Def. §31.2]], [[§28 Derivations and the Abstract Tangent Space#^lem-28-10|§28.10]]

This is the second of Uribe's three views, and it uses the velocities of Assignment 3, Problem 2 ([[§31 Tangent Vectors as Velocities of Curves|§31, Tangent Vectors as Velocities of Curves]]).

*Lecture 18. Uribe opened with this construction — “I realize that we can't prove the theorem of last time completely” without it — to finish the proof that left-invariant fields are smooth (Theorem [[§60 Lie Groups and Left-Invariant Vector Fields#^thm-60-7|§60.7]]). It is the partial derivative in the $M_1$ variables above, now with the base point in the other factor allowed to vary.*

> [!definition] Definition §31.4: Partial Derivative in One Factor
> Let $\varphi : M \times N \to \mathbb{R}$ be smooth, $p \in M$ and $v \in T_pM$. The **partial derivative of $\varphi$ in the direction $v$** is the function $\partial_v\varphi : N \to \mathbb{R}$,
>
> $$
> \partial_v\varphi(q) = \Theta(v, 0)[\varphi] = (\iota^q_{\ast}v)[\varphi] = v\big[\varphi(\cdot, q)\big], \qquad q \in N,
> $$
>
> where $\Theta(v, 0) \in T_{(p,q)}(M \times N)$ is the vector $(v, 0)$ under $T_{(p,q)}(M \times N) = T_pM \oplus T_qN$ (Theorem [[§31 Tangent Vectors as Velocities of Curves#^thm-31-6|§31.6]]), $0 \in T_qN$, and $\iota^q : M \to M \times N$, $x \mapsto (x, q)$, is the slice inclusion (Definition [[§19 Smooth Functions and Smooth Maps#^def-19-8|§19.8]]). In the same way, for $w \in T_qN$, the partial derivative **in the second variable** is $\partial_w\varphi : M \to \mathbb{R}$, $\partial_w\varphi(p) = \Theta(0, w)[\varphi] = w\big[\varphi(p, \cdot)\big]$.

^def-31-4

“This is our notation. I don't think it's in Lee.” The dependence on $q$ “is hidden in the fact that” the pair $(v, 0)$ is a tangent vector at $(p, q)$: the $0$ is the zero of $T_qN$, so the point at which $(v,0)$ sits moves with $q$. The three equal expressions in the definition are equal by the definition of $\Theta$ and of the pushforward (Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-6|§28.6]]): $\Theta(v, 0) = \iota^q_\ast v + \iota^p_\ast0 = \iota^q_\ast v$, and $(\iota^q_\ast v)[\varphi] = v[\varphi \circ \iota^q]$ with $(\varphi \circ \iota^q)(x) = \varphi(x, q)$.

> [!theorem] Proposition §31.9: Partial Derivatives by Curves and in Coordinates
> Let $\varphi \in C^\infty(M \times N)$, $p \in M$ and $v \in T_pM$.
>
> 1. If $\gamma : (-\varepsilon, \varepsilon) \to M$ is a smooth curve *adapted to $v$*, i.e. $\gamma(0) = p$ and $D_\gamma = v$, then for every $q \in N$
>
> $$
> \partial_v\varphi(q) = \frac{d}{dt}\Big|_{t=0} \varphi\big(\gamma(t), q\big).
> $$
>
> 2. In charts $(x^1, \ldots, x^m)$ near $p$ and $(y^1, \ldots, y^n)$ near $q$, if $v = \sum_{j=1}^m v^j\, \partial/\partial x^j|_p$, then
>
> $$
> \partial_v\varphi(q) = \sum_{j=1}^m v^j\, \frac{\partial\varphi}{\partial x^j}(p, q) .
> $$
>
> 3. $\partial_v\varphi \in C^\infty(N)$.
>
> The same holds in the second variable: for $w \in T_qN$, $\partial_w\varphi \in C^\infty(M)$.

^prop-31-9

> [!proof]+ Proof
> *(Lecture 18, in the lecture's order: curves, then coordinates, from which smoothness is read off. Details filled in.)*
>
> *1. Curves.* “Using curves, which I have said is a very good thing to do when you're working on manifolds”: $t \mapsto (\gamma(t), q) = \iota^q(\gamma(t))$ “is a horizontal curve … changing the first entry and not the second.” By the definition and Definition [[§31 Tangent Vectors as Velocities of Curves#^def-31-2|§31.2]],
>
> $$
> \partial_v\varphi(q) = v[\varphi \circ \iota^q] = D_\gamma[\varphi \circ \iota^q] = \frac{d}{dt}\Big|_{t=0} (\varphi \circ \iota^q)(\gamma(t)) = \frac{d}{dt}\Big|_{t=0} \varphi\big(\gamma(t), q\big).
> $$
>
> Equivalently, $\Theta(v, 0)$ is the velocity of the horizontal curve (Corollary [[§31 Tangent Vectors as Velocities of Curves#^cor-31-8|§31.8]]).
>
> *2. Coordinates.* “The $x$ and the $y$ together form a coordinate chart of $M \times N$” (Definition [[§19 Smooth Functions and Smooth Maps#^def-19-7|§19.7]]). By linearity of $\Theta$ and Corollary [[§31 Tangent Vectors as Velocities of Curves#^cor-31-7|§31.7]], $\Theta(v, 0) = \sum_j v^j\, \iota^q_\ast\big(\partial/\partial x^j|_p\big) = \sum_j v^j\, \partial/\partial x^j|_{(p,q)}$, and applying this to $\varphi$ gives the formula: “we're just differentiating in the $x$ variable.”
>
> *3. Smoothness.* “This coordinate description … makes it clear that whenever we do this construction, it's a smooth function on $N$.” *(Filled in.)* Fix charts $(U, \phi_U = (x^j))$ of $M$ at $p$ and $(V, \psi = (y^k))$ of $N$, and let $\hat\varphi(r, s) = \varphi\big(\phi_U^{-1}(r), \psi^{-1}(s)\big)$, a smooth function on $\phi_U(U) \times \psi(V)$, the coordinate representation of $\varphi$ in the product chart. By 2, for $q \in V$,
>
> $$
> \partial_v\varphi\big(\psi^{-1}(s)\big) = \sum_{j=1}^m v^j\, \frac{\partial\hat\varphi}{\partial r^j}\big(\phi_U(p), s\big), \qquad s \in \psi(V).
> $$
>
> Each $\partial\hat\varphi/\partial r^j$ is smooth, as a partial derivative of the smooth function $\hat\varphi$ — by Lemma [[§29 Coordinate Derivations and the Basis Theorem#^lem-29-1|§29.1]], applied to $\varphi$ in the product chart on $U \times V$, it is the coordinate representation of the smooth function $\partial\varphi/\partial x^j$ — and $s \mapsto (\phi_U(p), s)$ is smooth, so the right side is a smooth function of $s$: the coordinate representation of $\partial_v\varphi$ on $V$ is smooth. Charts $(V, \psi)$ cover $N$, so $\partial_v\varphi \in C^\infty(N)$. The second variable is the same with the factors exchanged.

^pf-31-9

*Uses:* [[§31 Tangent Vectors as Velocities of Curves#^def-31-2|Def. §31.2]], [[§31 Tangent Vectors as Velocities of Curves#^cor-31-8|§31.8]], [[§19 Smooth Functions and Smooth Maps#^def-19-7|Def. §19.7]], [[§31 Tangent Vectors as Velocities of Curves#^cor-31-7|§31.7]], [[§29 Coordinate Derivations and the Basis Theorem#^lem-29-1|§29.1]]

![[m591-31-2.svg]]

*The picture of the definition: one horizontal curve through $(p, q)$ for each $q$, all with the same velocity $v$ in the $M$ direction. Differentiating $\varphi$ along each gives one number per $q$, and Proposition [[§31 Tangent Vectors as Velocities of Curves#^prop-31-9|§31.9]](3) says these numbers vary smoothly with $q$.*

**Transcription note (Lecture 18).** Page 47 of the handwritten notes writes the splitting as “$T_{(p,q)}(M \times N) = T_pM \oplus T_qM$” (Uribe corrected it in lecture: “should be an $N$”); it is $T_pM \oplus T_qN$. The curves line has “$\forall\, q \in M$” for $q \in N$, and the coordinate formula sums to $n$ and evaluates at $q$; the sum runs to $m = \dim M$, and the partials are evaluated at $(p, q)$.
