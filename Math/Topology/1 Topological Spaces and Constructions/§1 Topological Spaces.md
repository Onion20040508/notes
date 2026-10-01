---
type: section
subject: "[[Topology]]"
chapter: 1
section: 1
tags: [topology, math590]
---
↑ [[· 1 Topological Spaces and Constructions]] · [[§2 Basis for a Topology]] →

## What is Topology?

Topology is the study of **topological spaces**, **continuous maps** between them, and **properties preserved by continuous maps**.

> [!example] Example §1.1: Topological Spaces
> Examples of topological spaces include:
> - $\mathbb{R}^n = \{(x_1, \ldots, x_n) \mid x_i \in \mathbb{R}\}$: Euclidean space
> - $\mathbb{R}^\infty$: Infinite-dimensional Euclidean space
> - Function spaces, e.g., $\{f : \mathbb{R} \to \mathbb{R}\}$ (with appropriate topology)
> - Circles $S^1$, surfaces, spheres $S^n$, tori $S^1 \times S^1$
> - Products: $S^1 \times S^1$, $S^1 \times S^1 \times S^1$, $S^1 \times \mathbb{R}$
> - Metric spaces (which have a natural topology induced by the distance function)

^ex-1-1

> [!remark] Question: Basic Question
> When are two topological spaces “the same”? For example, is a coffee mug $\approx$ a donut (torus)?
>
> What tools can we use to tell that two spaces are different? Intuitively, a circle $S^1 \neq$ a figure-eight $\infty$.

^rem-1-1

