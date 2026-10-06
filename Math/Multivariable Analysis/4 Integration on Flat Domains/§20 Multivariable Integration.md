---
type: section
subject: "[[Multivariable Analysis]]"
chapter: 4
section: 20
tags: [multivariable-analysis, math452]
---
← [[§19 The Unit Circle and Polar Coordinates]] · ↑ [[· 4 Integration on Flat Domains]] · [[§21 The Definition of the Integral]] →

## Part II: Integral Calculus and Vector Calculus

*Chapter 4: Integration on Flat Domains.*

**Contents:** [[#Motivation: Integration over General Domains|motivation]] · [[#Jordan Measure: Inner and Outer Approximations|Jordan measure]] · [[§21 The Definition of the Integral#Definition of the Integral|the integral]] · [[§22 Properties of the Integral#Properties of the Integral|properties]] (incl. polar coordinates, [[§22 Properties of the Integral#^thm-22-6|§22.6]]) · [[§23 Fubini's Theorem#Fubini's Theorem: Rigorous Treatment|Fubini]] ([[§23 Fubini's Theorem#^thm-23-1|§23.1]]–[[§23 Fubini's Theorem#^thm-23-5|§23.5]]) · [[§24 The Change of Variables Formula#General Change of Variables|change of variables]]: [[§24 The Change of Variables Formula#Preliminaries|preliminaries]], [[§24 The Change of Variables Formula#Main Theorem (Rectangular Domain)|rectangular case]] with three proofs ([[§24 The Change of Variables Formula#^thm-24-2|§24.2]]), [[§25 Change of Variables on General Domains#Extension to General Domains|general domains]] ([[§25 Change of Variables on General Domains#^prop-25-1|§25.1]]–[[§25 Change of Variables on General Domains#^prop-25-4|§25.4]]), [[§25 Change of Variables on General Domains#Geometric Interpretation and Higher Dimensions|ℝⁿ]] ([[§25 Change of Variables on General Domains#^prop-25-5|§25.5]]–[[§25 Change of Variables on General Domains#^thm-25-6|§25.6]]), [[§25 Change of Variables on General Domains#Common Coordinate Systems and Worked Examples|worked examples]].

## Motivation: Integration over General Domains

In single-variable calculus, we integrate over intervals $[a, b]$ ([[§32 The Definition of the Riemann Integral|451 §32]]). In multivariable calculus, we want to integrate over more complicated domains $D \subseteq \mathbb{R}^2$ (or $\mathbb{R}^n$).

**Problem:** How do we define the “area” of a general set $D$?

**Approach:** Jordan measure — approximate $D$ using squares (or rectangles) that we “trust.”

> [!remark] Remark
> This construction can be generalized to Lebesgue measure, which is more powerful but beyond the scope of this course.

^rem-20-1

## Squares and Rectangles

> [!definition] Definition §20.1: Square
> A **square** (or rectangle) in $\mathbb{R}^2$ with corners $(x, y)$ and $(x + a, y + a)$ is:
>
> $$
> S = [x, x + a] \times [y, y + a].
> $$
>
> We **manually define** its area: $\text{Area}(S) = a^2$.

^def-20-1

> [!definition] Definition §20.2: Rectangle
> More generally, a rectangle $R = [x_1, x_2] \times [y_1, y_2]$ has area $(x_2 - x_1)(y_2 - y_1)$.

^def-20-2

## Jordan Measure: Inner and Outer Approximations

**Goal:** Define the area of any set $D \subseteq \mathbb{R}^2$.

**Step 0: Draw a mesh.**

Consider a grid with mesh points at $\mathbb{Z} \times \mathbb{Z}$ (integer lattice). Each unit square has area 1. This is the “0-th approximation.”

> [!definition] Definition §20.3: 0-th Approximation
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

^def-20-3

**Key observation:** $A_0^-(D) \leq \text{“true area”} \leq A_0^+(D)$.

### Refining the Mesh

**$i$-th subdivision:** Divide each side by $2^i$, so each square has side length $\dfrac{1}{2^i}$ and area $\dfrac{1}{2^{2i}} = \dfrac{1}{4^i}$.

> [!definition] Definition §20.4: $i$-th Approximation
> - $\mathcal{S}_i^+ = \{ S : S \cap D \neq \emptyset \}$ = squares (of side $1/2^i$) intersecting $D$.
> - $\mathcal{S}_i^- = \{ S : S \subseteq D \}$ = squares (of side $1/2^i$) entirely in $D$.
>
> $$
> \begin{aligned}
> A_i^+(D) &= \#(\mathcal{S}_i^+) \cdot \left( \frac{1}{2^i} \right)^2 \\
> A_i^-(D) &= \#(\mathcal{S}_i^-) \cdot \left( \frac{1}{2^i} \right)^2
> \end{aligned}
> $$

^def-20-4

**Properties:**
- $A_i^-(D) \leq A_{i+1}^-(D)$ (inner approximations increase as mesh refines)
- $A_i^+(D) \geq A_{i+1}^+(D)$ (outer approximations decrease as mesh refines)
- $A_i^-(D) \leq A_i^+(D)$ for all $i$

### Jordan Content

> [!definition] Definition §20.5: Inner Jordan Content
> $$
> \begin{aligned}
> \underline{A}(D) &= \lim_{i \to \infty} A_i^-(D) = \sup_i A_i^-(D) \quad \text{(inner Jordan content)}
> \end{aligned}
> $$

^def-20-5

> [!definition] Definition §20.6: Outer Jordan Content
> $$
> \begin{aligned}
> \overline{A}(D) &= \lim_{i \to \infty} A_i^+(D) = \inf_i A_i^+(D) \quad \text{(outer Jordan content)}
> \end{aligned}
> $$

^def-20-6

> [!remark]- Connections
> - The limits exist because the sequences are monotone and bounded: [[Monotone Convergence Theorem]] (451).
> - The same inner/outer squeeze as the 1D [[§32 The Definition of the Riemann Integral#^def-32-4|Darboux lower and upper integrals]].
> - Lebesgue outer measure replaces the finite grids of squares by countable coverings with rectangles: [[§10 Lebesgue Outer Measure#^def-10-4|551 Def. §10.4]]; finite unions of rectangles still approximate every measurable set of finite measure, [[§13 Approximation and Continuity of Measure#^thm-13-6|551 Thm. §13.6]].

> [!definition] Definition §20.7: Jordan Measurable
> A set $D$ is **Jordan measurable** if $\underline{A}(D) = \overline{A}(D)$.
>
> In this case, the common value is the **Jordan content** (or **Jordan measure** or **area**) of $D$:
>
> $$
> \text{Area}(D) = \underline{A}(D) = \overline{A}(D).
> $$

^def-20-7

![[m452-15-3.svg]]
*Inner and outer approximations of an ellipse $D$ with semi-axes $1.75$ and $1.3$. Blue squares lie inside $D$. Red and blue squares together are the squares that meet $D$. With side $1$ ($i = 0$) this gives $A_0^-(D) = 2$ and $A_0^+(D) = 12$. Halving the side ($i = 1$) gives $A_1^-(D) = 5$ and $A_1^+(D) = 11$, a tighter bracket around the true area $\pi \cdot 1.75 \cdot 1.3 \approx 7.15$. The gap $A_i^+ - A_i^-$ is exactly the red squares, and every red square straddles $\partial D$. So the two limits agree precisely when the boundary squares have total area $\to 0$ (the Remark below).*

> [!remark] Remark
> The difference $A_i^+(D) - A_i^-(D)$ counts squares that straddle the boundary $\partial D$ ([[§2 Open and Closed Sets#^def-2-5|Def. §2.5]]). As $i \to \infty$, these boundary squares have total area $\to 0$ if and only if $\partial D$ has “measure zero.”
>
> A set $D$ is Jordan measurable $\iff$ its boundary $\partial D$ has Jordan content zero ([[§24 The Change of Variables Formula#^def-24-1|Def. §24.1]]).

^rem-20-2

> [!remark]- Connections
> - Lebesgue measurability ([[§11 Lebesgue Measurable Sets#^def-11-1|551 Def. §11.1]]) admits more sets: every Jordan measurable set is Lebesgue measurable with the same measure, while $\mathbb{Q} \cap [0,1]$ is not Jordan measurable but is a Lebesgue null set ([[§10 Lebesgue Outer Measure#^ex-10-2|551 Ex. §10.2]]).

### Almost Disjoint Sets

> [!definition] Definition §20.8: Almost Disjoint
> Two sets $D, E \subseteq \mathbb{R}^2$ are **almost disjoint** if their interiors ([[§2 Open and Closed Sets#^def-2-3|Def. §2.3]]) do not intersect:
>
> $$
> \text{int}(D) \cap \text{int}(E) = \emptyset.
> $$
>
> Equivalently, they can only overlap on their boundaries.

^def-20-8

> [!remark] Remark
> Almost disjoint sets can share boundary points, but not interior points. For example, two adjacent squares sharing an edge are almost disjoint.

^rem-20-3

### Additivity of Jordan Measure

> [!theorem] Theorem §20.1: Additivity
> If $D$ and $E$ are both Jordan measurable and almost disjoint, then $D \cup E$ is Jordan measurable and:
>
> $$
> |D \cup E| = |D| + |E|.
> $$

^thm-20-1

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
> The center $\mathbf{x}$ of $S$ is an interior point of $S$, hence of both $D$ and $E$ (since $S \subseteq D$ and $S \subseteq E$). But this contradicts $\text{int}(D) \cap \text{int}(E) = \emptyset$.
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

^pf-20-1

*Uses:* [[§20 Multivariable Integration#^def-20-4|Def. §20.4]], [[§20 Multivariable Integration#^def-20-5|Def. §20.5]], [[§20 Multivariable Integration#^def-20-6|Def. §20.6]], [[§20 Multivariable Integration#^def-20-7|Def. §20.7]], [[§20 Multivariable Integration#^def-20-8|Def. §20.8]], [[§2 Open and Closed Sets#^def-2-3|Def. §2.3]]

> [!remark]- Connections
> - For Lebesgue measure: additivity over disjoint measurable sets, [[§11 Lebesgue Measurable Sets#^lem-11-2|551 Lemma §11.2]], upgraded to countable additivity in [[§11 Lebesgue Measurable Sets#^thm-11-3|551 Thm. §11.3]].

*Continued in [[§21 The Definition of the Integral]]: partitions, upper and lower sums, mesh, and the integral over a Jordan measurable set.*
