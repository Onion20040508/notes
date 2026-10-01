---
type: section
subject: "[[Applied Linear Algebra]]"
chapter: 1
section: 8
lay: "1.8"
aliases: ["Lay 1.8"]
tags: [applied-linear-algebra, math235]
---
← [[§7 Linear Independence]] · ↑ [[· 1 Linear Equations in Linear Algebra]] · [[§9 The Matrix of a Linear Transformation]] →

*Lay, Section 1.8 · MATH 235 lectures Feb-18, L5.*

A matrix $A$ can be seen as acting on vectors: multiplication by $A$ transforms $\mathbf{x}$ into $A\mathbf{x}$. From this dynamic point of view, solving $A\mathbf{x} = \mathbf{b}$ means finding all vectors that $A$ sends to $\mathbf{b}$, and asking whether $\mathbf{b}$ is in the range. The two properties of the matrix–vector product, $A(\mathbf{u} + \mathbf{v}) = A\mathbf{u} + A\mathbf{v}$ and $A(c\mathbf{u}) = cA\mathbf{u}$, define the linear transformations, which preserve linear combinations (the superposition principle) and send $\mathbf{0}$ to $\mathbf{0}$. Projections, shears, dilations and rotations are first examples.

## Transformations

For instance,
$$
\begin{bmatrix} 4 & -3 & 1 & 3 \\ 2 & 0 & 5 & 1 \end{bmatrix}\begin{bmatrix} 1 \\ 1 \\ 1 \\ 1 \end{bmatrix} = \begin{bmatrix} 5 \\ 8 \end{bmatrix}
\qquad\text{and}\qquad
\begin{bmatrix} 4 & -3 & 1 & 3 \\ 2 & 0 & 5 & 1 \end{bmatrix}\begin{bmatrix} 1 \\ 4 \\ -1 \\ 3 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}
$$
say that multiplication by $A$ transforms $\mathbf{x} = (1, 1, 1, 1)$ into $\mathbf{b} = (5, 8)$ and transforms $\mathbf{u} = (1, 4, -1, 3)$ into the zero vector. Solving $A\mathbf{x} = \mathbf{b}$ amounts to finding all vectors $\mathbf{x}$ in $\mathbb{R}^4$ that are transformed into $\mathbf{b}$ in $\mathbb{R}^2$.

> [!definition] Definition §8.1: Transformation, Domain, Codomain, Image, Range
> A **transformation** (or **function** or **mapping**) $T$ from $\mathbb{R}^n$ to $\mathbb{R}^m$ is a rule that assigns to each vector $\mathbf{x}$ in $\mathbb{R}^n$ a vector $T(\mathbf{x})$ in $\mathbb{R}^m$. The set $\mathbb{R}^n$ is the **domain** of $T$, and $\mathbb{R}^m$ is the **codomain** of $T$; the notation $T: \mathbb{R}^n \to \mathbb{R}^m$ records both. For $\mathbf{x}$ in $\mathbb{R}^n$, the vector $T(\mathbf{x})$ is the **image** of $\mathbf{x}$ (under the action of $T$). The set of all images $T(\mathbf{x})$ is the **range** of $T$. (The lecture calls the range the *image of $T$*, and describes $T$ as a vector-valued function on $\mathbb{R}^n$.)
>
> *Lay: 1.8 (text)*

^def-8-1

