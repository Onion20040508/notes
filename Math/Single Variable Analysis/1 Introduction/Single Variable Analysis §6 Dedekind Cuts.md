---
subject: "[[Single Variable Analysis]]"
section: 6
chapter: 1
tags: [real-analysis, math451]
---
← [[Single Variable Analysis §5 The Symbols +∞, −∞]] · ↑ [[Single Variable Analysis — 1 Introduction]] · [[Single Variable Analysis §7 Limits of Sequences]] →

**Question.** How can $\mathbb{R}$ be *defined* from $\mathbb{Q}$?

We said $\mathbb{R}$ is complete but $\mathbb{Q}$ is not. One might try to define $\mathbb{R}$ using limits of sequences of rational numbers (“taking the closure”). In other courses this is fine — but it is a problem in *our* course: we want to have $\mathbb{R}$ first, and only then define the notion and properties of limits. Defining $\mathbb{R}$ via limits would be circular here.

A smart person came up with a way around this: **Dedekind**.

> [!definition] Definition §6.1: Dedekind Cut
> Given a real number $r \in \mathbb{R}$, it can be recovered from a subset of $\mathbb{Q}$:
>
> $$
> S_r = \{a \in \mathbb{Q} \mid a < r\}.
> $$
>
> For example, $\sup S_r = r$. The set $S_r$ is called the **Dedekind cut** associated with $r$.

^def-6-1

![[m451-6-1.svg]]
*The Dedekind cut $S_r$ (blue): all rationals to the left of $r$, with $r$ itself excluded (hollow). Its elements creep up to $r$ without a largest one — property (3) of Proposition 6.1 below — while $\sup S_r = r$.*

The important point: $S_r$ is completely determined by subsets and properties of $\mathbb{Q}$ alone. The idea is to *define* all operations and properties of real numbers in terms of these cuts. For this, we need to characterize which subsets of $\mathbb{Q}$ arise as cuts.

> [!theorem] Proposition §6.1: Characterization of Cuts
> For every $r \in \mathbb{R}$, the set $S_r$ satisfies:
>
> 1. $S_r \neq \mathbb{Q}$ and $S_r \neq \emptyset$: a proper nonempty subset;
>
> 2. if $a \in \mathbb{Q}$, $b \in S_r$, and $a \leq b$, then $a \in S_r$ (it contains all rationals below any of its elements);
>
> 3. $S_r$ does not have a maximum.
>
> Conversely, every subset of $\mathbb{Q}$ satisfying (1)–(3) is $S_r$ for a unique $r \in \mathbb{R}$: we get a bijective correspondence between Dedekind cuts and real numbers.

^prop-6-1

> [!proof]+ Proof
> (1) By the [[Archimedean Property|Archimedean property]], there are rationals (indeed integers) below $r$ and above $r$, so $S_r$ is nonempty and misses some rational.
>
> (2) If $b \in S_r$ and $a \leq b$, then $a \leq b < r$, so $a \in S_r$ by transitivity.
>
> (3) Why does $S_r$ have no maximum? By the *density of $\mathbb{Q}$ in $\mathbb{R}$* (§4): given any $a \in S_r$, since $a < r$ there exists a rational $a'$ with $a < a' < r$. Then $a' \in S_r$ and $a' > a$, so $a$ is not a maximum of $S_r$.
>
> (For the converse — that every set satisfying (1)–(3) determines a unique real number — one takes $r = \sup S$, using completeness; we do not carry this out here.)

^pf-6-1

> [!theorem] Proposition §6.2: Structure Transported to Cuts
> For $r_1, r_2 \in \mathbb{R}$:
>
> - (i) $r_1 \leq r_2$ if and only if $S_{r_1} \subseteq S_{r_2}$;
>
> - (ii) $S_{r_1} + S_{r_2} = S_{r_1 + r_2}$ (with $A + B$ as defined in §5).
>
> So the order and the addition of real numbers can be defined completely in terms of rational numbers.

^prop-6-2

For the construction to stand on its own, however, there is a logical gap in (ii) as stated: it *presupposes* $\mathbb{R}$ and verifies the formula afterwards. In the genuine construction, one must define the sum of two cuts *before* knowing what real numbers they represent — and prove that the result is again a cut, using only $\mathbb{Q}$. This is the well-definedness of addition:

