---
type: section
subject: "[[Functional Analysis]]"
chapter: 6
section: 33
tags: [functional-analysis, math556]
---
← [[§32 Sesquilinear Forms and the Lax–Milgram Theorem]] · ↑ [[· 6 Bounded Linear Maps]] · [[§34 Weak Solutions of the Dirichlet Problem]] →

*Stage: maps — Thread: completeness. Completing smooth functions in a norm that sees derivatives; the elements of the completion have derivatives only in a weak sense.*

[[§32 Sesquilinear Forms and the Lax–Milgram Theorem#^thm-32-2|Lax–Milgram]] is applied to elliptic PDE in Sobolev spaces. They were first met as completions in Example [[§23 Cauchy–Schwarz and the Induced Norm#^ex-23-3|§23.3]]; this section says what their elements are.

## Sobolev Spaces as Completions

> [!definition] Definition §33.1: The Sobolev Norm
> Let $\Omega \subset \mathbb{R}^n$ be bounded and open, with closure $\overline{\Omega}$, and let $X = C^\infty(\overline{\Omega})$ (as in Proposition [[§30 Boundedness and Continuity#^prop-30-5|§30.5]]). For $1 \le p < \infty$ and an integer $k \ge 0$ define
>
> $$
> |f|_{W^{k,p}} = \sum_{|\alpha| \le k} \|\partial^\alpha f\|_{L^p(\Omega)}, \qquad \partial^\alpha f = \partial_{x_1}^{\alpha_1} \cdots \partial_{x_n}^{\alpha_n} f, \quad \alpha = (\alpha_1, \ldots, \alpha_n).
> $$
>
> *Lax: §5.1, example (g)*

^def-33-1

> [!proof]+ $|\cdot|_{W^{k,p}}$ is a norm
> (Left to the class in lecture.) Each term $f \mapsto \|\partial^\alpha f\|_{L^p}$ is non-negative, homogeneous, and subadditive, because $\partial^\alpha$ is linear and $\|\cdot\|_{L^p}$ is a norm ([[§19 The Function Spaces Lᵖ(Ω)#^thm-19-2|Minkowski]]); a finite sum of such functions has the same three properties. If $|f|_{W^{k,p}} = 0$, then in particular the term $\alpha = 0$ gives $\|f\|_{L^p} = 0$, so $f = 0$ a.e., and $f = 0$ everywhere because $f$ is continuous.

^pf-def-33-1

*Uses:* [[§11 Normed Linear Spaces#^def-11-1|Def. §11.1]], [[§19 The Function Spaces Lᵖ(Ω)#^def-19-1|Def. §19.1]], [[§19 The Function Spaces Lᵖ(Ω)#^thm-19-2|§19.2]]

> [!definition] Definition §33.2: Sobolev Space as a Completion
> The **Sobolev space** $W^{k,p}(\Omega)$ is the completion (Definition [[§12 Completeness#^def-12-4|§12.4]]) of $(X, |\cdot|_{W^{k,p}})$, with $X = C^\infty(\overline{\Omega})$ and the norm of Definition [[§33 Sobolev Spaces and Weak Derivatives#^def-33-1|§33.1]].
>
> *Lax: §5.1, example (g)*

^def-33-2

> [!remark]- Connections
> - The completion machinery behind it: [[§12 Completeness#^prop-12-3|§12.3]], [[§13 The Completion of a Normed Space#^thm-13-1|§13.1]]; the same construction with $L^p$ norms only, [[§19 The Function Spaces Lᵖ(Ω)#^prop-19-8|§19.8]]; a norm with one derivative on a space of smoother functions is again not complete, [[§13 The Completion of a Normed Space#^prop-13-5|§13.5]].

> [!remark] Remark
> Every $\partial^\alpha f$ of a $C^\infty$ function is again $C^\infty$, and bounded on the compact set $\overline{\Omega}$, so every term is finite. The case $p = \infty$ can be treated as well. The two claims, that this is a norm and that $X$ is not complete, were left to the class; the first is proved after Definition [[§33 Sobolev Spaces and Weak Derivatives#^def-33-1|§33.1]], and the example of [[§33 Sobolev Spaces and Weak Derivatives#Examples|§33]] shows how completeness fails.

^rem-33-1

> [!example] Example §33.1: $k = 0$: the Completion is $L^p$
> For $k = 0$ the norm is $\|f\|_{L^p}$. Since smooth functions are dense in $L^p(\Omega)$ (Theorem [[§19 The Function Spaces Lᵖ(Ω)#^thm-19-4|§19.4]]), the completion of $C^\infty(\overline{\Omega})$ in this norm is $L^p(\Omega)$ (Proposition [[§13 The Completion of a Normed Space#^prop-13-3|§13.3]]).

^ex-33-1

> [!remark]- Connections
> - Density in $L^p$ in measure theory, with $C_c$ in place of $C^\infty$: [[§35 Lᵖ as a Banach Space#^thm-35-12|551 §35.12]](iii).
> - The one-dimensional case done earlier in the course, $L^p[a,b]$ as the completion of $C[a,b]$: [[§19 The Function Spaces Lᵖ(Ω)#^prop-19-8|§19.8]].

> [!remark] Remark: What is in $W^{1,p}$?
> An element $f$ of the completion for $k = 1$ is the limit of a sequence $g_n \in C^\infty(\overline{\Omega})$ that is Cauchy in $|\cdot|_{W^{1,p}}$. That means $\{g_n\}$ is Cauchy in $L^p$, and so is each $\{\partial_{x_j} g_n\}$. Hence $g_n \to f$ in $L^p$ and $\partial_{x_j} g_n \to f_j$ in $L^p$ for some $f_j$. Heuristically $f_j$ should be “$\partial_{x_j} f$”, but $f$ is only an $L^p$ function and has no derivative in the classical sense; difference quotients of an $L^p$ function make no sense. The question is: *in what sense is $f_j = \partial_{x_j} f$?* The answer is integration by parts.

^rem-33-2

## Integration by Parts and Weak Derivatives

> [!definition] Definition §33.3: Support
> Let $\Omega \subset \mathbb{R}^n$ be open and $f : \Omega \to \mathbb{F}$ continuous. The **support** of $f$ is
>
> $$
> \operatorname{supp} f = \overline{\{ x \in \Omega : f(x) \neq 0 \}},
> $$
>
> the [[§11 Normed Linear Spaces#^def-11-7|closure]] in $\mathbb{R}^n$ of the set where $f$ is not zero.

^def-33-3

> [!definition] Definition §33.4: Compact Support
> A continuous $f : \Omega \to \mathbb{F}$ has **compact support in $\Omega$**, written $\operatorname{supp} f \subset\subset \Omega$, if $\operatorname{supp} f$ (Definition [[§33 Sobolev Spaces and Weak Derivatives#^def-33-3|§33.3]]) is a [[§20 Compactness and the Unit Ball#^def-20-4|compact]] ([[§6 Open Covers and the Heine–Borel Theorem#^thm-6-4|closed and bounded]]) subset of $\Omega$.

^def-33-4

> [!remark]- Connections
> - Support and compact support of a function on a subset of $\mathbb{R}^n$ in measure theory: [[§17 Simple Functions and Modes of Convergence#^def-17-2|551 Def. §17.2]]; on a manifold, [[§56 Vector Fields#^def-56-10|591 Def. §56.10]].

> [!definition] Definition §33.5: Test Functions
> Let $\Omega \subset \mathbb{R}^n$ be open. The **test functions** on $\Omega$ are the $C^\infty$ functions with compact support in $\Omega$ (Definition [[§33 Sobolev Spaces and Weak Derivatives#^def-33-4|§33.4]]),
>
> $$
> C_c^\infty(\Omega) = \{ f \in C^\infty(\Omega) : \operatorname{supp} f \subset\subset \Omega \}.
> $$

^def-33-5

> [!remark]- Connections
> - The same space on a manifold, with bump functions as examples: [[§56 Vector Fields#^def-56-11|591 Def. §56.11]], [[§56 Vector Fields#^def-56-12|591 Def. §56.12]].

> [!theorem] Proposition §33.1: Extension by Zero
> Let $f \in C_c^\infty(\Omega)$ and $K = \operatorname{supp} f$. If $\Omega \neq \mathbb{R}^n$, then $K$ has positive distance from $\mathbb{R}^n \setminus \Omega$. The function $\tilde f$ equal to $f$ on $\Omega$ and to $0$ on $\mathbb{R}^n \setminus \Omega$ lies in $C_c^\infty(\mathbb{R}^n)$.

^prop-33-1

> [!proof]+ Proof
> (Stated in lecture.) *Distance.* The function $d(x) = \operatorname{dist}(x, \mathbb{R}^n \setminus \Omega)$ is continuous (it is $1$-Lipschitz), and $d(x) > 0$ for $x \in K$ because $K \subset \Omega$ and $\Omega$ is [[§20 Compactness and the Unit Ball#^def-20-2|open]], so a [[§11 Normed Linear Spaces#^def-11-10|ball]] around $x$ lies in $\Omega$. A continuous function on the [[§20 Compactness and the Unit Ball#^def-20-4|compact]] set $K$ [[§18 Compact Spaces#^thm-18-3|attains its minimum]], so $\min_K d > 0$.
>
> *Smoothness.* The open sets $\Omega$ and $\mathbb{R}^n \setminus K$ cover $\mathbb{R}^n$, since $K \subset \Omega$. On $\Omega$, $\tilde f = f$ is $C^\infty$. On $\mathbb{R}^n \setminus K$, $\tilde f = 0$: $f$ vanishes on $\Omega \setminus K$ by [[§33 Sobolev Spaces and Weak Derivatives#^def-33-3|definition of the support]], and $\tilde f = 0$ outside $\Omega$. Being $C^\infty$ is a local property, so $\tilde f \in C^\infty(\mathbb{R}^n)$, and its support is $K$, which is compact.

^pf-33-1

*Uses:* [[§33 Sobolev Spaces and Weak Derivatives#^def-33-3|Def. §33.3]], [[§33 Sobolev Spaces and Weak Derivatives#^def-33-4|Def. §33.4]], [[§33 Sobolev Spaces and Weak Derivatives#^def-33-5|Def. §33.5]], [[§20 Compactness and the Unit Ball#^def-20-2|Def. §20.2]], [[§11 Normed Linear Spaces#^def-11-10|Def. §11.10]], [[§18 Compact Spaces#^thm-18-3|590 §18.3]]

![[m556-33-3.svg]]
*A test function lives strictly inside $\Omega$: its support stays a positive distance away from the boundary, so extending it by $0$ creates no corner and no jump.*

> [!theorem] Lemma §33.2: Integration by Parts against a Test Function
> Let $\Omega \subset \mathbb{R}^n$ be open, $g \in C^1(\Omega)$, and $\varphi \in C_c^\infty(\Omega)$ a test function (Definition [[§33 Sobolev Spaces and Weak Derivatives#^def-33-5|§33.5]]). Then for each $j$,
>
> $$
> \int_\Omega \partial_{x_j} g(x)\, \varphi(x)\, dx = -\int_\Omega g(x)\, \partial_{x_j} \varphi(x)\, dx .
> $$

^lem-33-2

> [!proof]+ Proof
> The argument is the [[§28 The Divergence Theorem in Higher Dimensions and Green's Identities#^thm-28-1|divergence theorem]], $\int_\Omega \operatorname{div} \vec{F}\, dx = \int_{\partial\Omega} \vec{F} \cdot \vec{n}\, dS$, applied to the vector field $\vec{F}$ whose only nonzero component is the $j$-th, $F_j = g\varphi$. Then $\operatorname{div}\vec F = \partial_{x_j}(g \varphi) = (\partial_{x_j} g)\varphi + g\, \partial_{x_j}\varphi$, and the boundary integral $\int_{\partial\Omega} n_j\, g \varphi\, dS$ vanishes because $\varphi = 0$ near $\partial\Omega$. In one dimension it is the usual [[§34 Fundamental Theorem of Calculus#^thm-34-3|integration by parts]] on an interval $[a, b]$ containing the support of $\varphi$: $\int_a^b g'\varphi = [g\varphi]_a^b - \int_a^b g \varphi' = -\int_a^b g\varphi'$, since $\varphi(a) = \varphi(b) = 0$.
>
> (The divergence theorem needs a smooth enough boundary; the identity itself does not. Extend $g\varphi$ and $g\,\partial_{x_j}\varphi$ by $0$ outside the support $K$ of $\varphi$; then $h = g\varphi$ is $C^1$ on $\mathbb{R}^n$ with compact support. By [[§25 Invariance Properties and Fubini's Theorem#^thm-25-6|Fubini]], integrate $\partial_{x_j} h$ first in $x_j$: for fixed other variables, $\int_{\mathbb{R}} \partial_{x_j} h\, dx_j = 0$ by the [[§34 Fundamental Theorem of Calculus#^thm-34-1|fundamental theorem of calculus]], since $h$ vanishes outside a bounded interval. So $\int \partial_{x_j}(g\varphi) = 0$, which is the identity by the product rule.)

^pf-33-2

*Uses:* [[§33 Sobolev Spaces and Weak Derivatives#^def-33-5|Def. §33.5]], [[§28 The Divergence Theorem in Higher Dimensions and Green's Identities#^thm-28-1|452 §28.1]], [[§34 Fundamental Theorem of Calculus#^thm-34-3|451 §34.3]], [[§25 Invariance Properties and Fubini's Theorem#^thm-25-6|551 §25.6]], [[§34 Fundamental Theorem of Calculus#^thm-34-1|451 §34.1]]

> [!remark]- Connections
> - Integration by parts in $\mathbb{R}^n$ with the boundary term kept: [[§28 The Divergence Theorem in Higher Dimensions and Green's Identities#^thm-28-2|Green's first identity, 452 §28.2]].

> [!theorem] Proposition §33.3: Limits in $W^{1,p}$ Satisfy Integration by Parts
> Let $\Omega \subset \mathbb{R}^n$ be bounded and open, and let $g_n \in C^\infty(\overline{\Omega})$ with $g_n \to f$ and $\partial_{x_j} g_n \to f_j$ in $L^p(\Omega)$, $1 \le p < \infty$. Then for every $\varphi \in C_c^\infty(\Omega)$,
>
> $$
> \int_\Omega f_j(x)\, \varphi(x)\, dx = -\int_\Omega f(x)\, \partial_{x_j}\varphi(x)\, dx .
> $$

^prop-33-3

> [!proof]+ Proof
> By Lemma [[§33 Sobolev Spaces and Weak Derivatives#^lem-33-2|§33.2]], $\int_\Omega \partial_{x_j} g_n\, \varphi = -\int_\Omega g_n\, \partial_{x_j}\varphi$ for every $n$. Let $n \to \infty$ on both sides. On the right, by Hölder's inequality (Theorem [[§19 The Function Spaces Lᵖ(Ω)#^thm-19-1|§19.1]]) with $\frac1p + \frac1{p'} = 1$,
>
> $$
> \Bigl| \int_\Omega (g_n - f)\, \partial_{x_j} \varphi\, dx \Bigr| \le \|g_n - f\|_{L^p}\, \|\partial_{x_j}\varphi\|_{L^{p'}} \to 0,
> $$
>
> since $\partial_{x_j}\varphi$ is continuous with compact support, hence in every $L^{p'}$. The same argument on the left, with $\partial_{x_j} g_n - f_j$ and $\varphi$, gives $\int \partial_{x_j} g_n\, \varphi \to \int f_j\, \varphi$.

^pf-33-3

*Uses:* [[§33 Sobolev Spaces and Weak Derivatives#^lem-33-2|§33.2]], [[§19 The Function Spaces Lᵖ(Ω)#^def-19-1|Def. §19.1]], [[§19 The Function Spaces Lᵖ(Ω)#^thm-19-1|§19.1]]

> [!remark] Remark: Hölder, not Dominated Convergence
> The question is which theorem justifies the limit. The [[§23 The Dominated Convergence Theorem#^thm-23-3|dominated convergence theorem]] needs pointwise a.e. convergence, and $g_n \to f$ in $L^p$ does not give that (only a subsequence converges a.e.). [[§19 The Function Spaces Lᵖ(Ω)#^thm-19-1|Hölder's inequality]] needs only convergence in $L^p$ and a fixed partner in $L^{p'}$, which the test function supplies.

^rem-33-3

> [!remark]- Connections
> - The subsequence statement: [[§35 Lᵖ as a Banach Space#^cor-35-10|551 §35.10]]; the measure-theoretic home of Hölder, [[§34 Normed Linear Spaces and Lᵖ Spaces#^thm-34-5|551 §34.5]].

> [!definition] Definition §33.6: Weak Derivative
> Let $\Omega \subset \mathbb{R}^n$ be open, $1 \le p \le \infty$, and $f \in L^p(\Omega)$. If there is $f_j \in L^p(\Omega)$ such that
>
> $$
> \int_\Omega f_j(x)\, \varphi(x)\, dx = -\int_\Omega f(x)\, \partial_{x_j}\varphi(x)\, dx \qquad \text{for all } \varphi \in C_c^\infty(\Omega),
> $$
>
> then $f_j$ is a **weak** (or **distributional**) **derivative** of $f$, written $f_j = \partial_{x_j} f$. More generally, $g = \partial^\alpha f$ weakly if $\int_\Omega g\, \varphi = (-1)^{|\alpha|} \int_\Omega f\, \partial^\alpha \varphi$ for all $\varphi \in C_c^\infty(\Omega)$.

^def-33-6

> [!remark] Remark
> A weak derivative need not exist; the definition only says what one is if it does. Both sides make sense whenever $f, f_j \in L^p$, because $\varphi$ and $\partial_{x_j}\varphi$ lie in every $L^{p'}$. The general $\alpha$ version, with the sign $(-1)^{|\alpha|}$ from integrating by parts $|\alpha|$ times, defines weak derivatives of second and higher order. By Proposition [[§33 Sobolev Spaces and Weak Derivatives#^prop-33-3|§33.3]], for every element $f$ of the completion $W^{1,p}$ the limits $f_j$ are weak derivatives of $f$.

^rem-33-4

> [!theorem] Lemma §33.4: Fundamental Lemma of the Calculus of Variations
> Let $\Omega \subset \mathbb{R}^n$ be open and let $h$ be a locally integrable function on $\Omega$, that is, a measurable function that is integrable on every compact subset of $\Omega$. If
>
> $$
> \int_\Omega h(x)\, \varphi(x)\, dx = 0 \qquad \text{for all } \varphi \in C_c^\infty(\Omega),
> $$
>
> then $h = 0$ a.e. on $\Omega$.

^lem-33-4

> [!proof]+ Proof (not given in this course)
> A result of real analysis: a locally integrable function that integrates to $0$ against every test function vanishes a.e. It is quoted here and used in Lemma [[§33 Sobolev Spaces and Weak Derivatives#^lem-33-5|§33.5]] and Corollary [[§33 Sobolev Spaces and Weak Derivatives#^cor-33-7|§33.7]].

^pf-33-4

> [!theorem] Lemma §33.5: Weak Derivatives are Unique
> Let $\Omega \subset \mathbb{R}^n$ be open, $1 \le p \le \infty$, and $f \in L^p(\Omega)$. If $f_j$ and $\tilde f_j$ are both weak derivatives of $f$ in the $x_j$-direction (Definition [[§33 Sobolev Spaces and Weak Derivatives#^def-33-6|§33.6]]), then $f_j = \tilde f_j$ a.e.

^lem-33-5

> [!proof]+ Proof
> (Not covered in lecture.) Subtracting the defining identities of $f_j$ and $\tilde f_j$, the function $h = f_j - \tilde f_j$ satisfies $\int_\Omega h\, \varphi = 0$ for all $\varphi \in C_c^\infty(\Omega)$. It lies in $L^p(\Omega)$, so it is locally integrable: on a compact set $K \subset \Omega$, Hölder's inequality (Theorem [[§19 The Function Spaces Lᵖ(Ω)#^thm-19-1|§19.1]]) applied to $h$ and the characteristic function $\chi_K$ gives $\int_K |h| \le \|h\|_{L^p}\, \|\chi_K\|_{L^{p'}} < \infty$, because $K$ has finite measure. By Lemma [[§33 Sobolev Spaces and Weak Derivatives#^lem-33-4|§33.4]], $h = 0$ a.e.

^pf-33-5

*Uses:* [[§33 Sobolev Spaces and Weak Derivatives#^def-33-6|Def. §33.6]], [[§19 The Function Spaces Lᵖ(Ω)#^thm-19-1|§19.1]], [[§33 Sobolev Spaces and Weak Derivatives#^lem-33-4|§33.4]]

> [!theorem] Lemma §33.6: Classical Derivatives are Weak Derivatives
> Let $\Omega \subset \mathbb{R}^n$ be open, $1 \le p \le \infty$, and $f \in L^p(\Omega)$. If $f \in C^1(\Omega)$ and its classical derivative $\partial_{x_j} f$ lies in $L^p(\Omega)$, then the classical derivative is the weak derivative of $f$ in the $x_j$-direction.

^lem-33-6

> [!proof]+ Proof
> (Not covered in lecture.) Lemma [[§33 Sobolev Spaces and Weak Derivatives#^lem-33-2|§33.2]] with $g = f$ gives $\int_\Omega \partial_{x_j} f\, \varphi\, dx = -\int_\Omega f\, \partial_{x_j}\varphi\, dx$ for every $\varphi \in C_c^\infty(\Omega)$. This is the defining identity of Definition [[§33 Sobolev Spaces and Weak Derivatives#^def-33-6|§33.6]] with $f_j = \partial_{x_j} f \in L^p(\Omega)$, so the classical derivative is a weak derivative of $f$; by Lemma [[§33 Sobolev Spaces and Weak Derivatives#^lem-33-5|§33.5]] it is the only one, up to a.e. equality.

^pf-33-6

*Uses:* [[§33 Sobolev Spaces and Weak Derivatives#^lem-33-2|§33.2]], [[§33 Sobolev Spaces and Weak Derivatives#^def-33-6|Def. §33.6]], [[§33 Sobolev Spaces and Weak Derivatives#^lem-33-5|§33.5]]

> [!remark] Remark: Weak and Pointwise Derivatives
> Does the weak derivative always match the pointwise derivative? Where $f$ is $C^1$ in a region, the weak derivative is the classical one there (Corollary [[§33 Sobolev Spaces and Weak Derivatives#^cor-33-7|§33.7]] below). Where $f$ has a singularity, there is no pointwise derivative to compare with, and a weak derivative is an element of $L^p$, defined only almost everywhere: it has no value at a single point.

^rem-33-5

> [!theorem] Corollary §33.7: Weak and Classical Derivatives Agree Where $f$ is Smooth
> Let $\Omega \subset \mathbb{R}^n$ be open, $f \in L^p(\Omega)$ with weak derivative $f_j$ in the $x_j$-direction (Definition [[§33 Sobolev Spaces and Weak Derivatives#^def-33-6|§33.6]]), and $U \subset \Omega$ open. If $f$ agrees a.e. on $U$ with a function $g \in C^1(U)$, then $f_j = \partial_{x_j} g$ a.e. on $U$.

^cor-33-7

> [!proof]+ Proof
> (The argument indicated in lecture, written out.) Let $\varphi \in C_c^\infty(U)$, and let $\tilde\varphi$ be $\varphi$ on $U$ and $0$ on $\Omega \setminus U$. Then $\tilde\varphi \in C_c^\infty(\Omega)$: its support $\operatorname{supp}\varphi$ is a compact subset of $U \subset \Omega$, and $\tilde\varphi$ is $C^\infty$ on each of the open sets $U$ and $\Omega \setminus \operatorname{supp}\varphi$, which cover $\Omega$ (as in the proof of Proposition [[§33 Sobolev Spaces and Weak Derivatives#^prop-33-1|§33.1]]). By the definition of the weak derivative, applied to $\tilde\varphi$, and since $\tilde\varphi$ and $\partial_{x_j}\tilde\varphi$ vanish outside $U$,
>
> $$
> \int_U f_j\, \varphi\, dx = -\int_U f\, \partial_{x_j}\varphi\, dx = -\int_U g\, \partial_{x_j}\varphi\, dx = \int_U \partial_{x_j} g\; \varphi\, dx ,
> $$
>
> the second equality because $f = g$ a.e. on $U$, the third by Lemma [[§33 Sobolev Spaces and Weak Derivatives#^lem-33-2|§33.2]] on the open set $U$. So $h = f_j - \partial_{x_j} g$ satisfies $\int_U h\, \varphi = 0$ for every $\varphi \in C_c^\infty(U)$. It is locally integrable on $U$ ($f_j \in L^p$, and $\partial_{x_j} g$ is continuous), so by Lemma [[§33 Sobolev Spaces and Weak Derivatives#^lem-33-4|§33.4]] on the open set $U$, $h = 0$ a.e. on $U$.

^pf-33-7

*Uses:* [[§33 Sobolev Spaces and Weak Derivatives#^prop-33-1|§33.1]], [[§33 Sobolev Spaces and Weak Derivatives#^lem-33-2|§33.2]], [[§33 Sobolev Spaces and Weak Derivatives#^lem-33-4|§33.4]]

> [!remark]- Connections
> - The fundamental lemma for continuous functions on an interval, with its proof by a bump: [[§B5.1 The Euler–Lagrange Equation#^thm-b5-1-2|CM Lemma §B5.1.2]].

> [!definition] Definition §33.7: Sobolev Space via Weak Derivatives
> For $\Omega \subset \mathbb{R}^n$ open, an integer $k \ge 0$ and $1 \le p \le \infty$,
>
> $$
> W^{k,p}(\Omega) = \bigl\{ f \in L^p(\Omega) : \text{the weak derivatives } \partial^\alpha f \text{ exist and lie in } L^p(\Omega) \text{ for all } |\alpha| \le k \bigr\}.
> $$

^def-33-7

> [!remark] Remark
> Both descriptions of $W^{k,p}$ are used: the completion of Definition [[§33 Sobolev Spaces and Weak Derivatives#^def-33-2|§33.2]], and the weak-derivative space above. For $k = 1$ the completion sits inside the weak-derivative space (Corollary [[§33 Sobolev Spaces and Weak Derivatives#^cor-33-8|§33.8]] below). That the two coincide for reasonable $\Omega$ (every function with weak derivatives in $L^p$ is a $W^{k,p}$-limit of smooth functions) is the Meyers–Serrin theorem, which was not covered.

^rem-33-6

> [!theorem] Corollary §33.8: The Completion Sits Inside the Weak-Derivative Space
> Let $\Omega \subset \mathbb{R}^n$ be bounded and open with closure $\overline{\Omega}$, $1 \le p < \infty$, and let $\{g_n\} \subset C^\infty(\overline{\Omega})$ be Cauchy in $|\cdot|_{W^{1,p}}$ (Definition [[§33 Sobolev Spaces and Weak Derivatives#^def-33-1|§33.1]]). Then:
>
> 1. there are $f \in L^p(\Omega)$ and, for each $j$, $f_j \in L^p(\Omega)$ with $g_n \to f$ and $\partial_{x_j} g_n \to f_j$ in $L^p(\Omega)$;
> 2. $f_j$ is the weak derivative $\partial_{x_j} f$, so $f \in W^{1,p}(\Omega)$ in the sense of Definition [[§33 Sobolev Spaces and Weak Derivatives#^def-33-7|§33.7]];
> 3. $f$ and the $f_j$ depend only on the element of the completion represented by $\{g_n\}$;
> 4. conversely, that element is determined by $f$: if $f = 0$, then every $f_j = 0$ a.e. and $|g_n|_{W^{1,p}} \to 0$.

^cor-33-8

> [!proof]+ Proof
> (Details filled in.) (1) *The limits exist.* $\|g_n - g_m\|_{L^p} \le |g_n - g_m|_{W^{1,p}}$ and $\|\partial_{x_j} g_n - \partial_{x_j} g_m\|_{L^p} \le |g_n - g_m|_{W^{1,p}}$, since these are terms of the sum defining the norm. So $\{g_n\}$ and each $\{\partial_{x_j} g_n\}$ are Cauchy in $L^p(\Omega)$, which is complete (Theorem [[§19 The Function Spaces Lᵖ(Ω)#^thm-19-3|§19.3]]); call the limits $f$ and $f_j$.
>
> (2) *Weak derivatives.* By Proposition [[§33 Sobolev Spaces and Weak Derivatives#^prop-33-3|§33.3]], $\int_\Omega f_j \varphi = -\int_\Omega f\, \partial_{x_j}\varphi$ for every $\varphi \in C_c^\infty(\Omega)$; by Definition [[§33 Sobolev Spaces and Weak Derivatives#^def-33-6|§33.6]], $f_j$ is the weak derivative of $f$ in the $x_j$-direction. Since $f$ and all $f_j$ lie in $L^p(\Omega)$, $f \in W^{1,p}(\Omega)$ (Definition [[§33 Sobolev Spaces and Weak Derivatives#^def-33-7|§33.7]] with $k = 1$).
>
> (3) *Independence of the representative.* If $\{h_n\}$ is an equivalent Cauchy sequence, $|g_n - h_n|_{W^{1,p}} \to 0$, then $\|g_n - h_n\|_{L^p} \to 0$ and $\|\partial_{x_j} g_n - \partial_{x_j} h_n\|_{L^p} \to 0$, so $\{h_n\}$ and $\{\partial_{x_j} h_n\}$ have the same $L^p$ limits $f$ and $f_j$.
>
> (4) *The element is determined by $f$.* Let $f = 0$. By (2), each $f_j$ is a weak derivative of the zero function in the $x_j$-direction, and so is the zero function, since both sides of the defining identity then vanish. By Lemma [[§33 Sobolev Spaces and Weak Derivatives#^lem-33-5|§33.5]], $f_j = 0$ a.e. Hence $\|g_n\|_{L^p} \to 0$ and $\|\partial_{x_j} g_n\|_{L^p} \to 0$ for each $j$, so $|g_n|_{W^{1,p}} \to 0$: the sequence $\{g_n\}$ represents the zero element of the completion. By linearity, two elements of the completion with the same limit $f$ are equal, so the completion is identified with a linear subspace of $L^p(\Omega)$.

^pf-33-8

*Uses:* [[§19 The Function Spaces Lᵖ(Ω)#^thm-19-3|§19.3]], [[§33 Sobolev Spaces and Weak Derivatives#^prop-33-3|§33.3]], [[§33 Sobolev Spaces and Weak Derivatives#^def-33-6|Def. §33.6]], [[§33 Sobolev Spaces and Weak Derivatives#^def-33-7|Def. §33.7]], [[§33 Sobolev Spaces and Weak Derivatives#^lem-33-5|§33.5]]

> [!remark]- Connections
> - The continuum limit of the multipole-lattice model takes its configurations in $W^{1,2}$: unit-vector fields whose components have square-integrable weak first derivatives on every ball ([[§M7.1 Configurations as Maps; Potential and Stiffness; When the Continuum Limit is Well Posed#^def-m7-1-5|Thesis Def. §M7.1.5]]).
> - In one dimension and with positive stiffness, the gradient energy of such a field attains its minimum on this space, by the direct method ([[§M7.1 Configurations as Maps; Potential and Stiffness; When the Continuum Limit is Well Posed#^thm-m7-1-4|Thesis Thm. §M7.1.4]]).

## Examples

> [!example] Example §33.2: $|x|$ has Weak Derivative $\operatorname{sgn} x$
> Let $f(x) = |x|$ on $\mathbb{R}$. Then $f$ has the weak derivative
>
> $$
> g(x) = \begin{cases} 1, & x > 0, \\ -1, & x < 0, \end{cases}
> $$
>
> in the sense that $\int f\varphi' = -\int g\varphi$ for every $\varphi \in C_c^\infty(\mathbb{R})$; the value of $g$ at $0$ is irrelevant. In particular $|x| \in W^{1,p}(-1, 1)$ for every $p$.

^ex-33-2

> [!proof]+ Proof
> Split at $0$ and integrate by parts on each half-line:
>
> $$
> \begin{aligned}
> \int_{-\infty}^{\infty} |x|\, \varphi'(x)\, dx &= \int_0^\infty x\, \varphi'(x)\, dx + \int_{-\infty}^0 (-x)\, \varphi'(x)\, dx \\
> &= \bigl[ x\varphi(x) \bigr]_0^\infty - \int_0^\infty \varphi(x)\, dx - \bigl[ x\varphi(x) \bigr]_{-\infty}^0 + \int_{-\infty}^0 \varphi(x)\, dx \\
> &= -\int_0^\infty \varphi(x)\, dx + \int_{-\infty}^0 \varphi(x)\, dx = -\int_{-\infty}^\infty g(x)\, \varphi(x)\, dx .
> \end{aligned}
> $$
>
> The boundary terms vanish: at $0$ because $x\varphi(x) = 0$ there, and at $\pm\infty$ because $\varphi$ has compact support. Changing $g$ on the null set $\{0\}$ does not change any integral.

^pf-ex-33-2

*Uses:* [[§33 Sobolev Spaces and Weak Derivatives#^def-33-6|Def. §33.6]], [[§33 Sobolev Spaces and Weak Derivatives#^def-33-7|Def. §33.7]], [[§34 Fundamental Theorem of Calculus#^thm-34-3|451 §34.3]]

> [!example] Example §33.3: $\operatorname{sgn} x$ has No Weak Derivative
> Let $f(x) = 1$ for $x > 0$ and $f(x) = -1$ for $x < 0$. Then $\int f\varphi' = -2\varphi(0)$ for every $\varphi \in C_c^\infty(\mathbb{R})$, and there is no locally integrable $g$ with $\int f\varphi' = -\int g\varphi$ for all $\varphi$. So $f$ has no weak derivative, in any $L^p$.

^ex-33-3

> [!proof]+ Proof
> $\int_{-\infty}^\infty f\varphi' = \int_0^\infty \varphi' - \int_{-\infty}^0 \varphi' = \bigl[\varphi\bigr]_0^\infty - \bigl[\varphi\bigr]_{-\infty}^0 = -\varphi(0) - \varphi(0) = -2\varphi(0)$.
>
> (The non-existence was left to the class.) Suppose $g$ is locally integrable with $\int g\varphi = 2\varphi(0)$ for all test functions $\varphi$. Let $\psi(x) = e^{1 - 1/(1 - x^2)}$ for $|x| < 1$ and $\psi(x) = 0$ otherwise; this is a standard $C_c^\infty$ function with $0 \le \psi \le 1$ and $\psi(0) = 1$. For $0 < \varepsilon \le 1$ let $\varphi_\varepsilon(x) = \psi(x/\varepsilon)$, supported in $[-\varepsilon, \varepsilon]$ with $\varphi_\varepsilon(0) = 1$. Then
>
> $$
> 2 = 2\varphi_\varepsilon(0) = \int g\, \varphi_\varepsilon \le \int_{-\varepsilon}^{\varepsilon} |g(x)|\, dx \xrightarrow[\varepsilon \to 0]{} 0,
> $$
>
> the limit by the [[§23 The Dominated Convergence Theorem#^thm-23-3|dominated convergence theorem]] applied to $|g|\chi_{[-\varepsilon, \varepsilon]} \le |g|\chi_{[-1,1]} \in L^1$. This is a contradiction.

^pf-ex-33-3

*Uses:* [[§33 Sobolev Spaces and Weak Derivatives#^def-33-5|Def. §33.5]], [[§33 Sobolev Spaces and Weak Derivatives#^def-33-6|Def. §33.6]], [[§34 Fundamental Theorem of Calculus#^thm-34-1|451 §34.1]], [[§23 The Dominated Convergence Theorem#^thm-23-3|551 §23.3]]

> [!remark]- Connections
> - The flat function $e^{-1/x^2}$ behind $\psi$, smooth with every derivative $0$ at the origin: [[§31 Taylor's Theorem#^ex-31-3|451 Ex. §31.3]]; bump functions on manifolds, [[§56 Vector Fields#^cor-56-7|591 §56.7]].

![[m556-33-1.svg]]
*The board pictures. A corner is harmless: $|x|$ has the bounded weak derivative $\operatorname{sgn} x$. A jump is not: the “derivative” of $\operatorname{sgn} x$ is concentrated at a single point with total mass $2$, which no function can do.*

![[m556-33-a1.gif|480]]

*(Not from lecture; animation added, vault only.)* $|x|$ and $\mathrm{sgn}\,x$ smoothed at scale $\varepsilon$ (as $\sqrt{x^2 + \varepsilon^2}$ and $\tanh(x/\varepsilon)$, chosen for the picture), with their derivatives, for $\varepsilon$ from $0.5$ down to $0.05$ and back. Left: the derivatives tend to $\mathrm{sgn}\,x$ and stay bounded by $1$. Right: the derivatives are spikes of area $2$ and height $1/\varepsilon$, concentrating at $0$, so no function in $L^1_{\mathrm{loc}}$ can be the weak derivative.

> [!remark] Remark: Distributions
> What $\operatorname{sgn} x$ does have is a *distributional* derivative, $f' = 2\delta_0$, twice the delta “function” — zero away from the origin, with $\int (2\delta_0)\varphi = 2\varphi(0)$. A distribution is a linear functional on the test functions $C_c^\infty$, continuous in a suitable sense; $\delta_0(\varphi) = \varphi(0)$ is one, and every $L^p$ function defines one by $\varphi \mapsto \int f\varphi$. In this language every $L^p$ function has a distributional derivative, and a weak derivative is a distributional derivative that happens to be an $L^p$ function. Distributions are to come later in the course. (The name has nothing to do with probability distributions.)

^rem-33-7

> [!remark]- Connections
> - Distributions and their derivatives in Quantum Field Theory: [[§CA.2 Generalized Functions#^def-ca-2-2|QFT Def. §CA.2.2]], [[§CA.2 Generalized Functions#^def-ca-2-4|QFT Def. §CA.2.4]]; the step function has derivative $\delta$, the same computation as Example [[§33 Sobolev Spaces and Weak Derivatives#^ex-33-3|§33.3]] — [[§CA.2 Generalized Functions#^thm-ca-2-4|QFT Theorem §CA.2.4]].

## The Space $H^1_0$ and the Poincaré Inequality

> [!definition] Definition §33.8: The $W^{1,2}$ Norm on Test Functions
> Let $\Omega \subset \mathbb{R}^n$ be bounded and open. On $C_c^\infty(\Omega)$ put
>
> $$
> \|f\|_{W^{1,2}(\Omega)} = \Bigl( \|f\|_{L^2(\Omega)}^2 + \|\nabla f\|_{L^2(\Omega)}^2 \Bigr)^{1/2}, \qquad \|\nabla f\|_{L^2}^2 = \sum_{j=1}^n \|\partial_{x_j} f\|_{L^2}^2 .
> $$

^def-33-8

> [!definition] Definition §33.9: The Space $H^1_0(\Omega)$
> Let $\Omega \subset \mathbb{R}^n$ be bounded and open. $H^1_0(\Omega)$ is the completion of $C_c^\infty(\Omega)$ in the norm $\|\cdot\|_{W^{1,2}(\Omega)}$ of Definition [[§33 Sobolev Spaces and Weak Derivatives#^def-33-8|§33.8]].

^def-33-9

> [!theorem] Proposition §33.9: $H^1_0(\Omega)$ is a Hilbert Space
> - (a) The norm of Definition [[§33 Sobolev Spaces and Weak Derivatives#^def-33-8|§33.8]] is equivalent to the summed norm $\|f\|_{L^2} + \sum_j \|\partial_{x_j} f\|_{L^2}$ of Definition [[§33 Sobolev Spaces and Weak Derivatives#^def-33-1|§33.1]].
> - (b) $H^1_0(\Omega)$ is a Hilbert space.

^prop-33-9

> [!proof]+ Proof
> (Stated in lecture; (b) was left to the class.) (a) For non-negative numbers $t_0, \ldots, t_n$, $\bigl(\sum t_i^2\bigr)^{1/2} \le \sum t_i \le \sqrt{n+1}\,\bigl(\sum t_i^2\bigr)^{1/2}$: the first because $\bigl(\sum t_i\bigr)^2 \ge \sum t_i^2$, the second by [[§16 Means and Young's Inequality#^prop-16-1|Cauchy–Schwarz]] in $\mathbb{R}^{n+1}$ applied to $(t_i)$ and $(1, \ldots, 1)$. Apply this with $t_0 = \|f\|_{L^2}$, $t_j = \|\partial_{x_j} f\|_{L^2}$.
>
> (b) On $C_c^\infty(\Omega)$ the norm comes from the inner product $(f, g) = \int_\Omega f\bar g + \sum_j \int_\Omega \partial_{x_j} f\, \overline{\partial_{x_j} g}$ (the case $k = 1$ of Example [[§23 Cauchy–Schwarz and the Induced Norm#^ex-23-3|§23.3]]), so it satisfies the [[§24 The Parallelogram Law and Jordan–von Neumann#^prop-24-1|parallelogram law]]. The completion is a Banach space (Theorem [[§13 The Completion of a Normed Space#^thm-13-1|§13.1]]), and its norm is the limit of norms of representatives: $\|[\{f_n\}]\| = \lim_n \|f_n\|$. For $x = [\{f_n\}]$, $y = [\{g_n\}]$, the parallelogram law $\|f_n + g_n\|^2 + \|f_n - g_n\|^2 = 2\|f_n\|^2 + 2\|g_n\|^2$ holds for each $n$ and passes to the limit, so it holds in the completion. By the Jordan–von Neumann theorem (Theorem [[§24 The Parallelogram Law and Jordan–von Neumann#^thm-24-2|§24.2]]) the norm of the completion comes from an inner product; being complete, $H^1_0(\Omega)$ is a Hilbert space.

^pf-33-9

*Uses:* [[§16 Means and Young's Inequality#^prop-16-1|§16.1]], [[§14 New Normed Spaces from Old#^def-14-1|Def. §14.1]], [[§23 Cauchy–Schwarz and the Induced Norm#^ex-23-3|Ex. §23.3]], [[§24 The Parallelogram Law and Jordan–von Neumann#^prop-24-1|§24.1]], [[§13 The Completion of a Normed Space#^thm-13-1|§13.1]], [[§24 The Parallelogram Law and Jordan–von Neumann#^thm-24-2|§24.2]], [[§23 Cauchy–Schwarz and the Induced Norm#^def-23-1|Def. §23.1]]

> [!theorem] Proposition §33.10: Elements of $H^1_0(\Omega)$ are Functions
> Let $\Omega \subset \mathbb{R}^n$ be bounded and open, and let an element of $H^1_0(\Omega)$ be represented by a sequence $\{g_n\} \subset C_c^\infty(\Omega)$ that is Cauchy in the norm $\|\cdot\|_{W^{1,2}(\Omega)}$ (Definition [[§33 Sobolev Spaces and Weak Derivatives#^def-33-9|§33.9]]). Then:
>
> 1. there are $f \in L^2(\Omega)$ and $f_j \in L^2(\Omega)$, $j = 1, \ldots, n$, with $g_n \to f$ and $\partial_{x_j} g_n \to f_j$ in $L^2(\Omega)$, and they depend only on the element, not on the sequence representing it;
> 2. $f_j$ is the weak derivative $\partial_{x_j} f$ (Definition [[§33 Sobolev Spaces and Weak Derivatives#^def-33-6|§33.6]]);
> 3. the element is determined by $f$: two elements of $H^1_0(\Omega)$ with the same $f$ are equal;
> 4. the norm of the element in $H^1_0(\Omega)$ is $\bigl( \|f\|_{L^2}^2 + \sum_{j=1}^n \|\partial_{x_j} f\|_{L^2}^2 \bigr)^{1/2}$.
>
> Accordingly an element of $H^1_0(\Omega)$ is identified with its function $f$: $H^1_0(\Omega)$ is a linear subspace of $L^2(\Omega)$ whose elements have weak first derivatives in $L^2(\Omega)$, and $\nabla f = (\partial_{x_1} f, \ldots, \partial_{x_n} f)$ denotes the weak gradient.
>
> *Lax: §7.2, Lemma 2 and the paragraph after its proof*

^prop-33-10

> [!proof]+ Proof
> *(Not from lecture; filled in.)* *Reduction to Corollary [[§33 Sobolev Spaces and Weak Derivatives#^cor-33-8|§33.8]].* Every $g \in C_c^\infty(\Omega)$ lies in $C^\infty(\overline{\Omega})$: by Proposition [[§33 Sobolev Spaces and Weak Derivatives#^prop-33-1|§33.1]] its extension by zero is $C^\infty$ on $\mathbb{R}^n$, so every partial derivative of $g$ is the restriction to $\Omega$ of a continuous function on $\mathbb{R}^n$ and extends continuously to $\overline{\Omega}$. By the inequalities in the proof of Proposition [[§33 Sobolev Spaces and Weak Derivatives#^prop-33-9|§33.9]](a),
>
> $$
> \|g\|_{W^{1,2}(\Omega)} \le |g|_{W^{1,2}} \le \sqrt{n+1}\; \|g\|_{W^{1,2}(\Omega)} \qquad \text{for all } g \in C_c^\infty(\Omega),
> $$
>
> where $|g|_{W^{1,2}} = \|g\|_{L^2} + \sum_j \|\partial_{x_j} g\|_{L^2}$ is the norm of Definition [[§33 Sobolev Spaces and Weak Derivatives#^def-33-1|§33.1]] with $k = 1$, $p = 2$. So a sequence in $C_c^\infty(\Omega)$ is Cauchy, or tends to $0$, in one of the two norms if and only if it does in the other.
>
> (1) and (2). The sequence $\{g_n\}$ is Cauchy in $|\cdot|_{W^{1,2}}$, so parts (1) and (2) of Corollary [[§33 Sobolev Spaces and Weak Derivatives#^cor-33-8|§33.8]] with $p = 2$ give $f$ and the $f_j$, with $f_j$ the weak derivative $\partial_{x_j} f$. If $\{h_n\} \subset C_c^\infty(\Omega)$ represents the same element of $H^1_0(\Omega)$, then $\|g_n - h_n\|_{W^{1,2}(\Omega)} \to 0$, hence $|g_n - h_n|_{W^{1,2}} \to 0$, and part (3) of the corollary shows that $\{h_n\}$ gives the same $f$ and $f_j$.
>
> (3) Let two elements, represented by $\{g_n\}$ and $\{h_n\}$, have the same $f$. Then $\{g_n - h_n\} \subset C_c^\infty(\Omega)$ is Cauchy in $|\cdot|_{W^{1,2}}$ and converges to $f - f = 0$ in $L^2(\Omega)$. By part (4) of Corollary [[§33 Sobolev Spaces and Weak Derivatives#^cor-33-8|§33.8]], $|g_n - h_n|_{W^{1,2}} \to 0$, hence $\|g_n - h_n\|_{W^{1,2}(\Omega)} \to 0$: the two sequences represent the same element.
>
> (4) The norm of the element is $\lim_n \|g_n\|_{W^{1,2}(\Omega)}$ (Theorem [[§13 The Completion of a Normed Space#^thm-13-1|§13.1]]). Since $g_n \to f$ and $\partial_{x_j} g_n \to \partial_{x_j} f$ in $L^2(\Omega)$, Proposition [[§11 Normed Linear Spaces#^prop-11-4|§11.4]] gives $\|g_n\|_{L^2} \to \|f\|_{L^2}$ and $\|\partial_{x_j} g_n\|_{L^2} \to \|\partial_{x_j} f\|_{L^2}$. Hence
>
> $$
> \lim_{n \to \infty} \|g_n\|_{W^{1,2}(\Omega)} = \lim_{n \to \infty} \Bigl( \|g_n\|_{L^2}^2 + \sum_{j=1}^n \|\partial_{x_j} g_n\|_{L^2}^2 \Bigr)^{1/2} = \Bigl( \|f\|_{L^2}^2 + \sum_{j=1}^n \|\partial_{x_j} f\|_{L^2}^2 \Bigr)^{1/2} .
> $$
>
> The map sending an element to its $f$ is linear, because limits in $L^2(\Omega)$ are linear, and one-to-one by (3); this is the identification with a linear subspace of $L^2(\Omega)$.

^pf-33-10

*Uses:* [[§33 Sobolev Spaces and Weak Derivatives#^cor-33-8|§33.8]], [[§33 Sobolev Spaces and Weak Derivatives#^prop-33-1|§33.1]], [[§33 Sobolev Spaces and Weak Derivatives#^prop-33-9|§33.9]], [[§33 Sobolev Spaces and Weak Derivatives#^def-33-1|Def. §33.1]], [[§13 The Completion of a Normed Space#^thm-13-1|§13.1]], [[§11 Normed Linear Spaces#^prop-11-4|§11.4]]

> [!remark] Remark
> Every element of $H^1_0(\Omega)$ is a limit of functions that vanish near the boundary, so it is zero on the boundary in some sense — this is what distinguishes $H^1_0$ from the completion of $C^\infty(\overline\Omega)$, and it is the boundary condition of a Dirichlet problem built into the space. Making “zero on the boundary” precise (trace theorems) was not covered.

^rem-33-8

> [!theorem] Theorem §33.11: Poincaré Inequality
> Let $\Omega \subset \mathbb{R}^n$ be bounded and open. There is a constant $C > 0$, depending only on $\Omega$, such that
>
> $$
> \int_\Omega |f(x)|^2\, dx \le C^2 \int_\Omega |\nabla f(x)|^2\, dx \qquad \text{for all } f \in C_c^\infty(\Omega).
> $$
>
> One can take $C = 2L$ for any $L$ with $\Omega \subset (-L, L)^n$.
>
> *Lax: §7.2, Lemma 1 (Zaremba's inequality, with the width of the domain as the constant)*

^thm-33-11

> [!proof]+ Proof
> **Step 1: put $\Omega$ in a box and extend by zero.** Since $\Omega$ is bounded, $\Omega \subset (-L, L)^n$ for some $L > 0$. Extend $f$ by $f(x) = 0$ for $x \notin \Omega$; by Proposition [[§33 Sobolev Spaces and Weak Derivatives#^prop-33-1|§33.1]] the extension is $C^\infty$ on $\mathbb{R}^n$, and it vanishes outside $\Omega$, in particular on the face $x_1 = -L$ of the box.
>
> **Step 2: the [[§34 Fundamental Theorem of Calculus#^thm-34-1|fundamental theorem of calculus]] in $x_1$.** For $x = (x_1, x') \in [-L, L]^n$, $x' = (x_2, \ldots, x_n)$,
>
> $$
> f(x_1, x') = f(-L, x') + \int_{-L}^{x_1} \partial_{x_1} f(y_1, x')\, dy_1 = \int_{-L}^{x_1} \partial_{x_1} f(y_1, x')\, dy_1 ,
> $$
>
> since $f(-L, x') = 0$. Because $x_1 \le L$,
>
> $$
> |f(x_1, x')| \le \int_{-L}^{L} |\partial_{x_1} f(y_1, x')|\, dy_1 \le \Bigl( \int_{-L}^{L} |\partial_{x_1} f(y_1, x')|^2\, dy_1 \Bigr)^{1/2} \Bigl( \int_{-L}^{L} 1\, dy_1 \Bigr)^{1/2},
> $$
>
> by [[§19 The Function Spaces Lᵖ(Ω)#^thm-19-1|Hölder]] (Cauchy–Schwarz) with $p = p' = 2$. Squaring,
>
> $$
> |f(x_1, x')|^2 \le 2L \int_{-L}^{L} |\partial_{x_1} f(y_1, x')|^2\, dy_1 \qquad \text{for all } x_1 \in [-L, L].
> $$
>
> **Step 3: integrate over the box.** Integrate both sides over $x \in [-L, L]^n$. The right side does not depend on $x_1$, so integrating in $x_1$ multiplies it by $2L$; the remaining integrals in $x'$ combine with the $y_1$-integral into an integral over the box ([[§25 Invariance Properties and Fubini's Theorem#^thm-25-6|Fubini]]):
>
> $$
> \int_{[-L,L]^n} |f(x)|^2\, dx \le (2L) \cdot 2L \int_{[-L,L]^n} |\partial_{x_1} f(x)|^2\, dx .
> $$
>
> Since $f = 0$ outside $\Omega$ and $|\partial_{x_1} f|^2 \le |\nabla f|^2$,
>
> $$
> \int_\Omega |f(x)|^2\, dx \le (2L)^2 \int_\Omega |\nabla f(x)|^2\, dx .
> $$

^pf-33-11

*Uses:* [[§33 Sobolev Spaces and Weak Derivatives#^def-33-5|Def. §33.5]], [[§33 Sobolev Spaces and Weak Derivatives#^prop-33-1|§33.1]], [[§34 Fundamental Theorem of Calculus#^thm-34-1|451 §34.1]], [[§19 The Function Spaces Lᵖ(Ω)#^thm-19-1|§19.1]], [[§25 Invariance Properties and Fubini's Theorem#^thm-25-6|551 §25.6]]

![[m556-33-2.svg]]
*The proof in one picture: $f$ vanishes on the left face of the box, so its value at $x$ is the integral of $\partial_{x_1} f$ along the horizontal segment that reaches $x$, and Cauchy–Schwarz turns the length $2L$ of that segment into the constant. The constant depends only on the width of $\Omega$ in one direction. The principle: a function that is zero somewhere can be controlled by its gradient.*

> [!theorem] Corollary §33.12: Poincaré on $H^1_0$
> The Poincaré inequality $\|f\|_{L^2(\Omega)} \le C\, \|\nabla f\|_{L^2(\Omega)}$ holds for all $f \in H^1_0(\Omega)$.

^cor-33-12

> [!proof]+ Proof
> (Lecture 12.) By Theorem [[§33 Sobolev Spaces and Weak Derivatives#^thm-33-11|§33.11]] the inequality holds for every function in $C_c^\infty(\Omega)$; it remains to pass to limits. Let $f \in H^1_0(\Omega)$. By [[§33 Sobolev Spaces and Weak Derivatives#^def-33-9|definition of the completion]] there are $g_n \in C_c^\infty(\Omega)$ with
>
> $$
> g_n \to f \quad \text{and} \quad \partial_{x_j} g_n \to \partial_{x_j} f \quad \text{in } L^2(\Omega), \qquad j = 1, \ldots, n,
> $$
>
> where, as in Proposition [[§33 Sobolev Spaces and Weak Derivatives#^prop-33-3|§33.3]], $f$ is the $L^2$ limit of a [[§11 Normed Linear Spaces#^def-11-5|Cauchy sequence]] and $\partial_{x_j} f$, the $L^2$ limit of $\partial_{x_j} g_n$, is the [[§33 Sobolev Spaces and Weak Derivatives#^def-33-6|weak derivative]] of $f$. For each $n$, Theorem [[§33 Sobolev Spaces and Weak Derivatives#^thm-33-11|§33.11]] gives
>
> $$
> \int_\Omega |g_n(x)|^2\, dx \le C^2 \sum_{j=1}^n \int_\Omega |\partial_{x_j} g_n(x)|^2\, dx .
> $$
>
> By the reverse triangle inequality (Lemma [[§11 Normed Linear Spaces#^lem-11-3|§11.3]]), $\bigl| \|g_n\|_{L^2} - \|f\|_{L^2} \bigr| \le \|g_n - f\|_{L^2} \to 0$, so $\|g_n\|_{L^2} \to \|f\|_{L^2}$, and likewise $\|\partial_{x_j} g_n\|_{L^2} \to \|\partial_{x_j} f\|_{L^2}$ for each $j$. Squares and finite sums of convergent sequences converge, and limits preserve non-strict inequalities, so
>
> $$
> \int_\Omega |f(x)|^2\, dx \le C^2 \sum_{j=1}^n \int_\Omega |\partial_{x_j} f(x)|^2\, dx = C^2 \int_\Omega |\nabla f(x)|^2\, dx .
> $$

^pf-33-12

*Uses:* [[§33 Sobolev Spaces and Weak Derivatives#^thm-33-11|§33.11]], [[§33 Sobolev Spaces and Weak Derivatives#^def-33-9|Def. §33.9]], [[§33 Sobolev Spaces and Weak Derivatives#^prop-33-3|§33.3]], [[§33 Sobolev Spaces and Weak Derivatives#^def-33-6|Def. §33.6]], [[§11 Normed Linear Spaces#^lem-11-3|§11.3]], [[§9 Limit Theorems for Sequences#^prop-9-5|451 §9.5]]

> [!remark] Remark: Triangle Inequality, Not Inner Product
> The fact $\|g_n\|_{L^2} \to \|f\|_{L^2}$ follows from continuity of the inner product (Lemma [[§25 Projection and Orthogonal Decomposition#^lem-25-1|§25.1]]), since $L^2$ is an [[§22 Definition and Examples#^def-22-1|inner product space]]; but it is more general: in any [[§11 Normed Linear Spaces#^def-11-1|normed space]] $x_n \to x$ implies $\|x_n\| \to \|x\|$, by the reverse triangle inequality (Proposition [[§11 Normed Linear Spaces#^prop-11-4|§11.4]]). The whole argument is a standard technique: to prove an inequality on a space, prove it on a [[§11 Normed Linear Spaces#^def-11-8|dense subset]], then take limits ([[Functional Analysis Problem-Solving Techniques#^rem-t19|Technique 19]]).

^rem-33-9

> [!remark] Remark: What “Zero on the Boundary” Means
> One may think of $f \in H^1_0(\Omega)$ as $C_c^\infty$ in spirit, equal to $0$ on $\partial\Omega$ in an appropriate sense; making this precise needs much more of Sobolev space theory and is outside the course. Why only in an appropriate sense: for $f \in L^2$ alone, boundary values mean nothing, since $\partial\Omega$ has measure zero and an $L^2$ function can be changed there at will. What makes the boundary condition meaningful is that $\nabla f \in L^2$ as well. A function that stays away from $0$ up to $\partial\Omega$ and is $0$ outside has a jump at the boundary, and a jump has no $L^2$ derivative — its derivative is a [[§33 Sobolev Spaces and Weak Derivatives#^rem-33-7|delta]] (Example [[§33 Sobolev Spaces and Weak Derivatives#^ex-33-3|§33.3]]).
>
> Precisely: the extension $\tilde f$ of $f$ by zero has [[§33 Sobolev Spaces and Weak Derivatives#^def-33-6|weak derivatives]] in $L^2(\mathbb{R}^n)$, namely the extensions of $\partial_{x_j} f$ (Proposition [[§33 Sobolev Spaces and Weak Derivatives#^prop-33-13|§33.13]] below). In one dimension, $\tilde f$ therefore cannot jump at an endpoint of $\Omega$.

^rem-33-10

> [!theorem] Proposition §33.13: Extension by Zero of an $H^1_0$ Function
> Let $\Omega \subset \mathbb{R}^n$ be bounded and open and $f \in H^1_0(\Omega)$, with weak derivatives $\partial_{x_j} f \in L^2(\Omega)$ (the $L^2$ limits of $\partial_{x_j} g_n$ for $g_n \in C_c^\infty(\Omega)$ converging to $f$ in $H^1_0(\Omega)$, as in the proof of Corollary [[§33 Sobolev Spaces and Weak Derivatives#^cor-33-12|§33.12]]). Let $\tilde f$ and $\tilde h_j$ be the extensions of $f$ and $\partial_{x_j} f$ by $0$ to $\mathbb{R}^n$. Then $\tilde h_j$ is the weak derivative of $\tilde f$ on $\mathbb{R}^n$:
>
> $$
> \int_{\mathbb{R}^n} \tilde h_j\, \varphi\, dx = -\int_{\mathbb{R}^n} \tilde f\, \partial_{x_j}\varphi\, dx \qquad \text{for all } \varphi \in C_c^\infty(\mathbb{R}^n),\ j = 1, \ldots, n .
> $$
>
> In particular $\tilde f \in W^{1,2}(\mathbb{R}^n)$ in the sense of Definition [[§33 Sobolev Spaces and Weak Derivatives#^def-33-7|§33.7]].

^prop-33-13

> [!proof]+ Proof
> *(Not from lecture.)* Choose $g_n \in C_c^\infty(\Omega)$ with $g_n \to f$ and $\partial_{x_j} g_n \to \partial_{x_j} f$ in $L^2(\Omega)$. By Proposition [[§33 Sobolev Spaces and Weak Derivatives#^prop-33-1|§33.1]], the extension $\tilde g_n$ of $g_n$ by zero lies in $C_c^\infty(\mathbb{R}^n)$, and $\partial_{x_j} \tilde g_n$ is the extension by zero of $\partial_{x_j} g_n$: the two agree on $\Omega$, and both vanish on the open set $\mathbb{R}^n \setminus \operatorname{supp} g_n$, where $\tilde g_n = 0$. Since the differences vanish outside $\Omega$,
>
> $$
> \|\tilde g_n - \tilde f\|_{L^2(\mathbb{R}^n)} = \|g_n - f\|_{L^2(\Omega)} \to 0, \qquad \|\partial_{x_j}\tilde g_n - \tilde h_j\|_{L^2(\mathbb{R}^n)} = \|\partial_{x_j} g_n - \partial_{x_j} f\|_{L^2(\Omega)} \to 0
> $$
>
> (in particular the extensions have the same norms as the $g_n$, and $\{\tilde g_n\}$ is Cauchy in the $W^{1,2}(\mathbb{R}^n)$ norm). Fix $\varphi \in C_c^\infty(\mathbb{R}^n)$. By Lemma [[§33 Sobolev Spaces and Weak Derivatives#^lem-33-2|§33.2]] on $\mathbb{R}^n$ with $g = \tilde g_n \in C^1(\mathbb{R}^n)$,
>
> $$
> \int_{\mathbb{R}^n} \partial_{x_j}\tilde g_n\, \varphi\, dx = -\int_{\mathbb{R}^n} \tilde g_n\, \partial_{x_j}\varphi\, dx \qquad \text{for every } n .
> $$
>
> Let $n \to \infty$, as in the proof of Proposition [[§33 Sobolev Spaces and Weak Derivatives#^prop-33-3|§33.3]]: by Cauchy–Schwarz in $L^2(\mathbb{R}^n)$, $\bigl| \int (\tilde g_n - \tilde f)\, \partial_{x_j}\varphi \bigr| \le \|\tilde g_n - \tilde f\|_{L^2}\, \|\partial_{x_j}\varphi\|_{L^2} \to 0$, and likewise $\bigl| \int (\partial_{x_j}\tilde g_n - \tilde h_j)\, \varphi \bigr| \le \|\partial_{x_j}\tilde g_n - \tilde h_j\|_{L^2}\, \|\varphi\|_{L^2} \to 0$; $\varphi$ and $\partial_{x_j}\varphi$ are continuous with compact support, hence in $L^2$. This gives the identity. Finally $\tilde f$ and the $\tilde h_j$ lie in $L^2(\mathbb{R}^n)$, so $\tilde f \in W^{1,2}(\mathbb{R}^n)$.

^pf-33-13

*Uses:* [[§33 Sobolev Spaces and Weak Derivatives#^prop-33-1|§33.1]], [[§33 Sobolev Spaces and Weak Derivatives#^lem-33-2|§33.2]], [[§33 Sobolev Spaces and Weak Derivatives#^prop-33-3|§33.3]], [[§23 Cauchy–Schwarz and the Induced Norm#^thm-23-1|§23.1]]

![[m556-33-4.svg]]
*In one dimension, extended by zero: an element of $H^1_0(a,b)$ must come down to $0$ at the endpoints; a function that jumps there does not belong, although as an $L^2$ function it could be changed at the two endpoints without changing anything.*