> [!remark]- Connections
> - The general notions: function [[§8 Functions#^def-8-1|250 Def. §8.1]] and its image [[§8 Functions#^def-8-9|250 Def. §8.9]]; the range here is that image, and the codomain is the target set.

> [!definition] Definition §8.2: Matrix Transformation
> For an $m \times n$ matrix $A$, the **matrix transformation** $\mathbf{x} \mapsto A\mathbf{x}$ is the transformation $T: \mathbb{R}^n \to \mathbb{R}^m$ with $T(\mathbf{x}) = A\mathbf{x}$. The lecture writes it $T_A$. The domain is $\mathbb{R}^n$ because $A$ has $n$ columns, and the codomain is $\mathbb{R}^m$ because each column has $m$ entries.
>
> *Lay: 1.8 (text)*

^def-8-2

> [!theorem] Proposition §8.1: The Range of a Matrix Transformation
> The range of $\mathbf{x} \mapsto A\mathbf{x}$ is the set of all linear combinations of the columns of $A$, that is, the span of the columns of $A$.
>
> *Lay: 1.8 (text)*
> *Source: 235 lecture L5*

^prop-8-1

> [!proof]+ Proof
> Each image $T(\mathbf{x}) = A\mathbf{x} = x_1\mathbf{a}_1 + \cdots + x_n\mathbf{a}_n$ is a linear combination of the columns ([[§4 The Matrix Equation Ax = b#^def-4-1|Definition §4.1]]), and every linear combination $c_1\mathbf{a}_1 + \cdots + c_n\mathbf{a}_n$ is the image $A\mathbf{c}$ of $\mathbf{c} = (c_1, \ldots, c_n)$.

^pf-8-1

*Uses:* [[§4 The Matrix Equation Ax = b#^def-4-1|Def. §4.1]], [[§3 Vector Equations#^def-3-4|Def. §3.4]]

> [!example] Example §8.1: Images, Preimages and the Range
> Let
>
> $$
> A = \begin{bmatrix} 1 & -3 \\ 3 & 5 \\ -1 & 7 \end{bmatrix}, \quad \mathbf{u} = \begin{bmatrix} 2 \\ -1 \end{bmatrix}, \quad \mathbf{b} = \begin{bmatrix} 3 \\ 2 \\ -5 \end{bmatrix}, \quad \mathbf{c} = \begin{bmatrix} 3 \\ 2 \\ 5 \end{bmatrix},
> $$
>
> and define $T: \mathbb{R}^2 \to \mathbb{R}^3$ by $T(\mathbf{x}) = A\mathbf{x}$, so that $T(\mathbf{x}) = (x_1 - 3x_2,\ 3x_1 + 5x_2,\ -x_1 + 7x_2)$.
>
> **(a) Find $T(\mathbf{u})$.**
>
> $$
> T(\mathbf{u}) = A\mathbf{u} = \begin{bmatrix} 1 \cdot 2 - 3 \cdot (-1) \\ 3 \cdot 2 + 5 \cdot (-1) \\ (-1) \cdot 2 + 7 \cdot (-1) \end{bmatrix} = \begin{bmatrix} 5 \\ 1 \\ -9 \end{bmatrix} .
> $$
>
> **(b) Find an $\mathbf{x}$ with $T(\mathbf{x}) = \mathbf{b}$.** Solve $A\mathbf{x} = \mathbf{b}$ ($R_2 - 3R_1$, $R_3 + R_1$; $\tfrac1{14}R_2$; $R_3 - 4R_2$; $R_1 + 3R_2$):
>
> $$
> \begin{bmatrix} 1 & -3 & 3 \\ 3 & 5 & 2 \\ -1 & 7 & -5 \end{bmatrix}
> \sim
> \begin{bmatrix} 1 & -3 & 3 \\ 0 & 14 & -7 \\ 0 & 4 & -2 \end{bmatrix}
> \sim
> \begin{bmatrix} 1 & -3 & 3 \\ 0 & 1 & -.5 \\ 0 & 0 & 0 \end{bmatrix}
> \sim
> \begin{bmatrix} 1 & 0 & 1.5 \\ 0 & 1 & -.5 \\ 0 & 0 & 0 \end{bmatrix} .
> $$
>
> So $\mathbf{x} = (1.5, -.5)$. **Check:** $1.5 + 1.5 = 3$, $4.5 - 2.5 = 2$, $-1.5 - 3.5 = -5$.
>
> **(c) Is there more than one such $\mathbf{x}$?** No: there are no free variables, so the solution of $A\mathbf{x} = \mathbf{b}$ is unique (a uniqueness question in the language of transformations).
>
> **(d) Is $\mathbf{c}$ in the range of $T$?** That is, is $A\mathbf{x} = \mathbf{c}$ consistent (an existence question)? The same operations give
>
> $$
> \begin{bmatrix} 1 & -3 & 3 \\ 3 & 5 & 2 \\ -1 & 7 & 5 \end{bmatrix}
> \sim
> \begin{bmatrix} 1 & -3 & 3 \\ 0 & 14 & -7 \\ 0 & 4 & 8 \end{bmatrix}
> \sim
> \begin{bmatrix} 1 & -3 & 3 \\ 0 & 1 & -.5 \\ 0 & 4 & 8 \end{bmatrix}
> \sim
> \begin{bmatrix} 1 & -3 & 3 \\ 0 & 1 & -.5 \\ 0 & 0 & 10 \end{bmatrix} .
> $$
>
> The third equation is $0 = 10$: no solution, so $\mathbf{c}$ is not in the range of $T$. The range is not all of $\mathbb{R}^3$; by Proposition §8.1 it is the plane spanned by the two columns of $A$.
>
> *Lay: Example 1.8.1*
> *Source: 235 lecture L5*

^ex-8-1

> [!example] Example §8.2: A Projection and a Shear
> **(a) Projection.** If $A = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{bmatrix}$, then $\mathbf{x} \mapsto A\mathbf{x}$ **projects** points of $\mathbb{R}^3$ onto the $x_1x_2$-plane:
>
> $$
> \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} \mapsto \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{bmatrix}\begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} = \begin{bmatrix} x_1 \\ x_2 \\ 0 \end{bmatrix} .
> $$
>
> **(b) Shear.** Let $A = \begin{bmatrix} 1 & 3 \\ 0 & 1 \end{bmatrix}$. $T(\mathbf{x}) = A\mathbf{x}$ is a **shear transformation**. It maps the $2 \times 2$ square $0 \le x_1, x_2 \le 2$ onto the parallelogram with vertices $(0, 0)$, $(2, 0)$, $(8, 2)$, $(6, 2)$. The key facts are that $T$ maps line segments onto line segments (Remark: Lines Go to Lines, below), so it suffices to map the corners:
>
> $$
> T\begin{bmatrix} 0 \\ 2 \end{bmatrix} = \begin{bmatrix} 1 & 3 \\ 0 & 1 \end{bmatrix}\begin{bmatrix} 0 \\ 2 \end{bmatrix} = \begin{bmatrix} 6 \\ 2 \end{bmatrix}, \qquad
> T\begin{bmatrix} 2 \\ 2 \end{bmatrix} = \begin{bmatrix} 8 \\ 2 \end{bmatrix}, \qquad
> T\begin{bmatrix} 2 \\ 0 \end{bmatrix} = \begin{bmatrix} 2 \\ 0 \end{bmatrix} .
> $$
>
> $T$ deforms the square as if its top were pushed to the right while the base is held fixed: $(x_1, x_2) \mapsto (x_1 + 3x_2, x_2)$ moves each point horizontally by three times its height. Shears appear in physics, geology and crystallography.
>
> *Lay: Examples 1.8.2 and 1.8.3*

^ex-8-2

![[m235-8-1.svg]]
*The shear of Example §8.2(b). Vertical grid lines (blue) are tilted, horizontal ones (red) slide to the right by three times their height; straight lines stay straight and parallel lines stay parallel.*

## Linear Transformations

By [[§4 The Matrix Equation Ax = b#^thm-4-5|Theorem §4.5]], $\mathbf{x} \mapsto A\mathbf{x}$ satisfies $A(\mathbf{u} + \mathbf{v}) = A\mathbf{u} + A\mathbf{v}$ and $A(c\mathbf{u}) = cA\mathbf{u}$. Written in function notation, these properties single out the most important class of transformations in linear algebra.

> [!definition] Definition §8.3: Linear Transformation
> A transformation (or mapping) $T$ is **linear** if:
> 1. $T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v})$ for all $\mathbf{u}, \mathbf{v}$ in the domain of $T$;
> 2. $T(c\mathbf{u}) = cT(\mathbf{u})$ for all scalars $c$ and all $\mathbf{u}$ in the domain of $T$.
>
> Linear transformations *preserve the operations of vector addition and scalar multiplication*: adding $\mathbf{u}$ and $\mathbf{v}$ in $\mathbb{R}^n$ and then applying $T$ gives the same result as applying $T$ to each and adding $T(\mathbf{u})$ and $T(\mathbf{v})$ in $\mathbb{R}^m$. (The lecture adds (0) $T(\mathbf{0}) = \mathbf{0}$ to the list, and notes that it follows from (2).)
>
> *Lay: 1.8, Definition*

^def-8-3

> [!remark]- Connections
> - Rigorous treatment: [[§7 Vector Space of Linear Maps#^ladr-3-1|LADR 3.1]], for maps between any vector spaces $V \to W$ over $\mathbb{F}$; [[§7 Vector Space of Linear Maps#^ladr-3-10|LADR 3.10]] is $T(\mathbf{0}) = \mathbf{0}$. Lay meets linear maps on other spaces (polynomials, functions) in Chapters 4 and 5.
> - The total derivative of a differentiable map is a linear transformation, represented by the Jacobian matrix: [[§6 Differentiability#^def-6-2|452 Def. §6.2]].

> [!theorem] Proposition §8.2: Matrix Transformations Are Linear
> Every matrix transformation $\mathbf{x} \mapsto A\mathbf{x}$ is a linear transformation.
>
> *Lay: 1.8 (text)*

^prop-8-2

> [!proof]+ Proof
> Properties (i) and (ii) of Definition §8.3 for $T(\mathbf{x}) = A\mathbf{x}$ are parts (a) and (b) of [[§4 The Matrix Equation Ax = b#^thm-4-5|Theorem §4.5]].

^pf-8-2

*Uses:* [[§4 The Matrix Equation Ax = b#^thm-4-5|§4.5]]

Linear transformations that are not matrix transformations (on spaces of polynomials or functions) appear in Chapters 4 and 5. Between $\mathbb{R}^n$ and $\mathbb{R}^m$, every linear transformation is a matrix transformation ([[§9 The Matrix of a Linear Transformation#^thm-9-1|Theorem §9.1]]).

> [!theorem] Proposition §8.3: Zero, Combinations, Superposition
> If $T$ is a linear transformation, then
>
> $$
> T(\mathbf{0}) = \mathbf{0} \qquad (3)
> $$
>
> and
>
> $$
> T(c\mathbf{u} + d\mathbf{v}) = cT(\mathbf{u}) + dT(\mathbf{v}) \qquad (4)
> $$
>
> for all vectors $\mathbf{u}, \mathbf{v}$ in the domain of $T$ and all scalars $c, d$. Conversely, a transformation that satisfies (4) for all $\mathbf{u}, \mathbf{v}$ and $c, d$ is linear. More generally,
>
> $$
> T(c_1\mathbf{v}_1 + \cdots + c_p\mathbf{v}_p) = c_1T(\mathbf{v}_1) + \cdots + c_pT(\mathbf{v}_p) . \qquad (5)
> $$
>
> *Lay: 1.8, boxed statements (3), (4), (5)*

^prop-8-3

> [!proof]+ Proof
> **(3)** By (ii) with $c = 0$: $T(\mathbf{0}) = T(0\mathbf{u}) = 0\,T(\mathbf{u}) = \mathbf{0}$.
>
> **(4)** By (i), then (ii): $T(c\mathbf{u} + d\mathbf{v}) = T(c\mathbf{u}) + T(d\mathbf{v}) = cT(\mathbf{u}) + dT(\mathbf{v})$.
>
> **Converse.** If (4) holds for all $\mathbf{u}, \mathbf{v}, c, d$, then $c = d = 1$ gives (i), and $d = 0$ gives $T(c\mathbf{u}) = T(c\mathbf{u} + 0\mathbf{v}) = cT(\mathbf{u}) + 0\,T(\mathbf{v}) = cT(\mathbf{u})$, which is (ii).
>
> **(5)** By induction on $p$ ("repeated application of (4)"). For $p = 1$ this is (ii). If (5) holds for $p - 1$ vectors, then by (i), the induction hypothesis and (ii),
>
> $$
> T\Big(\sum_{i=1}^{p} c_i\mathbf{v}_i\Big) = T\Big(\sum_{i=1}^{p-1} c_i\mathbf{v}_i\Big) + T(c_p\mathbf{v}_p) = \sum_{i=1}^{p-1} c_iT(\mathbf{v}_i) + c_pT(\mathbf{v}_p) .
> $$

^pf-8-3

*Uses:* [[§8 Introduction to Linear Transformations#^def-8-3|Def. §8.3]]

In engineering and physics, (5) is the **superposition principle**. Think of $\mathbf{v}_1, \ldots, \mathbf{v}_p$ as signals that go into a system and $T(\mathbf{v}_1), \ldots, T(\mathbf{v}_p)$ as the responses. The system satisfies the superposition principle if, whenever an input is a linear combination of such signals, the response is *the same* linear combination of the individual responses.

> [!example] Example §8.3: Linear or Not?
> **(a)** $T: \mathbb{R}^2 \to \mathbb{R}^3$, $T(x_1, x_2) = (x_1 + x_2,\ x_1 + 2x_2,\ 3x_2)$ is linear. (0): $T(0, 0) = (0 + 0, 0 + 2 \cdot 0, 3 \cdot 0) = \mathbf{0}$. (1): with $\mathbf{x} = (x_1, x_2)$, $\mathbf{y} = (y_1, y_2)$,
>
> $$
> T(\mathbf{x} + \mathbf{y}) = \begin{bmatrix} (x_1 + y_1) + (x_2 + y_2) \\ (x_1 + y_1) + 2(x_2 + y_2) \\ 3(x_2 + y_2) \end{bmatrix} = \begin{bmatrix} x_1 + x_2 \\ x_1 + 2x_2 \\ 3x_2 \end{bmatrix} + \begin{bmatrix} y_1 + y_2 \\ y_1 + 2y_2 \\ 3y_2 \end{bmatrix} = T(\mathbf{x}) + T(\mathbf{y}) .
> $$
>
> (2): similarly $T(a\mathbf{x}) = (ax_1 + ax_2, ax_1 + 2ax_2, 3ax_2) = aT(\mathbf{x})$. In fact $T(\mathbf{x}) = A\mathbf{x}$ with $A = \begin{bmatrix} 1 & 1 \\ 1 & 2 \\ 0 & 3 \end{bmatrix}$. Likewise $(x_1, x_2) \mapsto (2x_1 + 3x_2, -7x_1 + \tfrac12 x_2)$ and $(x_1, x_2) \mapsto x_1 + x_2$ are linear.
>
> **(b)** $T: \mathbb{R}^2 \to \mathbb{R}^2$, $T(x_1, x_2) = (x_1x_2,\ x_2)$ is *not* linear, although $T(\mathbf{0}) = (0 \cdot 0, 0) = \mathbf{0}$. Property (1) fails:
>
> $$
> T(\mathbf{x} + \mathbf{y}) = \begin{bmatrix} (x_1 + y_1)(x_2 + y_2) \\ x_2 + y_2 \end{bmatrix} = \begin{bmatrix} x_1x_2 \\ x_2 \end{bmatrix} + \begin{bmatrix} y_1y_2 \\ y_2 \end{bmatrix} + \begin{bmatrix} x_1y_2 + x_2y_1 \\ 0 \end{bmatrix} = T(\mathbf{x}) + T(\mathbf{y}) + \begin{bmatrix} x_1y_2 + x_2y_1 \\ 0 \end{bmatrix} ,
> $$
>
> and the last vector is not zero in general (for $\mathbf{x} = (1, 0)$, $\mathbf{y} = (0, 1)$ it is $(1, 0)$). Similarly $(x_1, x_2) \mapsto (x_1x_2, x_1^2)$ and $(x_1, x_2) \mapsto (x_1x_2, e^{x_1})$ are not linear.
>
> **(c)** $T: \mathbb{R}^2 \to \mathbb{R}$, $T(x_1, x_2) = 2x_1 + x_2 - 2$ is not linear, because $T(0, 0) = -2 \ne 0$, contradicting (3).
>
> **(d)** The polar-coordinate map $T(r, \theta) = (r\sin\theta,\ r\cos\theta)$ is not linear: it sends the straight grid lines $\theta = $ const and $r = $ const of the $(r, \theta)$-plane to lines through the origin and to circles. Property (2) fails, for instance: $T\big(2(1, \tfrac{\pi}{2})\big) = T(2, \pi) = (0, -2)$, but $2T(1, \tfrac{\pi}{2}) = 2(1, 0) = (2, 0)$.
>
> *Source: 235 lectures Feb-18 and L5*

^ex-8-3

> [!remark] Remark: Recognizing a Linear Transformation
> In practice (lecture): $T: \mathbb{R}^n \to \mathbb{R}^m$, $T(\mathbf{x}) = \big(f_1(x_1, \ldots, x_n), \ldots, f_m(x_1, \ldots, x_n)\big)$, is linear if and only if each component $f_i$ is a linear function of the $x$'s with no constant term, $f_i = a_{i1}x_1 + \cdots + a_{in}x_n$ (so $f_i(0, \ldots, 0) = 0$). Then $T(\mathbf{x}) = A\mathbf{x}$ with $A = [a_{ij}]$. "If" is Proposition §8.2; "only if" follows from [[§9 The Matrix of a Linear Transformation#^thm-9-1|Theorem §9.1]]: a linear $T$ is $\mathbf{x} \mapsto A\mathbf{x}$, and the $i$th entry of $A\mathbf{x}$ is such a linear expression ([[§4 The Matrix Equation Ax = b#^prop-4-4|row–vector rule]]).
>
> *Source: 235 lectures Feb-18 and L5*

^rem-8-1

> [!example] Example §8.4: A Dilation and a Rotation
> **(a)** For a scalar $r$, define $T: \mathbb{R}^2 \to \mathbb{R}^2$ by $T(\mathbf{x}) = r\mathbf{x}$. $T$ is a **contraction** when $0 \le r \le 1$ and a **dilation** when $r > 1$. For $r = 3$, $T$ is linear: for $\mathbf{u}, \mathbf{v}$ in $\mathbb{R}^2$ and scalars $c, d$,
>
> $$
> T(c\mathbf{u} + d\mathbf{v}) = 3(c\mathbf{u} + d\mathbf{v}) = 3c\mathbf{u} + 3d\mathbf{v} = c(3\mathbf{u}) + d(3\mathbf{v}) = cT(\mathbf{u}) + dT(\mathbf{v}),
> $$
>
> using the definition of $T$ and vector arithmetic; so (4) holds.
>
> **(b)** Define $T: \mathbb{R}^2 \to \mathbb{R}^2$ by $T(\mathbf{x}) = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}\begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = \begin{bmatrix} -x_2 \\ x_1 \end{bmatrix}$. For $\mathbf{u} = (4, 1)$, $\mathbf{v} = (2, 3)$, $\mathbf{u} + \mathbf{v} = (6, 4)$:
>
> $$
> T(\mathbf{u}) = \begin{bmatrix} -1 \\ 4 \end{bmatrix}, \qquad T(\mathbf{v}) = \begin{bmatrix} -3 \\ 2 \end{bmatrix}, \qquad T(\mathbf{u} + \mathbf{v}) = \begin{bmatrix} -4 \\ 6 \end{bmatrix} = T(\mathbf{u}) + T(\mathbf{v}) .
> $$
>
> $T$ rotates $\mathbf{u}$, $\mathbf{v}$ and $\mathbf{u} + \mathbf{v}$ counterclockwise about the origin through $90^\circ$; in fact it transforms the whole parallelogram determined by $\mathbf{u}$ and $\mathbf{v}$ into the one determined by $T(\mathbf{u})$ and $T(\mathbf{v})$.
>
> *Lay: Examples 1.8.4 and 1.8.5*

^ex-8-4

> [!example] Example §8.5: From Production to Costs
> With the cost vectors of [[§3 Vector Equations#^ex-3-4|Example §3.4]], form the "unit cost" matrix $U = [\,\mathbf{b}\ \ \mathbf{c}\,]$ (columns: products B and C; rows: materials, labor, overhead), and for a production vector $\mathbf{x} = (x_1, x_2)$ ($x_1$ dollars of B, $x_2$ dollars of C) let
>
> $$
> T(\mathbf{x}) = U\mathbf{x} = x_1\begin{bmatrix} .45 \\ .25 \\ .15 \end{bmatrix} + x_2\begin{bmatrix} .40 \\ .30 \\ .15 \end{bmatrix} = \begin{bmatrix} \text{total cost of materials} \\ \text{total cost of labor} \\ \text{total cost of overhead} \end{bmatrix} .
> $$
>
> $T$ turns production quantities into total costs, and its linearity has two meanings. If production increases by a factor of $4$, from $\mathbf{x}$ to $4\mathbf{x}$, costs increase by the same factor, from $T(\mathbf{x})$ to $4T(\mathbf{x})$. And the cost of the combined production $\mathbf{x} + \mathbf{y}$ is the sum $T(\mathbf{x}) + T(\mathbf{y})$ of the separate costs.
>
> *Lay: Example 1.8.6*

^ex-8-5

> [!remark] Remark: Lines Go to Lines
> A linear transformation maps a line to a line or a point: for the line $\mathbf{x} = \mathbf{p} + t\mathbf{v}$,
>
> $$
> T(\mathbf{p} + t\mathbf{v}) = T(\mathbf{p}) + tT(\mathbf{v}), \qquad t \in \mathbb{R},
> $$
>
> which is the line through $T(\mathbf{p})$ in the direction $T(\mathbf{v})$ if $T(\mathbf{v}) \ne \mathbf{0}$, and the single point $T(\mathbf{p})$ if $T(\mathbf{v}) = \mathbf{0}$. Restricting to $0 \le t \le 1$: the segment from $\mathbf{p}$ to $\mathbf{p} + \mathbf{v}$ goes to the segment from $T(\mathbf{p})$ to $T(\mathbf{p}) + T(\mathbf{v})$ (or a point). In particular the segment from $\mathbf{0}$ to $\mathbf{u}$ goes to the segment from $\mathbf{0}$ to $T(\mathbf{u})$. (Lay leaves these facts to Exercises 25 and 27 and Practice Problem 3.) Parallel lines $\mathbf{p} + t\mathbf{v}$, $\mathbf{q} + t\mathbf{v}$ go to parallel lines (same direction $T(\mathbf{v})$), which is why a linear map turns a square grid into a grid of parallelograms (Figure above), while a nonlinear map such as the polar map of Example §8.3(d) bends it.
>
> The lecture states a converse: $T: \mathbb{R}^n \to \mathbb{R}^m$ is linear if and only if it maps every straight line to a straight line or a point and $T(\mathbf{0}) = \mathbf{0}$. *As stated, the converse needs an extra hypothesis: $T(x_1, x_2) = (x_1^3, 0)$ maps every line onto the $x_1$-axis or onto a point and fixes $\mathbf{0}$, but is not linear. It becomes true for bijections $T: \mathbb{R}^n \to \mathbb{R}^n$ with $n \ge 2$ (the fundamental theorem of affine geometry: such a map is $\mathbf{x} \mapsto A\mathbf{x} + \mathbf{b}$, and $T(\mathbf{0}) = \mathbf{0}$ forces $\mathbf{b} = \mathbf{0}$).*
>
> *Source: 235 lecture L5*

^rem-8-2

> [!remark]- Remark: The Jacobian Conjecture
> A side remark from lecture. A *polynomial transformation* $T: \mathbb{R}^2 \to \mathbb{R}^2$, $T(x, y) = (f(x, y), g(x, y))$ with $f, g$ polynomials (such as $f = x^2 + xy - y^2 + x^5y$), has the Jacobian determinant
>
> $$
> J = \frac{\partial f}{\partial x}\frac{\partial g}{\partial y} - \frac{\partial f}{\partial y}\frac{\partial g}{\partial x}
> $$
>
> (the lecture writes it with the opposite sign, which does not matter here). If $T$ has a polynomial inverse, then $J$ is a nonzero constant (by the chain rule, the product of the Jacobians of $T$ and $T^{-1}$ is $1$, and a polynomial with polynomial reciprocal is constant). The **Jacobian conjecture** (Keller, 1939) asserts the converse: if $J$ is a nonzero constant, then $T$ is bijective with a polynomial inverse. It is open, even for two variables. For a *linear* $T(\mathbf{x}) = A\mathbf{x}$ it is easy: $J = \det A$ is constant, and $\det A \ne 0$ makes $T$ invertible ([[§21 Properties of Determinants#^thm-21-3|Theorem §21.3]], [[§13 Characterizations of Invertible Matrices#^thm-13-3|Theorem §13.3]]). For general smooth maps, $J \ne 0$ gives only a local inverse, by the [[§13 The Inverse Function Theorem#^thm-13-2|inverse function theorem (452)]].
>
> *Source: 235 lecture Feb-18*

^rem-8-3
