---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C6a
section: C6a.3
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C6a.2 The Interaction Picture]] · ↑ [[· C6a Interactions and Correlation Functions]] · [[§C6a.4 The Time-Evolution Operator Between Two Times]] →

*Sources: the user's PHY 513 notes, Ch. 13 §13.3 · PHY 513 Lecture 13 (Larsen, 14 Oct 2026), Part B, slides 10–14, and transcript · Peskin & Schroeder, An Introduction to Quantum Field Theory, §4.2, pp. 84–86, eqs. (4.17)–(4.23), Fig. 4.1 · Yu Zhao-Huan, 量子场论讲义, §6.2, eqs. (6.100), (6.103)–(6.121), Fig. 6.2.*

The interacting field is the free field conjugated by one unitary, $\hat\phi_H = U(t)^\dagger\hat\phi_IU(t)$ with $U(t) = e^{i\hat H_0t}e^{-i\hat Ht}$ ([[§C6a.2 The Interaction Picture#^thm-c6a-2-4|Theorem §C6a.2.4]]). This section finds $U$ in terms of things one knows. The key is a first-order differential equation, $i\partial_tU = \hat H_I(t)U$, whose generator is the interaction in the interaction picture ([[§C6a.2 The Interaction Picture#^thm-c6a-2-6|Theorem §C6a.2.6]]). Because $\hat H_I$ is an operator, and operators at different times need not commute, the obvious solution, an exponential of the time integral, is wrong; the correct one orders the operators in time, latest on the left, as in the time-ordered product of [[§C2b.7 Time Ordering, the Feynman Propagator and the iε Prescription#^def-c2b-7-1|Def. §C2b.7.1]]. The result is Dyson's formula, $U = T\{e^{-i\int\hat H_I}\}$. Quantum mechanics proved the same formula for any time-dependent generator, with its convergence for bounded ones ([[§C3.1 The Time-Evolution Operator and the Schrödinger Equation#^thm-c3-1-4|QM Theorem §C3.1.4]]); the field theory adds the generator $\hat H_I$, a polynomial in free fields. The evolution operator $U(t, t')$ between any two times, with which the interacting vacuum of [[§C6a.5 The Interacting Vacuum and the Two-Point Function|§C6a.5]] is built, follows in [[§C6a.4 The Time-Evolution Operator Between Two Times|§C6a.4]]. The one piece of pure mathematics, the $n!$ that converts ordered integrals into integrals over a cube, has its home in [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-4|Theorem §CA.1.4]]. **Setup** ([[§C6a.1 From Free to Interacting Fields#^mod-c6a-1-1|Model §C6a.1.1]]): as in [[§C6a.2 The Interaction Picture|§C6a.2]], $\hat H_0$ and $\hat H_{\rm int}$ on one Hilbert space; every statement is exact operator algebra, with no state and no vacuum; the evolution operator of a source switched on and off ([[§C6a.0 Setups and Observables#^mod-c6a-0-1|Model §C6a.0.1]]) obeys the same equations with a time-dependent $\hat H_I(t)$.

*Conventions* ([[Larsen PHY 513]]): as in [[§C6a.2 The Interaction Picture|§C6a.2]]; $T\{\cdots\}$ is time ordering, braces always; the integrals of this section are over time, $\int_0^tdt'$, and $\hat H_I(t')$ is already integrated over space. Derivatives of operator-valued functions of time are taken on the regularized theory, where every operator is a matrix ([[§C6a.1 From Free to Interacting Fields#^rem-c6a-1-4|§C6a.1, ★ Remark: In what sense φ̂⁴(x) is defined]]).

The derivations differentiate and multiply exponentials of $\hat H_0$ and $\hat H$, always without reordering them; the rules for the matrix exponential they rest on are parts 3–5 of [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-5|Theorem §CB.1.5]] (proved in [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras|§CB.1]], listed at the end): exponents add only for commuting matrices, the adjoint of an exponential, and its derivative on either side,

$$
e^{X + Y} = e^Xe^Y \ \text{if } XY = YX, \qquad (e^X)^\dagger = e^{X^\dagger}, \qquad \frac{d}{ds}e^{sX} = Xe^{sX} = e^{sX}X .
$$

## Unitarity and the equation of motion

> [!theorem] Theorem §C6a.3.1: The Time-Evolution Operator Is Unitary
> $U(t)^\dagger = e^{i\hat Ht}e^{-i\hat H_0t} = U(t)^{-1}$ for every real $t$. $U(t)$ is a product of two unitaries but not itself the exponential of $-i\hat H_{\text{int}}t$ ([[§C6a.2 The Interaction Picture#^thm-c6a-2-5|Theorem §C6a.2.5]]).
>
> *Model:* [[§C6a.1 From Free to Interacting Fields#^mod-c6a-1-1|Model §C6a.1.1]]; *applies:* as in the opening: exact; time-independent $\hat H$; no state.
>
> *Source: PHY 513 Lecture 13, slide 10 ("The time evolution operator is unitary") · the user's PHY 513 notes, Ch. 13 §13.3 (Derivation "$U$ is unitary …", part "Unitarity") · PS §4.2, after eq. (4.17) · Yu §6.2, eq. (6.100)*

^thm-c6a-3-1

> [!derivation]- Derivation
> **Step 1** (the adjoint). The adjoint of a product reverses the order, and $(e^{i\hat At})^\dagger = e^{-i\hat At}$ for Hermitian $\hat A$ and real $t$. So $U(t)^\dagger = (e^{-i\hat Ht})^\dagger(e^{i\hat H_0t})^\dagger = e^{i\hat Ht}e^{-i\hat H_0t}$.
>
> **Step 2** (it is the inverse). $U(t)^\dagger U(t) = e^{i\hat Ht}e^{-i\hat H_0t}e^{i\hat H_0t}e^{-i\hat Ht} = e^{i\hat Ht}e^{-i\hat Ht} = \mathbf 1$, the inner pair cancelling first; likewise $U(t)U(t)^\dagger = e^{i\hat H_0t}e^{-i\hat Ht}e^{i\hat Ht}e^{-i\hat H_0t} = \mathbf 1$.
>
> **What the derivation shows.**
> - Only the Hermiticity of $\hat H$ and $\hat H_0$ was used; the interaction does not threaten unitarity at this level.

^der-c6a-3-1

*Uses:* [[§C6a.2 The Interaction Picture#^def-c6a-2-2|Def. §C6a.2.2]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-5|Theorem §CB.1.5]]

> [!theorem] Theorem §C6a.3.2: The Equation of Motion of the Time-Evolution Operator
> $U(t)$ is the solution of the first-order linear initial-value problem
>
> $$
> i\,\partial_tU(t) = \hat H_I(t)\,U(t), \qquad U(0) = \mathbf 1 ,
> $$
>
> with $\hat H_I(t) = e^{i\hat H_0t}\hat H_{\text{int}}e^{-i\hat H_0t}$ ([[§C6a.2 The Interaction Picture#^def-c6a-2-3|Def. §C6a.2.3]]). Equivalently, it solves the integral equation $U(t) = \mathbf 1 - i\int_0^tdt_1\,\hat H_I(t_1)\,U(t_1)$.
>
> *Model:* [[§C6a.1 From Free to Interacting Fields#^mod-c6a-1-1|Model §C6a.1.1]]; *applies:* as in the opening: exact; for a time-dependent $\hat H_{\rm int}(t)$ ([[§C6a.0 Setups and Observables#^mod-c6a-0-1|Model §C6a.0.1]]) the equation, with $\hat H_I(t) = e^{i\hat H_0t}\hat H_{\rm int}(t)e^{-i\hat H_0t}$, defines $U$.
>
> *Source: PHY 513 Lecture 13, slides 10–11 · the user's PHY 513 notes, Ch. 13 §13.3, eq. (Uode) · PS §4.2, eq. (4.18) · Yu §6.2, eqs. (6.104)–(6.105)*

^thm-c6a-3-2

> [!derivation]- Derivation
> **Step 1** (differentiate each exponential). $\hat H_0$ commutes with $e^{i\hat H_0t}$ (a function of $\hat H_0$), so $\partial_te^{i\hat H_0t} = i\hat H_0e^{i\hat H_0t} = e^{i\hat H_0t}\,i\hat H_0$: the factor may be written on either side. Likewise $\partial_te^{-i\hat Ht} = -i\hat He^{-i\hat Ht} = e^{-i\hat Ht}(-i\hat H)$. (Term-by-term differentiation of the exponential series, legitimate for matrices, [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-5|Theorem §CB.1.5]].)
>
> **Step 2** (the product rule, nothing reordered). Choose the forms that put both Hamiltonians in the middle:
>
> $$
> \partial_tU(t) = \bigl(e^{i\hat H_0t}\,i\hat H_0\bigr)e^{-i\hat Ht} + e^{i\hat H_0t}\bigl(-i\hat H\,e^{-i\hat Ht}\bigr) = e^{i\hat H_0t}\,\bigl(i\hat H_0 - i\hat H\bigr)\,e^{-i\hat Ht} .
> $$
>
> Multiply by $i$: $i\partial_tU(t) = e^{i\hat H_0t}(\hat H - \hat H_0)e^{-i\hat Ht}$. No two operators have been exchanged, which matters because $\hat H_0$ and $\hat H$ do not commute.
>
> **Step 3** (the interaction). $\hat H - \hat H_0 = \hat H_{\text{int}}$ ([[§C6a.1 From Free to Interacting Fields#^def-c6a-1-1|Def. §C6a.1.1]]), so $i\partial_tU = e^{i\hat H_0t}\hat H_{\text{int}}e^{-i\hat Ht}$. This is still a mixture of free and full evolution.
>
> **Step 4** (insert the identity). Write $e^{-i\hat Ht} = e^{-i\hat H_0t}e^{i\hat H_0t}e^{-i\hat Ht}$:
>
> $$
> i\partial_tU(t) = \underbrace{\bigl(e^{i\hat H_0t}\hat H_{\text{int}}e^{-i\hat H_0t}\bigr)}_{\hat H_I(t)}\,\underbrace{\bigl(e^{i\hat H_0t}e^{-i\hat Ht}\bigr)}_{U(t)} = \hat H_I(t)\,U(t) .
> $$
>
> **Step 5** (initial value and integral form). $U(0) = e^0e^0 = \mathbf 1$. Integrate the equation from $0$ to $t$ (fundamental theorem of calculus, [[§34 Fundamental Theorem of Calculus#^thm-34-1|451 Thm. §34.1]], entry by entry; the integrand $\hat H_I(t_1)U(t_1)$ is continuous in $t_1$), using $\partial_{t_1}U = -i\hat H_I(t_1)U(t_1)$:
>
> $$
> U(t) - U(0) = \int_0^tdt_1\,\partial_{t_1}U(t_1) = -i\int_0^tdt_1\,\hat H_I(t_1)\,U(t_1) \quad\Longrightarrow\quad U(t) = \mathbf 1 - i\int_0^tdt_1\,\hat H_I(t_1)\,U(t_1) .
> $$
>
> Conversely, differentiating the integral equation gives $\partial_tU(t) = -i\hat H_I(t)U(t)$, and at $t = 0$ the integral vanishes, $U(0) = \mathbf 1$.
>
> ⚑ By-product: no $\partial_t\hat H$ term appears, because $\hat H$ and $\hat H_0$ do not depend on time; $\hat H_I(t)$ acquired its time dependence only at the end, by conjugation with $e^{i\hat H_0t}$ → [[§C6a.3 The Time-Evolution Operator and Time Ordering#^rem-c6a-3-1|Remark: Space integrals and time integrals]].
>
> ⚑ By-product: a first-order linear equation with one initial condition has at most one solution; this is what identifies every candidate formula for $U$ below → [[§C6a.3 The Time-Evolution Operator and Time Ordering#^lem-c6a-3-3|Lemma §C6a.3.3]].
>
> **What the derivation shows.**
> - The generator of $U$ is the interaction alone, in the interaction picture: $\hat H_0$ dropped out because the free evolution has been taken out of $U$ by construction.
> - This is the Schrödinger equation of interaction-picture states ([[§C9.6 The Interaction Picture and the Atom–Field Interaction#^thm-c9-6-1|QM Theorem §C9.6.1]], 1), here as an equation for the operator.

^der-c6a-3-2

*Uses:* [[§C6a.2 The Interaction Picture#^def-c6a-2-2|Def. §C6a.2.2]], [[§C6a.2 The Interaction Picture#^def-c6a-2-3|Def. §C6a.2.3]], [[§C6a.1 From Free to Interacting Fields#^def-c6a-1-1|Def. §C6a.1.1]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-5|Theorem §CB.1.5]], [[§34 Fundamental Theorem of Calculus#^thm-34-1|451 Thm. §34.1]]

> [!theorem] Lemma §C6a.3.3: The Solution Is Unique
> On the regularized theory, let $\hat H_I(t)^\dagger = \hat H_I(t)$, and let $X(t)$ and $W(t)$ be differentiable operator-valued functions of $t$ with
>
> $$
> i\,\partial_tX = \hat H_I(t)\,X, \qquad i\,\partial_tW = \hat H_I(t)\,W, \qquad X(t_0) = W(t_0) = \mathbf 1 .
> $$
>
> If $X(t)$ is unitary for every $t$, then $W(t) = X(t)$ for every $t$. In particular ($X = U$, $t_0 = 0$; [[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-1|Theorem §C6a.3.1]], [[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-2|Theorem §C6a.3.2]]): every solution of $i\partial_tW = \hat H_I(t)W$ with $W(0) = \mathbf 1$ is $U(t)$.
>
> *Model:* [[§C6a.1 From Free to Interacting Fields#^mod-c6a-1-1|Model §C6a.1.1]]; *applies:* as in the opening: exact, on the regularized theory; any Hermitian operator-valued $\hat H_I(t)$, also that of a time-dependent $\hat H_{\rm int}(t)$ ([[§C6a.0 Setups and Observables#^mod-c6a-0-1|Model §C6a.0.1]]); no state.
>
> *Source: the user's PHY 513 notes, Ch. 13 §13.3 (Derivation "General reference times", "Proof of the second equality (filled in)": "A first-order linear equation has a unique solution for given initial data") · proof written here*

^lem-c6a-3-3

> [!derivation]- Derivation
> **Step 1** (the case $X = U$, $t_0 = 0$). Both $U$ ([[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-2|Theorem §C6a.3.2]]) and $W$ solve $i\partial_tX = \hat H_I(t)X$, $X(0) = \mathbf 1$. Consider $U(t)^\dagger W(t)$. The adjoint of $i\partial_tU = \hat H_IU$, with $\hat H_I^\dagger = \hat H_I$ (a unitary conjugate of the Hermitian $\hat H_{\text{int}}$), is
>
> $$
> (i\partial_tU)^\dagger = -i\,\partial_tU^\dagger = (\hat H_IU)^\dagger = U^\dagger\hat H_I \quad\Longrightarrow\quad \partial_tU^\dagger = i\,U^\dagger\hat H_I, \qquad \partial_tW = -i\,\hat H_IW .
> $$
>
> Then
>
> $$
> \partial_t\bigl(U^\dagger W\bigr) = (\partial_tU^\dagger)W + U^\dagger(\partial_tW) = \bigl(iU^\dagger\hat H_I\bigr)W + U^\dagger\bigl(-i\hat H_IW\bigr) = 0 ,
> $$
>
> so $U(t)^\dagger W(t) = U(0)^\dagger W(0) = \mathbf 1$, and multiplying by $U(t)$ on the left (unitarity, [[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-1|Theorem §C6a.3.1]]) gives $W(t) = U(t)$.
>
> **Step 2** (general $X$ and $t_0$). Step 1 used of $U$ only its equation, its initial value and its unitarity (to pass from $U^\dagger W = \mathbf 1$ to $W = U$), and of $\hat H_I$ only $\hat H_I^\dagger = \hat H_I$. With $X$ in place of $U$ and $t_0$ in place of $0$ the same lines read
>
> $$
> \partial_tX^\dagger = i\,X^\dagger\hat H_I, \qquad \partial_t\bigl(X^\dagger W\bigr) = \bigl(iX^\dagger\hat H_I\bigr)W + X^\dagger\bigl(-i\hat H_IW\bigr) = 0, \qquad X(t_0)^\dagger W(t_0) = \mathbf 1 \quad\Longrightarrow\quad W(t) = X(t) .
> $$
>
> **What the derivation shows.**
> - A first-order linear equation with one initial condition has at most one solution; nothing about the form of $W$ is used, only that it solves the equation.
> - Used next: the exponential for commuting generators ([[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-5|Theorem §C6a.3.5]], 2), Dyson's formula ([[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-7|Theorem §C6a.3.7]]) and its form between two times ([[§C6a.4 The Time-Evolution Operator Between Two Times#^thm-c6a-4-2|Theorem §C6a.4.2]]).

^der-c6a-3-3

*Uses:* [[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-1|Theorem §C6a.3.1]], [[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-2|Theorem §C6a.3.2]]

> [!remark] Remark: Space integrals and time integrals
> Two questions arise. *Is $\mathcal H_{\text{int}}$ a density?* Yes: every $\hat H$ in this chapter is a Hamiltonian, already integrated over space, $\hat H = \int d^3x\,\hat{\mathcal H}$, with a density at each point of space at a given time. The Hamiltonian itself is never integrated over time. The time integrals that appear from here on come from solving the equation of motion of $U$; they are something extra, and together with the space integral of $\hat H_I$ they make the spacetime integrals $\int d^4z$ of perturbation theory ([[§C6a.4 The Time-Evolution Operator Between Two Times#^ex-c6a-4-1|Example §C6a.4.1]]). *If $\hat H_I$ depends on time, why were there no $\partial_t\hat H$ terms?* Because in $U(t) = e^{i\hat H_0t}e^{-i\hat Ht}$ the Hamiltonians do not depend on time: they are conserved, evaluated once at the reference time. $\hat H_I(t)$ became time dependent only by being conjugated with $e^{i\hat H_0t}$ ([[§C6a.2 The Interaction Picture#^thm-c6a-2-6|Theorem §C6a.2.6]]).
>
> *Source: PHY 513 Lecture 13, transcript (two questions after slide 10) · the user's PHY 513 notes, Ch. 13 §13.3 (paragraphs "Space integrals and time integrals", "Where the time dependence came from")*

^rem-c6a-3-1

## The naive solution and why it fails

> [!theorem] Theorem §C6a.3.4: The Interaction Hamiltonians at Two Times
> For all $t_1$, $t_2$, with $x = (t_1, \mathbf x)$, $y = (t_2, \mathbf y)$,
>
> $$
> [\hat H_I(t_1), \hat H_I(t_2)] = \Bigl(\frac{\lambda}{4!}\Bigr)^2\int d^3x\,d^3y\;4iD(x - y)\sum_{k=0}^3\hat\phi_I(y)^k\,\hat\phi_I(x)^3\,\hat\phi_I(y)^{3-k} ,
> $$
>
> with $D$ the commutator function ([[§C2b.5 Microcausality and the Commutator Function#^def-c2b-5-1|Def. §C2b.5.1]]). The $c$-number coefficient $D(x - y)$ vanishes at spacelike separation, in particular for $t_1 = t_2$, $\mathbf x \ne \mathbf y$, but not inside the light cone. For $t_1 \ne t_2$ the integration region always reaches inside the cone.
>
> *Model:* [[§C6a.1 From Free to Interacting Fields#^mod-c6a-1-1|Model §C6a.1.1]]; *applies:* as in the opening: exact operator identity, every $\lambda$; it uses only the free commutator $iD(x - y)$ of $\hat\phi_I$ (free field, [[§C2a.1 Canonical Quantization of Fields#^mod-c2a-1-1|Model §C2a.1.1]]).
>
> *Source: PHY 513 Lecture 13, transcript ("There's no guarantee that they will commute, and in fact, they really won't") · the user's PHY 513 notes, Ch. 13 §13.3 (paragraph "How to read $T\{e^{\cdots}\}$", numerical check) · the commutator written here from [[§C2b.5 Microcausality and the Commutator Function#^thm-c2b-5-2|Theorem §C2b.5.2]]*

^thm-c6a-3-4

> [!derivation]- Derivation
> **Step 1** (the two fields). Write $\hat A = \hat\phi_I(x)$, $\hat B = \hat\phi_I(y)$. By [[§C6a.2 The Interaction Picture#^thm-c6a-2-3|Theorem §C6a.2.3]] their commutator is a number:
>
> $$
> [\hat A, \hat B] = iD(x - y)\,\mathbf 1 \equiv c .
> $$
>
> **Step 2** (fourth power against one field). $[\hat A^{m+1}, \hat B] = \hat A[\hat A^m, \hat B] + [\hat A, \hat B]\hat A^m$, and $c$ commutes with everything:
>
> $$
> [\hat A^2, \hat B] = \hat Ac + c\hat A = 2c\hat A, \qquad [\hat A^3, \hat B] = \hat A\,2c\hat A + c\hat A^2 = 3c\hat A^2, \qquad [\hat A^4, \hat B] = \hat A\,3c\hat A^2 + c\hat A^3 = 4c\hat A^3 .
> $$
>
> **Step 3** (fourth power against fourth power). $[X, \hat B^4] = \sum_{k=0}^3\hat B^k[X, \hat B]\hat B^{3-k}$ with $X = \hat A^4$. Written out:
>
> $$
> [\hat A^4, \hat B^4] = 4c\bigl(\hat A^3\hat B^3 + \hat B\hat A^3\hat B^2 + \hat B^2\hat A^3\hat B + \hat B^3\hat A^3\bigr) = 4iD(x - y)\sum_{k=0}^3\hat B^k\hat A^3\hat B^{3-k} .
> $$
>
> **Step 4** (integrate). $\hat H_I(t_k) = \int d^3x\,\frac{\lambda}{4!}\hat\phi_I(t_k, \mathbf x)^4$ ([[§C6a.2 The Interaction Picture#^thm-c6a-2-6|Theorem §C6a.2.6]]), and the commutator is bilinear:
>
> $$
> [\hat H_I(t_1), \hat H_I(t_2)] = \Bigl(\frac{\lambda}{4!}\Bigr)^2\int d^3x\,d^3y\;[\hat\phi_I(x)^4, \hat\phi_I(y)^4] ,
> $$
>
> which with Step 3 is the statement.
>
> **Step 5** (where the coefficient vanishes). $D(\xi) = 0$ for $\xi^2 < 0$ ([[§C2b.5 Microcausality and the Commutator Function#^thm-c2b-5-5|Theorem §C2b.5.5]]). Inside the cone, with $\tau = \sqrt{\xi^2}$ ([[§C2b.5 Microcausality and the Commutator Function#^thm-c2b-5-9|Theorem §C2b.5.9]]),
>
> $$
> D(\xi) = \operatorname{sgn}(\xi^0)\,\frac{m\,J_1(m\tau)}{4\pi\tau} \not\equiv 0 .
> $$
>
> For $t_1 \ne t_2$ the set $\{|\mathbf x - \mathbf y| < |t_1 - t_2|\}$, where $\xi^2 > 0$, has positive volume in $(\mathbf x, \mathbf y)$.
>
> **What the derivation shows.**
> - Equal-time Hamiltonians commute; at different times the free fields of the two vertices fail to commute inside the light cone, and nothing makes the operator integral vanish. In the one-oscillator model of [[§C6a.5 The Interacting Vacuum and the Two-Point Function#^ex-c6a-5-2|Example §C6a.5.2]] (pointer) the naive exponential misses $U(0.7)$ by $0.91$ in the largest matrix element (the user's notes; rerun), while the time-ordered product reproduces it.
> - Used next: part 3 of [[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-5|Theorem §C6a.3.5]], the naive exponential.

^der-c6a-3-4

*Uses:* [[§C6a.2 The Interaction Picture#^thm-c6a-2-3|Theorem §C6a.2.3]], [[§C6a.2 The Interaction Picture#^thm-c6a-2-6|Theorem §C6a.2.6]], [[§C2b.5 Microcausality and the Commutator Function#^def-c2b-5-1|Def. §C2b.5.1]], [[§C2b.5 Microcausality and the Commutator Function#^thm-c2b-5-2|Theorem §C2b.5.2]], [[§C2b.5 Microcausality and the Commutator Function#^thm-c2b-5-5|Theorem §C2b.5.5]], [[§C2b.5 Microcausality and the Commutator Function#^thm-c2b-5-9|Theorem §C2b.5.9]]

> [!theorem] Theorem §C6a.3.5: The Exponential Solves the Equation Only for Commuting Generators
> Let $\hat A(t) = \int_0^tdt'\,\hat H_I(t')$.
> 1. The derivative of the $n$-th power is the sum of $n$ terms with $\hat H_I(t)$ in each of the $n$ positions:
>
> $$
> \partial_t\bigl(\hat A(t)^n\bigr) = \sum_{k=0}^{n-1}\hat A(t)^k\,\hat H_I(t)\,\hat A(t)^{n-1-k} .
> $$
>
> 2. If $[\hat H_I(t_1), \hat H_I(t_2)] = 0$ for all $t_1, t_2 \in [0, t]$, then $U(t) = e^{-i\hat A(t)} = e^{-i\int_0^tdt'\,\hat H_I(t')}$.
> 3. In general the $n$ terms of part 1 are different operators, and $e^{-i\hat A(t)}$ does not satisfy $i\partial_tU = \hat H_I(t)U$.
>
> *Model:* any; *applies:* any operator-valued function $\hat H_I(t)$, independent of the dynamics; exact.
>
> *Source: PHY 513 Lecture 13, slides 11–12 ("Naïve solution (pretend $H_I(t)$ a function, not an operator)", "Correct for any time-dependent function $H_I(t)$. Incorrect for operator $H_I(t)$", "Differentiation w.r.t. $t$ gives $n$ terms with $H_I(t)$ at distinct positions, not always to the left") · the user's PHY 513 notes, Ch. 13 §13.3 (Derivation "The naïve solution, and why it fails") · PS §4.2, p. 84 ("should look something like $U \sim \exp(-iH_It)$") · [[§C3.1 The Time-Evolution Operator and the Schrödinger Equation#^thm-c3-1-4|QM Theorem §C3.1.4]], 2*

^thm-c6a-3-5

> [!derivation]- Derivation
> **Step 1** (the $n$-th term as an $n$-fold integral). The integration variables need different names (slide 12):
>
> $$
> \frac{(-i)^n}{n!}\hat A(t)^n = \frac{(-i)^n}{n!}\int_0^tdt_1\,\hat H_I(t_1)\int_0^tdt_2\,\hat H_I(t_2)\cdots\int_0^tdt_n\,\hat H_I(t_n) .
> $$
>
> **Step 2** (part 1: the product rule without reordering). $\partial_t\hat A(t) = \hat H_I(t)$ (fundamental theorem of calculus, [[§34 Fundamental Theorem of Calculus#^thm-34-4|451 Thm. §34.4]]). The product rule differentiates one factor at a time and leaves it in its place:
>
> $$
> \begin{aligned}
> \partial_t\bigl(\hat A^2\bigr) &= \hat H_I(t)\,\hat A + \hat A\,\hat H_I(t) ,\\
> \partial_t\bigl(\hat A^3\bigr) &= \hat H_I(t)\,\hat A^2 + \hat A\,\hat H_I(t)\,\hat A + \hat A^2\,\hat H_I(t) ,\\
> \partial_t\bigl(\hat A^n\bigr) &= \underbrace{\hat H_I(t)\hat A\cdots\hat A}_{k = 0} + \underbrace{\hat A\,\hat H_I(t)\cdots\hat A}_{k = 1} + \cdots + \underbrace{\hat A\cdots\hat A\,\hat H_I(t)}_{k = n-1} ,
> \end{aligned}
> $$
>
> which is part 1: instead of $n$ identical expressions there are $n$ different ones, with $H$ at different positions.
>
> **Step 3** (part 2: commuting generators). If all $\hat H_I(t')$, $t' \in [0, t]$, commute, then
>
> $$
> [\hat H_I(t), \hat A(t)] = \int_0^tdt'\,[\hat H_I(t), \hat H_I(t')] = 0 ,
> $$
>
> so in each term of part 1 the factor $\hat H_I(t)$ can be moved to the front, $\hat A^k\hat H_I(t)\hat A^{n-1-k} = \hat H_I(t)\hat A^{n-1}$, and $\partial_t\hat A^n = n\,\hat H_I(t)\hat A^{n-1}$. Then
>
> $$
> i\partial_t\sum_{n=0}^\infty\frac{(-i)^n}{n!}\hat A^n = \sum_{n=1}^\infty i\,\frac{(-i)^n}{n!}\,n\,\hat H_I(t)\hat A^{n-1} = \hat H_I(t)\sum_{n=1}^\infty\frac{(-i)^{n-1}}{(n-1)!}\hat A^{n-1} = \hat H_I(t)\,e^{-i\hat A(t)},
> $$
>
> using $i(-i)^n = (-i)^{n-1}$ (since $i\cdot(-i) = 1$) and $n/n! = 1/(n-1)!$; the $n = 0$ term is constant. (Differentiating the series term by term is legitimate: on the regularized theory $\|\hat H_I(t')\| \le h$, the differentiated series is dominated by $\sum h(ht)^{n-1}/(n-1)!$ and converges uniformly, [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-3|Theorem §CA.1.3]].) At $t = 0$, $\hat A = 0$ and $e^0 = \mathbf 1$. By uniqueness ([[§C6a.3 The Time-Evolution Operator and Time Ordering#^lem-c6a-3-3|Lemma §C6a.3.3]], with $X = U$, $W = e^{-i\hat A}$, $t_0 = 0$) this is $U(t)$.
>
> **Step 4** (part 3). Without commutativity the $n$ terms of part 1 differ, and only the first, $\hat H_I(t)\hat A^{n-1}$, has $\hat H_I(t)$ on the left, where the equation $i\partial_tU = \hat H_I(t)U$ requires it to act. At second order: the term of $e^{-i\hat A}$ is $\frac{(-i)^2}{2}\hat A^2$, and the equation requires $i\partial_t$ of it to be $\hat H_I(t)$ times the first-order term $-i\hat A$:
>
> $$
> i\partial_t\Bigl(\frac{(-i)^2}{2}\hat A^2\Bigr) = \frac{-i}{2}\bigl(\hat H_I(t)\hat A + \hat A\hat H_I(t)\bigr) = \hat H_I(t)\,(-i\hat A) + \frac{i}{2}\,[\hat H_I(t), \hat A(t)] ,
> $$
>
> off by $\frac{i}{2}[\hat H_I(t), \hat A(t)] = \frac{i}{2}\int_0^tdt'\,[\hat H_I(t), \hat H_I(t')]$, which is not zero ([[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-4|Theorem §C6a.3.4]]). For a c-number function $h(t)$ in place of $\hat H_I(t)$ the commutator vanishes: this is why the naive solution is "correct for any time-dependent function."
>
> **What the derivation shows.**
> - The exponential reorders operators implicitly: writing $(\int\hat H_I)^n$ and differentiating as if it were a number moves $\hat H_I(t)$ to the left of operators at earlier times.
> - The repair keeps the series and fixes the order of each term ([[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-7|Theorem §C6a.3.7]]).

^der-c6a-3-5

*Uses:* [[§34 Fundamental Theorem of Calculus#^thm-34-4|451 Thm. §34.4]], [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-3|Theorem §CA.1.3]], [[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-2|Theorem §C6a.3.2]], [[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-4|Theorem §C6a.3.4]], [[§C6a.3 The Time-Evolution Operator and Time Ordering#^lem-c6a-3-3|Lemma §C6a.3.3]]

> [!caution] Caution: A factor on slide 12
> Slide 12's commuting case reads $\to H_I(t)\sum_{n=1}^\infty\frac{1}{(n-1)!}\bigl(\int_0^tdt'H_I(t')\bigr)^{n-1} = H_I(t)U(t)$. The factor $(-i)^{n-1}$ is missing from the sum: $i\partial_t$ of $\frac{(-i)^n}{n!}(\int H_I)^n$ is $\frac{(-i)^{n-1}}{(n-1)!}H_I(t)(\int H_I)^{n-1}$ ([[§C6a.3 The Time-Evolution Operator and Time Ordering#^der-c6a-3-5|Derivation §C6a.3.5]], Step 3). Without it the sum would be $H_I(t)e^{+\int H_I}$, not $H_I(t)U(t)$.
>
> *Source: PHY 513 Lecture 13, slide 12 (page image)*

^cau-c6a-3-1

## Time ordering and the Dyson series

> [!definition] Definition §C6a.3.1: Time-Ordered Exponential
> For $t \ge t'$ the **time-ordered exponential** of $\hat H_I$ is the series
>
> $$
> T\Bigl\{\exp\Bigl[-i\int_{t'}^tdt''\,\hat H_I(t'')\Bigr]\Bigr\} \equiv \sum_{n=0}^\infty\frac{(-i)^n}{n!}\int_{t'}^tdt_1\int_{t'}^tdt_2\cdots\int_{t'}^tdt_n\;T\bigl\{\hat H_I(t_1)\hat H_I(t_2)\cdots\hat H_I(t_n)\bigr\} ,
> $$
>
> the exponential series with each term time-ordered: $T\{\hat H_I(t_1)\cdots\hat H_I(t_n)\}$ arranges the factors by decreasing time label, the latest on the left and the earliest on the right, as for fields ([[§C2b.7 Time Ordering, the Feynman Propagator and the iε Prescription#^def-c2b-7-1|Def. §C2b.7.1]], applied to operators labelled by a time). The $n = 0$ term is $\mathbf 1$. It is not an exponential: it is the series together with the instruction to time-order each term.
>
> *Model:* any; *applies:* any operator-valued $\hat H_I(t)$: that of [[§C6a.1 From Free to Interacting Fields#^mod-c6a-1-1|Model §C6a.1.1]] or of a source ([[§C6a.0 Setups and Observables#^mod-c6a-0-1|Model §C6a.0.1]]); a series of operators, convergent on the regularized theory ([[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-7|Theorem §C6a.3.7]]).
>
> *Source: PHY 513 Lecture 13, slide 13 ("$T$ = time-ordering: order $H_I$'s so smallest $t$ is on the right") · the user's PHY 513 notes, Ch. 13 §13.3, eq. (Dyson) · PS §4.2, eqs. (4.22)–(4.23) ("the time-ordering of the exponential is just defined as the Taylor series with each term time-ordered") · Yu §6.2, eqs. (6.107), (6.119)*

^def-c6a-3-1

> [!theorem] Theorem §C6a.3.6: Ordered Iterated Integrals Are Time-Ordered Cube Integrals
> For $t \ge t'$ and $n \ge 1$,
>
> $$
> \frac{1}{n!}\int_{t'}^tdt_1\cdots\int_{t'}^tdt_n\;T\bigl\{\hat H_I(t_1)\cdots\hat H_I(t_n)\bigr\} = \int_{t'}^tdt_1\,\hat H_I(t_1)\int_{t'}^{t_1}dt_2\,\hat H_I(t_2)\cdots\int_{t'}^{t_{n-1}}dt_n\,\hat H_I(t_n) ,
> $$
>
> where on the right each $t_{k+1}$ runs only up to $t_k$, so the factors already stand in time order.
>
> *Model:* any; *applies:* an identity for any operator-valued function $\hat H_I(t)$, independent of the dynamics.
>
> *Source: PHY 513 Lecture 13, slide 13 ("Example") · the user's PHY 513 notes, Ch. 13 §13.3 (Derivation "The time-ordered exponential (Dyson series)", paragraph "Removing the $n!$") · PS §4.2, eq. (4.21), Fig. 4.1, and the identity before eq. (4.22) · Yu §6.2, eqs. (6.116)–(6.118), Fig. 6.2*

^thm-c6a-3-6

> [!derivation]- Derivation
> **Step 1** ($n = 2$, the square as two triangles). The square $[t', t]^2$ is the union of the triangle $t_1 \ge t_2$ and the triangle $t_2 \ge t_1$, which meet only on the diagonal, a line of zero area (PS Fig. 4.1). On the first, $T\{\hat H_I(t_1)\hat H_I(t_2)\} = \hat H_I(t_1)\hat H_I(t_2)$; on the second, $T$ reorders it to $\hat H_I(t_2)\hat H_I(t_1)$. So
>
> $$
> \int_{t'}^tdt_1\int_{t'}^tdt_2\,T\{\hat H_I(t_1)\hat H_I(t_2)\} = \int_{t_1 \ge t_2}\hat H_I(t_1)\hat H_I(t_2) + \int_{t_2 \ge t_1}\hat H_I(t_2)\hat H_I(t_1) .
> $$
>
> **Step 2** (relabel the second triangle). In the second integral rename the variables $t_1 \leftrightarrow t_2$ (a permutation of coordinates, Jacobian of absolute value $1$, mapping the triangle $t_2 \ge t_1$ onto $t_1 \ge t_2$): it becomes $\int_{t_1 \ge t_2}\hat H_I(t_1)\hat H_I(t_2)$, equal to the first. Writing the triangle as an iterated integral, $t_2$ from $t'$ to $t_1$ (Fubini, [[§23 Fubini's Theorem#^thm-23-2|452 Thm. §23.2]]),
>
> $$
> \int_{t'}^tdt_1\int_{t'}^tdt_2\,T\{\hat H_I(t_1)\hat H_I(t_2)\} = 2\int_{t'}^tdt_1\int_{t'}^{t_1}dt_2\,\hat H_I(t_1)\hat H_I(t_2) ,
> $$
>
> which is the statement for $n = 2$ (PS eq. (4.21); Yu eq. (6.117)). The integrand $T\{\cdots\}$ is symmetric about the diagonal: "the double integral on the right-hand side just counts everything twice" (PS).
>
> **Step 3** ($n = 3$, the cube as six regions). Write $H_k \equiv \hat H_I(t_k)$. The cube $[t', t]^3$ is the union of the $3! = 6$ regions $R_\sigma = \{t_{\sigma(1)} \ge t_{\sigma(2)} \ge t_{\sigma(3)}\}$, overlapping only where two times coincide (zero volume). On each, $T$ puts the latest on the left:
>
> $$
> \begin{array}{lll}
> R_{123}\colon\ t_1 \ge t_2 \ge t_3, & T\{H_1H_2H_3\} = H_1H_2H_3; \qquad & R_{213}\colon\ t_2 \ge t_1 \ge t_3, \quad T\{\cdots\} = H_2H_1H_3;\\
> R_{132}\colon\ t_1 \ge t_3 \ge t_2, & T\{\cdots\} = H_1H_3H_2; & R_{231}\colon\ t_2 \ge t_3 \ge t_1, \quad T\{\cdots\} = H_2H_3H_1;\\
> R_{312}\colon\ t_3 \ge t_1 \ge t_2, & T\{\cdots\} = H_3H_1H_2; & R_{321}\colon\ t_3 \ge t_2 \ge t_1, \quad T\{\cdots\} = H_3H_2H_1.
> \end{array}
> $$
>
> On $R_\sigma$ rename $s_k = t_{\sigma(k)}$ (a permutation of coordinates, $|\det| = 1$), which maps $R_\sigma$ onto $\Delta_3 = \{t \ge s_1 \ge s_2 \ge s_3 \ge t'\}$ and the integrand onto $\hat H_I(s_1)\hat H_I(s_2)\hat H_I(s_3)$. For example on $R_{231}$: $s_1 = t_2$, $s_2 = t_3$, $s_3 = t_1$, and $H_2H_3H_1 = \hat H_I(s_1)\hat H_I(s_2)\hat H_I(s_3)$. Each of the six integrals is therefore the same, and
>
> $$
> \int_{[t', t]^3}d^3t\;T\{H_1H_2H_3\} = \sum_{\sigma\in S_3}\int_{R_\sigma}d^3t\;T\{H_1H_2H_3\} = 6\int_{t'}^tds_1\int_{t'}^{s_1}ds_2\int_{t'}^{s_2}ds_3\;\hat H_I(s_1)\hat H_I(s_2)\hat H_I(s_3) .
> $$
>
> **Step 4** (general $n$). On the regularized theory $\hat H_I(t'')$ is a matrix depending continuously on $t''$, and $T\{\hat H_I(t_1)\cdots\hat H_I(t_n)\}$ is the ordered product $\mathcal O(t_1, \dots, t_n)$ of [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-4|Theorem §CA.1.4]] with $f = \hat H_I$ on $[a, b] = [t', t]$. The same three moves as in Step 3, for the $n!$ permutations $\sigma \in S_n$:
>
> $$
> [t', t]^n = \bigcup_{\sigma\in S_n}R_\sigma, \qquad T\{\cdots\}\big|_{R_\sigma} = \hat H_I(t_{\sigma(1)})\cdots\hat H_I(t_{\sigma(n)}), \qquad s_k = t_{\sigma(k)}\colon\ R_\sigma \to \Delta_n,\ |\det| = 1 ,
> $$
>
> so (part 2 of that theorem)
>
> $$
> \int_{[t', t]^n}d^nt\;T\bigl\{\hat H_I(t_1)\cdots\hat H_I(t_n)\bigr\} = \sum_{\sigma\in S_n}\int_{\Delta_n}d^ns\;\hat H_I(s_1)\cdots\hat H_I(s_n) = n!\int_{t'}^tds_1\int_{t'}^{s_1}ds_2\cdots\int_{t'}^{s_{n-1}}ds_n\;\hat H_I(s_1)\cdots\hat H_I(s_n) .
> $$
>
> Divide by $n!$ and rename $s_k \to t_k$.
>
> ⚑ By-product: at coincident times the order is irrelevant, both because $\hat H_I(t_1) = \hat H_I(t_2)$ there and because the coincidence set has zero volume; time ordering of $\hat H_I$'s therefore needs no convention at equal times, unlike $\hat\phi$ with $\hat\pi$ ([[§C2b.7 Time Ordering, the Feynman Propagator and the iε Prescription#^cau-c2b-7-1|§C2b.7, Caution: The step function at zero]]).
>
> **What the derivation shows.**
> - The $\frac{1}{n!}$ of the exponential series is exactly what is needed to pick one of the $n!$ time orderings: the $1/n!$ compensates the sum over all possible orderings, leaving effectively one ordering, the time-ordered one.
> - Used next: Dyson's formula ([[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-7|Theorem §C6a.3.7]]).

^der-c6a-3-6

*Uses:* [[§C2b.7 Time Ordering, the Feynman Propagator and the iε Prescription#^def-c2b-7-1|Def. §C2b.7.1]], [[§23 Fubini's Theorem#^thm-23-2|452 Thm. §23.2]], [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-4|Theorem §CA.1.4]]

> [!theorem] Theorem §C6a.3.7: Dyson's Formula
> For $t \ge 0$,
>
> $$
> U(t) = T\Bigl\{\exp\Bigl[-i\int_0^tdt'\,\hat H_I(t')\Bigr]\Bigr\} = \mathbf 1 + \sum_{n=1}^\infty(-i)^n\int_0^tdt_1\int_0^{t_1}dt_2\cdots\int_0^{t_{n-1}}dt_n\;\hat H_I(t_1)\hat H_I(t_2)\cdots\hat H_I(t_n) ,
> $$
>
> the **Dyson series**. On the regularized theory, with $\|\hat H_I(t')\| \le h$, the series converges absolutely and uniformly on bounded intervals; in the field theory it is used as a formal power series in $\lambda$.
>
> *Model:* [[§C6a.1 From Free to Interacting Fields#^mod-c6a-1-1|Model §C6a.1.1]]; *applies:* as in the opening: exact on the regularized theory, a formal power series in $\lambda$ in the field theory; for a source switched on and off ([[§C6a.0 Setups and Observables#^mod-c6a-0-1|Model §C6a.0.1]]) the right side is $U$ by definition ([[§C6a.0 Setups and Observables#^der-c6a-0-4|Derivation §C6a.0.4]], Step 2).
>
> *Source: PHY 513 Lecture 13, slides 13–14 ("Correct solution") · the user's PHY 513 notes, Ch. 13 §13.3, eq. (Dyson) · PS §4.2, eqs. (4.20), (4.22) · Yu §6.2, eqs. (6.105)–(6.106), (6.119)*

^thm-c6a-3-7

> [!derivation]- Derivation
> **Step 1** (the ordered series). Call $W_0(t) = \mathbf 1$ and $W_n(t) = (-i)^n\int_0^tdt_1\int_0^{t_1}dt_2\cdots\int_0^{t_{n-1}}dt_n\,\hat H_I(t_1)\cdots\hat H_I(t_n)$ for $n \ge 1$, and $W = \sum_nW_n$. By [[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-6|Theorem §C6a.3.6]] with $t' = 0$, $W_n$ is the $n$-th term of the time-ordered exponential of [[§C6a.3 The Time-Evolution Operator and Time Ordering#^def-c6a-3-1|Def. §C6a.3.1]], so $W$ is the middle expression of the statement.
>
> **Step 2** (convergence). The ordered region has volume $t^n/n!$ ([[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-4|Theorem §CA.1.4]], 3), and the integrand has norm at most $h^n$:
>
> $$
> \|W_n(t)\| \le \int_0^tdt_1\cdots\int_0^{t_{n-1}}dt_n\,\|\hat H_I(t_1)\|\cdots\|\hat H_I(t_n)\| \le h^n\,\frac{t^n}{n!}, \qquad \sum_{n=0}^\infty\|W_n(t)\| \le \sum_{n=0}^\infty\frac{(ht)^n}{n!} = e^{ht} ,
> $$
>
> uniformly for $t$ in a bounded interval.
>
> **Step 3** ($W$ solves the equation). Now $t$ appears only once in $W_n$, as the upper limit of the outermost integral; the inner integrals depend on $t_1$, not on $t$. Pull out the outermost integral:
>
> $$
> W_n(t) = (-i)\int_0^tdt_1\,\hat H_I(t_1)\underbrace{\Bigl[(-i)^{n-1}\int_0^{t_1}dt_2\int_0^{t_2}dt_3\cdots\int_0^{t_{n-1}}dt_n\,\hat H_I(t_2)\cdots\hat H_I(t_n)\Bigr]}_{W_{n-1}(t_1)} = -i\int_0^tdt_1\,\hat H_I(t_1)\,W_{n-1}(t_1) ,
> $$
>
> the bracket being $W_{n-1}$ with its variables renamed $t_1, \dots, t_{n-1} \to t_2, \dots, t_n$ and upper limit $t_1$, again time ordered among themselves. By the fundamental theorem of calculus ([[§34 Fundamental Theorem of Calculus#^thm-34-4|451 Thm. §34.4]]; the integrand is continuous), differentiation acts only on the upper limit:
>
> $$
> i\,\partial_tW_n(t) = i\cdot(-i)\,\hat H_I(t)\,W_{n-1}(t) = \hat H_I(t)\,W_{n-1}(t) , \qquad n \ge 1 ,
> $$
>
> with $\hat H_I(t)$, the latest operator of all, to the left of everything. Summing over $n$ (term-by-term differentiation is legitimate: the differentiated series is bounded by $\sum_{n\ge1}h(ht)^{n-1}/(n-1)!$ uniformly, [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-3|Theorem §CA.1.3]]),
>
> $$
> i\partial_tW(t) = \hat H_I(t)\sum_{n=1}^\infty W_{n-1}(t) = \hat H_I(t)\,W(t), \qquad W(0) = \mathbf 1 ,
> $$
>
> since every $W_n$ with $n \ge 1$ vanishes at $t = 0$ (an integral over an empty interval). Written out to second order, as on slide 13:
>
> $$
> i\partial_t\Bigl[\mathbf 1 - i\int_0^tdt_1\,\hat H_I(t_1) + (-i)^2\int_0^tdt_1\int_0^{t_1}dt_2\,\hat H_I(t_1)\hat H_I(t_2) + \cdots\Bigr] = \hat H_I(t) - i\,\hat H_I(t)\int_0^tdt_2\,\hat H_I(t_2) + \cdots = \hat H_I(t)\bigl[\mathbf 1 - i\textstyle\int_0^t\hat H_I + \cdots\bigr] .
> $$
>
> **Step 4** (uniqueness: $W = U$). Both $U$ ([[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-2|Theorem §C6a.3.2]]) and $W$ (Step 3) solve $i\partial_tX = \hat H_I(t)X$, $X(0) = \mathbf 1$; $U$ is unitary ([[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-1|Theorem §C6a.3.1]]) and $\hat H_I^\dagger = \hat H_I$. So $W(t) = U(t)$ by [[§C6a.3 The Time-Evolution Operator and Time Ordering#^lem-c6a-3-3|Lemma §C6a.3.3]] ($X = U$, $t_0 = 0$).
>
> **Step 5** (second route: iterate the integral equation). Yu (6.105)–(6.106) and PS (4.20) reach the same series without guessing it. Start from the integral equation ([[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-2|Theorem §C6a.3.2]]) and substitute it for $U(t_1)$ under its own integral:
>
> $$
> \begin{aligned}
> U(t) &= \mathbf 1 - i\int_0^tdt_1\,\hat H_I(t_1)\,U(t_1)\\
> &= \mathbf 1 - i\int_0^tdt_1\,\hat H_I(t_1)\Bigl[\mathbf 1 - i\int_0^{t_1}dt_2\,\hat H_I(t_2)\,U(t_2)\Bigr]\\
> &= \mathbf 1 - i\int_0^tdt_1\,\hat H_I(t_1) + (-i)^2\int_0^tdt_1\int_0^{t_1}dt_2\,\hat H_I(t_1)\hat H_I(t_2)\,U(t_2)\\
> &= W_0 + W_1(t) + W_2(t) + (-i)^3\int_0^tdt_1\int_0^{t_1}dt_2\int_0^{t_2}dt_3\,\hat H_I(t_1)\hat H_I(t_2)\hat H_I(t_3)\,U(t_3) .
> \end{aligned}
> $$
>
> After $n$ substitutions the remainder, with $\|U\| = 1$, is bounded by $h^{n+1}t^{n+1}/(n+1)!$ (Step 2) and tends to zero, leaving $W$. The upper limit $t_1$ of the second integral is forced by the integral equation, which is where the time order comes from (Yu: the limits are "in decreasing order", $t \ge t_1 \ge t_2 \ge \cdots$).
>
> ⚑ By-product: the formula says nothing about convergence in the field theory, where $\hat H_I$ is unbounded and the regularization must be removed; it is used as a power series in $\lambda$, truncated after a few terms → [[§C6a.3 The Time-Evolution Operator and Time Ordering#^rem-c6a-3-3|Remark: Exact, or perturbative?]].
>
> **What the derivation shows.**
> - Differentiating the ordered series acts only on the outermost integral, so $\hat H_I(t)$ comes out on the left automatically; the naive exponential failed exactly there ([[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-5|Theorem §C6a.3.5]]).
> - Uniqueness ([[§C6a.3 The Time-Evolution Operator and Time Ordering#^lem-c6a-3-3|Lemma §C6a.3.3]]) used unitarity and the Hermiticity of $\hat H_I$; the bound of Step 2 is the same as in quantum mechanics ([[§C3.1 The Time-Evolution Operator and the Schrödinger Equation#^der-c3-1-4|QM Derivation §C3.1.4]]).
> - Used next: $U(t, t')$ for any two times ([[§C6a.4 The Time-Evolution Operator Between Two Times#^thm-c6a-4-2|Theorem §C6a.4.2]]).

^der-c6a-3-7

*Uses:* [[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-6|Theorem §C6a.3.6]], [[§C6a.3 The Time-Evolution Operator and Time Ordering#^def-c6a-3-1|Def. §C6a.3.1]], [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-4|Theorem §CA.1.4]], [[§34 Fundamental Theorem of Calculus#^thm-34-4|451 Thm. §34.4]], [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-3|Theorem §CA.1.3]], [[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-2|Theorem §C6a.3.2]], [[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-1|Theorem §C6a.3.1]], [[§C6a.3 The Time-Evolution Operator and Time Ordering#^lem-c6a-3-3|Lemma §C6a.3.3]]

> [!remark] Remark: How to read the time-ordered exponential
> $T\{e^{\cdots}\}$ is not an exponential; it is the series of [[§C6a.3 The Time-Evolution Operator and Time Ordering#^def-c6a-3-1|Def. §C6a.3.1]] with an instruction to be carried out at the very end. That has a useful consequence the lecture used at once: inside $T\{\cdots\}$ operators may be treated as if they commuted, exponents may be added, and the ordering is restored afterwards (the user's notes). The composition law ([[§C6a.4 The Time-Evolution Operator Between Two Times#^thm-c6a-4-1|Theorem §C6a.4.1]], 2) and the master formula ([[§C6a.5 The Interacting Vacuum and the Two-Point Function#^thm-c6a-5-6|Theorem §C6a.5.6]]) are this rule at work. PS: "the time-ordered exponential is just a compact way of writing and remembering the correct expression."
>
> *Source: PHY 513 Lecture 13, transcript (after slide 14) · the user's PHY 513 notes, Ch. 13 §13.3 (paragraph "How to read $T\{e^{\cdots}\}$") · PS §4.2, p. 85*

^rem-c6a-3-2

> [!remark] Remark: Exact, or perturbative?
> The formulas are exact, in the physicist's sense of the word: $\hat\phi_H = U^\dagger\hat\phi_IU$ and $U = T\{e^{-i\int\hat H_I}\}$ involve no approximation. Mathematically this is not the end: whether the series converges, and what kind of operators these are on so large a Hilbert space, are real questions, set aside at this level. For bounded generators the series converges ([[§C3.1 The Time-Evolution Operator and the Schrödinger Equation#^thm-c3-1-4|QM Theorem §C3.1.4]]); (★ beyond the course: for $\phi^4$ theory the perturbation series in $\lambda$ is believed to be asymptotic rather than convergent.) The perturbative step is a separate one: expand $U$ in powers of $\lambda$ and keep the first terms ([[§C6a.4 The Time-Evolution Operator Between Two Times#^ex-c6a-4-1|Example §C6a.4.1]]). For a coupling that is not small one studies the same exact expression by nonperturbative methods, for instance numerically.
>
> *Source: PHY 513 Lecture 13, transcript (last questions) · the user's PHY 513 notes, Ch. 13 §13.3 (paragraph "Exact, or perturbative?")*

^rem-c6a-3-3

> [!remark] Remark: Status
> Slide 14 takes stock. The interacting Heisenberg field is $\hat\phi_H(t, \mathbf x) = U(t)^\dagger\hat\phi_I(t, \mathbf x)U(t)$ with $\hat\phi_I$ the free mode expansion and $U(t) = T\{e^{-i\int_0^t\hat H_I}\}$, $\hat H_I$ a polynomial in $\hat\phi_I$. Everything is written in terms of $\hat a$'s and $\hat a^\dagger$'s, with many integrals and an ordering prescription. The prescription is complete, though not yet in a usable form: logically nothing more is needed. The work left is to organize the combinatorics (Wick's theorem, [[§C6a.7 Wick's Theorem#^thm-c6a-7-2|Theorem §C6a.7.2]]) and to choose what to compute: correlation functions in the true vacuum ([[§C6a.5 The Interacting Vacuum and the Two-Point Function|§C6a.5]]).
>
> *Source: PHY 513 Lecture 13, slide 14, and transcript · the user's PHY 513 notes, Ch. 13 §13.3 (paragraph "Status")*

^rem-c6a-3-4

> [!abstract]- Mathematical background
> Proved in CA and CB; each line says what the physics above relies on.
>
> - [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-5|Theorem §CB.1.5]] — the derivations differentiate and multiply exponentials of $\hat H_0$ and $\hat H$, always without reordering them; parts 3–5 are used: exponents add only for commuting matrices, the adjoint of an exponential, and its derivative on either side.
> - [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-4|Theorem §CA.1.4]] — the integral of the ordered product over the cube is $n!$ times the integral over the ordered region, whose volume is $t^n/n!$: the $\frac{1}{n!}$ of Dyson's formula (Theorem §C6a.3.6) and the bound $h^nt^n/n!$ that makes the series converge (Derivation §C6a.3.7, Step 2).
> - [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-3|Theorem §CA.1.3]] — a series whose differentiated terms converge uniformly may be differentiated term by term: used for the naive exponential (Derivation §C6a.3.5, Step 3) and for the Dyson series (Derivation §C6a.3.7, Step 3).

> [!remark]- Connections
> - Quantum mechanics has the same Dyson series for any time-dependent Hamiltonian, with a convergence proof for bounded ones, and the same series for a perturbation $V_I(t)$ in its interaction picture; the field theory adds a local, explicitly known generator — [[§C3.1 The Time-Evolution Operator and the Schrödinger Equation#^thm-c3-1-4|QM Theorem §C3.1.4]], [[§C9.4 Time-Dependent Perturbation Theory, Sudden and Adiabatic Limits#^thm-c9-4-3|QM Theorem §C9.4.3]], [[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-7|Theorem §C6a.3.7]].
> - The rule "later to the left" is the same for the time-ordered exponential and for the time-ordered product of fields, and for the same reason: operators act on a ket from right to left, so the earliest acts first — [[§C2b.7 Time Ordering, the Feynman Propagator and the iε Prescription#^rem-c2b-7-1|§C2b.7, Remark: Why the later operator stands to the left]], [[§C6a.3 The Time-Evolution Operator and Time Ordering#^def-c6a-3-1|Def. §C6a.3.1]].
> - The $n!$ of the exponential series is the number of orderings of $n$ times; this is a statement about integrals, homed in the methods chapter — [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-4|Theorem §CA.1.4]].
> - The time-ordered exponential is the continuum limit of a product of short-time exponentials, $\prod_k e^{-i\hat H_I(t_k)\Delta t}$ with the latest on the left; the Lie product formula is the same idea for constant generators, and Feynman's path integral is built the same way — [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-8|Theorem §CB.1.8]], QFT C11 (planned).
