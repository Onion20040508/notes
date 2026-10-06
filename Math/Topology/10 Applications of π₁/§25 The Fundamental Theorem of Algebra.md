---
type: section
subject: "[[Topology]]"
chapter: 10
section: 25
munkres: "§56"
tags: [topology, math590]
---
← [[§24a Lifting and the Fundamental Group of the Circle]] · ↑ [[· 10 Applications of π₁]] · [[§25a Retractions and Fixed Points]] →

> [!theorem] Theorem §25.1: Fundamental Theorem of Algebra
> Every polynomial equation $x^n + a_{n-1}x^{n-1} + \cdots + a_1 x + a_0 = 0$ with coefficients in $\mathbb{R}$ or $\mathbb{C}$, $n > 0$, has at least one root in $\mathbb{C}$.

^thm-25-1

> [!remark]- Connections
> - The same theorem in linear algebra, proved there with the extreme value theorem: [[Fundamental theorem of algebra, first version]].
> - Computational version: [[§58 Liouville's Theorem and the Fundamental Theorem of Algebra#^thm-58-2|342 Thm. §58.2]] (proof by Liouville's theorem) and [[§94 Rouché's Theorem#^ex-94-2|342 Ex. §94.2]] (proof by Rouché's theorem, the analytic form of this winding-number argument, via the argument principle [[§93 Argument Principle#^thm-93-4|342 Thm. §93.4]]).
> - Step 3 is the homotopy invariance behind Rouché's theorem, [[§94 Rouché's Theorem#^thm-94-1|342 Thm. §94.1]] (hub [[Rouché's Theorem]]): $|t(a_{n-1}z^{n-1} + \cdots + a_0)| < |z^n|$ on $S^1$ keeps the homotopy $F$ away from $0$, so $z^n$ and $p(z)$ wind equally often around $0$.

> [!proof]+ Proof
> The proof proceeds in four steps.
>
> **Step 1: The power map $f: S^1 \to S^1$, $z \mapsto z^n$, induces an injective homomorphism on $\pi_1$.**
>
> Under the [[Fundamental Group of the Circle|identification]] $\pi_1(S^1, b_0) \cong \mathbb{Z}$, the induced map $f_*: \mathbb{Z} \to \mathbb{Z}$ is multiplication by $n$: $f_*([k]) = nk$. Indeed, for the standard loop $\omega(s) = (\cos 2\pi s, \sin 2\pi s)$ the loop $f \circ \omega(s) = (\cos 2\pi n s, \sin 2\pi n s)$ lifts to $s \mapsto ns$, which ends at $n$, so $f_*([\omega]) = [\omega]^n$; since $[\omega]$ generates $\pi_1(S^1, b_0)$ ([[§24a Lifting and the Fundamental Group of the Circle#^thm-24-11|Theorem §24.11]]), $f_*([\omega]^k) = [\omega]^{nk}$. This is injective (since $n > 0$).
>
> **Step 2: If $g: S^1 \to \mathbb{R}^2 \setminus \{0\}$ is $g(z) = z^n$, then $g$ is not nullhomotopic.**
>
> Write $g = j \circ f$ where $f: S^1 \to S^1$ is $z \mapsto z^n$ and $j: S^1 \hookrightarrow \mathbb{R}^2 \setminus \{0\}$ is the inclusion. Then $g_* = j_* \circ f_*$.
>
> By Step 1, $f_*$ is injective. Since $S^1$ is a [[§25a Retractions and Fixed Points#^def-26-1|retract]] of $\mathbb{R}^2 \setminus \{0\}$ (via $r(x) = x/|x|$, with $r \circ j = \operatorname{id}_{S^1}$), the map $j_*$ is also injective (if $j_*([a]) = [e]$, then $[a] = r_*(j_*([a])) = r_*([e]) = [e]$).
>
> So $g_* = j_* \circ f_*$ is injective, hence not trivial. By the [[§24a Lifting and the Fundamental Group of the Circle#^lem-24-12|nullhomotopy characterization lemma]], $g$ is not [[§22 Homotopy of Paths#^def-22-2|nullhomotopic]].
>
> **Step 3: Special case — $|a_{n-1}| + \cdots + |a_1| + |a_0| < 1$.**
>
> We show $p(z) = z^n + a_{n-1}z^{n-1} + \cdots + a_0$ has a root in the unit ball $B^2 = \{|z| \leq 1\}$.
>
> Suppose not. Define $k: B^2 \to \mathbb{R}^2 \setminus \{0\}$ by $k(z) = z^n + a_{n-1}z^{n-1} + \cdots + a_1 z + a_0$. Since $p$ has no root in $B^2$, $k$ is well-defined (never hits $0$). Let $h = k|_{S^1}: S^1 \to \mathbb{R}^2 \setminus \{0\}$. Since $h$ extends to $k: B^2 \to \mathbb{R}^2 \setminus \{0\}$, the [[§24a Lifting and the Fundamental Group of the Circle#^lem-24-12|nullhomotopy lemma]] says $h$ is nullhomotopic.
>
> However, define $F: S^1 \times I \to \mathbb{R}^2 \setminus \{0\}$ by:
>
> $$
> F(z, t) = z^n + t(a_{n-1}z^{n-1} + \cdots + a_1 z + a_0).
> $$
>
> We verify $F(z, t) \neq 0$ for all $z \in S^1$, $t \in I$: for $|z| = 1$, the reverse triangle inequality and the triangle inequality for finite sums ([[§5 Triangle Inequality#^cor-5-2|342 Cor. §5.2]], [[§5 Triangle Inequality#^cor-5-3|342 Cor. §5.3]]) give
>
> $$
> |F(z, t)| \geq |z^n| - t(|a_{n-1}||z|^{n-1} + \cdots + |a_0|) \geq 1 - (|a_{n-1}| + \cdots + |a_0|) > 0.
> $$
>
> So $F$ is a homotopy from the power map $g(z) = z^n$ (at $t = 0$) to $h$ (at $t = 1$) in $\mathbb{R}^2 \setminus \{0\}$. This means $h \simeq g$, so $h$ is not nullhomotopic (since $g$ is not, by Step 2). Contradiction.
>
> **Step 4: General case.**
>
> Let $p(x) = x^n + a_{n-1}x^{n-1} + \cdots + a_0$. Substitute $x = cy$ for some $c \in \mathbb{R}_+$:
>
> $$
> (cy)^n + a_{n-1}(cy)^{n-1} + \cdots + a_1(cy) + a_0 = 0
> $$
>
> $$
> \Rightarrow \quad y^n + \frac{a_{n-1}}{c}\,y^{n-1} + \cdots + \frac{a_1}{c^{n-1}}\,y + \frac{a_0}{c^n} = 0.
> $$
>
> Choose $c$ large enough that $\frac{|a_{n-1}|}{c} + \frac{|a_{n-2}|}{c^2} + \cdots + \frac{|a_0|}{c^n} < 1$. By Step 3, this equation has a root $y_0$. Then $x_0 = cy_0$ is a root of the original equation.

^pf-25-1

*Uses:* [[Fundamental Group of the Circle|§24.10]], [[§24a Lifting and the Fundamental Group of the Circle#^thm-24-11|§24.11]], [[Functoriality of π₁|§23.5]], [[§25a Retractions and Fixed Points#^def-26-1|Def. §26.1]], [[§24a Lifting and the Fundamental Group of the Circle#^lem-24-12|§24.12]], [[§22 Homotopy of Paths#^def-22-2|Def. §22.2]], [[§5 Triangle Inequality#^cor-5-2|342 §5.2]], [[§5 Triangle Inequality#^cor-5-3|342 §5.3]]

![[m590-25-1.svg]]
*Step 3 for $p(z) = z^3 + 0.6z$ ($n = 3$, $\sum|a_i| = 0.6$). If $p$ had no root in the blue disk $B^2$, the red loop $h = p|_{S^1}$ would extend over $B^2$ inside $\mathbb{R}^2 \setminus \{0\}$ and so be nullhomotopic. But $F(z,t) = z^3 + t \cdot 0.6z$ (gray: $t = \tfrac12$) slides the blue loop $g(z) = z^3$, which winds three times around $0$, onto $h$ without entering the gray disk $|w| < 1 - \sum|a_i| = 0.4$. So $h \simeq g$ also winds three times around $0$ and is not nullhomotopic, so $p$ must vanish somewhere in $B^2$ (here at $z = 0$).*

> [!remark] Remark
> This proof is remarkable: a theorem about *algebra* (roots of polynomials) is proved using *topology* ($\pi_1(S^1) \cong \mathbb{Z}$ and the nullhomotopy characterization). The key ingredients are:
> - $\pi_1(S^1) \cong \mathbb{Z}$ ([[Fundamental Group of the Circle|§24.10]]) (the power map $z^n$ induces multiplication by $n$, which is injective).
> - $S^1$ is a [[§25a Retractions and Fixed Points#^def-26-1|retract]] of $\mathbb{R}^2 \setminus \{0\}$ (so the inclusion is injective on $\pi_1$, [[§25a Retractions and Fixed Points#^prop-26-3|§26.3]]).
> - The [[§24a Lifting and the Fundamental Group of the Circle#^lem-24-12|nullhomotopy lemma]] (extending to $B^2$ implies nullhomotopic implies trivial $h_*$).
> - The triangle inequality estimate $|z^n| - |a_{n-1}z^{n-1} + \cdots| > 0$ on $S^1$ (the analytic input).

^rem-25-1
