---
subject: math
type: theorem
source: "[[Linear Algebra]] 1.27"
ladr: "1.27"
page: 15
aliases: ["LADR 1.27"]
tags: [linear-algebra, ladr/1B]
---
> [!theorem] 1.27 Unique additive inverse
> Every element of a vector space has a unique additive inverse.

> [!proof]-
> Let $v\in V$ and let $w,w'$ both be additive inverses of $v$. Then
> $$
> w=w+0=w+(v+w')=(w+v)+w'=0+w'=w'.
> $$

## Uses (in the proof)
- (definitions only)

## Connections
- Makes the notation $-v$ and $w-v:=w+(-v)$ legitimate (notation 1.28).
- Computed concretely in [[The number −1 times a vector]]: $-v=(-1)v$.
