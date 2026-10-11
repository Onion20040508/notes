---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 3
section: 18
tags: [differentiable-manifolds, math591]
---
← [[§17 Differentiable Structures]] · ↑ [[· 3 Smooth Structures]] · [[§19 Smooth Functions and Smooth Maps]] →

*Stage: foundations — The quotient-built manifolds get their smooth structures from atlases written down by hand: $\mathbb{CP}^n$, with holomorphic transition functions.*

The projections $S^n \to \mathbb{RP}^n$ and $S^{2n+1} \to \mathbb{CP}^n$ through the course: the second is the quotient map that defines $\mathbb{CP}^n$ in [[§9 Complex Projective Space|Complex Projective Space]], an orbit map in [[§13 Group Actions and Orbit Spaces#^ex-13-3|projective space as an orbit space]]; the first is the quotient map of [[§18 Projective Spaces as Smooth Manifolds#^prop-18-6|The Two Topologies on RPⁿ Agree]], and both are read in the standard atlases of [[§18 Projective Spaces as Smooth Manifolds|Projective Spaces as Smooth Manifolds]]; [[§40 Projective Spaces and the Hopf Fibration|Projective Spaces and the Hopf Fibration]] shows the first is a two-to-one local diffeomorphism and the second a submersion and a fibration, the Hopf fibration, with local but no global sections; and for $n = 3$ the first returns as $S^3 = \mathrm{SU}(2) \to \mathrm{SO}(3) \cong \mathbb{RP}^3$ in [[§42 SU(2) → SO(3)꞉ The Double Cover#^thm-42-4|The Double Cover]].

*Assignment 2, Problem 2(b)–(c). This completes the construction begun in [[§9 Complex Projective Space|§9]]: there $\mathbb{CP}^n$ was shown to be compact, Hausdorff and second countable; here it acquires charts, and the charts turn out to be smoothly — indeed holomorphically — compatible.*

> [!definition] Definition §18.1: Homogeneous Coordinates
> For $\vec z = (z_0, \ldots, z_n) \in \mathbb{C}^{n+1} \setminus \{0\}$, write $[z_0 : z_1 : \cdots : z_n] \in \mathbb{CP}^n$ for the complex line through $\vec z$ ([[§9 Complex Projective Space#^prop-9-3|§9.3]]). The $z_i$ are **homogeneous coordinates** of that point; they are determined only up to a common nonzero factor, $[\vec z] = [\lambda\vec z]$ for every $\lambda \in \mathbb{C}^\times$.
>
> *Lee: Problem 1-9*

^def-18-1

Let $\pi : \mathbb{C}^{n+1} \setminus \{0\} \to \mathbb{CP}^n$ be the projection $\vec z \mapsto [\vec z]$ of [[§9 Complex Projective Space#^prop-9-3|§9.3]]. Throughout, $\mathbb{C}^m \cong \mathbb{R}^{2m}$ by [[§11 Topological Groups and Classical Matrix Groups#^def-11-9|Def. §11.9]].

> [!definition] Definition §18.2: The Standard Charts on $\mathbb{CP}^n$
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

^def-18-2

> [!theorem] Proposition §18.1: Each $\varphi_i$ Is a Chart
> $U_i$ is open in $\mathbb{CP}^n$, and $\varphi_i$ is a well-defined homeomorphism of $U_i$ onto $\mathbb{C}^n \cong \mathbb{R}^{2n}$, with inverse
>
> $$
> \varphi_i^{-1}(\vec w) = [\, w_0 : \cdots : w_{i-1} : 1 : w_{i+1} : \cdots : w_n \,] \qquad \text{($1$ in slot $i$).}
> $$
>
> *Lee: Problem 1-9*

^prop-18-1

![[m591-8-4.svg]]
*Here $p = \pi|_{\pi^{-1}(U_i)}$, the map $\tilde\varphi_i(\vec z) = (z_k/z_i)_{k\neq i}$ divides by the $i$-th coordinate, and $s_i$ inserts a $1$ in slot $i$. The pattern of [[§9 Complex Projective Space#^prop-9-3|§9.3]] recurs: upstairs $\tilde\varphi_i \circ s_i = \mathrm{id}$ but $s_i \circ \tilde\varphi_i$ rescales $\vec z$ to $\vec z/z_i$; downstairs $\varphi_i$ and $\psi_i = p \circ s_i$ are mutually inverse. The triangle $\varphi_i \circ p = \tilde\varphi_i$ is where the universal property is applied — to $p$, not to $\pi$, which is the job of [[§5 Quotient Maps#^lem-5-7|§5.7]].*

> [!proof]+ Proof
> *$U_i$ is well defined and open.* Every nonzero vector on a line $\ell$ is a scalar multiple $\lambda\vec z$, $\lambda \neq 0$, of any one of them, and $(\lambda\vec z)_i = \lambda z_i$, which is nonzero exactly when $z_i$ is (as $\lambda \neq 0$); so “$z_i \neq 0$” holds for one representative iff for all. Hence
>
> $$
> \pi^{-1}(U_i) = \{\, \vec z \in \mathbb{C}^{n+1}\setminus\{0\} \mid z_i \neq 0 \,\},
> $$
>
> whose complement in $\mathbb{C}^{n+1}\setminus\{0\}$ is $H_i \setminus \{0\}$ with $H_i = \{z_i = 0\}$ a linear subspace, hence closed. ($H_i$ is the preimage of the closed set $\{0\}$ under the continuous coordinate $\vec z \mapsto z_i$, and $H_i \setminus \{0\} = H_i \cap (\mathbb{C}^{n+1}\setminus\{0\})$ is then closed in the subspace $\mathbb{C}^{n+1}\setminus\{0\}$.) So $\pi^{-1}(U_i)$ is open and, by the definition of the quotient topology ($\pi$ is a quotient map, Definition [[§5 Quotient Maps#^def-5-1|§5.1]]: a set is open iff its preimage is), $U_i$ is open.
>
> *$\varphi_i$ is well defined.* The value $\varphi_i(\ell)$ must not depend on the representative. Two representatives of $\ell = [\vec z]$ differ by a factor $\lambda \in \mathbb{C}^\times$ (Definition [[§18 Projective Spaces as Smooth Manifolds#^def-18-1|§18.1]]), and for $k \neq i$, $(\lambda z_k)/(\lambda z_i) = z_k/z_i$. The quotients are defined because $z_i \neq 0$ on $U_i$.
>
> *Bijectivity.* Let $s_i : \mathbb{C}^n \to \mathbb{C}^{n+1}\setminus\{0\}$ insert $1$ in slot $i$, and $\psi_i = \pi \circ s_i$. The vector $s_i(\vec w)$ is nonzero with $i$-th entry $1 \neq 0$, so $\psi_i(\vec w) \in U_i$. Then $\varphi_i(\psi_i(\vec w)) = \vec w$, since the representative $s_i(\vec w)$ has $i$-th entry $1$:
>
> $$
> \varphi_i\big([s_i(\vec w)]\big) = \Big( \frac{s_i(\vec w)_k}{1} \Big)_{k \neq i} = (w_k)_{k \neq i} = \vec w .
> $$
>
> Conversely, for $\ell = [\vec z] \in U_i$ the vector $\vec z/z_i$ represents $\ell$ (take $\lambda = 1/z_i$), has $i$-th entry $z_i/z_i = 1$, and has remaining entries $z_k/z_i$, which are the entries of $\varphi_i(\ell)$; that is, $\vec z/z_i = s_i(\varphi_i(\ell))$, so
>
> $$
> \psi_i(\varphi_i(\ell)) = \big[s_i(\varphi_i(\ell))\big] = [\vec z/z_i] = [\vec z] = \ell .
> $$
>
> Thus $\varphi_i : U_i \to \mathbb{C}^n$ is a bijection and $\psi_i = \varphi_i^{-1}$, which is the displayed formula.
>
> *$\varphi_i$ is continuous.* By Lemma [[§5 Quotient Maps#^lem-5-7|§5.7]], since $\pi$ is a quotient map and $U_i$ is open, the restriction $p = \pi|_{\pi^{-1}(U_i)} : \pi^{-1}(U_i) \to U_i$ is a quotient map. The map $\tilde\varphi_i(\vec z) = (z_k/z_i)_{k\neq i}$ on $\pi^{-1}(U_i)$ is continuous (each component is a quotient of continuous functions with nonvanishing denominator) and constant on the fibres of $p$ by well-definedness: the fibre through $\vec z$ is $\{\lambda \vec z \mid \lambda \in \mathbb{C}^\times\}$ (Proposition [[§9 Complex Projective Space#^prop-9-3|§9.3]]), and $\tilde\varphi_i(\lambda\vec z) = \tilde\varphi_i(\vec z)$ by the computation above. By the universal property (Theorem [[§5 Quotient Maps#^thm-5-1|§5.1]]) it descends to a continuous map on $U_i$, which is $\varphi_i$. In detail: the theorem gives a unique $f : U_i \to \mathbb{C}^n$ with $f \circ p = \tilde\varphi_i$, continuous because $\tilde\varphi_i$ is (its part (1)); and $\varphi_i$ satisfies $\varphi_i \circ p = \tilde\varphi_i$, since $\varphi_i([\vec z]) = (z_k/z_i)_{k \neq i} = \tilde\varphi_i(\vec z)$ by Definition [[§18 Projective Spaces as Smooth Manifolds#^def-18-2|§18.2]]; by uniqueness $f = \varphi_i$.
>
> *$\varphi_i^{-1}$ is continuous.* $\psi_i = \pi \circ s_i$, and $s_i$ is continuous (its components are coordinates or the constant $1$), as is $\pi$. So $\psi_i$ is continuous into $\mathbb{CP}^n$, and since its values lie in $U_i$ it is continuous as a map into the subspace $U_i$ (Proposition [[§3 Subspaces and Products#^prop-3-3|§3.3]]). Hence $\varphi_i$ is a homeomorphism of $U_i$ onto $\mathbb{C}^n \cong \mathbb{R}^{2n}$.

^pf-18-1

*Uses:* [[§18 Projective Spaces as Smooth Manifolds#^def-18-1|Def. §18.1]], [[§18 Projective Spaces as Smooth Manifolds#^def-18-2|Def. §18.2]], [[§4 Quotient Spaces and Open Maps#^def-4-1|Def. §4.1]], [[§4 Quotient Spaces and Open Maps#^def-4-2|Def. §4.2]], [[§9 Complex Projective Space#^prop-9-3|§9.3]], [[§5 Quotient Maps#^lem-5-7|§5.7]], [[§5 Quotient Maps#^thm-5-1|§5.1]], [[Universal Property of Quotient Maps|590 §13.3]], [[§11 Product Topology on Arbitrary Products#^thm-11-1|590 §11.1]], [[§5 Quotient Maps#^def-5-1|Def. §5.1]], [[§3 Subspaces and Products#^prop-3-3|§3.3]]

> [!remark]- Connections
> - $\mathbb{CP}^n$ as the orbit space of $\mathbb{C}^\times$: [[§13 Group Actions and Orbit Spaces#^ex-13-3|Ex. §13.3]]; the home of quotient maps and their universal property: [[§13 Quotient Topology|590 §13]].

> [!remark] Remark
> This is where [[§5 Quotient Maps#^lem-5-7|§5.7]] earns its place. The map $\tilde\varphi_i$ is defined only on the open piece $\pi^{-1}(U_i)$ — it divides by $z_i$ — so the universal property cannot be applied to $\pi$ itself; it is applied to $\pi$ restricted over $U_i$, which the lemma guarantees is still a quotient map. Every chart on a quotient space is built by this two-step move.

^rem-18-1

> [!theorem] Theorem §18.2: The Standard Atlas Is Smooth
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

^thm-18-2

![[m591-8-5.svg]]
*The compatibility triangle of [[§17 Differentiable Structures#Compatibility of Charts|Compatibility of Charts]] for two standard charts. The overlap lives upstairs in $\mathbb{CP}^n$; its two images downstairs are open subsets of $\mathbb{C}^n$, each cut out by one nonvanishing coordinate, and the bottom arrow is the transition function computed below.*

> [!proof]+ Proof
> *Cover.* Every point of $\mathbb{CP}^n$ is $[\vec z]$ for some $\vec z \neq 0$ (Definition [[§18 Projective Spaces as Smooth Manifolds#^def-18-1|§18.1]]). If $\vec z \neq 0$ some $z_i \neq 0$, so $[\vec z] \in U_i$. Hence $\bigcup_i U_i = \mathbb{CP}^n$.
>
> *Domains.* Fix $i \neq j$. Since $\varphi_j : U_j \to \mathbb{C}^n$ is a bijection (Proposition [[§18 Projective Spaces as Smooth Manifolds#^prop-18-1|§18.1]]), $\vec w \in \varphi_j(U_i \cap U_j)$ iff $\varphi_j^{-1}(\vec w) \in U_i$. By Proposition [[§18 Projective Spaces as Smooth Manifolds#^prop-18-1|§18.1]], $\varphi_j^{-1}(\vec w)$ is represented by $s_j(\vec w)$, whose $j$-th entry is $1$ and whose $k$-th entry is $w_k$ for $k \neq j$. It lies in $U_i$ iff its $i$-th entry is nonzero, i.e. (as $i \neq j$, that entry is $w_i$) iff $w_i \neq 0$. This set is open, being the preimage of $\mathbb{C}\setminus\{0\}$ under the continuous coordinate $\vec w \mapsto w_i$.
>
> *Transition functions.* Applying $\varphi_i$ to the representative $s_j(\vec w)$ divides every entry by its $i$-th entry $w_i$ and deletes slot $i$, giving the displayed formula; in particular the entry in slot $j$ is $1/w_i$. Explicitly, for $w_i \neq 0$, by Definition [[§18 Projective Spaces as Smooth Manifolds#^def-18-2|§18.2]],
>
> $$
> \big(\varphi_i \circ \varphi_j^{-1}\big)(\vec w) = \varphi_i\big([s_j(\vec w)]\big) = \Big( \frac{s_j(\vec w)_k}{s_j(\vec w)_i} \Big)_{k \neq i} = \Big( \frac{s_j(\vec w)_k}{w_i} \Big)_{k \neq i} = \Big( \frac{w_k}{w_i} \Big)_{k \neq i},
> $$
>
> where in the last step $s_j(\vec w)_k = w_k$ for $k \neq j$, and $s_j(\vec w)_j = 1 = w_j$ under the convention $w_j := 1$. Each entry $w_k/w_i$ is a quotient of polynomials with denominator nonvanishing on the domain. In real coordinates, writing $w_k = a_k + \mathrm{i}\,b_k$ (with $\mathrm{i}$ the imaginary unit, to distinguish it from the index $i$),
>
> $$
> \frac{w_k}{w_i} = \frac{w_k\,\overline{w_i}}{|w_i|^2} = \frac{a_k a_i + b_k b_i}{a_i^2 + b_i^2} + \mathrm{i}\,\frac{b_k a_i - a_k b_i}{a_i^2 + b_i^2},
> $$
>
> so both real components are rational functions with nonvanishing denominator $|w_i|^2$, hence $C^\infty$. (For the slot-$j$ entry $1/w_i$ take $a_k = 1$, $b_k = 0$.) A map into $\mathbb{C}^n \cong \mathbb{R}^{2n}$ is smooth iff each of its $2n$ real components is, so $\varphi_i \circ \varphi_j^{-1}$ is $C^\infty$. Exchanging $i$ and $j$ gives the inverse transition, also $C^\infty$: the same computation with the letters $i$ and $j$ swapped shows that $\varphi_j \circ \varphi_i^{-1} : \{w_j \neq 0\} \to \{w_i \neq 0\}$ is $\vec w \mapsto (w_k/w_j)_{k \neq j}$ with $w_i := 1$. So $\varphi_i \circ \varphi_j^{-1}$ is a bijection (Proposition [[§2 Topological Manifolds#^prop-2-11|§2.11]]) which is smooth with smooth inverse, a diffeomorphism (Definition [[§17 Differentiable Structures#^def-17-3|§17.3]]); for $i = j$ the transition is the identity. So any two charts are compatible (Definition [[§17 Differentiable Structures#^def-17-4|§17.4]]).
>
> *Conclusion.* The $U_i$ are open and cover, the $\varphi_i$ are homeomorphisms onto the open set $\mathbb{C}^n \cong \mathbb{R}^{2n}$, and all transitions are diffeomorphisms: this is a smooth atlas (Definition [[§17 Differentiable Structures#^def-17-6|§17.6]]), determining a smooth structure by Theorem [[§17 Differentiable Structures#^thm-17-5|§17.5]]. Hausdorffness, second countability and compactness are Propositions [[§9 Complex Projective Space#^prop-9-1|§9.1]] and [[§9 Complex Projective Space#^prop-9-2|§9.2]] (proved for $S^{2n+1}/S^1$, which carries the same topology as $(\mathbb{C}^{n+1}\setminus\{0\})/\mathbb{C}^\times$ by Proposition [[§9 Complex Projective Space#^prop-9-3|§9.3]]). Together with the charts onto open subsets of $\mathbb{R}^{2n}$, which make $\mathbb{CP}^n$ locally Euclidean of dimension $2n$ (Proposition [[§2 Topological Manifolds#^prop-2-3|§2.3]]), these make $\mathbb{CP}^n$ a topological manifold of dimension $2n$ (Definition [[§2 Topological Manifolds#^def-2-2|§2.2]]), and with the atlas a compact smooth manifold of real dimension $2n$.

^pf-18-2

*Uses:* [[§18 Projective Spaces as Smooth Manifolds#^prop-18-1|§18.1]], [[§17 Differentiable Structures#^def-17-4|Def. §17.4]], [[§17 Differentiable Structures#^def-17-6|Def. §17.6]], [[§17 Differentiable Structures#^thm-17-5|§17.5]], [[§9 Complex Projective Space#^prop-9-1|§9.1]], [[§9 Complex Projective Space#^prop-9-2|§9.2]], [[§11 Topological Groups and Classical Matrix Groups#^def-11-9|Def. §11.9]], [[§8 Algebra of Differentiable Functions#^thm-8-6|452 §8.6]], [[§18 Projective Spaces as Smooth Manifolds#^def-18-1|Def. §18.1]], [[§18 Projective Spaces as Smooth Manifolds#^def-18-2|Def. §18.2]], [[§2 Topological Manifolds#^prop-2-11|§2.11]], [[§17 Differentiable Structures#^def-17-3|Def. §17.3]], [[§9 Complex Projective Space#^prop-9-3|§9.3]], [[§2 Topological Manifolds#^prop-2-3|§2.3]], [[§2 Topological Manifolds#^def-2-2|Def. §2.2]]

> [!theorem] Corollary §18.3: $\mathbb{CP}^n$ Is a Complex Manifold
> The transition functions of the standard atlas are holomorphic. Hence $\mathbb{CP}^n$ is a complex manifold of complex dimension $n$, in the sense of [[§17 Differentiable Structures#^def-17-5|Def. §17.5]].

^cor-18-3

> [!proof]+ Proof
> *(Not from lecture; filled in.)* By Definition [[§17 Differentiable Structures#^def-17-5|§17.5]], two things are required: charts with values in open subsets of $\mathbb{C}^n$, which the standard charts $\varphi_i : U_i \to \mathbb{C}^n$ are (Proposition [[§18 Projective Spaces as Smooth Manifolds#^prop-18-1|§18.1]]); and transition functions that are holomorphic with holomorphic inverses. Fix $i \neq j$ (for $i = j$ the transition is the identity). Each component $\vec w \mapsto w_k/w_i$ of a transition function $\varphi_i \circ \varphi_j^{-1}$ (Theorem [[§18 Projective Spaces as Smooth Manifolds#^thm-18-2|§18.2]]) — including the slot-$j$ component $1/w_i$, by the convention $w_j := 1$ — is a quotient of complex polynomials with denominator nonvanishing on the domain $\{w_i \neq 0\}$, hence holomorphic. A map into $\mathbb{C}^n$ is holomorphic iff each component is, so $\varphi_i \circ \varphi_j^{-1}$ is holomorphic. Its inverse is $\varphi_j \circ \varphi_i^{-1}$, given by the same formula with $i$ and $j$ interchanged, hence holomorphic by the same reasoning. So the standard atlas is a holomorphic atlas with values in $\mathbb{C}^n$, and $\mathbb{CP}^n$ is a complex manifold of complex dimension $n$.

^pf-18-3

*Uses:* [[§18 Projective Spaces as Smooth Manifolds#^thm-18-2|§18.2]], [[§17 Differentiable Structures#^def-17-5|Def. §17.5]], [[§18 Projective Spaces as Smooth Manifolds#^prop-18-1|§18.1]]

> [!theorem] Proposition §18.4: $\mathbb{CP}^1$ Is the Riemann Sphere
> $\mathbb{CP}^1$ is homeomorphic to $S^2$.
>
> *Lee: Problem 4-5(b)*

^prop-18-4

> [!proof]+ Proof
> *(Not from lecture; filled in.)* Points of $\mathbb{CP}^1$ are written $[z_0 : z_1]$ (Definition [[§18 Projective Spaces as Smooth Manifolds#^def-18-1|§18.1]]), and $N = (0,0,1)$ is the north pole. The plan: define $\Phi : S^2 \to \mathbb{CP}^1$, show it is continuous and bijective, and conclude by compactness.
>
> *The two formulas agree.* For $(x,y,z) \in S^2$ the identity $(x+iy)(x-iy) = x^2 + y^2 = (1-z)(1+z)$, which holds because $x^2 + y^2 = 1 - z^2$ on $S^2$, shows that $[x+iy : 1-z]$, defined when $z \ne 1$, and $[1+z : x-iy]$, defined when $z \ne -1$, are the same point of $\mathbb{CP}^1$ wherever both are defined. (The first is defined when $z \neq 1$ because then $(x+iy, 1-z) \neq 0$, and the second when $z \neq -1$ likewise.) In detail: if $z \neq \pm 1$, then $x^2 + y^2 = 1 - z^2 > 0$, so $x - iy \neq 0$, and $\lambda = (x-iy)/(1-z) \in \mathbb{C}^\times$ satisfies, by the identity,
>
> $$
> \lambda\,(x+iy) = \frac{x^2+y^2}{1-z} = \frac{(1-z)(1+z)}{1-z} = 1+z, \qquad \lambda\,(1-z) = x - iy .
> $$
>
> So $(1+z, x-iy) = \lambda\,(x+iy, 1-z)$, and the two classes are equal.
>
> *$\Phi$ is well defined and continuous.* So there is a well-defined map $\Phi : S^2 \to \mathbb{CP}^1$, given by the first formula on $O_+ = \{z \ne 1\}$ and by the second on $O_- = \{z \ne -1\}$. On $O_+$ it is the composite of the continuous map $(x,y,z) \mapsto (x+iy, 1-z)$ into $\mathbb{C}^2 \setminus \{0\}$ with the continuous projection $\pi$, and similarly on $O_-$; so $\Phi$ is continuous on each of the two open sets $\{z \ne 1\}$ and $\{z \ne -1\}$ covering $S^2$, hence continuous. (For $W \subseteq \mathbb{CP}^1$ open, $\Phi^{-1}(W) = (\Phi|_{O_+})^{-1}(W) \cup (\Phi|_{O_-})^{-1}(W)$, and each piece is open in an open subset of $S^2$, hence open in $S^2$.)
>
> *$\Phi$ on $S^2 \setminus \{N\}$.* The point of $S^2$ with $z = 1$ is $N$ (then $x^2 + y^2 = 0$), so $O_+ = S^2 \setminus \{N\}$. On $S^2 \setminus \{N\}$ it is $p \mapsto [\sigma(p) : 1]$, where $\sigma(x,y,z) = (x+iy)/(1-z)$ is the stereographic projection: multiply the representative $(x+iy, 1-z)$ by $1/(1-z)$. This is a bijection onto $\mathbb{C}$, with inverse $w \mapsto \big(2\operatorname{Re} w,\, 2\operatorname{Im} w,\, |w|^2 - 1\big)/(|w|^2+1)$. To check both composites: for $p = (x,y,z) \in S^2 \setminus \{N\}$ and $w = \sigma(p)$,
>
> $$
> |w|^2 = \frac{x^2+y^2}{(1-z)^2} = \frac{1+z}{1-z}, \qquad |w|^2 + 1 = \frac{2}{1-z}, \qquad |w|^2 - 1 = \frac{2z}{1-z},
> $$
>
> so $\big(2\operatorname{Re} w, 2\operatorname{Im} w, |w|^2 - 1\big)/(|w|^2+1) = \big(\tfrac{2x}{1-z}, \tfrac{2y}{1-z}, \tfrac{2z}{1-z}\big) \cdot \tfrac{1-z}{2} = (x,y,z)$. Conversely, for $w \in \mathbb{C}$ the point $q = \big(2\operatorname{Re} w, 2\operatorname{Im} w, |w|^2 - 1\big)/(|w|^2+1)$ satisfies
>
> $$
> |q|^2 = \frac{4|w|^2 + (|w|^2-1)^2}{(|w|^2+1)^2} = \frac{(|w|^2+1)^2}{(|w|^2+1)^2} = 1,
> $$
>
> its third coordinate is $<1$, so $q \in S^2 \setminus \{N\}$; and $1 - q_3 = 2/(|w|^2+1)$, so $\sigma(q) = \dfrac{2w/(|w|^2+1)}{2/(|w|^2+1)} = w$. So $\Phi$ maps $S^2 \setminus \{N\}$ bijectively onto $U_1 = \{[w : 1]\}$: there $\Phi = \varphi_1^{-1} \circ \sigma$, where $\varphi_1^{-1}(w) = [w : 1]$ is the inverse of the standard chart $\varphi_1$, a bijection $\mathbb{C} \to U_1$ (Proposition [[§18 Projective Spaces as Smooth Manifolds#^prop-18-1|§18.1]] with $n = 1$, $i = 1$).
>
> *$\Phi$ at $N$.* Since $N \in O_-$, the second formula gives $\Phi(N) = [2 : 0] = [1:0]$, and this is the one point outside $U_1$: every point outside $U_1$ has the form $[z_0 : 0]$ with $z_0 \neq 0$, which equals $[1 : 0]$. Hence $\Phi$ is a bijection $S^2 \to \mathbb{CP}^1$.
>
> *Conclusion.* Thus $\Phi$ is a continuous bijection from the compact $S^2$ (closed and bounded in $\mathbb{R}^3$, Proposition [[§1 Point-Set Topology Review#^prop-1-8|§1.8]](1)) onto the Hausdorff $\mathbb{CP}^1$ (Proposition [[§9 Complex Projective Space#^prop-9-1|§9.1]]), hence a homeomorphism (Proposition [[§1 Point-Set Topology Review#^prop-1-8|§1.8]](6)).

^pf-18-4

*Uses:* [[§18 Projective Spaces as Smooth Manifolds#^def-18-1|Def. §18.1]], [[§18 Projective Spaces as Smooth Manifolds#^def-18-2|Def. §18.2]], [[§9 Complex Projective Space#^prop-9-1|§9.1]], [[§1 Point-Set Topology Review#^prop-1-8|§1.8]], [[§10 Continuous Functions#^thm-10-4|590 §10.4 (local formulation of continuity)]], [[Heine–Borel Theorem|590 §18.12 (Heine–Borel)]], [[Bijection from Compact to Hausdorff is a Homeomorphism|590 §18.7]], [[§18 Projective Spaces as Smooth Manifolds#^prop-18-1|§18.1]]

> [!remark] Remark
> For $n = 1$ there are two standard charts and a single transition function, $w \mapsto 1/w$ on $\mathbb{C} \setminus \{0\}$ — the complex counterpart of the stereographic transition $u \mapsto 1/u$ of [[§17 Differentiable Structures#^ex-17-3|Ex. §17.3]].

^rem-18-2

> [!remark]- Connections
> - S² as the one-point compactification of ℝ² ≅ ℂ, by the same stereographic projection: [[§20 Local Compactness#^ex-20-7|590 Ex. §20.7]].
> - Computational version: [[§17 Limits Involving the Point at Infinity#^def-17-2|342 Def. §17.2]] (the extended complex plane as the Riemann sphere, by stereographic projection); the chart at ∞ is z ↦ 1/z, which reduces limits at ∞ to limits at 0, [[§17 Limits Involving the Point at Infinity#^thm-17-1|342 Thm. §17.1]], and is continuous on the extended plane, [[§97★ The Transformation w = 1∕z#^thm-97-2|342 Thm. §97.2]].

> [!theorem] Corollary §18.5: Real Projective Space
> Let $\mathbb{RP}^n = S^n/\{\pm 1\} \cong (\mathbb{R}^{n+1}\setminus\{0\})/\mathbb{R}^\times$, the space of real lines through the origin in $\mathbb{R}^{n+1}$. With $U_i = \{[\vec x] \mid x_i \neq 0\}$ and $\varphi_i([\vec x]) = (x_k/x_i)_{k \neq i}$, the family $\{(U_i, \varphi_i)\}_{i=0}^n$ is a smooth atlas, and $\mathbb{RP}^n$ is a compact smooth manifold of dimension $n$.
>
> *Lee: Example 1.33*

^cor-18-5

> [!proof]+ Proof
> *(Not from lecture; filled in.)* Every argument of [[§9 Complex Projective Space|§9]] and of this section goes through verbatim with $\mathbb{R}$, $\mathbb{R}^\times$, $\{\pm1\}$ and $S^n$ in place of $\mathbb{C}$, $\mathbb{C}^\times$, $S^1$ and $S^{2n+1}$: the group $\{\pm 1\}$ is finite, hence compact, and acts on $S^n$ by isometries; the transition maps are the real rational functions $x_k/x_i$. Hausdorffness can alternatively be read off from Corollary [[§13 Group Actions and Orbit Spaces#^cor-13-4|§13.4]]. Step by step:
>
> *The two descriptions.* Proposition [[§9 Complex Projective Space#^prop-9-3|§9.3]] with this renaming: the orbit of $\vec x \neq 0$ under $\mathbb{R}^\times$ is the punctured line $\mathbb{R}\vec x \setminus \{0\}$, and $\mathbb{R}^\times \vec x \mapsto \{\pm \vec x/|\vec x|\}$ is a homeomorphism $(\mathbb{R}^{n+1}\setminus\{0\})/\mathbb{R}^\times \to S^n/\{\pm1\}$; the proof is the same chase, with $g(\vec x) = \vec x/|\vec x|$ satisfying $g(\lambda\vec x) = (\lambda/|\lambda|)\,g(\vec x)$ and $\lambda/|\lambda| = \pm 1$ for $\lambda \in \mathbb{R}^\times$. So the two descriptions of $\mathbb{RP}^n$ carry the same topology. Write $\pi : \mathbb{R}^{n+1}\setminus\{0\} \to \mathbb{RP}^n$, $\vec x \mapsto [\vec x]$, for the quotient map.
>
> *Hausdorff, second countable, compact.* The group $\{\pm 1\}$ acts on $S^n$ by $(\varepsilon, \vec x) \mapsto \varepsilon\vec x$, continuously (a restriction of scalar multiplication), and is finite, hence compact; $S^n$ is compact (closed and bounded, Proposition [[§1 Point-Set Topology Review#^prop-1-8|§1.8]](1)) and Hausdorff (a metric space, Proposition [[§1 Point-Set Topology Review#^prop-1-6|§1.6]](1)). So $S^n/\{\pm1\}$ is Hausdorff by Corollary [[§13 Group Actions and Orbit Spaces#^cor-13-4|§13.4]]; the direct argument for $\mathbb{CP}^n$ of Assignment 2 also applies, since it uses only that the group is compact and acts by isometries. The orbit relation is open (Lemma [[§13 Group Actions and Orbit Spaces#^lem-13-3|§13.3]]) and $S^n$ is second countable (Proposition [[§1 Point-Set Topology Review#^prop-1-6|§1.6]](3)), so $S^n/\{\pm1\}$ is second countable by Theorem [[§6 Open Quotients#^thm-6-3|§6.3]]. It is compact as the continuous image of $S^n$ under the projection (Proposition [[§1 Point-Set Topology Review#^prop-1-8|§1.8]](2)).
>
> *Charts.* As in Proposition [[§18 Projective Spaces as Smooth Manifolds#^prop-18-1|§18.1]] with $\mathbb{R}$ for $\mathbb{C}$. $U_i$ is well defined, since $\lambda x_i \neq 0 \iff x_i \neq 0$ for $\lambda \in \mathbb{R}^\times$, and open, since $\pi^{-1}(U_i) = \{\vec x \neq 0 \mid x_i \neq 0\}$ is the complement of the closed set $H_i \setminus \{0\}$, $H_i = \{x_i = 0\}$. $\varphi_i$ is well defined, since $(\lambda x_k)/(\lambda x_i) = x_k/x_i$. It is a bijection $U_i \to \mathbb{R}^n$ with inverse $\vec w \mapsto [w_0 : \cdots : w_{i-1} : 1 : w_{i+1} : \cdots : w_n]$ ($1$ in slot $i$): applying $\varphi_i$ to this point returns $\vec w$, and for $[\vec x] \in U_i$ the vector $\vec x/x_i$ represents $[\vec x]$ and is $\vec w = \varphi_i([\vec x])$ with $1$ inserted in slot $i$. $\varphi_i$ is continuous by Lemma [[§5 Quotient Maps#^lem-5-7|§5.7]] and Theorem [[§5 Quotient Maps#^thm-5-1|§5.1]], applied to the continuous map $\vec x \mapsto (x_k/x_i)_{k \neq i}$ on $\pi^{-1}(U_i)$, which is constant on the fibres; and its inverse is $\pi$ composed with the continuous map inserting $1$ in slot $i$. So each $\varphi_i$ is a homeomorphism of $U_i$ onto $\mathbb{R}^n$.
>
> *Atlas.* Every $\vec x \neq 0$ has some $x_i \neq 0$, so the $U_i$ cover. For $i \neq j$ the computation of Theorem [[§18 Projective Spaces as Smooth Manifolds#^thm-18-2|§18.2]] gives $\varphi_j(U_i \cap U_j) = \{\vec w \in \mathbb{R}^n \mid w_i \neq 0\}$, an open set, and
>
> $$
> \big(\varphi_i \circ \varphi_j^{-1}\big)(\vec w) = \Big( \frac{w_k}{w_i} \Big)_{k \neq i}, \qquad w_j := 1 .
> $$
>
> Each component is a rational function of real variables with denominator $w_i \neq 0$ on the domain, hence $C^\infty$ — no splitting into real and imaginary parts is needed; and the inverse $\varphi_j \circ \varphi_i^{-1}$ is the same formula with $i$ and $j$ interchanged, also $C^\infty$. So all transitions are diffeomorphisms, the charts are pairwise compatible, and $\{(U_i, \varphi_i)\}_{i=0}^n$ is a smooth atlas (Definition [[§17 Differentiable Structures#^def-17-6|§17.6]]), determining a smooth structure (Theorem [[§17 Differentiable Structures#^thm-17-5|§17.5]]). The charts take values in $\mathbb{R}^n$, so $\mathbb{RP}^n$ is locally Euclidean of dimension $n$; with the two point-set conditions above it is a topological $n$-manifold (Definition [[§2 Topological Manifolds#^def-2-2|§2.2]]), and with this atlas a compact smooth manifold of dimension $n$.

^pf-18-5

*Uses:* [[§9 Complex Projective Space#^prop-9-1|§9.1]], [[§9 Complex Projective Space#^prop-9-2|§9.2]], [[§9 Complex Projective Space#^prop-9-3|§9.3]], [[§18 Projective Spaces as Smooth Manifolds#^prop-18-1|§18.1]], [[§18 Projective Spaces as Smooth Manifolds#^thm-18-2|§18.2]], [[§13 Group Actions and Orbit Spaces#^cor-13-4|§13.4]], [[§1 Point-Set Topology Review#^prop-1-8|§1.8]], [[§1 Point-Set Topology Review#^prop-1-6|§1.6]], [[§13 Group Actions and Orbit Spaces#^lem-13-3|§13.3]], [[§6 Open Quotients#^thm-6-3|§6.3]], [[§5 Quotient Maps#^lem-5-7|§5.7]], [[§5 Quotient Maps#^thm-5-1|§5.1]], [[§17 Differentiable Structures#^def-17-6|Def. §17.6]], [[§17 Differentiable Structures#^thm-17-5|§17.5]], [[§2 Topological Manifolds#^def-2-2|Def. §2.2]]

> [!remark]- Connections
> - The same space in 590, projective $n$-space: [[§38 Fundamental Group of Some Surfaces#^def-38-2|590 Def. §38.2]], [[Projective plane]]; the double cover $S^n \to \mathbb{RP}^n$ as a local diffeomorphism: [[§40 Projective Spaces and the Hopf Fibration#^ex-40-1|Ex. §40.1]].

![[m591-8-6.svg]]
*The chart $U_0$ of $\mathbb{RP}^1$, drawn in the plane of homogeneous coordinates. A point of $\mathbb{RP}^1$ is a line through the origin. A line $L$ with $x_0 \ne 0$ meets the affine line $x_0 = 1$ in exactly one point, $(1, x_1/x_0)$, and the chart $\varphi_0(L) = x_1/x_0$ records where. The one line with $x_0 = 0$ — the $x_1$-axis, the point $[0:1]$ — is parallel to $x_0 = 1$ and never meets it: it is the point at infinity that $U_0$ misses, and the second chart $U_1$ covers it. On the right, $\mathbb{RP}^1$ drawn as a circle, with $U_0$ everything except the top point. In $\mathbb{RP}^n$ the same picture holds with the affine hyperplane $x_0 = 1$ in place of the line.*

> [!theorem] Proposition §18.6: The Two Topologies on $\mathbb{RP}^n$ Agree
> 1. Under $[\vec x] \mapsto \mathbb{R}\vec x$, the quotient topology on $\mathbb{RP}^n = S^n/\{\pm1\}$ agrees with the topology of $\mathrm{Gr}_1(\mathbb{R}^{n+1})$ transported from the coset space $\mathrm{O}(n+1)/(\mathrm{O}(1)\times\mathrm{O}(n))$ in [[§14 Homogeneous Spaces|§14]].
> 2. $\mathbb{RP}^1$ is homeomorphic to $S^1$.
>
> *Lee: Examples 1.5 and 1.33*

^prop-18-6

> [!proof]+ Proof
> *(Not from lecture; filled in.)* (1) Write $\pi : S^n \to S^n/\{\pm1\}$, $\vec x \mapsto [\vec x] = \{\vec x, -\vec x\}$, and $\beta : S^n/\{\pm1\} \to \mathrm{Gr}_1(\mathbb{R}^{n+1})$, $[\vec x] \mapsto \mathbb{R}\vec x$, a bijection because each line through $0$ meets $S^n$ in exactly one antipodal pair (Remark [[§15 The Topology of G∕H and Real Grassmannians#^rem-15-3|remark]]). The claim is that $\beta$ is a homeomorphism when $\mathrm{Gr}_1(\mathbb{R}^{n+1})$ carries the topology of Corollary [[§15 The Topology of G∕H and Real Grassmannians#^cor-15-8|§15.8]].
>
> *The action.* $\mathrm{O}(n+1)$ acts on $S^n/\{\pm1\}$ by $g \cdot [\vec x] = [g\vec x]$, continuously: the map $\mathrm{id} \times \pi : \mathrm{O}(n+1) \times S^n \to \mathrm{O}(n+1) \times S^n/\{\pm1\}$ is an open continuous surjection, hence a quotient map, and the action descends along it by the universal property. In detail: for $g \in \mathrm{O}(n+1)$, $|g\vec x| = |\vec x| = 1$ and $g(-\vec x) = -g\vec x$, so $[g\vec x] \in S^n/\{\pm1\}$ depends only on $[\vec x]$; and $I \cdot [\vec x] = [\vec x]$, $g \cdot (g' \cdot [\vec x]) = [gg'\vec x] = (gg') \cdot [\vec x]$, so this is an action. The map $\mathrm{id} \times \pi$ is continuous by Theorem [[§3 Subspaces and Products#^thm-3-10|§3.10]] (its components $\mathrm{id} \circ \pi_1$ and $\pi \circ \pi_2$ are continuous), surjective because $\pi$ is, and open: $\pi$ is open by Lemma [[§13 Group Actions and Orbit Spaces#^lem-13-3|§13.3]] (it is the projection of the orbit relation of the continuous action $(\varepsilon, \vec x) \mapsto \varepsilon\vec x$ of $\{\pm1\}$), so the image $A \times \pi(B)$ of a basic open box $A \times B$ is open, and the image of a union of boxes is the union of their images. So it is a quotient map by Proposition [[§5 Quotient Maps#^prop-5-5|§5.5]]. The map $(g, \vec x) \mapsto \pi(g\vec x)$ on $\mathrm{O}(n+1) \times S^n$ is continuous (matrix multiplication followed by $\pi$) and constant on the fibres $\{(g, \vec x), (g, -\vec x)\}$ of $\mathrm{id} \times \pi$, since $\pi(g(-\vec x)) = \pi(-g\vec x) = \pi(g\vec x)$. By Theorem [[§5 Quotient Maps#^thm-5-1|§5.1]] it descends to a continuous map $\mathrm{O}(n+1) \times S^n/\{\pm1\} \to S^n/\{\pm1\}$, $(g, [\vec x]) \mapsto [g\vec x]$, which is the action; so the action is continuous (Definition [[§13 Group Actions and Orbit Spaces#^def-13-2|§13.2]]).
>
> *Transitive, with the Grassmannian's isotropy group.* The action is transitive: given $[\vec x], [\vec y]$, Proposition [[§15 The Topology of G∕H and Real Grassmannians#^prop-15-6|§15.6]] (with $k = 1$ and $n+1$ in place of $n$) gives $g \in \mathrm{O}(n+1)$ with $g(\mathbb{R}\vec x) = \mathbb{R}\vec y$, so $g\vec x = c\,\vec y$ with $|c| = |g\vec x| = 1$, i.e. $c = \pm 1$, and $g \cdot [\vec x] = [\pm\vec y] = [\vec y]$. Let $e_1$ be the first standard basis vector of $\mathbb{R}^{n+1}$ and $V_0 = \mathbb{R}e_1$. Then $g \cdot [e_1] = [e_1]$ iff $ge_1 = \pm e_1$ iff $g V_0 = V_0$ (as $|ge_1| = 1$), so the isotropy group $H$ of $[e_1]$ equals that of $V_0$ in $\mathrm{Gr}_1(\mathbb{R}^{n+1})$, which is $\mathrm{O}(1) \times \mathrm{O}(n)$ by Proposition [[§15 The Topology of G∕H and Real Grassmannians#^prop-15-7|§15.7]].
>
> *The homeomorphism.* The action is transitive, the coset space is compact, and $S^n/\{\pm1\}$ is Hausdorff, so Theorem [[§15 The Topology of G∕H and Real Grassmannians#^thm-15-3|§15.3]] identifies $S^n/\{\pm1\}$ homeomorphically with the coset space — which is precisely the transported topology. In detail: $\mathrm{O}(n+1)/H$ is compact as the image of the compact group $\mathrm{O}(n+1)$ (shown in the proof of Corollary [[§15 The Topology of G∕H and Real Grassmannians#^cor-15-8|§15.8]]) under the continuous projection (Proposition [[§1 Point-Set Topology Review#^prop-1-8|§1.8]](2)), and $S^n/\{\pm1\}$ is Hausdorff by Corollary [[§13 Group Actions and Orbit Spaces#^cor-13-4|§13.4]]. So Theorem [[§15 The Topology of G∕H and Real Grassmannians#^thm-15-3|§15.3]](2) makes $\Phi_1 : \mathrm{O}(n+1)/H \to S^n/\{\pm1\}$, $gH \mapsto g \cdot [e_1] = [ge_1]$, a homeomorphism. On the other side, $\Phi_2 : \mathrm{O}(n+1)/H \to \mathrm{Gr}_1(\mathbb{R}^{n+1})$, $gH \mapsto gV_0$, is a homeomorphism by the definition of the transported topology (Definition [[§15 The Topology of G∕H and Real Grassmannians#^def-15-2|§15.2]], Corollary [[§15 The Topology of G∕H and Real Grassmannians#^cor-15-8|§15.8]]). Since $\beta([ge_1]) = \mathbb{R}\,ge_1 = gV_0$, we have $\beta \circ \Phi_1 = \Phi_2$, so $\beta = \Phi_2 \circ \Phi_1^{-1}$ is a composite of homeomorphisms. That is, a set $W \subseteq \mathbb{RP}^n$ is open in the quotient topology iff $\beta(W)$ is open in the transported topology.
>
> (2) Let $\sigma_N, \sigma_S$ be the stereographic charts of Example [[§17 Differentiable Structures#^ex-17-3|§17.3]], and $\varphi_0, \varphi_1$ the standard charts of $\mathbb{RP}^1$, $\varphi_0([x_0 : x_1]) = x_1/x_0$ on $U_0 = \{x_0 \neq 0\}$ and $\varphi_1([x_0 : x_1]) = x_0/x_1$ on $U_1 = \{x_1 \neq 0\}$. Define $F = \sigma_N^{-1} \circ \varphi_0$ on $U_0$ and $F = \sigma_S^{-1} \circ \varphi_1$ on $U_1$.
>
> *Well defined and continuous.* On $U_0 \cap U_1$ we have $\varphi_1 = 1/\varphi_0$, since $x_0/x_1 = 1/(x_1/x_0)$, with $\varphi_0 \neq 0$ there; and $\sigma_S \circ \sigma_N^{-1}(u) = 1/u$ for $u \neq 0$ gives, applying $\sigma_S^{-1}$, $\sigma_N^{-1}(u) = \sigma_S^{-1}(1/u)$. So for $\ell \in U_0 \cap U_1$, with $u = \varphi_0(\ell)$,
>
> $$
> \sigma_S^{-1}\big(\varphi_1(\ell)\big) = \sigma_S^{-1}(1/u) = \sigma_N^{-1}(u) = \sigma_N^{-1}\big(\varphi_0(\ell)\big):
> $$
>
> the two formulas agree and $F$ is well defined. It is continuous on each of the open sets $U_0$, $U_1$ (a composite of homeomorphisms), which cover $\mathbb{RP}^1$, so it is continuous.
>
> *Bijective.* It maps $U_0$ bijectively onto $S^1 \setminus \{N\}$, as the composite of the bijections $\varphi_0 : U_0 \to \mathbb{R}$ and $\sigma_N^{-1} : \mathbb{R} \to S^1 \setminus \{N\}$. The one point outside $U_0$ is $[0:1]$ (a point $[0 : x_1]$ has $x_1 \neq 0$ and equals $[0:1]$), and $F([0:1]) = \sigma_S^{-1}(\varphi_1([0:1])) = \sigma_S^{-1}(0) = N$, since $\sigma_S(N) = 0/(1+1) = 0$. So $F$ is a bijection onto $S^1$. So $F$ is a continuous bijection from the compact $\mathbb{RP}^1$ (Corollary [[§18 Projective Spaces as Smooth Manifolds#^cor-18-5|§18.5]]) onto the Hausdorff $S^1$ (a metric space, Proposition [[§1 Point-Set Topology Review#^prop-1-6|§1.6]](1)), hence a homeomorphism (Proposition [[§1 Point-Set Topology Review#^prop-1-8|§1.8]](6)).
>
> *Diffeomorphism.* Both transition functions are $u \mapsto 1/u$, and in the charts used $F$ has coordinate representation the identity; so it is even a diffeomorphism, in the sense of Definition [[§19 Smooth Functions and Smooth Maps#^def-19-4|§19.4]] below. Explicitly, with $S^1$ carrying the stereographic atlas: $F(U_0) = S^1 \setminus \{N\}$ and $\sigma_N \circ F \circ \varphi_0^{-1} = \sigma_N \circ \sigma_N^{-1} \circ \varphi_0 \circ \varphi_0^{-1} = \mathrm{id}_{\mathbb{R}}$; likewise $\sigma_S \circ F \circ \varphi_1^{-1} = \mathrm{id}_{\mathbb{R}}$; and $F^{-1}$ is $\varphi_0^{-1} \circ \sigma_N$ on $S^1 \setminus \{N\}$ and $\varphi_1^{-1} \circ \sigma_S$ on $S^1 \setminus \{S\}$, with coordinate representations $\varphi_0 \circ F^{-1} \circ \sigma_N^{-1} = \mathrm{id}_{\mathbb{R}}$ and $\varphi_1 \circ F^{-1} \circ \sigma_S^{-1} = \mathrm{id}_{\mathbb{R}}$, all smooth.

^pf-18-6

*Uses:* [[§5 Quotient Maps#^prop-5-5|§5.5]], [[§5 Quotient Maps#^thm-5-1|§5.1]], [[§15 The Topology of G∕H and Real Grassmannians#^thm-15-3|§15.3]], [[§15 The Topology of G∕H and Real Grassmannians#^def-15-2|Def. §15.2]], [[§15 The Topology of G∕H and Real Grassmannians#^cor-15-8|§15.8]], [[§17 Differentiable Structures#^ex-17-3|Ex. §17.3]], [[§18 Projective Spaces as Smooth Manifolds#^cor-18-5|§18.5]], [[§19 Smooth Functions and Smooth Maps#^def-19-3|Def. §19.3]], [[§19 Smooth Functions and Smooth Maps#^def-19-4|Def. §19.4]], [[§10 Continuous Functions#^thm-10-4|590 §10.4 (local formulation of continuity)]], [[Bijection from Compact to Hausdorff is a Homeomorphism|590 §18.7]], [[§15 The Topology of G∕H and Real Grassmannians#^rem-15-3|§15.3]], [[§3 Subspaces and Products#^thm-3-10|§3.10]], [[§13 Group Actions and Orbit Spaces#^lem-13-3|§13.3]], [[§13 Group Actions and Orbit Spaces#^def-13-2|Def. §13.2]], [[§15 The Topology of G∕H and Real Grassmannians#^prop-15-6|§15.6]], [[§15 The Topology of G∕H and Real Grassmannians#^prop-15-7|§15.7]], [[§1 Point-Set Topology Review#^prop-1-8|§1.8]], [[§13 Group Actions and Orbit Spaces#^cor-13-4|§13.4]], [[§1 Point-Set Topology Review#^prop-1-6|§1.6]]

> [!remark]- Connections
> - $P^1 \cong S^1$ in 590: [[§38 Fundamental Group of Some Surfaces#^thm-38-3|590 §38.3]]; Grassmannians as homogeneous spaces: [[§15 The Topology of G∕H and Real Grassmannians#^cor-15-8|§15.8]].

![[m591-8-7.svg]]
*The quotient $S^n \to \mathbb{RP}^n$ of [[§18 Projective Spaces as Smooth Manifolds#^prop-18-6|§18.6]], drawn for $n = 2$. A line through the origin meets the sphere in two antipodal points $p$ and $-p$, which $\pi$ identifies. Every line meets the closed upper hemisphere: once if it is not horizontal, and in a pair of antipodal points $q$, $-q$ of the equator if it is. So $\mathbb{RP}^2$ can be pictured as a closed disc with antipodal boundary points glued, as the arrows indicate. For $n = 1$ the same gluing closes a half-circle into a circle, which is $\mathbb{RP}^1 \cong S^1$.*
