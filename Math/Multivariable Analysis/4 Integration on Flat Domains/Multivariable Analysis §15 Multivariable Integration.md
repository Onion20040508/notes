---
type: section
subject: "[[Multivariable Analysis]]"
chapter: 4
section: 15
tags: [multivariable-analysis, math452]
---
← [[Multivariable Analysis §14 Optimization and Lagrange Multipliers]] · ↑ [[Multivariable Analysis — 4 Integration on Flat Domains]] · [[Multivariable Analysis §16 Line Integrals and Green's Theorem]] →

## Part II: Integral Calculus and Vector Calculus

*Chapter 4: Integration on Flat Domains.*

## Motivation: Integration over General Domains

In single-variable calculus, we integrate over intervals $[a, b]$ ([[Single Variable Analysis §32 The Definition of the Riemann Integral|451 §32]]). In multivariable calculus, we want to integrate over more complicated domains $D \subseteq \mathbb{R}^2$ (or $\mathbb{R}^n$).

**Problem:** How do we define the “area” of a general set $D$?

**Approach:** Jordan measure — approximate $D$ using squares (or rectangles) that we “trust.”

> [!remark] Remark
> This construction can be generalized to Lebesgue measure, which is more powerful but beyond the scope of this course.

^rem-15-1

## Squares and Rectangles

> [!definition] Definition §15.1: Square/Rectangle
> A **square** (or rectangle) in $\mathbb{R}^2$ with corners $(x, y)$ and $(x + a, y + a)$ is:
>
> $$
> S = [x, x + a] \times [y, y + a].
> $$
>
> We **manually define** its area: $\text{Area}(S) = a^2$.
>
> More generally, a rectangle $R = [x_1, x_2] \times [y_1, y_2]$ has area $(x_2 - x_1)(y_2 - y_1)$.

^def-15-1

## Jordan Measure: Inner and Outer Approximations

**Goal:** Define the area of any set $D \subseteq \mathbb{R}^2$.

**Step 0: Draw a mesh.**

Consider a grid with mesh points at $\mathbb{Z} \times \mathbb{Z}$ (integer lattice). Each unit square has area 1. This is the “0-th approximation.”

> [!definition] Definition §15.2: 0-th Approximation
> For a set $D \subseteq \mathbb{R}^2$:
> - $\mathcal{S}_0^+ = \{ S : S \cap D \neq \emptyset \}$ = set of unit squares that **intersect** $D$.
> - $\mathcal{S}_0^- = \{ S : S \subseteq D \}$ = set of unit squares **entirely contained in** $D$.
>
> Define:
>
> $$
> \begin{aligned}
> A_0^+(D) &= \#(\mathcal{S}_0^+) \cdot 1^2 = \text{number of squares intersecting } D \quad \text{(outer approximation)} \\
> A_0^-(D) &= \#(\mathcal{S}_0^-) \cdot 1^2 = \text{number of squares inside } D \quad \text{(inner approximation)}
> \end{aligned}
> $$

^def-15-2

**Key observation:** $A_0^-(D) \leq \text{“true area”} \leq A_0^+(D)$.

### Refining the Mesh

**$i$-th subdivision:** Divide each side by $2^i$, so each square has side length $\dfrac{1}{2^i}$ and area $\dfrac{1}{2^{2i}} = \dfrac{1}{4^i}$.

> [!definition] Definition §15.3: $i$-th Approximation
> - $\mathcal{S}_i^+ = \{ S : S \cap D \neq \emptyset \}$ = squares (of side $1/2^i$) intersecting $D$.
> - $\mathcal{S}_i^- = \{ S : S \subseteq D \}$ = squares (of side $1/2^i$) entirely in $D$.
>
> $$
> \begin{aligned}
> A_i^+(D) &= \#(\mathcal{S}_i^+) \cdot \left( \frac{1}{2^i} \right)^2 \\
> A_i^-(D) &= \#(\mathcal{S}_i^-) \cdot \left( \frac{1}{2^i} \right)^2
> \end{aligned}
> $$

^def-15-3

**Properties:**
- $A_i^-(D) \leq A_{i+1}^-(D)$ (inner approximations increase as mesh refines)
- $A_i^+(D) \geq A_{i+1}^+(D)$ (outer approximations decrease as mesh refines)
- $A_i^-(D) \leq A_i^+(D)$ for all $i$

### Jordan Content

> [!definition] Definition §15.4: Inner and Outer Jordan Content
> $$
> \begin{aligned}
> \underline{A}(D) &= \lim_{i \to \infty} A_i^-(D) = \sup_i A_i^-(D) \quad \text{(inner Jordan content)} \\
> \overline{A}(D) &= \lim_{i \to \infty} A_i^+(D) = \inf_i A_i^+(D) \quad \text{(outer Jordan content)}
> \end{aligned}
> $$

^def-15-4

> [!remark]- Connections
> - The limits exist because the sequences are monotone and bounded: [[Monotone Convergence Theorem]] (451).
> - The same inner/outer squeeze as the 1D [[Single Variable Analysis §32 The Definition of the Riemann Integral#^def-32-2|Darboux lower and upper integrals]].

> [!definition] Definition §15.5: Jordan Measurable
> A set $D$ is **Jordan measurable** if $\underline{A}(D) = \overline{A}(D)$.
>
> In this case, the common value is the **Jordan content** (or **Jordan measure** or **area**) of $D$:
>
> $$
> \text{Area}(D) = \underline{A}(D) = \overline{A}(D).
> $$

^def-15-5

![[m452-15-3.svg]]
*Inner approximation (blue): squares entirely inside $D$; outer approximation (red $\cup$ blue): squares meeting $D$. Refining the mesh raises $A_i^-$ and lowers $A_i^+$; the region is Jordan measurable when the two limits agree. The mismatch lives entirely along the boundary — which is why measurability $\iff$ $\partial D$ has content zero.*

> [!remark] Remark
> The difference $A_i^+(D) - A_i^-(D)$ counts squares that straddle the boundary $\partial D$ ([[Multivariable Analysis §2 Open and Closed Sets#^def-2-3|Def. §2.3]]). As $i \to \infty$, these boundary squares have total area $\to 0$ if and only if $\partial D$ has “measure zero.”
>
> A set $D$ is Jordan measurable $\iff$ its boundary $\partial D$ has Jordan content zero ([[Multivariable Analysis §15 Multivariable Integration#^def-15-13|Def. §15.13]]).

^rem-15-2

### Almost Disjoint Sets

> [!definition] Definition §15.6: Almost Disjoint
> Two sets $D, E \subseteq \mathbb{R}^2$ are **almost disjoint** if their interiors ([[Multivariable Analysis §2 Open and Closed Sets#^def-2-3|Def. §2.3]]) do not intersect:
>
> $$
> \text{int}(D) \cap \text{int}(E) = \emptyset.
> $$
>
> Equivalently, they can only overlap on their boundaries.

^def-15-6

> [!remark] Remark
> Almost disjoint sets can share boundary points, but not interior points. For example, two adjacent squares sharing an edge are almost disjoint.

^rem-15-3

### Additivity of Jordan Measure

> [!theorem] Theorem §15.1: Additivity
> If $D$ and $E$ are both Jordan measurable and almost disjoint, then $D \cup E$ is Jordan measurable and:
>
> $$
> |D \cup E| = |D| + |E|.
> $$

^thm-15-1

> [!proof]+ Proof
> We prove this in two parts: first the upper bound (subadditivity), then the lower bound (superadditivity for almost disjoint sets).
>
> **Part 1: $A_k^+(D \cup E) \leq A_k^+(D) + A_k^+(E)$ (subadditivity of outer measure).**
>
> Consider $\mathcal{S}_k^+(D \cup E)$, the set of $k$-th level squares intersecting $D \cup E$.
>
> For any square $S$:
>
> $$
> S \in \mathcal{S}_k^+(D \cup E) \iff S \cap (D \cup E) \neq \emptyset \iff (S \cap D) \cup (S \cap E) \neq \emptyset \iff S \in \mathcal{S}_k^+(D) \text{ or } S \in \mathcal{S}_k^+(E).
> $$
>
> Therefore:
>
> $$
> \mathcal{S}_k^+(D \cup E) \subseteq \mathcal{S}_k^+(D) \cup \mathcal{S}_k^+(E).
> $$
>
> Counting elements (with possible overlap):
>
> $$
> \#\mathcal{S}_k^+(D \cup E) \leq \#\mathcal{S}_k^+(D) + \#\mathcal{S}_k^+(E).
> $$
>
> Multiplying by the area of each square $\left(\frac{1}{2^k}\right)^2$:
>
> $$
> A_k^+(D \cup E) \leq A_k^+(D) + A_k^+(E).
> $$
>
> Taking $k \to \infty$:
>
> $$
> \overline{A}(D \cup E) \leq \overline{A}(D) + \overline{A}(E).
> $$
>
> **Part 2: $A_k^-(D) + A_k^-(E) \leq A_k^-(D \cup E)$ (superadditivity of inner measure for almost disjoint sets).**
>
> Since $\text{int}(D) \cap \text{int}(E) = \emptyset$, we claim that $\mathcal{S}_k^-(D) \cap \mathcal{S}_k^-(E) = \emptyset$.
>
> Suppose $S \in \mathcal{S}_k^-(D)$ and $S \in \mathcal{S}_k^-(E)$. Then $S \subseteq D$ and $S \subseteq E$.
>
> Choose the center $\mathbf{x}$ of $S$. Since $S$ is contained in the interior of itself, $\mathbf{x}$ is an interior point of both $D$ and $E$. But this contradicts $\text{int}(D) \cap \text{int}(E) = \emptyset$.
>
> Therefore, $\mathcal{S}_k^-(D)$ and $\mathcal{S}_k^-(E)$ are disjoint.
>
> Also, $\mathcal{S}_k^-(D) \cup \mathcal{S}_k^-(E) \subseteq \mathcal{S}_k^-(D \cup E)$ since:
>
> $$
> S \subseteq D \Rightarrow S \subseteq D \cup E, \quad S \subseteq E \Rightarrow S \subseteq D \cup E.
> $$
>
> Since $\mathcal{S}_k^-(D)$ and $\mathcal{S}_k^-(E)$ are disjoint:
>
> $$
> \#\mathcal{S}_k^-(D) + \#\mathcal{S}_k^-(E) = \#(\mathcal{S}_k^-(D) \cup \mathcal{S}_k^-(E)) \leq \#\mathcal{S}_k^-(D \cup E).
> $$
>
> Therefore:
>
> $$
> A_k^-(D) + A_k^-(E) \leq A_k^-(D \cup E).
> $$
>
> Taking $k \to \infty$:
>
> $$
> \underline{A}(D) + \underline{A}(E) \leq \underline{A}(D \cup E).
> $$
>
> **Part 3: Combining the bounds.**
>
> We have:
>
> $$
> \underline{A}(D) + \underline{A}(E) \leq \underline{A}(D \cup E) \leq \overline{A}(D \cup E) \leq \overline{A}(D) + \overline{A}(E).
> $$
>
> Since $D$ and $E$ are Jordan measurable: $\underline{A}(D) = \overline{A}(D) = |D|$ and $\underline{A}(E) = \overline{A}(E) = |E|$.
>
> Thus:
>
> $$
> |D| + |E| \leq \underline{A}(D \cup E) \leq \overline{A}(D \cup E) \leq |D| + |E|.
> $$
>
> All inequalities are equalities, so $\underline{A}(D \cup E) = \overline{A}(D \cup E) = |D| + |E|$.
>
> Therefore $D \cup E$ is Jordan measurable with $|D \cup E| = |D| + |E|$.

^pf-15-1

*Uses:* [[Multivariable Analysis §15 Multivariable Integration#^def-15-3|Def. §15.3]], [[Multivariable Analysis §15 Multivariable Integration#^def-15-4|Def. §15.4]], [[Multivariable Analysis §15 Multivariable Integration#^def-15-5|Def. §15.5]], [[Multivariable Analysis §15 Multivariable Integration#^def-15-6|Def. §15.6]], [[Multivariable Analysis §2 Open and Closed Sets#^def-2-3|Def. §2.3]]

## Definition of the Integral

Now we define the integral of a function over a Jordan measurable set, analogous to Riemann integration in one dimension ([[Single Variable Analysis §32 The Definition of the Riemann Integral|451 §32]]).

> [!definition] Definition §15.7: Partition
> Let $D \subseteq \mathbb{R}^2$ be a bounded, Jordan measurable set. A **partition** of $D$ is a finite collection:
>
> $$
> \mathcal{T} = \{D_1, D_2, \ldots, D_N\}
> $$
>
> of Jordan measurable sets such that:
> 1. $\bigcup_{i=1}^{N} D_i = D$ (the pieces cover $D$)
> 2. $D_i$ and $D_j$ are almost disjoint for $i \neq j$ (interiors don't overlap)

^def-15-7

> [!definition] Definition §15.8: Upper and Lower Sums
> Given a bounded function $f: D \to \mathbb{R}$ and a partition $\mathcal{T} = \{D_1, \ldots, D_N\}$, define:
>
> $$
> M_i = \sup_{(x,y) \in D_i} f(x, y), \qquad m_i = \inf_{(x,y) \in D_i} f(x, y).
> $$
>
> The **upper sum** and **lower sum** are:
>
> $$
> U(f, \mathcal{T}) = \sum_{i=1}^{N} M_i |D_i|, \qquad L(f, \mathcal{T}) = \sum_{i=1}^{N} m_i |D_i|.
> $$

^def-15-8

> [!remark]- Connections
> - 1D version: [[Single Variable Analysis §32 The Definition of the Riemann Integral#^def-32-1|upper and lower (Darboux) sums]] (451 §32.1), with subintervals of length $t_k - t_{k-1}$ in place of pieces of area $|D_i|$.

> [!definition] Definition §15.9: Diameter and Mesh
> The **diameter** of a set $A \subseteq \mathbb{R}^2$ is:
>
> $$
> \text{diam}(A) = \sup_{\substack{(x, y) \in A \\ (x', y') \in A}} \left| (x, y) - (x', y') \right| = \sup_{\substack{(x, y) \in A \\ (x', y') \in A}} \sqrt{(x - x')^2 + (y - y')^2}.
> $$
>
> The **mesh** (or **norm**) of a partition $\mathcal{T} = \{D_1, \ldots, D_N\}$ is:
>
> $$
> \|\mathcal{T}\| = \max_{1 \leq i \leq N} \text{diam}(D_i).
> $$
>
> This measures the “scale” of the partition — the size of the largest piece.

^def-15-9

> [!definition] Definition §15.10: Integrable Function
> A bounded function $f: D \to \mathbb{R}$ is **integrable** (or **Riemann integrable**) over $D$ if:
>
> $$
> \lim_{\|\mathcal{T}\| \to 0} \sum_{i=1}^{N} (M_i - m_i) |D_i| = 0.
> $$
>
> Equivalently, the difference between the upper and lower sums vanishes as the partition becomes finer.

^def-15-10

![[m452-15-1.svg]]
*The two Darboux staircases over the same partition $\mathcal{T}$. Left: the lower sum $L(f,\mathcal{T}) = \sum m_i |D_i|$ with $m_i = \inf_{D_i} f$ — inscribed boxes, entirely under the surface. Right: the upper sum $U(f,\mathcal{T}) = \sum M_i |D_i|$ with $M_i = \sup_{D_i} f$ — circumscribing boxes, containing the surface. Every Riemann sum with arbitrary sample points is squeezed between them: $L(f,\mathcal{T}) \leq \sum f(\boldsymbol{\xi}_i)|D_i| \leq U(f,\mathcal{T})$. Integrability is exactly the statement that the gap $\sum (M_i - m_i)|D_i|$ — the skin between the two staircases — vanishes as $\|\mathcal{T}\| \to 0$; the common limit is $\iint_D f\,dA$. This is the 2D version of the upper/lower Darboux sums from [[Single Variable Analysis §32 The Definition of the Riemann Integral#^def-32-1|single-variable analysis]].*

> [!remark] Remark
> The condition says that as we refine the partition (make $\|\mathcal{T}\| \to 0$), the “error” between the upper and lower sums:
>
> $$
> U(f, \mathcal{T}) - L(f, \mathcal{T}) = \sum_{i=1}^{N} (M_i - m_i) |D_i|
> $$
>
> tends to zero. This is analogous to the Riemann criterion for integrability in one dimension ([[Single Variable Analysis §32 The Definition of the Riemann Integral#^thm-32-6|451 §32.6]]).

^rem-15-4

> [!remark]- Connections
> - 1D: the [[Single Variable Analysis §32 The Definition of the Riemann Integral#^thm-32-4|Cauchy criterion]] (451 §32.4) and its mesh form in [[Single Variable Analysis §32 The Definition of the Riemann Integral#^thm-32-6|Equivalence of the Two Integrals]] (451 §32.6).

> [!definition] Definition §15.11: The Integral
> If $f$ is integrable over $D$, the **integral** of $f$ over $D$ is the common limit:
>
> $$
> \iint_D f(x, y) \, dA = \lim_{\|\mathcal{T}\| \to 0} U(f, \mathcal{T}) = \lim_{\|\mathcal{T}\| \to 0} L(f, \mathcal{T}).
> $$

^def-15-11

> [!remark] Remark: Notation: $dA$, $dx\,dy$, and $dV$
> The symbol $dA$ denotes the **area element**. For rectangular partitions in Cartesian coordinates, each piece $D_i$ is a small rectangle with area $|D_i| = \Delta x \cdot \Delta y$. In the limit, we write:
>
> $$
> dA = dx \, dy.
> $$
>
> Thus, the following notations are equivalent for integrals in Cartesian coordinates:
>
> $$
> \iint_D f(x, y) \, dA = \iint_D f(x, y) \, dx \, dy.
> $$
>
> In other coordinate systems, $dA$ takes a different form. For example, in polar coordinates ([[Multivariable Analysis §15 Multivariable Integration#^thm-15-7|Theorem §15.7]]):
>
> $$
> dA = r \, dr \, d\theta.
> $$
>
> For triple integrals in $\mathbb{R}^3$, we use the **volume element** $dV$:
>
> $$
> dV = dx \, dy \, dz \quad \text{(Cartesian)}, \qquad dV = r \, dr \, d\theta \, dz \quad \text{(cylindrical)}, \qquad dV = \rho^2 \sin\phi \, d\rho \, d\phi \, d\theta \quad \text{(spherical)}.
> $$
>
> The general principle: when changing coordinates via a transformation with Jacobian $J$ ([[Multivariable Analysis §13 The Inverse Function Theorem#^def-13-1|Def. §13.1]]), the volume/area element transforms as:
>
> $$
> dA_{\text{new}} = |J| \, dA_{\text{old}}.
> $$

^rem-15-5

> [!remark] Remark: Evaluating the Integral
> To compute the integral, choose sample points $(\xi_i, \eta_i) \in D_i$ for each piece of the partition. Then:
>
> $$
> \iint_D f(x, y) \, dA = \lim_{\|\mathcal{T}\| \to 0} \sum_{i=1}^{N} f(\xi_i, \eta_i) |D_i|.
> $$
>
> The limit exists and equals the integral regardless of how the sample points are chosen (as long as $f$ is integrable).

^rem-15-6

> [!remark]- Connections
> - 1D: [[Single Variable Analysis §32 The Definition of the Riemann Integral#^def-32-3|Riemann sums]] (451 §32.3) and their agreement with the Darboux integral, [[Single Variable Analysis §32 The Definition of the Riemann Integral#^thm-32-6|451 §32.6]].

## Properties of the Integral

Throughout, assume $D$ is bounded and Jordan measurable, and all functions are integrable on $D$.

> [!theorem] Theorem §15.2: Scalar Multiplication
> If $f$ is integrable on $D$ and $c \in \mathbb{R}$, then $cf$ is integrable on $D$ and:
>
> $$
> \iint_D cf \, dA = c \iint_D f \, dA.
> $$

^thm-15-2

> [!proof]+ Proof
> Assume $c > 0$ (the case $c < 0$ is similar, and $c = 0$ is trivial).
>
> For any partition $\mathcal{T}$:
>
> $$
> S_{\mathcal{T}}^+(cf) = \sum_{i=1}^{N} \sup_{(x,y) \in D_i} (cf) \cdot |D_i| = \sum_{i=1}^{N} c \cdot \sup_{(x,y) \in D_i} f \cdot |D_i| = c \cdot S_{\mathcal{T}}^+(f).
> $$
>
> Similarly, $S_{\mathcal{T}}^-(cf) = c \cdot S_{\mathcal{T}}^-(f)$.
>
> Therefore:
>
> $$
> S_{\mathcal{T}}^+(cf) - S_{\mathcal{T}}^-(cf) = c \cdot \left( S_{\mathcal{T}}^+(f) - S_{\mathcal{T}}^-(f) \right).
> $$
>
> Since $f$ is integrable, $S_{\mathcal{T}}^+(f) - S_{\mathcal{T}}^-(f) \to 0$ as $\|\mathcal{T}\| \to 0$, so the same holds for $cf$.
>
> To evaluate: choose sample points $(\xi_i, \eta_i) \in D_i$. Then:
>
> $$
> \sum_{i=1}^{N} cf(\xi_i, \eta_i) |D_i| = c \sum_{i=1}^{N} f(\xi_i, \eta_i) |D_i| \xrightarrow{\|\mathcal{T}\| \to 0} c \iint_D f \, dA.
> $$

^pf-15-2

*Uses:* [[Multivariable Analysis §15 Multivariable Integration#^def-15-8|Def. §15.8]], [[Multivariable Analysis §15 Multivariable Integration#^def-15-10|Def. §15.10]], [[Multivariable Analysis §15 Multivariable Integration#^rem-15-6|§15 Rem. (Evaluating the Integral)]]

> [!theorem] Theorem §15.3: Additivity in the Integrand
> If $f$ and $g$ are integrable on $D$, then $f + g$ is integrable on $D$ and:
>
> $$
> \iint_D (f + g) \, dA = \iint_D f \, dA + \iint_D g \, dA.
> $$

^thm-15-3

> [!proof]+ Proof
> **Step 1: Bound the upper sums.**
>
> For any $(x, y) \in D_i$: $f(x,y) + g(x,y) \leq \sup_{D_i} f + \sup_{D_i} g$.
>
> Taking sup over $(x, y) \in D_i$: $\sup_{D_i}(f + g) \leq \sup_{D_i} f + \sup_{D_i} g$.
>
> Therefore:
>
> $$
> S_{\mathcal{T}}^+(f + g) = \sum_{i=1}^{N} \sup_{D_i}(f + g) \cdot |D_i| \leq \sum_{i=1}^{N} \left( \sup_{D_i} f + \sup_{D_i} g \right) |D_i| = S_{\mathcal{T}}^+(f) + S_{\mathcal{T}}^+(g).
> $$
>
> **Step 2: Bound the lower sums.**
>
> Similarly: $\inf_{D_i}(f + g) \geq \inf_{D_i} f + \inf_{D_i} g$.
>
> Therefore:
>
> $$
> S_{\mathcal{T}}^-(f + g) \geq S_{\mathcal{T}}^-(f) + S_{\mathcal{T}}^-(g).
> $$
>
> **Step 3: Integrability.**
>
> Combining:
>
> $$
> S_{\mathcal{T}}^-(f) + S_{\mathcal{T}}^-(g) \leq S_{\mathcal{T}}^-(f + g) \leq S_{\mathcal{T}}^+(f + g) \leq S_{\mathcal{T}}^+(f) + S_{\mathcal{T}}^+(g).
> $$
>
> Since $f$ and $g$ are integrable, both $S_{\mathcal{T}}^+(f) - S_{\mathcal{T}}^-(f) \to 0$ and $S_{\mathcal{T}}^+(g) - S_{\mathcal{T}}^-(g) \to 0$.
>
> By the [[Squeeze Theorem|squeeze theorem]], $S_{\mathcal{T}}^+(f+g) - S_{\mathcal{T}}^-(f+g) \to 0$, so $f + g$ is integrable.
>
> **Step 4: Evaluate the integral.**
>
> Choose sample points $(\xi_i, \eta_i) \in D_i$:
>
> $$
> \sum_{i=1}^{N} (f + g)(\xi_i, \eta_i) |D_i| = \sum_{i=1}^{N} f(\xi_i, \eta_i) |D_i| + \sum_{i=1}^{N} g(\xi_i, \eta_i) |D_i|.
> $$
>
> As $\|\mathcal{T}\| \to 0$:
>
> $$
> \iint_D (f + g) \, dA = \iint_D f \, dA + \iint_D g \, dA.
> $$

^pf-15-3

*Uses:* [[Multivariable Analysis §15 Multivariable Integration#^def-15-8|Def. §15.8]], [[Multivariable Analysis §15 Multivariable Integration#^def-15-10|Def. §15.10]], [[Multivariable Analysis §15 Multivariable Integration#^rem-15-6|§15 Rem. (Evaluating the Integral)]], [[Squeeze Theorem|451 §8.1]]

> [!remark]- Connections
> - Together with [[Multivariable Analysis §15 Multivariable Integration#^thm-15-2|Theorem §15.2]], the 2D version of [[Single Variable Analysis §33 Properties of the Riemann Integral#^thm-33-2|Linearity]] (451 §33.2).

> [!theorem] Theorem §15.4: Additivity over Domains
> Let $A$ and $B$ be Jordan measurable, almost disjoint sets. If $f$ is integrable on $A$, $B$, and $A \cup B$, then:
>
> $$
> \iint_{A \cup B} f \, dA = \iint_A f \, dA + \iint_B f \, dA.
> $$

^thm-15-4

> [!proof]+ Proof
> Let $\mathcal{T}_A$ be a partition of $A$ and $\mathcal{T}_B$ be a partition of $B$.
>
> Then $\mathcal{T}_A \cup \mathcal{T}_B$ is a partition of $A \cup B$ (since $A$ and $B$ are almost disjoint).
>
> If $\|\mathcal{T}_A\| \to 0$ and $\|\mathcal{T}_B\| \to 0$, then $\|\mathcal{T}_A \cup \mathcal{T}_B\| \to 0$.
>
> Suppose $\mathcal{T}_A$ has $N$ pieces and $\mathcal{T}_B$ has $M$ pieces. Then for sample points:
>
> $$
> \sum_{i=1}^{N+M} f(\xi_i, \eta_i) |D_i| = \underbrace{\sum_{i=1}^{N} f(\xi_i, \eta_i) |D_i|}_{\text{sum over } \mathcal{T}_A} + \underbrace{\sum_{i=1}^{M} f(\xi_i, \eta_i) |D_i|}_{\text{sum over } \mathcal{T}_B}.
> $$
>
> Taking $\|\mathcal{T}_A\|, \|\mathcal{T}_B\| \to 0$:
>
> $$
> \iint_{A \cup B} f \, dA = \iint_A f \, dA + \iint_B f \, dA.
> $$

^pf-15-4

*Uses:* [[Multivariable Analysis §15 Multivariable Integration#^def-15-6|Def. §15.6]], [[Multivariable Analysis §15 Multivariable Integration#^def-15-7|Def. §15.7]], [[Multivariable Analysis §15 Multivariable Integration#^def-15-9|Def. §15.9]], [[Multivariable Analysis §15 Multivariable Integration#^rem-15-6|§15 Rem. (Evaluating the Integral)]]

> [!remark]- Connections
> - 1D version: [[Single Variable Analysis §33 Properties of the Riemann Integral#^thm-33-5|Additivity over Subintervals]] (451 §33.5), where the “almost disjoint” pieces $[a,c]$ and $[c,b]$ share only the point $c$.

> [!remark] Remark: On the Intersection and Integrability
> A subtle point in the proof: when we combine $\mathcal{T}_A \cup \mathcal{T}_B$, pieces from $\mathcal{T}_A$ and $\mathcal{T}_B$ may overlap on $A \cap B$ (which lies in the boundaries since $A$ and $B$ are almost disjoint).
>
> Why doesn't this cause problems?
> - Since $A$ and $B$ are almost disjoint, $A \cap B \subseteq \partial A \cap \partial B$.
> - For Jordan measurable sets, the boundary has Jordan content zero ([[Multivariable Analysis §15 Multivariable Integration#^rem-15-2|§15 Remark]]): $|A \cap B| = 0$.
> - Any contribution from the intersection region has measure zero and doesn't affect the integral.
>
> More precisely, if a piece $D_i \in \mathcal{T}_A$ overlaps with a piece $D_j \in \mathcal{T}_B$, their overlap $D_i \cap D_j$ has Jordan content zero (it's contained in $A \cap B$). So even if we “double-count” this region, it contributes zero to both sums.
>
> This is why we need the hypothesis that $A$ and $B$ are **Jordan measurable** (not just arbitrary sets) — the boundary must have content zero for the additivity to work cleanly.

^rem-15-7

> [!remark] Remark
> To evaluate the integral, we only need *one* sequence of partitions whose mesh goes to zero. The limit is the same regardless of how we partition or where we choose sample points.

^rem-15-8

### Comparison / Mean-Value Property

> [!theorem] Theorem §15.5: Comparison Theorem
> If $f$ and $g$ are integrable on $D$ and $f \leq g$ on $D$, then:
>
> $$
> \iint_D f \, dA \leq \iint_D g \, dA.
> $$

^thm-15-5

> [!proof]+ Proof
> It suffices to show: if $f \geq 0$ on $D$, then $\iint_D f \, dA \geq 0$.
>
> This follows directly from the definition: for any partition $\mathcal{T}$ and sample points $(\xi_i, \eta_i) \in D_i$:
>
> $$
> \sum_{i=1}^{N} f(\xi_i, \eta_i) |D_i| \geq 0
> $$
>
> since each $f(\xi_i, \eta_i) \geq 0$ and $|D_i| \geq 0$.
>
> Taking the limit as $\|\mathcal{T}\| \to 0$ preserves the inequality.
>
> For the general case: if $f \leq g$, then $g - f \geq 0$, so $\iint_D (g - f) \, dA \geq 0$, which gives $\iint_D g \, dA \geq \iint_D f \, dA$.

^pf-15-5

*Uses:* [[Multivariable Analysis §15 Multivariable Integration#^rem-15-6|§15 Rem. (Evaluating the Integral)]], [[Multivariable Analysis §15 Multivariable Integration#^thm-15-2|§15.2]], [[Multivariable Analysis §15 Multivariable Integration#^thm-15-3|§15.3]]

> [!remark]- Connections
> - 1D version: [[Single Variable Analysis §33 Properties of the Riemann Integral#^thm-33-3|Monotonicity of the Integral]] (451 §33.3).

> [!theorem] Corollary §15.6: Absolute Value Inequality
> If $f$ is integrable on $D$, then $|f|$ is integrable and:
>
> $$
> \left| \iint_D f \, dA \right| \leq \iint_D |f| \, dA.
> $$

^cor-15-6

> [!proof]+ Proof
> Since $-|f| \leq f \leq |f|$, by the [[Multivariable Analysis §15 Multivariable Integration#^thm-15-5|comparison theorem]]:
>
> $$
> -\iint_D |f| \, dA \leq \iint_D f \, dA \leq \iint_D |f| \, dA.
> $$

^pf-15-6

*Uses:* [[Multivariable Analysis §15 Multivariable Integration#^thm-15-5|§15.5]]

> [!remark]- Connections
> - 1D version: [[Single Variable Analysis §33 Properties of the Riemann Integral#^thm-33-4|Absolute Values]] (451 §33.4), which also proves the integrability of $|f|$ that the proof here takes for granted.

### Iterated Integrals: The Simple Case

Consider the simple case where $D = [a, b] \times [c, d]$ is a rectangle.

Suppose $f$ is integrable on $D$. Partition:
- $[a, b]$ into $N$ pieces of width $h = \frac{b-a}{N}$
- $[c, d]$ into $M$ pieces of width $k = \frac{d-c}{M}$

This gives $N \times M$ small rectangles $D_{ij} = [a + (i-1)h, a + ih] \times [c + (j-1)k, c + jk]$.

The Riemann sum is:

$$
\sum_{i=1}^{N} \sum_{j=1}^{M} f(a + (i-1)h + \theta h, c + (j-1)k + \lambda k) \cdot hk
$$

for some $\theta, \lambda \in [0, 1]$ (or we can choose any sample point in $D_{ij}$).

Taking $h, k \to 0$ (i.e., $N, M \to \infty$):

$$
\iint_D f(x, y) \, dA = \int_a^b \int_c^d f(x, y) \, dy \, dx = \int_c^d \int_a^b f(x, y) \, dx \, dy.
$$

### Change of Variables: Polar Coordinates

> [!theorem] Theorem §15.7: Change of Variables to Polar Coordinates
> Let $D^* = \{(r, \theta) : a \leq r \leq b, \alpha \leq \theta \leq \beta\}$ be a region in polar coordinates, and let $D \subseteq \mathbb{R}^2$ be its image under the transformation $x = r\cos\theta$, $y = r\sin\theta$.
>
> If $f$ is continuous on $D$, then:
>
> $$
> \iint_D f(x, y) \, dx\, dy = \int_\alpha^\beta \int_a^b f(r\cos\theta, r\sin\theta) \cdot r \, dr \, d\theta.
> $$
>
> The factor $r$ is the absolute value of the Jacobian ([[Multivariable Analysis §13 The Inverse Function Theorem#^ex-13-4|Ex. §13.4]]): $\left| \dfrac{\partial(x, y)}{\partial(r, \theta)} \right| = r$.

^thm-15-7

> [!proof]+ Proof
> We prove this directly from the definition of the integral by computing areas of polar rectangles.
>
> **Step 1: Partition the polar region.**
>
> Partition:
> - $[a, b]$ into $M$ pieces of width $k = \frac{b-a}{M}$: radii $r_i = a + ik$ for $i = 0, 1, \ldots, M$.
> - $[\alpha, \beta]$ into $N$ pieces of width $h = \frac{\beta - \alpha}{N}$: angles $\theta_j = \alpha + jh$ for $j = 0, 1, \ldots, N$.
>
> This gives $M \times N$ polar rectangles $D_{ij}^*$ with:
> - Inner radius: $r_{i-1} = a + (i-1)k$
> - Outer radius: $r_i = a + ik$
> - Angular span: from $\theta_{j-1} = \alpha + (j-1)h$ to $\theta_j = \alpha + jh$
>
> **Step 2: Compute the area of each polar rectangle.**
>
> The area of a circular sector with radii $r_1$ to $r_2$ and angle $\Delta\theta$ is:
>
> $$
> \text{Area} = \frac{\Delta\theta}{2\pi} \cdot \pi r_2^2 - \frac{\Delta\theta}{2\pi} \cdot \pi r_1^2 = \frac{\Delta\theta}{2}(r_2^2 - r_1^2).
> $$
>
> For the $(i, j)$-th polar rectangle with $r_1 = a + (i-1)k$, $r_2 = a + ik$, $\Delta\theta = h$:
>
> $$
> |D_{ij}| = \frac{h}{2}\left( (a + ik)^2 - (a + (i-1)k)^2 \right).
> $$
>
> **Step 3: Expand the area formula.**
>
> $$
> \begin{aligned}
> (a + ik)^2 - (a + (i-1)k)^2 &= \left[ a^2 + 2aik + i^2k^2 \right] - \left[ a^2 + 2a(i-1)k + (i-1)^2k^2 \right] \\
> &= 2ak + \left( i^2 - (i-1)^2 \right) k^2 \\
> &= 2ak + (2i - 1)k^2.
> \end{aligned}
> $$
>
> Therefore:
>
> $$
> |D_{ij}| = \frac{h}{2}\left( 2ak + (2i-1)k^2 \right) = hk \left( a + \frac{(2i-1)k}{2} \right) = hk \cdot \bar{r}_i
> $$
>
> where $\bar{r}_i = a + (i - \frac{1}{2})k$ is the midpoint radius of the $i$-th annular strip.
>
> **Step 4: Form the Riemann sum.**
>
> Choose sample points in polar coordinates: $(\bar{r}_i, \bar{\theta}_j)$ where $\bar{r}_i = a + (i - \frac{1}{2})k$ and $\bar{\theta}_j = \alpha + (j - \frac{1}{2})h$.
>
> In Cartesian coordinates, these are:
>
> $$
> (x_{ij}, y_{ij}) = (\bar{r}_i \cos\bar{\theta}_j, \bar{r}_i \sin\bar{\theta}_j).
> $$
>
> The Riemann sum for $\iint_D f(x, y) \, dA$ is:
>
> $$
> \sum_{i=1}^{M} \sum_{j=1}^{N} f(x_{ij}, y_{ij}) \cdot |D_{ij}| = \sum_{i=1}^{M} \sum_{j=1}^{N} f(\bar{r}_i \cos\bar{\theta}_j, \bar{r}_i \sin\bar{\theta}_j) \cdot \bar{r}_i \cdot hk.
> $$
>
> **Step 5: Recognize as a Riemann sum in $(r, \theta)$.**
>
> Define $g(r, \theta) = f(r\cos\theta, r\sin\theta) \cdot r$. Then:
>
> $$
> \sum_{i=1}^{M} \sum_{j=1}^{N} f(\bar{r}_i \cos\bar{\theta}_j, \bar{r}_i \sin\bar{\theta}_j) \cdot \bar{r}_i \cdot hk = \sum_{i=1}^{M} \sum_{j=1}^{N} g(\bar{r}_i, \bar{\theta}_j) \cdot hk.
> $$
>
> This is exactly a Riemann sum for $\iint_{D^*} g(r, \theta) \, dr\, d\theta$ over the rectangle $[a, b] \times [\alpha, \beta]$.
>
> **Step 6: Take the limit.**
>
> As $M, N \to \infty$ (i.e., $h, k \to 0$):
>
> $$
> \iint_D f(x, y) \, dx\, dy = \lim_{M, N \to \infty} \sum_{i=1}^{M} \sum_{j=1}^{N} g(\bar{r}_i, \bar{\theta}_j) \cdot hk = \iint_{D^*} g(r, \theta) \, dr\, d\theta.
> $$
>
> By [[Fubini's Theorem|Fubini's theorem]] on the rectangle $[a, b] \times [\alpha, \beta]$:
>
> $$
> \iint_D f(x, y) \, dx\, dy = \int_\alpha^\beta \int_a^b f(r\cos\theta, r\sin\theta) \cdot r \, dr \, d\theta.
> $$

^pf-15-7

*Uses:* [[Multivariable Analysis §15 Multivariable Integration#^def-15-11|Def. §15.11]], [[Multivariable Analysis §15 Multivariable Integration#^rem-15-6|§15 Rem. (Evaluating the Integral)]], [[Fubini's Theorem|§15.8]]

> [!remark]- Connections
> - Special case of the general [[Multivariable Analysis §15 Multivariable Integration#^thm-15-14|Change of Variables Formula]] (§15.14, §15.17), revisited in [[Multivariable Analysis §15 Multivariable Integration#^ex-15-4|Ex. §15.4]].
> - In forms language the factor $r$ is the pullback $dx \wedge dy = r\,dr \wedge d\theta$: [[Multivariable Analysis §22 The Algebra of Differential Forms#^ex-22-4|Ex. §22.4]].

> [!remark] Remark: The Jacobian
> The factor $r$ appearing in the integrand is the **Jacobian** ([[Multivariable Analysis §13 The Inverse Function Theorem#^def-13-1|Def. §13.1]]) of the polar coordinate transformation:
>
> $$
> x = r\cos\theta, \quad y = r\sin\theta.
> $$
>
> $$
> J = \frac{\partial(x, y)}{\partial(r, \theta)} = \det \begin{pmatrix} \dfrac{\partial x}{\partial r} & \dfrac{\partial x}{\partial \theta} \\[8pt] \dfrac{\partial y}{\partial r} & \dfrac{\partial y}{\partial \theta} \end{pmatrix} = \det \begin{pmatrix} \cos\theta & -r\sin\theta \\ \sin\theta & r\cos\theta \end{pmatrix} = r\cos^2\theta + r\sin^2\theta = r.
> $$
>
> The proof above shows *why* the Jacobian appears: it measures how the transformation distorts area. A small rectangle $dr \times d\theta$ in polar coordinates maps to a region of area approximately $r \cdot dr \cdot d\theta$ in Cartesian coordinates.

^rem-15-9

![[m452-15-4.svg]]
*The Jacobian of the polar map $\Phi(r,\theta) = (r\cos\theta, r\sin\theta)$, seen three ways. Top: equal cells in the $(r,\theta)$ plane map to annular cells whose width grows with $r$ — the distortion is position-dependent. Bottom: zooming into one cell, the map straightens into its derivative $D\Phi$, sending the square to a rectangle with orthogonal sides $|\boldsymbol{\Phi}_r|\,dr = dr$ and $|\boldsymbol{\Phi}_\theta|\,d\theta = r_0\,d\theta$; hence $dx\,dy = r\,dr\,d\theta$ — the factor in every polar integral of §15 is literally the width of the cell. At $r = 0$ the tangential side collapses, $J = 0$, and $\Phi$ degenerates (all $\theta$ give the same point): the [[Inverse Function Theorem (several variables)|Inverse Function Theorem]]'s hypothesis fails exactly where polar coordinates fail.*

## Fubini's Theorem: Rigorous Treatment

Fubini's theorem allows us to compute double integrals as iterated single integrals and to change the order of integration. We develop this carefully.

> [!theorem] Theorem §15.8: Fubini's Theorem — Rectangle Case
> Let $f: [a, b] \times [c, d] \to \mathbb{R}$ be continuous. Then:
>
> $$
> \iint_{[a,b] \times [c,d]} f(x, y) \, dA = \int_a^b \left( \int_c^d f(x, y) \, dy \right) dx = \int_c^d \left( \int_a^b f(x, y) \, dx \right) dy.
> $$

^thm-15-8

> [!proof]+ Proof
> We prove the first equality; the second follows by symmetry.
>
> **Step 1: Setup the partitions.**
>
> Partition $[a, b]$ into $N$ equal subintervals of width $h = \frac{b-a}{N}$:
>
> $$
> a = x_0 < x_1 < \cdots < x_N = b, \quad x_i = a + ih.
> $$
>
> Partition $[c, d]$ into $M$ equal subintervals of width $k = \frac{d-c}{M}$:
>
> $$
> c = y_0 < y_1 < \cdots < y_M = d, \quad y_j = c + jk.
> $$
>
> This gives $N \times M$ small rectangles $R_{ij} = [x_{i-1}, x_i] \times [y_{j-1}, y_j]$, each with area $hk$.
>
> **Step 2: Riemann sum for the double integral.**
>
> Choose sample points $(\xi_i, \eta_j) \in R_{ij}$. The Riemann sum is:
>
> $$
> S_{N,M} = \sum_{i=1}^{N} \sum_{j=1}^{M} f(\xi_i, \eta_j) \cdot hk.
> $$
>
> As $N, M \to \infty$ (equivalently, $h, k \to 0$):
>
> $$
> S_{N,M} \to \iint_{[a,b] \times [c,d]} f(x, y) \, dA.
> $$
>
> **Step 3: Riemann sum for the iterated integral.**
>
> For the iterated integral, first fix $x = \xi_i$ and consider the inner integral:
>
> $$
> F(x) = \int_c^d f(x, y) \, dy.
> $$
>
> The [[Single Variable Analysis §32 The Definition of the Riemann Integral#^def-32-3|Riemann sum]] for $F(\xi_i)$ is:
>
> $$
> \sum_{j=1}^{M} f(\xi_i, \eta_j) \cdot k \approx F(\xi_i) = \int_c^d f(\xi_i, y) \, dy.
> $$
>
> Then the Riemann sum for the outer integral $\int_a^b F(x) \, dx$ is:
>
> $$
> \sum_{i=1}^{N} F(\xi_i) \cdot h \approx \int_a^b F(x) \, dx = \int_a^b \left( \int_c^d f(x, y) \, dy \right) dx.
> $$
>
> **Step 4: Connect the two.**
>
> Observe that:
>
> $$
> \sum_{i=1}^{N} \left( \sum_{j=1}^{M} f(\xi_i, \eta_j) \cdot k \right) h = \sum_{i=1}^{N} \sum_{j=1}^{M} f(\xi_i, \eta_j) \cdot hk = S_{N,M}.
> $$
>
> So the Riemann sum for the double integral equals the iterated Riemann sum.
>
> **Step 5: Take the limit.**
>
> Since $f$ is continuous on the compact set $[a,b] \times [c,d]$ ([[Heine–Borel Theorem|Heine–Borel]]), it is [[Topology §15 Compact Spaces#^rem-15-1|uniformly continuous]]. This ensures:
> - The inner integral $F(x) = \int_c^d f(x, y) \, dy$ exists for each $x$ ([[Single Variable Analysis §32 The Definition of the Riemann Integral#^thm-32-7|451 §32.7]]) and is continuous in $x$.
> - The Riemann sums converge uniformly.
>
> Taking $N, M \to \infty$:
>
> $$
> \iint_{[a,b] \times [c,d]} f(x, y) \, dA = \lim_{N,M \to \infty} S_{N,M} = \int_a^b \left( \int_c^d f(x, y) \, dy \right) dx.
> $$

^pf-15-8

*Uses:* [[Multivariable Analysis §15 Multivariable Integration#^def-15-11|Def. §15.11]], [[Multivariable Analysis §15 Multivariable Integration#^rem-15-6|§15 Rem. (Evaluating the Integral)]], [[Single Variable Analysis §32 The Definition of the Riemann Integral#^def-32-3|451 Def. §32.3]], [[Single Variable Analysis §32 The Definition of the Riemann Integral#^thm-32-7|451 §32.7]], [[Heine–Borel Theorem|590 §15.12]], [[Topology §15 Compact Spaces#^rem-15-1|590 §15 Rem. (uniform continuity on compact sets)]]

![[m452-15-2.svg]]
*Fubini's theorem geometrically: freeze $x$ and integrate over $y$ to get the cross-sectional area $A(x)$ (red slab); then integrate $A(x)$ over $x$ to stack the slabs into the volume. The iterated integral $\int\!\!\int f\,dy\,dx$ is this two-stage process; Fubini says it equals the double integral whenever $f$ is integrable.*

> [!remark]- Connections
> - Makes rigorous the simple-case computation (“Iterated Integrals: The Simple Case”) above; extended to curved regions in [[Multivariable Analysis §15 Multivariable Integration#^thm-15-9|Theorem §15.9]].
> - Its Type I/II form plus the [[Fundamental Theorem of Calculus]] in the inner variable proves [[Green's Theorem|Green's Theorem]] (§16.1), and one dimension up the [[Divergence Theorem in ℝⁿ|Divergence Theorem in ℝⁿ]] (§17.1).

> [!remark] Remark: Why Continuity Matters
> The key point is that $F(x) = \int_c^d f(x, y) \, dy$ must be well-defined and integrable. Continuity of $f$ guarantees this.
>
> More generally, Fubini's theorem holds if $f$ is **integrable** and the iterated integrals exist. The condition can be weakened to: $\iint_D |f| \, dA < \infty$ (absolute integrability).

^rem-15-10

### Fubini's Theorem for General Regions

> [!definition] Definition §15.12: Type I and Type II Regions
> A **Type I region** (vertically simple) is:
>
> $$
> D = \{(x, y) : a \leq x \leq b, \; g_1(x) \leq y \leq g_2(x)\}
> $$
>
> where $g_1, g_2: [a, b] \to \mathbb{R}$ are continuous with $g_1(x) \leq g_2(x)$.
>
> A **Type II region** (horizontally simple) is:
>
> $$
> D = \{(x, y) : c \leq y \leq d, \; h_1(y) \leq x \leq h_2(y)\}
> $$
>
> where $h_1, h_2: [c, d] \to \mathbb{R}$ are continuous with $h_1(y) \leq h_2(y)$.

^def-15-12

> [!theorem] Theorem §15.9: Fubini for Type I Regions
> If $D = \{(x, y) : a \leq x \leq b, \; g_1(x) \leq y \leq g_2(x)\}$ and $f$ is continuous on $D$, then:
>
> $$
> \iint_D f(x, y) \, dA = \int_a^b \left( \int_{g_1(x)}^{g_2(x)} f(x, y) \, dy \right) dx.
> $$

^thm-15-9

> [!proof]+ Proof
> We give a detailed proof that carefully controls the error from approximating the curved region with rectangles.
>
> **Setup and assumptions.**
>
> Let $D = \{(x, y) : a \leq x \leq b, \; \psi(x) \leq y \leq \varphi(x)\}$ where $\psi, \varphi: [a,b] \to \mathbb{R}$ are continuous with $\psi(x) \leq \varphi(x)$ for all $x \in [a, b]$.
>
> *Claim: $D$ is closed* ([[Multivariable Analysis §2 Open and Closed Sets#^def-2-4|Def. §2.4]]).
>
> Suppose $(x_k, y_k) \in D$ and $(x_k, y_k) \to (x_0, y_0)$ ([[Multivariable Analysis §1 Sequences and Limits in ℝⁿ#^def-1-1|Def. §1.1]]). Then $x_k \to x_0$ and $y_k \to y_0$. Since $(x_k, y_k) \in D$:
>
> $$
> a \leq x_k \leq b \quad \text{and} \quad \psi(x_k) \leq y_k \leq \varphi(x_k).
> $$
>
> Taking $k \to \infty$: since $[a,b]$ is closed, $a \leq x_0 \leq b$. By continuity of $\psi$ and $\varphi$:
>
> $$
> \psi(x_0) = \lim_{k \to \infty} \psi(x_k) \leq \lim_{k \to \infty} y_k = y_0 \leq \lim_{k \to \infty} \varphi(x_k) = \varphi(x_0).
> $$
>
> Thus $(x_0, y_0) \in D$, so $D$ is closed.
>
> *Boundedness.* Since $D$ is closed and bounded (contained in $[a, b] \times [\min \psi, \max \varphi]$), $D$ is compact ([[Heine–Borel Theorem|Heine–Borel]]). Since $f$ is continuous on the compact set $D$, $f$ is bounded ([[Continuous Image of a Compact Space is Compact|continuous image of compact is compact]]): there exists $B > 0$ such that $|f(x, y)| \leq B$ for all $(x, y) \in D$.
>
> Without loss of generality, embed $D$ in a square $[0, M] \times [0, M]$ for some $M > 0$.
>
> **Step 1: Partition the square into a grid.**
>
> Fix $\varepsilon > 0$. We will show the difference between the double integral and the iterated integral is $< C\varepsilon$ for some constant $C$ depending only on $B$ and $M$.
>
> Choose $k \in \mathbb{N}$ large (to be determined). Partition $[0, M]$ into $M \cdot 2^k$ intervals of width $h = \frac{1}{2^k}$:
>
> $$
> 0 = t_0 < t_1 < t_2 < \cdots < t_{M \cdot 2^k} = M, \quad t_i = \frac{i}{2^k}.
> $$
>
> This creates a grid of $(M \cdot 2^k)^2$ small squares, each of side $h = \frac{1}{2^k}$ and area $h^2 = \frac{1}{4^k}$.
>
> **Step 2: Use uniform continuity to control oscillation of boundary curves.**
>
> Since $\psi$ and $\varphi$ are continuous on the compact interval $[a, b]$, they are **uniformly continuous** ([[Single Variable Analysis §19 Uniform Continuity#^thm-19-1|451 §19.1]]).
>
> Thus, for our fixed $\varepsilon > 0$, there exists $\delta > 0$ such that:
>
> $$
> |x - x'| < \delta \implies |\varphi(x) - \varphi(x')| < \varepsilon \quad \text{and} \quad |\psi(x) - \psi(x')| < \varepsilon.
> $$
>
> Choose $k$ large enough that $\frac{1}{2^k} < \delta$. Then within any column of width $\frac{1}{2^k}$:
>
> $$
> \sup_{x \in [t_i, t_{i+1}]} \varphi(x) - \inf_{x \in [t_i, t_{i+1}]} \varphi(x) < \varepsilon.
> $$
>
> Similarly for $\psi$. This means: *within each column, the curves $\varphi$ and $\psi$ oscillate by less than $\varepsilon$*.
>
> **Step 3: Define approximating step functions.**
>
> For each column $[t_i, t_{i+1}]$ intersecting $[a, b]$, define:
>
> $$
> \begin{aligned}
> \varphi_k(x) &= \text{smallest grid value } \geq \sup_{x' \in [t_i, t_{i+1}]} \varphi(x') \quad \text{for } x \in [t_i, t_{i+1}] \\
> \psi_k(x) &= \text{largest grid value } \leq \inf_{x' \in [t_i, t_{i+1}]} \psi(x') \quad \text{for } x \in [t_i, t_{i+1}]
> \end{aligned}
> $$
>
> In other words:
> - $\varphi_k$ rounds $\varphi$ up to the nearest grid line (within each column, taking the sup first).
> - $\psi_k$ rounds $\psi$ down to the nearest grid line (within each column, taking the inf first).
>
> Then $\varphi_k$ and $\psi_k$ are step functions constant on each column, and:
>
> $$
> \psi_k(x) \leq \psi(x) \leq \varphi(x) \leq \varphi_k(x) \quad \text{for all } x \in [a, b].
> $$
>
> Also, define $a_k$ = largest grid point $\leq a$, and $b_k$ = smallest grid point $\geq b$.
>
> **Step 4: Define the rectangular approximation $D_k$.**
>
> Let:
>
> $$
> D_k = \{(x, y) : a_k \leq x \leq b_k, \; \psi_k(x) \leq y \leq \varphi_k(x)\}.
> $$
>
> This is a union of grid squares that contains $D$: specifically, $D \subseteq D_k$.
>
> The region $D_k$ is a “staircase” approximation to $D$, where each column consists of a stack of complete grid squares.
>
> **Step 5: Estimate the area of $D_k \setminus D$ (the error region).**
>
> The error region $D_k \setminus D$ consists of:
> 1. **Top boundary squares:** In each column $[t_i, t_{i+1}]$, the squares between $y = \varphi(x)$ and $y = \varphi_k(x)$.
>
>     Since $\sup \varphi - \inf \varphi < \varepsilon$ within the column (by uniform continuity), and $\varphi_k$ is the next grid line above $\sup \varphi$:
>
>     $$
>     \varphi_k(x) - \varphi(x) < \varepsilon + \frac{1}{2^k} < 2\varepsilon
>     $$
>
>     for $k$ large enough that $\frac{1}{2^k} < \varepsilon$.
> 2. **Bottom boundary squares:** Similarly, $\psi(x) - \psi_k(x) < 2\varepsilon$.
> 3. **Left boundary:** The strip from $x = a_k$ to $x = a$ has width $\leq \frac{1}{2^k} < \varepsilon$ and height $\leq M$.
> 4. **Right boundary:** The strip from $x = b$ to $x = b_k$ has width $\leq \frac{1}{2^k} < \varepsilon$ and height $\leq M$.
>
> Number of columns intersecting $[a, b]$: at most $(b - a) \cdot 2^k + 2 \leq M \cdot 2^k + 2$.
>
> Area contributed by top boundary squares in each column: $\leq 2\varepsilon \cdot \frac{1}{2^k}$.
>
> Total area from top boundary: $\leq 2\varepsilon \cdot \frac{1}{2^k} \cdot (M \cdot 2^k + 2) = 2\varepsilon(M + \frac{2}{2^k}) < 2\varepsilon(M + 1)$.
>
> Similarly for bottom boundary.
>
> Left/right boundary areas: each $\leq \varepsilon \cdot M$.
>
> Total:
>
> $$
> |D_k \setminus D| \leq 2\varepsilon(M+1) + 2\varepsilon(M+1) + 2\varepsilon M = \varepsilon(6M + 4).
> $$
>
> **Step 6: Compare integrals over $D$ and $D_k$.**
>
> Since $D \subseteq D_k$ ([[Multivariable Analysis §15 Multivariable Integration#^thm-15-4|additivity over domains]], [[Multivariable Analysis §15 Multivariable Integration#^cor-15-6|absolute value inequality]]):
>
> $$
> \left| \iint_D f \, dA - \iint_{D_k} f \, dA \right| = \left| \iint_{D_k \setminus D} f \, dA \right| \leq \iint_{D_k \setminus D} |f| \, dA \leq B \cdot |D_k \setminus D| \leq B\varepsilon(6M + 4).
> $$
>
> **Step 7: Apply Fubini for rectangles to $D_k$.**
>
> The key observation: $D_k$ is a union of grid squares, and within each column $[t_i, t_{i+1}]$, the region is a rectangle $[t_i, t_{i+1}] \times [\psi_k(x), \varphi_k(x)]$ (where $\psi_k, \varphi_k$ are constant on this column).
>
> By [[Fubini's Theorem|Fubini's theorem for rectangles]] (applied column by column):
>
> $$
> \iint_{D_k} f \, dA = \int_{a_k}^{b_k} \left( \int_{\psi_k(x)}^{\varphi_k(x)} f(x, y) \, dy \right) dx.
> $$
>
> **Step 8: Compare the iterated integrals.**
>
> We need to compare:
>
> $$
> \int_{a_k}^{b_k} \int_{\psi_k(x)}^{\varphi_k(x)} f \, dy \, dx \quad \text{vs.} \quad \int_a^b \int_{\psi(x)}^{\varphi(x)} f \, dy \, dx.
> $$
>
> For each fixed $x \in [a, b]$, since $\psi_k(x) \leq \psi(x) \leq \varphi(x) \leq \varphi_k(x)$ ([[Single Variable Analysis §33 Properties of the Riemann Integral#^thm-33-5|451 §33.5]], [[Single Variable Analysis §33 Properties of the Riemann Integral#^thm-33-4|451 §33.4]]):
>
> $$
> \begin{aligned}
> \left| \int_{\psi_k(x)}^{\varphi_k(x)} f \, dy - \int_{\psi(x)}^{\varphi(x)} f \, dy \right| &= \left| \int_{\psi_k(x)}^{\psi(x)} f \, dy + \int_{\varphi(x)}^{\varphi_k(x)} f \, dy \right| \\
> &\leq \int_{\psi_k(x)}^{\psi(x)} |f| \, dy + \int_{\varphi(x)}^{\varphi_k(x)} |f| \, dy \\
> &\leq B(\psi(x) - \psi_k(x)) + B(\varphi_k(x) - \varphi(x)) \\
> &\leq B \cdot 2\varepsilon + B \cdot 2\varepsilon = 4B\varepsilon.
> \end{aligned}
> $$
>
> Integrating over $x$:
>
> $$
> \left| \int_a^b \int_{\psi_k(x)}^{\varphi_k(x)} f \, dy \, dx - \int_a^b \int_{\psi(x)}^{\varphi(x)} f \, dy \, dx \right| \leq \int_a^b 4B\varepsilon \, dx = 4B\varepsilon(b - a) \leq 4BM\varepsilon.
> $$
>
> Also, the integrals over $[a_k, a]$ and $[b, b_k]$ contribute:
>
> $$
> \left| \int_{a_k}^{a} \int_{\psi_k}^{\varphi_k} f \, dy \, dx \right| \leq B \cdot M \cdot (a - a_k) \leq BM\varepsilon.
> $$
>
> Similarly for $[b, b_k]$. Total contribution from left/right strips: $\leq 2BM\varepsilon$.
>
> **Step 9: Combine all estimates.**
>
> $$
> \begin{aligned}
> &\left| \iint_D f \, dA - \int_a^b \int_{\psi(x)}^{\varphi(x)} f \, dy \, dx \right| \\
> &\leq \left| \iint_D f \, dA - \iint_{D_k} f \, dA \right| + \left| \iint_{D_k} f \, dA - \int_{a_k}^{b_k} \int_{\psi_k}^{\varphi_k} f \, dy \, dx \right| \\
> &\quad + \left| \int_{a_k}^{b_k} \int_{\psi_k}^{\varphi_k} f \, dy \, dx - \int_a^b \int_{\psi}^{\varphi} f \, dy \, dx \right| \\
> &\leq B\varepsilon(6M + 4) + 0 + (4BM\varepsilon + 2BM\varepsilon) \\
> &= B\varepsilon(6M + 4 + 6M) = B\varepsilon(12M + 4).
> \end{aligned}
> $$
>
> The middle term is $0$ because Fubini for rectangles gives exact equality for $D_k$.
>
> **Step 10: Conclusion.**
>
> Let $C = B(12M + 4)$. We have shown:
>
> $$
> \left| \iint_D f \, dA - \int_a^b \int_{\psi(x)}^{\varphi(x)} f \, dy \, dx \right| \leq C\varepsilon.
> $$
>
> Since $\varepsilon > 0$ was arbitrary and $C$ is independent of $\varepsilon$, the left side must equal $0$:
>
> $$
> \iint_D f(x, y) \, dA = \int_a^b \left( \int_{\psi(x)}^{\varphi(x)} f(x, y) \, dy \right) dx.
> $$

^pf-15-9

*Uses:* [[Multivariable Analysis §2 Open and Closed Sets#^def-2-4|Def. §2.4]], [[Multivariable Analysis §1 Sequences and Limits in ℝⁿ#^def-1-1|Def. §1.1]], [[Multivariable Analysis §15 Multivariable Integration#^thm-15-4|§15.4]], [[Multivariable Analysis §15 Multivariable Integration#^thm-15-5|§15.5]], [[Multivariable Analysis §15 Multivariable Integration#^cor-15-6|§15.6]], [[Fubini's Theorem|§15.8]], [[Heine–Borel Theorem|590 §15.12]], [[Continuous Image of a Compact Space is Compact|590 §15.3]], [[Single Variable Analysis §19 Uniform Continuity#^thm-19-1|451 §19.1]], [[Single Variable Analysis §33 Properties of the Riemann Integral#^thm-33-4|451 §33.4]], [[Single Variable Analysis §33 Properties of the Riemann Integral#^thm-33-5|451 §33.5]]

> [!theorem] Theorem §15.10: Fubini for Type II Regions
> If $D = \{(x, y) : c \leq y \leq d, \; h_1(y) \leq x \leq h_2(y)\}$ and $f$ is continuous on $D$, then:
>
> $$
> \iint_D f(x, y) \, dA = \int_c^d \left( \int_{h_1(y)}^{h_2(y)} f(x, y) \, dx \right) dy.
> $$

^thm-15-10

> [!proof]+ Proof
> The proof is identical to the [[Multivariable Analysis §15 Multivariable Integration#^thm-15-9|Type I case]], with the roles of $x$ and $y$ interchanged. The region is approximated by horizontal stacks of rectangles, and uniform continuity of $h_1, h_2$ controls the boundary oscillation.

^pf-15-10

*Uses:* [[Multivariable Analysis §15 Multivariable Integration#^thm-15-9|§15.9]], [[Single Variable Analysis §19 Uniform Continuity#^thm-19-1|451 §19.1]]

### Changing the Order of Integration

> [!theorem] Corollary §15.11: Changing Order of Integration
> If $D$ is both Type I and Type II (i.e., can be described either way), and $f$ is continuous on $D$, then:
>
> $$
> \int_a^b \int_{g_1(x)}^{g_2(x)} f(x, y) \, dy \, dx = \int_c^d \int_{h_1(y)}^{h_2(y)} f(x, y) \, dx \, dy.
> $$

^cor-15-11

> [!proof]+ Proof
> Both iterated integrals equal $\iint_D f \, dA$ by the [[Multivariable Analysis §15 Multivariable Integration#^thm-15-9|Type I]] and [[Multivariable Analysis §15 Multivariable Integration#^thm-15-10|Type II]] versions of Fubini's theorem.

^pf-15-11

*Uses:* [[Multivariable Analysis §15 Multivariable Integration#^thm-15-9|§15.9]], [[Multivariable Analysis §15 Multivariable Integration#^thm-15-10|§15.10]]

> [!remark] Remark: When to Change Order
> Changing the order of integration is useful when:
> - One order leads to an integral that is difficult or impossible to evaluate in closed form.
> - The other order simplifies the computation.
>
> The key step is to carefully describe the region $D$ in both Type I and Type II forms.

^rem-15-11

> [!example] Example §15.1: Changing Order of Integration
> Evaluate $\displaystyle \int_0^1 \int_x^1 e^{y^2} \, dy \, dx$.
>
> **Problem:** The inner integral $\int_x^1 e^{y^2} \, dy$ has no elementary antiderivative.
>
> **Solution:** Change the order of integration ([[Multivariable Analysis §15 Multivariable Integration#^cor-15-11|Corollary §15.11]]).
>
> The region is $D = \{(x, y) : 0 \leq x \leq 1, \; x \leq y \leq 1\}$.
>
> Rewrite as Type II: $D = \{(x, y) : 0 \leq y \leq 1, \; 0 \leq x \leq y\}$.
>
> Then:
>
> $$
> \int_0^1 \int_x^1 e^{y^2} \, dy \, dx = \int_0^1 \int_0^y e^{y^2} \, dx \, dy = \int_0^1 e^{y^2} \cdot y \, dy = \frac{1}{2} e^{y^2} \Big|_0^1 = \frac{e - 1}{2}.
> $$

^ex-15-1

### A Counterexample: When Fubini Fails

> [!example] Example §15.2: Failure without Absolute Integrability
> Consider $f(x, y) = \dfrac{x^2 - y^2}{(x^2 + y^2)^2}$ on $(0, 1] \times (0, 1]$.
>
> Compute the iterated integrals:
>
> $$
> \int_0^1 \left( \int_0^1 \frac{x^2 - y^2}{(x^2 + y^2)^2} \, dy \right) dx = \int_0^1 \frac{1}{x^2 + 1} \, dx = \frac{\pi}{4}.
> $$
>
> $$
> \int_0^1 \left( \int_0^1 \frac{x^2 - y^2}{(x^2 + y^2)^2} \, dx \right) dy = \int_0^1 \frac{-1}{y^2 + 1} \, dy = -\frac{\pi}{4}.
> $$
>
> The two iterated integrals give different values! This happens because:
>
> $$
> \iint_{(0,1] \times (0,1]} |f(x, y)| \, dA = +\infty.
> $$
>
> The function is not absolutely integrable, so Fubini's theorem does not apply.

^ex-15-2

> [!remark]- Connections
> - The integrals here are improper (the integrand is unbounded near the origin): [[Single Variable Analysis §36 Improper Integrals|451 §36]].

> [!theorem] Theorem §15.12: Fubini-Tonelli: Non-negative Functions
> If $f \geq 0$ is measurable on $D$, then:
>
> $$
> \iint_D f \, dA = \int \left( \int f \, dy \right) dx = \int \left( \int f \, dx \right) dy
> $$
>
> where all three quantities are equal (possibly $+\infty$).
>
> This is useful for checking absolute integrability: compute $\iint_D |f| \, dA$ using iterated integrals. If finite, Fubini applies to $f$.

^thm-15-12

## General Change of Variables

**The Core Idea.**

When we compute $\iint_D f(x,y) \, dx \, dy$, we are summing up $f$-values weighted by infinitesimal areas $dx \, dy$.

Under a coordinate transformation $(x, y) = \Phi(u, v)$, the domain $D$ becomes $D^*$ in the $(u, v)$-plane. But here's the key point: *the infinitesimal areas change*.

A small rectangle $du \times dv$ in the $(u,v)$-plane does **not** map to a rectangle of the same area in the $(x,y)$-plane. Instead, it maps to a (curvilinear) region with area approximately $|J| \, du \, dv$, where $J$ is the Jacobian determinant ([[Multivariable Analysis §13 The Inverse Function Theorem#^def-13-1|Def. §13.1]]).

![[m452-15-5.svg]]
*A small rectangle $du \cdot dv$ in the $(u,v)$-plane is carried by $\Phi$ to a curvilinear region in the $(x,y)$-plane of area $\approx |J|\,du\,dv$.*

To make the integral come out correctly, we must **compensate for this area distortion** by multiplying by $|J|$:

$$
\underbrace{\iint_D f(x, y) \, dx \, dy}_{\text{sum of } f \times \text{(true area)}} = \underbrace{\iint_{D^*} f(\Phi(u,v)) \cdot |J(u,v)| \, du \, dv}_{\text{sum of } f \times |J| \times du \, dv}
$$

The factor $|J|$ exactly cancels the area distortion, ensuring both sides compute the same weighted sum.

**Section Organization:**
1. **Preliminaries:** Jordan measurability and the 1D formula
2. **Main Theorem:** Statement for rectangular domains, with three proofs
3. **Extension:** General Jordan measurable domains
4. **Geometric Interpretation:** Determinants as volume distortion; higher dimensions
5. **Coordinate Systems and Worked Examples:** Polar, elliptical, spherical; full computations

### Preliminaries

> [!definition] Definition §15.13: Jordan Measure Zero
> A bounded set $E \subseteq \mathbb{R}^2$ has **Jordan measure zero** if for every $\varepsilon > 0$, there exist finitely many rectangles $R_1, \ldots, R_N$ such that:
>
> $$
> E \subseteq \bigcup_{k=1}^N R_k \quad \text{and} \quad \sum_{k=1}^N \text{Area}(R_k) < \varepsilon.
> $$

^def-15-13

> [!definition] Definition §15.14: Jordan Measurable Set
> A bounded set $D \subseteq \mathbb{R}^2$ is **Jordan measurable** if its boundary $\partial D$ ([[Multivariable Analysis §2 Open and Closed Sets#^def-2-3|Def. §2.3]]) has Jordan measure zero.

^def-15-14

> [!remark]- Connections
> - Agrees with the inner/outer-content definition [[Multivariable Analysis §15 Multivariable Integration#^def-15-5|Def. §15.5]] for bounded sets, by the [[Multivariable Analysis §15 Multivariable Integration#^rem-15-2|remark following it]].

> [!example] Example §15.3: Jordan Measurable Sets
> The following are Jordan measurable:
> - Rectangles, triangles, and polygons
> - Disks $\{(x,y): x^2 + y^2 \leq r^2\}$ and ellipses
> - [[Multivariable Analysis §15 Multivariable Integration#^def-15-12|Type I regions]]: $\{(x,y): a \leq x \leq b, \, \phi(x) \leq y \leq \psi(x)\}$ where $\phi, \psi$ are continuous
> - Type II regions: $\{(x,y): c \leq y \leq d, \, \phi(y) \leq x \leq \psi(y)\}$ where $\phi, \psi$ are continuous
> - Finite unions and intersections of the above
>
> **Non-example:** The set $\mathbb{Q}^2 \cap [0,1]^2$ (rationals in the unit square) is *not* Jordan measurable — its boundary is the entire square $[0,1]^2$.

^ex-15-3

> [!remark]- Connections
> - The non-example is the 2D analogue of the [[Single Variable Analysis §32 The Definition of the Riemann Integral#^ex-32-3|Dirichlet function]] (451 Ex. §32.3): its indicator function is not Riemann integrable.

> [!theorem] Lemma §15.13: One-Dimensional Change of Variables
> Let $g: [a, b] \to [\alpha, \beta]$ be a $C^1$ bijection with $g'(t) \neq 0$ throughout. If $f$ is continuous on $[\alpha, \beta]$, then:
>
> $$
> \int_\alpha^\beta f(x) \, dx = \int_a^b f(g(t)) \cdot |g'(t)| \, dt.
> $$

^lem-15-13

> [!proof]+ Proof
> Define $F(x) = \int_\alpha^x f(s) \, ds$, so $F'(x) = f(x)$ by the [[Single Variable Analysis §34 Fundamental Theorem of Calculus#^thm-34-4|Fundamental Theorem of Calculus]] (451 §34.4).
>
> Consider the composition $H(t) = F(g(t))$. By the [[Single Variable Analysis §28 Basic Properties of the Derivative#^thm-28-3|chain rule]]:
>
> $$
> H'(t) = F'(g(t)) \cdot g'(t) = f(g(t)) \cdot g'(t).
> $$
>
> Integrating from $a$ to $b$ ([[Single Variable Analysis §34 Fundamental Theorem of Calculus#^thm-34-1|451 §34.1]]):
>
> $$
> H(b) - H(a) = \int_a^b f(g(t)) \cdot g'(t) \, dt.
> $$
>
> But $H(b) - H(a) = F(g(b)) - F(g(a))$.
>
> If $g' > 0$: then $g(a) = \alpha$, $g(b) = \beta$, so $H(b) - H(a) = F(\beta) - F(\alpha) = \int_\alpha^\beta f(x) \, dx$.
>
> If $g' < 0$: then $g(a) = \beta$, $g(b) = \alpha$, and the formula gives a negative sign that cancels with $|g'| = -g'$.

^pf-15-13

*Uses:* [[Single Variable Analysis §34 Fundamental Theorem of Calculus#^thm-34-4|451 §34.4]], [[Single Variable Analysis §28 Basic Properties of the Derivative#^thm-28-3|451 §28.3]], [[Single Variable Analysis §34 Fundamental Theorem of Calculus#^thm-34-1|451 §34.1]]

> [!remark]- Connections
> - Both halves of the [[Fundamental Theorem of Calculus]] (451 §34) combined with the 1D chain rule; this lemma is the base case of every proof of [[Multivariable Analysis §15 Multivariable Integration#^thm-15-14|Theorem §15.14]] below.

### Main Theorem (Rectangular Domain)

> [!theorem] Theorem §15.14: Change of Variables Formula — Rectangular Case
> Let $D^* = [a,b] \times [c,d]$ be a rectangle. Let $\Phi: D^* \to D$ be a $C^1$ bijection with $C^1$ inverse, where $D = \Phi(D^*)$.
>
> Write $\Phi(u, v) = (\varphi(u, v), \psi(u, v)) = (x, y)$.
>
> Assume the **Jacobian** ([[Multivariable Analysis §13 The Inverse Function Theorem#^def-13-1|Def. §13.1]])
>
> $$
> J = \frac{\partial(x, y)}{\partial(u, v)} = \det \begin{pmatrix} \varphi_u & \varphi_v \\ \psi_u & \psi_v \end{pmatrix} = \varphi_u \psi_v - \varphi_v \psi_u
> $$
>
> satisfies $J \neq 0$ on $D^*$.
>
> If $f$ is continuous on $\overline{D}$, then:
>
> $$
> \boxed{\iint_D f(x, y) \, dx \, dy = \iint_{D^*} f(\varphi(u, v), \psi(u, v)) \cdot |J(u, v)| \, du \, dv}
> $$

^thm-15-14

We present three different proofs, each offering a distinct perspective:

| **Proof** | **Method** | **Key Idea** |
|:-:|:--|:--|
| 1 | Linear Case + Taylor | Prove for linear maps, then linearize via Taylor |
| 2 | Implicit Function Theorem | Reduce 2D to two 1D substitutions via IFT |
| 3 | Two-Step Decomposition | Factor into primitive transformations |

**Proof 1** is the most geometric: it shows why the Jacobian determinant measures area distortion. **Proof 2** is the most analytic: it tracks coordinate changes explicitly. **Proof 3** (from Courant-John) generalizes most easily to $n$ dimensions.

---

> [!proof]+ First Proof: Linear Case + Taylor Linearization
> We give a rigorous proof by first establishing the result for linear transformations, then extending to the general $C^1$ case with explicit error estimates.
>
> **Part I: The Linear Case.**
>
> Consider the linear transformation:
>
> $$
> \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \begin{pmatrix} u \\ v \end{pmatrix}, \quad \text{i.e.,} \quad x = au + bv, \quad y = cu + dv.
> $$
>
> The Jacobian is $J = ad - bc$ (the determinant of the matrix).
>
> *Claim:* A rectangle $[u_0, u_0 + h] \times [v_0, v_0 + k]$ maps to a parallelogram with area $|J| \cdot hk$.
>
> *Proof of claim:* The four corners of the rectangle map to:
>
> $$
> \begin{aligned}
> (u_0, v_0) &\mapsto (au_0 + bv_0, \, cu_0 + dv_0) =: P_0 \\
> (u_0 + h, v_0) &\mapsto (au_0 + bv_0 + ah, \, cu_0 + dv_0 + ch) =: P_1 \\
> (u_0, v_0 + k) &\mapsto (au_0 + bv_0 + bk, \, cu_0 + dv_0 + dk) =: P_2 \\
> (u_0 + h, v_0 + k) &\mapsto (au_0 + bv_0 + ah + bk, \, cu_0 + dv_0 + ch + dk) =: P_3
> \end{aligned}
> $$
>
> Observe that $\mathbf{P_0 P_1} = (ah, ch)$ and $\mathbf{P_0 P_2} = (bk, dk)$. Also, $\mathbf{P_2 P_3} = (ah, ch) = \mathbf{P_0 P_1}$ and $\mathbf{P_1 P_3} = (bk, dk) = \mathbf{P_0 P_2}$. Thus the image is indeed a parallelogram (opposite sides are equal and parallel).
>
> The two edge vectors of the parallelogram are:
>
> $$
> \boldsymbol{\alpha} = (ah, ch), \quad \boldsymbol{\beta} = (bk, dk).
> $$
>
> The area of the parallelogram is $|\det(\boldsymbol{\alpha}, \boldsymbol{\beta})|$ ([[Linear Algebra 9C Determinants#^ladr-9-61|LADR 9.61]]):
>
> $$
> \text{Area} = \left| \det \begin{pmatrix} ah & bk \\ ch & dk \end{pmatrix} \right| = |adhk - bchk| = |ad - bc| \cdot hk = |J| \cdot hk.
> $$
>
> **Part II: General Case $\varphi, \psi \in C^1(D^*)$.**
>
> Now consider the general transformation $\Phi(u, v) = (\varphi(u, v), \psi(u, v))$ where $\varphi, \psi$ are $C^1$ on a compact domain $\overline{D^*}$.
>
> Assume $J \neq 0$ on $D^*$ (WLOG, say $J > 0$; the case $J < 0$ is similar with $|J| = -J$).
>
> **Step 1: Taylor expansion with explicit remainder.**
>
> Fix a point $(u_0, v_0) \in D^*$. For $(u, v)$ near $(u_0, v_0)$, [[Multivariable Taylor's Theorem|Taylor's theorem]] gives:
>
> $$
> \begin{aligned}
> \varphi(u, v) &= \varphi(u_0, v_0) + \varphi_u(u_0, v_0)(u - u_0) + \varphi_v(u_0, v_0)(v - v_0) + R_\varphi(u, v) \\
> \psi(u, v) &= \psi(u_0, v_0) + \psi_u(u_0, v_0)(u - u_0) + \psi_v(u_0, v_0)(v - v_0) + R_\psi(u, v)
> \end{aligned}
> $$
>
> where the remainders satisfy:
>
> $$
> |R_\varphi(u, v)|, |R_\psi(u, v)| \leq M \cdot \|(u - u_0, v - v_0)\|^2
> $$
>
> for some constant $M$ depending on bounds for the second derivatives of $\varphi, \psi$.
>
> **Step 2: Image of a small rectangle.**
>
> Consider the rectangle $R = [u_0, u_0 + h] \times [v_0, v_0 + k]$. Define the **linearized map** at $(u_0, v_0)$ ([[Multivariable Analysis §6 Differentiability#^def-6-2|Def. §6.2]]):
>
> $$
> L(u, v) = \Phi(u_0, v_0) + J_\Phi(u_0, v_0) \cdot \begin{pmatrix} u - u_0 \\ v - v_0 \end{pmatrix}
> $$
>
> where $J_\Phi = \begin{pmatrix} \varphi_u & \varphi_v \\ \psi_u & \psi_v \end{pmatrix}$ is the Jacobian matrix.
>
> By Part I, the linearized map $L$ takes $R$ to a parallelogram $P$ with:
>
> $$
> \text{Area}(P) = |J(u_0, v_0)| \cdot hk.
> $$
>
> **Step 3: Rigorous error estimate for curvilinear vs. parallelogram area.**
>
> The actual image $\Phi(R)$ is a curvilinear quadrilateral. We need to show the area differs from the parallelogram area by a controllable amount.
>
> *Setup:* Divide $D^*$ into small squares of side $1/2^m$. The number of squares is $2^k \cdot 2^k = 2^{2k}$ for some $k$.
>
> Since $\varphi, \psi \in C^1(\overline{D^*})$, the functions $\varphi, \psi, \varphi_u, \varphi_v, \psi_u, \psi_v$ are all [[Topology §15 Compact Spaces#^rem-15-1|uniformly continuous]] on the compact domain. Also, assume these are bounded by some constant $B$:
>
> $$
> |\varphi_u|, |\varphi_v|, |\psi_u|, |\psi_v|, |\varphi|, |\psi| \leq B.
> $$
>
> *Focus on one small square:* Consider the square $[u_0, u_0 + h] \times [v_0, v_0 + k]$ where $h = k = 1/2^m$.
>
> A point $(u_0 + \theta h, v_0 + \alpha k)$ in this square (with $\theta, \alpha \in [0,1]$) maps to:
>
> $$
> \Phi(u_0 + \theta h, v_0 + \alpha k) = (\varphi(u_0 + \theta h, v_0 + \alpha k), \, \psi(u_0 + \theta h, v_0 + \alpha k)).
> $$
>
> The displacement from the corner $\Phi(u_0, v_0)$ is:
>
> $$
> \begin{aligned}
> &\Phi(u_0 + \theta h, v_0 + \alpha k) - \Phi(u_0, v_0) \\
> &= \big( \varphi(u_0 + \theta h, v_0 + \alpha k) - \varphi(u_0, v_0), \; \psi(u_0 + \theta h, v_0 + \alpha k) - \psi(u_0, v_0) \big).
> \end{aligned}
> $$
>
> *Linear approximation:* By the [[Mean Value Theorem]]:
>
> $$
> \begin{aligned}
> \varphi(u_0 + \theta h, v_0 + \alpha k) - \varphi(u_0, v_0) &= \varphi_u(u_0 + \theta' h, v_0 + \alpha' k) \cdot \theta h + \varphi_v(u_0 + \theta'' h, v_0 + \alpha'' k) \cdot \alpha k
> \end{aligned}
> $$
>
> for some intermediate points.
>
> The **linearized approximation** at $(u_0, v_0)$ would give:
>
> $$
> \varphi_u(u_0, v_0) \cdot \theta h + \varphi_v(u_0, v_0) \cdot \alpha k.
> $$
>
> *Error in first component:*
>
> $$
> \begin{aligned}
> |\text{error}_1| &= \big| \varphi_u(u_0 + \theta' h, v_0 + \alpha' k) - \varphi_u(u_0, v_0) \big| \cdot h \\
> &\quad + \big| \varphi_v(u_0 + \theta'' h, v_0 + \alpha'' k) - \varphi_v(u_0, v_0) \big| \cdot k.
> \end{aligned}
> $$
>
> *Using uniform continuity:* For any $\varepsilon > 0$, there exists $M$ such that for all $m \geq M$:
>
> $$
> \sup_{D_{ij}} \varphi_u - \inf_{D_{ij}} \varphi_u \leq \varepsilon
> $$
>
> where $D_{ij}$ is any square of side $1/2^m$. The same holds for $\varphi_v, \psi_u, \psi_v$ (six versions of $M$: $M_1, M_2, \ldots$; take $M = \max$).
>
> Therefore, for $m \geq M$:
>
> $$
> |\text{error}_1| \leq \varepsilon \cdot \frac{1}{2^m} + \varepsilon \cdot \frac{1}{2^m} = \frac{2\varepsilon}{2^m}.
> $$
>
> Similarly, $|\text{error}_2| \leq \frac{2\varepsilon}{2^m}$.
>
> *Total position error:*
>
> $$
> |\text{error}| \leq \sqrt{(\text{error}_1)^2 + (\text{error}_2)^2} \leq \sqrt{4\varepsilon^2 \cdot \frac{1}{2^{2m}} + 4\varepsilon^2 \cdot \frac{1}{2^{2m}}} = \sqrt{2} \cdot \frac{2\varepsilon}{2^m}.
> $$
>
> *Geometric interpretation:* For each point in the parallelogram (the linearized image), draw a ball of radius $r = 2\sqrt{2} \varepsilon / 2^m$. The actual image point lies inside this ball.
>
> Take the union: $\bigcup_{p \in \text{parallelogram}} B(p; 2\sqrt{2}\varepsilon/2^m)$.
>
> *Area error estimate:* Assume the error region remains on the same side (no self-intersection, guaranteed when $\varepsilon$ is small relative to $|J|$). The error region is like a “fattened boundary” of the parallelogram.
> - The parallelogram has perimeter $\leq 4B \cdot (h + k) = 8B/2^m$ (since edge vectors have length $\leq B \cdot h$ and $B \cdot k$).
> - Fattening by radius $r = 2\sqrt{2}\varepsilon/2^m$ adds area $\leq \text{perimeter} \times r + \pi r^2$.
>
> Therefore:
>
> $$
> |\text{Area}(\Phi(R)) - \text{Area}(P)| \leq \frac{8B}{2^m} \cdot \frac{2\sqrt{2}\varepsilon}{2^m} + \pi \left( \frac{2\sqrt{2}\varepsilon}{2^m} \right)^2 = O\left( \frac{\varepsilon}{2^{2m}} \right).
> $$
>
> Since Area$(P) = |J| \cdot h \cdot k = |J|/2^{2m}$, the relative error is $O(\varepsilon)$, which can be made arbitrarily small.
>
> **Step 4: Riemann sum estimate.**
>
> Partition $D^*$ into $N = 2^{2m}$ small squares $R_{ij}$ of side $\Delta = 1/2^m$.
>
> Let $(u_{ij}, v_{ij})$ be a point in $R_{ij}$, and let $(x_{ij}, y_{ij}) = \Phi(u_{ij}, v_{ij})$.
>
> The Riemann sum for $\iint_D f \, dA$ is:
>
> $$
> S_N := \sum_{i,j} f(x_{ij}, y_{ij}) \cdot \text{Area}(\Phi(R_{ij})).
> $$
>
> By Step 3:
>
> $$
> \text{Area}(\Phi(R_{ij})) = |J(u_{ij}, v_{ij})| \cdot \Delta^2 + E_{ij}
> $$
>
> where $|E_{ij}| \leq C \varepsilon \cdot \Delta^2$ for $m \geq M(\varepsilon)$.
>
> Therefore:
>
> $$
> S_N = \sum_{i,j} f(x_{ij}, y_{ij}) \cdot |J(u_{ij}, v_{ij})| \cdot \Delta^2 + \sum_{i,j} f(x_{ij}, y_{ij}) \cdot E_{ij}.
> $$
>
> **Step 5: Error vanishes in the limit.**
>
> Since $f$ is continuous on the compact set $\overline{D}$, it is bounded ([[Continuous Image of a Compact Space is Compact|continuous image of compact is compact]]): $|f| \leq M_f$.
>
> The total error is:
>
> $$
> \left| \sum_{i,j} f(x_{ij}, y_{ij}) \cdot E_{ij} \right| \leq M_f \cdot \sum_{i,j} |E_{ij}| \leq M_f \cdot C\varepsilon \sum_{i,j} \Delta^2 = M_f \cdot C\varepsilon \cdot \text{Area}(D^*).
> $$
>
> Since $\varepsilon > 0$ was arbitrary, this error can be made as small as desired by choosing $m$ large enough.
>
> **Step 6: Transition from finite sum to integral (Riemann sum argument).**
>
> Cut the domain $D^*$ into $(2^m)^2$ pieces. Label all squares as $D_{ij}^{(m)}$ for $1 \leq i, j \leq 2^m$.
>
> After being mapped by $(\varphi, \psi)$, the square $D_{ij}^{(m)}$ maps to a curvilinear region $\Sigma_{ij}^{(m)}$.
>
> Denote the parallelogram approximation of $\Sigma_{ij}^{(m)}$ as $S_{ij}^{(m)}$.
>
> By Step 5, for all $\varepsilon > 0$, there exists $M$ such that for all $m \geq M$:
>
> $$
> \sum_{i=1}^{2^m} \sum_{j=1}^{2^m} \big| |\Sigma_{ij}^{(m)}| - |S_{ij}^{(m)}| \big| \leq C\varepsilon
> $$
>
> for some constant $C$ depending only on the bound $B$ for the partial derivatives.
>
> Now we relate the two sums:
>
> *Exact area sum* ([[Multivariable Analysis §15 Multivariable Integration#^thm-15-1|additivity]]):
>
> $$
> \sum_{i,j} |\Sigma_{ij}^{(m)}| = |\Sigma| = \text{Area}(D) = \iint_D dx \, dy.
> $$
>
> *Parallelogram approximation sum:*
>
> $$
> \sum_{i,j} |S_{ij}^{(m)}| = \sum_{i,j} \left| \det \begin{pmatrix} \varphi_u & \varphi_v \\ \psi_u & \psi_v \end{pmatrix}_{(u_{i-1}, v_{j-1})} \right| \cdot \left( \frac{1}{2^m} \right)^2 = \sum_{i,j} |J(u_{i-1}, v_{j-1})| \cdot \left( \frac{1}{2^m} \right)^2.
> $$
>
> This is a Riemann sum for $\iint_{D^*} |J| \, du \, dv$.
>
> As $m \to \infty$, the Riemann sum converges:
>
> $$
> \sum_{i,j} |S_{ij}^{(m)}| = \sum_{i,j} |J(u_{i-1}, v_{j-1})| \cdot \left( \frac{1}{2^m} \right)^2 \xrightarrow{m \to \infty} \iint_{D^*} |J| \, du \, dv.
> $$
>
> Since $\big| \sum_{i,j} |\Sigma_{ij}^{(m)}| - \sum_{i,j} |S_{ij}^{(m)}| \big| \leq C\varepsilon$ for $m \geq M$, and $\varepsilon$ was arbitrary:
>
> $$
> \iint_D dx \, dy = |\Sigma| = \iint_{D^*} |J| \, du \, dv.
> $$
>
> **Step 7: Derive the final result with $f$.**
>
> Now consider $\iint_D f(x, y) \, dx \, dy$.
>
> The “diameter” ([[Multivariable Analysis §15 Multivariable Integration#^def-15-9|Def. §15.9]]) of the curvilinear region $\Sigma_{ij}^{(m)}$ is:
>
> $$
> \text{diam}(\Sigma_{ij}^{(m)}) = \sqrt{(\varphi(u_i, v_j) - \varphi(u_{i-1}, v_{j-1}))^2 + (\psi(u_i, v_j) - \psi(u_{i-1}, v_{j-1}))^2} \leq CB \cdot \sqrt{(u_i - u_{i-1})^2 + (v_j - v_{j-1})^2}
> $$
>
> for some constant $C$ depending on the bounds of the partial derivatives.
>
> As $m \to \infty$, the diameter $\to 0$, so by the definition of the Riemann integral ([[Multivariable Analysis §15 Multivariable Integration#^def-15-11|Def. §15.11]]):
>
> $$
> \iint_D f(x, y) \, dx \, dy = \lim_{m \to \infty} \sum_{i,j} f(x_{ij}^*, y_{ij}^*) \cdot |\Sigma_{ij}^{(m)}|
> $$
>
> where $(x_{ij}^*, y_{ij}^*)$ is any point in $\Sigma_{ij}^{(m)}$.
>
> Choose $(x_{ij}^*, y_{ij}^*) = (\varphi(u_{i-1}, v_{j-1}), \psi(u_{i-1}, v_{j-1}))$. Then:
>
> $$
> \begin{aligned}
> \iint_D f(x, y) \, dx \, dy &= \lim_{m \to \infty} \sum_{i,j} f(\varphi(u_{i-1}, v_{j-1}), \psi(u_{i-1}, v_{j-1})) \cdot |\Sigma_{ij}^{(m)}| \\
> &= \lim_{m \to \infty} \sum_{i,j} f(\varphi(u_{i-1}, v_{j-1}), \psi(u_{i-1}, v_{j-1})) \cdot |J(u_{i-1}, v_{j-1})| \cdot \frac{1}{(2^m)^2} \\
> &= \iint_{D^*} f(\varphi(u, v), \psi(u, v)) \cdot |J(u, v)| \, du \, dv.
> \end{aligned}
> $$
>
> The second equality uses that $|\Sigma_{ij}^{(m)}| = |J| \cdot (1/2^m)^2 + O(\varepsilon/2^{2m})$ and the error vanishes in the limit (since $f$ is bounded and the total error is $O(\varepsilon)$).
>
> This completes the proof for the case where $D^*$ is a square.

^pf-15-14

*Uses:* [[Linear Algebra 9C Determinants#^ladr-9-61|LADR 9.61]], [[Multivariable Taylor's Theorem|§9.2]], [[Multivariable Analysis §6 Differentiability#^def-6-2|Def. §6.2]], [[Multivariable Analysis §13 The Inverse Function Theorem#^def-13-1|Def. §13.1]], [[Mean Value Theorem|451 §29.3]], [[Topology §15 Compact Spaces#^rem-15-1|590 §15 Rem. (uniform continuity on compact sets)]], [[Continuous Image of a Compact Space is Compact|590 §15.3]], [[Multivariable Analysis §15 Multivariable Integration#^thm-15-1|§15.1]], [[Multivariable Analysis §15 Multivariable Integration#^def-15-9|Def. §15.9]], [[Multivariable Analysis §15 Multivariable Integration#^def-15-11|Def. §15.11]]

> [!remark] Remark: Extension to Arbitrary Domains: Jordan Measurability
> The proof above assumes $D^*$ is a square (or rectangle). For arbitrary domains, we need additional assumptions and a more careful treatment using **Jordan measure**.
>
> **The Problem:** If $D^*$ is not a rectangle, how do we define the Riemann sum? We can't simply partition $D^*$ into small squares — some squares will partially overlap the boundary $\partial D^*$.
>
> **Solution: Jordan Measurable Domains.**
>
> *Definition:* A bounded set $D^* \subseteq \mathbb{R}^2$ is **Jordan measurable** if its boundary $\partial D^*$ has Jordan measure zero, i.e., for any $\varepsilon > 0$, the boundary can be covered by finitely many rectangles with total area $< \varepsilon$ ([[Multivariable Analysis §15 Multivariable Integration#^def-15-13|Def. §15.13]], [[Multivariable Analysis §15 Multivariable Integration#^def-15-14|Def. §15.14]]).
>
> *Equivalently:* The **inner Jordan measure** (supremum of areas of finite unions of rectangles contained in $D^*$) equals the **outer Jordan measure** (infimum of areas of finite unions of rectangles containing $D^*$) ([[Multivariable Analysis §15 Multivariable Integration#^def-15-4|Def. §15.4]], [[Multivariable Analysis §15 Multivariable Integration#^def-15-5|Def. §15.5]]).
>
> **Procedure for Arbitrary Jordan Measurable $D^*$:**
>
> *Step 1:* Enclose $D^*$ in a large rectangle $R = [a, b] \times [c, d]$.
>
> *Step 2:* Partition $R$ into small squares of side $1/2^m$. Classify each square $D_{ij}^{(m)}$ as:
> - **Interior squares:** $D_{ij}^{(m)} \subseteq D^*$ (entirely inside)
> - **Exterior squares:** $D_{ij}^{(m)} \cap D^* = \emptyset$ (entirely outside)
> - **Boundary squares:** $D_{ij}^{(m)} \cap \partial D^* \neq \emptyset$ (touch the boundary)
>
> *Step 3:* For the Riemann sum, sum only over interior squares:
>
> $$
> S_m^{\text{inner}} = \sum_{\substack{i,j \\ D_{ij}^{(m)} \subseteq D^*}} f(\varphi(u_{ij}), \psi(u_{ij})) \cdot |J(u_{ij})| \cdot \frac{1}{(2^m)^2}.
> $$
>
> Similarly, define the outer sum including boundary squares.
>
> *Step 4:* Since $\partial D^*$ has Jordan measure zero:
>
> $$
> \#\{\text{boundary squares}\} \cdot \frac{1}{(2^m)^2} \to 0 \quad \text{as } m \to \infty.
> $$
>
> Therefore, inner and outer sums converge to the same limit.
>
> **Additional Assumption Needed:**
>
> For the Change of Variables formula, we need both $D^*$ and $D = \Phi(D^*)$ to be Jordan measurable.
>
> *Key Lemma* ([[Multivariable Analysis §15 Multivariable Integration#^prop-15-16|Proposition §15.16]]): If $D^*$ is Jordan measurable and $\Phi: D^* \to D$ is a $C^1$ diffeomorphism with $J \neq 0$, then $D = \Phi(D^*)$ is also Jordan measurable.
>
> *Proof sketch:* The boundary $\partial D = \Phi(\partial D^*)$. Since $\Phi$ is $C^1$ and $\partial D^*$ has measure zero, the image $\Phi(\partial D^*)$ also has measure zero (Lipschitz maps preserve measure zero sets). $\square$
>
> **Refined Theorem Statement:**
>
> > Let $D^* \subseteq \mathbb{R}^2$ be a **bounded, Jordan measurable** domain. Let $\Phi: \overline{D^*} \to \overline{D}$ be a $C^1$ bijection with $C^1$ inverse and $J \neq 0$ on $D^*$. If $f$ is continuous on $\overline{D}$, then:
> >
> > $$
> > \iint_D f(x, y) \, dx \, dy = \iint_{D^*} f(\varphi(u, v), \psi(u, v)) \cdot |J(u, v)| \, du \, dv.
> > $$
>
> **Common Jordan Measurable Domains** ([[Multivariable Analysis §15 Multivariable Integration#^ex-15-3|Ex. §15.3]]):
> - Rectangles, triangles, polygons
> - Disks, ellipses
> - Regions bounded by $C^1$ curves (Type I and Type II regions)
> - Finite unions and intersections of the above
>
> **Non-Example:** The set of points in $[0,1]^2$ with both coordinates rational is bounded but *not* Jordan measurable (its boundary is the entire square, which has positive area).

^rem-15-12

> [!remark] Remark: Alternative: Lebesgue Integration
> In Lebesgue integration theory (MATH 551), the situation is cleaner:
> - The change of variables formula holds for any **Lebesgue measurable** set $D^*$.
> - No need for Jordan measurability — Lebesgue measure handles much more general sets.
> - The assumption “$J \neq 0$ everywhere” can be relaxed to “$J \neq 0$ almost everywhere.”
>
> However, for this course (Riemann integration), Jordan measurability is the appropriate condition.

^rem-15-13

---

> [!proof]+ Second Proof: Implicit Function Theorem Approach
> This approach uses IFT to introduce intermediate coordinates $(x, v)$, reducing the 2D change of variables to two applications of the 1D formula ([[Multivariable Analysis §15 Multivariable Integration#^lem-15-13|Lemma §15.13]]).
>
> **Setup and Assumptions.**
>
> Consider the transformation $\Phi(u, v) = (\varphi(u, v), \psi(u, v))$ with Jacobian $J = \varphi_u \psi_v - \varphi_v \psi_u$.
>
> Since $J \neq 0$ and the partial derivatives are continuous, at least one of $\varphi_u$ or $\varphi_v$ is nonzero at each point. WLOG, assume $\varphi_u > 0$ throughout (if not, we can partition the domain or relabel variables).
>
> Also assume $J > 0$ (the case $J < 0$ gives $|J| = -J$).
>
> **Step 1: Apply IFT to introduce $(x, v)$ coordinates.**
>
> Define $F(u, v, x) = \varphi(u, v) - x$. Since $F_u = \varphi_u > 0$, by the [[Multivariable Analysis §12 The Implicit Function Theorem#^thm-12-2|Implicit Function Theorem]], we can locally solve $F = 0$ for $u$:
>
> $$
> \exists \, u = U(x, v) \quad \text{such that} \quad \varphi(U(x, v), v) = x.
> $$
>
> The function $U$ is $C^1$ with derivatives computed by implicit differentiation. Differentiating $\varphi(U(x,v), v) = x$:
>
> $$
> \begin{aligned}
> \text{w.r.t. } x: \quad & \varphi_u \cdot U_x = 1 \quad \Longrightarrow \quad U_x = \frac{1}{\varphi_u} > 0. \\
> \text{w.r.t. } v: \quad & \varphi_u \cdot U_v + \varphi_v = 0 \quad \Longrightarrow \quad U_v = -\frac{\varphi_v}{\varphi_u}.
> \end{aligned}
> $$
>
> **Step 2: Define $\gamma(x, v)$ and compute its derivative.**
>
> Define the composed function:
>
> $$
> \gamma(x, v) := \psi(U(x, v), v).
> $$
>
> This gives $y$ as a function of $(x, v)$: when we hold $x$ fixed and vary $v$, the point $(x, y) = (x, \gamma(x, v))$ traces a curve in the $(x, y)$-plane.
>
> Compute $\gamma_v$ using the [[Multivariable Chain Rule|chain rule]]:
>
> $$
> \begin{aligned}
> \gamma_v &= \psi_u \cdot U_v + \psi_v = \psi_u \cdot \left( -\frac{\varphi_v}{\varphi_u} \right) + \psi_v \\
> &= \frac{-\psi_u \varphi_v + \psi_v \varphi_u}{\varphi_u} = \frac{\varphi_u \psi_v - \varphi_v \psi_u}{\varphi_u} = \frac{J}{\varphi_u} > 0.
> \end{aligned}
> $$
>
> The inequality $\gamma_v > 0$ shows that, for fixed $x$, the map $v \mapsto y = \gamma(x, v)$ is strictly increasing.
>
> **Step 3: Change variables $(x, y) \to (x, v)$ using the 1D formula.**
>
> Consider any region $R$ in the $(x, y)$-plane that is the image of a region $B$ in the $(x, v)$-plane under the map $(x, v) \mapsto (x, \gamma(x, v))$.
>
> For fixed $x$, the map $v \mapsto y = \gamma(x, v)$ satisfies $\frac{dy}{dv} = \gamma_v(x, v)$.
>
> By the 1D change of variables formula ([[Multivariable Analysis §15 Multivariable Integration#^lem-15-13|Lemma §15.13]]) applied to the inner integral:
>
> $$
> \int_{y_1(x)}^{y_2(x)} f(x, y) \, dy = \int_{v_1}^{v_2} f(x, \gamma(x, v)) \cdot \gamma_v(x, v) \, dv.
> $$
>
> Integrating over $x$ and using [[Multivariable Analysis §15 Multivariable Integration#^thm-15-9|Fubini]]:
>
> $$
> \iint_R f(x, y) \, dx \, dy = \iint_B f(x, \gamma(x, v)) \cdot \gamma_v(x, v) \, dx \, dv = \iint_B f(x, y) \cdot \frac{J}{\varphi_u} \, dx \, dv.
> $$
>
> **Step 4: Change variables $(x, v) \to (u, v)$ using the 1D formula again.**
>
> Now we transform from $(x, v)$ to $(u, v)$ via $x = \varphi(u, v)$, $v = v$.
>
> For fixed $v$, the map $u \mapsto x = \varphi(u, v)$ satisfies $\frac{dx}{du} = \varphi_u(u, v) > 0$.
>
> By the 1D formula applied to the inner integral (now integrating over $x$):
>
> $$
> \int_{x_1(v)}^{x_2(v)} g(x, v) \, dx = \int_{u_1}^{u_2} g(\varphi(u, v), v) \cdot \varphi_u(u, v) \, du.
> $$
>
> Applying this to our integral with $g(x, v) = f(x, \gamma(x, v)) \cdot \frac{J}{\varphi_u}$:
>
> $$
> \iint_B f(x, y) \cdot \frac{J}{\varphi_u} \, dx \, dv = \iint_{D^*} f(\varphi, \psi) \cdot \frac{J(u,v)}{\varphi_u(u,v)} \cdot \varphi_u(u, v) \, du \, dv.
> $$
>
> The $\varphi_u$ terms cancel:
>
> $$
> \iint_R f(x, y) \, dx \, dy = \iint_{D^*} f(\varphi(u, v), \psi(u, v)) \cdot J(u, v) \, du \, dv.
> $$
>
> Since we assumed $J > 0$, we have $J = |J|$, completing the proof.

^pf-15-14-2

*Uses:* [[Multivariable Analysis §15 Multivariable Integration#^lem-15-13|§15.13]], [[Multivariable Analysis §12 The Implicit Function Theorem#^thm-12-2|§12.2]], [[Multivariable Chain Rule|§10.2]], [[Multivariable Analysis §15 Multivariable Integration#^thm-15-9|§15.9]]

---

> [!proof]+ Third Proof: Two-Step Decomposition (Courant-John)
> This approach, from Courant & John's *Introduction to Calculus and Analysis*, decomposes the general transformation into two simpler “primitive” transformations, each changing only one variable at a time. This method extends naturally to higher dimensions.
>
> **Setup.** We want to prove:
>
> $$
> \iint_R f(x, y) \, dx \, dy = \iint_{R'} f(\phi(u, v), \psi(u, v)) \left| \frac{\partial(x, y)}{\partial(u, v)} \right| du \, dv
> $$
>
> where $x = \phi(u, v)$, $y = \psi(u, v)$ gives a 1-1 $C^1$ mapping of region $R$ onto region $R'$ with $J \neq 0$.
>
> **Key Idea: Factor the transformation into two primitive steps.**
>
> A **primitive transformation** is one that changes only one coordinate:
> - Type I: $(x, v) \mapsto (x, y)$ where $x$ stays fixed, $y = \Phi(v, x)$
> - Type II: $(u, v) \mapsto (x, v)$ where $v$ stays fixed, $x = \Psi(u, v)$
>
> *Claim:* Any $C^1$ transformation with $J \neq 0$ can be locally decomposed as a composition of two primitive transformations.
>
> *Proof of claim:* Since $J = \phi_u \psi_v - \phi_v \psi_u \neq 0$, at least one of $\phi_u$ or $\phi_v$ is nonzero.
>
> **Case 1:** If $\phi_u \neq 0$, define:
>
> $$
> \begin{aligned}
> \text{Step 2: } & (u, v) \mapsto (x, v) \quad \text{via} \quad x = \phi(u, v), \; v = v \\
> \text{Step 1: } & (x, v) \mapsto (x, y) \quad \text{via} \quad x = x, \; y = \psi(U(x, v), v)
> \end{aligned}
> $$
>
> where $U(x, v)$ is the inverse of $u \mapsto \phi(u, v)$ for fixed $v$ (exists by [[Multivariable Analysis §12 The Implicit Function Theorem#^thm-12-2|IFT]] since $\phi_u \neq 0$).
>
> **Case 2:** If $\phi_v \neq 0$, we can interchange $u$ and $v$ and proceed similarly.
>
> In either case, the region $R$ can be covered by finitely many subregions where the decomposition works, and the integral over $R$ is the sum of integrals over these subregions ([[Multivariable Analysis §15 Multivariable Integration#^thm-15-4|additivity over domains]]). $\square$ (claim)
>
> **Primitive Transformation Formula.**
>
> We prove the change of variables formula for primitive transformations using the 1D result ([[Multivariable Analysis §15 Multivariable Integration#^lem-15-13|Lemma §15.13]]).
>
> Consider a Type I primitive: $(x, v) \mapsto (x, y)$ with $y = \Phi(v, x)$ and $\Phi_v > 0$.
>
> For fixed $x$, the map $v \mapsto y = \Phi(v, x)$ is a 1D change of variables with derivative $\Phi_v$.
>
> By [[Multivariable Analysis §15 Multivariable Integration#^lem-15-13|Lemma §15.13]]:
>
> $$
> \int_{y_1}^{y_2} f(x, y) \, dy = \int_{v_1}^{v_2} f(x, \Phi(v, x)) \cdot \Phi_v(v, x) \, dv.
> $$
>
> Integrating over $x$ and using [[Multivariable Analysis §15 Multivariable Integration#^thm-15-9|Fubini]]:
>
> $$
> \iint_R f(x, y) \, dx \, dy = \iint_B f(x, \Phi(v, x)) \cdot \Phi_v(v, x) \, dx \, dv.
> $$
>
> The Jacobian of the Type I primitive is:
>
> $$
> \frac{\partial(x, y)}{\partial(x, v)} = \det \begin{pmatrix} 1 & 0 \\ \Phi_x & \Phi_v \end{pmatrix} = \Phi_v.
> $$
>
> Similarly, for a Type II primitive $(u, v) \mapsto (x, v)$ with $x = \Psi(u, v)$ and $\Psi_u > 0$:
>
> $$
> \iint_B g(x, v) \, dx \, dv = \iint_{R'} g(\Psi(u, v), v) \cdot \Psi_u(u, v) \, du \, dv.
> $$
>
> The Jacobian is:
>
> $$
> \frac{\partial(x, v)}{\partial(u, v)} = \det \begin{pmatrix} \Psi_u & \Psi_v \\ 0 & 1 \end{pmatrix} = \Psi_u.
> $$
>
> **Combining the Two Steps.**
>
> Composing the two primitive transformations $(u, v) \xrightarrow{\text{II}} (x, v) \xrightarrow{\text{I}} (x, y)$:
>
> *Step 1 (Type II):*
>
> $$
> \iint_B f(x, \Phi(v, x)) \cdot \Phi_v \, dx \, dv = \iint_{R'} f(\Psi, \Phi(v, \Psi)) \cdot \Phi_v(v, \Psi) \cdot \Psi_u \, du \, dv.
> $$
>
> Note that $y = \Phi(v, \Psi(u, v)) = \psi(u, v)$ by construction.
>
> *Step 2* ([[Multivariable Analysis §10 Composition of Functions and the Chain Rule#^rem-10-4|Chain Rule for Jacobians]]):
>
> $$
> \frac{\partial(x, y)}{\partial(u, v)} = \frac{\partial(x, y)}{\partial(x, v)} \cdot \frac{\partial(x, v)}{\partial(u, v)} = \Phi_v \cdot \Psi_u.
> $$
>
> **Conclusion.**
>
> Combining everything:
>
> $$
> \iint_R f(x, y) \, dx \, dy = \iint_{R'} f(\phi(u, v), \psi(u, v)) \cdot \Phi_v \cdot \Psi_u \, du \, dv = \iint_{R'} f(\phi, \psi) \left| \frac{\partial(x, y)}{\partial(u, v)} \right| du \, dv.
> $$
>
> (The absolute value appears because if $\Phi_v < 0$ or $\Psi_u < 0$, the orientation reverses, but the area element remains positive.)

^pf-15-14-3

*Uses:* [[Multivariable Analysis §15 Multivariable Integration#^lem-15-13|§15.13]], [[Multivariable Analysis §12 The Implicit Function Theorem#^thm-12-2|§12.2]], [[Multivariable Analysis §15 Multivariable Integration#^thm-15-4|§15.4]], [[Multivariable Analysis §15 Multivariable Integration#^thm-15-9|§15.9]], [[Multivariable Analysis §10 Composition of Functions and the Chain Rule#^rem-10-4|§10 Rem. (Chain Rule for Jacobians)]], [[Linear Algebra 9C Determinants#^ladr-9-49|LADR 9.49]]

> [!remark]- Connections
> - The linear case (Part I of the first proof) is [[Linear Algebra 9C Determinants#^ladr-9-61|LADR 9.61]]: $T$ changes volume by the factor $|\det T|$; the $C^1$ case is this applied to the derivative cell by cell.
> - Generalizes the 1D substitution rule ([[Multivariable Analysis §15 Multivariable Integration#^lem-15-13|Lemma §15.13]]) and the [[Multivariable Analysis §15 Multivariable Integration#^thm-15-7|polar formula]]; extended to Jordan measurable domains in [[Change of Variables Formula (multiple integrals)|Theorem §15.17]] and to $\mathbb{R}^n$ in [[Multivariable Analysis §15 Multivariable Integration#^thm-15-20|Theorem §15.20]].
> - In forms language the integrand $f\,|J|\,du\,dv$ is the pullback $\Phi^*(f\,dx \wedge dy)$ (up to orientation): [[Multivariable Analysis §22 The Algebra of Differential Forms#^ex-22-4|Ex. §22.4]].

> [!remark] Remark: $|J|$ vs. $J$: Orientation and Area
> The change of variables formula uses $|J|$, not $J$. This distinction matters:
> - $|J|$ measures **area distortion**: how much the transformation stretches or compresses infinitesimal areas. This is always nonnegative and is the correct factor for computing integrals.
> - $J$ (with sign) measures **oriented area distortion**: $J > 0$ means the transformation preserves orientation, $J < 0$ means it reverses orientation (like a reflection).
>
> A common exam mistake is writing $J$ instead of $|J|$ in the formula. If you know $J > 0$ on your domain (e.g., polar coordinates with $J = r > 0$ for $r > 0$), then $|J| = J$ and the distinction is harmless. But if orientation could reverse (e.g., a transformation involving a reflection), omitting the absolute value gives the wrong answer.
>
> The signed Jacobian becomes important later when we study **differential forms** ([[Multivariable Analysis §21 Introduction to Differential Forms|§21]]) and **oriented integrals** ([[Multivariable Analysis §22 The Algebra of Differential Forms#^def-22-6|Def. §22.6]]), where the orientation of the domain carries geometric meaning.

^rem-15-14

> [!remark]- Connections
> - The linear-algebra picture: [[Linear Algebra 9C Determinants#^ladr-9-61|LADR 9.61]] (volume scales by $|\det T|$) and its orientation remark; $\det$ as signed volume.

### Extension to General Domains

The proofs above assume $D^*$ is a rectangle. We now extend to arbitrary Jordan measurable domains.

> [!theorem] Proposition §15.15: Boundary Squares Have Vanishing Total Area
> Let $D \subseteq \mathbb{R}^2$ be a bounded Jordan measurable set. Enclose $D$ in a rectangle $R$ and partition $R$ into $N^2$ squares of side $1/N$. Let $B_N$ denote the set of **boundary squares** (those that intersect $\partial D$).
>
> Then:
>
> $$
> \lim_{N \to \infty} \#(B_N) \cdot \frac{1}{N^2} = 0.
> $$

^prop-15-15

> [!proof]+ Proof
> Since $D$ is [[Multivariable Analysis §15 Multivariable Integration#^def-15-14|Jordan measurable]], $\partial D$ has [[Multivariable Analysis §15 Multivariable Integration#^def-15-13|Jordan measure zero]]. Thus for any $\varepsilon > 0$, there exist finitely many rectangles $R_1, \ldots, R_K$ with:
>
> $$
> \partial D \subseteq \bigcup_{k=1}^K R_k \quad \text{and} \quad \sum_{k=1}^K \text{Area}(R_k) < \varepsilon.
> $$
>
> A boundary square $S$ satisfies $S \cap \partial D \neq \emptyset$, so $S$ must intersect at least one $R_k$.
>
> For $N$ large enough (specifically, $1/N$ smaller than the minimum side length of the $R_k$'s), each $R_k$ can intersect at most $C \cdot N^2 \cdot \text{Area}(R_k)$ squares of side $1/N$, where $C$ is a universal constant.
>
> Therefore:
>
> $$
> \#(B_N) \leq C \cdot N^2 \cdot \sum_{k=1}^K \text{Area}(R_k) < C \cdot N^2 \cdot \varepsilon.
> $$
>
> Hence:
>
> $$
> \#(B_N) \cdot \frac{1}{N^2} < C \cdot \varepsilon.
> $$
>
> Since $\varepsilon > 0$ was arbitrary, the limit is zero.

^pf-15-15

*Uses:* [[Multivariable Analysis §15 Multivariable Integration#^def-15-13|Def. §15.13]], [[Multivariable Analysis §15 Multivariable Integration#^def-15-14|Def. §15.14]]

> [!theorem] Proposition §15.16: $C^1$ Diffeomorphisms Preserve Jordan Measurability
> Let $D^* \subseteq \mathbb{R}^2$ be bounded and Jordan measurable. Let $\Phi: \overline{D^*} \to \mathbb{R}^2$ be a $C^1$ map. Then $\Phi(\partial D^*)$ has Jordan measure zero.
>
> In particular, if $\Phi$ is a $C^1$ diffeomorphism onto $D = \Phi(D^*)$, then $D$ is Jordan measurable.

^prop-15-16

> [!proof]+ Proof
> Since $\Phi$ is $C^1$ on the compact set $\overline{D^*}$ ([[Heine–Borel Theorem|Heine–Borel]]), it is Lipschitz ([[Mean Value Theorem in Several Variables|mean value theorem]]): there exists $L > 0$ such that
>
> $$
> \|\Phi(p) - \Phi(q)\| \leq L \|p - q\| \quad \text{for all } p, q \in \overline{D^*}.
> $$
>
> Let $\varepsilon > 0$. Since $\partial D^*$ has Jordan measure zero, there exist rectangles $R_1, \ldots, R_K$ with:
>
> $$
> \partial D^* \subseteq \bigcup_{k=1}^K R_k \quad \text{and} \quad \sum_{k=1}^K \text{Area}(R_k) < \frac{\varepsilon}{L^2}.
> $$
>
> For each rectangle $R_k$ with side lengths $a_k \times b_k$, the image $\Phi(R_k \cap \overline{D^*})$ is contained in a rectangle of side lengths at most $L \cdot a_k \times L \cdot b_k$ (since $\Phi$ stretches distances by at most $L$).
>
> Therefore:
>
> $$
> \Phi(\partial D^*) \subseteq \bigcup_{k=1}^K \Phi(R_k \cap \overline{D^*}) \subseteq \bigcup_{k=1}^K \tilde{R}_k
> $$
>
> where $\text{Area}(\tilde{R}_k) \leq L^2 \cdot \text{Area}(R_k)$.
>
> Hence:
>
> $$
> \sum_{k=1}^K \text{Area}(\tilde{R}_k) \leq L^2 \sum_{k=1}^K \text{Area}(R_k) < L^2 \cdot \frac{\varepsilon}{L^2} = \varepsilon.
> $$
>
> Since $\partial D = \Phi(\partial D^*)$ (for a bijection), this shows $\partial D$ has Jordan measure zero, so $D$ is Jordan measurable.

^pf-15-16

*Uses:* [[Heine–Borel Theorem|590 §15.12]], [[Mean Value Theorem in Several Variables|§9.4]], [[Multivariable Analysis §15 Multivariable Integration#^def-15-13|Def. §15.13]], [[Multivariable Analysis §15 Multivariable Integration#^def-15-14|Def. §15.14]]

> [!theorem] Theorem §15.17: Change of Variables — General Jordan Measurable Domains
> Let $D^* \subseteq \mathbb{R}^2$ be bounded and Jordan measurable. Let $\Phi: \overline{D^*} \to \overline{D}$ be a $C^1$ bijection with $C^1$ inverse, where $D = \Phi(D^*)$.
>
> Write $\Phi(u, v) = (\varphi(u, v), \psi(u, v)) = (x, y)$, and assume $J = \varphi_u \psi_v - \varphi_v \psi_u \neq 0$ on $D^*$.
>
> If $f$ is continuous on $\overline{D}$, then:
>
> $$
> \boxed{\iint_D f(x, y) \, dx \, dy = \iint_{D^*} f(\varphi(u, v), \psi(u, v)) \cdot |J(u, v)| \, du \, dv}
> $$

^thm-15-17

> [!proof]+ Proof
> Enclose $D^*$ in a rectangle $R^* = [a, b] \times [c, d]$. Partition $R^*$ into squares of side $\Delta = 1/2^m$. Classify each square $S_{ij}$ as:
> - **Interior:** $S_{ij} \subseteq D^*$
> - **Exterior:** $S_{ij} \cap D^* = \emptyset$
> - **Boundary:** $S_{ij} \cap \partial D^* \neq \emptyset$ and $S_{ij} \cap D^* \neq \emptyset$
>
> Define the inner and outer Riemann sums:
>
> $$
> \begin{aligned}
> S_m^{\text{inner}} &= \sum_{\text{interior } S_{ij}} f(\varphi(u_{ij}), \psi(u_{ij})) \cdot |J(u_{ij})| \cdot \Delta^2, \\
> S_m^{\text{outer}} &= \sum_{\text{interior or boundary } S_{ij}} f(\varphi(u_{ij}), \psi(u_{ij})) \cdot |J(u_{ij})| \cdot \Delta^2.
> \end{aligned}
> $$
>
> Since $f \circ \Phi$ and $|J|$ are continuous on $\overline{D^*}$, they are bounded ([[Continuous Image of a Compact Space is Compact|continuous image of compact is compact]]): $|f \circ \Phi| \leq M_f$ and $|J| \leq M_J$.
>
> The difference between outer and inner sums is:
>
> $$
> |S_m^{\text{outer}} - S_m^{\text{inner}}| \leq M_f \cdot M_J \cdot \#(\text{boundary squares}) \cdot \Delta^2.
> $$
>
> By [[Multivariable Analysis §15 Multivariable Integration#^prop-15-15|Proposition §15.15]], this tends to zero as $m \to \infty$.
>
> For interior squares, the proof of [[Multivariable Analysis §15 Multivariable Integration#^thm-15-14|Theorem §15.14]] applies verbatim: each interior square maps to a curvilinear region with area $|J| \cdot \Delta^2 + O(\varepsilon \cdot \Delta^2)$.
>
> Therefore, both $S_m^{\text{inner}}$ and $S_m^{\text{outer}}$ converge to the same limit:
>
> $$
> \lim_{m \to \infty} S_m^{\text{inner}} = \lim_{m \to \infty} S_m^{\text{outer}} = \iint_{D^*} f(\varphi, \psi) \cdot |J| \, du \, dv.
> $$
>
> On the other side, the same argument for the images (using that $D$ is Jordan measurable by [[Multivariable Analysis §15 Multivariable Integration#^prop-15-16|Proposition §15.16]]) shows:
>
> $$
> \iint_D f(x, y) \, dx \, dy = \lim_{m \to \infty} \sum_{\text{interior } \Sigma_{ij}} f(x_{ij}, y_{ij}) \cdot \text{Area}(\Sigma_{ij})
> $$
>
> where $\Sigma_{ij} = \Phi(S_{ij})$.
>
> Since $\text{Area}(\Sigma_{ij}) = |J(u_{ij})| \cdot \Delta^2 + O(\varepsilon \cdot \Delta^2)$ by the error analysis in [[Multivariable Analysis §15 Multivariable Integration#^thm-15-14|Theorem §15.14]], the two limits are equal.

^pf-15-17

*Uses:* [[Continuous Image of a Compact Space is Compact|590 §15.3]], [[Multivariable Analysis §15 Multivariable Integration#^prop-15-15|§15.15]], [[Multivariable Analysis §15 Multivariable Integration#^prop-15-16|§15.16]], [[Multivariable Analysis §15 Multivariable Integration#^thm-15-14|§15.14]], [[Multivariable Analysis §15 Multivariable Integration#^def-15-11|Def. §15.11]]

> [!remark]- Connections
> - The $n$-dimensional version is [[Multivariable Analysis §15 Multivariable Integration#^thm-15-20|Theorem §15.20]]; in forms language it becomes $\int_{\Phi(D^*)} \omega = \int_{D^*} \Phi^*\omega$ for orientation-preserving $\Phi$ ([[Multivariable Analysis §22 The Algebra of Differential Forms#^def-22-3|pullback, Def. §22.3]]).
> - Used to parametrize surfaces and compute surface area: [[Surface Area via the Gram Matrix|Theorem §18.1]].

> [!theorem] Proposition §15.18: Isolated Zeros of the Jacobian
> The change of variables formula remains valid if $J = 0$ at finitely many isolated points $p_1, \ldots, p_n \in D^*$, provided $J$ does not change sign on $D^*$.

^prop-15-18

> [!proof]+ Proof
> For $\varepsilon > 0$, define $D^*_\varepsilon = D^* \setminus \bigcup_{k=1}^n B_\varepsilon(p_k)$ ([[Multivariable Analysis §2 Open and Closed Sets#^def-2-1|Def. §2.1]]).
>
> On $D^*_\varepsilon$, we have $J \neq 0$, so [[Change of Variables Formula (multiple integrals)|Theorem §15.17]] applies:
>
> $$
> \iint_{\Phi(D^*_\varepsilon)} f \, dx \, dy = \iint_{D^*_\varepsilon} f(\varphi, \psi) \cdot |J| \, du \, dv.
> $$
>
> As $\varepsilon \to 0$:
> - The left side converges to $\iint_D f \, dx \, dy$ since we remove sets of measure $O(\varepsilon^2)$.
> - The right side converges to $\iint_{D^*} f(\varphi, \psi) \cdot |J| \, du \, dv$ for the same reason.
>
> This is particularly important for polar coordinates, where $J = r$ vanishes at $r = 0$.

^pf-15-18

*Uses:* [[Multivariable Analysis §2 Open and Closed Sets#^def-2-1|Def. §2.1]], [[Change of Variables Formula (multiple integrals)|§15.17]], [[Multivariable Analysis §15 Multivariable Integration#^thm-15-4|§15.4]]

### Geometric Interpretation and Higher Dimensions

> [!theorem] Proposition §15.19: Determinants Measure Volume Distortion
> Let $T: \mathbb{R}^n \to \mathbb{R}^n$ be a linear map represented by matrix $A$. Then for any measurable set $E \subseteq \mathbb{R}^n$:
>
> $$
> \text{Vol}_n(T(E)) = |\det(A)| \cdot \text{Vol}_n(E).
> $$
>
> In particular, a unit $n$-cube maps to a parallelepiped of volume $|\det(A)|$.

^prop-15-19

> [!remark]- Connections
> - This is [[Linear Algebra 9C Determinants#^ladr-9-61|LADR 9.61]] ($T$ changes volume by factor of $|\det T|$), proved there via polar decomposition and singular values ([[Linear Algebra 9C Determinants#^ladr-9-60|LADR 9.60]]); the matrix and operator determinants agree by [[Linear Algebra 9C Determinants#^ladr-9-53|LADR 9.53]].
> - For $n = 2$ this is Part I of the first proof of [[Multivariable Analysis §15 Multivariable Integration#^thm-15-14|Theorem §15.14]].

This proposition explains why the Jacobian determinant appears in the change of variables formula: locally, the transformation $\Phi$ is approximated by its linearization $J_\Phi$ ([[Multivariable Analysis §6 Differentiability#^def-6-2|Def. §6.2]]), and $|\det(J_\Phi)| = |J|$ measures the local volume distortion.

> [!theorem] Theorem §15.20: Change of Variables in $\mathbb{R}^n$
> Let $D^* \subseteq \mathbb{R}^n$ be bounded and Jordan measurable. Let $\Phi: \overline{D^*} \to \overline{D}$ be a $C^1$ diffeomorphism with Jacobian matrix
>
> $$
> J_\Phi = \frac{\partial(x_1, \ldots, x_n)}{\partial(u_1, \ldots, u_n)} = \begin{pmatrix} \frac{\partial x_1}{\partial u_1} & \cdots & \frac{\partial x_1}{\partial u_n} \\ \vdots & \ddots & \vdots \\ \frac{\partial x_n}{\partial u_1} & \cdots & \frac{\partial x_n}{\partial u_n} \end{pmatrix}.
> $$
>
> If $\det(J_\Phi) \neq 0$ on $D^*$ and $f$ is continuous on $\overline{D}$, then:
>
> $$
> \int_D f(\mathbf{x}) \, d\mathbf{x} = \int_{D^*} f(\Phi(\mathbf{u})) \cdot |\det(J_\Phi(\mathbf{u}))| \, d\mathbf{u}.
> $$

^thm-15-20

The proof follows the same structure as the 2D case ([[Multivariable Analysis §15 Multivariable Integration#^pf-15-14-3|Proof 3]] generalizes most directly: decompose into $n$ primitive transformations).

> [!remark]- Connections
> - Linear-algebra core: [[Linear Algebra 9C Determinants#^ladr-9-61|LADR 9.61]] for the local volume factor and [[Linear Algebra 9C Determinants#^ladr-9-49|LADR 9.49]] (det is multiplicative) for composing primitive transformations.
> - In $\mathbb{R}^3$: the spherical volume element used in [[Multivariable Analysis §19 The Laplacian in Spherical Coordinates|§19]]; for general dimension it underlies the [[Divergence Theorem in ℝⁿ|Divergence Theorem in ℝⁿ]] and, as pullback of $n$-forms, the [[Generalized Stokes' Theorem|Generalized Stokes' Theorem]].

### Common Coordinate Systems and Worked Examples

> [!example] Example §15.4: Polar Coordinates
> The transformation $x = r\cos\theta$, $y = r\sin\theta$ maps $(r, \theta) \in [0, \infty) \times [0, 2\pi)$ to $(x, y) \in \mathbb{R}^2$.
>
> The Jacobian is:
>
> $$
> J = \det \begin{pmatrix} \cos\theta & -r\sin\theta \\ \sin\theta & r\cos\theta \end{pmatrix} = r\cos^2\theta + r\sin^2\theta = r.
> $$
>
> Therefore: $dx \, dy = r \, dr \, d\theta$.
>
> Note: $J = r = 0$ at the origin, but by [[Multivariable Analysis §15 Multivariable Integration#^prop-15-18|Proposition §15.18]], the formula still applies.

^ex-15-4

> [!remark]- Connections
> - Same Jacobian as [[Multivariable Analysis §13 The Inverse Function Theorem#^ex-13-4|Ex. §13.4]]; derived from scratch by polar rectangles in [[Multivariable Analysis §15 Multivariable Integration#^thm-15-7|Theorem §15.7]].

> [!example] Example §15.5: Elliptical Coordinates
> For an ellipse with semi-axes $a$ and $b$: $x = ar\cos\theta$, $y = br\sin\theta$.
>
> The Jacobian is:
>
> $$
> J = \det \begin{pmatrix} a\cos\theta & -ar\sin\theta \\ b\sin\theta & br\cos\theta \end{pmatrix} = abr\cos^2\theta + abr\sin^2\theta = abr.
> $$
>
> Therefore: $dx \, dy = abr \, dr \, d\theta$.
>
> This is useful for integrating over elliptical regions.

^ex-15-5

> [!example] Example §15.6: Spherical Coordinates in $\mathbb{R}^3$
> The transformation $x = \rho\sin\phi\cos\theta$, $y = \rho\sin\phi\sin\theta$, $z = \rho\cos\phi$ has Jacobian:
>
> $$
> J = \rho^2 \sin\phi.
> $$
>
> Therefore: $dx \, dy \, dz = \rho^2 \sin\phi \, d\rho \, d\phi \, d\theta$.

^ex-15-6

> [!remark]- Connections
> - The same coordinates parametrize the sphere in [[Multivariable Analysis §18 Surface Integrals#^ex-18-1|Ex. §18.1]] and give the Laplacian in [[Multivariable Analysis §19 The Laplacian in Spherical Coordinates#^thm-19-1|Theorem §19.1]].

We now demonstrate the change of variables formula with two complete computations.

> [!example] Example §15.7: The Gaussian Integral via Polar Coordinates
> **Goal:** Compute $I = \displaystyle\int_{-\infty}^{\infty} e^{-x^2} \, dx$ ([[Single Variable Analysis §36 Improper Integrals#^def-36-2|improper integral]]).
>
> *The trick:* We cannot evaluate $I$ directly (no elementary antiderivative for $e^{-x^2}$), but we *can* evaluate $I^2$.
>
> **Step 1: Square the integral.**
>
> $$
> I^2 = \left( \int_{-\infty}^{\infty} e^{-x^2} \, dx \right)\left( \int_{-\infty}^{\infty} e^{-y^2} \, dy \right) = \iint_{\mathbb{R}^2} e^{-(x^2 + y^2)} \, dx \, dy.
> $$
>
> The second equality uses [[Multivariable Analysis §15 Multivariable Integration#^thm-15-12|Fubini's theorem]] to combine the product of two single integrals into a double integral.
>
> **Step 2: Change to polar coordinates.**
>
> Apply $x = r\cos\theta$, $y = r\sin\theta$ with $J = r$, so $dx \, dy = r \, dr \, d\theta$ ([[Multivariable Analysis §15 Multivariable Integration#^ex-15-4|Ex. §15.4]]). Also, $x^2 + y^2 = r^2$.
>
> The domain $\mathbb{R}^2$ corresponds to $r \in [0, \infty)$, $\theta \in [0, 2\pi)$:
>
> $$
> I^2 = \int_0^{2\pi} \int_0^{\infty} e^{-r^2} \cdot r \, dr \, d\theta.
> $$
>
> **Step 3: Evaluate the inner integral.**
>
> The substitution $u = r^2$, $du = 2r \, dr$ ([[Multivariable Analysis §15 Multivariable Integration#^lem-15-13|Lemma §15.13]]) gives:
>
> $$
> \int_0^{\infty} e^{-r^2} \cdot r \, dr = \frac{1}{2} \int_0^{\infty} e^{-u} \, du = \frac{1}{2} \left[ -e^{-u} \right]_0^{\infty} = \frac{1}{2}.
> $$
>
> **Step 4: Evaluate the outer integral.**
>
> $$
> I^2 = \int_0^{2\pi} \frac{1}{2} \, d\theta = \pi.
> $$
>
> **Conclusion:** Since $I > 0$ (the integrand is positive), we obtain:
>
> $$
> \boxed{\int_{-\infty}^{\infty} e^{-x^2} \, dx = \sqrt{\pi}}
> $$
>
> This result is fundamental in probability theory (the normalization constant of the Gaussian distribution) and in physics (partition functions, path integrals).

^ex-15-7

> [!remark]- Connections
> - Pays off the debt taken “on credit” in MATH 451: [[Single Variable Analysis §36 Improper Integrals#^ex-36-4|The normal distribution]] (451 Ex. §36.4).

> [!example] Example §15.8: Area of an Ellipse
> **Goal:** Compute the area of the ellipse $D = \left\{ (x,y) : \dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} \leq 1 \right\}$.
>
> **Step 1: Choose the coordinate transformation.**
>
> Use elliptical coordinates ([[Multivariable Analysis §15 Multivariable Integration#^ex-15-5|Ex. §15.5]]): $x = ar\cos\theta$, $y = br\sin\theta$. The Jacobian is $J = abr$.
>
> The ellipse $D$ corresponds to $D^* = \{(r, \theta) : 0 \leq r \leq 1, \, 0 \leq \theta < 2\pi\}$.
>
> **Verification:** Under this map, $\dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} = r^2\cos^2\theta + r^2\sin^2\theta = r^2 \leq 1$. ✓
>
> **Step 2: Apply the [[Change of Variables Formula (multiple integrals)|change of variables formula]].**
>
> $$
> \text{Area}(D) = \iint_D 1 \, dx \, dy = \iint_{D^*} 1 \cdot |J| \, dr \, d\theta = \int_0^{2\pi} \int_0^1 abr \, dr \, d\theta.
> $$
>
> **Step 3: Evaluate.**
>
> $$
> \int_0^{2\pi} \int_0^1 abr \, dr \, d\theta = ab \int_0^{2\pi} \left[ \frac{r^2}{2} \right]_0^1 d\theta = ab \int_0^{2\pi} \frac{1}{2} \, d\theta = \frac{ab}{2} \cdot 2\pi = \pi ab.
> $$
>
> **Conclusion:**
>
> $$
> \boxed{\text{Area of the ellipse } \frac{x^2}{a^2} + \frac{y^2}{b^2} \leq 1 \text{ is } \pi ab}
> $$
>
> **Sanity check:** When $a = b = R$, this gives $\pi R^2$, the area of a circle of radius $R$. ✓

^ex-15-8
