---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C6a
section: C6a.3
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C6a.2 The Interaction Picture]] · ↑ [[· C6a Interactions and Correlation Functions]] · [[§C6a.4 The Interacting Vacuum and the Two-Point Function]] →

*Sources: the user's PHY 513 notes, Ch. 13 §13.3 · PHY 513 Lecture 13 (Larsen, 14 Oct 2026), Part B, slides 10–14, and transcript · Peskin & Schroeder, An Introduction to Quantum Field Theory, §4.2, pp. 84–86, eqs. (4.17)–(4.26), Fig. 4.1 · Yu Zhao-Huan, 量子场论讲义, §6.2, eqs. (6.93)–(6.121), Fig. 6.2.*

The interacting field is the free field conjugated by one unitary, $\hat\phi_H = U(t)^\dagger\hat\phi_IU(t)$ with $U(t) = e^{i\hat H_0t}e^{-i\hat Ht}$ ([[§C6a.2 The Interaction Picture#^thm-c6a-2-4|Theorem §C6a.2.4]]). This section finds $U$ in terms of things one knows. The key is a first-order differential equation, $i\partial_tU = \hat H_I(t)U$, whose generator is the interaction in the interaction picture ([[§C6a.2 The Interaction Picture#^thm-c6a-2-6|Theorem §C6a.2.6]]). Because $\hat H_I$ is an operator, and operators at different times need not commute, the obvious solution, an exponential of the time integral, is wrong; the correct one orders the operators in time, latest on the left, as in the time-ordered product of [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^def-c2b-6-1|Def. §C2b.6.1]]. The result is Dyson's formula, $U = T\{e^{-i\int\hat H_I}\}$. Quantum mechanics proved the same formula for any time-dependent generator, with its convergence for bounded ones ([[§C3.1 The Time-Evolution Operator and the Schrödinger Equation#^thm-c3-1-4|QM Theorem §C3.1.4]]); the field theory adds the generator $\hat H_I$, a polynomial in free fields, and the evolution operator $U(t, t')$ between any two times, with which the interacting vacuum of [[§C6a.4 The Interacting Vacuum and the Two-Point Function|§C6a.4]] is built. The one piece of pure mathematics, the $n!$ that converts ordered integrals into integrals over a cube, has its home in [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-4|Theorem §CA.1.4]].

*Conventions* ([[Larsen PHY 513]]): as in [[§C6a.2 The Interaction Picture|§C6a.2]]; $T\{\cdots\}$ is time ordering, braces always; the integrals of this section are over time, $\int_0^tdt'$, and $\hat H_I(t')$ is already integrated over space. Derivatives of operator-valued functions of time are taken on the regularized theory, where every operator is a matrix ([[§C6a.1 From Free to Interacting Fields#^rem-c6a-1-4|§C6a.1, ★ Remark: In what sense φ̂⁴(x) is defined]]).

The derivations differentiate and multiply exponentials of $\hat H_0$ and $\hat H$, always without reordering them; the rules for the matrix exponential they rest on, from [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras|§CB.1]] (parts 3–5 are used: exponents add only for commuting matrices, the adjoint of an exponential, and its derivative on either side):

![[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-5]]

## Unitarity and the equation of motion

> [!theorem] Theorem §C6a.3.1: The Time-Evolution Operator Is Unitary
> $U(t)^\dagger = e^{i\hat Ht}e^{-i\hat H_0t} = U(t)^{-1}$ for every real $t$. $U(t)$ is a product of two unitaries but not itself the exponential of $-i\hat H_{\text{int}}t$ ([[§C6a.2 The Interaction Picture#^thm-c6a-2-5|Theorem §C6a.2.5]]).
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

> [!theorem] Theorem §C6a.3.2: The Equation of Motion of the Time-Evolution Operator
> $U(t)$ is the solution of the first-order linear initial-value problem
>
> $$
> i\,\partial_tU(t) = \hat H_I(t)\,U(t), \qquad U(0) = \mathbf 1 ,
> $$
>
> with $\hat H_I(t) = e^{i\hat H_0t}\hat H_{\text{int}}e^{-i\hat H_0t}$ ([[§C6a.2 The Interaction Picture#^def-c6a-2-3|Def. §C6a.2.3]]). Equivalently, it solves the integral equation $U(t) = \mathbf 1 - i\int_0^tdt_1\,\hat H_I(t_1)\,U(t_1)$.
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
> ⚑ By-product: a first-order linear equation with one initial condition has at most one solution; this is what identifies every candidate formula for $U$ below → [[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-6|Theorem §C6a.3.6]], Step 4 of its derivation.
>
> **What the derivation shows.**
> - The generator of $U$ is the interaction alone, in the interaction picture: $\hat H_0$ dropped out because the free evolution has been taken out of $U$ by construction.
> - This is the Schrödinger equation of interaction-picture states ([[§C9.6 The Interaction Picture and the Atom–Field Interaction#^thm-c9-6-1|QM Theorem §C9.6.1]], 1), here as an equation for the operator.

^der-c6a-3-2

*Uses:* [[§C6a.2 The Interaction Picture#^def-c6a-2-2|Def. §C6a.2.2]], [[§C6a.2 The Interaction Picture#^def-c6a-2-3|Def. §C6a.2.3]], [[§C6a.1 From Free to Interacting Fields#^def-c6a-1-1|Def. §C6a.1.1]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-5|Theorem §CB.1.5]], [[§34 Fundamental Theorem of Calculus#^thm-34-1|451 Thm. §34.1]]

> [!remark] Remark: Space integrals and time integrals
> Two questions from the lecture. *Is $\mathcal H_{\text{int}}$ a density?* Yes: every $\hat H$ in this chapter is a Hamiltonian, already integrated over space, $\hat H = \int d^3x\,\hat{\mathcal H}$, with a density at each point of space at a given time. "The Hamiltonian is never integrated over time." The time integrals that appear from here on come from solving the equation of motion of $U$; they are something extra, and together with the space integral of $\hat H_I$ they make the spacetime integrals $\int d^4z$ of perturbation theory ([[§C6a.3 The Time-Evolution Operator and Time Ordering#^ex-c6a-3-1|Example §C6a.3.1]]). *If $\hat H_I$ depends on time, why were there no $\partial_t\hat H$ terms?* Because in $U(t) = e^{i\hat H_0t}e^{-i\hat Ht}$ the Hamiltonians do not depend on time: they are conserved, evaluated once at the reference time. $\hat H_I(t)$ became time dependent only by being conjugated with $e^{i\hat H_0t}$ ([[§C6a.2 The Interaction Picture#^thm-c6a-2-6|Theorem §C6a.2.6]]).
>
> *Source: PHY 513 Lecture 13, transcript (two questions after slide 10) · the user's PHY 513 notes, Ch. 13 §13.3 (paragraphs "Space integrals and time integrals", "Where the time dependence came from")*

^rem-c6a-3-1

## The naive solution and why it fails

> [!theorem] Theorem §C6a.3.3: The Interaction Hamiltonians at Two Times
> For all $t_1$, $t_2$, with $x = (t_1, \mathbf x)$, $y = (t_2, \mathbf y)$,
>
> $$
> [\hat H_I(t_1), \hat H_I(t_2)] = \Bigl(\frac{\lambda}{4!}\Bigr)^2\int d^3x\,d^3y\;4iD(x - y)\sum_{k=0}^3\hat\phi_I(y)^k\,\hat\phi_I(x)^3\,\hat\phi_I(y)^{3-k} ,
> $$
>
> with $D$ the commutator function ([[§C2b.4 Microcausality and the Commutator Function#^def-c2b-4-1|Def. §C2b.4.1]]). The $c$-number coefficient $D(x - y)$ vanishes at spacelike separation, in particular for $t_1 = t_2$, $\mathbf x \ne \mathbf y$, but not inside the light cone. For $t_1 \ne t_2$ the integration region always reaches inside the cone.
>
> *Source: PHY 513 Lecture 13, transcript ("There's no guarantee that they will commute, and in fact, they really won't") · the user's PHY 513 notes, Ch. 13 §13.3 (paragraph "How to read $T\{e^{\cdots}\}$", numerical check) · the commutator written here from [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-2|Theorem §C2b.4.2]]*

^thm-c6a-3-3

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
> **Step 5** (where the coefficient vanishes). $D(\xi) = 0$ for $\xi^2 < 0$ ([[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-5|Theorem §C2b.4.5]]). Inside the cone, with $\tau = \sqrt{\xi^2}$ ([[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-9|Theorem §C2b.4.9]]),
>
> $$
> D(\xi) = \operatorname{sgn}(\xi^0)\,\frac{m\,J_1(m\tau)}{4\pi\tau} \not\equiv 0 .
> $$
>
> For $t_1 \ne t_2$ the set $\{|\mathbf x - \mathbf y| < |t_1 - t_2|\}$, where $\xi^2 > 0$, has positive volume in $(\mathbf x, \mathbf y)$.
>
> **What the derivation shows.**
> - Equal-time Hamiltonians commute; at different times the free fields of the two vertices fail to commute inside the light cone, and nothing makes the operator integral vanish: "in fact, they really won't". In the one-oscillator model of [[§C6a.4 The Interacting Vacuum and the Two-Point Function#^ex-c6a-4-2|Example §C6a.4.2]] (pointer) the naive exponential misses $U(0.7)$ by $0.92$ in the largest matrix element (the user's notes; rerun), while the time-ordered product reproduces it.
> - Used next: part 3 of [[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-4|Theorem §C6a.3.4]], the naive exponential.

^der-c6a-3-3

*Uses:* [[§C6a.2 The Interaction Picture#^thm-c6a-2-3|Theorem §C6a.2.3]], [[§C6a.2 The Interaction Picture#^thm-c6a-2-6|Theorem §C6a.2.6]], [[§C2b.4 Microcausality and the Commutator Function#^def-c2b-4-1|Def. §C2b.4.1]], [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-2|Theorem §C2b.4.2]], [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-5|Theorem §C2b.4.5]], [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-9|Theorem §C2b.4.9]]

> [!theorem] Theorem §C6a.3.4: The Exponential Solves the Equation Only for Commuting Generators
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
> *Source: PHY 513 Lecture 13, slides 11–12 ("Naïve solution (pretend $H_I(t)$ a function, not an operator)", "Correct for any time-dependent function $H_I(t)$. Incorrect for operator $H_I(t)$", "Differentiation w.r.t. $t$ gives $n$ terms with $H_I(t)$ at distinct positions, not always to the left") · the user's PHY 513 notes, Ch. 13 §13.3 (Derivation "The naïve solution, and why it fails") · PS §4.2, p. 84 ("should look something like $U \sim \exp(-iH_It)$") · [[§C3.1 The Time-Evolution Operator and the Schrödinger Equation#^thm-c3-1-4|QM Theorem §C3.1.4]], 2*

^thm-c6a-3-4

> [!derivation]- Derivation
> **Step 1** (the $n$-th term as an $n$-fold integral). The integration variables need different names (slide 12):
>
> $$
> \frac{(-i)^n}{n!}\hat A(t)^n = \frac{(-i)^n}{n!}\int_0^tdt_1\,\hat H_I(t_1)\int_0^tdt_2\,\hat H_I(t_2)\cdots\int_0^tdt_n\,\hat H_I(t_n) .
> $$
>
> **Step 2** (part 1: the product rule without reordering). $\partial_t\hat A(t) = \hat H_I(t)$ (fundamental theorem of calculus, [[§34 Fundamental Theorem of Calculus#^thm-34-1|451 Thm. §34.1]]). The product rule differentiates one factor at a time and leaves it in its place:
>
> $$
> \begin{aligned}
> \partial_t\bigl(\hat A^2\bigr) &= \hat H_I(t)\,\hat A + \hat A\,\hat H_I(t) ,\\
> \partial_t\bigl(\hat A^3\bigr) &= \hat H_I(t)\,\hat A^2 + \hat A\,\hat H_I(t)\,\hat A + \hat A^2\,\hat H_I(t) ,\\
> \partial_t\bigl(\hat A^n\bigr) &= \underbrace{\hat H_I(t)\hat A\cdots\hat A}_{k = 0} + \underbrace{\hat A\,\hat H_I(t)\cdots\hat A}_{k = 1} + \cdots + \underbrace{\hat A\cdots\hat A\,\hat H_I(t)}_{k = n-1} ,
> \end{aligned}
> $$
>
> which is part 1. "Instead of there being $n$ identical expressions, they actually are $n$ different expressions, in that $H$ will be at different positions."
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
> using $i(-i)^n = (-i)^{n-1}$ (since $i\cdot(-i) = 1$) and $n/n! = 1/(n-1)!$; the $n = 0$ term is constant. (Differentiating the series term by term is legitimate: on the regularized theory $\|\hat H_I(t')\| \le h$, the differentiated series is dominated by $\sum h(ht)^{n-1}/(n-1)!$ and converges uniformly, [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-3|Theorem §CA.1.3]].) At $t = 0$, $\hat A = 0$ and $e^0 = \mathbf 1$. By uniqueness (Step 4 of [[§C6a.3 The Time-Evolution Operator and Time Ordering#^der-c6a-3-6|Derivation §C6a.3.6]]) this is $U(t)$.
>
> **Step 4** (part 3). Without commutativity the $n$ terms of part 1 differ, and only the first, $\hat H_I(t)\hat A^{n-1}$, has $\hat H_I(t)$ on the left, where the equation $i\partial_tU = \hat H_I(t)U$ requires it to act. At second order: the term of $e^{-i\hat A}$ is $\frac{(-i)^2}{2}\hat A^2$, and the equation requires $i\partial_t$ of it to be $\hat H_I(t)$ times the first-order term $-i\hat A$:
>
> $$
> i\partial_t\Bigl(\frac{(-i)^2}{2}\hat A^2\Bigr) = \frac{-i}{2}\bigl(\hat H_I(t)\hat A + \hat A\hat H_I(t)\bigr) = \hat H_I(t)\,(-i\hat A) + \frac{i}{2}\,[\hat H_I(t), \hat A(t)] ,
> $$
>
> off by $\frac{i}{2}[\hat H_I(t), \hat A(t)] = \frac{i}{2}\int_0^tdt'\,[\hat H_I(t), \hat H_I(t')]$, which is not zero ([[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-3|Theorem §C6a.3.3]]). For a c-number function $h(t)$ in place of $\hat H_I(t)$ the commutator vanishes: this is why the naive solution is "correct for any time-dependent function."
>
> **What the derivation shows.**
> - The exponential reorders operators implicitly: writing $(\int\hat H_I)^n$ and differentiating as if it were a number moves $\hat H_I(t)$ to the left of operators at earlier times.
> - The repair keeps the series and fixes the order of each term ([[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-6|Theorem §C6a.3.6]]).

^der-c6a-3-4

*Uses:* [[§34 Fundamental Theorem of Calculus#^thm-34-1|451 Thm. §34.1]], [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-3|Theorem §CA.1.3]], [[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-2|Theorem §C6a.3.2]], [[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-3|Theorem §C6a.3.3]]

> [!caution] Caution: A factor on slide 12
> Slide 12's commuting case reads $\to H_I(t)\sum_{n=1}^\infty\frac{1}{(n-1)!}\bigl(\int_0^tdt'H_I(t')\bigr)^{n-1} = H_I(t)U(t)$. The factor $(-i)^{n-1}$ is missing from the sum: $i\partial_t$ of $\frac{(-i)^n}{n!}(\int H_I)^n$ is $\frac{(-i)^{n-1}}{(n-1)!}H_I(t)(\int H_I)^{n-1}$ ([[§C6a.3 The Time-Evolution Operator and Time Ordering#^der-c6a-3-4|Derivation §C6a.3.4]], Step 3). Without it the sum would be $H_I(t)e^{+\int H_I}$, not $H_I(t)U(t)$.
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
> the exponential series with each term time-ordered: $T\{\hat H_I(t_1)\cdots\hat H_I(t_n)\}$ arranges the factors by decreasing time label, the latest on the left and the earliest on the right, as for fields ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^def-c2b-6-1|Def. §C2b.6.1]], applied to operators labelled by a time). The $n = 0$ term is $\mathbf 1$. It is not an exponential: it is the series together with the instruction to time-order each term.
>
> *Source: PHY 513 Lecture 13, slide 13 ("$T$ = time-ordering: order $H_I$'s so smallest $t$ is on the right") · the user's PHY 513 notes, Ch. 13 §13.3, eq. (Dyson) · PS §4.2, eqs. (4.22)–(4.23) ("the time-ordering of the exponential is just defined as the Taylor series with each term time-ordered") · Yu §6.2, eqs. (6.107), (6.119)*

^def-c6a-3-1

> [!theorem] Theorem §C6a.3.5: Ordered Iterated Integrals Are Time-Ordered Cube Integrals
> For $t \ge t'$ and $n \ge 1$,
>
> $$
> \frac{1}{n!}\int_{t'}^tdt_1\cdots\int_{t'}^tdt_n\;T\bigl\{\hat H_I(t_1)\cdots\hat H_I(t_n)\bigr\} = \int_{t'}^tdt_1\,\hat H_I(t_1)\int_{t'}^{t_1}dt_2\,\hat H_I(t_2)\cdots\int_{t'}^{t_{n-1}}dt_n\,\hat H_I(t_n) ,
> $$
>
> where on the right each $t_{k+1}$ runs only up to $t_k$, so the factors already stand in time order.
>
> *Source: PHY 513 Lecture 13, slide 13 ("Example") · the user's PHY 513 notes, Ch. 13 §13.3 (Derivation "The time-ordered exponential (Dyson series)", paragraph "Removing the $n!$") · PS §4.2, eq. (4.21), Fig. 4.1, and the identity before eq. (4.22) · Yu §6.2, eqs. (6.116)–(6.118), Fig. 6.2*

^thm-c6a-3-5

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
> ⚑ By-product: at coincident times the order is irrelevant, both because $\hat H_I(t_1) = \hat H_I(t_2)$ there and because the coincidence set has zero volume; time ordering of $\hat H_I$'s therefore needs no convention at equal times, unlike $\hat\phi$ with $\hat\pi$ ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^cau-c2b-6-1|§C2b.6, Caution: The step function at zero]]).
>
> **What the derivation shows.**
> - The $\frac{1}{n!}$ of the exponential series is exactly what is needed to pick one of the $n!$ time orderings: "those $1/n!$ correspond to all possible orderings … I get effectively one ordering. Which ordering? That one."
> - Used next: Dyson's formula ([[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-6|Theorem §C6a.3.6]]).

^der-c6a-3-5

*Uses:* [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^def-c2b-6-1|Def. §C2b.6.1]], [[§23 Fubini's Theorem#^thm-23-2|452 Thm. §23.2]], [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-4|Theorem §CA.1.4]]

> [!theorem] Theorem §C6a.3.6: Dyson's Formula
> For $t \ge 0$,
>
> $$
> U(t) = T\Bigl\{\exp\Bigl[-i\int_0^tdt'\,\hat H_I(t')\Bigr]\Bigr\} = \mathbf 1 + \sum_{n=1}^\infty(-i)^n\int_0^tdt_1\int_0^{t_1}dt_2\cdots\int_0^{t_{n-1}}dt_n\;\hat H_I(t_1)\hat H_I(t_2)\cdots\hat H_I(t_n) ,
> $$
>
> the **Dyson series**. On the regularized theory, with $\|\hat H_I(t')\| \le h$, the series converges absolutely and uniformly on bounded intervals; in the field theory it is used as a formal power series in $\lambda$.
>
> *Source: PHY 513 Lecture 13, slides 13–14 ("Correct solution") · the user's PHY 513 notes, Ch. 13 §13.3, eq. (Dyson) · PS §4.2, eqs. (4.20), (4.22) · Yu §6.2, eqs. (6.105)–(6.106), (6.119)*

^thm-c6a-3-6

> [!derivation]- Derivation
> **Step 1** (the ordered series). Call $W_0(t) = \mathbf 1$ and $W_n(t) = (-i)^n\int_0^tdt_1\int_0^{t_1}dt_2\cdots\int_0^{t_{n-1}}dt_n\,\hat H_I(t_1)\cdots\hat H_I(t_n)$ for $n \ge 1$, and $W = \sum_nW_n$. By [[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-5|Theorem §C6a.3.5]] with $t' = 0$, $W_n$ is the $n$-th term of the time-ordered exponential of [[§C6a.3 The Time-Evolution Operator and Time Ordering#^def-c6a-3-1|Def. §C6a.3.1]], so $W$ is the middle expression of the statement.
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
> the bracket being $W_{n-1}$ with its variables renamed $t_1, \dots, t_{n-1} \to t_2, \dots, t_n$ and upper limit $t_1$, again time ordered among themselves. By the fundamental theorem of calculus ([[§34 Fundamental Theorem of Calculus#^thm-34-1|451 Thm. §34.1]]; the integrand is continuous), differentiation acts only on the upper limit:
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
> **Step 4** (uniqueness: $W = U$). Both $U$ ([[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-2|Theorem §C6a.3.2]]) and $W$ solve $i\partial_tX = \hat H_I(t)X$, $X(0) = \mathbf 1$. Consider $U(t)^\dagger W(t)$. The adjoint of $i\partial_tU = \hat H_IU$, with $\hat H_I^\dagger = \hat H_I$ (a unitary conjugate of the Hermitian $\hat H_{\text{int}}$), is
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
> - Differentiating the ordered series acts only on the outermost integral, so $\hat H_I(t)$ comes out on the left automatically; the naive exponential failed exactly there ([[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-4|Theorem §C6a.3.4]]).
> - Uniqueness used unitarity and the Hermiticity of $\hat H_I$; the bound of Step 2 is the same as in quantum mechanics ([[§C3.1 The Time-Evolution Operator and the Schrödinger Equation#^der-c3-1-4|QM Derivation §C3.1.4]]).
> - Used next: $U(t, t')$ for any two times ([[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-8|Theorem §C6a.3.8]]).

^der-c6a-3-6

*Uses:* [[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-5|Theorem §C6a.3.5]], [[§C6a.3 The Time-Evolution Operator and Time Ordering#^def-c6a-3-1|Def. §C6a.3.1]], [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-4|Theorem §CA.1.4]], [[§34 Fundamental Theorem of Calculus#^thm-34-1|451 Thm. §34.1]], [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-3|Theorem §CA.1.3]], [[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-2|Theorem §C6a.3.2]], [[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-1|Theorem §C6a.3.1]]

> [!remark] Remark: How to read the time-ordered exponential
> $T\{e^{\cdots}\}$ is not an exponential; it is the series of [[§C6a.3 The Time-Evolution Operator and Time Ordering#^def-c6a-3-1|Def. §C6a.3.1]] with an instruction to be carried out at the very end. That has a useful consequence the lecture used at once: inside $T\{\cdots\}$ operators may be treated as if they commuted, exponents may be added, and the ordering is restored afterwards (the user's notes; in the lecture, one may "commute to your heart's content" as long as one time-orders at the end). The composition law ([[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-7|Theorem §C6a.3.7]], 2) and the master formula ([[§C6a.4 The Interacting Vacuum and the Two-Point Function#^thm-c6a-4-6|Theorem §C6a.4.6]]) are this rule at work. PS: "the time-ordered exponential is just a compact way of writing and remembering the correct expression."
>
> *Source: PHY 513 Lecture 13, transcript (after slide 14) · the user's PHY 513 notes, Ch. 13 §13.3 (paragraph "How to read $T\{e^{\cdots}\}$") · PS §4.2, p. 85*

^rem-c6a-3-2

> [!remark] Remark: Exact, or perturbative?
> Asked at the end of the lecture. The formulas are exact, in the physicist's sense of the word: $\hat\phi_H = U^\dagger\hat\phi_IU$ and $U = T\{e^{-i\int\hat H_I}\}$ involve no approximation. "Mathematicians might not be happy with this": whether the series converges, and what kind of operators these are on so large a Hilbert space, are real questions, but "you have to go a little further into details before you start nitpicking." For bounded generators the series converges ([[§C3.1 The Time-Evolution Operator and the Schrödinger Equation#^thm-c3-1-4|QM Theorem §C3.1.4]]); (★ beyond the course: for $\phi^4$ theory the perturbation series in $\lambda$ is believed to be asymptotic rather than convergent.) The perturbative step is a separate one: expand $U$ in powers of $\lambda$ and keep the first terms ([[§C6a.3 The Time-Evolution Operator and Time Ordering#^ex-c6a-3-1|Example §C6a.3.1]]). For a coupling that is not small one studies the same exact expression by nonperturbative methods, for instance numerically.
>
> *Source: PHY 513 Lecture 13, transcript (last questions) · the user's PHY 513 notes, Ch. 13 §13.3 (paragraph "Exact, or perturbative?")*

^rem-c6a-3-3

## General reference times

> [!definition] Definition §C6a.3.2: Time-Evolution Operator Between Two Times
> For any real $t$, $t'$,
>
> $$
> U(t, t') \equiv e^{i\hat H_0t}\,e^{-i\hat H(t - t')}\,e^{-i\hat H_0t'} ,
> $$
>
> the evolution relative to the free theory from $t'$ to $t$; $U(t, 0) = U(t)$ of [[§C6a.2 The Interaction Picture#^def-c6a-2-2|Def. §C6a.2.2]].
>
> *Source: PHY 513 Lecture 13, slide 14 ("More general time evolution (reference time not $t_0 = 0$)") · the user's PHY 513 notes, Ch. 13 §13.3, eq. (Utt) · PS §4.2, eq. (4.25) (with $t_0 = 0$) · Yu §6.2, eq. (6.95) ($U(t, t_0) = V(t)V^\dagger(t_0)$)*

^def-c6a-3-2

> [!theorem] Theorem §C6a.3.7: Properties of the Time-Evolution Operator
> For all real $t$, $t'$, $t_1$, $t_2$, $t_3$:
> 1. $U(t, t) = \mathbf 1$;
> 2. $U(t_1, t_2)\,U(t_2, t_3) = U(t_1, t_3)$ (composition);
> 3. $U(t, t')^\dagger = U(t, t')^{-1} = U(t', t)$ (unitarity; the inverse runs backwards);
> 4. $U(t, 0) = U(t)$ and $U(0, t) = U(t)^\dagger$, so the Heisenberg field is $\hat\phi_H(t, \mathbf x) = U(0, t)\,\hat\phi_I(t, \mathbf x)\,U(t, 0)$;
> 5. $i\partial_tU(t, t') = \hat H_I(t)\,U(t, t')$ and $i\partial_{t'}U(t, t') = -U(t, t')\,\hat H_I(t')$.
>
> *Source: PHY 513 Lecture 13, slides 14 ("composition $U(t, t') = U(t, t'')U(t'', t')$"), 21 ("$U^\dagger(t, 0) = U(0, t)$") · the user's PHY 513 notes, Ch. 13 §13.3 (Derivation "General reference times") · PS §4.2, eqs. (4.24), (4.26) · Yu §6.2, eqs. (6.96)–(6.102)*

^thm-c6a-3-7

> [!derivation]- Derivation
> **Step 1** (part 1). $U(t, t) = e^{i\hat H_0t}e^{0}e^{-i\hat H_0t} = \mathbf 1$.
>
> **Step 2** (part 2). Multiply the definitions; the middle factors cancel:
>
> $$
> U(t_1, t_2)U(t_2, t_3) = e^{i\hat H_0t_1}e^{-i\hat H(t_1 - t_2)}\underbrace{e^{-i\hat H_0t_2}e^{i\hat H_0t_2}}_{\mathbf 1}e^{-i\hat H(t_2 - t_3)}e^{-i\hat H_0t_3} = e^{i\hat H_0t_1}e^{-i\hat H(t_1 - t_3)}e^{-i\hat H_0t_3} ,
> $$
>
> using $e^{-i\hat H(t_1 - t_2)}e^{-i\hat H(t_2 - t_3)} = e^{-i\hat H(t_1 - t_3)}$ (two exponentials of the same operator commute and their exponents add, [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-5|Theorem §CB.1.5]]). No ordering of the times is assumed.
>
> **Step 3** (part 3). Adjoint, reversing the order: $U(t, t')^\dagger = e^{i\hat H_0t'}e^{i\hat H(t - t')}e^{-i\hat H_0t} = e^{i\hat H_0t'}e^{-i\hat H(t' - t)}e^{-i\hat H_0t} = U(t', t)$. By parts 2 and 1, $U(t', t)U(t, t') = U(t', t') = \mathbf 1$ and $U(t, t')U(t', t) = \mathbf 1$, so it is also the inverse.
>
> **Step 4** (part 4). $U(t, 0) = e^{i\hat H_0t}e^{-i\hat Ht}e^0 = U(t)$; by part 3, $U(0, t) = U(t, 0)^\dagger = U(t)^\dagger$. Substituting into [[§C6a.2 The Interaction Picture#^thm-c6a-2-4|Theorem §C6a.2.4]] gives the field formula.
>
> **Step 5** (part 5, in $t$). $e^{-i\hat H_0t'}$ multiplies from the right and does not depend on $t$, so Steps 1–4 of [[§C6a.3 The Time-Evolution Operator and Time Ordering#^der-c6a-3-2|Derivation §C6a.3.2]] go through unchanged:
>
> $$
> \begin{aligned}
> i\partial_tU(t, t') &= i\bigl(e^{i\hat H_0t}\,i\hat H_0\bigr)e^{-i\hat H(t - t')}e^{-i\hat H_0t'} + i\,e^{i\hat H_0t}\bigl(-i\hat H\,e^{-i\hat H(t - t')}\bigr)e^{-i\hat H_0t'} = e^{i\hat H_0t}\,(\hat H - \hat H_0)\,e^{-i\hat H(t - t')}e^{-i\hat H_0t'}\\
> &= \bigl(e^{i\hat H_0t}\hat H_{\text{int}}e^{-i\hat H_0t}\bigr)\bigl(e^{i\hat H_0t}e^{-i\hat H(t - t')}e^{-i\hat H_0t'}\bigr) = \hat H_I(t)\,U(t, t') ,
> \end{aligned}
> $$
>
> inserting $\mathbf 1 = e^{-i\hat H_0t}e^{i\hat H_0t}$ after $\hat H_{\text{int}}$.
>
> **Step 6** (part 5, in $t'$). Now $e^{i\hat H_0t}$ is the constant factor on the left; differentiate the other two, the Hamiltonians again placed in the middle:
>
> $$
> \partial_{t'}\bigl(e^{-i\hat H(t - t')}e^{-i\hat H_0t'}\bigr) = e^{-i\hat H(t - t')}\,(i\hat H)\,e^{-i\hat H_0t'} + e^{-i\hat H(t - t')}\,(-i\hat H_0)\,e^{-i\hat H_0t'} = e^{-i\hat H(t - t')}\,i\hat H_{\text{int}}\,e^{-i\hat H_0t'} ,
> $$
>
> so, inserting $\mathbf 1 = e^{-i\hat H_0t'}e^{i\hat H_0t'}$ before $\hat H_{\text{int}}$,
>
> $$
> i\partial_{t'}U(t, t') = -\,e^{i\hat H_0t}e^{-i\hat H(t - t')}\hat H_{\text{int}}e^{-i\hat H_0t'} = -\bigl(e^{i\hat H_0t}e^{-i\hat H(t - t')}e^{-i\hat H_0t'}\bigr)\bigl(e^{i\hat H_0t'}\hat H_{\text{int}}e^{-i\hat H_0t'}\bigr) = -U(t, t')\,\hat H_I(t') .
> $$
>
> **What the derivation shows.**
> - Composition and unitarity are immediate from the closed form; they need no ordering of the times. The time-ordered form, which does, is the next theorem.
> - Part 4 is slide 21's "$U^\dagger(t, 0) = U(0, t)$", the identity behind the master formula ([[§C6a.4 The Interacting Vacuum and the Two-Point Function#^thm-c6a-4-5|Theorem §C6a.4.5]]).

^der-c6a-3-7

*Uses:* [[§C6a.3 The Time-Evolution Operator and Time Ordering#^def-c6a-3-2|Def. §C6a.3.2]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-5|Theorem §CB.1.5]], [[§C6a.2 The Interaction Picture#^thm-c6a-2-4|Theorem §C6a.2.4]], [[§C6a.3 The Time-Evolution Operator and Time Ordering#^der-c6a-3-2|Derivation §C6a.3.2]]

> [!theorem] Theorem §C6a.3.8: Dyson's Formula Between Two Times
> For $t \ge t'$,
>
> $$
> U(t, t') = e^{i\hat H_0t}\,e^{-i\hat H(t - t')}\,e^{-i\hat H_0t'} = T\Bigl\{\exp\Bigl[-i\int_{t'}^tdt''\,\hat H_I(t'')\Bigr]\Bigr\} .
> $$
>
> In particular, inside one time ordering exponents add: $T\{e^{-i\int_{t_2}^{t_1}\hat H_I}\}\,T\{e^{-i\int_{t_3}^{t_2}\hat H_I}\} = T\{e^{-i\int_{t_3}^{t_1}\hat H_I}\}$ for $t_1 \ge t_2 \ge t_3$.
>
> *Source: PHY 513 Lecture 13, slide 14 ("Proof: composition … satisfied") · the user's PHY 513 notes, Ch. 13 §13.3 (Derivation "General reference times", "Proof of the second equality (filled in)") · PS §4.2, eqs. (4.23), (4.25) ("From this equation you can show that") · Yu §6.2, eq. (6.119)*

^thm-c6a-3-8

> [!derivation]- Derivation
> **Step 1** (the closed form solves the equation). By [[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-7|Theorem §C6a.3.7]], 5 and 1, $X(t) = U(t, t')$ obeys $i\partial_tX = \hat H_I(t)X$ for $t \ge t'$ with $X(t') = \mathbf 1$.
>
> **Step 2** (the ordered series solves it too). Repeat Steps 1–3 of [[§C6a.3 The Time-Evolution Operator and Time Ordering#^der-c6a-3-6|Derivation §C6a.3.6]] with lower limit $t'$ in place of $0$ in every integral. With
>
> $$
> W_n(t) = (-i)^n\int_{t'}^tdt_1\int_{t'}^{t_1}dt_2\cdots\int_{t'}^{t_{n-1}}dt_n\,\hat H_I(t_1)\cdots\hat H_I(t_n) = -i\int_{t'}^tdt_1\,\hat H_I(t_1)\,W_{n-1}(t_1), \qquad W_0 = \mathbf 1 ,
> $$
>
> the $n$-th term of $T\{e^{-i\int_{t'}^t\hat H_I}\}$ by [[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-5|Theorem §C6a.3.5]],
>
> $$
> i\partial_tW_n(t) = \hat H_I(t)\,W_{n-1}(t) \ (n \ge 1), \qquad i\partial_t\sum_{n\ge0}W_n(t) = \hat H_I(t)\sum_{n\ge0}W_n(t), \qquad W_n(t') = 0 \ (n \ge 1),\quad \sum_nW_n(t') = \mathbf 1 ,
> $$
>
> every integral being over the empty interval $[t', t']$ at $t = t'$.
>
> **Step 3** (uniqueness). As in Step 4 of Derivation §C6a.3.6, with $X = U(t, t')$ and $W = \sum_nW_n$:
>
> $$
> \partial_t\bigl(X^\dagger W\bigr) = \bigl(iX^\dagger\hat H_I(t)\bigr)W + X^\dagger\bigl(-i\hat H_I(t)W\bigr) = 0, \qquad X(t')^\dagger W(t') = \mathbf 1 \quad\Longrightarrow\quad W(t) = X(t) = U(t, t') .
> $$
>
> **Step 4** (exponents add inside $T$). For $t_1 \ge t_2 \ge t_3$, by Steps 1–3 and [[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-7|Theorem §C6a.3.7]], 2:
>
> $$
> T\{e^{-i\int_{t_2}^{t_1}\hat H_I}\}\,T\{e^{-i\int_{t_3}^{t_2}\hat H_I}\} = U(t_1, t_2)\,U(t_2, t_3) = U(t_1, t_3) = T\{e^{-i\int_{t_3}^{t_1}\hat H_I}\} .
> $$
>
> **Step 5** (the same, read in the series, to second order). Every operator of the left factor is later than every operator of the right factor. Multiply the two series:
>
> $$
> \begin{aligned}
> &\Bigl(\mathbf 1 - i\int_{t_2}^{t_1}\!ds\,\hat H_I(s) + (-i)^2\int_{t_2}^{t_1}\!ds\int_{t_2}^{s}\!ds'\,\hat H_I(s)\hat H_I(s') + \cdots\Bigr)\Bigl(\mathbf 1 - i\int_{t_3}^{t_2}\!ds\,\hat H_I(s) + (-i)^2\int_{t_3}^{t_2}\!ds\int_{t_3}^{s}\!ds'\,\hat H_I(s)\hat H_I(s') + \cdots\Bigr)\\
> &\quad= \mathbf 1 - i\Bigl(\int_{t_2}^{t_1} + \int_{t_3}^{t_2}\Bigr)ds\,\hat H_I(s) + (-i)^2\Bigl[\underbrace{\int_{t_2}^{t_1}\!ds\int_{t_2}^{s}\!ds'}_{\text{both in }[t_2, t_1]} + \underbrace{\int_{t_2}^{t_1}\!ds\int_{t_3}^{t_2}\!ds'}_{s \in [t_2, t_1],\ s' \in [t_3, t_2]} + \underbrace{\int_{t_3}^{t_2}\!ds\int_{t_3}^{s}\!ds'}_{\text{both in }[t_3, t_2]}\Bigr]\hat H_I(s)\hat H_I(s') + \cdots .
> \end{aligned}
> $$
>
> The first-order bracket is $\int_{t_3}^{t_1}$. The three second-order regions, $s \ge s'$ in each, are the triangle $\{t_1 \ge s \ge s' \ge t_3\}$ cut along $s = t_2$ and $s' = t_2$, so the bracket is $\int_{t_3}^{t_1}ds\int_{t_3}^{s}ds'\,\hat H_I(s)\hat H_I(s')$, the second-order term of $T\{e^{-i\int_{t_3}^{t_1}\hat H_I}\}$: $\int_{t_3}^{t_2} + \int_{t_2}^{t_1} = \int_{t_3}^{t_1}$ "inside" $T$.
>
> **What the derivation shows.**
> - Slide 14's "composition satisfied" is the key fact but not by itself a proof (the user's notes); the proof is that both sides solve the same first-order equation with the same initial value.
> - The time-ordered form needs $t \ge t'$; for $t < t'$ see [[§C6a.3 The Time-Evolution Operator and Time Ordering#^cau-c6a-3-2|Caution: Backwards in time the order reverses]].

^der-c6a-3-8

*Uses:* [[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-7|Theorem §C6a.3.7]], [[§C6a.3 The Time-Evolution Operator and Time Ordering#^der-c6a-3-6|Derivation §C6a.3.6]], [[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-5|Theorem §C6a.3.5]]

> [!caution] Caution: Backwards in time the order reverses
> For $t < t'$, $U(t, t') = U(t', t)^\dagger$ ([[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-7|Theorem §C6a.3.7]], 3), and the adjoint of a time-ordered product is anti-time-ordered (taking $\dagger$ reverses every product): $U(t, t') = \bar T\bigl\{\exp\bigl[+i\int_t^{t'}dt''\,\hat H_I(t'')\bigr]\bigr\}$, the earliest operator on the left ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^def-c2b-6-2|Def. §C2b.6.2]]). Such backward factors appear in the Heisenberg field, $U(0, t)$ for $t > 0$ (part 4); in the master formula they meet their forward partners and cancel ([[§C6a.4 The Interacting Vacuum and the Two-Point Function#^thm-c6a-4-5|Theorem §C6a.4.5]]). The composition law holds for all orderings of $t_1$, $t_2$, $t_3$; only the $T$-form is restricted.
>
> *Source: written here from PS §4.2, eqs. (4.23)–(4.26) ("$t \ge t'$") · Yu §6.2, eqs. (6.99)–(6.100)*

^cau-c6a-3-2

> [!example] Example §C6a.3.1: The Dyson Series of φ⁴ Theory to Second Order
> With $\hat H_I(t) = \int d^3x\,\frac{\lambda}{4!}\hat\phi_I(t, \mathbf x)^4$ ([[§C6a.2 The Interaction Picture#^thm-c6a-2-6|Theorem §C6a.2.6]]) and $z = (t_z, \mathbf z)$, for $t \ge t'$:
>
> $$
> U(t, t') = \mathbf 1 - \frac{i\lambda}{4!}\int_{t'}^{t}\!d^4z\;\hat\phi_I(z)^4 + \frac{1}{2!}\Bigl(\frac{-i\lambda}{4!}\Bigr)^2\int_{t'}^{t}\!d^4z_1\int_{t'}^{t}\!d^4z_2\;T\bigl\{\hat\phi_I(z_1)^4\,\hat\phi_I(z_2)^4\bigr\} + O(\lambda^3) ,
> $$
>
> where $\int_{t'}^td^4z$ means $\int_{t'}^tdt_z\int d^3z$.
>
> **Step 1** (first order). The $n = 1$ term of [[§C6a.3 The Time-Evolution Operator and Time Ordering#^def-c6a-3-1|Def. §C6a.3.1]] (one factor, nothing to order), with $\hat H_I$ inserted:
>
> $$
> -i\int_{t'}^tdt_1\,\hat H_I(t_1) = -i\int_{t'}^tdt_1\int d^3z\,\frac{\lambda}{4!}\,\hat\phi_I(t_1, \mathbf z)^4 = -\frac{i\lambda}{4!}\int_{t'}^{t}\!d^4z\;\hat\phi_I(z)^4 , \qquad z = (t_1, \mathbf z) .
> $$
>
> **Step 2** (second order: the two Hamiltonians). The $n = 2$ term is $\frac{(-i)^2}{2!}\int_{t'}^tdt_1\int_{t'}^tdt_2\,T\{\hat H_I(t_1)\hat H_I(t_2)\}$, and
>
> $$
> T\{\hat H_I(t_1)\hat H_I(t_2)\} = \theta(t_1 - t_2)\,\hat H_I(t_1)\hat H_I(t_2) + \theta(t_2 - t_1)\,\hat H_I(t_2)\hat H_I(t_1) = \Bigl(\frac{\lambda}{4!}\Bigr)^2\int d^3z_1\,d^3z_2\,\Bigl[\theta(t_1 - t_2)\,\hat\phi_I(z_1)^4\hat\phi_I(z_2)^4 + \theta(t_2 - t_1)\,\hat\phi_I(z_2)^4\hat\phi_I(z_1)^4\Bigr] ,
> $$
>
> with $z_k = (t_k, \mathbf z_k)$.
>
> **Step 3** (second order: the eight fields). The four fields in $\hat\phi_I(z_k)^4$ sit at the common time $t_k$ and commute ([[§C6a.2 The Interaction Picture#^thm-c6a-2-2|Theorem §C6a.2.2]], 1), so the bracket of Step 2 is the time-ordered product of the eight fields ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^def-c2b-6-1|Def. §C2b.6.1]]): $T\{\hat H_I(t_1)\hat H_I(t_2)\} = (\frac{\lambda}{4!})^2\int d^3z_1d^3z_2\,T\{\hat\phi_I(z_1)^4\hat\phi_I(z_2)^4\}$. Collect the constants:
>
> $$
> \frac{(-i)^2}{2!}\Bigl(\frac{\lambda}{4!}\Bigr)^2 = \frac{1}{2!}\Bigl(\frac{-i\lambda}{4!}\Bigr)^2, \qquad \int_{t'}^tdt_1\int d^3z_1\int_{t'}^tdt_2\int d^3z_2 = \int_{t'}^t\!d^4z_1\int_{t'}^t\!d^4z_2 .
> $$
>
> **Step 4** (order $n$). The same steps with $n$ factors:
>
> $$
> \frac{(-i)^n}{n!}\int_{t'}^t\!dt_1\cdots dt_n\,T\{\hat H_I(t_1)\cdots\hat H_I(t_n)\} = \frac{1}{n!}\Bigl(\frac{-i\lambda}{4!}\Bigr)^n\int_{t'}^t\!d^4z_1\cdots d^4z_n\;T\{\hat\phi_I(z_1)^4\cdots\hat\phi_I(z_n)^4\} :
> $$
>
> a power $\lambda^n$, one spacetime integral per interaction point, and a free time-ordered product.
>
> *Source: the user's PHY 513 notes, Ch. 13 §13.5 (paragraph "Preview: perturbation theory") · PHY 513 Lecture 13, slide 22 · PS §4.2, eq. (4.22)*

^ex-c6a-3-1

> [!remark] Remark: Status
> Slide 14 takes stock. The interacting Heisenberg field is $\hat\phi_H(t, \mathbf x) = U(t)^\dagger\hat\phi_I(t, \mathbf x)U(t)$ with $\hat\phi_I$ the free mode expansion and $U(t) = T\{e^{-i\int_0^t\hat H_I}\}$, $\hat H_I$ a polynomial in $\hat\phi_I$. Everything is written in terms of $\hat a$'s and $\hat a^\dagger$'s, with many integrals and an ordering prescription: "the prescription is complete. It's not being digested very well … Logically, we're kind of done." The work left is to organize the combinatorics (Wick's theorem, [[§C6a.6 Wick's Theorem#^thm-c6a-6-2|Theorem §C6a.6.2]]) and to choose what to compute: correlation functions in the true vacuum ([[§C6a.4 The Interacting Vacuum and the Two-Point Function|§C6a.4]]).
>
> *Source: PHY 513 Lecture 13, slide 14, and transcript · the user's PHY 513 notes, Ch. 13 §13.3 (paragraph "Status")*

^rem-c6a-3-4

> [!remark]- Connections
> - Quantum mechanics has the same Dyson series for any time-dependent Hamiltonian, with a convergence proof for bounded ones, and the same series for a perturbation $V_I(t)$ in its interaction picture; the field theory adds a local, explicitly known generator — [[§C3.1 The Time-Evolution Operator and the Schrödinger Equation#^thm-c3-1-4|QM Theorem §C3.1.4]], [[§C9.4 Time-Dependent Perturbation Theory, Sudden and Adiabatic Limits#^thm-c9-4-2|QM Theorem §C9.4.2]], [[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-6|Theorem §C6a.3.6]].
> - The rule "later to the left" is the same for the time-ordered exponential and for the time-ordered product of fields, and for the same reason: operators act on a ket from right to left, so the earliest acts first — [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^rem-c2b-6-1|§C2b.6, Remark: Why the later operator stands to the left]], [[§C6a.3 The Time-Evolution Operator and Time Ordering#^def-c6a-3-1|Def. §C6a.3.1]].
> - The $n!$ of the exponential series is the number of orderings of $n$ times; this is a statement about integrals, homed in the methods chapter — [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-4|Theorem §CA.1.4]].
> - The time-ordered exponential is the continuum limit of a product of short-time exponentials, $\prod_k e^{-i\hat H_I(t_k)\Delta t}$ with the latest on the left; the Lie product formula is the same idea for constant generators, and Feynman's path integral is built the same way — [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-8|Theorem §CB.1.8]], QFT C11 (planned).
> - $U(t, t')$ in the limit $t \to +\infty$, $t' \to -\infty$ is Yu's definition of the $S$-matrix, $S = U(+\infty, -\infty)$ (Yu eqs. (6.122)–(6.125)); the course defines $\hat S$ by the full evolution between in and out states (Lecture 15), and the two agree up to a phase between free states — [[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-1|Theorem §C6b.1.1]].
> - The combinatorial factor $\frac{1}{n!}(\frac{-i\lambda}{4!})^n$ of each order meets the $n!$ ways of permuting identical vertices and the $4!$ ways of attaching lines to each; their cancellation is what the convention $\lambda/4!$ was chosen for — [[§C6a.3 The Time-Evolution Operator and Time Ordering#^ex-c6a-3-1|Example §C6a.3.1]], Wick's theorem ([[§C6a.6 Wick's Theorem#^thm-c6a-6-2|Theorem §C6a.6.2]]).
