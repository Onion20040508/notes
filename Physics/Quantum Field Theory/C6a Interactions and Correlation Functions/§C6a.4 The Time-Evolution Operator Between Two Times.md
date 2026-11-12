---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C6a
section: C6a.4
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C6a.3 The Time-Evolution Operator and Time Ordering]] · ↑ [[· C6a Interactions and Correlation Functions]] · [[§C6a.5 The Interacting Vacuum and the Two-Point Function]] →

*Sources: the user's PHY 513 notes, Ch. 13 §13.3 (Derivation "General reference times: $U(t,t')$", eq. (Utt)), §13.5 (paragraph "Preview: perturbation theory") · PHY 513 Lecture 13 (Larsen, 14 Oct 2026), Part B, slide 14 ("More general time evolution (reference time not $t_0 = 0$)"), and transcript; Part C, slides 21–22 · Peskin & Schroeder, An Introduction to Quantum Field Theory, §4.2, pp. 85–86, eqs. (4.22)–(4.26) · Yu Zhao-Huan, 量子场论讲义, §6.2, eqs. (6.93)–(6.102), (6.119).*

The time-evolution operator of [[§C6a.3 The Time-Evolution Operator and Time Ordering|§C6a.3]] runs from the reference time $0$: $U(t) = e^{i\hat H_0t}e^{-i\hat Ht}$, and Dyson's formula writes it as a time-ordered exponential of $\int_0^t\hat H_I$ ([[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-7|Theorem §C6a.3.7]]). The interacting vacuum and the master formula ([[§C6a.5 The Interacting Vacuum and the Two-Point Function|§C6a.5]]) need the evolution between any two times, from $-T$ to $T$, and the Heisenberg field needs it backwards, from $t$ to $0$. This section defines $U(t, t')$, proves its algebra (composition, unitarity, the equations in both arguments) and Dyson's formula between two times, with the uniqueness argument of [[§C6a.3 The Time-Evolution Operator and Time Ordering#^lem-c6a-3-3|Lemma §C6a.3.3]]; it ends with the Dyson series of $\phi^4$ theory to second order, the form in which perturbation theory uses it. **Setup** ([[§C6a.1 From Free to Interacting Fields#^mod-c6a-1-1|Model §C6a.1.1]]): as in [[§C6a.3 The Time-Evolution Operator and Time Ordering|§C6a.3]], $\hat H_0$ and $\hat H_{\rm int}$ on one Hilbert space; every statement is exact operator algebra, with no state and no vacuum; for a source switched on and off ([[§C6a.0 Setups and Observables#^mod-c6a-0-1|Model §C6a.0.1]]) $U(t, t')$ is the time-ordered exponential, and the statements say which of their parts hold for it.

