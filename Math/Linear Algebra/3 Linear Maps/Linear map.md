---
subject: math
type: definition
source: "[[Linear Algebra]] 3.1"
ladr: "3.1"
page: 52
aliases: ["LADR 3.1"]
tags: [linear-algebra, ladr/3A]
---
> [!definition] 3.1 Linear map
> A *linear map* from $V$ to $W$ is a function $T:V\to W$ with
> - **additivity** $T(u+v)=Tu+Tv$ for all $u,v\in V$;
> - **homogeneity** $T(\lambda v)=\lambda(Tv)$ for all $\lambda\in\F$, $v\in V$.
>
> $\Lin(V,W)$ denotes the set of linear maps $V\to W$, and $\Lin(V)=\Lin(V,V)$.

> [!remark] Not every 'linear' function
> $f(x)=mx+b$ on $\R$ is a linear map only when $b=0$ (see [[Linear maps take 0 to 0]]). And $\cos$ is not linear, whatever one might wish about $\cos(x+y)$.

## Connections
- Determined by values on a basis: [[Linear map lemma]]. Vector space of linear maps: [[Addition and scalar multiplication on L(V, W)]]. Composition: [[Product of linear maps]].
- Two subspaces attached to every linear map: [[Null space, null T]], [[Range]], tied together by [[Fundamental theorem of linear maps]].
- Physics: observables and time evolution in quantum mechanics are linear maps on the state space.
