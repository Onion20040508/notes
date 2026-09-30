---
subject: math
type: theorem
source: "[[Axler LADR]] 3.21"
ladr: "3.21"
page: 62
aliases: ["LADR 3.21", "rank-nullity", "rank–nullity theorem"]
tags: [linear-algebra, ladr/3B]
---
> [!theorem] 3.21 Fundamental theorem of linear maps
> Suppose $V$ is finite-dimensional and $T \in \Lin(V, W)$. Then $\range T$ is finite-dimensional and
> $$
> \dim V = \dim \nullsp T + \dim \range T.
> $$

> [!remark] Hypotheses
> Only $V$ is assumed finite-dimensional; $W$ may be infinite-dimensional. That is why "$\range T$ is finite-dimensional" is part of the conclusion rather than automatic.

> [!proof]-
> *(Filled in; implicit in Axler.)* $\nullsp T$ is a subspace of the finite-dimensional space $V$, hence finite-dimensional by [[Finite-dimensional subspaces]]. Let $u_1, \dots, u_m$ be a basis of $\nullsp T$, so $\dim \nullsp T = m$.
>
> By [[Every linearly independent list extends to a basis]], extend it to a basis $u_1, \dots, u_m, v_1, \dots, v_n$ of $V$, so $\dim V = m + n$. It remains to show that $Tv_1, \dots, Tv_n$ is a basis of $\range T$.
>
> **Spanning.** Any $v \in V$ can be written $v = a_1 u_1 + \dots + a_m u_m + b_1 v_1 + \dots + b_n v_n$. Applying $T$ kills every $u_k$ since $u_k \in \nullsp T$, so
> $$
> Tv = b_1 Tv_1 + \dots + b_n Tv_n .
> $$
> Hence $Tv_1, \dots, Tv_n$ spans $\range T$; in particular $\range T$ is finite-dimensional.
>
> **Linear independence.** Suppose $c_1 Tv_1 + \dots + c_n Tv_n = 0$. By linearity $T(c_1 v_1 + \dots + c_n v_n) = 0$, so $c_1 v_1 + \dots + c_n v_n \in \nullsp T$ and we can write
> $$
> c_1 v_1 + \dots + c_n v_n = d_1 u_1 + \dots + d_m u_m .
> $$
> Moving everything to one side gives a linear combination of the basis $u_1, \dots, u_m, v_1, \dots, v_n$ equal to $0$, so all $c_j$ (and $d_k$) are $0$.
>
> Therefore $\dim \range T = n$, and $\dim V = m + n = \dim \nullsp T + \dim \range T$.

## Uses (cited in Axler's proof)
- [[Every linearly independent list extends to a basis]] (2.32)
- [[Finite-dimensional subspaces]] (2.25, implicit)

## Connections
- **Immediate consequences.** Comparing dimensions: [[Linear map to a lower-dimensional space is not injective]] (3.22), [[Linear map to a higher-dimensional space is not surjective]] (3.24), [[Injectivity is equivalent to surjectivity (if dim V = dim W ＜ ∞)]] (3.65).
- **Isomorphism classes.** [[Dimension shows whether vector spaces are isomorphic]] (3.70) uses it to show isomorphic ⟺ equal dimension.
- **Matrix form.** With [[Dimension of range T equals column rank of M(T)]] (3.78), it becomes the matrix rank–nullity