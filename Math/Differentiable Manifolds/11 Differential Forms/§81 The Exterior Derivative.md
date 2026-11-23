---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 11
section: 81
tags: [differentiable-manifolds, math591]
---
← [[§80 Differential Forms on Manifolds]] · ↑ [[· 11 Differential Forms]] · [[§82 De Rham Cohomology]] →

*Stage: forms — The operator $d$ on forms of every degree, characterized by four axioms; constructed on open subsets of $\mathbb{R}^m$ by a forced formula, then on manifolds through charts.*

*(Lecture 32.)* The main object of this section is the *exterior derivative* $d$ (also called the *exterior differential*). It extends the differential of functions, $d : \Omega^0(M) \to \Omega^1(M)$ (Proposition [[§53 One-Forms#^prop-53-3|§53.3]]), to forms of every degree. The cleanest way to present the theory is axiomatic, by four properties that characterize $d$; it is also the most opaque about what $d$ means, and the meaning (in $\mathbb{R}^3$, the curl and the divergence, and its relation to Stokes' theorem of [[§73 Stokes' Theorem in Calculus III|§73]]) will be explained later. Throughout, $M$ is a smooth manifold of dimension $m$.

> [!remark] Remark: Notation of Lecture 32
> In addition to the remark *Notation of Lecture 31* ([[§79 Pullbacks of Linear Forms|§79]]):
> - *Sums over index sets.* A sum $\sum_A$ is always over the $k$-element subsets $A = \{a_1 < \cdots < a_k\}$ of $\{1, \ldots, m\}$, that is, over increasing indices, and $dx^A = dx^{a_1} \wedge \cdots \wedge dx^{a_k}$. Lee writes such sums with a prime, $\sum'$, as a reminder that the indices increase; the board occasionally does too. Sums $\sum_j$ over a single index run over $1, \ldots, m$ with no restriction.
> - *Coordinates.* On an open subset $U \subseteq \mathbb{R}^m$, Step I uses the board's $x^1, \ldots, x^m$ for the standard coordinates (the identity chart, whose coordinates the notes elsewhere call $r^i$), and $y^1, \ldots, y^n$ on an open subset of $\mathbb{R}^n$. In Step II, where a chart $\varphi = (x^1, \ldots, x^m)$ of $M$ appears, the standard coordinates of $\mathbb{R}^m$ are $r^1, \ldots, r^m$ again, and $x^i = r^i \circ \varphi$.
> - *One letter for many operators.* All the operators $d : \Omega^k(M) \to \Omega^{k+1}(M)$, for all $k$ and all manifolds, are written $d$; they have different domains and targets, and the context says which is meant. Where it matters, $d_M$ is the one on $M$.
> - *Degree.* $|\alpha|$ is the degree of $\alpha$ (Definition [[§80 Differential Forms on Manifolds#^def-80-2|§80.2]]); in the product rule $\alpha$ has a single degree $k$.
> - *Betti numbers.* The board writes $\beta_k$ for the $k$-th Betti number ([[§82 De Rham Cohomology|§82]]). Since $\beta$ denotes a form throughout this chapter, these notes write $b_k$.
> - *Cohomology.* The board's $H^k(M)$ is Lee's $H^k_{\mathrm{dR}}(M)$.

^rem-81-1

> [!definition] Definition §81.1: The Four Properties of an Exterior Derivative
> Suppose that on every smooth manifold $M$, of any dimension $m$, a sequence of linear operators
>
> $$
> \Omega^0(M) = C^\infty(M) \xrightarrow{\ d\ } \Omega^1(M) \xrightarrow{\ d\ } \Omega^2(M) \xrightarrow{\ d\ } \cdots \xrightarrow{\ d\ } \Omega^m(M) \xrightarrow{\ d\ } 0
> $$
>
> is given. These operators have the **properties of an exterior derivative** if:
>
> 1. $d : \Omega^0(M) \to \Omega^1(M)$ is the differential of functions (Definition [[§32 The Cotangent Space#^def-32-5|§32.5]], Proposition [[§53 One-Forms#^prop-53-3|§53.3]]);
> 2. *(product rule)* $d(\alpha \wedge \beta) = (d\alpha) \wedge \beta + (-1)^{|\alpha|}\, \alpha \wedge (d\beta)$ for $\alpha \in \Omega^k(M)$ and $\beta \in \Omega^l(M)$;
> 3. $d \circ d = 0$, wherever the composition is defined;
> 4. *(naturality)* if $F : M \to N$ is a smooth map, then $F^{\ast}(d\beta) = d(F^{\ast}\beta)$ for every $\beta \in \Omega^k(N)$.
>
> *Source: Lecture 32*
>
> *Lee: Theorem 14.24; Proposition 14.26*

^def-81-1

Lecture 32 stated a theorem at this point: there exists a unique sequence of linear operators with the four properties. It is Theorem [[§81 The Exterior Derivative#^thm-81-7|§81.7]], after the construction; the properties are recorded first, because the construction uses them.

> [!remark]- Connections
> - The same operator on open subsets of $\mathbb{R}^n$ in MATH 452, defined by the coordinate formula: [[§38 The Exterior Derivative#^def-38-1|452 Def. §38.1]], with $d^2 = 0$ as [[§38 The Exterior Derivative#^thm-38-4|452 Thm. §38.4]].
> - Property (1) is the differential of functions: [[§53 One-Forms#^prop-53-3|§53.3]]; property (4) for functions: [[§53 One-Forms#^cor-53-5|§53.5]].
> - The theorem that there is exactly one such family: [[§81 The Exterior Derivative#^thm-81-7|§81.7]].

*Reading the properties.* The sequence stops at $\Omega^m(M)$ because every form of degree $m + 1$ or more on $M$ is identically zero (Corollary [[§75 Multilinear Algebra#^cor-75-3|§75.3]]); the last $d$ is zero. The operators are all denoted $d$, although they are different operators, with different domains and targets; the notation does not distinguish them. In the product rule, parentheses are written the first time and dropped afterwards: $d\alpha \wedge \beta$ means $(d\alpha) \wedge \beta$. Property (3) makes the sequence a *cochain complex* (in MATH 592, chain complexes appear, with a boundary operator whose square is zero). Property (4) involves the operators on two manifolds, $M$ and $N$: on the left, $d$ is $d_N$, on the right $d_M$. So the properties concern the operators on all smooth manifolds at once, and it is in this sense that uniqueness is proved in Theorem [[§81 The Exterior Derivative#^thm-81-7|§81.7]]: the operators on all manifolds, open subsets of $\mathbb{R}^m$ included, are determined by (1)–(4). (Lee proves uniqueness on a single manifold from (1)–(3) alone, using bump functions to show that $d$ is local; Theorem 14.24.) In the language of commutative diagrams, (4) says that $F^{\ast}$ is a map of cochain complexes:

![[m591-79-1.svg]]

*(Not from lecture; diagram added.)* Each square commutes: going right then down is $F^{\ast}(d\beta)$, going down then right is $d(F^{\ast}\beta)$. For functions, the first square is Corollary [[§53 One-Forms#^cor-53-5|§53.5]], from September; property (4) extends it to all degrees.

*Plan.* The theorem to be proved is that there is exactly one family of operators with these properties (Theorem [[§81 The Exterior Derivative#^thm-81-7|§81.7]]). I. Do the case of an open subset $M \subseteq \mathbb{R}^m$, proving all four properties there; for (4), $M \subseteq \mathbb{R}^m$ and $N \subseteq \mathbb{R}^n$ are both open. II. Use charts to pass to manifolds. This is possible because $d$ is a differential operator, of order one: it takes one derivative of each component, so it is local.

## Step I: open subsets of $\mathbb{R}^m$

Let $U \subseteq \mathbb{R}^m$ be open, with the standard coordinates $x^1, \ldots, x^m$. A $k$-form $\alpha \in \Omega^k(U)$ is written once more as

$$
\alpha = \sum_A f_A\, dx^A , \qquad f_A \in C^\infty(U), \qquad dx^A = dx^{a_1} \wedge \cdots \wedge dx^{a_k} ,
$$

the sum over $A = \{a_1 < \cdots < a_k\} \subseteq \{1, \ldots, m\}$ (Definition [[§80 Differential Forms on Manifolds#^def-80-3|§80.3]] for the identity chart, Lemma [[§80 Differential Forms on Manifolds#^lem-80-2|§80.2]]).

*The formula is forced.* Suppose that operators $d$ with properties (1)–(3) exist on $U$. By linearity, $d\alpha = \sum_A d(f_A\, dx^A)$. Since $f_A$ is a $0$-form, $f_A\, dx^A = f_A \wedge dx^A$, and the product rule (2), with $|f_A| = 0$, gives

$$
d\alpha = \sum_A \Big( df_A \wedge dx^A + f_A\, d\big(dx^A\big) \Big) .
$$

Now $d(dx^A) = d\big(dx^{a_1} \wedge \cdots \wedge dx^{a_k}\big)$ can be expanded by the product rule again, and each term of the expansion contains a factor $d(dx^{a_i}) = d\big(d(x^{a_i})\big)$, which is zero by (1) and (3). So $d(dx^A) = 0$ and $d\alpha = \sum_A df_A \wedge dx^A$. The logic: if $d$ exists, this computation can be done, and it leads to this formula. The formula is now taken as the definition, and the properties have to be checked.

> [!definition] Definition §81.2: Exterior Derivative on Open Subsets of $\mathbb{R}^m$
> Let $U \subseteq \mathbb{R}^m$ be open and $\alpha = \sum_A f_A\, dx^A \in \Omega^k(U)$. Its **exterior derivative** is
>
> $$
> d\alpha = \sum_A df_A \wedge dx^A = \sum_A \sum_{j=1}^m \frac{\partial f_A}{\partial x^j}\; dx^j \wedge dx^{a_1} \wedge \cdots \wedge dx^{a_k} \ \in \Omega^{k+1}(U) .
> $$
>
> *Lee: Ch. 14, The Exterior Derivative, (14.19)–(14.20)*

^def-81-2

The second expression substitutes $df_A = \sum_j \frac{\partial f_A}{\partial x^j}\, dx^j$ (Lemma [[§33 Covectors in Coordinates#^lem-33-1|§33.1]]). The form $d\alpha$ is smooth by Proposition [[§80 Differential Forms on Manifolds#^prop-80-4|§80.4]], and $d$ is linear, since the components $f_A$ depend linearly on $\alpha$ and $f \mapsto df$ is linear. On a function, $k = 0$: the only index set is $A = \varnothing$, with $dx^\varnothing = 1$, so $df$ is the differential of $f$ — there are no $dx$'s, only the number $1$, and that is how the definition reads. Note that $dx^j \wedge dx^A$ is not, in general, one of the basis forms $dx^{A'}$: $j$ may be out of order, or repeated.

> [!theorem] Lemma §81.1: Wedging $dx^j$ onto $dx^A$
> Let $j \in \{1, \ldots, m\}$ and $A = \{a_1 < \cdots < a_k\} \subseteq \{1, \ldots, m\}$. Then
>
> $$
> dx^j \wedge dx^A = \begin{cases} 0 & \text{if } j \in A, \\ \pm\, dx^{A \cup \{j\}} & \text{if } j \notin A, \end{cases}
> $$
>
> with the sign $(-1)^s$, where $s$ is the number of elements of $A$ smaller than $j$.
>
> *Lee: Ch. 14, The Exterior Derivative*

^lem-81-1

> [!proof]+ Proof
> *(Lecture 32; the sign is filled in.)* All the forms are one-forms at each point, and for one-forms $\theta \wedge \theta' = -\theta' \wedge \theta$ (Proposition [[§78 Properties of the Wedge Product#^prop-78-4|§78.4]](3) with $k = l = 1$), while the wedge product is associative. If $j = a_i \in A$, move $dx^j$ to the right past $dx^{a_1}, \ldots, dx^{a_{i-1}}$; this changes the sign $i - 1$ times and puts $dx^j$ next to $dx^{a_i} = dx^j$. For every one-form $\theta$, $\theta \wedge \theta = 0$, because exchanging the two factors gives $\theta \wedge \theta = -\,\theta \wedge \theta$ (Corollary [[§78 Properties of the Wedge Product#^cor-78-5|§78.5]]). So the product is $0$. If $j \notin A$, move $dx^j$ to the right past the $s$ factors $dx^{a_i}$ with $a_i < j$; this gives $(-1)^s$ times a wedge product of the $dx^c$, $c \in A \cup \{j\}$, in increasing order, which is $dx^{A \cup \{j\}}$.

^pf-81-1

*Uses:* [[§78 Properties of the Wedge Product#^prop-78-4|§78.4]], [[§78 Properties of the Wedge Product#^cor-78-5|§78.5]]

So the definition can be rewritten as $d\alpha = \sum_A \sum_{j \notin A} \pm \frac{\partial f_A}{\partial x^j}\, dx^{A \cup \{j\}}$: an expression of the same kind as the one we started with, except for the signs. The same reasoning gives the following lemma, which says that the defining formula may be used for any product of $dx$'s, sorted or not.

> [!theorem] Lemma §81.2: The Formula for Unsorted Indices
> Let $U \subseteq \mathbb{R}^m$ be open, $f \in C^\infty(U)$ and $c_1, \ldots, c_k \in \{1, \ldots, m\}$, in any order and possibly repeated. Then
>
> $$
> d\big( f\, dx^{c_1} \wedge \cdots \wedge dx^{c_k} \big) = df \wedge dx^{c_1} \wedge \cdots \wedge dx^{c_k} .
> $$

^lem-81-2

> [!proof]+ Proof
> *(Filled in; Lecture 32 used it implicitly.)* As in the proof of Lemma [[§81 The Exterior Derivative#^lem-81-1|§81.1]] (and of Proposition [[§80 Differential Forms on Manifolds#^prop-80-4|§80.4]]), exchanging neighbouring factors shows that $dx^{c_1} \wedge \cdots \wedge dx^{c_k}$ is $0$ if two of the $c_i$ are equal, and otherwise equals $\epsilon\, dx^C$, with $C = \{c_1, \ldots, c_k\}$ and a constant sign $\epsilon = \pm 1$. In the first case both sides are $0$ ($d$ is linear, so $d0 = 0$). In the second, by Definition [[§81 The Exterior Derivative#^def-81-2|§81.2]] and linearity, $d(f\, \epsilon\, dx^C) = \epsilon\, df \wedge dx^C = df \wedge \epsilon\, dx^C$.

^pf-81-2

*Uses:* [[§81 The Exterior Derivative#^lem-81-1|§81.1]], [[§80 Differential Forms on Manifolds#^prop-80-4|§80.4]], [[§81 The Exterior Derivative#^def-81-2|Def. §81.2]]

> [!theorem] Proposition §81.3: Properties of the Euclidean Exterior Derivative
> On open subsets of Euclidean spaces, the operators $d$ of Definition [[§81 The Exterior Derivative#^def-81-2|§81.2]] are linear and satisfy:
>
> 1. on $\Omega^0(U) = C^\infty(U)$, $d$ is the differential of functions;
> 2. $d(\alpha \wedge \beta) = d\alpha \wedge \beta + (-1)^{|\alpha|}\, \alpha \wedge d\beta$ for $\alpha \in \Omega^k(U)$, $\beta \in \Omega^l(U)$;
> 3. $d \circ d = 0$;
> 4. if $U \subseteq \mathbb{R}^m$ and $V \subseteq \mathbb{R}^n$ are open and $F : U \to V$ is smooth, then $F^{\ast}(d\beta) = d(F^{\ast}\beta)$ for every $\beta \in \Omega^k(V)$.
>
> Moreover $d$ commutes with restriction: $(d\alpha)|_{U'} = d(\alpha|_{U'})$ for every open $U' \subseteq U$.
>
> *Lee: Proposition 14.23*

^prop-81-3

> [!remark]- Connections
> - $d^2 = 0$ is the equality of mixed partial derivatives: [[Schwarz–Clairaut Theorem]]; in forms language, [[§39 Closed and Exact Forms#^prop-39-4|452 Prop. §39.4]].
> - The sign in the product rule comes from moving a one-form across $k$ one-forms: graded anticommutativity, [[§78 Properties of the Wedge Product#^prop-78-4|§78.4]](3).

> [!proof]+ Proof
> *(Lecture 32, in this order: (1), (3), (2), (4); the details marked are filled in.)* *Restriction* *(filled in)*: the components of $\alpha|_{U'}$ are the restrictions $f_A|_{U'}$, and the partial derivatives of $f_A|_{U'}$ are the restrictions of those of $f_A$.
>
> (1) This was observed after Definition [[§81 The Exterior Derivative#^def-81-2|§81.2]].
>
> (3) $d^2 = 0$. Let $\alpha = \sum_A f_A\, dx^A$. By the definition, $d\alpha = \sum_A \sum_j \frac{\partial f_A}{\partial x^j}\, dx^j \wedge dx^A$, and by Lemma [[§81 The Exterior Derivative#^lem-81-2|§81.2]] (with the function $\partial f_A/\partial x^j$ and the indices $j, a_1, \ldots, a_k$) and associativity,
>
> $$
> d^2\alpha = \sum_A \sum_j d\Big( \frac{\partial f_A}{\partial x^j} \Big) \wedge dx^j \wedge dx^A = \sum_A \Big( \sum_j d\Big( \frac{\partial f_A}{\partial x^j} \Big) \wedge dx^j \Big) \wedge dx^A = \sum_A d\big(d f_A\big) \wedge dx^A ,
> $$
>
> the last step by the definition of $d$ on the one-form $df_A = \sum_j \frac{\partial f_A}{\partial x^j}\, dx^j$. So it is enough to show that $d^2 f = 0$ for every function $f$; that is, that the composite of the first two arrows of the sequence is zero. By the definition, twice,
>
> $$
> d^2 f = d\Big( \sum_{j=1}^m \frac{\partial f}{\partial x^j}\, dx^j \Big) = \sum_{j=1}^m d\Big( \frac{\partial f}{\partial x^j} \Big) \wedge dx^j = \sum_{j, l = 1}^m \frac{\partial^2 f}{\partial x^l\, \partial x^j}\; dx^l \wedge dx^j ,
> $$
>
> where $\frac{\partial^2 f}{\partial x^l\, \partial x^j} = \frac{\partial}{\partial x^l}\big(\frac{\partial f}{\partial x^j}\big)$. The pairs $(l, j)$ are unrestricted. When $l = j$ the term is $0$, since $dx^j \wedge dx^j = 0$. When $l \neq j$, exchange the names in the terms with $l > j$ and use $dx^j \wedge dx^l = -\,dx^l \wedge dx^j$:
>
> $$
> d^2 f = \sum_{1 \le l < j \le m} \Big( \frac{\partial^2 f}{\partial x^l\, \partial x^j} - \frac{\partial^2 f}{\partial x^j\, \partial x^l} \Big)\, dx^l \wedge dx^j = 0 ,
> $$
>
> because the mixed partials of the smooth function $f$ are equal (Clairaut's theorem). This is where $d^2 = 0$ comes from: it is the calculus fact that mixed partial derivatives commute. (All functions here are smooth, so the mixed partials exist and are continuous.)
>
> (2) Product rule. By linearity in $\alpha$ and in $\beta$, it is enough to consider $\alpha = \sum_A f_A\, dx^A$ of degree $k$ and $\beta = \sum_B g_B\, dx^B$ of degree $l$, with $B$ running over the $l$-element subsets. Functions commute with everything, so they can be brought to the front, and bilinearity gives
>
> $$
> \alpha \wedge \beta = \sum_{A, B} f_A\, g_B\; dx^A \wedge dx^B .
> $$
>
> By Lemma [[§81 The Exterior Derivative#^lem-81-2|§81.2]], since $dx^A \wedge dx^B = dx^{a_1} \wedge \cdots \wedge dx^{a_k} \wedge dx^{b_1} \wedge \cdots \wedge dx^{b_l}$, and the product rule for functions, $d(fg) = f\, dg + g\, df$ (Proposition [[§53 One-Forms#^prop-53-3|§53.3]]),
>
> $$
> d(\alpha \wedge \beta) = \sum_{A, B} d\big(f_A g_B\big) \wedge dx^A \wedge dx^B = \sum_{A, B} \Big( \underbrace{f_A\; dg_B \wedge dx^A \wedge dx^B}_{\text{①}} + \underbrace{g_B\; df_A \wedge dx^A \wedge dx^B}_{\text{②}} \Big) .
> $$
>
> *Terms ②.* Scalars move freely across wedges, so $g_B\, df_A \wedge dx^A \wedge dx^B = (df_A \wedge dx^A) \wedge (g_B\, dx^B)$; summing over $A$ and $B$ and undoing the distributivity gives $\sum_{A, B} \text{②} = d\alpha \wedge \beta$, with no sign.
>
> *Terms ①.* To move $dg_B$ next to $dx^B$, it has to cross $dx^A$. Now $dg_B$ is a one-form, and $dx^A$ is a wedge product of $|A| = k$ one-forms; each exchange of $dg_B$ with one of them gives a factor $-1$, so $dg_B \wedge dx^A = (-1)^k\, dx^A \wedge dg_B$. Hence
>
> $$
> \sum_{A, B} \text{①} = (-1)^{|\alpha|} \sum_{A, B} f_A\, dx^A \wedge \big( dg_B \wedge dx^B \big) = (-1)^{|\alpha|}\, \alpha \wedge d\beta .
> $$
>
> This is where the sign in the product rule comes from.
>
> (4) Naturality. Let $x^1, \ldots, x^m$ be the coordinates on $U \subseteq \mathbb{R}^m$ and $y^1, \ldots, y^n$ those on $V \subseteq \mathbb{R}^n$, and $\beta = \sum_A f_A\, dy^A \in \Omega^k(V)$, now with $A \subseteq \{1, \ldots, n\}$. The task is to show $d\big(F^{\ast}\beta\big) = F^{\ast}(d\beta)$. Both sides are linear in $\beta$, so it is enough to show it for each summand $f_A\, dy^A$. Since the pullback of a wedge product is the wedge product of the pullbacks (Proposition [[§80 Differential Forms on Manifolds#^prop-80-5|§80.5]](2)) and the pullback commutes with $d$ on functions (Proposition [[§80 Differential Forms on Manifolds#^prop-80-5|§80.5]](3)),
>
> $$
> F^{\ast}\big(f_A\, dy^A\big) = F^{\ast}(f_A)\; F^{\ast}(dy^{a_1}) \wedge \cdots \wedge F^{\ast}(dy^{a_k}) = F^{\ast}(f_A)\; d\big(F^{\ast}y^{a_1}\big) \wedge \cdots \wedge d\big(F^{\ast}y^{a_k}\big) ,
> $$
>
> as in the example at the beginning of the lecture (the remark *Putting $F^{\ast}$ Everywhere* in [[§80 Differential Forms on Manifolds|§80]]). Apply $d$, using the properties already proved. By (2), with $F^{\ast}(f_A)$ of degree $0$,
>
> $$
> d\Big( F^{\ast}(f_A)\; d\big(F^{\ast}y^{a_1}\big) \wedge \cdots \wedge d\big(F^{\ast}y^{a_k}\big) \Big) = d\big(F^{\ast}(f_A)\big) \wedge d\big(F^{\ast}y^{a_1}\big) \wedge \cdots \wedge d\big(F^{\ast}y^{a_k}\big) ,
> $$
>
> because the other term contains $d\big(dh_1 \wedge \cdots \wedge dh_k\big)$, with $h_i = F^{\ast}y^{a_i}$, and this is $0$: *(filled in)* by induction on $k$, using (2) and (3), $d\big(dh_1 \wedge (dh_2 \wedge \cdots \wedge dh_k)\big) = d(dh_1) \wedge (\cdots) - dh_1 \wedge d(dh_2 \wedge \cdots \wedge dh_k) = 0 - 0$. Finally, $d\big(F^{\ast}(f_A)\big) = F^{\ast}(df_A)$ (on functions), and the $d(F^{\ast}y^{a_i})$ are again $F^{\ast}(dy^{a_i})$, so
>
> $$
> d\, F^{\ast}\big(f_A\, dy^A\big) = F^{\ast}(df_A) \wedge F^{\ast}(dy^A) = F^{\ast}\big(df_A \wedge dy^A\big) = F^{\ast}\big(d(f_A\, dy^A)\big) ,
> $$
>
> the last step by Definition [[§81 The Exterior Derivative#^def-81-2|§81.2]]. This is (4) for one summand.

^pf-81-3

*Uses:* [[§81 The Exterior Derivative#^def-81-2|Def. §81.2]], [[§81 The Exterior Derivative#^lem-81-2|§81.2]], [[§53 One-Forms#^prop-53-3|§53.3]], [[§80 Differential Forms on Manifolds#^prop-80-5|§80.5]]

**Transcription notes (Lecture 32).** In the proof of (3) the board wrote $d^2\alpha = \sum_A \sum_j d(df_A) \wedge dx^A$; once the inner sum over $j$ has been absorbed into $d(df_A)$, only $\sum_A$ remains. In the proof of (2) the board wrote $\sum_{A, B} \text{②} = d\alpha \wedge d\beta$; the terms ② give $d\alpha \wedge \beta$.

So the exterior derivative exists on open sets of $\mathbb{R}^m$.

## Step II: passing to manifolds

The definition on a manifold transports the Euclidean $d$ through a chart. Its consistency rests on how pullbacks compose, which has been used implicitly so far and is recorded here.

> [!theorem] Lemma §81.4: Pullbacks Compose
> Let $F : M \to N$ and $G : N \to P$ be smooth, and $\omega$ a $k$-form on $P$.
>
> 1. $(G \circ F)^{\ast}\omega = F^{\ast}(G^{\ast}\omega)$, and $\mathrm{id}_P^{\ast}\, \omega = \omega$.
> 2. If $F$ is a diffeomorphism, then $F^{\ast} : \Omega^k(N) \to \Omega^k(M)$ is bijective, with inverse $(F^{-1})^{\ast}$.
> 3. If $U \subseteq M$ is open and $\iota : U \hookrightarrow M$ is the inclusion, then $\iota^{\ast}\eta = \eta|_U$ for a form $\eta$ on $M$; and if $F(U) \subseteq V$ with $V \subseteq N$ open, then $(F^{\ast}\eta')|_U = (F|_U)^{\ast}(\eta'|_V)$ for a form $\eta'$ on $N$, where $F|_U : U \to V$.
>
> *Source: not from lecture · filled in*
>
> *Lee: Proposition 12.25(e),(f) (for covariant tensors)*

^lem-81-4

> [!proof]+ Proof
> (1) For linear maps $T : V_1 \to V_2$ and $S : V_2 \to V_3$, $(S \circ T)^{\ast} = T^{\ast} \circ S^{\ast}$ on $\Lambda^k V_3^{\ast}$, since both send $\beta$ to $(v^1, \ldots, v^k) \mapsto \beta(STv^1, \ldots, STv^k)$ (Definition [[§79 Pullbacks of Linear Forms#^def-79-1|§79.1]]). By the chain rule (Theorem [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]]), $d(G \circ F)_p = dG_{F(p)} \circ dF_p$, so at each $p$, $\big((G \circ F)^{\ast}\omega\big)_p = (dF_p)^{\ast} (dG_{F(p)})^{\ast}\, \omega_{G(F(p))} = \big(F^{\ast}(G^{\ast}\omega)\big)_p$ (Definition [[§80 Differential Forms on Manifolds#^def-80-9|§80.9]]). The differential of the identity is the identity, whose pullback is the identity. (2) follows from (1) applied to $F^{-1} \circ F = \mathrm{id}_M$ and $F \circ F^{-1} = \mathrm{id}_N$. (3) Under the identification $T_pU = T_pM$ by $d\iota_p$ (Lemma [[§28 Derivations and the Abstract Tangent Space#^lem-28-8|§28.8]]), $(\iota^{\ast}\eta)_p = (d\iota_p)^{\ast}\eta_p = \eta_p$. Similarly $d(F|_U)_p = dF_p$, so both sides of the last identity are $(dF_p)^{\ast}\eta'_{F(p)}$ at $p \in U$.

^pf-81-4

*Uses:* [[§79 Pullbacks of Linear Forms#^def-79-1|Def. §79.1]], [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]], [[§80 Differential Forms on Manifolds#^def-80-9|Def. §80.9]], [[§28 Derivations and the Abstract Tangent Space#^lem-28-8|§28.8]]

Let $(U, \varphi)$ be a smooth chart of $M$. The chart is a diffeomorphism $\varphi : U \to \varphi(U)$ onto an open subset of $\mathbb{R}^m$ (Proposition [[§28 Derivations and the Abstract Tangent Space#^prop-28-9|§28.9]]), so $\varphi^{-1} : \varphi(U) \to U$ pulls forms on $U$ back to forms on $\varphi(U) \subseteq \mathbb{R}^m$, where the Euclidean $d$ of Step I is available. So a form on $U$ can be pulled back to Euclidean space, differentiated there, and the result pulled back up: for $\alpha \in \Omega^k(M)$ this gives the $(k+1)$-form $\varphi^{\ast}\, d\, (\varphi^{-1})^{\ast}\alpha$ on $U$, where $(\varphi^{-1})^{\ast}\alpha$ means $(\varphi^{-1})^{\ast}(\alpha|_U)$.

The argument is not circular: the $d$ in the middle is the Euclidean one, constructed in Step I. The lecture took this formula as the definition of $d\alpha$ on $U$ and left as an exercise that it does not depend on the chart. The exercise comes first here, so that the definition is complete when it is stated.

> [!theorem] Lemma §81.5: Independence of the Chart
> Let $(U, \varphi)$ and $(V, \psi)$ be smooth charts of $M$ and $\alpha \in \Omega^k(M)$. On $W = U \cap V$,
>
> $$
> \varphi^{\ast}\, d\, \big(\varphi^{-1}\big)^{\ast}\alpha = \psi^{\ast}\, d\, \big(\psi^{-1}\big)^{\ast}\alpha .
> $$
>
> *Lee: Theorem 14.24, proof*

^lem-81-5

> [!proof]+ Proof
> *(Lecture 32 left this as an exercise in diagram chasing, with the hint to use naturality; filled in.)* Both sides restrict to $W$, and by Proposition [[§81 The Exterior Derivative#^prop-81-3|§81.3]] (restriction) and Lemma [[§81 The Exterior Derivative#^lem-81-4|§81.4]](3), the left side on $W$ is computed with the chart $\varphi|_W : W \to \varphi(W)$ and the right side with $\psi|_W : W \to \psi(W)$. So assume $U = V = W$. The change of coordinates $\tau = \psi \circ \varphi^{-1} : \varphi(W) \to \psi(W)$ is a smooth map between open subsets of $\mathbb{R}^m$ (a diffeomorphism, Definition [[§17 Differentiable Structures#^def-17-4|§17.4]]), with $\psi = \tau \circ \varphi$ and $\varphi^{-1} = \psi^{-1} \circ \tau$. By Lemma [[§81 The Exterior Derivative#^lem-81-4|§81.4]](1), then naturality of the Euclidean $d$ (Proposition [[§81 The Exterior Derivative#^prop-81-3|§81.3]](4)) for $\tau$, then Lemma [[§81 The Exterior Derivative#^lem-81-4|§81.4]](1) again,
>
> $$
> \varphi^{\ast}\, d\, (\varphi^{-1})^{\ast}\alpha = \varphi^{\ast}\, d\, \tau^{\ast} (\psi^{-1})^{\ast}\alpha = \varphi^{\ast}\, \tau^{\ast}\, d\, (\psi^{-1})^{\ast}\alpha = (\tau \circ \varphi)^{\ast}\, d\, (\psi^{-1})^{\ast}\alpha = \psi^{\ast}\, d\, (\psi^{-1})^{\ast}\alpha .
> $$

^pf-81-5

*Uses:* [[§81 The Exterior Derivative#^prop-81-3|§81.3]], [[§81 The Exterior Derivative#^lem-81-4|§81.4]], [[§17 Differentiable Structures#^def-17-4|Def. §17.4]]

![[m591-79-2.svg]]

*(Not from lecture; diagram added.)* The proof of Lemma [[§81 The Exterior Derivative#^lem-81-5|§81.5]], with $\tau = \psi \circ \varphi^{-1}$. The top and bottom triangles commute because pullbacks compose ($\varphi^{-1} = \psi^{-1} \circ \tau$ and $\psi = \tau \circ \varphi$), and the middle square is the naturality of the Euclidean $d$ for $\tau$. So the two ways from the top to the bottom, through the left chart and through the right one, agree.

> [!definition] Definition §81.3: Exterior Derivative on a Manifold
> Let $\alpha \in \Omega^k(M)$. For a smooth chart $(U, \varphi)$ of $M$, define $d\alpha$ on $U$ by
>
> $$
> d\alpha\big|_U = \varphi^{\ast}\, d\, \big(\varphi^{-1}\big)^{\ast} \alpha ,
> $$
>
> where $(\varphi^{-1})^{\ast}\alpha$ means $(\varphi^{-1})^{\ast}(\alpha|_U) \in \Omega^k(\varphi(U))$ (Proposition [[§80 Differential Forms on Manifolds#^prop-80-5|§80.5]](5)), $d$ is the Euclidean exterior derivative of Definition [[§81 The Exterior Derivative#^def-81-2|§81.2]] on the open set $\varphi(U) \subseteq \mathbb{R}^m$, and $\varphi^{\ast}$ pulls the resulting $(k+1)$-form back to $U$. By Lemma [[§81 The Exterior Derivative#^lem-81-5|§81.5]], the forms so defined for different charts agree where their domains overlap, so they define a form $d\alpha$ on all of $M$; it is smooth, since it is smooth on each chart domain.
>
> *Lee: Theorem 14.24, proof*

^def-81-3

![[m591-79-3.svg]]

![[m591-79-4.svg]]

*(Not from lecture; diagram added.)* Definition [[§81 The Exterior Derivative#^def-81-3|§81.3]]. Above, the chart, as drawn on the board. Below, the dashed arrow $d$ on $U$ is defined to make the square commute: across to Euclidean space by $(\varphi^{-1})^{\ast}$, down by the Euclidean $d$, and back by $\varphi^{\ast}$. Since $\varphi^{\ast}$ and $(\varphi^{-1})^{\ast}$ are inverse bijections (Lemma [[§81 The Exterior Derivative#^lem-81-4|§81.4]](2)), the square then commutes in both directions, $(\varphi^{-1})^{\ast}\, d\alpha|_U = d\, (\varphi^{-1})^{\ast}\alpha$: naturality for the diffeomorphism $\varphi^{-1}$ holds by construction.

> [!theorem] Corollary §81.6: The Exterior Derivative in Coordinates
> Let $(U, \varphi = (x^1, \ldots, x^m))$ be a smooth chart and $\alpha = \sum_A f_A\, dx^A$ on $U$. Then, on $U$,
>
> $$
> d\alpha = \sum_A df_A \wedge dx^A = \sum_A \sum_{j=1}^m \frac{\partial f_A}{\partial x^j}\; dx^j \wedge dx^A ,
> $$
>
> the same formula as in Definition [[§81 The Exterior Derivative#^def-81-2|§81.2]], now with the coordinates of the chart.
>
> *Source: not from lecture · filled in*
>
> *Lee: Theorem 14.24 and (14.19)*

^cor-81-6

> [!proof]+ Proof
> Let $r^1, \ldots, r^m$ be the standard coordinates of $\mathbb{R}^m$, so $x^i = r^i \circ \varphi$ and $r^i = x^i \circ \varphi^{-1}$. By Proposition [[§80 Differential Forms on Manifolds#^prop-80-5|§80.5]](2),(3), $(\varphi^{-1})^{\ast}(dx^i) = d(x^i \circ \varphi^{-1}) = dr^i$ and $\varphi^{\ast}(dr^i) = dx^i$, so $(\varphi^{-1})^{\ast}\alpha = \sum_A (f_A \circ \varphi^{-1})\, dr^A$. The Euclidean $d$ gives $\sum_A d(f_A \circ \varphi^{-1}) \wedge dr^A$, and pulling back by $\varphi$, with $\varphi^{\ast}\, d(f_A \circ \varphi^{-1}) = d(f_A \circ \varphi^{-1} \circ \varphi) = df_A$, gives $\sum_A df_A \wedge dx^A$. The second form is Lemma [[§33 Covectors in Coordinates#^lem-33-1|§33.1]].

^pf-81-6

*Uses:* [[§80 Differential Forms on Manifolds#^prop-80-5|§80.5]], [[§33 Covectors in Coordinates#^lem-33-1|§33.1]]

> [!theorem] Theorem §81.7: The Exterior Derivative
> There is exactly one family of linear operators $d : \Omega^k(M) \to \Omega^{k+1}(M)$, for all smooth manifolds $M$ and all $k \ge 0$, with the four properties of Definition [[§81 The Exterior Derivative#^def-81-1|§81.1]]:
>
> 1. on $\Omega^0(M) = C^\infty(M)$, $d$ is the differential of functions;
> 2. $d(\alpha \wedge \beta) = d\alpha \wedge \beta + (-1)^{|\alpha|}\, \alpha \wedge d\beta$;
> 3. $d \circ d = 0$;
> 4. $F^{\ast}(d\beta) = d(F^{\ast}\beta)$ for every smooth map $F : M \to N$ and every $\beta \in \Omega^k(N)$.
>
> It is the operator of Definition [[§81 The Exterior Derivative#^def-81-3|§81.3]], the **exterior derivative**: in any smooth chart $(U, (x^i))$, $d\big(\sum_A f_A\, dx^A\big) = \sum_A df_A \wedge dx^A$ (Corollary [[§81 The Exterior Derivative#^cor-81-6|§81.6]]).
>
> *Lee: Theorem 14.24; Proposition 14.26*

^thm-81-7

> [!proof]+ Proof
> *(Lecture 32 stated Step II and left the details; filled in.)* *Existence.* Define $d$ on $M$ by Definition [[§81 The Exterior Derivative#^def-81-3|§81.3]]; it is linear, because each $\varphi^{\ast}$, $(\varphi^{-1})^{\ast}$ and the Euclidean $d$ are. All four properties can be checked on the domain $U$ of a chart $\varphi$, since such domains cover $M$; write $\alpha' = (\varphi^{-1})^{\ast}\alpha$ and $\beta' = (\varphi^{-1})^{\ast}\beta$, so that $\alpha|_U = \varphi^{\ast}\alpha'$, $\beta|_U = \varphi^{\ast}\beta'$, $d\alpha|_U = \varphi^{\ast} d\alpha'$ and $d\beta|_U = \varphi^{\ast} d\beta'$ (Lemma [[§81 The Exterior Derivative#^lem-81-4|§81.4]](2)).
>
> 1. For $f \in C^\infty(M)$, $df|_U = \varphi^{\ast}\, d(f \circ \varphi^{-1}) = d\big(f \circ \varphi^{-1} \circ \varphi\big) = d(f|_U)$, by Proposition [[§81 The Exterior Derivative#^prop-81-3|§81.3]](1) and Corollary [[§53 One-Forms#^cor-53-5|§53.5]]: the differential of $f$ on $U$.
> 2. The pullback preserves wedge products, so $(\varphi^{-1})^{\ast}(\alpha \wedge \beta) = \alpha' \wedge \beta'$, and by the Euclidean product rule,
>
> $$
> d(\alpha \wedge \beta)|_U = \varphi^{\ast}\big( d\alpha' \wedge \beta' + (-1)^k \alpha' \wedge d\beta' \big) = d\alpha \wedge \beta + (-1)^k\, \alpha \wedge d\beta \quad \text{on } U .
> $$
>
> 3. $(\varphi^{-1})^{\ast}(d\alpha|_U) = d\alpha'$, so $d(d\alpha)|_U = \varphi^{\ast}\, d(d\alpha') = 0$ by the Euclidean (3).
> 4. Let $F : M \to N$ and $p \in M$. By Lemma [[§19 Smooth Functions and Smooth Maps#^lem-19-3|§19.3]] there are charts $(U, \varphi)$ at $p$ and $(V, \psi)$ at $F(p)$ with $F(U) \subseteq V$; let $\hat F = \psi \circ F \circ \varphi^{-1} : \varphi(U) \to \psi(V)$, a smooth map between open subsets of Euclidean spaces, so that $F|_U = \psi^{-1} \circ \hat F \circ \varphi$. On $U$, by Lemma [[§81 The Exterior Derivative#^lem-81-4|§81.4]] and the Euclidean naturality for $\hat F$,
>
> $$
> \begin{aligned}
> d(F^{\ast}\beta)|_U &= \varphi^{\ast}\, d\, (\varphi^{-1})^{\ast} \varphi^{\ast}\, \hat F^{\ast}\, (\psi^{-1})^{\ast}\beta = \varphi^{\ast}\, d\, \hat F^{\ast}\, (\psi^{-1})^{\ast}\beta \\
> &= \varphi^{\ast}\, \hat F^{\ast}\, d\, (\psi^{-1})^{\ast}\beta = F^{\ast}\, \psi^{\ast}\, d\, (\psi^{-1})^{\ast}\beta = F^{\ast}(d\beta)|_U .
> \end{aligned}
> $$
>
> *Uniqueness.* Suppose operators $d'$ on all smooth manifolds satisfy (1)–(4). On an open subset of $\mathbb{R}^m$, the computation before Definition [[§81 The Exterior Derivative#^def-81-2|§81.2]] used only linearity and (1)–(3), so $d'$ is the Euclidean $d$. On $M$, let $(U, \varphi)$ be a chart and $\iota : U \hookrightarrow M$ the inclusion. Naturality (4) for $\iota$ gives $(d'\alpha)|_U = \iota^{\ast}(d'\alpha) = d'(\iota^{\ast}\alpha) = d'(\alpha|_U)$: $d'$ is local. Naturality for the smooth map $\varphi : U \to \varphi(U)$, applied to $(\varphi^{-1})^{\ast}\alpha$, gives
>
> $$
> d'\big(\alpha|_U\big) = d'\big(\varphi^{\ast}\, (\varphi^{-1})^{\ast}\alpha\big) = \varphi^{\ast}\, d'\big((\varphi^{-1})^{\ast}\alpha\big) = \varphi^{\ast}\, d\, (\varphi^{-1})^{\ast}\alpha = d\alpha|_U ,
> $$
>
> the third step because $d'$ is the Euclidean $d$ on $\varphi(U)$. As the chart domains cover $M$, $d' = d$. The formula in coordinates is Corollary [[§81 The Exterior Derivative#^cor-81-6|§81.6]].

^pf-81-7

*Uses:* [[§81 The Exterior Derivative#^def-81-3|Def. §81.3]], [[§81 The Exterior Derivative#^lem-81-4|§81.4]], [[§81 The Exterior Derivative#^prop-81-3|§81.3]], [[§53 One-Forms#^cor-53-5|§53.5]], [[§19 Smooth Functions and Smooth Maps#^lem-19-3|§19.3]], [[§81 The Exterior Derivative#^def-81-2|Def. §81.2]], [[§81 The Exterior Derivative#^cor-81-6|§81.6]]

*Not from lecture: the exterior derivative on $\mathbb{R}^3$.* The lecture announced that on $\mathbb{R}^3$ the second and third arrows of the sequence are the curl and the divergence; with Corollary [[§81 The Exterior Derivative#^cor-81-6|§81.6]] this is a computation. Subscripts denote partial derivatives, $P_y = \partial P/\partial y$.

> [!example] Example §81.1: The Exterior Derivative on $\mathbb{R}^3$
> On an open set of $\mathbb{R}^3$ with coordinates $x, y, z$:
>
> 1. $df = f_x\, dx + f_y\, dy + f_z\, dz$: the components are those of the gradient of $f$.
> 2. For $\theta = P\, dx + Q\, dy + R\, dz$,
>
> $$
> d\theta = (R_y - Q_z)\; dy \wedge dz + (P_z - R_x)\; dz \wedge dx + (Q_x - P_y)\; dx \wedge dy ,
> $$
>
> whose components are those of the curl of $(P, Q, R)$.
>
> 3. For $\eta = A\, dy \wedge dz + B\, dz \wedge dx + C\, dx \wedge dy$,
>
> $$
> d\eta = (A_x + B_y + C_z)\; dx \wedge dy \wedge dz ,
> $$
>
> whose coefficient is the divergence of $(A, B, C)$.
>
> *Source: not from lecture · filled in*
>
> *Lee: Example 14.27*

^ex-81-1

> [!remark]- Connections
> - Gradient, curl and divergence as $d$ on $0$-, $1$- and $2$-forms in MATH 452: [[§38 The Exterior Derivative#^prop-38-1|452 Prop. §38.1]], [[§38 The Exterior Derivative#^prop-38-2|452 Prop. §38.2]], [[§38 The Exterior Derivative#^prop-38-3|452 Prop. §38.3]].
> - The two-form of a vector field in $\mathbb{R}^3$, with the basis $dy \wedge dz$, $dz \wedge dx$, $dx \wedge dy$: [[§74 The Integrand Is a Two-Form|§74]].
> - Stokes' theorem in $\mathbb{R}^3$, which $d$ is built to generalize: [[§73 Stokes' Theorem in Calculus III|§73]].

> [!proof]+ Computation
> (1) is Lemma [[§33 Covectors in Coordinates#^lem-33-1|§33.1]]. (2) $d\theta = dP \wedge dx + dQ \wedge dy + dR \wedge dz$, and in $dP \wedge dx = P_y\, dy \wedge dx + P_z\, dz \wedge dx$ the term with $dx \wedge dx$ is $0$; collecting, with $dy \wedge dx = -\,dx \wedge dy$ and $dz \wedge dy = -\,dy \wedge dz$, gives the formula. (3) In $dA \wedge dy \wedge dz$ only $A_x\, dx \wedge dy \wedge dz$ survives; $dB \wedge dz \wedge dx$ leaves $B_y\, dy \wedge dz \wedge dx = B_y\, dx \wedge dy \wedge dz$ (a cyclic permutation of three one-forms is even: two exchanges); likewise $C_z\, dz \wedge dx \wedge dy = C_z\, dx \wedge dy \wedge dz$.

^pf-ex-81-1

*Uses:* [[§33 Covectors in Coordinates#^lem-33-1|§33.1]]

The basis $dy \wedge dz$, $dz \wedge dx$, $dx \wedge dy$ is used here (with $dz \wedge dx = -\,dx \wedge dz$, out of increasing order) because it matches the components of a vector field, as in [[§74 The Integrand Is a Two-Form|§74]]. In this dictionary $d \circ d = 0$ becomes $\operatorname{curl} \operatorname{grad} = 0$ and $\operatorname{div} \operatorname{curl} = 0$. For one-forms, $d\theta = 0$ is the condition $\partial\theta_j/\partial x^k = \partial\theta_k/\partial x^j$ of Definition [[§53 One-Forms#^def-53-5|§53.5]]: by Corollary [[§81 The Exterior Derivative#^cor-81-6|§81.6]] and the computation in the proof of Proposition [[§81 The Exterior Derivative#^prop-81-3|§81.3]](3), $d\theta = \sum_{j < k} \big( \partial\theta_k/\partial x^j - \partial\theta_j/\partial x^k \big)\, dx^j \wedge dx^k$ in every chart.

## Assignment 9, Problem 3: The Tautological One-Form

*From Assignment 9, Problem 3 (submitted). The cotangent bundle carries a one-form defined without any choice, the Liouville form; its exterior derivative makes $T^{\ast}M$ a symplectic manifold. The assignment's reading is Tu, *An Introduction to Manifolds*, Example 17.4. The submitted solution is given in the notation of these notes: $(\bar x^1, \ldots, \bar x^m, \xi_1, \ldots, \xi_m)$ are the standard coordinates on $T^{\ast}U$ (Definition [[§52 The Cotangent Bundle#^def-52-5|§52.5]]), with $\bar x^i = x^i \circ \pi$ and $\xi_i(p, \xi) = \xi(\partial/\partial x^i|_p)$. The steps that are general statements are stated as lemmas.*

Throughout, $M$ is a smooth manifold of dimension $m$ and $\pi : T^{\ast}M \to M$, $\pi(p, \xi) = p$, is the projection.

> [!definition] Definition §81.4: The Tautological One-Form
> A point $(p, \xi)$ of $T^{\ast}M$ is itself a covector $\xi \in T_p^{\ast}M$. The **tautological one-form**, or **Liouville form**, $\lambda$ on $T^{\ast}M$ is defined at this point as the pullback of $\xi$ by the differential of $\pi$:
>
> $$
> \lambda_{(p, \xi)}(X) = \xi\big( \pi_{\ast(p, \xi)} X \big) \qquad \text{for } X \in T_{(p, \xi)}(T^{\ast}M) .
> $$
>
> *Source: Assignment 9, Problem 3 · Tu, Example 17.4*

^def-81-4

> [!remark]- Connections
> - The standard coordinates $(\bar x^i, \xi_j)$ on $T^{\ast}M$: [[§52 The Cotangent Bundle#^def-52-5|Def. §52.5]]; the one-form $df$ as a map into $T^{\ast}M$, and its differential: [[§55 Morse Functions and the Zero Section#^prop-55-7|Prop. §55.7]].
> - A rough section, smooth once its coefficients are: [[§45 Fibrations#^def-45-5|Def. §45.5]].

Each $\lambda_{(p, \xi)}$ is linear in $X$, so $\lambda$ is a rough section of $T^{\ast}(T^{\ast}M)$ (Definition [[§45 Fibrations#^def-45-5|§45.5]]); it is smooth by Proposition [[§81 The Exterior Derivative#^prop-81-9|§81.9]]. The definition uses no chart.

> [!theorem] Lemma §81.8: The Differential of the Projection in Standard Coordinates
> Let $(U, \varphi = (x^i))$ be a chart of $M$ and $(p, \xi) \in T^{\ast}U$. Then, for $j = 1, \ldots, m$,
>
> $$
> \pi_{\ast(p, \xi)}\Big( \frac{\partial}{\partial \bar x^j}\Big|_{(p, \xi)} \Big) = \frac{\partial}{\partial x^j}\Big|_p, \qquad \pi_{\ast(p, \xi)}\Big( \frac{\partial}{\partial \xi_j}\Big|_{(p, \xi)} \Big) = 0 .
> $$
>
> So the kernel of $\pi_{\ast(p, \xi)}$, the vertical space at $(p, \xi)$ (Definition [[§45 Fibrations#^def-45-6|§45.6]]), is spanned by $\partial/\partial \xi_1, \ldots, \partial/\partial \xi_m$.
> Proposition [[§55 Morse Functions and the Zero Section#^prop-55-6|§55.6]](1) is the case of the points $(p, 0)$.
>
> *Source: Assignment 9, Problem 3(a) · submitted solution*

^lem-81-8

> [!proof]+ Proof
> *(The submitted solution.)* In the standard coordinates on $T^{\ast}U$ and the coordinates $(x^i)$ on $U$, the projection is $(\bar x^1, \ldots, \bar x^m, \xi_1, \ldots, \xi_m) \mapsto (\bar x^1, \ldots, \bar x^m)$ (Corollary [[§52 The Cotangent Bundle#^cor-52-3|§52.3]](1)), whose Jacobian is the $m \times 2m$ matrix $\begin{pmatrix} I_m & 0 \end{pmatrix}$. Reading off its columns (Theorem [[§30 The Differential in Coordinates#^thm-30-2|§30.2]]) gives the two formulas. The kernel of a matrix $\begin{pmatrix} I_m & 0 \end{pmatrix}$ consists of the vectors whose first $m$ components vanish.

^pf-81-8

*Uses:* [[§52 The Cotangent Bundle#^cor-52-3|§52.3]], [[§30 The Differential in Coordinates#^thm-30-2|§30.2]]

> [!theorem] Proposition §81.9: The Tautological One-Form in Coordinates
> Let $(U, (x^i))$ be a chart of $M$. In the standard coordinates on $T^{\ast}U$,
>
> $$
> \lambda = \sum_{i=1}^m \xi_i\, d\bar x^i .
> $$
>
> In particular:
>
> 1. $\lambda$ is smooth, $\lambda \in \Omega^1(T^{\ast}M)$;
> 2. $\lambda$ vanishes on vertical vectors: $\lambda_{(p, \xi)}(X) = 0$ if $\pi_{\ast(p, \xi)} X = 0$;
> 3. the expression $\sum_i \xi_i\, d\bar x^i$ is the same one-form on $T^{\ast}(U \cap U')$ for any two charts $(U, (x^i))$ and $(U', (x'^i))$ of $M$.
>
> *Source: Assignment 9, Problem 3(a)*

^prop-81-9

> [!proof]+ Proof
> *(The submitted solution; the consequences (1)–(3) are filled in.)* Fix $(p, \xi) \in T^{\ast}U$.
>
> *$\lambda$ on $\partial/\partial \bar x^j$.* For $j = 1, \ldots, m$, by Definition [[§81 The Exterior Derivative#^def-81-4|§81.4]], then Lemma [[§81 The Exterior Derivative#^lem-81-8|§81.8]], then the definition of the coordinate $\xi_j$ (Definition [[§52 The Cotangent Bundle#^def-52-5|§52.5]]),
>
> $$
> \lambda_{(p, \xi)}\Big( \frac{\partial}{\partial \bar x^j}\Big|_{(p, \xi)} \Big) = \xi\Big( \pi_{\ast(p, \xi)}\Big( \frac{\partial}{\partial \bar x^j}\Big|_{(p, \xi)} \Big) \Big) = \xi\Big( \frac{\partial}{\partial x^j}\Big|_p \Big) = \xi_j(p, \xi) .
> $$
>
> *$\lambda$ on $\partial/\partial \xi_j$.* By Definition [[§81 The Exterior Derivative#^def-81-4|§81.4]] and Lemma [[§81 The Exterior Derivative#^lem-81-8|§81.8]], and since $\xi$ is linear,
>
> $$
> \lambda_{(p, \xi)}\Big( \frac{\partial}{\partial \xi_j}\Big|_{(p, \xi)} \Big) = \xi\Big( \pi_{\ast(p, \xi)}\Big( \frac{\partial}{\partial \xi_j}\Big|_{(p, \xi)} \Big) \Big) = \xi(0) = 0 .
> $$
>
> *Conclusion.* A covector is the sum of its values on the coordinate vectors times the dual basis (Corollary [[§33 Covectors in Coordinates#^cor-33-2|§33.2]], on the manifold $T^{\ast}U$ with the coordinates $(\bar x^i, \xi_j)$), so
>
> $$
> \lambda_{(p, \xi)} = \sum_{j=1}^m \lambda_{(p, \xi)}\Big( \frac{\partial}{\partial \bar x^j} \Big)\, d\bar x^j\big|_{(p, \xi)} + \sum_{j=1}^m \lambda_{(p, \xi)}\Big( \frac{\partial}{\partial \xi_j} \Big)\, d\xi_j\big|_{(p, \xi)} = \sum_{j=1}^m \xi_j(p, \xi)\, d\bar x^j\big|_{(p, \xi)} .
> $$
>
> Since $(p, \xi) \in T^{\ast}U$ was arbitrary, $\lambda = \sum_i \xi_i\, d\bar x^i$ on $T^{\ast}U$.
>
> *(1)* The coefficient functions of $\lambda$ in the chart are the coordinate functions $\xi_i$ and the constant $0$, which are smooth; the domains $T^{\ast}U$ cover $T^{\ast}M$, so $\lambda$ is smooth (Proposition [[§53 One-Forms#^prop-53-1|§53.1]](3)). *(2)* Immediate from Definition [[§81 The Exterior Derivative#^def-81-4|§81.4]]: if $\pi_\ast X = 0$ then $\lambda(X) = \xi(0) = 0$. *(3)* Both expressions equal $\lambda$, which was defined without a chart.

^pf-81-9

*Uses:* [[§81 The Exterior Derivative#^def-81-4|Def. §81.4]], [[§81 The Exterior Derivative#^lem-81-8|§81.8]], [[§52 The Cotangent Bundle#^def-52-5|Def. §52.5]], [[§33 Covectors in Coordinates#^cor-33-2|§33.2]], [[§53 One-Forms#^prop-53-1|§53.1]]

> [!theorem] Proposition §81.10: Every One-Form Is a Pullback of the Tautological One-Form
> Let $\alpha \in \Omega^1(M)$, and let $s_\alpha : M \to T^{\ast}M$, $s_\alpha(p) = (p, \alpha_p)$, be the corresponding section: the one-form $\alpha$ regarded as a map (Definition [[§53 One-Forms#^def-53-1|§53.1]]). Then
>
> $$
> s_\alpha^{\ast}\lambda = \alpha ,
> $$
>
> hence the name *tautological*.
>
> *Source: Assignment 9, Problem 3(b)*

^prop-81-10

> [!proof]+ Proof
> *(Assignment 9, Problem 3(b), as submitted: the proof in coordinates.)* Both $s_\alpha^{\ast}\lambda$ and $\alpha$ are one-forms on $M$. Let $(U, (x^i))$ be a chart of $M$ and write $\alpha = \sum_i a_i\, dx^i$ on $U$, with $a_i = \alpha(\partial/\partial x^i) \in C^\infty(U)$. In the standard coordinates on $T^{\ast}U$,
>
> $$
> s_\alpha(x^1, \ldots, x^m) = \big( x^1, \ldots, x^m, a_1(x), \ldots, a_m(x) \big) ,
> $$
>
> since $\xi_i(p, \alpha_p) = \alpha_p(\partial/\partial x^i|_p) = a_i(p)$ (Proposition [[§53 One-Forms#^prop-53-1|§53.1]](2)). Fix $p \in U$ and $v = \sum_j v^j\, \partial/\partial x^j|_p \in T_pM$.
>
> *The pullback.* By Definition [[§53 One-Forms#^def-53-8|§53.8]], $(s_\alpha^{\ast}\lambda)_p(v) = \lambda_{s_\alpha(p)}\big( (s_\alpha)_{\ast p} v \big)$. Since $\pi(s_\alpha(p)) = p \in U$, the point $s_\alpha(p)$ lies in $T^{\ast}U$, and by Proposition [[§81 The Exterior Derivative#^prop-81-9|§81.9]]
>
> $$
> (s_\alpha^{\ast}\lambda)_p(v) = \sum_{i=1}^m \xi_i\big(s_\alpha(p)\big)\; d\bar x^i\big|_{s_\alpha(p)}\big( (s_\alpha)_{\ast p} v \big) .
> $$
>
> *The coefficients.* $\xi_i(s_\alpha(p)) = \xi_i(p, \alpha_p) = a_i(p)$.
>
> *The factors.* By the coordinate expression of $s_\alpha$ and the matrix of the differential (Theorem [[§30 The Differential in Coordinates#^thm-30-2|§30.2]]),
>
> $$
> (s_\alpha)_{\ast p} v = \sum_{j=1}^m v^j\, \frac{\partial}{\partial \bar x^j}\Big|_{s_\alpha(p)} + \sum_{i=1}^m \Big( \sum_{j=1}^m \frac{\partial a_i}{\partial x^j}(p)\, v^j \Big) \frac{\partial}{\partial \xi_i}\Big|_{s_\alpha(p)} .
> $$
>
> The covector $d\bar x^i|_{s_\alpha(p)}$ returns the coefficient of $\partial/\partial \bar x^i$, so the $\xi$-part does not contribute, and $d\bar x^i|_{s_\alpha(p)}\big( (s_\alpha)_{\ast p} v \big) = v^i$.
>
> *Conclusion.* Substituting, $(s_\alpha^{\ast}\lambda)_p(v) = \sum_i a_i(p)\, v^i = \sum_i a_i(p)\, dx^i|_p(v) = \alpha_p(v)$. Since $p \in U$ and $v \in T_pM$ were arbitrary, $s_\alpha^{\ast}\lambda = \alpha$ on $U$; the chart domains cover $M$.

^pf-81-10

*Uses:* [[§53 One-Forms#^prop-53-1|§53.1]], [[§53 One-Forms#^def-53-8|Def. §53.8]], [[§81 The Exterior Derivative#^prop-81-9|§81.9]], [[§30 The Differential in Coordinates#^thm-30-2|§30.2]]

> [!proof]+ Second proof
> *(Assignment 9, Problem 3(b), as submitted: the alternative without coordinates.)* For $p \in M$ and $v \in T_pM$, since $s_\alpha(p) = (p, \alpha_p)$, Definition [[§81 The Exterior Derivative#^def-81-4|§81.4]] at this point gives $\lambda_{s_\alpha(p)}(X) = \alpha_p(\pi_\ast X)$ for $X \in T_{s_\alpha(p)}(T^{\ast}M)$. Hence, by the chain rule (Theorem [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]]) and $\pi \circ s_\alpha = \mathrm{id}_M$,
>
> $$
> (s_\alpha^{\ast}\lambda)_p(v) = \lambda_{s_\alpha(p)}\big( (s_\alpha)_{\ast p} v \big) = \alpha_p\big( \pi_\ast (s_\alpha)_{\ast p} v \big) = \alpha_p\big( (\pi \circ s_\alpha)_{\ast p} v \big) = \alpha_p(v) .
> $$

^pf-81-10-2

*Uses:* [[§81 The Exterior Derivative#^def-81-4|Def. §81.4]], [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]]

The second proof uses only two facts about $s_\alpha$: $\pi \circ s_\alpha = \mathrm{id}_M$, and that the point $s_\alpha(p)$, as a covector, is $\alpha_p$. The first proof shows in addition how the derivatives $\partial a_i/\partial x^j$ of the coefficients enter $(s_\alpha)_{\ast p}$ and drop out, because $\lambda$ vanishes on vertical vectors (Proposition [[§81 The Exterior Derivative#^prop-81-9|§81.9]](2)). For $\alpha = df$ the matrix $(\partial a_i/\partial x^j)$ is the Hessian matrix of Proposition [[§55 Morse Functions and the Zero Section#^prop-55-7|§55.7]](2).

> [!definition] Definition §81.5: Non-Degenerate Bilinear Form
> A bilinear form $B : W \times W \to \mathbb{R}$ on a finite-dimensional real vector space $W$ is **non-degenerate** if the only $X \in W$ with $B(X, Y) = 0$ for all $Y \in W$ is $X = 0$.
>
> *Source: Assignment 9, Problem 3(c) · Wikipedia*

^def-81-5

> [!theorem] Lemma §81.11: Non-Degeneracy and the Matrix of a Bilinear Form
> Let $(e_1, \ldots, e_N)$ be a basis of $W$ and $J$ the matrix of $B$, $J_{ij} = B(e_i, e_j)$. Then $B$ is non-degenerate if and only if $J$ is invertible.
>
> *Source: Assignment 9, Problem 3(c) · submitted solution*

^lem-81-11

> [!proof]+ Proof
> *(The submitted solution, which uses the implication from right to left; the converse is filled in.)* Write $X = \sum_i X^i e_i$ and $Y = \sum_j Y^j e_j$, and let $X, Y$ also denote the column vectors of components. By bilinearity, $B(X, Y) = \sum_{i, j} X^i J_{ij} Y^j = X^{\mathsf T} J\, Y$. So $B(X, Y) = 0$ for all $Y$ means that the row vector $X^{\mathsf T} J$ is zero, that is, $J^{\mathsf T} X = 0$. Hence $B$ is non-degenerate if and only if $J^{\mathsf T}$ has trivial kernel, if and only if $J^{\mathsf T}$ is invertible, if and only if $J$ is invertible (a square matrix is invertible exactly when its transpose is).

^pf-81-11

> [!definition] Definition §81.6: Symplectic Form
> A **symplectic form** on a manifold $X$ is a two-form $\omega \in \Omega^2(X)$ such that
>
> 1. at each $x \in X$, $\omega_x$ is a non-degenerate bilinear form on $T_xX$ (Definition [[§81 The Exterior Derivative#^def-81-5|§81.5]]), and
> 2. $d\omega = 0$.
>
> A *symplectic manifold* is a pair $(X, \omega)$ of a manifold and a symplectic form on it.
>
> *Source: Assignment 9, Problem 3(c)*

^def-81-6

> [!theorem] Theorem §81.12: The Cotangent Bundle Is a Symplectic Manifold
> Let $\omega = d\lambda \in \Omega^2(T^{\ast}M)$. In the standard coordinates on $T^{\ast}U$,
>
> $$
> \omega = \sum_{i=1}^m d\xi_i \wedge d\bar x^i ,
> $$
>
> and $\omega$ is a symplectic form on $T^{\ast}M$. In the basis $\partial/\partial \bar x^1, \ldots, \partial/\partial \bar x^m, \partial/\partial \xi_1, \ldots, \partial/\partial \xi_m$ of a tangent space of $T^{\ast}U$, the matrix of $\omega$ is $J = \begin{pmatrix} 0 & -I_m \\ I_m & 0 \end{pmatrix}$.
>
> *Source: Assignment 9, Problem 3(c)*

^thm-81-12

> [!remark]- Connections
> - Flows that preserve a symplectic form: [[§85 Lie Derivatives of Forms#^rem-85-2|Rem. Hamiltonian Flows (§85)]], with [[§85 Lie Derivatives of Forms#^cor-85-5|Cor. §85.5]].

> [!proof]+ Proof
> *(Assignment 9, Problem 3(c), as submitted.)* *$\omega$ in coordinates.* By Proposition [[§81 The Exterior Derivative#^prop-81-9|§81.9]], $\lambda = \sum_i \xi_i\, d\bar x^i$ on $T^{\ast}U$, and by Corollary [[§81 The Exterior Derivative#^cor-81-6|§81.6]], $d\big(\sum_i f_i\, d\bar x^i\big) = \sum_i df_i \wedge d\bar x^i$. Here $f_i = \xi_i$ is a coordinate function, so $df_i = d\xi_i$, and $\omega = d\lambda = \sum_i d\xi_i \wedge d\bar x^i$ on $T^{\ast}U$.
>
> *Non-degeneracy.* Let $\mathbf{x} \in T^{\ast}M$, and choose a chart $(U, (x^i))$ of $M$ with $\pi(\mathbf{x}) \in U$, so that $\mathbf{x} \in T^{\ast}U$. By Lemma [[§78 Properties of the Wedge Product#^lem-78-2|§78.2]] with $k = 2$ (Problem 1(a)), $(d\xi_i \wedge d\bar x^i)(X, Y) = d\xi_i(X)\, d\bar x^i(Y) - d\xi_i(Y)\, d\bar x^i(X)$. Write $\partial_{\bar x^j}$ and $\partial_{\xi_j}$ for the coordinate vectors at $\mathbf{x}$. The coordinate covectors act by
>
> $$
> d\bar x^i(\partial_{\bar x^j}) = \delta^i_j, \qquad d\bar x^i(\partial_{\xi_j}) = 0, \qquad d\xi_i(\partial_{\bar x^j}) = 0, \qquad d\xi_i(\partial_{\xi_j}) = \delta_{ij} .
> $$
>
> Hence, for $j, k = 1, \ldots, m$,
>
> $$
> \begin{aligned}\omega_{\mathbf{x}}(\partial_{\bar x^j}, \partial_{\bar x^k}) &= \sum_{i=1}^m \big[ d\xi_i(\partial_{\bar x^j})\, d\bar x^i(\partial_{\bar x^k}) - d\xi_i(\partial_{\bar x^k})\, d\bar x^i(\partial_{\bar x^j}) \big] = 0 , \\
> \omega_{\mathbf{x}}(\partial_{\xi_j}, \partial_{\xi_k}) &= \sum_{i=1}^m \big[ d\xi_i(\partial_{\xi_j})\, d\bar x^i(\partial_{\xi_k}) - d\xi_i(\partial_{\xi_k})\, d\bar x^i(\partial_{\xi_j}) \big] = 0 , \\
> \omega_{\mathbf{x}}(\partial_{\bar x^j}, \partial_{\xi_k}) &= \sum_{i=1}^m \big[ d\xi_i(\partial_{\bar x^j})\, d\bar x^i(\partial_{\xi_k}) - d\xi_i(\partial_{\xi_k})\, d\bar x^i(\partial_{\bar x^j}) \big] = -\sum_{i=1}^m \delta_{ik}\, \delta^i_j = -\delta_{jk} ,\end{aligned}
> $$
>
> and, by antisymmetry, $\omega_{\mathbf{x}}(\partial_{\xi_j}, \partial_{\bar x^k}) = \delta_{jk}$. So the matrix of $\omega_{\mathbf{x}}$ in this basis is, in $m \times m$ blocks, $J = \begin{pmatrix} 0 & -I_m \\ I_m & 0 \end{pmatrix}$. By block multiplication $J^2 = -I_{2m}$, so $J$ is invertible, with $J^{-1} = -J$. By Lemma [[§81 The Exterior Derivative#^lem-81-11|§81.11]], $\omega_{\mathbf{x}}$ is non-degenerate. Since $\mathbf{x}$ was arbitrary, this holds at every point of $T^{\ast}M$.
>
> *$d\omega = 0$.* Since $\omega = d\lambda$ and $d \circ d = 0$ (Theorem [[§81 The Exterior Derivative#^thm-81-7|§81.7]](3)), $d\omega = d(d\lambda) = 0$.

^pf-81-12

*Uses:* [[§81 The Exterior Derivative#^prop-81-9|§81.9]], [[§81 The Exterior Derivative#^cor-81-6|§81.6]], [[§78 Properties of the Wedge Product#^lem-78-2|§78.2]], [[§81 The Exterior Derivative#^lem-81-11|§81.11]], [[§81 The Exterior Derivative#^thm-81-7|§81.7]]

> [!theorem] Corollary §81.13: The Symplectic Form Pulled Back by a One-Form
> For $\alpha \in \Omega^1(M)$, $s_\alpha^{\ast}\omega = d\alpha$. So $s_\alpha^{\ast}\omega = 0$ if and only if $\alpha$ is closed; in particular $s_{df}^{\ast}\omega = 0$ for every $f \in C^\infty(M)$.
>
> *Source: not from the assignment*

^cor-81-13

> [!proof]+ Proof
> *(Not from the assignment; Problems 3(b) and 3(c) combined.)* By naturality of $d$ (Theorem [[§81 The Exterior Derivative#^thm-81-7|§81.7]](4)) and Proposition [[§81 The Exterior Derivative#^prop-81-10|§81.10]], $s_\alpha^{\ast}\omega = s_\alpha^{\ast}(d\lambda) = d(s_\alpha^{\ast}\lambda) = d\alpha$. For $\alpha = df$, $d(df) = 0$.

^pf-81-13

*Uses:* [[§81 The Exterior Derivative#^thm-81-7|§81.7]], [[§81 The Exterior Derivative#^prop-81-10|§81.10]]

The section $s_{df}$ is the map $s_f$ of [[§55 Morse Functions and the Zero Section|§55]], whose intersection with the zero section gives the critical points of $f$. The flows that preserve $\omega$ are the subject of the remark *Hamiltonian Flows* in [[§85 Lie Derivatives of Forms|§85]].
