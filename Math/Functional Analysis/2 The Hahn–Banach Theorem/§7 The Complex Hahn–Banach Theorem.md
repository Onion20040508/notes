---
type: section
subject: "[[Functional Analysis]]"
chapter: 2
section: 7
tags: [functional-analysis, math556]
---
← [[§6 The Hyperplane Separation Theorem]] · ↑ [[· 2 The Hahn–Banach Theorem]] · [[§8 Normed Linear Spaces]] →

*Stage: algebra — Thread: functionals. Reduction to the real case through real parts.*

For a complex linear space the inequality $\ell(y) \le p(y)$ makes no sense, since $\ell(y)$ is complex; the correct hypothesis and conclusion use the modulus, and the homogeneity of $p$ must be strengthened to complex scalars.

> [!theorem] Theorem §7.1: Complex Hahn–Banach
> Let $X$ be a linear space over $\mathbb{C}$ and $p : X \to \mathbb{R}$ a real-valued function satisfying
> - (1) $p(ax) = |a|\, p(x)$ for all $a \in \mathbb{C}$, $x \in X$;
> - (2) $p(x + y) \le p(x) + p(y)$ for all $x, y \in X$.
>
> Let $Y$ be a linear subspace of $X$ and $\ell : Y \to \mathbb{C}$ a linear functional satisfying $|\ell(y)| \le p(y)$ for all $y \in Y$. Then $\ell$ can be extended to a linear functional on $X$ satisfying $|\ell(x)| \le p(x)$ for all $x \in X$.
>
> *Lax: §3.3, Thm 8*

^thm-7-1

