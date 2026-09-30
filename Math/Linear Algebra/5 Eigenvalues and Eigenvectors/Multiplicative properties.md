---
subject: math
type: theorem
source: "[[Linear Algebra]] 5.17"
ladr: "5.17"
page: 138
aliases: ["LADR 5.17"]
tags: [linear-algebra, ladr/5A]
---
> [!theorem] 5.17 Multiplicative properties
> For $p,q\in\Poly(\F)$ and $T\in\Lin(V)$:
> - (a) $(pq)(T)=p(T)q(T)$;
> - (b) $p(T)q(T)=q(T)p(T)$.

> [!remark] Informally
> Expanding a product by distributivity does not care whether the symbol is $z$ or $T$: all powers of one operator commute.

> [!proof]-
> (a) With $p(z)=\sum_ja_jz^j$ and $q(z)=\sum_kb_kz^k$, $(pq)(z)=\sum_{j,k}a_jb_kz^{j+k}$, so
> $$
> (pq)(T)=\sum_{j,k}a_jb_kT^{j+k}=\Big(\sum_ja_jT^j\Big)\Big(\sum_kb_kT^k\Big)=p(T)q(T).
> $$
> (b) $p(T)q(T)=(pq)(T)=(qp)(T)=q(T)p(T)$ by (a) twice.

## Uses (in the proof)
- (definitions only)

## Connections
- Used constantly: [[Null space and range of p(T) are invariant under T]], [[Existence of eigenvalues]], [[Q(T) = 0 ⟺ q is a polynomial multiple of the minimal polynomial]].
