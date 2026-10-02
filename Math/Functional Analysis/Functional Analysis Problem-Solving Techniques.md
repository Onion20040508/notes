---
type: summary
subject: "[[Functional Analysis]]"
tags: [functional-analysis, math556]
---
↑ [[Functional Analysis]]

# Problem-Solving Techniques

This appendix distills the recurring proof strategies from homework problems in the course. It is organized by technique rather than by topic.

## Technique 1: Well-Definedness on Quotients

Any operation on $X/Y$ defined through representatives must be shown independent of the representative before anything else is proved.

> [!remark] Remark: Strategy
> To show $[x] \mapsto F(x)$ is well defined on $X/Y$: take $[x] = [x']$, i.e. $x - x' \in Y$, and show $F(x) = F(x')$. For operations built from those of $X$, the difference of the two candidate outputs is a linear combination of elements of $Y$, hence in $Y$ by closure. Only after this do the axioms or other properties get checked, and then each follows by “definition $\to$ axiom of $X$ $\to$ definition.”

^rem-t1

> [!example] Example T1: Applications (HW1)
> - **$X/Y$ is a linear space**: $[x_1]+[x_2] := [x_1+x_2]$ and $a[x] := [ax]$ are well defined because $(x_1+x_2)-(x_1'+x_2') = (x_1-x_1')+(x_2-x_2') \in Y$ and $ax - ax' = a(x-x') \in Y$; each axiom then transfers from $X$ in one line.
> - **Surjectivity of $X \to X/Y \oplus Y$**: to hit $([x], y)$, replace $x$ by the representative $w$ of its class lying in the complement $W$; $[w] = [x]$ since $x - w \in Y$.

^ex-t1

## Technique 2: Trivial Intersection Gives Uniqueness

> [!remark] Remark: Strategy
> To show a representation $x = w + y$ ($w \in W$, $y \in Y$) is unique, or that a map reading off components is injective: subtract two representations. The difference $w_1 - w_2 = y_2 - y_1$ lies in $W \cap Y$; if that is $\{0\}$, both differences vanish. The same argument shows $[w_1] = [w_2]$ in $X/Y$ forces $w_1 = w_2$ for $w_i \in W$.

^rem-t2

> [!example] Example T2: Applications (HW1)
> - **Unique decomposition** for a complement $W$ of $Y$ (Lemma [[§1 Linear Spaces#^lem-1-10|§1.10]]).
> - **Injectivity of $M : X \to X/Y \oplus Y$** and of $W \to X/Y$, $w \mapsto [w]$ (Theorem [[§1 Linear Spaces#^thm-1-11|§1.11]], Corollary [[§1 Linear Spaces#^cor-1-12|§1.12]]).

^ex-t2

## Technique 3: One-Step Enlargement plus Zorn

The pattern of the [[§3 Statement and Motivation#^thm-3-2|Hahn–Banach]] proof, reusable whenever a maximal object with a closure property is needed.

> [!remark] Remark: Strategy
> - (i) **One-step lemma**: show that if the desired property holds for an object $W$ and $W$ is not yet “full,” there is a strictly larger $W'$ with the same property. This is where the actual mathematics lives.
> - (ii) **Poset**: let $P$ be the set of all objects with the property, ordered by inclusion/extension. Check $P \neq \varnothing$ and that chains have upper bounds — usually the union of the chain, with the property inherited because it holds member-by-member and any finitely many elements of the union lie in a single member.
> - (iii) **Maximal element**: [[§4 Proof of the Hahn–Banach Theorem#^thm-4-2|Zorn]] gives one; the one-step lemma shows it must be full.
>
> In finite dimensions replace (ii)–(iii) by iterating (i) finitely many times.

^rem-t3

> [!example] Example T3: Applications
> - **Hahn–Banach** (lecture): objects are pairs $(Z, \ell_Z)$ with $\ell_Z \le p$; one-step lemma is Lemma [[§4 Proof of the Hahn–Banach Theorem#^lem-4-1|§4.1]].
> - **Existence of a complement** (HW1): objects are subspaces $W$ with $W \cap Y = \{0\}$; one-step lemma is Lemma [[§1 Linear Spaces#^lem-1-7|§1.7]].
> - **Existence of an orthonormal basis** (Lecture 9, Theorem [[§20 Orthonormal Sets and Bases#^thm-20-12|§20.12]]): objects are orthonormal sets; the one-step move adds $x/\|x\|$ for a nonzero $x$ orthogonal to all of them.

^ex-t3

## Technique 4: Linearity via Uniqueness

> [!remark] Remark: Strategy
> When a map is defined by “decompose $x$ and read off a component,” prove linearity by decomposing $a x_1 + b x_2$ *by hand* as $(a w_1 + b w_2) + (a y_1 + b y_2)$, checking each summand lies in the right subspace by closure, and invoking uniqueness of the decomposition to conclude that this is the decomposition the map sees.

^rem-t4

> [!example] Example T4: Application (HW1)
> Linearity of $M(x) = ([w], y)$ in Theorem [[§1 Linear Spaces#^thm-1-11|§1.11]]. The same device proves linearity of any projection onto a summand of a direct sum.

^ex-t4

## Technique 5: Completeness — Find the Candidate, Then Close

> [!remark] Remark: Strategy
> To prove a normed space is complete, take a Cauchy sequence and proceed in two separate stages, never merged.
> - (i) **Candidate.** Use the Cauchy property in a *weaker* form that reduces to a space already known complete — coordinatewise for sequence spaces ($\mathbb{F}$ is complete), pointwise or almost everywhere for function spaces (via a subsequence) — and let that produce an object $a$. At this stage nothing is known about $a$ except that it exists.
> - (ii) **Closing.** Return to the Cauchy property in its *full* form, with the $N$ fixed once and for all, and show both that $a$ lies in the space and that $\|a^{(n)} - a\| \to 0$. The second usually gives the first: $a = a^{(N)} + (a - a^{(N)})$.
>
> Wu: “In any completeness problem, the first thing you need to do is find the candidate. Then try to argue the sequence does converge. If you don't have a candidate, we have nothing to do.”

^rem-t5

> [!example] Example T5: Applications
> - **$\ell^p$ complete** (lecture, Theorem [[§13 Minkowski's Inequality and the Spaces ℓᵖ#^thm-13-5|§13.5]]): candidate by coordinates; closing by the tail estimate ([[§13 Minkowski's Inequality and the Spaces ℓᵖ#^pf-13-5|4.4]]).
> - **Completion of a normed space** (HW2 P3, Theorem [[§9 Completeness#^thm-9-4|§9.4]]): candidate is the diagonal sequence $y_j = x^{(M_j)}_{N_j}$; closing by two three-term triangle inequalities with an auxiliary index sent to infinity last.
> - **$C[a,b]$ with the sup norm** (HW2 P1, Theorem [[§9 Completeness#^thm-9-1|§9.1]]): candidate by pointwise limits; closing by uniform convergence, then the $3\varepsilon$ argument for continuity of the limit.

^ex-t5

## Technique 6: Truncate, Then Pass to the Limit

> [!remark] Remark: Strategy
> When an estimate involves an infinite sum or an integral that might be infinite, or when two limits interact, cut off to a finite sum first.
> - (i) Prove the inequality for finitely supported objects, where every quantity is finite and algebra (dividing, cancelling) is legitimate.
> - (ii) Apply it to the truncations $a^{(n)} = (a_1, \ldots, a_n, 0, \ldots)$, bound the right side by the untruncated quantity (a partial sum of non-negative terms is at most the full sum), and let $n \to \infty$ using monotone convergence of the partial sums.
>
> When two limits are present (an index $m \to \infty$ inside a sum over $i$, and the length $k$ of the sum $\to \infty$): keep the full-strength hypothesis with its uniform $N$, truncate to $k$ terms, pass $m \to \infty$ termwise through the finite sum, and only then send $k \to \infty$. Never let the threshold $N$ depend on $k$.

^rem-t6

> [!example] Example T6: Applications
> - **Minkowski for sequences** (lecture, Theorem [[§13 Minkowski's Inequality and the Spaces ℓᵖ#^thm-13-1|§13.1]]): the cancellation of $\|a+b\|_p^{\,p-1}$ is only valid for finitely supported sequences; the general case follows by truncation.
> - **Completeness of $\ell^p$**, Step 2 (Theorem [[§13 Minkowski's Inequality and the Spaces ℓᵖ#^thm-13-5|§13.5]]): the order truncate $\to$ $m \to \infty$ $\to$ $k \to \infty$.
> - **Hölder for finite sums** is the special case of Theorem [[§12 Hölder's Inequality for Sequences#^thm-12-1|§12.1]] with zero tails; conversely no truncation is needed there because every quantity is a sum of non-negative terms and inequalities in $[0,\infty]$ suffice.

^ex-t6

## Technique 7: Compactness of the Unit Sphere in Finite Dimensions

> [!remark] Remark: Strategy
> To get a lower bound $\|x\|' \ge c\|x\|$ between two norms on a finite-dimensional space, or more generally to show a continuous positive function is bounded away from $0$: restrict to the unit sphere $S$ of one norm, show $S$ is sequentially compact (bounded coordinates $\Rightarrow$ [[Bolzano–Weierstrass Theorem|Bolzano–Weierstrass]] coordinate by coordinate), show the function is continuous on $S$ (usually via a one-sided estimate and the [[§8 Normed Linear Spaces#^lem-8-3|reverse triangle inequality]]), conclude it attains its infimum, and use positivity at the minimizer to get $c > 0$. Homogeneity then extends the bound from $S$ to all of $X$. The step that fails in infinite dimensions is the compactness of $S$.

^rem-t7

> [!example] Example T7: Applications (HW2)
> - **All norms on $\mathbb{F}^n$ are equivalent** (P2(a), Theorem [[§10 New Normed Spaces from Old#^thm-10-3|§10.3]]), Steps 4–7.
> - **Finite-dimensional subspaces are closed** (P2(b), Corollary [[§10 New Normed Spaces from Old#^cor-10-5|§10.5]]), via the equivalence with the coordinate norm.

^ex-t7

## Technique 8: Rotate to Make it Real

> [!remark] Remark: Strategy
> A real inequality of the form $\operatorname{Re}\Lambda(x) \le p(x)$ gives no control on $|\Lambda(x)|$ directly. To upgrade it, multiply $x$ by a unimodular scalar chosen for that one $x$: write $\Lambda(x) = |\Lambda(x)|e^{i\varphi}$ and set $a = e^{-i\varphi}$, so that $\Lambda(ax) = a\Lambda(x) = |\Lambda(x)|$ is real and non-negative, hence equals its own real part. Applying the real bound to $ax$ and using $|a| = 1$ to undo the rotation on the right gives $|\Lambda(x)| \le p(x)$ with constant $1$. The gain over splitting into real and imaginary parts is the constant: that route costs a factor $\sqrt{2}$, because it uses the bound twice.

^rem-t8

> [!example] Example T8: Applications
> - **Complex Hahn–Banach**, Step 5 (Theorem [[§7 The Complex Hahn–Banach Theorem#^thm-7-1|§7.1]]): rotate $x$ so that $L(ax)$ is real, then apply $U \le p$.
> - **Cauchy–Schwarz**, Step 4 (Theorem [[§17 Cauchy–Schwarz and the Induced Norm#^thm-17-1|§17.1]]): rotate $y$ so that $(e^{i\theta}y, x)$ is real, then apply the bound on $|\operatorname{Re}(y,x)|$ obtained from the real quadratic.

^ex-t8

## Technique 9: Incompleteness and Identifying the Completion

> [!remark] Remark: Strategy
> To show a normed space $(X, \|\cdot\|)$ is not complete and find its completion:
> - (i) find a Banach space $Z$ and a norm-preserving linear map $J : X \to Z$ (often an inclusion, or $f \mapsto [f]$ into an $L^p$ space);
> - (ii) show $J(X)$ is dense in $Z$;
> - (iii) show $J(X) \ne Z$ by exhibiting $z \in Z \setminus J(X)$.
>
> Then $\overline{X} = Z$ (Proposition [[§9 Completeness#^prop-9-5|§9.5]]), and $X$ is not complete, because a sequence in $X$ whose image converges to $z$ is Cauchy with no limit in $X$. When a proof without the ambient $Z$ is wanted, write the Cauchy sequence down explicitly and show that any limit in $X$ would have to violate the defining property of $X$ (continuity, differentiability, …). Before starting, check the norm, not only the set: the same set may be complete under one norm and not under another.

^rem-t9

> [!example] Example T9: Applications (HW3)
> - **$C[a,b]$ in the $L^p$ norm** (P1, Proposition [[§14 The Function Spaces Lᵖ(Ω)#^prop-14-8|§14.8]]): $Z = L^p[a,b]$; witness the step function, approached by ramps.
> - **$C^2[a,b]$ in the norm $\max|f| + \max|f'|$** (P2, Proposition [[§9 Completeness#^prop-9-7|§9.7]]): $Z = C^1[a,b]$; density by approximating $f'$ uniformly and integrating; witness $|x - c|^{3/2}$.
> - **Contrast**: $C[a,b]$ in the sup norm is already complete (Theorem [[§9 Completeness#^thm-9-1|§9.1]]), and so is $C^2[a,b]$ in the full $C^2$ norm.

^ex-t9

## Technique 10: From $\mathbb{N}$ to $\mathbb{R}$ by Continuity

> [!remark] Remark: Strategy
> To prove $F(ax) = aF(x)$ for all real $a$ from additivity $F(x + y) = F(x) + F(y)$: induction gives $a \in \mathbb{N}$; $F(0) = 0$ and $F(-x) = -F(x)$ give $a \in \mathbb{Z}$; $n F(\frac{m}{n}x) = F(mx) = mF(x)$ gives $a \in \mathbb{Q}$; and continuity of $a \mapsto F(ax)$, together with density of $\mathbb{Q}$, gives $a \in \mathbb{R}$. The last step is the only analytic one and cannot be skipped.

^rem-t10

> [!example] Example T10: Application (HW3)
> Real homogeneity of the polarization form in the Jordan–von Neumann theorem (P3, Theorem [[§17 Cauchy–Schwarz and the Induced Norm#^thm-17-4|§17.4]]), with continuity supplied by [[§8 Normed Linear Spaces#^prop-8-4|continuity of the norm]].

^ex-t10

## Technique 11: Minimize, Then Perturb

> [!remark] Remark: Strategy
> To produce a point with a geometric property (closest point, orthogonal vector) in a Hilbert space:
> - (i) **Minimize.** Take a minimizing sequence for the relevant infimum, and show it is Cauchy by applying the [[§17 Cauchy–Schwarz and the Induced Norm#^prop-17-3|parallelogram law]] to two of its terms; convexity of the constraint set puts the midpoint back in the set and makes the cross term large. Completeness gives a limit; closedness keeps it in the set.
> - (ii) **Perturb.** To extract the property of the minimizer, compare it with nearby competitors $y_0 + ty$, expand $\|v - ty\|^2$, and let $t \to 0$ along a ray $t = s e^{i\theta}$ chosen ([[#^rem-t8|Technique 8]]) to make the linear term real: a minimum forces the coefficient of the linear term to vanish. Write down explicitly how small $s$ must be.
>
> The same two moves prove uniqueness (apply (i) to two minimizers) and the double-complement identity (apply (ii) to the decomposition).

^rem-t11

> [!example] Example T11: Applications
> - **Projection theorem** (Theorem [[§18 Projection and Orthogonal Decomposition#^thm-18-2|§18.2]]): step (i).
> - **Orthogonal decomposition** (Theorem [[§18 Projection and Orthogonal Decomposition#^thm-18-4|§18.4]]): step (i) applied to $K = Y$, then step (ii) to show $x_0 - y_0 \perp Y$.
> - **Cauchy–Schwarz** (Theorem [[§17 Cauchy–Schwarz and the Induced Norm#^thm-17-1|§17.1]]) is step (ii) in disguise: $\|x + ty\|^2 \ge 0$ for all $t$, with the quadratic in $t$ minimized at $t = -B/A$.

^ex-t11

## Technique 12: Countability by Level Sets

> [!remark] Remark: Strategy
> To show that $S = \{ \alpha : t_\alpha \neq 0 \}$ is countable for a family of numbers $(t_\alpha)$ over a possibly uncountable index set, split it into level sets $\Lambda_k = \{ \alpha : |t_\alpha| \ge 1/k \}$, so that $S = \bigcup_k \Lambda_k$, and bound the number of elements of each $\Lambda_k$ by an inequality that holds for every *finite* subset, such as a [[§20 Orthonormal Sets and Bases#^lem-20-2|finite Bessel inequality]] or a finite measure bound. Wu: “you want to show something is finite, and then you take a lower bound.” Only finite subsets can be fed into the inequality; the uniform bound on them is what proves $\Lambda_k$ finite.

^rem-t12

> [!example] Example T12: Application
> Countable support of the orthonormal coefficients $(x, e_\alpha)$ (Proposition [[§20 Orthonormal Sets and Bases#^prop-20-4|§20.4]]), with $\#\Lambda_k \le k^2\|x\|^2$ from Lemma [[§20 Orthonormal Sets and Bases#^lem-20-2|§20.2]].

^ex-t12

## Technique 13: Test Against a Well-Chosen Vector

> [!remark] Remark: Strategy
> To bound $\|h\|$ from below, find a vector $g$ whose inner product with $h$ is determined by the data, and apply [[§17 Cauchy–Schwarz and the Induced Norm#^thm-17-1|Cauchy–Schwarz]]: $|(h, g)| \le \|h\|\,\|g\|$. The best $g$ lies in the span of the vectors whose inner products with $h$ are prescribed (projection onto that span). Dually, to show a vector is small, bound each of its coefficients by Cauchy–Schwarz and add them up with [[§20 Orthonormal Sets and Bases#^thm-20-8|Parseval]].

^rem-t13

> [!example] Example T13: Applications (HW4)
> - **Sharp integral inequality** (P4, Proposition [[§18 Projection and Orthogonal Decomposition#^prop-18-8|§18.8]]): $h = f''$, $g$ linear, $(h,g) = -1$ from the boundary data.
> - **Perturbed orthonormal sets** (P3, Proposition [[§20 Orthonormal Sets and Bases#^prop-20-10|§20.10]]): $(x, e_n) = (x, e_n - f_n)$, then Parseval.

^ex-t13

## Technique 14: Computing an Orthogonal Complement

> [!remark] Remark: Strategy
> To show $S^\perp = C$: first guess $C$ and check $C \subset S^\perp$ directly (often by a symmetry). For $S^\perp \subset C$, decompose an arbitrary $g \in S^\perp$ as $g = s + c$ with $s \in S$, $c \in C$, and test $g$ against its own $S$-component: $0 = (g, s) = \|s\|^2 + (c, s) = \|s\|^2$. For a set $M$ that is not a closed subspace, first replace it by $\overline{\operatorname{span}}\, M$, which has the same complement.

^rem-t14

> [!example] Example T14: Applications (HW4)
> - **Even and odd functions** (P1, Proposition [[§18 Projection and Orthogonal Decomposition#^prop-18-7|§18.7]]): symmetry gives $O \subset E^\perp$; testing against $g_e$ gives the rest.
> - **Double complement** (P2, Theorem [[§18 Projection and Orthogonal Decomposition#^thm-18-6|§18.6]]): Lemma [[§18 Projection and Orthogonal Decomposition#^lem-18-5|§18.5]], then Theorem [[§18 Projection and Orthogonal Decomposition#^thm-18-4|§18.4]](2).

^ex-t14

## Technique 15: Separability by Truncation and Rational Approximation

> [!remark] Remark: Strategy
> To show a space is separable, write down a countable set built from finitely many rational parameters (finitely many rational coordinates, rational coefficients on finitely many basis vectors, rational heights on rational rectangles). Countability: a [[Countable Union of Countable Sets is Countable|countable union]] over the number of parameters of countable products. Density: first cut off a small “tail” (the tail of a convergent series or expansion, or the part of a function outside a large box), then replace the finitely many remaining parameters by nearby rationals. The first step is what fails in $\ell^\infty$ and $L^\infty$, where the norm is a supremum rather than a sum or integral.

^rem-t15

> [!example] Example T15: Applications (Lecture 9)
> - $\ell^p$, $1 \le p < \infty$ (Proposition [[§20 Orthonormal Sets and Bases#^prop-20-13|§20.13]]).
> - $L^p(E)$, $1 \le p < \infty$ (Proposition [[§20 Orthonormal Sets and Bases#^prop-20-16|§20.16]]), after reducing to continuous functions.
> - A Hilbert space with a countable orthonormal basis (Theorem [[§20 Orthonormal Sets and Bases#^thm-20-18|§20.18]], $\Rightarrow$).

^ex-t15

## Technique 16: Non-Separability from an Uncountable Separated Family

> [!remark] Remark: Strategy
> To show a space is not [[§20 Orthonormal Sets and Bases#^def-20-5|separable]], find uncountably many elements at mutual distance at least $\delta > 0$. The balls of radius $\delta/2$ about them are disjoint, a [[§8 Normed Linear Spaces#^def-8-7|dense]] set must meet each of them, and choosing one point of the dense set in each ball gives a one-to-one map from an uncountable set into the dense set. Indicator functions (or indicator sequences) are the usual source: in a supremum norm two different indicators are at distance $1$.

^rem-t16

> [!example] Example T16: Applications (HW5)
> - $L^\infty([0,1])$ (P1(b), Proposition [[§20 Orthonormal Sets and Bases#^prop-20-17|§20.17]]): $\chi_{[0,t]}$, $t \in (0,1]$.
> - $\ell^\infty$ (Proposition [[§20 Orthonormal Sets and Bases#^prop-20-15|§20.15]]): $\chi_S$, $S \subset \mathbb{N}$.

^ex-t16

## Technique 17: Complete the Square to Reach a Distance

> [!remark] Remark: Strategy
> A quadratic functional $\frac12\|v\|^2 - \ell(v)$ on a Hilbert space becomes, after writing $\ell = (\cdot, u^*)$ by [[§19 Bounded Linear Functionals and the Riesz Representation Theorem#^thm-19-2|Riesz]] and adding and subtracting $\frac12\|u^*\|^2$, the function $\frac12\|u^* - v\|^2 - \frac12\|u^*\|^2$. Minimizing it is minimizing a distance, and the [[§18 Projection and Orthogonal Decomposition#^thm-18-2|projection theorem]] gives existence and uniqueness of the minimizer.

^rem-t17

> [!example] Example T17: Applications (HW5)
> - Quadratic minimization over a closed convex set (P3, Proposition [[§19 Bounded Linear Functionals and the Riesz Representation Theorem#^prop-19-5|§19.5]]).

^ex-t17

## Technique 18: Subtract a Multiple of $x_0$ to Land in the Null Space

> [!remark] Remark: Strategy
> For a [[§2 Linear Maps, Convexity, and Linear Functionals#^def-2-5|linear functional]] $\ell$ and a fixed $x_0$ with $\ell(x_0) \neq 0$, the vector $x - \frac{\ell(x)}{\ell(x_0)} x_0$ lies in the [[§22 Dual Spaces#^prop-22-5|null space]] of $\ell$ for every $x$. This one formula splits $X$ as null space plus a line, and, applied to a sequence, produces points of the null space near a given point off it.

^rem-t18

> [!example] Example T18: Applications (HW5)
> - Codimension one (P4, Proposition [[§22 Dual Spaces#^prop-22-5|§22.5]]).
> - Closed null space implies bounded (P5, Proposition [[§22 Dual Spaces#^prop-22-6|§22.6]]): $y_n = x_0 - x_n/\ell(x_n)$.
> - The [[§19 Bounded Linear Functionals and the Riesz Representation Theorem#^thm-19-2|Riesz representation theorem]], part (2) (Lemma [[§19 Bounded Linear Functionals and the Riesz Representation Theorem#^lem-19-4|§19.4]](c)).

^ex-t18