*Conventions* ([[Larsen PHY 513]]): as in [[§C6a.3 The Time-Evolution Operator and Time Ordering|§C6a.3]]; $T\{\cdots\}$ is time ordering, braces always; a time-ordered exponential from $t'$ to $t$ is written only for $t \ge t'$ (for $t < t'$, [[§C6a.4 The Time-Evolution Operator Between Two Times#^cau-c6a-4-1|Caution: Backwards in time the order reverses]]). The derivations multiply and differentiate exponentials of $\hat H_0$ and $\hat H$ by the rules of [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-5|Theorem §CB.1.5]] recalled in §C6a.3, never reordering them.

## General reference times

> [!definition] Definition §C6a.4.1: Time-Evolution Operator Between Two Times
> For any real $t$, $t'$,
>
> $$
> U(t, t') \equiv e^{i\hat H_0t}\,e^{-i\hat H(t - t')}\,e^{-i\hat H_0t'} ,
> $$
>
> the evolution relative to the free theory from $t'$ to $t$; $U(t, 0) = U(t)$ of [[§C6a.2 The Interaction Picture#^def-c6a-2-2|Def. §C6a.2.2]].
>
> *Model:* [[§C6a.1 From Free to Interacting Fields#^mod-c6a-1-1|Model §C6a.1.1]]; *applies:* as in the opening: exact; time-independent $\hat H$.
>
> *Source: PHY 513 Lecture 13, slide 14 ("More general time evolution (reference time not $t_0 = 0$)") · the user's PHY 513 notes, Ch. 13 §13.3, eq. (Utt) · PS §4.2, eq. (4.25) (with $t_0 = 0$) · Yu §6.2, eq. (6.95) ($U(t, t_0) = V(t)V^\dagger(t_0)$)*

^def-c6a-4-1

> [!theorem] Theorem §C6a.4.1: Properties of the Time-Evolution Operator
> For all real $t$, $t'$, $t_1$, $t_2$, $t_3$:
> 1. $U(t, t) = \mathbf 1$;
> 2. $U(t_1, t_2)\,U(t_2, t_3) = U(t_1, t_3)$ (composition);
> 3. $U(t, t')^\dagger = U(t, t')^{-1} = U(t', t)$ (unitarity; the inverse runs backwards);
> 4. $U(t, 0) = U(t)$ and $U(0, t) = U(t)^\dagger$, so the Heisenberg field is $\hat\phi_H(t, \mathbf x) = U(0, t)\,\hat\phi_I(t, \mathbf x)\,U(t, 0)$;
> 5. $i\partial_tU(t, t') = \hat H_I(t)\,U(t, t')$ and $i\partial_{t'}U(t, t') = -U(t, t')\,\hat H_I(t')$.
>
> *Model:* [[§C6a.1 From Free to Interacting Fields#^mod-c6a-1-1|Model §C6a.1.1]]; *applies:* as in the opening: exact; parts 1–3 and 5 also for $U(t, t') = T\{e^{-i\int_{t'}^t\hat H_I}\}$ of a time-dependent interaction ([[§C6a.0 Setups and Observables#^mod-c6a-0-1|Model §C6a.0.1]]; used in [[§C6a.0 Setups and Observables#^der-c6a-0-4|Derivation §C6a.0.4]], Step 2); part 4 for time-independent $\hat H$.
>
> *Source: PHY 513 Lecture 13, slides 14 ("composition $U(t, t') = U(t, t'')U(t'', t')$"), 21 ("$U^\dagger(t, 0) = U(0, t)$") · the user's PHY 513 notes, Ch. 13 §13.3 (Derivation "General reference times") · PS §4.2, eqs. (4.24), (4.26) · Yu §6.2, eqs. (6.96)–(6.102)*

^thm-c6a-4-1

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
> - Part 4 is slide 21's "$U^\dagger(t, 0) = U(0, t)$", the identity behind the master formula ([[§C6a.5 The Interacting Vacuum and the Two-Point Function#^thm-c6a-5-5|Theorem §C6a.5.5]]).

^der-c6a-4-1

*Uses:* [[§C6a.4 The Time-Evolution Operator Between Two Times#^def-c6a-4-1|Def. §C6a.4.1]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-5|Theorem §CB.1.5]], [[§C6a.2 The Interaction Picture#^thm-c6a-2-4|Theorem §C6a.2.4]], [[§C6a.3 The Time-Evolution Operator and Time Ordering#^der-c6a-3-2|Derivation §C6a.3.2]]

> [!theorem] Theorem §C6a.4.2: Dyson's Formula Between Two Times
> For $t \ge t'$,
>
> $$
> U(t, t') = e^{i\hat H_0t}\,e^{-i\hat H(t - t')}\,e^{-i\hat H_0t'} = T\Bigl\{\exp\Bigl[-i\int_{t'}^tdt''\,\hat H_I(t'')\Bigr]\Bigr\} .
> $$
>
> In particular, inside one time ordering exponents add: $T\{e^{-i\int_{t_2}^{t_1}\hat H_I}\}\,T\{e^{-i\int_{t_3}^{t_2}\hat H_I}\} = T\{e^{-i\int_{t_3}^{t_1}\hat H_I}\}$ for $t_1 \ge t_2 \ge t_3$.
>
> *Model:* [[§C6a.1 From Free to Interacting Fields#^mod-c6a-1-1|Model §C6a.1.1]]; *applies:* as in the opening: exact; the first equality for time-independent $\hat H$; the time-ordered form and the composition inside one ordering for any $\hat H_I(t)$, e.g. [[§C6a.0 Setups and Observables#^mod-c6a-0-1|Model §C6a.0.1]].
>
> *Source: PHY 513 Lecture 13, slide 14 ("Proof: composition … satisfied") · the user's PHY 513 notes, Ch. 13 §13.3 (Derivation "General reference times", "Proof of the second equality (filled in)") · PS §4.2, eqs. (4.23), (4.25) ("From this equation you can show that") · Yu §6.2, eq. (6.119)*

^thm-c6a-4-2

> [!derivation]- Derivation
> **Step 1** (the closed form solves the equation). By [[§C6a.4 The Time-Evolution Operator Between Two Times#^thm-c6a-4-1|Theorem §C6a.4.1]], 5 and 1, $X(t) = U(t, t')$ obeys $i\partial_tX = \hat H_I(t)X$ for $t \ge t'$ with $X(t') = \mathbf 1$.
>
> **Step 2** (the ordered series solves it too). Repeat Steps 1–3 of [[§C6a.3 The Time-Evolution Operator and Time Ordering#^der-c6a-3-7|Derivation §C6a.3.7]] with lower limit $t'$ in place of $0$ in every integral. With
>
> $$
> W_n(t) = (-i)^n\int_{t'}^tdt_1\int_{t'}^{t_1}dt_2\cdots\int_{t'}^{t_{n-1}}dt_n\,\hat H_I(t_1)\cdots\hat H_I(t_n) = -i\int_{t'}^tdt_1\,\hat H_I(t_1)\,W_{n-1}(t_1), \qquad W_0 = \mathbf 1 ,
> $$
>
> the $n$-th term of $T\{e^{-i\int_{t'}^t\hat H_I}\}$ by [[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-6|Theorem §C6a.3.6]],
>
> $$
> i\partial_tW_n(t) = \hat H_I(t)\,W_{n-1}(t) \ (n \ge 1), \qquad i\partial_t\sum_{n\ge0}W_n(t) = \hat H_I(t)\sum_{n\ge0}W_n(t), \qquad W_n(t') = 0 \ (n \ge 1),\quad \sum_nW_n(t') = \mathbf 1 ,
> $$
>
> every integral being over the empty interval $[t', t']$ at $t = t'$.
>
> **Step 3** (uniqueness). By [[§C6a.3 The Time-Evolution Operator and Time Ordering#^lem-c6a-3-3|Lemma §C6a.3.3]] with $t_0 = t'$, $X = U(t, t')$ (unitary, [[§C6a.4 The Time-Evolution Operator Between Two Times#^thm-c6a-4-1|Theorem §C6a.4.1]], 3) and $W = \sum_nW_n$:
>
> $$
> \partial_t\bigl(X^\dagger W\bigr) = \bigl(iX^\dagger\hat H_I(t)\bigr)W + X^\dagger\bigl(-i\hat H_I(t)W\bigr) = 0, \qquad X(t')^\dagger W(t') = \mathbf 1 \quad\Longrightarrow\quad W(t) = X(t) = U(t, t') .
> $$
>
> **Step 4** (exponents add inside $T$). For $t_1 \ge t_2 \ge t_3$, by Steps 1–3 and [[§C6a.4 The Time-Evolution Operator Between Two Times#^thm-c6a-4-1|Theorem §C6a.4.1]], 2:
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
> - The time-ordered form needs $t \ge t'$; for $t < t'$ see [[§C6a.4 The Time-Evolution Operator Between Two Times#^cau-c6a-4-1|Caution: Backwards in time the order reverses]].

^der-c6a-4-2

*Uses:* [[§C6a.4 The Time-Evolution Operator Between Two Times#^thm-c6a-4-1|Theorem §C6a.4.1]], [[§C6a.3 The Time-Evolution Operator and Time Ordering#^der-c6a-3-7|Derivation §C6a.3.7]], [[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-6|Theorem §C6a.3.6]], [[§C6a.3 The Time-Evolution Operator and Time Ordering#^lem-c6a-3-3|Lemma §C6a.3.3]]

> [!caution] Caution: Backwards in time the order reverses
> For $t < t'$, $U(t, t') = U(t', t)^\dagger$ ([[§C6a.4 The Time-Evolution Operator Between Two Times#^thm-c6a-4-1|Theorem §C6a.4.1]], 3), and the adjoint of a time-ordered product is anti-time-ordered (taking $\dagger$ reverses every product): $U(t, t') = \bar T\bigl\{\exp\bigl[+i\int_t^{t'}dt''\,\hat H_I(t'')\bigr]\bigr\}$, the earliest operator on the left ([[§C2b.7 Time Ordering, the Feynman Propagator and the iε Prescription#^def-c2b-7-2|Def. §C2b.7.2]]). Such backward factors appear in the Heisenberg field, $U(0, t)$ for $t > 0$ (part 4); in the master formula they meet their forward partners and cancel ([[§C6a.5 The Interacting Vacuum and the Two-Point Function#^thm-c6a-5-5|Theorem §C6a.5.5]]). The composition law holds for all orderings of $t_1$, $t_2$, $t_3$; only the $T$-form is restricted.
>
> *Source: written here from PS §4.2, eqs. (4.23)–(4.26) ("$t \ge t'$") · Yu §6.2, eqs. (6.99)–(6.100)*

^cau-c6a-4-1

> [!example] Example §C6a.4.1: The Dyson Series of φ⁴ Theory to Second Order
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
> **Step 3** (second order: the eight fields). The four fields in $\hat\phi_I(z_k)^4$ sit at the common time $t_k$ and commute ([[§C6a.2 The Interaction Picture#^thm-c6a-2-2|Theorem §C6a.2.2]], 1), so the bracket of Step 2 is the time-ordered product of the eight fields ([[§C2b.7 Time Ordering, the Feynman Propagator and the iε Prescription#^def-c2b-7-1|Def. §C2b.7.1]]): $T\{\hat H_I(t_1)\hat H_I(t_2)\} = (\frac{\lambda}{4!})^2\int d^3z_1d^3z_2\,T\{\hat\phi_I(z_1)^4\hat\phi_I(z_2)^4\}$. Collect the constants:
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

^ex-c6a-4-1

> [!abstract]- Mathematical background
> Proved in CA and CB; each line says what the physics above relies on.
>
> - [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-5|Theorem §CB.1.5]] — Derivation §C6a.4.1 multiplies and differentiates exponentials of $\hat H_0$ and $\hat H$ without reordering them: two exponentials of the same operator commute and their exponents add (Step 2), the adjoint of an exponential (Step 3), its derivative on either side (Steps 5–6).
> - [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-4|Theorem §CA.1.4]] — the $n!$ that turns the ordered iterated integrals with lower limit $t'$ into the terms of the time-ordered exponential (through Theorem §C6a.3.6, Derivation §C6a.4.2, Step 2), and the bound $h^n(t - t')^n/n!$ of those integrals.
> - [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-3|Theorem §CA.1.3]] — the ordered series with lower limit $t'$ is differentiated term by term, as in Derivation §C6a.3.7, Step 3 (Derivation §C6a.4.2, Step 2).

> [!remark]- Connections
> - Dyson's formula from the reference time $0$ is the case $t' = 0$ of the formula between two times, and one uniqueness argument proves both: two solutions of the same first-order equation with the same initial value agree — [[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-7|Theorem §C6a.3.7]], [[§C6a.3 The Time-Evolution Operator and Time Ordering#^lem-c6a-3-3|Lemma §C6a.3.3]].
> - $U(t, t')$ in the limit $t \to +\infty$, $t' \to -\infty$ is Yu's definition of the $S$-matrix, $S = U(+\infty, -\infty)$ (Yu eqs. (6.122)–(6.125)); the course defines $\hat S$ by the full evolution between in and out states (Lecture 15), and the two agree up to a phase between free states — [[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-1|Theorem §C6b.1.1]].
> - The combinatorial factor $\frac{1}{n!}(\frac{-i\lambda}{4!})^n$ of each order meets the $n!$ ways of permuting identical vertices and the $4!$ ways of attaching lines to each; their cancellation is what the convention $\lambda/4!$ was chosen for — [[§C6a.4 The Time-Evolution Operator Between Two Times#^ex-c6a-4-1|Example §C6a.4.1]], Wick's theorem ([[§C6a.7 Wick's Theorem#^thm-c6a-7-2|Theorem §C6a.7.2]]).
