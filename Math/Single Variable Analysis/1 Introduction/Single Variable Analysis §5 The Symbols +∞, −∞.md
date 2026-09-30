---
subject: "[[Single Variable Analysis]]"
section: 5
chapter: 1
tags: [real-analysis, math451]
---
← [[Single Variable Analysis §4 The Completeness Axiom]] · ↑ [[Single Variable Analysis — 1 Introduction]] · [[Single Variable Analysis §6 Dedekind Cuts]] →

These symbols are convenient. For any $a \in \mathbb{R}$,

$$
-\infty < a < +\infty,
$$

so we can write $\mathbb{R} = (-\infty, +\infty)$. Often we need the **extended real number system**

$$
[-\infty, +\infty] = \mathbb{R} \cup \{-\infty, +\infty\}.
$$

Then we can write extended intervals such as $[a, +\infty)$ — more convenient than $\{x \in \mathbb{R} \mid x \geq a\}$ — and similarly $[a, +\infty]$, $(a, +\infty)$, $(a, +\infty]$, etc.

**Another convenience.** If $S \subseteq \mathbb{R}$ is nonempty and bounded from above, then $\sup S$ exists and belongs to $\mathbb{R}$ (completeness). If $S$ is *not* bounded from above, we *define*

$$
\sup S = +\infty,
$$

and similarly $\inf S = -\infty$ if $S$ is not bounded from below. In this way, every nonempty subset $S \subseteq \mathbb{R}$ has both $\sup S$ and $\inf S$ in $[-\infty, +\infty]$.

The first payoff of the conventions: a basic inequality that needs no boundedness hypotheses at all.

> [!theorem] Proposition §5.1: Infimum at Most Supremum in Full Generality (HW)
> For *every* nonempty subset $S \subseteq \mathbb{R}$,
>
> $$
> \inf S \leq \sup S \qquad \text{in } [-\infty, +\infty].
> $$

^prop-5-1

> [!proof]+ Proof
> If $S$ is unbounded above, then $\sup S = +\infty$ by convention, and $\inf S \leq +\infty$ holds for every element of $[-\infty,+\infty]$. Symmetrically, if $S$ is unbounded below, then $\inf S = -\infty \leq \sup S$. If $S$ is bounded above and below, both $\inf S$ and $\sup S$ are real (completeness); since $S \neq \emptyset$, pick $x_0 \in S$: by the definitions of infimum and supremum,
>
> $$
> \inf S \leq x_0 \leq \sup S,
> $$
>
> and transitivity finishes. (Note where the conventions earn their keep: the unbounded cases are settled *by definition*, and only the bounded case needs an actual element of $S$.)

^pf-5-1

> [!remark] Remark: Arithmetic with infinities
> The extended real numbers carry partial arithmetic operations $+$, $\times$, etc., but some expressions are *not allowed*:
>
> $$
> \frac{0}{0}, \qquad \frac{+\infty}{+\infty}, \qquad (+\infty) - (+\infty).
> $$
>
> In dealing with limits we will also need $\pm\infty$; one must be careful with these arithmetic operations.

^rem-5-1

> [!theorem] Proposition §5.2: Supremum of a Sum of Sets
> For nonempty subsets $A, B \subseteq \mathbb{R}$, define
>
> $$
> A + B = \{x + y \mid x \in A,\ y \in B\}.
> $$
>
> Then
>
> $$
> \sup (A + B) = \sup A + \sup B, \qquad \inf (A+B) = \inf A + \inf B,
> $$
>
> as equalities in $[-\infty, +\infty]$; the forbidden operations above never occur here.

^prop-5-2

> [!proof]+ Proof
> We prove the $\sup$ statement; the $\inf$ statement follows by applying it to $-A, -B$ and using $\inf S = -\sup(-S)$ (§4).
>
> *Unbounded case.* If $A$ (say) is not bounded above, then neither is $A + B$: fixing any $y_0 \in B$, the elements $x + y_0$ with $x \in A$ are unbounded above. So both sides equal $+\infty$. (Note $\sup B > -\infty$ since $B \neq \emptyset$, so the right side is never the forbidden $+\infty + (-\infty)$.)
>
> *Bounded case.* Suppose both $\sup A$ and $\sup B$ are finite.
>
> ($\leq$) For any $x \in A$, $y \in B$: $x + y \leq \sup A + \sup B$, so $\sup A + \sup B$ is an upper bound of $A + B$, giving $\sup(A+B) \leq \sup A + \sup B$.
>
> ($\geq$) We use the [[Characterization of the Supremum|characterization of the supremum]]. Let $M_1 < \sup A + \sup B$ and set $\delta = \sup A + \sup B - M_1 > 0$. Since $\sup A - \delta/2 < \sup A$, there exists $x_1 \in A$ with $x_1 > \sup A - \delta/2$; similarly there exists $y_1 \in B$ with $y_1 > \sup B - \delta/2$. Then
>
> $$
> x_1 + y_1 > \sup A + \sup B - \delta = M_1,
> $$
>
> so no $M_1 < \sup A + \sup B$ is an upper bound of $A + B$. Hence $\sup(A+B) = \sup A + \sup B$.

^pf-5-2
