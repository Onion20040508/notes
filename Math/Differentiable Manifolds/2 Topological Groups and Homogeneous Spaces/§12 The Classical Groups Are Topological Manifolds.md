---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 2
section: 12
tags: [differentiable-manifolds, math591]
---
← [[§11 Topological Groups and Classical Matrix Groups]] · ↑ [[· 2 Topological Groups and Homogeneous Spaces]] · [[§13 Group Actions and Orbit Spaces]] →

*Thread: equations — The classical groups as regular level sets of polynomial maps ([[§7 The Regular Value Theorem|§7]]): each is a topological manifold.*

> [!remark] Remark: The Method: Level Sets and the Implicit Function Theorem
> “For the first time, we're going to use some calculus.” $\mathrm{SL}(n,\mathbb{R})$ is a *level set*, $\det^{-1}(1)$, of a smooth function on $\mathbb{R}^{n^2}$. Multivariable calculus says that a level set of $F$ is locally a graph—hence locally Euclidean—near any point where $\nabla F \neq 0$. So the work is to compute $\nabla \det$ and show it does not vanish on $\mathrm{SL}(n,\mathbb{R})$. Uribe's methodological message: the [[§37 Determinants#^ladr-9-46|Leibniz formula]] makes computing $\nabla\det$ directly “a nightmare”; instead, *differentiate along curves* and use the [[Multivariable Chain Rule|chain rule]]. “It's nice to compute gradients or differentials using curves.” This kind of computation “will happen several times.”

^rem-12-1

> [!remark]- Connections
> - “Locally a graph near a point with $\nabla F \neq 0$”: [[§7 The Regular Value Theorem#^cor-7-2|§7.2]], home [[§15 The Implicit Function Theorem#^thm-15-2|452 §15.2]].
> - Differentiating along curves, made coordinate-free: [[§22 The Differential of a Map Between Vector Spaces#^thm-22-3|§22.3]].

Throughout, identify $\operatorname{Mat}(n,\mathbb{R}) = \mathbb{R}^{n^2}$ via [[§11 Topological Groups and Classical Matrix Groups#^def-11-2|Definition §11.2]], writing $x_{ij}$ for the coordinate that reads off the $(i,j)$ entry, and for $F : \mathbb{R}^{n^2} \to \mathbb{R}$ differentiable write $\nabla F(g) \in \mathbb{R}^{n^2}$ for the gradient, with components $\partial F/\partial x_{ij}(g)$. The dot product on $\mathbb{R}^{n^2}$ is $A \cdot B = \sum_{i,j} A_{ij} B_{ij}$. The [[Multivariable Chain Rule|chain rule]] for a curve $\gamma$ reads $\frac{d}{dt} F(\gamma(t)) = \nabla F(\gamma(t)) \cdot \gamma'(t)$.

> [!theorem] Proposition §12.1: Derivative of the Determinant
> Let $g \in \mathrm{GL}(n,\mathbb{R})$ and $A \in \operatorname{Mat}(n,\mathbb{R})$. Then
>
> $$
> \nabla \det(g) \cdot A \;=\; \frac{d}{dt}\Big|_{t=0} \det(g + tA) \;=\; \det(g)\, \operatorname{tr}\!\big(g^{-1} A\big).
> $$
>
> In particular, for $g \in \mathrm{SL}(n,\mathbb{R})$: $\nabla\det(g) \cdot A = \operatorname{tr}(g^{-1}A)$.
>
> *Lee: Problem 7-4*

^prop-12-1

> [!proof]+ Proof
> *(Lecture 3's computation, as on the board — page 9 of the handwritten notes. A student caught the order of operations: differentiate first, then set $t = 0$.)* The first equality is the [[Multivariable Chain Rule|chain rule]] applied to the affine line $\gamma(t) = g + tA$, for which $\gamma(0) = g$ and $\gamma'(t) = A$.
>
> For the second, factor out $g$ (invertible): $g + tA = g\,(I + t g^{-1} A)$. Put $V = g^{-1}A$. Since $\det$ is multiplicative,
>
> $$
> \det(g + tA) = \det(g)\, \det(I + tV),
> $$
>
> and $\det(g)$ is a constant, so it suffices to show $\frac{d}{dt}\big|_{t=0} \det(I + tV) = \operatorname{tr} V$. By the Leibniz formula, with $(I + tV)_{ij} = \delta_{ij} + t V_{ij}$,
>
> $$
> \det(I + tV) = \sum_{\sigma \in S_n} \operatorname{sgn}(\sigma) \prod_{i=1}^n \big( \delta_{i,\sigma(i)} + t\, V_{i,\sigma(i)} \big).
> $$
>
> Differentiation is linear, so it passes inside the finite sum. For the product of $n$ factors use the product rule in the form $\frac{d}{dt} \prod_{i=1}^n f_i(t) = \sum_{j=1}^n f_j'(t) \prod_{i \neq j} f_i(t)$; here $f_i(t) = \delta_{i,\sigma(i)} + t V_{i,\sigma(i)}$, so $f_j'(t) = V_{j,\sigma(j)}$. Differentiating first and only then setting $t = 0$ (in the other order one gets $0$),
>
> $$
> \frac{d}{dt}\Big|_{t=0} \det(I + tV) = \sum_{\sigma \in S_n} \operatorname{sgn}(\sigma) \sum_{j=1}^n V_{j,\sigma(j)} \prod_{i \neq j} \delta_{i,\sigma(i)}.
> $$
>
> Fix $\sigma$ and $j$. The product $\prod_{i \neq j} \delta_{i,\sigma(i)}$ is nonzero only if $\sigma(i) = i$ for all $i \neq j$; a permutation fixing $n-1$ of the $n$ symbols is the identity ([[§11 Topological Groups and Classical Matrix Groups#^prop-11-2|Proposition §11.2]](4)), so $\sigma = \mathrm{id}$, for which $\operatorname{sgn}(\sigma) = 1$ and the product equals $1$. Every other permutation contributes $0$. Hence
>
> $$
> \frac{d}{dt}\Big|_{t=0} \det(I + tV) = \sum_{j=1}^n V_{jj} = \operatorname{tr} V = \operatorname{tr}(g^{-1}A).
> $$

^pf-12-1

*Uses:* [[Multivariable Chain Rule|452 §12.2 (chain rule)]], [[§37 Determinants#^ladr-9-49|LADR 9.49]], [[§37 Determinants#^ladr-9-46|LADR 9.46]], [[§11 Topological Groups and Classical Matrix Groups#^def-11-3|Def. §11.3]], [[§11 Topological Groups and Classical Matrix Groups#^def-11-4|Def. §11.4]], [[§11 Topological Groups and Classical Matrix Groups#^prop-11-2|§11.2]], [[§33 Trace꞉ A Connection Between Matrices and Operators#^ladr-8-47|LADR 8.47]], [[§28 Basic Properties of the Derivative#^thm-28-2|451 §28.2]]

> [!remark]- Connections
> - The same computation without coordinates, as the differential of $\det$: [[§22 The Differential of a Map Between Vector Spaces#^thm-22-3|§22.3]].
> - Used in ODEs: along a solution matrix $\mathbf{X}(t)$ of $\mathbf{x}' = \mathbf{P}(t)\mathbf{x}$ it gives $W' = (\operatorname{tr}\mathbf{P})\,W$ for the Wronskian $W = \det\mathbf{X}$, Abel's (Liouville's) formula, [[§36 Basic Theory of Systems of First-Order Linear Equations#^thm-36-3|331 Thm. §36.3]].
> - Used in Quantum Field Theory: at $g = I$, $\det(I + A) = 1 + \operatorname{tr}A$ to first order gives the Jacobian of an infinitesimal change of spacetime coordinates, $d^4x' = [1 + \partial_\mu(\delta x^\mu)]\,d^4x$, which is $1$ for translations and Lorentz transformations — [[§C1.12 Spacetime Symmetries꞉ Energy–Momentum and Angular Momentum#^thm-c1-12-2|QFT Theorem §C1.12.2]].

In lecture the computation was carried out for $g \in \mathrm{SL}(n,\mathbb{R})$, where $\det(g) = 1$ and the factor disappears; the general-$g$ statement (Jacobi's formula) is the same computation with the constant $\det(g)$ carried along.

> [!theorem] Corollary §12.2: Jacobi's Formula — Gradient Form
> For invertible $g$,
>
> $$
> \nabla\det(g) = \det(g)\,(g^{-1})^{\mathsf T}
> $$
>
> as an element of $\mathbb{R}^{n^2}$ arranged as an $n \times n$ matrix; equivalently $\dfrac{\partial \det}{\partial x_{ij}}(g) = \operatorname{adj}(g)_{ji}$, the $(i,j)$ cofactor of $g$.
>
> *Lee: Problem 7-4*

^cor-12-2

> [!proof]+ Proof
> $\det$ is scalar-valued, so its gradient at $g$ is a vector in $\mathbb{R}^{n^2}$, determined by its dot products with all directions $A$, and [[§12 The Classical Groups Are Topological Manifolds#^prop-12-1|Proposition §12.1]] gives those dot products as $\det(g)\operatorname{tr}(g^{-1}A)$. Expanding the trace,
>
> $$
> \operatorname{tr}(g^{-1}A) = \sum_{i,j} (g^{-1})_{ji}\, A_{ij} = \sum_{i,j} \big((g^{-1})^{\mathsf T}\big)_{ij}\, A_{ij} = (g^{-1})^{\mathsf T} \cdot A .
> $$
>
> As this holds for every $A$, $\nabla\det(g) = \det(g)(g^{-1})^{\mathsf T}$. By the cofactor formula $g^{-1} = \operatorname{adj}(g)/\det(g)$ this is $\operatorname{adj}(g)^{\mathsf T}$, whose $(i,j)$ entry is $\operatorname{adj}(g)_{ji}$.

^pf-12-2

*Uses:* [[§12 The Classical Groups Are Topological Manifolds#^prop-12-1|§12.1]], [[§33 Trace꞉ A Connection Between Matrices and Operators#^ladr-8-47|LADR 8.47]], [[§9 Matrices#^ladr-3-54|LADR 3.54]], [[§9 Matrices#^ladr-3-46|LADR 3.46]]

> [!remark] Remark: The Gradient Itself
> Differentiating the determinant with respect to one entry recovers the cofactor expansion along that entry's row. The directional form of [[§12 The Classical Groups Are Topological Manifolds#^prop-12-1|Proposition §12.1]] is the one used in proofs; the gradient form is what one checks against a direct computation for $n = 2$.

^rem-12-2

> [!theorem] Corollary §12.3: $1$ Is a Regular Value of $\det$
> For every $g \in \mathrm{SL}(n,\mathbb{R})$, $\nabla \det(g) \neq 0$. Hence every point of the level set $\det^{-1}(1)$ is a regular point of $\det$, i.e. $1$ is a regular value of $\det$ ([[§7 The Regular Value Theorem#^def-7-4|Definition §7.4]]). Equivalently, $0$ is a regular value of the function $\det - 1$, which has the same gradient and the same level set $\{\det - 1 = 0\}$.
>
> *Lee: Ch. 7, p. 158*

^cor-12-3

> [!proof]+ Proof
> *(Lecture 3: “I can easily find matrices $A$ for which this is not zero, so the gradient cannot be zero”; the choice $A = g$ is filled in.)* Take $A = g$ in [[§12 The Classical Groups Are Topological Manifolds#^prop-12-1|Proposition §12.1]]: $\nabla\det(g) \cdot g = \operatorname{tr}(g^{-1} g) = \operatorname{tr}(I) = n \neq 0$. A vector with a nonzero dot product against something is nonzero.

^pf-12-3

*Uses:* [[§12 The Classical Groups Are Topological Manifolds#^prop-12-1|§12.1]], [[§7 The Regular Value Theorem#^def-7-4|Def. §7.4]], [[§7 The Regular Value Theorem#^def-7-3|Def. §7.3]], [[§11 Topological Groups and Classical Matrix Groups#^def-11-6|Def. §11.6]]

**Transcription note.** Both the board and the audio say “$0 \in \mathbb{R}$ is a regular value of $\det$.” Read literally this is false for $n \ge 2$: the zero matrix lies in $\det^{-1}(0)$, and along the line $\gamma(t) = tA$ one has $\det(tA) = t^n \det A$, whose derivative at $t = 0$ vanishes for $n \ge 2$; so $\nabla\det(0) = 0$ and $0$ is a critical value. What the computation proves is that $1$ is a regular value of $\det$ (or $0$ of $\det - 1$, the form in which level sets are usually written as zero sets). The general statement is [[§12 The Classical Groups Are Topological Manifolds#^cor-12-4|Corollary §12.4]] below.

> [!theorem] Corollary §12.4: Every Nonzero Value Is a Regular Value of $\det$
> Every $c \ne 0$ is a regular value of $\det : \operatorname{Mat}(n,\mathbb{R}) \to \mathbb{R}$, so $\det^{-1}(c)$ is a topological manifold of dimension $n^2 - 1$. For $c = 1$ this is $\mathrm{SL}(n,\mathbb{R})$, treated in [[§12 The Classical Groups Are Topological Manifolds#^cor-12-5|Corollary §12.5]] below.
>
> *Lee: Ch. 7, p. 158*

^cor-12-4

> [!proof]+ Proof
> *(Not from lecture: the general form of [[§12 The Classical Groups Are Topological Manifolds#^cor-12-3|Corollary §12.3]].)* Let $\det g = c \ne 0$. By [[§12 The Classical Groups Are Topological Manifolds#^prop-12-1|Proposition §12.1]] in the direction $A = g$,
>
> $$
> \nabla\det(g) \cdot g = \det(g)\,\operatorname{tr}(g^{-1}g) = c\,n \ne 0,
> $$
>
> so $\nabla\det(g) \ne 0$ and $D\det_g$ is onto $\mathbb{R}$. [[§7 The Regular Value Theorem#^thm-7-3|Theorem §7.3]] gives the manifold.

^pf-12-4

*Uses:* [[§12 The Classical Groups Are Topological Manifolds#^prop-12-1|§12.1]], [[§7 The Regular Value Theorem#^def-7-4|Def. §7.4]], [[§7 The Regular Value Theorem#^thm-7-3|§7.3]]

The passage from “nonvanishing gradient” to “locally a graph” is the Implicit Function Theorem, proved in MATH 452 and used here as a black box. We record it in the general vector-valued form ([[§7 The Regular Value Theorem#^thm-7-1|§7.1]]), since that is what the [[§7 The Regular Value Theorem#^thm-7-3|regular value theorem]] (PSet 1, Problem 6) needs, and then specialize ([[§7 The Regular Value Theorem#^cor-7-2|§7.2]]).

> [!theorem] Corollary §12.5: $\mathrm{SL}(n,\mathbb{R})$ Is a Manifold of Dimension $n^2 - 1$
> $\mathrm{SL}(n,\mathbb{R})$ is a topological manifold of dimension $n^2 - 1$.
>
> *Lee: Ch. 7, p. 158*

^cor-12-5

> [!proof]+ Proof via the Regular Value Theorem
> *(Lecture 3 gave the intuition only — “I'm going to wave my hands a little bit … you will write it in homework six”: the gradient is nonzero, so one of its components is, and the projection forgetting that coordinate has a local inverse, making $\mathrm{SL}(n,\mathbb{R})$ locally a graph. The proof below is that homework, via [[§7 The Regular Value Theorem#^thm-7-3|Theorem §7.3]].)* Apply [[§7 The Regular Value Theorem#^thm-7-3|Theorem §7.3]] to $F = \det - 1$ on $\mathbb{R}^{n^2} = \mathbb{R}^{(n^2-1)+1}$, with $k = 1$: $F$ is a polynomial, $F^{-1}(0) = \mathrm{SL}(n,\mathbb{R})$, and $\nabla F = \nabla \det$ is nonzero at every point of that level set by [[§12 The Classical Groups Are Topological Manifolds#^cor-12-3|Corollary §12.3]], so $0$ is a regular value. Hence $\mathrm{SL}(n,\mathbb{R})$ is a topological manifold of dimension $n^2 - 1$.

^pf-12-5

*Uses:* [[§7 The Regular Value Theorem#^thm-7-3|§7.3]], [[§7 The Regular Value Theorem#^def-7-4|Def. §7.4]], [[§12 The Classical Groups Are Topological Manifolds#^cor-12-3|§12.3]], [[§11 Topological Groups and Classical Matrix Groups#^def-11-6|Def. §11.6]]

The argument given in lecture is the same one specialized by hand; it is recorded because the explicit chart is worth seeing.

> [!proof]+ Proof as given in lecture
> Let $g \in \mathrm{SL}(n,\mathbb{R})$. Number the $N = n^2$ coordinates of $\mathbb{R}^N$ as in [[§11 Topological Groups and Classical Matrix Groups#^def-11-2|Definition §11.2]], so that coordinate $x_k$ with $k = n(i-1)+j$ is the matrix entry $x_{ij}$. By [[§12 The Classical Groups Are Topological Manifolds#^cor-12-3|Corollary §12.3]] some component of $\nabla\det(g)$ is nonzero: $\dfrac{\partial \det}{\partial x_k}(g) \neq 0$ for some $k \in \{1, \ldots, N\}$. If $k \neq N$, let $\tau : \mathbb{R}^N \to \mathbb{R}^N$ be the linear map that swaps coordinates $k$ and $N$. It is a homeomorphism (linear, and its own inverse), so $\tau(\mathrm{SL}(n,\mathbb{R}))$ is homeomorphic to $\mathrm{SL}(n,\mathbb{R})$, and it equals the level set $\{\det \circ \tau^{-1} = 1\}$ of the polynomial $\det \circ \tau^{-1}$, whose gradient at $\tau(g)$ is $\nabla\det(g)$ with coordinates $k$ and $N$ swapped, hence has nonzero last component. Since being locally Euclidean is a topological property, we may replace $(\mathrm{SL}(n,\mathbb{R}), \det)$ by $(\tau(\mathrm{SL}(n,\mathbb{R})), \det \circ \tau^{-1})$; that is, WLOG $k = N$.
>
> Apply [[§7 The Regular Value Theorem#^cor-7-2|Theorem §7.2]] to $F = \det$ (a polynomial, hence $C^\infty$), $a = g$, $c = 1$: there are $W' \ni g'$ open in $\mathbb{R}^{N-1}$, an interval $J \ni g_N$, and a smooth $h : W' \to J$ with
>
> $$
> \mathrm{SL}(n,\mathbb{R}) \cap (W' \times J) = \{\, (x', h(x')) \mid x' \in W' \,\}.
> $$
>
> Set $U = \mathrm{SL}(n,\mathbb{R}) \cap (W' \times J)$. Since $W' \times J$ is open in $\mathbb{R}^N$, $U$ is an open neighborhood of $g$ in $\mathrm{SL}(n,\mathbb{R})$. Define
>
> $$
> \varphi : U \to W', \qquad \varphi(x', x_N) = x' ,
> $$
>
> the restriction to $U$ of the projection $\mathbb{R}^N \to \mathbb{R}^{N-1}$ onto the first $N-1$ coordinates. Then $\varphi$ is continuous (restriction of a continuous map, [[§3 Subspaces and Products#^prop-3-3|Proposition §3.3]]), and it is a bijection onto $W'$ with inverse
>
> $$
> \varphi^{-1} : W' \to U, \qquad \varphi^{-1}(x') = (x', h(x')),
> $$
>
> which is continuous as a map into $\mathbb{R}^N$ (its components $x'$ and $h(x')$ are continuous), hence into the subspace $U$. So $\varphi$ is a homeomorphism from a neighborhood of $g$ onto the open set $W' \subseteq \mathbb{R}^{N-1}$, and [[§2 Topological Manifolds#^prop-2-3|Proposition §2.3]] gives local Euclideanness of dimension $N - 1 = n^2 - 1$. With [[§3 Subspaces and Products#^thm-3-5|Theorem §3.5]] for the two point-set conditions, $\mathrm{SL}(n,\mathbb{R})$ is a topological manifold of dimension $n^2-1$.

^pf-12-5-2

*Uses:* [[§11 Topological Groups and Classical Matrix Groups#^def-11-2|Def. §11.2]], [[§12 The Classical Groups Are Topological Manifolds#^cor-12-3|§12.3]], [[§7 The Regular Value Theorem#^cor-7-2|§7.2]], [[§3 Subspaces and Products#^prop-3-3|§3.3]], [[§2 Topological Manifolds#^prop-2-3|§2.3]], [[§3 Subspaces and Products#^thm-3-5|§3.5]], [[Multivariable Chain Rule|452 §12.2 (chain rule)]], [[§11 Product Topology on Arbitrary Products#^thm-11-1|590 §11.1]]

> [!remark]- Connections
> - The smooth structure on $\mathrm{SL}(n,\mathbb{R})$: [[§20 Manifolds in Euclidean Space#^prop-20-2|§20.2]]; its dimension and tangent space among all six classical groups: [[§25 The Geometric Tangent Space#^thm-25-5|§25.5]].

**Transcription note.** The board (and the handwritten notes) describe the chart as “the projection of $\mathrm{SL}(n,\mathbb{R}) \to \mathbb{R}$ by taking the last component has a local inverse.” The chart is the projection onto the *other* $n^2 - 1$ coordinates, as above; the last coordinate is the one that becomes a function $h$ of the rest. Uribe described this part as hand-waving; the full argument for a general regular level set is PSet 1, Problem 6 ([[§7 The Regular Value Theorem#^thm-7-3|Theorem §7.3]]), which is “a more elaborate version” of this computation.

> [!remark] Remark: Dimension Count
> $\mathrm{SL}(n,\mathbb{R})$ is cut out of $\mathbb{R}^{n^2}$ by one equation with nonvanishing gradient, and it loses exactly one dimension: $\dim \mathrm{SL}(n,\mathbb{R}) = n^2 - 1$. This is the pattern for all the classical groups: $\mathrm{O}(n)$ is cut out by the $\tfrac{n(n+1)}{2}$ independent equations $g^T g = I$ (symmetric matrix), giving $\dim \mathrm{O}(n) = n^2 - \tfrac{n(n+1)}{2} = \tfrac{n(n-1)}{2}$; checking that these equations have independent gradients is done in [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-23-1|Example §23.1]].

^rem-12-3

> [!theorem] Theorem §12.6: Classical Groups Are Manifolds
> Each of $\mathrm{GL}(n,\mathbb{R})$, $\mathrm{SL}(n,\mathbb{R})$, $\mathrm{O}(n,\mathbb{R})$, $\mathrm{SO}(n,\mathbb{R})$, $\mathrm{GL}(n,\mathbb{C})$, and $\mathrm{U}(n)$, with the topology induced from the Euclidean space of matrices, is a topological manifold. (In fact they will turn out to be smooth manifolds, indeed Lie groups.)
>
> *Lee: Examples 1.27 and 7.27–7.30*

^thm-12-6

> [!proof]+ Proof
> The proof has two parts of very different difficulty. The point-set part is free: each group is a subspace of $\mathbb{R}^{n^2}$ or $\mathbb{R}^{2n^2}$, hence $T_2$ and second countable by [[§3 Subspaces and Products#^thm-3-5|Theorem §3.5]]. Local Euclideanness is the real content, and it is established in stages. $\mathrm{GL}(n,\mathbb{R})$ and $\mathrm{GL}(n,\mathbb{C})$ are open subsets of Euclidean space and hence locally Euclidean of dimensions $n^2$ and $2n^2$ ([[§3 Subspaces and Products#^prop-3-6|Proposition §3.6]]). $\mathrm{SL}(n,\mathbb{R})$ is done above, in this section. $\mathrm{O}(n)$, $\mathrm{SO}(n)$ and $\mathrm{U}(n)$ need the coordinate-free differential and are done in [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds|§23, The Orthogonal Group as a Smooth Manifold]] and [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#The Unitary Group as a Smooth Manifold|§23, The Unitary Group as a Smooth Manifold]]; [[§25 The Geometric Tangent Space#^thm-25-5|Theorem §25.5]] collects all six, with their dimensions and geometric tangent spaces.

^pf-12-6

*Uses:* [[§3 Subspaces and Products#^thm-3-5|§3.5]], [[§3 Subspaces and Products#^prop-3-6|§3.6]], [[§12 The Classical Groups Are Topological Manifolds#^cor-12-5|§12.5]], [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-23-1|Ex. §23.1]], [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-23-2|Ex. §23.2]], [[§25 The Geometric Tangent Space#^thm-25-5|§25.5]]

The classical groups through the course: defined in [[§11 Topological Groups and Classical Matrix Groups|Topological Groups and Classical Matrix Groups]], with the examples of [[§16 The Classical Groups|The Classical Groups]]; topological manifolds as level sets in [[§12 The Classical Groups Are Topological Manifolds#^thm-12-6|Classical Groups Are Manifolds]]; $\mathrm{SO}(2)$ and $\mathrm{SO}(3)$ acting on $\mathbb{R}^2$ and $\mathbb{R}^3$ in [[§13 Group Actions and Orbit Spaces#^ex-13-4|the rotations of the plane]] and [[§13 Group Actions and Orbit Spaces#^ex-13-5|the rotations of space]], and $\mathrm{SO}(3)$ on $S^2$ in [[§14 Homogeneous Spaces#^ex-14-2|the isotropy of the north pole]] and [[§14 Homogeneous Spaces#^ex-14-3|the sphere as a homogeneous space]]; $\mathrm{O}(n)$ acting on the Grassmannians in [[§15 The Topology of G∕H and Real Grassmannians#^cor-15-8|Grassmannians as Homogeneous Spaces]]; smooth manifolds in [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-23-1|the orthogonal group]] and [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-23-2|the unitary group]]; their tangent spaces at the identity in [[§25 The Geometric Tangent Space#^thm-25-5|The Classical Groups]], with [[§25 The Geometric Tangent Space#^ex-25-4|the infinitesimal rotations]]; and the double cover $\mathrm{SU}(2) \to \mathrm{SO}(3)$ in [[§41 SU(2) → SO(3)꞉ The Double Cover#^thm-41-4|The Double Cover]].

