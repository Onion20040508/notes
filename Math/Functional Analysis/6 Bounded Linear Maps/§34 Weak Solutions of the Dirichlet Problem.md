---
type: section
subject: "[[Functional Analysis]]"
chapter: 6
section: 34
tags: [functional-analysis, math556]
---
← [[§33 Sobolev Spaces and Weak Derivatives]] · ↑ [[· 6 Bounded Linear Maps]] · [[§35 Measures and the Radon–Nikodym Theorem]] →

*Stage: maps — Thread: functionals. A boundary value problem for a PDE becomes the representation of a bounded functional by a coercive form.*

Wu: “we are going to do some application in analysis.” Throughout, a *bounded domain* is a bounded open set $\Omega \subset \mathbb{R}^n$, and functions are real-valued (“in the real world temperature is real”). $C^2(\overline{\Omega})$ denotes the functions whose derivatives up to order $2$ exist on $\Omega$ and extend continuously to $\overline{\Omega}$, as in Example [[§30 Boundedness and Continuity#^ex-30-1|§30.1]].

> [!definition] Definition §34.1: The Dirichlet Problem
> Let $\Omega \subset \mathbb{R}^n$ be a bounded domain and $f$ a function on $\Omega$. The **Dirichlet problem** for the Poisson equation is
>
> $$
> (D) \qquad \begin{cases} -\Delta u(x) = f(x), & x \in \Omega, \\ \phantom{-\Delta} u(x) = 0, & x \in \partial\Omega, \end{cases} \qquad \Delta = \partial_{x_1}^2 + \cdots + \partial_{x_n}^2 .
> $$
>
> A **classical solution** is a $u \in C^2(\overline{\Omega})$ satisfying both equations pointwise.

^def-34-1

> [!remark]- Connections
> - Classical uniqueness for the Dirichlet problem, by [[Green's First Identity|Green's first identity]]: [[§28 The Divergence Theorem in Higher Dimensions and Green's Identities#^ex-28-1|452 Ex. §28.1]]; the Dirichlet problem for Laplace's equation in fluid flow, [[§29 Conservation of Mass and Laplace's Equation#^rem-29-4|452 §29]].
> - The same problem in electrostatics (Poisson's equation with prescribed boundary potential), uniqueness of classical solutions: [[§B3.1 Laplace's Equation and the Uniqueness Theorems#^thm-b3-1-3|EM Theorem §B3.1.3]].

> [!remark] Remark: Where the Equation Comes From
> The heat equation $(\partial_t - \mu\Delta) u = f(x)$, $\mu > 0$, describes the temperature $u(x,t)$ in a piece of material occupying $\Omega$, with a time-independent heat source $f$; the term $\mu\Delta u$ is diffusion. Hold the boundary at temperature $0$, keep heating, and wait: the temperature settles to an equilibrium, which no longer depends on $t$, so $\partial_t u = 0$ and $-\mu\Delta u = f$. (Absorbing $\mu$ into $f$ gives $(D)$.) So $(D)$ describes the equilibrium state of a heated piece of material, $u$ the temperature and $f$ the heat source. If the model is right, there should be exactly one equilibrium. Hence Wu's question: *does $(D)$ have a unique solution for every $f$?*

^rem-34-1

> [!remark]- Connections
> - The heat equation with a source, derived from heat flux and heat capacity: [[§B5.3★ The Thermal Diffusion Equation#^thm-b5-3-2|TH Theorem §B5.3.2]]; its steady states $\nabla^2 T = -H/\kappa$, unique for given boundary temperatures: [[§B5.3★ The Thermal Diffusion Equation#^thm-b5-3-5|TH Theorem §B5.3.5]].

![[m556-34-1.svg]]
*The board picture: a plate held at temperature $0$ on its boundary and heated inside. The equilibrium temperature $u$ solves $(D)$.*

![[m556-34-2.svg]]
*The equilibrium temperature computed: the solution of $(D)$ on a plate-shaped $\Omega$ for a heat source $f$ concentrated in the white circle (a Gaussian bump), found numerically by finite differences, with isotherms at $5\%, 10\%, 20\%, \ldots, 90\%$ of the maximum. Below, the temperature along the dashed line: hottest at the source, falling to $0$ at $\partial\Omega$. (Not from lecture; computed for these notes.)*

> [!remark] Remark: Why Not Solve Directly
> Finding an exact solution is generally out of reach: formulas are available essentially only for ODE, and a PDE on a rectangle can be reduced to ODE by separation of variables, but a general domain cannot. A student suggested approximating $\Omega$ by small rectangles; Wu: on each small rectangle one would need its boundary values, which are exactly what is unknown — different boundary temperatures give different solutions. The strategy is instead to *enlarge the class of solutions*: find a solution in a weaker sense, then (regularity theory, not covered) show that it is classical when $f$ is smooth. “When you don't have anywhere to go, you try to expand your search.”

^rem-34-2

> [!theorem] Proposition §34.1: Classical Solutions Satisfy the Weak Equation
> Let $u \in C^2(\overline{\Omega})$ be a classical solution of $(D)$ with $f$ continuous. Then
>
> $$
> \int_\Omega \nabla u(x) \cdot \nabla v(x)\, dx = \int_\Omega f(x)\, v(x)\, dx \qquad \text{for all } v \in C_c^2(\Omega).
> $$

^prop-34-1

> [!proof]+ Proof
> Multiply the equation by $v$ and integrate: $\int_\Omega -\Delta u\, v\, dx = \int_\Omega f\, v\, dx$. Write $\Delta u = \operatorname{div}(\nabla u)$, where $\operatorname{div}\vec F = \partial_{x_1} F_1 + \cdots + \partial_{x_n} F_n$. By the product rule in each component,
>
> $$
> \operatorname{div}(v\, \nabla u) = \sum_{j=1}^n \partial_{x_j}\bigl( v\, \partial_{x_j} u \bigr) = \nabla v \cdot \nabla u + v\, \Delta u .
> $$
>
> By the [[§28 The Divergence Theorem in Higher Dimensions and Green's Identities#^thm-28-1|divergence theorem]] $\int_\Omega \operatorname{div}\vec F\, dx = \int_{\partial\Omega} \vec n \cdot \vec F\, dS$, with $\vec n$ the outward unit normal,
>
> $$
> \int_\Omega \nabla v \cdot \nabla u\, dx + \int_\Omega v\, \Delta u\, dx = \int_{\partial\Omega} (\vec n \cdot \nabla u)\, v\, dS = 0,
> $$
>
> because $v = 0$ on $\partial\Omega$. Hence $\int_\Omega \nabla u \cdot \nabla v\, dx = -\int_\Omega v\, \Delta u\, dx = \int_\Omega f v\, dx$.
>
> (The divergence theorem needs a smooth enough $\partial\Omega$. It can be avoided: for each $j$, Lemma [[§33 Sobolev Spaces and Weak Derivatives#^lem-33-2|§33.2]] with $g = \partial_{x_j} u \in C^1(\Omega)$ and $\varphi = v$ gives $\int_\Omega \partial_{x_j}^2 u\, v = -\int_\Omega \partial_{x_j} u\, \partial_{x_j} v$; its proof uses only $\varphi \in C^1$ with compact support in $\Omega$. Summing over $j$ gives the same identity.)

^pf-34-1

*Uses:* [[§34 Weak Solutions of the Dirichlet Problem#^def-34-1|Def. §34.1]], [[§28 The Divergence Theorem in Higher Dimensions and Green's Identities#^thm-28-1|452 §28.1]], [[§33 Sobolev Spaces and Weak Derivatives#^lem-33-2|§33.2]]

> [!remark]- Connections
> - The identity in the proof with the boundary term kept is [[§28 The Divergence Theorem in Higher Dimensions and Green's Identities#^thm-28-2|Green's first identity, 452 §28.2]].

> [!remark] Remark
> Two points Wu made. Only $v$ has to vanish on the boundary; $\nabla u$ need not, and indeed for $u$ in the [[§34 Weak Solutions of the Dirichlet Problem#^def-34-2|larger class below]], $\nabla u$ is only in $L^2$ and has no boundary values at all. And $u$ need not be $C_c^2$: $C^2$ up to the boundary is enough to integrate by parts.

^rem-34-3

> [!definition] Definition §34.2: Weak Solution
> Let $f \in L^2(\Omega)$ ([[§22 Definition and Examples#^ex-22-3|Ex. §22.3]]). A function $u \in H^1_0(\Omega)$ ([[§33 Sobolev Spaces and Weak Derivatives#^def-33-9|Def. §33.9]]) is a **weak solution** of $(D)$ if
>
> $$
> \int_\Omega \nabla u(x) \cdot \nabla v(x)\, dx = \int_\Omega f(x)\, v(x)\, dx \qquad \text{for all } v \in H^1_0(\Omega),
> $$
>
> where $\nabla u$, $\nabla v$ are [[§33 Sobolev Spaces and Weak Derivatives#^def-33-6|weak gradients]].

^def-34-2

> [!remark] Remark: Why This is the Right Definition
> The boundary condition $u = 0$ is [[§33 Sobolev Spaces and Weak Derivatives#^rem-33-8|built into the space]] $H^1_0(\Omega)$, and the equation is the identity of Proposition [[§34 Weak Solutions of the Dirichlet Problem#^prop-34-1|§34.1]], which makes sense as soon as $u, v \in H^1_0$ and $f \in L^2$, because only first derivatives in $L^2$ appear. A strong (classical) solution is a weak solution; a weak solution need not be strong, and showing that it is (for smooth $f$) is the regularity theory of PDE (Wu: “you need to show if my source is smooth, then the solution is smooth”). The only difference between the two notions is the class of functions in which a solution is sought.
>
> To pass from $v \in C_c^2$ to $v \in H^1_0$: if $u \in H^1_0(\Omega)$ satisfies the identity for all $v \in C_c^\infty(\Omega)$, it satisfies it for all $v \in H^1_0(\Omega)$, because $C_c^\infty$ is dense in $H^1_0$ ([[§33 Sobolev Spaces and Weak Derivatives#^def-33-9|Def. §33.9]], [[§12 Completeness#^prop-12-3|§12.3]]) and both sides are continuous in $v$ for the $H^1_0$ norm (by [[§23 Cauchy–Schwarz and the Induced Norm#^thm-23-1|Cauchy–Schwarz]], $|\int \nabla u \cdot \nabla v| \le \|\nabla u\|_{L^2}\|\nabla v\|_{L^2}$ and $|\int f v| \le \|f\|_{L^2}\|v\|_{L^2}$). That a classical solution of $(D)$ lies in $H^1_0(\Omega)$ is true for domains with a reasonable boundary, but is not proved here.

^rem-34-4

> [!theorem] Theorem §34.2: Existence and Uniqueness of Weak Solutions
> Let $\Omega \subset \mathbb{R}^n$ be a bounded domain and $f \in L^2(\Omega)$. Then $(D)$ has a unique weak solution $u \in H^1_0(\Omega)$.

^thm-34-2

> [!proof]+ Proof
> **Step 1: the Hilbert space.** $H^1_0(\Omega)$, over $\mathbb{R}$, with the inner product
>
> $$
> (u, v)_{H^1_0} = \int_\Omega u(x)\, v(x)\, dx + \int_\Omega \nabla u(x) \cdot \nabla v(x)\, dx,
> $$
>
> is a [[§23 Cauchy–Schwarz and the Induced Norm#^def-23-1|Hilbert space]] (Proposition [[§33 Sobolev Spaces and Weak Derivatives#^prop-33-5|§33.5]]). Write $\|u\|_{H^1_0}^2 = \|u\|_{L^2}^2 + \|\nabla u\|_{L^2}^2$.
>
> **Step 2: the form is bilinear and bounded.** Let $B(u, v) = \int_\Omega \nabla u(x) \cdot \nabla v(x)\, dx$. It is bilinear, and
>
> $$
> |B(u, v)| \le \|\nabla u\|_{L^2}\, \|\nabla v\|_{L^2} \le \|u\|_{H^1_0}\, \|v\|_{H^1_0} .
> $$
>
> (The first inequality: $|\nabla u \cdot \nabla v| \le |\nabla u|\,|\nabla v|$ pointwise by [[§16 Means and Young's Inequality#^prop-16-1|Cauchy–Schwarz]] in $\mathbb{R}^n$, then [[§23 Cauchy–Schwarz and the Induced Norm#^thm-23-1|Cauchy–Schwarz]] in $L^2$; the second because $\|\nabla u\|_{L^2} \le \|u\|_{H^1_0}$ by the definition of the norm.)
>
> **Step 3: the form is coercive.** We want $\alpha > 0$ with $B(u,u) \ge \alpha \|u\|_{H^1_0}^2$, i.e.
>
> $$
> \int_\Omega |\nabla u|^2\, dx \ge \alpha \Bigl( \int_\Omega |u|^2\, dx + \int_\Omega |\nabla u|^2\, dx \Bigr) .
> $$
>
> By the Poincaré inequality on $H^1_0$ (Corollary [[§33 Sobolev Spaces and Weak Derivatives#^cor-33-7|§33.7]]), $\int_\Omega |u|^2 \le C_0 \int_\Omega |\nabla u|^2$ for all $u \in H^1_0(\Omega)$, with $C_0 = C^2$. Hence
>
> $$
> \|u\|_{H^1_0}^2 \le C_0 \int_\Omega |\nabla u|^2\, dx + \int_\Omega |\nabla u|^2\, dx = (C_0 + 1)\, B(u, u),
> $$
>
> and $\alpha = \frac{1}{1 + C_0}$ works. Wu: coercivity “is really important here” — $B$ contains only the gradient, and it is Poincaré that controls the missing $L^2$ part.
>
> **Step 4: the functional is bounded.** Let $\ell(v) = \int_\Omega f(x)\, v(x)\, dx$ for $v \in H^1_0(\Omega)$. It is linear, and by Cauchy–Schwarz in $L^2$,
>
> $$
> |\ell(v)| \le \|f\|_{L^2}\, \|v\|_{L^2} \le \|f\|_{L^2}\, \|v\|_{H^1_0},
> $$
>
> so $\ell \in H^1_0(\Omega)'$ ([[§31 Dual Spaces#^def-31-1|Def. §31.1]]).
>
> **Step 5: Lax–Milgram.** By Theorem [[§32 Sesquilinear Forms and the Lax–Milgram Theorem#^thm-32-2|§32.2]] there is a unique $u \in H^1_0(\Omega)$ with $\ell(v) = B(v, u)$ for all $v \in H^1_0(\Omega)$. Since $B$ is symmetric, $B(v, u) = B(u, v)$, and the identity reads $\int_\Omega \nabla u \cdot \nabla v\, dx = \int_\Omega f v\, dx$ for all $v$: $u$ is a weak solution, and it is the only one.

^pf-34-2

*Uses:* [[§34 Weak Solutions of the Dirichlet Problem#^def-34-2|Def. §34.2]], [[§33 Sobolev Spaces and Weak Derivatives#^prop-33-5|§33.5]], [[§32 Sesquilinear Forms and the Lax–Milgram Theorem#^def-32-1|Def. §32.1]], [[§16 Means and Young's Inequality#^prop-16-1|§16.1]], [[§23 Cauchy–Schwarz and the Induced Norm#^thm-23-1|§23.1]], [[§33 Sobolev Spaces and Weak Derivatives#^cor-33-7|§33.7]], [[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^def-26-1|Def. §26.1]], [[§31 Dual Spaces#^def-31-1|Def. §31.1]], [[§32 Sesquilinear Forms and the Lax–Milgram Theorem#^thm-32-2|§32.2]]

> [!remark]- Connections
> - Used in Electromagnetism for the existence of the Dirichlet Green function of a bounded region: [[§C7.3 Green Functions for Poisson’s Equation#^rem-c7-3-1|EM ★ Remark: Existence of the Dirichlet Green function]]; the symmetric form $B$ is the Dirichlet energy of [[§C6.4★ The Complex Potential and the Variational Principle#^thm-c6-4-3|Dirichlet's principle, EM Theorem §C6.4.3]].
> - Uniqueness of classical solutions without Hilbert spaces: [[§28 The Divergence Theorem in Higher Dimensions and Green's Identities#^ex-28-1|452 Ex. §28.1]].

> [!remark] Remark
> Here $B$ is symmetric, so Lax–Milgram reduces to the [[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^thm-26-4|Riesz representation theorem]] for the inner product $B$ (Proposition [[§32 Sesquilinear Forms and the Lax–Milgram Theorem#^prop-32-4|§32.4]]); Steps 2 and 3 say exactly that $B$ is an [[§22 Definition and Examples#^def-22-1|inner product]] on $H^1_0(\Omega)$ whose norm is [[§14 New Normed Spaces from Old#^def-14-1|equivalent]] to $\|\cdot\|_{H^1_0}$. Wu's point: for the Laplacian the form is symmetric, but for general elliptic equations ([[§34 Weak Solutions of the Dirichlet Problem#^thm-34-4|below]]) it is not, and then Lax–Milgram is needed. The proof gives existence and uniqueness, not a construction; a student asked how to find $u$: there are numerical methods, which are the subject of another course.

^rem-34-5

> [!remark] Remark: Nonzero Boundary Values
> Wu sketched how a solution can be sought in practice. To solve $\Delta u = f$ in $\Omega$ with given boundary values, first find any $u_0$ with $\Delta u_0 = f$, ignoring the boundary. Then $w = u - u_0$ solves the Laplace equation $\Delta w = 0$ in $\Omega$ with boundary values $w = u - u_0$ on $\partial\Omega$ (for $u = 0$ on $\partial\Omega$, $w = -u_0$ there): an equilibrium with no heat source, held at prescribed boundary temperatures. In one dimension $w'' = 0$ means $w$ is linear, fixed by its two boundary values; in higher dimensions one can approximate $w$ from below by “subsolutions” (Perron's method). Not covered.

^rem-34-6

## General Elliptic Equations

Wu: the same method “goes through” for a whole class of equations, the *elliptic* ones, in which the Laplacian $\Delta u = \operatorname{div}(\nabla u)$ is replaced by $\operatorname{div}(A(x)\nabla u)$ for a matrix of coefficients $A(x)$ — “if it's a Laplacian equation, $A$ is just identity. But in general, we want $A$ positive definite”, with “a lower bound, positive”. The set-up runs parallel to the [[§34 Weak Solutions of the Dirichlet Problem#^def-34-1|Dirichlet problem]] above.

> [!definition] Definition §34.3: Uniformly Elliptic Coefficient Matrix
> Let $\Omega \subset \mathbb{R}^n$ be a bounded domain. An $n \times n$ real matrix $A(x) = (a_{ij}(x))$ of bounded measurable functions on $\Omega$ is **uniformly elliptic** (**uniformly positive definite**) if there are constants $\alpha, \Lambda > 0$ with
>
> $$
> \xi^{\mathsf T} A(x)\, \xi \ge \alpha\, |\xi|^2 \quad \text{and} \quad |A(x)\xi| \le \Lambda\, |\xi| \qquad \text{for all } \xi \in \mathbb{R}^n,\ x \in \Omega .
> $$
>
> $\alpha$ is the **ellipticity constant**.

^def-34-3

> [!definition] Definition §34.4: The Elliptic Dirichlet Problem
> Let $\Omega \subset \mathbb{R}^n$ be a bounded domain, $A$ a [[§34 Weak Solutions of the Dirichlet Problem#^def-34-3|uniformly elliptic]] matrix on $\Omega$ ([[§34 Weak Solutions of the Dirichlet Problem#^def-34-3|Definition §34.3]]) and $f$ a function on $\Omega$. The **Dirichlet problem** for the elliptic operator $u \mapsto -\operatorname{div}(A\nabla u)$ is
>
> $$
> (E) \qquad \begin{cases} -\operatorname{div}\bigl(A(x)\nabla u(x)\bigr) = f(x), & x \in \Omega, \\ \phantom{-\operatorname{div}\bigl(A(x)\nabla} u(x) = 0, & x \in \partial\Omega, \end{cases} \qquad \operatorname{div}(A\nabla u) = \sum_{i=1}^n \partial_{x_i}\Bigl( \sum_{j=1}^n a_{ij}(x)\, \partial_{x_j} u \Bigr).
> $$
>
> For $A = I$ it is the problem $(D)$ of [[§34 Weak Solutions of the Dirichlet Problem#^def-34-1|Definition §34.1]]. When the $a_{ij}$ are in $C^1(\overline{\Omega})$, a **classical solution** is a $u \in C^2(\overline{\Omega})$ satisfying both equations pointwise.

^def-34-4

> [!remark] Remark: Where the Elliptic Equation Comes From
> *(Not from lecture.)* Heat flows from hot to cold. In a homogeneous, isotropic material the heat flux is $\vec q = -\mu\nabla u$ (Fourier's law), and at equilibrium the heat produced in any region flows out through its boundary, $\operatorname{div}\vec q = f$; this is $-\mu\Delta u = f$, the equation of the remark [[§34 Weak Solutions of the Dirichlet Problem#^rem-34-1|Where the Equation Comes From]] above. In an inhomogeneous or anisotropic material — a composite, a crystal, layered rock — the conductivity depends on the position and on the direction, and Fourier's law becomes $\vec q = -A(x)\nabla u$ with a *conductivity matrix* $A(x)$. Equilibrium is again $\operatorname{div}\vec q = f$, which is $(E)$. Uniform ellipticity says that heat never flows uphill: $\vec q \cdot \nabla u = -(A\nabla u)\cdot\nabla u \le -\alpha |\nabla u|^2$, so the flux always has a component towards lower temperature, and the bound $\Lambda$ says the conductivity is finite.

^rem-34-7

> [!theorem] Proposition §34.3: Classical Solutions of $(E)$ Satisfy the Weak Equation
> Let $a_{ij} \in C^1(\overline{\Omega})$, $f$ continuous, and $u \in C^2(\overline{\Omega})$ a classical solution of $(E)$. Then
>
> $$
> \int_\Omega \bigl(A(x)\nabla u(x)\bigr) \cdot \nabla v(x)\, dx = \int_\Omega f(x)\, v(x)\, dx \qquad \text{for all } v \in C_c^2(\Omega).
> $$

^prop-34-3

> [!proof]+ Proof
> *(As in [[§34 Weak Solutions of the Dirichlet Problem#^prop-34-1|Proposition §34.1]].)* Let $F = A\nabla u$, the vector field with components $F_i = \sum_j a_{ij}\, \partial_{x_j} u \in C^1(\Omega)$, so that $\operatorname{div} F = -f$. For each $i$, [[§33 Sobolev Spaces and Weak Derivatives#^lem-33-2|Lemma §33.2]] with $g = F_i$ and $\varphi = v$ (its proof uses only $\varphi \in C^1$ with compact support in $\Omega$) gives $\int_\Omega \partial_{x_i} F_i\, v\, dx = -\int_\Omega F_i\, \partial_{x_i} v\, dx$. Summing over $i$,
>
> $$
> -\int_\Omega f\, v\, dx = \int_\Omega \operatorname{div} F\, v\, dx = -\int_\Omega F \cdot \nabla v\, dx = -\int_\Omega (A\nabla u) \cdot \nabla v\, dx .
> $$

^pf-34-3

*Uses:* [[§34 Weak Solutions of the Dirichlet Problem#^def-34-4|Def. §34.4]], [[§33 Sobolev Spaces and Weak Derivatives#^lem-33-2|§33.2]]

> [!definition] Definition §34.5: Weak Solution of $(E)$
> Let $f \in L^2(\Omega)$. A function $u \in H^1_0(\Omega)$ is a **weak solution** of $(E)$ if
>
> $$
> \int_\Omega \bigl(A(x)\nabla u(x)\bigr) \cdot \nabla v(x)\, dx = \int_\Omega f(x)\, v(x)\, dx \qquad \text{for all } v \in H^1_0(\Omega),
> $$
>
> where $\nabla u$, $\nabla v$ are [[§33 Sobolev Spaces and Weak Derivatives#^def-33-6|weak gradients]]. For $A = I$ this is [[§34 Weak Solutions of the Dirichlet Problem#^def-34-2|Definition §34.2]].

^def-34-5

> [!theorem] Theorem §34.4: General Elliptic Equations
> Let $\Omega \subset \mathbb{R}^n$ be a bounded domain and $A$ [[§34 Weak Solutions of the Dirichlet Problem#^def-34-3|uniformly elliptic]] on $\Omega$ ([[§34 Weak Solutions of the Dirichlet Problem#^def-34-3|Definition §34.3]]). For every $f \in L^2(\Omega)$ the problem $(E)$ has a unique [[§34 Weak Solutions of the Dirichlet Problem#^def-34-5|weak solution]] $u \in H^1_0(\Omega)$ ([[§34 Weak Solutions of the Dirichlet Problem#^def-34-5|Definition §34.5]]). For $A = I$ this is Theorem [[§34 Weak Solutions of the Dirichlet Problem#^thm-34-2|§34.2]].

^thm-34-4

> [!proof]+ Proof
> (Stated in lecture; Wu: “it goes through the same process.”) The weak formulation is Proposition [[§34 Weak Solutions of the Dirichlet Problem#^prop-34-3|§34.3]]. Let $B(v, u) = \int_\Omega (A(x)\nabla u) \cdot \nabla v\, dx$; it is bilinear. *Bounded:* $|(A\nabla u)\cdot\nabla v| \le \Lambda |\nabla u|\, |\nabla v|$, so $|B(v,u)| \le \Lambda \|u\|_{H^1_0} \|v\|_{H^1_0}$ as in Step 2 above. *Coercive:* $(A\xi)\cdot\xi = \xi^{\mathsf T} A\, \xi$ (a $1 \times 1$ matrix equals its transpose, and $(A\xi)\cdot\xi = \xi^{\mathsf T}A^{\mathsf T}\xi$), so $B(u,u) \ge \alpha \int_\Omega |\nabla u|^2 \ge \frac{\alpha}{1 + C_0} \|u\|_{H^1_0}^2$ by Step 3 above. The functional $\ell$ is as in Step 4. Theorem [[§32 Sesquilinear Forms and the Lax–Milgram Theorem#^thm-32-2|§32.2]] gives a unique $u$ with $\ell(v) = B(v, u)$ for all $v$, which is the weak equation. Unless $A$ is symmetric, $B$ is not symmetric, and the Riesz theorem alone does not apply.

^pf-34-4

*Uses:* [[§34 Weak Solutions of the Dirichlet Problem#^def-34-3|Def. §34.3]], [[§34 Weak Solutions of the Dirichlet Problem#^def-34-5|Def. §34.5]], [[§34 Weak Solutions of the Dirichlet Problem#^prop-34-3|§34.3]], [[§34 Weak Solutions of the Dirichlet Problem#^thm-34-2|§34.2]], [[§33 Sobolev Spaces and Weak Derivatives#^prop-33-5|§33.5]], [[§32 Sesquilinear Forms and the Lax–Milgram Theorem#^def-32-1|Def. §32.1]], [[§16 Means and Young's Inequality#^prop-16-1|§16.1]], [[§23 Cauchy–Schwarz and the Induced Norm#^thm-23-1|§23.1]], [[§33 Sobolev Spaces and Weak Derivatives#^cor-33-7|§33.7]], [[§32 Sesquilinear Forms and the Lax–Milgram Theorem#^thm-32-2|§32.2]]
