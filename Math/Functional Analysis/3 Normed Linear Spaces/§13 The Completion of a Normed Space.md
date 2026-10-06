---
type: section
subject: "[[Functional Analysis]]"
chapter: 3
section: 13
tags: [functional-analysis, math556]
---
← [[§12 Completeness]] · ↑ [[· 3 Normed Linear Spaces]] · [[§14 New Normed Spaces from Old]] →

*Stage: norms — Thread: completeness. The completion of a normed space is a Banach space, and in practice it can be written down as a concrete space.*

## Completion of a Normed Linear Space

For a normed linear space $X$, the completion $\overline{X}$ as a metric space should again be a normed linear space, with $X$ sitting inside it as a subspace and with the original norm. The natural candidate for the norm of a class is the limit of the norms of a representative.

> [!theorem] Theorem §13.1: The Completion of a Normed Space is a Banach Space
> Let $(X, \|\cdot\|)$ be a normed linear space and $\overline{X}$ its completion. For a Cauchy sequence $\{x_n\}$ in $X$, write $[\{x_n\}] \in \overline{X}$ for its class, and define
>
> $$
> \bigl\| [\{x_n\}] \bigr\| := \lim_{n \to \infty} \|x_n\|.
> $$
>
> Then $\overline{X}$ is a linear space, this is a well-defined norm on it, $\|[(x, x, \ldots)]\| = \|x\|$ for $x \in X$, and $(\overline{X}, \|\cdot\|)$ is complete.
>
> *Source: HW2, Problem 3*
> *Lax: §5.1, Thm 3*

^thm-13-1

> [!remark] Note: Notation for the Proof
> The norm of $X$ is written $\|\cdot\|$ and the candidate norm on $\overline{X}$ is written $\|\cdot\|_{\overline{X}}$. A sequence in $\overline{X}$ is a sequence of classes; its $m$-th term is written $[\{x^{(m)}_n\}_n]$, where $\{x^{(m)}_n\}_n$ is a Cauchy sequence in $X$ (superscript: which class; subscript: which term of the representative).

^rem-13-1

