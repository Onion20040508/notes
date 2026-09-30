---
type: section
subject: "[[Topology]]"
chapter: 10
section: 26
munkres: "§58"
tags: [topology, math590]
---
← [[Topology §25 The Fundamental Theorem of Algebra]] · ↑ [[Topology — 10 Applications of π₁]] · [[Topology §27 The Fundamental Group of Sⁿ]] →

## Homotopic Maps Induce the Same Homomorphism

> [!theorem] Lemma §26.1: Homotopic Maps and Induced Homomorphisms
> Let $h, k: (X, x_0) \to (Y, y_0)$ be continuous. If $h$ and $k$ are homotopic, and the image of $x_0$ remains fixed at $y_0$ during the homotopy, then $h_* = k_*$ as homomorphisms $\pi_1(X, x_0) \to \pi_1(Y, y_0)$.

^lem-26-1

> [!remark]- Connections
> - Generalized to a moving basepoint: [[Topology §26 Deformation Retracts and Homotopy Type#^lem-26-14|Homotopic Maps and π₁: General Case]].

> [!proof]+ Proof
> Let $H: X \times I \to Y$ be the homotopy with $H(x, 0) = h(x)$, $H(x, 1) = k(x)$, and $H(x_0, t) = y_0$ for all $t$.
>
> Let $[f] \in \pi_1(X, x_0)$, where $f: I \to X$ is a loop at $x_0$. Consider the composition:
>
> $$
> I \times I \xrightarrow{f \times \operatorname{id}} X \times I \xrightarrow{H} Y.
> $$
>
> This map sends $(s, t) \mapsto H(f(s), t)$, and is a [[Topology §22 Homotopy of Paths#^def-22-4|path homotopy]] between $h \circ f$ and $k \circ f$:
> - $(s, 0) \mapsto H(f(s), 0) = h(f(s))$, i.e., the path $h \circ f$.
> - $(s, 1) \mapsto H(f(s), 1) = k(f(s))$, i.e., the path $k \circ f$.
> - $(0, t) \mapsto H(f(0), t) = H(x_0, t) = y_0$. Endpoints fixed.
> - $(1, t) \mapsto H(f(1), t) = H(x_0, t) = y_0$. Endpoints fixed.
>
> So $h \circ f \simeq_p k \circ f$, giving $[h \circ f] = [k \circ f]$, i.e., $h_*([f]) = k_*([f])$.

^pf-26-1

*Uses:* [[Topology §22 Homotopy of Paths#^def-22-4|Def. §22.4]], [[Topology §23 The Fundamental Group#^def-23-4|Def. §23.4]]

## Application: $S^n \hookrightarrow \mathbb{R}^{n+1} \setminus \{0\}$ Induces an Isomorphism

> [!theorem] Theorem §26.2: $\pi_1(S^n) \cong \pi_1(\mathbb{R}^{n+1} \setminus \{0\})$
> The inclusion $j: S^n \hookrightarrow \mathbb{R}^{n+1} \setminus \{0\}$ induces an isomorphism on fundamental groups.

^thm-26-2

> [!proof]+ Proof
> Let $X = \mathbb{R}^{n+1} \setminus \{0\}$ and $b_0 = (1, 0, \ldots, 0)$. Define $r: X \to S^n$ by $r(x) = x / \|x\|$.
>
> **$j_*$ is injective:** $r \circ j: S^n \to S^n$ is the identity map, so $(r \circ j)_* = r_* \circ j_* = \operatorname{id}$ on $\pi_1(S^n, b_0)$. If $j_*([f]) = [e]$, then $[f] = r_*(j_*([f])) = r_*([e]) = [e]$. So $j_*$ is injective.
>
> **$j_*$ is surjective:** We show $j \circ r: X \to X$ is homotopic to $\operatorname{id}_X$ with $b_0$ fixed. Define:
>
> $$
> H: X \times I \to X, \qquad H(x, t) = (1-t)x + t\frac{x}{\|x\|}.
> $$
>
> This is continuous and well-defined: for each $t$, $H(x, t)$ is a convex combination of $x$ and $x/\|x\|$, both nonzero, so $H(x, t) \neq 0$ (since $x$ and $x/\|x\|$ point in the same direction).
>
> Check: $H(x, 0) = x = \operatorname{id}_X(x)$ and $H(x, 1) = x/\|x\| = (j \circ r)(x)$. Also $H(b_0, t) = (1-t)b_0 + tb_0 = b_0$.
>
> By [[Topology §26 Deformation Retracts and Homotopy Type#^lem-26-1|the lemma]], $(j \circ r)_* = j_* \circ r_* = \operatorname{id}$ on $\pi_1(X, b_0)$. So for any $[g] \in \pi_1(X, b_0)$: $[g] = j_*(r_*([g]))$, showing $j_*$ is surjective.

^pf-26-2

*Uses:* [[Functoriality of π₁|§23.5]], [[Topology §26 Deformation Retracts and Homotopy Type#^lem-26-1|§26.1]]

![[m590-26-8.svg]]
*The homotopy $H(x,t) = (1-t)x + t\,x/\|x\|$ slides every point along its own ray (red) to the blue unit sphere, from outside and from inside alike. Nothing ever reaches the removed origin, and points of $S^n$ never move, so $S^n$ is a [[Topology §26 Deformation Retracts and Homotopy Type#^ex-26-7|deformation retract]] of $\mathbb{R}^{n+1} \setminus \{0\}$ (drawn for $n = 1$). Keeping only the outer arrows gives [[Topology §26 Deformation Retracts and Homotopy Type#^ex-26-4|Example §26.4]].*

## Retractions

> [!definition] Definition §26.1: Retraction
> Let $A \subseteq X$. A continuous map $r: X \to A$ is a **retraction** of $X$ onto $A$ if $r(a) = a$ for all $a \in A$, i.e., $r \circ j = \operatorname{id}_A$ where $j: A \hookrightarrow X$ is the inclusion.
>
> If such an $r$ exists, $A$ is called a **retract** of $X$.

^def-26-1

> [!remark]- Connections
> - The group-theoretic preview in §21: [[Topology §21 Algebra Prerequisites꞉ Groups#^rem-21-8|Why This Matters for π₁: Two Directions from a Retraction]].

> [!theorem] Proposition §26.3: Algebraic Properties of Retractions
> Let $A$ be a retract of $X$ with retraction $r: X \to A$ and inclusion $j: A \hookrightarrow X$. Then:
> 1. $j_*: \pi_1(A, x_0) \to \pi_1(X, x_0)$ is injective.
> 2. $r_*: \pi_1(X, x_0) \to \pi_1(A, x_0)$ is surjective.

^prop-26-3

> [!proof]+ Proof
> The equation $r \circ j = \operatorname{id}_A$ gives, by [[Functoriality of π₁|functoriality]]:
>
> $$
> r_* \circ j_* = \operatorname{id}_{\pi_1(A)}.
> $$
>
> **(1)** If $j_*([f]) = j_*([g])$, apply $r_*$ to both sides: $[f] = (r_* \circ j_*)([f]) = (r_* \circ j_*)([g]) = [g]$.
>
> **(2)** For any $[\gamma] \in \pi_1(A)$, the element $j_*([\gamma]) \in \pi_1(X)$ maps to it: $r_*(j_*([\gamma])) = [\gamma]$.

^pf-26-3

*Uses:* [[Functoriality of π₁|§23.5]]

> [!remark] Remark
> But that is *all* you get. $\pi_1(A)$ injects into $\pi_1(X)$, and $r_*$ surjects onto $\pi_1(A)$, but $\pi_1(X)$ can be strictly larger than $\pi_1(A)$.
>
> **Example:** $X = S^1 \vee S^1$, $A$ = one of the two circles. The map $r$ that collapses the other circle to the [[Topology §28 Fundamental Group of Some Surfaces#^def-28-3|wedge point]] is a retraction. Here $\pi_1(A) \cong \mathbb{Z}$ and $\pi_1(X) \cong F_2$. The inclusion $j_*$ embeds $\mathbb{Z}$ as one free factor of $F_2$, and $r_*$ projects $F_2$ onto that factor. But $F_2 \not\cong \mathbb{Z}$ — the retraction does not force the fundamental groups to be isomorphic.
>
> **For a full isomorphism $\pi_1(X) \cong \pi_1(A)$, we need the stronger notion of a deformation retract** (see [[Topology §26 Deformation Retracts and Homotopy Type#^def-26-3|below]]).

^rem-26-1

> [!theorem] Corollary §26.4: What Properties Transfer via Retraction
> Let $A$ be a retract of $X$. Then $\pi_1(A)$ is simultaneously a subgroup of $\pi_1(X)$ (via $j_*$) and a quotient of $\pi_1(X)$ (via $r_*$).
>
> **Up** (from $A$ to $X$, via $j_*$ injective): any property [[Topology §21 Algebra Prerequisites꞉ Groups#^prop-21-9|inherited by subgroups]] transfers upward. If $\pi_1(A)$ is non-abelian, nontrivial, infinite, or has torsion, so does $\pi_1(X)$.
>
> **Down** (from $X$ to $A$, via $r_*$ surjective): any property [[Topology §21 Algebra Prerequisites꞉ Groups#^prop-21-10|inherited by quotients]] transfers downward. If $\pi_1(X)$ is abelian or finitely generated, so is $\pi_1(A)$.

^cor-26-4

*Uses:* [[Topology §26 Deformation Retracts and Homotopy Type#^prop-26-3|§26.3]], [[Topology §21 Algebra Prerequisites꞉ Groups#^prop-21-9|§21.9]], [[Topology §21 Algebra Prerequisites꞉ Groups#^prop-21-10|§21.10]]

> [!example] Example §26.1: $\pi_1(\Sigma_2)$ is Non-Abelian
> The [[Topology §28 Fundamental Group of Some Surfaces#^def-28-4|figure eight]] $S^1 \vee S^1$ retracts from $\Sigma_2$, so $F_2 = \pi_1(S^1 \vee S^1)$ embeds in $\pi_1(\Sigma_2)$. Since $F_2$ is non-abelian, $\pi_1(\Sigma_2)$ is non-abelian. The retraction does not tell us *what* $\pi_1(\Sigma_2)$ is — only that it contains $F_2$ as a subgroup.

^ex-26-1

> [!remark]- Connections
> - The full argument, with the retraction constructed: [[Topology §28 Fundamental Group of Some Surfaces#^thm-28-5|π₁(Σ₂) is Non-Abelian]].
> - $\pi_1(S^1 \vee S^1) \cong F_2$: [[Topology §29 The Seifert–van Kampen Theorem#^ex-29-2|The Figure Eight via van Kampen]].

> [!definition] Definition §26.2: Closed Balls $B^n$ and Spheres $S^{n-1}$
> The **closed unit ball** in $\mathbb{R}^n$ is $B^n = \{x \in \mathbb{R}^n : \|x\| \leq 1\}$. Its boundary is the **unit sphere** $S^{n-1} = \{x \in \mathbb{R}^n : \|x\| = 1\}$.
>
> In particular: $B^2 = \{(x,y) \in \mathbb{R}^2 : x^2 + y^2 \leq 1\}$ is the closed unit disk, with boundary $S^1$.

^def-26-2

> [!theorem] Proposition §26.5: $B^n$ is Convex and Simply Connected
> $B^n$ is convex: if $x, y \in B^n$, then $(1-t)x + ty \in B^n$ for all $t \in [0,1]$.
> Therefore $\pi_1(B^n, x_0) = 0$.

^prop-26-5

> [!remark]- Connections
> - Instance of [[Topology §23 The Fundamental Group#^ex-23-2|Convex Subsets of ℝⁿ are Simply Connected]].

> [!proof]+ Proof
> **Convexity:** By the triangle inequality,
>
> $$
> \|(1-t)x + ty\| \leq (1-t)\|x\| + t\|y\| \leq (1-t) \cdot 1 + t \cdot 1 = 1.
> $$
>
> **$\pi_1 = 0$:** Let $f$ be a loop at $x_0 \in B^n$. The [[Topology §22 Homotopy of Paths#^thm-22-1|straight-line homotopy]] $H(s, t) = (1-t)f(s) + t \cdot x_0$ satisfies $H(s,0) = f(s)$, $H(s,1) = x_0$, and $H(0,t) = H(1,t) = (1-t)x_0 + tx_0 = x_0$. By convexity, $H(s,t) \in B^n$ for all $s, t$. So every loop contracts to a point.

^pf-26-5

*Uses:* [[Topology §22 Homotopy of Paths#^thm-22-1|§22.1]]

> [!theorem] Theorem §26.6: No-Retraction Theorem (Munkres 55.2)
> There is no retraction of $B^2$ onto $S^1$.

^thm-26-6

> [!remark]- Connections
> - All dimensions: [[Topology §26 Deformation Retracts and Homotopy Type#^thm-26-9|Generalized No-Retraction Theorem]].

> [!proof]+ Proof
> Suppose for contradiction that $r: B^2 \to S^1$ is a retraction, i.e., $r$ is continuous and $r(a) = a$ for all $a \in S^1$. We derive a contradiction using $\pi_1$.
>
> **Step 1: Set up the maps.** Let $j: S^1 \hookrightarrow B^2$ be the inclusion map. Since $r$ fixes every point of $S^1$, the composition $r \circ j: S^1 \to S^1$ satisfies $(r \circ j)(a) = r(a) = a$ for all $a \in S^1$. That is,
>
> $$
> r \circ j = \operatorname{id}_{S^1}.
> $$
>
> **Step 2: Apply $\pi_1$ (functoriality).** Both $j$ and $r$ are continuous maps, so by the induced homomorphism construction ([[Topology §23 The Fundamental Group#^def-23-4|§23]]), each gets an induced group homomorphism:
>
> $$
> j_*: \pi_1(S^1, b_0) \to \pi_1(B^2, b_0), \qquad r_*: \pi_1(B^2, b_0) \to \pi_1(S^1, b_0).
> $$
>
> (Here $j_*([f]) = [j \circ f]$ and $r_*([g]) = [r \circ g]$—compose loops with the maps.) By the functorial properties ([[Functoriality of π₁|§23]]):
> - **Composition rule:** $(r \circ j)_* = r_* \circ j_*$.
> - **Identity rule:** $(\operatorname{id}_{S^1})_* = \operatorname{id}$ on $\pi_1(S^1, b_0)$.
>
> Since $r \circ j = \operatorname{id}_{S^1}$, we combine:
>
> $$
> r_* \circ j_* = (r \circ j)_* = (\operatorname{id}_{S^1})_* = \operatorname{id}.
> $$
>
> **Step 3: Conclude $j_*$ is injective.** If $j_*([f]) = j_*([g])$, apply $r_*$ to both sides:
>
> $$
> [f] = (r_* \circ j_*)([f]) = (r_* \circ j_*)([g]) = [g].
> $$
>
> So $j_*$ is injective.
>
> **Step 4: Contradiction.** We have computed $\pi_1(S^1) \cong \mathbb{Z}$ ([[Fundamental Group of the Circle|Theorem §24.10]]) and $\pi_1(B^2) = 0$ ([[Topology §26 Deformation Retracts and Homotopy Type#^prop-26-5|the proposition above]]: $B^2$ is convex, so every loop contracts via the straight-line homotopy). The homomorphism $j_*: \mathbb{Z} \to 0$ must send every element to $0$ (the only element of the trivial group). In particular, $j_*(1) = j_*(2) = 0$, so $j_*$ is not injective. This contradicts Step 3.

^pf-26-6

*Uses:* [[Topology §23 The Fundamental Group#^def-23-4|Def. §23.4]], [[Functoriality of π₁|§23.5]], [[Fundamental Group of the Circle|§24.10]], [[Topology §26 Deformation Retracts and Homotopy Type#^prop-26-5|§26.5]]

![[m590-26-9.svg]]
*The blue boundary loop $f$ generates $\pi_1(S^1, b_0) \cong \mathbb{Z}$, but inside the convex disk the straight-line homotopy $(1-t)f(s) + t\,b_0$ shrinks it (lighter circles) to $b_0$. A retraction $r$ fixes $f$, so it would carry this shrinking into $S^1$ and contract a generator of $\mathbb{Z}$. That is the algebraic contradiction “$j_*: \mathbb{Z} \to 0$ is injective”, drawn as a picture.*

> [!remark] Remark: Why This Matters
> This is the first real application of $\pi_1$: a purely topological fact (no retraction exists) proved using algebra ($\mathbb{Z} \not\cong 0$). The proof pattern — assume a map exists, apply $\pi_1$, get a contradiction from group theory — is the template for all obstruction arguments. The [[Brouwer Fixed Point Theorem|Brouwer fixed point theorem below]] is a direct consequence.

^rem-26-2

> [!theorem] Theorem §26.7: Brouwer Fixed Point Theorem for $B^2$ (Munkres 55.6)
> Every continuous map $f: B^2 \to B^2$ has a fixed point.

^thm-26-7

> [!remark]- Connections
> - The one-dimensional case ($B^1 = [-1,1]$) follows from the [[Intermediate Value Theorem]].
> - All dimensions: [[Topology §26 Deformation Retracts and Homotopy Type#^thm-26-10|Generalized Brouwer Fixed Point Theorem]].

> [!proof]+ Proof
> Suppose $f(x) \neq x$ for all $x \in B^2$. We construct a retraction $r: B^2 \to S^1$, contradicting the [[No-Retraction Theorem|no-retraction theorem]].
>
> **Step 1: Define the ray.** Since $f(x) \neq x$, the points $f(x)$ and $x$ are distinct. Two distinct points in $\mathbb{R}^2$ determine a unique line: starting at $f(x)$, walking in the direction $x - f(x)$ (the vector from $f(x)$ to $x$), we parametrize it as
>
> $$
> \gamma(t) = f(x) + t\bigl(x - f(x)\bigr), \qquad t \in \mathbb{R}.
> $$
>
> At $t = 0$ we are at $f(x)$; at $t = 1$ we are at $x$; for $t > 1$ we continue past $x$ away from $f(x)$. The direction $x - f(x) \neq \mathbf{0}$ precisely because $f(x) \neq x$—this is where the “no fixed point” assumption is used.
>
> The **ray** is the half with $t \geq 0$: it starts at $f(x)$, passes through $x$, and continues outward. Since $f(x) \in B^2$, the ray eventually exits the disk and crosses $S^1$. We define $r(x)$ to be that crossing point.
>
> **Step 2: Find the intersection with $S^1$.** Recall $S^1 = \{v \in \mathbb{R}^2 : \|v\| = 1\}$—the set of points at distance $1$ from the *origin*. So $\gamma(t) \in S^1$ if and only if the point $\gamma(t)$ has distance $1$ from the origin, i.e., $\|\gamma(t)\| = 1$. (Note: $\|\gamma(t)\|$ is not the distance traveled along the ray—it is the distance from $\gamma(t)$ to $(0,0)$ in $\mathbb{R}^2$.) We square both sides to avoid square roots: $\|\gamma(t)\|^2 = 1$, i.e.,
>
> $$
> \|f(x) + t(x - f(x))\|^2 = 1.
> $$
>
> Write $\mathbf{p} = f(x) = (p_1, p_2)$ and $\mathbf{d} = x - f(x) = (d_1, d_2)$. Then $\gamma(t) = (p_1 + td_1,\; p_2 + td_2)$, so:
>
> $$
> \begin{aligned}
> \|\gamma(t)\|^2 &= (p_1 + td_1)^2 + (p_2 + td_2)^2 \\
> &= p_1^2 + 2p_1 d_1 t + d_1^2 t^2 + p_2^2 + 2p_2 d_2 t + d_2^2 t^2 \\
> &= \underbrace{(d_1^2 + d_2^2)}_{\|\mathbf{d}\|^2}\,t^2 + \underbrace{2(p_1 d_1 + p_2 d_2)}_{\text{dot product }\mathbf{p} \cdot \mathbf{d}}\,t + \underbrace{(p_1^2 + p_2^2)}_{\|\mathbf{p}\|^2}.
> \end{aligned}
> $$
>
> Setting $\|\gamma(t)\|^2 = 1$ gives the quadratic $at^2 + bt + c = 0$ where:
>
> $$
> a = \|x - f(x)\|^2, \qquad b = 2\,\mathbf{p} \cdot \mathbf{d}, \qquad c = \|f(x)\|^2 - 1.
> $$
>
> This is a quadratic in $t$ with:
> - $a = \|x - f(x)\|^2 > 0$ (since $f(x) \neq x$ by assumption).
> - $c = \|f(x)\|^2 - 1 \leq 0$ (since $f(x) \in B^2$, so $\|f(x)\| \leq 1$).
>
> By Vieta's formulas, the product of the two roots is $c/a \leq 0$, so one root is $\leq 0$ and the other is $\geq 0$. Define $r(x) = \gamma(t_0)$, where $t_0$ is the larger (hence non-negative) root.
>
> **Step 3: $r(x) \in S^1$.** By construction, $\|\gamma(t_0)\| = 1$.
>
> **Step 4: $r$ is continuous.** The larger root $t_0$ is given by the quadratic formula:
>
> $$
> t_0 = \frac{-b + \sqrt{b^2 - 4ac}}{2a}
> $$
>
> (the “$+$” root, since the other root is $\leq 0$). Since $a, b, c$ depend continuously on $x$ and the discriminant $b^2 - 4ac \geq b^2 \geq 0$ (as $a > 0$, $c \leq 0$), $t_0$ depends continuously on $x$, and hence $r(x) = \gamma(t_0)$ is continuous.
>
> **Step 5: $r$ is a retraction.** For $x \in S^1$, we have $\|x\|^2 = 1$, so $t = 1$ satisfies the quadratic (since $\gamma(1) = x$ and $\|x\| = 1$). Since the other root is $c/a \leq 0 < 1$, the larger root is $t_0 = 1$, giving $r(x) = \gamma(1) = x$.
>
> Thus $r: B^2 \to S^1$ is a retraction, contradicting the no-retraction theorem.

^pf-26-7

*Uses:* [[Topology §26 Deformation Retracts and Homotopy Type#^def-26-1|Def. §26.1]], [[No-Retraction Theorem|§26.6]]

![[m590-26-10.svg]]
*The ray construction. Starting at $f(x)$ and passing through $x$, the ray leaves $B^2$ at $r(x) = \gamma(t_0)$ (red). For a boundary point $y$ the exit point is $y$ itself ($t_0 = 1$), so $r$ fixes $S^1$. The construction needs only one thing: a direction $x - f(x) \neq 0$, i.e. no fixed point.*

> [!remark] Remark
> The Brouwer fixed point theorem is a purely existential result—it tells you a fixed point exists but gives no method for finding it. The proof illustrates the power of algebraic topology: the computation $\pi_1(S^1) \cong \mathbb{Z} \neq 0$ ([[Fundamental Group of the Circle|§24.10]]) (which took real work via [[Topology §24 Covering Spaces|covering spaces]]) has a concrete geometric consequence about maps of the disk to itself.

^rem-26-3

## Generalization to Higher Dimensions

All three results—the [[Topology §24 Covering Spaces#^lem-24-12|nullhomotopy extension lemma]], the [[No-Retraction Theorem|no-retraction theorem]], and the [[Brouwer Fixed Point Theorem|Brouwer fixed point theorem]]—generalize to arbitrary dimension. The proofs of the first and third are identical to the $B^2$ case; the second requires tools beyond $\pi_1$.

> [!theorem] Lemma §26.8: Generalized Nullhomotopy Lemma (Munkres 55.3 for $S^n$)
> Let $h: S^n \to X$ be continuous. Then $h$ is nullhomotopic if and only if $h$ extends to a continuous map $k: B^{n+1} \to X$ (i.e., $k|_{S^n} = h$).

^lem-26-8

> [!remark]- Connections
> - The case $n = 1$, together with the $\pi_1$ criterion: [[Topology §24 Covering Spaces#^lem-24-12|Equivalent Conditions for Nullhomotopy]].

> [!proof]+ Proof
> **($\Leftarrow$): Extension $\Rightarrow$ nullhomotopic.** Given $k: B^{n+1} \to X$ with $k|_{S^n} = h$, the homotopy is:
>
> ![[m590-26-1.svg]]
> *The homotopy (blue) evaluates $k$ on the shrinking sphere of radius $1-t$: at $t = 0$ it is $h = k|_{S^n}$, at $t = 1$ it is the constant $k(0)$. It stays inside $B^{n+1}$, which is all we need from $k$.*
>
> Check: $\|(1-t)x\| = 1-t \leq 1$ so $(1-t)x \in B^{n+1}$; $H(x,0) = k(x) = h(x)$; $H(x,1) = k(0)$ is constant.
>
> **($\Rightarrow$): Nullhomotopic $\Rightarrow$ extension.** We apply the Universal Property of Quotient Maps ([[Universal Property of Quotient Maps|§12.3]]). The maps involved are:
>
> ![[m590-26-2.svg]]
> *The cone map $\pi(x,t) = (1-t)x$ is a quotient map that crushes only the top $S^n \times \{1\}$ to the center $0$. The nullhomotopy $H$ is constant ($= c$) exactly there, so it factors through $\pi$: the red dashed $k$ with $k \circ \pi = H$ is the extension, and its bottom edge gives $k|_{S^n} = h$.*
>
> where $H: S^n \times I \to X$ is the nullhomotopy ($H(x,0) = h(x)$, $H(x,1) = c$) and $\pi(x, t) = (1-t)x$ is the cone map.
>
> *Step 1: $\pi$ is a quotient map.*
> - *Continuous:* $(x, t) \mapsto (1-t)x$ is a product of continuous functions.
> - *Surjective:* Every $y \in B^{n+1} \setminus \{0\}$ equals $\pi(y/\|y\|,\; 1 - \|y\|)$, and $0 = \pi(x, 1)$ for any $x$.
> - *Closed:* $S^n \times I$ is compact and $B^{n+1}$ is Hausdorff, so $\pi$ is closed.
>
> Continuous + surjective + closed = quotient map ([[Topology §12 Quotient Topology#^prop-12-2|§12]]).
>
> *Step 2: $H$ is constant on fibers of $\pi$.* For $t < 1$, $\pi$ is injective ($\pi(x,t) = (1-t)x$ determines both $t$ and $x$ uniquely), so there is nothing to check. The only non-trivial fiber is $\pi^{-1}(0) = S^n \times \{1\}$, where $H(x, 1) = c$ for all $x$—same value. ✓
>
> *Step 3: Universal Property.* Since $\pi$ is a quotient map and $H$ is constant on fibers, the [[Universal Property of Quotient Maps|Universal Property]] gives a unique continuous $k: B^{n+1} \to X$ with $k \circ \pi = H$.
>
> *Step 4: $k|_{S^n} = h$.* For $x \in S^n$: $k(x) = k(\pi(x, 0)) = H(x, 0) = h(x)$. ✓

^pf-26-8

*Uses:* [[Universal Property of Quotient Maps|§12.3]], [[Topology §12 Quotient Topology#^prop-12-2|§12.2]], [[Closed Subspace of a Compact Space is Compact|§15.2]], [[Continuous Image of a Compact Space is Compact|§15.3]], [[Compact Subspace of a Hausdorff Space is Closed|§15.4]]

> [!theorem] Theorem §26.9: Generalized No-Retraction Theorem
> For each $n \geq 0$, there is no retraction $r: B^{n+1} \to S^n$.

^thm-26-9

> [!remark] Remark: Why Our Proof Does Not Generalize
> For $n = 1$, we proved this using $\pi_1$ ([[No-Retraction Theorem|§26.6]]): a retraction $r: B^2 \to S^1$ would force an injection $j_*: \pi_1(S^1) \hookrightarrow \pi_1(B^2)$, i.e., $\mathbb{Z} \hookrightarrow 0$, which is impossible.
>
> ![[m590-26-3.svg]]
> *Apply $\pi_1$ to $r \circ j = \operatorname{id}_{S^1}$ (blue): the identity of $\mathbb{Z}$ (red) would have to factor through $\pi_1(B^2) = 0$, which is impossible. For $n \ge 2$ the bottom row becomes $0 \to 0 \to 0$ and this contradiction disappears.*
>
> For $n \geq 2$, this argument fails: $\pi_1(S^n) = 0$ (spheres of dimension $\geq 2$ are simply connected, [[Sⁿ is Simply Connected for n ≥ 2|§27.3]]), so the injection $0 \hookrightarrow 0$ is no contradiction. The proof for general $n$ requires **homology theory** (specifically, $H_n(S^n) \cong \mathbb{Z}$ replaces $\pi_1(S^1) \cong \mathbb{Z}$), which is beyond this course.
>
> We therefore take the general no-retraction theorem as a given fact when working in dimension $n \geq 2$.

^rem-26-4

> [!theorem] Theorem §26.10: Generalized Brouwer Fixed Point Theorem
> For each $n \geq 0$, every continuous map $f: B^{n+1} \to B^{n+1}$ has a fixed point.

^thm-26-10

> [!proof]+ Proof
> The proof is identical to the $B^2$ case ([[Topology §26 Deformation Retracts and Homotopy Type#^pf-26-7|§26.7]])—the ray construction works in any dimension. The logical structure is:
>
> ![[m590-26-4.svg]]
> *The proof builds one thing, the red arrow: from a fixed-point-free $f$, the ray from $f(x)$ through $x$ produces a retraction $r: B^{n+1} \to S^n$, which the [[Topology §26 Deformation Retracts and Homotopy Type#^thm-26-9|no-retraction theorem]] forbids.*
>
> Suppose $f(x) \neq x$ for all $x \in B^{n+1}$. Since $f(x)$ and $x$ are distinct, the ray $\gamma(t) = f(x) + t(x - f(x))$ for $t \geq 0$ is well-defined. The ray crosses $S^n$ when $\|\gamma(t)\| = 1$ (distance from $\gamma(t)$ to the origin equals $1$). Expanding $\|\gamma(t)\|^2 = 1$ in coordinates gives a quadratic $at^2 + bt + c = 0$ with:
> - $a = \|x - f(x)\|^2 = \sum_{i=1}^{n+1} (x_i - f(x)_i)^2 > 0$ (since $f(x) \neq x$).
> - $c = \|f(x)\|^2 - 1 \leq 0$ (since $f(x) \in B^{n+1}$).
>
> The expansion involves $(n+1)$ squared terms instead of $2$, but collects identically into $at^2 + bt + c = 0$. By Vieta's formulas, the product of the roots is $c/a \leq 0$, so the larger root $t_0 = (-b + \sqrt{b^2 - 4ac})/2a$ is non-negative.
>
> Define $r(x) = \gamma(t_0)$. Then:
> - $r(x) \in S^n$: $\|\gamma(t_0)\| = 1$ by construction.
> - $r$ is continuous: $t_0$ depends continuously on $x$ via the quadratic formula.
> - $r$ is a retraction: for $x \in S^n$, $\|x\| = 1$ so $t = 1$ solves $\|\gamma(1)\| = \|x\| = 1$, giving $t_0 = 1$ and $r(x) = x$.
>
> Thus $r: B^{n+1} \to S^n$ is a retraction, contradicting the [[Topology §26 Deformation Retracts and Homotopy Type#^thm-26-9|no-retraction theorem]].

^pf-26-10

*Uses:* [[Brouwer Fixed Point Theorem|§26.7]], [[Topology §26 Deformation Retracts and Homotopy Type#^thm-26-9|§26.9]]

> [!remark] Remark: Summary: The Logical Dependencies
> The full chain for dimension $n$:
>
> ![[m590-26-5.svg]]
> *Blue arrows are proved in these notes; the dashed gray arrow (no retraction for general $n$, from $H_n(S^n) \cong \mathbb{Z}$) needs homology and is taken as given. Everything to the right of “no retraction” uses only the ray construction and composition, so it holds in every dimension once that one input is granted.*
>
> For $n = 1$, we proved everything from scratch. For $n \geq 2$, the [[Topology §26 Deformation Retracts and Homotopy Type#^thm-26-9|no-retraction theorem]] is taken as given (it requires homology), but everything downstream follows by the same arguments.

^rem-26-5

## Deformation Retracts

A [[Topology §26 Deformation Retracts and Homotopy Type#^prop-26-3|retraction]] gives $j_*$ injective and $r_*$ surjective, but not an isomorphism. The extra ingredient needed is a homotopy from $\operatorname{id}_X$ to $j \circ r$ — this upgrades the retraction to a deformation retraction and the injection to a full isomorphism.

> [!definition] Definition §26.3: Deformation Retract
> A subspace $A \subseteq X$ is a **deformation retract** of $X$ if $\operatorname{id}_X: X \to X$ is homotopic to a map that carries all of $X$ into $A$, such that each point of $A$ remains fixed during the homotopy.
>
> That is, there exists a continuous map $H: X \times I \to X$ (called a **deformation retraction**) such that:
> - $H(x, 0) = x$ for all $x \in X$ (starts as identity).
> - $H(x, 1) \in A$ for all $x \in X$ (ends in $A$).
> - $H(a, t) = a$ for all $a \in A$, $t \in I$ ($A$ stays fixed throughout).

^def-26-3

> [!remark] Remark
> The map $r(x) = H(x, 1)$ is a [[Topology §26 Deformation Retracts and Homotopy Type#^def-26-1|retraction]] of $X$ onto $A$ (check: $r(a) = H(a, 1) = a$ by condition 3). A deformation retract is thus a retract with the additional property that the retraction is homotopic to the identity—this “continuous collapsing over time” is what gives surjectivity of $j_*$.

^rem-26-6

> [!theorem] Theorem §26.11: Deformation Retract Induces Isomorphism on $\pi_1$
> Let $A$ be a deformation retract of $X$, and let $x_0 \in A$. Then the inclusion $j: (A, x_0) \hookrightarrow (X, x_0)$ induces an isomorphism on fundamental groups.

^thm-26-11

> [!remark]- Connections
> - Special case of [[Topology §26 Deformation Retracts and Homotopy Type#^thm-26-15|Homotopy Equivalence Induces Isomorphism on π₁]] (see [[Topology §26 Deformation Retracts and Homotopy Type#^rem-26-12|Deformation Retract as a Special Case]]).

> [!proof]+ Proof
> The argument is the [[Topology §26 Deformation Retracts and Homotopy Type#^thm-26-2|same]] as for $S^n \hookrightarrow \mathbb{R}^{n+1} \setminus \{0\}$.
>
> Let $r: X \to A$ be the retraction ($r(x) = H(x,1)$) and $j: A \hookrightarrow X$ the inclusion.
>
> **$j_*$ is injective:** $r \circ j = \operatorname{id}_A$, so $r_* \circ j_* = \operatorname{id}$ on $\pi_1(A, x_0)$.
>
> **$j_*$ is surjective:** $H$ is a homotopy from $\operatorname{id}_X$ to $j \circ r$ that fixes $x_0$ (since $x_0 \in A$ and $H(a, t) = a$ for all $a \in A$). By [[Topology §26 Deformation Retracts and Homotopy Type#^lem-26-1|the lemma]] (homotopic maps with fixed basepoint induce the same homomorphism), $(j \circ r)_* = (\operatorname{id}_X)_* = \operatorname{id}$ on $\pi_1(X, x_0)$. So $j_* \circ r_* = \operatorname{id}$, giving surjectivity of $j_*$.

^pf-26-11

*Uses:* [[Topology §26 Deformation Retracts and Homotopy Type#^thm-26-2|§26.2]], [[Topology §26 Deformation Retracts and Homotopy Type#^prop-26-3|§26.3]], [[Functoriality of π₁|§23.5]], [[Topology §26 Deformation Retracts and Homotopy Type#^lem-26-1|§26.1]]

> [!theorem] Corollary §26.12: Deformation Retracts Have the Same $\pi_1$
> If $A$ is a deformation retract of $X$, then $\pi_1(X, x_0) \cong \pi_1(A, x_0)$ for any $x_0 \in A$.
>
> In practice: to compute $\pi_1(X)$, find a deformation retract $A \subseteq X$ whose $\pi_1$ you already know.

^cor-26-12

*Uses:* [[Deformation Retract Induces Isomorphism on π₁|§26.11]]

> [!remark] Remark: Retraction vs. Deformation Retraction: Summary
> |  | **Retraction** | **Deformation retraction** |
> |---|---|---|
> | Definition | $r \circ j = \operatorname{id}_A$ | Same, plus $H$ from $\operatorname{id}_X$ to $j \circ r$ fixing $A$ |
> | $j_*$ | injective | isomorphism |
> | $r_*$ | surjective | isomorphism |
> | $\pi_1(X)$ vs $\pi_1(A)$ | $\pi_1(A)$ embeds, $\pi_1(X)$ can be bigger | $\pi_1(X) \cong \pi_1(A)$ |
>
> **Exam consequence:** To show $A$ is not a deformation retract of $X$, it suffices to show $\pi_1(X) \not\cong \pi_1(A)$ (easier). To show $A$ is not a retract, you need the stronger argument that $j_*$ injective with left inverse leads to a contradiction (harder, but catches cases where $\pi_1(X) \cong \pi_1(A)$).

^rem-26-7

## Examples

> [!example] Example §26.2: $\mathbb{R}^3 \setminus \{z\text{-axis}\}$ deformation retracts onto $\mathbb{R}^2 \setminus \{0\}$
> Let $X = \mathbb{R}^3 \setminus \{z\text{-axis}\}$. Note $\mathbb{R}^2 \setminus \{0\} \subseteq X$ (as the $z = 0$ plane minus the origin). Define
>
> $$
> H: X \times I \to X, \qquad H(x, y, z, t) = (x, y, z(1-t)).
> $$
>
> This collapses the $z$-coordinate to $0$ while preserving $(x, y) \neq (0,0)$. So $\mathbb{R}^2 \setminus \{0\}$ is a [[Topology §26 Deformation Retracts and Homotopy Type#^cor-26-12|deformation retract]] of $X$, and
>
> $$
> \pi_1(\mathbb{R}^3 \setminus \{z\text{-axis}\}) \cong \pi_1(\mathbb{R}^2 \setminus \{0\}) \cong \pi_1(S^1) \cong \mathbb{Z}.
> $$

^ex-26-2

![[m590-26-11.svg]]
*$H(x,y,z,t) = (x, y, (1-t)z)$ moves every point straight down (red) onto the blue plane $z = 0$; points below the plane rise the same way. Since $(x, y) \neq (0,0)$ never changes, no point ever touches the removed $z$-axis (red, dashed), and in particular none lands on the origin.*

> [!example] Example §26.3: $B^2$ deformation retracts onto a point
> $H: B^2 \times I \to B^2$ defined by $H(x, t) = (1-t)x$. So $\pi_1(B^2) = 0$ (trivial).

^ex-26-3

> [!example] Example §26.4: $\{x \in \mathbb{R}^2 : \|x\| > 1\}$ deformation retracts onto $S^1$
> The exterior of the unit disk deformation retracts onto the unit circle via
>
> $$
> H(x, t) = (1-t)x + t\frac{x}{\|x\|}.
> $$
>
> This is the [[Topology §26 Deformation Retracts and Homotopy Type#^pf-26-2|same formula]] as for $\mathbb{R}^2 \setminus \{0\}$ restricted to $\|x\| > 1$. So $\pi_1(\{x : \|x\| > 1\}) \cong \mathbb{Z}$.

^ex-26-4

> [!example] Example §26.5: Doubly punctured plane
> $\mathbb{R}^2 \setminus \{p, q\}$ (two points removed) deformation retracts onto a [[Topology §28 Fundamental Group of Some Surfaces#^def-28-4|figure-eight space]] (wedge of two circles). So $\pi_1(\mathbb{R}^2 \setminus \{p, q\}) \cong F_2$ (the [[Topology §21 Algebra Prerequisites꞉ Groups#^def-21-8|free group]] on two generators).

^ex-26-5

> [!example] Example §26.6: Doubly punctured plane
> The plane with two points removed deformation retracts onto both a figure-eight space and a “theta” space ($\Theta$). Similarly, neither the figure-eight nor the theta space is a deformation retract of the other, but they have isomorphic fundamental groups (both $\cong F_2$).
>
> This illustrates that **isomorphic $\pi_1$ does not imply deformation retract**—the relationship is one-directional.

^ex-26-6

![[m590-26-12.svg]]
*The doubly punctured plane deformation retracts onto the figure eight (left) and onto the theta space (right): points flow away from the punctures $p, q$ and in from far away onto the blue graph. So both graphs have $\pi_1 \cong F_2$ and the same homotopy type as $\mathbb{R}^2 \setminus \{p, q\}$, although neither graph is a deformation retract of the other.*

> [!example] Example §26.7: $S^n$ is a deformation retract of $\mathbb{R}^{n+1} \setminus \{0\}$
> Via $H(x,t) = (1-t)x + tx/\|x\|$ (proved in the [[Topology §26 Deformation Retracts and Homotopy Type#^thm-26-2|previous theorem]]). So $\pi_1(\mathbb{R}^{n+1} \setminus \{0\}) \cong \pi_1(S^n)$.
>
> For $n \geq 2$: $\pi_1(S^n) = 0$ ([[Sⁿ is Simply Connected for n ≥ 2|simply connected]]), so $\pi_1(\mathbb{R}^{n+1} \setminus \{0\}) = 0$.
>
> For $n = 1$: $\pi_1(S^1) \cong \mathbb{Z}$ ([[Fundamental Group of the Circle|§24.10]]), so $\pi_1(\mathbb{R}^2 \setminus \{0\}) \cong \mathbb{Z}$.

^ex-26-7

> [!example] Example §26.8: $\mathbb{R}^2 \setminus \{0\}$ is Not a Deformation Retract of $\mathbb{R}^2$
> If $\mathbb{R}^2 \setminus \{0\}$ were a deformation retract of $\mathbb{R}^2$, then by [[Topology §26 Deformation Retracts and Homotopy Type#^cor-26-12|the corollary]]:
>
> $$
> \pi_1(\mathbb{R}^2) \cong \pi_1(\mathbb{R}^2 \setminus \{0\}).
> $$
>
> But $\pi_1(\mathbb{R}^2) = 0$ ([[Topology §23 The Fundamental Group#^ex-23-2|convex]]) and $\pi_1(\mathbb{R}^2 \setminus \{0\}) \cong \mathbb{Z}$ ([[Topology §26 Deformation Retracts and Homotopy Type#^ex-26-7|deformation retracts]] onto $S^1$). Since $0 \not\cong \mathbb{Z}$, no such deformation retract exists.
>
> **General principle:** To show $A$ is *not* a deformation retract of $X$, show $\pi_1(X) \not\cong \pi_1(A)$. This is $\pi_1$ as an **obstruction**: it doesn't tell you when a deformation retract exists, but it tells you when one *cannot* exist.

^ex-26-8

> [!example] Example §26.9: $T^2 \setminus \{pt\}$ Deformation Retracts onto the Figure Eight
> The punctured torus has $\pi_1(T^2 \setminus \{pt\}) \cong F_2$ (the free group on two generators). The proof combines the quotient map construction ([[Topology §12 Quotient Topology|§12]]) with a deformation retract argument, using the [[Universal Property of Quotient Maps|universal property]] to pass from the square to the torus. We go through this step by step.
>
> **Step 1: Represent the torus as a quotient of the square.**
>
> The torus $T^2 = S^1 \times S^1$ is the [[Topology §12 Quotient Topology#^ex-12-3|quotient of the square]] $[0, 2\pi]^2$ by the equivalence relation that identifies opposite edges:
> - $(0, t) \sim (2\pi, t)$ for all $t$ (left edge $\sim$ right edge),
> - $(s, 0) \sim (s, 2\pi)$ for all $s$ (bottom edge $\sim$ top edge).
>
> The quotient map is $\pi: [0, 2\pi]^2 \to T^2$, defined by $\pi(s, t) = (e^{is}, e^{it})$. This map is:
> - *Continuous:* Composition of continuous functions.
> - *Surjective:* Every $(e^{is}, e^{it}) \in S^1 \times S^1$ is hit.
> - *Quotient map:* $[0, 2\pi]^2$ is compact, $T^2$ is Hausdorff, so $\pi$ is closed, hence a [[Topology §12 Quotient Topology#^prop-12-2|quotient map]].
>
> **Step 2: Identify what the boundary becomes.**
>
> Under $\pi$, the boundary $\partial[0, 2\pi]^2$ maps onto $(S^1 \times \{1\}) \cup (\{1\} \times S^1)$—the **[[Topology §28 Fundamental Group of Some Surfaces#^def-28-4|figure eight]]** in $T^2$. Concretely:
> - All four corners $(0,0), (2\pi, 0), (0, 2\pi), (2\pi, 2\pi)$ map to the single point $(1, 1) \in T^2$ (the basepoint).
> - The top and bottom edges ($t = 0$ and $t = 2\pi$) both map to $S^1 \times \{1\}$ (one circle of the figure eight).
> - The left and right edges ($s = 0$ and $s = 2\pi$) both map to $\{1\} \times S^1$ (the other circle).
>
> **Step 3: Choose the puncture point.**
>
> Let $q = (\pi, \pi)$ be the center of the square, and let $pt = \pi(q) \in T^2$. Since $q$ is in the interior of $[0, 2\pi]^2$, it is the *only* preimage of $pt$ under $\pi$ (the identifications only happen on the boundary). So:
> - $[0, 2\pi]^2 \setminus \{q\}$ is the punctured square (simple, convex minus a point).
> - $T^2 \setminus \{pt\}$ is the punctured torus (what we want to study).
> - $\pi$ restricts to a quotient map $\pi: [0, 2\pi]^2 \setminus \{q\} \to T^2 \setminus \{pt\}$.
>
> **Step 4: Deformation retract on the punctured square.**
>
> On the punctured square $[0, 2\pi]^2 \setminus \{q\}$, we deformation retract onto the boundary $\partial[0, 2\pi]^2$ by “pushing outward from $q$.” For each point $x \neq q$, draw the ray from $q$ through $x$; it hits the boundary at a unique point $r(x)$. Define:
>
> $$
> \tilde{F}: ([0, 2\pi]^2 \setminus \{q\}) \times I \to [0, 2\pi]^2 \setminus \{q\}, \qquad \tilde{F}(x, t) = (1-t)x + t \cdot r(x).
> $$
>
> This is a straight-line homotopy from $x$ toward $r(x)$. Check the deformation retract conditions:
> - $\tilde{F}(x, 0) = x$ for all $x$ (starts as identity). ✓
> - $\tilde{F}(x, 1) = r(x) \in \partial[0, 2\pi]^2$ for all $x$ (ends on boundary). ✓
> - If $x \in \partial[0, 2\pi]^2$: the ray from $q$ through $x$ hits the boundary at $x$ itself, so $r(x) = x$, and $\tilde{F}(x, t) = (1-t)x + tx = x$ for all $t$ (boundary stays fixed). ✓
> - $\tilde{F}(x, t) \neq q$ for all $t$: each $(1-t)x + tr(x)$ lies on the segment from $x$ to $r(x)$, which lies on the ray from $q$ through $x$, beyond $x$ (as seen from $q$), so it never contains $q$. ✓
>
> So $\tilde{F}$ is a deformation retraction of the punctured square onto its boundary.
>
> **Step 5: Descend to the torus via the universal property.**
>
> We want a deformation retraction $F: (T^2 \setminus \{pt\}) \times I \to T^2 \setminus \{pt\}$. We have $\tilde{F}$ on the square. Consider the diagram:
>
> ![[m590-26-6.svg]]
> *Upstairs, $\tilde F$ is an explicit straight-line push to the boundary; the vertical maps are the quotient maps. The red dashed $F$ is what the universal property delivers, and the only thing to check is that $\pi \circ \tilde F$ is constant on fibers, which holds because $\tilde F$ never moves the (glued) boundary points.*
>
> We want the dashed arrow $F$ to exist and be continuous. By the universal property ([[Universal Property of Quotient Maps|§12.3]]), the composite $\pi \circ \tilde{F}$ descends to a continuous map $F$ on $(T^2 \setminus \{pt\}) \times I$ if and only if $\pi \circ \tilde{F}$ is **constant on fibers** of $\pi \times \operatorname{id}$.
>
> **What does “constant on fibers” mean here?** Two points $(x_1, t)$ and $(x_2, t)$ are in the same fiber of $\pi \times \operatorname{id}$ when $\pi(x_1) = \pi(x_2)$ (and same $t$). This happens exactly when $x_1 \sim x_2$ under the edge identifications. We need:
>
> $$
> \text{if } x_1 \sim x_2, \quad \text{then } \pi(\tilde{F}(x_1, t)) = \pi(\tilde{F}(x_2, t)) \text{ for all } t.
> $$
>
> **Verification.** The identifications only happen on the boundary: $(0, s) \sim (2\pi, s)$ and $(s, 0) \sim (s, 2\pi)$. Since $\tilde{F}$ is **stationary on the boundary** ($\tilde{F}(x, t) = x$ for all $x \in \partial[0, 2\pi]^2$ and all $t$), identified points stay where they are throughout the homotopy:
>
> $$
> \tilde{F}((0, s), t) = (0, s) \quad \text{and} \quad \tilde{F}((2\pi, s), t) = (2\pi, s).
> $$
>
> Since $(0, s) \sim (2\pi, s)$ under $\pi$, we have $\pi(\tilde{F}((0,s), t)) = \pi(0, s) = \pi(2\pi, s) = \pi(\tilde{F}((2\pi, s), t))$. ✓
>
> Similarly for $(s, 0) \sim (s, 2\pi)$. ✓
>
> No other identifications exist (interior points have unique preimages), so there is nothing else to check.
>
> **Step 6: Conclusion.**
>
> By the universal property, $F$ exists and is continuous. Since $\tilde{F}$ is a deformation retraction of the punctured square onto $\partial[0, 2\pi]^2$, $F$ is a deformation retraction of $T^2 \setminus \{pt\}$ onto $\pi(\partial[0, 2\pi]^2)$ = the figure eight. Therefore:
>
> $$
> \pi_1(T^2 \setminus \{pt\}) \cong \pi_1(\text{figure eight}) \cong F_2.
> $$
>
> **Summary of the method:**
> 1. Work on the *square* (simple geometry: rays, straight lines).
> 2. Build a deformation retraction $\tilde{F}$ on the square.
> 3. Check that $\tilde{F}$ *respects the gluing*: identified boundary points stay identified throughout the homotopy (because $\tilde{F}$ is stationary on the boundary).
> 4. The universal property of quotient maps automatically gives a continuous deformation retraction $F$ on the torus.
>
> This is the general strategy whenever you want to build continuous maps on quotient spaces: work upstairs where geometry is simple, verify the gluing is respected, then descend.

^ex-26-9

![[m590-26-13.svg]]
*Step 4 on the square $[0, 2\pi]^2$: the red rays push every point away from the puncture $q = (\pi, \pi)$ onto the boundary, which stays fixed. After gluing (the two $a$ edges together, the two $b$ edges together, all four corners to one point) the boundary is the figure eight $a \vee b$. The orange loop $t$ around $q$ expands to the boundary word $aba^{-1}b^{-1}$ ([[Topology §26 Deformation Retracts and Homotopy Type#^rem-26-8|the ungluing argument]]).*

> [!remark]- Connections
> - $\pi_1$ of the figure eight: [[Topology §29 The Seifert–van Kampen Theorem#^ex-29-2|π₁(S¹ ∨ S¹) ≅ ℤ ∗ ℤ]]. Used in [[Topology §29 The Seifert–van Kampen Theorem#^ex-29-4|π₁(T²) ≅ ℤ × ℤ via van Kampen]].
> - The square-to-torus quotient map: [[Topology §12 Quotient Topology#^ex-12-6|The Square-to-Torus Quotient Map]].

> [!remark] Remark: The Ungluing Argument
> The punctured torus result is used in the van Kampen computation of $\pi_1(T^2)$ ([[Topology §29 The Seifert–van Kampen Theorem#^ex-29-4|§29]]), where the key step is showing that a small loop $t$ around the puncture satisfies $i_1(t) = aba^{-1}b^{-1}$ in $\pi_1(T^2 \setminus \{pt\}) \cong F_2$. Here is the geometric argument:
>
> **1. $t$ survives ungluing.** The loop $t$ is a small circle around $q = (\pi, \pi)$, the center of the fundamental square. Since $t$ lives entirely in the *interior* of $[0, 2\pi]^2$ — it doesn't touch any edge — it is unaffected by the edge identifications. When we “unglue” (go from the torus back to the square), $t$ remains a loop.
>
> **2. Expand $t$ to the boundary.** In the punctured square, the deformation retract ([[Topology §26 Deformation Retracts and Homotopy Type#^ex-26-9|Step 4 above]]) pushes $t$ radially outward from $q$, expanding it until it reaches the boundary $\partial[0, 2\pi]^2$.
>
> **3. Read off the boundary word.** Going counterclockwise around $\partial[0, 2\pi]^2$ from the bottom-left corner: bottom edge = $a$, right edge = $b$, top edge = $a^{-1}$ (same label, reversed direction), left edge = $b^{-1}$. So $t \simeq aba^{-1}b^{-1}$.
>
> **Why other loops can't be treated this way:** The loop $a$ (going around the “hole” of the torus) *crosses* an identified edge — it enters through the left side and exits through the right side. When you unglue, it breaks into a path from the left edge to the right edge, not a loop. You cannot make $a$ small enough to avoid the edges, because crossing the edge *is* what the loop does. So $a$ and $b$ are generators of the figure eight, not expressible as boundary words.
>
> **Connection to van Kampen:** Removing $q$ “frees” $aba^{-1}b^{-1}$ from being trivial: in $T^2$ it contracts to $q$, but in $T^2 \setminus \{q\}$ the contraction is blocked. Gluing the disk back (the van Kampen computation, [[Topology §29 The Seifert–van Kampen Theorem#^ex-29-4|§29]]) forces $aba^{-1}b^{-1} = e$, which is exactly $ab = ba$, recovering $\pi_1(T^2) \cong \mathbb{Z} \times \mathbb{Z}$ ([[Topology §23 The Fundamental Group#^cor-23-8|§23.8]]).

^rem-26-8

## Homotopy Equivalence

Deformation retracts give isomorphisms on $\pi_1$, but they require $A \subseteq X$ and that $A$ stays fixed throughout the homotopy. The notion of *homotopy equivalence* is far more general: it relates spaces that need not be subspaces of each other.

> [!definition] Definition §26.4: Homotopy Equivalence
> Let $f: X \to Y$ and $g: Y \to X$ be continuous maps. If
>
> $$
> f \circ g \simeq \operatorname{id}_Y \qquad \text{and} \qquad g \circ f \simeq \operatorname{id}_X,
> $$
>
> then $f$ and $g$ are called **homotopy equivalences**, and $g$ is a **homotopy inverse** of $f$ (and vice versa).

^def-26-4

> [!remark] Remark: Homotopy Equivalence vs Homeomorphism
> The definition is structurally identical to [[Topology §9 Continuous Functions#^def-9-2|homeomorphism]], with equality relaxed to homotopy:
>
> |  | **Homeomorphism** | **Homotopy Equivalence** |
> |---|---|---|
> | Condition | $f \circ g = \operatorname{id}_Y$ and $g \circ f = \operatorname{id}_X$ | $f \circ g \simeq \operatorname{id}_Y$ and $g \circ f \simeq \operatorname{id}_X$ |
> | Meaning | Points go back to exactly where they started | The composition can be continuously deformed into the identity |
> | Preserves | All topological properties (compactness, dimension, $\pi_1$, …) | $\pi_1$ and all homotopy invariants, but NOT compactness, dimension, … |
>
> Since $=$ is a special case of $\simeq$ (use the constant homotopy $H(x,t) = x$):
>
> $$
> \text{Homeomorphic} \implies \text{Homotopy equivalent} \implies \text{Isomorphic } \pi_1.
> $$
>
> Neither arrow reverses:
> - $S^1$ and $\mathbb{R}^2 \setminus \{0\}$: homotopy equivalent ([[Topology §26 Deformation Retracts and Homotopy Type#^ex-26-7|deformation retract]]) but NOT homeomorphic (compact vs. non-compact).
> - $S^2$ and $\{pt\}$: both have $\pi_1 = 0$, but NOT homotopy equivalent ($S^2$ is not [[Topology §26 Deformation Retracts and Homotopy Type#^def-26-6|contractible]]).

^rem-26-9

> [!remark] Remark: Composition of Homotopy Equivalences
> If $f: X \to Y$ and $h: Y \to Z$ are homotopy equivalences, then $h \circ f: X \to Z$ is a homotopy equivalence.
>
> *Proof.* Let $g$ be a homotopy inverse of $f$ (so $f \circ g \simeq \operatorname{id}_Y$ and $g \circ f \simeq \operatorname{id}_X$) and $k$ a homotopy inverse of $h$ (so $h \circ k \simeq \operatorname{id}_Z$ and $k \circ h \simeq \operatorname{id}_Y$). We claim $g \circ k$ is a homotopy inverse of $h \circ f$.
>
> **Check 1:** $(g \circ k) \circ (h \circ f) \simeq \operatorname{id}_X$?
>
> $$
> \begin{aligned}
> (g \circ k) \circ (h \circ f) &= g \circ (k \circ h) \circ f &\text{(associativity of composition)}\\
> &\simeq g \circ \operatorname{id}_Y \circ f &\text{(since } k \circ h \simeq \operatorname{id}_Y\text{)}\\
> &= g \circ f &\\
> &\simeq \operatorname{id}_X. &\text{(since } g \circ f \simeq \operatorname{id}_X\text{)}
> \end{aligned}
> $$
>
> (Here we use: if $\alpha \simeq \beta$, then $g \circ \alpha \circ f \simeq g \circ \beta \circ f$—homotopy is preserved by pre- and post-composition with continuous maps.)
>
> **Check 2:** $(h \circ f) \circ (g \circ k) \simeq \operatorname{id}_Z$? Same idea: $h \circ (f \circ g) \circ k \simeq h \circ \operatorname{id}_Y \circ k = h \circ k \simeq \operatorname{id}_Z$.

^rem-26-10

> [!theorem] Theorem §26.13: Homotopy Equivalence is an Equivalence Relation
> The relation “$X \simeq Y$” (there exists a homotopy equivalence $f: X \to Y$) is an equivalence relation on topological spaces.

^thm-26-13

> [!proof]+ Proof
> **Reflexive ($X \simeq X$):** Take $f = \operatorname{id}_X: X \to X$. Its homotopy inverse is also $\operatorname{id}_X$: $\operatorname{id}_X \circ \operatorname{id}_X = \operatorname{id}_X \simeq \operatorname{id}_X$ in both directions.
>
> **Symmetric ($X \simeq Y \Rightarrow Y \simeq X$):** Suppose $f: X \to Y$ is a homotopy equivalence with homotopy inverse $g: Y \to X$. The [[Topology §26 Deformation Retracts and Homotopy Type#^def-26-4|definition]] is symmetric in $f$ and $g$: the conditions $f \circ g \simeq \operatorname{id}_Y$ and $g \circ f \simeq \operatorname{id}_X$ say exactly that $g$ is a homotopy equivalence with homotopy inverse $f$.
>
> **Transitive ($X \simeq Y$ and $Y \simeq Z \Rightarrow X \simeq Z$):** Suppose $f: X \to Y$ and $h: Y \to Z$ are homotopy equivalences. By [[Topology §26 Deformation Retracts and Homotopy Type#^rem-26-10|the remark above]], $h \circ f: X \to Z$ is a homotopy equivalence.

^pf-26-13

*Uses:* [[Topology §26 Deformation Retracts and Homotopy Type#^def-26-4|Def. §26.4]]

> [!definition] Definition §26.5: Homotopy Type
> Two topological spaces that are homotopy equivalent are said to have the same **homotopy type**.

^def-26-5

> [!example] Example §26.10: Deformation Retracts Give Homotopy Equivalences
> If $A$ is a [[Topology §26 Deformation Retracts and Homotopy Type#^def-26-3|deformation retract]] of $X$, then the retraction $r: X \to A$ and the inclusion $j: A \hookrightarrow X$ are homotopy inverses: $r \circ j = \operatorname{id}_A$ (exactly, not just up to homotopy) and $j \circ r \simeq \operatorname{id}_X$ (via the deformation retraction). In particular, $A$ and $X$ have the same homotopy type.

^ex-26-10

> [!example] Example §26.11: Figure-Eight and Theta Space
> The [[Topology §28 Fundamental Group of Some Surfaces#^def-28-4|figure-eight space]] $S^1 \vee S^1$ and the theta space $\Theta$ (two arcs joining two points) have the same homotopy type, even though neither is a deformation retract of the other. Both have $\pi_1 \cong F_2$.

^ex-26-11

## The General Basepoint-Change Lemma

The [[Topology §26 Deformation Retracts and Homotopy Type#^lem-26-1|lemma in §26.1]] assumed the basepoint stays fixed during the homotopy ($H(x_0, t) = y_0$ for all $t$). In practice, homotopy equivalences move the basepoint. The following generalization handles this by introducing a [[Basepoint Independence of π₁|basepoint-change]] path.

> [!theorem] Lemma §26.14: Homotopic Maps and $\pi_1$: General Case
> Let $h, k: X \to Y$ be continuous, and let $H: X \times I \to Y$ be a homotopy from $h$ to $k$. Let $x_0 \in X$, and define the path $\alpha: I \to Y$ by
>
> $$
> \alpha(t) = H(x_0, t).
> $$
>
> Then $\alpha$ is a path from $h(x_0)$ to $k(x_0)$, and
>
> $$
> k_* = \hat{\alpha} \circ h_*,
> $$
>
> where $\hat{\alpha}: \pi_1(Y, h(x_0)) \to \pi_1(Y, k(x_0))$ is the [[Basepoint Independence of π₁|basepoint-change isomorphism]] $\hat{\alpha}([f]) = [\bar{\alpha}] * [f] * [\alpha]$.
>
> In diagram form:
>
> ![[m590-26-7.svg]]
> *The lemma asserts the red arrow: $k_*$ is $h_*$ followed by the basepoint-change isomorphism $\hat\alpha$ along the track $\alpha(t) = H(x_0, t)$ of the basepoint. If the basepoint does not move, $\hat\alpha = \operatorname{id}$ and the triangle collapses to $k_* = h_*$.*

^lem-26-14

> [!proof]+ Proof
> This generalizes the [[Topology §26 Deformation Retracts and Homotopy Type#^lem-26-1|fixed-basepoint lemma]]. Let $[f] \in \pi_1(X, x_0)$, so $f: I \to X$ is a loop at $x_0$.
>
> Consider the composition $H \circ (f \times \operatorname{id}): I \times I \to Y$, where $(f \times \operatorname{id})(s, t) = (f(s), t)$. This map sends:
> - Bottom edge ($t = 0$): $(s, 0) \mapsto H(f(s), 0) = h(f(s))$, i.e., the loop $h \circ f$.
> - Top edge ($t = 1$): $(s, 1) \mapsto H(f(s), 1) = k(f(s))$, i.e., the loop $k \circ f$.
> - Left edge ($s = 0$): $(0, t) \mapsto H(f(0), t) = H(x_0, t) = \alpha(t)$.
> - Right edge ($s = 1$): $(1, t) \mapsto H(f(1), t) = H(x_0, t) = \alpha(t)$.
>
> The bottom is the loop $h \circ f$ at $h(x_0)$; the top is the loop $k \circ f$ at $k(x_0)$; both side edges trace the path $\alpha$. By an analysis of this square (see Munkres for details), the paths
>
> $$
> \alpha * (k \circ f) \qquad \text{and} \qquad (h \circ f) * \alpha
> $$
>
> are path homotopic. Therefore:
>
> $$
> [\alpha] * [k \circ f] = [h \circ f] * [\alpha],
> $$
>
> which gives $[k \circ f] = [\bar{\alpha}] * [h \circ f] * [\alpha] = \hat{\alpha}([h \circ f])$, i.e., $k_*([f]) = \hat{\alpha}(h_*([f]))$.

^pf-26-14

*Uses:* [[Basepoint Independence of π₁|§23.2]], [[Topology §26 Deformation Retracts and Homotopy Type#^lem-26-1|§26.1]]

![[m590-26-14.svg]]
*The square $I \times I$, each corner labeled by its image under $H \circ (f \times \operatorname{id})$: bottom $h \circ f$, top $k \circ f$, both sides $\alpha$. The blue path (bottom, then right side) and the red path (left side, then top) have the same endpoints in the convex square, so they are path homotopic there (gray). Composing with $H \circ (f \times \operatorname{id})$ gives $(h \circ f) * \alpha \simeq_p \alpha * (k \circ f)$.*

> [!remark] Remark
> When $H(x_0, t) = y_0$ for all $t$ (the basepoint stays fixed), the path $\alpha$ is constant, so $\hat{\alpha} = \operatorname{id}$ and we recover [[Topology §26 Deformation Retracts and Homotopy Type#^lem-26-1|the earlier lemma]]: $k_* = h_*$.

^rem-26-11

## Homotopy Equivalences Induce Isomorphisms on $\pi_1$

> [!theorem] Theorem §26.15: Homotopy Equivalence Induces Isomorphism on $\pi_1$
> If $f: X \to Y$ is a homotopy equivalence, then for every $x_0 \in X$,
>
> $$
> f_*: \pi_1(X, x_0) \to \pi_1(Y, f(x_0))
> $$
>
> is an isomorphism.

^thm-26-15

> [!proof]+ Proof
> Let $g: Y \to X$ be a homotopy inverse of $f$, so $f \circ g \simeq \operatorname{id}_Y$ and $g \circ f \simeq \operatorname{id}_X$.
>
> Consider the chain $X \xrightarrow{f} Y \xrightarrow{g} X \xrightarrow{f} Y$.
>
> **$f_*$ is surjective:** Since $f \circ g \simeq \operatorname{id}_Y$, the [[Topology §26 Deformation Retracts and Homotopy Type#^lem-26-14|general lemma]] gives
>
> $$
> (\operatorname{id}_Y)_* = \hat{\alpha} \circ (f \circ g)_* = \hat{\alpha} \circ f_* \circ g_*
> $$
>
> for some path $\alpha$. Since $(\operatorname{id}_Y)_* = \operatorname{id}$ and $\hat{\alpha}$ is an [[Basepoint Independence of π₁|isomorphism]], $f_* \circ g_*$ is an isomorphism. In particular, $f_*$ is surjective (it has a right inverse up to isomorphism).
>
> **$f_*$ is injective:** Since $g \circ f \simeq \operatorname{id}_X$, the [[Topology §26 Deformation Retracts and Homotopy Type#^lem-26-14|general lemma]] gives
>
> $$
> (\operatorname{id}_X)_* = \hat{\beta} \circ (g \circ f)_* = \hat{\beta} \circ g_* \circ f_*
> $$
>
> for some path $\beta$. So $g_* \circ f_*$ is an isomorphism, hence $f_*$ is injective (it has a left inverse up to isomorphism).

^pf-26-15

*Uses:* [[Topology §26 Deformation Retracts and Homotopy Type#^lem-26-14|§26.14]], [[Basepoint Independence of π₁|§23.2]], [[Functoriality of π₁|§23.5]]

> [!remark] Remark: Deformation Retract as a Special Case
> For a deformation retract $A \subseteq X$, the inclusion $j: A \hookrightarrow X$ is a [[Topology §26 Deformation Retracts and Homotopy Type#^ex-26-10|homotopy equivalence]] (with homotopy inverse $r$). The theorem recovers [[Deformation Retract Induces Isomorphism on π₁|our earlier result]] that $j_*$ is an isomorphism—but now we see it as a special case of a much more general principle.

^rem-26-12

## Contractible Spaces

> [!definition] Definition §26.6: Contractible Space
> A space $X$ is **contractible** if $\operatorname{id}_X: X \to X$ is [[Topology §22 Homotopy of Paths#^def-22-2|nullhomotopic]], i.e., homotopic to a constant map.

^def-26-6

> [!theorem] Theorem §26.16: $X$ Contractible $\iff$ Homotopy Type of a Point
> A space $X$ is contractible if and only if $X$ has the homotopy type of a one-point space.

^thm-26-16

> [!proof]+ Proof
> ($\Rightarrow$) Suppose $X$ is contractible, so $\operatorname{id}_X \simeq c$ where $c: X \to X$ is the constant map $c(x) = x_0$ for some $x_0 \in X$. Let $\{p\}$ be a one-point space. Define $f: X \to \{p\}$ (the unique map) and $g: \{p\} \to X$ by $g(p) = x_0$. Then:
> - $f \circ g = \operatorname{id}_{\{p\}}$ (exactly).
> - $g \circ f: X \to X$ sends every point to $x_0$, i.e., $g \circ f = c \simeq \operatorname{id}_X$.
>
> So $f$ and $g$ are homotopy inverses.
>
> ($\Leftarrow$) Suppose $f: X \to \{p\}$ and $g: \{p\} \to X$ are homotopy inverses. Then $g \circ f: X \to X$ is a constant map (it sends everything to $g(p)$), and $g \circ f \simeq \operatorname{id}_X$. So $\operatorname{id}_X$ is nullhomotopic.

^pf-26-16

*Uses:* [[Topology §26 Deformation Retracts and Homotopy Type#^def-26-4|Def. §26.4]], [[Topology §26 Deformation Retracts and Homotopy Type#^def-26-6|Def. §26.6]]

> [!remark] Remark
> Since a one-point space has trivial fundamental group, any contractible space satisfies $\pi_1(X, x_0) = 0$. Examples: $\mathbb{R}^n$, $B^n$, and any convex subset of $\mathbb{R}^n$ are contractible (via [[Topology §22 Homotopy of Paths#^thm-22-1|straight-line homotopies]]).

^rem-26-13

> [!theorem] Proposition §26.17: Retract of a Contractible Space is Contractible
> If $X$ is contractible and $A$ is a retract of $X$, then $A$ is contractible.

^prop-26-17

> [!proof]+ Proof
> Let $r: X \to A$ be a [[Topology §26 Deformation Retracts and Homotopy Type#^def-26-1|retraction]] ($r|_A = \operatorname{id}_A$). Since $X$ is contractible, $\operatorname{id}_X$ is nullhomotopic: there exists $F: X \times I \to X$ with $F(x, 0) = x$ and $F(x, 1) = x_0$ for some point $x_0$.
>
> Define $F': A \times I \to A$ by $F' = r \circ F|_{A \times I}$. Check:
> - $F'(a, 0) = r(F(a, 0)) = r(a) = a$ (since $a \in A$ and $r|_A = \operatorname{id}_A$).
> - $F'(a, 1) = r(F(a, 1)) = r(x_0)$ (a fixed point in $A$).
> - $F'$ is continuous (composition of continuous maps).
>
> So $F'$ is a homotopy from $\operatorname{id}_A$ to the constant map $a \mapsto r(x_0)$. Thus $A$ is contractible.

^pf-26-17

*Uses:* [[Topology §26 Deformation Retracts and Homotopy Type#^def-26-1|Def. §26.1]], [[Topology §26 Deformation Retracts and Homotopy Type#^def-26-6|Def. §26.6]]
