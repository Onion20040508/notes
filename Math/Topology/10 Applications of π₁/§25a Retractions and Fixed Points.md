---
type: section
subject: "[[Topology]]"
chapter: 10
section: "25a"
munkres: "§55, §58"
tags: [topology, math590]
---
← [[§25 The Fundamental Theorem of Algebra]] · ↑ [[· 10 Applications of π₁]] · [[§26 Deformation Retracts and Homotopy Type]] →

*First applications of $\pi_1$ to maps: homotopic maps (with the basepoint fixed) induce the same homomorphism, a [[§25a Retractions and Fixed Points#^def-26-1|retraction]] gives $j_{\ast}$ injective and $r_{\ast}$ surjective, and this proves the [[No-Retraction Theorem|no-retraction theorem]] and the [[Brouwer Fixed Point Theorem|Brouwer fixed point theorem]]. The stronger notion of a deformation retract continues in [[§26 Deformation Retracts and Homotopy Type]].*

## Homotopic Maps Induce the Same Homomorphism

> [!theorem] Lemma §26.1: Homotopic Maps and Induced Homomorphisms
> Let $h, k: (X, x_0) \to (Y, y_0)$ be continuous. If $h$ and $k$ are [[§22 Homotopy of Paths#^def-22-1|homotopic]], and the image of $x_0$ remains fixed at $y_0$ during the homotopy, then $h_* = k_*$ as homomorphisms $\pi_1(X, x_0) \to \pi_1(Y, y_0)$.

^lem-26-1

> [!remark]- Connections
> - Generalized to a moving basepoint: [[§26 Deformation Retracts and Homotopy Type#^lem-26-14|Homotopic Maps and π₁: General Case]].

> [!proof]+ Proof
> Let $H: X \times I \to Y$ be the homotopy with $H(x, 0) = h(x)$, $H(x, 1) = k(x)$, and $H(x_0, t) = y_0$ for all $t$.
>
> Let $[f] \in \pi_1(X, x_0)$, where $f: I \to X$ is a loop at $x_0$. Consider the composition:
>
> $$
> I \times I \xrightarrow{f \times \operatorname{id}} X \times I \xrightarrow{H} Y.
> $$
>
> This map sends $(s, t) \mapsto H(f(s), t)$, and is a [[§22 Homotopy of Paths#^def-22-4|path homotopy]] between $h \circ f$ and $k \circ f$:
> - $(s, 0) \mapsto H(f(s), 0) = h(f(s))$, i.e., the path $h \circ f$.
> - $(s, 1) \mapsto H(f(s), 1) = k(f(s))$, i.e., the path $k \circ f$.
> - $(0, t) \mapsto H(f(0), t) = H(x_0, t) = y_0$. Endpoints fixed.
> - $(1, t) \mapsto H(f(1), t) = H(x_0, t) = y_0$. Endpoints fixed.
>
> So $h \circ f \simeq_p k \circ f$, giving $[h \circ f] = [k \circ f]$, i.e., $h_*([f]) = k_*([f])$.

^pf-26-1

*Uses:* [[§22 Homotopy of Paths#^def-22-4|Def. §22.4]], [[§23 The Fundamental Group#^def-23-4|Def. §23.4]]

## Application: $S^n \hookrightarrow \mathbb{R}^{n+1} \setminus \{0\}$ Induces an Isomorphism

> [!theorem] Theorem §26.2: $\pi_1(S^n) \cong \pi_1(\mathbb{R}^{n+1} \setminus \{0\})$
> The inclusion $j: S^n \hookrightarrow \mathbb{R}^{n+1} \setminus \{0\}$ induces an isomorphism on fundamental groups.

^thm-26-2

> [!proof]+ Proof
> Let $X = \mathbb{R}^{n+1} \setminus \{0\}$ and $b_0 = (1, 0, \ldots, 0)$. Define $r: X \to S^n$ by $r(x) = x / \|x\|$.
>
> **$j_{\ast}$ is injective:** $r \circ j: S^n \to S^n$ is the identity map, so $(r \circ j)_{\ast} = r_{\ast} \circ j_{\ast} = \operatorname{id}$ on $\pi_1(S^n, b_0)$. If $j_{\ast}([f]) = [e]$, then $[f] = r_{\ast}(j_{\ast}([f])) = r_{\ast}([e]) = [e]$. So $j_{\ast}$ is injective.
>
> **$j_{\ast}$ is surjective:** We show $j \circ r: X \to X$ is homotopic to $\operatorname{id}_X$ with $b_0$ fixed. Define:
>
> $$
> H: X \times I \to X, \qquad H(x, t) = (1-t)x + t\frac{x}{\|x\|}.
> $$
>
> This is continuous and well-defined: for each $t$, $H(x, t)$ is a convex combination of $x$ and $x/\|x\|$, both nonzero, so $H(x, t) \neq 0$ (since $x$ and $x/\|x\|$ point in the same direction).
>
> Check: $H(x, 0) = x = \operatorname{id}_X(x)$ and $H(x, 1) = x/\|x\| = (j \circ r)(x)$. Also $H(b_0, t) = (1-t)b_0 + tb_0 = b_0$.
>
> By [[§25a Retractions and Fixed Points#^lem-26-1|the lemma]], $(j \circ r)_* = j_* \circ r_* = \operatorname{id}$ on $\pi_1(X, b_0)$. So for any $[g] \in \pi_1(X, b_0)$: $[g] = j_*(r_*([g]))$, showing $j_*$ is surjective.

^pf-26-2

*Uses:* [[Functoriality of π₁|§23.5]], [[§25a Retractions and Fixed Points#^lem-26-1|§26.1]]

![[m590-26-8.svg]]
*The homotopy $H(x,t) = (1-t)x + t\,x/\|x\|$ slides every point along its own ray (red) to the blue unit sphere, from outside and from inside alike. Nothing ever reaches the removed origin, and points of $S^n$ never move, so $S^n$ is a [[§26 Deformation Retracts and Homotopy Type#^ex-26-7|deformation retract]] of $\mathbb{R}^{n+1} \setminus \{0\}$ (drawn for $n = 1$). Keeping only the outer arrows gives [[§26 Deformation Retracts and Homotopy Type#^ex-26-4|Example §26.4]].*

## Retractions

> [!definition] Definition §26.1: Retraction
> Let $A \subseteq X$. A continuous map $r: X \to A$ is a **retraction** of $X$ onto $A$ if $r(a) = a$ for all $a \in A$, i.e., $r \circ j = \operatorname{id}_A$ where $j: A \hookrightarrow X$ is the inclusion.
>
> If such an $r$ exists, $A$ is called a **retract** of $X$.

^def-26-1

> [!remark]- Connections
> - The group-theoretic preview in §21: [[§21 Algebra Prerequisites꞉ Groups#^rem-21-8|Why This Matters for π₁: Two Directions from a Retraction]].

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
> **(1)** If $j_{\ast}([f]) = j_{\ast}([g])$, apply $r_{\ast}$ to both sides: $[f] = (r_{\ast} \circ j_{\ast})([f]) = (r_{\ast} \circ j_{\ast})([g]) = [g]$.
>
> **(2)** For any $[\gamma] \in \pi_1(A)$, the element $j_{\ast}([\gamma]) \in \pi_1(X)$ maps to it: $r_{\ast}(j_{\ast}([\gamma])) = [\gamma]$.

^pf-26-3

*Uses:* [[Functoriality of π₁|§23.5]]

> [!remark] Remark
> But that is *all* you get. $\pi_1(A)$ injects into $\pi_1(X)$, and $r_{\ast}$ surjects onto $\pi_1(A)$, but $\pi_1(X)$ can be strictly larger than $\pi_1(A)$.
>
> **Example:** $X = S^1 \vee S^1$, $A$ = one of the two circles. The map $r$ that collapses the other circle to the [[§28 Fundamental Group of Some Surfaces#^def-28-3|wedge point]] is a retraction. Here $\pi_1(A) \cong \mathbb{Z}$ and $\pi_1(X) \cong F_2$. The inclusion $j_{\ast}$ embeds $\mathbb{Z}$ as one free factor of $F_2$, and $r_{\ast}$ projects $F_2$ onto that factor. But $F_2 \not\cong \mathbb{Z}$ — the retraction does not force the fundamental groups to be isomorphic.
>
> **For a full isomorphism $\pi_1(X) \cong \pi_1(A)$, we need the stronger notion of a deformation retract** (see [[§26 Deformation Retracts and Homotopy Type#^def-26-3|below]]).

^rem-26-1

> [!theorem] Corollary §26.4: What Properties Transfer via Retraction
> Let $A$ be a retract of $X$. Then $\pi_1(A)$ is simultaneously a subgroup of $\pi_1(X)$ (via $j_*$) and a quotient of $\pi_1(X)$ (via $r_*$).
>
> **Up** (from $A$ to $X$, via $j_{\ast}$ injective): $\pi_1(X)$ contains an isomorphic copy of $\pi_1(A)$ ([[§21 Algebra Prerequisites꞉ Groups#^prop-21-9|§21.9]]), so any property that a group has as soon as one of its subgroups has it transfers upward. If $\pi_1(A)$ is non-abelian, nontrivial, infinite, or has torsion, so does $\pi_1(X)$.
>
> **Down** (from $X$ to $A$, via $r_{\ast}$ surjective): any property [[§21 Algebra Prerequisites꞉ Groups#^prop-21-10|inherited by quotients]] transfers downward. If $\pi_1(X)$ is abelian or finitely generated, so is $\pi_1(A)$.

^cor-26-4

*Uses:* [[§25a Retractions and Fixed Points#^prop-26-3|§26.3]], [[§21 Algebra Prerequisites꞉ Groups#^prop-21-9|§21.9]], [[§21 Algebra Prerequisites꞉ Groups#^prop-21-10|§21.10]]

> [!example] Example §26.1: $\pi_1(\Sigma_2)$ is Non-Abelian
> The [[§28 Fundamental Group of Some Surfaces#^def-28-4|figure eight]] $S^1 \vee S^1$ retracts from $\Sigma_2$, so $F_2 = \pi_1(S^1 \vee S^1)$ embeds in $\pi_1(\Sigma_2)$. Since $F_2$ is non-abelian, $\pi_1(\Sigma_2)$ is non-abelian. The retraction does not tell us *what* $\pi_1(\Sigma_2)$ is — only that it contains $F_2$ as a subgroup.

^ex-26-1

> [!remark]- Connections
> - The full argument, with the retraction constructed: [[§28 Fundamental Group of Some Surfaces#^thm-28-5|π₁(Σ₂) is Non-Abelian]].
> - $\pi_1(S^1 \vee S^1) \cong F_2$: [[§29 The Seifert–van Kampen Theorem#^ex-29-2|The Figure Eight via van Kampen]].

*Chain (genus 2 surface): later in [[§29a The Projective Plane, the Figure Eight, the Double Torus and the Torus|Chapter 11]] · [[Double torus|all appearances]]*

> [!definition] Definition §26.2: Closed Balls $B^n$
> The **closed unit ball** in $\mathbb{R}^n$ is $B^n = \{x \in \mathbb{R}^n : \|x\| \leq 1\}$.

^def-26-2

> [!definition] Definition §26.2: Spheres $S^{n-1}$
> Let $B^n$ be the [[§25a Retractions and Fixed Points#^def-26-2|closed unit ball]] in $\mathbb{R}^n$. Its boundary is the **unit sphere** $S^{n-1} = \{x \in \mathbb{R}^n : \|x\| = 1\}$.
>
> In particular: $B^2 = \{(x,y) \in \mathbb{R}^2 : x^2 + y^2 \leq 1\}$ is the closed unit disk, with boundary $S^1$.

^def-26-new1

> [!theorem] Proposition §26.5: $B^n$ is Convex and Simply Connected
> $B^n$ is convex: if $x, y \in B^n$, then $(1-t)x + ty \in B^n$ for all $t \in [0,1]$.
> Therefore $\pi_1(B^n, x_0) = 0$.

^prop-26-5

> [!remark]- Connections
> - Instance of [[§23 The Fundamental Group#^ex-23-2|Convex Subsets of ℝⁿ are Simply Connected]].

> [!proof]+ Proof
> **Convexity:** By the triangle inequality,
>
> $$
> \|(1-t)x + ty\| \leq (1-t)\|x\| + t\|y\| \leq (1-t) \cdot 1 + t \cdot 1 = 1.
> $$
>
> **$\pi_1 = 0$:** Let $f$ be a loop at $x_0 \in B^n$. The [[§22 Homotopy of Paths#^thm-22-1|straight-line homotopy]] $H(s, t) = (1-t)f(s) + t \cdot x_0$ satisfies $H(s,0) = f(s)$, $H(s,1) = x_0$, and $H(0,t) = H(1,t) = (1-t)x_0 + tx_0 = x_0$. By convexity, $H(s,t) \in B^n$ for all $s, t$. So every loop contracts to a point.

^pf-26-5

*Uses:* [[§22 Homotopy of Paths#^thm-22-1|§22.1]]

> [!theorem] Theorem §26.6: No-Retraction Theorem (Munkres 55.2)
> There is no retraction of $B^2$ onto $S^1$.

^thm-26-6

> [!remark]- Connections
> - All dimensions: [[§25a Retractions and Fixed Points#^thm-26-9|Generalized No-Retraction Theorem]].

> [!proof]+ Proof
> Suppose for contradiction that $r: B^2 \to S^1$ is a retraction, i.e., $r$ is continuous and $r(a) = a$ for all $a \in S^1$. We derive a contradiction using $\pi_1$.
>
> **Step 1: Set up the maps.** Let $j: S^1 \hookrightarrow B^2$ be the inclusion map. Since $r$ fixes every point of $S^1$, the composition $r \circ j: S^1 \to S^1$ satisfies $(r \circ j)(a) = r(a) = a$ for all $a \in S^1$. That is,
>
> $$
> r \circ j = \operatorname{id}_{S^1}.
> $$
>
> **Step 2: Apply $\pi_1$ (functoriality).** Both $j$ and $r$ are continuous maps, so by the induced homomorphism construction ([[§23 The Fundamental Group#^def-23-4|§23]]), each gets an induced group homomorphism:
>
> $$
> j_*: \pi_1(S^1, b_0) \to \pi_1(B^2, b_0), \qquad r_*: \pi_1(B^2, b_0) \to \pi_1(S^1, b_0).
> $$
>
> (Here $j_*([f]) = [j \circ f]$ and $r_*([g]) = [r \circ g]$—compose loops with the maps.) By the functorial properties ([[Functoriality of π₁|§23]]):
> - **Composition rule:** $(r \circ j)_{\ast} = r_{\ast} \circ j_{\ast}$.
> - **Identity rule:** $(\operatorname{id}_{S^1})_{\ast} = \operatorname{id}$ on $\pi_1(S^1, b_0)$.
>
> Since $r \circ j = \operatorname{id}_{S^1}$, we combine:
>
> $$
> r_* \circ j_* = (r \circ j)_* = (\operatorname{id}_{S^1})_* = \operatorname{id}.
> $$
>
> **Step 3: Conclude $j_{\ast}$ is injective.** If $j_{\ast}([f]) = j_{\ast}([g])$, apply $r_{\ast}$ to both sides:
>
> $$
> [f] = (r_* \circ j_*)([f]) = (r_* \circ j_*)([g]) = [g].
> $$
>
> So $j_*$ is injective.
>
> **Step 4: Contradiction.** We have computed $\pi_1(S^1) \cong \mathbb{Z}$ ([[Fundamental Group of the Circle|Theorem §24.10]]) and $\pi_1(B^2) = 0$ ([[§25a Retractions and Fixed Points#^prop-26-5|the proposition above]]: $B^2$ is convex, so every loop contracts via the straight-line homotopy). The homomorphism $j_{\ast}: \mathbb{Z} \to 0$ must send every element to $0$ (the only element of the trivial group). In particular, $j_{\ast}(1) = j_{\ast}(2) = 0$, so $j_{\ast}$ is not injective. This contradicts Step 3.

^pf-26-6

*Uses:* [[§23 The Fundamental Group#^def-23-4|Def. §23.4]], [[Functoriality of π₁|§23.5]], [[Fundamental Group of the Circle|§24.10]], [[§25a Retractions and Fixed Points#^prop-26-5|§26.5]]

![[m590-26-9.svg]]
*The blue boundary loop $f$ generates $\pi_1(S^1, b_0) \cong \mathbb{Z}$, but inside the convex disk the straight-line homotopy $(1-t)f(s) + t\,b_0$ shrinks it (lighter circles) to $b_0$. A retraction $r$ fixes $f$, so it would carry this shrinking into $S^1$ and contract a generator of $\mathbb{Z}$. That is the algebraic contradiction “$j_{\ast}: \mathbb{Z} \to 0$ is injective”, drawn as a picture.*

> [!remark] Remark: Why This Matters
> This is the first real application of $\pi_1$: a purely topological fact (no retraction exists) proved using algebra ($\mathbb{Z} \not\cong 0$). The proof pattern — assume a map exists, apply $\pi_1$, get a contradiction from group theory — is the template for all obstruction arguments. The [[Brouwer Fixed Point Theorem|Brouwer fixed point theorem below]] is a direct consequence.

^rem-26-2

> [!theorem] Theorem §26.7: Brouwer Fixed Point Theorem for $B^2$ (Munkres 55.6)
> Every continuous map $f: B^2 \to B^2$ has a fixed point.

^thm-26-7

> [!remark]- Connections
> - The one-dimensional case ($B^1 = [-1,1]$) follows from the [[Intermediate Value Theorem]].
> - All dimensions: [[§25a Retractions and Fixed Points#^thm-26-10|Generalized Brouwer Fixed Point Theorem]].

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
> &= \underbrace{(d_1^2 + d_2^2)}_{\|\mathbf{d}\|^2}\,t^2 + \underbrace{2(p_1 d_1 + p_2 d_2)}_{2\,\mathbf{p} \cdot \mathbf{d}}\,t + \underbrace{(p_1^2 + p_2^2)}_{\|\mathbf{p}\|^2}.
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

*Uses:* [[§25a Retractions and Fixed Points#^def-26-1|Def. §26.1]], [[No-Retraction Theorem|§26.6]]

![[m590-26-10.svg]]
*The ray construction. Starting at $f(x)$ and passing through $x$, the ray leaves $B^2$ at $r(x) = \gamma(t_0)$ (red). For a boundary point $y$ the exit point is $y$ itself ($t_0 = 1$), so $r$ fixes $S^1$. The construction needs only one thing: a direction $x - f(x) \neq 0$, i.e. no fixed point.*

> [!remark] Remark
> The Brouwer fixed point theorem is a purely existential result—it tells you a fixed point exists but gives no method for finding it. The proof illustrates the power of algebraic topology: the computation $\pi_1(S^1) \cong \mathbb{Z} \neq 0$ ([[Fundamental Group of the Circle|§24.10]]) (which took real work via [[§24 Covering Spaces|covering spaces]]) has a concrete geometric consequence about maps of the disk to itself.

^rem-26-3

## Generalization to Higher Dimensions

All three results—the [[§24a Lifting and the Fundamental Group of the Circle#^lem-24-12|nullhomotopy extension lemma]], the [[No-Retraction Theorem|no-retraction theorem]], and the [[Brouwer Fixed Point Theorem|Brouwer fixed point theorem]]—generalize to arbitrary dimension. The proofs of the first and third are identical to the $B^2$ case; the second requires tools beyond $\pi_1$.

> [!theorem] Lemma §26.8: Generalized Nullhomotopy Lemma (Munkres 55.3 for $S^n$)
> Let $h: S^n \to X$ be continuous. Then $h$ is [[§22 Homotopy of Paths#^def-22-2|nullhomotopic]] if and only if $h$ extends to a continuous map $k: B^{n+1} \to X$ (i.e., $k|_{S^n} = h$).

^lem-26-8

> [!remark]- Connections
> - The case $n = 1$, together with the $\pi_1$ criterion: [[§24a Lifting and the Fundamental Group of the Circle#^lem-24-12|Equivalent Conditions for Nullhomotopy]].

> [!proof]+ Proof
> **($\Leftarrow$): Extension $\Rightarrow$ nullhomotopic.** Given $k: B^{n+1} \to X$ with $k|_{S^n} = h$, the homotopy is $H: S^n \times I \to X$, $H(x, t) = k((1-t)x)$:
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
> Continuous + surjective + closed = quotient map ([[§12 Quotient Topology#^prop-12-2|§12]]).
>
> *Step 2: $H$ is constant on fibers of $\pi$.* For $t < 1$, $\pi$ is injective ($\pi(x,t) = (1-t)x$ determines both $t$ and $x$ uniquely), so there is nothing to check. The only non-trivial fiber is $\pi^{-1}(0) = S^n \times \{1\}$, where $H(x, 1) = c$ for all $x$—same value. ✓
>
> *Step 3: Universal Property.* Since $\pi$ is a quotient map and $H$ is constant on fibers, the [[Universal Property of Quotient Maps|Universal Property]] gives a unique continuous $k: B^{n+1} \to X$ with $k \circ \pi = H$.
>
> *Step 4: $k|_{S^n} = h$.* For $x \in S^n$: $k(x) = k(\pi(x, 0)) = H(x, 0) = h(x)$. ✓

^pf-26-8

*Uses:* [[Universal Property of Quotient Maps|§12.3]], [[§12 Quotient Topology#^prop-12-2|§12.2]], [[Closed Subspace of a Compact Space is Compact|§15.2]], [[Continuous Image of a Compact Space is Compact|§15.3]], [[Compact Subspace of a Hausdorff Space is Closed|§15.4]]

> [!theorem] Theorem §26.9: Generalized No-Retraction Theorem
> For each $n \geq 0$, there is no retraction $r: B^{n+1} \to S^n$.

^thm-26-9

*The course proves only the case $n = 1$ ([[No-Retraction Theorem|Theorem §26.6]]). The case $n = 0$ is connectedness: a retraction $B^1 = [-1, 1] \to S^0 = \{-1, 1\}$ would be a continuous surjection (it fixes both points) from a [[§14 Connected Subspaces of ℝ#^cor-14-2|connected]] space onto a disconnected one, contradicting [[Continuous Image of a Connected Space is Connected|Theorem §13.3]]. For $n \geq 2$ the proof needs homology, and the theorem is taken as given (remark below).*

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
> The proof is identical to the $B^2$ case ([[§25a Retractions and Fixed Points#^pf-26-7|§26.7]])—the ray construction works in any dimension. The logical structure is:
>
> ![[m590-26-4.svg]]
> *The proof builds one thing, the red arrow: from a fixed-point-free $f$, the ray from $f(x)$ through $x$ produces a retraction $r: B^{n+1} \to S^n$, which the [[§25a Retractions and Fixed Points#^thm-26-9|no-retraction theorem]] forbids.*
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
> Thus $r: B^{n+1} \to S^n$ is a retraction, contradicting the [[§25a Retractions and Fixed Points#^thm-26-9|no-retraction theorem]].

^pf-26-10

*Uses:* [[Brouwer Fixed Point Theorem|§26.7]], [[§25a Retractions and Fixed Points#^thm-26-9|§26.9]]

> [!remark] Remark: Summary: The Logical Dependencies
> The full chain for dimension $n$:
>
> ![[m590-26-5.svg]]
> *Blue arrows are proved in these notes; the dashed gray arrow (no retraction for general $n$, from $H_n(S^n) \cong \mathbb{Z}$) needs homology and is taken as given. Everything to the right of “no retraction” uses only the ray construction and composition, so it holds in every dimension once that one input is granted.*
>
> For $n = 1$, we proved everything from scratch. For $n \geq 2$, the [[§25a Retractions and Fixed Points#^thm-26-9|no-retraction theorem]] is taken as given (it requires homology), but everything downstream follows by the same arguments.

^rem-26-5