> [!proof]+ Proof
> (HW2, Problem 3.) Throughout, $\{x_n\}$ denotes a Cauchy sequence in $(X, \|\cdot\|)$ and $[\{x_n\}]$ its class in $\overline{X}$; two Cauchy sequences are equivalent iff $\lim_n \|x_n - y_n\| = 0$.
>
> **Step 1: the limit $\lim_n \|x_n\|$ exists.** For all $m, k$, the reverse triangle inequality (Lemma [[§11 Normed Linear Spaces#^lem-11-3|§11.3]]) gives $\bigl|\,\|x_m\| - \|x_k\|\,\bigr| \le \|x_m - x_k\|$. Given $\varepsilon > 0$, choose $N$ with $\|x_m - x_k\| < \varepsilon$ for all $m, k > N$; then $\bigl|\,\|x_m\| - \|x_k\|\,\bigr| < \varepsilon$ for all $m, k > N$. So $\{\|x_n\|\}$ is a Cauchy sequence of real numbers, and since $\mathbb{R}$ is complete, $\lim_n \|x_n\|$ exists.
>
> **Step 2: $\sim$ is an equivalence relation.** *Reflexive:* $\lim_n \|x_n - x_n\| = \lim_n 0 = 0$. *Symmetric:* since $\|y_n - x_n\| = \|x_n - y_n\|$ for every $n$, $\lim_n \|x_n - y_n\| = 0$ implies $\lim_n \|y_n - x_n\| = 0$. *Transitive:* if $\lim_n \|x_n - y_n\| = 0$ and $\lim_n \|y_n - z_n\| = 0$, then by the triangle inequality
>
> $$
> 0 \le \|x_n - z_n\| \le \|x_n - y_n\| + \|y_n - z_n\| \to 0 + 0 = 0,
> $$
>
> and limits preserve non-strict inequalities, so $\lim_n \|x_n - z_n\| = 0$.
>
> **Step 3: $\|\cdot\|_{\overline{X}}$ is well defined.** Suppose $\{x_n\} \sim \{x_n'\}$. By the reverse triangle inequality, $0 \le \bigl|\,\|x_n\| - \|x_n'\|\,\bigr| \le \|x_n - x_n'\|$, so $\lim_n \bigl(\|x_n\| - \|x_n'\|\bigr) = 0$. Both limits exist by Step 1, so by linearity of limits $\lim_n \|x_n\| - \lim_n \|x_n'\| = 0$. Hence $\|[\{x_n\}]\|_{\overline{X}} = \lim_n \|x_n\|$ does not depend on the representative.
>
> **Step 4: the operations on $\overline{X}$ are well defined.** Define $[\{x_n\}] + [\{y_n\}] = [\{x_n + y_n\}]$ and $a[\{x_n\}] = [\{a x_n\}]$.
>
> *The results are Cauchy sequences.* Given $\varepsilon > 0$, choose $N$ with $\|x_m - x_k\| < \varepsilon/2$ and $\|y_m - y_k\| < \varepsilon/2$ for $m, k > N$; then $\|(x_m + y_m) - (x_k + y_k)\| \le \|x_m - x_k\| + \|y_m - y_k\| < \varepsilon$. For $a \neq 0$, choose $N$ with $\|x_m - x_k\| < \varepsilon/|a|$ for $m, k > N$; then $\|a x_m - a x_k\| = |a|\,\|x_m - x_k\| < \varepsilon$. For $a = 0$ the sequence is constantly $0$, hence Cauchy.
>
> *Independence of representatives.* If $\{x_n\} \sim \{x_n'\}$ and $\{y_n\} \sim \{y_n'\}$, then
>
> $$
> \|(x_n + y_n) - (x_n' + y_n')\| \le \|x_n - x_n'\| + \|y_n - y_n'\| \to 0, \qquad \|a x_n - a x_n'\| = |a|\,\|x_n - x_n'\| \to 0,
> $$
>
> so $\{x_n + y_n\} \sim \{x_n' + y_n'\}$ and $\{a x_n\} \sim \{a x_n'\}$.
>
> **Step 5: $\overline{X}$ is a linear space.** In each line the outer equalities use the definition of the operations on classes and the middle equality is the corresponding axiom of $X$, applied at each index $n$. Let $[\{x_n\}], [\{y_n\}], [\{z_n\}] \in \overline{X}$ and $a, k \in \mathbb{F}$.
>
> *Commutativity:* $[\{x_n\}] + [\{y_n\}] = [\{x_n + y_n\}] = [\{y_n + x_n\}] = [\{y_n\}] + [\{x_n\}]$.
>
> *Associativity:* $\bigl([\{x_n\}] + [\{y_n\}]\bigr) + [\{z_n\}] = [\{(x_n + y_n) + z_n\}] = [\{x_n + (y_n + z_n)\}] = [\{x_n\}] + \bigl([\{y_n\}] + [\{z_n\}]\bigr)$.
>
> *Additive identity:* the constant sequence $\{0\}$ is Cauchy, and $[\{x_n\}] + [\{0\}] = [\{x_n + 0\}] = [\{x_n\}] = [\{0 + x_n\}] = [\{0\}] + [\{x_n\}]$.
>
> *Additive inverse:* $\{-x_n\}$ is Cauchy (Step 4 with $a = -1$), and $[\{x_n\}] + [\{-x_n\}] = [\{x_n - x_n\}] = [\{0\}] = [\{-x_n + x_n\}] = [\{-x_n\}] + [\{x_n\}]$.
>
> *Compatibility:* $k\bigl(a[\{x_n\}]\bigr) = k[\{a x_n\}] = [\{k(a x_n)\}] = [\{(ka)x_n\}] = (ka)[\{x_n\}]$.
>
> *Distributivity over vector addition:* $k\bigl([\{x_n\}] + [\{y_n\}]\bigr) = [\{k(x_n + y_n)\}] = [\{k x_n + k y_n\}] = k[\{x_n\}] + k[\{y_n\}]$.
>
> *Distributivity over scalar addition:* $(a + k)[\{x_n\}] = [\{(a + k)x_n\}] = [\{a x_n + k x_n\}] = a[\{x_n\}] + k[\{x_n\}]$.
>
> *Unit:* $1[\{x_n\}] = [\{1 \cdot x_n\}] = [\{x_n\}]$.
>
> Hence $\overline{X}$ is a linear space over $\mathbb{F}$ with zero element $[\{0\}]$.
>
> **Step 6: $\|\cdot\|_{\overline{X}}$ is a norm.** *Positivity.* Each $\|x_n\| \ge 0$, so $\lim_n \|x_n\| \ge 0$. If $\|[\{x_n\}]\|_{\overline{X}} = 0$, then $\lim_n \|x_n - 0\| = 0$, so $\{x_n\} \sim \{0\}$ and $[\{x_n\}] = [\{0\}]$. Conversely, if $[\{x_n\}] = [\{0\}]$ then $\lim_n \|x_n\| = 0$.
>
> *Homogeneity.* By Step 3 it suffices to compute with one representative: $\|a[\{x_n\}]\|_{\overline{X}} = \lim_n \|a x_n\| = \lim_n |a|\,\|x_n\| = |a| \lim_n \|x_n\| = |a|\,\|[\{x_n\}]\|_{\overline{X}}$.
>
> *Triangle inequality.* For every $n$, $\|x_n + y_n\| \le \|x_n\| + \|y_n\|$; all three limits exist by Step 1, and limits preserve non-strict inequalities, so
>
> $$
> \|[\{x_n\}] + [\{y_n\}]\|_{\overline{X}} = \lim_n \|x_n + y_n\| \le \lim_n \|x_n\| + \lim_n \|y_n\| = \|[\{x_n\}]\|_{\overline{X}} + \|[\{y_n\}]\|_{\overline{X}} .
> $$
>
> *Extension.* For $x \in X$, $\|[(x, x, \ldots)]\|_{\overline{X}} = \lim_n \|x\| = \|x\|$.
>
> **Step 7: construction of a candidate limit.** Let $\bigl([\{x^{(m)}_n\}_n]\bigr)_{m \ge 1}$ be Cauchy in $\overline{X}$. We build a sequence $\{y_j\}$ in $X$ by choosing, for each $j$, a sequence index $M_j$ and a term index $N_j$: one term out of one representative for each $j$, a diagonal choice.
>
> *Choice of the sequence indices.* Applying the Cauchy property with $\varepsilon = 1/j$, there is $m_j$ with $\|[\{x^{(m)}_n\}] - [\{x^{(k)}_n\}]\|_{\overline{X}} < 1/j$ for all $m, k \ge m_j$. Set $M_j = \max\{m_1, \ldots, m_j\}$, so that $M_1 \le M_2 \le \cdots$ and $M_j \ge m_j$. The condition then holds for all indices $\ge M_j$; taking $k = M_j$,
>
> $$
> \bigl\| [\{x^{(M_j)}_n\}] - [\{x^{(m)}_n\}] \bigr\|_{\overline{X}} = \lim_{n \to \infty} \bigl\| x^{(M_j)}_n - x^{(m)}_n \bigr\| < \frac{1}{j} \qquad \text{for all } m \ge M_j. \tag{3.1}
> $$
>
> *Choice of the term indices.* With the $M_j$ fixed, each $\{x^{(M_j)}_n\}_n$ is Cauchy in $X$, so there is $n_j$ with $\|x^{(M_j)}_n - x^{(M_j)}_{n'}\| < 1/j$ for all $n, n' \ge n_j$. Set $N_j = \max\{n_1, \ldots, n_j\}$, so $N_1 \le N_2 \le \cdots$ and
>
> $$
> \bigl\| x^{(M_j)}_n - x^{(M_j)}_{n'} \bigr\| < \frac{1}{j} \qquad \text{for all } n, n' \ge N_j. \tag{3.2}
> $$
>
> *The candidate.* Define $y_j := x^{(M_j)}_{N_j} \in X$, the $N_j$-th term of the $M_j$-th sequence. Property (3.1) compares the sequence $\{x^{(M_j)}_n\}_n$ to every later sequence in the norm of $\overline{X}$; property (3.2) compares terms of that one sequence to each other.
>
> **Step 8: $\{y_j\}$ is Cauchy in $X$.** Let $\varepsilon > 0$ and choose $J$ with $3/J < \varepsilon$. Take $j, k \ge J$; since $\|y_j - y_k\| = \|y_k - y_j\|$ and the case $j = k$ is trivial, assume $j > k \ge J$. For any index $n'$, inserting two intermediate terms,
>
> $$
> \|y_j - y_k\| \le \underbrace{\bigl\| x^{(M_j)}_{N_j} - x^{(M_j)}_{n'} \bigr\|}_{\text{①}} + \underbrace{\bigl\| x^{(M_j)}_{n'} - x^{(M_k)}_{n'} \bigr\|}_{\text{②}} + \underbrace{\bigl\| x^{(M_k)}_{n'} - x^{(M_k)}_{N_k} \bigr\|}_{\text{③}} .
> $$
>
> *Term ①.* Both term indices belong to the single sequence $\{x^{(M_j)}_n\}_n$; by (3.2) at index $j$, if $n' \ge N_j$ then ① $< 1/j$.
>
> *Term ③.* Likewise, by (3.2) at index $k$, if $n' \ge N_k$ then ③ $< 1/k$.
>
> *Term ②.* The two entries come from different sequences at the same term index. Since $j > k$ and $\{M_j\}$ is non-decreasing, $M_j \ge M_k$, so (3.1) at index $k$ applies with $m = M_j$: $\lim_{n} \|x^{(M_k)}_n - x^{(M_j)}_n\| < 1/k$. A sequence of reals whose limit is $< 1/k$ is eventually $< 1/k$, so there is $N$ (depending on $j$ and $k$) with ② $< 1/k$ for all $n' \ge N$.
>
> *Choice of $n'$.* Take $n' \ge \max\{N_j, N_k, N\}$. All three bounds hold, and since $1/j < 1/k \le 1/J$,
>
> $$
> \|y_j - y_k\| < \frac{1}{j} + \frac{1}{k} + \frac{1}{k} \le \frac{3}{J} < \varepsilon .
> $$
>
> Here $n'$ was chosen after $j$ and $k$ were fixed and does not appear in the conclusion. Hence $\{y_j\}$ is Cauchy in $X$, and $[\{y_j\}] \in \overline{X}$.
>
> **Step 9: $[\{x^{(m)}_n\}] \to [\{y_n\}]$ in $\overline{X}$.** Let $\varepsilon > 0$ and fix $j$ with $3/j < \varepsilon$. For any $m \ge M_j$,
>
> $$
> \bigl\| [\{x^{(m)}_n\}] - [\{y_n\}] \bigr\|_{\overline{X}} \le \underbrace{\bigl\| [\{x^{(m)}_n\}] - [\{x^{(M_j)}_n\}] \bigr\|_{\overline{X}}}_{\text{Ⓐ}} + \underbrace{\bigl\| [\{x^{(M_j)}_n\}] - [\{y_n\}] \bigr\|_{\overline{X}}}_{\text{Ⓑ}} . \tag{3.3}
> $$
>
> *Term Ⓐ.* Since $m \ge M_j$, (3.1) at index $j$ gives Ⓐ $< 1/j$.
>
> *Term Ⓑ.* We claim Ⓑ $\le 2/j$. By definition, Ⓑ $= \lim_n \|x^{(M_j)}_n - y_n\| = \lim_n \|x^{(M_j)}_n - x^{(M_n)}_{N_n}\|$, so it suffices to bound $\|x^{(M_j)}_n - x^{(M_n)}_{N_n}\|$ for all large $n$. Let $n \ge \max\{j, N_j\}$. For any auxiliary index $n'$,
>
> $$
> \bigl\| x^{(M_j)}_n - x^{(M_n)}_{N_n} \bigr\| \le \underbrace{\bigl\| x^{(M_j)}_n - x^{(M_j)}_{n'} \bigr\|}_{\text{①}} + \underbrace{\bigl\| x^{(M_j)}_{n'} - x^{(M_n)}_{n'} \bigr\|}_{\text{②}} + \underbrace{\bigl\| x^{(M_n)}_{n'} - x^{(M_n)}_{N_n} \bigr\|}_{\text{③}} .
> $$
>
> For ①: both term indices lie in $\{x^{(M_j)}_n\}_n$, so by (3.2) at index $j$, if $n' \ge N_j$ (and $n \ge N_j$, which holds) then ① $< 1/j$. For ②: since $n \ge j$ and $\{M_n\}$ is non-decreasing, $M_n \ge M_j$, so (3.1) at index $j$ with $m = M_n$ gives $\lim_{n'} \|x^{(M_j)}_{n'} - x^{(M_n)}_{n'}\| < 1/j$, and there is $P$ (depending on $j$ and $n$) with ② $< 1/j$ for all $n' \ge P$. For ③: both term indices lie in $\{x^{(M_n)}_{n'}\}_{n'}$, so by (3.2) at index $n$, if $n' \ge N_n$ then ③ $< 1/n$. Taking $n' \ge \max\{N_j, N_n, P\}$, all three bounds hold and $n'$ disappears:
>
> $$
> \bigl\| x^{(M_j)}_n - x^{(M_n)}_{N_n} \bigr\| < \frac{2}{j} + \frac{1}{n} \qquad \text{for all } n \ge \max\{j, N_j\}.
> $$
>
> Letting $n \to \infty$, Ⓑ $\le 2/j$.
>
> *Conclusion.* By (3.3), for every $m \ge M_j$, $\|[\{x^{(m)}_n\}] - [\{y_n\}]\|_{\overline{X}} < 1/j + 2/j = 3/j < \varepsilon$. So the Cauchy sequence converges in $\overline{X}$ to $[\{y_n\}]$, and $(\overline{X}, \|\cdot\|_{\overline{X}})$ is complete; with Steps 5 and 6 it is a Banach space.

^pf-13-1

*Uses:* [[§11 Normed Linear Spaces#^lem-11-3|§11.3]], [[§11 Normed Linear Spaces#^def-11-1|Def. §11.1]], [[§11 Normed Linear Spaces#^def-11-5|Def. §11.5]], [[§12 Completeness#^def-12-1|Def. §12.1]], [[§12 Completeness#^def-12-3|Def. §12.3]], [[§12 Completeness#^def-12-4|Def. §12.4]], [[§1 Linear Spaces#^def-1-1|Def. §1.1]], [[§10a Cauchy Sequences#^thm-10a-3|451 §10a.3]] (completeness of $\mathbb{R}$)

> [!remark]- Connections
> - The same construction for $\mathbb{Q} \subset \mathbb{R}$: [[§10a Cauchy Sequences#^rem-10a-4|451 Remark (construction of the reals)]]; there $\Phi = \lim$ is [[§6★ ℝ from Cauchy Sequences of Rationals#^thm-6s-12|451 Theorem §6★.12]], and uniqueness is [[§6★ ℝ from Cauchy Sequences of Rationals#^cor-6s-14|451 §6★.14]].
> - The pattern of the proof: [[Functional Analysis Problem-Solving Techniques#^ex-t5|Technique 5, applications]].

> [!remark] Remark: Comparison with the $\ell^p$ Proof
> The structure is the one from Theorem [[§18 Minkowski's Inequality and the Spaces ℓᵖ#^thm-18-5|§18.5]], with the roles shifted. In $\ell^p$ the candidate came from coordinates and the closing step needed a uniform tail estimate obtained by truncating. Here the candidate is a *diagonal* sequence $y_j = x^{(M_j)}_{N_j}$: one term from each representative, chosen far enough out that within-representative fluctuations (3.2) and between-representative distances (3.1) are both below $1/j$. The closing step is the same three-term triangle inequality used twice, with an auxiliary index $n'$ that is sent far out after everything else is fixed and then disappears. The two monotone index sequences $M_j, N_j$ are what make “$m = M_n \ge M_j$ when $n \ge j$” available; without the $\max$ in their definition the comparisons in (3.1) could not be applied in the direction needed.

^rem-13-2

> [!remark] Remark
> A student asked whether one could define the norm of a class as the norm of its limit. There is no limit in $X$ to speak of — that is the whole reason for the construction — so the definition must be phrased in terms of the sequence itself, and existence of $\lim \|x_n\|$ is then a claim to prove, not a definition. The relevant estimate is the reverse triangle inequality (Lemma [[§11 Normed Linear Spaces#^lem-11-3|§11.3]]), $\bigl|\,\|x_m\| - \|x_k\|\,\bigr| \le \|x_m - x_k\|$, which makes $\{\|x_n\|\}$ a Cauchy sequence of real numbers.

^rem-13-3

## Identifying a Completion

The construction by equivalence classes is abstract, but in practice the completion of a concrete space can almost always be written down as a concrete space. The following proposition is the tool: if the space is already sitting densely inside something complete, that something *is* the completion.

> [!theorem] Proposition §13.2: Identifying a Completion
> Let $(X, \|\cdot\|_X)$ be a normed linear space, $(Z, \|\cdot\|_Z)$ a Banach space, and $J : X \to Z$ a linear map with $\|Jx\|_Z = \|x\|_X$ for all $x \in X$, such that $J(X)$ is dense in $Z$. Then
>
> $$
> \Phi : \overline{X} \to Z, \qquad \Phi\bigl([\{x_n\}]\bigr) = \lim_{n \to \infty} J x_n,
> $$
>
> is an isometric isomorphism of $\overline{X}$ onto $Z$, and it sends the class of the constant sequence $(x, x, \ldots)$ to $Jx$. In particular, if $X \subset Z$ is a dense linear subspace carrying the restricted norm ($J$ the inclusion), then $\overline{X}$ is isometrically isomorphic to $Z$ by an isomorphism that is the identity on $X$.

^prop-13-2

> [!proof]+ Proof
> (Not covered in lecture.) *The limit exists.* If $\{x_n\}$ is Cauchy in $X$, then $\|Jx_n - Jx_m\|_Z = \|J(x_n - x_m)\|_Z = \|x_n - x_m\|_X$, so $\{Jx_n\}$ is Cauchy in $Z$, and it converges because $Z$ is complete.
>
> *Well defined.* If $\{x_n\} \sim \{x_n'\}$ then $\|Jx_n - Jx_n'\|_Z = \|x_n - x_n'\|_X \to 0$, so the two limits coincide.
>
> *Linear.* The operations on $\overline{X}$ are termwise, $J$ is linear, and limits in $Z$ are linear.
>
> *Isometric.* By continuity of the norm (Proposition [[§11 Normed Linear Spaces#^prop-11-4|§11.4]]),
>
> $$
> \|\Phi([\{x_n\}])\|_Z = \lim_n \|Jx_n\|_Z = \lim_n \|x_n\|_X = \|[\{x_n\}]\|,
> $$
>
> the last equality being the definition of the norm on $\overline{X}$. An isometry is injective: $\Phi(\xi) = 0$ forces $\|\xi\| = 0$, hence $\xi = 0$.
>
> *Surjective.* Let $z \in Z$. By density there are $x_n \in X$ with $Jx_n \to z$. A convergent sequence is Cauchy (Proposition [[§11 Normed Linear Spaces#^prop-11-5|§11.5]]), and $\|x_n - x_m\|_X = \|Jx_n - Jx_m\|_Z$, so $\{x_n\}$ is Cauchy in $X$ and $\Phi([\{x_n\}]) = z$.
>
> Finally $\Phi([(x, x, \ldots)]) = \lim_n Jx = Jx$.

^pf-13-2

*Uses:* [[§13 The Completion of a Normed Space#^thm-13-1|§13.1]], [[§12 Completeness#^def-12-3|Def. §12.3]], [[§12 Completeness#^def-12-4|Def. §12.4]], [[§11 Normed Linear Spaces#^prop-11-4|§11.4]], [[§11 Normed Linear Spaces#^prop-11-5|§11.5]], [[§11 Normed Linear Spaces#^def-11-7|Def. §11.7]], [[§11 Normed Linear Spaces#^def-11-8|Def. §11.8]], [[§3 Linear Maps, Convexity, and Linear Functionals#^def-3-1|Def. §3.1]]

> [!remark]- Connections
> - Used for concrete completions: [[§13 The Completion of a Normed Space#^prop-13-4|§13.4]] ($C^1$), [[§19 The Function Spaces Lᵖ(Ω)#^prop-19-8|§19.8]] ($L^p$).

> [!remark] Remark
> The embedding form is needed in practice: an element of $L^p[a,b]$ is a class of functions equal almost everywhere, so $C[a,b]$ is not literally a subset of $L^p[a,b]$; it sits inside via $f \mapsto [f]$. The proposition is the precise meaning of “$Z$ *is* the completion of $X$”: the abstract $\overline{X}$ and the concrete $Z$ are the same Banach space, with $X$ corresponding to $J(X)$.

^rem-13-4

> [!theorem] Corollary §13.3: Uniqueness of the Completion
> Let $X$ be a normed linear space. If $Z_1$ and $Z_2$ are Banach spaces each containing $X$ as a dense subspace with the same norm, then $Z_1$ and $Z_2$ are isometrically isomorphic by a map fixing $X$. In this sense the completion of $X$ is unique.

^cor-13-3

> [!proof]+ Proof
> (Stated in lecture without proof; the proof is not from lecture.) Both are isometrically isomorphic to $\overline{X}$ by Proposition [[§13 The Completion of a Normed Space#^prop-13-2|§13.2]]; compose one isomorphism with the inverse of the other (Lemma [[§3 Linear Maps, Convexity, and Linear Functionals#^lem-3-1|§3.1]]).

^pf-13-3

*Uses:* [[§13 The Completion of a Normed Space#^prop-13-2|§13.2]], [[§3 Linear Maps, Convexity, and Linear Functionals#^lem-3-1|§3.1]]

> [!remark] Remark: “How Do We Know We Have Not Added Too Much?”
> This was asked in lecture, and Corollary [[§13 The Completion of a Normed Space#^cor-13-3|§13.3]] is the answer: there is no freedom. The construction adds only limits of Cauchy sequences in $X$ and identifies two sequences whenever they head for the same place, so nothing extra can appear.
>
> A larger complete space containing $X$ need not be the completion. A student's example: with the usual absolute value, the completion of $\mathbb{Q}$ is $\mathbb{R}$, and $\mathbb{R} \subset \mathbb{C}$ with $\mathbb{C}$ complete — but $\mathbb{C}$ is not the completion of $\mathbb{Q}$, because a Cauchy sequence of rationals cannot converge to a non-real number. Equivalently in Wu's version, $\mathbb{R} \subset \mathbb{R}^2$ is a complete space containing $\mathbb{R}$, and is not its completion. The condition that fails is density.
>
> Also worth separating: the definition of $\overline{X}$ is by equivalence classes, and the description “$X$ together with all its limit points” is a way of thinking, not a definition — before the construction there is no ambient space in which those limit points live. Wu: “the previous one is more precise; the later one is a way of thinking. What is the limit when you don't even have a point?”

^rem-13-5

> [!remark] Remark: The Norm Decides, Not the Set
> A second trap. As *sets*, $C[a,b] \subset L^1[a,b]$, and $L^1[a,b]$ is complete; but $L^1[a,b]$ is not the completion of $\bigl(C[a,b], \|\cdot\|_\infty\bigr)$, which is already complete (Theorem [[§12 Completeness#^thm-12-1|§12.1]]) and is therefore its own completion. The two norms $\|\cdot\|_\infty$ and $\|\cdot\|_{L^1}$ are not [[§14 New Normed Spaces from Old#^def-14-1|equivalent]], so they give different topologies, different Cauchy sequences, and different completions. A normed linear space is the pair $(X, \|\cdot\|)$, never the set alone; the completion is determined by the norm. The same set $C[a,b]$ with the $L^p$ norm, $1 \le p < \infty$, does have completion $L^p[a,b]$ ([[§19 The Function Spaces Lᵖ(Ω)#^prop-19-8|§19.8]]).

^rem-13-6

## An Incomplete Normed Space

> [!example] Example §13.1: $C^2[a,b]$ with a $C^1$ Norm
> Let $C^k[a,b]$ denote the $k$ times continuously differentiable functions on $[a,b]$. The natural norm on $C^2[a,b]$ is
>
> $$
> \|f\|_{C^2[a,b]} = \max_{[a,b]} |f| + \max_{[a,b]} |f'| + \max_{[a,b]} |f''|,
> $$
>
> and $(C^2[a,b], \|\cdot\|_{C^2})$ is complete, by the same argument as for $C[a,b]$ (Theorem [[§12 Completeness#^thm-12-1|§12.1]]) applied to $f$, $f'$, $f''$ simultaneously. But the set $X = C^2[a,b]$ may also be given the smaller norm
>
> $$
> \|f\|_X = \max_{[a,b]} |f| + \max_{[a,b]} |f'|,
> $$
>
> which omits the second derivative, and $(X, \|\cdot\|_X)$ is a normed linear space that is *not* complete. This is another instance of the previous remark: the same set, two inequivalent norms, one complete and one not.

^ex-13-1

> [!theorem] Proposition §13.4: $(C^2[a,b], \|\cdot\|_X)$ is Not Complete
> With $\|f\|_X = \max |f| + \max |f'|$, the space $X = C^2[a,b]$ is not complete, and its completion is $C^1[a,b]$ with the same norm.
>
> *Source: HW3, Problem 2*

^prop-13-4

> [!proof]+ Proof
> (HW3, Problem 2.)
> Throughout, $C^k([a,b])$ ($k = 1, 2$) denotes the functions $f : [a,b] \to \mathbb{F}$ that are $k$ times differentiable on $[a,b]$ (one-sided at the endpoints) with $f^{(k)}$ continuous, and $\|g\|_\infty = \max_{[a,b]} |g|$ for $g \in C([a,b])$; $(C([a,b]), \|\cdot\|_\infty)$ is a Banach space (Theorem [[§12 Completeness#^thm-12-1|§12.1]]). Write $\|f\| = \|f\|_X = \|f\|_\infty + \|f'\|_\infty$. For complex-valued functions, differentiation and integration act on real and imaginary parts, so the fundamental theorem of calculus holds, and $\bigl|\int_\alpha^\beta h\bigr| \leq \int_\alpha^\beta |h|$ for continuous $h$. We show that $(X, \|\cdot\|)$ is a normed linear space, that it is *not* complete, and that its completion is $C^1([a,b])$ with the same norm.
>
> **Part 1: $(X, \|\cdot\|)$ is a normed linear space.** If $f, g \in X$ and $c \in \mathbb{F}$, then $(f + g)' = f' + g'$, $(f+g)'' = f'' + g''$, $(cf)' = cf'$ and $(cf)'' = cf''$, all continuous; so $X$ is a linear subspace of $C([a,b])$, hence a linear space. The norm is well defined because $f$ and $f'$ are continuous on $[a,b]$, so both maxima exist.
>
> *Positivity.* $\|f\| \geq 0$. If $\|f\| = 0$, then $\|f\|_\infty = 0$, since both terms are non-negative; so $f = 0$.
>
> *Homogeneity.* $\|cf\| = \|cf\|_\infty + \|cf'\|_\infty = |c|\,\|f\|_\infty + |c|\,\|f'\|_\infty = |c|\,\|f\|$.
>
> *Triangle inequality.* By the triangle inequality for $\|\cdot\|_\infty$,
>
> $$\|f + g\| = \|f + g\|_\infty + \|f' + g'\|_\infty \leq \|f\|_\infty + \|g\|_\infty + \|f'\|_\infty + \|g'\|_\infty = \|f\| + \|g\|.$$
>
> The same computations, which use only the first derivative, show that $\|\cdot\|$ is also a norm on $C^1([a,b])$. Write $Z = (C^1([a,b]), \|\cdot\|)$; then $X \subset Z$, with the same norm.
>
> **Part 2: $Z$ is complete.** Let $\{f_n\}$ be Cauchy in $Z$. Since $\|f_n - f_m\|_\infty \leq \|f_n - f_m\|$ and $\|f_n' - f_m'\|_\infty \leq \|f_n - f_m\|$, both $\{f_n\}$ and $\{f_n'\}$ are Cauchy in $(C([a,b]), \|\cdot\|_\infty)$, which is complete. So there are $f, g \in C([a,b])$ with
>
> $$\|f_n - f\|_\infty \to 0, \qquad \|f_n' - g\|_\infty \to 0.$$
>
> By the fundamental theorem of calculus, for every $n$ and every $x \in [a,b]$,
>
> $$f_n(x) = f_n(a) + \int_a^x f_n'(t)\,dt.$$
>
> Fix $x$. As $n \to \infty$, $f_n(x) \to f(x)$, $f_n(a) \to f(a)$, and
>
> $$\Bigl| \int_a^x f_n'(t)\,dt - \int_a^x g(t)\,dt \Bigr| \leq \int_a^x |f_n' - g| \leq (b - a)\,\|f_n' - g\|_\infty \to 0.$$
>
> Hence
>
> $$f(x) = f(a) + \int_a^x g(t)\,dt \qquad \text{for all } x \in [a,b].$$
>
> Since $g$ is continuous, the fundamental theorem of calculus shows that $f$ is differentiable on $[a,b]$ with $f' = g$. So $f \in C^1([a,b])$, and
>
> $$\|f_n - f\| = \|f_n - f\|_\infty + \|f_n' - g\|_\infty \to 0.$$
>
> Thus $Z$ is complete.
>
> **Part 3: $X$ is dense in $Z$.** Let $f \in C^1([a,b])$ and $\varepsilon > 0$. Since $f'$ is continuous on $[a,b]$, the [[§27 Weierstrass's Approximation Theorem (Not Covered)|Weierstrass approximation theorem]] (applied to the real and imaginary parts if $\mathbb{F} = \mathbb{C}$) gives a polynomial $P$ with
>
> $$\|P - f'\|_\infty < \frac{\varepsilon}{1 + b - a}.$$
>
> Define
>
> $$q(x) = f(a) + \int_a^x P(t)\,dt, \qquad x \in [a,b].$$
>
> Then $q$ is a polynomial, so $q \in C^2([a,b]) = X$, and $q' = P$. Using $f(x) = f(a) + \int_a^x f'(t)\,dt$,
>
> $$|q(x) - f(x)| = \Bigl| \int_a^x \bigl( P(t) - f'(t) \bigr)\,dt \Bigr| \leq (b - a)\,\|P - f'\|_\infty \qquad \text{for all } x \in [a,b].$$
>
> Hence
>
> $$\|q - f\| = \|q - f\|_\infty + \|P - f'\|_\infty \leq (1 + b - a)\,\|P - f'\|_\infty < \varepsilon.$$
>
> **Part 4: $X \neq Z$.** Let $c = (a+b)/2$ and $\varphi(x) = |x - c|^{3/2}$. For $x \neq c$, the chain rule gives $\varphi'(x) = \frac32 \operatorname{sgn}(x - c)\,|x - c|^{1/2}$. At $x = c$,
>
> $$\Bigl| \frac{\varphi(c + h) - \varphi(c)}{h} \Bigr| = |h|^{1/2} \xrightarrow[h \to 0]{} 0,$$
>
> so $\varphi'(c) = 0$. Thus $\varphi'(x) = \frac32 \operatorname{sgn}(x - c)\,|x - c|^{1/2}$ for all $x$ (with $\operatorname{sgn} 0 = 0$), and $\varphi'$ is continuous on $[a,b]$: it is continuous away from $c$, and $|\varphi'(x)| = \frac32 |x - c|^{1/2} \to 0 = \varphi'(c)$ as $x \to c$. So $\varphi \in C^1([a,b])$. However,
>
> $$\frac{\varphi'(c + h) - \varphi'(c)}{h} = \frac32 \cdot \frac{\operatorname{sgn}(h)\,|h|^{1/2}}{h} = \frac32\,|h|^{-1/2} \xrightarrow[h \to 0]{} \infty,$$
>
> so $\varphi'$ is not differentiable at $c$, and $\varphi \notin C^2([a,b])$.
>
> **Part 5: conclusion.**
>
> *$X$ is not complete.* By Part 3 there are $q_n \in X$ with $\|q_n - \varphi\| \to 0$. The sequence $\{q_n\}$ is Cauchy in $X$, since $\|q_n - q_m\| \leq \|q_n - \varphi\| + \|\varphi - q_m\|$. If it converged in $X$ to some $h \in X$, then, as $X$ carries the norm of $Z$, it would converge in $Z$ to both $h$ and $\varphi$. Limits in a metric space are unique, so $\varphi = h \in X$, contradicting Part 4. Hence $(X, \|\cdot\|)$ is not complete.
>
> *The completion.* The inclusion $J : X \to Z$ is linear and norm-preserving, $J(X) = X$ is dense in $Z$ by Part 3, and $Z$ is a Banach space by Part 2. By Proposition [[§13 The Completion of a Normed Space#^prop-13-2|§13.2]], the completion of $(X, \|\cdot\|)$ is
>
> $$\Bigl( C^1([a,b]),\ \|f\| = \max_{t \in [a,b]} |f(t)| + \max_{t \in [a,b]} |f'(t)| \Bigr).$$

^pf-13-4

*Uses:* [[§12 Completeness#^thm-12-1|§12.1]], [[§13 The Completion of a Normed Space#^prop-13-2|§13.2]], [[§1 Linear Spaces#^def-1-2|Def. §1.2]], [[§11 Normed Linear Spaces#^def-11-1|Def. §11.1]], [[§11 Normed Linear Spaces#^prop-11-5|§11.5]], [[§12 Completeness#^def-12-1|Def. §12.1]], [[Fundamental Theorem of Calculus|451 Fundamental Theorem of Calculus]], [[§33 Properties of the Riemann Integral#^thm-33-4|451 §33.4]], [[§27 Weierstrass's Approximation Theorem (Not Covered)|451 §27 (Weierstrass approximation)]]
