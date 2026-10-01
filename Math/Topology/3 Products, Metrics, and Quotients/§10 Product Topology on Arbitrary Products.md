---
type: section
subject: "[[Topology]]"
chapter: 3
section: 10
munkres: "§19"
tags: [topology, math590]
---
← [[§9 Continuous Functions]] · ↑ [[· 3 Products, Metrics, and Quotients]] · [[§11 Metric Topology]] →

## Definition and Basis

> [!definition] Definition §10.1: Product Topology on Arbitrary Products
> The **product topology** on $\prod_{\alpha \in J} X_\alpha$, where each $X_\alpha$ is a topological space, is the topology with basis consisting of all subsets of the form $\prod_{\alpha \in J} U_\alpha$, where:
>
> - $U_\alpha \subseteq X_\alpha$ is open for each $\alpha$
> - $U_\alpha = X_\alpha$ for all but finitely many $\alpha$ (i.e., at most finitely many $U_\alpha$ are proper subsets of $X_\alpha$)

^def-10-1

> [!remark]- Connections
> - The two-factor case: Product Topology on $X \times Y$ ([[§4 Product Topology#^def-4-1|Def. §4.1]]), with basis from [[§4 Product Topology#^thm-4-1|Theorem §4.1]].
> - Contrast: [[§10 Product Topology on Arbitrary Products#^def-10-2|Box Topology]].

> [!remark] Remark: Checking the Basis Axioms
> (1) Given $x \in \prod X_\alpha$, $x$ is contained in $\prod U_\alpha$ where all $U_\alpha = X_\alpha$.
>
> (2) If $x \in (\prod U_\alpha) \cap (\prod V_\alpha) = \prod (U_\alpha \cap V_\alpha)$, this is again a basis element.
>
> *Justification:* Suppose finitely many of the $U_\alpha$ and finitely many of the $V_\alpha$ are proper subsets of $X_\alpha$. We claim that $U_\alpha \cap V_\alpha$ is a proper subset of $X_\alpha$ only if $U_\alpha$ or $V_\alpha$ is a proper subset of $X_\alpha$. (Contrapositive: if both $U_\alpha = X_\alpha$ and $V_\alpha = X_\alpha$, then $U_\alpha \cap V_\alpha = X_\alpha$.)
>
> Thus:
>
> $$
> \{\alpha \mid U_\alpha \cap V_\alpha \subsetneq X_\alpha\} = \{\alpha \mid U_\alpha \subsetneq X_\alpha \text{ or } V_\alpha \subsetneq X_\alpha\} \subseteq \{\alpha \mid U_\alpha \subsetneq X_\alpha\} \cup \{\alpha \mid V_\alpha \subsetneq X_\alpha\}
> $$
>
> which is a union of two finite sets, hence finite. So $\prod(U_\alpha \cap V_\alpha)$ satisfies the product basis criteria.

^rem-10-1

## Continuity and Product Topology

> [!theorem] Theorem §10.1: Continuity into Product Spaces
> Let $A$ be a topological space. Let $f: A \to \prod_{\alpha \in J} X_\alpha$ be given by $f(a) = (f_\alpha(a))_{\alpha \in J}$, where $f_\alpha: A \to X_\alpha$ is a map. Then $f$ is continuous if and only if $f_\alpha$ is continuous for all $\alpha \in J$.

^thm-10-1

> [!proof]+ Proof
> $(\Rightarrow)$ Let $\pi_\beta: \prod X_\alpha \to X_\beta$ be the projection to the $\beta$-factor: $(x_\alpha)_{\alpha \in J} \mapsto x_\beta$.
>
> **Claim:** $\pi_\beta$ is a continuous map.
>
> *Proof of claim:* Let $U_\beta \subseteq X_\beta$ be an open set. Then $\pi_\beta^{-1}(U_\beta) = \prod_{\alpha \in J} U_\alpha$ (with $U_\beta$ in the $\beta$-th factor), which is open in the product topology (it's a basis element with $U_\alpha = X_\alpha$ for $\alpha \neq \beta$).
>
> Note $f_\beta = \pi_\beta \circ f$, a [[§9 Continuous Functions#^thm-9-4|composition of continuous maps]], hence continuous.
>
> $(\Leftarrow)$ Suppose $f_\alpha$ is continuous for all $\alpha \in J$. To show $f$ is continuous, it suffices to show $f^{-1}(\prod_{\alpha \in J} U_\alpha)$ is open in $A$, where $\prod U_\alpha$ is a basis element for the product topology.
>
> Note: $U_\alpha = X_\alpha$ for all but finitely many $\alpha$, say $\alpha_1, \ldots, \alpha_n$.
>
> $$
> f^{-1}\left(\prod_{\alpha \in J} U_\alpha\right) = \bigcap_{\alpha \in J} f_\alpha^{-1}(U_\alpha) = f_{\alpha_1}^{-1}(U_{\alpha_1}) \cap \cdots \cap f_{\alpha_n}^{-1}(U_{\alpha_n})
> $$
>
> (Since if $U_\alpha = X_\alpha$, then $f_\alpha^{-1}(U_\alpha) = A$.)
>
> Each $f_{\alpha_i}^{-1}(U_{\alpha_i})$ is open because $f_{\alpha_i}$ is continuous, so this is a finite intersection of open sets in $A$, hence open.

^pf-10-1

*Uses:* [[§9 Continuous Functions#^thm-9-4|§9.4]], [[§9 Continuous Functions#^def-9-1|Def. §9.1]]

> [!remark]- Connections
> - Used for products of paths: [[§14 Connected Subspaces of ℝ#^thm-14-5|Product of Path-Connected Spaces]], and for products of quotient maps: [[§12 Quotient Topology#^thm-12-5|Theorem §12.5]].
> - For two factors, 591 proves this as the universal property of the product and shows that it characterizes the product topology: [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^thm-3-10|591 Thm. §3.10]], [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^cor-3-11|591 Cor. §3.11]].

> [!example] Example §10.1: $\mathbb{R}^\omega$
> Define $\mathbb{R}^\omega = \mathbb{R} \times \mathbb{R} \times \cdots = \prod_{n \in \mathbb{Z}_{>0}} X_n$, where $X_n = \mathbb{R}$.
>
> Let $f: \mathbb{R} \to \mathbb{R}^\omega$ given by $f(t) = (t, t, \ldots, \ldots)$. This is continuous when we endow $\mathbb{R}^\omega$ with product topology because $f_n(t) = t$ is continuous for each $n$ ([[§10 Product Topology on Arbitrary Products#^thm-10-1|Theorem §10.1]]).

^ex-10-1

## Box Topology

> [!definition] Definition §10.2: Box Topology
> The **box topology** on $\prod_{\alpha \in J} X_\alpha$ is the topology with basis given by $\prod_{\alpha \in J} U_\alpha$, where $U_\alpha \subseteq X_\alpha$ is open (with no finiteness restriction).

^def-10-2

> [!remark] Remark
> The box topology is in general strictly finer than the product topology (i.e., has more open sets). This causes various pathologies.

^rem-10-2

> [!remark] Remark: Why the Product Topology is “Right”
> The box topology might seem more natural (open in each factor $\Rightarrow$ open in the product), but it is the *product topology* that satisfies the [[§10 Product Topology on Arbitrary Products#^thm-10-1|universal property]]: $f: Z \to \prod X_\alpha$ is continuous iff each $\pi_\alpha \circ f$ is continuous. [[§10 Product Topology on Arbitrary Products#^ex-10-2|The example below]] shows this fails for the box topology—the diagonal map $t \mapsto (t, t, \ldots)$ into $\mathbb{R}^\omega$ is continuous componentwise but not in the box topology.
>
> The product topology also gives us Tychonoff's theorem (arbitrary products of compact spaces are compact), one of the most powerful results in topology. This fails for the box topology. The lesson: imposing only finitely many constraints at a time is what makes infinite products manageable.

^rem-10-3

> [!example] Example §10.2: $f: \mathbb{R} \to \mathbb{R}^\omega$ Not Continuous in Box Topology
> The map $f: \mathbb{R} \to \mathbb{R}^\omega$, $f(t) = (t, t, \ldots)$ is **not** continuous when $\mathbb{R}^\omega$ is endowed with the box topology.
>
> Consider $U = \prod_{n \in \mathbb{Z}_{>0}} \left(-\frac{1}{n}, \frac{1}{n}\right) = (-1, 1) \times \left(-\frac{1}{2}, \frac{1}{2}\right) \times \cdots \subseteq \mathbb{R}^\omega$, which is open in the box topology.
>
> But $f^{-1}(U) = \bigcap_{n=1}^{\infty} \left(-\frac{1}{n}, \frac{1}{n}\right) = \{0\}$, which is not open in $\mathbb{R}$.

^ex-10-2

![[m590-10-1.svg]]
*Each vertical line is one factor of $\mathbb{R}^\omega$ and the blue segments are the $U_n$ (open endpoints hollow). The red dots are the point $f(t) = (t, t, \ldots)$. Left: a product basis element restricts only finitely many factors (here $n = 1, 2$), so $f(t)$ lies in it for all $|t| < \tfrac12$ and the preimage contains an interval. Right: the box set $U = \prod (-\tfrac1n, \tfrac1n)$ restricts every factor. Whatever $t \neq 0$ is, the intervals eventually shrink below height $t$ ($n \ge 3$ in the drawing), so $f^{-1}(U) = \{0\}$.*
