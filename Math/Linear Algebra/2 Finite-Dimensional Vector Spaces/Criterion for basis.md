---
subject: math
type: theorem
source: "[[Linear Algebra]] 2.28"
ladr: "2.28"
page: 39
aliases: ["LADR 2.28"]
tags: [linear-algebra, ladr/2B]
---
> [!theorem] 2.28 Criterion for basis
> A list $v_1,\dots,v_n$ in $V$ is a basis of $V$ iff every $v\in V$ can be written uniquely as
> $$
> v=a_1v_1+\dots+a_nv_n,\qquad a_1,\dots,a_n\in\F .
> $$

> [!proof]-
> ($\Rightarrow$) Spanning gives existence. If also $v=c_1v_1+\dots+c_nv_n$, subtracting gives $0=\sum(a_k-c_k)v_k$, so all $a_k=c_k$ by independence.
>
> ($\Leftarrow$) Existence of representations means the list spans. Taking $v=0$, uniqueness says $0=\sum a_kv_k$ forces all $a_k=0$ (since $0=\sum 0\,v_k$ is one representation), i.e. independence.

## Uses (in the proof)
- (definitions only)

## Connections
- The unique $a_k$ are coordinates: [[Matrix of a vector, M(v)]]. Uniqueness is also what makes [[Linear map lemma]] work.
