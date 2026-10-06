---
type: section
subject: "[[Fourier Series and PDEs]]"
chapter: 2
section: 23
powers: "2.7"
aliases: ["Powers 2.7"]
tags: [fourier-series-and-pdes, math341]
---
← [[§22 Example꞉ Convection]] · ↑ [[· 2 The Heat Equation]] · [[§24 Expansion in Series of Eigenfunctions]] →

*Powers, Section 2.7 · MAT 341 lectures 10.10, 10.17 · HW 7, HW 8.*

Every heat problem so far has ended in an eigenvalue problem $\phi'' + \lambda^2\phi = 0$ with two boundary conditions, and every solution has relied on the orthogonality of the eigenfunctions. For the convection problem ([[§22 Example꞉ Convection#^thm-22-1|Theorem §22.1]]) the eigenvalues are roots of a transcendental equation, and checking orthogonality by direct integration is already laborious. This section shows that orthogonality comes from the structure of the problem, through one integration by parts, for the whole class of regular Sturm–Liouville problems $(s\phi')' - q\phi + \lambda^2 p\phi = 0$; these are the eigenvalue problems of a rod whose conductivity, density and specific heat vary along its length ([[§25 Generalities on the Heat Conduction Problem|§25]]). It also collects what is known about their eigenvalues: they are real, simple and increase to infinity, and the $n$th eigenfunction has $n - 1$ zeros. In the language of linear algebra, the Sturm–Liouville operator is symmetric for a weighted inner product, and these facts are the infinite-dimensional counterpart of the spectral theorem for symmetric matrices.

## A Model Problem

In simple problems, separation of variables leads to eigenvalue problems of the form

$$
\begin{aligned}
\phi'' + \lambda^2\phi &= 0, && l < x < r, && (1) \\
\alpha_1\phi(l) - \alpha_2\phi'(l) &= 0, && && (2) \\
\beta_1\phi(r) + \beta_2\phi'(r) &= 0. && && (3)
\end{aligned}
$$

The eigenvalues can be found and the orthogonality of the eigenfunctions checked by direct calculation (as in [[§23 Sturm–Liouville Problems#^ex-23-3|Example §23.3]]), but an indirect calculation is easier and works for every choice of boundary conditions at once.

> [!theorem] Proposition §23.1: Orthogonality for φ″ + λ²φ = 0
> Let $\phi_n$ and $\phi_m$ be eigenfunctions of (1)–(3), where $(\alpha_1, \alpha_2) \ne (0, 0)$ and $(\beta_1, \beta_2) \ne (0, 0)$, corresponding to different eigenvalues $\lambda_n^2 \ne \lambda_m^2$. Then
>
> $$
> \int_l^r \phi_n(x)\phi_m(x)\,dx = 0 .
> $$
>
> *Powers: 2.7 (text)*

^prop-23-1

> [!proof]+ Proof
> The eigenfunctions satisfy
>
> $$
> \phi_n'' + \lambda_n^2\phi_n = 0, \qquad \phi_m'' + \lambda_m^2\phi_m = 0 ,
> $$
>
> and both satisfy the boundary conditions. Multiply the first equation by $\phi_m$ and the second by $\phi_n$, subtract, and move the terms containing $\phi_n\phi_m$ to the right:
>
> $$
> \phi_n''\phi_m - \phi_m''\phi_n = (\lambda_m^2 - \lambda_n^2)\phi_n\phi_m .
> $$
>
> The right side is a nonzero constant times the integrand of the orthogonality relation, so it is enough to show that the left side has integral zero. Integrate by parts (the eigenfunctions are solutions of a linear equation with constant coefficients, hence twice continuously differentiable on $[l, r]$):
>
> $$
> \int_l^r (\phi_n''\phi_m - \phi_m''\phi_n)\,dx = \Big[\phi_n'(x)\phi_m(x) - \phi_m'(x)\phi_n(x)\Big]_l^r - \int_l^r (\phi_n'\phi_m' - \phi_m'\phi_n')\,dx .
> $$
>
> The last integrand is identically zero, so
>
> $$
> (\lambda_m^2 - \lambda_n^2)\int_l^r \phi_n(x)\phi_m(x)\,dx = \Big[\phi_n'(x)\phi_m(x) - \phi_m'(x)\phi_n(x)\Big]_l^r .
> $$
>
> **The boundary terms vanish.** Both $\phi_n$ and $\phi_m$ satisfy the condition at $x = r$:
>
> $$
> \beta_1\phi_m(r) + \beta_2\phi_m'(r) = 0, \qquad \beta_1\phi_n(r) + \beta_2\phi_n'(r) = 0 .
> $$
>
> Read these as two homogeneous linear equations for the unknowns $\beta_1$, $\beta_2$. They have the nonzero solution $(\beta_1, \beta_2)$ (otherwise there would be no boundary condition), so the determinant of the system is zero:
>
> $$
> \phi_m(r)\phi_n'(r) - \phi_n(r)\phi_m'(r) = 0 .
> $$
>
> The same argument with the nonzero pair $(\alpha_1, -\alpha_2)$ gives $\phi_m(l)\phi_n'(l) - \phi_n(l)\phi_m'(l) = 0$. So the bracket vanishes at both ends, $(\lambda_m^2 - \lambda_n^2)\int_l^r \phi_n\phi_m\,dx = 0$, and since $\lambda_m^2 \ne \lambda_n^2$ the integral is zero.

^pf-23-1

## Regular Sturm–Liouville Problems

The same procedure works, with very little change, for the model eigenvalue problem that arises from separation of variables in a heat conduction problem with variable material properties ([[§25 Generalities on the Heat Conduction Problem|§25]]):

$$
\begin{aligned}
\big(s(x)\phi'(x)\big)' - q(x)\phi(x) + \lambda^2 p(x)\phi(x) &= 0, && l < x < r, && (5) \\
\alpha_1\phi(l) - \alpha_2\phi'(l) &= 0, && && (6) \\
\beta_1\phi(r) + \beta_2\phi'(r) &= 0. && && (7)
\end{aligned}
$$

To guarantee that eigenfunctions exist and that the integrations by parts are legitimate, Powers imposes conditions on the coefficients.

> [!definition] Definition §23.1: Regular Sturm–Liouville Problem; Eigenvalue; Eigenfunction
> The problem (5)–(7) is called a **regular Sturm–Liouville problem** if the following conditions are fulfilled:
> - (a) $s(x)$, $s'(x)$, $q(x)$ and $p(x)$ are continuous for $l \le x \le r$;
> - (b) $s(x) > 0$ and $p(x) > 0$ for $l \le x \le r$;
> - (c) the $\alpha$'s and $\beta$'s are nonnegative, and $\alpha_1^2 + \alpha_2^2 > 0$, $\beta_1^2 + \beta_2^2 > 0$;
> - (d) the parameter $\lambda$ occurs only where shown.
>
> A number $\lambda^2$ for which (5)–(7) has a solution $\phi$ that is not identically zero is an **eigenvalue**, and such a $\phi$ is an **eigenfunction** corresponding to $\lambda^2$. The function $p(x)$ is the **weight function**.
>
> *Powers: 2.7, Definition; Source: 341 lecture 10.10*

^def-23-1

> [!remark] Remark: What the Conditions Do
> - Condition (a) and the first half of (b) guarantee that (5) has solutions with continuous first and second derivatives on the closed interval: dividing by $s > 0$ gives $\phi'' + (s'/s)\phi' + \big((\lambda^2p - q)/s\big)\phi = 0$ with continuous coefficients, and [[§14 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-14-1|331 Thm. §14.1]] applies. In particular $s(l)$ and $s(r)$ must be positive, not zero; when $s$ vanishes at an end (Bessel's and Legendre's equations, [[§23 Sturm–Liouville Problems#^ex-23-2|Example §23.2]]) the problem is *singular*.
> - Condition (c) just says that there are two boundary conditions: $\alpha_1^2 + \alpha_2^2 = 0$ only if $\alpha_1 = \alpha_2 = 0$, which would be no condition. The signs are those of fixed-temperature, insulated and convective ends; they matter for the sign of the eigenvalues ([[§23 Sturm–Liouville Problems#^thm-23-5|Theorem §23.5]](c)).
> - The other requirements contribute to the properties below in ways that are not obvious.

^rem-23-1

> [!remark] Remark: Method — Putting an Equation in Sturm–Liouville Form
> A general second-order eigenvalue equation $a(x)\phi'' + b(x)\phi' + c(x)\phi + \mu\, w(x)\phi = 0$ with $a > 0$ can always be rewritten in the form (5):
> 1. Compute the integrating factor $s(x) = \exp\big(\int b(x)/a(x)\,dx\big)$, so that $s' = (b/a)s$.
> 2. Multiply the equation by $s/a$. Since $(s\phi')' = s\phi'' + (b/a)s\phi' = (s/a)(a\phi'' + b\phi')$, it becomes
>
> $$
> (s\phi')' + \frac{cs}{a}\,\phi + \mu\,\frac{ws}{a}\,\phi = 0 ,
> $$
>
> so $q = -cs/a$ and the weight is $p = ws/a$ (and $\mu = \lambda^2$).
> 3. Check conditions (a)–(d) of Definition §23.1 on the closed interval.
>
> For instance, $x(x\phi')' = \mu\phi$ ([[§23 Sturm–Liouville Problems#^ex-23-4|Example §23.4]]) is $x^2\phi'' + x\phi' - \mu\phi = 0$; here $b/a = 1/x$, $s = x$, and dividing by $x$ gives $(x\phi')' - \mu\,\frac1x\,\phi = 0$. Since the term in $\mu$ has $w = -1$, this is (5) with $\lambda^2 = -\mu$ and positive weight $p = 1/x$.
>
> *Source: 341 lecture 10.10*

^rem-23-2

> [!theorem] Theorem §23.2: Orthogonality of Eigenfunctions (Sturm–Liouville Theorem)
> The regular Sturm–Liouville problem has an infinite number of eigenfunctions $\phi_1, \phi_2, \ldots$, each corresponding to a different eigenvalue $\lambda_1^2, \lambda_2^2, \ldots$. If $n \ne m$, the eigenfunctions $\phi_n$ and $\phi_m$ are orthogonal with weight function $p(x)$:
>
> $$
> \int_l^r \phi_n(x)\phi_m(x)p(x)\,dx = 0, \qquad n \ne m .
> $$
>
> *Powers: 2.7, Theorem 1*

^thm-23-2

> [!proof]+ Proof
> Powers proves the orthogonality; the existence of infinitely many eigenvalues is part (a) of [[§23 Sturm–Liouville Problems#^thm-23-5|Theorem §23.5]], which he does not prove.
>
> The eigenfunctions satisfy
>
> $$
> (s\phi_n')' - q\phi_n + \lambda_n^2p\phi_n = 0, \qquad (s\phi_m')' - q\phi_m + \lambda_m^2p\phi_m = 0 .
> $$
>
> Multiply the first by $\phi_m$ and the second by $\phi_n$ and subtract. The terms containing $q$ cancel, and moving the term with $p\phi_n\phi_m$ to the other side gives
>
> $$
> (s\phi_n')'\phi_m - (s\phi_m')'\phi_n = (\lambda_m^2 - \lambda_n^2)p\phi_n\phi_m . \qquad (4)
> $$
>
> By condition (a), $s\phi_n'$ and $s\phi_m'$ are continuously differentiable on $[l, r]$, so both sides can be integrated from $l$ to $r$ and the left side integrated by parts:
>
> $$
> \int_l^r \big[(s\phi_n')'\phi_m - (s\phi_m')'\phi_n\big]\,dx = \Big[s\phi_n'\phi_m - s\phi_m'\phi_n\Big]_l^r - \int_l^r (s\phi_n'\phi_m' - s\phi_m'\phi_n')\,dx .
> $$
>
> The second integral is zero. By the determinant argument of [[§23 Sturm–Liouville Problems#^prop-23-1|Proposition §23.1]] (which uses only the boundary conditions, now (6) and (7)),
>
> $$
> \phi_n'(r)\phi_m(r) - \phi_m'(r)\phi_n(r) = 0, \qquad \phi_n'(l)\phi_m(l) - \phi_m'(l)\phi_n(l) = 0 ,
> $$
>
> so the bracket vanishes at both ends (multiplied by $s(r)$ and $s(l)$). Integrating (4) therefore gives $(\lambda_m^2 - \lambda_n^2)\int_l^r p\phi_n\phi_m\,dx = 0$, and since $\lambda_n^2 \ne \lambda_m^2$,
>
> $$
> \int_l^r p(x)\phi_n(x)\phi_m(x)\,dx = 0 .
> $$
>
> (The 10.10 lecture finishes the boundary step by noting that $\phi_n'(0)/\phi_n(0) = \alpha_1/\alpha_2 = \phi_m'(0)/\phi_m(0)$; the determinant argument avoids dividing by quantities that may be zero.)

^pf-23-2

*Uses:* [[§23 Sturm–Liouville Problems#^def-23-1|Def. §23.1]], [[§23 Sturm–Liouville Problems#^prop-23-1|§23.1]]

> [!remark]- Connections
> - Finite-dimensional version: eigenvectors of a symmetric matrix for distinct eigenvalues are orthogonal, [[§48★ Diagonalization of Symmetric Matrices#^thm-48-1|235 Thm. §48.1]], by the same one-line computation; for self-adjoint operators on an inner product space ([[§22 Self-Adjoint and Normal Operators#^ladr-7-10|LADR 7.10]]), and more generally normal ones, it is [[§22 Self-Adjoint and Normal Operators#^ladr-7-22|LADR 7.22]]. See the remark below for the dictionary.
> - $\langle f, g\rangle_p = \int_l^r f(x)g(x)p(x)\,dx$ is an inner product (a weighted version of [[§20 Definition and Examples#^ex-20-3|556 Ex. §20.3]] and [[§46 Inner Product Spaces#^ex-46-4|235 Ex. §46.4]]), and the theorem says that the eigenfunctions form an orthogonal set for it in the sense of [[§24 Orthonormal Sets and Bases#^def-24-1|556 Def. §24.1]].
> - Used in Electromagnetism: separation of variables in electrostatics — the separated equations as Sturm–Liouville problems, orthonormality, completeness and closure of their eigenfunctions, and the orthogonality of Bessel functions — [[§C6.2 Separation in Cartesian and Spherical Coordinates#^def-c6-2-1|EM Def. §C6.2.1]], [[§C6.2 Separation in Cartesian and Spherical Coordinates#^thm-c6-2-1|EM Theorem §C6.2.1]], [[§C6.3 Separation in Cylindrical and Polar Coordinates#^thm-c6-3-2|EM Theorem §C6.3.2]].
> - In several variables the integration by parts of the proof becomes Green's second identity, [[§17 The Divergence Theorem in Higher Dimensions and Green's Identities#^thm-17-3|452 Thm. §17.3]], which makes the Laplacian symmetric in the same way under Dirichlet or Neumann boundary conditions.

> [!remark] Remark: Self-Adjointness
> The 10.10 lecture labels the key step of the proof "self-adjoint". Write $L[\phi] = (s\phi')' - q\phi$. The integration by parts above shows, for any two twice continuously differentiable functions $\phi$, $\psi$ satisfying the boundary conditions (6) and (7),
>
> $$
> \int_l^r L[\phi]\,\psi\,dx - \int_l^r \phi\,L[\psi]\,dx = \Big[s(\phi'\psi - \phi\psi')\Big]_l^r = 0 .
> $$
>
> So the operator $\mathcal{L} = -\frac1p L$ satisfies $\langle \mathcal{L}\phi, \psi\rangle_p = \langle \phi, \mathcal{L}\psi\rangle_p$ for the weighted inner product, and the Sturm–Liouville problem is the eigenvalue problem $\mathcal{L}\phi = \lambda^2\phi$. This is the analogue of $(A\mathbf{x}) \cdot \mathbf{y} = \mathbf{x} \cdot (A\mathbf{y})$ for a symmetric matrix $A$: the boundary conditions are part of the operator, and they are exactly what makes the boundary terms vanish. Theorem §23.2, [[§23 Sturm–Liouville Problems#^prop-23-3|Proposition §23.3]] and the expansion theorem, [[§24 Expansion in Series of Eigenfunctions#^thm-24-2|Theorem §24.2]], are then the statements "eigenvectors for different eigenvalues are orthogonal", "the eigenvalues are real" and "the eigenvectors form a basis".
>
> *Source: 341 lecture 10.10*

^rem-23-3

## Properties of the Eigenvalues

Powers writes the eigenvalue as $\lambda^2$ and orders the eigenvalues, which presupposes that they are real. That follows from the same identity.

> [!theorem] Proposition §23.3: The Eigenvalues Are Real
> Even if complex numbers $\mu$ in place of $\lambda^2$ and complex-valued solutions $\phi$ are admitted, every eigenvalue of a regular Sturm–Liouville problem is real, and to each eigenvalue there corresponds a real-valued eigenfunction.
>
> *Powers: 2.7, implicit in Theorems 1 and 2 (the eigenvalues are written $\lambda^2$ and ordered)*

^prop-23-3

> [!proof]+ Proof
> Suppose $\phi \not\equiv 0$ is a complex-valued solution of $(s\phi')' - q\phi + \mu p\phi = 0$ satisfying (6) and (7), with $\mu \in \mathbb{C}$. The functions $s$, $q$, $p$ and the numbers $\alpha_i$, $\beta_i$ are real, so taking complex conjugates shows that $\bar\phi$ satisfies the same boundary conditions and $(s\bar\phi')' - q\bar\phi + \bar\mu p\bar\phi = 0$.
>
> Repeat the computation in the proof of [[§23 Sturm–Liouville Problems#^thm-23-2|Theorem §23.2]] with $\phi_n = \phi$, $\lambda_n^2 = \mu$ and $\phi_m = \bar\phi$, $\lambda_m^2 = \bar\mu$. Nothing in it used real values: (4) and the integration by parts hold for complex-valued functions, and the determinant argument at each end works because the pair $(\beta_1, \beta_2)$ (or $(\alpha_1, -\alpha_2)$) is a nonzero solution of the two equations. So
>
> $$
> (\bar\mu - \mu)\int_l^r p(x)\phi(x)\bar\phi(x)\,dx = 0 .
> $$
>
> Now $\phi\bar\phi = |\phi|^2 \ge 0$ is continuous and not identically zero, and $p > 0$, so $\int_l^r p|\phi|^2\,dx > 0$. Hence $\bar\mu = \mu$: the eigenvalue is real.
>
> With $\mu$ real, write $\phi = \phi_1 + i\phi_2$ with $\phi_1$, $\phi_2$ real. Since the equation and the boundary conditions have real coefficients, the real and imaginary parts of the equation and of the conditions separate (as in [[§14 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-14-6|331 Thm. §14.6]]), so $\phi_1$ and $\phi_2$ both solve the problem. They are not both identically zero, and the nonzero one is a real eigenfunction.

^pf-23-3

*Uses:* [[§23 Sturm–Liouville Problems#^thm-23-2|§23.2]], [[§23 Sturm–Liouville Problems#^def-23-1|Def. §23.1]], [[§14 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-14-6|331 Thm. §14.6]]

> [!remark]- Connections
> - The same argument for a self-adjoint operator, $\lambda\|v\|^2 = \langle Tv, v\rangle = \langle v, Tv\rangle = \bar\lambda\|v\|^2$: [[§22 Self-Adjoint and Normal Operators#^ladr-7-12|LADR 7.12]]. Matrix versions: part (a) of [[§48★ Diagonalization of Symmetric Matrices#^thm-48-3|235 Thm. §48.3]] (real symmetric) and [[§29 Systems of Linear Algebraic Equations; Linear Independence, Eigenvalues, Eigenvectors#^thm-29-5|331 Thm. §29.5]] (Hermitian).
> - Used in Electromagnetism: the separation constants of electrostatic boundary-value problems are real — [[§C6.2 Separation in Cartesian and Spherical Coordinates#^thm-c6-2-1|EM Theorem §C6.2.1]].

Powers also notes that any constant multiple of an eigenfunction is an eigenfunction, but that apart from a constant multiplier the eigenfunctions are unique.

> [!theorem] Proposition §23.4: Each Eigenvalue Has Only One Eigenfunction
> Any nonzero constant multiple of an eigenfunction of a regular Sturm–Liouville problem is an eigenfunction for the same eigenvalue. Conversely, if $\phi$ and $\psi$ are eigenfunctions corresponding to the same eigenvalue $\lambda^2$, then $\psi = c\phi$ for a constant $c$.
>
> *Powers: 2.7 (text)*

^prop-23-4

> [!proof]+ Proof
> The equation (5) and the conditions (6), (7) are linear and homogeneous, so $c\phi$ satisfies them whenever $\phi$ does.
>
> (Powers asserts the converse; here is why.) Let $\phi$ and $\psi$ be eigenfunctions for the same $\lambda^2$. Both satisfy (6), so by the determinant argument of [[§23 Sturm–Liouville Problems#^prop-23-1|Proposition §23.1]] at $x = l$, $\phi(l)\psi'(l) - \phi'(l)\psi(l) = 0$. This says that the vectors $(\phi(l), \phi'(l))$ and $(\psi(l), \psi'(l))$ are linearly dependent: there are constants $c_1$, $c_2$, not both zero, with
>
> $$
> c_1\phi(l) + c_2\psi(l) = 0, \qquad c_1\phi'(l) + c_2\psi'(l) = 0 .
> $$
>
> The function $\chi = c_1\phi + c_2\psi$ solves (5), which after division by $s > 0$ is a second-order linear equation with continuous coefficients on $[l, r]$ (extend them continuously a little past $l$), and $\chi(l) = \chi'(l) = 0$. By the uniqueness part of [[§14 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-14-1|331 Thm. §14.1]], $\chi \equiv 0$. If $c_2 = 0$, then $c_1 \ne 0$ and $\phi \equiv 0$, which is impossible for an eigenfunction; so $c_2 \ne 0$ and $\psi = -(c_1/c_2)\phi$.

^pf-23-4

*Uses:* [[§23 Sturm–Liouville Problems#^def-23-1|Def. §23.1]], [[§23 Sturm–Liouville Problems#^prop-23-1|§23.1]], [[§14 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-14-1|331 Thm. §14.1]]

> [!theorem] Theorem §23.5: Properties of the Eigenvalues
> - (a) The regular Sturm–Liouville problem has an infinite number of eigenvalues, and $\lambda_n^2 \to \infty$ as $n \to \infty$.
> - (b) If the eigenvalues are numbered in order, $\lambda_1^2 < \lambda_2^2 < \cdots$, then the eigenfunction corresponding to $\lambda_n^2$ has exactly $n - 1$ zeros in the interval $l < x < r$ (endpoints excluded).
> - (c) If $q(x) \ge 0$ and $\alpha_1$, $\alpha_2$, $\beta_1$, $\beta_2$ are all greater than or equal to zero, then all the eigenvalues are nonnegative.
>
> *Powers: 2.7, Theorem 2*

^thm-23-5

*Powers omits the proof. For Dirichlet conditions, part (c) follows from the Rayleigh quotient of [[§33★ Estimation of Eigenvalues#^prop-33-1|Proposition §33.1]] (Eq. (3)); the remark below extends that argument to all the boundary conditions of Definition §23.1. Parts (a) and (b) (Sturm's oscillation theory) are not proved anywhere in the vault.*

> [!remark] Remark: Why the Eigenvalues Are Nonnegative
> Let $\phi$ be a real eigenfunction for $\lambda^2$ ([[§23 Sturm–Liouville Problems#^prop-23-3|Proposition §23.3]]). Multiply (5) by $\phi$, integrate from $l$ to $r$, and integrate $\int (s\phi')'\phi\,dx$ by parts:
>
> $$
> \lambda^2\int_l^r p\phi^2\,dx = \int_l^r \big(s\phi'^2 + q\phi^2\big)\,dx - s(r)\phi(r)\phi'(r) + s(l)\phi(l)\phi'(l) .
> $$
>
> At $x = r$: if $\beta_2 > 0$, then $\phi'(r) = -(\beta_1/\beta_2)\phi(r)$ and $-s(r)\phi(r)\phi'(r) = s(r)(\beta_1/\beta_2)\phi(r)^2 \ge 0$; if $\beta_2 = 0$, then $\phi(r) = 0$ and the term is zero. Likewise at $x = l$: if $\alpha_2 > 0$, then $s(l)\phi(l)\phi'(l) = s(l)(\alpha_1/\alpha_2)\phi(l)^2 \ge 0$, and if $\alpha_2 = 0$ the term is zero. With $q \ge 0$ every term on the right is nonnegative, while $\int p\phi^2 > 0$; so $\lambda^2 \ge 0$. The quotient
>
> $$
> \lambda^2 = \frac{\int_l^r (s\phi'^2 + q\phi^2)\,dx + \text{boundary terms}}{\int_l^r p\phi^2\,dx}
> $$
>
> is the Rayleigh quotient; physically, the numerator measures how fast the temperature profile $\phi$ loses heat. Moreover $\lambda^2 = 0$ forces $\phi' \equiv 0$, so $0$ can be an eigenvalue only with a constant eigenfunction, which happens when $q \equiv 0$ and both ends are insulated ($\alpha_1 = \beta_1 = 0$).
>
> Theorem §23.5 on familiar problems: for $\phi'' + \lambda^2\phi = 0$, $\phi(0) = \phi(a) = 0$, the eigenvalues $(n\pi/a)^2$ are positive and increase to $\infty$, and $\sin(n\pi x/a)$ has the $n - 1$ zeros $x = ja/n$, $j = 1, \ldots, n - 1$. With $\phi'(0) = \phi'(a) = 0$ instead, the numbering starts with $\lambda_1^2 = 0$, $\phi_1 = 1$ (no zeros), and $\phi_n = \cos((n - 1)\pi x/a)$ has $n - 1$ zeros.

^rem-23-4

> [!remark]- Connections
> - Finite-dimensional analogue: a real symmetric $n \times n$ matrix has $n$ real eigenvalues and an orthonormal basis of eigenvectors, [[§48★ Diagonalization of Symmetric Matrices#^thm-48-3|235 Thm. §48.3]]; for self-adjoint operators this is the real spectral theorem, [[§23 Spectral Theorem#^ladr-7-29|LADR 7.29]]. Theorems §23.2 and §23.5 with the expansion theorem of [[§24 Expansion in Series of Eigenfunctions#^thm-24-2|§24]] are the infinite-dimensional version, in which "basis" means orthonormal basis in the sense of [[§24 Orthonormal Sets and Bases#^def-24-4|556 Def. §24.4]] and there are infinitely many eigenvalues, increasing to $\infty$.

## Examples

> [!example] Example §23.1: Recognizing Regular Sturm–Liouville Problems
> **(a)** The eigenvalue problems of [[§19 Example꞉ Fixed End Temperatures|§19]]–[[§22 Example꞉ Convection|§22]] are all regular Sturm–Liouville problems, as is (1)–(3). In particular, the convection problem
>
> $$
> \phi'' + \lambda^2\phi = 0, \quad 0 < x < a, \qquad \phi(0) = 0, \qquad h\phi(a) + \kappa\phi'(a) = 0
> $$
>
> is one, with $s(x) = p(x) = 1$, $q(x) = 0$, $\alpha_1 = 1$, $\alpha_2 = 0$, $\beta_1 = h$, $\beta_2 = \kappa$. All conditions of Definition §23.1 are met ($h$, $\kappa > 0$), so its eigenfunctions $\sin(\lambda_n x)$ are orthogonal on $0 < x < a$ with weight $1$, and its eigenvalues are positive.
>
> **(b)** A less trivial example is
>
> $$
> (x\phi')' + \lambda^2\Big(\frac1x\Big)\phi = 0, \quad 1 < x < 2, \qquad \phi(1) = 0, \quad \phi(2) = 0 .
> $$
>
> Here $s(x) = x$, $p(x) = 1/x$, $q(x) = 0$, and $\alpha_1 = \beta_1 = 1$, $\alpha_2 = \beta_2 = 0$. The functions $s$, $s' = 1$, $q$, $p$ are continuous on $[1, 2]$ and $s$, $p$ are positive there, so this is a regular Sturm–Liouville problem, and the orthogonality relation is
>
> $$
> \int_1^2 \phi_n(x)\phi_m(x)\,\frac1x\,dx = 0, \qquad n \ne m .
> $$
>
> The conclusions of Theorems §23.2 and §23.5 hold for both problems. The eigenvalues of (b) are found in Example §23.4.
>
> *Powers: 2.7, Examples 1 and 2*

^ex-23-1

> [!example] Example §23.2: Bessel's and Legendre's Equations
> The lecture lists three choices of coefficients in (5):
> - $s = 1$, $q = 0$, $p = 1$: $\phi'' + \lambda^2\phi = 0$, the equation of the standard heat problems.
> - $s = x$, $q = \nu^2/x$, $p = x$: $(x\phi')' - \frac{\nu^2}{x}\phi + \lambda^2x\phi = 0$. Multiplying by $x$ gives $x^2\phi'' + x\phi' + (\lambda^2x^2 - \nu^2)\phi = 0$, **Bessel's equation** of order $\nu$ ([[§45★ Bessel's Equation#^def-45-1|Definition §45.1]]).
> - $s = 1 - x^2$, $q = 0$, $p = 1$: $\big((1 - x^2)\phi'\big)' + \lambda^2\phi = 0$, **Legendre's equation** ([[§49★ Spherical Coordinates; Legendre Polynomials#^def-49-2|Definition §49.2]]).
>
> Are they regular? The first is, on any interval with the boundary conditions (6), (7). Bessel's equation on $0 < x < a$ (the radius of a disk or cylinder) is not: $s(0) = 0$ violates (b), and for $\nu \ne 0$, $q = \nu^2/x$ is not continuous at $0$. On $c < x < a$ with $c > 0$ (an annulus) it is regular. Legendre's equation on $-1 < x < 1$ is not regular either, since $s(\pm1) = 0$. These are **singular** Sturm–Liouville problems; the boundary condition at a singular end is replaced by a boundedness condition, and orthogonality survives because the factor $s$ kills the boundary term there (Powers' Exercise 2.7.6). Their eigenfunctions are the Bessel functions and Legendre polynomials of Chapter 5.
>
> *Source: 341 lecture 10.10*

^ex-23-2

> [!example] Example §23.3: The Convection Eigenfunctions by Direct Integration
> Let $\lambda_n$ be the $n$th positive solution of the equation $\tan(a\lambda) = -\kappa\lambda/h$, so that $\phi_n = \sin(\lambda_n x)$ are the eigenfunctions of Example §23.1(a) ([[§22 Example꞉ Convection#^thm-22-1|Theorem §22.1]]). **(a)** Verify that
>
> $$
> \int_0^a \sin^2(\lambda_n x)\,dx = \frac a2 + \frac{\kappa}{h}\,\frac{\cos^2(\lambda_n a)}{2} .
> $$
>
> **(b)** Prove directly that $\int_0^a \sin(\lambda_n x)\sin(\lambda_m x)\,dx = 0$ for $n \ne m$.
>
> The eigenvalue equation, multiplied by $\cos(\lambda_j a)$, reads
>
> $$
> \sin(\lambda_j a) = -\frac{\kappa}{h}\,\lambda_j\cos(\lambda_j a) \qquad (j = n, m) . \qquad (\ast)
> $$
>
> **(a)** By $\sin^2\alpha = \frac12(1 - \cos 2\alpha)$ and $\sin 2\alpha = 2\sin\alpha\cos\alpha$,
>
> $$
> \int_0^a \sin^2(\lambda_n x)\,dx = \frac a2 - \frac{\sin(2\lambda_n a)}{4\lambda_n} = \frac a2 - \frac{\sin(\lambda_n a)\cos(\lambda_n a)}{2\lambda_n} = \frac a2 + \frac{\kappa}{h}\,\frac{\cos^2(\lambda_n a)}{2} ,
> $$
>
> using $(\ast)$ in the last step.
>
> **(b)** By $\sin\alpha\sin\beta = \frac12\big(\cos(\alpha - \beta) - \cos(\alpha + \beta)\big)$, for $\lambda_n \ne \lambda_m$,
>
> $$
> \int_0^a \sin(\lambda_n x)\sin(\lambda_m x)\,dx = \frac{\sin\big((\lambda_n - \lambda_m)a\big)}{2(\lambda_n - \lambda_m)} - \frac{\sin\big((\lambda_n + \lambda_m)a\big)}{2(\lambda_n + \lambda_m)} .
> $$
>
> Write $S_j = \sin(\lambda_j a)$ and $C_j = \cos(\lambda_j a)$. By the addition formulas and $(\ast)$,
>
> $$
> S_nC_m - C_nS_m = -\frac{\kappa}{h}(\lambda_n - \lambda_m)C_nC_m, \qquad S_nC_m + C_nS_m = -\frac{\kappa}{h}(\lambda_n + \lambda_m)C_nC_m ,
> $$
>
> so the integral equals
>
> $$
> \frac{S_nC_m - C_nS_m}{2(\lambda_n - \lambda_m)} - \frac{S_nC_m + C_nS_m}{2(\lambda_n + \lambda_m)} = -\frac{\kappa}{h}\,\frac{C_nC_m}{2} + \frac{\kappa}{h}\,\frac{C_nC_m}{2} = 0 .
> $$
>
> Part (b) is Proposition §23.1 checked by hand: the direct route needs the eigenvalue equation in a specific algebraic form, while the Sturm–Liouville argument needs only that both functions satisfy the same boundary conditions (the answer key accepts that argument for half of the credit). Part (a) shows that the eigenfunctions are *not* normalized like $\sin(n\pi x/a)$: $\int_0^a \sin^2 \ne a/2$ in general, which matters for the coefficients in [[§24 Expansion in Series of Eigenfunctions#^ex-24-1|Example §24.1]].
>
> *Source: 341 HW 7, Problem 1; Powers: Exercise 2.6.10*

^ex-23-3

Several problems in the course have $s(x)p(x) = 1$, and then one substitution reduces the equation to $\psi'' + \lambda^2\psi = 0$.

> [!remark] Remark: Method — The Substitution y = ∫dx/s When sp = 1
> Suppose $q = 0$ and $s(x)p(x) = 1$, so that the equation is $(s\phi')' + \lambda^2\frac1s\phi = 0$ on $l < x < r$.
> 1. Introduce the new variable $y = \int_l^x \frac{d\xi}{s(\xi)}$, which runs from $0$ to $Y = \int_l^r \frac{d\xi}{s(\xi)}$, and write $\phi(x) = \psi(y)$.
> 2. Since $dy/dx = 1/s$, the chain rule gives $s\phi' = \psi'(y)$ and $(s\phi')' = \psi''(y)/s$, so the equation becomes $\psi''/s + \lambda^2\psi/s = 0$, that is,
>
> $$
> \psi''(y) + \lambda^2\psi(y) = 0, \qquad 0 < y < Y .
> $$
>
> 3. Transfer the boundary conditions: $\phi(l) = \psi(0)$, $\phi(r) = \psi(Y)$, $s\phi' = \psi'$.
> 4. Solve the constant-coefficient problem; for $\phi(l) = \phi(r) = 0$ the result is $\lambda_n = n\pi/Y$ and $\phi_n(x) = \sin\big(n\pi y(x)/Y\big)$.
>
> The weight is then the Jacobian of the substitution, $p\,dx = dx/s = dy$, so orthogonality with weight $p$ in $x$ is ordinary orthogonality in $y$. Any function of the form $A + By$ works as the new variable (the course also used $y = 1 - e^{-x}$ and $1 - e^{-2x}$).
>
> *Source: 341 lecture 10.17; 341 HW 8, Problem 1(b) (hint)*

^rem-23-5

> [!example] Example §23.4: An Eigenvalue Problem on 1 < x < b
> Separate variables, $w(x, t) = \phi(x)T(t)$, in the problem
>
> $$
> \frac{\partial w}{\partial t} = x\frac{\partial}{\partial x}\Big(x\frac{\partial w}{\partial x}\Big), \quad 1 < x < b, \ t > 0, \qquad w(1, t) = 0, \quad w(b, t) = 0 ,
> $$
>
> with $T'(t) = \mu T(t)$, and find all pairs $(\mu, \phi)$ with $\phi \not\equiv 0$.
>
> **The eigenvalue problem.** Substituting, $\phi T' = x(x\phi')'T$, so $\mu = T'/T = x(x\phi')'/\phi$ and
>
> $$
> x(x\phi'(x))' = \mu\phi(x), \quad 1 < x < b, \qquad \phi(1) = 0, \quad \phi(b) = 0 ,
> $$
>
> because $\phi(1)T(t) = 0$ for all $t$ and $T \not\equiv 0$ (and likewise at $b$). Dividing by $x$ gives the Sturm–Liouville form $(x\phi')' - \mu\frac1x\phi = 0$: $s = x$, $p = 1/x$, $q = 0$, and with $\mu = -\lambda^2$ and $b = 2$ this is Example §23.1(b).
>
> **Substitution.** Since $sp = 1$, put $\psi(\ln x) = \phi(x)$, i.e. $y = \ln x = \int_1^x d\xi/\xi$. Then $\psi'(\ln x) = x\phi'(x)$ and $\psi''(\ln x) = x(x\phi'(x))'$, so
>
> $$
> \psi''(y) = \mu\psi(y), \quad 0 < y < \ln b, \qquad \psi(0) = 0, \quad \psi(\ln b) = 0 .
> $$
>
> **Cases.**
> - $\mu = \nu^2 > 0$: $\psi = Ae^{\nu y} + Be^{-\nu y}$. Then $\psi(0) = A + B = 0$ and $\psi(\ln b) = A(b^\nu - b^{-\nu}) = 0$. Since $b > 1$ and $\nu > 0$, $b^\nu \ne b^{-\nu}$, so $A = B = 0$: no nonzero solution.
> - $\mu = 0$: $\psi = Ay + B$, and $\psi(0) = B = 0$, $\psi(\ln b) = A\ln b = 0$ give $A = 0$: no nonzero solution.
> - $\mu = -\lambda^2 < 0$: $\psi = A\cos(\lambda y) + B\sin(\lambda y)$. Then $\psi(0) = A = 0$, and $\psi(\ln b) = B\sin(\lambda\ln b) = 0$ has a solution with $B \ne 0$ exactly when $\lambda\ln b = n\pi$.
>
> So the eigenvalues and eigenfunctions are
>
> $$
> \lambda_n^2 = \Big(\frac{n\pi}{\ln b}\Big)^2, \qquad \phi_n(x) = \sin\Big(\frac{n\pi\ln x}{\ln b}\Big), \qquad n = 1, 2, \ldots ,
> $$
>
> with $\mu_n = -\lambda_n^2$ and $T_n(t) = e^{-\lambda_n^2t}$. For $b = 2$ (Powers' Example 2): $\lambda_1^2 = (\pi/\ln 2)^2 \approx 20.54$, $\lambda_2^2 \approx 82.17$, $\lambda_3^2 \approx 184.88$.
>
> **Checking the theorems.** The eigenvalues are positive and increase to $\infty$ (Theorem §23.5(a), (c)). $\phi_n$ vanishes where $\ln x/\ln b = j/n$, that is at $x = b^{j/n}$, $j = 1, \ldots, n - 1$: exactly $n - 1$ zeros in $1 < x < b$ (Theorem §23.5(b)), but not equally spaced (figure). Orthogonality with weight $1/x$ can be checked directly, as Powers' Exercise 2.7.1 asks: with $y = \ln x$, $dx/x = dy$,
>
> $$
> \int_1^b \phi_n(x)\phi_m(x)\,\frac{dx}{x} = \int_0^{\ln b} \sin\Big(\frac{n\pi y}{\ln b}\Big)\sin\Big(\frac{m\pi y}{\ln b}\Big)\,dy = 0, \qquad n \ne m .
> $$
>
> *Source: 341 HW 8, Problem 1(a)–(b); Powers: 2.7, Example 2*

^ex-23-4

![[m341-23-1.svg]]
*The first three eigenfunctions $\phi_n(x) = \sin(n\pi\ln x/\ln b)$ of Example §23.4, drawn for $b = 8$. As Theorem §23.5(b) predicts, $\phi_n$ has $n - 1$ zeros in $1 < x < 8$, at $x = 8^{j/n}$: $2\sqrt2$ for $n = 2$, and $2$, $4$ for $n = 3$. The zeros crowd toward the left end, where the weight $1/x$ is largest.*