> [!theorem] Proposition §6.3: The Sum of Two Cuts Is a Cut (HW)
> Let $A, B \subseteq \mathbb{Q}$ satisfy properties (1)–(3), and define
>
> $$
> A + B = \{ a + b \mid a \in A,\ b \in B \}.
> $$
>
> Then $A + B$ also satisfies (1)–(3).

^prop-6-3

> [!proof]+ Proof
> Note first a consequence of (2): if $a^* \notin A$, then $a < a^*$ for every $a \in A$ — for if $a^* \leq a$ for some $a \in A$, downward closure would force $a^* \in A$.
>
> (1) *Proper and nonempty.* $A + B \neq \emptyset$ since $A, B \neq \emptyset$. For properness, choose $a^* \notin A$ and $b^* \notin B$ (possible by (1) for $A$ and $B$). By the observation above, every element $a + b \in A + B$ satisfies $a + b < a^* + b^*$; in particular $a^* + b^* \notin A + B$.
>
> (2) *Downward closed.* Let $c \in \mathbb{Q}$ with $c \leq a + b$ for some $a \in A$, $b \in B$. Write
>
> $$
> c = a' + b, \qquad a' = c - b \leq a.
> $$
>
> By property (2) for $A$, $a' \in A$; hence $c = a' + b \in A + B$.
>
> (3) *No maximum.* Let $a + b \in A + B$. By property (3) for $A$, there is $a' \in A$ with $a' > a$; then $a' + b \in A + B$ and $a' + b > a + b$, so $a + b$ is not a maximum.
>
> Every step used only the arithmetic and order of $\mathbb{Q}$ — no real numbers needed.

^pf-6-3

> [!remark] Remark: An alternative for downward closure
> Property (2) can also be proved symmetrically: for $c < a + b$, set $\varepsilon = \tfrac{a+b-c}{2} > 0$ and shave it off both summands, $a' = a - \varepsilon \in A$, $b' = b - \varepsilon \in B$ (downward closure of each factor), so that $c = a' + b' \in A + B$. This $\varepsilon$-splitting is the recurring trick of the whole construction — it reappears in part (c) of the embedding below and in the correct definition of $-A$.

^rem-6-1

Recall the logical gap flagged above: the compatibility statements for $S_{r_1}, S_{r_2}$ presupposed $\mathbb{R}$. For *rational* numbers, no such presupposition is needed — everything can be proved inside $\mathbb{Q}$, which is exactly what the genuine construction requires of its copy of $\mathbb{Q}$:

> [!theorem] Proposition §6.4: The Rational Cuts Embed Faithfully (HW)
> For $s, t \in \mathbb{Q}$, write $S_s = \{q \in \mathbb{Q} \mid q < s\}$ (a cut, by direct check). Then:
>
> - (a) $s \leq t$ if and only if $S_s \subseteq S_t$;
>
> - (b) $s = t$ if and only if $S_s = S_t$;
>
> - (c) $S_{s+t} = S_s + S_t$ (the sum of cuts defined above).
>
> So the map $q \mapsto S_q$ embeds $\mathbb{Q}$ into the set of cuts, preserving order and addition — and injectively, by (b).

^prop-6-4

> [!proof]+ Proof
> (a) ($\Rightarrow$) Assume $s \leq t$ and let $q \in S_s$; then $q < s \leq t$, so $q \in S_t$. ($\Leftarrow$) Assume $S_s \subseteq S_t$ and suppose, for a contradiction, $s > t$. The rational midpoint $q = \tfrac{s+t}{2}$ satisfies $t < q < s$, so $q \in S_s$ but $q \notin S_t$ — contradicting the inclusion. Hence $s \leq t$.
>
> (b) ($\Rightarrow$) is immediate from the definition (both inclusions as in (a)). ($\Leftarrow$) If $S_s = S_t$, then both inclusions hold, so by (a) both $s \leq t$ and $t \leq s$, whence $s = t$.
>
> (c) ($\subseteq$) Let $q \in S_{s+t}$, i.e. $q \in \mathbb{Q}$ with $q < s + t$. Split the slack evenly:
>
> $$
> \varepsilon = \frac{s + t - q}{2} > 0, \qquad a = s - \varepsilon, \qquad b = t - \varepsilon.
> $$
>
> Then $a, b \in \mathbb{Q}$ (closure of $\mathbb{Q}$), $a < s$ and $b < t$ (so $a \in S_s$, $b \in S_t$), and
>
> $$
> a + b = s + t - 2\varepsilon = q,
> $$
>
> hence $q \in S_s + S_t$. ($\supseteq$) If $q = a + b$ with $a \in S_s$, $b \in S_t$, then $a < s$ and $b < t$ give $q = a + b < s + t$, so $q \in S_{s+t}$. Combining, $S_{s+t} = S_s + S_t$.

