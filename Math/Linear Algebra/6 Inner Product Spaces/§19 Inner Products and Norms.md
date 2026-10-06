---
type: section
subject: "[[Linear Algebra]]"
chapter: 6
section: 19
aliases: ["LADR 6A", "6A Inner Products and Norms"]
tags: [linear-algebra]
---
← [[§18 Commuting Operators]] · ↑ [[· 6 Inner Product Spaces]] · [[§20 Orthonormal Bases]] →

> [!definition] Definition 6.1: Dot product
> For $x,y\in\R^n$ the *dot product* is
> $$
> x\cdot y=x_1y_1+\dots+x_ny_n .
> $$
> It is a number, $x\cdot x=\|x\|^2$, and it is positive definite ($x\cdot x\ge0$, $=0$ iff $x=0$), linear in $x$ for fixed $y$, and symmetric.

^ladr-6-1

> [!remark] Remark: Why the complex case needs conjugates
> For $z\in\C^n$ the length is $\|z\|^2=|z_1|^2+\dots+|z_n|^2=z_1\bar z_1+\dots+z_n\bar z_n$, which suggests pairing $w$ with $z$ as $w_1\bar z_1+\dots+w_n\bar z_n$. Without the bar, $(i)\cdot(i)=-1<0$.

> [!remark]- Connections
> - Abstracted in [[§19 Inner Products and Norms#^ladr-6-2|6.2]].
> - Same definition in ℝ² and ℝ³: [[§82 The Dot Product#^def-82-1|Calc Def. §82.1]] (with worked examples).
> - Computational version: [[§40 Inner Product, Length, and Orthogonality#^def-40-1|235 Def. §40.1]] (the dot product as $\mathbf u^T\mathbf v$) and its properties, [[§40 Inner Product, Length, and Orthogonality#^thm-40-1|235 Thm. §40.1]].

> [!definition] Definition 6.2: Inner product
> An *inner product* on $V$ is a function $(u,v)\mapsto\langle u,v\rangle\in\F$ with
> - **positivity** $\langle v,v\rangle\ge0$;
> - **definiteness** $\langle v,v\rangle=0$ iff $v=0$;
> - **additivity in the first slot** $\langle u+v,w\rangle=\langle u,w\rangle+\langle v,w\rangle$;
> - **homogeneity in the first slot** $\langle\lambda u,v\rangle=\lambda\langle u,v\rangle$;
> - **conjugate symmetry** $\langle u,v\rangle=\overline{\langle v,u\rangle}$.
>
> Over $\R$ the last condition is plain symmetry.

^ladr-6-2

> [!remark] Remark: Convention warning (physics)
> Axler is linear in the **first** slot and conjugate-linear in the second. Physics (Dirac notation, and your PHY 513 conventions) is linear in the **second** slot: $\langle\psi|\phi\rangle_{\text{phys}}=\langle\phi,\psi\rangle_{\text{Axler}}$. Every formula with a conjugate moves slots when translating, e.g. [[§20 Orthonormal Bases#^ladr-6-30|6.30]](c) and [[Riesz representation theorem|6.42]].

> [!remark]- Connections
> - Basic consequences: [[§19 Inner Products and Norms#^ladr-6-6|6.6]]. Norm: [[§19 Inner Products and Norms#^ladr-6-7|6.7]].
> - Same definition in 556 ([[§20 Definition and Examples#^def-20-1|556 Def. §20.1]]); a complete inner product space is a Hilbert space ([[§21 Cauchy–Schwarz and the Induced Norm#^def-21-1|556 Def. §21.1]]), and every finite-dimensional one is complete ([[§12 New Normed Spaces from Old#^cor-12-4|556 Cor. §12.4]]).
> - Computational version: [[§46 Inner Product Spaces#^def-46-1|235 Def. §46.1]] (real inner products, the same axioms, with worked examples).

> [!example] Example 6.3: Inner products (p. 184)
> - (a) **Euclidean** on $\F^n$: $\langle w,z\rangle=w_1\bar z_1+\dots+w_n\bar z_n$.
> - (b) **Weighted**: $\langle w,z\rangle=c_1w_1\bar z_1+\dots+c_nw_n\bar z_n$ for fixed $c_k>0$ (positivity needs every $c_k>0$).
> - (c) On continuous real functions on $[-1,1]$: $\langle f,g\rangle=\int_{-1}^1fg$. Definiteness uses continuity: if $f$ is continuous and $\int_{-1}^1f^2=0$, then the continuous function $f^2\ge0$ vanishes identically, so $f=0$.
> - (d) On $\Poly(\R)$: $\langle p,q\rangle=p(0)q(0)+\int_{-1}^1p'q'$. Definiteness: $\int(p')^2=0$ forces $p$ constant, and $p(0)=0$ forces $p=0$.
> - (e) On $\Poly(\R)$: $\langle p,q\rangle=\int_0^\infty p(x)q(x)e^{-x}\,dx$ (converges because $e^{-x}$ beats polynomials). Gram–Schmidt with this weight produces the Laguerre polynomials; their associated versions appear in the hydrogen radial wave functions.

^ladr-6-3

> [!remark]- Connections
> - Computational version: [[§46 Inner Product Spaces#^ex-46-1|235 Ex. §46.1]] (a weighted inner product on $\mathbb R^2$, as in (b)) and [[§46 Inner Product Spaces#^ex-46-4|235 Ex. §46.4]] (the integral inner product on $C[a,b]$, as in (c)).
> - Computational version of (a) on $\mathbb{C}^n$: [[§28 Matrices#^def-28-3|331 Def. §28.3]], with [[§28 Matrices#^ex-28-2|331 Ex. §28.2]].

> [!definition] Definition 6.4: Inner product space
> An *inner product space* is a vector space $V$ together with an inner product on $V$. $\F^n$ always carries the Euclidean inner product ([[§19 Inner Products and Norms#^ladr-6-3|6.3]](a)) unless said otherwise.

^ladr-6-4

> [!remark] Notation 6.5: V, W (p. 185)
> In this chapter and the next, $V$ and $W$ denote inner product spaces over $\F$.

^ladr-6-5

> [!theorem] Theorem 6.6: Basic properties of an inner product
> In an inner product space:
> - (a) for fixed $v$, $u\mapsto\langle u,v\rangle$ is linear $V\to\F$;
> - (b) $\langle0,v\rangle=0$;
> - (c) $\langle v,0\rangle=0$;
> - (d) $\langle u,v+w\rangle=\langle u,v\rangle+\langle u,w\rangle$;
> - (e) $\langle u,\lambda v\rangle=\bar\lambda\langle u,v\rangle$.

^ladr-6-6

> [!proof]+ Proof
> (a) is additivity and homogeneity in the first slot. (b) follows from (a) and [[§7 Vector Space of Linear Maps#^ladr-3-10|3.10]]. (c) $\langle v,0\rangle=\overline{\langle0,v\rangle}=0$. (d) $\langle u,v+w\rangle=\overline{\langle v+w,u\rangle}=\overline{\langle v,u\rangle}+\overline{\langle w,u\rangle}=\langle u,v\rangle+\langle u,w\rangle$. (e) $\langle u,\lambda v\rangle=\overline{\lambda\langle v,u\rangle}=\bar\lambda\,\overline{\langle v,u\rangle}=\bar\lambda\langle u,v\rangle$.

*Uses:* [[§7 Vector Space of Linear Maps#^ladr-3-10|3.10]]

> [!remark] Remark: Sesquilinear
> So $\langle\cdot,\cdot\rangle$ is linear in the first slot and conjugate-linear in the second ('one and a half' linear).

> [!remark]- Connections
> - (a) is the functional that [[Riesz representation theorem|6.42]] shows is the only kind.
> - Computational version: [[§46 Inner Product Spaces#^prop-46-1|235 Prop. §46.1]] (the same consequences of the axioms, real case).
> - Computational version for the Euclidean inner product on $\mathbb{C}^n$: [[§28 Matrices#^prop-28-2|331 Prop. §28.2]].

> [!definition] Definition 6.7: Norm, ‖v‖
> The *norm* of $v\in V$ is $\|v\|=\sqrt{\langle v,v\rangle}$.

^ladr-6-7

> [!remark]- Connections
> - Properties: [[§19 Inner Products and Norms#^ladr-6-9|6.9]], [[Triangle inequality|6.17]]. Whether a norm comes from an inner product is decided by [[§19 Inner Products and Norms#^ladr-6-21|6.21]].
> - The general notion of a norm, not necessarily coming from an inner product: [[§10 Normed Linear Spaces#^def-10-1|556 Def. §10.1]]; that this one satisfies those axioms is [[§21 Cauchy–Schwarz and the Induced Norm#^thm-21-2|556 Thm. §21.2]].
> - In ℝ² and ℝ³: the length of a vector, [[§81 Vectors#^def-81-6|Calc Def. §81.6]] and [[§81 Vectors#^thm-81-3|Calc Thm. §81.3]] (with worked examples).
> - Computational version: [[§40 Inner Product, Length, and Orthogonality#^def-40-2|235 Def. §40.2]] (length in $\mathbb R^n$) and [[§46 Inner Product Spaces#^def-46-2|235 Def. §46.2]] (in an inner product space).

> [!example] Example 6.8: Norms (p. 186)
> - (a) In $\F^n$: $\|(z_1,\dots,z_n)\|=\sqrt{|z_1|^2+\dots+|z_n|^2}$.
> - (b) With [[§19 Inner Products and Norms#^ladr-6-3|6.3]](c): $\|f\|=\sqrt{\int_{-1}^1f^2}$, the $L^2$ norm. A function can have a small $L^2$ norm while being large at some points.

^ladr-6-8

> [!remark]- Connections
> - Example (a) in ℝ² and ℝ³: [[§81 Vectors#^thm-81-3|Calc Thm. §81.3]]; the distance formula [[§80 Three-Dimensional Coordinate Systems#^thm-80-1|Calc Thm. §80.1]] is ‖P₂ − P₁‖.

> [!theorem] Theorem 6.9: Basic properties of the norm
> For $v\in V$: (a) $\|v\|=0$ iff $v=0$; (b) $\|\lambda v\|=|\lambda|\,\|v\|$ for all $\lambda\in\F$.

^ladr-6-9

> [!proof]+ Proof
> (a) is definiteness. (b) $\|\lambda v\|^2=\langle\lambda v,\lambda v\rangle=\lambda\bar\lambda\langle v,v\rangle=|\lambda|^2\|v\|^2$ ([[§19 Inner Products and Norms#^ladr-6-6|6.6]]); take square roots.

*Uses:* [[§19 Inner Products and Norms#^ladr-6-6|6.6]]

> [!remark] Remark: Working with squares
> Norms squared are inner products and expand algebraically; this is the standard move.

> [!definition] Definition 6.10: Orthogonal
> $u,v\in V$ are *orthogonal* if $\langle u,v\rangle=0$ (symmetric in $u,v$ by conjugate symmetry).

^ladr-6-10

> [!remark] Remark: Geometry
> In $\R^2$, $\langle u,v\rangle=\|u\|\|v\|\cos\theta$, so orthogonal means perpendicular.

> [!remark]- Connections
> - Pythagoras: [[§19 Inner Products and Norms#^ladr-6-12|6.12]]. Orthogonal complements: [[§21 Orthogonal Complements and Minimization Problems#^ladr-6-46|6.46]].
> - In ℝ² and ℝ³: [[§82 The Dot Product#^def-82-3|Calc Def. §82.3]] and the test $\mathbf a \cdot \mathbf b = 0$, [[§82 The Dot Product#^thm-82-4|Calc Thm. §82.4]] (with worked examples).
> - Computational version: [[§40 Inner Product, Length, and Orthogonality#^def-40-5|235 Def. §40.5]] (orthogonal vectors in $\mathbb R^n$); in an inner product space, [[§46 Inner Product Spaces#^def-46-2|235 Def. §46.2]].

> [!theorem] Theorem 6.11: Orthogonality and 0
> (a) $0$ is orthogonal to every vector. (b) $0$ is the only vector orthogonal to itself.

^ladr-6-11

> [!proof]+ Proof
> (a) is [[§19 Inner Products and Norms#^ladr-6-6|6.6]](b). (b) $\langle v,v\rangle=0$ forces $v=0$ by definiteness.

*Uses:* [[§19 Inner Products and Norms#^ladr-6-6|6.6]]

> [!theorem] Theorem 6.12: Pythagorean theorem
> If $u,v\in V$ are orthogonal, then $\|u+v\|^2=\|u\|^2+\|v\|^2$.

^ladr-6-12

> [!proof]+ Proof
> $\|u+v\|^2=\langle u,u\rangle+\langle u,v\rangle+\langle v,u\rangle+\langle v,v\rangle=\|u\|^2+\|v\|^2$.

> [!remark] Remark: Converse
> Over $\R$ the converse holds (the expansion shows $2\langle u,v\rangle=0$). Over $\C$ it fails: $u=1$, $v=i$ in $\C$ satisfy the equation but $\langle u,v\rangle=-i\ne0$; only $\operatorname{Re}\langle u,v\rangle=0$ follows.

> [!remark]- Connections
> - Used in [[Cauchy–Schwarz inequality|6.14]], [[§20 Orthonormal Bases#^ladr-6-24|6.24]], [[§20 Orthonormal Bases#^ladr-6-26|6.26]], [[§21 Orthogonal Complements and Minimization Problems#^ladr-6-61|6.61]].
> - Same statement in 556, together with [[§20 Orthonormal Bases#^ladr-6-24|LADR 6.24]]: [[§24 Orthonormal Sets and Bases#^lem-24-1|556 Lemma §24.1]].
> - The Law of Cosines, [[§119 Trigonometry#^thm-119-11|Calc Thm. §119.11]], reduces to it when the angle is a right angle.
> - Computational version: [[§40 Inner Product, Length, and Orthogonality#^thm-40-4|235 Thm. §40.4]] (the Pythagorean theorem in $\mathbb R^n$, stated as an iff).

> [!theorem] Theorem 6.13: An orthogonal decomposition
> Let $u,v\in V$, $v\ne0$. Set $c=\dfrac{\langle u,v\rangle}{\|v\|^2}$ and $w=u-cv$. Then $u=cv+w$ and $\langle w,v\rangle=0$.

^ladr-6-13

> [!proof]+ Proof
> $\langle w,v\rangle=\langle u,v\rangle-c\|v\|^2=0$. (This is how $c$ was found: require $\langle u-cv,v\rangle=0$ and solve.)

> [!remark]- Connections
> - $cv$ is the orthogonal projection of $u$ onto $\Span(v)$ ([[§21 Orthogonal Complements and Minimization Problems#^ladr-6-56|6.56]]). Iterated, this is Gram–Schmidt ([[Gram–Schmidt procedure|6.32]]). Used for [[Cauchy–Schwarz inequality|6.14]].
> - Computational version: vector and scalar projections, [[§82 The Dot Product#^thm-82-6|Calc Thm. §82.6]] (with worked examples).
> - Computational version: [[§41 Orthogonal Sets#^prop-41-3|235 Prop. §41.3]] (decomposing $\mathbf y$ along $\mathbf u$, with the projection of [[§41 Orthogonal Sets#^def-41-3|235 Def. §41.3]]).

%% ex:6.13-fig %%
> [!example] Example: The orthogonal decomposition, pictured
> $cv$ is the foot of the perpendicular from $u$ to the line $\Span(v)$, and $w=u-cv$ is the perpendicular.
>
> ![[ladr-6.13-orth-decomp.svg|340]]

> [!theorem] Theorem 6.14: Cauchy–Schwarz inequality
> For $u,v\in V$,
> $$
> |\langle u,v\rangle|\le\|u\|\,\|v\|,
> $$
> with equality iff one of $u,v$ is a scalar multiple of the other.

^ladr-6-14

> [!proof]+ Proof
> If $v=0$ both sides are $0$. Otherwise write $u=\frac{\langle u,v\rangle}{\|v\|^2}v+w$ with $w\perp v$ ([[§19 Inner Products and Norms#^ladr-6-13|6.13]]). By [[§19 Inner Products and Norms#^ladr-6-12|6.12]],
> $$
> \|u\|^2=\frac{|\langle u,v\rangle|^2}{\|v\|^2}+\|w\|^2\ \ge\ \frac{|\langle u,v\rangle|^2}{\|v\|^2}.
> $$
> Multiply by $\|v\|^2$ and take square roots. Equality holds iff $w=0$, i.e. iff $u$ is a multiple of $v$.

*Uses:* [[§19 Inner Products and Norms#^ladr-6-13|6.13]], [[§19 Inner Products and Norms#^ladr-6-12|6.12]]

> [!remark]- Connections
> - Computational version: [[§46 Inner Product Spaces#^thm-46-4|235 Thm. §46.4]] (Cauchy–Schwarz in a real inner product space).
> - For integrals: the case $p=2$ of [[Hölder's Inequality|551 Thm. §19.5]], which extends it to $L^p$. In several variables its equality case gives the direction of steepest ascent, $D_{\mathbf u}f=\nabla f\cdot\mathbf u\le|\nabla f|$, [[Directional Derivative Formula|452 Thm. §7.1]].
> - In ℝ² and ℝ³ it follows from $\mathbf a \cdot \mathbf b = |\mathbf a|\,|\mathbf b| \cos\theta$, [[§82 The Dot Product#^thm-82-2|Calc Thm. §82.2]]; used to maximize directional derivatives in [[§95 Directional Derivatives and the Gradient Vector#^thm-95-4|Calc Thm. §95.4]].

%% ex:6.14-fig %%
> [!example] Example: Cauchy–Schwarz as leg $\le$ hypotenuse
> In the decomposition $u=cv+w$ of [[§19 Inner Products and Norms#^ladr-6-13|6.13]] the right triangle has hypotenuse $\|u\|$ and legs $\|cv\|=\frac{|\langle u,v\rangle|}{\|v\|}$ and $\|w\|$. A leg is at most the hypotenuse: that is the inequality. Equality means $w=0$, i.e. $u\in\Span(v)$.
>
> ![[ladr-6.14-cauchy-schwarz.svg|360]]

> [!example] Example 6.16: Cauchy–Schwarz inequality (p. 189)
> - (a) For real $x_k,y_k$: $(x_1y_1+\dots+x_ny_n)^2\le(x_1^2+\dots+x_n^2)(y_1^2+\dots+y_n^2)$.
> - (b) For continuous real $f,g$ on $[-1,1]$: $\Big|\int_{-1}^1fg\Big|^2\le\Big(\int_{-1}^1f^2\Big)\Big(\int_{-1}^1g^2\Big)$.
>
> Both are [[Cauchy–Schwarz inequality|6.14]], for [[§19 Inner Products and Norms#^ladr-6-3|6.3]](a) and [[§19 Inner Products and Norms#^ladr-6-3|6.3]](c). A quick use of (a): $(x_1+\dots+x_n)^2\le n(x_1^2+\dots+x_n^2)$ (take all $y_k=1$).

^ladr-6-16

> [!theorem] Theorem 6.17: Triangle inequality
> For $u,v\in V$,
> $$
> \|u+v\|\le\|u\|+\|v\|,
> $$
> with equality iff one of $u,v$ is a nonnegative real multiple of the other.

^ladr-6-17

> [!proof]+ Proof
> $$
> \|u+v\|^2=\|u\|^2+\|v\|^2+2\operatorname{Re}\langle u,v\rangle\le\|u\|^2+\|v\|^2+2|\langle u,v\rangle|\le\|u\|^2+\|v\|^2+2\|u\|\|v\|=(\|u\|+\|v\|)^2,
> $$
> using [[Cauchy–Schwarz inequality|6.14]] in the last step. Equality forces both inequalities to be equalities, i.e. $\langle u,v\rangle=\|u\|\|v\|$. Then equality in [[Cauchy–Schwarz inequality|6.14]] makes one a multiple of the other, and the scalar must be real and $\ge0$ for $\langle u,v\rangle$ to equal $\|u\|\|v\|\ge0$. Conversely a nonnegative multiple gives equality.

*Uses:* [[Cauchy–Schwarz inequality|6.14]]

> [!remark] Remark: Reverse form
> $\big|\|u\|-\|v\|\big|\le\|u-v\|$, by applying the inequality to $u=(u-v)+v$ and symmetrically.

> [!remark]- Connections
> - Used in Relativity: for timelike vectors in spacetime the inequality reverses, and the straight worldline is the longest — [[§B1.3 Causal Structure and Proper Time#^thm-b1-3-2|REL Theorem §B1.3.2]].
> - Computational version: [[§46 Inner Product Spaces#^thm-46-5|235 Thm. §46.5]] (the triangle inequality in a real inner product space).
> - The case $V=\R$ is the absolute-value triangle inequality, [[§3 The Set ℝ of Real Numbers#^thm-3-3|451 Thm. §3.3]](i). It is axiom 3 of a metric ([[§13 Some Topological Concepts in Metric Spaces#^def-13-1|451 Def. §13.1]]), so $d(u,v)=\|u-v\|$ makes every inner product space a metric space. For the $L^p$ norms it is [[Minkowski's Inequality|551 Thm. §19.9]].

> [!theorem] Theorem 6.21: Parallelogram equality
> For $u,v\in V$,
> $$
> \|u+v\|^2+\|u-v\|^2=2\big(\|u\|^2+\|v\|^2\big).
> $$

^ladr-6-21

> [!proof]+ Proof
> Expand both squares: the cross terms $\pm(\langle u,v\rangle+\langle v,u\rangle)$ cancel, leaving $2\|u\|^2+2\|v\|^2$.

> [!remark] Remark: Which norms come from inner products
> A norm comes from an inner product iff it satisfies this identity (Jordan–von Neumann); the inner product is then recovered by polarization, e.g. over $\R$: $\langle u,v\rangle=\tfrac14\big(\|u+v\|^2-\|u-v\|^2\big)$. The max-norm on $\R^2$ fails it: $u=(1,0)$, $v=(0,1)$ give $1+1\ne4$.

> [!remark]- Connections
> - Geometry: diagonals of a parallelogram (figure below).
> - The converse, that a norm satisfying this identity comes from an inner product, is the Jordan–von Neumann theorem: [[§21 Cauchy–Schwarz and the Induced Norm#^thm-21-4|556 Thm. §21.4]] (polarization in [[§21 Cauchy–Schwarz and the Induced Norm#^prop-21-3|556 Prop. §21.3]]).

%% ex:6.21-fig %%
> [!example] Example: The parallelogram
> The sides are $u,v$ (each twice) and the diagonals $u+v$, $u-v$: the sum of the squares of the diagonals equals the sum of the squares of the four sides.
>
> ![[ladr-6.21-parallelogram.svg|340]]

