---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 11
section: 73
tags: [differentiable-manifolds, math591]
---
← · ↑ · →

*Stage: forms — The theorem to be generalized, recalled from Calculus III: parametrized surfaces, orientation by a unit normal, surface integrals, the induced orientation of the boundary, and Stokes' theorem in $\mathbb{R}^3$.*

*(Lecture 28.)* The course reviews Stokes' theorem of Calculus III because it is the theorem to be generalized. The definitions of this section are recalled from Calculus III (Stewart, Sections 16.6–16.8, in MATH 233) and from MATH 452 (§§31–34), where the theorem is proved. They are restated in the notation of the lecture, which differs from both:

\begin{center}
\small
\begin{tabular}{llll}
\toprule
& these notes & Calculus III (Stewart) & MATH 452 \ \midrule
vector field & $\mathbf{X} = (f^1, f^2, f^3)$, $\vec G = (g^1, g^2, g^3)$ & $\mathbf{F} = P\,\mathbf{i} + Q\,\mathbf{j} + R\,\mathbf{k}$ & $\mathbf{F} = (P, Q, R)$ \\
coordinates on $\mathbb{R}^3$ & $x^1, x^2, x^3$ & $x, y, z$ & $x, y, z$ \\
parametrization & $\vec r(s, t)$, $(s, t) \in D$ & $\mathbf{r}(u, v)$ & $\mathbf{X}(u, v)$ \\
tangent vectors & $\vec r_s$, $\vec r_t$ & $\mathbf{r}_u$, $\mathbf{r}_v$ & $\mathbf{X}_u$, $\mathbf{X}_v$ \\
unit normal & $\mathbf{n}$ & $\mathbf{n}$ & $\hat n$ \\
\bottomrule
\end{tabular}
\end{center}
In these notes a bold $\mathbf{X}$ is always a vector field; in MATH 452 the same letter is the parametrization of the surface.

> [!definition] Definition §73.1: Parametrized Surface
> Let $D \subseteq \mathbb{R}^2$ be a compact region of the $(s, t)$-plane bounded by a piecewise smooth closed curve, and let $\vec r : D \to \mathbb{R}^3$ be the restriction of a smooth map defined on an open set containing $D$,
>
> $$
> \vec r(s, t) = \big( x^1(s, t), x^2(s, t), x^3(s, t) \big) .
> $$
>
> The image $S = \vec r(D)$ is a **parametrized surface**, and $\vec r$ is a **parametrization** of $S$.

^def-73-1

*(Recalled from Calculus III: Stewart, Section 16.6; MATH 452, §31.)* The partial derivatives

$$
\vec r_s = \frac{\partial \vec r}{\partial s} = (x^1_s, x^2_s, x^3_s), \qquad \vec r_t = \frac{\partial \vec r}{\partial t} = (x^1_t, x^2_t, x^3_t)
$$

are two fields of vectors along $S$, tangent to $S$: $\vec r_s$ is the velocity of the curve $s \mapsto \vec r(s, t)$ with $t$ fixed, $\vec r_t$ that of $t \mapsto \vec r(s, t)$. The standard grid of $D$ goes to a mesh of these curves on $S$ (figure below).