^pf-6-4

> [!remark] Remark: Why subtraction is the delicate one
> One might guess the negation of a cut to be $-A = \{-a \mid a \notin A\}$. This fails property (3) exactly when $\mathbb{Q} \setminus A$ has a *least* element — i.e. when $A = S_r$ with $r$ rational: then $\mathbb{Q}\setminus A = \{q \geq r\}$ has minimum $r$, and the naive set $\{q \leq -r\}$ has the maximum $-r$. The correct definition excludes the boundary:
>
> $$
> -A = \{ c \in \mathbb{Q} \mid -c - \varepsilon \notin A \ \text{for some rational } \varepsilon > 0 \}.
> $$
>
> This is the one genuinely trap-laden point of the whole construction; the rest is careful bookkeeping.

^rem-6-2

![[m451-6-2.svg]]
*The negation trap for a rational $r$. Top: $A = S_r$ excludes $r$, so its complement has the minimum $r$ (filled). Middle: negating the complement gives $\{q \leq -r\}$, whose maximum $-r$ (red) violates property (3). Bottom: the correct $-A$ drops that boundary point, leaving $\{q < -r\}$ (hollow endpoint).*

> [!theorem] Proposition §6.5: Completion of the Construction — Exercises
> Let $\mathcal{R}$ denote the set of all cuts, i.e. all $A \subseteq \mathbb{Q}$ satisfying (1)–(3), ordered by $A \leq B \iff A \subseteq B$, with addition as above. Then:
>
> - (i) $-A$ (as defined in the remark) is a cut, and $A + (-A) = S_0$: additive inverses exist.
>
> - (ii) For *positive* cuts ($A \supsetneq S_0$), the product
>
>   $$
>   A \cdot B = \{ q \in \mathbb{Q} \mid q \leq ab \ \text{for some } a \in A,\ b \in B \ \text{with } a, b > 0 \}
>   $$
>
>   is a cut; multiplication extends to all cuts by the usual sign rules (with $S_0$ absorbing), handled case by case.
>
> - (iii) With these operations and the order $\subseteq$, the set $\mathcal{R}$ satisfies all the field axioms A1–A6 and order axioms O1–O5 of §3: $\mathcal{R}$ is an ordered field.
>
> - (iv) $\mathcal{R}$ satisfies the [[Completeness Axiom|completeness axiom]]: if $\mathcal{S} \subseteq \mathcal{R}$ is nonempty and bounded above (under $\subseteq$), then
>
>   $$
>   \sup \mathcal{S} = \bigcup_{A \in \mathcal{S}} A
>   $$
>
>   — the union of the cuts is itself a cut and is the least upper bound.
>
> The proofs are left as exercises (in the same style as the addition proposition; (iv) is the most elegant one). Complete details can be found in Rudin, *Principles of Mathematical Analysis*, Appendix to Chapter 1.

^prop-6-5

> [!remark] Remark: The logical role of cuts
> In this course we take the axiomatic approach: $\mathbb{R}$ is *assumed* to be a complete ordered field, and everything is derived from the axioms. Dedekind cuts address a different question — whether such an object *exists* at all. The construction sketches an affirmative answer: starting from $\mathbb{Q}$ only, one defines the set of all cuts, equips it with the order (i) and operations like (ii), and verifies all the axioms, including completeness. So the axioms of §3–§4 are not vacuous.

^rem-6-3