> [!remark]- Connections
> - “The same” is made precise by [[§9 Continuous Functions#^def-9-2|homeomorphism]] (see [[§9 Continuous Functions#^rem-9-2|What Homeomorphism Really Means]]).
> - Telling $S^1$ from the figure-eight: [[§29 The Seifert–van Kampen Theorem#^ex-29-2|π₁ of the figure eight]] vs. [[Fundamental Group of the Circle|π₁(S¹) ≅ ℤ]].

**Goal:** Define topological invariants. Understand what properties are preserved under continuous maps.

## Definition of a Topology

> [!definition] Definition §1.1: Topology
> Let $X$ be a set. A **topology** $\mathcal{T}$ on $X$ is a collection of subsets of $X$ satisfying the following properties:
> 1. $\emptyset$ and $X$ are elements of $\mathcal{T}$.
> 2. If $\{U_i\}_{i \in I}$ is any collection of elements of $\mathcal{T}$, then $\bigcup_{i \in I} U_i \in \mathcal{T}$.
> 3. If $U_1, \ldots, U_m \in \mathcal{T}$ (for some $m \in \mathbb{N}$, **finite**), then $U_1 \cap \cdots \cap U_m \in \mathcal{T}$.
>
> The pair $(X, \mathcal{T})$ is called a **topological space** (or often just $X$ with $\mathcal{T}$ omitted if clear from context). The elements of $\mathcal{T}$ are called the **open sets** of the topological space $X$.

^def-1-1

> [!remark]- Connections
> - MATH 451 version: [[§13 Some Topological Concepts in Metric Spaces#^def-13-5|open subsets of a metric space]]; these form the [[§11 Metric Topology#^def-11-3|metric topology]].
> - Dual axioms for complements: [[§6 Closed Sets and Limit Points#^thm-6-1|Properties of Closed Sets]].

> [!remark] Remark
> Note that condition (2) allows for *arbitrary* unions (including uncountable), while condition (3) only allows *finite* intersections. This asymmetry is crucial!

^rem-1-2

> [!example] Example §1.2: Trivial/Indiscrete Topology
> Let $X$ be a set. Then $\mathcal{T} = \{\emptyset, X\}$ is a topology on $X$, called the **trivial topology** or **indiscrete topology**.
>
> *Verification:* Check $\emptyset \cup X = X \in \mathcal{T}$ and $\emptyset \cap X = \emptyset \in \mathcal{T}$. $\checkmark$

^ex-1-2

> [!example] Example §1.3: Discrete Topology
> Let $X$ be a set. Let $\mathcal{T} = \mathcal{P}(X)$ be the collection of *all* subsets of $X$. Then $\mathcal{T}$ is a topology on $X$, called the **discrete topology**.

^ex-1-3

> [!remark]- Connections
> - Basis of one-point sets: [[§2 Basis for a Topology#^ex-2-1|Basis for Discrete Topology]]; recognizing it: [[§2 Basis for a Topology#^rem-2-2|Characterization of Discrete Topology]].

> [!remark] Remark
> A set $X$ can have different topologies on it. The trivial and discrete topologies represent the two extremes.

^rem-1-3

> [!remark] Remark: Why Abstract Topology?
> In [[Single Variable Analysis|MATH 451]] (real analysis), “open” meant something concrete: a set $U \subseteq \mathbb{R}^n$ where every point has an $\varepsilon$-ball inside $U$. That definition depends on a *metric* (distance function). But many natural constructions—quotient spaces (gluing edges of a polygon), function spaces ($\mathbb{R}^\mathbb{R}$), spaces arising in algebraic geometry—have no natural metric, or the “right” topology isn't the one a metric would give.
>
> The axioms of a topology distill exactly what we need from “open sets” to do analysis: define continuity, convergence, compactness, and connectedness. By keeping only these three axioms, we gain the flexibility to study spaces that metrics cannot reach, while every theorem we prove applies automatically to $\mathbb{R}^n$, metric spaces, and beyond.

^rem-1-4

> [!remark]- Connections
> - The MATH 451 notion: [[§13 Some Topological Concepts in Metric Spaces#^def-13-5|Open and Closed Subsets]] of a metric space.
> - Quotient spaces: [[§12 Quotient Topology#^def-12-3|Quotient Space]].

> [!example] Example §1.4: Checking Topologies on a Three-Element Set
> Which of the following represent a topology on $X = \{a, b, c\}$?
> 1. $\mathcal{T}_1 = \{\emptyset, X\}$ ✓ (trivial topology)
> 2. $\mathcal{T}_2 = \{\emptyset, \{a\}, \{a,b\}, X\}$ ✓
> 3. $\mathcal{T}_3 = \{\emptyset, \{a\}, \{b,c\}, X\}$ ✓
> 4. $\mathcal{T}_4 = \{\emptyset, \{a\}, \{b\}, X\}$ $\times$ (fails: $\{a\} \cup \{b\} = \{a,b\} \notin \mathcal{T}_4$)
> 5. $\mathcal{T}_5 = \{\emptyset, \{a,b\}, \{b,c\}, X\}$ $\times$ (fails: $\{a,b\} \cap \{b,c\} = \{b\} \notin \mathcal{T}_5$)

^ex-1-4

![[m590-1-1.svg]]
*The five collections of Example §1.4 on $X=\{a,b,c\}$ (the frame is $X$ itself; blue loops are the other open sets). $\mathcal{T}_4$ fails because the union $\{a,b\}$ of two of its open sets (dashed red) is missing; $\mathcal{T}_5$ fails because the intersection $\{b\}$ of two of its open sets (dashed red) is missing.*

## The Standard Topology on $\mathbb{R}$

> [!example] Example §1.5: Standard Topology on $\mathbb{R}$
> The **standard topology** on $\mathbb{R}$ (denoted $\mathcal{T}_{\text{std}}$) includes: $(a,b) \in \mathcal{T}_{\text{std}}$ for all $a, b \in \mathbb{R}$.
>
> More precisely, a set $U \subseteq \mathbb{R}$ is open in $\mathcal{T}_{\text{std}}$ if and only if for every $x \in U$, there exists $\varepsilon > 0$ such that $(x - \varepsilon, x + \varepsilon) \subseteq U$.

^ex-1-5

> [!remark]- Connections
> - MATH 451: [[§13 Some Topological Concepts in Metric Spaces#^ex-13-6|Open intervals are open]].
> - Generated by open intervals: [[§2 Basis for a Topology#^ex-2-2|Standard Topology on ℝ (basis)]]; equals the [[§3 Order Topology#^ex-3-5|order topology on ℝ]].

> [!remark] Question
> What are some other examples of elements in $\mathcal{T}_{\text{std}}$, i.e., other open sets in $(\mathbb{R}, \mathcal{T}_{\text{std}})$?

^rem-1-5

> [!example] Example §1.6: Open Sets in Standard Topology
> - $(a,b) \cup (c,d)$ (union of disjoint intervals)
> - $(a,b) \cap (c,d)$ (intersection, possibly empty)
> - $(-\infty, a) = \{x \mid x < a\}$
> - $(a, \infty) = \{x \mid x > a\}$
> - $\mathbb{R} \setminus \mathbb{Z} = \bigcup_{n \in \mathbb{Z}} (n, n+1)$
> - $\bigcup_{n \in \mathbb{N}} \left(\frac{1}{n}, a\right)$ for fixed $a$
> - $(b, \infty) = \bigcup_{n \in \mathbb{N}} (b, b + n)$

^ex-1-6

## Comparing Topologies

> [!definition] Definition §1.2: Finer and Coarser Topologies
> If $\mathcal{T}$ and $\mathcal{T}'$ are two topologies on a set $X$, then:
> 1. If $\mathcal{T}' \supset \mathcal{T}$, then $\mathcal{T}'$ is **finer** than $\mathcal{T}$. Furthermore, if $\mathcal{T}' \neq \mathcal{T}$, then $\mathcal{T}'$ is **strictly finer**.
> 2. If $\mathcal{T}' \subset \mathcal{T}$, then $\mathcal{T}'$ is **coarser** than $\mathcal{T}$. Similarly, strictly coarser if $\mathcal{T}' \subsetneq \mathcal{T}$.
> 3. $\mathcal{T}$ and $\mathcal{T}'$ are **comparable** if $\mathcal{T} \subset \mathcal{T}'$ or $\mathcal{T} \supset \mathcal{T}'$.

^def-1-2

> [!remark]- Connections
> - Tested on bases: [[§2 Basis for a Topology#^lem-2-2|Comparing Topologies via Bases]], [[§2 Basis for a Topology#^cor-2-3|Comparing Topologies via Basis Openness]].
> - Worked case: [[§2 Basis for a Topology#^ex-2-5|ℝ_ℓ and ℝ_K are strictly finer than ℝ_std]].

> [!example] Example §1.7
> - The trivial topology on $X$: $\mathcal{T}_t = \{\emptyset, X\}$ is coarser than any topology on $X$.
> - The discrete topology on $X$: $\mathcal{T}_d = \mathcal{P}(X)$ is finer than any topology on $X$.

^ex-1-7
