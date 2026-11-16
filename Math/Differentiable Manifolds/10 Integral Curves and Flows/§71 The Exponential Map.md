---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 10
section: 71
tags: [differentiable-manifolds, math591]
---
← [[§70 Complete Vector Fields]] · ↑ [[· 10 Integral Curves and Flows]] · [[§72 Lie Derivatives]] →

*Stage: Lie groups — The integral curve of a left-invariant field through the identity is a one-parameter subgroup; following it to time $1$ defines $\exp : \mathfrak{g} \to G$, the matrix exponential for linear groups, smooth and a local diffeomorphism at $0$.*

*Lecture 26: the exponential map of Lie groups. Last time: every left-invariant field on $G$ is complete (Theorem [[§70 Complete Vector Fields#^thm-70-11|§70.11]]). The exponential map comes from the integral curve of a left-invariant field $\mathbf{X}$ starting at the identity, which is special.*

*Notation.* The Lie algebra has two incarnations: the left-invariant fields with their bracket, and the tangent space at the identity (Theorem [[§60 Lie Groups and Left-Invariant Vector Fields#^thm-60-9|§60.9]]; the remark [[§61 Lie Group Morphisms and Linear Groups#^rem-61-1|Recap]] ($\mathfrak{g}$ is $T_eG$) in [[§61 Lie Group Morphisms and Linear Groups|§61]]). Capital letters $A, B \in T_eG = \mathfrak{g}$ are vectors at the identity, and

$$
\mathbf{X}^A = \text{the corresponding left-invariant field, with } \mathbf{X}^A_e = A, \qquad \varphi^A = \text{the flow of } \mathbf{X}^A
$$

(Definition [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-5|§60.5]]).
So $\varphi^A_t(e)$ is the integral curve of $\mathbf{X}^A$ starting at $e$, evaluated at $t$; here the superscript is the vector $A$, and the point is in parentheses. $A \mapsto \mathbf{X}^A$ is linear, since $\mathbf{X}^A_g = d(L_g)_e(A)$; in particular $\mathbf{X}^{cA} = c\,\mathbf{X}^A$.

> [!theorem] Proposition §71.1: One-Parameter Subgroups
> Let $\mathbf{X}$ be a left-invariant vector field on a Lie group $G$, with flow $\varphi$. Then for all $s, t \in \mathbb{R}$
>
> $$
> \varphi_{t+s}(e) = \varphi_s(e) \cdot \varphi_t(e),
> $$
>
> the product in $G$. So $t \mapsto \varphi_t(e)$ is a group morphism from the additive group $(\mathbb{R}, +)$ to $G$.
>
> *Lee: Theorem 20.1*

^prop-71-1

> [!proof]+ Proof
> *(Lecture 26.)* $\mathbf{X}$ is complete (Theorem [[§70 Complete Vector Fields#^thm-70-11|§70.11]]), so all these are defined. Fix $s$. $\mathbf{X}$ is $L_{\varphi_s(e)}$-related to itself, because being left-invariant means being $L_g$-related to itself for every $g$ (Lemma [[§60 Lie Groups and Left-Invariant Vector Fields#^lem-60-5|§60.5]]). So, by Proposition [[§70 Complete Vector Fields#^prop-70-10|§70.10]],
>
> $$
> t \mapsto L_{\varphi_s(e)}\big(\varphi_t(e)\big)
> $$
>
> is an integral curve of $\mathbf{X}$, and it starts at $L_{\varphi_s(e)}(e) = \varphi_s(e)$: composing an integral curve of $\mathbf{X}$ with a map gives an integral curve of a related field, and here the related field is $\mathbf{X}$ itself. So is $t \mapsto \varphi_{t+s}(e)$, an integral curve by the translation lemma (Lemma [[§67 Integral Curves#^lem-67-4|§67.4]](1)) with value $\varphi_s(e)$ at $t = 0$. Therefore, by uniqueness (Proposition [[§68 Local Existence and Uniqueness#^prop-68-3|§68.3]]), for all $t$,
>
> $$
> \varphi_{t+s}(e) = L_{\varphi_s(e)}\big(\varphi_t(e)\big) = \varphi_s(e) \cdot \varphi_t(e) .
> $$
>
> Writing out what $L$ is, the group multiplication appears explicitly for the first time.

^pf-71-1

*Uses:* [[§70 Complete Vector Fields#^thm-70-11|§70.11]], [[§60 Lie Groups and Left-Invariant Vector Fields#^lem-60-5|§60.5]], [[§70 Complete Vector Fields#^prop-70-10|§70.10]], [[§67 Integral Curves#^lem-67-4|§67.4]], [[§68 Local Existence and Uniqueness#^prop-68-3|§68.3]]

This is the case $g = \varphi^e(s)$ of $\varphi^g(t) = g\,\varphi^e(t)$ in Theorem [[§70 Complete Vector Fields#^thm-70-11|§70.11]], combined with the group law $\varphi^{\varphi^e(s)}(t) = \varphi^e(t + s)$. Since $s + t = t + s$, the elements $\varphi_s(e)$ and $\varphi_t(e)$ commute: a one-parameter subgroup is abelian, even in a non-abelian $G$.

Conversely, every smooth group morphism $\mathbb{R} \to G$ arises this way (Proposition [[§71 The Exponential Map#^prop-71-3|§71.3]] below); this was not pursued in lecture.

The one-parameter subgroup is an orbit: the left-invariant field $\mathbf{X}^A$ is complete, so it generates an $\mathbb{R}$-action (Proposition [[§70 Complete Vector Fields#^prop-70-7|§70.7]]), and $t \mapsto \varphi^A_t(e)$ is the orbit of the identity.

> [!definition] Definition §71.1: The Exponential Map
> Let $G$ be a Lie group, with Lie algebra $\mathfrak{g} = T_eG$. The **exponential map** $\exp : \mathfrak{g} \to G$ is
>
> $$
> \exp(A) = \varphi^A_t(e)\big|_{t=1}, \qquad A \in \mathfrak{g} :
> $$
>
> make $A$ into the left-invariant field $\mathbf{X}^A$, take its flow, and follow the integral curve through $e$ up to time $1$.
>
> *Lee: Ch. 20, The Exponential Map*

^def-71-1

![[m591-71-4.svg]]

*(Figure after the board.)* The group is drawn like a sphere (think of a three-sphere). The vector $A$ in the tangent space $\mathfrak{g} = T_eG$ generates a one-parameter group; following it to time one gives a point $\exp(A)$ of the group.

The name is well motivated: for subgroups of the general linear group, $\exp$ is the matrix exponential (Theorem [[§71 The Exponential Map#^thm-71-12|§71.12]] below). The essential step is the following.

> [!theorem] Proposition §71.2: Exponentials of Multiples
> For all $t \in \mathbb{R}$ and $A \in \mathfrak{g}$,
>
> $$
> \exp(tA) = \varphi^A_t(e) .
> $$
>
> So $t \mapsto \exp(tA)$ is the one-parameter subgroup of Proposition [[§71 The Exponential Map#^prop-71-1|§71.1]] for $\mathbf{X}^A$.
>
> *Lee: Proposition 20.5*

^prop-71-2

> [!proof]+ Proof
> *(Lecture 26.)* For $t = 1$ this is the definition. In general, by definition,
>
> $$
> \exp(tA) = \varphi^{tA}_s(e)\big|_{s=1} :
> $$
>
> take the field $\mathbf{X}^{tA} = t\,\mathbf{X}^A$ and flow $e$ up to $s = 1$. By the rescaling lemma (Lemma [[§67 Integral Curves#^lem-67-4|§67.4]](2)), $s \mapsto \varphi^A_{ts}(e)$ is an integral curve of $t\,\mathbf{X}^A = \mathbf{X}^{tA}$, starting at $e$: the flow of $c\mathbf{X}$ is $\varphi_{ct}$, by the chain rule. By uniqueness (Proposition [[§68 Local Existence and Uniqueness#^prop-68-3|§68.3]]) it is $s \mapsto \varphi^{tA}_s(e)$, so
>
> $$
> \exp(tA) = \varphi^{tA}_s(e)\big|_{s=1} = \varphi^A_{ts}(e)\big|_{s=1} = \varphi^A_t(e) .
> $$

^pf-71-2

*Uses:* [[§67 Integral Curves#^lem-67-4|§67.4]], [[§68 Local Existence and Uniqueness#^prop-68-3|§68.3]]

> [!theorem] Proposition §71.3: Every Smooth One-Parameter Subgroup Is $t \mapsto \exp(tA)$
> Let $G$ be a Lie group and $\gamma : \mathbb{R} \to G$ a smooth group morphism from the additive group $(\mathbb{R}, +)$, and put $A = \dot\gamma(0) \in T_eG = \mathfrak{g}$. Then $\gamma$ is the integral curve of $\mathbf{X}^A$ starting at $e$:
>
> $$
> \gamma(t) = \varphi^A_t(e) = \exp(tA) \qquad \text{for all } t \in \mathbb{R} .
> $$
>
> *Lee: Theorem 20.1*

^prop-71-3

> [!proof]+ Proof
> *(Filled in, for smooth morphisms; the converse was not pursued in lecture.)* $\gamma(0) = e$, because $\gamma$ is a group morphism; so $\dot\gamma(0) \in T_eG$. Fix $t \in \mathbb{R}$. Differentiating $\gamma(t + s) = \gamma(t)\gamma(s) = L_{\gamma(t)}(\gamma(s))$ in $s$ at $s = 0$ gives $\dot\gamma(t) = d(L_{\gamma(t)})_e(A) = \mathbf{X}^A_{\gamma(t)}$ (Corollary [[§31 Tangent Vectors as Velocities of Curves#^cor-31-5|§31.5]]). In detail: on the left, the derivative of $s \mapsto \gamma(t + s)$ at $s = 0$ is $\dot\gamma(t)$ (Definition [[§31 Tangent Vectors as Velocities of Curves#^def-31-3|§31.3]] and the chain rule for real functions, as in the proof of Lemma [[§67 Integral Curves#^lem-67-4|§67.4]]); on the right, the curve $s \mapsto \gamma(s)$ passes through $e$ at $s = 0$ with velocity $A$, so by Corollary [[§31 Tangent Vectors as Velocities of Curves#^cor-31-5|§31.5]] the velocity of $s \mapsto L_{\gamma(t)}(\gamma(s))$ at $s = 0$ is $d(L_{\gamma(t)})_e(A)$, which is $\mathbf{X}^A_{\gamma(t)}$ by Definition [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-5|§60.5]]. So $\gamma$ is the integral curve of $\mathbf{X}^A$ starting at $\gamma(0) = e$, defined on $\mathbb{R}$, and $\gamma(t) = \varphi^A_t(e)$ (Proposition [[§69 Maximal Integral Curves and Flows#^prop-69-1|§69.1]]); this is $\exp(tA)$ by Proposition [[§71 The Exponential Map#^prop-71-2|§71.2]].

^pf-71-3

*Uses:* [[§31 Tangent Vectors as Velocities of Curves#^cor-31-5|§31.5]], [[§31 Tangent Vectors as Velocities of Curves#^def-31-3|Def. §31.3]], [[§67 Integral Curves#^lem-67-4|§67.4]], [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-5|Def. §60.5]], [[§69 Maximal Integral Curves and Flows#^prop-69-1|§69.1]], [[§71 The Exponential Map#^prop-71-2|§71.2]]

Continuous group morphisms $\mathbb{R} \to G$ are automatically smooth (Lee, Problem 20-11(a); not proved in these notes), so the same holds for them.

> [!theorem] Corollary §71.4: The Exponential Law on a Line
> For all $s, t \in \mathbb{R}$ and $A \in \mathfrak{g}$,
>
> $$
> \exp\big((s + t)A\big) = \exp(sA) \cdot \exp(tA) .
> $$
>
> *Lee: Proposition 20.8*

^cor-71-4

> [!proof]+ Proof
> *(Lecture 26.)* By Proposition [[§71 The Exponential Map#^prop-71-2|§71.2]], then Proposition [[§71 The Exponential Map#^prop-71-1|§71.1]], then Proposition [[§71 The Exponential Map#^prop-71-2|§71.2]] twice:
>
> $$
> \exp\big((s + t)A\big) = \varphi^A_{s+t}(e) = \varphi^A_s(e) \cdot \varphi^A_t(e) = \exp(sA) \cdot \exp(tA) .
> $$

^pf-71-4

*Uses:* [[§71 The Exponential Map#^prop-71-2|§71.2]], [[§71 The Exponential Map#^prop-71-1|§71.1]]

This explains the name: it is an exponential law. In particular $\exp(0) = e$ and $\exp(-A) = \exp(A)^{-1}$.

> [!remark] Remark: Warning: $\exp(A + B) \neq \exp(A)\exp(B)$ in General
> It is *not* true in general that
>
> $$
> \exp(A + B) = \exp(A) \cdot \exp(B) .
> $$
>
> The reason: many Lie groups are non-abelian. The plus on the left is the addition in the tangent space at the identity, which is commutative, while the group law is not; so the identity cannot hold in general. There is a famous formula for $\exp(A)\exp(B)$, the Baker–Campbell–Hausdorff formula, a complicated series of iterated brackets of $A$ and $B$. For a single direction, $A$ and $B = cA$, the identity holds (Corollary [[§71 The Exponential Map#^cor-71-4|§71.4]]); more generally, it holds if $A$ and $B$ commute, which is not easy to show and is not proved in the course. (Lee, Problem 20-8, characterizes the groups where it holds for all $A$, $B$.)
>
> *(Not from lecture.)* A concrete failure in $\mathrm{GL}(2, \mathbb{R})$, using the matrix exponential of Theorem [[§71 The Exponential Map#^thm-71-12|§71.12]], is Example [[§71 The Exponential Map#^ex-71-1|§71.1]] below.

^rem-71-1

![[m591-71-3.svg]]

*(Not from lecture; figure added.)* The two matrices of Example [[§71 The Exponential Map#^ex-71-1|§71.1]] acting on the unit square: $\exp(A)\exp(B)$ (blue) and $\exp(A + B)$ (red). Both have determinant $1$, so the parallelograms have the same area, but they are different maps.

*(Assignment 7, Problem 5.)* The exponential map of a subgroup is the restriction of that of the larger group, because the integral curves are; for a linear group this identifies $\exp$ with the matrix exponential series, completing the proof of Theorem [[§71 The Exponential Map#^thm-71-12|§71.12]] below. The series facts are Lemma [[§71 The Exponential Map#^lem-71-5|§71.5]]: $e^{tA} = \sum_{\ell \ge 0} \frac{t^\ell}{\ell!} A^\ell$ converges and may be differentiated term by term, $\frac{d}{dt} e^{tA} = A\, e^{tA} = e^{tA} A$.

> [!theorem] Lemma §71.5: The Matrix Exponential Series
> Let $A \in \operatorname{Mat}(n, \mathbb{R})$.
>
> 1. For every $t \in \mathbb{R}$ the series
>
> $$
> e^{tA} = \sum_{\ell=0}^\infty \frac{t^\ell}{\ell!} A^\ell
> $$
>
> converges in $\operatorname{Mat}(n, \mathbb{R})$, in any norm: each entry of $e^{tA}$ is a real power series in $t$ that converges absolutely for every $t \in \mathbb{R}$. In particular $e^{0 \cdot A} = I$.
>
> 2. The curve $\mathbb{R} \to \operatorname{Mat}(n, \mathbb{R})$, $t \mapsto e^{tA}$, is smooth, the series may be differentiated term by term, and
>
> $$
> \frac{d}{dt}\, e^{tA} = A\, e^{tA} = e^{tA} A .
> $$
>
> *Lee: Proposition 20.2*

^lem-71-5

> [!proof]+ Proof
> *(Not from lecture; filled in. Lecture 26 left the series facts as an exercise. Three facts are quoted from analysis: the comparison test for series; that a real power series $\sum_\ell c_\ell t^\ell$ which converges for every $t \in \mathbb{R}$ is a smooth function of $t$, whose derivative is the series $\sum_{\ell \ge 1} \ell c_\ell t^{\ell - 1}$ of the derivatives of its terms, again convergent for every $t$; and that all norms on a finite-dimensional real vector space are equivalent.)*
>
> *A bound on the powers.* For $B \in \operatorname{Mat}(n, \mathbb{R})$ write $|B| = \max_{i,j} |B_{ij}|$, a norm on $\operatorname{Mat}(n, \mathbb{R})$. For $B, C \in \operatorname{Mat}(n, \mathbb{R})$ each entry $(BC)_{ij} = \sum_{k=1}^n B_{ik} C_{kj}$ is a sum of $n$ products, so $|BC| \le n\, |B|\, |C|$. Put $a = n|A|$. Then $|A^\ell| \le a^\ell$ for every $\ell \ge 0$, by induction: $|A^0| = |I| = 1$, and if $|A^\ell| \le a^\ell$, then $|A^{\ell + 1}| = |A^\ell A| \le n\, |A^\ell|\, |A| \le a^\ell \cdot a$.
>
> *(1)* Fix $i, j$. The $(i, j)$ entry of the $\ell$-th term of the series is $c_\ell t^\ell$ with $c_\ell = (A^\ell)_{ij}/\ell!$, and by the bound $|c_\ell t^\ell| \le (a|t|)^\ell/\ell!$. The series $\sum_\ell (a|t|)^\ell/\ell!$ converges, to $e^{a|t|}$; so by the comparison test $\sum_\ell c_\ell t^\ell$ converges absolutely, for every $t \in \mathbb{R}$. Hence the partial sums of the matrix series converge in every entry, which is convergence in the norm $|\cdot|$, and so in any norm on $\operatorname{Mat}(n, \mathbb{R})$, since all norms on this finite-dimensional space are equivalent. At $t = 0$ only the term $\ell = 0$ is nonzero, and it is $A^0 = I$.
>
> *(2)* A curve in $\operatorname{Mat}(n, \mathbb{R}) = \mathbb{R}^{n^2}$ is smooth exactly when its entries are, and its derivative is taken entry by entry. By the quoted fact on power series, each entry $t \mapsto \sum_\ell c_\ell t^\ell$ of $e^{tA}$ is smooth, with derivative
>
> $$
> \sum_{\ell \ge 1} \ell\, c_\ell\, t^{\ell - 1} = \sum_{\ell \ge 1} \frac{t^{\ell - 1}}{(\ell - 1)!}\, (A^\ell)_{ij} = \sum_{m \ge 0} \frac{t^m}{m!}\, (A^{m+1})_{ij} \qquad (m = \ell - 1) :
> $$
>
> differentiating $t^\ell$ brings out a factor $\ell$, which cancels against $\ell!$, and the index is shifted. So $t \mapsto e^{tA}$ is smooth and
>
> $$
> \frac{d}{dt}\, e^{tA} = \sum_{m=0}^\infty \frac{t^m}{m!}\, A^{m+1} .
> $$
>
> Now $A^{m+1} = A\, A^m = A^m A$. For a fixed matrix $B$, each entry of $BC$ and of $CB$ is a finite sum of entries of $C$ multiplied by entries of $B$; so if a series of matrices $\sum_m C_m$ converges in every entry, then $\sum_m B C_m = B \sum_m C_m$ and $\sum_m C_m B = \big(\sum_m C_m\big) B$, by the linearity of limits. With $B = A$ and $C_m = \frac{t^m}{m!} A^m$:
>
> $$
> \sum_{m=0}^\infty \frac{t^m}{m!}\, A\, A^m = A\, e^{tA}, \qquad \sum_{m=0}^\infty \frac{t^m}{m!}\, A^m A = e^{tA} A .
> $$
>
> The extra factor $A$ can be put on the left or on the right.

^pf-71-5

> [!theorem] Lemma §71.6: The Matrix Exponential Is Invertible
> For $A \in \operatorname{Mat}(n, \mathbb{R})$ and $t \in \mathbb{R}$, $e^{tA}\, e^{-tA} = I$. So $e^{tA} \in \mathrm{GL}(n, \mathbb{R})$, with inverse $e^{-tA}$.

^lem-71-6

> [!proof]+ Proof
> *(Not from lecture; filled in. The outline of the proof of Theorem [[§71 The Exponential Map#^thm-71-12|§71.12]] and the submitted solution of Assignment 7, Problem 5(b), use that $e^{tA}$ is invertible without proof.)* Each entry of a product of matrix-valued curves is a sum of products of entries, so the product rule holds: $\frac{d}{dt}(B(t)C(t)) = B'(t)C(t) + B(t)C'(t)$. With $\frac{d}{dt} e^{tA} = A e^{tA} = e^{tA} A$ (Lemma [[§71 The Exponential Map#^lem-71-5|§71.5]](2)) and, by the chain rule, $\frac{d}{dt} e^{-tA} = -A\, e^{-tA}$,
>
> $$
> \frac{d}{dt}\big(e^{tA} e^{-tA}\big) = \big(e^{tA} A\big) e^{-tA} + e^{tA}\big(-A\, e^{-tA}\big) = 0 .
> $$
>
> So every entry of $e^{tA} e^{-tA}$ is a function on $\mathbb{R}$ with zero derivative, hence constant, and at $t = 0$ the product is $I \cdot I = I$. Thus $e^{tA} e^{-tA} = I$ for all $t$; then $\det(e^{tA}) \det(e^{-tA}) = 1$, so $e^{tA}$ is invertible, and its inverse is $e^{-tA}$, since a one-sided inverse of a square matrix is the inverse.

^pf-71-6

*Uses:* [[§71 The Exponential Map#^thm-71-12|§71.12]], [[§71 The Exponential Map#^lem-71-5|§71.5]]

> [!theorem] Lemma §71.7: Exponentials of Nilpotent and of Diagonal Matrices
> Let $A \in \operatorname{Mat}(n, \mathbb{R})$ and $e^{A} = \sum_{\ell \ge 0} A^\ell/\ell!$ (Lemma [[§71 The Exponential Map#^lem-71-5|§71.5]] with $t = 1$).
>
> 1. If $A^k = 0$ for some $k \ge 1$, then $e^{A} = \displaystyle\sum_{\ell=0}^{k-1} \frac{1}{\ell!}\, A^\ell$, a finite sum.
> 2. If $A = \mathrm{diag}(\lambda_1, \ldots, \lambda_n)$, then $e^{A} = \mathrm{diag}\big( e^{\lambda_1}, \ldots, e^{\lambda_n} \big)$.

^lem-71-7

> [!proof]+ Proof
> *(Assignment 8, Problems 2(a) and 3(b): the two computations of the submitted solution, in general.)*
>
> *(1).* For $\ell \ge k$, $A^\ell = A^{\ell - k} A^k = 0$; so all terms of the series from the $k$-th on vanish.
>
> *(2).* The product of two diagonal matrices is the diagonal matrix of the products of their entries, so by induction $A^\ell = \mathrm{diag}(\lambda_1^\ell, \ldots, \lambda_n^\ell)$. The series converges in every entry (Lemma [[§71 The Exponential Map#^lem-71-5|§71.5]](1)): the off-diagonal entries of all partial sums are $0$, and the $i$-th diagonal entry is $\sum_{\ell \ge 0} \lambda_i^\ell/\ell! = e^{\lambda_i}$.

^pf-71-7

*Uses:* [[§71 The Exponential Map#^lem-71-5|§71.5]]

> [!theorem] Lemma §71.8: Integral Curves of a Left-Invariant Field on a Lie Subgroup
> Let $H$ be a Lie group and $G \subseteq H$ a subgroup that is a Lie group with the inclusion $\iota : G \hookrightarrow H$ smooth and $d\iota_e$ injective — a Lie subgroup (Definition [[§61 Lie Group Morphisms and Linear Groups#^def-61-3|§61.3]]), as in Theorem [[§61 Lie Group Morphisms and Linear Groups#^thm-61-7|§61.7]] — so that $\mathfrak{g} = T_eG$ is identified with $d\iota_e(\mathfrak{g}) \subseteq \mathfrak{h} = T_eH$. For $A \in \mathfrak{g}$ let $\mathbf{A}^G \in \mathfrak{X}(G)$ and $\mathbf{A}^H \in \mathfrak{X}(H)$ be the left-invariant fields with $\mathbf{A}^G_e = A$ and $\mathbf{A}^H_e = d\iota_e(A)$ (the fields written $\mathbf{X}^A$ in the notation of this section, one on each group). Then $\mathbf{A}^G$ is $\iota$-related to $\mathbf{A}^H$, and for every integral curve $\gamma$ of $\mathbf{A}^G$, $\iota \circ \gamma$ is an integral curve of $\mathbf{A}^H$.

^lem-71-8

> [!proof]+ Proof
> *(Assignment 7, Problem 5(a): the submitted solution. The relatedness is also Lemma [[§61 Lie Group Morphisms and Linear Groups#^lem-61-1|§61.1]] for the morphism $\iota$, and the second statement Proposition [[§70 Complete Vector Fields#^prop-70-10|§70.10]]; the solution proves both directly.)* $\iota$ is a Lie group morphism (Definition [[§61 Lie Group Morphisms and Linear Groups#^def-61-2|§61.2]]), and by Definition [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-5|§60.5]]
>
> $$
> \mathbf{A}^G_g = d(L_g)_e(A) \quad (g \in G), \qquad \mathbf{A}^H_h = d(L_h)_e\big(d\iota_e(A)\big) \quad (h \in H),
> $$
>
> where $L_g$ and $L_h$ are left translations in $G$ and in $H$.
>
> *$\mathbf{A}^G$ is $\iota$-related to $\mathbf{A}^H$.* Let $g \in G$. For $k \in G$, since $\iota$ is a homomorphism, $\iota \circ L_g(k) = \iota(gk) = \iota(g)\iota(k) = L_{\iota(g)} \circ \iota(k)$; so $\iota \circ L_g = L_{\iota(g)} \circ \iota$ as maps $G \to H$. Differentiating at $e$ by the chain rule, with $L_g(e) = g$ and $\iota(e) = e$,
>
> $$
> d\iota_g \circ d(L_g)_e = d(L_{\iota(g)})_e \circ d\iota_e : T_eG \to T_{\iota(g)}H .
> $$
>
> Applying both sides to $A$,
>
> $$
> d\iota_g\big(\mathbf{A}^G_g\big) = d\iota_g\big(d(L_g)_e(A)\big) = d(L_{\iota(g)})_e\big(d\iota_e(A)\big) = \mathbf{A}^H_{\iota(g)} \qquad \text{for all } g \in G .
> $$
>
> *Integral curves.* Let $\gamma : J \to G$ be an integral curve of $\mathbf{A}^G$, so $\gamma'(t) = \mathbf{A}^G_{\gamma(t)}$ for $t \in J$. The curve $\iota \circ \gamma : J \to H$ is smooth, and by the chain rule and the relatedness,
>
> $$
> (\iota \circ \gamma)'(t) = d\iota_{\gamma(t)}\big(\gamma'(t)\big) = d\iota_{\gamma(t)}\big(\mathbf{A}^G_{\gamma(t)}\big) = \mathbf{A}^H_{\iota(\gamma(t))} \qquad \text{for all } t \in J .
> $$
>
> So $\iota \circ \gamma$ is an integral curve of $\mathbf{A}^H$.

^pf-71-8

*Uses:* [[§61 Lie Group Morphisms and Linear Groups#^lem-61-1|§61.1]], [[§70 Complete Vector Fields#^prop-70-10|§70.10]], [[§61 Lie Group Morphisms and Linear Groups#^def-61-2|Def. §61.2]], [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-5|Def. §60.5]]

> [!theorem] Corollary §71.9: The Exponential Map of a Lie Subgroup
> In the setting of Lemma [[§71 The Exponential Map#^lem-71-8|§71.8]], for $A \in \mathfrak{g}$ and $t \in \mathbb{R}$,
>
> $$
> \iota\big(\exp_G(tA)\big) = \exp_H\big(t\, d\iota_e(A)\big) .
> $$
>
> So the exponential map of $G$ is the restriction of that of $H$ to $\mathfrak{g} \subseteq \mathfrak{h}$, and $\exp_H(tA) \in G$ for all $t$.

^cor-71-9

> [!proof]+ Proof
> *(Filled in.)* $\mathbf{A}^G$ is complete (Theorem [[§70 Complete Vector Fields#^thm-70-11|§70.11]]), and its integral curve starting at $e$ is $\gamma(t) = \exp_G(tA)$, $t \in \mathbb{R}$ (Proposition [[§71 The Exponential Map#^prop-71-2|§71.2]]). By Lemma [[§71 The Exponential Map#^lem-71-8|§71.8]], $\iota \circ \gamma$ is an integral curve of $\mathbf{A}^H$ defined on $\mathbb{R}$ and starting at $\iota(e) = e$; so it is the maximal integral curve of $\mathbf{A}^H$ starting at $e$ (Proposition [[§69 Maximal Integral Curves and Flows#^prop-69-1|§69.1]]), which is $t \mapsto \exp_H(t\, d\iota_e(A))$ (Proposition [[§71 The Exponential Map#^prop-71-2|§71.2]]).

^pf-71-9

*Uses:* [[§70 Complete Vector Fields#^thm-70-11|§70.11]], [[§71 The Exponential Map#^prop-71-2|§71.2]], [[§71 The Exponential Map#^lem-71-8|§71.8]], [[§69 Maximal Integral Curves and Flows#^prop-69-1|§69.1]]

> [!theorem] Corollary §71.10: Lie Group Morphisms Commute with the Exponential Map
> Let $F : H \to G$ be a Lie group morphism. Then $F(\exp_H A) = \exp_G\big(dF_e(A)\big)$ for every $A \in \mathfrak{h}$.
>
> *Lee: Proposition 20.8(g)*

^cor-71-10

> [!proof]+ Proof
> *(Not from the assignment; filled in: the proof of Corollary [[§71 The Exponential Map#^cor-71-9|§71.9]] with $F$ in place of $\iota$.)* Let $\mathbf{X}^A \in \mathfrak{X}(H)$ and $\mathbf{Y}^{\tilde A} \in \mathfrak{X}(G)$, $\tilde A = dF_e(A)$, be the left-invariant extensions; they are $F$-related (Lemma [[§61 Lie Group Morphisms and Linear Groups#^lem-61-1|§61.1]]). The integral curve $t \mapsto \exp_H(tA)$ of $\mathbf{X}^A$ starting at $e$ is defined on $\mathbb{R}$ (Theorem [[§70 Complete Vector Fields#^thm-70-11|§70.11]], Proposition [[§71 The Exponential Map#^prop-71-2|§71.2]]), so $t \mapsto F(\exp_H(tA))$ is an integral curve of $\mathbf{Y}^{\tilde A}$ on $\mathbb{R}$ (Proposition [[§70 Complete Vector Fields#^prop-70-10|§70.10]]) starting at $F(e) = e$. By Proposition [[§69 Maximal Integral Curves and Flows#^prop-69-1|§69.1]] it is $t \mapsto \exp_G(t\tilde A)$ (Proposition [[§71 The Exponential Map#^prop-71-2|§71.2]]); take $t = 1$.

^pf-71-10

*Uses:* [[§71 The Exponential Map#^cor-71-9|§71.9]], [[§61 Lie Group Morphisms and Linear Groups#^lem-61-1|§61.1]], [[§70 Complete Vector Fields#^thm-70-11|§70.11]], [[§71 The Exponential Map#^prop-71-2|§71.2]], [[§70 Complete Vector Fields#^prop-70-10|§70.10]], [[§69 Maximal Integral Curves and Flows#^prop-69-1|§69.1]]

> [!theorem] Proposition §71.11: Integral Curves of Left-Invariant Fields on a Linear Group
> Let $G \subseteq \mathrm{GL}(n, \mathbb{R})$ be a linear group that is a Lie subgroup (Theorem [[§61 Lie Group Morphisms and Linear Groups#^thm-61-7|§61.7]]), with $\mathfrak{g}$ identified with a subspace of $\operatorname{Mat}(n, \mathbb{R})$, and $A \in \mathfrak{g}$. For every $g \in G$ the integral curve of the left-invariant field $\mathbf{A}^G$ (with $\mathbf{A}^G_e = A$, as in Lemma [[§71 The Exponential Map#^lem-71-8|§71.8]]) starting at $g$ is
>
> $$
> t \longmapsto g\, e^{tA} = g \Big(\sum_{\ell=0}^\infty \frac{t^\ell}{\ell!} A^\ell\Big), \qquad t \in \mathbb{R} .
> $$
>
> In particular $g\, e^{tA} \in G$ for all $t$.

^prop-71-11

> [!proof]+ Proof
> *(Assignment 7, Problem 5(b): the submitted solution, with the invertibility of $e^{tA}$ supplied by Lemma [[§71 The Exponential Map#^lem-71-6|§71.6]] and the convergence and term-by-term differentiation of the series by Lemma [[§71 The Exponential Map#^lem-71-5|§71.5]]; the solution takes $c(t) \in \mathrm{GL}(n, \mathbb{R})$ for granted.)* Let $\iota : G \hookrightarrow \mathrm{GL}(n, \mathbb{R})$ be the inclusion. Since $\mathrm{GL}(n, \mathbb{R})$ is open in $\operatorname{Mat}(n, \mathbb{R})$, $T_X \mathrm{GL}(n, \mathbb{R}) = \operatorname{Mat}(n, \mathbb{R})$ for each $X$ (Example [[§60 Lie Groups and Left-Invariant Vector Fields#^ex-60-1|§60.1]]); the velocity of a matrix-valued curve is its entrywise derivative, and $A \in \mathfrak{g}$ is identified with the matrix $d\iota_e(A)$. Let $\mathbf{A}^{\mathrm{GL}}$ be the left-invariant field on $\mathrm{GL}(n, \mathbb{R})$ with $\mathbf{A}^{\mathrm{GL}}_I = A$.
>
> *The field $\mathbf{A}^{\mathrm{GL}}$.* For $h \in \mathrm{GL}(n, \mathbb{R})$, $L_h(X) = hX$ is the restriction of the linear map $X \mapsto hX$ of $\operatorname{Mat}(n, \mathbb{R})$. Computing its differential along the curve $t \mapsto I + tA$, which passes through $I$ with velocity $A$,
>
> $$
> \mathbf{A}^{\mathrm{GL}}_h = d(L_h)_I(A) = \frac{d}{dt}\Big|_{t=0} h(I + tA) = \frac{d}{dt}\Big|_{t=0} (h + t\, hA) = hA ,
> $$
>
> as in Example [[§60 Lie Groups and Left-Invariant Vector Fields#^ex-60-1|§60.1]].
>
> *$t \mapsto g\,e^{tA}$ is an integral curve of $\mathbf{A}^{\mathrm{GL}}$.* Let $g \in G$ and $c(t) = g \sum_{\ell \ge 0} \frac{t^\ell}{\ell!} A^\ell$, $t \in \mathbb{R}$. By Lemma [[§71 The Exponential Map#^lem-71-6|§71.6]], $c(t) = g\, e^{tA}$ is a product of invertible matrices, so $c : \mathbb{R} \to \mathrm{GL}(n, \mathbb{R})$; and $c(0) = gI = g$. Differentiating term by term, the $\ell = 0$ term $I$ is constant, and for $\ell \ge 1$, $\frac{d}{dt}\frac{t^\ell}{\ell!} A^\ell = \frac{t^{\ell-1}}{(\ell-1)!} A^\ell$. Since left multiplication by $g$ and right multiplication by $A$ are linear and continuous, reindexing with $m = \ell - 1$ gives
>
> $$
> c'(t) = g \sum_{m=0}^\infty \frac{t^m}{m!} A^{m+1} = \Big(g \sum_{m=0}^\infty \frac{t^m}{m!} A^m\Big) A = c(t)\, A = \mathbf{A}^{\mathrm{GL}}_{c(t)} \qquad \text{for all } t \in \mathbb{R} .
> $$
>
> *Comparison with $\mathbf{A}^G$.* Left-invariant fields are complete (Theorem [[§70 Complete Vector Fields#^thm-70-11|§70.11]]), so the integral curve $\gamma$ of $\mathbf{A}^G$ starting at $g$ is defined on $\mathbb{R}$. By Lemma [[§71 The Exponential Map#^lem-71-8|§71.8]] with $H = \mathrm{GL}(n, \mathbb{R})$, $\iota \circ \gamma : \mathbb{R} \to \mathrm{GL}(n, \mathbb{R})$ is an integral curve of $\mathbf{A}^{\mathrm{GL}}$ with $\iota \circ \gamma(0) = g$. So $c$ and $\iota \circ \gamma$ are integral curves of $\mathbf{A}^{\mathrm{GL}}$ on $\mathbb{R}$ with the same starting point, and by uniqueness (Proposition [[§68 Local Existence and Uniqueness#^prop-68-3|§68.3]])
>
> $$
> c(t) = \iota(\gamma(t)) \qquad \text{for all } t \in \mathbb{R} .
> $$
>
> Hence $c(t) \in G$ for all $t$, and $c$ is the integral curve of $\mathbf{A}^G$ starting at $g$.

^pf-71-11

*Uses:* [[§71 The Exponential Map#^lem-71-6|§71.6]], [[§60 Lie Groups and Left-Invariant Vector Fields#^ex-60-1|Ex. §60.1]], [[§70 Complete Vector Fields#^thm-70-11|§70.11]], [[§71 The Exponential Map#^lem-71-8|§71.8]], [[§68 Local Existence and Uniqueness#^prop-68-3|§68.3]], [[§71 The Exponential Map#^lem-71-5|§71.5]]

> [!theorem] Theorem §71.12: The Exponential Map of a Linear Group
> Let $G \subseteq \mathrm{GL}(n, \mathbb{R})$ be a linear group (Definition [[§61 Lie Group Morphisms and Linear Groups#^def-61-1|§61.1]]) that is a Lie subgroup (Definition [[§61 Lie Group Morphisms and Linear Groups#^def-61-3|§61.3]]; Theorem [[§61 Lie Group Morphisms and Linear Groups#^thm-61-7|§61.7]]), and $A \in \mathfrak{g}$, a matrix. Then
>
> $$
> \exp(A) = \sum_{\ell=0}^\infty \frac{1}{\ell!} A^\ell ,
> $$
>
> the series converging in any norm on $\operatorname{Mat}(n, \mathbb{R})$.
>
> *Lee: Proposition 20.2, Example 20.4*

^thm-71-12

> [!proof]+ Proof (outline from Lecture 26; the general case from Assignment 7, Problem 5)
> *(The lecture gave the case $G = \mathrm{GL}(n, \mathbb{R})$ in outline; the series facts are an exercise, worked out in Lemma [[§71 The Exponential Map#^lem-71-5|§71.5]], and the case of a general $G \subseteq \mathrm{GL}(n, \mathbb{R})$ needs an extra argument, which is part of the homework: Proposition [[§71 The Exponential Map#^prop-71-11|§71.11]], Assignment 7, Problem 5(b).)* The method is once again uniqueness. Show it first for $G = \mathrm{GL}(n, \mathbb{R})$. Define $e^A = \sum_{\ell \ge 0} A^\ell / \ell!$. Then
>
> $$
> \frac{d}{dt}\, e^{tA} = A\, e^{tA} = e^{tA} A ,
> $$
>
> by manipulating the series (Lemma [[§71 The Exponential Map#^lem-71-5|§71.5]]): it converges strongly enough in norm to be differentiated term by term; differentiating $t^\ell$ brings out a factor $\ell$, which cancels against $\ell!$, and the resulting shift of index produces the extra factor $A$, which can be put on the left or on the right. So $\gamma(t) = e^{tA}$ is a curve in $\mathrm{GL}(n, \mathbb{R})$ (it is invertible, Lemma [[§71 The Exponential Map#^lem-71-6|§71.6]]), and
>
> $$
> \frac{d}{dt}\gamma(t) = e^{tA} A = d\big(L_{e^{tA}}\big)_e(A) = \mathbf{X}^A_{e^{tA}} ,
> $$
>
> because $L_{e^{tA}} : g \mapsto e^{tA} g$ is the restriction to $\mathrm{GL}(n, \mathbb{R})$ of a linear map, so it is its own differential (Example [[§60 Lie Groups and Left-Invariant Vector Fields#^ex-60-1|§60.1]]). With $\gamma(0) = e$, $\gamma$ is the integral curve of $\mathbf{X}^A$ starting at $e$:
>
> $$
> \left\{ \begin{aligned} \tfrac{d}{dt}\gamma(t) &= \mathbf{X}^A_{\gamma(t)} \\ \gamma(0) &= e \end{aligned} \right.
> \qquad \Longrightarrow \qquad e^{tA} = \varphi^A_t(e) ,
> $$
>
> and at $t = 1$, $e^A = \exp(A)$ by Definition [[§71 The Exponential Map#^def-71-1|§71.1]]. For a general $G \subseteq \mathrm{GL}(n, \mathbb{R})$: by Proposition [[§71 The Exponential Map#^prop-71-11|§71.11]] with $g = e = I$, the integral curve of the left-invariant field $\mathbf{X}^A$ on $G$ starting at $e$ is $t \mapsto e^{tA}$, and at $t = 1$, $\exp(A) = e^A$ by Definition [[§71 The Exponential Map#^def-71-1|§71.1]]. *(Completed with Assignment 7, Problem 5.)*

^pf-71-12

*Uses:* [[§60 Lie Groups and Left-Invariant Vector Fields#^ex-60-1|Ex. §60.1]], [[§71 The Exponential Map#^def-71-1|Def. §71.1]], [[§71 The Exponential Map#^prop-71-11|§71.11]], [[§71 The Exponential Map#^lem-71-6|§71.6]], [[§71 The Exponential Map#^lem-71-5|§71.5]]

> [!example] Example §71.1: $\exp(A + B) \neq \exp(A)\exp(B)$ for Two Nilpotent Matrices
> *(Not from lecture.)* In $\mathrm{GL}(2, \mathbb{R})$, for $A = \begin{psmallmatrix} 0 & 1 \\ 0 & 0 \end{psmallmatrix}$ and $B = \begin{psmallmatrix} 0 & 0 \\ 1 & 0 \end{psmallmatrix}$,
>
> $$
> \exp(A)\exp(B) = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix} \neq \begin{pmatrix} \cosh 1 & \sinh 1 \\ \sinh 1 & \cosh 1 \end{pmatrix} = \exp(A + B) ,
> $$
>
> a concrete failure of the identity of the [[§71 The Exponential Map#^rem-71-1|warning]] above. Here $[A, B] = AB - BA = \begin{psmallmatrix} 1 & 0 \\ 0 & -1 \end{psmallmatrix} \neq 0$.
>
> *The exponential is the series.* For $G = \mathrm{GL}(2, \mathbb{R})$, $\mathfrak{g} = \operatorname{Mat}(2, \mathbb{R})$ (Example [[§60 Lie Groups and Left-Invariant Vector Fields#^ex-60-1|§60.1]]), and Theorem [[§71 The Exponential Map#^thm-71-12|§71.12]] gives $\exp(C) = \sum_{\ell \ge 0} C^\ell/\ell!$.
>
> *$\exp(A)\exp(B)$.* $A^2 = B^2 = 0$, so all higher powers vanish and $\exp(A) = I + A$, $\exp(B) = I + B$:
>
> $$
> \exp(A)\exp(B) = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}\begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix} = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}.
> $$
>
> *$\exp(A + B)$.* $A + B = \begin{psmallmatrix} 0 & 1 \\ 1 & 0 \end{psmallmatrix}$ has $(A + B)^2 = I$, so $(A + B)^{2k} = I$ and $(A + B)^{2k+1} = A + B$. Splitting the series into even and odd terms,
>
> $$
> \exp(A + B) = \Big(\sum_{k \ge 0} \frac{1}{(2k)!}\Big) I + \Big(\sum_{k \ge 0} \frac{1}{(2k+1)!}\Big)(A + B) = \cosh 1\; I + \sinh 1\; (A + B) = \begin{pmatrix} \cosh 1 & \sinh 1 \\ \sinh 1 & \cosh 1 \end{pmatrix}.
> $$
>
> *They differ.* The top-left entries are $2$ and $\cosh 1 = (e + e^{-1})/2 < (3 + 1)/2 = 2$.
>
> *The bracket.* $AB = \begin{psmallmatrix} 1 & 0 \\ 0 & 0 \end{psmallmatrix}$ and $BA = \begin{psmallmatrix} 0 & 0 \\ 0 & 1 \end{psmallmatrix}$, so $[A, B] = \begin{psmallmatrix} 1 & 0 \\ 0 & -1 \end{psmallmatrix} \neq 0$: $A$ and $B$ do not commute.

^ex-71-1

> [!remark] Remark: Surjectivity and Injectivity of $\exp$
> For many groups, but not for all groups, $\exp$ is surjective: for instance for all unitary groups, and more generally for compact connected groups, a fact that needs proof *(not proved here)*. But globally it is not one-to-one for a compact group: the exponential wraps the tangent space around the group, as $t \mapsto e^{it}$ wraps $\mathfrak{u}(1) = i\mathbb{R}$ around $\mathrm{U}(1)$ (the figure below). *(Not from lecture.)* Surjectivity can fail: $\exp$ takes values in the identity component, so it misses $\mathrm{O}(n) \setminus \mathrm{SO}(n)$; and even for the connected group $\mathrm{SL}(2, \mathbb{R})$ the matrix $\begin{psmallmatrix} -1 & 1 \\ 0 & -1 \end{psmallmatrix}$ is not an exponential (Example [[§71 The Exponential Map#^ex-71-2|§71.2]] below).

^rem-71-2

![[m591-71-1.svg]]

*(Not from lecture; figure added.)* Wrapping the tangent space around the group, for $G = \mathrm{U}(1)$: $\mathfrak{u}(1) = i\mathbb{R}$, and $\exp(ti) = e^{it}$ (Theorem [[§71 The Exponential Map#^thm-71-12|§71.12]] with $n = 1$, complex). The segment $[0, 2\pi i]$ (blue) goes once around the circle and $[-\pi i, 0]$ (red) covers the lower half again: $\exp$ is onto but not one-to-one, while near $0$ it is one-to-one, as Proposition [[§71 The Exponential Map#^prop-71-13|§71.13]] guarantees in general.

> [!example] Example §71.2: Two Groups Where $\exp$ Is Not Surjective
> *(Not from lecture; filled in.)*
>
> 1. For $G = \mathrm{O}(n)$, $\exp(A) \in \mathrm{SO}(n)$ for every $A \in T_I\mathrm{O}(n)$; so no element of $\mathrm{O}(n) \setminus \mathrm{SO}(n)$, for instance $\mathrm{diag}(-1, 1, \ldots, 1)$, is an exponential.
> 2. For $G = \mathrm{SL}(2, \mathbb{R})$, the matrix $B = \begin{psmallmatrix} -1 & 1 \\ 0 & -1 \end{psmallmatrix}$, which has $\det B = 1$, is not $\exp(A)$ for any $A \in \mathfrak{sl}(2, \mathbb{R})$. ($\mathrm{SL}(2, \mathbb{R})$ is connected, by Corollary [[§71 The Exponential Map#^cor-71-16|§71.16]] below; so here the failure is not a matter of components.)
>
> *(1).* Let $A \in T_I\mathrm{O}(n)$. The curve $t \mapsto \exp(tA)$ is an integral curve in $\mathrm{O}(n)$ (Proposition [[§71 The Exponential Map#^prop-71-2|§71.2]]), so it is continuous. Every $g \in \mathrm{O}(n)$ has $\det(g)^2 = \det(g)\det(g^{\mathsf T}) = \det I = 1$, so $\det g = \pm 1$. Hence $t \mapsto \det \exp(tA)$ is a continuous function $\mathbb{R} \to \{1, -1\}$ with the value $\det I = 1$ at $t = 0$; by the intermediate value theorem it is constant, and $\det \exp(A) = 1$: $\exp(A) \in \mathrm{SO}(n)$ (Definition [[§11 Topological Groups and Classical Matrix Groups#^def-11-8|§11.8]]). The matrix $\mathrm{diag}(-1, 1, \ldots, 1)$ is orthogonal with determinant $-1$, so $\mathrm{O}(n) \setminus \mathrm{SO}(n)$ is not empty.
>
> *(2), the exponential.* $\mathrm{SL}(2, \mathbb{R})$ is a linear group that is a Lie subgroup of $\mathrm{GL}(2, \mathbb{R})$ (Theorem [[§61 Lie Group Morphisms and Linear Groups#^thm-61-7|§61.7]]), with $\mathfrak{sl}(2, \mathbb{R}) = \{ A \in \operatorname{Mat}(2, \mathbb{R}) : \operatorname{tr} A = 0 \}$ (Theorem [[§25 The Geometric Tangent Space#^thm-25-5|§25.5]]); so $\exp(A) = \sum_{\ell \ge 0} A^\ell/\ell!$ (Theorem [[§71 The Exponential Map#^thm-71-12|§71.12]]).
>
> *(2), the series for a traceless matrix.* Let $A = \begin{psmallmatrix} a & b \\ c & -a \end{psmallmatrix}$ and $d = \det A = -a^2 - bc$. Then
>
> $$
> A^2 = \begin{pmatrix} a^2 + bc & ab - ba \\ ca - ac & cb + a^2 \end{pmatrix} = -d\, I ,
> $$
>
> so $A^{2k} = (-d)^k I$ and $A^{2k+1} = (-d)^k A$. Splitting the series, which converges absolutely in every entry (Lemma [[§71 The Exponential Map#^lem-71-5|§71.5]]), into even and odd terms,
>
> $$
> \exp(A) = \alpha\, I + \beta\, A, \qquad \alpha = \sum_{k \ge 0} \frac{(-d)^k}{(2k)!}, \quad \beta = \sum_{k \ge 0} \frac{(-d)^k}{(2k+1)!} ,
> $$
>
> and $\operatorname{tr} \exp(A) = 2\alpha$, because $\operatorname{tr} I = 2$ and $\operatorname{tr} A = 0$.
>
> *(2), $\exp(A) \neq B$.* Suppose $\exp(A) = B$. Then $2\alpha = \operatorname{tr} B = -2$, so $\alpha = -1$. If $d = 0$, then $\alpha = 1$. If $d < 0$, put $\omega = \sqrt{-d}$; then $\alpha = \sum_k \omega^{2k}/(2k)! = \cosh\omega \ge 1$. So $d > 0$; put $\omega = \sqrt{d} > 0$. Then $\alpha = \sum_k (-1)^k \omega^{2k}/(2k)! = \cos\omega$ and $\beta = \sum_k (-1)^k \omega^{2k}/(2k+1)! = \sin\omega/\omega$. From $\cos\omega = -1$ and $\cos^2\omega + \sin^2\omega = 1$, $\sin\omega = 0$, so $\beta = 0$ and $\exp(A) = -I$. But $-I \neq B$: their upper right entries are $0$ and $1$. So $B$ is not an exponential.

^ex-71-2

> [!remark]- Connections
> - Ordinary differential equations: $x(t) = e^{tA}x_0$ solves $x' = Ax$ — [[Matrix Exponential Solution]]. Here the same series is the integral curve of the left-invariant field $\mathbf{X}^A_g = gA$ on $\mathrm{GL}(n, \mathbb{R})$, i.e. the solution of the matrix equation $\gamma' = \gamma A$, $\gamma(0) = I$.

*Uses:* [[§60 Lie Groups and Left-Invariant Vector Fields#^ex-60-1|Ex. §60.1]], [[§71 The Exponential Map#^thm-71-12|§71.12]]

What is always true is the following local statement.

> [!theorem] Proposition §71.13: Smoothness and the Differential at $0$
> $\exp : \mathfrak{g} \to G$ is smooth, and $d(\exp)_0 = \mathrm{Id}_{\mathfrak{g}}$, under the identifications $T_0\mathfrak{g} = \mathfrak{g}$ (Corollary [[§30 The Differential in Coordinates#^cor-30-6|§30.6]]) and $T_eG = \mathfrak{g}$. Hence $\exp$ is a local diffeomorphism at $0 \in \mathfrak{g} = T_eG$: it maps some open neighbourhood of $0$ diffeomorphically onto an open neighbourhood of $e$.
>
> *Lee: Proposition 20.8*

^prop-71-13

> [!proof]+ Proof
> *(Lecture 26. Smoothness is awkward to prove directly, but there is a neat trick. The smoothness of the field $\mathbf{V}$, not gone into in lecture, is filled in.)*
>
> *1. Smoothness.* The flow evaluated at time one has to be considered as a function of $A$, which is new: so far only one vector field at a time has been considered. The trick, also used for variations, is to put together all the $\mathbf{X}^A$ as a single field over a larger space that includes the parameters, $G \times \mathfrak{g}$. Define
>
> $$
> \mathbf{V}_{(g, A)} = \big(\mathbf{X}^A_g, 0\big) \in T_gG \oplus T_A\mathfrak{g} = T_{(g, A)}(G \times \mathfrak{g}) ,
> $$
>
> using Theorem [[§31 Tangent Vectors as Velocities of Curves#^thm-31-7|§31.7]], and $T_A\mathfrak{g} = \mathfrak{g}$, by the vector space structure. In the second slot one simply puts zero.
>
> *Claim: $\mathbf{V}$ is smooth* (this is where the smoothness of left multiplication is used). *(Filled in.)* By Lemma [[§56 Vector Fields#^lem-56-11|§56.11]] it suffices that $\mathbf{V}h$ is smooth for every $h \in C^\infty(G \times \mathfrak{g})$. With $\iota_A : G \to G \times \mathfrak{g}$, $x \mapsto (x, A)$, Theorem [[§31 Tangent Vectors as Velocities of Curves#^thm-31-7|§31.7]] gives $\mathbf{V}_{(g,A)} = (\iota_A)_{\ast}\mathbf{X}^A_g$, so
>
> $$
> (\mathbf{V}h)(g, A) = \mathbf{X}^A_g\big[h(\cdot, A)\big] = d(L_g)_e(A)\big[h(\cdot, A)\big] = A\big[x \mapsto h(gx, A)\big] .
> $$
>
> Let $\psi(g, x, A) = h(gx, A)$, smooth on $G \times G \times \mathfrak{g}$ because multiplication is smooth (Definition [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-1|§60.1]]). Take a chart $(W, y^1, \ldots, y^m)$ of $G$ at $e$ and write $A = \sum_j A^j\, \partial/\partial y^j|_e$; the coefficients $A^j$ are linear, hence smooth, functions of $A \in \mathfrak{g}$. Then
>
> $$
> (\mathbf{V}h)(g, A) = \sum_{j=1}^m A^j\, \frac{\partial \psi}{\partial y^j}(g, e, A) ,
> $$
>
> the partial derivatives of $\psi$ in the coordinates $y^j$ of the middle factor, which are smooth on $G \times W \times \mathfrak{g}$. So $\mathbf{V}h$ is smooth. (This is the trick of Proposition [[§60 Lie Groups and Left-Invariant Vector Fields#^prop-60-8|§60.8]], now with $A$ varying too.)
>
> *$\mathbf{V}$ is complete* — because each $\mathbf{X}^A$ is, and the integration only takes place in the $G$ variable; the $\mathfrak{g}$ variable plays no role. For $(g, A) \in G \times \mathfrak{g}$, the curve $t \mapsto \big(\varphi^A_t(g), A\big)$ has velocity $\big(\mathbf{X}^A_{\varphi^A_t(g)}, 0\big) = \mathbf{V}_{(\varphi^A_t(g), A)}$ (Theorem [[§31 Tangent Vectors as Velocities of Curves#^thm-31-7|§31.7]]: the components of a velocity are the velocities of the components), it starts at $(g, A)$, and it is defined for all $t$, since $\mathbf{X}^A$ is complete. So the flow of $\mathbf{V}$ is
>
> $$
> \Phi : \mathbb{R} \times G \times \mathfrak{g} \longrightarrow G \times \mathfrak{g}, \qquad (t, g, A) \longmapsto \big(\varphi^A_t(g), A\big),
> $$
>
> which is smooth (Theorem [[§69 Maximal Integral Curves and Flows#^thm-69-4|§69.4]](2)). Now put $t = 1$, $g = e$, and project:
>
> ![[m591-71-5.svg]]
>
> $$
> A \longmapsto \varphi^A_1(e) = \exp(A) .
> $$
>
> The composite is $\exp$, so $\exp$ is smooth.
>
> *2. The differential at $0$.* We want $d(\exp)_0 : T_0\mathfrak{g} = \mathfrak{g} \to T_eG = \mathfrak{g}$ invertible; in fact it is the identity. The differential of a map is computed with curves (Corollary [[§31 Tangent Vectors as Velocities of Curves#^cor-31-5|§31.5]]). The straight line $t \mapsto tA$ in $\mathfrak{g}$ is at $0$ when $t = 0$, with velocity $A$; so, with Proposition [[§71 The Exponential Map#^prop-71-2|§71.2]],
>
> $$
> d(\exp)_0(A) = \frac{d}{dt}\Big|_{t=0} \exp(tA) = \frac{d}{dt}\Big|_{t=0} \varphi^A_t(e) = \mathbf{X}^A_e = A .
> $$
>
> *3. Local diffeomorphism.* $d(\exp)_0$ is bijective, so by the inverse function theorem, in the form of the proof of Theorem [[§35 Local Diffeomorphisms#^thm-35-2|§35.2]] ($\Leftarrow$) at the single point $0$, $\exp$ restricts to a diffeomorphism from an open neighbourhood of $0$ onto an open neighbourhood of $e$.

^pf-71-13

*Uses:* [[§31 Tangent Vectors as Velocities of Curves#^thm-31-7|§31.7]], [[§56 Vector Fields#^lem-56-11|§56.11]], [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-1|Def. §60.1]], [[§60 Lie Groups and Left-Invariant Vector Fields#^prop-60-8|§60.8]], [[§69 Maximal Integral Curves and Flows#^thm-69-4|§69.4]], [[§31 Tangent Vectors as Velocities of Curves#^cor-31-5|§31.5]], [[§71 The Exponential Map#^prop-71-2|§71.2]], [[§35 Local Diffeomorphisms#^thm-35-2|§35.2]]

**Transcription note (board 11/4).** The board writes $\exp : \mathfrak{g} \to A$ in the statement (for $G$), $\mathbf{V}_{(g,A)} \in (T_gG) \times \mathfrak{g} = T_A\mathfrak{g}$ (the space is $T_{(g,A)}(G \times \mathfrak{g})$), and the flow as $(t, g, A) \mapsto (\varphi^A_t(g), 0)$; the second component of the flow is $A$, which the field leaves unchanged, as above.

![[m591-71-2.svg]]

*(Not from lecture; figure added.)* $\exp$ for the group $G = \{(a, b) : a > 0\}$ of affine maps $x \mapsto ax + b$ of Example [[§70 Complete Vector Fields#^ex-70-1|§70.1]]. With $A = (u, v) \in \mathfrak{g}$ (meaning $\mathbf{X}^A_e = (u, v)$ in the coordinates $(a, b)$), the one-parameter subgroup is $\varphi^A_t(e) = \big(e^{ut}, \tfrac{v}{u}(e^{ut} - 1)\big)$, so $\exp(u, v) = \big(e^u, \tfrac{v}{u}(e^u - 1)\big)$ ($= (1, v)$ if $u = 0$). Lines $u = \text{const}$ (blue) go to the horizontal lines $a = e^u$, lines $v = \text{const}$ (red) to curves crossing the row $a = 1$ at $b = v$, and each one-parameter subgroup is a straight ray $b = \tfrac{v}{u}(a - 1)$ through $e$, run at exponential speed; near $0$ the grid is barely distorted, which is $d(\exp)_0 = \mathrm{Id}$. Here $\exp$ is even a diffeomorphism of $\mathfrak{g}$ onto $G$: given $(a, b)$, $u = \log a$ and $v = bu/(a - 1)$.

![[m591-71-a1.gif|620]]

*(Not from lecture; animation added, vault only.)* $\exp$ as “follow the one-parameter subgroup to time $1$”, in the same group. Left: $24$ vectors $A$ on a circle in $\mathfrak{g}$, scaled by $\tau$. Right: the points $\exp(\tau A) = \varphi^A_\tau(e)$ (Proposition [[§71 The Exponential Map#^prop-71-2|§71.2]]) moving out from $e$ along their one-parameter subgroups, straight rays at exponential speed; at $\tau = 1$ the red curve is the image of the circle under $\exp$. For small $\tau$ it is nearly a round circle, which is $d(\exp)_0 = \mathrm{Id}$.

## The Heisenberg Group and the Iwasawa Decomposition

*(Assignment 8, Problems 2 and 3: the submitted solutions, reorganized. Two groups on which the exponential map can be computed by hand. By-products that are not in the assignment are marked.)*

> [!example] Example §71.3: The Heisenberg Group
> Let
>
> $$
> m_X = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}, \qquad
> m_Y = \begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{pmatrix}, \qquad
> m_Z = \begin{pmatrix} 0 & 0 & 1 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix} .
> $$
>
> Then $[m_X, m_Y] = m_Z$, and $m_Z$ commutes with $m_X$ and $m_Y$. So the span
>
> $$
> \mathfrak{h}_3 = \big\{ A(a, b, c) : a, b, c \in \mathbb{R} \big\}, \qquad A(a, b, c) = a\, m_X + b\, m_Y + c\, m_Z = \begin{pmatrix} 0 & a & c \\ 0 & 0 & b \\ 0 & 0 & 0 \end{pmatrix} ,
> $$
>
> is closed under the commutator: it is a three-dimensional Lie subalgebra of $\mathfrak{gl}(3, \mathbb{R})$ (Theorem [[§60 Lie Groups and Left-Invariant Vector Fields#^thm-60-10|§60.10]]), the *Heisenberg Lie algebra*. Put
>
> $$
> u(x, y, z) = \begin{pmatrix} 1 & x & z \\ 0 & 1 & y \\ 0 & 0 & 1 \end{pmatrix}, \qquad H_3 = \big\{ u(x, y, z) : x, y, z \in \mathbb{R} \big\} .
> $$
>
> 1. $e^{A(a, b, c)} = I + A + \tfrac12 A^2 = u\big( a,\ b,\ c + \tfrac{ab}{2} \big)$. So the matrix exponential maps $\mathfrak{h}_3$ bijectively onto $H_3$, with inverse $u(x, y, z) \mapsto A\big( x,\ y,\ z - \tfrac{xy}{2} \big)$.
> 2. $u(x, y, z)\, u(x', y', z') = u(x + x',\ y + y',\ z + z' + xy')$ and $u(x, y, z)^{-1} = u(-x,\ -y,\ -z + xy)$. So $H_3$ is a subgroup of $\mathrm{GL}(3, \mathbb{R})$, the *Heisenberg group*; and if $u(x, y, z) = e^{A}$, then $u(x, y, z)^{-1} = e^{-A}$.
> 3. $H_3$ is a closed regular submanifold of $\mathrm{GL}(3, \mathbb{R})$ of dimension $3$, with the global chart $(g_{12}, g_{23}, g_{13})|_{H_3}$, whose inverse is $u : \mathbb{R}^3 \to H_3$. So $H_3$ is an embedded Lie subgroup of $\mathrm{GL}(3, \mathbb{R})$ (Proposition [[§61 Lie Group Morphisms and Linear Groups#^prop-61-4|§61.4]]), diffeomorphic to $\mathbb{R}^3$.
> 4. $T_IH_3 = \mathfrak{h}_3$, and the exponential map of the Lie group $H_3$ is the matrix exponential of (1). So $\exp : \mathfrak{h}_3 \to H_3$ is a diffeomorphism.

^ex-71-3

> [!remark]- Connections
> - The Heisenberg group among the subgroups of $GL_3(\mathbb{R})$: [[§5 A Zoo of Subgroups#^ex-5-5|493 Ex. §5.5]].
> - Its left-invariant vector fields: [[§71 The Exponential Map#^ex-71-4|Ex. §71.4]]; two of them have no integral surface: [[§59 Related Vector Fields#^ex-59-2|Ex. §59.2]].

> [!proof]+ Proof
> *(Assignment 8, Problem 2: the submitted solution. The commutators, which the assignment asks to check without submitting, the closedness in (3), and (4) are filled in.)*
>
> *The commutators.* Write $E_{ij}$ for the matrix with entry $1$ in place $(i, j)$ and $0$ elsewhere, so that $E_{ij}E_{kl} = E_{il}$ if $j = k$ and $E_{ij}E_{kl} = 0$ otherwise. Here $m_X = E_{12}$, $m_Y = E_{23}$, $m_Z = E_{13}$, and
>
> $$
> \begin{aligned}
> m_X m_Y &= E_{12}E_{23} = E_{13} = m_Z, \qquad m_Y m_X = E_{23}E_{12} = 0, \\
> m_X m_Z &= m_Z m_X = m_Y m_Z = m_Z m_Y = 0 .
> \end{aligned}
> $$
>
> So $[m_X, m_Y] = m_Z$ and $[m_X, m_Z] = [m_Y, m_Z] = 0$. The commutator is bilinear and antisymmetric, so the commutator of two elements of $\mathfrak{h}_3$ is a multiple of $m_Z$, in $\mathfrak{h}_3$.
>
> *(1).* Let $A = A(a, b, c)$. Multiplying out, the only nonzero entry of $A^2$ is the $(1, 3)$ entry $ab$, and $A^3 = A^2 A = 0$, since that entry lies in the third column and the third row of $A$ is zero. By Lemma [[§71 The Exponential Map#^lem-71-7|§71.7]](1),
>
> $$
> e^{A} = I + A + \tfrac12 A^2 = \begin{pmatrix} 1 & a & c + \frac{ab}{2} \\ 0 & 1 & b \\ 0 & 0 & 1 \end{pmatrix} = u\big( a,\ b,\ c + \tfrac{ab}{2} \big) \in H_3 .
> $$
>
> Conversely, for $x, y, z \in \mathbb{R}$ the matrix $A = A\big( x, y, z - \tfrac{xy}{2} \big)$ has $e^{A} = u\big( x,\ y,\ z - \tfrac{xy}{2} + \tfrac{xy}{2} \big) = u(x, y, z)$, and it is the only element of $\mathfrak{h}_3$ with this exponential, because $a = x$, $b = y$ and $c + \tfrac{ab}{2} = z$ determine $a$, $b$, $c$.
>
> *(2).* Multiplying the matrices,
>
> $$
> u(x, y, z)\, u(x', y', z') = u(x + x',\ y + y',\ z + z' + xy') . \tag{$\star$}
> $$
>
> So $H_3$ is closed under products, $I = u(0, 0, 0) \in H_3$, and by $(\star)$
>
> $$
> u(x, y, z)\, u(-x, -y, -z + xy) = u\big( 0,\ 0,\ z - z + xy - xy \big) = I ;
> $$
>
> these being square matrices, $u(x, y, z)^{-1} = u(-x, -y, -z + xy) \in H_3$. In particular the elements of $H_3$ are invertible, and $H_3$ is a subgroup of $\mathrm{GL}(3, \mathbb{R})$. If $u(x, y, z) = e^{A}$ with $A = A(a, b, c)$, then by (1) $e^{-A} = u\big( -a,\ -b,\ -c + \tfrac{ab}{2} \big)$, and $-c + \tfrac{ab}{2} = -\big(z - \tfrac{xy}{2}\big) + \tfrac{xy}{2} = -z + xy$: $e^{-A} = u(x, y, z)^{-1}$, as Lemma [[§71 The Exponential Map#^lem-71-6|§71.6]] says in general.
>
> *(3).* In the entry chart $(g_{ij})$ of $\mathrm{GL}(3, \mathbb{R})$, the restriction of the linear chart of $\operatorname{Mat}(3, \mathbb{R}) = \mathbb{R}^9$ to this open set,
>
> $$
> H_3 = \big\{\, g \in \mathrm{GL}(3, \mathbb{R}) : g_{11} = g_{22} = g_{33} = 1,\ g_{21} = g_{31} = g_{32} = 0 \,\big\} :
> $$
>
> a matrix with these six entries is $u(g_{12}, g_{23}, g_{13})$. So $H_3$ is cut out, in one chart whose domain is all of $\mathrm{GL}(3, \mathbb{R})$, by setting six of the nine coordinates equal to constants: it is a regular submanifold of codimension $6$, with induced chart the remaining three coordinates $(g_{12}, g_{23}, g_{13})|_{H_3}$ (Proposition [[§37 Regular Submanifolds#^prop-37-2|§37.2]], Proposition [[§37 Regular Submanifolds#^prop-37-3|§37.3]]). This chart is defined on all of $H_3$, has image $\mathbb{R}^3$, and its inverse is $u$; so $u : \mathbb{R}^3 \to H_3$ is a diffeomorphism (Proposition [[§28 Derivations and the Abstract Tangent Space#^prop-28-9|§28.9]]). $H_3$ is closed in $\mathrm{GL}(3, \mathbb{R})$, as the set where six continuous functions take prescribed values. Being a subgroup by (2), it is an embedded Lie subgroup (Proposition [[§61 Lie Group Morphisms and Linear Groups#^prop-61-4|§61.4]]).
>
> The submitted solution reaches the Lie group structure by hand, which shows what the proposition does in this case: in the chart $(x, y, z)$, by $(\star)$ and the formula for inverses, multiplication and inversion are the polynomial maps
>
> $$
> \big( (x, y, z), (x', y', z') \big) \mapsto (x + x',\ y + y',\ z + z' + xy'), \qquad (x, y, z) \mapsto (-x,\ -y,\ -z + xy) ,
> $$
>
> and the inclusion into $\mathrm{GL}(3, \mathbb{R})$ has the coordinate representation $(x, y, z) \mapsto (1, x, z, 0, 1, y, 0, 0, 1)$, whose Jacobian has the rows $(1, 0, 0)$, $(0, 1, 0)$, $(0, 0, 1)$ in the places of $g_{12}$, $g_{23}$, $g_{13}$ and zero rows elsewhere, of rank $3$: an immersion.
>
> *(4).* For $a, b, c \in \mathbb{R}$ the curve $t \mapsto u(ta, tb, tc)$ lies in $H_3$, passes through $I$ at $t = 0$, and its velocity there, as a matrix, is $A(a, b, c)$. So $\mathfrak{h}_3 \subseteq T_IH_3$, both regarded as subspaces of $\operatorname{Mat}(3, \mathbb{R})$, and both have dimension $3$: $T_IH_3 = \mathfrak{h}_3$. $H_3$ is a linear group and a Lie subgroup of $\mathrm{GL}(3, \mathbb{R})$, so its exponential map is $A \mapsto e^{A}$ (Theorem [[§71 The Exponential Map#^thm-71-12|§71.12]]). In the linear coordinates $(a, b, c)$ of $\mathfrak{h}_3$ and the chart $(x, y, z)$ of $H_3$ it is the map $(a, b, c) \mapsto \big( a, b, c + \tfrac{ab}{2} \big)$ of (1), polynomial with the polynomial inverse $(x, y, z) \mapsto \big( x, y, z - \tfrac{xy}{2} \big)$: a diffeomorphism.

^pf-ex-71-3

*Uses:* [[§71 The Exponential Map#^lem-71-7|§71.7]], [[§71 The Exponential Map#^lem-71-6|§71.6]], [[§37 Regular Submanifolds#^prop-37-2|§37.2]], [[§37 Regular Submanifolds#^prop-37-3|§37.3]], [[§28 Derivations and the Abstract Tangent Space#^prop-28-9|§28.9]], [[§61 Lie Group Morphisms and Linear Groups#^prop-61-4|§61.4]], [[§71 The Exponential Map#^thm-71-12|§71.12]]

For the Heisenberg group the exponential map is a diffeomorphism; for $\mathrm{SL}(2, \mathbb{R})$ it is not even surjective (Example [[§71 The Exponential Map#^ex-71-2|§71.2]]).

> [!theorem] Proposition §71.14: The Product of Two Exponentials in the Heisenberg Group
> For $A, B \in \mathfrak{h}_3$ (Example [[§71 The Exponential Map#^ex-71-3|§71.3]]),
>
> $$
> e^{A}\, e^{B} = e^{A + B + \frac12 [A, B]}, \qquad [A, B] = AB - BA .
> $$
>
> In coordinates: for $A = A(a, b, c)$ and $B = A(a', b', c')$, $[A, B] = (ab' - a'b)\, m_Z$ and
>
> $$
> e^{A(a, b, c)}\, e^{A(a', b', c')} = e^{A\left( a + a',\ b + b',\ c + c' + \frac12 (ab' - a'b) \right)} .
> $$
>
> So $e^{A} e^{B} = e^{A + B}$ exactly when $[A, B] = 0$.

^prop-71-14

> [!remark]- Connections
> - The same identity for operators whose commutator is a number, used for the coherent states of the harmonic oscillator: [[§B4.3 Coherent States#^der-b4-3-1|QM §B4.3.1, derivation]].
> - Two nilpotent matrices with $\exp(A + B) \neq \exp(A)\exp(B)$: [[§71 The Exponential Map#^ex-71-1|Ex. §71.1]].

> [!proof]+ Proof
> *(Not from the assignment; computed from Example [[§71 The Exponential Map#^ex-71-3|§71.3]].)* *The commutator.* By the relations of Example [[§71 The Exponential Map#^ex-71-3|§71.3]] and bilinearity, the only products of $m_X, m_Y, m_Z$ that do not vanish are $m_X m_Y = m_Z$; so $AB = ab'\, m_Z$, $BA = a'b\, m_Z$, and $[A, B] = (ab' - a'b)\, m_Z$. Hence $A + B + \tfrac12 [A, B] = A\big( a + a',\ b + b',\ c + c' + \tfrac12 (ab' - a'b) \big)$.
>
> *The two sides.* By parts (1) and (2) of the example,
>
> $$
> e^{A}\, e^{B} = u\big( a, b, c + \tfrac{ab}{2} \big)\, u\big( a', b', c' + \tfrac{a'b'}{2} \big) = u\big( a + a',\ b + b',\ c + c' + \tfrac{ab}{2} + \tfrac{a'b'}{2} + ab' \big) ,
> $$
>
> and by part (1),
>
> $$
> e^{A + B + \frac12 [A, B]} = u\Big( a + a',\ b + b',\ c + c' + \tfrac12 (ab' - a'b) + \tfrac12 (a + a')(b + b') \Big) .
> $$
>
> The last entries agree:
>
> $$
> \tfrac12 (ab' - a'b) + \tfrac12 (ab + ab' + a'b + a'b') = \tfrac{ab}{2} + \tfrac{a'b'}{2} + ab' .
> $$
>
> *The last sentence.* The exponential is injective on $\mathfrak{h}_3$ (Example [[§71 The Exponential Map#^ex-71-3|§71.3]](1)), so $e^{A + B + \frac12 [A, B]} = e^{A + B}$ exactly when $\tfrac12 [A, B] = 0$.

^pf-71-14

*Uses:* [[§71 The Exponential Map#^ex-71-3|Ex. §71.3]]

This is the correction to the false rule $\exp(A + B) = \exp(A)\exp(B)$ of the remark *Warning: $\exp(A + B) \neq \exp(A)\exp(B)$ in General*: in the Heisenberg group the first correction term $\tfrac12 [A, B]$ is the only one.

> [!example] Example §71.4: Left-Invariant Fields on the Heisenberg Group
> *(Not from the assignment; it connects Problems 2 and 5.)* On $H_3$ use the global chart $(a, b, c)$, the inverse of the diffeomorphism $(a, b, c) \mapsto e^{A(a, b, c)}$ of Example [[§71 The Exponential Map#^ex-71-3|§71.3]](4) (*exponential coordinates*). In this chart the identity is $(0, 0, 0)$, the product is
>
> $$
> (a, b, c) \cdot (a', b', c') = \big( a + a',\ b + b',\ c + c' + \tfrac12 (ab' - a'b) \big) ,
> $$
>
> and the left-invariant vector fields with the values $m_X$, $m_Y$, $m_Z$ at the identity are
>
> $$
> \mathbf{X} = \frac{\partial}{\partial a} - \frac{b}{2}\, \frac{\partial}{\partial c}, \qquad \mathbf{Y} = \frac{\partial}{\partial b} + \frac{a}{2}\, \frac{\partial}{\partial c}, \qquad \mathbf{Z} = \frac{\partial}{\partial c} .
> $$
>
> They satisfy $[\mathbf{X}, \mathbf{Y}] = \mathbf{Z}$ and $[\mathbf{X}, \mathbf{Z}] = [\mathbf{Y}, \mathbf{Z}] = 0$, the relations of the matrices $m_X$, $m_Y$, $m_Z$, as Theorem [[§61 Lie Group Morphisms and Linear Groups#^thm-61-7|§61.7]] requires. With $(a, b, c)$ renamed $(x, y, z)$, $\mathbf{X}$ and $\mathbf{Y}$ are the two fields of Example [[§59 Related Vector Fields#^ex-59-2|§59.2]].

^ex-71-4

> [!proof]+ Proof
> *The product* is Proposition [[§71 The Exponential Map#^prop-71-14|§71.14]], read in the chart.
>
> *The fields.* Fix $g = (a, b, c)$. In the chart, left translation is $L_g(a', b', c') = \big( a + a',\ b + b',\ c + c' + \tfrac12 (ab' - a'b) \big)$, an affine map of $\mathbb{R}^3$ with Jacobian matrix
>
> $$
> \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ -\frac{b}{2} & \frac{a}{2} & 1 \end{pmatrix}
> $$
>
> at every point. Its columns are the images of $\partial_a|_e$, $\partial_b|_e$, $\partial_c|_e$ under $d(L_g)_e$; so the left-invariant extensions of these three vectors (Definition [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-5|§60.5]]) are $\mathbf{X}$, $\mathbf{Y}$, $\mathbf{Z}$. The vector $\partial_a|_e$ is the velocity at $0$ of the curve $t \mapsto e^{A(t, 0, 0)} = I + t\, m_X$, which as a matrix is $m_X$; likewise $\partial_b|_e$ and $\partial_c|_e$ are $m_Y$ and $m_Z$.
>
> *The brackets.* By Proposition [[§58 Lie Bracket and Lie Algebra#^prop-58-2|§58.2]], the $\partial_a$ and $\partial_b$ components of $[\mathbf{X}, \mathbf{Y}]$ vanish, the corresponding coefficients being constant, and its $\partial_c$ component is $\mathbf{X}\big( \tfrac{a}{2} \big) - \mathbf{Y}\big( -\tfrac{b}{2} \big) = \tfrac12 + \tfrac12 = 1$. The coefficients of $\mathbf{X}$ and $\mathbf{Y}$ do not depend on $c$ and those of $\mathbf{Z}$ are constant, so $[\mathbf{X}, \mathbf{Z}] = [\mathbf{Y}, \mathbf{Z}] = 0$.

^pf-ex-71-4

*Uses:* [[§71 The Exponential Map#^prop-71-14|§71.14]], [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-5|Def. §60.5]], [[§58 Lie Bracket and Lie Algebra#^prop-58-2|§58.2]]

So the two fields with no integral surface are left-invariant fields of a Lie group, and the reason found in Example [[§59 Related Vector Fields#^ex-59-2|§59.2]], $[\mathbf{X}, \mathbf{Y}] \notin \operatorname{Span}\{\mathbf{X}, \mathbf{Y}\}$, is the statement that $\operatorname{Span}\{m_X, m_Y\}$ is not a Lie subalgebra of $\mathfrak{h}_3$.

The classical groups through the course: defined in [[§11 Topological Groups and Classical Matrix Groups|Topological Groups and Classical Matrix Groups]], with the examples of [[§16 The Classical Groups|The Classical Groups]]; topological manifolds as level sets in [[§12 The Classical Groups Are Topological Manifolds#^thm-12-6|Classical Groups Are Manifolds]]; $\mathrm{SO}(2)$ and $\mathrm{SO}(3)$ acting on $\mathbb{R}^2$ and $\mathbb{R}^3$ in [[§13 Group Actions and Orbit Spaces#^ex-13-6|the rotations of the plane]] and [[§13 Group Actions and Orbit Spaces#^ex-13-7|the rotations of space]], and $\mathrm{SO}(3)$ on $S^2$ in [[§14 Homogeneous Spaces#^ex-14-2|the isotropy of the north pole]] and [[§14 Homogeneous Spaces#^ex-14-5|the sphere as a homogeneous space]]; $\mathrm{O}(n)$ acting on the Grassmannians in [[§15 The Topology of G∕H and Real Grassmannians#^cor-15-8|Grassmannians as Homogeneous Spaces]]; smooth manifolds in [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-23-1|the orthogonal group]] and [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-23-3|the unitary group]]; their tangent spaces at the identity in [[§25 The Geometric Tangent Space#^thm-25-5|The Classical Groups]], with [[§25 The Geometric Tangent Space#^ex-25-4|the infinitesimal rotations]]; the double cover $\mathrm{SU}(2) \to \mathrm{SO}(3)$ in [[§44 SU(2) → SO(3)꞉ The Double Cover#^thm-44-5|The Double Cover]]; the Lie algebra $\mathfrak{so}(3)$ and the cross product in [[§58 Lie Bracket and Lie Algebra#^ex-58-3|Ex. §58.3]]; Lie groups in [[§60 Lie Groups and Left-Invariant Vector Fields#^prop-60-1|§60.1]]; and $\mathrm{SL}(2, \mathbb{R})$ factored as $\mathrm{SO}(2) \cdot A \cdot N$, hence diffeomorphic to $S^1 \times \mathbb{R}^2$, in Proposition [[§71 The Exponential Map#^prop-71-15|§71.15]] below.

> [!example] Example §71.5: Three One-Parameter Subgroups of $\mathrm{SL}({2,\mathbb{R}})$
> In $\mathfrak{sl}(2, \mathbb{R}) = \{ A \in \operatorname{Mat}(2, \mathbb{R}) : \operatorname{tr} A = 0 \}$ (Theorem [[§25 The Geometric Tangent Space#^thm-25-5|§25.5]]) consider the three lines
>
> $$
> \mathfrak{k} = \Big\{ \begin{pmatrix} 0 & -\theta \\ \theta & 0 \end{pmatrix} : \theta \in \mathbb{R} \Big\}, \qquad
> \mathfrak{a} = \Big\{ \begin{pmatrix} \lambda & 0 \\ 0 & -\lambda \end{pmatrix} : \lambda \in \mathbb{R} \Big\}, \qquad
> \mathfrak{n} = \Big\{ \begin{pmatrix} 0 & b \\ 0 & 0 \end{pmatrix} : b \in \mathbb{R} \Big\} ,
> $$
>
> where $\mathfrak{k} = T_I\mathrm{SO}(2)$ is the Lie algebra of $\mathrm{SO}(2)$ (Example [[§41 Embeddings#^ex-41-3|§41.3]](4)).
>
> 1. $\mathfrak{sl}(2, \mathbb{R}) = \mathfrak{k} \oplus \mathfrak{a} \oplus \mathfrak{n}$ as vector spaces.
> 2. The exponentials of the three lines are
>
> $$
> \begin{aligned}
> &\exp\begin{pmatrix} 0 & -\theta \\ \theta & 0 \end{pmatrix} = R(\theta), \\
> &\exp\begin{pmatrix} \lambda & 0 \\ 0 & -\lambda \end{pmatrix} = \begin{pmatrix} e^{\lambda} & 0 \\ 0 & e^{-\lambda} \end{pmatrix} =: a(\lambda), \qquad
> \exp\begin{pmatrix} 0 & b \\ 0 & 0 \end{pmatrix} = \begin{pmatrix} 1 & b \\ 0 & 1 \end{pmatrix} =: n(b) ,
> \end{aligned}
> $$
>
> with $R(\theta)$ the rotation of Example [[§41 Embeddings#^ex-41-3|§41.3]].
>
> 3. $K = \exp(\mathfrak{k}) = \mathrm{SO}(2)$, $A = \exp(\mathfrak{a}) = \big\{ \begin{psmallmatrix} s & 0 \\ 0 & s^{-1} \end{psmallmatrix} : s > 0 \big\}$ and $N = \exp(\mathfrak{n}) = \{ n(b) : b \in \mathbb{R} \}$ are subgroups of $\mathrm{SL}(2, \mathbb{R})$, with $a(\lambda)\, a(\lambda') = a(\lambda + \lambda')$ and $n(b)\, n(b') = n(b + b')$.
> 4. $\exp : \mathfrak{a} \to A$ and $\exp : \mathfrak{n} \to N$ are bijections. $A$ and $N$ are regular submanifolds of $\mathrm{SL}(2, \mathbb{R})$ of dimension $1$, with the global charts $g \mapsto \log g_{11}$ on $A$ and $g \mapsto g_{12}$ on $N$, for which these exponentials are diffeomorphisms. So $A$ and $N$ are embedded Lie subgroups of $\mathrm{SL}(2, \mathbb{R})$ (Proposition [[§61 Lie Group Morphisms and Linear Groups#^prop-61-4|§61.4]]), and $\lambda \mapsto a(\lambda)$, $b \mapsto n(b)$ are isomorphisms of Lie groups from $(\mathbb{R}, +)$.

^ex-71-5

> [!proof]+ Proof
> *(Assignment 8, Problem 3(a) and (b): the submitted solution. The exponential of $\mathfrak{k}$ in (2) is not from the assignment.)*
>
> *(1).* Every matrix in $\mathfrak{k}$, $\mathfrak{a}$ and $\mathfrak{n}$ has trace zero, so these are subspaces of $\mathfrak{sl}(2, \mathbb{R})$, each of dimension $1$. A general element of $\mathfrak{k} + \mathfrak{a} + \mathfrak{n}$ is
>
> $$
> \begin{pmatrix} 0 & -\theta \\ \theta & 0 \end{pmatrix} + \begin{pmatrix} \lambda & 0 \\ 0 & -\lambda \end{pmatrix} + \begin{pmatrix} 0 & b \\ 0 & 0 \end{pmatrix} = \begin{pmatrix} \lambda & -\theta + b \\ \theta & -\lambda \end{pmatrix} .
> $$
>
> Suppose two such sums, with parameters $(\theta, \lambda, b)$ and $(\theta', \lambda', b')$, are equal. The $(1, 1)$ entries give $\lambda = \lambda'$, the $(2, 1)$ entries give $\theta = \theta'$, and then the $(1, 2)$ entries give $-\theta + b = -\theta' + b'$, so $b = b'$. So every element of the sum has a unique such representation: the sum is direct, of dimension $1 + 1 + 1 = 3 = \dim \mathfrak{sl}(2, \mathbb{R})$ (the traceless $2 \times 2$ matrices $\begin{psmallmatrix} p & q \\ r & -p \end{psmallmatrix}$ have three free entries), and a subspace of full dimension is the whole space.
>
> *(2).* $\mathrm{SL}(2, \mathbb{R})$ is a linear group and a Lie subgroup of $\mathrm{GL}(2, \mathbb{R})$, so its exponential map is the matrix exponential (Theorem [[§71 The Exponential Map#^thm-71-12|§71.12]]; this rests on Assignment 7, Problem 5). The second and third formulas are Lemma [[§71 The Exponential Map#^lem-71-7|§71.7]]: (2) for the diagonal matrix, and (1) with $k = 2$ for $\begin{psmallmatrix} 0 & b \\ 0 & 0 \end{psmallmatrix}$, whose square is $0$. For the first, $J = \begin{psmallmatrix} 0 & -1 \\ 1 & 0 \end{psmallmatrix}$ has $J^2 = -I$, so $(\theta J)^{2k} = (-1)^k \theta^{2k} I$ and $(\theta J)^{2k+1} = (-1)^k \theta^{2k+1} J$; splitting the series, which converges absolutely in every entry, into even and odd terms,
>
> $$
> e^{\theta J} = \Big( \sum_{k \ge 0} \frac{(-1)^k \theta^{2k}}{(2k)!} \Big) I + \Big( \sum_{k \ge 0} \frac{(-1)^k \theta^{2k+1}}{(2k+1)!} \Big) J = \cos\theta\, I + \sin\theta\, J = R(\theta) .
> $$
>
> *(3).* By (2) and Example [[§41 Embeddings#^ex-41-3|§41.3]](1), $\exp(\mathfrak{k}) = \{ R(\theta) \} = \mathrm{SO}(2)$; the description of $A$ follows from (2) with $s = e^{\lambda}$, which takes every positive value. All these matrices have determinant $1$. Multiplying the matrices,
>
> $$
> \begin{aligned}
> a(0) &= I, & a(\lambda)\, a(\lambda') &= a(\lambda + \lambda'), & a(\lambda)\, a(-\lambda) &= I , \\
> n(0) &= I, & n(b)\, n(b') &= n(b + b'), & n(b)\, n(-b) &= I .
> \end{aligned}
> $$
>
> So $A$ and $N$ contain $I$ and are closed under products and inverses: they are subgroups of $\mathrm{SL}(2, \mathbb{R})$, as is $\mathrm{SO}(2)$.
>
> *(4), bijections.* $\lambda \mapsto a(\lambda)$ and $b \mapsto n(b)$ are onto $A$ and $N$ by definition, and injective: if $a(\lambda) = a(\lambda')$, the $(1, 1)$ entries give $e^{\lambda} = e^{\lambda'}$, so $\lambda = \lambda'$; if $n(b) = n(b')$, the $(1, 2)$ entries give $b = b'$.
>
> *(4), embeddings into $\operatorname{Mat}(2, \mathbb{R})$.* The maps $a, n : \mathbb{R} \to \operatorname{Mat}(2, \mathbb{R})$ are smooth, with entries $e^{\pm\lambda}$, $0$, $1$, $b$. The functions
>
> $$
> L_A : \{ g \in \operatorname{Mat}(2, \mathbb{R}) : g_{11} > 0 \} \to \mathbb{R}, \quad L_A(g) = \log g_{11}, \qquad L_N : \operatorname{Mat}(2, \mathbb{R}) \to \mathbb{R}, \quad L_N(g) = g_{12} ,
> $$
>
> are smooth on open subsets of $\operatorname{Mat}(2, \mathbb{R})$ containing $A$ and $N$, and $L_A(a(\lambda)) = \log e^{\lambda} = \lambda$, $L_N(n(b)) = b$. By Lemma [[§41 Embeddings#^lem-41-6|§41.6]](2), $a$ and $n$ are embeddings. (Directly, as in the submitted solution: the derivatives $(e^{\lambda}, 0, 0, -e^{-\lambda})$ and $(0, 1, 0, 0)$ of their coordinate representations never vanish, so they are immersions; and the inverses $a^{-1} = L_A|_A$, $n^{-1} = L_N|_N$ are restrictions of continuous functions.) So $A$ and $N$ are regular submanifolds of $\operatorname{Mat}(2, \mathbb{R})$ of dimension $1$ (Theorem [[§41 Embeddings#^thm-41-1|§41.1]]), and $a : \mathbb{R} \to A$, $n : \mathbb{R} \to N$ are diffeomorphisms (Corollary [[§41 Embeddings#^cor-41-3|§41.3]]); their inverses $\log g_{11}$ and $g_{12}$ are global charts (Lemma [[§36 Submersions#^lem-36-5|§36.5]]).
>
> *(4), into $\mathrm{SL}(2, \mathbb{R})$.* $\mathrm{SL}(2, \mathbb{R}) = \det^{-1}(1)$ is a regular submanifold of $\operatorname{Mat}(2, \mathbb{R})$ (Corollary [[§12 The Classical Groups Are Topological Manifolds#^cor-12-3|§12.3]], Theorem [[§38 The Regular Value Theorem for Manifolds#^thm-38-2|§38.2]]), and $A, N \subseteq \mathrm{SL}(2, \mathbb{R})$. So $A$ and $N$ are regular submanifolds of $\mathrm{SL}(2, \mathbb{R})$, with the same smooth structures (Corollary [[§41 Embeddings#^cor-41-8|§41.8]]; the submitted solution argues through the inclusions, as in Lemma [[§41 Embeddings#^lem-41-7|§41.7]]). Being subgroups, they are embedded Lie subgroups (Proposition [[§61 Lie Group Morphisms and Linear Groups#^prop-61-4|§61.4]]). The diffeomorphisms $a$ and $n$ are group morphisms from $(\mathbb{R}, +)$ by (3), with smooth inverses: isomorphisms of Lie groups.

^pf-ex-71-5

*Uses:* [[§71 The Exponential Map#^thm-71-12|§71.12]], [[§71 The Exponential Map#^lem-71-7|§71.7]], [[§41 Embeddings#^ex-41-3|Ex. §41.3]], [[§41 Embeddings#^lem-41-6|§41.6]], [[§41 Embeddings#^thm-41-1|§41.1]], [[§41 Embeddings#^cor-41-3|§41.3]], [[§36 Submersions#^lem-36-5|§36.5]], [[§12 The Classical Groups Are Topological Manifolds#^cor-12-3|§12.3]], [[§38 The Regular Value Theorem for Manifolds#^thm-38-2|§38.2]], [[§41 Embeddings#^cor-41-8|§41.8]], [[§41 Embeddings#^lem-41-7|§41.7]], [[§61 Lie Group Morphisms and Linear Groups#^prop-61-4|§61.4]]

> [!theorem] Proposition §71.15: The Iwasawa Decomposition of $\mathrm{SL}({2,\mathbb{R}})$
> With $K = \mathrm{SO}(2)$, $A$ and $N$ as in Example [[§71 The Exponential Map#^ex-71-5|§71.5]], the map
>
> $$
> \Phi : K \times A \times N \longrightarrow \mathrm{SL}(2, \mathbb{R}), \qquad \Phi(k, a, n) = kan ,
> $$
>
> is a diffeomorphism. Its inverse is
>
> $$
> \Phi^{-1}(g) = \left( \frac{1}{r}\begin{pmatrix} g_{11} & -g_{21} \\ g_{21} & g_{11} \end{pmatrix},\ \begin{pmatrix} r & 0 \\ 0 & r^{-1} \end{pmatrix},\ \begin{pmatrix} 1 & \frac{g_{11}g_{12} + g_{21}g_{22}}{r^2} \\ 0 & 1 \end{pmatrix} \right), \qquad r = \sqrt{g_{11}^2 + g_{21}^2} .
> $$
>
> $\Phi$ is not a group morphism from the product group $K \times A \times N$.

^prop-71-15

> [!remark]- Connections
> - The inverse is the Gram–Schmidt procedure, and $g = k \cdot (an)$ is the QR factorization: [[§21 Orthonormal Bases#^ladr-6-32|LADR 6.32]], [[§26 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-58|LADR 7.58]].
> - The factor $K = \mathrm{SO}(2)$ as a manifold: [[§41 Embeddings#^ex-41-3|Ex. §41.3]].

> [!proof]+ Proof
> *(Assignment 8, Problem 3(c): the submitted solution.)* By Examples [[§41 Embeddings#^ex-41-3|§41.3]] and [[§71 The Exponential Map#^ex-71-5|§71.5]], $K$, $A$, $N$ are $1$-dimensional regular submanifolds of $\operatorname{Mat}(2, \mathbb{R})$, so $K \times A \times N$ is a $3$-dimensional manifold (Definition [[§19 Smooth Functions and Smooth Maps#^def-19-8|§19.8]]), and $\dim \mathrm{SL}(2, \mathbb{R}) = 3$.
>
> *$\Phi$ is smooth.* Matrix multiplication $\operatorname{Mat}(2, \mathbb{R})^3 \to \operatorname{Mat}(2, \mathbb{R})$, $(X, Y, Z) \mapsto XYZ$, is smooth, since each entry of $XYZ$ is a polynomial in the $12$ entries of $X$, $Y$, $Z$. The inclusions of $K$, $A$, $N$ into $\operatorname{Mat}(2, \mathbb{R})$ are smooth (Lemma [[§37 Regular Submanifolds#^lem-37-5|§37.5]](1)), so their product $K \times A \times N \to \operatorname{Mat}(2, \mathbb{R})^3$ is smooth, as in the proof of Proposition [[§61 Lie Group Morphisms and Linear Groups#^prop-61-4|§61.4]]. So $\Phi$ is smooth as a map into $\operatorname{Mat}(2, \mathbb{R})$. Since $\det(kan) = \det k \det a \det n = 1$, it has values in the regular submanifold $\mathrm{SL}(2, \mathbb{R})$, so it is smooth as a map into $\mathrm{SL}(2, \mathbb{R})$ (Lemma [[§37 Regular Submanifolds#^lem-37-5|§37.5]](2)).
>
> *$\Phi$ is bijective.* For $\theta, \lambda, b \in \mathbb{R}$ write $c = \cos\theta$, $s = \sin\theta$, $u_1 = (c, s)^{\mathsf T}$, $u_2 = (-s, c)^{\mathsf T}$. Then
>
> $$
> R(\theta)\, a(\lambda)\, n(b) = \begin{pmatrix} c & -s \\ s & c \end{pmatrix} \begin{pmatrix} e^{\lambda} & 0 \\ 0 & e^{-\lambda} \end{pmatrix} \begin{pmatrix} 1 & b \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} e^{\lambda} c & e^{\lambda} c b - e^{-\lambda} s \\ e^{\lambda} s & e^{\lambda} s b + e^{-\lambda} c \end{pmatrix} ,
> $$
>
> whose first column is $e^{\lambda} u_1$ and whose second column is $e^{\lambda} b\, u_1 + e^{-\lambda} u_2$. Let $g \in \mathrm{SL}(2, \mathbb{R})$; we solve $R(\theta)\, a(\lambda)\, n(b) = g$.
>
> *First column.* The equation $(g_{11}, g_{21})^{\mathsf T} = e^{\lambda} u_1$, with $|u_1| = 1$ and $e^{\lambda} > 0$, forces, taking lengths,
>
> $$
> e^{\lambda} = r = \sqrt{g_{11}^2 + g_{21}^2}, \qquad (c, s) = \frac{1}{r}\, (g_{11}, g_{21}) .
> $$
>
> Here $r > 0$, since the first column of the invertible matrix $g$ is nonzero. So $\lambda = \log r$ is determined, and $(c, s)$ is a determined unit vector, so $k = R(\theta)$ is a determined element of $K$.
>
> *Second column.* Since $u_1, u_2$ is an orthonormal basis of $\mathbb{R}^2$, the equation $(g_{12}, g_{22})^{\mathsf T} = e^{\lambda} b\, u_1 + e^{-\lambda} u_2$ holds if and only if its components along $u_1$ and $u_2$ agree. The $u_1$-component gives
>
> $$
> c\, g_{12} + s\, g_{22} = e^{\lambda} b, \qquad \text{so} \qquad b = \frac{c\, g_{12} + s\, g_{22}}{r} = \frac{g_{11} g_{12} + g_{21} g_{22}}{g_{11}^2 + g_{21}^2} ,
> $$
>
> which determines $b$. The $u_2$-component requires $-s\, g_{12} + c\, g_{22} = e^{-\lambda}$, and this holds:
>
> $$
> -s\, g_{12} + c\, g_{22} = \frac{g_{11} g_{22} - g_{21} g_{12}}{r} = \frac{\det g}{r} = \frac{1}{r} = e^{-\lambda} .
> $$
>
> So $kan = g$ has exactly one solution $(k, a, n) \in K \times A \times N$, the one of the statement: $\Phi$ is bijective, with the inverse displayed there.
>
> *$\Phi^{-1}$ is smooth.* On the open set $W = \{ g \in \operatorname{Mat}(2, \mathbb{R}) : g_{11}^2 + g_{21}^2 > 0 \}$, which contains $\mathrm{SL}(2, \mathbb{R})$, each of the three components of the displayed formula is a smooth map into $\operatorname{Mat}(2, \mathbb{R})$, since $r = \sqrt{g_{11}^2 + g_{21}^2}$ is smooth and positive on $W$. Restricted to $\mathrm{SL}(2, \mathbb{R})$ they are smooth (Lemma [[§37 Regular Submanifolds#^lem-37-5|§37.5]](1)) and take values in the regular submanifolds $K$, $A$, $N$ of $\operatorname{Mat}(2, \mathbb{R})$, so they are smooth as maps into $K$, $A$, $N$ (Lemma [[§37 Regular Submanifolds#^lem-37-5|§37.5]](2)). A map into a product manifold is smooth when its components are (as in the proof of Proposition [[§61 Lie Group Morphisms and Linear Groups#^prop-61-4|§61.4]]). So $\Phi^{-1}$ is smooth, and $\Phi$ is a diffeomorphism.
>
> *$\Phi$ is not a group morphism.* Let $k = R(\tfrac{\pi}{2}) = \begin{psmallmatrix} 0 & -1 \\ 1 & 0 \end{psmallmatrix} \in K$ and $n = n(1) = \begin{psmallmatrix} 1 & 1 \\ 0 & 1 \end{psmallmatrix} \in N$. In the product group, $(I, I, n)\,(k, I, I) = (k, I, n)$, so
>
> $$
> \Phi\big( (I, I, n)\,(k, I, I) \big) = kn = \begin{pmatrix} 0 & -1 \\ 1 & 1 \end{pmatrix}, \qquad \Phi(I, I, n)\, \Phi(k, I, I) = nk = \begin{pmatrix} 1 & -1 \\ 1 & 0 \end{pmatrix} .
> $$
>
> These differ.

^pf-71-15

*Uses:* [[§41 Embeddings#^ex-41-3|Ex. §41.3]], [[§71 The Exponential Map#^ex-71-5|Ex. §71.5]], [[§19 Smooth Functions and Smooth Maps#^def-19-8|Def. §19.8]], [[§37 Regular Submanifolds#^lem-37-5|§37.5]], [[§61 Lie Group Morphisms and Linear Groups#^prop-61-4|§61.4]]

The inverse is the Gram–Schmidt process applied to the columns $g_1, g_2$ of $g$: $u_1 = g_1/|g_1|$ and the unit vector $u_2$ orthogonal to it are the columns of $k$, $r = |g_1|$ is the stretch, and $g_2 = r b\, u_1 + r^{-1} u_2$. In other words $g = k \cdot (an)$ is the factorization of $g$ into a rotation and an upper triangular matrix with positive diagonal (the $QR$ factorization). The decomposition generalizes to many other groups, under the name *Iwasawa decomposition*.

![[m591-77-2.svg]]

*(Not from lecture; figure added.)* The factorization $g = kan$ of Proposition [[§71 The Exponential Map#^prop-71-15|§71.15]], for $\theta = 35^\circ$, $\lambda = 0.4$, $b = 0.8$, read from right to left on the unit square: $n$ shears it, $a$ stretches it by $e^{\lambda}$ horizontally and by $e^{-\lambda}$ vertically, and $k$ rotates it by $\theta$. All four parallelograms have area $1$. In the last panel the edges are the columns $g_1$ (blue) and $g_2$ (red) of $g$, and Gram–Schmidt reads the factors back: $u_1 = g_1/|g_1|$ gives $k$, $|g_1| = e^{\lambda}$ gives $a$, and the component $e^{\lambda} b$ of $g_2$ along $u_1$ gives $n$; its component along $u_2$ is then $e^{-\lambda}$, because $\det g = 1$.

![[m591-77-a2.gif|520]]

*(Not from lecture; animation added, vault only.)* The three factors of $g = kan$ acting one after the other on the unit square, for the values of the figure: the shear $n$, the stretch $a$, the rotation $k$. The area stays $1$ throughout; at the end the blue and red edges are the columns $g_1$, $g_2$ of $g$.

> [!theorem] Corollary §71.16: $\mathrm{SL}({2,\mathbb{R}})$ Is Diffeomorphic to $S^1 \times \mathbb{R}^2$
> The map
>
> $$
> S^1 \times \mathbb{R} \times \mathbb{R} \longrightarrow \mathrm{SL}(2, \mathbb{R}), \qquad \big( (c, s), \lambda, b \big) \longmapsto \begin{pmatrix} c & -s \\ s & c \end{pmatrix} \begin{pmatrix} e^{\lambda} & 0 \\ 0 & e^{-\lambda} \end{pmatrix} \begin{pmatrix} 1 & b \\ 0 & 1 \end{pmatrix} ,
> $$
>
> is a diffeomorphism: $\mathrm{SL}(2, \mathbb{R})$ is diffeomorphic to $S^1 \times \mathbb{R}^2$, an open solid torus. In particular $\mathrm{SL}(2, \mathbb{R})$ is connected, and it is not compact.

^cor-71-16

> [!remark]- Connections
> - $\mathrm{GL}(n, \mathbb{R})$ has exactly two components: [[§16 The Classical Groups#^thm-16-2|§16.2]].
> - Connected, and still $\exp$ is not surjective: [[§71 The Exponential Map#^ex-71-2|Ex. §71.2]].

> [!proof]+ Proof
> *(Assignment 8, Problem 3(c): the submitted solution; connectedness and non-compactness are filled in.)* The map is the composite of $\Phi$ (Proposition [[§71 The Exponential Map#^prop-71-15|§71.15]]) with the product of the three diffeomorphisms $S^1 \to K$ (Example [[§41 Embeddings#^ex-41-3|§41.3]](5)), $\lambda \mapsto a(\lambda)$ and $b \mapsto n(b)$ (Example [[§71 The Exponential Map#^ex-71-5|§71.5]](4)). A product of diffeomorphisms is a diffeomorphism: it and its inverse are smooth, their components being smooth.
>
> *Connected.* $S^1 \times \mathbb{R}^2$ is the image of $\mathbb{R}^3$ under the continuous map $(\theta, \lambda, b) \mapsto \big( (\cos\theta, \sin\theta), \lambda, b \big)$; $\mathbb{R}^3$ is connected and the continuous image of a connected space is connected (Proposition [[§1 Point-Set Topology Review#^prop-1-7|§1.7]](4) and (1)). A diffeomorphism is a homeomorphism, so $\mathrm{SL}(2, \mathbb{R})$ is connected.
>
> *Not compact.* $\mathrm{SL}(2, \mathbb{R})$ carries the subspace topology of $\operatorname{Mat}(2, \mathbb{R}) = \mathbb{R}^4$ and contains $n(b)$ for every $b \in \mathbb{R}$, so it is not bounded; by the Heine–Borel theorem (Proposition [[§1 Point-Set Topology Review#^prop-1-8|§1.8]](1)) it is not compact.

^pf-71-16

*Uses:* [[§71 The Exponential Map#^prop-71-15|§71.15]], [[§41 Embeddings#^ex-41-3|Ex. §41.3]], [[§71 The Exponential Map#^ex-71-5|Ex. §71.5]], [[§1 Point-Set Topology Review#^prop-1-7|§1.7]], [[§1 Point-Set Topology Review#^prop-1-8|§1.8]]

So every element of $\mathrm{SL}(2, \mathbb{R})$ is a product $e^{\theta J}\, e^{\lambda H}\, e^{bE}$ of three exponentials, with $J = \begin{psmallmatrix} 0 & -1 \\ 1 & 0 \end{psmallmatrix}$, $H = \begin{psmallmatrix} 1 & 0 \\ 0 & -1 \end{psmallmatrix}$, $E = \begin{psmallmatrix} 0 & 1 \\ 0 & 0 \end{psmallmatrix}$, although not every element is a single exponential: the matrix $\begin{psmallmatrix} -1 & 1 \\ 0 & -1 \end{psmallmatrix}$ of Example [[§71 The Exponential Map#^ex-71-2|§71.2]] is $R(\pi)\, a(0)\, n(-1)$.

The term exponential map comes up again in Riemannian geometry (MATH 635), for any manifold with a Riemannian structure. There, a tangent vector is the initial data of a geodesic, which one follows to time $1$. To exponentiate geometrically one needs a way of launching a curve from a tangent vector: here the one-parameter subgroups do this, in Riemannian geometry the geodesics. Next topic: Lie derivatives.
