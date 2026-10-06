---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 1
section: 10
tags: [differentiable-manifolds, math591]
---
← [[§9 Complex Projective Space]] · ↑ [[· 1 Topological Manifolds]] · [[§11 Topological Groups and Classical Matrix Groups]] →

*Thread: examples — The line with two origins, the standard space that is locally Euclidean and second countable but not Hausdorff, in one place: its description as a quotient of two lines, and the Hausdorff criterion for open quotients applied to it.*

The line with two origins through the course: defined by its neighbourhood bases, and not Hausdorff, in [[§1 Point-Set Topology Review#^ex-1-4|the real line with two origins]]; second countable and locally Euclidean but not Hausdorff, so not a manifold, in [[§2 Topological Manifolds#^ex-2-1|the line with two origins fails Hausdorff]]; the quotient of two lines in [[§4 Quotient Spaces and Open Maps#^ex-4-1|the line with two origins as a quotient]], the two constructions agreeing by [[§4 Quotient Spaces and Open Maps#^prop-4-2|the two constructions agree]]; and, with its description as a quotient and the Hausdorff criterion for open quotients applied to it, in *this section*.

> [!remark] Remark: The Line with Two Origins as a Quotient
> Equivalently ([[§4 Quotient Spaces and Open Maps#^prop-4-2|Proposition §4.2]]), the line with two origins $X$ of [[§1 Point-Set Topology Review#^ex-1-4|Example §1.4]] is the quotient of $\mathbb{R} \times \{1, 2\}$ (two disjoint copies of $\mathbb{R}$) by the equivalence relation $(x, 1) \sim (x, 2)$ for all $x \neq 0$: glue the two lines everywhere except at the origins. This is the standard example showing that *a quotient of a Hausdorff space need not be Hausdorff* (cf. [[§13 Quotient Topology|590 §13]]). We met this space again in [[§2 Topological Manifolds|§2]] as the reason the Hausdorff condition must be imposed *separately* on manifolds—it does not follow from being locally Euclidean.

^rem-10-1

> [!example] Example §10.1: The Line with Two Origins — via the Criterion
> Let $X = (\mathbb{R} \times \{1\}) \cup (\mathbb{R} \times \{2\}) \subseteq \mathbb{R}^2$ with the subspace topology (two disjoint copies of $\mathbb{R}$), and $(x,1) \sim (x,2)$ for $x \neq 0$, as in [[§4 Quotient Spaces and Open Maps#^ex-4-1|Example §4.1]]. The graph
>
> $$
> \Gamma = \{(a,b) \in X \times X \mid a = b\} \cup \{\, ((x,i),(x,j)) \mid x \neq 0,\ i \neq j \,\}
> $$
>
> is *not* closed in $X \times X$: the points $\big((\tfrac1n, 1), (\tfrac1n, 2)\big)$ lie in $\Gamma$ for every $n$, and converge in $X \times X$ to $\big((0,1),(0,2)\big)$, which is not in $\Gamma$ (the two origins are distinct and are not identified, the identification being imposed only for $x \neq 0$). A closed set contains the limits of its convergent sequences, so $\Gamma$ is not closed.
>
> The relation is open: the saturation of an open $U \subseteq X$ is $U \cup \sigma(U \setminus (\{0\} \times \{1,2\}))$, where $\sigma(x,i) = (x, 3-i)$ swaps the two copies—a homeomorphism of $X$—so the saturation is a union of two open sets. [[§6 Open Quotients#^thm-6-1|Theorem §6.1]] therefore applies and gives: $X/{\sim}$ is *not* Hausdorff. This recovers [[§1 Point-Set Topology Review#^ex-1-4|Example §1.4]] from the criterion rather than by separating the origins by hand.

^ex-10-1

*Uses:* [[§4 Quotient Spaces and Open Maps#^ex-4-1|Ex. §4.1]], [[§6 Open Quotients#^def-6-1|Def. §6.1]], [[§4 Quotient Spaces and Open Maps#^prop-4-5|§4.5]], [[§6 Open Quotients#^thm-6-1|§6.1]], [[§12 Metric Topology#^lem-12-8|590 §12.8]]

> [!remark]- Connections
> - “A closed set contains the limits of its convergent sequences” is the [[§12 Metric Topology#^lem-12-8|Sequence Lemma, 590 §12.8]].

PSet 1, Problem 2 asks for the non-closedness of $\Gamma$ directly. The sequence argument above needs no metrizability: in any topological space, if $z_n \to z$ with all $z_n$ in a closed set $C$, then $z \in C$ (otherwise the open set $X \setminus C$ would eventually contain the $z_n$).
