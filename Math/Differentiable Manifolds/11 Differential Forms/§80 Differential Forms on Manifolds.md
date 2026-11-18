---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 11
section: 80
tags: [differentiable-manifolds, math591]
---
← [[§79 Pullbacks of Linear Forms]] · ↑ [[· 11 Differential Forms]] · [[§81 The Exterior Derivative]] →

*Stage: forms — A $k$-form on a manifold is a linear $k$-form on each tangent space; smoothness through chart components; the bundle $\Lambda^k T^{\ast}M$; pullbacks by smooth maps, computed by substitution.*

*(Lecture 31.)* The linear algebra of [[§75 Multilinear Algebra|§75]]–[[§79 Pullbacks of Linear Forms|§79]] is now put to use. The vector space $V$ was always meant to be a tangent space, $V = T_pM$, and all of that linear algebra is done at each point of a manifold. Throughout, $M$ is a smooth manifold of dimension $m$.

> [!definition] Definition §80.1: $k$-Form on a Manifold
> Let $M$ be a smooth manifold. A **$k$-form** $\omega$ on $M$ is an assignment
>
> $$
> M \ni p \longmapsto \omega_p \in \Lambda^k T_p^{\ast}M ,
> $$
>
> of a linear $k$-form on $T_pM$ (Definition [[§75 Multilinear Algebra#^def-75-2|§75.2]], with $V = T_pM$ and $V^{\ast} = T_p^{\ast}M$) to every point of $M$.
>
> *Lee: Ch. 14, Differential Forms on Manifolds*

^def-80-1

> [!remark]- Connections
> - Degree one, the one-forms: [[§53 One-Forms#^def-53-1|Def. §53.1]]; degree two in $\mathbb{R}^3$, the integrand of a surface integral: [[§74 The Integrand Is a Two-Form#^def-74-1|Def. §74.1]].
> - Forms on open subsets of $\mathbb{R}^n$ in MATH 452: [[§36 Introduction to Differential Forms|452 §36]], [[§37 The Algebra of Differential Forms#^def-37-1|452 Def. §37.1]].

> [!definition] Definition §80.2: Degree of a Form
> The **degree** of a $k$-form $\omega$ on $M$ (Definition [[§80 Differential Forms on Manifolds#^def-80-1|§80.1]]) is the number $k$. It is written $|\omega| = k$.

^def-80-2

No smoothness is required yet; smooth forms come next. The case $k = 1$ was seen in September: an assignment of a covector to each point is a section of $T^{\ast}M$, and a smooth one is a one-form (Definition [[§53 One-Forms#^def-53-1|§53.1]]); this is its version in arbitrary degree. For $k = 0$, $\Lambda^0 T_p^{\ast}M = \mathbb{R}$, and a $0$-form assigns a number to each point: it is a function on $M$. The notation $|\omega|$ for the degree is not Lee's, but it is used in other books. Notation, normalizations and sign conventions vary a lot from book to book in this subject (and more so in MATH 635), down to which index of a matrix labels the rows; so the conventions of the book at hand have to be checked before its formulas are used.

*Coordinates.* Let $(U, \varphi = (x^1, \ldots, x^m))$ be a smooth chart and $q \in U$. The coordinate vectors $\partial/\partial x^1|_q, \ldots, \partial/\partial x^m|_q$ form a basis of $T_qM$, with dual basis $dx^1|_q, \ldots, dx^m|_q$ of $T_q^{\ast}M$ (Lemma [[§33 Covectors in Coordinates#^lem-33-1|§33.1]]). By Propositions [[§75 Multilinear Algebra#^prop-75-6|§75.6]] and [[§78 Properties of the Wedge Product#^prop-78-4|§78.4]](4), for $A = \{a_1 < \cdots < a_k\} \subseteq \{1, \ldots, m\}$ the forms

$$
dx^A\big|_q = dx^{a_1}\big|_q \wedge \cdots \wedge dx^{a_k}\big|_q ,
$$

the elementary $k$-forms $\varepsilon^A$ of Definition [[§75 Multilinear Algebra#^def-75-3|§75.3]] for this dual basis, form a basis of $\Lambda^k T_q^{\ast}M$. The assignment $q \mapsto dx^A|_q$ is a $k$-form on $U$, written $dx^A$.

> [!definition] Definition §80.3: Components of a $k$-Form in a Chart
> Let $\omega$ be a $k$-form on $M$ and $(U, \varphi = (x^1, \ldots, x^m))$ a smooth chart. For each $q \in U$ write
>
> $$
> \omega_q = \sum_A f_A(q)\, dx^A\big|_q , \qquad f_A(q) = \omega_q\Big( \frac{\partial}{\partial x^{a_1}}\Big|_q, \ldots, \frac{\partial}{\partial x^{a_k}}\Big|_q \Big) ,
> $$
>
> the sum over all $A = \{a_1 < \cdots < a_k\} \subseteq \{1, \ldots, m\}$ (the formula for $f_A(q)$ is Proposition [[§75 Multilinear Algebra#^prop-75-6|§75.6]]). This defines, for every such $A$, a **component function** $f_A : U \to \mathbb{R}$ of $\omega$ in the chart.
>
> *Lee: Ch. 14, Differential Forms on Manifolds*

^def-80-3

> [!definition] Definition §80.4: Smooth $k$-Form
> A $k$-form $\omega$ on $M$ is **smooth** ($C^\infty$) if for every $p \in M$ there is a smooth chart $(U, \varphi = (x^1, \ldots, x^m))$ with $p \in U$ such that every component function of $\omega$ in it is smooth: $f_A \in C^\infty(U)$ for every $A$.
>
> *Lee: Ch. 14, Differential Forms on Manifolds*

^def-80-4

This is the criterion for vector fields (Proposition [[§56 Vector Fields#^prop-56-1|§56.1]]) and for one-forms (Proposition [[§53 One-Forms#^prop-53-1|§53.1]](3)), and for $k = 1$ it is that criterion, since $dx^{\{j\}} = dx^j$ and $f_{\{j\}} = \theta_j$. The definition asks for one good chart at each point. By the next two lemmas, the components are then smooth in every chart, as for vector fields.

> [!theorem] Lemma §80.1: Change of Frame
> Let $(U, \varphi = (x^1, \ldots, x^m))$ and $(V, \psi = (y^1, \ldots, y^m))$ be smooth charts of $M$. For every $k$-element subset $B = \{b_1 < \cdots < b_k\}$ of $\{1, \ldots, m\}$, at every $q \in U \cap V$,
>
> $$
> dy^B\big|_q = \sum_A \det\Big( \frac{\partial y^{b_i}}{\partial x^{a_j}}(q) \Big)_{i, j = 1, \ldots, k}\; dx^A\big|_q ,
> $$
>
> the sum over all $k$-element subsets $A = \{a_1 < \cdots < a_k\}$ of $\{1, \ldots, m\}$, with row index $i$ and column index $j$. The coefficients are smooth functions on $U \cap V$.
>
> *Lee: Ch. 14, Differential Forms on Manifolds*

^lem-80-1

> [!proof]+ Proof
> *(Lecture 31 wrote the formula, from the case $k = 1$, $dy^j = \sum_i \frac{\partial y^j}{\partial x^i}\, dx^i$ (Lemma [[§33 Covectors in Coordinates#^lem-33-1|§33.1]]), and from the linear algebra at the beginning of the lecture, leaving its verification as a check; verified here.)* Fix $q \in U \cap V$ and apply Proposition [[§79 Pullbacks of Linear Forms#^prop-79-2|§79.2]] to the identity map $\mathrm{id} : T_qM \to T_qM$, with the basis $e_i = \partial/\partial x^i|_q$ (dual basis $\varepsilon^i = dx^i|_q$) on the domain and the basis $f_j = \partial/\partial y^j|_q$ (dual basis $\phi^j = dy^j|_q$, Lemma [[§33 Covectors in Coordinates#^lem-33-1|§33.1]]) on the target. Since $\mathrm{id}^{\ast}$ is the identity of $\Lambda^k T_q^{\ast}M$, the proposition expands $dy^B|_q = \mathrm{id}^{\ast}(dy^B|_q)$ in the basis $dx^A|_q$, with coefficients
>
> $$
> \det\Big( dy^{b_i}\big|_q \Big( \frac{\partial}{\partial x^{a_j}}\Big|_q \Big) \Big)_{i, j} = \det\Big( \frac{\partial y^{b_i}}{\partial x^{a_j}}(q) \Big)_{i, j}
> $$
>
> by Proposition [[§32 The Cotangent Space#^prop-32-2|§32.2]]. For $k = 1$ this is the formula for $dy^j$ again, which is the check made in the lecture.
>
> *Smoothness.* The chart $\varphi$ restricts to a smooth chart on the open set $U \cap V$ (Lemma [[§17 Differentiable Structures#^lem-17-7|§17.7]](1)), and $y^b$ is smooth there, so each $\partial y^b/\partial x^a$ is smooth on $U \cap V$ (Lemma [[§29 Coordinate Derivations and the Basis Theorem#^lem-29-3|§29.3]]). A $k \times k$ determinant is a polynomial in its entries, so the coefficients are smooth.

^pf-80-1

*Uses:* [[§33 Covectors in Coordinates#^lem-33-1|§33.1]], [[§79 Pullbacks of Linear Forms#^prop-79-2|§79.2]], [[§32 The Cotangent Space#^prop-32-2|§32.2]], [[§17 Differentiable Structures#^lem-17-7|§17.7]], [[§29 Coordinate Derivations and the Basis Theorem#^lem-29-3|§29.3]]

**Transcription note (Lecture 31).** The board wrote $\det\big(\partial y^{b_i}/\partial x^a\big)$; the column index is $a_j$, as in the lemma. The formula checked out.

So the change of basis functions, from the frame $\{dx^A\}_A$ to the frame $\{dy^B\}_B$ (such families of sections are called *frames*), are smooth functions on $U \cap V$.

> [!theorem] Lemma §80.2: Smoothness in Every Chart
> A $k$-form $\omega$ on $M$ is smooth (Definition [[§80 Differential Forms on Manifolds#^def-80-4|§80.4]]) if and only if for every smooth chart $(V, \psi = (y^1, \ldots, y^m))$ the components $g_B$ of $\omega$ with respect to $\{dy^B\}_B$, $\omega_q = \sum_B g_B(q)\, dy^B|_q$, are smooth functions on $V$.
>
> *Lee: Ch. 14, Differential Forms on Manifolds*

^lem-80-2

> [!proof]+ Proof
> *(Lecture 31 gave the reason, the change of frame; the details are filled in.)* If the components are smooth in every chart, then in particular in some chart at each point, so $\omega$ is smooth. Conversely, let $\omega$ be smooth and $(V, \psi)$ a chart. Smoothness is local, so it suffices to show that each $g_B$ is smooth near each $q_0 \in V$. By Definition [[§80 Differential Forms on Manifolds#^def-80-4|§80.4]] there is a chart $(U, \varphi = (x^1, \ldots, x^m))$ at $q_0$ in which the components $f_A$ of $\omega$ are smooth. On $U \cap V$, Lemma [[§80 Differential Forms on Manifolds#^lem-80-1|§80.1]] with the two charts exchanged gives $dx^A|_q = \sum_B \det\big(\partial x^{a_i}/\partial y^{b_j}(q)\big)\, dy^B|_q$, so
>
> $$
> \omega_q = \sum_A f_A(q)\, dx^A\big|_q = \sum_B \Big( \sum_A f_A(q)\, \det\Big( \frac{\partial x^{a_i}}{\partial y^{b_j}}(q) \Big)_{i, j} \Big)\, dy^B\big|_q \qquad (q \in U \cap V) .
> $$
>
> The $dy^B|_q$ form a basis of $\Lambda^k T_q^{\ast}M$, so the coefficients are unique, and $g_B = \sum_A f_A \det\big(\partial x^{a_i}/\partial y^{b_j}\big)$ on $U \cap V$: a sum of products of smooth functions. So $g_B$ is smooth on the neighbourhood $U \cap V$ of $q_0$.

^pf-80-2

*Uses:* [[§80 Differential Forms on Manifolds#^def-80-4|Def. §80.4]], [[§80 Differential Forms on Manifolds#^lem-80-1|§80.1]]

*The bundle of $k$-forms.* Vector fields and one-forms were defined as sections of bundles. So are $k$-forms; the definition through components above only avoids constructing the bundle first. There is a general principle with vector bundles: anything that can be done naturally on a vector space can be done naturally on bundles.

> [!definition] Definition §80.5: The Bundle of $k$-Forms
> Let $M$ be a smooth manifold and $k \ge 0$. As a set, copying the cotangent bundle (Definition [[§52 The Cotangent Bundle#^def-52-1|§52.1]]),
>
> $$
> \Lambda^k T^{\ast}M = \bigsqcup_{p \in M} \Lambda^k T_p^{\ast}M , \qquad \pi : \Lambda^k T^{\ast}M \to M, \quad \pi(p, \xi) = p .
> $$
>
> A $k$-form $\omega$ on $M$ (Definition [[§80 Differential Forms on Manifolds#^def-80-1|§80.1]]) is the same thing as a map $M \to \Lambda^k T^{\ast}M$, $p \mapsto (p, \omega_p)$, whose composite with $\pi$ is the identity of $M$. For each chart $(U, \varphi = (x^1, \ldots, x^m))$ the forms $dx^A$ are such maps over $U$, $dx^A : U \to \pi^{-1}(U)$.
>
> *Lee: Ch. 14, Differential Forms on Manifolds*

^def-80-5

> [!theorem] Proposition §80.3: The Smooth Structure of $\Lambda^k T^{\ast}M$
> Let $N = \binom{m}{k}$. For each smooth chart $(U, \varphi = (x^1, \ldots, x^m))$ of $M$ let
>
> $$
> \hat\varphi : \pi^{-1}(U) \longrightarrow \varphi(U) \times \mathbb{R}^N, \qquad \Big(q, \sum_A \xi_A\, dx^A\big|_q\Big) \longmapsto \big(\varphi(q), (\xi_A)_A\big) .
> $$
>
> There is a unique topology on $\Lambda^k T^{\ast}M$ for which every $\pi^{-1}(U)$ is open and every $\hat\varphi$ is a homeomorphism onto its image; with it and the charts $\hat\varphi$, $\Lambda^k T^{\ast}M$ (Definition [[§80 Differential Forms on Manifolds#^def-80-5|§80.5]]) is a smooth manifold of dimension $m + N$, and $\pi$ is a fibration with fibre $\mathbb{R}^N$ (Definition [[§45 Fibrations#^def-45-1|§45.1]]) whose local trivializations are linear isomorphisms on each fibre: a vector bundle of rank $N$, like $TM$ and $T^{\ast}M$. The forms $dx^A$ are smooth sections over $U$, and a $k$-form $\omega$ is smooth (Definition [[§80 Differential Forms on Manifolds#^def-80-4|§80.4]]) if and only if $\omega : M \to \Lambda^k T^{\ast}M$, $p \mapsto (p, \omega_p)$, is a smooth section.
>
> *Lee: Exercise 14.14; Lemma 10.6*

^prop-80-3

> [!proof]+ Proof
> *(Stated in Lecture 31 without proof, the verification being long but routine; filled in.)* Each $\hat\varphi$ is a bijection onto $\varphi(U) \times \mathbb{R}^N$, since the $dx^A|_q$ form a basis of each fibre $\Lambda^k T_q^{\ast}M$, $q \in U$. Apply Lemma [[§51 The Tangent Bundle#^lem-51-2|§51.2]] with $X = \Lambda^k T^{\ast}M$, $n = m + N$ and the maps $\hat\varphi$. Conditions (1), (2), (4) and (5) are checked word for word as in the proof of Proposition [[§52 The Cotangent Bundle#^prop-52-2|§52.2]], with $T^{\ast}U$ replaced by $\pi^{-1}(U)$: $\hat\varphi(\pi^{-1}(U) \cap \pi^{-1}(V)) = \varphi(U \cap V) \times \mathbb{R}^N$ is open, countably many chart domains cover $M$, and points over distinct points of $M$ are separated by charts over disjoint open sets. For (3), let $(V, \psi = (y^j))$ be a second chart, $\tau = \psi \circ \varphi^{-1}$, and $(r, \xi) \in \varphi(U \cap V) \times \mathbb{R}^N$ with $q = \varphi^{-1}(r)$. By Lemma [[§80 Differential Forms on Manifolds#^lem-80-1|§80.1]] with the charts exchanged, as in the proof of Lemma [[§80 Differential Forms on Manifolds#^lem-80-2|§80.2]],
>
> $$
> \hat\psi \circ \hat\varphi^{-1}(r, \xi) = \Big( \tau(r),\ \Big( \sum_A \xi_A \det\Big( \frac{\partial x^{a_i}}{\partial y^{b_j}}(q) \Big)_{i, j} \Big)_B \Big) ,
> $$
>
> smooth in $(r, \xi)$, because $q \mapsto \partial x^a/\partial y^b(q)$ is smooth on $U \cap V$ and $\varphi^{-1}$ is smooth. So the lemma gives the topology and the smooth structure. As in Corollary [[§52 The Cotangent Bundle#^cor-52-3|§52.3]], $\varphi \circ \pi \circ \hat\varphi^{-1}(r, \xi) = r$, so $\pi$ is smooth, and $\Psi = (\varphi^{-1} \times \mathrm{id}) \circ \hat\varphi : \pi^{-1}(U) \to U \times \mathbb{R}^N$ is a local trivialization which is linear on each fibre. Finally, the coordinate representation of a $k$-form $\omega$ in the charts $\varphi$ and $\hat\varphi$ is $r \mapsto \big(r, (f_A(\varphi^{-1}(r)))_A\big)$, with $f_A$ its components (Definition [[§80 Differential Forms on Manifolds#^def-80-3|§80.3]]); it is smooth exactly when the $f_A$ are smooth on $U$. For $\omega = dx^A$ the components are constant, $0$ or $1$. Since smoothness of a map is local, $\omega$ is a smooth section exactly when its components are smooth in a chart at each point.

^pf-80-3

*Uses:* [[§51 The Tangent Bundle#^lem-51-2|§51.2]], [[§52 The Cotangent Bundle#^prop-52-2|§52.2]], [[§80 Differential Forms on Manifolds#^lem-80-1|§80.1]], [[§80 Differential Forms on Manifolds#^lem-80-2|§80.2]], [[§52 The Cotangent Bundle#^cor-52-3|§52.3]], [[§80 Differential Forms on Manifolds#^def-80-3|Def. §80.3]]

In this terminology a smooth $k$-form is a smooth section of that bundle. The practical way of knowing when a section is smooth is Definition [[§80 Differential Forms on Manifolds#^def-80-4|§80.4]]: its coefficients with respect to the frames $\{dx^A\}$ are smooth. The transition functions of the bundle are the change of frame functions of Lemma [[§80 Differential Forms on Manifolds#^lem-80-1|§80.1]], and their smoothness is what gives the smooth structure in the first place.

> [!definition] Definition §80.6: The Space $\Omega^k(M)$
> $\Omega^k(M)$ is the set of all smooth $k$-forms on $M$. In particular
>
> $$
> \Omega^0(M) = C^\infty(M), \qquad \Omega^1(M) = \{\text{one-forms on } M\} .
> $$
>
> *Lee: Ch. 14, Differential Forms on Manifolds*

^def-80-6

The case $k = 0$ has to be included: by definition $\Lambda^0$ is $\mathbb{R}$, so a $0$-form associates a real number to every point, that is, it is a function; it is smooth exactly when the function is (for $k = 0$ the only component is $f_\varnothing = f$, since $dx^\varnothing = 1$). $\Omega^1(M)$ is the space $C^\infty(M, T^{\ast}M)$ of Definition [[§53 One-Forms#^def-53-2|§53.2]]. By Corollary [[§75 Multilinear Algebra#^cor-75-3|§75.3]], $\Omega^k(M) = \{0\}$ for $k > m$.

*Not from lecture: the operations on forms.* The example at the end of the lecture adds forms, multiplies them by functions and wedges them; these are pointwise operations, recorded here.

> [!definition] Definition §80.7: Sums and Function Multiples of Forms
> *(Not from lecture; filled in.)* Let $\omega, \omega'$ be $k$-forms on $M$, $f : M \to \mathbb{R}$ a function and $c \in \mathbb{R}$. The $k$-forms $\omega + c\,\omega'$ and $f\omega$ are defined at every $p \in M$ with the operations of $\Lambda^k T_p^{\ast}M$ (Definition [[§75 Multilinear Algebra#^def-75-2|§75.2]]):
>
> $$
> (\omega + c\,\omega')_p = \omega_p + c\,\omega'_p, \qquad (f\omega)_p = f(p)\,\omega_p .
> $$
>
> The same formulas are used for forms given on an open subset $U \subseteq M$; so $\omega = \sum_A f_A\, dx^A$ on $U$ in Definition [[§80 Differential Forms on Manifolds#^def-80-3|§80.3]].
>
> *Lee: Ch. 14, Differential Forms on Manifolds*

^def-80-7

> [!definition] Definition §80.8: Wedge Product of Forms on a Manifold
> *(Not from lecture; filled in.)* Let $\omega$ be a $k$-form and $\eta$ an $l$-form on $M$. Their **wedge product** is the $(k + l)$-form $\omega \wedge \eta$ given at every $p \in M$ by the wedge product of Definition [[§77 The Wedge Product#^def-77-1|§77.1]]:
>
> $$
> (\omega \wedge \eta)_p = \omega_p \wedge \eta_p .
> $$
>
> For a $0$-form $f$, $f \wedge \eta = f\eta$. The same formula is used on an open subset $U \subseteq M$; so $dx^A = dx^{a_1} \wedge \cdots \wedge dx^{a_k}$ as $k$-forms on $U$.
>
> *Lee: Ch. 14, Differential Forms on Manifolds*

^def-80-8

The properties of Proposition [[§78 Properties of the Wedge Product#^prop-78-4|§78.4]] hold pointwise, hence for forms on $M$: the wedge product is bilinear (also over functions: $(f\omega) \wedge \eta = f\, (\omega \wedge \eta) = \omega \wedge (f\eta)$, since $f(p)$ is a scalar at each point), associative, and $\eta \wedge \omega = (-1)^{kl}\, \omega \wedge \eta$. In particular functions, of degree $0$, commute with all forms, and a one-form $\theta$ has $\theta \wedge \theta = 0$ (Corollary [[§78 Properties of the Wedge Product#^cor-78-5|§78.5]]).

> [!theorem] Proposition §80.4: Pointwise Operations Preserve Smoothness
> If $\omega, \omega' \in \Omega^k(M)$, $\eta \in \Omega^l(M)$, $f \in C^\infty(M)$ and $c \in \mathbb{R}$, then $\omega + c\,\omega' \in \Omega^k(M)$, $f\omega \in \Omega^k(M)$ and $\omega \wedge \eta \in \Omega^{k+l}(M)$. In particular $\Omega^k(M)$ is a vector space.

^prop-80-4

> [!proof]+ Proof
> *(Not from lecture; filled in.)* Fix $p \in M$ and a chart $(U, \varphi = (x^i))$ at $p$. By Lemma [[§80 Differential Forms on Manifolds#^lem-80-2|§80.2]] the components $f_A$, $f'_A$ of $\omega$, $\omega'$ and $h_C$ of $\eta$ in this chart are smooth on $U$. The components of $\omega + c\,\omega'$ and of $f\omega$ are $f_A + c f'_A$ and $f f_A$, smooth. For the wedge product, bilinearity gives $\omega \wedge \eta = \sum_{A, C} f_A h_C\, dx^A \wedge dx^C$ on $U$, with $C$ running over the $l$-element subsets. By associativity, $dx^A \wedge dx^C = dx^{a_1} \wedge \cdots \wedge dx^{a_k} \wedge dx^{c_1} \wedge \cdots \wedge dx^{c_l}$. If $A \cap C \neq \varnothing$, two factors are equal; moving them next to each other changes at most the sign (graded anticommutativity for one-forms, $dx^a \wedge dx^b = -dx^b \wedge dx^a$), and then $dx^c \wedge dx^c = 0$ makes the product $0$. If $A \cap C = \varnothing$, sorting the $k + l$ factors into increasing order by exchanges of neighbours gives $dx^A \wedge dx^C = \pm\, dx^{A \cup C}$, with a sign that depends only on $A$ and $C$, not on the point. So each component of $\omega \wedge \eta$ is a finite sum of terms $\pm f_A h_C$, smooth on $U$. As $p$ was arbitrary, the forms are smooth by Definition [[§80 Differential Forms on Manifolds#^def-80-4|§80.4]].

^pf-80-4

*Uses:* [[§80 Differential Forms on Manifolds#^lem-80-2|§80.2]], [[§80 Differential Forms on Manifolds#^def-80-4|Def. §80.4]]

*(Lecture 31, as a definition and a lemma combined.)* A smooth map pulls forms back, pointwise, by the pullback of linear forms through its differential.

> [!definition] Definition §80.9: Pullback of $k$-Forms
> Let $F : M \to N$ be a smooth map. For a $k$-form $\omega$ on $N$, the **pullback** $F^{\ast}\omega$ is the $k$-form on $M$ given at each $p \in M$ by
>
> $$
> (F^{\ast}\omega)_p = (dF_p)^{\ast}\, \omega_{F(p)}, \qquad \text{that is,} \qquad (F^{\ast}\omega)_p(v^1, \ldots, v^k) = \omega_{F(p)}\big(dF_p v^1, \ldots, dF_p v^k\big) ,
> $$
>
> where $dF_p : T_pM \to T_{F(p)}N$ is the differential and $(dF_p)^{\ast} : \Lambda^k T^{\ast}_{F(p)}N \to \Lambda^k T_p^{\ast}M$ its pullback (Definition [[§79 Pullbacks of Linear Forms#^def-79-1|§79.1]]).
>
> *Lee: Ch. 14, Differential Forms on Manifolds*

^def-80-9

> [!remark]- Connections
> - The earlier cases: functions, [[§53 One-Forms#^def-53-7|Def. §53.7]]; one-forms, [[§53 One-Forms#^def-53-8|Def. §53.8]]; covectors at a point, [[§34 The Cotangent Space from Germs#^def-34-3|Def. §34.3]].
> - The linear algebra at each point: [[§79 Pullbacks of Linear Forms#^def-79-1|Def. §79.1]].

The lecture stated the definition for smooth forms, as a map $F^{\ast} : \Omega^k(N) \to \Omega^k(M)$; that $F^{\ast}\omega$ is smooth when $\omega$ is, is Proposition [[§80 Differential Forms on Manifolds#^prop-80-5|§80.5]](5) below. The definition is pointwise. Fix $p$; the differential $dF_p$ is a linear map $T_pM \to T_{F(p)}N$, and $\omega_{F(p)}$ is in $\Lambda^k$ of the dual of the target, so it can be pulled back as in [[§79 Pullbacks of Linear Forms|§79]]. For $k = 0$, $(dF_p)^{\ast}$ is the identity of $\mathbb{R}$, so $(F^{\ast}g)(p) = g(F(p))$: $F^{\ast}g = g \circ F$ is the pullback of functions (Definition [[§53 One-Forms#^def-53-7|§53.7]]). For $k = 1$ it is the pullback of one-forms (Definition [[§53 One-Forms#^def-53-8|§53.8]]). In charts, the matrix of the linear map $dF_p$ is the Jacobian of $F$ (Theorem [[§30 The Differential in Coordinates#^thm-30-2|§30.2]]), and induced coordinates give induced bases $dx^A$, $dy^B$ of the wedges; so the pullback is computed by minors of the Jacobian, part (4) below. None of these determinants has to be remembered: in practice, by parts (2) and (3), one only substitutes and computes wedges.

> [!theorem] Proposition §80.5: Properties of the Pullback of Forms
> Let $F : M \to N$ be smooth.
>
> 1. $F^{\ast}(\omega + c\,\omega') = F^{\ast}\omega + c\, F^{\ast}\omega'$ for $k$-forms $\omega, \omega'$ on $N$ and $c \in \mathbb{R}$.
> 2. $F^{\ast}(\omega \wedge \eta) = F^{\ast}\omega \wedge F^{\ast}\eta$ for forms $\omega$, $\eta$ on $N$; in particular $F^{\ast}(g\,\omega) = (g \circ F)\, F^{\ast}\omega$ for a function $g$ on $N$.
> 3. $F^{\ast}(dg) = d(F^{\ast}g)$ for $g \in C^\infty(N)$.
> 4. Let $(U, \varphi = (x^1, \ldots, x^m))$ and $(V, \psi = (y^1, \ldots, y^n))$ be smooth charts of $M$ and $N$ with $F(U) \subseteq V$, and $F^j = y^j \circ F$ on $U$. If $\omega = \sum_B g_B\, dy^B$ on $V$, then on $U$
>
> $$
> F^{\ast}\omega = \sum_B (g_B \circ F)\; dF^{b_1} \wedge \cdots \wedge dF^{b_k} = \sum_A \Big( \sum_B (g_B \circ F)\, \det\Big( \frac{\partial F^{b_i}}{\partial x^{a_j}} \Big)_{i, j = 1, \ldots, k} \Big)\, dx^A .
> $$
>
> 5. If $\omega \in \Omega^k(N)$, then $F^{\ast}\omega \in \Omega^k(M)$; so $F^{\ast} : \Omega^k(N) \to \Omega^k(M)$ is a linear map.
>
> *Lee: Lemma 14.16*

^prop-80-5

> [!proof]+ Proof
> *(Lecture 31 observed (3), by the chain rule, and (2), from its linear version; the rest is filled in.)* (1) and (2) hold at each point $p$, by Lemma [[§79 Pullbacks of Linear Forms#^lem-79-1|§79.1]](2) and Proposition [[§79 Pullbacks of Linear Forms#^prop-79-4|§79.4]] for the linear map $dF_p$. For a function $g$ (a $0$-form), $g\,\omega = g \wedge \omega$ and $F^{\ast}g = g \circ F$, so $F^{\ast}(g\,\omega) = (g \circ F) \wedge F^{\ast}\omega = (g \circ F)\, F^{\ast}\omega$.
>
> (3) is Corollary [[§53 One-Forms#^cor-53-5|§53.5]] (Lecture 15), a consequence of the chain rule.
>
> (4) The forms on both sides are determined pointwise, so the open subset $U$ may be used in place of $M$ and the map $F|_U : U \to V$ in place of $F$. By (1) and (2), $F^{\ast}\big(g_B\, dy^{b_1} \wedge \cdots \wedge dy^{b_k}\big) = (g_B \circ F)\, F^{\ast}(dy^{b_1}) \wedge \cdots \wedge F^{\ast}(dy^{b_k})$, and by (3), applied to the function $y^b \in C^\infty(V)$, $F^{\ast}(dy^b) = d(y^b \circ F) = dF^b$. Summing over $B$ gives the first equality. For the second, fix $p \in U$. By Proposition [[§79 Pullbacks of Linear Forms#^prop-79-2|§79.2]] for the linear map $dF_p$, with the bases $\partial/\partial x^a|_p$ and $\partial/\partial y^b|_{F(p)}$ and their dual bases (Lemma [[§33 Covectors in Coordinates#^lem-33-1|§33.1]]), the $dx^A|_p$-coefficient of $(dF_p)^{\ast}\big(dy^B|_{F(p)}\big)$ is the minor with entries
>
> $$
> \begin{aligned}
> dy^{b_i}\big|_{F(p)}\Big( dF_p \frac{\partial}{\partial x^{a_j}}\Big|_p \Big) &= \Big( F_p^{\ast}\, dy^{b_i}\big|_{F(p)} \Big)\Big( \frac{\partial}{\partial x^{a_j}}\Big|_p \Big) \\
> &= dF^{b_i}_p\Big( \frac{\partial}{\partial x^{a_j}}\Big|_p \Big) = \frac{\partial F^{b_i}}{\partial x^{a_j}}(p) ,
> \end{aligned}
> $$
>
> by Definition [[§34 The Cotangent Space from Germs#^def-34-3|§34.3]], Proposition [[§34 The Cotangent Space from Germs#^prop-34-7|§34.7]] and Proposition [[§32 The Cotangent Space#^prop-32-2|§32.2]]: the minor of the Jacobian $\big(\partial F^j/\partial x^i(p)\big)$ of $F$ (Theorem [[§30 The Differential in Coordinates#^thm-30-2|§30.2]]) in the rows $b_1, \ldots, b_k$ and the columns $a_1, \ldots, a_k$. Since, by (1),
>
> $$
> (F^{\ast}\omega)_p = \sum_B g_B(F(p))\; (dF_p)^{\ast}\big(dy^B|_{F(p)}\big) ,
> $$
>
> this is the second equality at $p$.
>
> (5) Let $p \in M$. By Lemma [[§19 Smooth Functions and Smooth Maps#^lem-19-3|§19.3]] there are charts $(U, \varphi)$ at $p$ and $(V, \psi)$ at $F(p)$ with $F(U) \subseteq V$. The components $g_B$ of $\omega$ are smooth on $V$ (Lemma [[§80 Differential Forms on Manifolds#^lem-80-2|§80.2]]), so $g_B \circ F$ is smooth on $U$ (Lemma [[§19 Smooth Functions and Smooth Maps#^lem-19-5|§19.5]]); each $F^b = y^b \circ F$ is smooth on $U$, so $\partial F^b/\partial x^a$ is smooth on $U$ (Lemma [[§29 Coordinate Derivations and the Basis Theorem#^lem-29-3|§29.3]]). By (4) the components of $F^{\ast}\omega$ in the chart $(U, \varphi)$ are sums of products of these, hence smooth, and $F^{\ast}\omega$ is smooth by Definition [[§80 Differential Forms on Manifolds#^def-80-4|§80.4]]. Linearity is (1).

^pf-80-5

*Uses:* [[§79 Pullbacks of Linear Forms#^lem-79-1|§79.1]], [[§79 Pullbacks of Linear Forms#^prop-79-4|§79.4]], [[§53 One-Forms#^cor-53-5|§53.5]], [[§79 Pullbacks of Linear Forms#^prop-79-2|§79.2]], [[§33 Covectors in Coordinates#^lem-33-1|§33.1]], [[§34 The Cotangent Space from Germs#^def-34-3|Def. §34.3]], [[§34 The Cotangent Space from Germs#^prop-34-7|§34.7]], [[§32 The Cotangent Space#^prop-32-2|§32.2]], [[§30 The Differential in Coordinates#^thm-30-2|§30.2]], [[§19 Smooth Functions and Smooth Maps#^lem-19-3|§19.3]], [[§80 Differential Forms on Manifolds#^lem-80-2|§80.2]], [[§19 Smooth Functions and Smooth Maps#^lem-19-5|§19.5]], [[§29 Coordinate Derivations and the Basis Theorem#^lem-29-3|§29.3]], [[§80 Differential Forms on Manifolds#^def-80-4|Def. §80.4]]

> [!example] Example §80.1: A Pullback from $\mathbb{R}^2$ to $\mathbb{R}^3$
> *(Lecture 31.)* Let $F : \mathbb{R}^2 \to \mathbb{R}^3$,
>
> $$
> F(u, v) = \Big( u + v,\ u - v,\ \frac{u^2 + v^2}{2} \Big) , \qquad \omega = xy\; dy \wedge dz \in \Omega^2(\mathbb{R}^3) .
> $$
>
> (Different letters are used for the coordinates on the two sides: $(u, v)$ on $\mathbb{R}^2$ and $(x, y, z)$ on $\mathbb{R}^3$.) $F^{\ast}\omega$ is a two-form on $\mathbb{R}^2$, a top-degree form: pointwise there is only one basis element (the bundle $\Lambda^2 T^{\ast}\mathbb{R}^2$ has rank $\binom{2}{2} = 1$), so $F^{\ast}\omega = (\text{some function})\; du \wedge dv$. To find it, write the map as a change of variables,
>
> $$
> x = u + v, \qquad y = u - v, \qquad z = \frac{u^2 + v^2}{2} ,
> $$
>
> the components $F^1, F^2, F^3$ of $F$. Then $dy = du - dv$ and $dz = u\, du + v\, dv$, and substituting,
>
> $$
> \begin{aligned}
> F^{\ast}\omega &= (u + v)(u - v)\; (du - dv) \wedge (u\, du + v\, dv) \\
> &= (u^2 - v^2)\, \big( v\; du \wedge dv - u\; dv \wedge du \big) \\
> &= (u^2 - v^2)(u + v)\; du \wedge dv .
> \end{aligned}
> $$
>
> *Lee: cf. Example 14.18*

^ex-80-1

> [!proof]+ Justification
> *(Lecture 31 did the computation first and justified it afterwards in words; the justification is written out.)* The first line is Proposition [[§80 Differential Forms on Manifolds#^prop-80-5|§80.5]](4) with $\omega = g\, dy \wedge dz$, $g = xy$ and $B = \{2, 3\}$: $g \circ F = (u + v)(u - v)$, and $dF^2 = d(u - v) = du - dv$, $dF^3 = d\big(\tfrac{u^2 + v^2}{2}\big) = u\, du + v\, dv$ by Lemma [[§33 Covectors in Coordinates#^lem-33-1|§33.1]]. For the second, distribute the wedge product (bilinearity): $du \wedge du = dv \wedge dv = 0$ (Corollary [[§78 Properties of the Wedge Product#^cor-78-5|§78.5]]), so only the cross terms remain, $du \wedge (v\, dv) = v\, du \wedge dv$ (functions commute with forms, being forms of even degree) and $(-dv) \wedge (u\, du) = -u\, dv \wedge du$. For the third, $dv \wedge du = -du \wedge dv$, so the bracket is $(v + u)\, du \wedge dv$.
>
> *Check with the determinant formula.* By the second equality of Proposition [[§80 Differential Forms on Manifolds#^prop-80-5|§80.5]](4), with $A = \{1, 2\}$ and $B = \{2, 3\}$, the coefficient is $g \circ F$ times the minor of the Jacobian of $F$ in the rows $2, 3$:
>
> $$
> \det \begin{pmatrix} \partial F^2/\partial u & \partial F^2/\partial v \\ \partial F^3/\partial u & \partial F^3/\partial v \end{pmatrix} = \det \begin{pmatrix} 1 & -1 \\ u & v \end{pmatrix} = u + v .
> $$
>
> The Jacobians of the general formula are all contained in the computation above: substituting $x = F^1$, $y = F^2$, $z = F^3$ and computing $dF^2 \wedge dF^3$ computes this minor of the Jacobian.

^pf-ex-80-1

*Uses:* [[§80 Differential Forms on Manifolds#^prop-80-5|§80.5]], [[§33 Covectors in Coordinates#^lem-33-1|§33.1]], [[§78 Properties of the Wedge Product#^cor-78-5|§78.5]]

**Transcription note (Lecture 31).** The board first wrote $dz = u\, du + 2v\, dv$, and the $2$ was then struck out. The correct $dz = u\, du + v\, dv$ is the one used in the computation.

> [!remark] Remark: Putting $F^{\ast}$ Everywhere
> *(Lecture 32 returned to Example [[§80 Differential Forms on Manifolds#^ex-80-1|§80.1]] to justify the practical computation.)* Regard $\omega = x\, y\, dy \wedge dz$ as a wedge product of four factors, the $0$-forms $x$ and $y$ (for which the wedge product is the ordinary product) and the one-forms $dy$ and $dz$. The pullback of a wedge product is the wedge product of the pullbacks (Proposition [[§80 Differential Forms on Manifolds#^prop-80-5|§80.5]](2)), a pointwise property, so
>
> $$
> F^{\ast}\omega = F^{\ast}(x)\, F^{\ast}(y)\; F^{\ast}(dy) \wedge F^{\ast}(dz) ,
> $$
>
> and since the pullback commutes with $d$ on functions (Proposition [[§80 Differential Forms on Manifolds#^prop-80-5|§80.5]](3), from September),
>
> $$
> F^{\ast}\omega = F^{\ast}(x)\, F^{\ast}(y)\; d\big(F^{\ast}y\big) \wedge d\big(F^{\ast}z\big) .
> $$
>
> Here $x$ is the function taking the first coordinate, so $F^{\ast}x = x \circ F = u + v$; likewise $F^{\ast}y = u - v$ and $F^{\ast}z = \frac12(u^2 + v^2)$. Compared with the practical computation, the only thing missing there is a number of $F^{\ast}$'s: “$x = u + v$” stands for $F^{\ast}x = u + v$, and “$dx = du + dv$” for $F^{\ast}(dx) = d(F^{\ast}x) = du + dv$. One puts $F^{\ast}$ in front of everything, and then stops writing it.

^rem-80-1

**Transcription note (Lecture 32).** The board wrote “$y = du - dv$” for $dy = du - dv$, and then $F^{\ast}\omega = (u + v)(u - v)(du + dv) \wedge (u\, du + v\, dv)$. Since $\omega$ contains $dy \wedge dz$, the first one-form is $F^{\ast}(dy) = du - dv$, as in Example [[§80 Differential Forms on Manifolds#^ex-80-1|§80.1]]; $du + dv = F^{\ast}(dx)$ does not occur.

![[m591-78-2.svg]]

*(Not from lecture; figure added.)* Example [[§80 Differential Forms on Manifolds#^ex-80-1|§80.1]] at the point $p = (u, v) = (0.6, -0.3)$. $F$ maps the square $[-1, 1]^2$ onto a piece of the paraboloid $z = (x^2 + y^2)/4$ (since $x^2 + y^2 = 2(u^2 + v^2)$); the grid lines $u = \mathrm{const}$ (blue) and $v = \mathrm{const}$ (red) go to curves on it. The differential pushes the coordinate vectors to the tangent vectors $dF_p(\partial_u) = \partial F/\partial u = (1, 1, u)$ and $dF_p(\partial_v) = (1, -1, v)$ of the surface, and by Definition [[§80 Differential Forms on Manifolds#^def-80-9|§80.9]], $(F^{\ast}\omega)_p(\partial_u, \partial_v) = \omega_{F(p)}\big(dF_p \partial_u, dF_p \partial_v\big) = xy\, \big(1 \cdot v - u \cdot (-1)\big) = (u^2 - v^2)(u + v)$, the coefficient found above.

![[m591-78-a2.gif|680]]

*(Not from lecture; animation added, vault only.)* The same picture with $p$ moving once around a closed curve in the $(u, v)$-plane. The differential pushes $\partial_u$ (red) and $\partial_v$ (blue) to tangent vectors of the paraboloid, and the number shown is $\omega_{F(p)}$ evaluated on the two pushed vectors, which is $(F^{\ast}\omega)_p(\partial_u, \partial_v) = (u^2 - v^2)(u + v)$: the coefficient of $du \wedge dv$ in $F^{\ast}\omega$ at $p$. It changes sign where $u = \pm v$.

*Not from lecture: top degree on manifolds.* For a map between manifolds of the same dimension, part (4) has one term, the boxed formula of Proposition [[§79 Pullbacks of Linear Forms#^prop-79-3|§79.3]] at every point; this is the formula that will make integrals of top-degree forms independent of the chart.

> [!theorem] Corollary §80.6: Pullback of Top-Degree Forms
> *(Not from lecture.)* Let $F : M \to N$ be smooth with $\dim M = \dim N = m$, and let $(U, (x^i))$, $(V, (y^j))$ be smooth charts with $F(U) \subseteq V$. For a function $g$ on $V$, on $U$
>
> $$
> F^{\ast}\big( g\; dy^1 \wedge \cdots \wedge dy^m \big) = (g \circ F)\, \det\Big( \frac{\partial F^j}{\partial x^i} \Big)\; dx^1 \wedge \cdots \wedge dx^m ,
> $$
>
> with the Jacobian of $F$ in these charts. In particular, for two charts at the same points, $dy^1 \wedge \cdots \wedge dy^m = \det\big(\partial y^j/\partial x^i\big)\, dx^1 \wedge \cdots \wedge dx^m$ on $U \cap V$.
>
> *Lee: Proposition 14.20; Corollary 14.21*

^cor-80-6

> [!proof]+ Proof
> *(Filled in.)* Proposition [[§80 Differential Forms on Manifolds#^prop-80-5|§80.5]](4) with $k = m$ has the single term $A = B = \{1, \ldots, m\}$, whose minor is the whole Jacobian (the determinant of a matrix equals that of its transpose, so it does not matter which index labels rows). That proof uses only the pointwise formulas, so it applies to any function $g$, smooth or not. The second statement is the first for the identity map of $U \cap V$, in the charts $(x^i)$ on the domain and $(y^j)$ on the target; it is also Lemma [[§80 Differential Forms on Manifolds#^lem-80-1|§80.1]] with $k = m$.

^pf-80-6

*Uses:* [[§80 Differential Forms on Manifolds#^prop-80-5|§80.5]], [[§80 Differential Forms on Manifolds#^lem-80-1|§80.1]]

> [!example] Example §80.2: Polar Coordinates
> *(Not from lecture.)* On $\mathbb{R}^2$ minus a closed ray from the origin, use the polar coordinates $(r, \vartheta)$ in the domain and $(x, y)$ in the target of the identity map, $x = r\cos\vartheta$, $y = r\sin\vartheta$. Substituting as in Example [[§80 Differential Forms on Manifolds#^ex-80-1|§80.1]],
>
> $$
> \begin{aligned}
> dx \wedge dy &= (\cos\vartheta\; dr - r\sin\vartheta\; d\vartheta) \wedge (\sin\vartheta\; dr + r\cos\vartheta\; d\vartheta) \\
> &= r\cos^2\vartheta\; dr \wedge d\vartheta - r\sin^2\vartheta\; d\vartheta \wedge dr = r\; dr \wedge d\vartheta ,
> \end{aligned}
> $$
>
> and $r = \det \begin{pmatrix} \cos\vartheta & -r\sin\vartheta \\ \sin\vartheta & r\cos\vartheta \end{pmatrix}$ is the Jacobian determinant of Corollary [[§80 Differential Forms on Manifolds#^cor-80-6|§80.6]]: the factor $r$ of $dx\, dy = r\, dr\, d\vartheta$ in the change of variables formula for double integrals.
>
> *Lee: Example 14.19*

^ex-80-2

> [!remark]- Connections
> - The factor $r$ in polar coordinates, as a change of variables in a double integral: [[§22 Properties of the Integral#^thm-22-6|452 Thm. §22.6]].
> - Polar coordinates as a chart, with $\partial_r$ and $\partial_\vartheta$: [[§30 The Differential in Coordinates#^ex-30-1|Ex. §30.1]].

Next: the exterior derivative, which extends $d : \Omega^0(M) \to \Omega^1(M)$ to forms of every degree ([[§81 The Exterior Derivative|§81]]).
