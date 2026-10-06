---
type: section
subject: "[[Functional Analysis]]"
chapter: 5
section: 23
tags: [functional-analysis, math556]
---
← [[§22 Definition and Examples]] · ↑ [[· 5 Inner Product Spaces]] · [[§24 The Parallelogram Law and Jordan–von Neumann]] →

*Stage: inner products — Thread: convexity. Every inner product induces a norm.*

## The Cauchy–Schwarz Inequality

> [!remark] Note: Notation
> Throughout this section $(X, (\cdot,\cdot))$ is an inner product space and
>
> $$
> \|x\| := (x,x)^{1/2},
> $$
>
> which is well defined since $(x,x) \ge 0$. Calling it a norm is an abuse of language until Theorem [[§23 Cauchy–Schwarz and the Induced Norm#^thm-23-2|§23.2]] below; Wu flagged this explicitly while writing the proof.

^rem-23-1

> [!theorem] Theorem §23.1: Cauchy–Schwarz
> For all $x, y$ in an inner product space $X$,
>
> $$
> |(x,y)| \le \|x\|\, \|y\|.
> $$
>
> *Lax: §6.1, Thm 1*

^thm-23-1

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

^pf-23-1

*Uses:* [[§22 Definition and Examples#^def-22-1|Def. §22.1]]

> [!remark]- Connections
> - The same inequality in $\mathbb{R}^n$, stated without proof in Chapter 4: [[§16 Means and Young's Inequality#^prop-16-1|§16.1]].
> - The finite-dimensional home: [[Cauchy–Schwarz inequality|LADR 6.14]].
> - The rotation $e^{i\theta}$ that makes a complex number real: [[Functional Analysis Problem-Solving Techniques#^rem-t8|Technique 8]].
> - In $L^2$ it is the case $p = q = 2$ of Hölder's inequality, [[§34 Normed Linear Spaces and Lᵖ Spaces#^thm-34-5|551 Thm. §34.5]].
> - Computational version: [[§56 Inner Product Spaces#^thm-56-4|235 Thm. §56.4]] (real inner product spaces).

## The Induced Norm and Hilbert Spaces

> [!theorem] Theorem §23.2: The Inner Product Induces a Norm
> Let $(X, (\cdot,\cdot))$ be an inner product space. Then $\|x\| = (x,x)^{1/2}$ is a norm on $X$, so $(X, \|\cdot\|)$ is a normed linear space.
>
> *Lax: §6.1, (3)*

^thm-23-2

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
> *Subadditivity.* This is the only part needing Cauchy–Schwarz. Expanding as in [[§23 Cauchy–Schwarz and the Induced Norm#^pf-23-1|(5.1)]] with $t = 1$ and $y$ in place of $ty$,
>
> $$
> \|x + y\|^2 = \|x\|^2 + 2\operatorname{Re}(x,y) + \|y\|^2 \le \|x\|^2 + 2\,|(x,y)| + \|y\|^2 \le \|x\|^2 + 2\|x\|\,\|y\| + \|y\|^2,
> $$
>
> using $\operatorname{Re} w \le |w|$ and then Theorem [[§23 Cauchy–Schwarz and the Induced Norm#^thm-23-1|§23.1]]. The right-hand side is $\bigl( \|x\| + \|y\| \bigr)^2$, so taking square roots gives $\|x + y\| \le \|x\| + \|y\|$.

^pf-23-2

*Uses:* [[§22 Definition and Examples#^def-22-1|Def. §22.1]], [[§23 Cauchy–Schwarz and the Induced Norm#^thm-23-1|§23.1]], [[§11 Normed Linear Spaces#^def-11-1|Def. §11.1]]

> [!remark]- Connections
> - The finite-dimensional home: [[§20 Inner Products and Norms#^ladr-6-7|LADR 6.7]], [[§20 Inner Products and Norms#^ladr-6-9|LADR 6.9]], [[Triangle inequality|LADR 6.17]].
> - The norm axioms in 551: [[§34 Normed Linear Spaces and Lᵖ Spaces#^def-34-2|551 Def. §34.2]].
> - Computational version: length from an inner product, [[§56 Inner Product Spaces#^def-56-2|235 Def. §56.2]], and the triangle inequality, [[§56 Inner Product Spaces#^thm-56-5|235 Thm. §56.5]].

> [!remark] Remark
> So every inner product space is a normed linear space, and all of Chapters [[· 3 Normed Linear Spaces|3]] and [[· 4 Infinite-Dimensional Spaces꞉ ℓᵖ, Lᵖ, and Compactness|4]] applies to it. The converse question — which norms come from an inner product — is answered in [[§24 The Parallelogram Law and Jordan–von Neumann#Which Norms Come from an Inner Product|§24]].

^rem-23-2

> [!definition] Definition §23.1: Hilbert Space
> An inner product space that is complete in the induced norm $\|x\| = (x,x)^{1/2}$ is a **Hilbert space**.
>
> *Lax: §6.1, definition of Hilbert space*

^def-23-1

> [!remark]- Connections
> - Complete normed spaces: [[§12 Completeness#^def-12-2|Def. §12.2]] (Banach space); in 551, [[§34 Normed Linear Spaces and Lᵖ Spaces#^def-34-5|551 Def. §34.5]], where $L^2$ is noted to be a Hilbert space ([[§34 Normed Linear Spaces and Lᵖ Spaces#^rem-34-1|551 Remark §19.1]]).

> [!example] Example §23.1: Hilbert Spaces
> $\mathbb{R}^n$ and $\mathbb{C}^n$ with the dot product are Hilbert spaces, being finite-dimensional (Corollary [[§14 New Normed Spaces from Old#^cor-14-4|§14.4]]); so are $\ell^2$ and $L^2(\Omega)$ with the inner products of [[§22 Definition and Examples|§22]], complete by Theorems [[§18 Minkowski's Inequality and the Spaces ℓᵖ#^thm-18-5|§18.5]] and [[§19 The Function Spaces Lᵖ(Ω)#^thm-19-3|§19.3]]. Wu: “I proved all $L^p$ is complete; I should at some point put my proof online.”

^ex-23-1

> [!remark]- Connections
> - Completeness of $L^p$ in 551: [[Riesz–Fischer Theorem|551 §35.11]].

> [!example] Example §23.2: An Inner Product Space that is Not a Hilbert Space
> Let $X = C_c(\mathbb{R}^n)$, the continuous functions with compact support (the set where $f \neq 0$ is contained in a bounded set, so $f$ is integrable), with
>
> $$
> (f, g) = \int_{\mathbb{R}^n} f(x)\,\overline{g(x)}\,dx .
> $$
>
> This is the inner product of $L^2(\mathbb{R}^n)$ restricted to $X$, so $(X, (\cdot,\cdot))$ is an inner product space. It is not complete: $C_c(\mathbb{R}^n)$ is dense in $L^2(\mathbb{R}^n)$ (Theorem [[§19 The Function Spaces Lᵖ(Ω)#^thm-19-4|§19.4]]), so any $F \in L^2 \setminus C_c$ is the $L^2$-limit of a sequence in $X$, which is then Cauchy in $X$ with no limit in $X$. By Proposition [[§13 The Completion of a Normed Space#^prop-13-2|§13.2]], $\overline{X} = L^2(\mathbb{R}^n)$. (The same argument, with the same conclusion, applies to $C_c^\infty$.)
>
> *Lax: §6.1, Example 1*

^ex-23-2

> [!remark]- Connections
> - Density of $C_c$ in $L^p$: [[§35 Lᵖ as a Banach Space#^thm-35-12|551 §35.12]] (iii); for $L^1$, [[Continuous Functions of Compact Support are Dense in L¹|551 §16]].

> [!example] Example §23.3: Sobolev Spaces
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

^ex-23-3
