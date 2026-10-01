---
type: section
subject: "[[Functional Analysis]]"
chapter: 5
section: 16
tags: [functional-analysis, math556]
---
← [[§15 Compactness and the Unit Ball]] · ↑ [[· 5 Inner Product Spaces]] · [[§17 Cauchy–Schwarz and the Induced Norm]] →

*Stage: inner products — Length and angle; $\ell^2$ and $L^2$.*

> [!definition] Definition §16.1: Inner Product; Scalar Product
> Let $X$ be a linear space over $\mathbb{F}$ and let $(\cdot, \cdot) : X \times X \to \mathbb{F}$ be a function.
>
> If $\mathbb{F} = \mathbb{R}$, it is an **inner product** (or **scalar product**) if for all $x, y, z \in X$ and $a, b \in \mathbb{R}$:
> - (1) **bilinearity**: $(ax + by,\, z) = a(x,z) + b(y,z)$ and $(x,\, ay + bz) = a(x,y) + b(x,z)$;
> - (2) **symmetry**: $(x,y) = (y,x)$;
> - (3) **positivity**: $(x,x) \ge 0$, and $(x,x) = 0$ if and only if $x = 0$.
>
> If $\mathbb{F} = \mathbb{C}$, it is an inner product if for all $x, y, z \in X$ and $a, b \in \mathbb{C}$:
> - (1′) **sesquilinearity**: $(ax + by,\, z) = a(x,z) + b(y,z)$ and $(x,\, ay + bz) = \bar{a}(x,y) + \bar{b}(x,z)$;
> - (2′) **skew-symmetry** (conjugate symmetry): $(x,y) = \overline{(y,x)}$;
> - (3′) **positivity**: $(x,x) \ge 0$, and $(x,x) = 0$ if and only if $x = 0$.
>
> The pair $(X, (\cdot,\cdot))$ is an **inner product space** or **scalar product space**.
>
> *Lax: §6.1, (i)–(iii)*

^def-16-1

> [!remark]- Connections
> - The finite-dimensional definition: [[§19 Inner Products and Norms#^ladr-6-2|LADR 6.2]] (inner product), [[§19 Inner Products and Norms#^ladr-6-4|LADR 6.4]] (inner product space).

> [!remark] Remark: Reading the Complex Axioms
> Three points.
>
> First, the placement of the conjugate is a convention: here the inner product is linear in the *first* argument and conjugate-linear in the second, which is the usual convention in mathematics. Physics texts put the conjugate on the first argument. Nothing depends on the choice, but formulas must be read consistently, and every computation below uses this one.
>
> Second, sesquilinearity forces the conjugate in the second slot: if the product were linear in both slots then, taking $a = i$ and $y = z = x$, skew-symmetry would give $i(x,x) = (ix, x) = \overline{(x, ix)} = \overline{i(x,x)} = -i\,\overline{(x,x)}$, which fails for $(x,x) > 0$. “Sesqui” is Latin for one and a half: linear in one argument, conjugate-linear in the other.
>
> Third, positivity is a statement about a real number even though $(\cdot,\cdot)$ is complex-valued: skew-symmetry applied with $y = x$ gives $(x,x) = \overline{(x,x)}$, so $(x,x) \in \mathbb{R}$ automatically, and the inequality $(x,x) \ge 0$ makes sense. The real case is the special case of the complex one in which all values are real and conjugation does nothing. (The second and third points were not made in lecture.)

^rem-16-1

> [!remark]- Connections
> - The physicists' convention, used in the quantum mechanics chapter: [[§22 Bras, Kets, and the Riesz Map#^rem-22-1|Remark: Conventions]].

> [!example] Example §16.1: Euclidean Spaces
> On $\mathbb{R}^n$, $(x,y) = \sum_{i=1}^n x_i y_i$ is an inner product — the dot product. On $\mathbb{C}^n$,
>
> $$
> (x,y) = \sum_{i=1}^n x_i \overline{y_i},
> $$
>
> where the conjugate on the second factor is exactly what makes $(x,x) = \sum_i |x_i|^2 \ge 0$, and is the source of the sesquilinearity convention above.

^ex-16-1

> [!remark]- Connections
> - [[§19 Inner Products and Norms#^ladr-6-1|LADR 6.1]] (dot product), [[§19 Inner Products and Norms#^ladr-6-3|LADR 6.3]] (Euclidean inner product on $\mathbb{F}^n$).

> [!example] Example §16.2: $\ell^2$
> On $\ell^2$, the sequences $a = (a_1, a_2, \ldots)$ with $\|a\|_2 = \bigl(\sum_j |a_j|^2\bigr)^{1/2} < \infty$, define
>
> $$
> (a, b) = \sum_{i=1}^{\infty} a_i \overline{b_i}.
> $$
>
> The series converges absolutely, by Hölder's inequality (Theorem [[§12 Hölder's Inequality for Sequences#^thm-12-1|§12.1]]) with $p = q = 2$:
>
> $$
> \sum_{i=1}^\infty \bigl| a_i \overline{b_i} \bigr| = \sum_{i=1}^\infty |a_i|\,|b_i| \le \|a\|_2\, \|b\|_2 < \infty .
> $$
>
> So the definition makes sense precisely on $\ell^2$, and nowhere else among the $\ell^p$: this is the one exponent for which the conjugate exponent is $p$ itself.
>
> *Lax: §6.1, Example 2*

^ex-16-2

> [!example] Example §16.3: $L^2(\Omega)$
> On $L^2(\Omega)$ define
>
> $$
> (f, g) = \int_\Omega f(x)\, \overline{g(x)}\, dx,
> $$
>
> the direct continuum analogue of the $\mathbb{C}^n$ dot product. The integral converges absolutely by Hölder for functions (Theorem [[§14 The Function Spaces Lᵖ(Ω)#^thm-14-1|§14.1]]) with $p = q = 2$: $\int_\Omega |f \bar g| \le \|f\|_{L^2}\|g\|_{L^2} < \infty$.

^ex-16-3

> [!remark]- Connections
> - $L^2(E)$ as a Hilbert space in 551: [[§19 Normed Linear Spaces and Lᵖ Spaces#^rem-19-1|551 Remark §19.1]]; Hölder's inequality there: [[Hölder's Inequality|551 §19.5]].

> [!remark] Remark
> In each example $(x,x)$ is the square of the norm already attached to the space: $(x,x) = \|x\|_2^2$ on $\mathbb{R}^n$, $\ell^2$, and $L^2$. That is not a coincidence, and the [[§17 Cauchy–Schwarz and the Induced Norm#^thm-17-2|next section]] shows it holds in general: every inner product determines a norm by $\|x\| = (x,x)^{1/2}$. Note the logical order — an inner product space is a linear space with an inner product, no norm assumed; the norm is produced.

^rem-16-2
