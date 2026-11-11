---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 11
section: 74
tags: [differentiable-manifolds, math591]
---
← [[§73 Stokes' Theorem in Calculus III]] · ↑ [[· 11 Differential Forms]] · [[§75 Multilinear Algebra]] →

*Stage: forms — Reading the Calculus III surface integrand as a two-form: the $2 \times 2$ minors $dx^i \wedge dx^j$ fed the two tangent vectors; and the shape of the general Stokes theorem.*

*(Lecture 28.)* Back to manifolds, thinking geometrically: what kind of object is integrated in the surface integral of [[§73 Stokes' Theorem in Calculus III|§73]]? Expand the determinant of Lemma [[§73 Stokes' Theorem in Calculus III#^lem-73-3|§73.3]] along its top row:

$$
g^1\big(x^2_s x^3_t - x^2_t x^3_s\big) + g^2\big(x^3_s x^1_t - x^3_t x^1_s\big) + g^3\big(x^1_s x^2_t - x^1_t x^2_s\big) .
$$

*(The lecture wrote the first term; the other two are filled in.)* Each bracket is a $2 \times 2$ minor of the matrix with rows $\vec r_s, \vec r_t$: a scalar extracted from the two vectors $\vec r_s, \vec r_t$, linearly in each of them. A function that is fed two vectors and returns a scalar in this way is a two-form.

> [!definition] Definition §74.1: The Two-Forms $dx^i \wedge dx^j$ on $\mathbb{R}^3$
> For $i, j \in \{1, 2, 3\}$, define the bilinear map
>
> $$
> dx^i \wedge dx^j : \mathbb{R}^3 \times \mathbb{R}^3 \longrightarrow \mathbb{R}, \qquad (u, v) \longmapsto \det \begin{pmatrix} u^i & u^j \\ v^i & v^j \end{pmatrix} = u^i v^j - u^j v^i .
> $$
>
> *Lee: Ch. 14, The Wedge Product*

^def-74-1

> [!remark]- Connections
> - MATH 452 defines the wedge product of forms on $\mathbb{R}^n$ by its rules: [[§37 The Algebra of Differential Forms#^def-37-1|452 Def. §37.1]]. Its [[§36 Introduction to Differential Forms#^def-36-2|452 §36]] has the shadow picture of Lemma [[§74 The Integrand Is a Two-Form#^lem-74-1|§74.1]] with an animation of a turning parallelogram (in 452's notation).

*(Lecture 28, on the board for $(i, j) = (2, 3)$, named $dx^2 \wedge dx^3$ after the two indices involved; the other pairs are filled in the same way.)* The name is explained by the wedge product of covectors: $dx^i$ is the covector $u \mapsto u^i$ (Definition [[§21 Linear Algebra Toolkit#^def-21-1|§21.1]]), and $dx^i \wedge dx^j$ is the wedge product of $dx^i$ and $dx^j$ (Example [[§76 The Wedge Product#^ex-76-2|§76.2]]).

> [!theorem] Lemma §74.1: Properties of $dx^i \wedge dx^j$
> For $i, j \in \{1, 2, 3\}$ and $u, v \in \mathbb{R}^3$:
>
> 1. $dx^i \wedge dx^j$ is bilinear, and alternating: $(dx^i \wedge dx^j)(v, u) = -(dx^i \wedge dx^j)(u, v)$; in particular $(dx^i \wedge dx^j)(u, u) = 0$;
> 2. $dx^j \wedge dx^i = -\,dx^i \wedge dx^j$, and $dx^i \wedge dx^i = 0$;
> 3. the values of the three forms $dx^2 \wedge dx^3$, $dx^3 \wedge dx^1$, $dx^1 \wedge dx^2$ on $(u, v)$ are the three components of the cross product:
>
> $$
> u \times v = \big( (dx^2 \wedge dx^3)(u, v),\ (dx^3 \wedge dx^1)(u, v),\ (dx^1 \wedge dx^2)(u, v) \big) ;
> $$
>
> 4. $(dx^i \wedge dx^j)(u, v)$ is the signed area of the parallelogram spanned by the projections of $u$ and $v$ to the $(x^i, x^j)$-plane, positive when the projection of $u$ turns to the projection of $v$ counterclockwise as seen with the $x^i$-axis pointing right and the $x^j$-axis up.

^lem-74-1

> [!proof]+ Proof
> *(Not from lecture; filled in.)* All four are properties of $2 \times 2$ determinants.
>
> (1) For fixed $v$, $u \mapsto u^i v^j - u^j v^i$ is linear, since $u \mapsto u^i$ and $u \mapsto u^j$ are; likewise in $v$. Exchanging $u$ and $v$ gives $v^i u^j - v^j u^i = -(u^i v^j - u^j v^i)$. With $v = u$ this says $(dx^i \wedge dx^j)(u, u) = -(dx^i \wedge dx^j)(u, u)$, so it is $0$.
>
> (2) $(dx^j \wedge dx^i)(u, v) = u^j v^i - u^i v^j = -(u^i v^j - u^j v^i)$ for all $u, v$; and $(dx^i \wedge dx^i)(u, v) = u^i v^i - u^i v^i = 0$.
>
> (3) By definition of the cross product, $u \times v = (u^2 v^3 - u^3 v^2,\ u^3 v^1 - u^1 v^3,\ u^1 v^2 - u^2 v^1)$, and the three components are, by Definition [[§74 The Integrand Is a Two-Form#^def-74-1|§74.1]], the values of $dx^2 \wedge dx^3$, $dx^3 \wedge dx^1$ and $dx^1 \wedge dx^2$ on $(u, v)$.
>
> (4) The projection to the $(x^i, x^j)$-plane sends $u$ to the plane vector $(u^i, u^j)$ and $v$ to $(v^i, v^j)$. The determinant of two plane vectors $a, b$ is $|a|\,|b| \sin\phi$, with $\phi$ the counterclockwise angle from $a$ to $b$; this is the area of the parallelogram they span, with the sign of $\sin \phi$. Applied to $a = (u^i, u^j)$, $b = (v^i, v^j)$, it gives the claim.

^pf-74-1

*Uses:* [[§74 The Integrand Is a Two-Form#^def-74-1|Def. §74.1]]

![[m591-74-1.svg]]

*(Not from lecture; figure added.)* Lemma [[§74 The Integrand Is a Two-Form#^lem-74-1|§74.1]](3) and (4). A parallelogram spanned by $u, v \in \mathbb{R}^3$ (blue) and its shadows on the three coordinate planes: on the $(x^2, x^3)$-plane (green), the $(x^3, x^1)$-plane (orange) and the $(x^1, x^2)$-plane (red), with the shadows of $u$ and $v$ drawn as arrows. The signed areas of the shadows are the values of $dx^2 \wedge dx^3$, $dx^3 \wedge dx^1$, $dx^1 \wedge dx^2$ on $(u, v)$, and together they are $u \times v$. Here $u = (0.96, 0, -0.48)$ and $v = (-0.23, 0.96, -0.46)$, so $u \times v = (0.46, 0.55, 0.92)$: all three shadows are positively oriented. A shadow whose orientation is reversed gives a negative value, and a parallelogram seen edge-on from a coordinate axis has a shadow of area $0$ there.

> [!theorem] Proposition §74.2: The Surface Integrand Is a Two-Form
> Let $\vec r : D \to S$ be a positive parametrization of the oriented surface $S$ and $\vec G = (g^1, g^2, g^3)$ a continuous field on $S$. Put
>
> $$
> \omega_{\vec G} = g^1\, dx^2 \wedge dx^3 + g^2\, dx^3 \wedge dx^1 + g^3\, dx^1 \wedge dx^2 ,
> $$
>
> a two-form with variable coefficients: at each point $q \in S$ the bilinear map $(u, v) \mapsto g^1(q)\, (dx^2 \wedge dx^3)(u, v) + g^2(q)\, (dx^3 \wedge dx^1)(u, v) + g^3(q)\, (dx^1 \wedge dx^2)(u, v)$. Then at every point of $D$, with the coefficients evaluated at $\vec r(s, t)$,
>
> $$
> \vec G \cdot (\vec r_s \times \vec r_t) = \omega_{\vec G}(\vec r_s, \vec r_t), \qquad \text{so} \qquad \iint_S \vec G \cdot d\vec S = \iint_D \omega_{\vec G}(\vec r_s, \vec r_t)\, ds\, dt .
> $$

^prop-74-2

> [!remark]- Connections
> - The same computation in MATH 452's notation: [[§37 The Algebra of Differential Forms#^ex-37-3|452 Ex. §37.3]], and [[§37 The Algebra of Differential Forms#^rem-37-3|452 Remark: The Cross Product Is the Pullback in Disguise]].

> [!proof]+ Proof
> *(Lecture 28: “$\vec G \cdot d\vec S = (g^1\, dx^2 \wedge dx^3 + \cdots)(\vec r_s, \vec r_t)\, ds\, dt$”; the details are filled in.)* By Lemma [[§74 The Integrand Is a Two-Form#^lem-74-1|§74.1]](3) with $u = \vec r_s$, $v = \vec r_t$, the components of $\vec r_s \times \vec r_t$ are $(dx^2 \wedge dx^3)(\vec r_s, \vec r_t)$, $(dx^3 \wedge dx^1)(\vec r_s, \vec r_t)$ and $(dx^1 \wedge dx^2)(\vec r_s, \vec r_t)$. So
>
> $$
> \vec G \cdot (\vec r_s \times \vec r_t) = g^1 (dx^2 \wedge dx^3)(\vec r_s, \vec r_t) + g^2 (dx^3 \wedge dx^1)(\vec r_s, \vec r_t) + g^3 (dx^1 \wedge dx^2)(\vec r_s, \vec r_t) = \omega_{\vec G}(\vec r_s, \vec r_t) .
> $$
>
> By Lemma [[§73 Stokes' Theorem in Calculus III#^lem-73-3|§73.3]], $\iint_S \vec G \cdot d\vec S$ is the integral over $D$ of $\vec G \cdot (\vec r_s \times \vec r_t)$, hence of $\omega_{\vec G}(\vec r_s, \vec r_t)$.

^pf-74-2

*Uses:* [[§74 The Integrand Is a Two-Form#^lem-74-1|§74.1]], [[§73 Stokes' Theorem in Calculus III#^lem-73-3|§73.3]]

So the thing integrated in a surface integral is a two-form: at every point, evaluate the coefficients $g^i$ to get scalars and combine the three basic forms; then feed it the two tangent vectors $\vec r_s, \vec r_t$, and integrate the result over $D$. In Calculus III one does exactly this in Stokes' theorem without saying so. By Lemma [[§74 The Integrand Is a Two-Form#^lem-74-1|§74.1]](4), $\omega_{\vec G}(\vec r_s, \vec r_t)\, ds\, dt$ weighs the shadows of the small parallelogram on the three coordinate planes by the components of $\vec G$.

*Where this is going: the general Stokes theorem.* *(In the lecture this came right after Stokes' theorem in $\mathbb{R}^3$.)* The theorem of this chapter will read

$$
\int_{\partial S} \alpha = \int_S d\alpha .
$$

Here $S$ is an oriented manifold with boundary of dimension $m$, its boundary $\partial S$ has dimension $m - 1$, $\alpha$ is a *differential form* of degree $m - 1$, and $d\alpha$, the *exterior derivative* of $\alpha$, has degree $m$: to integrate a form over a manifold, the degree of the form has to match the dimension of the manifold. Matching the ingredients with Theorem [[§73 Stokes' Theorem in Calculus III#^thm-73-2|§73.2]] ($m = 2$):
- the field $\mathbf{X}$ on the left becomes a one-form, a section of the cotangent bundle (Definition [[§53 One-Forms#^def-53-1|§53.1]]), the kind of form already known;
- the integrand on the right becomes a two-form, as in Proposition [[§74 The Integrand Is a Two-Form#^prop-74-2|§74.2]];
- $\mathbf{X} \mapsto \nabla \times \mathbf{X}$ is an instance of $d$.

Green's theorem, the divergence theorem, the fundamental theorem of calculus for line integrals, and also Cauchy's theorem in complex analysis are instances of the same formula. For Cauchy's theorem, $d\alpha$ is zero. *(Filled in: with $\alpha = f\, dz$ for holomorphic $f$, $d\alpha = \frac{\partial f}{\partial \bar z}\, d\bar z \wedge dz = 0$.)*

> [!remark]- Connections
> - Green's theorem: [[§27 Line Integrals and Green's Theorem#^thm-27-1|452 Thm. §27.1]], and as the planar case of Stokes' theorem [[§27 Line Integrals and Green's Theorem#^thm-27-3|452 Thm. §27.3]]; Calculus III: [[§130 Green's Theorem#^thm-130-1|Calc Thm. §130.1]].
> - The divergence theorem: [[§32 Flux Integrals and the Divergence Theorem in ℝ³#^thm-32-1|452 Thm. §32.1]]; Calculus III: [[§137 The Divergence Theorem#^thm-137-1|Calc Thm. §137.1]].
> - Cauchy's theorem: [[§51 Proof of the Theorem (Cauchy–Goursat Theorem)#^thm-51-3|Complex Variables Thm. §51.3]].
