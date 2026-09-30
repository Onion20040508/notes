---
type: section
subject: "[[Topology]]"
chapter: 10
section: 25
munkres: "§56"
tags: [topology, math590]
---
← [[Topology §24 Covering Spaces]] · ↑ [[Topology — 10 Applications of π₁]] · [[Topology §26 Deformation Retracts and Homotopy Type]] →

> [!theorem] Theorem §25.1: Fundamental Theorem of Algebra
> Every polynomial equation $x^n + a_{n-1}x^{n-1} + \cdots + a_1 x + a_0 = 0$ with coefficients in $\mathbb{R}$ or $\mathbb{C}$, $n > 0$, has at least one root in $\mathbb{C}$.

^thm-25-1

> [!remark]- Connections
> - The same theorem in linear algebra (used there without proof): [[Fundamental theorem of algebra, first version]].

> [!proof]+ Proof
> The proof proceeds in four steps.
>
> **Step 1: The power map $f: S^1 \to S^1$, $z \mapsto z^n$, induces an injective homomorphism on $\pi_1$.**
>
> Under the [[Fundamental Group of the Circle|identification]] $\pi_1(S^1, b_0) \cong \mathbb{Z}$, the induced map $f_*: \mathbb{Z} \to \mathbb{Z}$ is multiplication by $n$: $f_*([k]) = nk$. This is injective (since $n > 0$).
>
> **Step 2: If $g: S^1 \to \mathbb{R}^2 \setminus \{0\}$ is $g(z) = z^n$, then $g$ is not nullhomotopic.**
>
> Write $g = j \circ f$ where $f: S^1 \to S^1$ is $z \mapsto z^n$ and $j: S^1 \hookrightarrow \mathbb{R}^2 \setminus \{0\}$ is the inclusion. Then $g_* = j_* \circ f_*$.
>
> By Step 1, $f_*$ is injective. Since $S^1$ is a [[Topology §26 Deformation Retracts and Homotopy Type#^def-26-1|retract]] of $\mathbb{R}^2 \setminus \{0\}$ (via $r(x) = x/|x|$, with $r \circ j = \operatorname{id}_{S^1}$), the map $j_*$ is also injective (if $j_*([a]) = [e]$, then $[a] = r_*(j_*([a])) = r_*([e]) = [e]$).
>
> So $g_* = j_* \circ f_*$ is injective, hence not trivial. By the [[Topology §24 Covering Spaces#^lem-24-12|nullhomotopy characterization lemma]], $g$ is not [[Topology §22 Homotopy of Paths#^def-22-2|nullhomotopic]].
>
> **Step 3: Special case — $|a_{n-1}| + \cdots + |a_1| + |a_0| < 1$.**
>
> We show $p(z) = z^n + a_{n-1}z^{n-1} + \cdots + a_0$ has a root in the unit ball $B^2 = \{|z| \leq 1\}$.
>
> Suppose not. Define $k: B^2 \to \mathbb{R}^2 \setminus \{0\}$ by $k(z) = z^n + a_{n-1}z^{n-1} + \cdots + a_1 z + a_0$. Since $p$ has no root in $B^2$, $k$ is well-defined (never hits $0$). Let $h = k|_{S^1}: S^1 \to \mathbb{R}^2 \setminus \{0\}$. Since $h$ extends to $k: B^2 \to \mathbb{R}^2 \setminus \{0\}$, the [[Topology §24 Covering Spaces#^lem-24-12|nullhomotopy lemma]] says $h$ is nullhomotopic.
>
> However, define $F: S^1 \times I \to \mathbb{R}^2 \setminus \{0\}$ by:
>
> $$
> F(z, t) = z^n + t(a_{n-1}z^{n-1} + \cdots + a_1 z + a_0).
> $$
>
> We verify $F(z, t) \neq 0$ for all $z \in S^1$, $t \in I$: for $|z| = 1$,
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

*Uses:* [[Fundamental Group of the Circle|§24.10]], [[Functoriality of π₁|§23.5]], [[Topology §26 Deformation Retracts and Homotopy Type#^def-26-1|Def. §26.1]], [[Topology §24 Covering Spaces#^lem-24-12|§24.12]]

> [!remark] Remark
> This proof is remarkable: a theorem about *algebra* (roots of polynomials) is proved using *topology* ($\pi_1(S^1) \cong \mathbb{Z}$ and the nullhomotopy characterization). The key ingredients are:
> - [[Fundamental Group of the Circle|π₁(S¹) ≅ ℤ]] (the power map $z^n$ induces multiplication by $n$, which is injective).
> - $S^1$ is a [[Topology §26 Deformation Retracts and Homotopy Type#^def-26-1|retract]] of $\mathbb{R}^2 \setminus \{0\}$ (so the inclusion is [[Topology §26 Deformation Retracts and Homotopy Type#^prop-26-3|injective on π₁]]).
> - The [[Topology §24 Covering Spaces#^lem-24-12|nullhomotopy lemma]] (extending to $B^2$ implies nullhomotopic implies trivial $h_*$).
> - The triangle inequality estimate $|z^n| - |a_{n-1}z^{n-1} + \cdots| > 0$ on $S^1$ (the analytic input).

^rem-25-1
