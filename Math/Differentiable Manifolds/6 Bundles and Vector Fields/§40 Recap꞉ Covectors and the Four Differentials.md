---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 6
section: 40
tags: [differentiable-manifolds, math591]
---
← [[§39 Recap꞉ Germs, Derivations and Tangent Vectors]] · ↑ [[· 6 Bundles and Vector Fields]] · [[§41 The Tangent Bundle]] →

*Stage: recap — Covectors, the differential of a function, pullbacks — and the four objects that the course calls “the differential”, side by side.*

*Not from lecture: a recap written for these notes, continuing [[§39 Recap꞉ Germs, Derivations and Tangent Vectors|§39]]. Nothing here is new; every object is defined, and every fact proved, where the cross-reference points.*

Keep one picture in mind: $M$ is a surface, $f$ is the temperature on it, and you are walking on it. A tangent vector is a direction to walk in. This section is about the objects that *eat* directions.

**Step 1: covectors are linear functions on a vector space.** The dual space $V^{\ast}$ of a vector space $V$ consists of the linear maps $V \to \mathbb{R}$, its elements are called *covectors*, and a basis $(e_i)$ of $V$ has a dual basis $(\varepsilon^i)$ with $\varepsilon^i(e_j) = \delta^i_j$ ([[§20 Linear Algebra Toolkit#^def-20-1|Definitions §20.1]] and [[§20 Linear Algebra Toolkit#^def-20-2|§20.2]]). Components come out by evaluation, $\lambda = \sum_i \lambda(e_i)\, \varepsilon^i$ ([[§20 Linear Algebra Toolkit#^prop-20-2|Proposition §20.2]]). A linear map $A : V \to W$ has a dual map $A^{\ast} : W^{\ast} \to V^{\ast}$, $A^{\ast}\lambda = \lambda \circ A$, which goes *backwards* ([[§20 Linear Algebra Toolkit#^def-20-3|Definition §20.3]]).

![[§20 Linear Algebra Toolkit#^def-20-1]]

![[§20 Linear Algebra Toolkit#^def-20-2]]

![[§20 Linear Algebra Toolkit#^def-20-3]]

**Step 2: the cotangent space.** At $p \in M$, $T_p^{\ast}M = (T_pM)^{\ast}$ ([[§30 The Cotangent Space#^def-30-1|Definition §30.1]]). A covector $\alpha \in T_p^{\ast}M$ eats a direction $v \in T_pM$ and returns a number $\alpha(v)$: think of it as a price list for the first step of a walk.

![[§30 The Cotangent Space#^def-30-1]]

**Step 3: a function produces a covector, its differential.** The *differential* of $f$ at $p$ is the covector

$$
df_p \in T_p^*M, \qquad df_p(v) = v[f]
$$

([[§30 The Cotangent Space#^def-30-2|Definition §30.2]] and [[§30 The Cotangent Space#^prop-30-1|Proposition §30.1]]): feed it a direction, and it returns how fast the temperature changes that way. Officially $df_p$ is the pushforward $f_{\ast p} : T_pM \to T_{f(p)}\mathbb{R}$ followed by the identification $T_{f(p)}\mathbb{R} \cong \mathbb{R}$, so it is the differential of Step 5 of [[§39 Recap꞉ Germs, Derivations and Tangent Vectors|§39]] for the special target $N = \mathbb{R}$. In a chart the differentials $dx^i|_p$ of the coordinate functions form the basis dual to $\partial/\partial x^i|_p$, and

$$
df_p = \sum_{i=1}^m \frac{\partial f}{\partial x^i}(p)\, dx^i\big|_p
$$

([[§30 The Cotangent Space#^lem-30-2|Lemma §30.2]]); the components of any covector are found by evaluation, $\alpha = \sum_j \alpha(\partial/\partial x^j|_p)\, dx^j|_p$ ([[§30 The Cotangent Space#^cor-30-3|Corollary §30.3]]). This is the formula of multivariable calculus, but $df_p$ is *not* the gradient: turning the covector $df_p$ into a vector needs an inner product, which a manifold does not come with ([[§30 The Cotangent Space#^rem-30-2|Remark: Differential — Not Gradient]]). In $\mathbb{R}^n$ with the dot product, $df_p(v) = \nabla f(p) \cdot v$.

![[§30 The Cotangent Space#^def-30-2]]

![[§30 The Cotangent Space#^lem-30-2]]

![[§30 The Cotangent Space#^cor-30-3]]

![[m591-40-1.svg]]
*A covector drawn as a stack of parallel lines. In $\mathbb{R}^2$ (or in one tangent space, after choosing a basis) the covector $\alpha = 2\,dx + dy$ is pictured by its level lines $\{\alpha = 0\}, \{\alpha = 1\}, \ldots$; its value on an arrow is the number of lines the arrow crosses, with sign. $v = \partial_x + \partial_y$ crosses three, so $\alpha(v) = 3$; $w = 0.6\,\partial_x - 1.2\,\partial_y$ runs along the lines, so $\alpha(w) = 0$. For $\alpha = df_p$ the lines are the level sets of the linear approximation of $f$ at $p$: closely spaced lines mean a steep $f$. An arrow and a stack of lines are different kinds of objects; only an inner product turns one into the other.*

**Step 4: the cotangent space from germs alone.** The differential of $f$ depends only on $f$ to first order: $T_p^{\ast}M \cong I_p/I_p^2$, the germs vanishing at $p$ modulo those vanishing to second order, by $[[f - f(p)]] \mapsto df_p$ ([[§30 The Cotangent Space#^thm-30-8|Theorem §30.8]]). So covectors can be built from functions without mentioning tangent vectors at all — the cotangent space is “very extremely natural from the point of view of functions” ([[§30 The Cotangent Space#^rem-30-4|Remark: The Most Natural Description]]).

![[§30 The Cotangent Space#^def-30-3]]

![[§30 The Cotangent Space#^thm-30-8]]

**Step 5: covectors pull back.** For $F : M \to N$, the dual map of $F_{\ast p}$ is the *pullback of covectors* $F_p^{\ast} : T^{\ast}_{F(p)}N \to T_p^{\ast}M$, $(F_p^{\ast}\alpha)(v) = \alpha(F_{\ast p}v)$ ([[§30 The Cotangent Space#^def-30-5|Definition §30.5]]). It commutes with differentials: $F_p^{\ast}(df_{F(p)}) = d(f \circ F)_p$ ([[§30 The Cotangent Space#^prop-30-10|Proposition §30.10]]), which is the chain rule in covector form. The same symbol $F_p^{\ast}$ already denoted the pullback of germs (Step 5 of [[§39 Recap꞉ Germs, Derivations and Tangent Vectors|§39]]); the two are compatible, as [[§30 The Cotangent Space#^rem-30-5|Remark: One Symbol for Two Pullbacks]] explains.

![[§30 The Cotangent Space#^def-30-5]]

![[§30 The Cotangent Space#^prop-30-10]]

**Step 6: the word “differential”.** The course uses it for four objects. They are one idea at four levels of generality.

| Name | Symbol | Takes … to … | Defined in |
|---|---|---|---|
| differential of a map between vector spaces | $dF_p$ | a vector in $X$ to a vector in $Y$ (the Jacobian) | [[§21 The Differential of a Map Between Vector Spaces#^def-21-4\|Definition §21.4]] |
| differential (pushforward) of a smooth map | $F_{\ast p}$ | $T_pM \to T_{F(p)}N$ | [[§26 Derivations and the Abstract Tangent Space#^def-26-5\|Definition §26.5]] |
| differential of a function at $p$ | $df_p$ | $T_pM \to \mathbb{R}$, a covector | [[§30 The Cotangent Space#^def-30-2\|Definition §30.2]] |
| the operator $d$ | $d$ | a function $f$ to the one-form $df$ | [[§43 One-Forms#^prop-43-2\|Proposition §43.2]] |

How they fit: on open subsets of $\mathbb{R}^n$ the second is the first ([[§28 The Differential in Coordinates#^prop-28-5|Proposition §28.5]]); Lee writes $dF_p$ for what these notes call $F_{\ast p}$, and Uribe said in Lecture 15 that $F_{\ast p}$ “we should have called the differential of $F$ ages ago”. The third is the second for maps into $\mathbb{R}$. The fourth collects the third over all points: $df$ is the field $p \mapsto df_p$, a one-form ([[§43 One-Forms|§43]]).

**Step 7: forward and backward.** Given $F : M \to N$:

| Object | Moves | Rule |
|---|---|---|
| point $p \in M$ | forward | $p \mapsto F(p)$ |
| tangent vector $v \in T_pM$ | forward | $F_{\ast p}v \in T_{F(p)}N$ ([[§26 Derivations and the Abstract Tangent Space#^def-26-5\|Definition §26.5]]) |
| function $f$ on $N$ | backward | $F^{\ast}f = f \circ F$ on $M$ |
| germ $[g]$ at $F(p)$ | backward | $F_p^{\ast}[g] = [g \circ F]$ ([[§26 Derivations and the Abstract Tangent Space#^def-26-4\|Definition §26.4]]) |
| covector $\alpha \in T^{\ast}_{F(p)}N$ | backward | $(F_p^{\ast}\alpha)(v) = \alpha(F_{\ast p}v)$ ([[§30 The Cotangent Space#^def-30-5\|Definition §30.5]]) |

Things that *are* somewhere move forward with the points; things that *eat* move backward, because to evaluate one on $M$ you push its input forward and evaluate on $N$.

**What this chapter builds.** So far every object lives at a single point. This chapter lets the point vary. The tangent spaces are assembled into one manifold, the tangent bundle $TM$ ([[§41 The Tangent Bundle|§41]]), and the cotangent spaces into the cotangent bundle $T^{\ast}M$ ([[§42 The Cotangent Bundle|§42]]). A smooth choice of a covector at every point is a one-form; $d$ turns functions into one-forms, and $F^{\ast}$ pulls one-forms back ([[§43 One-Forms|§43]]). A smooth choice of a tangent vector at every point is a vector field, and a vector field differentiates functions everywhere at once ([[§44 Vector Fields|§44]]).

> [!example] Example §40.1: Covectors in the Plane
> Continue [[§39 Recap꞉ Germs, Derivations and Tangent Vectors#^ex-39-1|Example §39.1]]: $p = (1, 2)$, $f = x^2 y$, $v = 3\,\partial_x - \partial_y$, and $F(x, y) = (x^2, x + y)$ with $F(p) = (1, 3)$ and $F_{\ast p}v = 6\,\partial_u + 2\,\partial_w$.
> 1. *The differential of $f$.* $df_p = \partial_x f(p)\, dx + \partial_y f(p)\, dy = 4\, dx + dy$, and $df_p(v) = 4 \cdot 3 + 1 \cdot (-1) = 11 = v[f]$, as Step 3 promises.
> 2. *A covector at $F(p)$.* Let $g(u, w) = u w^2$ on the target. Then $dg_{F(p)} = w^2\, du + 2uw\, dw = 9\, du + 6\, dw$ at $(1, 3)$.
> 3. *Its pullback, by definition.* $(F_p^{\ast} dg_{F(p)})(v) = dg_{F(p)}(F_{\ast p}v) = 9 \cdot 6 + 6 \cdot 2 = 66$.
> 4. *Its pullback, by the chain rule.* $g \circ F = x^2 (x + y)^2$, with $\partial_x (g \circ F)(p) = 2x(x+y)^2 + 2x^2(x+y) = 18 + 6 = 24$ and $\partial_y (g \circ F)(p) = 2x^2(x+y) = 6$. So $d(g \circ F)_p = 24\, dx + 6\, dy$, and $d(g \circ F)_p(v) = 72 - 6 = 66$: the two agree, as [[§30 The Cotangent Space#^prop-30-10|Proposition §30.10]] says.
> 5. *The transpose.* The components of $F_p^{\ast}$ come from the *transpose* of the Jacobian: $\begin{pmatrix} 2 & 1 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 9 \\ 6 \end{pmatrix} = \begin{pmatrix} 24 \\ 6 \end{pmatrix}$. Vectors are pushed forward by the Jacobian, covectors pulled back by its transpose.

^ex-40-1

*Uses:* [[§30 The Cotangent Space#^lem-30-2|§30.2]], [[§30 The Cotangent Space#^def-30-5|Def. §30.5]], [[§30 The Cotangent Space#^prop-30-10|§30.10]], [[§28 The Differential in Coordinates#^thm-28-2|§28.2]]
