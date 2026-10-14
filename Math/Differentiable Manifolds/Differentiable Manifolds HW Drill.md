---
type: review
subject: "[[Differentiable Manifolds]]"
tags: [differentiable-manifolds, math591, review]
---
↑ [[Differentiable Manifolds]] · [[Differentiable Manifolds Midterm Review|Midterm Review]]

# Homework Drill (HW1–HW5)

Uribe on the midterm (Lecture 17, Oct 9): the short proofs "will be either identical to homework problems, or very close to pieces of homework problems". Every problem of Assignments 1–5 is broken here into small questions, in order. All five assignments are submitted.

**How to drill.**
1. Read the statement and try the questions top to bottom on paper, closed book.
2. **[def]** marks a definition to state exactly; **[why]** asks what breaks without a hypothesis.
3. Tick a question when you can answer it without looking.
4. When all the questions of a problem are ticked, write the full proof in one go.
5. Only open **Hints** when stuck. It lists the definitions and results involved (linked to the notes), the strategy (codes S1–S15, listed at the end) and a note on your submitted solution.

## Assignment 1 (due 9/13)

### HW1.1 Connected manifolds are path connected

Show that a connected topological manifold is path connected.

^hw1-1

- [ ] Q1 **[def]** State the definition of a topological manifold. Which of its three conditions does this proof actually use?
- [ ] Q2 Let $\varphi : U \to \mathbb{R}^n$ be a chart. Show $U$ is path connected (pull back straight segments).
- [ ] Q3 State the concatenation lemma. Why is the concatenated path continuous (which version of the pasting lemma)?
- [ ] Q4 Fix $x_0$ and let $S$ be the set of points joined to $x_0$ by a path. Show $S$ is open.
- [ ] Q5 Show $M \setminus S$ is open.
- [ ] Q6 Conclude $S = M$; then explain how to join two arbitrary points $x, y$ (reversal + concatenation).
- [ ] Q7 **[why]** Give a connected space that is not path connected (topologist's sine curve). Which step of Q4–Q5 breaks for it, and which hypothesis on $M$ prevented that?

> [!tip]- Hints: definitions, results, strategy
> **Topic and definitions.** Topological manifolds; connectedness vs path connectedness.
> - Locally Euclidean: [[§2 Topological Manifolds#^def-2-1|Def §2.1]]
> - Topological manifold: [[§2 Topological Manifolds#^def-2-2|Def §2.2]]
> - Connected component: [[§1 Point-Set Topology Review#^def-1-9|Def §1.9]]; connectedness facts [[§1 Point-Set Topology Review#^prop-1-7|Prop §1.7]]
>
> **Key results.** [[§2 Topological Manifolds#^thm-2-8|Thm §2.8]] (this problem, PSet 1 #1); concatenation and reversal of paths [[§2 Topological Manifolds#^lem-2-7|Lem §2.7]]; consequence [[§2 Topological Manifolds#^cor-2-9|Cor §2.9]].
>
> **Strategy (S13).** Clopen argument: the set of points reachable from $x_0$ by a path is nonempty, open and closed, because chart domains are path connected.
>
> **Difficulty 1.** Submitted solution: standard, four explicit steps (path-connected chart neighbourhood, concatenation lemma, clopen set, conclusion). The same clopen template is reused in HW4.1.

### HW1.2 The graph of the line-with-two-origins relation is not closed

Let $X = (\mathbb{R}\times\{1\}) \cup (\mathbb{R}\times\{2\})$ and $(x,1) \sim (x,2)$ for all $x \in \mathbb{R}\setminus\{0\}$. Show directly that the graph $\Gamma$ of $\sim$ is not closed. (Hint: a sequence in $\Gamma$ converging to a point not in $\Gamma$.)

^hw1-2

- [ ] Q1 **[def]** Define the graph $\Gamma$ of an equivalence relation. Write $\Gamma$ for this $\sim$ explicitly (do not forget the diagonal).
- [ ] Q2 Describe a basis of the product topology on $X \times X$.
- [ ] Q3 Show the sequence $\big((1/n,1),(1/n,2)\big)$ converges in $X \times X$, and identify the limit.
- [ ] Q4 Show the limit is not in $\Gamma$.
- [ ] Q5 Prove: in any topological space, the limit of a sequence lying in a closed set lies in that set (no metric needed).
- [ ] Q6 **[why]** To conclude that the quotient is not Hausdorff from "$\Gamma$ not closed", which hypothesis of Thm §6.1 must you check? Does it hold here?
- [ ] Q7 Show the quotient (the line with two origins) is locally Euclidean and second countable. Which manifold axiom fails?

> [!tip]- Hints: definitions, results, strategy
> **Topic and definitions.** Quotients and the Hausdorff property.
> - Graph of a relation: [[§6 Open Quotients#^def-6-1|Def §6.1]]
> - Quotient space / topology: [[§4 Quotient Spaces and Open Maps#^def-4-1|Def §4.1]], [[§4 Quotient Spaces and Open Maps#^def-4-2|Def §4.2]]
> - Product topology: [[§3 Subspaces and Products#^def-3-3|Def §3.3]]; open equivalence relation [[§4 Quotient Spaces and Open Maps#^def-4-4|Def §4.4]]
> - Hausdorff: [[§1 Point-Set Topology Review#^def-1-8|Def §1.8]]
>
> **Key results.** Hausdorff criterion [[§6 Open Quotients#^thm-6-1|Thm §6.1]] (open relation: quotient Hausdorff iff graph closed); [[§10 The Line with Two Origins#^ex-10-1|Ex §10.1]] (this problem); [[§4 Quotient Spaces and Open Maps#^ex-4-1|Ex §4.1]], [[§2 Topological Manifolds#^ex-2-1|Ex §2.1]].
>
> **Strategy (S14).** Sequence test: $\big((1/n,1),(1/n,2)\big) \in \Gamma$ converges to $\big((0,1),(0,2)\big) \notin \Gamma$.
>
> **Difficulty 1.** Submitted solution: phrased as "the limit is a limit point of $\Gamma$", checked on basis boxes $V_1 \times V_2$; the notes (§10) add that the sequence argument needs no metrizability.

### HW1.3 A non-Hausdorff orbit space

Let $\mathbb{R}^+$ act on $X = \mathbb{R}^2\setminus\{0\}$ by $t\cdot(x,y) = (tx, y/t)$. Show that $X/\mathbb{R}^+$ is not Hausdorff.

^hw1-3

- [ ] Q1 **[def]** Define the orbit space and its topology.
- [ ] Q2 Sketch the orbits: each branch of the hyperbolas $xy = c$, $c \neq 0$, and the four open half-axes.
- [ ] Q3 Show $[(1,0)] \neq [(0,1)]$.
- [ ] Q4 Find $t$ with $t \cdot (1, 1/n) = (1/n, 1)$.
- [ ] Q5 Show $[z_n] \to [(1,0)]$ and $[z_n] \to [(0,1)]$ (pull an open neighbourhood back to $X$).
- [ ] Q6 Why does a sequence in a Hausdorff space have at most one limit?
- [ ] Q7 **[why]** Cor §13.4 says a compact group acting on a Hausdorff space has a Hausdorff orbit space. Which hypothesis fails here? Explain how non-compactness of $\mathbb{R}^+$ lets the two half-axis orbits be approached by the same hyperbolas.
- [ ] Q8 Alternative route: show the graph of the orbit relation is not closed and apply Thm §6.1 (why is the relation open?).

> [!tip]- Hints: definitions, results, strategy
> **Topic and definitions.** Group actions and orbit spaces.
> - Group action / continuous action: [[§13 Group Actions and Orbit Spaces#^def-13-1|Def §13.1]], [[§13 Group Actions and Orbit Spaces#^def-13-2|Def §13.2]]
> - Orbit, orbit relation, orbit space: [[§13 Group Actions and Orbit Spaces#^def-13-3|Def §13.3]], [[§13 Group Actions and Orbit Spaces#^def-13-4|Def §13.4]], [[§13 Group Actions and Orbit Spaces#^def-13-5|Def §13.5]]
> - Hausdorff: [[§1 Point-Set Topology Review#^def-1-8|Def §1.8]]
>
> **Key results.** [[§13 Group Actions and Orbit Spaces#^ex-13-6|Ex §13.6]] (this problem); orbit relations are open [[§13 Group Actions and Orbit Spaces#^lem-13-3|Lem §13.3]]; compact group gives Hausdorff orbit space [[§13 Group Actions and Orbit Spaces#^cor-13-4|Cor §13.4]], [[§13 Group Actions and Orbit Spaces#^thm-13-5|Thm §13.5]]; [[§6 Open Quotients#^thm-6-1|Thm §6.1]].
>
> **Strategy (S14).** One sequence with two limits: $z_n = (1, 1/n)$ is in the same orbit as $(1/n, 1)$, so $[z_n]$ converges to both $[(1,0)]$ and $[(0,1)]$.
>
> **Difficulty 1.** Submitted solution: the rescaling trick $(1/n)\cdot(1,1/n) = (1/n,1)$, then two convergence checks via basic boxes. Short.

### HW1.4 First and second countability; a non-second-countable quotient

*Parts: (a), (b).*

^hw1-4

#### (a)

$X$ is first countable at $x_0$ iff there is a countable base of neighbourhoods of $x_0$. Show a second countable space is first countable at each of its points.

^hw1-4-a

- [ ] Q1 **[def]** Define "countable base of neighbourhoods of $x_0$" and "second countable".
- [ ] Q2 Given a countable basis $\mathcal{B}$, show $\mathcal{B}_{x_0} = \{B \in \mathcal{B} : x_0 \in B\}$ is countable.
- [ ] Q3 Show every open $U \ni x_0$ contains some member of $\mathcal{B}_{x_0}$.
- [ ] Q4 **[why]** Is the converse true? Give a space that is first countable at every point but not second countable ($\mathbb{R}$ discrete).

> [!tip]- Hint (a): strategy
> **Strategy.** Keep the members of a countable basis that contain $x_0$.

#### (b)

$X = \mathbb{R}/\sim$ with $x \sim y$ iff $x = y$ or $x, y \in \mathbb{Z}$; all integers become one point $x_0$. Show $X$ is not first countable at $x_0$, hence not second countable. (Hint: WLOG $\pi^{-1}(U_j) = \bigcup_{n\in\mathbb{Z}}(n - a_{j,n}, n + a_{j,n})$; diagonal process.)

^hw1-4-b

- [ ] Q1 **[def]** State the quotient topology. For which open $U \subseteq \mathbb{R}$ is $\pi(U)$ open?
- [ ] Q2 Show: $V \ni x_0$ is open in $X$ iff $\pi^{-1}(V)$ is open in $\mathbb{R}$ and contains $\mathbb{Z}$; and every open $U \supseteq \mathbb{Z}$ is saturated.
- [ ] Q3 Explain why one may shrink each $U_j$ to a union of symmetric intervals around the integers without losing the "base" property.
- [ ] Q4 Construct $W = \bigcup_n (n - b_n, n + b_n)$ with $b_j < a_{j,j}$ for $j \ge 1$. Show $\pi(W)$ is an open neighbourhood of $x_0$.
- [ ] Q5 For each $j$, exhibit a point of $U_j$ not in $W$, and conclude.
- [ ] Q6 **[why]** Why must infinitely many integers be identified? (If only finitely many points are collapsed, what goes wrong with the diagonal argument?)
- [ ] Q7 **[why]** $\mathbb{R}$ is second countable; Thm §6.3 says open quotients of second countable spaces are second countable. Why is $\pi$ not an open map?

> [!tip]- Hint (b): strategy
> **Strategy (S4, diagonal).** Neighbourhoods of $x_0$ are open sets of $\mathbb{R}$ containing $\mathbb{Z}$; given countably many, build one whose $j$-th arm is smaller than the $j$-th arm of the $j$-th set.

> [!tip]- Hints: definitions and results for the whole problem
> **Topic and definitions.**
> - Basis: [[§1 Point-Set Topology Review#^def-1-1|Def §1.1]]; basis of neighbourhoods at a point [[§1 Point-Set Topology Review#^def-1-5|Def §1.5]]
> - Second countable: [[§1 Point-Set Topology Review#^def-1-6|Def §1.6]]; first countable at a point [[§1 Point-Set Topology Review#^def-1-7|Def §1.7]]
> - (b) Quotient topology [[§4 Quotient Spaces and Open Maps#^def-4-2|Def §4.2]]; saturation, saturated set [[§4 Quotient Spaces and Open Maps#^def-4-5|Def §4.5]], [[§4 Quotient Spaces and Open Maps#^def-4-6|Def §4.6]]
>
> **Key results.** (a) [[§1 Point-Set Topology Review#^prop-1-4|Prop §1.4]], [[§1 Point-Set Topology Review#^prop-1-3|Prop §1.3]]. (b) [[§4 Quotient Spaces and Open Maps#^ex-4-4|Ex §4.4]] (this problem, proof in the notes), [[§4 Quotient Spaces and Open Maps#^rem-4-4|Remark: Why the Diagonal]] (why the diagonal), openness via saturations [[§4 Quotient Spaces and Open Maps#^prop-4-5|Prop §4.5]]; contrast: open quotients stay second countable [[§6 Open Quotients#^thm-6-3|Thm §6.3]].
>
> **Difficulty** (a) 1, (b) 2. Submitted solution: caps radii at $1/4$ so the arms stay disjoint, proves $\pi^{-1}(\pi(U)) = U$ for open $U \supseteq \mathbb{Z}$, and uses $b_n = a_{n,n}/2$ with the witness $w_j = j + \tfrac34 a_{j,j}$. Careful bookkeeping of $\mathbb{N}$ vs $\mathbb{Z}$ indices.

### HW1.5 Projections are quotient maps

A quotient map is a surjection with $U$ open iff $F^{-1}(U)$ open; then $Y \cong X/\sim$, $a \sim b \iff F(a) = F(b)$ (no proof needed). Prove that any projection $\pi_i : X_1 \times \cdots \times X_n \to X_i$ is a quotient map.

^hw1-5

- [ ] Q1 **[def]** State the definition of a quotient map (both directions of the "iff").
- [ ] Q2 Why is $\pi_i^{-1}(U) = X_1 \times \cdots \times U \times \cdots \times X_n$ open?
- [ ] Q3 Show $\pi_i$ maps an open box onto its $i$-th factor, and deduce $\pi_i$ is open.
- [ ] Q4 Prove: a continuous open surjection is a quotient map (use $\pi(\pi^{-1}(U)) = U$).
- [ ] Q5 **[why]** What happens if some $X_k$, $k \ne i$, is empty? Which step uses nonemptiness?
- [ ] Q6 Give a quotient map that is not open (e.g. the map of HW1.4(b)).

> [!tip]- Hints: definitions, results, strategy
> **Topic and definitions.**
> - Quotient map: [[§5 Quotient Maps#^def-5-1|Def §5.1]]
> - Product topology, projections: [[§3 Subspaces and Products#^def-3-3|Def §3.3]], [[§3 Subspaces and Products#^def-3-4|Def §3.4]]
> - Open map: [[§4 Quotient Spaces and Open Maps#^def-4-3|Def §4.3]]
>
> **Key results.** Box characterization [[§3 Subspaces and Products#^prop-3-8|Prop §3.8]]; projections are open [[§4 Quotient Spaces and Open Maps#^ex-4-2|Ex §4.2]]; open surjections are quotient maps [[§5 Quotient Maps#^prop-5-5|Prop §5.5]]; [[§5 Quotient Maps#^ex-5-2|Ex §5.2]] (this problem); a quotient map presents its target [[§5 Quotient Maps#^prop-5-4|Prop §5.4]].
>
> **Strategy (S4).** Continuous + open + surjective ⇒ quotient map; openness from $\pi_i(\text{box}) = U_{x,i}$.
>
> **Difficulty 1.** Submitted solution: proves it directly from boxes, and treats the empty-factor case explicitly (the statement fails if another factor is empty). The notes (§5) keep the direct argument as a remark next to the "open surjection" proof.

### HW1.6 Regular level sets are topological manifolds

Let $F : \mathbb{R}^{n+k} \to \mathbb{R}^k$ be smooth with $F'(p)$ of maximal rank for all $p \in F^{-1}(\vec 0)$. Use the implicit function theorem (Lee C.40) to show $X = F^{-1}(\vec 0)$ is a topological manifold. (Hint: relabel coordinates so that $(\partial F^i/\partial y^j(p))$ is non-singular.)

^hw1-6

- [ ] Q1 **[def]** Define regular value. What does "maximal rank" mean for a $k \times (n+k)$ matrix?
- [ ] Q2 Why are Hausdorff and second countable automatic for $X$?
- [ ] Q3 Show some $k$ columns of $F'(p)$ are independent, and that permuting coordinates is a linear homeomorphism carrying $X$ to a set of the same kind.
- [ ] Q4 State the IFT precisely (hypotheses on which block of the Jacobian, conclusion with neighbourhoods $V_0, W_0$ and $G$).
- [ ] Q5 Show $X \cap (V_0 \times W_0) = \{(x, G(x))\}$ and that $(x,y) \mapsto x$ is a homeomorphism onto $V_0$ with inverse $x \mapsto (x, G(x))$.
- [ ] Q6 Why is a homeomorphism onto an open subset of $\mathbb{R}^n$ enough (Prop §2.3)?
- [ ] Q7 **[why]** Where is the rank condition needed? Look at $F(x,y) = x^2 - y^2$ at $0$: what is $F^{-1}(0)$ and why is it not a manifold?
- [ ] Q8 Why are two such graph charts $C^\infty$-compatible (HW2 background)?

> [!tip]- Hints: definitions, results, strategy
> **Topic and definitions.** The regular value theorem.
> - Jacobian, rank: [[§7 The Regular Value Theorem#^def-7-1|Def §7.1]], [[§7 The Regular Value Theorem#^def-7-2|Def §7.2]]
> - Regular point/value: [[§7 The Regular Value Theorem#^def-7-3|Def §7.3]], [[§7 The Regular Value Theorem#^def-7-4|Def §7.4]]
> - Subspace topology: [[§3 Subspaces and Products#^def-3-1|Def §3.1]]; topological manifold [[§2 Topological Manifolds#^def-2-2|Def §2.2]]
>
> **Key results.** Implicit function theorem [[§7 The Regular Value Theorem#^thm-7-1|Thm §7.1]]; regular value theorem [[§7 The Regular Value Theorem#^thm-7-3|Thm §7.3]] (this problem) and [[§7 The Regular Value Theorem#^cor-7-4|Cor §7.4]]; subspaces inherit $T_2$ and 2C [[§3 Subspaces and Products#^thm-3-5|Thm §3.5]]; charts onto open subsets suffice [[§2 Topological Manifolds#^prop-2-3|Prop §2.3]]; smooth version [[§20 Manifolds in Euclidean Space#^prop-20-2|Prop §20.2]].
>
> **Strategy (S5).** Rank $k$ ⇒ $k$ independent columns ⇒ after permuting coordinates the IFT writes $X$ locally as a graph $y = G(x)$; projection to $x$ is a chart.
>
> **Difficulty 2.** Submitted solution: long (permutation matrix $M(\sigma)$ bookkeeping, explicit ball-to-$\mathbb{R}^n$ homeomorphism $u \mapsto (u-a)/(r-|u-a|)$). Prop §2.3 makes the last step unnecessary. The notes' Thm §7.3 proof is the condensed version.
>
> ---
>
> ## Assignment 2 (due 9/20)
>
> Background given in the assignment: $c$ is a regular value of $F : W \to \mathbb{R}^k$ ($W \subseteq \mathbb{R}^{n+k}$ open) if $F'(p)$ has rank $k$ on $F^{-1}(c)$; the geometric tangent space is $T_pM = \ker F'(p)$.

### HW2.1 Homogeneous spaces vs coset spaces

*Parts: (a), (b).*

^hw2-1

#### (a)

$G$ acts transitively and continuously on $X$, $H$ the isotropy group of $x_0$, $\Phi : G/H \to X$ the natural bijection. Show $\Phi$ is continuous.

^hw2-1-a

- [ ] Q1 **[def]** Define the isotropy subgroup and the map $\Phi(gH) = g \cdot x_0$. Which action axioms make $\Phi$ well defined and injective; which hypothesis makes it surjective?
- [ ] Q2 State the universal property of a quotient map.
- [ ] Q3 Show the orbit map is continuous, as $A \circ (\mathrm{id}_G, \text{const}_{x_0})$.
- [ ] Q4 Conclude that $\Phi$ is continuous.

> [!tip]- Hint (a): strategy
> **Strategy (S3).** $\Phi \circ \pi$ is the orbit map $g \mapsto g\cdot x_0$, which is continuous; the universal property gives continuity of $\Phi$.

#### (b)

If $G/H$ is compact and $X$ is Hausdorff, then $\Phi$ is a homeomorphism.

^hw2-1-b

- [ ] Q5 Prove: closed in compact is compact; compact in Hausdorff is closed; continuous image of compact is compact.
- [ ] Q6 Deduce $\Phi$ is a closed map, and that $\Phi^{-1}$ is continuous.
- [ ] Q7 **[why]** In Ex §15.2 ($G = \mathbb{R}_{\mathrm{disc}}$ acting on $\mathbb{R}$ by translation), $\Phi$ is a continuous bijection that is not a homeomorphism. Which hypothesis of (b) fails?
- [ ] Q8 **[why]** The board version said "$G$ compact" with no condition on $X$. Why is that the wrong pair of hypotheses (which space must be compact, and why is Hausdorffness of $X$ needed)?

> [!tip]- Hint (b): strategy
> **Strategy (S12).** A continuous bijection from a compact space to a Hausdorff space is closed, hence a homeomorphism.

> [!tip]- Hints: definitions and results for the whole problem
> **Topic and definitions.**
> - Topological group: [[§11 Topological Groups and Classical Matrix Groups#^def-11-1|Def §11.1]]; continuous action [[§13 Group Actions and Orbit Spaces#^def-13-2|Def §13.2]]
> - Transitive action, isotropy subgroup, orbit map: [[§14 Homogeneous Spaces#^def-14-1|Def §14.1]], [[§14 Homogeneous Spaces#^def-14-3|Def §14.3]], [[§14 Homogeneous Spaces#^def-14-4|Def §14.4]]
> - Coset space, canonical projection: [[§14 Homogeneous Spaces#^def-14-6|Def §14.6]], [[§14 Homogeneous Spaces#^def-14-7|Def §14.7]]; topology on $G/H$ [[§15 The Topology of G∕H and Real Grassmannians#^def-15-1|Def §15.1]]
>
> **Key results.** Natural bijection [[§14 Homogeneous Spaces#^lem-14-5|Lem §14.5]]; $\pi$ is a quotient map [[§15 The Topology of G∕H and Real Grassmannians#^cor-15-2|Cor §15.2]]; universal property [[§5 Quotient Maps#^thm-5-1|Thm §5.1]], [[§5 Quotient Maps#^cor-5-2|Cor §5.2]]; [[§15 The Topology of G∕H and Real Grassmannians#^thm-15-3|Thm §15.3]] (this problem); compactness facts [[§1 Point-Set Topology Review#^prop-1-8|Prop §1.8]]; examples [[§15 The Topology of G∕H and Real Grassmannians#^ex-15-1|Ex §15.1]], [[§15 The Topology of G∕H and Real Grassmannians#^ex-15-2|Ex §15.2]].
>
> **Difficulty 1.** Submitted solution: clean; (b) via "$\Phi$ maps closed sets to closed sets". The notes record that this problem corrected a misstatement on the board (Lecture 4).

### HW2.2 Complex projective space

*Parts: (a), (b), (c).*

^hw2-2

#### (a)

Explain why $\mathbb{CP}^n$ (complex lines in $\mathbb{C}^{n+1}$) is naturally $S^{2n+1}/S^1$, and prove that with the quotient topology it is second countable, Hausdorff and compact.

^hw2-2-a

- [ ] Q1 **[def]** Give three descriptions of $\mathbb{CP}^n$ (lines; $(\mathbb{C}^{n+1}\setminus 0)/\mathbb{C}^\times$; $S^{2n+1}/S^1$). Why must $0$ be removed?
- [ ] Q2 Show $z \mapsto S^1\cdot z/|z|$ is constant on $\mathbb{C}^\times$-orbits; get a continuous map by the universal property, and a continuous inverse the same way.
- [ ] Q3 Show the projection onto an orbit space of a group action is open: $\pi^{-1}(\pi(U)) = \bigcup_\lambda \lambda U$.
- [ ] Q4 Prove that an open continuous surjection carries a countable basis to a countable basis.
- [ ] Q5 Hausdorff: either quote Cor §13.4, or show directly that two distinct orbits are compact, disjoint, at positive distance $d$, and that $S^1 \cdot B(u, d/3)$, $S^1 \cdot B(v, d/3)$ are disjoint saturated open sets.
- [ ] Q6 Why is $S^{2n+1}/S^1$ compact?
- [ ] Q7 **[why]** Where does the Hausdorff argument use that $|\lambda| = 1$ (isometric action) and that $S^1$ is compact? What goes wrong for $\mathbb{C}^\times$ acting on all of $\mathbb{C}^{n+1}$?

> [!tip]- Hint (a): strategy
> **Strategy (S3, S4, S12).** Normalization $z \mapsto z/|z|$ descends through the universal property in both directions; quotients by group actions are open, so bases push forward; compact group acting by isometries gives Hausdorff; continuous image of the compact sphere.

#### (b)

$U_i = \{\ell : \ell \cap \{z_i = 0\} = \{0\}\}$, $\varphi_i([z]) = (z_0/z_i, \ldots, \widehat{z_i/z_i}, \ldots, z_n/z_i)$. Show $U_i$ is open and $\varphi_i$ is a homeomorphism onto $\mathbb{C}^n \cong \mathbb{R}^{2n}$.

^hw2-2-b

- [ ] Q1 Show: $\ell \in U_i$ iff $z_i \neq 0$ for one (equivalently every) nonzero $z \in \ell$.
- [ ] Q2 Show $U_i$ is open.
- [ ] Q3 **[def]** What does "well defined" mean for $\varphi_i$? Check it.
- [ ] Q4 State and prove: the restriction of a quotient map $p$ to $p^{-1}(V)$, $V$ open, is a quotient map onto $V$ (Lem §5.7). Which two hypotheses are used where?
- [ ] Q5 Deduce $\varphi_i$ continuous; show $\psi_i = \pi \circ s$ (insert $1$) is a continuous inverse.
- [ ] Q6 **[why]** Why can the universal property not be applied to $\pi : \mathbb{C}^{n+1}\setminus 0 \to \mathbb{CP}^n$ itself to get $\varphi_i$?

> [!tip]- Hint (b): strategy
> **Strategy (S2, S3).** Work upstairs ($\pi^{-1}(U_i) = \{z_i \neq 0\}$), check independence of the representative, get continuity from the universal property of the restricted quotient map, write the inverse $w \mapsto [w \text{ with } 1 \text{ in slot } i]$.

#### (c)

Show $\{(U_i, \varphi_i)\}$ is a $C^\infty$ atlas (FYI: transitions are holomorphic).

^hw2-2-c

- [ ] Q1 **[def]** State the three conditions for a smooth atlas.
- [ ] Q2 Show the $U_i$ cover $\mathbb{CP}^n$.
- [ ] Q3 Compute $\varphi_j(U_i \cap U_j)$ and show it is open.
- [ ] Q4 Compute the transition map and show it is $C^\infty$ as a map of $\mathbb{R}^{2n}$ (real and imaginary parts).
- [ ] Q5 **[why]** Why must transition domains be open? Why is a homeomorphism onto $\mathbb{C}^n$ not by itself enough for a smooth structure?
- [ ] Q6 Why are the transitions holomorphic, and what does that buy (Cor §18.3)?

> [!tip]- Hint (c): strategy
> **Strategy (S1).** Compute $\varphi_i \circ \varphi_j^{-1}(w) = (1/w_i, (w_k/w_i)_{k \ne i,j})$ on the open set $\{w_i \neq 0\}$: rational with nonvanishing denominator.

> [!tip]- Hints: definitions and results for the whole problem
> **Topic and definitions.**
> - $\mathbb{CP}^n$: [[§9 Complex Projective Space#^def-9-1|Def §9.1]]; as an orbit space [[§13 Group Actions and Orbit Spaces#^ex-13-3|Ex §13.3]]
> - Open map, saturation: [[§4 Quotient Spaces and Open Maps#^def-4-3|Def §4.3]], [[§4 Quotient Spaces and Open Maps#^def-4-5|Def §4.5]]
> - Homogeneous coordinates, standard charts: [[§18 Projective Spaces as Smooth Manifolds#^def-18-1|Def §18.1]], [[§18 Projective Spaces as Smooth Manifolds#^def-18-2|Def §18.2]]
> - Chart, smooth compatibility, atlas: [[§17 Differentiable Structures#^def-17-1|Def §17.1]], [[§17 Differentiable Structures#^def-17-4|Def §17.4]], [[§17 Differentiable Structures#^def-17-6|Def §17.6]]
>
> **Key results.** [[§9 Complex Projective Space#^prop-9-1|Prop §9.1]] (Hausdorff, 2C), [[§9 Complex Projective Space#^prop-9-2|Prop §9.2]] (compact), [[§9 Complex Projective Space#^prop-9-3|Prop §9.3]] (lines); open surjections push bases forward [[§5 Quotient Maps#^lem-5-6|Lem §5.6]]; restricting a quotient map over an open set [[§5 Quotient Maps#^lem-5-7|Lem §5.7]]; orbit relations are open [[§13 Group Actions and Orbit Spaces#^lem-13-3|Lem §13.3]]; [[§13 Group Actions and Orbit Spaces#^cor-13-4|Cor §13.4]]; [[§6 Open Quotients#^thm-6-3|Thm §6.3]]; [[§5 Quotient Maps#^thm-5-1|Thm §5.1]]; charts [[§18 Projective Spaces as Smooth Manifolds#^prop-18-1|Prop §18.1]]; atlas [[§18 Projective Spaces as Smooth Manifolds#^thm-18-2|Thm §18.2]]; complex manifold [[§18 Projective Spaces as Smooth Manifolds#^cor-18-3|Cor §18.3]].
>
> **Difficulty** (a) 2, (b) 2, (c) 1. Submitted solution: the longest of HW2; proves Hausdorff directly via the distance between compact orbits (radius $d/3$, isometric action), and proves the "open surjections push bases forward" and "restriction over an open set" lemmas inline. These are now Lem §5.6, Lem §5.7 and the "direct proof" after Prop §9.1; Cor §13.4 gives Hausdorff in one line.

### HW2.3 A level set in $\mathbb{R}^4$ (QR August 2013)

$F(x,y,u,v) = (x^2-y^2-u^2+v^2+2u,\ 2xy-2uv+2v)$, $M = F^{-1}(-1,0)$. Show $M$ is a submanifold of $\mathbb{R}^4$ and describe $T_{x_0}M$, $x_0 = (0,1,0,0)$.

^hw2-3

- [ ] Q1 **[def]** Define regular value. Why does it suffice to check rank only on $F^{-1}(-1,0)$?
- [ ] Q2 Compute $F'(p)$.
- [ ] Q3 With $a = 2x$, $b = 2y$, $c = 2-2u$, $d = 2v$ the rows are $(a,-b,c,d)$, $(b,a,-d,c)$. Show they are dependent only if $a=b=c=d=0$.
- [ ] Q4 Check $F(p_0) = (1,0) \neq (-1,0)$ and $F(x_0) = (-1,0)$.
- [ ] Q5 Compute $\ker F'(x_0)$; check its dimension is $4 - 2$.
- [ ] Q6 **[why]** What would happen at the level $(1,0) = F(p_0)$? Is that level set a manifold near $p_0$?
- [ ] Q7 Write $F$ as $(\mathrm{Re}, \mathrm{Im})$ of $z^2 - w^2 + 2w$, $z = x+iy$, $w = u+iv$. How does the holomorphic RVT shorten Q3?

> [!tip]- Hints: definitions, results, strategy
> **Topic and definitions.** Regular value [[§7 The Regular Value Theorem#^def-7-4|Def §7.4]]; geometric tangent space [[§25 The Geometric Tangent Space#^def-25-1|Def §25.1]]; holomorphic map [[§7 The Regular Value Theorem#^def-7-5|Def §7.5]].
>
> **Key results.** [[§7 The Regular Value Theorem#^ex-7-2|Ex §7.2]] (this problem), [[§7 The Regular Value Theorem#^ex-7-3|Ex §7.3]] (it is a cylinder); [[§7 The Regular Value Theorem#^cor-7-4|Cor §7.4]]; holomorphic RVT [[§7 The Regular Value Theorem#^cor-7-7|Cor §7.7]], [[§7 The Regular Value Theorem#^rem-7-8|Remark: The Example Re-read]]; tangent space is the kernel [[§25 The Geometric Tangent Space#^thm-25-3|Thm §25.3]].
>
> **Strategy (S5, S6).** Find where the rank drops (only at $p_0 = (0,0,1,0)$), check $p_0 \notin M$; tangent space $= \ker F'(x_0)$.
>
> **Difficulty 1.** Submitted solution: the row-pair dependence analysis. The notes add that "submanifold" had not yet been defined; what is proved is a smooth manifold carrying the subspace topology.

### HW2.4 The unitary group

Prove $U(n) = F^{-1}(I)$ for $F : \mathrm{Mat}(n,\mathbb{C}) \to \mathrm{Herm}(n)$, $g \mapsto gg^*$ (both real vector spaces) inherits a smooth manifold structure; find $\dim U(n)$ and its geometric tangent space at $g$.

^hw2-4

- [ ] Q1 **[def]** Define $U(n)$. Show $gg^* = I$ implies $g^*g = I$.
- [ ] Q2 Compute $\dim_{\mathbb{R}}\mathrm{Mat}(n,\mathbb{C}) = 2n^2$ and $\dim_{\mathbb{R}}\mathrm{Herm}(n) = n^2$.
- [ ] Q3 Compute $dF_g(h) = \frac{d}{dt}\big|_0 F(g+th)$.
- [ ] Q4 Show $dF_g$ is onto $\mathrm{Herm}(n)$ for $g \in U(n)$ (find $h$ for a given Hermitian $A$).
- [ ] Q5 Conclude $\dim U(n) = n^2$; show $\ker dF_g = \{Xg : X^* = -X\} = \mathfrak{u}(n)\,g$; why is this also $g\,\mathfrak{u}(n)$?
- [ ] Q6 **[why]** Why must the spaces be regarded as real? Show $dF_g(ih) \neq i\,dF_g(h)$ in general, and that $\mathrm{Herm}(n)$ is not a complex subspace.
- [ ] Q7 **[why]** Why is the target $\mathrm{Herm}(n)$ and not $\mathrm{Mat}(n,\mathbb{C})$? (Could $I$ be a regular value of $g \mapsto gg^*$ into $\mathrm{Mat}(n,\mathbb{C})$?)
- [ ] Q8 **[why]** Where does $g \in U(n)$ enter the surjectivity proof? Compute $dF_0$.

> [!tip]- Hints: definitions, results, strategy
> **Topic and definitions.**
> - Unitary group: [[§11 Topological Groups and Classical Matrix Groups#^def-11-10|Def §11.10]]
> - $\mathrm{Herm}(n)$ as a real vector space: [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^def-23-2|Def §23.2]]
> - Differential of a map between vector spaces: [[§22 The Differential of a Map Between Vector Spaces#^def-22-5|Def §22.5]]; geometric tangent space [[§25 The Geometric Tangent Space#^def-25-1|Def §25.1]]
>
> **Key results.** One-sided inverse suffices [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^lem-23-3|Lem §23.3]]; [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-23-2|Ex §23.2]] (this problem), kernel [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^prop-23-4|Prop §23.4]]; differential by curves [[§22 The Differential of a Map Between Vector Spaces#^thm-22-3|Thm §22.3]]; regular values without coordinates [[§22 The Differential of a Map Between Vector Spaces#^cor-22-4|Cor §22.4]]; [[§25 The Geometric Tangent Space#^ex-25-3|Ex §25.3]], [[§25 The Geometric Tangent Space#^rem-25-7|Remark: Left and Right Translates]]; contrast [[§7 The Regular Value Theorem#^rem-7-9|Remark: The Contrast with the Unitary Group]]; model case $O(n)$ [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-23-1|Ex §23.1]].
>
> **Strategy (S5, S10).** RVT on $g \mapsto gg^*$; differentiate along $t \mapsto g + th$ to get $dF_g(h) = hg^* + gh^*$; surjective via $h = \tfrac12 Ag$; kernel via $h = Xg$.
>
> **Difficulty 2.** Submitted solution: long, because it builds explicit coordinates $\phi$, $\phi_H$ and transports the atlas from $\mathbb{R}^{2n^2}$; Cor §22.4 makes that unnecessary. Tricks worth remembering: $h = \tfrac12 Ag$ and $h = Xg$.

### HW2.5 Transversality to a regular level set (Euclidean)

$F : \mathbb{R}^N \to \mathbb{R}^k$, $G : \mathbb{R}^k \to \mathbb{R}^\ell$ smooth, $0$ a regular value of $G$, $S = G^{-1}(0)$, and $\mathrm{Image}\,F'(p) + T_{F(p)}S = \mathbb{R}^k$ for all $p \in F^{-1}(S)$. Show $M = F^{-1}(S)$ has a natural manifold structure, describe $T_pM$, and show $\operatorname{codim} M = \operatorname{codim} S$.

^hw2-5

- [ ] Q1 **[def]** State the transversality condition and the definition of codimension.
- [ ] Q2 Show $M = (G\circ F)^{-1}(0)$.
- [ ] Q3 Show $(G\circ F)'(p)$ is surjective: lift $w$ through $G'(q)$, split the lift as $F'(p)v + t$ with $t \in \ker G'(q)$.
- [ ] Q4 Prove $\ker(B\circ A) = A^{-1}(\ker B)$ and deduce $T_pM = F'(p)^{-1}(T_{F(p)}S)$.
- [ ] Q5 Compute both codimensions.
- [ ] Q6 Prove the converse: if $(G\circ F)'(p)$ is onto for all $p \in M$, then $F$ is transverse to $S$ (Prop §26.2).
- [ ] Q7 **[why]** Give an $F$ not transverse to $S$ for which $F^{-1}(S)$ is not a manifold, and one for which it is a manifold of the wrong codimension (Ex §26.2).
- [ ] Q8 **[why]** The condition "does not mention $G$". Why does that matter for HW5.2?

> [!tip]- Hints: definitions, results, strategy
> **Topic and definitions.** Codimension [[§26 Transversality#^def-26-1|Def §26.1]]; transversality [[§26 Transversality#^def-26-2|Def §26.2]]; geometric tangent space [[§25 The Geometric Tangent Space#^def-25-1|Def §25.1]].
>
> **Key results.** [[§26 Transversality#^thm-26-1|Thm §26.1]] (this problem); transversality is the regular value condition [[§26 Transversality#^prop-26-2|Prop §26.2]]; [[§26 Transversality#^cor-26-3|Cor §26.3]]; transverse intersections [[§26 Transversality#^prop-26-4|Prop §26.4]]; failures [[§26 Transversality#^ex-26-2|Ex §26.2]]; [[§25 The Geometric Tangent Space#^thm-25-3|Thm §25.3]].
>
> **Strategy (S11, S5).** $M = (G \circ F)^{-1}(0)$; transversality makes $G'(q)F'(p)$ surjective; $\ker(B \circ A) = A^{-1}(\ker B)$.
>
> **Difficulty 2.** Submitted solution: about one page; the same lifting argument is reused for HW5.2.
>
> ---
>
> ## Assignment 3 (due 9/27)

### HW3.1 One-chart structures on $\mathbb{R}^n$

*Parts: (a), (b).*

^hw3-1

#### (a)

$h : \mathbb{R}^n \to \mathbb{R}^n$ a homeomorphism, $\mathcal{A} = \{h\}$. Explain why $\mathcal{A}$ is a smooth atlas.

^hw3-1-a

- [ ] Q1 **[def]** State the definition of a smooth atlas and of a transition map.
- [ ] Q2 List the transition maps of a one-chart atlas.
- [ ] Q3 **[why]** Why must $h$ be a homeomorphism and not merely a bijection?

> [!tip]- Hint (a): strategy
> **Strategy (S1).** The only transition map is $h \circ h^{-1} = \mathrm{id}$.

#### (b)

With $M = \mathbb{R}^n$ carrying the structure of $\mathcal{A}$, show $M$ is diffeomorphic to standard $\mathbb{R}^n$.

^hw3-1-b

- [ ] Q4 **[def]** Define a smooth map between manifolds via charts, and a diffeomorphism.
- [ ] Q5 Compute $\mathrm{id} \circ h \circ h^{-1}$ and $h \circ h^{-1} \circ \mathrm{id}^{-1}$.
- [ ] Q6 **[why]** For $h(x) = x^3$ on $\mathbb{R}$: show $\mathrm{id} : M \to \mathbb{R}$ is not smooth, so the two structures differ, yet $M \cong \mathbb{R}$. State the difference between "distinct smooth structures" and "non-diffeomorphic manifolds".

> [!tip]- Hint (b): strategy
> **Strategy (S1).** The map $h : M \to \mathbb{R}^n$ itself is the diffeomorphism: its coordinate representations are identities.

> [!tip]- Hints: definitions and results for the whole problem
> **Topic and definitions.** Chart [[§17 Differentiable Structures#^def-17-1|Def §17.1]]; atlas [[§17 Differentiable Structures#^def-17-6|Def §17.6]]; maximal atlas [[§17 Differentiable Structures#^def-17-8|Def §17.8]]; smooth structure [[§17 Differentiable Structures#^def-17-9|Def §17.9]]; smooth map [[§19 Smooth Functions and Smooth Maps#^def-19-3|Def §19.3]]; diffeomorphism [[§19 Smooth Functions and Smooth Maps#^def-19-4|Def §19.4]]; diffeomorphic [[§19 Smooth Functions and Smooth Maps#^def-19-5|Def §19.5]].
>
> **Key results.** [[§19 Smooth Functions and Smooth Maps#^cor-19-9|Cor §19.9]] (this problem); transport of structure [[§19 Smooth Functions and Smooth Maps#^prop-19-8|Prop §19.8]]; [[§19 Smooth Functions and Smooth Maps#^ex-19-1|Ex §19.1]], [[§19 Smooth Functions and Smooth Maps#^ex-19-2|Ex §19.2]]; [[§19 Smooth Functions and Smooth Maps#^rem-19-8|Remark: Distinct Structures versus Non-Diffeomorphic Manifolds]] (distinct structures vs non-diffeomorphic manifolds); smoothness independent of charts [[§19 Smooth Functions and Smooth Maps#^prop-19-2|Prop §19.2]].
>
> **Difficulty 1.** Submitted solution: short and direct. The key idea is that the diffeomorphism is $h$, not the identity.

### HW3.2 Every tangent vector is a velocity

For a smooth curve $\gamma : (-\epsilon,\epsilon) \to M$, $\gamma(0) = p$, let $D_\gamma[f] = \frac{d}{dt}f(\gamma(t))|_{t=0}$. Show every $D \in T_pM$ equals $D_\gamma$ for some such curve.

^hw3-2

- [ ] Q1 **[def]** Define a derivation at $p$ on germs and the tangent space $T_pM$.
- [ ] Q2 State the basis theorem and explain why the coefficients of $D$ are $D[x^i]$.
- [ ] Q3 For $\gamma = \varphi^{-1}\circ c$, show $D_\gamma = \sum_j (c^j)'(0)\,\partial/\partial x^j|_p$ (chain rule).
- [ ] Q4 Choose $\epsilon$ so that $c(t) = \varphi(p) + ta$ stays in $\varphi(U)$.
- [ ] Q5 Conclude $D = D_\gamma$.
- [ ] Q6 **[why]** Why is $D_\gamma$ a derivation (write it as $\gamma_{*0}(d/dt|_0)$)? Why must $\gamma$ be smooth and not just continuous?
- [ ] Q7 Is $\gamma$ unique? What data of $\gamma$ does $D_\gamma$ depend on?

> [!tip]- Hints: definitions, results, strategy
> **Topic and definitions.** Germs [[§27 Germs#^def-27-2|Def §27.2]]; derivation at a point [[§28 Derivations and the Abstract Tangent Space#^def-28-1|Def §28.1]]; abstract tangent space [[§28 Derivations and the Abstract Tangent Space#^def-28-2|Def §28.2]]; coordinate functions/derivations [[§29 Coordinate Derivations and the Basis Theorem#^def-29-1|Def §29.1]], [[§29 Coordinate Derivations and the Basis Theorem#^def-29-2|Def §29.2]]; smooth curve, velocity [[§31 Tangent Vectors as Velocities of Curves#^def-31-1|Def §31.1]], [[§31 Tangent Vectors as Velocities of Curves#^def-31-2|Def §31.2]].
>
> **Key results.** Basis theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|Thm §29.6]]; velocity in coordinates [[§31 Tangent Vectors as Velocities of Curves#^prop-31-1|Prop §31.1]]; [[§31 Tangent Vectors as Velocities of Curves#^thm-31-2|Thm §31.2]] (this problem); pushforward is a derivation [[§28 Derivations and the Abstract Tangent Space#^prop-28-5|Prop §28.5]]; chain rule [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|Thm §28.6]].
>
> **Strategy (S9).** A derivation is determined by $a^i = D[x^i]$; take the straight line $c(t) = \varphi(p) + ta$ in the chart and $\gamma = \varphi^{-1}\circ c$.
>
> **Difficulty 1.** Submitted solution: treats the basis vectors first, then the general case; the notes keep only the general argument (it contains the basis case).

### HW3.3 The cotangent space as $I_p/I_p^2$

*Parts: (a), (b).*

^hw3-3

#### (a)

Explain why $T_pM \times (I_p/I_p^2) \to \mathbb{R}$, $(v, {[}[f]{]}) \mapsto v(f)$, is well defined.

^hw3-3-a

- [ ] Q1 **[def]** Define $I_p$, $I_p^2$, and the class ${[}[f]{]}$. Show $I_p^2$ is a subspace of $I_p$.
- [ ] Q2 Show $v(I_p^2) = 0$ for every derivation $v$.
- [ ] Q3 Explain why Q2 is exactly the well-definedness (universal property of the quotient vector space).

> [!tip]- Hint (a): strategy
> **Strategy (S2).** Leibniz: $v(uw) = v(u)w(p) + u(p)v(w) = 0$ for $u, w \in I_p$, so $v$ kills $I_p^2$ and descends.

#### (b)

Show the (bilinear) pairing is non-degenerate, hence $I_p/I_p^2 \cong (T_pM)^*$; the isomorphism does not depend on a chart.

^hw3-3-b

- [ ] Q4 **[def]** State both halves of "non-degenerate pairing".
- [ ] Q5 Show $v([1]) = 0$ and then left non-degeneracy.
- [ ] Q6 State Hadamard's lemma (with the formula $f_i(a) = \partial f/\partial r^i(a)$) and prove right non-degeneracy.
- [ ] Q7 Show a non-degenerate pairing of finite-dimensional spaces gives $V \cong W^*$: which half gives which inequality of dimensions?
- [ ] Q8 Alternatively, show ${[}[x^i - x^i(p)]{]} \mapsto$ the dual basis of $\{\partial/\partial x^j|_p\}$.
- [ ] Q9 **[why]** Why is the isomorphism chart-independent although a chart was used? Why is one half of non-degeneracy not enough without finite dimension (the remark after Thm §21.5)?

> [!tip]- Hint (b): strategy
> **Strategy (S9, S7).** Left: a derivation vanishing on $I_p$ and on constants is $0$. Right: if all first partials of $f \in I_p$ vanish, Hadamard writes $f = \sum (x^i - x^i(p))f_i$ with $f_i(p) = 0$, so $f \in I_p^2$. Then the pairing theorem (or the dual basis ${[}[x^i - x^i(p)]{]}$).

> [!tip]- Hints: definitions and results for the whole problem
> **Topic and definitions.** $I_p$ and $I_p^2$ [[§28 Derivations and the Abstract Tangent Space#^def-28-3|Def §28.3]], [[§28 Derivations and the Abstract Tangent Space#^def-28-4|Def §28.4]]; quotient vector space [[§21 Linear Algebra Toolkit#^def-21-6|Def §21.6]]; $I_p/I_p^2$ [[§34 The Cotangent Space from Germs#^def-34-1|Def §34.1]]; bilinear and non-degenerate pairing [[§21 Linear Algebra Toolkit#^def-21-4|Def §21.4]], [[§21 Linear Algebra Toolkit#^def-21-5|Def §21.5]]; dual space and dual basis [[§21 Linear Algebra Toolkit#^def-21-1|Def §21.1]], [[§21 Linear Algebra Toolkit#^def-21-2|Def §21.2]]; cotangent space [[§32 The Cotangent Space#^def-32-4|Def §32.4]]; the pairing [[§34 The Cotangent Space from Germs#^def-34-2|Def §34.2]].
>
> **Key results.** [[§28 Derivations and the Abstract Tangent Space#^lem-28-1|Lem §28.1]]; derivations kill constants [[§28 Derivations and the Abstract Tangent Space#^lem-28-2|Lem §28.2]]; universal property of quotient vector spaces [[§21 Linear Algebra Toolkit#^prop-21-6|Prop §21.6]]; non-degenerate pairings [[§21 Linear Algebra Toolkit#^thm-21-5|Thm §21.5]]; Hadamard's lemma [[§29 Coordinate Derivations and the Basis Theorem#^lem-29-3|Lem §29.3]]; second-order vanishing [[§34 The Cotangent Space from Germs#^prop-34-1|Prop §34.1]]; basis of $I_p/I_p^2$ [[§34 The Cotangent Space from Germs#^prop-34-2|Prop §34.2]]; [[§34 The Cotangent Space from Germs#^prop-34-3|Prop §34.3]], [[§34 The Cotangent Space from Germs#^thm-34-4|Thm §34.4]] (this problem).
>
> **Difficulty** (a) 1, (b) 2. Submitted solution: proves the isomorphism by injectivity (right non-degeneracy) plus surjectivity (dual basis), rather than the dimension-count pairing theorem; the notes discuss both routes after Thm §34.4.

### HW3.4 The moment map on $\mathbb{CP}^n$

*Parts: (a), (b), (c).*

^hw3-4

#### (a)

$F([z_0,\ldots,z_n]) = (|z_1|^2/|z|^2, \ldots, |z_n|^2/|z|^2)$. Prove $F$ is well defined and smooth.

^hw3-4-a

- [ ] Q1 **[def]** Define smoothness of $F : \mathbb{CP}^n \to \mathbb{R}^n$ through charts.
- [ ] Q2 Show $F(\lambda z) = F(z)$.
- [ ] Q3 Compute $F \circ \varphi_0^{-1}(w) = (|w_j|^2/(1+|w|^2))_j$. What changes in $\varphi_j$, $j \ge 1$?
- [ ] Q4 **[why]** Why is one chart computation not enough to conclude smoothness everywhere?

> [!tip]- Hint (a): strategy
> **Strategy (S2, S1).** Scale invariance; in each chart $F\circ\varphi_j^{-1}$ is rational with denominator $\ge 1$.

#### (b)

Show the image of $F$ is the closed simplex $\Delta = \{t_j \ge 0, \sum t_j \le 1\}$.

^hw3-4-b

- [ ] Q5 Show $\sum_j t_j = 1 - |z_0|^2/|z|^2$, hence $F(\mathbb{CP}^n) \subseteq \Delta$.
- [ ] Q6 Given $t \in \Delta$, produce a preimage (real square roots).

#### (c)

For $c$ in the interior of $\Delta$, $dF_p$ is surjective for every $p \in F^{-1}(c)$.

^hw3-4-c

- [ ] Q7 Show the interior of $\Delta$ is $\{t_j > 0, \sum t_j < 1\}$, and that every $p \in F^{-1}(c)$ has all $z_j \neq 0$.
- [ ] Q8 Explain why $dF_p$ is onto iff the Jacobian of $F\circ\varphi_0^{-1}$ at $\varphi_0(p)$ has rank $n$ (Thm §30.2).
- [ ] Q9 Compute $\partial F^j_\varphi/\partial u_k = \frac{2u_k}{S^2}(\delta_{jk}S - |w_j|^2)$, and the $v_k$ analogue, with $S = 1 + |w|^2$.
- [ ] Q10 Show the rank is $n$ using $w_k \neq 0$. (Shortcut to try: $F\circ\varphi_0^{-1} = \Phi \circ Q$ with $Q(w) = (|w_1|^2,\ldots,|w_n|^2)$ and $\Phi(s) = s/(1+\sum s_l)$; why is $\Phi$ a local diffeomorphism?)
- [ ] Q11 **[why]** What fails at a boundary point of $\Delta$ (some $c_j = 0$, or $\sum c_j = 1$)? Is $F$ submersive there?

> [!tip]- Hint (c): strategy
> **Strategy (S1, S9).** Interior ⇒ all $z_j \neq 0$ ⇒ the fibre lies in $U_0$; the Jacobian of $F \circ \varphi_0^{-1}$ has rank $n$ there.

> [!tip]- Hints: definitions and results for the whole problem
> **Topic and definitions.** Smooth map [[§19 Smooth Functions and Smooth Maps#^def-19-3|Def §19.3]]; standard charts [[§18 Projective Spaces as Smooth Manifolds#^def-18-2|Def §18.2]]; differential (pushforward) [[§28 Derivations and the Abstract Tangent Space#^def-28-6|Def §28.6]]; rank, regular value [[§30 The Differential in Coordinates#^def-30-2|Def §30.2]], [[§30 The Differential in Coordinates#^def-30-4|Def §30.4]].
>
> **Key results.** [[§18 Projective Spaces as Smooth Manifolds#^thm-18-2|Thm §18.2]]; matrix of the differential [[§30 The Differential in Coordinates#^thm-30-2|Thm §30.2]]; partials upstairs/downstairs [[§30 The Differential in Coordinates#^prop-30-1|Prop §30.1]]; regular values inside one chart [[§30 The Differential in Coordinates#^prop-30-8|Prop §30.8]] and [[§30 The Differential in Coordinates#^rem-30-6|Remark: The Strategy]] (this problem); [[§30 The Differential in Coordinates#^cor-30-9|Cor §30.9]].
>
> **Difficulty** (a) 1, (b) 1, (c) 2. Submitted solution: long "matching coefficients" derivation of the Jacobian; the rank argument factors columns as $u_k\eta_k$, $v_k\eta_k$ and proves the $\eta_k$ independent by summing the equations ($\sigma = \sum a_k = 0$). The notes cite it as the model case of Prop §30.8.

### HW3.5 Critical points of $f_A$ on $\mathbb{RP}^2$ (not integrated in the notes)

*Parts: (a), (b).*

^hw3-5

#### (a)

$A = \mathrm{diag}(\lambda_1,\lambda_2,\lambda_3)$, $\lambda_1<\lambda_2<\lambda_3$, $f_A(\ell) = \langle Av,v\rangle/\|v\|^2$, $v \in \ell\setminus 0$. In the canonical chart $\varphi_0 = (x^1,x^2)$ on $U_0$ (Tu §7.7) compute $\partial f_A/\partial x^i$, show they vanish at $\ell \in U_0$ iff $\ell = [1:0:0]$; then by symmetry find all critical points.

^hw3-5-a

- [ ] Q1 **[def]** Define a critical point of $f : M \to \mathbb{R}$. Why is "$df_p = 0$" equivalent to "all partials vanish in some chart", and why is it chart-independent?
- [ ] Q2 Show $f_A$ is well defined on $\mathbb{RP}^2$.
- [ ] Q3 Compute $f_A\circ\varphi_0^{-1}(r) = \dfrac{\lambda_1 + \lambda_2 (r^1)^2 + \lambda_3 (r^2)^2}{1 + (r^1)^2 + (r^2)^2}$ and its partials.
- [ ] Q4 Solve "both partials $= 0$" using $\lambda_1 < \lambda_2 < \lambda_3$.
- [ ] Q5 Symmetry: for a permutation matrix $P$, show $[v] \mapsto [Pv]$ is a diffeomorphism with $f_A \circ \bar P = f_{P^{\mathsf T}AP}$; deduce the critical points in $U_1$ and $U_2$ from Q4. (After permuting, the diagonal entries are no longer in increasing order: check that the conclusion of Q4 holds whenever the three entries are merely distinct.)
- [ ] Q6 Identify the maximum, minimum and the third critical point. Why must a function on compact $\mathbb{RP}^2$ have at least two critical points?
- [ ] Q7 **[why]** What is the critical set if $\lambda_1 = \lambda_2 < \lambda_3$? Are the critical points still isolated?

> [!tip]- Hint (a): strategy
> **Strategy (S1, S15).** Compute in one chart; permuting coordinates is a diffeomorphism of $\mathbb{RP}^2$ that conjugates $f_A$ to $f_{A'}$ with permuted eigenvalues.

#### (b)

$A$ symmetric with distinct eigenvalues. Conjecture the critical points of $f_A$ and prove it by diagonalizing $A$ with an orthogonal $g$.

^hw3-5-b

- [ ] Q8 State the conjecture (the three eigenlines).
- [ ] Q9 Show $f_A = f_D \circ G$ with $D = g^{\mathsf T}Ag$.
- [ ] Q10 Show $G$ is a diffeomorphism of $\mathbb{RP}^2$ (coordinate representations are ratios of affine functions; inverse $[v] \mapsto [gv]$).
- [ ] Q11 Use the chain rule to show $\ell$ is critical for $f_A$ iff $G(\ell)$ is critical for $f_D$.
- [ ] Q12 **[why]** Where are "symmetric" and "orthogonal" used? What breaks for a non-symmetric $A$ with real distinct eigenvalues?

> [!tip]- Hint (b): strategy
> **Strategy (S15, S14).** $f_A = f_D \circ G$ with $G([v]) = [g^{\mathsf T}v]$ a diffeomorphism; critical points correspond under $G$ (chain rule).

> [!tip]- Hints: definitions and results for the whole problem
> **Topic and definitions.** Real projective space and its charts [[§18 Projective Spaces as Smooth Manifolds#^cor-18-5|Cor §18.5]]; smooth function [[§19 Smooth Functions and Smooth Maps#^def-19-2|Def §19.2]]; coordinate derivations [[§29 Coordinate Derivations and the Basis Theorem#^def-29-2|Def §29.2]]; regular and critical points [[§36 Submersions#^def-36-3|Def §36.3]]; critical set [[§36 Submersions#^def-36-5|Def §36.5]].
>
> **Key results.** Critical points of real-valued functions [[§36 Submersions#^prop-36-2|Prop §36.2]]; local extrema are critical [[§36 Submersions#^prop-36-3|Prop §36.3]]; matrix of the differential [[§30 The Differential in Coordinates#^thm-30-2|Thm §30.2]]; chain rule [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|Thm §28.6]]; diffeomorphisms induce isomorphisms [[§28 Derivations and the Abstract Tangent Space#^cor-28-7|Cor §28.7]].
>
> **Difficulty 2.** Submitted solution: (a) computes directly in all three charts rather than using the symmetry argument; (b) proves continuity of $G$ via the open quotient map $\mathbb{R}^3\setminus 0 \to \mathbb{RP}^2$ pushing bases forward. No box in the notes is built from this problem.
>
> ---
>
> ## Assignment 4 (due 10/4)

### HW4.1 Zero differential implies constant

$F : M \to N$ smooth with $F_{*,p} = 0$ for all $p$, $M$ connected. Prove $F$ is constant.

^hw4-1

- [ ] Q1 **[def]** Define $F_{*,p}$ and write its matrix in coordinate bases.
- [ ] Q2 Choose charts with $F(U_0) \subseteq V$ and $\varphi(U_0)$ a ball. Why can you?
- [ ] Q3 Show the Jacobian of $\psi\circ F\circ\varphi^{-1}$ vanishes on the ball, hence (MVT on each component along a segment) $F$ is constant on $U_0$.
- [ ] Q4 Show $\{p : F(p) = F(p_0)\}$ is open and closed. (Which property of $N$ makes it closed in one line?)
- [ ] Q5 **[why]** Why is connectedness needed? Why a ball (convex) rather than an arbitrary chart domain?

> [!tip]- Hints: definitions, results, strategy
> **Topic and definitions.** Differential [[§28 Derivations and the Abstract Tangent Space#^def-28-6|Def §28.6]]; matrix of the differential [[§30 The Differential in Coordinates#^thm-30-2|Thm §30.2]].
>
> **Key results.** [[§30 The Differential in Coordinates#^prop-30-10|Prop §30.10]] (this problem); chart mapped into a chart [[§19 Smooth Functions and Smooth Maps#^lem-19-3|Lem §19.3]]; connectedness [[§1 Point-Set Topology Review#^prop-1-7|Prop §1.7]].
>
> **Strategy (S1, S13).** In a chart ball the Jacobian of the coordinate representation vanishes, so (MVT along segments) $F$ is locally constant; locally constant + connected ⇒ constant.
>
> **Difficulty 1.** Submitted solution: builds $C$ as the union of all neighbourhoods of $p_0$ on which $F$ is constant and shows it is clopen. Shorter: $F^{-1}(F(p_0))$ is closed because points of $N$ are closed.

### HW4.2 No submersion from a compact manifold to $\mathbb{R}^k$

Show that if $M$ is compact there is no submersion $F : M \to \mathbb{R}^k$ for any $k$.

^hw4-2

- [ ] Q1 **[def]** Define a submersion.
- [ ] Q2 Prove submersions are open maps from the local normal form.
- [ ] Q3 Show $F(M)$ is closed.
- [ ] Q4 Conclude $F(M) = \mathbb{R}^k$ and derive the contradiction.
- [ ] Q5 **[why]** Where are compactness, $k \ge 1$ and $M \neq \emptyset$ used? What happens for $k = 0$? For non-compact $M$?
- [ ] Q6 State the general version (Thm §36.10). Why does the torus admit a submersion onto $S^1$?

> [!tip]- Hints: definitions, results, strategy
> **Topic and definitions.** Submersion [[§36 Submersions#^def-36-1|Def §36.1]]; compactness facts [[§1 Point-Set Topology Review#^prop-1-8|Prop §1.8]].
>
> **Key results.** Local normal form for submersions [[§36 Submersions#^thm-36-6|Thm §36.6]]; submersions are open maps [[§36 Submersions#^cor-36-9|Cor §36.9]]; [[§36 Submersions#^thm-36-10|Thm §36.10]], [[§36 Submersions#^cor-36-11|Cor §36.11]] (this problem).
>
> **Strategy (S12, S13).** $F(M)$ is open (submersion), closed (compact in Hausdorff), nonempty; $\mathbb{R}^k$ connected ⇒ $F(M) = \mathbb{R}^k$, which is not compact.
>
> **Difficulty 1.** Submitted solution: short; notes the $k = 0$ and $M = \emptyset$ edge cases.

### HW4.3 Unit quaternions, $SU(2)$ and the double cover of $SO(3)$

*Parts: (a), (b).*

^hw4-3

#### (a)

With $\vec e_1,\vec e_2,\vec e_3$ a basis of $T_1S^3$, compute $\sigma_j := dF_1(\vec e_j)$ (hint: curves, not coordinates).

^hw4-3-a

- [ ] Q1 **[def]** Write the matrix of $R_q$ on $\mathbb{C}^2$ and the formula for $F(x)$, $x \in S^3$.
- [ ] Q2 Show $T_1S^3 = \{x_0 = 0\}$ (level set of $|x|^2$, kernel of the gradient).
- [ ] Q3 State the "velocity of a composite" rule $F_*(\gamma'(0)) = (F\circ\gamma)'(0)$.
- [ ] Q4 Compute $\sigma_1, \sigma_2, \sigma_3$. (Observe that $F$ is the restriction of a real-linear map $L$, so $dF_1 = L|_{T_1S^3}$.)
- [ ] Q5 Check $\sigma_j$ is traceless and skew-Hermitian, i.e. lies in $\mathfrak{su}(2)$.

> [!tip]- Hint (a): strategy
> **Strategy (S10).** $\gamma_j(t) = \cos t + \sin t\,u_j$ ($u_j = i, j, k$) has velocity $\vec e_j$; $\sigma_j = \frac{d}{dt}\big|_0 F(\gamma_j(t))$.

#### (b)

Conjugation gives a 2–1 group morphism $S^3 \to SO(3)$ (assume these facts), hence a 2–1 map $G : SU(2) \to SO(3)$. Compute $dG_I(\sigma_j)$ and verify $G$ is a local diffeomorphism.

^hw4-3-b

- [ ] Q6 Why does $G \circ F = C$ give $dG_I \circ dF_1 = dC_1$?
- [ ] Q7 Show $C(\gamma_j(t))$ is the rotation by $2t$ about the $j$-th axis; differentiate to get $2\hat e_j$.
- [ ] Q8 Show $dG_I$ is an isomorphism (independence + $\dim = 3$).
- [ ] Q9 Show $dG_g$ is an isomorphism for every $g$ via the translation identity.
- [ ] Q10 **[def]** Define a local diffeomorphism and state the inverse function theorem on manifolds.
- [ ] Q11 **[why]** Why is "$dG_I$ invertible" alone not enough without the homomorphism property? Why can $G$ not be a global diffeomorphism?

> [!tip]- Hint (b): strategy
> **Strategy (S14, S15, S8).** $G \circ F = C$ gives $dG_I(\sigma_j) = \frac{d}{dt}|_0 C(\gamma_j(t))$; $dG_I$ is an isomorphism; translate to every $g$ by $G\circ L_g = L_{G(g)}\circ G$; then the inverse function theorem.

> [!tip]- Hints: definitions and results for the whole problem
> **Topic and definitions.** Quaternions [[§45 The Unit Quaternions and SU(2)#^def-45-1|Def §45.1]]; velocity [[§31 Tangent Vectors as Velocities of Curves#^def-31-2|Def §31.2]]; local diffeomorphism [[§35 Local Diffeomorphisms#^def-35-1|Def §35.1]]; hat map [[§25 The Geometric Tangent Space#^def-25-3|Def §25.3]].
>
> **Key results.** $S^3 \cong SU(2)$ [[§45 The Unit Quaternions and SU(2)#^prop-45-5|Prop §45.5]]; tangent space at the identity [[§45 The Unit Quaternions and SU(2)#^prop-45-6|Prop §45.6]] (part (a)); computing differentials by curves [[§31 Tangent Vectors as Velocities of Curves#^cor-31-3|Cor §31.3]]; conjugation is rotation [[§46 SU(2) → SO(3)꞉ The Double Cover#^prop-46-1|Prop §46.1]]; translating the differential [[§46 SU(2) → SO(3)꞉ The Double Cover#^lem-46-3|Lem §46.3]]; [[§46 SU(2) → SO(3)꞉ The Double Cover#^thm-46-4|Thm §46.4]] (part (b)); inverse function theorem [[§35 Local Diffeomorphisms#^thm-35-1|Thm §35.1]]; local diffeomorphisms detected by the differential [[§35 Local Diffeomorphisms#^thm-35-2|Thm §35.2]]; tangent space of a sphere [[§25 The Geometric Tangent Space#^ex-25-1|Ex §25.1]].
>
> **Difficulty 3.** Submitted solution: very long. It builds hyperspherical adapted charts to prove $S^3$ and $SU(2)$ are submanifolds and to compute $T_1S^3$, where the RVT for $|x|^2 = 1$ does it in one line. Results: $\sigma_1 = \begin{pmatrix} -i & 0\\ 0 & i\end{pmatrix}$, $\sigma_2 = \begin{pmatrix} 0 & 1\\ -1 & 0\end{pmatrix}$, $\sigma_3 = \begin{pmatrix} 0 & -i\\ -i & 0\end{pmatrix}$, and $dG_I(\sigma_j) = 2\hat e_j$. It takes as given that $SO(3)$ is a 3-dimensional submanifold. The notes (§45–§46) reorganize it and prove the facts the problem allowed to be assumed.

### HW4.4 Local sections and trivializations of the Hopf fibration

$\Pi : S^{2n+1} \to \mathbb{CP}^n$, $U_i$ as in HW2.2. Show there is a smooth $s_i : U_i \to \Pi^{-1}(U_i)$ with $\Pi\circ s_i = 1_{U_i}$, and use it to build an equivariant diffeomorphism $\Phi_i : \Pi^{-1}(U_i) \to U_i \times S^1$ over $U_i$; i.e. $\Pi$ is a fibration with fibre $S^1$. (Hint: $\Phi_i\circ s_i$ is $u \mapsto (u,1)$; extend by equivariance.)

^hw4-4

- [ ] Q1 **[def]** Define a fibration with fibre $F$, a local trivialization, a local section, and an equivariant map.
- [ ] Q2 Define $s_i(u) = v_i(u)/|v_i(u)|$, $v_i(u) = z/z_i$. Show it is well defined, smooth and $\Pi\circ s_i = \mathrm{id}$.
- [ ] Q3 Show each $z \in \Pi^{-1}(U_i)$ is $\lambda\,s_i(\Pi(z))$ for a unique $\lambda \in S^1$, namely $z_i/|z_i|$.
- [ ] Q4 Write $\Phi_i$ and $\Psi_i$, check they are inverse, equivariant, and that $\mathrm{pr}_1\circ\Phi_i = \Pi$.
- [ ] Q5 Justify smoothness of $\Phi_i$, $\Psi_i$ (maps into the submanifolds $S^{2n+1}$ and $S^1$).
- [ ] Q6 **[why]** Why only local sections: why is there no global section for $n \ge 1$ (Cor §44.2)?
- [ ] Q7 **[why]** Why is the second component $z_i/|z_i|$ rather than $z_i$, and why must $s_i(u)$ have positive real $i$-th entry for $\Phi_i\circ s_i = (\cdot, 1)$?

> [!tip]- Hints: definitions, results, strategy
> **Topic and definitions.** Fibration [[§38 Fibrations#^def-38-1|Def §38.1]]; trivial fibration [[§38 Fibrations#^def-38-2|Def §38.2]]; section, local section [[§38 Fibrations#^def-38-3|Def §38.3]], [[§38 Fibrations#^def-38-4|Def §38.4]]; Hopf fibration [[§44 Projective Spaces and the Hopf Fibration#^ex-44-3|Ex §44.3]]; standard charts [[§18 Projective Spaces as Smooth Manifolds#^def-18-2|Def §18.2]].
>
> **Key results.** Local sections give trivializations [[§44 Projective Spaces and the Hopf Fibration#^prop-44-1|Prop §44.1]]; [[§44 Projective Spaces and the Hopf Fibration#^cor-44-2|Cor §44.2]] (this problem; no global section); trivializations give sections [[§38 Fibrations#^prop-38-4|Prop §38.4]]; [[§39 Examples of Fibrations#^rem-39-1|Remark: Where Explicit Trivializations Come From]]; smooth maps into submanifolds [[§37 Regular Submanifolds#^lem-37-5|Lem §37.5]]; product manifolds [[§19 Smooth Functions and Smooth Maps#^prop-19-11|Prop §19.11]].
>
> **Strategy (S15).** Lift with the chart ($z/z_i$), normalize to the sphere; every point of $\Pi^{-1}(U_i)$ is uniquely $\lambda s_i(u)$, which gives $\Phi_i(z) = (\Pi(z), z_i/|z_i|)$ with inverse $(u,\lambda) \mapsto \lambda s_i(u)$.
>
> **Difficulty 2.** Submitted solution: explicit formulas and separate smoothness checks for $\pi_1$, $\Pi$, both components. The notes add an inner-product formula for the inverse that works for any local section.

### HW4.5 The irrational line on the torus

*Parts: (a), (b).*

^hw4-5

#### (a)

$\alpha$ irrational, $\gamma(t) = (e^{2\pi i t}, e^{2\pi i\alpha t})$. Verify $\gamma$ is an immersion.

^hw4-5-a

- [ ] Q1 **[def]** Define an immersion; what does it mean for a curve?
- [ ] Q2 Compute $(\iota\circ\gamma)'(t)$ and explain why $d\gamma_t(\partial_t) \neq 0$.

> [!tip]- Hint (a): strategy
> **Strategy (S14).** $(\iota\circ\gamma)'(t) \neq 0$ in $\mathbb{C}^2$; the chain rule through the inclusion gives $d\gamma_t \neq 0$.

#### (b)

Show the image of $\gamma$ is dense in $T$, and deduce $\gamma$ is not an embedding (Lee Ex. 4.20, Lem. 4.21).

^hw4-5-b

- [ ] Q3 **[def]** Define an embedding.
- [ ] Q4 Show $\gamma$ is injective (irrationality).
- [ ] Q5 State Dirichlet's lemma and show $\gamma(n_N) \to \gamma(0)$ with $n_N \ge 1$.
- [ ] Q6 Show $\{e^{2\pi i\alpha k}\}_{k\in\mathbb{Z}}$ is dense in $S^1$ (powers of $w_N = e^{i\theta_N}$ with $0 < |\theta_N| < 2\pi/N$), and deduce $\gamma(\mathbb{R})$ dense.
- [ ] Q7 Show $\gamma^{-1} : \gamma(\mathbb{R}) \to \mathbb{R}$ is not continuous.
- [ ] Q8 Second proof: images of embeddings are locally closed (Prop §42.7); a dense locally closed set is open (Cor §42.8). Why is $\gamma(\mathbb{R})$ not open in $T$?
- [ ] Q9 **[why]** What if $\alpha$ is rational? Is $\gamma$ injective; what is its image?

> [!tip]- Hint (b): strategy
> **Strategy (S14).** Dirichlet gives integers $n_N \ge 1$ with $\gamma(n_N) \to \gamma(0)$; powers of a small rotation are dense in $S^1$; $\gamma^{-1}$ sends $\gamma(n_N) \to \gamma(0)$ to $n_N \not\to 0$.

> [!tip]- Hints: definitions and results for the whole problem
> **Topic and definitions.** Immersion [[§41 Immersions#^def-41-1|Def §41.1]]; embedding [[§42 Embeddings#^def-42-1|Def §42.1]]; locally closed [[§42 Embeddings#^def-42-3|Def §42.3]]; immersed submanifold [[§42 Embeddings#^def-42-4|Def §42.4]].
>
> **Key results.** Dirichlet [[§42 Embeddings#^lem-42-11|Lem §42.11]]; [[§42 Embeddings#^prop-42-12|Prop §42.12]] (this problem); images of embeddings are locally closed [[§42 Embeddings#^prop-42-7|Prop §42.7]]; dense regular submanifolds are open [[§42 Embeddings#^cor-42-8|Cor §42.8]]; [[§42 Embeddings#^ex-42-1|Ex §42.1]]; injective immersion that is not a homeomorphism onto its image [[§41 Immersions#^ex-41-2|Ex §41.2]].
>
> **Difficulty** (a) 1, (b) 2. Submitted solution: proves Dirichlet-based density in full; non-embedding by the sequence $n_N$. The notes add the locally-closed proof.
>
> ---
>
> ## Assignment 5 (due 10/11)

### HW5.1 Sections are embeddings

Let $\pi : E \to M$ be a surjective submersion. Show any section $s : M \to E$ ($\pi\circ s = 1_M$) is an embedding.

^hw5-1

- [ ] Q1 **[def]** Define embedding and section.
- [ ] Q2 Show $s$ is injective.
- [ ] Q3 Show $\pi|_{s(M)}$ is a continuous inverse of $s : M \to s(M)$ (subspace topology).
- [ ] Q4 Differentiate $\pi\circ s = \mathrm{id}_M$ and conclude $s_{*p}$ is injective.
- [ ] Q5 **[why]** Which hypotheses are actually used? Are "surjective" and "submersion" needed?
- [ ] Q6 Show $s(M) = \{y : s(\pi(y)) = y\}$ is closed in $E$. What property of $E$ does that use?
- [ ] Q7 Show $T_{s(p)}E = \operatorname{im} s_{*p} \oplus \ker \pi_{*s(p)}$.

> [!tip]- Hints: definitions, results, strategy
> **Topic and definitions.** Section [[§38 Fibrations#^def-38-3|Def §38.3]]; immersion [[§36 Submersions#^def-36-2|Def §36.2]]; embedding [[§42 Embeddings#^def-42-1|Def §42.1]]; vertical space [[§38 Fibrations#^def-38-5|Def §38.5]].
>
> **Key results.** [[§42 Embeddings#^prop-42-10|Prop §42.10]] (this problem: sections are closed embeddings); splitting along a section [[§38 Fibrations#^prop-38-5|Prop §38.5]]; chain rule [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|Thm §28.6]].
>
> **Strategy (S14).** Differentiate $\pi\circ s = \mathrm{id}$: $\pi_*\circ s_* = \mathrm{id}$, so $s_*$ is injective; $\pi|_{s(M)}$ is a continuous inverse of $s$ onto its image.
>
> **Difficulty 1.** Submitted solution: short and complete. The notes observe it only uses $\pi\circ s = \mathrm{id}$, and add closedness.

### HW5.2 Transversality to a regular submanifold

$F : M \to N$ smooth, $S \subset N$ a regular submanifold, $F$ transverse to $S$: $\mathrm{Image}(dF_p) + T_{F(p)}S = T_{F(p)}N$ for $p \in F^{-1}(S)$. Show $F^{-1}(S)$ is a regular submanifold of $M$; give its codimension and its tangent spaces. (Hint: an earlier homework problem.)

^hw5-2

- [ ] Q1 **[def]** Define a regular submanifold, an adapted chart, and the codimension.
- [ ] Q2 In an adapted chart $(x_a, x_b)$, show $x_b$ is a submersion with $x_b^{-1}(0) = U\cap S$ and $\ker(x_b)_{*q} = T_qS$.
- [ ] Q3 Show $(x_b\circ F)_{*p}$ is surjective using transversality.
- [ ] Q4 Apply the RVT (or the submersion normal form at $p$) to $x_b\circ F$ to get a chart of $M$ adapted to $F^{-1}(S)$. What is the codimension?
- [ ] Q5 Show $T_pF^{-1}(S) \subseteq (F_{*p})^{-1}(T_{F(p)}S)$ by the chain rule, then equality by counting dimensions.
- [ ] Q6 Special cases: $S$ a point (regular value theorem); $F$ the inclusion of a submanifold (transverse intersection of submanifolds). What do they say?
- [ ] Q7 **[why]** Why is the condition imposed only at points of $F^{-1}(S)$? Give a non-transverse example where $F^{-1}(S)$ is not a submanifold.

> [!tip]- Hints: definitions, results, strategy
> **Topic and definitions.** Regular submanifold [[§37 Regular Submanifolds#^def-37-2|Def §37.2]]; adapted chart [[§37 Regular Submanifolds#^def-37-3|Def §37.3]]; transversality to a submanifold [[§37 Regular Submanifolds#^def-37-5|Def §37.5]]; normal space [[§37 Regular Submanifolds#^def-37-6|Def §37.6]].
>
> **Key results.** [[§37 Regular Submanifolds#^thm-37-15|Thm §37.15]] (this problem); adapted charts give local defining maps [[§37 Regular Submanifolds#^prop-37-7|Prop §37.7]]; level sets near a regular point [[§37 Regular Submanifolds#^lem-37-11|Lem §37.11]]; RVT for manifolds [[§37 Regular Submanifolds#^thm-37-12|Thm §37.12]]; submersion normal form [[§36 Submersions#^thm-36-6|Thm §36.6]]; tangent spaces of a regular submanifold [[§37 Regular Submanifolds#^prop-37-6|Prop §37.6]]; [[§37 Regular Submanifolds#^prop-37-16|Prop §37.16]], special cases [[§37 Regular Submanifolds#^cor-37-17|Cor §37.17]]; HW2.5 = [[§26 Transversality#^thm-26-1|Thm §26.1]].
>
> **Strategy (S12, S11, S8, S6).** Locally $S = x_b^{-1}(0)$ with $x_b$ a submersion; transversality makes $x_b\circ F$ a submersion at $p$ (the HW2.5 lifting); RVT or normal form gives an adapted chart; tangent space by "$\subseteq$ + dimension count".
>
> **Difficulty 2.** Submitted solution: complete but long (explicit translation and permutation of the normal-form chart). The notes record two completed steps: the normal form is applied at a single point, and $\ker(x_b)_*$ is computed directly (now Prop §37.7 and Lem §37.11).

### HW5.3 Morse functions and the zero section

*Parts: (a), (b).*

^hw5-3

#### (a)

$s_f(p) = (p, df_p)$; $s_f^{-1}(\mathcal{Z}) = \mathrm{Crit}(f)$. Show $s_f$ is transverse to $\mathcal{Z}$ iff at every critical point the Hessian $H_p = (\partial^2 f/\partial x^i\partial x^j(p))$ is non-degenerate in any coordinate system.

^hw5-3-a

- [ ] Q1 **[def]** Define the zero section, the standard coordinates $(\bar x^j, \xi_j)$ on $T^*M$, and show $\mathcal{Z} = \{\xi = 0\}$ locally (warm-up).
- [ ] Q2 Write $s_f$ in standard coordinates; why is it smooth?
- [ ] Q3 Compute $(s_f)_{*p}(\partial/\partial x^i|_p)$ at a critical point.
- [ ] Q4 Compute $T_{(p,0)}\mathcal{Z}$ inside $T_{(p,0)}T^*M$.
- [ ] Q5 Show the sum is everything iff $\det H_p \neq 0$ (block determinant, or: modulo $T\mathcal{Z}$ only the $\xi$-components matter).
- [ ] Q6 **[why]** Why is non-degeneracy of $H_p$ independent of the chart at a critical point, while the Hessian matrix itself depends on the chart elsewhere (Ex §52.1, Prop §52.2)?
- [ ] Q7 **[why]** Why does transversality only need checking at critical points?

> [!tip]- Hint (a): strategy
> **Strategy (S1, S9, S7).** In standard coordinates $(\bar x, \xi)$: $s_f = (x, \partial f/\partial x)$, $(s_f)_*(\partial_{x^i}) = \partial_{\bar x^i} + \sum_j H_{ij}\partial_{\xi_j}$, $T\mathcal{Z} = \mathrm{span}\{\partial_{\bar x^i}\}$; $2m$ vectors span iff $\det\begin{pmatrix} I & I\\ H & 0\end{pmatrix} = (-1)^m\det H \neq 0$.

#### (b)

$f$ is Morse iff all critical points are non-degenerate. What can you say about the set of critical points of a Morse function?

^hw5-3-b

- [ ] Q8 **[def]** Define a Morse function.
- [ ] Q9 Apply HW5.2 to compute the codimension of $\mathrm{Crit}(f)$.
- [ ] Q10 Show a $0$-dimensional regular submanifold is a discrete set of isolated points.
- [ ] Q11 On a compact $M$, why are there finitely many critical points (Cor §52.12)?
- [ ] Q12 **[why]** For $f(x) = x^3$ on $\mathbb{R}$: is $0$ nondegenerate? Is $s_f$ transverse to $\mathcal{Z}$ there (Ex §52.2)?

> [!tip]- Hint (b): strategy
> **Strategy (S12).** HW5.2: $\mathrm{Crit}(f) = s_f^{-1}(\mathcal{Z})$ is a regular submanifold of codimension $m$, i.e. dimension $0$: discrete.

> [!tip]- Hints: definitions and results for the whole problem
> **Topic and definitions.** Cotangent bundle [[§50 The Cotangent Bundle#^def-50-1|Def §50.1]]; zero section [[§50 The Cotangent Bundle#^def-50-3|Def §50.3]]; charts of $T^*M$ [[§50 The Cotangent Bundle#^def-50-5|Def §50.5]]; Hessian matrix [[§52 Critical Points and the Hessian#^def-52-1|Def §52.1]]; Hessian at a critical point [[§52 Critical Points and the Hessian#^def-52-2|Def §52.2]]; nondegenerate critical point [[§52 Critical Points and the Hessian#^def-52-3|Def §52.3]]; Morse function [[§52 Critical Points and the Hessian#^def-52-4|Def §52.4]]; critical set [[§36 Submersions#^def-36-5|Def §36.5]].
>
> **Key results.** Zero section is a regular submanifold [[§52 Critical Points and the Hessian#^prop-52-5|Prop §52.5]]; Hessian change of coordinates [[§52 Critical Points and the Hessian#^prop-52-2|Prop §52.2]], [[§52 Critical Points and the Hessian#^ex-52-1|Ex §52.1]]; well defined at a critical point [[§52 Critical Points and the Hessian#^prop-52-3|Prop §52.3]]; vertical space along $\mathcal{Z}$ [[§52 Critical Points and the Hessian#^prop-52-8|Prop §52.8]]; $d(df)$ at a critical point [[§52 Critical Points and the Hessian#^prop-52-9|Prop §52.9]]; [[§52 Critical Points and the Hessian#^thm-52-10|Thm §52.10]] (part (a)); [[§52 Critical Points and the Hessian#^ex-52-2|Ex §52.2]]; [[§52 Critical Points and the Hessian#^cor-52-11|Cor §52.11]] (part (b)), [[§52 Critical Points and the Hessian#^cor-52-12|Cor §52.12]]; HW5.2 [[§37 Regular Submanifolds#^thm-37-15|Thm §37.15]].
>
> **Difficulty** (a) 2, (b) 1. Submitted solution: block determinant $\det A_p = (-1)^m\det H_p$, carefully derived $H_{ij} = \partial_{x^i}(\partial f/\partial x^j)$. The notes give a second proof through the vertical splitting along $\mathcal{Z}$ (Prop §52.8) and keep the determinant as the second proof.

### HW5.4 Lagrange multipliers revisited

*Parts: (a), (b).*

^hw5-4

#### (a)

$N_pM = \{\alpha \in T_p^*N : \alpha|_{T_pM} = 0\} = \ker\iota_p^*$. For $f = \iota^*\Phi$, explain why $p$ is critical for $f$ iff $d\Phi_p \in N_pM$.

^hw5-4-a

- [ ] Q1 **[def]** Define the conormal space and the pullback $\iota_p^*$.
- [ ] Q2 Show $df_p = \iota_p^*(d\Phi_p)$.
- [ ] Q3 Conclude, and show the two descriptions of $N_pM$ (annihilator, kernel of $\iota_p^*$) agree.

> [!tip]- Hint (a): strategy
> **Strategy (S14).** Chain rule: $df_p = \iota_p^*(d\Phi_p)$.

#### (b)

$M = G^{-1}(0)$, $G : N \to \mathbb{R}^k$, $0$ a regular value. Prove $\{dG^1_p,\ldots,dG^k_p\}$ is a basis of $N_pM$, and explain how the method of Lagrange multipliers follows.

^hw5-4-b

- [ ] Q4 Show $\dim N_pM = k$ using an adapted chart.
- [ ] Q5 Show $dG^j_p \in N_pM$.
- [ ] Q6 Show the $dG^j_p$ are independent: if $\sum c_j dG^j_p = 0$, pick $v$ with $G_{*p}v = c$.
- [ ] Q7 Derive $d\Phi_p = \sum\lambda_j dG^j_p$ (in $\mathbb{R}^n$: $\nabla\Phi = \sum\lambda_j\nabla G^j$) at critical points; why are the $\lambda_j$ unique?
- [ ] Q8 Why are constrained local extrema critical points of $f$ (curves through $p$)?
- [ ] Q9 **[why]** What fails without "regular value"? Minimize $\Phi(x,y) = x$ on $\{y^2 = x^3\}$ ($G = y^2 - x^3$): where is the minimum, and does $\nabla\Phi = \lambda\nabla G$ hold there?

> [!tip]- Hint (b): strategy
> **Strategy (S7, S6).** $\dim N_pM = k$ (adapted chart); each $dG^j_p \in N_pM$ ($G^j\circ\iota \equiv 0$); independent because $G_{*p}$ is onto; $k$ independent vectors in a $k$-dimensional space.

> [!tip]- Hints: definitions and results for the whole problem
> **Topic and definitions.** Conormal space [[§37 Regular Submanifolds#^def-37-4|Def §37.4]]; pullback of covectors [[§34 The Cotangent Space from Germs#^def-34-3|Def §34.3]]; differential of a function [[§32 The Cotangent Space#^def-32-5|Def §32.5]]; critical point [[§36 Submersions#^def-36-3|Def §36.3]].
>
> **Key results.** Critical points of a restriction [[§37 Regular Submanifolds#^prop-37-18|Prop §37.18]] (part (a)); basis of the conormal space [[§37 Regular Submanifolds#^prop-37-8|Prop §37.8]]; conormal space of a regular level set [[§37 Regular Submanifolds#^prop-37-19|Prop §37.19]] (part (b)); submersions to $\mathbb{R}^k$ and independent differentials [[§36 Submersions#^prop-36-4|Prop §36.4]]; Lagrange multipliers [[§37 Regular Submanifolds#^thm-37-20|Thm §37.20]]; pullback commutes with $d$ [[§34 The Cotangent Space from Germs#^prop-34-6|Prop §34.6]]; local extrema are critical [[§36 Submersions#^prop-36-3|Prop §36.3]]; adapted charts give local defining maps [[§37 Regular Submanifolds#^prop-37-7|Prop §37.7]].
>
> **Difficulty 2.** Submitted solution: gives two independence arguments (Jacobian rank and the coordinate-free "$|c|^2 = 0$" trick); the notes make them the two proofs of Prop §36.4.

### HW5.5 The normal bundle and focal points

*Parts: (a), (b).*

^hw5-5

#### (a)

$M \subset \mathbb{R}^n$ a submanifold of dimension $m < n$, $\mathcal{N} = \{(p,v) : p \in M, v \in (T_pM)^\perp\}$. Show $\mathcal{N}$ is a submanifold of $\mathbb{R}^{2n}$ of dimension $n$. (Hint: adapted coordinates, $X_j = \partial/\partial x^j$, $F(p,v) = (x^{m+1}(p),\ldots,x^n(p), X_1(p)\cdot v,\ldots,X_m(p)\cdot v)$; show $0$ is a regular value.)

^hw5-5-a

- [ ] Q1 **[def]** Define the normal bundle. Why should its dimension be $m + (n - m) = n$?
- [ ] Q2 Show $F^{-1}(0) = \mathcal{N}\cap(U\times\mathbb{R}^n)$, using $T_pM = \mathrm{span}\{X_1(p),\ldots,X_m(p)\}$ for $p \in U\cap M$.
- [ ] Q3 Compute $DF$ in block form.
- [ ] Q4 Show $DF(p,v)$ has rank $n$ everywhere on $U\times\mathbb{R}^n$.
- [ ] Q5 Conclude $\mathcal{N}$ is a regular submanifold, patching over adapted charts.
- [ ] Q6 **[why]** Why is an adapted chart needed? Why not cut $\mathcal{N}$ out globally by "$v$ orthogonal to $T_pM$" with one formula?

> [!tip]- Hint (a): strategy
> **Strategy (S5, S12).** RVT on the hinted $F$; its Jacobian is block triangular with an identity block and the independent rows $X_j(p)^{\mathsf T}$.

#### (b)

$E(p,v) = p + v$; $q$ is a focal point if $q = E(p,v)$ with $dE_{(p,v)}$ not of maximal rank. Parametrize the set of focal points of the parabola $y = x^2$ by a smooth curve $r : \mathbb{R} \to \mathbb{R}^2$.

^hw5-5-b

- [ ] Q7 **[def]** Define the endpoint map and a focal point.
- [ ] Q8 Show $T_pM = \mathrm{span}\{(1,2a)\}$, $(T_pM)^\perp = \mathrm{span}\{(-2a,1)\}$, and that $\Psi$ is a diffeomorphism $\mathbb{R}^2 \to \mathcal{N}$.
- [ ] Q9 Compute $E\circ\Psi$, its Jacobian determinant, and the critical set.
- [ ] Q10 Obtain $r(a)$; locate its cusp.
- [ ] Q11 **[why]** Why is the rank of $dE$ the rank of $D(E\circ\Psi)$? Interpret $\lambda|(-2a,1)|$ as the radius of curvature (remark Focal Points Are Centres of Curvature in §40).

> [!tip]- Hint (b): strategy
> **Strategy (S1).** Global chart $\Psi(a,\lambda) = ((a,a^2), \lambda(-2a,1))$; $\det D(E\circ\Psi) = 1 - 2\lambda + 4a^2$; substitute $\lambda = (1+4a^2)/2$.

> [!tip]- Hints: definitions and results for the whole problem
> **Topic and definitions.** Normal bundle [[§40 The Normal Bundle of a Submanifold of Euclidean Space#^def-40-1|Def §40.1]]; endpoint map [[§40 The Normal Bundle of a Submanifold of Euclidean Space#^def-40-2|Def §40.2]]; focal point [[§40 The Normal Bundle of a Submanifold of Euclidean Space#^def-40-3|Def §40.3]]; adapted chart [[§37 Regular Submanifolds#^def-37-3|Def §37.3]]; regular value [[§30 The Differential in Coordinates#^def-30-4|Def §30.4]].
>
> **Key results.** [[§40 The Normal Bundle of a Submanifold of Euclidean Space#^prop-40-1|Prop §40.1]] (part (a)); adapted chart of a submanifold of $\mathbb{R}^n$ [[§37 Regular Submanifolds#^lem-37-10|Lem §37.10]]; fourth description [[§37 Regular Submanifolds#^prop-37-9|Prop §37.9]]; normal bundle is a fibration [[§40 The Normal Bundle of a Submanifold of Euclidean Space#^prop-40-2|Prop §40.2]]; [[§40 The Normal Bundle of a Submanifold of Euclidean Space#^ex-40-1|Ex §40.1]] (part (b)); focal points are centres of curvature [[§40 The Normal Bundle of a Submanifold of Euclidean Space#^rem-40-1|Remark: Focal Points Are Centres of Curvature]].
>
> **Difficulty** (a) 2, (b) 1. Submitted solution: follows the hint; result $r(a) = (-4a^3, 3a^2 + \tfrac12)$, cusp at $(0, \tfrac12)$ (the evolute). The notes record two completed steps in (a): that the first $m$ coordinate vectors span $T_pM$ (Lem §37.10(3)), and converting the Jacobian from the coordinates $(x, v)$ to standard coordinates of $\mathbb{R}^{2n}$.

## Strategy codes
Codes match the "Strategies" list in `review_spec.md` where they coincide (S1–S13); S14–S15 are additional.

1. **S1 Check in a chart, then show the chart does not matter.** Coordinate representations decide smoothness and rank; transition maps make "some chart" equal "every chart". HW2.2(c), HW3.1, HW3.4(a)(c), HW3.5(a), HW4.1, HW5.3(a), HW5.5(b).
2. **S2 Define on representatives, check well-definedness.** HW2.2(a)(b), HW3.3(a), HW3.4(a), HW3.5(a), HW4.4 ($s_i$ via $z/z_i$).
3. **S3 Maps out of a quotient: the universal property.** HW2.1(a), HW2.2(a)(b); linear version (descend to $V/W$) in HW3.3(a).
4. **S4 Work upstairs in a quotient** (preimages, saturations, open quotient maps push bases forward; diagonal constructions for counterexamples). HW1.4(b), HW1.5, HW2.2(a)(b), HW3.5(b).
5. **S5 Regular value theorem on a well-chosen map.** HW1.6 (the theorem itself), HW2.3, HW2.4, HW2.5 ($G\circ F$), HW5.2 ($x_b\circ F$), HW5.4(b), HW5.5(a).
6. **S6 Tangent space = kernel; prove $\subseteq$, then count dimensions.** HW2.3, HW2.4, HW2.5, HW5.2, HW5.4(b).
7. **S7 Linear algebra closes the gap** (rank–nullity, injective between equal dimensions, $k$ independent vectors in a $k$-dimensional space, non-degenerate pairings). HW2.3, HW3.3(b), HW3.4(c), HW4.3(b), HW5.2, HW5.3(a), HW5.4(b).
8. **S8 Normal forms and the inverse function theorem give charts, openness, local diffeomorphisms.** HW1.6 (IFT), HW4.2 (submersions are open), HW4.3(b) (IFT ⇒ local diffeomorphism), HW5.2 (submersion normal form), HW5.5(b) ($\Psi$ a diffeomorphism).
9. **S9 A derivation is determined by its values on coordinate functions** (basis theorem, Hadamard, matching coefficients). HW3.2, HW3.3(b), HW3.4(c), HW5.3(a).
10. **S10 Compute differentials with curves:** $F_*(\gamma'(0)) = (F\circ\gamma)'(0)$, or $\frac{d}{dt}F(g+th)$. HW2.4, HW3.2, HW4.3(a)(b), HW5.4(b) (extrema are critical).
11. **S12 Transversality = the images span ⇒ a composite is a submersion** (lift through the defining map, split off the kernel). HW2.5, HW5.2, HW5.3(a)(b).
12. **S13 Compactness and Hausdorffness upgrade local to global** (continuous bijection compact → Hausdorff, compact images closed, compact group ⇒ Hausdorff orbit space, finitely many critical points). HW1.3 (failure: non-compact group), HW2.1(b), HW2.2(a), HW4.2, HW5.3(b).
13. **S13′ Connectedness: local property + clopen set ⇒ global.** HW1.1, HW4.1, HW4.2. (Listed under S13 in `review_spec.md` only implicitly; worth naming.)
14. **S14 Differentiate (or invert) an identity; test with sequences.** Chain rule on $\pi\circ s = \mathrm{id}$, $G\circ F = C$, $f_A = f_D\circ G$, $f = \Phi\circ\iota$; sequences detect non-closed graphs, non-unique limits, discontinuous inverses. HW1.2, HW1.3, HW3.5(b), HW4.3(b), HW4.5(a)(b), HW5.1, HW5.4(a).
15. **S15 Symmetry and equivariance: work at one point or on one slice, then move by the group.** Translate to the identity ($G\circ L_g = L_{G(g)}\circ G$; $h = Xg$), permute or rotate coordinates, extend a section to a trivialization by the $S^1$-action, normalize $z/|z|$. HW2.2(a), HW2.4, HW3.5(a)(b), HW4.3(b), HW4.4.

(S11 of `review_spec.md`, "local then global via germs and bump functions", appears in the homework only through the germ formalism of HW3.2–HW3.3.)
