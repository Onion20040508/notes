---
subject: math
type: theorem
source: "[[Linear Algebra]] 2.43"
ladr: "2.43"
page: 47
aliases: ["LADR 2.43"]
tags: [linear-algebra, ladr/2C]
---
> [!theorem] 2.43 Dimension of a sum
> If $V_1,V_2$ are subspaces of a finite-dimensional vector space, then
> $$
> \dim(V_1+V_2)=\dim V_1+\dim V_2-\dim(V_1\cap V_2).
> $$

> [!remark] Analogy and its limit
> This mirrors $|A\cup B|=|A|+|B|-|A\cap B|$. The analogue of inclusion–exclusion fails for three subspaces (three distinct lines in $\R^2$ are a counterexample).

> [!proof]-
> Let $v_1,\dots,v_m$ be a basis of $V_1\cap V_2$. Extend it to a basis $v_1,\dots,v_m,u_1,\dots,u_j$ of $V_1$ and to a basis $v_1,\dots,v_m,w_1,\dots,w_k$ of $V_2$ ([[Every linearly independent list extends to a basis]]). We claim
> $$
> v_1,\dots,v_m,\;u_1,\dots,u_j,\;w_1,\dots,w_k \tag{$*$}
> $$
> is a basis of $V_1+V_2$; then $\dim(V_1+V_2)=m+j+k=(m+j)+(m+k)-m$.
>
> **Spans.** The span of $(*)$ lies in $V_1+V_2$ and contains both $V_1$ and $V_2$, hence equals $V_1+V_2$ ([[Sum of subspaces is the smallest containing subspace]]).
>
> **Independent.** Suppose $\sum a_iv_i+\sum b_iu_i+\sum c_iw_i=0$. Then $\sum c_iw_i=-\sum a_iv_i-\sum b_iu_i\in V_1$, and also $\in V_2$, so $\sum c_iw_i\in V_1\cap V_2$ and $\sum c_iw_i=\sum d_iv_i$ for some $d_i$. Since $v_1,\dots,v_m,w_1,\dots,w_k$ is independent, all $c_i=0$ (and $d_i=0$). Then $\sum a_iv_i+\sum b_iu_i=0$, and independence of the basis of $V_1$ gives all $a_i=b_i=0$.

## Uses (in the proof)
- [[Every linearly independent list extends to a basis]] (2.32)
- [[Sum of subspaces is the smallest containing subspace]] (1.40)

## Connections
- Direct-sum case: [[A sum is a direct sum if and only if dimensions add up]] ($\dim(V_1+V_2)=\dim V_1+\dim V_2 \iff V_1\cap V_2=\{0\}$).
- Alternative proof via [[Fundamental theorem of linear maps]]: apply it to $T:V_1\times V_2\to V$, $T(x,y)=x+y$. Then $\range T=V_1+V_2$, $\nullsp T=\{(x,-x):x\in V_1\cap V_2\}\cong V_1\cap V_2$, and $\dim(V_1\times V_2)=\dim V_1+\dim V_2$ by [[Dimension of a product is the sum of dimensions]].
