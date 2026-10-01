---
type: section
subject: "[[Functional Analysis]]"
chapter: 5
section: 17
tags: [functional-analysis, math556]
---
← [[§16 Definition and Examples]] · ↑ [[· 5 Inner Product Spaces]] · [[§18 Projection and Orthogonal Decomposition]] →

*Stage: inner products — Thread: convexity. Every inner product induces a norm, and the parallelogram law says which norms arise.*

## The Cauchy–Schwarz Inequality

> [!remark] Note: Notation
> Throughout this section $(X, (\cdot,\cdot))$ is an inner product space and
>
> $$
> \|x\| := (x,x)^{1/2},
> $$
>
> which is well defined since $(x,x) \ge 0$. Calling it a norm is an abuse of language until Theorem [[§17 Cauchy–Schwarz and the Induced Norm#^thm-17-2|§17.2]] below; Wu flagged this explicitly while writing the proof.

^rem-17-1

> [!theorem] Theorem §17.1: Cauchy–Schwarz
> For all $x, y$ in an inner product space $X$,
>
> $$
> |(x,y)| \le \|x\|\, \|y\|.
> $$
>
> *Lax: §6.1, Thm 1*

^thm-17-1

> [!proof]+ Proof
> **Step 1: expand a square.** For $t \in \mathbb{F}$, positivity gives $(x + ty,\, x + ty) \ge 0$. Expanding by sesquilinearity,
>
> $$
> (x + ty,\, x + ty) = (x,x) + \bar{t}\,(x,y) + t\,(y,x) + t\bar{t}\,(y,y).
> $$
>
> By skew-symmetry $(x,y) = \overline{(y,x)}$, so $\bar t (x,y) = \overline{t (y,x)}$ and the two middle terms are a number plus its conjugate:
>
> $$
> \|x + ty\|^2 = \|x\|^2 + 2\operatorname{Re}\bigl( t\,(y,x) \bigr) + |t|^2 \|y\|^2 \ \ge\ 0 \qquad \text{for all } t \in \mathbb{F}. \tag{5.1}
> $$
>
> **Step 2: restrict to real $t$ and read off a quadratic.** The inequality holds in particular for $t \in \mathbb{R}$, where $\operatorname{Re}(t(y,x)) = t \operatorname{Re}(y,x)$. Writing
>
> $$
> A = \|y\|^2, \qquad B = \operatorname{Re}(y,x), \qquad C = \|x\|^2,
> $$
>
> (5.1) says
>
> $$
> A t^2 + 2Bt + C \ge 0 \qquad \text{for all } t \in \mathbb{R}.
> $$
>
> **Step 3: complete the square.** If $y = 0$ then both sides of the theorem are $0$ and there is nothing to prove, so assume $y \ne 0$; then $A = \|y\|^2 > 0$ by positivity. For $t \in \mathbb{R}$,
>
> $$
> A t^2 + 2Bt + C = A\Bigl( t + \frac{B}{A} \Bigr)^2 + C - \frac{B^2}{A} \ \ge\ 0 .
> $$
>
> Choosing $t = -B/A$ kills the square and leaves $C - B^2/A \ge 0$, i.e.
>
> $$
> B^2 \le AC, \qquad \text{that is} \qquad \bigl| \operatorname{Re}(y,x) \bigr| \le \|x\|\,\|y\|.
> $$
>
> **Step 4: remove the real part by rotating.** Over $\mathbb{R}$ this already is the theorem. Over $\mathbb{C}$, write the complex number $(y,x)$ in polar form and choose $\theta$ with
>
> $$
> |(y,x)| = e^{i\theta}\,(y,x).
> $$
>
> By linearity in the first argument, $e^{i\theta}(y,x) = (e^{i\theta} y,\, x)$. So $(e^{i\theta}y, x)$ is a non-negative real number, hence equal to its own real part, and Step 3 applied to the pair $e^{i\theta}y$, $x$ gives
>
> $$
> |(y,x)| = \operatorname{Re}\bigl( e^{i\theta} y,\, x \bigr) \le \bigl\| e^{i\theta} y \bigr\|\, \|x\| = \|y\|\,\|x\|,
> $$
>
> where the last equality is
>
> $$
> \bigl\| e^{i\theta} y \bigr\|^2 = \bigl( e^{i\theta} y,\, e^{i\theta} y \bigr) = e^{i\theta}\,\overline{e^{i\theta}}\,(y,y) = |e^{i\theta}|^2 \|y\|^2 = \|y\|^2 .
> $$
>
> Finally $|(x,y)| = |\overline{(y,x)}| = |(y,x)|$, so the bound holds in the stated order as well.

^pf-17-1

*Uses:* [[§16 Definition and Examples#^def-16-1|Def. §16.1]]

> [!remark]- Connections
> - The same inequality in $\mathbb{R}^n$, stated without proof in Chapter 4: [[§11 Means and Young's Inequality#^prop-11-1|§11.1]].
> - The finite-dimensional home: [[Cauchy–Schwarz inequality|LADR 6.14]].
> - The rotation $e^{i\theta}$ that makes a complex number real: [[Functional Analysis Problem-Solving Techniques#^rem-t8|Technique 8]].
> - In $L^2$ it is the case $p = q = 2$ of Hölder's inequality, [[§19 Normed Linear Spaces and Lᵖ Spaces#^thm-19-5|551 Thm. §19.5]].

## The Induced Norm and Hilbert Spaces

> [!theorem] Theorem §17.2: The Inner Product Induces a Norm
> Let $(X, (\cdot,\cdot))$ be an inner product space. Then $\|x\| = (x,x)^{1/2}$ is a norm on $X$, so $(X, \|\cdot\|)$ is a normed linear space.
>
> *Lax: §6.1, (3)*

^thm-17-2

> [!proof]+ Proof
> *Positivity* is axiom (3): $\|x\| = (x,x)^{1/2} \ge 0$, and $\|x\| = 0$ iff $(x,x) = 0$ iff $x = 0$.
>
> *Homogeneity.* By sesquilinearity, for $a \in \mathbb{F}$,
>
> $$
> \|ax\|^2 = (ax, ax) = a \bar{a}\, (x,x) = |a|^2 \|x\|^2,
> $$
>
> and taking non-negative square roots gives $\|ax\| = |a|\,\|x\|$.
>
> *Subadditivity.* This is the only part needing Cauchy–Schwarz. Expanding as in [[§17 Cauchy–Schwarz and the Induced Norm#^pf-17-1|(5.1)]] with $t = 1$ and $y$ in place of $ty$,
>
> $$
> \|x + y\|^2 = \|x\|^2 + 2\operatorname{Re}(x,y) + \|y\|^2 \le \|x\|^2 + 2\,|(x,y)| + \|y\|^2 \le \|x\|^2 + 2\|x\|\,\|y\| + \|y\|^2,
> $$
>
> using $\operatorname{Re} w \le |w|$ and then Theorem [[§17 Cauchy–Schwarz and the Induced Norm#^thm-17-1|§17.1]]. The right-hand side is $\bigl( \|x\| + \|y\| \bigr)^2$, so taking square roots gives $\|x + y\| \le \|x\| + \|y\|$.

^pf-17-2

*Uses:* [[§16 Definition and Examples#^def-16-1|Def. §16.1]], [[§17 Cauchy–Schwarz and the Induced Norm#^thm-17-1|§17.1]], [[§8 Normed Linear Spaces#^def-8-1|Def. §8.1]]

> [!remark]- Connections
> - The finite-dimensional home: [[§19 Inner Products and Norms#^ladr-6-7|LADR 6.7]], [[§19 Inner Products and Norms#^ladr-6-9|LADR 6.9]], [[Triangle inequality|LADR 6.17]].
> - The norm axioms in 551: [[§19 Normed Linear Spaces and Lᵖ Spaces#^def-19-2|551 Def. §19.2]].

> [!remark] Remark
> So every inner product space is a normed linear space, and all of Chapters [[· 3 Normed Linear Spaces|3]] and [[· 4 Infinite-Dimensional Spaces꞉ ℓᵖ, Lᵖ, and Compactness|4]] applies to it. The converse question — which norms come from an inner product — is answered in [[§17 Cauchy–Schwarz and the Induced Norm#Which Norms Come from an Inner Product|§17]].

^rem-17-2

> [!definition] Definition §17.1: Hilbert Space
> An inner product space that is complete in the induced norm $\|x\| = (x,x)^{1/2}$ is a **Hilbert space**.
>
> *Lax: §6.1, definition of Hilbert space*

^def-17-1

> [!remark]- Connections
> - Complete normed spaces: [[§9 Completeness#^def-9-2|Def. §9.2]] (Banach space); in 551, [[§19 Normed Linear Spaces and Lᵖ Spaces#^def-19-4|551 Def. §19.4]], where $L^2$ is noted to be a Hilbert space ([[§19 Normed Linear Spaces and Lᵖ Spaces#^rem-19-1|551 Remark §19.1]]).

> [!example] Example §17.1: Hilbert Spaces
> $\mathbb{R}^n$ and $\mathbb{C}^n$ with the dot product are Hilbert spaces, being finite-dimensional (Corollary [[§10 New Normed Spaces from Old#^cor-10-4|§10.4]]); so are $\ell^2$ and $L^2(\Omega)$ with the inner products of [[§16 Definition and Examples|§16]], complete by Theorems [[§13 Minkowski's Inequality and the Spaces ℓᵖ#^thm-13-5|§13.5]] and [[§14 The Function Spaces Lᵖ(Ω)#^thm-14-3|§14.3]]. Wu: “I proved all $L^p$ is complete; I should at some point put my proof online.”

^ex-17-1

> [!remark]- Connections
> - Completeness of $L^p$ in 551: [[Riesz–Fischer Theorem|551 §19.18]].

> [!example] Example §17.2: An Inner Product Space that is Not a Hilbert Space
> Let $X = C_c(\mathbb{R}^n)$, the continuous functions with compact support (the set where $f \neq 0$ is contained in a bounded set, so $f$ is integrable), with
>
> $$
> (f, g) = \int_{\mathbb{R}^n} f(x)\,\overline{g(x)}\,dx .
> $$
>
> This is the inner product of $L^2(\mathbb{R}^n)$ restricted to $X$, so $(X, (\cdot,\cdot))$ is an inner product space. It is not complete: $C_c(\mathbb{R}^n)$ is dense in $L^2(\mathbb{R}^n)$ (Theorem [[§14 The Function Spaces Lᵖ(Ω)#^thm-14-4|§14.4]]), so any $F \in L^2 \setminus C_c$ is the $L^2$-limit of a sequence in $X$, which is then Cauchy in $X$ with no limit in $X$. By Proposition [[§9 Completeness#^prop-9-5|§9.5]], $\overline{X} = L^2(\mathbb{R}^n)$. (The same argument, with the same conclusion, applies to $C_c^\infty$.)
>
> *Lax: §6.1, Example 1*

^ex-17-2

> [!remark]- Connections
> - Density of $C_c$ in $L^p$: [[§19 Normed Linear Spaces and Lᵖ Spaces#^thm-19-19|551 §19.19]] (iii); for $L^1$, [[Continuous Functions of Compact Support are Dense in L¹|551 §16]].

> [!example] Example §17.3: Sobolev Spaces
> Let $\Omega \subset \mathbb{R}^n$ be a domain, $k \ge 0$ an integer, and $X = C_c^\infty(\Omega)$, the smooth functions whose support is a compact subset of $\Omega$. For a multi-index $\alpha = (\alpha_1, \ldots, \alpha_n)$ write $|\alpha| = \alpha_1 + \cdots + \alpha_n$ and
>
> $$
> \partial^\alpha f = \partial_{x_1}^{\alpha_1} \partial_{x_2}^{\alpha_2} \cdots \partial_{x_n}^{\alpha_n} f ,
> $$
>
> which makes sense for every $\alpha$ because $f$ is $C^\infty$, and is again in $C_c^\infty(\Omega)$. Define
>
> $$
> (f, g) = \sum_{|\alpha| \le k} \int_\Omega \partial^\alpha f(x)\, \overline{\partial^\alpha g(x)}\,dx .
> $$
>
> Each summand is the $L^2$ inner product of two functions in $C_c^\infty$, so this is an inner product on $X$ (a finite sum of inner products with the same sesquilinearity and symmetry; positivity from the $\alpha = 0$ term). The induced norm is $\|f\|^2 = \sum_{|\alpha| \le k} \|\partial^\alpha f\|_{L^2}^2$, which controls $f$ and all its derivatives up to order $k$ in $L^2$. For $k = 0$ this is the previous example. $X$ is not complete; its completion is a **Sobolev space**, denoted $H^k_0(\Omega)$, the subscript recording that it comes from functions with compact support in $\Omega$. Lax (§5.1, example (g)) instead completes the $C^\infty$ functions on $\Omega$ for which the norm is finite, with no support condition, and calls the result $W^{k,p}$; for $p = 2$ it is written $H^k(\Omega)$. Informally, elements of either completion are functions whose derivatives up to order $k$ lie in $L^2$; making this precise requires weak derivatives, which the course does not develop.
>
> Wu's motivation: if $f$ is a velocity, $\int |f|^2$ is an energy, and a physical process with finite, conserved energy naturally lives in a space of this type; the completion is what makes limits of approximate solutions available. This is the setting of the modern theory of partial differential equations, but the course stays with functional analysis.
>
> *Lax: §5.1, example (g)*

^ex-17-3

## Which Norms Come from an Inner Product

> [!theorem] Proposition §17.3: Parallelogram Law and Polarization
> Let $(X, (\cdot,\cdot))$ be an inner product space and $\|x\| = (x,x)^{1/2}$. For all $x, y \in X$:
> - (a) (parallelogram law) $\|x + y\|^2 + \|x - y\|^2 = 2\|x\|^2 + 2\|y\|^2$;
> - (b) (polarization) if $\mathbb{F} = \mathbb{R}$, $(x,y) = \frac14\bigl( \|x+y\|^2 - \|x-y\|^2 \bigr)$; if $\mathbb{F} = \mathbb{C}$,
>
> $$
> (x,y) = \frac14 \bigl( \|x+y\|^2 - \|x-y\|^2 \bigr) + \frac{i}{4} \bigl( \|x+iy\|^2 - \|x-iy\|^2 \bigr) = \frac14 \sum_{k=0}^{3} i^k\, \|x + i^k y\|^2 .
> $$
>
> In particular an inner product is determined by the norm it induces.
>
> *Lax: §6.1, (6)*

^prop-17-3

> [!proof]+ Proof
> (Part (b) not covered in lecture.) By [[§17 Cauchy–Schwarz and the Induced Norm#^pf-17-1|(5.1)]] with $t = \pm 1$, and since $(x,y)$ and $(y,x)$ are conjugate and so have the same real part,
>
> $$
> \|x \pm y\|^2 = \|x\|^2 \pm 2\operatorname{Re}(x,y) + \|y\|^2 .
> $$
>
> Adding the two gives (a): in Wu's words, “$t$ positive cancels with $t$ negative.” Subtracting gives $\|x+y\|^2 - \|x-y\|^2 = 4\operatorname{Re}(x,y)$, which is (b) when $\mathbb{F} = \mathbb{R}$. When $\mathbb{F} = \mathbb{C}$, apply the same identity to $x$ and $iy$: since $(x, iy) = \bar{i}\,(x,y) = -i(x,y)$,
>
> $$
> \|x+iy\|^2 - \|x-iy\|^2 = 4\operatorname{Re}\bigl( -i(x,y) \bigr) = 4\operatorname{Im}(x,y),
> $$
>
> and $(x,y) = \operatorname{Re}(x,y) + i\operatorname{Im}(x,y)$ is the formula in (b).

^pf-17-3

*Uses:* [[§17 Cauchy–Schwarz and the Induced Norm#^pf-17-1|§17.1 (5.1)]], [[§16 Definition and Examples#^def-16-1|Def. §16.1]]

> [!remark]- Connections
> - The finite-dimensional home: [[§19 Inner Products and Norms#^ladr-6-21|LADR 6.21]] (parallelogram equality).
> - Used in Relativity: polarization recovers the Minkowski scalar product from the interval, without positivity — [[§B1.1 The Metric and Index Notation#^thm-b1-1-1|REL Theorem §B1.1.1]].

The parallelogram law is a statement of plane geometry: in the parallelogram spanned by $x$ and $y$, the diagonals are $x + y$ and $x - y$, and the squares of the two diagonals sum to the squares of the four sides.

![[m556-17-1.svg]]
*The parallelogram spanned by $x$ and $y$, with its two diagonals $x + y$ (red) and $x - y$ (blue). The law says the two diagonals' squares add up to the four sides' squares; polarization reads it the other way: the difference of the diagonals' squares is $4\operatorname{Re}(x,y)$, so the norm alone determines the inner product.*

The next theorem says it is the *only* obstruction.

> [!theorem] Theorem §17.4: Jordan–von Neumann
> Let $(X, \|\cdot\|)$ be a normed linear space. There is an inner product $(\cdot,\cdot)$ on $X$ with $(x,x) = \|x\|^2$ for all $x \in X$ if and only if $\|\cdot\|$ satisfies the parallelogram law. The inner product is then unique, given by the polarization formula of Proposition [[§17 Cauchy–Schwarz and the Induced Norm#^prop-17-3|§17.3]](b).
>
> *Source: HW3, Problem 3*
>
> *Lax: §6.1, Exercise 1*

^thm-17-4

> [!proof]+ Proof
> Necessity and uniqueness are Proposition [[§17 Cauchy–Schwarz and the Induced Norm#^prop-17-3|§17.3]]. (HW3, Problem 3.)
> For sufficiency, assume the parallelogram law
>
> $$
> \|x + y\|^2 + \|x - y\|^2 = 2\bigl( \|x\|^2 + \|y\|^2 \bigr) \qquad \text{for all } x, y \in X. \tag{P}
> $$
>
> We treat $\mathbb{F} = \mathbb{R}$ first and then reduce $\mathbb{F} = \mathbb{C}$ to it. Two properties of the norm are used repeatedly: $\|\lambda w\| = |\lambda|\,\|w\|$, in particular $\|{-w}\| = \|w\|$; and the norm is continuous, since $\bigl|\,\|u\| - \|v\|\,\bigr| \leq \|u - v\|$.
>
> **Part 1: the real case.** Let $\mathbb{F} = \mathbb{R}$ and define
>
> $$
> (x, y) := \frac14 \bigl( \|x + y\|^2 - \|x - y\|^2 \bigr), \qquad x, y \in X.
> $$
>
> *Step 1: symmetry and positivity.* Since $y + x = x + y$ and $\|y - x\| = \|{-(x - y)}\| = \|x - y\|$, we have $(y, x) = (x, y)$. Also
>
> $$
> (x, x) = \frac14 \bigl( \|2x\|^2 - \|0\|^2 \bigr) = \frac14 \cdot 4\|x\|^2 = \|x\|^2,
> $$
>
> so $(x,x) \geq 0$, with $(x,x) = 0$ if and only if $x = 0$, and $\|x\|^2 = (x,x)$.
>
> *Step 2: a midpoint identity.* We claim that
>
> $$
> (x, z) + (y, z) = 2\Bigl( \frac{x + y}{2},\, z \Bigr) \qquad \text{for all } x, y, z \in X. \tag{1}
> $$
>
> Put $u = \frac{x + y}{2}$ and $v = \frac{x - y}{2}$, so that $u + v = x$ and $u - v = y$. Applying (P) to the pair $u + z$, $v$ and to the pair $u - z$, $v$,
>
> $$
> \begin{aligned}
> \|x + z\|^2 + \|y + z\|^2 &= \|(u + z) + v\|^2 + \|(u + z) - v\|^2 = 2\|u + z\|^2 + 2\|v\|^2, \\
> \|x - z\|^2 + \|y - z\|^2 &= \|(u - z) + v\|^2 + \|(u - z) - v\|^2 = 2\|u - z\|^2 + 2\|v\|^2.
> \end{aligned}
> $$
>
> Subtracting the second line from the first,
>
> $$
> \bigl( \|x + z\|^2 - \|x - z\|^2 \bigr) + \bigl( \|y + z\|^2 - \|y - z\|^2 \bigr) = 2\bigl( \|u + z\|^2 - \|u - z\|^2 \bigr),
> $$
>
> that is, $4(x,z) + 4(y,z) = 8(u,z)$, which is (1).
>
> *Step 3: additivity in the first argument.* First, $(0, z) = \frac14 \bigl( \|z\|^2 - \|{-z}\|^2 \bigr) = 0$. Taking $y = 0$ in (1) gives $(x, z) = 2\bigl( \frac{x}{2}, z \bigr)$ for every $x \in X$. Applying this with $x + y$ in place of $x$, and then (1),
>
> $$
> (x + y, z) = 2\Bigl( \frac{x + y}{2}, z \Bigr) = (x, z) + (y, z).
> $$
>
> *Step 4: rational homogeneity.* We show $(ax, z) = a(x, z)$ for all $a \in \mathbb{Q}$. For $n \in \mathbb{N}$, induction on $n$ using Step 3 gives $(nx, z) = n(x, z)$, the case $n = 0$ being $(0, z) = 0$. Next,
>
> $$
> (-x, z) = \frac14 \bigl( \|{-x} + z\|^2 - \|{-x} - z\|^2 \bigr) = \frac14 \bigl( \|x - z\|^2 - \|x + z\|^2 \bigr) = -(x, z),
> $$
>
> so $(-nx, z) = -(nx, z) = -n(x, z)$, and the claim holds for all $a \in \mathbb{Z}$. Finally, for $m \in \mathbb{Z}$ and $n \in \mathbb{N}$ with $n \geq 1$,
>
> $$
> n\Bigl( \frac{m}{n}x,\, z \Bigr) = \Bigl( n \cdot \frac{m}{n}x,\, z \Bigr) = (mx, z) = m(x, z),
> $$
>
> and dividing by $n$ gives $\bigl( \frac{m}{n}x, z \bigr) = \frac{m}{n}(x, z)$.
>
> *Step 5: real homogeneity.* Fix $x, z \in X$ and define $\phi, \psi : \mathbb{R} \to \mathbb{R}$ by
>
> $$
> \phi(a) = (ax, z) = \frac14 \bigl( \|ax + z\|^2 - \|ax - z\|^2 \bigr), \qquad \psi(a) = a\,(x, z).
> $$
>
> The maps $a \mapsto ax \pm z$ are continuous from $\mathbb{R}$ to $X$, since $\|(ax \pm z) - (a'x \pm z)\| = |a - a'|\,\|x\|$; the norm is continuous; and $t \mapsto t^2$ is continuous. So $\phi$ is continuous, and so is $\psi$. By Step 4, $\phi = \psi$ on $\mathbb{Q}$. Given $a \in \mathbb{R}$, choose rationals $a_k \to a$; then
>
> $$
> \phi(a) = \lim_{k} \phi(a_k) = \lim_{k} \psi(a_k) = \psi(a).
> $$
>
> Hence $(ax, z) = a(x, z)$ for all $a \in \mathbb{R}$.
>
> *Step 6: conclusion.* By Steps 3 and 5, $(ax + by, z) = (ax, z) + (by, z) = a(x, z) + b(y, z)$ for all $a, b \in \mathbb{R}$, and by the symmetry of Step 1 the same holds in the second argument. Together with Step 1, $(\cdot,\cdot)$ is bilinear, symmetric and positive, i.e. a scalar product on $X$, and $(x, x) = \|x\|^2$ for all $x \in X$.
>
> **Part 2: the complex case.** Let $\mathbb{F} = \mathbb{C}$ and define
>
> $$
> (x, y) := \frac14 \bigl( \|x + y\|^2 - \|x - y\|^2 \bigr) + \frac{i}{4} \bigl( \|x + iy\|^2 - \|x - iy\|^2 \bigr), \qquad x, y \in X.
> $$
>
> Writing $R(x, y) := \frac14 \bigl( \|x + y\|^2 - \|x - y\|^2 \bigr) \in \mathbb{R}$, this reads
>
> $$
> (x, y) = R(x, y) + i\,R(x, iy). \tag{2}
> $$
>
> *Step 1: $R$ is a real scalar product.* Restricting scalar multiplication to $\mathbb{R}$ makes $X$ a linear space over $\mathbb{R}$; $\|\cdot\|$ is still a norm on it, and (P) still holds. By Part 1, $R$ is real-bilinear and symmetric, with $R(x, x) = \|x\|^2$.
>
> *Step 2: two identities.* For all $x, y \in X$,
>
> $$
> \text{(i)}\ \ R(ix, iy) = R(x, y), \qquad \text{(ii)}\ \ R(ix, y) = -R(x, iy).
> $$
>
> For (i): $\|ix \pm iy\| = \|i(x \pm y)\| = |i|\,\|x \pm y\| = \|x \pm y\|$. For (ii): since $i \cdot (-iy) = y$, identity (i) gives $R(ix, y) = R\bigl( ix, i(-iy) \bigr) = R(x, -iy)$, and $R(x, -iy) = -R(x, iy)$ by the real linearity of $R$ in its second argument.
>
> *Step 3: complex linearity in the first argument.* Additivity and real homogeneity, $(x + x', y) = (x, y) + (x', y)$ and $(ax, y) = a(x, y)$ for $a \in \mathbb{R}$, follow from (2) and the real bilinearity of $R$. For multiplication by $i$, by (2), (ii) and (i),
>
> $$
> (ix, y) = R(ix, y) + i\,R(ix, iy) = -R(x, iy) + i\,R(x, y) = i\bigl( R(x, y) + i\,R(x, iy) \bigr) = i\,(x, y).
> $$
>
> Hence, for $c = c_1 + ic_2$ with $c_1, c_2 \in \mathbb{R}$,
>
> $$
> (cx, y) = \bigl( c_1 x + c_2\,(ix),\, y \bigr) = c_1 (x, y) + c_2 (ix, y) = c_1 (x, y) + i c_2 (x, y) = c\,(x, y),
> $$
>
> and together with additivity, $(ax + by, z) = a(x, z) + b(y, z)$ for all $a, b \in \mathbb{C}$.
>
> *Step 4: skew-symmetry.* Since $R$ is real-valued, $\overline{(x, y)} = R(x, y) - i\,R(x, iy)$. On the other hand, by (2), the symmetry of $R$, and (ii),
>
> $$
> (y, x) = R(y, x) + i\,R(y, ix) = R(x, y) + i\,R(ix, y) = R(x, y) - i\,R(x, iy).
> $$
>
> So $(x, y) = \overline{(y, x)}$.
>
> *Step 5: conjugate linearity in the second argument.* By Steps 4 and 3,
>
> $$
> (x, ay + bz) = \overline{(ay + bz, x)} = \overline{a(y, x) + b(z, x)} = \bar{a}\,\overline{(y, x)} + \bar{b}\,\overline{(z, x)} = \bar{a}\,(x, y) + \bar{b}\,(x, z).
> $$
>
> *Step 6: positivity.* By (2), $(x, x) = R(x, x) + i\,R(x, ix)$, where $R(x, x) = \|x\|^2$ and
>
> $$
> R(x, ix) = \frac14 \bigl( \|(1 + i)x\|^2 - \|(1 - i)x\|^2 \bigr) = \frac14 \bigl( |1 + i|^2 - |1 - i|^2 \bigr) \|x\|^2 = 0.
> $$
>
> Hence $(x, x) = \|x\|^2 \geq 0$, with equality if and only if $x = 0$.
>
> By Steps 3–6, $(\cdot,\cdot)$ is sesquilinear, skew-symmetric and positive, i.e. a scalar product on $X$, and $(x, x) = \|x\|^2$ for all $x \in X$.

^pf-17-4

*Uses:* [[§17 Cauchy–Schwarz and the Induced Norm#^prop-17-3|§17.3]], [[§16 Definition and Examples#^def-16-1|Def. §16.1]], [[§8 Normed Linear Spaces#^def-8-1|Def. §8.1]], [[§8 Normed Linear Spaces#^lem-8-3|§8.3]], [[§8 Normed Linear Spaces#^prop-8-4|§8.4]], [[§4 The Completeness Axiom#^thm-4-7|451 §4.7]]

> [!remark]- Connections
> - The finite-dimensional parallelogram equality, whose remark names Jordan–von Neumann: [[§19 Inner Products and Norms#^ladr-6-21|LADR 6.21]].
> - Used to rule out $p \neq 2$: [[§17 Cauchy–Schwarz and the Induced Norm#^cor-17-5|§17.5]]; and as an application of [[Functional Analysis Problem-Solving Techniques#^ex-t10|Technique 10]].

> [!remark] Remark
> Two points about the proof. First, the only genuinely analytic step is real homogeneity: additivity yields it for rational scalars by pure algebra, and continuity of the norm extends it to the reals. Additivity alone would not suffice — there exist additive functions $\mathbb{R} \to \mathbb{R}$ that are not linear, constructed from a Hamel basis — which is why continuity must be invoked. Second, the complex case is reduced to the real one exactly as in the [[§7 The Complex Hahn–Banach Theorem#^thm-7-1|complex Hahn–Banach theorem]]: the real part determines everything, because $\operatorname{Im}(x,y) = \operatorname{Re}(x, iy)$, just as $\operatorname{Im}\ell(x) = -\operatorname{Re}\ell(ix)$ there.

^rem-17-3

> [!theorem] Corollary §17.5: Only $p = 2$ Gives an Inner Product
> Let $1 \le p \le \infty$ with $p \neq 2$. The norm $\|\cdot\|_p$ on $\mathbb{F}^n$ ($n \ge 2$), on $\ell^p$, and on $L^p(\Omega)$ does not come from an inner product.

^cor-17-5

> [!proof]+ Proof
> By Theorem [[§17 Cauchy–Schwarz and the Induced Norm#^thm-17-4|§17.4]] it suffices to exhibit $x, y$ violating the parallelogram law. In $\mathbb{F}^n$ and $\ell^p$ take $x = e_1$, $y = e_2$. In $L^p(\Omega)$ take disjoint $A, B \subset \Omega$ of positive measure (two disjoint small balls) and $x = \chi_A / m(A)^{1/p}$, $y = \chi_B / m(B)^{1/p}$, or $x = \chi_A$, $y = \chi_B$ if $p = \infty$. In each case $\|x\|_p = \|y\|_p = 1$ and $x, y$ have disjoint supports, so $|x \pm y|^p = |x|^p + |y|^p$ pointwise and $\|x \pm y\|_p = 2^{1/p}$ for $p < \infty$, while $\|x \pm y\|_\infty = 1$. The parallelogram law would require $\|x+y\|_p^2 + \|x-y\|_p^2 = 2 \cdot 2^{2/p}$ to equal $2(\|x\|_p^2 + \|y\|_p^2) = 4$, i.e. $2^{2/p} = 2$, i.e. $p = 2$; for $p = \infty$ it would require $2 = 4$. (Not covered in lecture.)

^pf-17-5

*Uses:* [[§17 Cauchy–Schwarz and the Induced Norm#^thm-17-4|§17.4]], [[§13 Minkowski's Inequality and the Spaces ℓᵖ#^def-13-1|Def. §13.1]], [[§14 The Function Spaces Lᵖ(Ω)#^def-14-1|Def. §14.1]]

![[m556-17-2.svg]]
*The proof in $\mathbb{R}^2$: the unit spheres of $\|\cdot\|_1$ (red), $\|\cdot\|_2$ (blue) and $\|\cdot\|_\infty$ (black). The sides $e_1$, $e_2$ of the square have norm $1$ in all three, but the diagonals $e_1 \pm e_2$ (dashed) cross the three spheres at $\tfrac12$, $\tfrac{1}{\sqrt2}$ and $1$ of their length, so their norms are $2$, $\sqrt2$ and $1$. The parallelogram law needs $\|e_1 + e_2\|^2 + \|e_1 - e_2\|^2 = 4$, which only the round sphere delivers.*
