---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 4
section: 32
tags: [differentiable-manifolds, math591]
---
← [[§31 Tangent Vectors as Velocities of Curves]] · ↑ [[· 4 Tangent and Cotangent Spaces]] · [[§33 Covectors in Coordinates]] →

*Stage: abstract, dual — The cotangent space as the dual of the tangent space, and the differential of a function as a covector; in coordinates ([[§33 Covectors in Coordinates|§33]]) and from germs alone ([[§34 The Cotangent Space from Germs|§34]]) after this.*

## Differentials of Functions and the Cotangent Space

*Lecture 10: “a very special case — a very important case.” The target is $N = \mathbb{R}$, and the differential of a scalar function becomes a covector.*

The target $\mathbb{R}$ is itself a smooth manifold, so $f_{\ast p}$ lands in a tangent space of $\mathbb{R}$. The lecture disposed of these tangent spaces in one line — “we identify this with $\mathbb{R}$ forever” — and the next three boxes spell that line out: the chart and coordinate of $\mathbb{R}$, its coordinate derivation, and the identification.

> [!definition] Definition §32.1: The Standard Coordinate on $\mathbb{R}$
> $\mathbb{R}$ is a smooth $1$-manifold, with the smooth structure of the single global chart $(\mathbb{R}, \mathrm{id}_\mathbb{R})$ ([[§22 The Differential of a Map Between Vector Spaces#^def-22-4|Definition §22.4]], with $X = \mathbb{R}$ and $L = \mathrm{id}_\mathbb{R}$). Its [[§29 Coordinate Derivations and the Basis Theorem#^def-29-1|coordinate function]] is written $r$:
>
> $$
> r : \mathbb{R} \to \mathbb{R}, \qquad r(t) = t .
> $$
>
> Because the chart is the identity, a smooth function $h$ on an open subset of $\mathbb{R}$ is its own coordinate representation: $h_{\mathrm{id}} = h \circ \mathrm{id}^{-1} = h$.

^def-32-1

> [!definition] Definition §32.2: The Coordinate Derivation on $\mathbb{R}$
> For $c \in \mathbb{R}$, $\partial/\partial r|_c \in T_c\mathbb{R}$ is the [[§29 Coordinate Derivations and the Basis Theorem#^def-29-2|coordinate derivation]] of the chart $(\mathbb{R}, \mathrm{id}_\mathbb{R})$ at $c$. Since $h_{\mathrm{id}} = h$ ([[§32 The Cotangent Space#^def-32-1|Definition §32.1]]), it is the ordinary derivative at $c$:
>
> $$
> \frac{\partial}{\partial r}\Big|_c [h] = h'(c) \qquad \text{for every germ } [h] \text{ at } c .
> $$
>
> In particular $\partial/\partial r|_c\,[r] = r'(c) = 1$.

^def-32-2

> [!theorem] Proposition §32.1: The Tangent Spaces of $\mathbb{R}$
> Let $c \in \mathbb{R}$.
> 1. $T_c\mathbb{R}$ ([[§28 Derivations and the Abstract Tangent Space#^def-28-2|abstract tangent space]]) is one-dimensional, with basis $\{\partial/\partial r|_c\}$.
> 2. Every $v \in T_c\mathbb{R}$ is $v = v[r]\,\partial/\partial r|_c$: its coefficient on the basis vector is its value on the coordinate function $r$.
> 3. The map $\iota_c : T_c\mathbb{R} \to \mathbb{R}$, $\iota_c(v) = v[r]$, is a linear isomorphism, with $\iota_c\big(a\,\partial/\partial r|_c\big) = a$ for $a \in \mathbb{R}$ and inverse $a \mapsto a\,\partial/\partial r|_c$.

^prop-32-1

> [!proof]+ Proof
> *(Not from lecture; filled in.)* (1) and (2) are the Basis Theorem ([[§29 Coordinate Derivations and the Basis Theorem#^thm-29-5|Theorem §29.5]]) for the chart $(\mathbb{R}, \mathrm{id}_\mathbb{R})$, with $n = 1$ and $x^1 = r$; (2) is its universal formula. (3) $\iota_c$ is linear because the vector-space operations of $T_c\mathbb{R}$ are pointwise on germs ([[§28 Derivations and the Abstract Tangent Space#^def-28-2|Definition §28.2]]): $(v + w)[r] = v[r] + w[r]$ and $(av)[r] = a\,v[r]$. By [[§32 The Cotangent Space#^def-32-2|Definition §32.2]], $\iota_c(a\,\partial/\partial r|_c) = a \cdot 1 = a$, so $\iota_c$ is surjective, and $a \mapsto a\,\partial/\partial r|_c$ is a right inverse; it is also a left inverse by (2), $v = \iota_c(v)\,\partial/\partial r|_c$.

^pf-32-1

*Uses:* [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-5|§29.5]], [[§28 Derivations and the Abstract Tangent Space#^def-28-2|Def. §28.2]], [[§32 The Cotangent Space#^def-32-1|Def. §32.1]], [[§32 The Cotangent Space#^def-32-2|Def. §32.2]]

> [!definition] Definition §32.3: The Standard Identification of $T_c\mathbb{R}$ with $\mathbb{R}$
> For every $c \in \mathbb{R}$, $T_c\mathbb{R}$ is identified with $\mathbb{R}$ by the isomorphism $\iota_c$ of [[§32 The Cotangent Space#^prop-32-1|Proposition §32.1]]:
>
> $$
> T_c\mathbb{R} \xrightarrow{\ \iota_c\ } \mathbb{R}, \qquad a\,\frac{\partial}{\partial r}\Big|_c \longmapsto a, \qquad \text{equivalently} \quad v \longmapsto v[r] .
> $$

^def-32-3

Concretely, $a\,\partial/\partial r|_c$ is the derivation $h \mapsto a\,h'(c)$: differentiation at $c$ at speed $a$, the [[§31 Tangent Vectors as Velocities of Curves|velocity]] of the curve $t \mapsto c + at$. The identification records the speed $a$ and forgets the base point $c$; this is why it can be made for all $c$ at once.


> [!definition] Definition §32.4: Cotangent Space
> Let $M$ be a smooth manifold and $p \in M$. The **cotangent space** of $M$ at $p$ is the dual of the abstract tangent space,
>
> $$
> T_p^*M = (T_pM)^* .
> $$
>
> *Lee: Ch. 11, Covectors*

^def-32-4

> [!definition] Definition §32.5: The Differential of a Function
> Let $M$ be a smooth manifold and $p \in M$, and let $f : M \to \mathbb{R}$ be smooth (or defined and smooth only near $p$). Its [[§28 Derivations and the Abstract Tangent Space#^def-28-6|pushforward]] at $p$ is a linear map into the tangent space of $\mathbb{R}$ at the point $f(p)$:
>
> $$
> f_{*p} : T_pM \longrightarrow T_{f(p)}\mathbb{R}, \qquad \big(f_{*p}D\big)[h] = D[\,h \circ f\,] .
> $$
>
> The **differential** of $f$ at $p$ is this map followed by the standard identification $\iota_{f(p)} : T_{f(p)}\mathbb{R} \to \mathbb{R}$ ([[§32 The Cotangent Space#^def-32-3|Definition §32.3]]):
>
> $$
> df_p = \iota_{f(p)} \circ f_{*p} : T_pM \longrightarrow \mathbb{R}, \qquad df_p(D) = \big(f_{*p}D\big)[r] .
> $$
>
> So $df_p(D)$ is the coefficient of $f_{\ast p}D$ on the basis vector $\partial/\partial r|_{f(p)}$ of $T_{f(p)}\mathbb{R}$ ([[§32 The Cotangent Space#^prop-32-1|Proposition §32.1]]): $f_{\ast p}D = df_p(D)\,\partial/\partial r|_{f(p)}$. As a composite of linear maps, $df_p$ is linear, so $df_p \in T_p^{\ast}M$, the [[§32 The Cotangent Space#^def-32-4|cotangent space]] of Definition §32.4. [[§32 The Cotangent Space#^prop-32-2|Proposition §32.2]] computes it: $df_p(D) = D[f]$.
>
> *Lee: Ch. 11, Covectors*

^def-32-5

![[m591-13-1.svg]]
*The differential of a function is its pushforward followed by the permanent identification of every tangent space of $\mathbb{R}$ with $\mathbb{R}$; so $df_p$ is the pushforward $f_{\ast p}$ under another name. The notation $T_p^{\ast}M$ puts the star on the $T$ “to save some ink.”*

> [!remark]- Connections
> - The linear algebra: the dual space is [[§12 Duality#^ladr-3-110|LADR 3.110]].
> - In multivariable calculus: [[§10 The Differential#^def-10-1|452 Def. §10.1]] and [[§39 Closed and Exact Forms#^prop-39-1|452 §39.1 (gradient = differential = 1-form)]].
> - Assembled over all of $M$: the cotangent bundle, [[§48 The Cotangent Bundle#^def-48-1|Def. §48.1]].
> - Used in Relativity: the differential of a scalar field is why its gradient $\partial_\mu\phi$ carries a lower index — [[§B2.2 Tensors and the Covariance Principle#^rem-b2-2-5|REL Remark: Why the gradient carries a lower index]], [[§B2.2 Tensors and the Covariance Principle#^thm-b2-2-6|REL Theorem §B2.2.6]].

> [!theorem] Proposition §32.2: The Differential Evaluates Derivations
> For every $D \in T_pM$, $\ df_p(D) = D[f]$. In particular $df_p\big(\partial/\partial x^j|_p\big) = \partial f/\partial x^j(p)$ in any chart.
>
> *Lee: Ch. 11, Covectors*

^prop-32-2

> [!proof]+ Proof
> By [[§32 The Cotangent Space#^def-32-5|Definition §32.5]] and the definition of the pushforward ([[§28 Derivations and the Abstract Tangent Space#^def-28-6|Definition §28.6]]), $df_p(D) = (f_{*p}D)[r] = D[r \circ f] = D[f]$, since $r \circ f = f$ ($r$ is the identity of $\mathbb{R}$, [[§32 The Cotangent Space#^def-32-1|Definition §32.1]]). For $D = \partial/\partial x^j|_p$ this is $\partial/\partial x^j|_p\,[f] = \partial f/\partial x^j(p)$ ([[§29 Coordinate Derivations and the Basis Theorem#^def-29-2|Definition §29.2]]).

^pf-32-2

*Uses:* [[§32 The Cotangent Space#^def-32-5|Def. §32.5]], [[§28 Derivations and the Abstract Tangent Space#^def-28-6|Def. §28.6]], [[§32 The Cotangent Space#^def-32-1|Def. §32.1]], [[§29 Coordinate Derivations and the Basis Theorem#^def-29-2|Def. §29.2]]

> [!theorem] Corollary §32.3: Properties of the Differential of a Function
> Let $f, g$ be smooth near $p$ and $a, b \in \mathbb{R}$.
> 1. *Linearity:* $d(af + bg)_p = a\,df_p + b\,dg_p$.
> 2. *Product rule:* $d(fg)_p = f(p)\,dg_p + g(p)\,df_p$.
> 3. *Chain rule:* if $h$ is smooth on an open interval containing the values of $f$ near $p$, then $d(h \circ f)_p = h'(f(p))\,df_p$.
>
> *Lee: Proposition 11.20*

^cor-32-3

> [!proof]+ Proof
> *(Not from lecture; filled in.)* All three are equalities in $T_p^{\ast}M = (T_pM)^{\ast}$ ([[§32 The Cotangent Space#^def-32-4|Definition §32.4]]), whose elements are functions on $T_pM$; two of them are equal when they take the same value at every $D \in T_pM$, and sums and scalar multiples in a dual space are taken pointwise, $(a\alpha + b\beta)(D) = a\,\alpha(D) + b\,\beta(D)$ ([[§21 Linear Algebra Toolkit#^def-21-1|Definition §21.1]]). So fix $D \in T_pM$. Each step below uses one of: [[§32 The Cotangent Space#^prop-32-2|Proposition §32.2]], $dk_p(D) = D[k]$ for any $k$ smooth near $p$; the algebra operations on [[§27 Germs#^def-27-2|germs]] ([[§27 Germs#^prop-27-2|Proposition §27.2]]), $[af + bg] = a[f] + b[g]$ and $[fg] = [f][g]$; and the two defining properties of the [[§28 Derivations and the Abstract Tangent Space#^def-28-1|derivation]] $D$ ([[§28 Derivations and the Abstract Tangent Space#^def-28-1|Definition §28.1]]).
>
> *(1)* By $\mathbb{R}$-linearity of $D$:
>
> $$
> d(af + bg)_p(D) = D\big[af + bg\big] = D\big(a[f] + b[g]\big) = a\,D[f] + b\,D[g] = a\,df_p(D) + b\,dg_p(D) = \big(a\,df_p + b\,dg_p\big)(D).
> $$
>
> *(2)* By the Leibniz rule $D([f][g]) = f(p)\,D[g] + g(p)\,D[f]$, applied to the germs $[f]$ and $[g]$:
>
> $$
> d(fg)_p(D) = D\big[fg\big] = D\big([f][g]\big) = f(p)\,D[g] + g(p)\,D[f] = f(p)\,dg_p(D) + g(p)\,df_p(D) = \big(f(p)\,dg_p + g(p)\,df_p\big)(D).
> $$
>
> Here $f(p)$ and $g(p)$ are numbers, the values of the germs at $p$, so the right side is a linear combination of the covectors $dg_p$ and $df_p$.
>
> *(3)* The composite $h \circ f$ is smooth near $p$, and $h$ is smooth near $f(p)$, so $[h]$ is a germ at $f(p)$ on $\mathbb{R}$. By the definition of the pushforward ([[§28 Derivations and the Abstract Tangent Space#^def-28-6|Definition §28.6]]), $D[h \circ f] = (f_{\ast p}D)[h]$. By [[§32 The Cotangent Space#^def-32-5|Definition §32.5]], $f_{\ast p}D = df_p(D)\,\partial/\partial r|_{f(p)}$; this is an equality of derivations at $f(p)$, so both sides take the same value on $[h]$. With [[§32 The Cotangent Space#^def-32-2|Definition §32.2]]:
>
> $$
> d(h \circ f)_p(D) = D[h \circ f] = (f_{*p}D)[h] = df_p(D)\,\frac{\partial}{\partial r}\Big|_{f(p)}[h] = df_p(D)\,h'(f(p)) = \big(h'(f(p))\,df_p\big)(D).
> $$
>
> Since $D$ was arbitrary, the three identities hold in $T_p^{\ast}M$.

^pf-32-3

*Uses:* [[§32 The Cotangent Space#^prop-32-2|§32.2]], [[§28 Derivations and the Abstract Tangent Space#^def-28-1|Def. §28.1]], [[§27 Germs#^prop-27-2|§27.2]], [[§21 Linear Algebra Toolkit#^def-21-1|Def. §21.1]], [[§28 Derivations and the Abstract Tangent Space#^def-28-6|Def. §28.6]], [[§32 The Cotangent Space#^def-32-4|Def. §32.4]], [[§32 The Cotangent Space#^def-32-5|Def. §32.5]], [[§32 The Cotangent Space#^def-32-2|Def. §32.2]]
