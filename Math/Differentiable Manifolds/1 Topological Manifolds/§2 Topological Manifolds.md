---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 1
section: 2
tags: [differentiable-manifolds, math591]
---
← [[§1 Point-Set Topology Review]] · ↑ [[· 1 Topological Manifolds]] · [[§3 Subspaces and Products]] →

*Foundations — The definition of a topological manifold and the role of each axiom. The two ways of building examples begin next: by quotients ([[§3 Subspaces and Products|§3]]) and by equations ([[§7 The Regular Value Theorem|§7]]).*

*Reference: Lee Ch. 1, “Topological Manifolds.”*

## The Definition

> [!definition] Definition §2.1: Locally Euclidean
> $X$ is **locally Euclidean** (of dimension $n$) if there exists $n \in \mathbb{N}$ such that for every $p \in X$ there exist a neighborhood $U$ of $p$ and a map
>
> $$
> \varphi : U \longrightarrow \mathbb{R}^n
> $$
>
> which is a **homeomorphism**: $\varphi$ is continuous, bijective, and $\varphi^{-1} : \mathbb{R}^n \to U$ is also continuous.

^def-2-1

> [!remark] Remark: Quantifier Order
> As first written on the board, the definition read “$\forall p\ \exists U\ \exists \varphi: U \to \mathbb{R}^n$,” with $n$ implicitly fixed. A student asked whether $n$ is allowed to depend on $p$; the answer in this course is **no**: “$\exists n$” comes *before* “$\forall p$.” See the remark “[[§2 Topological Manifolds#^rem-2-3|Conventions on the Dimension]]” below for what happens under the other convention.

^rem-2-1

> [!definition] Definition §2.2: Topological Manifold
> A **topological manifold** (of dimension $n$) is a topological space $X$ that is
> 1. second countable,
> 2. Hausdorff ($T_2$), and
> 3. locally Euclidean of dimension $n$.
>
> *Lee: Ch. 1, “Topological Manifolds”*

^def-2-2

> [!remark]- Connections
> - The three conditions: [[§1 Point-Set Topology Review#^def-1-5|Def. §1.5]], [[§1 Point-Set Topology Review#^def-1-7|Def. §1.7]], [[§2 Topological Manifolds#^def-2-1|Def. §2.1]]; the smooth version is [[§13 Differentiable Structures#^def-13-9|Smooth Manifold Structure, Def. §13.9]].

> [!remark] Remark: Why These Three Conditions?
> Locally Euclidean is the substantive geometric condition: near every point the space looks like $\mathbb{R}^n$, so calculus can (eventually) be imported chart by chart. The other two are global point-set hygiene. Hausdorff rules out non-uniqueness of limits (and, later, guarantees that compact subsets are closed, that one-point sets are closed, etc.); second countability rules out spaces that are “uncountably large” and is the hypothesis behind partitions of unity. Neither of the two hygiene conditions is implied by local Euclideanness—this is the content of the [[§2 Topological Manifolds#^prop-2-4|independence remark]] and the examples preceding it.

^rem-2-2

## Dimension

> [!remark] Remark: Conventions on the Dimension
> Manifold theory is an old subject (a couple of hundred years, depending on where one starts counting), and conventions vary between books. In particular, **some books allow $n$ to depend on $p$**. Under that convention, the union of a sphere and a line (disjoint) would be a manifold with dimension $2$ on one component and $1$ on the other. It is a theorem, however, that $n$ is then constant on connected components ([[§2 Topological Manifolds#^cor-2-2|Corollary §2.2]] below). A second convention, which follows Lee: the empty set satisfies the definition of a topological $n$-manifold for *every* $n$, which is why statements about dimension, such as Lee's Theorem 1.2, are made for nonempty manifolds. This is a minor point—but the general lesson is important: *when you read a book on this subject, always check its conventions first.* (Uribe warns this gets worse in MATH 635, Riemannian geometry.)

^rem-2-3

The fact that the dimension of a manifold is well-defined rests on the following theorem, which was stated but not proved in lecture. Its proof is genuinely hard and uses tools from algebraic topology.

> [!theorem] Theorem §2.1: Topological Invariance of Dimension
> Let $A \subseteq \mathbb{R}^n$ and $B \subseteq \mathbb{R}^m$ be nonempty open sets. If $A$ and $B$ are homeomorphic, then $n = m$.
>
> *Lee: Theorem 1.2 (proved as Theorem 17.26)*

^thm-2-1

> [!proof]+ Proof (to be filled)
> Not proved in this course (Lee proves it as Theorem 17.26). To be filled.

^pf-2-1

**Not proved in this course.** The theorem follows from Brouwer's *invariance of domain*; Lee proves it in Chapter 17 (Theorem 17.26) using de Rham cohomology. Note that the statement is purely about point-set topology—no differentiability is assumed—which is what makes it hard: the obvious linear-algebra argument ($\mathbb{R}^n \cong \mathbb{R}^m$ as vector spaces implies $n=m$) is unavailable, because homeomorphisms need not be linear or even differentiable. Compare: $\mathbb{R}$ and $\mathbb{R}^2$ are not homeomorphic by a connectedness argument (remove a point), but already $\mathbb{R}^2$ vs. $\mathbb{R}^3$ needs more.

> [!remark]- Connections
> - The case ℝ² ≇ ℝ³ is proved in 590 by comparing π₁ of the punctured spaces: [[§23 The Fundamental Group#^rem-23-2|590 §23, Remark: What π₁ Cannot See]].

> [!theorem] Corollary §2.2: Dimension is Locally Constant
> Suppose $X$ satisfies the definition of “locally Euclidean” with $n$ allowed to depend on $p$. Then for each $p$ the integer $n(p)$ is well-defined, and $p \mapsto n(p)$ is constant on each connected component of $X$.
>
> *Lee: cf. Theorem 1.2*

^cor-2-2

> [!proof]+ Proof (not given in lecture)
> *Well-defined:* if $\varphi : U \to \mathbb{R}^n$ and $\psi : V \to \mathbb{R}^m$ are homeomorphisms with $p \in U \cap V$, then $\varphi(U \cap V) \subseteq \mathbb{R}^n$ and $\psi(U \cap V) \subseteq \mathbb{R}^m$ are nonempty open sets (images of an open set under homeomorphisms onto open sets), and $\psi \circ \varphi^{-1}$ restricts to a homeomorphism between them. By the theorem, $n = m$.
>
> *Locally constant:* if $\varphi : U \to \mathbb{R}^n$ is a homeomorphism with $p \in U$, then the same $\varphi$ shows $n(q) = n$ for *every* $q \in U$. Hence $X_n := \{q \in X \mid n(q) = n\}$ is open for each $n$. The sets $X_n$ are pairwise disjoint and cover $X$, so each $X_n$ is also closed (its complement is a union of open sets). A connected component $C$ is connected and $C = \bigsqcup_n (C \cap X_n)$ is a decomposition into disjoint relatively open sets, so exactly one $C \cap X_n$ is nonempty.

^pf-2-2

*Uses:* [[§2 Topological Manifolds#^thm-2-1|§2.1]], [[§2 Topological Manifolds#^def-2-1|Def. §2.1]], [[§1 Point-Set Topology Review#^prop-1-5|§1.5]], [[§1 Point-Set Topology Review#^def-1-8|Def. §1.8]], [[§1 Point-Set Topology Review#^prop-1-7|§1.7]], [[§13 Connected Spaces#^def-13-1|590 Def. §13.1]]

> [!theorem] Proposition §2.3: Charts onto Open Subsets Suffice
> In the definition of locally Euclidean, replacing “$\varphi : U \to \mathbb{R}^n$ is a homeomorphism” by
>
> $$
> \text{“}\varphi : U \to A \text{ is a homeomorphism onto some } \textit{open} \text{ set } A \subseteq \mathbb{R}^n\text{”}
> $$
>
> yields an equivalent notion.
>
> *Lee: Ch. 1, “Topological Manifolds”*

^prop-2-3

> [!proof]+ Proof (sketched in lecture; details filled in)
> The original definition trivially implies the seemingly more general one (take $A = \mathbb{R}^n$). Conversely, suppose $\varphi : U \to A$ is a homeomorphism onto an open $A \subseteq \mathbb{R}^n$ and $p \in U$. Since $A$ is open and $\varphi(p) \in A$, there is an open ball $B = B(\varphi(p), r) \subseteq A$. Set $U' = \varphi^{-1}(B)$. Then $U'$ is open in $U$ (continuity of $\varphi$), hence open in $X$ (since $U$ is open in $X$), and $p \in U'$. The restriction $\varphi|_{U'} : U' \to B$ is a homeomorphism (restriction of a homeomorphism to an open set, onto its image). It remains to exhibit a homeomorphism $h : B \to \mathbb{R}^n$. Write $c = \varphi(p)$ and define
>
> $$
> h : B(c,r) \to \mathbb{R}^n, \quad h(y) = \frac{y - c}{r - |y - c|}, \qquad\qquad g : \mathbb{R}^n \to B(c,r), \quad g(z) = c + \frac{r\, z}{1 + |z|}.
> $$
>
> $h$ is continuous on $B(c,r)$ because the denominator $r - |y-c|$ is continuous and strictly positive there. $g$ is continuous on $\mathbb{R}^n$, and takes values in $B(c,r)$ since $|g(z) - c| = \dfrac{r|z|}{1+|z|} < r$. For $y \in B(c,r)$ put $v = y - c$ and $s = |v| < r$; then $h(y) = v/(r-s)$, $|h(y)| = s/(r-s)$, so $1 + |h(y)| = r/(r-s)$ and
>
> $$
> g(h(y)) = c + r \cdot \frac{v}{r-s} \cdot \frac{r-s}{r} = c + v = y.
> $$
>
> For $z \in \mathbb{R}^n$ put $v = g(z) - c = \dfrac{rz}{1+|z|}$; then $|v| = \dfrac{r|z|}{1+|z|}$, so $r - |v| = \dfrac{r}{1+|z|}$ and
>
> $$
> h(g(z)) = \frac{v}{r - |v|} = \frac{rz}{1+|z|} \cdot \frac{1+|z|}{r} = z.
> $$
>
> Thus $h$ is a bijection with continuous inverse $g$, i.e. a homeomorphism $B \to \mathbb{R}^n$, and $h \circ \varphi|_{U'} : U' \to \mathbb{R}^n$ is a homeomorphism from a neighborhood of $p$ onto $\mathbb{R}^n$, as required.

^pf-2-3

*Uses:* [[§2 Topological Manifolds#^def-2-1|Def. §2.1]], [[§1 Point-Set Topology Review#^prop-1-5|§1.5]] (3), [[§5 Subspace Topology#^lem-5-2|590 §5.2]], [[§9 Continuous Functions#^prop-9-3|590 §9.3]]

> [!remark] Remark
> Lee takes the “open subset” version as the *definition* of locally Euclidean and leaves the equivalence as Exercise 1.1. The practical upshot: to verify that a space is locally Euclidean, it is enough to exhibit, around each point, a homeomorphism onto an open ball, or onto an open disk, or onto any open subset of $\mathbb{R}^n$—one never needs to hit all of $\mathbb{R}^n$. This is used immediately in the $S^2$ example ([[§2 Topological Manifolds#^ex-2-4|Ex. §2.4]]) below.

^rem-2-4

## Independence of the Three Conditions

> [!remark] Remark: The Exam Trap: Locally Euclidean Does Not Imply Hausdorff
> It is tempting to argue: “each point has a neighborhood homeomorphic to a disk, and points in Euclidean space can be separated, so a locally Euclidean space must be Hausdorff.” This is **false**. The argument only separates points lying in a *common* chart; two points may fail to share any chart, and then no Euclidean argument applies. The line with two origins is exactly this failure.

^rem-2-5

> [!example] Example §2.1: Fails $T_2$: The Line with Two Origins
> Let $X$ be the line with two origins ([[§1 Point-Set Topology Review#^ex-1-4|Example §1.4]]). Then $X$ is second countable and locally Euclidean of dimension $1$, but not Hausdorff.
> - *Not $T_2$:* shown in [[§1 Point-Set Topology Review#^ex-1-4|Example §1.4]].
> - *Locally Euclidean.* Throughout, $\mathcal{B}$ and $N_i(\varepsilon)$ are as in [[§1 Point-Set Topology Review#^ex-1-4|Example §1.4]]. Recall that for an open $U \subseteq X$ the sets $B \cap U$, $B \in \mathcal{B}$, form a basis of the subspace topology on $U$ (an open subset of $U$ is $W \cap U$ with $W$ a union of members of $\mathcal{B}$).
>
>   *Points of a ray.* Let $p$ lie in a ray and let $I = (a,b)$ be an open interval in that ray with $p \in I$; $I \in \mathcal{B}$ is open in $X$. Every member of $\mathcal{B}$ meets $I$ in an open interval or the empty set (Axiom 2 computation in [[§1 Point-Set Topology Review#^ex-1-4|Example §1.4]]), so the subspace topology on $I$ has the open subintervals of $I$ as a basis, i.e. is the usual topology on $(a,b) \subseteq \mathbb{R}$. Thus $\mathrm{id} : I \to (a,b)$ is a homeomorphism onto an open subset of $\mathbb{R}$.
>
>   *The origins.* Fix $i \in \{1,2\}$, let $j$ be the other index, fix $\varepsilon > 0$, and let $U = N_i(\varepsilon)$, an open neighborhood of $0_i$. Define
>
>   $$
>   \varphi : U \to (-\varepsilon, \varepsilon), \qquad \varphi(x) = x \ \text{ for } x \neq 0_i, \quad \varphi(0_i) = 0.
>   $$
>
>   $\varphi$ is a bijection. We show it is continuous and open.
>
>   *Basis of $U$.* Intersecting the members of $\mathcal{B}$ with $U$, with $m = \min(\delta, \varepsilon)$:
>
>   $$
>   \begin{aligned}
>   (a,b) \cap U &= \text{an open interval contained in } (-\varepsilon, 0) \text{ or in } (0, \varepsilon), \text{ or } \emptyset; \\
>   N_i(\delta) \cap U &= N_i(m); \\
>   N_j(\delta) \cap U &= (-m, 0) \cup (0, m).
>   \end{aligned}
>   $$
>
>   Hence a basis $\mathcal{B}_U$ of $U$ consists of: open intervals contained in $(-\varepsilon,0)$ or $(0,\varepsilon)$; the sets $N_i(\delta)$ with $0 < \delta \le \varepsilon$; and the sets $(-m,0) \cup (0,m)$ with $0 < m \le \varepsilon$.
>
>   *$\varphi$ is open.* Since images commute with unions, it suffices that $\varphi(B)$ is open for $B \in \mathcal{B}_U$. For an interval $(a,b)$ in a ray, $\varphi((a,b)) = (a,b)$; $\varphi(N_i(\delta)) = (-\delta, 0) \cup \{0\} \cup (0, \delta) = (-\delta, \delta)$; $\varphi((-m,0) \cup (0,m)) = (-m,0) \cup (0,m)$. All are open in $(-\varepsilon, \varepsilon)$.
>
>   *$\varphi$ is continuous.* Since preimages commute with unions, it suffices that $\varphi^{-1}(J)$ is open for every open interval $J = (a,b)$ with $-\varepsilon \le a < b \le \varepsilon$, these forming a basis of $(-\varepsilon,\varepsilon)$. If $0 \notin J$, then $J$ lies in $(-\varepsilon,0)$ or $(0,\varepsilon)$ and $\varphi^{-1}(J) = J \in \mathcal{B}_U$. If $0 \in J$, i.e. $a < 0 < b$, then with $m = \min(-a, b)$,
>
>   $$
>   \varphi^{-1}(J) = (a, 0) \cup \{0_i\} \cup (0, b) = N_i(m) \cup (a, 0) \cup (0, b),
>   $$
>
>   a union of members of $\mathcal{B}_U$, hence open.
>
>   Therefore $\varphi$ is a homeomorphism of the neighborhood $U$ of $0_i$ onto the open set $(-\varepsilon,\varepsilon) \subseteq \mathbb{R}$, and [[§2 Topological Manifolds#^prop-2-3|Proposition §2.3]] shows $X$ is locally Euclidean of dimension $1$ at $0_i$.
> - *Second countable.* Let
>
>   $$
>   \mathcal{B}_{\mathbb{Q}} = \{\, (a,b) \in \mathcal{B} \mid a, b \in \mathbb{Q} \,\} \;\cup\; \{\, N_i(q) \mid i = 1, 2,\ q \in \mathbb{Q}_{>0} \,\},
>   $$
>
>   a countable subcollection of $\mathcal{B}$ (indexed by subsets of $\mathbb{Q}^2$ and $\{1,2\} \times \mathbb{Q}$). We verify [[§1 Point-Set Topology Review#^def-1-1|Definition §1.1]]. Let $W$ be open and $x \in W$; then $x$ lies in some member $B \in \mathcal{B}$ with $B \subseteq W$.
>   If $x$ lies in a ray: either $B = (a,b)$ is an interval, or $B = N_k(\delta)$ and then $x \in (-\delta, 0)$ or $x \in (0,\delta)$, an interval contained in $B$; in both cases $x$ lies in an open interval $(a,b) \subseteq W$ inside a ray, and choosing rationals $a < a' < x < b' < b$ with $(a',b')$ still inside the ray gives $x \in (a',b') \in \mathcal{B}_{\mathbb{Q}}$ and $(a',b') \subseteq W$.
>   If $x = 0_i$: the only members of $\mathcal{B}$ containing $0_i$ are the $N_i(\delta)$, so $B = N_i(\delta)$; choose $q \in \mathbb{Q}$ with $0 < q < \delta$, and then $0_i \in N_i(q) \subseteq N_i(\delta) \subseteq W$ with $N_i(q) \in \mathcal{B}_{\mathbb{Q}}$.
>
> Uribe: this is the *trickiest* of the three counterexamples to come up with—once you have one, there are a million variations.

^ex-2-1

*Uses:* [[§1 Point-Set Topology Review#^ex-1-4|Ex. §1.4]], [[§1 Point-Set Topology Review#^def-1-1|Def. §1.1]], [[§1 Point-Set Topology Review#^def-1-5|Def. §1.5]], [[§1 Point-Set Topology Review#^prop-1-5|§1.5]], [[§2 Topological Manifolds#^prop-2-3|§2.3]], [[§5 Subspace Topology#^lem-5-1|590 §5.1]]

> [!remark]- Connections
> - The same space as a quotient: [[§4 Quotient Spaces and Open Maps#^ex-4-1|Ex. §4.1]], [[§6 Open Quotients and Complex Projective Space#^ex-6-1|Ex. §6.1]].

> [!example] Example §2.2: Fails Locally Euclidean: $\mathbb{Q}$
> $X = \mathbb{Q}$ with the subspace topology from $\mathbb{R}$ is second countable (subspace of a second countable space) and $T_2$ (metric space), but is not locally Euclidean of any dimension.
>
> *Reason (not given in lecture):* suppose $p \in \mathbb{Q}$ has a neighborhood $U$ homeomorphic to $\mathbb{R}^n$. If $n \ge 1$, then $\mathbb{R}^n$ is uncountable while $U \subseteq \mathbb{Q}$ is countable—a homeomorphism is in particular a bijection, contradiction. If $n = 0$, then $\mathbb{R}^0$ is a single point, so $U = \{p\}$ would be open in $\mathbb{Q}$; but $\mathbb{Q}$ has no isolated points (every interval around $p$ contains other rationals). Contradiction either way.
>
> *Lee: no counterpart; a course example*

^ex-2-2

*Uses:* [[§1 Point-Set Topology Review#^prop-1-6|§1.6]], [[§2 Topological Manifolds#^def-2-1|Def. §2.1]], [[§18 Countability Axioms#^thm-18-3|590 §18.3]]

> [!example] Example §2.3: Fails Second Countability: $\mathbb{R}_{\mathrm{disc}} \times \mathbb{R}$
> Let $X = \mathbb{R}_{\mathrm{disc}} \times \mathbb{R}$, where $\mathbb{R}_{\mathrm{disc}}$ is $\mathbb{R}$ with the discrete topology and the product carries the product topology. As a *set* this is the plane $\mathbb{R}^2$, but topologically it is a completely different animal: each horizontal line $\{a\} \times \mathbb{R}$ is open (product of the open set $\{a\}$ with $\mathbb{R}$), and its subspace topology is the usual one on $\mathbb{R}$. Thus
>
> $$
> X \;\cong\; \bigsqcup_{a \in \mathbb{R}} \mathbb{R},
> $$
>
> a disjoint union of uncountably many copies of $\mathbb{R}$ (“an enormous line”), and:
> - *$T_2$:* any two points on the same line are separated inside that line; points on different lines are separated by the lines themselves.
> - *Locally Euclidean of dimension $1$:* the neighborhood $\{a\} \times \mathbb{R}$ of $(a, t)$ is homeomorphic to $\mathbb{R}$ via projection.
> - *Not second countable:* each line $\{a\} \times \mathbb{R}$ is a nonempty open set, so any basis must contain some nonempty $U_\alpha \subseteq \{a\} \times \mathbb{R}$. Distinct lines are disjoint, so distinct $a$ give distinct $U_\alpha$, and there are uncountably many $a$.
>
> *Lee: Problem 1-2, an uncountable disjoint union of lines*

^ex-2-3

*Uses:* [[§1 Point-Set Topology Review#^def-1-5|Def. §1.5]], [[§1 Point-Set Topology Review#^def-1-7|Def. §1.7]], [[§2 Topological Manifolds#^def-2-1|Def. §2.1]], [[§3 Subspaces and Products#^def-3-3|Def. §3.3]], [[§4 Product Topology#^def-4-1|590 Def. §4.1]]

> [!theorem] Proposition §2.4: The Three Conditions Are Independent
> Second countability, the Hausdorff property, and local Euclideanness are independent: for each of the three there is a space satisfying the other two but not it.
>
> *Lee: Problems 1-1 and 1-2*

^prop-2-4

> [!proof]+ Proof
> *(Lecture 1 gave the three examples, each with a one-line reason; the verifications are in the examples above.)* The examples above exhibit this, organized by the property that fails: $\mathbb{R}_{\mathrm{disc}} \times \mathbb{R}$ fails only second countability ([[§2 Topological Manifolds#^ex-2-3|Example §2.3]]); the line with two origins fails only the Hausdorff property ([[§2 Topological Manifolds#^ex-2-1|Example §2.1]]); and $\mathbb{Q}$ fails only local Euclideanness ([[§2 Topological Manifolds#^ex-2-2|Example §2.2]]).

^pf-2-4

*Uses:* [[§2 Topological Manifolds#^ex-2-1|Ex. §2.1]], [[§2 Topological Manifolds#^ex-2-2|Ex. §2.2]], [[§2 Topological Manifolds#^ex-2-3|Ex. §2.3]], [[§1 Point-Set Topology Review#^ex-1-4|Ex. §1.4]]

> [!remark] Remark: Dimension-Zero Version
> A student observed that $\mathbb{R}_{\mathrm{disc}}$ alone already works: it is $T_2$ (discrete), locally Euclidean of dimension $0$ (each $\{x\}$ is an open neighborhood homeomorphic to $\mathbb{R}^0 = \{\text{pt}\}$), and not second countable ([[§1 Point-Set Topology Review#^ex-1-2|Example §1.2]]). The next proposition says exactly why: it is uncountable.

^rem-2-6

> [!theorem] Proposition §2.5: Zero-Dimensional Manifolds
> A topological space is a topological manifold of dimension $0$ if and only if it is a countable discrete space.
>
> *Lee: Example 1.21*

^prop-2-5

> [!proof]+ Proof
> ($\Rightarrow$) $\mathbb{R}^0$ is a single point, so every $p$ has an open neighborhood homeomorphic to a point, i.e. $\{p\}$ is open, and $X$ is discrete. In a discrete space every basis contains each singleton, since $\{p\}$ is the only open set $B$ with $p \in B \subseteq \{p\}$; so a countable basis forces $X$ to be countable. ($\Leftarrow$) A countable discrete space is Hausdorff, has the countable basis $\{\{p\} \mid p \in X\}$, and each $\{p\}$ is an open neighborhood homeomorphic to $\mathbb{R}^0$.

^pf-2-5

*Uses:* [[§2 Topological Manifolds#^def-2-2|Def. §2.2]], [[§1 Point-Set Topology Review#^def-1-1|Def. §1.1]], [[§1 Point-Set Topology Review#^def-1-5|Def. §1.5]], [[§1 Point-Set Topology Review#^ex-1-2|Ex. §1.2]], [[§2 Basis for a Topology#^rem-2-2|590 §2 (Characterization of Discrete Topology)]]

> [!remark] Remark: A Warning: $\mathbb{R}_{\mathrm{disc}} \times \mathbb{R}$ vs. $\mathbb{R}^2$
> A student asked whether the horizontal lines are homeomorphic to $\mathbb{R}^2$. No: each line is a $1$-dimensional open subset. Since no two Euclidean spaces of different dimensions are homeomorphic ([[§2 Topological Manifolds#^thm-2-1|Theorem §2.1]]), $X$ is not homeomorphic to $\mathbb{R}^2$ even though it has the same underlying set. The topology, not the set, is what determines the dimension.

^rem-2-7

The failure of second countability in the last example is detected by counting components. This is the mechanism Uribe alluded to (“when you have a countable basis, the number of connected components is countable”); the precise statement needs local connectedness, which locally Euclidean spaces have.

> [!theorem] Proposition §2.6: Countably Many Components
> If $X$ is locally Euclidean and second countable, then $X$ has at most countably many connected components.
>
> *Lee: Proposition 1.11(d)*

^prop-2-6

> [!proof]+ Proof (not given in lecture)
> First, each connected component $C$ of $X$ is open. Indeed, let $p \in C$ and let $\varphi : U \to \mathbb{R}^n$ be a homeomorphism from a neighborhood $U$ of $p$. Then $U \subseteq C$ ([[§1 Point-Set Topology Review#^prop-1-7|Proposition §1.7]]: $U$ is connected by (4), and the component of $p$ contains every connected set through $p$). Hence $C$ is a union of open sets.
>
> Now let $\{U_\alpha\}_{\alpha \in A}$ be a countable basis. For each component $C$, pick $p_C \in C$; since $C$ is open, there is $\alpha_C \in A$ with $p_C \in U_{\alpha_C} \subseteq C$. Distinct components are disjoint, so $C \mapsto \alpha_C$ is injective into the countable set $A$.

^pf-2-6

*Uses:* [[§2 Topological Manifolds#^def-2-1|Def. §2.1]], [[§1 Point-Set Topology Review#^def-1-8|Def. §1.8]], [[§1 Point-Set Topology Review#^prop-1-7|§1.7]], [[§1 Point-Set Topology Review#^def-1-1|Def. §1.1]], [[§1 Point-Set Topology Review#^def-1-5|Def. §1.5]]

**Rigor flag.** “Second countable $\Rightarrow$ countably many components” is *false* without local connectedness: the Cantor set is a compact metric (hence second countable) space with uncountably many components (each a point). The proposition uses locally Euclidean only through “components are open,” i.e. local connectedness.

## The Sphere

> [!example] Example §2.4: $S^2$ is a Topological $2$-Manifold
> Let $S^2 = \{x \in \mathbb{R}^3 \mid |x| = 1\}$ with the subspace topology.
> - *$T_2$ and second countable:* $S^2$ is a metric space (restriction of the Euclidean metric), hence $T_2$; and a subspace of a second countable space is second countable (intersect a countable basis of $\mathbb{R}^3$ with $S^2$).
> - *Locally Euclidean:* let $p = (p_1, p_2, p_3) \in S^2$. Since $|p| = 1$, some coordinate of $p$ is nonzero. Upon relabeling coordinates (and possibly replacing $z$ by $-z$), we may assume **WLOG that the $z$-coordinate of $p$ is positive**. Let
>
>   $$
>   U = \{(x, y, z) \in S^2 \mid z > 0\} \quad \text{(the open northern hemisphere)},
>   $$
>
>   $$
>   \varphi : U \to \mathbb{R}^2, \qquad (x, y, z) \mapsto (x, y).
>   $$
>
>   $U$ is open in $S^2$ (preimage of $(0, \infty)$ under the continuous coordinate function $z$), and $p \in U$.
>
>   **Claim:** $\varphi$ is a homeomorphism of $U$ onto the open unit disk $D = \{(x, y) \mid x^2 + y^2 < 1\} \subseteq \mathbb{R}^2$.
>
> *Lee: Example 1.4*

^ex-2-4

> [!proof]+ Proof of Claim (not given in lecture)
> *Image:* for $(x, y, z) \in U$, $x^2 + y^2 = 1 - z^2 < 1$ since $0 < z \le 1$, so $\varphi(U) \subseteq D$. Conversely, for $(x, y) \in D$, the point $(x, y, \sqrt{1 - x^2 - y^2})$ lies in $U$ and maps to $(x, y)$; so $\varphi(U) = D$.
>
> *Injective:* if $(x, y, z), (x, y, z') \in U$, then $z = \sqrt{1 - x^2 - y^2} = z'$, using $z, z' > 0$.
>
> *Continuous with continuous inverse:* $\varphi$ is the restriction of the projection $\mathbb{R}^3 \to \mathbb{R}^2$, hence continuous. The inverse $\varphi^{-1} : D \to U$, $(x, y) \mapsto (x, y, \sqrt{1 - x^2 - y^2})$, is continuous as a map into $\mathbb{R}^3$ (each component is continuous on $D$), hence continuous into the subspace $U$.
>
> Since $D$ is open in $\mathbb{R}^2$, [[§2 Topological Manifolds#^prop-2-3|Proposition §2.3]] shows $S^2$ is locally Euclidean of dimension $2$ at $p$.

^pf-ex-2-4

*Uses:* [[§2 Topological Manifolds#^prop-2-3|§2.3]], [[§1 Point-Set Topology Review#^prop-1-6|§1.6]], [[§1 Point-Set Topology Review#^prop-1-5|§1.5]] (4), [[§9 Continuous Functions#^thm-9-4|590 §9.4]], [[§18 Countability Axioms#^thm-18-3|590 §18.3]]

![[m591-2-1.svg]]
*The hemisphere chart: projection $(x,y,z) \mapsto (x,y)$ carries the open northern hemisphere $U = \{z > 0\}$ homeomorphically onto the open unit disk in $\mathbb{R}^2$.*

> [!theorem] Proposition §2.7: Spheres Are Topological Manifolds
> $S^n = \{x \in \mathbb{R}^{n+1} \mid |x| = 1\}$ is a topological $n$-manifold.
>
> *Lee: Example 1.4*

^prop-2-7

> [!proof]+ Proof
> As in [[§2 Topological Manifolds#^ex-2-4|Example §2.4]], $S^n$ is a metric space (restriction of the Euclidean metric), hence Hausdorff, and second countable: intersecting a countable basis of $\mathbb{R}^{n+1}$ with $S^n$ gives a countable basis. The $2(n+1)$ open hemispheres $U_i^{\pm} = \{x \in S^n \mid \pm x_i > 0\}$ cover $S^n$, since every point has a nonzero coordinate. On $U_i^\pm$, the map $\varphi_i^\pm$ forgetting the $i$-th coordinate is continuous and lands in the open unit ball $B^n$, because the remaining coordinates satisfy $\sum_{j \ne i} x_j^2 = 1 - x_i^2 < 1$. Its inverse inserts $\pm\sqrt{1 - |y|^2}$ in slot $i$ and is continuous. So each $\varphi_i^\pm$ is a homeomorphism onto the open set $B^n \subseteq \mathbb{R}^n$, and [[§2 Topological Manifolds#^prop-2-3|Proposition §2.3]] applies.

^pf-2-7

*Uses:* [[§2 Topological Manifolds#^ex-2-4|Ex. §2.4]], [[§2 Topological Manifolds#^def-2-2|Def. §2.2]], [[§2 Topological Manifolds#^prop-2-3|§2.3]], [[§1 Point-Set Topology Review#^prop-1-6|§1.6]], [[§18 Countability Axioms#^thm-18-3|590 §18.3]]

> [!remark]- Connections
> - The hemisphere charts as an atlas: [[§13 Differentiable Structures#^def-13-6|Def. §13.6]]; the circle case with its smooth atlases is [[§13 Differentiable Structures#^ex-13-2|Ex. §13.2]].

> [!remark] Remark
> This is the argument of [[§2 Topological Manifolds#^ex-2-4|Example §2.4]], for every $n$ (Lee, Example 1.4). The hemisphere charts will be our first example of an *atlas*, and the maps between overlapping charts ([[§2 Topological Manifolds#Charts and Transition Functions|§2, Charts and Transition Functions]]) will turn out to be smooth.

^rem-2-8

Many spaces are *not* topological manifolds (e.g. two lines crossing, a cone point, a closed disk—the last of these is a manifold *with boundary*). There was no time to discuss these in lecture; the homework is where such examples live. Uribe emphasized that the most interesting examples of the course are in the homework, which is a reason to do it without AI.

## Connectedness and Path Connectedness

> [!remark] Remark
> For general topological spaces, path connectedness is strictly stronger than connectedness (the topologist's sine curve is the standard counterexample, [[§14 Connected Subspaces of ℝ#^ex-14-7|590 §14]]). For manifolds the two coincide, because being locally Euclidean makes the space locally path connected. This is PSet 1, Problem 1.

^rem-2-9

> [!theorem] Lemma §2.8: Concatenation and Reversal of Paths
> Let $X$ be a topological space. If $\alpha$ is a path from $a$ to $b$ and $\beta$ a path from $b$ to $c$, then there is a path from $a$ to $c$. If $\alpha$ is a path from $a$ to $b$, there is a path from $b$ to $a$.
>
> *Lee: App. A, “Connectedness and Compactness”*

^lem-2-8

> [!proof]+ Proof
> Define $\gamma : [0,1] \to X$ by $\gamma(t) = \alpha(2t)$ for $t \in [0, \tfrac12]$ and $\gamma(t) = \beta(2t-1)$ for $t \in [\tfrac12, 1]$. The two formulas agree at $t = \tfrac12$, where both give $\alpha(1) = b = \beta(0)$, so $\gamma$ is well defined. The sets $[0,\tfrac12]$ and $[\tfrac12,1]$ are closed and cover $[0,1]$, and $\gamma$ is continuous on each (a composite of an affine map with $\alpha$, resp. $\beta$), so $\gamma$ is continuous by the [[Pasting Lemma|pasting lemma]] ([[§9 Continuous Functions#^thm-9-5|590 §9]]). Finally $\gamma(0) = a$, $\gamma(1) = c$. For the reversal, $t \mapsto \alpha(1-t)$ is continuous and runs from $b$ to $a$.

^pf-2-8

*Uses:* [[Pasting Lemma|590 §9.5 (Pasting Lemma)]], [[§14 Connected Subspaces of ℝ#^def-14-3|590 Def. §14.3]]

> [!remark]- Connections
> - The same concatenation is the product of paths in 590: [[§22 Homotopy of Paths#^def-22-6|590 Def. §22.6]], with its algebra in [[Properties of Path Concatenation]].

> [!theorem] Theorem §2.9: Connected Manifolds Are Path Connected
> A connected topological manifold is path connected.
>
> *Lee: Proposition 1.11(b)*

^thm-2-9

> [!proof]+ Proof
> Let $M$ be a connected topological manifold; we may assume $M \neq \emptyset$, the empty space being vacuously path connected.
>
> *Step 1: every point has a path-connected open neighborhood.* Let $x \in M$ and let $\varphi : U_x \to \mathbb{R}^n$ be a homeomorphism from a neighborhood of $x$. For $x', x'' \in U_x$, the straight-line path $\gamma(t) = (1-t)\varphi(x') + t\varphi(x'')$ is continuous in $\mathbb{R}^n$, so $\varphi^{-1} \circ \gamma$ is a path in $U_x$ from $x'$ to $x''$. Hence $U_x$ is path connected.
>
> *Step 2: the set of points reachable from a base point is clopen.* Fix $x_0 \in M$ and let
>
> $$
> S = \{\, x \in M \mid \text{there is a path in } M \text{ from } x_0 \text{ to } x \,\}.
> $$
>
> $S \neq \emptyset$: the constant path shows $x_0 \in S$. Both openness and closedness follow from one observation: *if $U$ is a path-connected set and $U \cap S \neq \emptyset$, then $U \subseteq S$*—for $z \in U \cap S$ and $y \in U$, concatenate a path from $x_0$ to $z$ with one from $z$ to $y$ ([[§2 Topological Manifolds#^lem-2-8|Lemma §2.8]]). Now: if $x \in S$, then $U_x \cap S \ni x$, so $U_x \subseteq S$ and $S$ is open; if $y \notin S$, then $U_y \cap S = \emptyset$ (else $U_y \subseteq S \ni y$), so $U_y \subseteq M \setminus S$ and $M \setminus S$ is open.
>
> *Step 3.* $S$ is a nonempty subset of the connected space $M$ that is both open and closed, so $S = M$. Given $x, y \in M$, reverse a path from $x_0$ to $x$ and concatenate with one from $x_0$ to $y$ ([[§2 Topological Manifolds#^lem-2-8|Lemma §2.8]]) to get a path from $x$ to $y$.

^pf-2-9

*Uses:* [[§2 Topological Manifolds#^def-2-2|Def. §2.2]], [[§2 Topological Manifolds#^def-2-1|Def. §2.1]], [[§2 Topological Manifolds#^lem-2-8|§2.8]], [[§13 Connected Spaces#^lem-13-1|590 §13.1]], [[§14 Connected Subspaces of ℝ#^def-14-3|590 Def. §14.3]]

> [!theorem] Corollary §2.10: Components of a Manifold
> Let $M$ be a topological manifold. Then the connected components of $M$ are open, coincide with its path components, and each is itself a topological manifold of the same dimension.
>
> *Lee: Proposition 1.11(c) and (d)*

^cor-2-10

> [!proof]+ Proof
> A component $C$ is open: for $p \in C$ the connected set $U_p$ (homeomorphic to $\mathbb{R}^n$, connected by [[§1 Point-Set Topology Review#^prop-1-7|Proposition §1.7]](4)) contains $p$, hence lies in $C$. Being open in $M$, $C$ is a manifold of the same dimension by the open-submanifold remark of [[§3 Subspaces and Products#^prop-3-6|§3.6]], and it is connected, hence path connected by [[§2 Topological Manifolds#^thm-2-9|Theorem §2.9]]; so $C$ is contained in the path component of any of its points. Conversely a path-connected set is connected, so the path component of $p$ is contained in $C$.

^pf-2-10

*Uses:* [[§1 Point-Set Topology Review#^def-1-8|Def. §1.8]], [[§1 Point-Set Topology Review#^prop-1-7|§1.7]], [[§3 Subspaces and Products#^prop-3-6|§3.6]], [[§2 Topological Manifolds#^thm-2-9|§2.9]], [[§14 Connected Subspaces of ℝ#^thm-14-4|590 §14.4]]

> [!remark] Remark
> This is the mechanism behind [[§2 Topological Manifolds#^prop-2-6|Proposition §2.6]]: openness of the components is what turns second countability into a bound on their number. It is also the reason [[§2 Topological Manifolds#^cor-2-2|Corollary §2.2]] can speak of the dimension being constant on components.

^rem-2-10

## Charts and Transition Functions

*Reference: Lee Ch. 1, “Coordinate Charts.” Presented in the last minutes of Lecture 1 as a preview; the topological content is recorded here, the smooth version is [[· 3 Smooth Structures|Chapter 3]].*

Suppose $X$ is a topological manifold of dimension $n$, and let $p \in X$. By definition (in the form of [[§2 Topological Manifolds#^prop-2-3|Proposition §2.3]]), there is a neighborhood $U$ of $p$ and a homeomorphism $\varphi : U \to A$ onto an open set $A \subseteq \mathbb{R}^n$.

> [!definition] Definition §2.3: Chart
> Let $X$ be a topological space and $p \in X$. A **chart** at $p$ is a pair $(U, \varphi)$ where $U$ is an open neighborhood of $p$ and $\varphi : U \to A$ is a homeomorphism onto an open set $A \subseteq \mathbb{R}^n$.
>
> *Lee: Ch. 1, “Coordinate Charts”*

^def-2-3

> [!remark]- Connections
> - Restated at the start of Chapter 3: [[§13 Differentiable Structures#^def-13-1|Def. §13.1]]; the smooth version is [[§15 Smooth Functions and Smooth Maps#^def-15-1|Smooth Chart, Def. §15.1]].

> [!theorem] Lemma §2.11: Restricting and Recomposing Charts
> Let $(U, \varphi)$ be a chart on a topological $n$-manifold: $\varphi$ is a homeomorphism of the open set $U$ onto an open subset of $\mathbb{R}^n$.
> 1. If $U' \subseteq U$ is open, then $(U', \varphi|_{U'})$ is a chart.
> 2. If $h$ is a homeomorphism of an open set $W \supseteq \varphi(U)$ onto an open subset of $\mathbb{R}^n$, then $(U, h \circ \varphi)$ is a chart.
>
> *Lee: Ch. 1, “Coordinate Charts”*

^lem-2-11

> [!proof]+ Proof
> (1) By [[§1 Point-Set Topology Review#^prop-1-5|Proposition §1.5]](3), $\varphi|_{U'}$ is a homeomorphism onto $\varphi(U')$, which is open in $\varphi(U)$. An open subset of the open set $\varphi(U)$ has the form $V \cap \varphi(U)$ with $V$ open in $\mathbb{R}^n$, an intersection of two open sets, so $\varphi(U')$ is open in $\mathbb{R}^n$. (2) $h \circ \varphi$ is a homeomorphism onto $h(\varphi(U))$, which is open in $h(W)$ by the same fact, hence in $\mathbb{R}^n$ by the same argument.

^pf-2-11

*Uses:* [[§2 Topological Manifolds#^def-2-3|Def. §2.3]], [[§1 Point-Set Topology Review#^prop-1-5|§1.5]], [[§3 Subspaces and Products#^def-3-1|Def. §3.1]], [[§5 Subspace Topology#^lem-5-2|590 §5.2]]

> [!remark] Remark: Charts Are Not Unique
> Nothing in the definition pins down $U$ or $\varphi$: by the lemma, a chart can be shrunk or recomposed at will. Consequently, the fundamental picture of the first weeks of the course is: *two* charts at the same point, and the map that compares them.

^rem-2-11

Let $\varphi : U \to A$ and $\psi : V \to B$ be two charts at $p$, with $A, B \subseteq \mathbb{R}^n$ open. The overlap $U \cap V$ is an open neighborhood of $p$, and it appears in both charts as the open sets $\varphi(U \cap V) \subseteq A$ and $\psi(U \cap V) \subseteq B$.

![[m591-2-2.svg]]
*The overlap $U \cap V$ seen in both charts: $\varphi$ and $\psi$ carry it to open subsets of $\mathbb{R}^n$, compared by $\psi \circ \varphi^{-1}$.*

> [!definition] Definition §2.4: Transition Function (Preliminary)
> The **transition function** from the chart $(U, \varphi)$ to the chart $(V, \psi)$ is the map
>
> $$
> \psi \circ \varphi^{-1} : \varphi(U \cap V) \longrightarrow \psi(U \cap V),
> $$
>
> where $\varphi^{-1}$ is restricted to $\varphi(U \cap V)$.

^def-2-4

> [!remark]- Connections
> - Chapter 3 asks these maps to be smooth: [[§13 Differentiable Structures#^def-13-4|Smoothly Compatible Charts, Def. §13.4]].

> [!theorem] Proposition §2.12: Transition Functions Are Homeomorphisms
> For a topological manifold, $\varphi(U \cap V)$ and $\psi(U \cap V)$ are open subsets of $\mathbb{R}^n$, and $\psi \circ \varphi^{-1}$ is a homeomorphism between them, with inverse $\varphi \circ \psi^{-1}$.
>
> *Lee: Ch. 1, “Smooth Structures”*

^prop-2-12

> [!proof]+ Proof
> *(Stated in Lecture 1 — “for a topological manifold, this will be a continuous map, homeomorphism actually”; filled in.)* $U \cap V$ is open in $U$, so $\varphi(U \cap V)$ is open in $A$ ($\varphi$ is a homeomorphism, hence an open map), and therefore open in $\mathbb{R}^n$ since $A$ is; likewise for $\psi(U \cap V)$. The map $\varphi^{-1}|_{\varphi(U \cap V)} : \varphi(U \cap V) \to U \cap V$ is a homeomorphism (restriction of one), as is $\psi|_{U \cap V} : U \cap V \to \psi(U \cap V)$; their composite is a homeomorphism.

^pf-2-12

*Uses:* [[§2 Topological Manifolds#^def-2-3|Def. §2.3]], [[§2 Topological Manifolds#^def-2-4|Def. §2.4]], [[§1 Point-Set Topology Review#^prop-1-5|§1.5]], [[§5 Subspace Topology#^lem-5-2|590 §5.2]]

![[m591-2-3.svg]]
*Two charts on the same manifold. On the overlap $U \cap V$ (orange) both charts apply, and the two pictures of it, $\varphi(U \cap V)$ and $\psi(U \cap V)$, are compared by the transition map $\psi \circ \varphi^{-1}$ — a homeomorphism between open subsets of $\mathbb{R}^n$ by [[§2 Topological Manifolds#^prop-2-12|Proposition §2.12]]. [[· 3 Smooth Structures|Chapter 3]] defines smooth structures by asking these maps to be smooth.*

> [!example] Example §2.5: Two Hemisphere Charts on $S^2$
> Take $U = \{z > 0\}$ with $\varphi(x, y, z) = (x, y)$ and $V = \{x > 0\}$ with $\psi(x, y, z) = (y, z)$, both charts onto the open unit disk. Then $U \cap V = \{x > 0, z > 0\}$, $\varphi(U \cap V) = \{(x, y) \in D \mid x > 0\}$, and
>
> $$
> \psi \circ \varphi^{-1}(x, y) = \psi\big(x, y, \sqrt{1 - x^2 - y^2}\big) = \big(y, \sqrt{1 - x^2 - y^2}\big).
> $$
>
> Note that this map is not merely continuous but $C^\infty$ on its (open) domain, since $1 - x^2 - y^2 > 0$ there. This is no accident, and it is the point of the [[§13 Differentiable Structures#^def-13-4|next definition]].

^ex-2-5

*Uses:* [[§2 Topological Manifolds#^ex-2-4|Ex. §2.4]], [[§2 Topological Manifolds#^def-2-4|Def. §2.4]]

> [!remark] Remark: Preview: What Makes a Manifold *Differentiable*
> For a topological manifold, transition functions are homeomorphisms between open subsets of $\mathbb{R}^n$—and that is all one can say. To speak of *differentiable* manifolds, we will **require** that all transition functions be differentiable (in fact $C^\infty$).
>
> Why is this the right move? Differentiability is not a topological notion: it makes no sense to ask whether a map $X \to \mathbb{R}$ on an abstract topological space is differentiable, because $X$ has no linear structure. What *does* make sense is to pull $f$ back to Euclidean space via a chart, $f \circ \varphi^{-1} : A \to \mathbb{R}$, and ask whether *that* is differentiable. For this to be independent of the chart chosen, one needs $f \circ \psi^{-1} = (f \circ \varphi^{-1}) \circ (\varphi \circ \psi^{-1})$ to be differentiable whenever $f \circ \varphi^{-1}$ is—which is exactly the requirement that transition functions be differentiable. (He expected to begin this on Wednesday; in the event, Lecture 2 stayed with topology—see [[§3 Subspaces and Products|§3]].)

^rem-2-12

> [!remark]- Connections
> - Carried out in [[§13 Differentiable Structures#^def-13-2|Def. §13.2]] (smooth in the sense of a chart), [[§13 Differentiable Structures#^rem-13-3|the problem this creates]] and [[§13 Differentiable Structures#^thm-13-1|§13.1]].
