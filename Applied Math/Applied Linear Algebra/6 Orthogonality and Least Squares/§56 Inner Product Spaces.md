---
type: section
subject: "[[Applied Linear Algebra]]"
chapter: 6
section: 56
lay: "6.7"
aliases: ["Lay 6.7"]
tags: [applied-linear-algebra, math235]
---
← [[§55 Applications to Linear Models]] · ↑ [[· 6 Orthogonality and Least Squares]] · [[§57 Applications of Inner Product Spaces]] →

*Lay, Section 6.7.*

Length, distance and orthogonality in $\mathbb{R}^n$ were built from four properties of the dot product ([[§49 Inner Product, Length, and Orthogonality#^thm-49-1|Theorem §49.1]]). Here those properties become axioms. Any real vector space with a function $\langle \mathbf{u}, \mathbf{v}\rangle$ satisfying them is an inner product space, and nearly everything in this chapter carries over: orthogonal bases, Gram–Schmidt, projections, best approximation. New examples are weighted inner products on $\mathbb{R}^n$, inner products on polynomials by evaluation at points, and the integral inner product on $C[a, b]$, where "best approximation" means approximating a function. The section also proves the Cauchy–Schwarz and triangle inequalities.

> [!definition] Definition §56.1: Inner Product; Inner Product Space
> An **inner product** on a vector space $V$ is a function that, to each pair of vectors $\mathbf{u}$ and $\mathbf{v}$ in $V$, associates a real number $\langle \mathbf{u}, \mathbf{v}\rangle$ and satisfies the following axioms, for all $\mathbf{u}$, $\mathbf{v}$, $\mathbf{w}$ in $V$ and all scalars $c$:
>
> 1. $\langle \mathbf{u}, \mathbf{v}\rangle = \langle \mathbf{v}, \mathbf{u}\rangle$
> 2. $\langle \mathbf{u} + \mathbf{v}, \mathbf{w}\rangle = \langle \mathbf{u}, \mathbf{w}\rangle + \langle \mathbf{v}, \mathbf{w}\rangle$
> 3. $\langle c\mathbf{u}, \mathbf{v}\rangle = c\langle \mathbf{u}, \mathbf{v}\rangle$
> 4. $\langle \mathbf{u}, \mathbf{u}\rangle \ge 0$, and $\langle \mathbf{u}, \mathbf{u}\rangle = 0$ if and only if $\mathbf{u} = \mathbf{0}$.
>
> A vector space with an inner product is called an **inner product space**. $\mathbb{R}^n$ with $\langle \mathbf{u}, \mathbf{v}\rangle = \mathbf{u} \cdot \mathbf{v}$ (the standard inner product) is one, by [[§49 Inner Product, Length, and Orthogonality#^thm-49-1|Theorem §49.1]].
>
> *Lay: 6.7, Definition*

^def-56-1

> [!remark]- Connections
> - Rigorous treatment: [[§20 Inner Products and Norms#^ladr-6-2|LADR 6.2]], over $\mathbb{R}$ or $\mathbb{C}$ (over $\mathbb{C}$, axiom 1 becomes $\langle u, v\rangle = \overline{\langle v, u\rangle}$); Axler's examples [[§20 Inner Products and Norms#^ladr-6-3|LADR 6.3]] include the weighted inner product of [[§56 Inner Product Spaces#^ex-56-1|Example §56.1]] and the integral inner product of [[§56 Inner Product Spaces#^ex-56-4|Example §56.4]]. Same definition in [[§20 Definition and Examples#^def-20-1|556 Def. §20.1]].
> - The function-space examples become complete only after enlarging $C[a, b]$ to $L^2[a, b]$: [[§20 Definition and Examples#^ex-20-3|556 Ex. §20.3]]; an inner product space of continuous functions that is not complete is [[§21 Cauchy–Schwarz and the Induced Norm#^ex-21-2|556 Ex. §21.2]].

> [!example] Example §56.1: A Weighted Inner Product on ℝ²
> Fix two positive numbers, say $4$ and $5$, and for $\mathbf{u} = (u_1, u_2)$, $\mathbf{v} = (v_1, v_2)$ in $\mathbb{R}^2$ set
>
> $$
> \langle \mathbf{u}, \mathbf{v}\rangle = 4u_1v_1 + 5u_2v_2 . \tag{1}
> $$
>
> Show that (1) defines an inner product.
>
> **Axiom 1.** $\langle \mathbf{u}, \mathbf{v}\rangle = 4u_1v_1 + 5u_2v_2 = 4v_1u_1 + 5v_2u_2 = \langle \mathbf{v}, \mathbf{u}\rangle$.
>
> **Axiom 2.** With $\mathbf{w} = (w_1, w_2)$,
>
> $$
> \langle \mathbf{u} + \mathbf{v}, \mathbf{w}\rangle = 4(u_1 + v_1)w_1 + 5(u_2 + v_2)w_2 = (4u_1w_1 + 5u_2w_2) + (4v_1w_1 + 5v_2w_2) = \langle \mathbf{u}, \mathbf{w}\rangle + \langle \mathbf{v}, \mathbf{w}\rangle .
> $$
>
> **Axiom 3.** $\langle c\mathbf{u}, \mathbf{v}\rangle = 4(cu_1)v_1 + 5(cu_2)v_2 = c(4u_1v_1 + 5u_2v_2) = c\langle \mathbf{u}, \mathbf{v}\rangle$.
>
> **Axiom 4.** $\langle \mathbf{u}, \mathbf{u}\rangle = 4u_1^2 + 5u_2^2 \ge 0$, and $4u_1^2 + 5u_2^2 = 0$ only if $u_1 = u_2 = 0$, that is, $\mathbf{u} = \mathbf{0}$; also $\langle \mathbf{0}, \mathbf{0}\rangle = 0$.
>
> The positivity of the weights is what makes Axiom 4 hold; with a weight $0$ or negative it fails. Weighted inner products like (1) on $\mathbb{R}^n$ arise in weighted least-squares problems, where more reliable measurements get more weight ([[§57 Applications of Inner Product Spaces#^def-57-1|§57]]).
>
> *Lay: Example 6.7.1*

^ex-56-1

From now on, polynomials and other functions in an inner product space are written in the familiar way ($p$, $f$), not in boldface. Each is still a vector of the space.

> [!example] Example §56.2: An Inner Product on Polynomials by Evaluation
> **(a) The inner product.** Let $t_0, \ldots, t_n$ be distinct real numbers. For $p$, $q$ in $\mathbb{P}_n$ define
>
> $$
> \langle p, q\rangle = p(t_0)q(t_0) + p(t_1)q(t_1) + \cdots + p(t_n)q(t_n) . \tag{2}
> $$
>
> Axioms 1–3 follow as in [[§56 Inner Product Spaces#^ex-56-1|Example §56.1]] (each term is symmetric and linear in $p$). For Axiom 4: $\langle p, p\rangle = [p(t_0)]^2 + \cdots + [p(t_n)]^2 \ge 0$, and $\langle \mathbf{0}, \mathbf{0}\rangle = 0$ for the zero polynomial $\mathbf{0}$. If $\langle p, p\rangle = 0$, then $p$ vanishes at the $n + 1$ points $t_0, \ldots, t_n$. A nonzero polynomial of degree at most $n$ has at most $n$ roots, so $p$ is the zero polynomial. So (2) is an inner product on $\mathbb{P}_n$.
>
> **(b) Computing.** Let $V = \mathbb{P}_2$ with $t_0 = 0$, $t_1 = \frac12$, $t_2 = 1$, and let $p(t) = 12t^2$, $q(t) = 2t - 1$. The values are $p(0), p(\frac12), p(1) = 0, 3, 12$ and $q(0), q(\frac12), q(1) = -1, 0, 1$. So
>
> $$
> \langle p, q\rangle = (0)(-1) + (3)(0) + (12)(1) = 12, \qquad \langle q, q\rangle = (-1)^2 + 0^2 + 1^2 = 2 .
> $$
>
> **(c) Lengths** ([[§56 Inner Product Spaces#^def-56-2|Definition §56.2]] below):
>
> $$
> \|p\|^2 = \langle p, p\rangle = 0^2 + 3^2 + 12^2 = 153, \quad \|p\| = \sqrt{153}; \qquad \|q\| = \sqrt{\langle q, q\rangle} = \sqrt2 .
> $$
>
> *Lay: Examples 6.7.2, 6.7.3 and 6.7.4*

^ex-56-2

> [!theorem] Proposition §56.1: Consequences of the Axioms
> In an inner product space $V$, for all $\mathbf{u}, \mathbf{v}, \mathbf{w} \in V$ and scalars $c$:
>
> 1. $\langle \mathbf{v}, \mathbf{0}\rangle = \langle \mathbf{0}, \mathbf{v}\rangle = 0$;
> 2. $\langle \mathbf{u}, \mathbf{v} + \mathbf{w}\rangle = \langle \mathbf{u}, \mathbf{v}\rangle + \langle \mathbf{u}, \mathbf{w}\rangle$;
> 3. $\langle \mathbf{u}, c\mathbf{v}\rangle = c\langle \mathbf{u}, \mathbf{v}\rangle$.
>
> So all the properties of [[§49 Inner Product, Length, and Orthogonality#^thm-49-1|Theorem §49.1]] hold for $\langle\ ,\ \rangle$, including the rule for linear combinations in either slot.
>
> *Lay: 6.7, Practice Problems 1 and 2; Exercise 15*

^prop-56-1

> [!proof]+ Proof
> (1) By Axiom 3 with $c = 0$, $\langle \mathbf{0}, \mathbf{v}\rangle = \langle 0\mathbf{v}, \mathbf{v}\rangle = 0\langle \mathbf{v}, \mathbf{v}\rangle = 0$, and by Axiom 1, $\langle \mathbf{v}, \mathbf{0}\rangle = \langle \mathbf{0}, \mathbf{v}\rangle = 0$.
>
> (2) By Axioms 1, 2 and 1 again: $\langle \mathbf{u}, \mathbf{v} + \mathbf{w}\rangle = \langle \mathbf{v} + \mathbf{w}, \mathbf{u}\rangle = \langle \mathbf{v}, \mathbf{u}\rangle + \langle \mathbf{w}, \mathbf{u}\rangle = \langle \mathbf{u}, \mathbf{v}\rangle + \langle \mathbf{u}, \mathbf{w}\rangle$.
>
> (3) By Axioms 1, 3, 1: $\langle \mathbf{u}, c\mathbf{v}\rangle = \langle c\mathbf{v}, \mathbf{u}\rangle = c\langle \mathbf{v}, \mathbf{u}\rangle = c\langle \mathbf{u}, \mathbf{v}\rangle$.

^pf-56-1

*Uses:* [[§56 Inner Product Spaces#^def-56-1|Def. §56.1]]

## Lengths, Distances, and Orthogonality

> [!definition] Definition §56.2: Length (Norm) in an Inner Product Space
> Let $V$ be an inner product space. As in $\mathbb{R}^n$:
> - the **length** (or **norm**) of $\mathbf{v}$ is $\|\mathbf{v}\| = \sqrt{\langle \mathbf{v}, \mathbf{v}\rangle}$, equivalently $\|\mathbf{v}\|^2 = \langle \mathbf{v}, \mathbf{v}\rangle$;
> - a **unit vector** is a vector of length $1$.
>
> The square root exists by Axiom 4, but $\langle \mathbf{v}, \mathbf{v}\rangle$ need not be a "sum of squares", since $\mathbf{v}$ need not be in $\mathbb{R}^n$. As in [[§49 Inner Product, Length, and Orthogonality#^prop-49-2|Proposition §49.2]], $\|c\mathbf{v}\| = |c|\,\|\mathbf{v}\|$ (by Axiom 3 and [[§56 Inner Product Spaces#^prop-56-1|Proposition §56.1]](3)).
>
> *Lay: 6.7 (text)*

^def-56-2

> [!definition] Definition §56.3: Distance in an Inner Product Space
> Let $V$ be an inner product space. As in $\mathbb{R}^n$, the **distance between $\mathbf{u}$ and $\mathbf{v}$** is $\|\mathbf{u} - \mathbf{v}\|$.
>
> *Lay: 6.7 (text)*

^def-56-3

> [!definition] Definition §56.4: Orthogonality in an Inner Product Space
> Let $V$ be an inner product space. As in $\mathbb{R}^n$, $\mathbf{u}$ and $\mathbf{v}$ are **orthogonal** if $\langle \mathbf{u}, \mathbf{v}\rangle = 0$.
>
> *Lay: 6.7 (text)*

^def-56-4

## The Gram–Schmidt Process

> [!theorem] Theorem §56.2: Orthogonal Bases and Projections in an Inner Product Space
> Let $W$ be a finite-dimensional subspace of an inner product space $V$.
>
> 1. **Gram–Schmidt.** The formulas of [[§53 The Gram–Schmidt Process#^thm-53-1|Theorem §53.1]], with $\mathbf{x} \cdot \mathbf{v}$ replaced by $\langle \mathbf{x}, \mathbf{v}\rangle$, turn any basis of $W$ into an orthogonal basis of $W$. In particular, if $W \ne \{\mathbf{0}\}$, it has an orthogonal basis.
> 2. **Orthogonal decomposition.** If $\{\mathbf{u}_1, \ldots, \mathbf{u}_p\}$ is an orthogonal basis of $W$, every $\mathbf{v} \in V$ can be written uniquely as $\mathbf{v} = \hat{\mathbf{v}} + \mathbf{z}$ with $\hat{\mathbf{v}} \in W$ and $\mathbf{z}$ orthogonal to every vector of $W$, and
>
> $$
> \hat{\mathbf{v}} = \operatorname{proj}_W \mathbf{v} = \frac{\langle \mathbf{v}, \mathbf{u}_1\rangle}{\langle \mathbf{u}_1, \mathbf{u}_1\rangle}\mathbf{u}_1 + \cdots + \frac{\langle \mathbf{v}, \mathbf{u}_p\rangle}{\langle \mathbf{u}_p, \mathbf{u}_p\rangle}\mathbf{u}_p .
> $$
>
> The projection does not depend on the choice of orthogonal basis.
> 3. **Best approximation.** $\|\mathbf{v} - \operatorname{proj}_W \mathbf{v}\| < \|\mathbf{v} - \mathbf{w}\|$ for every $\mathbf{w} \in W$ with $\mathbf{w} \ne \operatorname{proj}_W \mathbf{v}$.
>
> *Lay: 6.7 (text)*

^thm-56-2

> [!proof]+ Proof
> Lay states that these hold "just as in $\mathbb{R}^n$". Indeed, the proofs of [[§51 Orthogonal Sets#^thm-51-1|Theorem §51.1]] (orthogonal sets of nonzero vectors are independent), [[§50 Orthogonal Complements and Angles#^thm-50-1|Theorem §50.1]] (the vectors orthogonal to $W$ form a subspace meeting $W$ only in $\mathbf{0}$, and orthogonality to a spanning set suffices), [[§49 Inner Product, Length, and Orthogonality#^prop-49-3|Proposition §49.3]] and the Pythagorean Theorem [[§49 Inner Product, Length, and Orthogonality#^thm-49-4|§49.4]], the Orthogonal Decomposition Theorem [[§52 Orthogonal Projections#^thm-52-1|§52.1]], the Best Approximation Theorem [[§52 Orthogonal Projections#^thm-52-3|§52.3]] and Gram–Schmidt [[§53 The Gram–Schmidt Process#^thm-53-1|§53.1]] use only:
> - the properties (a)–(d) of [[§49 Inner Product, Length, and Orthogonality#^thm-49-1|Theorem §49.1]], which hold for $\langle\ ,\ \rangle$ by the axioms and [[§56 Inner Product Spaces#^prop-56-1|Proposition §56.1]];
> - dimension counting inside the finite-dimensional spaces $W$ and $W_k = \operatorname{Span}\{\mathbf{x}_1, \ldots, \mathbf{x}_k\}$ (the Basis Theorem, [[§33 The Dimension of a Vector Space#^thm-33-5|Theorem §33.5]], which Lay proves for any vector space).
>
> They never use coordinates of vectors in $\mathbb{R}^n$, or the dimension of the ambient space. So they hold verbatim with $\mathbf{u} \cdot \mathbf{v}$ replaced by $\langle \mathbf{u}, \mathbf{v}\rangle$, even when $V$ is infinite-dimensional, as $C[a, b]$ is. (Only $W$ must be finite-dimensional: Gram–Schmidt and the projection formula need a finite basis of $W$.) Uniqueness of the decomposition shows that the projection does not depend on the orthogonal basis chosen, exactly as in [[§52 Orthogonal Projections#^def-52-1|Definition §52.1]].

^pf-56-2

*Uses:* [[§49 Inner Product, Length, and Orthogonality#^thm-49-1|§49.1]] (properties (a)–(d)), [[§50 Orthogonal Complements and Angles#^thm-50-1|§50.1]], [[§49 Inner Product, Length, and Orthogonality#^prop-49-3|§49.3]], [[§49 Inner Product, Length, and Orthogonality#^thm-49-4|§49.4]], [[§51 Orthogonal Sets#^thm-51-1|§51.1]], [[§52 Orthogonal Projections#^thm-52-1|§52.1]], [[§52 Orthogonal Projections#^thm-52-3|§52.3]], [[§53 The Gram–Schmidt Process#^thm-53-1|§53.1]], [[§56 Inner Product Spaces#^prop-56-1|§56.1]], [[§33 The Dimension of a Vector Space#^thm-33-5|§33.5]], [[§52 Orthogonal Projections#^def-52-1|Def. §52.1]] (the projection does not depend on the basis)

> [!remark]- Connections
> - PDE version: [[§15★ Mean Error and Convergence in Mean#^thm-15-2|341 Thm. §15.2]] (part 3 for the integral inner product: the truncated Fourier series is the best mean-square approximation by trigonometric polynomials); Gram–Schmidt applied to $1, x, x^2, \ldots$ in $C[-1, 1]$ gives, up to scaling, the Legendre polynomials, [[§60★ Spherical Coordinates; Legendre Polynomials#^def-60-3|341 Def. §60.3]], orthogonal by [[§60★ Spherical Coordinates; Legendre Polynomials#^prop-60-5|341 Prop. §60.5]].

A common problem in applied mathematics is to approximate a function $f$ in a space $V$ of functions by a function $g$ from a specified subspace $W$. How close the approximation is depends on how $\|f - g\|$ is defined. When the distance comes from an inner product, [[§56 Inner Product Spaces#^thm-56-2|Theorem §56.2]](3) says that **the best approximation to $f$ by functions in $W$ is the orthogonal projection of $f$ onto $W$**.

> [!example] Example §56.3: Orthogonal Polynomials and a Best Approximation
> Let $V = \mathbb{P}_4$ with the inner product (2) given by evaluation at $-2, -1, 0, 1, 2$, and view $\mathbb{P}_2$ as a subspace of $V$.
>
> **(a) An orthogonal basis of $\mathbb{P}_2$.** The inner product depends only on the values at $-2, \ldots, 2$, so record each polynomial by its vector of values in $\mathbb{R}^5$. The inner product of two polynomials is then the ordinary dot product of their value vectors. (A polynomial in $\mathbb{P}_4$ is determined by its values at five points; the correspondence $p \mapsto$ (values) is an isomorphism $\mathbb{P}_4 \to \mathbb{R}^5$.)
>
> $$
> 1: \begin{bmatrix} 1 \\ 1 \\ 1 \\ 1 \\ 1 \end{bmatrix}, \qquad t: \begin{bmatrix} -2 \\ -1 \\ 0 \\ 1 \\ 2 \end{bmatrix}, \qquad t^2: \begin{bmatrix} 4 \\ 1 \\ 0 \\ 1 \\ 4 \end{bmatrix} .
> $$
>
> Apply Gram–Schmidt to $1, t, t^2$. Since $\langle t, 1\rangle = -2 - 1 + 0 + 1 + 2 = 0$, take $p_0(t) = 1$ and $p_1(t) = t$. For $p_2$, project $t^2$ onto $\operatorname{Span}\{p_0, p_1\}$:
>
> $$
> \langle t^2, p_0\rangle = 4 + 1 + 0 + 1 + 4 = 10, \qquad \langle p_0, p_0\rangle = 5, \qquad \langle t^2, p_1\rangle = -8 - 1 + 0 + 1 + 8 = 0 .
> $$
>
> The projection is $\frac{10}{5}p_0 + 0p_1 = 2$, so $p_2(t) = t^2 - 2$. The orthogonal basis of $\mathbb{P}_2$ is
>
> $$
> p_0: \begin{bmatrix} 1 \\ 1 \\ 1 \\ 1 \\ 1 \end{bmatrix}, \qquad p_1: \begin{bmatrix} -2 \\ -1 \\ 0 \\ 1 \\ 2 \end{bmatrix}, \qquad p_2: \begin{bmatrix} 2 \\ -1 \\ -2 \\ -1 \\ 2 \end{bmatrix} . \tag{3}
> $$
>
> **(b) Best approximation.** Find the best approximation to $p(t) = 5 - \frac12t^4$ by polynomials in $\mathbb{P}_2$. The values of $p$ at $-2, -1, 0, 1, 2$ are $-3, \frac92, 5, \frac92, -3$. Using (3),
>
> $$
> \langle p, p_0\rangle = -3 + \tfrac92 + 5 + \tfrac92 - 3 = 8, \qquad \langle p, p_1\rangle = 6 - \tfrac92 + 0 + \tfrac92 - 6 = 0, \qquad \langle p, p_2\rangle = -6 - \tfrac92 - 10 - \tfrac92 - 6 = -31,
> $$
>
> and $\langle p_0, p_0\rangle = 5$, $\langle p_2, p_2\rangle = 4 + 1 + 4 + 1 + 4 = 14$. By [[§56 Inner Product Spaces#^thm-56-2|Theorem §56.2]],
>
> $$
> \hat{p} = \operatorname{proj}_{\mathbb{P}_2} p = \frac{\langle p, p_0\rangle}{\langle p_0, p_0\rangle}p_0 + \frac{\langle p, p_1\rangle}{\langle p_1, p_1\rangle}p_1 + \frac{\langle p, p_2\rangle}{\langle p_2, p_2\rangle}p_2 = \frac85p_0 - \frac{31}{14}p_2 = \frac85 - \frac{31}{14}(t^2 - 2) .
> $$
>
> This is the polynomial in $\mathbb{P}_2$ closest to $p$ *when distance is measured only at $-2, -1, 0, 1, 2$*. Polynomials such as $p_0, p_1, p_2$ are called **orthogonal polynomials** in statistics; tables list them by their values at points such as $-2, \ldots, 2$.
>
> *Lay: Examples 6.7.5 and 6.7.6*

^ex-56-3

![[m235-46-1.svg]]
*[[§56 Inner Product Spaces#^ex-56-3|Example §56.3]]: $p(t) = 5 - \frac12t^4$ (blue) and its best approximation $\hat{p}(t) = \frac85 - \frac{31}{14}(t^2 - 2)$ in $\mathbb{P}_2$ (red), for the inner product given by evaluation at the five marked points $t = -2, \ldots, 2$. Away from these points the two graphs separate; the inner product does not see that.*

## Two Inequalities

> [!theorem] Proposition §56.3: The Projection Is Shorter
> Let $W$ be a finite-dimensional subspace of an inner product space $V$ and $\mathbf{v} \in V$. Then
>
> $$
> \|\mathbf{v}\|^2 = \|\operatorname{proj}_W \mathbf{v}\|^2 + \|\mathbf{v} - \operatorname{proj}_W \mathbf{v}\|^2, \qquad\text{so}\qquad \|\operatorname{proj}_W \mathbf{v}\| \le \|\mathbf{v}\| .
> $$
>
> In words: the hypotenuse is the longest side.
>
> *Lay: 6.7 (text)*

^prop-56-3

> [!proof]+ Proof
> By [[§56 Inner Product Spaces#^thm-56-2|Theorem §56.2]](2), $\mathbf{v} = \operatorname{proj}_W \mathbf{v} + (\mathbf{v} - \operatorname{proj}_W \mathbf{v})$, where the first term lies in $W$ and the second is orthogonal to $W$, in particular to the first term. The Pythagorean Theorem (valid in $V$ by [[§56 Inner Product Spaces#^thm-56-2|Theorem §56.2]]'s proof: $\|\mathbf{a} + \mathbf{b}\|^2 = \|\mathbf{a}\|^2 + \|\mathbf{b}\|^2 + 2\langle \mathbf{a}, \mathbf{b}\rangle$) gives the equality, and dropping the nonnegative second term gives the inequality.

^pf-56-3

*Uses:* [[§56 Inner Product Spaces#^thm-56-2|§56.2]], [[§49 Inner Product, Length, and Orthogonality#^thm-49-4|§49.4]]

> [!theorem] Theorem §56.4: The Cauchy–Schwarz Inequality
> For all $\mathbf{u}$, $\mathbf{v}$ in an inner product space $V$,
>
> $$
> |\langle \mathbf{u}, \mathbf{v}\rangle| \le \|\mathbf{u}\|\,\|\mathbf{v}\| . \tag{4}
> $$
>
> *Lay: Theorem 16 (6.7)*

^thm-56-4

> [!proof]+ Proof
> If $\mathbf{u} = \mathbf{0}$, both sides of (4) are $0$ ([[§56 Inner Product Spaces#^prop-56-1|Proposition §56.1]](1)), so (4) holds. If $\mathbf{u} \ne \mathbf{0}$, let $W = \operatorname{Span}\{\mathbf{u}\}$. Using $\|c\mathbf{u}\| = |c|\,\|\mathbf{u}\|$,
>
> $$
> \|\operatorname{proj}_W \mathbf{v}\| = \Big\| \frac{\langle \mathbf{v}, \mathbf{u}\rangle}{\langle \mathbf{u}, \mathbf{u}\rangle}\mathbf{u} \Big\| = \frac{|\langle \mathbf{v}, \mathbf{u}\rangle|}{|\langle \mathbf{u}, \mathbf{u}\rangle|}\|\mathbf{u}\| = \frac{|\langle \mathbf{v}, \mathbf{u}\rangle|}{\|\mathbf{u}\|^2}\|\mathbf{u}\| = \frac{|\langle \mathbf{u}, \mathbf{v}\rangle|}{\|\mathbf{u}\|} .
> $$
>
> By [[§56 Inner Product Spaces#^prop-56-3|Proposition §56.3]], $\|\operatorname{proj}_W \mathbf{v}\| \le \|\mathbf{v}\|$, so $\dfrac{|\langle \mathbf{u}, \mathbf{v}\rangle|}{\|\mathbf{u}\|} \le \|\mathbf{v}\|$, which is (4).

^pf-56-4

*Uses:* [[§56 Inner Product Spaces#^prop-56-3|§56.3]], [[§56 Inner Product Spaces#^prop-56-1|§56.1]], [[§56 Inner Product Spaces#^def-56-2|Def. §56.2]]

In $\mathbb{R}^n$ this is the Cauchy inequality $(u_1v_1 + \cdots + u_nv_n)^2 \le (u_1^2 + \cdots + u_n^2)(v_1^2 + \cdots + v_n^2)$, which the lecture read off from $\mathbf{u} \cdot \mathbf{v} = \|\mathbf{u}\|\,\|\mathbf{v}\|\cos\vartheta$ in $\mathbb{R}^2$ and $\mathbb{R}^3$ ([[§50 Orthogonal Complements and Angles#^rem-50-2|§50, Remark: The Cauchy Inequality]]). The proof above needs no angles, and it is what justifies defining the angle in $\mathbb{R}^n$ by $\cos\vartheta = \mathbf{u} \cdot \mathbf{v} / (\|\mathbf{u}\|\,\|\mathbf{v}\|)$.

> [!theorem] Theorem §56.5: The Triangle Inequality
> For all $\mathbf{u}$, $\mathbf{v}$ in an inner product space $V$,
>
> $$
> \|\mathbf{u} + \mathbf{v}\| \le \|\mathbf{u}\| + \|\mathbf{v}\| .
> $$
>
> *Lay: Theorem 17 (6.7)*

^thm-56-5

> [!proof]+ Proof
> $$
> \begin{aligned}
> \|\mathbf{u} + \mathbf{v}\|^2 = \langle \mathbf{u} + \mathbf{v}, \mathbf{u} + \mathbf{v}\rangle &= \langle \mathbf{u}, \mathbf{u}\rangle + 2\langle \mathbf{u}, \mathbf{v}\rangle + \langle \mathbf{v}, \mathbf{v}\rangle \\
> &\le \|\mathbf{u}\|^2 + 2|\langle \mathbf{u}, \mathbf{v}\rangle| + \|\mathbf{v}\|^2 \\
> &\le \|\mathbf{u}\|^2 + 2\|\mathbf{u}\|\,\|\mathbf{v}\| + \|\mathbf{v}\|^2 && \text{(Cauchy–Schwarz)} \\
> &= (\|\mathbf{u}\| + \|\mathbf{v}\|)^2 .
> \end{aligned}
> $$
>
> The first line expands by Axioms 1, 2 and [[§56 Inner Product Spaces#^prop-56-1|Proposition §56.1]](2). Taking square roots of both (nonnegative) sides gives the triangle inequality.

^pf-56-5

*Uses:* [[§56 Inner Product Spaces#^thm-56-4|§56.4]], [[§56 Inner Product Spaces#^prop-56-1|§56.1]]

> [!remark]- Connections
> - Rigorous treatment: [[§20 Inner Products and Norms#^ladr-6-14|LADR 6.14]] (Cauchy–Schwarz, with equality iff one vector is a multiple of the other; Axler's proof uses the orthogonal decomposition [[§20 Inner Products and Norms#^ladr-6-13|LADR 6.13]], the same projection idea) and [[§20 Inner Products and Norms#^ladr-6-17|LADR 6.17]] (triangle inequality).
> - In 556: [[§21 Cauchy–Schwarz and the Induced Norm#^thm-21-1|556 Thm. §21.1]] and [[§21 Cauchy–Schwarz and the Induced Norm#^thm-21-2|556 Thm. §21.2]] (the inner product induces a norm); the parallelogram law characterizes the norms that come from inner products, [[§21 Cauchy–Schwarz and the Induced Norm#^thm-21-4|556 Thm. §21.4]].

## An Inner Product for C[a, b] (Calculus Required)

> [!remark] Remark: From Evaluation to Integration
> Let $p$ be a polynomial and $n \ge \deg p$. Evaluation at $n + 1$ points of $[a, b]$ gives a "length" of $p$ ([[§56 Inner Product Spaces#^ex-56-2|Example §56.2]]), but it sees only those points. Since $p \in \mathbb{P}_n$ for all large $n$, one can use many more points. Partition $[a, b]$ into $n + 1$ subintervals of length $\Delta t = (b - a)/(n + 1)$ and pick points $t_0, \ldots, t_n$ in them. For large $n$ the evaluation inner product of $\mathbb{P}_n$ gives large values, so scale it down by $n + 1$; since $\frac{1}{n + 1} = \frac{\Delta t}{b - a}$,
>
> $$
> \langle p, q\rangle = \frac{1}{n + 1}\sum_{j=0}^n p(t_j)q(t_j) = \frac{1}{b - a}\Big[\sum_{j=0}^n p(t_j)q(t_j)\,\Delta t\Big] .
> $$
>
> As $n \to \infty$, the bracket is a Riemann sum ([[§39 The Definite Integral#^def-39-3|Calc Def. §39.3]]) of the continuous function $pq$ and tends to $\int_a^b p(t)q(t)\,dt$. So the limit is the *average value* of $p(t)q(t)$ on $[a, b]$:
>
> $$
> \frac{1}{b - a}\int_a^b p(t)q(t)\,dt .
> $$
>
> This makes sense for all continuous functions, not only polynomials. The factor $\frac{1}{b - a}$ is inessential and is usually omitted.

^rem-56-1

> [!example] Example §56.4: The Integral Inner Product on C[a, b]
> For $f$, $g$ in $C[a, b]$, the space of continuous functions on $[a, b]$, set
>
> $$
> \langle f, g\rangle = \int_a^b f(t)g(t)\,dt . \tag{5}
> $$
>
> Show that (5) defines an inner product on $C[a, b]$.
>
> Axioms 1–3 follow from elementary properties of definite integrals: $\int fg = \int gf$, $\int (f + g)h = \int fh + \int gh$, $\int (cf)g = c\int fg$. For Axiom 4,
>
> $$
> \langle f, f\rangle = \int_a^b [f(t)]^2\,dt \ge 0,
> $$
>
> since $[f(t)]^2$ is continuous and nonnegative on $[a, b]$. If $\int_a^b [f(t)]^2\,dt = 0$, then $[f(t)]^2$ must be identically zero on $[a, b]$, by a theorem of advanced calculus ([[§33 Properties of the Riemann Integral#^cor-33-8|451 Cor. §33.8]]), so $f$ is the zero function. Thus $\langle f, f\rangle = 0$ implies $f = 0$, and (5) is an inner product.
>
> *Lay: Example 6.7.7*

^ex-56-4

> [!example] Example §56.5: Gram–Schmidt in C[0, 1]
> Let $V = C[0, 1]$ with the inner product (5), and let $W$ be spanned by $p_1(t) = 1$, $p_2(t) = 2t - 1$, $p_3(t) = 12t^2$. Find an orthogonal basis of $W$.
>
> Let $q_1 = p_1$. Then
>
> $$
> \langle p_2, q_1\rangle = \int_0^1 (2t - 1)(1)\,dt = (t^2 - t)\Big|_0^1 = 0,
> $$
>
> so $p_2$ is already orthogonal to $q_1$, and $q_2 = p_2$. For the projection of $p_3$ onto $W_2 = \operatorname{Span}\{q_1, q_2\}$:
>
> $$
> \begin{aligned}
> \langle p_3, q_1\rangle &= \int_0^1 12t^2\,dt = 4t^3\Big|_0^1 = 4, &
> \langle q_1, q_1\rangle &= \int_0^1 1\,dt = 1, \\
> \langle p_3, q_2\rangle &= \int_0^1 12t^2(2t - 1)\,dt = \int_0^1 (24t^3 - 12t^2)\,dt = 6 - 4 = 2, &
> \langle q_2, q_2\rangle &= \int_0^1 (2t - 1)^2\,dt = \frac16(2t - 1)^3\Big|_0^1 = \frac13 .
> \end{aligned}
> $$
>
> Then
>
> $$
> \operatorname{proj}_{W_2} p_3 = \frac{4}{1}q_1 + \frac{2}{1/3}q_2 = 4q_1 + 6q_2, \qquad
> q_3 = p_3 - 4q_1 - 6q_2 = 12t^2 - 4 - 6(2t - 1) = 12t^2 - 12t + 2 .
> $$
>
> The orthogonal basis is $\{1,\ 2t - 1,\ 12t^2 - 12t + 2\}$. (Check: $\int_0^1 (12t^2 - 12t + 2)\,dt = 4 - 6 + 2 = 0$.) Up to scaling these are the Legendre polynomials moved from $[-1, 1]$ to $[0, 1]$.
>
> *Lay: Example 6.7.8*

^ex-56-5