> [!definition] Definition §73.2: Regular Parametrization
> A parametrization $\vec r : D \to \mathbb{R}^3$ (Definition [[§73 Stokes' Theorem in Calculus III#^def-73-1|§73.1]]) is **regular** if $\vec r_s \times \vec r_t \neq 0$ at every point of $D$, that is, if $\vec r_s$ and $\vec r_t$ are linearly independent everywhere.

^def-73-2

*(Recalled from Calculus III: Stewart, Section 16.6, a smooth surface; MATH 452, §31.)* Regular means that the Jacobian $d\vec r$, the $3 \times 2$ matrix with columns $\vec r_s, \vec r_t$, has rank $2$: on the interior of $D$, $\vec r$ is an immersion (Definition [[§36 Submersions#^def-36-2|§36.2]]). “In 95\% of the examples in Calc III,” a single injective regular parametrization covers $S$; when $\vec r$ restricted to the interior of $D$ is moreover a homeomorphism onto its image, it is an embedding (Definition [[§44 Embeddings#^def-44-1|§44.1]]), its image is a regular submanifold of $\mathbb{R}^3$ (Theorem [[§44 Embeddings#^thm-44-1|§44.1]]), and the inverse of $\vec r$ is a chart of that submanifold.

> [!definition] Definition §73.3: Orientation of a Surface by a Unit Normal
> Let $S \subseteq \mathbb{R}^3$ be a $2$-dimensional regular submanifold (Definition [[§37 Regular Submanifolds#^def-37-2|§37.2]]). A **unit normal field** on $S$ is a continuous map $\mathbf{n} : S \to \mathbb{R}^3$ such that for every $q \in S$, $\mathbf{n}(q)$ is a unit vector perpendicular to the tangent plane $T_qS \subseteq \mathbb{R}^3$. A choice of unit normal field is an **orientation** of $S$, and $S$ with this choice is an **oriented surface**.

^def-73-3

*(Recalled from Calculus III: Stewart, Section 16.7; MATH 452, §32.)* At each point there are two unit normals, $\mathbf{n}(q)$ and $-\mathbf{n}(q)$; the orientation is a continuous choice of one of them. The continuity is part of the definition (a student's question in Lecture 28): “it's supposed to vary” continuously. If $\mathbf{n}$ is an orientation, so is $-\mathbf{n}$.

> [!definition] Definition §73.4: Positive Parametrization
> Let $S$ be oriented by $\mathbf{n}$ (Definition [[§73 Stokes' Theorem in Calculus III#^def-73-3|§73.3]]). A regular parametrization $\vec r : D \to S$ (Definition [[§73 Stokes' Theorem in Calculus III#^def-73-2|§73.2]]) is **positive** if the normal $\vec r_s \times \vec r_t$ points in the direction of $\mathbf{n}$:
>
> $$
> \vec r_s \times \vec r_t = |\vec r_s \times \vec r_t|\; \mathbf{n}\big(\vec r(s, t)\big) \qquad \text{for all } (s, t) \in D .
> $$

^def-73-4

*(Lecture 28; Stewart, Section 16.7, calls $\mathbf{n} = \vec r_s \times \vec r_t / |\vec r_s \times \vec r_t|$ the orientation that a parametrization “supplies”.)* Exchanging $s$ and $t$ turns a positive parametrization into a negative one, since $\vec r_t \times \vec r_s = -\vec r_s \times \vec r_t$. The inverse of a positive parametrization will be a positively oriented chart, once orientations of manifolds are defined.

![[m591-73-2.svg]]

*(Figure after the board, redrawn from a computed surface.)* A positive parametrization. Left: the parameter domain $D$ with its grid, the lines $t = \text{const}$ (orange) and $s = \text{const}$ (blue), and the unit vectors $e_s, e_t$ at a point $(s_0, t_0)$. Right: the image $S = \vec r(D)$; the grid goes to the mesh of the two families of curves on $S$, and $e_s, e_t$ go to the tangent vectors $\vec r_s, \vec r_t$ at $\vec r(s_0, t_0)$, the velocities of the orange and the blue curve through that point. The normal $\vec r_s \times \vec r_t$ (red) points to the side from which the mesh is seen here; orienting $S$ by that side makes $\vec r$ positive (Definition [[§73 Stokes' Theorem in Calculus III#^def-73-4|§73.4]]). The surface drawn is $\vec r(s, t) = \big(1.7s + 0.3,\ 1.5t + 0.3,\ 0.75 + 0.25 \sin 2.4s - 0.3t^2 + 0.1st\big)$ on $D = [0, 1]^2$.

> [!definition] Definition §73.5: Surface Integral of a Vector Field
> Let $S$ be oriented by $\mathbf{n}$, let $\vec r : D \to S$ be a positive parametrization (Definition [[§73 Stokes' Theorem in Calculus III#^def-73-4|§73.4]]) that is injective on the interior of $D$, and let $\vec G = (g^1, g^2, g^3)$ be a continuous vector field on $S$. The **surface integral** (or **flux**) of $\vec G$ through $S$ is
>
> $$
> \iint_S \vec G \cdot d\vec S = \iint_S (\vec G \cdot \mathbf{n})\, dS = \iint_D \vec G\big(\vec r(s, t)\big) \cdot \mathbf{n}\big(\vec r(s, t)\big)\, |\vec r_s \times \vec r_t|\; ds\, dt ,
> $$
>
> where $dS = |\vec r_s \times \vec r_t|\, ds\, dt$ is the element of surface area and $d\vec S = \mathbf{n}\, dS$.
>
> *Lee: Ch. 16, Surface Integrals*

^def-73-5

*(Recalled from Calculus III: Stewart, Section 16.7; MATH 452, Definition 32.1.)* The factor $|\vec r_s \times \vec r_t|\, ds\, dt$ is the area of the parallelogram spanned by $\vec r_s\, ds$ and $\vec r_t\, dt$, the image of a small rectangle of $D$ to first order. That the integral does not depend on the positive parametrization is the change of variables formula (MATH 452, §§24 and 32); for integrals of forms it will be proved in this course.

> [!definition] Definition §73.6: Induced Orientation of the Boundary Curve
> Let $S$ be a compact oriented surface with boundary in $\mathbb{R}^3$, oriented by $\mathbf{n}$, whose boundary $\partial S$ is a piecewise smooth closed curve (or a finite union of such curves). The **induced orientation** of $\partial S$ is the direction of travel along $\partial S$ in which a walker with $\mathbf{n}$ pointing from his feet to his head has the surface on his left. With this orientation, $\partial S$ is **positively oriented**.

^def-73-6

*(Lecture 28: the right-hand rule, or “Amp\`ere's little guy”; Stewart, Section 16.8; MATH 452, Theorem 34.1.)* Surfaces with boundary are taken here in the sense of Calculus III; manifolds with boundary come later in the chapter. The walker can be traded for a formula of the kind that will generalize: put the outward direction first.

> [!theorem] Lemma §73.1: The Induced Orientation Puts the Outward Direction First
> In the setting of Definition [[§73 Stokes' Theorem in Calculus III#^def-73-6|§73.6]], let $q \in \partial S$ be a point where $\partial S$ is smooth, let $T$ be the unit tangent vector of $\partial S$ at $q$ in the direction of travel, and let $\nu$ be the unit vector tangent to $S$ at $q$, perpendicular to $T$ and pointing out of $S$. Then $\partial S$ is positively oriented at $q$ if and only if
>
> $$
> \nu \times T = \mathbf{n}(q) .
> $$

^lem-73-1

> [!proof]+ Proof
> *(Filled in.)* The vectors $\nu, T$ are orthonormal and span $T_qS$, and $\mathbf{n} = \mathbf{n}(q)$ is a unit vector perpendicular to both. So $\nu \times T$, a unit vector perpendicular to $\nu$ and $T$, is $\pm\mathbf{n}$; we show that it is $+\mathbf{n}$ exactly when the surface is on the walker's left.
>
> *The walker's left.* A walker facing the unit vector $T$ with his head along the unit vector $\mathbf{n} \perp T$ has his left along $\mathbf{n} \times T$: for $T = e_1$ and $\mathbf{n} = e_3$ his left is $e_2 = e_3 \times e_1$, and every such pair $(T, \mathbf{n})$ is carried to $(e_1, e_3)$ by a rotation, which preserves cross products. The surface lies on his left exactly when the inward vector $-\nu$ is his left, $\mathbf{n} \times T = -\nu$.
>
> *The two conditions agree.* If $\nu \times T = \mathbf{n}$, then $(\nu, T, \mathbf{n})$ is a positively oriented orthonormal basis, so its cross products are cyclic: $T \times \mathbf{n} = \nu$, and $\mathbf{n} \times T = -T \times \mathbf{n} = -\nu$. If instead $\nu \times T = -\mathbf{n}$, the same argument with $-\mathbf{n}$ in place of $\mathbf{n}$ gives $(-\mathbf{n}) \times T = -\nu$, so $\mathbf{n} \times T = \nu \neq -\nu$. Hence the surface is on the walker's left if and only if $\nu \times T = \mathbf{n}$.

^pf-73-1

For a region of the $(x^1, x^2)$-plane oriented by $\mathbf{n} = e_3$, the lemma says that the boundary is traversed counterclockwise: on the right edge of a disk, $\nu = e_1$ and $T = e_2$, and $e_1 \times e_2 = e_3$. This is the orientation of Green's theorem.

> [!theorem] Theorem §73.2: Stokes' Theorem in $\mathbb{R}^3$
> Let $S \subseteq \mathbb{R}^3$ be a compact oriented surface with boundary, oriented by $\mathbf{n}$ (Definition [[§73 Stokes' Theorem in Calculus III#^def-73-3|§73.3]]), with $\partial S$ carrying the induced orientation (Definition [[§73 Stokes' Theorem in Calculus III#^def-73-6|§73.6]]), and let $\mathbf{X} = (f^1, f^2, f^3)$ be a smooth vector field on a neighbourhood of $S$. Then
>
> $$
> \oint_{\partial S} \mathbf{X} \cdot d\vec r = \iint_S (\nabla \times \mathbf{X}) \cdot d\vec S ,
> $$
>
> where the right-hand side is the surface integral of Definition [[§73 Stokes' Theorem in Calculus III#^def-73-5|§73.5]], $d\vec S = \mathbf{n}\, dS$.
>
> *Lee: Theorem 16.34*

^thm-73-2

> [!proof]+ Proof (not given in this course)
> The theorem is proved in MATH 452 (Theorem 34.1: first for graphs, then for parametrized surfaces, by pulling both sides back to the parameter domain and applying Green's theorem there); Stewart (Section 16.8) proves the case of a graph. In this course it will be a special case of the general Stokes theorem, which is how Lee deduces it (Theorem 16.34).

^pf-73-2

The ingredients, all to be generalized:
- a *surface with boundary*: manifolds with boundary will be needed;
- an *orientation*: in Calculus III a unit normal field $\mathbf{n}$ (Definition [[§73 Stokes' Theorem in Calculus III#^def-73-3|§73.3]]);
- the *induced orientation* on $\partial S$, by the right-hand rule (Definition [[§73 Stokes' Theorem in Calculus III#^def-73-6|§73.6]], Lemma [[§73 Stokes' Theorem in Calculus III#^lem-73-1|§73.1]]);
- the *integrals* on the two sides: a line integral of $\mathbf{X}$ and a surface integral of $\nabla \times \mathbf{X}$ (Definition [[§73 Stokes' Theorem in Calculus III#^def-73-5|§73.5]]);
- the operation $\mathbf{X} \mapsto \nabla \times \mathbf{X}$.

All of them have to be understood and generalized to manifolds.

![[m591-73-1.svg]]

*(Figure after the board, redrawn from a computed surface.)* The cap $x^3 = 0.4\,\big(1 - (x^1)^2 - (x^2)^2\big)$ over the unit disk, oriented by the upward unit normal $\mathbf{n}$ (orange, drawn at a few points). Its boundary $\partial S$ is the unit circle in the $(x^1, x^2)$-plane, with the induced orientation (red): counterclockwise seen from above, dashed where the cap hides it. “Amp\`ere's little guy” stands on $\partial S$ with $\mathbf{n}$ from his feet to his head; at the rim the normal leans outward, so he leans too. Walking in the direction of $\partial S$ he has the surface on his left (Definition [[§73 Stokes' Theorem in Calculus III#^def-73-6|§73.6]]); at his position the outward direction $\nu$ points towards the viewer and $T$ to the right, and $\nu \times T = \mathbf{n}$ (Lemma [[§73 Stokes' Theorem in Calculus III#^lem-73-1|§73.1]]).

*The surface integral, computed.* The right-hand side of Stokes' theorem is the surface integral of a field, $\nabla \times \mathbf{X}$. For any field $\vec G = (g^1, g^2, g^3)$, how is $\iint_S \vec G \cdot d\vec S$ computed? Parametrize $S$ positively; then the integrand is a $3 \times 3$ determinant, the “magic formula” of the lecture.

> [!theorem] Lemma §73.3: The Surface Integrand as a Determinant
> Let $\vec r : D \to S$ be a positive parametrization of the surface $S$ oriented by $\mathbf{n}$ (Definition [[§73 Stokes' Theorem in Calculus III#^def-73-4|§73.4]]), and $\vec G = (g^1, g^2, g^3)$ a continuous field on $S$. At every point of $D$, with $\vec G$ evaluated at $\vec r(s, t)$,
>
> $$
> \det \begin{pmatrix} g^1 & g^2 & g^3 \\ x^1_s & x^2_s & x^3_s \\ x^1_t & x^2_t & x^3_t \end{pmatrix} = \vec G \cdot (\vec r_s \times \vec r_t) = (\vec G \cdot \mathbf{n})\, |\vec r_s \times \vec r_t| .
> $$
>
> Consequently
>
> $$
> \iint_S \vec G \cdot d\vec S = \iint_D \det \begin{pmatrix} g^1 & g^2 & g^3 \\ x^1_s & x^2_s & x^3_s \\ x^1_t & x^2_t & x^3_t \end{pmatrix} ds\, dt .
> $$

^lem-73-3

> [!proof]+ Proof
> *(Lecture 28 states the formula, “$\vec G \cdot d\vec S = \det(\ldots)\, ds\, dt = (\vec G \cdot \mathbf{n})\, dS$”; the proof is filled in.)* *The first equality.* Expand the determinant along the first row:
>
> $$
> \det(\ldots) = g^1 \big(x^2_s x^3_t - x^3_s x^2_t\big) - g^2 \big(x^1_s x^3_t - x^3_s x^1_t\big) + g^3 \big(x^1_s x^2_t - x^2_s x^1_t\big) .
> $$
>
> The three brackets, with the sign of the middle one moved inside, are the components of the cross product,
>
> $$
> \vec r_s \times \vec r_t = \big( x^2_s x^3_t - x^3_s x^2_t,\ \ x^3_s x^1_t - x^1_s x^3_t,\ \ x^1_s x^2_t - x^2_s x^1_t \big) ,
> $$
>
> so the determinant is $g^1 (\vec r_s \times \vec r_t)^1 + g^2 (\vec r_s \times \vec r_t)^2 + g^3 (\vec r_s \times \vec r_t)^3 = \vec G \cdot (\vec r_s \times \vec r_t)$, the triple product.
>
> *The second equality.* Since $\vec r$ is positive, $\vec r_s \times \vec r_t = |\vec r_s \times \vec r_t|\, \mathbf{n}$ (Definition [[§73 Stokes' Theorem in Calculus III#^def-73-4|§73.4]]); taking the dot product with $\vec G$ gives $\vec G \cdot (\vec r_s \times \vec r_t) = (\vec G \cdot \mathbf{n})\, |\vec r_s \times \vec r_t|$.
>
> *The integral.* By Definition [[§73 Stokes' Theorem in Calculus III#^def-73-5|§73.5]], $\iint_S \vec G \cdot d\vec S$ is the integral over $D$ of $(\vec G \cdot \mathbf{n})\, |\vec r_s \times \vec r_t|$, which by the two equalities is the integral of the determinant.

^pf-73-3

*Uses:* [[§73 Stokes' Theorem in Calculus III#^def-73-4|Def. §73.4]], [[§73 Stokes' Theorem in Calculus III#^def-73-5|Def. §73.5]]

![[m591-73-3.svg]]

*(Not from lecture; figure added.)* Lemma [[§73 Stokes' Theorem in Calculus III#^lem-73-3|§73.3]] in one picture. A small rectangle $\Delta s \times \Delta t$ of $D$ goes, to first order, to the parallelogram spanned by $\vec r_s\, \Delta s$ and $\vec r_t\, \Delta t$ (blue), of area $|\vec r_s \times \vec r_t|\, \Delta s\, \Delta t$. The field $\vec G$ (orange) sweeps it out into a slanted box, whose volume is the absolute value of the determinant with rows $\vec G$, $\vec r_s\, \Delta s$, $\vec r_t\, \Delta t$. The volume is also base times height, and the height is the component $\vec G \cdot \mathbf{n}$ of $\vec G$ along the unit normal (red, dashed from the centre of the top face down to the plane of the base). If $\vec G$ is the velocity of a fluid, the box is the fluid crossing the patch in unit time: this is why $\iint_S \vec G \cdot d\vec S$ is called a flux. The sign of the determinant records on which side of the patch $\vec G$ points.
