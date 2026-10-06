---
type: section
subject: "[[Functional Analysis]]"
chapter: 6
section: 33
tags: [functional-analysis, math556]
---
← [[§32 Sesquilinear Forms and the Lax–Milgram Theorem]] · ↑ [[· 6 Bounded Linear Maps]] · [[§34 ℝⁿ, Cᵐ and Lᵖ]] →

*Stage: maps — Thread: completeness. Completing smooth functions in a norm that sees derivatives; the elements of the completion have derivatives only in a weak sense.*

[[§32 Sesquilinear Forms and the Lax–Milgram Theorem#^thm-32-2|Lax–Milgram]] is applied to elliptic PDE in Sobolev spaces. Wu revisited them (they were first met as completions in Example [[§23 Cauchy–Schwarz and the Induced Norm#^ex-23-3|§23.3]]) to say what their elements are.

## Sobolev Spaces as Completions

> [!definition] Definition §33.1: The Sobolev Norm
> Let $\overline{\Omega} \subset \mathbb{R}^n$ be bounded and closed, with interior $\Omega$, and let $X = C^\infty(\overline{\Omega})$. For $1 \le p < \infty$ and an integer $k \ge 0$ define
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
> - The completion machinery behind it: [[§12 Completeness#^prop-12-3|§12.3]], [[§13 The Completion of a Normed Space#^thm-13-1|§13.1]]; the same construction with $L^p$ norms only, [[§19 The Function Spaces Lᵖ(Ω)#^prop-19-8|§19.8]]; a norm with one derivative on a space of smoother functions is again not complete, [[§13 The Completion of a Normed Space#^prop-13-4|§13.4]].

> [!remark] Remark
> Every $\partial^\alpha f$ of a $C^\infty$ function is again $C^\infty$, and bounded on the compact set $\overline{\Omega}$, so every term is finite. Wu noted that $p = \infty$ can be treated as well. The two claims “this is a norm” and “$X$ is not complete” were left to the class; the first is proved after Definition [[§33 Sobolev Spaces and Weak Derivatives#^def-33-1|§33.1]], and the example of [[§33 Sobolev Spaces and Weak Derivatives#Examples|§33]] shows how completeness fails.

^rem-33-1

> [!example] Example §33.1: $k = 0$: the Completion is $L^p$
> For $k = 0$ the norm is $\|f\|_{L^p}$. Since smooth functions are dense in $L^p(\Omega)$ (Theorem [[§19 The Function Spaces Lᵖ(Ω)#^thm-19-4|§19.4]]), the completion of $C^\infty(\overline{\Omega})$ in this norm is $L^p(\Omega)$ (Proposition [[§13 The Completion of a Normed Space#^prop-13-2|§13.2]]).

^ex-33-1

> [!remark]- Connections
> - Density in $L^p$ in measure theory, with $C_c$ in place of $C^\infty$: [[§35 Lᵖ as a Banach Space#^thm-35-12|551 §35.12]](iii).
> - The one-dimensional case done earlier in the course, $L^p[a,b]$ as the completion of $C[a,b]$: [[§19 The Function Spaces Lᵖ(Ω)#^prop-19-8|§19.8]].

> [!remark] Remark: What is in $W^{1,p}$?
> An element $f$ of the completion for $k = 1$ is the limit of a sequence $g_n \in C^\infty(\overline{\Omega})$ that is Cauchy in $|\cdot|_{W^{1,p}}$. That means $\{g_n\}$ is Cauchy in $L^p$, and so is each $\{\partial_{x_j} g_n\}$. Hence $g_n \to f$ in $L^p$ and $\partial_{x_j} g_n \to f_j$ in $L^p$ for some $f_j$. Heuristically $f_j$ should be “$\partial_{x_j} f$”, but $f$ is only an $L^p$ function and has no derivative in the classical sense; difference quotients of an $L^p$ function make no sense. The question is: *in what sense is $f_j = \partial_{x_j} f$?* The answer is integration by parts.

^rem-33-2

## Integration by Parts and Weak Derivatives

> [!definition] Definition §33.3: Test Functions
> Let $\Omega \subset \mathbb{R}^n$ be open. The **test functions** on $\Omega$ are the elements of $C_c^\infty(\Omega)$, the $C^\infty$ functions whose support is a compact subset of $\Omega$.

^def-33-3

> [!theorem] Lemma §33.1: Integration by Parts against a Test Function
> Let $\Omega \subset \mathbb{R}^n$ be open, $g \in C^1(\Omega)$, and $\varphi \in C_c^\infty(\Omega)$ a test function (Definition [[§33 Sobolev Spaces and Weak Derivatives#^def-33-3|§33.3]]). Then for each $j$,
>
> $$
> \int_\Omega \partial_{x_j} g(x)\, \varphi(x)\, dx = -\int_\Omega g(x)\, \partial_{x_j} \varphi(x)\, dx .
> $$

^lem-33-1

> [!proof]+ Proof
> Wu's argument is the [[§28 The Divergence Theorem in Higher Dimensions and Green's Identities#^thm-28-1|divergence theorem]], $\int_\Omega \operatorname{div} \vec{F}\, dx = \int_{\partial\Omega} \vec{F} \cdot \vec{n}\, dS$, applied to the vector field $\vec{F}$ whose only nonzero component is the $j$-th, $F_j = g\varphi$. Then $\operatorname{div}\vec F = \partial_{x_j}(g \varphi) = (\partial_{x_j} g)\varphi + g\, \partial_{x_j}\varphi$, and the boundary integral $\int_{\partial\Omega} n_j\, g \varphi\, dS$ vanishes because $\varphi = 0$ near $\partial\Omega$. In one dimension it is the usual [[§34 Fundamental Theorem of Calculus#^thm-34-3|integration by parts]] on an interval $[a, b]$ containing the support of $\varphi$: $\int_a^b g'\varphi = [g\varphi]_a^b - \int_a^b g \varphi' = -\int_a^b g\varphi'$, since $\varphi(a) = \varphi(b) = 0$.
>
> (The divergence theorem needs a smooth enough boundary; the identity itself does not. Extend $g\varphi$ and $g\,\partial_{x_j}\varphi$ by $0$ outside the support $K$ of $\varphi$; then $h = g\varphi$ is $C^1$ on $\mathbb{R}^n$ with compact support. By [[§25 Invariance Properties and Fubini's Theorem#^thm-25-6|Fubini]], integrate $\partial_{x_j} h$ first in $x_j$: for fixed other variables, $\int_{\mathbb{R}} \partial_{x_j} h\, dx_j = 0$ by the [[§34 Fundamental Theorem of Calculus#^thm-34-1|fundamental theorem of calculus]], since $h$ vanishes outside a bounded interval. So $\int \partial_{x_j}(g\varphi) = 0$, which is the identity by the product rule.)

^pf-33-1

*Uses:* [[§33 Sobolev Spaces and Weak Derivatives#^def-33-3|Def. §33.3]], [[§28 The Divergence Theorem in Higher Dimensions and Green's Identities#^thm-28-1|452 §28.1]], [[§34 Fundamental Theorem of Calculus#^thm-34-3|451 §34.3]], [[§25 Invariance Properties and Fubini's Theorem#^thm-25-6|551 §25.6]], [[§34 Fundamental Theorem of Calculus#^thm-34-1|451 §34.1]]

> [!remark]- Connections
> - Integration by parts in $\mathbb{R}^n$ with the boundary term kept: [[§28 The Divergence Theorem in Higher Dimensions and Green's Identities#^thm-28-2|Green's first identity, 452 §28.2]].

> [!theorem] Proposition §33.2: Limits in $W^{1,p}$ Satisfy Integration by Parts
> Let $g_n \in C^\infty(\overline{\Omega})$ with $g_n \to f$ and $\partial_{x_j} g_n \to f_j$ in $L^p(\Omega)$, $1 \le p < \infty$. Then for every $\varphi \in C_c^\infty(\Omega)$,
>
> $$
> \int_\Omega f_j(x)\, \varphi(x)\, dx = -\int_\Omega f(x)\, \partial_{x_j}\varphi(x)\, dx .
> $$

^prop-33-2

> [!proof]+ Proof
> By Lemma [[§33 Sobolev Spaces and Weak Derivatives#^lem-33-1|§33.1]], $\int_\Omega \partial_{x_j} g_n\, \varphi = -\int_\Omega g_n\, \partial_{x_j}\varphi$ for every $n$. Let $n \to \infty$ on both sides. On the right, by Hölder's inequality (Theorem [[§19 The Function Spaces Lᵖ(Ω)#^thm-19-1|§19.1]]) with $\frac1p + \frac1{p'} = 1$,
>
> $$
> \Bigl| \int_\Omega (g_n - f)\, \partial_{x_j} \varphi\, dx \Bigr| \le \|g_n - f\|_{L^p}\, \|\partial_{x_j}\varphi\|_{L^{p'}} \to 0,
> $$
>
> since $\partial_{x_j}\varphi$ is continuous with compact support, hence in every $L^{p'}$. The same argument on the left, with $\partial_{x_j} g_n - f_j$ and $\varphi$, gives $\int \partial_{x_j} g_n\, \varphi \to \int f_j\, \varphi$.

^pf-33-2

*Uses:* [[§33 Sobolev Spaces and Weak Derivatives#^lem-33-1|§33.1]], [[§19 The Function Spaces Lᵖ(Ω)#^def-19-1|Def. §19.1]], [[§19 The Function Spaces Lᵖ(Ω)#^thm-19-1|§19.1]]

> [!remark] Remark: Hölder, not Dominated Convergence
> Wu asked the class which theorem justifies the limit. The [[§23 The Dominated Convergence Theorem#^thm-23-3|dominated convergence theorem]] needs pointwise a.e. convergence, and $g_n \to f$ in $L^p$ does not give that (only a subsequence converges a.e.). [[§19 The Function Spaces Lᵖ(Ω)#^thm-19-1|Hölder's inequality]] needs only convergence in $L^p$ and a fixed partner in $L^{p'}$, which the test function supplies.

^rem-33-3

> [!remark]- Connections
> - The subsequence statement: [[§35 Lᵖ as a Banach Space#^cor-35-10|551 §35.10]]; the measure-theoretic home of Hölder, [[§34 Normed Linear Spaces and Lᵖ Spaces#^thm-34-5|551 §34.5]].

> [!definition] Definition §33.4: Weak Derivative
> Let $\Omega \subset \mathbb{R}^n$ be open, $1 \le p \le \infty$, and $f \in L^p(\Omega)$. If there is $f_j \in L^p(\Omega)$ such that
>
> $$
> \int_\Omega f_j(x)\, \varphi(x)\, dx = -\int_\Omega f(x)\, \partial_{x_j}\varphi(x)\, dx \qquad \text{for all } \varphi \in C_c^\infty(\Omega),
> $$
>
> then $f_j$ is a **weak** (or **distributional**) **derivative** of $f$, written $f_j = \partial_{x_j} f$. More generally, $g = \partial^\alpha f$ weakly if $\int_\Omega g\, \varphi = (-1)^{|\alpha|} \int_\Omega f\, \partial^\alpha \varphi$ for all $\varphi \in C_c^\infty(\Omega)$.

^def-33-4

> [!remark] Remark
> A weak derivative need not exist; the definition only says what one is if it does (Wu added the words “if there exists” after the first example). Both sides make sense whenever $f, f_j \in L^p$, because $\varphi$ and $\partial_{x_j}\varphi$ lie in every $L^{p'}$. The general $\alpha$ version, with the sign $(-1)^{|\alpha|}$ from integrating by parts $|\alpha|$ times, is how Wu's “we can continue to define second order or others” is made precise. By Proposition [[§33 Sobolev Spaces and Weak Derivatives#^prop-33-2|§33.2]], for every element $f$ of the completion $W^{1,p}$ the limits $f_j$ are weak derivatives of $f$.

^rem-33-4

> [!theorem] Lemma §33.3: Weak Derivatives are Unique
> If $f_j$ and $\tilde f_j$ are both weak derivatives of $f$ in the $x_j$-direction, then $f_j = \tilde f_j$ a.e. If $f \in C^1(\Omega)$ and its classical derivative $\partial_{x_j} f$ lies in $L^p(\Omega)$, then the classical derivative is the weak derivative.

^lem-33-3

> [!proof]+ Proof
> (Not covered in lecture.) $h = f_j - \tilde f_j$ satisfies $\int_\Omega h\, \varphi = 0$ for all $\varphi \in C_c^\infty(\Omega)$. By the fundamental lemma of the calculus of variations (real analysis: a locally integrable function that integrates to $0$ against every test function vanishes a.e.), $h = 0$ a.e. For the second part, Lemma [[§33 Sobolev Spaces and Weak Derivatives#^lem-33-1|§33.1]] shows that the classical derivative satisfies the defining identity.

^pf-33-3

*Uses:* [[§33 Sobolev Spaces and Weak Derivatives#^def-33-4|Def. §33.4]], [[§33 Sobolev Spaces and Weak Derivatives#^lem-33-1|§33.1]]

> [!remark]- Connections
> - The fundamental lemma for continuous functions on an interval, with its proof by a bump: [[§B5.1 The Euler–Lagrange Equation#^thm-b5-1-2|CM Lemma §B5.1.2]].

> [!remark] Remark: Weak and Classical Derivatives Agree Where $f$ is Smooth
> A student asked whether the weak derivative always matches the pointwise derivative. Wu: where $f$ is $C^1$ in a region, take test functions supported in that region; there the weak derivative is the classical one (Lemma [[§33 Sobolev Spaces and Weak Derivatives#^lem-33-3|§33.3]]). Where $f$ has a singularity, there is no pointwise derivative to compare with, and a weak derivative is an element of $L^p$, defined only almost everywhere: it has no value at a single point.

^rem-33-5

> [!definition] Definition §33.5: Sobolev Space via Weak Derivatives
> For $\Omega \subset \mathbb{R}^n$ open, an integer $k \ge 0$ and $1 \le p \le \infty$,
>
> $$
> W^{k,p}(\Omega) = \bigl\{ f \in L^p(\Omega) : \text{the weak derivatives } \partial^\alpha f \text{ exist and lie in } L^p(\Omega) \text{ for all } |\alpha| \le k \bigr\}.
> $$

^def-33-5

> [!remark] Remark
> Wu used both descriptions of $W^{k,p}$: the completion of Definition [[§33 Sobolev Spaces and Weak Derivatives#^def-33-2|§33.2]], and the weak-derivative space above. Proposition [[§33 Sobolev Spaces and Weak Derivatives#^prop-33-2|§33.2]] shows that every element of the completion (for $k = 1$) has its weak first derivatives in $L^p$, so the completion sits inside the weak-derivative space. That the two coincide for reasonable $\Omega$ (every function with weak derivatives in $L^p$ is a $W^{k,p}$-limit of smooth functions) is the Meyers–Serrin theorem, which was not covered.

^rem-33-6

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
> Wu's computation. Split at $0$ and integrate by parts on each half-line:
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

*Uses:* [[§33 Sobolev Spaces and Weak Derivatives#^def-33-4|Def. §33.4]], [[§33 Sobolev Spaces and Weak Derivatives#^def-33-5|Def. §33.5]], [[§34 Fundamental Theorem of Calculus#^thm-34-3|451 §34.3]]

> [!example] Example §33.3: $\operatorname{sgn} x$ has No Weak Derivative
> Let $f(x) = 1$ for $x > 0$ and $f(x) = -1$ for $x < 0$. Then $\int f\varphi' = -2\varphi(0)$ for every $\varphi \in C_c^\infty(\mathbb{R})$, and there is no locally integrable $g$ with $\int f\varphi' = -\int g\varphi$ for all $\varphi$. So $f$ has no weak derivative, in any $L^p$.

^ex-33-3

> [!proof]+ Proof
> Wu's computation: $\int_{-\infty}^\infty f\varphi' = \int_0^\infty \varphi' - \int_{-\infty}^0 \varphi' = \bigl[\varphi\bigr]_0^\infty - \bigl[\varphi\bigr]_{-\infty}^0 = -\varphi(0) - \varphi(0) = -2\varphi(0)$.
>
> (The non-existence was left to the class.) Suppose $g$ is locally integrable with $\int g\varphi = 2\varphi(0)$ for all test functions $\varphi$. Let $\psi(x) = e^{1 - 1/(1 - x^2)}$ for $|x| < 1$ and $\psi(x) = 0$ otherwise; this is a standard $C_c^\infty$ function with $0 \le \psi \le 1$ and $\psi(0) = 1$. For $0 < \varepsilon \le 1$ let $\varphi_\varepsilon(x) = \psi(x/\varepsilon)$, supported in $[-\varepsilon, \varepsilon]$ with $\varphi_\varepsilon(0) = 1$. Then
>
> $$
> 2 = 2\varphi_\varepsilon(0) = \int g\, \varphi_\varepsilon \le \int_{-\varepsilon}^{\varepsilon} |g(x)|\, dx \xrightarrow[\varepsilon \to 0]{} 0,
> $$
>
> the limit by the [[§23 The Dominated Convergence Theorem#^thm-23-3|dominated convergence theorem]] applied to $|g|\chi_{[-\varepsilon, \varepsilon]} \le |g|\chi_{[-1,1]} \in L^1$. This is a contradiction.

^pf-ex-33-3

*Uses:* [[§33 Sobolev Spaces and Weak Derivatives#^def-33-3|Def. §33.3]], [[§33 Sobolev Spaces and Weak Derivatives#^def-33-4|Def. §33.4]], [[§34 Fundamental Theorem of Calculus#^thm-34-1|451 §34.1]], [[§23 The Dominated Convergence Theorem#^thm-23-3|551 §23.3]]

> [!remark]- Connections
> - The flat function $e^{-1/x^2}$ behind $\psi$, smooth with every derivative $0$ at the origin: [[§31 Taylor's Theorem#^ex-31-3|451 Ex. §31.3]]; bump functions on manifolds, [[§47 Vector Fields#^prop-47-3|591 §47.3]].

![[m556-33-1.svg]]
*The board pictures. A corner is harmless: $|x|$ has the bounded weak derivative $\operatorname{sgn} x$. A jump is not: the “derivative” of $\operatorname{sgn} x$ is concentrated at a single point with total mass $2$, which no function can do.*

> [!remark] Remark: Distributions
> Wu: what $\operatorname{sgn} x$ does have is a *distributional* derivative, $f' = 2\delta_0$, twice the delta “function” — zero away from the origin, with $\int (2\delta_0)\varphi = 2\varphi(0)$. A distribution is a linear functional on the test functions $C_c^\infty$, continuous in a suitable sense; $\delta_0(\varphi) = \varphi(0)$ is one, and every $L^p$ function defines one by $\varphi \mapsto \int f\varphi$. In this language every $L^p$ function has a distributional derivative, and a weak derivative is a distributional derivative that happens to be an $L^p$ function. Distributions are to come later in the course. (A student asked whether the name has to do with probability distributions: it does not.)

^rem-33-7

> [!remark]- Connections
> - Distributions and their derivatives in Quantum Field Theory: [[§CA.2 Generalized Functions#^def-ca-2-2|QFT Def. §CA.2.2]], [[§CA.2 Generalized Functions#^def-ca-2-4|QFT Def. §CA.2.4]]; the step function has derivative $\delta$, the same computation as Example [[§33 Sobolev Spaces and Weak Derivatives#^ex-33-3|§33.3]] — [[§CA.2 Generalized Functions#^thm-ca-2-3|QFT Theorem §CA.2.3]].

## The Space $H^1_0$ and the Poincaré Inequality

> [!definition] Definition §33.6: The $W^{1,2}$ Norm on Test Functions
> Let $\Omega \subset \mathbb{R}^n$ be bounded and open. On $C_c^\infty(\Omega)$ put
>
> $$
> \|f\|_{W^{1,2}(\Omega)} = \Bigl( \|f\|_{L^2(\Omega)}^2 + \|\nabla f\|_{L^2(\Omega)}^2 \Bigr)^{1/2}, \qquad \|\nabla f\|_{L^2}^2 = \sum_{j=1}^n \|\partial_{x_j} f\|_{L^2}^2 .
> $$

^def-33-6

> [!definition] Definition §33.7: The Space $H^1_0(\Omega)$
> Let $\Omega \subset \mathbb{R}^n$ be bounded and open. $H^1_0(\Omega)$ is the completion of $C_c^\infty(\Omega)$ in the norm $\|\cdot\|_{W^{1,2}(\Omega)}$ of Definition [[§33 Sobolev Spaces and Weak Derivatives#^def-33-6|§33.6]].

^def-33-7

> [!theorem] Proposition §33.4: $H^1_0(\Omega)$ is a Hilbert Space
> - (a) The norm of Definition [[§33 Sobolev Spaces and Weak Derivatives#^def-33-6|§33.6]] is equivalent to the summed norm $\|f\|_{L^2} + \sum_j \|\partial_{x_j} f\|_{L^2}$ of Definition [[§33 Sobolev Spaces and Weak Derivatives#^def-33-1|§33.1]].
> - (b) $H^1_0(\Omega)$ is a Hilbert space.

^prop-33-4

> [!proof]+ Proof
> (Stated in lecture; (b) was left to the class.) (a) For non-negative numbers $t_0, \ldots, t_n$, $\bigl(\sum t_i^2\bigr)^{1/2} \le \sum t_i \le \sqrt{n+1}\,\bigl(\sum t_i^2\bigr)^{1/2}$: the first because $\bigl(\sum t_i\bigr)^2 \ge \sum t_i^2$, the second by [[§16 Means and Young's Inequality#^prop-16-1|Cauchy–Schwarz]] in $\mathbb{R}^{n+1}$ applied to $(t_i)$ and $(1, \ldots, 1)$. Apply this with $t_0 = \|f\|_{L^2}$, $t_j = \|\partial_{x_j} f\|_{L^2}$.
>
> (b) On $C_c^\infty(\Omega)$ the norm comes from the inner product $(f, g) = \int_\Omega f\bar g + \sum_j \int_\Omega \partial_{x_j} f\, \overline{\partial_{x_j} g}$ (the case $k = 1$ of Example [[§23 Cauchy–Schwarz and the Induced Norm#^ex-23-3|§23.3]]), so it satisfies the [[§24 The Parallelogram Law and Jordan–von Neumann#^prop-24-1|parallelogram law]]. The completion is a Banach space (Theorem [[§13 The Completion of a Normed Space#^thm-13-1|§13.1]]), and its norm is the limit of norms of representatives: $\|[\{f_n\}]\| = \lim_n \|f_n\|$. For $x = [\{f_n\}]$, $y = [\{g_n\}]$, the parallelogram law $\|f_n + g_n\|^2 + \|f_n - g_n\|^2 = 2\|f_n\|^2 + 2\|g_n\|^2$ holds for each $n$ and passes to the limit, so it holds in the completion. By the Jordan–von Neumann theorem (Theorem [[§24 The Parallelogram Law and Jordan–von Neumann#^thm-24-2|§24.2]]) the norm of the completion comes from an inner product; being complete, $H^1_0(\Omega)$ is a Hilbert space.

^pf-33-4

*Uses:* [[§16 Means and Young's Inequality#^prop-16-1|§16.1]], [[§14 New Normed Spaces from Old#^def-14-1|Def. §14.1]], [[§23 Cauchy–Schwarz and the Induced Norm#^ex-23-3|Ex. §23.3]], [[§24 The Parallelogram Law and Jordan–von Neumann#^prop-24-1|§24.1]], [[§13 The Completion of a Normed Space#^thm-13-1|§13.1]], [[§24 The Parallelogram Law and Jordan–von Neumann#^thm-24-2|§24.2]], [[§23 Cauchy–Schwarz and the Induced Norm#^def-23-1|Def. §23.1]]

> [!remark] Remark
> Every element of $H^1_0(\Omega)$ is a limit of functions that vanish near the boundary, so it “is zero on the boundary in some sense” (Wu) — this is what distinguishes $H^1_0$ from the completion of $C^\infty(\overline\Omega)$, and it is the boundary condition of a Dirichlet problem built into the space. Making “zero on the boundary” precise (trace theorems) was not covered.

^rem-33-8

> [!theorem] Theorem §33.5: Poincaré Inequality
> Let $\Omega \subset \mathbb{R}^n$ be bounded and open. There is a constant $C > 0$, depending only on $\Omega$, such that
>
> $$
> \int_\Omega |f(x)|^2\, dx \le C^2 \int_\Omega |\nabla f(x)|^2\, dx \qquad \text{for all } f \in C_c^\infty(\Omega).
> $$
>
> One can take $C = 2L$ for any $L$ with $\Omega \subset (-L, L)^n$.

^thm-33-5

> [!proof]+ Proof
> **Step 1: put $\Omega$ in a box and extend by zero.** Since $\Omega$ is bounded, $\Omega \subset (-L, L)^n$ for some $L > 0$. Extend $f$ by $f(x) = 0$ for $x \notin \Omega$; because the support of $f$ is a compact subset of $\Omega$, the extension is $C^\infty$ on $\mathbb{R}^n$ and vanishes outside $\Omega$, in particular on the face $x_1 = -L$ of the box.
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

^pf-33-5

*Uses:* [[§33 Sobolev Spaces and Weak Derivatives#^def-33-3|Def. §33.3]], [[§34 Fundamental Theorem of Calculus#^thm-34-1|451 §34.1]], [[§19 The Function Spaces Lᵖ(Ω)#^thm-19-1|§19.1]], [[§25 Invariance Properties and Fubini's Theorem#^thm-25-6|551 §25.6]]

![[m556-33-2.svg]]
*The proof in one picture: $f$ vanishes on the left face of the box, so its value at $x$ is the integral of $\partial_{x_1} f$ along the horizontal segment that reaches $x$, and Cauchy–Schwarz turns the length $2L$ of that segment into the constant. The constant depends only on the width of $\Omega$ in one direction. “If the function is zero somewhere, it can be controlled by its gradient.”*

> [!theorem] Corollary §33.6: Poincaré on $H^1_0$
> The Poincaré inequality $\|f\|_{L^2(\Omega)} \le C\, \|\nabla f\|_{L^2(\Omega)}$ holds for all $f \in H^1_0(\Omega)$.

^cor-33-6

> [!proof]+ Proof
> Next lecture (by approximating $f$ with a Cauchy sequence in $C_c^\infty(\Omega)$).

^pf-33-6
