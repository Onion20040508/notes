---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 9
section: 66
tags: [differentiable-manifolds, math591]
---
← [[§65 The Whitney Embedding Theorem]] · ↑ [[· 9 Sard's Theorem]]

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

> [!proof]+ Proof of Theorem [[§66 Partitions of Unity#^thm-66-1|§66.1]] (begun in Lecture 22, to be completed in Lecture 23)
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
> *To be completed in Lecture 23*: that the sums are locally finite, so that $\sum_j f_j$, the $g_i$ and the $\chi_\alpha$ are smooth, and that $\operatorname{supp}\chi_\alpha \subseteq U_\alpha$. One point to watch there: local finiteness of $\{B_i\}$ does not by itself make $\{\operatorname{supp} f_i\}$ locally finite, since $\operatorname{supp} f_i$ sits in the larger ball $\varphi_i^{-1}(B_{\varepsilon_i}(0))$, not in $\overline{B_i}$. Lee's proof of Theorem 2.23 avoids this by taking $f_i$ positive on $B_i$ and supported in $\overline{B_i}$, and using that the closures of a locally finite family are locally finite.

^pf-66-5-2

*Uses:* [[§66 Partitions of Unity#^thm-66-4|§66.4]], [[§66 Partitions of Unity#^lem-66-2|§66.2]], [[§56 Vector Fields#^prop-56-4|§56.4]]

**Transcription note (Lecture 22).** Page 58 of the handwritten notes states the theorem “if $X$ is $T_2$ and 2nd countable, then it is paracompact (need locally compact?)”; as stated it is false in general, and local compactness, which manifolds have, is the missing hypothesis (Remark [[§66 Partitions of Unity#^rem-66-1|remark]]).

