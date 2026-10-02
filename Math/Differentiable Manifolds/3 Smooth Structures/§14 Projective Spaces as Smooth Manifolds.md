---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 3
section: 14
tags: [differentiable-manifolds, math591]
---
← [[§13 Differentiable Structures]] · ↑ [[· 3 Smooth Structures]] · [[§15 Smooth Functions and Smooth Maps]] →

*Stage: foundations — The quotient-built manifolds get their smooth structures from atlases written down by hand: $\mathbb{CP}^n$, with holomorphic transition functions.*

*Assignment 2, Problem 2(b)–(c). This completes the construction begun in [[§6 Open Quotients and Complex Projective Space#Application: Complex Projective Space|§6, Application: Complex Projective Space]]: there $\mathbb{CP}^n$ was shown to be compact, Hausdorff and second countable; here it acquires charts, and the charts turn out to be smoothly — indeed holomorphically — compatible.*

> [!definition] Definition §14.1: Homogeneous Coordinates
> For $\vec z = (z_0, \ldots, z_n) \in \mathbb{C}^{n+1} \setminus \{0\}$, write $[z_0 : z_1 : \cdots : z_n] \in \mathbb{CP}^n$ for the complex line through $\vec z$ ([[§6 Open Quotients and Complex Projective Space#^prop-6-6|§6.6]]). The $z_i$ are **homogeneous coordinates** of that point; they are determined only up to a common nonzero factor, $[\vec z] = [\lambda\vec z]$ for every $\lambda \in \mathbb{C}^\times$.
>
> *Lee: Problem 1-9*

^def-14-1

Let $\pi : \mathbb{C}^{n+1} \setminus \{0\} \to \mathbb{CP}^n$ be the projection $\vec z \mapsto [\vec z]$ of [[§6 Open Quotients and Complex Projective Space#^prop-6-6|§6.6]]. Throughout, $\mathbb{C}^m \cong \mathbb{R}^{2m}$ by [[§8 Topological Groups and Classical Matrix Groups#^def-8-8|Def. §8.8]].

> [!definition] Definition §14.2: The Standard Charts on $\mathbb{CP}^n$
> For $i \in \{0, 1, \ldots, n\}$ let
>
> $$
> U_i = \{\, [\vec z] \in \mathbb{CP}^n \mid z_i \neq 0 \,\},
> \qquad
> \varphi_i : U_i \to \mathbb{C}^n, \quad \varphi_i\big([z_0 : \cdots : z_n]\big) = \Big( \frac{z_k}{z_i} \Big)_{k \neq i}.
> $$
>
> It is convenient to index the $n$ entries of a point of the target by $\{0,\ldots,n\} \setminus \{i\}$ rather than by $\{1,\ldots,n\}$; this only relabels the slots. Equivalently $U_i = \{\ell \mid \ell \cap \{z_i = 0\} = \{0\}\}$: the lines not lying in the $i$-th coordinate hyperplane.
>
> *Lee: Problem 1-9*

^def-14-2

> [!theorem] Proposition §14.1: Each $\varphi_i$ Is a Chart
> $U_i$ is open in $\mathbb{CP}^n$, and $\varphi_i$ is a well-defined homeomorphism of $U_i$ onto $\mathbb{C}^n \cong \mathbb{R}^{2n}$, with inverse
>
> $$
> \varphi_i^{-1}(\vec w) = [\, w_0 : \cdots : w_{i-1} : 1 : w_{i+1} : \cdots : w_n \,] \qquad \text{($1$ in slot $i$).}
> $$
>
> *Lee: Problem 1-9*

^prop-14-1

![[m591-8-4.svg]]
*Here $p = \pi|_{\pi^{-1}(U_i)}$, the map $\tilde\varphi_i(\vec z) = (z_k/z_i)_{k\neq i}$ divides by the $i$-th coordinate, and $s_i$ inserts a $1$ in slot $i$. The pattern of [[§6 Open Quotients and Complex Projective Space#^prop-6-6|§6.6]] recurs: upstairs $\tilde\varphi_i \circ s_i = \mathrm{id}$ but $s_i \circ \tilde\varphi_i$ rescales $\vec z$ to $\vec z/z_i$; downstairs $\varphi_i$ and $\psi_i = p \circ s_i$ are mutually inverse. The triangle $\varphi_i \circ p = \tilde\varphi_i$ is where the universal property is applied — to $p$, not to $\pi$, which is the job of [[§5 Quotient Maps#^lem-5-7|§5.7]].*

> [!proof]+ Proof
> *$U_i$ is well defined and open.* Every nonzero vector on a line $\ell$ is a scalar multiple $\lambda\vec z$, $\lambda \neq 0$, of any one of them, and $(\lambda\vec z)_i = \lambda z_i$; so “$z_i \neq 0$” holds for one representative iff for all. Hence
>
> $$
> \pi^{-1}(U_i) = \{\, \vec z \in \mathbb{C}^{n+1}\setminus\{0\} \mid z_i \neq 0 \,\},
> $$
>
> whose complement in $\mathbb{C}^{n+1}\setminus\{0\}$ is $H_i \setminus \{0\}$ with $H_i = \{z_i = 0\}$ a linear subspace, hence closed. So $\pi^{-1}(U_i)$ is open and, by the definition of the quotient topology, $U_i$ is open.
>
> *$\varphi_i$ is well defined.* For $\lambda \in \mathbb{C}^\times$ and $k \neq i$, $(\lambda z_k)/(\lambda z_i) = z_k/z_i$.
>
> *Bijectivity.* Let $s_i : \mathbb{C}^n \to \mathbb{C}^{n+1}\setminus\{0\}$ insert $1$ in slot $i$, and $\psi_i = \pi \circ s_i$. Then $\varphi_i(\psi_i(\vec w)) = \vec w$, since the representative $s_i(\vec w)$ has $i$-th entry $1$. Conversely, for $\ell = [\vec z] \in U_i$ the vector $\vec z/z_i$ represents $\ell$, has $i$-th entry $1$, and has remaining entries $\varphi_i(\ell)$; so $\psi_i(\varphi_i(\ell)) = \ell$. Thus $\psi_i = \varphi_i^{-1}$.
>
> *$\varphi_i$ is continuous.* By [[§5 Quotient Maps#^lem-5-7|§5.7]], since $\pi$ is a quotient map and $U_i$ is open, the restriction $p = \pi|_{\pi^{-1}(U_i)} : \pi^{-1}(U_i) \to U_i$ is a quotient map. The map $\tilde\varphi_i(\vec z) = (z_k/z_i)_{k\neq i}$ on $\pi^{-1}(U_i)$ is continuous (each component is a quotient of continuous functions with nonvanishing denominator) and constant on the fibres of $p$ by well-definedness. By the universal property ([[§5 Quotient Maps#^thm-5-1|§5.1]]) it descends to a continuous map on $U_i$, which is $\varphi_i$.
>
> *$\varphi_i^{-1}$ is continuous.* $\psi_i = \pi \circ s_i$, and $s_i$ is continuous (its components are coordinates or the constant $1$).

^pf-14-1

*Uses:* [[§14 Projective Spaces as Smooth Manifolds#^def-14-1|Def. §14.1]], [[§14 Projective Spaces as Smooth Manifolds#^def-14-2|Def. §14.2]], [[§4 Quotient Spaces and Open Maps#^def-4-1|Def. §4.1]], [[§6 Open Quotients and Complex Projective Space#^prop-6-6|§6.6]], [[§5 Quotient Maps#^lem-5-7|§5.7]], [[§5 Quotient Maps#^thm-5-1|§5.1]], [[Universal Property of Quotient Maps|590 §12.3]], [[§10 Product Topology on Arbitrary Products#^thm-10-1|590 §10.1]]

> [!remark]- Connections
> - $\mathbb{CP}^n$ as the orbit space of $\mathbb{C}^\times$: [[§10 Group Actions and Orbit Spaces#^ex-10-3|Ex. §10.3]]; the home of quotient maps and their universal property: [[§12 Quotient Topology|590 §12]].

> [!remark] Remark
> This is where [[§5 Quotient Maps#^lem-5-7|§5.7]] earns its place. The map $\tilde\varphi_i$ is defined only on the open piece $\pi^{-1}(U_i)$ — it divides by $z_i$ — so the universal property cannot be applied to $\pi$ itself; it is applied to $\pi$ restricted over $U_i$, which the lemma guarantees is still a quotient map. Every chart on a quotient space is built by this two-step move.

^rem-14-1

> [!theorem] Theorem §14.2: The Standard Atlas Is Smooth
> $\{(U_i, \varphi_i)\}_{i=0}^n$ is a $C^\infty$ atlas on $\mathbb{CP}^n$. For $i \neq j$,
>
> $$
> \varphi_j(U_i \cap U_j) = \{\, \vec w \in \mathbb{C}^n \mid w_i \neq 0 \,\},
> \qquad
> \big(\varphi_i \circ \varphi_j^{-1}\big)(\vec w) = \Big( \frac{w_k}{w_i} \Big)_{k \neq i},
> $$
>
> with the convention $w_j := 1$.
> Consequently $\mathbb{CP}^n$ is a compact smooth manifold of (real) dimension $2n$.
>
> *Lee: Problem 1-9*

^thm-14-2

![[m591-8-5.svg]]
*The compatibility triangle of [[§13 Differentiable Structures#Compatibility of Charts|Compatibility of Charts]] for two standard charts. The overlap lives upstairs in $\mathbb{CP}^n$; its two images downstairs are open subsets of $\mathbb{C}^n$, each cut out by one nonvanishing coordinate, and the bottom arrow is the transition function computed below.*

> [!proof]+ Proof
> *Cover.* If $\vec z \neq 0$ some $z_i \neq 0$, so $[\vec z] \in U_i$.
>
> *Domains.* By [[§14 Projective Spaces as Smooth Manifolds#^prop-14-1|§14.1]], $\varphi_j^{-1}(\vec w)$ is represented by $s_j(\vec w)$, whose $j$-th entry is $1$ and whose $k$-th entry is $w_k$ for $k \neq j$. It lies in $U_i$ iff its $i$-th entry is nonzero, i.e. (as $i \neq j$) iff $w_i \neq 0$. This set is open, being the preimage of $\mathbb{C}\setminus\{0\}$ under the continuous coordinate $\vec w \mapsto w_i$.
>
> *Transition functions.* Applying $\varphi_i$ to the representative $s_j(\vec w)$ divides every entry by its $i$-th entry $w_i$ and deletes slot $i$, giving the displayed formula; in particular the entry in slot $j$ is $1/w_i$. Each entry $w_k/w_i$ is a quotient of polynomials with denominator nonvanishing on the domain. In real coordinates, writing $w_k = a_k + \mathrm{i}\,b_k$ (with $\mathrm{i}$ the imaginary unit, to distinguish it from the index $i$),
>
> $$
> \frac{w_k}{w_i} = \frac{w_k\,\overline{w_i}}{|w_i|^2} = \frac{a_k a_i + b_k b_i}{a_i^2 + b_i^2} + \mathrm{i}\,\frac{b_k a_i - a_k b_i}{a_i^2 + b_i^2},
> $$
>
> so both real components are rational functions with nonvanishing denominator $|w_i|^2$, hence $C^\infty$. Exchanging $i$ and $j$ gives the inverse transition, also $C^\infty$; so any two charts are compatible.
>
> *Conclusion.* The $U_i$ are open and cover, the $\varphi_i$ are homeomorphisms onto the open set $\mathbb{C}^n \cong \mathbb{R}^{2n}$, and all transitions are diffeomorphisms: this is a smooth atlas, determining a smooth structure by [[§13 Differentiable Structures#^thm-13-5|§13.5]]. Hausdorffness, second countability and compactness are [[§6 Open Quotients and Complex Projective Space#^prop-6-4|§6.4]] and [[§6 Open Quotients and Complex Projective Space#^prop-6-5|§6.5]].

^pf-14-2

*Uses:* [[§14 Projective Spaces as Smooth Manifolds#^prop-14-1|§14.1]], [[§13 Differentiable Structures#^def-13-4|Def. §13.4]], [[§13 Differentiable Structures#^def-13-6|Def. §13.6]], [[§13 Differentiable Structures#^thm-13-5|§13.5]], [[§6 Open Quotients and Complex Projective Space#^prop-6-4|§6.4]], [[§6 Open Quotients and Complex Projective Space#^prop-6-5|§6.5]], [[§8 Topological Groups and Classical Matrix Groups#^def-8-8|Def. §8.8]], [[§6 Differentiability#^thm-6-8|452 §6.8]]

> [!theorem] Corollary §14.3: $\mathbb{CP}^n$ Is a Complex Manifold
> The transition functions of the standard atlas are holomorphic. Hence $\mathbb{CP}^n$ is a complex manifold of complex dimension $n$, in the sense of [[§13 Differentiable Structures#^def-13-5|Def. §13.5]].

^cor-14-3

> [!proof]+ Proof
> *(Not from lecture; filled in.)* Each component $\vec w \mapsto w_k/w_i$ of a transition function ([[§14 Projective Spaces as Smooth Manifolds#^thm-14-2|§14.2]]) is a quotient of complex polynomials with denominator nonvanishing on the domain, hence holomorphic.

^pf-14-3

*Uses:* [[§14 Projective Spaces as Smooth Manifolds#^thm-14-2|§14.2]], [[§13 Differentiable Structures#^def-13-5|Def. §13.5]]

> [!theorem] Proposition §14.4: $\mathbb{CP}^1$ Is the Riemann Sphere
> $\mathbb{CP}^1$ is homeomorphic to $S^2$.
>
> *Lee: Problem 4-5(b)*

^prop-14-4

> [!proof]+ Proof
> *(Not from lecture; filled in.)* For $(x,y,z) \in S^2$ the identity $(x+iy)(x-iy) = x^2 + y^2 = (1-z)(1+z)$ shows that $[x+iy : 1-z]$, defined when $z \ne 1$, and $[1+z : x-iy]$, defined when $z \ne -1$, are the same point of $\mathbb{CP}^1$ wherever both are defined. So there is a well-defined map $\Phi : S^2 \to \mathbb{CP}^1$, continuous on each of the two open sets $\{z \ne 1\}$ and $\{z \ne -1\}$ covering $S^2$, hence continuous. On $S^2 \setminus \{N\}$ it is $p \mapsto [\sigma(p) : 1]$, where $\sigma(x,y,z) = (x+iy)/(1-z)$ is the stereographic projection. This is a bijection onto $\mathbb{C}$, with inverse $w \mapsto \big(2\operatorname{Re} w,\, 2\operatorname{Im} w,\, |w|^2 - 1\big)/(|w|^2+1)$. So $\Phi$ maps $S^2 \setminus \{N\}$ bijectively onto $U_1 = \{[w : 1]\}$, and $\Phi(N) = [2 : 0] = [1:0]$ is the one point outside $U_1$. Thus $\Phi$ is a continuous bijection from the compact $S^2$ onto the Hausdorff $\mathbb{CP}^1$ ([[§6 Open Quotients and Complex Projective Space#^prop-6-4|§6.4]]), hence a homeomorphism.

^pf-14-4

*Uses:* [[§14 Projective Spaces as Smooth Manifolds#^def-14-1|Def. §14.1]], [[§14 Projective Spaces as Smooth Manifolds#^def-14-2|Def. §14.2]], [[§6 Open Quotients and Complex Projective Space#^prop-6-4|§6.4]], [[§1 Point-Set Topology Review#^prop-1-8|§1.8]], [[§9 Continuous Functions#^thm-9-4|590 §9.4 (local formulation of continuity)]], [[Heine–Borel Theorem|590 §15.12 (Heine–Borel)]], [[Bijection from Compact to Hausdorff is a Homeomorphism|590 §15.7]]

> [!remark] Remark
> For $n = 1$ there are two standard charts and a single transition function, $w \mapsto 1/w$ on $\mathbb{C} \setminus \{0\}$ — the complex counterpart of the stereographic transition $u \mapsto 1/u$ of [[§13 Differentiable Structures#^ex-13-3|Ex. §13.3]].

^rem-14-2

> [!remark]- Connections
> - S² as the one-point compactification of ℝ² ≅ ℂ, by the same stereographic projection: [[§17 Local Compactness#^ex-17-7|590 Ex. §17.7]].

> [!theorem] Corollary §14.5: Real Projective Space
> Let $\mathbb{RP}^n = S^n/\{\pm 1\} \cong (\mathbb{R}^{n+1}\setminus\{0\})/\mathbb{R}^\times$, the space of real lines through the origin in $\mathbb{R}^{n+1}$. With $U_i = \{[\vec x] \mid x_i \neq 0\}$ and $\varphi_i([\vec x]) = (x_k/x_i)_{k \neq i}$, the family $\{(U_i, \varphi_i)\}_{i=0}^n$ is a smooth atlas, and $\mathbb{RP}^n$ is a compact smooth manifold of dimension $n$.
>
> *Lee: Example 1.33*

^cor-14-5

> [!proof]+ Proof
> *(Not from lecture; filled in.)* Every argument of [[§6 Open Quotients and Complex Projective Space#Application: Complex Projective Space|§6, Application: Complex Projective Space]] and of this section goes through verbatim with $\mathbb{R}$, $\mathbb{R}^\times$, $\{\pm1\}$ and $S^n$ in place of $\mathbb{C}$, $\mathbb{C}^\times$, $S^1$ and $S^{2n+1}$: the group $\{\pm 1\}$ is finite, hence compact, and acts on $S^n$ by isometries; the transition maps are the real rational functions $x_k/x_i$. Hausdorffness can alternatively be read off from [[§10 Group Actions and Orbit Spaces#^cor-10-4|§10.4]].

^pf-14-5

*Uses:* [[§6 Open Quotients and Complex Projective Space#^prop-6-4|§6.4]], [[§6 Open Quotients and Complex Projective Space#^prop-6-5|§6.5]], [[§6 Open Quotients and Complex Projective Space#^prop-6-6|§6.6]], [[§14 Projective Spaces as Smooth Manifolds#^prop-14-1|§14.1]], [[§14 Projective Spaces as Smooth Manifolds#^thm-14-2|§14.2]], [[§10 Group Actions and Orbit Spaces#^cor-10-4|§10.4]]

> [!remark]- Connections
> - The same space in 590, projective $n$-space: [[§28 Fundamental Group of Some Surfaces#^def-28-2|590 Def. §28.2]], [[Projective plane]]; the double cover $S^n \to \mathbb{RP}^n$ as a local diffeomorphism: [[§28 Local Diffeomorphisms and Submersions#^ex-28-2|Ex. §28.2]].

![[m591-8-6.svg]]
*The chart $U_0$ of $\mathbb{RP}^1$, drawn in the plane of homogeneous coordinates. A point of $\mathbb{RP}^1$ is a line through the origin. A line $L$ with $x_0 \ne 0$ meets the affine line $x_0 = 1$ in exactly one point, $(1, x_1/x_0)$, and the chart $\varphi_0(L) = x_1/x_0$ records where. The one line with $x_0 = 0$ — the $x_1$-axis, the point $[0:1]$ — is parallel to $x_0 = 1$ and never meets it: it is the point at infinity that $U_0$ misses, and the second chart $U_1$ covers it. On the right, $\mathbb{RP}^1$ drawn as a circle, with $U_0$ everything except the top point. In $\mathbb{RP}^n$ the same picture holds with the affine hyperplane $x_0 = 1$ in place of the line.*

> [!theorem] Proposition §14.6: The Two Topologies on $\mathbb{RP}^n$ Agree
> 1. Under $[\vec x] \mapsto \mathbb{R}\vec x$, the quotient topology on $\mathbb{RP}^n = S^n/\{\pm1\}$ agrees with the topology of $\mathrm{Gr}_1(\mathbb{R}^{n+1})$ transported from the coset space $\mathrm{O}(n+1)/(\mathrm{O}(1)\times\mathrm{O}(n))$ in [[§11 Homogeneous Spaces|§11]].
> 2. $\mathbb{RP}^1$ is homeomorphic to $S^1$.
>
> *Lee: Examples 1.5 and 1.33*

^prop-14-6

> [!proof]+ Proof
> *(Not from lecture; filled in.)* (1) $\mathrm{O}(n+1)$ acts on $S^n/\{\pm1\}$ by $g \cdot [\vec x] = [g\vec x]$, continuously: the map $\mathrm{id} \times \pi : \mathrm{O}(n+1) \times S^n \to \mathrm{O}(n+1) \times S^n/\{\pm1\}$ is an open continuous surjection, hence a quotient map, and the action descends along it by the universal property. The action is transitive, the coset space is compact, and $S^n/\{\pm1\}$ is Hausdorff, so [[§12 The Topology of G∕H and Real Grassmannians#^thm-12-3|§12.3]] identifies $S^n/\{\pm1\}$ homeomorphically with the coset space — which is precisely the transported topology.
>
> (2) Let $\sigma_N, \sigma_S$ be the stereographic charts of [[§13 Differentiable Structures#^ex-13-3|Ex. §13.3]], and $\varphi_0, \varphi_1$ the standard charts of $\mathbb{RP}^1$. Define $F = \sigma_N^{-1} \circ \varphi_0$ on $U_0$ and $F = \sigma_S^{-1} \circ \varphi_1$ on $U_1$. On $U_0 \cap U_1$ we have $\varphi_1 = 1/\varphi_0$, and $\sigma_S \circ \sigma_N^{-1}(u) = 1/u$ gives $\sigma_N^{-1}(u) = \sigma_S^{-1}(1/u)$; so the two formulas agree and $F$ is well defined and continuous. It maps $U_0$ bijectively onto $S^1 \setminus \{N\}$, and the one point $[0:1]$ outside $U_0$ to $\sigma_S^{-1}(0) = N$. So $F$ is a continuous bijection from the compact $\mathbb{RP}^1$ onto the Hausdorff $S^1$, hence a homeomorphism. Both transition functions are $u \mapsto 1/u$, and in the charts used $F$ has coordinate representation the identity; so it is even a diffeomorphism, in the sense of [[§15 Smooth Functions and Smooth Maps#^def-15-3|Def. §15.3]] below.

^pf-14-6

*Uses:* [[§5 Quotient Maps#^prop-5-5|§5.5]], [[§5 Quotient Maps#^thm-5-1|§5.1]], [[§12 The Topology of G∕H and Real Grassmannians#^thm-12-3|§12.3]], [[§12 The Topology of G∕H and Real Grassmannians#^def-12-2|Def. §12.2]], [[§12 The Topology of G∕H and Real Grassmannians#^cor-12-8|§12.8]], [[§13 Differentiable Structures#^ex-13-3|Ex. §13.3]], [[§14 Projective Spaces as Smooth Manifolds#^cor-14-5|§14.5]], [[§15 Smooth Functions and Smooth Maps#^def-15-3|Def. §15.3]], [[§9 Continuous Functions#^thm-9-4|590 §9.4 (local formulation of continuity)]], [[Bijection from Compact to Hausdorff is a Homeomorphism|590 §15.7]]

> [!remark]- Connections
> - $P^1 \cong S^1$ in 590: [[§28 Fundamental Group of Some Surfaces#^thm-28-3|590 §28.3]]; Grassmannians as homogeneous spaces: [[§12 The Topology of G∕H and Real Grassmannians#^cor-12-8|§12.8]].

![[m591-8-7.svg]]
*The quotient $S^n \to \mathbb{RP}^n$ of [[§14 Projective Spaces as Smooth Manifolds#^prop-14-6|§14.6]], drawn for $n = 2$. A line through the origin meets the sphere in two antipodal points $p$ and $-p$, which $\pi$ identifies. Every line meets the closed upper hemisphere: once if it is not horizontal, and in a pair of antipodal points $q$, $-q$ of the equator if it is. So $\mathbb{RP}^2$ can be pictured as a closed disc with antipodal boundary points glued, as the arrows indicate. For $n = 1$ the same gluing closes a half-circle into a circle, which is $\mathbb{RP}^1 \cong S^1$.*
