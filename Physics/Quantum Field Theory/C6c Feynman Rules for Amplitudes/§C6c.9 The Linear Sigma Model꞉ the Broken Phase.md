---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C6c
section: C6c.9
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C6c.8 The Linear Sigma Model꞉ Fields with an Internal Index]] · ↑ [[· C6c Feynman Rules for Amplitudes]] · [[§C6c.10 The Linear Sigma Model꞉ Explicit Symmetry Breaking]] →

*Sources: PHY 513, Problem Set 10 ("Scattering Processes"), Problem 1(b)–(c) (statement, Larsen; the user's solution, 2026-11-13) · Peskin & Schroeder, An Introduction to Quantum Field Theory, Problem 4.3(b)–(c), pp. 127–128 (page images checked) · the homes cited in each box.*

[[§C6c.8 The Linear Sigma Model꞉ Fields with an Internal Index|§C6c.8]] treated the linear sigma model ([[§C6c.8 The Linear Sigma Model꞉ Fields with an Internal Index#^mod-c6c-8-1|Model §C6c.8.1]]) for $m^2 > 0$: $N$ fields of mass $m$, one quartic vertex. This section takes $m^2 = -\mu^2 < 0$ (Problem 1(b)–(c)). The quadratic term $+\frac12\mu^2\Phi^i\Phi^i$ of $\mathcal L$ then has the wrong sign for a mass term, $\Phi = 0$ is not the minimum of the potential, and the expansion in particles has to be made around a minimum. The section finds the minima ([[§C6c.9 The Linear Sigma Model꞉ the Broken Phase#^thm-c6c-9-1|Theorem §C6c.9.1]]), rewrites the Lagrangian in fields $\pi^i$, $\sigma$ that vanish at one of them ([[§C6c.9 The Linear Sigma Model꞉ the Broken Phase#^def-c6c-9-2|Def. §C6c.9.2]], [[§C6c.9 The Linear Sigma Model꞉ the Broken Phase#^thm-c6c-9-2|Theorem §C6c.9.2]]), reads off the masses and the Feynman rules ([[§C6c.9 The Linear Sigma Model꞉ the Broken Phase#^thm-c6c-9-4|Theorem §C6c.9.4]], [[§C6c.9 The Linear Sigma Model꞉ the Broken Phase#^thm-c6c-9-5|Theorem §C6c.9.5]]), computes $\pi\pi \to \pi\pi$ at order $\lambda$ ([[§C6c.9 The Linear Sigma Model꞉ the Broken Phase#^thm-c6c-9-6|Theorem §C6c.9.6]]) and shows that this amplitude vanishes at threshold and, for one pion, also at first order in the momenta ([[§C6c.9 The Linear Sigma Model꞉ the Broken Phase#^thm-c6c-9-7|Theorem §C6c.9.7]], [[§C6c.9 The Linear Sigma Model꞉ the Broken Phase#^thm-c6c-9-8|Theorem §C6c.9.8]]). The model with an added term $a\Phi^N$ is [[§C6c.10 The Linear Sigma Model꞉ Explicit Symmetry Breaking|§C6c.10]].

**The mathematical picture.** The potential depends on the field vector $\Phi = (\Phi^1, \dots, \Phi^N) \in \mathbb R^N$ only through its length, so its set of minima is invariant under $O(N)$ ([[§11 Topological Groups and Classical Matrix Groups#^def-11-7|591 Def. §11.7]]): it is the sphere $S^{N-1}$ of radius $v$ ([[§34 Retractions and Fixed Points#^def-34-3|590 Def. §34.3]], scaled by $v$), not a point. Every point of the sphere is a minimum, and a rotation carries any one of them into any other (for $N = 3$: [[§13 Group Actions and Orbit Spaces#^ex-13-7|591 Example §13.7]]). Perturbation theory needs one point to expand around; the problem chooses the point $(0, \dots, 0, v)$ on the $N$-th axis. The new fields are the coordinates of $\Phi$ measured from that point: $\sigma$ along the radial direction, $\pi^1, \dots, \pi^{N-1}$ along the $N - 1$ directions tangent to the sphere. What is still visible of the symmetry in the Lagrangian written in $\pi$ and $\sigma$: the $\pi$'s enter only through $\pi^i\pi^i$ and $\partial_\mu\pi^i\,\partial^\mu\pi^i$, so it is invariant under the rotations of the $N - 1$ fields $\pi^i$ among themselves, the group $O(N - 1)$.

![[ph-qft-c6c-9-1.svg]]
*The potential for $N = 2$ (field space is the plane of $\Phi^1$ and $\Phi^N = \Phi^2$). (a) $a = 0$: the level curves are circles, the minima form the circle $\Phi^i\Phi^i = v^2$ (blue); at the chosen point $(0, v)$ the field $\sigma$ measures the radial direction and $\pi$ the direction along the circle ([[§C6c.9 The Linear Sigma Model꞉ the Broken Phase#^thm-c6c-9-1|Theorem §C6c.9.1]], [[§C6c.9 The Linear Sigma Model꞉ the Broken Phase#^def-c6c-9-2|Def. §C6c.9.2]]). (b) The potential along the $\Phi^N$ axis without and with the term $-a\Phi^N$. (c) $a > 0$: one minimum, on the positive $\Phi^N$ axis ([[§C6c.10 The Linear Sigma Model꞉ Explicit Symmetry Breaking#^thm-c6c-10-2|Theorem §C6c.10.2]]). Added figure; drawn for $a = 0.25\,\mu^3/\sqrt\lambda$.*

**Setup and scope.** [[§C6c.8 The Linear Sigma Model꞉ Fields with an Internal Index#^mod-c6c-8-1|Model §C6c.8.1]] with $m^2 = -\mu^2 < 0$, $\lambda > 0$; statements about the potential are classical (constant fields); the particle content and the Feynman rules are those of the Lagrangian rewritten in $\pi$, $\sigma$, an instance of [[§C6a.0 Setups and Observables#^mod-c6a-0-3|Model §C6a.0.3]] with $N$ fields, treated at the lowest order, with free relativistic states of the fields $\hat\pi^i$, $\hat\sigma$ over their free vacuum for the in and out states ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^pr-c6b-1-3|Principle §C6b.1.3]]). *Conventions:* as in §C6c.8; from [[§C6c.9 The Linear Sigma Model꞉ the Broken Phase#^def-c6c-9-2|Def. §C6c.9.2]] on, the index of $\pi^i$ runs over $1, \dots, N - 1$ and is summed when repeated; $v$, $\mu$, $\sigma$, $\pi^i$ as defined below ([[§C6c.9 The Linear Sigma Model꞉ the Broken Phase#^cau-c6c-9-1|Caution: Four letters with other meanings]]).

## The minima of the potential

> [!definition] Definition §C6c.9.1: The Potential of the Fields
> For a Lagrangian $\mathcal L = \frac12\,\partial_\mu\Phi^i\,\partial^\mu\Phi^i - V(\Phi)$ with $V$ a function of the fields without derivatives, $V$ is the **potential**: the non-derivative part of $-\mathcal L$. For fields constant in space and time the derivative terms vanish and the Hamiltonian density ([[§C1b.4 Hamiltonian Field Theory#^def-c1b-4-2|Def. §C1b.4.2]]) is $\mathcal H = V(\Phi)$: the potential is the energy density of a constant field. For [[§C6c.8 The Linear Sigma Model꞉ Fields with an Internal Index#^mod-c6c-8-1|Model §C6c.8.1]],
>
> $$
> V(\Phi) = \frac12\,m^2\,\Phi^i\Phi^i + \frac\lambda4\bigl(\Phi^i\Phi^i\bigr)^2 .
> $$
>
> It contains the mass term as well as the interaction potential $V_{\rm int}$ of Model §C6c.8.1, 3.
>
> *Source: PHY 513, Problem Set 10, Problem 1(b) (the user's solution: "For constant fields the potential is the non-derivative part of $-\mathcal L$") · PS Problem 4.3, p. 127 ("For (classical) field configurations of $\Phi^i(x)$ that are constant in space and time, this term gives the only contribution to $H$; hence, $V$ is the field potential energy")*

^def-c6c-9-1

> [!theorem] Theorem §C6c.9.1: The Minima of the Potential for m² < 0
> Let $m^2 = -\mu^2 < 0$ and $\lambda > 0$ in the potential of [[§C6c.9 The Linear Sigma Model꞉ the Broken Phase#^def-c6c-9-1|Def. §C6c.9.1]]. It depends on the fields only through $\rho^2 \equiv \Phi^i\Phi^i$, the squared length of the field vector:
>
> $$
> V = -\frac12\,\mu^2\rho^2 + \frac\lambda4\,\rho^4 , \qquad \rho \ge 0 .
> $$
>
> 1. Its stationary points in $\rho$ are $\rho = 0$, with $V = 0$, and $\rho = \mu/\sqrt\lambda$, with $V = -\dfrac{\mu^4}{4\lambda} < 0$.
> 2. The minimum is attained for every constant field with
>
> $$
> \Phi^i\Phi^i = v^2 , \qquad v \equiv \frac{\mu}{\sqrt\lambda} ,
> $$
>
> a sphere $S^{N-1}$ of radius $v$ in field space (for $N = 2$ a circle, for $N = 1$ the two points $\pm v$).
> 3. $\Phi = 0$ is not the minimum.
>
> *Model:* [[§C6c.8 The Linear Sigma Model꞉ Fields with an Internal Index#^mod-c6c-8-1|Model §C6c.8.1]] with $m^2 = -\mu^2 < 0$; *applies:* the classical potential of constant fields; exact.
>
> *Source: PHY 513, Problem Set 10, Problem 1(b) (the user's solution) · PS Problem 4.3(b), p. 128 ("In this case, $V$ has a local maximum, rather than a minimum, at $\Phi^i = 0$")*

^thm-c6c-9-1

> [!derivation]- Derivation
> **Step 1** (the potential). For constant fields the potential is the non-derivative part of $-\mathcal L$ ([[§C6c.9 The Linear Sigma Model꞉ the Broken Phase#^def-c6c-9-1|Def. §C6c.9.1]]),
>
> $$
> V(\Phi) = \frac12\,m^2\,\Phi^i\Phi^i + \frac\lambda4\bigl(\Phi^i\Phi^i\bigr)^2 ,
> $$
>
> with $\lambda > 0$.
>
> **Step 2** (one variable). It depends on the components only through $\rho^2 \equiv \Phi^i\Phi^i$, the squared length of the field vector, so with $m^2 = -\mu^2$
>
> $$
> V = -\frac12\,\mu^2\rho^2 + \frac\lambda4\,\rho^4 , \qquad \rho \ge 0 ,
> $$
>
> and minimizing $V$ over all $\Phi$ is the same as minimizing it over $\rho$.
>
> **Step 3** (stationary points). Differentiating,
>
> $$
> V'(\rho) = -\mu^2\rho + \lambda\rho^3 = \lambda\rho\Bigl(\rho^2 - \frac{\mu^2}{\lambda}\Bigr) ,
> $$
>
> so $V'(\rho) = 0$ at $\rho = 0$ and at $\rho = \mu/\sqrt\lambda$.
>
> **Step 4** (the values). Plugging these into $V$,
>
> $$
> V(0) = 0 , \qquad V\Bigl(\frac{\mu}{\sqrt\lambda}\Bigr) = -\frac12\,\mu^2\,\frac{\mu^2}{\lambda} + \frac\lambda4\,\frac{\mu^4}{\lambda^2} = -\frac{\mu^4}{4\lambda} < 0 ,
> $$
>
> so $\rho = 0$ is not the minimum, and the minimum is at $\rho = v \equiv \mu/\sqrt\lambda$.
>
> **Step 5** (all minima). The minimum is therefore attained for any constant field with $\Phi^i\Phi^i = v^2$.
>
> **What the derivation shows.**
> - $\lambda > 0$ is used: $V \to +\infty$ for $\rho \to \infty$, so the smallest value is taken at a stationary point, and Step 4 decides between the two.
> - The condition fixes only the length of $\Phi$; its direction is free. The choice of a direction is made in [[§C6c.9 The Linear Sigma Model꞉ the Broken Phase#^def-c6c-9-2|Def. §C6c.9.2]].
> - For $m^2 > 0$ the same computation gives $V'(\rho) = \rho(m^2 + \lambda\rho^2)$, zero only at $\rho = 0$: the setting of §C6c.8.

^der-c6c-9-1

*Uses:* [[§C6c.9 The Linear Sigma Model꞉ the Broken Phase#^def-c6c-9-1|Def. §C6c.9.1]]

## The fields π and σ

> [!definition] Definition §C6c.9.2: The Fields π and σ
> Choose the minimum of [[§C6c.9 The Linear Sigma Model꞉ the Broken Phase#^thm-c6c-9-1|Theorem §C6c.9.1]] along the $N$-th direction, $\Phi = (0, \dots, 0, v)$, and write
>
> $$
> \Phi^i = \pi^i \quad (i = 1, \dots, N - 1) , \qquad \Phi^N = v + \sigma ,
> $$
>
> with $v$ a constant. The $N - 1$ fields $\pi^i$ are the **pion fields** and $\sigma$ is the **sigma field**; both vanish at the chosen minimum. For $N = 2$ there is a single pion field.
>
> *Model:* [[§C6c.8 The Linear Sigma Model꞉ Fields with an Internal Index#^mod-c6c-8-1|Model §C6c.8.1]]; *applies:* a change of field variables, valid for any constant $v$ (used with the $v$ of Theorem §C6c.9.1 here and with that of [[§C6c.10 The Linear Sigma Model꞉ Explicit Symmetry Breaking#^thm-c6c-10-2|Theorem §C6c.10.2]] in §C6c.10).
>
> *Source: PHY 513, Problem Set 10, Problem 1(b) (statement, Larsen: "Choose the vacuum along the $N$'th direction and write $\Phi^i = \pi^i$ ($i = 1, \dots, N - 1$), $\Phi^N = v + \sigma$") · PS Problem 4.3(b), p. 128 ("By rotational invariance, we can consider this shift to be in the $N$th direction … where $v$ is a constant chosen to minimize $V$")*

^def-c6c-9-2

> [!caution] Caution: Four letters with other meanings
> In this section and the next, $\pi^i$ is a field, not the canonical momentum density of [[§C1b.4 Hamiltonian Field Theory#^def-c1b-4-1|Def. §C1b.4.1]]; $\sigma$ is a field, not a cross section; $\mu$ is the parameter of $m^2 = -\mu^2$ with the dimension of a mass, not a Lorentz index and not the cubic coupling of the $\Phi\phi^2$ theory ([[§C6b.6 Decay Kinematics#^mod-c6b-6-4|Model §C6b.6.4]]); $v$ is the length of the field at the minimum, not a velocity.
>
> *Source: PS Problem 4.3(b), p. 128 ("The notation $\pi^i$ suggests a pion field and should not be confused with a canonical momentum") · the other three written here*

^cau-c6c-9-1

> [!theorem] Theorem §C6c.9.2: The Lagrangian in π and σ
> With $m^2 = -\mu^2$ and the fields of [[§C6c.9 The Linear Sigma Model꞉ the Broken Phase#^def-c6c-9-2|Def. §C6c.9.2]], the Lagrangian of [[§C6c.8 The Linear Sigma Model꞉ Fields with an Internal Index#^mod-c6c-8-1|Model §C6c.8.1]] is:
> 1. for any constant $v$,
>
> $$
> \begin{aligned}
> \mathcal L ={}& \Bigl[\frac12\,\partial_\mu\pi^i\,\partial^\mu\pi^i + \frac12\bigl(\mu^2 - \lambda v^2\bigr)\pi^i\pi^i - \frac\lambda4\bigl(\pi^i\pi^i\bigr)^2\Bigr] \\
> &+ \Bigl[\frac12\,\partial_\mu\sigma\,\partial^\mu\sigma + v\bigl(\mu^2 - \lambda v^2\bigr)\sigma + \frac12\bigl(\mu^2 - 3\lambda v^2\bigr)\sigma^2 - \lambda v\,\sigma^3 - \frac\lambda4\,\sigma^4\Bigr] \\
> &+ \Bigl[-\lambda v\,\pi^i\pi^i\,\sigma - \frac\lambda2\,\pi^i\pi^i\,\sigma^2\Bigr] + \frac12\,\mu^2v^2 - \frac\lambda4\,v^4 ;
> \end{aligned}
> $$
>
> 2. at the minimum, $v = \mu/\sqrt\lambda$, i.e. $\lambda v^2 = \mu^2$,
>
> $$
> \begin{aligned}
> \mathcal L ={}& \Bigl[\frac12\,\partial_\mu\pi^i\,\partial^\mu\pi^i - \frac\lambda4\bigl(\pi^i\pi^i\bigr)^2\Bigr] + \Bigl[\frac12\,\partial_\mu\sigma\,\partial^\mu\sigma - \frac12\,(2\mu^2)\,\sigma^2 - \lambda v\,\sigma^3 - \frac\lambda4\,\sigma^4\Bigr] \\
> &+ \Bigl[-\lambda v\,\pi^i\pi^i\,\sigma - \frac\lambda2\,\pi^i\pi^i\,\sigma^2\Bigr] + \frac{\mu^4}{4\lambda} .
> \end{aligned}
> $$
>
> The brackets collect the terms with only $\pi^i$, only $\sigma$, and both; the last term is a constant. The $\pi^i$ enter only through $\pi^i\pi^i$ and $\partial_\mu\pi^i\,\partial^\mu\pi^i$.
>
> *Model:* [[§C6c.8 The Linear Sigma Model꞉ Fields with an Internal Index#^mod-c6c-8-1|Model §C6c.8.1]] with $m^2 = -\mu^2$; *applies:* an identity between Lagrangians (a change of variables), exact; part 1 for every constant $v$, part 2 for $v = \mu/\sqrt\lambda$.
>
> *Source: PHY 513, Problem Set 10, Problem 1(b) (the user's solution; the form of part 1, with $v$ left general, is reused in Problem 1(d): [[§C6c.10 The Linear Sigma Model꞉ Explicit Symmetry Breaking#^thm-c6c-10-3|Theorem §C6c.10.3]]) · checked with `qft-C/tools/hw10/verify.py`*

^thm-c6c-9-2

> [!derivation]- Derivation
> **Step 1** (the Lagrangian). With $m^2 = -\mu^2$ the Lagrangian is
>
> $$
> \mathcal L = \frac12\,\partial_\mu\Phi^i\,\partial^\mu\Phi^i + \frac12\,\mu^2\,\Phi^i\Phi^i - \frac\lambda4\bigl(\Phi^i\Phi^i\bigr)^2 .
> $$
>
> **Step 2** (substitute). Substituting $\Phi^i = \pi^i$ for $i = 1, \dots, N - 1$ and $\Phi^N = v + \sigma$, the sum over $i$ splits as
>
> $$
> \Phi^i\Phi^i = \pi^i\pi^i + (v + \sigma)^2 ,
> $$
>
> where from now on the index of $\pi^i$ is summed over $i = 1, \dots, N - 1$. Since $v$ is constant, $\partial_\mu(v + \sigma) = \partial_\mu\sigma$, so
>
> $$
> \begin{aligned}
> \mathcal L ={}& \frac12\,\partial_\mu\pi^i\,\partial^\mu\pi^i + \frac12\,\partial_\mu\sigma\,\partial^\mu\sigma + \frac12\,\mu^2\Bigl[\pi^i\pi^i + (v + \sigma)^2\Bigr] \\
> &- \frac\lambda4\Bigl[\bigl(\pi^i\pi^i\bigr)^2 + 2\,\pi^i\pi^i\,(v + \sigma)^2 + (v + \sigma)^4\Bigr] .
> \end{aligned}
> $$
>
> **Step 3** (expand). Expanding $(v + \sigma)^2 = v^2 + 2v\sigma + \sigma^2$ and $(v + \sigma)^4 = v^4 + 4v^3\sigma + 6v^2\sigma^2 + 4v\sigma^3 + \sigma^4$,
>
> $$
> \begin{aligned}
> \mathcal L ={}& \frac12\,\partial_\mu\pi^i\,\partial^\mu\pi^i + \frac12\,\partial_\mu\sigma\,\partial^\mu\sigma + \frac12\,\mu^2\Bigl[\pi^i\pi^i + v^2 + 2v\sigma + \sigma^2\Bigr] \\
> &- \frac\lambda4\Bigl[\bigl(\pi^i\pi^i\bigr)^2 + 2\,\pi^i\pi^i\bigl(v^2 + 2v\sigma + \sigma^2\bigr) + v^4 + 4v^3\sigma + 6v^2\sigma^2 + 4v\sigma^3 + \sigma^4\Bigr] .
> \end{aligned}
> $$
>
> **Step 4** (group). Grouping the terms that contain only $\pi^i$, only $\sigma$, both, and neither: $\pi^i\pi^i$ has the coefficient $\frac12\mu^2 - \frac\lambda4\cdot2v^2 = \frac12(\mu^2 - \lambda v^2)$; $\sigma$ has $\frac12\mu^2\cdot2v - \frac\lambda4\cdot4v^3 = v(\mu^2 - \lambda v^2)$; $\sigma^2$ has $\frac12\mu^2 - \frac\lambda4\cdot6v^2 = \frac12(\mu^2 - 3\lambda v^2)$; $\sigma^3$ has $-\frac\lambda4\cdot4v = -\lambda v$; $\pi^i\pi^i\sigma$ has $-\frac\lambda4\cdot2\cdot2v = -\lambda v$; $\pi^i\pi^i\sigma^2$ has $-\frac\lambda4\cdot2 = -\frac\lambda2$. This is part 1.
>
> **Step 5** (at the minimum). With $v = \mu/\sqrt\lambda$, i.e. $\lambda v^2 = \mu^2$, the term linear in $\sigma$ and the $\pi^i\pi^i$ term vanish, $\frac12(\mu^2 - 3\lambda v^2) = -\mu^2$, and $\frac12\mu^2v^2 - \frac\lambda4v^4 = \frac{\mu^4}{2\lambda} - \frac{\mu^4}{4\lambda} = \frac{\mu^4}{4\lambda}$: part 2.
>
> **What the derivation shows.**
> - ⚑ By-product: the term linear in $\sigma$ has the coefficient $v(\mu^2 - \lambda v^2)$, which vanishes at the minimum, and the constant is minus the value of the potential there → [[§C6c.9 The Linear Sigma Model꞉ the Broken Phase#^thm-c6c-9-3|Theorem §C6c.9.3]].
> - ⚑ By-product: the same $\lambda v^2 = \mu^2$ removes the term quadratic in $\pi^i$ → [[§C6c.9 The Linear Sigma Model꞉ the Broken Phase#^thm-c6c-9-4|Theorem §C6c.9.4]].
> - Steps 1–4 do not use the value of $v$; this is what Problem 1(d) reuses ([[§C6c.10 The Linear Sigma Model꞉ Explicit Symmetry Breaking#^thm-c6c-10-3|Theorem §C6c.10.3]]).
> - The shift produces cubic terms, $\lambda v\,\sigma^3$ and $\lambda v\,\pi^i\pi^i\sigma$, from the quartic interaction; both are proportional to $v$.

^der-c6c-9-2

*Uses:* [[§C6c.9 The Linear Sigma Model꞉ the Broken Phase#^def-c6c-9-2|Def. §C6c.9.2]], [[§C6c.8 The Linear Sigma Model꞉ Fields with an Internal Index#^mod-c6c-8-1|Model §C6c.8.1]]

> [!theorem] Theorem §C6c.9.3: The Term Linear in σ Vanishes Exactly at a Stationary Point of the Potential
> In part 1 of [[§C6c.9 The Linear Sigma Model꞉ the Broken Phase#^thm-c6c-9-2|Theorem §C6c.9.2]], with $V(v) = -\frac12\mu^2v^2 + \frac\lambda4v^4$ the potential ([[§C6c.9 The Linear Sigma Model꞉ the Broken Phase#^def-c6c-9-1|Def. §C6c.9.1]]) on the $N$-th axis:
> 1. the coefficient of $\sigma$ is $v(\mu^2 - \lambda v^2) = -V'(v)$: the term linear in $\sigma$ vanishes exactly when $v$ is a stationary point of the potential;
> 2. the constant is $\frac12\mu^2v^2 - \frac\lambda4v^4 = -V(v)$; at $v = \mu/\sqrt\lambda$ it is $\frac{\mu^4}{4\lambda}$, minus the minimal value of [[§C6c.9 The Linear Sigma Model꞉ the Broken Phase#^thm-c6c-9-1|Theorem §C6c.9.1]].
>
> So the Lagrangian expanded around a minimum starts at second order in the fields, apart from a constant; a term linear in a field means that the expansion point is not a stationary point.
>
> *Model:* [[§C6c.8 The Linear Sigma Model꞉ Fields with an Internal Index#^mod-c6c-8-1|Model §C6c.8.1]] with $m^2 = -\mu^2$; *applies:* the classical Lagrangian in the variables of [[§C6c.9 The Linear Sigma Model꞉ the Broken Phase#^def-c6c-9-2|Def. §C6c.9.2]], any constant $v$; the same holds with the term $a\Phi^N$ ([[§C6c.10 The Linear Sigma Model꞉ Explicit Symmetry Breaking#^thm-c6c-10-3|Theorem §C6c.10.3]]).
>
> *Source: PHY 513, Problem Set 10, Problem 1(b) (the user's solution: "With $v = \mu/\sqrt\lambda$ … the term linear in $\sigma$ and the $\pi^i\pi^i$ term vanish") and Problem 1(d) ("By the new condition … the term linear in $\sigma$ vanishes"; "The constant is … $= -V(v)$") · stated as one box here*

^thm-c6c-9-3

> [!derivation]- Derivation
> **Step 1** (part 1). $V'(v) = -\mu^2v + \lambda v^3 = -v(\mu^2 - \lambda v^2)$ (Step 3 of [[§C6c.9 The Linear Sigma Model꞉ the Broken Phase#^der-c6c-9-1|Derivation §C6c.9.1]] with $\rho = v$), which is minus the coefficient of $\sigma$ in part 1 of Theorem §C6c.9.2.
>
> **Step 2** (part 2). $-V(v) = \frac12\mu^2v^2 - \frac\lambda4v^4$, the constant of part 1 of Theorem §C6c.9.2; at $v = \mu/\sqrt\lambda$, $V(v) = -\frac{\mu^4}{4\lambda}$ (Step 4 of Derivation §C6c.9.1).
>
> **Step 3** (why). With all $\pi^i = 0$ and $\sigma$ constant, $\mathcal L = -V$ evaluated at $\Phi = (0, \dots, 0, v + \sigma)$, that is, $-V(v + \sigma) = -V(v) - V'(v)\,\sigma - \frac12V''(v)\,\sigma^2 - \cdots$: the constant and the linear coefficient of $\mathcal L$ are the first two Taylor coefficients of $-V$ at $v$.

^der-c6c-9-3

*Uses:* [[§C6c.9 The Linear Sigma Model꞉ the Broken Phase#^thm-c6c-9-2|Theorem §C6c.9.2]], [[§C6c.9 The Linear Sigma Model꞉ the Broken Phase#^thm-c6c-9-1|Theorem §C6c.9.1]], [[§C6c.9 The Linear Sigma Model꞉ the Broken Phase#^def-c6c-9-1|Def. §C6c.9.1]]

> [!theorem] Theorem §C6c.9.4: The N − 1 Pion Fields Are Massless and σ Has Mass √2 μ
> In the Lagrangian of [[§C6c.9 The Linear Sigma Model꞉ the Broken Phase#^thm-c6c-9-2|Theorem §C6c.9.2]], 2 (expanded around the minimum $v = \mu/\sqrt\lambda$),
>
> $$
> m_\pi^2 = 0 , \qquad m_\sigma^2 = 2\mu^2 :
> $$
>
> the $N - 1$ fields $\pi^i$ are massless and $\sigma$ has mass $\sqrt2\,\mu$. The negative $m^2 = -\mu^2$ of the original fields does not appear as the mass of any field.
>
> *Model:* [[§C6c.8 The Linear Sigma Model꞉ Fields with an Internal Index#^mod-c6c-8-1|Model §C6c.8.1]] with $m^2 = -\mu^2$, in the fields of [[§C6c.9 The Linear Sigma Model꞉ the Broken Phase#^def-c6c-9-2|Def. §C6c.9.2]]; *applies:* the masses read off the quadratic terms of the Lagrangian, i.e. the masses of the free fields $\hat\pi^i$, $\hat\sigma$ of the perturbation expansion (lowest order).
>
> *Source: PHY 513, Problem Set 10, Problem 1(b) (the user's solution; statement: "Show that the $N - 1$ fields $\pi^i$ are massless and that $\sigma$ has mass $m_\sigma^2 = 2\mu^2$") · PS Problem 4.3(b), p. 128 ("a theory of a massive $\sigma$ field and $N - 1$ massless pion fields")*

^thm-c6c-9-4

> [!derivation]- Derivation
> **Step 1** (how a mass is read off). A field $\phi$ whose quadratic terms are $\frac12\,\partial_\mu\phi\,\partial^\mu\phi - \frac12\,m^2\phi^2$ has mass $m$ (the free real field, [[§C2a.1 Canonical Quantization of Fields#^mod-c2a-1-1|Model §C2a.1.1]]).
>
> **Step 2** (the pions). There is no term quadratic in $\pi^i$ other than the kinetic term, so the $N - 1$ fields $\pi^i$ are massless.
>
> **Step 3** (the sigma). The quadratic terms of $\sigma$ are $\frac12\,\partial_\mu\sigma\,\partial^\mu\sigma - \frac12\,(2\mu^2)\,\sigma^2$, so $m_\sigma^2 = 2\mu^2$.
>
> **What the derivation shows.**
> - For general $v$ the quadratic coefficients are $\frac12(\mu^2 - \lambda v^2)$ and $\frac12(\mu^2 - 3\lambda v^2)$ (part 1 of Theorem §C6c.9.2); the pion term is proportional to the coefficient of the linear term ([[§C6c.9 The Linear Sigma Model꞉ the Broken Phase#^thm-c6c-9-3|Theorem §C6c.9.3]]), so the pions are massless exactly when the expansion point is a stationary point with $v \ne 0$. With the term $a\Phi^N$ this changes → [[§C6c.10 The Linear Sigma Model꞉ Explicit Symmetry Breaking#^thm-c6c-10-3|Theorem §C6c.10.3]].

^der-c6c-9-4

*Uses:* [[§C6c.9 The Linear Sigma Model꞉ the Broken Phase#^thm-c6c-9-2|Theorem §C6c.9.2]], [[§C2a.1 Canonical Quantization of Fields#^mod-c2a-1-1|Model §C2a.1.1]]

## The Feynman rules

> [!theorem] Theorem §C6c.9.5: Feynman Rules of the Broken Phase
> ![[ph-qft-c6c-9-2.svg]]
> *The rules: pion lines solid blue with their indices, sigma lines dashed red. Added figure.*
>
> For the Lagrangian of [[§C6c.9 The Linear Sigma Model꞉ the Broken Phase#^thm-c6c-9-2|Theorem §C6c.9.2]], 2, with $v = \mu/\sqrt\lambda$ and pion indices $i, j, k, l \in \{1, \dots, N - 1\}$:
> 1. *Propagators.*
>
> $$
> \begin{aligned}
> \langle0|T\,\hat\pi^i(x)\hat\pi^j(y)|0\rangle &= \delta^{ij}\int\frac{d^4p}{(2\pi)^4}\,\frac{i}{p^2 + i\varepsilon}\,e^{-ip\cdot(x - y)} , \\
> \langle0|T\,\hat\sigma(x)\hat\sigma(y)|0\rangle &= \int\frac{d^4p}{(2\pi)^4}\,\frac{i}{p^2 - 2\mu^2 + i\varepsilon}\,e^{-ip\cdot(x - y)} , \\
> \langle0|T\,\hat\pi^i(x)\hat\sigma(y)|0\rangle &= 0 ;
> \end{aligned}
> $$
>
> in momentum space a pion line is $\dfrac{i\,\delta^{ij}}{p^2 + i\varepsilon}$, a sigma line $\dfrac{i}{p^2 - 2\mu^2 + i\varepsilon}$, and no line joins a pion to a sigma.
> 2. *Vertices:* two cubic and three quartic,
>
> | vertex | term of $\hat{\mathcal H}_I$ | contractions | factor |
> |---|---|---|---|
> | $\pi^i\pi^j\sigma$ | $\lambda v\,\hat\pi^m\hat\pi^m\hat\sigma$ | $2!\cdot1$ | $-2i\lambda v\,\delta^{ij}$ |
> | $\sigma\sigma\sigma$ | $\lambda v\,\hat\sigma^3$ | $3!$ | $-6i\lambda v$ |
> | $\pi^i\pi^j\sigma\sigma$ | $\frac\lambda2\,\hat\pi^m\hat\pi^m\hat\sigma^2$ | $2!\cdot2!$ | $-2i\lambda\,\delta^{ij}$ |
> | $\sigma\sigma\sigma\sigma$ | $\frac\lambda4\,\hat\sigma^4$ | $4!$ | $-6i\lambda$ |
> | $\pi^i\pi^j\pi^k\pi^l$ | $\frac\lambda4\bigl(\hat\pi^m\hat\pi^m\bigr)^2$ | as [[§C6c.8 The Linear Sigma Model꞉ Fields with an Internal Index#^thm-c6c-8-3\|Theorem §C6c.8.3]] | $-2i\lambda\,\bigl(\delta^{ij}\delta^{kl} + \delta^{ik}\delta^{jl} + \delta^{il}\delta^{jk}\bigr)$ |
>
> 3. Every vertex has an even number of pion lines, since the Lagrangian contains the $\pi^i$ only through $\pi^i\pi^i$; the two cubic vertices carry a factor $v$.
>
> The remaining rules (external lines $1$, momentum conservation at each vertex, loop integrals, $\frac1S$) are those of [[§C6c.6 Feynman Rules for Amplitudes#^thm-c6c-6-3|Theorem §C6c.6.3]] ([[§C6c.6 Feynman Rules for Amplitudes#^thm-c6c-6-1|Theorem §C6c.6.1]]).
>
> *Model:* [[§C6c.8 The Linear Sigma Model꞉ Fields with an Internal Index#^mod-c6c-8-1|Model §C6c.8.1]] with $m^2 = -\mu^2$, expanded around the minimum on the $N$-th axis ([[§C6c.9 The Linear Sigma Model꞉ the Broken Phase#^def-c6c-9-2|Def. §C6c.9.2]]); *applies:* propagators: the free fields $\hat\pi^i$, $\hat\sigma$, free vacuum, exact; vertices: every order; amplitudes from them at lowest order exactly (as [[§C6c.6 Feynman Rules for Amplitudes#^thm-c6c-6-2|Theorem §C6c.6.2]]).
>
> *Source: PHY 513, Problem Set 10, Problem 1(b) (the user's solution) · PS Problem 4.3(b), p. 128 (the two propagators and the five vertices drawn, values left to the reader) · part 3 and the second route written here; checked with `qft-C/tools/hw10/verify.py`*

^thm-c6c-9-5

> [!derivation]- Derivation
> **Step 1** (the interaction). The interaction Hamiltonian density is minus the cubic and quartic terms of $\mathcal L$ ([[§C6c.9 The Linear Sigma Model꞉ the Broken Phase#^thm-c6c-9-2|Theorem §C6c.9.2]], 2; no derivatives: [[§C6a.1 From Free to Interacting Fields#^thm-c6a-1-5|Theorem §C6a.1.5]]),
>
> $$
> \hat{\mathcal H}_I = \lambda v\,\hat\pi^m\hat\pi^m\,\hat\sigma + \lambda v\,\hat\sigma^3 + \frac\lambda4\bigl(\hat\pi^m\hat\pi^m\bigr)^2 + \frac\lambda2\,\hat\pi^m\hat\pi^m\,\hat\sigma^2 + \frac\lambda4\,\hat\sigma^4 ,
> $$
>
> with $m$ summed over $1, \dots, N - 1$. There are two cubic and three quartic terms, so two cubic and three quartic vertices.
>
> **Step 2** (how a vertex is read off). As in [[§C6c.8 The Linear Sigma Model꞉ Fields with an Internal Index#^der-c6c-8-3|Derivation §C6c.8.3]], each vertex factor is read off from the first-order term $\langle f|\,(-i)\int d^4z\,\hat{\mathcal H}_I(z)\,|i\rangle$: a field contracts only with an external particle of its own type, and the vertex factor is $-i$ times the coupling of the term times the number of contractions.
>
> **Step 3** (four pions). The term $\frac\lambda4\bigl(\hat\pi^m\hat\pi^m\bigr)^2$ has the form of the interaction of §C6c.8, with the $N - 1$ fields $\hat\pi^m$ in place of the $N$ fields $\hat\Phi^m$. By [[§C6c.8 The Linear Sigma Model꞉ Fields with an Internal Index#^thm-c6c-8-3|Theorem §C6c.8.3]], for pions of types $i, j, k, l \in \{1, \dots, N - 1\}$ the vertex factor is $-2i\lambda\,\bigl(\delta^{ij}\delta^{kl} + \delta^{ik}\delta^{jl} + \delta^{il}\delta^{jk}\bigr)$.
>
> **Step 4** (four sigmas). The term $\frac\lambda4\,\hat\sigma^4$ is the case of four legs of the same field (Step 6 of Derivation §C6c.8.3): the four particles contract with the four fields in $4!$ ways, and the vertex factor is $(-i)\cdot\frac\lambda4\cdot4! = -6i\lambda$.
>
> **Step 5** (three sigmas). The first-order term is
>
> $$
> \langle f|\,(-i)\,\lambda v\int d^4z\;\hat\sigma(z)\,\hat\sigma(z)\,\hat\sigma(z)\,|i\rangle ,
> $$
>
> which is nonzero only if the three external particles are sigmas. They contract with the three fields in $3!$ ways, so the vertex factor is
>
> $$
> (-i)\cdot\lambda v\cdot3! = -6i\lambda v .
> $$
>
> **Step 6** (two pions and one sigma). For external pions of types $i$ and $j$ and one sigma, the first-order term is
>
> $$
> \langle f|\,(-i)\,\lambda v\int d^4z\,\sum_{m=1}^{N-1}\hat\pi^m(z)\,\hat\pi^m(z)\,\hat\sigma(z)\,|i\rangle .
> $$
>
> The term $m$ of the sum contributes only if both pions are of type $m$, so $i = j$. The two pions contract with the two $\hat\pi^m$ in $2!$ ways and the sigma with $\hat\sigma$ in one way, so the vertex factor is
>
> $$
> (-i)\cdot\lambda v\cdot2!\cdot1\cdot\delta^{ij} = -2i\lambda v\,\delta^{ij} .
> $$
>
> **Step 7** (two pions and two sigmas). For external pions of types $i$ and $j$ and two sigmas, the first-order term is
>
> $$
> \langle f|\,(-i)\,\frac\lambda2\int d^4z\,\sum_{m=1}^{N-1}\hat\pi^m(z)\,\hat\pi^m(z)\,\hat\sigma(z)\,\hat\sigma(z)\,|i\rangle .
> $$
>
> Again $i = j$; the two pions contract with the two $\hat\pi^m$ in $2!$ ways and the two sigmas with the two $\hat\sigma$ in $2!$ ways, so the vertex factor is
>
> $$
> (-i)\cdot\frac\lambda2\cdot2!\cdot2!\cdot\delta^{ij} = -2i\lambda\,\delta^{ij} .
> $$
>
> Steps 3–7 are the table of part 2.
>
> **Step 8** (propagators). The quadratic part of $\mathcal L$ is a sum of independent real Klein–Gordon Lagrangians, for the $N - 1$ fields $\hat\pi^i$ with mass $0$ and for the field $\hat\sigma$ with mass $m_\sigma^2 = 2\mu^2$ ([[§C6c.9 The Linear Sigma Model꞉ the Broken Phase#^thm-c6c-9-4|Theorem §C6c.9.4]]):
>
> $$
> \mathcal L_0 = \sum_{i=1}^{N-1}\frac12\,\partial_\mu\hat\pi^i\,\partial^\mu\hat\pi^i + \frac12\,\partial_\mu\hat\sigma\,\partial^\mu\hat\sigma - \frac12\,(2\mu^2)\,\hat\sigma^2 .
> $$
>
> As in [[§C6c.8 The Linear Sigma Model꞉ Fields with an Internal Index#^der-c6c-8-2|Derivation §C6c.8.2]], each field has the mode expansion of a real scalar field with its own oscillators, and the oscillators of different fields commute. So the time-ordered product of two different fields vanishes, and that of two equal fields is the propagator of a single real scalar field of the corresponding mass ([[§C6a.14 Feynman Rules for Polynomial Interactions#^lem-c6a-14-1|Lemma §C6a.14.1]], 1): part 1.
>
> **Step 9** (part 3). Every term of $\hat{\mathcal H}_I$ in Step 1 contains $\hat\pi^m\hat\pi^m$ to the power $0$, $1$ or $2$: an even number of pion fields, hence of pion legs. The cubic terms are the two with the coefficient $\lambda v$.
>
> **What the derivation shows.**
> - One rule gives all five factors: $-i\times$ coupling $\times$ number of contractions; the $\delta^{ij}$ comes from the sum over $m$, which a pair of external pions can use only if they are of the same type.
> - The same five factors by differentiating → the second route below ([[§C6c.8 The Linear Sigma Model꞉ Fields with an Internal Index#^thm-c6c-8-4|Theorem §C6c.8.4]]).

^der-c6c-9-5

> [!derivation]- Derivation (second route: differentiating the interaction potential)
> By [[§C6c.8 The Linear Sigma Model꞉ Fields with an Internal Index#^thm-c6c-8-4|Theorem §C6c.8.4]], with $V_{\rm int}(\pi, \sigma) = \lambda v\,\pi^m\pi^m\sigma + \lambda v\,\sigma^3 + \frac\lambda4(\pi^m\pi^m)^2 + \frac\lambda2\,\pi^m\pi^m\sigma^2 + \frac\lambda4\,\sigma^4$, each vertex is $-i$ times a derivative at $\pi = \sigma = 0$. Here $V_{\rm int}$ has cubic and quartic terms, so the value at zero field matters (part 1 of that theorem). Use $\frac{\partial^2}{\partial\pi^i\partial\pi^j}(\pi^m\pi^m) = 2\delta^{ij}$.
>
> **Step 1** ($\pi^i\pi^j\sigma$).
>
> $$
> \frac{\partial^3V_{\rm int}}{\partial\pi^i\partial\pi^j\partial\sigma} = \lambda v\cdot2\delta^{ij} + \frac\lambda2\cdot2\delta^{ij}\cdot2\sigma = 2\lambda v\,\delta^{ij} + 2\lambda\,\delta^{ij}\sigma \;\xrightarrow{\ \sigma = 0\ }\; 2\lambda v\,\delta^{ij}
> $$
>
> (the terms $\lambda v\,\sigma^3$, $\frac\lambda4\sigma^4$ have no $\pi$, and $\frac\lambda4(\pi^m\pi^m)^2$ has no $\sigma$), so the factor is $-2i\lambda v\,\delta^{ij}$. The term $2\lambda\delta^{ij}\sigma$ that is dropped at $\sigma = 0$ belongs to the quartic vertex of Step 3.
>
> **Step 2** ($\sigma\sigma\sigma$). $\frac{\partial^3V_{\rm int}}{\partial\sigma^3} = \lambda v\cdot3! + \frac\lambda4\cdot4\cdot3\cdot2\,\sigma = 6\lambda v + 6\lambda\sigma \to 6\lambda v$: factor $-6i\lambda v$.
>
> **Step 3** ($\pi^i\pi^j\sigma\sigma$). $\frac{\partial^4V_{\rm int}}{\partial\pi^i\partial\pi^j\partial\sigma^2} = \frac\lambda2\cdot2\delta^{ij}\cdot2 = 2\lambda\,\delta^{ij}$: factor $-2i\lambda\,\delta^{ij}$.
>
> **Step 4** ($\sigma\sigma\sigma\sigma$). $\frac{\partial^4V_{\rm int}}{\partial\sigma^4} = \frac\lambda4\cdot4! = 6\lambda$: factor $-6i\lambda$.
>
> **Step 5** ($\pi^i\pi^j\pi^k\pi^l$). Only $\frac\lambda4(\pi^m\pi^m)^2$ survives four pion derivatives at $\sigma = 0$, and [[§C6c.8 The Linear Sigma Model꞉ Fields with an Internal Index#^ex-c6c-8-1|Example §C6c.8.1]] with $N - 1$ fields gives $2\lambda(\delta^{ij}\delta^{kl} + \delta^{ik}\delta^{jl} + \delta^{il}\delta^{jk})$: factor $-2i\lambda(\delta^{ij}\delta^{kl} + \delta^{ik}\delta^{jl} + \delta^{il}\delta^{jk})$.
>
> **Step 6** (no other vertex). An odd number of pion derivatives leaves an odd power of $\pi$ in every term, which vanishes at $\pi = 0$: no $\pi\sigma\sigma$, $\pi\pi\pi$, $\pi\sigma\sigma\sigma$ or $\pi\pi\pi\sigma$ vertex.
>
> The two routes agree: the factorials of the derivatives are the numbers of contractions of the first route.

^der-c6c-9-5b

*Uses:* [[§C6c.9 The Linear Sigma Model꞉ the Broken Phase#^thm-c6c-9-2|Theorem §C6c.9.2]], [[§C6c.9 The Linear Sigma Model꞉ the Broken Phase#^thm-c6c-9-4|Theorem §C6c.9.4]], [[§C6c.8 The Linear Sigma Model꞉ Fields with an Internal Index#^thm-c6c-8-3|Theorem §C6c.8.3]], [[§C6c.8 The Linear Sigma Model꞉ Fields with an Internal Index#^der-c6c-8-2|Derivation §C6c.8.2]], [[§C6c.8 The Linear Sigma Model꞉ Fields with an Internal Index#^der-c6c-8-3|Derivation §C6c.8.3]], [[§C6a.1 From Free to Interacting Fields#^thm-c6a-1-5|Theorem §C6a.1.5]], [[§C6a.14 Feynman Rules for Polynomial Interactions#^lem-c6a-14-1|Lemma §C6a.14.1]]; second route: [[§C6c.8 The Linear Sigma Model꞉ Fields with an Internal Index#^thm-c6c-8-4|Theorem §C6c.8.4]], [[§C6c.8 The Linear Sigma Model꞉ Fields with an Internal Index#^ex-c6c-8-1|Example §C6c.8.1]]

*Procedure:* [[P6 Tree Amplitude from a Lagrangian#^p6-1|P6, steps 1–2]]

## Pion–pion scattering

> [!theorem] Theorem §C6c.9.6: ππ → ππ at Order λ
> ![[ph-qft-c6c-9-3.svg]]
> *The four diagrams of $\pi^i(p_1)\,\pi^j(p_2) \to \pi^k(p_3)\,\pi^l(p_4)$ at order $\lambda$: $\sigma$ exchange in the $s$-, $t$- and $u$-channels, each with two cubic vertices $-2i\lambda v\,\delta$, and the four-pion contact vertex; incoming left, outgoing right; the value of each diagram below it. Added figure.*
>
> *Order counting.* The cubic vertices are proportional to $\lambda v$, and $\lambda v^2 = \mu^2$ counts as order one; so two cubic vertices, $(\lambda v)^2 = \lambda\cdot\lambda v^2$, are of the same order $\lambda$ as one quartic vertex. With the rules of [[§C6c.9 The Linear Sigma Model꞉ the Broken Phase#^thm-c6c-9-5|Theorem §C6c.9.5]], for incoming pions of momenta $p_1, p_2$ and types $i, j$ and outgoing pions of momenta $p_3, p_4$ and types $k, l$, at order $\lambda$:
>
> $$
> \begin{aligned}
> i\mathcal M ={}& -2i\lambda\,\bigl(\delta^{ij}\delta^{kl} + \delta^{ik}\delta^{jl} + \delta^{il}\delta^{jk}\bigr) \\
> &+ (-2i\lambda v)^2\biggl[\delta^{ij}\delta^{kl}\,\frac{i}{(p_1 + p_2)^2 - 2\mu^2} + \delta^{ik}\delta^{jl}\,\frac{i}{(p_1 - p_3)^2 - 2\mu^2} + \delta^{il}\delta^{jk}\,\frac{i}{(p_1 - p_4)^2 - 2\mu^2}\biggr] .
> \end{aligned}
> $$
>
> 1. The first line is the contact diagram; the three terms of the bracket are the exchange of a $\sigma$ in the $s$-, $t$- and $u$-channels, $s = (p_1 + p_2)^2$, $t = (p_1 - p_3)^2$, $u = (p_1 - p_4)^2$ ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-7|Theorem §C6b.1.7]], with $A, B, 1, 2 \to 1, 2, 3, 4$; [[§C6c.6 Feynman Rules for Amplitudes#^thm-c6c-6-4|Theorem §C6c.6.4]]).
> 2. Each channel carries the pair of $\delta$'s of the two pions that meet at each of its vertices: $\delta^{ij}\delta^{kl}$ in $s$, $\delta^{ik}\delta^{jl}$ in $t$, $\delta^{il}\delta^{jk}$ in $u$; the contact term carries all three.
>
> *Model:* [[§C6c.8 The Linear Sigma Model꞉ Fields with an Internal Index#^mod-c6c-8-1|Model §C6c.8.1]] with $m^2 = -\mu^2$, in the fields of [[§C6c.9 The Linear Sigma Model꞉ the Broken Phase#^def-c6c-9-2|Def. §C6c.9.2]]; *applies:* tree level, order $\lambda$ with $\lambda v^2 = \mu^2$ counted as order one, free relativistic massless pion states for the in and out states; the $i\varepsilon$ of the $\sigma$ propagator is dropped as in the solution, which requires $s \ne 2\mu^2$ ($t, u \le 0$ never reach $2\mu^2$: [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-8|Theorem §C6b.4.8]]).
>
> *Source: PHY 513, Problem Set 10, Problem 1(c) (the user's solution; statement: "There are four diagrams: $\sigma$-exchange in the $s$-, $t$- and $u$-channels, each built from two cubic $\sigma\pi\pi$ vertices, and the quartic $\pi\pi\pi\pi$ contact vertex"; "count $\lambda v^2 = \mu^2$ as order one") · PS Problem 4.3(c), p. 128 · Step 9 (the check by the rules) written here*

^thm-c6c-9-6

> [!derivation]- Derivation
> **Step 1** (states). Let the incoming pions have momenta $p_1, p_2$ and types $i, j$, and the outgoing pions momenta $p_3, p_4$ and types $k, l$:
>
> $$
> |i\rangle = |\pi^i(p_1)\,\pi^j(p_2)\rangle , \qquad \langle f| = \langle\pi^k(p_3)\,\pi^l(p_4)| .
> $$
>
> **Step 2** (the terms of order $\lambda$). With $\hat{\mathcal H}_I$ from Step 1 of [[§C6c.9 The Linear Sigma Model꞉ the Broken Phase#^der-c6c-9-5|Derivation §C6c.9.5]], two terms of $\langle f|\,T\exp\bigl(-i\int d^4z\,\hat{\mathcal H}_I\bigr)|i\rangle$ are of order $\lambda$, counting $\lambda v^2 = \mu^2$ as order one:
>
> $$
> \begin{aligned}
> \langle f|\,i\hat T\,|i\rangle ={}& \langle f|\,(-i)\int d^4z\;\frac\lambda4\bigl(\hat\pi^m\hat\pi^m\bigr)^2(z)\,|i\rangle \\
> &+ \langle f|\,\frac{(-i)^2}{2!}\int d^4z_1\,d^4z_2\;T\Bigl[\lambda v\,\hat\pi^m\hat\pi^m\hat\sigma(z_1)\;\lambda v\,\hat\pi^n\hat\pi^n\hat\sigma(z_2)\Bigr]|i\rangle .
> \end{aligned}
> $$
>
> The second term is of order $(\lambda v)^2 = \lambda\cdot\lambda v^2$.
>
> **Step 3** (first term). All four fields contract with the four external pions, so there is no propagator. Each contraction gives a plane wave, $e^{-ip\cdot z}$ for an incoming and $e^{ip\cdot z}$ for an outgoing pion, and the number of contractions is counted by the four-pion vertex factor of [[§C6c.9 The Linear Sigma Model꞉ the Broken Phase#^thm-c6c-9-5|Theorem §C6c.9.5]]:
>
> $$
> \langle f|\,(-i)\int d^4z\;\frac\lambda4\bigl(\hat\pi^m\hat\pi^m\bigr)^2(z)\,|i\rangle = -2i\lambda\,\bigl(\delta^{ij}\delta^{kl} + \delta^{ik}\delta^{jl} + \delta^{il}\delta^{jk}\bigr)\int d^4z\;e^{-i(p_1 + p_2 - p_3 - p_4)\cdot z} .
> $$
>
> The $z$ integral gives $(2\pi)^4\delta^4(p_1 + p_2 - p_3 - p_4)$ ([[§CA.4 Fourier Transforms and Fourier Tricks#^thm-ca-4-3|Theorem §CA.4.3]]).
>
> **Step 4** (second term: the propagator and the three splits). The four pion fields contract with the four external pions, and the two $\hat\sigma$ contract with each other into the sigma propagator of Theorem §C6c.9.5,
>
> $$
> \langle0|T\,\hat\sigma(z_1)\hat\sigma(z_2)|0\rangle = \int\frac{d^4q}{(2\pi)^4}\,\frac{i}{q^2 - 2\mu^2 + i\varepsilon}\,e^{-iq\cdot(z_1 - z_2)} .
> $$
>
> Two of the external pions contract at one vertex and two at the other. The four pions can be split into two pairs in three ways: $(p_1, p_2)$ with $(p_3, p_4)$, $(p_1, p_3)$ with $(p_2, p_4)$, and $(p_1, p_4)$ with $(p_2, p_3)$.
>
> **Step 5** (the split $(p_1, p_2)$ with $(p_3, p_4)$: the count). There are $2$ choices of the vertex, $z_1$ or $z_2$, that takes the pair $(p_1, p_2)$, $2!$ ways to contract that pair with the two pion fields at its vertex, and $2!$ ways for the other pair, so $2\cdot2\cdot2 = 8$ contractions, all equal. (With the pion fields $\hat\pi^m_a\hat\pi^m_b$ at $z_1$ and $\hat\pi^n_a\hat\pi^n_b$ at $z_2$: $\{p_1a, p_2b\}$ or $\{p_1b, p_2a\}$ at $z_1$, each with $\{p_3a, p_4b\}$ or $\{p_3b, p_4a\}$ at $z_2$, and the same four with $z_1 \leftrightarrow z_2$.) With the prefactor,
>
> $$
> \frac{(-i)^2}{2!}\,(\lambda v)^2\cdot8 = (-2i\lambda v)^2 .
> $$
>
> At the vertex with $(p_1, p_2)$ both pions must have the type of the fields there, which gives $\delta^{ij}$, and likewise $\delta^{kl}$ at the other vertex.
>
> **Step 6** (the split $(p_1, p_2)$ with $(p_3, p_4)$: the integrals). Calling $z_1$ the vertex with the incoming pair, this split contributes
>
> $$
> (-2i\lambda v)^2\,\delta^{ij}\delta^{kl}\int d^4z_1\,d^4z_2\;e^{-i(p_1 + p_2)\cdot z_1}\,e^{i(p_3 + p_4)\cdot z_2}\int\frac{d^4q}{(2\pi)^4}\,\frac{i}{q^2 - 2\mu^2 + i\varepsilon}\,e^{-iq\cdot(z_1 - z_2)} .
> $$
>
> The $z$ integrals give
>
> $$
> \begin{aligned}
> \int d^4z_1\;e^{-i(p_1 + p_2 + q)\cdot z_1} &= (2\pi)^4\delta^4(p_1 + p_2 + q) , \\
> \int d^4z_2\;e^{i(p_3 + p_4 + q)\cdot z_2} &= (2\pi)^4\delta^4(p_3 + p_4 + q) ,
> \end{aligned}
> $$
>
> and the $q$ integral sets $q = -(p_1 + p_2)$:
>
> $$
> (-2i\lambda v)^2\,\delta^{ij}\delta^{kl}\,\frac{i}{(p_1 + p_2)^2 - 2\mu^2}\,(2\pi)^4\delta^4(p_1 + p_2 - p_3 - p_4) .
> $$
>
> **Step 7** (the other two splits). They have the same structure. For $(p_1, p_3)$ with $(p_2, p_4)$ the plane waves at $z_1$ are $e^{-i(p_1 - p_3)\cdot z_1}$, so $q = -(p_1 - p_3)$ and the types give $\delta^{ik}\delta^{jl}$; for $(p_1, p_4)$ with $(p_2, p_3)$, $q = -(p_1 - p_4)$ with $\delta^{il}\delta^{jk}$.
>
> **Step 8** (total). With $\langle f|\,i\hat T\,|i\rangle = i\mathcal M\,(2\pi)^4\delta^4(p_1 + p_2 - p_3 - p_4)$ ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-3|Def. §C6b.1.3]]), Steps 3, 6 and 7 add up to the statement.
>
> **Step 9** (check: the rules give the same expression at once). By the tree rules ([[§C6c.6 Feynman Rules for Amplitudes#^thm-c6c-6-2|Theorem §C6c.6.2]]) with the factors of Theorem §C6c.9.5, the $s$-channel diagram is vertex $\times$ internal line $\times$ vertex,
>
> $$
> \bigl(-2i\lambda v\,\delta^{ij}\bigr)\,\frac{i}{(p_1 + p_2)^2 - 2\mu^2}\,\bigl(-2i\lambda v\,\delta^{kl}\bigr) ,
> $$
>
> the internal momentum fixed by conservation at the vertex of $p_1, p_2$; the $t$- and $u$-channel diagrams follow with the pairs $(p_1, p_3)$ and $(p_1, p_4)$, and the contact diagram is the four-pion vertex: the four terms of the statement. A pair of pions can meet at a $\pi\pi\sigma$ vertex in each of the three channels, so all three exist ([[§C6c.6 Feynman Rules for Amplitudes#^thm-c6c-6-6|Theorem §C6c.6.6]], 1), each with its $\delta$'s.
>
> **What the derivation shows.**
> - The $\frac{1}{2!}$ of the second-order term is cancelled by the $2$ choices of the vertex ([[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^thm-c6c-5-2|Theorem §C6c.5.2]]), and the $2!\cdot2!$ turn the two couplings $\lambda v$ into two vertex factors $-2i\lambda v$: the product of vertex factors of the rules.
> - The three splits of the four pions into two pairs are the three channels, and they are also the three pairings of the indices in the contact vertex: the same combinatorics appears in the kinematics and in the index structure → [[§C6c.9 The Linear Sigma Model꞉ the Broken Phase#^thm-c6c-9-7|Theorem §C6c.9.7]], where this lets the terms cancel structure by structure.

^der-c6c-9-6

*Uses:* [[§C6c.9 The Linear Sigma Model꞉ the Broken Phase#^thm-c6c-9-5|Theorem §C6c.9.5]], [[§C6c.9 The Linear Sigma Model꞉ the Broken Phase#^der-c6c-9-5|Derivation §C6c.9.5]], [[§CA.4 Fourier Transforms and Fourier Tricks#^thm-ca-4-3|Theorem §CA.4.3]], [[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-3|Def. §C6b.1.3]], [[§C6c.6 Feynman Rules for Amplitudes#^thm-c6c-6-2|Theorem §C6c.6.2]], [[§C6c.6 Feynman Rules for Amplitudes#^thm-c6c-6-4|Theorem §C6c.6.4]], [[§C6c.6 Feynman Rules for Amplitudes#^thm-c6c-6-6|Theorem §C6c.6.6]], [[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^thm-c6c-5-2|Theorem §C6c.5.2]], [[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-7|Theorem §C6b.1.7]]

*Procedure:* [[P6 Tree Amplitude from a Lagrangian#^p6-3|P6, steps 3–6]]

> [!theorem] Theorem §C6c.9.7: The ππ → ππ Amplitude Vanishes at Threshold
> For the amplitude of [[§C6c.9 The Linear Sigma Model꞉ the Broken Phase#^thm-c6c-9-6|Theorem §C6c.9.6]], at threshold, where all external momenta vanish, $p_1 = p_2 = p_3 = p_4 = 0$:
>
> $$
> i\mathcal M\Big|_{\text{threshold}} = \bigl(-2i\lambda + 2i\lambda\bigr)\bigl(\delta^{ij}\delta^{kl} + \delta^{ik}\delta^{jl} + \delta^{il}\delta^{jk}\bigr) = 0 ,
> $$
>
> for every $N$ and all types $i, j, k, l$. The contact term $-2i\lambda$ is cancelled by the three exchange terms, each $+2i\lambda$ times its pair of $\delta$'s; the cancellation uses $\lambda v^2 = \mu^2$, the condition of the minimum ([[§C6c.9 The Linear Sigma Model꞉ the Broken Phase#^thm-c6c-9-1|Theorem §C6c.9.1]]).
>
> *Model:* as [[§C6c.9 The Linear Sigma Model꞉ the Broken Phase#^thm-c6c-9-6|Theorem §C6c.9.6]]; *applies:* order $\lambda$, tree level; massless pions, for which the threshold $E_{\rm cm} = 0$ ([[§C6b.3 The Cross Section#^thm-c6b-3-12|Theorem §C6b.3.12]]) is the point where every external four-momentum vanishes.
>
> *Source: PHY 513, Problem Set 10, Problem 1(c) (the user's solution; statement: "Show that $\mathcal M$ vanishes at threshold, where all external momenta vanish") · PS Problem 4.3(c)*

^thm-c6c-9-7

> [!derivation]- Derivation
> **Step 1** (the kinematic point). The pions are massless, so at threshold, where they have no kinetic energy, all external four-momenta vanish, $p_1 = p_2 = p_3 = p_4 = 0$, and
>
> $$
> (p_1 + p_2)^2 = (p_1 - p_3)^2 = (p_1 - p_4)^2 = 0 .
> $$
>
> **Step 2** (the exchange terms). All three denominators become $-2\mu^2$, so with $(-2i\lambda v)^2 = -4\lambda^2v^2$ the exchange terms are
>
> $$
> (-2i\lambda v)^2\,\frac{i}{-2\mu^2}\,\bigl(\delta^{ij}\delta^{kl} + \delta^{ik}\delta^{jl} + \delta^{il}\delta^{jk}\bigr) = \frac{2i\lambda^2v^2}{\mu^2}\,\bigl(\delta^{ij}\delta^{kl} + \delta^{ik}\delta^{jl} + \delta^{il}\delta^{jk}\bigr) .
> $$
>
> **Step 3** (the cancellation). Since $\lambda v^2 = \mu^2$, the prefactor is $2i\lambda$, which cancels the contact term $-2i\lambda$: the statement.
>
> **What the derivation shows.**
> - At zero momentum the exchange of a $\sigma$ is a constant, $\frac{i}{-2\mu^2}$ times the two vertices: it acts as a contact term of strength $(-2i\lambda v)^2\frac{i}{-2\mu^2} = +2i\lambda\frac{\lambda v^2}{\mu^2}$, with the sign opposite to that of the four-pion vertex.
> - The cancellation is exact only for $\lambda v^2 = \mu^2$; with $\lambda v^2 = \mu^2 + a/v$ a remainder proportional to $a$ is left → [[§C6c.10 The Linear Sigma Model꞉ Explicit Symmetry Breaking#^thm-c6c-10-5|Theorem §C6c.10.5]].

^der-c6c-9-7

*Uses:* [[§C6c.9 The Linear Sigma Model꞉ the Broken Phase#^thm-c6c-9-6|Theorem §C6c.9.6]], [[§C6c.9 The Linear Sigma Model꞉ the Broken Phase#^thm-c6c-9-1|Theorem §C6c.9.1]]

> [!theorem] Theorem §C6c.9.8: For One Pion (N = 2) the Term of First Order in s, t, u Vanishes Too
> For $N = 2$ there is a single pion, $i = j = k = l = 1$, and the amplitude of [[§C6c.9 The Linear Sigma Model꞉ the Broken Phase#^thm-c6c-9-6|Theorem §C6c.9.6]] is
>
> $$
> i\mathcal M = -6i\lambda + (-2i\lambda v)^2\biggl[\frac{i}{s - 2\mu^2} + \frac{i}{t - 2\mu^2} + \frac{i}{u - 2\mu^2}\biggr] .
> $$
>
> 1. Expanded for $s$, $t$, $u$ small compared with $2\mu^2$,
>
> $$
> i\mathcal M = \frac{i\lambda}{\mu^2}\,(s + t + u) + O(s^2, t^2, u^2) .
> $$
>
> 2. For momenta with $p_1 + p_2 = p_3 + p_4$, $s + t + u = p_1^2 + p_2^2 + p_3^2 + p_4^2$ ([[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-1|Theorem §C1a.5.1]], 1), which is $0$ for massless on-shell pions. Hence
>
> $$
> s + t + u = 0 , \qquad i\mathcal M = O(s^2, t^2, u^2) :
> $$
>
> the term of first order in $s$, $t$, $u$ vanishes as well as the constant.
>
> *Model:* as [[§C6c.9 The Linear Sigma Model꞉ the Broken Phase#^thm-c6c-9-6|Theorem §C6c.9.6]] with $N = 2$; *applies:* order $\lambda$, tree level, external pions on shell with $p_n^2 = 0$, $|s|, |t|, |u| \ll 2\mu^2$.
>
> *Source: PHY 513, Problem Set 10, Problem 1(c) (the user's solution; statement: "For $N = 2$ there is a single pion. Expand $\mathcal M$ to first order in $s$, $t$, $u$ and show that this term vanishes as well") · the sum rule: PHY 513, Problem Set 10, statement, eq. (2) ("if all four particles have the same mass $m$, then $s + t + u = 4m^2$")*

^thm-c6c-9-8

> [!derivation]- Derivation
> **Step 1** ($N = 2$). With a single pion, $i = j = k = l = 1$ and all the deltas are $1$. With $s = (p_1 + p_2)^2$, $t = (p_1 - p_3)^2$, $u = (p_1 - p_4)^2$,
>
> $$
> i\mathcal M = -6i\lambda + (-2i\lambda v)^2\biggl[\frac{i}{s - 2\mu^2} + \frac{i}{t - 2\mu^2} + \frac{i}{u - 2\mu^2}\biggr] .
> $$
>
> **Step 2** (the geometric series). For $x \in \{s, t, u\}$ small compared with $2\mu^2$ ([[§14 Series#^ex-14-4|451 Example §14.4]]),
>
> $$
> \frac{1}{x - 2\mu^2} = -\frac{1}{2\mu^2}\cdot\frac{1}{1 - \frac{x}{2\mu^2}} = -\frac{1}{2\mu^2}\Bigl(1 + \frac{x}{2\mu^2} + O(x^2)\Bigr) .
> $$
>
> **Step 3** (one exchange term). With $(-2i\lambda v)^2\cdot i = -4i\lambda^2v^2$ and $\lambda v^2 = \mu^2$, each exchange term is
>
> $$
> (-2i\lambda v)^2\,\frac{i}{x - 2\mu^2} = \frac{2i\lambda^2v^2}{\mu^2}\Bigl(1 + \frac{x}{2\mu^2}\Bigr) + O(x^2) = 2i\lambda + \frac{i\lambda}{\mu^2}\,x + O(x^2) .
> $$
>
> **Step 4** (the sum). Adding the three exchange terms and the contact term,
>
> $$
> i\mathcal M = -6i\lambda + 6i\lambda + \frac{i\lambda}{\mu^2}\,(s + t + u) + O(s^2, t^2, u^2) = \frac{i\lambda}{\mu^2}\,(s + t + u) + O(s^2, t^2, u^2) .
> $$
>
> **Step 5** ($s + t + u$). Expanding $s$, $t$ and $u$,
>
> $$
> s + t + u = (p_1 + p_2)^2 + (p_1 - p_3)^2 + (p_1 - p_4)^2 = 3p_1^2 + 2p_1\cdot(p_2 - p_3 - p_4) + p_2^2 + p_3^2 + p_4^2 .
> $$
>
> By momentum conservation, $p_1 + p_2 = p_3 + p_4$, so $p_2 - p_3 - p_4 = -p_1$ and
>
> $$
> s + t + u = 3p_1^2 - 2p_1^2 + p_2^2 + p_3^2 + p_4^2 = p_1^2 + p_2^2 + p_3^2 + p_4^2 .
> $$
>
> **Step 6** (on shell). The external pions are on shell and massless, $p_n^2 = m_\pi^2 = 0$ for $n = 1, \dots, 4$ ([[§C6c.9 The Linear Sigma Model꞉ the Broken Phase#^thm-c6c-9-4|Theorem §C6c.9.4]]), so $s + t + u = 0$ and $i\mathcal M = O(s^2, t^2, u^2)$.
>
> **What the derivation shows.**
> - The constant term cancels by $\lambda v^2 = \mu^2$ ([[§C6c.9 The Linear Sigma Model꞉ the Broken Phase#^thm-c6c-9-7|Theorem §C6c.9.7]]); the first-order term cancels by the kinematic identity $s + t + u = \sum_np_n^2$ together with $m_\pi = 0$. For $N > 2$ the three channels carry different $\delta$'s and the first-order term is $\frac{i\lambda}{\mu^2}\bigl(s\,\delta^{ij}\delta^{kl} + t\,\delta^{ik}\delta^{jl} + u\,\delta^{il}\delta^{jk}\bigr)$, which the identity does not remove.
> - Step 5 holds for any four momenta with $p_1 + p_2 = p_3 + p_4$, on shell or not; with masses it is the sum rule of [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-1|Theorem §C1a.5.1]], 1.

^der-c6c-9-8

*Uses:* [[§C6c.9 The Linear Sigma Model꞉ the Broken Phase#^thm-c6c-9-6|Theorem §C6c.9.6]], [[§C6c.9 The Linear Sigma Model꞉ the Broken Phase#^thm-c6c-9-4|Theorem §C6c.9.4]], [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-1|Theorem §C1a.5.1]], [[§14 Series#^ex-14-4|451 Example §14.4]]

> [!remark] Remark: At low momenta the pions interact weakly
> By [[§C6c.9 The Linear Sigma Model꞉ the Broken Phase#^thm-c6c-9-7|Theorem §C6c.9.7]] and [[§C6c.9 The Linear Sigma Model꞉ the Broken Phase#^thm-c6c-9-8|Theorem §C6c.9.8]] the $\pi\pi \to \pi\pi$ amplitude at order $\lambda$ is small when the momenta are small compared with $\mu$, although each of its four diagrams is of size $\lambda$: the contact diagram and the $\sigma$ exchanges cancel, at zero momentum for every $N$, and for $N = 2$ also at first order in $s$, $t$, $u$.
>
> *Source: read off Theorems §C6c.9.7–§C6c.9.8 (PHY 513, Problem Set 10, Problem 1(c)) · PS Problem 4.3, p. 127 ("The interactions of pions at low energy can be described by a phenomenological model called the linear sigma model")*

^rem-c6c-9-1

> [!abstract]- Mathematical background
> Proved in the Math vault and in CA; each line says what the physics above relies on.
>
> - [[§11 Topological Groups and Classical Matrix Groups#^def-11-7|591 Def. §11.7]] — $O(N)$ preserves the length of the field vector, so the potential, a function of $\Phi^i\Phi^i$, is constant on spheres and its set of minima is a union of spheres (here one).
> - [[§34 Retractions and Fixed Points#^def-34-3|590 Def. §34.3]] — the sphere $S^{N-1}$; the minima are its image under scaling by $v$.
> - [[§13 Group Actions and Orbit Spaces#^ex-13-7|591 Example §13.7]] — the rotations act transitively on each sphere (written there for $N = 3$): any minimum can be rotated onto the $N$-th axis, which is why the choice of [[§C6c.9 The Linear Sigma Model꞉ the Broken Phase#^def-c6c-9-2|Def. §C6c.9.2]] loses no generality; the sphere as a quotient of the rotation group: [[§14 Homogeneous Spaces#^ex-14-5|591 Example §14.5]].
> - [[§14 Series#^ex-14-4|451 Example §14.4]] — the geometric series, used to expand the $\sigma$ propagator at small $s$, $t$, $u$.
> - [[§CA.4 Fourier Transforms and Fourier Tricks#^thm-ca-4-3|Theorem §CA.4.3]] — the vertex integrals give the momentum deltas; the $q$ integral over one of them fixes the momentum of the $\sigma$ line.

> [!remark]- Connections
> - The rules are those of a theory with several fields and several vertices; only the vertices changed with respect to §C6c.8, and they were read off the rewritten Lagrangian — [[§C6c.6 Feynman Rules for Amplitudes#^thm-c6c-6-1|Theorem §C6c.6.1]], [[§C6c.8 The Linear Sigma Model꞉ Fields with an Internal Index#^thm-c6c-8-4|Theorem §C6c.8.4]].
> - $\pi\pi \to \pi\pi$ has the shape of the $2 \to 2$ amplitude of the cubic–quartic theory, three exchange poles and a contact term, with $g \to 2\lambda v$ and the contact term $\lambda \to 2\lambda(\delta\delta + \delta\delta + \delta\delta)$; there the couplings are independent, here $\lambda v^2 = \mu^2$ ties them together and the terms cancel at zero momentum — [[§C6c.6 Feynman Rules for Amplitudes#^thm-c6c-6-4|Theorem §C6c.6.4]].
> - The cubic vertex $-2i\lambda v\,\delta^{ij}$ is that of the $\Phi\phi^2$ theory with $\mu_{\Phi\phi^2} = \lambda v$: a heavy field coupled to pairs of a light one — [[§C6b.6 Decay Kinematics#^mod-c6b-6-4|Model §C6b.6.4]], [[§C6c.4 First Order꞉ Enumerate, then Filter#^ex-c6c-4-4|Example §C6c.4.4]].
> - The sum rule $s + t + u = \sum_nm_n^2$ of Problem Set 1 is what removes the first-order term for one massless pion — [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-1|Theorem §C1a.5.1]], [[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-7|Theorem §C6b.1.7]].
> - With a term $a\Phi^N$ the minimum is a single point, the pions get the mass $a/v$, and the threshold amplitude is proportional to $a$ — [[§C6c.10 The Linear Sigma Model꞉ Explicit Symmetry Breaking|§C6c.10]].
