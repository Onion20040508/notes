---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 10
section: 71
tags: [differentiable-manifolds, math591]
---
← [[§70 Complete Vector Fields]] · ↑ [[· 10 Integral Curves and Flows]] · [[§72 Lie Derivatives]] →

*Stage: Lie groups — The integral curve of a left-invariant field through the identity is a one-parameter subgroup; following it to time $1$ defines $\exp : \mathfrak{g} \to G$, the matrix exponential for linear groups, smooth and a local diffeomorphism at $0$.*

*Lecture 26. “Today's topic really is the exponential map of Lie groups.” Last time: every left-invariant field on $G$ is complete (Theorem [[§70 Complete Vector Fields#^thm-70-7|§70.7]]). “The discovery of the exponential map is … thinking about the integral curve starting at the identity. Given a left-invariant field $\mathbf{X}$, it is special.”*

*Notation.* “We have two incarnations of the Lie algebra”: the left-invariant fields with their bracket, and the tangent space at the identity (Theorem [[§60 Lie Groups and Left-Invariant Vector Fields#^thm-60-9|§60.9]]; Remark [[§61 Lie Group Morphisms and Linear Groups#^rem-61-1|remark]]). Capital letters $A, B \in T_eG = \mathfrak{g}$ are vectors at the identity, and

$$
\mathbf{X}^A = \text{the corresponding left-invariant field, with } \mathbf{X}^A_e = A, \qquad \varphi^A = \text{the flow of } \mathbf{X}^A
$$

(Definition [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-5|§60.5]]).
So $\varphi^A_t(e)$ is the integral curve of $\mathbf{X}^A$ starting at $e$, evaluated at $t$; here the superscript is the vector $A$, and the point is in parentheses. $A \mapsto \mathbf{X}^A$ is linear, since $\mathbf{X}^A_g = d(L_g)_e(A)$; in particular $\mathbf{X}^{cA} = c\,\mathbf{X}^A$.

> [!theorem] Proposition §71.1: One-Parameter Subgroups
> Let $\mathbf{X}$ be a left-invariant vector field on a Lie group $G$, with flow $\varphi$. Then for all $s, t \in \mathbb{R}$
>
> $$
> \varphi_{t+s}(e) = \varphi_s(e) \cdot \varphi_t(e),
> $$
>
> the product in $G$. So $t \mapsto \varphi_t(e)$ is a group morphism from the additive group $(\mathbb{R}, +)$ to $G$.
>
> *Lee: Theorem 20.1*

^prop-71-1

> [!proof]+ Proof
> *(Lecture 26.)* $\mathbf{X}$ is complete (Theorem [[§70 Complete Vector Fields#^thm-70-7|§70.7]]), so all these are defined. Fix $s$. $\mathbf{X}$ is $L_{\varphi_s(e)}$-related to itself, because being left-invariant means being $L_g$-related to itself for every $g$ (Lemma [[§60 Lie Groups and Left-Invariant Vector Fields#^lem-60-5|§60.5]]). So, by Proposition [[§70 Complete Vector Fields#^prop-70-6|§70.6]],
>
> $$
> t \mapsto L_{\varphi_s(e)}\big(\varphi_t(e)\big)
> $$
>
> is an integral curve of $\mathbf{X}$, and it starts at $L_{\varphi_s(e)}(e) = \varphi_s(e)$: “I'm composing an integral curve of $\mathbf{X}$ with a map, and I get an integral curve of a related field, but the related field is $\mathbf{X}$ itself.” So is $t \mapsto \varphi_{t+s}(e)$, an integral curve by the translation lemma (Lemma [[§67 Integral Curves#^lem-67-4|§67.4]](1)) with value $\varphi_s(e)$ at $t = 0$. Therefore, by uniqueness (Proposition [[§68 Local Existence and Uniqueness#^prop-68-3|§68.3]]), for all $t$,
>
> $$
> \varphi_{t+s}(e) = L_{\varphi_s(e)}\big(\varphi_t(e)\big) = \varphi_s(e) \cdot \varphi_t(e) .
> $$
>
> “It's amazing how much mileage you can get out of uniqueness.” Writing out what $L$ is, “we get for the first time the group multiplication explicitly.”

^pf-71-1

*Uses:* [[§70 Complete Vector Fields#^thm-70-7|§70.7]], [[§60 Lie Groups and Left-Invariant Vector Fields#^lem-60-5|§60.5]], [[§70 Complete Vector Fields#^prop-70-6|§70.6]], [[§67 Integral Curves#^lem-67-4|§67.4]], [[§68 Local Existence and Uniqueness#^prop-68-3|§68.3]]

This is the case $g = \varphi^e(s)$ of $\varphi^g(t) = g\,\varphi^e(t)$ in Theorem [[§70 Complete Vector Fields#^thm-70-7|§70.7]], combined with the group law $\varphi^{\varphi^e(s)}(t) = \varphi^e(t + s)$. Since $s + t = t + s$, the elements $\varphi_s(e)$ and $\varphi_t(e)$ commute: a one-parameter subgroup is abelian, even in a non-abelian $G$.

“Conversely, the converse is true: any group morphism arises this way. Let's not worry about that.” *(Filled in, for smooth morphisms.)* If $\gamma : \mathbb{R} \to G$ is a smooth group morphism and $A = \dot\gamma(0)$, then differentiating $\gamma(t + s) = \gamma(t)\gamma(s) = L_{\gamma(t)}(\gamma(s))$ in $s$ at $s = 0$ gives $\dot\gamma(t) = d(L_{\gamma(t)})_e(A) = \mathbf{X}^A_{\gamma(t)}$ (Corollary [[§31 Tangent Vectors as Velocities of Curves#^cor-31-5|§31.5]]). So $\gamma$ is the integral curve of $\mathbf{X}^A$ starting at $\gamma(0) = e$, and $\gamma(t) = \varphi^A_t(e)$. Lee, Theorem 20.1, also covers continuous morphisms.

A student asked whether this is related to orbits. “Yes. The left-invariant field $\mathbf{X}^A$ generates an $\mathbb{R}$-action, because it's a complete field” (Proposition [[§70 Complete Vector Fields#^prop-70-3|§70.3]]), “so this is the orbit of the identity.”

> [!definition] Definition §71.1: The Exponential Map
> Let $G$ be a Lie group, with Lie algebra $\mathfrak{g} = T_eG$. The **exponential map** $\exp : \mathfrak{g} \to G$ is
>
> $$
> \exp(A) = \varphi^A_t(e)\big|_{t=1}, \qquad A \in \mathfrak{g} :
> $$
>
> make $A$ into the left-invariant field $\mathbf{X}^A$, take its flow, and follow the integral curve through $e$ up to time $1$.
>
> *Lee: Ch. 20, The Exponential Map*

^def-71-1

“So the number one appears for the first time. It's not zero; it's one.”

![[m591-71-4.svg]]

*(Figure after the board.)* “I always think that the group is like a three-sphere. This is my cartoon.” The vector $A$ in the tangent space $\mathfrak{g} = T_eG$ “generates a one-parameter group, and I follow that one-parameter group to time one, and I get somewhere in the group.”

“Is there motivation behind why this is called exponential?” “Yes, very much”: for subgroups of the general linear group, $\exp$ is the matrix exponential (Theorem [[§71 The Exponential Map#^thm-71-4|§71.4]] below). “The essential step” is the following.

> [!theorem] Proposition §71.2: Exponentials of Multiples
> For all $t \in \mathbb{R}$ and $A \in \mathfrak{g}$,
>
> $$
> \exp(tA) = \varphi^A_t(e) .
> $$
>
> So $t \mapsto \exp(tA)$ is the one-parameter subgroup of Proposition [[§71 The Exponential Map#^prop-71-1|§71.1]] for $\mathbf{X}^A$.
>
> *Lee: Proposition 20.5*

^prop-71-2

> [!proof]+ Proof
> *(Lecture 26.)* For $t = 1$ this is the definition. In general, by definition,
>
> $$
> \exp(tA) = \varphi^{tA}_s(e)\big|_{s=1} :
> $$
>
> take the field $\mathbf{X}^{tA} = t\,\mathbf{X}^A$ and flow $e$ up to $s = 1$. By the rescaling lemma (Lemma [[§67 Integral Curves#^lem-67-4|§67.4]](2)) — “something that I kind of pooh-poohed at the time” — $s \mapsto \varphi^A_{ts}(e)$ is an integral curve of $t\,\mathbf{X}^A = \mathbf{X}^{tA}$, starting at $e$: “the flow of $c\mathbf{X}$ is $\varphi_{ct}$ … that's just the chain rule.” By uniqueness (Proposition [[§68 Local Existence and Uniqueness#^prop-68-3|§68.3]]) it is $s \mapsto \varphi^{tA}_s(e)$, so
>
> $$
> \exp(tA) = \varphi^{tA}_s(e)\big|_{s=1} = \varphi^A_{ts}(e)\big|_{s=1} = \varphi^A_t(e) .
> $$

^pf-71-2

*Uses:* [[§67 Integral Curves#^lem-67-4|§67.4]], [[§68 Local Existence and Uniqueness#^prop-68-3|§68.3]]

> [!theorem] Corollary §71.3: The Exponential Law on a Line
> For all $s, t \in \mathbb{R}$ and $A \in \mathfrak{g}$,
>
> $$
> \exp\big((s + t)A\big) = \exp(sA) \cdot \exp(tA) .
> $$
>
> *Lee: Proposition 20.8*

^cor-71-3

> [!proof]+ Proof
> *(Lecture 26.)* By Proposition [[§71 The Exponential Map#^prop-71-2|§71.2]], then Proposition [[§71 The Exponential Map#^prop-71-1|§71.1]], then Proposition [[§71 The Exponential Map#^prop-71-2|§71.2]] twice:
>
> $$
> \exp\big((s + t)A\big) = \varphi^A_{s+t}(e) = \varphi^A_s(e) \cdot \varphi^A_t(e) = \exp(sA) \cdot \exp(tA) .
> $$

^pf-71-3

*Uses:* [[§71 The Exponential Map#^prop-71-2|§71.2]], [[§71 The Exponential Map#^prop-71-1|§71.1]]

“This answers your question” about the name: it is an exponential law. In particular $\exp(0) = e$ and $\exp(-A) = \exp(A)^{-1}$.

> [!remark] Remark: Warning: $\exp(A + B) \neq \exp(A)\exp(B)$ in General
> “Red light. Don't generalize too much.” It is *not* true in general that
>
> $$
> \exp(A + B) = \exp(A) \cdot \exp(B) .
> $$
>
> “It's very dangerous to write things that are not true on the board, because if you are distracted, you think that I'm saying that it is true.” The reason: “there are many Lie groups that are non-abelian. This plus is the plus in the tangent space at the identity. That's commutative, but the group law is not. So this cannot possibly be true.” There is a formula for $\exp(A)\exp(B)$, “a huge, tremendous mess … a famous formula, it has people's names on it,” the Baker–Campbell–Hausdorff formula, a series of iterated brackets of $A$ and $B$. For a single direction, $A$ and $B = cA$, the identity holds (Corollary [[§71 The Exponential Map#^cor-71-3|§71.3]]); more generally, “it's not easy to show, but if $A$ and $B$ commute, then this is true. We won't go into that.” (Lee, Problem 20-8, characterizes the groups where it holds for all $A$, $B$.)
>
> *(Not from lecture.)* A concrete failure in $\mathrm{GL}(2, \mathbb{R})$, using the matrix exponential of Theorem [[§71 The Exponential Map#^thm-71-4|§71.4]]: for $A = \begin{psmallmatrix} 0 & 1 \\ 0 & 0 \end{psmallmatrix}$ and $B = \begin{psmallmatrix} 0 & 0 \\ 1 & 0 \end{psmallmatrix}$, $A^2 = B^2 = 0$, so
>
> $$
> \exp(A)\exp(B) = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}\begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix} = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}, \qquad
> \exp(A + B) = \begin{pmatrix} \cosh 1 & \sinh 1 \\ \sinh 1 & \cosh 1 \end{pmatrix},
> $$
>
> since $(A + B)^2 = I$. Here $[A, B] = AB - BA = \begin{psmallmatrix} 1 & 0 \\ 0 & -1 \end{psmallmatrix} \neq 0$.

^rem-71-1

![[m591-71-3.svg]]

*(Not from lecture; figure added.)* The two matrices of the remark acting on the unit square: $\exp(A)\exp(B)$ (blue) and $\exp(A + B)$ (red). Both have determinant $1$, so the parallelograms have the same area, but they are different maps.

> [!theorem] Theorem §71.4: The Exponential Map of a Linear Group
> Let $G \subseteq \mathrm{GL}(n, \mathbb{R})$ be a linear group (Definition [[§61 Lie Group Morphisms and Linear Groups#^def-61-1|§61.1]]) and $A \in \mathfrak{g}$, a matrix. Then
>
> $$
> \exp(A) = \sum_{\ell=0}^\infty \frac{1}{\ell!} A^\ell ,
> $$
>
> the series converging in any norm on $\operatorname{Mat}(n, \mathbb{R})$.
>
> *Lee: Proposition 20.2, Example 20.4*

^thm-71-4

> [!remark]- Connections
> - Ordinary differential equations: $x(t) = e^{tA}x_0$ solves $x' = Ax$ — [[Matrix Exponential Solution]]. Here the same series is the integral curve of the left-invariant field $\mathbf{X}^A_g = gA$ on $\mathrm{GL}(n, \mathbb{R})$, i.e. the solution of the matrix equation $\gamma' = \gamma A$, $\gamma(0) = I$.

> [!proof]+ Proof (outline from Lecture 26; to be completed after the homework)
> *(The lecture gave the case $G = \mathrm{GL}(n, \mathbb{R})$ in outline; the series facts are an exercise, and the case of a general $G \subseteq \mathrm{GL}(n, \mathbb{R})$ “needs an extra argument, and that's part of your homework.” The proof is to be filled in after the assignment is submitted.)* “What you do is once again you use uniqueness.” Show it first for $G = \mathrm{GL}(n, \mathbb{R})$. Define $e^A = \sum_{\ell \ge 0} A^\ell / \ell!$. Then
>
> $$
> \frac{d}{dt}\, e^{tA} = A\, e^{tA} = e^{tA} A ,
> $$
>
> “by manipulating the series”: “the series converges very strongly in norm, so you can differentiate inside the sum … You put a $t$ in there, differentiate, you get an $\ell$ that comes out. You can cancel a factor of the factorials. You get a shift, which is the extra $A$ that is going to come out. You can put it on the left or on the right.” So $\gamma(t) = e^{tA}$ is a curve in $\mathrm{GL}(n, \mathbb{R})$ (“it's invertible”), and
>
> $$
> \frac{d}{dt}\gamma(t) = e^{tA} A = d\big(L_{e^{tA}}\big)_e(A) = \mathbf{X}^A_{e^{tA}} ,
> $$
>
> because $L_{e^{tA}} : g \mapsto e^{tA} g$ is the restriction to $\mathrm{GL}(n, \mathbb{R})$ of a linear map, so it is its own differential (Example [[§60 Lie Groups and Left-Invariant Vector Fields#^ex-60-1|§60.1]]). With $\gamma(0) = e$, $\gamma$ is the integral curve of $\mathbf{X}^A$ starting at $e$:
>
> $$
> \left\{ \begin{aligned} \tfrac{d}{dt}\gamma(t) &= \mathbf{X}^A_{\gamma(t)} \\ \gamma(0) &= e \end{aligned} \right.
> \qquad \Longrightarrow \qquad e^{tA} = \varphi^A_t(e) ,
> $$
>
> and at $t = 1$, $e^A = \exp(A)$ by Definition [[§71 The Exponential Map#^def-71-1|§71.1]]. For a general $G \subseteq \mathrm{GL}(n, \mathbb{R})$: in the homework.

^pf-71-4

*Uses:* [[§60 Lie Groups and Left-Invariant Vector Fields#^ex-60-1|Ex. §60.1]], [[§71 The Exponential Map#^def-71-1|Def. §71.1]]

“We want to understand what is going on” with $\exp$. “For many groups, but not for all groups, this is surjective. Like for all unitary groups” — for compact connected groups, which “needs to be proved.” But globally it is not one-to-one for a compact group: “the exponential is sort of wrapping the tangent space around” the group, as $t \mapsto e^{it}$ wraps $\mathfrak{u}(1) = i\mathbb{R}$ around $\mathrm{U}(1)$. *(Not from lecture.)* Surjectivity can fail: $\exp$ takes values in the identity component, so it misses $\mathrm{O}(n) \setminus \mathrm{SO}(n)$; and even for the connected group $\mathrm{SL}(2, \mathbb{R})$ the matrix $\begin{psmallmatrix} -1 & 1 \\ 0 & -1 \end{psmallmatrix}$ is not an exponential.

![[m591-71-1.svg]]

*(Not from lecture; figure added.)* “Wrapping the tangent space around” the group, for $G = \mathrm{U}(1)$: $\mathfrak{u}(1) = i\mathbb{R}$, and $\exp(ti) = e^{it}$ (Theorem [[§71 The Exponential Map#^thm-71-4|§71.4]] with $n = 1$, complex). The segment $[0, 2\pi i]$ (blue) goes once around the circle and $[-\pi i, 0]$ (red) covers the lower half again: $\exp$ is onto but not one-to-one, while near $0$ it is one-to-one, as Proposition [[§71 The Exponential Map#^prop-71-5|§71.5]] guarantees in general.

“But one thing that is always true”:

> [!theorem] Proposition §71.5: Smoothness and the Differential at $0$
> $\exp : \mathfrak{g} \to G$ is smooth, and $d(\exp)_0 = \mathrm{Id}_{\mathfrak{g}}$, under the identifications $T_0\mathfrak{g} = \mathfrak{g}$ (Corollary [[§30 The Differential in Coordinates#^cor-30-6|§30.6]]) and $T_eG = \mathfrak{g}$. Hence $\exp$ is a local diffeomorphism at $0 \in \mathfrak{g} = T_eG$: it maps some open neighbourhood of $0$ diffeomorphically onto an open neighbourhood of $e$.
>
> *Lee: Proposition 20.8*

^prop-71-5

> [!proof]+ Proof
> *(Lecture 26. “The smoothness is a pain in the neck … but there's a very nice trick.” The smoothness of the field $\mathbf{V}$, which Uribe did not go into, is filled in.)*
>
> *1. Smoothness.* “We need to think of the flow evaluated at time one as a function of $A$, something that we have not done before. So far, we've only been considering one vector field at a time.” The trick, “used in variations”: put together all the $\mathbf{X}^A$ “as a single field over a larger space,” $G \times \mathfrak{g}$, “that includes the parameters.” Define
>
> $$
> \mathbf{V}_{(g, A)} = \big(\mathbf{X}^A_g, 0\big) \in T_gG \oplus T_A\mathfrak{g} = T_{(g, A)}(G \times \mathfrak{g}) ,
> $$
>
> using Theorem [[§31 Tangent Vectors as Velocities of Curves#^thm-31-6|§31.6]], and $T_A\mathfrak{g} = \mathfrak{g}$, “using the vector space structure.” In the second slot “I can put anything I want, kind of. But actually, we can just put zero.”
>
> *Claim: $\mathbf{V}$ is smooth* (“that's where you use the smoothness of left multiplication”). *(Filled in.)* By Lemma [[§56 Vector Fields#^lem-56-8|§56.8]] it suffices that $\mathbf{V}h$ is smooth for every $h \in C^\infty(G \times \mathfrak{g})$. With $\iota_A : G \to G \times \mathfrak{g}$, $x \mapsto (x, A)$, Theorem [[§31 Tangent Vectors as Velocities of Curves#^thm-31-6|§31.6]] gives $\mathbf{V}_{(g,A)} = (\iota_A)_{\ast}\mathbf{X}^A_g$, so
>
> $$
> (\mathbf{V}h)(g, A) = \mathbf{X}^A_g\big[h(\cdot, A)\big] = d(L_g)_e(A)\big[h(\cdot, A)\big] = A\big[x \mapsto h(gx, A)\big] .
> $$
>
> Let $\psi(g, x, A) = h(gx, A)$, smooth on $G \times G \times \mathfrak{g}$ because multiplication is smooth (Definition [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-1|§60.1]]). Take a chart $(W, y^1, \ldots, y^m)$ of $G$ at $e$ and write $A = \sum_j A^j\, \partial/\partial y^j|_e$; the coefficients $A^j$ are linear, hence smooth, functions of $A \in \mathfrak{g}$. Then
>
> $$
> (\mathbf{V}h)(g, A) = \sum_{j=1}^m A^j\, \frac{\partial \psi}{\partial y^j}(g, e, A) ,
> $$
>
> the partial derivatives of $\psi$ in the coordinates $y^j$ of the middle factor, which are smooth on $G \times W \times \mathfrak{g}$. So $\mathbf{V}h$ is smooth. (This is the trick of Proposition [[§60 Lie Groups and Left-Invariant Vector Fields#^prop-60-8|§60.8]], now with $A$ varying too.)
>
> *$\mathbf{V}$ is complete* — “because these guys are, and we're just really integrating in one variable; the other variable is not playing any role.” For $(g, A) \in G \times \mathfrak{g}$, the curve $t \mapsto \big(\varphi^A_t(g), A\big)$ has velocity $\big(\mathbf{X}^A_{\varphi^A_t(g)}, 0\big) = \mathbf{V}_{(\varphi^A_t(g), A)}$ (Theorem [[§31 Tangent Vectors as Velocities of Curves#^thm-31-6|§31.6]]: the components of a velocity are the velocities of the components), it starts at $(g, A)$, and it is defined for all $t$, since $\mathbf{X}^A$ is complete. So the flow of $\mathbf{V}$ is
>
> $$
> \Phi : \mathbb{R} \times G \times \mathfrak{g} \longrightarrow G \times \mathfrak{g}, \qquad (t, g, A) \longmapsto \big(\varphi^A_t(g), A\big),
> $$
>
> which is smooth (Theorem [[§69 Maximal Integral Curves and Flows#^thm-69-4|§69.4]](2)). Now put $t = 1$, $g = e$, and project:
>
> ![[m591-71-5.svg]]
>
> $$
> A \longmapsto \varphi^A_1(e) = \exp(A) .
> $$
>
> The composite is $\exp$, so $\exp$ is smooth. (“You want proof? I'll give you proof.”)
>
> *2. The differential at $0$.* We want $d(\exp)_0 : T_0\mathfrak{g} = \mathfrak{g} \to T_eG = \mathfrak{g}$ invertible; “in fact, it's the identity.” “How do we compute the differential of a map? We use curves, as we said months ago” (Corollary [[§31 Tangent Vectors as Velocities of Curves#^cor-31-5|§31.5]]). The straight line $t \mapsto tA$ in $\mathfrak{g}$ is at $0$ when $t = 0$, with velocity $A$; so, with Proposition [[§71 The Exponential Map#^prop-71-2|§71.2]],
>
> $$
> d(\exp)_0(A) = \frac{d}{dt}\Big|_{t=0} \exp(tA) = \frac{d}{dt}\Big|_{t=0} \varphi^A_t(e) = \mathbf{X}^A_e = A .
> $$
>
> *3. Local diffeomorphism.* $d(\exp)_0$ is bijective, so by the inverse function theorem, in the form of the proof of Theorem [[§35 Local Diffeomorphisms#^thm-35-2|§35.2]] ($\Leftarrow$) at the single point $0$, $\exp$ restricts to a diffeomorphism from an open neighbourhood of $0$ onto an open neighbourhood of $e$.

^pf-71-5

*Uses:* [[§31 Tangent Vectors as Velocities of Curves#^thm-31-6|§31.6]], [[§56 Vector Fields#^lem-56-8|§56.8]], [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-1|Def. §60.1]], [[§60 Lie Groups and Left-Invariant Vector Fields#^prop-60-8|§60.8]], [[§69 Maximal Integral Curves and Flows#^thm-69-4|§69.4]], [[§31 Tangent Vectors as Velocities of Curves#^cor-31-5|§31.5]], [[§71 The Exponential Map#^prop-71-2|§71.2]], [[§35 Local Diffeomorphisms#^thm-35-2|§35.2]]

**Transcription note (board 11/4).** The board writes $\exp : \mathfrak{g} \to A$ in the statement (for $G$), $\mathbf{V}_{(g,A)} \in (T_gG) \times \mathfrak{g} = T_A\mathfrak{g}$ (the space is $T_{(g,A)}(G \times \mathfrak{g})$), and the flow as $(t, g, A) \mapsto (\varphi^A_t(g), 0)$; the second component of the flow is $A$, which the field leaves unchanged, as above.

![[m591-71-2.svg]]

*(Not from lecture; figure added.)* $\exp$ for the group $G = \{(a, b) : a > 0\}$ of affine maps $x \mapsto ax + b$ of the example after Theorem [[§70 Complete Vector Fields#^thm-70-7|§70.7]]. With $A = (u, v) \in \mathfrak{g}$ (meaning $\mathbf{X}^A_e = (u, v)$ in the coordinates $(a, b)$), the one-parameter subgroup is $\varphi^A_t(e) = \big(e^{ut}, \tfrac{v}{u}(e^{ut} - 1)\big)$, so $\exp(u, v) = \big(e^u, \tfrac{v}{u}(e^u - 1)\big)$ ($= (1, v)$ if $u = 0$). Lines $u = \text{const}$ (blue) go to the horizontal lines $a = e^u$, lines $v = \text{const}$ (red) to curves crossing the row $a = 1$ at $b = v$, and each one-parameter subgroup is a straight ray $b = \tfrac{v}{u}(a - 1)$ through $e$, run at exponential speed; near $0$ the grid is barely distorted, which is $d(\exp)_0 = \mathrm{Id}$. Here $\exp$ is even a diffeomorphism of $\mathfrak{g}$ onto $G$: given $(a, b)$, $u = \log a$ and $v = bu/(a - 1)$.

![[m591-71-a1.gif|620]]

*(Not from lecture; animation added, vault only.)* $\exp$ as “follow the one-parameter subgroup to time $1$”, in the same group. Left: $24$ vectors $A$ on a circle in $\mathfrak{g}$, scaled by $\tau$. Right: the points $\exp(\tau A) = \varphi^A_\tau(e)$ (Proposition [[§71 The Exponential Map#^prop-71-2|§71.2]]) moving out from $e$ along their one-parameter subgroups, straight rays at exponential speed; at $\tau = 1$ the red curve is the image of the circle under $\exp$. For small $\tau$ it is nearly a round circle, which is $d(\exp)_0 = \mathrm{Id}$.

“If you take 635 next semester … you will hear the word exponential map again, but that will be for any manifold that has a Riemannian structure.” There, a tangent vector is the initial data of a geodesic, which one follows to time $1$. “To exponentiate geometrically means that you have to have a way of launching a curve given a tangent vector … Here we do it by taking these one-parameter groups; in geometry, you look at geodesics.” Next topic: Lie derivatives.
