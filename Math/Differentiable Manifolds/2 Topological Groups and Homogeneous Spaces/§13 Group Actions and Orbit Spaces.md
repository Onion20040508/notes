---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 2
section: 13
tags: [differentiable-manifolds, math591]
---
← [[§12 The Classical Groups Are Topological Manifolds]] · ↑ [[· 2 Topological Groups and Homogeneous Spaces]] · [[§14 Homogeneous Spaces]] →

*Thread: quotients — Orbit spaces generalize the quotients of [[§4 Quotient Spaces and Open Maps|§4]]–[[§6 Open Quotients|§6]] — $\mathbb{CP}^n = S^{2n+1}/\mathrm{U}(1)$ — and the Hausdorff question returns (Corollary [[§13 Group Actions and Orbit Spaces#^cor-13-4|§13.4]]).*

*Reference: Lee Ch. 21 (“Quotient Manifolds”), the sections on group actions and quotients by group actions.*

> [!remark] Remark: Why This Section
> This returns to the quotient thread of [[§4 Quotient Spaces and Open Maps|§4]]–[[§6 Open Quotients|§6]]: a great many interesting manifolds are quotients, and among those, most are *orbit spaces* of group actions. [[§6 Open Quotients|§6]] gave a criterion (Theorem [[§6 Open Quotients#^thm-6-1|§6.1]]) for a quotient by an *open* relation to be Hausdorff. The main result here is that orbit relations of continuous actions are *always* open, so the criterion applies to every orbit space—“this is one of the main uses of our theorem”—and the payoff is a clean sufficient condition (Corollary [[§13 Group Actions and Orbit Spaces#^cor-13-4|§13.4]]) for an orbit space to be Hausdorff.

^rem-13-1

## Actions and Orbits

> [!definition] Definition §13.1: Group Action
> Let $G$ be a group and $X$ a set. A (left) **action** of $G$ on $X$ is a map
>
> $$
> G \times X \to X, \qquad (g, x) \mapsto g \cdot x,
> $$
>
> such that
> 1. $e \cdot x = x$ for all $x \in X$, where $e \in G$ is the identity; and
> 2. $g \cdot (h \cdot x) = (gh) \cdot x$ for all $g, h \in G$ and $x \in X$, where $gh$ is the product in $G$.
>
> *Lee: Ch. 7, Group Actions and Equivariant Maps*

^def-13-1

> [!remark]- Connections
> - Home of the algebra of actions: [[§25 Actions#^def-25-1|493 Def. §25.1 (Action)]], [[§25 Actions#^def-25-2|493 Def. §25.2 (Right Action)]]; the permutation picture [[Actions Are Homomorphisms to S_X]].

> [!example] Example §13.1: Matrix Groups Acting on Column Vectors
> Each of the groups over $\mathbb{R}$ above ($\mathrm{GL}(n,\mathbb{R})$, $\mathrm{SL}$, $\mathrm{O}$, $\mathrm{SO}$) acts on $X = \mathbb{R}^n$, regarded as column vectors, by matrix multiplication $g \cdot x = gx$: $Ix = x$, and $g(hx) = (gh)x$ by associativity of matrix multiplication. Likewise the complex groups act on $\mathbb{C}^n$.

^ex-13-1

> [!remark]- Connections
> - In 493: [[§32 Linear Groups, the Cube, S₃ and A₄#^prop-32-1|493 §32.1 (GL₃ acting on ℝ³)]], [[§32 Linear Groups, the Cube, S₃ and A₄#^prop-32-2|493 §32.2 (O₃ acting on ℝ³)]]; the groups themselves: [[Matrix groups GLₙ, SLₙ and O(n)]].

> [!example] Example §13.2: A Subgroup Acting by Multiplication
> If $H \le G$ is a subgroup, then $H$ acts on $G$ by group multiplication, $H \times G \to G$, $(h, g) \mapsto hg$: axiom (1) is $eg = g$, axiom (2) is $h_1(h_2 g) = (h_1 h_2) g$. Note the notational clash with Definition [[§13 Group Actions and Orbit Spaces#^def-13-1|§13.1]]: here $H$ plays the role of the acting group and $G$ the role of the set.

^ex-13-2

> [!remark]- Connections
> - In 493 the orbits of this action are the right cosets: [[§28 Left and Right Cosets#^prop-28-1|493 §28.1 (Cosets Are Orbits)]]; the left-coset version is [[§14 Homogeneous Spaces#^prop-14-4|§14.4]].

> [!definition] Definition §13.2: Continuous Action
> If $G$ is a topological group and $X$ a topological space, an action is **continuous** if the map $G \times X \to X$, $(g,x) \mapsto g \cdot x$, is continuous (product topology on $G \times X$).

^def-13-2

> [!remark] Remark
> Both examples above are continuous: matrix multiplication $g x$ is polynomial in the entries of $(g, x)$, and $(h, g) \mapsto hg$ is the restriction to $H \times G$ of the (continuous) multiplication of $G$. For a continuous action each individual map $x \mapsto g \cdot x$ is a homeomorphism of $X$ (Lemma [[§13 Group Actions and Orbit Spaces#^lem-13-2|§13.2]] below).

^rem-13-2

> [!definition] Definition §13.3: Orbit
> Assume $G$ acts on $X$. The **orbit** of $x \in X$ is
>
> $$
> \mathcal{O}_x = \{\, g \cdot x \mid g \in G \,\} \subseteq X,
> $$
>
> the set of everything reachable from $x$ by acting with elements of $G$.
>
> *Lee: Ch. 7, Group Actions and Equivariant Maps*

^def-13-3

> [!remark]- Connections
> - Home: [[§27 Orbits#^def-27-1|493 Def. §27.1 (Orbit)]], where the orbit is written $Gx$.

> [!remark] Remark: What an Orbit Is
> The orbit of $x$ is the set of all places $x$ can be sent by the group: everything *reachable* from $x$ by acting with some $g \in G$. Two questions determine what an orbit looks like: what does the group *preserve*, and what does it *mix*? Whatever quantity is preserved by every $g$ is constant on orbits (so the orbit lies inside a level set of it); whatever the group can mix, it mixes within that level set. For rotations of $\mathbb{R}^n$ the preserved quantity is the norm $|x|$, and rotations mix everything of a given norm; so the orbits are spheres (Example [[§13 Group Actions and Orbit Spaces#^ex-13-4|§13.4]], Example [[§13 Group Actions and Orbit Spaces#^ex-13-5|§13.5]]).

^rem-13-3

> [!definition] Definition §13.4: Orbit Relation
> For an action of a group $G$ on a set $X$, the **orbit relation** on $X$ is
>
> $$
> x \sim y \iff \text{there is } g \in G \text{ with } y = g \cdot x .
> $$
>
> *Lee: proof of Proposition 21.4, where it is also called the orbit relation*

^def-13-4

> [!theorem] Proposition §13.1: Orbits Partition $X$
> The orbit relation $\sim$ of Definition [[§13 Group Actions and Orbit Spaces#^def-13-4|§13.4]] is an equivalence relation, its equivalence classes are exactly the orbits, and consequently the orbits partition $X$.
>
> *Lee: Ch. 7, Group Actions and Equivariant Maps*

^prop-13-1

> [!proof]+ Proof
> *(Claimed in Lecture 4 — “Claim: this is an equivalence relation”; filled in.)* *Reflexive:* $x = e \cdot x$. *Symmetric:* if $y = g \cdot x$ then $g^{-1} \cdot y = g^{-1} \cdot (g \cdot x) = (g^{-1} g) \cdot x = e \cdot x = x$, so $x = g^{-1} \cdot y$. *Transitive:* if $y = g \cdot x$ and $z = h \cdot y$ then $z = h \cdot (g \cdot x) = (hg) \cdot x$. The class of $x$ is $\{y \mid \exists g,\ y = g \cdot x\} = \mathcal{O}_x$ by definition. Equivalence classes of an equivalence relation partition the underlying set.

^pf-13-1

*Uses:* [[§13 Group Actions and Orbit Spaces#^def-13-1|Def. §13.1]], [[§13 Group Actions and Orbit Spaces#^def-13-3|Def. §13.3]], [[§13 Group Actions and Orbit Spaces#^def-13-4|Def. §13.4]], [[§24 Equivalence Relations and Partitions#^prop-24-1|493 §24.1]]

> [!remark]- Connections
> - Home of this result: [[§27 Orbits#^prop-27-2|493 §27.2 (The Orbit Relation)]], with a direct proof in [[§27 Orbits#^prop-27-1|493 §27.1 (Orbits Partition X)]].

> [!remark] Remark: “Reachable” Is the Equivalence Relation
> In words: *$x \sim y$ iff $y$ can be reached from $x$ by the action*, and the orbit of $x$ is its equivalence class. The point of the proof is that “reachable” is automatically symmetric and transitive *because $G$ is a group*: if $g$ takes $x$ to $y$ then $g^{-1}$ takes $y$ back to $x$, and if $g$ takes $x$ to $y$ and $h$ takes $y$ to $z$ then $hg$ takes $x$ to $z$. Nothing had to be added by hand. Contrast Example [[§4 Quotient Spaces and Open Maps#^ex-4-3|§4.3]] in [[§4 Quotient Spaces and Open Maps#Open Maps and Open Relations|§4]], where the relation on $\mathbb{R}$ had to be *generated* by the single identification $0 \sim 1$ to become an equivalence relation. So the mental sequence for any orbit space is:
> 1. the group moves points around;
> 2. two points are declared equivalent if one can be moved to the other;
> 3. the classes are the orbits, and the orbit space is the set of orbits with the quotient topology.

^rem-13-4

> [!definition] Definition §13.5: Orbit Space
> The **orbit space** of an action of $G$ on $X$ is the quotient
>
> $$
> X/G \;:=\; X/{\sim}
> $$
>
> of $X$ by the orbit relation, with the quotient topology ([[§4 Quotient Spaces and Open Maps|§4, Quotient Spaces]]). Explicitly: a point of $X/G$ is an orbit $\mathcal{O}_x \subseteq X$; the quotient map is $\pi(x) = \mathcal{O}_x$; and $W \subseteq X/G$ is open iff $\bigcup_{\mathcal{O} \in W} \mathcal{O}$ (the union in $X$ of the orbits belonging to $W$) is open in $X$.
>
> *Lee: Ch. 21, Quotients of Manifolds by Group Actions*

^def-13-5

> [!remark]- Connections
> - The underlying set is the orbit set of [[§27 Orbits#^def-27-4|493 Def. §27.4 (Orbit Space Notation)]], written $G \backslash X$ there for a left action.
> - The topology is the quotient topology of [[§13 Quotient Topology#^def-13-3|590 Def. §13.3 (Quotient Space)]].

> [!example] Example §13.3: $\mathbb{CP}^n$ Is an Orbit Space
> The relation of [[§9 Complex Projective Space#^def-9-1|Def. §9.1]] on $S^{2n+1}$, $z \sim w \iff w = \xi z$ for some $\xi \in S^1$, is precisely the orbit relation of the action of $\mathrm{U}(1) = S^1$ on $S^{2n+1}$ by scalar multiplication, $\xi \cdot z = \xi z$, which is continuous, being polynomial in the real coordinates. So $\mathbb{CP}^n = S^{2n+1}/\mathrm{U}(1)$ is an orbit space, and Proposition [[§9 Complex Projective Space#^prop-9-1|§9.1]] was our first Hausdorff orbit space. Which continuous actions have Hausdorff orbit spaces in general is the subject of Corollary [[§13 Group Actions and Orbit Spaces#^cor-13-4|§13.4]] below.
>
> *Lee: cf. Problem 1-9*

^ex-13-3

> [!remark]- Connections
> - The smooth structure on this orbit space: [[§18 Projective Spaces as Smooth Manifolds#^thm-18-2|§18.2 (The Standard Atlas Is Smooth)]].

Complex projective space through the course: the open quotient $S^{2n+1}/S^1$, Hausdorff, second countable and compact, in [[§9 Complex Projective Space|Complex Projective Space]]; the circle group $\mathrm{U}(1)$ acting there in [[§11 Topological Groups and Classical Matrix Groups#^ex-11-3|U(1) is the circle]]; an orbit space in [[§13 Group Actions and Orbit Spaces#^ex-13-3|projective space as an orbit space]]; a smooth and complex manifold through its standard atlas in [[§18 Projective Spaces as Smooth Manifolds|Projective Spaces as Smooth Manifolds]]; a homogeneous space of $\mathrm{U}(n+1)$ in [[§25 The Geometric Tangent Space#^rem-25-9|Dimension Checks through Homogeneous Spaces]]; the domain of the moment map in [[§30 The Differential in Coordinates#^rem-30-5|Remark: The Strategy]]; and the base of the Hopf fibration in [[§39 Projective Spaces and the Hopf Fibration|Projective Spaces and the Hopf Fibration]].

> [!example] Example §13.4: $\mathrm{SO}(2)$ Acting on $\mathbb{R}^2$ — the Picture
> Let $\mathrm{SO}(2,\mathbb{R})$, the rotations of the plane, act on $\mathbb{R}^2$ by matrix multiplication. A rotation preserves $|x|$, so $g \cdot x$ stays on the circle of radius $|x|$; and a rotation through the right angle takes $x$ to any prescribed point of that circle. Hence
>
> $$
> \mathcal{O}_x = \{\, y \in \mathbb{R}^2 \mid |y| = |x| \,\} \ \text{ for } x \neq 0, \qquad \mathcal{O}_0 = \{0\}.
> $$
>
> Every point of a given circle is equivalent to every other point of it, and to nothing off it. The orbit space collapses each circle to a single point, leaving one point per radius:
>
> $$
> \mathbb{R}^2/\mathrm{SO}(2) \;\cong\; [0, \infty), \qquad [x] \longmapsto |x|.
> $$

^ex-13-4

![[m591-6-1.svg]]
*The orbits of $\mathrm{SO}(2)$ on $\mathbb{R}^2$: each circle about the origin is one orbit and the origin is its own orbit; the projection $\pi$ collapses each circle to its radius, so $\mathbb{R}^2/\mathrm{SO}(2) \cong [0,\infty)$.*

> [!example] Example §13.5: $\mathrm{SO}(3)$ Acting on $\mathbb{R}^3$
> This is the previous example one dimension up, with spheres in place of circles. Let $\mathrm{SO}(3,\mathbb{R})$ act on $\mathbb{R}^3$ by matrix multiplication. Orthogonal matrices preserve the norm ($|gx|^2 = (gx)\cdot(gx) = x \cdot x = |x|^2$), so each orbit lies in a sphere $S_r = \{|x| = r\}$ centered at the origin. In fact:
> - $\mathcal{O}_0 = \{0\}$.
> - For $x \neq 0$, $\mathcal{O}_x = S_{|x|}$, the whole sphere of radius $|x|$: given $y$ with $|y| = |x| = r$, let $u = x/r$, $v = y/r$, extend $u$ to an orthonormal basis $(u, u_2, u_3)$ and $v$ to an orthonormal basis $(v, v_2, v_3)$ of $\mathbb{R}^3$ (Gram–Schmidt), replacing $u_3$ by $-u_3$ if necessary so that both bases are positively oriented; then the matrix $g$ with $g u = v$, $g u_2 = v_2$, $g u_3 = v_3$ maps an orthonormal basis to an orthonormal basis, so $g \in \mathrm{O}(3)$, and it maps a positive basis to a positive basis, so $\det g > 0$, i.e. $g \in \mathrm{SO}(3)$; and $g x = r\, g u = r v = y$.
>
> So the orbits are the concentric spheres together with the origin, and the orbit space is parametrized by the radius:
>
> $$
> \mathbb{R}^3/\mathrm{SO}(3) \;\cong\; [0, \infty).
> $$

^ex-13-5

> [!proof]+ Proof that $\mathbb{R}^3/\mathrm{SO}(3) \cong [0,\infty)$
> *(Not from lecture; filled in.)* Define $\rho : \mathbb{R}^3/\mathrm{SO}(3) \to [0,\infty)$ by $\rho([x]) = |x|$. It is well defined because $|gx| = |x|$, and it is a bijection by the description of the orbits ($\rho$ is injective since $[x] = [y]$ iff $|x| = |y|$, and surjective since $\rho([(r,0,0)]) = r$). It is continuous by Proposition [[§5 Quotient Maps#^cor-5-2|§5.2]], since $\rho \circ \pi = |\cdot| : \mathbb{R}^3 \to [0,\infty)$ is continuous. Its inverse $[0,\infty) \to \mathbb{R}^3/\mathrm{SO}(3)$, $r \mapsto [(r,0,0)]$, is the composite of the continuous map $r \mapsto (r,0,0)$ with the continuous map $\pi$. Hence $\rho$ is a homeomorphism.

^pf-ex-13-5

*Uses:* [[§13 Group Actions and Orbit Spaces#^ex-13-5|Ex. §13.5]], [[§13 Group Actions and Orbit Spaces#^def-13-5|Def. §13.5]], [[§5 Quotient Maps#^cor-5-2|§5.2]], [[Universal Property of Quotient Maps]]

> [!remark]- Connections
> - The same orbits for $\mathrm{O}_3$, with the orthonormal-basis argument and the bijection with the radius: [[§32 Linear Groups, the Cube, S₃ and A₄#^prop-32-2|493 §32.2]], [[§27 Orbits#^def-27-4|493 Def. §27.4]]; extending to an orthonormal basis is [[§21 Orthonormal Bases#^ladr-6-36|LADR 6.36]] ([[Gram–Schmidt procedure]]).
> - With $r = 1$ this is the transitivity used in [[§14 Homogeneous Spaces#^ex-14-3|The Sphere as a Homogeneous Space, §14.3]].

> [!remark] Remark
> This example was Uribe's last-minute illustration, given verbally; the proof above supplies the details. Compare it with $\mathbb{CP}^n$: there $S^1$ acts on $S^{2n+1}$ by $z \mapsto \xi z$, the orbit of $z$ is the circle $\{\xi z \mid |\xi| = 1\}$ traced inside the big sphere, and *every* orbit is a circle of the same kind—no special points. That uniformity is part of why $\mathbb{CP}^n$ comes out a manifold. The rotation examples already show one thing the coming theory must accommodate: orbits can have different “sizes” (a point and $2$-spheres), and the orbit space can have boundary ($[0,\infty)$ is a manifold *with boundary*, not a manifold). Conditions ruling this out—free actions, properness—are where the theory of quotient manifolds (Lee Ch. 21) is headed.

^rem-13-5

The classical groups through the course: defined in [[§11 Topological Groups and Classical Matrix Groups|Topological Groups and Classical Matrix Groups]], with the examples of [[§16 The Classical Groups|The Classical Groups]]; topological manifolds as level sets in [[§12 The Classical Groups Are Topological Manifolds#^thm-12-6|Classical Groups Are Manifolds]]; $\mathrm{SO}(2)$ and $\mathrm{SO}(3)$ acting on $\mathbb{R}^2$ and $\mathbb{R}^3$ in [[§13 Group Actions and Orbit Spaces#^ex-13-4|the rotations of the plane]] and [[§13 Group Actions and Orbit Spaces#^ex-13-5|the rotations of space]], and $\mathrm{SO}(3)$ on $S^2$ in [[§14 Homogeneous Spaces#^ex-14-2|the isotropy of the north pole]] and [[§14 Homogeneous Spaces#^ex-14-3|the sphere as a homogeneous space]]; $\mathrm{O}(n)$ acting on the Grassmannians in [[§15 The Topology of G∕H and Real Grassmannians#^cor-15-8|Grassmannians as Homogeneous Spaces]]; smooth manifolds in [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-23-1|the orthogonal group]] and [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-23-2|the unitary group]]; their tangent spaces at the identity in [[§25 The Geometric Tangent Space#^thm-25-5|The Classical Groups]], with [[§25 The Geometric Tangent Space#^ex-25-4|the infinitesimal rotations]]; and the double cover $\mathrm{SU}(2) \to \mathrm{SO}(3)$ in [[§41 SU(2) → SO(3)꞉ The Double Cover#^thm-41-4|The Double Cover]].

## Orbit Relations Are Open

Throughout, $G$ is a topological group acting continuously on a topological space $X$ (Definition [[§13 Group Actions and Orbit Spaces#^def-13-1|§13.1]] and [[§13 Group Actions and Orbit Spaces#^def-13-2|the definition following it]]), and $\sim$ is the orbit relation: $x \sim y \iff \exists\, g \in G$ with $y = g \cdot x$ (Proposition [[§13 Group Actions and Orbit Spaces#^prop-13-1|§13.1]]).

> [!theorem] Lemma §13.2: Left Translations Are Homeomorphisms
> For $g \in G$ define $L_g : X \to X$, $L_g(x) = g \cdot x$. Then:
> 1. $L_g$ is continuous;
> 2. $L_g \circ L_{g'} = L_{gg'}$ for all $g, g' \in G$, and $L_e = \mathrm{id}_X$;
> 3. $L_g$ is a homeomorphism with inverse $L_{g^{-1}}$.
>
> *Lee: proof of Lemma 21.1*

^lem-13-2

> [!proof]+ Proof
> *(Lecture 4, in full: Uribe gave this proof “because I want to model what is expected of you when you write your homework.”)* (1) $L_g$ is the composite
>
> $$
> X \longrightarrow G \times X \longrightarrow X, \qquad x \longmapsto (g, x) \longmapsto g \cdot x .
> $$
>
> The first map is continuous by Theorem [[§3 Subspaces and Products#^thm-3-10|§3.10]]: its components are the constant map $x \mapsto g$ and the identity. The second is the action, continuous by hypothesis. A composite of continuous maps is continuous.
>
> (2) For $x \in X$, $(L_g \circ L_{g'})(x) = g \cdot (g' \cdot x) = (gg') \cdot x = L_{gg'}(x)$ by the second action axiom, and $L_e(x) = e \cdot x = x$ by the first.
>
> (3) By (2), $L_g \circ L_{g^{-1}} = L_{gg^{-1}} = L_e = \mathrm{id}_X$ and $L_{g^{-1}} \circ L_g = L_{g^{-1}g} = L_e = \mathrm{id}_X$. So $L_g$ is a bijection with inverse $L_{g^{-1}}$, which is continuous by (1) applied to $g^{-1}$.

^pf-13-2

*Uses:* [[§13 Group Actions and Orbit Spaces#^def-13-1|Def. §13.1]], [[§13 Group Actions and Orbit Spaces#^def-13-2|Def. §13.2]], [[§3 Subspaces and Products#^thm-3-10|§3.10]], [[§10 Continuous Functions#^thm-10-4|590 §10.4]]

> [!remark]- Connections
> - The algebraic half (2)–(3) is [[§25 Actions#^prop-25-2|493 §25.2 (Each Group Element Acts Bijectively)]]; (2) says $g \mapsto L_g$ is a homomorphism, as in [[§25 Actions#^thm-25-3|493 §25.3]].

> [!remark] Remark: A Model Proof
> Uribe: “the reason I want to do this with simple proofs is because I want to model what is expected of you when you write your homework.” The features to imitate: name the map you are studying ($L_g$); prove continuity by exhibiting it as a composite of maps already known to be continuous; get the inverse from the algebra (the action axioms), not from a separate argument; and say which axiom is used where.

^rem-13-6

> [!theorem] Lemma §13.3: Orbit Relations Are Open
> For a continuous action of $G$ on $X$, the orbit relation is an open equivalence relation (Definition of open relation in [[§4 Quotient Spaces and Open Maps#Open Maps and Open Relations|§4, Open Maps and Open Relations]]). Equivalently: for every open $U \subseteq X$, its saturation $\tilde U = \pi^{-1}(\pi(U))$ is open.
>
> *Lee: Lemma 21.1, the same statement and proof*

^lem-13-3

> [!proof]+ Proof
> *(Lecture 4: the saturation of $U$ is the union of the open sets $L_g(U)$.)* By Proposition [[§4 Quotient Spaces and Open Maps#^prop-4-5|§4.5]] it suffices to show the saturation of every open $U$ is open. **Claim:** $\tilde U = \bigcup_{g \in G} L_g(U)$. By definition of saturation and of the orbit relation,
>
> $$
> \tilde U = \{\, y \in X \mid \exists\, x \in U \text{ with } y \sim x \,\} = \{\, y \in X \mid \exists\, x \in U,\ g \in G \text{ with } y = g \cdot x \,\},
> $$
>
> using symmetry of $\sim$ to write $y \sim x$ as $y = g \cdot x$. And $y = g \cdot x$ for some $x \in U$ means exactly $y \in L_g(U)$; so $\tilde U = \bigcup_g L_g(U)$, proving the claim. Each $L_g(U)$ is open, since $L_g$ is a homeomorphism (Lemma [[§13 Group Actions and Orbit Spaces#^lem-13-2|§13.2]]) and homeomorphisms are open maps (Proposition [[§1 Point-Set Topology Review#^prop-1-5|§1.5]](2)). A union of open sets is open.

^pf-13-3

*Uses:* [[§4 Quotient Spaces and Open Maps#^def-4-4|Def. §4.4]], [[§4 Quotient Spaces and Open Maps#^def-4-5|Def. §4.5]], [[§4 Quotient Spaces and Open Maps#^prop-4-5|§4.5]], [[§13 Group Actions and Orbit Spaces#^def-13-4|Def. §13.4]], [[§13 Group Actions and Orbit Spaces#^prop-13-1|§13.1]], [[§13 Group Actions and Orbit Spaces#^lem-13-2|§13.2]], [[§1 Point-Set Topology Review#^prop-1-5|§1.5]]

> [!remark]- Connections
> - For $G/H$ this is the openness of the projection: [[§15 The Topology of G∕H and Real Grassmannians#^prop-15-1|§15.1]] and [[§15 The Topology of G∕H and Real Grassmannians#^rem-15-1|the remark after §15.2]].

## Hausdorff Orbit Spaces

> [!theorem] Corollary §13.4: Compact Group and Compact Hausdorff Space
> If $G$ acts continuously on $X$, and $G$ and $X$ are compact and $X$ is Hausdorff, then the orbit space $X/G$ is Hausdorff.
>
> *Lee: Proposition 21.4 with Corollary 21.6, for Lie groups acting on manifolds*

^cor-13-4

> [!proof]+ Proof
> We apply the Hausdorff Criterion (Theorem [[§6 Open Quotients#^thm-6-1|§6.1]]) to the orbit relation $\sim$ on $X$. It has two hypotheses, and its conclusion is exactly that $X/{\sim} = X/G$ is $T_2$.
>
> *Hypothesis 1: $\sim$ is an open relation.* This is Lemma [[§13 Group Actions and Orbit Spaces#^lem-13-3|§13.3]], which uses only continuity of the action.
>
> *Hypothesis 2: the graph of $\sim$ is closed in $X \times X$.* The graph is
>
> $$
> \Gamma = \{\, (x, y) \in X \times X \mid x \sim y \,\} = \{\, (x, g \cdot x) \mid x \in X,\ g \in G \,\}.
> $$
>
> Consider
>
> $$
> \Psi : G \times X \longrightarrow X \times X, \qquad \Psi(g, x) = (x, g \cdot x). \tag{$\ast$}
> $$
>
> $\Psi$ is continuous by Theorem [[§3 Subspaces and Products#^thm-3-10|§3.10]], its components being the projection to $X$ and the action. Its image is $\Gamma$: a pair lies in the image iff it has the form $(x, g \cdot x)$ iff it lies in $\Gamma$. Since $G \times X$ is compact (Proposition [[§1 Point-Set Topology Review#^prop-1-8|§1.8]](3)), $\Gamma = \Psi(G \times X)$ is compact (Proposition [[§1 Point-Set Topology Review#^prop-1-8|§1.8]](2)). Since $X$ is Hausdorff, so is $X \times X$ (Theorem [[§3 Subspaces and Products#^thm-3-12|§3.12]]), and a compact subset of a Hausdorff space is closed (Proposition [[§1 Point-Set Topology Review#^prop-1-8|§1.8]](4)). So $\Gamma$ is closed.
>
> Both hypotheses of Theorem [[§6 Open Quotients#^thm-6-1|§6.1]] hold, so $X/G$ is Hausdorff.

^pf-13-4

*Uses:* [[§6 Open Quotients#^thm-6-1|§6.1]], [[§6 Open Quotients#^def-6-1|Def. §6.1]], [[§13 Group Actions and Orbit Spaces#^lem-13-3|§13.3]], [[§3 Subspaces and Products#^thm-3-10|§3.10]], [[§1 Point-Set Topology Review#^prop-1-8|§1.8]], [[§3 Subspaces and Products#^thm-3-12|§3.12]], [[Continuous Image of a Compact Space is Compact]], [[Compact Subspace of a Hausdorff Space is Closed]], [[§18 Compact Spaces#^thm-18-9|590 §18.9]]

> [!remark]- Connections
> - Applied to coset spaces in [[§15 The Topology of G∕H and Real Grassmannians#^cor-15-5|§15.5]] and to $\mathbb{RP}^{n-1} = S^{n-1}/\{\pm I\}$ in [[§15 The Topology of G∕H and Real Grassmannians#^rem-15-3|On the Index]]; the special case $\mathbb{CP}^n$ was [[§9 Complex Projective Space#^prop-9-1|§9.1]].

> [!example] Example §13.6: Compactness Is Needed: a Non-Hausdorff Orbit Space
> Let the multiplicative group $\mathbb{R}^{+}$ of positive reals act on $X = \mathbb{R}^2 \setminus \{0\}$ by
>
> $$
> t \cdot (x, y) = (tx,\, y/t).
> $$
>
> This is a continuous action ($X$ is preserved because $t > 0$, and the axioms are immediate), $X$ is Hausdorff and second countable, and the orbit relation is open by Lemma [[§13 Group Actions and Orbit Spaces#^lem-13-3|§13.3]]. Nonetheless $X/\mathbb{R}^{+}$ is *not* Hausdorff.
>
> *Lee: cf. Example 21.3*

^ex-13-6

![[m591-6-2.svg]]
*The orbits of $t \cdot (x,y) = (tx, y/t)$ in the first quadrant: the hyperbola branches $xy = c$ and the two positive half-axes. The orbit of $z_n = (1, \tfrac1n)$ also passes through $\tfrac1n \cdot z_n = (\tfrac1n, 1)$, so this one orbit has a point near $(1,0)$ and a point near $(0,1)$: $[z_n]$ converges to both $[(1,0)]$ and $[(0,1)]$, as in the proof below.*

> [!proof]+ Proof (PSet 1, Problem 3)
> The orbits of $(1,0)$ and $(0,1)$ are the positive $x$-axis $\{(t,0) \mid t>0\}$ and the positive $y$-axis $\{(0,s) \mid s>0\}$; they are distinct classes, since $t \cdot (1,0) = (t,0)$ never has a nonzero second coordinate. Consider $z_n = (1, \tfrac1n) \in X$.
>
> *$[z_n] \to [(1,0)]$.* Let $W \ni [(1,0)]$ be open. Then $\pi^{-1}(W)$ is open in $X$ and contains $(1,0)$, so it contains a box around $(1,0)$, which contains $z_n$ for all large $n$; hence $[z_n] \in \pi(\pi^{-1}(W)) = W$ eventually.
>
> *$[z_n] \to [(0,1)]$.* Acting by $t = \tfrac1n$ gives $\tfrac1n \cdot (1, \tfrac1n) = (\tfrac1n, 1)$, so $[z_n] = [(\tfrac1n, 1)]$, and the same argument applied to the representatives $(\tfrac1n, 1) \to (0,1)$ shows $[z_n]$ is eventually in every open set containing $[(0,1)]$.
>
> A sequence in a Hausdorff space has at most one limit (if $p \neq q$ had disjoint neighborhoods, the sequence could not be eventually in both), so $X/\mathbb{R}^{+}$ is not Hausdorff.

^pf-ex-13-6

*Uses:* [[§13 Group Actions and Orbit Spaces#^def-13-5|Def. §13.5]], [[§4 Quotient Spaces and Open Maps#^def-4-1|Def. §4.1]], [[§4 Quotient Spaces and Open Maps#^def-4-2|Def. §4.2]], [[§3 Subspaces and Products#^prop-3-8|§3.8]], [[§1 Point-Set Topology Review#^def-1-8|Def. §1.8]], [[§9 Hausdorff Spaces#^thm-9-3|590 §9.3]]

> [!remark] Remark: What the Example Shows
> Every hypothesis of Corollary [[§13 Group Actions and Orbit Spaces#^cor-13-4|§13.4]] except compactness of $G$ holds here, so compactness is not removable. Seen through the criterion: the relation is open, so by Theorem [[§6 Open Quotients#^thm-6-1|§6.1]] the graph $\Gamma$ must fail to be closed — and indeed $\big((1,\tfrac1n),(\tfrac1n,1)\big) \in \Gamma$ converges to $\big((1,0),(0,1)\big) \notin \Gamma$. The mechanism is that the orbits, the hyperbolas $xy = c$ together with the two half-axes, *accumulate on each other*: the hyperbola through $z_n$ approaches both axes at once. Compactness of $G$ is what prevents an orbit from running off to infinity and limiting onto a different orbit; properness is the general condition that does the same job for non-compact $G$.
>
> Note also that openness of the relation is *automatic* here (Lemma [[§13 Group Actions and Orbit Spaces#^lem-13-3|§13.3]]) and buys nothing by itself: the two hypotheses of Theorem [[§6 Open Quotients#^thm-6-1|§6.1]] are genuinely independent, and for orbit spaces it is always the closed-graph half that carries the content.

^rem-13-7

> [!theorem] Theorem §13.5: Compactness of $X$ Is Not Needed
> If a compact topological group $G$ acts continuously on a Hausdorff space $X$, then the orbit space $X/G$ is Hausdorff.
>
> *Lee: Proposition 21.4 with Corollary 21.6, for Lie groups acting on manifolds*

^thm-13-5

**Not proved in this course.** Stated in lecture as a strengthening of Corollary [[§13 Group Actions and Orbit Spaces#^cor-13-4|§13.4]], with the proof declined: “another ten minutes of point-set topology which we will not take.” The gap is exactly the step where compactness of $X$ was used — in Corollary [[§13 Group Actions and Orbit Spaces#^cor-13-4|§13.4]] it made $\Psi(G \times X) = \Gamma$ compact, hence closed; without it one shows directly that $\Gamma$ is closed, using compactness of $G$ alone (a tube-lemma argument). Corollary [[§13 Group Actions and Orbit Spaces#^cor-13-4|§13.4]] is the version proved in lecture, and it suffices for every application below, since all the groups met are compact and all the spaces are compact Hausdorff. For completeness, the tube-lemma argument is short enough to give here.

> [!proof]+ Proof of Theorem §10.5 (filled in; not from lecture)
> *(Stated in Lecture 4 — “compactness of $X$ is not strictly necessary”; filled in.)* By Lemma [[§13 Group Actions and Orbit Spaces#^lem-13-3|§13.3]] the orbit relation is open, so by Theorem [[§6 Open Quotients#^thm-6-1|§6.1]] it suffices to show that $\Gamma = \{(x, g\cdot x)\}$ is closed in $X \times X$. Let $(x, y) \notin \Gamma$, so that $g \cdot x \ne y$ for every $g \in G$. For each $g$, choose disjoint open sets $U_g \ni g \cdot x$ and $V_g \ni y$, using that $X$ is Hausdorff. By continuity of the action at $(g, x)$, choose open $A_g \ni g$ and $B_g \ni x$ with $a \cdot x' \in U_g$ for all $a \in A_g$ and $x' \in B_g$. The sets $A_g$ cover the compact $G$, so finitely many, $A_{g_1}, \ldots, A_{g_m}$, suffice; put $B = \bigcap_i B_{g_i}$ and $V = \bigcap_i V_{g_i}$, open neighbourhoods of $x$ and $y$. If some $(x', y') \in B \times V$ had $y' = a \cdot x'$, then $a \in A_{g_i}$ for some $i$, whence $y' \in U_{g_i}$; but also $y' \in V \subseteq V_{g_i}$, which is disjoint from $U_{g_i}$. So $B \times V$ misses $\Gamma$, and $\Gamma$ is closed.

^pf-13-5

*Uses:* [[§13 Group Actions and Orbit Spaces#^lem-13-3|§13.3]], [[§6 Open Quotients#^thm-6-1|§6.1]], [[§6 Open Quotients#^def-6-1|Def. §6.1]], [[§13 Group Actions and Orbit Spaces#^def-13-2|Def. §13.2]], [[§1 Point-Set Topology Review#^def-1-8|Def. §1.8]], [[§3 Subspaces and Products#^prop-3-8|§3.8]]

> [!remark]- Connections
> - The finite-subcover step is the argument of the [[Tube Lemma]] (590 §18.8), with the compact factor $G$.

> [!definition] Definition §13.6: Proper Map
> A continuous map is **proper** if the preimage of every compact set is compact.
>
> *Lee: Ch. 21, Proper Actions*

^def-13-6

> [!definition] Definition §13.7: Proper Action
> A continuous action of a topological group $G$ on a space $X$ is **proper** if the map $\Psi : G \times X \to X \times X$, $\Psi(g,x) = (x, g\cdot x)$, of $(\ast)$ in the proof of Corollary [[§13 Group Actions and Orbit Spaces#^pf-13-4|§13.4]] is proper ([[§13 Group Actions and Orbit Spaces#^def-13-6|Definition §13.6]]).
>
> *Lee: Ch. 21, Proper Actions*

^def-13-7

> [!remark] Remark: Proper Actions
> Uribe: “this is one of many theorems people are interested in on when quotient spaces are Hausdorff, and this is the simplest one.” Properness is the notion that replaces compactness of $G$ altogether: every action of a compact group on a Hausdorff space is proper, and proper actions of non-compact groups are what Lee Ch. 21 treats. He warned that his own examples will be mostly compact — “I tend to be a compact-manifold person.”

^rem-13-8

> [!remark] Remark
> Proposition [[§9 Complex Projective Space#^prop-9-1|§9.1]] is a special case: $\mathrm{U}(1) = S^1$ is compact, $S^{2n+1}$ is compact Hausdorff, and the proof given there is exactly the proof of the corollary specialized to that action.

^rem-13-9