> [!remark]- Connections
> - The real theorem it reduces to: [[§3 Statement and Motivation#^thm-3-2|§3.2]]. Seminorms and norms satisfy (1)–(2): [[§8 Normed Linear Spaces#^def-8-2|Def. §8.2]], [[§8 Normed Linear Spaces#^def-8-1|Def. §8.1]].

> [!theorem] Lemma §7.2: Consequences of Complex Homogeneity
> Let $p : X \to \mathbb{R}$ satisfy (1) and (2) of Theorem [[§7 The Complex Hahn–Banach Theorem#^thm-7-1|§7.1]]. Then $p(0) = 0$, $p(-x) = p(x)$ and $p(x) \ge 0$ for all $x \in X$; and, regarding $X$ as a linear space over $\mathbb{R}$, $p$ is positive homogeneous and subadditive.

^lem-7-2

> [!proof]+ Proof
> (Not covered in lecture.) (1) with $a = 0$ gives $p(0) = 0$, and with $a = -1$ gives $p(-x) = p(x)$. By (2), $0 = p(x + (-x)) \le p(x) + p(-x) = 2p(x)$. Restricting (1) to real $a \ge 0$ gives positive homogeneity, and (2) is subadditivity.

^pf-7-2

*Uses:* [[§3 Statement and Motivation#^def-3-1|Def. §3.1]]

> [!remark] Remark
> The theorem does not assume $p \ge 0$. Wu remarked that $p$ is “very often” non-negative; under complex homogeneity it is forced. (Not stated in lecture.)

^rem-7-1

> [!proof]+ Proof
> As elsewhere, $\ell$ is the given functional on $Y$ and $L$ will be its extension. Two further names are needed because the real theorem is applied to one functional while a different one is being built: $u$ below plays the role of “$\ell$ on $Y$” in Theorem [[§3 Statement and Motivation#^thm-3-2|§3.2]], and $U$ the role of “$L$” there; the complex $L$ is then assembled from $U$. The auxiliary $v$ appears only in Step 2 and is never extended. Regard $X$ also as a linear space over $\mathbb{R}$ (same set, same addition, scalar multiplication restricted to real scalars); $Y$ is then a real subspace. “Real-linear” means linear with respect to real scalars; “complex-linear” with respect to complex scalars.
>
> **Step 1: The real part of $\ell$ is real-linear.** Define $u : Y \to \mathbb{R}$ by $u(y) = \operatorname{Re} \ell(y)$. For $y, y' \in Y$ and $c \in \mathbb{R}$,
>
> $$
> u(y + y') = \operatorname{Re}\bigl(\ell(y) + \ell(y')\bigr) = u(y) + u(y'), \qquad u(cy) = \operatorname{Re}\bigl(c\,\ell(y)\bigr) = c\, u(y),
> $$
>
> the second because $c$ is real. So $u$ is a real-linear functional on $Y$. (The same holds for $\operatorname{Im} \ell$; it will not be needed separately.)
>
> **Step 2: $\ell$ is determined by $u$.** For $y \in Y$, write $\ell(y) = u(y) + i\,v(y)$ with $v(y) = \operatorname{Im} \ell(y) \in \mathbb{R}$. Since $\ell$ is complex-linear and $iy \in Y$,
>
> $$
> \ell(iy) = i\,\ell(y) = i\,u(y) - v(y).
> $$
>
> On the other hand, by definition of $u$ and $v$ applied to the vector $iy$,
>
> $$
> \ell(iy) = u(iy) + i\,v(iy).
> $$
>
> Both right-hand sides are the same complex number; comparing real parts, $u(iy) = -v(y)$. Hence
>
> $$
> \ell(y) = u(y) - i\,u(iy) \qquad \text{for all } y \in Y. \tag{2.2}
> $$
>
> **Step 3: Extend $u$ by the real theorem.** For $y \in Y$,
>
> $$
> u(y) = \operatorname{Re} \ell(y) \le |\ell(y)| \le p(y),
> $$
>
> since the real part of a complex number is at most its modulus. Also $p$ is positive homogeneous and subadditive on the real space $X$ (Lemma [[§7 The Complex Hahn–Banach Theorem#^lem-7-2|§7.2]]). So $u$ satisfies the hypotheses of Theorem [[§3 Statement and Motivation#^thm-3-2|§3.2]] on the real space $X$ with subspace $Y$, and there is a real-linear $U : X \to \mathbb{R}$ with
>
> $$
> U|_Y = u \qquad \text{and} \qquad U(x) \le p(x) \quad \text{for all } x \in X.
> $$
>
> **Step 4: Define $L$ and check it is a complex-linear extension.** Guided by (2.2), define
>
> $$
> L : X \to \mathbb{C}, \qquad L(x) = U(x) - i\, U(ix).
> $$
>
> This is meaningful since $ix \in X$. Note that $\operatorname{Re} L(x) = U(x)$, as $U$ is real-valued.
>
> *$L$ extends $\ell$.* For $y \in Y$, $iy \in Y$, so $U(y) = u(y)$ and $U(iy) = u(iy)$; then $L(y) = u(y) - i\,u(iy) = \ell(y)$ by (2.2).
>
> *$L$ is additive and real-homogeneous.* Immediate from real-linearity of $U$ and of $x \mapsto ix$: $L(x + x') = U(x + x') - iU(ix + ix') = L(x) + L(x')$, and $L(cx) = cU(x) - iU(c\,ix) = c\,L(x)$ for $c \in \mathbb{R}$.
>
> *$L(ix) = i\,L(x)$.* Using $i \cdot ix = -x$ and real-linearity of $U$,
>
> $$
> L(ix) = U(ix) - i\,U(-x) = U(ix) + i\,U(x) = i\bigl(U(x) - i\,U(ix)\bigr) = i\,L(x).
> $$
>
> *Complex homogeneity.* For $c = c_1 + i c_2$ with $c_1, c_2 \in \mathbb{R}$, using the two previous items,
>
> $$
> L(cx) = L(c_1 x + c_2\, ix) = c_1 L(x) + c_2 L(ix) = c_1 L(x) + c_2\, i\,L(x) = c\, L(x).
> $$
>
> So $L$ is a complex-linear functional on $X$ extending $\ell$.
>
> **Step 5: The bound $|L(x)| \le p(x)$.** Fix $x \in X$. If $L(x) = 0$ the bound holds since $p \ge 0$ (Lemma [[§7 The Complex Hahn–Banach Theorem#^lem-7-2|§7.2]]). Otherwise write $L(x) = |L(x)|\,e^{i\theta}$ with $\theta \in [0, 2\pi)$, and set $a = e^{-i\theta} \in \mathbb{C}$, so $|a| = 1$ and
>
> $$
> a\,L(x) = |L(x)|.
> $$
>
> By complex linearity, $a\,L(x) = L(ax)$. Thus $L(ax)$ is a non-negative real number, so it equals its own real part:
>
> $$
> L(ax) = \operatorname{Re} L(ax) = U(ax).
> $$
>
> Now apply the bound from Step 3 to the vector $ax$, then homogeneity (1) of $p$:
>
> $$
> |L(x)| = L(ax) = U(ax) \le p(ax) = |a|\,p(x) = p(x).
> $$

^pf-7-1

*Uses:* [[§3 Statement and Motivation#^thm-3-2|§3.2]], [[§7 The Complex Hahn–Banach Theorem#^lem-7-2|§7.2]]

![[m556-7-1.svg]]
*Multiplying $x$ by $a = e^{-i\theta}$ multiplies $L(x)$ by $a$, by complex linearity, rotating it onto the positive real axis. There $L(ax)$ is real, so $L(ax) = U(ax)$, and the real bound $U \le p$ applies.*

> [!remark] Remark: Why Rotate
> Step 5 is the only place the complex structure does real work. For an arbitrary $x$, $L(x)$ is complex and the real bound $U \le p$ says nothing about its modulus. The trick is to rotate $x$ by the unimodular scalar $a = e^{-i\theta}$, chosen for this one $x$, so that $L(ax)$ becomes real and non-negative; then the real bound applies to $ax$, and homogeneity of $p$ with $|a| = 1$ undoes the rotation on the right-hand side. A student proposed instead the direct route $|L(x)|^2 = U(x)^2 + U(ix)^2 \le p(x)^2 + p(ix)^2 = 2p(x)^2$; this gives only $|L(x)| \le \sqrt{2}\,p(x)$, which is too weak (and even that needs $U \ge -p$, i.e. $|U| \le p$, which follows from $U(-x) \le p(-x) = p(x)$). The rotation gets the constant $1$ because it uses the bound once, on a single well-chosen vector, rather than twice.

^rem-7-2

> [!remark]- Connections
> - The same rotation in the complex Cauchy–Schwarz inequality: [[§17 Cauchy–Schwarz and the Induced Norm#^thm-17-1|§17.1]]; as a technique: [[Functional Analysis Problem-Solving Techniques#^rem-t8|Technique 8]].
