---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 10
section: 70
tags: [differentiable-manifolds, math591]
---
← [[§69 Maximal Integral Curves and Flows]] · ↑ [[· 10 Integral Curves and Flows]] · [[§71 The Exponential Map]] →

*Stage: dynamics — Vector fields whose integral curves exist for all time: the uniform time lemma, compact manifolds, actions of $\mathbb{R}$, and left-invariant fields on Lie groups.*

*Lecture 24 (the definition and the uniform time lemma) and Lecture 25 (its proof and its consequences).*

> [!definition] Definition §70.1: Complete Vector Field
> $\mathbf{X} \in \mathfrak{X}(M)$ is **complete** if $(\alpha(p), \beta(p)) = \mathbb{R}$ for every $p \in M$.
>
> *Lee: Ch. 9, Complete Vector Fields*

^def-70-1

“This is the case where there are no headaches … you can go forever, and backwards in time as well, forever.” (“The existential question is: the time domain of the universe — is it complete?”) The rotation field and the Euler field are complete; the fields of Examples [[§69 Maximal Integral Curves and Flows#^ex-69-1|§69.1]] and [[§69 Maximal Integral Curves and Flows#^ex-69-2|§69.2]] are not.

“When you're doing theory, you wonder: are there results that have the conclusion ‘this vector field is complete’? It's hard to tell in general.” “A very powerful-seeming little result”:

> [!theorem] Lemma §70.1: Uniform Time Lemma
> Let $\mathbf{X} \in \mathfrak{X}(M)$. If there is $\varepsilon > 0$ such that $(-\varepsilon, \varepsilon) \subseteq (\alpha(p), \beta(p))$ for every $p \in M$, then $\mathbf{X}$ is complete.
>
> *Lee: Lemma 9.15*

^lem-70-1

> [!proof]+ Proof
> *(Lecture 25, with the hypothesis written $(-\varepsilon, \varepsilon) \times M \subseteq \mathcal{D}$, Theorem [[§69 Maximal Integral Curves and Flows#^thm-69-4|§69.4]](2).)* By contradiction. Suppose some $p \in M$ has $\alpha(p) \neq -\infty$ or $\beta(p) \neq +\infty$; take $\beta(p) < +\infty$, “the other one is analogous.” *(Filled in: for $\alpha(p) > -\infty$, apply the argument to $-\mathbf{X}$, whose integral curves are those of $\mathbf{X}$ run backwards (Lemma [[§67 Integral Curves#^lem-67-4|§67.4]](2)), whose maximal domains are the $(-\beta(p), -\alpha(p))$, and which satisfies the same hypothesis.)* Then $\beta(p)$ is a real number; choose $t_1 \in \mathbb{R}$ with
>
> $$
> \beta(p) - \varepsilon < t_1 < \beta(p) .
> $$
>
> *(Filled in.)* $t_1 \in (\alpha(p), \beta(p))$: by hypothesis $\beta(p) \ge \varepsilon$, so $t_1 > 0 > \alpha(p)$. “This is supposed to be the end of the world, the end of time”: the idea is to relaunch the flow at $\varphi_{t_1}(p)$, which by hypothesis can run for time $\varepsilon$ and so goes past $\beta(p)$. Define
>
> $$
> c(t) = \begin{cases} \varphi_t(p), & t \in (\alpha(p), \beta(p)), \\ \varphi_{t - t_1}\big(\varphi_{t_1}(p)\big), & |t - t_1| < \varepsilon, \text{ i.e. } t_1 - \varepsilon < t < t_1 + \varepsilon . \end{cases}
> $$
>
> The second line is defined, since $(-\varepsilon, \varepsilon) \subseteq (\alpha(q), \beta(q))$ for $q = \varphi_{t_1}(p)$.
>
> *Claim: $c$ is an integral curve.* The first piece is $\varphi^p$. The second, $t \mapsto \varphi^{q}(t - t_1)$, is an integral curve by the translation lemma (Lemma [[§67 Integral Curves#^lem-67-4|§67.4]](1)). Both pieces agree at $t = t_1$, where both equal $\varphi_{t_1}(p)$, so by Proposition [[§68 Local Existence and Uniqueness#^prop-68-3|§68.3]] they agree on their whole common domain: $c$ is well defined, and it is an integral curve on $(\alpha(p), t_1 + \varepsilon)$, since being one only involves $c$ near each time. It starts at $p$, and $t_1 + \varepsilon > \beta(p)$. This contradicts the maximality of $(\alpha(p), \beta(p))$ (Proposition [[§69 Maximal Integral Curves and Flows#^prop-69-1|§69.1]]). “We thought it was the end of time, but having an $\varepsilon$ is enough to keep going forever.”

^pf-70-1

*Uses:* [[§69 Maximal Integral Curves and Flows#^thm-69-4|§69.4]], [[§67 Integral Curves#^lem-67-4|§67.4]], [[§68 Local Existence and Uniqueness#^prop-68-3|§68.3]], [[§69 Maximal Integral Curves and Flows#^prop-69-1|§69.1]]

![[m591-70-4.svg]]

*(Figure after the board.)* The maximal curve $\varphi^p$ (blue) seems to end at time $\beta(p)$; relaunched at $\varphi_{t_1}(p)$, a point less than $\varepsilon$ before the end, the flow runs for time $\varepsilon$ more (red) and passes $\beta(p)$.

![[m591-70-1.svg]]

*(Not from lecture; figure added.)* The same proof on the time axis. The maximal curve $\varphi^p$ (blue) is assumed to end at $\beta(p) < \infty$. Restarting the flow at $q = \varphi_{t_1}(p)$, with $t_1$ within $\varepsilon$ of the end, gives a curve (orange) that lives for time $\varepsilon$ on either side of $t_1$, so past $\beta(p)$. The two agree on the overlap (grey), and glued together (black) they form an integral curve from $p$ on a longer interval.

![[m591-70-a1.gif|460]]

*(Not from lecture; animation added, vault only.)* The step of the proof, repeated. Knowing only that every integral curve lives at least for $|t| < \varepsilon$ ($\varepsilon = 1.2$ here), restarting the flow at a time $t_k$ just before the end of what is known (orange dots on the curve, orange segments on the time axis) extends the curve by $2\varepsilon/3$ each time, so the known domain (blue bar) grows without bound. The field is the spiral field of the group-law animation, which is complete.

*The new homework asks for “a similar thing,” the escape lemma.*

![[m591-68-3.svg]]

*(Figure after the board.)* “The horizontal line is $M$, and then you have $\mathbb{R}$ here”: over each $p$, the maximal domain $(\alpha(p), \beta(p))$, between the graphs $t = \beta(p) > 0$ and $t = \alpha(p) < 0$. The lemma's hypothesis is that a uniform strip $(-\varepsilon, \varepsilon) \times M$ fits inside; its conclusion is that the whole of $\mathbb{R} \times M$ does. (“I always reverse the cartoon axes. Someday I'll learn.”)

Announced at the end of Lecture 24 and proved in Lecture 25 (Theorems [[§70 Complete Vector Fields#^thm-70-2|§70.2]] and [[§70 Complete Vector Fields#^thm-70-7|§70.7]] below), as consequences of Lemma [[§70 Complete Vector Fields#^lem-70-1|§70.1]]:
- every vector field on a compact manifold is complete: “compactness will assure that there is a uniform time” (Lee, Corollary 9.17);
- every left-invariant vector field on a Lie group is complete, “because you're going to be able to translate solutions” (Lee, Theorem 9.18).

The uniform time lemma (Lemma [[§70 Complete Vector Fields#^lem-70-1|§70.1]], proved in Lecture 25) says: if $(-\varepsilon, \varepsilon) \times M \subseteq \mathcal{D}$ for some $\varepsilon > 0$, “if we can fit a little strip like this, of constant width, inside $\mathcal{D}$”, then $\mathcal{D} = \mathbb{R} \times M$. “As a corollary, we're going to prove the theorem, which is a very nice theorem to have.”

> [!theorem] Theorem §70.2: Vector Fields on Compact Manifolds Are Complete
> If $M$ is compact, every $\mathbf{X} \in \mathfrak{X}(M)$ is complete.
>
> *Lee: Corollary 9.17*

^thm-70-2

“You don't have to worry about it.”

> [!proof]+ Proof
> *(Lecture 25.)* For every $p \in M$ there is a flow box $(-\varepsilon_p, \varepsilon_p) \times U_p$ with $p \in U_p$ (Lemma [[§69 Maximal Integral Curves and Flows#^lem-69-3|§69.3]]). $\{U_p\}_{p \in M}$ is an open cover of $M$, so by compactness there are $p_1, \ldots, p_k \in M$ with
>
> $$
> M = \bigcup_{j=1}^k U_{p_j} .
> $$
>
> Let $\varepsilon = \min\{ \varepsilon_{p_j} : j = 1, \ldots, k \} > 0$. *Claim: Lemma [[§70 Complete Vector Fields#^lem-70-1|§70.1]] applies with this $\varepsilon$.* For $p \in M$ there is $j$ with $p \in U_{p_j}$, so $\varphi^p$ is defined on $(-\varepsilon_{p_j}, \varepsilon_{p_j}) \supseteq (-\varepsilon, \varepsilon)$. So $\mathbf{X}$ is complete.

^pf-70-2

*Uses:* [[§69 Maximal Integral Curves and Flows#^lem-69-3|§69.3]], [[§70 Complete Vector Fields#^lem-70-1|§70.1]]

![[m591-70-5.svg]]

*(Not from lecture; figure added.)* Each point has a flow box of its own width $\varepsilon_p$, which can shrink from point to point; compactness leaves finitely many, and the smallest width is a uniform time. Lee proves more: compactly supported fields are complete (Theorem 9.16).

![[m591-70-2.svg]]

*(Not from lecture; figure added.)* The same proof in $\mathbb{R} \times M$, for $M$ a circle drawn as an interval whose ends $a$ are one point. The flow boxes have heights $\varepsilon_{p_j}$; the shortest has height $\varepsilon$, so the strip $(-\varepsilon, \varepsilon) \times M$ (dashed) lies inside the flow domain. Compactness is needed: the fields of Examples [[§69 Maximal Integral Curves and Flows#^ex-69-1|§69.1]] and [[§69 Maximal Integral Curves and Flows#^ex-69-2|§69.2]] live on noncompact manifolds and are not complete.

*Complete fields and actions of $\mathbb{R}$.* “Let's go back to the group law, but now for complete fields.” Suppose $\mathbf{X}$ is complete. Then $\mathcal{D} = \mathbb{R} \times M$, so for every $t \in \mathbb{R}$ there is a map $\varphi_t : M \to M$, and the group law holds for all $s, t$.

> [!theorem] Proposition §70.3: The Flow of a Complete Field
> Let $\mathbf{X} \in \mathfrak{X}(M)$ be complete, with flow $\varphi : \mathbb{R} \times M \to M$. Then
>
> $$
> \varphi_0 = \mathrm{id}_M, \qquad \varphi_t \circ \varphi_s = \varphi_{t + s} \quad (s, t \in \mathbb{R}), \qquad \varphi_{-t} = (\varphi_t)^{-1},
> $$
>
> and every $\varphi_t$ is a diffeomorphism of $M$. Equivalently, $\varphi$ is a smooth action of the additive group $(\mathbb{R}, +)$ on $M$ (Definition [[§13 Group Actions and Orbit Spaces#^def-13-1|§13.1]]), written $t \cdot p = \varphi_t(p)$.
>
> *Lee: Ch. 9, Flows; Theorem 9.12(c)*

^prop-70-3

> [!proof]+ Proof
> *(Lecture 25; details filled in.)* $\varphi_0(p) = \varphi^p(0) = p$. All maximal domains are $\mathbb{R}$, so Proposition [[§69 Maximal Integral Curves and Flows#^prop-69-5|§69.5]] applies for all $s, t \in \mathbb{R}$: $\varphi_t \circ \varphi_s = \varphi_{t + s}$. In particular $\varphi_{-t} \circ \varphi_t = \varphi_0 = \mathrm{id}_M = \varphi_t \circ \varphi_{-t}$, so $\varphi_t$ is a bijection with inverse $\varphi_{-t}$. Each $\varphi_t$ is smooth, as the smooth map $\varphi$ (Theorem [[§69 Maximal Integral Curves and Flows#^thm-69-4|§69.4]](2)) restricted to the slice $\{t\} \times M$; so is its inverse $\varphi_{-t}$. In the action notation, $0 \cdot p = p$ and the group law reads $t \cdot (s \cdot p) = (t + s) \cdot p$, the two conditions of Definition [[§13 Group Actions and Orbit Spaces#^def-13-1|§13.1]] for the group $(\mathbb{R}, +)$, whose identity is $0$ and whose product is $+$.

^pf-70-3

*Uses:* [[§69 Maximal Integral Curves and Flows#^prop-69-5|§69.5]], [[§69 Maximal Integral Curves and Flows#^thm-69-4|§69.4]], [[§13 Group Actions and Orbit Spaces#^def-13-1|Def. §13.1]]

“This looks a lot like a group action kind of thing, and in fact it is.” There is a clash of notations: for an action, $(t, p) \mapsto t \cdot p$; for a flow, $(t, p) \mapsto \varphi_t(p)$. “It's just a matter of notation. We get the same thing.”

> [!theorem] Lemma §70.4: A Complete Field Is Related to Itself by Its Flow
> Let $\mathbf{X} \in \mathfrak{X}(M)$ be complete, with flow $\varphi$. For every $t \in \mathbb{R}$, $\mathbf{X}$ is $\varphi_t$-related to itself: $d(\varphi_t)_p(\mathbf{X}_p) = \mathbf{X}_{\varphi_t(p)}$ for every $p \in M$.
>
> *Lee: Ch. 9, Flows*

^lem-70-4

> [!proof]+ Proof
> *(Lecture 26, a warm-up: “it's sort of the infinitesimal version of the group law.”)* Fix $t$ and $p$. To compute $d(\varphi_t)_p(\mathbf{X}_p)$ “we need a curve whose velocity is $\mathbf{X}_p$”: $\mathbf{X}_p = \frac{d}{ds}\big|_{s=0} \varphi_s(p)$. By Corollary [[§31 Tangent Vectors as Velocities of Curves#^cor-31-5|§31.5]] (applied to the curve $s \mapsto \varphi_s(p)$ and the map $\varphi_t$) and the group law (Proposition [[§70 Complete Vector Fields#^prop-70-3|§70.3]]),
>
> $$
> d(\varphi_t)_p(\mathbf{X}_p) = \frac{d}{ds}\Big|_{s=0} \varphi_t\big(\varphi_s(p)\big) = \frac{d}{ds}\Big|_{s=0} \varphi_{t+s}(p) = \mathbf{X}_{\varphi_t(p)} .
> $$
>
> The last step is the translation lemma: $s \mapsto \varphi_{t+s}(p) = \varphi^p(t + s)$ is an integral curve (Lemma [[§67 Integral Curves#^lem-67-4|§67.4]](1)), so its velocity at $s = 0$ is the value of the field at $\varphi_t(p)$. “The pushforward of $\mathbf{X}$ is $\mathbf{X}$, where it should be.”

^pf-70-4

*Uses:* [[§31 Tangent Vectors as Velocities of Curves#^cor-31-5|§31.5]], [[§70 Complete Vector Fields#^prop-70-3|§70.3]], [[§67 Integral Curves#^lem-67-4|§67.4]]

> [!definition] Definition §70.2: Infinitesimal Generator
> If $\mathbf{X} \in \mathfrak{X}(M)$ is complete, it is the **infinitesimal generator** of the $\mathbb{R}$-action $\varphi$ of Proposition [[§70 Complete Vector Fields#^prop-70-3|§70.3]].
>
> *Lee: Ch. 9, Flows*

^def-70-2

“We have shown half a theorem”: a complete vector field gives rise to an $\mathbb{R}$-action on $M$. “The converse is true. It's really an observation.”

> [!theorem] Theorem §70.5: Every Smooth $\mathbb{R}$-Action Has a Generator
> Let $\varphi : \mathbb{R} \times M \to M$ be a smooth action of $(\mathbb{R}, +)$ on $M$, written $\varphi_t(p) = \varphi^p(t) = \varphi(t, p)$. Define
>
> $$
> \mathbf{X}_p = \frac{d}{dt}\Big|_{t=0} \varphi^p(t) = \dot\varphi^p(0) \in T_pM , \qquad p \in M .
> $$
>
> Then $\mathbf{X}$ is a smooth vector field, it is complete, and its flow is $\varphi$.
>
> *Lee: Proposition 9.7*

^thm-70-5

> [!proof]+ Proof
> *(Lecture 25: “Maybe I'm making a pedagogical mistake … Let's prove it. There's something to be proved.” The smoothness of $\mathbf{X}$ and the last step, which Uribe skipped, are filled in.)*
>
> *$\mathbf{X}$ is smooth.* “These guys are defined because the action is smooth … it's like a partial derivative, and you get a vector field.” In a chart $(U, x^1, \ldots, x^m)$ around $p_0$, for $p$ near $p_0$ and $t$ near $0$ the point $\varphi(t, p)$ stays in $U$ (continuity of $\varphi$, $\varphi(0, p_0) = p_0$), and by Corollary [[§31 Tangent Vectors as Velocities of Curves#^cor-31-2|§31.2]]
>
> $$
> \mathbf{X}_p = \sum_{i=1}^m \frac{\partial (x^i \circ \varphi)}{\partial t}(0, p)\, \frac{\partial}{\partial x^i}\Big|_p ,
> $$
>
> whose coefficients are smooth functions of $p$, since $x^i \circ \varphi$ is smooth near $(0, p_0)$. So $\mathbf{X}$ is smooth near $p_0$ (Proposition [[§56 Vector Fields#^prop-56-1|§56.1]]).
>
> *The curves $\varphi^p$ are integral curves of $\mathbf{X}$.* Let $\theta$ (script $\varphi$ on the board) be the flow of $\mathbf{X}$, defined on its maximal domain $\mathcal{D}_{\mathbf{X}}$; we want $\theta = \varphi$, that is, $t \mapsto \varphi^p(t)$ is an integral curve of $\mathbf{X}$. “We know this equality only at time zero, but now we have to prove it at an arbitrary time. We have to use the group law.” Fix $s$. The action gives $\varphi_t(\varphi_s(p)) = \varphi_{t + s}(p)$ for all $t$. Take $\frac{d}{dt}\big|_{t=0}$ of both sides: on the left, by the definition of $\mathbf{X}$ at the point $\varphi_s(p)$, $\mathbf{X}_{\varphi_s(p)}$; on the right, by the chain rule in the variable $t$, the velocity of $\varphi^p$ at time $s$:
>
> $$
> \mathbf{X}_{\varphi_s(p)} = \frac{d}{dt}\Big|_{t=s} \varphi_t(p) = \dot\varphi^p(s) .
> $$
>
> So $t \mapsto \varphi_t(p)$ is an integral curve of $\mathbf{X}$ starting at $p$, “where we very much use the group law.”
>
> *$\mathbf{X}$ is complete and $\theta = \varphi$.* A student asked how we know the flow of $\mathbf{X}$ is complete; Uribe: “I can't assume that $\mathbf{X}$ is complete. It has to come out of the proof,” by the group law, which he skipped. *(Filled in, by maximality instead.)* $\varphi^p$ is an integral curve starting at $p$ defined on all of $\mathbb{R}$, so by Proposition [[§69 Maximal Integral Curves and Flows#^prop-69-1|§69.1]] the maximal domain of $p$ contains $\mathbb{R}$, and $\theta^p = \varphi^p$. This holds for every $p$: $\mathbf{X}$ is complete and $\theta = \varphi$ on $\mathcal{D}_{\mathbf{X}} = \mathbb{R} \times M$.

^pf-70-5

*Uses:* [[§31 Tangent Vectors as Velocities of Curves#^cor-31-2|§31.2]], [[§56 Vector Fields#^prop-56-1|§56.1]], [[§69 Maximal Integral Curves and Flows#^prop-69-1|§69.1]]

So complete vector fields on $M$ and smooth $\mathbb{R}$-actions on $M$ are the same thing, by $\mathbf{X} \mapsto$ its flow and $\varphi \mapsto$ its infinitesimal generator. In physics language: a time-independent dynamical law with solutions for all time is a one-parameter group of diffeomorphisms of the state space.

*Naturality of integral curves.* “Now I want to do one more thing.”

> [!theorem] Proposition §70.6: Naturality of Integral Curves
> Let $F : M \to N$ be smooth, $\mathbf{X} \in \mathfrak{X}(M)$ and $\mathbf{Y} \in \mathfrak{X}(N)$. Then $\mathbf{X}$ and $\mathbf{Y}$ are $F$-related (Definition [[§59 Related Vector Fields#^def-59-2|§59.2]]) if and only if, for every integral curve $c : I \to M$ of $\mathbf{X}$, $F \circ c : I \to N$ is an integral curve of $\mathbf{Y}$.
>
> *Lee: Proposition 9.6*

^prop-70-6

“If you have related fields, then composing integral curves of the first with $F$ will give you integral curves of $\mathbf{Y}$.”

> [!proof]+ Proof
> *(Lecture 25, $(\Rightarrow)$; $(\Leftarrow)$ filled in.)* Recall that $\mathbf{X}$ and $\mathbf{Y}$ are $F$-related if and only if $dF_p(\mathbf{X}_p) = \mathbf{Y}_{F(p)}$ for every $p \in M$. For a smooth curve $c$, the chain rule (Theorem [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]]) gives the velocity of $F \circ c$:
>
> $$
> \frac{d}{dt}(F \circ c)(t) = (F \circ c)_{\ast t}\Big(\frac{d}{dt}\Big) = dF_{c(t)}\big(\dot c(t)\big) .
> $$
>
> $(\Rightarrow)$ If $\dot c(t) = \mathbf{X}_{c(t)}$, then with $p = c(t)$, “being related means” $dF_{c(t)}(\dot c(t)) = dF_p(\mathbf{X}_p) = \mathbf{Y}_{F(c(t))}$, which by the display is the velocity of $F \circ c$ at $t$. “$\mathbf{X}$ is the velocity of integral curves, and you can use the integral curves to compute the differential of $F$ acting on $\mathbf{X}$.”
>
> $(\Leftarrow)$ Given $p \in M$, let $c$ be an integral curve of $\mathbf{X}$ starting at $p$ (Theorem [[§68 Local Existence and Uniqueness#^thm-68-2|§68.2]]). $F \circ c$ is an integral curve of $\mathbf{Y}$, so at $t = 0$, by the display, $\mathbf{Y}_{F(p)} = dF_p(\dot c(0)) = dF_p(\mathbf{X}_p)$.

^pf-70-6

*Uses:* [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]], [[§68 Local Existence and Uniqueness#^thm-68-2|§68.2]]

Lemma [[§67 Integral Curves#^lem-67-5|§67.5]] is the case of a diffeomorphism $F$ and $\mathbf{Y} = F_\ast\mathbf{X}$, the unique field $F$-related to $\mathbf{X}$ (Proposition [[§59 Related Vector Fields#^prop-59-2|§59.2]]). “But the reason I'm rushing is because there is a very important case of $F$-related fields, which is the left-invariant fields on a Lie group.”

> [!theorem] Theorem §70.7: Left-Invariant Fields Are Complete
> Every left-invariant vector field $\mathbf{X}$ on a Lie group $G$ is complete. Moreover, $\varphi^g(t) = g\, \varphi^e(t)$ for all $g \in G$ and $t \in \mathbb{R}$.
>
> *Lee: Theorem 9.18*

^thm-70-7

> [!proof]+ Proof
> *(Lecture 25, by the uniform time lemma.)* Let $\varepsilon > 0$ be such that the integral curve of $\mathbf{X}$ starting at $e \in G$ is defined for $|t| < \varepsilon$ (any $\varepsilon$ with $(-\varepsilon, \varepsilon) \subseteq (\alpha(e), \beta(e))$). Pick $g \in G$. The left translation $L_g : G \to G$ is smooth and $\mathbf{X}$ is $L_g$-related to itself (Lemma [[§60 Lie Groups and Left-Invariant Vector Fields#^lem-60-5|§60.5]]), so by Proposition [[§70 Complete Vector Fields#^prop-70-6|§70.6]]
>
> $$
> t \mapsto L_g\big(\varphi_t(e)\big) = g\, \varphi^e(t)
> $$
>
> is an integral curve of $\mathbf{X}$, “obviously also defined for the same values of $t$,” $|t| < \varepsilon$. It starts at $L_g(e) = g$, with velocity $dL_g(\mathbf{X}_e) = \mathbf{X}_g$. *(On the board: “it starts at $d(L_g)(\mathbf{X}) = \mathbf{X}_g$”; the starting point is $g$, and $\mathbf{X}_g$ is the velocity there.)* So the integral curve starting at $g$ is defined at least for $|t| < \varepsilon$, with $\varepsilon$ independent of $g$, “$g$ was arbitrary”; by Lemma [[§70 Complete Vector Fields#^lem-70-1|§70.1]], $\mathbf{X}$ is complete. *(Filled in.)* For the last statement, now $\varphi^e$ is defined on $\mathbb{R}$, and the same argument shows that $t \mapsto g\varphi^e(t)$ is an integral curve on $\mathbb{R}$ starting at $g$, so it is $\varphi^g$ (Proposition [[§69 Maximal Integral Curves and Flows#^prop-69-1|§69.1]]).

^pf-70-7

*Uses:* [[§60 Lie Groups and Left-Invariant Vector Fields#^lem-60-5|§60.5]], [[§70 Complete Vector Fields#^prop-70-6|§70.6]], [[§70 Complete Vector Fields#^lem-70-1|§70.1]], [[§69 Maximal Integral Curves and Flows#^prop-69-1|§69.1]]

![[m591-70-6.svg]]

“It says more. It says that left translating integral curves through the identity gives you integral curves through the $g$ that you translated”: the figure. For $G = \mathrm{GL}(n, \mathbb{R})$ and the left-invariant field with $\mathbf{X}_I = A$, the curve $\varphi^I(t)$ is the matrix exponential $e^{tA}$ (not yet in the course), and $\varphi^g(t) = g\, e^{tA}$.

![[m591-70-3.svg]]

*(Not from lecture; figure added.)* A worked example: the group $G = \{(a, b) : a > 0\}$ of affine maps $x \mapsto ax + b$, an open subset of $\mathbb{R}^2$ (drawn with $b$ horizontal and $a$ vertical), with product $(a, b)(a', b') = (aa', ab' + b)$ and identity $e = (1, 0)$. Since $L_{(a,b)}(a', b') = (aa', ab' + b)$ has differential $a \cdot \mathrm{id}$, the left-invariant field with $\mathbf{X}_e = (u, v)$ is $\mathbf{X}_{(a,b)} = a(u, v)$ (grey arrows; here $u = \tfrac12$, $v = 1$). Its integral curve through $e$ is $\varphi^e(t) = \big(e^{ut}, \tfrac{v}{u}(e^{ut} - 1)\big)$ (blue), defined for all $t$: as $t \to -\infty$ it approaches the missing line $a = 0$ without reaching it. The curve through $g$ is $g\,\varphi^e(t)$ (red), and $L_g$ carries $\varphi^e(1)$ to $g\,\varphi^e(1)$.


![[m591-70-a2.gif|480]]

*(Not from lecture; animation added, vault only.)* The same example moving: the blue point runs along $\varphi^e(t)$, forwards to $t = 1.4$ and back to $t = -2.5$; each red point is $g\,\varphi^e(t)$ for one of three elements $g$, joined to the blue point by the dotted $L_g$. Each red point stays on its own line, the integral curve through $g$: left translation carries the curve through $e$ to the curve through $g$, at the same times.
