---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 6
section: 42
tags: [differentiable-manifolds, math591]
---
← [[§41 SU(2) → SO(3)꞉ The Double Cover]] · ↑ [[· 6 Bundles and Vector Fields]] · [[§43 Recap꞉ Covectors and the Four Differentials]] →

*Stage: recap — Chapter 4's road from arrows to derivations, retraced in one place before tangent vectors are gathered into bundles and fields.*

*Not from lecture: a recap written for these notes at the start of the chapter on bundles and vector fields. Nothing here is new. Every object is defined, and every fact proved, where the cross-reference points; this section puts them in order and says why each step was taken.*

**The problem.** On a surface in $\mathbb{R}^3$ a tangent vector is an arrow: the velocity of a curve that stays on the surface ([[§25 The Geometric Tangent Space#^def-25-1|Definition §25.1]]). An abstract manifold, built from charts or as a quotient, sits in no ambient space, so there is nowhere for an arrow to live. The course solved this by keeping not the arrow but *what the arrow does to functions*. Six steps lead from one to the other.

![[§25 The Geometric Tangent Space#^def-25-1]]

**Step 1: an arrow differentiates functions.** For a geometric tangent vector $v$ at $p$ and a function $f$ near $p$, the number

$$
D_v(f) = \frac{d}{dt}\Big|_{t=0} f(\gamma(t))
$$

is the rate of change of $f$ along a curve $\gamma$ through $p$ with velocity $v$ ([[§25 The Geometric Tangent Space#^def-25-4|Definition §25.4]]). The map $f \mapsto D_v(f)$ is linear and obeys the product rule ([[§25 The Geometric Tangent Space#^prop-25-8|Proposition §25.8]]), and it determines $v$ ([[§25 The Geometric Tangent Space#^prop-25-9|Proposition §25.9]]). So nothing is lost by remembering only how $v$ acts on functions.

![[§25 The Geometric Tangent Space#^def-25-4]]

**Step 2: only the behaviour near $p$ matters, so use germs.** $D_v(f)$ depends on $f$ only on a neighbourhood of $p$, however small. Two functions defined near $p$ *agree near $p$* if they coincide on some open set around $p$ ([[§27 Germs#^def-27-1|Definition §27.1]]); a *germ* at $p$ is an equivalence class $[f]$ of this relation, and $C^\infty_p(M)$ is the set of germs ([[§27 Germs#^def-27-2|Definition §27.2]]). A germ remembers $f$ near $p$ without committing to a particular neighbourhood — no single neighbourhood serves every representative ([[§27 Germs#^ex-27-1|Example §27.1]]). Germs can be added and multiplied, and evaluated at $p$: $[f](p) = f(p)$ ([[§27 Germs#^prop-27-2|Proposition §27.2]]). The germs vanishing at $p$ form the ideal $I_p$ ([[§28 Derivations and the Abstract Tangent Space#^def-28-3|Definition §28.3]]), which returns in the cotangent space.

![[§27 Germs#^def-27-1]]

![[§27 Germs#^def-27-2]]

![[§28 Derivations and the Abstract Tangent Space#^def-28-3]]

![[§28 Derivations and the Abstract Tangent Space#^def-28-4]]

**Step 3: a tangent vector is a derivation.** The two properties of $D_v$ become the definition. A *derivation at $p$* is a linear map $D : C^\infty_p(M) \to \mathbb{R}$ with the Leibniz rule $D([f][g]) = f(p)\,D[g] + g(p)\,D[f]$ ([[§28 Derivations and the Abstract Tangent Space#^def-28-1|Definition §28.1]]), and the *tangent space* $T_pM$ is the vector space of all derivations at $p$ ([[§28 Derivations and the Abstract Tangent Space#^def-28-2|Definition §28.2]]). A tangent vector is therefore a machine: feed it a germ at $p$, and it returns a number. Lee lets derivations act on global functions $C^\infty(M)$ instead of germs; the two spaces are canonically isomorphic ([[§28 Derivations and the Abstract Tangent Space#^prop-28-3|Proposition §28.3]]).

![[§28 Derivations and the Abstract Tangent Space#^def-28-1]]

![[§28 Derivations and the Abstract Tangent Space#^def-28-2]]

**Step 4: coordinates give a basis.** In a chart $(U, \varphi = (x^1, \ldots, x^m))$, the *coordinate derivation* $\partial/\partial x^i|_p$ takes the $i$-th partial derivative of the coordinate representation $f \circ \varphi^{-1}$ at $\varphi(p)$ ([[§29 Coordinate Derivations and the Basis Theorem#^def-29-2|Definition §29.2]]). The Basis Theorem says these $m$ derivations form a basis of $T_pM$, and the *universal formula* gives the components of any $D$: they are the values of $D$ on the coordinate functions,

$$
D = \sum_{i=1}^m D[x^i]\, \frac{\partial}{\partial x^i}\Big|_p
$$

([[§29 Coordinate Derivations and the Basis Theorem#^thm-29-5|Theorem §29.5]]). So $\dim T_pM = m$, and for a level set in $\mathbb{R}^N$ the derivations are exactly the old arrows: $v \mapsto D_v$ is an isomorphism ([[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|Theorem §29.6]]).

![[§29 Coordinate Derivations and the Basis Theorem#^def-29-2]]

![[§29 Coordinate Derivations and the Basis Theorem#^thm-29-5]]

**Step 5: maps push vectors forward.** Let $F : M \to N$ be smooth. Germs travel *backwards* along $F$: a germ $[g]$ at $F(p)$ pulls back to the germ $F_p^{\ast}[g] = [g \circ F]$ at $p$ ([[§28 Derivations and the Abstract Tangent Space#^def-28-5|Definition §28.5]]). Tangent vectors then travel *forwards*: the *pushforward*, or *differential*, of $F$ at $p$ is

$$
F_{*p} : T_pM \to T_{F(p)}N, \qquad (F_{*p}D)[g] = D\big(F_p^*[g]\big) = D[g \circ F]
$$

([[§28 Derivations and the Abstract Tangent Space#^def-28-6|Definition §28.6]]) — to see how $F_{\ast p}D$ differentiates $g$, pull $g$ back and let $D$ differentiate it. The chain rule is $(G \circ F)_{\ast p} = G_{\ast F(p)} \circ F_{\ast p}$ ([[§28 Derivations and the Abstract Tangent Space#^thm-28-6|Theorem §28.6]]). In charts the matrix of $F_{\ast p}$ is the Jacobian of the coordinate representation ([[§30 The Differential in Coordinates#^thm-30-2|Theorem §30.2]], with [[§30 The Differential in Coordinates#^prop-30-1|Proposition §30.1]]), and on open subsets of Euclidean space $F_{\ast p}$ *is* the ordinary derivative, the differential $dF_p$ of [[§22 The Differential of a Map Between Vector Spaces#^def-22-5|Definition §22.5]] ([[§30 The Differential in Coordinates#^prop-30-5|Proposition §30.5]]).

![[§28 Derivations and the Abstract Tangent Space#^def-28-5]]

![[§28 Derivations and the Abstract Tangent Space#^def-28-6]]

![[§22 The Differential of a Map Between Vector Spaces#^def-22-5]]

**Step 6: back to arrows, through curves.** A smooth curve $\gamma$ with $\gamma(0) = p$ has the velocity $D_\gamma = \gamma_{\ast 0}(d/dt|_0)$, which differentiates $f$ by $D_\gamma[f] = (f \circ \gamma)'(0)$ ([[§31 Tangent Vectors as Velocities of Curves#^def-31-2|Definition §31.2]]), and every tangent vector is the velocity of some curve ([[§31 Tangent Vectors as Velocities of Curves#^thm-31-2|Theorem §31.2]]). So the arrow picture survives on every manifold, as “the velocity of a curve”, even where there is no ambient space to draw the arrow in.

![[§31 Tangent Vectors as Velocities of Curves#^def-31-1]]

![[§31 Tangent Vectors as Velocities of Curves#^def-31-2]]

| Object | What it is | What it does |
|---|---|---|
| germ $[f]$ at $p$ | $f$ near $p$, neighbourhood forgotten | has a value $f(p)$; can be differentiated |
| tangent vector $D \in T_pM$ | a derivation at $p$ | eats a germ at $p$, returns $D[f] \in \mathbb{R}$ |
| $\partial/\partial x^i\vert_p$ | a coordinate derivation | returns the $i$-th partial in the chart |
| $F_p^{\ast}$ | pullback of germs | germ at $F(p)$ $\mapsto$ germ at $p$ |
| $F_{\ast p}$ | pushforward (differential) of $F$ | vector at $p$ $\mapsto$ vector at $F(p)$ |
| $D_\gamma$ | velocity of a curve | the arrow picture, on any manifold |

> [!example] Example §42.1: Vectors in the Plane in Three Ways
> On $M = \mathbb{R}^2$ with coordinates $(x, y)$, let $p = (1, 2)$, $f(x, y) = x^2 y$, and
>
> $$
> v = 3\,\frac{\partial}{\partial x}\Big|_p - \frac{\partial}{\partial y}\Big|_p \in T_pM .
> $$
>
> 1. *As a derivation.* $v[f] = 3\, \partial_x f(p) - \partial_y f(p) = 3 \cdot 2xy\big|_p - x^2\big|_p = 3 \cdot 4 - 1 = 11$.
> 2. *As a velocity.* The curve $\gamma(t) = (1 + 3t,\ 2 - t)$ has $\gamma(0) = p$ and velocity $v$, since $D_\gamma[x] = 3$ and $D_\gamma[y] = -1$ (universal formula). Indeed $f(\gamma(t)) = (1 + 3t)^2 (2 - t)$, whose derivative at $t = 0$ is $2 \cdot 3 \cdot 2 - 1 = 11$.
> 3. *Pushed forward.* Let $F : \mathbb{R}^2 \to \mathbb{R}^2$, $F(x, y) = (x^2,\ x + y)$, with coordinates $(u, w)$ on the target, so $F(p) = (1, 3)$. The Jacobian at $p$ is $\begin{pmatrix} 2x & 0 \\ 1 & 1 \end{pmatrix}_p = \begin{pmatrix} 2 & 0 \\ 1 & 1 \end{pmatrix}$, so
>
>    $$
>    F_{*p} v = (2 \cdot 3 + 0)\, \frac{\partial}{\partial u}\Big|_{F(p)} + (3 - 1)\, \frac{\partial}{\partial w}\Big|_{F(p)} = 6\, \frac{\partial}{\partial u} + 2\, \frac{\partial}{\partial w} .
>    $$
>
>    By the definition instead: $(F_{\ast p}v)[u] = v[u \circ F] = v[x^2] = 3 \cdot 2 = 6$ and $(F_{\ast p}v)[w] = v[x + y] = 3 - 1 = 2$, the same components by the universal formula.
>
> The example continues with covectors in [[§43 Recap꞉ Covectors and the Four Differentials#^ex-43-1|Example §43.1]].

^ex-42-1

*Uses:* [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-5|§29.5]], [[§31 Tangent Vectors as Velocities of Curves#^def-31-1|Def. §31.1]], [[§31 Tangent Vectors as Velocities of Curves#^def-31-2|Def. §31.2]], [[§30 The Differential in Coordinates#^thm-30-2|§30.2]], [[§28 Derivations and the Abstract Tangent Space#^def-28-6|Def. §28.6]]
