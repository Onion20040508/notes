---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 9
section: 66
tags: [differentiable-manifolds, math591]
---
← [[§65 The Whitney Embedding Theorem]] · ↑ [[· 9 Sard's Theorem]] · [[§67 Integral Curves]] →

*Stage: analysis — Writing $1$ as a locally finite sum of smooth functions subordinate to any open cover: the tool for gluing local constructions into global ones.*

*Lecture 22. “A key tool for constructing exhaustion functions, and many other things — we're going to use it to integrate forms, for example — is the notion of partition of unity. And Lee pays the bills up front. He deposits a lot of money” (Lee, Chapter 2).*

> [!definition] Definition §66.1: Partition of Unity
> A **partition of unity** on $M$ is an indexed family $\{\chi_\alpha\}_{\alpha \in A}$ of smooth functions on $M$, over an arbitrary index set $A$ (“could be uncountable”), such that
>
> 1. $0 \le \chi_\alpha \le 1$ for every $\alpha$;
> 2. the family of supports $\{\operatorname{supp}\chi_\alpha\}_{\alpha \in A}$ is **locally finite**: every $p \in M$ has a neighbourhood $U$ for which $\{ \alpha \in A : U \cap \operatorname{supp}\chi_\alpha \neq \varnothing \}$ is finite;
> 3. $\sum_{\alpha \in A} \chi_\alpha(p) = 1$ for every $p \in M$.
>
> By (2) the sum in (3) has only finitely many nonzero terms at each point. The partition is **subordinate** to an open cover $\{U_\alpha\}_{\alpha \in A}$ if $\operatorname{supp}\chi_\alpha \subseteq U_\alpha$ for every $\alpha$.
>
> *Lee: Ch. 2, Partitions of Unity*

^def-66-1

“This is where the name comes from. You take the number one, and you write it as a sum of smooth functions.” “These things allow us to localize”; the bump functions so far, and the cutoffs $\rho_i$ above, are made of the same material.

![[m591-66-2.svg]]

The simplest example, on $M = \mathbb{R}$: a function $\chi_1$ that is $1$ far to the left and $0$ far to the right, and $\chi_2 = 1 - \chi_1$.

> [!theorem] Theorem §66.1: Existence of Partitions of Unity
> If $\{U_\alpha\}_{\alpha \in A}$ is any open cover of $M$, there is a partition of unity $\{\chi_\alpha\}_{\alpha \in A}$ subordinate to it.
>
> *Lee: Theorem 2.23*

^thm-66-1

The proof has two steps of different kinds: an analysis step in $\mathbb{R}^m$, and “serious point set topology” on $M$. *Reading (Uribe's email of Oct 26): Lee, Chapter 2, from Lemma 2.20 to the beginning of the section on applications of partitions of unity (p. 44); for paracompactness, Theorem 1.15 (p. 9).*

> [!theorem] Lemma §66.2: Plateau Functions
> For all $\varepsilon > \delta > 0$ there is $\rho \in C^\infty(\mathbb{R})$ with $0 \le \rho \le 1$, $\rho \equiv 1$ on $[-\delta, \delta]$ and $\operatorname{supp}\rho \subseteq (-\varepsilon, \varepsilon)$. Then $f(x) = \rho(|x|)$ is smooth on $\mathbb{R}^m$, $f \equiv 1$ on the closed ball $\overline{B}_\delta$, and $\operatorname{supp} f \subseteq B_\varepsilon = \{ x \in \mathbb{R}^m : |x| < \varepsilon \}$.
>
> *Lee: Lemmas 2.20–2.22*

^lem-66-2

> [!proof]+ Proof
> *(Lecture 22: “I'm not going to prove that … you start with a function that is $e^{-1/x}$ for $x$ positive and zero for $x$ negative … and then you do trickery with it — reflect, divide, add. It's not complicated, but it takes 10 minutes to check.” The trickery is step 2 of the proof of Proposition [[§56 Vector Fields#^prop-56-4|§56.4]].)* With $h$ as there and $\delta < r' < \varepsilon$, take $\rho(t) = h(r'^2 - t^2)\big/\big(h(r'^2 - t^2) + h(t^2 - \delta^2)\big)$: smooth, between $0$ and $1$, equal to $1$ for $|t| \le \delta$ and $0$ for $|t| \ge r'$, so $\operatorname{supp}\rho \subseteq [-r', r'] \subseteq (-\varepsilon, \varepsilon)$. Then $f(x) = \rho(|x|)$ is the function $H$ of that proof (with $r = \delta$), smooth on $\mathbb{R}^m$ — “$|x|$ is not a $C^\infty$ function at the origin; however, $\rho$ is constant equal to one near $0$”, so $f$ is constant near $x = 0$ — with $f \equiv 1$ on $\overline{B}_\delta$ and $\operatorname{supp} f = \overline{B}_{r'} \subseteq B_\varepsilon$.

^pf-66-2

*Uses:* [[§56 Vector Fields#^prop-56-4|§56.4]]

![[m591-66-3.svg]]

*The topology.* “We need some serious point set topology … we're paying the bills. It's a little painful.”

> [!definition] Definition §66.2: Paracompact Space
> A space $X$ is **paracompact** if every open cover $\{U_\alpha\}_{\alpha \in A}$ has an open refinement $\{V_i\}_{i \in \mathbb{N}}$ that covers and is locally finite:
>
> 1. $X = \bigcup_i V_i$, and for every $i$ there is $\alpha(i)$ with $V_i \subseteq U_{\alpha(i)}$;
> 2. every $p \in X$ has a neighbourhood $W$ such that $\{ i : W \cap V_i \neq \varnothing \}$ is finite.
>
> *Lee: Ch. 1, Paracompactness*

^def-66-2

“Compactness would say that any cover has a finite subcover, and in this case we have [a] locally finite … it's not a subcover; it's just a refinement.” (The usual definition allows refinements indexed by any set; with the countable index set of the lecture it is what holds for manifolds, Theorem [[§66 Partitions of Unity#^thm-66-4|§66.4]] below.)

> [!theorem] Lemma §66.3: Exhaustion by Compact Sets
> A second-countable, locally compact Hausdorff space $X$ is the union of compact sets $K_1 \subseteq K_2 \subseteq \cdots$ with $K_j \subseteq \operatorname{Int}K_{j+1}$ for every $j$.
>
> *Lee: Proposition A.60*

^lem-66-3

> [!proof]+ Proof
> *(Not from lecture; filled in, following Lee.)* *A countable basis of precompact sets.* Let $\mathcal{B}$ be a countable basis, and $\mathcal{B}'$ the set of $B \in \mathcal{B}$ with compact closure. $\mathcal{B}'$ is still a basis: if $x \in W$ open, local compactness gives an open $V \ni x$ with $\overline V$ compact, and some $B \in \mathcal{B}$ has $x \in B \subseteq V \cap W$; then $\overline B$ is a closed subset of the compact $\overline V$ (closures computed in the Hausdorff space $X$), so compact. Enumerate $\mathcal{B}' = \{B_1, B_2, \ldots\}$ (if it is finite, $X$ is compact and $K_j = X$ works).
> *The exhaustion.* Put $K_1 = \overline{B_1}$. Given $K_j$ compact, it is covered by the $B_i$, hence by $B_1, \ldots, B_n$ for some $n$; take the least such $n$ with $n \ge j + 1$, and $K_{j+1} = \overline{B_1} \cup \cdots \cup \overline{B_n}$, compact as a finite union of compact sets. Then $K_j \subseteq B_1 \cup \cdots \cup B_n \subseteq \operatorname{Int}K_{j+1}$, and $B_j \subseteq K_j$ for all $j$, so $\bigcup_j K_j = X$.

^pf-66-3

> [!theorem] Theorem §66.4: Manifolds Are Paracompact
> Let $M$ be a topological manifold, $\{U_\alpha\}$ an open cover, and $\mathcal{B}$ any basis of the topology of $M$. Then $\{U_\alpha\}$ has a countable, locally finite open refinement that covers $M$ and consists of elements of $\mathcal{B}$. In particular $M$ is paracompact. More generally, every second-countable, locally compact Hausdorff space is paracompact, by the same proof.
>
> *Lee: Theorem 1.15*

^thm-66-4

> [!proof]+ Proof
> *(Stated in Lecture 22 — “manifolds are paracompact, and in fact the refinements can always be taken from a basis of the topology” — with the proof left to Lee; filled in, following Lee.)* $M$ is Hausdorff, second countable (Definition [[§1 Point-Set Topology Review#^def-1-6|§1.6]]) and locally compact (Proposition [[§2 Topological Manifolds#^prop-2-12|§2.12]]); let $K_1 \subseteq K_2 \subseteq \cdots$ be as in Lemma [[§66 Partitions of Unity#^lem-66-3|§66.3]], and $K_0 = K_{-1} = \varnothing$. For $j \ge 0$ put
>
> $$
> A_j = K_{j+1} \setminus \operatorname{Int}K_j \ \ \text{(compact)}, \qquad W_j = \operatorname{Int}K_{j+2} \setminus K_{j-1} \ \ \text{(open)}, \qquad A_j \subseteq W_j .
> $$
>
> For each $x \in A_j$ choose $\alpha$ with $x \in U_\alpha$, and $B_x \in \mathcal{B}$ with $x \in B_x \subseteq U_\alpha \cap W_j$. Finitely many $B_x$ cover the compact set $A_j$. The union over $j$ of these finite families is a countable family of elements of $\mathcal{B}$; it covers $M$, because the $A_j$ do (each point lies in some $K_{j+1} \setminus \operatorname{Int}K_j$); and it refines $\{U_\alpha\}$. *Locally finite:* the sets chosen for $j$ lie in $W_j$, and $W_j \cap W_k = \varnothing$ when $|j - k| \ge 3$; a point of $A_j$ has the neighbourhood $W_j$, which meets only the sets chosen for $j - 2, \ldots, j + 2$, finitely many.

^pf-66-4

*Uses:* [[§1 Point-Set Topology Review#^def-1-6|Def. §1.6]], [[§2 Topological Manifolds#^prop-2-12|§2.12]], [[§66 Partitions of Unity#^lem-66-3|§66.3]]

![[m591-66-1.svg]]

*(Not from lecture; figure added.)* The proof of Theorem [[§66 Partitions of Unity#^thm-66-4|§66.4]] for $j = 2$. The compact ring $A_2 = K_3 \setminus \operatorname{Int}K_2$ (teal) is covered by finitely many basis sets $B_x$ (blue), each inside some $U_\alpha$ and inside the open ring $W_2 = \operatorname{Int}K_4 \setminus K_1$ (between the dashed circles). Rings $W_j$ and $W_k$ with $|j - k| \ge 3$ are disjoint, so a point of $A_j$ has the neighbourhood $W_j$, which meets only the sets chosen for $j - 2, \ldots, j + 2$: the refinement is locally finite.

> [!remark] Remark: Is Local Compactness Needed?
> The board stated the theorem as “if $X$ is $T_2$ and second countable, then it is paracompact”, and Uribe was unsure: “I'm not sure … whether you need local compactness … Check your email. I'll clarify.” The email (Oct 26) settled it: “Indeed local compactness is needed: Hausdorff, 2nd countable and local compactness imply paracompactness. Lee proves directly what we need for manifolds in Theorem 1.15, page 9.” So the theorem is stated with local compactness, as above. *(Filled in.)* Why some hypothesis beyond Hausdorff and second countable is needed: A paracompact Hausdorff space is normal, in particular regular (Munkres, Theorem 41.1), and the *$K$-topology* on $\mathbb{R}$ — generated by the open intervals and the sets $(a, b) \setminus \{1/n : n \ge 1\}$ — is Hausdorff and second countable but not regular (Munkres, §31), so not paracompact. Local compactness, as above, suffices; so does regularity. For manifolds nothing changes: they are locally compact. Uribe on second countability: “we haven't used [it] at all until this moment, when we're paying the bills” — it was used once before, for countable subcovers in measure zero (Lemma [[§62 Sets of Measure Zero#^lem-62-3|§62.3]]).

^rem-66-1

> [!definition] Definition §66.3: Regular Coordinate Ball
> An open set $B \subseteq M$ is a **regular coordinate ball** if there are a chart $(U, \varphi)$ with $B \subseteq U$ and numbers $0 < \delta < \varepsilon$ such that $\varphi(B) = B_\delta(0)$, the $\delta$-ball centred at $0$, and $B_\varepsilon(0) \subseteq \varphi(U)$ — an $\varepsilon$-ball centred at $0$ containing $\varphi(B)$, with room to spare.
>
> *Lee: Ch. 1, Regular Coordinate Balls*

^def-66-3

“Why do you even need the second condition?” asked a student. “Because I want to pull back my function that I had before. You need a little room.”

![[m591-66-4.svg]]

> [!theorem] Lemma §66.5: Regular Coordinate Balls Form a Basis
> Let $\{U_\alpha\}$ be an open cover of $M$. The regular coordinate balls $B$ whose chart $(U, \varphi)$ can be chosen with $U$ inside some $U_\alpha$ form a basis of the topology of $M$.

^lem-66-5

> [!proof]+ Proof
> *(Filled in.)* Let $W$ be open and $x \in W$, say $x \in U_\alpha$. Take a chart $(V, \psi)$ at $x$, restrict it to $U = V \cap W \cap U_\alpha$, and translate so that $\varphi = \psi|_U - \psi(x)$ sends $x$ to $0$. $\varphi(U)$ is open, so it contains some $B_\varepsilon(0)$; for $0 < \delta < \varepsilon$, $B = \varphi^{-1}(B_\delta(0))$ is a regular coordinate ball with $x \in B \subseteq U \subseteq W$, and its chart domain $U$ lies in $U_\alpha$.

^pf-66-5

> [!proof]+ Proof of Theorem [[§66 Partitions of Unity#^thm-66-1|§66.1]] (begun in Lecture 22; completed, following Lee)
> *(The lecture's steps; Uribe stopped here: “I will finish the proof next time.”)* By Theorem [[§66 Partitions of Unity#^thm-66-4|§66.4]] with the basis of Lemma [[§66 Partitions of Unity#^lem-66-5|§66.5]], there is a countable, locally finite refinement $\{B_i\}_{i \in \mathbb{N}}$ of $\{U_\alpha\}$ covering $M$, each $B_i$ a regular coordinate ball with chart $(U_i, \varphi_i)$, $\varphi_i(B_i) = B_{\delta_i}(0)$, $B_{\varepsilon_i}(0) \subseteq \varphi_i(U_i)$, and $U_i \subseteq U_{\alpha(i)}$. “Pull back the function $f$ from the first part” (Lemma [[§66 Partitions of Unity#^lem-66-2|§66.2]], with $\delta_i < \varepsilon_i$) by $\varphi_i$, and extend it by zero: this gives a smooth $f_i : M \to \mathbb{R}$, as in step 3 of the proof of Proposition [[§56 Vector Fields#^prop-56-4|§56.4]], with
>
> $$
> f_i|_{B_i} \equiv 1, \qquad \operatorname{supp} f_i \subseteq U_i \subseteq U_{\alpha(i)} .
> $$
>
> “The $B_i$ form a cover, and $f_i$ is identically equal to one there,” so $\sum_j f_j \ge 1$ at every point. Let
>
> $$
> g_i = \frac{f_i}{\sum_j f_j}, \qquad \text{so that} \qquad \sum_i g_i \equiv 1, \qquad
> \chi_\alpha = \sum_{i \,:\, \alpha(i) = \alpha} g_i .
> $$
>
> “What we don't have [yet] is the index”: grouping the $g_i$ by $\alpha(i)$ re-indexes the partition by $A$.
>
> *(Lecture 23 went straight on to an application, [[§66 Partitions of Unity|§66]]; the rest is the assigned reading, Lee's proof of Theorem 2.23. Completed here, following Lee.)* What remains: the sums are locally finite, so that $\sum_j f_j$, the $g_i$ and the $\chi_\alpha$ are smooth, and $\operatorname{supp}\chi_\alpha \subseteq U_\alpha$. One point needs care. Local finiteness of $\{B_i\}$ does not by itself make $\{\operatorname{supp} f_i\}$ locally finite, since $\operatorname{supp} f_i$ sits in the larger ball $\varphi_i^{-1}(B_{\varepsilon_i}(0))$, not in $\overline{B_i}$. Lee avoids this by choosing $f_i$ positive on $B_i$ and supported in $\overline{B_i}$. That is the only change to the lecture's construction: $f_i$ is no longer $\equiv 1$ on $B_i$, only positive there, which is all the division needs.
>
> *Two facts about a locally finite family $\{A_i\}$ of subsets.* (a) $\{\overline{A_i}\}$ is locally finite: an open set meeting $\overline{A_i}$ meets $A_i$. (b) If each $A_i$ is closed, then $\bigcup_i A_i$ is closed: for $p \notin \bigcup_i A_i$, take an open $W \ni p$ meeting only $A_{i_1}, \ldots, A_{i_k}$; then $W \setminus (A_{i_1} \cup \cdots \cup A_{i_k})$ is an open neighbourhood of $p$ missing every $A_i$.
>
> *The new $f_i$.* With $h$ as in step 1 of the proof of Proposition [[§56 Vector Fields#^prop-56-4|§56.4]] ($h(t) = e^{-1/t}$ for $t > 0$, $h(t) = 0$ for $t \le 0$), put
>
> $$
> f_i = h\big(\delta_i^2 - |\varphi_i|^2\big) \ \text{ on } U_i, \qquad f_i = 0 \ \text{ on } M \setminus U_i .
> $$
>
> $f_i > 0$ exactly on $B_i = \varphi_i^{-1}(B_{\delta_i}(0))$. The set $K_i = \varphi_i^{-1}\big(\overline{B}_{\delta_i}(0)\big)$ is compact ($\overline{B}_{\delta_i}(0) \subseteq B_{\varepsilon_i}(0) \subseteq \varphi_i(U_i)$, and $\varphi_i^{-1}$ is continuous), hence closed in $M$. So $f_i$ is smooth, as it is smooth on the open set $U_i$ and zero on the open set $M \setminus K_i$, which together cover $M$ (as in step 3 of the proof of Proposition [[§56 Vector Fields#^prop-56-4|§56.4]]). Its support is $\overline{B_i} = K_i$: $K_i$ is closed and contains $B_i$, and every point of $K_i$ is a limit of points of $B_i$.
>
> *Smoothness.* By (a) the supports $\overline{B_i}$ form a locally finite family. Each $p$ has an open neighbourhood $W$ on which all but finitely many $f_j$ vanish, so on $W$ the sum $\sum_j f_j$ is a finite sum of smooth functions; hence $\sum_j f_j$ is smooth. It is positive everywhere, because the $B_i$ cover $M$ and $f_i > 0$ on $B_i$. So $g_i = f_i / \sum_j f_j$ is smooth, $0 \le g_i \le 1$, $\operatorname{supp} g_i = \overline{B_i} \subseteq U_i \subseteq U_{\alpha(i)}$, and $\sum_i g_i \equiv 1$.
>
> *Re-indexing.* For $\alpha \in A$ let $\chi_\alpha = \sum_{i : \alpha(i) = \alpha} g_i$, with the empty sum $0$. On $W$ as above, only finitely many terms are nonzero, so $\chi_\alpha$ is smooth; and $0 \le \chi_\alpha \le \sum_i g_i = 1$. Each $i$ has exactly one $\alpha(i)$, so $\sum_\alpha \chi_\alpha = \sum_i g_i \equiv 1$. The set $\{\chi_\alpha \neq 0\}$ lies in $\bigcup_{\alpha(i) = \alpha} \overline{B_i}$, which is closed by (b), so
>
> $$
> \operatorname{supp}\chi_\alpha \subseteq \bigcup_{i \,:\, \alpha(i) = \alpha} \overline{B_i} \subseteq U_\alpha .
> $$
>
> Finally, $W$ meets $\operatorname{supp}\chi_\alpha$ only if it meets some $\overline{B_i}$ with $\alpha(i) = \alpha$, and $W$ meets only finitely many $\overline{B_i}$. So $\{\operatorname{supp}\chi_\alpha\}$ is locally finite, and $\{\chi_\alpha\}_{\alpha \in A}$ is a partition of unity subordinate to $\{U_\alpha\}$.

^pf-66-1

*Uses:* [[§66 Partitions of Unity#^thm-66-4|§66.4]], [[§66 Partitions of Unity#^lem-66-2|§66.2]], [[§56 Vector Fields#^prop-56-4|§56.4]]

**Transcription note (Lecture 22).** Page 58 of the handwritten notes states the theorem “if $X$ is $T_2$ and 2nd countable, then it is paracompact (need locally compact?)”; as stated it is false in general, and local compactness, which manifolds have, is the missing hypothesis (Remark [[§66 Partitions of Unity#^rem-66-1|remark]]).

## An Application: Exhaustion Functions

*Lecture 23. “I do want to tell you about the application of partitions of unity that we need for the sketch of the Whitney embedding theorem, the noncompact case”: the existence of exhaustion functions (Definition [[§65 The Whitney Embedding Theorem#^def-65-1|§65.1]], Proposition [[§65 The Whitney Embedding Theorem#^prop-65-5|§65.5]]). “The proof will be quick using partitions of unity.”*

The proof starts from a countable cover by open sets with compact closures, which was set as an exercise.

> [!theorem] Lemma §66.6: Countable Precompact Covers
> Every manifold $M$ has a countable open cover $\{V_i\}_{i \ge 1}$ such that $\overline{V_i}$ is compact for every $i$.
>
> *Lee: Proposition 2.28 (proof)*

^lem-66-6

> [!proof]+ Proof
> *(Set in Lecture 23 as an exercise: “The argument that I have in mind uses paracompactness. Maybe you have another way of doing it.” Filled in, by paracompactness.)* Every $p \in M$ has an open neighbourhood $W_p$ with $\overline{W_p}$ compact (Proposition [[§2 Topological Manifolds#^prop-2-12|§2.12]]). By Theorem [[§66 Partitions of Unity#^thm-66-4|§66.4]] the cover $\{W_p\}_{p \in M}$ has a countable open refinement $\{V_i\}$ covering $M$; if it is finite, repeat one of its sets to index it by $i \ge 1$. Each $V_i$ lies in some $W_{p(i)}$, so $\overline{V_i}$ is a closed subset of the compact set $\overline{W_{p(i)}}$, hence compact. (Another way: the countable basis of precompact sets built in the proof of Lemma [[§66 Partitions of Unity#^lem-66-3|§66.3]] is already such a cover. Local finiteness of the refinement is not needed here.)

^pf-66-6

*Uses:* [[§1 Point-Set Topology Review#^def-1-6|Def. §1.6]], [[§2 Topological Manifolds#^prop-2-12|§2.12]], [[§66 Partitions of Unity#^lem-66-3|§66.3]], [[§66 Partitions of Unity#^thm-66-4|§66.4]]

> [!proof]+ Proof of Proposition [[§65 The Whitney Embedding Theorem#^prop-65-5|§65.5]]
> *(Lecture 23.)* Let $\{V_i\}_{i \ge 1}$ be as in Lemma [[§66 Partitions of Unity#^lem-66-6|§66.6]], and let $\{\chi_i\}_{i \ge 1}$ be a partition of unity subordinate to it (Theorem [[§66 Partitions of Unity#^thm-66-1|§66.1]]). Reviewing what this means (Definition [[§66 Partitions of Unity#^def-66-1|§66.1]]):
>
> 1. $0 \le \chi_i \le 1$ for all $i$;
> 2. $\{\operatorname{supp}\chi_i\}$ is locally finite;
> 3. $\sum_i \chi_i(p) = 1$ for all $p \in M$ — a finite sum at each point, by (2);
> 4. $\operatorname{supp}\chi_i \subseteq V_i$ for all $i$ — “that's the subordinate part.”
>
> “The clever construction” is to define
>
> $$
> f = \sum_{j \ge 1} j\, \chi_j .
> $$
>
> “If you don't put the $j$, you get one. But the clever idea is to put $j$ in front.” Again this is a locally finite sum of smooth functions, so $f$ is smooth; and $f \ge 0$ because the $\chi_j$ are nonnegative (in fact $f \ge \sum_j \chi_j = 1$). It remains to show that the sublevel sets are compact.
>
> *Claim.* For every $c \in \mathbb{R}$ and every integer $N \ge 0$ with $N \ge c$,
>
> $$
> f^{-1}\big((-\infty, c]\big) \subseteq \bigcup_{i=1}^N V_i \subseteq \bigcup_{i=1}^N \overline{V_i} .
> $$
>
> *The claim implies the proposition.* $\bigcup_{i=1}^N \overline{V_i}$ is a finite union of compact sets, so it is compact. $f^{-1}((-\infty, c])$ is closed, since $f$ is continuous, and a closed subset of a compact set is compact.
>
> *Proof of the claim.* We prove the contrapositive. Let $p \notin \bigcup_{i=1}^N V_i$. For $i = 1, \ldots, N$, $p \notin V_i \supseteq \operatorname{supp}\chi_i$, so $\chi_i(p) = 0$. Hence the sum defining $f(p)$ really starts at $N + 1$, and since every coefficient is at least $N + 1$ (“an $\ell^1$–$\ell^\infty$ estimate, or whatever”),
>
> $$
> f(p) = \sum_{j = N+1}^\infty j\, \chi_j(p) \ \ge\ (N + 1) \underbrace{\sum_{j = N+1}^\infty \chi_j(p)}_{=\, \sum_j \chi_j(p) \,=\, 1} = N + 1 > c .
> $$
>
> So $p \notin f^{-1}((-\infty, c])$.

^pf-65-5-2

*Uses:* [[§66 Partitions of Unity#^lem-66-6|§66.6]], [[§66 Partitions of Unity#^thm-66-1|§66.1]], [[§66 Partitions of Unity#^def-66-1|Def. §66.1]]

> [!remark] Remark: Why the Closures
> A student asked whether the contrapositive should use the union of the *closures*. Uribe: the proof shows the inclusion in $\bigcup_{i \le N} V_i$, and that “is contained in the union of the closures, so it doesn't make a difference.” The open sets give the stronger statement; the closures are where compactness lives, since the $V_i$ were chosen so that the $\overline{V_i}$ are compact, and $\bigcup_{i \le N} V_i$ alone need not be compact. “It is important that in the end I end up in here.” Lee runs the contrapositive from $p \notin \bigcup_{j \le N} \overline{V_j}$ instead (Proposition 2.28); either way the sublevel set lands inside the compact set $\bigcup_{j \le N} \overline{V_j}$.

^rem-66-2

![[m591-66-5.svg]]

*(Not from lecture; figure added, computed.)* The construction on $M = \mathbb{R}$, with $V_1 = (-1, 1)$ and $V_j = \{ j - 1.6 < |x| < j \}$ for $j \ge 2$, and $\chi_j$ obtained by normalizing bumps positive exactly on $V_j$. Then $f = \sum_j j\chi_j$ climbs one step on each successive $V_j$, so it grows like $|x|$. The sublevel set $f^{-1}((-\infty, 2.5])$ (red) lies inside $\overline{V_1} \cup \overline{V_2} \cup \overline{V_3} = [-3, 3]$, as the claim with $N = 3$ says.

“This technique of using partitions of unity is a very common technique in this subject, and the best way to learn to use it is to use it in a homework problem with hints.” The next assignment will have “at least one, maybe a couple of applications of partitions of unity.”

**Transcription note (Lecture 23).** The board defined $f = \sum_{j \ge 0} j\chi_j$ but wrote the union in the claim from $i = 1$ (Uribe: “wherever your index starts”). These notes index the cover and the partition from $1$, as Lee does. If the index starts at $0$, the union in the claim must start at $i = 0$ too. Otherwise a point of $V_0$ outside $V_1, \ldots, V_N$ can have $f(p) = \sum_{j > N} j\chi_j(p) < N + 1$, since then $\sum_{j > N}\chi_j(p) = 1 - \chi_0(p)$.
