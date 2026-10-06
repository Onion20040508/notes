---
type: section
subject: "[[Linear Algebra]]"
chapter: 7
section: 28
aliases: ["LADR 7F", "7F Consequences of Singular Value Decomposition"]
tags: [linear-algebra]
---
← [[§27 Singular Value Decomposition]] · ↑ [[· 7 Operators on Inner Product Spaces]] · [[§29 The Operator (2w − 3z, 3w + 2z)]] →

> [!theorem] Theorem 7.82: Upper bound for ‖Tv‖
> If $s_1$ is the largest singular value of $T\in\Lin(V,W)$, then $\|Tv\|\le s_1\|v\|$ for all $v$, with equality for $v=e_1$.

^ladr-7-82

> [!proof]+ Proof
> From an SVD of $T$ ([[Singular value decomposition|7.70]]), $\|Tv\|^2=\sum_ks_k^2|\langle v,e_k\rangle|^2\le s_1^2\sum_k|\langle v,e_k\rangle|^2\le s_1^2\|v\|^2$ (Bessel, [[§21 Orthonormal Bases#^ladr-6-26|6.26]]). And $Te_1=s_1f_1$.

*Uses:* [[Singular value decomposition|7.70]], [[§21 Orthonormal Bases#^ladr-6-26|6.26]]

> [!remark]- Connections
> - Hence $\max\{\|Tv\|:\|v\|\le1\}=s_1$, motivating [[§28 Consequences of Singular Value Decomposition#^ladr-7-86|7.86]].
> - Computational version: [[§61★ The Singular Value Decomposition#^prop-61-2|235 Prop. §61.2]] ($\sigma_1$ is the maximum of $\|A\mathbf x\|$ over unit vectors).

> [!definition] Definition 7.86: Norm of a linear map, ‖⋅ ‖
> The *norm* of $T\in\Lin(V,W)$ is
> $$
> \|T\|=\max\{\|Tv\|:v\in V,\ \|v\|\le1\}.
> $$
> The maximum exists and equals the largest singular value ([[§28 Consequences of Singular Value Decomposition#^ladr-7-82|7.82]]).

^ladr-7-86

> [!remark] Remark: Not an inner-product norm
> This operator norm generally does not come from an inner product on $\Lin(V,W)$ (it fails the parallelogram law, [[§20 Inner Products and Norms#^ladr-6-21|6.21]]). The Frobenius norm $\sqrt{\operatorname{tr}T^*T}$ does.

> [!remark]- Connections
> - Same as the operator norm in functional analysis ([[§26 Boundedness and Continuity#^def-26-2|556 Def. §26.2]]): there the max becomes a sup.

> [!theorem] Theorem 7.87: Basic properties of norms of linear maps
> For $S,T\in\Lin(V,W)$: (a) $\|T\|\ge0$; (b) $\|T\|=0\iff T=0$; (c) $\|\lambda T\|=|\lambda|\|T\|$; (d) $\|S+T\|\le\|S\|+\|T\|$.

^ladr-7-87

> [!proof]+ Proof
> (a) clear. (b) If $\|T\|=0$ then $T$ kills the unit ball, so $Tu=\|u\|T(u/\|u\|)=0$ for $u\ne0$. (c) $\max\|\lambda Tv\|=|\lambda|\max\|Tv\|$. (d) Pick $v$, $\|v\|\le1$, with $\|S+T\|=\|(S+T)v\|\le\|Sv\|+\|Tv\|\le\|S\|+\|T\|$.

> [!remark] Remark: Distance
> $\|S-T\|$ is a distance on $\Lin(V,W)$; e.g. invertible operators come arbitrarily close to any $T$.

> [!remark]- Connections
> - Same properties for bounded maps between normed spaces, which make ℒ(X, Y) a normed space: [[§26 Boundedness and Continuity#^thm-26-5|556 Thm. §26.5]].

> [!theorem] Theorem 7.88: Alternative formulas for ‖T‖
> For $T\in\Lin(V,W)$:
> - (a) $\|T\|$ is the largest singular value;
> - (b) $\|T\|=\max\{\|Tv\|:\|v\|=1\}$;
> - (c) $\|T\|$ is the smallest $c$ with $\|Tv\|\le c\|v\|$ for all $v$.

^ladr-7-88

> [!proof]+ Proof
> (a) is [[§28 Consequences of Singular Value Decomposition#^ladr-7-82|7.82]]. (b) for $0<\|v\|\le1$, $u=v/\|v\|$ has $\|Tu\|=\|Tv\|/\|v\|\ge\|Tv\|$. (c) $\|T(v/\|v\|)\|\le\|T\|$ gives $\|Tv\|\le\|T\|\|v\|$; conversely if $\|Tv\|\le c\|v\|$ for all $v$, then $\|Tv\|\le c$ on the unit ball, so $\|T\|\le c$.

*Uses:* [[§28 Consequences of Singular Value Decomposition#^ladr-7-82|7.82]]

> [!remark] Remark: Computing
> (a) is the practical route: form $T^*T$, compute its largest eigenvalue numerically, take the square root.

> [!remark]- Connections
> - Parts (b) and (c) are [[§26 Boundedness and Continuity#^prop-26-1|556 Prop. §26.1]] (a) and (c), with max replaced by sup.
> - Computational version: [[§61★ The Singular Value Decomposition#^prop-61-2|235 Prop. §61.2]] (formula (b) for matrices, via [[§60★ Constrained Optimization#^thm-60-1|235 Thm. §60.1]] applied to $A^TA$).

> [!example] Example 7.90: Norms (p. 283)
> - $\|I\|=1$.
> - If $\mathcal{M}(T)$ on $\F^n$ is all $1$'s, then $\|T\|=n$: $T^*T=nT$ has largest eigenvalue $n^2$ (eigenvector $(1,\dots,1)$).
> - If $T$ has an orthonormal eigenbasis with eigenvalues $\lambda_k$, then $\|T\|=\max_k|\lambda_k|$.
> - For the $5\times5$ matrix with entries $\frac1{j^2+k}$: largest singular value $\approx0.81$, smallest $\approx9.6\times10^{-7}$ (recomputed), so $\|T\|\approx0.81$ and $\|T^{-1}\|\approx10^6$. Such matrices are *ill-conditioned*: tiny input errors can be amplified a million-fold.

^ladr-7-90

> [!remark]- Connections
> - Computational version: [[§62★ The Singular Value Decomposition in Applications#^def-62-1|235 Def. §62.1]] (the condition number $\sigma_1/\sigma_n$, the ill-conditioning of the last bullet).

> [!theorem] Theorem 7.91: Norm of the adjoint
> For $T\in\Lin(V,W)$, $\|T^*\|=\|T\|$.

^ladr-7-91

> [!proof]+ Proof
> $\|T^*w\|^2=\langle TT^*w,w\rangle\le\|TT^*w\|\|w\|\le\|T\|\|T^*w\|\|w\|$ ([[Cauchy–Schwarz inequality|6.14]], [[§28 Consequences of Singular Value Decomposition#^ladr-7-88|7.88]](c)), so $\|T^*w\|\le\|T\|\|w\|$ and $\|T^*\|\le\|T\|$. Apply to $T^*$ and use $(T^*)^*=T$.

*Uses:* [[Cauchy–Schwarz inequality|6.14]], [[§28 Consequences of Singular Value Decomposition#^ladr-7-88|7.88]]

> [!remark] Remark: Via SVD
> [[§27 Singular Value Decomposition#^ladr-7-75|7.75]] shows $T$ and $T^*$ have the same positive singular values.

> [!theorem] Theorem 7.92: Best approximation by linear map whose range has dimension ≤ k
> Let $T\in\Lin(V,W)$ with positive singular values $s_1\ge\dots\ge s_m$ and $1\le k<m$. Then
> $$
> \min\{\|T-S\|:\dim\range S\le k\}=s_{k+1},
> $$
> attained by the truncation $T_kv=\sum_{j\le k}s_j\langle v,e_j\rangle f_j$ of an SVD.

^ladr-7-92

> [!proof]+ Proof
> **$T_k$ achieves $s_{k+1}$.** By the SVD ([[Singular value decomposition|7.70]]), $\|(T-T_k)v\|^2=\sum_{j>k}s_j^2|\langle v,e_j\rangle|^2\le s_{k+1}^2\|v\|^2$ (Bessel, [[§21 Orthonormal Bases#^ladr-6-26|6.26]]), with equality at $v=e_{k+1}$.
>
> **Nothing does better.** If $\dim\range S\le k$, the $k+1$ vectors $Se_1,\dots,Se_{k+1}$ in $\range S$ are dependent ([[Length of linearly independent list ≤ length of spanning list|2.22]]): $\sum_{j\le k+1}a_jSe_j=0$ with $u=\sum a_je_j\ne0$. Then
> $$
> \|(T-S)u\|^2=\|Tu\|^2=\sum_{j\le k+1}s_j^2|a_j|^2\ge s_{k+1}^2\|u\|^2 ,
> $$
> so $\|T-S\|\ge s_{k+1}$.

*Uses:* [[Singular value decomposition|7.70]], [[§21 Orthonormal Bases#^ladr-6-26|6.26]], [[Length of linearly independent list ≤ length of spanning list|2.22]]

> [!remark] Remark: Eckart–Young
> This is the operator-norm Eckart–Young theorem: to compress a matrix to rank $k$, keep the top $k$ singular triples. Basis of PCA and image compression.

> [!theorem] Theorem 7.93: Polar decomposition
> For $T\in\Lin(V)$ there is a unitary $S\in\Lin(V)$ with
> $$
> T=S\sqrt{T^*T}.
> $$

^ladr-7-93

> [!proof]+ Proof
> Take an SVD $Tv=\sum_{k\le m}s_k\langle v,e_k\rangle f_k$ and extend $e$'s and $f$'s to orthonormal bases of $V$ ([[§21 Orthonormal Bases#^ladr-6-36|6.36]]). Define $Sv=\sum_{k\le n}\langle v,e_k\rangle f_k$: $\|Sv\|^2=\sum|\langle v,e_k\rangle|^2=\|v\|^2$, so $S$ is unitary. By [[§27 Singular Value Decomposition#^ladr-7-75|7.75]], $T^*Tv=\sum_ks_k^2\langle v,e_k\rangle e_k$, so $\sqrt{T^*T}v=\sum_ks_k\langle v,e_k\rangle e_k$ (this operator is positive with square $T^*T$; [[§25 Positive Operators#^ladr-7-39|7.39]]). Then $S\sqrt{T^*T}v=\sum_ks_k\langle v,e_k\rangle f_k=Tv$.

*Uses:* [[§21 Orthonormal Bases#^ladr-6-36|6.36]], [[§27 Singular Value Decomposition#^ladr-7-75|7.75]], [[§25 Positive Operators#^ladr-7-39|7.39]]

> [!remark] Remark: Number analogy and geometry
> $z=e^{i\theta}|z|$: every operator is a positive stretch (along the orthogonal axes $e_k$) followed by an isometry. Figure below.

> [!remark]- Connections
> - Physics/mechanics: the polar decomposition of the deformation gradient $F=RU$ into rotation and stretch in continuum mechanics.
> - Used in Quantum Field Theory: every $\lambda \in SL(2, \mathbb C)$ is $e^hU$, a boost times a rotation, which makes $SL(2, \mathbb C) \cong \mathbb R^3\times S^3$ simply connected — [[§C5a.1 Weyl Spinors and SL(2,C)#^thm-c5a-1-4|QFT Theorem §C5a.1.4]].

%% ex:7.93-fig %%
> [!example] Example: Polar decomposition pictured
> $\sqrt{T^*T}$ stretches along the orthogonal axes $e_1,e_2$ (by $s_1,s_2$), then the isometry $S$ rotates $e_k$ to $f_k$. Same $T$ as in the SVD figure.
>
> ![[ladr-7.93-polar.svg|560]]

> [!definition] Definition 7.95: Ball, B
> The *unit ball* $B=\{v\in V:\|v\|<1\}$.

^ladr-7-95

> [!definition] Definition 7.96: Ellipsoid, E(s1f1, ...,snfn), principal axes
> For an orthonormal basis $f_1,\dots,f_n$ and $s_1,\dots,s_n>0$, the *ellipsoid* with *principal axes* $s_1f_1,\dots,s_nf_n$ is
> $$
> E(s_1f_1,\dots,s_nf_n)=\Big\{v\in V:\ \frac{|\langle v,f_1\rangle|^2}{s_1^2}+\dots+\frac{|\langle v,f_n\rangle|^2}{s_n^2}<1\Big\}.
> $$
> $E(f_1,\dots,f_n)=B$ by Parseval ([[§21 Orthonormal Bases#^ladr-6-30|6.30]](b)).

^ladr-7-96

> [!example] Example 7.97: Ellipsoids (p. 287)
> - $E(2f_1,f_2)$ in $\R^2$ with the standard basis: the ellipse $x^2/4+y^2<1$.
> - $E(2f_1,f_2)$ with $f_1=\tfrac1{\sqrt2}(1,1)$, $f_2=\tfrac1{\sqrt2}(-1,1)$: the same ellipse rotated by $45^\circ$.
> - $E(4f_1,3f_2,2f_3)$ in $\R^3$ (standard basis): semi-axes $4,3,2$.
> - $E(f_1,\dots,f_n)=B$ for any orthonormal basis.

^ladr-7-97

> [!remark] Notation 7.98: T(Ω) (p. 288)
> For a function $T$ defined on $V$ and $\Omega\subseteq V$, $T(\Omega)=\{Tv : v\in\Omega\}$.

^ladr-7-98

> [!theorem] Theorem 7.99: Invertible operator takes ball to ellipsoid
> An invertible $T\in\Lin(V)$ maps $B$ onto the ellipsoid $E(s_1f_1,\dots,s_nf_n)$, where $Tv=\sum s_k\langle v,e_k\rangle f_k$ is an SVD.

^ladr-7-99

> [!proof]+ Proof
> All $s_k>0$ ([[§27 Singular Value Decomposition#^ladr-7-68|7.68]]). For $v\in B$, $\langle Tv,f_k\rangle=s_k\langle v,e_k\rangle$, so $\sum_k|\langle Tv,f_k\rangle|^2/s_k^2=\sum_k|\langle v,e_k\rangle|^2=\|v\|^2<1$. Conversely, for $w$ in the ellipsoid, $v=\sum_k\frac{\langle w,f_k\rangle}{s_k}e_k$ has $\|v\|<1$ and $Tv=w$.

*Uses:* [[§27 Singular Value Decomposition#^ladr-7-68|7.68]]

> [!remark]- Connections
> - Figure after [[Singular value decomposition|7.70]].
> - Computational version: [[§61★ The Singular Value Decomposition#^ex-61-1|235 Ex. §61.1]] (a matrix maps the unit sphere onto an ellipse whose semi-axes are the singular values).

> [!theorem] Theorem 7.101: Invertible operator takes ellipsoids to ellipsoids
> An invertible $T\in\Lin(V)$ maps every ellipsoid onto an ellipsoid.

^ladr-7-101

> [!proof]+ Proof
> $E=E(s_1f_1,\dots,s_nf_n)=S(B)$ for $S(\sum a_kf_k)=\sum a_ks_kf_k$ (check with the definition). So $T(E)=(TS)(B)$, an ellipsoid by [[§28 Consequences of Singular Value Decomposition#^ladr-7-99|7.99]].

*Uses:* [[§28 Consequences of Singular Value Decomposition#^ladr-7-99|7.99]]

> [!definition] Definition 7.102: P(v1, ..., vn), parallelepiped
> For a basis $v_1,\dots,v_n$, $P(v_1,\dots,v_n)=\{a_1v_1+\dots+a_nv_n:a_k\in(0,1)\}$. A *parallelepiped* is a translate $u+P(v_1,\dots,v_n)$, with *edges* $v_1,\dots,v_n$.

^ladr-7-102

> [!example] Example 7.103: Parallelepipeds (p. 289)
> $(0.3,0.5)+P\big((1,0),(1,1)\big)$ is a parallelogram in $\R^2$ with corner $(0.3,0.5)$ and edges $(1,0)$, $(1,1)$ (open: the boundary is excluded since $a_k\in(0,1)$).

^ladr-7-103

> [!theorem] Theorem 7.104: Invertible operator takes parallelepipeds to parallelepipeds
> If $T$ is invertible, $T\big(u+P(v_1,\dots,v_n)\big)=Tu+P(Tv_1,\dots,Tv_n)$.

^ladr-7-104

> [!proof]+ Proof
> $Tv_1,\dots,Tv_n$ is a basis, and $T(u+\sum a_kv_k)=Tu+\sum a_kTv_k$.

> [!definition] Definition 7.105: Box
> A *box* is $u+P(r_1e_1,\dots,r_ne_n)$ with $e_1,\dots,e_n$ orthonormal and $r_k>0$: a parallelepiped with orthogonal edges.

^ladr-7-105

> [!example] Example 7.106: Boxes (p. 290)
> - $(1,0)+P(\sqrt2e_1,\sqrt2e_2)$ with $e_1=\tfrac1{\sqrt2}(1,1)$, $e_2=\tfrac1{\sqrt2}(-1,1)$: a square of side $\sqrt2$ tilted by $45^\circ$, area $2$.
> - $P(e_1,2e_2,e_3)$ in $\R^3$: a $1\times2\times1$ box, volume $2$.

^ladr-7-106

> [!theorem] Theorem 7.107: Every invertible operator takes some boxes to boxes
> Let $T$ be invertible with SVD $Tv=\sum s_k\langle v,e_k\rangle f_k$ ($e$'s, $f$'s orthonormal bases). Then $T$ maps the box $u+P(r_1e_1,\dots,r_ne_n)$ onto the box $Tu+P(r_1s_1f_1,\dots,r_ns_nf_n)$.

^ladr-7-107

> [!proof]+ Proof
> $T(u+\sum a_kr_ke_k)=Tu+\sum a_kr_ks_kf_k$, since $Te_k=s_kf_k$.

> [!remark] Remark: Point
> A generic box goes to a slanted parallelepiped; boxes aligned with the right singular vectors go to boxes. This is what makes volume computable ([[§28 Consequences of Singular Value Decomposition#^ladr-7-111|7.111]]).

%% ex:7.107-fig %%
> [!example] Example: Boxes aligned with the singular vectors, pictured
> Same $T$ as in the SVD figure after [[Singular value decomposition|7.70]] ($s_1=2$, $s_2=0.8$). The blue box $P(e_1,e_2)$ goes to the box $P(s_1f_1,s_2f_2)$, again with a right angle. The orange unit square, not aligned with $e_1,e_2$, goes to a slanted parallelogram. Both areas are multiplied by $s_1s_2=1.6$ ([[§28 Consequences of Singular Value Decomposition#^ladr-7-111|7.111]]).
>
> ![[ladr-7.107-boxes.svg|440]]

> [!definition] Definition 7.108: Volume of a box
> ($\F=\R$) $\operatorname{volume}\big(u+P(r_1e_1,\dots,r_ne_n)\big)=r_1\cdots r_n$.

^ladr-7-108

> [!definition] Definition 7.109: Volume
> ($\F=\R$, informal) The volume of $\Omega\subseteq V$ is approximately the sum of the volumes of disjoint boxes approximating $\Omega$ (made rigorous by measure theory).

^ladr-7-109

> [!remark]- Connections
> - Riemann sums in [[Single Variable Analysis]] ([[§32 The Definition of the Riemann Integral#^def-32-7|451 Def. §32.7]]) are the one-dimensional version; Lebesgue measure makes this precise.
> - Rigorous treatment: approximating a plane region from inside and outside by grids of squares gives its Jordan content, [[§20 Multivariable Integration#^def-20-5|452 Def. §20.5]], [[§20 Multivariable Integration#^def-20-6|452 Def. §20.6]]; Lebesgue outer measure on ℝⁿ takes the infimum over countable coverings by boxes, [[§10 Lebesgue Outer Measure#^def-10-4|551 Def. §10.4]], and Lebesgue measure is its restriction to measurable sets, [[§11 Lebesgue Measurable Sets#^def-11-5|551 Def. §11.5]].

> [!example] Example 7.110: Volume change by a linear map (p. 292)
> $Tv=2\langle v,e_1\rangle e_1+\langle v,e_2\rangle e_2$ on $\R^2$ stretches by $2$ along $e_1$. Boxes aligned with $e_1,e_2$ go to boxes of twice the width, so every approximating box doubles in area, and so does the ball: $T(B)$ has area $2\pi$. The general statement is [[§28 Consequences of Singular Value Decomposition#^ladr-7-111|7.111]].

^ladr-7-110

> [!theorem] Theorem 7.111: Volume changes by a factor of the product of the singular values
> ($\F=\R$) If $T\in\Lin(V)$ is invertible and $\Omega\subseteq V$, then
> $$
> \operatorname{volume}T(\Omega)=(s_1\cdots s_n)\operatorname{volume}\Omega .
> $$

^ladr-7-111

> [!proof]+ Proof
> Approximate $\Omega$ by boxes aligned with the $e_k$ of an SVD. Each $u+P(r_1e_1,\dots,r_ne_n)$ goes to the box $Tu+P(r_1s_1f_1,\dots,r_ns_nf_n)$ ([[§28 Consequences of Singular Value Decomposition#^ladr-7-107|7.107]]) of volume $s_1\cdots s_n\,r_1\cdots r_n$, and the image boxes approximate $T(\Omega)$.

*Uses:* [[§28 Consequences of Singular Value Decomposition#^ladr-7-107|7.107]]

> [!remark]- Connections
> - $s_1\cdots s_n=|\det T|$ ([[§37 Determinants#^ladr-9-60|∣det T∣ = product of singular values of T]]): the Jacobian factor in the change-of-variables formula, [[Change of Variables Formula (multiple integrals)|452 Thm. §25.3]]. The linear case, volume scales by $|\det T|$, is proved for Jordan measurable sets in [[§25 Change of Variables on General Domains#^prop-25-5|452 Prop. §25.5]].

